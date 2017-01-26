#lang racket
(define (clean-repl-exit func)
  (with-handlers ([exn:fail:contract? (λ (e) (displayln "bye!"))])
    (func)))

#|
  1- When you post a message on Facebook, depending on the number of people who like your post, Facebook displays different information.
  If no one likes your post, it doesn't display anything.
  If only one person likes your post, it displays: [Friend's Name] likes your post.
  If two people like your post, it displays: [Friend 1] and [Friend 2] like your post.
  If more than two people like your post, it displays: [Friend 1], [Friend 2] and [Number of Other People] others like your post.
  Write a program and continuously ask the user to enter different names, until the user presses Enter (without supplying a name). Depending on the number of names provided, display   a message based on the above pattern.
|#
(define (make-likes-message l)
  (cond
    [(= 1 (length l)) (format "~a likes your post."       (car l))]
    
    [(= 2 (length l)) (format "~a and ~a like your post." (car l) (cadr l))]
    
    [else (let        ([len (length (cdr (cdr l)))])
            (format "~a, ~a, and ~a other~a like your post."
                    (car l)
                    (cadr l)
                    len
                    (if (> len 1) "s" "")))]))

(define (facebook-repl)
  (display "enter a name! ")
  
  (let repl ([namelist '()]
             [input     (read-line)])
    
    (if (string=? "" input)
        (displayln (make-likes-message namelist))
        
        (let ()
          (display "enter another! ")
          (repl (append namelist (list input)) (read-line))))))

;; 2- Write a program and ask the user to enter their name. Use an array to reverse the name and then store the result in a new string. Display the reversed name on the console.
(define (reverse-name-repl)
  (display "enter your name! ")
  (let repl ()
    (printf "reversed: ~a\n" (list->string (reverse (string->list (read-line)))))
    (display "enter another! ")
    (repl)))

;; 3- Write a program and ask the user to enter 5 numbers. If a number has been previously entered, display an error message and ask the user to re-try. Once the user successfully enters 5 unique numbers, sort them and display the result on the console.
(define (number-sort-repl)
  (display "enter a number! ")
  (define nums '#())
  (for ([i (in-range 1 5)])
    (define input (string->number (read-line)))    
    (when (vector-member input nums)
      (displayln "you have already entered that number!"))
    (let ()
      (display "enter another! ")
      (set! nums (vector-append nums (vector input)))))
  (display (sort (vector->list nums) <)))

;; 4- Write a program and ask the user to continuously enter a number or type "Quit" to exit. The list of numbers may include duplicates. Display the unique numbers that the user has entered.
(define (uniq-numbers-repl)
  (display "enter a number! ")
  
  (let repl ([nums '()]
             [input (read-line)])
    
    (if (string=? "" input)
        (displayln (remove-duplicates (map string->number nums)))
        
        (let ()
          (display "enter another! ")
          (repl (append nums (list input)) (read-line))))))

;; 5- Write a program and ask the user to supply a list of comma separated numbers (e.g 5, 1, 9, 2, 10). If the list is empty or includes less than 5 numbers, display "Invalid List" and ask the user to re-try; otherwise, display the 3 smallest numbers in the list.

(module+ main
  (define in 0)
  (define funcs (list facebook-repl reverse-name-repl number-sort-repl uniq-numbers-repl))
  (display "Which problem? (number in 1:5 or 0 to run all) ")
  (set! in (string->number (read-line)))
  (cond
    [(member in (range 1 6)) ((list-ref funcs (- in 1)))]
    [(= 0 in) (for-each clean-repl-exit funcs)]
    [else    (displayln "Wrong! You cheating scum!")]))
#!/usr/bin/env racket
#lang racket
(require math)
(define % modulo)
(define (clean-repl-exit func)
  (with-handlers ([exn:fail:contract? (λ (e) (displayln "bye!"))])
    (func)))
;;1 - Write a program to count how many numbers between 1 and 100 are divisible by 3
;;    with no remainder.Display the count on the console.
;; count how many numbers are evenly divisible by N in range R
(define (divisible-in-range n r)
  (if (zero? n)
      (let ()
        (displayln "zero? please, no! ")
        '())
      (filter
       (λ (x) (zero? (% x n)))
       (range 1 r))))

(define (divrange-repl)
  (define r 0)
  (define n 0)
  (define result '())
  (let repl ()
    (display "enter the range! ")
    (set! r (string->number (read-line)))
    (display "enter the divisor! ")
    (set! n (string->number (read-line)))
    (set! result (divisible-in-range n r))
    (for-each (λ (i) (printf "~a % ~a = 0 \n" i n))
              result)
    (printf "numbers in range ~a divisible by ~a: ~a\n" r n (length result))
    (repl)))

;;2 - Write a program and continuously ask the user to enter a number or "ok" to 
;;    exit. Calculate the sum of all the previously entered numbers and display 
;;    it on the console.
(define (sum-repl)
  (let repl ()
    (display "enter some numbers, space separated! ")
    (printf "sum of numbers: ~a \n"
            (sum (map string->number
                      (string-split (read-line) " "))))
    (repl)))


;;3 - Write a program and ask the user to enter a number. Compute the factorial of 
;;    the number and print it on the console. For example, if the user enters 5, 
;;    the program should calculate 5 x 4 x 3 x 2 x 1 and display it as 5! = 120.
(define (fact-repl)
  (define n 0)
  (define r 0)
  (let repl ()
    (display "enter a number! ")
    (set! n (string->number (read-line)))
    (set! r (range 1 (+ 1 n)))
    (printf "~a! = ~a = ~a \n" n (string-join (map number->string r) " × ") (foldl * 1 r))
    (repl)))


;;4 - Write a program that picks a random number between 1 and 10.Give the user 4 
;;    chances to guess the number.If the user guesses the number, display “You won"; 
;;    otherwise, display “You lost". (To make sure the program is behaving correctly, 
;;    you can display the secret number on the console first.)
(define (guess-repl)
  (displayln "guess my number!")
  (define guesses 0)
  (define choice  0)
  (display "enter the upper limit! ")
  (define answer  (random (+ 1 (string->number (read-line)))))
  (let repl ()
    (display "enter the number of guesses! ")
    (set! guesses (string->number (read-line)))
    (printf "(1 / ~a) enter a guess! " guesses)
    (for ([i (in-range 2 (+ 1 guesses))])
      (set! choice (string->number (read-line)))
      #:break (= choice answer)
      (printf "(~a / ~a) that guess is ~a! enter another! "
              i
              guesses
              (if (not (member choice (range 0 answer)))
                  "not even close"
                  "wrong")))
    (displayln "Correct!")
    (repl)))

;;5 - Write a program and ask the user to enter a series of numbers separated by 
;;    comma.Find the maximum of the numbers and display it on the console. For 
;;    example, if the user enters “5, 3, 8, 1, 4", the program should display 8.
(define (max-repl)
  (let repl ()
    (display "enter some numbers, space separated! ")
    (printf "max of numbers: ~a \n"
            (foldl max 0 (map string->number
                              (string-split
                               (list->string
                                (filter (λ (c) (not (char=? c #\,)))
                                        (string->list (read-line)))) " "))))
    (repl)))


(module+ main
  (define in 0)
  (define funcs (list divrange-repl sum-repl fact-repl guess-repl max-repl))
  (display "Which problem? (number in 1:5 or 0 to run all) ")
  (set! in (string->number (read-line)))
  (cond
    [(member in (range 1 6)) ((list-ref funcs (- in 1)))]
    [(= 0 in) (for-each clean-repl-exit funcs)]
    [else    (displayln "Wrong! You cheating scum!")]))
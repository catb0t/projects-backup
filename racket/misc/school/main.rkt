#lang racket
#|
  1- Write a program and ask the user to enter a number.
  The number should be between 1 to 10.
  If the user enters a valid number, display "Valid" on the console.
  Otherwise, display "Invalid".
  (This logic is used a lot in applications where values entered into input boxes need to be validated.)

  2- Write a program which takes two numbers from the console and displays the maximum of the two.

  3- Write a program and ask the user to enter the width and height of an image.
  Then tell if the image is landscape or portrait.

  4- Your job is to write a program for a speed camera.
  For simplicity, ignore the details such as camera, sensors, etc and focus purely on the logic.
  Write a program that asks the user to enter the speed limit.
  Once set, the program asks for the speed of a car.
  If the user enters a value less than the speed limit, program should display 'OK' on the console.
  If the value is above the speed limit, the program should calculate the number of demerit points.
  For every 5 mph above the speed limit, 1 demerit points should be incurred and displayed on the console.
  If the number of demerit points is above 12, the program should display 'License Suspended'.
|#

(require math)

(define (map-reduce reduce-func map-func xs [identity 0])
  (foldl reduce-func identity (map map-func xs)))

(define (string->words str)
  (filter
   (λ (x) (not (zero? (string-length x))))
   (regexp-split #px"\\W" str)))

(define (numprompt . xs) (display "one or more real numbers, separated by spaces "))

; task 1: validate input
(define (_validate-str x [start 1] [end 10])
  (define (say-valid x) (format "valid: ~a" x))

  (let* ([r               (range start end)                                       ]
         [x-in-range?     (member (string->number x) r)                           ]
         [sum-x-in-range? (< (sum (map string->number (string->words x))) (sum r))])

    ; if more than one number is entered,
    ; and the sum of the numbers is less than the sum of the range, then it is valid
    (if (or x-in-range? sum-x-in-range?)
        (say-valid x)
        "Invalid")))

(define (get-input)
  (numprompt)
  (displayln (_validate-str (read-line))))


; task 2: max of inputs
(define (_max-of-str str)
  (map-reduce max string->number (string->words str)))

(define (get-max)
  (numprompt)
  (displayln (_max-of-str (read-line))))

; task 3: image recognition
(define (_decide-dims str)
  (let* ([l (map string->number (string->words str))]
         [x (car  l)                                ]
         [y (cadr l)                                ])
    (~a "image is " (cond [(> x y) 'landscape]
                          [(< x y) 'portrait ]
                          [(= x y) 'square   ]))))

(define (get-dims)
  (display "image dimensions as two real numbers, separated by a space ")
  (displayln (_decide-dims (read-line))))

; task 4: speed camera
(define (speed-camera)
  ; minimise duplication
  (define (prompt-number p)
    (display p)
    (string->number (read-line)))
  (let* ([limit    (prompt-number "enter the limit ")]
         [speed    (prompt-number "enter the speed of a car ")]
         [demerits (quotient (- limit speed) -5)])
    (if (zero? demerits)
        "OK"
        (format "~aDemerits: ~a"
                (if (>= demerits 12)
                    "License Suspended: "
                    "")
                demerits))))
#|

 # The above is a translation of: Python:
  def speed_camera():
   p = int(input("enter the limit ")) - int(input("enter the speed of a car ")) // -5
   return "{}".format("OK" if not p else "{}Demerits: {}".format("" if p < 12 else "License Suspended: ", p))

 ! The above is a translation of: Factor:
  : (speed-camera) ( limit speed -- demerits/f)
   2dup >= [ 2drop f ] [ - -5 /i ] if ;

  : speed-camera ( -- result)
   "enter the limit " write readln
   "enter the speed of a car " write readln
   [ string>number ] bi@ (speed-camera) dup
   [ dup 12 >= "License Suspended: " "" ? swap "%sDemerits: %s" sprintf]
   [ drop "OK" ] if ;

|#

; stick a fork in it, we're done!

; main
(module+ main
  (get-input)
  (get-max)
  (get-dims)
  (displayln (speed-camera)))
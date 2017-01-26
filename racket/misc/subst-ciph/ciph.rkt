#lang racket

(define (zip . xs)
  (apply map list xs))

(define (key-table)
  (make-hash (zip
              (map integer->char (range 97 123))
              (string->list (read-line)))))

(define k (key-table))

(define (ciph-repl)
  (displayln (list->string (map
                            (λ (x)
                              (car (hash-ref k x x)))
                            (string->list (read-line)))))
  (ciph-repl))
#lang racket

(define (thing ls)
  (if (> (length ls) 10)
      'p
      'q))

(define (thing2 ls)
  (cond
    [(> (add1 (thing2 (cdr ls))) 10) 'p]
    [else 'q]))
#lang racket
(define (sqr n) (expt n 2))

(define (pythag a b)
  (sqrt (foldl + 0 (map sqr (list a b)))))
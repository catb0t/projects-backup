#lang racket

(require urlang)

(urlang
  (urmodule sum-example
      (define (even? x) (=== (% x 2) 0))
      (var (sum 0) x (a (array 1 2 3 4 5)) (i 0) (n a.length))
      (while (< i n)
        (:= x (ref a i))
        (cond
          [(even? x)  (+= sum (ref a i))]
          [else       "skip"])
        (+= i 1))
      sum))
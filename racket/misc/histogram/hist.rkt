#lang racket
(require math)
(define (logn n x)
  (/ (log x) (log n)))

(define (H string)
  (let ([str (string->list string)])
    (sum (map
          (λ (c)
            (logn 2 (/ (length str) (count (λ (x) (char=? c x)) str))))
          str))))

(λ(S)
  (let ([s(string->list S)])
    (sum(map
         (λ(c)(/ (log (/(length s)(count
                                    (λ(x)(char=? c x))
                                    s)))
                  (log 2)))
               s))))
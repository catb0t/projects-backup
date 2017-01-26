#lang racket  ; An echo server

(define listener (tcp-listen (string->number (read-line))))
(define (mk-server)
  (let echo-server ()
    (define-values (in out) (tcp-accept listener))
    (thread
     (λ()
       (define-values (a b) (tcp-addresses out))
       (write (~a (foldl + 0(map string->number(string-split a "."))) out))
       (newline out)
       (close-output-port out)))
    (echo-server)))
;(mk-server)
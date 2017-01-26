#lang racket

(with-handlers ([exn:break:terminate? (λ(x) (displayln "broke"))])
  (for ([i (in-naturals)])
    (displayln i)
    (sleep 0.5))) ; hello

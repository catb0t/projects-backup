#lang racket/base

(module+ test
  (require rackunit rackunit/text-ui)

  (provide suite)

  (define suite
    (test-suite
     "perfect numbers tests"

     (test-equal? "return 4 perfect numbers for range 1 - 10000"
                  "string"
                  "string")))

  (run-tests suite))

(require 'test)
(suite)

#lang racket
(require net/url)
(require net/uri-codec)


(define (zip a b) (map list a b))

(define (open-url term)
  (call/input-url
   (string->url (string-append "http://" term)) ; url
   (curry get-pure-port #:redirections 5)
   port->string))

(define (parse-page term)
  (car (regexp-match
        #px"s\">About [\\d,]+ results"
        (open-url
         (string-append
          "google.com/search?nfpr=1&q="
          (uri-encode term))))))

(define (get-result term)
  (string->number
   (string-replace
    (list-ref
     (string-split
      (parse-page term)
      " ")
     1)
    "," "")))

(define (google-fite terms)
  (last (cdr
         (sort
          (zip terms (map get-result terms)))
         #:key cdr <)))
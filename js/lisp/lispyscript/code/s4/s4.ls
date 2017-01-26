(->
  (require "http")
  (.createServer
    (function (request response)
      (response.writeHead 200 {'Content-Type': 'text/plain'})
      (response.end
        (str (-> (request.socket.remoteAddress)
             (.split ".")
             (.map parseFloat)
             (.reduce (function (x y) (+ x y)))))
          '\n')
  (.listen (|| (get 2 process.argv) 1337) "127.0.0.1"))))
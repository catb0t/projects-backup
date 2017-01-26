(var http (require 'http'))
(var url  (require 'url'))
(var fs   (require 'fs'))
(var path (require 'path'))
(var port (|| (get 2 process.argv) 1337))
(var baseDir __dirname)

(->
  (http.createServer
    (function (request response)
      (try
        (var reqUrl (url.parse request.url))
        ; // use path.normalize to prevent access to dirs under basedir
        (var fsPath (str baseDir (path.normalize reqUrl.pathname)))

        (response.writeHead 200 {"Content-Type": "text/html"})
        (var fStream (fs.createReadStream fsPath))
        (fStream.pipe response)
        (fStream.on
          'error'
          (function (err)
            ; // assume enoent
            (response.writeHead 404)
            (response.end)))
        ; // catch (err)
        (function (err)
          (response.writeHead 500)
          (response.end)
          (console.log e.stack)))))
  (.listen port))

(console.log "listening on port" port)

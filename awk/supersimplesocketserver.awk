BEGIN {
  while (s = "/inet/tcp/80/0/0") {
    print"HTTP/1.1 418\n" |& s
    close(s)
  }
}
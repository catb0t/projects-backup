
main = do
  putStrLn (([n|n<-[0..],(==)=<<map(gcd n)$[product,sum]<*>[read.pure<$>show n]]!!) 50)
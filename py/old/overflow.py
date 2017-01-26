x=lambda x:x(x)
while x:
   try:x(x);
   except RuntimeError:pass
   except KeyboardInterrupt:pass

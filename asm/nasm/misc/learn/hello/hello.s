  global _start

  section .text

_start:
  mov   rax, 1
  mov   rdi, 1
  mov   rsi, mesg
  mov   rdx, 13
  syscall

  mov   eax, 60
  xor   rdi, rdi
  syscall

mesg:
  db   "Hello, World!", 10

global _start
section .text

end:
  mov rax, 60 ; sys_exit
  mov rdi, 3  ; int code
  syscall

_start:
  jmp end

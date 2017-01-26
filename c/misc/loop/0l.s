	.file	"l.c"
	.intel_syntax noprefix
# GNU C11 (Ubuntu 6.2.0-5ubuntu12) version 6.2.0 20161005 (x86_64-linux-gnu)
#	compiled by GNU C version 6.2.0 20161005, GMP version 6.1.1, MPFR version 3.1.5, MPC version 1.0.3, isl version 0.15
# GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
# options passed:  -imultiarch x86_64-linux-gnu l.c -masm=intel
# -mtune=generic -march=x86-64 -auxbase-strip 0l.s -O0
# -fno-asynchronous-unwind-tables -fverbose-asm -fstack-protector-strong
# -Wformat -Wformat-security
# options enabled:  -fPIC -fPIE -faggressive-loop-optimizations
# -fauto-inc-dec -fchkp-check-incomplete-type -fchkp-check-read
# -fchkp-check-write -fchkp-instrument-calls -fchkp-narrow-bounds
# -fchkp-optimize -fchkp-store-bounds -fchkp-use-static-bounds
# -fchkp-use-static-const-bounds -fchkp-use-wrappers -fcommon
# -fdelete-null-pointer-checks -fdwarf2-cfi-asm -fearly-inlining
# -feliminate-unused-debug-types -ffunction-cse -fgcse-lm -fgnu-runtime
# -fgnu-unique -fident -finline-atomics -fira-hoist-pressure
# -fira-share-save-slots -fira-share-spill-slots -fivopts
# -fkeep-static-consts -fleading-underscore -flifetime-dse
# -flto-odr-type-merging -fmath-errno -fmerge-debug-strings -fpeephole
# -fplt -fprefetch-loop-arrays -freg-struct-return
# -fsched-critical-path-heuristic -fsched-dep-count-heuristic
# -fsched-group-heuristic -fsched-interblock -fsched-last-insn-heuristic
# -fsched-rank-heuristic -fsched-spec -fsched-spec-insn-heuristic
# -fsched-stalled-insns-dep -fschedule-fusion -fsemantic-interposition
# -fshow-column -fsigned-zeros -fsplit-ivs-in-unroller -fssa-backprop
# -fstack-protector-strong -fstdarg-opt -fstrict-volatile-bitfields
# -fsync-libcalls -ftrapping-math -ftree-cselim -ftree-forwprop
# -ftree-loop-if-convert -ftree-loop-im -ftree-loop-ivcanon
# -ftree-loop-optimize -ftree-parallelize-loops= -ftree-phiprop
# -ftree-reassoc -ftree-scev-cprop -funit-at-a-time -fverbose-asm
# -fzero-initialized-in-bss -m128bit-long-double -m64 -m80387
# -malign-stringops -mavx256-split-unaligned-load
# -mavx256-split-unaligned-store -mfancy-math-387 -mfp-ret-in-387 -mfxsr
# -mglibc -mieee-fp -mlong-double-80 -mmmx -mno-sse4 -mpush-args -mred-zone
# -msse -msse2 -mstv -mtls-direct-seg-refs -mvzeroupper

	.text
	.globl	main
	.type	main, @function
main:
	push	rbp	#
	mov	rbp, rsp	#,
	call	main2	#
	mov	eax, 0	# _3,
	pop	rbp	#
	ret
	.size	main, .-main
	.section	.rodata
.LC0:
	.string	"%lu, %lu\n"
	.text
	.globl	loop
	.type	loop, @function
loop:
	push	rbp	#
	mov	rbp, rsp	#,
	sub	rsp, 32	#,
	mov	QWORD PTR -24[rbp], rdi	# n, n
	mov	rax, QWORD PTR -24[rbp]	# tmp89, n
	mov	QWORD PTR -8[rbp], rax	# i, tmp89
	jmp	.L4	#
.L7:
	mov	rax, QWORD PTR -8[rbp]	# tmp90, i
	and	eax, 1	# _7,
	test	rax, rax	# _7
	je	.L5	#,
	mov	rax, QWORD PTR -8[rbp]	# tmp91, i
	add	rax, 1	# iftmp.0_2,
	jmp	.L6	#
.L5:
	mov	rax, QWORD PTR -8[rbp]	# tmp92, i
	shr	rax	# iftmp.0_2
.L6:
	mov	QWORD PTR -8[rbp], rax	# i, iftmp.0_2
	mov	rdx, QWORD PTR -8[rbp]	# tmp93, i
	mov	rax, QWORD PTR -24[rbp]	# tmp94, n
	mov	rsi, rax	#, tmp94
	lea	rdi, .LC0[rip]	#,
	mov	eax, 0	#,
	call	printf@PLT	#
.L4:
	cmp	QWORD PTR -8[rbp], 0	# i,
	jne	.L7	#,
	nop
	leave
	ret
	.size	loop, .-loop
	.section	.rodata
.LC1:
	.string	"%LF, %LF\n"
	.text
	.globl	main2
	.type	main2, @function
main2:
	push	rbp	#
	mov	rbp, rsp	#,
	sub	rsp, 16	#,
	mov	edi, 100	#,
	call	fac	#
	fstp	TBYTE PTR -16[rbp]	# %sfp
	mov	edi, 10	#,
	call	fac	#
	push	QWORD PTR -8[rbp]	# %sfp
	push	QWORD PTR -16[rbp]	# %sfp
	lea	rsp, -16[rsp]	#,
	fstp	TBYTE PTR [rsp]	#
	lea	rdi, .LC1[rip]	#,
	mov	eax, 0	#,
	call	printf@PLT	#
	add	rsp, 32	#,
	nop
	leave
	ret
	.size	main2, .-main2
	.globl	fac
	.type	fac, @function
fac:
	push	rbp	#
	mov	rbp, rsp	#,
	mov	QWORD PTR -40[rbp], rdi	# n, n
	fld1
	fstp	TBYTE PTR -16[rbp]	# o
	mov	rax, QWORD PTR -40[rbp]	# tmp91, n
	mov	QWORD PTR -24[rbp], rax	# i, tmp91
	jmp	.L10	#
.L12:
	fild	QWORD PTR -24[rbp]	# i
	cmp	QWORD PTR -24[rbp], 0	# i,
	jns	.L11	#,
	fld	TBYTE PTR .LC4[rip]	#
	faddp	st(1), st	#,
.L11:
	fld	TBYTE PTR -16[rbp]	# o
	fmulp	st(1), st	#,
	fstp	TBYTE PTR -16[rbp]	# o
	sub	QWORD PTR -24[rbp], 1	# i,
.L10:
	cmp	QWORD PTR -24[rbp], 0	# i,
	jne	.L12	#,
	fld	TBYTE PTR -16[rbp]	# o
	pop	rbp	#
	ret
	.size	fac, .-fac
	.section	.rodata
	.align 16
.LC4:
	.long	0
	.long	2147483648
	.long	16447
	.long	0
	.ident	"GCC: (Ubuntu 6.2.0-5ubuntu12) 6.2.0 20161005"
	.section	.note.GNU-stack,"",@progbits

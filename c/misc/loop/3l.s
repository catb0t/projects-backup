	.file	"l.c"
	.intel_syntax noprefix
# GNU C11 (Ubuntu 6.2.0-5ubuntu12) version 6.2.0 20161005 (x86_64-linux-gnu)
#	compiled by GNU C version 6.2.0 20161005, GMP version 6.1.1, MPFR version 3.1.5, MPC version 1.0.3, isl version 0.15
# GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
# options passed:  -imultiarch x86_64-linux-gnu l.c -masm=intel
# -mtune=generic -march=x86-64 -auxbase-strip 3l.s -O3
# -fno-asynchronous-unwind-tables -fverbose-asm -fstack-protector-strong
# -Wformat -Wformat-security
# options enabled:  -fPIC -fPIE -faggressive-loop-optimizations
# -falign-labels -fauto-inc-dec -fbranch-count-reg -fcaller-saves
# -fchkp-check-incomplete-type -fchkp-check-read -fchkp-check-write
# -fchkp-instrument-calls -fchkp-narrow-bounds -fchkp-optimize
# -fchkp-store-bounds -fchkp-use-static-bounds
# -fchkp-use-static-const-bounds -fchkp-use-wrappers
# -fcombine-stack-adjustments -fcommon -fcompare-elim -fcprop-registers
# -fcrossjumping -fcse-follow-jumps -fdefer-pop
# -fdelete-null-pointer-checks -fdevirtualize -fdevirtualize-speculatively
# -fdwarf2-cfi-asm -fearly-inlining -feliminate-unused-debug-types
# -fexpensive-optimizations -fforward-propagate -ffunction-cse -fgcse
# -fgcse-after-reload -fgcse-lm -fgnu-runtime -fgnu-unique
# -fguess-branch-probability -fhoist-adjacent-loads -fident -fif-conversion
# -fif-conversion2 -findirect-inlining -finline -finline-atomics
# -finline-functions -finline-functions-called-once
# -finline-small-functions -fipa-cp -fipa-cp-alignment -fipa-cp-clone
# -fipa-icf -fipa-icf-functions -fipa-icf-variables -fipa-profile
# -fipa-pure-const -fipa-ra -fipa-reference -fipa-sra -fira-hoist-pressure
# -fira-share-save-slots -fira-share-spill-slots
# -fisolate-erroneous-paths-dereference -fivopts -fkeep-static-consts
# -fleading-underscore -flifetime-dse -flra-remat -flto-odr-type-merging
# -fmath-errno -fmerge-constants -fmerge-debug-strings
# -fmove-loop-invariants -fomit-frame-pointer -foptimize-sibling-calls
# -foptimize-strlen -fpartial-inlining -fpeephole -fpeephole2 -fplt
# -fpredictive-commoning -fprefetch-loop-arrays -free -freg-struct-return
# -freorder-blocks -freorder-functions -frerun-cse-after-loop
# -fsched-critical-path-heuristic -fsched-dep-count-heuristic
# -fsched-group-heuristic -fsched-interblock -fsched-last-insn-heuristic
# -fsched-rank-heuristic -fsched-spec -fsched-spec-insn-heuristic
# -fsched-stalled-insns-dep -fschedule-fusion -fschedule-insns2
# -fsemantic-interposition -fshow-column -fshrink-wrap -fsigned-zeros
# -fsplit-ivs-in-unroller -fsplit-paths -fsplit-wide-types -fssa-backprop
# -fssa-phiopt -fstack-protector-strong -fstdarg-opt -fstrict-aliasing
# -fstrict-overflow -fstrict-volatile-bitfields -fsync-libcalls
# -fthread-jumps -ftoplevel-reorder -ftrapping-math -ftree-bit-ccp
# -ftree-builtin-call-dce -ftree-ccp -ftree-ch -ftree-coalesce-vars
# -ftree-copy-prop -ftree-cselim -ftree-dce -ftree-dominator-opts
# -ftree-dse -ftree-forwprop -ftree-fre -ftree-loop-distribute-patterns
# -ftree-loop-if-convert -ftree-loop-im -ftree-loop-ivcanon
# -ftree-loop-optimize -ftree-loop-vectorize -ftree-parallelize-loops=
# -ftree-partial-pre -ftree-phiprop -ftree-pre -ftree-pta -ftree-reassoc
# -ftree-scev-cprop -ftree-sink -ftree-slp-vectorize -ftree-slsr -ftree-sra
# -ftree-switch-conversion -ftree-tail-merge -ftree-ter -ftree-vrp
# -funit-at-a-time -funswitch-loops -fverbose-asm -fzero-initialized-in-bss
# -m128bit-long-double -m64 -m80387 -malign-stringops
# -mavx256-split-unaligned-load -mavx256-split-unaligned-store
# -mfancy-math-387 -mfp-ret-in-387 -mfxsr -mglibc -mieee-fp
# -mlong-double-80 -mmmx -mno-sse4 -mpush-args -mred-zone -msse -msse2
# -mstv -mtls-direct-seg-refs -mvzeroupper

	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"%lu, %lu\n"
	.text
	.p2align 4,,15
	.globl	loop
	.type	loop, @function
loop:
	test	rdi, rdi	# n
	je	.L13	#,
	push	r12	#
	lea	r12, .LC0[rip]	# tmp93,
	push	rbp	#
	mov	rbp, rdi	# n, n
	push	rbx	#
	mov	rbx, rdi	# i, n
	.p2align 4,,10
	.p2align 3
.L7:
	lea	rax, 1[rbx]	# tmp92,
	mov	rdx, rbx	# tmp91, i
	mov	rsi, r12	#, tmp93
	shr	rdx	# tmp91
	and	ebx, 1	# i,
	mov	edi, 1	#,
	cmove	rax, rdx	# tmp91,, tmp92
	mov	rdx, rbp	#, n
	mov	rbx, rax	# i, tmp92
	mov	rcx, rax	#, i
	xor	eax, eax	#
	call	__printf_chk@PLT	#
	test	rbx, rbx	# i
	jne	.L7	#,
	pop	rbx	#
	pop	rbp	#
	pop	r12	#
.L13:
	rep ret
	.size	loop, .-loop
	.section	.rodata.str1.1
.LC2:
	.string	"%LF, %LF\n"
	.text
	.p2align 4,,15
	.globl	main2
	.type	main2, @function
main2:
	fld1
	sub	rsp, 24	#,
	mov	eax, 100	# i,
	.p2align 4,,10
	.p2align 3
.L16:
	mov	QWORD PTR 8[rsp], rax	# %sfp, i
	sub	rax, 1	# i,
	fild	QWORD PTR 8[rsp]	# %sfp
	fmulp	st(1), st	#,
	jne	.L16	#,
	sub	rsp, 16	#,
	movabs	rax, -2487112894215356416	#,
	lea	rsi, .LC2[rip]	#,
	fstp	TBYTE PTR [rsp]	#
	push	16404	#
	push	rax	#
	mov	edi, 1	#,
	xor	eax, eax	#
	call	__printf_chk@PLT	#
	add	rsp, 56	#,
	ret
	.size	main2, .-main2
	.section	.text.startup,"ax",@progbits
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
	sub	rsp, 8	#,
	call	main2	#
	xor	eax, eax	#
	add	rsp, 8	#,
	ret
	.size	main, .-main
	.text
	.p2align 4,,15
	.globl	fac
	.type	fac, @function
fac:
	test	rdi, rdi	# n
	fld1
	jne	.L24	#,
	jmp	.L25	#
	.p2align 4,,10
	.p2align 3
.L23:
	sub	rdi, 1	# i,
	fmulp	st(1), st	#,
	je	.L27	#,
.L24:
	mov	QWORD PTR -16[rsp], rdi	# %sfp, i
	test	rdi, rdi	# i
	fild	QWORD PTR -16[rsp]	# %sfp
	jns	.L23	#,
	sub	rdi, 1	# i,
	fadd	DWORD PTR .LC5[rip]	#
	fmulp	st(1), st	#,
	jne	.L24	#,
.L27:
	rep ret
.L25:
	rep ret
	.size	fac, .-fac
	.section	.rodata.cst4,"aM",@progbits,4
	.align 4
.LC5:
	.long	1602224128
	.ident	"GCC: (Ubuntu 6.2.0-5ubuntu12) 6.2.0 20161005"
	.section	.note.GNU-stack,"",@progbits

all: main test

main: conv.c main.c
	cc main.c -o bin/main -g

test: test_conv.c
	$(shell ./makememtest.sh)
	cc -lcriterion test_conv.c -o bin/test_conv
	cc conv_memtest.c -o bin/conv_test -g
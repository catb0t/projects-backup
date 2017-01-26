dir=$(shell basename `pwd`)

all: normal

.PHONY:
normal:
	nasm -felf $(dir).s -o $(dir).o
	gcc -m32 -nostartfiles $(dir).o -o $(dir)
	rm $(dir).o

clean:
	rm -rf $(dir).o $(dir)
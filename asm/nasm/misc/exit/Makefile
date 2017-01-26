dir=$(shell basename `pwd`)

all: clean normal

.PHONY:
normal:
	yasm -pnasm -felf64 $(dir).s -o $(dir).o
	ld $(dir).o -o $(dir)

clean:
	rm -rf $(dir).o $(dir)
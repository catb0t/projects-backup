#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <syscall.h>

int main(){
    char cmdbuf[1000];
    while (1){
        printf("Crap Shell> ");
        fgets(cmdbuf, 1000, stdin);
        system(cmdbuf);
    }
}
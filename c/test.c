#include<stdio.h>

i,j;
f(char*a){
	while(*a)putchar(*a),*++a?putchar(40),i++:0;
	while(j<i)putchar(41),j++;
}


main (void) {
	f(gets(NULL));
}


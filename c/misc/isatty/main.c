#include <stdio.h>
#include <unistd.h>
#include <sys/stat.h>

int main (void) {
	if ( isatty(1) ) {
		printf("Hello, tty %s\n", ttyname(1));
	} else {
		printf("stdout: not a typewriter: how boring\n");
	}
	return 0;
}


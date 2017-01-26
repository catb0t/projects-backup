#include <stdio.h>
#include <unistd.h>
int main(void) {
	printf("Forking...\n");
	int pid;
	if ((pid = fork()) == 0)
		printf("Child!\n");
	else printf("Parent! pid: %d\n", pid);
	return 0;
}

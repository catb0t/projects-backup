/*
 * main.cpp	$Revision: 1.3 $	$Date: 2002/11/10 16:11:00 $	MB
 */

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include "Enema.h"

int main(int argc, char **argv)
{
	if (argc < 2) {
		printf("usage: %s <filename> [arg1 arg2 ...]\n", argv[0]);
	} else {
		CEnema	enema(65536*2);
		int		index	= 2;

		enema.readProgram(argv[1]);

		while (index < argc) {
			if (isdigit(argv[index][0])) {
				enema.pushArg(atoi(argv[index++]));
			} else {
				const char	*p	= argv[index++];

				while (*p) {
					enema.pushArg(*p++);
				}
			}
		}
		
		enema.run();
	}
	
	return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <limits.h>

#define MAXLENGTH 1024

void retrieveStringInput(char *str, size_t buffersize);
int stringToInt(char *str);

void retrieveStringInput(char *str, size_t buffersize)
{
    for (;;) {
        if (fgets(str, (int) buffersize, stdin) != NULL) {
            str[strcspn(str, "\n")] = '\0';
            return;
        }
        printf("No input detected please try again...\n");
    }
}


int stringToInt(char *str)
{
    char *end = NULL;
    long number = strtol(str, &end, 10);
    if (!*end && end != str) {
        if (number <= INT_MIN || number >= INT_MAX) {
            printf("ERROR INPUT IS OUT OF RANGE FOR INTEGER VALUE, %d < number < %d\n", INT_MIN, INT_MAX);
            return 0;
        }
        return (int)number;
    }
    printf("STRING FAIILED TO CONVERT...\n");
    return 0;
}

int main(void)
{
    char number[MAXLENGTH];
    int convertNumber = 0;
    retrieveStringInput(number, sizeof number);

    if (number[0] == '0') {
        printf("Your number is: %d\n", convertNumber);
    }

    if ((convertNumber = stringToInt(number)) != 0)
        printf("YOUR NUMBER IS: %d\n", convertNumber);

    printf("Press any key to continue...\n");
    getchar();
    return 0;
}

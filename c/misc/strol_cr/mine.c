#include <stdbool.h>
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <limits.h>

#define MAXLENGTH 1024

bool    readln  (char** buf, const size_t len);
char*  conv_str (const char* const str, long* out);
void str_chomp  (char* const str);

// read a line of STDIN
bool readln (char** buf, const size_t len) {

  if ( fgets(*buf, len > INT_MAX ? INT_MAX : (int) len, stdin) != NULL) {
    str_chomp(*buf);
    return true;
  }
  return false;

}

// try to convert a string to a number or return the erroneous part
char* conv_str (const char* const str, long* out) {
  char* end   = NULL;
  long number = strtol(str, &end, 10);

  if ( end != str && !(*end) ) {
    *out = number;
    end = NULL;
  }

  return end;
}

// cut the last newline or don't
void str_chomp (char* const str) {

  if (str && (strchr(str, '\n') != NULL) ) {
    str[ strcspn(str, "\n") ] = 0;
  }
}

int main(void) {

  char* in_buf = malloc(sizeof (char) * MAXLENGTH);

  printf("Enter a number! ");

  while ( ! readln(&in_buf, MAXLENGTH) ) {
    printf("\nEnter another! ");
  }

  long out;
  char* err = conv_str(in_buf, &out);
  if ( err == NULL) {
    printf("Your number was: %ld\n", out);

  } else {
    fprintf(stderr, "That number '%s' was junk!\n", err);
  }

  free(in_buf);
  return EXIT_SUCCESS;
}

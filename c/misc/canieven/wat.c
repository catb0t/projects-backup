#include <stdio.h>
#include <string.h>
#include <stdint.h>

int main(void) {
  const char* text = "asdasdasdasdasdasdasd";
  for(int i = 0; i < (int)strlen(text); i++){
    printf("%c", (char)text[i]);
  }
  return 0;
}

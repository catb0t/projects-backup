#ifdef _WIN32
  #include <msvcrt.h>
#elif defined __linux__
  #include <unistd.h>
  #include <fcntl.h>
#endif

#include <string.h>
#include <stdlib.h>


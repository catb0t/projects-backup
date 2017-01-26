#include <iostream>

static int current = 1;

struct print {
    print() { std::cout << current++ << std::endl; }
};

int main() {
  print numbers [1000];
}

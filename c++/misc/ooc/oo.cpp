#include <iostream>

class test {
  public: test (void) { return; };
  virtual ~test(void);
  public: int a;
  private: int b;
  public: int c;
};

int main (void) {
  test* t = new test();

  delete t;
}

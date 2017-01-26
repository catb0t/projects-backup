#include <iostream>

namespace cinout {

  class cin {

public:
    cin () {}

    std::string operator ()() {
      std::string a;
      std::cin >> a;
      return a;
    }

  };

  template <typename T, typename... OtherArgs>
  class cout {

public:
    cout () {};

    void operator () () {};

    void operator ()(T&& t, OtherArgs&& ...args) {

      std::cout << std::forward<T>(t);

      this(std::forward<OtherArgs>(args)...);

    }

  };

};

using namespace cinout;

int main (void) {

  cinout::cin  cin;
  cinout::cout cout;

  std::string a = cout();

  return 0;
}
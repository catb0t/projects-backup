#include <stdexcept>
#include <exception>
#include <iostream>

using namespace std;

int main() {
  try {
    // Do not allocate exceptions on the heap using _new_.
    throw std::runtime_error("A problem occurred");
  }

  // Catch exceptions by const reference if they are objects
  catch (const std::exception& ex)
  {
      std::cout << ex.what();
  }

  // Catches any exception not caught by previous _catch_ blocks
  catch (...)
  {
      std::cout << "Unknown exception caught";
      throw; // Re-throws the exception
  }
}
#include <iostream>
#include <string>
#include <map>
using namespace std;

struct S
{
    map<string, string> m;

    S()
    {
        m["key"] = "asdasdb";
    }

    const string &func() const
    {
        return m.find("key")->second;
    }
};

int main()
{
    for (char c : S().func())
        cout << c;

    return 0;
}
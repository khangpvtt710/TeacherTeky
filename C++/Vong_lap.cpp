#include <iostream>
using namespace std;
int main()
{
    int a = -1, b = 5;
    // while
    while (a > 0)
    {
        cout << a << endl;
        a--;
    }
    // do while
    do
    {
        cout << a << endl;
    } while (a > 0);
    // for
    for (int i = 0; i < b; i++)
    {
        cout << i;
    }

    return 0;
}
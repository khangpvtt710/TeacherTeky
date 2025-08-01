// Online C++ compiler to run C++ program online
#include <iostream>
#include <string>
using namespace std;
// hàm trả về số
int tong(int a, int b)
{
    return a + b;
}
// hàm trả về chữ
string congchuoi(string a, string b)
{
    return a + b;
}
// hàm ko có giá trị trả về
void inRa()
{
    cout << "đây là hàm in ra";
}
// demo
int dem = 0;
void kiemTraSoLe(int a)
{
    if (a % 2 != 0)
    {
        cout << "là số lẻ";
        dem = 1;
    }
}
int timSoChan(int a)
{
    kiemTraSoLe(a);
    if (dem == 1)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
int main()
{
    // cout << tong(3,4);
    // cout << congchuoi("hello","Tien");
    // inRa();
    cout << timSoChan(5);
    return 0;
}
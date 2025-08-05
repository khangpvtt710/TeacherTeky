#include <iostream>
#include <string>
using namespace std;

struct SinhVien
{
    string hoTen;
    int mssv;
    int tuoi;
    float diemTrungBinh;
    string xeploai(float diemTrungBinh)
    {
        if (diemTrungBinh > 8)
        {
            return "giỏi";
        }
        else
        {
            return "khá";
        }
    }
};

int main()
{
    SinhVien sv1;
    sv1.hoTen = "Nguyen Van A";
    sv1.tuoi = 20;
    sv1.diemTrungBinh = 8.5;

    SinhVien sv2;
    sv2.hoTen = "Tiến";
    sv2.tuoi = 14;
    sv2.diemTrungBinh = 9;
    sv2.mssv = 145;
    cout << sv2.hoTen;

    return 0;
}

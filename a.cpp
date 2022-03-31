#include <iostream>
#include <string>
#include <vector>
using namespace std;

class NgayThang
{
    int ngay, thang, nam;

public:
    NgayThang()
    {
        ngay = 1;
        thang = 1;
        nam = 1;
    }

    NgayThang(int nm, int th, int ng)
    {
        this->ngay = ng;
        this->thang = th;
        this->nam = nm;
    }
    bool check()
    {
        if (this->ngay <= 0)
            return false;

        switch (this->thang)
        {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
        {
            if (this->ngay <= 31)
                return true;
            else
                return false;
        }
        case 4:
        case 6:
        case 9:
        case 11:
        {
            if (this->ngay <= 30)
                return true;
            else
                return false;
        }
        case 2:
        {
            if (this->nam % 400 == 0 || (this->nam % 4 == 0 && !this->nam % 100 != 0))
            {
                if (this->ngay <= 29)
                    return true;
                else
                    return false;
            }

            if (this->ngay <= 29)
                return true;
            else
                return false;
        }

        default:
            return false;
        }
    }

    friend istream &operator>>(istream &in, NgayThang &n)
    {
        int d, m, y;

        while (1)
        {

            cout << "Moi nhap nam: ";
            cin >> y;
            cout << "Moi nhap thang: ";
            cin >> m;

            cout << "Moi nhap ngay: ";
            cin >> d;

            n.ngay = d;
            n.thang = m;
            n.nam = y;

            if (n.check())
                break;
            else
                cout << "Nhap sai, moi nhap lai!!!" << endl;
        }
        return in;
    }
    friend ostream &operator<<(ostream &out, const NgayThang &n)
    {
        out << n.ngay << "/" << n.thang << "/" << n.nam;
        return out;
    }
};

class DocGia
{
    string ma, hoTen;
    NgayThang ngayHetHan;
    bool gioiTinh;

public:
    DocGia()
    {
        ma = "";
        hoTen = "";
        ngayHetHan = NgayThang();
        gioiTinh = 0;
    }
    DocGia(const DocGia &a)
    {
        ma = a.ma;
        hoTen = a.hoTen;
        ngayHetHan = a.ngayHetHan;
        gioiTinh = a.gioiTinh;
    }
    virtual int Phi();
    virtual void nhap()
    {
        cout << "Moi nhap thong tin cua doc gia" << endl;
        cout << "Moi nhap ma doc gia: ";
        cin >> ma;
        cin.ignore();
        cout << "Moi nhap ho ten doc gia: ";
        getline(cin, hoTen, '\n');
        cout << "Moi nhap ngay het han" << endl;
        cin >> ngayHetHan;
        cout << "Moi nhap gioi tinh cua doc gia(0/1): ";
        cin >> gioiTinh;
    }
    virtual void xuat()
    {
        cout << "Ma doc gia: " << ma << endl;
        cout << "Ho ten doc gia: " << hoTen << endl;
        cout << "Ngay het han: " << ngayHetHan << endl;
        cout << "Gioi tinh cua doc gia: " << gioiTinh << endl;
    }
};
class DocGiaThuong : public DocGia
{
    int soLuong;

public:
    DocGiaThuong() : DocGia()
    {
        soLuong = 0;
    }
    DocGiaThuong(const DocGiaThuong &a) : DocGia()
    {
        soLuong = a.soLuong;
    }
    int Phi()
    {
        return soLuong * 5000;
    }
    void nhap()
    {
        DocGia::nhap();
        cout << "Moi nhap so luong sach: ";
        cin >> soLuong;
    }
    void xuat()
    {
        DocGia::xuat();
        cout << "So luong sach: " << soLuong << endl;
    }
};
class DocGiaVIP : public DocGia
{
public:
    DocGiaVIP() : DocGia() {}
    DocGiaVIP(const DocGiaVIP &a) : DocGia() {}
    int Phi()
    {
        return 50000;
    }
    void nhap()
    {
        DocGia::nhap();
    }
    void xuat()
    {
        DocGia::xuat();
    }
};

class ThuVien
{
    vector<DocGia> a;

public:
    void nhap()
    {
        cout << "Moi nhap so luong doc gia: ";
    };
    int tongLePhi()
    {
        int s = 0;
        for (auto i : a)
        {
            s += i.Phi();
        }
        return s;
    }

    DocGia maxDocGia()
    {
        int lp = a[0].Phi();
        int index = 0;
        for (int i = 1; i < a.size(); i++)
        {
            if (a[i].Phi() > lp)
                lp = a[i].Phi();
            index = i;
        }
        return a[index];
    }
    vector<DocGia> tren30k(){
        vector<DocGia> t;
        for (auto i : a)
        {
            if (i.Phi() > 30000){
                t.push_back(i);
            }
        }
        return t;
    }
};

int main()
{

    return 0;
}

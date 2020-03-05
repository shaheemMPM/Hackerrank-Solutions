#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int a;
    long b;
    char c;
    float d;
    double e;
    cin>>a>>b>>c>>d>>e;
    cout<<a<<"\n";
    cout<<b<<"\n";
    cout<<c<<"\n";
    std::cout << std::fixed;
    std::cout << std::setprecision(3);
    std::cout << d;
    cout<<"\n";
    std::cout << std::fixed;
    std::cout << std::setprecision(9);
    std::cout << e;
    return 0;
}

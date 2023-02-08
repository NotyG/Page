// #include <algorithm>
#include <iostream>
// #include <fstream>
// #include <vector>

using namespace std;

long long count = 0;
int dif;
void countWays(int num, int lev) {
    if (lev == 8) {
        count++;
        return;
    }
    if (num - dif >= 0) countWays(num - dif, lev + 1);
    if (num + dif <= 9) countWays(num + dif, lev + 1);
}

int main() {
    dif = 2;
    count = 0;
    int sumCount = 0;
    for (int i = 1; i <= 9; i++) {
        countWays(i, 1);
        cout << i << ' ' << count << '\n';
        sumCount += count;
        count = 0;
    }
    count = 0;
    dif = 8;
    cout << "sum " << sumCount << '\n';
    for (int i = 1; i <= 9; i++) {
        countWays(i, 1);
        cout << i << ' ' << count << '\n';
        sumCount += count;
        count = 0;
    }
    cout << "Total Sum " << sumCount << '\n';
    return 0;
}
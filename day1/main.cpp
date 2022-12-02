/* This is how C++ was supposed to be written
 */

#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

template <class R, typename T> R comp (T i, T j) { return (i>j); }

int main(int argc, char **argv) {
    ifstream input("input.txt");

    vector<int> m;
    string line;
    int r = 0;
    while (!getline(input, line).eof()) {
        if (line == "\0") {
            m.push_back(r);
            r = 0;
        } else {
            r += stoi(line);
        }
    }

    sort<vector<int>::iterator>(m.begin(), m.end(), &comp<bool, int>);

    int s = 0;
    vector<int>::const_iterator rit = m.begin(); 
    for (int i = 0; i < 3; i++) {
        s += *(rit++);
    }

    cout << s << endl;

    return 0;
}

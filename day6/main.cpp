#include <stdio.h>
#include <set>
#include <deque>
#include <set>

using namespace std;

int p2() {
    char inc;
    FILE *fp = fopen("in.txt", "r"); 
    deque<char> window;

    for (int i = 0; i < 13; i++) {
        window.push_back(fgetc(fp));
    }

    int iter = 13;

    while ( (inc = fgetc(fp)) != EOF) {
        iter++;
        window.push_back(inc); // 1
        set<char> st(window.begin(), window.end()); // 4
        if (st.size() == 14) {
            printf("%d\n", iter);
            break;
        }
        window.pop_front(); // 1
    }

    fclose(fp);

    return 0;
}

int p1() {
    char inc;
    FILE *fp = fopen("in.txt", "r"); 
    deque<char> window;

    for (int i = 0; i < 3; i++) {
        window.push_back(fgetc(fp));
    }

    int iter = 3;

    while ( (inc = fgetc(fp)) != EOF) {
        iter++;
        window.push_back(inc); // 1
        set<char> st(window.begin(), window.end()); // 4
        if (st.size() == 4) {
            printf("%d\n", iter);
            break;
        }
        window.pop_front(); // 1
    }

    fclose(fp);

    return 0;
}

#include <iostream>
#include <fstream>
#include <string>

// C++ version
int p1_alt() {
    ifstream input("in.txt");
    string line;
    getline(input, line);
    int count = 3;
    for (auto i = line.begin();;i++) {
        set<char> st(i, i+4);
        count++;
        if (st.size() == 4) break;
    }
    cout << count << endl;
    input.close();
    return 0;
}

// C++ version
int p2_alt() {
    ifstream input("in.txt");
    string line;
    getline(input, line);
    int count = 13;
    for (auto i = line.begin();;i++) {
        set<char> st(i, i+14);
        count++;
        if (st.size() == 14) break;
    }
    cout << count << endl;
    input.close();
    return 0;
}

int main() {
    p1();
    p1_alt();
    p2();
    p2_alt();
}

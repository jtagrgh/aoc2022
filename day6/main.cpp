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
    bool done = false;

    while ( (inc = fgetc(fp)) != EOF && !done) {
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
    bool done = false;

    while ( (inc = fgetc(fp)) != EOF && !done) {
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

int main() {
    p1();
    p2();
}

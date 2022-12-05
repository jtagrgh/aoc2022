#include <string.h>
#include <stdio.h>
#include <stack>
#include <deque>

using namespace std;

int p2() {
    FILE *fp = fopen("in.txt", "r");
    char line[1000];

    deque<char> stacks[9];

    int itr = 0;
    for (int i = 0; i < 8*9; i ++) {
        fscanf(fp, "%s\n", line);
        if (line[1] != '0') {
            stacks[itr % 9].push_back(line[1]);
        } 
        itr++;
    }

    stack<char> iter;

    int m1, m2, m3;
    while (fscanf(fp, "%*s %d %*s %d %*s %d\n", &m1, &m2, &m3) != EOF) {
        for (int i = 0; i < m1; i++) {
            iter.push(stacks[m2-1].front());
            stacks[m2-1].pop_front();
        }
        while(!iter.empty()){
            stacks[m3-1].push_front(iter.top());
            iter.pop();
        }
    }

    for (int i = 0; i < 9; i ++) {
        printf("%c", stacks[i].front());
    }
    printf("\n");

    fclose(fp);

    return 0;
}

int p1() {
    FILE *fp = fopen("in.txt", "r");
    char line[1000];

    deque<char> stacks[9];

    int itr = 0;
    for (int i = 0; i < 8*9; i ++) {
        fscanf(fp, "%s\n", line);
        if (line[1] != '0') {
            stacks[itr % 9].push_back(line[1]);
        } 
        itr++;
    }

    int m1, m2, m3;
    while (fscanf(fp, "%*s %d %*s %d %*s %d\n", &m1, &m2, &m3) != EOF) {
        for (int i = 0; i < m1; i++) {
            stacks[m3-1].push_front(stacks[m2-1].front());
            stacks[m2-1].pop_front();
        }
    }

    for (int i = 0; i < 9; i ++) {
        printf("%c", stacks[i].front());
    }
    printf("\n");

    fclose(fp);

    return 0;
}

int main() {
    p1();
    p2();
}

#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <string.h>

using namespace std;

int p1() {
    FILE *fp = fopen("in.txt", "r");
    char c;

    int width;
    int length;

    int grid[100][100];
    int w = 0;
    int l = 0;

    while ( (c = getc(fp)) != EOF) {
        if (c == '\n') {
            l++;
            if (w > width) width = w;
            w = 0;
        } else {
            grid[l][w++] = c - '0';
        }
    }

    length = l;

    int total = 0;

    for (int i = 1; i < length - 1; i ++) {
        for (int j = 1; j < width - 1; j++) {
            int is_vis = 4;
            int check = grid[i][j];

            for (int k = 0; k < i; k++) {
                if (grid[k][j] >= check) {
                    is_vis--;
                    break;
                }
            }

            for (int k = i+1; k < length; k++) {
                if (grid[k][j] >= check) {
                    is_vis--;
                    break;
                }
            }

            for (int l = 0; l < j; l++) {
                if (grid[i][l] >= check) {
                    is_vis--;
                    break;
                }
            }

            for (int l = j+1; l < width; l++) {
                if (grid[i][l] >= check) {
                    is_vis--;
                    break;
                }
            }

            if (is_vis) {
                total++;
            }
        }
    }

    total += 2 * width + 2 * (length - 2);

    cout << total << endl;

    return 0;
}

int p2() {
    FILE *fp = fopen("in.txt", "r");
    char c;

    int grid[100][100];
    int width = 0;

    while ( (c = getc(fp)) != '\n') {
        grid[0][width++] = c - '0';
    }

    int length = 1;
    int i = 0;

    while ( (c = getc(fp)) != EOF) {
        if (c == '\n') {
            length++;
            i = 0;
        } else {
            grid[length][i++] = c - '0';
        }
    }

    int mx = 0;

    for (int i = 1; i < length - 1; i ++) {
        for (int j = 1; j < width - 1; j++) {
            int is_vis = 4;
            int check = grid[i][j];
            int lmx =0;

            int len = 0;
            for (int k = i-1; k >= 0; k--) {
                len++;
                if (grid[k][j] >= check) {
                    is_vis--;
                    break;
                }
            }
            lmx = len;

            len = 0;
            for (int k = i+1; k < length; k++) {
                len++;
                if (grid[k][j] >= check) {
                    is_vis--;
                    break;
                }
            }
            lmx *= len;

            len = 0;
            for (int l = j-1; l >= 0; l--) {
                len++;
                if (grid[i][l] >= check) {
                    is_vis--;
                    break;
                }
            }
            lmx *= len;

            len = 0;
            for (int l = j+1; l < width; l++) {
                len++;
                if (grid[i][l] >= check) {
                    is_vis--;
                    break;
                }
            }
            lmx *= len;

            if (lmx > mx) mx = lmx;

        }
    }

    cout << mx << endl;

    return 0;
}

int main() {
    p1();
    p2();
}

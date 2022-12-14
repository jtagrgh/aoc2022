#include <stdio.h>
#include <iostream>
#include <deque>
#include <vector>
#include <string.h>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <string>
#include <fstream>
#include <stack>
#include <list>

using namespace std;

void p1() {
    ifstream input("in2.txt");

    multimap<string, pair<int, set<string>>> tree;
    int out_val {0};

    stack<string> dirs;
    dirs.push(".");
    string line;
    while (!getline(input, line).eof()) {
        if (line[0] == '$') {
            if (line[2] ==  'c') {
                if (line[5] != '.') {
                    string name {line.substr(5)};
                    tree.insert({dirs.top() + "/" + name, pair<int, set<string>>{0, set<string>()}});
                    dirs.push(dirs.top() + "/" + name);
                }
                else { // .. cmd
                    int sum {0};
                    for (const auto &i: tree.find(dirs.top())->second.second){
                        int val {tree.find(i)->second.first}; 
                        sum += val;
                    }

                    tree.find(dirs.top())->second.first = sum;
                    if (sum <= 100000 && sum > 0) {
                        out_val += sum;
                    }
                    dirs.pop();
                }
            } else {
                continue;
            }
        }
        else if (line[0] == 'd') {
            unsigned long pos {line.find(" ") + 1};
            tree.find(dirs.top())->second.second.insert(dirs.top() + "/" + line.substr(pos));
        }
        else {
            unsigned long pos {line.find(" ")};
            int size {stoi(line.substr(0, pos))};
            pos++;
            string name {line.substr(pos)};
            tree.insert({dirs.top() + "/" + name, pair<int, set<string>>(size, set<string>())});
            tree.find(dirs.top())->second.second.insert(dirs.top() + "/" + name);
        }
    }

    while (dirs.top() != ".") {
        int sum {0};
        for (const auto &i: tree.find(dirs.top())->second.second){
            int val = tree.find(i)->second.first;
            sum += val;
        }

        tree.find(dirs.top())->second.first = sum;
        if (sum <= 100000 && sum > 0) {
            out_val += sum;
        }
        dirs.pop();
    }
    
    cout << "final " << out_val << endl;
}

void p2() {
    ifstream input("in2.txt");

    multimap<string, pair<int, set<string>>> tree;

    list<int> greed;

    stack<string> dirs;
    dirs.push(".");
    string line;
    while (!getline(input, line).eof()) {
        if (line[0] == '$') {
            if (line[2] ==  'c') {
                if (line[5] != '.') {
                    string name = line.substr(5);
                    tree.insert({dirs.top() + "->" + name, pair<int, set<string>>(0, set<string>())});
                    dirs.push(dirs.top() + "->" + name);
                }
                else { // .. cmd
                    int sum = 0;
                    for (const auto &i: tree.find(dirs.top())->second.second){
                        int val = tree.find(i)->second.first; 
                        sum += val;
                    }
                    greed.push_back(sum);
                    tree.find(dirs.top())->second.first = sum;
                    dirs.pop();
                }
            } else {
                continue;
            }
        }
        else if (line[0] == 'd') {
            int pos = line.find(" ") + 1;
            tree.find(dirs.top())->second.second.insert(dirs.top() + "->" + line.substr(pos));
        }
        else {
            int pos = line.find(" ");
            int size = stoi(line.substr(0, pos));
            pos++;
            string name = line.substr(pos);
            tree.insert({dirs.top() + "->" + name, pair<int, set<string>>(size, set<string>())});
            tree.find(dirs.top())->second.second.insert(dirs.top() + "->" + name);
        }
    }

    while (dirs.top() != ".") {
        int sum = 0;
        for (const auto &i: tree.find(dirs.top())->second.second){
            int val = tree.find(i)->second.first;
            sum += val;
        }
        greed.push_back(sum);
        tree.find(dirs.top())->second.first = sum;
        dirs.pop();
    }

    greed.sort();
    for (const auto &i: greed) {
        if ((70000000 - tree.find(".->/")->second.first) + i >= 30000000) {
            cout << " good space " << i << endl; 
            break;
        }
    }
}

int main () {
    p1();
    p2();
    return 0;
}

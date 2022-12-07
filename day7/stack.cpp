#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <stack>

using namespace std;

ifstream input;
int total = 0;
string line;
string word;
stringstream line_s;
int last_sum;

int main() {
    input.open("in2.txt");
    stack<int> call_stack;

    while (!getline(input, line).eof()) {
        line_s.str(line + " ");
        line_s.clear(); // Clear eof bit
        while (!getline(line_s, word, ' ').eof()) {
            if (isdigit(word[0])) { // File in dir, add size to sum
                call_stack.top() += stoi(word);
            }
            else if (word == "cd") {
                getline(line_s, word, ' ');
                if (word == "..") { // Dir finished, return sum
                    int sum = call_stack.top();
                    if (sum < 100000) total += sum;
                    call_stack.pop();
                    call_stack.top() += sum;
                } else { // Dir in dir, add dir size to sum
                    call_stack.push({0});
                }
            }
        }
    }

    while (1) {
        int sum = call_stack.top();
        if (sum < 100000) total += sum;
        call_stack.pop();
        if (call_stack.empty()) break;
        call_stack.top() += sum;
    }

    cout << total << endl;
}

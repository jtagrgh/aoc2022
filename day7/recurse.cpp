#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;
ifstream input;
int total = 0;
string line;
string word;
stringstream line_s;
int last_sum;

static int R() {
    int sum = 0;
    while (!getline(input, line).eof()) {
        line_s.str(line + " ");
        line_s.clear(); // Clear eof bit
        while (!getline(line_s, word, ' ').eof()) {
            if (isdigit(word[0])) { // File in dir, add size to sum
                sum += stoi(word);
            }
            else if (word == "cd") {
                getline(line_s, word, ' ');
                if (word == "..") { // Dir finished, return sum
                    if (sum < 100000) total += sum;
                    return sum;
                } else { // Dir in dir, add dir size to sum
                    sum += R();
                }
            }
        }
    }

    // Will happen on file eof, brings the call 
    // stack up to root
    if (sum < 100000) total += sum;
    return sum;  
}

int main() {
    input.open("in2.txt");
    R();

    cout << total << endl;

    return 0;
}

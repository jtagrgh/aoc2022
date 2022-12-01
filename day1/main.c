#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp = fopen("input.txt", "r");
    int maxcals[3] = {0};

    int running = 0;
    char buf[100];
    while (fgets(buf, 100, fp)) {
        printf("%d\n", atoi(buf));
        if (atoi(buf) != 0) {
            running += atoi(buf);
        } else {
            int lowest = 99999999;
            int lp = -1;
            for (int i = 0; i < 3; i++) {
                if (maxcals[i] < lowest) {
                    lowest = maxcals[i];
                    lp = i;
                }
            }
            if (lp != -1) {
                if (running > maxcals[lp]) maxcals[lp] = running;
            }
            running = 0;
        }
    }

    printf("%d %d %d\n", maxcals[0], maxcals[1], maxcals[2]);
    printf("%d\n", maxcals[0] + maxcals[1] + maxcals[2]);

    fclose(fp);
    return 0;
}

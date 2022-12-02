#include <stdio.h>
#include <string.h>

/* int main() { */
/*     FILE *fp = fopen("input.txt", "rb"); */

/*     char buff[100]; */
/*     char me, op; */
/*     int score = 0; */
/*     while (fgets(buff, 100, fp)) { */
/*         op = buff[0]; */
/*         me = buff[2]; */
/*         me -= ('X' - 'A'); */
/*         score += me - 'A' + 1; */
/*         if ((me - op) == 1 || (op - me) == 2) { */
/*             score += 6; */
/*         } */
/*         else if (me == op) { */
/*             score += 3; */
/*     } */

/*     printf("%d\n", score); */

/*     return 0; */
/* } */

int main() {
    FILE *fp = fopen("input.txt", "rb");

    char buff[100];
    char me, op;
    int score = 0;
    while (fgets(buff, 100, fp)) {
        op = buff[0];
        me = buff[2];

        printf("%c %c ", op, me);

        if (me == 'Z') {
            me = op + 1;
            if (me == 'D') me = 'A';
            score += 6;
        }
        else if (me == 'Y') {
            me = op;
            score += 3;
        } else {
            me = op - 1;
            if (me == 'A' - 1) me = 'C';
        }

        printf("%c \n", me);

        score += me - 'A' + 1;
    }

    printf("%d\n", score);

    return 0;
}

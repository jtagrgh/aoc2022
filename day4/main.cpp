#include <stdio.h>
#include <string.h>

/* int main() { */

/*     FILE *fp = fopen("in.txt", "r"); */

/*     int l1, l2, r1, r2; */

/*     char l[1000]; */
/*     int n = 0; */
/*     while (fscanf(fp, "%d-%d,%d-%d\n", &l1, &l2, &r1, &r2) != EOF) { */
/*         if (l1 <= r1 && l2 >= r2) { */
/*             n++; */
/*         } */
/*         else if (r1 <= l1 && r2 >= l2) { */
/*             n++; */
/*         } */
/*     } */

/*     printf("%d\n", n); */

/*     return 0; */
/* } */

int main() {

    FILE *fp = fopen("in.txt", "r");

    int l1, l2, r1, r2;

    char l[1000];
    int n = 0;
    while (fscanf(fp, "%d-%d,%d-%d\n", &l1, &l2, &r1, &r2) != EOF) {
        if (l1 >= r1 && l1 <= r2) {
            n++;
        }
        else if (l2 >= r1 && l2 <= r2) {
            n++;
        }
        else if (l1 <= r1 && l2 >= r2) {
            n++;
        }
        else if (r1 <= l1 && r2 >= l2) {
            n++;
        }
    }

    printf("%d\n", n);

    return 0;
}

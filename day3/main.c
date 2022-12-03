#include <stdio.h>
#include <string.h>

/* int main() { */
/*     FILE *fp = fopen("in.txt", "r"); */

/*     char l[1000]; */
/*     int len; */

/*     int score = 0; */

/*     while (fscanf(fp, "%s\n", l) != EOF) { */
/*         int hash[1000] = {0}; */
/*         len = strlen(l); */

/*         char share; */

/*         for (int i = 0; i < len/2; i++) { */
/*             hash[l[i]] = 1; */
/*         } */
/*         for (int i = len/2; i < len; i++) { */
/*             if (hash[l[i]] == 1) { */
/*                 share = l[i]; */
/*             } */
/*         } */

/*         if (share >= 'A' && share <= 'Z') { */
/*             score += share - 'A' + 27; */
/*         } */
/*         else if (share >= 'a' && share <= 'z') { */
/*             score += share - 'a' + 1; */
/*         } */
/*     } */

/*     return 0; */
/* } */


int main() {
    FILE *fp = fopen("in.txt", "r");

    char l1[1000];
    char l2[1000];
    char l3[1000];
    char l[1000];
    int len;

    int score = 0;

    int itr = 0;
    while (fscanf(fp, "%s\n%s\n%s\n", l1, l2, l3) != EOF) {
        int hash[1000] = {0};

        for (int i = 0; i < strlen(l1); i++) {
            if (hash[l1[i]] == 0) {
                hash[l1[i]] = 1;
            }
        }
        for (int i = 0; i < strlen(l2); i++) {
            if (hash[l2[i]] == 1) {
                hash[l2[i]] = 2;
            }
        }
        for (int i = 0; i < strlen(l3); i++) {
            if (hash[l3[i]] == 2) {
                hash[l3[i]] = 3;
            }
        }

        char share;
        for (int i = 0; i < 1000; i ++) {
            if (hash[i] == 3) {
                share = i;
            }
        }

        if (share >= 'A' && share <= 'Z') {
            score += share - 'A' + 27;
        }
        else if (share >= 'a' && share <= 'z') {
            score += share - 'a' + 1;
        }
    }

    printf("%d\n", score);

    return 0;
}


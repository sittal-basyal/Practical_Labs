/* Pure TM: a^n b^(n+1) */
#include <stdio.h>
#include <string.h>

int main() {
    char tape[100], again = 'y';

    while (again == 'y' || again == 'Y') {
        printf("Enter string: ");
        scanf("%99s", tape);

        int n = strlen(tape);
        int p = 0, ok = 1;

        /* Check format: a's followed by b's */
        while (tape[p] == 'a')
            p++;

        while (tape[p] == 'b')
            p++;

        if (p != n) {
            ok = 0;
        } else {
            int i = 0;

            /* Mark each a and one corresponding b */
            while (1) {
                while (tape[i] == 'X')
                    i++;

                if (tape[i] == '\0')
                    break;

                if (tape[i] != 'a') {
                    break;
                }

                tape[i] = 'X';

                int j = i + 1;

                while (tape[j] == 'a' || tape[j] == 'X')
                    j++;

                while (tape[j] == 'Y')
                    j++;

                if (tape[j] != 'b') {
                    ok = 0;
                    break;
                }

                tape[j] = 'Y';
                i++;
            }

            /* Count unmarked b's */
            int rem = 0;

            for (int k = 0; tape[k] != '\0'; k++) {
                if (tape[k] == 'b')
                    rem++;
            }

            if (rem != 1)
                ok = 0;
        }

        if (ok)
            printf("Accepted (a^n b^(n+1))\n");
        else
            printf("Rejected\n");

        printf("Test another string? (y/n): ");
        scanf(" %c", &again);
    }

    return 0;
}
/* Pure TM: a^(2n) b^n */

#include <stdio.h>
#include <string.h>

int main() {
    char tape[100], again = 'y';

    while (again == 'y' || again == 'Y') {
        printf("Enter string: ");
        scanf("%99s", tape);

        int n = strlen(tape);
        int p = 0;

        /* Check a's followed by b's */
        while (tape[p] == 'a')
            p++;

        while (tape[p] == 'b')
            p++;

        if (p != n) {
            printf("Rejected\n");
        } else {
            int ok = 1;

            while (1) {
                /* Find an unmarked b */
                int i = 0;
                while (tape[i] == 'a' || tape[i] == 'X' ||
                       tape[i] == 'Y')
                    i++;

                if (tape[i] == '\0')
                    break;

                if (tape[i] != 'b') {
                    ok = 0;
                    break;
                }

                tape[i] = 'Y';

                /* Mark two unmarked a's */
                int count = 0;
                int j = 0;

                while (count < 2) {
                    while (tape[j] == 'X' || tape[j] == 'Y')
                        j++;

                    if (tape[j] != 'a') {
                        ok = 0;
                        break;
                    }

                    tape[j] = 'X';
                    count++;
                    j++;
                }

                if (!ok)
                    break;
            }

            /* Ensure no unmarked a or b remains */
            for (int k = 0; k < n; k++) {
                if (tape[k] == 'a' || tape[k] == 'b')
                    ok = 0;
            }

            printf(ok ? "Accepted (a^(2n) b^n)\n"
                      : "Rejected\n");
        }

        printf("Test another string? (y/n): ");
        scanf(" %c", &again);
    }

    return 0;
}
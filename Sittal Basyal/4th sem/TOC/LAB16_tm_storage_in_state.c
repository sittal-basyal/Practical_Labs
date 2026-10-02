/* TM: storage in state, accepts ab* + ba* */

#include <stdio.h>
#include <string.h>

int main() {
    char s[100], again = 'y';

    while (again == 'y' || again == 'Y') {
        printf("Enter string: ");
        scanf("%99s", s);

        int n = strlen(s);
        int ok = 1;

        if (n == 0) {
            ok = 0;
        } else {
            char store = s[0];

            if (store == 'a') {
                for (int i = 1; i < n; i++) {
                    if (s[i] != 'b') {
                        ok = 0;
                        break;
                    }
                }
            } else if (store == 'b') {
                for (int i = 1; i < n; i++) {
                    if (s[i] != 'a') {
                        ok = 0;
                        break;
                    }
                }
            } else {
                ok = 0;
            }
        }

        printf(ok ? "Accepted (ab* + ba*)\n" : "Rejected\n");

        printf("Test another string? (y/n): ");
        scanf(" %c", &again);
    }

    return 0;
}
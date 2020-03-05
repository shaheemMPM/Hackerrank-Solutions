#include <stdio.h>
#include <math.h>

void update(int *a,int *b) {
    int copy = *a;
    *a += *b;
    *b -= copy;
    *b = abs(*b);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}

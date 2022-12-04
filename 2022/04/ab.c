#include <stdio.h>

int fully_contained(const int *elf1, const int *elf2);
int overlaps(const int *elf1, const int *elf2);

int main(int argc, char **argv){

    FILE *fp = fopen("input.txt", "r");

    int elf1[2], elf2[2];
    int fully_contained_pairs = 0;
    int overlapping_pairs = 0;

    while(fscanf(fp, "%d-%d,%d-%d\n", elf1, elf1+1, elf2, elf2+1) != EOF){
        fully_contained_pairs += fully_contained(elf1, elf2);
        overlapping_pairs += overlaps(elf1, elf2);
    }

    printf("%d\n", fully_contained_pairs);
    printf("%d\n", overlapping_pairs);

    fclose(fp);
    return 0;
}

int fully_contained(const int *elf1, const int *elf2){
    if( elf1[0] >= elf2[0] && elf1[1] <= elf2[1]) return 1;
    if( elf2[0] >= elf1[0] && elf2[1] <= elf1[1]) return 1;
    return 0;
}

int overlaps(const int *elf1, const int *elf2){
    if( elf1[0] > elf2[1] ) return 0;
    if( elf1[1] < elf2[0] ) return 0;
    return 1;
}

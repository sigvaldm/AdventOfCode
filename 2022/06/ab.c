/*
 * Compile and run with:
 *      $ gcc ab.c; ./a.out
 *
 * Very fast and memory efficient. Only keep NUM letters in memory at a time in
 * a ring buffer-like structure.
 */

#include <stdio.h>

int duplicates(char *buffer);

/* const int NUM = 4; /* part a */
const int NUM = 14; /* part b */

int main(int argc, char **argv){

    FILE *fp = fopen("input.txt", "r");

    char buffer[NUM];

    int i = 0;
    while((buffer[i%NUM] = fgetc(fp)) != EOF){
        if(i>NUM-1 && !duplicates(buffer)){
            printf("%d\n", i+1);
            return 0;
        }
        i++;
    }

    return 1;
}

int duplicates(char *buffer){
    for(int i=0; i<NUM; ++i){
        for(int j=i+1; j<NUM; ++j){
            if(buffer[i]==buffer[j]) return 1;
        }
    }
    return 0;
}

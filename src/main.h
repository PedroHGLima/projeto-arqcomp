#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "dgemm.h"

#define	SEED 42

void get_args(int argc, char* argv[], size_t* n) {
    if (argc > 1) {
        *n = strtoul(argv[1], NULL, 10);
    } else {
        fprintf(stderr, "Uso: %s <size>\n", argv[0]);
        exit(EXIT_FAILURE);
    }
}

void zerar_matriz(double* matriz, size_t n) {
    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) {
            matriz[i * n + j] = 0;
        }
    }
}

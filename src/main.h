#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#include "dgemm.h"

#define	SEED 42
typedef enum { false, true } bool;

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

bool comparar_matriz(double* A, double* B, size_t n) {
    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) {
            if (A[i * n + j] != B[i * n + j]) {
                return false;
            }
        }
    }
    return true;
}

double multiplicar(size_t n, double *A, double *B, double *Ref, void (*metodo)(size_t, double*, double*, double*)) {
    double start_time, end_time;
    double time_taken;

    double *C = (double*) aligned_alloc(4*sizeof(double), n*n * sizeof(double));
    zerar_matriz(C, n);

    // Multiplica as matrizes A e B usando o método fornecido
    start_time = omp_get_wtime();
    metodo(n, A, B, C);
    end_time = omp_get_wtime();

    time_taken = (end_time - start_time) * 1000;

    time_taken = comparar_matriz(C, Ref, n) ? time_taken : -1;
    free(C);
    return time_taken;
}

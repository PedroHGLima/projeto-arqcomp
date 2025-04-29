#include "main.h"

int main(int argc, char* argv[]) {
    srand(SEED);
    size_t n, n2;
    get_args(argc, argv, &n);
    if ((n == 0) || (n%16 != 0)) {
        fprintf(stderr, "Tamanho da matriz deve ser maior que 0 e multiplo de 16\n");
        return 1;
    }
    n2 = n * n;
    printf("Tamanho da matriz:\nN=%lu\nN2=%lu\nMEM=%.2f MB\n", n, n2, n2*sizeof(double)/1e6);

    double *A, *B, *Ref;	// declarando assim para garantir memoria alinhada
    A = (double*) aligned_alloc(4*sizeof(double), n2 * sizeof(double));
    B = (double*) aligned_alloc(4*sizeof(double), n2 * sizeof(double));
    Ref = (double*) aligned_alloc(4*sizeof(double), n2 * sizeof(double));
    for (size_t i = 0; i < n2; i++) {
        A[i] = (double)rand() / RAND_MAX;
        B[i] = (double)rand() / RAND_MAX;
        Ref[i] = 0.0;
    }
    if (A == NULL || B == NULL || Ref == NULL) {
        fprintf(stderr, "Erro ao alocar memoria\n");
        return 1;
    }

    double time_taken;
    dgemm(n, A, B, Ref);
    printf("Tempo de execucao: \n");
    
    // Testar a funcao dgemm original
    time_taken = multiplicar(n, A, B, Ref, dgemm);
    if (time_taken!=-1) printf("DGEMM %.3f ms\n", time_taken);

    // Testar a funcao dgemm otimizada com AVX
    time_taken = multiplicar(n, A, B, Ref, avx_dgemm);
    if (time_taken!=-1) printf("AVX %.3f ms\n", time_taken);

    // Testar a funcao dgemm otimizada com AVX e loop unrolling
    time_taken = multiplicar(n, A, B, Ref, loop_unr);
    if (time_taken!=-1) printf("AVX+LU %.3f ms\n", time_taken);

    // Testar a funcao dgemm otimizada com AVX e cache blocking
    time_taken = multiplicar(n, A, B, Ref, cache_blocking);
    if (time_taken!=-1) printf("AVX+CB %.3f ms\n", time_taken);

    free(A);
    free(B);
    free(Ref);

    return 0;
}
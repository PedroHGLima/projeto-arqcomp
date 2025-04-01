#include "main.h"

int main(int argc, char* argv[]) {
	srand(SEED);
	size_t n, n2;
	get_args(argc, argv, &n);
	if (n == 0) {
		fprintf(stderr, "Tamanho da matriz deve ser maior que 0\n");
		return 1;
	}
	n2 = n * n;
	printf("Tamanho da matriz:\nN=%lu\nN2=%lu\nMEM=%.2f MB\n", n, n2, n2*sizeof(double)/1e6);

	double *A, *B, *C;	// declarando assim para garantir memoria alinhada
	A = (double*) aligned_alloc(4*sizeof(double), n2 * sizeof(double));
	B = (double*) aligned_alloc(4*sizeof(double), n2 * sizeof(double));
	C = (double*) aligned_alloc(4*sizeof(double), n2 * sizeof(double));
	for (size_t i = 0; i < n2; i++) {
		A[i] = (double)rand() / RAND_MAX;
		B[i] = (double)rand() / RAND_MAX;
		C[i] = 0.0;
	}
	if (A == NULL || B == NULL || C == NULL) {
		fprintf(stderr, "Erro ao alocar memoria\n");
		return 1;
	}

	clock_t start, end;
	double time_taken;
	printf("Tempo de execucao: \n");
	
	// Testar a funcao dgemm original
	start = clock();
    dgemm(n, A, B, C);
	end = clock();
	time_taken = ((double)(end - start)) / CLOCKS_PER_SEC * 1000;
	printf("DGEMM: %.2f ms\n", time_taken);

	// Testar a funcao dgemm otimizada com AVX
	zerar_matriz(C, n);
	start = clock();
	avx_dgemm(n, A, B, C);
	end = clock();
	time_taken = ((double)(end - start)) / CLOCKS_PER_SEC * 1000;
	printf("AVX: %.2f ms\n", time_taken);

	// Printar a matriz C
	// for (size_t i = 0; i < n; i++) {
	// 	for (size_t j = 0; j < n; j++) {
	// 		printf("%lf ", C[i * n + j]);
	// 	}
	// 	printf("\n");
	// }

    free(A);
    free(B);
    free(C);

    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void dgemm (unsigned long n, double* A, double* B, double* C) {
	for (unsigned long i = 0; i < n; ++i)
		for (unsigned long j = 0; j < n; ++j) {
			double cij = C[i+j*n]; /* cij= C[i][j] */
			for (unsigned long k = 0; k < n; k++ )
				cij += A[i+k*n] * B[k+j*n]; /*cij+=A[i][k]*B[k][j]*/
			C[i+j*n] = cij; /* C[i][j] = cij */
		}
}

void get_args(int argc, char* argv[], unsigned long* n) {
	if (argc > 1) {
		*n = strtoul(argv[1], NULL, 10);
	} else {
		fprintf(stderr, "Usage: %s <size>\n", argv[0]);
		exit(EXIT_FAILURE);
	}
}


int main(int argc, char* argv[]) {
	unsigned long n; // Size of the matrix
	get_args(argc, argv, &n);
	if (n == 0) {
		fprintf(stderr, "Matrix size must be greater than 0\n");
		return 1;
	}
	unsigned long n2 = n * n; // Total number of elements in the matrix
	printf("Matrix size: %lu x %lu = %lu\n", n, n, n2);

	clock_t start, end;
    double* A = malloc(n2 * sizeof(double));
    double* B = malloc(n2 * sizeof(double));
    double* C = malloc(n2 * sizeof(double));

    if (!A || !B || !C) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    for (unsigned long i = 0; i < n2; i++) {
        A[i] = (double)i + 1;
        B[i] = (double)i + 1;
        C[i] = 0;
    }

	start = clock();
    dgemm(n, A, B, C);
	end = clock();

	double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC * 1000;
	printf("Execution time (CPU time): %.2f ms\n", time_taken);

    free(A);
    free(B);
    free(C);

    return 0;
}

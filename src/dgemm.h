#include <stdio.h>
#include <x86intrin.h>

#define UNROLL (4)
#define BLOCKSIZE 32

/**
 * @brief Funcao DGEMM original
 * pg. 438
 * fig 3.19
 * 
 * @param n Tamanho da matriz (n x n)
 * @param A Operando A
 * @param B Operando B
 * @param C Resultado
 * 
 */
void dgemm (size_t n, double* A, double* B, double* C);

/**
 * @brief DGEMM otimizada usando paralelismo subword AVX
 * pg. 440
 * fig 3.21
 * 
 * @param n Tamanho da matriz (n x n)
 * @param A Operando A
 * @param B Operando B
 * @param C Resultado
 */
void avx_dgemm (size_t n, double* A, double* B, double* C);

/**
 * @brief DGEMM otimizada usando loop unrolling,
 *  criando mais oportunidades para paralelismo a nível de instrução
 * pg. 651
 * fig 4.77
 * 
 * @param n Tamanho da matriz (n x n)
 * @param A Operando A
 * @param B Operando B
 * @param C Resultado
 */
void loop_unr (size_t n, double* A, double* B, double* C);

/**
 * @brief DGEMM otimizada usando cache blocking
 * pg. 923
 * fig 5.47
 * 
 * @param n Tamanho da matriz (n x n)
 * @param A Operando A
 * @param B Operando B
 * @param C Resultado
 */
void cache_blocking(size_t n, double* A, double* B, double* C);
void do_block(int n, int si, int sj, int sk, double *A, double *B, double *C);

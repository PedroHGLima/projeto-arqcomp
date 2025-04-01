#include <stdio.h>
#include <x86intrin.h>

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

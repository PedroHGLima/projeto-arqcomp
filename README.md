# Arquitetura de Computadores
Este repositório contém o código fonte do projeto de arquitetura de computadores.

## Descrição 
O projeto consiste em testar diversas implementações de um algoritmo de multiplicação de matrizes, utilizando diferentes abordagens e técnicas de otimização. O objetivo é comparar o desempenho das implementações em termos de tempo de execução e uso de memória.

## Estrutura do Repositório
- [analise](analise) - Contém os scripts de análise de desempenho das implementações.
- [bin](bin) - Contém os executáveis das implementações.
- [scripts](scripts) - Contém os scripts para rodar automaticamente as implementações.
- [src](src) - Código fonte.

## Compilação
Para compilar o projeto, utilize o comando `make` na [pasta source](src). Isso irá compilar todas as implementações e gerar os executáveis na pasta `bin`.

```bash
make
```

## Benchmark
O programa responsável pelos benchmarks está na [pasta analise](analise). Ele irá executar todas as implementações algumas vezes e gerar um arquivo CSV com os resultados. Para executar o benchmark, utilize o comando:

```bash
./scripts/run_benchmark.sh
```

# Grupo
- [Pedro Lima](https://github.com/PedroHGLima)


import os
import pandas as pd

def extrair_dados(arquivo:str, n=0, run=0):
    """Gera um dicionário com os dados do benchmark.

    Parameters
    ----------
    arquivo : str
        caminho para o arquivo.txt a ser lido
    n : int, optional
        Tamanho da matriz, by default 0
    run : int, optional
        Número de run, by default 0

    Yields
    ------
    dict
        dicionário com os dados do benchmark
        - n: tamanho da matriz
        - run: número de run
        - metodo: nome do método
        - tempo: tempo gasto em ms
    """
    with open(arquivo, "r") as f:
        lines = f.readlines()[5:]  # pular para o resultado
        for line in lines:
            yield {
                "n": n,
                "run": run,
                "metodo": line.split(' ')[0],
                "tempo": float(line.split(' ')[1])  # ms
            }
            
def main():
    """
    Monta o dataset com os dados do benchmark.
    Isso é útil para casos em que o benchmark morre sem salvar os dados.
    """
    path = os.path.join(os.path.dirname(__file__), "benchmark")
    outputs = [file for file in os.listdir(path) if file.endswith(".txt")]
    dados = list()
    
    for file in outputs:
        arquivo = os.path.join(path, file)
        n, run = map(int, file.split(".")[0].split("_")[1:3])
        for dado in extrair_dados(arquivo, n, run):
            dados.append(dado)
            
    df = pd.DataFrame(dados)
    path = os.path.join(os.path.dirname(__file__), "benchmark")
    df.to_csv(os.path.join(path, "benchmark.csv"), index=False)

if __name__ == "__main__":
    main()
    
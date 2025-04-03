import os
import pandas as pd
from tqdm import tqdm
from itertools import product

from dataset import extrair_dados

n_sizes = [2**n for n in range(4, 11)]
n_repeats = 10


def main():
    path_to_bins = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../bin"))
    os.makedirs(f"{os.path.dirname(__file__)}/benchmark", exist_ok=True)
    
    dados = []
    pbar = tqdm(product(n_sizes, range(n_repeats)), total=(len(n_sizes) * n_repeats), disable=None)
    for n, i in pbar:
        pbar.set_description(f"{n=} {i=}")
        # rodar o programa
        arquivo = f"{os.path.dirname(__file__)}/benchmark/run_{n}_{i:02d}.txt"
        cmd = f"{path_to_bins}/dgemm.exe {n} > {arquivo}"
        # print(cmd)
        c = os.system(cmd)
        if c != 0:
            print(f"Interrompendo benchmark, erro: {c}")
            break

        # pegar o resultado
        dados_arquivo = extrair_dados(arquivo, n, i)
        for dado in dados_arquivo:
            dados.append(dado)
    
    df = pd.DataFrame(dados)
    print(f"Salvando o csv em: {os.path.dirname(__file__)}/benchmark/benchmark.csv")
    df.to_csv(f"{os.path.dirname(__file__)}/benchmark/benchmark.csv", index=False)


if __name__ == "__main__":
    main()

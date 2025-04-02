import os
import pandas as pd
from tqdm import tqdm

n_sizes = [16, 32, 64, 128, 256, 512, 1024, 2048]
n_repeats = 10


def main():
    path_to_bins = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../bin"))
    os.makedirs(f"{os.path.dirname(__file__)}/benchmark", exist_ok=True)
    
    dados = []
    for n in tqdm(n_sizes):
        for i in tqdm(range(n_repeats), leave=False):
            # rodar o programa
            arquivo = f"{os.path.dirname(__file__)}/benchmark/run_{n}_{i:02d}.txt"
            cmd = f"cd {path_to_bins} && ./dgemm.exe {n} > {arquivo}"
            # print(cmd)
            os.system(cmd)

            # pegar o resultado
            with open(arquivo, "r") as f:
                lines = f.readlines()[5:]
                for line in lines:
                    metodo = line.split(' ')[0]
                    tempo = float(line.split(' ')[1]) # ms
                    
                    dados.append(
                        {
                            "n": n,
                            "run": i,
                            "metodo": metodo,
                            "tempo": tempo
                        }
                    )
    
    df = pd.DataFrame(dados)
    print(df.head())
    df.to_csv(f"{os.path.dirname(__file__)}/benchmark/benchmark.csv", index=False)


if __name__ == "__main__":
    main()

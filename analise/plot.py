import os
import pandas as pd
import matplotlib.pyplot as plt

def main():
    path_to_data = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "benchmark/benchmark.csv"))
    df = pd.read_csv(path_to_data)
    
    df_grouped = df.groupby(["n", "metodo"]).agg(
        tempo_medio=("tempo", "mean"),
        tempo_std=("tempo", "std")
    ).reset_index()
    
    plt.figure()
    for metodo in df_grouped["metodo"].unique():
        df_temp = df_grouped[df_grouped["metodo"] == metodo]
        plt.errorbar(
            df_temp["n"], df_temp["tempo_medio"], yerr=df_temp["tempo_std"],
            label=metodo, capsize=5, fmt='-o'
        )
    
    plt.xscale("log", base=2)
    plt.xlabel("Tamanho da matriz (n)")
    plt.yscale("log", base=10)
    plt.ylabel("Tempo [ms]")
    plt.title("Tempo de execução x Tamanho da matriz")
    plt.xticks(df_grouped["n"].unique())
    plt.tight_layout()
    plt.legend()
    plt.grid()
    plt.savefig(f"{os.path.dirname(__file__)}/benchmark/benchmark.png")

if __name__ == "__main__":
    main()

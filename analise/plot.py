import os
import pandas as pd
import matplotlib.pyplot as plt

def main():
    path_to_data = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "benchmark/benchmark.csv"))
    plots_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "benchmark", "plots"))
    os.makedirs(plots_path, exist_ok=True)

    df = pd.read_csv(path_to_data)
    
    df_grouped = df.groupby(["n", "metodo"]).agg(
        tempo_medio=("tempo", "mean"),
        tempo_std=("tempo", "std"),
        tempo_dgemm=("tempo", lambda x: x[df["metodo"] == "DGEMM"].mean()),
    ).reset_index()
    
    # Gráfico combinado
    plt.figure()
    color_cycle = iter(plt.rcParams['axes.prop_cycle'])
    colors = {metodo: next(color_cycle)['color'] for metodo in df_grouped["metodo"].unique()}

    for metodo in df_grouped["metodo"].unique():
        df_temp = df_grouped[df_grouped["metodo"] == metodo]
        plt.errorbar(
            df_temp["n"], df_temp["tempo_medio"], yerr=df_temp["tempo_std"],
            label=f"{metodo:<7}: {df_temp['tempo_medio'].mean()/df_grouped['tempo_dgemm'].mean():>7.2%}",
            capsize=5, fmt='-o'
        )

    plt.xscale("log", base=2)
    plt.xlabel("Tamanho da matriz (n)")
    plt.yscale("log", base=10)
    plt.ylabel("Tempo [ms]")
    plt.title("Tempo de execução x Tamanho da matriz")
    plt.xticks(df_grouped["n"].unique())
    plt.tight_layout()
    plt.legend(prop={"family": "monospace"}, title="Método : % DGEMM")
    plt.grid()
    plt.savefig(f"{plots_path}/benchmark.png")

    # Gráficos individuais para cada método
    for metodo in df_grouped["metodo"].unique():
        df_temp = df_grouped[df_grouped["metodo"] == metodo]
        plt.figure()
        plt.errorbar(
            df_temp["n"], df_temp["tempo_medio"], yerr=df_temp["tempo_std"],
            label=f"{metodo:<7}", capsize=5, fmt='-o', color=colors[metodo]  # Usa a cor associada ao método
        )
        plt.xscale("log", base=2)
        plt.xlabel("Tamanho da matriz (n)")
        plt.yscale("log", base=10)
        plt.ylabel("Tempo [ms]")
        plt.title(f"Tempo de execução x Tamanho da matriz ({metodo})")
        plt.xticks(df_grouped["n"].unique())
        plt.tight_layout()
        plt.legend(prop={"family": "monospace"})
        plt.grid()
        plt.savefig(f"{plots_path}/{metodo}_benchmark.png")        

if __name__ == "__main__":
    main()

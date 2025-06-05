import os
import pandas as pd
import matplotlib.pyplot as plt
import math

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

    num_repetitions = 10

    n_sizes = df_grouped["n"].unique()
    
    overall_mean_times = df_grouped.groupby("metodo")["tempo_medio"].mean().sort_values()
    methods_sorted = overall_mean_times.index.tolist()

    num_methods = len(methods_sorted)

    bar_width = 0.4 / num_methods 
    x_positions_log = {n: math.log2(n) for n in n_sizes}

    # Gráfico combinado
    plt.figure(figsize=(12, 7))
    color_cycle = iter(plt.rcParams['axes.prop_cycle'])
    colors = {metodo: next(color_cycle)['color'] for metodo in methods_sorted}

    for i, metodo in enumerate(methods_sorted):
        df_temp = df_grouped[df_grouped["metodo"] == metodo]
        
        offsets = [(j - (num_methods - 1) / 2) * bar_width for j in range(num_methods)]
        current_offset = offsets[i]

        x_values_for_bars = [x_positions_log[n] + current_offset for n in df_temp["n"]]
        percentages = []
        for index, row in df_temp.iterrows():

            dgemm_time = df_grouped[(df_grouped['n'] == row['n']) & (df_grouped['metodo'] == 'DGEMM')]['tempo_medio'].iloc[0]
            percentages.append(row['tempo_medio'] / dgemm_time)
        
        # Recalculando a porcentagem para a legenda de forma mais clara, usando a média global do DGEMM
        mean_dgemm_time_overall = df_grouped[df_grouped["metodo"] == "DGEMM"]["tempo_medio"].mean()
        mean_method_time_overall = df_grouped[df_grouped["metodo"] == metodo]["tempo_medio"].mean()
        percentage_label = f"{metodo:<7}: {mean_method_time_overall / mean_dgemm_time_overall:>7.2%}"


        plt.bar(
            x_values_for_bars,
            df_temp["tempo_medio"],
            yerr=df_temp["tempo_std"],
            width=bar_width * 0.9, # Reduz um pouco a largura para mais espaçamento entre barras
            label=percentage_label,
            capsize=5,
            color=colors[metodo],
            edgecolor='black'
        )

    plt.xlabel("Tamanho da matriz (n)")
    plt.yscale("log", base=10)
    plt.ylabel("Tempo [ms]")
    plt.title(f"Tempo de execução x Tamanho da matriz ({num_repetitions} repetições)")
    
    min_log_n = min(x_positions_log.values())
    max_log_n = max(x_positions_log.values())
    plt.xlim(min_log_n - bar_width * num_methods / 2 - 0.1, max_log_n + bar_width * num_methods / 2 + 0.1)

    plt.xticks(list(x_positions_log.values()), n_sizes)
    plt.tight_layout()
    plt.legend(prop={"family": "monospace"}, title="Método : % DGEMM")
    plt.grid()
    plt.savefig(f"{plots_path}/benchmark.png")
    plt.close()

    # Gráficos individuais para cada método
    for metodo in methods_sorted:
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
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

def get_fig(result):
    fig, ax = plt.subplots()
    df = pd.concat([
        pd.read_csv(Path("results", result, "for.csv"), header=None, names=["for"]),
        pd.read_csv(Path("results", result, "lcomp.csv"), header=None, names=["lcomp"]),
        pd.read_csv(Path("results", result, "reduce.csv"), header=None, names=["reduce"])
    ])
    df.boxplot(ax = ax)
    ax.set_ylabel("Time in seconds")
    fig.suptitle(result, fontsize=16)
    fig.savefig(Path("results", result, "boxplot.png"))
    return fig, ax

fig2, ax2 = get_fig("result_1e2")
fig3, ax3 = get_fig("result_1e3")
fig6, ax6 = get_fig("result_1e6")



plt.show()
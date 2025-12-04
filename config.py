import matplotlib as mpl
import matplotlib.pyplot as plt


def config_colors():
    custom_colors = [
        "#D0417E",  # Cor base
        "#41D0A8",  # Complementar
        "#417ED0",  # Análago
        "#D08141",  # Análogo quente
        "#8D41D0",  # Triádica
    ]

    mpl.rcParams.update({

        # Fundo da figura e dos eixos
        "figure.facecolor": "#001e2a",
        "axes.facecolor": "#001e2a",

        # Bordas e spines
        "axes.edgecolor": "#cccccc",
        "axes.linewidth": 0.8,

        # Títulos e labels
        "axes.labelcolor": "white",
        "axes.titlesize": 16,
        "axes.titlecolor": "white",

        # Ticks
        "xtick.color": "white",
        "ytick.color": "white",

        # Grid
        "axes.grid": True,
        "grid.color": "#444444",
        "grid.linestyle": "--",
        "grid.linewidth": 0.4,

        # Legendas
        "legend.facecolor": "#2a2a2a",
        "legend.edgecolor": "#e7edeb",
        "legend.fontsize": 11,
        "legend.framealpha": 0.6,
        "legend.labelcolor": "white",

        # Ciclo de cores (paleta moderna)
        "axes.prop_cycle": plt.cycler(color=custom_colors),

        # Fonte
        "font.size": 12,
    })

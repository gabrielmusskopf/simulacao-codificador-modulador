import random
import math


def apply_awgn(symbols: list[float], snr_db: int) -> list[float]:
    """
    Adiciona ruído branco gaussiano (AWGN) aos símbolos transmitidos.
    """
    noisy_symbols: list[float] = []

    signal_power = 1.0

    # Da fórmula SNR = 10.log(P_sinal / P_ruido)
    noise_power = signal_power / (10 ** (snr_db / 10))

    # Potência = Variância = Desvio padrão ^ 2
    noise_std_dev = math.sqrt(noise_power)

    for s in symbols:
        noise = random.gauss(0, noise_std_dev)
        noisy_symbols.append(s + noise)

    return noisy_symbols

import matplotlib.pyplot as plt
import random

import channel_coding
import modulation
import channel


def generate_random_bits(amount: int) -> list[int]:
    """Gera uma lista de N bits aleatórios (0 ou 1)"""
    return [random.choice([0, 1]) for _ in range(amount)]


def calculate_ber(sent_bits: list[int], received_bits: list[int]) -> float:
    """
    Calcula o Bit Error Rate (Taxa de Erro de Bit).
    Retorna um float entre 0.0 (0%) e 1.0 (100%).
    """
    if len(sent_bits) != len(received_bits):
        raise ValueError("Listas de bits devem ter o mesmo tamanho para calcular BER")

    erros = 0
    total = len(sent_bits)

    for i in range(total):
        bit_enviado = sent_bits[i]
        bit_recebido = received_bits[i]

        if bit_enviado != bit_recebido:
            erros = erros + 1

    return erros / total


if __name__ == "__main__":
    num_bits = 10000            # Quantidade de bits para ter relevância estatística
    snr_range = range(-4, 11)   # Testar de -4dB até 10dB
    print(f"--- Iniciando Benchmark ({num_bits} bits por ponto) ---")

    simulated_ber = []

    for snr in snr_range:
        bits = generate_random_bits(num_bits)

        bits_manchester = channel_coding.encode_manchester(bits)
        simbolos_tx = modulation.modulate_bpsk(bits_manchester)
        simbolos_rx = channel.apply_awgn(simbolos_tx, snr)
        bits_demodulados = modulation.demodulate_bpsk(simbolos_rx)

        erro = calculate_ber(bits_manchester, bits_demodulados)
        simulated_ber.append(erro)

        print(f"SNR: {snr}dB | BER: {erro:.5f}")

    plt.figure(figsize=(10, 6))

    # Curva Simulada
    plt.semilogy(snr_range, simulated_ber, 'bo-', label='Simulado (BPSK)')

    plt.title('Desempenho de BER vs SNR')
    plt.xlabel('SNR (dB) - Relação Sinal-Ruído')
    plt.ylabel('BER (Bit Error Rate) - Escala Log')
    plt.grid(True, which="both", ls="-")
    plt.legend()
    plt.ylim(0.00001, 1)

    print("Gerando gráfico...")
    plt.show()

import matplotlib.pyplot as plt
import random

from config import config_colors
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
    config_colors()

    num_bits = 500000            # Quantidade de bits para ter relevância estatística
    snr_range = range(-4, 20)   # Testar de -4dB até 20dB
    print(f"--- Iniciando Benchmark ({num_bits} bits por ponto) ---")

    ber_bpsk = []
    ber_ask = []
    ber_qpsk = []
    ber_8psk = []
    ber_16psk = []

    for snr in snr_range:
        bits = generate_random_bits(num_bits)
        bits = channel_coding.encode_manchester(bits)

        # Simulação BPSK
        tx_bpsk = modulation.modulate_bpsk(bits)
        rx_bpsk = channel.apply_awgn(tx_bpsk, snr)
        dec_bpsk = modulation.demodulate_bpsk(rx_bpsk)
        ber_bpsk.append(calculate_ber(bits, dec_bpsk))

        # Simulação ASK
        tx_ask = modulation.modulate_ask(bits)
        rx_ask = channel.apply_awgn(tx_ask, snr)
        dec_ask = modulation.demodulate_ask(rx_ask)
        ber_ask.append(calculate_ber(bits, dec_ask))

        # Simulação QPSK
        tx_qpsk = modulation.modulate_qpsk(bits)
        rx_qpsk = channel.apply_awgn(tx_qpsk, snr)  # Usa Canal Complexo
        dec_qpsk = modulation.demodulate_qpsk(rx_qpsk)
        # Ajuste de tamanho (pode sobrar 1 bit se impar)
        limit = min(len(bits), len(dec_qpsk))
        ber_qpsk.append(calculate_ber(bits[:limit], dec_qpsk[:limit]))

        # 8-PSK (M=8)
        tx_8 = modulation.modulate_mpsk(bits, M=8)
        rx_8 = channel.apply_awgn(tx_8, snr)
        dec_8 = modulation.demodulate_mpsk(rx_8, M=8)
        ber_8psk.append(calculate_ber(bits[:len(dec_8)], dec_8))

        # 16-PSK (M=16)
        tx_16 = modulation.modulate_mpsk(bits, M=16)
        rx_16 = channel.apply_awgn(tx_16, snr)
        dec_16 = modulation.demodulate_mpsk(rx_16, M=16)
        ber_16psk.append(calculate_ber(bits[:len(dec_16)], dec_16))

        print(f"SNR {snr}dB | BPSK: {ber_bpsk[-1]:.4f} | ASK: {ber_ask[-1]:.4f} | QPSK: {ber_qpsk[-1]:.5f} | 8-PSK: {ber_8psk[-1]:.5f} | 16-PSK: {ber_16psk[-1]:.5f}")

    plt.semilogy(snr_range, ber_bpsk, 'b-o', label='BPSK Sim')
    plt.semilogy(snr_range, ber_ask, 'r-s', label='ASK Sim')
    plt.semilogy(snr_range, ber_qpsk, 'c-o', label='QPSK (2 bits/símbolo)')
    plt.semilogy(snr_range, ber_8psk, 'm-o', label='8-PSK (3 bits/símbolo)')
    plt.semilogy(snr_range, ber_16psk, 'y-o', label='16-PSK (4 bits/símbolo)')

    plt.title('Comparativo de Desempenho (BER vs SNR)')
    plt.xlabel('SNR (dB)')
    plt.ylabel('BER (Escala Log)')
    plt.grid(True, which="both", alpha=0.4)
    plt.legend()
    plt.ylim(1e-5, 1)
    print("Gerando gráfico comparativo...")
    plt.show()

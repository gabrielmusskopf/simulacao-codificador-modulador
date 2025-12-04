import matplotlib.pyplot as plt
import modulation
import channel
from benchmark import generate_random_bits
from config import config_colors


def run_mpsk_viz():
    config_colors()

    num_bits = 2000
    snr_db = 15
    bits = generate_random_bits(num_bits)

    plt.figure(figsize=(10, 5))

    # --- 4-PSK (2 bits) ---
    plt.subplot(1, 2, 1)
    tx = modulation.modulate_mpsk(bits, M=4)
    rx = channel.apply_awgn(tx, snr_db)
    plt.scatter([s.real for s in rx], [s.imag for s in rx], c='purple', alpha=0.5, s=50)
    plt.title("4-PSK (2 bits/sym)")
    plt.grid(True)
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)

    # --- 16-PSK (4 bits) ---
    plt.subplot(1, 2, 2)
    tx = modulation.modulate_mpsk(bits, M=16)
    rx = channel.apply_awgn(tx, snr_db)
    plt.scatter([s.real for s in rx], [s.imag for s in rx], c='orange', alpha=0.5, s=50)
    plt.title("16-PSK (4 bits/sym)")
    plt.grid(True)
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)

    plt.show()


if __name__ == "__main__":
    run_mpsk_viz()

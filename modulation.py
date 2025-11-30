def modulate_bpsk(bits: list[int]) -> list[float]:
    """
    Modulação BPSK (Binary Phase Shift Keying).
    Mapeia bits lógicos para símbolos de constelação (+1/-1).

    Bit 0 -> -1.0
    Bit 1 -> +1.0
    """
    symbols: list[float] = []

    for bit in bits:
        if bit == 0:
            symbols.append(-1.0)
        elif bit == 1:
            symbols.append(1.0)
        else:
            raise ValueError(f"Bit inválido encontrado na modulação: {bit}")

    return symbols


def demodulate_bpsk(received_symbols: list[float]) -> list[int]:
    """
    Demodulação BPSK.
    Decide se o símbolo recebido é 0 ou 1 baseando-se no limiar de decisão (0.0).

    Símbolo < 0.0  -> Bit 0
    Símbolo >= 0.0 -> Bit 1
    """
    bits: list[int] = []

    for symbol in received_symbols:
        if symbol >= 0.0:
            bits.append(1)
        else:
            bits.append(0)

    return bits

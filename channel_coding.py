def encode_manchester(bits: list[int]) -> list[int]:
    """
    Codificação Manchester
    Bit 0 -> 0, 1
    Bit 1 -> 1, 0
    """
    encoded_stream: list[int] = []

    for bit in bits:
        if bit == 0:
            # Transição Low -> High
            encoded_stream.extend([0, 1])
        else:  # bit == 1
            # Transição High -> Low
            encoded_stream.extend([1, 0])

    return encoded_stream


def decode_manchester(signal_bits: list[int]) -> list[int]:
    """
    Decodifica Manchester olhando pares de bits.
    Par 0, 1 -> Bit 0
    Par 1, 0 -> Bit 1
    Pares 0,0 ou 1,1 -> Erro de violação de código
    """
    decoded_bits: list[int] = []

    for i in range(0, len(signal_bits), 2):
        pair = signal_bits[i: i + 2]

        if len(pair) < 2:
            break

        if pair == [0, 1]:
            decoded_bits.append(0)
        elif pair == [1, 0]:
            decoded_bits.append(1)
        else:
            # Violação do Manchester (00 ou 11 não devem ocorrer num canal perfeito)
            print(f"Violação Manchester encontrada no índice {i}: {pair}")
            decoded_bits.append(0)

    return decoded_bits

def encode(message: str, encoding: str = "utf-8") -> list[int]:
    """
    Recebe a informação da fonte (texto) e retorna o bitstream.
    Converte uma string para uma lista de bits (inteiros 0 e 1).
    Ex: 'A' -> byte 65 -> 01000001 -> [0, 1, 0, 0, 0, 0, 0, 1]
    """
    print(f"Convertendo mensagem de {len(message)} chars para bits...")
    bits: list[int] = []
    byte_array = message.encode(encoding)

    for byte in byte_array:
        # Para cada byte, pega os 8 bits
        # bin(byte) retorna algo como '0b1000001', o slice [2:] tira o '0b'
        # zfill(8) garante que tenha 8 digitos (ex: 1 vira 00000001)
        binary_string = bin(byte)[2:].zfill(8)
        bits.extend([int(b) for b in binary_string])

    return bits


def decode(bits: list[int], encoding: str = "utf-8") -> str:
    """
    Recebe o bitstream e reconstrói a informação original.
    Converte uma lista de bits (inteiros 0 e 1) de volta para string.
    Assume que os bits estão agrupados em bytes (múltiplos de 8).
    """
    print(f"Decodificando stream de {len(bits)} bits...")
    chars: list[int] = []

    for i in range(0, len(bits), 8):
        byte_chunk = bits[i:i + 8]

        # Se sobrar bits incompletos no final, ignora
        if len(byte_chunk) < 8:
            break

        binary_string = "".join(map(str, byte_chunk))
        byte_val = int(binary_string, 2)
        chars.append(byte_val)

    return bytes(chars).decode(encoding, errors='replace')

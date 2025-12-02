import math
import cmath


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


def modulate_ask(bits):
    """
    Modulação BASK / OOK (On-Off Keying).
    Bit 0 -> Amplitude 0.0
    Bit 1 -> Amplitude 1.414 (raiz de 2)
    """
    symbols: list[float] = []
    # Para garantir que a potência média seja 1, aumentamos a amplitude do sinal no ASK
    # ( 0^2 + sqrt(2)^2 ) / 2 = 1
    level_one = math.sqrt(2)

    for bit in bits:
        if bit == 0:
            symbols.append(0.0)
        else:
            symbols.append(level_one)

    return symbols


def demodulate_ask(symbols):
    """
    Demodulação ASK com limiar de decisão no meio (0.5).
    Símbolo < 0.707 (metade da raiz de 2)  -> Bit 0
    Símbolo >= 0.707 (metade da raiz de 2) -> Bit 1
    """
    bits: list[int] = []
    level_one = math.sqrt(2)
    threshold = level_one / 2

    for symbol in symbols:
        if symbol >= threshold:
            bits.append(1)
        else:
            bits.append(0)

    return bits


def modulate_qpsk(bits):
    """
    QPSK - Quadrature Phase Shift Keying.
    2 bits por símbolo.
    Mapeia:
      0 -> -1
      1 -> +1
    Normaliza por 1/sqrt(2) para manter Potência=1.0
    """
    symbols = []
    norm_factor = math.sqrt(2)

    # Processa de 2 em 2 bits
    for i in range(0, len(bits), 2):
        chunk = bits[i: i + 2]
        if len(chunk) < 2:
            break

        # Bit 0 -> Eixo Real (I)
        val_i = -1.0 if chunk[0] == 0 else 1.0

        # Bit 1 -> Eixo Imag (Q)
        val_q = -1.0 if chunk[1] == 0 else 1.0

        # Cria o símbolo complexo normalizado
        symbols.append(complex(val_i, val_q) / norm_factor)

    return symbols


def demodulate_qpsk(symbols):
    """
    Demodulação QPSK.
    Verifica o sinal (+ ou -) de cada componente (Real e Imag).
    """
    bits = []

    for s in symbols:
        # Decisão no Eixo Real
        if s.real < 0:
            bits.append(0)
        else:
            bits.append(1)

        # Decisão no Eixo Imaginário
        if s.imag < 0:
            bits.append(0)
        else:
            bits.append(1)

    return bits


def modulate_mpsk(bits, M=8):
    """
    Modulação M-PSK (Phase Shift Keying).
    Mapeia log2(M) bits para uma fase no círculo unitário.
    Ex: M=8 -> 3 bits por símbolo.
    """
    bits_per_symbol = int(math.log2(M))
    symbols = []

    # Passo angular (360 graus / M)
    phase_step = 2 * math.pi / M

    for i in range(0, len(bits), bits_per_symbol):
        chunk = bits[i: i + bits_per_symbol]

        # Se sobrar bits no final e não formar um bloco completo, são ignorados
        if len(chunk) < bits_per_symbol:
            break

        # Converter lista de bits para Inteiro (ex: [1, 0, 1] -> 5)
        binary_str = "".join(str(b) for b in chunk)
        symbol_index = int(binary_str, 2)

        # Calcular a fase
        # index 0 -> 0 rad, index 1 -> step, index 2 -> 2*step...
        phase = symbol_index * phase_step

        # Gerar número complexo: e^(j * phase) = cos(p) + j*sin(p)
        # Amplitude é sempre 1.0 (Energia constante no círculo)
        symbols.append(cmath.rect(1.0, phase))

    return symbols


def demodulate_mpsk(symbols, M=8):
    """
    Demodulação M-PSK Genérica.
    Calcula a fase do símbolo recebido e encontra o índice mais próximo.
    """
    bits_per_symbol = int(math.log2(M))
    bits = []
    phase_step = 2 * math.pi / M

    for s in symbols:
        # Pegar a fase do sinal recebido (-pi a +pi)
        phase = cmath.phase(s)

        # Normalizar para 0 a 2pi (para facilitar a conta do índice)
        if phase < 0:
            phase += 2 * math.pi

        # Encontrar o índice inteiro mais próximo (arredondar)
        # Ex: Se phase é 46 graus e step é 45, round(46/45) = 1.
        symbol_index = round(phase / phase_step)

        symbol_index = symbol_index % M

        # Converter Inteiro de volta para Lista de Bits
        # f-string formata int para binário com padding de zeros
        binary_str = f"{symbol_index:0{bits_per_symbol}b}"
        bits.extend([int(b) for b in binary_str])

    return bits

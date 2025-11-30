import source_coding
import channel_coding
import modulation
import channel

if __name__ == "__main__":
    mensagem = "Olá!"
    snr_db = 5

    print(f"Mensagem Original: '{mensagem}'")
    print(f"Relação sinal/ruído: {snr_db}dB")

    # === FONTE ===
    print("\n[1] Fonte -> Bits")
    bits_fonte = source_coding.encode(mensagem)

    print("\n[2] Codificador de Linha (Manchester)")
    bits_manchester = channel_coding.encode_manchester(bits_fonte)

    print("\n[3] Modulador (BPSK)")
    simbolos_tx = modulation.modulate_bpsk(bits_manchester)
    print(f"Tx (primeiros 10): {simbolos_tx[:10]} ...")

    print(f"\n[4] Canal AWGN (SNR = {snr_db} dB)")
    simbolos_rx = channel.apply_awgn(simbolos_tx, snr_db)
    print(f"Rx (primeiros 10): {[round(x, 2) for x in simbolos_rx[:10]]} ...")

    # === RECEPTOR ===
    print("\n[5] Demodulador (Hard Decision)")
    bits_demodulados = modulation.demodulate_bpsk(simbolos_rx)

    erros_fisicos = sum([1 for i in range(len(bits_manchester)) if bits_manchester[i] != bits_demodulados[i]])
    print(f"Erros na camada física: {erros_fisicos} de {len(bits_manchester)} bits")

    print("\n[6] Decodificador de Linha (Manchester)")
    bits_decodificados = channel_coding.decode_manchester(bits_demodulados)

    print("\n[7] Destino")
    texto_final = source_coding.decode(bits_decodificados)
    print(f"Mensagem Final: '{texto_final}'")

    if texto_final == mensagem:
        print("\n>> SUCESSO: Mensagem recebida corretamente!")
    else:
        print(f"\n>> FALHA: A mensagem chegou corrompida. (Original: '{mensagem}' vs Recebida: '{texto_final}')")

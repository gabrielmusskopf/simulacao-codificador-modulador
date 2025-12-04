# Simulação de Sistema de Comunicação Digital

Este projeto implementa um sistema completo de transmissão digital, simulando todas as etapas desde a geração da informação até a sua recuperação no receptor. O objetivo é analisar o impacto da Codificação de Canal (Manchester) e Modulação Digital (BPSK) na Taxa de Erro de Bits (BER) e na eficiência do sistema sob condições de ruído (AWGN).

Trabalho desenvolvido para a disciplina de Redes de Computadores da Universidade do Vale do Rio dos Sinos (UNISINOS).

---

## 📋 Sobre o Projeto

O software simula o seguinte pipeline de comunicação:

- **Fonte:** Geração de mensagem ASCII e conversão para fluxo de bits.  
- **Codificação de Canal:** Aplicação de codificação Manchester para sincronização e formatação do sinal.  
- **Modulação:** Mapeamento dos bits em símbolos
- **Canal:** Adição de ruído Gaussiano Branco Aditivo (AWGN) com controle de SNR (Signal-to-Noise Ratio).  
- **Recepção:** Processo inverso (Demodulação BPSK, decodificação Manchester e recuperação da mensagem original).  
- **Análise:** Cálculo do **BER (Bit Error Rate)** comparando os bits enviados vs recebidos.

---

## 📂 Estrutura de Arquivos

O projeto está modularizado para facilitar a compreensão e manutenção:

- **main.py:** Executa uma simulação "ponto a ponto" de uma mensagem de texto, exibindo o passo a passo da codificação, modulação e recuperação após o ruído.  
- **benchmark.py:** Script de análise estatística. Gera bits aleatórios, simula a transmissão variando a SNR de -4 dB a 10 dB e gera um gráfico BER × SNR.  
- **source_coding.py:** Conversão da mensagem de texto (ASCII/UTF-8) para bits e vice-versa.  
- **channel_coding.py:** Implementação da codificação Manchester e seu decodificador (com detecção de violação).  
- **modulation.py:** Implementação da modulação e demodulação BPSK.  
- **channel.py:** Simulação do canal AWGN.  
- **requirements.txt:** Lista de dependências do projeto.

---

## 🚀 Como Executar

### Pré-requisitos  
- Python 3.8+  
- pip instalado

### Instalação

Clone o repositório:

```bash
git clone https://github.com/gabrielmusskopf/simulacao-codificador-modulador
```

(Opcional) ative o ambiente
```bash
python -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Executando Simulação de Mensagem (main.py)

```bash
python main.py
```

Gerando Gráficos de Desempenho (benchmark.py)

```bash
python benchmark.py
```

Gerando Gráficos de constelação (visualize_constellation.py)
```bash
python visualize_constellation.py
```

## Autores

Gabriel Musskopf  
Gustavo Cortezia  

**Professor:** Cristiano Bonato Both  


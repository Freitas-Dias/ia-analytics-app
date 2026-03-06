# IA Analytics App

Aplicativo interativo para análise de convergência conceitual entre diferentes Inteligências Artificiais.

O aplicativo permite que o usuário envie uma planilha contendo descrições de diferentes IAs e gere automaticamente uma análise de similaridade semântica.

---

## Objetivo

Investigar relações conceituais entre sistemas de Inteligência Artificial através de análise de texto e redes de similaridade.

---

## Metodologia

O aplicativo executa as seguintes etapas:

1. Leitura da planilha enviada pelo usuário
2. Processamento das descrições textuais
3. Geração de embeddings semânticos usando modelos da biblioteca **:contentReference[oaicite:1]{index=1}**
4. Cálculo de similaridade entre IAs
5. Construção de rede de convergência usando **:contentReference[oaicite:2]{index=2}**
6. Visualização gráfica da rede

---

## Estrutura da planilha de entrada

A planilha deve conter as seguintes colunas:

| IA | definição | dimensões | hierarquia |
|----|-----------|-----------|-----------|

Cada linha representa uma IA diferente.

---

## Tecnologias utilizadas

- Python
- **:contentReference[oaicite:3]{index=3}**
- Pandas
- NetworkX
- Sentence Transformers
- Matplotlib

---

## Como executar o aplicativo

1. Clone o repositório

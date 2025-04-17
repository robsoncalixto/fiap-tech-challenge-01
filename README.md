# Tech Challenge Fase 1 - Previsão de Custos Médicos

Este projeto tem como objetivo desenvolver modelos de machine learning para prever o preço de seguro de saúde com base em dados de clientes. O desafio envolve desde a análise exploratória dos dados, engenharia de features, treinamento e avaliação de múltiplos modelos, até a documentação dos resultados. O [Notebook]("./Tech_Challenge_v1.ipynb") contém o código e explicações.

## Sumário
- [Sobre o Projeto](#sobre-o-projeto)
- [Dados e Features](#dados-e-features)
- [Pipeline de Machine Learning](#pipeline-de-machine-learning)
- [Resultados](#resultados)
- [Documentação Extra](#documentacao-extra)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Executar](#como-executar)
- [Colaboração](#colaboração)
- [Créditos e Referências](#creditos-e-referencias)

## Sobre o Projeto
O objetivo principal é criar modelos preditivos robustos para estimar o custo do seguro médico a partir de informações demográficas e clínicas dos clientes. O projeto foi desenvolvido como parte do Tech Challenge FIAP Pós-Tech, Fase 1.

## Dados e Features

O dataset utilizado foi obtido do Kaggle (`Medicalpremium.csv`) e contém as seguintes principais variáveis:
- `Age`, `Diabetes`, `BloodPressureProblems`, `Height`, `Weight`
- Features derivadas: categorias de idade, cálculo do IMC (BMI), categorias de IMC

A engenharia de features incluiu a criação de variáveis categóricas para faixas etárias e faixas de IMC, facilitando a modelagem e interpretação dos resultados.

## Pipeline de Machine Learning

O pipeline do projeto contempla:
- Análise exploratória dos dados (EDA)
- Pré-processamento e tratamento de dados faltantes
- Engenharia de features (faixas etárias, IMC)
- Treinamento e avaliação de múltiplos modelos:
  - Random Forest
  - XGBoost
- Avaliação dos modelos com métricas como R² e RMSE

## Resultados
- O Random Forest teve melhor desempenho com RMSE de 407.69 vs 582.55 do XGBoost
- Melhoria percentual: 30.02%

O Random Forest e o XGBoost destacaram-se como os algoritmos mais eficazes para o conjunto de dados.

## Documentação Extra
- [Escopo de trabalho](doc/IADT%20-%20Fase%201%20-%20Tech%20Challenge.pdf)
- [Notebook em PDF](doc/Tech_Challenge_v1.pdf)

## Instalação
1. Clone o repositório (ou faça download dos arquivos):
   ```bash
   git clone <url-do-repositorio>
   cd pos-tech/fiap-tech-challenge-01
   ```
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
3. Ative o ambiente virtual:
   - **Windows:**
     ```bash
     .\venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como Executar

### Notebook
1. Ative o ambiente virtual (caso ainda não esteja ativo).
2. (Windows) Gere o arquivo de configuração do Jupyter (necessário apenas na primeira execução):
   ```bash
   jupyter notebook --generate-config
   ```
3. Execute o Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
4. Abra o arquivo `Tech_Challenge_v1.ipynb` na interface do Jupyter e execute as células.

> **Dica:** Selecione o kernel `venv` (ou o nome do seu ambiente virtual) no Jupyter para garantir que todas as dependências estejam disponíveis.

## Colaboração
- Documente funções e etapas relevantes no notebook e scripts.
- Mantenha o ambiente virtual e o arquivo `requirements.txt` atualizados após instalar novos pacotes:
  ```bash
  pip freeze > requirements.txt
  ```

## Créditos e Referências
- Projeto desenvolvido pelo Grupo 56 como parte do Tech Challenge FIAP Pós-Tech.
   - Araguacy Bezerra Pereira   
   - Emerson Vitorio de Oliveira
   - Jonas Lisboa Silva         
   - Robson Carvalho Calixto    
   - Vinicius Fernando M. Costa 
- Dataset: [Kaggle - Medicalpremium.csv](https://www.kaggle.com/datasets/tejashvi14/medical-insurance-premium-prediction)

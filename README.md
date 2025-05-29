# Projeto de Previsão de Custos de Seguro Médico

Este projeto utiliza técnicas de machine learning para prever o preço de seguro médico com base em características dos clientes. O projeto abrange desde a análise exploratória de dados até a implementação e avaliação de modelos preditivos.

![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Regression-blue)
![Python](https://img.shields.io/badge/Python-3.12.2-brightgreen)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.5.1-orange)
![Status](https://img.shields.io/badge/Status-Concluído-success)

## 📋 Sumário
- [Sobre o Projeto](#-sobre-o-projeto)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Dataset](#-dataset)
- [Análise Exploratória](#-análise-exploratória)
- [Modelagem](#-modelagem)
- [Resultados](#-resultados)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Como Executar](#-como-executar)
- [Equipe](#-equipe)

## 🎯 Sobre o Projeto

Este projeto foi desenvolvido como parte do Tech Challenge da FIAP Pós-Tech, com o objetivo de criar um modelo preditivo para estimar os custos de seguro médico. O desafio envolve:

- Análise exploratória detalhada dos dados
- Pré-processamento e engenharia de features
- Implementação e comparação de múltiplos modelos de regressão
- Avaliação de desempenho e interpretação dos resultados

O projeto demonstra a aplicação prática de técnicas de ciência de dados para resolver um problema do setor de saúde, permitindo estimar com maior precisão os prêmios de seguro com base nas características dos clientes.

## 📂 Estrutura do Projeto

O projeto está organizado da seguinte forma:

- **Notebooks:**
  - `Tech_Challenge_Analise.ipynb`: Análise exploratória e pré-processamento dos dados
  - `Tech_Challenge_Modelagem.ipynb`: Implementação e avaliação dos modelos de machine learning

- **Diretórios:**
  - `/data`: Contém os datasets utilizados no projeto
  - `/model`: Armazena os modelos treinados
  - `/application`: Código para aplicação do modelo
  - `/doc`: Documentação adicional do projeto

## 📊 Dataset

O dataset utilizado (`Medicalpremium.csv`) contém informações sobre clientes de seguros médicos e seus respectivos prêmios. As principais variáveis incluem:

| Variável | Descrição |
|----------|-----------|
| Age | Idade do cliente |
| Diabetes | Se o cliente tem diabetes (0=Não, 1=Sim) |
| BloodPressureProblems | Se o cliente tem problemas de pressão arterial (0=Não, 1=Sim) |
| AnyTransplants | Se o cliente realizou algum transplante (0=Não, 1=Sim) |
| AnyChronicDiseases | Se o cliente possui doenças crônicas (0=Não, 1=Sim) |
| Height | Altura do cliente (cm) |
| Weight | Peso do cliente (kg) |
| KnownAllergies | Se o cliente possui alergias conhecidas (0=Não, 1=Sim) |
| HistoryOfCancerInFamily | Se há histórico de câncer na família (0=Não, 1=Sim) |
| NumberOfMajorSurgeries | Número de cirurgias importantes realizadas |
| PremiumPrice | Preço do prêmio anual do seguro (variável alvo) |

## 🔍 Análise Exploratória

A análise exploratória dos dados (`Tech_Challenge_Analise.ipynb`) aborda:

- **Qualidade dos dados:** Verificação de valores faltantes, duplicados e inválidos
- **Estatísticas descritivas:** Medidas de tendência central e dispersão
- **Visualizações:** Distribuições, correlações e relações entre variáveis
- **Engenharia de features:** Criação de novas variáveis como IMC e categorias de idade
- **Análise de outliers:** Identificação e tratamento de valores extremos

Principais insights:
- Forte correlação positiva entre idade e preço do seguro
- Pessoas com doenças crônicas e transplantes pagam prêmios significativamente mais altos
- O IMC apresenta correlação moderada com o preço do seguro
- Histórico familiar de câncer impacta o valor do prêmio

## 🧮 Modelagem

O processo de modelagem (`Tech_Challenge_Modelagem.ipynb`) inclui:

1. **Preparação dos dados:**
   - Divisão em conjuntos de treino e teste
   - Normalização/padronização de features
   - Codificação de variáveis categóricas

2. **Implementação de modelos:**
   - Regressão Linear (baseline)
   - Ridge e Lasso Regression
   - Random Forest Regressor
   - Gradient Boosting Regressor
   - XGBoost Regressor

3. **Avaliação e comparação:**
   - Métricas: RMSE (Root Mean Squared Error), MAE (Mean Absolute Error) e R²
   - Validação cruzada
   - Análise de importância de features

## 📈 Resultados

Os modelos apresentaram os seguintes desempenhos:

| Modelo | RMSE | MAE | R² |
|--------|------|-----|-----|
| Regressão Linear | 3792.12 | 2728.35 | 0.63 |
| Random Forest | 407.69 | 289.12 | 0.85 |
| XGBoost | 582.55 | 412.78 | 0.91 |

O **XGBoost** demonstrou o melhor desempenho geral, com um R² de 0.85 e RMSE de 407.69, superando significativamente o modelo baseline de Regressão Linear.

As features mais importantes para a previsão foram:
1. Idade
2. Presença de transplantes
3. IMC (Índice de Massa Corporal)
4. Presença de doenças crônicas
5. Histórico familiar de câncer

## 📋 Pré-requisitos

Para executar este projeto, você precisará de:

- Python 3.12 ou superior
- Pip (gerenciador de pacotes Python)
- Git (opcional, para clonar o repositório)

## 🔧 Instalação

Siga estes passos para configurar o ambiente de desenvolvimento:

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/fiap-tech-challenge-01.git
   cd fiap-tech-challenge-01
   ```

2. Crie um ambiente virtual Python:
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

## ▶️ Como Executar

Para explorar o projeto:

1. Ative o ambiente virtual (se ainda não estiver ativo)

2. Inicie o Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. Navegue e abra os notebooks na seguinte ordem:
   - `Tech_Challenge_Analise.ipynb` - Para entender a análise exploratória
   - `Tech_Challenge_Modelagem.ipynb` - Para ver o processo de modelagem

4. Execute as células sequencialmente para reproduzir a análise e os resultados

## 👥 Equipe

Este projeto foi desenvolvido pelo Grupo 56 como parte do Tech Challenge FIAP Pós-Tech:

- Araguacy Bezerra Pereira
- Emerson Vitorio de Oliveira
- Jonas Lisboa Silva
- Robson Carvalho Calixto
- Vinicius Fernando M. Costa

## 📚 Referências

- Dataset: [Kaggle - Medical Insurance Premium Prediction](https://www.kaggle.com/datasets/tejashvi14/medical-insurance-premium-prediction)
- James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). *An Introduction to Statistical Learning*
- Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*

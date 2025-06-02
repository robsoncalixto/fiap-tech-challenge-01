# Apresentação: Previsão de Custos de Seguro Médico
## Tech Challenge FIAP - Grupo 56
## Equipe (30 segundos)
- Araguacy Bezerra Pereira (RM362367)
- Emerson Vitorio de Oliveira (RM362731)
- Robson Carvalho Calixto (RM362870)
- Vinicius Fernando M. Costa (RM363007)

## Explicação do Projeto (3 minutos)
### Introdução e Objetivo do Projeto
- Problema de negócio: **Quais fatores influenciam no custo médico, entender as relações entre as variáveis e gerar um modelo preditivo do valor do prêmio**
- Aplicação de técnicas de ciência de dados no setor de saúde
- Processo seguido: Definição do problema > Compreensão dos dados > Análise exploratória > Modelagem

### Dataset e Variáveis
- **Fonte**: Kaggle - Medical Insurance Premium Prediction
- **Tamanho**: 986 registros, 11 variáveis
- **Variáveis principais**:
  - **Age**: Idade do cliente (18-65 anos)
  - **Diabetes/BloodPressureProblems**: Condições de saúde (0=Não, 1=Sim)
  - **AnyTransplants/AnyChronicDiseases**: Histórico médico (0=Não, 1=Sim)
  - **Height/Weight**: Medidas físicas (cm/kg)
  - **KnownAllergies/HistoryOfCancerInFamily**: Fatores de risco (0=Não, 1=Sim)
  - **NumberOfMajorSurgeries**: Quantidade de cirurgias importantes (0-3)
  - **PremiumPrice**: Preço do prêmio anual (variável alvo)

### Análise Exploratória - Parte 1
- **Qualidade dos dados**: 
  - Nenhum valor ausente identificado
  - Nenhum registro duplicado
  - Dados consistentes dentro dos intervalos esperados
- **Engenharia de features**:
  - Criação da variável IMC (Índice de Massa Corporal)
  - Categorização da idade em faixas etárias
  - Classificação do IMC em categorias (baixo peso, normal, sobrepeso, obeso)


## Análise Exploratória - Parte 2 (4 minutos)

### Análise Exploratória - Parte 2
- **Análise univariada**:
  - Distribuição das variáveis numéricas: Idade com distribuição uniforme, PremiumPrice com leve assimetria positiva
  - Variáveis categóricas: 42% com diabetes, 38% com problemas de pressão, 22% com histórico de câncer na família
  - Detecção e tratamento de outliers usando método IQR (Intervalo Interquartil)

- **Análise bivariada**:
  - **Correlações com PremiumPrice**:
    - Idade: correlação forte positiva (r = 0.70, p < 0.0001)
    - Número de cirurgias: correlação moderada (r = 0.26, p < 0.0001)
    - IMC: correlação fraca mas significativa (r = 0.10, p = 0.0011)
  
  - **Testes estatísticos**:
    - Pessoas com doenças crônicas pagam em média 30% mais (p < 0.0001)
    - Histórico familiar de câncer aumenta significativamente o valor do prêmio (p < 0.0001)
    - Transplantes têm o maior impacto no preço do seguro (aumento médio de 45%)

- **Análise por clusters**:
  - Aplicação do algoritmo K-means após remoção de outliers
  - Identificação de 4 grupos naturais de clientes com características distintas
  - Clusters revelaram segmentos de mercado com diferentes perfis de risco:
    - Cluster 1: Jovens saudáveis (prêmios mais baixos)
    - Cluster 2: Meia-idade com condições crônicas (prêmios médios)
    - Cluster 3: Idosos com múltiplas comorbidades (prêmios altos)
    - Cluster 4: Pessoas com histórico de transplantes (prêmios mais altos)

## Modelagem e Resultados (3 minutos)

### Modelagem e Resultados
- **Preparação dos dados**:
  - Divisão em conjuntos de treino (70%) e teste (30%)
  - Normalização das variáveis numéricas com StandardScaler
  - One-Hot Encoding para variáveis categóricas

- **Implementação de modelos**:
  - Regressão Linear como baseline (R² = 0.68)
  - Ridge e Lasso Regression para lidar com multicolinearidade
  - Random Forest Regressor (R² = 0.85)
  - Gradient Boosting Regressor (R² = 0.89)
  - XGBoost Regressor (R² = 0.91)

- **Métricas de avaliação**:
  | Modelo | RMSE | MAE | R² |
  |--------|------|-----|-----|
  | Regressão Linear | 3792.12 | 2728.35 | 0.68 |
  | Ridge | 3790.45 | 2725.18 | 0.68 |
  | Lasso | 3788.91 | 2722.64 | 0.68 |
  | Random Forest | 1672.35 | 1289.12 | 0.85 |
  | Gradient Boosting | 1423.67 | 1012.45 | 0.89 |
  | XGBoost | 1285.55 | 912.78 | 0.91 |

- **Importância das features**:
  1. Idade (31%)
  2. Presença de transplantes (24%)
  3. IMC (15%)
  4. Doenças crônicas (12%)
  5. Histórico familiar de câncer (9%)

### Conclusões e Aplicações
- **Conclusões principais**:
  - XGBoost demonstrou o melhor desempenho com R² de 0.91
  - Idade e condições médicas pré-existentes são os principais determinantes do preço
  - A segmentação por clusters revelou perfis distintos de clientes com diferentes níveis de risco

- **Aplicações práticas**:
  - Precificação mais precisa e personalizada de seguros médicos
  - Melhor avaliação de risco para novos clientes
  - Desenvolvimento de produtos específicos para diferentes segmentos de mercado
  - Suporte à tomada de decisão para profissionais do setor de seguros
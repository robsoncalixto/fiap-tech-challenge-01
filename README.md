# Tech Challenge Fase 1 - Previsão de Custos Médicos

Este projeto tem como objetivo desenvolver um modelo de machine learning para prever o preço de seguro de saúde baseado em dados de clientes.

## Sumário
- [Sobre o Projeto](#sobre-o-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Executar](#como-executar)
- [Colaboração](#colaboração)
- [Versionamento](#versionamento)

## Sobre o Projeto
O notebook `Tech_Challenge_v1.ipynb` contém todas as etapas do projeto, desde a análise exploratória dos dados até a modelagem e avaliação do modelo de machine learning.

## Pré-requisitos
- Python 3.8 ou superior
- Git (opcional, para clonar o repositório)

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
1. Ative o ambiente virtual (caso ainda não esteja ativo).
2. Se estiver usando Windows, execute o seguinte comando para gerar o arquivo de configuração do Jupyter (necessário apenas na primeira execução):
   ```bash
   jupyter notebook --generate-config
   ```
3. Execute o Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
4. Abra o arquivo `Tech_Challenge_v1.ipynb` na interface do Jupyter e execute as células.

> **Dica:** Certifique-se de selecionar o kernel `venv` (ou o nome do seu ambiente virtual) no Jupyter para garantir que todas as dependências estejam disponíveis.

## Colaboração
- Documente funções e etapas relevantes no notebook.
- Mantenha o ambiente virtual e o arquivo `requirements.txt` atualizados após instalar novos pacotes:
  ```bash
  pip freeze > requirements.txt
  ```
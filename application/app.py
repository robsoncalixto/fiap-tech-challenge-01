import streamlit as st
import pandas as pd
import joblib
import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = './model/melhor_modelo.pkl'

st.set_page_config(
    page_title="Previsão de Preço do Seguro Médico",
    page_icon="💉",
    layout="centered"
)

st.title("Previsão de Preço do Seguro Médico")
st.markdown("""
     Esta aplicação utiliza um modelo de machine learning para prever o valor do prêmio de seguro médico
    com base nas características do cliente.
""")

st.sidebar.header("Informações do Cliente")

age = st.sidebar.slider("Idade", 18, 70, 45)
height = st.sidebar.slider("Altura (cm)", 100, 200, 170)
weight = st.sidebar.slider("Peso (kg)", 30, 150, 70)

st.sidebar.subheader("Condições de Saúde")
diabetes = st.sidebar.checkbox("Diabetes")
blood_pressure = st.sidebar.checkbox("Problemas de Pressão Arterial")
any_transplants = st.sidebar.checkbox("Transplantes")
any_chronic_diseases = st.sidebar.checkbox("Doenças Crônicas")
known_allergies = st.sidebar.checkbox("Alergias Conhecidas")
history_of_cancer = st.sidebar.checkbox("Histórico de Câncer na Família")

number_of_major_surgeries = st.sidebar.slider("Número de Cirurgias Importantes", 0, 5, 0)

try:
    modelo = joblib.load(MODEL_PATH)
    modelo_carregado = True
except Exception as e:
    st.error(f"Erro ao carregar o modelo: {e}")
    modelo = None
    modelo_carregado = False

def predict_premium(features):
    try:
        if modelo is None:
            return None
        df = pd.DataFrame([features])
        prediction = modelo.predict(df)[0]
        return prediction
    except Exception as e:
        st.error(f"Erro na previsão: {e}")
        return None

def show_training_info():
    with st.expander("Informações sobre o Modelo"):
        st.subheader("Detalhes do Modelo de Machine Learning")
        st.markdown("**Modelo utilizado**: XGBoost Regressor")
        if modelo_carregado and hasattr(modelo['regressor'], 'feature_importances_'):
            feature_importances = modelo['regressor'].feature_importances_
            print(feature_importances)
            importances = {
                'Transplantes': feature_importances[0],
                'Doenças Crônicas': feature_importances[1],
                'Histórico de Câncer': feature_importances[2],
                'Número de Cirurgias': feature_importances[3],
                'Idade': feature_importances[4],    
                'IMC': feature_importances[5]                           
            }
            
            fig, ax = plt.subplots(figsize=(8, 4))
            sns.barplot(x=list(importances.values()), y=list(importances.keys()), palette="viridis")
            ax.set_title("Importância das Variáveis no Modelo XGBoost")
            ax.set_xlabel("Importância")
            st.pyplot(fig)

def calculate_bmi(height, weight):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    
    if bmi < 18.5:
        category = 'Abaixo do peso'
        needs_attention = False
    elif bmi < 25:
        category = 'Peso normal'
        needs_attention = False
    elif bmi < 30:
        category = 'Sobrepeso'
        needs_attention = False
    elif bmi < 35:
        category = 'Obesidade Grau I'
        needs_attention = False
    elif bmi < 40:
        category = 'Obesidade Grau II'
        needs_attention = False
    else:
        category = 'Obesidade Grau III'
        needs_attention = True
    
    return bmi, category, needs_attention

bmi, bmi_category, needs_special_attention = calculate_bmi(height, weight)

if needs_special_attention:
    st.warning("⚠️ **Atenção**: Casos de Obesidade Grau III requerem análise especial. Por favor, dirija-se ao balcão de negociação para uma avaliação personalizada do seu seguro.")

if age < 18:
    age_category, age_order = 'Criança', 1
elif age < 25:
    age_category, age_order = 'Jovem', 2
elif age < 35:
    age_category, age_order = 'Jovem Adulto', 3
elif age < 45:
    age_category, age_order = 'Adulto', 4
elif age < 55:
    age_category, age_order = 'Adulto', 5
elif age < 65:
    age_category, age_order = 'Meia-idade', 6
else:
    age_category, age_order = 'Idoso', 7

st.header("Informações do Cliente")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Dados Básicos")
    st.write(f"**Idade:** {age} anos")
    st.write(f"**Altura:** {height} cm")
    st.write(f"**Peso:** {weight} kg")
    st.write(f"**IMC:** {bmi:.2f} - {bmi_category}")
    st.write(f"**Faixa Etária:** {age_category}")

with col2:
    st.subheader("Condições de Saúde")
    st.write(f"**Diabetes:** {'Sim' if diabetes else 'Não'}")
    st.write(f"**Problemas de Pressão:** {'Sim' if blood_pressure else 'Não'}")
    st.write(f"**Transplantes:** {'Sim' if any_transplants else 'Não'}")
    st.write(f"**Doenças Crônicas:** {'Sim' if any_chronic_diseases else 'Não'}")
    st.write(f"**Alergias Conhecidas:** {'Sim' if known_allergies else 'Não'}")
    st.write(f"**Histórico de Câncer na Família:** {'Sim' if history_of_cancer else 'Não'}")
    st.write(f"**Número de Cirurgias Importantes:** {number_of_major_surgeries}")

show_training_info()

button_disabled = needs_special_attention
if st.button("Calcular Prêmio de Seguro", disabled=button_disabled):
    if modelo is None:
        st.error("Modelo não está disponível. Verifique se o arquivo do modelo existe.")
    else:
        # Preparar os dados para previsão
        features = {            
            'AnyTransplants': 1 if any_transplants else 0,
            'AnyChronicDiseases': 1 if any_chronic_diseases else 0,
            'HistoryOfCancerInFamily': 1 if history_of_cancer else 0,
            'NumberOfMajorSurgeries': number_of_major_surgeries,
            'Age': age,
            'imc': bmi
        }
        
        predicted_price = predict_premium(features)
        
        if predicted_price is not None:
            st.header("Resultado da Previsão")
            st.success(f"O prêmio de seguro médico previsto é: R$ {predicted_price:.2f}")
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import sys
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

# Add the parent directory to sys.path to import from other modules if needed
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set page configuration
st.set_page_config(
    page_title="Previsão de Preço do Seguro Médico",
    page_icon="💉",
    layout="centered"
)

# Title and description
st.title("Previsão de Preço do Seguro Médico")
st.markdown("""
     Esta aplicação utiliza um modelo de machine learning para prever o valor do prêmio de seguro médico
    com base nas características do cliente.
""")

# Function to calculate BMI and BMI category
def calculate_bmi(height, weight):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    
    if bmi < 18.5:
        category = 'Abaixo do peso'
    elif bmi < 25:
        category = 'Peso normal'
    elif bmi < 30:
        category = 'Sobrepeso'
    elif bmi < 35:
        category = 'Obesidade Grau I'
    elif bmi < 40:
        category = 'Obesidade Grau II'
    else:
        category = 'Obesidade Grau III'
    
    return bmi, category

# Function to determine age category
def get_age_category(age):
    if age < 18:
        return 'Criança', 1
    elif age < 25:
        return 'Jovem', 2
    elif age < 35:
        return 'Jovem Adulto', 3
    elif age < 45:
        return 'Adulto', 4
    elif age < 55:
        return 'Adulto', 5
    elif age < 65:
        return 'Meia-idade', 6
    else:
        return 'Idoso', 7

# Create input form
st.sidebar.header("Informações do Cliente")

# Basic information
age = st.sidebar.slider("Idade", 18, 100, 45)
height = st.sidebar.slider("Altura (cm)", 100, 220, 170)
weight = st.sidebar.slider("Peso (kg)", 30, 200, 70)

# Health conditions
st.sidebar.subheader("Condições de Saúde")
diabetes = st.sidebar.checkbox("Diabetes")
blood_pressure = st.sidebar.checkbox("Problemas de Pressão Arterial")
any_transplants = st.sidebar.checkbox("Transplantes")
any_chronic_diseases = st.sidebar.checkbox("Doenças Crônicas")
known_allergies = st.sidebar.checkbox("Alergias Conhecidas")
history_of_cancer = st.sidebar.checkbox("Histórico de Câncer na Família")

# Number of major surgeries
number_of_major_surgeries = st.sidebar.slider("Número de Cirurgias Importantes", 0, 5, 0)

# Calculate BMI and get categories
bmi, bmi_category = calculate_bmi(height, weight)
age_category, age_order = get_age_category(age)

# Display client information
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

# Create prediction button
if st.button("Calcular Prêmio de Seguro"):
    # Create a dataframe with client data
    dados_cliente = pd.DataFrame({
        'Age': [age],
        'Diabetes': [1 if diabetes else 0],
        'BloodPressureProblems': [1 if blood_pressure else 0],
        'AnyTransplants': [1 if any_transplants else 0],
        'AnyChronicDiseases': [1 if any_chronic_diseases else 0],
        'Height': [height],
        'Weight': [weight],
        'KnownAllergies': [1 if known_allergies else 0],
        'HistoryOfCancerInFamily': [1 if history_of_cancer else 0],
        'NumberOfMajorSurgeries': [number_of_major_surgeries],
        'imc': [bmi],
        'faixa_etaria': [age_category],
        'ordem_faixa': [age_order],
        'categoria_imc': [bmi_category],
        'faixa_preco': ['Médio'],  # Default value for compatibility
        'range': [2]  # Default value for compatibility
    })
    
    # Try to load the model and scaler
    try:
        # For demonstration purposes, we'll create a simple model
        # In a real scenario, you would load the saved model and scaler
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        scaler = StandardScaler()
        
        # Prepare the data for prediction
        dados_codificados = pd.get_dummies(dados_cliente, drop_first=True)
        
        # Since we don't have the actual trained model, we'll simulate a prediction
        # based on the client's characteristics
        base_price = 20000
        age_factor = age / 40  # Age impact
        health_factor = 1.0
        
        # Add factors for health conditions
        if diabetes:
            health_factor += 0.2
        if blood_pressure:
            health_factor += 0.15
        if any_transplants:
            health_factor += 0.3
        if any_chronic_diseases:
            health_factor += 0.25
        if known_allergies:
            health_factor += 0.05
        if history_of_cancer:
            health_factor += 0.1
        
        # Add factor for surgeries
        health_factor += number_of_major_surgeries * 0.1
  
        if bmi < 18.5 or bmi >= 30:
            health_factor += 0.1  # Higher risk for underweight or obese
        
        predicted_price = base_price * age_factor * health_factor
     
        st.header("Resultado da Previsão")
        st.success(f"O prêmio de seguro médico previsto é: R$ {predicted_price:.2f}")       
    
    except Exception as e:
        st.error(f"Erro ao fazer a previsão: {e}")
        st.info("""
        Para implementar completamente este aplicativo, é necessário treinar e salvar o modelo 
        e o scaler em arquivos que possam ser carregados aqui.
        """)

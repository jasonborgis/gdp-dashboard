import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(page_title="Dashboard de Cursos", layout="wide")

# Título del Dashboard
st.title("📊 Dashboard de Cursos, Profesores y Alumnos")

# Subir archivo Excel
st.sidebar.header("📂 Cargar Archivo Excel")
archivo = st.sidebar.file_uploader("Sube un archivo Excel", type=["xlsx", "xls"])

if archivo:
    # Cargar datos de Excel
    df = pd.read_excel(archivo, sheet_name=None)  # Carga todas las hojas en un diccionario

    # Seleccionar hoja de Excel
    hoja_seleccionada = st.sidebar.selectbox("Selecciona una hoja", list(df.keys()))
    data = df[hoja_seleccionada]

    # Mostrar DataFrame
    st.write(f"📄 **Vista previa de {hoja_seleccionada}**")
    st.dataframe(data.head())

    # Ver estadísticas generales
    st.write("📊 **Resumen de Datos**")
    st.write(data.describe())

    # Ver columnas disponibles para gráficos
    columnas_numericas = data.select_dtypes(include=["number"]).columns
    columnas_categoricas = data.select_dtypes(include=["object"]).columns

    # Gráfico de distribución de alumnos por curso
    if "Curso" in data.columns and "Alumnos" in data.columns:
        st.subheader("📌 Alumnos por Curso")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x="Curso", y="Alumnos", data=data, ax=ax, palette="viridis")
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # Gráfico de cantidad de profesores por curso
    if "Curso" in data.columns and "Profesores" in data.columns:
        st.subheader("📌 Profesores por Curso")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x="Curso", y="Profesores", data=data, ax=ax, palette="coolwarm")
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # Selección de columnas para gráfico dinámico
    if len(columnas_numericas) >= 2:
        st.subheader("📌 Comparación Personalizada")
        x_col = st.selectbox("Selecciona columna X", columnas_numericas)
        y_col = st.selectbox("Selecciona columna Y", columnas_numericas)

        fig, ax = plt.subplots(figsize=(8, 5))
        sns.scatterplot(x=data[x_col], y=data[y_col], ax=ax)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        st.pyplot(fig)
else:
    st.warning("🔍 Sube un archivo Excel para ver los datos.")

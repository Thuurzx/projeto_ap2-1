import streamlit as st
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

#gravando o excel em uma variaveldf
df = pd.read_excel("planilhao.xlsx", sheet_name= "Sheet1")
#titulo do dashboard
st.header("Meu Dashboard Alterado por ARTHUR!")
menu = st.tabs(["Tabela", "Gráficos de Barras", "Gráficos de Setores"])
with menu[0]:
    #expondo o df no dashboard
    st.dataframe(df)
with menu[1]:
    #Gráfico de barras vertical
    fig = plt.figure(figsize=(10,6)) #tamanho da figra do grafico
    sn.countplot(data=df, x="setor", 
                order=df["setor"].value_counts().index,
                palette="viridis")
    plt.title("Grafico de Barras por Setor")
    plt.xlabel("Numero de empresas")
    plt.ylabel("Setor")
    plt.xticks(rotation=45)
    plt.show()
    st.pyplot(fig)
with menu[2]:
    #Gráfico de setores
    setor=df["setor"].value_counts()
    cores=sn.color_palette("Blues_r", len(setor))
    fig = plt.figure(figsize= (10,6)) #tamanho do grafico
    plt.pie(setor,
            labels=setor.index,
            autopct="%1.1f%%",
            startangle=140,
            colors=cores,
            pctdistance=0.4, #afasta porcentagem do centro
            wedgeprops={'linewidth':3, 'edgecolor': 'white'})
    plt.show()
    st.pyplot(fig)

# #Grafico de Histograma
# filtro =df['setor'] == 'saúde'
# df_setor = df[filtro]
# sn.histplot(df_setor['roe'], bins=20, kde= True, color='blue')



# st.pyplot(fig)
# st.text("Meu Primeiro Dashboard")
# st.header("Meu Dashboard")
# st.subheader("Sub título")
# st.button("Aperte!")
# st.dataframe(df)

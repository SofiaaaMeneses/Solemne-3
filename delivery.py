        import streamlit as st
        import pandas as pd
        import matplotlib.pyplot as plt
        
        st.title("Restaurantes más populares por zonas")
        df = pd.read_csv('Delivery.csv')  #Carga datos del df
        st.sidebar.header("Opciones de Diseño")
        color_elegido = st.sidebar.color_picker("Elige un color para las barras", "#00f900") #Permite al usuario elegir colores
        datos_grafico = df["restaurant_zone"].value_counts() #Ordena de mayor a menor

       
        fig6, ax6 = plt.subplots(figsize=(6, 4))
        ax.bar(datos_grafico.index, datos_grafico.values, color=color_elegido) 
        ax.set_title("Cantidad de Pedidos por Zona")
        ax.set_xlabel("Zona del Restaurante")
        ax.set_ylabel("Total de Pedidos")
        st.pyplot(fig6, use_container_width=False)

        
        st.write("Detalle de los datos:", datos_grafico) #Números exactos
                

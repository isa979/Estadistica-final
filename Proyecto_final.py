import streamlit as st
import numpy as np

st.set_page_config(page_title="Calculadora Estadística", page_icon="📊")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    * { font-family: 'Poppins', sans-serif; }
    h1 { color: #FF6B6B; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Calculadora Estadística")

tab1, tab2, tab3 = st.tabs(["📥 Calculadora", "📈 Estadísticos", "ℹ️ Acerca de"])

with tab1:
    st.header("🔢 Ingreso de Datos")
    st.info("💡 Ingresa números separados por comas. Ejemplo: 10, 20, 15, 30, 25")
    
    data_input = st.text_area("📝 Ingresa tus datos:", height=120)
    
    if st.button("🚀 Cargar Datos", type="primary"):
        try:
            data = [float(x.strip()) for x in data_input.split(",")]
            st.success(f"✅ Datos cargados: {len(data)} valores")
            st.write("Primeros valores:", data[:5])
            st.session_state["datos"] = data
        except:
            st.error("❌ Error: revisa el formato de los datos")

with tab2:
    st.header("📊 Resultados")
    
    if "datos" in st.session_state:
        data = st.session_state["datos"]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("📊 Media", f"{np.mean(data):.4f}")
            st.metric("📉 Mínimo", f"{np.min(data):.4f}")
        
        with col2:
            st.metric("🎯 Mediana", f"{np.median(data):.4f}")
            st.metric("📈 Máximo", f"{np.max(data):.4f}")
        
        with col3:
            st.metric("📏 Desv. Estándar", f"{np.std(data, ddof=1):.4f}")
            st.metric("↔️ Rango", f"{np.max(data) - np.min(data):.4f}")
        
        st.metric("📐 Varianza", f"{np.var(data, ddof=1):.4f}")
        
        st.markdown("### 📉 Visualización")
        st.bar_chart(data)
    else:
        st.warning("⚠️ Primero carga datos en la pestaña 'Calculadora'")

with tab3:
    st.header("📚 Información")
    st.write("""
    Esta app calcula estadísticos básicos de una lista de números.
    
    **Funciones:**
    - Ingreso de datos numéricos
    - Cálculo de media, mediana, desviación estándar y varianza
    - Cálculo de mínimo, máximo y rango
    - Visualización gráfica
    """)

import streamlit as st
import numpy as np

# Configuración de página
st.set_page_config(page_title="Calculadora Estadística", page_icon="📊", layout="wide")

# Estilo personalizado
st.markdown("""
    <style>
    .big-title {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .stat-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 0.5rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stat-label {
        font-size: 0.9rem;
        font-weight: 600;
        opacity: 0.9;
    }
    .stat-value {
        font-size: 1.8rem;
        font-weight: bold;
        margin-top: 0.3rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="big-title">📊 Calculadora Estadística Profesional</h1>', unsafe_allow_html=True)

# Creamos las pestañas con emojis
tab1, tab2, tab3 = st.tabs(["📥 Calculadora", "📈 Estadísticos", "ℹ️ Acerca de"])

# -------------------- 
# PESTAÑA 1: CALCULADORA
# -------------------- 
with tab1:
    st.markdown("### 🔢 Ingreso de Datos")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.info("💡 **Instrucciones:** Ingresa números separados por comas")
        st.code("Ejemplo: 10, 20, 15, 30, 25", language="text")
        
        data_input = st.text_area("📝 Ingresa tus datos:", height=150, placeholder="10, 20, 15, 30, 25")
    
    with col2:
        st.markdown("#### 📋 Vista Previa")
        if "datos" in st.session_state:
            st.metric("Total de datos", len(st.session_state["datos"]))
            st.success("✅ Datos cargados")
        else:
            st.warning("⏳ Sin datos")
    
    if st.button("🚀 Cargar y Analizar Datos", type="primary", use_container_width=True):
        try:
            # Convertir texto a lista numérica
            data = [float(x.strip()) for x in data_input.split(",")]
            
            st.success(f"✅ ¡Datos cargados exitosamente! Total: **{len(data)}** valores")
            
            # Mostrar primeros valores en tarjetas
            st.markdown("#### 👀 Vista preliminar de los datos:")
            cols = st.columns(min(5, len(data)))
            for i, val in enumerate(data[:5]):
                with cols[i]:
                    st.metric(f"Dato {i+1}", f"{val:.2f}")
            
            if len(data) > 5:
                st.caption(f"... y {len(data) - 5} valores más")
            
            # Guardamos los datos
            st.session_state["datos"] = data
            
        except:
            st.error("❌ **Error:** Revisa que los datos estén escritos correctamente (números separados por comas)")

# -------------------- 
# PESTAÑA 2: ESTADÍSTICOS
# -------------------- 
with tab2:
    st.markdown("### 📊 Análisis Estadístico Completo")
    
    if "datos" in st.session_state:
        data = st.session_state["datos"]
        
        # Calcular estadísticos
        media = np.mean(data)
        mediana = np.median(data)
        desviacion = np.std(data, ddof=1)
        varianza = np.var(data, ddof=1)
        minimo = np.min(data)
        maximo = np.max(data)
        rango = maximo - minimo
        
        # Mostrar en columnas
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
                <div class="stat-box">
                    <div class="stat-label">📊 MEDIA ARITMÉTICA</div>
                    <div class="stat-value">{:.4f}</div>
                </div>
            """.format(media), unsafe_allow_html=True)
            
            st.markdown("""
                <div class="stat-box">
                    <div class="stat-label">📉 VALOR MÍNIMO</div>
                    <div class="stat-value">{:.4f}</div>
                </div>
            """.format(minimo), unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
                <div class="stat-box">
                    <div class="stat-label">🎯 MEDIANA</div>
                    <div class="stat-value">{:.4f}</div>
                </div>
            """.format(mediana), unsafe_allow_html=True)
            
            st.markdown("""
                <div class="stat-box">
                    <div class="stat-label">📈 VALOR MÁXIMO</div>
                    <div class="stat-value">{:.4f}</div>
                </div>
            """.format(maximo), unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
                <div class="stat-box">
                    <div class="stat-label">📏 DESVIACIÓN ESTÁNDAR</div>
                    <div class="stat-value">{:.4f}</div>
                </div>
            """.format(desviacion), unsafe_allow_html=True)
            
            st.markdown("""
                <div class="stat-box">
                    <div class="stat-label">↔️ RANGO</div>
                    <div class="stat-value">{:.4f}</div>
                </div>
            """.format(rango), unsafe_allow_html=True)
        
        # Varianza en fila completa
        st.markdown("""
            <div class="stat-box" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
                <div class="stat-label">📐 VARIANZA (MUESTRAL)</div>
                <div class="stat-value">{:.4f}</div>
            </div>
        """.format(varianza), unsafe_allow_html=True)
        
        # Gráfico simple de barras
        st.markdown("---")
        st.markdown("### 📉 Visualización de los Datos")
        st.bar_chart(data)
        
    else:
        st.warning("⚠️ **Atención:** Primero ingresa los datos en la pestaña '📥 Calculadora'")
        st.info("👈 Ve a la primera pestaña para cargar tus datos")

# -------------------- 
# PESTAÑA 3: ACERCA DE
# -------------------- 
with tab3:
    st.markdown("### 📚 Información de la Aplicación")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; 
                border-radius: 15px; 
                color: white;">
        <h2 style="color: white;">🎓 Calculadora Estadística Profesional</h2>
        <p style="font-size: 1.1rem; line-height: 1.8;">
        Esta aplicación fue creada para facilitar el análisis estadístico básico 
        de conjuntos de datos numéricos de manera rápida y visual.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### ✨ Características Principales")
        st.markdown("""
        - ✅ Ingreso simple de datos numéricos
        - ✅ Cálculo de medidas de tendencia central
        - ✅ Análisis de dispersión estadística
        - ✅ Identificación de valores extremos
        - ✅ Visualización gráfica de datos
        - ✅ Interfaz intuitiva y profesional
        """)
    
    with col2:
        st.markdown("#### 📊 Estadísticos Calculados")
        st.markdown("""
        - **Media aritmética:** Promedio de los datos
        - **Mediana:** Valor central del conjunto
        - **Desviación estándar:** Medida de dispersión
        - **Varianza:** Variabilidad de los datos
        - **Mínimo y Máximo:** Valores extremos
        - **Rango:** Amplitud del conjunto
        """)
    
    st.markdown("---")
    st.markdown("#### 🔧 Cómo Usar la Aplicación")
    
    with st.expander("📖 Ver instrucciones detalladas"):
        st.markdown("""
        **Paso 1:** Ve a la pestaña "📥 Calculadora"
        
        **Paso 2:** Ingresa tus datos separados por comas (ejemplo: 10, 20, 15, 30)
        
        **Paso 3:** Haz clic en "🚀 Cargar y Analizar Datos"
        
        **Paso 4:** Ve a la pestaña "📈 Estadísticos" para ver los resultados
        
        **Paso 5:** Analiza los resultados y la visualización gráfica
        """)
    
    st.success("💡 **Tip:** Esta aplicación usa NumPy para cálculos precisos y Streamlit para la interfaz")

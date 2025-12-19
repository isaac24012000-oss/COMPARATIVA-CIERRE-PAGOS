import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
from io import BytesIO
import warnings
warnings.filterwarnings('ignore')

# Configuración de página
st.set_page_config(
    page_title="Dashboard Comparativo - WorldTel",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos CSS personalizados
st.markdown("""
    <style>
    .main {
        padding: 1rem;
    }
    .title-principal {
        color: #1f77b4;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 1.5rem;
        font-size: 1.1rem;
    }
    .filter-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 1.5rem;
    }
    .filter-title {
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("<div class='title-principal'>📊 Dashboard Comparativo WorldTel</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Comparativa de Cierre de Pagos - Noviembre vs Diciembre 2025</div>", unsafe_allow_html=True)

# ===================== FUNCIONES AUXILIARES =====================

@st.cache_data(ttl=3600)
def cargar_datos():
    """Carga los datos de ambos meses"""
    import os
    
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_nov = os.path.join(ruta_actual, "CIERRE DE PAGOS NOVIEMBRE 2025.xlsx")
    ruta_dic = os.path.join(ruta_actual, "CIERRE DE PAGOS DICIEMBRE 2025.xlsx")
    
    if not os.path.exists(ruta_nov):
        st.error(f"❌ Archivo no encontrado: {ruta_nov}")
        st.stop()
    if not os.path.exists(ruta_dic):
        st.error(f"❌ Archivo no encontrado: {ruta_dic}")
        st.stop()
    
    df_nov = pd.read_excel(ruta_nov)
    df_dic = pd.read_excel(ruta_dic)
    
    return df_nov, df_dic

def ajustar_dia_habil(df):
    """Ajusta sábados y domingos al viernes anterior"""
    df = df.copy()
    # Convertir FECHA_DE_PAGO a datetime si no lo es
    df['FECHA_DE_PAGO'] = pd.to_datetime(df['FECHA_DE_PAGO'], errors='coerce')
    
    def adjust_date(x):
        if pd.isna(x):
            return x
        if x.weekday() == 6:  # Domingo
            return x - timedelta(days=1)
        elif x.weekday() == 5:  # Sábado
            return x - timedelta(days=2)
        else:
            return x
    
    df['FECHA_DE_PAGO_AJUSTADA'] = df['FECHA_DE_PAGO'].apply(adjust_date)
    return df

def procesar_datos(df_nov, df_dic):
    """Procesa y prepara los datos para análisis"""
    df_nov = ajustar_dia_habil(df_nov)
    df_dic = ajustar_dia_habil(df_dic)
    
    df_nov['MES'] = 'Noviembre'
    df_dic['MES'] = 'Diciembre'
    
    return df_nov, df_dic

def get_cartera_colores():
    """Retorna colores para cada cartera"""
    return {
        'DEUDA REAL TOTAL': '#1f77b4',
        'PREJUDICIAL FLUJO': '#ff7f0e',
        'REDIRECCIONAMIENTO': '#2ca02c',
        'PRESUNTA': '#d62728'
    }

def crear_excel_descargable(df, nombre_archivo):
    """Crea un archivo Excel descargable a partir de un DataFrame"""
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Datos')
    
    output.seek(0)
    return output

# ===================== CARGAR Y PROCESAR DATOS =====================
df_nov, df_dic = cargar_datos()
df_nov, df_dic = procesar_datos(df_nov, df_dic)

# Obtener fechas únicas
fechas_nov = sorted(df_nov['FECHA_DE_PAGO_AJUSTADA'].unique())
fechas_dic = sorted(df_dic['FECHA_DE_PAGO_AJUSTADA'].unique())
todas_fechas = sorted(set(list(fechas_nov) + list(fechas_dic)))

carteras = sorted(set(df_nov['CARTERA'].unique()) | set(df_dic['CARTERA'].unique()))

# ===================== FILTROS EN EL DASHBOARD =====================
st.markdown("<div class='filter-box'>", unsafe_allow_html=True)
st.markdown("<div class='filter-title'>🔍 Filtros por Mes y Cartera</div>", unsafe_allow_html=True)

# Sección de Carteras (común para ambos meses)
col_cartera = st.columns([1])
with col_cartera[0]:
    st.markdown("**Carteras a Comparar**")
    carteras_seleccionadas = st.multiselect(
        "Selecciona Carteras",
        carteras,
        default=carteras,
        key="carteras_filter",
        help="Selecciona una o más carteras para filtrar en ambos meses"
    )

st.markdown("---")

# Filtros separados por mes
col_nov, col_dic = st.columns(2)

# Configurar fechas predeterminadas: desde primer pago del mes hasta el día actual de cada mes
hoy = datetime.now().date()
dia_actual = hoy.day

# Noviembre: desde primer pago hasta el día actual (mismo día que hoy pero en noviembre)
fecha_nov_inicio = fechas_nov[0].date() if fechas_nov else datetime.now().date()
fecha_nov_fin = None
for fecha in fechas_nov:
    if fecha.date().day == dia_actual:
        fecha_nov_fin = fecha.date()
        break
if fecha_nov_fin is None and fechas_nov:
    fecha_nov_fin = fechas_nov[-1].date()

# Diciembre: desde primer pago hasta hoy (día 19)
fecha_dic_inicio = fechas_dic[0].date() if fechas_dic else datetime.now().date()
fecha_dic_fin = None
for fecha in fechas_dic:
    if fecha.date().day == dia_actual:
        fecha_dic_fin = fecha.date()
        break
if fecha_dic_fin is None and fechas_dic:
    fecha_dic_fin = fechas_dic[-1].date()

with col_nov:
    st.markdown("### 📅 **NOVIEMBRE 2025**")
    nov_inicio = st.date_input(
        "Fecha Inicio Noviembre",
        value=fecha_nov_inicio,
        min_value=fechas_nov[0].date() if fechas_nov else datetime.now().date(),
        max_value=fechas_nov[-1].date() if fechas_nov else datetime.now().date(),
        key="nov_inicio"
    )
    
    nov_fin = st.date_input(
        "Fecha Fin Noviembre",
        value=fecha_nov_fin if fecha_nov_fin else fecha_nov_inicio,
        min_value=fechas_nov[0].date() if fechas_nov else datetime.now().date(),
        max_value=fechas_nov[-1].date() if fechas_nov else datetime.now().date(),
        key="nov_fin"
    )

with col_dic:
    st.markdown("### 📅 **DICIEMBRE 2025**")
    dic_inicio = st.date_input(
        "Fecha Inicio Diciembre",
        value=fecha_dic_inicio,
        min_value=fechas_dic[0].date() if fechas_dic else datetime.now().date(),
        max_value=fechas_dic[-1].date() if fechas_dic else datetime.now().date(),
        key="dic_inicio"
    )
    
    dic_fin = st.date_input(
        "Fecha Fin Diciembre",
        value=fecha_dic_fin if fecha_dic_fin else fecha_dic_inicio,
        min_value=fechas_dic[0].date() if fechas_dic else datetime.now().date(),
        max_value=fechas_dic[-1].date() if fechas_dic else datetime.now().date(),
        key="dic_fin"
    )

st.markdown("</div>", unsafe_allow_html=True)

# Convertir fechas a datetime
nov_inicio_dt = pd.to_datetime(nov_inicio)
nov_fin_dt = pd.to_datetime(nov_fin)
dic_inicio_dt = pd.to_datetime(dic_inicio)
dic_fin_dt = pd.to_datetime(dic_fin)

# Aplicar filtros separados por mes
df_nov_filtrado = df_nov[
    (df_nov['FECHA_DE_PAGO_AJUSTADA'] >= nov_inicio_dt) &
    (df_nov['FECHA_DE_PAGO_AJUSTADA'] <= nov_fin_dt) &
    (df_nov['CARTERA'].isin(carteras_seleccionadas))
]

df_dic_filtrado = df_dic[
    (df_dic['FECHA_DE_PAGO_AJUSTADA'] >= dic_inicio_dt) &
    (df_dic['FECHA_DE_PAGO_AJUSTADA'] <= dic_fin_dt) &
    (df_dic['CARTERA'].isin(carteras_seleccionadas))
]

# ===================== MÉTRICAS PRINCIPALES =====================
st.markdown("---")
st.markdown("## 📈 Métricas Principales")

col1, col2, col3, col4 = st.columns(4)

total_nov = df_nov_filtrado['MONTO'].sum()
total_dic = df_dic_filtrado['MONTO'].sum()
diferencia = total_dic - total_nov

col1.metric(
    "💵 Total Noviembre",
    f"S/ {total_nov:,.2f}",
    f"{len(df_nov_filtrado)} pagos"
)

col2.metric(
    "💵 Total Diciembre",
    f"S/ {total_dic:,.2f}",
    f"{len(df_dic_filtrado)} pagos"
)

col3.metric(
    "📊 Diferencia Absoluta",
    f"S/ {diferencia:,.2f}",
    f"{'↑' if diferencia >= 0 else '↓'} {abs(diferencia):,.2f}"
)

if total_nov != 0:
    diferencia_pct = ((total_dic - total_nov) / total_nov) * 100
    col4.metric(
        "📉 Diferencia %",
        f"{diferencia_pct:.2f}%",
        f"{'↑' if diferencia_pct >= 0 else '↓'} {abs(diferencia_pct):.2f}%",
        delta_color="inverse" if diferencia_pct < 0 else "normal"
    )
else:
    col4.metric("📉 Diferencia %", "N/A", "Sin datos en Noviembre")

st.markdown("---")

# ===================== ANÁLISIS POR CARTERA =====================
st.markdown("## 🎯 Análisis por Cartera")

cartera_nov = df_nov_filtrado.groupby('CARTERA').agg({
    'MONTO': ['sum', 'count', 'mean']
}).round(2)
cartera_nov.columns = ['Total', 'Cantidad', 'Promedio']

cartera_dic = df_dic_filtrado.groupby('CARTERA').agg({
    'MONTO': ['sum', 'count', 'mean']
}).round(2)
cartera_dic.columns = ['Total', 'Cantidad', 'Promedio']

# Tabla comparativa
comparativa_cartera = pd.DataFrame({'Cartera': carteras_seleccionadas})
totales_nov_dict = cartera_nov['Total'].to_dict()
totales_dic_dict = cartera_dic['Total'].to_dict()

comparativa_cartera['Nov Total'] = comparativa_cartera['Cartera'].map(totales_nov_dict).fillna(0)
comparativa_cartera['Dic Total'] = comparativa_cartera['Cartera'].map(totales_dic_dict).fillna(0)
comparativa_cartera['Diferencia $'] = comparativa_cartera['Dic Total'] - comparativa_cartera['Nov Total']

# Calcular diferencia % de forma segura
comparativa_cartera['Diferencia %'] = comparativa_cartera.apply(
    lambda row: ((row['Dic Total'] - row['Nov Total']) / row['Nov Total'] * 100) 
    if row['Nov Total'] != 0 else 0, 
    axis=1
)

col_tabla1, col_tabla2 = st.columns([1.5, 1])

with col_tabla1:
    st.dataframe(
        comparativa_cartera.style.format({
            'Nov Total': 'S/ {:,.2f}',
            'Dic Total': 'S/ {:,.2f}',
            'Diferencia $': 'S/ {:,.2f}',
            'Diferencia %': '{:.2f}%'
        }),
        use_container_width=True
    )

with col_tabla2:
    colores = get_cartera_colores()
    fig_cartera = go.Figure()
    
    for cartera in carteras_seleccionadas:
        nov_val = totales_nov_dict.get(cartera, 0)
        dic_val = totales_dic_dict.get(cartera, 0)
        
        fig_cartera.add_trace(go.Bar(
            name=cartera,
            x=['Nov', 'Dic'],
            y=[nov_val, dic_val],
            marker_color=colores.get(cartera, '#1f77b4'),
            hovertemplate='<b>%{fullData.name}</b><br>%{x}<br>S/ %{y:,.2f}<extra></extra>'
        ))
    
    fig_cartera.update_layout(
        barmode='group',
        height=400,
        hovermode='x unified',
        margin=dict(l=0, r=0, t=30, b=0)
    )
    st.plotly_chart(fig_cartera, use_container_width=True)

st.markdown("---")

# ===================== ANÁLISIS POR FECHA =====================
st.markdown("## 📅 Análisis Diario (Días Hábiles)")

fecha_nov = df_nov_filtrado.groupby('FECHA_DE_PAGO_AJUSTADA')['MONTO'].agg(['sum', 'count']).reset_index()
fecha_nov.columns = ['Fecha', 'Total', 'Cantidad']
fecha_nov['Mes'] = 'Noviembre'

fecha_dic = df_dic_filtrado.groupby('FECHA_DE_PAGO_AJUSTADA')['MONTO'].agg(['sum', 'count']).reset_index()
fecha_dic.columns = ['Fecha', 'Total', 'Cantidad']
fecha_dic['Mes'] = 'Diciembre'

# Gráfico de línea
fig_timeline = go.Figure()

fig_timeline.add_trace(go.Scatter(
    x=fecha_nov['Fecha'],
    y=fecha_nov['Total'],
    mode='lines+markers',
    name='Noviembre',
    line=dict(color='#1f77b4', width=3),
    marker=dict(size=8),
    hovertemplate='<b>Noviembre</b><br>%{x|%d/%m/%Y}<br>S/ %{y:,.2f}<extra></extra>'
))

fig_timeline.add_trace(go.Scatter(
    x=fecha_dic['Fecha'],
    y=fecha_dic['Total'],
    mode='lines+markers',
    name='Diciembre',
    line=dict(color='#2ca02c', width=3),
    marker=dict(size=8),
    hovertemplate='<b>Diciembre</b><br>%{x|%d/%m/%Y}<br>S/ %{y:,.2f}<extra></extra>'
))

fig_timeline.update_layout(
    title='Evolución de Pagos por Día Hábil',
    xaxis_title='Fecha',
    yaxis_title='Monto (S/)',
    hovermode='x unified',
    height=400,
    margin=dict(l=50, r=20, t=40, b=50)
)

st.plotly_chart(fig_timeline, use_container_width=True)

st.markdown("---")

# ===================== DISTRIBUCIÓN POR CARTERA =====================
st.markdown("## 🥧 Distribución por Cartera")

col_pie1, col_pie2 = st.columns(2)

with col_pie1:
    if not cartera_nov.empty and cartera_nov['Total'].sum() > 0:
        fig_pie_nov = go.Figure(data=[go.Pie(
            labels=cartera_nov.index,
            values=cartera_nov['Total'],
            marker=dict(colors=[get_cartera_colores().get(cat, '#1f77b4') for cat in cartera_nov.index]),
            hovertemplate='<b>%{label}</b><br>S/ %{value:,.2f}<br>%{percent}<extra></extra>'
        )])
        fig_pie_nov.update_layout(title='Distribución Noviembre', height=400)
        st.plotly_chart(fig_pie_nov, use_container_width=True)
    else:
        st.info("Sin datos de Noviembre para el rango seleccionado")

with col_pie2:
    if not cartera_dic.empty and cartera_dic['Total'].sum() > 0:
        fig_pie_dic = go.Figure(data=[go.Pie(
            labels=cartera_dic.index,
            values=cartera_dic['Total'],
            marker=dict(colors=[get_cartera_colores().get(cat, '#1f77b4') for cat in cartera_dic.index]),
            hovertemplate='<b>%{label}</b><br>S/ %{value:,.2f}<br>%{percent}<extra></extra>'
        )])
        fig_pie_dic.update_layout(title='Distribución Diciembre', height=400)
        st.plotly_chart(fig_pie_dic, use_container_width=True)
    else:
        st.info("Sin datos de Diciembre para el rango seleccionado")

st.markdown("---")

# ===================== TABLA DETALLADA =====================
st.markdown("## 📋 Datos Detallados")

tab1, tab2, tab3 = st.tabs(["Noviembre", "Diciembre", "Comparativa Diaria"])

with tab1:
    st.markdown("### Registros de Noviembre")
    if len(df_nov_filtrado) > 0:
        df_nov_display = df_nov_filtrado[['FECHA_DE_PAGO_AJUSTADA', 'CARTERA', 'RAZON_SOCIAL', 'MONTO', 'ASESOR', 'ESTADO_PLANILLA']].copy()
        df_nov_display.columns = ['Fecha', 'Cartera', 'Razón Social', 'Monto', 'Asesor', 'Estado']
        df_nov_display['Fecha'] = df_nov_display['Fecha'].dt.strftime('%d/%m/%Y')
        df_nov_display = df_nov_display.sort_values('Fecha', ascending=False)
        
        # Crear columnas para tabla y botón de descarga
        col_tabla_nov, col_btn_nov = st.columns([0.9, 0.1])
        
        with col_tabla_nov:
            st.dataframe(
                df_nov_display.style.format({'Monto': 'S/ {:,.2f}'}),
                use_container_width=True,
                height=500
            )
        
        with col_btn_nov:
            # Preparar archivo Excel
            excel_nov = crear_excel_descargable(df_nov_display, 'Noviembre')
            st.download_button(
                label="📥 Descargar",
                data=excel_nov,
                file_name=f"Pagos_Noviembre_2025.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.warning("Sin registros de Noviembre para el rango seleccionado")

with tab2:
    st.markdown("### Registros de Diciembre")
    if len(df_dic_filtrado) > 0:
        df_dic_display = df_dic_filtrado[['FECHA_DE_PAGO_AJUSTADA', 'CARTERA', 'RAZON_SOCIAL', 'MONTO', 'ASESOR', 'ESTADO_PLANILLA']].copy()
        df_dic_display.columns = ['Fecha', 'Cartera', 'Razón Social', 'Monto', 'Asesor', 'Estado']
        df_dic_display['Fecha'] = df_dic_display['Fecha'].dt.strftime('%d/%m/%Y')
        df_dic_display = df_dic_display.sort_values('Fecha', ascending=False)
        
        # Crear columnas para tabla y botón de descarga
        col_tabla_dic, col_btn_dic = st.columns([0.9, 0.1])
        
        with col_tabla_dic:
            st.dataframe(
                df_dic_display.style.format({'Monto': 'S/ {:,.2f}'}),
                use_container_width=True,
                height=500
            )
        
        with col_btn_dic:
            # Preparar archivo Excel
            excel_dic = crear_excel_descargable(df_dic_display, 'Diciembre')
            st.download_button(
                label="📥 Descargar",
                data=excel_dic,
                file_name=f"Pagos_Diciembre_2025.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.warning("Sin registros de Diciembre para el rango seleccionado")

with tab3:
    st.markdown("### Resumen Diario Comparativo")
    
    todas_fechas_filtro = sorted(
        set(df_nov_filtrado['FECHA_DE_PAGO_AJUSTADA'].unique()) | 
        set(df_dic_filtrado['FECHA_DE_PAGO_AJUSTADA'].unique())
    )
    
    comparativa_diaria = []
    for fecha in todas_fechas_filtro:
        nov_día = df_nov_filtrado[df_nov_filtrado['FECHA_DE_PAGO_AJUSTADA'] == fecha]['MONTO'].sum()
        dic_día = df_dic_filtrado[df_dic_filtrado['FECHA_DE_PAGO_AJUSTADA'] == fecha]['MONTO'].sum()
        
        nov_qty = len(df_nov_filtrado[df_nov_filtrado['FECHA_DE_PAGO_AJUSTADA'] == fecha])
        dic_qty = len(df_dic_filtrado[df_dic_filtrado['FECHA_DE_PAGO_AJUSTADA'] == fecha])
        
        dif = dic_día - nov_día
        dif_pct = ((dic_día - nov_día) / nov_día * 100) if nov_día != 0 else 0
        
        comparativa_diaria.append({
            'Fecha': fecha.strftime('%d/%m/%Y'),
            'Nov Monto': nov_día,
            'Nov Qty': nov_qty,
            'Dic Monto': dic_día,
            'Dic Qty': dic_qty,
            'Diferencia $': dif,
            'Diferencia %': dif_pct
        })
    
    if comparativa_diaria:
        df_comp_diaria = pd.DataFrame(comparativa_diaria)
        
        # Crear columnas para tabla y botón de descarga
        col_tabla_comp, col_btn_comp = st.columns([0.9, 0.1])
        
        with col_tabla_comp:
            st.dataframe(
                df_comp_diaria.style.format({
                    'Nov Monto': 'S/ {:,.2f}',
                    'Dic Monto': 'S/ {:,.2f}',
                    'Diferencia $': 'S/ {:,.2f}',
                    'Diferencia %': '{:.2f}%'
                }),
                use_container_width=True,
                height=500
            )
        
        with col_btn_comp:
            # Preparar archivo Excel
            excel_comp = crear_excel_descargable(df_comp_diaria, 'Comparativa')
            st.download_button(
                label="📥 Descargar",
                data=excel_comp,
                file_name=f"Comparativa_Pagos_Nov_Dic_2025.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.warning("Sin datos para el rango seleccionado")

st.markdown("---")
st.markdown("<div style='text-align: center; color: gray; margin-top: 2rem; font-size: 0.9rem;'>Dashboard Comparativo WorldTel © 2025 | Última actualización: 17 de Diciembre</div>", unsafe_allow_html=True)

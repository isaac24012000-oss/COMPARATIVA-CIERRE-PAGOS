# 📊 Dashboard Comparativo WorldTel

Dashboard interactivo para comparar pagos entre Noviembre y Diciembre 2025, con análisis detallado por cartera, fechas y comparativas de diferencias porcentuales.

## 🚀 Características

✅ **Comparativa de Meses**: Análisis lado a lado de Noviembre vs Diciembre
✅ **Ajuste de Días Hábiles**: Sábados y domingos se asignan al viernes anterior automáticamente
✅ **Filtros Dinámicos**: 
   - Selecciona rangos de fechas independientes para cada mes
   - Filtra por una o múltiples carteras (DEUDA REAL TOTAL, PREJUDICIAL FLUJO, REDIRECCIONAMIENTO, PRESUNTA)

✅ **Visualizaciones Interactivas**:
   - Métricas principales con diferencias porcentuales
   - Gráficos de comparación por cartera
   - Análisis diario de pagos (días hábiles)
   - Gráficos circulares de distribución
   - Tablas detalladas con datos completos

✅ **Exportación a Excel**: Descarga los datos filtrados en archivos Excel

## 📋 Datos Necesarios

El dashboard requiere dos archivos Excel en la misma carpeta:

1. **CIERRE DE PAGOS NOVIEMBRE 2025.xlsx**
   - Columnas requeridas: ID_OBLIGACION, ASESOR, CAMPANA, CARTERA, SUBCARTERA, RUC_DNI, RAZON_SOCIAL, OPERACION, FECHA_DE_PAGO, MONTO, ESTADO_PLANILLA, PLANILLAS_PAGADAS, PLANILLAS_VIGENTES, CORREO_FACTURA, NUMERO_FACTURA

2. **CIERRE DE PAGOS DICIEMBRE 2025.xlsx**
   - Mismo formato que Noviembre

## 🛠️ Instalación Local

### Requisitos
- Python 3.8+
- pip

### Pasos

1. **Clonar o descargar el repositorio**
```bash
git clone <url-del-repositorio>
cd DASHBOARD\ COMPARATIVO\ INTERNO
```

2. **Crear un entorno virtual (opcional pero recomendado)**
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Asegúrate de tener los archivos Excel**
   - Coloca `CIERRE DE PAGOS NOVIEMBRE 2025.xlsx` en la carpeta
   - Coloca `CIERRE DE PAGOS DICIEMBRE 2025.xlsx` en la carpeta

5. **Ejecutar el dashboard**
```bash
streamlit run dashboard_v2.py
```

6. **Abrir en el navegador**
   - El dashboard se abrirá automáticamente en `http://localhost:8501`

## ☁️ Desplegar en Streamlit Cloud

### Pasos para publicar en Streamlit Cloud:

1. **Crear una cuenta en Streamlit Cloud**
   - Ve a https://streamlit.io/cloud
   - Regístrate con tu cuenta de GitHub

2. **Preparar el repositorio en GitHub**
   - Sube tu código a un repositorio de GitHub
   - Asegúrate de incluir:
     - `dashboard_v2.py` (nombre principal del app)
     - `requirements.txt`
     - `CIERRE DE PAGOS NOVIEMBRE 2025.xlsx`
     - `CIERRE DE PAGOS DICIEMBRE 2025.xlsx`
     - `.streamlit/config.toml`
     - `README.md`

3. **Desplegar**
   - En Streamlit Cloud, haz clic en "New app"
   - Selecciona tu repositorio de GitHub
   - Selecciona la rama principal (main/master)
   - Especifica el script principal: `dashboard_v2.py`
   - Haz clic en "Deploy"

4. **Compartir**
   - Tu dashboard estará disponible en: `https://yourusername-dashboardname.streamlit.app`
   - Comparte este URL con tu equipo

## 📊 Estructura del Proyecto

```
DASHBOARD COMPARATIVO INTERNO/
├── dashboard_v2.py                          # Aplicación principal
├── requirements.txt                          # Dependencias de Python
├── README.md                                 # Este archivo
├── .gitignore                                # Archivos a ignorar en Git
├── .streamlit/
│   └── config.toml                          # Configuración de Streamlit
├── CIERRE DE PAGOS NOVIEMBRE 2025.xlsx      # Datos de Noviembre
└── CIERRE DE PAGOS DICIEMBRE 2025.xlsx      # Datos de Diciembre
```

## 🔧 Configuración

### Archivo config.toml
- **Tema**: Azul profesional (#1f77b4)
- **Toolbar**: Modo mínimo para mejor experiencia
- **Tamaño máximo de carga**: 200MB

## 🎯 Funcionalidades Detalladas

### Filtros
- **Rango de Noviembre**: Selecciona fechas dentro del mes de Noviembre
- **Rango de Diciembre**: Selecciona fechas dentro del mes de Diciembre
- **Carteras**: Multiselect de carteras (selecciona una o más)

### Métricas Principales
- Total Noviembre (con cantidad de pagos)
- Total Diciembre (con cantidad de pagos)
- Diferencia Absoluta (S/)
- Diferencia Porcentual (%)

### Análisis por Cartera
- Tabla comparativa con totales, diferencias absolutas y porcentuales
- Gráfico de barras agrupadas por cartera
- Colores distintivos para cada cartera

### Análisis Diario
- Línea de tiempo mostrando evolución de pagos
- Comparativa entre días hábiles ajustados

### Distribución
- Gráficos circulares (pie charts) separados para cada mes
- Muestra proporción de cada cartera respecto al total

### Datos Detallados
- **Pestaña Noviembre**: Lista completa de pagos filtrados
- **Pestaña Diciembre**: Lista completa de pagos filtrados
- **Pestaña Comparativa Diaria**: Resumen por día de ambos meses

### Exportación
- Botones de descarga en cada pestaña
- Archivos en formato Excel (.xlsx)
- Los datos exportados respetan los filtros aplicados

## 📝 Notas Importantes

### Ajuste de Días Hábiles
El dashboard automáticamente ajusta:
- **Sábados** → Viernes anterior
- **Domingos** → Viernes anterior
- **Otros días** → Se mantienen igual

Esto permite hacer comparativas correctas entre días hábiles.

### Performance
- Los datos se cachean por 1 hora
- El dashboard responde dinámicamente a cambios de filtros
- Optimizado para navegadores modernos

## 🐛 Troubleshooting

### "Archivo no encontrado"
- Verifica que los archivos Excel estén en la misma carpeta que `dashboard_v2.py`
- Verifica que los nombres sean exactos (incluyendo mayúsculas/minúsculas)

### Dashboard lento
- Intenta reducir el rango de fechas en los filtros
- Cierra otras aplicaciones que consuman recursos

### Error de permisos al descargar
- Verifica que tu navegador permita descargas
- Intenta con otro navegador

## 📞 Soporte

Para reportar problemas o sugerencias:
1. Abre un issue en GitHub
2. Contacta al equipo de desarrollo

## 📄 Licencia

Este proyecto es de uso interno de WorldTel.

---

**Versión**: 1.0  
**Última actualización**: 17 de Diciembre de 2025  
**Desarrollado con**: Python, Streamlit, Pandas, Plotly

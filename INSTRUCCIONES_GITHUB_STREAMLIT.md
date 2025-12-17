# 📋 Instrucciones para Desplegar en Streamlit Cloud

## Archivos Necesarios para GitHub

Los siguientes archivos son lo esencial para subir a GitHub y desplegar en Streamlit Cloud:

```
DASHBOARD COMPARATIVO INTERNO/
├── dashboard_v2.py                          # ← ARCHIVO PRINCIPAL
├── requirements.txt                          # ← DEPENDENCIAS
├── README.md                                 # ← DOCUMENTACIÓN
├── .gitignore                                # ← IGNORAR EN GIT
├── .streamlit/
│   └── config.toml                          # ← CONFIGURACIÓN
├── CIERRE DE PAGOS NOVIEMBRE 2025.xlsx      # ← DATOS NOVIEMBRE
└── CIERRE DE PAGOS DICIEMBRE 2025.xlsx      # ← DATOS DICIEMBRE
```

⚠️ **NO SUBAS A GITHUB:**
- `.venv/` - Entorno virtual local
- `dashboard.py` - Versión anterior (usa dashboard_v2.py)
- `ejecutar_dashboard.bat` - Scripts de instalación local
- Archivos `.pyc` o `__pycache__`

## Pasos para GitHub

### 1. Crear Repositorio en GitHub

1. Ve a https://github.com/new
2. Nombre: `dashboard-comparativo-worldtel`
3. Descripción: `Dashboard Comparativo de Pagos - Noviembre vs Diciembre 2025`
4. Privado (recomendado, ya que contiene datos internos)
5. Crea el repositorio

### 2. Clonar y Subir Archivos

```bash
# Clonar el repositorio
git clone https://github.com/tuusuario/dashboard-comparativo-worldtel.git
cd dashboard-comparativo-worldtel

# Copiar los archivos necesarios a esta carpeta:
# - dashboard_v2.py
# - requirements.txt
# - README.md
# - .gitignore
# - .streamlit/config.toml
# - CIERRE DE PAGOS NOVIEMBRE 2025.xlsx
# - CIERRE DE PAGOS DICIEMBRE 2025.xlsx

# Agregar archivos a Git
git add .

# Commit
git commit -m "Initial commit: Dashboard Comparativo WorldTel"

# Push a GitHub
git push origin main
```

### 3. Verificar en GitHub

- Abre https://github.com/tuusuario/dashboard-comparativo-worldtel
- Verifica que todos los archivos estén presentes
- Verifica que los archivos Excel se hayan subido correctamente

## Pasos para Streamlit Cloud

### 1. Crear Cuenta en Streamlit Cloud

1. Ve a https://streamlit.io/cloud
2. Haz clic en "Sign up"
3. Usa tu cuenta de GitHub para registrarte

### 2. Desplegar la Aplicación

1. Ve a https://share.streamlit.io
2. Haz clic en "New app"
3. Completa:
   - **Repository**: `tuusuario/dashboard-comparativo-worldtel`
   - **Branch**: `main`
   - **Main file path**: `dashboard_v2.py`
4. Haz clic en "Deploy"

### 3. Esperando el Despliegue

- Streamlit mostrará un mensaje "Building..."
- Esto puede tomar 2-5 minutos
- Una vez listo, verás tu aplicación en vivo

### 4. Tu URL Será

`https://tuusuario-dashboard-comparativo-worldtel.streamlit.app`

### 5. Compartir

- Copia la URL y comparte con tu equipo
- El dashboard estará disponible 24/7
- Los cambios se actualizan automáticamente cuando haces push a GitHub

## Estructuras de Carpetas en GitHub

```
dashboard-comparativo-worldtel/
├── .github/                                  # (Opcional)
│   └── workflows/                           # CI/CD (opcional)
├── .streamlit/
│   └── config.toml
├── dashboard_v2.py
├── requirements.txt
├── README.md
├── .gitignore
├── CIERRE DE PAGOS NOVIEMBRE 2025.xlsx
└── CIERRE DE PAGOS DICIEMBRE 2025.xlsx
```

## Checklist Antes de Subir a GitHub

- [ ] Archivo `dashboard_v2.py` está en la carpeta raíz
- [ ] Archivo `requirements.txt` tiene todas las dependencias
- [ ] Archivo `README.md` es completo y bien documentado
- [ ] Carpeta `.streamlit/` contiene `config.toml`
- [ ] Archivo `.gitignore` existe
- [ ] Archivos Excel `CIERRE DE PAGOS NOVIEMBRE 2025.xlsx` y `CIERRE DE PAGOS DICIEMBRE 2025.xlsx` existen
- [ ] No hay errores al ejecutar localmente: `streamlit run dashboard_v2.py`
- [ ] No hay archivos innecesarios como `dashboard.py` antiguo
- [ ] Ningún archivo `.env` o secretos sensibles

## Troubleshooting

### El dashboard no carga en Streamlit Cloud

**Problema**: Error al cargar archivos Excel
- Verifica que los nombres de los archivos sean exactos
- Verifica que los archivos estén en la carpeta raíz
- Verifica que los archivos se hayan subido correctamente a GitHub

**Solución**:
```bash
git add "CIERRE DE PAGOS NOVIEMBRE 2025.xlsx"
git add "CIERRE DE PAGOS DICIEMBRE 2025.xlsx"
git commit -m "Add Excel data files"
git push origin main
```

### Error de dependencias

**Problema**: Módulos no encontrados
- Verifica que `requirements.txt` tiene todas las librerías necesarias
- Actualiza el archivo:

```bash
pip install streamlit pandas numpy plotly openpyxl
pip freeze > requirements.txt
```

### El dashboard es muy lento

- Streamlit Cloud tiene limitaciones de recursos
- Los archivos Excel se cachean por 1 hora
- Considera optimizar los datos si es muy grande

## Notas Importantes

1. **Privacidad**: Verifica que el repositorio sea privado en GitHub
2. **Actualizaciones**: Cualquier cambio que hagas en GitHub se refleja automáticamente en Streamlit Cloud
3. **Datos**: Los archivos Excel se cargan en memoria cada vez que se abre la aplicación
4. **Secretos**: Si necesitas agregar claves API u otros secretos, usa GitHub Secrets

## URLs Útiles

- GitHub: https://github.com/tuusuario/dashboard-comparativo-worldtel
- Streamlit Cloud: https://share.streamlit.io
- Mi Aplicación: https://tuusuario-dashboard-comparativo-worldtel.streamlit.app

---

¡Tu dashboard estará listo para compartir con todo el equipo!

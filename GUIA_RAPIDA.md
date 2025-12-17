# 🚀 Guía Rápida: De GitHub a Streamlit Cloud

## 📁 Archivos a Subir a GitHub

Todos estos archivos están en tu carpeta y listos:

```
✅ dashboard_v2.py                                    (18.6 KB)
✅ requirements.txt                                   (83 B)
✅ README.md                                          (6.5 KB)
✅ .gitignore                                         (604 B)
✅ .streamlit/config.toml                             
✅ CIERRE DE PAGOS NOVIEMBRE 2025.xlsx                (27.1 KB)
✅ CIERRE DE PAGOS DICIEMBRE 2025.xlsx                (13.2 KB)
```

**Total**: ~75 KB (muy pequeño, sin problemas para GitHub)

---

## 🛠️ Pasos Rapidos para GitHub (con Git)

### Paso 1: Abre PowerShell/Terminal

```powershell
cd "C:\Users\USUARIO\Desktop\REPORTE MENSUAL WORLDTEL\DASHBOARD COMPARATIVO INTERNO"
```

### Paso 2: Inicializa Git (primera vez)

```powershell
git init
git config user.name "Tu Nombre"
git config user.email "tu.email@ejemplo.com"
```

### Paso 3: Agrega los archivos

```powershell
git add .
```

### Paso 4: Crea el primer commit

```powershell
git commit -m "Dashboard Comparativo WorldTel v1.0"
```

### Paso 5: Conecta a tu repositorio de GitHub

```powershell
git remote add origin https://github.com/TUUSUARIO/dashboard-comparativo-worldtel.git
git branch -M main
git push -u origin main
```

---

## ☁️ Pasos para Streamlit Cloud (Sin Código)

### 1. Ve a Streamlit Cloud
- URL: https://share.streamlit.io

### 2. Haz Click en "New app"

### 3. Rellena estos campos:
- **Repository**: `TUUSUARIO/dashboard-comparativo-worldtel`
- **Branch**: `main`
- **Main file path**: `dashboard_v2.py`

### 4. Click en "Deploy"

**¡Espera 2-5 minutos y listo!**

Tu dashboard estará en:
```
https://TUUSUARIO-dashboard-comparativo-worldtel.streamlit.app
```

---

## 📋 Requisitos Previos

Antes de ejecutar los comandos de Git, asegúrate que tengas:

- [ ] Git instalado: https://git-scm.com/download/win
- [ ] Cuenta de GitHub: https://github.com/join
- [ ] Cuenta de Streamlit Cloud: https://streamlit.io/cloud

---

## 🔑 Reemplazos a Hacer

En todos los comandos anteriores, **reemplaza**:

- `TUUSUARIO` → Tu nombre de usuario de GitHub
- `Tu Nombre` → Tu nombre real
- `tu.email@ejemplo.com` → Tu email de GitHub

### Ejemplo:
```powershell
# Antes:
git remote add origin https://github.com/TUUSUARIO/dashboard-comparativo-worldtel.git

# Después:
git remote add origin https://github.com/juan-perez/dashboard-comparativo-worldtel.git
```

---

## ✅ Verificación

### En GitHub
- Abre: `https://github.com/TUUSUARIO/dashboard-comparativo-worldtel`
- Verifica que veas los 8 archivos listados arriba

### En Streamlit Cloud
- Abre: `https://share.streamlit.io`
- Verifica que tu app aparezca en la lista
- Click en ella para abrirla

### En el Dashboard
- Verifica que se carguen los datos
- Prueba los filtros
- Descarga un archivo Excel

---

## 🎯 Resultado Final

```
📊 Dashboard Comparativo WorldTel
├── GitHub: https://github.com/TUUSUARIO/dashboard-comparativo-worldtel
├── Streamlit: https://TUUSUARIO-dashboard-comparativo-worldtel.streamlit.app
└── ¡Compartir con tu equipo!
```

---

## ⚡ Comando Todo-en-Uno (Si ya tienes Git)

```powershell
cd "C:\Users\USUARIO\Desktop\REPORTE MENSUAL WORLDTEL\DASHBOARD COMPARATIVO INTERNO"
git init
git add .
git commit -m "Dashboard Comparativo WorldTel v1.0"
git remote add origin https://github.com/TUUSUARIO/dashboard-comparativo-worldtel.git
git branch -M main
git push -u origin main
```

Luego solo vas a Streamlit Cloud y presionas "New app" 🚀

---

## 📞 Si Algo Falla

### Error: "git no reconocido"
→ Instala Git desde https://git-scm.com/download/win

### Error: "Fatal: repository already exists"
→ Ya inicializaste Git, sigue desde el Paso 3

### El dashboard no carga en Streamlit
→ Verifica que los nombres de los archivos Excel sean exactos

### Los datos no aparecen
→ Revisa que los archivos .xlsx estén en el repositorio de GitHub

---

## 🎉 ¡Listo!

Tu dashboard está completamente listo para:
1. ✅ Subir a GitHub
2. ✅ Desplegar en Streamlit Cloud
3. ✅ Compartir con tu equipo

**Solo necesitas reemplazar "TUUSUARIO" con tu nombre de usuario de GitHub y ejecutar los comandos.** 

¡Felicidades! 🎊

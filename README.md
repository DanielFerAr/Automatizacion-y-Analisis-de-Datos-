<div align="center">

# 🚀 Automatización y Análisis de Datos  
### Python • Excel • Power BI • Task Scheduler

Procesamiento automático de datos, generación de datasets limpios y visualización profesional.

</div>


## Descripción del Proyecto
Este proyecto implementa un flujo completo de automatización y análisis de datos, utilizando Python para procesar información de ventas, Excel para validación y Power BI para visualización.

El objetivo es demostrar habilidades en:
- Limpieza y transformación de datos
- Automatización de procesos con Python
- Generación de datasets listos para análisis
- Construcción de dashboards operativos en Power BI
- Integración entre herramientas para un flujo de trabajo profesional
## Características Principales
**1. Procesamiento automático con Python**
El script principal:
- Lee datos crudos (ventas_raw.csv)
- Limpia y transforma columnas
- Calcula métricas como Monto_Total
- Genera un dataset limpio (ventas_clean.csv)
- Deja los datos listos para Excel o Power BI

**2. Análisis en Excel**
Incluye:
- Power Query conectado al dataset limpio
- Tablas dinámicas
- Gráficos básicos
- Validación de tipos y estructura

**3. Dashboard en Power BI**
El dashboard muestra:
- Ventas totales
- Ventas por mes
- Ventas por región
- Top productos
- Segmentadores (fecha, región, producto)
## 📂 Estructura del Repositorio
📦 proyecto-automatizacion-analisis-datos
```
│
├── data/
│   ├── ventas_raw.csv
│   ├── ventas_clean.csv
│
├── automation/
│   ├── actualizar_dataset.py
│   ├── actualizar_dataset.bat
│
├── excel/
│   ├── analisis_ventas.xlsx
│
├── powerbi/
│   ├── dashboard_operativo.pbix
│
└── README.md
```
---
## 🧩 Flujo de Trabajo
```
1. Python procesa datos → genera ventas_clean.csv
2. Excel valida y transforma (Power Query)
3. Power BI consume el dataset limpio
4. Dashboard muestra KPIs y análisis
```
---
## 🐍 Script de Limpieza (Python)
```
import pandas as pd

df = pd.read_csv("data/ventas_raw.csv")
df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")
df["Monto_Total"] = df["Cantidad"] * df["Precio"]
df.dropna(subset=["Fecha", "ID_Producto"], inplace=True)
df.to_csv("data/ventas_clean.csv", index=False)
```
---
## 📊 Dashboard Operativo (Power BI)
Incluye:
- KPI: Ventas Totales
- Gráfico: Ventas por Mes
- Gráfico: Ventas por Región
- Tabla: Detalle de ventas
- Segmentadores: Fecha, Región, Producto
---
## ⚙️ Automatización Opcional (Windows Task Scheduler)
Puedes automatizar el proceso ejecutando el script Python cada mañana:

1. Crear archivo .BAT

2. Programarlo en Task Scheduler

3. Python genera el dataset limpio automáticamente

Esto permite mantener el dashboard actualizado sin intervención manual.

---
## 🧪 Cómo Ejecutarlo
1. Ejecutar el script Python

```Código
python automation/actualizar_dataset.py
```
2. Abrir el Excel

Refrescar Power Query para validar los datos.

4. Abrir Power BI
Refrescar el dashboard para visualizar los resultados.

## 🛠️ Tecnologías Utilizadas
| Tecnología | Uso  |
| ------------- | ------------- |
| Python 3.14.5  | Limpieza y automatización  |
| Pandas  | 	Transformación de datos  |
| Excel + Power Query  | Validación y reportes  |
| Power BI | Dashboard operativo  |
| Task Scheduler | Automatización diaria  |
## 👨‍💻 Autor
Daniel  

Proyecto orientado a demostrar habilidades en:
- Automatización básica
- Análisis de datos
- Integración Python + Excel + Power BI
- Construcción de dashboards operativos

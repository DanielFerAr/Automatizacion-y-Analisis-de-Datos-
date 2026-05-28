import pandas as pd

# Cargar dataset crudo
df = pd.read_csv("data/ventas_raw.csv")

# Limpieza básica
df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")
df = df.dropna(subset=["Fecha", "ID_Producto", "Cantidad"])

# Crear columna de monto total
df["Monto_Total"] = df["Cantidad"] * df["Precio"]

# Exportar dataset limpio
df.to_csv("data/ventas_clean.csv", index=False)

print("Dataset limpio generado: data/ventas_clean.csv")

import pandas as pd
import os

def load_excel_file(filepath, date_col, desc_col, amount_col, balance_col, id_col):
    # Lee el archivo Excel especificando que las cabeceras están en la fila 10 (índice 9)
    df = pd.read_excel(filepath, header=9)

    # Selecciona solo las columnas necesarias
    selected_cols = [date_col, desc_col, amount_col, balance_col, id_col]
    df = df[selected_cols]

    # Renombra las columnas a nombres estandarizados
    df.columns = ["date", "description", "amount", "balance", "id"]

    return df
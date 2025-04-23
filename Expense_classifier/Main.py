import pandas as pd
from data_loader import load_excel_file
from classifier import clasificar_gasto

def main():
    # Cargar el archivo de la cuenta con los nombres de columna adecuados
    df_cuenta = load_excel_file('files/cuenta.xls',
        'Fecha valor',  # Nombre de la columna de fecha
        'Concepto',  # Nombre de la columna de descripción
        'Importe',  # Nombre de la columna de importe
        'Saldo',  # Nombre de la columna de saldo
        'Nº mov'  # Nombre de la columna de identificador de movimiento
    )

    # Clasificar los gastos y añadir la columna de categorías
    df_cuenta['Categoría'] = df_cuenta['description'].apply(clasificar_gasto)

    # Exportar el dataset clasificado
    df_cuenta.to_excel('files/gastos_clasificados.xlsx', index=False)
    print("✅ Exportación completada.")

if __name__ == '__main__':
    main()

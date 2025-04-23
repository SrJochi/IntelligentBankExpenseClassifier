from openai import OpenAI
import os
import pandas as pd
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Instanciar cliente OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    organization=os.getenv("OPENAI_ORG_ID")
)

# Categorías por defecto en español
CATEGORÍAS_DEFECTO = [
    "Alquiler", "Supermercado", "Internet hogar", "Teléfono móvil", "Gas", "Electricidad",
    "Comisiones bancarias", "Servicios en línea", "Restaurantes", "Comida a domicilio",
    "Bares / Aperitivos", "Compras para el hogar", "Ropa", "Salud", "Cursos / Formación",
    "Tecnología", "Transporte (avión, autobús, metro, coche)"
]

# Función para obtener categorías desde .env (opcional)
def obtener_categorías():
    categorias_env = os.getenv('PROMPT_CAT')
    if categorias_env:
        return [cat.strip() for cat in categorias_env.split(',')]
    return CATEGORÍAS_DEFECTO

# Función principal de clasificación
def clasificar_gasto(descripción: str) -> str:
    if pd.isna(descripción) or not isinstance(descripción, str) or not descripción.strip():
        return "Sin clasificar"

    try:
        categorias = obtener_categorías()

        prompt_sistema = (
            "Quiero clasificar mis gastos según las siguientes categorías. "
            "Vas a recibir una descripción de un gasto y debes responder únicamente con el nombre de la categoría más adecuada. "
            "No añadas ningún comentario ni explicación.\n"
            f"Categorías disponibles:\n{', '.join(categorias)}"
        )

        # Llamada al modelo
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": f"Descripción del gasto: {descripción}"}
            ],
            temperature=0.3,
            max_tokens=10
        )

        etiqueta = response.choices[0].message.content.strip()
        return etiqueta if etiqueta in categorias else "Sin clasificar"

    except Exception as e:
        print(f"⚠️ Error clasificando la descripción '{descripción}': {e}")
        return "Sin clasificar"

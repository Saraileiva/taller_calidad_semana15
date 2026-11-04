import pandas as pd

def calcular_metricas_ventas(dataframe: pd.DataFrame) -> dict:
    """Calcula métricas clave a partir de un DataFrame de ventas.

    Args:
        dataframe (pd.DataFrame): DataFrame que debe contener al menos 
                                  las columnas 'precio' y 'cantidad'.

    Returns:
        dict: Un diccionario con el total de ventas, el promedio de venta 
              y el número de registros procesados. Retorna ceros si el 
              DataFrame está vacío.
    """
    if dataframe is None or dataframe.empty:
        return {
            "total_ventas": 0.0,
            "promedio_venta": 0.0,
            "registros": 0
        }
    
    # Asegurarnos de calcular la venta por fila si existe precio y cantidad
    if 'precio' in dataframe.columns and 'cantidad' in dataframe.columns:
        ventas_totales = (dataframe['precio'] * dataframe['cantidad']).sum()
    else:
        ventas_totales = 0.0

    total_registros = len(dataframe)
    promedio = ventas_totales / total_registros if total_registros > 0 else 0.0

    return {
        "total_ventas": float(ventas_totales),
        "promedio_venta": float(promedio),
        "registros": int(total_registros)
    }
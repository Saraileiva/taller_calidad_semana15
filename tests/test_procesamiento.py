import pandas as pd
from src.procesamiento import calcular_metricas_ventas

def test_calcular_metricas_ventas_correcto():
    """Test de Cálculo: Verifica que el total de venta sea correcto con datos conocidos."""
    data = {
        'precio': [10.0, 20.0, 30.0],
        'cantidad': [2, 1, 3]
    }
    df = pd.DataFrame(data)
    
    resultado = calcular_metricas_ventas(df)
    
    # 10*2 (20) + 20*1 (20) + 30*3 (90) = 130.0
    assert resultado["total_ventas"] == 130.0
    assert resultado["registros"] == 3
    assert resultado["promedio_venta"] == 130.0 / 3

def test_calcular_metricas_ventas_vacio():
    """Test de Vacío: Evalúa cómo reacciona la función ante un DataFrame sin registros."""
    df_vacio = pd.DataFrame()
    
    resultado = calcular_metricas_ventas(df_vacio)
    
    assert resultado["total_ventas"] == 0.0
    assert resultado["promedio_venta"] == 0.0
    assert resultado["registros"] == 0
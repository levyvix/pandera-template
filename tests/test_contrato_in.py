import sys
import os
# Add the root directory of your project to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd

from src.contrato import MetricasFinanceiras

def test_contrato_correto():

    df_test = pd.DataFrame({
        "setor_da_empresa": ["VND_A1B2C3", "REP_X7Y8Z9", "MNT_4D5E6F"],
        "receita_operacional": [1000,1000,1000],
        "data": ["2023-01-01", "2023-01-01", "2023-01-01"],
        "percentual_de_imposto": [0.1, 0.1, 0.1],
        "custo_dos_bens": [200,200,200]
    })

    MetricasFinanceiras.validate(df_test)
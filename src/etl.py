import pandas as pd
import pandera as pa
from datetime import datetime

from contrato import MetricasFinanceirasBase, MetricasFinanceirasOut

@pa.check_output(MetricasFinanceirasBase)
def extrai_dados(dir_arquivo: str) -> pd.DataFrame:
    """Extrai os dados, transformando em um dataframe"""
    df = pd.read_csv(dir_arquivo)
    return df


@pa.check_output(MetricasFinanceirasOut)
def transforma_dados(df: pd.DataFrame) -> pd.DataFrame:
    """"Calcula o custo total, faturamento líquido e a margem operacional"""
    df_transformado = df.copy()
    df_transformado["valor_do_imposto"] = df_transformado["percentual_de_imposto"] * df_transformado["receita_operacional"]
    df_transformado["custo_total"] = df_transformado["valor_do_imposto"] + df_transformado["custo_dos_bens"]
    df_transformado["receita_liquida"] = df_transformado["receita_operacional"] - df_transformado["custo_total"]
    df_transformado["margem_operacional"] = (df_transformado["receita_liquida"] / df_transformado["receita_operacional"]) 
    df_transformado["transformado_em"] = datetime.now().strftime('%Y-%m-%d')
    return df_transformado

def carrega_dados(df: pd.DataFrame) -> None:
    """Carrega os dados no Banco de Dados"""
    pass

if __name__ == '__main__':
    dir_arquivo = 'data/dados_financeiros.csv'
    df = extrai_dados(dir_arquivo=dir_arquivo)
    df_transformado = transforma_dados(df)
    print(df_transformado)
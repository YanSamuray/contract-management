"""
utils.py

Funções utilitárias, como salvar DataFrame em CSV e configurações de logging.
"""

import logging
import pandas as pd
from pathlib import Path

# Configuração de logging simples
logging.basicConfig(
    format='[%(levelname)s] %(asctime)s - %(message)s',
    level=logging.INFO
)

def salvar_em_csv(df: pd.DataFrame, filepath: Path) -> None:
    """
    Salva o DataFrame em CSV (UTF-8, sem índice).
    :param df: DataFrame a ser salvo
    :param filepath: Caminho do arquivo de saída (Path ou string)
    """
    df.to_csv(filepath, index=False, encoding='utf-8')
    logging.info(f"DataFrame salvo em: {filepath}")

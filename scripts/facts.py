"""
facts.py

Funções para gerar DataFrames de fatos (Contratos, Pagamentos, Violações).
"""

import random
import pandas as pd
from typing import List
from config import fake

def gerar_fato_contratos(num_contratos: int,
                         clientes_ids: List[int],
                         fornecedores_ids: List[int],
                         tipos_contrato_ids: List[int]) -> pd.DataFrame:
    contratos = []
    for _ in range(num_contratos):
        data_inicio = fake.date_between(start_date='-2y', end_date='today')
        data_fim = fake.date_between(start_date='today', end_date='+2y')
        valor_total = round(random.uniform(10000.0, 500000.0), 2)
        saldo_contrato = round(valor_total * random.uniform(0.1, 1.0), 2)
        contratos.append({
            'ID_Contrato': fake.unique.random_int(min=10000, max=99999),
            'ID_Cliente': random.choice(clientes_ids) if clientes_ids else None,
            'ID_Fornecedor': random.choice(fornecedores_ids) if fornecedores_ids else None,
            'ID_Tipo_Contrato': random.choice(tipos_contrato_ids) if tipos_contrato_ids else None,
            'Data_Início': data_inicio,
            'Data_Término': data_fim,
            'Valor_Total': valor_total,
            'Status_Contrato': random.choice(['Ativo', 'Encerrado', 'Pendente']),
            'Saldo_Contrato': saldo_contrato
        })
    return pd.DataFrame(contratos)


def gerar_fato_pagamentos(num_pagamentos: int,
                          contratos_ids: List[int],
                          tipos_pagamento_ids: List[int]) -> pd.DataFrame:
    pagamentos = []
    for _ in range(num_pagamentos):
        data_pagamento = fake.date_between(start_date='-2y', end_date='today')
        valor_pagamento = round(random.uniform(1000.0, 50000.0), 2)
        pagamentos.append({
            'ID_Pagamento': fake.unique.random_int(min=50000, max=999999),
            'ID_Contrato': random.choice(contratos_ids) if contratos_ids else None,
            'Data_Pagamento': data_pagamento,
            'Valor_Pagamento': valor_pagamento,
            'Método_Pagamento': random.choice(['Online', 'Presencial']),
            'ID_Tipo_Pagamento': random.choice(tipos_pagamento_ids) if tipos_pagamento_ids else None
        })
    return pd.DataFrame(pagamentos)


def gerar_fato_violacoes(num_violacoes: int,
                         contratos_ids: List[int],
                         tipos_violacao_ids: List[int]) -> pd.DataFrame:
    violacoes = []
    for _ in range(num_violacoes):
        data_violacao = fake.date_between(start_date='-1y', end_date='today')
        violacoes.append({
            'ID_Violação': fake.unique.random_int(min=70000, max=999999),
            'ID_Contrato': random.choice(contratos_ids) if contratos_ids else None,
            'Data_Violação': data_violacao,
            'ID_Tipo_Violação': random.choice(tipos_violacao_ids) if tipos_violacao_ids else None,
            'Descrição_Violação': fake.sentence(nb_words=6),
            'Ação_Tomada': random.choice(['Sim', 'Não']),
            'Severidade': random.choice(['Baixa', 'Média', 'Alta'])
        })
    return pd.DataFrame(violacoes)

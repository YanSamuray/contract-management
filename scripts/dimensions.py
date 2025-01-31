"""
dimensions.py

Funções para gerar DataFrames de dimensões (clientes, fornecedores etc.).
"""

import random
import pandas as pd
from typing import List
from config import fake  # Reutiliza o Faker definido em config

def gerar_dim_clientes(num_clientes: int) -> pd.DataFrame:
    clientes = []
    for _ in range(num_clientes):
        cliente = {
            'ID_Cliente': fake.unique.random_int(min=1000, max=9999),
            'Nome_Cliente': fake.company(),
            'Segmento': random.choice(['Varejo', 'Tecnologia', 'Saúde', 'Financeiro', 'Educação']),
            'Localização': fake.city(),
            'Tamanho_Empresa': random.choice(['Pequena', 'Média', 'Grande'])
        }
        clientes.append(cliente)
    return pd.DataFrame(clientes)


def gerar_dim_fornecedores(num_fornecedores: int) -> pd.DataFrame:
    fornecedores = []
    for _ in range(num_fornecedores):
        fornecedor = {
            'ID_Fornecedor': fake.unique.random_int(min=5000, max=9999),
            'Nome_Fornecedor': fake.company(),
            'Categoria': random.choice(['Matérias-primas', 'Serviços', 'Equipamentos', 'Consultoria']),
            'Localização': fake.city(),
            'Avaliação': random.randint(1, 5)
        }
        fornecedores.append(fornecedor)
    return pd.DataFrame(fornecedores)


def gerar_dim_tipo_contrato() -> pd.DataFrame:
    tipos_contrato = [
        {'ID_Tipo_Contrato': 1, 'Descrição_Tipo': 'Fornecimento', 'Categoria_Tipo': 'Produtos'},
        {'ID_Tipo_Contrato': 2, 'Descrição_Tipo': 'Prestação de Serviços', 'Categoria_Tipo': 'Serviços'},
        {'ID_Tipo_Contrato': 3, 'Descrição_Tipo': 'Locação', 'Categoria_Tipo': 'Imóveis'},
        {'ID_Tipo_Contrato': 4, 'Descrição_Tipo': 'Parceria', 'Categoria_Tipo': 'Negócios'},
        {'ID_Tipo_Contrato': 5, 'Descrição_Tipo': 'Distribuição', 'Categoria_Tipo': 'Logística'}
    ]
    return pd.DataFrame(tipos_contrato)


def gerar_dim_tipo_pagamento() -> pd.DataFrame:
    tipos_pagamento = [
        {'ID_Tipo_Pagamento': 1, 'Descrição_Pagamento': 'Boleto Bancário'},
        {'ID_Tipo_Pagamento': 2, 'Descrição_Pagamento': 'Cartão de Crédito'},
        {'ID_Tipo_Pagamento': 3, 'Descrição_Pagamento': 'Transferência Bancária'},
        {'ID_Tipo_Pagamento': 4, 'Descrição_Pagamento': 'Depósito'},
        {'ID_Tipo_Pagamento': 5, 'Descrição_Pagamento': 'Pix'}
    ]
    return pd.DataFrame(tipos_pagamento)


def gerar_dim_tipo_violacao() -> pd.DataFrame:
    tipos_violacao = [
        {'ID_Tipo_Violação': 1, 'Descrição_Violação': 'Atraso na Entrega', 'Categoria_Violação': 'Operacional'},
        {'ID_Tipo_Violação': 2, 'Descrição_Violação': 'Não Conformidade', 'Categoria_Violação': 'Qualidade'},
        {'ID_Tipo_Violação': 3, 'Descrição_Violação': 'Inadimplência', 'Categoria_Violação': 'Financeiro'},
        {'ID_Tipo_Violação': 4, 'Descrição_Violação': 'Quebra de Exclusividade', 'Categoria_Violação': 'Legal'},
        {'ID_Tipo_Violação': 5, 'Descrição_Violação': 'Uso Indevido de Marca', 'Categoria_Violação': 'Marketing'}
    ]
    return pd.DataFrame(tipos_violacao)


def gerar_dim_profissionais(num_profissionais: int, contratos_ids: List[int]) -> pd.DataFrame:
    profissionais = []
    for _ in range(num_profissionais):
        profissional = {
            'ID_Profissional': fake.unique.random_int(min=2000, max=9999),
            'Nome_Profissional': fake.name(),
            'Categoria_Profissional': random.choice(['Gerente de Projetos', 'Advogado', 'Analista de Contratos', 'Financeiro']),
            'Departamento': random.choice(['Jurídico', 'Financeiro', 'Operações', 'Vendas']),
            'ID_Contrato': random.choice(contratos_ids) if contratos_ids else None
        }
        profissionais.append(profissional)
    return pd.DataFrame(profissionais)


def gerar_dim_tempo(data_inicio, data_fim) -> pd.DataFrame:
    datas = pd.date_range(start=data_inicio, end=data_fim)
    df_tempo = pd.DataFrame({
        'Data': datas,
        'Dia': datas.day,
        'Mês': datas.month,
        'Ano': datas.year,
        'Trimestre': datas.quarter,
        'Dia_Semana': datas.day_name(locale='pt_BR')  # depende de locale pt_BR
    })
    return df_tempo

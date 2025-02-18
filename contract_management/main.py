"""
main.py

Script principal que orquestra a geração e salvamento de dados (dimensões e fatos).
"""

import logging
from config import (
    NUM_CLIENTES, NUM_FORNECEDORES, NUM_CONTRATOS, NUM_PAGAMENTOS,
    NUM_VIOLACOES, NUM_PROFISSIONAIS,
    ARQ_DIM_CLIENTES, ARQ_DIM_FORNECEDORES, ARQ_DIM_TIPO_CONTRATO,
    ARQ_DIM_TIPO_PAGAMENTO, ARQ_DIM_TIPO_VIOLACAO, ARQ_DIM_PROFISSIONAIS,
    ARQ_DIM_TEMPO, ARQ_FATO_CONTRATOS, ARQ_FATO_PAGAMENTOS,
    ARQ_FATO_VIOLACOES
)
from dimensions import (
    gerar_dim_clientes, gerar_dim_fornecedores, gerar_dim_tipo_contrato,
    gerar_dim_tipo_pagamento, gerar_dim_tipo_violacao,
    gerar_dim_profissionais, gerar_dim_tempo
)
from facts import (
    gerar_fato_contratos, gerar_fato_pagamentos, gerar_fato_violacoes
)
from utils import salvar_em_csv

def gerar_todas_bases() -> None:
    """
    Gera todas as bases de dados (dimensões e fatos) e salva em CSV.
    """
    logging.info("=== Iniciando geração de todas as bases ===")

    # 1) Gerar e salvar dimensões "básicas"
    df_clientes = gerar_dim_clientes(NUM_CLIENTES)
    salvar_em_csv(df_clientes, ARQ_DIM_CLIENTES)

    df_fornecedores = gerar_dim_fornecedores(NUM_FORNECEDORES)
    salvar_em_csv(df_fornecedores, ARQ_DIM_FORNECEDORES)

    df_tipo_contrato = gerar_dim_tipo_contrato()
    salvar_em_csv(df_tipo_contrato, ARQ_DIM_TIPO_CONTRATO)

    df_tipo_pagamento = gerar_dim_tipo_pagamento()
    salvar_em_csv(df_tipo_pagamento, ARQ_DIM_TIPO_PAGAMENTO)

    df_tipo_violacao = gerar_dim_tipo_violacao()
    salvar_em_csv(df_tipo_violacao, ARQ_DIM_TIPO_VIOLACAO)

    # 2) Gerar e salvar Fato_Contratos
    df_contratos = gerar_fato_contratos(
        NUM_CONTRATOS,
        df_clientes['ID_Cliente'].tolist(),
        df_fornecedores['ID_Fornecedor'].tolist(),
        df_tipo_contrato['ID_Tipo_Contrato'].tolist()
    )
    salvar_em_csv(df_contratos, ARQ_FATO_CONTRATOS)

    # 3) Gerar e salvar Fato_Pagamentos
    df_pagamentos = gerar_fato_pagamentos(
        NUM_PAGAMENTOS,
        df_contratos['ID_Contrato'].tolist(),
        df_tipo_pagamento['ID_Tipo_Pagamento'].tolist()
    )
    salvar_em_csv(df_pagamentos, ARQ_FATO_PAGAMENTOS)

    # 4) Gerar e salvar Fato_Violacoes
    df_violacoes = gerar_fato_violacoes(
        NUM_VIOLACOES,
        df_contratos['ID_Contrato'].tolist(),
        df_tipo_violacao['ID_Tipo_Violação'].tolist()
    )
    salvar_em_csv(df_violacoes, ARQ_FATO_VIOLACOES)

    # 5) Gerar e salvar Dim_Profissionais
    df_profissionais = gerar_dim_profissionais(
        NUM_PROFISSIONAIS,
        df_contratos['ID_Contrato'].tolist()
    )
    salvar_em_csv(df_profissionais, ARQ_DIM_PROFISSIONAIS)

    # 6) Gerar e salvar Dim_Tempo (baseada nas datas dos fatos)
    data_min = min(
        df_contratos['Data_Início'].min(),
        df_pagamentos['Data_Pagamento'].min(),
        df_violacoes['Data_Violação'].min()
    )
    data_max = max(
        df_contratos['Data_Término'].max(),
        df_pagamentos['Data_Pagamento'].max(),
        df_violacoes['Data_Violação'].max()
    )
    df_tempo = gerar_dim_tempo(data_min, data_max)
    salvar_em_csv(df_tempo, ARQ_DIM_TEMPO)

    logging.info("=== Todas as bases foram geradas com sucesso! ===")


if __name__ == "__main__":
    gerar_todas_bases()

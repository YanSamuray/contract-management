"""
config.py

Configurações gerais do projeto:
- Seeds (para reprodutibilidade)
- Parâmetros de geração (quantidades)
- Definição de caminhos (usando pathlib)
"""

import random
from faker import Faker
from pathlib import Path

# =============================================================================
# SEMENTES
# =============================================================================
random.seed(0)
fake = Faker('pt_BR')
Faker.seed(0)

# =============================================================================
# PARÂMETROS DE GERAÇÃO
# =============================================================================
NUM_CLIENTES = 10000
NUM_FORNECEDORES = 1500
NUM_CONTRATOS = 1000
NUM_PAGAMENTOS = 50000
NUM_VIOLACOES = 3000
NUM_PROFISSIONAIS = 1500

# =============================================================================
# CAMINHOS (PATHS)
# =============================================================================
# Partimos do próprio local deste arquivo (scripts/) e subimos um nível para chegar em raiz
BASE_DIR = Path(__file__).resolve().parent.parent

# Pasta onde salvaremos os CSVs: raiz/data/raw
DATA_RAW_DIR = BASE_DIR / "data" / "raw"

# Se quiser nomes fixos de arquivo para cada tabela, define aqui:
ARQ_DIM_CLIENTES = DATA_RAW_DIR / "Dim_Clientes.csv"
ARQ_DIM_FORNECEDORES = DATA_RAW_DIR / "Dim_Fornecedores.csv"
ARQ_DIM_TIPO_CONTRATO = DATA_RAW_DIR / "Dim_Tipo_Contrato.csv"
ARQ_DIM_TIPO_PAGAMENTO = DATA_RAW_DIR / "Dim_Tipo_Pagamento.csv"
ARQ_DIM_TIPO_VIOLACAO = DATA_RAW_DIR / "Dim_Tipo_Violacao.csv"
ARQ_DIM_PROFISSIONAIS = DATA_RAW_DIR / "Dim_Profissionais.csv"
ARQ_DIM_TEMPO = DATA_RAW_DIR / "Dim_Tempo.csv"
ARQ_FATO_CONTRATOS = DATA_RAW_DIR / "Fato_Contratos.csv"
ARQ_FATO_PAGAMENTOS = DATA_RAW_DIR / "Fato_Pagamentos.csv"
ARQ_FATO_VIOLACOES = DATA_RAW_DIR / "Fato_Violacoes.csv"

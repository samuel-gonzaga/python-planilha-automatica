from drive_utils import baixar_arquivo_drive, enviar_para_drive
from chamada import processar_chamada
import os

# IDs do Google Drive
ID_MASTER = '12T8udyYFmfBWgWViTdOfMey9J8oDJcMC'
ID_TEMPLATE = '1p8-va-vmrq8od3mYigKlMPRJNPFnRdNj'
ID_PASTA_UPLOAD = '16XakderrRBPhGelfTmGyoBZJhCju_zHg'

# Nomes dos arquivos locais
ARQUIVO_MASTER = 'master.xlsx'
ARQUIVO_TEMPLATE = 'lista_chamada.xlsx'
ARQUIVO_SAIDA = 'lista_chamada_atualizada.xlsx'

# Baixar arquivos necessários
baixar_arquivo_drive(ID_MASTER, ARQUIVO_MASTER)
baixar_arquivo_drive(ID_TEMPLATE, ARQUIVO_TEMPLATE)

# Processar planilhas
processar_chamada(ARQUIVO_MASTER, ARQUIVO_TEMPLATE, ARQUIVO_SAIDA)

# Enviar resultado para o Google Drive
enviar_para_drive(ARQUIVO_SAIDA, ID_PASTA_UPLOAD)

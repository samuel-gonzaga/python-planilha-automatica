from drive_utils import baixar_arquivo_drive, enviar_para_drive, deletar_arquivo_local
from chamada import processar_chamada
import os

# IDs do Google Drive
ID_MASTER = '1rsduFSjliaSennFSuYm4KJ8N8h5fW3nh'
ID_TEMPLATE = '1Acw48Bd2jk-tYOSFqTxExJFcdM7lq3Gm'
ID_PASTA_UPLOAD = '1Y7eoLU2c9TsEDsD9tT8dhBL4rHTh7-mK'

# Nomes dos arquivos locais
ARQUIVO_MASTER = 'master.xlsx'
ARQUIVO_TEMPLATE = 'lista_chamada.xlsx'
ARQUIVO_SAIDA = 'lista_chamada_maio.xlsx'

# Baixar arquivos necessários
baixar_arquivo_drive(ID_MASTER, ARQUIVO_MASTER)
baixar_arquivo_drive(ID_TEMPLATE, ARQUIVO_TEMPLATE)

# Processar planilhas
processar_chamada(ARQUIVO_MASTER, ARQUIVO_TEMPLATE, ARQUIVO_SAIDA)

# Enviar resultado para o Google Drive
enviar_para_drive(ARQUIVO_SAIDA, ID_PASTA_UPLOAD)

# Deleta os arquivos que ficaram após o procedimento
deletar_arquivo_local(ARQUIVO_MASTER)
deletar_arquivo_local(ARQUIVO_TEMPLATE)
deletar_arquivo_local(ARQUIVO_SAIDA)

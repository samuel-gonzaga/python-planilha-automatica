from drive_utils import (
    baixar_arquivo_drive,
    enviar_para_drive,
    deletar_arquivo_local,
    buscar_id_por_nome
)
from chamada import processar_chamada
import shutil

# Nomes dos arquivos locais
ARQUIVO_MASTER = 'master.xlsx'
ARQUIVO_TEMPLATE = 'lista_chamada.xlsx'
ARQUIVO_SAIDA = 'lista_chamada_maio.xlsx'

# IDs do Google Drive
ID_MASTER = buscar_id_por_nome(ARQUIVO_MASTER)
ID_TEMPLATE = buscar_id_por_nome(ARQUIVO_TEMPLATE)
ID_ARQUIVO_EXISTENTE = buscar_id_por_nome(ARQUIVO_SAIDA)
ID_PASTA_UPLOAD = '1Y7eoLU2c9TsEDsD9tT8dhBL4rHTh7-mK'

# Baixar arquivos necessários
baixar_arquivo_drive(ID_MASTER, ARQUIVO_MASTER)
baixar_arquivo_drive(ID_TEMPLATE, ARQUIVO_TEMPLATE)

shutil.copy(ARQUIVO_TEMPLATE, ARQUIVO_SAIDA)

# Processar planilhas
processar_chamada(ARQUIVO_MASTER, ARQUIVO_SAIDA, ARQUIVO_SAIDA)

# Enviar resultado para o Google Drive
enviar_para_drive(ARQUIVO_SAIDA, ID_PASTA_UPLOAD, ID_ARQUIVO_EXISTENTE)

# Deleta os arquivos que ficaram após o procedimento
deletar_arquivo_local(ARQUIVO_MASTER)
deletar_arquivo_local(ARQUIVO_TEMPLATE)
deletar_arquivo_local(ARQUIVO_SAIDA)

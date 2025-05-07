from openpyxl import load_workbook
from openpyxl.cell.cell import MergedCell

def extrair_nomes(sheet, col, linha_ini, linha_fim):
    return [
        sheet.cell(row=i, column=col).value
        for i in range(linha_ini, linha_fim)
        if sheet.cell(row=i, column=col).value
    ]

def colar_nomes(sheet, nomes, col, linha_ini):
    for i, nome in enumerate(nomes, start=linha_ini):
        cell = sheet.cell(row=i, column=col)
        if not isinstance(cell, MergedCell):
            cell.value = nome

# 1. Abrir arquivos
wb_master = load_workbook('master.xlsx')
wb_template = load_workbook('lista_chamada.xlsx')

# 2. Selecionar planilhas
planilhas = {
    "08-10": wb_master['Pannunzio - Sab 8h-10h'],
    "10-12": wb_master['Pannunzio - Sab 10h-12h'],
    "12-14": wb_master['Pannunzio - Sab 12h30-14h30'],
    "14-16": wb_master['Pannunzio - Sab 14h30-16h30'],
}

# 3. Mapeamento de salas com suas posições
mapeamento = [
    # (hora, sala, linha_inicio, linha_fim, linha_destino)
    ("08-10", "6", 5, 50, 5),
    ("08-10", "7", 55, 105, 66),
    ("10-12", "6", 5, 50, 129),
    ("10-12", "7", 55, 105, 188),
    ("12-14", "6", 5, 50, 248),
    ("12-14", "7", 55, 105, 290),
    ("14-16", "6", 5, 50, 336),
    ("14-16", "7", 55, 105, 394),
]

sheet_output = wb_template['Table 1']

# 4. Executar extração e colagem
for hora, sala, ini, fim, destino in mapeamento:
    planilha = planilhas[hora]
    nomes = extrair_nomes(planilha, col=1, linha_ini=ini, linha_fim=fim)
    colar_nomes(sheet_output, nomes, col=8, linha_ini=destino)

# 5. Salvar resultado
wb_template.save('lista_chamada_atualizada.xlsx')

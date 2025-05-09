# 📝 Automatizador de Chamada para Escolas

Este projeto nasceu de um problema real enfrentado durante o gerenciamento de chamadas em uma escola de cursos profissionalizantes. A rotina era marcada por retrabalho, confusão e lentidão no processo de marcação de presenças. Esta ferramenta automatiza e organiza esse processo, poupando tempo e reduzindo erros.

## 🚨 O Problema

A rotina de chamada seguia este fluxo:

1. 📄 A chamada era feita **manualmente em papel**.
2. ⌨️ Depois, as informações eram passadas **manualmente para uma planilha digital**.
3. 🔁 O retrabalho e a falta de atualização entre as listas causavam:
   - Nomes em horários errados.
   - Alunos antigos ainda aparecendo na lista.
   - Atrasos e desorganização.

## ✅ A Solução

Esta aplicação:

- 🔄 **Sincroniza** a lista de chamada com uma planilha principal (master).
- 📥 **Baixa a planilha do Google Drive** com todos os alunos.
- 📤 **Gera uma nova lista de chamada organizada por horário e turma.**
- 🧹 Evita erros e duplicidades, **mantendo os dados organizados e atualizados**.
- ⏱️ Pode ser executada automaticamente (via `cron`) ou manualmente.

> Esta versão pública usa dados fictícios e randomizados, preservando a privacidade dos alunos reais.

## 💼 Tecnologias utilizadas

- Python
- API do Google Drive
- `google-auth` e `google-api-python-client`
- Agendamento com `cron`
- Hospedagem em nuvem (Railway)

## 🔧 Como funciona

1. A ferramenta acessa uma planilha no Google Drive.
2. Processa os dados para organizar a lista de chamada por horário e turma.
3. Gera uma nova planilha pronta para impressão ou uso digital.
4. Envia a lista atualizada de volta ao Google Drive.

## 📸 Demonstração

Em breve, será adicionado aqui um vídeo mostrando o **antes e depois** da ferramenta em ação.

---

## ⚙️ Configuração (versão pública)

Em breve informações de configuração e execução da ferramenta.

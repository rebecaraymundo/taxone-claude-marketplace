---
source: "MTZ_Tela_Agrupamento_Relatorio.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS

Agrupamento Relatório
Report Fiscal >> Relatórios >> Lucro Presumido



DOCUMENTO DE REQUISITO


Sumário

**1.	OBJETIVO	3**
2.	TELA	3
3.	Regras dos Campos	4

# OBJETIVO

Criar uma tela de agrupamentos para o relatório de Apuração do Lucro Presumido IR/CSLL/PIS/COFINS."

# TELA








# Regras dos Campos

Localização da tela: Módulo: Básicos>> Report Fiscal
Menu: Relatórios >> Lucro Presumido >> Agrupamento Relatório

Título da tela: Agrupamento Relatório

**Opções da barra de menu:**

NOVO – Cria uma nova linha, permitindo a inclusão de um novo registro.

EXCLUI – Permite a exclusão do registro selecionado.

CONFIRMA – Salva os dados incluídos ou alterados.

RELATÓRIO – Para emitir o relatório das parametrizações criadas.

FECHA – Fecha a janela da parametrização.



---

| MFS | Nome | Descrição |
| --- | --- | --- |
| MFS-865787 | Alessandra Cristina Navatta | Criação do Documento |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS |
| --- | --- | --- | --- | --- | --- | --- |
| Empresa | Lista | S | S | Cód – Razão Social | Exibe a empresa que está logada | MFS-865787 |
| Agrupamento | Lista | S | N | Default: Lucro Presumido com Sinergia PIS COFINS | Lista de valores válidos:  Lucro Presumido com Sinergia PIS COFINS | MFS-865787 |
| Cód. Agrupador | Texto | S | S |  | Informar o cód. Agrupador  Campo alfanumérico | MFS-865787 |
| Num. Ordem | Texto | S | S |  | Campo numérico | MFS-865787 |
| Descrição | Texto | N | S |  | Campo alfanumérico | MFS-865787 |
| Comportamento | Lista | S | S |  | Lista de Valores Válidos:  Totalizador Recuperação de Contas | MFS-865787 |
| Base Cálculo IR | Lista | S | S |  | Lista de Valores Válidos:  Base de Cálculo Imposto de Renda - 8% Base de Cálculo Imposto de Renda - 20% Receitas Financeiras Demais Receitas Tributáveis | MFS-865787 |
| Base Cálculo PIS/COFINS | Lista | S | S |  | Lista de Valores Válidos: Pis/Cofins Cumulativo Pis/Cofins Não-Cumulativo | MFS-865787 |
| Replicar para as Empresas | Checkbox | N | S | Default: Não selecionado | Quando selecionado deverá permitir replicar a parametrização para outras empresas | MFS-865787 |
| Confirma | Botão |  |  |  | Campos obrigatórios não preenchidos:  Quando o campo Comportamento, não for preenchido, exibir a mensagem: “Informe o campo Comportamento”  Quando o campo Cód. Agrupamento, não for preenchido, exibir a mensagem: “Informe o Cód. Agrupamento”  Quando o campo Núm. Ordem, não for preenchido, exibir a mensagem: “Informe o campo Núm. Ordem”  Quando o campo Base de Cálculo IR, não for preenchido, exibir a mensagem: “Informe a Base de Cálculo IR”  Quando o campo Base de Cálculo PISCOFINS, não for preenchido, exibir a mensagem: “Informe a Base de Cálculo PISCOFINS” | MFS-865787 |

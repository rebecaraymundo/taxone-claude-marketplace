---
source: "MTZ_Tela_Recuperacao_de_Contas.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS

Recuperação de Contas
Report Fiscal >> Relatórios >> Lucro Presumido



DOCUMENTO DE REQUISITO


Sumário

**1 - OBJETIVO	3**
2 - TELA	3
3 - Regras dos Campos	4

# 1 - OBJETIVO

Criar uma tela, para identificar quais contas devem ser incluídas e os métodos de recuperação de valores correspondentes, organizados por agrupamento (definido na tela de Agrupamento de Relatório), a serem considerados na elaboração do relatório de Apuração do Lucro Presumido IR/CSLL/PIS/COFINS."

# 2 - TELA




# 3 - Regras dos Campos

Localização da tela: Módulo: Básicos>> Report Fiscal
Menu: Relatórios >> Lucro Presumido >> Recuperação de Contas

Título da tela: Recuperação de Contas

**Opções da barra de menu:**

NOVO – Cria uma nova linha, permitindo a inclusão de um novo registro de conta.

EXCLUI – Permite a exclusão do registro selecionado.

CONFIRMA – Salva os dados incluídos ou alterados.

RELATÓRIO – Para emitir o relatório das contas que serão recuperadas.

FECHA – Fecha a janela da parametrização.

Na abertura da tela, apresentar os campos citados abaixo:





---

| MFS | Nome | Descrição |
| --- | --- | --- |
| MFS-865787 | Alessandra Cristina Navatta | Criação do Documento |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS |
| --- | --- | --- | --- | --- | --- | --- |
| Empresa | Lista | S | S | Cód – Razão Social | Exibe a empresa que está logada | MFS-865787 |
| Grupo | Pasta | S | S | Cód - Decrição | Apresentar o código e a descrição dos grupos vinculados a empresa selecionada. | MFS-865787 |
| Conta Contábil | Lista | S | S | Código | Permite selecionar as contas contábeis (SAFX2002), de acordo com o grupo selecionado. | MFS-865787 |
| Descrição Conta Contábil | Texto | S | N |  | Exibe a descrição da conta que foi selecionada pelo usuário. Campo não editável | MFS-865787 |
| Natureza | Texto | S | N |  | Exibe a descrição da natureza da conta selecionada no campo Conta Contábil (campo IND_NATUREZA da SAFX2002)  Campo não editável. | MFS-865787 |
| Agrupamento | Lista | S | S |  | Permite selecionar as informações de agrupamento, cadastrados na tela de Agrupamento Relatório, cujo Comportamento = Recuperação de Contas | MFS-865787 |
| Recuperação de Valores | Lista | S | S |  | Lista de Valores Válidos: Crédito Débito Movimento Saldo Final | MFS-865787 |
| Exceção BC | Lista | S | S |  | Lista de Valores Válidos:  Sim Não | MFS-865787 |
| Replicar para as Empresas | Checkbox | N | S | Default: Não selecionado | Quando selecionado deverá permitir replicar a parametrização para outras empresas, desde que as empresas estejam no mesmo grupo. | MFS-865787 |
| Confirma | Botão |  |  |  | Campos obrigatórios não preenchidos:  Quando o campo Grupo não for preenchido, exibir a mensagem: “Informe o Grupo” Quando o campo Conta Contábil, não for preenchido, exibir a mensagem: “Informe a Conta Contábil”  Quando o campo Agrupamento, não for preenchido, exibir a mensagem: “Informe o Agrupamento”  Quando o campo Recuperação de Valores, não for preenchido, exibir a mensagem: “Informe o campo Recuperação de Valores”  Quando o campo Exceção BC, não for preenchido, exibir a mensagem: “Informe o campo Exceção BC” | MFS-865787 |

# MTZ-DW-Manutencao_SAFX03

- **Fonte:** MTZ-DW-Manutencao_SAFX03.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 30 KB

---

        

# <a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>Módulo DW – Manutenção – Contas a Pagar /Aba Título

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS4579

Alteração de Campo

Alteração no tamanho do campo Número de Lançamento

20/02/2015

MFS\-12777

Inclusão de Campos

Inclusão de campos para atendimento ao SPED\- REINF

22/08/2017

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN01__

__Campo  Número do lançamento__

Deverá ser alterado para suporta até 40 caracteres\.

__OS4579__

__RN02__

__Campo Valor Retenção __

Não Obrigatório / Numérico / Default: Não Selecionado / Text Box

__MFS\-12777__

__RN03__

__Campo Valor Retenção não Efetuada__

Não Obrigatório / Numérico / Default: Não Selecionado / Text Box

__MFS\-12777__

__RN04__

__Campo Tipo do Processo__

Deverá ser criado o campo “Tipo do Processo Retenção”

Não Obrigatório / Alfanumérico / Default: Não Selecionado / DropDown

Deverá listar as seguintes opções:

1. Administrativo
2. Judicial 

__MFS\-12777__

__RN05__

__Campo Número do Processo__

Não Obrigatório / Alfanumérico / Pasta

Deverão ser listados os processos conforme cadastro de processos na tela: \(MastersafDW >> Menu Manutenção >> Códigos >> Cadastro de Processo Admin/Judicial \(REINF\) aba Informações do Processo\) e filtro por tipo de processo\. 

__MFS\-12777__

__RN06__

__Campo Código Suspensão__

Não Obrigatório / Alfanumérico / Pasta

Deverão ser listados os códigos conforme cadastro de suspensão na tela: \(MastersafDW >> Menu Manutenção >> Códigos >> Cadastro de Processo Admin/Judicial \(REINF\) aba Informações de Suspensão de Exigibilidade de Tributos\) e filtro por número de processo e tipo de processo\. Caso houver apenas um código cadastrado este deverá ser apresentado automaticamente e o campo bloqueado\.

__MFS\-12777__


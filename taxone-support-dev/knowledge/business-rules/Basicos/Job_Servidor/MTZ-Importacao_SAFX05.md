# MTZ-Importacao_SAFX05

- **Fonte:** MTZ-Importacao_SAFX05.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 31 KB

---

# JOB SERVIDOR – IMPORTAÇÃO SAFX05 \(Arquivo de Contas a Pagar\)

__Módulo__: Básicos 🡪 Job Servidor

__Menu1__: Importação 🡪 Programação / Execução

__Menu2__: Importação batch 🡪 Programação / Execução

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS4316

Criação de Campos

Criação dos campos Código e Descrição da SCP

OS4579

Elenilson Coutinho

Alteração no tamanho do campo NUM\_LANCAMENTO

OS3814

Criação do Módulo DMED

Criação do Módulo DMED \(Declaração de Serviços Médicos e de Saúde\)

\(ver __RN03__ e __RN04__\)

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

__Campo Código da SCP__

Alterar a rotina de importação e importação batch para que seja considerado o novo campo:

Tabela: SAFX05

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

Deverá existir um cadastro correspondente na SAFX2057 para o código informado\. Caso não exista, retornar a mensagem: “Cadastro da SCP não encontrado”\.

__OS4316__

__RN02__

__Campo NUM\_LANCAMENTO__

Alterar a rotina de importação e importação batch para que seja considerado o novo campo:

Tabela: SAFX05

Item: 27

Nome do Campo: Número do Lançamento

Tipo: A

Tamanho: 040

Obrigatório: Não

Chave: Não

Comentário: Informar o número ou código do lançamento contábil, correspondente ao cadastramento inicial do título\. Atende o Ato Cotepe nr 70/05 \- Registro Z030\.

__OS4579__

__RN03__

__Campo Indicador do Beneficiário \(DMED\)                   __*\(campo incluído na OS3814\)*

Tipo: A

Tamanho: 001

Obrigatório: Não

Se preenchido, deve conter uma das opções referentes ao campo “Indicador da Pessoa Física/Jurídica” da SAFX04\. Caso contrário, será gravada a seguinte mensagem de erro no log, e o registro não será importado:

          *“Indicador do Beneficiário inválido\. Preencher de acordo com o indicador de pessoa a fis/jur da SAFX04”*

__OS3814__

__RN04__

__Campo Código do Beneficiário \(DMED\)                   __*\(campo incluído na OS3814\)*

Tipo: A

Tamanho: 014

Obrigatório: Não

Se preenchido, serão feitas as seguintes validações da pessoa informada na tabela de pessoas físicas/jurídicas \(SAFX04\):

Crítica 1 🡪 Caso não exista o indicador / código informado, será gravada a seguinte mensagem de erro no log, e o registro                   não será importado:

*                        “Beneficiário inválido\. Informar uma pessoa fis/jur existente na tabela SAFX04”*

Crítica 2 🡪 Caso a pessoa exista, mas seja a mesma pessoa fis/jur do movimento \(campos 04 e 05\), será gravada a seguinte mensagem de erro no log, e o registro não será importado:

*             “Quando o beneficiário é a própria pessoa fis/jur do movimento, o campo Beneficiário não deve ser preenchido” *

Crítica 3 🡪 A pessoa informada deve ser uma pessoa física, ou seja, o conteúdo do campo 06\-CPF\_CGC deve ter apenas 11 caracteres preenchidos __ou__ nulo \(o que acontece quando o indicador do campo 04 é = 4, indicando uma pessoa “Especial”\)\. Caso esta condição não ocorra, será gravada a seguinte mensagem de erro no log, e o registro não será importado:

*                                                  “O beneficiário deve ser uma pessoa física” *

__OS3814__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


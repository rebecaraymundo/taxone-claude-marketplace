# MTZ-DW-Manutencao_SAFX317

- **Fonte:** MTZ-DW-Manutencao_SAFX317.docx
- **Modificado:** 2021-10-22
- **Tamanho:** 76 KB

---

THOMSON REUTERS

Módulo DW

Tabela Operações com Instrumentos de Pagamentos Eletrônicos \(SAFX317\)

__Localização__: Menu Básicos, módulo DW, menu Manutenção 🡪 Operações com Instrumentos de Pagamentos Eletrônicos

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS73697

Criação da SAFX317 

Criação da SAFX317 para a importação das operações realizadas por meio de instrumentos de pagamentos eletrônicos, a serem utilizadas na geração do Sped Fiscal, registro 1601 \(versão 1\.15, Jan/2022\)\. 

22/10/2021

Sumário

[1\.	Regras Gerais	2](#_Toc451260495)

[2\.	Layout da Tela	2](#_Toc451260496)

[3\.	Regras de Funcionamento dos Campos	3](#_Toc451260497)

# <a id="_Toc451260495"></a>Regras Gerais

Tabela SAFX317 \- Operações com Instrumentos de Pagamentos Eletrônicos:

Estrutura da tabela:

__Descrição__

__CAMPO__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Empresa

COD\_EMPRESA

A

003

SIM

SIM

Estabelecimento

COD\_ESTAB

A

006

SIM

SIM

Data de Movimento

DATA\_MOVTO

N

008

SIM

SIM

Indicador Pessoa Física/Jurídica da Instituição Financeira e de pagamento

IND\_FIS\_JUR

A

001

SIM

SIM

Código da Pessoa Física/Jurídica da Instituição Financeira e de pagamento

COD\_FIS\_JUR

A

014

SIM

SIM

Indicador Pessoa Física/Jurídica Intermediador da Transação

IND\_FIS\_JUR\_IT

A

001

__NÃO__

__SIM__

Código da Pessoa Física/Jurídica Intermediador da Transação

COD\_FIS\_JUR\_IT

A

014

__NÃO__

__SIM__

Total das Operações com ICMS

VLR\_TOT\_OP\_ICMS

N

015V002

NÃO

NÃO

Total das Operações com ISS

VLR\_TOT\_OP\_ISS

N

015V002

NÃO

NÃO

Total de Outras Operações

VLR\_TOT\_OP\_OUTR

N

015V002

NÃO

NÃO

# <a id="_Toc451260496"></a>Layout da Tela

__Título: Operações com Instrumentos de Pagamentos Eletrônicos__

Estabelecimento: \[\\/\] \[codigo – razão social\]

Data de Movimento: \[ dd/mm/aaaa \]

Pessoa Fis/Jur Instituição Financeira e de Pagamento: \[grupo\] \[pastinha\] \[indicador\] \[código \] \[ descrição                                 \]

Pessoa Fis/Jur Intermediador da Transação:                 \[grupo\] \[pastinha\] \[indicador\] \[código \] \[ descrição                                 \]

Vlr Total das Operações com ICMS:  \[          	,00\]

Vlr Total das Operações com ISS:      \[          	,00\]

Vlr Total de Outras Operações:          \[           	,00\]

__Botões da barra de menu__:

NOVO

Ao clicar nesta opção, as informações dos campos serão limpas e o usuário poderá incluir um novo registro\.

ABRE

Ao clicar nesta opção, será aberta a janela para seleção dos registros já cadastrados para consulta ou manutenção\. 	

EXCLUI

Esta opção permite a exclusão do registro\. 

CONFIRMA

Opção para salvar as informações do registro incluído ou alterado\.

RELATÓRIO

Esta opção permite imprimir os dados da tabela\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Toc451260497"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Estabelecimento

Alfanumérico 

__S__

S

Listbox

Neste campo será exibida a lista dos estabelecimentos da empresa para seleção do usuário\. 

Caso tenha sido informado um estabelecimento no login, este campo exibirá fixo o estabelecimento informado, e o usuário não poderá alterá\-lo\.

Caso ao salvar o registro, caso o campo não esteja preenchido, exibir a mensagem de erro:

*O código do estabelecimento deve ser preenchido\.*

Data de Movimento

Data

__S__

S

  \(DD/MM/AAAA\)

Neste campo deve ser informado uma data válida\.

Caso ao salvar o registro, o campo não esteja preenchido, exibir a mensagem de erro:

*“O campo Data de Movimento é de preenchimento obrigatório e não foi informado”*

\.

Pessoa Fis/Jur Instituição Financeira e de Pagamento

Alfanumérico

__S__

S

Pastinha \+ grupo \+ indicador \+ código \+ descrição

Este campo trabalha com janela de seleção da Tabela de Cadastro da Pessoa Fis/Jur \(SAFX04\)\.

Serão disponibilizadas para seleção apenas as linhas da SAFX04 do Grupo \(Relacionamento Tabela x Grupo\) a ser utilizado, e cuja data de validade seja <= a Data de Movimento informada\.

O* *__*Grupo*__* a ser utilizado será obtido a partir da regra básica, considerando o Grupo de maior data de validade <= a Data de Movimento informada, e para o qual a tabela SAFX04 esteja associada\.*

Se o código da pessoa fis/jur for digitado, deve atender às mesmas regras descritas para data de validade\. Caso contrário, a operação não será salva e será exibida mensagem de erro: 

     *“O Código da Pessoa Fisica/Juridica da Instituição Financeira e de Pagamento não está cadastrado”\.*

Caso ao salvar o registro, o campo não esteja preenchido, exibir a mensagem de erro:

*“O Código da Pessoa Fisica/Juridica da Instituição Financeira e de Pagamento é de preenchimento obrigatório e não foi informado”*

Pessoa Fis/Jur Intermediador da Transação

Alfanumérico

__N__

S

Pastinha \+ grupo \+ indicador \+ código \+ descrição

Este campo trabalha com janela de seleção da Tabela de Cadastro da Pessoa Fis/Jur \(SAFX04\)\.

Serão disponibilizadas para seleção apenas as linhas da SAFX04 do Grupo \(Relacionamento Tabela x Grupo\) a ser utilizado, e cuja data de validade seja <= a Data de Movimento informada\.

O* *__*Grupo*__* a ser utilizado será obtido a partir da regra básica, considerando o Grupo de maior data de validade <= a Data de Movimento informada, e para o qual a tabela SAFX04 esteja associada\.*

Se o código da pessoa fis/jur for digitado, deve atender às mesmas regras descritas para data de validade\. Caso contrário, a operação não será salva e será exibida mensagem de erro: 

     *“O Código da Pessoa Fisica/Juridica da Intermediador da Transação não está cadastrado”\.*

Vlr Total das Operações com ICMS

Numérico

__N__

S

Neste campo deve ser informado um valor válido\. 

Vlr Total das Operações com ISS

Numérico

__N__

S

Neste campo deve ser informado um valor válido\. 

Vlr Total de Outras Operações

Numérico

__N__

S

Neste campo deve ser informado um valor válido\. 

       = = = = = =


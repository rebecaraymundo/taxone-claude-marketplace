# MTZ_JOB_SERVIDOR_Importacao_SAFX534

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_SAFX534.docx
- **Modificado:** 2025-05-14
- **Tamanho:** 67 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__*MFS*__

__Nome__

__Descrição__

MFS\-79885

Alessandra Cristina Navatta

Definição das regras de Carga, importação \(Online e Batch\) e Exportação da SAFX534\.

MFS\-432689

Alessandra Cristina Navatta

Inclusão de critério na recuperação do registro pai \(SAFX531\) considerando apenas os registros que possuem tipo de rendimento =’3’

MFS\-566870

Alessandra Cristina Navatta

Ajustes referente a nota técnica 03/2023, conforme INFOLEGIS 1740/23 \- Z \- 084 \- EFD REINF\_NT 03/2023 \- DW/T1

Alteração no campo:

Tipo de Dedução: Inclusão da opção 8 

MFS\-805178

Alessandra Cristina Navatta

Para atender a NT 01/2025 do REINF, fizemos os seguintes ajustes:

- Campo Número do Processo, passa a ser não obrigatório \(RN01\)
- \*Campo Código Suspensão, inclusão de validação \(RN06\)

\(\*\) Não houve impacto neste documento \(regra documentada/detalhada na matriz de importação da SAFX531\)

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN01

As rotinas de Carga, Importação \(Online e Batch\) e Exportação do módulo Job Servidor deverão ser alteradas para contemplar os campos listados abaixo na tabela SAFX534:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Código da Empresa

A

003

SIM

SIM

Código do Estabelecimento

A

006

SIM

SIM

Data do Movimento

N

008

SIM

SIM

Indicador de Pessoa Física/Jurídica

A

001

SIM

SIM

Código do Fornecedor

A

014

SIM

SIM

Tipo do Documento

A

005

SIM

SIM

Número do Documento

A

012

SIM

SIM

Série do Documento

A

003

NÃO

SIM

Subsérie do Documento

A

002

NÃO

SIM

Código de Operação

A

006

SIM

SIM

Código do DARF

A

004

SIM

SIM

Tipo de Rendimento

A

001

SIM

SIM

Tipo do Processo

A

001

SIM

SIM

Número do processo

A

020

SIM NÃO

SIM

Código Suspensão

A

014

NÃO

SIM

Número de Dedução

A

002

SIM

SIM

Indicador do Tipo de Dedução

A

002

SIM

NÃO

Valor da Dedução da Base de Cálculo do IR com Exigibilidade Suspensa

N

015V002

NÃO

NÃO

 

MFS\-79885

MFS\-805178

RN02

__Verificação de existência do registro pai__

Por ser esta tabela filha da SAFX531, no momento da importação deve ser verificada a existência de registro correspondente na tabela pai, considerando as mesmas informações dos campos chave da tabela de origem\. A SAFX534 só pode ser associada a uma SAFX531 cujo campo tipo de rendimento seja igual a ‘3’\. Caso não encontre, ou o tipo de rendimento seja diferente de ‘3’ retornar a mensagem: “SAFX531 correspondente a SAFX534 não localizada, ou está com o tipo de rendimento diferente de ‘3’”\. 

__Exclusão de Registros__

Ao excluir o registro, todos os registros filhos serão excluídos também\. 

__Ocorrência permitida:__

Serão permitidos até 25 ocorrências\.

MFS\-79885

MFS\-432689

RN03

__Campo Número de Dedução__

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O número de dedução é de preenchimento obrigatório”

MFS\-79885

RN04

__Campo Indicador do Tipo de Dedução__

__\[ALTERAÇÃO MFS\-566870\] – Inclusão da opção 8__

Lista de Valores válidos: 1, 2, 3, 4, 5, 7, 8\.

Caso seja informado um conteúdo diferente, retornar mensagem: “Indicador do Tipo de Dedução Inválido\. Conteúdo do campo deve ser igual a <1> ou <2> ou <3> ou <4> ou <5> ou <7> ou <8>”\.

MFS\-79885

MFS\-566870

RN05

__Campo Valor da Dedução da Base de Cálculo do IR com Exigibilidade Suspensa__

Informar este campo, apenas se o campo VLR\_REND\_EXIG\_SUSP\_IR da SAFX531 for maior que zero, caso contrário, exibir a mensagem: “O campo ‘Valor da Dedução da Base de Cálculo do IR com Exigibilidade Suspensa’, só deve ser informado, quando o valor do campo ‘Valor do Rendimento Com Exigibilidade Suspensa – IR’ for maior que zero\.

MFS\-79885

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


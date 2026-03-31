# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2087

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2087.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 71 KB

---

THOMSON REUTERS

87

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4835

Julyana Perrucini

Este documento tem como objetivo alterar o tamanho dos campos “COO” e “COO Final para Reinicio” de 006 para 009 posições\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX2087 \- Cadastro de Equipamento ECF, que deve ser criada com a seguinte estrutura:

__\[ALTERADA – OS4835\]__

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Empresa

A

003

SIM

NÃO

Estabelecimento

A

006

SIM

NÃO

Modelo Documento

A

002

SIM

NÃO

Nùmero do Caixa

A

003

SIM

SIM

Data validade

N

008

NÃO

NÃO

Código Modelo NF

A

002

SIM

NÃO

Número de fabricação

A

021

NÃO

NÃO

MF adicional

A

001

NÃO

NÃO

Tipo de ECF

A

007

NÃO

NÃO

Marca do ECF

A

030

NÃO

NÃO

Modelo do ECF

A

030

NÃO

NÃO

Número do Aplicativo

A

002

NÃO

NÃO

Nome do Aplicativo

A

040

NÃO

NÃO

Versão do Aplicativo

A

010

NÃO

NÃO

Indicador Pessoa Física/Jurídica

A

001

NÃO

NÃO

Código da Pessoa Física/Jurídica

A

014

NÃO

NÃO

Linha 01

A

042

NÃO

NÃO

Linha 02

A

042

NÃO

NÃO

Versão do SB

A

010

NÃO

NÃO

Data da gravação do SB

N

008

NÃO

NÃO

Hora da gravação do SB

N

006

NÃO

NÃO

Número do usuário

A

002

NÃO

NÃO

Data do cadastro

N

008

NÃO

NÃO

Hora do cadastro

N

006

NÃO

NÃO

Incidência de Desconto ISSQN

A

001

NÃO

NÃO

Indicador do Tipo de Desconto sobre subtotal

A

001

NÃO

NÃO

Indicador do Tipo de Acréscimo sobre subtotal

A

001

NÃO

NÃO

Ordem de aplicação de Desconto e Acréscimo

A

001

NÃO

NÃO

Versão da biblioteca

A

008

NÃO

NÃO

Comando de geração

A

003

NÃO

NÃO

Versão do Ato/COTEPE

A

015

NÃO

NÃO

Indicador de Arredondamento ou Truncamento \(IAT\)

A

001

NÃO

NÃO

Casas decimais da quantidade

N

001

NÃO

NÃO

Casas decimais de valor unitário

N

001

NÃO

NÃO

COO

A

 009

NÃO

NÃO

CRO \(Contador de Reinício de Operação\)

A

006

NÃO

NÃO

GT \(Totalizador Geral\)

N

015V002

NÃO

NÃO

COO Final para Reinicio

A

 009

NÃO

NÃO

Nº da APF

A

009

NÃO

NÃO

Data da APF

N

008

NÃO

NÃO

 

OS4835

RN02

__Campo COO__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

__\[ALTERADA – OS4835\]__

__Tratamento:__

- Será permitida a importação de até nove posições;
- Retirar espaços em branco da direita e esquerda\.

OS4835

RN03

__Campo COO Final para Reinicio__

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo\.

__\[ALTERADA – OS4835\]__

__Tratamento:__

- Será permitida a importação de até nove posições;
- Retirar espaços em branco da direita e esquerda\.

OS4835

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


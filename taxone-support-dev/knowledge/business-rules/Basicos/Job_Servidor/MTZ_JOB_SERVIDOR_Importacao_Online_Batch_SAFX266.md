# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX266

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX266.docx
- **Modificado:** 2021-05-20
- **Tamanho:** 70 KB

---

THOMSON REUTERS

266

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-13327

Julyana Perrucini

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de importação, Online e Batch, da SAFX266 para atender os Registros K290 e K300 da EFD\-ICMS/IPI/ISS\. 

MFS\-21976

Julyana Perrucini

Essa MFS tem como objetivo incluir o campo Inscrição Estadual – AM para atender a geração do arquivo magnético PIM, e o campo Código Diferenciador de Produção para distinguir códigos de produção duplicados\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX266 – Produção Conjunta, que deve ser criada com a seguinte estrutura:

\[ALTERADA – MFS\-21976\]

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

Estabelecimento

A

006

SIM

SIM

Período de Referência

N

006

SIM

SIM

Tipo de Produção Conjunta

N

001

SIM

SIM

Data da Produção no Terceiro

N

008

SIM

SIM

Código da Ordem de Produção

A

030

SIM

SIM

Código Diferenciador de Produção

A

015

NÃO

SIM

Data Início OP

N

008

SIM

SIM

Data Conclusão OP

N

008

NÃO

NÃO

Industrializado para terceiro por encomenda \(S/N\)

A

001

NÃO

NÃO

Inscrição Estadual – AM

A

014

NÃO

NÃO

 

MFS\-13327

MFS\-21976

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-13327

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-13327

RN04

__Campo Período de Referência__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-13327

RN05

__Campo Tipo de Produção Conjunta __

Como o campo é obrigatório de preenchimento e deve ser um conteúdo válido\. Caso esse campo não esteja preenchido ou preenchido de forma incorreta, deve ser exibida mensagem de erro:* “Tipo de Produção Conjunta não preenchido ou inválido”*\.

__Conteúdo válido:__

1 – Própria

2 – Efetuada por Terceiros

MFS\-13327

RN06

__Campo Data da Produção no Terceiro__

Como o campo é obrigatório de preenchimento para o Tipo de Produção Conjunta igual a 2 e deve ser uma data válida\. Caso esse campo não esteja preenchido ou preenchido de forma incorreta, deve ser exibida mensagem de erro: *“Data da Produção no Terceiro não preenchida ou inválida”*\. Se o Tipo de Produção Conjunta for igual a 1 esse campo deve ser preenchido com “branco” \(01/01/1900\)\.

MFS\-13327

RN07

__Campo Código da Ordem de Produção__

Quando esta tabela for utilizada e a empresa não utilizar numeração para as ordens de produção e o Tipo de Produção Conjunta for igual a 1, o campo poderá ser preenchido com qualquer informação que o auxilie em um possível controle \(número de lote, por exemplo\)\.

Como o campo é obrigatório de preenchimento para o Tipo de Produção Conjunta igual a 1\. Caso esse campo não esteja preenchido, deve ser exibida mensagem de erro: *“Código da Ordem de Produção não preenchido”*\. Se o Tipo de Produção Conjunta for igual a 2 esse campo deve ser preenchido com branco\.

Se não desejar que a informação seja utilizada no arquivo da EFD, deverá selecionar o parâmetro “Não informar o número da ordem de produção / serviço” na parametrização do SPED Fiscal, no menu “Parâmetros > Dados Iniciais”\. Mas para utilizar este parâmetro, é necessário que a carga dos dados da produção seja feita com apenas um registro na SAFX266 por Período de Referência\. Caso contrário ocorrerá duplicidade na geração do registro K290\.

MFS\-13327

RN08

__Campo Data Início OP__

Como o campo é obrigatório de preenchimento para o Tipo de Produção Conjunta igual a 1 e deve ser uma data válida\. Caso esse campo não esteja preenchido ou preenchido de forma incorreta, deve ser exibida mensagem de erro: *“Data Início OP não preenchida ou inválida”*\. Se o Tipo de Produção Conjunta for igual a 2 esse campo deve ser preenchido com “branco” \(01/01/1900\)\.

MFS\-13327

RN09

__Campo Data Conclusão OP__

Campo de preenchimento não obrigatório para o Tipo de Produção Conjunta igual a 1 e deve ser uma data válida, aceitar conteúdo informado inclusive “branco” \(01/01/1900\)\.

MFS\-13327

RN10

__Industrializado para terceiro por encomenda \(S/N\)__

Campo de preenchimento não obrigatório\.

__Conteúdo válido:__

S – SIM

N – NÃO

Quando o campo for preenchido, deve ter um dos seguintes valores: “S” ou “N”\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem de erro: *“Industrializado para terceiro por encomenda inválida\. Os valores válidos são: S ou N”\.*

MFS\-13327

RN11

Inscrição Estadual – AM

Campo de preenchimento não obrigatório, aceitar conteúdo informado inclusive nulo ou branco\.

A informação será utilizada na geração do Bloco K do SPED Fiscal \(menu Geração \- PIM\), quando será gerado um arquivo magnético para cada Inscrição Estadual do PIM\.

Quando preenchido, a importação verifica se o conteúdo informado é uma inscrição estadual já cadastrada para o estado do Amazonas\. A inscrição deve estar cadastrada para o Estabelecimento na tabela das inscrições estaduais do Amazonas \(módulo Parâmetros, menu “Funcionais 🡪 Inscrições Estaduais do Estabelecimento AM”\)\. Caso não exista, será gravada a seguinte mensagem no log de erro e o registro não será importado: “Inscrição Estadual\-AM não cadastrada na tabela das Inscrições Estaduais do Estado do Amazonas”\.

MFS\-21976

RN12

__Código Diferenciador de Produção__

Campo de preenchimento não obrigatório, porém chave na tabela, aceitar conteúdo informado, e quando não preenchido, o campo será gravado com um caractere branco\.

MFS\-21976

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


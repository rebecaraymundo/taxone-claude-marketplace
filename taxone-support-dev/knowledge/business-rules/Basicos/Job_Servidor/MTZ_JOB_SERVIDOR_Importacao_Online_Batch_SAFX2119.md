# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2119

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2119.docx
- **Modificado:** 2024-11-26
- **Tamanho:** 77 KB

---

THOMSON REUTERS

 – Parametrização do Identificador da Natureza de Receita

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

Carga à Programação à Execução

 Importação à Programação à Execução     

 Importação batch à Programação à Execução

 Exportação de Dados à Programação à Execução

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

MFS\-690007

Alessandra Navatta

Definição das regras de importação, Online e Batch, da SAFX2119 – Parametrização do Identificador da Natureza de Receita

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN00

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX2119, que deve ser criada com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Empresa

A

003

SIM

SIM

Estabelecimento

A

006

SIM

SIM

Tipo Parametrização

A

001

NÃO

NÃO

Data Validade Inicial

N

008

SIM

SIM

Data Validade Final

N

008

NÃO

NÃO

CST PIS/COFINS

A

002

SIM

SIM

Indicador do Produto

A

001

NÃO

SIM

Produto

A

060

NÃO

SIM

NBM Inicial

A

010

NÃO

SIM

NBM Final

A

010

NÂO

NÃO

Serviço

A

004

NÃO

SIM

Cód\. Natureza da Receita

A

003

SIM

NÃO

CFOP

A

004

NÃO

SIM

Conta Contábil

A

070

NÃO

SIM

Alíquota PIS \(em %\)

N

003V004

NÃO

SIM

Alíquota COFINS \(em %\)

N

003V004

NÃO

SIM

Alíquota PIS \(em Reais\)

N

015V004

NÃO

SIM

Alíquota COFINS \(em Reais\)

N

015V004

NÃO

SIM

Descrição 

A

400

NÃO

NÃO

 

MFS\-690007

RN00\.1

__Campos Chave:__

Empresa, Estabelecimento, CST PIS/COFINS, Data Validade Inicial, Produto, NBM Inicial, Serviço, CFOP, Conta Contábil, Alíquota PIS \(em %\), Alíquota COFINS \(em %\), Alíquota PIS \(em Reais\), Alíquota COFINS \(em Reais\)\.

__Mensagens:__

Na exibição das mensagens, no log, deve ser apresentada as informações chave da tabela, para facilitar o cliente identificar o registro\.

Mfs\-690007

RN01

__Empresa__

Crítica padrão: quando o campo não estiver preenchido,* *o registro não será importado, e no log de erros será gravada a seguinte mensagem: *“Código da empresa não preenchido\.”  *\(Ex\.: código 90001 da CAT\_ERRO\)

MFS\-690007

RN02

__Estabelecimento__

Crítica padrão: quando o campo não estiver preenchido,* *o registro não será importado, e no log de erros será gravada a seguinte mensagem:* “Código do estabelecimento deve ser preenchido\.” *\(Ex\.: código 90002 da CAT\_ERRO\)

MFS\-690007

RN03

__Campo Tipo Parametrização __

Opções válidas:

@ \- Nulo

P \- Produto/NBM

S \- Serviço

A \- CST/Alíquota 

C \- CST/Conta Contábil

Comportamento:

Se não preenchido, o campo deve assumir ‘P’ – Produto/NBM\.

Validação:

Quando preenchido com valor inválido, o registro não será importado e será gerada a seguinte mensagem de erro no log: *“Tipo Parametrização, deve ser preenchido com um valor válido\. Valores Válidos: @, P, S, A ou C\.” *\(ex: código 93732 da CAT\_ERRO\)

MFS\-690007

RN04

__Campo Validade Inicial__

Deve ser data válida, e a data deve ser preenchida\.

Caso estas condições não sejam atendidas, o registro não será importado e serão geradas as seguintes mensagens de erro no log, conforme a situação:*“O Campo Validade Inicial com formato inválido” *\(ex: código 93733 da CAT\_ERRO\)

* “Validade Inicial não preenchida ou inválida” * \(ex: código 93734 da CAT\_ERRO\)

MFS\-690007

RN05

__Campo Validade Final__

Deve ser data válida, e a data final quando preenchida deve ser > data inicial\.

Caso estas condições não sejam atendidas, o registro não será importado e serão geradas as seguintes mensagens de erro no log, conforme a situação: *“O Campo  Validade Final com formato inválido” *\(ex: código 93735 da CAT\_ERRO\)

*“A Validade Final não pode ser menor que a Validade Inicial” * \(ex: código 93737 da CAT\_ERRO\)

MFS\-690007

RN06

__Campo CST PIS/COFINS__

O campo deve ser preenchido e o código deve estar previamente cadastrado na TACES65 \- Códigos Situação Tributária e com Ind\_tributacao =1

Caso não seja preenchido, ou o código não for encontrado na tabela de Códigos de Situação Tributária, o registro não será importado e deve ser exibida a mensagem de erro no log*: ”CST PIS/COFINS deve ser preenchido e deve estar previamente cadastrado na tabela de Códigos Situação Tributária \(TACES65\)” *\(ex: código 93738 da CAT\_ERRO\)

MFS\-690007

RN07

__Campo Indicador do Produto__

Valores Válidos:

1 \- Produto Acabado;

2 \- Insumos;

3 \- Embalagem;

4 \- Consumo;

5 \- Outros;

6 \- Em Elaboração;

7 \- Intermediário;

8 \- Miscelâneas\.

O campo deve ser preenchido quando Tipo Parametrização = P e o código deve estar previamente cadastrado na Tabela de Produtos \(SAFX2013\)\. Nestas condições, caso não preenchido, ou se, não for um valor válido, o registro não será importado e deve ser exibida a mensagem de erro no log*: “Indicador do Produto, deve ser preenchido com um valor válido\. Valores Válidos: 1, 2, 3, 4, 5, 6, 7, ou 8\.” *\(ex: código 

93756 da CAT\_ERRO\)

Este campo não deve ser preenchido, quando Tipo Parametrização for diferente de ‘P’\. Nestas condições, se preenchido, o registro não será importado e deve ser exibida a mensagem de erro no log*:”Indicador do Produto não deve ser preenchido quando Tipo Parametrização não for igual a ‘P’\.” *\(ex: código 93736 da CAT\_ERRO\)

MFS\-690007

RN08

__Campo Produto__

O campo deve ser preenchido quando Tipo Parametrização = P e o código deve estar previamente cadastrado na Tabela de Produtos \(SAFX2013\)\. Nestas condições, caso não preenchido, ou se, não estiver cadastrado na tabela de produtos, o registro não será importado e deve ser exibida a mensagem de erro no log*: ”Produto informado não existe na Tabela Produtos \(SAFX2013\)” *\(ex: código 92446 da CAT\_ERRO\)

Este campo não deve ser preenchido, quando Tipo Parametrização for diferente de ‘P’\. Nestas condições, se preenchido, o registro não será importado e deve ser exibida a mensagem de erro no log*:”Produto não deve ser preenchido quando Tipo Parametrização não for igual a ‘P’\.” *\(ex: código 93739 da CAT\_ERRO\)

MFS\-690007

RN09

__Campo NBM Inicial__

Este campo pode ser preenchido quando Tipo Parametrização = P e neste caso, o código deve estar previamente cadastrado na Tabela Códigos NBM \(SAFX2043\)\. Nestas condições, caso não estiver cadastrado na tabela de NBM, o registro não será importado e deve ser exibida a mensagem de erro no log*:”NBM Inicial deve estar previamente cadastrada na tabela Códigos NBM \(SAFX2043\)” \(*ex: código 93740 da CAT\_ERRO\)

Este campo não deve ser preenchido, quando Tipo Parametrização for diferente de ‘P’\. Nestas condições, se preenchido, o registro não será importado e deve ser exibida a mensagem de erro no log: ”*NBM Inicial não deve ser preenchido quando Tipo Parametrização não for igual a ‘P’\.” *\(ex: código 93741 da CAT\_ERRO\)

Quando Tipo Parametrização for = ‘P’ e o campo NBM Final estiver preenchido e o NBM Inicial sem preenchimento, o registro não será importado e deve ser exibida a mensagem de erro no log*:”NBM Inicial deve ser preenchido\.” *\(ex: código 93742 da CAT\_ERRO\)

MFS\-690007

RN10

__Campo NBM Final__

Este campo pode ser preenchido quando Tipo Parametrização = P e neste caso, o código deve estar previamente cadastrado na Tabela Códigos NBM \(SAFX2043\)\. Nestas condições, caso não estiver cadastrado na tabela de NBM, o registro não será importado e deve ser exibida a mensagem de erro no log:*”NBM Final deve estar previamente cadastrada na tabela Códigos NBM \(SAFX2043\)”*\(ex: código 93743 da CAT\_ERRO\)

Este campo não deve ser preenchido, quando Tipo Parametrização for diferente de ‘P’\. Nestas condições, se preenchido, o registro não será importado e deve ser exibida a mensagem de erro no log*:”NBM Final não deve ser preenchido quando Tipo Parametrização não for igual a ‘P’\.” *\(ex: código 93744 da CAT\_ERRO\)

MFS\-690007

RN11

__Campo Serviço__

O campo deve ser preenchido quando Tipo Parametrização = S e o código deve estar previamente cadastrado na Tabela de Serviços \(SAFX2018\)\. Nestas condições, caso não preenchido, ou se, não estiver cadastrado na tabela de serviços, o registro não será importado e deve ser exibida a mensagem de erro no log: “*Código do Serviço não cadastrado na Tabela de Códigos de Serviço \(SAFX2018\)” *\(ex: código 92585 da CAT\_ERRO\)

Este campo não deve ser preenchido, quando Tipo Parametrização for diferente de ‘S’\. Nestas condições, se preenchido, o registro não será importado e deve ser exibida a mensagem de erro no log: “*Serviço não deve ser preenchido quando Tipo Parametrização não for igual a ‘S’\.”*

\(ex: código 93745 da CAT\_ERRO\)

MFS\-690007

RN12

__Campo Cód\. Natureza da Receita__

O Cód\. Natureza da Receita deve ser preenchido e deve estar previamente cadastrado na TACES72\. Se o código não estiver preenchido, ou não cadastrado na TACES72, o registro não será importado e deve ser exibida a mensagem de erro no log*:”Cód\. Natureza de Receita deve ser preenchida e deve estar previamente cadastrada na tabela de Código da Natureza da Receita \(TACES72\)\.”*\(ex: código 93754 da CAT\_ERRO\)

MFS\-690007

RN13

__Campo CFOP__

Este campo não deve ser preenchido, quando Tipo Parametrização for ‘S’ ou ‘C’\. Nestas condições, se preenchido, o registro não será importado e deve ser exibida a mensagem de erro no log*:”CFOP não deve ser preenchido quando Tipo Parametrização igual a ‘S’ ou‘C’\.”* \(ex: código 93746 da CAT\_ERRO\)

Quando Tipo Parametrização for ‘P’ ou ‘A’ e este campo estiver preenchido, o CFOP deve estrar previamente cadastrado na tabela de Códigos Fiscais \(SAFX2012\)\. Nestas condições, se o código não estiver cadastrado na SAFX2012, o registro não será importado e deve ser exibida a mensagem de erro no log*:”CFOP não está cadastrado na tabela de Códigos Fiscais \(SAFX2012\)\.”* \(ex: código 93747 da CAT\_ERRO\)

MFS\-690007

RN14

__Campo Conta Contábil__

Quando este campo estiver preenchido, a Conta Contábil deve estar previamente cadastrada na tabela de Plano de Contas \(SAFX2002\)\. Nestas condições, se o código não estiver cadastrado na SAFX2002, o registro não será importado e deve ser exibida a mensagem de erro no log:*”Conta Contábil não está cadastrada na tabela de Códigos Fiscais \(SAFX2002\)\.” *\(ex: código 93748 da CAT\_ERRO\)

MFS\-690007

RN15

__Campo Alíquota PIS \(em %\)__

Este campo não deve ser preenchido, quando Tipo Parametrização for ‘C’\. Nestas condições, se preenchido, o registro não será importado e deve ser exibida a mensagem de erro no log: “*Alíquota PIS \(em %\) não deve ser preenchido quando Tipo Parametrização igual a ‘C’\.”* \(ex: código 93749 da CAT\_ERRO\)

Se este campo for preenchido, não pode ser preenchido nenhum dos campos de alíquota PIS/COFINS em Reais\. Nestas condições, se preenchido, o registro não será importado e deve ser exibida a mensagem de erro no log: ”*Não pode ser preenchido Alíquota PIS/COFINS \(em %\)  e Alíquota PIS/COFINS em Reais no mesmo registro\.” *\(ex: código 93753 da CAT\_ERRO\)

Se este campo for preenchido, a Alíquota COFINS em % deve ser preenchida, caso contrário, exibir a mensagem:*”A Alíquota  COFINS \(em %\) deve  ser preenchida quando o campo Alíquota PIS \(em %\) estiver estiver preenchida\.” \(ex: código 93757 da CAT\_ERRO\)*

MFS\-690007

RN16

__Campo Alíquota COFINS \(em %\)__

Este campo não deve ser preenchido, quando Tipo Parametrização for ‘C’\. Nestas condições, se preenchido, o registro não será importado e deve ser exibida a mensagem de erro no log*:”Alíquota COFINS \(em %\) não deve ser preenchido quando Tipo Parametrização igual a ‘C’\.” *\(ex: código 93750 da CAT\_ERRO\)

Se este campo for preenchido, não pode ser preenchido nenhum dos campos de alíquota PIS e COFINS em Reais\. Nestas condições, se preenchido, o registro não será importado e deve ser exibida a mensagem de erro no log:*”Não pode ser preenchido Alíquota PIS/COFINS \(em %\)  e Alíquota PIS/COFINS em Reais no mesmo registro\.”  *\(ex: código 93753 da CAT\_ERRO\)

Se este campo for preenchido, a Alíquota PIS em % deve ser preenchida, caso contrário, exibir a mensagem:*”A Alíquota  PIS \(em %\) deve  ser preenchida quando o campo Alíquota COFINS \(em %\) estiver estiver preenchida\.” \(ex: código 93758 da CAT\_ERRO\)*

MFS\-690007

RN17

__Campo Alíquota PIS \(em Reais\)__

Este campo não deve ser preenchido, quando Tipo Parametrização for ‘C’\. Nestas condições, se preenchido, o registro não será importado e deve ser exibida a mensagem de erro no log*:”Alíquota PIS \(em Reais\) não deve ser preenchido quando Tipo Parametrização igual a ‘C’\.”* \(ex: código 93751 da CAT\_ERRO\)

Se este campo for preenchido, a Alíquota COFINS em % deve ser preenchida, caso contrário, exibir a mensagem:*”A Alíquota  COFINS \(em Reais\) deve  ser preenchida quando o campo Alíquota PIS \(em Reais\) estiver estiver preenchida\.” \(ex: código 93759 da CAT\_ERRO\)*

MFS\-690007

RN18

__Campo Alíquota COFINS \(em Reais\)__

Este campo não deve ser preenchido, quando Tipo Parametrização for ‘C’\. Nestas condições, se preenchido, o registro não será importado e deve ser exibida a mensagem de erro no log*:”Alíquota COFINS \(em Reais\) não deve ser preenchido quando Tipo Parametrização igual a ‘C’\.” *\(ex: código 93752 da CAT\_ERRO\)

Se este campo for preenchido, a Alíquota PIS em Reias deve ser preenchida, caso contrário, exibir a mensagem:*”A Alíquota  PIS \(em Reais\) deve  ser preenchida quando o campo Alíquota COFINS \(em Reais\) estiver estiver preenchida\.” \(ex: código 93760 da CAT\_ERRO\)*

MFS\-690007

RN19

__Campo Descrição__

Campo de texto\. Este campo não é recuperado de nenhuma tabela\. 

MFS\-690007

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


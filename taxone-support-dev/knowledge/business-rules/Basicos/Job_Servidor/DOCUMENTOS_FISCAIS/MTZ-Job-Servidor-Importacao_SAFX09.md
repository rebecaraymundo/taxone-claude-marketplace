# MTZ-Job-Servidor-Importacao_SAFX09

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX09.docx
- **Modificado:** 2022-11-11
- **Tamanho:** 46 KB

---

# Módulo Job Servidor – Carga/Importação/Batch e Exportação SAFX09 \(Item de Serviço\)

*\(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX09, conforme o Manual de Layout, o que facilita a consulta\) \(Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como  RN00\)*

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Carga 🡪 Execução

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

\- Exportação Dados 🡪 Execução

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3003

Incluir tratamento que compõe o Valor do INSS

O objetivo desta OS é passar a carregar a informação de INSS Retido na SAFX09\.

14/09/2010

CH101898

Tratamento de erro para Situação Tributária COFINS

Incluir tratamento de erro para o campo situação tributária de COFINS

14/07/2011

OS3065\-DW

Novos campos

Inclusão de novos campos na SAFX07 para atendimento ao SEF II \- PE

14/09/2011

OS3169\-GE16

EFD PIS/COFINS \- Criar Indicador para Documentos de Invoice na SAFX07

O cliente Chevron necessita informar os Documentos de Invoice para geração dos registros A100, A120 e A170 do EFD PIS/COFINS\. Ocorre que pela regra do EFD PIS/COFINS informada no Guia Prático versão 1\.0\.3 de 01/09/2011, esses documentos de importação devem ser gerados nos registros A100, A120 e A170\.

Para que o cliente utilize corretamente esses documentos e que os mesmos não sejam lidos erroneamente para outras obrigações, deverá ser criado um Indicador na capa do Documento Fiscal que diferencie o Invoice de Documentos Fiscais de Serviço comuns\.

10/12/2011

OS3924

Inclusão de novo campo

Incluir o campo NBS

15/02/2013

OS3841

Tratamento na Importação da SAFX09

Incluir um tratamento para recuperar o IDENT da tabela pai \(SAFX07\), no momento da importação ou inserção de dados na tabela de itens de serviço \(SAFX09\)\.

17/06/2013

OS4226

Inclusão de novo campo

Para atender o registro B440 do ATO Cotepe 70/05 o cliente Odebrecht S\.A necessita que seja criado campo na SAFX09 que receberá o campo 6 do registro, a alíquota  do ISS\.   

31/03/2014

OS4514

Inclusão de campos para atender e\-Social

Criação de novos campos que serão utilizados para integração com e\-Social

22/05/2014

OS 4667

DW \- Municipal \- Florianópolis \-

Será criado o campo “Código Situação Tributária ISS”, que ficará localizado da tela de “Item Serviço” \(SAFX09\)\.

MFS8789

Inclusão de campos para atender ao REINF

Para atender o registro R\-2010 e R\-2020 do REINF, foram criados 4 novos campos   

12/01/2017

MFS10357

Inclusão de campos para atender ao REINF

Para atender o registro R\-2010 e R\-2020 do REINF, foram criados 6 novos campos   

04/04/2017

MFS13205

Inclusão de campos para atender ao REINF

Para atender o registro R\-2010 e R\-2020 do REINF, foram criados 3 novos campos   

20/09/2017

MFS\-20985

Inclusão do campo Valor do Abatimento não tributado

Este documento tem como objetivo criar o campo Valor do Abatimento não tributado

18/09/2018

MFS24154

Alteração do campo 86

Alteração na lista de valores válidos do campo 86\- Natureza da Base de Crédito \(EFD\-PIS/PASEP\-COFINS\)

01/02/2019

MFS31367

Andréa Rocha

Inclusão de campo de código de atividade

17/12/2019

MFS31262

Andréa Rocha

Inclusão de campos reservados

19/06/2020

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

*\(espaço reservado para regras genéricas, que não dizem respeito a campos específicos\)*

__RN00A__

__Regra do Controle de Concorrência entre processos de Importação e Equalização__

O controle de concorrência garante que não seja executado simultaneamente mais de um processo de importação das SAFX07, SAFX08, SAFX09 e equalização DataMart, referenciados por uma determinada empresa e estabelecimento\.

Com a liberação da MFS\-87822 o controle de concorrência entre processos de importação e equalização de documento fiscal passou a considerar também o período \(mês/ano\) dos documentos fiscais\. Ou seja, o controle passou a ser feito por empresa, estabelecimento e período \(mês/ano\) dos documentos fiscais\.

Tabelas utilizadas pelo Controle de Concorrência:

\- PRT\_IDENT\_DMART\_PERÍODO: Controle por empresa, estabelecimento e período\.

\- PRT\_IDENT\_DMART: Controle por empresa, estabelecimento\.

Antes da MFS\-87822, o controle de concorrência por empresa, estabelecimento e período era realizado apenas na equalização DataMart\.

Com a MFS\-82822 a tabela PRT\_IDENT\_DMART\_PERÍODO passa a ser utilizada na equalização e na importação dos documentos fiscais\.

Exemplo de controle de processos ao serem executados simultaneamente:

\-  Dois processos: um de Importação e outro de Importação;

\-  Dois processos: um de Equalização e outro de Equalização;

\-  Dois processos: um de Importação e outro de Equalização;

Determinação do período para controle de concorrência:

1. Importação com uso do Limita período:

Período considerado para o controle de concorrência = período informado na tela de programação da importação\.

1. Importação sem limita período:

Período considerado para o controle de concorrência = período determinado pelo mês/ano da data da nota\.

1. Equalização Data Mart:

Período considerado para o controle de concorrência = período informado na tela de programação da importação\.

Nesse controle de concorrência estão sendo consideradas as duas formas de importação, batch e online\.

MFS87822

__RN76__

__Campo 76 – Base INSS__:

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Base INSS nas tabelas SAFX09 / X09\_ITENS\_SERV\.

Tabela: __SAFX09__

Item: __Sugerido 76__

Descrição: __Valor__ __Base INSS__

Nome do Campo: __Será definido pelo A&D__

Comentário: __Informar o valor da Base INSS calculado sobre o item vinculado ao serviço prestado\. Essas informações passaram a ser solicitadas pela IN\-SRB 971/09\. As obrigações SEFIP e GPS continuam utilizando o valor da Base do INSS da Capa do Documento Fiscal\.__

Tamanho: __015V002__

Tipo: __N__

Não obrigatório

OS3003

__RN77__

__Campo 77 – INSS Retido__:

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo INSS Retido nas tabelas SAFX09 / X09\_ITENS\_SERV\.

Tabela: __SAFX09__

Item: __Sugerido 77__

Descrição: __Valor__ __INSS Retido__

Nome do Campo: __Será definido pelo A&D__

Comentário: __Informar o valor do INSS Retido calculado sobre o item vinculado ao serviço prestado\.  Essas informações passaram a ser solicitadas pela IN\-SRB 971/09\. As obrigações SEFIP e GPS continuam utilizando o valor do INSS Retido da Capa do Documento Fiscal\.__

Tamanho: __015V002__

Tipo: __N__

Não obrigatório

OS3003

__RN78__

__Campo 78 – Alíquota INSS__:

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Aliquota INSS nas tabelas SAFX09 / X09\_ITENS\_SERV\.

Tabela: __SAFX09__

Item: __Sugerido 78__

Descrição: __Valor__ __Aliquota__ __INSS__

Nome do Campo: __Será definido pelo A&D__

Comentário: __Informar o valor da Alíquota de INSS calculado sobre o item vinculado ao serviço prestado\. Essas informações passaram a ser solicitadas pela IN\-SRB 971/09\. As obrigações SEFIP e GPS continuam utilizando o valor da Alíquota do INSS da Capa do Documento Fiscal\.__

Tamanho: __003V004__

Tipo: __N__

Não obrigatório

OS3003

__RN69__

__Campo 69 – Situação Tributária COFINS__

Se o campo 69 \(COD\_SITUACAO\_COFINS\) <> de caracteres numéricos, então gerar log de erro conforme o código “91628” da TFIX22:

“Codigo da Situacao Tributaria COFINS inexistente ou invalido para a data do documento\.”

CH101898

__RN86__

__Campo 86 \- Natureza da Base de Crédito \(EFD\-PIS/PASEP\-COFINS\)__

01 \- Aquisição de bens para revenda\.

02 \- Aquisição de bens utilizados como insumo\.

03 \- Aquisição de serviços utilizados como insumo\.

04 \- Energia elétrica e térmica, inclusive sob a forma de vapor\.

05 \- Aluguéis de prédios\.

06 \- Aluguéis de máquinas e equipamentos\.

07 \- Armazenagem de mercadoria e frete na operação de venda\.

08 \- Contraprestações de arrendamento mercantil

09 \- Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado \(crédito sobre encargos de depreciação\)\.

10 \- Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado \(crédito com base no valor de aquisição\)\.

11 \- Amortização e Depreciação de edificações e benfeitorias em imóveis\.

12 \- Devolução de Vendas Sujeitas à Incidência Não Cumulativa\.

13 \- Outras Operações com Direito a Crédito\.

14 \- Atividade de Transporte de Cargas – Subcontratação\.

15 \- Atividade Imobiliária – Custo Incorrido de Unidade Imobiliária\.

16 – Atividade Imobiliária – Custo Orçado de Unidade não concluída

17 \- Atividade de Prestação de Serviços de Limpeza, Conservação e Manutenção – vale\-transporte, vale\-refeição ou vale\-alimentação, fardamento ou uniforme\.

18 \- Estoque de abertura de bens\.

Obs\.: Retirar a regra relativa a classificação do documento fiscal, mostrar todos os códigos independente da classificação do documento e incluir os novos códigos\.

Crítica 🡪 *Quando preenchido*, o conteúdo do campo deverá ser um dos novos valores da lista acima\. Caso contrário, será gravada a mensagem abaixo no log e o registro não será importado: 

      “Esse campo deve ser preenchido com o Codigo da Natureza da Base de Credito 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17 ou 18, conforme a tabela 4\.3\.7 \- EFD PIS/COFINS”

MFS24154

__RN87__

__Campo Valor Acréscimo:                            __\(campo criado na OS3065\-dw\)

Obrigatório 🡪 Não 

Críticas 🡪 sem críticas

OS3065\-dw

__RN88__

Caso ao importar o registro da SAFX09 a capa dessa NF da SAFX07 possuir no campo 12 – COD\_CLASS\_DOC\_FIS o valor “I” \(referente a Invoice\) a importação deverá ser permitida normalmente\.

OS3169\-GE16

__RN89__

__Campo NBS:__

O campo NBS deve ser recuperado da SAFX2055, caso contrário exibir a msg ao usuário: O código Codigo NBS não esta cadastrado\.

Solução: Realize o Cadastro no modulo DW no menu Manutencao \-> Codigos \-> Codigo NBS

Campo Não obrigatório

\- Recuperação do código NBS:

O sistema deve considerar o código de maior validade que seja menor ou igual a data da escrita fiscal da SAFX09 \(03 \- DATA\_FISCAL\)

OS3924

__RN90__

Deve ser recuperado o IDENT da tabela pai \(SAFX07\), no momento da importação ou inserção de dados na SAFX09 \(deixando de considerar o IDENT mais atual, baseado na data de importação do registro\)\.

Esta alteração se faz necessária, para manter o padrão de tratamento já utilizado para a SAFX08 e conservar o vínculo entre os IDENTs dos cadastros carregados inicialmente, que tenham sido apresentados em obrigações acessórias\. 

OS3841

__RN91__

__Alíquota do ISS Retido__:

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o campo Alíquota do ISS Retido nas tabelas SAFX09 / X09\_ITENS\_SERV\.

Tabela: __SAFX09__

Item: __Será definido pelo A&D\.__

Descrição: __Alíquota__ __do__ __ISS Retido__

Nome do Campo: __Será definido pelo A&D__

Comentário: __Informar a alíquota do ISS retido que será utilizada na geração do campo 06 do registro B440 “Relatório dos valores retidos” do Ato Cotepe Nº 70/05\.__

Tamanho: __03V004__

Tipo: __N__

Não obrigatório

OS4226

__RN92__

__Campo Valor Total Adicional__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o novo campo nas tabelas SAFX09 / X09\_ITENS\_SERV\.

Obrigatoriedade: Não obrigatório

Item: A ser definido por A&D

Descrição: Valor Total Adicional

Nome do Campo: A ser definido por A&D

Comentário: Valor Total Adicional da NF\.

Tamanho: 015V002

Tipo: N

OS4514

__RN93__

__Campo XPTO__ __Valor Total não Retido pelo Contratante__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o novo campo nas tabelas SAFX09 / X09\_ITENS\_SERV\.

Obrigatoriedade: Não obrigatório

Item: A ser definido por A&D

Descrição: Valor Total não Retido pelo Contratante

Nome do Campo: A ser definido por A&D

Comentário: Valor de retenção que deixou de ser efetuada pelo contratante\.

Tamanho: 015V002

Tipo: N

OS4514

__RN94__

__Campo Valor das Deduções Previdenciárias da NF__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o novo campo nas tabelas SAFX09 / X09\_ITENS\_SERV\.

Obrigatoriedade: Não obrigatório

Item: A ser definido por A&D

Descrição: Valor das Deduções Previdenciárias da NF

Nome do Campo: A ser definido por A&D

Comentário: Valor das Deduções da Nota Fiscal/Fatura\.

Tamanho: 015V002

Tipo: N

OS4514

__RN95__

__Campo Valor da Retenção Previdenciária da NF__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o novo campo nas tabelas SAFX09 / X09\_ITENS\_SERV\.

Obrigatoriedade: Não obrigatório

Item: A ser definido por A&D

Descrição: Valor da Retenção Previdenciária da NF

Nome do Campo: A ser definido por A&D

Comentário: Valor da retenção apurada relativa aos serviços contidos na nota fiscal/fatura\.

Tamanho: 015V002

Tipo: N

OS4514

__RN96__

__Campo Valor da Retenção Previdenciária relativo a Serviços Subempreitados__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o novo campo nas tabelas SAFX09 / X09\_ITENS\_SERV\.

Obrigatoriedade: Não obrigatório

Item: A ser definido por A&D

Descrição: Valor da Retenção Previdenciária relativo a Serviços Subempreitados

Nome do Campo: A ser definido por A&D

Comentário: Valor da retenção destacada na nota fiscal relativo aos serviços subempreitados, se houver\.

Tamanho: 015V002

Tipo: N

OS4514

__RN97__

__Campo Código Situação Tributária ISS__

__Item__: Verificar com o A&D

__Nome__: Verificar com o A&D

__Descrição__: Código CST \(Código Situação Tributária ISS\)

__Tamanho__: 02

__Tipo__: Numérico

__Obrigatoriedade__: N

__Valor default__: Nulo

Quando preenchido, o seu conteúdo será verificado na TACES88 \(Código Situação Tributária ISS\)\. 

Caso o código informado não exista na tabela, será gravada uma mensagem de erro no log e o item não será importado: 

 *“Código da Situação Tributária ISS inválido”*

O log informará os dados básicos do item da nota para permitir a identificação e correção do problema\.

OS4667

__RN98__

__Campo \- Retenção Principal não Efetuada:__

__Tipo: __N

__Tamanho: __015V002

__Obrigatório: __Não

MFS8789

__RN99__

__Campo \- Retenção Adicional não Efetuada:__

__Tipo: __N

__Tamanho: __015V002

__Obrigatório: __Não

MFS8789

__RN100__

__Campo \- Dedução por Custo de Alimentação:__

__Tipo: __N

__Tamanho: __015V002

__Obrigatório: __Não

MFS8789

__RN101__

__Campo \- Dedução por Custo de Transporte:__

__Tipo: __N

__Tamanho: __015V002

__Obrigatório: __Não

MFS8789

__RN102__

A rotina de importação online e batch do módulo JOB Servidor deverão ser ajustadas para que contemple a alteração da tabela SAFX09 – Item de Serviço

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Tipo do Processo Retenção Principal

A

001

NÃO

SIM

Número do Processo Retenção Principal

A

021

NÃO

SIM

Código Suspensão Principal

A

014

NÃO

SIM

Tipo do Processo Retenção Adicional

A

001

NÃO

SIM

Número do Processo Retenção Adicional

A

021

NÃO

SIM

Código Suspensão Adicional

A

014

NÃO

SIM

MFS10357

RN103

__Campo Tipo do Processo Retenção Principal__

Crítica: Valor esperado 1, 2 e 3 caso contrário exibir a seguinte mensagem: “Indicador do Tipo do Processo Retenção Principal deve ser <1> ou <2> ou <3>”\.

Se tipo de processo retenção principal não preenchido e número processo retenção principal estiver preenchido exibir a seguinte mensagem: “Tipo de Processo Retenção Principal” deve ser preenchido referente ao “Número do Processo Retenção Principal” identificado\. 

MFS10357

RN104

__Campo Número do Processo Retenção Principal__

Se tipo de processo retenção principal não preenchido e número processo retenção principal estiver preenchido exibir a seguinte mensagem: “Número de Processo Retenção Principal” deve ser preenchido referente ao “Tipo de Processo Retenção Principal identificado”\.

Caso campo não preenchido quando tipo do processo retenção principal igual a “1” e “2” exibir a seguinte mensagem: “Campo Número do Processo Retenção Principal deve ser preenchido”

Caso campo preenchido quando tipo do processo retenção principal igual a “3” exibir a seguinte mensagem: “Campo Número do Processo Retenção Principal não deve ser preenchido quando Tipo do Processo Retenção Principal igual a 3 – Judicial Prestador”\.

Caso não identificado Número do Processo Retenção Principal no cadastro de Processos \(SAFX2058\), exibir a seguinte mensagem: “Número Processo Retenção Principal não cadastrado na tabela de Processos \(SAFX2058\)”\.

MFS10357

RN105

__Campo Código Suspensão Principal__

Caso não encontrado o código de suspensão no cadastro de suspensão \(SAFX2059\) referente aos processos identificados pelos campos \(“Tipo do Processo Retenção Principal” e “Número do Processo Retenção Principal”\) exibir a seguinte mensagem: “Código de Suspensão” deve ser preenchido, referente ao “Tipo do Processo Retenção Principal” e “Número do Processo Retenção Principal” identificado\.

Caso campo preenchido quando tipo do processo retenção principal igual a “3” exibir a seguinte mensagem: “Campo Número do Processo Retenção Principal não deve ser preenchido quando Tipo do Processo Retenção Principal igual a 3 – Judicial Prestador”\.

MFS10357

RN106

__Campo Tipo do Processo Retenção Adicional__

Crítica: Valor esperado 1, 2 e 3 caso contrário exibir a seguinte mensagem: “Indicador do Tipo do Processo Retenção Adicional deve ser <1> ou <2> ou <3>”\.

Se tipo de processo retenção Adicional não preenchido e número processo retenção Adicional estiver preenchido exibir a seguinte mensagem: “Tipo de Processo Retenção Adicional” deve ser preenchido referente ao “Número do Processo Retenção Adicional” identificado\. 

MFS10357

RN107

__Campo Número do Processo Retenção Adicional__

Se tipo de processo retenção Adicional não preenchido e número processo retenção Adicional estiver preenchido exibir a seguinte mensagem: “Número de Processo Retenção Adicional” deve ser preenchido referente ao “Tipo de Processo Retenção Adicional identificado”\.

Caso campo não preenchido quando tipo do processo retenção Adicional igual a “1” e “2” exibir a seguinte mensagem: “Campo Número do Processo Retenção Adicional deve ser preenchido”

Caso campo preenchido quando tipo do processo retenção Adicional igual a “3” exibir a seguinte mensagem: “Campo Número do Processo Retenção Adicional não deve ser preenchido quando Tipo do Processo Retenção Adicional igual a 3 – Judicial Prestador”\.

Caso não identificado Número do Processo Retenção Adicional no cadastro de Processos \(SAFX2058\), exibir a seguinte mensagem: “Número Processo Retenção Adicional não cadastrado na tabela de Processos \(SAFX2058\)”\.

MFS10357

RN108

__Campo Código Suspensão Adicional__

Caso não encontrado o código de suspensão no cadastro de suspensão \(SAFX2059\) referente aos processos identificados pelos campos \(“Tipo do Processo Retenção Adicional” e “Número do Processo Retenção Adicional”\) exibir a seguinte mensagem: “Código de Suspensão” deve ser preenchido, referente ao “Tipo do Processo Retenção Adicional” e “Número do Processo Retenção Adicional” identificado\.

Caso campo preenchido quando tipo do processo retenção Adicional igual a “3” exibir a seguinte mensagem: “Campo Número do Processo Retenção Adicional não deve ser preenchido quando Tipo do Processo Retenção Adicional igual a 3 – Judicial Prestador”\.

MFS10357

RN109

__Campo \- Valor do Serviço Prestado em Condições Especiais para 15 anos:__

__Tipo: __N

__Tamanho: __015V002

__Obrigatório: __Não

MFS13205

RN110

__Campo \- Valor do Serviço Prestado em Condições Especiais para 20 anos:__

__Tipo: __N

__Tamanho: __015V002

__Obrigatório: __Não

MFS13205

RN111

__Campo \- Valor do Serviço Prestado em Condições Especiais para 25 anos:__

__Tipo: __N

__Tamanho: __015V002

__Obrigatório: __Não

MFS13205

RN112

__Campo – Valor do Abatimento não tributado:__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o novo campo na tabela SAFX08\. 

__Item:__ A ser reservado pelo Desenvolvimento

__Nome do Campo:__ Será definido pelo Desenvolvimento

__Tipo: __N

__Tamanho: __015V002

__Obrigatório: __Não

__Chave:__ Não

__Comentário: __Informar o valor do abatimento não tributado e não comercial\.

Exemplos:

- Desconto da ZFM;
- Quando a aplicação da redução de base de cálculo ficar condicionada ao repasse para o contribuinte do valor equivalente ao imposto dispensado na operação;

Isenção com repasse para o contribuinte na saída, em operação interna, de mercadoria ou bem destinado a órgãos da administração pública estadual direta, suas fundações e autarquias\.

MFS\-20985

RN113

__Campo \- Atividade \(RJ\)__

__Tipo: __N

__Tamanho: __007

__Obrigatório: __Não

MFS31367

RN114

__Campo – Reservado 4__

__Tipo: __A

__Tamanho: __050

__Obrigatório: __Não

MFS31262

RN115

__Campo – Reservado 5__

__Tipo: __A

__Tamanho: __050

__Obrigatório: __Não

MFS31262

RN116

__Campo – Reservado 6__

__Tipo: __N

__Tamanho: __015V002

__Obrigatório: __Não

MFS31262

RN117

__Campo – Reservado 7__

__Tipo: __N

__Tamanho: __015V002

__Obrigatório: __Não

MFS31262

RN118

__Campo – Reservado 8__

__Tipo: __N

__Tamanho: __015V002

__Obrigatório: __Não

MFS31262


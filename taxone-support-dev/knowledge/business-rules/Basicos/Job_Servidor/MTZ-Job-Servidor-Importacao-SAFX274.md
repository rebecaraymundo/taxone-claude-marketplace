# MTZ-Job-Servidor-Importacao-SAFX274

- **Fonte:** MTZ-Job-Servidor-Importacao-SAFX274.docx
- **Modificado:** 2025-12-03
- **Tamanho:** 42 KB

---

# Módulo Job Servidor 

#  Importação SAFX274 

#  \(Tabela dos Créditos Disponíveis da EFD – Contribuições\) 

__Localização__: Menu Básicos, Módulo: Job Servidor, item Importação 🡪 Execução

##                                            Documento de Requisito

__Doc__

__Alteração__

__Data__

__Resp__

MFS26175

Criação da SAFX274 p/carga dos créditos disponíveis da EFD – Contribuições

07/05/2019

\(Criação do doc\)

Vânia Mattos

MFS\-547432

Permitir a carga dos créditos, mesmo existindo apuração gerada na base\. 

17/07/2023

Alessandra Cristina Navatta

__RN00 – Regras Gerais__

A tabela SAFX274 foi criada pela MFS26175 com objetivo de permitir a carga dos dados dos créditos disponíveis do módulo EFD – Contribuições\. A tabela dos créditos disponíveis já existe, e sua manutenção é feita nos menus descritos a seguir:

- Obrigações 🡪 Manutenção 🡪 Controle dos Créditos Fiscais Produtos – PIS/PASEP 🡪 Créditos Disponíveis
- Obrigações 🡪 Manutenção 🡪 Controle dos Créditos Fiscais Produtos – COFINS 🡪 Créditos Disponíveis
- Obrigações SCP 🡪 Manutenção 🡪 Controle dos Créditos Fiscais Produtos – PIS/PASEP 🡪 Créditos Disponíveis
- Obrigações SCP 🡪 Manutenção 🡪 Controle dos Créditos Fiscais Produtos – COFINS 🡪 Créditos Disponíveis

Tabelas definitivas que receberão os dados da nova SAFX: 

EPC\_APUR\_CRED\_DISP

Tabela dos créditos

EPC\_APURACAO

Tabela da apuração

A seguir serão descritas as regras de validação campo a campo, e as regras da gravação dos dados nas duas tabelas \(__RN17\-Gravação dos Dados na Tabela da Apuração e Tabela dos Créditos__\)\.

__RN01 – Código da Empresa__

Crítica padrão: quando o campo não estiver preenchido,* *o registro não será importado, e no log de erros será gravada a seguinte mensagem \(ex: código 90001 da CAT\_ERRO\):

*                                               “Código da empresa não preenchido” *

__RN02 – Código do Estabelecimento__

Crítica padrão: quando o campo não estiver preenchido,* *o registro não será importado, e no log de erros será gravada a seguinte mensagem \(ex: código 90002 da CAT\_ERRO\):

*                                                “Código do estabelecimento deve ser preenchido”*

O estabelecimento informado deve atender a uma das seguintes condições:

- Ser um estabelecimento centralizador, conforme a centralização de estabelecimentos do módulo Parâmetros, menu “Preliminares > Centralização da Escrituração de Obrigações Federais”;
- Ser um estabelecimento independente, ou seja, não constar na centralização de estabelecimentos do módulo Parâmetros \(menu citado acima\), nem como centralizador, nem como centralizado;

Desta forma, *não* pode ser um estabelecimento que conste na centralização como um centralizado\. Caso isso aconteça, o registro não será importado e será gerada a seguinte mensagem de erro no log:

* “Estabelecimento inválido\. Deve ser um estabelecimento centralizador, ou um estabelecimento independente”*

 

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN03 – Código da SCP__

Campo *não* obrigatório\.

Quando preenchido, deve ser um código da Tabela de Cadastro da SCP \(SAFX2057\)\. Caso contrário, o registro não será importado e será gerada a seguinte mensagem de erro no log:

*                                             “Código da SCP não cadastrado”*

                                            \(ex: código 92551 da CAT\_ERRO\)

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

  

__RN04 – Data Inicial do Período da Apuração\)__

__RN05 – Data Final do Período da Apuração__

As duas datas são de preenchimento obrigatório\.

Devem ser datas válidas, e a data final deve ser > data inicial\.

Caso estas condições não sejam atendidas, o registro não será importado e serão geradas as seguintes mensagens de erro no log, conforme a situação:

*                                     “Data Inicial do Período não preenchida ou inválida” *

                                              \(ex: código 92970 da CAT\_ERRO\)

*                                     “Data Final do Período não preenchida ou inválida”*

*                                           *  \(ex: código 92971 da CAT\_ERRO\)

*                  “A Data Final de Apuração não pode ser menor que a Data Inicial de Apuração” *

                                              \(ex: código 90526 da CAT\_ERRO\)

__Crítica da existência da Apuração:__

 

A importação de créditos será permitida apenas para usuários que estão implantando o módulo EFD\-Contribuições, ou migrando de outros sistemas \(GF ou Smart\)\. Por isso, serão feitas algumas validações, e em alguns casos, a importação será rejeitada\.

Observação sobre a coluna COD\_TIPO\_LIVRO da EPC\_APURACAO:

\(código de controle interno do módulo\) 

COD\_TIPO\_LIVRO = “__SLI__” = Apuração incluída manualmente pelas telas de manutenção dos 

Créditos Disponíveis, ou via importação \(SAFX274\), referentes a períodos anteriores da escrituração digital realizada no modulo EFD\-Contribuições;

COD\_TIPO\_LIVRO = “__EPC__” = Apuração gerada pelo módulo EFD\-Contribuições;

O módulo EFD\-Contribuições permite a inclusão de um crédito disponível mesmo quando a apuração do período não existe\. Neste caso, além de gravar o registro do crédito na tabela EPC\_APUR\_CRED\_DISP, é gravado também um registro da apuração do período na tabela EPC\_APURACAO\.

\[MFS\-547432 – EXCLUSÃO\] – Não será impedida a inserção dos créditos, quando existir apuração na base\.

__1\-Crítica da existência de Apuração no período, ou períodos anteriores:__

Será verificada a existência do registro da apuração para a Empresa e Estabelecimento em questão, seja no período informado, __*ou*__, para períodos anteriores, da seguinte forma:

Tabela EPC\_APURACAO

\- COD\_EMPRESA = Campo “01\-Código da Empresa” da SAFX274

\- COD\_ESTAB = Campo “02\-Código do Estabelecimento” da SAFX274

\- COD\_TIPO\_LIVRO = “__EPC__”

\- DAT\_APUR\_FIM = Qualquer data que seja <= campo “05\-Data Final do Período” da SAFX274

\- COD\_SCP = Campo “03\-Código da SCP” da SAFX274

Caso exista\(m\) registro\(s\) de apuração conforme os dados acima, a importação não será permitida e será gerada a seguinte mensagem de erro no log:

* “A inclusão de créditos disponíveis não é permitida quando existir apuração já gerada para o período, ou períodos anteriores”*

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__2\-Crítica da existência de Apuração Fechada em períodos posteriores:__

Nesse caso, será verificada a existência de apurações para períodos *posteriores* ao período informado, que já estejam validadas, da seguinte forma:

\- COD\_EMPRESA = Campo “01\-Código da Empresa” da SAFX274

\- COD\_ESTAB = Campo “02\-Código do Estabelecimento” da SAFX274

\- COD\_TIPO\_LIVRO = “__EPC__”

\- DAT\_APUR\_INI = Qualquer data de período posterior ao período informado na SAFX274 

\- DAT\_APUR\_FIM = Qualquer data de período posterior ao período informado na SAFX274

\- COD\_SCP = Campo “03\-Código da SCP” da SAFX274

\- IND\_SITUACAO\_APUR = “__3__” \(Apuração Fechada\)

Caso exista\(m\) registro\(s\) de apuração conforme os dados acima, a importação não será permitida e será gerada a seguinte mensagem de erro no log:

* “A inclusão de créditos disponíveis não é permitida quando existir apuração fechada em períodos posteriores”*

__RN06 – Tipo da Contribuição__

Campo obrigatório\.

Deve ser um dos seguintes valores: “PIS” ou “COFINS”\.

Quando não preenchido ou inválido, o registro não será importado e será gerada a seguinte mensagem de erro no log:

*                     “O Tipo da Contribuição deve ser preenchido com “PIS” ou “COFINS”*

 

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN07 – Tipo de Crédito__

Campo obrigatório\.

Deve ser um código da Tabela Código de Tipo de Crédito da Obrigação Acessória SPED Contribuições \(TFIX93\)\.

Quando não preenchido ou inválido, o registro não será importado e será gerada a seguinte mensagem de erro no log:

* “O Tipo de Crédito deve ser preenchido de acordo com a Tabela Código de Tipo de Crédito da Obrigação Acessória SPED Contribuições \(TFIX93\)”*

 

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN08 – Origem do Crédito__

Campo obrigatório\.

Deve ser um dos seguintes valores:

“0” \(= Operações próprias\)

“1” \(= Eventos de incorporação, cisão ou fusão\)

Quando não preenchido ou inválido, o registro não será importado e será gerada a seguinte mensagem de erro no log:

* “A Origem do Crédito deve ser preenchida com “0” \(Operações Próprias\) ou “1” \(Eventos de Incorporação, cisão ou fusão\)”*

 

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN09 – CNPJ__

A validação deste campo depende do campo Origem do Crédito, da seguinte forma:

__Se campo “08\-Origem do Crédito” = “0”:__

Neste caso, este campo *não* deve ser preenchido\. Caso contrário, o registro não será importado e será gerada a seguinte mensagem de erro no log:

* “O campo CNPJ só deve ser informado quando a origem do crédito for = “1” \(Eventos de Incorporação, cisão ou fusão\)”*

__Se campo “08\-Origem do Crédito” = “1”:__

Neste caso, e campo é de preenchimento obrigatório, e deve ser um CNPJ válido\. Caso contrário, o registro não será importado e será gerada a seguinte mensagem de erro no log:

* “CNPJ não preenchido ou inválido\. O preenchimento deste campo é obrigatório quando a origem do crédito for = “1” \(Eventos de Incorporação, cisão ou fusão\)”*

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN10 – Valor Crédito__

Campo obrigatório\.

Deve ser um valor > zeros\. Caso contrário, o registro não será importado e será gerada a seguinte mensagem de erro no log: * “O Valor do Crédito deve ser preenchido com um valor maior que zero”*

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN11 – Valor Crédito \- Extemporâneo__

Campo *não* obrigatório\.

Quando preenchido, deve ser um valor > zeros\. Caso contrário, o registro não será importado e será gerada a seguinte mensagem de erro no log: * “O Valor Crédito \- Extemporâneo deve ser preenchido com um valor maior que zero”*

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN12 – Valor Crédito \- Desconto__

Campo *não* obrigatório\.

Quando preenchido, deve ser um valor > zeros\. Caso contrário, o registro não será importado e será gerada a seguinte mensagem de erro no log: * “O Valor Crédito \- Desconto deve ser preenchido com um valor maior que zero”*

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN13 – Valor Crédito \- Ressarcimento__

Campo *não* obrigatório\.

Quando preenchido, deve ser um valor > zeros\. Caso contrário, o registro não será importado e será gerada a seguinte mensagem de erro no log: * “O Valor Crédito \- Ressarcimento deve ser preenchido com um valor maior que zero”*

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN14 – Valor Crédito \- Compensação__

Campo *não* obrigatório\.

Quando preenchido, deve ser um valor > zeros\. Caso contrário, o registro não será importado e será gerada a seguinte mensagem de erro no log: * “O Valor Crédito \- Compensação deve ser preenchido com um valor maior que zero”*

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN15 – Valor Crédito \- Transferência__

Campo *não* obrigatório\.

Quando preenchido, deve ser um valor > zeros\. Caso contrário, o registro não será importado e será gerada a seguinte mensagem de erro no log: * “O Valor Crédito \- Transferência deve ser preenchido com um valor maior que zero”*

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN16 – Valor Crédito \- Outros__

Campo *não* obrigatório\.

Quando preenchido, deve ser um valor > zeros\. Caso contrário, o registro não será importado e será gerada a seguinte mensagem de erro no log: * “O Valor Crédito \- Outros deve ser preenchido com um valor maior que zero”*

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN17 – Gravação dos Dados na Tabela da Apuração e Tabela dos Créditos __

Antes de gravar os dados do crédito, será verificado se já existe registro da apuração para a Empresa, Estabelecimento e Período, com o código do tipo do livro = “__SLI__”\. 

\- COD\_EMPRESA = Campo “01\-Código da Empresa” da SAFX274

\- COD\_ESTAB = Campo “02\-Código do Estabelecimento” da SAFX274

\- COD\_TIPO\_LIVRO = “__SLI__”

\- DAT\_APUR\_INI = Campo “04\-Data Inicial do Período” da SAFX274

\- DAT\_APUR\_FIM = Campo “05\-Data Final do Período” da SAFX274

\- COD\_SCP = Campo “03\-Código da SCP” da SAFX274

Caso já exista, será gravado \(incluído/alterado\), *apenas* o registro do crédito \(EPC\_APUR\_CRED\_DISP\)\.

Caso *não* exista, será gravado em primeiro lugar o registro da apuração \(EPC\_APURACAO\), e depois o registro do crédito \(EPC\_APUR\_CRED\_DISP\)\.

A gravação dos dados segue as regras descritas a seguir:

__Tabela da apuração \(EPC\_APURACAO\):__

ID\_REG

Identificador gerado pelo sistema

COD\_EMPRESA

Campo “01\-Código da Empresa” da SAFX274

COD\_ESTAB

Campo “02\-Código do Estabelecimento” da SAFX274

COD\_TIPO\_LIVRO

Este campo é gravado sempre com “__SLI__”

*\(“SLI” \- Apuração incluída manualmente pela manutenção dos Créditos Disponíveis, ou importação da SAFX274, referentes a períodos anteriores ao da escrituração digital realizada no módulo EFD\-Contribuições\)*

DAT\_APUR\_INI

Campo “04\-Data Inicial do Período” da SAFX274

DAT\_APUR\_FIM

Campo “05\-Data Final do Período” da SAFX274

COD\_LAYOUT

O código do layout depende da data da apuração, da seguinte forma:

   \- Período = Junho/2012 ou anterior 🡪 “EPC100”

   \- Período = Julho/2012 a Dez/2018 🡪 “EPC201”

   \- Período = Jan/2019 ou posterior 🡪 “EPC310”

 

*\(conforme regra da tela de geração dos registros\) *

IND\_SITUACAO\_APUR

= “1” 

IND\_VALID\_APUR

*\(esta coluna não será preenchida\)*

DSC\_OBS

Este campo será gravado sempre com o seguinte conteúdo:

“Apuração incluída via importação da SAFX274 – Tabela dos Créditos Disponíveis\. Objetivo: inclusão dos créditos de períodos anteriores às escriturações digitais realizadas no módulo EFD\-Contribuições”

DAT\_REALIZACAO

Este campo é gravado com a mesma data do campo DAT\_APUR\_INI

COD\_PERFIL

*\(esta coluna não será preenchida\)*

COD\_SCP

Campo “03\- Código da SCP” da SAFX274

Quando o Código da SCP *não* for informado na SAFX274, este campo não será preenchido\.

__Tabela dos créditos disponíveis \(EPC\_APUR\_CRED\_DISP\):__

ID\_REG\_CRED\_DISP

Identificador gerado pelo sistema

ID\_REG

ID referente à apuração \(EPC\_APURACAO\) a qual o crédito se refere\.

COD\_PIS\_COFINS

Campo “06\-Tipo da Contribuição” da SAFX274

COD\_CRED

Campo “07\-Tipo de Crédito” da SAFX274

IND\_CRED\_ORI

Campo “08\-Origem do Crédito” da SAFX274

CNPJ\_SUC

Campo “09\-CNPJ” da SAFX274

VLR\_CRED\_APUR

Campo “10\-Valor Crédito” da SAFX274

VLR\_CRED\_APUR\_EXTEMP

Campo “11\-Valor Crédito \- Extemporâneo” da SAFX274

VLR\_CRED\_UTIL\_DESC

Campo “12\-Valor Crédito \- Desconto” da SAFX274

VLR\_CRED\_UTIL\_PER

Campo “13\-Valor Crédito \- Ressarcimento” da SAFX274

VLR\_CRED\_UTIL\_DCOMP

Campo “14\-Valor Crédito \- Compensação” da SAFX274

VLR\_CRED\_UTIL\_TRANS

Campo “15\-Valor Crédito \- Transferência” da SAFX274

VLR\_CRED\_UTIL\_OUT

Campo “16\-Valor Crédito \- Outros” da SAFX274

VLR\_CRED\_DISP

Este campo é o resultado da totalização dos seguintes campos:

VLR\_CRED\_APUR \+ VLR\_CRED\_APUR\_EXTEMP – 

\(VLR\_CRED\_UTIL\_DESC \+ VLR\_CRED\_UTIL\_PER \+

VLR\_CRED\_UTIL\_DCOMP \+ VLR\_CRED\_UTIL\_TRANS \+

VLR\_CRED\_UTIL\_OUT\)

Quando o resultado obtido for um valor negativo, o registro não será importado e será gerada a seguinte mensagem de erro no log: * “O valor total do crédito disponível não pode ser negativo \(total dos créditos – créditos utilizados\)”*

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

IND\_GRAVACAO

= “1” \(registro importado\)

PER\_APU\_CRED

Este campo é preenchido com brancos \(‘bbbbbbb’\) 

= = = = =


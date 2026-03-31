# MTZ-Job-Servidor-Importacao-SAFX540

- **Fonte:** MTZ-Job-Servidor-Importacao-SAFX540.docx
- **Modificado:** 2024-10-08
- **Tamanho:** 42 KB

---

# Módulo Job Servidor 

#  Importação SAFX540

#  \(Tabela das Retenções Disponíveis da EFD – Contribuições\) 

__Localização__: Menu Básicos, Módulo: Job Servidor, item Importação 🡪 Execução

##                                            Documento de Requisito

__Doc__

__Alteração__

__Data__

__Resp__

MFS\-684620

Criação da SAFX540 p/carga das retenções disponíveis da EFD – Contribuições

18/09/2024

Alessandra Navatta

__RN00 – Regras Gerais__

A tabela SAFX540 foi criada pela MFS\-684620 com objetivo de permitir a carga das retenções disponíveis do módulo EFD – Contribuições\. A tabela das retenções disponíveis já existe, e sua manutenção é feita nos menus descritos a seguir:

DW

Obrigações 🡪 Manutenção 🡪 Controle das Retenções na Fonte – PIS/PASEP🡪 Retenções Disponíveis

Obrigações 🡪 Manutenção 🡪 Controle das Retenções na Fonte – COFINS 🡪 Retenções Disponíveis

DW e TAXONE

Obrigações SCP 🡪 Manutenção 🡪 Controle das Retenções na Fonte – PIS/PASEP 🡪 Retenções Disponíveis

Obrigações SCP 🡪 Manutenção 🡪 Controle das Retenções na Fonte – COFINS🡪 Retenções Disponíveis

TAXONE 

__Obrigações __🡪 Manutenção 🡪 Apuração Geral PIS/COFINS

Tabelas definitivas que receberão os dados da nova SAFX: 

EPC\_APUR\_RET\_DISP

Tabela das retenções

EPC\_APURACAO

Tabela da apuração

A seguir serão descritas as regras de validação campo a campo, e as regras da gravação dos dados nas duas tabelas \(__RN14\-Gravação dos Dados na Tabela da Apuração e Tabela das Retenções__\)\.

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

 \(ex: código 93209 da CAT\_ERRO\)

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN03 – Data Inicial do Período da Apuração\)__

__RN04 – Data Final do Período da Apuração__

As duas datas são de preenchimento obrigatório\.

Devem ser datas válidas, e a data final deve ser > data inicial\.

Caso estas condições não sejam atendidas, o registro não será importado e serão geradas as seguintes mensagens de erro no log, conforme a situação:

*“O Campo de Data de Validade com formato inválido”*

\(ex: código 90209 da CAT\_ERRO\)

*                                     “Data Inicial do Período não preenchida ou inválida” *

                                              \(ex: código 92970 da CAT\_ERRO\)

*                                     “Data Final do Período não preenchida ou inválida”*

*                                           *  \(ex: código 92971 da CAT\_ERRO\)

*                  “A Data Final de Apuração não pode ser menor que a Data Inicial de Apuração” *

                                              \(ex: código 90526 da CAT\_ERRO\)

__Crítica da existência da Apuração:__

 

A importação de retenções será permitida apenas para usuários que estão implantando o módulo EFD\-Contribuições, ou migrando de outros sistemas \(GF,  Smart, por exemplo\)\. Por isso, serão feitas algumas validações, e em alguns casos, a importação será rejeitada\.

Observação sobre a coluna COD\_TIPO\_LIVRO da EPC\_APURACAO:

\(código de controle interno do módulo\) 

COD\_TIPO\_LIVRO = “__SLI__” = Apuração incluída manualmente pelas telas de manutenção dos 

Retenção Disponíveis, ou via importação \(SAFX540\), referentes a períodos anteriores da escrituração digital realizada no modulo EFD\-Contribuições;

COD\_TIPO\_LIVRO = “__EPC__” = Apuração gerada pelo módulo EFD\-Contribuições;

O módulo EFD\-Contribuições permite a inclusão de uma retenção disponível mesmo quando a apuração do período não existe\. Neste caso, além de gravar o registro da retenção na tabela EPC\_APUR\_RET\_DISP, é gravado também um registro da apuração do período na tabela EPC\_APURACAO\. Neste cenário, a apuração criada não será apresentada na tela da Apuração apenas estará disponível na tabela EPC\_APURACAO, com o campo COD\_TIPO\_LIVRO =“SLI”\. As retenções só estarão disponíveis e poderão ser utilizadas, em apurações criadas pelo módulo EFD\-Contribuições \(COD\_TIPO\_LIVRO = “EPC”\)

Atenção\! Não será impedida a inserção das retenções, quando existir apuração na base\.

__RN05 – Tipo da Contribuição__

Campo obrigatório\.

Deve ser um dos seguintes valores: “PIS” ou “COFINS”\.

Quando não preenchido ou inválido, o registro não será importado e será gerada a seguinte mensagem de erro no log:

*                     “O Tipo da Contribuição deve ser preenchido com “PIS” ou “COFINS”*

           			     \(ex: código 93212 da CAT\_ERRO\)

 

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN06 – Indicador da Natureza de Retenção na Fonte__

Campo obrigatório\.

Informar o Indicador de Natureza da Retenção na Fonte de acordo com o Manual de leiaute da EFD\-PIS/COFINS: Lista de valores Válidos:

01 \- Retenção por Órgãos, Autarquias e Fundações Federais;

02 \- Retenção por outras Entidades da Administração Pública Federal;

03 \- Retenção por Pessoas Jurídicas de Direito Privado;

04 \- Recolhimento por Sociedade Cooperativa;

05 \- Retenção por Fabricante de Máquinas e Veículos; 

99 \- Outras Retenções

Quando não preenchido ou inválido, o registro não será importado e será gerada a seguinte mensagem de erro no log:

* “Indicador de Natureza da Retenção, deve ser preenchido com um valor válido\. Valores Válidos: 01, 02, 03, 04, 05 ou 99\.”*

 				\(ex: código 93721 da CAT\_ERRO\)

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN07 – Indicador da Natureza de Receita__

Campo obrigatório\.

Deve ser um dos seguintes valores:

“0” \(= Receita não Cumulativa\)

“1” \(= Receita Cumulativa\)

Quando não preenchido ou inválido, o registro não será importado e será gerada a seguinte mensagem de erro no log:

* “O indicador da Natureza de Receita deve ser preenchido com “0” \(Receita não Cumulativa\) ou “1” \(Receita Cumulativa\)”*

  				\(ex: código 93722 da CAT\_ERRO\)

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.”\.

__RN08 – Indicador da Condição da Pessoa Jurídica Declarante__

Campo obrigatório\.

Deve ser um dos seguintes valores:

“0” \(= Beneficiária da Retenção/Recolhimento\)

“1” \(= Responsável pela Retenção/Recolhimento\)

Quando não preenchido ou inválido, o registro não será importado e será gerada a seguinte mensagem de erro no log:

* “O indicador da Condição da Pessoa Jurídica Declarante deve ser preenchido com “0” \(Beneficiária da Retenção/Recolhimento\) ou “1” \(Responsável pela Retenção/Recolhimento\)”*

    \(ex: código 92155 da CAT\_ERRO\)

 

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN09 – Código da SCP__

Campo *não* obrigatório\.

Quando preenchido, deve ser um código da Tabela de Cadastro da SCP \(SAFX2057\)\. Caso contrário, o registro não será importado e será gerada a seguinte mensagem de erro no log:

*                                             “Código da SCP não cadastrado”*

                                            \(ex: código 92551 da CAT\_ERRO\)

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN10 – Valor da Retenção Apurado__

Campo obrigatório\.

Deve ser um valor > zeros\. Caso contrário, o registro não será importado e será gerada a seguinte mensagem de erro no log: * “O Valor da Retenção Apurado deve ser preenchido com um valor maior que zero”*

  				\(ex: código 93723 da CAT\_ERRO\)

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN11 – Valor Total da Retenção Utilizado para a Dedução na Contribuição__

Campo não obrigatório\.

Quando preenchido, deve ser um valor igual ou maior que zero\. Caso contrário, o registro não será importado e será gerada a seguinte mensagem de erro no log: *“O Valor Total da Retenção Utilizado para a Dedução na Contribuição deve ser preenchido com um valor igual ou maior que zero”*

  				\(ex: código 93724 da CAT\_ERRO\)

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN12 – Valor Total da Retenção Utilizado por Pedido de Restituição__

Campo não obrigatório\.

Quando preenchido, deve ser um valor *igual ou maior que *zero\. Caso contrário, o registro não será importado e será gerada a seguinte mensagem de erro no log:* “O Valor Total da Retenção Utilizado por Pedido de Restituição deve ser preenchido com um valor igual ou maior que zero”*

  				\(ex: código 93725 da CAT\_ERRO\)

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN13 – Valor Total da Retenção Utilizado por Declaração de Compensação__

Campo não obrigatório\.

Quando preenchido, deve ser um valor *igual ou maior que *zero\. Caso contrário, o registro não será importado e será gerada a seguinte mensagem de erro no log: *“O Valor Total da Retenção Utilizado por Declaração de Compensação deve ser preenchido com um valor igual ou maior que zero”*

  				\(ex: código 93726 da CAT\_ERRO\)

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

__RN14 – Valor da Retenção Disponível para ser Utilizado__

Campo obrigatório

Se o valor informado no campo, não for igual ao resultado do \(VLR\_RET\_APUR – VLR\_RET\_UTIL\_DED – VLR\_RET\_UTIL\_PER – VLR\_RET\_UTIL\_DCOMP\), o registro não será importado e será gerada a seguinte mensagem de erro no log*: ”A Retenção Disponível para ser Utilizada deve ser o resultado da: Retenção Apurada – Total Retenção \(Dedução\) – Total Retenção \(Pedido de Restituição\) \- Total Retenção \(Declaração de Compensação\)”*

  				\(ex: código 93727 da CAT\_ERRO\)

__RN15 – Gravação dos Dados na Tabela da Apuração e Tabela das Retenções__

Antes de gravar os dados do retenção, será verificado se já existe registro da apuração para a Empresa, Estabelecimento e Período, com o código do tipo do livro = “__SLI__”\. 

\- COD\_EMPRESA = Campo “01\-Código da Empresa” da SAFX540

\- COD\_ESTAB = Campo “02\-Código do Estabelecimento” da SAFX540

\- COD\_TIPO\_LIVRO = “__SLI__”

\- DAT\_APUR\_INI = Campo “04\-Data Inicial do Período” da SAFX540

\- DAT\_APUR\_FIM = Campo “05\-Data Final do Período” da SAFX540

\- COD\_SCP = Campo “03\-Código da SCP” da SAFX540

Caso já exista, será gravado \(incluído/alterado\), *apenas* o registro do retenção \(EPC\_APUR\_RET\_DISP\)\.

Caso *não* exista, será gravado em primeiro lugar o registro da apuração \(EPC\_APURACAO\), e depois o registro da retenção \(EPC\_APUR\_RET\_DISP\)\.

A gravação dos dados segue as regras descritas a seguir:

__Tabela da apuração \(EPC\_APURACAO\):__

ID\_REG

Identificador gerado pelo sistema

COD\_EMPRESA

Campo “01\-Código da Empresa” da SAFX540

COD\_ESTAB

Campo “02\-Código do Estabelecimento” da SAFX540

COD\_TIPO\_LIVRO

Este campo é gravado sempre com “__SLI__”

*\(“SLI” \- Apuração incluída manualmente pela manutenção das Retenções Disponíveis, ou importação da SAFX540, referentes a períodos anteriores ao da escrituração digital realizada no módulo EFD\-Contribuições\)*

DAT\_APUR\_INI

Campo “04\-Data Inicial do Período” da SAFX540

DAT\_APUR\_FIM

Campo “05\-Data Final do Período” da SAFX540

COD\_LAYOUT

O código do layout depende da data da apuração, da seguinte forma:

   \- Período = Junho/2012 ou anterior 🡪 “EPC100”

   \- Período = Julho/2012 a Dez/2018 🡪 “EPC201”

   \- Período = Jan/2019 a Dez/2019 🡪 “EPC310”

    \- Período = Jan2020 ou posterior 🡪 “EPC320”

 *\(conforme regra da tela de geração dos registros\) *

IND\_SITUACAO\_APUR

= “1” 

IND\_VALID\_APUR

*\(esta coluna não será preenchida\)*

DSC\_OBS

Este campo será gravado sempre com o seguinte conteúdo:

“Apuração incluída via importação da SAFX540 – Tabela das Retenções Disponíveis\. Objetivo: inclusão das retenções de períodos anteriores às escriturações digitais realizadas no módulo EFD\-Contribuições”

DAT\_REALIZACAO

Este campo é gravado com a mesma data do campo DAT\_APUR\_INI

COD\_PERFIL

*\(esta coluna não será preenchida\)*

COD\_SCP

Campo “03\- Código da SCP” da SAFX540

Quando o Código da SCP *não* for informado na SAFX540, este campo não será preenchido\.

__Tabela das retenções disponíveis \(EPC\_APUR\_RET\_DISP\):__

ID\_REG\_RET\_DISP

Identificador gerado pelo sistema

ID\_REG

ID referente à apuração \(EPC\_APURACAO\) a qual a retenção se refere\.

COD\_PIS\_COFINS

Campo “05 \- Tipo da Contribuição” da SAFX540

COD\_RET\_FONTE

Campo “06\- Indicador da Natureza de Retenção na Fonte” da SAFX540

IND\_NAT\_REC

Campo “07\- Indicador da Natureza de Receita” da SAFX540

IND\_COND\_PJ\_DECL

Campo “08\- Indicador da Condição da Pessoa Jurídica Declarante” da SAFX540

VLR\_RET\_APUR

Campo “10 \- Valor da Retenção Apurado” da SAFX540

VLR\_RET\_UTIL\_DED

Campo “11\-Valor Retenção \- Dedução” da SAFX540

VLR\_RET\_UTIL\_PER

Campo “12\-Valor Retenção – Pedido de Restituição” da SAFX540

VLR\_RET\_UTIL\_DCOMP

Campo “13\-Valor Retenção – Compensação” da SAFX540

VLR\_RET\_DISP

Campo “14 – VLR\_RET\_DISP” da SAFX540\.

Este campo é o resultado da subtração dos seguintes campos:

VLR\_RET\_APUR – VLR\_RET\_UTIL\_DED – VLR\_RET\_UTIL\_PER – VLR\_RET\_UTIL\_DCOMP

Quando o resultado obtido for um valor negativo, o registro não será importado e será gerada a seguinte mensagem de erro no log: * “O valor total da retenção disponível não pode ser negativo \(total das retenções – retenções utilizadas\)”*

\(ex: código 93728 da CAT\_ERRO\)

O log deve exibir as informações chave da apuração para a conferência do usuário \(Empresa, Estabelecimento, Data Inicial, Data Final e Código SCP”\.

IND\_GRAVACAO

= “1” \(registro importado\)


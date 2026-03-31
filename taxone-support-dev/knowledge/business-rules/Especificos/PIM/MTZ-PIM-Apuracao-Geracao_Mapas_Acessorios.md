# MTZ-PIM-Apuracao-Geracao_Mapas_Acessorios

- **Fonte:** MTZ-PIM-Apuracao-Geracao_Mapas_Acessorios.docx
- **Modificado:** 2022-07-06
- **Tamanho:** 108 KB

---

THOMSON REUTERS

PIM \- Gestão do Controle de Incentivos Fiscais do Pólo Industrial de Manaus

Geração dos Mapas Acessórios

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4785

Julyana Perrucini

Este documento tem como objetivo alterar o cálculo do Fundo de Fomento às Micro e Pequenas Empresas – FMPES por Crédito Estímulo\.

OS4784

Julyana Perrucini

Este documento tem como objetivo alterar o cálculo em favor da Universidade do Estado do Amazonas \- UEA por Crédito Estímulo\.

MFS6111

Andréa Rocha

Alteração do cálculo do F\.T\.I\. para desconsiderar o valor das notas fiscais de devolução de vendas\.

MFS6153

Andréa Rocha

Alteração do cálculo do U\.E\.A\. para desconsiderar o valor das notas fiscais de devolução de vendas\.

MFS84429

Liliane Assaf

Alteração nos cálculos dos componentes 21 e 19 para gravar a Tabela de Itens de Nota Fiscal para Relatório Analítico dos Mapas \(ICT\_AM\_AP\_IT\_NF\)

MFS84451

Liliane Assaf

RN04: Geração dos Débitos Especiais a partir do valor da contribuição calculado para os componentes: 19 – F\.T\.I, 20 – F\.M\.P\.E\.S, 21 – U\.E\.A

MFS85986

Liliane Assaf

RN05: Geração dos Valores Declaratórios a partir dos valores calculados para os componentes: 19 – F\.T\.I, 20 – F\.M\.P\.E\.S, 21 – U\.E\.A

RN01, RN02, RN03: Alteração na geração dos componentes 19 – F\.T\.I, 20 – F\.M\.P\.E\.S, 21 – U\.E\.A para gravar o valor considerado com base de cálculo na tabela de Mapas Acessórios \(ICT\_AM\_AP\_E\_S\)

MFS85991

Liliane Assaf

RN06: Geração das Guias de Recolhimento a partir dos valores calculados para os componentes: 19 – F\.T\.I, 20 – F\.M\.P\.E\.S, 21 – U\.E\.A

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

<Descrição detalhada da regra de negócio>

<OS>\.

RN01

__Cálculo do Componente 20\-F\.M\.P\.E\.S__

__Procedure SAFF\_AP\_ICMS\_AM\_FM__

__\[ALTERADA – OS4785\]__

Aplicar a taxa parametrizada no campo Taxa F\.M\.P\.E\.S da tela Parâmetros de Cálculo por Linha, localizada no item de menu Cadastros >> Linhas de Incentivos no __valor de Crédito Estímulo__ do Relatório de Cálculo do Crédito Estímulo, localizado no item de menu Relatórios >> Créditos \(Operações de Entradas\), no qual é calculado através da rotina Cálculo dos Créditos \(Entradas\) >> Crédito Estímulo, localizada no item de menu Apuração, armazenado no campo VLR\_CRED\_ESTIMULO da tabela ICT\_AM\_REL\_IES\_EST\.

__MFS85986__: Gravação da Base de Cálculo na Tabela de Geração dos Mapas Acessórios \(ICT\_AM\_AP\_E\_S\):

O resultado do cálculo é gravado na tabela de geração dos mapas acessórios \(ICT\_AM\_AP\_E\_S\):

     Cálculo do F\.M\.P\.E\.S = valor de crédito Estímulo \*  \(taxa de F\.M\.P\.E\.S / 100\)

     Base de Cálculo do F\.M\.P\.E\.S = valor de crédito Estímulo

__*Observações:*__

\- Para calcular o componente 20\-FMPES, é necessário recuperar a apuração dos saldos \(tabela ICT\_AM\_SLD\_APUR\) para identificar os valores por código de linha do produto que estão parametrizados\. Após isso recuperar a taxa do FMPES por Inscrição Estadual e Código de Linha, e aplicá\-lo sobre o valor do Crédito Estímulo\.

OS4785

RN02

__Cálculo do Componente 21\-Contribuicao de U\.E\.A__

__Procedure SAF\_AP\_ICMS\_AM\_UE__

__\[ALTERADA – OS4784\]__

__ITEM 001 \(U\.E\.A s/ Crédito Estímulo\)__

Aplicar a taxa parametrizada no campo Taxa U\.E\.A da tela Parâmetros de Cálculo por Linha, localizada no item de menu Cadastros >> Linhas de Incentivos no __valor de Crédito Estímulo__ do Relatório de Cálculo do Crédito Estímulo, localizado no item de menu Relatórios >> Créditos \(Operações de Entradas\), no qual é calculado através da rotina Cálculo dos Créditos \(Entradas\) >> Crédito Estímulo, localizada no item de menu Apuração, armazenado no campo VLR\_CRED\_ESTIMULO da tabela ICT\_AM\_REL\_IES\_EST\.

__MFS85986__: Gravação da Base de Cálculo na Tabela de Geração dos Mapas Acessórios \(ICT\_AM\_AP\_E\_S\):

O resultado do cálculo é gravado na tabela de geração dos mapas acessórios \(ICT\_AM\_AP\_E\_S\):

     Cálculo do U\.E\.A = valor de crédito Estímulo \*  \(taxa de U\.E\.A / 100\)

     Base de Cálculo do U\.E\.A = valor de crédito Estímulo

__*Observações:*__

\- Para calcular o componente 21\-__ __Contribuicao de U\.E\.A, é necessário recuperar a apuração dos saldos \(tabela ICT\_AM\_SLD\_APUR\) para identificar os valores por código de linha do produto que estão parametrizados\. Após isso recuperar a taxa do U\.E\.A por Inscrição Estadual e Código de Linha, e aplicá\-lo sobre o valor do Crédito Estímulo\.

\[MFS6153\]

__Item 002 \( U\.E\.A\. s/ faturamento\)__

O cálculo do U\.E\.A\. é feito baseado nas notas fiscais \(SAFX07 e SAFX08\), conforme regras de recuperação abaixo:

\- Notas fiscais que pertençam ao estabelecimento e inscrição estadual selecionados em tela,

\- Somente Notas fiscais de mercadoria,

\- Notas fiscais de saída \(MOVTO\_E\_S = ‘9’\),

\- Notas fiscais não canceladas,

\- Classificação de mercadoria igual a ‘1’ e’ 3’,

\- Notas fiscais que não sejam de transferência,

\- Notas parametrizadas para CFOP ou CFOP/Natureza para o componente = 21, estrutura = 01 e item  = 002 \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\),

\- Somente os produtos que fazem parte de uma linha de produto \(Cadastros > Linhas de incentivos > Linhas de produtos incentivados\), e recuperar o código de linha do produto

Para fazer o cálculo do U\.E\.A\. deve\-se recuperar a taxa de incentivo do U\.E\.A\. s/ faturamento da tela de Parâmetros de Cálculo por Linha \(Cadastros > Linhas de incentivos > Parâmetros de cálculos por linha\) para a empresa, o estabelecimento, a inscrição estadual, o código da linha produto de cada produto da nota fiscal e a máxima data de validade que seja menor ou igual à data fim de geração\.

__MFS85986__: Gravação da Base de Cálculo na Tabela de Geração dos Mapas Acessórios \(ICT\_AM\_AP\_E\_S\):

O cálculo do U\.E\.A\. é feito para cada item de nota recuperado e é gravado na tabela de geração dos mapas acessórios \(ICT\_AM\_AP\_E\_S\):

     Cálculo do U\.E\.A\. Faturamento = valor contábil do item \(campo 64 da SAFX08\) \*  \(taxa de U\.E\.A\. / 100\)

     Base de Cálculo do U\.E\.A = valor contábil do item

Deste valor calculado para o U\.E\.A\. deve\-se deduzir o valor das notas fiscais de devolução de vendas, conforme regras de recuperação abaixo:

\- Notas fiscais que pertençam ao estabelecimento e inscrição estadual selecionados em tela,

\- Somente Notas fiscais de mercadoria,

\- Notas fiscais de entrada \(MOVTO\_E\_S <> ‘9’\),

\- Notas fiscais não canceladas,

\- Notas fiscais de devolução,

\- Classificação de mercadoria igual a ‘1’ e ‘3’,

\- Notas fiscais que não sejam de transferência,

\- Notas parametrizadas para CFOP ou CFOP/Natureza de devolução de vendas para o componente = 21, estrutura = 01 e item  = 002 \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza \- Devolução de Vendas\),

\- Somente os produtos que fazem parte de uma linha de produto \(Cadastros > Linhas de incentivos > Linhas de produtos incentivados\), e recuperar o código de linha do produto\.

Para fazer o cálculo do U\.E\.A\. deve\-se recuperar a taxa de incentivo do U\.E\.A\. s/ faturamento da tela de Parâmetros de Cálculo por Linha \(Cadastros > Linhas de incentivos > Parâmetros de cálculos por linha\) para a empresa, o estabelecimento, a inscrição estadual, o código da linha produto de cada produto da nota fiscal e a máxima data de validade que seja menor ou igual à data fim de geração\.

__MFS85986__: Gravação da Base de Cálculo na Tabela de Geração dos Mapas Acessórios \(ICT\_AM\_AP\_E\_S\):

O cálculo do U\.E\.A\. de devolução é feito para cada item de nota recuperado e deve ser subtraído do valor gravado na tabela de geração dos mapas acessórios \(ICT\_AM\_AP\_E\_S\):

     Cálculo do U\.E\.A\. devolução = valor contábil do item \(campo 64 da SAFX08\) \*  \(taxa de U\.E\.A\.\. / 100\) 

     Base de Cálculo do U\.E\.A devolução = valor contábil do item

__\[MFS84429\]__

__Gravação da Tabela de Itens de Nota Fiscal para Relatório Analítico dos Mapas__:

Todos os itens de mercadoria que foram considerados para a geração do componente 21, estrutura 01 e __item 002__ devem ser gravados na tabela a seguir, a fim de gerar o Relatório Analítico dos Mapas que demonstra o cálculo da contribuição __U\.E\.A\. s/ faturamento__ item a item da nota fiscal\. 

O Relatório Analítico dos Mapas está disponivel no módulo PIM, menu: Relatórios 🡪 Emissão dos Mapas 🡪 Relatório Analítico dos Mapas\.

Obs: essa tabela não será gravada para o cálculo do U\.E\.A s/ Crédito Estímulo \(componente 21, estrutura 01, item 001\), pois este cálculo não parte da leitura dos documentos fiscais e sim do valor do crédito estímulo já previamente calculado\.

__Tabela ICT\_AM\_AP\_IT\_NF__:

Campo

Regra de Preenchimento

COD\_EMPRESA

Código da empresa de login

COD\_ESTAB

Código do estabelecimento da nota fiscal considerada no cálculo do__ U\.E\.A\. s/ faturamento__

INSC\_ESTADUAL

Inscrição Estadual PIM da nota fiscal \(campo 126 da SAFX07\)

DAT\_APURACAO

Data Fim do Periodo informado na Tela de Geração dos Mapas Acessórios

COD\_LINHA\_PRD

Código da Linha de Incentivo parametrizado para o produto da nota fiscal

COD\_COMP\_APUR

Código do Componente \(21\) parametrizado ao CFOP ou CFOP/Natureza da nota em \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\)

COD\_ESTRUT

Código da Estrutura parametrizado ao CFOP ou CFOP/Natureza da nota em \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\)

COD\_ITEM\_APUR

Código do Item parametrizado ao CFOP ou CFOP/Natureza da nota em \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\)

DATA\_FISCAL

Data Fiscal da nota fiscal

MOVTO\_E\_S

Indicador Movimento Entrada/Saída da nota fiscal \(campo 03 da SAFX07\)

NORM\_DEV

Indicador de Normal ou Devolução da nota fiscal \(campo 04 da SAFX07\)

IDENT\_DOCTO

Identificador do Tipo do Documento da nota fiscal \(referente ao campo 05 da SAFX07\)

IDENT\_FIS\_JUR

Identificador Pessoa Física Jurídica da nota fiscal \(referente ao campo 06, 07 da SAFX07\)

NUM\_DOCFIS

Número do Documento Fiscal \(campo 08 da SAFX07\)

SERIE\_DOCFIS

Série do Documento Fiscal \(campo 09 da SAFX07\)

SUB\_SERIE\_DOCFIS

Subsérie do Documento Fiscal \(campo 10 da SAFX07\)

DISCRI\_ITEM

Preencher com o DISCR\_ITEM da DWT\_ITENS\_MERC

NUM\_ITEM

Número do Item de mercadoria \(campo 18 da SAFX08\)

IDENT\_PRODUTO

Identificador do Produto do item de mercadoria \(referente aos campos 13, 14 da SAFX08\)

IDENT\_CFO

Identificador do CFOP do item de mercadoria \(referente ao campo 22 da SAFX08\)

IDENT\_NATUREZA\_OP

Identificador da Natureza de Operação do item de mercadoria \(referente ao campo 23 da SAFX08\)

VLR\_CONTAB\_ITEM

Valor Contabil do Item de mercadoria \(campo 64 da SAFX08\)

ALIQ\_TRIBUTO\_CMS

Alíquota do Tributo ICMS do item de mercadoria \(campo 42 da SAFX08\)

VLR\_TRIBUTO\_ICMS

Valor do Tributo ICMS do item de mercadoria \(campo 43 da SAFX08\)

VLR\_BASE\_ICMS\_TRIB

Base Tributada ICMS do item de mercadoria \(VLR\_BASE\_ICMS\_1 da DWT\_ITENS\_MERC\)

VLR\_BASE\_ICMS\_ISENT

Base Isenta \+ Reduzida ICMS do item de mercadoria \(VLR\_BASE\_ICMS\_2 \+  VLR\_BASE\_ICMS\_4 da DWT\_ITENS\_MERC\)

VLR\_BASE\_ICMS\_OUTR

Base Outras ICMS do item de mercadoria \(VLR\_BASE\_ICMS\_3 da DWT\_ITENS\_MERC\)\.

Verificar o parâmetro “ICMS Retido/Outras” da Tela de Geração dos Mapas Acessórios\.

Se parâmetro “ICMS Retido/Outras” estiver marcado, então:

  Preencher este campo com Base Outras ICMS \+ Valor do ICMS\-ST\.

Senão

  Preencher este campo com Base Outras ICMS\.  

ALIQ\_TRIBUTO\_ICMSS

Alíquota do Tributo ICMS\-ST do item de mercadoria \(campo 51 da SAFX08\)

VLV\_TRIBUTO\_ICMSS

Valor do Tributo ICMS\-ST do item de mercadoria \(campo 52 da SAFX08\)

VLR\_BASE\_ICMSS

Valor da Base ICMS\-ST do item de mercadoria \(campo 61 da SAFX08\)

VLR\_TAXA

Taxa de incentivo do __U\.E\.A\. s/ faturamento__ que foi recuperada tela de Parâmetros de Cálculo por Linha \(Cadastros > Linhas de incentivos > Parâmetros de cálculos por linha\), para o cálculo do componente 21\.

\- Preencher este campo a Taxa __U\.E\.A\. s/ faturamento__ \(VLR\_TX\_UEA\_FATUR\)

VLR\_CONTRIBUICAO

Preencher com o valor calculado para o __U\.E\.A\. s/ faturamento__

Para o cálculo do compontente 21, estrutura 01 item 002:

\- Valor do “Cálculo do U\.E\.A\. Faturamento”

\- Valor do “Cálculo do U\.E\.A devolução” 🡪 este valor será gravado com sinal negativo

USUARIO

Usuário de login da aplicação

NUM\_PROCESSO

Número do processo da Geração dos Mapas Acessórios

OS4784

MFS6153

RN03

__Cálculo do Componente 19\- F\.T\.I\. __

__Procedure SAF\_AP\_ICMS\_AM\_FT__

__Item 001 \( F\.T\.I\. s/ Importação Matéria\-Prima\)__

O cálculo do F\.T\.I\. é feito baseado nas notas fiscais \(SAFX07 e SAFX08\), conforme regras de recuperação abaixo:

\- Notas fiscais que pertençam ao estabelecimento e inscrição estadual selecionados em tela,

\- Somente Notas fiscais de mercadoria,

\- Notas fiscais de entrada  \(MOVTO\_E\_S <> ‘9’\),

\- Notas fiscais não canceladas,

\- Classificação de mercadoria igual a ‘1’ e’ 3’,

\- Notas fiscais com Indicador de Tipo de Frete \(IND\_TP\_FRETE\) = 2 \-Frete para Conta do Destinatário \(FOB\);

\- Notas parametrizadas para CFOP ou CFOP/Natureza para o componente = 19, estrutura = 01 e item  = 001 \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\),

\- Somente os produtos que fazem parte de uma linha de produto \(Cadastros > Linhas de incentivos > Linhas de produtos incentivados\), e recuperar o código de linha do produto

Para fazer o cálculo do F\.T\.I\. deve\-se recuperar a taxa de incentivo do F\.T\.I\. s/ Imp\. Matéria\-Prima da tela de Parâmetros de Cálculo por Linha \(Cadastros > Linhas de incentivos > Parâmetros de cálculos por linha\) para a empresa, o estabelecimento, a inscrição estadual, o código da linha produto de cada produto da nota fiscal e a máxima data de validade que seja menor ou igual à data fim de geração\.

O cálculo do F\.T\.I\. é feito para cada item de nota recuperado e é gravado na tabela de geração dos mapas acessórios \(ICT\_AM\_AP\_E\_S\) e na tabela de itens de Nota fiscal para Relatório Analítico dos Mapas \(ICT\_AM\_AP\_IT\_NF\)\.

__MFS85986__: Gravação da Base de Cálculo na Tabela de Geração dos Mapas Acessórios \(ICT\_AM\_AP\_E\_S\):

     Cálculo do F\.T\.I\. Imp Matéria\-Prima = valor contábil do item \(campo 64 da SAFX08\) \*  \(taxa de F\.T\.I\. / 100\)

     Base de Cálculo do F\.T\.I  = valor contábil do item

__Item 002 \( F\.T\.I\. s/ faturamento\)__

O cálculo do F\.T\.I\. é feito baseado nas notas fiscais \(SAFX07 e SAFX08\), conforme regras de recuperação abaixo:

\- Notas fiscais que pertençam ao estabelecimento e inscrição estadual selecionados em tela,

\- Somente Notas fiscais de mercadoria,

\- Notas fiscais de saída \(MOVTO\_E\_S = ‘9’\),

\- Notas fiscais não canceladas,

\- Classificação de mercadoria igual a ‘1’ e’ 3’,

\- Notas fiscais que não sejam de transferência,

\- Notas parametrizadas para CFOP ou CFOP/Natureza para o componente = 19, estrutura = 01 e item  = 002 \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\),

\- Somente os produtos que fazem parte de uma linha de produto \(Cadastros > Linhas de incentivos > Linhas de produtos incentivados\), e recuperar o código de linha do produto

Para fazer o cálculo do F\.T\.I\. deve\-se recuperar a taxa de incentivo do F\.T\.I\. s/ faturamento da tela de Parâmetros de Cálculo por Linha \(Cadastros > Linhas de incentivos > Parâmetros de cálculos por linha\) para a empresa, o estabelecimento, a inscrição estadual, o código da linha produto de cada produto da nota fiscal e a máxima data de validade que seja menor ou igual à data fim de geração\.

O cálculo do F\.T\.I\. é feito para cada item de nota recuperado e é gravado na tabela de geração dos mapas acessórios \(ICT\_AM\_AP\_E\_S\) e na tabela de itens de Nota fiscal para Relatório Analítico dos Mapas \(ICT\_AM\_AP\_IT\_NF\):

__MFS85986__: Gravação da Base de Cálculo na Tabela de Geração dos Mapas Acessórios \(ICT\_AM\_AP\_E\_S\):

     Cálculo do F\.T\.I\. Faturamento = valor contábil do item \(campo 64 da SAFX08\) \*  \(taxa de F\.T\.I\. / 100\)

     Base de Cálculo do F\.T\.I  = valor contábil do item

Deste valor calculado para o F\.T\.I\. deve\-se deduzir o valor das notas fiscais de devolução de vendas, conforme regras de recuperação abaixo:

\- Notas fiscais que pertençam ao estabelecimento e inscrição estadual selecionados em tela,

\- Somente Notas fiscais de mercadoria,

\- Notas fiscais de entrada \(MOVTO\_E\_S <> ‘9’\),

\- Notas fiscais não canceladas,

\- Notas fiscais de devolução,

\- Classificação de mercadoria igual a ‘1’ e ‘3’,

\- Notas fiscais que não sejam de transferência,

\- Notas parametrizadas para CFOP ou CFOP/Natureza de devolução de vendas para o componente = 19, estrutura = 01 e item  = 002 \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza \- Devolução de Vendas\),

\- Somente os produtos que fazem parte de uma linha de produto \(Cadastros > Linhas de incentivos > Linhas de produtos incentivados\), e recuperar o código de linha do produto\.

Para fazer o cálculo do F\.T\.I\. deve\-se recuperar a taxa de incentivo do F\.T\.I\. s/ faturamento da tela de Parâmetros de Cálculo por Linha \(Cadastros > Linhas de incentivos > Parâmetros de cálculos por linha\) para a empresa, o estabelecimento, a inscrição estadual, o código da linha produto de cada produto da nota fiscal e a máxima data de validade que seja menor ou igual à data fim de geração\.

__MFS85986__: Gravação da Base de Cálculo na Tabela de Geração dos Mapas Acessórios \(ICT\_AM\_AP\_E\_S\):

O cálculo do F\.T\.I\. de devolução é feito para cada item de nota recuperado e deve ser subtraído do valor gravado na tabela de geração dos mapas acessórios \(ICT\_AM\_AP\_E\_S\):

     Cálculo do F\.T\.I\. devolução = valor contábil do item \(campo 64 da SAFX08\) \*  \(taxa de F\.T\.I\. / 100\)

     Base de Cálculo do F\.T\.I devolução = valor contábil do item

Cada item de nota de devolução também é gravado na tabela de itens de Nota fiscal para Relatório Analítico dos Mapas \(ICT\_AM\_AP\_IT\_NF\)\.

__Item 003 \( F\.T\.I\. \)__

O cálculo do F\.T\.I\. é feito baseado nas notas fiscais \(SAFX07e SAFX08\), conforme regras de recuperação abaixo:

\- Notas fiscais que pertençam ao estabelecimento e inscrição estadual selecionados em tela,

\- Somente Notas fiscais de mercadoria,

\- Notas fiscais de entrada  \(MOVTO\_E\_S <> ‘9’\),

\- Notas fiscais não canceladas,

\- Classificação de mercadoria igual a ‘1’ e’ 3’,

\- Notas parametrizadas para CFOP ou CFOP/Natureza para o componente = 19, estrutura = 01 e item  = 003 \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\),

\- Somente os produtos que fazem parte de uma linha de produto \(Cadastros > Linhas de incentivos > Linhas de produtos incentivados\), e recuperar o código de linha do produto

Para fazer o cálculo do F\.T\.I\. deve\-se recuperar a taxa de incentivo do F\.T\.I\. da tela de Parâmetros de Cálculo por Linha \(Cadastros > Linhas de incentivos > Parâmetros de cálculos por linha\) para a empresa, o estabelecimento, a inscrição estadual, o código da linha produto de cada produto da nota fiscal e a máxima data de validade que seja menor ou igual à data fim de geração\.

O cálculo do F\.T\.I\. é feito para cada item de nota recuperado e é gravado na tabela de geração dos mapas acessórios \(ICT\_AM\_AP\_E\_S\) e na tabela de itens de Nota fiscal para Relatório Analítico dos Mapas \(ICT\_AM\_AP\_IT\_NF\):

__MFS85986__: Gravação da Base de Cálculo na Tabela de Geração dos Mapas Acessórios \(ICT\_AM\_AP\_E\_S\):

     Cálculo do F\.T\.I\. = valor contábil do item \(campo 64 da SAFX08\) \*  \(taxa de F\.T\.I\. / 100\)

     Base de Cálculo do F\.T\.I  = valor contábil do item

__\[MFS84429\]__

__Gravação da Tabela de Itens de Nota Fiscal para Relatório Analítico dos Mapas__:

Todos os itens de mercadoria que foram considerados para a geração do componente 19, estrutura 01 e itens 001, 002, 003 devem ser gravados na tabela a seguir, a fim de gerar o Relatório Analítico dos Mapas que demonstra o cálculo da contribuição F\.T\.I item a item da nota fiscal\. 

O Relatório Analítio dos Mapas está disponivel no módulo PIM, menu: Relatórios 🡪 Emissão dos Mapas 🡪 Relatório Analítico dos Mapas\.

__Tabela ICT\_AM\_AP\_IT\_NF__:

Campo

Regra de Preenchimento

COD\_EMPRESA

Código da empresa de login

COD\_ESTAB

Código do estabelecimento da nota fiscal considerada no cálculo do FTI

INSC\_ESTADUAL

Inscrição Estadual PIM da nota fiscal \(campo 126 da SAFX07\)

DAT\_APURACAO

Data Fim do Periodo informado na Tela de Geração dos Mapas Acessórios

COD\_LINHA\_PRD

Código da Linha de Incentivo parametrizado para o produto da nota fiscal

COD\_COMP\_APUR

Código do Componente \(19\) parametrizado ao CFOP ou CFOP/Natureza da nota em \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\)

COD\_ESTRUT

Código da Estrutura parametrizado ao CFOP ou CFOP/Natureza da nota em \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\)

COD\_ITEM\_APUR

Código do Item parametrizado ao CFOP ou CFOP/Natureza da nota em \(Parâmetros 🡪 Parâmetros dos Mapas 🡪 Itens / Operações 🡪 CFOP ou CFOP/Natureza\)

DATA\_FISCAL

Data Fiscal da nota fiscal

MOVTO\_E\_S

Indicador Movimento Entrada/Saída da nota fiscal \(campo 03 da SAFX07\)

NORM\_DEV

Indicador de Normal ou Devolução da nota fiscal \(campo 04 da SAFX07\)

IDENT\_DOCTO

Identificador do Tipo do Documento da nota fiscal \(referente ao campo 05 da SAFX07\)

IDENT\_FIS\_JUR

Identificador Pessoa Física Jurídica da nota fiscal \(referente ao campo 06, 07 da SAFX07\)

NUM\_DOCFIS

Número do Documento Fiscal \(campo 08 da SAFX07\)

SERIE\_DOCFIS

Série do Documento Fiscal \(campo 09 da SAFX07\)

SUB\_SERIE\_DOCFIS

Subsérie do Documento Fiscal \(campo 10 da SAFX07\)

DISCRI\_ITEM

Preencher com o DISCR\_ITEM da DWT\_ITENS\_MERC

NUM\_ITEM

Número do Item de mercadoria \(campo 18 da SAFX08\)

IDENT\_PRODUTO

Identificador do Produto do item de mercadoria \(referente aos campos 13, 14 da SAFX08\)

IDENT\_CFO

Identificador do CFOP do item de mercadoria \(referente ao campo 22 da SAFX08\)

IDENT\_NATUREZA\_OP

Identificador da Natureza de Operação do item de mercadoria \(referente ao campo 23 da SAFX08\)

VLR\_CONTAB\_ITEM

Valor Contabil do Item de mercadoria \(campo 64 da SAFX08\)

ALIQ\_TRIBUTO\_CMS

Alíquota do Tributo ICMS do item de mercadoria \(campo 42 da SAFX08\)

VLR\_TRIBUTO\_ICMS

Valor do Tributo ICMS do item de mercadoria \(campo 43 da SAFX08\)

VLR\_BASE\_ICMS\_TRIB

Base Tributada ICMS do item de mercadoria \(VLR\_BASE\_ICMS\_1 da DWT\_ITENS\_MERC\)

VLR\_BASE\_ICMS\_ISENT

Base Isenta \+ Reduzida ICMS do item de mercadoria \(VLR\_BASE\_ICMS\_2 \+  VLR\_BASE\_ICMS\_4 da DWT\_ITENS\_MERC\)

VLR\_BASE\_ICMS\_OUTR

Base Outras ICMS do item de mercadoria \(VLR\_BASE\_ICMS\_3 da DWT\_ITENS\_MERC\)

Verificar o parâmetro “ICMS Retido/Outras” da Tela de Geração dos Mapas Acessórios\.

Se parâmetro “ICMS Retido/Outras” estiver marcado, então:

  Preencher este campo com Base Outras ICMS \+ Valor do ICMS\-ST\.

Senão

  Preencher este campo com Base Outras ICMS\.  

ALIQ\_TRIBUTO\_ICMSS

Alíquota do Tributo ICMS\-ST do item de mercadoria \(campo 51 da SAFX08\)

VLV\_TRIBUTO\_ICMSS

Valor do Tributo ICMS\-ST do item de mercadoria \(campo 52 da SAFX08\)

VLR\_BASE\_ICMSS

Valor da Base ICMS\-ST do item de mercadoria \(campo 61 da SAFX08\)

VLR\_TAXA

Taxa de incentivo do F\.T\.I\. que foi recuperada tela de Parâmetros de Cálculo por Linha \(Cadastros > Linhas de incentivos > Parâmetros de cálculos por linha\), para o cálculo do componente 19\.

Para o cálculo do compontente 19, estrutura 01 item 001:

\- Preencher este campo com a Taxa F\.T\.I\. s/ Imp\. Matéria\-Prima \(VLR\_TX\_FTI\_IMP\_MP\)

Para o cálculo do compontente 19, estrutura 01 item 002:

\- Preencher este campo com a Taxa F\.T\.I\. s/ faturamento \(VLR\_TAXA\_FTI\_FATUR\)

Para o cálculo do compontente 19, estrutura 01 item 003:

\- Preencher este campo a Taxa F\.T\.I a com \(VLR\_TAXA\_FTI\)

VLR\_CONTRIBUICAO

Preencher com o valor calculado para o F\.T\.I\.

Para o cálculo do compontente 19, estrutura 01 item 001:

\- Valor do “Cálculo do F\.T\.I\. Imp Matéria\-Prima”

Para o cálculo do compontente 19, estrutura 01 item 002:

\- Valor do “Cálculo do F\.T\.I\. Faturamento”

\- Valor do “Cálculo do F\.T\.I\. devolução” 🡪 este valor será gravado com sinal negativo

Para o cálculo do compontente 19, estrutura 01 item 003:

\- Valor do “Cálculo do F\.T\.I\.”

USUARIO

Usuário de login da aplicação

NUM\_PROCESSO

Número do processo da Geração dos Mapas Acessórios

MFS6111

RN04

__Geração Automática dos Débitos Especiais__

Após o cálculo de todos os componentes, realizar a geração dos débitos especiais aplicada aos componentes 19 – F\.T\.I, 20 – F\.M\.P\.E\.S e 21 – U\.E\.A\.

Esta geração consiste em recuperar o valor calculado dos Mapas Acessórios para cada Linha de Incentivo/Componente/Estrutura/Item e gerar um registro de Débito Especial com o valor calculado mais o código de ajuste e descrição definidos na Parametrização para Geração Automática dos Débitos Especiais \(Sped Fiscal – E111/1921\)\.

O valor calculado dos Mapas Acessórios – tabela  ICT\_AM\_AP\_E\_S pode ser conferido através do Relatório Sintético dos Mapas \(menu Relatórios>> Emissão dos Mapas >> Relatório Sintético dos Mapas\)\.

A Parametrização para Geração Automática dos Débitos Especiais \(Sped Fiscal – E111/1921\) – tabela ICT\_AM\_PAR\_GER\_DEB\_ESP está disponível no menu Parâmetros >> Parâmetros dos Mapas >> Parâmetros para Geração Automática >> Débitos Especiais \(Sped Fiscal – E111/1921\) e contempla apenas os componentes 19, 20 e 21\.

 

__Procedimentos para Geração:__

A geração dos Débitos Especiais só será executada se pelo menos um dos componentes selecionados na tela de geração possuir: 

     \- Parametrização para Geração Automática dos Débitos Especiais \(Sped Fiscal – E111/1921\) – tabela 

__       ICT\_AM\_PAR\_GER\_DEB\_ESP__ para o Estabelecimento, inscrição estadual selecionados na tela de geração\.

      

Atendido esse critério, executar os passos a seguir\.

__Passo 1 \- Validação:__

Fazer as seguintes validações em relação aos cadastros de Obrigação Fiscal, Calendáro e Status da Apuração:

1. Verificar a existência de __Obrigação Fiscal__ cadastrada, fazendo uma consulta na tabela __ICT\_OBRIG\_INSC\_EST__, com os seguintes critérios:

\- Estabelecimento = selecionado na tela de geração

\- Inscrição Estadual = selecionado na tela de geração

\- Código do Livro = ‘108’

Se não existir Obrigação Fiscal, exibir a mensagem:

“Não é possível gerar os registros de Débitos Especiais e Guias de Recolhimento, pois não foi cadastrada Obrigação Fiscal 108, para o Estabelecimento e Inscrição Estadual informados\. Favor criar o cadastro no módulo Estadual >> Controle das Obriações Estaduais, menu Obrigações >> Obrigações Fiscais >> Por Inscrição Estadual para ZFM”\.

Dados Chave: Estabelecimento – Inscrição Estadual

1. Verificar a existência de __Calendário da Obrigação Fiscal__, fazendo uma consulta na tabela ICT\_CALEN\_INSC\_EST considerando os critérios:

\- Estabelecimento = selecionado na tela de geração

\- Inscrição Estadual = selecionado na tela de geração

\- Código do Livro = 108

\- Data Apuração = último dia do período informado na tela de geração

Se não existir Calendário da Obrigação Fiscal, exibir a mensagem:

“Não é possível gerar os registros de Débitos Especiais e Guias de Recolhimento, pois não foi criado Calendário para a Obrigação Fiscal 108, para o Estabelecimento, Inscrição Estadual e Período informados\. Favor criar o cadastro no módulo Estadual >> Controle das Obriações Estaduais, menu Obrigações >> Calendário das Obrigações >> Por Inscrição Estadual para ZFM”\.

Dados Chave: Estabelecimento – Inscrição Estadual – Último dia do Período informado na tela

1.  Verificar __Status da Obrigação Fiscal__, fazendo uma consulta na tabela ICT\_APUR\_INSC\_EST, considerando os critérios:

\- Estabelecimento = selecionado na tela de geração

\- Inscrição Estadual = selecionado na tela de geração

\- Código do Livro = 108

\- Data Apuração = último dia do período informado na tela de geração

\- Situação = 2\- Apuração Realizada

\- Validade = 2 \- Válido

Se consulta acima retornar registro, significa que a apuração está encerrada\. Nesse caso, exibir a mensagem:

“Não é possível gerar os registros de Débitos Especiais e Guias de Recolhimento, pois a Apuração do ICMS encontra\-se encerrada,  para o Estabelecimento, Inscrição Estadual e Período informados\. Favor reabrir a apuração através da opção disponível no menu Parâmetros >> Status das Obrigações Estaduais”\.

Dados Chave: Estabelecimento – Inscrição Estadual – Último dia do Período informado na tela

Se ocorrer qualquer uma dessas críticas, os próximos passos não serão executados\.

__Passo 2: Limpeza dos Débitos Especiais:__

Através da consulta a seguir eliminar os registros de Débitos Especiais gerados automaticamente em processamentos anteriores\.

Tabela: ICT\_DEB\_ESP\_IES

Critérios:

\- Estabelecimento = selecionado na tela de geração

\- Inscrição Estadual = selecionado na tela de geração

\- Código do Livro = 108

\- Data Apuração = último dia do período informado na tela de geração

\- Se compontente 19 estiver selecionado para geração:

   Excluir os registros com Ind\_Dig\_Calculado = ‘2’

\- Se compontente 20 estiver selecionado para geração:

   Excluir os registros com Ind\_Dig\_Calculado = ‘3’

\- Se compontente 21 estiver selecionado para geração:

   Excluir os registros com Ind\_Dig\_Calculado = ‘4’

É importante ressaltar que os Débitos Especiais incluídos manualmente via tela de Lançamento Complementar não podem ser eliminados\. E apenas excluir os débitos especiais gerados automaticamente relacionados aos componentes selecionados na tela de geração\.

Sendo assim estamos utilizando o campo IND\_DIG\_CALCULADO para identificar a origem do Débito Especial:

IND\_DIG\_CALCULADO:

 \- 1 \- inserido manualmente;

 \- 2 \- gerado automaticamente para o Componente 19

 \- 3 \- gerado automaticamente para o Componente 20

 \- 4 \- gerado automaticamente para o Componente 21

__Passo 3: Recuperação dos Valores dos Mapas Acessórios do FTI, UEA, FMPES__

Recuperar os Valor Calculado para cada Linha de Incentivo, Componente, Estrutura e Item dos Mapas Acessórios, fazendo uma consulta na tabela __ICT\_AM\_AP\_E\_S__ com os seguintes critérios:

\- Estabelecimento = selecionado na tela de geração

\- Inscrição Estadual = selecionado na tela de geração

\- Data Apuração = último dia do período informado na tela de geração

\- Código do Componente = selecionados na tela de geração

\- Código do Componente = 19 \(FTI\) ou 20 \(FMPES\) ou 21 \(UEA\)

Recuperar as seguintes informações:

\- Código da Linha de Incentivo

\- Código do Componente

\- Código da Estrutura

\- Código do Item

\- Valor da Contribuição

Para cada registro do Mapa Acessório acima recuperado, consultar a Parametrização para Geração Automática dos Débitos Especiais \(Sped Fiscal – E111/1921\) – tabela __ICT\_AM\_PAR\_GER\_DEB\_ESP__ com os seguintes critérios:

\- Estabelecimento = selecionado na tela de geração

\- Inscrição Estadual = selecionado na tela de geração

\- Código da Linha de Incentivo, Código do Componente, Código da Estrutura, Código do Item recuperado do Mapa Acessório 

Caso a parametrização não seja encontrada, exibir a seguinte mensagem:

“Aviso: Não foi encontrada parametrização para geração do registro de Débito Especial para a Linha de Incentivo, Componente, Estrutura e Item\. Favor rever a parametrização disponível no menu Parâmetros >> Parâmetros dos Mapas >> Parâmetros para Geração Automática >> Débitos Especiais \(Sped Fiscal – E111/1921\)”\.

Dados Chave: Estabelecimento – Inscrição Estadual – Linha de Incentivo – Componente – Estrutura \- Item

Caso encontrada, recuperar o Código de Ajuste, a Descrição e o Código da Subapuração e efetuar a gravação do Débito Especial\.

__Passo 4: Gravação dos Débitos Especiais__

A relação entre as tabelas de Mapas Acessórios \(ICT\_AM\_AP\_E\_S\) e Débitos Especiais \(ICT\_DEB\_ESP\_IES\) é 1:1, ou seja, um registro de Mapa Acessório gera um registro de Débito Especial\. Veja a regra de preenchimento de cada campo para gravação do Débito Especial\.

__Tabela de Débito Especial \(ICT\_DEB\_ESP\_IES\)__

- Empresa \(cod\_empresa\): empresa de login;
- Estabelecimento \(cod\_estab\): estabelecimento selecionado para geração;
- Inscrição Estadual \(insc\_estadual\): inscrição estadual selecionada para geração;
- Obrigação Fiscal \(cod\_tipo\_livro\): 108;
- Data Apuração \(dat\_apuracao\): último dia do período informado para geração;
- Num\_discriminacao: sequencial único por empresa, estabelecimento, inscrição estadual, obrigação fiscal e data apuração\.
- Código de Ajuste \(cod\_ajuste\_icms\): Código de Ajuste recuperado da parametrização Geração Automática dos Débitos Especiais \(Sped Fiscal – E111/1921\) – tabela __ICT\_AM\_PAR\_GER\_DEB\_ESP__\.
- Valor do Débito \(val\_debito\) : Valor da Contribuição do Mapa Acessório recuperado da tabela __ICT\_AM\_AP\_E\_S__
- Descrição \(dsc\_debito\): Descrição recuperada da parametrização Geração Automática dos Débitos Especiais \(Sped Fiscal – E111/1921\) – tabela __ICT\_AM\_PAR\_GER\_DEB\_ESP__\.
- ind\_dig\_calculado: 

Se compontente 19 estiver selecionado para geração:

   Ind\_Dig\_Calculado = ‘2’

\- Se compontente 20 estiver selecionado para geração:

   Ind\_Dig\_Calculado = ‘3’

\- Se compontente 21 estiver selecionado para geração:

  Ind\_Dig\_Calculado = ‘4’

- Subapuração do Sped Fiscal \(ind\_sub\_apur\): Código da Subapuração recuperado da parametrização Geração Automática dos Débitos Especiais \(Sped Fiscal – E111/1921\) – tabela __ICT\_AM\_PAR\_GER\_DEB\_ESP__\.

Os Débitos Especiais gerados podem ser consultados, alterados e excluídos via tela de manutenção dos Lançamentos Complementares da Apuração do ICMS \-  aba Débitos Especiais\.

MFS84451

RN05

__Geração Automática dos Valores Declaratórios__

Após o cálculo de todos os componentes, realizar a geração dos Valores Declaratórios para os componentes 19 – F\.T\.I, 20 – F\.M\.P\.E\.S e 21 – U\.E\.A\.

Esta geração consiste em recuperar o valor calculado dos Mapas Acessórios para cada Linha de Incentivo/Componente/Estrutura/Item e gerar um registro de Valor Declaratório com o valor da contribuição ou valor da sua base de cálculo, conforme Parametrização para Geração Automática dos Valores Declaratórios \(Sped Fiscal – E115/1925\)\.

O valor da contribuição calculada nos Mapas Acessórios – tabela  ICT\_AM\_AP\_E\_S pode ser conferida através do Relatório Sintético dos Mapas \(menu Relatórios>> Emissão dos Mapas >> Relatório Sintético dos Mapas\)\.

A Parametrização para Geração Automática dos Valores Declaratórios \(Sped Fiscal – E115/1925\) – tabela ICT\_AM\_PAR\_GER\_VAL\_DEC está disponível no menu Parâmetros >> Parâmetros dos Mapas >> Parâmetros para Geração Automática >> Valores Declaratórios \(Sped Fiscal – E115/1925\) e contempla apenas os componentes 19, 20 e 21\.

 

__Procedimentos para Geração:__

A geração dos Valores Declaratórios só será executada se pelo menos um dos componentes selecionados na tela de geração possuir: 

     \- Parametrização para Geração Automática dos Valores Declaratórios \(Sped Fiscal – E115/1925\) – tabela 

__       ICT\_AM\_PAR\_GER\_VAL\_DEC__ para o Estabelecimento, inscrição estadual selecionados na tela de geração\.

      

Atendido esse critério, executar os passos a seguir\.

__Passo 1: Limpeza dos Valores Declaratórios:__

Através da consulta a seguir, eliminar os registros de Valores Declaratórios gerados automaticamente em processamentos anteriores\.

Tabela: EFD\_REG\_E115\_IES

Critérios:

\- Estabelecimento = selecionado na tela de geração

\- Inscrição Estadual = selecionado na tela de geração

\- Data Inicial e Data Final compreendidas entre a data inicial e final do período informado na tela de geração

\- Se compontente 19 estiver selecionado para geração:

   Excluir os registros com Ind\_Gravacao = ‘2’

\- Se compontente 20 estiver selecionado para geração:

   Excluir os registros com Ind\_Gravacao = ‘3’

\- Se compontente 21 estiver selecionado para geração:

   Excluir os registros com Ind\_Gravacao = ‘4’

É importante ressaltar que os Valores Declaratórios incluídos manualmente ou importados via SAFX245 não podem ser eliminados\. Apenas excluir os Valores Declaratórios gerados automaticamente relacionados aos componentes selecionados na tela de geração\.

Sendo assim estamos utilizando o campo IND\_GRAVACAO para identificar a origem do Valor Declaratório:

IND\_GRAVACAO:

\- Nulo – inserido manualmente via tela disponível no módulo Sped Fiscal – Menu Geração – PIM >> Manutenção\.

 \- 1 – Importado via SAFX245;

 \- 2 \- gerado automaticamente para o Componente 19

 \- 3 \- gerado automaticamente para o Componente 20

 \- 4 \- gerado automaticamente para o Componente 21

__Passo 3: Recuperação dos Valores dos Mapas Acessórios do FTI, UEA, FMPES__

Recuperar os Valores da Contribuição e da Base de Cálculo para cada Linha de Incentivo, Componente, Estrutura e Item dos Mapas Acessórios, fazendo uma consulta na tabela __ICT\_AM\_AP\_E\_S__ com os seguintes critérios:

\- Estabelecimento = selecionado na tela de geração

\- Inscrição Estadual = selecionado na tela de geração

\- Data Apuração = último dia do período informado na tela de geração

\- Código do Componente = selecionados na tela de geração

\- Código do Componente = 19 \(FTI\) ou 20 \(FMPES\) ou 21 \(UEA\)

Recuperar as seguintes informações:

\- Código da Linha de Incentivo

\- Código do Componente

\- Código da Estrutura

\- Código do Item

\- Valor da Contribuição \(vlr\_icms\)

\- Valor da Base de Cálculo da Contribuição \(vlr\_base\_calc\)

Para cada registro do Mapa Acessório acima recuperado, consultar a Parametrização para Geração Automática dos Valores Declaratórios \(Sped Fiscal – E115/1925\) – tabela __ICT\_AM\_PAR\_GER\_VAL\_DEC__ com os seguintes critérios:

\- Estabelecimento = selecionado na tela de geração

\- Inscrição Estadual = selecionado na tela de geração

\- Código da Linha de Incentivo, Código do Componente, Código da Estrutura, Código do Item recuperado do Mapa Acessório 

Caso a parametrização não seja encontrada, exibir a seguinte mensagem:

“Aviso: Não foi encontrada parametrização para geração do registro de Valores Declaratórios para a Linha de Incentivo, Componente, Estrutura e Item\. Favor rever a parametrização disponível no menu Parâmetros >> Parâmetros dos Mapas >> Parâmetros para Geração Automática >> Valores Declaratórios \(Sped Fiscal – E115/1925\)”\.

Dados Chave: Estabelecimento – Inscrição Estadual – Linha de Incentivo – Componente – Estrutura \- Item

Caso encontrada, recuperar os campo abaixo e seguir para gravação do registro de Valor Declaratório:

\- Código Informação Adicional \(cod\_inf\_adic\)

\- “Gerar Valor Declaratório com” \(ind\_vlr\_adic\)

\- Descrição Complementar \(dsc\_compl\) 

\- Código da Subapuração \(ind\_sub\_apur\)\.

__Passo 4: Gravação dos Valores Declaratórios__

A relação entre as tabelas de Mapas Acessórios \(ICT\_AM\_AP\_E\_S\) e Valores Declaratórios \(EFD\_REG\_E115\_IES\) é 1:1, ou seja, um registro de Mapa Acessório gera um registro de Valor Declaratório\. Veja a regra de preenchimento de cada campo:

__Tabela de Valores Declaratórios \(EFD\_REG\_E115\_IES\)__

- Empresa \(cod\_empresa\): empresa de login;
- Estabelecimento \(cod\_estab\): estabelecimento selecionado para geração;
- Inscrição Estadual \(insc\_estadual\): inscrição estadual selecionada para geração;
- Data Inicial \(data\_ini\): primeiro dia do período informado para geração;
- Data Final \(data\_fim\): último dia do período informado para geração;
- Sequencial: sequencial único por empresa, estabelecimento, inscrição estadual, Data Inicial e Data Final\.
- Código Informação Adicional \(cod\_inf\_adic\): “Código Informação Adicional” recuperado da parametrização Geração Automática dos Valores Declaratórios \(Sped Fiscal – E115/1925\) – tabela __ICT\_AM\_PAR\_GER\_VAL\_DEC__\.
- Valor da Informação Adicional \(vlr\_inf\_adic\): 

Se campo “Gerar Valor Declaratório com” = “Valor da Contribuição” \(ind\_vlr\_adic = ‘C’\), então:

    Preencher com Valor da Contribuição \(vlr\_icms\) do Mapa Acessório recuperado da tabela __ICT\_AM\_AP\_E\_S__

Se campo “Gerar Valor Declaratório com” = “Base de Cálculo” \(ind\_vlr\_adic = ‘B’\), então:

    Preencher com Valor da Base de Cálculo da Contribuição \(vlr\_base\_calc\) do Mapa Acessório recuperado da tabela __ICT\_AM\_AP\_E\_S__

- Descrição Complementar \(dsc\_compl\): “Descrição Complementar” recuperada da parametrização Geração Automática dos Valores Declaratórios \(Sped Fiscal – E115/1925\) – tabela __ICT\_AM\_PAR\_GER\_VAL\_DEC__\.\.
- Usuário: usuário de login da aplicação
- Data Operação \(dat\_operacao\): data atual da execução da geração do mapa acessório\.
- Subapuração do Sped Fiscal \(ind\_sub\_apur\): Código da Subapuração recuperado da parametrização Geração Automática dos Valores Declaratórios \(Sped Fiscal – E115/1925\) – tabela __ICT\_AM\_PAR\_GER\_VAL\_DEC__\.
- Número Processo \(num\_processo\): número do processo da execução da geração\.
- Ind\_gravacao: 

Se Compontente do Mapa Acessório recuperado da tabela __ICT\_AM\_AP\_E\_S __for ‘19’, então:

   Gravar Ind\_gravacao com ‘2’

\- Se Compontente do Mapa Acessório recuperado da tabela __ICT\_AM\_AP\_E\_S__ for ‘20’, então:

   Gravar Ind\_gravacao com ‘3’

\- Se Compontente do Mapa Acessório recuperado da tabela __ICT\_AM\_AP\_E\_S __for ‘21’, então:

  Gravar Ind\_gravacao com ‘4’

Os Valores Declaratórios gerados podem ser consultados, alterados e excluídos via tela de manutenção disponível no módulo Sped Fiscal – Menu Geração – PIM >> Manutenção >> Registro E115/1925 \(Valores Declaratórios\)\.

MFS85986

RN06

__Geração Automática das Guias de Recolhimento__

Após o cálculo de todos os componentes, realizar a geração das guias de recolhimento aplicada aos componentes 19 – F\.T\.I, 20 – F\.M\.P\.E\.S e 21 – U\.E\.A\.

Esta geração consiste em recuperar o valor calculado dos Mapas Acessórios para cada Linha de Incentivo/Componente/Estrutura/Item e gerar um registro de Guia de Recolhimento com o valor calculado e com as informações da Parametrização para Geração Automática das Guias de Recolhimento \(Sped Fiscal – E116/1926\)\.

O valor calculado dos Mapas Acessórios – tabela  ICT\_AM\_AP\_E\_S pode ser conferido através do Relatório Sintético dos Mapas \(menu Relatórios>> Emissão dos Mapas >> Relatório Sintético dos Mapas\)\.

A Parametrização para Geração Automática das Guias de Recolhimento \(Sped Fiscal – E116/1926\) – tabela ICT\_AM\_PAR\_GER\_GUIA está disponível no menu Parâmetros >> Parâmetros dos Mapas >> Parâmetros para Geração Automática >> Guias de Recolhimento \(Sped Fiscal – E116/1926\) e contempla apenas os componentes 19, 20 e 21\.

 

__Procedimentos para Geração:__

A geração das Guias de Recolhimento só será executada se pelo menos um dos componentes selecionados na tela de geração possuir: 

     \- Parametrização para Geração Automática das Guias de Recolhimento \(Sped Fiscal – E116/1926\) \-  tabela 

__       ICT\_AM\_PAR\_GER\_GUIA __para o Estabelecimento, inscrição estadual selecionados na tela de geração\.

      

Atendido esse critério, executar os passos a seguir\.

__Passo 1 \- Validação:__

Fazer as seguintes validações em relação aos cadastros de Obrigação Fiscal, Calendáro e Status da Apuração:

1. Verificar a existência de __Obrigação Fiscal__ cadastrada, fazendo uma consulta na tabela __ICT\_OBRIG\_INSC\_EST__, com os seguintes critérios:

\- Estabelecimento = selecionado na tela de geração

\- Inscrição Estadual = selecionado na tela de geração

\- Código do Livro = ‘108’

Se não existir Obrigação Fiscal, exibir a mensagem:

“Não é possível gerar os registros de Débitos Especiais e Guias de Recolhimento, pois não foi cadastrada Obrigação Fiscal 108, para o Estabelecimento e Inscrição Estadual informados\. Favor criar o cadastro no módulo Estadual >> Controle das Obriações Estaduais, menu Obrigações >> Obrigações Fiscais >> Por Inscrição Estadual para ZFM”\.

Dados Chave: Estabelecimento – Inscrição Estadual

1. Verificar a existência de __Calendário da Obrigação Fiscal__, fazendo uma consulta na tabela ICT\_CALEN\_INSC\_EST considerando os critérios:

\- Estabelecimento = selecionado na tela de geração

\- Inscrição Estadual = selecionado na tela de geração

\- Código do Livro = 108

\- Data Apuração = último dia do período informado na tela de geração

Se não existir Calendário da Obrigação Fiscal, exibir a mensagem:

“Não é possível gerar os registros de Débitos Especiais e Guias de Recolhimento, pois não foi criado Calendário para a Obrigação Fiscal 108, para o Estabelecimento, Inscrição Estadual e Período informados\. Favor criar o cadastro no módulo Estadual >> Controle das Obriações Estaduais, menu Obrigações >> Calendário das Obrigações >> Por Inscrição Estadual para ZFM”\.

Dados Chave: Estabelecimento – Inscrição Estadual – Último dia do Período informado na tela

1.  Verificar __Status da Obrigação Fiscal__, fazendo uma consulta na tabela ICT\_APUR\_INSC\_EST, considerando os critérios:

\- Estabelecimento = selecionado na tela de geração

\- Inscrição Estadual = selecionado na tela de geração

\- Código do Livro = 108

\- Data Apuração = último dia do período informado na tela de geração

\- Situação = 2\- Apuração Realizada

\- Validade = 2 \- Válido

Se consulta acima retornar registro, significa que a apuração está encerrada\. Nesse caso, exibir a mensagem:

“Não é possível gerar os registros de Débitos Especiais e Guias de Recolhimento, pois a Apuração do ICMS encontra\-se encerrada,  para o Estabelecimento, Inscrição Estadual e Período informados\. Favor reabrir a apuração através da opção disponível no menu Parâmetros >> Status das Obrigações Estaduais”\.

Dados Chave: Estabelecimento – Inscrição Estadual – Último dia do Período informado na tela

Se ocorrer qualquer uma dessas críticas, os próximos passos não serão executados\.

__Passo 2: Limpeza das Guias de Recolhimento:__

Através da consulta a seguir eliminar os registros de Guias de Recolhimento geradas automaticamente em processamentos anteriores\.

Tabela: GUIA\_RECOL\_IES

Critérios:

\- Estabelecimento = selecionado na tela de geração

\- Inscrição Estadual = selecionado na tela de geração

\- Código do Livro = 108

\- Data Apuração = último dia do período informado na tela de geração

\- Se compontente 19 estiver selecionado para geração:

   Excluir os registros com Ind\_Dig\_Calculado = ‘2’

\- Se compontente 20 estiver selecionado para geração:

   Excluir os registros com Ind\_Dig\_Calculado = ‘3’

\- Se compontente 21 estiver selecionado para geração:

   Excluir os registros com Ind\_Dig\_Calculado = ‘4’

É importante ressaltar que as Guias de Recolhimento incluídas manualmente via tela de Lançamento Complementar não podem ser eliminadas\. Apenas excluir as guias geradas automaticamente relacionadas aos componentes selecionados na tela de geração\.

Sendo assim estamos utilizando o campo IND\_DIG\_CALCULADO para identificar a origem da GUIA DE RECOLHIMENTO:

IND\_DIG\_CALCULADO:

 \- NULO \- inserido manualmente;

 \- 2 \- gerado automaticamente para o Componente 19

 \- 3 \- gerado automaticamente para o Componente 20

 \- 4 \- gerado automaticamente para o Componente 21

__Passo 3: Recuperação dos Valores dos Mapas Acessórios do FTI, UEA, FMPES__

Recuperar os Valor Calculado para cada Linha de Incentivo, Componente, Estrutura e Item dos Mapas Acessórios, fazendo uma consulta na tabela __ICT\_AM\_AP\_E\_S__ com os seguintes critérios:

\- Estabelecimento = selecionado na tela de geração

\- Inscrição Estadual = selecionado na tela de geração

\- Data Apuração = último dia do período informado na tela de geração

\- Código do Componente = selecionados na tela de geração

\- Código do Componente = 19 \(FTI\) ou 20 \(FMPES\) ou 21 \(UEA\)

Recuperar as seguintes informações:

\- Código da Linha de Incentivo

\- Código do Componente

\- Código da Estrutura

\- Código do Item

\- Valor da Contribuição

Para cada registro do Mapa Acessório acima recuperado, consultar a Parametrização para Geração Automática das Guias de Recolhimento \(Sped Fiscal – E116/1926\) – tabela __ICT\_AM\_PAR\_GER\_GUIA__ com os seguintes critérios:

\- Estabelecimento = selecionado na tela de geração

\- Inscrição Estadual = selecionado na tela de geração

\- Código da Linha de Incentivo, Código do Componente, Código da Estrutura, Código do Item recuperado do Mapa Acessório 

Caso a parametrização não seja encontrada, exibir a seguinte mensagem:

“Aviso: Não foi encontrada parametrização para geração do registro de Guia de Recolhimento para a Linha de Incentivo, Componente, Estrutura e Item\. Favor rever a parametrização disponível no menu Parâmetros >> Parâmetros dos Mapas >> Parâmetros para Geração Automática >> Guias de Recolhimento \(Sped Fiscal – E116/1926\)”\.

Dados Chave: Estabelecimento – Inscrição Estadual – Linha de Incentivo – Componente – Estrutura \- Item

Caso encontrada, recuperar os dados da parametrização, calcular a Data Vencimento e efetuar a gravação da Guia de Recolhimento\.

__Passo 4: Gravação das Guias de Recolhimento__

A relação entre as tabelas de Mapas Acessórios \(ICT\_AM\_AP\_E\_S\) e Guias de Recolhimento \(GUIA\_RECOL\_IES\) é 1:1, ou seja, um registro de Mapa Acessório gera um registro de Guia de Recolhimento\. Veja a regra de preenchimento de cada campo para gravação da Guia\. Obs: apenas gravaremos os campos obrigatórios para geração dos registros do Sped Fiscal \(E116/1926\)

__Tabela de Guias de Recolhimento \(GUIA\_RECOL\_IES\)__

- Empresa \(cod\_empresa\): empresa de login;
- Estabelecimento \(cod\_estab\): estabelecimento selecionado para geração;
- Inscrição Estadual \(insc\_estadual\): inscrição estadual selecionada para geração;
- Obrigação Fiscal \(cod\_tipo\_livro\): 108;
- Data Apuração \(dat\_apuracao\): último dia do período informado para geração;
- Número da Guia \(NUM\_GUIA\_RECOL\): sequencial único por empresa, estabelecimento, inscrição estadual, obrigação fiscal e data apuração\.
- Data Recolhimento \(DAT\_GUIA\_RECOL\): não preencher
- Valor Recolhimento \(VAL\_GUIA\_RECOL\): Valor da Contribuição do Mapa Acessório recuperado da tabela __ICT\_AM\_AP\_E\_S__
- Data Entrega \(DAT\_ENTREGA\): não preencher
- Local Entrega \(DSC\_LOCAL\_ENTREGA\): não preencher
- Orgão Arreadador \(ident\_org\_arrecad\): não preencher
- Receita Estadual\(IDENT\_RECEITA\_EST\): Receita Estadual da parametrização Geração Automática das Guias de Recolhimento \(Sped Fiscal – E116/1926\) – tabela __ICT\_AM\_PAR\_GER\_GUIA__\. Gravar o  IDENT\_RECEITA\_EST do registro de máxima validade recuperado da tabela X2080\_COD\_REC\_UF com o Grupo Receita, UF e Código da Receita e Validade <=Data Apuração\.
- IDENT\_ESTADO: UF da Receita Estadual da parametrização Geração Automática das Guias de Recolhimento \(Sped Fiscal – E116/1926\) – tabela __ICT\_AM\_PAR\_GER\_GUIA__ – IDENT\_ESTADO\.
- Número Processo \(num\_proc\): não preencher
- Origem Processo \(origem\_proc\): não preencher
- Descrição Processo \(dsc\_proc\): não preencher
- Código Obrigação \(cod\_obrigacao\): Código Obrigação da parametrização Geração Automática das Guias de Recolhimento \(Sped Fiscal – E116/1926\) – tabela __ICT\_AM\_PAR\_GER\_GUIA__\.
- Descrição Complementar \(dsc\_complementar\): Descrição recuperada da parametrização Geração Automática das Guias de Recolhimento \(Sped Fiscal – E116/1926\) – tabela __ICT\_AM\_PAR\_GER\_GUIA__\.
- Data Vencimento \(DAT\_VENCTO\): Data calculada a partir da Data Apuração gravada na guia de recolhimento com os parâmetros “Número de Dias p/ Vencimento” e “Critério de Dias p/ Vencimento” da parametrização da Geração Automática das Guias de Recolhimento \(Sped Fiscal – E116/1926\)\.

                                     Data Vencimento = Data Apuração \+ Número de Dias p/ Vencimento

 Onde

\- Data Apuração = último dia do período informado para geração

Ao somar o Número de Dias p/ Vencimento, será considerado o parâmetro “Critério de Dias p/ Vencimento”, da seguinte forma:

‘1’ \- Dias úteis 🡪 ao efetuar a soma dos dias, considerar apenas os dias úteis, excluindo sábados, domingos e feriados \(\*\*\*\)\.

‘4’ \- Dias fixos \(antecipar\) 🡪 usar o critério do Dia Fixo, mas antecipando para o dia útil imediatamente anterior, quando o vencimento calculado cair em sábado, domingo ou feriado\.

‘5’ \- Dias fixos \(postergar\) 🡪 usar o critério do Dia Fixo, mas postergando para o dia útil imediatamente posterior, quando o vencimento calculado cair em sábado, domingo ou feriado\.

‘9’ \- Dia fixo 🡪 neste caso o vencimento será sempre no dia informado no campo “Número de dias p/ Vencimento”, considerando o mês/ano subsequente ao da Data Apuração:

\(\*\*\*\) Para verificar os feriados, utilizar o cadastro dos feriados do módulo DW\. Considerar todos os feriados nacionais e os feriados estaduais referentes à UF em questão \(UF favorecida\)\.

- Mês/Ano Referência \(MES\_ANO\_REF\): último dia do período informado para geração
- Subapuração do Sped Fiscal \(ind\_sub\_apur\): Código da Subapuração recuperado da parametrização Geração Automática das Guias de Recolhimento \(Sped Fiscal – E116/1926\) – tabela __ICT\_AM\_PAR\_GER\_GUIA__ – DIA\_VENCTO\.
- ind\_dig\_calculado: 

Se compontente 19 estiver selecionado para geração:

   Ind\_Dig\_Calculado = ‘2’

\- Se compontente 20 estiver selecionado para geração:

   Ind\_Dig\_Calculado = ‘3’

\- Se compontente 21 estiver selecionado para geração:

  Ind\_Dig\_Calculado = ‘4’

As Guias de Recolhimento geradas podem ser consultadas, alterados e excluídas via tela de manutenção dos Lançamentos Complementares da Apuração do ICMS \-  aba Guias\.

MFS84451

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


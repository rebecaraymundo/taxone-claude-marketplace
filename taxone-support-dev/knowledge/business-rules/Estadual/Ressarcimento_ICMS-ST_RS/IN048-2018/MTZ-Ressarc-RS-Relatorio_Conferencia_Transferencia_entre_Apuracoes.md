# MTZ-Ressarc-RS-Relatorio_Conferencia_Transferencia_entre_Apuracoes

- **Fonte:** MTZ-Ressarc-RS-Relatorio_Conferencia_Transferencia_entre_Apuracoes.docx
- **Modificado:** 2021-09-30
- **Tamanho:** 84 KB

---

THOMSON REUTERS

Módulo Ressarcimento de ICMS\-ST – RS \(IN\-RE 048/2018\) 

Relatório de Conferência da Transferência entre Apurações 

<a id="_Hlk2155195"></a>__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\), menu Relatórios 🡪 IN\-RE 048/2018 🡪 Conferência da Transferência entre Apurações 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS29923

Liliane V\. Assaf

Alteração no relatório de conferência das transferências entre apurações

23/08/2019

Sumário

[1\.	Regras Gerais	3](#_Toc17485998)

[2\.	Layout da Tela	3](#_Toc17485999)

[3\.	Regras de Funcionamento dos Campos	4](#_Toc17486000)

[4\.	Definição do Relatório	5](#_Toc17486001)

[4\.1 – Recuperação dos Registros:	5](#_Toc17486002)

[4\.2 – Layout e Preenchimento dos Campos:	7](#_Toc17486003)

# <a id="_Toc17485998"></a>Regras Gerais

Este relatório tem por objetivo demonstrar os lançamentos de transferência gerados no menu “Geração > Transferência entre Apurações\.

Os lançamento são realizados em duas apurações:

- Subapuração do RS
- Apuração do ICMS\-ST \(P9\-ST\)

# <a id="_Toc17485999"></a>Layout da Tela

<a id="_Hlk17482979"></a>Período : \[ dd/aaaa \]

Geração por Inscrição Estadual Única \[ x \]

Estabelecimentos:

Contribuinte Varejista \[x\] 

\[ x \] xxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx      

\[ y \] xxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx      

\[    \] xxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[    \] xxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# <a id="_Toc17486000"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato / Default__

__Regra__

Período 

Data

\(mês e ano\)

S

S

\(MM/AAAA\)

Neste campo será informado o período \(mês e ano\) para a emissão do relatório\.

Deve ser um mês válido\.

Geração por Inscrição Estadual Ùnica

Check box

N

N

Não

O parâmetro de Geração por Inscrição Estadual Ùnica determina os estabelecimentos a serem apresentados\.

\(NÃO VAMOS TRATAR NA MFS\-28005\)

Portanto vamos mantê\-lo desabilitado\.

Contribuinte Varejista

Check box

S

S

Sim

Informar se o estabelecimento é varejista ou não\. 

Com base nesta informação, o sistema disponibiliza o conjunto de estabelecimentos parametrizados em Dados Iniciais como varejista ou não varejista\.

Estabelecimentos

Alfanumérico 

__     __S 

S

Neste campo é exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário\.

Serão disponibilizados para seleção os estabelecimentos que atendam os critérios:

\- Estabelecimentos do Rio Grande do Sul \(UF = __RS__\)\.

\- Caso a opção “Contribuinte Varejista” seja selecionada: 

    Apresentar os estabelecimentos parametrizados em Dados

    Iniciais como Varejista\.

\- Caso a opção “Contribuinte Varejista” seja desmarcada:

    Apresentar os estabelecimentos definidos com Não 

    Varejistas na parametrização dos Dados Iniciais\. 

Selecionar

N

N

Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos\.

O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimento”:

\- Somente Estabelecimentos da empresa do login;

\- Somente Estabelecimentos da UF de RS;

\- Caso a opção “Contribuinte Varejista” seja selecionada: 

    Somente os estabelecimentos parametrizados em Dados

    Iniciais como Varejista\.

\- Caso a opção “Contribuinte Varejista” seja desmarcada:

    Somente os estabelecimentos definidos com Não 

    Varejistas na parametrização dos Dados Iniciais\.

Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimentos” já marcados\.    

Marcar todos

N

N

Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos”\.

# <a id="_Toc17486001"></a>Definição do Relatório

## <a id="_Toc17486002"></a>4\.1 – Recuperação dos Registros:

Será gerado um único relatório para a empresa de login\.

Todos os estabelecimentos selecionados em tela são apresentados nas linhas de detalhes\.

<a id="_Hlk17483997"></a>Origem dos dados:  \- Tabela de Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUB__RS__\)

                                  Tabela de Lançamentos da Apuração do ICMS\-ST \(ITEM\_APURAC\_SUB__ST__\)

                                   \(vide documento MTZ\-Ressarc\-RS\-Geracao\_Transferencia\_entre\_Apuracoes\)\.

Critérios da Recuperação dos Lançamentos da Origem da Transferência:

Fazer uma consulta nas Tabelas abaixo: 

- Tabela do Resumo da Subapuração do RS \(ICT\_SUB\_APURACAO\_RS\)
- Tabela de Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUB__RS__\)

Assumir os critérios:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Códigos dos estabelecimentos selecionados em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

- Indicador de Lançamento Digitado/calculado  \(ind\_dig\_calculado\) = __‘5’__ \- lançamento gerado via processo de transferência

Critérios da Recuperação dos Lançamentos de Destino da Transferência

Fazer uma consulta na Tabela de Lançamentos da Apuração do ICMS\-ST \(ITEM\_APURAC\_SUB__ST__\), com os critérios:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Códigos dos estabelecimentos selecionados em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

- Estado = “RS”
- Indicador de Lançamento Digitado/calculado \(ind\_dig\_calculado\) = __‘5’__ \- lançamento gerado via processo de transferência

Na mesma linha do relatório serão apresentados os dados do estabelecimento, do lançamento de origem e do lançamento de destino\.

O relatório é a conferência do resultado do processo de Geração da Transferência  \(menu Geração >> Transferência entre Apurações\)\.  Para enterder as regras de geração veja “*MTZ\-Ressarc\-RS\-Geracao\_Transferencia\_entre\_Apuracoes\.doc*”\.

As regras de ordenação e preenchimento das colunas no relatório estão descritas no item a seguir\.

## <a id="_Toc17486003"></a>4\.2 – Layout e Preenchimento dos Campos:

Layout: vide planilha “__Layout\-Relatorios\-Conferencia__”, aba “__Transferência__”\.

Ordenação dos movimentos:

- Código do Estabelecimento; 

Preenchimento dos campos do relatório:

__Linhas de cabeçalho:__

Primeira linha de cabeçalho

Informações desta linha: 

\- Razão social da empresa;

\- Data da emissão do relatório;

\- Página do relatório;

Segunda linha de cabeçalho

Informações desta linha:

\- Título do relatório \(“Listagem das Transferências entre Apurações”\); 

Teceira linha de cabeçalho

Período solicitado em tela \(mês e ano\);

__Linhas de detalhamento dos movimentos:__

Estabelecimento

Apresentar o código e a razão social do estabelecimento

__Origem da Transferência__

Apuração 

Preencher com “Subapuração” \+ Código da Subapuração em que foi realizado o lançamento\. 

\(tabela ITEM\_APURAC\_SUBRS – campo IND\_SUB\_APUR\)

Lançamento \(cód\. – descrição\)

Preencher com o Código e a Descrição do Item da Apuração em que foi realizado o lançamento na subapuração mais o Código do Ajuste ICMS\.

\(tabela ITEM\_APURAC\_SUB__RS__ – campo COD\_OPER\_APUR \+ 

 tabela OPERACAO\_APURACAO – campo DSC\_OPER\_APUR \+

 tabela ITEM\_APURAC\_SUB__RS__ \- campo COD\_AJUSTE\_ICMS\)

Valor

Valor do lançamento realizado na subapuração\.

\(tabela ITEM\_APURAC\_SUBRS – campo VAL\_ITEM\_DISCRIM\)

Saldo Final

Soma dos campos ICMS a Recolher \+ Saldo Credor a Transportar da Tabela do Resumo da Subapuração do RS

\(ICT\_SUB\_APURACAO\_RS – campo VLR\_ICMS\_RECOLHER campo VL\_SLD\_CREDOR\_TRANSP\)\.

__Destino da Transferência__

Apuração

Fixo “ICMS\-ST”

Lançamento \(cód\. – descrição\)

Preencher com o Código e a Descrição do Item da Apuração em que foi realizado o lançamento na Apuração ICMS\-ST mais o Código do Ajuste ICMS\.

\(tabela ITEM\_APURAC\_SUB__ST__ – campo COD\_OPER\_APUR \+ 

 tabela OPERACAO\_APURACAO – campo DSC\_OPER\_APUR \+ 

 tabela ITEM\_APURAC\_SUB__ST__ – campo COD\_AJUSTE\_ICMS\)

Valor

Valor do lançamento realizado na Apuração do ICMS\-ST\.

\(tabela ITEM\_APURAC\_SUB__ST__ – campo VAL\_ITEM\_DISCRIM\)

= = = = = =


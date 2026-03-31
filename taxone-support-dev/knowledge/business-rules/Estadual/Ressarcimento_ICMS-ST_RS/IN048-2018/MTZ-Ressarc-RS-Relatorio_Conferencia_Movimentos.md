# MTZ-Ressarc-RS-Relatorio_Conferencia_Movimentos

- **Fonte:** MTZ-Ressarc-RS-Relatorio_Conferencia_Movimentos.docx
- **Modificado:** 2024-01-22
- **Tamanho:** 139 KB

---

THOMSON REUTERS

Módulo Ressarcimento de ICMS\-ST – RS \(IN\-RE 048/2018\) 

Relatório de Conferência dos Movimentos

<a id="_Hlk2155195"></a>__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\), menu Relatórios 🡪 IN\-RE 048/2018 🡪 Conferência dos Movimentos 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS28005

Liliane V\. Assaf

Criação do relatório de conferência do movimento de saída para consumidor final

18/07/2019

MFS28007

Liliane V\. Assaf

Alteração no relatório de conferência do movimento de Entrada \(Não varejista\) 

02/08/2019

MFS28009

Liliane V\. Assaf

Alteração no relatório de conferência do movimento de saída para consumidor final

02/08/2019

MFS28003

Liliane V\. Assaf

Alteração no relatório de conferência do movimento de Entrada \(varejista\)

02/08/2019

MFS28008

Liliane V\. Assaf

Alteração no relatório de conferência da subapuração

16/08/2019

MFS28011

Liliane V\. Assaf

Gerar Relatório das Saídas para Outras UF's, Isentas ou Não Tributadas \(Varejista\)

21/08/2019

MFS62415

Liliane V\. Assaf

Tópicos 6 e 7 para alteração nos labels de alguns campos\.

21/08/2021

__MFS47349__

Liliane Videira Assaf

Tratamento de Produtos Associados na geração dos movimentos

30/03/2021

__MFS81764__

Liliane Videira Assaf

Criação da Geração da Parcela do Crédito das Mercadorias em Estoque

03/03/2022

__MFS81804__

Liliane Assaf

Tratamento das Devoluções de Saídas de Mercadorias destinadas a Consumidor Final

07/03/2022

__MFS591083__

Liliane Assaf

Tratamento das Incorporações de Empresas/Estabelecimentos

22/01/2024

Sumário

[1\.	Regras Gerais	1](#_Toc97911717)

[2\.	Layout da Tela	1](#_Toc97911718)

[3\.	Regras de Funcionamento dos Campos	1](#_Toc97911719)

[4\.	Relatório de Conferência das Saídas para Consumidor Final	1](#_Toc97911720)

[4\.1 – Recuperação dos Registros:	1](#_Toc97911721)

[4\.2 – Layout e Preenchimento dos Campos:	1](#_Toc97911722)

[5\.	Relatório de Conferência das Entradas \(Varejista\)	1](#_Toc97911723)

[5\.1 – Recuperação dos Registros:	1](#_Toc97911724)

[5\.2 – Layout e Preenchimento dos Campos:	1](#_Toc97911725)

[6\.	Relatório de Conferência das Entradas \(Não Varejista\)	1](#_Toc97911726)

[6\.1 – Recuperação dos Registros:	1](#_Toc97911727)

[6\.2 – Layout e Preenchimento dos Campos:	1](#_Toc97911728)

[7\.	Relatório de Conferência das Saídas para Outras Ufs, Isentas ou Não Tributadas \(Varejista\)	1](#_Toc97911729)

[7\.1 – Recuperação dos Registros:	1](#_Toc97911730)

[7\.2 – Layout e Preenchimento dos Campos:	1](#_Toc97911731)

[8\.	Relatório de Conferência das Subapurações	1](#_Toc97911732)

[7\.1 – Recuperação dos Registros:	1](#_Toc97911733)

[7\.2 – Layout e Preenchimento dos Campos:	1](#_Toc97911734)

[9\.	Relatório de Conferência da Parcela do Crédito das Mercadorias em Estoque	1](#_Toc97911735)

[4\.1 – Recuperação dos Registros:	1](#_Toc97911736)

[4\.2 – Layout e Preenchimento dos Campos:	1](#_Toc97911737)

[10\.	Relatório de Conferência das Devoluções de Saídas de Mercadorias destinadas a Consumidor Final	1](#_Toc97911738)

[4\.1 – Recuperação dos Registros:	1](#_Toc97911739)

[4\.2 – Layout e Preenchimento dos Campos:	1](#_Toc97911740)

# <a id="_Toc97911717"></a>Regras Gerais

Este relatório tem por objetivo demonstrar os movimentos de saída para consumidor final que compõem o cálculo do ressarcimento de ICMS\-ST do estado de RS\. Estes movimentos são gerados no menu “Geração > Geração dos Movimentos \(opção “Saídas para Consumidor Final”\), e posteriormente gravados no registro 1923 do arquivo magnético do SPED FISCAL\.

# <a id="_Toc97911718"></a>Layout da Tela

Período : \[ dd/aaaa \]

Geração por Inscrição Estadual Única \[ x \]

Entradas \(x \)

Saídas para Consumidor Final \( \)

Saídas para Outras UF’s, Isentas ou Não tributadas \(Varejistas\) \( \)

Devolução das Saídas de Mercadoria destinadas a Consumidor Final \( \) \[__MFS81804\]__

Parcela do Crédito das Mercadorias em Estoque \( \) \[__MFS81764__\]

Subapuração \( \)

Estabelecimentos:

Contribuinte Varejista \[x\] 

\[ x \] xxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx      

\[ y \] xxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx      

\[   \] xxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[   \] xxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# <a id="_Toc97911719"></a>Regras de Funcionamento dos Campos

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

Radion\-button

S

S

Relatórios disponíveis:

- Entradas 
- Saídas para Consumidor Final 
- Saídas para Outras UF’s, Isentas ou Não tributadas 
- Devolução das Saídas de Mercadoria destinadas a Consumidor Final \[__MFS81804\]__
- Parcela do Crédito das Mercadorias em Estoque \[__MFS81764__\]
- Subapuração

Só é permitida a seleção de um dos relatórios\.

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

<a id="_Hlk97643953"></a>

# <a id="_Toc97911720"></a>Relatório de Conferência das Saídas para Consumidor Final 

Este relatório será emitido caso a opção “Saída para Consumidor Final” tenha sido selecionada na tela\.

Pré\-requisito:

- Realizar a Geração do Movimento para Saída para Consumidor Final;

## <a id="_Toc97911721"></a>4\.1 – Recuperação dos Registros:

Será gerado um relatório para cada um dos estabelecimentos selecionados em tela\.

Origem dos dados:  \- Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS

\(ITEM\_APURAC\_SUBRS\_AJUSTE\)

                                   \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

 Critérios da recuperação da movimentação do período:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

- Indicador de Lançamento Digitado/calculado = ‘__2__’ \- lançamento gerado via processo de geração da saida a Consumidor Final\. 

O relatório apresentará os documentos fiscais de saída para consumidor final com seus itens de mercadorias com o valor do ajuste que foi calculado\.

O relatório é a conferência do resultado do processo de Geração do Movimento \(menu Geração >> Geração dos Movimentos\)\.  Para entender as regras de geração veja “*MTZ\-Ressarc\-RS\-Geracao\_Movimentos\.doc*”\.

Ao final, será exibido o valor total dos ajustes\. Este é valor do lançamento à débito na subapuração do ICMS\-ST e que será gerado no registro 1921 do SPED FISCAL\.

As regras de ordenação e preenchimento das colunas no relatório estão descritas no item a seguir\.

## <a id="_Toc97911722"></a>4\.2 – Layout e Preenchimento dos Campos:

Layout: vide planilha “__Layout\-Relatorios\-Conferencia__”, aba “__Saidas Consumidor Final__”\.

Ordenação dos movimentos:

- Data Fiscal; 
- Número Documento;
- Série
- Sub Série
- Número do Item

Preenchimento dos campos do relatório:

__Linhas de cabeçalho:__

Primeira linha de cabeçalho

Informações desta linha: 

\- Razão social da empresa;

\- Data da emissão do relatório;

\- Página do relatório;

Segunda linha de cabeçalho

Informações desta linha: 

\- Campo “Filial” – Código e razão social do estabelecimento em questão;

\- Inscrição estadual do estabelecimento na sua UF;

\- CNPJ do estabelecimento; 

Terceira linha de cabeçalho

Informações desta linha:

\- Título do relatório \(“Relatório de Conferência das Saídas para Consumidor Final deste Estado \(Varejistas e Não Varejistas\)”\); 

Quarta linha de cabeçalho

Período solicitado em tela \(mês e ano\);

__Linhas de Grupamento por Produto:__

Agrupar os registros lidos da Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS por Produto Principal, apresentando as seguintes informações:

Indicador do Produto e 

Código do Produto

__\[MFS47349\]__

Campos “01\- Indicador do Produto” e “02\-Código do Produto” da SAFX2013 referente ao Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – IND\_PROD\_PRINC, COD\_PROD\_PRINC

Campos “12\-Indicador do Produto” e “14\-Código do Produto” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Descrição do Produto

Campos “04\-Descrição do Produto” da SAFX2013 referente ao Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Redução BC \(%\)    

Campo “%Redução BC” parametrizado para o Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Parametrização do Produto disponível no módulo nas opções: por Código, NCM, CEST\.

Alíq Interna \(%\) 

Campo “Alíquota Interna” parametrizado para o Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Parametrização do Produto disponível no módulo nas opções: por Código, NCM, CEST\.

Alíq FCP \(%\) 

Campo “Alíquota FCP” parametrizado para o Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS

 \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Parametrização do Produto disponível no módulo nas opções: por Código, NCM, CEST\.

Unidade

Campo “14 \- Unidade de Medida” da SAFX2013 referente ao Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __COD\_MEDIDA\_DEST__

__Linhas de detalhamento dos movimentos:__

Data Fiscal

Campo “Data Fiscal” referente ao documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)

Número/Seríe/Sub Série 

Campos “08\-Número do Documento”, “09\-Série do Documento” e “10\-SubSérie do Documento” da SAFX07 referente ao documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Modelo

Campo “13\-Modelo de Documento” da SAFX07 referente ao documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Pessoa Fis/Jur \(Ind – Cód\)

Campos “06\-Indicador de Pessoa Fis/Jur” e “07\-Código de Pessoa Fis/Jur”da SAFX07 referente ao documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Item 

Campos “18\-Item da Nota Fiscal” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Produto

__\[MFS47349\]__

Campos “12\-Indicador do Produto” e “14\-Código do Produto” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – IND\_PRODUTO, COD\_PRODUTO

CFOP

Campos “22\-Código Fiscal” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Nat\. Oper\.

Campos “23\-Natureza de Operação” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Valor Contábil Item

Campos “64\-Valor Contábil do Item” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Valor da Base de Cálculo

Campo Valor da Base de Cálculo referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE \- VLR\_BASE\_CALC

Valor do ICMS

Campo Valor do ICMS referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE \- __VLR\_ICMS__

Valor do AMPARA

Campo Valor do ICMS referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE \- __VLR\_FECP\_ICMS\_ST__

Valor Ajuste

Campo Valor do ICMS referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE \- __VLR\_AJUSTE__

<a id="OLE_LINK38"></a><a id="OLE_LINK39"></a><a id="OLE_LINK40"></a>__Linha de total por Produto:__

Valor Total do Ajuste para o Produto

Totalização da coluna “*Valor Ajuste*” dos movimentos

__Linha de total por Estabelecimento:__

Valor Total do Ajuste à __Débito__ \(Código do Ajuste Sped Fiscal ZZZ\)

Onde:

ZZZ é o campo “Código do Ajuste ICMS” da tabela dos Ajustes da Subapuração do RS \(campo COD\_AJUSTE\_ICMS da  ITEM\_APURAC\_SUBRS\)\.

Equivale ao Codigo de Ajuste parametrizado em Dados Iniciais \(Tabela: EST\_ST\_RS\_DADOS\_INI \- COD\_AJUSTE\_ICMS\_SAIDA\_CF\)

Totalização da coluna “*Valor Ajuste*” dos movimentos

__Linha de Rodapé__:

Legenda

Valor da Base de Cálculo = Valor Contábil  x \(1 \-  %Redução BC\)

Valor do ICMS = Valor da Base de Cálculo x %Aliq Interna

Valor do AMPARA = Valor da Base de Cálculo x %Aliq FCP

Valor do Ajuste = ICMS \+ AMPARA

# <a id="_Toc97911723"></a>Relatório de Conferência das Entradas \(Varejista\) 

Este relatório será emitido caso a opçao “Entradas” tenha sido selecionada na tela e o contribuinte seja __varejista__\.

A indicação se o contribuinte é varejista ou não está na parametrização dos Dados Iniciais \(menu Parâmetros >> Dados Iniciais, tabela EST\_ST\_RS\_DADOS\_INI campo IND\_VAREJISTA\)\.

Pré\-requisito:

- Realizar a Geração do Movimento para Entrada\.

## <a id="_Toc97911724"></a>5\.1 – Recuperação dos Registros:

Será gerado um relatório para cada um dos estabelecimentos selecionados em tela\.

Origem dos dados:  \- Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS  

			\(ITEM\_APURAC\_SUBRS\_AJUSTE\)

                                   \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

 Critérios da recuperação da movimentação do período:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Única" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Única" marcado

- Indicador de Lançamento Digitado/calculado = __‘3’__ \- lançamento gerado via processo de geração das entradas 

O relatório apresentará os documentos fiscais de entrada com seus itens de mercadorias, com o valor do ajuste que foi calculado\.

O relatório é a conferência do resultado do processo de Geração do Movimento \(menu Geração >> Geração dos Movimentos\)\.  Para entender as regras de geração veja “*MTZ\-Ressarc\-RS\-Geracao\_Movimentos\.doc*”\.

Ao final, será exibido o valor total dos ajustes\. Este é valor do lançamento à crédito na subapuração do ICMS\-ST, e que será gerado no registro 1921 do SPED FISCAL\.

As regras de ordenação e preenchimento das colunas no relatório estão descritas no item a seguir\.

## <a id="_Toc97911725"></a>5\.2 – Layout e Preenchimento dos Campos:

Layout: vide planilha “__Layout\-Relatorios\-Conferencia__”, aba “__Entradas Varejista__”\.

Ordenação dos movimentos:

- Data Fiscal; 
- Número Documento;
- Série
- Sub Série
- Número do Item

Preenchimento dos campos do relatório:

__Linhas de cabeçalho:__

Primeira linha de cabeçalho

Informações desta linha: 

\- Razão social da empresa;

\- Data da emissão do relatório;

\- Página do relatório;

Segunda linha de cabeçalho

Informações desta linha: 

\- Campo “Filial” – Código e razão social do estabelecimento em questão;

\- Inscrição estadual do estabelecimento na sua UF;

\- CNPJ do estabelecimento; 

Terceira linha de cabeçalho

Informações desta linha:

\- Título do relatório \(“Relatório de Conferência das Entradas Sujeitas a ST \(Varejistas\)”\); 

Quarta linha de cabeçalho

Período solicitado em tela \(mês e ano\);

__Linhas de Grupamento por Produto:__

Agrupar os registros lidos da Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS por Produto Principal, apresentando as seguintes informações:

Indicador do Produto e 

Código do Produto

__\[MFS47349\]__

Campos “01\- Indicador do Produto” e “02\-Código do Produto” da SAFX2013 referente ao Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – IND\_PROD\_PRINC, COD\_PROD\_PRINC

Campos “12\-Indicador do Produto” e “14\-Código do Produto” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Descrição do Produto

Campos “04\-Descrição do Produto” da SAFX2013 referente ao Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\)

Unidade 

Campo “14 \- Unidade de Medida” da SAFX2013 referente ao Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\)

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __COD\_MEDIDA\_DEST__

__Linhas de detalhamento dos movimentos:__

Data Fiscal

Campo “Data Fiscal” referente ao documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\)

Número/Série/Sub Série 

Campos “08\-Número do Documento”, “09\-Série do Documento” e “10\-SubSérie do Documento” da SAFX07 referente ao documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\)

Modelo 

Campo “13\-Modelo de Documento” da SAFX07 referente ao documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\)

Pessoa Fis/Jur \(Ind – Cód\)

Campos “06\-Indicador de Pessoa Fis/Jur” e “07\-Código de Pessoa Fis/Jur”da SAFX07 referente ao documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\)

Item 

Campos “18\-Item da Nota Fiscal” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\)\.

Produto

__\[MFS47349\]__

Campos “12\-Indicador do Produto” e “14\-Código do Produto” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – IND\_PRODUTO, COD\_PRODUTO

CFOP

Campos “22\-Código Fiscal” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\)

Nat\. Oper\.

Campos “23\-Natureza de Operação” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\)

Valor Contábil Item

Campos “64\-Valor Contábil do Item” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\)

Valor do ICMS

Campo Valor do ICMS referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\)

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE \- __VLR\_ICMS__

Valor ICMS\-ST

Campo Valor do ICMS referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\)

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE \- __VLR\_ICMS\_ST__

Valor ICMS\-ST FECEP

Campo Valor do ICMS referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\)

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE \- __VLR\_FECP\_ICMS\_ST__

Valor Ajuste

Campo Valor do ICMS referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\)

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE \- __VLR\_AJUSTE__

__Linha de total por Produto:__

Valor Total do Ajuste para o Produto

Totalização da coluna “*Valor Ajuste*” dos movimentos

__Linha de total por Estabelecimento:__

Valor Total do Ajuste à __Crédito__ \(Código do Ajuste Sped Fiscal ZZZ\)

Onde:

ZZZ é o campo “Código do Ajuste ICMS” da tabela dos Ajustes da Subapuração do RS \(campo COD\_AJUSTE\_ICMS da  ITEM\_APURAC\_SUBRS\)\.

Equivale ao Codigo de Ajuste parametrizado em Dados Iniciais\( Tabela: EST\_ST\_RS\_DADOS\_INI \- COD\_AJUSTE\_ICMS\_ENTR\)

Totalização da coluna “*Valor Ajuste*” dos movimentos

# <a id="_Toc97911726"></a>Relatório de Conferência das Entradas \(Não Varejista\)

Este relatório será emitido caso a opção “Entradas” tenha sido selecionada na tela e o contribuinte seja __não__ __varejista__\.

A indicação se o contribuinte é varejista ou não está na parametrização dos Dados Iniciais \(menu Parâmetros >> Dados Iniciais, tabela EST\_ST\_RS\_DADOS\_INI campo IND\_VAREJISTA\)\.

Pré\-requisito:

- Realizar a Geração do Movimento para Saída para Consumidor Final;
- Realizar a Geração do Movimento para Entrada\.

## <a id="_Toc97911727"></a>6\.1 – Recuperação dos Registros:

Será gerado um relatório para cada um dos estabelecimentos selecionados em tela\.

Origem dos dados:  \- Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS

			\(ITEM\_APURAC\_SUBRS\_AJUSTE\)

                                   \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Critérios da recuperação da movimentação do período:

Recuperar os documentos fiscais de saída para consumidor final, com os seguintes critérios:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

- Indicador de Lançamento Digitado/calculado = __‘2’__ \- lançamento gerado via processo de geração da saída a Consumidor Final

Para cada documento fiscal de saída a consumidor final recuperado, buscar a nota fiscal de entrada relacionada a última compra do produto vendido naquela nota de saída\. Para isso, os seguintes critérios devem ser aplicados:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

- Campo interno da tabela \(ID\_REG\_AJUSTE\_REG\) = identificação do ajuste gerado para a nota de saída a consumidor final
- Indicador de Lançamento Digitado/calculado = __‘3’__ \- lançamento gerado via processo de geração das entradas 

A nota de entrada pode ou não ser encontrada\.

O relatório apresentará cada documento fiscal de saída para consumidor final com sua respectiva nota de entrada\.  Apresentará também os documentos fiscais de saída para consumidor final, cuja nota de entrada não foi encontrada\. 

O relatório demonstra o resultado do processo de Geração do Movimento \(menu Geração >> Geração dos Movimentos\)\.  Para entender as regras de geração veja “*MTZ\-Ressarc\-RS\-Geracao\_Movimentos\.doc*”\.

Os valores dos ajustes das notas de saídas são totalizados gerando o valor do lançamento à débito na subapuração do ICMS\-ST\. 

Da mesma forma, os valores dos ajustes das notas de entradas são totalizados gerando o valor do lançamento à crédito na subapuração\. 

Esses valores são demonstrados ao final do relatório, sendo totais por estabelecimento\.  

Ambos os lançamentos são apresentados no registro 1921 do SPED FISCAL\.

As regras de ordenação e preenchimento das colunas no relatório estão descritas no item a seguir\.

## <a id="_Toc97911728"></a>6\.2 – Layout e Preenchimento dos Campos:

Layout: vide planilha “__Layout\-Relatorios\-Conferencia__”, aba “__Entradas Não Varejista__”\.

Ordenação dos movimentos:

Campos relacionados à nota de saída a consumidor final:

- Data Fiscal; 
- Número Documento;
- Série
- Sub Série
- Número do Item

Preenchimento dos campos do relatório:

__Linhas de cabeçalho:__

Primeira linha de cabeçalho

Informações desta linha: 

\- Razão social da empresa;

\- Data da emissão do relatório;

\- Página do relatório;

Segunda linha de cabeçalho

Informações desta linha: 

\- Campo “Filial” – Código e razão social do estabelecimento em questão;

\- Inscrição estadual do estabelecimento na sua UF;

\- CNPJ do estabelecimento; 

Terceira linha de cabeçalho

Informações desta linha:

\- Título do relatório \(“Relatório de Conferência das Entradas Sujeitas a ST relacionadas às Saídas para Consumidor Final \(Não Varejistas\)”\); 

Quarta linha de cabeçalho

Período solicitado em tela \(mês e ano\);

__Linhas de Grupamento por Produto:__

Agrupar os registros lidos da Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS por Produto Principal, apresentando as seguintes informações:

Indicador do Produto e 

Código do Produto

__\[MFS47349\]__

Campos “01\- Indicador do Produto” e “02\-Código do Produto” da SAFX2013 referente ao Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – IND\_PROD\_PRINC, COD\_PROD\_PRINC

Campos “12\-Indicador do Produto” e “14\-Código do Produto” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Descrição do Produto

Campos “04\-Descrição do Produto” da SAFX2013 referente ao Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Unidade 

Campo “14 \- Unidade de Medida” da SAFX2013 referente ao Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __COD\_MEDIDA\_DEST__

Observação: Estamos considerando o produto da nota de saída, pois existe a situação apresentada no relatório da nota de saída não ter entrada relacionada\.

__Linhas de detalhamento dos movimentos:__

__Nota/Cupom Fiscal de Saída a Consumidor final__

Data

Campo “Data Fiscal” referente ao documento fiscal de __Saída__ gravada na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Número/Seríe/Sub Série 

Campos “08\-Número do Documento”, “09\-Série do Documento” e “10\-SubSérie do Documento” da SAFX07 referente ao documento fiscal de __Saída__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Item 

Campo “18\-Item da Nota Fiscal” da SAFX08 referente ao item de mercadoria do documento fiscal de __Saída__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)\.

Produto

__\[MFS47349\]__

Campos “12\-Indicador do Produto” e “14\-Código do Produto” da SAFX08 referente ao item de mercadoria do documento fiscal de __Saída__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – IND\_PRODUTO, COD\_PRODUTO

Qtd Item

Campo “24\-Quantidade” da SAFX08 referente ao item de mercadoria do documento fiscal de __Saída__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __QTDE\_ITEM__

Qtd Convertida

Campo “24\-Quantidade” da SAFX08 aplicada o Fator de Conversão de Unidades de Medidas, referente ao item de mercadoria do documento fiscal de __Saída__, gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __QTDE\_CONV__

Valor Ajuste

Campo Valor do ICMS referente ao item de mercadoria do documento fiscal de __Saída__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE \- __VLR\_AJUSTE__

__Nota Fiscal de Entrada__

Empresa

__\[MFS591083\] Tratamento das Incorporações de Empresas/Estabelecimentos:__

Campo “Código da Empresa de Origem” referente ao documento fiscal de __Entrada__ gravada na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Estab

__\[MFS591083\] Tratamento das Incorporações de Empresas/Estabelecimentos:__

Campo “Código do Estabelecimento de Origem” referente ao documento fiscal de __Entrada__ gravada na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Data

Campo “Data Fiscal” referente ao documento fiscal de __Entrada__ gravada na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Número/Seríe/Sub Série 

Campos “08\-Número do Documento”, “09\-Série do Documento” e “10\-SubSérie do Documento” da SAFX07 referente ao documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Item 

Campo “18\-Item da Nota Fiscal” da SAFX08 referente ao item de mercadoria do documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)\.

Produto

__\[MFS47349\]__

Campos “12\-Indicador do Produto” e “14\-Código do Produto” da SAFX08 referente ao item de mercadoria do documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – IND\_PRODUTO, COD\_PRODUTO

Pessoa Fis/Jur

Campos “06\- Indicador da Pessoa fis/jur”, “07\-Código da Pessoa fis/jur” da SAFX07 referente ao documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Qtd Item

Campo “24\-Quantidade” da SAFX08 referente ao item de mercadoria do documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __QTDE\_ITEM__

Qtd Convertida

Campo “24\-Quantidade” da SAFX08 aplicada o Fator de Conversão de Unidades de Medidas, referente ao item de mercadoria do documento fiscal de __Entrada__, gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __QTDE\_CONV__

Valor ICMS

Valor do ICMS \(campos 43, 80,225 da SAFX08\) referente ao item de mercadoria do documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __VLR\_ICMS__

Valor ICMS\-ST

Valor do ICMS \(campos 52, 145,133, 107 da SAFX08\) referente ao item de mercadoria do documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __VLR\_ICMS\_ST__

Valor FECEP \(ST\)

Valor do ICMS \(campo 140 da SAFX08\) referente ao item de mercadoria do documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __VLR\_FECEP\_ICMS\_ST__

Valor Unitário da Entrada

Valor Unitário calculado para o item de mercadoria do documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __VLR\_UNIT__

Valor Ajuste

Valor do Ajuste calculado para o item de mercadoria do documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_ Nao\_Varejista\)

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE \- __VLR\_AJUSTE__

__Linha de total por Produto:__

Valor Total do Ajuste para o Produto

Totalização da coluna “*Valor Ajuste*” dos movimentos de saída

Valor Total do Ajuste para o Produto

Totalização da coluna “*Valor Ajuste*” dos movimentos de entrada

__Linha de total por Estabelecimento:__

Valor Total do Ajuste à __Débito__ \(Código do Ajuste Sped Fiscal ZZZ\)

Onde:

ZZZ é o campo “Código do Ajuste ICMS” da tabela dos Ajustes da Subapuração do RS das notas de saída \(campo COD\_AJUSTE\_ICMS da  ITEM\_APURAC\_SUBRS\)\.

Equivale ao Codigo de Ajuste parametrizado em Dados Iniciais 

\(Tabela: EST\_ST\_RS\_DADOS\_INI \- COD\_AJUSTE\_ICMS\_SAIDA\_CF\)

Totalização da coluna “*Valor Ajuste*” dos movimentos de saída\.

Valor Total do Ajuste à __Crédito__ \(Código do Ajuste Sped Fiscal ZZZ\)

Onde:

ZZZ é o campo “Código do Ajuste ICMS” da tabela dos Ajustes da Subapuração do RS das notas de Entrada \(campo COD\_AJUSTE\_ICMS da  ITEM\_APURAC\_SUBRS\)\.

Equivale ao Codigo de Ajuste parametrizado em Dados Iniciais 

\(Tabela: EST\_ST\_RS\_DADOS\_INI \- COD\_AJUSTE\_ICMS\_ENTR\)

Totalização da coluna “*Valor Ajuste*” dos movimentos das entradas\.

Valor do Ressarcimento

Esta  linha deve ser apresentada ou omitida, de acordo com a regra:

Se Valor Total do Ajuste à Débito__ <__ Valor Total do Ajuste à Crédito, então:

     Apresentar esta linha com a diferença dos totais dos valores dos ajustes 

     Valor do Ressarcimento = \(Crédito \- Débito\)

Se Valor Total do Ajuste à Débito __= __Valor Total do Ajuste à Crédito, então:

     Apresentar a linha com Valor do Ressarcimento = zero\. 

Se Valor Total do Ajuste à Débito__ >__ Valor Total do Ajuste à Crédito, então:

     Omitir esta linha\.

Valor do Complemento

Esta  linha deve ser apresentada ou omitida, de acordo com a regra:

Se Valor Total do Ajuste à Débito __<__ Valor Total do Ajuste à Crédito, então:

     Omitir esta linha\.

Se Valor Total do Ajuste à Débito __= __Valor Total do Ajuste à Crédito, então:

     Apresentar a linha com Valor do Ressarcimento = zero\. 

Se Valor Total do Ajuste à Débito > Valor Total do Ajuste à Crédito, então:

     Apresentar esta linha com a diferença dos totais dos valores dos ajustes 

     Valor do Complemento = \(Débito \- Crédito\)

# <a id="_Toc97911729"></a>Relatório de Conferência das Saídas para Outras Ufs, Isentas ou Não Tributadas \(Varejista\)

Este relatório será emitido caso a opçao “Saídas para Outras UF’s, Isentas ou Não Tributadas” tenha sido selecionada na tela e o contribuinte seja __varejista__\.

A indicação se o contribuinte é varejista ou não está na parametrização dos Dados Iniciais \(menu Parâmetros >> Dados Iniciais, tabela EST\_ST\_RS\_DADOS\_INI campo IND\_VAREJISTA\)\.

## <a id="_Toc97911730"></a>7\.1 – Recuperação dos Registros:

Será gerado um relatório para cada um dos estabelecimentos selecionados em tela\.

Origem dos dados das Notas de Saída para outras Ufs, Isentas ou Não Tributadas

- Tabela dos Ajustes da Subapuração do RS \(registro 1921\) \- __ITEM\_APURAC\_SUBRS__
- Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(registro 1923\) \- __ITEM\_APURAC\_SUBRS\_AJUSTE__

            

Origem dos dados das Notas de Entrada

- Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(registro 1923\) \- __ITEM\_APURAC\_SUBRS\_AJUSTE__

Observação:

Notas de entrada __NÃO__ possui registro de lançamento correspondente na Tabela dos Ajustes da Subapuração do RS \(registro 1921\) \- __ITEM\_APURAC\_SUBRS __\(vide tópico 4 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Critérios da recuperação das Notas de Saída para outras Ufs, Isentas ou Não Tributadas:

Recuperar os documentos fiscais de saída para consumidor final, com os seguintes critérios:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Única" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Única" marcado

- Indicador de Lançamento Digitado/calculado = ‘__4’ __– lançamento gerado via processo de geração da saída para outras Ufs, Isentas ou Não Tributadas

Para cada documento fiscal de saída recuperado, buscar a nota fiscal de entrada relacionada a última compra do produto vendido naquela nota de saída\. 

Critérios da recuperação das Notas de Entrada:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

- Campo interno da tabela \(ID\_REG\_AJUSTE\_REG\) = identificação do ajuste gerado para a nota de saída
- Indicador de Lançamento Digitado/calculado = ‘__4’ __– lançamento gerado via processo de geração da saida para outras Ufs, Isentas ou Não Tributadas 

A nota de entrada pode ou não ser encontrada\.

O relatório apresentará cada documento fiscal de saída com sua respectiva nota de entrada\.  Apresentará também os documentos fiscais de saída, cuja nota de entrada não foi encontrada\. 

O relatório demonstra o resultado do processo de Geração do Movimento \(menu Geração >> Geração dos Movimentos\)\.  Para entender as regras de geração veja “*MTZ\-Ressarc\-RS\-Geracao\_Movimentos\.doc*”\.

Os valores dos ajustes das notas de saídas são totalizados gerando o valor do lançamento à débito na subapuração do ICMS\-ST\. 

Os valores dos ajustes das notas de entradas __NÃO__ são totalizados para gerar o valor do lançamento à crédito na subapuração\. 

Apenas o valor total dos ajustes das notas de Saída é demonstrado ao final do relatório por estabelecimento, pois será um lançamento apresentado no registro 1921 no SPED FISCAL\.  

As regras de ordenação e preenchimento das colunas no relatório estão descritas no item a seguir\.

## <a id="_Toc97911731"></a>7\.2 – Layout e Preenchimento dos Campos:

Layout: vide planilha “__Layout\-Relatorios\-Conferencia__”, aba “__Saídas outras UFs Varejista__”\.

Ordenação dos movimentos:

Campos relacionados à nota de saída a consumidor final:

- Data Fiscal; 
- Número Documento;
- Série
- Sub Série
- Número do Item

Preenchimento dos campos do relatório:

__Linhas de cabeçalho:__

Primeira linha de cabeçalho

Informações desta linha: 

\- Razão social da empresa;

\- Data da emissão do relatório;

\- Página do relatório;

Segunda linha de cabeçalho

Informações desta linha: 

\- Campo “Filial” – Código e razão social do estabelecimento em questão;

\- Inscrição estadual do estabelecimento na sua UF;

\- CNPJ do estabelecimento; 

Terceira linha de cabeçalho

Informações desta linha:

\- Título do relatório \(“Relatório de Conferência das Saídas para Outras UF's, Isentas ou Não Tributadas \(Varejistas\)”\); 

Quarta linha de cabeçalho

Período solicitado em tela \(mês e ano\);

__Linhas de Grupamento por Produto:__

Agrupar os registros lidos da Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS por Produto Principal, apresentando as seguintes informações:

, apresentando as seguintes informações:

Indicador do Produto e 

Código do Produto

__MFS47349\]__

Campos “01\- Indicador do Produto” e “02\-Código do Produto” da SAFX2013 referente ao Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – IND\_PROD\_PRINC, COD\_PROD\_PRINC

Campos “12\-Indicador do Produto” e “14\-Código do Produto” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Descrição do Produto

Campos “04\-Descrição do Produto” da SAFX2013 referente ao item de mercadoria do documento fiscal de __Saída__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS 

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Unidade 

Campo “14 \- Unidade de Medida” da SAFX2013 referente ao item de mercadoria do documento fiscal de __Saída__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS 

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __COD\_MEDIDA\_DEST__

Observação: Estamos considerando o produto da nota de saída, pois existe a situação apresentada no relatório da nota de saída não ter entrada relacionada\.

__Linhas de detalhamento dos movimentos:__

__Nota/Cupom Fiscal de Saída__

Data

Campo “Data Fiscal” referente ao documento fiscal de __Saída__ gravada na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Número/Seríe/Sub Série 

Campos “08\-Número do Documento”, “09\-Série do Documento” e “10\-SubSérie do Documento” daSAFX07 referente ao documento fiscal de __Saída__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\.

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Item 

Campo “18\-Item da Nota Fiscal” da SAFX08 referente ao item de mercadoria do documento fiscal de __Saída__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\.

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Produto

__\[MFS47349\]__

Campos “12\-Indicador do Produto” e “14\-Código do Produto” da SAFX08 referente ao item de mercadoria do documento fiscal de __Saída__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – IND\_PRODUTO, COD\_PRODUTO

Qtd Item

Campo “24\-Quantidade” da SAFX08 referente ao item de mercadoria do documento fiscal de __Saída__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __QTDE\_ITEM__

Qtd Convertida

Campo “24\-Quantidade” da SAFX08 aplicada o Fator de Conversão de Unidades de Medidas, referente ao item de mercadoria do documento fiscal de __Saída__, gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __QTDE\_CONV__

Valor Ajuste

Campo Valor do ICMS referente ao item de mercadoria do documento fiscal de __Saída__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\.

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE \- __VLR\_AJUSTE__

__Nota Fiscal de Entrada__

Empresa

__\[MFS591083\] Tratamento das Incorporações de Empresas/Estabelecimentos:__

Campo “Código da Empresa de Origem” referente ao documento fiscal de __Entrada__ gravada na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Estab

__\[MFS591083\] Tratamento das Incorporações de Empresas/Estabelecimentos:__

Campo “Código do Estabelecimento de Origem” referente ao documento fiscal de __Entrada__ gravada na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Data

Campo “Data Fiscal” referente ao documento fiscal de __Entrada__ gravada na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Número/Seríe/Sub Série 

Campos “08\-Número do Documento”, “09\-Série do Documento” e “10\-SubSérie do Documento” daSAFX07 referente ao documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\.

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Item 

Campo “18\-Item da Nota Fiscal” da SAFX08 referente ao item de mercadoria do documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\.

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Produto

__\[MFS47349\]__

Campos “12\-Indicador do Produto” e “14\-Código do Produto” da SAFX08 referente ao item de mercadoria do documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – IND\_PRODUTO, COD\_PRODUTO

Pessoa Fis/Jur

Campos “06\- Indicador da Pessoa fis/jur”, “07\-Código da Pessoa fis/jur” da SAFX07 referente ao documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\.

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Qtd Item

Campo “24\-Quantidade” da SAFX08 referente ao item de mercadoria do documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\.

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __QTDE\_ITEM__

Qtd Convertida

Campo “24\-Quantidade” da SAFX08 aplicada o Fator de Conversão de Unidades de Medidas, referente ao item de mercadoria do documento fiscal de __Entrada__, gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __QTDE\_CONV__

Valor ICMS

Valor do ICMS \(campos 43, 80,225 da SAFX08\) referente ao item de mercadoria do documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __VLR\_ICMS__

Valor ICMS\-ST

Valor do ICMS \(campos 52, 145,133, 107 da SAFX08\) referente ao item de mercadoria do documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __VLR\_ICMS\_ST__

Valor FECEP \(ST\)

Valor do ICMS \(campo 140 da SAFX08\) referente ao item de mercadoria do documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __VLR\_FECEP\_ICMS\_ST__

Valor Unitário da Entrada

Valor Unitário calculado para o item de mercadoria do documento fiscal de __Entrada__ gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __VLR\_UNIT__

__Linha de total por Produto:__

Valor Total do Ajuste para o Produto

Totalização da coluna “*Valor Ajuste*” dos movimentos de saída

__Linha de total por Estabelecimento:__

Valor Total do Ajuste à __Débito__ \(Código do Ajuste Sped Fiscal ZZZ\)

Onde:

ZZZ é o campo “Código do Ajuste ICMS” da tabela dos Ajustes da Subapuração do RS das notas de saída \(campo COD\_AJUSTE\_ICMS da  ITEM\_APURAC\_SUBRS\)\.

Equivale ao Codigo de Ajuste parametrizado em Dados Iniciais 

\(Tabela: EST\_ST\_RS\_DADOS\_INI \- COD\_AJUSTE\_ICMS\_SAIDA\_UF\)

Totalização da coluna “*Valor Ajuste*” dos movimentos de saída\.

# <a id="_Toc97911732"></a>Relatório de Conferência das Subapurações 

Este relatório será emitido caso a opção “Subapuração” tenha sido selecionada na tela e pode ser utilizado tanto para contribuintes varejistas como para não varejistas\. 

Pré\-requisito:

- Realizar a Geração do Movimento 

## <a id="_Toc97911733"></a>7\.1 – Recuperação dos Registros:

Será gerado um relatório para cada um dos estabelecimentos selecionados em tela\.

Origem dos dados:  \- Tabela dos Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\)

                                \- Tabela do Resumo da Subapuração do RS \(ICT\_SUB\_APURACAO\_RS\) 

                                   Vide tópico 3 dos documentos matrizes de geração do movimento:

                                   MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final

                                   MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Nao\_Varejista

                                   MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista

Critérios da recuperação da apuração do período:

Recuperar os documentos fiscais de saída para consumidor final, com os seguintes critérios:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

Todos os valores da tabela de Resumo da Subapuração são apresentados linha a linha no relatório\. Os lançamentos gravados na tabela de Ajustes da Subapuração do RS são apresentados logo abaixo dos valores de Outros Débitos, Estorno de Crédito, Outros Créditos e Deduções\. 

O relatório demonstra o resultado do processo de Geração do Movimento \(menu Geração >> Geração dos Movimentos\)\.  Para enterder as regras de geração veja “*MTZ\-Ressarc\-RS\-Geracao\_Movimentos\.doc*”\.

Os valores da tabela de Resumo da Subapuração são apresentados no registro 1920 do SPED FISCAL e os lançamentos da Tabela dos Ajustes da Subapuração do RS no registro 1921\.

As regras de ordenação e preenchimento das colunas no relatório estão descritas no item a seguir\.

## <a id="_Toc97911734"></a>7\.2 – Layout e Preenchimento dos Campos:

Layout: vide planilha “__Layout\-Relatorios\-Conferencia__”, aba “__SubApuração__”\.

Ordenação dos Ajustes:

- Operação da Apuração; 
- Número Lançamento;

Preenchimento dos campos do relatório:

__Linhas de cabeçalho:__

Primeira linha de cabeçalho

Informações desta linha: 

\- Razão social da empresa;

\- Data da emissão do relatório;

\- Página do relatório;

Segunda linha de cabeçalho

Informações desta linha: 

\- Campo “Filial” – Código e razão social do estabelecimento em questão;

\- Inscrição estadual do estabelecimento na sua UF;

\- CNPJ do estabelecimento; 

Terceira linha de cabeçalho

Informações desta linha:

\- Título do relatório \(“Relatório de Conferência da Subapuração”\); 

Quarta linha de cabeçalho

Período solicitado em tela \(mês e ano\);

__Linhas de detalhamento:__

Débitos de Notas Fiscais

Campo “__Valor total dos débitos por “Saídas e prestações com débito do imposto__” gravado na tabela de Tabela do Resumo da Subapuração do RS \(ICT\_SUB\_APURACAO\_RS – campo VLR\_TOT\_DEB\)\. 

Outros Débitos

Campo “__Valor total de Ajustes a débitos__” gravado na tabela de Tabela do Resumo da Subapuração do RS \(ICT\_SUB\_APURACAO\_RS – campo VLR\_OUT\_DEB\)\.

Lançamentos em Outros Débitos

Recuperar os lançamentos da Tabela dos Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) cujo código de Operação da Apuração = ‘__002’__ – Outros Débitos\.

Apresentar a Descrição, o Código de Ajuste ICMS e o Valor do lançamento\.

Estornos de Créditos

Campo “__Valor total de Ajustes de Estornos de Crédito__” gravado na tabela de Tabela do Resumo da Subapuração do RS \(ICT\_SUB\_APURACAO\_RS – campo VLR\_ESTORNO\_CRED\)\.

Lançamento em Estornos de Créditos

Recuperar os lançamentos da Tabela dos Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) cujo código de Operação da Apuração = ‘__003’__ – Estorno de Créditos\.

Apresentar a Descrição, o Código de Ajuste ICMS e o Valor do lançamento\.

Total dos Débitos

Somatório das linhas:

\- Débitos de Notas Fiscais

\- Outros Débitos

\- Estornos de Créditos

Créditos de Notas Fiscais

Campo “__Valor total dos créditos por Entradas e aquisições com crédito do imposto__” gravado na tabela de Tabela do Resumo da Subapuração do RS \(ICT\_SUB\_APURACAO\_RS – campo VLR\_TOT\_CRED\)\.

Outros Créditos

Campo “__Valor total de Ajustes a créditos__” gravado na tabela de Tabela do Resumo da Subapuração do RS \(ICT\_SUB\_APURACAO\_RS – campo VLR\_OUT\_CRED\)\.

Lançamentos em Outros Créditos 

Recuperar os lançamentos da Tabela dos Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) cujo código de Operação da Apuração = ‘__006’__ – Outros Créditos\.

Apresentar a Descrição, o Código de Ajuste ICMS e o Valor do lançamento\.

Estornos de Débitos

Campo “__Valor total de Ajustes de Estorno de débitos__” gravado na tabela de Tabela do Resumo da Subapuração do RS \(ICT\_SUB\_APURACAO\_RS \- VLR\_ESTORNO\_DEB\)\.

Saldo Credor do Período Anterior

Campo “__Valor total de Saldo credor do período anterior__” gravado na tabela de Tabela do Resumo da Subapuração do RS \(ICT\_SUB\_APURACAO\_RS \-  campo VLR\_SALDO\_CRED\)\.

Total dos Créditos

Somatório das linhas:

\- Créditos de Notas Fiscais

 \- Outros Créditos

\- Estornos de Débitos

\- Saldo Credor do Período Anterior

Saldo Apurado

Campo “__Valor do saldo devedor apurado__” gravado na tabela de Tabela do Resumo da Subapuração do RS \(ICT\_SUB\_APURACAO\_RS – campo VLR\_SLD\_APURADO\)\.

Deduções

Campo “__Valor total de deduções__” gravado na tabela de Tabela do Resumo da Subapuração do RS \(ICT\_SUB\_APURACAO\_RS – campo VLR\_TOT\_DED\)\.

Lançamentos em Deduções

Recuperar os lançamentos da Tabela dos Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) cujo código de Operação da Apuração = ‘__012’__ – Deduções\.

Apresentar a Descrição, o Código de Ajuste ICMS e o Valor do lançamento\.

ICMS a Recolher

Campo “__Valor total de ICMS a recolher”__ gravado na tabela de Tabela do Resumo da Subapuração do RS \(ICT\_SUB\_APURACAO\_RS – campo VLR\_ICMS\_RECOLHER\)\.

Saldo Credor a Transportar

Campo “__Valor total do Saldo credor a transportar para o período seguinte__” gravado na tabela de Tabela do Resumo da Subapuração do RS \(ICT\_SUB\_APURACAO\_RS \-  campo VL\_SLD\_CREDOR\_TRANSP\)\.

Débitos Especiais

Campo “__Valores recolhidos ou a recolher, extraapuração__” gravado na tabela de Tabela do Resumo da Subapuração do RS \(ICT\_SUB\_APURACAO\_RS \-  campo VLR\_DEB\_ESP\)\.

# <a id="_Toc97911735"></a>Relatório de Conferência da Parcela do Crédito das Mercadorias em Estoque

__\[MFS81764\]__ Criação do Relatório

Este relatório será emitido caso a opção “Parcela do Crédito das Mercadorias em Estoque” tenha sido selecionada na tela\.

Pré\-requisito:

- Realizar a Geração do Movimento para Parcela do Crédito das Mercadorias em Estoque \(menu: Geração 🡪 IN\-RE 048/2018 🡪 Geração dos Movimentos \);

## <a id="_Toc97911736"></a>4\.1 – Recuperação dos Registros:

Será gerado um relatório para cada um dos estabelecimentos selecionados em tela\.

Origem dos dados:  \- Tabela de Identificação dos Produtos Inventariados \(ITEM\_APURAC\_SUBRS\_INVENT\)

                                \- Tabela dos Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\)

                                   \(vide tópicos 3 e 4 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Estoque\)\.

                                 

 Critérios da recuperação da movimentação do período:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  
-                              "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado
- Indicador de Lançamento Digitado/calculado = ‘__6’__ \- lançamento gerado via processo de geração da parcela do crédito das mercadorias em estoque\. 
- A ligação entre as tabelas ITEM\_APURAC\_SUBRS e ITEM\_APURAC\_SUBRS\_INVENT deve ser feita através dos campos:
	- Código da Empresa \(COD\_EMPRESA\)
	- Código do Estabelecimento \(COD\_ESTAB\)
	- Data da Apuração \(DAT\_APURACAO\)
	- Código do Livro \(COD\_TIPO\_LIVRO\)
	- Identificador da Subapuração \(IND\_SUB\_APUR\)
	- Número do Lançamento \(NUM\_DISCRIMINACAO\)

O relatório apresentará registro a registros de inventário que foi recuperado da tabela ITEM\_APURAC\_SUBRS\_INVENT\.

O relatório é a conferência do resultado do processo de Geração do Movimento \(menu Geração >> Geração dos Movimentos\)\.  Para entender as regras de geração veja “*MTZ\-Ressarc\-RS\-Geracao\_Movimentos\.doc*”\.

Ao final, será exibido o valor do lançamento recuperado tabela dos Ajustes da Subapuração do RS \(campo VAL\_ITEM\_DISCRIM da  ITEM\_APURAC\_SUBRS\) \. Este é valor do lançamento à crédito na subapuração do ICMS\-ST e que será gerado no registro 1921 do SPED FISCAL\.

As regras de ordenação e preenchimento das colunas no relatório estão descritas no item a seguir\.

## <a id="_Toc97911737"></a>4\.2 – Layout e Preenchimento dos Campos:

Layout: vide planilha “__Layout\-Relatorios\-Conferencia__”, aba “__Parcela Crédito Estoque__”\.

Ordenação dos movimentos de inventário:

- Data Inventário; 
- Produto \(Indicador\-Código\);
- Grupo Contagem
- Natureza Estoque

Preenchimento dos campos do relatório:

__Linhas de cabeçalho:__

Primeira linha de cabeçalho

Informações desta linha: 

\- Razão social da empresa;

\- Data da emissão do relatório;

\- Página do relatório;

Segunda linha de cabeçalho

Informações desta linha: 

\- Campo “Filial” – Código e razão social do estabelecimento em questão;

\- Inscrição estadual do estabelecimento na sua UF;

\- CNPJ do estabelecimento; 

Terceira linha de cabeçalho

Informações desta linha:

\- Título do relatório \(“Relatório de Conferência da Parcela do Crédito das Mercadorias em Estoque”\); 

Quarta linha de cabeçalho

Período solicitado em tela \(mês e ano\);

__Linhas de detalhamento dos movimentos de inventário:__

Data Inventário

Campo “Data Inventário” referente ao registro de inventário gravado na tabela de Tabela de Identificação dos Produtos Inventariados

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Estoque\)

Tabela ITEM\_APURAC\_SUBRS\_INVENT – DATA\_INVENTARIO

Produto 

Campos “Indicador do Produto” \+ “Código do Produto” referente ao registro de inventário gravado na tabela de Tabela de Identificação dos Produtos Inventariados

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Estoque\)\.

Forma de apresentação: Indicador do Produto \+ ‘\-‘ \+ Código do Produto

Tabela ITEM\_APURAC\_SUBRS\_INVENT – IND\_PRODUTO, COD\_PRODUTO

Grupo Contágem

Campo “Grupo Contágem” referente ao registro de inventário gravado na tabela de Tabela de Identificação dos Produtos Inventariados

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Estoque\)

Tabela ITEM\_APURAC\_SUBRS\_INVENT – GRUPO\_CONTAGEM

Natureza Estoque

Campo “Natureza do Estoque” referente ao registro de inventário gravado na tabela de Tabela de Identificação dos Produtos Inventariados

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Estoque\)

Tabela ITEM\_APURAC\_SUBRS\_INVENT – COD\_NAT\_ESTOQUE

Valor ICMS 

Campo “Valor do ICMS” referente ao registro de inventário gravado na tabela de Tabela de Identificação dos Produtos Inventariados

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Estoque\)

Tabela ITEM\_APURAC\_SUBRS\_INVENT – VLR\_ICMS

__Linha de total por Estabelecimento:__

Somatório do Valor ICMS

Totalizar o campo “Valor do ICMS” dos registros de inventário gravados na Tabela de Identificação dos Produtos Inventariados \(ITEM\_APURAC\_SUBRS\_INVENT\)

Valor Total do Ajuste à Crédito \(Código do Ajuste Sped Fiscal ZZZ\)

Onde:

ZZZ é o campo “Código do Ajuste ICMS” da tabela dos Ajustes da Subapuração do RS \(campo COD\_AJUSTE\_ICMS da  ITEM\_APURAC\_SUBRS\)\.

Equivale ao Codigo de Ajuste parametrizado em Dados Iniciais para “Lançamento de Outros Créditos para Mercadorias em Estoque” \(Tabela: EST\_ST\_RS\_DADOS\_INI\)

Apresentar o campo Valor do Lançamento da tabela dos Ajustes da Subapuração do RS \(campo VAL\_ITEM\_DISCRIM da  <a id="_Hlk97655346"></a>ITEM\_APURAC\_SUBRS\)

__Linha de Rodapé__:

Legenda

Valor Total do Ajuste à Crédito = Somatório do Valor ICMS /3

# <a id="_Toc97911738"></a>Relatório de Conferência das Devoluções de Saídas de Mercadorias destinadas a Consumidor Final 

\[MFS81804\] Criação do relatório: 

Para criar este relatório tomar como base o relatório da Saída para Consumidor Final, só que considerar o IND\_DIG\_CALCULADO = ‘7’ ao invés de ‘2’

Este relatório será emitido caso a opção “Devolução das Saídas de Mercadoria destinadas a Consumidor Final” tenha sido selecionada na tela\.

Pré\-requisito:

- Realizar a Geração do Movimento para Devolução de Saída de Mercadoria destinada a Consumidor Final;

## <a id="_Toc97911739"></a>4\.1 – Recuperação dos Registros:

Será gerado um relatório para cada um dos estabelecimentos selecionados em tela\.

Origem dos dados:  \- Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS

\(ITEM\_APURAC\_SUBRS\_AJUSTE\)

                                   \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

 Critérios da recuperação da movimentação do período:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

- Indicador de Lançamento Digitado/calculado = ‘__7 __– lançamento gerado via processo de geração da devolução das saidas para consumidor final\. 

O relatório apresentará os documentos fiscais de devolução de saída para consumidor final com seus itens de mercadorias com o valor do ajuste que foi calculado\.

O relatório é a conferência do resultado do processo de Geração do Movimento \(menu Geração >> Geração dos Movimentos\)\.  Para entender as regras de geração veja “*MTZ\-Ressarc\-RS\-Geracao\_Movimentos\.doc*”\.

Ao final, será exibido o valor total dos ajustes\. Este é valor do lançamento à __crédito__ na subapuração do ICMS\-ST e que será gerado no registro 1921 do SPED FISCAL\.

As regras de ordenação e preenchimento das colunas no relatório estão descritas no item a seguir\.

## <a id="_Toc97911740"></a>4\.2 – Layout e Preenchimento dos Campos:

Layout: vide planilha “__Layout\-Relatorios\-Conferencia__”, aba “ __Devol\. Saida Consumidor Final__”\.

Ordenação dos movimentos:

- Data Fiscal; 
- Número Documento;
- Série
- Sub Série
- Número do Item

Preenchimento dos campos do relatório:

__Linhas de cabeçalho:__

Primeira linha de cabeçalho

Informações desta linha: 

\- Razão social da empresa;

\- Data da emissão do relatório;

\- Página do relatório;

Segunda linha de cabeçalho

Informações desta linha: 

\- Campo “Filial” – Código e razão social do estabelecimento em questão;

\- Inscrição estadual do estabelecimento na sua UF;

\- CNPJ do estabelecimento; 

Terceira linha de cabeçalho

Informações desta linha:

\- Título do relatório \(“Relatório de Conferência das Devoluções de Saídas para Consumidor Final deste Estado \(Varejistas e Não Varejistas\)”\); 

Quarta linha de cabeçalho

Período solicitado em tela \(mês e ano\);

__Linhas de Grupamento por Produto:__

Agrupar os registros lidos da Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS por Produto Principal, apresentando as seguintes informações:

Indicador do Produto e 

Código do Produto

__\[MFS47349\]__

Campos “01\- Indicador do Produto” e “02\-Código do Produto” da SAFX2013 referente ao Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – IND\_PROD\_PRINC, COD\_PROD\_PRINC

Descrição do Produto

Campos “04\-Descrição do Produto” da SAFX2013 referente ao Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

Redução BC \(%\)    

Campo “%Redução BC” parametrizado para o Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

Parametrização do Produto disponível no módulo nas opções: por Código, NCM, CEST\.

Alíq Interna \(%\) 

Campo “Alíquota Interna” parametrizado para o Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

Parametrização do Produto disponível no módulo nas opções: por Código, NCM, CEST\.

Alíq FCP \(%\) 

Campo “Alíquota FCP” parametrizado para o Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS

 \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

Parametrização do Produto disponível no módulo nas opções: por Código, NCM, CEST\.

Unidade

Campo “14 \- Unidade de Medida” da SAFX2013 referente ao Produto Principal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – __COD\_MEDIDA\_DEST__

__Linhas de detalhamento dos movimentos:__

Data Fiscal

Campo “Data Fiscal” referente ao documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\. 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)

Número/Seríe/Sub Série 

Campos “08\-Número do Documento”, “09\-Série do Documento” e “10\-SubSérie do Documento” da SAFX07 referente ao documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS\.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

Modelo

Campo “13\-Modelo de Documento” da SAFX07 referente ao documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

Pessoa Fis/Jur \(Ind – Cód\)

Campos “06\-Indicador de Pessoa Fis/Jur” e “07\-Código de Pessoa Fis/Jur”da SAFX07 referente ao documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS 

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

Item 

Campos “18\-Item da Nota Fiscal” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

Produto

__\[MFS47349\]__

Campos “12\-Indicador do Produto” e “14\-Código do Produto” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE – IND\_PRODUTO, COD\_PRODUTO

CFOP

Campos “22\-Código Fiscal” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

Nat\. Oper\.

Campos “23\-Natureza de Operação” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

Valor Contábil Item

Campos “64\-Valor Contábil do Item” da SAFX08 referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

Valor da Base de Cálculo

Campo Valor da Base de Cálculo referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE \- VLR\_BASE\_CALC

Valor do ICMS

Campo Valor do ICMS referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE \- __VLR\_ICMS__

Valor do AMPARA

Campo Valor do ICMS referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE \- __VLR\_FECP\_ICMS\_ST__

Valor Ajuste

Campo Valor do ICMS referente ao item de mercadoria do documento fiscal gravado na tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \.

\(vide tópico 3 do documento MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\)\.

Tabela ITEM\_APURAC\_SUBRS\_AJUSTE \- __VLR\_AJUSTE__

__Linha de total por Produto:__

Valor Total do Ajuste para o Produto

Totalização da coluna “*Valor Ajuste*” dos movimentos

__Linha de total por Estabelecimento:__

Valor Total do Ajuste à __Crédito__ \(Código do Ajuste Sped Fiscal ZZZ\)

Onde:

ZZZ é o campo “Código do Ajuste ICMS” da tabela dos Ajustes da Subapuração do RS \(campo COD\_AJUSTE\_ICMS da  ITEM\_APURAC\_SUBRS\)\.

Totalização da coluna “*Valor Ajuste*” dos movimentos

__Linha de Rodapé__:

Legenda

Valor da Base de Cálculo = Valor Contábil  x \(1 \-  %Redução BC\)

Valor do ICMS = Valor da Base de Cálculo x %Aliq Interna

Valor do AMPARA = Valor da Base de Cálculo x %Aliq FCP

Valor do Ajuste = ICMS \+ AMPARA

= = = = = =


# MTZ-LAIPI-Lancamento _no_Livro_de_Apuracao

- **Fonte:** MTZ-LAIPI-Lancamento _no_Livro_de_Apuracao.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 70 KB

---

THOMSON REUTERS

Módulo Lançamentos Automáticos do IPI

Rotina de Gravação dos Lançamento Calculados na Apuração do IPI

__Localização__: Menu Federal, módulo Lançamentos Automáticos do IPI”, menu Lançamentos 🡪 Lançamentos no Livro de Apuração 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS17499__

<a id="OLE_LINK12"></a><a id="OLE_LINK13"></a><a id="OLE_LINK14"></a>Alteração para considerar as informações dos documentos fiscais vinculados\.

<a id="OLE_LINK15"></a><a id="OLE_LINK19"></a>Alteração na gravação dos lançamentos no P8, para gravar também os documentos fiscais vinculados que foram gerados no cálculo do lançamento\. 

26/04/2018 

\(criação do documento\)

Sumário

[1\.	Parâmetros da Tela	2](#_Toc512589366)

[2\.	Recuperação dos Dados e Processamento	3](#_Toc512589367)

[3\.	Gravação dos Lançamentos na Apuração do IPI	3](#_Toc512589368)

# <a id="_Toc512589366"></a>Parâmetros da Tela 

Esta rotina recupera os lançamentos gravados na FDT\_LANCTO\_P8 \(no menu “Cálculo dos Lançamentos”\), e grava na tabela dos lançamentos complementares da Apuração do IPI \(__ITEM\_APURAC\_DISCR__\)\.

Alteração __MFS17499__: 

Além de gravar os lançamentos na tabela __ITEM\_APURAC\_DISCR__, esta rotina foi alterada para gravar também as informações dos documentos fiscais vinculados ao lançamento na tabela __ITEM\_APURAC\_DISCR\_AJUSTE__\.

Esta alteração foi necessária porque o lançamento do tipo “__Matérias Primas referente às Devoluções__” foi alterado para gerar de forma automática os documentos fiscais vinculados\. Essas informações são gravadas numa tabela “filha” da FDT\_LANCTO\_P8\.

# <a id="_Toc350763252"></a><a id="_Toc512589367"></a>Recuperação dos Dados e Processamento

# <a id="_Toc512589368"></a>Gravação dos Lançamentos na Apuração do IPI

__Gravação dos lançamentos na ITEM\_APURAC\_DISCR:__

Alteração __MFS17499__: Devido à alteração no cálculo do lançamento “*Matérias Primas referente às Devoluções*” para gerar os documentos vinculados, foi necessário alterar a gravação do lançamento na ITEM\_APURAC\_DISCR, conforme descrito a seguir:

Sempre que o lançamento a ser gravado na ITEM\_APUREAC\_DISCR __tiver documentos fiscais vinculados informados na tabela “filha” da FDT\_LANCTO\_P8__, a coluna ORIGEM\_PROC será gravada da seguinte forma:

__ITEM\_APURAC\_DISCR__

__Conteúdo__

ORIGEM\_PROC

= __3__

\(indica lançamento originado de NF’s\)

\(ver OBS abaixo\)

Obs\.: Na tela dos lançamentos complementares da Apuração do IPI, os lançamentos que têm documentos fiscais vinculados devem ter o campo ORIGEM\_PROC = 3 \(na tela é o campo “Origem” do quadro “Documento Vinculado ao Ajuste”\)\. Caso contrário, a opção “*Documentos Fiscais Vinculados \(Sped Fiscal – Reg\. E531\)*” fica desabilitada\.

__Gravação dos documentos vinculados na ITEM\_APURAC\_DISCR\_AJUSTE:__

A gravação destes dados foi implementada na __MFS17499__, quando o lançamento “*Matérias Primas referente às Devoluções*” foi alterado para gerar de forma automática os documentos fiscais vinculados\. 

O preenchimento destas informações \(originadas da tabela “filha” da FDT\_LANCTO\_P8\) na tabela dos documentos fiscais vinculados do Livro de Apuração do IPI \(tabela __ITEM\_APURAC\_DISCR\_AJUSTE__\) é feito da seguinte forma:

__ITEM\_APURAC\_DISCR\_AJUSTE__

__Conteúdo__

__Origem Informação__

COD\_EMPRESA

Dados da chave do lançamento gravado na ITEM\_APURAC\_DISCR

ITEM\_APURAC\_DISCR

COD\_ESTAB

COD\_TIPO\_LIVRO

DAT\_APURACAO

COD\_OPER\_APUR

NUM\_DISCRIMINACAO

DATA\_FISCAL

Dados da chave do item do documento fiscal 

Tabela “filha” da FDT\_LANCTO\_P8 que contém as informações dos documentos ficais vinculados ao lançamento

MOVTO\_E\_S

NORM\_DEV

IDENT\_DOCTO

IDENT\_FIS\_JUR

NUM\_DOCFIS

SERIE\_DOCFIS

SUB\_SERIE\_DOCFIS

DISCRI\_ITEM

NUM\_ITEM

Número do item do documento fiscal

VLR\_AJUSTE

Valor do ajuste correspondente ao item

IND\_DIG\_CALCULADO

= __9__ 

\(indica lançamento gerado automaticamente pelo módulo Lançamentos Automáticos do ICMS ou IPI\)  

\(conteúdo fixo\)

	

= = = = = =

 


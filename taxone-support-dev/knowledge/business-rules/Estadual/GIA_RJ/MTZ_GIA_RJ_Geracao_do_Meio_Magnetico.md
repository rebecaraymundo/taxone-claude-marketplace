# MTZ_GIA_RJ_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_GIA_RJ_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 72 KB

---

THOMSON REUTERS

GIA\-RJ

Geração do Meio Magnético

__Localização__: Menu Estadual, Módulo GIA\-RJ, item Obrigações 🡪 Meio Magnético

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4694

Julyana Perrucini

Este documento tem como objetivo documentar a reversa do preenchimento dos campos “Valor da Base de Cálculo ST” e “Valor do Imposto Retido ST” do Registro 0120\.

MFS23922

Andréa Rocha

Inclusão do campo sequencial na tabela de manutenção do registro 0250\.

MFS15084

Liliane Assaf

Inclusão de relatório contendo os resumos: “Operações Próprias” e “Substituição Tributária Interna”\.

Sumário

[1\.	Regras Gerais	2](#_Toc962178)

[2\.	Layout da Tela	3](#_Toc962179)

[3\.	Regras de Funcionamento dos Campos	3](#_Toc962180)

[4\.	Recuperação dos Dados	4](#_Toc962181)

[5\.	Registro 0120 \- Preenchimento dos Campos:	6](#_Toc962182)

[6\.	Registro 0130 \- Preenchimento dos Campos:	7](#_Toc962183)

[7\.	Registro 0250 \- Preenchimento dos Campos:	8](#_Toc962184)

[8\.	Regras de Formatação do Arquivo:	10](#_Toc962185)

# <a id="_Toc962178"></a>Regras Gerais

Esta funcionalidade tem como objetivo gerar o meio magnético da GIA\-RJ e um relatório que auxilia na conferência composto por <a id="_Hlk961745"></a>dois resumos: das Operações Próprias e de Substituição Tributária Interna\.

<a id="_Hlk954943"></a>Mais de um estabelecimento pode ser selecionado para geração\.  <a id="_Hlk961873"></a>Nesse caso, vários arquivos do meio magnético são gravados, um para cada estabelecimento\. No caso do relatório, apenas um arquivo é gerado, contendo os resumos de todos os estabelecimentos\.

Ao final da geração o sistema disponibiliza:

\- O número do processo através do qual pode ser emitido o Relatório do Log do Processo onde podem ser conferidos erros ocorridos durante a geração\. 

\- O arquivo do meio magnético, gravado no subdiretório “DISCO01” do diretório informado na tela\. 

\- O arquivo do relatório de resumos, salvo no diretório informado na tela\. 

\- O relatório dos resumos na aba “Resumo Operações Próprias / ST Interna” para visualização em tela\.

A especificação para os Resumos está num documento matriz próprio: “MTZ\-GIA\-RJ\- Resumos Operações Próprias e ST Interna\.docx”\.

# <a id="_Toc962179"></a>Layout da Tela

Período:  \[ MM/AAAA \]

Versão:   \[ N\.N\.N\.N \]

Estabelecimento:

\[ \] Cód\. Estabelecimento – Razão Social

\[ \] Cód\. Estabelecimento – Razão Social

\[ \] Cód\. Estabelecimento – Razão Social

Diretório:    \[                                                  \]

Arquivo:      \[GIARJ\.gia                                 \]

Arquivo Resumos:    \[RESUMOS\.psr                         \]

# <a id="_Toc962180"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato / Default__

__Regra__

Período

Numérico

S

S

Mês/Ano

Campo onde deve ser informado o mês e ano da declaração\.

Estabelecimento

S

S

Seleção de um ou vários estabelecimentos\.

<a id="_Hlk525829679"></a>Diretório

Texto

S

S

Campo onde deve ser informado o caminho do diretório onde o arquivo magnético e o relatório será salvo\.

Arquivo

Texto

S

S

GIARJ\.gia

Campo onde deve ser informado o nome do arquivo a ser gravado\.

Arquivo Resumos

Texto

S

S

RESUMOS\.psr

Campo onde deve ser informado o nome do relatório a ser gravado\. O formato do arquivo será sempre psr\.

# <a id="_Toc962181"></a><a id="_Toc506457465"></a>Recuperação dos Dados

Recuperar os dados do __Parâmetro da Apuração da GIA__ \(vide menu Parâmetros >> Por Apuração da GIA\) considerando os seguintes critérios:

- Empresa de login
- Estabelecimento informados na Tela de Geração do Meio Magnético\.
- Período \(mês/ano\) informados na Tela de Geração do Meio Magnético\.

Com o Parâmetro da Apuração da Gia recuperado, fazer a recuperação os registros listados abaixo\. 

Tais registros são criados na Apuração Gia através da geração dos registros \(vide de menu Obrigações >> Geração >> Geração dos Registros\) ou digitados manualmente \(vide de menu Obrigações >> Manutenção\)\.

Recuperação dos Registros que compõe os resumos:

- Registro 0110 \- Registro de Identificação da Declaração:

__Origem:__

- Registro 0120 \- Movimentação de Entradas  

__Origem:__ Obrigações >> Manutenção >> Entradas e Saídas – Reg\. 0120 e 0130

- Registro 0130 \- Movimentação de Saídas     

__Origem:__  Obrigações >> Manutenção >> Entradas e Saídas – Reg\. 0120 e 0130

- Registro 0140 \- Movimentação de Outros débitos 

__Origem__: Obrigações >> Manutenção >> Estorno e Outros Deb/Cred\. Prazo Esp\., Outros ICMS Dev – Reg\. 0140 a 0200 

- Registro 0150 \- Movimentação de Estornos Crédito 

__Origem__: Obrigações >> Manutenção >> Estorno e Outros Deb/Cred\. Prazo Esp\., Outros ICMS Dev – Reg\. 0140 a 0200

- Registro 0160 \- Movimentação de Outros Créditos  

__Origem__: Obrigações >> Manutenção >> Estorno e Outros Deb/Cred\. Prazo Esp\., Outros ICMS Dev – Reg\. 0140 a 0200

- Registro 0170 \- Movimentação de Estornos Débito 

__Origem__: Obrigações >> Manutenção >> Estorno e Outros Deb/Cred\. Prazo Esp\., Outros ICMS Dev – Reg\. 0140 a 0200

- Registro 0180 \- Movimentação de Deduções

__Origem__: Obrigações >> Manutenção >> Estorno e Outros Deb/Cred\. Prazo Esp\., Outros ICMS Dev – Reg\. 0140 a 0200

- Registro 0200 \- Movimentação de Outros ICMS devido 

__Origem__:

- Registro 0210 \- Movimentação de Entradas Interestaduais

__Origem__:

- Registro 0210 \- Movimentação de Entradas Interestaduais

__Origem__:

- Registro 0220 \- Movimentação de Saídas Interestaduais

__Origem__:

- Registro 0230 \- Movimentação de Saídas para ZFM/ALC

__Origem__:

- Registro 0240 \- Movimentação de SCE Compensado entre Estabelecimentos

__Origem__:

- Registro 0250 \- Movimentação de SCE Compensado do Próprio

__Origem__:

- Registro 0260 \- Movimentação de SCE Recebido

__Origem__:

- Registro 0270 \- Movimentação de SCE Transferido

__Origem__:

- Registro

  
  


# <a id="_Toc171673"></a><a id="_Toc962182"></a>Registro 0120 \- Preenchimento dos Campos:

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN0120

__Regra Geral – Registro 0120__

A geração do registro é baseada na tabela de manutenção dos registros 0120 e 0130 \(Obrigações >> Manutenção >> Entradas e Saídas – Reg\. 0120 e 0130\)\. 

Serão recuperados os registros filtrando por:

\- Empresa

\- Estabelecimento

\- Mês e ano da apuração

\- Tipo Registro = 0120 \- Entradas

OS4694

RN0120\-09

__Campo Valor da Base de Cálculo ST:__

__Origem:__ Estadual >> GIA\-RJ >> Obrigações >> Manutenção >> Entradas e Saídas – Reg\. 0120 e 0130\.

- Para cada CFOP gerar uma linha em que o campo Valor da Base de Cálculo ST recebe o conteúdo do campo “Valor Base ICMS\-ST”\.
- Se não houver valor para o CFOP gravar zeros\.

Características do campo

Tipo: Valor

Tamanho: 015

Posição inicial e final: 099 a 113

OS4694

RN0120\-10

__Campo Valor do Imposto Retido ST:__

__Origem:__ Estadual >> GIA\-RJ >> Obrigações >> Manutenção >> Entradas e Saídas – Reg\. 0120 e 0130\.

- Para cada CFOP gerar uma linha em que o campo Valor do Imposto Retido ST recebe o conteúdo do campo “Valor ICMS\-ST”\.
- Se não houver valor para o CFOP gravar zeros\.

Características do campo

Tipo: Valor

Tamanho: 015

Posição inicial e final: 114 a 128

OS4694

  


# <a id="_Toc962183"></a>Registro 0130 \- Preenchimento dos Campos:

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN0130

__Regra Geral – Registro 0130__

A geração do registro é baseada na tabela de manutenção dos registros 0120 e 0130 \(Obrigações >> Manutenção >> Entradas e Saídas – Reg\. 0120 e 0130\)\. 

Serão recuperados os registros filtrando por:

\- Empresa

\- Estabelecimento

\- Mês e ano da apuração

\- Tipo Registro = 0130 \- Saídas

OS4694

RN0130\-01

OS4694

# <a id="_Toc962184"></a>Registro 0250 \- Preenchimento dos Campos:

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN0250

__Regra Geral – Registro 0250__

A geração do registro é baseada na tabela de manutenção do registro 0250 \(Obrigações >> Manutenção >> SCE Compensado do Próprio – Reg\. 0250\)\. 

Serão recuperados os registros filtrando por:

\- Empresa

\- Estabelecimento

\- Mês e ano da apuração

MFS23922

RN0250\-01

__Campo Subtipo:__

__Origem:__ gravar fixo ‘0250’\.

Características do campo

Tipo: Numérico

Tamanho: 004

Posição inicial e final: 001 a 004

MFS23922

RN0250\-02

__Campo Identificador da Declaração:__

__Origem:__ Campo Sequencial do registro 0250\.

Características do campo

Tipo: Numérico

Tamanho: 015

Posição inicial e final: 005 a 019

MFS23922

RN0250\-03

__Campo Sequencial de Ocorrência:__

__Origem:__ A partir do código do amparo legal do registro 0250, recuperar o código do amparo da GIA\-RJ correspondente na TACES43 \(Amparo/Texto/Ocorrência x Código GIA\-RJ\)\.

Características do campo

Tipo: Numérico

Tamanho: 005

Posição inicial e final: 020 a 024

MFS23922

RN0250\-04

__Campo Observação:__

__Origem:__ Campo Dado complementar do registro 0250\.

Características do campo

Tipo: Alfanumérico

Tamanho: 100

Posição inicial e final: 025 a 124

MFS23922

RN0250\-05

__Campo Valor Compensado:__

__Origem:__ Campo Valor compensado do registro 0250\.

Características do campo

Tipo: Valor

Tamanho: 015

Posição inicial e final: 125 a 139

MFS23922

RN0250\-06

__Campo Filler:__

__Origem:__ gravar fixo brancos\.

Características do campo

Tipo: Alfanumérico

Tamanho: 706

Posição inicial e final: 140 a 845

MFS23922

RN0250\-07

__Campo Contador de linha:__

__Origem:__ gerar contador do número de linhas do arquivo\.

Características do campo

Tipo: Numérico

Tamanho: 005

Posição inicial e final: 846 a 850

MFS23922

# <a id="_Toc962185"></a>Regras de Formatação do Arquivo:

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral:__

Observações:

- Campos do tipo Valor devem ser alinhados à direita e preenchidos com zeros à esquerda sendo os dois últimos dígitos à direita as casas decimais\.

OS4694

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


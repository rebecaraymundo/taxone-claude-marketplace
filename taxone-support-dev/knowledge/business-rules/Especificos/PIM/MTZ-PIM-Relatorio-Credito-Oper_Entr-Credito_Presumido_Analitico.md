# MTZ-PIM-Relatorio-Credito-Oper_Entr-Credito_Presumido_Analitico

- **Fonte:** MTZ-PIM-Relatorio-Credito-Oper_Entr-Credito_Presumido_Analitico.docx
- **Modificado:** 2022-06-27
- **Tamanho:** 90 KB

---

THOMSON REUTERS

__PIM \- Gestão do Controle de Incentivos Fiscais do Pólo Industrial de Manaus__

Localização 🡪 Menu: Específicos, Módulo: PIM, item: Relatórios >> Créditos \(Operações de Entradas\) >> Crédito Presumido \- Analítico

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS86300

Liliane Videira Assaf

Criação do Documento

27/06/2022

Sumário

[1\.	Parâmetros da Tela	1](#_Toc107239683)

[2\.	Origem e Recuperação dos Dados	1](#_Toc107239684)

[3\.	Processamento	1](#_Toc107239685)

[4\.	Layout e Regra de Preenchimento dos Campos do Relatório	1](#_Toc107239686)

# <a id="_Toc107239683"></a>Parâmetros da Tela 

__Tela deve ser desenvolvida em Framework\.__

__Aba Parâmetros__:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

Tipo de Execução: \( \) Imediata     \( \) Programada   Data/Hora de Execução \[ dd/mm/aaaa hh:mm \]                 \[Executar\]

Período: \[DD/MM/AAAA\] a \[DD/MM/AAAA\]

Estabelecimento – Inscrição Estadual:

\[ \] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \- xxxxxxxxxxxxxx

\[ \] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \- xxxxxxxxxxxxxx

\[ \] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \- xxxxxxxxxxxxxx

\[ \] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \- xxxxxxxxxxxxxx

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

	

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Período

Data

__S__

S

DD/MM/AAAA a

DD/MM/AAAA

Este campo deve ser preenchido com o primeiro e o último dia do período em que o cálculo do crédito presumido foi efetuado\.

Consistências:

1\) Deve ser uma data válida\.

2\) Caso os campos não sejam preenchidos, exibir mensagem na tela:

        “Informe o Período”

3\) O período deve ser no máximo de um mês\. Caso ultrapasse um mês, exibir mensagem:

“O período superior ao permitido\. Informar período máximo mensal”

        

Estabelecimento – Inscrição Estadual

Alfanumérico 

__S__

S

Neste campo é exibida a lista dos estabelecimentos da Empresa do login, com suas inscrições estaduais cadastradas no módulo PIM\.

Serão disponibilizados para seleção os estabelecimentos com suas Inscrições Estaduais cadastradas no menu “Cadastros > Inscrição Estadual por Estabelecimento” do módulo PIM, atendendo a “UF”\.

    Para montagem dessa listagem, fazer uma consulta envolvendo as tabelas:

    \- ESTABELECIMENTO, 

    \- ICT\_ESTAB\_IESTAD \(tabela de Inscrições Estaduais do PIM\)

    Considerar os critérios:

    \- Associar as tabelas ESTABELECIMENTO e ICT\_ESTAB\_IESTAD através dos campos COD\_EMPRESA, COD\_ESTAB\.

    Demonstrar os seguintes campos de forma concatenada, na listagem de estabelecimentos:

    \- COD\_ESTAB \+ RAZAO\_SOCIAL \+ INSC\_ESTADUAL

Selecionar

N

N

Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos/inscrição estadual através de uma janela de seleção da tabela de estabelecimentos\.

O filtro dos estabelecimentos/inscrições estaduais disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimento – Inscrição Estadual”:

Quando esta opção é utilizada, após escolher os estabelecimentos/inscrições estaduais e clicar no botão <OK> da janela de seleção, os estabelecimentos/inscrições estaduais selecionados pelo usuário serão demonstrados no campo “Estabelecimento – Inscrição Estadual” já marcados\. 

   

Marcar todos

N

N

Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos/inscrições estaduais demonstrados no campo “Estabelecimento – Inscrição Estadual”\.

__Pré\-requisito:__

\- Cálculo do Crédito Presumido \(menu Apuração => Cálculos dos Créditos \(Entradas\) => Crédito Presumido\)

# <a id="_Toc350763252"></a><a id="_Toc107239684"></a>Origem e Recuperação dos Dados 

Origem dos Dados: Tabela de Itens de Nota Fiscal para Relatório Analítico do Crédito Presumido \(ICT\_AM\_REL\_IES\_NF\_PRES\)

                                Tabela de Capa de Documentos Fiscals \(DWT\_DOCTO\_FISCAL\);

                                Tabela de Itens de Mercadoria \(DWT\_ITENS\_MERC\);

  

Critérios de recuperação:

\- Código da Empresa – Empresa do login;

\- Código do Estabelecimento – Estabelecimento informado na tela de geração;

\- Inscrição Estadual \(campo INSC\_ESTADUAL \- item 126 da SAFX07\) = Inscrição Estadual PIM informada na tela de geração;

\- Data Início da ICT\_AM\_REL\_IES\_NF\_PRES = Data Inicial do Período informado na tela de geração;

\- Data Fim da ICT\_AM\_REL\_IES\_NF\_PRES = Data Final do Período informado na tela de geração;

\- Relacionar a tabela ICT\_AM\_REL\_IES\_NF\_PRES com a tabela DWT\_DOCTO\_FISCAL pelos campos da PK da Capa do Documento Fiscal\.

\- Relacionar a tabela ICT\_AM\_REL\_IES\_NF\_PRES com a tabela DWT\_ITENS\_MERC pelos campos da PK do Item do Documento Fiscal\.

Recuperar registro a registro \(sem consolidar\) da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Caso a consulta não retorne registro, exibir a mesangem a seguir e finalizar o processamento:

“Não foram encontrados dados para geração do relatório\. Favor verifique se o Cálculo do Crédito Presumido foi realizado para o período/estabelecimento/inscrição estadual informado\.”

Observação:

A Tabela de Itens de Nota Fiscal para Relatório Analítico do Crédito Presumido \(ICT\_AM\_REL\_IES\_NF\_PRES\) é carregada na Geração do Crédito Presumido com os documentos fiscais que compuseram o cálculo\. Ver regra no documento MTZ\-PIM\-Apuracao\-Calculo\_dos\_Creditos\-Entrada\-Credito\_Presumido\.doc\.

# <a id="_Toc107239685"></a>Processamento

Os documentos fiscais recuperados no tópico 2 serão gravados arquivos separados por empresa, estabelecimento, inscrição estadual PIM e período\. 

Os arquivos são formato Excel \(extensão xlsx\)\. 

Tratar o cenário em que o número de registros ultrapasse o limite do excel \(1milhao de linhas\), quebrando em mais de um arquivo\.

Veja o layout dos arquivos nos próximos tópicos\.

# <a id="_Toc107239686"></a>Layout e Regra de Preenchimento dos Campos do Relatório 

<a id="_Hlk101878485"></a>Gerar um arquivo formato Excel \(extensão xlsx\) contendo os documentos fiscais recuperados para a empresa, estabelecimento, inscrição estadual PIM e período\.

Nomeclatura p/ Arquivo: “<a id="_Hlk101537340"></a>Rel\_CPres\_XXXXXX\_YYYYYYYYYYYYY\_DD\_MM\_AAAA\_999\.xlsx”

Onde:

XXXXXX: Estabelecimento informada na tela

YYYYYYYYYYYYY: Inscrição Estadual informada na tela

DD\_MM\_AAAA: Data Fim informada na tela

\_999´: número do volume \(001, 002,\.\.\.\)\.  

Se o número de registros a serem gravados no arquivo ultrapassar o limite do excel \(1milhão de linhas\), quebrar em mais de um arquivo \(Rel\_CPres\_XXXXXX\_YYYYYYYYYYYYY\_DD\_MM\_AAAA\_001\.xlsx, Rel\_CPres\_XXXXXX\_YYYYYYYYYYYYY\_DD\_MM\_AAAA\_002\.xls,\.\.\.\)\. Este tratamento é feito hoje no Relatorio de NF p/ CFOP – Formato XLS do Report Fiscal \(ver package REL\_NF\_CFO\_EXCEL\_FPROC\)\.

O arquivo será composto pelas seguintes colunas:

__Campo__

__Regra de Preenchimento__

Empresa

Código da Empresa do documento fiscal\.

Utilizar o caracter especial chr\(2\) concatenado com o COD\_EMPRESA, para que no Excel o código se mantenha com zeros à esquerda\.

Obs: esse tratamento é feito na package PKG\_DW\_CONF\_CHAVE\.

Campo COD\_EMPRESA da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Estab

Código do Estabelecimento do Documento Fiscal\.

Utilizar o caracter especial chr\(2\) concatenado com o COD\_ESTAB, para que no Excel o código se mantenha com zeros à esquerda\.

Campo COD\_ESTAB da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Razão Social

Razão Social do Estabelecimento\.

Campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO\.

CGC

CNPJ do Estabelecimento\.

Utilizar o caracter especial chr\(2\) concatenado com o CGC, para que no Excel o código se mantenha com zeros à esquerda\.

Campo CGC da tabela ESTABELECIMENTO\.

Inscrição Estadual PIM

Inscrição Estadual PIM do Estabelecimento informada na tela de Geração\.

Utilizar o caracter especial chr\(2\) concatenado, para que no Excel o código se mantenha com zeros à esquerda\.

Campo INSC\_ESTADUAL da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Data Inicio

Data Inicial do Período informada na tela de Geração\.

Campo DAT\_INICIO da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Data Fim

Data Final do Período informada na tela de Geração\.

Campo DAT\_FIM da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Linha Produto Incentivo

Linha de Produto Incentivado gerado nos mapas de entrada/saída\.

Utilizar o caracter especial chr\(2\) concatenado, para que no Excel o código se mantenha com zeros à esquerda\.

Campo COD\_LINHA\_PRD da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Pessoa Fis/Jur \(ind\-cod\)

Concatenar o Indicador \+ “\-“ \+ Código da Pessoa Fis/Jur do Documento Fiscal, relacionado ao campo IDENT\_FIS\_JUR da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Razão Social Pessoa Fis/Jur

Razão Social da Pessoa Fis/Jur do Documento Fiscal, relacionado ao campo IDENT\_FIS\_JUR da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

CPF/CNPJ Pessoa Fis/Jur

CPF/CNPJ da Pessoa Fis/Jur do Documento Fiscal, relacionado ao campo IDENT\_FIS\_JUR da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Utilizar o caracter especial chr\(2\) concatenado, para que no Excel o código se mantenha com zeros à esquerda\.

UF Pessoa Fis/Jur

UF da Pessoa Fis/Jur do Documento Fiscal, relacionado ao campo IDENT\_FIS\_JUR da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Inscrição Estadual Pessoa Fis/Jur

Inscrição Estadual da Pessoa Fis/Jur do Documento Fiscal, relacionado ao campo IDENT\_FIS\_JUR da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Utilizar o caracter especial chr\(2\) concatenado, para que no Excel o código se mantenha com zeros à esquerda\.

Data Fiscal

Data Fiscal do documento Fiscal\.

Campo DATA\_FISCAL da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Num Doc Fiscal

Número do Documento Fiscal

Campo num\_docfis da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Utilizar o caracter especial chr\(2\) concatenado, para que no Excel o código se mantenha com zeros à esquerda\.

Serie Doc Fiscal

Série do Documento Fiscal

Campo serie\_docfis da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Utilizar o caracter especial chr\(2\) concatenado, para que no Excel o código se mantenha com zeros à esquerda\.

Sub Série Doc Fiscal

Subsérie do Documento Fiscal

Campo sub\_serie\_docfis da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Utilizar o caracter especial chr\(2\) concatenado, para que no Excel o código se mantenha com zeros à esquerda\.

Modelo

Modelo do Documento Fiscal, relacionado ao IDENT\_MODELO da DWT\_DOCTO\_FISCAL \(campo 13 da SAFX07\)\.

Utilizar o caracter especial chr\(2\) concatenado, para que no Excel o código se mantenha com zeros à esquerda\.

Num\. Autentic\. Nfe

Chave de Acesso da NF\-Eletrônica do Documento fiscal\. Campo NUM\_AUTENTIC\_NFE da DWT\_DOCTO\_FISCAL \(campo 226 da SAFX07\)\.

Utilizar o caracter especial chr\(2\) concatenado, para que no Excel o código se mantenha com zeros à esquerda\.

Cod\. Cfo

Código do CFOP do Item de Mercadoria do Documento Fiscal\.

Campo COD\_CFO da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Conforme tratamento da geração do Crédito Presumido o campo COD\_CFOP da tabela ICT\_AM\_REL\_IES\_NF\_PRES é gravado com o CFOP do item de mercadoria quando o CFOP ou CFOP \+ Natureza da Operação estiver parametrizado em Parâmetros Gerais de Cálculo CFOP ou CFOP/Natureza para opção Crédito Presumido \(vide menu Parâmetros >> Crédito Presumido/Estímulo \(Entradas\) >> Parâmetros Gerais de Cálculo CFOP ou Parâmetros Gerais de Cálculo CFOP/Natureza\)\.

Cod\. Natureza Op

Código da Natureza de Operação do Item de Mercadoria do Documento Fiscal\.

Campo COD\_NATUREZA\_OP da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Utilizar o caracter especial chr\(2\) concatenado, para que no Excel o código se mantenha com zeros à esquerda\.

Conforme tratamento da geração do Crédito Presumido o campo COD\_NATUREZA\_OP da tabela ICT\_AM\_REL\_IES\_NF\_PRES é gravado com a Natureza Operação do item de mercadoria quando o CFOP \+ Natureza da Operação estiver parametrizado em Parâmetros Gerais de Cálculo CFOP/Natureza para opção Crédito Presumido \(vide menu Parâmetros >> Crédito Presumido/Estímulo \(Entradas\) >> Parâmetros Gerais de Cálculo CFOP/Natureza\)\.

Origem

Preencher com a Descrição relacionada indicador gravado no campo IND\_PARAM\_CALCULO da tabela ICT\_AM\_REL\_IES\_NF\_PRES:

IND\_PARAM\_CALCULO

Descrição

1

Valor Contábil

2

Base Tributada

4

Base Outras

5

Base Isenta

Conforme tratamento da geração do Crédito Presumido o campo IND\_PARAM\_CALCULO da tabela ICT\_AM\_REL\_IES\_NF\_PRES é gravado com campo “Parâmetro para o Cálculo” da parametrização do CFOP ou CFOP/Natureza \(menu Parâmetros >> Crédito Presumido/Estímulo \(Entradas\) >> Parâmetros Gerais de Cálculo CFOP ou Parâmetros Gerais de Cálculo CFOP/Natureza\);

Produto \(ind\-cod\)

Concatenar o Indicador \+ “\-“ \+ Código do Produto do item de Mercadoria do Documento Fiscal, relacionado ao campo IDENT\_PRODUTO da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Descrição Produto

Descrição do Produto \(campo 04 da SAFX2013\) relacionado ao campo IDENT\_PRODUTO da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Para documento fiscal sem item de mercadoria, esta coluna não será preenchida\.

NBM

Código NBM do Produto \(campo 05 da SAFX2013\) relacionado ao campo IDENT\_PRODUTO da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Utilizar o caracter especial chr\(2\) concatenado, para que no Excel o código se mantenha com zeros à esquerda\.

Para documento fiscal sem item de mercadoria, esta coluna não será preenchida\.

Item Merc

Número do Item de Mercadoria do Documento Fiscal\.

Campo num\_item da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Sit\. Tributária A

Código da Situação Tributária A do Item de Mercadoria do Documento Fiscal \(campo 30 da SAFX08\), relacionado ao IDENT\_SITUACAO\_A da DWT\_ITENS\_MERC\.

Utilizar o caracter especial chr\(2\) concatenado, para que no Excel o código se mantenha com zeros à esquerda\.

Para documento fiscal sem item de mercadoria, a coluna Sit Tributária A não será preenchida\.

Sit\. Tributária B

Código da Situação Tributária B do Item de Mercadoria do Documento Fiscal \(campo 31 da SAFX08\), relacionado ao IDENT\_SITUACAO\_B da DWT\_ITENS\_MERC\.

Utilizar o caracter especial chr\(2\) concatenado, para que no Excel o código se mantenha com zeros à esquerda\.

Para documento fiscal sem item de mercadoria, a coluna Sit\. Tributária B não será preenchida\.

Vlr Contábil

Valor Contábil do Item de Mercadoria do Documento Fiscal \(campo 64 da SAFX08\)

Campo VLR\_CONTAB\_ITEM da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Vlr Base ICMS Tributada

Valor da Base Tributada de ICMS do Item de Mercadoria do Documento Fiscal

Campo VLR\_BASE\_ICMS\_TRIB da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Alíquota ICMS

Valor da Alíquota de ICMS do Item de Mercadoria do Documento Fiscal

Campo ALIQ\_TRIBUTO\_ICMS da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Vlr ICMS

Valor do ICMS do Item de Mercadoria do Documento Fiscal

Campo VLR\_TRIBUTO\_ICMS da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Vlr Base ICMS Isenta

Valor da Base Isenta de ICMS do Item de Mercadoria do Documento Fiscal

Campo VLR\_BASE\_ICMS\_ISENT da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Vlr Base ICMS Outras

Valor da Base Outras de ICMS do Item de Mercadoria do Documento Fiscal

Campo VLR\_BASE\_ICMS\_OUTR da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Vlr Base Crédito Presumido

Base de Cálculo do Crédito Presumido\.

Campo VLR\_BASE\_ICMS\_PRES da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Alíquota Crédito Presumido

Alíquota considerada para cálculo do crédito presumido

Campo ALIQ\_ICMS\_PRES da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

Vlr Crédito Presumido

Valor do Crédito Presumido

Campo VLR\_ICMS\_PRES da tabela ICT\_AM\_REL\_IES\_NF\_PRES\.

= = = = = =

 


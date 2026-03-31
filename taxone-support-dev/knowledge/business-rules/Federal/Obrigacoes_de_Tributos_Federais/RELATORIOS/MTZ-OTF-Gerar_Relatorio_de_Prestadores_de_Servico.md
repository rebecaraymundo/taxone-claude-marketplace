# MTZ-OTF-Gerar_Relatorio_de_Prestadores_de_Servico

- **Fonte:** MTZ-OTF-Gerar_Relatorio_de_Prestadores_de_Servico.docx
- **Modificado:** 2023-01-27
- **Tamanho:** 43 KB

---

# Obrigações de Tributos Federais – Relação dos Prestadores de Serviço na Construção Civil

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3003

Incluir tratamento que compõe o Valor do INSS

Este documento de requisito tem por objetivo permitir que o módulo Obrigações de Tributos Federais realize a geração do novo relatório com informações de Prestadores de Serviços na Construção Civil disponibilizado na IN SRP 971/09\.

O escopo de criação dessa OS contempla o módulo Obrigações de Tributos Federais\. Porém para que o usuário consiga gerar o relatório corretamente, é preciso ter documentos de entrada com informações necessárias para as Guias de Previdência Social dos prestadores de serviços de construção civil\.

Inclusão do Relatório Relação dos Prestadores de Serviço na Construção Civil

14/09/2010

CH72696

Alteração na regra RN24 – Assinatura do Responsável

Embora o campo deva ser preenchido manualmente o cliente solicita que o nome do responsável seja informado automaticamente no campo\. A Receita Federal não detalhou a situação da assinatura do responsável\.

04/03/2011

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

# RN00

O relatório deverá ser exibido na área de “Relatórios” no menu principal da tela do módulo Obrigações de Tributos Federais, menu Relatórios >> Relação dos Prestadores de Serviço na Construção Civil, essa opção deverá ser criada abaixo do Relatório de Tributos Federais

Título do Relatório: 

__“MINISTERIO DA FAZENDA__

__SECRETARIA DA RECEITA FEDERAL DO BRASIL__

RELACAO DOS PRESTADORES DE SERVICOS NA CONSTRUCAO CIVIL”

OS3003

# RN01

__1 – Estabelecimento__

Incluir o critério Estabelecimento para a geração do relatório\. Essa informação deve ser recuperada através do campo COD\_ESTAB concatenado com RAZAO\_SOCIAL da tabela ESTABELECIMENTO\. Informar mensagem de erro caso este parâmetro seja nulo\.

OS3003

# RN02

__2 – Data de Emissão__

Incluir o critério Data e Emissão de início e final para a geração do relatório\. Essa informação deve ser recuperada através do campo 11 \(DATA\_EMISSAO\) da tabela SAFX07\. Informar mensagem de erro caso este parâmetro seja nulo\.

OS3003

# RN03

__3 – Prestador de Serviço__

Incluir o critério Prestador de Serviço para a geração do relatório\. Essa informação deve ser recuperada através do campo 02 \(COD\_FIS\_JUR\) concatenado com o campo 05 \(RAZAO\_SOCIAL\) da tabela SAFX04\. Esse parâmetro não é obrigatório, porém se informado deverá ser apresentado no relatório somente informações do mesmo\.

OS3003

# RN04

__4 – Responsável Legal__

Incluir o critério Responsável Legal para a geração do relatório\. Essa informação deve ser recuperada através do campo: NOM\_RESPONSAVEL da tabela RESP\_INFORMACAO\. Esse parâmetro é obrigatório e deverá ser informado no Rodapé apenas o campo NUM\_CPF da tabela RESP\_INFORMACAO\.

OS3003

# RN05

O Estabelecimento gerador deverá possuir no cadastro, a Matricula CEI, campo CEI\_PORT63 da tabela ESTABELECIMENTO\.

Deverá ser recuperado somente o tipo de serviço Equiparado a Construção Civil, campo 04 \(IND\_TP\_SERVICO\) da tabela SAFX2018\.

As informações do relatório serão recuperadas da tabela IRT\_RET\_INSS\_DF em virtude desse relatório servir como conferência em relação às GPS’s emitidas para pagamento no banco\.

Selecionar da tabela IRT\_RET\_INSS\_DF os registros que possuam notas fiscais de entrada, ou seja, o campo MOVTO\_E\_S = ‘E’\.

OS3003

# RN06

__EMPRESA__

Preencher no cabeçalho do relatório o Estabelecimento que foi selecionado\. Essa informação deve ser recuperada através do campo: RAZAO\_SOCIAL da tabela ESTABELECIMENTO\.

OS3003

# RN07

__CNPJ__

Preencher no cabeçalho do relatório o CNPJ do Estabelecimento\. Essa informação deve ser recuperada através do campo: CGC da tabela ESTABELECIMENTO\.

Exemplo CNPJ: 10277281000188

Gravar como: 10\.277\.281/0001\-88

OS3003

# RN08

__MATRICULA CEI__

Preencher no cabeçalho do relatório a Matrícula CEI\. Essa informação deve ser recuperada através do campo: CEI\_PORT63 da tabela ESTABELECIMENTO\.

OS3003

# RN09

__ENDEREÇO__

Preencher no cabeçalho do relatório o Endereço do Estabelecimento\. Essa informação deve ser recuperada através do campo: ENDERECO concatenado com o NUM\_ENDERECO da tabela ESTABELECIMENTO\.

OS3003

# RN10

__FONE CONTATO__

Preencher no cabeçalho do relatório o Fone Contato do Estabelecimento\. Essa informação deve ser recuperada através dos campos: DDD e TELEFONE da tabela ESTABELECIMENTO\. As informações devem ser gravadas conforme exemplo abaixo:

DDD: 11

Telefone: 21590500

Gravar como: \(11\) 2159\-0500

OS3003

# RN11

__CNPJ Prestador do Serviço__

Gravar na coluna 1 do relatório o CNPJ Prestador do Serviço\. 

Essa informação deve ser recuperada através da comparação do conteúdo do campo COD\_FIS\_JUR da tabela IRT\_RET\_INSS\_DF com o cadastro do Estabelecimento Prestador, campo 02 \(COD\_FIS\_JUR\) da tabela SAFX04\. Após identificar o mesmo conteúdo do campo COD\_FIS\_JUR nas tabelas distintas, recuperar o valor contido no campo 06 \(CPF\_CGC\) da tabela SAFX04\.

Exemplo CNPJ: 10277281000188

Gravar como: 10\.277\.281/0001\-88

OS3003

# RN12

__Nome do Prestador__

Gravar na coluna 2 do relatório o Nome do Prestador do Serviço\. 

Essa informação deve ser recuperada através da comparação do conteúdo do campo COD\_FIS\_JUR da tabela IRT\_RET\_INSS\_DF com a informação do campo 02 \(COD\_FIS\_JUR\) da tabela SAFX04\. Após identificar o mesmo conteúdo do campo COD\_FIS\_JUR nas tabelas distintas, recuperar o valor contido no campo 05 \(RAZAO\_SOCIAL\) da tabela SAFX04\.

OS3003

# RN13

__Tipo de Serviço Prestado__

Gravar na coluna 3 do relatório o Tipo de Serviço Prestado\. 

Essa informação deve ser recuperada através da comparação do conteúdo do campo 12 \(COD\_SERVICO\) da tabela SAFX09 com a informação do campo 01 \(COD\_SERVICO\) da tabela SAFX2018\. Após identificar o mesmo conteúdo do campo COD\_SERVICO nas tabelas distintas, recuperar o valor contido no campo 03 \(DESCRICAO\) da tabela SAFX2018\.

Quando o documento fiscal possuir dois ou mais itens de serviços distintos, deverá apresentar o ITEM 01 como sendo o registro principal, preenchendo todas as colunas conforme critérios abaixo, exceto as colunas COLUNA 3 \(o campo 12 \(COD\_SERVICO\) da tabela SAFX09\) e a COLUNA 8 Base INSS da tabela SAFX09, que deverá trazer somente a informação correspondente ao ITEM 01\.

Os outros ITENS serão apresentados nas demais linhas, porém trazendo somente a COLUNA 3 \(o campo 12 \(COD\_SERVICO\) da tabela SAFX09\) e a COLUNA 8 Base INSS da tabela SAFX09\.

Caso contrário, o documento fiscal possuir apenas um item, utilizar os critérios de cada campo\.

OS3003

# RN14

__Número da NF__

Gravar na coluna 4 do relatório o Número da Nota Fiscal\. Essa informação deve ser recuperada do campo 08 \(NUM\_DOCFIS\) da tabela SAFX07\.

OS3003

# RN15

__Data da NF__

Gravar na coluna 5 do relatório a Data de Emissão\. Essa informação deve ser recuperada do campo 11 \(DATA\_EMISSAO\) da tabela SAFX07\. A data será gravada no formato DD/MM/AAAA\. 

OS3003

# RN16

__Valor Bruto da NF__

Gravar na coluna 6 do relatório o Valor Bruto da Nota Fiscal\. Essa informação deve ser recuperada do campo 23 \(VLR\_TOT\_NOTA\) da tabela SAFX07\.

OS3003

# RN17

__Valor da Retenção__

Gravar na coluna 7 do relatório o Valor da Retenção da Nota Fiscal\. Essa informação deve ser recuperada do campo 87 \(VLR\_INSS\_RETIDO\) da tabela SAFX07\.

OS3003

# RN18

__Base de Cálculo da Contribuição__

Gravar na coluna 8 do relatório o Valor da Base de Cálculo da Contribuição\. Essa informação deve ser recuperada do campo Base INSS da tabela SAFX09\.

Quando o documento fiscal possuir dois ou mais itens de serviços distintos, deverá apresentar o ITEM 01 como sendo o registro principal, preenchendo todas as colunas conforme critérios abaixo, exceto as colunas COLUNA 3 \(o campo 12 \(COD\_SERVICO\) da tabela SAFX09\) e a COLUNA 8 Base INSS da tabela SAFX09, que deverá trazer somente a informação correspondente ao ITEM 01\.

Os outros ITENS serão apresentados nas demais linhas, porém trazendo somente a COLUNA 3 \(o campo 12 \(COD\_SERVICO\) da tabela SAFX09\) e a COLUNA 8  Base INSS da tabela SAFX09\.

Caso contrário, o documento fiscal possuir apenas um item, utilizar os critérios de cada campo\.

__Atenção__: Na ausência da informação do campo novo __Base INSS__ da SAFX09/__ __DWT\_ITENS\_SERV, deverá ser recuperado da capa do documento fiscal, ou seja, o conteúdo do campo VLR\_BASE\_INSS da SAFX07/DWT\_DOCTO\_FISCAL\. Quando houver esta situação o valor total da Base de INSS será a mesma para todos os itens\.

OS3003

# RN19

__Competência__

Gravar na coluna 9 do relatório o período de competência no formato MM/AAAA\. Essa informação deve ser recuperada do campo MES\_COMPETENCIA e ANO\_COMPETENCIA da tabela IRT\_RET\_INSS\_DF\.

OS3003

# RN20

__Banco/Agência__

Gravar na coluna 10 do relatório o Banco e a Agência da GPS\. Essa informação deve ser recuperada do campo COD\_BANCO concatenado COD\_AGENCIA da tabela IRT\_GPS\.

OS3003

# RN21

__Data da Autenticação__

Gravar na coluna 11 do relatório a Data da Autenticação\. Essa informação deve ser recuperada do campo DAT\_PAGAMENTO da tabela IRT\_GPS\.

OS3003

# RN22

__Valor Autenticado__

Gravar na coluna 12 do relatório o Valor Autenticado\. Essa informação deve ser recuperada do campo VLR\_TOT\_RECOLH da tabela IRT\_GPS\.

OS3003

# RN23

__Local/Data__

Preencher no rodapé do relatório o Local/Data de geração do relatório\. O Local deve ser recuperado através da comparação do conteúdo do campo COD\_MUNICIPIO da tabela ESTABELECIMENTO com a informação do campo COD\_MUNICIPIO da tabela MUNICIPIO\. Após identificar o mesmo conteúdo do campo COD\_MUNICIPIO nas tabelas distintas, recuperar o valor contido no campo DESCRICAO para preencher o Local\. Imprimir a barra “/” e em seguida, a Data de geração do relatório no formato DD/MM/AAAA\.

OS3003

# RN24

__Assinatura e CPF do Responsável pelas informações __

Preencher no rodapé do relatório o __NOME__ e o CPF do Responsável Legal pelas informações\. Quando informado o contador responsável no filtro de seleção do relatório, o NOME e o CPF deverão ser informados no local reservado conforme modelo de apresentação do relatório destacado no documento “REQ \- OS3003 \- OTF \- Gerar Relatório de Prestadores de Serviço\.doc”\. 

O NOME e CPF devem ser recuperados da RN04\. Utilizar o traço no relatório para trazer e preencher o Nome do Responsável que foi informado no parâmetro inicial da geração do relatório\.

OS3003/

CH72696

# RN25

__\(CONTADOR/CHEFE DEPARTAMENTO PESSOAL/PROPRIETÁRIO/DONO DA OBRA OU INCORPORADOR\)__

Preencher no rodapé do relatório o conteúdo fixo:__ “\(CONTADOR/CHEFE DEPARTAMENTO PESSOAL/PROPRIETÁRIO/DONO DA OBRA OU INCORPORADOR\)”__

Verificar o modelo de apresentação do relatório destacado no documento “REQ \- OS3003 \- OTF \- Gerar Relatório de Prestadores de Serviço\.doc”\.

OS3003

# RN26

__Modelo aprovado IN__

__ __

Preencher no rodapé do relatório a base legal de acordo com o informado no modelo\. Conteúdo fixo: “__Modelo aprovado pela Instrução Normativa RFB nº 971, de 13 de novembro de 2009\.”__

OS3003

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


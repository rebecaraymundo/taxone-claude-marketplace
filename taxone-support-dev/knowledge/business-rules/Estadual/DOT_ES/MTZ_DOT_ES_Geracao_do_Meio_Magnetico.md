# MTZ_DOT_ES_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_DOT_ES_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2020-12-09
- **Tamanho:** 72 KB

---

THOMSON REUTERS

DOT\-ES

Geração do Meio Magnético

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS1990

Julyana Perrucini

Este documento tem como objetivo definir as regras para preenchimento dos campos do arquivo magnético da DOT\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN00

__Regra Geral__

- Para geração do arquivo magnético, deverão ser consideradas as informações dos Quadros: A, B, C, D e Detalhamento dos Municípios; assim como, é feito para geração do Relatório;
- Será gerado um arquivo por estabelecimento selecionado\.

MFS1990

RN01

__Regra de criação do nome do arquivo__

O arquivo pode ser gerado com qualquer nome a critério do contribuinte, então colocaremos a nomenclatura padrão\.

__NºPROCESSO\_DOT\-ES\.xml__, onde:

__NºPROCESSO:__ representa o número do processo, caso o usuário não marque a opção “Gera Arquivo S/ Nº Processo”\.

__DOT\-ES:__ representa o nome da obrigação acessória\.

__\.xml:__ extensão do arquivo\.

*Exemplos:*

DOT\-ES\.xml

1234\_ DOT\-ES\.xml

MFS1990

RN02

__Regras referentes à formatação dos registros gerados no meio magnético__

- O arquivo a ser carregado, deverá ser do tipo XML, versão 1\.0, ISO\-8859\-1;
- A TAG de que abre o arquivo de importação é <IMPORTAR\_DOTS></IMPORTAR\_DOTS> dentro dela ficará as declarações que serão importadas;
- As informações da declaração ficarão dentro da TAG <DECLARACAO></DECLARACAO>, inclusive os detalhamentos quando houver;
- O detalhamento ficará dentro da TAG <DETALHAMENTOS></DETALHAMENTOS> e as informações de cada município ficará dentro da TAG <DETALHAMENTO></DETALHAMENTO>;
- As TAG dos Quadros A, B, C e D serão obrigatórias as suas criações, mesmo sendo zeradas ou vazias\.

__*Exemplo:*__

*<?xml version="1\.0" encoding="ISO\-8859\-1"?>*

*<IMPORTAR\_DOTS>*

*<DECLARACAO>*

*\.\.\.*

*<DETALHAMENTOS>*

*<DETALHAMENTO>*

*\.\.\.*

*</DETALHAMENTO>*

*</DETALHAMENTOS>*

*</DECLARACAO>*

*</IMPORTAR\_DOTS>*

MFS1990

RN03

__Regra geral p/ recuperar as informações dos Quadros __

O arquivo deve as informações com as seguintes características:

- Estabelecimento Quadros = Estabelecimento marcado na tela de geração
- Data das Operações compreendida entre a Data Inicial e Data Final preenchida na tela de geração

*Observações:*

Quadros A e B considerar campo “Operações de: até”;

Quadros C e D considerar campo “Ano de Geração”;

Detalhamento dos Municípios considerar campo “Referência”\.

MFS1990

RN04

__Dados do Contribuinte – Campo <NUM\_INSCEST></NUM\_INSCEST>__

Campo alfanumérico de preenchimento obrigatório sem definição de tamanho\.

__Origem: __Básicos >> Parâmetros >> Preliminares >> Inscrições Estaduais\.

Preencher com o conteúdo do campo Inscrição Estadual vinculada ao Estabelecimento informado na geração do arquivo, quando o conteúdo do campo U\.F for igual a “ES”\.

__Tratamento:__

- A Inscrição Estadual deverá ser gerada no formato: 999\.999\.99\-9;
- Caso esse campo não esteja preenchido, emitir a mensagem no log: “A Inscrição Estadual não está preenchida para o Estabelecimento gerado\. Campo de preenchimento obrigatório, favor verificar\.”\.

MFS1990

RN05

__Dados do Contribuinte – Campo <DATA\_INICIO\_DECLARACAO></DATA\_INICIO\_DECLARACAO>__

Campo data de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Geração do Meio Magnético\.

Preencher com o conteúdo do campo Data Inicial informada na geração do arquivo\.

__Tratamento:__

- A Data Inicial deverá ser gerada no formato: AAAAMMDD\.

MFS1990

RN06

__Dados do Contribuinte – Campo <DATA\_FIM\_DECLARACAO></DATA\_FIM\_DECLARACAO>__

Campo data de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Geração do Meio Magnético\.

Preencher com o conteúdo do campo Data Final informada na geração do arquivo\.

__Tratamento:__

- A Data Final deverá ser gerada no formato: AAAAMMDD\.

MFS1990

RN07

__Dados do Contribuinte – Campo <CODG\_MUNICIPIO></CODG\_MUNICIPIO>__

Campo numérico inteiro de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Parâmetros >> Municípios IBGE X Municípios ES\.

Preencher com o conteúdo do campo Município Destino vinculado ao campo Município do Estabelecimento informado na geração do arquivo\.

__Tratamento:__

- Caso o campo Município do Estabelecimento não esteja preenchido, emitir a mensagem no log: “O Município do Contribuinte não está preenchido para o Estabelecimento gerado\. Campo de preenchimento obrigatório, favor verificar\.”\.

MFS1990

RN08

__Dados do Contribuinte – Campo <CODG\_APRESENTACAO></CODG\_APRESENTACAO>__

Campo inteiro de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Geração do Meio Magnético\.

Preencher com o conteúdo do campo Tipo de Apresentação informada na geração do arquivo\.

MFS1990

RN09

__Quadro A – Campo <VALR\_ESTOQUE\_INICIAL></VALR\_ESTOQUE\_INICIAL>__

Campo numérico decimal de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Consulta do Quadro A\.

Preencher com o conteúdo do campo Estoque Inicial \- 01\.

__Tratamento:__

- Por ser um campo obrigatório, caso o valor for igual à zero, gerar 0\.00\.

MFS1990

RN10

__Quadro A – Campo <VALR\_COMPRA\_DEVOL\_TRANSF></VALR\_COMPRA\_DEVOL\_TRANSF>__

Campo numérico decimal de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Consulta do Quadro A\.

Preencher com o conteúdo do campo Compras, Transferências e Devoluções do Estado \- 02\.

__Tratamento:__

- Por ser um campo obrigatório, caso o valor for igual à zero, gerar 0\.00\.

MFS1990

RN11

__Quadro A – Campo <VALR\_PROD\_RURAL\_PROPRIA></VALR\_PROD\_RURAL\_PROPRIA>__

Campo numérico decimal de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Consulta do Quadro A\.

Preencher com o conteúdo do campo Entrada de Produção Rural Própria \- 03\.

__Tratamento:__

- Por ser um campo obrigatório, caso o valor for igual à zero, gerar 0\.00\.

MFS1990

RN12

__Quadro A – Campo <VALR\_AQZ\_PESSOA\_FISICA></VALR\_AQZ\_PESSOA\_FISICA>__

Campo numérico decimal de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Consulta do Quadro A\.

Preencher com o conteúdo do campo Compras de PF ou Não Contribuinte do ICMS Estado \- 04\.

__Tratamento:__

- Por ser um campo obrigatório, caso o valor for igual à zero, gerar 0\.00\.

MFS1990

RN13

__Quadro A – Campo <VALR\_COMPRA\_FORA\_EST></VALR\_COMPRA\_FORA\_EST>__

Campo numérico decimal de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Consulta do Quadro A\.

Preencher com o conteúdo do campo Compras, Transferências e Devoluções de Outros Estados \- 05\.

__Tratamento:__

- Por ser um campo obrigatório, caso o valor for igual à zero, gerar 0\.00\.

MFS1990

RN14

__Quadro A – Campo <VALR\_COMPRA\_EXTERIOR></VALR\_COMPRA\_EXTERIOR>__

Campo numérico decimal de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Consulta do Quadro A\.

Preencher com o conteúdo do campo Compras, Transferências e Devoluções do Exterior \- 06\.

__Tratamento:__

- Por ser um campo obrigatório, caso o valor for igual à zero, gerar 0\.00\.

MFS1990

RN15

__Quadro A – Campo <VALR\_VENDA\_DEVOLUCAO></VALR\_VENDA\_DEVOLUCAO>__

Campo numérico decimal de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Consulta do Quadro A\.

Preencher com o conteúdo do campo Vendas, Transferências e Devoluções Internas \- 08\.

__Tratamento:__

- Por ser um campo obrigatório, caso o valor for igual à zero, gerar 0\.00\.

MFS1990

RN16

__Quadro A – Campo <VALR\_VENDA\_FORA\_ESTADO></VALR\_VENDA\_FORA\_ESTADO>__

Campo numérico decimal de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Consulta do Quadro A\.

Preencher com o conteúdo do campo Vendas, Transferências e Devoluções para Outros Estados \- 09\.

__Tratamento:__

- Por ser um campo obrigatório, caso o valor for igual à zero, gerar 0\.00\.

MFS1990

RN17

__Quadro A – Campo <VALR\_VENDA\_EXTERIOR></VALR\_VENDA\_EXTERIOR>__

Campo numérico decimal de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Consulta do Quadro A\.

Preencher com o conteúdo do campo Vendas para o Exterior \- 10\.

__Tratamento:__

- Por ser um campo obrigatório, caso o valor for igual à zero, gerar 0\.00\.

MFS1990

RN18

__Quadro A – Campo <VALR\_ESTOQUE\_FINAL></VALR\_ESTOQUE\_FINAL>__

Campo numérico decimal de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Consulta do Quadro A\.

Preencher com o conteúdo do campo Estoque Final \- 11\.

__Tratamento:__

- Por ser um campo obrigatório, caso o valor for igual à zero, gerar 0\.00\.

MFS1990

RN19

__Quadro B – Campo <VALR\_ENERGIA\_ELETRICA></VALR\_ENERGIA\_ELETRICA>__

Campo numérico decimal de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Consulta do Quadro B\.

Preencher com o conteúdo do campo Energia Elétrica \- 14\.

__Tratamento:__

- Por ser um campo obrigatório, caso o valor for igual à zero, gerar 0\.00\.

MFS1990

RN20

__Quadro B – Campo <VALR\_TRANSPORTE></VALR\_TRANSPORTE>__

Campo numérico decimal de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Consulta do Quadro B\.

Preencher com o conteúdo do campo Transporte \- 15\.

__Tratamento:__

- Por ser um campo obrigatório, caso o valor for igual à zero, gerar 0\.00\.

MFS1990

RN21

__Quadro B – Campo <VALR\_COMUNICACAO></VALR\_COMUNICACAO>__

Campo numérico decimal de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Consulta do Quadro B\.

Preencher com o conteúdo do campo Comunicação \- 16\.

__Tratamento:__

- Por ser um campo obrigatório, caso o valor for igual à zero, gerar 0\.00\.

MFS1990

RN22

__Quadro B – Campo <VALR\_EXTRACAO\_PETROLEO></VALR\_EXTRACAO\_PETROLEO>__

Campo numérico decimal de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Consulta do Quadro B\.

Preencher com o conteúdo do campo Extração de Petróleo \- 17\.

__Tratamento:__

- Por ser um campo obrigatório, caso o valor for igual à zero, gerar 0\.00\.

MFS1990

RN23

__Quadro B – Campo <VALR\_AGUA></VALR\_AGUA>__

Campo numérico decimal de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Consulta do Quadro B\.

Preencher com o conteúdo do campo Distribuição de Água Canalizada \- 18\.

__Tratamento:__

- Por ser um campo obrigatório, caso o valor for igual à zero, gerar 0\.00\.

MFS1990

RN24

__Quadro B – Campo <VALR\_OUTRAS\_ATIVIDADES></VALR\_OUTRAS\_ATIVIDADES>__

Campo numérico decimal de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Consulta do Quadro B\.

Preencher com o conteúdo do campo Outras Atividades \- 19\.

__Tratamento:__

- Por ser um campo obrigatório, caso o valor for igual à zero, gerar 0\.00\.

MFS1990

RN25

__Quadro C – Campo <VALR\_OUTROS\_SER\_TRANS></VALR\_OUTROS\_SER\_TRANS>__

Campo numérico decimal de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Manutenção >> Quadro C e D\.

Preencher com o conteúdo do campo Outros \- 20\.

__Tratamento:__

- Por ser um campo obrigatório, caso o valor for igual à zero, gerar 0\.00\.

MFS1990

RN26

__Quadro D – Campo <MEMO\_OBS></MEMO\_OBS>__

Campo alfanumérico de preenchimento obrigatório sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Manutenção >> Quadro C e D\.

Preencher com o conteúdo do campo Quadro D – Informações Complementares\.

__Tratamento:__

- Por ser um campo obrigatório, caso não esteja preenchido, gerar nulo \(<></>\)\.

MFS1990

RN27

__Regras dos Campos dos Quadros de Detalhamentos__

- O detalhamento só será criado quando um dos campos descritos a seguir possuírem valores diferentes de zero, nesse caso será necessário criar o detalhamento com os 78 municípios que existem no Estado do Espírito Santo mesmo que não existam valores a serem detalhados para eles, mas apenas quando não tiver nenhum detalhamento para o mesmo e seu código será gerado como 1 com valores zerados;
- Os campos que obrigaram a criação da TAG de <DETALHAMENTOS> serão: <VALR\_PROD\_RURAL\_PROPRIA>, <VALR\_AQZ\_PESSOA\_FISICA> do quadro A e os <VALR\_ENERGIA\_ELETRICA>, <VALR\_TRANSPORTE>, <VALR\_COMUNICACAO>, <VALR\_EXTRACAO\_PETROLEO>, <VALR\_AGUA> e <VALR\_OUTRAS\_ATIVIDADES> do quadro B;
- A TAG <VALR\_DETALHADO\_2> só será utilizada quando o campo <VALR\_ENERGIA\_ELETRICA> possuir valores neste caso o <VALR\_DETALHADO\_1> será os valores referente à Geração de Energia e o <VALR\_DETALHADO\_2> será os valores referente à Distribuição\.

MFS1990

RN28

__Quadro Detalhamentos – Campo <CODG\_MUNICIPIO></CODG\_MUNICIPIO>__

Campo inteiro de preenchimento obrigatório \(de acordo com a RN27\) sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Manutenção >> Detalhamentos dos Valores p/ Município\.

Preencher com código do município do conteúdo do campo Município\.

__Tratamento:__

- Por ser um campo obrigatório, caso não esteja preenchido, gerar nulo \(<></>\)\.

MFS1990

RN29

__Quadro Detalhamentos – Campo <CODG\_DETALHAMENTO></CODG\_DETALHAMENTO>__

Campo inteiro de preenchimento obrigatório \(de acordo com a RN27\) sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Manutenção >> Detalhamentos dos Valores p/ Município\.

Preencher com:

__1__\-Energia Elétrica, quando o conteúdo do campo Opção do Detalhamento for igual a “Energia Elétrica”;

__2__\-Transporte, quando o conteúdo do campo Opção do Detalhamento for igual a “Transporte”;

__3__\-Comunicação, quando o conteúdo do campo Opção do Detalhamento for igual a “Comunicação”;

__4__\-Produção Rural Própria, quando o conteúdo do campo Opção do Detalhamento for igual a “Entrada Produção Rural Própria”;

__5__\-Água, quando o conteúdo do campo Opção do Detalhamento for igual a “Distribuição de Água Canalizada”;

__6__\-Extração Petróleo, quando o conteúdo do campo Opção do Detalhamento for igual a “Extração de Petróleo”;

__7__\-Pessoa Física, quando o conteúdo do campo Opção do Detalhamento for igual a “Compras PF ou não contribuinte”;

__8__\-Outros, quando o conteúdo do campo Opção do Detalhamento for igual a “Outras Atividades”\.

__Tratamento:__

- Por ser um campo obrigatório, caso não esteja preenchido, gerar 1 \(<>1</>\)\.

MFS1990

RN30

__Quadro Detalhamentos – Campo <VALR\_DETALHADO\_1></VALR\_DETALHADO\_1>__

Campo numérico decimal de preenchimento obrigatório \(de acordo com a RN27\) sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Manutenção >> Detalhamentos dos Valores p/ Município\.

Preencher com o conteúdo do campo Valor\.

__Tratamento:__

- Por ser um campo obrigatório, caso o valor for igual à zero, gerar 0\.00\.

MFS1990

RN31

__Quadro Detalhamentos – Campo <VALR\_DETALHADO\_2></VALR\_DETALHADO\_2>__

Campo numérico decimal de preenchimento obrigatório \(de acordo com a RN27\) sem definição de tamanho\.

__Origem:__ Estadual >> DOT\-ES >> Obrigações >> Manutenção >> Detalhamentos dos Valores p/ Município\.

Preencher com o conteúdo do campo Valor de Distribuição\.

__Tratamento:__

- Considerar valor apenas quando o conteúdo do campo Opção do Detalhamento for igual a “Energia Elétrica”, as demais opções de detalhamento, gerar 0\.00\.

MFS1990

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN


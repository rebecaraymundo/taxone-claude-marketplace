# MTZ-Basicos_Processos Customizados_Deleção em Massa de Documento Fiscal

> Fonte: MTZ-Basicos_Processos Customizados_Deleção em Massa de Documento Fiscal.doc




THOMSON REUTERS

Processo Customizado


Deleção em Massa de Documento Fiscal


Localização:
Módulo: Básicos --> Processos Customizados
Menu: Não há, pois a funcionalidade será disponibilizada como serviço, acionado pelo envio do arquivo Excel via SFTP.


(Obs: As regras descritas neste documento são numeradas de acordo com os campos do layout do arquivo de Deleção em Massa, conforme o Manual de Layout, o que facilita a consulta. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00).




DOCUMENTO DE REQUISITO

DR
Nome
Descrição
MFS1020256
Liliane Assaf
Criação do Processo Customizado para Deleção em Massa de Documento Fiscal.




REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN00
Layout do Arquivo de Deleção em Massa de Documento Fiscal

A Deleção em Massa de Documento Fiscal é um serviço disponibilizado no Tax One para excluir os documentos fiscais das tabelas definitivas (Capa e tabelas filhas), a partir da relação de documentos carregados num arquivo Excel. Esse serviço é acionado pelo envio do arquivo Excel via SFTP.

O layout do arquivo que contém o conjunto de nota fiscal está definido a seguir.

Estrutura do Arquivo de Deleção em Massa de Documento Fiscal:
PK
OBRIG
ITEM
DESCRIÇÃO
CAMPO
TAM
TIPO
X
(*)
01
Código da Empresa
COD_EMPRESA
003
A
X
(*)
02
Código do Estabelecimento
COD_ESTAB
006
A
X
(*)
03
Data da Escrita Fiscal
DAT_FISCAL
008
N
X
(*)
04
Movimento Entrada/Saída
MOVTO_E_S
001
A
X
(*)
05
Normal ou Devolução
NORM_DEV
001
A
X
(*)
06
Tipo do Documento
COD_DOCTO
005
A
X
(*)
07
Indicador da Pessoa Física/Jurídica
IND_FIS_JUR
001
A
X
(*)
08
Código do Destinatário/Emitente
COD_FIS_JUR
014
A
X
(*)
09
Número do Documento Fiscal
NUM_DOCFIS
012
A
X

10
Série do Documento Fiscal
SERIE_DOCFIS
003
A
X

11
Subsérie do Documento Fiscal
SUB_SERIE_DOCFIS
002
A











































Sobre as mensagens de erro:
Todas as mensagens gravadas no log de erros devem mostrar os dados de identificação do processo referenciado pela Capa do Documento Fiscal, para permitir ao usuário a identificação do registro com erro.
MFS1020256
RN01

Campo Código da Empresa

Campo de preenchimento obrigatório.

 (registros das tabelas SAFX sem a informação da Empresa são desconsiderados)

90001
Codigo de Empresa nao esta preenchido

MFS1020256
RN02

Campo Código do Estabelecimento

Campo de preenchimento obrigatório.

(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados)

Quando não preenchido, o registro não será excluído, e no log do processo será gravada uma mensagem de erro:

90002
Codigo de Estabelecimento deve ser preenchido

MFS1020256
RN03

Campo Data da Escrita Fiscal

Campo de preenchimento obrigatório.

Quando não preenchido ou preenchido com informação que não seja uma data válida, o registro não será excluído, e no log do processo será gravada uma mensagem de erro:

92285
O campo data fiscal nao preenchido ou preenchido com formato invalido.

MFS1020256
RN04

Campo Movimento Entrada/Saída

Campo de preenchimento obrigatório.

Domínio de Valores válidos:
1 - Documento de Entrada, Documento de Terceiros;
2 - Documento de Entrada emitida pelo Estabelecimento, acolhendo Notas de Produtores Agropecuários;
3 - Documento de Entrada emitida pelo Estabelecimento, por retorno de mercadorias não entregues ao destinatário;
4 - Documento de Entrada emitida pelo Estabelecimento, outros motivos legais;
5 - Documento de Entrada emitida pelo Estabelecimento, globalizando Conhecimento de Frete ou Material Uso/Consumo;
9 - Documento de Saída.

Quando o campo não for preenchido ou preenchido com valor inválido, o registro não será excluído, e no log de erros será gravada uma mensagem de erro, conforme as mensagens padrão:

90129
O Campo Tipo de Movimento de Entrada/Saida nao esta preenchido ou com informacao invalida.


MFS1020256
RN05
Campo Normal ou Devolução

Campo de preenchimento obrigatório.
Domínio de Valores válidos:
1 - Normal;
2 - Devolução

Quando o campo não for preenchido ou preenchido com valor inválido, o registro não será excluído, e no log de erros será gravada uma mensagem de erro:

90130
O Campo Normal ou Devolucao nao esta preenchido ou preenchido com informacao invalida.

MFS1020256
RN06
Campo Tipo do Documento

Campo de preenchimento obrigatório.
Tabela de Origem: SAFX2005 - Cadastro do Tipo Documento

Quando o campo não for preenchido ou preenchido com informação inválida, o registro não será excluído, e no log de erros será gravada uma das mensagens de erro:

Verificar validação, conforme SAFX2005

90119
O Campo Codigo do Tipo de Documento nao esta preenchido.

90470
Nao foi possivel recuperar para o estabelecimento o grupo de centralizacao do Codigo de Tipo de Documento.

90125
O Codigo do Tipo de Documento nao esta cadastrado


MFS1020256
RN07

Campo Indicador da Pessoa Física/Jurídica

Campo de preenchimento obrigatório.

Domínio de Valores válidos: '1', '2', '3', '4', '5'.

Quando não preenchido ou inválido, o registro não será excluído, e no log do processo será gravada uma mensagem de erro:

90088
O Indicador de Pessoa Fisica/Juridica nao esta preenchido ou com informacao invalida.

MFS1020256
RN08

Campo Código da Pessoa Física/Jurídica

Campo de preenchimento obrigatório.
Tabela de Origem: SAFX04 - Cadastro de Pessoa Fis/Jur

Quando o campo não for preenchido ou preenchido com informação inválida, o registro não será excluído, e no log de erros será gravada uma das mensagens de erro:

90087
Nao foi possivel recuperar para o estabelecimento o grupo de centralizacao do Codigo de Pessoa Fisica/Juridica.

90089
O Codigo da Pessoa Fisica/Juridica nao esta preenchido

A partir do conteúdo dos campos 04 e 05 (indicador e código da pessoa fis/jur) será verificada a existência da pessoa informada na Tabela de Pessoas Fis/Jur (SAFX04). Quando não encontrada, o registro não será excluído, e no log do processo será gravada uma mensagem de erro:

90124
O Codigo da Pessoa Fisica/Juridica nao esta cadastrado.


MFS1020256
RN09
Campo Número do Documento Fiscal

Campo de preenchimento obrigatório.

Quando não preenchido, o registro não será excluído, e no log do processo será gravada uma mensagem de erro:

90112
O Campo Numero do Documento nao esta preenchido.


MFS1020256
RN10

Campo Série do Documento Fiscal

Campo não obrigatório

Colocar um caracter de espaço caso estiver vazio

MFS1020256
RN11

Campo Subsérie do Documento Fiscal

Campo não obrigatório

Colocar um caracter de espaço caso estiver vazio

MFS1020256
RN12
Fechamento do Grupo:

Se o documento fiscal que se deseja excluir pertencer a um período já fechado

90807 -  Nao e permitido importar/alterar Documentos Fiscais quando a Data Fiscal/Data Extemporanea e menor ou igual a Data de Fechamento do Grupo de Docs.

Usar a função SAF_FECHAMENTO_OL com os parâmetros (P_COD_EMPRESA, P_COD_ESTAB, 3, DT_FECHAMENTO_W, ST_FECHA_W);
MFS1020256
RN12
Deleção do Documento Fiscal
Recuperar o documento fiscal na tabela definitiva X07_DOCTO_FISCAL partir dos campos informados no layout.

Caso não seja encontrado documento fiscal, o registro não será excluído, e no log de erros será gravada uma mensagem de erro:

"Código: 92975
Mensagem: O documento fiscal informado nao foi identificado na Tabela de Documentos Fiscais."

Caso seja encontrado documento fiscal, excluir da tabela X07_DOCTO_FISCAL e de todas as tabelas filhas que fazem parte do documento fiscal.
X07_DOCTO_FISCAL
X07_TRIB_DOCFIS
X07_BASE_DOCFIS
X07_CUPOM_FISCAL
EST_GNRE_DOCFIS
X08_ITENS_MERC
X08_TRIB_MERC
X08_BASE_MERC
X09_ITENS_SERV
X09_TRIB_SERV
X09_BASE_SERV
X112_OBS_DOCFIS
X113_AJUSTE_APUR
X114
X115
X116
X117
X118
X110_ITEM_ROMANEIO
X119_ITENS_MEDICAMENTO
X120_ITENS_ARMA
X325
X326
X331_PRG_FIDEL_FAT_NFE
X332
X333
X50_TRANSP_DOCFIS
X51_ITENS_FRETE
X701_VOO_PASSAG

A lista de tabelas não está completa, deve-se fazer o levantamento via banco através das FKs para a tabela X07_DOCTO_FISCAL e demais tabelas filhas.

MFS1020256
RN13
Data Mart Automático

Caso o Data Mart esteja parametrizado para ser executado automaticamente, a exclusão também será aplicada nas tabelas do Data Mart: DWT_DOCTO_FISCAL DWT_ITENS_MERC e DWT_ITENS_SERV, DWT_DOCTO_FISCAL_SPED.
MFS1020256

RN14
Auditoria

Disponibilizar informações para auditoria da deleção, como o usuário que enviou o arquivo via SFTP.

MFS1020256
RN15
Acompanhamento do Processo

O módulo de Processos Customizados disponibiliza uma tela para consulta dos processos executados.

MFS1020256

Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN




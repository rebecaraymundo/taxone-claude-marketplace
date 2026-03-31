# REQ_DIMP

- **Fonte:** REQ_DIMP.docx
- **Modificado:** 2025-03-18
- **Tamanho:** 87 KB

---

THOMSON REUTERS

__	__

Revisões

__Data__

__OS/Chamado__

__Descrição__

__Autor__

Sumário

[1\.	INTRODUÇÃO	3](#_Toc87519355)

[1\.1	Documentos e Base Legal para a Solução	3](#_Toc87519356)

[2\.	PROCEDIMENTOS PARA CONTEÚDO	3](#_Toc87519357)

[2\.1	Criação / Alteração em telas e relatórios \(manual operacional, roteiro e help\)	3](#_Toc87519358)

[2\.1\.1	Manual Operacional – DIMP	3](#_Toc87519359)

[2\.1\.2	Roteiro – DIMP	4](#_Toc87519360)

# <a id="_Toc200962059"></a><a id="_Toc200996459"></a><a id="_Toc200996577"></a><a id="_Toc200998055"></a><a id="_Toc354574223"></a><a id="_Ref354574309"></a><a id="_Ref354574320"></a><a id="_Toc354574398"></a><a id="_Toc354574442"></a><a id="_Toc354574527"></a><a id="_Toc354578073"></a><a id="_Toc354578300"></a><a id="_Toc354578991"></a><a id="_Toc354579132"></a><a id="_Toc87519355"></a>INTRODUÇÃO

Este documento tem como objetivo demonstrar o manual operacional e roteiro de utilização do novo módulo DIMP de acordo com o layout disponibilizado pela Confaz\.

Embasamento legal:

Ato Cotepe/ICMS 65/18, de19 de dezembro de 2018\.

Convênio ICMS 134/2016 – ementa 71/20

[*https://www\.confaz\.fazenda\.gov\.br/legislacao/arquivo\-manuais*](https://www.confaz.fazenda.gov.br/legislacao/arquivo-manuais)

# <a id="Premissas"></a><a id="_Toc200962071"></a><a id="_Toc200996470"></a><a id="_Toc200996588"></a><a id="_Toc200998068"></a><a id="_Toc354574229"></a><a id="_Toc354574404"></a><a id="_Toc354574448"></a><a id="_Toc354574533"></a><a id="_Toc354578079"></a><a id="_Toc354578306"></a><a id="_Toc354578997"></a><a id="_Toc354579138"></a><a id="_Toc87519357"></a>PROCEDIMENTOS PARA CONTEÚDO

<a id="_Toc199304378"></a><a id="_Toc200962072"></a><a id="_Toc200996471"></a><a id="_Toc200996589"></a><a id="_Toc200998069"></a>

## <a id="_Toc200996472"></a><a id="_Toc200996590"></a><a id="_Toc200998070"></a><a id="_Toc354574231"></a><a id="_Toc354574406"></a><a id="_Toc354574450"></a><a id="_Toc354574535"></a><a id="_Toc354578081"></a><a id="_Toc354578308"></a><a id="_Toc354578999"></a><a id="_Toc354579140"></a><a id="_Toc87519358"></a>Criação / Alteração em telas e relatórios \(manual operacional, roteiro e help\)

### <a id="_Toc87519359"></a>Manual Operacional – DIMP

__Localização__: Módulo: Estadual

                       Menu: DIMP

Manual Operacional

DIMP – Declaração de Informações de Meios de Pagamentos\.

Introdução

Neste modulo será gerado o arquivo DIMP \(Declaração de Informações de Meios de Pagamentos\) para contribuintes de instituições financeiras e de pagamentos, integrantes ou não do Sistema de Pagamentos Brasileiros – SPB, relativas as transações mercantis com cartões de débito, crédito, de loja \(private label\) e demais instrumentos de pagamento eletrônico, bem como, sobre o fornecimento de informações prestadas por intermediadores \(agenciadores, plataformas de delivery, marketplaces e similares\) de serviços e de negócio referente a transações\.

Deverão ser gerados 27 arquivos mensais, sendo que para as unidades de Federação em que não existir transações, deverá ser enviado o arquivo com finalidade ‘zerado’\.

A Obrigação DIMP contempla as seguintes tabelas para geração do arquivo, SAFX312 Cadastro de Meios de Pagamentos, SAFX313 Movimentação Financeira, SAFX314 Cadastro de Autorização para Instituição Parceira, SAFX315 Cadastro da Van do Cliente e SAFX316 Transação Van do Cliente\.

As tabelas deverão ser preenchidas de acordo com a obrigatoriedade de cada cliente e regra de negócio\.

Menu Parâmetro

Neste Menu o usuário poderá preencher os dados de cadastro van do cliente, transação van do cliente, autorização da instituição parceira, cadastro de meios de pagamentos e movimentação financeira, bem como gerar relatório de cada tela\.

Parâmetro – Cadastro Van do Cliente – Registro 0105\.

O objetivo desta tela é associar o cadastro dos clientes informados no registro 0100 e que utilizam a estrutura de tecnologia do declarante do arquivo VAN para captura de transações, sendo a liquidação do pagamento efetuada pelo CNPJ informado nesse registro\.

Descrições dos campos:

Código Empresa: Informar o código da empresa escolhido pelo usuário, na tela de login do sistema\.

Código de Estabelecimento: Informar o código de estabelecimento de acordo com grupo e validade associado\.

Fís\./Jur \(Gr\./Cód\./Ind\./Val\.\): Informar o código da Pessoa Física ou Jurídica correspondente a operação de acordo com a tabela X04\_PESSOA\_FIS\_JUR\.

Validade: Informar da data inicial de validade\.

CNPJ VAN: Informar o CNPJ da Instituição de Pagamento VAN\.

OBS: O CNPJ associado deve estar cadastrado na tabela Safx04 \- Código de Estabelecimento: Informar o código de estabelecimento de acordo com grupo e validade associado\.

Nome Comercial Van: Informar o nome comercial da VAN\.

Para conferência clicar no ícone de relatório da tela\.

Parâmetro – Transação Cliente Van – Registro 0105\.

A tela de transação Van está associada a tela de Cadastro Van do Cliente, ou seja, para abrir a tela de transação e informar o período de movimentação e quantidade de movimentos deve primeiro cadastrar o cliente e depois associar com a instituição de pagamento Van\.

Período Movimentação: Informar a data de movimentação\.

Quantidade: Informar a quantidade de transações que foram realizadas no terminal cadastrado para o cliente\. \(Obrigatório a partir de 01/2023\)

Para conferência clicar no ícone de relatório da tela\.

Parâmetro – Autorização Instituição Parceira – Registro 0600\.

A tela de autorização instituição parceira atende o registro 0600, quando a finalidade do arquivo for 6 – Autorização para Instituição Parceira\. Este parâmetro é exclusivo para instituição de pagamentos ou marketplace cujas transações serão formalmente enviadas por outra instituição de pagamento ou marketplace\.

O arquivo com a autorização para Instituição parceira irá gerar apenas os Registros abaixo:

0000,0001,0005,0600,0990,1001,1990,9001,9990,9900 e 9999\.

Descrições dos campos:

Código de Estabelecimento: Informar o código de estabelecimento de acordo com grupo e validade associado\.

Fís\./Jur \(Gr\./Cód\./Ind\./Val\.\): Informar o código da Pessoa Física ou Jurídica correspondente a operação de acordo com a tabela X04\_PESSOA\_FIS\_JUR\.

Tipo de Autorização: Informar 1 – Inclusão ou 2 – Exclusão\.

Transações Comerciais: 0 – Não ou 1 – Sim\.

Data de Habilitação: Informar a data de início da autorização\.

Data Fim Hab\.: Informar a data fim da autorização\.

Para conferência clicar no ícone de relatório da tela\.

Parâmetro – Cadastro Meios de Pagamentos – Registro 0200\.

Esta tela tem como objetivo cadastrar os meios de pagamentos para geração do registro 0200\.

Descrições dos campos:

Estabelecimento: Informar o estabelecimento\.

Código Meio de Captura: Informar o código de meio de captura\.

Tipo de Tecnologia: Informar o tipo de tecnologia de acordo com as opções abaixo:

1 – TEF \-POS INTEGRADOS;

2 – MOBILE;

3 – POS;

4 – E – COMMERCE;

5 – DEMAIS TECNOLOGIAS;

6 – URA/MOTO;

7 – PAGAMENTO EFETUADO EM DINHEIRO OU POR OUTRA ESTRUTURA;

Tipo Terminal: Informar o tipo de terminal, 0 – Terminal próprio ou 1 – Terminal de terceiro\.

Num Log: Informar o número do log\.

Inst\. Pagto\./Intermediador: Informar a marca indicando a Instituição de Pagamento ou Intermediador identificado no comprovante\.

Para conferência clicar no ícone de relatório da tela\.

Parâmetro – Movimento DIMP – Registros 0100, 0300, 1100, 1110, 1115, 1120, 1200 e 1220;

Esta tela tem como objetivo demonstrar as operações financeiras e seus detalhes\.

Código de Estabelecimento: Informar o código de estabelecimento de acordo com grupo e validade associado\.

Data Operação: Informar data de operação:

Instituição Parceira \(Gr\./Cód\./Ind\./Val\.\): Informar o código da instituição parceira correspondente a operação de acordo com a tabela X04\_PESSOA\_FIS\_JUR\.

Instituição Cliente \(Gr\./Cód\./Ind\./Val\.\): Informar o código do cliente correspondente a operação de acordo com a tabela X04\_PESSOA\_FIS\_JUR\.

Pagto\. Exterior: Informar pagamento no exterior, 0 – Não ou 1 – Sim\.

Oper\. Extemporânea: Informar operação extemporânea, 0 – Não ou 1 – Sim\.

Cód\. Meio Captura: Informar o código de meio de captura de acordo com o cadastro da tabela X312\_dimp\_mcapt\.

Valor Total Operação: Informar o valor do total da operação\.

OBS: Regra de validação procedure

I – Uma única operação:

Agrupa por empresa, estabelecimento, ident da instituição parceira, ident cliente e indicador comex\.

II – Totalizador com operação de dois meios de pagamentos

Agrupa por empresa, estabelecimento, ident da instituição parceira, ident cliente e indicador comex \+ ID trasação complementar quando os códigos são iguais\.

III – Totalização por dia:

Agrupa por empresa, estabelecimento, ident da instituição parceira, ident cliente e indicador comex \+ data operação\.

Qtd\. Total Operação: Informar a quantidade total da operação\.

OBS: Regra de validação procedure

I – Uma única operação:

Agrupa por empresa, estabelecimento, ident da instituição parceira, ident cliente e indicador comex\.

II – Totalizador com operação de dois meios de pagamentos

Agrupa por empresa, estabelecimento, ident da instituição parceira, ident cliente e indicador comex \+ ID trasação complementar quando os códigos são iguais\.

III – Totalização por dia:

Agrupa por empresa, estabelecimento, ident da instituição parceira, ident cliente e indicador comex \+ data operação\.

CNPJ Adquirente: Informar o CNPJ da Adquirente\.

Num\. Seq\. Único \(NSU\): Informar o código NSU \(número sequencial único\)\.

Cód\. Autorização: Informar o código de autorização atribuído pela Instituição de Pagamento\.

ID\. Transação Pagto\.: Informar a identificação de transação de pagamento\. \(quando diferente do NSU\)

Split: Informar o indicador de operação, 0 – Não splitado ou 1 – Splitado\.

Bandeira: Informar a bandeira do cartão do cliente\.

Hora Transação: Informar hora da transação\.

Valor Operação: Informar o valor da operação\.

Nat\. Oper\. Pagamento:  Informar a natureza de operação\.

1 – Cartão de Crédito;

2 – Cartão de Débito;

3 – Boleto de transações próprias;

4 – Transferência de Recursos;

5 – Pagamento efetuado em dinheiro ou por outra estrutura;

6 – Pix \(valido para arquivos enviados a partir de 11/2021\);

7 – Voucher;

8 – Saque em estabelecimento comercial;

9 – Outros \(válido para arquivos enviados até 11/2021\);

10 – Depósito;

11 – Recepção de pagamento de boletos, guias emitidas por terceiros e recargas de celular;

Cód\. Georreferenciamento: Informar a antena de celular que autorizou a operação\.

Chave NFE/NFCE: Informar a chave de acesso da nota fiscal referente a operação\.

CNPJ/CPF Destinatário: Informar o CNPJ ou CPF do destinatário que efetuou a compra\.

Código Destinatário: Informar o código do destinatário quando não preenchido o campo CNPJ/CPF destinatário\.

Situação: Informar a situação da operação S – Cancelado ou N – Normal\.

Data Cancelamento: Informar a data de cancelamento\.

Valor Cancelamento: Informar o valor do cancelamento\.

Cód\. Chave NFs\-E: Informar a chave de acesso da nota fiscal referente a operação\.

Cód\. Chave Dc\-E: Informar a chave da declaração de conteúdo eletrônico referente a operação\.

Operação Intermediação Comercial/Pagamentos: Informar se a operação é intermediação comercial ou de pagamentos com 0 – Não realiza intermediação de transação de terceiros ou 1 – Realiza intermediação de terceiros\. \(Informação para o preenchimento do campo 14 – IND\_SUB registro 0100\)\.

UF Saída Mercadoria: Informar a UF de saída de mercadoria\.

CNPJ Saída Mercadoria: Informar o CNPJ de saída da mercadoria\.

ID transação Complementar: Informar o número de identificação interno\. \(OBS: Quando existir um pagamento duplo para uma operação, repetir o número do ID nas duas operações\)\.

Para conferência clicar no ícone de relatório da tela\.

Menu Geração 

Geração do Meio Magnético\.

Esta tela tem como objetivo programar a geração do arquivo DIMP\.

Data Início: Informar a data de inicial do período de geração do arquivo em que o usuário deseja gerar\.

Data Fim: Informar a data fim do período de geração do arquivo em que o usuário deseja gerar\.

UF: Informar a UF que o usuário deseja gerar o arquivo\.

Finalidade do Arquivo: Informar qual finalidade do arquivo\.

Exemplo: 1 – Remessa de arquivo normal;

                2 – Remessa de arquivo de retificação de informações;

                3 – Remessa de arquivo para atender notificação;

                4 – Remessa de arquivo zerado;

	   5 – Remessa de arquivo de encerramento de atividade;

 	   6 – Autorização para instituição parceira;

Tipo de Ambiente: Informar com o tipo de ambiente, Produção ou Homologação\.

 

Versão do Layout: 07

Estabelecimento: Informar qual estabelecimento deseja gerar o arquivo\.

Geração – Processos/Arquivos\.

Na tela de processos identificamos os arquivos gerados\.

Destino: Informar local para salvar o log/arquivo, local/rede ou Servidor \(banco de dados\)

Tamanho máximo por volume: Informar o tamanho do arquivo\.

Diretório: informar o diretório onde será salvo o log/arquivo\.

Salvar Processos selecionados: clicar em salvar\.

### <a id="_Toc87519360"></a>Roteiro – DIMP

ROTEIRO DE UTILIZAÇÃO  
DIMP

Procedimento para Geração do Meio Magnético

Para realizar a geração do arquivo Dimp seguir os passos abaixo\.

1. Efetuar a [importação](file:///C:/mastersaf/Executaveis_BACKUP/Help_on_line/basicos/ferramentas/oper_saffr.htm#menu_IMPORTAR_TFA) da Tabela Estados \(TFIX04\)
2. Efetuar a [importação](file:///C:/mastersaf/Executaveis_BACKUP/Help_on_line/basicos/ferramentas/oper_saffr.htm#menu_IMPORTAR_TFA) dos cadastros relacionados as operações DIMP através da tabela safx04 no módulo Basicos/Job Servidor\.
3. Efetuar a importação das tabelas no módulo Básicos/Job Servidor:

- Safx312 – Registro 0200;
- Safx313 – Registros 0100, 0300, 1100, 1110, 1115, 1120, 1200 e 1220;
- Safx314 – Registro 0600;
- Safx315 – Registro 0105;
- Safx316 – Registro 0105;

1. Manutenções

Para realizar manutenção dos dados importados\.

Mastersaf Dw – Estadual – DIMP\.

Parâmetros – Cliente VAN;

Parâmetros – Transação VAN;

Parâmetros – Autorização Instituição Parceira;

Parâmetros – Meio de Captura;

Parâmetros – Movimento DIMP;

1. Gerações 

Para geração do arquivo seguir os passos abaixo:

Mastersaf Dw – Estadual – DIMP – Geração – Geração do meio magnético\.

Data Início: Informar a data de inicial do período de geração do arquivo em que o usuário deseja gerar\.

Data Fim: Informar a data fim do período de geração do arquivo em que o usuário deseja gerar\.

UF: Informar a UF que o usuário deseja gerar o arquivo\.

OBS: Para seleção todas as federações o módulo já verifica quais federações não tem movimento e gera o arquivo com finalidade 4\.

Finalidade do Arquivo: Informar qual finalidade do arquivo\.

Exemplo: 1 – Remessa de arquivo normal;

                2 – Remessa de arquivo de retificação de informações;

                3 – Remessa de arquivo para atender notificação;

                4 – Remessa de arquivo zerado;

	   5 – Remessa de arquivo de encerramento de atividade;

 	   6 – Autorização para instituição parceira;

Tipo de Ambiente: Informar com tipo de ambiente, Produção ou Homologação\.

 

Versão do Layout: 07

Estabelecimento: Informar qual estabelecimento deseja gerar o arquivo\.

1. Processos/Arquivos

Após a geração do arquivo na aba processos identificará os processos gerados e ao selecionar o processo abrirá a aba de arquivos onde apresenta os arquivos gerados\.

Na aba arquivos selecionar o arquivo desejado e escolher onde será salvo\.

- Loca/Rede
- Servidor \(Banco de dados\)
- Informar o Diretório e salvar\.


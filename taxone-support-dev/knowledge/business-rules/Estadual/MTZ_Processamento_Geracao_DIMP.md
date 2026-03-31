# MTZ_Processamento_Geração_DIMP

> Fonte: MTZ_Processamento_Geração_DIMP.docx












THOMSON REUTERS

Processamento de Geração Dimp (Declaração de Informações de Meios de Pagamentos)
Localização: MastersafDW >> Estadual >> DIMP>> Geração.



















Sumário

1.	CONTROLE DE ALTERAÇÕES	3
2.	INTRODUÇÃO	4
2.1.	Os arquivos DIMP são enviados por UF de cadastro do recebedor dos recursos informados no registro 0100. As informações somente serão enviadas a outra UF se ocorrer a solicitação formal do envio das informações ou nas transações reportadas por intermediadores, com preenchimento do registro 1120 e UF de destino diferente da UF do vendedor.	4
3.	DOCUMENTOS DE REFERÊNCIA	6
4.	TERMOS TECNICOS	7
5.	TABELAS	9
6.	DEFINIÇÃO DAS REGRAS	9
7.	TELA DE GERAÇÃO DO ARQUIVO	16




















## CONTROLE DE ALTERAÇÕES





















## INTRODUÇÃO


Este documento tem por objetivo a geração do arquivo digital referente à Declaração de informações de Meios de Pagamentos DIMP, prestadas por instituições financeiras e de pagamentos, integrantes ou não do Sistema de Pagamentos Brasileiros – SPB, relativas às transações mercantis com cartões de débito, credito, de loja (private label) e demais instrumentos de pagamento eletrônico, bem como, sobre o fornecimento de informações prestadas por intermediadores (agenciadores, plataformas de delivery, marketplaces e similares) de serviços e de negócio referente a transações.
Deverão ser gerados 27 arquivos mensais, sendo que para as unidades da Federação em que não existir transações, deverá ser enviado o arquivo com finalidade ‘zerado’.
#### Os arquivos DIMP são enviados por UF de cadastro do recebedor dos recursos informados no registro 0100. As informações somente serão enviadas a outra UF se ocorrer a solicitação formal do envio das informações ou nas transações reportadas por intermediadores, com preenchimento do registro 1120 e UF de destino diferente da UF do vendedor.

As informações prestadas por instituições financeiras e de pagamentos, integrantes ou não do sistema de pagamento brasileiro, bem como as prestadas por intermediadores de serviços e de negócio, exigidas pelo Convenio 134/2016 de 09/12/2016, serão geradas mensalmente em um arquivo único para cada unidade da Federação, com transmissão via TED-TEF (programa que válida, gera, Declaração digitalmente e transmite o arquivo para o Fiscos Estaduais.

A Obrigação DIMP contempla 5 tabelas para geração do arquivo, SAFX312 Cadastro de Meios de Pagamentos, SAFX313 Movimentação Financeira, SAFX314 Cadastro de Autorização para Instituição Parceira, SAFX315 Cadastro da Van do Cliente e SAFX316 Transação Van do Cliente.
As tabelas deverão ser preenchidas de acordo com a obrigatoriedade de cada cliente e regra de negócio.

O arquivo obedece às especificações técnicas do layout e terá como finalidade a remessa do arquivo:
Original

Substituto para retificação de informações (arquivo para substituição integral de informações prestadas pela Instituição referentes exclusivamente ao período objeto da retificação. Este arquivo sobrescreve, inclusive, as transações ajustadas extemporaneamente).

Específico para cumprimento de notificação para um CPF/CNPJ referente ao período solicitado, apresentação de arquivo zerado ou de encerramento de atividades.

A apresentação dos blocos deve obedecer a sequência a seguir apresentada, sendo que o registro de abertura do bloco indicará se haverá ou não informações.

Blocos estruturantes:

0 – Abertura, identificação e referencias das Instituições;
1 – Operações de pagamento e demais transações;
9 – Controle e encerramento do arquivo digital.



Versões de leiaute atendidas:
- Leiaute 06 – vigência de 01/01/2021 a 31/10/2021 [MFS-79177]
- Leiaute 07 - vigência é a partir de 01/11/2021 a 31/12/2022 [MFS-91838]
- Leiaute 08 – vigência a partir de 01/01/2023 (substituída pela versão 09)
- Leiaute 09 – vigência é a partir de 01/04/2023
- Leiaute 10 – vigência é a partir de 01/06/2025
## DOCUMENTOS DE REFERÊNCIA

Manual Layout DIMP versão 7

https://www.confaz.fazenda.gov.br/legislacao/arquivo-manuais

## TERMOS TECNICOS


- Adquirente: A adquirente é a ferramenta responsável por processar o pagamento tanto no e-commerce quanto nas lojas físicas, fazendo a comunicação entre os estabelecimentos comerciais, as bandeiras e os bancos emissores dos cartões.

- Subadquirente: As subadquirentes são empresas que fazem a intermediação dos pagamentos entre todos agentes e sua função é transmitir os dados da transação a adquirente e liquidar os recebiveis junto aos lojistas.

- Intermediador: Intermediadores de pagamento, também conhecidos como subadquirentes, são soluções que conectam os consumidores, os lojistas e as adquirentes, que são as empresas responsáveis por processar e liquidar as transações por cartão.

- Seller: Dentro do universo do e-commerce, é a forma como é chamado o vendedor que disponibiliza seus produtos em sites que atuam como marketplaces

- Olist: É uma plataforma que conecta a sua loja virtual ao seu público na internet, funciona comoum facilitador de processos, uma conexão Segura entre lojistas e consumidores.

- Gateway: Faz o papel de processar o pagamento no momento do checkout e facilitar a integração das lojas com os diversos meios de pagamento existentes no mercado ao transmitir os dados fornecidos pelos varejistas. A comunicação da loja virtual com o gateway ocorre por meio de um webservice que é disponibilizado como API (interface de programação de aplicativos).

- Meio de Captura: Sistema usado para capturar a venda realizada.

- Transações cross border: Cross border, ou cross-border trade, é uma expressão de língua inglesa que pode ser traduzida como “comércio transfronteiriço”. Refere-se à prática comercial de ampliar as vendas para outros países, fazendo com que seus produtos cruzem a fronteira.

- NSU: Número sequencial único é o número de identificação de uma operação de venda realizada com cartões. É atribuído a cada documento fiscal emitido.

- Split: O Split de pagamentos do Pagar.me é a solução que divide uma transação em quantas partes (recebedores) forem necessárias para que cada participante da venda receba seu respectivo valor.

- Bandeira: As bandeiras de cartão são as empresas que fazem a comunicação entre a adquirente e o banco emissor do cartão.

- Van: Value Adde Network (Rede de Valor Agredado) VAN é uma rede privada que permite que empresas troquem informações de forma segura. No caso da VAN Bancária, a troca ocorre entre os bancos e os clientes.

- Chargeback: O termo chargeback vem do inglês e significa estorno. No que se refere às transações virtuais, é o cancelamento de uma compra realizada por meio do cartão de crédito ou de débito.

- Tef – Pos: Tef é a sigla transferência eletrônica de fundos e POS ponto de venda.

- Mobile: Pagamento via tecnologia smartphones.

- Pos: Transações financeiras

- E-commerce: E-commerce, ou comércio eletrônico, refere-se às vendas pela internet, mais especificamente, as que são realizadas por uma única empresa.

- Ura/moto: Unidade de Resposta Audível, MOTO (mail order / telephone order).
- Marketplace: O marketplace remete a um conceito mais coletivo de vendas online. Nessa plataforma, diferentes lojas podem anunciar seus produtos, dando ao cliente um leque de opções.

- PIX: O PIX permite a transferência de valores em dinheiro em poucos segundos, em qualquer horário ou dia.

- Private label: Private Label é um tipo de terceirização da produção, em que uma empresa contrata outra para o desenvolvimento de um serviço ou produto com o seu nome.



## TABELAS


Para informações de cada tabela SAFX, consultar o documento DEXPARA_DIMP.

## DEFINIÇÃO DAS REGRAS




Os registros de encerramento serão calculados pela procedure de acordo com a movimentação de dados.


## TELA DE GERAÇÃO DO ARQUIVO


Mastesaf DW à Estadual à Dimp à Geração

Processos:


Arquivos:


| Data | Demanda | Descrição | Autor |
| --- | --- | --- | --- |
| 29/07/2021 |  | Reserva das tabelas safx312. Safx313 e safx314 | Juliana Ogaua |
| 05/08/2021 |  | Solicitação do licenciamento modulo DIMP DW | Daniel Oliveira |
| 16/08/2021 |  | Reserva das tabelas safx315 e safx316 | Juliana Ogaua |
| 31/08/2021 |  | Reserva de código de erros | Juliana Ogaua |
| 23/09/2021 |  | Reserva de código de erros | Juliana Ogaua |
| 11/09/2021 |  | Reserva de código de erros | Juliana Ogaua |
| 13/01/2022 | MFS-79177 | A DIMP foi criada atendendo a versão de leiaute 07. Esta MFS tem como objetivo contemplar o leiaute 06 da DIMP. Leiaute 06 – vigência de 01/01/2021 a 31/10/2021 Leiaute 07 - vigência é a partir de 01/11/2021 | Liliane Assaf |
| 29/06/2022 | MFS-86995 | Alteração na geração do Registro 1110 para retirar o campo de ID Transação Complementar na regra de agrupamento. (ocasionando erro no validador). | Rogério Ohashi |
| 09/08/2022 | MFS-91838 | Inclusão da nova versão 09 do layout com vigência a partir de 01/04/2023. | Aline Melo |
| 01/02/2023 | MFS436070 | Ajuste da obrigatoriedade do campo 04-QTDE do registro 0105 e inclusão de mensagem na tela de Cadastro de Transações VAN. | Aline Melo |
| 06/02/2023 | MFS436204 |  | Aline Melo |
| 18/02/2025 | MFS748247 | Inclisão da Versão versão 10 | Graciela Soares |


| Registro | Regra |
| --- | --- |
| 0000 - Abertura do arquivo digital e identificação da Instituição de Pagamento, financeira ou do Intermediador  Regra transferida para doc do Bloco 0 | Para o preenchimento do Registro 0000, o programa irá buscar os dados da tela de geração e do Parâmetro de Empresa/Estabelecimento. Para os campos 05 - CNPJ e 06 - Nome do Layout DIMP é preenchido através das informações contidas no parâmetro Estabelecimento. Os demais campos será preenchido conforme tela de Parâmetros de Geração do arquivo Dimp. Observação: Quando a indicação for código 6 - Autorização para Instituição Parceira no campo 03, deverá ter o cadastro da Autorização da Instituição Parceira SAFX314 para que seja gerado o Registro 0600. Para as Federações sem movimento o programa já irá gerar com finalidade 4 – Arquivo zerado para que não tenha que gerar novamente um a um.   Versões do layout atendidas: 06 – vigência de 01/01/2021 a 31/10/2021 [MFS-79177] 07 - vigência é a partir de 01/11/2021 a 31/03/2023 [MFS-91838] 08 – vigência a partir de 01/01/2023 (substituída pela versão 09) 09 – vigência a partir de 01/04/2023 10 – vigência a partir de 01/06/2025 |
| 0001 - Abertura do Bloco 0 Regra transferida para doc do Bloco 0 | Será preenchido de acordo com o preenchimento do Registro 0000 |
| 0002 - Abertura do Bloco 0 Regra constante no Doc do Bloco 0 | Será preenchido de acordo com o preenchimento do Registro 0002 a Partir da versão do Layout 10 |
| 0005 - Dados Complementares do Autor do Arquivo Regra transferida para doc do Bloco 0 | [MFS436204] Para consultar as regras a partir da versão 09, verificar os documentos: MTZ-DIMP_Regras_Bloco_0.docx DIMP_DEPARA.xlsx       O preenchimento do Registro 0005, o programa irá buscar os dados do Parâmetro de Empresa/Estabelecimento e do parâmetro de responsável. Mastersaf DW à Básicos à Parâmetros à Preliminares à Empresa/Estabelecimento.   Campo 07 - Nome da pessoa responsável para contato = Parâmetro responsável + campo contabilista responsável do parâmetro de dados iniciais do Sped Fiscal. Mastersaf DW à Básicos à Sped à EFD – Escrituração Fiscal Digital à Parâmetros àDados Iniciais à Campo Contabilista Responsável. |
| 0100 - Tabela de Cadastro do Cliente Regra transferida para doc do Bloco 0 | O preenchimento do Registro 0100 irá buscar os dados do cadastro da tabela safx04. OBS: O campo 14 - Indicador de operação de intermediação comercial e/ou de pagamentos será preenchido através da tabela safx313 campo 32. |
| 0105 Tabela de Van do Cliente Regra transferida para doc do Bloco 0 | O preenchimento do Registro 0105 será preenchido através da safx315 associação do código de cliente com o cadastro de Van do cliente e safx316 transação de movimentação Van do cliente. Mastersaf DW à Estadual à Dimp à Parâmetros à Cliente Van    Mastersaf DW > Estadual > Dimp > Parâmetros > Transações VAN  OBS: Quantidade Obrigatório a partir de 01/2023.  [ADO436070] Se o período informado no campo “Período Movimentação” for a partir de 01/01/2023 e o campo Quantidade NÃO for preenchido, a operação não será salva e será exibida a seguinte mensagem de erro: “Para o período informado, não foi informada a quantidade de transações.”. |
| 0200 Tabela de Cadastro de Meio de Captura Regra transferida para doc do Bloco 0 | O preenchimento do Registro 0200 será preenchido através da tabela safx312 tabela de cadastro de Meio de Captura. |
| 0300 Dados da Instituição Parceira | O preenchimento do Registro 0300 será preenchido através da tabela de cadastro safx04 cadastro de pessoa física e jurídica. OBS:O Registro 0300 está associado ao Registro 1100 campo 2. |
| 0600 Autorização para Instituição Parceira | O preenchimento do Registro 0600 será preenchido através da tabela safx314 - Cadastro de Autorização Para Instituição Parceira. OBS: O arquivo irá preencher o registro 0600 quando a finalidade no Registro 0000 campo 3 for do tipo 6. A partir da data da emissão de autorização, a outorgante não poderá mais enviar arquivos com suas transações, concedendo essa autonomia as parceiras. No arquivo de autorização deve ser informado, obrigatoriamente, os registros 0000,0001,0005,0600,0990,1001,1990,9001,9990,9900 e 9999. O Uso da Finalidade 6 é exclusivo para uma instituição de pagamento ou Marketplace. Mastesaf DW à Estadual à Dimp à Parâmetros à Autorização da Instituição Parceira. |
| 1001 Abertura do Bloco 1 | O preenchimento do Registro 1001 será preenchido de acordo com a movimentação de dados do arquivo. |
| 1100 Resumo mensal das Operações de Pagamento | O preenchimento do registro 1100 será preenchido de acordo com os dados informados na tabela safx313 Movimentação Financeiras. |
| 1110 Operações Diárias de Pagamento Por Meio de Captura | O preenchimento do registro 1110 será preenchido de acordo com os dados informados na tabela safx313 Movimentação Financeiras. [MFS86995] Alteração da regra de agrupamento na geração do 1110 (Totalizador com operação de dois meios de pagamentos. Regras campo 11 - VLR_TOT  I – Uma única operação: Agrupar por empresa, estabelecimento, ident da instituição parceira, ident cliente e indicador comex. II – Totalizador com operação de dois meios de pagamentos: Agrupa por empresa, estabelecimento, ident da instituição parceira, ident cliente e indicador comex + ID trasação complementar quando os códigos são iguais. III – Totalização por dia: Agrupa por empresa, estabelecimento, ident da instituição parceira, ident cliente e indicador comex + data operação. Regra campo 12 QTD_TOT I – Uma única operação: Agrupar por empresa, estabelecimento, ident da instituição parceira, ident cliente e indicador comex. II – Totalizador com operação de dois meios de pagamentos: Agrupa por empresa, estabelecimento, ident da instituição parceira, ident cliente e indicador comex + ID trasação complementar quando os códigos são iguais: III – Totalização por dia. Agrupa por empresa, estabelecimento, ident da instituição parceira, ident cliente e indicador comex + data operação. |
| 1115 Operações por Comprovante de Transação | O preenchimento do registro 1115 será preenchido de acordo com os dados informados na tabela safx313 Movimentação Financeiras. |
| 1120 Intermediador de Serviços e Negócios | O preenchimento do registro 1120 será preenchido de acordo com os dados informados na tabela safx313 Movimentação Financeiras. |
| 1200 Cancelamento Extemporâneo | O preenchimento do registro 1200 será preenchido de acordo com os dados informados na tabela safx313 Movimentação Financeiras. OBS: A Procedure irá validar se o campo Data de Cancelamento está no mês de geração do arquivo. |
| 1220 Cancelamento Transação de Intermediador | O preenchimento do registro 1220 será preenchido de acordo com os dados informados na tabela safx313 Movimentação Financeiras. OBS: A Procedure irá validar se o campo Data de cancelamento está no mês de geração do arquivo. |


| 1990 Encerramento do Bloco 1 |
| --- |
| 9 Controle e encerramento do Arquivo Digital |
| 9900 Registro do arquivo |
| 9990 Encerramento do Bloco 9 |
| 9999 Encerramento do Arquivo Digital |

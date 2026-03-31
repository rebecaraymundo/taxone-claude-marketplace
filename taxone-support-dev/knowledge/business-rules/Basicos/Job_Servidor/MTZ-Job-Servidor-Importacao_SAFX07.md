# MTZ-Job-Servidor-Importacao_SAFX07

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX07.docx
- **Modificado:** 2026-02-10
- **Tamanho:** 91 KB

---

__         __

# Módulo Job Servidor – Importação SAFX07 \(Capa de Documento Fiscal\)

                      Localização: Menu Básicos, Módulo: Job Servidor, item Importação 🡪 Execução

*\(Obs: As regras descritas neste documento são numeradas de acordo com os campos  da SAFX07, conforme o Manual de Layout,  o que facilita a consulta\) *

*\(Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como  RN00\)\.*

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS 3132

DW \- ESTADUAL \- SEF\-PE \- Atendimento a TELECOM \- Revisão da OS2867

Revisão geral da geração dos registros 76 e 77 para o SEF\-PE\.

OS3169\-DW1

Novo campo para o Bloco D do Pis/COFINS

Inclusão do campo Indicador da Natureza de Frete para atender o Bloco D do PIS/Cofins\.

OS\-2931\-D

Alteração no tamanho do campo NRO\_AIDF\_NF

Alterado o tamanho do campo NRO\_AIDF\_NF conforme novo layout do guia prático do SPED Fiscal, versão 2\.0\.4\.

OS3065\-DW

Novos campos

Inclusão de novos campos na SAFX07 para atendimento ao SEF II – PE\.

OS3065\-A

Geração do arquivo LA\-ICMS do SEFII

Geração do arquivo LA\-ICMS do SEFII \(parte 1\)\.

OS3141

Nova crítica de importação\.

Nova crítica de importação para documentos de entrada que seja cancelado e emitido por terceiros\.

OS3410

Inclusão de item no campo 119

Inclusão de item no campo 119

OS3169\-GE16

Criar Indicador para Documentos de Invoice na SAFX07

O cliente Chevron necessita informar os Documentos de Invoice para geração dos registros A100, A120 e A170 do EFD PIS/COFINS\. Ocorre que pela regra do EFD PIS/COFINS informada no Guia Prático versão 1\.0\.3 de 01/09/2011, esses documentos de importação devem ser gerados nos registros A100, A120 e A170\.

Para que o cliente utilize corretamente esses documentos e que os mesmos não sejam lidos erroneamente para outras obrigações, deverá ser criado um Indicador na capa do Documento Fiscal que diferencie o Invoice de Documentos Fiscais de Serviço comuns\.

OS3513

Data Fiscal

Alteração no tratamento da data fiscal de saída de mercadoria\.

OS3564

Novo código de modelo – 58\.

Novo código de modelo de Documento Fiscal \- Manifesto Eletrônico de Documentos Fiscais \- MDF\-e\.

OS3557

Crítica no campo de classe de consumo

Crítica no campo de classe de consumo para atendimento do SPED FISCAL

CH\_7058\-A\_2012

Correção do tratamento da data fiscal

Quando os documentos possuírem data fiscal igual á data de saída/recebimento da mercadoria, desconsiderar o tratamento do parâmetro “Data fiscal – Saídas de mercadorias”

OS3556

Criar Indicador para Notas Fiscais de Venda Emitidas por Terceiros

O cliente Açúcar Guarani exerce operações de venda de cana de açúcar, e conforme artigo 6 do anexo X do RICMS/SP, estão dispensados da emissão de NF\-e para justificar esta venda, onde conforme legislação a nota é emitida pelo adquirente da cana\.

  
No entanto, não conseguem escriturar esse documento corretamente no MasterSAF, visto que não é possível identificar a direção de emissão de terceiros para esta NFe de saída\.

Este fato está causando impacto na entrega da obrigação EFD PIS/COFINS, pois a NF\-e segue como emissão própria quando na verdade a emissão foi de terceiros\.

OS3696\-DW

Alterações do SEF II PE

Alteração na lista de valores do campo 255\-NF Emitida em Contingência

OS\_3749

Criação de campos

Criação de campos reservados

OS3743

Inclusão de Campo

Inclusão dos campos Identificador do Documento Fiscal  e Código do Sistema de Origem na SAFX07\.

OS3717

Inclusão de opção no campo Natureza da Base de Crédito

Incluir a opção ‘10 \- Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado \(crédito com base no valor de aquisição\)\.’

OS4316

Criação de Campos

Criação dos campos Código e Descrição da SCP	

OS4514

Criação de Campos

Criação de campos para atendimento ao e\-Social

CH13277\_2014

Inclusão novos conteúdos no campo “NF Emitida em Contingência”

Este documento tem como objetivo incluir os conteúdos: <a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK11"></a><a id="OLE_LINK12"></a><a id="OLE_LINK13"></a><a id="OLE_LINK14"></a>Emissão em contingência com SVC\-NA<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a><a id="OLE_LINK17"></a> e Emissão em contingência com SVC\-RS, no campo “NF Emitida em Contingência”, ajustando também a crítica de importação\.

OS4514\-D

Criação de Campos

Criação de campos para atendimento ao e\-Social

OS4579

Elenilson Coutinho

Alteração no tamanho do campo NUM\_LANCAMENTO

MFS2101

Criação de Campos

Novos campos para atendimento ao Ato Cotepe ICMS 44/2015 \(ver __RN283__, __RN284__ e __RN285__\)

MFS\-2967

Inclusão de Campos

Criação de campos para atendimento ao e\-Social

OS3341

Criação de campo

Criação de campo para receber o número de documento fiscal de serviço quando o mesmo for maior que 12 posições\.

CH19066\_2014

Alteração na descrição dos modelos 27, 29 e 30 do campo 229 \- COD\_MODELO\_COTEPE

Este documento tem como objetivo alterar a descrição dos modelos 27, 29 e 30 do campo 229 \- COD\_MODELO\_COTEPE de acordo com a tabela 4\.1\.1 do SPED\.

CH17235\_2015

Inclusão de Modelo de Documento

Este documento tem como objetivo incluir o conteúdo código de modelo do documento fiscal 59\-Cupom Fiscal Eletrônico – CF\-e \(CF\-e\-SAT\) no campo 229 da SAFX07\.

OS3888\-A3

DW \- MUNICIPAL \- Gerenciador ISS \- Tratamento de Divergências \(gerar NFS Complementar\)

Inclusão de nova opção no campo Tipo do RPS da Nota Fiscal Eletrônica\.

CH119738

Nova mensagem de crítica

Nova mensagem de Crítica para quando o CFOP for nulo ou estiver vazio\.

MFS8789

Ajuste no tamanho do campo Código CEI para atender ao REINF

Para atender o REINF, foi ajustado o tamanho do campo Código CEI\.

MFS11800

Criação de campo

Este documento tem como objetivo criar campo de CPF/CNPJ do Consumidor em atendimento a NFC\-e\.

CH13577\_2017 \(MFS12877\)

Alteração da descrição do campo CPF/CNPJ do Consumidor/ Produtor

Este documento tem como objetivo alterar o nome do campo CPF/CNPJ do Consumidor para CPF/CNPJ do Consumidor/ Produtor, em atendimento ao e\-Social Evento S\-1250\.

MFS13120

Criação de campo

Este documento tem como objetivo criar campo de Nº Certificado Qualidade em atendimento ao i\-SIMP\.

MFS13290

Alteração do campo 72

Inclusão de duas novas opções no campo “72\-Indicador do Tipo de Frete”\.

CH17739\_2017 \(MFS\-13849\)

Alteração dos campos 287 e 288 

Os campos 287 e 288 sofreram alteração na Descrição e Comentário para melhor o entendimento no momento do seu preenchimento\.

MFS9525

Alteração Campo Indicador de Prestação de Serviços em Obra

Alteração Campo Indicador de Prestação de Serviços em Obra, excluindo a opção 3 – Obra de Construção Civil \- Subempreitada

MFS17919

Inclusão de campos para atender ao REINF

Para atender o registro R\-2020 do REINF, foram criados 5 novos campos   

MFS\-19270

Inclusão de Modelo de Documento

Este documento tem como objetivo incluir o conteúdo código de modelo do documento fiscal 63\-Bilhete de Passagem Eletrônico \- BP\-e e 67\-Conhecimento de Transporte Eletrônico para Outros Serviços \- CT\-e OS no campo 229 da SAFX07\.

MFS\-20029

Alteração do campo Tipo de Aquisição/Comercialização da Produção\.

Este documento tem como objetivo incluir novos valores válidos para o campo da Campo Tipo de Aquisição/Comercialização da Produção conforme atualização da nota técnica 08/2018 e Social\.

MFS\-20985

Criação de campo

Este documento tem como objetivo criar o campo “Valor Total do IPI Devolvido” em atendimento a NT 2016\.002 V4\.0 referente a capa da nota fiscal de Mercadoria, no qual resultará a somatória do IPI Devolvido dos itens\.

MFS\-20913

Alteração do campo 276 – 

IND\_TIPO\_AQUIS

Essa alteração tem como objetivo incluir um novo valor válido para o campo, vide EFD REINF \- Ajustes Layout 1\.4\.

MFS22545

Criação de campo

Criação dos campos 298 e 299 \(Valor SEST e Valor SENAT\)

MFS31259

Criação de campo

Criação dos campos 300 e 301 \(Valor Finalidade Emissão da NFe e Chave de Acesso da NFe Substituída\)

MFS33987

Alteração de campo

Inclusão de modelo de documento no campo “229\-Código Modelo NF”\.

MFS32070

Criação de campo

Inclusão do campo “302\- Indicador de preenchimento dos Valores de ICMS cobrados anteriormente por ST”

MFS\-58346

Alteração do campo 276 – 

IND\_TIPO\_AQUIS

Inclusão da opção 0\- Aquisição de produção de produtor rural pessoa física ou segurado especial para fins de exportação no campo 32\- IND\_TIPO\_AQUIS, para atender o layout 1\.5\.1\. do EFD\-REINF \(RN276\)

MFS64383

Inclusão do campo 303 \- IND\_TRIB\_PRODUTOR\_CP

Criação do campo 303 \- IND\_TRIB\_PRODUTOR\_CP, para atender o layout 1\.5\.1 do EFD\-REINF \(estamos utilizando o mesmo domínio do campo 33\-IND\_TRIB\_PRODUTOR\_CP definido para a SAFX63\)  \(RN303\)

MFS58553

Alteração no campo 125 \- IND\_SITUACAO\_ESP

\- Campo 125 \(Situação Especial\): inclusão do código “E”

MFS73688

Criação de Campos

Sped Fiscal Atualização 2022 :

__RN304__ Inclusão do campo Modelo do Documento Fiscal NF Substituida\.

__RN305__: Inclusão do campo Código de Autenticação Digital \(Convênio 115/2003\) Substituida\.

__RN306__: Inclusão do campo Energia Injetada\.

__RN307__: Inclusão do campo Outras Deduções\.

MFS90399

Alteração no campo 175 \- DT\_PAGTO\_NF

\- Campo 175 \(Data de Pagamento da Nota Fiscal\): Tratamento para aceitar o valor de ‘00000000’

MFS90034

Criação de Campos

Sped Fiscal Atualização 2023:

Alteração nas regras de validação dos campos para contemplar o novo Código do Modelo 62: RN229, RN300, RN304, RN305\.

Inclusão do campo Tipo Faturamento \(NFe\): RN308\.

MFS523869

Alteração no campo 125 \- IND\_SITUACAO\_ESP

Inclusão do códigos F,  em atendimento ao modelo 63\.

MFS652063

Inclusão de Campos novos para a NFCom

Inclusão de Campos novos para a NFCom

MFS784653

Inclusão de Campos novos para a NFCom

Inclusão de Campos novos para a NFCom: itens 331 ao 336\.

MFS\-851680

Alessandra Cristina Navatta

Aumento do campo 81 \- Canal de Distribuição/Código Obra \(RN81\)

__MFS877174__

Liliane Assaf

Criação da tabela particionada DWT\_DOCTO\_FISCAL\_SPED espelho da DWT\_DOCTO\_FISCAL

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Data Fiscal__

Com a empresa/estabelecimento devidamente parametrizada, então ao incluir uma nota fiscal de saída de mercadoria no sistema, sendo por importação ou digitação, o sistema assumirá a “Data Fiscal” como sendo a “Data E/S”, ou seja:

Se o campo 03 \(MOVTO\_E\_S\) da SAFX07 = ‘9’

E campo 12 \(COD\_CLASS\_DOC\_FIS\) = ‘1’ ou ‘3’ ou ‘7’, então

Verificar se o documento já existe na base com a DATA\_FISCAL igual á data de escrituração ORIGINAL do sistema, ou seja, Data Fiscal = Data de emissão \(Campo 11 da SAFX07\)

Se sim, então não importar e emitir a seguinte mensagem no log de importação:

“Documento fiscal não importado, pois já existe na base com “Data Fiscal” igual á “Data de Emissão” \(Escrituração antiga\)”\.

Se não, então importar o documento e considerar DATA\_FISCAL = campo 20 \(DATA\_SAIDA\_REC\)\.

Esta regra somente será valida Se campo 01 \(COD\_EMPRESA\) OU campo 02 \(COD\_ESTAB\) corretamente parametrizado em  "Módulo: Básicos > Parâmetros, Menu: Preliminares > Parametrização para Data Fiscal"

Caso não exista a parametrização, o documento seja de entrada ou não seja de mercadoria, 

__*Crítica para quando o novo parâmetro para Data Fiscal NÃO estiver configurado no estabelecimento:*__

Se o campo 03 \(MOVTO\_E\_S\) da SAFX07 = ‘9’

E campo 12 \(COD\_CLASS\_DOC\_FIS\) = ‘1’ ou ‘3’ ou ‘7’, então

Verificar se o documento já existe na base com a DATA\_FISCAL igual á data de escrituração NOVA do sistema, ou seja, Data Fiscal = Data de Saída/Recebimento \(Campo 20 da SAFX07\)

Se sim, então não importar e emitir a seguinte mensagem no log de importação:

“Documento fiscal não importado, pois já existe na base com “Data Fiscal” igual á “Data de Saída/Recebimento” \(Escrituração Nova\)”\.

Se não, então importar o documento e continuar escriturando da forma como é feita hoje:

\- Notas de entrada = data de saída/recebimento \(campo 20 da SAFX07\);                                                                             

\- Notas de saída = data da emissão do documento \(Campo 11 da SAFX07\)\.  

\[__Alteração__ – CH7058\-A\_2012\]

__Atenção:__ Se o campo 11, data da emissão \(DATA\_EMISSAO\) for igual á data do campo 20, Data de saída/Recebimento  \(DATA\_SAIDA\_REC\), então desconsiderar o tratamento do parâmetro da Data Fiscal\. Devendo assim não emitir as críticas dessa regra\.

__OS3513 / CH7058\-A\_2012__

__RN00A__

__Regra do Controle de Concorrência entre processos de Importação e Equalização__

O controle de concorrência garante que não seja executado simultaneamente mais de um processo de importação das SAFX07, SAFX08, SAFX09 e equalização DataMart, referenciados por uma determinada empresa e estabelecimento\.

Com a liberação da MFS\-87822 o controle de concorrência entre processos de importação e equalização de documento fiscal passou a considerar também o período \(mês/ano\) dos documentos fiscais\. Ou seja, o controle passou a ser feito por empresa, estabelecimento e período \(mês/ano\) dos documentos fiscais\.

Tabelas utilizadas pelo Controle de Concorrência:

\- PRT\_IDENT\_DMART\_PERÍODO: Controle por empresa, estabelecimento e período\.

\- PRT\_IDENT\_DMART: Controle por empresa, estabelecimento\.

Antes da MFS\-87822, o controle de concorrência por empresa, estabelecimento e período era realizado apenas na equalização DataMart\.

Com a MFS\-82822 a tabela PRT\_IDENT\_DMART\_PERÍODO passa a ser utilizada na equalização e na importação dos documentos fiscais\.

Exemplo de controle de processos ao serem executados simultaneamente:

\-  Dois processos: um de Importação e outro de Importação;

\-  Dois processos: um de Equalização e outro de Equalização;

\-  Dois processos: um de Importação e outro de Equalização;

Determinação do período para controle de concorrência:

1. Importação com uso do Limita período:

Período considerado para o controle de concorrência = período informado na tela de programação da importação\.

1. Importação sem limita período:

Período considerado para o controle de concorrência = período determinado pelo mês/ano da data da nota\.

1. Equalização Data Mart:

Período considerado para o controle de concorrência = período informado na tela de programação da importação\.

Nesse controle de concorrência estão sendo consideradas as duas formas de importação, batch e online\.

__\[MFS877174\]__

Quando o Estabelecimento estiver parametrizado para executar o Data Mart automático, importação das SAFX07, SAFX08 e SAFX09, irá carregar as tabelas do Data Mart: DWT\_DOCTO\_FISCAL DWT\_ITENS\_MERC e DWT\_ITENS\_SERV, 

A partir da MFS877174 todas as capas de documentos fiscais gravadas na DWT\_DOCTO\_FISCAL, também são gravadas na DWT\_DOCTO\_FISCAL\_SPED

MFS87822

__RN03__

__Campo 03\-Movimento Entrada/Saída:__

__Nova Crítica de importação \(OS3141\):__

Emitir a crítica *“Nota Fiscal de entrada cancelada emitida por terceiro importada”* no relatório de importação para os documentos que se enquadram nos critérios descritos abaixo:

\- Documento de entrada emitido por terceiros, ou seja, Campo 03 \(MOVTO\_E\_S\) da SAFX07 = “1” \(Documento de Entrada, Documento de Terceiros\);

E

\- Documento cancelado, ou seja, campo 30 \(SITUACAO\) da SAFX07 = “S” \(Nota Fiscal regularmente cancelada\)\.

Obs\.: O documento será importado normalmente, como já é feito atualmente\.

__OS3141__

__RN12__

__Campo 12\-Classificação do Documento Fiscal:__

__Criação de novo item para o campo Código de Classificação de Documento Fiscal:__

Alterar a rotina de importação para que seja considerado na mesma o item “I” \(Documento Internacional/Invoice\) que foi criado no campo 12 – COD\_CLASS\_DOC\_FIS da tabela SAFX07/X07\_DOCTO\_FISCAL/DWT\_DOCTO\_FISCAL\.

__OS3169\-GE16__

__RN13__

__Campo 13 \- COD\_MODELO__

Aceitar a importação do novo código de modelo “58”\.

__OS3564__

__RN14__

__Campo 14\-Código Fiscal \(CFOP\): __

Se o campo 12 \(COD\_CLASS\_DOC\_FIS\) da SAFX07 = “1” ou “7”  

E o campo 14 \(COD\_CFO\)  da SAFX07 estiver vazio: “” ou Nulo: “@”, então 

emitir a mensagem de crítica 90028 da tabela CAT\_ERRO\.

“CFOP \- Codigo Fiscal de Operacao e Prestacao deve ser preenchido”

Importar o documento normalmente\.

__CH119738__

__RN72__

__Campo 72\-Indicador do Tipo de Frete__

Alteração __MFS13290__: A lista de opções do campo do campo “72\-Indicador do Tipo__ de Frete__” foi alterada para a inclusão das novas opções “3” e “4”:

1\-Frete para Conta do Emitente \(CIF\);

2\-Frete para Conta do Destinatário \(FOB\);

__3\-Transporte Próprio por conta do Remetente;__

__4\-Transporte Próprio por conta do Destinatário;__

0\-Outros;

Quando o campo estiver preenchido, o conteúdo informado deve ser = '0', '1', '2', ‘3’ ou ‘4’, caso contrário, será gravada mensagem de erro no log \(código de erro = 90145\), e o registro não será importado\.

__MFS13290__

__RN81__

__Campo 81 \- Canal de Distribuição/Código Obra__

A rotina de Importação do módulo JOB Servidor deve ser ajustada para que contemple a alteração de aumento do campo COD\_CANAL\_DISTRIB da tabela SAFX07\- Arquivo de Notas Fiscais\. 

__![](data:image/png;base64,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)__

__Item__: 81

__Nome__: COD\_CANAL\_DISTRIB

__Descrição__: Canal de Distribuição/Código da Obra

__Tamanho__: 15

__Tipo__: A

__Obrigatoriedade__: N

__MFS\-851680__

__RN97__

__Campo 97– Número da Autorização de Impressão de Documentos Fiscais:__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alterada para contemplar o campo Indicador

__OS\-2931\-D__

__RN119__

__Campo 119\-Tipo de Dispositivo de Segurança:__

Alterar a importação para que possa considerar o novo item \(Conhecimento de Transporte Eletrônico\) que foi criado no campo 119 – COD\_TP\_DISP\_SEG,  da tabela de  “Arquivo de Notas Fiscais”\.

__OS3410__

__RN125__

__Campo 125 \- Situação Especial__

Obrigatoriedade: Não obrigatório

Tamanho: 001

Tipo: A

Lista de códigos válidos para preenchimento deste campo:

1 \- Nota Fiscal de Venda Globalizada de acordo com o Protocolo ICMS 52/2000 \(Cláusula Quarta\);

2 \- Nota Fiscal de Acompanhamento de ECF;

3 \- NF não considerada no livro de apuração do ICMS \- Crédito Presumido de ICMS \- AM;

4 \- NF de Sinistro;

5 \- NF Complementar ou CT\-e de Complemento de Valores \(modelo: 57\);

6 \- Nota Fiscal para cancelamento cupons fiscais;

7 \- NF de Ressarcimento de Substituição Tributária;

8 \- NF de Remessa por Conta e Ordem;

9 \- NF escriturada sem que o valor do ICMS destacado seja contabilizado nos livros de entrada \(P1\) e apuração \(P9\), conforme IN DRP 45/98 \- RICMS/RS Livro II art\. 153\.

A \- NF de Venda Fora do Estabelecimento\. \(Este campo é utilizado para identificação das NF's de venda ambulante emitidas fora do estabelecimento\)

B \- CT\-e emitido em hipótese de anulação de débito \(modelo: 57\);

C \- CT\-e substituto ao CT\-e cancelado \(modelo: 57\);

D \- Venda para entrega futura”\.

E \- Nota Fiscal Eletrônica de Ajuste;

F – BP\-e substituição \(modelo 63\)\.

Caso o registro importado esteja preenchido com um valor não contido na lista acima, exibir a seguinte mensagem:

*O campo Indicador de Notas fiscais Especiais com informacao invalida\.*

\[__MFS58553__\]: inclusão do código “E”

__MFS58553__

__MFS523869__

__RN172__

__Campo 172 \- Código CEI__

Obrigatoriedade: Não obrigatório

Tamanho: 015

Tipo: A

__MFS8789__

__RN175__

__Campo 175 – Data de Pagamento da Nota Fiscal__

__Tabela: __SAFX07

__Item: __175

__Nome do Campo:__ DT\_PAGTO\_NF

__Descrição:__ Data de Pagamento da Nota Fiscal

__Tipo:__ N

__Tamanho: __008

__Chave__: Não

__Não Obrigatório__

__Comentário: __Informar a data efetiva do pagamento da nota fiscal para o fornecedor da mercadoria e/ou serviço\. 

Alguns municípios especificam a data de recolhimento baseados na data efetiva de pagamento da nota fiscal, a partir dessa informação será efetuado o cálculo da data de recolhimento do ISS\.

__\[ALTERAÇÃO\-MFS90399\] __Tratamento para o valor de data preenchida com ‘00000000’

__Se__ o campo de o Campo de  DT\_PAGTO\_NF estiver preenchido com ‘00000000’

  __Permitir__ a importação considerando como valor __nulo__

__Obs\.: __Trata\-se da mesma regra implementada para o Campo 75 – DAT\_DI\.

__MFS90399__

__RN185__

__Campo 185 – NUM\_LANCAMENTO__

__Tabela: __SAFX07

__Item: __185

__Nome do Campo:__ Número do Lançamento

__Descrição:__ NUM\_LANCAMENTO

__Tipo:__ A

__Tamanho: __040

__Chave__: Não

__Não Obrigatório__

__Comentário: __Número do Lançamento Contábil \- Ato Cotepe 70/05 \- Registro B020 / E100 / E020

__OS4579__

__RN195__

__Campo 195 – Classe de Consumo – SPED FISCAL \(COD\_CLASSE\_CONSUMO\)__

O código da classe de consumo informado para o campo 195 da SAFX07 é validado na Tabela de Classes de Consumo \(DWT\_CLASSE\_CONSUMO\), verificando se ele existe na tabela com modelo = modelo da nota, e indicador = “1”\. 

O indicador serve para identificar a qual obrigação se refere os códigos da tabela, onde neste caso será sempre “1”, pois trata\-se de SPED FISCAL\.

Este tratamento já existe atualmente, porém deve ser validado com a equipe de Qualidade se a importação está atendendo os novos códigos\.

Quando o código informado não for encontrado na tabela nas condições estabelecidas, gravar a mensagem abaixo no log, e não importar o registro:

                     “Código da classe de consumo do SPED FISCAL inexistente ou inválido para o modelo do documento fiscal”

Obs\.: Esta mensagem pode ser alterada por A&D ou Conteúdo, caso julguem necessário\. Não encontrei mensagem semelhante na TFIX22\.

__OS3557__

__RN221__

__Campo 221\-Tipo do RPS da Nota Fiscal Eletrônica:__

Alterar a rotina de Exportação para que seja considerada a nova opção “RPS\-G – Recibo Provisório de Serviço Complementar proveniente do Gerenciador de ISS” do campo Tipo do RPS da Nota Fiscal Eletrônica\.

__OS3888\-A3__

__RN229__

__Campo 229 – Código Modelo NF \(COD\_MODELO\_COTEPE\)__

__\[ALTERADA – CH17235\_2015\]__

Aceitar a importação do novo código de modelo: “58”, “59”, “60”, “65”\.

__\[ALTERADA – MFS\-19270\]__

Aceitar a importação do novo código de modelo: “63”, “67”\.

__\[ALTERADA – CH19066\_2014\]__

Alterar a descrição dos modelos:

27 \- Nota Fiscal de Serviço de Transporte Ferroviário

29 \- Nota Fiscal/Conta de Fornecimento de Água Canalizada

30 \- Manifesto de Vôo

__\[ALTERADA – MFS\-33987\]__

Inclusão do modelo 66 \- Nota Fiscal de Energia Elétrica Eletrônica – NF3e

__\[ALTERADA – MFS90034 – Sped Fiscal 2023\]__

Inclusão do modelo 62 – “Nota Fiscal Fatura Eletrônica de Serviços de Comunicação – NFCom”\.

__OS3564__

__CH19066\_2014__

__CH17235\_2015__

__MFS\-19270__

__MFS33987__

__RN244__

__Campo 244 – Código da Classe de Consumo para o SEF\-PE__

O campo de código da classe de consumo não será obrigatório\.

Caso o código informado não esteja contido na lista de valores previstos para o SEF\-PE, apresentar a mensagem no log:

Crítica: Código da classe de consumo inválido para o SEF\-PE\.

Solução: Consulte o manual de orientação do SEF\-PE para verificar a lista dos códigos permitidos\.

 

Alteração da OS3065\-A: Alterada a regra de validação do campo, para atender as duas versões do SEF \(SEF e SEF II\):

__Validação atual__ \(antes da OS3065\-A\) 🡺 o código informado é validado na Tabela de Classes de Consumo, buscando pelos critérios:  modelo = modelo da nota  e  indicador = “2”

*\(o indicador serve para identificar a qual obrigação se refere os códigos da tabela, e 2 indica SEF\-PE\)*

__Nova validação__ \(a partir da OS3065\-A\) 🡺 devido à nova versão do SEF, \(SEF II\), foi incluída uma nova lista de códigos nesta tabela, que receberam o indicador = “3”, indicando tratar\-se da obrigação SEF II\.

Com isso, a validação passou a ser feita a partir de uma data parametrizada no Módulo SEF II, da seguinte forma:

Parâmetros que serão utilizados na validação:

 

- Parâmetro “*Mês/Ano inicial da entrega do SEF II*” \(Módulo SEF II – PE, menu “Dados Iniciais”\)
- Data fiscal do documento

Validação:

__Se__ mês/ano do parâmetro não existente __ou__ nulo:

      Valida se o código da classe de consumo existe na tabela nas seguintes condições: 

- Modelo = modelo do documento \(campo “13\-Modelo do Documento”\);
- Indicador de Uso  = __“2”__ \(indicando que a obrigação é o  __SEF\-PE__\);

__Senão__

      __Se__ o mês/ano da data fiscal do documento for igual ou superior ao mês/ano do parâmetro 

            Valida se o código da classe de consumo existe na tabela nas seguintes condições: 

- Modelo = modelo do documento \(campo “13\-Modelo do Documento”\);
- Indicador de Uso  = __“3”__ \(indicando que a obrigação é o  __SEF II\-PE__\);

      __Senão __

            Valida se o código da classe de consumo existe na tabela nas seguintes condições: 

- Modelo = modelo do documento \(campo “13\-Modelo do Documento”\);
- Indicador de Uso  = __“2”__ \(indicando que a obrigação é o  __SEF\-PE__\);

__OS 3132__

__OS3065\-A__

__RN244__

Quando o código informado não for encontrado na tabela nas condições estabelecidas, será gravada a seguinte mensagem no log, e o registro não será importado: “Código da classe de consumo inexistente ou inválido para a data da nota fiscal”\.

Obs: Para obter o parâmetro da data do SEF II, será feita a pesquisa pela parametrização do Estabelecimento\. Caso não exista, será verificada a parametrização a partir do Estabelecimento Centralizador, caso o estabelecimento em questão conste como componente de alguma centralização \(centralização dos estabelecimentos por inscrição estadual única que consta no módulo de controle das obrigações estaduais\)\.  

__OS 3132__

__OS3065\-A__

__RN245__

__Campo 245– Indicador da Natureza de Frete:__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alterada para contemplar o campo Indicador da Natureza de Frete na tabela SAFX07\.

Tabela: __SAFX07__

Item: __Sugerido 245__

Descrição: __Indicador da Natureza de Frete__

Nome do Campo: __Será definido pelo A&D__

Comentário: __Opções de Preenchimento: __

0 – Operações de vendas, com ônus suportado pelo estabelecimento vendedor 

1 – Operações de vendas, com ônus suportado pelo adquirente

2 – Operações de compras \(bens para revenda, matérias primas e outros   produtos, geradores de crédito

3 – Operações de compras \(bens para revenda, matérias primas e outros  produtos, não geradores de crédito

4 – Transferência de produtos acabados entre estabelecimentos da pessoa jurídica

5 – Transferência de produtos em elaboração entre estabelecimentos da pessoa jurídica

9 – Outros 

Tamanho: __001__

Tipo: __N__

Obrigatório

__OS3169\-DW1__

__RN254__

__Campo 254 \- Natureza da Base de Crédito \(EFD\-PIS/PASEP\-COFINS\)__

Incluir a opção ‘10 \- Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado \(crédito com base no valor de aquisição\)’, no campo Natureza da Base de Crédito\.

__OS3717__

__RN255__

__Campo NF Emitida em Contingência__:      \(campo criado na OS3065\-dw\)

Campo do tipo S/N

Obrigatório 🡪 Não 

Críticas 🡪 quando preenchido, o conteúdo deve ser =  “S” ou “N”, caso contrário, será gravada a seguinte mensagem  no log e o registro não será importado:  “*Campo NF Emitida em Contingência com conteúdo inválido\. Informar “S” ou “N”*

Alteração da OS3696\-DW:

__\[ALTERADA – CH13277\_2014\]__

Alterada a crítica do campo “*255\-NF Emitida em Contingência*” para considerar a nova lista de valores válidos, como descrito a seguir:

    Valores originais 

S / N

Nova lista de valores 

N, S, 1, 2, 3, 4, 5 e 6

Crítica 🡪 *Quando preenchido*, o conteúdo do campo deverá ser um dos novos valores da lista acima\. Caso contrário, será gravada a mensagem abaixo no log e o registro não será importado: 

                      “Campo NF Emitida em Contingência com conteúdo inválido\. Informar S, N, 1, 2, 3, 4, 5 ou 6\.”

OS3065\-DW

__OS3696\-DW__

__CH13277\_2014__

__RN256__

__Campo Valor Acréscimo:                            __\(campo criado na OS3065\-dw\)

Obrigatório 🡪 Não 

Críticas 🡪 sem críticas

__OS3065\-dw__

__RN257__

__Campo Valor da Antecipação Tributária:    __\(campo criado na OS3065\-dw\)

Obrigatório 🡪 Não 

Críticas 🡪 sem críticas

__OS3065\-dw__

__RN259__

__Campo Reservado 01__

Alterar a rotina de importação para contemplar este campo

Tabela: SAFX07

Item: A ser agendado pelo A&D

Nome do Campo: Reservado 1

Descrição: DSC\_RESERVADO1

Tipo: A

Tamanho 50

Comentário: Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

Não obrigatório\.

__OS\_3749__

__RN260__

__Campo Reservado 02__

Alterar a rotina de importação para contemplar este campo

Tabela: SAFX07

Item: A ser agendado pelo A&D

Nome do Campo: Reservado 2

Descrição: DSC\_RESERVADO2

Tipo: A

Tamanho 50

Comentário: Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

Não obrigatório\.

__OS\_3749__

__RN261__

__Campo Reservado 03__

Alterar a rotina de importação para contemplar este campo

Tabela: SAFX07

Item: A ser agendado pelo A&D

Nome do Campo: Reservado 3

Descrição: DSC\_RESERVADO3

Tipo: A

Tamanho 50

Comentário: Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

Não obrigatório\.

__OS\_3749__

__RN263__

__Campo 263\-Nota Fiscal de Venda Emitida por Terceiro:__

Alterar a rotina de Importação Batch para que seja considerado o novo campo “Nota Fiscal de Venda Emitida por Terceiro” criado na tabela SAFX07\.

Caso durante a rotina de importação o campo “Nota Fiscal de Venda Emitida por Terceiro” esteja preenchido e o campo 03 – MOVTO\_E\_S <> “9” da SAFX07, o sistema deverá exibir uma mensagem de erro no log de importação e não devem importar o dado\. A mensagem a ser exibida é:

“Nao sera permitida a importacao de uma NF de Venda para Terceiro cujo campo Indicador de E/S seja diferente de 9\.”

Só será permitida a importação de Documentos Fiscais na SAFX07 cujo “Nota Fiscal de Venda Emitida por Terceiro” esteja preenchido, caso o campo 03 – MOVTO\_E\_S = 9\.

__OS3556__

__RN264__

__Campo Reservado 04__

Alterar a rotina de importação para contemplar este campo

Tabela: SAFX07

Item: A ser agendado pelo A&D

Nome do Campo: Reservado 4

Descrição: DSC\_RESERVADO4

Tipo: A

Tamanho 50

Comentário: Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

Não obrigatório\.

__OS\_3749__

__RN265__

__Campo Reservado 05__

Alterar a rotina de importação para contemplar este campo

Tabela: SAFX07

Item: A ser agendado pelo A&D

Nome do Campo: Reservado 5

Descrição: DSC\_RESERVADO5

Tipo: A

Tamanho 50

Comentário: Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

Não obrigatório\.

__OS\_3749__

__RN266__

__Campo Reservado 06__

Alterar a rotina de importação para contemplar este campo

Tabela: SAFX07

Item: A ser agendado pelo A&D

Nome do Campo: Reservado 6

Descrição: DSC\_RESERVADO6

Tipo: N

Tamanho: 015V002

Comentário: Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

Não obrigatório\.

__OS\_3749__

__RN267__

__Campo Reservado 07__

Alterar a rotina de importação para contemplar este campo

Tabela: SAFX07

Item: A ser agendado pelo A&D

Nome do Campo: Reservado 7

Descrição: DSC\_RESERVADO7

Tipo: N

Tamanho: 015V002

Comentário: Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

Não obrigatório\.

__OS\_3749__

__RN268__

__Campo Reservado 08__

Alterar a rotina de importação para contemplar este campo

Tabela: SAFX07

Item: A ser agendado pelo A&D

Nome do Campo: Reservado 8

Descrição: DSC\_RESERVADO8

Tipo: N

Tamanho: 015V002

Comentário: Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

Não obrigatório\.

__OS\_3749__

__RN269__

__Campo 269\-Identificador do  Documento Fiscal__

__Tabela: __SAFX07

__Item: __A ser definido pelo A&D

__Nome do Campo:__ Será definido pelo A&D

__Descrição:__ Identificador do Documento Fiscal

__Tipo:__ A

__Tamanho: __128

__Não Obrigatório__

__Comentário: __Informar o Identificador do Documento Fiscal

__OS3743__

__RN270__

__Campo 270\-Código do  Sistema de Origem__

__Tabela: __SAFX07

__Item: __A ser definido pelo A&D

__Nome do Campo:__ Será definido pelo A&D

__Descrição:__ Código do Sistema de Origem

__Tipo:__ A

__Tamanho: __004

__Não Obrigatório__

__Comentário: __Informar o código do Sistema de Origem

__OS3743__

__RN271__

__Campo 271\-Código da SCP__

Alterar a rotina de importação para que seja considerado o novo campo:

Tabela: SAFX07

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

Deverá existir um cadastro correspondente na SAFX2057 para o código informado\. Caso não exista, retornar a mensagem: “Cadastro da SCP não encontrado”\.

__OS4316__

__RN272__

__Campo 272\-Indicador de Prestação de Serviços em Obra__

Obrigatoriedade: Não Obrigatório

Item: A ser reservado pelo A&D

Descrição: Indicador de Prestação de Serviços em Obra

Nome do Campo: A ser reservado pelo A&D

Comentário: Indicador de prestação de serviços em obra de construção civil\. 

__\[Alteração MFS9525\]__

Preencher com:

0 \- Não é obra de construção civil ou não está sujeita a matrícula;

1 \- Obra de Construção Civil \- Empreitada Total;

2 \- Obra de Construção Civil \- Empreitada Parcial;

3 \- Obra de Construção Civil \- Subempreitada\.

Tamanho: 001

Tipo: A

Validação deste campo: O conteúdo do Indicador de Prestação de Serviços em Obra deve ser igual a <0>, <1>, <2>, <3> ou não ser informado\. Caso seja diferente de um destes valores, retornar a mensagem: “Indicador de Prestação de Serviços em Obra Inválido\. Conteúdo do campo deve ser igual a <0>, <1>, <2>, <3> ou não preenchido”\.

__OS4514__

__MFS9525__

__RN273__

__Campo 273\-Tipo do Processo__

Obrigatoriedade: Não Obrigatório

Item: A ser reservado pelo A&D

Descrição: Tipo do Processo

Nome do Campo: A ser reservado pelo A&D

Comentário: Tipo do Processo Jurídico\. 

Preencher com:

1 \- Administrativo

2 \- Judicial

Tamanho: 001

Tipo: A

Validação deste campo: O conteúdo do Tipo do Processo deve ser igual a <1>, <2> ou não ser informado\. Caso seja diferente de um destes valores, retornar a mensagem: “Tipo do Processo Inválido\. Conteúdo do campo deve ser igual a <1>, <2> ou não preenchido”\.

__OS4514__

__RN274__

__Campo 274\-Número do Processo__

Obrigatoriedade: Não Obrigatório

Item: A ser reservado pelo A&D

Descrição: Número do Processo

Nome do Campo: A ser reservado pelo A&D

Comentário: Número do Processo Jurídico\.

Tamanho: 020

Tipo: A

__OS4514__

__RN275__

__Campo 275\-Abrangência da Decisão do Processo__

Obrigatoriedade: Não Obrigatório

Item: A ser reservado pelo A&D

Descrição: Indicador de abrangência da decisão originada do processo\.

Preencher com:

1 \- Todos os estabelecimentos do contribuinte

2 \- Estabelecimento\(s\) relacionado\(s\)\.

Nome do Campo: A ser reservado pelo A&D

Comentário: Valor da Contribuição Destinada ao SENAR, Incidente sobre a Aquisição de Produção Rural de Produtor Rural Pessoa Física/Segurado Especial\.

Tamanho: 001

Tipo: A

Validação deste campo: O conteúdo da Abrangência da Decisão do Processo deve ser igual a <1> ou <2> ou não ser informado\. Caso seja diferente de um destes valores, retornar a mensagem: “Abrangência da Decisão do Processo Inválida\. Conteúdo do campo deve ser igual a <1>, <2> ou não preenchido”\.

__OS4514__

__RN276__

__Campo 276\-Tipo de Aquisição/Comercialização da Produção__

Obrigatoriedade: Não Obrigatório

Item: A ser reservado pelo A&D

Descrição: Tipo de Aquisição/Comercialização da Produção

Nome do Campo: A ser reservado pelo A&D

Comentário: Tipo de aquisição ou comercialização, conforme lista a seguir:

1 \- Aquisição da Produção de Prod\. Rural PF ou segurado especial/Comercialização da Produção por Prod\. Rural PJ/Agroindústria;

2 \- Aquisição da produção de produtor rural pessoa física ou segurado especial em geral por Entidade do PAA;

3 \- Aquisição da produção de produtor rural pessoa jurídica por Entidade do PAA;

4 \- Aquisição da produção de produtor rural pessoa física ou segurado especial em geral \- Produção Isenta \(Lei 13\.606/2018\)

5 \- Aquisição da produção de produtor rural pessoa física ou segurado especial em geral por Entidade do PAA \- Produção Isenta \(Lei 13\.606/2018\)

6 \- Aquisição da produção de produtor rural pessoa jurídica por Entidade do PAA \- Produção Isenta \(Lei 13\.606/2018\)

7 \- Comercialização da Produção com Isenção de Contribuição Previdenciária \(Lei 13\.606/2018\)

8 \- Comercialização da Produção para Entidade inscrita no PAA;

9 \- Comercialização da Produção no Mercado Externo;

0 \- Aquisição de produção de produtor rural pessoa física ou segurado especial para fins de exportação\.

Tamanho: 001

Tipo: A

Validação deste campo: O conteúdo do Tipo de Aquisição/Comercialização da Produção deve ser igual a <1>, <2>, <3>, <4>, <5>, <6>, <7>, <8>, <9>, <0> ou não ser informado\. Caso seja diferente de um destes valores, retornar a mensagem: “Tipo de Aquisição/Comercialização da Produção Inválido\. Conteúdo do campo deve ser igual a <1>, <2>, <3>, <4>, <5>, <6>, <7>, <8>, <9>, <0> ou não preenchido”\.

__OS4514__

__MFS20029__

__MFS20913__

__MFS\-58346__

__RN277__

__Campo – Valor da GILRAT Não Retida__

__\[ALTERADA \- CH17739\_2017 \(MFS\-13849\)\]__

Alterar a rotina de Importação para que seja considerada a inclusão do campo:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Valor da GILRAT Não Retida

N

017V002

NÃO

NÃO

__MFS\-2967__

__CH17739\_2017 \(MFS\-13849\)__

__RN278__

__Campo – Valor do SENAR Não Retido__

__\[ALTERADA \- CH17739\_2017 \(MFS\-13849\)\]__

Alterar a rotina de Importação para que seja considerada a inclusão do campo:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Valor do SENAR Não Retido

N

017V002

NÃO

NÃO

__MFS\-2967__

__CH17739\_2017 \(MFS\-13849\)__

__RN279__

__Campo 279\-CNPJ Subempreiteiro__

Obrigatoriedade: Não Obrigatório

Item: A ser reservado pelo A&D

Descrição: CNPJ Subempreiteiro

Comentário: CNPJ Subempreiteiro para situações de obra com subempreitada\.

Tamanho: 014

Tipo: A

Deverá ser realizada a validação do conteúdo informado\. Caso seja informado um CNPJ inválido, retornar a mensagem: “Numero de CNPJ informado nao e valido, conforme regras da Secretaria de Fazenda”\.

__OS4514\-D__

__RN280__

__Campo 280\-CNPJ/CPF do Proprietário do CNO__

Obrigatoriedade: Não Obrigatório

Item: A ser reservado pelo A&D

Descrição: CNPJ/CPF do Proprietário do CNO

Comentário: CNPJ/CPF do Proprietário do CNO para serviços tomados e prestados de obra de construção civil\.

Tamanho: 014

Tipo: A

Deverá ser realizada a validação do conteúdo informado\. Caso seja informado um CNPJ inválido, retornar a mensagem: “Numero de CNPJ informado nao e valido, conforme regras da Secretaria de Fazenda”\.

__OS4514\-D__

__RN281__

__Campo 281\-Valor Retido do subempreitado__

Obrigatoriedade: Não Obrigatório

Item: A ser reservado pelo A&D

Descrição: Valor Retido do subempreitado

Comentário: Valor da Contribuição Previdenciária Retida da Subempreitada\.

Tamanho: 015V002

Tipo: N

__OS4514\-D__

__RN282__

__Campo 282\-Número Documento Fiscal de serviço \(60 posições\)__

__Tabela: __SAFX07 

__Item:__ A ser definido pelo A&D

__Nome do Campo:__ Será definido pelo A&D__ __

__Descrição: __Número Documento Fiscal de serviço \(60 posições\) __  __

__Tipo: __A

__Tamanho: __060

__Chave: __Não

__Campo não obrigatório __

Este campo foi criado para receber os números de documento fiscal de serviço que contenham mais de 12 posições\.

__Regras de preenchimento__

__Tela\-A__ 🡸__  Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__  

O campo número Doc\. Fiscal \(60 Posições\) só será preenchido quando os seguintes campos forem verdadeiros: 

SE

     Campo COD\_ESTAB selecionado na importação for = o campo __COD\_ESTAB__ da __Tela\-A__

      E

     Campo COD\_CLASS\_DOC\_FIS = “2” ou = “3”

      E

    Campo DATA\_FISCAL __>= Data Inicio__ da __Tela\-A__

Se não, 

__Mensagem:__ Importação não realizada\.

O campo __<<nome do campo criado pelo A&D>> __não esta preenchido\.

__Solução:__ Preencher o campo ou desabilitar o parâmetro no Modulo:__ __Básicos >> Parâmetros__ __Menu: Preliminares >> Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)\.

Ou

__Mensagem:__ Não existe parâmetro para o campo __<<nome do campo criado pelo A&D>>__   

__Solução:__ Apagar a informação do campo ou habilitar o parâmetro no Modulo:__ __Básicos >> Parâmetros__ __Menu: Preliminares >> Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)\.

__OS3341__

__RN283__

__Campo “283\-Valor FCP UF Destino”__

__Tipo:__ N

__Tamanho: __015V002

__Obrigatório: __Não__ __

__MFS2101__

__RN284__

__Campo “284\-Valor ICMS UF Destino”__

__Tipo:__ N

__Tamanho: __015V002

__Obrigatório: __Não__ __

__MFS2101__

__RN285__

__Campo “285\-Valor ICMS UF Origem”__

__Tipo:__ N

__Tamanho: __015V002

__Obrigatório: __Não__ __

__MFS2101__

__RN286__

__Campo 286\-Valor da Contribuição Previdenciária__

Alterar a rotina de Importação para que seja considerada a inclusão do campo:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Valor da Contribuição Previdenciária

N

017V002

NÃO

NÃO

__MFS\-2967__

__RN287__

__Campo Valor do Desconto da Contribuição Destinada ao GILRAT__

Obrigatoriedade: Não Obrigatório

Item: A ser reservado pelo A&D

Descrição: Valor do Desconto da Contribuição Destinada ao GILRAT

Nome do Campo: A ser reservado pelo A&D

Comentário: Valor da Contribuição Destinada ao Financiamento dos Benefícios Concedidos em Razão do Grau de Incidência da Incapacidade Laborativa Decorrente dos Riscos Ambientais do Trabalho, Incidente sobre a Aquisição de Produção Rural de Produtor Rural Pessoa Física\.

Tamanho: 015V002

Tipo: N

__OS4514__

__RN288__

__Campo Valor do Desconto da Contribuição Destinada ao SENAR__

Obrigatoriedade: Não Obrigatório

Item: A ser reservado pelo A&D

Descrição: Valor do Desconto da Contribuição Destinada ao SENAR

Nome do Campo: A ser reservado pelo A&D

Comentário: Valor da Contribuição Destinada ao SENAR, Incidente sobre a Aquisição de Produção Rural de Produtor Rural Pessoa Física/Segurado Especial\.

Tamanho: 015V002

Tipo: N

__OS4514__

__RN289__

__Campo CPF/CNPJ do Consumidor/ Produtor__

__\[ALTERADA \- CH13577\_2017 \(MFS12877\)\]__

Obrigatoriedade: Não Obrigatório

Item: A ser reservado pelo A&D

Descrição: CPF/CNPJ do Consumidor/ Produtor

Comentário: CPF/CNPJ do Consumidor para NF de modelo 65 \(NFC\-e\) ou CPF/CNPJ do Produtor Rural para atendimento do Evento S\-1250 do e\-Social\.

Tamanho: 014

Tipo: A

__MFS11800__

__CH13577\_2017 \(MFS12877\)__

__RN290__

__Campo 290\-Nº Certificado Qualidade__

Obrigatoriedade: Não Obrigatório

Item: A ser reservado pelo A&D

Descrição: Nº Certificado Qualidade

Comentário: Número do certificado de qualidade do produto em atendimento a obrigação acessória i\-SIMP\.

É obrigatória a declaração do número do certificado de qualidade, no caso de Produtores, nas operações comerciais de venda\. Deverão ser declarados por intermédio do preenchimento do campo 25 \(Valor encontrado da característica\)\. Apenas os caracteres numéricos dos certificados deverão ser declarados no campo 25, descartando\-se os caracteres alfanuméricos conforme item 3\.6 do Regulamento Técnico ANP nº 1/2004, anexo à Resolução ANP 17/2004\.

*Exemplo de Preenchimento do Campo 25:*

Nº certificado \- AB123F987

DPMP – 0000123987

Tamanho: 010

Tipo: A

__Tratamento:__

Esse campo será alfanumérico, mas deverá aceitar apenas número\.

Isso por que o certificado em forma física aceita qualquer tipo, mas a obrigação exige apenas a numeração\.

Se na carga para importação tiver texto o sistema não deverá aceitar e deve emitir erro com a mensagem: “Campo Nº Certificado Qualidade precisa ser numérico”\.

__MFS13120__

__RN291__

__RN292__

__Campo 292\-Valor Total Adicional__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o novo campo nas tabelas SAFX07\.

__Tipo: __N

__Tamanho: __015V002

__Obrigatório: __Não

__MFS17919__

__RN293__

__Campo 293\-Valor da Retenção Previdenciária relativo a Serviços Subempreitados__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o novo campo nas tabelas SAFX07\.

__Tipo: __N

__Tamanho: __015V002

__Obrigatório: __Não

__MFS17919__

__RN294__

__Campo 294\-Valor do Serviço Prestado em Condições Especiais para 15 anos:__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o novo campo nas tabelas SAFX07\. 

__Tipo: __N

__Tamanho: __015V002

__Obrigatório: __Não

__MFS17919__

__RN295__

__Campo 295\-Valor do Serviço Prestado em Condições Especiais para 20 anos:__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o novo campo nas tabelas SAFX07\. 

__Tipo: __N

__Tamanho: __015V002

__Obrigatório: __Não

__MFS17919__

__RN296__

__Campo 296\-Valor do Serviço Prestado em Condições Especiais para 25 anos:__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o novo campo nas tabelas SAFX07\. 

__Tipo: __N

__Tamanho: __015V002

__Obrigatório: __Não

__MFS17919__

__RN297__

__Campo – Valor Total do IPI Devolvido:__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o novo campo na tabela SAFX07\. 

__Item:__ A ser reservado pelo Desenvolvimento

__Nome do Campo:__ Será definido pelo Desenvolvimento

__Tipo: __N

__Tamanho: __015V002

__Obrigatório: __Não

__Chave:__ Não

__Comentário: __Este campo tem como finalidade apresentar a soma dos valores totais dos itens da nota fiscal de mercadoria que possuírem IPI Devolvido destacado\. 

__MFS\-20985__

__RN298__

__Campo 298\-Valor SEST:__

\(Campo criado na MFS22545\)

Campo numérico, *não* obrigatório \(vide especificação no Manual de Layout\)\.

__MFS22545__

__RN299__

__Campo 299\-Valor SENAT:__

\(Campo criado na MFS22545\)

Campo numérico, *não* obrigatório \(vide especificação no Manual de Layout\)\.

__MFS22545__

__RN300__

Campo __Finalidade Emissão da NFe__:                        

Campo *não* obrigatório\.

Poderá ser preenchido apenas quando o Modelo do Documento = 66 \(NF3e\) ou 62 \(NFCom\)\. Se for preenchido para qualquer outro modelo de documento, o registro não será importado e será gravada uma mensagem de erro no log\. \(“<a id="_Hlk118835205"></a>*O* *campo Finalidade Emissão NFe deve ser informado apenas quando se tratar de modelo de documento = 62 ou 66*”\)\.

Quando preenchido, seu conteúdo deve ser = 1 \(Normal\), 2 \(Substituição\) ou 3 \(Normal com Ajuste\)\. Caso contrário, o registro não será importado e será gravada uma mensagem de erro no log \(“*Campo Finalidade Emissão NFe inválido\. Preencher com 1, 2 ou 3*”\)\.

__\[ALTERADA – MFS90034 – Sped Fiscal 2023\]__

Inclusão do modelo 62 – “Nota Fiscal Fatura Eletrônica de Serviços de Comunicação – NFCom”\. Com isso, a regra de validação do campo “Finalidade Emissão da NFe” é alterada para permitir o preenchimento do campo, para os modelos 66 e 62\.

__MFS31259__

__RN301__

Campo __Chave de Acesso da NFe Substituída__:

__ __

Campo *não* obrigatório\.

Este campo só poderá ser informado quando o campo anterior \(campo “__Finalidade Emissão da NFe”__\) for válido e igual a “2” \(Substituição\)\. Caso contrário, o registro não será importado e será gravada uma mensagem de erro no log \(“*O* *campo Chave de Acesso da NFe Substituída deve ser informado apenas quando a Finalidade da Emissão da NFe for = 2\-Substituição*\)\.

__MFS31259__

__RN302__

Campo __Indicador de preenchimento dos Valores de ICMS cobrados anteriormente por ST__:__  __

__   __

Campo *não* obrigatório\.

Quando preenchido, seu conteúdo deve ser igual a S \(Sim\) ou N \(Não\)\. Caso contrário, o registro não será importado e será gravada uma mensagem de erro no log \(“*Campo Indicador de preenchimento dos Valores de ICMS cobrados anteriormente por ST preenchida com conteúdo inválido\. Preencher com S ou N*\)\.

__MFS32070__

__RN303__

__Ca__mp__o \- Forma de Tributação do Produtor Rural__

 

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar o novo campo na tabela SAFX07\. 

__Tabela: __SAFX07

__Nome do Campo: __IND\_TRIB\_PRODUTOR\_CP

__Descrição: __Forma de Tributação do Produtor Rural

__Tipo:__ A

__Tamanho: __001

__Não Obrigatório__

__Opções Válidas: __1,2

1 \- Sobre a comercialização da sua produção;

2 \- Sobre a folha de pagamento\.

Campo de preenchimento não obrigatório, caso preenchido, se o valor informado for inválido exibir a seguinte msg ao usuário: “Forma de Tributação do Produtor Rural Inválido\. Conteúdo do campo deve ser igual a <1> ou <2>”\.

__MFS64383__

__RN304__

\[__MFS73688__\]: Sped Fiscal Atualização 2022 \- Inclusão do Campo

__Campo – Modelo do Documento Fiscal NF Substituída__

Campo *não* obrigatório

Os conteúdos válidos para este campo são “01”, “06”, “21”, “22” ou “66” ou “62” e devem estar cadastrados na SAFX2024\. Se for diferente deste conteúdo, gerar a mensagem de erro no log: “<a id="_Hlk118835150"></a>*Código do Modelo de Documento Fiscal NF Substituída invalido\. Os codigos validos são: 01, 06, 21, 22, 62 ou 66*”\. Código erro: <a id="_Hlk118835138"></a>913177

__\[ALTERADA – MFS90034 – Sped Fiscal 2023\]__

Inclusão do modelo 62 – “Nota Fiscal Fatura Eletrônica de Serviços de Comunicação – NFCom”\.

MFS73688

__RN305__

\[__MFS73688__\]: Sped Fiscal Atualização 2022 \- Inclusão do Campo

__Campo \- Código de Autenticação Digital \(Convênio 115/2003\) NF Substituída:__

Campo *não* obrigatório\.

Este campo só poderá ser informado quando o campo “__Finalidade Emissão da NFe”__\) for válido e = “2” \(Substituição\) e o campo “__Modelo do Documento Fiscal NF Substituída__” for = ‘06’, ‘21’ ou ‘22’\. Caso contrário, o registro não será importado e será gravada uma mensagem de erro no log \(“*O* *campo Código de Autenticação Digital \(Convênio 115/2003\) NF Substituída deve ser informado apenas quando a Finalidade da Emissão da NFe for = 2\-Substituição e Modelo Doc\. Fiscal NF Substituída for = 06, 21 ou 22”*\)\. Código erro: 913178

__\[ALTERADA – MFS90034 – Sped Fiscal 2023\]__

Regra alterada para inclusão dos modelos 21 e 22\- Serviços de Comunicação”\.

MFS73688

__RN306__

\[__MFS73688__\]: Sped Fiscal Atualização 2022 \- Inclusão do Campo

__Campo \- Energia injetada__

Campo *não* obrigatório\.

MFS73688

__RN307__

\[__MFS73688__\]: Sped Fiscal Atualização 2022 \- Inclusão do Campo

__Campo \- Outras Deduções__

Campo *não* obrigatório\.

MFS73688

__RN308__

\[__MFS90034__\]: Sped Fiscal Atualização 2023 \- Inclusão do Campo

__Campo – Tipo Faturamento \(NFe\)__

Campo *não* obrigatório\.

Poderá ser preenchido apenas quando o Modelo do Documento = 62 \(NFCom\)\. Se for preenchido para qualquer outro modelo de documento, o registro não será importado e será gravada uma mensagem de erro no log\. <a id="_Hlk118835084"></a>\(“*O* *campo Tipo Faturamento NFe deve ser informado apenas quando se tratar de modelo de documento = 62*” – código 913220\)\.

Quando preenchido, seu conteúdo deve ser = 0 \(Faturamento Normal\), 1 \(Faturamento Centralizado\) ou 2 \(Cofaturamento\)\. Caso contrário, o registro não será importado e será gravada uma mensagem de erro no log \(“<a id="_Hlk118835114"></a>*Campo Tipo Faturamento NFe inválido\. Preencher com 0 \(Normal\), 1 \(Centralizado\) ou 2 \(Cofaturamento\)*” – código 913221\)\.

MFS90034

__RN309__

__Campo 309 – Tipo do Ambiente__

__Obrigatoriedade: Não obrigatório__

__Descrição: Tipo do Ambiente__

__Nome do Campo: IND\_TP\_AMB\_NFE__

__Tamanho: 001__

__Tipo: A__

__Lista Fixa apresentanto os itens abaixo \+ Um item na lista em Branco:__

__1 \- Produção__

__2 – Homologação__

Se o campo for preenchido com algum valor diferente, será gravada mensagem de erro padrão  \(Verificar mensagem padrão\) e o registro não será importado\.

Validação do campo: o conteúdo informado deve ser igual a < Nulo >, <1> ou <2>\. Caso seja informado um código diferente, retornar a mensagem: “Indicador do Tipo do Ambiente inválido\. Informe <1> , <2> ou deixar em branco\.”

Reserva TFIX22: 913241

MFS652063

__RN310__

__Campo 310 – Código numérico que compõe a Chave de Acesso__

__Obrigatoriedade: Não obrigatório__

__Descrição: Código Chave de Acesso__

__Nome do Campo: COD\_NF\_NFE__

__Tamanho: 007__

__Tipo: A__

MFS652063

__RN311__

__Campo 311 – Indicador de serviço pré\-pago__

__Obrigatoriedade: Não obrigatório__

__Descrição: Serviço pré\-pago__

__Nome do Campo: IND\_PRE\_PAGO__

__Tamanho: 001__

__Tipo: A__

__Check\-Box com a descrição “Serviço Pré\-Pago”, marcando a opção inserir o valor “1” na base de dados atendendo à regra da NFCom \(__1 – Serviço pré\-pago \(informar a tag somente se a nota for referente a um serviço exclusivamente pré\-pago\)__ \)__

Se o campo for preenchido com algum valor diferente, será gravada mensagem de erro padrão  \(Verificar mensagem padrão\) e o registro não será importado\.

Validação do campo: o conteúdo informado deve ser igual a < Nulo > ou <1>\. Caso seja informado um código diferente, retornar a mensagem: “Indicador de Serviço Pré\-Pago inválido\. Informe <1> ou deixar em branco\.”

Reserva TFIX22: 913242

MFS652063

__RN312__

__Campo 312 – Indicador de Sessão de Meios de Rede__

__Obrigatoriedade: Não obrigatório__

__Descrição: Sessão de Meios de Rede__

__Nome do Campo: IND\_SESSAO\_REDE__

__Tamanho: 001__

__Tipo: A__

__Check\-Box com a descrição “Sessão de Meios de Rede”, marcando a opção inserir o valor “1” na base de dados atendendo à regra da NFCom \(__\(valor = 1\), essa tag dispensa geração do grupo Fatura\.  
Apenas para notas dos tipos Normal e Substituição com tipo de faturamento normal__\)__

Validação do campo: o conteúdo informado deve ser igual a < Nulo > ou <1>\. Caso seja informado um código diferente, retornar a mensagem: “Indicador de Sessão de Meios de Rede inválido\. Informe <1> ou deixar em branco\.

Reserva TFIX22: 913243

MFS652063

__RN313__

__Campo 313 – Data de início do contrato__

__Obrigatoriedade: Não obrigatório__

__Descrição: Data Início do contrato__

__Nome do Campo: DAT\_INI\_CONTRATO__

__Tamanho: 008__

__Tipo: N \(Campo de Data\)__

Validação do campo: Validar o campo tipo DATA, caso a informação do campo for inválida emitir a segunte mensagem: “Data Inicial do Contrato preenchida com informação inválida\.”

Reserva TFIX22: 93625

MFS652063

__RN314__

__Campo 314 – Data de término do contrato__

__Obrigatoriedade: Não obrigatório__

__Descrição: Data término do contrato__

__Nome do Campo: DAT\_FIM\_CONTRATO__

__Tamanho: 008__

__Tipo: N \(Campo de Data\)__

Validação do campo: Validar o campo tipo DATA, caso a informação do campo for inválida emitir a segunte mensagem: “A Data Final do Contrato deve ser uma data válida, igual ou superior a Data Inicial do Contrato\.\.”

Reserva TFIX22: 93626

MFS652063

__RN315__

__Campo 315 – Número do Terminal Principal do serviço contratado__

__Obrigatoriedade: Não obrigatório__

__Descrição: Número do Terminal__

__Nome do Campo: NUM\_TERMINAL\_TEL__

__Tamanho: 012__

__Tipo: A__

MFS652063

__RN316__

__Campo 316 – Código da UF de habilitação do terminal__

__Obrigatoriedade: Não obrigatório__

__Descrição: UF de habilitação do terminal__

__Nome do Campo: UF\_TERMINAL\_TEL__

__Tamanho: 002__

__Tipo: A__

Validação do campo: Caso o campo esteja preenchido no arquivo, validar seu conteúdo na tabela ESTADO\. Se o código não existir na tabela Campo “COD\_ESTADO”, gravar a seguinte mensagem no log de importação e não gravar o registro:  “O Codigo da Unidade da Federacao de habilitação do Terminal é invalido\.”

Reserva TFIX22: 913244

MFS652063

__RN317__

__Campo 317 – Valor Total do ICMS desonerado__

__Obrigatoriedade: Não obrigatório__

__Descrição: Valor ICMS Desonerado__

__Nome do Campo: VLR\_ICMS\_DESONERADO__

__Tamanho: __015V002

__Tipo: N__

MFS652063

__RN318__

__Campo 318 – Valor Total do FCP \(Fundo de Combate à Pobreza\)__

__Obrigatoriedade: Não obrigatório__

__Descrição: Valor FCP \(Fundo de Combate à Pobreza\)__

__Nome do Campo: VLR\_FCP__

__Tamanho: __015V002

__Tipo: N__

MFS652063

__RN319__

__Campo 319 – Valor do FUNTTEL__

__Obrigatoriedade: Não obrigatório__

__Descrição: Valor FUNTTEL__

__Nome do Campo: VLR\_FUNTTEL__

__Tamanho: __015V002

__Tipo: N__

MFS652063

__RN320__

__Campo 320 – Valor do FUST__

__Obrigatoriedade: Não obrigatório__

__Descrição: Valor FUST__

__Nome do Campo: VLR\_FUST__

__Tamanho: __015V002

__Tipo: N__

MFS652063

__RN321__

__Campo 321 – CNPJ do autorizado para download__

__Obrigatoriedade: Não obrigatório__

__Descrição: CNPJ Autorizado para download__

__Nome do Campo: CNPJ\_DOWNLOAD__

__Tamanho: __014

__Tipo: A__

MFS652063

__RN322__

__Campo 322 – CPF do autorizado para download__

__Obrigatoriedade: Não obrigatório__

__Descrição: CPF Autorizado para download__

__Nome do Campo: CPF\_DOWNLOAD__

__Tamanho: 011__

__Tipo: A__

MFS652063

__RN323__

__Campo 323 – Valor da CSLL retida__

__Obrigatoriedade: Não obrigatório__

__Descrição: Valor CSLL Retida__

__Nome do Campo: VLR\_CSLL\_RETIDO__

__Tamanho: __015V002

__Tipo: N__

MFS652063

__RN324__

__Campo 324– Valor do IRRF retido__

__Obrigatoriedade: Não obrigatório__

__Descrição: Valor IRRF Retido__

__Nome do Campo: VLR\_IRRF\_RETIDO__

__Tamanho: __015V002

__Tipo: N__

MFS652063

__RN325__

__Campo 325 – Inscrição Estadual Virtual__

__Obrigatoriedade: Não obrigatório__

__Descrição: Inscrição Estadual Virtual__

__Nome do Campo: INSC\_EST\_VIRTUAL__

__Tamanho: 014__

__Tipo: A__

MFS652063

__RN326__

__Campo 326 – Ano e mês da emissão da NF__

__Obrigatoriedade: Não obrigatório__

__Descrição: Período Apuração NF Substituída__

__Nome do Campo: PERIOD\_APUR\_SUBST__

__Tamanho: 006__

__Tipo: N \(Campo de Data\)__

Validação do campo: Validar o campo com a formatação AAAAMM, caso a informação do campo for inválida emitir a segunte mensagem: “Ano e mês da emissão da NF preenchida com informação inválida\.”

Reserva TFIX22: 93657

MFS652063

__RN327__

__Campo 327 – Motivo da Substituição__

__Obrigatoriedade: Não obrigatório__

__Descrição: Motivo da Substituição__

__Nome do Campo: COD\_MOTIVO\_SUBST__

__Tamanho: 002__

__Tipo: A__

__Lista Fixa apresentanto os itens abaixo \+ Um item na lista em Branco:__

01 – Erro de Preço  
02 – Erro Cadastral  
03 – Decisão Judicial  
04 \- Erro de Tributação  
05 \- Descontinuidade do Serviço

Se o campo for preenchido com algum valor diferente, será gravada mensagem de erro padrão  \(Verificar mensagem padrão\) e o registro não será importado\.

Validação do campo: o conteúdo informado deve ser igual a < Nulo >, <1> , <2>, <3>, <4> ou <5>\. Caso seja informado um código diferente, retornar a mensagem: “Campo 139 \- Motivo da Substituição inválido\. Informe <1> , <2>, <3>, <4>, <5> ou deixar em branco\.”

Reserva TFIX22: 913245

MFS652063

__RN328__

__Campo 328 – Chave de acesso da NFCom emitida pela Operadora Local__

__Obrigatoriedade: Não obrigatório__

__Descrição: Chave de acesso da NFCom emitida pela Operadora Local__

__Nome do Campo: COD\_AUTENTIC\_COF__

__Tamanho: 044__

__Tipo: A__

MFS652063

__RN329__

__Campo 329 – CNPJ do Emitente centralizador do Faturamento__

__Obrigatoriedade: Não obrigatório__

__Descrição: CNPJ do Emitente do Faturamento__

__Nome do Campo: CNPJ\_EMIT\_FATURAMENTO__

__Tamanho: 014__

__Tipo: A__

MFS652063

__RN330__

__Campo 330 – UF do Emitente centralizador do Faturamento__

__Obrigatoriedade: Não obrigatório__

__Descrição: UF do Emitente do Faturamento__

__Nome do Campo: UF\_EMIT\_FATURAMENTO__

__Tamanho: 002__

__Tipo: A__

Validação do campo: Caso o campo esteja preenchido no arquivo, validar seu conteúdo na tabela ESTADO\. Se o código não existir na tabela Campo “COD\_ESTADO”, gravar a seguinte mensagem no log de importação e não gravar o registro: “O Codigo da Unidade da Federacao do Emitente do Faturamento é invalido”\.

Reserva TFIX22: 913246

MFS652063

__RN331__

__Campo 331 \- CNPJ do Emitente NF Cofaturamento__

__Tipo__: A

__Tamanho__: 014

__Obrigatório__: Não 

Validação:

Quando o campo estiver preenchido, verificar se o conteúdo informado é um CNPJ válido\. 

Caso não seja válido, exibir a seguinte mensagem no log de importação e não gravar o registro: “*Numero de CNPJ informado nao e valido, conforme regras da Secretaria de Fazenda*\.” Código erro: 90082

Função SAF\_VALIDA\_CGC

Contemplar CNPJ Alfanumérico vigente a partir de 2026\.

MFS784653

__RN332__

__Campo 332 \- Modelo do Documento NF Cofaturamento__

__Tipo__: A

__Tamanho__: 002

__Obrigatório__: Não 

Validação:

Quando o campo estiver preenchido, verificar se código do modelo está cadastrados na SAFX2024\. 

Caso não esteja cadastrado, exibir a seguinte mensagem no log de importação e não gravar o registro: “*Código do Modelo de Documento NF Cofaturamento invalido\.*” Código erro: 93767

MFS784653

__RN333__

__Campo 333 \- Serie do Documento Fiscal Cofaturamento__

__Tipo__: A

__Tamanho__: 003

__Obrigatório__: Não 

MFS784653

__RN334__

__Campo 334 \- Número do Documento Fiscal Cofaturamento__

__Tipo__: A

__Tamanho__: 012

__Obrigatório__: Não 

MFS784653

__RN335__

__Campo 335 \- Ano e mês da emissão da NF Cofaturamento \(AAAAMM\)__

__Tipo__: N

__Tamanho__: 006

__Obrigatório__: Não

Validação: Quando o campo estiver preenchido, verificar se os 4 primeiros caracteres são referentes a um ano e os 2 últimos a um mês válido\.  

Caso a informação não seja um ano e mês válido, exibir a seguinte mensagem no log de importação e não gravar o registro: “*Ano e mês da emissão da NF Cofaturamento preenchida com informação inválida\.*” Código erro: 93768

MFS784653

__RN336__

__Campo 336 \- Hash do registro no arquivo do convênio 115 – NF Cofaturamento__

__Tipo__: A

__Tamanho__: 032

__Obrigatório__: Não

MFS784653


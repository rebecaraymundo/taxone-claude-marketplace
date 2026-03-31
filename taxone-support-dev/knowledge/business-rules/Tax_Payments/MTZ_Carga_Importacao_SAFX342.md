---
source: "MTZ_Carga_Importacao_SAFX342 .docx"
category: Tax Payments
converted: auto
---





THOMSON REUTERS


TAX PAYMENTS – IMPORTAÇÃO - SAFX342 (Guias de Pagamentos -Extra Apuração)
TAXONE >> Básicos > Data Warehouse > Manutenção > Guia de Pagamento


DOCUMENTO DE REQUISITO



# Introdução

A tabela SAFX342 foi desenvolvida especificamente para carregar informações relacionadas às guias de pagamento que não estão disponíveis no sistema Tax One. O principal objetivo desta tabela é facilitar a geração do JSON necessário para a integração com o sistema Tax Payments.
Adicionalmente, a funcionalidade de importação associada à SAFX342 tem o propósito de trazer dados exclusivos para o Grupo de Impostos 'Extras Apurações'. Estes dados, ausentes no Tax One, são essenciais para viabilizar a correta geração das guias de pagamento.


**Localização:**
Módulo: Básicos > Job Servidor
Menu: Carga > Programação > Execução
Importação > Programação > Execução
Importação batch > Programação > Execução

**(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX342 conforme o Manual de Layout, o que facilita a consulta. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00).**

Procedimentos para a Importação da SAFX342:

A importação da SAFX342 deve seguir as seguintes premissas de negócio e comportamentos:
No campo Grupo de Imposto, considerar sempre "Extra Apuração". Essa informação é exclusivamente para receber os impostos importados via SAFX342.
Quando o imposto "Extra Apuração" for importado, o campo Grupo de Imposto na tela Status deverá permanecer com o preenchimento fixo "Aguardando Envio". Isso serve para sinalizar ao usuário que será necessário gerar o arquivo JSON.
O Relatório de Guias deve ser atualizado automaticamente para receber as informações importadas pela SAFX342.

**Resultado da Importação:**
Caso a importação seja realizada com sucesso, os dados serão preenchidos nas seguintes telas:
**Manutenção > Guias de Pagamentos > Status das Guias**
**Manutenção > Guias de Pagamentos > Relatórios de Guias**




Regra Geral para validação

1º ) Consistências Básicas:

Campos Data inválidos
Campos Obrigatórios
Campos Numéricos inválidos
Campo Código de Arrecadação -Vide regra RN07
Campo Código de Receita – Vide regra RN08
Campo Detalhamento da Receita -Vide regra RN09
Campo Número do Documento de Origem – Vide regra RN 10
Campo Unidade Federal Favorecida – Vide regra RN 12
Campo Cadastro Participante – Vide regra RN 27
Campo Grupo de Imposto – Vide regra RN 32
Campo Usuário – Vide regra RN 33
Campo Status – Vide regra RN 34



REGRAS DE NEGÓCIO



Considerações deste modelo:

**Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**




---

| MFS | Nome | Descrição |
| --- | --- | --- |
| ADO- 768407 | Beatriz Tie Terada, Millys Lopes | Definição das regras de importação da SAFX342. |


---

| CÓD | DESCRIÇÃO | ADO |
| --- | --- | --- |
| RN00 |  | ADO- 768407 |
| RN00.1 | Campos Obrigatório não preenchido  Se algum campo de preenchimento obrigatório não estiver preenchido, exibir a mensagem “Campo <<Nome do campo>> deve ser preenchido” | ADO- 768407 |
| RN01 | Campo 01 - Código da empresa   Tabela: SAFX342 Item: 01 Nome do Campo: COD_EMPRESA Descrição: Código da empresa Tipo: A Tamanho: 008 Campo Obrigatório Chave Primária Comentário: Informar o Código da Empresa Exibir a mensagem da TFIX 22 CÓDIGO 90001 | ADO- 768407 |
| RN02 | Campo 02 - Código do estabelecimento  Tabela: SAFX342 Item: 02 Nome do Campo: COD_ESTAB Descrição: Código do estabelecimento Tipo: A Tamanho: 006  Campo Obrigatório Chave Primária Comentário: Informar o Código do Estabelecimento Exibir a mensagem da TFIX 22 CÓDIGO 90002 | ADO- 768407 |
| RN03 | Campo 03 – Código do Tipo do Livro Tabela: SAFX342 Item: 03 Nome do Campo: COD_TIPO_LIVRO Descrição: Código do Tipo do Livro Tipo: C Tamanho: 003 Campo Obrigatório Chave Primária Comentário:  Informe o código 'EXT' do livro de apuração, que corresponde ao imposto 'Extra Apuração'. Exibir a mensagem da TFIX 22 CÓDIGO 913307 | ADO- 768407 |
| RN04 | Campo 04 – Período  Tabela: SAFX342 Item: 04 Nome do Campo: PERIODO Descrição: Data da ocorrência ou do encerramento do período Tipo: N Tamanho: 008 Campo NÃO OB Chave Primária Comentário: Informar o Período Relacionado ao Imposto para Extra Apuração e a Data da Ocorrência ou do Encerramento do Período Exibir a mensagem da TFIX 22 CÓDIGO 913293 | ADO- 768407 |
| RN05 | Campo 05 – Número da Guia de Pagamento  Tabela: SAFX342 Item: 05 Nome do Campo: NUM_GUIA_PAG Descrição:  Tipo: C Tamanho: 030 Campo Obrigatório Chave Primária Comentário: Este campo de preenchimento automático do sistema Tax One gera um número sequencial para cada guia. Por favor, não preencha este campo manualmente. Exibir a mensagem da TFIX 22 CÓDIGO 913306 | ADO- 768407 |
| RN06 | Campo 06 – Data da Guia de Pagamento Tabela: SAFX342 Item: 06 Nome do Campo: DAT_GUIA_PAG Descrição: Data de Pagamento da Guia Tipo: N Tamanho: 08 Campo Obrigatório Chave Primária Comentário: Informa a data do pagamento da guia. Exibir a mensagem da TFIX 22 CÓDIGO 913295 | ADO- 768407 |
| RN07 | Campo 07 – Código de Arrecadação  Tabela: SAFX342 Item: 07 Nome do Campo: COD_ARRECADACAO Descrição: Tipo de documento utilizado na arrecadação, conforme cadastro no Dootax. (ex.: DARF; GNRE) Tipo: C Tamanho: 020 Campo Obrigatório Chave Primária Comentário: Informar o Código de Arrecadação conforme tabela TACES 119 (Tabela de Código Tax Payments)  Exibir a mensagem da TFIX 22 CÓDIGO 913297 | ADO- 768407 |
| RN08 | Campo 08 – Código de Receita  Tabela: SAFX342 Item: 08 Nome do Campo: COD_RECEITA Descrição: Código da receita que está sendo paga, de acordo com o tipo de documento de arrecadação. Tipo: N Tamanho: 020 Campo SIM Chave Primária Comentário: Este campo informa o Código de Receita conforme tabela TACES 119 (Tabela de Código Tax Payments (DOOTAX) Exibir a mensagem da TFIX 22 CÓDIGO 913298 | ADO- 768407 |
| RN09 | Campo 09 – Detalhamento da Receita  Tabela: SAFX342 Item: 09 Nome do Campo: DET_RECEITA Descrição: Código do detalhamento da receita. Tipo: N Tamanho: 020 Campo NÃO OBRIGATÓRIO Chave Primária Comentário: Este campo informa o detalhamento da receita, conforme a tabela TACES 119 (Tabela de Código Tax Payments).  Exibir a mensagem da TFIX 22 CÓDIGO 913299 | ADO- 768407 |
| RN10 | Campo 10 – Número do Documento de Origem   Tabela: SAFX342 Item: 10 Nome do Campo: NUM_DOC_ORIGEM Descrição: Número do documento que deu origem ao pagamento. Tipo: N Tamanho: 019 Campo SIM Chave Primária Comentário:  Preencher a Chave do ID   O ID será composto pelos seguintes elementos, com tamanhos ajustados: Cod_Empresa: 3 caracteres (Ex.: "001"). Cod_Estabelecimento: 6 caracteres (Ex.: "000001"). Cod_Receita: 6 caracteres (Ex.: "131701"). Hora de Geração: 4 caracteres (Ex.: "1536"). Formato Final [Cod_Empresa][Cod_Estabelecimento][Cod_Receita][Hora] Exemplo Final: 0010000011317011536  Exibir a mensagem da TFIX 22 CÓDIGO 913300 | ADO- 768407 |
| RN11 | Campo 11 – Série  Tabela: SAFX342 Item: 11 Nome do Campo: SERIE Descrição: Série do documento Tipo: C Tamanho: 003 Campo Obrigatório Chave Primária Comentário: Informe o código '01' para série, que corresponde ao imposto 'Extra Apuração'. Exibir a mensagem da TFIX 22 CÓDIGO 913308 | ADO- 768407 |
| RN12 | Campo 12 – Unidade Federal Favorecida Tabela: SAFX342 Item: 12 Nome do Campo: UF_FAVORECIDA Descrição: Sigla da UF favorecida. Tipo: C Tamanho: 002 Campo Não Obrigatório Chave Primária Comentário: Este campo deve informar a Unidade Federal Favorecida conforme especificado na tabela TACES 119 (Tabela de Código Tax Payments). O preenchimento é obrigatório e deve estar em conformidade com o COD_RECEITA preenchido anteriormente.  Exibir a mensagem da TFIX 22 CÓDIGO 913301 | ADO- 768407 |
| RN13 | Campo 13 – CNPJ Favorecido  Tabela: SAFX342 Item: 13 Nome do Campo: CNPJ_FAVORECIDO Descrição: CNPJ do favorecido. Esse campo é usado para identificar o favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros. Tipo: C Tamanho: 014 Campo Não Obrigatório Chave Primária Comentário: Informar o CNPJ do favorecido. Esse campo é usado para identificar o favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros. | ADO- 768407 |
| RN14 | Campo 14 – Inscrição Estadual Favorecida  Tabela: SAFX342 Item: 14 Nome do Campo: IE_FAVORECIDA Descrição: Inscrição Estadual do favorecido.  Esse campo é usado para identificar o favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros.  Tipo: C Tamanho: 030 Campo Não Obrigatório Comentário: Informar a sigla da Inscrição Estadual Favorecida | ADO- 768407 |
| RN15 | Campo 15 – Valor Principal Tabela: SAFX342 Item: 15 Nome do Campo: VLR_PRINCIPAL Descrição: Valor principal do título. Tipo: N Tamanho: 015V002 Campo Obrigatório Comentário: Informar o Valor da Guia para Recolhimento do Imposto "Extra Apuração" Exibir a mensagem da TFIX 22 CÓDIGO 913296 | ADO- 768407 |
| RN16 | Campo 16 – Data do Vencimento  Tabela: SAFX342 Item: 16 Nome do Campo: DATA_VENCIMENTO Descrição: Informar a data de vencimento da Guia. Tipo: N Tamanho: 008 Campo Não Obrigatório Comentário: Informar a Data do Vencimento. Exibir a mensagem da TFIX 22 CÓDIGO 913294 | ADO- 768407 |
| RN17 | Campo 17 – Data do Pagamento  Tabela: SAFX342 Item: 17 Nome do Campo: DATA_PAGAMENTO Descrição: Data do Pagamento. Esse campo será calculado automaticamente pelo sistema Tax Payments. Tipo: N Tamanho: 008 Campo Não Obrigatório Comentário: Informar a Data do Pagamento. Exibir a mensagem da TFIX 22 CÓDIGO 913295 | ADO- 768407 |
| RN18 | Campo 18 – Valor da Multa   Tabela: SAFX342 Item: 18 Nome do Campo: VLR_MULTA Descrição: Valor da multa quando o pagamento ocorrer em atraso. Esse campo será calculado automaticamente pelo sistema, caso não seja informado na integração. Tipo: N Tamanho: 015V002 Campo Não Obrigatório Comentário: Informar o valor da multa quando o pagamento ocorrer em atraso. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração Tax Payments | ADO- 768407 |
| RN19 | Campo 19 – Valor dos Juros  Tabela: SAFX342 Item: 19 Nome do Campo: VLR_JUROS Descrição: Valor dos juros quando o pagamento ocorrer em atraso. Esse campo será calculado automaticamente pelo sistema, caso não seja informado na integração. Tipo: N Tamanho: 015V002 Campo NÃO Obrigatório Comentário: Valor dos juros quando o pagamento ocorrer em atraso. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração no Tax Payments | ADO- 768407 |
| RN20 | Campo 20 – Informação Complementar  Tabela: SAFX342 Item: 20 Nome do Campo: INFO_COMPLEMENTAR Descrição: Informação complementar a ser incluída na emissão do título a pagar. Tipo: C Tamanho: 300 Campo Não Obrigatório  Comentário: Informação complementar a ser incluída na emissão da guia de pagamento. | ADO- 768407 |
| RN21 | Campo 21 – Valor do Fundo Estadual de Combate à Pobreza  Tabela: SAFX342 Item: 21 Nome do Campo: VLR_FECP Descrição: Valor do recolhimento ao Fundo Estadual de Combate à Pobreza. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr_principal com o valor da guia excluído o valor do recolhimento ao FECP. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr_principal. Tipo: N Tamanho: 015V002 Campo Não Obrigatório Comentário: Informar o valor do recolhimento ao Fundo Estadual de Combate à Pobreza. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr_principal com o valor da guia excluído o valor do recolhimento ao FECP. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr_principal. | ADO- 768407 |
| RN22 | Campo 22 – Valor do Fundo Estadual de Combate à Pobreza – Multa  Tabela: SAFX342 Item: 22 Nome do Campo: VLR_FECP_MULTA Descrição: Valor da multa sobre o recolhimento ao Fundo Estadual de Combate à Pobreza, quando o pagamento ocorrer em atraso. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr_multa com o valor da multa excluído o valor da multa referente ao FECP. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr_multa. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração.  Tipo: N Tamanho: 015V002 Campo Não Obrigatório Comentário: Informar o valor da multa quando o pagamento ocorrer em atraso. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração no Tax Payments | ADO- 768407 |
| RN23 | Campo 23 – Valor do Fundo Estadual de Combate à Pobreza – Juros  Tabela: SAFX342 Item: 23 Nome do Campo: VLR_FECP_JUROS Descrição: Valor dos juros sobre o recolhimento ao Fundo Estadual de Combate à Pobreza, quando o pagamento ocorrer em atraso. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr_juros com o valor dos juros excluído o valor dos juros referente ao FECP. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr_juros. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração. Tipo: N Tamanho: 015V002 Campo Não Obrigatório Comentário: Informar o valor dos juros quando o pagamento ocorrer em atraso. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração. | ADO- 768407 |
| RN24 | Campo 24 – Convênio Tabela: SAFX342 Item: 24 Nome do Campo: CONVENIO Descrição: Convênio ou protocolo ICMS que regulamenta a forma de recolhimento do tributo. Esse campo é utilizado na geração da GNRE por apuração. Tipo: C Tamanho: 030 Campo Não Obrigatório Chave Primária Comentário: Informar o Convênio ou protocolo ICMS que regulamenta a forma de recolhimento do tributo. Esse campo é utilizado na geração da GNRE por apuração. | ADO- 768407 |
| RN25 | Campo 25 – Código do Produto Tabela: : SAFX342 Item: 25 Nome do Campo: COD_PRODUTO Descrição: Na emissão da GNRE, algumas UFs exigem o preenchimento do código do produto no recolhimento do ICMS por apuração. Consulte a UF para obter a lista de códigos de produtos válidos. Tipo: N Tamanho: 005 Campo Não Obrigatório Chave Primária Comentário: Na emissão da GNRE, algumas UFs exigem o preenchimento do código do produto no recolhimento do ICMS por apuração. | ADO- 768407 |
| RN26 | Campo 26 – Chave de Documentos Fiscal Eletrônico   Tabela: SAFX342 Item: 26 Nome do Campo: CHAVE_DFE Descrição: Chave de acesso do documento fiscal: Para documentos fiscais eletrônicos, informar a chave com 44 dígitos. Tipo: N Tamanho: 044 Campo Não Obrigatório Comentário: Chave de acesso do documento fiscal: Para documentos fiscais eletrônicos, informar a chave com 44 dígitos. | ADO- 768407 |
| RN27 | Campo 27 – Cadastro Participante  Tabela: SAFX342 Item: 27 Nome do Campo: CAD_PART Descrição: Informações do participante (destinatário, emitente, transportador etc.). Esse campo deve ser informado quando os dados do participante são exigidos na emissão ou visualização da guia. Ver layout do campo na aba "Cadastros", tabela "cad_part". Tipo: O Tamanho: - Campo Não Obrigatório Comentário: O campo CAD_PART não é obrigatório. No entanto, se optar por preenchê-lo, torna-se necessário informar também os seguintes campos complementares: cod_participante ,data_valid, razao_social, nome_fantasia e UF.  Exibir a mensagem da TFIX 22 CÓDIGO 913302 | ADO- 768407 |
| RN27.1 | Campo 27.1 – Código do Participante  Tabela: SAFX342 Item: 27.1 Nome do Campo: COD_PARTICIPANTE Descrição: Código de identificação do participante no sistema Tipo: C Tamanho: 60 Campo Obrigatório Comentário: Informar o Código de identificação do participante. Caso de preenchimento deste campo os demais campos Exibir a mensagem da TFIX 22 CÓDIGO 913302 | ADO- 768407 |
| RN27.2 | Campo 27.2 – Data de Validação  Tabela: SAFX342 Item: 27.2 Nome do Campo: DATA_VALID Descrição: Data de inclusão ou alteração do cadastro do participante Tipo: N Tamanho: 8 Campo Obrigatório Chave Primária Comentário: Informar a Data de Inclusão ou Alteração do Cadastro do Participante Relacionado ao Campo "Cad_part" Exibir a mensagem da TFIX 22 CÓDIGO 913302 | ADO- 768407 |
| RN27.3 | Campo 27.3 – CNPJ  Tabela: SAFX342 Item: 27.3 Nome do Campo: CNPJ Descrição: CNPJ do participante, se Pessoa Jurídica Tipo: N Tamanho: 14 Campo Não Obrigatório Chave Primária Comentário: Informar o CNPJ do participante, se Pessoa Jurídica Relacionado ao Campo "Cad_part" | ADO- 768407 |
| RN27.4 | Campo 27.4 – CPF  Tabela: SAFX342 Item: 27.4 Nome do Campo: CPF Descrição: CPF do participante, se Pessoa Física Tipo: N Tamanho: 11 Campo Não Obrigatório Chave Primária Comentário: Informar o CPF do participante, se Pessoa Física Relacionado ao Campo "Cad_part" | ADO- 768407 |
| RN27.5 | Campo 27.5 – ID Estrangeiro  Tabela: SAFX342 Item: 27.5 Nome do Campo: ID_ESTRANGEIRO Descrição: ID do participante, se estrangeiro Tipo: C Tamanho: 20 Campo Não Obrigatório Chave Primária Comentário: Informar o ID do participante, se estrangeiro Relacionado ao Campo "Cad_part" | ADO- 768407 |
| RN27.6 | Campo 27.6 – Razão Social  Tabela: SAFX342 Item: 27.6 Nome do Campo: RAZAO_SOCIAL Descrição: Nome pessoal ou razão social do participante Tipo: C Tamanho: 255 Campo Obrigatório Comentário: Informar o nome pessoal ou razão social do participante Relacionado ao Campo "Cad_part" Exibir a mensagem da TFIX 22 CÓDIGO 913302 | ADO- 768407 |
| RN27.7 | Campo 27.7 – Nome Fantasia  Tabela: SAFX342 Item: 27.7 Nome do Campo: NOME_FANTASIA Descrição:  Nome fantasia, se Pessoa Jurídica Tipo: C Tamanho: 255 Campo Obrigatório Comentário: Informar o nome fantasia, se Pessoa Jurídica Relacionado ao Campo "Cad_part" Exibir a mensagem da TFIX 22 CÓDIGO 913302 | ADO- 768407 |
| RN27.8 | Campo 27.8 – Endereço  Tabela: SAFX342 Item: 27.8 Nome do Campo: ENDERECO Descrição:  Endereço, sem o número Tipo: C Tamanho: 60 Campo Não Obrigatório Comentário: Informar o endereço, sem o número Relacionado ao Campo "Cad_part" | ADO- 768407 |
| RN27.9 | Campo 27.9 – Número  Tabela: SAFX342 Item: 27.9 Nome do Campo: NUMERO Descrição: Número do endereço Tipo: C Tamanho: 10 Campo Não Obrigatório Comentário: Informar o número do endereço Relacionado ao Campo "Cad_part" | ADO- 768407 |
| RN27.10 | Campo 27.10 – Complemento  Tabela: cad_part Item: 27.10 Nome do Campo: COMPLEMENTO Descrição: Complemento do endereço Tipo: C Tamanho: 60 Campo Não Obrigatório Comentário: Informar o Complemento do endereço Relacionado ao Campo "Cad_part" | ADO- 768407 |
| RN27.11 | Campo 27.11 – Bairro  Tabela: SAFX342 Item: 27.11 Nome do Campo: BAIRRO Descrição: Bairro em que o imóvel está situado Tipo: C Tamanho: 60 Campo Não Obrigatório Comentário: Informar o bairro em que o imóvel está situado Relacionado ao Campo "Cad_part" | ADO- 768407 |
| RN27.12 | Campo 27.12 – CEP  Tabela: SAFX342 Item: 27.12 Nome do Campo: CEP Descrição: CEP do imóvel Tipo: N Tamanho: 8 Campo Não Obrigatório Comentário: Informar o CEP relacionado ao "Cad_part" | ADO- 768407 |
| RN27.13 | Campo 27.13 – Código do Município  Tabela: SAFX342 Item: 27.13 Nome do Campo: COD_MUNICIPIO Descrição: Código do município, conforme tabela do IBGE Tipo: N Tamanho: 7 Campo Não Obrigatório Comentário: Informar Código do município, conforme tabela do IBGE e Relacionado ao Campo "Cad_part" | ADO- 768407 |
| RN27.14 | Campo 27.14 – Unidade Federal  Tabela: SAFX342 Item: 27.14 Nome do Campo: UF Descrição: UF do participante  Tipo: C Tamanho: 2 Campo Obrigatório Comentário: Informar UF do participante | ADO- 768407 |
| RN27.15 | Campo 27.15 – Código do País  Tabela: SAFX342 Item: 27.15 Nome do Campo: COD_PAIS Descrição: Código do país, conforme tabela publicada pela RFB Tipo: N Tamanho: 5 Campo Não Obrigatório Comentário: Informar Código do país e Relacionado ao Campo "Cad_part" | ADO- 768407 |
| RN27.16 | Campo 27.16 – DDD  Tabela: SAFX342 Item: 27.16 Nome do Campo: DDD Descrição: DDD telefônico Tipo: N Tamanho: 2 Campo Não Obrigatório Comentário: Informar o DDD telefônico e Relacionado ao Campo "Cad_part" | ADO- 768407 |
| RN27.17 | Campo 27.17 – Telefone Tabela: SAFX342 Item: 27.17 Nome do Campo: TELEFONE Descrição: Número do telefone Tipo: N Tamanho: 2 Campo Não Obrigatório Comentário: Informar o telefone e Relacionado ao Campo "Cad_part" |  |
| RN27.18 | Campo 27.18 – E-mail Tabela: SAFX342 Item: 27.18 Nome do Campo: EMAIL Descrição: Endereço de e-mail  Tipo: C Tamanho: 60 Campo Não Obrigatório Comentário: Informar o endereço do e-mail e Relacionado ao Campo "Cad_part" |  |
| RN27.19 | Campo 27.19 – Inscrição Estadual Tabela: SAFX342 Item: 27.19 Nome do Campo: INSC_ESTADUAL Descrição: Inscrição estadual do participante, se contribuinte do ICMS  Tipo: C Tamanho: 14 Campo Não Obrigatório Comentário: Informar a Inscrição estadual do participante, se contribuinte do ICMS  e Relacionado ao Campo "Cad_part" |  |
| RN27.20 | Campo 27.20 – Inscrição Municipal Tabela: SAFX342 Item: 27.20 Nome do Campo: INSC_MUNICIPAL Descrição: Inscrição municipal do participante, se contribuinte do ICMS Tipo: C Tamanho: 15 Campo Não Obrigatório Comentário: Informar a Inscrição municipal do participante, se contribuinte do ICMS  e Relacionado ao Campo "Cad_part" |  |
| RN27.21 | Campo 27.21 – SUFRAMA Tabela: SAFX342 Item: 27.21 Nome do Campo: SUFRAMA Descrição: Inscrição na SUFRAMA Tipo: C Tamanho: 9 Campo Não Obrigatório Comentário: Informar a Inscrição suframa do participante. | ADO- 768407 |
| RN28 | Campo 28 – Código do Município Favorecido Tabela: SAFX342 Item: 28 Nome do Campo: COD_MUN_FAVORECIDO Descrição: Código do município - Este campo deve ser informado quando a guia a ser emitida utilize o código de município diferente do que está no cadastro da empresa Tipo: N Tamanho: 007 Campo Não Obrigatório Chave Primária Comentário: Informar o Código do município - Este campo deve ser informado quando a guia a ser emitida utilize o código de município diferente do que está no cadastro da empresa | ADO- 768407 |
| RN29 | Campo 29 – Valor Outros  Tabela: SAFX342 Item: 29 Nome do Campo: VLR_OUTROS Descrição: Valor de outras despesas que devam ser utilizadas na geração da guia Tipo: N Tamanho: 015V002 Campo Não Obrigatório Comentário: Informar o valor de outras despesas que devam ser utilizadas na geração da guia "Extra Apuração" | MFS- 768407 |
| RN30 | Campo 30 – Valor da base de Cálculo  Tabela: SAFX342 Item: 30 Nome do Campo: VLR_VASE_CALC Descrição: Valor de base de cálculo. Utilizado nas guias que utilizam deste valor para calcular o valor da guia Tipo: N Tamanho: 015V002 Campo Não Obrigatório Comentário: Informar o valor de base de cálculo. Utilizado nas guias que utilizam deste valor para calcular o valor da guia "Extra Apuração" | MFS- 768407 |
| RN31 | Campo 31 – Campos Extras  Tabela: SAFX342 Item: 31 Nome do Campo: CAMPOS_EXTRAS Descrição: Utilizado para enviar um JSON com campos adicionais Tipo: C Tamanho: - Campo Não Obrigatório Comentário: Utilizado para enviar um JSON com campos adicionais | MFS- 768407 |
| RN32 | Campo 32 – Grupo do Imposto  Tabela: SAFX342 Item: 32 Nome do Campo: GRUPO_IMPOSTO Descrição: Informar o grupo de imposto selecionado para a geração da guia de acordo com os impostos  Tipo: C Tamanho: 30 Campo Obrigatório O preenchimento esperado para este campo é "Extra Apuração".  Exibir a mensagem da TFIX 22 CÓDIGO 913303 | MFS- 768407 |
| RN33 | Campo 33 – Usuário Tabela: SAFX342 Item: 33 Nome do Campo: USUARIO Descrição: Informa o usuário Tipo: C Tamanho: 100 Campo Obrigatório Comentário:  Este campo é obrigatório e deve ser preenchido com o nome ou identificação válida do usuário existente no Tax One. Exibir a mensagem da TFIX 22 CÓDIGO 913304 | MFS- 768407 |
| RN34 | Campo 34 – Status Tabela: SAFX342 Item: 34 Nome do Campo: STATUS Descrição: Informa o status de guias  Tipo: N Tamanho: 003 Campo Obrigatório Comentário:  Este campo deve ser preenchido exclusivamente com o valor 'Aguardando Envio'. Exibir a mensagem da TFIX 22 CÓDIGO 913305 | MFS- 768407 |


---

| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |


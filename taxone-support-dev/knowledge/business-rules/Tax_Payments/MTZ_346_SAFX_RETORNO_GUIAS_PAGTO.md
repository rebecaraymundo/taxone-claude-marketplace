---
source: "MTZ_346_SAFX_RETORNO_GUIAS_PAGTO.docx"
category: Tax Payments
converted: auto
---





THOMSON REUTERS


TAX PAYMENTS –  IMPORTAÇÃO - SAFX346 (Retorno das Guias de Pagamentos)
TAXONE >> Básicos > Data Warehouse > Manutenção > Guia de Pagamento


DOCUMENTO DE REQUISITO



**Introdução**

A nova SAFX de Retorno será responsável por receber os dados fornecidos pelo sistema OBI (Tax Payments DOOTAX), que disponibilizará informações sobre o status das guias e outras informações, como pagamentos realizados, pendentes ou cancelados, por exemplo.
O sistema OBI irá consumir esses dados, realizar o processamento necessário e enviar as informações, através da nova SAFX de Retorno, o Tax One, onde serão utilizadas posteriormente.
Para o cliente Raízen, é necessário realizar a inversão do código de empresa no sistema Tax One, garantindo que os dados sejam recebidos corretamente.
Os campos-chave: Empresa, Estabelecimento, Período, Código de Arrecadação, Código da Receita, Número do Documento de Origem e Status. Além disso, sempre que houver alteração no status da guia — como, por exemplo, de "Aguardando Pagamento" para "Guia Paga" — a SAFX deverá receber a atualização correspondente. Esse Retorno  proporcionará os seguintes benefícios:
Atualização automática do status das guias no Relatório de Status do sistema Tax One.
Registro detalhado e confiável dos valores pagos, retornados pela DOOTAX, para o status de Guias Pagas.
Disponibilização dos dados necessários para a geração da Guia Complementar.
Atualização de status para possibilitar cancelamentos, quando aplicável.




**Localização:**
Módulo: Básicos > Guias de Pagamentos
Menu: Guias de Pagamentos

**(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX346 conforme o Manual de Layout, o que facilita a consulta. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00).**

Procedimentos para a Importação da SAFX346:
**A importação da SAFX346 deve atender às seguintes premissas de negócio e comportamentos:**
Os campos obrigatórios e chaves devem estar devidamente preenchidos.
O processo deve identificar e atualizar corretamente o status da guia.
Resultado da Importação:
Se a importação for realizada com sucesso, os dados serão registrados nas seguintes telas:
**Tax One > Básico > Data Warehouse > Manutenção > Guias de Pagamentos > Relatório de Status**
**Tax One > Básico > Data Warehouse > Manutenção > Guias de Pagamentos > Guia Complementar**




Regra Geral para validação

1º ) Consistências Básicas:

Campos Data inválidos
Campos Obrigatórios
Campos Numéricos inválidos
Campo ID da Guia – Vide regra RN01
Campo ID do Título – Vide regra RN02
Campo CNPJ da Empresa – Vide regra RN03
Campo Código da Empresa – Vide regra RN04
Campo Código do Estabelecimento – Vide regra RN05
Campo Data da Competência – Vide regra RN08
Campo Tipo do Pagamento – Vide regra RN09
Campo Código de Receita – Vide regra RN10
Campo Código de Detalhamento da Receita – Vide regra RN11
Campo Tipo do Pagamento – Vide regra RN09
Campo Código de Receita – Vide regra RN10



REGRAS DE NEGÓCIO



Considerações deste modelo:

**Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**




---

| MFS | Nome | Descrição |
| --- | --- | --- |
| ADO- 877116 | Beatriz Tie Terada, Millys Lopes | Definição das regras de importação da SAFX346 |
| ADO-1043049 | Millys Lopes | Alterar o campo GRUPO_IMPOSTO de obrigatório para não obrigatório |
| ADO-1043049 | Millys Lopes | Alterar o nome descrição do campo TIPO_PAGTO |


---

| CÓD | DESCRIÇÃO | MFS |
| --- | --- | --- |
| RN00 |  | ADO- 877116 1043049 |
| RN00.1 | Campos Obrigatório não preenchido  Se algum campo de preenchimento obrigatório não estiver preenchido, exibir a mensagem “Campo <<Nome do campo>> deve ser preenchido” | ADO- 877116 |
| RN01 | Campo 01 – ID da Guia  Tabela: SAFX346 Item: 01 Nome do Campo: ID_GUIA Descrição: ID da Guia  Tipo: N Tamanho: 038 Campo Não Obrigatório Chave Primária Comentário: Informar o ID da Guia de Pagamento | ADO- 877116 |
| RN02 | Campo 02 – ID do Título  Tabela: SAFX346 Item: 02 Nome do Campo: ID_TITULO Descrição: ID do Título Tipo: N Tamanho: 038 Campo Não Obrigatório Comentário:  Informar o Título da Guia de Pagamento | ADO- 877116 |
| RN03 | Campo 03 – CNPJ da Empresa  Tabela: SAFX346 Item: 03 Nome do Campo: CNPJ_EMPRESA Descrição: CNPJ da Empresa  Tipo:A Tamanho: 014 Campo Não Obrigatório Chave Primária Comentário: Informar o CNPJ da Empresa | ADO- 877116 |
| RN04 | Campo 04 – Código da empresa   Tabela: SAFX346 Item: 04 Nome do Campo: COD_EMPRESA Descrição: Código da empresa Tipo: N Tamanho: 008 Campo Obrigatório Chave Primária Comentário: Informar o Código da Empresa Exibir a mensagem da TFIX 22 CÓDIGO 90001 | ADO- 877116 |
| RN05 | Campo 05 – Código do estabelecimento  Tabela: SAFX346 Item: 05 Nome do Campo: COD_ESTAB Descrição: Código do estabelecimento Tipo: C Tamanho: 006  Campo Obrigatório Chave Primária Comentário: Informar o Código do Estabelecimento | ADO- 877116 |
| RN06 | Campo 06 – Inscrição Substituta  Tabela: SAFX346 Item: 06 Nome do Campo: INSC_SUBSTITUTA Descrição: Inscrição substituta. Tipo: N Tamanho: 30 Campo Não Obrigatório Comentário: Informar a Inscrição Substituta Exibir a mensagem da TFIX 22 CÓDIGO 90002 | ADO- 877116 |
| RN07 | Campo 07 – Tipo de Inscrição Substituta  Tabela: SAFX346 Item: 07 Nome do Campo: TIPO_INSC_SUBSTITUTA Descrição: Tipo de Inscrição Substituta. Tipo: C Tamanho: 40 Campo Não Obrigatório Comentário: Informar o Tipo de Inscrição Substituta | ADO- 877116 |
| RN08 | Campo 08 – Data da Competência  Tabela: SAFX346 Item: 08 Nome do Campo: DATA_COMP Descrição: Data de competência da conta. Tipo: N Tamanho: 008 Campo Não Obrigatório Comentário: Informar a Data da Competência da Conta. Exemplo: AAAAMMDD | ADO- 877116 |
| RN09 | Campo 09 – Tipo de Pagamento   Tabela: SAFX346 Item: 09 Nome do Campo: TIPO_PAGTO Descrição: Código de Arrecadação Tipo: String Tamanho: 4000 Campo Não Obrigatório Comentário: Informar o tipo de pagamento, de acordo com a Guia. | ADO- 877116 |
| RN10 | Campo 10 – Código de Receita  Tabela: SAFX346 Item: 10 Nome do Campo: COD_RECEITA Descrição: Código da receita que está sendo paga. Tipo: Number Tamanho: 020 Campo Obrigatório Chave Primária Comentário: Este campo informa o Código de Receita. Exibir a mensagem da TFIX 22 CÓDIGO 913298 | ADO- 877116 |
| RN11 | Campo 11 – Código de Detalhamento da Receita  Tabela: SAFX346 Item: 11 Nome do Campo: DET_RECEITA Descrição: Código do detalhamento da receita. Tipo: N Tamanho: 020 Campo Obrigatório Chave Primária Comentário: Este campo informa o Detalhamento da Receita.  Exibir a mensagem da TFIX 22 CÓDIGO 913299 | ADO- 877116 |
| RN12 | Campo 12 – GRUPO de IMPOSTO  Tabela: SAFX346 Item: 12 Nome do Campo: GRUPO_IMPOSTO Descrição: Nome do imposto Tipo: C Tamanho: 030 Campo Não Obrigatório. Comentário: | ADO- 877116 1043049 |
| RN13 | Campo 13 – Unidade Federal Favorecida  Tabela: SAFX346 Item: 13 Nome do Campo: UF_FAVORECIDA  Descrição: UF favorecida  Tipo: C Tamanho: 002 Campo Não Obrigatório Comentário: Este campo informa a Unidade Federal Favorecida conforme a SAFX 163 (Guia de Recolhimento de Tributos Estaduais – GNRE), SAFX 223 (Tabela das Guias de Recolhimento do ICMS Diferencial de Alíquota UF Orig./Dest (EC 87/15)), SAFX 224 (Tabela das Guias de Recolhimento do ICMS Diferencial de Alíquota UF Orig./Dest (EC 87/15) – Módulo PIM), SAFX 305 (Tabela das Guias de Recolhimento da Apuração do ICMS) | ADO- 877116 |
| RN14 | Campo 14 – Código do Documento   Tabela: SAFX346 Item: 14 Nome do Campo: COD_DOC Descrição: Código da Cidade do Documento. Tipo: N Tamanho: 038 Campo Não Obrigatório Comentário: Este campo informa Código da Cidade do Documento | ADO- 877116 |
| RN15 | Campo 15 – Número do Documento  Tabela: SAFX346 Item: 15 Nome do Campo: NUM_DOC_ORIGEM Descrição: Número do Documento Tipo: N Tamanho: 4000 Campo Obrigatório Comentário: Este campo informa o Número do Documento Exibir a mensagem da TFIX 22 CÓDIGO 913300 | ADO- 877116 |
| RN16 | Campo 16 – Série  Tabela: SAFX346 Item: 16 Nome do Campo: SERIE_DOC Descrição: Série do documento Tipo: C Tamanho: 003 Campo Não Obrigatório Comentário: Este campo possui informações referente a Série do Documento | ADO- 877116 |
| RN17 | Campo 17 – Chave de Nota Fiscal  Tabela: SAFX346 Item: 17 Nome do Campo: CHAVE_NF Descrição: Chave NF Tipo: N Tamanho:44 Campo Não Obrigatório Comentário: Este campo possui informações referentes a Chave de Nota Fiscal | ADO- 877116 |
| RN18 | Campo 18 – Indicação de Cancelamento  Tabela: SAFX346 Item: 18 Nome do Campo: IND_CANCELAMENTO Descrição: Indicação de cancelamento Tipo: Boolean Tamanho: True/false Campo Não Obrigatório Comentário: Este campo indica se ocorreu ou não o cancelamento das Guias de Pagamento | ADO- 877116 |
| RN19 | Campo 19 – Informações de Cancelamento  Tabela: SAFX346 Item: 19 Nome do Campo: INFO_CANCELAMENTO Descrição: Informações sobre o cancelamento Tipo: String Tamanho: 4000 Campo Não Obrigatório  Comentário: Este campo exibe informações referentes ao cancelamento das Guias. | ADO- 877116 |
| RN20 | Campo 20 - Status  Tabela: SAFX346 Item: 20 Nome do Campo: STATUS Descrição: Status da Guia de Pagamento Tipo: N Tamanho: 38 Campo Obrigatório Comentário: Informar  o código do status da guia de pagamento. O campo STATUS deve ser preenchido e informar o codigo do status da guia de pagamento. (Vide RN21) Exibir a mensagem da TFIX 22 CÓDIGO 913340 | ADO- 877116 |
| RN21 | Campo 21 – Descrição do Status  Tabela: SAFX346 Item: 21 Nome do Campo: DSC_STATUS Descrição: Descrição do status Tipo: C Tamanho: 50 Campo Obrigatório Comentário: Exibir o status das Guias de Pagamento, podendo variar entre: 1) Aguardando Guia, 2) Processando Guia, 3) Aguardando Pagamento, 4) Aguardando Aprovação, 5) Processando Pagamento e 6) Guia Paga. Compõe o campo STATUS  O campo DSC_STATUS deve ser preenchido e informar a descrição do status da guia de pagamento (RN20) Exibir a mensagem da TFIX 22 CÓDIGO 913341 | ADO- 877116 |
| RN22 | Campo 22 – Valor Principal do Título  Tabela: SAFX346 Item: 22 Nome do Campo: VLR_PRINCIPAL Descrição: Valor principal do título Tipo: N Tamanho: 38 Campo Não Obrigatório Comentário: Este campo possui informações referentes ao Valor Principal do Título/Documento de Arrecadação Exibir a mensagem da TFIX 22 CÓDIGO 913296 | ADO- 877116 |
| RN23 | Campo 23 – Valor do Fundo Estadual de Combate à Pobreza  Tabela: SAFX346 Item: 23 Nome do Campo: VLR_FECP Descrição: Valor do recolhimento ao Fundo Estadual de Combate à Pobreza. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr_principal com o valor da guia excluído o valor do recolhimento ao FECP. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr_principal. Tipo: N Tamanho: 015V002 Campo Não Obrigatório Comentário: Este campo possui informações referentes ao Valor do Fundo Estadual de Combate à Pobreza. | ADO- 877116 |
| RN24 | Campo 24 – Valor dos Juros  Tabela: SAFX346 Item: 24 Nome do Campo: VLR_JUROS Descrição: Valor dos juros quando o pagamento ocorrer em atraso. Esse campo foi calculado automaticamente pelo sistema, caso não tenha sido informado na integração. Tipo: N Tamanho: 015,2 Campo Não Obrigatório Comentário: Este campo possui informações referentes ao Valor dos Juros, que, caso não tenha sido informado na integração, o sistema fez o cálculo automaticamente. | ADO- 877116 |
| RN25 | Campo 25 – Valor da Multa   Tabela: SAFX346 Item: 25 Nome do Campo: VLR_MULTA Descrição: Valor da multa quando o pagamento ocorrer em atraso. Esse campo será calculado automaticamente pelo sistema, caso não seja informado na integração. Tipo: N Tamanho: 015V002 Campo Não Obrigatório Comentário: Este campo possui informações referentes ao Valor da Multa, que, caso não tenha sido informado na integração, o sistema fez o cálculo automaticamente. | ADO- 877116 |
| RN26 | Campo 26 – Valor de Atualização Monetária  Tabela: SAFX346 Item: 27 Nome do Campo: VLR_ATUAL_MONETARIA Descrição: Valor da atualização monetária  Tipo: N Tamanho: 038 Campo Não Obrigatório Comentário: Informa o Valor de Atualização Monetária. | ADO- 877116 |
| RN27 | Campo 27 – Outros Valores  Tabela: SAFX346 Item: 27 Nome do Campo: VLR_OUTROS  Descrição: Outros valores Tipo: N Tamanho: 015V002 Campo Não Obrigatório Comentário: Este campo possui informações referentes a Outros Valores, retornadas de acordo com o banco, com o qual foi feito o recolhimento dos impostos ICMS, ICMS-ST,ICMS ANTECIPADO, PIS/COFINS, IRPJ-CSLL, IRPJ-CSLL, IPI, DIFAL, FCP. | ADO- 877116 |
| RN28 | Campo 28 - Valor do Fundo Estadual de Combate à Pobreza – Juros  Tabela: SAFX346 Item: 28 Nome do Campo: VLR_FECP_JUROS Descrição: Valor dos juros sobre o recolhimento ao Fundo Estadual de Combate à Pobreza, quando o pagamento ocorrer em atraso. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr_juros com o valor dos juros excluído o valor dos juros referente ao FECP. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr_juros. Esse campo será calculado automaticamente pelo sistema caso não tenha sido informado na integração. Tipo:N Tamanho: 015V002 Campo Não Obrigatório Chave Primária Comentário: Este campo possui informações referentes ao Valor de Juros referente ao Fundo Estadual de Combate à Pobreza, que, caso não tenha sido informado na integração, o sistema fez o cálculo automaticamente. | ADO- 877116 |
| RN29 | Campo 29 – Valor do Fundo Estadual de Combate à Pobreza – Multa  Tabela: SAFX346 Item: 29 Nome do Campo: VLR_FECP_MULTA Descrição: Valor da multa sobre o recolhimento ao Fundo Estadual de Combate à Pobreza, quando o pagamento ocorrer em atraso. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr_multa com o valor da multa excluído o valor da multa referente ao FECP. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr_multa. Esse campo será calculado automaticamente pelo sistema caso não tenha sido informado na integração.  Tipo: N Tamanho: 015V002 Campo Não Obrigatório Chave Primária Comentário: Este campo possui informações referentes ao Valor de Multa referente ao Fundo Estadual de Combate à Pobreza, que, caso não tenha sido informado na integração, o sistema fez o cálculo automaticamente. | ADO- 877116 |
| RN30 | Campo 30 – Valor Total  Tabela: SAFX346 Item: 30 Nome do Campo: VLR_TOTAL Descrição: Valor total Tipo: N Tamanho: 38 Campo Não Obrigatório Chave Primária Comentário: Este campo possui informações referentes ao Valor Total, retornadas de acordo com o banco, com o qual foi feito o recolhimento dos impostos ICMS, ICMS-ST,ICMS ANTECIPADO, PIS/COFINS, IRPJ-CSLL, IRPJ-CSLL, IPI, DIFAL, FCP. | ADO- 877116 |
| RN31 | Campo 31 – Código do Produto  Tabela: SAFX346 Item: 32 Nome do Campo: COD_PRODUTO  Descrição: Na emissão da GNRE, algumas UFs exigem o preenchimento do código do produto no recolhimento do ICMS por apuração. Consulte a UF para obter a lista de códigos de produtos válidos. Tipo: N Tamanho: 005 Campo Não Obrigatório Chave Primária Comentário: Este campo informa o Código do Produto conforme a SAFX 163 (Guia de Recolhimento de Tributos Estaduais – GNRE), SAFX 223 (Tabela das Guias de Recolhimento do ICMS Diferencial de Alíquota UF Orig./Dest (EC 87/15)), SAFX 224 (Tabela das Guias de Recolhimento do ICMS Diferencial de Alíquota UF Orig./Dest (EC 87/15) – Módulo PIM), SAFX 305 (Tabela das Guias de Recolhimento da Apuração do ICMS) | ADO- 877116 |
| RN32 | Campo 32 – Convênio  Tabela: SAFX346 Item: 32 Nome do Campo: CONVENIO Descrição: Convênio ou protocolo ICMS que regulamenta a forma de recolhimento do tributo. Esse campo é utilizado na geração da GNRE por apuração. Tipo: C Tamanho: 030 Campo Não Obrigatório Chave Primária Comentário: Este campo possui informações referentes ao Convênio, retornadas de acordo com o banco, com o qual foi feito o recolhimento dos impostos ICMS, ICMS-ST,ICMS ANTECIPADO, PIS/COFINS, IPI, DIFAL, FCP. | ADO- 877116 |
| RN33 | Campo 33 – CNPJ Favorecido  Tabela: SAFX346 Item: 34 Nome do Campo: CNPJ_FAVORECIDO Descrição: CNPJ do favorecido. Esse campo é usado para identificar o favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros. Tipo: A Tamanho: 014 Campo Não Obrigatório Comentário: Informar o CNPJ do Favorecido | ADO- 877116 |
| RN34 | Campo 34 – Inscrição Estadual do Favorecido  Tabela: SAFX346 Item: 34 Nome do Campo: INSC_ESTADUAL_FAVORECIDO Descrição: Inscrição Estadual do favorecido.  Esse campo é usado para identificar o favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros.  Tipo: C Tamanho: 030 Campo Não Obrigatório Comentário: Esse campo identifica a inscrição estadual do favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros. | ADO- 877116 |
| RN35 | Campo 35 – CPF do Favorecido  Tabela: SAFX346 Item: 35 Nome do Campo: CPF_FAVORECIDO Descrição: CPF do favorecido Tipo: A Tamanho: 014 Campo Não Obrigatório Comentário: Esse campo identifica o CPF do favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros. | ADO- 877116 |
| RN36 | Campo 36 – Informações Complementares  Tabela: SAFX346 Item: 36 Nome do Campo: INFO_COMPL_DOCUMENTO Descrição: Informações complementares do documento  Tipo: C Tamanho: 050 Campo Não Obrigatório Comentário: Exibe as informações complementares referentes ao documento. | ADO- 877116 |
| RN37 | Campo 37 – Indicador de Erro  Tabela: SAFX346 Item: 38 Nome do Campo: IND_ERRO Descrição: Indicador de erro Tipo: Boolean Tamanho: True/false Campo Não Obrigatório Comentário: Este campo indica a possibilidade de ter ocorrido ou não um erro por parte do sistema. | ADO- 877116 |
| RN38 | Campo 38 – Mensagem de Erro  Tabela: SAFX346 Item: 39 Nome do Campo: MENSAGEM_ERRO Descrição: Mensagem de erro Tipo: String Tamanho: 4000 Campo Não Obrigatório Comentário: Caso tenha ocorrido um erro, o sistema exibirá uma mensagem especificando o erro que ocorreu. | ADO- 877116 |
| RN39 | Campo 39 – Data de Vencimento  Tabela: SAFX346 Item: 39 Nome do Campo: DATA_VENCTO Descrição: Informar a data de vencimento da Guia. Tipo: N Tamanho: 008 Campo Não Obrigatório Comentário: Informar a Data do Vencimento  da Guia de Pagamento. | ADO- 877116 |
| RN40 | Campo 40 – Data de Vencimento Original  Tabela: SAFX346 Item: 40 Nome do Campo: DATA_VENCTO_ORIGINAL Descrição: data de vencimento original Tipo: N Tamanho: 8 Campo Não Obrigatório Comentário: Informar a  Data de Vencimento Original da Guia de Pagamento. | ADO- 877116 |
| RN41 | Campo 41– Código de Barras  Tabela: SAFX346 Item: 41 Nome do Campo: COD_BARRAS Descrição: Código de Barras Tipo: String Tamanho: 4000 Campo Não Obrigatório Comentário: Informar o código de barras da Guia de Pagamento. | ADO- 877116 |
| RN42 | Campo 42 – Número de Controle  Tabela: SAFX346 Item: 42 Nome do Campo: NUM_CONTROLE Descrição: Número de Controle Tipo: String Tamanho: 4000 Campo Não Obrigatório Comentário: Informar o número de controle do documento de arrecadação. | ADO- 877116 |
| RN43 | Campo 43 – Data SEFAZ  Tabela: SAFX346 Item: 43 Nome do Campo: DATA_SEFAZ Descrição: Data da resposta do SEFAZ Tipo: N Tamanho: 8 Campo Não Obrigatório Comentário: Informa a data de resposta da Secretaria da Fazenda. | ADO- 877116 |
| RN44 | Campo 44 – ID do Pagamento  Tabela: SAFX346 Item: 44 Nome do Campo: ID_PAGTO Descrição: ID do pagamento  Tipo: N Tamanho: 38 Campo Não Obrigatório Comentário: Informa a Identificação do Pagamento | ADO- 877116 |
| RN45 | Campo 45 – Data do Pagamento  Tabela: SAFX346 Item: 45 Nome do Campo: DATA_PAGTO Descrição: Data do Pagamento. Esse campo será calculado automaticamente pelo sistema Tax Payments. Tipo: N Tamanho: 008 Campo Não Obrigatório Comentário: Informar a Data do Pagamento. Este campo será calculado automaticamente pelo sistema Tax Payments. | ADO- 877116 |
| RN46 | Campo 46 – Número de Autenticação  Tabela: SAFX346 Item: 46 Nome do Campo: NUM_AUTENTICACAO Descrição: Número da autenticação  Tipo: String Tamanho: 4000 Campo Não Obrigatório Comentário: Informar o Número de Autenticação Bancária | ADO- 877116 |
| RN47 | Campo 47 – ID do Pagador  Tabela: SAFX346 Item: 47 Nome do Campo: ID_PAGADOR Descrição: ID do pagador Tipo: N Tamanho: 038 Campo Não Obrigatório Chave Primária Comentário: Informar a identificação do pagador | ADO- 877116 |
| RN48 | Campo 48 – CNPJ do Pagador  Tabela: SAFX346 Item: 48 Nome do Campo: CNPJ_PAGADOR Descrição: CNPJ do pagador Tipo: A Tamanho: 014 Campo Não Obrigatório Comentário: Informar o CNPJ do Pagador | ADO- 877116 |
| RN49 | Campo 49 – Código do Banco  Tabela: SAFX346 Item: 49 Nome do Campo: COD_BANCO Descrição: Código do banco Tipo: N Tamanho: 003 Campo Não Obrigatório Comentário: Informar o Código do Banco | ADO- 877116 |
| RN50 | Campo 50 – Agência  Tabela: SAFX346 Item: 50 Nome do Campo: AGENCIA Descrição: Agência Tipo: N  Tamanho: 005 Campo Não Obrigatório Comentário: Informar a agência bancária | ADO- 877116 |
| RN51 | Campo 51 – Dígito da Agência  Tabela: SAFX346 Item: 51 Nome do Campo: DIG_AGENCIA Descrição: Dígito da Agência   Tipo: N Tamanho: 001 Campo Não Obrigatório Comentário:  Informar o Dígito que compõe a Agência Bancária | ADO- 877116 |
| RN52 | Campo 52 – Conta Corrente  Tabela: SAFX346 Item: 52 Nome do Campo: CONTA_CORRENTE Descrição: Conta Corrente Tipo: N  Tamanho: 015 Campo Não Obrigatório Comentário:  Informar a Conta Corrente | ADO- 877116 |
| RN53 | Campo 53 – Dígito da Conta Corrente   Tabela: SAFX346 Item: 53 Nome do Campo: DIG_CONTA_CORRENTE Descrição: Dígito da conta corrente Tipo: N Tamanho: 001 Campo Não Obrigatório Comentário:  Informar o Dígito que compõe a Conta Corrente | ADO- 877116 |
| RN54 | Campo 54 – Objeto JSON  Tabela: SAFX346 Item: 55 Nome do Campo: OBJETO_JSON Descrição: Objeto JSON com customizações das regras de pagamento associadas à guia Tipo: Null Tamanho: - Campo Não Obrigatório Comentário:  Informar o Objeto JSON com customizações das regras de pagamento associadas à guia | ADO- 877116 |
| RN55 | Campo 55 – Array Bytes  Tabela: SAFX346 Item: 55 Nome do Campo: ARRAY_BYTES Descrição: Array de bytes do PDF, comprimido usando biblioteca de compressão Zlib e codificado em Base64 Tipo: String Tamanho: - Campo Não Obrigatório Comentário:  Informar o array de bytes do PDF, comprimido usando biblioteca de compressão Zlib e codificado em Base64. | ADO- 877116 |
| RN56 | Campo 56 – Conteúdo JSON  Tabela: SAFX346 Item: 57 Nome do Campo: CONTEUDO_JSON Descrição: Conteúdo que foi recebido no atributo campos extras do JSON Tipo: C Tamanho: - Campo Não Obrigatório Comentário:  Este campo possui informações referentes ao conteúdo que foi recebido no atributo campos extras do JSON | ADO- 877116 |
| RN57 | Campo 57 – QR Code do PIX  Tabela: SAFX346 Item: 57 Nome do Campo: QR_CODE_PIX Descrição: QR Code do PIX Tipo: String Tamanho: 4000 Campo Não Obrigatório Comentário:  Comentário:  Informar o QR Code da transação realizada através do PIX | ADO- 877116 |
| RN58 | Campo 58 – Login do Usuário  Tabela: SAFX346 Item: 58 Nome do Campo: LOGIN_USUARIO Descrição: Login do usuário que importou o arquivo Tipo: String Tamanho: 4000 Campo Não Obrigatório Comentário:  Informar o Login de Usuário que importou o arquivo | ADO- 877116 |
| RN59 | Campo 59 – Data de Débito  Tabela: SAFX346 Item: 59 Nome do Campo: DAT_DEBITO Descrição: Data de Débito Tipo: N Tamanho: 008 Campo Não Obrigatório Comentário:  Este campo possui informações referentes a Data de Débito. | ADO- 877116 |
| RN60 | Campo 60 – Total de Elementos  Tabela: SAFX346 Item: 60 Nome do Campo: TOTAL_ELEMENTOS Descrição: Total de Registros/Elementos da página Tipo: N Tamanho: 038 Campo Não Obrigatório Comentário:  Informar o Total de Registros da Página | ADO- 877116 |
| RN61 | Campo 61 – Total de Páginas  Tabela: SAFX346 Item: 61 Nome do Campo: TOTAL_PAGINAS Descrição: Total de páginas Tipo: N Tamanho: 038 Campo Não Obrigatório Comentário:  Informar o Total de Páginas | ADO- 877116 |
| RN62 | Campo 62 – Tamanho  Tabela: SAFX346 Item: 62 Nome do Campo: TAMANHO Descrição: Tamanho máximo da página (máximo 100) Tipo: N Tamanho: 038 Campo Não Obrigatório Comentário:  Este campo possui informações referentes ao Tamanho Máximo de Páginas | ADO- 877116 |
| RN63 | Campo 63 – Número  Tabela: SAFX346 Item: 63 Nome do Campo: NUMERO Descrição: Número da página Tipo: N Tamanho: 038 Campo Não Obrigatório Comentário:  Este campo possui informações referentes ao Número da Página | ADO- 877116 |
| RN64 | Campo 64 – Número de Elementos  Tabela: SAFX346 Item: 64 Nome do Campo: NUMERO_ELEMENTOS Descrição: Número de registros da página Tipo: N Tamanho: 038 Campo Não Obrigatório Comentário:  Este campo possui informações referentes ao Número de Registros da Página | ADO- 877116 |
| RN65 | Campo 65 – Último  Tabela: SAFX346 Item: 65 Nome do Campo: ULTIMO Descrição: Retorna a informação se a página atual é a última Tipo: N Tamanho: 038 Campo Não Obrigatório Comentário:  Este campo possui informações permitindo ao usuário saber se a página atual é a última | ADO- 877116 |
| RN66 | Campo 66 – Primeiro  Tabela: SAFX346 Item: 66 Nome do Campo: PRIMEIRO Descrição: Retorna informação se a página atual é a primeira Tipo: N Tamanho: 038 Campo Não Obrigatório Comentário:  Este campo possui informações permitindo ao usuário verificar se a página atual é a primeira | ADO- 877116 |
| RN67 | Campo 67 – Ordenação  Tabela: SAFX346 Item: 67 Nome do Campo: ORDENACAO Descrição: É utilizado na ordenação do resultado Tipo: N Tamanho: 038 Campo Não Obrigatório Comentário:  Este campo possui informações referentes a Ordenação do Resultado | ADO- 877116 |


---

| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |


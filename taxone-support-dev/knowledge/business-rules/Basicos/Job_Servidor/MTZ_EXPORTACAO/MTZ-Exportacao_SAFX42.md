# MTZ-Exportacao_SAFX42

- **Fonte:** MTZ-Exportacao_SAFX42.docx
- **Modificado:** 2025-07-04
- **Tamanho:** 40 KB

---

__         __

# Módulo Job Servidor – Importação SAFX42 \(Documento Fiscal Utilities\)

                      Localização: Menu Básicos, Módulo: Job Servidor, item Exportação de Dados 

__*\(Obs: As regras descritas neste documento são numeradas de acordo com os campos  da SAFX42, conforme o Manual de Layout,  o que facilita a consulta\) *__

__*\(Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como  RN00\)*__

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__OS2890__

Criação de campos para atendimento do Ato Cotepe 24/2010

Criação de campos referente as notas de fiscais modelo 21 e 22 de  Ressarcimento ao Cliente\.

__OS3424__

Criação de campos para atendimento Portaria CAT Nº 115/11, que altera a Portaria CAT Nº 187/10

Criação de campos para atendimento Portaria CAT Nº 115/11, que altera a Portaria CAT Nº 187/10

__OS4076__

Inclusão do campo “Número do Item da Nota Fiscal de Ressarcimento ao Cliente” no Registro Tipo 2 do Anexo I

De acordo com o INFOLEGIS nº 288/13 – C, o CONFAZ disponibilizou o Ato Cotepe/ICMS n° 22, de 18/06/2013 alterando o item 5 do Anexo I do Ato Cotepe/ICMS nº 24/2010, que trata do registro de itens com ICMS recuperado ou a recuperar\.

O item 5 do anexo I, passa a vigorar com as seguintes alterações:

__DESCRICAO__

__TAM__

__DE__

__ATE__

__TIPO__

27

Número do item da Nota Fiscal de ressarcimento ao cliente     

3

508

511

N

28

Brancos

10

512

520

X

Este Ato entra em vigor na data de sua publicação no Diário Oficial da União em 24/06/2013\.

A alteração ocorrerá no Registro Tipo “2” do Anexo I do meio magnético gerado\. Essa alteração ocorrerá nesse ponto do sistema, visto que ocorreu somente a inclusão de um novo campo\.

OS4316

Criação de Campos

Criação dos campos Código e Descrição da SCP

OS4579

Alteração no tamanho do campo 

Alteração no tamanho do campo NUM\_LANCTO\_CONTABIL para 40 posições\.

MFS\-851680

Alessandra Cristina Navatta

Aumento do campo 54 \- Canal de Distribuição/ Código da Obra \(RN54\)

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

*\(espaço reservado para regras genéricas, que não dizem respeito a campos específicos\)*

__RN01__

__Campo Código da SCP__

Alterar a rotina de exportação para que seja considerado o novo campo:

Tabela: SAFX42

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

__OS4316__

__RN54__

__Campo Código da Obra__

A rotina de Exportação do módulo JOB Servidor deve ser ajustada para que contemple a alteração de aumento do campo COD\_CANAL\_DISTRIB da tabela SAFX42\-Capa de Documentos Fiscais de Utilities\. 

__![](data:image/png;base64,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)__

__Item__: 54

__Nome__: COD\_CANAL\_DISTRIB

__Descrição__: Canal de Distribuição/ Código da Obra

__Tamanho__: 15

__Tipo__: A

__Obrigatoriedade__: N

MFS\-851680

__RN97__

__Campo 97 \(Sugerido\):__ Número da NF com ressarcimento ao cliente

__Item__: 97 \(Sugerido\)

__Descrição do campo__: Número da NF com ressarcimento ao cliente

__Nome do campo__: A ser definido pelo A&D

__Comentário__: Número da Nota Fiscal com ressarcimento ao cliente\. Essa informação deve ser preenchida nos casos de Documentos Fiscais de Utilities cujo modelo seja 21 – Comunicação ou 22 – Telecomunicação para geração dos arquivos digitais do módulo Estorno de Débitos – Modelos 21/22 nos layouts “Ato COTEPE 24/2010” e “Portaria CAT 06/2009”\.

__Tamanho__: 012

__Tipo__: N

__OS2890__

__RN98__

__Campo 98 \(Sugerido\):__ Série da NF com ressarcimento ao cliente

__Item__: 98 \(Sugerido\)

__Descrição do campo__: Série da NF com ressarcimento ao cliente

__Nome do campo__: A ser definido pelo A&D

__Comentário__: Série da Nota Fiscal com ressarcimento ao cliente\.\. Essa informação deve ser preenchida nos casos de Documentos Fiscais de Utilities cujo modelo seja 21 – Comunicação ou 22 – Telecomunicação para geração dos arquivos digitais do módulo Estorno de Débitos – Modelos 21/22 nos layouts “Ato COTEPE 24/2010” e “Portaria CAT 06/2009”\.

__Tamanho__: 003

__Tipo__: A

__OS2890__

__RN99__

__Campo 99 \(Sugerido\):__ Modelo da NF com ressarcimento ao cliente

__Item__: 99 \(Sugerido\)

__Descrição do campo__: Modelo da NF com ressarcimento ao cliente

__Nome do campo__: A ser definido pelo A&D

__Comentário__: Modelo da Nota Fiscal com ressarcimento ao cliente\. O Código deve estar registrado na Tabela de Modelos de Documentos Fiscais \(__SAFX2024__\)\.

Essa informação deve ser preenchida nos casos de Documentos Fiscais de Utilities cujo modelo seja 21 – Comunicação ou 22 – Telecomunicação para geração dos arquivos digitais do módulo Estorno de Débitos – Modelos 21/22 nos layouts “Ato COTEPE 24/2010” e “Portaria CAT 06/2009”\.

__Tamanho__: 002

__Tipo__: N

__OS2890__

__RN100__

__Campo 100 \(Sugerido\):__ Data de Emissão da NF com ressarcimento ao cliente

__Item__: 100 \(Sugerido\)

__Descrição do campo__: Data de Emissão da NF com ressarcimento ao cliente

__Nome do campo__: A ser definido pelo A&D

__Comentário__: Data de Emissão da Nota Fiscal com ressarcimento ao cliente\. Essa informação deve ser preenchida nos casos de Documentos Fiscais de Utilities cujo modelo seja 21 – Comunicação ou 22 – Telecomunicação para geração dos arquivos digitais do módulo Estorno de Débitos – Modelos 21/22 nos layouts “Ato COTEPE 24/2010” e “Portaria CAT 06/2009”\.

__Tamanho__: 008

__Tipo__: D

__OS2890__

__RN102__

__Campo 102 \(campo reservado\): JUROS DE MORA__

__Item__: 102 \(Reservado\)

__Descrição do campo__: Juros de Mora

__Nome do campo__: A ser definido pelo A&D

__Comentário__: Valor referente a Juros de Mora

__Tamanho__: 015V002

__Tipo__: N

__OS3424__

__RN103__

__Campo 103 \(campo reservado\): MULTA DE MORA__

__Item__: 103 \(Reservado\)

__Descrição do campo__: Multa de Mora

__Nome do campo__: A ser definido pelo A&D

__Comentário__: Valor referente a Multa de Mora

__Tamanho__: 015V002

__Tipo__: N

__OS3424__

__RN104__

__Campo 104 \(campo reservado\): ACRÉSCIMOS LEGAIS__

__Item__: 104 \(Reservado\)

__Descrição do campo__: Acréscimos Legais

__Nome do campo__: A ser definido pelo A&D

__Comentário__: Valor referente a Acréscimos Legais

__Tamanho__: 015V002

__Tipo__: N

__OS3424__

### RN105

__Campo 105 \(campo reservado\): DATA FIM AÇÃO JUDICIAL:__

__Item:__ 105 \(Reservado\)

__Descrição do campo:__ Data Fim Ação Judicial

__Nome do campo:__ A ser definido pelo A&D

__Comentário:__ Referente a Data Fim da Ação Judicial

__Tamanho:__ 008

__Tipo:__ N

__OS3424__

### RN106

__Campo – Número do Item da Nota Fiscal de Ressarcimento ao Cliente__

__Tabela: __SAFX42

__Item: __A ser definido pelo A&D

__Nome do Campo:__ Será definido pelo A&D

__Descrição:__ Número do Item da Nota Fiscal de Ressarcimento ao Cliente

__Tipo:__ N

__Tamanho: __003

__Não Obrigatório__

__OS4076__

### RN107

A rotina de Exportação do módulo JOB Servidor deve ser ajustada para que contemple a alteração no campo NUM\_LANCTO\_CONTAIL da tabela SAFX42 – Arquivo de Notas Fiscais para Hotéis, que deve ser criada com a seguinte estrutura:

__ __

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

NUM\_LANCTO\_CONTABIL

A

40

NAO

NAO

__OS4579__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


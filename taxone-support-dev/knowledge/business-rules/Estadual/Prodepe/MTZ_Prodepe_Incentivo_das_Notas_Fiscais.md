# MTZ_Prodepe_Incentivo_das_Notas_Fiscais

- **Fonte:** MTZ_Prodepe_Incentivo_das_Notas_Fiscais.docx
- **Modificado:** 2025-12-22
- **Tamanho:** 35 KB

---

# Módulo PRODEPE – Rotina do Incentivo das Notas Fiscais

__Localização__: Menu Estadual, Módulo Prodepe, item Obrigações 🡪 Incentivo das Notas Fiscais

##### DOCUMENTO DE REQUISITO

###### __DR__

__Alteração__

__Data __

__Resp\.__

OS3722

Novas parametrizações p/ identificação dos produtos incentivados \(Indústria e CD\)\.

31/08/2012

\(criação do documento\)

Vânia Mattos

__MFS21913__

Alteração da tabela guia dos incentivos \(ICT\_GUIA\_INCENT\) para inclusão do Código de Informação Adicional\. Trata\-se do código da tabela “5\.6 \- Tabela informações adicionais dos itens do documento fiscal” do Sped Fiscal, utilizado no preenchimento do campo COD\_INF\_ITEM do registro C177 \(ver __RN05__\)\.

25/10/2018

Vânia Mattos

__ __

# RN00

__Regras Gerais:__

O item de menu da rotina de incentivo das notas trabalha com todos os tipos de incentivo \(Indústria, Importação e CD\), mas para cada um deles é feita a chamada de uma procedure específica, conforme o quadro abaixo:

__Procedure __

__Tipo do incentivo__

SAF\_GERA\_INCENT1   

Incentivo do tipo “Indústria” quando a regra do incentivo é controlada por período da apuração ou por período de validade da regra \(parâmetro informado no campo “Controle das Faixas de Incentivo” da manutenção das regras\)

SAF\_GERA\_INCENT1A

Incentivo do tipo “Indústria” quando a regra do incentivo é controlada por período da apuração *com base nos valores acumulados* \(parâmetro informado no campo “Controle das Faixas de Incentivo” da manutenção das regras\)

\(desenvolvido para o cliente Klabin\)

SAF\_GERA\_INCENT2

Incentivo do tipo “Importação”

SAF\_GERA\_INCENT3

Incentivo do tipo “Central de Distribuição”

__Parâmetros de tela__:

Período 🡪 Data inicial e final para a recuperação dos documentos fiscais que serão processados

 

Estabelecimento 🡪 Neste quadro serão exibidos todos os estabelecimentos da Empresa parametrizados no Prodepe \(menu “Parâmetros 🡪 Dados Gerais”\)

__Origem dos dados__:

- Documentos fiscais do período informado \(DWT\_DOCTO\_FISCAL e DWT\_ITENS\_MERC\)
- Tabela das regras do incentivo
- Tabela da parametrização dos produtos incentivados 
- Tabela da parametrização das operações incentivadas \(CFOP e CFOP/Natureza\)
- Tabela da parametrização dos Insumos Comuns \(CFOP/Natureza x Grupos de Incentivo\)  *\(somente Indústria\)*
- Tabela da parametrização das Vendas Não Incentivadas de Insumos Incentivados   *\(somente Indústria\)*

__Dados Gerados no Processo__:

- Tabela Guia das Operações Incentivadas / Não Incentivadas \(ICT\_GUIA\_INCENT\)
- Tabela do Histórico das Saídas dos Produtos Incentivados \(auxilia no controle das faixas\) \(ICT\_HIST\_INCENT\)

*                                                                                                                                                 \(somente Indústria e Importação\)*

- Tabela dos Valores Acumulados \(auxilia no controle das faixas\) \(ICT\_ACUMULADO\_INCE\) *\(somente Indústria\)*

Alteração __MFS21913:__

Conforme Portaria SF 126, de 30/08/2018, os contribuintes de PE passaram a gerar o Sped Fiscal a partir de 2019\. O registro C177 mudou o layout, e passou a ter um código para identificar os produtos e operações incentivados, além de identificar a sub apuração do Bloco 1 \(registros 1960/1970/1975/1980\)\. Por isso, a rotina do incentivo das notas passou a gerar este código de forma automática, e gravá\-lo na ICT\_GUIA\_INCENT para posterior utilização na geração do Sped Fiscal\. As regras da geração do código estão definidas na __RN05__\. 

# RN01

__Incentivo da Indústria   __\(com controle das faixas do incentivo por período da apuração ou por período de validade da regra\)

Alteração da __OS3722__ \(Set/2012\):

A geração do incentivo foi alterada para identificar os produtos incentivados através da nova parametrização de produtos \(menu “Parâmetros 🡪 Incentivo – Indústria 🡪 Produtos Incentivados”\)\. 

*Originalmente, ao recuperar os itens dos documentos fiscais, a verificação se o produto é incentivado ou não, era feita através do campo “16\-Código do Incentivo Fiscal” da SAFX2013, mas devido a problemas que começaram a ocorrer com usuários com mais de um estabelecimento em PE \(e todos beneficiários do Prodepe\), o campo 16 da SAFX2013 não será mais utilizado \(ver detalhes na OS3722\)\. *

# RN02

__Incentivo da Indústria__    \(com controle das faixas do incentivo por período da apuração com base nos valores acumulados\)

Alteração da __OS3722__ \(Set/2012\):

A geração do incentivo foi alterada para identificar os produtos incentivados através da nova parametrização de produtos \(menu “Parâmetros 🡪 Incentivo – Indústria 🡪 Produtos Incentivados”\)\. 

*Originalmente, ao recuperar os itens dos documentos fiscais, a verificação se o produto é incentivado ou não, era feita através do campo “16\-Código do Incentivo Fiscal” da SAFX2013, mas devido a problemas que começaram a ocorrer com usuários com mais de um estabelecimento em PE \(e todos beneficiários do Prodepe\), o campo 16 da SAFX2013 não será mais utilizado \(ver detalhes na OS3722\)\. *

# RN03

__Incentivo da Importação__

*Obs\.: Este incentivo nunca utilizou o campo “16\-Código do Incentivo Fiscal” da SAFX2013\. Ele já foi criado com parametrização de produto \(menu “Parâmetros 🡪 Incentivo – Importação 🡪 Produtos Incentivados”\)\.*

# RN04

__Incentivo da Central de Distribuição__

Alteração da __OS3722__ \(Set/2012\):

A geração do incentivo foi alterada para identificar os produtos incentivados através da nova parametrização de produtos \(menu “Parâmetros 🡪 Incentivo – Indústria 🡪 Produtos Incentivados”\)\. 

*Originalmente, ao recuperar os itens dos documentos fiscais, a verificação se o produto é incentivado ou não, era feita através do campo “16\-Código do Incentivo Fiscal” da SAFX2013, mas devido a problemas que começaram a ocorrer com usuários com mais de um estabelecimento em PE \(e todos beneficiários do Prodepe\), o campo 16 da SAFX2013 não será mais utilizado \(ver detalhes na OS3722\)\. *

# RN05

__Gravação do Código de Informação Adicional: __

Alteração __MFS21913__: Alteração da tabela guia dos incentivos \(ICT\_GUIA\_INCENT\) para inclusão do Código de Informação Adicional\. 

Este código se refere à tabela “__5\.6 \- Tabela informações adicionais dos itens do documento fiscal__” do Sped Fiscal, e é utilizado no preenchimento do campo COD\_INF\_ITEM do registro C177 \(registro “filho” do C170\)\.

Para o estado de PE o código tem a seguinte formatação: __PE XX XX XX, __onde:

     Posições 1 e 2 = sigla da UF de PE;

     Posições 3 e 4 = indica o tipo do incentivo \(Indústria, Importação ou Central de Distribuição\);

     Posições 5 e 6 = indica o código da apuração no Sped \(4\.7\.1\-Tabela de Indicadores de Sub Apuração por Tipo de Benefício\); 

     Posições 7 e 8 = indica se a operação é incentivada ou não incentivada;  

	

As regras para geração de cada componente do código se baseiam na informação dos seguintes campos da tabela das guias: COD\_GRP\_INCENT, SERIE\_LIVRO, SUB\_SERIE\_LIVRO, e IND\_INCENT, da seguinte forma:

 

__Posições 1 e 2:__

Conteúdo__ __= “PE”; 

__Posições 3 e 4__: 

O conteúdo será gerado a partir da informação do campo “Tipo de Incentivo” do cadastro do grupo de incentivo \(menu “Parâmetros > Grupos de Incentivo”\)\. Na tabela das guias, o grupo de incentivo é o campo COD\_GRP\_INCENT\.

      \- Se “Tipo de Incentivo” = “Indústria\-Crédito Presumido” ou “Indústria\-Crédito Presumido \(Sucata\)” 🡪 conteúdo = “01”   

      \- Se “Tipo de Incentivo” = “Importação\-Diferimento/Crédito Presumido”  🡪 conteúdo = “03”

      \- Se “Tipo de Incentivo” = “Central de Distribuição – Créd\. Presumido \(entrada e saída\)” 🡪 conteúdo = “04”

__Posições 5 e 6__:

O conteúdo será gerado a partir da parametrização “Livros Incentivados do PRODEPE x Indicador Sub\-Apuração” do Sped Fiscal \(módulo Sped Fiscal, menu “Parâmetros 🡪 Livros Incentivados PRODEPE x Indicador Sub\-Apuração da EFD”\)\. 

O conteúdo a ser gerado será exatamente o código de sub apuração parametrizado para a Série e Sub\-série da apuração do Prodepe \(colunas SERIE\_LIVRO e SUB\_SERIE\_LIVRO\);

Quando não for identificada a parametrização para a Série e Sub\-série da apuração em questão, o código não será gerado, e no log de erros será gravada a seguinte mensagem de erro:

*    “Não foi identificada a parametrização Livros Incentivados PRODEPE x Indicador Sub\-Apuração da EFD para a apuração\. *

*                                    O Código de Informação Adicional do Sped Fiscal \(C177\) não será gerado”*

O log deve mostrar a Série/Subsérie da apuração para conferência do usuário\.

Importante: Esta mensagem de erro deverá ser gerada __uma única vez__ para cada Série e Subsérie de Apuração\.

__Posições 7 e 8__: 

O conteúdo será gerado a partir do indicador de operação incentivada \(coluna IND\_INCENT\), da seguinte forma:

      \- Se IND\_INCENT <> “I” \(Operação não Incentivada\) 🡪 conteúdo = “01”   

      \- Se IND\_INCENT = “I” \(Operação Incentivada\) 🡪 conteúdo = “02”   

__OBS__: A tabela ICT\_GUIA\_INCENT possui apenas as operações com produtos incentivados\. Em relação às operações com produtos não incentivados, o código também será gerado de forma automática, mas no momento da geração do Sped Fiscal\. O conteúdo será o código específica de produtos não incentivados: “__PE000100__”\.

 


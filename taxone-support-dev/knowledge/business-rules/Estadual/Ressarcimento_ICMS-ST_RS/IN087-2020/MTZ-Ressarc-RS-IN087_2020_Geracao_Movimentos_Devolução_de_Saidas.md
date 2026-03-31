# MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Devolução de Saidas

- **Fonte:** MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Devolução de Saidas.docx
- **Modificado:** 2024-08-15
- **Tamanho:** 295 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 087/2020\) 

Geração dos Movimentos – Devolução de Saídas 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\),

 itens: Geração à IN\-RE 087/20 à Geração dos Movimentos 

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS48753__

Liliane Videira Assaf

Criação da funcionalidade\.

Não estamos trabalhando com Produtos Associados, apesar do documento mencionar tal parametrização em algumas regras\.

Não estamos considerando Devolução de Cupom Fiscal nesta entrega\.

22/12/2020 

__MFS58042__

Liliane Videira Assaf

2ª Entrega:

__Escopo da 2ª Entrega__

- Item 19\.3\-A\.1\.9, da IN 096/20

Operações contempladas:

- 778Saída para Outra UF \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)
- 780Devolução para fornecedor de outra UF, quando a retenção inicial foi realizada pelo próprio remetente da devolução, nos moldes do RICMS, Livro III, art\. 53\-A \(RICMS, Livro III, art\. 25\)
- 781Saída para Exportação \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)
- 782Saída Interna com nova ST \(RICMS, Livro III, art\.23, III\) \(e Devoluções\)
- 783Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.23, V\) \(e Devoluções\)

08/02/2021

__MFS59698__

Liliane Videira Assaf

3ª Entrega

__Escopo da 3ª Entrega__

- Fato Gerador Não Realizado item \(item 19\.3\-A\.1\.7, da IN 096/20\)
- Situação de emissão de Nota Fiscal para estabelecimento que realizou retenção \(item 19\.3\-A\.1\.10, da IN 096/20\)
- Situação de operação de saída de mercadoria a destinatário do RS que não seja consumidor final \(item 19\.3\-A\.1\.13, da IN 096/20\)

Operações contempladas:

- 772Furto ou Roubo \- baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)
- 773Perda, extravio ou Deterioração – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)
- 774Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)
- 775Furto ou Roubo \- baixa sem Ressarcimento
- 776Perda, extravio ou Deterioração – baixa sem Ressarcimento
- 777Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa sem Ressarcimento
- 779Saída para Outra UF \(RICMS, Livro III, art\.24\) \(e Devoluções\)
- 784Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.24\-A\) \(e Devoluções\)
- 785Saída com ST não destinada a consumidor final deste Estado, ao abrigo de exclusão de responsabilidade \(RICMS, Livro III, art\. 11\) \(e Devoluções\)

08/02/2021

__MFS63471__

Liliane Videira Assaf

A regra que hoje determina se há ressarcimento ou complemento, compara a Base de Cálculo da Entrada com a da Saída\.

Esta regra está sendo alterada para que a comparação seja feita com os valores de Entrada \(ICMS \+ ICMS\-ST\) e Saída \(ICMS\), em substituição ao uso das bases\.

Campos impactados: 31 \- COD\_MOTIVO\_SAI, 43 \- VLR\_UNIT\_ICMSS\_REST\_SAI, 44 \- VLR\_UNIT\_FCP\_REST\_SAI, 45 \- VLR\_UNIT\_ICMSS\_COMPL\_SAI, 46 \- VLR\_UNIT\_FCP\_COMPL\_SAI,

13/04/2021

__MFS65137__

Liliane Videira Assaf

Retirada dos parâmetros da tela de geração, pois foram para a Tela de Dados Iniciais:

\- Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)

\- Tratamento p/ Entrada objeto da Devolução de períodos anteriores à adoção da sistemática da IN\-RE 087/20:

Valores Unitários Médios recuperados:

\( \) do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)

\( \) da própria Nota de Entrada referenciada pela Devolução

Dt anterior à adoção IN\-RE087/20: \[31/12/2020\]

13/05/2021

__MFS61955__

Liliane Videira Assaf

5ª Entrega

Inclusão das Devoluções de Saídas com referência para Cupom Fiscal\.

19/05/2021

__MFS66171__

Liliane Videira Assaf

Hoje a Geração da Média Ponderada calcula o campo “Valor Médio Unitário do ICMS\-ST” sem FECEP\. 

O Cálculo está sendo alterado para fornecer o Valor médio de ICMS\-ST com e sem FECEP, através dos campos: 

\- “Valor Médio Unitário ICMS\-ST __c/__ FECEP”\. 

\- “Valor Médio Unitário ICMS\-ST __s/__ FECEP”\.

A nota de Devolução de saída deve recuperar o Médio de ICMS\-ST com FECEP para demonstrar no C181 \- 14 \- VLR\_UNIT\_ICMSS\_ESTQ\_SAI\.  Além disso, recuperar o Médio de ICMS\-ST sem FECEP para preencher o campo VLR\_UNIT\_ICMS\_ST\_DEV\_SAI\_MP\.

07/06/2021

__MFS66473__

Liliane Videira Assaf

Inclusão do tratamento para saída de produtos farmacêuticos baseados nos artigos 103 e 104 do LIVRO III do RICMS\.  Segundo esses artigos, a substituição tributária não se aplica a produtos farmacêuticos destinados a distribuidores, logo as saídas oriundas desses distribuidores não têm direito a ressarcimento ST, logo essas notas de saída não devem sair no C185, por consequente suas devoluções também não saem no C181\.

Cliente Santa Cruz encaminhou os CFOPs das notas de saída que devem entrar nesse tratamento: __5405 e 5910__\.

21/06/2021

__MFS64191__

Liliane Videira Assaf

IN\-RE 037/21:

Desconsiderar o código da operação 780 na geração dos movimentos de devolução de saída\. Esse código passa a ser considerado na geração da Devolução da Entrada\. 

- 780 \- Devolução para fornecedor de outra UF, quando a retenção inicial foi realizada pelo próprio remetente da devolução, nos moldes do RICMS, Livro III, art\. 53\-A \(RICMS, Livro III, art\. 25\)

15/07/2021

__MFS67809__

Aline Melo

Criação de tela de parametrização de produtos farmacêuticos, que permita ao usuário informar os códigos de produtos que não devem ser considerados para a geração de devolução de saídas de nota fiscal \(registro C185\)\.

27/07/2021

__MFS69784__

Aline Melo

Ajuste na regra de geração do registro C181, na devolução de saída por cupom fiscal, quando emitidas por distribuidora farmacêutica\.

30/07/2021

__MFS72429__

Andréa Rocha

Inclusão do arredondamento dos valores calculados, ou seja, os valores calculados não serão mais truncados\.  Conforme informação passada pela SEFAZ/RS\.

04/10/2021

__MFS77274__

Liliane Videira Assaf

Alteração no Tratamento para Notas de Produtos Farmacêuticos emitidas por Distribuidores criada pela MFS66473 para retirar os CFOPs 5405 e 5910 da regra\. 

Além disso, hoje o tratamento é aplicado às notas e aos cupons fiscais referenciados pela devolução\. Com esta alteração, o tratamento passa a ser aplicado direto na nota de devolução\.

10/12/2021

__MFS84243__

Andréa Rocha

Inclusão da verificação da data fiscal da nota fiscal para recuperar a parametrização por Produto/NCM/CEST\.

12/04/2022

__MFS90131__

Liliane Assaf

Chamado Lasa/Magalu: Tratamento na diferença de 0,000001 do valor médio unitário do último dia do mês para o do primeiro dia do mês seguinte\. 

01/08/2022

__MFS89648__

Liliane Assaf

Atualização legal IN55/22:

 Tratamento para Valor Médio Ponderado Móvel calculado ao final do dia negativo \(19\.3\-A\.2\.2\.2 da IN\-045/98\) 

Quando o Valor Médio Ponderado Móvel for negativo, os Movimentos de Devolução de Saídas Internas p/ Consumidor Final \(Cod\. Operação 770\) sofrerão as seguintes alterações:

- Valor Unitário do ICMS calculado através da multiplicação da Alíquota Interna pelo Valor Médio Ponderado Móvel \(sem sinal\), será adicionado ao campo 16 \-VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV\_SAIDA dos registros C181;
- Os campos referentes ao ICMS, ICMS\-ST, FECEP das mercadorias em estoque no dia da saída \(13 \- VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV\_SAIDA, 14 \- VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\_SAIDA e 15 \- VL\_UNIT\_FCP\_ICMS\_ST\_ ESTOQUE\_CONV\_SAIDA\) do C181 zerão zerados\.

10/08/2022

__MFS96666__

Liliane Assaf

Atualização legal IN RE 96/22 \(jan\-2023\):

Tópico 19\.3\-A\.1\.12 da IN RE045/98: criação dos códigos RS601, \.\.\., RS656 e RS801, \.\.\., RS856 para as devoluções de saídas internas a consumidor final quando a base de cálculo é reduzida\. Os códigos RS600 ou RS800 passam a ser aplicados apenas quando a base de cálculo for integral\.

Atualização Legal Sped Fiscal \(jan 2023\):

Os códigos de motivos RS5xx: passam a preencher os campos 13,14 e 15 do C181\.

07/12/2022

__MFS543860__

Andréa Rocha

Tratamento do parâmetro para definir se o valor do FECEP está embutido nos valores de ICMS não destacado e não escriturado\.

19/06/2023

Sumário

[1\.	Introdução	1](#_Toc72506250)

[1\.1	– Operações de Saídas \(e devoluções\) acobertadas pelo Ressarcimento de ST	1](#_Toc72506251)

[2\.	Recuperação dos Dados e Processamento	1](#_Toc72506252)

[2\.0 – Recuperação das Devoluções de Saídas \(norm\_dev = 2 /movto\_e\_s <> 9\)	1](#_Toc72506253)

[2\.1 – Recuperação das Notas Fiscais de Saídas referenciadas pela Devolução \(norm\_dev = 1 /movto\_e\_s = 9\)	1](#_Toc72506254)

[2\.2 – Recuperação dos Cupons Fiscais referenciados pela Devolução	1](#_Toc72506255)

[2\.3 – Recuperação dos Valores Unitários Médios referenciados pela SAÍDA objeto da devolução	1](#_Toc72506256)

[3\.	Gravação dos Dados na Tabela dos Movimentos	1](#_Toc72506257)

[3\.1 – Gravação das Devoluções de Saídas \(referência para Nota Fiscal e Cupom Fiscal\)	1](#_Toc72506258)

[4\.	RELATORIO DE CONFERÊNCIA	1](#_Toc72506259)

# <a id="_Toc72506250"></a>Introdução 

__\[MFS61955\]__

Esse documento tem como objetivo definir a geração das __Devoluções das Saídas__ que consiste em:

- Recuperar as notas fiscais de devolução de saídas do período, com base nas parametrizações de Produto e CFOP/Naturaza da Operação;
- Recuperar as notas de saídas e os cupons fiscais referenciados pelas notas de devolução; Tais documentos podem estar em períodos anteriores ao da geração\.
- Recuperar os valores unitários médios ponderados relacionados ao produto e data da nota de saída e dos cupons\. Tais valores são recuperados da tabela EST\_ST\_RS\_MEDIA\_POND, que armazena as médias ponderadas diárias por produto\.  Caso não seja encontrado, os valores médios serão calculados com base na última nota de recebimento do produto anterior à saída;
- Gravar as notas de devolução e suas respectivas saídas \(por nota ou cupom\) na tabela específica dessa geração \(EST\_ST\_RS\_NF\_DEV\_SAI\);
- Gerar o Relatório de Conferência a partir da tabela EST\_ST\_RS\_NF\_DEV\_SAI, demonstrando o detalhamento do cálculo dos valores que serão apresentados no C181 do Sped Fiscal\.

Esse processamento é base para a geração do registro C181\. Todos os registros gravados na tabela EST\_ST\_RS\_NF\_DEV\_SAI numa próxima etapa serão copiados para a tabela X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV de onde parte a geração do registro C181 no módulo SPED FISCAL\.  Ou seja, as regras que definem o C181 são realizadas nessa fase\.

__Observação__:

Em todas as recuperações dos movimentos \(entrada, saída, devolução de entrada, devolução de saída\) é necessário que a parametrização por Produto \(opções “Por Código”, “Por NCM” ou “Por CEST”\) tenha data de validade vigente no período informado na tela da geração\.

Na geração da Devolução da Saída, são calculados os valores de ICMS apresentados na ocasião da saída\. Para esse cálculo são necessários Alíquota Interna, Alíquota FCP e %Redução BC que são parametrizados por Produto, vigente na data de emissão da Saída\. 

Logo, na geração da Devolução da Saída é necessário que existam parametrizações por Produto \(opções “Por Código”, “Por NCM” ou “Por CEST”\) vigentes no período informado na tela da geração e na data de emissão das notas de saídas \(e cupons fiscais\) devolvidas\.

*Veja orientação no Guia Prático do Sped Fiscal, quanto ao campo 16 do C181: *

*“VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV\_SAIDA Valor unitário para o ICMS na operação, correspondente ao valor do campo VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV, preenchido na ocasião da saída\.”*

- 
	1. <a id="_Toc63787821"></a><a id="_Toc72506251"></a>– <a id="COD_OP_SAIDA"></a>Operações de Saídas \(e devoluções\) acobertadas pelo Ressarcimento de ST__:__

\[__MFS58042/ MFS59698\]__

Lista dos Códigos de Operação considerados para a geração do movimento de Saída e Devolução de Saída\. 

Tais códigos estão disponíveis na parametrização por CFOP e por Natureza de Operação no *menu Parâmetros à \(IN\-RE 087/20\) à Operações\.*

Vale ressaltar que as devoluções se aplicam às operações de saída, EXCETO para a faixa de códigos de operações de 772 a 777\.

Cód Operação

Descrição da Operação \(*menu Parâmetros à \(IN\-RE 087/20\) à Operações\)*

Cód Motivo

Base Legal 

IN 096/20

770

Saída Interna para Consumidor Final \(e Devoluções\)

RS100, RS300, 

RS101, RS301,

…

RS156, RS356,

RS600, RS800

RS601, RS801,

…

RS656, RS856

19\.3\-A\.1\.12 

772

Furto ou Roubo \- baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

RS211

19\.3\-A\.1\.7 

773

Perda, extravio ou Deterioração – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

RS212

19\.3\-A\.1\.7

774

Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

RS215

19\.3\-A\.1\.7

775

Furto ou Roubo \- baixa sem Ressarcimento 

RS011

19\.3\-A\.1\.7

776

Perda, extravio ou Deterioração – baixa sem Ressarcimento 

RS012

19\.3\-A\.1\.7

777

Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa sem Ressarcimento 

RS015

19\.3\-A\.1\.7

778

Saída para outra UF \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)

RS213, RS713

19\.3\-A\.1\.9 

779

Saída para outra UF \(RICMS, Livro III, art\.24\) \(e Devoluções\)

RS001, RS501

19\.3\-A\.1\.10 

780

__MFS64191__

Devolução para fornecedor de outra UF, quando a retenção inicial foi realizada pelo próprio remetente da devolução, nos moldes do RICMS, Livro III, art\. 53\-A \(RICMS, Livro III, art\. 25\)

RS213, RS713

19\.3\-A\.1\.9 

781

Saída para Exportação \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)

RS214, RS714

19\.3\-A\.1\.9 

782

Saída Interna com nova ST \(RICMS, Livro III, art\.23, III\) \(e Devoluções\)

RS217, RS717

19\.3\-A\.1\.9 

783

Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.23, V\) \(e Devoluções\)

RS219, RS719

19\.3\-A\.1\.9 

784

Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.24\-A\) \(e Devoluções\)

RS001, RS501

19\.3\-A\.1\.10 

785

Saída com ST não destinada a consumidor final deste Estado, ao abrigo de exclusão de responsabilidade \(RICMS, Livro III, art\. 11\) \(e Devoluções\)

RS000, RS500

19\.3\-A\.1\.13 

Nos tópicos de 19\.3\-A\.1\.7 a 19\.3\-A\.1\.13 da IN\-RE 096/20, são definidos os tratamentos e os códigos de motivo a serem aplicados a cada uma das operações\. Esses tratamentos estão descritos no item 3 desse documento\.

__Nota__: A parametrização dos Produtos Associados se aplica apenas na geração da IN048/18\. Não se aplica a IN087/20\!

# <a id="_Toc350763252"></a><a id="_Toc72506252"></a>Recuperação dos Dados e Processamento

__Visão resumida do Processamento__

A Geração dos Movimentos de Devolução de Saídas deve ser executada dia por dia, em __ordem cronológica__\.

Para cada __dia__ do mês da geração, executar:

 1º: Geração os Movimentos de Devolução das Saídas do dia;

 2º: Cálculo da Média Ponderada Móvel dos Valores Unitários do dia\.

__Geração os Movimentos de Devolução das Saídas do dia:__

Ver definições de recuperação do movimento e gravação na tabela EST\_ST\_RS\_NF\_DEV\_SAF nos topicos a seguir\.

__Cálculo da Média Ponderada Móvel dos Valores Unitários do dia__:

 Veja documento “*MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Cálculo Média Ponderada\.docx*”

As devoluções de Saídas estão associadas a duas origens:

1. Devolução de Saída, cuja saída é uma __nota fiscal__: 

A nota de Devolução é uma nota de entrada, carregada nas SAFX07/SAFX08\. 

A nota de saída devolvida também está carregada na SAFX07/SAFX08\. 

A associação da nota de devolução com a nota de saída pode ser feita de duas formas:

1\.1\) Utilizando os campos de referência da __SAFX08__:

  Neste caso, no item da nota de devolução, os campos 117, 118, 119, 102 \(SAFX08\) são preenchidos com os dados de identificação da nota fiscal de saída;

1\.2\) Utilizando a tabela de referência __SAFX192__:

 Neste caso, a SAFX192 é carregada da seguinte forma: do campo 01 ao 15 são os dados de identificação do item da nota de devolução, campo 16 preenchido com “1 \- Devolução \(Entrada\) x Documentos de Origem \(Saídas\)” e do campo 17 ao 23 são os dados de identificação do item da nota de saída devolvida\.

 O campo 24 é a quantidade devolvida da nota de saída\. Vale observar que essa pode ser igual ou inferior a registrada no item da nota de saída\.

__\[MFS61955\]__

1. Devolução de Saída cuja saída é um __cupom fiscal__:

A nota de Devolução é uma nota de entrada, carregada nas SAFX07/SAFX08\.

O cupom fiscal é carregado nas SAFX993/SAFX994\.

A associação da nota de devolução com o cupom se dá através da __SAFX192__, que deve ser carregada da seguinte forma: do campo 01 ao 15 são os dados de identificação do item da nota de devolução, campo 16 – Tipo de Referência preenchido com “4 \- Devolução \(Entrada\) x Documento de Origem \(Cupom Fiscal Saída\)” e os campos 23, 27, 28, 29, 30 são os dados de identificação do item do cupom fiscal devolvido\.

 O campo 24 é a quantidade devolvida do item do cupom fiscal, que pode ser igual ou inferior à registrada no item do cupom fiscal de saída\.

Obs: não utilizamos a SAFX117 pois ela não identifica o item do cupom só a capa\.

Todas essas formas de devolução são consideradas no processamento e armazenadas na tabela EST\_ST\_RS\_NF\_DEV\_SAI\.

## <a id="_2.0_–_Recuperação"></a><a id="_Toc72506253"></a>2\.0 – Recuperação das Devoluções de Saídas \(norm\_dev = 2 /movto\_e\_s <> 9\)

__Origem dos dados__: \- Parametrização de Produtos \(por Código, por NCM e por CEST\);

                                  \- Parametrização de CFOP / Natureza de Operação;

                                  \- SAFX07 / SAFX08 – Tabelas dos Documentos Fiscais \(DATAMART\)

__Critérios da recuperação das Notas Fiscais de Devolução: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data Fiscal – data enquadrada no período informado em tela;

\- Nota fiscal de devolução \(NORM\_DEV = “2”\);

\- Nota de entrada \(MOVTO\_E\_S <> “9”\);

\- Modelo = 01, 1B, 04, 55, 65 

\- Somente notas *não canceladas*;

\- Somente notas *com itens*;

__\[MFS84243\] __Inclusão da verificação da data fiscal da nota fiscal para recuperar a parametrização por Produto/NCM/CEST\.

\- O produto do item deve constar na parametrização do menu “*Parâmetros à Produtos à Por Código*”, __ou__, seu NCM deve estar parametrizado no menu “*Parâmetros à Produtos à Por NCM*”, __ou__, seu CEST deve estar parametrizado no menu “*Parâmetros à Produtos à Por CEST*”\. 

  Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\.  Somente devem ser considerados os produtos em que a data fiscal da nota fiscal esteja compreendida entre a data inicial de vigência e a data final de vingência da parametrização\.  Quando a data final de vigência não estiver preenchida, a parametrização ainda está válida, ou seja, o produto será considerado\.

   No caso da parametrização dos produtos, primeiro é verificado se o produto consta na parametrização da opção “Por Código”\. Ao verificar a parametrização por código, deve\-se considerar também os produtos associados\. Ou seja, o produto da nota deve constar como o produto “principal” da parametrização \(__ESP\_SP\_PROD\_ST__\), ou ser um produto “associado” ao produto principal \(__ESP\_SP\_PROD\_ST\_ASS__\)\.  Módulos de ressarcimento de SC e SP trabalham com produto associado\.

   Os produtos “associados” são produtos cuja movimentação será demonstrada na Ficha 3 em nome do produto principal parametrizado\. 

  A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

 

        \-Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada\.

        \-Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “Por NCM”\.

        \-Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada\.

        \-Caso não, é verificado se o CEST do produto \(CEST do cadastro do produto\) consta na parametrização da opção “Por CEST”\.

 \- O CFOP ou CFOP/Natureza do item deve constar na parametrização do menu “*Parâmetros à \(IN\-RE 087/20\) à Operações*” para a seguinte operação:

\[__MFS58042/ MFS59698\]__

Cód Operação

Descrição da Operação \(*menu Parâmetros à \(IN\-RE 087/20\) à Operações\)*

770

Saída Interna para Consumidor Final \(e Devoluções\)

778

Saída para Outra UF \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)

779

Saída para Outra UF \(RICMS, Livro III, art\.24\) \(e Devoluções\)

780

__MFS64191__

Devolução para fornecedor de outra UF, quando a retenção inicial foi realizada pelo próprio remetente da devolução, nos moldes do RICMS, Livro III, art\. 53\-A \(RICMS, Livro III, art\. 25\)

781

Saída para Exportação \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)

782

Saída Interna com nova ST \(RICMS, Livro III, art\.23, III\) \(e Devoluções\)

783

Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.23, V\) \(e Devoluções\)

784

Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.24\-A\) \(e Devoluções\)

785

Saída com ST não destinada a consumidor final deste Estado, ao abrigo de exclusão de responsabilidade \(RICMS, Livro III, art\. 11\) \(e Devoluções\)

        Obs: As devoluções não se aplicam aos códigos de operações de 772 a 777\.

Recuperar as seguintes informações da nota de devolução \(SAFX07/SAFX08\):

\- Campos de Identificação da Capa e do Item da nota de devolução;

\- 13,14 \- Produto – GRUPO\_PRODUTO, IND\_PRODUTO, COD\_PRODUTO \(SAFX08\)

\- Unidade de Medida do Produto \(SAFX2013\)

__\- Caso o produto do item da nota de devolução tenha sido parametrizado por Código \(menu “Parâmetros à Produtos à Por Código”\) recuperar o Produto Principal \(grupo, indicador e código\) e a Unidade de Medida do Produto Principal \(SAFX2013 – campo 14 – COD\_MEDIDA\)\.__

\- 24 \- Quantidade \- QUANTIDADE \(SAFX08\)

\-137\-Quantidade Convertida \(SAFX08\)

\- 25 \- Unidade de Medida \- COD\_MEDIDA \(SAFX08\)

__MFS66473/MFS67809/ MFS77274__

__Tratamento para Notas de Produtos Farmacêuticos emitidas por Distribuidores:__

Esse tratamento serve ser aplicado à nota de devolução\.

Verificar os critérios a seguir:

- Estabelecimento é um __Distribuidor__ \(atacadista\), ou seja, na Tela de Dados Iniciais estiver com o campo “Contribuinte Varejista?” = Não;
- __Produto__ do Item da Nota de Devolução estiver cadastrado, na tela de Parametrização de Produtos Farmacêuticos por Código, no menu: Parametros >  \(IN\-RE 087/20\) > Produtos Farmacêuticos > Código\.

Se os dois critérios forem atendidos, então:

            O item de mercadoria dessa nota de devolução não será gravado na tabela EST\_ST\_RS\_NF\_DEV\_SAI, e a seguinte mensagem será exibida no log:

“*Registro C181: Devolução de saída do produto farmacêutico amparado pelo art 103/104 do Livro III do RICMS não será gerada no C181”\.*

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Saída exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

Obsevação importante: as notas de devolução de produtos farmaceuticos não possuem referências para nota de saída nem para cupom\. Por isso este tratamento deve ser aplicado antes da verificação se a devolução possui referência para nota/cupom de saída\. Caso contrário cairá na mensagem *Registro C181: Nota de Devolução de saída não considerada na geração, pois não existe referência para operação de saída original* indevidamente\.  

__\[MFS61955\]__

Para cada item de mercadoria da nota de devolução vamos recuperar a\(s\) nota\(s\) de saída\(s\) devolvida\(s\) ou cupons fiscais devolvidos\.

Primeiro buscar a saída a partir dos campos de referência da __SAFX08 __\(117, 118, 119, 102\)\. Caso esses campos não estejam preenchidos, buscar as saídas \(por notas ou cupons fiscais\) referenciadas a partir da __SAFX192__, considerando campo “16\-Tipo de Referência” da SAFX192 = “__1__” \(para nota fiscais\) e “4” \(para cupom fiscal\)\. 

Se o item de mercadoria da nota de devolução não tiver nenhuma das referências para nota/cupom de saída preenchidas, exibir a seguinte mensagem no log e não gravar a nota de devolução na tabela EST\_ST\_RS\_NF\_DEV\_SAI:

*         “Registro C181: Nota de Devolução de saída não considerada na geração, pois não existe referência para operação de saída original\.*

*          Favor informar as saídas devolvidas na SAFX192 ou utilizar os campos de referência da SAFX08 \(117, 118, 119, 102\)\.”*

                                \(o log deve exibir a identificação do item da devolução para conferência do usuário\)

## <a id="_2.1_–_Recuperação"></a><a id="_Toc72506254"></a>2\.1 – Recuperação das Notas Fiscais de Saídas referenciadas pela Devolução \(norm\_dev = 1 /movto\_e\_s = 9\)

Para cada item de mercadoria da nota de devolução recuperada conforme tópico [2\.0](#_2.0_–_Recuperação), vamos recuperar as notas de saída devolvidas, referenciadas pela nota de devolução\. Esta referência pode ser de duas maneiras:

1. A nota de saída devolvida está identificada através dos campos de referência da __SAFX08 __\(117, 118, 119, 102\) do item da nota de devolução;
2. As notas de saídas devolvidas estão identificadas através da SAFX192 associado ao item da nota de devolução, considerando campo “16\-Tipo de Referência” da SAFX192 = “__1__”\.

Abaixo estão definidas as duas formas de recuperar as notas de saída\.

__Recuperação das saídas referenciadas pela SAFX08:__

Caso o item de mercadoria da nota de devolução possua os campos 117, 118, 119, 102 \(SAFX08\) preenchidos, recuperar o documento de referência \(nota de saída devolvida\), a partir dos critérios descritos abaixo: 

\- Empresa                  = Código da empresa da nota de devolução

\- Estabelecimento      = Código do estabelecimento da nota de devolução

\- Movimento E/S        = deve ser uma nota de saída \(MOVTO\_E\_S = “9”\) 

\- Normal/Devolução   = deve ser uma nota normal \(NORM\_DEV = ‘1’\)

\- Pessoa Fis/Jur         = mesma pessoa fis/jur da nota de devolução

\- Número                    = campo “117\-Número do Documento Fiscal de Referência” do item da nota de devolução

\- Série                         = campo “118\-Série do Documento Fiscal de Referência “do item da nota de devolução

\- Subsérie                  = campo “119\-Subsérie do Documento Fiscal de Referência“ do item da nota de devolução

\- Data de Emissão     = campo “102\-Data DI / Data Doc Refer” do item da nota de devolução

\- Produto                    = produto do item da nota de devolução \(grupo,indicador e código\); 

Recuperar as seguintes informações da nota de saída referenciada \(SAFX07/SAFX08\):

\- Campos de Identificação da Capa e do Item da nota de saída referenciada;

\- 11 \- Data da Emissão \- DATA\_EMISSAO \(SAFX07\)

\- 13,14 \- Produto – GRUPO\_PRODUTO, IND\_PRODUTO, COD\_PRODUTO \(SAFX08\)

\- Unidade de Medida do Produto \(SAFX2013\)

\- 24 \- Quantidade \- QUANTIDADE \(SAFX08\)

\-137\-Quantidade Convertida \(SAFX08\)

\- 25 \- Unidade de Medida \- COD\_MEDIDA \(SAFX08\)

\- 64 \- Valor Contábil do Item \- VLR\_CONTAB\_ITEM \(SAFX08\) 

O parâmetro “__*Utilizar DATA MART para períodos anteriores*__” determinará se a nota fiscal de saída será recuperada das Tabelas Normais \(X07/X08\), ou das Tabelas DATAMART \(dwt\)\. Caso o parâmetro esteja selecionado, as tabelas DATAMART serão consideradas, caso contrário utilizar as tabelas Normais \(X07/X08\)\.

__OBS__: O uso dos campos de referência da SAFX08 da nota de devolução para identificar a nota de saída, espera\-se que apenas um item da nota de saída seja recuperado\. Mas, caso seja encontrado mais de um item da nota de saída para o produto devolvido, todos serão gravados na tabela EST\_ST\_RS\_NF\_DEV\_SAI\.  

O correto é utilizar os campos de referência da SAFX08 da nota de devolução quando apenas um item da nota de saída está relacionado ao produto devolvido\. Caso mais de um item de saída esteja relacionado ao produto devolvido, deve\-se utilizar a SAFX192\.

Crítica a ser realizada:

Caso a nota de referência não seja encontrada na base de dados, será gravada a seguinte mensagem no log: 

   “*Registro C181: Nota de Devolução de saída não considerada na geração, pois a nota de saída original referenciada no item da nota não foi encontrada na base de dados\.”*\. 

   \(o log deve exibir a identificação do item da devolução para conferência do usuário \+ campos 117, 118, 119, 102 que identifica a nota de saída referenciada\)

__Recuperação das saídas referenciadas na SAFX192:__

O item de mercadoria da nota de devolução pode ter um ou mais registros na SAFX192 com tipo de 16\-Tipo de Referência” = ‘1’ \- Devolução \(Entrada\) x Documentos de Origem \(Saídas\)\. Recuperar o\(s\) documento\(s\) de referência \(notas de saídas devolvidas\), a partir dos critérios descritos abaixo: 

SAFX192:

\- Campos 1 ao 15 da SAFX192 identificam o item da nota de devolução em questão;

\- Campo “16\-Tipo de Referência” da SAFX192 = “__1__”;

\- Campos 17 ao 23 identificam o item da nota de saída referenciado;

SAFX08:

Para cada documento de referência recuperado da SAFX192 \(identificado pelos campos 17 ao 23\), consultar a SAFX08 dos critérios descritos abaixo: 

\- Empresa                  = Código da empresa da nota de devolução \(campo 01 da SAFX192\)

\- Estabelecimento      = Código do estabelecimento da nota de devolução \(campo 02 da SAFX192\)

\- Movimento E/S        = deve ser uma nota de saída \(MOVTO\_E\_S = “9”\) 

\- Normal/Devolução   = deve ser uma nota normal \(NORM\_DEV = ‘1’\)

\- Pessoa Fis/Jur         = campos 21 e 22 \- Pessoa Física/Jurídica do Documento Fiscal de Referência\(SAFX192\)

\- Número                    = campo 17 \- Número do Documento Fiscal de Referência \(SAFX192\)

\- Série                         = campo 18 \- Série do Documento Fiscal de Referência \(SAFX192\)

\- Subsérie                  = campo 19\-Subsérie do Documento Fiscal de Referência \(SAFX192\)

\- Data Fiscal              = campo 20\- Data da Escrita Fiscal do Documento de Referência \(SAFX192\)

\- Num\. Item               = campo 23 \- Item da Nota Fiscal de Referência \(SAFX192\);

Recuperar as seguintes informações da nota de saída referenciada \(SAFX07/SAFX08\):

\- 11 \- Data da Emissão \- DATA\_EMISSAO \(SAFX07\)

\- 13,14 \- Produto – GRUPO\_PRODUTO, IND\_PRODUTO, COD\_PRODUTO \(SAFX08\)

\- Unidade de Medida do Produto \(SAFX2013\)

\- 24 \- Quantidade \- QUANTIDADE \(SAFX08\)

\-137\- Quantidade Convertida \(SAFX08\)

\- 25 \- Unidade de Medida \- COD\_MEDIDA \(SAFX08\)

\- 64 \- Valor Contábil do Item \- VLR\_CONTAB\_ITEM \(SAFX08\) 

Recuperar quantidade devolvida da SAFX192:

\- 24 \- Quantidade da Devolução

O parâmetro “__*Utilizar DATA MART para períodos anteriores*__” determinará se a nota fiscal de saída será recuperada das Tabelas Normais \(X07/X08\), ou das Tabelas DATAMART \(dwt\)\. Caso o parâmetro esteja selecionado, as tabelas DATAMART serão consideradas, caso contrário utilizar as tabelas Normais \(X07/X08\)\.

Obs\.: 

\- A tabela permite mais de uma nota de referência para um único item da nota de devolução\. Todos todos os itens devem ser gravados na tabela EST\_ST\_RS\_NF\_DEV\_SAI\. 

\-  A Quantidade da Devolução está expressa na mesma unidade de medida da nota de saída \(25 \- Unidade de Medida \- COD\_MEDIDA \(SAFX08\)\. Ou seja se eu vendi em litros, devolvo em litros\.

__MFS66473/MFS67809 MFS77274 \- tratamento transferido para nota de devolução__

__Tratamento para Notas de Produtos Farmacêuticos emitidas por Distribuidores:__

Esse tratamento serve tanto para saída referenciada pela SAFX08 quanto pela SAFX192\.

Verificar os critérios a seguir:

- Estabelecimento é um __Distribuidor__ \(atacadista\), ou seja, na Tela de Dados Iniciais estiver com o campo “Contribuinte Varejista?” = Não;
- __CFOP__ do Item da Nota de Saída referenciada for __5405 ou 5910;__
- __Produto__ do Item da Nota de Saída estiver cadastrado, na tela de Parametrização de Produtos Farmacêuticos por Código, no menu: Parametros >  \(IN\-RE 087/20\) > Produtos Farmacêuticos > Código\.

Se os três critérios forem atendidos, então:

            O item de mercadoria dessa nota de saída não será gravado na tabela EST\_ST\_RS\_NF\_DEV\_SAI, e a seguinte mensagem será exibida no log:

“*Registro C181: Devolução da Nota de Saída de produto farmacêutico amparado pelo art 103/104 do Livro III do RICMS não será gerada no C181”\.*

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Saída e da Saída referenciada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

## <a id="_2.2_–_Recuperação"></a><a id="_Toc72506255"></a>2\.2 – Recuperação dos Cupons Fiscais referenciados pela Devolução 

__\[MFS61955\]__

Para cada item de mercadoria da nota de devolução recuperada conforme tópico [2\.0](#_2.0_–_Recuperação), vamos recuperar os cupons fiscais devolvidos, referenciados pela nota de devolução\. Os cupons fiscais devolvidos estão identificados através da SAFX192 associado ao item da nota de devolução, considerando campo “16\-Tipo de Referência” da SAFX192 = “__4__”\.

__Recuperação dos cupons fiscais referenciados na SAFX192:__

O item de mercadoria da nota de devolução pode ter um ou mais registros na SAFX192, com tipo de 16\-Tipo de Referência” = “4” – “Devolução \(Entrada\) x Documento de Origem \(Cupom Fiscal Saída\)”\.

Recuperar o\(s\) documento\(s\) de referência \(cupons fiscais devolvidos\), a partir dos critérios descritos abaixo: 

SAFX192:

    \- Campos 1 ao 15 da SAFX192 identificam o item da nota de devolução em questão;

    \- Campo “16\-Tipo de Referência” da SAFX192 = “4”;

Recuperar os campos 23, 27, 28, 29 e 30 identificam o item do cupom fiscal de saída referenciado\.

SAFX994:

Para cada documento de referência recuperado da SAFX192 \(identificado pelos campos 23, 27, 28, 29 e 30\), consultar a SAFX994 dos critérios descritos abaixo: 

    \- Código da Empresa \(campo 01 SAFX994\) = Código da empresa da nota de devolução;

    \- Código do Estabelecimento \(campo 02 SAFX994\) = Código do estabelecimento da nota de devolução;

    \- Modelo Documento \(campo 03 SAFX994\) = campo 27 \- Modelo do Cupom Fiscal de Referência da SAFX192;

    \- Número do Caixa \(campo 04 SAFX994\) = campo 28 \- Número do Caixa do Cupom Fiscal de Referência da SAFX192;

    \- COO \(campo 05 SAFX994\) = campo 29 \- COO \(Contador de Ordem de Operação\) do Cupom Fiscal de Referência da SAFX192;

    \- Data da emissão \(campo 06 SAFX994\) = campo 30 \- Data de Emissão do Cupom Fiscal de Referência da SAFX192;

    \- Número do item \(campo 07 SAFX994\) = campo 23 \- Item da Nota Fiscal de Referência \(SAFX192\);

Recuperar as seguintes informações do cupom fiscal referenciado \(SAFX994\):

\- 06 \- Data da Emissão \(SAFX994\);

\- 08,09 \- Produto – GRUPO\_PRODUTO, IND\_PRODUTO, COD\_PRODUTO \(SAFX994\);

\- Unidade de Medida do Produto \(SAFX2013\);

\- 16 \- Quantidade \- QTDE \(SAFX994\);

\- 17 \- Unidade de Medida \- COD\_MEDIDA \(SAFX994\);

\- 22 \- Valor total líquido \- VLR\_LIQ\_ITEM \(SAFX994\); 

Recuperar quantidade devolvida da SAFX192:

\- 24 \- Quantidade da Devolução

Obs\.: 

\- A tabela permite mais de um cupom de referência para um único item da nota de devolução\. Todos todos os itens devem ser gravados na tabela EST\_ST\_RS\_NF\_DEV\_SAI\. 

\-  A Quantidade da Devolução está expressa na mesma unidade de medida do cupom de saída \(17 \- Unidade de Medida \- COD\_MEDIDA \(SAFX994\)\)\. Ou seja se eu vendi em litros, devolvo em litros\.

__MFS77274 \- tratamento transferido para nota de devolução__

__Tratamento para Notas de Produtos Farmacêuticos emitidas por Distribuidores:__

__MFS69784 – Solução definitiva para devolução de saída por Cupom Fiscal \(inclui o tratamento definido na MFS66473 e na MFS67809\)__

Verificar os seguintes critérios:

- Estabelecimento é um __Distribuidor__ \(atacadista\), ou seja, na Tela de Dados Iniciais estiver com o campo “Contribuinte Varejista?” = Não;
- <a id="_Hlk78537649"></a>__CFOP__ do Item do Cupom Fiscal referenciado for __5405 ou 5910;__
- __Produto__ do Item do Cupom Fiscal estiver cadastrado, na tela de Parametrização de Produtos Farmacêuticos por Código, no menu: Parametros >  \(IN\-RE 087/20\) > Produtos Farmacêuticos > Código\.

Se os três critérios forem atendidos, então:

            O item do Cupom Fiscal não será gravado na tabela EST\_ST\_RS\_NF\_DEV\_SAI, e a seguinte mensagem será exibida no log:

“*Registro C181: Devolução do Cupom Fiscal de produto farmacêutico amparado pelo art 103/104 do Livro III do RICMS não será gerada no C181”\.*

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Saída e do Cupom referenciado\. Para nota exibir o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item\. Para o cupom informar Número do Caixa \(campo 04 SAFX994\), Modelo \(campo 03 SAFX994\), COO \(campo 05 SAFX994\), Data da emissão \(campo 06 SAFX994\), Número do Item \(campo 07 SAFX994\)\.

## <a id="_2.3_–_Recuperação"></a><a id="_Toc72506256"></a>2\.3 – Recuperação dos Valores Unitários Médios referenciados pela SAÍDA objeto da devolução

Segundo a IN\-RE 087/20, Tópico 19\.3\-A\.2\.2, alínea “b” os valores unitários médios a serem considerados para as devoluções, são os calculados para o dia da saída objeto da devolução\. Veja: 

*”b\) acrescentar ao valor apurado na alínea "a" as informações referentes a todas as devoluções de saídas da mercadoria e retornos de mercadorias não entregues, de que trata a alínea "c" do subitem 19\.3\-A\.1, ocorridos durante o dia, que corresponderá à soma das multiplicações da quantidade de mercadorias de cada devolução e retorno pelo valor unitário médio móvel calculado ao fim do dia em que ocorreu a saída objeto de devolução ou retorno;”*

Segundo a IN\-RE 087/20, Tópico 19\.3\-A\.1\.5\.1, se a saída objeto da devolução ocorrer antes de 1º de janeiro de 2021, utiliza\-se a última nota de recebimento da mercadoria anterior a saída\. Veja:

*"19\.3\-A\.1\.5\.1 \- Se a venda objeto de devolução ou retorno ocorreu antes de 1º de janeiro de 2021, para o preenchimento dos campos:*

*a\) VL\_UNIT\_CONV\_SAIDA, deverá ser utilizado o valor unitário da mercadoria constante no documento fiscal da saída objeto da devolução ou retorno;*

*b\) VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV\_SAIDA, deverá ser utilizado o valor unitário do ICMS que o contribuinte teria se creditado referente ao último recebimento da mercadoria pelo estabelecimento, antes da saída objeto da devolução ou retorno, caso a mercadoria estivesse submetida ao regime normal de tributação;*

*c\) VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\_SAIDA, deverá ser utilizado o valor unitário do ICMS\-ST constante no documento fiscal do último recebimento da mercadoria pelo estabelecimento antes da saída objeto da devolução ou retorno;*

*d\) VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV\_SAIDA, deverá ser utilizado o montante do imposto efetivo informado no campo VL\_AJ\_APUR, conforme subitem 19\.2\.2, "a", ou 19\.3\.1, "a", conforme o caso\.”*

Sendo assim vamos realizar o seguinte procedimento para busca dos Valores Unitários Médios:

__Passo 1__: Consultar a Tabela de “Cálculo da Média Pondera Móvel dos Valores Unitários” \(__EST\_ST\_RS\_MEDIA\_POND__\) com os seguintes critérios:

\- Empresa login;

\- Estabelecimento selecionado na tela de geração;

\- Data = Data de Emissão da Nota fiscal de Saída \(SAFX07\) objeto da Devolução \(vide [2\.1](#_2.1_–_Recuperação)\); ou

              Data de Emissão do Cupom Fiscal \(SAFX993\), objeto da Devolução \(vide [2\.2](#_2.2_–_Recuperação)\);

\- Produto = Produto do item da Nota de Devolução da Saída \(vide [2\.0](#_2.0_–_Recuperação)\);

                   __Caso o produto do item tenha sido parametrizado por Código __

__                  \(menu “Parâmetros à Produtos à Por Código”\) considerar o Produto Principal \(grupo, indicador e código\)__\.

*\(ver OBS sobre os produtos associados, pois os valores medios estariam no produto principal\)*

Recuperar os Valores Médios:

\- Valor Médio Unitário do ICMS \(VLR\_UNIT\_ICMS\_FIM\_MP\);

\- Valor Médio Unitário do ICMS\-ST s/ FECEP \(VLR\_UNIT\_ICMS\_ST\_FIM\_MP\); __\[MFS66171\]__

\- Valor Médio Unitário do ICMS\-ST c/ FECEP \(VLR\_UNIT\_ICMS\_ST\_FECEP\_FIM\_MP\); __\[MFS66171\]__

\- Valor Médio Unitário da Base de Cálculo do ICMS\-ST \(VLR\_UNIT\_BC\_ST\_FIM\_MP\);

\- Valor Médio Unitário do FECEP\-ST \(VLR\_UNIT\_FECEP\_ST\_FIM\_MP\);

Caso a consulta acima não retorne registros, então executar o passo 2\.

__Passo 2__: Buscar a __última nota fiscal de entrada da mercadoria__, anterior à saída \(por nota ou cupom\)\. 

Consultar as Tabelas normais de Documento Fiscal \(X07/X08\), com os seguintes critérios:

\- Empresa                  = Código da empresa da Nota fiscal de Saída \(SAFX07\) objeto da Devolução \(vide [2\.1](#_2.1_–_Recuperação)\); ou

                                      Código da empresa do Cupom Fiscal \(SAFX993\), objeto da Devolução \(vide [2\.2](#_2.2_–_Recuperação)\);

\- Estabelecimento      = Código do estabelecimento da Nota fiscal de Saída \(SAFX07\) objeto da Devolução \(vide [2\.1](#_2.1_–_Recuperação)\); ou

                                     Código do Estabelecimento do Cupom Fiscal \(SAFX993\), objeto da Devolução \(vide [2\.2](#_2.2_–_Recuperação)\);

\- Movimento E/S        = deve ser uma nota de entrada \(MOVTO\_E\_S <> “9”\) 

\- Normal/Devolução   = deve ser uma nota normal \(NORM\_DEV = ‘1’\)

\- Somente notas não canceladas;

\- Somente notas com itens;

\- O CFOP ou CFOP/Natureza do item deve estar parametrizado \(menu “Parâmetros à \(IN\-RE 087/20\) à Operações”\) para a operação “Entradas \(e Devoluções\)” \(código parâmetro 771\);

\- Data Fiscal         < Data de Emissão da Nota fiscal de Saída \(SAFX07\) objeto da Devolução \(vide [2\.1](#_2.1_–_Recuperação)\); OU

                             < Data de Emissão do Cupom Fiscal \(SAFX993\), objeto da Devolução \(vide [2\.2](#_2.2_–_Recuperação)\);

\- O produto do item da Entrada deve ser o mesmo produto da Saída em questão, 

  ou

 A parametrização “Por Código” que o produto da Saída pertença, deve conter o produto da Entrada\. Ou seja, os dois produtos devem pertencer a mesma parametrização \(menu “Parâmetros > Produtos > Por Código”\), com __data de validade de acordo com o período informado na tela da geração__, sendo um produto “principal” \(ESP\_SP\_PROD\_ST\), ou um produto “associado” ao produto principal \(ESP\_SP\_PROD\_ST\_ASS\)\.  

Ex:

__Produto principal__: COCA\-COLA PET                 \(unidade de medida do estoque – SAFX2013 = UN\) 

__Produtos associados__: COCA\-COLA PET–1      \(unidade de medida do estoque – SAFX2013 = PAC \(6 unidades\)\)

__Produtos associados__: COCA\-COLA PET–2      \(unidade de medida do estoque – SAFX2013 = PAC12 \(12 unidades\)\)

A saída com o produto associado COCA\-COLA PET–2 e a entrada com produto principal COCA\-COLA PET\. 

Mesmo a nota de saída com produto diferente da nota de entrada, essa nota de entrada é considera, pois os dois produtos estão relacionados numa parametrização de Produto Principal x Produtos Associados\.

 Lembrando que Produto do item da Nota de Devolução da Saída é mesmo da Nota fiscal de Saída \(SAFX08\) objeto da Devolução \(vide [2\.1](#_2.1_–_Recuperação)\) ou item do Cupom Fiscal \(SAFX994\), objeto da Devolução \(vide [2\.2](#_2.2_–_Recuperação)\)\.

\- Dentre todos os documentos fiscais que atendam aos critérios acima, recuperar o documento fiscal de maior a Data Fiscal\.

Recuperar as seguintes informações da nota de entrada \(SAFX07/SAFX08\):

\- Número, Série, Subsérie e Data Fiscal \(SAFX08 campos 08, 09, 10, 03\)

\- Número do Item \(SAFX08 campo 18\)

\- 24 \- Quantidade \(SAFX08\)

\-137\- Quantidade Convertida \(SAFX08\)

\- 25 \- Unidade de Medida \- COD\_MEDIDA \(SAFX08\)

\- 43\-Valor ICMS”\(SAFX08\)

\- 80\-ICMS não Escriturado \(SAFX08\)

\- 225\-Valor ICMS Não Destacado \(SAFX08\)

\- 61\-BASE\_SUB\_TRIB\_ICMS e 52\-VLR\_SUBST\_ICMS \(SAFX08\)

\-144\- VLR\_BASE\_ICMSS\_N\_ESCRIT e 145\- VLR\_ICMSS\_N\_ESCRIT \(SAFX08\)

\- 133\- VLR\_ICMSS\_NDESTAC

\- 106\- VLR\_BASE\_ICMS\_ORIG e 107\- VLR\_TRIB\_ICMS\_ORIG

\- 140\-FECEP ICMS\-ST \(SAFX08\)

O parâmetro “__*Utilizar DATA MART para períodos anteriores*__” determinará se a nota fiscal de entrada será recuperada das Tabelas Normais \(X07/X08\), ou das Tabelas DATAMART \(dwt\)\. Caso o parâmetro esteja selecionado, as tabelas DATAMART serão consideradas, caso contrário utilizar as tabelas Normais \(X07/X08\)\.

__\[MFS61955\]__

Caso a __última nota fiscal de entrada da mercadoria__ NÃO seja recuperada, então:

    Gravar mensagem de erro no log:

*“Registro C181: Não foi possível recuperar o valor unitário médio móvel calculado para o dia da saída objeto de devolução, nem encontrar a última nota de entrada do produto vendido\. A Nota de Devolução de saída será gerada no C181 sem valores unitários de ICMS e ICMS\-ST Estoque Conv e não irá compor Média Pondera Móvel dos Valores Unitários do dia DD/MM/YYYY\.*

DD/MM/YYYY é Data Fiscal da Nota de Devolução da Saída\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Saída e da Saída referenciada, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)\. Caso a saída referenciada pela devolução seja um cupom fiscal \(SAFX994\) \(vide [2\.2](#_2.2_–_Recuperação)\) informar Número do Caixa \(campo 04 SAFX994\), COO \(campo 05 SAFX994\), Data da emissão \(campo 06 SAFX994\)\.

*\(\*\) A decisão de considerar a nota fiscal de entrada de maior Número, foi feita sem embasamento legal, pois a IN096/20 não especifica o tratamento para tal situação\. Foi comentado com o Carrefour em reunião realizada em 08/02/2021, e eles não se opuseram ao critério de desempate adotado\. Também realizei consulta a SEFAZ\-RS, e não obtive resposta esclarecedora, veja email em anexo:*

![](data:image/x-emf;base64,AQAAAGwAAAAAAAAAAQAAAGUAAAA7AAAAAAAAAAAAAAAtBwAApQQAACBFTUYAAAEAJBYAABUAAAACAAAAAAAAAAAAAAAAAAAAgAcAADgEAABYAQAAwgAAAAAAAAAAAAAAAAAAAMA/BQDQ9QIAGAAAAAwAAAAAAAAAGQAAAAwAAAD///8AcgAAAKAQAAAjAAAAAQAAAEIAAAAgAAAAIwAAAAEAAAAgAAAAIAAAAACA/wEAAAAAAAAAAAAAgD8AAAAAAAAAAAAAgD8AAAAAAAAAAP///wAAAAAAbAAAADQAAACgAAAAABAAACAAAAAgAAAAKAAAACAAAAAgAAAAAQAgAAMAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAA/wAA/wAA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4Ojr/ODo6/zg6Ov84Ojr/ODo6/zg6Ov84Ojr/ODo6/zg6Ov84Ojr/ODo6/zg6Ov84Ojr/ODo6/zg6Ov84Ojr/ODo6/zg6Ov84Ojr/ODo6/zg6Ov84Ojr/ODo6/zg6Ov84Ojr/ODo6/zg6Ov84Ojr/AAAAAAAAAAAAAAAAAAAAADg6Ov/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/zg6Ov8AAAAAAAAAAAAAAAAAAAAAODo6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/ODo6/wAAAAAAAAAAAAAAAAAAAAA4Ojr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v84Ojr/AAAAAAAAAAAAAAAAAAAAADg6Ov/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/zg6Ov8AAAAAAAAAAAAAAAAAAAAAODo6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/ODo6/wAAAAAAAAAAAAAAAAAAAAA4Ojr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v84Ojr/AAAAAAAAAAAAAAAAAAAAADg6Ov/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/zg6Ov8AAAAAAAAAAAAAAAAAAAAAODo6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/5mamv+Zmpr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/ODo6/wAAAAAAAAAAAAAAAAAAAAA4Ojr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/+Li4v9pamr/ODo6/zg6Ov9pamr/4uLi//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v84Ojr/AAAAAAAAAAAAAAAAAAAAADg6Ov/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v+lpqb/REZG/1xeXv/W1tb/1tbW/1xeXv9ERkb/paam//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/zg6Ov8AAAAAAAAAAAAAAAAAAAAAODo6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/u7u7/dXZ2/zg6Ov+Njo7/+vr6//r6+v/6+vr/+vr6/42Ojv84Ojr/dXZ2/+7u7v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/ODo6/wAAAAAAAAAAAAAAAAAAAAA4Ojr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/vb6+/0RGRv9QUlL/ysrK//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/8rKyv9QUlL/REZG/72+vv/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v84Ojr/AAAAAAAAAAAAAAAAAAAAADg6Ov/6+vr/+vr6//r6+v/6+vr/7u7u/4GCgv84Ojr/gYKC/+7u7v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/+7u7v+BgoL/ODo6/4GCgv/u7u7/+vr6//r6+v/6+vr/+vr6/zg6Ov8AAAAAAAAAAAAAAAAAAAAAODo6//r6+v/6+vr/+vr6/8rKyv9QUlL/REZG/72+vv/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v+9vr7/REZG/1BSUv/Kysr/+vr6//r6+v/6+vr/ODo6/wAAAAAAAAAAAAAAAAAAAAA4Ojr/+vr6//r6+v+Njo7/ODo6/3V2dv/u7u7/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/u7u7/dXZ2/zg6Ov+Njo7/+vr6//r6+v84Ojr/AAAAAAAAAAAAAAAAAAAAADg6Ov/W1tb/XF5e/0RGRv+lpqb/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/paam/0RGRv9cXl7/1tbW/zg6Ov8AAAAAAAAAAAAAAAAAAAAAODo6/zg6Ov91dnb/4uLi//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/4uLi/2lqav84Ojr/ODo6/wAAAAAAAAAAAAAAAAAAAAA4Ojr/ODo6/zg6Ov84Ojr/ODo6/zg6Ov84Ojr/ODo6/zg6Ov84Ojr/ODo6/zg6Ov84Ojr/ODo6/zg6Ov84Ojr/ODo6/zg6Ov84Ojr/ODo6/zg6Ov84Ojr/ODo6/zg6Ov84Ojr/ODo6/zg6Ov84Ojr/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAADAAAAAAAAAISAAAADAAAAAEAAABSAAAAcAEAAAEAAAAQAAAAAAAAAAAAAAAAAAAAvAIAAAAAAAABAgIiUwB5AHMAdABlAG0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAewIAAKDttT57AgAAAAAAAAAAAACg7bU+ewIAABjMrj57AgAAAAAAAAAAAAAAAHkAcwB0AGUAbQAAAAEAAAAAAAAAAAAHAAAAAAAAAAAAeQBzAHQAZQBtAAAAAAAAAAAAAAAAAAcAAAAAAAAAZT9ag9UmAACL6CvBAAAAAGizsj57AgAAAAAAAAAAAADBC+YAAAAAAP//////////0FdvmLsAAAABAAAAAAAAAAAAAAAAAAAAj6SiVAAAAAAAV2+YuwAAAO1kmlT8fwAAQAAAAAAAAACL6CvB/H8AANBXb5i7AAAA+VZvmLsAAAAgAAAAAAAAANBXb5hkdgAIAAAAACUAAAAMAAAAAQAAACUAAAAMAAAADQAAgCgAAAAMAAAAAQAAAFIAAABwAQAAAQAAAPX///8AAAAAAAAAAAAAAACQAQAAAAAAAABAACJTAGUAZwBvAGUAIABVAEkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABi0b5i7AAAAYZdOw/x/AAAAAAAAAAAAAKDttT57AgAAGMyuPnsCAAAAAAAAAAAAAAAALzR7AgAAUA13Vfx/AACweiU0ewIAANoEAAAAAAAAAAAvNHsCAAAwTi40ewIAAAAAAAAAAAAABwAAAAAAAAAAABAyewIAAIDYG0IAAAAAaLOyPnsCAAAA9voxewIAAAAAAAAAAAAACAAAAAAAAABos7I+ewIAAEAAAAAAAAAAAAAAAAAAAADA8wlYAAAAAAA4LzR7AgAAkV5Ow/x/AABAAAAAAAAAAIvoK8H8fwAAALRvmLsAAABpsm+YuwAAACAAAAAAAAAAALRvmGR2AAgAAAAAJQAAAAwAAAABAAAAVAAAAGQAAAApAAAAIgAAAD4AAAAuAAAAAQAAAFVVj0EmtI9BKQAAACIAAAAEAAAATAAAAAQAAAAAAAAAAAAAAGYAAABCAAAAVAAAAFIARQBTACAABwAAAAYAAAAGAAAAAwAAAFQAAAC4AAAAAAAAAC8AAABlAAAAOwAAAAEAAABVVY9BJrSPQQAAAAAvAAAAEgAAAEwAAAAEAAAAAAAAAAAAAABmAAAAQgAAAHAAAABJAEMATQBTAEwAZQBnAGkAcwBsAGEA5wDjAG8ALgBtAHMAZwADAAAABwAAAAoAAAAGAAAABQAAAAYAAAAHAAAAAwAAAAUAAAADAAAABgAAAAUAAAAGAAAABwAAAAMAAAAJAAAABQAAAAcAAAAlAAAADAAAAA0AAIBGAAAAIAAAABIAAABJAGMAbwBuAE8AbgBsAHkAAAAAAEYAAAA8AAAALgAAAFIARQBTACAASQBDAE0AUwBMAGUAZwBpAHMAbABhAOcA4wBvAC4AbQBzAGcAAAAAAEYAAAAQAAAAAgAAAAAAAABGAAAAEAAAAAQAAAABAQAARgAAACAAAAASAAAASQBjAG8AbgBPAG4AbAB5AAAAAAAOAAAAFAAAAAAAAAAQAAAAFAAAAA==)

# <a id="_Toc72506257"></a>Gravação dos Dados na Tabela dos Movimentos

Os documentos fiscais de Devolução recuperados serão gravados__ item a item__, com todas as referências para as notas / cupons fiscais de saídas devolvidos, conforme definido a seguir\.

## <a id="_Toc72506258"></a>3\.1 – Gravação das Devoluções de Saídas \(referência para Nota Fiscal e Cupom Fiscal\)

__\[MFS61955\]__

Para Devolução de Saída, onde a saída referenciada é uma Nota Fiscal \(vide [2\.1](#_2.1_–_Recuperação)\) e onde a saída é referenciada é um Cupom Fiscal \(vide [2\.2](#_2.2_–_Recuperação)\) realizar a gravação da tabela EST\_ST\_RS\_NF\_DEV\_SAF conforme regra a seguir

__Tabela EST\_ST\_RS\_NF\_DEV\_SAI__

Os campos sinalizados com asterisco compõem a chave da tabela\.

A estrutura da tabela __EST\_ST\_RS\_NF\_DEV\_SAI __é baseada na SAFX308\. Contém todos os campos da SAFX308 e campos a mais usados no relatorio de conferência\.

PK

Item

SAFX308

Campo

Regra de Preenchimento

Campos para relatório

\(\*\)

Código do Estabelecimento

COD\_ESTAB\_GER

Código do estabelecimento SELECIONADO na tela de geração\.

Esse campo foi criado, pois no futuro poderemos ter a geração por Inscrição Estadual Única, e nessa opção o estabelecimento selecionado na tela de geração é o centralizador, e as notas fiscais são dos estabelecimentos centralizador e centralizados\.

Não apresentar

__*Campos do layout da SAFX308 \(Item da nota de devoução com item da nota/cupom de saída objeto da devolução\)*__

\(\*\)

01

Código da Empresa 

COD\_EMPRESA

Código da empresa da nota de Devolução da Saída \(SAFX07\) 

Cod Empresa

\(\*\)

02

Código do Estabelecimento

COD\_ESTAB

Código do estabelecimento da nota de Devolução da Saída \(SAFX07\)

Cod Estab

\(\*\)

03

Data Escrita Fiscal

DATA\_FISCAL

Data fiscal da nota de Devolução da Saída \(SAFX07\) recuperada no tópico [2\.0](#_2.0_–_Recuperação)\.

Dt Fiscal NF Devolução

\(\*\)

04

Movimento Entrada / Saída

MOVTO\_E\_S

Indicador do movimento da nota de Devolução da Saída \(SAFX07\) recuperada no tópico [2\.0](#_2.0_–_Recuperação)\.

E/S NF Devolução

\(\*\)

05

Normal ou Devolução

NORM\_DEV

Indicando de Normal/Devolução da nota de Devolução da Saída \(SAFX07\) recuperada no tópico [2\.0](#_2.0_–_Recuperação)\.

Norm/Dev NF Devolução

\(\*\)

06

Tipo do Documento

COD\_DOCTO 

\(IDENT\_DOCTO\)

Tipo do documento da nota de Devolução da Saída recuperada no tópico [2\.0](#_2.0_–_Recuperação)\.

Cod Docto NF Devolução

\(\*\)

07

08

Pessoa Física/Jurídica

IND\_FIS\_JUR/ COD\_FIS\_JUR

\(IDENT\_FIS\_JUR\)

Pessoa física/jurídica da nota de Devolução da Saída \(SAFX07\) recuperada no tópico [2\.0](#_2.0_–_Recuperação)\.

Ind Fis/Jur NF Devolução

Cod Fis/Jur NF Devolução

\(\*\)

09

Número do Documento Fiscal

NUM\_DOCFIS

Número do documento fiscal da Devolução da Saída recuperada no tópico [2\.0](#_2.0_–_Recuperação)\.

Num Docfis NF Devolução

 \(\*\)

10

Série do Documento Fiscal

SERIE\_DOCFIS

Série do documento fiscal da Devolução da Saída recuperada no tópico [2\.0](#_2.0_–_Recuperação)\.

Serie NF Devolução

 \(\*\)

11

Subsérie do Documento Fiscal

SUB\_SERIE\_DOCFIS

Subsérie do documento fiscal da Devolução da Saída recuperada no tópico [2\.0](#_2.0_–_Recuperação)\.

SubSerie NF Devolução

\(\*\)

12 13 14 15

Identificador do Item

DISCRI\_ITEM

Campo identificador do item de mercadoria da Devolução da Saída 

\(DISCR\_ITEM da X08\_ITENS\_MERC\) recuperada no tópico [2\.0](#_2.0_–_Recuperação)\.

Num Item NF Devolução

\(\*\)

16

Espécie do Documento de Referência da Devolução

ESPECIE\_DOCTO\_DEV

Se a saída referenciada pela devolução for uma Nota Fiscal \(vide [2\.1](#_2.1_–_Recuperação)\), então:

    Preencher com: 1\-Nota Fiscal \(SAFX07/08\)

__\[MFS61955\]__

Se a saída referenciada pela devolução for um Cupom Fiscal \(vide [2\.2](#_2.2_–_Recuperação)\), então:

    Preencher com: 2\-Cupom Fiscal \(SAFX993/994\)

Nota da SAFX308: 

A identificação do documento fiscal de referência, é feita através dos campos 17 ao 30, e dependendo da espécie do documento, devem ser preenchidos, obrigatoriamente, os seguintes campos:  
Se opção = 1, devem ser preenchidos os campos 17 ao 23, e o campo 30;  
Se opção = 2, devem ser preenchidos os campos 24, 25, 26, 27 e 30;  
Se opção = 3, devem ser preenchidos os campos 27, 28, 29 e 30\.  


Não Apresentar

\(\*\) 

17

Número do Documento Fiscal de Referência

NUM\_DOCFIS\_REF

Se a saída referenciada pela devolução for uma Nota Fiscal \(vide [2\.1](#_2.1_–_Recuperação)\), então:

   Preencher com Número da nota fiscal de saída referenciada, cfm tópico [2\.1](#_2.1_–_Recuperação)\.

__\[MFS61955\]__

Se a saída referenciada pela devolução for um Cupom Fiscal \(vide [2\.2](#_2.2_–_Recuperação)\), então:

    Não preencher\.

Num Docfis NF Saída 

\(C181\-08\)

 \(\*\)

18

Série do Documento Fiscal de Referência

SERIE\_DOCFIS\_REF

Se a saída referenciada pela devolução for uma Nota Fiscal \(vide [2\.1](#_2.1_–_Recuperação)\), então:

   Preencher com Série da nota fiscal de saída referenciada, cfm tópico [2\.1](#_2.1_–_Recuperação)\.

__\[MFS61955\]__

Se a saída referenciada pela devolução for um Cupom Fiscal \(vide [2\.2](#_2.2_–_Recuperação)\), então:

    Não preencher\.

Serie NF Saída \(C181\-06\)

 \(\*\)

19

Subsérie do Documento Fiscal de Referência

SUB\_SERIE\_DOCFIS\_REF

Se a saída referenciada pela devolução for uma Nota Fiscal \(vide [2\.1](#_2.1_–_Recuperação)\), então:

   Preencher com Subsérie da nota fiscal de saída referenciada, cfm tópico [2\.1](#_2.1_–_Recuperação)\.

__\[MFS61955\]__

Se a saída referenciada pela devolução for um Cupom Fiscal \(vide [2\.2](#_2.2_–_Recuperação)\), então:

    Não preencher\.

SubSerie NF Saída

 \(\*\)

20

Tipo do Documento de Referência

COD\_DOCTO\_REF

\(IDENT\_DOCTO\_REF\)

Se a saída referenciada pela devolução for uma Nota Fiscal \(vide [2\.1](#_2.1_–_Recuperação)\), então:

   Preencher com Tipo do documento fiscal da nota fiscal de saída referenciada cfm

   tópico [2\.1](#_2.1_–_Recuperação), de acordo com a Tabela de Tipos de Documentos \(SAFX2005\)\.

__\[MFS61955\]__

Se a saída referenciada pela devolução for um Cupom Fiscal \(vide [2\.2](#_2.2_–_Recuperação)\), então:

    Não preencher\.

Cod Docto NF Saída

 \(\*\)

21

Data Escrita Fiscal do Documento de Referência

DATA\_FISCAL\_REF

Se a saída referenciada pela devolução for uma Nota Fiscal \(vide [2\.1](#_2.1_–_Recuperação)\), então:

   Preencher com Data da Fiscal da nota fiscal de saída referenciada, cfm tópico 

   [2\.1](#_2.1_–_Recuperação)\.                  
__\[MFS61955\]__

Se a saída referenciada pela devolução for um Cupom Fiscal \(vide [2\.2](#_2.2_–_Recuperação)\), então:

    Não preencher\.

Dt Fiscal NF Saída \(C181\-10\)

 \(\*\)

22

23

Pessoa Física/Jurídica do Documento de Referência

IND\_FIS\_JUR\_REF/ COD\_FIS\_JUR\_REF

\(IDENT\_FIS\_JUR\_REF\)

Se a saída referenciada pela devolução for uma Nota Fiscal \(vide [2\.1](#_2.1_–_Recuperação)\), então:

    Preencher com Pessoa física/jurídica da nota fiscal de saída referenciada, cfm 

    no tópico [2\.1](#_2.1_–_Recuperação), de acordo com a Tabela de Pessoas Físicas/Jurídicas \(SAFX04\)\.           
__\[MFS61955\]__

Se a saída referenciada pela devolução for um Cupom Fiscal \(vide [2\.2](#_2.2_–_Recuperação)\), então:

    Não preencher\.

Não Apresentar, pois é igual a Pessoa Fis/Jur da Devolução

 \(\*\)

24

Modelo do Cupom Fiscal de Referência

COD\_MODELO\_REF

\(IDENT\_MODELO\_REF\)

Se a saída referenciada pela devolução for uma Nota Fiscal \(vide [2\.1](#_2.1_–_Recuperação)\), então:

    Não preencher

__\[MFS61955\]__

Se a saída referenciada pela devolução for um Cupom Fiscal \(vide [2\.2](#_2.2_–_Recuperação)\), então:

    Preencher com Modelo do Documento do cupom fiscal referenciado, cfm 

    no tópico [2\.2](#_2.2_–_Recuperação), de acordo com Tabela de Modelos de Documentos Fiscais 

    \(SAFX2024\)\.

Modelo ECF

\(C181\-05\)

 \(\*\)

25

Número do Caixa do Cupom Fiscal de Referência

COD\_CAIXA\_ECF\_REF

\(IDENT\_CAIXA\_ECF\)

Se a saída referenciada pela devolução for uma Nota Fiscal \(vide [2\.1](#_2.1_–_Recuperação)\), então:

    Não preencher

__\[MFS61955\]__

Se a saída referenciada pela devolução for um Cupom Fiscal \(vide [2\.2](#_2.2_–_Recuperação)\), então:

    Preencher com Número do Caixa do cupom fiscal referenciado, cfm 

    no tópico [2\.2](#_2.2_–_Recuperação), de acordo com Tabela de Cadastro de Equipamentos ECF 

    \(SAFX2087\)\.

Número Caixa ECF

 \(\*\)

26

COO \(Contador de Ordem de Operação\) do Cupom Fiscal de Referência

NUM\_COO\_REF

Se a saída referenciada pela devolução for uma Nota Fiscal \(vide [2\.1](#_2.1_–_Recuperação)\), então:

    Não preencher

__\[MFS61955\]__

Se a saída referenciada pela devolução for um Cupom Fiscal \(vide [2\.2](#_2.2_–_Recuperação)\), então:

    Preencher com Número do Contador de Ordem de Operação \(COO\) do cupom 

    fiscal referenciado, cfm no tópico [2\.2](#_2.2_–_Recuperação)\.

COO Cupom Fiscal \(C181\-08\)

 \(\*\)

27

Data de Emissão do Cupom Fiscal de Referência

DATA\_EMISSAO\_REF

Se a saída referenciada pela devolução for uma Nota Fiscal \(vide [2\.1](#_2.1_–_Recuperação)\), então:

    Não preencher

__\[MFS61955\]__

Se a saída referenciada pela devolução for um Cupom Fiscal \(vide [2\.2](#_2.2_–_Recuperação)\), então:

    Preencher com Data Emissão do cupom fiscal referenciado, cfm no tópico [2\.2](#_2.2_–_Recuperação)\.

COO Cupom Fiscal \(C181\-10\)

 \(\*\)

28

Número do Equipamento SAT do Cupom Fiscal de Referência

NUM\_EQUIP\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal SAT\. 

Não Apresentar

 \(\*\)

29

Número do Cupom Fiscal do Referência 

NUM\_CUPOM\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal SAT\.

Não Apresentar

\(\*\)

30

Número do Item do Documento de Referência

NUM\_ITEM\_DOC\_REF

Se a saída referenciada pela devolução for uma Nota Fiscal \(vide [2\.1](#_2.1_–_Recuperação)\), então:

    Preencher com Número do Item da nota fiscal referenciada, cfm tópico [2\.1](#_2.1_–_Recuperação)\.

__\[MFS61955\]__

Se a saída referenciada pela devolução for um Cupom Fiscal \(vide [2\.2](#_2.2_–_Recuperação)\), então:

    Preencher com Número do Item do cupom fiscal referenciado, cfm no tópico [2\.2](#_2.2_–_Recuperação)

Num Item NF Saída

\(C181\-11\)

31

Código Motivo

Campos da EFD correspondentes: 02 do C181 e 06 do C186\.

COD\_MOTIVO

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal de devolução \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

__\[MFS96666\]: Inclusão dos códigos RS601, \.\.\., RS656 e RS801, \.\.\., RS856 a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com __RS600__ quando for Estorno do Ressarcimento\-ST\.

          Preencher com __RS800 __quando for Estorno do Complemento\-ST\.__ __

       Para período da geração a partir de Jan\-2023, então:

          Preencher com __RS600 __ou __RS601, \.\.\., RS656__ quando for Estorno de 

          Ressarcimento\-ST\.

          Preencher com __RS800 __ou __RS801, \.\.\., RS856__ quando for Estorno de

          Complemento\-ST\.

__       __Vide “[Regra p/ Operação de Saída Interna p/ Consumidor Final](#COD_MOTIVO_CONS_FINAL)”\(\*\)\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 778 – Outra UF:

Preencher com RS713\.

__MFS64191__

- Para Cód\. Operação = 781 – Exportação:

Preencher com RS714\.

- Para Cód\. Operação = 782 – Nova ST:

Preencher com RS717\.

- Para Cód\. Operação = 783 – Isenção:

Preencher com RS719\.

- Para Cód\. Operação = 779 – Outra UF Art 24:

Preencher com RS501\.

- Para Cód\. Operação = 784 – Isenção Art 24\-A:

Preencher com RS501\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com RS500\.

<a id="COD_MOTIVO_CONS_FINAL"></a>\(\*\) Regra p/ Operação de Saída Interna p/ Consumidor Final:

__\[MFS\-63471\]__ A regra original foi feita baseada no Ressarcimento MG, onde eram comparadas as bases \(BC Entrada e BC Saída\) para determinar se houve ressarcimento ou complemento\. Conceitualmente não havia erro nessa abordagem só que, na prática, um cenário apresentou divergência entre o resultado da comparação pela base e o valor em si calculado para complemento/ressarcimento\.

O cenário foi: \[BC Saída > BC Entrada\] e \[\(ICMS Saída\) < \(ICMS Entrada \+ ICMS\-ST Entrada\)\]\.

Pela comparação de bases, o resultado deu complemento, mas ao calcular o valor do complemento no campo 31, o valor deu negativo, veja fórmula:

 \(ICMS Saída \(VLR\_UNIT\_ICMS\_OPER\_SAI\) \- 

  ICMS Entrada \(VLR\_UNIT\_ICMS\_ESTQ\_SAI\) \- 

  ICMS\-ST Entrada \(VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) 

O valor negativo demonstra que na verdade temos ressarcimento, pois a soma dos valores das entradas foi maior que da saída\. 

Sendo assim alteramos a regra para utilizarmos como comparação os próprios valores de ICMS e ICMS\-ST de Saída e Entrada, em substituição BC\-Entrada e BC\-Saída

__\[MFS96666\]: Inclusão dos códigos RS601, \.\.\., RS656 e RS801, \.\.\., RS856 a partir de Jan\-2023:__

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_UNIT\_ICMS\_OPER\_SAI > 0 \(entrada > saída = ressarcimento\) então:

       A saída referenciada pela devolução obteve Restituição \(RS100\);

Para período da geração anterior a Jan\-2023, então:

          Preencher com __RS600__ \- Estorno do Ressarcimento\-ST

       Para período da geração a partir de Jan\-2023, então:

          Preencher com __RS600__, para operação sem redução de base de cálculo;

          Preencher com “__RS601”__, \.\.\., “__RS605__”, para operação com alíquota interna reduzida;

          Preencher com “__RS651, __\.\.\., __RS656__, para operação com % redução de base de cálculo;

          Veja “[Regra para Códigos Motivo Consumidor Final 2023](#Regra_COD_MOTIVO_2023)” [\(\*\*\)](#Regra_COD_MOTIVO_2023)

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_UNIT\_ICMS\_OPER\_SAI < 0 \(entrada < saída = complemento\) então:

   A saída referenciada pela devolução obteve Complemento \(RS300\);

Para período da geração anterior a Jan\-2023, então:

          Preencher com __RS800__ \- Estorno do Complemento\-ST

       Para período da geração a partir de Jan\-2023, então:

          Preencher com __RS800__, para operação sem redução de base de cálculo;

          Preencher com “__RS801”__, \.\.\., “__RS805__”, para operação com alíquota interna reduzida;

          Preencher com “__RS851, __\.\.\., __RS856__, para operação com % redução de base de cálculo;

          Veja “[Regra para Códigos Motivo Consumidor Final 2023](#Regra_COD_MOTIVO_2023)” [\(\*\*\)](#Regra_COD_MOTIVO_2023)

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_UNIT\_ICMS\_OPER\_SAI = 0 \(entrada = saída\) então: \(\*\*\*\)

   A saída referenciada pela devolução não teve nem Restituição nem 

   Complemento\.

Para período da geração anterior a Jan\-2023, então:

          Preencher com __RS600__ \- Estorno do Ressarcimento\-ST

       Para período da geração a partir de Jan\-2023, então:

          Preencher com __RS600__, para operação sem redução de base de cálculo;

          Preencher com “__RS601”__, \.\.\., “__RS605__”, para operação com alíquota interna reduzida;

          Preencher com “__RS651, __\.\.\., __RS656__, para operação com % redução de base de cálculo;

          Veja “[Regra para Códigos Motivo Consumidor Final 2023](#Regra_COD_MOTIVO_2023)” [\(\*\*\)](#Regra_COD_MOTIVO_2023)

 

__\[MFS96666\]: Inclusão dos códigos RS101, \.\.\., RS156 e RS301, \.\.\., RS356 a partir de Jan\-2023:__

Essa regra considera o campo “Código do Amparo/Texto/Ocorrência ICMS\-ST” do item de Mercadoria do Documento Fiscal de Saída devolvido \(item 66 – COD\_OBS\_VCONT\_ITEM da SAFX08\) ou item do Cupom Fiscal devolvido \(item 45 – COD\_AMPARO\_LEGAL da SAFX994\)\.

\(\*\*\) <a id="Regra_COD_MOTIVO_2023"></a>Regra para Códigos Motivo Consumidor Final 2023

          \- Se Cod\_Amparo = \(4601 ou 4623 ou 4629 ou 4651 ou 4652 ou 4665\) 

            então:

              Preencher com RS601 quando estorno de ressarcimento;

              Preencher com RS801 quando estorno de complemento;

          \- Se Cod\_Amparo = 4613 então: 

              Preencher com RS602 quando estorno de ressarcimento;

              Preencher com RS802 quando estorno de complemento;

          \- Se Cod\_Amparo = 4614 então: 

              Preencher com RS603 quando estorno de ressarcimento;

              Preencher com RS803 quando estorno de complemento;

          \- Se Cod\_Amparo = \(4620 ou 4624 ou 4662 ou 4681\) então: 

              Preencher com RS604 quando estorno de ressarcimento;

              Preencher com RS804 quando estorno de complemento;

          \- Se Cod\_Amparo = 4663b então: 

              Preencher com RS605 quando estorno de ressarcimento;

              Preencher com RS805 quando estorno de complemento;

          \- Se Cod\_Amparo = “4616” então:

               Preencher c/ RS651 quando estorno de ressarcimento;

               Preencher c/ RS851 quando estorno de complemento;

          \- Se Cod\_Amparo = “4617a1” então: 

              Preencher c/ RS652 quando estorno de ressarcimento;

              Preencher c/ RS852 quando estorno de complemento;

          \- Se Cod\_Amparo = \(“4617a2” ou “4617b3” ou “4656b”\)    então:

              Preencher c/ RS653 quando estorno de ressarcimento;

              Preencher c/ RS853 quando estorno de complemento;

          \- Se Cod\_Amparo = “4617b1” então: 

              Preencher c/ RS654 quando estorno de ressarcimento;

              Preencher c/ RS854 quando estorno de complemento;

          \- Se Cod\_Amparo = \(“4617b2” ou “4656a"\) então: 

              Preencher c/ RS655 quando estorno de ressarcimento;

              Preencher c/ RS855 quando estorno de complemento;

          \- Se Cod\_Amparo = “4617b4” então: 

               Preencher c/ RS656 quando estorno de ressarcimento;

               Preencher c/ RS856 quando estorno de complemento;

          \- Se Cod\_Amparo não estiver preenchido ou for diferente dos acima mencionados então: 

             Preencher com RS600 quando estorno de ressarcimento;

             Preencher com RS800 quando estorno de complemento;

          Se “__%Redução BC__” preenchido e Código Amparo não preenchido ou diferente dos acima mencionados, então: 

               Exibir a mensagem de aviso no relatório de Log:

              Se a devolução for de uma nota fiscal, o texto da mensagem será:

*“Registro C181: Devolução da Nota de Saída com base de cálculo reduzida foi gerado código de motivo RS600 ou RS800, pois faltou informação no campo Amparo/Texto/Ocorrência \(ST\) do item de mercadoria da saída devolvida, ou este foi preenchido com um código de Amparo cujo inciso não está acobertado pela tabela 5\.7 do Sped Fiscal\. Reveja o % de Redução BC parametrizado para o Produto, acessando uma das opções disponíveis no menu Parâmetros >> Produtos \(Por Código, Por NCM ou Por CEST\) e o Amparo Legal \(ST\) do Item de Mercadoria da NF de Saída \(item 66 da SAFX08\)\. *

*Consulte o manual operacional do módulo para obter esclarecimentos sobre a correlação dos códigos de Amparo Legal com o % de Redução BC\.”*

              Se a devolução for de um cupom fiscal, o texto da mensagem será:

*“Registro C181: Devolução do Cupom Fiscal com base de cálculo reduzida foi gerado código de motivo RS600 ou RS800, pois faltou informação no campo Amparo/Texto/Ocorrência do item do cupom fiscal de saída devolvido, ou este foi preenchido com um código de Amparo cujo inciso não está acobertado pela tabela 5\.7 do Sped Fiscal\. Reveja o % de Redução BC parametrizado para o Produto, acessando uma das opções disponíveis no menu Parâmetros >> Produtos \(Por Código, Por NCM ou Por CEST\) e o Amparo Legal do Item do Cupom Fiscal de Saída \(item 45 da SAFX994\)\. *

*Consulte o manual operacional do módulo para obter esclarecimentos sobre a correlação dos códigos de Amparo Legal com o % de Redução BC\.”*

O log deve demonstrar o % Redução BC parametrizado \+ Código do Amparo do item do documento de saída \(ou do item do cupom fiscal\) \+ as informações necessárias para a identificação do item da Nota de Devolução da Saída e da Saída \(nota ou cupom fiscal\) referenciada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)\. Caso a saída referenciada pela devolução seja um cupom fiscal \(SAFX994\) \(vide [2\.2](#_2.2_–_Recuperação)\) informar Número do Caixa \(campo 04 SAFX994\), COO \(campo 05 SAFX994\), Data da emissão \(campo 06 SAFX994\)\.

Onde:

- \(BC\-Entrada\):

“Valor Médio Unitário da Base de Cálculo do ICMS\-ST \([BC\-Entrada](#BC_Entrada)\)”\.

Ver [*Dados para o Cálculo da Média Pondera Móvel dos Valores Unitários*](#Detalha_Media_ponderada)

- \(BC\-Saída\): 

Para Nota Fiscal de saída referenciada pela devolução \(vide [2\.1](#_2.1_–_Recuperação)\):

 “Valor Unitário da BC do ICMS na Operação Conv \([BC\-Saída](#BC_SAIDA_NF_SAI)\)”

 Ver  [*Detalhamento da Nota de Saída Referenciada pela Devolução*](#Detalha_NF_SAI)\.

        Para Cupom Fiscal de saída referenciado pela devolução \(vide [2\.2](#_2.2_–_Recuperação)\):

         “Valor Unitário da BC do ICMS na Operação Conv Cupom Fiscal \([BC\-Saída](#BC_SAIDA_CUPOM_SAI)\)”

          Ver *[Detalhamento do Cupom Fiscal Referenciado pela Devolução](#Detalha_CUPOM_SAI)*

- %Redução BC e Alíquota Interna da parametrização de Produto por Código ou NCM ou CEST sujeito ao ICMS\-ST, vigente na __Data de Emissão da Saída__ referenciada;

\(\*\*\*\) 12/01/2021: Consulta foi realizada a nossa Área da Informação \(CAN\) que explicou que conceitualmente esse cenário não existe, por isso o fisco foi omisso e não especificou tratamento\. Como sistemicamente isso pode ocorrer, o tratamento que foi dado é emissão de mensagem no log\. Nesse caso, o cliente deve revisar sua nota\.

\[__MFS64550\]: __O fisco definiu que a nota sem ressarcimento e complemento seja apresenta\. O validador da GIA\-RS já está considerando C185 nota sem ressarcimento e complemento com código “__RS100__”\. __\[MFS61955\]: __Logo estamos deduzindo que o C181 também deve ser ajustado para que, nesse caso, gere com RS600\.

Cod Motivo \(C181\-02\)

32

Quantidade Convertida

Campos da EFD correspondentes: 03 do C181 e 07 do C186\.

QTD\_CONV

Preencher com a quantidade de devolução convertida\.

Se a saída referenciada pela devolução for uma Nota Fiscal \(vide [2\.1](#_2.1_–_Recuperação)\), então:

- Caso a nota fiscal de saída esteja associada à nota de Devolução pela __SAFX192__:

Preencher com:

“Qtde da Devolução Convertida Calculada p/ Saída Referenciada \(safx192\) \([QTD\_CONV\_REF\_DEV](#QTD_CONV_REF_DEV)\)” 

- Caso a nota de saída esteja associada à nota de devolução pela __SAFX08__:

Preencher com:

“Qtde Convertida Calculada para NF de Devolução de Saída \(safx08\) \([QTD\_CONV\_NF\_DEV](#QTD_CONV_NF_DEV)\)”

__\[MFS61955\]__

Se a saída referenciada pela devolução for um Cupom Fiscal \(vide [2\.2](#_2.2_–_Recuperação)\), então:

    Preencher com:

    “Qtde da Devolução Convertida Calculada p/ Saída Referenciada \(safx192\) 

    \([QTD\_CONV\_REF\_DEV](#QTD_CONV_REF_DEV)\)”

Ver __*[Detalhamento da Nota de Devolução](#Detalha_NF_DEV)*__

Qtde Conv \(C181\-03\)

33

Unidade de Medida

Campos da EFD correspondentes: 04 do C181 e 08 do C186\.

COD\_MEDIDA

\(IDENT\_MEDIDA\)

Campo 14 – Unidade de Medida do Cadastro do Produto \(SAFX2013\), do produto pertencente ao item da nota de Devolução da Saída, recuperada no tópico [2\.0](#_2.0_–_Recuperação)\.

 *\(ver OBS abaixo sobre os produtos associados\)*

__Sobre os produtos associados:__ Quando se tratar de uma nota fiscal de produto “associado”, a unidade de medida apresentada será a __unidade do produto principal__\.

Medida

\(C181\-04\)

 

34

Valor Unitário Conv

Campos da EFD correspondentes: 12 do C181 e 15 do C186\.

VLR\_UNIT\_CONV

Se a saída referenciada pela devolução for uma Nota Fiscal \(vide [2\.1](#_2.1_–_Recuperação)\), então:

    Preencher com:

    VLR\_UNIT\_CONV = VLR\_CONTAB\_ITEM da SAFX08 / QTD\_CONV\_NF\_SAI

    Onde:

- VLR\_CONTAB\_ITEM é o campo 64\-valor Contabil do Item da nota de saída referenciada;
- QTD\_CONV\_NF\_SAI: “Qtde Convertida Calculada para o Item da NF de Saída Referenciada \([QTD\_CONV\_NF\_SAI](#QTD_CONV_NF_SAI)\)”” 

    Ver  *[Detalhamento da Nota de Saída Referenciada pela Devolução](#Detalha_NF_SAI)*\.

__\[MFS61955\]__

Se a saída referenciada pela devolução for um Cupom Fiscal \(vide [2\.2](#_2.2_–_Recuperação)\), então:

    Preencher com:

    VLR\_UNIT\_CONV = VLR\_LIQ\_ITEM da SAFX994 / QTD\_CONV\_CF

    Onde:

- VLR\_LIQ\_ITEM é o campo 22\-Valor Total Líquido \(SAFX994\) do Item do cupom fiscal referenciado;
- QTD\_CONV\_CF: “Qtde Convertida Calculada para o Item do Cupom Fiscal Referenciado \([QTD\_CONV\_CF](#QTD_CONV_CF)\)” 

    Ver *[Detalhamento do Cupom Fiscal Referenciado pela Devolução](#Detalha_CUPOM_SAI)*\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

Vlr Unit Conv \(C181\-12\)

 

35

Valor Unitário ICMS OP Conv

Campos da EFD correspondentes: 17 do C181 e 16 do C186

VLR\_ICMS\_CONV

Preencher com zero\. \(idem ao ressarcimento MG\)

Vlr Unit ICMS Op Conv \(C181\-17\)

 

36

Valor Unitário Base ICMS ST Conv da Entrada

Campo da EFD correspondente: 17 do C186\.

VLR\_UNIT\_BC\_ICMSS\_ENT

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Entradas\.   


Não Apresentar

 

37

Valor Unitário ICMS ST Conv da Entrada

Campo da EFD correspondente: 18 do C186\.

VLR\_UNIT\_ICMSS\_CONV\_ENT

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Entradas\.

Não Apresentar

 

38

Valor Unitário FCP ST Conv da Entrada

Campo da EFD correspondente: 19 do C186\.

VLR\_UNIT\_FCP\_CONV\_ENT

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Entradas\.

Não Apresentar

 

39

Valor Unitário ICMS OP Estoque Conv

Campo da EFD correspondente: 13 do C181\.

VLR\_UNIT\_ICMS\_ESTQ\_SAI

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher conforme [Regra do Valor Médio Unitário do ICMS](#REGRA_VLR_UNIT_ICMS_ESTQ) \(\*\)

__       \[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:__

       Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST”  

       \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no tópico [2\.3](#_2.3_–_Recuperação) __Passo 1__ for negativo, 

        então:

          Desconsiderar a regra acima e preencher este campo com ZERO\.

\[__MFS58042/ MFS59698\]__

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher conforme [Regra do Valor Médio Unitário do ICMS](#REGRA_VLR_UNIT_ICMS_ESTQ) \(\*\)

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

__\[MFS96666\]: RS5xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

  Preencher conforme [Regra do Valor Médio Unitário do ICMS](#REGRA_VLR_UNIT_ICMS_ESTQ) \(\*\)\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

__\[MFS96666\]: RS5xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

  Preencher conforme [Regra do Valor Médio Unitário do ICMS](#REGRA_VLR_UNIT_ICMS_ESTQ) \(\*\)\.

<a id="REGRA_VLR_UNIT_ICMS_ESTQ"></a>\(\*\) Regra do Valor Médio Unitário do ICMS: 

Preencher com o “Valor Médio Unitário do ICMS” recuperado do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\), para o Produto na Data de Emissão da nota \(ou cupom\) de saída referenciada\. 

Caso não seja encontrada, considerar a última nota de entrada do produto anterior à saída e calcular o valor unitário do ICMS\. Para isso, executar:

__Se__ a consulta realizada no __Passo 1__ do tópico [2\.3](#_2.3_–_Recuperação) retornar registro, então:

    Preencher com: \[“Valor Médio Unitário do ICMS”\] do

   “Cálculo da Média Pondera Móvel dos Valores Unitários” 

    \(campo VLR\_UNIT\_ICMS\_FIM\_MP da EST\_ST\_RS\_MEDIA\_POND\);

__Senão__:

      Se a consulta realizada no __Passo 2__ do tópico [2\.3](#_2.3_–_Recuperação) retornar registro, então:

           Calcular o Valor Unitário do ICMS com base na Última Nota de Entrada\.

           Veja Regra de Preenchimento \(\*\) descrita a seguir\.

\(\*\) Regra de Preenchimento:

Preencher com:

 Valor do ICMS / QTD\_CONV\_NF\_ENT 

Onde os valores são oriundos do item da Última Nota de Entrada:

- Valor do ICMS é oriundo de um dos três campos SAFX08, dependendo de qual esteja preenchido:

Campo “43\-Valor ICMS”, se preenchido, ou

   Campo “80\-ICMS não Escriturado”, se preenchido, ou

       Campo “225\-Valor ICMS Não Destacado”  

- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF Última Entrada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  __*[Detalhamento da Ùltima Nota Fiscal de Entrada](#Detalha_ULT_NF_ENT)*__\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ arredondar para 6 casas decimais o valor médio unitário recuperado da Média Ponderada pois compõe o layout do C181\.

Vlr Unit ICMS Estoque Conv \(C181\-13\)

40

Valor Unitário ICMS ST Estoque Conv

Campo da EFD correspondente: 14 do C181\.

VLR\_UNIT\_ICMSS\_ESTQ\_SAI

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher conforme [Regra do Valor Médio Unitário do ICMS\-ST](#REGRA_VLR_UNIT_ICMS_ST_ESTQ) \(\*\)

__       \[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:__

       Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST”  

       \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no tópico [2\.3](#_2.3_–_Recuperação) __Passo 1__ for negativo, 

        então:

          Desconsiderar a regra acima e preencher este campo com ZERO\.

\[__MFS58042/ MFS59698\]__

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher conforme [Regra do Valor Médio Unitário do ICMS\-ST](#REGRA_VLR_UNIT_ICMS_ST_ESTQ) \(\*\)

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

__\[MFS96666\]: RS5xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

  Preencher conforme [Regra do Valor Médio Unitário do ICMS\-ST](#REGRA_VLR_UNIT_ICMS_ST_ESTQ) \(\*\)\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

__\[MFS96666\]: RS5xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

  Preencher conforme [Regra do Valor Médio Unitário do ICMS\-ST](#REGRA_VLR_UNIT_ICMS_ST_ESTQ) \(\*\)\.

<a id="REGRA_VLR_UNIT_ICMS_ST_ESTQ"></a>\(\*\) Regra do Valor Médio Unitário do ICMS\-ST: 

__\[MFS66171\]__

Preencher com “Valor Médio Unitário do ICMS\-ST c/ FECEP” recuperado do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\), para o Produto na Data de Emissão da nota \(ou cupom\) de saída referenciada\. 

Caso não seja encontrada, considerar a última nota de entrada do produto anterior à saída e calcular os valores unitários do ICMS\-ST e FECEP\-ST\. Para isso, executar:

__Se__ a consulta realizada no Passo 1 do tópico [2\.3](#_2.3_–_Recuperação) retornar registro, então:

    Preencher com:

     \[“Valor Médio Unitário do ICMS\-ST c/ FECEP”\] do “Cálculo da Média Pondera 

    Móvel dos Valores Unitários” 

    \(campo VLR\_UNIT\_ICMS\_ST\_FECEP\_FIM\_MP EST\_ST\_RS\_MEDIA\_POND\);

__Senão__:

      Se a consulta realizada no Passo 2 do tópico [2\.3](#_2.3_–_Recuperação) retornar registro, então:

           Calcular os Valores Unitários com base na Última Nota de Entrada\.

           Veja Regra de Preenchimento \(\*\) descrita a seguir\.

\(\*\) Regra de Preenchimento:

O preenchimento do campo seria:

 \(Valor do ICMS\-ST \+ Valor do FECEP\-ST\)/ QTD\_CONV\_NF\_ENT

Mas deve\-se tratar o caso do Valor do ICMS\-ST já conter o FECEP\-ST, para que este não seja somado duas vezes\. 

Como premissa, a tabela DATAMART já contém o FECEP\-ST embutido no campo 52\-ICMS\-ST, pois na equalização do DATA MART, os clientes são orientados a marcar o parâmetro para Somar FECEP ao ICMS/ICMS\-ST, quando o FECEP não “nasce” embutido ao ICMS/ICMS\-ST nas tabelas “normais” X07/X08\. 

Quanto às tabelas “normais”, o FECEP pode ou não estar embutido campo 52\-ICMS\-ST via importação da SAFX08, por isso existe o parâmetro “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)”, da tela de Dados Iniciais \(menu Parâmetros 🡪 IN\-RE 087/2020 🡪 Dados Iniciais\)\.__\]__\.

Tratamento do FECEP embutido nos vlrs de ICMS/ICMS\-ST \(aplicado às Entradas e Devoluções de Entradas\):

  Se o item de mercadoria foi recuperado das tabelas “normais” \(X07/X08\), então:

        Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos 

        itens \(SAFX08\)” foi marcado na tela de Dados Iniciais, então:

             Se for considerado o “52\-Valor ICMS Substituição Tributária” p/ o  

             __Valor do ICMS\-ST__ \(\*\*\):

    Preencher com: \(Valor do ICMS\-ST\) / QTD\_CONV\_NF\_ENT 

Senão:

                  Preencher com: 

                 \(Valor do ICMS\-ST \+ Valor do ICMS\-ST FECEP\) / QTD\_CONV\_NF\_ENT

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos 

      itens \(SAFX08\)” não foi marcado, então:

           Preencher com:  

           \(Valor do ICMS\-ST \+ Valor do ICMS\-ST FECEP\) / QTD\_CONV\_NF\_ENT

  Se o item de mercadoria foi recuperado das tabelas do DATAMART, então:

       Se for considerado o “52\-Valor ICMS Substituição Tributária” para o 

       __Valor do ICMS\-ST__ \(\*\*\):

           Preencher com: \(Valor do ICMS\-ST\) / QTD\_CONV\_NF\_ENT

       Senão

           Preencher com:  

           \(Valor do ICMS\-ST \+ Valor do ICMS\-ST FECEP\) / QTD\_CONV\_NF\_ENT

__\[MFS543860\]__ Tratamento do parâmetro para identificar se o valor do FECP está embutido nos valores de ICMS não destacado/não escriturado

Tratamento do FECEP embutido nos valores de ICMS\-ST não escriturado e não destacado \(aplicado às Entradas e Devoluções de Entradas\):

    Se o parâmetro “Valores de FECEP estão embutidos nos valores de ICMS\-ST não destacado/não escriturado” for marcado na tela de Dados Iniciais, então:

             Se for considerado o campo “145\- VLR\_ICMSS\_N\_ESCRIT” p/ o

             __Valor do ICMS\-ST__ \(\*\):

    Preencher com: \(VLR\_ICMSS\_N\_ESCRIT\) / QTD\_CONV\_NF\_ENT 

Senão:

                  Preencher com:

                  \(VLR\_ICMSS\_N\_ESCRIT \+ Valor do ICMS\-ST FECEP\) / 

                  QTD\_CONV\_NF\_ENT

            Se for considerado o campo “133\- VLR\_ICMSS\_NDESTAC” p/ o

             __Valor do ICMS\-ST__ \(\*\):

    Preencher com: \(VLR\_ICMSS\_NDESTAC\) / QTD\_CONV\_NF\_ENT 

Senão:

                  Preencher com:

                  \(VLR\_ICMSS\_NDESTAC \+ Valor do ICMS\-ST FECEP\) / 

                  QTD\_CONV\_NF\_ENT

    Se o parâmetro “Valores de FECEP estão embutidos nos valores de ICMS\-ST não destacado/não escriturado” não for marcado, então:

         Preencher com:  

         \(VLR\_ICMSS\_N\_ESCRIT \+ Valor do ICMS\-ST FECEP\) /   

          QTD\_CONV\_NF\_ENT

              OU

         \(VLR\_ICMSS\_NDESTAC \+ Valor do ICMS\-ST FECEP\) / 

          QTD\_CONV\_NF\_ENT

  

Onde os valores são oriundos do item da Última Nota de Entrada:

- \(\*\*\)__Valor do ICMS\-ST__ é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

         Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

    Senão:

        Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                         “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então:

             Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

        Senão:

            Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                              “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, então:

                 Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.
- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF Última Entrada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  __*[Detalhamento da Ùltima Nota Fiscal de Entrada](#Detalha_ULT_NF_ENT)*__\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ arredondar para 6 casas decimais o valor médio unitário recuperado da Média Ponderada pois compõe o layout do C181\.

Vlr Unit ICMS\-ST Estoque Conv \(C181\-14\)

 

41

Valor Unitário FCP ICMS ST Estoque Conv

Campo da EFD correspondente: 15 do C181\.

VLR\_UNIT\_FCP\_ESTQ\_SAI

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher conforme [Regra do Valor Médio Unitário do FECEP\-ST](#REGRA_VLR_UNIT_FECEP_ST_ESTQ) \(\*\)

__       \[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:__

       Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST”  

       \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no tópico [2\.3](#_2.3_–_Recuperação) __Passo 1__ for negativo, 

        então:

          Desconsiderar a regra acima e preencher este campo com ZERO\.

\[__MFS58042/ MFS59698\]__

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher conforme [Regra do Valor Médio Unitário do FECEP\-ST](#REGRA_VLR_UNIT_FECEP_ST_ESTQ) \(\*\)

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

__\[MFS96666\]: RS5xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

  Preencher conforme [Regra do Valor Médio Unitário do FECEP\-ST](#REGRA_VLR_UNIT_FECEP_ST_ESTQ) \(\*\)\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

__\[MFS96666\]: RS5xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

  Preencher conforme [Regra do Valor Médio Unitário do FECEP\-ST](#REGRA_VLR_UNIT_FECEP_ST_ESTQ) \(\*\)\.

<a id="REGRA_VLR_UNIT_FECEP_ST_ESTQ"></a>\(\*\) Regra do Valor Médio Unitário do FECEP\-ST: 

Preencher com “Valor Médio Unitário do FECEP\-ST” recuperado do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\), para o Produto na Data de Emissão da nota \(ou cupom\) de saída referenciada\. Caso não seja encontrada, considerar a última nota de entrada do produto anterior à saída e calcular o valor unitário do FECEP\-ST\. Para isso, executar:

__Se__ a consulta realizada no __Passo 1__ do tópico [2\.3](#_2.3_–_Recuperação) retornar registro, então:

    Preencher com: \[“Valor Médio Unitário do FECEP\-ST”\] do

   “Cálculo da Média Pondera Móvel dos Valores Unitários” 

    \(Campo VLR\_UNIT\_FECEP\_ST\_FIM\_MP da EST\_ST\_RS\_MEDIA\_POND\);

__Senão__:

      Se a consulta realizada no __Passo 2__ do tópico [2\.3](#_2.3_–_Recuperação) retornar registro, então:

           Calcular o Valor Unitário do FECEP\-ST com base na Última Nota de Entrada\.

           Veja Regra de Preenchimento \(\*\) descrita a seguir\.

\(\*\) Regra de Preenchimento:

Preencher com:

 Valor do FECEP\-ST / QTD\_CONV\_NF\_ENT 

Onde os valores são oriundos do item da Última Nota de Entrada:

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.
- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF Última Entrada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  __*[Detalhamento da Ùltima Nota Fiscal de Entrada](#Detalha_ULT_NF_ENT)*__\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ arredondar para 6 casas decimais o valor médio unitário recuperado da Média Ponderada pois compõe o layout do C181\.

Vlr Unit FCP\-ST Estoque Conv \(C181\-15\)

 

42

Valor Unitário ICMS na Operação Conv

Campo da EFD correspondente: 16 do C181\.

VLR\_UNIT\_ICMS\_OPER\_SAI

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

       Preencher com   BC\-Saída \* Alíquota interna / 100

__        \[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:__

        Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” 

        \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no __Passo 1 __do tópico [2\.3](#_2.3_–_Recuperação) for 

         negativo, então:

            Acrescentar ao valor calculado pela regra acima, o valor a seguir:

            VLR\_UNIT\_BC\_ST\_FIM\_MP \* Alíquota Interna / 100 \(sem sinal negativo\)

__        \[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 \[__MFS63471/MFS72429\]: __Arredondar o resultado acima em 6 decimais\.

\[__MFS58042/ MFS59698\]__

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com Zero\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

Preencher com Zero\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com Zero\.

Onde:

- Alíquota Interna da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na __Data de Emissão da Saída__ referenciada;

Ver [Detalhamento da Parametrização por Produto](#Detalha_Parametrização_Produto)

- \(BC\-Saída\): 

       Para Nota Fiscal de saída referenciada pela devolução \(vide [2\.1](#_2.1_–_Recuperação)\):

    “Valor Unitário da BC do ICMS na Operação Conv \([BC\-Saída](#BC_SAIDA_NF_SAI)\)”

    Ver  [*Detalhamento da Nota de Saída Referenciada pela Devolução*](#Detalha_NF_SAI)\.

__       \[MFS61955\]__

       Para Cupom Fiscal de saída referenciado pela devolução \(vide [2\.2](#_2.2_–_Recuperação)\):

         “Valor Unitário da BC do ICMS na Operação Conv Cupom Fiscal \([BC\-Saída](#BC_SAIDA_CUPOM_SAI)\)”

          Ver *[Detalhamento do Cupom Fiscal Referenciado pela Devolução](#Detalha_CUPOM_SAI)*

Vlr Unit ICMS Operação Conv \(C181\-16\)

 

43

Valor Unitário ICMS ST Conv Rest

Campo da EFD correspondente: 18 do C181\.

VLR\_UNIT\_ICMSS\_REST\_SAI

Campo referente ao estorno de Complemento, logo deve ser preenchido no caso da saída referenciada tenha sido objeto de Complemento\.

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher com o Valor do estorno da Complementação\.

Vide “[Regra p/ Operação de Saída Interna p/ Consumidor Final](#COMPL_CONS_FINAL)”\(\*\)\.

\[__MFS58042/ MFS59698\]__

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com Zero\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

Preencher com Zero\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com Zero\.

<a id="COMPL_CONS_FINAL"></a>\(\*\)Regra p/ Operação de Saída Interna p/ Consumidor Final:

__\[MFS\-63471\]__ Não utilizar as bases \(BC\-Entrada e BC\-Saída\) na comparação para identificar se houve ressarcimento ou complemento\. Usar os próprios valores de ICMS e ICMS\-ST de Saída e Entrada\.

Se \(BC\-Entrada\) < \(BC\-Saída\) então:

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_UNIT\_ICMS\_OPER\_SAI < 0 \(entrada < saída = complemento\) então:

   Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMS\_OPER\_SAI \- 

    VLR\_UNIT\_ICMS\_ESTQ\_SAI \- 

    VLR\_UNIT\_ICMSS\_ESTQ\_SAI

    Onde:

- VLR\_UNIT\_ICMS\_OPER\_SAI: valor gravado no campo 42\-Valor Unitário ICMS na Operação Conv;
- VLR\_UNIT\_ICMS\_ESTQ\_SAI: valor gravado no campo 39\- Valor Unitário ICMS OP Estoque Conv;
- VLR\_UNIT\_ICMSS\_ESTQ\_SAI: valor gravado no campo 40\-Valor Unitário ICMS ST Estoque Conv;

Senão:

   Não preencher

Onde:

- \(BC\-Entrada\):

“Valor Médio Unitário da Base de Cálculo do ICMS\-ST \([BC\-Entrada](#BC_Entrada)\)”\.

Ver [*Dados para o Cálculo da Média Pondera Móvel dos Valores Unitários*](#Detalha_Media_ponderada)

-  \(BC\-Saída\):

Para Nota Fiscal de saída referenciada pela devolução \(vide [2\.1](#_2.1_–_Recuperação)\):

 “Valor Unitário da BC do ICMS na Operação Conv \([BC\-Saída](#BC_SAIDA_NF_SAI)\)”

 Ver  [*Detalhamento da Nota de Saída Referenciada pela Devolução*](#Detalha_NF_SAI)\.

       Para Cupom Fiscal de saída referenciado pela devolução \(vide [2\.2](#_2.2_–_Recuperação)\):

         “Valor Unitário da BC do ICMS na Operação Conv Cupom Fiscal \([BC\-Saída](#BC_SAIDA_CUPOM_SAI)\)”

          Ver *[Detalhamento do Cupom Fiscal Referenciado pela Devolução](#Detalha_CUPOM_SAI)*

Validação:

Caso o valor gravado no campo seja negativo, exibir mensagem de aviso no log:

*“Registro C181: Nota de Saída gerada com valor unitário do ressarcimento negativo\.”*

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Saída e da Saída referenciada\.

Vlr Unit ICMS\-ST Conv Rest \(C181\-18\)

 

44

Valor Unitário FCP ST Conv Rest

Campo da EFD correspondente: 19 do C181\.

VLR\_UNIT\_FCP\_REST\_SAI

Campo referente ao estorno de Complemento FECEP, logo deve ser preenchido no caso da saída referenciada tenha sido objeto de Complemento\.

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher com o Valor do estorno da Complementação FECEP\.

Vide “[Regra p/ Operação de Saída Interna p/ Consumidor Final](#COMPL_FECEP_CONS_FINAL)”\(\*\)\.

\[__MFS58042/ MFS59698\]__

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com Zero\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

Preencher com Zero\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com Zero\.

<a id="COMPL_FECEP_CONS_FINAL"></a>\(\*\)Regra p/ Operação de Saída Interna p/ Consumidor Final:

__\[MFS\-63471\]__ Não utilizar as bases \(BC\-Entrada e BC\-Saída\) na comparação para identificar se houve ressarcimento ou complemento\. Usar os próprios valores de ICMS e ICMS\-ST de Saída e Entrada\.

Se \(BC\-Entrada\) < \(BC\-Saída\) então:

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_UNIT\_ICMS\_OPER\_SAI < 0 \(entrada < saída = complemento\) então:

   Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMSS\_REST\_SAI \* Alíquota FCP / 100

Onde:

- VLR\_UNIT\_ICMSS\_REST\_SAI: valor gravado no campo 43\-Valor Unitário ICMS ST Conv Rest;
- Alíquota FCP da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na __Data de Emissão da Saída__ referenciada;

Ver [Detalhamento da Parametrização por Produto](#Detalha_Parametrização_Produto)

Senão:

   Não preencher

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

Vlr Unit FCP\-ST Conv Rest \(C181\-19\)

 

45

Valor Unitário ICMS ST Conv Compl

Campo da EFD correspondente: 20 do C181\.

VLR\_UNIT\_ICMSS\_COMPL\_SAI

Campo referente ao estorno de Restituição, logo deve ser preenchido no caso da saída referenciada tenha sido objeto de Restituição\.

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher com o Valor do estorno da Restitiução\.

Vide “[Regra p/ Operação de Saída Interna p/ Consumidor Final](#REST_CONS_FINAL)”\(\*\)\.

\[__MFS58042/ MFS59698\]__

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com o Valor do estorno da Restitiução\.

Vide “[Regra p/ Operação de Outra UF, Exportação, Nova ST, Isenção](#REST_OUT_UF)”\(\*\*\)\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

Preencher com Zero\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com Zero\.

<a id="REST_CONS_FINAL"></a>\(\*\)Regra p/ Operação de Saída Interna p/ Consumidor Final:

__\[MFS\-63471\]__ Não utilizar as bases \(BC\-Entrada e BC\-Saída\) na comparação para identificar se houve ressarcimento ou complemento\. Usar os próprios valores de ICMS e ICMS\-ST de Saída e Entrada\.

Se \(BC\-Entrada\) > \(BC\-Saída\) então:

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_UNIT\_ICMS\_OPER\_SAI > 0 \(entrada > saída = ressarcimento\) então:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ 

    VLR\_UNIT\_ICMSS\_ESTQ\_SAI – 

    VLR\_UNIT\_ICMS\_OPER\_SAI  

    Onde:

- VLR\_UNIT\_ICMS\_OPER\_SAI: valor gravado no campo 42\-Valor Unitário ICMS na Operação Conv;
- VLR\_UNIT\_ICMS\_ESTQ\_SAI : valor gravado no campo 39\- Valor Unitário ICMS OP Estoque Conv;
- VLR\_UNIT\_ICMSS\_ESTQ\_SAI: valor gravado no campo 40\-Valor Unitário ICMS ST Estoque Conv;

Senão:

   Não preencher

Onde:

- \(BC\-Entrada\):

“Valor Médio Unitário da Base de Cálculo do ICMS\-ST \([BC\-Entrada](#BC_Entrada)\)”\.

Ver [*Dados para o Cálculo da Média Pondera Móvel dos Valores Unitários*](#Detalha_Media_ponderada)

- \(BC\-Saída\): 

Para Nota Fiscal de saída referenciada pela devolução \(vide [2\.1](#_2.1_–_Recuperação)\):

 “Valor Unitário da BC do ICMS na Operação Conv \([BC\-Saída](#BC_SAIDA_NF_SAI)\)”

 Ver  [*Detalhamento da Nota de Saída Referenciada pela Devolução*](#Detalha_NF_SAI)\.

       Para Cupom Fiscal de saída referenciado pela devolução \(vide [2\.2](#_2.2_–_Recuperação)\):

         “Valor Unitário da BC do ICMS na Operação Conv Cupom Fiscal \([BC\-Saída](#BC_SAIDA_CUPOM_SAI)\)”

          Ver *[Detalhamento do Cupom Fiscal Referenciado pela Devolução](#Detalha_CUPOM_SAI)*

<a id="REST_OUT_UF"></a>\(\*\*\)Regra p/ Operação de Outra UF, Exportação, Nova ST, Isenção:

    Preencher com o resultado da formula:

    VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ 

    VLR\_UNIT\_ICMSS\_ESTQ\_SAI 

    Onde:

- VLR\_UNIT\_ICMS\_ESTQ\_SAI: valor gravado no campo 39\- Valor Unitário ICMS OP Estoque Conv;
- VLR\_UNIT\_ICMSS\_ESTQ\_SAI: valor gravado no campo 40\-Valor Unitário ICMS ST Estoque Conv;

Validação:

Caso o valor gravado no campo seja negativo, exibir mensagem de aviso no log:

*“Registro C181: Nota de Saída gerada com valor unitário do complemento negativo\.”*

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Saída e da Saída referenciada\.

Vlr Unit ICMS\-ST Conv Compl \(C181\-20\)

 

46

Valor Unitário FCP ST Conv Compl

Campo da EFD correspondente: 21 do C181\.

VLR\_UNIT\_FCP\_COMPL\_SAI

Campo referente ao estorno de Restituição FECEP, logo deve ser preenchido no caso da saída referenciada tenha sido objeto de Restituição\.

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher com o Valor do estorno da Restitiução FECEP\.

Vide “[Regra p/ Operação de Saída Interna p/ Consumidor Final](#FECEP_CONS_FINAL)”\(\*\)\.

\[__MFS58042/ MFS59698\]__

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com o Valor do estorno da Restitiução FECEP\.

Vide “[Regra p/ Operação de Outra UF, Exportação, Nova ST, Isenção](#FECEP_OUT_UF)”\(\*\*\)\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

Preencher com Zero\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com Zero\.

<a id="FECEP_CONS_FINAL"></a>\(\*\)Regra p/ Operação de Saída Interna p/ Consumidor Final:

__\[MFS\-63471\]__ Não utilizar as bases \(BC\-Entrada e BC\-Saída\) na comparação para identificar se houve ressarcimento ou complemento\. Usar os próprios valores de ICMS e ICMS\-ST de Saída e Entrada\.

Se \(BC\-Entrada\) > \(BC\-Saída\) então:

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_UNIT\_ICMS\_OPER\_SAI > 0 \(entrada > saída = ressarcimento\) então:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMSS\_COMPL\_SAI \* Alíquota FCP / 100

    Onde:

- VLR\_UNIT\_ICMSS\_COMPL\_SAI: valor gravado no campo 45\-Valor Unitário ICMS ST Conv Compl;
- Alíquota FCP da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na __Data de Emissão da Saída__ referenciada;

Ver [Detalhamento da Parametrização por Produto](#Detalha_Parametrização_Produto)

Senão:

   Não preencher

<a id="FECEP_OUT_UF"></a>\(\*\*\)Regra p/ Operação de Outra UF, Exportação, Nova ST, Isenção:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMSS\_COMPL\_SAI \* Alíquota FCP / 100

    Onde:

- VLR\_UNIT\_ICMSS\_COMPL\_SAI: valor gravado no campo 45\-Valor Unitário ICMS ST Conv Compl;
- Alíquota FCP da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na __Data de Emissão da Saída__ referenciada;

Ver [Detalhamento da Parametrização por Produto](#Detalha_Parametrização_Produto)

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

Vlr Unit FCP\-ST Conv Compl \(C181\-21\)

<a id="Detalha_Parametrização_Produto"></a>__*Parametrização do Produto \(por Código, NCM ou CEST\)*__

Produto da NF de Devolução

GRUPO\_PROD\_NF\_DEV

IND\_PROD\_NF\_DEV

COD\_PROD\_NF\_DEV

Produto do item da nota de devolução\.

Ind Produto

\(SAFX2013\-01\)

Cod Produto \(SAFX2013\-02\)

Unidade de Medida do Produto NF de Devolução

COD\_MEDIDA\_PROD\_NF\_DEV

Unidade de Medida do Produto da nota de Devolução \(SAFX2013 – campo 14 – COD\_MEDIDA\)

Medida Produto \(SAFX2013\-14\)

NCM do Produto NF de Devolução

COD\_NBM\_PROD\_NF\_DEV

Código NBM do Produto da nota de Devolução \(SAFX2013 – campo 05 – Código NBM\)

NCM Produto \(SAFX2013\-05\)

CEST do Produto NF de Devolução

COD\_CEST\_PROD\_NF\_DEV

Código CEST do Produto da nota de Devolução \(SAFX2013 – campo 54 – Código Especificador da Substituição Tributária\)

CEST Produto \(SAFX2013\-54\)

Produto Principal

GRUPO\_PROD\_PRINC

IND\_PROD\_PRINC

COD\_PROD\_PRINC

Caso o produto do item da nota de devolução tenha sido parametrizado por Código \(menu “Parâmetros à Produtos à Por Código”\) apresentar o Produto Principal \(grupo, indicador e código\)\.

Não Apresentar

Unidade de Medida do Produto Principal

COD\_MEDIDA\_PROD\_PRINC

Caso o produto do item da nota de devolução tenha sido parametrizado por Código \(menu “Parâmetros à Produtos à Por Código”\) apresentar a Unidade de Medida do Produto Principal \(SAFX2013 – campo 14 – COD\_MEDIDA\)\.

Não Apresentar

%Redução BC

PRC\_REDUCAO\_BC

%Redução BC da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na __Data de Emissão da Saída__ referenciada;

__Atenção__: para busca da Alíquota Interna, Alíquota FCP e %Redução de BC, considerar a parametrização vigente __na Data de Emissão da NF \(Cupom\) de Saída__ e não a vigente no período da geração\.

Isso porque os cálculos devem bater com os valores apresentados no C185 dessa nota \(cupom\) de saída\.

Caso não seja encontradada parametrização do Produto \(menu “Parâmetros à Produtos à Por Código”, ou, “Parâmetros à Produtos à Por NCM”, ou “Parâmetros à Produtos à Por CEST\), exibir a seguinte mensagem:

__\[MFS61955\]__

 “*Registro C181: Não foi encontrada Parametrização por Código, NCM ou Cest para o produto da Nota de Devolução de Saída, vigente na Data de Emissão da  Saída <DD/MM/AAAA>\. Sem a definição da Alíquota Interna o registro C181 será gerado sem valor unitário de ICMS \(campo 16\)”\.*

Onde: DD/MM/AAAA é a Data de Emissão da NF \(ou cupom\) de Saída\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Saída e da Saída referenciada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\) __\[MFS61955\] __Caso a saída referenciada pela devolução seja um cupom fiscal \(SAFX994\) \(vide [2\.2](#_2.2_–_Recuperação)\) informar Número do Caixa \(campo 04 SAFX994\), COO \(campo 05 SAFX994\), Data da emissão\(campo 06 SAFX994\)\.

%Redução BC \(Parametrização Produto\)

Alíquota Interna

ALIQ\_INTERNA

Alíquota Interna da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na __Data de Emissão da Saída __referenciada;

Alíq\. Interna \(Parametrização Produto\)

Alíquota FCP

ALIQ\_FCP

Alíquota FCP da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na __Data de Emissão da Saída__ referenciada;

Alíq\. FCP \(Parametrização Produto\)

<a id="Detalha_NF_DEV"></a>__*Detalhamento da Nota de Devolução recuperada nos tópicos [2\.0](#_2.0_–_Recuperação)*__

Quantidade da NF de Devolução de Saída 

\(safx08 – item 24\)

QTD\_NF\_DEV

Campo 24\-Quantidade \(SAFX08\) do item da nota de Devolução de saída, recuperada no tópico [2\.0](#_2.0_–_Recuperação)

Qtde Item NF Devolução \(SAFX08\-24\)

Quantidade Convertida da NF de Devolução de Saída \(safx08 – item137\)

QTD\_CONV\_X08\_NF\_DEV

Campo 137 – Quantidade Convertida \(SAFX08\) do item da nota de Devolução de saída, recuperada no tópico [2\.0](#_2.0_–_Recuperação)

Qtde Conv Item NF Devolução \(SAFX08\-137\)

Unidade de Medida da NF de Devolulção de Saída \(safx08 \- item 25\)

COD\_MEDIDA\_NF\_DEV

Campo 25 – Unidade de Medida \(SAFX08\) do item da nota de Devolução de saída, recuperada no tópico [2\.0](#_2.0_–_Recuperação)

Medida Item NF Devolução \(SAFX08\-25\)

Fator Conversão da Medida da NF de Devolução de Saída p/ Medida do Produto

FAT\_CONV\_NF\_DEV

Preencher com o Fator de Conversão utilizado na regra do campo “Qtde Convertida Calculada para NF de Devolução de Saída \(QTD\_CONV\_NF\_DEV\)” a seguir\.

__Se__ unidade da nota = unidade do cadastro do produto, então:__  __

__    __Campo será preenchido com 1;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\), então:

         Campo não será preenchido;

     Senão         

           Se não encontrado Fator de Conversão nos Cadastros de Conversão de Unidades de 

           Medidas, então:

                Campo será preenchido com \-1;

           Senão

                 Campo será preenchido com o Fator de Conversão encontrado\.

Fator Conv NF Devolução \(Cadastro Conversão Medida\)

Qtde Convertida Calculada para NF de Devolução de Saída \(safx08\)

\(<a id="QTD_CONV_NF_DEV"></a>QTD\_CONV\_NF\_DEV\)

QTD\_CONV\_NF\_DEV

Campo 24\-Quantidade \(SAFX08\) do Item da nota de Devolução de Saída, aplicando a conversão, quando necessário\. Veja:

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\)  __*\(ver OBS abaixo sobre os produtos associados\)*

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria quantidade do

      item da nota;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\)

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade Convertida”;

     Senão         

         Nesse caso a quantidade do item \(SAFX08\) será convertida para a unidade de medida do cadastro do produto;

         \[ Quantidade do item da nota \(SAFX08\) \* Fator de Conversão \]

__Sobre os produtos associados:__ Quando se tratar de uma nota fiscal de produto “associado”, a comparação será feita da unidade de medida da nota, com a __unidade do produto principal__\.

Exemplo:

__Produto principal__: COCA\-COLA PET                 \(unidade de medida do estoque – SAFX2013 = UN\) 

__Produtos associados__: COCA\-COLA PET–1      \(unidade de medida do estoque – SAFX2013 = PAC \(6 unidades\)\)

Nota de venda do produto associado: __COCA\-COLA PET\-1__, unidade da nota = PAC, Quantidade = __5__

Compara a unidade de medida da nota do produto associado com a unidade de estoque do produto principal: PAC x UN

Como é diferente, deve\-se converter a quantidade da nota de PAC para UN\. 

Para acessar a tabela de conversão por produto, será utilizado o código do produto principal:

__DWT\_CONV\_MEDIDA\-2: __Produto = __COCA\-COLA PET__

                                          Unidade Origem = PAC

                                          Unidade Destino = UN

                                          Fator de conversão = 6,0000

Conversão da quantidade da nota do associado:  QTD da nota x Fator de Conversão   =  5 x 6,0000 = 30,0000 

Lembrando que, quando não existe fator na tabela de conversão por produto \(DWT\_CONV\_MEDIDA\_2\), será utilizada a tabela padrão \(DWT\_CONV\_MEDIDA\)\.  

__= = = = =__

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, será gravada a seguinte mensagem de erro no log:

“*Registro C181: Fator de conversão de medida de XXX para XXX não encontrado\. Nota de Devolução de saída será gerada no C181 sem informação no campo 03 \- Quantidade Convertida e não irá compor a Média Pondera Móvel dos Valores Unitários do dia DD/MM/YYYY”\. Favor rever medida da NF de devolução e Cadastro de Conversão de Unidades de Medida, no módulo DW, menu Manutenção >> Cadastros >> Conversão de Unidades de Medida\.”*

\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Saída e da Saída referenciada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)\. __\[MFS61955\] __Caso a saída referenciada pela devolução seja um cupom fiscal \(SAFX994\) \(vide [2\.2](#_2.2_–_Recuperação)\) informar Número do Caixa \(campo 04 SAFX994\), COO \(campo 05 SAFX994\), Data da emissão\(campo 06 SAFX994\)\.

Qtde Conv Calculada p/ NF Devolução

Quantidade da Devolução p/ Saída Referenciada \(safx192 – item 24\)

QTD\_REF\_DEV

Campo 24 \- Quantidade da Devolução \(QTD\_DEVOL\) da SAFX192, recuperada nos tópicos [2\.1](#_2.1_–_Recuperação) \(quando faz referência ao item da nota fiscal de saída\), ou [2\.2](#_2.2_–_Recuperação) \(quando faz referência ao item do cupom fiscal de saída\)\. 

Qtde Devolvida \(SAFX192\-24\)

Qtde da Devolução Convertida Calculada p/ Saída Referenciada \(safx192\)

\(<a id="QTD_CONV_REF_DEV"></a>QTD\_CONV\_REF\_DEV\)

QTD\_CONV\_REF\_DEV

Campo 24 \- Quantidade da Devolução \(QTD\_DEVOL\) da SAFX192:

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\)  __*\(ver OBS abaixo sobre os produtos associados\)*

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08 da NF Devolução da Saída \(reg pai\)

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria Quantidade da Devolução da SAFX192 \(QTD\_DEVOL\);

__Senão __

         Nesse caso a quantidade da Devolução \(QTD\_DEVOL\) será convertida para a unidade de medida do cadastro do produto;

         \[Quantidade da Devolução \(SAFX192\) \* Fator de Conversão\]

__Sobre os produtos associados:__ Quando se tratar de uma nota fiscal de produto “associado”, a comparação será feita da unidade de medida da nota, com a __unidade do produto principal__\.

Exemplo:

__Produto principal__: COCA\-COLA PET                 \(unidade de medida do estoque – SAFX2013 = UN\) 

__Produtos associados__: COCA\-COLA PET–1      \(unidade de medida do estoque – SAFX2013 = PAC \(6 unidades\)\)

Nota de venda do produto associado: __COCA\-COLA PET\-1__, unidade da nota = PAC, Quantidade = __5__

Compara a unidade de medida da nota do produto associado com a unidade de estoque do produto principal: PAC x UN

Como é diferente, deve\-se converter a quantidade da nota de PAC para UN\. 

Para acessar a tabela de conversão por produto, será utilizado o código do produto principal:

__DWT\_CONV\_MEDIDA\-2: __Produto = __COCA\-COLA PET__

                                          Unidade Origem = PAC

                                          Unidade Destino = UN

                                          Fator de conversão = 6,0000

Conversão da quantidade da nota do associado:  QTD da nota x Fator de Conversão   =  5 x 6,0000 = 30,0000 

Lembrando que, quando não existe fator na tabela de conversão por produto \(DWT\_CONV\_MEDIDA\_2\), será utilizada a tabela padrão \(DWT\_CONV\_MEDIDA\)\.  

__= = = = =__

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, será gravada a seguinte mensagem de erro no log:

“*Registro C181: Fator de conversão de medida de XXX para XXX não encontrado\. Nota de Devolução de saída será gerada no C181 sem informação no campo 03 \- Quantidade Convertida e não irá compor a Média Pondera Móvel dos Valores Unitários do dia DD/MM/YYYY”\. Favor rever medida da NF de devolução e Cadastro de Conversão de Unidades de Medida, no módulo DW, menu Manutenção >> Cadastros >> Conversão de Unidades de Medida\.”*

*\(essa mensagem não precisa ser dada pois é a mesma já especificada no campo QTD\_CONV\_NF\_DEV\)*

\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Saída e da Saída referenciada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\) __\[MFS61955\] __Caso a saída referenciada pela devolução seja um cupom fiscal \(SAFX994\) \(vide [2\.2](#_2.2_–_Recuperação)\) informar Número do Caixa \(campo 04 SAFX994\), COO \(campo 05 SAFX994\), Data da emissão\(campo 06 SAFX994\)\.

Qtde Devolvida Conv Calculada \(SAFX192\-24 aplicado Fator Conv\)

<a id="Detalha_NF_SAI"></a>__*Detalhamento da Nota de Saída Referenciada pela Devolução recuperada no tópico [2\.1](#_2.1_–_Recuperação)*__

Quantidade do Item da NF de Saída Referenciada \(safx08 – item 24\)

QTD\_NF\_SAI

Campo 24\-Quantidade \(SAFX08\) do item da nota fiscal de saída referenciada, recuperada no tópico [2\.1](#_2.1_–_Recuperação)

Qtde Item NF Saída \(SAFX08\-24\)

Quantidade Convertida do Item da NF de Saída Referenciada \(safx08 – item137\)

QTD\_CONV\_X08\_NF\_SAI

Campo 137 – Quantidade Convertida \(SAFX08\) do item da nota fiscal de saída referenciada, recuperada no tópico [2\.1](#_2.1_–_Recuperação)

Qtde Conv Item NF Saída \(SAFX08\-137\)

Unidade de Medida do Item da NF de Saída Referenciada

\(safx08 \- item 25\)

COD\_MEDIDA\_NF\_SAI

Campo 25 – Unidade de Medida \(SAFX08\) do item da nota fiscal de saída referenciada, recuperada no tópico [2\.1](#_2.1_–_Recuperação)\.

Medida Item NF Saída \(SAFX08\-25\)

Fator Conversão

FAT\_CONV\_NF\_SAI

Preencher com o Fator de Conversão utilizado na regra do campo “Qtde Convertida Calculada para o Item da Nota de Saída \(QTD\_CONV\_NF\_SAI\)” a seguir\.

__Se__ unidade da nota = unidade do cadastro do produto, então:__  __

__    __Campo será preenchido com 1;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\), então:

         Campo não será preenchido;

     Senão         

           Se não encontrado Fator de Conversão nos Cadastros de Conversão de Unidades de 

           Medidas, então:

                Campo será preenchido com \-1;

           Senão

                 Campo será preenchido com o Fator de Conversão encontrado\.

Fator Conv NF Saída \(Cadastro Conversão Medida\)

Qtde Convertida Calculada para o Item da NF de Saída Referenciada

\(<a id="QTD_CONV_NF_SAI"></a>QTD\_CONV\_NF\_SAI\)

QTD\_CONV\_NF\_SAI

Campo 24\-Quantidade \(SAFX08\) do Item da nota de Saída referenciada, aplicando a conversão, quando necessário\. Veja:

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\)  __*\(ver OBS abaixo sobre os produtos associados\)*

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08 do Item da NF de Saída Referenciada

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria quantidade do

      item da nota;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\)

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade Convertida”;

     Senão         

         Nesse caso a quantidade do item \(SAFX08\) será convertida para a unidade de medida do cadastro do produto;

         \[ Quantidade do item da nota \(SAFX08\) \* Fator de Conversão \]

__Sobre os produtos associados:__ Quando se tratar de uma nota fiscal de produto “associado”, a comparação será feita da unidade de medida da nota, com a __unidade do produto principal__\.

Exemplo:

__Produto principal__: COCA\-COLA PET                 \(unidade de medida do estoque – SAFX2013 = UN\) 

__Produtos associados__: COCA\-COLA PET–1      \(unidade de medida do estoque – SAFX2013 = PAC \(6 unidades\)\)

Nota de venda do produto associado: __COCA\-COLA PET\-1__, unidade da nota = PAC, Quantidade = __5__

Compara a unidade de medida da nota do produto associado com a unidade de estoque do produto principal: PAC x UN

Como é diferente, deve\-se converter a quantidade da nota de PAC para UN\. 

Para acessar a tabela de conversão por produto, será utilizado o código do produto principal:

__DWT\_CONV\_MEDIDA\-2: __Produto = __COCA\-COLA PET__

                                          Unidade Origem = PAC

                                          Unidade Destino = UN

                                          Fator de conversão = 6,0000

Conversão da quantidade da nota do associado:  QTD da nota x Fator de Conversão   =  5 x 6,0000 = 30,0000 

Lembrando que, quando não existe fator na tabela de conversão por produto \(DWT\_CONV\_MEDIDA\_2\), será utilizada a tabela padrão \(DWT\_CONV\_MEDIDA\)\.  

__= = = = =__

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas será gravada a seguinte mensagem de erro no log:

“*Registro C181: Fator de conversão de medida de XXX para XXX não encontrado\. Nota de Devolução de saída será gerada no C181 sem valores unitários da Mercadoria e ICMS \(campos 12 e 16\)”\. Favor rever medida da NF de saída referenciada pela devolução e Cadastro de Conversão de Unidades de Medida, no módulo DW, menu Manutenção >> Cadastros >> Conversão de Unidades de Medida\.”*

\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Saída e da Saída referenciada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

Qtde Conv Calculada p/ NF Saída

Valor Contabil do Item de Saída Referencida

\(safx08 – item 64\)

VLR\_CONTAB\_SAI

Campo 64\-“Vlr Contabil do Item”\(SAFX08\) do item da nota fiscal de saída referenciada, recuperada no tópico [2\.1](#_2.1_–_Recuperação)

Vlr Contabil Item NF Saída \(SAFX08\-64\)

Amparo Legal \(safx08\- item 66\)

COD\_AMPARO\_LEGAL

__\[MFS96666\]: Inclusão dos códigos RS101, \.\.\., RS156 e RS301, \.\.\., RS356 a partir de Jan\-2023:__

Campo 66 \- Código do Amparo/Texto/Ocorrência para ICMS de Substituição Tributária do item de mercadoria da nota fiscal de saída devolvida\.

Amparo Legal \(safx08\- item 66\)

Valor Unitário da BC do ICMS na Operação Conv

\(<a id="BC_SAIDA_NF_SAI"></a>BC\-Saída\)

VLR\_BC\_ICMS\_SAI

Valor Unitário da BC do ICMS na Operação Conv, calculado conforme regra:

Se o campo “__%Redução BC__” da parametrização de Produto ou NCM ou CEST está preenchido com valor > 0, então:

  Este campo será gerado da seguinte forma:

  \[\(Vlr Contábil – \(Vlr Contábil \* “%Redução BC” / 100\)\)\]/ QTD\_CONV\_NF\_SAI

Senão:

  Este campo será gerado da seguinte forma:

  \[\(Vlr Contábil\)\] / QTD\_CONV\_NF\_SAI

Onde:

- %Redução BC da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na __Data de Emissão da Saída__ referenciada;
- Vl Contábil = 64\-Vlr Contabil do Item da nota fiscal de saída referenciada, recuperada no tópico [2\.1](#_2.1_–_Recuperação)\.
- [QTD\_CONV\_NF\_SAI](#QTD_CONV_NF_SAI): Qtde Convertida Calculada para o Item da Nota de Saída referenciada, recuperada no tópico [2\.1](#_2.1_–_Recuperação)\. 

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\)

<a id="Detalha_CUPOM_SAI"></a>__*Detalhamento de Cupom Fiscal Referenciado pela Devolução recuperado no tópico [2\.2](#_2.2_–_Recuperação)*__

Quantidade do Item do Cupom Fiscal Referenciado \(safx994 – item 16\)

QTD\_CUPOM

__\[MFS61955\]__

Campo 16\-Quantidade \(SAFX994\) do item do cupom fiscal referenciado, recuperado no tópico [2\.2](#_2.2_–_Recuperação)

Qtde Item Cupom Fiscal \(SAFX994\-16\)

Unidade de Medida do Item do Cupom Fiscal Referenciado

\(safx994 \- item 17\)

COD\_MEDIDA\_NF\_CUPOM

__\[MFS61955\]__

Campo 17\-Quantidade \(SAFX994\) do item do cupom fiscal referenciado, recuperado no tópico [2\.2](#_2.2_–_Recuperação)

Medida Item Cupom Fiscal \(SAFX994\-17\)

Fator de Conversão

FAT\_CONV\_NF\_CUPOM

__\[MFS61955\]__

Preencher com o Fator de Conversão utilizado na regra do campo “Qtde Convertida Calculada para o Item do Cupom Fiscal \(QTD\_CONV\_CF\)” a seguir\.

__Se__ unidade do cupom = unidade do cadastro do produto, então:__  __

__    __Campo será preenchido com 1;

__Senão __

           Se não encontrado Fator de Conversão nos Cadastros de Conversão de 

           Unidades de Medidas, então:

                Campo será preenchido com \-1;

           Senão

                 Campo será preenchido com o Fator de Conversão encontrado\.

Fator Conv Cupom Fiscal \(Cadastro Conversão Medida\)

Qtde Convertida Calculada para o Item do Cupom Fiscal

\(<a id="QTD_CONV_CF"></a>QTD\_CONV\_CF\)

QTD\_CONV\_NF\_CUPOM

__\[MFS61955\]__

Campo 16\-Quantidade \(SAFX994\) do item do cupom fiscal referenciado, aplicando a conversão, quando necessário\. Veja:

__Se__ unidade do cupom __\(\*\)__ = unidade do cadastro do produto __\(\*\*\) __*\(ver OBS abaixo sobre os produtos associados\)*

      __\(\*\)__ unidade do cupom = campo “17\-Unidade de Medida” da SAFX994 do Item do

           Cupom fiscal referenciado

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria

      quantidade do item do cupom fiscal;

__Senão __

       Nesse caso a quantidade do item do cupom fiscal \(SAFX994\) será convertida

       para a unidade de medida do cadastro do produto;

         \[Quantidade do item Cupom Fiscal \(SAFX994\) \* Fator de Conversão\]

__Sobre os produtos associados:__ Quando se tratar de um cupom fiscal de produto “associado”, a comparação será feita da unidade de medida do cupom, com a __unidade do produto principal__\.

Exemplo:

__Produto principal__: COCA\-COLA PET                 \(unidade de medida do estoque – SAFX2013 = UN\) 

__Produtos associados__: COCA\-COLA PET–1      \(unidade de medida do estoque – SAFX2013 = PAC \(6 unidades\)\)

Cupom de venda do produto associado: __COCA\-COLA PET\-1__, unidade do cupom = PAC, Quantidade = __5__

Compara a unidade de medida do cupom do produto associado com a unidade de estoque do produto principal: PAC x UN

Como é diferente, deve\-se converter a quantidade da nota de PAC para UN\. 

Para acessar a tabela de conversão por produto, será utilizado o código do produto principal:

__DWT\_CONV\_MEDIDA\-2: __Produto = __COCA\-COLA PET__

                                          Unidade Origem = PAC

                                          Unidade Destino = UN

                                          Fator de conversão = 6,0000

Conversão da quantidade do cupom do associado:  QTD do cupom x Fator de Conversão   =  5 x 6,0000 = 30,0000 

Lembrando que, quando não existe fator na tabela de conversão por produto \(DWT\_CONV\_MEDIDA\_2\), será utilizada a tabela padrão \(DWT\_CONV\_MEDIDA\)\.  

__= = = = =__

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas será gravada a seguinte mensagem de erro no log:

“*Registro C181: Fator de conversão de medida de XXX para XXX não encontrado\. Nota de Devolução de saída será gerada no C181 sem valores unitários da Mercadoria e ICMS \(campos 12 e 16\)”\. Favor rever medida do Cupom Fiscal de saída referenciado pela devolução e Cadastro de Conversão de Unidades de Medida, no módulo DW, menu Manutenção >> Cadastros >> Conversão de Unidades de Medida\.”*

\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Saída e da Saída referenciada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)__ \[MFS61955\] __Como a saída referenciada pela devolução é um cupom fiscal \(SAFX994\), informar Número do Caixa \(campo 04 SAFX994\), COO \(campo 05 SAFX994\) e Data da emissão\(campo 06 SAFX994\)\.

Qtde Conv Calculada p/ Cupom Fiscal \(SAFX994\-16 aplicado Fator Conv\)

Valor total líquido do Item do Cupom Fiscal

\(safx994 – item 22\)

VLR\_CONTAB\_CUPOM

__\[MFS61955\]__

Campo 22\-Valor Total Líquido \(SAFX994\) do item do cupom fiscal referenciado, recuperado no tópico [2\.2](#_2.2_–_Recuperação)

Vlr Líquido Item Cupom Fiscal \(SAFX994\-22\)

Amparo Legal \(safx994\- item 45\)

COD\_AMPARO\_LEGAL

__\[MFS96666\]: Inclusão dos códigos RS101, \.\.\., RS156 e RS301, \.\.\., RS356 a partir de Jan\-2023:__

“Código do Amparo/Texto/Ocorrência” do item do Cupom Fiscal devolvido \(item 45 – COD\_AMPARO\_LEGAL da SAFX994\)\.

Amparo Legal \(safx994\- item 45\)

Valor Unitário da BC do ICMS na Operação Conv Cupom Fiscal

\(<a id="BC_SAIDA_CUPOM_SAI"></a>BC\-Saída\)

VLR\_BC\_ICMS\_CUPOM

__\[MFS61955\]__

Valor Unitário da BC do ICMS na Operação Conv, calculado conforme regra:

Se o campo “__%Redução BC__” da parametrização de Produto ou NCM ou CEST está preenchido com valor > 0, então:

     Este campo será gerado da seguinte forma:

     \[\(Vlr Liq Item – \(Vlr Liq Item \* “%Redução BC” / 100\)\)\]/ QTD\_CONV\_CF

Senão:

      Este campo será gerado da seguinte forma:

      \[\(Vlr Liq Item\)\] / QTD\_CONV\_CF

Onde:

- %Redução BC da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na __Data de Emissão do cupom __referenciado;
- Vlr Liq Item = 22 \- Vlr Total Líquido do Item do cupom referenciado, recuperado no tópico [2\.2](#_2.2_–_Recuperação)\.
- [QTD\_CONV\_CF](#QTD_CONV_CF): Qtde Convertida Calculada para o Item do cupom fiscal referenciado, recuperado no tópico [2\.2](#_2.2_–_Recuperação)\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

Vlr Unit BC ICMS Operação Conv \(Vlr Líquido Item Cupom c/ %Redução BC\)

__*Valores Unitários da Média Pondera Móvel do dia da operação de saída \(recuperada no passo 1 do tópico [2\.3](#_2.3_–_Recuperação)\.\)*__

Valor Médio Unitário do ICMS no dia Saída \(Tabela de Média Diária\)

VLR\_UNIT\_ICMS\_SAI

“Valor Médio Unitário do ICMS” recuperado no passo 1 do tópico [2\.3](#_2.3_–_Recuperação)\.  

Campo VLR\_UNIT\_ICMS\_FIM\_MP da EST\_ST\_RS\_MEDIA\_POND\.

__\[MFS90131\]__ mantém com 8 casas decimais o valor médio unitário recuperado da Média Ponderada\. Campo utilizado apenas para o relatório de conferência\.

Vlr Unit ICMS \(Recuperado da Média Ponderada na ocasião da Emissão da Saída\)

Valor Médio Unitário do ICMS\-ST s/ FECEP no dia Saída \(Tabela de Média Diária\)

VLR\_UNIT\_ICMS\_ST\_SAI

__\[MFS66171\]__

“Valor Médio Unitário do ICMS\-ST s/ FECEP” recuperado no passo 1 do tópico [2\.3](#_2.3_–_Recuperação)\.

Campo VLR\_UNIT\_ICMS\_ST\_FIM\_MP da EST\_ST\_RS\_MEDIA\_POND\.

__\[MFS90131\]__ mantém com 8 casas decimais o valor médio unitário recuperado da Média Ponderada\. Campo utilizado apenas para o relatório de conferência\.

Vlr Unit ICMS\-ST\(s/ FECEP\-ST\) \(Recuperado da Média Ponderada na ocasião da Emissão da Saída\)

Valor Médio Unitário do ICMS\-ST c/ FECEP no dia Saída \(Tabela de Média Diária\)

VLR\_UNIT\_ICMS\_ST\_FECEP\_SAI

__\[MFS66171__\]

“Valor Médio Unitário do ICMS\-ST c/ FECEP” recuperado no passo 1 do tópico [2\.3](#_2.3_–_Recuperação)\.

Campo VLR\_UNIT\_ICMS\_ST\_FECEP\_FIM\_MP da EST\_ST\_RS\_MEDIA\_POND\.

__\[MFS90131\]__ mantém com 8 casas decimais o valor médio unitário recuperado da Média Ponderada\. Campo utilizado apenas para o relatório de conferência\.

Vlr Unit ICMS\-ST\(c/ FECEP\-ST\) \(Recuperado da Média Ponderada na ocasião da Emissão da Saída\)

Valor Médio Unitário da Base de Cálculo do ICMS\-ST no dia Saída \(Tabela de Média Diária\)

VLR\_UNIT\_BC\_ST\_SAI

“Valor Médio Unitário da Base de Cálculo do ICMS\-ST” recuperado no passo 1 do tópico [2\.3](#_2.3_–_Recuperação)\.

Campo VLR\_UNIT\_BC\_ST\_FIM\_MP da EST\_ST\_RS\_MEDIA\_POND\.

__\[MFS90131\]__ mantém com 8 casas decimais o valor médio unitário recuperado da Média Ponderada\. Campo utilizado apenas para o relatório de conferência\.

Vlr Unit BC ICMS\-ST \(Recuperado da Média Ponderada na ocasião da Emissão da Saída\)

Valor Médio Unitário do FECEP\-ST no dia Saída \(Tabela de Média Diária\)

VLR\_UNIT\_FECEP\_ST\_SAI

“Valor Médio Unitário do FECEP\-ST” recuperado no passo 1 do tópico [2\.3](#_2.3_–_Recuperação)\.

Campo VLR\_UNIT\_FECEP\_ST\_FIM\_MP da EST\_ST\_RS\_MEDIA\_POND\.

__\[MFS90131\]__ mantém com 8 casas decimais o valor médio unitário recuperado da Média Ponderada\. Campo utilizado apenas para o relatório de conferência\.

Vlr Unit FECEP\-ST \(Recuperado da Média Ponderada na ocasião da Emissão da Saída\)

<a id="Detalha_ULT_NF_ENT"></a>__*Dados da Última Nota Fiscal de Entrada \(recuperada no passo 2 do tópico [2\.3](#_2.3_–_Recuperação)\.\)*__

Número Última Entrada

NUM\_DOCFIS\_NF\_ENT

Número da NF Última Entrada recuperada no passo 2 do tópico [2\.3](#_2.3_–_Recuperação)\.

\(SAFX07 – campo 08 \- NUM\_DOCFIS\)  

Num Docfis NF Última Entrada

Série NF Última Entrada

SERIE\_DOCFIS\_NF\_ENT

Série da NF Última Entrada recuperada no passo 2 do tópico [2\.3](#_2.3_–_Recuperação)\.  

\(SAFX07 – campo 09 \- SERIE\_DOCFIS\)  

Serie NF Última Entrada

Subsérie NF Última Entrada

SUB\_SERIE\_DOCFIS\_NF\_ENT

Subsérie da NF Última Entrada recuperada no passo 2 do tópico [2\.3](#_2.3_–_Recuperação)\.  

\(SAFX07 – campo 10 – SUB\_SERIE\_DOCFIS\)

SubSerie NF Última Entrada

Data Fiscal NF Última Entrada

DATA\_FISCAL\_NF\_ENT

Data Fiscal da NF Última Entrada recuperada no passo 2 do tópico [2\.3](#_2.3_–_Recuperação)\.  

\(SAFX08 – campo 03 \- DATA\_FISCAL\)

Dt Fiscal NF Última Entrada

Num Item NF Última Entrada

NUM\_ITEM\_NF\_ENT

Número do Item da NF Última Entrada recuperada no passo 2 do tópico [2\.3](#_2.3_–_Recuperação)\.  

\(SAFX08 – campo 18 – NUM\_ITEM\)

Num Item NF Última Entrada

Quantidade do Item da NF Última Entrada \(safx08 – item 24\)

QTD\_NF\_ENT

Quantidade do Item da NF Última Entrada recuperada no passo 2 do tópico [2\.3](#_2.3_–_Recuperação)\.  

\(SAFX08 \- campo 24 \- QUANTIDADE\)

Qtde Item NF Última Entrada \(SAFX08\-24\)

Quantidade Convertida do Item da NF Última Entrada \(safx08 – item137\)

QTD\_CONV\_X08\_NF\_ENT

Quantidade Convertida do Item da NF Última Entrada recuperada no passo 2 do tópico [2\.3](#_2.3_–_Recuperação)\.  

\(SAFX08 \- campo 137 \- QUANTIDADE\_CONV\)

Qtde Conv Item NF Última Entrada \(SAFX08\-137\)

Unidade de Medida do Item da NF Última Entrada \(safx08 \- item 25\)

COD\_MEDIDA\_NF\_ENT

Unidade de Medida do Item da NF Última Entrada recuperada no passo 2 do tópico [2\.3](#_2.3_–_Recuperação)\.  

\(SAFX08 \- campo 25 – COD\_MEDIDA\)

Medida Item NF Última Entrada \(SAFX08\-25\)

Fator Conversão Parametrizado

FAT\_CONV\_NF\_ENT

Preecher com o Fator de Conversão utilizado na regra do campo “Qtde Convertida Calculada para o Item da NF Última Entrada \(QTD\_CONV\_NF\_ENT\)” a seguir\.

__Se__ unidade da nota = unidade do cadastro do produto, então:__  __

__    __Campo será preenchido com 1;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\), então:

         Campo não será preenchido;

     Senão         

           Se não encontrado Fator de Conversão nos Cadastros de Conversão de Unidades de 

           Medidas, então:

                Campo será preenchido com \-1;

           Senão

                 Campo será preenchido com o Fator de Conversão encontrado\.

Fator Conv NF Última Entrada \(Cadastro Conversão Medida\)

Qtde Convertida Calculada para o Item da NF Última Entrada 

<a id="QTD_CONV_NF_ENT"></a>QTD\_CONV\_NF\_ENT

Campo 24\-Quantidade do Item da NF Última Entrada, aplicando a conversão, quando necessário\. Veja:

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\)  __*\(ver OBS abaixo sobre os produtos associados\)*

   __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08 da NF de entrada

 __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

  Nesse caso não há necessidade de conversão, e o campo será gerado a própria quantidade do item da nota;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\)

         Nesse caso, será utilizada a informação da quantidade já convertida do 

         campo “137\-Quantidade Convertida”;

     Senão         

         Nesse caso a quantidade do item \(SAFX08\) será convertida para a unidade 

         de medida do cadastro do produto;

         \[ Quantidade do item da nota \(SAFX08\) \* Fator de Conversão \]

__Sobre os produtos associados:__ Quando se tratar de uma nota fiscal de produto “associado”, a comparação será feita da unidade de medida da nota, com a __unidade do produto principal__\.

Exemplo:

__Produto principal__: COCA\-COLA PET                 \(unidade de medida do estoque – SAFX2013 = UN\) 

__Produtos associados__: COCA\-COLA PET–1      \(unidade de medida do estoque – SAFX2013 = PAC \(6 unidades\)\)

Nota de venda do produto associado: __COCA\-COLA PET\-1__, unidade da nota = PAC, Quantidade = __5__

Compara a unidade de medida da nota do produto associado com a unidade de estoque do produto principal: PAC x UN

Como é diferente, deve\-se converter a quantidade da nota de PAC para UN\. 

Para acessar a tabela de conversão por produto, será utilizado o código do produto principal:

__DWT\_CONV\_MEDIDA\-2: __Produto = __COCA\-COLA PET__

                                          Unidade Origem = PAC

                                          Unidade Destino = UN

                                          Fator de conversão = 6,0000

Conversão da quantidade da nota do associado:  QTD da nota x Fator de Conversão   =  5 x 6,0000 = 30,0000 

Lembrando que, quando não existe fator na tabela de conversão por produto \(DWT\_CONV\_MEDIDA\_2\), será utilizada a tabela padrão \(DWT\_CONV\_MEDIDA\)\.  

__= = = = =__

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o item da nota será gerado com o campo Quantidade da Saída sem informação, e será gravada a seguinte mensagem de erro no log:

“*Registro C181: Fator de conversão de medida de XXX para XXX não encontrado\. Nota de Devolução de saída será gerada no C181 sem valores unitários de ICMS, ICMS\-ST e FCP Estoque Conv \(campos 13, 14 E 15\) e não irá compor Média Pondera Móvel dos Valores Unitários do dia DD/MM/YYYY”\. Favor rever medida da NF de Entrada e Cadastro de Conversão de Unidades de Medida, no módulo DW, menu Manutenção >> Cadastros >> Conversão de Unidades de Medida\.”*

* *\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto e DD/MM/YYYY é Data Fiscal da Nota de Devolução da Saída\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Saída, da Nota de Saída referenciada e da Nota de Entrada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)__ \[MFS61955\] __Como a saída referenciada pela devolução é um cupom fiscal \(SAFX994\), informar Número do Caixa \(campo 04 SAFX994\), COO \(campo 05 SAFX994\) e Data da emissão\(campo 06 SAFX994\)\.

Qtde Conv Calculada p/ NF Última Entrada

Valor do ICMS do Item da NF Última Entrada \(safx08 – itens 43, 80 ou 225\)

VLR\_ICMS\_NF\_ENT

Valor do ICMS do Item da NF Última Entrada, recuperado no passo 2 \- tópico [2\.3](#_2.3_–_Recuperação)\.  

Valor do ICMS oriundo de um dos três campos SAFX08, dependendo de qual esteja preenchido:

   Campo “43\-Valor ICMS”, se preenchido, ou

       Campo “80\-ICMS não Escriturado”, se preenchido, ou

            Campo “225\-Valor ICMS Não Destacado”  

Vlr ICMS Item NF Última Entrada \(SAFX08\-43,80,225\)

Valor do ICMS\-ST do Item da NF Última Entrada \(safx08 – itens 52, 145, 133 ou 107\)

VLR\_ICMS\_ST\_NF\_ENT

Valor do ICMS\-ST do Item da NF Última Entrada, recuperado no passo 2 \- tópico [2\.3](#_2.3_–_Recuperação)\.  

Valor do ICMS\-ST oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

     Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

   Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                    “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

        Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

   Senão:

     Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                      “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então:

          Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

     Senão:

       Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                        “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, então:

                    Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

Vlr ICMS\-ST Item NF Última Entrada \(SAFX08\-52,145,133,107\)

Valor da Base de Cálculo do ICMS\-ST do Item da NF Última Entrada \(safx08 – itens 61, 144, ou 106\)

VLR\_BC\_ST\_NF\_ENT

Valor da Base de Cálculo do ICMS\-ST do Item da NF Última Entrada recuperado no passo 2 do tópico [2\.3](#_2.3_–_Recuperação)\.

Valor da Base de Cálculo do ICMS\-ST é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor da BC\-ST = 61\-BASE\_SUB\_TRIB\_ICMS\.

Senão: 

   Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

        Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

   Senão:

      Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                       “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então:

            Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

      Senão:

         Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e

                          “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, então:

               Valor da BC\-ST = 106 \- VLR\_BASE\_ICMS\_ORIG

Vlr BC ICMS\-ST Item NF Última Entrada \(SAFX08\-61,144,106\)

Valor do FECEP\-ST do Item da NF Última Entrada \(safx08 – itens 61, 144, ou 106\)

VLR\_FECEP\_ST\_NF\_ENT

Campo 140\-FECEP ICMS\-ST \(SAFX08\) do Item da NF Última Entrada recuperado no passo 2 do tópico [2\.3](#_2.3_–_Recuperação)\.

Vlr FECEP\-ST Item NF Última Entrada \(SAFX08\-144\)

<a id="Detalha_Media_ponderada"></a>__*Dados para o “Cálculo da Média Pondera Móvel dos Valores Unitários” alínea “b” do 19\.3\-A\.2\.2 da IN\-RE 087/20*__

Quantidade Devolvida Convertida \(a\)

QTD\_CONV\_DEV\_SAI\_MP

__Igual ao campo 32 – Quantidade Convertida \(QTD\_CONV\)__

Se a saída referenciada pela devolução for uma Nota Fiscal \(vide [2\.1](#_2.1_–_Recuperação)\), então:

- Caso a nota fiscal de saída esteja associada à nota de Devolução pela __SAFX192__:

Preencher com:

“Qtde da Devolução Convertida Calculada p/ Saída Referenciada \(safx192\) \([QTD\_CONV\_REF\_DEV](#QTD_CONV_REF_DEV)\)” 

- Caso a nota de saída esteja associada à nota de devolução pela __SAFX08__:

Preencher com:

“Qtde Convertida Calculada para NF de Devolução de Saída \(safx08\) \([QTD\_CONV\_NF\_DEV](#QTD_CONV_NF_DEV)\)”

__\[MFS61955\]__

Se a saída referenciada pela devolução for um Cupom Fiscal \(vide [2\.2](#_2.2_–_Recuperação)\), então:

    Preencher com:

    “Qtde da Devolução Convertida Calculada p/ Saída Referenciada \(safx192\) 

    \([QTD\_CONV\_REF\_DEV](#QTD_CONV_REF_DEV)\)”

Ver __*[Detalhamento da Nota de Devolução](#Detalha_NF_DEV)*__

Não Apresentar pois já é o campo Qtde Conv \(C181\-03\)

Valor Médio Unitário do ICMS \(b\)

VLR\_UNIT\_ICMS\_DEV\_SAI\_MP

__Igual ao campo 39 \- Valor Unitário ICMS OP Estoque Conv \(VLR\_UNIT\_ICMS\_ESTQ\_SAI\)__

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher conforme Regra do Valor Médio Unitário do ICMS \(\*\)

       __\[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:__

       Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST”  

       \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no tópico [2\.3](#_2.3_–_Recuperação) __Passo 1__ for negativo, 

        então:

          Desconsiderar a regra acima e preencher este campo com ZERO\.

\[__MFS58042/ MFS59698\]__

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher conforme Regra do Valor Médio Unitário do ICMS \(\*\)

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

__\[MFS96666\]: RS5xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

  Preencher conforme Regra do Valor Médio Unitário do ICMS \(\*\)\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

__\[MFS96666\]: RS5xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

  Preencher conforme Regra do Valor Médio Unitário do ICMS \(\*\)\.

\(\*\) Regra do Valor Médio Unitário do ICMS: 

Preencher com o “Valor Médio Unitário do ICMS” recuperado do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\), para o Produto na Data de Emissão da nota \(ou cupom\) de saída referenciada\. 

Caso não seja encontrada, considerar a última nota de entrada do produto anterior à saída e calcular o valor unitário do ICMS\. Para isso, executar:

__Se__ a consulta realizada no __Passo 1__ do tópico [2\.3](#_2.3_–_Recuperação) retornar registro, então:

    Preencher com: \[“Valor Médio Unitário do ICMS”\] do

   “Cálculo da Média Pondera Móvel dos Valores Unitários” 

    \(campo VLR\_UNIT\_ICMS\_FIM\_MP da EST\_ST\_RS\_MEDIA\_POND\);

__Senão__:

      Se a consulta realizada no __Passo 2__ do tópico [2\.3](#_2.3_–_Recuperação) retornar registro, então:

           Calcular o Valor Unitário do ICMS com base na Última Nota de Entrada\.

           Veja Regra de Preenchimento \(\*\) descrita a seguir\.

\(\*\) Regra de Preenchimento:

Preencher com:

 Valor do ICMS / QTD\_CONV\_NF\_ENT 

Onde os valores são oriundos do item da Última Nota de Entrada:

- Valor do ICMS é oriundo de um dos três campos SAFX08, dependendo de qual esteja preenchido:

Campo “43\-Valor ICMS”, se preenchido, ou

   Campo “80\-ICMS não Escriturado”, se preenchido, ou

       Campo “225\-Valor ICMS Não Destacado”  

- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF Última Entrada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  __*[Detalhamento da Ùltima Nota Fiscal de Entrada](#Detalha_ULT_NF_ENT)*__\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ arredondar para 6 casas decimais o valor médio unitário recuperado da Média Ponderada pois compõe o layout do C181\.

Vlr Unit ICMS \(p/ Cálculo da Média Ponderada\)

Valor Médio Unitário do ICMS\-ST \(c\)

VLR\_UNIT\_ICMS\_ST\_DEV\_SAI\_MP

__Não é igual ao campo 40 \- Valor Unitário ICMS ST Estoque Conv \(VLR\_UNIT\_ICMSS\_ESTQ\_SAI\)__

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher conforme Regra do Valor Médio Unitário do ICMS\-ST \(\*\)

__       \[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:__

       Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST”  

       \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no tópico [2\.3](#_2.3_–_Recuperação) __Passo 1__ for negativo, 

        então:

          Desconsiderar a regra acima e preencher este campo com ZERO\.

\[__MFS58042/ MFS59698\]__

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher conforme Regra do Valor Médio Unitário do ICMS\-ST \(\*\)

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

__\[MFS96666\]: RS5xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

  Preencher conforme Regra do Valor Médio Unitário do ICMS\-ST \(\*\)\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

__\[MFS96666\]: RS5xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

  Preencher conforme Regra do Valor Médio Unitário do ICMS\-ST \(\*\)\.

\(\*\) Regra do Valor Médio Unitário do ICMS\-ST: 

__\[MFS66171\]__

Preencher com “Valor Médio Unitário do ICMS\-ST s/ FECEP” recuperado do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\), para o Produto na Data de Emissão da nota \(cupom\) de saída referenciada\. Caso não seja encontrada, considerar a última nota de entrada do produto anterior à saída e calcular o valor unitário do ICMS\-ST\. Para isso, executar:

__Se__ a consulta realizada no Passo 1 do tópico [2\.3](#_2.3_–_Recuperação) retornar registro, então:

    Preencher com:

     \[“Valor Médio Unitário do ICMS\-ST s/ FECEP”\]

     do “Cálculo da Média Pondera Móvel dos Valores Unitários” 

    \(campo VLR\_UNIT\_ICMS\_ST\_FIM\_MP da EST\_ST\_RS\_MEDIA\_POND\);

__Senão__: 

      Se a consulta realizada no Passo 2 do tópico [2\.3](#_2.3_–_Recuperação) retornar registro, então:

           Calcular o Valor Unitário do ICMS\-ST com base na Última Nota de Entrada\.

           Veja Regra de Preenchimento \(\*\) descrita a seguir\.

\(\*\) Regra de Preenchimento:

O preenchimento do campo seria:

 Valor do ICMS\-ST/ QTD\_CONV\_NF\_ENT

Mas para cálculo da Média Ponderada, precisamos separar o FECEP\-ST do ICMS\-ST\. O motivo é que na geração da Saída e Devolução de Saída o campo VLR\_UNIT\_ICMSS\_ESTQ\_SAI \(13 \(C185\) e 09 \(C380\)\) é resultante da soma do ICMS\-ST e FECEP\-ST oriundos do Cálculo da Média Ponderada \(EST\_ST\_RS\_MEDIA\_POND\)\. Se não calcularmos e gravá\-los separadamente na tabela EST\_ST\_RS\_MEDIA\_POND, o FECEP\-ST pode sair duplicado no campo VLR\_UNIT\_ICMSS\_ESTQ\_SAI\.

Tratamento do FECEP embutido nos vlrs de ICMS/ICMS\-ST \(aplicado às Entradas e Devoluções de Entradas\):

Se o item de mercadoria foi recuperado das tabelas “normais” \(X07/X08\), então:

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST 

      nos itens \(SAFX08\)” foi marcado na tela de Dados Iniciais 

      \(menu Parâmetros 🡪 IN\-RE 087/2020 🡪 Dados Iniciais\)\.__ \[MFS65137\]__, então:

             Se for considerado o “52\-Valor ICMS Substituição Tributária” p/ o

             __Valor do ICMS\-ST__ \(\*\):

    Preencher com: 

    \(Valor do ICMS\-ST\- Valor do ICMS\-ST FECEP\) /

    QTD\_CONV\_NF\_ENT 

Senão:

                  Preencher com:

                  \(Valor do ICMS\-ST\) / QTD\_CONV\_NF\_ENT

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST

      nos itens \(SAFX08\)” não foi marcado, então:

           Preencher com:  

             \(Valor do ICMS\-ST\) / QTD\_CONV\_NF\_ENT

Se o item de mercadoria foi recuperado das tabelas do DATAMART, então:

     Se for considerado o “52\-Valor ICMS Substituição Tributária” para o  

__     Valor do ICMS\-ST__ \(\*\):

           Preencher com:  

            \(Valor do ICMS\-ST \- Valor do ICMS\-ST FECEP\) / QTD\_CONV\_NF\_ENT

     Senão

           Preencher com:

          \(Valor do ICMS\-ST\) / QTD\_CONV\_NF\_ENT

__\[MFS543860\]__ Tratamento do parâmetro para identificar se o valor do FECP está embutido nos valores de ICMS não destacado/não escriturado

Tratamento do FECEP embutido nos valores de ICMS\-ST não escriturado e não destacado \(aplicado às Entradas e Devoluções de Entradas\):

    Se o parâmetro “Valores de FECEP estão embutidos nos valores de ICMS\-ST não destacado/não escriturado” for marcado na tela de Dados Iniciais, então:

             Se for considerado o campo “145\- VLR\_ICMSS\_N\_ESCRIT” p/ o

             __Valor do ICMS\-ST__ \(\*\):

    Preencher com: \(VLR\_ICMSS\_N\_ESCRIT \- Valor do ICMS\-ST FECEP\) / QTD\_CONV\_NF\_ENT 

Senão:

                  Preencher com: VLR\_ICMSS\_N\_ESCRIT / QTD\_CONV\_NF\_ENT

            Se for considerado o campo “133\- VLR\_ICMSS\_NDESTAC” p/ o

             __Valor do ICMS\-ST__ \(\*\):

    Preencher com: \(VLR\_ICMSS\_NDESTAC\- Valor do ICMS\-ST FECEP\) / QTD\_CONV\_NF\_ENT 

Senão:

                  Preencher com: VLR\_ICMSS\_NDESTAC / QTD\_CONV\_NF\_ENT

    Se o parâmetro “Valores de FECEP estão embutidos nos valores de ICMS\-ST não destacado/não escriturado” não for marcado, então:

           Preencher com:  

          \(VLR\_ICMSS\_N\_ESCRIT \+ Valor do ICMS\-ST FECEP\) / QTD\_CONV\_NF\_ENT

              OU

             \(VLR\_ICMSS\_NDESTAC \+ Valor do ICMS\-ST FECEP\) / 

               QTD\_CONV\_NF\_ENT

Onde os valores são oriundos do item da Última Nota de Entrada:

- \(\*\)__Valor do ICMS\-ST__ é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

         Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

    Senão:

        Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                         “133\- VLR\_ICMSS\_NDESTAC” preenchidos, então:

             Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

        Senão:

            Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                             “107\- VLR\_TRIB\_ICMS\_ORIG” preenchidos, então:

                 Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.
- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF Última Entrada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  __*[Detalhamento da Ùltima Nota Fiscal de Entrada](#Detalha_ULT_NF_ENT)*__\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr Unit ICMS\-ST\(s/ FECEP\-ST\) \(p/ Cálculo da Média Ponderada\)

Valor Médio Unitário da Base de Cálculo do ICMS\-ST \(<a id="BC_Entrada"></a>BC\-Entrada\) \(d\)

VLR\_UNIT\_BC\_ST\_DEV\_SAI\_MP

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher conforme Regra do Valor Médio Unitário da BC\-ST \(\*\)

__       \[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:__

       Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST”  

       \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no tópico [2\.3](#_2.3_–_Recuperação) __Passo 1__ for negativo, 

        então:

          Desconsiderar a regra acima e preencher este campo com ZERO\.

\[__MFS58042/ MFS59698\]__

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher conforme Regra do Valor Médio Unitário da BC\-ST \(\*\)

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

__\[MFS96666\]: RS5xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

  Preencher conforme Regra do Valor Médio Unitário da BC\-ST \(\*\)\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

__\[MFS96666\]: RS5xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

  Preencher conforme Regra do Valor Médio Unitário da BC\-ST \(\*\)\.

\(\*\) Regra do Valor Médio Unitário da BC\-ST: 

Preencher com o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” recuperado do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\), para o Produto na Data de Emissão da nota \(cupom\) de saída referenciada\. Caso não seja encontrada, considerar a última nota de entrada do produto anterior à saída e calcular o valor unitário da Base\-ST\. Para isso, executar:

__Se__ a consulta realizada no __Passo 1__ do tópico [2\.3](#_2.3_–_Recuperação) retornar registro, então:

    Preencher com: \[“Valor Médio Unitário da Base de Cálculo do ICMS\-ST”\] do

   “Cálculo da Média Pondera Móvel dos Valores Unitários” 

    \(campo VLR\_UNIT\_BC\_ST\_FIM\_MP da EST\_ST\_RS\_MEDIA\_POND\);

__Senão__: 

      Se a consulta realizada no __Passo 2__ do tópico [2\.3](#_2.3_–_Recuperação) retornar registro, então:

           Calcular o Valor Unitário da Base de Cálculo do ICMS\-ST com base na

           Última Nota de Entrada\.

           Veja Regra de Preenchimento \(\*\) descrita a seguir\.

\(\*\) Regra de Preenchimento:

Preencher com:

 Valor da BC\-ST / QTD\_CONV\_NF\_ENT 

Onde os valores são oriundos do item da Última Nota de Entrada:

- Valor da BC\-ST é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor da BC\-ST = 61\-BASE\_SUB\_TRIB\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

       Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

    Senão:

       Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                        “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então:

          Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

       Senão:

           Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                             “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, 

           então:

               Valor da BC\-ST = 106 \- VLR\_BASE\_ICMS\_ORIG  

- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF Última Entrada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  __*[Detalhamento da Ùltima Nota Fiscal de Entrada](#Detalha_ULT_NF_ENT)*__\. 

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr Unit BC ICMS\-ST \(p/ Cálculo da Média Ponderada\)

Valor Médio Unitário do FECEP\-ST \(e\)

VLR\_UNIT\_FECEP\_ST\_DEV\_SAI\_MP

__Igual ao campo 41 \- Valor Unitário FCP ICMS ST Estoque Conv \(VLR\_UNIT\_FCP\_ESTQ\_SAI\)__

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher conforme [Regra do Valor Médio Unitário do FECEP\-ST](#REGRA_VLR_UNIT_FECEP_ST_ESTQ) \(\*\)

__       \[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:__

       Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST”  

       \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no tópico [2\.3](#_2.3_–_Recuperação) __Passo 1__ for negativo, 

        então:

          Desconsiderar a regra acima e preencher este campo com ZERO\.

\[__MFS58042/ MFS59698\]__

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher conforme [Regra do Valor Médio Unitário do FECEP\-ST](#REGRA_VLR_UNIT_FECEP_ST_ESTQ) \(\*\)

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

__\[MFS96666\]: RS5xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

  Preencher conforme [Regra do Valor Médio Unitário do FECEP\-ST](#REGRA_VLR_UNIT_FECEP_ST_ESTQ) \(\*\)\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

__\[MFS96666\]: RS5xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

  Preencher conforme [Regra do Valor Médio Unitário do FECEP\-ST](#REGRA_VLR_UNIT_FECEP_ST_ESTQ) \(\*\)\.

\(\*\) Regra do Valor Médio Unitário do FECEP\-ST: 

Preencher com “Valor Médio Unitário do FECEP\-ST” recuperado do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_RS\_MEDIA\_POND\), para o Produto na Data de Emissão da nota \(ou cupom\) de saída referenciada\. Caso não seja encontrada, considerar a última nota de entrada do produto anterior à saída e calcular o valor unitário do FECEP\-ST\. Para isso, executar:

__Se__ a consulta realizada no __Passo 1__ do tópico [2\.3](#_2.3_–_Recuperação) retornar registro, então:

    Preencher com: \[“Valor Médio Unitário do FECEP\-ST”\] do

   “Cálculo da Média Pondera Móvel dos Valores Unitários” 

    \(Campo VLR\_UNIT\_FECEP\_ST\_FIM\_MP da EST\_ST\_RS\_MEDIA\_POND\);

__Senão__:

      Se a consulta realizada no __Passo 2__ do tópico [2\.3](#_2.3_–_Recuperação) retornar registro, então:

           Calcular o Valor Unitário do FECEP\-ST com base na Última Nota de Entrada\.

           Veja Regra de Preenchimento \(\*\) descrita a seguir\.

\(\*\) Regra de Preenchimento:

Preencher com:

 Valor do FECEP\-ST / QTD\_CONV\_NF\_ENT 

Onde os valores são oriundos do item da Última Nota de Entrada:

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.
- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF Última Entrada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  __*[Detalhamento da Ùltima Nota Fiscal de Entrada](#Detalha_ULT_NF_ENT)*__\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ arredondar para 6 casas decimais o valor médio unitário recuperado da Média Ponderada pois compõe o layout do C181\.

Vlr Unit FECEP\-ST \(p/ Cálculo da Média Ponderada\)

Valor do ICMS Calculado para Devolução \(f\) = \(a\*b\)

VLR\_ICMS\_DEV\_SAI\_MP

Preencher com:

\[Quantidade Devolvida Convertida \(a\) \* Valor Médio Unitário do ICMS \(b\)\]

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr ICMS \(p/ Cálculo da Média Ponderada\)

Valor do ICMS\-ST Calculado para Devolução \(g\) = \(a \* c\)

VLR\_ICMS\_ST\_DEV\_SAI\_MP

Preencher com:

\[Quantidade Devolvida Convertida \(a\) \* Valor Médio Unitário do ICMS\-ST \(c\)\]

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr ICMS\-ST\(s/ FECEP\-ST\) \(p/ Cálculo da Média Ponderada\)

Valor Base de Cálculo do ICMS\-ST Calculado para Devolução \(h\) = \(a \* d\)

VLR\_BC\_ST\_DEV\_SAI\_MP

Preencher com:

\[Quantidade Devolvida Convertida \(a\) \* Valor Médio Unitário da Base de Cálculo do ICMS\-ST \(d\)\]

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr BC ICMS\-ST \(p/ Cálculo da Média Ponderada\)

Valor FECEP\-ST Calculado para Devolução \(i\) = \(a \* e\)

VLR\_FECEP\_ST\_DEV\_SAI\_MP

Preencher com:

\[Quantidade Devolvida Convertida \(a\) \* Valor Médio Unitário do FECEP\-ST \(e\)\]

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

 Arredondar o resultado acima em 6 decimais\.

__\[MFS90131\]__ arredonda para 8 casas decimais, pois o campo é utilizado no Cálculo da Média Ponderada\.

Vlr FECEP\-ST \(p/ Cálculo da Média Ponderada\)

OBSERVAÇÃO

DSC\_OBS

 \[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no tópico [2\.3](#_2.3_–_Recuperação) for negativo, então:

Preencher este campo com a observação:

“Valor médio ponderado móvel do dia da emissão da saída está negativo\. Campo Vlr Unit ICMS Operação Conv foi acrescido de 9999,99 e os campos Vlr Unit ICMS Estoque Conv, Vlr Unit ICMS\-ST Estoque Conv e Vlr Unit FCP\-ST Estoque Conv foram zerados\. Tratamento baseado no tópico 19\.3\-A\.2\.2\.2 da IN45/98”

Onde:

9999,99:

               VLR\_UNIT\_BC\_ST\_FIM\_MP \* Alíquota Interna / 100 \(sem sinal negativo\)

- Para os demais Cód\. Operação:

Não preencher\.

Observação

# <a id="_Toc72506259"></a>RELATORIO DE CONFERÊNCIA

Gerar um arquivo excel a partir da leitura da tabela __EST\_ST\_RS\_NF\_DEV\_SAI__

Nome do arquivo: Relatório\_Conferencia\_C181\_mm\_aaaa\_cod\_estab\.xlsx

= = = = = =

 


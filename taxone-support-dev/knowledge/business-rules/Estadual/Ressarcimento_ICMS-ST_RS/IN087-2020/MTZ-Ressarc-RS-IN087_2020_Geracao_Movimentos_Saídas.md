# MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Saídas

- **Fonte:** MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos_Saídas.docx
- **Modificado:** 2024-08-15
- **Tamanho:** 232 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 087/2020\) 

Geração dos Movimentos – Saídas 

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

Não estamos considerando Cupom Fiscal nesta entrega\.

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
- 782Saída interna com nova ST \(RICMS, Livro III, art\.23, III\) \(e Devoluções\)
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

Campos impactados: 24 \- COD\_MOTIVO\_SAI, 29 \- VLR\_UNIT\_ICMSS\_REST\_SAI, 30 \- VLR\_UNIT\_FCP\_REST\_SAI, 31 \- VLR\_UNIT\_ICMSS\_COMPL\_SAI, 32 \- VLR\_UNIT\_FCP\_COMPL\_SAI, 

13/04/2021

__MFS64550__

Liliane Videira Assaf

A tabela 5\.7 do Sped Fiscal alterou a descrição dos códigos RS100 e RS300, indicando sua aplicação no caso da nota não resultar em ressarcimento nem complemento\.

Com isso vamos alterar a geração do C185 para que a nota que não resulte em ressarcimento nem complemento passe a ser gerada no C185 com código de motivo igual a RS100\. Antes desta alteração, a nota não era gerada e uma mensagem era apresentada no log\.

04/05/2021

__MFS65137__

Liliane Videira Assaf

Inclusão do Cupom Fiscal \(Mod\. 02, 2D e 60\) para viabilizar a geração do registro C480 do Sped Fiscal\.

Os cupons gerados por esse processo devem ser gravados na tabela EST\_ST\_RS\_ECF e gerados em relatório de conferência\.

13/05/2021

__MFS66171__

Liliane Videira Assaf

Hoje a Geração da Média Ponderada calcula o campo “Valor Médio Unitário do ICMS\-ST” sem FECEP\. 

O Cálculo está sendo alterado para fornecer o Valor médio de ICMS\-ST com e sem FECEP, através dos campos: 

\- “Valor Médio Unitário ICMS\-ST __c/__ FECEP”\. 

\- “Valor Médio Unitário ICMS\-ST __s/__ FECEP”\.

A nota saída deve recuperar o Médio de ICMS\-ST com FECEP para demonstrar no C185 \- 13 \- VLR\_UNIT\_ICMSS\_ESTQ\_SAI \(C380 – 09\)\.  

O cupom fiscal deve recuperar o Médio de ICMS\-ST com FECEP para demonstrar no C480\-09\- VLR\_UNIT\_ICMSS\_ESTQ\_SAI\.  

07/06/2021

__MFS66473__

Liliane Videira Assaf

Inclusão do tratamento para saída de produtos farmacêuticos baseados nos artigos 103 e 104 do LIVRO III do RICMS\.  Segundo esses artigos, a substituição tributária não se aplica a produtos farmacêuticos destinados a distribuidores, logo as saídas oriundas desses distribuidores não têm direito a ressarcimento ST, logo essas notas de saída não devem sair no C185, por consequente suas devoluções também não saem no C181\.

Cliente Santa Cruz encaminhou os CFOPs que devem entrar nesse tratamento: __5405 e 5910__\.

21/06/2021

__MFS64191__

Liliane Videira Assaf

IN\-RE 037/21:

Desconsiderar o código da operação 780 na geração dos movimentos de saída\. Esse código passa a ser considerado na geração da Devolução da Entrada\. 

- 780 \- Devolução para fornecedor de outra UF, quando a retenção inicial foi realizada pelo próprio remetente da devolução, nos moldes do RICMS, Livro III, art\. 53\-A \(RICMS, Livro III, art\. 25\)

15/07/2021

__MFS67809__

Aline Melo

Criação de tela de parametrização de produtos farmacêuticos, que permita ao usuário informar os códigos de produtos que não devem ser considerados para a geração de saídas de nota fiscal e cupom \(registro C185\)\.

27/07/2021

__MFS72429__

Andréa Rocha

Inclusão do arredondamento dos valores calculados, ou seja, os valores calculados não serão mais truncados\.  Conforme informação passada pela SEFAZ/RS\.

11/10/2021

__MFS77274__

Liliane Videira Assaf

Alteração no Tratamento para Notas de Produtos Farmacêuticos emitidas por Distribuidores criada pela MFS66473 para retirar os CFOPs 5405 e 5910 da regra\. Tratamento é aplicado às notas fiscais e aos cupons fiscais\.

10/12/2021

__MFS84243__

Andréa Rocha

Inclusão da verificação da data fiscal da nota fiscal / cupom fiscal para recuperar a parametrização por Produto/NCM/CEST\.

12/04/2022

__MFS90131__

Liliane Assaf

Chamado Lasa/Magalu: Tratamento na diferença de 0,000001 do valor médio unitário do último dia do mês para o do primeiro dia do mês seguinte\. 

Obs: Não chegamos a conclusão se o arredondamento dos valores médios unitários do C185 – campos 12, 13 e 14 pode torná\-los superiores aos dos registros H030, C180, C181 e C186, causando erro no validador\. Esse ponto ficará sob observação, podendo futuramente alterar para TRUNCAMENTO\. Críticas do validador:

"O conteúdo informado em registro C185, no campo 13 \(VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\), por ser uma média, não pode ser superior aos demais valores apresentados no arquivo EFD \(Bloco H, registros C180, C181 e C186\)"

“ A quantidade total de imposto presumido sumarizada pela EFD para estoques \(registros H010 e H030\) \+ entradas \(registros C180 e C181\), expressa em reais \(R$\), subtraída pela quantidade total de imposto sumarizada para as saídas, informadas em registros C185, C197 \(RS99993016 ou o RS99993024\) e E115 \(RSRS991255\), resultou em um valor negativo \(saiu ICMS que não entrou, o que é impossível\)\.”

01/08/2022

__MFS89648__

Liliane Assaf

Atualização legal IN55/22:

 Tratamento para Valor Médio Ponderado Móvel calculado ao final do dia negativo \(19\.3\-A\.2\.2\.2 da IN\-045/98\) 

Quando o Valor Médio Ponderado Móvel for negativo, os Movimentos de Saídas Internas p/ Consumidor Final \(Cod\. Operação 770\) sofrerão as seguintes alterações:

- Valor Unitário do ICMS calculado através da multiplicação da Alíquota Interna pelo Valor Médio Ponderado Móvel \(sem sinal\), será adicionado ao campo VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV dos registros C185, C380, C480;
- Os campos referentes ao ICMS, ICMS\-ST, FECEP das mercadorias em estoque no dia da saída \(VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV, VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV e  VL\_UNIT\_FCP\_ICMS\_ST\_ ESTOQUE\_CONV\) dos registros C185, C380 e C480 zerão zerados\.

10/08/2022

__MFS96666__

Liliane Assaf

Atualização legal IN RE 96/22 \(jan\-2023\):

Tópico 19\.3\-A\.1\.12 da IN RE045/98: criação dos códigos RS101, \.\.\., RS156 e RS301, \.\.\., RS356 para as saídas internas a consumidor final quando a base de cálculo é reduzida\. Os códigos RS100 ou RS300 passam a ser aplicados apenas quando a base de cálculo for integral\.

Atualização Legal Sped Fiscal \(jan 2023\):

Os códigos de motivos RS0xx: passam a preencher os campos 12,13,14 do C185, os campos 08, 09, 10 do C380 e os campos 08, 09, 10 do C480\.

07/12/2022

Sumário

<a id="_Introdução"></a>[1\.	Introdução	1](#_Toc71832838)

[1\.1	– Operações de Saídas \(e devoluções\) acobertadas pelo Ressarcimento de ST	1](#_Toc71832839)

[2\.	Recuperação dos Dados e Processamento	1](#_Toc71832840)

[2\.1 – Recuperação das Notas Fiscais de Saídas \(C185, C380\)	1](#_Toc71832841)

[2\.2 – Recuperação dos Cupons Fiscais \(C480\)	1](#_Toc71832842)

[2\.3 – Recuperação dos Valores Unitários Médios referenciados pela SAÍDA	1](#_Toc71832843)

[3\.	Gravação dos Dados na Tabela dos Movimentos	1](#_Toc71832844)

[3\.1 – Gravação das Notas Fiscais de Saídas \(C185, C380\)	1](#_Toc71832845)

[3\.2 – Gravação dos Cupons Fiscais \(C480\)	1](#_Toc71832846)

[4\.	RELATORIO DE CONFERÊNCIA	1](#_Toc71832847)

# <a id="_Toc71832838"></a>Introdução 

Esse documento tem como objetivo definir a geração das __Saídas__ que consiste em:

- Recuperar as notas fiscais de saídas e cupons fiscais do período;
- Recuperar os valores unitários médios ponderados relacionados ao dia e produto da nota de saída \(ou cupom\)\. Tais valores são recuperados da tabela EST\_ST\_RS\_MEDIA\_POND;
- Gravar as notas de saídas na tabela específica dessa geração \(EST\_ST\_RS\_NF\_SAI\);
- Gravar os cupons fiscais na tabela específica EST\_ST\_RS\_ECF; __\[MFS\-65137\]__
- Gerar os Relatórios de Conferências a partir da tabela EST\_ST\_RS\_NF\_SAI, demonstrando o detalhamento do cálculo dos valores que serão apresentados nos registros C185, C380 do Sped Fiscal\.
- Gerar o Relatório de Conferência a partir da tabela EST\_ST\_RS\_ECF, demonstrando o detalhamento do cálculo dos valores que serão apresentados no C480 do Sped Fiscal\. __\[MFS\-65137\]__

Obs: O Cálculo da Média Pondera Móvel dos Valores Unitários do ICMS, ICMS\-ST, Base de Cálculo do ICMS\-ST e FECEP\-ST é realizado na etapa anterior\. Logo ao realizar essa etapa, os valores médios já estarão gravados na tabela EST\_ST\_RS\_MEDIA\_POND\.

Esse processamento é base para a geração dos registros C185, C380 e C480\. Todos os registros gravados na tabela EST\_ST\_RS\_SAI numa próxima etapa serão copiados para a tabela x296\_info\_compl\_st\_itens\_merc de onde são gerados os registros C185 e C380 no módulo SPED FISCAL\.  E os registros da tabela EST\_ST\_RS\_ECF copiados para a X297\_INF\_COMP\_ST\_CUPOM\_ECF para gerar o C480\. Ou seja, as regras para geração dos registros C185, C380 e C480 são realizadas nessa fase\.

- 
	1. <a id="_Toc71832839"></a>– <a id="COD_OP_SAIDA"></a>Operações de Saídas \(e devoluções\) acobertadas pelo Ressarcimento de ST__:__

\[__MFS58042/ MFS59698\]__

Lista dos Códigos de Operação considerados para a geração do movimento de Saída e Devolução de Saída\. 

Tais códigos estão disponíveis na parametrização por CFOP e por Natureza de Operação no *menu Parâmetros à \(IN\-RE 087/20\) à Operações\.*

Vale ressaltar que, EXCETO para as operações da faixa 772 a 777, a devolução se aplica às operações de saída listadas\.

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

Saída para Outra UF \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)

RS213, RS713

19\.3\-A\.1\.9 

779

Saída para Outra UF \(RICMS, Livro III, art\.24\) \(e Devoluções\)

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

# <a id="_Toc350763252"></a><a id="_Toc71832840"></a>Recuperação dos Dados e Processamento

## <a id="_2.1_–_Recuperação"></a><a id="_Toc71832841"></a>2\.1 – Recuperação das Notas Fiscais de Saídas \(C185, C380\)

__Origem dos dados__: \- Parametrização de Produtos \(por Código, por NCM e por CEST\);

                                  \- Parametrização de CFOP / Natureza de Operação;

                                  \- SAFX07 / SAFX08 – Tabelas dos Documentos Fiscais \(DATAMART\)

__Critérios da recuperação das Notas Fiscais de Saída: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data Fiscal – data enquadrada no período informado em tela;

\- Nota fiscal de devolução \(NORM\_DEV = “1”\);

\- Nota de entrada \(MOVTO\_E\_S = “9”\);

\- Modelo = 01, 02, 1B, 04, 55, 65 

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

772

Furto ou Roubo \- baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

773

Perda, extravio ou Deterioração – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

774

Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

775

Furto ou Roubo \- baixa sem Ressarcimento 

776

Perda, extravio ou Deterioração – baixa sem Ressarcimento 

777

Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa sem Ressarcimento 

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

__Campos a serem recuperados: __

Recuperar as seguintes informações da nota de saída \(SAFX07/SAFX08\):

\- Campos de Identificação da Capa e do Item da nota de devolução;

\- 13,14 \- Produto – GRUPO\_PRODUTO, IND\_PRODUTO, COD\_PRODUTO \(SAFX08\)

\- Unidade de Medida do Produto \(SAFX2013\)

__\- Caso o produto do item da nota de devolução tenha sido parametrizado por Código \(menu “Parâmetros à Produtos à Por Código”\) recuperar o Produto Principal \(grupo, indicador e código\) e a Unidade de Medida do Produto Principal \(SAFX2013 – campo 14 – COD\_MEDIDA\)\.__

\- 24 \- Quantidade \- QUANTIDADE \(SAFX08\)

\-137\-Quantidade Convertida \(SAFX08\)

\- 25 \- Unidade de Medida \- COD\_MEDIDA \(SAFX08\)

<a id="_Hlk75194865"></a>__MFS66473/MFS67809/ MFS77274__

__Tratamento para Notas de Produtos Farmacêuticos emitidas por Distribuidores:__

<a id="_Hlk75258358"></a>Verificar os critérios a seguir:

- Estabelecimento é um __Distribuidor__ \(atacadista\), ou seja, na Tela de Dados Iniciais estiver com o campo “Contribuinte Varejista?” = Não; 
- <a id="_Hlk78292438"></a>__Produto__ do Item da Nota de Saída estiver cadastrado, na tela de Parametrização de Produtos Farmacêuticos por Código, no menu: Parametros >  \(IN\-RE 087/20\) > Produtos Farmacêuticos > Código

<a id="_Hlk75258481"></a>Se os dois critérios forem atendidos, então:

            O item de mercadoria dessa nota de saída não será gravado na tabela EST\_ST\_RS\_NF\_SAI, e a seguinte mensagem será exibida no log:

Para Nota Fiscal de Saída de modelos 01, 1B, 04, 55, 65:

“*Registro C185: Nota de Saída de produto farmacêutico amparada pelo art 103/104 do Livro III do RICMS não será gerada no C185”\.*

Para Nota Fiscal de Saída de modelos 02:

“*Registro C380: Nota de Saída de produto farmacêutico amparada pelo art 103/104 do Livro III do RICMS não será gerada no C185”\.*

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Saída exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

## <a id="_2.2_–_Recuperação"></a><a id="_Toc71832842"></a>2\.2 – Recuperação dos Cupons Fiscais \(C480\) 

__\[MFS\-65137\]__

O objetivo é recuperar toda movimentação de cupom de modelos 02, 2D e 60, com os mesmos critérios da geração do registro C470 do SPED FISCAL\.  

Esta regra foi escrita com base nos documentos Sped\_Fiscal\_Regras\_Bloco\_C\.docx\.

__Origem dos dados__: 

\- SAFX991 – Tabela de Capa da Redução Z;

\- SAFX993 – Tabela de Capa do Cupom Fiscal;

\- SAFX994 – Tabela de Item do Cupom Fiscal;

\- SAFX2087 \-Tabela de Equipamento ECF

\- Parametrização de Produtos \(por Código, por NCM e por CEST\);

\- Parametrização de CFOP 

OBS: A Parametrização da Natureza de Operação não é utilizada, pois cupom fiscal não possui Código de Natureza da Operação, apenas CFOP\.

__Critérios da recuperação dos Cupons Fiscais: __

\- Empresa da Redução Z \(SAFX991\) – código da empresa do login;

\- Estabelecimento da Redução Z \(SAFX991\) – código do estabelecimento selecionado para geração; 

\- Data do movimento da Redução Z \(DATA\_FISCAL SAFX991\) enquadrada no período informado em tela;

\- Com os dados do Equipamento ECF da Redução Z \(campos COD\_EMPRESA, COD\_ESTABELECIMETO, COD\_MODELO e COD\_CAIXA\_ECF da SAFX991\), acessar a Tabela de Equipamento ECF \(SAFX2087\) e recuperar o Código Modelo NF \(COD\_MODELO\_COTEPE\) e COO Final para Reinicio \(NUM\_COO\_FIM\_REI\);

\- Código Modelo NF do Equipamento ECF \(COD\_MODELO\_COTEPE da SAFX2087\) = 02, 2D, 60;

\- Com os dados do COO Inicial e COO Final da Redução Z \(campos COD\_EMPRESA, COD\_ESTABELECIMETO, COD\_MODELO, COD\_CAIXA\_ECF, DATA\_FISCAL, NUM\_COO\_INI, NUM\_COO\_FIM da SAFX991\) acessar a Tabela de Capa do Cupom Fiscal \(SAFX993\) e recuperar os cupons emitidos no dia\. Fazer a seguinte associação de campos:

- COD\_EMPRESA SAFX991 = COD\_EMPRESA SAFX993
- COD\_ESTAB SAFX991= COD\_ESTAB SAFX993
- COD\_MODELO SAFX991= COD\_MODELO SAFX993
- COD\_CAIXA\_ECF SAFX991= COD\_CAIXA\_ECF SAFX993
- DATA\_FISCAL SAFX991 = DATA\_EMISSAO SAFX993
- NUM\_COO SAFX993 compreendido entre o NUM\_COO\_INI, NUM\_COO\_FIM da SAFX991\.

Fazer tratamento para quando o contador do cupom é reiniciado no meio do dia, caso em que o NUM\_COO\_INI fica maior que o NUM\_COO\_FIM\. Nesse caso, recupera os cupons compreendidos em duas faixas:

- NUM\_COO SAFX993 compreendido entre o NUM\_COO\_INI da SAFX991 e NUM\_COO\_FIM\_REI da SAFX2087;

e

- NUM\_COO SAFX993 compreendido entre 000000 e NUM\_COO\_FIM da SAFX991;

\- Data Emissão do Cupom \(DATA\_EMISSAO SAFX993\) enquadrada no período de geração

\- Situação do Cupom = 1 – Documento Normal *\(*IND\_SITUACAO\_CUPOM da SAFX993*\)*;

\- Tipo de Documento = 1 – Cupom Fiscal \(IND\_TIPO\_CUPOM da SAFX993\);

\- Com os dados da Capa do Cupom \(campos COD\_EMPRESA, COD\_ESTABELECIMETO, COD\_MODELO, COD\_CAIXA\_ECF, DATA\_EMISSAO, NUM\_COO da SAFX993\) acessar a Tabela de Item do Cupom Fiscal \(SAFX994\) e recuperar os itens dos cupons emitidos no dia\.

\- Situação do item no Cupom = 1 – Item Normal ou 3 – Item Cancelado Parcialmente \(IND\_SITUACAO\_ITEM da SAFX994\);

__\[MFS84243\] __Inclusão da verificação da data fiscal do cupom fiscal para recuperar a parametrização por Produto/NCM/CEST\.

\- O produto do item deve constar na parametrização do menu “*Parâmetros à Produtos à Por Código*”, __ou__, seu NCM deve estar parametrizado no menu “*Parâmetros à Produtos à Por NCM*”, __ou__, seu CEST deve estar parametrizado no menu “*Parâmetros à Produtos à Por CEST*”\. 

  Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\.  Somente devem ser considerados os produtos em que a data inicial de vigência da parametrização seja menor ou igual a data fiscal do cupom fiscal\.

   No caso da parametrização dos produtos, primeiro é verificado se o produto consta na parametrização da opção “Por Código”\. Ao verificar a parametrização por código, deve\-se considerar também os produtos associados\. Ou seja, o produto da nota deve constar como o produto “principal” da parametrização \(__ESP\_SP\_PROD\_ST__\), ou ser um produto “associado” ao produto principal \(__ESP\_SP\_PROD\_ST\_ASS__\)\.  Módulos de ressarcimento de SC e SP trabalham com produto associado\.

   Os produtos “associados” são produtos cuja movimentação será demonstrada na Ficha 3 em nome do produto principal parametrizado\. 

  A prioridade na pesquisa da parametrização dos produtos é: por Código, por NCM, e por último, por CEST, da seguinte forma:

 

        \-Caso o produto conste na parametrização por código, a parametrização por NCM não precisa ser verificada\.

        \-Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “Por NCM”\.

        \-Caso o produto conste na parametrização por NCM, a parametrização por CEST não precisa ser verificada\.

        \-Caso não, é verificado se o CEST do produto \(CEST do cadastro do produto\) consta na parametrização da opção “Por CEST”\.

 \- O CFOP do item do Cupom deve constar na parametrização do menu “*Parâmetros à \(IN\-RE 087/20\) à Operações*” para a seguinte operação:

Cód Operação

Descrição da Operação \(*menu Parâmetros à \(IN\-RE 087/20\) à Operações\)*

770

Saída Interna para Consumidor Final \(e Devoluções\)

772

Furto ou Roubo \- baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

773

Perda, extravio ou Deterioração – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

774

Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

775

Furto ou Roubo \- baixa sem Ressarcimento 

776

Perda, extravio ou Deterioração – baixa sem Ressarcimento 

777

Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa sem Ressarcimento 

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

  


\- Não considerar as Reduções Z com Venda Bruta Zerada, ou seja, registro da SAFX991 com os três critérios atendidos:

- VLR\_VENDA\_BRUTA = 0
- VLR\_VENDA\_LIQ = 0 e 
- NUM\_COO\_INI = NUM\_COO\_FIM\.

__Campos a serem recuperados: __

Recuperar as seguintes informações do cupom \(SAFX993/SAFX994\):

\- Campos de Identificação da Capa e do Item do Cupom Fiscal;

\- 08, 09 \- Produto – GRUPO\_PRODUTO, IND\_PRODUTO, COD\_PRODUTO \(SAFX994\)

\- Unidade de Medida do Produto \(SAFX2013\)

__\- Caso o produto do item da nota de devolução tenha sido parametrizado por Código \(menu “Parâmetros à Produtos à Por Código”\) recuperar o Produto Principal \(grupo, indicador e código\) e a Unidade de Medida do Produto Principal \(SAFX2013 – campo 14 – COD\_MEDIDA\)\.__

\- 16 \- Quantidade \- QTDE \(SAFX994\)

\- 17 \- Unidade de Medida \- COD\_MEDIDA \(SAFX994\)

\- 22 \- Valor total líquido \- VLR\_LIQ\_ITEM \(SAFX994\)\.

__MFS66473/MFS67809 / MFS77274__

__Tratamento para Notas de Produtos Farmacêuticos emitidas por Distribuidores:__

Verificar os critérios a seguir:

- Estabelecimento é um __Distribuidor__ \(atacadista\), ou seja, na Tela de Dados Iniciais estiver com o campo “Contribuinte Varejista?” = Não;
- __Produto__ do Item do Cupom Fiscal estiver cadastrado, na tela de Parametrização de Produtos Farmacêuticos por Código, no menu: Parametros >  \(IN\-RE 087/20\) > Produtos Farmacêuticos > Código

Se os dois critérios forem atendidos, então:

            O item do cupom fiscal não será gravado na tabela EST\_ST\_RS\_ECF, e a seguinte mensagem será exibida no log:

“*Registro C480: Cupom Fiscal de produto farmacêutico amparado pelo art 103/104 do Livro III do RICMS não será gerada no C480”\.*

O log deve demonstrar as informações necessárias para permitir a identificação do item do cupom exibindo o Estabelecimento, Número do Caixa, Modelo, Número COO, Data Emissão, Número do Item\)

__Nota técnica:__

__*Ver C\_EFD21 da Efd\_Dic\_Dados\_ECF*__

## <a id="_2.3_–_Recuperação"></a><a id="_Toc71832843"></a>2\.3 – Recuperação dos Valores Unitários Médios referenciados pela SAÍDA

Base para utilização do valor unitário móvel para as notas de saída, segundo IN\-RE 087/20\. Veja: 

” 19\.3\-A\.1\.6 \- Nos registros C185, C380 e C480, os campos VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV e VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV, devem ser informados com os valores atualizados diariamente até o dia da operação, considerando todas entradas, devoluções de saídas, retornos de mercadorias não entregues e devoluções de entradas de mercadorias ocorridas ao longo do dia\.”

“19\.3\-A\.2\.1 \- O valor médio ponderado móvel unitário será calculado, em periodicidade diária, de acordo com as informações referentes às mercadorias recebidas com substituição tributária existentes em estoque no fim do dia anterior, acrescido das informações referentes às entradas do dia da operação, sendo fixado e aplicado para todas as operações de saída registradas no respectivo dia\.”

Sendo assim vamos realizar o seguinte procedimento para busca dos Valores Unitários Médios:

Consultar a Tabela de “Cálculo da Média Pondera Móvel dos Valores Unitários” \(__EST\_ST\_RS\_MEDIA\_POND__\) com os seguintes critérios:

\- Empresa login;

\- Estabelecimento selecionado na tela de geração;

\- Data = Data de Emissão da Nota fiscal de Saída \(SAFX07\) \(vide [2\.1](#_2.1_–_Recuperação)\); ou

              Data de Emissão do Cupom Fiscal \(SAFX993\) \(vide [2\.2](#_2.2_–_Recuperação)\);

\- Produto = Produto do item da Nota de Saída ou Cupom Fiscal \(vide [2\.1](#_2.1_–_Recuperação) , [2\.2](#_2.2_–_Recuperação)\);

                   __Caso o produto do item tenha sido parametrizado por Código __

__                  \(menu “Parâmetros à Produtos à Por Código”\) considerar o Produto Principal \(grupo, indicador e código\)__\.

*\(ver OBS sobre os produtos associados, pois os valores medios estariam no produto principal\)*

Recuperar os Valores Médios:

\- Valor Médio Unitário do ICMS \(VLR\_UNIT\_ICMS\_FIM\_MP\);

\- Valor Médio Unitário do ICMS\-ST s/ FECEP \(VLR\_UNIT\_ICMS\_ST\_FIM\_MP\); __\[MFS66171\]__

\- Valor Médio Unitário do ICMS\-ST c/ FECEP \(VLR\_UNIT\_ICMS\_ST\_FECEP\_FIM\_MP\); __\[MFS66171\]__

\- Valor Médio Unitário da Base de Cálculo do ICMS\-ST \(VLR\_UNIT\_BC\_ST\_FIM\_MP\);

\- Valor Médio Unitário do FECEP\-ST \(VLR\_UNIT\_FECEP\_ST\_FIM\_MP\);

Caso a consulta acima não retorne registros, gravar mensagem de erro no log:

	Para Nota Fiscal de Saída de modelos 01, 1B, 04, 55, 65:

*“Registro C185: Não foi possível recuperar o valor unitário médio móvel calculado para o dia da saída\. A Nota de saída será gerada no C185 sem valores unitários de ICMS e ICMS\-ST Estoque Conv\.”*

	Para Nota Fiscal de Saída de modelo 02:

*“Registro C380: Não foi possível recuperar o valor unitário médio móvel calculado para o dia da saída\. A Nota de saída será gerada no C380 sem valores unitários de ICMS e ICMS\-ST Estoque Conv\.”*

	__\[MFS\-65137\]__

Para Cupom Fiscal:

*“Registro C480: Não foi possível recuperar o valor unitário médio móvel calculado para o dia da saída\. O Cupom Fiscal será gerado no C480 sem valores unitários de ICMS e ICMS\-ST Estoque Conv\.”*

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Saída, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

__\[MFS\-65137\]__ No caso de cupom fiscal, informar Estabelecimento, Número do Caixa, Modelo, Número COO, Data Emissão, Produto\.

# <a id="_Toc71832844"></a>Gravação dos Dados na Tabela dos Movimentos

## <a id="_Toc71832845"></a>3\.1 – Gravação das Notas Fiscais de Saídas \(C185, C380\)

As notas fiscais recuperadas conforme tópico [2\.1](#_2.1_–_Recuperação) são gravadas__ item a item__ na tabela EST\_ST\_RS\_NF\_SAI conforme definido a seguir\.

__Tabela EST\_ST\_RS\_NF\_SAI__

Os campos sinalizados com asterisco compõem a chave da tabela\.

A estrutura da tabela __EST\_ST\_RS\_NF\_SAI __é baseada na SAFX296\. Contém todos os campos da SAFX296 e campos a mais usados no relatório de conferência\.

PK

Item

SAFX296

Campo

Regra de Preenchimento

Campos para relatório

\(C185\)

Saída com Cod Modelo 01, 1B, 04, 55, 65

Campos para relatório

\(C380\)

Saída com Cod Modelo 02

\(\*\)

Código do Estabelecimento

COD\_ESTAB\_GER

Código do estabelecimento SELECIONADO na tela de geração\.

Esse campo foi criado, pois no futuro poderemos ter a geração por Inscrição Estadual Única, e nessa opção o estabelecimento selecionado na tela de geração é o centralizador, e as notas fiscais são dos estabelecimentos centralizador e centralizados\.

Não apresentar

Não apresentar

__*Campos do layout da SAFX296 \(Item da nota de de saída\)*__

\(\*\)

01

Código da Empresa 

COD\_EMPRESA

Código da empresa da nota de Saída \(SAFX07\) 

Cod Empresa

Cod Empresa

\(\*\)

02

Código do Estabelecimento

COD\_ESTAB

Código do estabelecimento da nota de Saída \(SAFX07\)

Cod Estab

Cod Estab

\(\*\)

03

Data Escrita Fiscal

DATA\_FISCAL

Data fiscal da nota de Saída \(SAFX07\)

Dt Fiscal

Dt Fiscal

\(\*\)

04

Movimento Entrada / Saída

MOVTO\_E\_S

Indicador do movimento da nota de Saída \(SAFX07\)

E/S

E/S

\(\*\)

05

Normal ou Devolução

NORM\_DEV

Indicando de Normal/Devolução da nota de Saída \(SAFX07\)

Norm/Dev

Norm/Dev

\(\*\)

06

Tipo do Documento

COD\_DOCTO 

\(IDENT\_DOCTO\)

Tipo do documento da nota de Saída\.

Cod Docto

Cod Docto

\(\*\)

07

08

Pessoa Física/Jurídica

IND\_FIS\_JUR/ COD\_FIS\_JUR

\(IDENT\_FIS\_JUR\)

Pessoa física/jurídica da nota de Saída \(SAFX07\)

Ind Fis/Jur

Cod Fis/Jur

Ind Fis/Jur

Cod Fis/Jur

\(\*\)

09

Número do Documento Fiscal

NUM\_DOCFIS

Número do documento fiscal de Saída\.

Num Docfis

Num Docfis

 

10

Série do Documento Fiscal

SERIE\_DOCFIS

Série do documento fiscal de Saída\.

Serie

Serie

 

11

Subsérie do Documento Fiscal

SUB\_SERIE\_DOCFIS

Subsérie do documento fiscal de Saída

SubSerie

SubSerie

12 13 14 15

Identificador do Item

DISCRI\_ITEM

Campo identificador do item de mercadoria de Saída

\(DISCR\_ITEM da X08\_ITENS\_MERC\)\.

Num Item

Num Item

16

Quantidade Convertida

Campos da EFD correspondentes: 03 do C180, 07 do C185 e 03 \(C380\)\.

QTD\_CONV

Preencher com:

“Qtde Convertida Calculada para o Item da NF de Saída \([QTD\_CONV\_NF\_SAI](#QTD_CONV_NF_SAI)\)”

Ver  [__*Detalhamento da Nota de Saída*__](#Detalhamento_Nota_Saída)\.

Qtde Conv \(C185\-07\)

Qtde Conv \(C380\-03\)

17

Unidade de Medida

Campos da EFD correspondentes: 04 do C180, 08 do C185 e 04 \(C380\)\.

COD\_MEDIDA

Campo 14 – Unidade de Medida do Cadastro do Produto \(SAFX2013\), do produto pertencente ao item da nota de Saída\. *\(ver OBS abaixo sobre os produtos associados\)*

__Sobre os produtos associados:__ Quando se tratar de uma nota fiscal de produto “associado”, a unidade de medida apresentada será a __unidade do produto principal__\.

Medida

\(C185\-08\)

Medida

\(C380\-04\)

18

Valor Unitário Conv\.

Campos da EFD correspondes: 05 \(C180\), 09 \(C185\) e 05 \(C380\)\.

VLR\_UNIT\_CONV

Preencher com:

  VLR\_CONTAB\_ITEM da SAFX08 / QTD\_CONV\_NF\_SAI

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o resultado acima em 6 decimais\.

Onde os valores são oriundos do item da nota de Saída:

- VLR\_CONTAB\_ITEM é o campo 64\-Valor Contabil \(SAFX08\) do Item da nota de Saída;
- QTD\_CONV\_NF\_SAI: “Qtde Convertida Calculada para o Item da NF de Saída \([QTD\_CONV\_NF\_SAI](#QTD_CONV_NF_SAI)\)”

Ver  [__*Detalhamento da Nota de Saída*__](#Detalhamento_Nota_Saída)\.

Vlr Unit Conv \(C185\-09\)

Vlr Unit Conv \(C380\-05\)

19

Valor Unitário ICMS Conv\.

Campos da EFD correspondes: 06 \(C180\), 10 \(C185\) e 06 \(C380\)\.

VLR\_ICMS\_CONV

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

       Preencher com   BC\-Saída \* Aliquota interna / 100

__\[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:__

Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no tópico [2\.3](#_2.3_–_Recuperação) for negativo, então:

    Acrescentar ao valor calculado pela regra acima, o valor a seguir:

    VLR\_UNIT\_BC\_ST\_FIM\_MP \* Alíquota Interna / 100 \(sem sinal negativo\)

__       \[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o resultado acima em 6 decimais\.

__\[MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772, 773, 774 – Furto, Perda, Uso baixa c/ Ressarc:

Preencher com Zero\.

- Para Cód\. Operação = 775, 776, 777 – Furto, Perda, Uso baixa s/ Ressarc:

Preencher com Zero\.

__        MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com Zero\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

Preencher com Zero\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com Zero\.

Onde:

- __Alíquota Interna__ da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Data de Emissão da Saída \(pode considerada a parametrização vigente no período informado na tela da geração\);
- \(__BC\-Saída__\): “Valor Unitário da BC ICMS Conv \([BC\-Saída](#BC_SAIDA)\)”

Ver  [__*Detalhamento da Nota de Saída*__](#Detalhamento_Nota_Saída)\.

Vlr Unit ICMS Operação Conv \(C185\-10\)

Vlr Unit ICMS Operação Conv \(C380\-06\)

20

Responsável Retenção \(Entradas\)

Campo da EFD corresponde: 02 \(C180\)

IND\_RESP\_RET\_ENT

Não Preencher\. Esse campo da SAFX296 é utilizado nas notas de entradas\.

Não Apresentar

Não Apresentar

21

Valor Unitário BC ICMS\-ST Conv\. \(Entradas\)

Campo da EFD corresponde: 07 \(C180\)

VLR\_UNIT\_BC\_ICMSS\_ENT

Não Preencher\. Esse campo da SAFX296 é utilizado nas notas de entradas\.

Não Apresentar

Não Apresentar

22

Valor Unitário ICMS\-ST Conv\.  \(Entradas\)

Campo da EFD corresponde: 08 \(C180\)\.

VLR\_UNIT\_ICMSS\_CONV\_ENT

Não Preencher\. Esse campo da SAFX296 é utilizado nas notas de entradas\.

Não Apresentar

Não Apresentar

23

Valor Unitário FCP\-ST Conv\.  \(Entradas\)

Campo da EFD corresponde: 09 \(C180\)\.

VLR\_UNIT\_FCP\_CONV\_ENT

Não Preencher\. Esse campo da SAFX296 é utilizado nas notas de entradas\.

Não Apresentar

Não Apresentar

 

24

Código Motivo \(Saídas\)

Campos da EFD correspondes: 06 \(C185\) e 02 \(C380\)\.

COD\_MOTIVO\_SAI

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

__\[MFS96666\]: Inclusão dos códigos RS101, \.\.\., RS156 e RS301, \.\.\., RS356 partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com __RS100__ quando for restituição\.

          Preencher com __RS300 __quando for complemento\.__ __

       Para período da geração a partir de Jan\-2023, então:

          Preencher com __RS100 __ou __RS101, \.\.\., RS156__ quando for restituição\.

          Preencher com __RS300 __ou __RS301, \.\.\., RS356__ quando for complemento\.

__       __Vide “[Regra p/ Operação de Saída Interna p/ Consumidor Final](#COD_MOTIVO_CONS_FINAL)”\(\*\)\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772 – Furto baixa c/ Ressarc: 

Preencher com RS211\.

- Para Cód\. Operação = 773 – Perda baixa c/ Ressarc:

Preencher com RS212\.

- Para Cód\. Operação = 774 – Uso baixa c/ Ressarc:

Preencher com RS215\.

- Para Cód\. Operação = 775 – Furto baixa s/ Ressarc:

Preencher com RS011\.

- Para Cód\. Operação = 776 – Perda baixa s/ Ressarc:

Preencher com RS012\.

- Para Cód\. Operação = 777 – Uso baixa s/ Ressarc:

Preencher com RS015\.

- Para Cód\. Operação = 778 – Outra UF:

Preencher com RS213\.

- Para Cód\. Operação = 781 – Exportação:

Preencher com RS214\.

- Para Cód\. Operação = 782 – Nova ST:

Preencher com RS217\.

- Para Cód\. Operação = 783 – Isenção:

Preencher com RS219\.

- Para Cód\. Operação = 779 – Outra UF Art 24:

Preencher com RS001\.

- Para Cód\. Operação = 784 – Isenção Art 24\-A:

Preencher com RS001\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com RS000\.

<a id="COD_MOTIVO_CONS_FINAL"></a>\(\*\) Regra p/ Operação de Saída Interna p/ Consumidor Final:

__\[MFS\-63471\]__ A regra original foi feita baseada no Ressarcimento MG, onde eram comparadas as bases \(BC Entrada e BC Saída\) para determinar se houve ressarcimento ou complemento\. Conceitualmente não havia erro nessa abordagem só que, na prática, um cenário apresentou divergência entre o resultado da comparação pela base e o valor em si calculado para complemento/ressarcimento\.

O cenário foi: \[BC Saída > BC Entrada\] e \[\(ICMS Saída\) < \(ICMS Entrada \+ ICMS\-ST Entrada\)\]\.

Pela comparação de bases, o resultado deu complemento, mas ao calcular o valor do complemento no campo 31, o valor deu negativo, veja fórmula:

 \(ICMS Saída \(VLR\_ICMS\_CONV\) \- 

  ICMS Entrada \(VLR\_UNIT\_ICMS\_ESTQ\_SAI\) \- 

  ICMS\-ST Entrada \(VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) 

O valor negativo demonstra que na verdade temos ressarcimento, pois a soma dos valores das entradas foi maior que da saída\. 

Sendo assim alteramos a regra para utilizarmos como comparação os próprios valores de ICMS e ICMS\-ST de Saída e Entrada, em substituição BC\-Entrada e BC\-Saída

__\[MFS96666\]: Inclusão dos códigos RS101, \.\.\., RS156 e RS301, \.\.\., RS356 a partir de Jan\-2023:__

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_ICMS\_CONV > 0 \(entrada > saída = ressarcimento\) então:

       A saída obteve Restituição;

       Para período da geração anterior a Jan\-2023, então:

          Preencher com __RS100__\.

       Para período da geração a partir de Jan\-2023, então:

          Preencher com __RS100__, para operação sem redução de base de cálculo;

          Preencher com “__RS101”__, \.\.\., “__RS105__”, para operação com alíquota interna reduzida;

          Preencher com “__RS151, __\.\.\., __RS156__, para operação com % redução de base de cálculo;

          Veja “[Regra para Códigos Motivo Consumidor Final 2023](#Regra_COD_MOTIVO_2023)” [\(\*\*\)](#Regra_COD_MOTIVO_2023)

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_ICMS\_CONV < 0 \(entrada < saída = complemento\) então:

       A saída obteve Complemento;

       Para período da geração anterior a Jan\-2023, então:

          Preencher com __RS300__\.__ __

       Para período da geração a partir de Jan\-2023, então:

          Preencher com __RS300__, para operação sem redução de base de cálculo;

          Preencher com “__RS301”__, \.\.\., “__RS305__”, para operação com alíquota interna reduzida;

          Preencher com “__RS351, __\.\.\., __RS356__, para operação com % redução de base de cálculo;

          Veja “[Regra para Códigos Motivo Consumidor Final 2023](#Regra_COD_MOTIVO_2023)” [\(\*\*\)](#Regra_COD_MOTIVO_2023)

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) – 

    VLR\_ICMS\_CONV = 0 \(entrada = saída\) então: \(\*\*\*\)

       A saída não teve nem Restituição nem Complemento\.

       Para período da geração anterior a Jan\-2023, então:

          Preencher com __RS100__\.

       Para período da geração a partir de Jan\-2023, então:

          Preencher com __RS100__, para operação sem redução de base de cálculo;

          Preencher com “__RS101”__, \.\.\., “__RS105__”, para operação com alíquota interna reduzida;

          Preencher com “__RS151, __\.\.\., __RS156__, para operação com % redução de base de cálculo;

          Veja “[Regra para Códigos Motivo Consumidor Final 2023](#Regra_COD_MOTIVO_2023)” [\(\*\*\)](#Regra_COD_MOTIVO_2023)

__\[MFS96666\]: Inclusão dos códigos RS101, \.\.\., RS156 e RS301, \.\.\., RS356 a partir de Jan\-2023:__

Essa regra considera o campo “Código do Amparo/Texto/Ocorrência ICMS\-ST” do item de Mercadoria Documento Fiscal \(item 66 – COD\_OBS\_VCONT\_ITEM da SAFX08\)\.

\(\*\*\) <a id="Regra_COD_MOTIVO_2023"></a>Regra para Códigos Motivo Consumidor Final 2023

          \- Se Cod\_Amparo = \(4601 ou 4623 ou 4629 ou 4651 ou 4652 ou 4665\) então:

              Preencher com RS101 quando ressarcimento;

              Preencher com RS301 quando complemento;

          \- Se Cod\_Amparo = 4613 então: 

              Preencher com RS102 quando ressarcimento;

              Preencher com RS302 quando complemento;

          \- Se Cod\_Amparo = 4614 então: 

              Preencher com RS103 quando ressarcimento;

              Preencher com RS303 quando complemento;

          \- Se Cod\_Amparo = \(4620 ou 4624 ou 4662 ou 4681\) então: 

              Preencher com RS104 quando ressarcimento;

              Preencher com RS304 quando complemento;

          \- Se Cod\_Amparo = 4663b então: 

              Preencher com RS105 quando ressarcimento;

              Preencher com RS305 quando complemento;

          \- Se Cod\_Amparo = “4616” então:

               Preencher c/ RS151 quando ressarcimento;

               Preencher c/ RS351 quando complemento;

          \- Se Cod\_Amparo = “4617a1” então: 

              Preencher c/ RS152 quando ressarcimento;

              Preencher c/ RS352 quando complemento;

          \- Se Cod\_Amparo = \(“4617a2” ou “4617b3” ou “4656b”\) então:

              Preencher c/ RS153 quando ressarcimento;

              Preencher c/ RS353 quando complemento;

          \- Se Cod\_Amparo = “4617b1” então: 

              Preencher c/ RS154 quando ressarcimento;

              Preencher c/ RS354 quando complemento;

          \- Se Cod\_Amparo = \(“4617b2” ou “4656a"\) então: 

              Preencher c/ RS155 quando ressarcimento;

              Preencher c/ RS355 quando complemento;

          \- Se Cod\_Amparo = “__4617b4__” então: 

               Preencher c/ RS156 quando ressarcimento;

               Preencher c/ RS356 quando complemento;

          \- Se Cod\_Amparo não estiver preenchido ou for diferente dos acima mencionados então: 

             Preencher com RS100 quando ressarcimento;

             Preencher com RS300 quando complemento;

          Se “__%Redução BC__” preenchido e Código Amparo não preenchido ou diferente dos acima mencionados, então: 

               Exibir a mensagem de aviso no relatório de Log:

*“Registro XXXX: Documento Fiscal com base de cálculo reduzida foi gerado código de motivo RS100 ou RS300, pois faltou informação no campo Amparo/Texto/Ocorrência \(ST\) no item de mercadoria, ou este foi preenchido com um código de Amparo cujo inciso não está acobertado pela tabela 5\.7 do Sped Fiscal\. Reveja o % de Redução BC parametrizado para o Produto, acessando uma das opções disponíveis no menu Parâmetros >> Produtos \(Por Código, Por NCM ou Por CEST\) e o Amparo Legal \(ST\) do Item de Mercadoria \(item 66 da SAFX08\)\. *

*Consulte o manual operacional do módulo para obter esclarecimentos sobre a correlação dos códigos de Amparo Legal com o % de Redução BC\.”*

              Onde XXXX é deve substituído por:

              \- “C185”: para Nota Fiscal de modelos 01, 1B, 04, 55, 65\.

              \- “C380”: para Notas Fiscais de modelo 02

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Saída \+ % Redução BC parametrizado \+ Código do Amparo do item de mercadoria\.

Onde:

- \([BC\-Entrada](#BC_ENTRADA)\) = “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

É o valor unitário médio móvel da BC ICMS\-ST calculado para o Produto na Data de Emissão da nota de saída\.

- \(BC\-Saída\): “Valor Unitário da BC ICMS Conv \([BC\-Saída](#BC_SAIDA)\)”
- %Redução BC e Alíquota Interna da parametrização de Produto por Código ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Emissão da Saída \(pode considerada a parametrização vigente no período informado na tela da geração\);

Ver  [__*Detalhamento da Nota de Saída*__](#Detalhamento_Nota_Saída)\.

\(\*\*\*\) 12/01/2021: Consulta foi realizada a nossa Área da Informação \(CAN\) que explicou que conceitualmente esse cenário não existe, por isso o fisco foi omisso e não especificou tratamento\. Como sistemicamente isso pode ocorrer, o tratamento que foi dado é emissão de mensagem no log\. Nesse caso, o cliente deve revisar sua nota\.

\[__MFS64550\]: __O fisco definiu que a nota sem ressarcimento e complemento seja apresenta\. O validador da GIA\-RS já está considerando a nota sem ressarcimento e complemento com código “__RS100__”\. 

Cod Motivo \(C185\-06\)

Cod Motivo \(C380\-02\)

 

25

Valor Unitário ICMS na Oper\. Conv\. \(Saídas\)

Campos da EFD correspondes: 11 \(C185\) e 07 \(C380\)\.

VLR\_UNIT\_ICMS\_OPER\_SAI

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

       Preencher com Zero\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772, 773, 774 – Furto, Perda, Uso baixa c/ Ressarc:

Preencher com o valor atribuído ao campo 26\-VLR\_UNIT\_ICMS\_ESTQ\_SAI\.

- Para Cód\. Operação = 775, 776, 777 – Furto, Perda, Uso baixa s/ Ressarc:

Preencher com Zero\.

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com Zero\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

Preencher com Zero\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com Zero\.

Vlr Unit ICMS Op Conv \(C185\-11\)

Vlr Unit ICMS Op Conv \(C380\-07\)

26

Valor Unitário ICMS Estoque Conv\. \(Saídas\)

Campos da EFD correspondes: 12 \(C185\) e 08 \(C380\)\.

VLR\_UNIT\_ICMS\_ESTQ\_SAI

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher com “Valor Médio Unitário do ICMS” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

__\[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:__

Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no tópico [2\.3](#_2.3_–_Recuperação) for negativo, então:

    Desconsiderar a regra acima e preencher este campo com ZERO\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772, 773, 774 – Furto, Perda, Uso baixa c/ Ressarc:

Preencher com “Valor Médio Unitário do ICMS” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

- Para Cód\. Operação = 775, 776, 777 – Furto, Perda, Uso baixa s/ Ressarc:

__\[MFS96666\]: RS0xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

          Preencher com “Valor Médio Unitário do ICMS” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com “Valor Médio Unitário do ICMS” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

__\[MFS96666\]: RS0xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

          Preencher com “Valor Médio Unitário do ICMS” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

__\[MFS96666\]: RS0xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

   Preencher com “Valor Médio Unitário do ICMS” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

Onde:

- O valor unitário médio móvel do ICMS é calculado para o Produto na Data de Emissão da nota de saída\.

__\[MFS90131\]__ arredondar para 6 casas decimais o valor médio unitário recuperado da Média Ponderada pois compõe o layout do C185\.

Vlr Unit ICMS Estoque Conv \(C185\-12\)

Vlr Unit ICMS Estoque Conv \(C380\-08\)

27

Valor Unitário ICMS\-ST Estoque Conv\. \(Saídas\)

Campos da EFD correspondes: 13 \(C185\) e 09 \(C380\)\.

VLR\_UNIT\_ICMSS\_ESTQ\_SAI

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher com:

__\[MFS66171\]__

\[“Valor Médio Unitário do ICMS\-ST” \+ Valor Médio Unitário do FECEP\-ST\] 

“Valor Médio Unitário do ICMS\-ST c/ FECEP”

Tais valores são recuperados no tópico [2\.3](#_2.3_–_Recuperação)\.

__\[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:__

Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no tópico [2\.3](#_2.3_–_Recuperação) for negativo, então:

    Desconsiderar a regra acima e preencher este campo com ZERO\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772, 773, 774 – Furto, Perda, Uso baixa c/ Ressarc:

Preencher com:

__\[MFS66171\]__

\[“Valor Médio Unitário do ICMS\-ST” \+ Valor Médio Unitário do FECEP\-ST\] 

“Valor Médio Unitário do ICMS\-ST c/ FECEP”

Tais valores são recuperados no tópico [2\.3](#_2.3_–_Recuperação)\.

- Para Cód\. Operação = 775, 776, 777 – Furto, Perda, Uso baixa s/ Ressarc:

__\[MFS96666\]: RS0xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

   Preencher com “Valor Médio Unitário do ICMS\-ST c/ FECEP” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

- __MFS64191__

Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com:

__\[MFS66171\]__

\[“Valor Médio Unitário do ICMS\-ST” \+ Valor Médio Unitário do FECEP\-ST\] 

\[“Valor Médio Unitário do ICMS\-ST c/ FECEP”\] 

Tais valores são recuperados no tópico [2\.3](#_2.3_–_Recuperação)\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

__\[MFS96666\]: RS0xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

   Preencher com “Valor Médio Unitário do ICMS\-ST c/ FECEP” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

__\[MFS96666\]: RS0xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

   Preencher com “Valor Médio Unitário do ICMS\-ST c/ FECEP” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

Onde:

- Os valores unitários médios móvel do ICMS\-ST e do FECEP\-ST são calculados para o Produto na Data de Emissão da nota de saída\.

__\[MFS90131\]__ arredondar para 6 casas decimais o valor médio unitário recuperado da Média Ponderada pois compõe o layout do C185\.

Vlr Unit ICMS\-ST Estoque Conv \(C185\-13\)

Vlr Unit ICMS\-ST Estoque Conv \(C380\-09\)

28

Valor Unitário FCP\-ST Estoque Conv\. \(Saídas\)

Campos da EFD correspondes: 14 \(C185\) e 10 \(C380\)\.

VLR\_UNIT\_FCP\_ESTQ\_SAI

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher com “Valor Médio Unitário do FECEP\-ST” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

__\[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:__

Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no tópico [2\.3](#_2.3_–_Recuperação) for negativo, então:

    Desconsiderar a regra acima e preencher este campo com ZERO\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772, 773, 774 – Furto, Perda, Uso baixa c/ Ressarc:

Preencher com “Valor Médio Unitário do FECEP\-ST” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

- Para Cód\. Operação = 775, 776, 777 – Furto, Perda, Uso baixa s/ Ressarc:

__\[MFS96666\]: RS0xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

   Preencher com “Valor Médio Unitário do FECEP\-ST” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com “Valor Médio Unitário do FECEP\-ST” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

__\[MFS96666\]: RS0xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

   Preencher com “Valor Médio Unitário do FECEP\-ST” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

__\[MFS96666\]: RS0xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

   Preencher com “Valor Médio Unitário do FECEP\-ST” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

Onde:

- O valor unitário médio móvel do FECEP\-ST é calculado para o Produto na Data de Emissão da nota de saída\.

__\[MFS90131\]__ arredondar para 6 casas decimais o valor médio unitário recuperado da Média Ponderada pois compõe o layout do C185\.

Vlr Unit FCP\-ST Estoque Conv \(C185\-14\)

Vlr Unit FCP\-ST Estoque Conv \(C380\-10\)

29

Valor Unitário ICMS\-ST Conv\. Rest\. \(Saídas\)

Campos da EFD correspondes: 15 \(C185\) e 11 \(C380\)\.

VLR\_UNIT\_ICMSS\_REST\_SAI

Campo deve ser preenchido no caso da saída ser objeto de Restituição\.

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher com o Valor da Restituição\.

Vide “[Regra p/ Operação de Saída Interna p/ Consumidor Final](#REST_CONS_FINAL)”\(\*\)\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772, 773, 774 – Furto, Perda, Uso baixa c/ Ressarc:

Preencher com o Valor da Restituição\.

Vide “[Regra p/ Operação de Furto, Perda, Uso baixa c/ Ressarc](#REST_FURTO)”\(\*\*\)\.

- Para Cód\. Operação = 775, 776, 777 – Furto, Perda, Uso baixa s/ Ressarc:

Preencher com Zero\.

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com o Valor da Restituição\.

Vide “[Regra p/ Operação de Outra UF, Exportação, Nova ST, Isenção](#REST_OUT_UF)”\(\*\*\*\)\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

Preencher com Zero\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com Zero\.

<a id="REST_CONS_FINAL"></a>\(\*\) Regra p/ Operação de Saída Interna p/ Consumidor Final:

__\[MFS\-63471\]__ Não utilizar as bases \(BC\-Entrada e BC\-Saída\) na comparação para identificar se houve ressarcimento ou complemento\. Usar os próprios valores de ICMS e ICMS\-ST de Saída e Entrada\.

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_ICMS\_CONV > 0 \(entrada > saída = ressarcimento\) então:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ 

    VLR\_UNIT\_ICMSS\_ESTQ\_SAI – 

    VLR\_ICMS\_CONV 

    Onde:

- VLR\_ICMS\_CONV: valor gravado no campo 19\- Valor Unitário ICMS Conv\.;
- VLR\_UNIT\_ICMS\_ESTQ\_SAI : valor gravado no campo 26\- Valor Unitário ICMS Estoque Conv\. \(Saídas\);
- VLR\_UNIT\_ICMSS\_ESTQ\_SAI: valor gravado no campo 27\- Valor Unitário ICMS\-ST Estoque Conv\. \(Saídas\);

Senão

    Não preencher;

- \([BC\-Entrada](#BC_ENTRADA)\) = “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

É o valor unitário médio móvel da BC ICMS\-ST calculado para o Produto na Data de Emissão da nota de saída\.

- \(BC\-Saída\): “Valor Unitário da BC ICMS Conv \([BC\-Saída](#BC_SAIDA)\)”

Ver  [__*Detalhamento da Nota de Saída*__](#Detalhamento_Nota_Saída)\.

<a id="REST_FURTO"></a>\(\*\*\) Regra p/ Operação de Furto, Perda, Uso baixa c/ Ressarc:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ 

    VLR\_UNIT\_ICMSS\_ESTQ\_SAI – 

    VLR\_UNIT\_ICMS\_OPER\_SAI

    Onde:

- VLR\_UNIT\_ICMS\_OPER\_SAI: valor gravado no campo 25\- Valor Unitário ICMS na Oper\. Conv\. \(Saídas\);
- VLR\_UNIT\_ICMS\_ESTQ\_SAI : valor gravado no campo 26\- Valor Unitário ICMS Estoque Conv\. \(Saídas\);
- VLR\_UNIT\_ICMSS\_ESTQ\_SAI: valor gravado no campo 27\- Valor Unitário ICMS\-ST Estoque Conv\. \(Saídas\);

<a id="REST_OUT_UF"></a>\(\*\*\*\) Regra p/ Operação de Outra UF, Exportação, Nova ST, Isenção:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ 

    VLR\_UNIT\_ICMSS\_ESTQ\_SAI 

    Onde:

- VLR\_UNIT\_ICMS\_ESTQ\_SAI : valor gravado no campo 26\- Valor Unitário ICMS Estoque Conv\. \(Saídas\);
- VLR\_UNIT\_ICMSS\_ESTQ\_SAI: valor gravado no campo 27\- Valor Unitário ICMS\-ST Estoque Conv\. \(Saídas\);

Validação:

Caso o valor gravado no campo seja negativo, exibir mensagem de aviso no log:

Para Nota Fiscal de Saída de modelos 01, 1B, 04, 55, 65:

*“Registro C185: Nota de Saída gerada com valor unitário do ressarcimento negativo\.”*

Para Nota Fiscal de Saída de modelo 02:

*“Registro C380: Nota de Saída gerada com valor unitário do ressarcimento negativo\.”*

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Saída\. 

Vlr Unit ICMS\-ST Conv Rest \(C185\-15\)

Vlr Unit ICMS\-ST Conv Rest \(C380\-11\)

30

Valor Unitário FCP\-ST Conv\. Rest\. \(Saídas\)

Campos da EFD correspondes: 16 \(C185\) e 12 \(C380\)\.

VLR\_UNIT\_FCP\_REST\_SAI

Campo deve ser preenchido no caso da saída ser objeto de Restituição\.

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher com o Valor do FECEP p/ Restituição\.

Vide “[Regra p/ Operação de Saída Interna p/ Consumidor Final](#FECEP_CONS_FINAL)”\(\*\)\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772, 773, 774 – Furto, Perda, Uso baixa c/ Ressarc:

Preencher com o Valor do FECEP p/ Restituição\.

Vide “[Regra p/ Operação de Furto, Perda, Uso baixa c/ Ressarc](#FECEP_FURTO)”\(\*\*\)\.

- Para Cód\. Operação = 775, 776, 777 – Furto, Perda, Uso baixa s/ Ressarc:

Preencher com Zero\.

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com o Valor do FECEP p/  Restitiução\.

Vide “[Regra p/ Operação de Outra UF, Exportação, Nova ST, Isenção](#FECEP_OUT_UF)”\(\*\*\*\)\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

Preencher com Zero\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com Zero\.

<a id="FECEP_CONS_FINAL"></a>\(\*\) Regra p/ Operação de Saída Interna p/ Consumidor Final:

__\[MFS\-63471\]__ Não utilizar as bases \(BC Entrada e BC Saída\) na comparação para identificar se houve ressarcimento ou complemento\. Usar os próprios valores de ICMS e ICMS\-ST de Saída e Entrada\.

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_ICMS\_CONV > 0 \(entrada > saída = ressarcimento\) então:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMSS\_REST\_SAI \* Alíquota FCP / 100

    Onde:

- VLR\_UNIT\_ICMSS\_REST\_SAI: valor gravado no campo 29\- Valor Unitário ICMS\-ST Conv\. Rest\. \(Saídas\);
- Alíquota FCP da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Data de Emissão da Saída \(pode considerada a parametrização vigente no período informado na tela da geração\);

Senão:

    Não preencher;

<a id="FECEP_FURTO"></a>\(\*\*\) Regra p/ Operação de Furto, Perda, Uso baixa c/ Ressarc:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMSS\_REST\_SAI \* Alíquota FCP / 100

   Onde:

- VLR\_UNIT\_ICMSS\_REST\_SAI: valor gravado no campo 29\- Valor Unitário ICMS\-ST Conv\. Rest\. \(Saídas\);
- Alíquota FCP da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Data de Emissão da Saída \(pode considerada a parametrização vigente no período informado na tela da geração\);

<a id="FECEP_OUT_UF"></a>\(\*\*\*\) Regra p/ Operação de Outra UF, Exportação, Nova ST, Isenção:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMSS\_REST\_SAI \* Alíquota FCP / 100

    Onde:

- VLR\_UNIT\_ICMSS\_REST\_SAI: valor gravado no campo 29\- Valor Unitário ICMS\-ST Conv\. Rest\. \(Saídas\);
- Alíquota FCP da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Data de Emissão da Saída \(pode considerada a parametrização vigente no período informado na tela da geração\);

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o resultado acima em 6 decimais\.

Vlr Unit FCP\-ST Conv Rest \(C185\-16\)

Vlr Unit FCP\-ST Conv Rest \(C380\-12\)

31

Valor Unitário ICMS\-ST Conv\. Compl\. \(Saídas\)

Campos da EFD correspondes: 17 \(C185\) e 13 \(C380\)\.

VLR\_UNIT\_ICMSS\_COMPL\_SAI

Campo deve ser preenchido no caso da saída ser objeto de Complementação\.

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher com o Valor da Complementação\.

Vide “[Regra p/ Operação de Saída Interna p/ Consumidor Final](#COMPL_CONS_FINAL)”\(\*\)\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772, 773, 774 – Furto, Perda, Uso baixa c/ Ressarc:

Preencher com Zero\.

- Para Cód\. Operação = 775, 776, 777 – Furto, Perda, Uso baixa s/ Ressarc:

Preencher com Zero\.

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com Zero\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

Preencher com Zero\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com Zero\.

<a id="COMPL_CONS_FINAL"></a>\(\*\) Regra p/ Operação de Saída Interna p/ Consumidor Final:

__\[MFS\-63471\]__ Não utilizar as bases \(BC Entrada e BC Saída\) na comparação para identificar se houve ressarcimento ou complemento\. Usar os próprios valores de ICMS e ICMS\-ST de Saída e Entrada\.

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_ICMS\_CONV < 0 \(entrada < saída = complemento\) então:

    Preencher com o resultado da fórmula:

    VLR\_ICMS\_CONV \-

    VLR\_UNIT\_ICMS\_ESTQ\_SAI \- 

    VLR\_UNIT\_ICMSS\_ESTQ\_SAI 

    

    Onde:

- VLR\_ICMS\_CONV: valor gravado no campo 19\- Valor Unitário ICMS Conv\.;
- VLR\_UNIT\_ICMS\_ESTQ\_SAI: valor gravado no campo 26\- Valor Unitário ICMS Estoque Conv\. \(Saídas\);
- VLR\_UNIT\_ICMSS\_ESTQ\_SAI: valor gravado no campo 27\- Valor Unitário ICMS\-ST Estoque Conv\. \(Saídas\);

Senão:

    Não preencher;

Onde:

- \([BC\-Entrada](#BC_ENTRADA)\) = “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

É o valor unitário médio móvel da BC ICMS\-ST calculado para o Produto na Data de Emissão da nota de saída\.

- \(BC\-Saída\): “Valor Unitário da BC ICMS Conv \([BC\-Saída](#BC_SAIDA)\)”

Ver  [__*Detalhamento da Nota de Saída*__](#Detalhamento_Nota_Saída)\.

Validação:

Caso o valor gravado no campo seja negativo, exibir mensagem de aviso no log:

Para Nota Fiscal de Saída de modelos 01, 1B, 04, 55, 65:

*“Registro C185: Nota de Saída gerada com valor unitário do complemento negativo\.”*

Para Nota Fiscal de Saída de modelo 02:

*“Registro C380: Nota de Saída gerada com valor unitário do complemento negativo\.”*

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Saída\.

Vlr Unit ICMS\-ST Conv Compl \(C185\-17\)

Vlr Unit ICMS\-ST Conv Compl \(C380\-13\)

32

Valor Unitário FCP\-ST Conv\. Compl\. \(Saídas\)

Campos da EFD correspondes: 18 \(C185\) e 14 \(C380\)\.

VLR\_UNIT\_FCP\_COMPL\_SAI

Campo deve ser preenchido no caso da saída seja objeto de Complementação\.

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher com o Valor da Complementação FECEP\.

Vide “[Regra p/ Operação de Saída Interna p/ Consumidor Final](#COMPL_FECEP_CONS_FINAL)”\(\*\)\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772, 773, 774 – Furto, Perda, Uso baixa c/ Ressarc:

Preencher com Zero\.

- Para Cód\. Operação = 775, 776, 777 – Furto, Perda, Uso baixa s/ Ressarc:

Preencher com Zero\.

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com Zero\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

Preencher com Zero\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com Zero\.

<a id="COMPL_FECEP_CONS_FINAL"></a>\(\*\) Regra p/ Operação de Saída Interna p/ Consumidor Final:

__\[MFS\-63471\]__ Não utilizar as bases \(BC Entrada e BC Saída\) na comparação para identificar se houve ressarcimento ou complemento\. Usar os próprios valores de ICMS e ICMS\-ST de Saída e Entrada\.

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_ICMS\_CONV < 0 \(entrada < saída = complemento\) então:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMSS\_COMPL\_SAI \* Alíquota FCP / 100

    Onde:

- VLR\_UNIT\_ICMSS\_C0MPL\_SAI: valor gravado no campo 31\- Valor Unitário ICMS\-ST Conv\. Compl\. \(Saídas\);
- Alíquota FCP da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Data de Emissão da Saída \(pode considerada a parametrização vigente no período informado na tela da geração\);

Senão:

    Não preencher;

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o resultado acima em 6 decimais\.

Vlr Unit FCP\-ST Conv Compl \(C185\-18\)

Vlr Unit FCP\-ST Conv Compl \(C380\-14\)

__*Parametrização do Produto \(por Código, NCM ou CEST\)*__

Produto da NF 

GRUPO\_PROD\_NF

IND\_PROD\_NF

COD\_PROD\_NF

Produto do item da nota de Saída\.

Ind Produto

\(SAFX2013\-01\)

Cod Produto \(SAFX2013\-02\)

Ind Produto

\(SAFX2013\-01\)

Cod Produto \(SAFX2013\-02\)

Unidade de Medida do Produto NF

COD\_MEDIDA\_PROD\_NF

Unidade de Medida do Produto da nota de Saída \(SAFX2013 – campo 14 – COD\_MEDIDA\)

Medida Produto \(SAFX2013\-14\)

Medida Produto \(SAFX2013\-14\)

NCM do Produto NF

COD\_NBM\_PROD\_NF

Código NBM do Produto da nota de Saída \(SAFX2013 – campo 05 – Código NBM\)

NCM Produto \(SAFX2013\-05\)

NCM Produto \(SAFX2013\-05\)

CEST do Produto NF

COD\_CEST\_PROD\_NF

Código CEST do Produto da nota de Saída \(SAFX2013 – campo 54 – Código Especificador da Substituição Tributária\)

CEST Produto \(SAFX2013\-54\)

CEST Produto \(SAFX2013\-54\)

Produto Principal

GRUPO\_PROD\_PRINC

IND\_PROD\_PRINC

COD\_PROD\_PRINC

Caso o produto do item da nota de saída tenha sido parametrizado por Código \(menu “Parâmetros à Produtos à Por Código”\) apresentar o Produto Principal \(grupo, indicador e código\)\.

Não Apresentar

Não Apresentar

Unidade de Medida do Produto Principal

COD\_MEDIDA\_PROD\_PRINC

Caso o produto do item da nota de saída tenha sido parametrizado por Código \(menu “Parâmetros à Produtos à Por Código”\) apresentar a Unidade de Medida do Produto Principal \(SAFX2013 – campo 14 – COD\_MEDIDA\)\.

Não Apresentar

Não Apresentar

%Redução BC

PRC\_REDUCAO\_BC

%Redução BC da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Emissão da Saída \(pode considerada a parametrização vigente no período informado na tela da geração\);

%Redução BC \(Parametrização Produto\)

%Redução BC \(Parametrização Produto\)

Alíquota Interna

ALIQ\_INTERNA

Alíquota Interna da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Emissão da Saída \(pode considerada a parametrização vigente no período informado na tela da geração\);

Alíq\. Interna \(Parametrização Produto\)

Alíq\. Interna \(Parametrização Produto\)

Alíquota FCP

ALIQ\_FCP

Alíquota FCP da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Emissão da Saída \(pode considerada a parametrização vigente no período informado na tela da geração\);

Alíq\. FCP \(Parametrização Produto\)

Alíq\. FCP \(Parametrização Produto\)

<a id="Detalhamento_Nota_Saída"></a>__*Detalhamento da Nota de Saída *__

Quantidade do Item da NF de Saída \(safx08 – item 24\)

QTD\_NF\_SAI

Campo 24\-Quantidade \(SAFX08\) do item da nota fiscal de Saída\.

Qtde Item \(SAFX08\-24\)

Qtde Item \(SAFX08\-24\)

Quantidade Convertida do Item da NF de Saída \(safx08 – item137\)

QTD\_CONV\_X08\_NF\_SAI

Campo 137 – Quantidade Convertida \(SAFX08\) do item da nota fiscal de Saída

Qtde Conv Item \(SAFX08\-137\)

Qtde Conv Item \(SAFX08\-137\)

Unidade de Medida do Item da NF de Saída 

\(safx08 \- item 25\)

COD\_MEDIDA\_NF\_SAI

Campo 25 – Unidade de Medida \(SAFX08\) do item da nota fiscal de Saída\.

Medida Item \(SAFX08\-25\)

Medida Item \(SAFX08\-25\)

Fator Conversão

FAT\_CONV\_NF\_SAI

Preecher com o Fator de Conversão utilizado na regra do campo “Qtde Convertida Calculada para o Item da NF de Saída \(QTD\_CONV\_NF\_SAI\)” a seguir\.

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

Fator Conv \(Cadastro Conversão Medida\)

Fator Conv \(Cadastro Conversão Medida\)

Qtde Convertida Calculada para o Item da NF de Saída

\(<a id="QTD_CONV_NF_SAI"></a>QTD\_CONV\_NF\_SAI\)

QTD\_CONV\_NF\_SAI

Campo 24\-Quantidade \(SAFX08\) do Item da nota de Saída, aplicando a conversão, quando necessário\. Veja:

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

         \[  Quantidade do item da nota \(SAFX08\) \* Fator de Conversão \]

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

Para Nota Fiscal de Saída de modelos 01, 1B, 04, 55, 65:

“*Registro C185: Fator de conversão de medida de XXX para XXX não encontrado\. Nota de Saída será gerada no C185 sem Quantidade Convertida e valores unitários da Mercadoria e ICMS \(campos 7, 9 e 10\)”\.*

Para Nota Fiscal de Saída de modelos 02:

“*Registro C380: Fator de conversão de medida de XXX para XXX não encontrado\. Nota de Saída será gerada no C380 sem Quantidade Convertida e valores unitários da Mercadoria e ICMS \(campos 3, 5 e 6\)”\.*

\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Saída exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

Não Apresentar pois já é o campo Qtde Conv \(C185\-07\)

Não Apresentar pois já é o campo Qtde Conv \(C380\-03\)

Valor Contabil do Item de Saída

\(safx08 – item 64\)

VLR\_CONTAB\_SAI

Campo 64\-“Vlr Contabil do Item”\(SAFX08\) do item da nota fiscal de saída\.

Vlr Contabil Item \(SAFX08\-64\)

Vlr Contabil Item \(SAFX08\-64\)

Amparo Legal \(safx08\- item 66\)

COD\_AMPARO\_LEGAL

__\[MFS96666\]: Inclusão dos códigos RS101, \.\.\., RS156 e RS301, \.\.\., RS356 a partir de Jan\-2023:__

Campo 66 \- Código do Amparo/Texto/Ocorrência para ICMS de Substituição Tributária do item de mercadoria da nota fiscal de saída

Amparo Legal \(safx08\- item 66\)

Amparo Legal \(safx08\- item 66\)

Valor Unitário da BC ICMS Conv \(<a id="BC_SAIDA"></a>BC\-Saída\)

VLR\_BC\_ICMS\_SAI

Valor Unitário da BC do ICMS na Operação Conv, calculado conforme regra:

Se o campo “__%Redução BC__” da parametrização de Produto ou NCM ou CEST está preenchido com valor > 0, então:

     Este campo será gerado da seguinte forma:

     \[\(Vlr Contábil – \(Vlr Contábil \* “%Redução BC” / 100\)\)\]/ QTD\_CONV\_NF\_SAI

Senão:

      Este campo será gerado da seguinte forma:

      \[\(Vlr Contábil\)\] / QTD\_CONV\_NF\_SAI

Onde:

- %Redução BC da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Emissão da Saída \(pode considerada a parametrização vigente no período informado na tela da geração\);
- Vl Contábil = 64\-Vlr Contabil do Item da nota fiscal de saída\.
- [QTD\_CONV\_NF\_SAI](#QTD_CONV_NF_SAI): Qtde Convertida Calculada para o Item da NF de Saída\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o resultado acima em 6 decimais\.

Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\)

Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\)

__*Valores Unitários da Média Pondera Móvel do dia da operação de saída \(recuperada no tópico *__[__*2\.3*__](#_2.3_–_Recuperação)__*\.\)*__

Valor Médio Unitário do ICMS no dia Saída \(Tabela de Média Diária\)

VLR\_UNIT\_ICMS\_SAI

“Valor Médio Unitário do ICMS” recuperado no passo 1 do tópico [2\.3](#_2.3_–_Recuperação)\.  

__\[MFS90131\]__ mantém com 8 casas decimais o valor médio unitário recuperado da Média Ponderada\. Campo utilizado apenas para o relatório de conferência\.

Vlr Unit ICMS \(Recuperado da Média Ponderada\)

Vlr Unit ICMS \(Recuperado da Média Ponderada\)

Valor Médio Unitário do ICMS\-ST s/ FECEP no dia Saída \(Tabela de Média Diária\)

VLR\_UNIT\_ICMS\_ST\_SAI

__\[MFS66171\]__

“Valor Médio Unitário do ICMS\-ST s/ FECEP” recuperado no passo 1 do tópico [2\.3](#_2.3_–_Recuperação)\.

Campo VLR\_UNIT\_ICMS\_ST\_FIM\_MP da EST\_ST\_RS\_MEDIA\_POND\.

__\[MFS90131\]__ Mantém com 8 casas decimais o valor médio unitário recuperado da Média Ponderada\. Campo utilizado apenas para o relatório de conferência\.

Vlr Unit ICMS\-ST\(s/ FECEP\-ST\) \(Recuperado da Média Ponderada\)

Vlr Unit ICMS\-ST\(s/ FECEP\-ST\) \(Recuperado da Média Ponderada\)

Valor Médio Unitário do ICMS\-ST c/ FECEP no dia Saída \(Tabela de Média Diária\)

VLR\_UNIT\_ICMS\_ST\_FECEP\_SAI

__\[MFS66171__\]

“Valor Médio Unitário do ICMS\-ST c/ FECEP” recuperado no passo 1 do tópico [2\.3](#_2.3_–_Recuperação)\.

Campo VLR\_UNIT\_ICMS\_ST\_FECEP\_FIM\_MP da EST\_ST\_RS\_MEDIA\_POND\.

__\[MFS90131\]__ mantém com 8 casas decimais o valor médio unitário recuperado da Média Ponderada\. Campo utilizado apenas para o relatório de conferência\.

Vlr Unit ICMS\-ST\(c/ FECEP\-ST\) \(Recuperado da Média Ponderada\)

Vlr Unit ICMS\-ST\(c/ FECEP\-ST\) \(Recuperado da Média Ponderada\)

Valor Médio Unitário da Base de Cálculo do ICMS\-ST no dia Saída \(Tabela de Média Diária\)

\(<a id="BC_ENTRADA"></a>BC\-Entrada\)

VLR\_UNIT\_BC\_ST\_SAI

“Valor Médio Unitário da Base de Cálculo do ICMS\-ST” recuperado no passo 1 do tópico [2\.3](#_2.3_–_Recuperação)\.

__\[MFS90131\]__ mantém com 8 casas decimais o valor médio unitário recuperado da Média Ponderada\. Campo utilizado apenas para o relatório de conferência\.

Vlr Unit BC ICMS\-ST \(Recuperado da Média Ponderada\)

Vlr Unit BC ICMS\-ST \(Recuperado da Média Ponderada\)

Valor Médio Unitário do FECEP\-ST no dia Saída \(Tabela de Média Diária\)

VLR\_UNIT\_FECEP\_ST\_SAI

“Valor Médio Unitário do FECEP\-ST” recuperado no passo 1 do tópico [2\.3](#_2.3_–_Recuperação)\.

__\[MFS90131\]__ mantém com 8 casas decimais o valor médio unitário recuperado da Média Ponderada\. Campo utilizado apenas para o relatório de conferência\.

Vlr Unit FECEP\-ST \(Recuperado da Média Ponderada\)

Vlr Unit FECEP\-ST \(Recuperado da Média Ponderada\)

OBSERVAÇÃO

DSC\_OBS

\[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no tópico [2\.3](#_2.3_–_Recuperação) for negativo, então:

Preencher este campo com a observação:

“Valor médio ponderado móvel do dia negativo\. Campo Vlr Unit ICMS Operação Conv foi acrescido de 9999,99 e os campos Vlr Unit ICMS Estoque Conv, Vlr Unit ICMS\-ST Estoque Conv e Vlr Unit FCP\-ST Estoque Conv foram zerados\. Tratamento baseado no tópico 19\.3\-A\.2\.2\.2 da IN45/98\.”

Onde:

9999,99:

 VLR\_UNIT\_BC\_ST\_FIM\_MP \* Alíquota Interna / 100 \(sem sinal negativo\)

- Para os demais Cód\. Operação:

Não preencher\.

Observação

Observação

## <a id="_Toc71832846"></a>3\.2 – Gravação dos Cupons Fiscais \(C480\) 

__\[MFS\-65137\]__

Os itens dos Cupons Fiscais recuperados conforme tópico [2\.2](#_2.2_–_Recuperação) devem ser agrupados por Cupom/Produto e gravadas na tabela __EST\_ST\_RS\_ECF__ conforme regra a seguir:

__Tabela EST\_ST\_RS\_ECF__

Os campos sinalizados com asterisco compõem a chave da tabela\.

A estrutura da tabela __EST\_ST\_RS\_ECF__ é baseada na SAFX297\. Contém todos os campos da SAFX297 e campos a mais usados no relatório de conferência\.

PK

Item

SAFX297

Campo

Regra de Preenchimento

Campos para relatório

\(C480\)

\(\*\)

Código do Estabelecimento

COD\_ESTAB\_GER

Código do estabelecimento SELECIONADO na tela de geração\.

Esse campo foi criado, pois no futuro poderemos ter a geração por Inscrição Estadual Única, e nessa opção o estabelecimento selecionado na tela de geração é o centralizador, e as notas fiscais são dos estabelecimentos centralizador e centralizados\.

Não apresentar

__*Campos do layout da SAFX297 \(cupom fiscal\)*__

\(\*\)

01

Código da Empresa 

COD\_EMPRESA

Código da empresa do cupom fiscal \(SAFX993\) 

Cod Empresa

\(\*\)

02

Código do Estabelecimento

COD\_ESTAB

Código do estabelecimento do cupom fiscal \(SAFX993\)

Cod Estab

\(\*\)

03

Modelo do Documento

COD\_MODELO \(IDENT\_MODELO\)

Código do Modelo do cupom fiscal \(SAFX993\)

Cod Modelo

\(\*\)

04

Número do Caixa

COD\_CAIXA\_ECF \(IDENT\_CAIXA\_ECF\)

Número do Caixa ECF do cupom fiscal \(SAFX993\)

Num Caixa

\(\*\)

05

COO \(Contador de Ordem de Operação\)

NUM\_COO

Número do Contador de Ordem de Operação \(COO\) do cupom fiscal \(SAFX993\)

Num COO

\(\*\)

06

Data da Emissão

DATA\_EMISSAO

Data de emissão do cupom fiscal \(SAFX993\)

Dt Emissão

\(\*\)

07

08

Produto

IND\_PRODUTO/ COD\_PRODUTO

\(IDENT\_PRODUTO\)

Produto do item do cupom fiscal \(SAFX994\)

Ind Produto

Cod Produto

09

Código do Motivo

Campo da EFD correspondente: 02 do C480\.

Obs: mesma regra do C185 – 06\.

COD\_MOTIVO

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP do item do cupom \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

__\[MFS96666\]: Inclusão dos códigos RS101, \.\.\., RS156 e RS301, \.\.\., RS356 a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com __RS100__ quando for restituição\.

          Preencher com __RS300 __quando for complemento\.__ __

       Para período da geração a partir de Jan\-2023, então:

          Preencher com __RS100 __ou __RS101, \.\.\., RS156__ quando for restituição\.

          Preencher com __RS300 __ou __RS301, \.\.\., RS356__ quando for complemento\.

__       __Vide “[Regra p/ Operação de Saída Interna p/ Consumidor Final](#COD_MOTIVO_CONS_FINAL_CF)”\(\*\)\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772 – Furto baixa c/ Ressarc: 

Preencher com RS211\.

- Para Cód\. Operação = 773 – Perda baixa c/ Ressarc:

Preencher com RS212\.

- Para Cód\. Operação = 774 – Uso baixa c/ Ressarc:

Preencher com RS215\.

- Para Cód\. Operação = 775 – Furto baixa s/ Ressarc:

Preencher com RS011\.

- Para Cód\. Operação = 776 – Perda baixa s/ Ressarc:

Preencher com RS012\.

- Para Cód\. Operação = 777 – Uso baixa s/ Ressarc:

Preencher com RS015\.

- Para Cód\. Operação = 778 – Outra UF:

Preencher com RS213\.

- Para Cód\. Operação = 781 – Exportação:

Preencher com RS214\.

- Para Cód\. Operação = 782 – Nova ST:

Preencher com RS217\.

- Para Cód\. Operação = 783 – Isenção:

Preencher com RS219\.

- Para Cód\. Operação = 779 – Outra UF Art 24:

Preencher com RS001\.

- Para Cód\. Operação = 784 – Isenção Art 24\-A:

Preencher com RS001\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com RS000\.

<a id="COD_MOTIVO_CONS_FINAL_CF"></a>\(\*\) Regra p/ Operação de Saída Interna p/ Consumidor Final:

__\[MFS\-63471\]__ A regra original foi feita baseada no Ressarcimento MG, onde eram comparadas as bases \(BC Entrada e BC Saída\) para determinar se houve ressarcimento ou complemento\. Conceitualmente não havia erro nessa abordagem só que, na prática, um cenário apresentou divergência entre o resultado da comparação pela base e o valor em si calculado para complemento/ressarcimento\.

O cenário foi: \[BC Saída > BC Entrada\] e \[\(ICMS Saída\) < \(ICMS Entrada \+ ICMS\-ST Entrada\)\]\.

Pela comparação de bases, o resultado deu complemento, mas ao calcular o valor do complemento no campo 20, o valor deu negativo, veja fórmula:

 \(ICMS Saída \(VLR\_UNIT\_ICMS\_OPER\_CONV\) \- 

  ICMS Entrada \(VLR\_UNIT\_ICMS\_ESTQ\_CONV\) \- 

  ICMS\-ST Entrada \(VLR\_UNIT\_ICMSS\_ESTQ\_CONV\) 

O valor negativo demonstra que na verdade temos ressarcimento, pois a soma dos valores das entradas foi maior que da saída\. 

Sendo assim alteramos a regra para utilizarmos como comparação os próprios valores de ICMS e ICMS\-ST de Saída e Entrada, em substituição BC\-Entrada e BC\-Saída\.

__\[MFS96666\]: Inclusão dos códigos RS101, \.\.\., RS156 e RS301, \.\.\., RS356 a partir de Jan\-2023:__

Se \(VLR\_UNIT\_ICMS\_ESTQ\_CONV \+ VLR\_UNIT\_ICMSS\_ESTQ\_CONV\) \- 

    VLR\_UNIT\_ICMS\_OPER\_CONV > 0 \(entrada > saída = ressarcimento\) então:

       A saída obteve Restituição;

       Para período da geração anterior a Jan\-2023, então:

          Preencher com __RS100__\.

       Para período da geração a partir de Jan\-2023, então:

          Preencher com __RS100__, para operação sem redução de base de cálculo;

          Preencher com “__RS101”__, \.\.\., “__RS105__”, para operação com alíquota interna reduzida;

          Preencher com “__RS151, __\.\.\., __RS156__, para operação com % redução de base de cálculo;

          Veja “[Regra para Códigos Motivo Consumidor Final 2023](#Regra_COD_MOTIVO_CF_2023)” \(\*\*\)

Se \(VLR\_UNIT\_ICMS\_ESTQ\_CONV \+ VLR\_UNIT\_ICMSS\_ESTQ\_CONV\) \- 

    VLR\_UNIT\_ICMS\_OPER\_CONV < 0 \(entrada < saída = complemento\) então:

       A saída obteve Complemento;

       Para período da geração anterior a Jan\-2023, então:

          Preencher com __RS300__\.__ __

       Para período da geração a partir de Jan\-2023, então:

          Preencher com __RS300__, para operação sem redução de base de cálculo;

          Preencher com “__RS301”__, \.\.\., “__RS305__”, para operação com alíquota interna reduzida;

          Preencher com “__RS351, __\.\.\., __RS356__, para operação com % redução de base de cálculo;

          Veja “[Regra para Códigos Motivo Consumidor Final 2023](#Regra_COD_MOTIVO_CF_2023)” \(\*\*\)

Se \(VLR\_UNIT\_ICMS\_ESTQ\_CONV \+ VLR\_UNIT\_ICMSS\_ESTQ\_CONV\) – 

    VLR\_UNIT\_ICMS\_OPER\_CONV = 0 \(entrada = saída\) então: \(\*\*\)

       A saída não teve nem Restituição nem Complemento\.

       Para período da geração anterior a Jan\-2023, então:

          Preencher com __RS100__\.

       Para período da geração a partir de Jan\-2023, então:

          Preencher com __RS100__, para operação sem redução de base de cálculo;

          Preencher com “__RS101”__, \.\.\., “__RS105__”, para operação com alíquota interna reduzida;

          Preencher com “__RS151, __\.\.\., __RS156__, para operação com % redução de base de cálculo;

          Veja “[Regra para Códigos Motivo Consumidor Final 2023](#Regra_COD_MOTIVO_CF_2023)” \(\*\*\)

  

__\[MFS96666\]: Inclusão dos códigos RS101, \.\.\., RS156 e RS301, \.\.\., RS356 a partir de Jan\-2023:__

Essa regra considera o campo “Código do Amparo/Texto/Ocorrência” do item do Cupom Fiscal \(item 45 – COD\_AMPARO\_LEGAL da SAFX994\)\.

\(\*\*\) <a id="Regra_COD_MOTIVO_CF_2023"></a>Regra para Códigos Motivo Consumidor Final 2023

          \- Se Cod\_Amparo = \(4601 ou 4623 ou 4629 ou 4651 ou 4652 ou 4665\) então:

              Preencher com RS101 quando ressarcimento;

              Preencher com RS301 quando complemento;

          \- Se Cod\_Amparo = 4613 então: 

              Preencher com RS102 quando ressarcimento;

              Preencher com RS302 quando complemento;

          \- Se Cod\_Amparo = 4614 então: 

              Preencher com RS103 quando ressarcimento;

              Preencher com RS303 quando complemento;

          \- Se Cod\_Amparo = \(4620 ou 4624 ou 4662 ou 4681\) então: 

              Preencher com RS104 quando ressarcimento;

              Preencher com RS304 quando complemento;

          \- Se Cod\_Amparo = 4663b então: 

              Preencher com RS105 quando ressarcimento;

              Preencher com RS305 quando complemento;

          \- Se Cod\_Amparo = “4616” então:

               Preencher c/ RS151 quando ressarcimento;

               Preencher c/ RS351 quando complemento;

          \- Se Cod\_Amparo = “4617a1” então: 

              Preencher c/ RS152 quando ressarcimento;

              Preencher c/ RS352 quando complemento;

          \- Se Cod\_Amparo = \(“4617a2” ou “4617b3” ou “4656b”\)    então:

              Preencher c/ RS153 quando ressarcimento;

              Preencher c/ RS353 quando complemento;

          \- Se Cod\_Amparo = “4617b1” então: 

              Preencher c/ RS154 quando ressarcimento;

              Preencher c/ RS354 quando complemento;

          \- Se Cod\_Amparo = \(“4617b2” ou “4656a"\) então: 

              Preencher c/ RS155 quando ressarcimento;

              Preencher c/ RS355 quando complemento;

          \- Se Cod\_Amparo = “4617b4” então: 

               Preencher c/ RS156 quando ressarcimento;

               Preencher c/ RS356 quando complemento;

          \- Se Cod\_Amparo não estiver preenchido ou for diferente dos acima mencionados então: 

             Preencher com RS100 quando ressarcimento;

             Preencher com RS300 quando complemento;

          Se “__%Redução BC__” preenchido e Código Amparo não preenchido ou diferente dos acima mencionados, então: 

               Exibir a mensagem de aviso no relatório de Log:

*“Registro C480: Cupom Fiscal com base de cálculo reduzida foi gerado código de motivo RS100 ou RS300, pois faltou informação no campo Amparo/Texto/Ocorrência no item do cupom, ou este foi preenchido com um código de Amparo cujo inciso não está acobertado pela tabela 5\.7 do Sped Fiscal\. Reveja o % de Redução BC parametrizado para o Produto, acessando uma das opções disponíveis no menu Parâmetros >> Produtos \(Por Código, Por NCM ou Por CEST\) e o Amparo Legal do Item do Cupom Fiscal \(item 45 da SAFX994\)\. *

*Consulte o manual operacional do módulo para obter esclarecimentos sobre a correlação dos códigos de Amparo Legal com o % de Redução BC\.”*

O log deve demonstrar as informações necessárias para permitir a identificação do item do Cupom Fiscal \+ % Redução BC parametrizado \+ Código do Amparo do item\.

Onde:

- \([BC\-Entrada](#BC_ENTRADA_CF)\) = “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

É o valor unitário médio móvel da BC ICMS\-ST calculado para o Produto na Data de Emissão do cupom fiscal\.

- \([BC\-Saída](#BC_SAIDA_CF)\): “Valor Unitário da BC ICMS Conv \(BC\-Saída\)”
- %Redução BC e Alíquota Interna da parametrização de Produto por Código ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Emissão da Saída \(pode considerada a parametrização vigente no período informado na tela da geração\);

Ver [__*Detalhamento do Cupom Fiscal*__](#detalhamento_cupom)\.

\(\*\*\) 12/01/2021: Consulta foi realizada a nossa Área da Informação \(CAN\) que explicou que conceitualmente esse cenário não existe, por isso o fisco foi omisso e não especificou tratamento\. Como sistemicamente isso pode ocorrer, o tratamento que foi dado é emissão de mensagem no log\. Nesse caso, o cliente deve revisar sua nota\.

\[__MFS64550\]: __O fisco definiu que a nota sem ressarcimento e complemento seja apresenta\. O validador da GIA\-RS já está considerando a nota sem ressarcimento e complemento com código “__RS100__”\. 

Cod Motivo \(C480\-02\)

 

10

Quantidade Convertida

Campos da EFD correspondentes: 03 do C480\.

QTD\_CONV

Preencher com:

“Qtde Convertida Calculada para o Item do Cupom \([QTD\_CONV\_CF](#QTD_CONV_CF)\)”

Ver [__*Detalhamento do Cupom Fiscal*__](#detalhamento_cupom)\.

Qtde Conv \(C480\-03\)

 

11

Unidade de Medida

Campos da EFD correspondentes: 04 do C480\.

COD\_MEDIDA \(IDENT\_MEDIDA\)

Campo 14 – Unidade de Medida do Cadastro do Produto \(SAFX2013\), do produto pertencente ao item do cupom\. *\(ver OBS abaixo sobre os produtos associados\)*

__Sobre os produtos associados:__ Quando se tratar de uma nota fiscal de produto “associado”, a unidade de medida apresentada será a __unidade do produto principal__\.

Medida

\(C480\-04\)

12

Valor Unitário Conv\.

C480\-05

VLR\_UNIT\_CONV

Preencher com:

  VLR\_LIQ\_ITEM da SAFX994 / QTD\_CONV\_CF

Onde os valores são oriundos do item do cupom fiscal:

- VLR\_LIQ\_ITEM: é o campo 22\-Valor total líquido \(SAFX994\) do Item do cupom;
- QTD\_CONV\_CF: “Qtde Convertida Calculada para o Item do Cupom \([QTD\_CONV\_CF](#QTD_CONV_CF)\)”

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o resultado acima em 6 decimais\.

Ver [__*Detalhamento do Cupom Fiscal*__](#detalhamento_cupom)\.

Vlr Unit Conv \(C480\-05\)

13

Valor Unitário ICMS na Oper\. Conv\.

Campo da EFD correspondente: 06 do C480

Obs: mesma regra do C185 \- 10

VLR\_UNIT\_ICMS\_OPER\_CONV

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP do cupom \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

       Preencher com   BC\-Saída \* Alíquota interna / 100

__       \[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o resultado acima em 6 decimais\.

\[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:

Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no tópico [2\.3](#_2.3_–_Recuperação) for negativo, então:

    Acrescentar ao valor calculado pela regra acima, o valor a seguir:

    VLR\_UNIT\_BC\_ST\_FIM\_MP \* Alíquota Interna / 100 \(sem sinal negativo\)

__\[MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772, 773, 774 – Furto, Perda, Uso baixa c/ Ressarc:

Preencher com Zero\.

- Para Cód\. Operação = 775, 776, 777 – Furto, Perda, Uso baixa s/ Ressarc:

Preencher com Zero\.

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com Zero\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

Preencher com Zero\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com Zero\.

Onde:

- __Alíquota Interna__ da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Data de Emissão do cupom \(pode considerada a parametrização vigente no período informado na tela da geração\);
- \([__BC\-Saída__](#BC_SAIDA_CF)\): “Valor Unitário da BC ICMS Conv \(BC\-Saída\)”

Ver [__*Detalhamento do Cupom Fiscal*__](#detalhamento_cupom)\.

Vlr Unit ICMS na Operação Conv \(C480\-06\)

14

Valor Unitário ICMS Conv\.

Campos da EFD correspondes: 07 do C480

Obs: mesma regra do C185 \- 11

VLR\_UNIT\_ICMS\_CONV

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP do cupom \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

       Preencher com Zero\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772, 773, 774 – Furto, Perda, Uso baixa c/ Ressarc:

Preencher com o valor atribuído ao campo 15\- VLR\_UNIT\_ICMS\_ESTQ\_CONV\.

- Para Cód\. Operação = 775, 776, 777 – Furto, Perda, Uso baixa s/ Ressarc:

Preencher com Zero\.

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com Zero\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

Preencher com Zero\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com Zero\.

Vlr Unit ICMS Conv \(C480\-07\)

15

Valor Unitário ICMS Estoque Conv\.

Campos da EFD correspondes: 08 do C480

Obs: mesma regra do C185 \- 12

VLR\_UNIT\_ICMS\_ESTQ\_CONV

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP do cupom \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher com “Valor Médio Unitário do ICMS” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

__\[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:__

Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no tópico [2\.3](#_2.3_–_Recuperação) for negativo, então:

    Desconsiderar a regra acima e preencher este campo com ZERO\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772, 773, 774 – Furto, Perda, Uso baixa c/ Ressarc:

Preencher com “Valor Médio Unitário do ICMS” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

- Para Cód\. Operação = 775, 776, 777 – Furto, Perda, Uso baixa s/ Ressarc:

__\[MFS96666\]: RS0xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

   Preencher com “Valor Médio Unitário do ICMS” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com “Valor Médio Unitário do ICMS” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

__\[MFS96666\]: RS0xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

   Preencher com “Valor Médio Unitário do ICMS” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

__\[MFS96666\]: RS0xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

   Preencher com “Valor Médio Unitário do ICMS” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

Onde:

- O valor unitário médio móvel do ICMS é calculado para o Produto na Data de Emissão do cupom fiscal\.

__\[MFS90131\]__ arredondar para 6 casas decimais o valor médio unitário recuperado da Média Ponderada pois compõe o layout do C480\.

Vlr Unit ICMS Estoque Conv \(C480\-08\)

16

Valor Unitário ICMS\-ST Estoque Conv\.

Campos da EFD correspondes: 09 do C480

Obs: mesma regra do C185 \- 13

VLR\_UNIT\_ICMSS\_ESTQ\_CONV

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP do cupom fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher com:

__\[MFS66171\]__

\[“Valor Médio Unitário do ICMS\-ST” \+ Valor Médio Unitário do FECEP\-ST\] 

\[“Valor Médio Unitário do ICMS\-ST c/ FECEP”\] 

Tais valores são recuperados no tópico [2\.3](#_2.3_–_Recuperação)\.

__\[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:__

Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no tópico [2\.3](#_2.3_–_Recuperação) for negativo, então:

    Desconsiderar a regra acima e preencher este campo com ZERO\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772, 773, 774 – Furto, Perda, Uso baixa c/ Ressarc:

Preencher com:

__\[MFS66171\]__

\[“Valor Médio Unitário do ICMS\-ST” \+ Valor Médio Unitário do FECEP\-ST\] 

\[“Valor Médio Unitário do ICMS\-ST c/ FECEP”\] 

Tais valores são recuperados no tópico [2\.3](#_2.3_–_Recuperação)\.

- Para Cód\. Operação = 775, 776, 777 – Furto, Perda, Uso baixa s/ Ressarc:

__\[MFS96666\]: RS0xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

   Preencher com “Valor Médio Unitário do ICMS\-ST c/ FECEP” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com:

__\[MFS66171\]__

\[“Valor Médio Unitário do ICMS\-ST” \+ Valor Médio Unitário do FECEP\-ST\] 

\[“Valor Médio Unitário do ICMS\-ST c/ FECEP”\] 

Tais valores são recuperados no tópico [2\.3](#_2.3_–_Recuperação)\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

__\[MFS96666\]: RS0xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

   Preencher com “Valor Médio Unitário do ICMS\-ST c/ FECEP” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

__\[MFS96666\]: RS0xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

   Preencher com “Valor Médio Unitário do ICMS\-ST c/ FECEP” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

Onde:

- Os valores unitários médios móvel do ICMS\-ST e do FECEP\-ST são calculados para o Produto na Data de Emissão do cupom fiscal\.

__\[MFS90131\]__ arredondar para 6 casas decimais o valor médio unitário recuperado da Média Ponderada pois compõe o layout do C480\.

Vlr Unit ICMS\-ST Estoque Conv \(C480\-09\)

17

Valor Unitário FCP\-ST Estoque Conv\.

Campos da EFD correspondes: 10 do C480

Obs: mesma regra do C185 \- 14

VLR\_UNIT\_FCPS\_ESTQ\_CONV

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher com “Valor Médio Unitário do FECEP\-ST” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

__\[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:__

Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no tópico [2\.3](#_2.3_–_Recuperação) for negativo, então:

    Desconsiderar a regra acima e preencher este campo com ZERO\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772, 773, 774 – Furto, Perda, Uso baixa c/ Ressarc:

Preencher com “Valor Médio Unitário do FECEP\-ST” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

- Para Cód\. Operação = 775, 776, 777 – Furto, Perda, Uso baixa s/ Ressarc:

__\[MFS96666\]: RS0xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

   Preencher com “Valor Médio Unitário do FECEP\-ST” recuperado no tópico [2\.3](#_2.3_–_Recuperação)

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com “Valor Médio Unitário do FECEP\-ST” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

__\[MFS96666\]: RS0xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

   Preencher com “Valor Médio Unitário do FECEP\-ST” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

__\[MFS96666\]: RS0xx preenche campo a partir de Jan\-2023:__

       Para período da geração anterior a Jan\-2023, então:

          Preencher com Zero\.

       Para período da geração a partir de Jan\-2023, então:

   Preencher com “Valor Médio Unitário do FECEP\-ST” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

Onde:

- O valor unitário médio móvel do FECEP\-ST é calculado para o Produto na Data de Emissão do cupom fiscal\.

__\[MFS90131\]__ arredondar para 6 casas decimais o valor médio unitário recuperado da Média Ponderada pois compõe o layout do C480\.

Vlr Unit FCP\-ST Estoque Conv \(C480\-10\)

18

Valor Unitário ICMS\-ST Conv\. Rest\.

Campos da EFD correspondes: 11 do C480

Obs: mesma regra do C185 \- 15

VLR\_UNIT\_ICMSS\_REST\_CONV

Campo deve ser preenchido no caso da saída ser objeto de Restituição\.

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP do cupom fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher com o Valor da Restituição\.

Vide “[Regra p/ Operação de Saída Interna p/ Consumidor Final](#REST_CONS_FINAL)”\(\*\)\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772, 773, 774 – Furto, Perda, Uso baixa c/ Ressarc:

Preencher com o Valor da Restituição\.

Vide “[Regra p/ Operação de Furto, Perda, Uso baixa c/ Ressarc](#REST_FURTO)”\(\*\*\)\.

- Para Cód\. Operação = 775, 776, 777 – Furto, Perda, Uso baixa s/ Ressarc:

Preencher com Zero\.

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com o Valor da Restituição\.

Vide “[Regra p/ Operação de Outra UF, Exportação, Nova ST, Isenção](#REST_OUT_UF)”\(\*\*\*\)\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

Preencher com Zero\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com Zero\.

\(\*\) Regra p/ Operação de Saída Interna p/ Consumidor Final:

__\[MFS\-63471\]__ Não utilizar as bases \(BC\-Entrada e BC\-Saída\) na comparação para identificar se houve ressarcimento ou complemento\. Usar os próprios valores de ICMS e ICMS\-ST de Saída e Entrada\.

Se \(VLR\_UNIT\_ICMS\_ESTQ\_CONV \+ VLR\_UNIT\_ICMSS\_ESTQ\_CONV\) \- 

    VLR\_UNIT\_ICMS\_OPER\_CONV > 0 \(entrada > saída = ressarcimento\) então:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMS\_ESTQ\_CONV \+ 

    VLR\_UNIT\_ICMSS\_ESTQ\_CONV – 

    VLR\_UNIT\_ICMS\_OPER\_CONV 

    Onde:

- VLR\_UNIT\_ICMS\_OPER\_CONV: valor gravado no campo 13 \- Valor Unitário ICMS na Oper\. Conv\.;
- VLR\_UNIT\_ICMS\_ESTQ\_CONV: valor gravado no campo 15\- Valor Unitário ICMS Estoque Conv\.;
- VLR\_UNIT\_ICMSS\_ESTQ\_CONV: valor gravado no campo 16\- Valor Unitário ICMS\-ST Estoque Conv\.;

Senão

    Não preencher;

- \([BC\-Entrada](#BC_ENTRADA)\) = “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

É o valor unitário médio móvel da BC ICMS\-ST calculado para o Produto na Data de Emissão do cupom fiscal\.

- \([BC\-Saída](#BC_SAIDA_CF)\): “Valor Unitário da BC ICMS Conv \(BC\-Saída\)”

Ver [__*Detalhamento do Cupom Fiscal*__](#detalhamento_cupom)\.

\(\*\*\) Regra p/ Operação de Furto, Perda, Uso baixa c/ Ressarc:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMS\_ESTQ\_CONV \+ 

    VLR\_UNIT\_ICMSS\_ESTQ\_CONV – 

    VLR\_UNIT\_ICMS\_CONV

    Onde:

- VLR\_UNIT\_ICMS\_CONV: valor gravado no campo 14\- Valor Unitário ICMS Conv\.;
- VLR\_UNIT\_ICMS\_ESTQ\_CONV: valor gravado no campo 15\-Valor Unitário ICMS Estoque Conv\.;
- VLR\_UNIT\_ICMSS\_ESTQ\_CONV: valor gravado no campo 16\- Valor Unitário ICMS\-ST Estoque Conv\.;

\(\*\*\*\) Regra p/ Operação de Outra UF, Exportação, Nova ST, Isenção:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMS\_ESTQ\_CONV \+ 

    VLR\_UNIT\_ICMSS\_ESTQ\_CONV 

    Onde:

- VLR\_UNIT\_ICMS\_ESTQ\_CONV: valor gravado no campo 15\- Valor Unitário ICMS Estoque Conv\.;
- VLR\_UNIT\_ICMSS\_ESTQ\_CONV: valor gravado no campo 16\- Valor Unitário ICMS\-ST Estoque Conv\.;

Validação:

Caso o valor gravado no campo seja negativo, exibir mensagem de aviso no log:

*“Registro C480: Cupom Fiscal gerado com valor unitário do ressarcimento negativo\.”*

O log deve demonstrar as informações necessárias para permitir a identificação do Cupom Fiscal exibindo o Estabelecimento, Número do Caixa, Modelo, Número COO, Data Emissão, Produto\. 

Vlr Unit ICMS\-ST Conv Rest \(C480\-11\)

19

Valor Unitário FCP\-ST Conv\. Rest\.

Campos da EFD correspondes: 12 do C480

Obs: mesma regra do C185 \- 16

VLR\_UNIT\_FCPS\_REST\_CONV

Campo deve ser preenchido no caso da saída ser objeto de Restituição\.

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP do cupom fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher com o Valor do FECEP p/ Restituição\.

Vide “[Regra p/ Operação de Saída Interna p/ Consumidor Final](#FECEP_CONS_FINAL)”\(\*\)\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772, 773, 774 – Furto, Perda, Uso baixa c/ Ressarc:

Preencher com o Valor do FECEP p/ Restituição\.

Vide “[Regra p/ Operação de Furto, Perda, Uso baixa c/ Ressarc](#FECEP_FURTO)”\(\*\*\)\.

- Para Cód\. Operação = 775, 776, 777 – Furto, Perda, Uso baixa s/ Ressarc:

Preencher com Zero\.

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com o Valor do FECEP p/ Restituição\.

Vide “[Regra p/ Operação de Outra UF, Exportação, Nova ST, Isenção](#FECEP_OUT_UF)”\(\*\*\*\)\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

Preencher com Zero\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com Zero\.

\(\*\) Regra p/ Operação de Saída Interna p/ Consumidor Final:

__\[MFS\-63471\]__ Não utilizar as bases \(BC Entrada e BC Saída\) na comparação para identificar se houve ressarcimento ou complemento\. Usar os próprios valores de ICMS e ICMS\-ST de Saída e Entrada\.

Se \(VLR\_UNIT\_ICMS\_ESTQ\_CONV \+ VLR\_UNIT\_ICMSS\_ESTQ\_CONV\) \- 

    VLR\_UNIT\_ICMS\_OPER\_CONV > 0 \(entrada > saída = ressarcimento\) então:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMSS\_REST\_CONV \* Alíquota FCP / 100

    Onde: 

- VLR\_UNIT\_ICMSS\_REST\_CONV: valor gravado no campo 18\- Valor Unitário ICMS\-ST Conv\. Rest\.;
- Alíquota FCP da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Data de Emissão do Cupom \(pode considerada a parametrização vigente no período informado na tela da geração\);

Senão:

    Não preencher;

\(\*\*\) Regra p/ Operação de Furto, Perda, Uso baixa c/ Ressarc:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMSS\_REST\_CONV \* Alíquota FCP / 100

   Onde:

- VLR\_UNIT\_ICMSS\_REST\_CONV: valor gravado no campo 18\- Valor Unitário ICMS\-ST Conv\. Rest\.;
- Alíquota FCP da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Data de Emissão do Cupom \(pode considerada a parametrização vigente no período informado na tela da geração\);

\(\*\*\*\) Regra p/ Operação de Outra UF, Exportação, Nova ST, Isenção:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMSS\_REST\_CONV \* Alíquota FCP / 100

    Onde:

- VLR\_UNIT\_ICMSS\_REST\_CONV: valor gravado no campo 18\- Valor Unitário ICMS\-ST Conv\. Rest\.;
- Alíquota FCP da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Data de Emissão do Cupom \(pode considerada a parametrização vigente no período informado na tela da geração\);

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o resultado acima em 6 decimais\.

Vlr Unit FCP\-ST Conv Rest \(C480\-12\)

20

Valor Unitário ICMS\-ST Conv\. Compl\.

Campos da EFD correspondes: 13 do C480

Obs: mesma regra do C185 \- 17

VLR\_UNIT\_ICMSS\_COMPL\_CONV

Campo deve ser preenchido no caso da saída ser objeto de Complementação\.

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP do cupom fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher com o Valor da Complementação\.

Vide “[Regra p/ Operação de Saída Interna p/ Consumidor Final](#COMPL_CONS_FINAL)”\(\*\)\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772, 773, 774 – Furto, Perda, Uso baixa c/ Ressarc:

Preencher com Zero\.

- Para Cód\. Operação = 775, 776, 777 – Furto, Perda, Uso baixa s/ Ressarc:

Preencher com Zero\.

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com Zero\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

Preencher com Zero\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com Zero\.

\(\*\) Regra p/ Operação de Saída Interna p/ Consumidor Final:

__\[MFS\-63471\]__ Não utilizar as bases \(BC Entrada e BC Saída\) na comparação para identificar se houve ressarcimento ou complemento\. Usar os próprios valores de ICMS e ICMS\-ST de Saída e Entrada\.

Se \(VLR\_UNIT\_ICMS\_ESTQ\_CONV \+ VLR\_UNIT\_ICMSS\_ESTQ\_CONV\) \- 

    VLR\_UNIT\_ICMS\_OPER\_CONV < 0 \(entrada < saída = complemento\) então:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMS\_OPER\_CONV \-

    VLR\_UNIT\_ICMS\_ESTQ\_CONV \- 

    VLR\_UNIT\_ICMSS\_ESTQ\_CONV 

    

    Onde:

- VLR\_UNIT\_ICMS\_OPER\_CONV: valor gravado no campo 13 \- Valor Unitário ICMS na Oper\. Conv\.;
- VLR\_UNIT\_ICMS\_ESTQ\_CONV: valor gravado no campo 15\- Valor Unitário ICMS Estoque Conv\.;
- VLR\_UNIT\_ICMSS\_ESTQ\_CONV: valor gravado no campo 16\- Valor Unitário ICMS\-ST Estoque Conv\.;

Senão:

    Não preencher;

Onde:

- \([BC\-Entrada](#BC_ENTRADA)\) = “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” recuperado no tópico [2\.3](#_2.3_–_Recuperação)\.

É o valor unitário médio móvel da BC ICMS\-ST calculado para o Produto na Data de Emissão da nota de saída\.

- \(BC\-Saída\): “Valor Unitário da BC ICMS Conv \([BC\-Saída](#BC_SAIDA)\)”

Ver [__*Detalhamento do Cupom Fiscal*__](#detalhamento_cupom)\.

Validação:

Caso o valor gravado no campo seja negativo, exibir mensagem de aviso no log:

*“Registro C480: Cupom Fiscal gerado com valor unitário do complemento negativo\.”*

O log deve demonstrar as informações necessárias para permitir a identificação do Cupom Fiscal exibindo o Estabelecimento, Número do Caixa, Modelo, Número COO, Data Emissão, Produto\.

Vlr Unit ICMS\-ST Conv Compl \(C480\-13\)

21

Valor Unitário FCP\-ST Conv\. Compl\.

Campos da EFD correspondes: 14 do C480

Obs: mesma regra do C185 \- 18

VLR\_UNIT\_FCPS\_COMPL\_CONV

Campo deve ser preenchido no caso da saída seja objeto de Complementação\.

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP do cupom fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Preencher com o Valor da Complementação FECEP\.

Vide “[Regra p/ Operação de Saída Interna p/ Consumidor Final](#COMPL_FECEP_CONS_FINAL)”\(\*\)\.

\[__MFS58042/ MFS59698\]__

- Para Cód\. Operação = 772, 773, 774 – Furto, Perda, Uso baixa c/ Ressarc:

Preencher com Zero\.

- Para Cód\. Operação = 775, 776, 777 – Furto, Perda, Uso baixa s/ Ressarc:

Preencher com Zero\.

__MFS64191__

- Para Cód\. Operação = 778, 781, 782, 783 – Outra UF, Exportação, Nova ST, Isenção:

Preencher com Zero\.

- Para Cód\. Operação = 779, 784 – Outra UF Art 24, Isenção Art 24\-A:

Preencher com Zero\.

- Para Cód\. Operação = 785 – Saída ao abrigo da Exclusão:

Preencher com Zero\.

\(\*\) Regra p/ Operação de Saída Interna p/ Consumidor Final:

__\[MFS\-63471\]__ Não utilizar as bases \(BC Entrada e BC Saída\) na comparação para identificar se houve ressarcimento ou complemento\. Usar os próprios valores de ICMS e ICMS\-ST de Saída e Entrada\.

Se \(VLR\_UNIT\_ICMS\_ESTQ\_CONV \+ VLR\_UNIT\_ICMSS\_ESTQ\_CONV\) \- 

    VLR\_UNIT\_ICMS\_OPER\_CONV < 0 \(entrada < saída = complemento\) então:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMSS\_COMPL\_CONV \* Alíquota FCP / 100

    Onde:

- VLR\_UNIT\_ICMSS\_COMPL\_CONV: valor gravado no campo 20\- Valor Unitário ICMS\-ST Conv\. Compl\.;
- Alíquota FCP da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Data de Emissão do Cupom \(pode considerada a parametrização vigente no período informado na tela da geração\);

Senão:

    Não preencher;

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o resultado acima em 6 decimais\.

Vlr Unit FCP\-ST Conv Compl \(C480\-14\)

__*Parametrização do Produto \(por Código, NCM ou CEST\)*__

Produto da NF 

GRUPO\_PROD\_CF

IND\_PROD\_CF

COD\_PROD\_CF

Produto do item do cupom fiscal\.

Ind Produto

\(SAFX2013\-01\)

Cod Produto \(SAFX2013\-02\)

Unidade de Medida do Produto NF

COD\_MEDIDA\_PROD\_CF

Unidade de Medida do Produto do cupom fiscal \(SAFX2013 – campo 14 – COD\_MEDIDA\)

Medida Produto \(SAFX2013\-14\)

NCM do Produto NF

COD\_NBM\_PROD\_CF

Código NBM do Produto do cupom fiscal \(SAFX2013 – campo 05 – Código NBM\)

NCM Produto \(SAFX2013\-05\)

CEST do Produto NF

COD\_CEST\_PROD\_CF

Código CEST do Produto do cupom fiscal \(SAFX2013 – campo 54 – Código Especificador da Substituição Tributária\)

CEST Produto \(SAFX2013\-54\)

Produto Principal

GRUPO\_PROD\_PRINC

IND\_PROD\_PRINC

COD\_PROD\_PRINC

Caso o produto do item do cupom fiscal tenha sido parametrizado por Código \(menu “Parâmetros à Produtos à Por Código”\) apresentar o Produto Principal \(grupo, indicador e código\)\.

Não Apresentar

Unidade de Medida do Produto Principal

COD\_MEDIDA\_PROD\_PRINC

Caso o produto do item do cupom fiscal tenha sido parametrizado por Código \(menu “Parâmetros à Produtos à Por Código”\) apresentar a Unidade de Medida do Produto Principal \(SAFX2013 – campo 14 – COD\_MEDIDA\)\.

Não Apresentar

%Redução BC

PRC\_REDUCAO\_BC

%Redução BC da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Emissão do Cupom Fiscal \(pode considerada a parametrização vigente no período informado na tela da geração\);

%Redução BC \(Parametrização Produto\)

Alíquota Interna

ALIQ\_INTERNA

Alíquota Interna da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Emissão do Cupom Fiscal \(pode considerada a parametrização vigente no período informado na tela da geração\);

Alíq\. Interna \(Parametrização Produto\)

Alíquota FCP

ALIQ\_FCP

Alíquota FCP da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Emissão do Cupom Fiscal \(pode considerada a parametrização vigente no período informado na tela da geração\);

Alíq\. FCP \(Parametrização Produto\)

<a id="detalhamento_cupom"></a>__*Detalhamento do Cupom Fiscal*__

Quantidade do Item do Cupom \(safx994 – item 16\)

QTD\_CF

Campo 16\-Quantidade \(SAFX994\) do item do cupom fiscal

Qtde Item \(SAFX994\-16\)

Unidade de Medida do Item do Cupom \(safx994 – item 17\)

COD\_MEDIDA\_CF

Campo 17 – Unidade de Medida \(SAFX994\) do item do cupom fiscal\.

Medida Item \(SAFX994\-17\)

Fator Conversão

FAT\_CONV\_CF

Preencher com o Fator de Conversão utilizado na regra do campo “Qtde Convertida Calculada para o Item do cupom fiscal \(QTD\_CONV\_CF\)” a seguir\.

__Se__ unidade do cupom = unidade do cadastro do produto, então:__  __

__    __Campo será preenchido com 1;

__Senão __

    Se não encontrado Fator de Conversão nos Cadastros de Conversão de Unidades

    de Medidas, então:

          Campo será preenchido com \-1;

    Senão

           Campo será preenchido com o Fator de Conversão encontrado\.

Fator Conv \(Cadastro Conversão Medida\)

Qtde Convertida Calculada para o Item do Cupom

\(<a id="QTD_CONV_CF"></a>QTD\_CONV\_CF\)

QTD\_CONV\_CF

Campo 16\-Quantidade \(SAFX994\) do Item do cupom fiscal, aplicando a conversão, quando necessário\. Veja:

__Se__ unidade do cupom __\(\*\)__ = unidade do cadastro do produto __\(\*\*\)  __*\(ver OBS abaixo sobre os produtos associados\)*

      __\(\*\)__ unidade do cupom = campo “17\-Unidade de Medida” da SAFX994

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria quantidade do item do cupom;

__Senão __

         Nesse caso a quantidade do item do cupom \(SAFX994\) será convertida para a 

         unidade de medida do cadastro do produto;

         \[Quantidade do item do cupom \(SAFX994\) \* Fator de Conversão\]

__Sobre os produtos associados:__ Quando se tratar de um cupom fiscal de produto “associado”, a comparação será feita da unidade de medida do cupom, com a __unidade do produto principal__\.

Exemplo:

__Produto principal__: COCA\-COLA PET                 \(unidade de medida do estoque – SAFX2013 = UN\) 

__Produtos associados__: COCA\-COLA PET–1      \(unidade de medida do estoque – SAFX2013 = PAC \(6 unidades\)\)

Cupom de venda do produto associado: __COCA\-COLA PET\-1__, unidade do cupom= PAC, Quantidade = __5__

Compara a unidade de medida do cupom do produto associado com a unidade de estoque do produto principal: PAC x UN

Como é diferente, deve\-se converter a quantidade do cupom de PAC para UN\. 

Para acessar a tabela de conversão por produto, será utilizado o código do produto principal:

__DWT\_CONV\_MEDIDA\-2: __Produto = __COCA\-COLA PET__

                                          Unidade Origem = PAC

                                          Unidade Destino = UN

                                          Fator de conversão = 6,0000

Conversão da quantidade do cupom do associado:  QTD da cupom x Fator de Conversão   =  5 x 6,0000 = 30,0000 

Lembrando que, quando não existe fator na tabela de conversão por produto \(DWT\_CONV\_MEDIDA\_2\), será utilizada a tabela padrão \(DWT\_CONV\_MEDIDA\)\.  

__= = = = =__

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas será gravada a seguinte mensagem de erro no log:

“*Registro C480: Fator de conversão de medida de XXX para XXX não encontrado\. Cupom Fiscal será gerada no C480 sem Quantidade Convertida e valores unitários da Mercadoria e ICMS \(campos 3, 5 e 6\)”\.*

\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do Cupom Fiscal exibindo o Estabelecimento, Número do Caixa, Modelo, Número COO, Data Emissão, Produto\.

Não Apresentar pois já é o campo Qtde Conv \(C480\-03\)

Valor total líquido do Item do Cupom \(safx994 – item 22\)

VLR\_LIQ\_ITEM

Campo 22 \- “Valor total líquido” \(SAFX994\) do item do cupom fiscal\.

Vlr Líquido Item \(SAFX994\-22\)

Amparo Legal \(safx994\- item 45\)

COD\_AMPARO\_LEGAL

__\[MFS96666\]: Inclusão dos códigos RS101, \.\.\., RS156 e RS301, \.\.\., RS356 a partir de Jan\-2023:__

“Código do Amparo/Texto/Ocorrência” do item do Cupom Fiscal \(item 45 – COD\_AMPARO\_LEGAL da SAFX994\)\.

Amparo Legal \(safx994\- item 45\)

Valor Unitário da BC ICMS Conv \(<a id="BC_SAIDA_CF"></a>BC\-Saída\)

VLR\_BC\_ICMS\_CF

Valor Unitário da BC do ICMS na Operação Conv, calculado conforme regra:

Se o campo “__%Redução BC__” da parametrização de Produto ou NCM ou CEST está preenchido com valor > 0, então:

     Este campo será gerado da seguinte forma:

     \[\(Vlr Liq Item – \(Vlr Liq Item \* “%Redução BC” / 100\)\)\]/ QTD\_CONV\_CF

Senão:

      Este campo será gerado da seguinte forma:

      \[\(Vlr Liq Item\)\] / QTD\_CONV\_CF

Onde:

- %Redução BC da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na Emissão do cupom \(pode considerada a parametrização vigente no período informado na tela da geração\);
- Vlr Liq Item = 22 \- Vlr Total Líquido do Item do cupom\.
- QTD\_CONV\_CF: Qtde Convertida Calculada para o Item do Cupom \([QTD\_CONV\_CF](#QTD_CONV_CF)\)\.

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

Arredondar o resultado acima em 6 decimais\.

Vlr Unit BC ICMS Operação Conv \(Vlr Liquido Item c/ %Redução BC\)

__*Valores Unitários da Média Pondera Móvel do dia da operação de saída \(recuperada no tópico *__[__*2\.3*__](#_2.3_–_Recuperação)__*\.\)*__

Valor Médio Unitário do ICMS no dia Saída \(Tabela de Média Diária\)

VLR\_UNIT\_ICMS\_SAI

“Valor Médio Unitário do ICMS” recuperado no passo 1 do tópico [2\.3](#_2.3_–_Recuperação)\.  

__\[MFS90131\]__ mantém com 8 casas decimais o valor médio unitário recuperado da Média Ponderada\. Campo utilizado apenas para o relatório de conferência\.

Vlr Unit ICMS \(Recuperado da Média Ponderada\)

Valor Médio Unitário do ICMS\-ST s/ FECEP no dia Saída \(Tabela de Média Diária\)

VLR\_UNIT\_ICMS\_ST\_SAI

__\[MFS66171\]__

“Valor Médio Unitário do ICMS\-ST s/ FECEP” recuperado no passo 1 do tópico [2\.3](#_2.3_–_Recuperação)\.

Campo VLR\_UNIT\_ICMS\_ST\_FIM\_MP da EST\_ST\_RS\_MEDIA\_POND\.

__\[MFS90131\]__ mantém com 8 casas decimais o valor médio unitário recuperado da Média Ponderada\. Campo utilizado apenas para o relatório de conferência\.

Vlr Unit ICMS\-ST\(s/ FECEP\-ST\) \(Recuperado da Média Ponderada\)

Valor Médio Unitário do ICMS\-ST c/ FECEP no dia Saída \(Tabela de Média Diária\)

VLR\_UNIT\_ICMS\_ST\_FECEP\_SAI

__\[MFS66171__\]

“Valor Médio Unitário do ICMS\-ST c/ FECEP” recuperado no passo 1 do tópico [2\.3](#_2.3_–_Recuperação)\.

Campo VLR\_UNIT\_ICMS\_ST\_FECEP\_FIM\_MP da EST\_ST\_RS\_MEDIA\_POND\.

__\[MFS90131\]__ mantém com 8 casas decimais o valor médio unitário recuperado da Média Ponderada\. Campo utilizado apenas para o relatório de conferência\.

Vlr Unit ICMS\-ST\(c/ FECEP\-ST\) \(Recuperado da Média Ponderada\)

Valor Médio Unitário da Base de Cálculo do ICMS\-ST no dia Saída \(Tabela de Média Diária\)

\(<a id="BC_ENTRADA_CF"></a>BC\-Entrada\)

VLR\_UNIT\_BC\_ST\_SAI

“Valor Médio Unitário da Base de Cálculo do ICMS\-ST” recuperado no passo 1 do tópico [2\.3](#_2.3_–_Recuperação)\.

__\[MFS90131\]__ mantém com 8 casas decimais o valor médio unitário recuperado da Média Ponderada\. Campo utilizado apenas para o relatório de conferência\.

Vlr Unit BC ICMS\-ST \(Recuperado da Média Ponderada\)

Valor Médio Unitário do FECEP\-ST no dia Saída \(Tabela de Média Diária\)

VLR\_UNIT\_FECEP\_ST\_SAI

“Valor Médio Unitário do FECEP\-ST” recuperado no passo 1 do tópico [2\.3](#_2.3_–_Recuperação)\.

__\[MFS90131\]__ Mantém com 8 casas decimais o valor médio unitário recuperado da Média Ponderada\. Campo utilizado apenas para o relatório de conferência\.

Vlr Unit FECEP\-ST \(Recuperado da Média Ponderada\)

OBSERVAÇÃO

DSC\_OBS

\[MFS89648\]: Tratamento para Valor Médio Ponderado negativo:

A regra de preenchimento desse campo depende da Operação parametrizada para o CFOP ou Natureza de Operação da nota fiscal \(vide tópico [1\.1](#COD_OP_SAIDA)\):

- Para Cód\. Operação = 770 – Saída Interna p/ Consumidor Final: 

Caso o “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” \(VLR\_UNIT\_BC\_ST\_FIM\_MP\), recuperado no tópico [2\.3](#_2.3_–_Recuperação) for negativo, então:

Preencher este campo com a observação:

“Valor médio ponderado móvel do dia negativo\. Campo Vlr Unit ICMS Operação Conv foi acrescido de 9999,99 e os campos Vlr Unit ICMS Estoque Conv, Vlr Unit ICMS\-ST Estoque Conv e Vlr Unit FCP\-ST Estoque Conv foram zerados\. Tratamento baseado no tópico 19\.3\-A\.2\.2\.2 da IN45/98\.”

Onde:

9999,99:

 VLR\_UNIT\_BC\_ST\_FIM\_MP \* Alíquota Interna / 100 \(sem sinal negativo\)

- Para os demais Cód\. Operação:

Não preencher\.

Observação

# <a id="_Toc71832847"></a>RELATORIO DE CONFERÊNCIA

Gerar arquivos excel a partir da leitura das tabelas __EST\_ST\_RS\_NF\_SAI__ e __EST\_ST\_RS\_ECF__\.

Nome dos arquivos: Relatório\_Conferencia\_C185\_mm\_aaaa\_cod\_estab\.xlsx

                                 Relatório\_Conferencia\_C380\_mm\_aaaa\_cod\_estab\.xlsx

                                 Relatório\_Conferencia\_C480\_mm\_aaaa\_cod\_estab\.xlsx

Relatório de Conferência

Tabelas Específicas da Geração do Movimento

Movimento de Saídas \(C185\)

EST\_ST\_RS\_NF\_SAI, filtrar as notas de Modelo = 01, 1B, 04, 55, 65

Movimento de Saídas \(C380\)

EST\_ST\_RS\_NF\_SAI, filtrar as notas de Modelo = 02

Movimento de Cupons Fiscais \(C480\)

EST\_ST\_RS\_ECF __\[MFS\-65137\]__ 

= = = = = =

 


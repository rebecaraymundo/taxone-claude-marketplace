# MTZ-ICMS-Listagem-Apuracao-ICMS-ST

- **Fonte:** MTZ-ICMS-Listagem-Apuracao-ICMS-ST.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 71 KB

---

THOMSON REUTERS

                                                                                       __Módulo ICMS__

__  __

__                                      Listagem de Conferência da Apuração do ICMS\-ST__

__Localização__: Menu Estadual, Módulo ICMS, item Operacional 🡪 Listagens da Apuração 🡪 Listagem de Substituição Tributária

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4352

Alterações na listagem de conferência da Apuração do ST 

Correções e melhorias na listagem de conferência da apuração do ICMS\-ST \(vide __RN03__ e __RN04__\)\.

30/01/2014

\(criação do docto\)

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

O objetivo deste relatório é conferir os dados do ICMS\-ST gerados no Livro de Apuração \(P9\)\.

O relatório é gerado a partir das tabelas que armazenam os dados resultantes da apuração do ICMS\-ST __\(\*\*\*\)__\. Assim, é pré\-requisito executar a apuração do ICMS para a sua emissão\.

__\(\*\*\*\)__ RESUMO\_APUR\_ST e ITEM\_APURAC\_SUBST

__RN01__

__                                                        Parâmetros de Tela__

Campo “__Estabelecimento__”:

- lista com a relação de todos os Estabelecimentos da Empresa do login \+ opção “Todos”;

Campo  “__Tipo Livro__”:

- este campo trabalha com janela de pesquisa da tabela das obrigações fiscais, mas considerando apenas as obrigações referentes a Apuração do ICMS: 108, 142, 143 e 165;

*Obs: os livros 142 e 143 \(livros incentivados e não incentivados do módulo Prodede\) não são mais utilizados no Módulo ICMS\. Provavelmente, estes códigos aparecem na lista porque este relatório é muito antigo, e na época da sua criação estes livros ainda eram tratados no módulo ICMS\.*

Campos “__Data Apuração__”:

- neste campo o usuário informará a data da apuração para a recuperação dos dados;

__RN02__

__                                     Recuperação e Processamento dos Dados__

__Origem dos dados: __ Tabelas que armazenam os dados resultantes da apuração do ICMS\-ST 

                                   \(RESUMO\_APUR\_ST e  ITEM\_APURAC\_SUBST\)

O relatório é gerado por Estabelecimento e UF\.

Para cada estabelecimento selecionado em tela, será gerado o relatório demonstrando os valores da apuração de cada UF, conforme consta no layout \(vide __RN03__\)\.

Recuperação dos dados nas tabelas da apuração do ICMS\-ST:

     \- Empresa             – empresa do login

     \- Estabelecimento – estabelecimento em questão

     \- Tipo do Livro       – código do livro informado na tela da geração

     \- Data Apuração    – data informada na tela da geração

Nas duas tabelas, a UF é identificada através do IDENT\_UF \(indicador referente à tabela ESTADO\)\.  

Cada uma das tabelas utilizadas no relatório contém os valores referentes aos seguintes itens da apuração do ST de cada UF:

RESUMO\_APUR\_ST:

001\-Saídas com Débito

004\-Subtotal

005\-Entradas com Crédito

008\-Subtotal

009\-Saldo Credor Anterior

010\-Subtotal

011\-Saldo Devedor

013\-Imposto a Recolher

014\-Saldo Credor a Transportar

ITEM\_APURAC\_SUBST:

002\-Outros Débitos

003\-Estorno de Créditos

006\-Outros Créditos

007\-Estorno de Débitos

012\-Deduções

__RN03__

__                                                      Layout do Relatório__

__Alterações da OS4352 \(Fev/2014\):__

\- O título “Entradas” foi substituído por “Créditos”

\- O título “Saídas” foi substituído por “Débitos”

\- Inclusão da coluna “Lançamentos/Saldo Anterior” \(sob o título “Créditos”\)

\- Inclusão da coluna “Lançamentos”  \(sob o título “Débitos”\)

__UF__

__Créditos__

__Débitos__

__Valor Saldo__

__D/C__

__Valor Base Crédito __

__Imposto Creditado__

__Lançamentos/__

__Saldo Anterior__

__Valor Base Débito __

__Imposto Debitado__

__Lançamentos__

XX

 99\.999\.999\.999,99

99\.999\.999\.999,99

999\.999\.999,99

99\.999\.999\.999,99

99\.999\.999\.999,99

99\.999\.999,99

9\.999\.999,99

  X

XX

99\.999\.999\.999,99

99\.999\.999\.999,99

999\.999\.999,99

99\.999\.999\.999,99

99\.999\.999\.999,99

99\.999\.999,99

9\.999\.999,99

  X

XX

99\.999\.999\.999,99

99\.999\.999\.999,99

999\.999\.999,99

99\.999\.999\.999,99

99\.999\.999\.999,99

99\.999\.999,99

9\.999\.999,99

  X

XX

99\.999\.999\.999,99

99\.999\.999\.999,99

999\.999\.999,99

99\.999\.999\.999,99

99\.999\.999\.999,99

99\.999\.999,99

9\.999\.999,99

  X

XX

99\.999\.999\.999,99

999\.999\.999,99

99\.999\.999\.999,99

99\.999\.999\.999,99

99\.999\.999,99

9\.999\.999,99

  X

Total por Estabelecimento:

99\.999\.999\.999,99

999\.999\.999,99

99\.999\.999\.999,99

99\.999\.999,99

9\.999\.999,99

  X

Total:

99\.999\.999\.999,99

999\.999\.999,99

99\.999\.999\.999,99

99\.999\.999,99

9\.999\.999,99

  X

__RN04__

__                                                   Preenchimento dos Dados no Relatório__

__Ordenação dos Dados__ 🡪 Estabelecimento / UF Favorecida

__Alterações da OS4352 \(Fev/2014\)__:

\- Com a inclusão das colunas “Lançamentos/Saldo Anterior” e “Lançamentos”, as colunas “Impostos Creditado” e “Imposto Debitado”

  passaram a exibir apenas o valor de ST oriundos das notas fiscais;

\- Os valores de ST referentes aos lançamentos complementares passaram a ser demonstrados separadamente nas colunas

  “Lançamentos/Saldo Anterior” e “Lançamentos”;

\- O relatório passou a tratar também os valores de ST do saldo anterior das UF’s, que é exibido, quando existir, na coluna

   “Lançamentos/Saldo Anterior”, junto com os lançamentos à crédito;

__Coluna __

__Conteúdo __

UF

Sigla da UF favorecida 

\(obtida na tabela ESTADO a partir do identificador da UF das tabelas da apuração\)

Valor Base Crédito

Valor da base de cálculo do ICMS\-ST das notas fiscais de entrada:

Origem da informação:

Tabela RESUMO\_APUR\_ST, linha de COD\_OPER\_APUR = “__005__” \(Entradas c/Crédito\)

Coluna VLR\_BASE 

Imposto Creditado

Valor do ICMS\-ST das notas fiscais de entrada:

Origem da informação:

Tabela RESUMO\_APUR\_ST, linha de COD\_OPER\_APUR = “__005__” \(Entradas c/Crédito\)

Coluna VLR\_ICMS

Lançamentos/Saldo Anterior

Valor total dos lançamentos a crédito \+ valor do saldo anterior 

Origem da informação:

ITEM\_APURAC\_SUBST, linha de COD\_OPER\_APUR = “__006__” \(Outros Créditos\), coluna VAL\_ITEM\_DISCRIM

\+

ITEM\_APURAC\_SUBST, linha de COD\_OPER\_APUR = “__007__” \(Estorno de Débitos\), coluna VAL\_ITEM\_DISCRIM

\+ 

ITEM\_APURAC\_SUBST, linha de COD\_OPER\_APUR = “__012__” \(Deduções\), coluna VAL\_ITEM\_DISCRIM

\+

RESUMO\_APUR\_ST, linha de COD\_OPER\_APUR = “__009__” \(Saldo Anterior\), coluna VLR\_ICMS

Valor Base Débito

Valor da base de cálculo do ICMS\-ST das notas fiscais de saída:

Origem da informação:

Tabela RESUMO\_APUR\_ST, linha de COD\_OPER\_APUR = “__001__” \(Saídas c/Débito\)

Coluna VLR\_BASE 

Imposto Debitado

Valor do ICMS\-ST das notas fiscais de saída:

Origem da informação:

Tabela RESUMO\_APUR\_ST, linha de COD\_OPER\_APUR = “__001__” \(Saídas c/Débito\)

Coluna VLR\_ICMS

Lançamentos

Valor total dos lançamentos a débito

Origem da informação:

ITEM\_APURAC\_SUBST, linha de COD\_OPER\_APUR = “__002__” \(Outros Débitos\), coluna VAL\_ITEM\_DISCRIM

\+

ITEM\_APURAC\_SUBST, linha de COD\_OPER\_APUR = “__003__” \(Estorno de Créditos\), coluna VAL\_ITEM\_DISCRIM

Valor Saldo

Saldo resultante da UF\. Este valor será obtido a partir do resultado das colunas anteriores, da seguinte forma:

  \(“Imposto Debitado” \+ “Lançamentos”\) \- \(“Imposto Creditado” \+ “Lançamentos/Saldo Anterior”\)

D/C

O preenchimento desta coluna depende do conteúdo apurado na coluna “Valor Saldo”, da seguinte forma:

Se Valor Saldo positivo 🡪 a coluna “D/C” será preenchida com “D”

Se Valor Saldo negativo 🡪 a coluna “D/C” será preenchida com “C”

Se Valor Saldo = 0 🡪 a coluna “D/C” será preenchida com brancos 

Linha “Total por Estabelecimento”

Esta linha mostra a totalização de todas as UF’s de um Estabelecimento\.

Serão totalizadas as seguintes colunas do relatório:

\-Imposto Creditado

\-Lançamentos/Saldo Anterior

\-Imposto Debitado

\-Lançamentos

\-Valor Saldo 🡪 o valor do saldo final do Estabelecimento será apurado a partir do resultado

                         totalizado para as demais colunas desta linha, da mesma forma descrita para

                         o preenchimento desta coluna;

Linha “Total”

Esta linha mostra a totalização do resultado de todos os estabelecimentos, seguindo a mesma lógica descrita para a linha “Total por Estabelecimento”\.

        = = = = =


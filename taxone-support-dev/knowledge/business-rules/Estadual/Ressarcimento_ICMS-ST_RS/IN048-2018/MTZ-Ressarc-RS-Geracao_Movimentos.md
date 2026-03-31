# MTZ-Ressarc-RS-Geracao_Movimentos

- **Fonte:** MTZ-Ressarc-RS-Geracao_Movimentos.docx
- **Modificado:** 2024-01-22
- **Tamanho:** 112 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 048/2018\) 

Geração dos Movimentos 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\), itens:

Geração 🡪 IN\-RE 048/2018 🡪 Geração dos Movimentos

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS28006__

Liliane Videira Assaf

Geração dos movimentos de saída para Consumidor Final

\.\.\.\.\.

04/07/2019 

__MFS29437__

Liliane Videira Assaf

Geração dos movimentos das entradas para Não Varejistas\.

20/07/2019

__MFS28004__

Liliane Videira Assaf

Geração dos movimentos das entradas para Varejistas\. Ver marcações em verde\.

01/08/2019

__MFS28011__

Liliane Videira Assaf

Gerar saídas para Outras UF's, Isentas ou Não Tributadas \(Varejista\)

21/08/2019

__MFS28013__

Liliane Videira Assaf

Limpeza dos lançamentos de transferência

25/08/2019

__MFS29925__

Liliane Videira Assaf

Tratamento do Controle Subapuração entre módulos Ressarcimento ST e ICMS:

Se o número da Subapuração parametrizada nos Dados Iniciais, já estiver sendo utilizado em subapurações, oriundas do módulo Estadual >> ICMS, exibir mensagem de erro\.

19/09/2019

__MFS47349__

Liliane Videira Assaf

Tratamento de Produtos Associados na geração dos movimentos

30/03/2021

__MFS81764__

Liliane Videira Assaf

Criação da Geração da Parcela do Crédito das Mercadorias em Estoque

03/03/2022

__MFS81804__

Liliane Assaf

Tratamento das Devoluções de Saídas de Mercadorias destinadas a Consumidor Final

07/03/2022

__MFS591083__

Liliane Assaf

Criação do parâmetro “Considerar as notas fiscais da empresa incorporada”\.

22/01/2024

Sumário

[1\.	Visão Geral da Solução	1](#_Toc68093853)

[2\.	Introdução	1](#_Toc68093854)

[3\.	Parâmetros da Tela	1](#_Toc68093855)

[4\.	Críticas	1](#_Toc68093856)

[5\.	Processamento	1](#_Toc68093857)

[5\.1 – Limpeza do Resultado Gerado	1](#_Toc68093858)

[5\.2 – Limpeza dos Lançamentos Gerados pela Transferência entre Apurações	1](#_Toc68093859)

[5\.3 – Geração dos Movimentos	1](#_Toc68093860)

# <a id="_Toc68093853"></a>Visão Geral da Solução

O processo do cálculo do Ressarcimento/Complemento do RS está dividido em etapas:

1º : Geração dos Movimentos

2º : Transferência do ICMS\-ST da Subapuração para a Apuração do ICMS \(Substituição Tributária\)

3º : Execução da Apuração do ICMS \(P9\) para recalcular os totais do resumo da Substituição Tributária\.

4º : Geração do Sped Fiscal

__Primeira Etapa:__

Na primeira etapa, Geração dos Movimentos, os documentos fiscais são recuperados com base nas parametrizações por produtos sujeitos a ICMS\-ST \(Código, NCM, Cest\) e operações \(CFOP, CFOP/Natureza Operação\) disponíveis no módulo do Ressarcimento RS\. 

Durante esse processo, os valores de ajuste de ICMS\-ST são calculados para os documentos fiscais e consolidados para realização dos lançamentos na Subapuração RS\. 

Pré\-requisito:

Para que a subapuração seja gerada, a parametrização em Dados Iniciais deve ser efetuada\.  Nesta tela, serão definidos o número da subapuração e informações dos itens da apuração a serem gerados\. Exemplo:

- Geração das Entradas 🡪 Item da Apuração  = 006 – Outros Créditos
- Geração das Saídas para Consumidor Final 🡪 Item da Apuração  = 002 – Outros Débitos
- Geração das Saídas para Outras Uf’s, Isentas ou não tributadas 🡪 Item da Apuração  = 003 – Estorno de Créditos

A subapuração, seus lançamentos e documentos vinculados aos lançamentos são base para a geração dos registros 1900, 1921, 1923 do SPED FISCAL \(terceira etapa\)\. 

Para conferência do resultado do processamento o módulo disponibiliza relatórios de Conferência, onde é possível conferir os documentos fiscais de entradas e saídas e os lançamentos realizados na subapuração\.

Feita as conferências, segue para a segunda etapa\.

__Segunda Etapa:__

Na seguda etapa,Transferência do ICMS\-ST da Subapuração para a Apuração do ICMS\-ST, o valor resultante da Subapuração, credor ou devedor do ICMS\-ST, é transferido para Apuração do ICMS\-ST\. 

Durante esse processo dois lançamentos são gerados:

- Um lançamento na Subapuração RS para estornar o valor transferido\. 
- Um lançamento na Apuração do ICMS\-ST para creditar ou debitar o valor transferido\.

Ao final deste processo a Subapuração RS ficará sempre zerada\.

O resultado esta etapa pode ser conferido através do relatório da Subapuração e de transferências disponíveis no módulo\.

A apuração do ICMS\-ST deve ser consultada diretamente no  módulo ICMS\.

__Terceira Etapa:__

Após a geração da transferência, a Apuração do ICMS deve ser executada para que os subtotais e totais de crédito e débito do Resumo da Substituição Tributária sejam recalculados\. Localização: módulo Estadual >> ICMS, item de menu DATA MART >> Apuração do ICMS\. 

Este procedimento já é adotado no DW, quando utliza\-se o Módulo Lançamentos Automáticos ICMS para gerar automaticamente lançamentos na apuração do ICMS e quando criamos manualmente lançamentos no módulo ICMS\. Em ambas as situações, após a criação dos lançamentos, a Apuração do ICMS deve ser executada\.

O Resumo da Apuração do ICMS\-ST serão recalculados a partir dos lançamentos\. Os valores dos lançamentos da tabela __ITEM\_APURAC\_SUBST__ são consolidados por código de operação, atualizando os códigos de operação do Resumo da Apuração do ICMS\-ST \(RESUMO\_APUR\_ST\)

__Quarta Etapa:__

A última etapa diz respeito à geração do SPED FISCAL, onde a Subapuração é demostrada nos registros do bloco 9 \(registros 1920, 1921, 1923\) e a apuração do ICMS\-ST no bloco E \(registros E210, E220\)

Tabelas que compõe a Subapuração: 

- Subapuração RS \(registro 1920\)
- Ajustes da Subapuração \(registro 1921\) 
- Identificação dos Documentos fiscais \(registro 1923\)

__Quanto a Subapuração__:

A Subapuração gerada no módulo Ressarcimento do RS é diferente da Subapuração do ICMS gerada no módulo ICMS\. Cada módulo só enxerga sua Subapuração\. Ou seja a Subapuração do RS não é enxergada pelo módulo ICMS, e vice\-versa\. 

A decisão de fazermos a Subapuração RS separada da Subapuração do ICMS, se deu pelos seguintes motivos:

- A Subapuração do ICMS tem regras completamente diferentes da Subapuração RS\. O conceito da Subapuração do ICMS é completamente diferente da Subapuração do RS\. A Subapuração do ICMS foi criada para detalhar determinados incentivos fiscal de ICMS criados por alguns estados\. Já a Subapuração do RS foi criada para ICMS\-ST\.
- O lançamento complementar realizado na Subapuração do ICMS, é demonstrado na Apuração do ICMS Oficial \(P9\)\. Como a geração do Ressarmcimento RS gera lançamentos a crédito e a débito de ICMS\-ST na Subapuração RS,se não tratássemos de forma diferenciada da Subapuração do ICMS, todos esses lançamentos iriam aparecer na Apuração do ICMS Oficial, o que estaria incorreto\.

Ou seja, mesmo tendo a Subapuração do ICMS e a Subapuração do RS sendo apresentadas no mesmo conjunto de registros do Sped Fiscal, as regras do cálculo das duas apurações são completamente diferentes\.  Por isso a Subapuração do RS foi criada completamente separada da Subapuração do ICMS, tanto processamento quanto o conjunto de tabelas que compõe a Subapuração\. Como consequencia desta decisão, os lançamentos a crédito e a débito gerados na Subapuração RS não podem ser alterados manualmente via tela de manutenção  do módulo ICMS \(menu Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração do ICMS >> Ajuste SINIEF ou Empresas c/ Inscr\. Estadual Única\)\. Como foi dito, cada módulo só manipula a Subapuração por ele gerada\. 

Veja a seguir, o conjunto de tabelas pertinente a cada uma das Sub\-Apurações\.

__Tabelas da APURAÇÃO ICMS__

__Tabelas da SUBAPURAÇÃO ICMS__

__Tabelas da SUBAPURAÇÃO RS__

__Tabelas da APURAÇÃO ICMS\-ST__

ITEM\_APURAC\_CALC

ICT\_SUB\_APURACAO

ICT\_SUB\_APURACAO\_RS

RESUMO\_APUR\_ST

ITEM\_APURAC\_DISCR

ITEM\_APURAC\_DISCR

ITEM\_APURAC\_SUBRS

ITEM\_APURAC\_SUBST

ITEM\_APURAC\_DISCR\_AJUSTE

ITEM\_APURAC\_DISCR\_AJUSTE

ITEM\_APURAC\_SUBRS\_AJUSTE

ITEM\_APURAC\_SUBST\_AJUSTE 

Base Legal: INSTRUÇÃO NORMATIVA RE Nº 048/18 

__MFS47349__

__Quanto a Parametrização de Produtos Associados__:

A recuperação dos movimentos de entradas e saídas é feita considerando o produto Principal seus os produtos Associados, definidos na Parametrização de Produtos, opção Por Código\. 

No relatório de conferência, os documentos fiscais são apresentados com seus respectivos produtos e agrupados em nome do Produto Principal\. 

No Sped Fiscal, o documento fiscal é apresentado no registo 1923 com o produto que de fato está escriturado na nota, não havendo forma de demonstrar a relação do Produto Principal com os Produtos Associados\. Esta relação só é possível observar dentro do módulo Ressarcimento ICMS\-ST RS, através dos relatórios de conferência dos movimentos\. 

# <a id="_Toc68093854"></a>Introdução

Particularmente a Geração dos Movimentos está definida pelo seguinte conjunto de documentos:

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\.docx

Documento principal que referencia todos os outros documentos\.

Contém especificação de tela da geração, validações gerais e a regra de disparo para cada tipo de geração \(entradas, saídas para consumidor final\)\.

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\.docx

Documento específico da geração dos movimentos de Saída para Consumidor Final deste Estado\.  Aplicada a contribuintes Varejistas e Não Varejistas\.

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\.docx

Documento específico da geração dos movimentos de Saída para outras UF’s, Isentas ou Não Tributadas\. Aplicada a contribuintes Varejistas\.

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\.docx

Documento específico da geração dos movimentos de Entrada sujeita a Substituição Tributária\. Aplicada a contribuintes Varejistas\.

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Nao\_Varejista

Documento específico da geração dos movimentos de Entrada sujeita a Substituição Tributária\. Aplicada a contribuintes Não Varejistas\.

__MFS81764__

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Estoque\.docx

Documento específico da geração dos créditos das mercadorias em estoque\. Aplicada a contribuintes Varejistas e Não Varejistas\.

__MFS81804__

MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\.docx

Documento específico da geração dos movimentos de Devolução das Saídas de mercadorias destinadas a consumidor final\. Aplicada a contribuintes Varejistas e Não Varejistas\.

Para facilitar o entendimento, a leitura deve partir do documento principal \(MTZ\-Ressarc\-RS\-Geracao\_Movimentos\.docx\) para os documentos específicos de cada tipo de geração\.

# <a id="_Toc68093855"></a>Parâmetros da Tela 

Aba Parâmetros

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Período:  

\[mm/aaaa\]

 

 

 

 

EXECUTAR

 

 \[  \] Gerar por Inscrição Estadual Única

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 \[ x  \] Gerar saídas para Consumidor Final

 

 

 

 

 

 \[ x \] Gerar entradas

\[ x \] Gerar saídas para Outras UF's, Isentas ou Não Tributadas 

 

 

 

 

 

 

 

 

 

 

 \[ x \] Gerar Devolução das Saídas de Mercadoria destinadas a Consumidor Final

 

 \[ x \] Gerar Parcela do Crédito das Mercadorias em Estoque

 

 

 

 Pesquisar Últimas entradas até: 

\[ dd/mm/aaaa \] 

 

 

 

 

 Data do Inventário:  \[dd/mm/aaaa \]

 

 

 

 

 

 \[  \] Utilizar DATA MART para períodos anteriores

\[ \] Considerar as notas fiscais da empresa incorporada

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

ESTABELECIMENTO

 

 

 

 

 

 

 

\[x \] 001 \- XXXXXXXXXXXXXXXXXXXXX

 

 

 

 

 

\[x \] 002 \- YYYYYYYYYYYYYYYYYYYYYYYYYYY

 

 

 

 

 

\[x \] 003 \- ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ

 

 

 

 

 

 

 

 

 

 

 

 

 

Funcionamento dos campos:

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

<a id="_Hlk517437550"></a>Período 

Data

\(mês e ano\)

S

S

\(MM/AAAA\)

Neste campo será informado o período \(mês e ano\) para a geração dos dados dos cupons fiscais\.

Deve ser um mês válido\.

Geração p/ Inscrição Estadual Ùnica

Check box

N

N

Não

O parâmetro de Geração p/ Inscrição Estadual Ùnica determina os estabelecimentos a serem apresentados\.

\(NÃO VAMOS TRATAR NA MFS\-28006, MFS\-28004\)

Gerar saídas para Consumidor Final

Check box

N

S

Não

Gerar saídas para Outras UF's, Isentas ou Não Tributadas \(Varejista\)

Check box

N

S

Não

Gerar Entradas

Check box

N

S

Não

Obs: Quanto a posição deste campo na tela, ele não deve ficar antes do “Gerar Saídas para Consumidor Final”, pois para contribuinte não varejista, a geração da entrada depende da saída para consumidor final\.

__MFS81804__

Gerar Devolução das Saídas de Mercadoria destinadas a Consumidor Final

Check box

N

S

Não

__MFS81764__

Gerar Parcela do Crédito das Mercadorias em Estoque

Check box

N

S

Não

Parâmetro deve ser marcado para gerar o lançamento em Outros Créditos referente a 1/3 dos Créditos dos produtos sujeitos a ST existente no estoque\. Segundo a IN48, o crédito existente em estoque será lançado em três parcelas mensais e iguais\.

Pesquisar Últimas entradas até:

Data

\(dd/mm/aaaa\)

N

N

DD/MM/AAAA

__Default__: 01/01/XXXX, onde XXXX é o ano anterior à Data Inicial\.

Neste campo é informada a data limite até onde será feita a pesquisa das últimas notas de entrada do produto\.

Este ficará habilitado/desabilitado dependendo dos campos “Gerar Entradas” e “Gerar saídas para Outras UF's, Isentas ou Não Tributadas \(Varejista\)”\. 

Caso “Gerar Entradas” OU “Gerar saídas para Outras UF's, Isentas ou Não Tributadas \(Varejista\)” seja marcado, então:

    O sistema deve habilitar do campo “Pesquisar Últimas entradas até:”\.

Caso contrário, 

     O sistema deve limpar e desabilitar do campo “Pesquisar Últimas entradas até:”\.

Obs: Deve ser uma data válida e <= ao primeiro dia do Período informado\. A pesquisa da movimentação das entradas, na geração para contribuintes Não Varejistas, considera o Período informado até a data limite informada neste campo\. Assim, esta data é apenas um limite “genérico” para os casos em que as entradas não sejam encontradas \(para evitar que a pesquisa seja feita indeterminadamente\)\.

__MFS81764__

Data do Inventário

Data

\(dd/mm/aaaa\)

__N__

N

DD/MM/AAAA

Este campo deve ser habilitado apenas quando o campo “Gerar Parcela do Crédito das Mercadorias em Estoque” estiver marcado\.

Caso “Gerar Parcela do Crédito das Mercadorias em Estoque” seja marcado, então:

    O sistema deve habilitar do campo “Data do Inventário”\.

Caso contrário, 

     O sistema deve limpar e desabilitar o campo “Data do Inventário”\.

__MFS81804__

Utilizar DATA MART 

para períodos anteriores

Check box

__N__

N

Não

__MFS591083__

Considerar as notas fiscais da empresa incorporada

Alfanumérico

N

S

Check\-box, com default habilitado e desmarcado\.

Este campo é um checkbox onde o usuário informa se vai considerar as notas fiscais de entrada da empresa incorporada, além das notas fiscais da empresa/estabelecimento da geração\. Aplicável a duas gerações:

\- Saídas para Outras UF's, Isentas ou Não Tributadas \(Varejista\) 

\- Entradas Não Varejistas\.

Estabelecimentos

Alfanumérico 

__S__

S

Neste campo é exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário\.

Serão disponibilizados para seleção apenas os estabelecimentos de RS \(UF do estabelecimento = RS\)\.

Selecionar

N

N

Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos\.

O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimento”:

\- Somente Estabelecimentos da empresa do login;

\- Somente Estabelecimentos da UF de RS;

Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimentos” já marcados\. 

   

Marcar todos

N

N

Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos”\.

# <a id="_Toc68093856"></a>Críticas 

Existem informações obrigatórias para a geração dos movimentos que são solicitadas através das parametrizações disponíveis no módulo\.

Assim, antes de iniciar cada uma das gerações \(das entradas, saídas para consumidor final\.\.\.\), vamos checar se elas foram feitas\. Caso encontre alguma falha nestas verificação, o processo será aborado\.

__Consistências dos Parâmetros da Tela de Geração:__

Pelo menos uma das opções de gerações deve estar selecinada:

- Gerar Parcela do Crédito das Mercadorias em Estoque \[__MFS81764\]__
- Gerar Devolução das Saídas de Mercadoria destinadas a Consumidor Final __\[MFS81804\]__
- Gerar Entradas
- Gerar saídas para Consumidor Final
- Gerar saídas para Outras UF's, Isentas e Não Tributadas \(Varejista\)

Caso nenhum esteja selecionada, exibir mensagem de erro no Log da Geração:

“*Faltou informar os movimentos a serem gerados \(Entradas, Saídas para Consumidor Final, Saídas para Outras Ufs, Isentas ou Não Tributadas, Crédito das Mercadorias em Estoque, Devolução de Saídas\)*\. 

Caso o contribuinte seja __Não Varejista__, executar as validações abaixo:

1. Caso a opção “Gerar saídas para Outras UF's, Isentas ou Não Tributadas \(Varejista\)” seja selecionado, exibir mensagem de erro no Log da Geração:

*“A Geração das Saídas para Outras Ufs, Isentas ou Não Tributadas se aplica especificamente a contribuintes Varejistas\.”*

1. Caso a opção “Gerar Entradas” seja selecionado e não for informada a data em “Pesquisar as últimas entradas até”, exibir mensagem de erro no Log da Geração:

*“Data da Pesquisa das últimas entradas deve ser preechida e menor ou igual ao Período informado\.”*

1. Caso a opção “Gerar Entradas” seja selecionado e a Data informada em “Pesquisar as últimas entradas até” seja maior que o primeiro dia do Período informado, exibir a mensagem de erro: 

“*Data da Pesquisa das últimas entradas deve ser preechida e menor ou igual ao o Período informado”\.*

Caso o contribuinte seja __Varejista__, executar as validações abaixo:

1. Caso a opção “Gerar saídas para Outras UF's, Isentas ou Não Tributadas \(Varejista\)” seja selecionado e não for informada a data em “Pesquisar as últimas entradas até”, exibir mensagem de erro no Log da Geração::

*“Data da Pesquisa das últimas entradas deve ser preechida e menor ou igual ao Período informado\.”*

1. Caso a opção “Gerar saídas para Outras UF's, Isentas ou Não Tributadas \(Varejista\)” seja selecionado e a Data informada em “Pesquisar as últimas entradas até” seja maior que o primeiro dia do Período informado, exibir a mensagem de erro: 

“*Data da Pesquisa das últimas entradas deve ser preechida e menor ou igual ao o Período informado”\.*

\[__MFS81764\]__

Tanto para contribuinte __Varejista__ como para __Não Varejista__, executar a validação a seguir:

1. Caso a opção “Gerar Parcela do Crédito das Mercadorias em Estoque” seja selecionada e a Data do Inventário não esteja preenchida, exibir mensagem de erro no Log da Geração:

*“Data do Inventário deve ser informada\.”*

1. Caso a opção “Gerar Parcela do Crédito das Mercadorias em Estoque” seja selecionada e já existam três lançamentos relativos às parcelas do crédito em estoque para o estabelecimento, realizados em períodos anteriores ao informado na tela da geração, então exibir a seguinte mensagem:

*“O crédito das mercadorias em estoque já foi creditado em três parcelas com lançamentos nas apurações anteriores\. Sendo assim, para realizar esta apuração o parâmetro Gerar Parcela do Crédito das Mercadorias em Estoque deve estar desmarcado\.“*

Para fazer esta crítica, consultar a tabela de Ajustes da Subapuração RS \(ITEM\_APURAC\_SUBRS\) com os seguintes critérios:

\- código empresa de login

\- código do estabelecimento informado na tela de geração

\- data da apuração menor que o primeiro dia do período informado na tela

\- IND\_DIG\_CALCULADO = ‘__6’__ – lançamento gerado via processo de geração da parcela do crédito das mercadorias em estoque;

Se a consulta retornar 3 registros, a mensagem de erro deve ser exibida\.

1. Caso a opção “Gerar Parcela do Crédito das Mercadorias em Estoque” seja selecionada e a Data do Inventário esteja preenchida com uma data maior que o último dia do Período informado em tela, exibir mensagem de erro no Log da Geração:

*“Data do Inventário não pode ser superior ao Período informado\.”*

A definição para contribuinte ser  varejista ou não varejista, está na parametrização dos Dados Iniciais\.

Acontecendo qualquer erro, finalizar a geração com status = “\-1” – Erro\.

__Consistências para Controle de Depedência entre Geração das Entradas e Geração das Saídas a Consumidor Final:__

A regra abaixo se aplica especificamente à contribuintes __Não Varejistas__\.

A geração da entrada \(Não Varejista\) tem como pré\-requisito a execução da geração da saída para consumidor final\. Logo, para contribuintes Não Vareistas, duas situações são proibidas:

- Gerar a entrada sem a existência de movimento de saída para consumidor final para o estabelecimento / período / livro\. 
- Regerar a saída para consumidor final sem regerar entrada, no caso que já existam movimentos de saída e entrada gerados para o estabelecimento / período / livro\. 

Caso o contribuinte seja __Não Varejista__, executar as validações abaixo:

1. Caso a opção “Gerar Entradas” esteja selecionada, a opção “Gerar saídas para Consumidor Final” desmarcada e não exista movimento de Saída para Consumidor Final gerado para o estabelecimento / período / livro, exibir mensagem de erro no Log da Geração:

“*Não é possível realizar a geração das Entradas para o estabelecimento XXX, pois a geração de Saída para Consumidor Final não foi realizada para o período informado\. Favor selecionar a opção de geração para Saídas para Consumidor Final\.” *

1. Caso a opção “Gerar saídas para Consumidor Final” esteja selecionado e “Gerar Entradas” desmarcado, e exista movimento de Entrada gerado para o estabelecimento / período / livro, exibir mensagem de erro no Log da Geração:

“*Não é possível realizar a geração das Saídas para Consumidor Final para o estabelecimento XXX, sem regerar as Entradas\. Favor selecionar  as duas opções de geração Saídas para Consumidor Final e Entradas\.” *

Acontecendo qualquer erro, finalizar a geração com status = “\-1” – Erro\.

__Consistência da Paramentrização dos Dados Iniciais:__

Verificar se existe parametrização dos Dados Iniciais para a Empresa e Estabelecimento foco da geração\.

Verificar se a parametrização contém as informações que são obrigatórias para a geração:

- Subapuração
- Código de Ajuste de Sped Fiscal

Se não for encontrada parametrização dos Dados Iniciais, exibir a seguinte mensagem no Log da Geração:

*Faltou realizar parametrização dos Dados Iniciais para o estabelecimento”\.*

Se a informação de Subapuração não for encontrada, exibir a seguinte mensagem no Log da Geração:

*“Subapuração não informada para o Estabelecimento\. Favor realizar parametrização dos Dados Iniciais”\.*

Se o número da Subapuração parametrizada nos Dados Iniciais, já estiver sendo utilizado em subapurações, oriundas do módulo Estadual >> ICMS \(menu Apuração >> Sub\-Apurações do Sped Fiscal >> Apuração dos Resultados\), exibir a seguinte mensagem no Log da Geração:

*“Número da Subapuração RS parametrizada em Dados Iniciais, já utilizada por outra Subapuração no Módulo ICMS\. Favor redefinir o número da Subapuração RS\.”*

Se a opção “Gerar Entradas” estiver selecionada e não for encontrado o Código de Ajuste de Outros Créditos para Entrada de mercadorias, exibir a seguinte mensagem no Log da Geração:

*“Código de Ajuste de Outros Créditos para Entrada de mercadorias não informado para o Estabelecimento\. Favor realizar parametrização dos Dados Iniciais”\.*

Se a opção “Gerar Saídas para Consumidor Final” estiver selecionada e não for encontrado o Código de Ajuste de Outros Débitos para Saídas de mercadorias destinadas a consumidor final deste Estado, exibir a seguinte mensagem no Log da Geração:

*“Código de Ajuste de Outros Débitos para Saídas de mercadorias destinadas a consumidor final deste Estado não informado para o Estabelecimento\. Favor realizar parametrização dos Dados Iniciais”\.*

Se a opção “Gerar Saídas para Outras Ufs, Isentas e Não Tributadas” estiver selecionada e não for encontrado o Código de Ajuste de Estorno de Crédito para Saídas de mercadorias destinadas a outros Estados ou isentas ou não tributadas, exibir a seguinte mensagem no Log da Geração:

*“Código de Ajuste de Estorno de Crédito para Saídas de mercadorias destinadas a outros Estados ou isentas ou não tributadas, não informado para o Estabelecimento\. Favor realizar parametrização dos Dados Iniciais”\.*

\[__MFS81764\]__

Se a opção “Gerar Parcela do Crédito das Mercadorias em Estoque” estiver selecionada e não for encontrado o Código de Ajuste de Outros Créditos para Mercadorias em Estoque, exibir a seguinte mensagem no Log da Geração:

*“Código de Ajuste de Outros Créditos para Mercadorias em Estoque não informado para o Estabelecimento\. Favor realizar parametrização dos Dados Iniciais”\.*

__\[MFS81804\]__

Se a opção “Gerar Devolução das Saídas de Mercadoria destinadas a Consumidor Final” estiver selecionada e não for encontrado o Código de Ajuste de Outros Créditos para Devolução das Saídas de Mercadorias destinadas a Consumidor Final deste Estado, exibir a seguinte mensagem no Log da Geração:

	“*Código de Ajuste de Outros Créditos para Devolução das Saídas de Mercadorias destinadas a Consumidor Final deste Estado, não informado para o Estabelecimento\. Favor realizar a parametrização dos Dados Iniciais\.”*

__Parametrização de Produtos \(por Código, por NCM e por CEST\):__

Verificar se existe pelo menos uma das parametrizaçoes para Produto \(por Código, por NCM e por CEST\) para a UF = RS\.

Se não for encontrada nenhuma das parametrizações, então exibir mensagem no Log da Geração:

*“Faltou realizar parametrização por Produto”\.*

__Parametrização de Operação \(por CFOP, por Natureza de Operação\)__

__\[MFS81804\]__

Se pelo menos uma das opções “Gerar Saídas para Consumidor Final”ou “Gerar Devolução das Saídas de Mercadoria destinadas a Consumidor Final” estiver selecionada, então:

Verificar se existe pelo menos uma das parametrizaçoes para Operação de “Saída a Consumidor Final \(e Devoluções\)” \(código parâmetro __744__\), por CFOP ou por Natureza de Operação\)\. 

Se não for encontrada parametrização de CFOP nem Natureza de Operação, então exibir mensagem no Log da Geração:

*“Faltou realizar parametrização por CFOP e/ou Natureza da Operação para a Saída a Consumidor Final \(e devoluções\)”\.*

Se a opção “Gerar Saídas para Outras Ufs, Isentas e Não Tributadas” estiver selecionada, então:

Verificar se existe pelo menos uma das parametrizaçoes para Operação de “Saida para outro Estado, Saida Isenta ou Nao Tributada” \(código parâmetro __745__\), por CFOP ou por Natureza de Operação\)\. 

Se não for encontrada parametrização de CFOP nem Natureza de Operação, então exibir mensagem no Log da Geração:

*“Faltou realizar parametrização por CFOP e/ou Natureza da Operação para a Saída para outro Estado, Saída Isenta ou Não *

*Tributada”\.*

Se a opção “Gerar Entradas” estiver selecionada, então:

Verificar se existe pelo menos uma das parametrizaçoes para Operação de “Entrada com Substituicao Tributaria” \(código parâmetro __746__\), por CFOP ou por Natureza de Operação\)\. 

Se não for encontrada parametrização de CFOP nem Natureza de Operação, então exibir mensagem no Log da Geração:

*“Faltou realizar parametrização por CFOP e/ou Natureza da Operação para Entrada com Substituição Tributária\.”\.*

Acontecendo qualquer erro, finalizar a geração com status = “\-1” – Erro\.

# <a id="_Toc68093857"></a>Processamento

## <a id="_Toc68093858"></a>5\.1 – Limpeza do Resultado Gerado 

Limpar os lançamentos da tabela de Ajustes da Subapuração do RS \(ITEM\_APURAC\_SUBRS\) e os documentos fiscais vinculados ao ajuste \(ITEM\_APURAC\_SUBRS\_AJUSTE\) que foram gerados neste processo\.

Por isso que é importante identificar os laçamentos gerados por esse processo \(IND\_DIG\_CALCULADO da ITEM\_APURAC\_SUBRS\)\.

Utilizar os critérios:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Códigos dos estabelecimentos selecionados em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

- Indicador de Lançamento Digitado/calculado  \(ind\_dig\_calculado\) =

 __2 __– lançamento gerado via processo de geração da saida a Consumidor Final\.

__ 3__ – lançamento gerado via processo de geração das entradas\.

‘__4’ __– lançamento gerado via processo de geração da saida para outras Ufs, Isentas ou Não Tributadas

‘__6’__ – lançamento gerado via processo de geração da parcela do crédito das mercadorias em estoque \[MFS81764\]

__7 __– lançamento gerado via processo de geração da devolução das saidas para consumidor final\. \[MFS81804\]

Caso o opção “Gerar Parcela do Crédito das Mercadorias em Estoque” estiver selecionada na tela de geração, limpar os inventários da tabela ITEM\_APURAC\_SUBRS\_INVENT\.

## <a id="_Toc68093859"></a>5\.2 – Limpeza dos Lançamentos Gerados pela Transferência entre Apurações

Antes de iniciar a geração dos movimentos, vamos eliminar os lançamentos de transferência, gerados pelo Processso de Transferência Entre Apurações\.

Esse procedimento é necessário, pois há possibidade de um reprocessamento da geração do movimento após a execução do processo de transferência entre apurações\. 

__Eliminação do Lançamento na Tabela de Ajustes da Subapuração RS \(ITEM\_APURAC\_SUBRS\)__

Identificar o lançamento com os critérios abaixo:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Códigos dos estabelecimentos selecionados em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

- Indicador de Lançamento Digitado/calculado  \(ind\_dig\_calculado\) = __‘5’__ \- lançamento gerado via processo de transferência

__Eliminação do Lançamento na Tabela de Lançamentos da Apuração do ICMS\-ST \(ITEM\_APURAC\_SUBST\)__

Identificar o lançamento com os critérios abaixo:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Códigos dos estabelecimentos selecionados em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = "108", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" estiver desmarcado\.  

                                          "165", quando o parâmetro "Geração p/ Inscrição Estadual Ùnica" marcado

- Indicador de Lançamento Digitado/calculado  \(ind\_dig\_calculado\) = __‘5’__ \- lançamento gerado via processo de transferência

## <a id="_Toc68093860"></a>5\.3 – Geração dos Movimentos

Este processamento é composto pelas gerações: entradas \(Varejistas\), entradas \(Não Varejistas\), saídas para Consumidor Final, saídas para outras Ufs, Isentas ou Não Tributadas e estoque\.

As gerações dos movimentos de entradas e saídas partem a leitura de documentos fiscais e finalizam com a gravação de um conjunto de tabelas que compõe a Subapuração RS:

- Subapuração RS \(registro 1920\)
- Ajustes da Subapuração \(registro 1921\) 
- Identificação dos Documentos fiscais \(registro 1923\)

Ja a geração do movimento de estoque parte da leitura do inventário \(SAFX52\) e finaliza com a gravação do mesmo conjunto de tabelas que compõe a Subapuração RS\.

As regras específicas de cada geração estão definidas nas matrizes:

- MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\.doc
- MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\.doc
- MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\.doc
- MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Nao\_Varejista\.doc
- MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Estoque\.docx \[MFS81764\]
- MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\.docx \[MFS81804\]

\[MFS81764\]

Se a opção “Gerar Parcela do Crédito das Mercadorias em Estoque” estiver selecionada, então:

	Executar a geração do movimento de estoque\.

	Para isso ver as regras descritas no “MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Estoque\.docx”

\[MFS81804\]

Se a opção “Gerar Devolução das Saídas de Mercadoria destinadas a Consumidor Final” estiver selecionada, então:

	Executar a geração do movimento de Devolução de Saída\.

	Para isso ver as regras descritas no “MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Devolucao\_Saidas\_Consumidor\_Final\.docx”

Se a opção “Gerar Saídas para Consumidor Final” estiver selecionada, então:

	Executar a geração dos movimentos de Saída para Consumidor Final deste Estado\.

Para isso ver as regras de geração descritas no “MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Consumidor\_Final\.doc”\.	

Se a opção “Gerar Saídas para Outras Ufs, Isentas e Não Tributadas” estiver selecionada, então:

	Executar geração dos movimentos de saída para outras Ufs, ou Isentas ou Não tributadas\.

Para isso ver as regras de geração descritas no “MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Saidas\_Outras\_UFs\.doc”\.

Se o contribuinte for__ Varejista__ a opção “Gerar Entradas” estiver selecionada, então:

	Executar a geração dos movimentos de entradas com Substituição Tributária\.

Para isso ver as regras de geração descritas no “MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Varejista\.doc”\.

Se o contribuinte for __Não Varejista __a opção “Gerar Entradas” estiver selecionada, então:

Caso não exista movimento de Saída para Consumidor Final gerado para o estabelecimento / período / livro, exibir mensagem de erro no Log da Geração:

“*Não é possível realizar a geração das Entradas para o estabelecimento XXX, pois não há movimentação de Saída para Consumidor Final gerada para o período informado\.” *

	Caso contrário: 

	Executar a geração dos movimentos de entradas com Substituição Tributária\.

Para isso ver as regras de geração descritas no “MTZ\-Ressarc\-RS\-Geracao\_Movimentos\_Entradas\_Nao\_Varejista\.doc”\.

Observação:

Existe uma ordem de execução entre as gerações no caso do contribuinte ser __Não Varejista__: primeiro efetua a geração das Saídas para Consumidor Final e em seguida a geração das Entradas\.

	

= = = = = =

 


# MTZ-DFC-PR

- **Fonte:** MTZ-DFC-PR.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 51 KB

---

# MTZ – DFC\-PR

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Autor__

__Regras de Negócio__

OS1495

Criação do Módulo

Disponibilizar módulo DFC\-PR

CH76177

Atualização dos CFOP’s

Inclusão de CFOP’s na geração dos Quadros 17 e 18

OS3111\-F

Permitir geração por Inscrição Estadual Única e Gerar Quadro 22 por Município do Ponto de Consumo

Alterar as rotinas de geração da DFC\-PR para atender o segmento de utilities e também inscrição estadual única\.

OS3348

Criar parametrização por CFOP/Natureza de Operação para gerar Quadro 22

Criar parametrização por CFOP/Natureza de Operação para gerar Quadro 22

__CH122226__

Arredondamento de valores

Alteração no tratamento da soma do quadro 17, registro tipo 02

__CH81\_2012__

Correção na geração do Quadro 22

Correção na geração do Quadro 22

__CH12999\_2012__

Número Responsável

Correção do campo CPF do contabilista Registro Tipo 01

Edilson Marcelino

__RN50__

__CH1432\_2012__

Tipo do Responsável

Alteração do campo para gerar fixo “C” Registro Tipo 01, conforme alteração legal

Edilson Marcelino

__RN49__

__CH81\-A\_2012__

Correção na geração do Quadro 22

Correção para considerar os documentos de frete \(SAFX07\) sem itens na SAFX51 para a totalização dos valores do Quadro 22 \(ver RN61\)\. 

Vânia Dias Mattos 

__CH5302\_2014__

Correção na geração do Quadro 22

Correção da totalização dos valores do Quadro 22 por documento fiscal de transporte 

Julyana Perrucini

__RN61__

__CH1876\_2013__

Atualização na geração das Linhas 907 e 914

Inclusão de novos CFOPs válidos

Marcos de Paula

__RN28 e RN35__

__CH449\-A\_2015__

Atualização versão 25\.00

Este documento tem como objetivo tratar a geração do arquivo magnético para que o exercício 2015 desconsidere a GI\.

Julyana Perrucini

__RN43\-A__

__RN45__

__RN51__

## REGRAS DE NEGÓCIO

OS de Criação: 1495

OS de Atualização: 2310

#### Cód\.

### Descrição

### DR

__RN00__

__Quadro 17 – Linha 801__

Considerar para a geração desta linha os seguintes CFOP’s:

1101 a 1126 \+ 1401 \+ 1403 \+ 1651 a 1653

OS1495

__RN01__

__Quadro 17 – Linha 802__

Considerar para a geração desta linha os seguintes CFOP’s:

1151 \+ 1152 \+ 1154 \+ 1408 a 1411 \+ 1201 a 1209 \+ 1658 a 1662

OS1495

__RN02__

__Quadro 17 – Linha 803__

Considerar para a geração desta linha os seguintes CFOP’s:

1251 a 1257 \+ 1153

OS1495

__RN03__

__Quadro 17 – Linha 804__

Considerar para a geração desta linha os seguintes CFOP’s:

1301 a 1306

OS1495

__RN04__

__Quadro 17 – Linha 805__

Considerar para a geração desta linha os seguintes CFOP’s:

1351 a 1356 \+ 1360 \+ 1931 \+ 1932

OS1495

__RN05__

__Quadro 17 – Linha 806__

Considerar para a geração desta linha os seguintes CFOP’s:

1351 a 1356 \+ 1360 \+ 1931 \+ 1932

OS1495

__RN06__

__Quadro 17 – Linha 807__

Considerar para a geração desta linha os seguintes CFOP’s:

1451 \+ 1452 \+ 1501 a 1504 1910 \+ 1911

OS1495

__RN07__

__\[ALTERADO CH76177\]__

__Quadro 17 – Linha 808__

Considerar para a geração desta linha os seguintes CFOP’s:

1601 a 1605 \+ 1414 \+ 1415 \+ 1505 \+ 1506 \+ 1901 a 1909 \+ 1912 a 1926 \+ 1933 \+ 1949 \+ 1663 a 1664

OS1495 / 

CH76177

__RN08__

__Quadro 17 – Linha 809__

Considerar para a geração desta linha os seguintes CFOP’s:

2101 a 2126 \+ 2401 \+ 2403 \+ 2151 \+ 2152 \+ 2154 \+ 2408 a 2411 \+ 2201 a 2209 \+ 2651 a 2662

OS1495

__RN09__

__Quadro 17 – Linha 810__

Considerar para a geração desta linha os seguintes CFOP’s:

2251 a 2257 \+ 2153

OS1495

__RN10__

__Quadro 17 – Linha 811__

Considerar para a geração desta linha os seguintes CFOP’s:

2301 a 2306

OS1495

__RN11__

__Quadro 17 – Linha 812__

Considerar para a geração desta linha os seguintes CFOP’s:

2351 a 2356 \+ 2931 \+ 2932

OS1495

__RN12__

__Quadro 17 – Linha 813__

Considerar para a geração desta linha os seguintes CFOP’s:

2406 \+ 2407 \+ 2551 a 2557

OS1495

__RN13__

__Quadro 17 – Linha 814__

Considerar para a geração desta linha os seguintes CFOP’s:

2501 a 2504 \+ 2910 \+ 2911

OS1495

__RN14__

__\[ALTERADO CH76177\]__

__Quadro 17 – Linha 815__

Considerar para a geração desta linha os seguintes CFOP’s:

2603 \+ 2414 \+ 2415 \+ 2505 \+ 2506 \+ 2901 a 2909 \+ 2912 a 2925 \+ 2933 \+ 2949 \+ 2663 a 2664

OS1495 / CH76177

__RN15__

__Quadro 17 – Linha 816__

Considerar para a geração desta linha os seguintes CFOP’s:

3101 a 3126 \+ 3201 a 3207 \+ 3503 \+ 3651 a 3653

OS1495

__RN16__

__Quadro 17 – Linha 817__

Considerar para a geração desta linha os seguintes CFOP’s:

3251

OS1495

__RN17__

__Quadro 17 – Linha 818__

Considerar para a geração desta linha os seguintes CFOP’s:

3301

OS1495

__RN18__

__Quadro 17 – Linha 819__

Considerar para a geração desta linha os seguintes CFOP’s:

3351 a 3356

OS1495

__RN19__

__Quadro 17 – Linha 820__

Considerar para a geração desta linha os seguintes CFOP’s:

3551 a 3556

OS1495

__RN20__

__Quadro 17 – Linha 821__

Considerar para a geração desta linha os seguintes CFOP’s:

3127 \+ 3211

OS1495

__RN21__

__Quadro 17 – Linha 822__

Considerar para a geração desta linha os seguintes CFOP’s:

3930 \+ 3949

OS1495

__RN22__

__\[ALTERADO CH76177\]__

__Quadro 18 – Linha 901__

Considerar para a geração desta linha os seguintes CFOP’s:

5101 a 5125 \+ 5401 a 5411 \+ 5151 \+ 5152 \+ 5155 \+ 5156 \+ 5201 a 5210 \+ 5651 a 5656 \+ 5658 a 5662 \+ 5667

OS1495 / CH76177

__RN23__

__Quadro 18 – Linha 902__

Considerar para a geração desta linha os seguintes CFOP’s:

5251 a 5258 \+ 5153

OS1495

__RN24__

__Quadro 18 – Linha 903__

Considerar para a geração desta linha os seguintes CFOP’s:

5301 a 5307

OS1495

__RN25__

__\[ALTERADO CH76177\]__

__Quadro 18 – Linha 904__

Considerar para a geração desta linha os seguintes CFOP’s:

5351 a 5357 \+ 5360 \+ 5931 \+ 5932 \+ 5359

OS1495 / CH76177

__RN26__

__Quadro 18 – Linha 905__

Considerar para a geração desta linha os seguintes CFOP’s:

5412 \+ 5413 \+ 5551 a 5557

OS1495

__RN27__

__Quadro 18 – Linha 906__

Considerar para a geração desta linha os seguintes CFOP’s:

5451 \+ 5501 a 5503 \+ 5910 \+ 5911 \+ 5927 \+ 5928

OS1495

__RN28__

__\[ALTERADO CH1876/2013\]__

__Quadro 18 – Linha 907__

Considerar para a geração desta linha os seguintes CFOP’s:

5414 \+ 5415 \+ 5504 \+ 5505 \+ 5601 a 5606 \+ 5901 a 5909 \+ 5912 a 5926 \+ 5929 \+ 5949 \+ 5657 \+ 5663 a 5666 \+ 5933 \+ 5934

OS1495 / CH76177/

CH1876/2013

__RN29__

__\[ALTERADO CH76177\]__

__Quadro 18 – Linha 908__

Considerar para a geração desta linha os seguintes CFOP’s:

6101 a 6125 \+ 6401 a 6411 \+ 6151 \+ 6152 \+ 6155 \+ 6156 \+ 6201 a 6210 \+ 6651 a 6656 \+ 6658 a 6662 \+ 6667

OS1495 / CH76177

__RN30__

__Quadro 18 – Linha 909__

Considerar para a geração desta linha os seguintes CFOP’s:

6251 a 6258 \+ 6153

OS1495

__RN31__

__Quadro 18 – Linha 910__

Considerar para a geração desta linha os seguintes CFOP’s:

6301 a 6307

OS1495

__RN32__

__\[ALTERADO CH76177\]__

__Quadro 18 – Linha 911__

Considerar para a geração desta linha os seguintes CFOP’s:

6351 a 6357 \+ 6360 \+ 6931 \+ 6932 \+ 6359

OS1495 / CH76177

__RN33__

__Quadro 18 – Linha 912__

Considerar para a geração desta linha os seguintes CFOP’s:

6412 \+ 6413 \+ 6551 a 6557

OS1495

__RN34__

__Quadro 18 – Linha 913__

Considerar para a geração desta linha os seguintes CFOP’s:

6501 a 6503 \+ 6910 \+ 6911

OS1495

__RN35__

__\[ALTERADO CH1876/2013\]__

__Quadro 18 – Linha 914__

Considerar para a geração desta linha os seguintes CFOP’s:

6603 \+ 6901 a 6909 \+ 6414 \+ 6415 \+ 6504 \+ 6505 \+ 6912 a 6929 \+ 6949 \+6657 \+ 6663 a 6666 \+ 6933 \+ 6934

OS1495 / CH76177/

CH1876/2013

__RN36__

__\[ALTERADO CH76177\]__

__Quadro 18 – Linha 915__

Considerar para a geração desta linha os seguintes CFOP’s:

7101 a 7106 \+ 7127 \+ 7501 \+ 7651 a 7654 \+ 7667

OS1495 / CH76177

__RN37__

__Quadro 18 – Linha 916__

Considerar para a geração desta linha os seguintes CFOP’s:

7201 a 7210 \+ 7211

OS1495

__RN38__

__Quadro 18 – Linha 917__

Considerar para a geração desta linha os seguintes CFOP’s:

7251

OS1495

__RN39__

__Quadro 18 – Linha 918__

Considerar para a geração desta linha os seguintes CFOP’s:

7301

OS1495

__RN40__

__Quadro 18 – Linha 919__

Considerar para a geração desta linha os seguintes CFOP’s:

7358

OS1495

__RN41__

__Quadro 18 – Linha 920__

Considerar para a geração desta linha os seguintes CFOP’s:

7551 a 7556 \+ 7930 \+ 7949

OS1495

__RN42__

__DFC\-PR → Parâmetros → Dados Acessórios__

Criar o flag __\[   \] Considerar Município do Ponto de Consumo \(Utilities\)__

Quando o flag estiver marcado:

\- Considerar o Município do Ponto de Consumo \(campo 76/safx42\) na geração do campo 02/Quadro 22

\- Esta situação somente irá se aplicar às notas de saídas que estiverem na safx42 \(modelo 01, 06, 21 ou 22\)

\- Para as notas que estiverem na x07, considerar o município do cadastro da pessoa fis/jur \(safx04\)

Quando o flag estiver desmarcado:

\- Considerar o município do cadastra de pessoa fis/jur, \(campos\), de acordo com a pessoa fis/jur da NF\.

OS3111\-F

__RN43__

__DFC\-PR → Obrigações → Geração dos Registros__

Criar o flag __\[   \] Geração Centralizada c/ Insc\. Estadual Única__

Se parâmetro __Geração centralizada por Inscrição Estadual Única__ *desmarcado*:

     Mostrar todos os Estabelecimentos da Empresa\.

Se parâmetro __Geração centralizada por Inscrição Estadual Única__ *marcado*:

     Mostrar apenas os Estabelecimentos parametrizados como *centralizadores* na parametrização dos Estabelecimentos com Inscrição Estadual Única do módulo de Controle das Obrigações Estaduais\.

OS3111\-F

__RN43\-A__

__Os documentos correspondentes ao exercício 2015, contendo informações do ano\-base 2014 e baixas no exercício desconsidera a entrega da GI__ __a partir de 01/01/2015, conforme o Regulamento do ICMS\.__

__Então quando o “Ano base” informado na tela de Geração dos Arquivos – DFC\-PR for igual a 2014, desconsiderar a geração da GI\.__

OS449\-A\_2015

__RN44__

__Registro Tipo 1__

__Campo Tipo do Registro__

Gravar o valor fixo = 1\.

OS1495

__RN45__

__Registro Tipo 1__

__Campo Tipo de Documento__

Gravar o código conforme especificação da regra abaixo:

1. Gravar o código 21 quando o usuário selecionar o campo “Normal” no quadro DFC da tela de parâmetros para geração\.
2. Gravar o código 22 quando o usuário selecionar o campo “Retificação” no quadro DFC da tela de parâmetros para geração\.
3. Gravar o código 24 quando o usuário selecionar o campo “Baixa” no quadro DFC da tela de parâmetros para geração\.
4. Gravar o código 31 quando o usuário selecionar o campo “Normal” no quadro GI da tela de parâmetros para geração\.
5. Gravar o código 32 quando o usuário selecionar o campo “Retificação” no quadro GI da tela de parâmetros para geração\.
6. Gravar o código 33 quando o usuário selecionar o campo “Baixa” no quadro GI da tela de parâmetros para geração\.

__\[ALTERADA – CH449\-A\_2015\]__

__Tratamento:__

Quando o campo “Ano base” informada na tela de Geração dos Arquivos – DFC\-PR for igual a 2014, desconsiderar a geração da GI\.

OS1495

CH449\-A\_2015

__RN46__

__\[ALTERADA OS3111\-F\]__

__Registro Tipo 1__

__Campo Inscrição CAD/ICMS__

Gravar o número da inscrição estadual do cadastro de Empresa/Estabelecimento com dígitos verificadores\.

No caso de geração por Inscrição Estadual Única, gravar a inscrição estadual do estabelecimento centralizador\.

OS1495 / OS3111\-F

__RN47__

__\[ALTERADA OS3111\-F\]__

__Registro Tipo 1__

__Campo Inscrição CNPJ__

Gravar o número de inscrição no CNPJ do cadastro de Empresa/Estabelecimento\.

No caso de geração por Inscrição Estadual Única, gravar a inscrição estadual do estabelecimento centralizador\.

OS1495 / OS3111\-F

__RN48__

__Registro Tipo 1__

__Campo Data Referência__

Gravar a data informada no campo “Ano base” na tela de Geração dos Arquivos – DFC\-PR considerando que o campo mês do arquivo de layout para o meio magnético será considerado 00\.

OS1495

__RN49__

__\[ALTERADO CH1432\_2013__

__Registro Tipo 1__

__Campo Tipo do Responsável__

Gravar o valor fixo = F C\.

OS1495

CH1432\_2013

__RN50__

__\[ALTERADO CH12999\_2012\]__

__Registro Tipo 1__

__Campo Número do Responsável__

Gravar o CRC CPF do cadastro do contabilista responsável pelas informações do módulo Parâmetros 🡪 Requisitos Legais 🡪 Responsável por Informações, selecionado no campo “Contabilista” na tela de Geração dos Registros – DFC\-PR\.

OS1495

CH12999\_2012

__RN51__

__Registro Tipo 1__

__Campo Modelo da DFC__

Gravar valor fixo para os arquivos da DFC = 8 e para a GI = branco\.

__\[ALTERADA – CH449\-A\_2015\]__

__Tratamento:__

Quando o campo “Ano base” informada na tela de Geração dos Arquivos – DFC\-PR for igual a 2014, desconsiderar a geração da GI\.

OS1495

CH449\-A\_2015

__RN52__

__Registro Tipo 1__

__Campo Não utilizado__

Gravar espaço em branco\.

OS1495

__RN53__

__Registro Tipo 1__

__Campo Quantidade Linhas__

Gravar a quantidade de linhas de registros tipo 2 no arquivo gerado\.

OS1495

__RN54__

__Registro Tipo 2__

__Campo Tipo de Registro__

Gravar valor fixo = 2\.

OS1495

__RN55__

__Registro Tipo 2__

__Campo Número da Linha__

Gravar o número da linha\.

OS1495

__RN56__

__Registro Tipo 2__

__Campo Valor da Linha__

Gravar o valor da somatória dos campos \(Valor Contábil, Base de Cálculo, Isentas e Outras\)\.

OS1495

__RN57__

__Quadro 17__

O sistema deve fazer a somatória do Valor Contábil, Base de Cálculo, Isentas e Outras dos CFOP’s, conforme “Tabela dos CFOP’s x Linhas” \(verificar RN00 até RN21\)\.

\[__Alteração __\- CH122226\]

Atualmente o sistema está truncando os centavos para depois realizar a soma dos CFOPS\. Alterar este tratamento para que os centavos sejam truncados após as somas dos CFOPs\.

Gravar os respectivos valores no arquivo magnético Registro Tipo 2 – Valores dos Campos:

Linhas de número 801 a 823 → Valor Contábil

Linhas de número 826 a 847 → Base de Cálculo

Linhas de número 851 a 872 → Isentas 

Linhas de número 876 a 897 → Outras

O sistema deve gravar o valor do estoque inicial, da linha 823, considerando apenas os produtos para venda, mercadorias para revenda, matérias primas, materiais intermediários ou secundários, e embalagens\. Não se incluem nos estoques materiais de uso e consumo do estabelecimento e bens do ativo imobilizado, assim como os pertencentes a terceiros, recebidos para industrialização, facção, consignação, depósito, etc\. Os valores declarados deverão coincidir com os registrados no livro Registro de Inventário e inscritos no balanço geral da empresa\.

O sistema faz a somatória dos saldos finais de inventário, da Safx52 e 62, quando os grupos de contagem forem iguais aos códigos 1 e 2\.

OS1495

CH122226

__RN58__

__Quadro 18__

O sistema deve fazer a somatória do Valor Contábil, Base de Cálculo, Isentas e Outras dos CFOP’s, conforme “Tabela dos CFOPs x Linhas \(verificar RN22 até RN41\)\.

Gravar os respectivos valores no arquivo magnético, Registro Tipo 2 – Valores dos Campos:

Linhas de número 901 a 824 → Valor Contábil

Linhas de número 926 a 945 → Base de Cálculo

Linhas de número 951 a 970 → Isentas

Linhas de número 976 a 995 → Outras\. 

O sistema deve gravar o valor do estoque Final, da linha 921, considerando apenas os produtos para venda, mercadorias para revenda, matérias primas, materiais intermediários ou secundários, e embalagens\. Não se incluem nos estoques materiais de uso e consumo do estabelecimento e bens do ativo imobilizado, assim como os pertencentes  a terceiros, recebidos para industrialização, facção, consignação, depósito, etc\. Os valores declarados deverão coincidir com os registrados no livro Registro de Inventário e inscritos no balanço geral da empresa\.

O sistema faz a somatória dos saldos finais de inventário, da Safx52 e 62, quando os grupos de contagem forem iguais aos códigos 1 e 2\.

OS1495

__RN59__

__Quadro 19__

O sistema deve gravar o valor contábil digitado no campo “Valor”, no menu Parâmetros – Quadro 19 \-  Valor a Excluir \- Entrada e gravar no arquivo magnético Registro Tipo 2 – Valores dos Campos, na linha 671 no período especificado\. Disponibilizar uma ferramenta para consulta dos valores digitados, selecionando os campos “Ano” e “Estabelecimento”, conforme Tela  demonstrativa\.

O sistema deve fazer a somatória do valor contábil dos CFOPs 1\.414, 2\.414, 1\.415, 2\.415, 1\.904, 2\.904 e gravar na linha 672\.

OS1495

__RN60__

__Quadro 20__

O sistema deve fazer a somatória do valor do ICMS retido por substituição tributária das operações interestaduais e gravar no arquivo magnético Registro Tipo 2 – Valores dos Campos, na linha 681\.

O sistema deve fazer a somatória do valor contábil dos CFOPs 5\.414, 6\.414, 5\.415, 6\.415, 5\.904, 6\.904 e gravar na linha 682\.

OS1495

__RN61__

__\[ALTERADA OS3111\-F\]__

__Quadro 22__

O sistema deve fazer a somatória do valor contábil dos CFOP’s  parametrizados e gravar no arquivo magnético Registro Tipo 2 – Valores dos Campos\. Gravar o código do município no campo linha\.

Para a DFC é convencionado que os valores do Quadro 22 \(municípios\) ocupam os 4 espaços do campo Número da Linha\. Já os demais números de linha que não pertencem ao Quadro 22, devem ser alinhados à esquerda, ocupando 3 primeiros espaços do campo, com o quarto e último = 0 \(zero\)\.

Quando tiver movimentação de Utilities, buscar as notas fiscais de saída nas tabelas safx42/safx43\.

Não considerar no cálculo as notas fiscais da safx07 geradas pelo mapa resumo de ICMS\.

No cálculo do valor contábil, quando o movimento for gerado a partir das utilities, considerar valor contábil deduzindo o valor dos descontos \(campo 19/safx43 – campo 18/safx42\)\.

__\[ALTERADA – CH81\_2012\]__

Na geração, o sistema deve passar a recuperar os dados informados no campo 182 \- COD\_MUNICIPIO\_ORIG \(SAFX07\) e não mais do campo 42 \- COD\_MUNIC\_COLETA \(SAFX51\), devendo obedecer o filtro abaixo:

\- Campo 03 \- MOVTO\_E\_S \(SAFX07\) = ‘S’;

\- Campo 04 \- NORM\_DEV = ‘1’;

\- Campo 11 \- DATA\_EMISSAO \(SAFX07\) deve estar pertinente ao período de geração da obrigação\.

__Correção do chamado 81\-A \(2012\):__

Na totalização dos valores do Quadro 22, a recuperação dos documentos de transportes da SAFX07 *\(documentos com código de classificação = 4\), *deve considerar também os documentos sem itens de frete na SAFX51\.

__\[ALTERADA – CH5302\]__

__Tratamento para documentos de transportes, classificação igual a “4”:__

De acordo com as especificações anteriores, o valor contábil para documentos fiscais de transporte é recuperado de acordo com o valor total do documento fiscal da SAFX07 \(havendo ou não item de frete\)\. Não há recuperação pela SAFX08 por se tratar de item de frete\.

__OS1495__

__OS3111\-F CH81\_2012__

__CH81\-A\_2012__

__CH5302\_2014__

- COM ou SEM item de frete, recuperar VLR\_TOT\_NOTA da DWT\_DOCTO\_FISCAL \(equalização do campo 23\- Valor Total do Documento Fiscal da SAFX07\) armazenando no campo VLR\_CONTABIL da view EST\_RES\_TRANSP\_MUNIC\_V, em que esta será utilizada na leitura do package DFCPR\_FPROC;

__RN62__

__\[ALTERADA OS3348\]__

Gravação do Campo Município \(campo 02 – Registro 2\):

Quando parâmetro “__Considerar Município do Ponto de Consumo__” selecionado:

   Totalizar o movimento de utilities \(safx42/43\) do período, buscando por município do ponto de consumo \(campo 76/safx42\), de acordo com os CFOP’s parametrizados em: DFC\-PR → Parâmetros → Quadro 22 → Por CFOP ou DFC\-PR → Parâmetros → Quadro 22 → Por CFOP/Natureza de Operação\.

Olhar apenas uma das parametrizações: Se o usuário estiver utilizando o parâmetro por CFOP/Natureza, não considerar a parametrização por CFOP \(e vice\-versa\)\.

   De acordo com este município, verificar correspondência na tabela “Municípios IBGE x Município das UF’s” \(TACES24\), e gravar o município destino\.

Quando parâmetro “__Considerar Município do Ponto de Consumo__” não selecionado:

   Totalizar o movimento de notas fiscais do período, buscando pela município da pessoa fis/jur da safx07 na safx04, de acordo com os CFOP’s parametrizados em: DFC\-PR → Parâmetros → Quadro 22 → Por CFOP ou DFC\-PR → Parâmetros → Quadro 22 → Por CFOP/Natureza de Operação\.

Olhar apenas uma das parametrizações: Se o usuário estiver utilizando o parâmetro por CFOP/Natureza, não considerar a parametrização por CFOP \(e vice\-versa\)\.

   De acordo com este município, verificar correspondência na tabela “Municípios IBGE x Município das UF’s” \(TACES24\), e gravar o município destino\.

OS3111\-F / OS3348

__RN63__

__Quadro 03 – GI__

Gravar a somatória dos valores das operações e prestações de serviços interestaduais, nas operações de Entrada, por Unidade da Federação, das colunas Valor Contábil, Base de Cálculo, Outras e ICMS cobrado por Substituição Tributária:  Petróleo/Energia Elétrica e Outros Produtos\.

No caso da GI, o número da Linha é formado pelo Quadro\+Linha\+Coluna\. Assim sendo, para informar o Valor Contábil das Entradas para Acre, o número da linha será 3011 e para informar o Valor da Base de Cálculo das Entradas, o número da linha será 3012\. Entrada de Outros Produtos, vindos de Santa Catarina, será 3255 e ICMS cobrado por Substituição Tributária nas Saídas para Pernambuco será 5186 e assim por diante\.

OS1495

__RN64__

__Quadro 05 \- GI__

Gravar a somatória dos valores das operações e prestações de serviços interestaduais, nas operações de Saída, por Unidade da Federação, das colunas Valor Contábil – Não Contribuinte, Valor Contábil – Contribuinte,  Base de Cálculo – Não Contribuinte, Base de Cálculo – Contribuinte,  Outras e ICMS cobrado por Substituição Tributária\.

No caso da GI, o número da Linha é formado pelo Quadro\+Linha\+Coluna\. Assim sendo, para informar o Valor Contábil das Entradas para Acre, o número da linha será 3011 e para informar o Valor da Base de Cálculo das Entradas, o número da linha será 3012\. Entrada de Outros Produtos, vindos de Santa Catarina, será 3255 e ICMS cobrado por Substituição Tributária nas Saídas para Pernambuco será 5186 e assim por diante\.

OS1495

__RN65__

__Parâmetro “Geração centralizada por Inscrição Estadual Única”__

A partir da criação deste parâmetro, a regra para demonstrar os estabelecimentos no quadro “Estabelecimentos” passa a ser:

Se parâmetro __Geração centralizada por Inscrição Estadual Única__ *desmarcado*:

     Mostrar todos os Estabelecimentos da Empresa\.

Se parâmetro __Geração centralizada por Inscrição Estadual Única__ *marcado*:

     Mostrar apenas os Estabelecimentos parametrizados como *centralizadores* na parametrização dos

     Estabelecimentos com Inscrição Estadual Única do módulo de Controle das Obrigações Estaduais;

A geração do arquivo foi alterada para considerar o novo parâmetro incluído na tela\. O tratamento da inscrição estadual única será o mesmo já existente no Mastersaf para a emissão dos livros fiscais, da seguinte forma:

- Os registros de identificação do contribuinte devem ser gerados com os dados do estabelecimento centralizador;
- Ao utilizar qualquer parametrização cujo cadastro seja por estabelecimento  \(CFOP’s, Produtos etc \.\.\.\), deve\-se utilizar a parametrização feita em nome do estabelecimento centralizador;
- Além dos documentos fiscais do estabelecimento da geração, que é o estabelecimento centralizador, deverão ser recuperados também os documentos dos estabelecimentos centralizados\. Assim, a regra é considerar os documentos fiscais de todos os estabelecimentos envolvidos na centralização, lembrando que a parametrização dos estabelecimentos, Centralizador x Centralizados fica no módulo Controle das Obrigações Estaduais, no item “Obrigações 🡪 Empresas/Estabelecimentos com Inscrição Estadual Única”; 

OS3111\-F

__RN66__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


# RNG-D_Segmento_Transportes_V7

- **Fonte:** RNG-D_Segmento_Transportes_V7.docx
- **Modificado:** 2025-11-21
- **Tamanho:** 51 KB

---

# bREGISTRO D200 \- Resumo da Escrituração Diária – Prestação de Serviços de Transporte 

# Nota Fiscal de Serviço de Transporte \(Código 07\)

# Conhecimentos de Transporte de Cargas \(Código 08\), 

# Conhecimentos de Transporte de Cargas \(Código 08B\), 

# Aquaviário de Cargas \(Código 09\), Aéreo \(Código 10\),  

# Ferroviário de Cargas \(Código 11\),

# Multimodal de Cargas \(Código 26\),

# Nota Fiscal de Transporte Ferroviário de Carga \(Código 27\)

# Conhecimento de Transporte Eletrônico – CT\-e \(Código 57\),

__Bilhete de Passagem Eletrônico \- BP\-e \(Código 63\) e__

# Conhecimento de Transporte Eletrônico p/Outros Serviços – Cte OS \(Código 67\)\. 

__RNG\-D200__

Este registro tem por objetivo informar agrupamento da sumarização diária das notas \(SAFX07/SAFX08\), com base das seguintes informações:

\- Modelo de Documento \(campo 13 da SAFX07\) 

\- Série \(campo 09 da SAFX07\)

\- Sub Serie \(campo 10 da SAFX07\)

\- Data de Emissão \(campo 11 da SAFX07\)

\- CFOP \(campo 14 da SAFX07\) 

__Regra de recuperação das notas: __

Movimento Entrada/Saída: \(campo 03 da SAFX07\)

		Igual a “9 – Documento de Saída”

	

	Data de Emissão: \(campo 11 da SAFX07\)

		Entre a Data Inicial e Data Final de geração do arquivo

	Classificação: \(campo “12 – Classificação do Documento” da SAFX07\)

		Igual a “1 – Mercadoria”, “4 – Conhecimento de Frete”, “5 – Redespacho de Fretes”, “6 – Subcontratação de Fretes” e Se o parâmetro __Notas Fiscais de Mercadoria Não Escrituradas__ estiver marcado em Dados Iniciais, as notas fiscais de saída com Classificação ‘7 – Notas Fiscais de Mercadoria não Escrituradas’, \(campo 12 da safx07\) e que possuam CST´s de PIS e COFINS \(SAFX07 ou 08\), deverão ser considerados na EFD\-Contribuições\.

	Modelo: \(campo “13 – Modelo de Documento” da SAFX07\)

		Igual a ‘’07’’, ‘’08’’, ‘’08B’’, ‘’10’’, ‘’11’, ‘’26’’, ‘’27’’, ‘’57’’, __“63”__ ou “67”

Crédito/Contribuição Extemporânea: \(campo novo da SAFX08\)

Item não extemporâneo \(campo novo = “N”\)

*Alteração MFS12767: Inclusão do modelo 67\. Conforme orientação do GP, este modelo de documento fiscal foi instituído pelo Ajuste SINIEF nº 10, de 2016, e deve ser utilizado parar os fatos geradores a partir de 01 de julho de 2017\.*

*Alteração MFS\-19270: Inclusão do modelo 63\. Conforme orientação do GP de vrs 1\.26 sem publicação de ato legal, apenas orientação da Receita Federal em 21/06/2018 de acordo com a disponibilização do PVA 3\.00\.*

*Alteração CH9851\_2018*

*MFS\- 22745: Inclusão das Classificações de Documentos 5 e 6\.*

\[OS4316\-A\] __Tratamento para Geração de SCPs__

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

\[OS4316\-C\] Observar a parametrização de "Dados Iniciais" \(menu: Parâmetros >> Dados Iniciais\) para geração ou não do registro\. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP\. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo \(Código da SCP não informada\) como valido também para a SCP para o qual o arquivo está sendo gerado\.

Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido\.

__Obs1\.:__ Se o documento fiscal possuir item, mas o campo “Crédito/Contribuição Extemporânea” não estiver preenchido, considerar o conteúdo desse campo informado na capa do documento fiscal \(SAFX07\)\.

__Obs2\.:__ Para as notas fiscais que não possuem item mercadoria, as verificações devem ser feitas com base no CST, CFOP e Crédito/Contribuição Extemporânea de acordo com as informações da capa do documento\.

\(\*\) Alteração feita no chamado CH68490\-DHL devido à situação especial do cliente, que emite CTRC modelo 08 com dois valores de BC e diferentes alíquotas, e para isso, carrega o documento com classificação fiscal = ‘1’ para poder carregar os valores diferenciados na SAFX08 \(ver doc CH68490 com todo histórico da situação\);

__RND200\-03__

Campo COD\_SIT:

Para o preenchimento deste campo deverão ser verificados alguns campos da SAFX07, conforme segue:

Se for nota eletrônica, verificar:

     se a nota foi denegada        🡪 gravar “04”

     se a nota foi  ou inutilizada 🡪 gravar “05”

Se for nota cancelada,

      gravar “02”

Se for nota complementar:

      gravar “06”

Se nota tem Ato Normativo, Regime Especial etc\.\.\.

      gravar “08”

Se a nota não atende a nenhuma das opções anteriores:

      gravar “00”

__Importante:__ 

Os testes devem ser executados exatamente nesta prioridade\. Assim, o teste deve ser encerrado na primeira regra atendida pela nota, e sempre que isto *não ocorrer*, será gravado o conteúdo “00”\.

A lógica seria a seguinte:

__Se__ nota é eletrônica e foi  \(denegada ou inutilizada\)

        __Se__ nota é denegada

              gravar “04”

        __Senão__*  \(é inutilizada\)*

              gravar “05”

# Senão

        __Se__ nota é cancelada

              gravar “02”

              __Senão__

                    __Se__ nota é complementar

                         gravar “06”

                    __Senão__

                         __Se__ nota tem Ato Normativo, Regime Especial etc

                              gravar “08”

                         __Senão__

                             gravar “00”;

  

__Campos da SAFX07 para verificação das regras:__

Nota cancelada 🡪 campo “30\-Situação da nota” =  “S”;

Nota complementar 🡪 campo “125\-Situação Especial” = “5”;

*\(Alteração MFS12767: Inclusão do modelo 67\)*

*\(Alteração MFS\-19270: Inclusão do modelo 63\)*

Nota Eletrônica 🡪 campo “13\-Modelo de Documento” = “57”, __“63”__ __ou “67”__;

Nota Eletrônica denegada 🡪 campo “13\-Modelo de Documento” = \(“57”, __“63”__ __ou “67”__\) e o campo “231\-Nfe Denegada/Inutilizada” = “1” \(denegada\);

Nota Eletrônica inutilizada 🡪 campo “13\-Modelo de Documento” = \(“57”, __“63”__ __ou “67”__\) e o campo “231\-Nfe Denegada/Inutilizada” = “2” \(inutilizada\);

Nota com Ato Normativo, Regime Especial etc 🡪 o campo “232\-NF Baseada em Regime Especial ou Norma Específica” será = “S”\.

__RND200\-06__

Campo NUM\_DOC\_INI:

Gravar nesse campo a menor número da nota fiscal dos registros da SAFX07 encontrados para aquele modelo de acordo com a RNG\-D200\.

__RND200\-07__

Campo NUM\_DOC\_FIN:

Gravar nesse campo a maior número da nota fiscal dos registros da SAFX07 encontrados para aquele modelo de acordo com a RNG\-D200

__RND200\-08__

Campo COD\_CFO:

Para as notas *sem* itens 🡪 o campo deve ser preenchido com o CFOP da SAFX07 \(campo 14\- COD\_CFO\);

Notas com item 🡪 o campo deve ser preenchido com o CFOP da SAFX08 \(campo 22\- COD\_CFO\)\.

__RND200\-10__

Campo: VL\_DOC

Este campo deve ser preenchido com o valor da nota mais o desconto, ou seja:

Notas sem item 🡪 campo 23 \(Valor Total\)  \+  campo 28  \(Desconto\) da SAFX07

Notas com item 🡪 total = campo 64 \(Valor Contábil\)  \+  campo 29 \(Desconto\) dos itens da SAFX08

Para notas canceladas este campo não deverá ser informado\.

__RND200\-11__

Campo VL\_DESC:

Para as notas *sem* itens 🡪 o campo deve ser preenchido com o valor do desconto da SAFX07 \(campo 28\-Valor Descontos\);

Para as notas *com *itens 🡪 neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria e serviço da nota, considerando o campo “29\-Valor do Desconto” da SAFX08\.

Para notas canceladas este campo não deverá ser informado\.

	

# REGISTRO D201 – Totalização do Resumo Diário – PIS/PASEP 

__RNG\-D201__

Esse registro deve ser gerado o agrupamento da totalização dos itens dos documentos fiscais gerados no registro D200 com base nas seguintes informações:

\- CST PIS 

\- Alíquota PIS

\- Código da Conta

__Obs\. 1:__ Os itens dos documentos fiscais cancelados, os itens que não passaram pela regra de geração do registro D200 e os itens que não possuírem informação de CST PIS/Cofins, não devem ser considerados no agrupamento\.

__Obs\. 2:__ Para os documentos que não possuírem item, considerar a informação destacada na capa \(SAFX07\)\.

__RND201\-02__

Campo CST\_PIS:

Notas sem item 🡪 campo Código da Situação Tributária PIS da SAFX07

Notas com item 🡪 campo 175 \(Código da Situação Tributária PIS\) da SAFX08\.

__RND201\-03__

Campo VL\_ITEM:

Notas sem item 🡪 campo 23 \- Valor Total da SAFX07

Notas com item 🡪 somatório do campo 64 \(Valor Contábil dos itens\) da SAFX08\.

__RND201\-04__

Campo VL\_BC\_PIS:

Notas sem item 🡪 campo 102\- Valor da Base de Cálculo PIS da SAFX07

Notas com item 🡪 somatório do campo 86 – Valor da Base de Cálculo PIS da SAFX08\.

__RND201\-05__

Campo ALIQ\_PIS:

Notas sem item 🡪 campo 164\- Valor da Alíquota PIS da SAFX07

Notas com item 🡪 somatório do campo 129 – Valor da Alíquota PIS da SAFX08\.

__RND201\-06__

Campo VL\_PIS:

Notas sem item 🡪 campo 103\- Valor do PIS da SAFX07

Notas com item 🡪 somatório do campo 87 – Valor do PIS da SAFX08\.

# REGISTRO D205 – Totalização do Resumo Diário – COFINS 

__RNG\-D205__

Esse registro deve ser gerado o agrupamento da totalização dos itens dos documentos fiscais gerados no registro D200 com base nas seguintes informações:

\- CST PIS 

\- Alíquota PIS

\- Código da Conta

__Obs\. 1:__ Os itens dos documentos fiscais cancelados, os itens que não passaram pela regra de geração do registro D200 e os itens que não possuírem informação de CST PIS/Cofins, não devem ser considerados no agrupamento\.

__Obs\. 2:__ Para os documentos que não possuírem item, considerar a informação destacada na capa \(SAFX07\)\.

__RND205\-02__

Campo CST\_COFINS:

Notas sem item 🡪 campo Código da Situação Tributária COFINS da SAFX07

Notas com item 🡪 campo 178 \(Código da Situação Tributária COFINS\) da SAFX08\.

__RND205\-03__

Campo VL\_ITEM:

Notas sem item 🡪 campo 23 \- Valor Total da SAFX07

Notas com item 🡪 somatório do campo 64 \(Valor Contábil dos itens\) da SAFX08\.

__RND205\-04__

Campo VL\_BC\_COFINS:

Notas sem item 🡪 campo 104\- Valor da Base de Cálculo COFINS da SAFX07

Notas com item 🡪 somatório do campo 88 – Valor da Base de Cálculo COFINS da SAFX08\.

__RND205\-05__

Campo ALIQ\_COFINS:

Notas sem item 🡪 campo 130\- Valor da Alíquota COFINS da SAFX07

Notas com item 🡪 somatório do campo 50 – Valor da Alíquota COFINS da SAFX08\.

__RND205\-06__

Campo VL\_COFINS:

Notas sem item 🡪 campo 105\- Valor da COFINS da SAFX07

Notas com item 🡪 somatório do campo 89 – Valor da COFINS da SAFX08\.

__Registro D209 – Processo Referenciado__

__RNG\-D209__

Nesse registro devem ser gravados os registros da SAFX114 relacionados ao documento gerado no registro D200, que atendam aos critérios abaixo:

Vinculação: \(campo ‘’15 – Vinculação da SAFX112\)

             Igual a ‘’2 – EFD PIS/COFINS

Origem do Processo: \(campo “14 – Origem do Processo” da SAFX114\)

	Igual a “1 – Justiça Federal”, “3 – Secex/RFB” ou “9 – Outros”

 

# REGISTRO D300 – Resumo da Escrituração Diária – 

# Bilhetes Consolidados de Passagem Rodoviário \(Código 13\), 

# Passagem Aquaviário \(Código 14\), 

# Passagem e Nota de Bagagem \(Código 15\), 

# Passagem Ferroviário \(Código 16\) e Resumo de Movimento Diário \(Código 18\)\.

__RNG\-D300__

O registro D300 é um agrupamento diário dos bilhetes de passagem armazenados na SAFX07 que atendam os seguintes critérios:

Movimento Entrada/Saída: \(campo 03 da SAFX07\)

		Igual a “9 – Documento de Saída”

	

	Data de Emissão: \(campo 11 da SAFX07\)

		Entre a Data Inicial e Data Final de geração do arquivo

	Classificação: \(campo “12 – Classificação do Documento” da SAFX07\)

		Igual a “1” e Se o parâmetro __Notas Fiscais de Mercadoria Não Escrituradas__ estiver marcado em Dados Iniciais, as notas fiscais de saída com Classificação ‘7 – Notas Fiscais de Mercadoria não Escrituradas’, \(campo 12 da safx07\) e que possuam CST´s de PIS e COFINS \(SAFX07 ou 08\), deverão ser considerados na EFD\-Contribuições\.

	Modelo: \(campo “13 – Modelo de Documento” da SAFX07\)

		Igual a ‘13’’, ‘‘14’’, ‘’15’’, ‘’16’’ ou ”18” 

	Situação: \(campo “30 – Situação da Nota” da SAFX07\)

		Somente documentos não cancelados \(situação = “N’’\)

	Crédito/Contribuição Extemporânea: \(campo novo da SAFX08\)

	Item não extemporâneo \(campo novo = “N”\)

__Obs\. 1:__ Se o documento fiscal possuir item, mas o campo “Crédito/Contribuição Extemporânea” não estiver preenchido, considerar o conteúdo desse campo informado na capa do documento fiscal \(SAFX07\)\.

__Obs\. 2:__ Os itens dos documentos fiscais cancelados, os itens que não passaram pela regra de geração do registro D300 e os itens que não possuírem informação de CST PIS/Cofins, não devem ser considerados no agrupamento\.

__Obs\. 3:__ Para os documentos que não possuírem item, considerar a informação destacada na capa \(SAFX07\)\.

Agrupamento 1 🡪 è o agrupamento diário dos bilhetes em ordem crescente atendido na condição 1 descrita neste documento, a quebra do registro ocorrerá cada vez que diferenciar um ítem do agrupamento\.

__AGRUPAMENTO 1__

Data de Emissão;

Modelo de Documento;

Série do Documento Fiscal;

Subsérie do Documento Fiscal;

Código Fiscal;

CST PIS;

CST COFINS;

Alíquota do PIS;

Alíquota da COFINS;

Conta Contábil\.

A identificação dos códigos para preenchimento do campo 02 do registro D300 deve ser feita pelo campo “__13 – Modelo de Documento__” da SAFX07\.

__Descrição do Campo:__

__Nº do Campo:__

__Nome do Campo no MasterSAF:__

__Nome do Campo no Registro D300:__

Data de Emissão

11

DATA\_EMISSAO

08\-DT\_REF

Modelo de Documento

13

COD\_MODELO

COD\_MOD

Classificação do Documento Fiscal

12

COD\_CLASS\_DOC\_FIS

Movimento Entrada/Saída

3

MOVTO\_E\_S

Série do Documento Fiscal

09

SERIE\_DOCFIS

SER

Subsérie do Documento Fiscal

10

SUB\_SERIE\_DOCFIS

SUB

CFOP

14

COD\_CFO

CFOP

CST PIS

COD\_SITUACAO\_PIS

CST\_PIS

CST COFINS

COD\_SITUACAO\_COFINS

CST COFINS

Alíquota  PIS

164

VLR\_ALIQ\_PIS

ALIQ\_PIS

Alíquota COFINS

165

VLR\_ALIQ\_COFINS

ALIQ\_COFINS

Conta Contábil

33

COD\_CONTA

COD\_CTA

\[OS4316\-A\] __Tratamento para Geração de SCPs__

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

\[OS4316\-C\] Observar a parametrização de "Dados Iniciais" \(menu: Parâmetros >> Dados Iniciais\) para geração ou não do registro\. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP\. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo \(Código da SCP não informada\) como valido também para a SCP para o qual o arquivo está sendo gerado\.

Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido\.

__RND300\-02__

__Campo: COD\_MOD__:

De acordo com o agrupamento 1 gravar o conteúdo do campo “modelo de documento” \(campo 13 da SAFX07\) = 13, 14, 15, 16 ou 18

REGISTRO ANALÍTICO DOS BILHETES CONSOLIDADOS DE:

BILHETES DE PASSAGEM RODOVIÁRIO \(CÓDIGO 13\),

BILHETES DE PASSAGEM AQUAVIÁRIO \(CÓDIGO 14\), 

BILHETES DE  PASSAGEM E NOTA DE BAGAGEM \(CÓDIGO 15\) E

BILHETES DE PASSAGEM FERROVIÁRIO  \(CÓDIGO 16\)\.

RESUMO DE MOVIMENTO DIÁRIO \(CÓDIGO 18\)\.

__RND300\-03__

__Campo: SER__

De acordo com o agrupamento 1 gravar o conteúdo do campo “série” \(campo: 09/SAFX07\)\.

__RND300\-04__

__Campo: SUB__

De acordo com o agrupamento 1 gravar o conteúdo do campo “sub\-série” \(campo: 10/SAFX07\)\.

__RND300\-05__

__Campo: NUM\_DOC\_INI__

De acordo com o __agrupamento 1__ gravar neste campo o número do primeiro bilhete de passagem emitido no dia independente de ser cancelado ou não \(campo: 08/SAFX07\)\. 

__RND300\-06__

__Campo: NUM\_DOC\_FIN__

De acordo com o __agrupamento 1__ gravar neste campo o número do último bilhete de passagem emitido no dia independente de ser cancelado ou não \(campo: 08/SAFX07\)\.

__RND300\-07__

__Campo: CFOP__

De acordo com o agrupamento 1 gravar neste campo o conteúdo do campo “Código Fiscal” \(campo: 14/SAFX07\)\.

__RND300\-08__

__Campo: DT\_REF__

De acordo com o agrupamento 1 gravar neste o conteúdo do campo “Data de Emissão” \(campo: 11/SAFX07\)\.

__RND300\-09__

__Campo VL\_DOC:__

De acordo com o agrupamento 1 gravar neste campo o conteúdo do campo “Valor Total da Nota” \(campo: 23/SAFX07\)\.

__RND300\-10__

__Campo VL\_DESC:__

De acordo com o agrupamento 1 gravar neste campo o conteúdo do campo “Valor Descontos” \(campo: 28/SAFX07\)\.

__RND300\-11__

__Campo CST\_PIS:__

De acordo com o agrupamento 1 gravar neste campo o conteúdo do campo “Código da Situação Tributária PIS” \(campo novo/SAFX07\)\.

__RND300\-12__

__Campo VL\_BC\_PIS:__

De acordo com o agrupamento 1 gravar neste campo o conteúdo do campo “Valor da Base de Cálculo PIS” \(campo 102/SAFX07\)\.

__RND300\-13__

__Campo ALIQ\_PIS:__

De acordo com o agrupamento 1 gravar neste campo o conteúdo do campo “Valor da Alíquota PIS” \(campo 164/SAFX07\)\.

__RND300\-14__

__Campo VL\_PIS:__

De acordo com o agrupamento 1 gravar neste campo o conteúdo do campo “Valor do PIS” \(campo 103/SAFX07\)\.

__RND300\-15__

__Campo CST\_COFINS:__

De acordo com o agrupamento 1 gravar neste campo o conteúdo do campo “Código da Situação Tributária COFINS” \(campo novo/SAFX07\)\.

__RND300\-16__

__Campo VL\_BC\_COFINS__

De acordo com o agrupamento 1 gravar neste campo o conteúdo do campo “Valor da Base de Cálculo COFINS” \(campo 104/SAFX07\)\.

__RND300\-17__

__Campo ALIQ\_COFINS__

De acordo com o agrupamento 1 gravar neste campo o conteúdo do campo “Valor da Alíquota COFINS” \(campo 164/SAFX07\)\.

__RND300\-18__

__Campo VL\_COFINS__

De acordo com o agrupamento 1 gravar neste campo o conteúdo do campo “Valor da Alíquota COFINS” \(campo 105/SAFX07\)\.

__RND300\-19__

__Campo: COD\_CONTA__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Conta Contábil” \(campo: 33/SAFX07\)\.  

__Registro D309 – Processo Referenciado__

__RNG\-D309__

Nesse registro devem ser gravados os registros da SAFX114 relacionados ao documento gerado no registro D300, que atendam aos critérios abaixo:

Vinculação: \(campo ‘’15 – Vinculação da SAFX112\)

             Igual a ‘’2 – EFD PIS/COFINS

Origem do Processo: \(campo “14 – Origem do Processo” da SAFX114\)

	Igual a “1 – Justiça Federal”, “3 – Secex/RFB” ou “9 – Outros”

 

# Registro D350 – Resumo Diário de Cupom Fiscal Emitido por ECF – \(Códigos 2E, 13, 14, 15 e 16\)   

__RND350__

Este registro deverá ser gerado com a sumarização diária dos bilhetes de passagem comercializados na Redução Z, ou seja, todos os itens vendidos no dia\.

Para o sistema identificar as informações de todos os documentos fiscais da tabela SAFX991, totalizados na redução Z, deve atender aos critérios abaixo:

__Data de Movimento:__ \(campo 06 da SAFX991\)

	Entre a data inicial e final de geração do arquivo\.

__Modelo:__ \(campo 03 da SAFX991\)

	Igual a “2E”, 13, 14, 15 e 16\.

A seleção da chave do registro será:

Empresa;

Estabelecimento;

Modelo Documento;

Nº do Caixa;

Data Movimento\.

CRZ

O sistema deve identificar os cupons fiscais que integram cada redução Z através dos seguintes filtros:

__Passo 1:__ Selecionar na SAFX991 o COO Inicial \(Campo 11\), o COO Final \(Campo 12\), a data de movimento \(campo 06\) e o número do caixa \(campo 04\)\.

__Passo 2: __Selecionar na SAFX993 os cupons com número do caixa \(campo 04\) igual ao número do caixa encontrado no passo 1 e com situação \(campo 10\) igual a “1”\.

__Passo 3:__ Nos cupons encontrados no passo 2, selecionar na SAFX993 os cupons com data de emissão \(campo 06\) igual à data de movimento encontrada no passo 1 e com hora final de emissão \(campo 19\) >= 02:00, __OU__, com data de emissão \(campo 06\) um dia maior que a data de movimento encontrada no passo 1 e com hora final de emissão \(campo 19\) <= 02:00\.

__Obs\.:__ Se o campo Hora Final de Emissão não estiver preenchido, considerar apenas os registros da SAFX993 com data de emissão \(campo 06\) igual à data de movimento encontrada no passo 1\.

__Passo 4:__

Se o COO Inicial da redução Z for __menor__ que o COO Final \(ambos selecionados no passo 1\):

	Nos cupons encontrados no passo 3, selecionar na SAFX993 os cupons que possuírem COO 	\(campo 05\) entre o COO Inicial e o COO Final\.

Se o COO Inicial da redução Z for __maior__ que o COO Final \(ambos selecionados no passo 1\):

	Nos cupons encontrados no passo 3, selecionar na SAFX993 os cupons que possuírem COO 	\(campo 05\) entre o COO Inicial e o COO Final p/ Reinício \(campo 38 da SAFX2087 referente ao 	equipamento ECF em questão\), e também os cupons que possuírem COO \(campo 05\) entre 	“000000” e o COO Final

__Passo 5:__ Dos cupons encontrados no passo 4, selecionar na SAFX994 os registros que possuam a mesma chave \(abaixo\) da SAFX993 e cuja situação do item no cupom \(campo 11\) igual a “1” ou “3

Empresa;

Estabelecimento;

Modelo Documento;

Nº do Caixa;

COO;

 

__Passo 6:__ Deve ser gerado um registro D350 para cada combinação de \(produto/serviço, CST PIS, Alíquota PIS, Alíquota PIS – em reais, Alíquota COFINS, Alíquota COFINS – em reais e Conta Contábil\) presente nos detalhes de cupom fiscal encontrados no passo 5\.

\[OS4316\-A\] __Tratamento para Geração de SCPs__

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

\[OS4316\-C\] Observar a parametrização de "Dados Iniciais" \(menu: Parâmetros >> Dados Iniciais\) para geração ou não do registro\. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP\. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo \(Código da SCP não informada\) como valido também para a SCP para o qual o arquivo está sendo gerado\.

Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido\.

__RND350\-03__

Campo ECF\_MOD:

Neste campo deve gravar o conteúdo do campo 11 – Modelo do ECF da tabela SAFX2087 referente ao número do caixa \(campo 4\) informado na tabela SAFX991\.

__RND350\-04__

Campo ECF\_FAB:

Neste campo deve gravar o conteúdo do campo 07 – Número de série de fabricação do ECF da tabela SAFX2087 referente ao número do caixa \(campo 4\) da tabela SAFX991\.

__RND350\-08__

Campo NUM\_COO\_FIN:

Neste campo deve gravar o conteúdo do campo 07 – COO da tabela SAFX991\.

__\[ALTERADA – OS4835\]__

__ALTERADA – MFS18316\]__

__Tratamento:__

\-	Se o campo estiver preenchido com mais de seis posições permitidas pelo layout, truncar a informação considerando as seis primeiras ultimas posições e emitir a seguinte mensagem no log: “O Número do Contador de Ordem de Operação \(COO\) do Registro D350 excede o tamanho permitido, favor verificar Redução Z ”\.


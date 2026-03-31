# Sped_Fiscal_Regras_Bloco_1

- **Fonte:** Sped_Fiscal_Regras_Bloco_1.docx
- **Modificado:** 2026-03-23
- **Tamanho:** 273 KB

---

<a id="OLE_LINK109"></a>Quadro de Revisões

__                                                Revisões realizadas a partir de 01/01/2020__

__   As revisões anteriores podem ser consultadas no tópico “Histórico das Revisões”__

__Data__

__OS / Chamado__

__Descrição__

__Responsável__

07/01/2020

MFS31423

Inclusão da geração dos registros 1250 e 1255 \(Guia Prático Vrs 3\.0\.3\)

Andréa Rocha

11/02/2020

MFS31407

Atualização versão 1\.13 \(JAN/2020\): Inclusão dos novos campos do registro 1391 \(Produção Diária da Usina\)

Vânia Mattos

12/02/2020

MFS33701

Alteração na geração do campo 05\-COD\_REC do registro 1926, para tratar as regras específicas de algumas UF’s, conforme é feito na geração do COD\_REC do E116\.

Vânia Mattos

13/02/2020

MFS34187

Alteração da regra do registro 1400 SP\-DIPAM31

Andréa Rocha

15/02/2020

MFS33871

Alteração na geração do registro 1400 para o estado de SC\.

Andréa Rocha

05032020

MFS34598

Ajuste na geração do H005 do inventário Motivo “06” \(ver __RNH005__\)

Vânia Mattos

09/03/2020

MFS34479

Ajuste na geração do 1391 – Campo 3 \- QTD\_MOID

Andréa Rocha

21/03/202

MFS\-34707

Ajuste nos campos 19 e 20 do 1391  \(RN1391\-19, RN1391\-20,\)

Ajuste no ampo 02 do 1390 \(RN1390, RN1390\-02\)

Liliane Assaf

11/05/2020

MFS36578

Alteração no registro 1923 p/atendimento ao regime especial RS \(Apuração Assistida – RS\): Não gerar os registros “filhos” \(1923\) referentes ao ajuste \(1921\) dos valores do ICMS Efetivo das NFC\-e \(Mod 65\), caso existam \(ver RN1923\)\. 

Vânia Mattos’

03/06/2020

MFS35568

Alteração na geração do registro 1400, Energia Elétrica, Geração Padrão e Geração Específica por UF para o RS, Código 02\. Para efetuar a dedução do valor do Desconto dos itens de dedução, não será mais utilizada a parametrização Dedução à Por CST x Produto\. 

Vânia Mattos

<a id="_Hlk80273260"></a>22/06/2020

MFS35133

Alteração na geração do registro 1400, estado do Tocantis, geração automática para os códigos TOIPME05 e TOIPMS05\. regra transferida para documento __MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_TO__

Vânia Mattos

25/06/2020

MFS39109

Alteração no registro 1255, nos campos de valores que não possuem informação na tabela\.  \(ver RN1250, RN1255 , RN1255\-3, RN1255\-4, RN1255\-5, RN1255\-6 e RN1255\-7\)

Alessandra Cristina Navatta

23/09/2020

MFS42592

Alterada a geração do H020 p/os estabelecimentos do RS \(RNH020\)

Vânia Mattos

09/11/2020

Sped\_Fiscal\_Regras\_atual\.doc que continha a especificação dos blocos H e 1, foi dividido em dois documentos:

- Sped\_Fiscal\_Regras\_Bloco\_H\.doc

Sped\_Fiscal\_Regras\_Bloco\_1\.doc

Liliane Assaf

03/11/2020

MFS46087

Alteração na geração do registro__ 1400__ Energia Elétrica – Geração __Padrão__\.

A CPFL tem realizado um trabalho junto a TR para definição da geração do 1400 para atendimento ao segmento de Energia Elétrica\.

A última regra definida foi  implementada pela __MFS35568\.__ Mas durante sua homologação, a CPFL identificou que não atenderia a todos os cenários\. A regra foi então redefinida pela CPFL e está sendo implementada na __MFS46087__\.

Liliane Assaf

08/12/2020

MFS45819

Alteração na geração do 1400 – Específica para UF = SP

Tratamento para que registro 1400 com valor negativo não ser gravado no arquivo\.  Preferimos fazer esta alteração apenas para o código SPDIPAM23, objeto do chamado\. Não haveria tempo abil para aplicar esse tratamento nos outros códigos da DIPAM, nem nas demas gerações \(Padrão e Específicas de outras Ufs\)\. Validador rejeita 1400 com valor negativo\.

Liliane Assaf

10/02/2021

MFS59468

Alteração na geração do registro 1400, estado do Pernanbuco, geração automática para o código PEIPMS0\. \(regra transferida para documento __MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_PE__

Aline Melo

05/03/2021

MFS58137

Alteração na geração do registro__ 1400__ Energia Elétrica – Geração __Padrão__\.

A CPFL tem realizado um trabalho junto a TR para definição da geração do 1400 para atendimento ao segmento de Energia Elétrica\.Esta MFS é continuação da MFS46087, incluindo as parametrizações de Produtos c/ Isenção de ICMS e Produtos c/ Desconto\.

Liliane Assaf

10/03/2021

[MFS60170](https://jira.thomsonreuters.com/browse/MFS-60170)

Alteração na geração do registro __1400__ – Geração Específica para UF = MG

Tratamento na geração do registro __1400,  “3\.5 \- __Prestação de Serviço de Transporte Rodoviário” –  que de acordo com a Resolução 5\.369 de 22 de maio de 2020 – Subitem 3\.4\.2\.1, passa a ser informado __mensalmente__\.

Rogério Ohashi

16/03/2021

MFS61931

Ajuste na regra do registro 1400 para UF = PE, para que considerere classificação fiscal igual a ‘3’ e modelos gerados nos registros D300 e D400 do Sped Fiscal

__\(regra transferida para o documento MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_PE\)__

Aline Melo

16/03/2021

MFS60545

Inclusão de tratamento do Campo COD\_INF do Registro 1500 \(__RN1500\-23__\)\.

Rogério Ohashi

22/03/2021

MFS62000 / MFS62415

Registro 1923: alterações referentes a IN\-RE006/19 do Ressarcimento ST RS\.

\- Inclusão dos cupons fiscais do 1923

\- Geração do 1923 para Lançamento de Estorno de Créditos referente às saídas para outras Ufs, isentas ou não tributadas

Liliane Assaf

23/03/2021

MFS61948

Alteração na geração do registro 1400, estado da Bahia, geração automática para os códigos BAE07, BAE13 e BAE14\. \(__regra transferida para o documento MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_BA\)__

Aline Melo

29/03/2021

MFS37872

Alteração na geração do registro 1600, retirar a obrigatoriedade das mensagens de erro, de acordo com a informação do validador\.

Andréa Rocha

31/03/2021

[MFS60170](https://jira.thomsonreuters.com/browse/MFS-60170)

Alteração na geração do registro __1400__ – Geração Específica para UF = MG

Tratamento na geração do registro __1400, item “3\.5 \- __<a id="_Hlk68106826"></a>Prestação de Serviço de Transporte Rodoviário” –  que de acordo com a Resolução 5\.369 de 22 de maio de 2020 – Subitem 3\.4\.2, passa a ser informado __mensalmente__ e gerado diretamente pelo menu Geração > Meio Magnético\. \(__RN1400\-MG\-05a\)__

Rogério Ohashi

01/04/2021

MFS40529

Alteração da regra do 1400 padrão, para não mostrar a mensagem de valor negativo no log de geração

Andréa Rocha

09/04/2021

MFS61950

Alteração na geração do registro 1400, estado da Bahia, geração automática para os códigos BAE05 e BAS05\. \(__regra transferida para o documento MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_BA\)__

Aline Melo

09/04/2021

MFS61951

Alteração na geração do registro 1400, estado da Bahia, geração automática para os códigos BAE06 e BAS06\. \(__regra transferida para o documento MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_BA\)__

Aline Melo

09/04/2021

MFS63191

Registro 1400: Formato padrão ajustes internos

Liliane Assaf

13/04/2021

MFS62608

Inclusão de código, para a geração manual do registro 1400 do Estado do Paraná\. \(__regra transferida para o documento MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_PR\)__

Aline Melo

30/04/2021

MFS64052

Inclusão de código IPM 3\.5, para a geração automática do registro 1400 do Estado do Rio Grande do Norte\.

Aline Melo

20/05/2021

MFS64779

Inclusão do código PEIPMS4, para a geração automática do registro 1400 do Estado de Pernambuco\. Regra transferida para __MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_PE__

Aline Melo

01/06/2021

MFS64253

Inclusão do código IPM 3\.6, na geração manual e ajuste na geração do código 4\.1 para o periodo mensal do registro 1400, para o estado do Rio Grande do Norte\.

Aline Melo

08/06/2021

MFS58410

Alteração do Registro 1400 – Específico por UF, para SP, Código “__SPDIPAM35” __ Inclusão na regra para considerar o Campo MOVTO\_E\_S =“1” e Campo COD\_CLASS\_DOC\_FIS = ‘1’, para possibilitar a geração da operação de nfs de remessa de garantia emitidas por terceiros, conforme solicitação do cliente Yamaha\. Equiparação de regra, alterada na GIA\-SP\.

Rogério Ohashi

14/06/2021

MFS62640

Inclusão do código PRDISTRIBEE01 na geração automática do registro 1400, em atendimento ao cenário de Energia Elétrica, para o estado do Paraná\. \(__regra transferida para o documento MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_PR\)__

Aline Melo

22/06/2021

MFS67283

Correção da regra de geração do Registro 1400 – Padrão, somente por Município quando o parâmetro “Calcular Valores por Produto” não estiver selecionado, \(tratamento para as operações de Transporte e Deduções\)\.

Rogério Ohashi

15/07/2021

MFS45370

Inclusão do codigo “Geracao\_de\_Energia\_Eletrica” na geração do 1400, para Minas Gerais\. Transferencia das regras de MG para o documento “MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_MG\.docx”

Aline Melo

20/07/2021

MFS68839

Alteração do Registro 1400 – Específico por UF, para __MG__, Código 3\.1 \- “Produtos Agropecuários”, alteração na regra para considerar somente o Campo MOVTO\_E\_S =“2”\. 

Rogério Ohashi

20/09/2021

MFS35221

Inclusão dos códigos RJVAF20002 e RJVAF20003 na geração automática do registro 1400, para o estado do Rio de Janeiro\. Transferencia das regras do RJ para o documento “MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_RJ\.docx”

Aline Melo

14/10/2021

MFS72164

Alteração da regra do campo 18\-COD\_ITEM do registro 1391, para ficar igual ao que já estava implementado\. 

Andréa Rocha

15/10/2021

MFS47088

Inclusão de códigos para geração manual e automática do registro 1400, para o estado do Maranhão\.

Aline Melo

26/10/2021

MFS74676

Ato Cotepe 62/2021, novo leiaute EFD115 \(versão 1\.15, Jan/2022\):

\- Alteração no registro 1010 – regra RN1010\-08 campo IND\_CART\.

\- Exclusão do registro 1600, sendo substituído pelo 1601

\- Inclusão do registro 1601

Liliane V\. Assaf

14/01/2022

MFS77290

Alteração na geração dos registros 1390/1391 para estabelecimentos localizados em Alagoas\. Alagoas divulgou sua própria tabela 5\.8, introduzido novos códigos de produto a serem apresentados no registro 1390\.

Liliane V\. Assaf

08/03/2022

MFS81804

Alteração na geração do registro 1923 para incluir os lançamentos de devolução de saída gerado no módulo Ressarcimento RS – IN\-RE048/18\.

Liliane V\. Assaf

01/06/2022

MFS85762

Alteração do Registro 1400 – Específico por UF, para SP, Código “SPDIPAM35”\. Inclusão na regra para considerar outros tipos de notas de entrada, quando o Campo COD\_CLASS\_DOC\_FIS = ‘1’, para passar a considerar as notas de retorno de mercadoria\.

Andréa Rocha

10/06/2022

MFS86203

Inclusão do código IPM 3\.6 na geração automática do registro 1400, para o estado do Rio Grande do Norte\. Transferencia das regras do RN para o documento “MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_RN\.docx”

Aline Melo

05/09/2022

MFS92607

__AC 21/2022, nova versão 1\.16, Jan/2023__

Alteração nas regras de preenchimento dos campos a seguir, para tratar o aumentou de 15 para 60 posições\.

- 03 – NUM\_PROC do registro 1922

Liliane Assaf

05/09/2022

MFS92402

__AC 21/2022, nova versão 1\.16, Jan/2023__

Alteração nas regras de preenchimento dos campos a seguir, para tratar o aumentou de 15 para 60 posições\.

- 06 – NUM\_PROC do registro 1926

Liliane Assaf

11/10/2022

MFS92120

Alteração da regra da geração do registro 1400, código da DIPAM 11, para gerar o registro somente para pessoa física\. Conforme legislação da DIPAM,  o produtor rural tem de ser pessoa física\.

Andréa Rocha

19/10/2022

MFS94497

Inclusão do código 1201 na geração automática do registro 1400, para o estado de Alagoas\. Regras de Alagoas para o documento “MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_RN\.docx”\.

Aline Melo

03/11/2022

MFS95773

Inclusão da utilização do modelo 66 para a geração do registro 1400 – opção padrão, para a geração de energia elétrica\.

Andréa Rocha

04/11/2022

MFS95293

Alteração da geração do campo COD\_PART do registro 1923 para o modelo 65, quando o código de ajuste for = RS001920\.

Andréa Rocha

<a id="_Hlk123672197"></a>03/01/2023

MFS99537

Alteração na geração do 1400 tipo de geração “Padrão” para considerar os documentos fiscais de modelo 62 \(SAFX07\) na totalizar os valores de deduções \(Etapa 2\)\.

Liliane Assaf

29/05/2023

MFS539087

Inclusão da utilização do modelo 59 para a geração do registro 1400 para o código SPDIPAM22\. Esse modelo está sendo incluído para recuperar as mesmas notas já recuperadas pela geração da GIA\-SP\.

Andréa Rocha

29/09/2023

MFS436036

Tratamento das notas de saída de modelo 62 \(NFCom\) na geração do registro 1400\.

Liliane Assaf

08/11/2023

MFS577276

__Versão 1\.17 – Jan/2024__

Registro 1391: geração dos resíduos DDG e WDG produzidos no mesmo dia\.

Liliane Assaf

03/02/2025

MFS710674

Inclusão do modelo 66 na regra do código do registro 1400 – Padrão \- Etapa 2 \- Totalizar os valores de deduções\.

Graciela Soares

11/08/2025

MFS861835

Inclusão do campo 11 no registro 1310 a partir da nova versão de layout 1\.19

Liliane Assaf

08/09/2025

MFS861834

Preenchimento do campo 11 no registro 1310 a partir da nova versão de layout 1\.19 com o campo 07 \- Capacidade \(em litros\) da SAFX2060\.

Liliane Assaf

27/01/2026

MFS1002797

<a id="_Hlk220583023"></a>Alteração da regra de geração do campo 05 do registro 1391, para considerar os movimentos de estorno de acordo com o parâmetro criado\.

Lyene Benvenutti e Andréa Rocha

Table of Contents

[Histórico das Revisões	2](#_Toc75782957)

[Registro 1001 – Abertura do Bloco 1	6](#_Toc75782958)

[Registro 1010 – Obrigatoriedade De Registros Do Bloco 1	6](#_Toc75782959)

[Registro 1100 – Registro de Informações sobre Exportação	7](#_Toc75782960)

[Registro 1105 – Documentos Fiscais de Exportação	9](#_Toc75782961)

[Registro 1110 – Operações de Exportação Indireta de Produtos não	10](#_Toc75782962)

[Industrializados pelo Estabelecimento Emitente	10](#_Toc75782963)

[Registro 1200 – Controle de Créditos Fiscais	12](#_Toc75782964)

[Registro 1210 – Utilização de Créditos Fiscais	12](#_Toc75782965)

[Registro 1250 – Informações consolidadas de saldos de restituição,ressarcimento e complementação do ICMS	12](#_Toc75782966)

[Registro 1300 – Movimentação Diária de Combustíveis	14](#_Toc75782967)

[Registro 1310 – Movimentação Diária de Combustíveis por Tanque	14](#_Toc75782968)

[Registro 1320 – Volume de Vendas	15](#_Toc75782969)

[Registro 1350 \- Bombas	15](#_Toc75782970)

[Registro 1360 – Lacres da Bomba	15](#_Toc75782971)

[Registro 1370 – Bicos da Bomba	15](#_Toc75782972)

[Registro 1390 – CONTROLE DE PRODUÇÃO DE USINA	16](#_Toc75782973)

[Registro 1391 – PRODUÇÃO DIÁRIA DA USINA	17](#_Toc75782974)

[Registro 1400 – Informação sobre Valores Agregados	25](#_Toc75782975)

[Regras da geração do 1400 para o tipo de geração = “Padrão”:	26](#_Toc75782976)

[Regras da geração do 1400 para o tipo de geração = “Específico por UF”,	34](#_Toc75782977)

[e o Estabelecimento é de MG:	34](#_Toc75782978)

[Regras da geração do 1400 para o tipo de geração = “Específico por UF”,	39](#_Toc75782979)

[e o Estabelecimento é de SP:	39](#_Toc75782980)

[Regras da geração do 1400 para o tipo de geração = “Específico por UF”,	57](#_Toc75782981)

[e o Estabelecimento é do ES:	57](#_Toc75782982)

[Regras da geração do 1400 para o tipo de geração = “Específico por UF”,	68](#_Toc75782983)

[e o Estabelecimento é de RN:	68](#_Toc75782984)

[Regras da geração do 1400 para o tipo de geração = “Específico por UF”,	81](#_Toc75782985)

[e o Estabelecimento é do RS:	81](#_Toc75782986)

[Regras da geração do 1400 para o tipo de geração = “Específico por UF”,	87](#_Toc75782987)

[e o Estabelecimento é de BA:	87](#_Toc75782988)

[Regras da geração do 1400 para o tipo de geração = “Específico por UF”,	111](#_Toc75782989)

[e o Estabelecimento é de TO:	111](#_Toc75782990)

[Regras da geração do 1400 para o tipo de geração = “Específico por UF”,	130](#_Toc75782991)

[e o Estabelecimento é de RJ:	130](#_Toc75782992)

[Regras da geração do 1400 para o tipo de geração = “Específico por UF”,	131](#_Toc75782993)

[e o Estabelecimento é de PE:	131](#_Toc75782994)

[Regras da geração do 1400 para o tipo de geração = “Específico por UF”,	134](#_Toc75782995)

[e o Estabelecimento é de SC:	134](#_Toc75782996)

[Regras da geração do 1400 para o tipo de geração = “Específico por UF”,	134](#_Toc75782997)

[e o Estabelecimento é de PR:	134](#_Toc75782998)

[Regras do 1400 – UF: PR foram transferidas para o documento MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_PR	134](#_Toc75782999)

[Registro 1500 – NF/Conta EE \(Código 06\) – Operações Interestaduais	136](#_Toc75783000)

[Registro 1510 – Itens da NF/Conta EE \(Código 06\) – Operações Interestaduais	137](#_Toc75783001)

[Registro 1600 – Total das Operações com Cartão de Crédito e/ou Débito	137](#_Toc75783002)

[Registro 1700 – Documentos Fiscais Utilizados	138](#_Toc75783003)

[Registro 1710 – Documentos Fiscais Cancelados/Inutilizados	139](#_Toc75783004)

[Registro 1800 – DCTA – Demonstrativo de Crédito do ICMS sobre Transporte Aéreo	139](#_Toc75783005)

[Registro 1900 – Indicador de Sub Apuração do ICMS	141](#_Toc75783006)

[Registro 1910 – Período da Sub Apuração do ICMS	141](#_Toc75783007)

[Registro 1920 – Sub Apuração do ICMS	141](#_Toc75783008)

[Registro 1921 – Ajustes da Sub Apuração do ICMS	142](#_Toc75783009)

[Registro 1922 – Informações Adicionais dos Ajustes \(DA e Processos\)	143](#_Toc75783010)

[Registro 1923 – Informações Adicionais dos Ajustes \(Doctos Fiscais\)	143](#_Toc75783011)

[Registro 1925 – Valores Declaratórios	146](#_Toc75783012)

[Registro 1926 – Obrigações a Recolher da Sub Apuração	146](#_Toc75783013)

# <a id="_Toc75782957"></a>Histórico das Revisões

Data

OS / Chamado

Descrição

Responsável

06/11/2009

OS2388\-E14  

Gravação das notas denegadas / inutilizadas nos registros C100 e D100 a partir da nova tabela SAFX130

Vânia Dias Mattos

25/11/2009

CH72944

Alteração na regra de preenchimento do campo 13, registro D100

Vânia Dias Mattos

30/11/2009

OS2931\-A

Geração do novo registro 0500, conforme Ato Cotepe 38/2009

Vânia Dias Mattos

10/12/2009

OS2931\-Cge

Geração dos novos registros 1700, 1710 e 1800

Camila Orlandi

22/12/2009

CH74570

Alterar regra de geração do campo 03 do registro H010

Camila Orlandi

28/12/2009

OS2388\-E18

Geração do novo registro C105

Vânia Dias Mattos

12/02/2010

CH77581

Alteração na geração das Classes de Consumo \(Registros C500, C600 e 1500\)

Camila Orlandi

24/03/2010

CH78835

Alteração na regra de recuperação dos documentos cancelados/inutilizados, para geração do registro 1710

Liliane V\. Assaf

14/03/2010

OS2388\-E20

Alterar regra de geração do campo 24 do registro D500

Luis Pessoto

31/03/2010

OS2931\-E

Atendimento ao PIM registros 1700 e 1710, e alterações no registro 1800

Anderson Lopes

08/04/2010

OS2931\-B5

Geração do novos registros 0300, 0305, 0600 e registros do Bloco G \(AC 38/2009 e alterações feitas no AC 47/2009\) 

Vânia Dias Mattos

08/07/2010

OS2931\-B9

Alterações do Bloco G \(Guia Prático vrs 2\.0\.1 de Maio/2010\) \.

Vânia Dias Mattos

21/07/2010

OS2931\-B11

Alterações Geração Bloco G \(etapa de testes no validador\)

Vânia Dias Mattos

23/07/2010

CH86865

Contemplação do Convênio ICMS 51/00 nos registros C105 e E210

Marcos Roberto de Oliveira

26/07/2010

OS2931\-B2

Alterar tratamento que compõe o Valor de Crédito do ICMS\-ST 

Juliana Garcia

11/08/2010

OS2931\-B7

Tratamento dos Bens Resultantes x Componentes

Vânia Dias Mattos

26/08/2010

OS2388\-E19

Alterações publicadas no Ato Cotepe 47 de Julho/2010\. Incluir o modelo 29 – Água Canalizada no bloco C500, C510 e C590\.

Juliana Garcia

10/09/2010

OS2931\-B12

Geração do Bloco G p/a opção “Geração – PIM” \(YAMAHA\)

Vânia Dias Mattos

22/09/2010

OS2931\-B10

Cálculo dos Créditos Extemporâneos p/ Geração do G126

Vânia Dias Mattos

15/10/2010

OS2931\-B13

Totalização das Aquisições de mesmo Código de Bem;

Ajustes G125 \(campo 10\-VL\_PARC\_PASS\) e G130;

Vânia Dias Mattos

02/11/2010

CH87096\-A

Ajustar campo 05 – Registro C790 para itens de desconto

Camila Orlandi

25/11/2010

OS3169\-DW1

Alteração no critério do Registro C110 devido o novo módulo EFD\-PIS/COFINS utilizar outro tipo de observação\.

Juliana Garcia

03/12/2010

OS2931\-F

Regras p/ geração dos novos registros das Sub Apurações \(1900\);

Alteração de regras do Bloco E devido às Sub Apurações; 

Vânia Dias Mattos

06/12/2010

OS2931\-B16

Alteração na geração do registro G125 \(tipo movimento = “CI”\)

Vânia Dias Mattos

07/12/2010

OS2388\-E19

Alteradas as regras de geração do novo campo MÊS\_REF \(registros E116 e E250\)\.

Vânia Dias Mattos

10/01/2011

OS2388\-Sge

Alteradas as regras de geração dos registros D100, D160, D161 e D162\.

Criadas as regras de geração dos registros D170 e D180

Natália Resino

22/02/2011

CH99933

Alterada a regra de geração do Registro 0305\.

Juliana Garcia

01/03/2011

CH98286

Alteração na regra do Registro 0500 para atendimento do Guia Prático 2\.0\.3

Juliana Garcia

11/03/2011

CH99471

Alteração na regra do campo 07 do Registro G130\. O campo informava a chave de NFE para qualquer tipo de documento fiscal sendo que é somente para documento de emissão própria\.

Juliana Garcia

11/03/2011

CH94166

Alterada a regra do campo 09 do Registro C100\. O campo era preenchido quando a nota eletrônica era de emissão própria, porém no Guia Prático 2\.0\.3 do Sped Fiscal, a regra de validação informa ser facultativo o preenchimento do campo quando for emissão de terceiro\. Será obrigatório para Emissão Própria, e se houver a informação no campo será também preenchido para Emissão de Terceiros\.

Juliana Garcia

21/03/2011

CH99945

Correção na regra do Campo 04  \- Registro C420\. 

Juliana Garcia

29/03/2011

OS3114\-E

Alteradas regras as do Bloco G para o tratamento dos dados do CIAP a partir dos cálculos feitos por Estabelecimento __e__ IE\-PIM\.   

Vânia Dias Mattos

13/04/2011

CH103152

Alterado tamanho do campo 06 “Nome empresarial da entidade” no registro 0000\. De acordo com a nova versão do Guia Prático \(Versão 2\.0\.4\), este campo pode possuir até 100 caracteres\.

Tatiane Lima

12/05/2011

OS2768\-P

Ajustes na geração do C700 e 1500 p/as empresas que apuram o ICMS das NF’s de EE pelo vencimento, ao invés da emissão\.

Vânia Dias Mattos

13/05/2011

CH96507\-A

Novo LOG de erro e tratamento para o registro 0300 quando a conta contábil ultrapassar o tamanho limite de 60 caracteres

Tatiane Lima

17/05/2011

CH103949

Correção na geração do campo 05 \(Código do Município do local de coleta\) do registro D161\.

Tatiane Lima

17/05/2011

CH103949

Correção na geração do campo 08 \(Código do Município do local de entrega\) do registro D161\.

Tatiane Lima

17/05/2011

CH92772

Alteração da geração do registro D100 para notas fiscais conjugadas \(mercadoria e serviço\) de serviço de transporte \(modelo 07\)\.

Tatiane Lima

17/05/2011

OS\-CH107481

Alteração na regra do registro G130 onde quando o tipo de movimento for igual a perda, então não gerar o registro G130

Tatiane Lima

18/05/2011

CH99308\-A

Alteração na mensagem de Log quando não encontrado o livro de apuração ICMS P9,  referente ao código 108\.

Tatiane Lima

20/05/2011

CH104488

Criação de Log de erro para o registro 0305\.

Tatiane Lima

30/05/2011

OS2388\-E22

Alteração da regra do campo 15 do registro E110 para atender nova versão do guia prático\.

Tatiane Lima

30/05/2011

OS2388\-E22

Alteração nas regras de geração do G125 para mostrar as baixas dos Bens “Informativos”, p/ atender nova versão do guia prático\.

Tatiane Lima

13/06/2011

OS3065\-DW

Alteração no preenchimento dos campos 03\-CNPJ e 05\-CNPJ do registro 0100

Vânia Dias Mattos

13/06/2011

OS2388\-E17

Criação da regra de geração dos registros 0400 e C170 referente ao código da natureza de operação quando ultrapassar 3 caracteres\.

Tatiane Lima

16/06/2011

OS3168

Criação da regra de geração dos registros 0305 e 0600 referente ao código do centro de custo quando ultrapassar 28 caracteres\.

Tatiane Lima

22/06/2011

OS3335\-A

Alterações na geração do D697 

Vânia Dias Mattos

28/06/2011

OS3471

Alterações na geração dos registros D590 e D690 \(GP vrs 2\.0\.5\) 

Vânia Dias Mattos

11/07/2011

OS3230

Alteração da regra dos campos NRO\_RE e DT\_RE referente ao registro 1100\.

Tatiane Lima

14/07/2011

CH105713

Criada regra do campo 15 do registro 0000 para quando o tipo de atividade da empresa for comércio\.

Tatiane Lima

11/08/2011

3471\-A

Alterada a regra para IND\_FRT de documentos a partir de Jan/2012 para atendimento do guia prático 2\.0\.5\.

Tatiane Lima

22/08/2011

3217\-A

Alterada a geração dos registros 0200, C170, C425, C470, C495, C510, C610, D510, D610, 1510, para que passem a buscar as informações de código da natureza do serviço e descrição a partir dos novos campos da SAFX2018, quando houver preenchimento\.

Tatiane Lima

02/09/2011

CH112840

Alterada a regra do registro D300 para que seja gerado por Inscrição Estadual única\.

Tatiane Lima

22/09/2011

CH103884

Alterada a regra do registro C495\.

Vanessa W\. Bravo

27/09/2011

OS3227

Alteração no tratamento de notas extemporâneas de SAIDA\.

Tatiane Lima

29/09/2011

CH108997

Altera a regra de geração do Campo 09 do C100 para que verifique o parâmetro “Gerar Chave de acesso NFE para notas fiscais emitidas por terceiros”\.

Tatiane Lima

07/11/2011

CH117570

Alterada a regra do campo 03 \(DESCR\_COMPL\_AJ\) do registro C197 para que sejam consideradas todas descrições complementares\.

Tatiane Lima

10/11/2011

CH106717

Alterada a regra de geração do registro E200 para que não considere a UF do estabelecimento quando não houver operações internas de ICMS\-ST\.

Tatiane Lima

01/12/2011

OS3423

Alteração da tabela de versão de leiaute, nova versão 1\.0\.4 – início da obrigatoriedade 01/01/2012\);

Tatiane Lima

13/12/2011

OS3401\-A

Inscrição Estadual Especial do Paraná para o registro 0015

Tatiane Lima

22/12/2011

CH121480

O objetivo dessa demanda é realizar a correta geração do campo 15 – IND\_ATV do Registro 0000\.

Natália Resino

27/12/2011

OS3516

Atualizações do Ato Cotepe 52 de 29/11/2011 referente aos campos IND\_FRT, IND\_PGTO e obrigatoriedade dos registros D400 e D411 saídas do perfil B\.

Tatiane Lima

04/01/2011

OS3526\-B

Alteração no tratamento de documentos fiscais com situação especial “D – Operação de Compra/Venda para entrega Futura”

Tatiane Lima

12/01/2011

OS3423\-B

Novo campo para o Bloco H005 e inclusão do novo registro H020, conforme alteração legal descrita no Guia Prático 2\.0\.7 para junho/2012\.

Tatiane Lima

16/01/2011

OS3423\-A

Criação dos blocos D195 e D197, conforme alteração legal descrita no Guia Prático 2\.0\.7 para Junho/2012

Tatiane Lima

19/01/2012

CH234\_2012

Alteração no tratamento do campo 07 do registro C945 para UF = ‘BA’

Cynthia Gomes

20/01/2012

OS3547

Atualização legal – Santa Catarina

Vanessa W\. Bravo

23/01/2012

Ch115852

Alteração no tratamento dos campos VL\_ ICMS\_UF e VL\_BC\_ICMS\_UF

Cynthia Gomes

31/01/2012

CH1117\_2012

Correção no tratamento de CT\-e \(Conhecimento de transporte eletrônico\) – D100\.

Tatiane Lima

08/02/2012

OS3543\-A

Alteração no tratamento de concatenação do campo COD\_ITEM \- 0200

Tatiane Lima

15/02/2012

CH3935\_2012

Alteração no tratamento de CT\-e \(Conhecimento de transporte eletrônico\) –D100

Tatiane Lima

06/03/2011

OS3557

Incluído o código de classe de consumo 08 para os documentos de modelo 28 e 06\.

Tatiane Lima

22/03/2011

OS3417

Alterada a regra do registro 1400 para considerar produtos dos itens de documentos de conhecimento de frete\.

Tatiane Lima

13/04/2012

CH8720\-A\_2012

Alterada a regra de geração do registro 0150

Tatiane Lima

26/04/2012

OS3423\-C

Criação dos Registros 1010, 1390 e 1391, conforme alteração legal descrita no Guia Prático 2\.0\.7 para Julho/2012

Tatiane Lima

30/04/2012

OS3598

Alteração no parâmetro de geração da CHV\_NFE do C100 

Vânia Mattos

09/05/2012

OS3352

Alteração na recuperação do Registro E250 para as GNREs automáticas

Juliana Garcia

14/05/2012

CH9664\_2012

Alterada a regra de geração do campo “Chave CTE” para dos documentos de transporte \(D100\) conforme publicado no novo guia prático VRS 2\.0\.8\.

Tatiane Lima

23/05/2012

OS3423\-D

Aumento do campo OBS do registro 1391

Tatiane Lima

01/06/2012

OS3851

Correção dos registros de Telecom \(campos VL\_BC\_ICMS\_UF e VL\_ICMS\_UF\)

Vânia Mattos

06/07/2012

CH11564\_2012

Correção no tratamento no registro D100 para Chave\-Nfe\.

Vanessa W\. Bravo / Tatiane Lima

16/07/2012

CH17962\_2012

Alterada a regra de geração do campo 16 do registro 1391 para que busque as informações da tabela de movimento de estoque

Tatiane Lima

27/07/2012

CH11475\_2012

Alterada a regra do C100 campo 03\. 

Juliana Garcia

02/05/2012

CH16797\_2012

Alterada a regra do campo 15 do 1391 para considerar Álcool Anidro e Hidratado

Tatiane Lima

09/08/2012

OS3701\-A

Alterada a regra de geração do registro H020

Tatiane Lima

20/08/2012

CH21598\-A\_2012

Adicionado uma regra dentro dos campos 14 e 15 para considerar as outras entradas de mel residual

Tatiane Lima

04/09/2012

OS3736

Atualiza a regra de geração do campo 04 do registro 1391 para que busque as informações do inventário considerando a data do saldo inicial parametrizada na tela de geração do SPED Fiscal

Marcos G\. de Paula

13/09/2012

CH23602\_2012

Atualiza a regra de geração do campo 04 do registro 1391 para que gere o Estoque Inicial com zero considerando que não há registros de Inventário\.

Marcos G\. de Paula

18/09/2012

OS\-3747

Realizados ajustes no registro 1391 para o tratamento do reprocessamento do açúcar\.

Tatiane Lima

19/09/2012

OS3736\-A

Atualiza a regra de geração do campo 04 do registro 1391 para que busque as informações do inventário considerando a data do saldo inicial parametrizada na tela de geração do SPED Fiscal Meio Magnético Especial 

Juliana Garcia

27/08/2012

CH18537\_2012

Geração do campo C110

Henrique Francisco

25/09/2012

CH23730\_2012

Inserido um log na geração do registro D400 para quando não houver sido informado ao menos um registro D410\.

Tatiane Lima

05/10/2012

OS3701\-C

Geração do Motivo do inventário do H005

Tatiane Lima

17/10/2012

CH25861\_2012

Correção na geração do registro 1391, campo 12

Vanessa Bravo

29/10/2012

CH24703\-A\_2012

Atualiza regra de geração do registro C115 passando a gerar o mesmo apenas quando o modelo da NF que deu origem ao registro pai, C110, for diferente de 55

Marcos

30/10/2012

CH8770\_2012

Alteração de regra do Registro D100

Henrique Francisco

30/10/2012

OS3785

Atualização Legal/ Ato Cotepe 50 Ago/2012

Juliana Garcia

31/10/2012

CH25861\-A\_2012

Correção na geração do registro 1391, campo 12

Vanessa Bravo

09/11/2012

CH25861\-B\_2012

Correção na geração do registro 1391, campos 04 e 13

Marcos

05/12/2012

OS\-3838

Atualização legal – Ato cotepe 57 de Nov/2012 – Novo Código de leiaute e alteração na obrigatoriedade do campo EMAIL do registro 0100

Tatiane Lima

26/12/2012

OS3744

Atualização dos códigos de Classe de consumo

Tatiane Lima

28/12/2012

OS3369

Alteração para Geração por Inscrição Estadual Única

Tatiane Lima

28/01/2013

OS3865

Criação de campo na tabela Estabelecimento para atendimento ao registro 005

Vanessa W\. Bravo

31/01/2013

CH31859\_2012

Atualiza geração dos registros 0460, C590 e D590 passando a gerar o campo COD\_OBS\.

Marcos G\. de Paula

06/\-2/2013

OS3726

Atualização da geração do Registro 1105 para demonstrar itens de serviços

Marcos G\. de Paula

03/04/2013

OS3520\-D

Alteração SPED p/utilizar guias da GNRE Online \(reg E250\) 

Vânia Dias Mattos

22/02/2013

OS3928

Atualização na geração dos registros E116 e E250, para UF SC

Vanessa W\. Bravo

26/04/2013

OS3983

Atualização legal: inclusão do layout 1\.0\.7\.

Impactos nas regras: RN0000\-02, RNC100, RNC100\-04, RNC100\-06, RNC100\-09, RNC190, RNC400, RNC405, RNC420, RNC460, RNC465 e RNC490

Marcos G\. de Paula

09/05/2013

OS2931\-H1

Geração dos registros de Cupom Fiscal Eletrônico \(CF\-e\)

\(C116, C800, C850, C860 e C890\)

Vânia Dias Mattos

28/05/2013

OS4045

Alteração na geração do registro 1400 p/considerar as operações especiais de venda de energia elétrica de modelo 55\. 

Vânia Dias Mattos

27/06/2013

CH5209\-A/2013

Ajustes na regra de geração do E500 e filhos para geração através do módulo PIM

Marcos G\. de Paula

22/07/2013

OS4070

Tratamento para conversão de unidade de medida nas quantidades do Registro 1391 

Vânia Dias Mattos

11/09/2013

OS4043

Alteração na regra do campo Valor Unitário quando o Estabelecimento possui IEU\.

Juliana Garcia Vilas Boas

18/10/2013

CH26284/2013

Ajustar a regra de seleção do registro 0205 para que passe a gerar alterações na descrição do item realizadas em período anterior à movimentação atual, desde que não tenham sido registradas movimentações no intervalo entre a atualização e o período de geração\.

Marcos G\. De Paula

21/10/2013

CH26274\_2013

Ajustar a regra de seleção do registro 0175 para que desconsidere a Inscrição Estadual do participante

Julyana Perrucini

29/10/2013

CH26996\-A/2013

Ajustar a regra de seleção do registro 0200 para que seja gerado em função do 0220 quando há movimentação no período, mesmo que a movimentação do produto não seja demonstrada\.

Marcos G\. de Paula

31/10/2013

OS4139

Alteração nas regras de geração dos registros 1350/1370  \(Postos de Combustível\)

Vânia Dias Mttos

05/11/2013

OS4261

Alterações do Ato Cotepe 43/2013\. Aumento na qdt das sub\-apurações\.

Vânia Dias Mttos

06/12/2013

OS4261

Alterações do Ato Cotepe 52/2013\. Nova versão de layout \(RN0000\-02\)

Marcos G\. de Paula

23/12/2013

CH11204\-B

Alteração na gravação do código do Bem \(regsitros 0200, C170 e G140\)

Vânia Dias Mttos

14/01/2013

CH31293\_2013

Alteração do campo 08 do Registro H010 para preenchê\-lo apenas quando o proprietário/possuidor que não seja o informante do arquivo\.

Julyana Perrucini

28/01/2014

CH1701\_2014

Alteração na regra de geração do campo VL\_ICMS do registro C490

Vânia Dias Mattos

04/02/2014

CH2034\_2014

Correção de duplicidade na geração do registro 1105

Vânia Dias Mattos

11/02/2014

OS4350

Tratamento para truncar informação do campo 03 – TXT\_COMPL dos Registros 0450 e C110

Julyana Perrucini

27/02/2014

CH11946\_2013

Alteração na regra de totalização do valor das operações do período e da totalização dos valores de deduções do Registro 1400 para Telecom / Energia Elétrica / Água

Julyana Perrucini

13/03/2014

OS4416

Ajuste na geração do campo 03\-QTD\_MOID do registro 1391

Vânia Dias Mattos

07/03/2014

OS4342

Geração do Bloco K \(registros K200/K220\)

Vânia Dias Mattos

20/03/2014

Ch5218/2014

Correção na geração do D197 

Vânia Dias Mattos

27/03/2014

OS4461

Ateração de Regra de Negócio Registro 0175

Marcelo Souza

28/03/2014

OS4342\-A

Geração do Bloco K \(registros 0210/K230/K235\)

Vânia Dias Mattos

01/04/2014

OS4342\-B

Geração do Bloco K \(registros K250/K255\) 

Vânia Dias Mattos

11/04/2014

OS4459\-A

Alterações no Modelo C para mostrar os resultados separados por fração

Vânia Dias Mattos

22/04/2014

OS4342\-C

Inclusão do novo campo VL\_ITEM\_IR do registro H010

Vânia Dias Mattos

05/06/2014

OS4533

Alteração geração do campo 05\-COD\_REC dos registros E116 e E250

Vânia Dias Mattos

01/07/2014

OS4535

Inlusão da versão 1\.0\.8 \(Ato Cotepe 22/2014\) \(ver __RN0000\-02__\)

Vânia Dias Mattos

03/07/2014

OS4540

Criação de parâmetro p/a geração do campo VLR\_ICMS do registro C490 \(__RNC490\-07\)__

Vânia Dias Mattos

18/07/2014

OS4567

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Alteração do Registro 0205 para gravar a informação  quando houver alteração do código de item \(__RN0205/RN0200\-05__\)\.

Julyana Perrucini

18/07/2014

OS3655

Alteração geração do campo BAIRRO do registro 0005 para utilizar o novo campo “Bairro” incluído no cadastro dos Estabelecimentos \(ver __RN0005\-07__\)

Vânia Dias Mattos

04/08/2014

OS4578

Alteração na geração do campo 05\-COD\_REC do registro E250

Vânia Dias Mattos

14/08/2014

CH31337\_2013

Alteração na recuperação do Registro E210 a partir do módulo PIM \(ver __RNE210__\)

Julyana Perrucini

03/09/2014

OS4508

Alteração da geração para multiempresa \(apenas o menu da geração “normal”\)

\(C800, C860, E510\)\. Foi realizado apenas um ajuste nessas regras para não causar confusão\. Na verdade, as regras da geração não se alteram p/a geração multiempresa\.

Vânia Dias Mattos

18/09/2014

OS4593\-B

Alteração da geração da opção “Geração\-PIM” para gravar as subapurações \(1900 e filhos\) 

Vânia Dias Mattos

22/09/2014

CH20470\-A\_2014

Alteração na regra de geração do registro 0205 para demonstrar alterações para períodos maiores ou iguais a 01/01/2000\.

Marcos G\. de Paula

29/09/2014

CH13937/2014

Alteração na regra de geração do campo IND\_PGTO do registro C100, para considerar a versão do layout parametrizada ao invés da data fiscal na geração do campo\.

Marcos G\. de Paula

21/11/2014

CH23229\_2014

Este documento tem como objetivo alterar a regra o campo 05 – Código de Receita do Registro E250 para UF favorecida de SC quando não houver preenchimento da Classe de Vencimento\.

Julyana Perrucini

24/11/2014

CH26523\_2014

Este documento tem como objetivo incluir tratamento para o campo 11 – Código do serviço do Registro 0200 em atendimento ao Ato Cotepe nº 59/2014\.

Julyana Perrucini

05/12/2014

OS4609

Inlusão da versão 1\.0\.9 \(Ato Cotepe 49/2014\) \(ver __RN0000\-02__\)

Vânia Dias Mattos

22/01/2015

CH706/2015

Este documento tem como objetivo alterar a geração do Registro H010 para contemplar o campo 11\-Valor do item para efeitos do Imposto de Renda para inventários que devem ser entregues em 2015\. Obs\.: Lembrando que em via de regra o inventário ocorre em data anterior\.

Julyana Perrucini

23/01/2015

CH16777\_2014

Este documento tem como objetivo alterar a geração do campo 15\-Valores recolhidos ou a recolher, extraapuração do Registro E210 contemplando débito especial de serviços de transportes\.

Julyana Perrucini

04/02/2015

CH28472\_2014

Este documento tem como objetivo ajustar o tratamento para o campo 11 – Código do serviço do Registro 0200 em atendimento ao Ato Cotepe nº 59/2014\.

Julyana Perrucini

11/02/2015

CH1938\_2015

Este documento tem como objetivo ajustar o tratamento para o campo 11 – Código do serviço do Registro 0200 em atendimento ao Ato Cotepe nº 59/2014\.

Julyana Perrucini

01/04/2015

OS4747

Alteração na geração dos registros 0150, C100, C113, C160, C165, C176, C500, C510, D100, D130, D140, D170, D400, D500, D510, E113, E240, G130, H010, K200, 1110, 1500, 1510, 1600 e 1923\.

Marcos G\. de Paula

09/04/2015

CH7058\_2015

Tratamento na geração do campo 07\-SER dos Registros C100 e D100 para considerar o preenchimento obrigatório das três posições exigidas pelo layout para NF\-e, NFC\-e e CT\-e\.

Julyana Perrucini

29/04/2015

CH8390\_2015

Ajuste na geração do registro 0150 para que seja considerado apenas o cadastro de participante correspondente a última nota que houve movimentação no período\.

Lara Aline

06/05/2015

CH28561\-B

Alteração na geração do campo 15\-DEB\_ESP\_ST do registro E210\. 

Vânia Dias Mattos

21/05/2015

OS’s4728

OS’s4735

Alteração na geração do registro 1400 para atendimento à Resolução 4730/14\-MG e  Portaria CAT 137/2014\-SP\. Consultar as observações descritas no cabeçalho do reg\. 1400, e as regras específicas de MG e SP: __RN1400\-MG\-“nn” e RN1400\-SP\-“nn”__\.

Vânia Dias Mattos

25/05/2015

OS4786

Alteração na geração do Convênio 115 p/tratamento do modelo \(ver RNC700, RNC790, RNC791, RND695, RND696 e RND697\)

Vânia Dias Mattos

18/06/2015

CH2489\_2015

Alteração na geração do Registro 0210 p/ tratamento de recursividade \(Ver RN0210 e RN0210\-02\)\.

Julyana Perrucini

30/06/2015

CH13043\_2015

Alteração de regra G130 para geração de TIPO\_MOV = CI

Marcos G\. de Paula

30/06/2015

CH4543\_3015

Alteração da regra do G130 para atender à geração especial\.

Marcos G\. de Paula

22/07/2015

CH14943\_2015

Alteração da gravação do campo Município do Registro 1400 referente a regra específica de SP \(DIPAM 31, 35 e 36\)\.

Julyana Perrucini

27/07/2015

CH15998\_2015

Observação sobre a geração do Registro 1900 e “filhos” para outras UFs que não estão especificadas no GUIA PRÁTICO\.

Julyana Perrucini

30/07/2015

CH16703\_2015

Melhoria na especificação da regra de negócio do Registro 0175\.

Julyana Perrucini

11/08/2015

OS4821

Atualização da Geração do Registro C178, para contemplar geração das informações “Ad Valorem”\.

Marcos de Paula

13/08/2015

CH13043\-B/2015

Atualização da regra de geração do campo Chave da Nfe do registro G130, considerando regra do GP 2\.0\.16\.

Marcos de Paula

21/08/2015

CH16394 / 2015

Alterada regra de geração do campo 03\-DT\_FIN\_OP do K230  

Vânia Dias Mattos

08/09/2015

MFS1507

Alteração na geração do registro 1400 para atendimento à Portaria N\. 34\-R, de 26/08/2015 – Sefaz\-ES\. Ver as observações descritas no cabeçalho do reg\. 1400, e as regras específicas do ES: __RN1400\-ES e RN1400\-ES\-“nn”__\.

Vânia Dias Mattos

11/09/2015

MFS1513

Alteração na geração do registro 1400 para atendimento à Portaria N\. 34\-R, de 26/08/2015 – Sefaz\-ES\. Geração auitomática dos códigos 01, 02,  03 e 06\. 

\(ver __RN1400\-ES\-01__,__  RN1400\-ES\-02, RN1400\-ES\-03 __e__ RN1400\-ES\-06\)__

Vânia Dias Mattos

14/09/2015

MFS1566

Alteração na geração do registro 1400 para atendimento à Portaria N\. 34\-R, de 26/08/2015 – Sefaz\-ES\. Geração auitomática dos códigos 05, 07, 09  e 10\. 

\(ver __RN1400\-ES\-05__,__  RN1400\-ES\-07__,__ RN1400\-ES\-09  __e__ RN1400\-ES\-10\)__

Vânia Dias Mattos

15/09/2015

CH21311\_2015

Alteração na seleção das informações a partir da SAFX130 para geração do Registro C100 \(ver __RNC100__\)\.

Julyana Perrucini

22/09/2015

MFS1401

Alterou a geração do registro 1390/1391 para que os saldos sejam demonstrados diariamente, mesmo qdo não houver movimentação \(ver __RN1390 __e__ RN1391__\)\.

Vânia Dias Mattos

22/10/2015

MFS1858 \(CH23338 e 23915\)

Alteração na geração do H020 \(só gerar qdo o MOT\_INV do H005  <> 01\) 

Vânia Dias Mattos

28/10/2015

MFS1993

Alteração na geração do K230, campo 04\-COD\_DOC\_OP \(ver __RNK230\-04__\)\. 

Ajuste no K220, K230 e K50 quanto ao tipo do item \(__RNK220, RNK230 __e__ RNK250 __\)

Ajuste no 0210 quanto a identificação do tipo do item nos componentes “subprodutos”\. \(ver __RN0210\-02__\)\.

Vânia Dias Mattos

06/11/2015

MFS2068 \(CH25342\_2015\)

Alteração na geração do K200 para que não seja recuperado registros de inventários igual a zero \(ver RNK200\)\. 

Lara Aline

10/11/2015

MFS2159

\(CH 25797/15\)

Ajustes na geração do 0210 sobre recuperação dos dados da lista técnica \(ver __RN0210__\)\.

Ajustes na geração do COD\_DOC\_OP do K230 \(ver __RNK230\-04__\)

Vânia Dias Mattos

10/11/2015

MFS2128 \(CH16250\_2015\)

Alteração na geração do 0206 para os Postos de Combustíveis sejam considerados como Classe de atividade do Estabelecimento \(ver RN0206\)\. 

Lara Aline

13/11/2015

CH24790\_2015

Alteração dos campos 05 e 14 do Registro 1391 e recuperação do grupo de contagem 3 quando for a partir de estoque \(Ver __RN1391, RN1391\-05 e RN1391\-14__\)

Julyana Perrucini

27/11/2015

MFS2133

Geração dos Registros do Ato Cotepe/ICMS 44/2015 \(ver RNC101, RND101, RNE300, RNE311, RNE312, RNE313 e RNE316\)

Vânia Dias Mattos

14/12/2015

CH24790\-C\_2015

Alteração do campo 05 do Registro 1391 para considerar a Operação parametrizada \(Ver __RN1391\-05__\)

Julyana Perrucini

17/12/2015

MFS2413 \(CH25930/15\)

Altera geração do K230/K235 para permitir produção sem insumos associados, nos casos em que a produção for iniciada em períodos anteriores \(ver __RNK235__\)

Vânia Dias Mattos

22/12/2015

CH28328\_2015

Este documento tem como objetivo alterar a geração do campo 04\-Valor total do ICMS ST de devolução de Mercadorias e do campo 06\-Valor total de Ajustes "Outros créditos ST" e “Estorno de débitos ST” do Registro E210 da obrigação acessória SPED Fiscal\.

Julyana Perrucini

11/01/2016

CH165\_2016

Alteração do campo 04 do Registro 1391 para considerar o grupo de contagem 3 \(Ver __RN1391\-04__\)

Julyana Perrucini

08/12/2015

MFS2406

Geração dos Registros do Ato Cotepe/ICMS 44/2015 a partir do Módulo PIM

Vânia Dias Mattos

18/01/2016

MFS2901

Geração dos Registros do Ato Cotepe/ICMS 44/2015 a aprtir do livro “165”

Vânia Dias Mattos

25/01/2016

MFS2232

Alteração da geração do campo 02 do Registro 1390 e do campo 03 do Registro 1391 para considerar também as informações da SAFX10 via parametrização\.

Julyana Perrucini

25/01/2016

MFS2714

Alteração no Módulo CIAP: Nova parametrização de regras específicas no formato “Por Estabelecimento” \(ver __RN0300\-07__\)\.

Vânia Dias Mattos

16/02/2016

MFS3132

Alteração na geração do registro 1400 para atendimento à Orientação Técnica EFD nº 011/2016 – Versão 1\.10, de 11/02/2016 – SET\-RN\. Ver as observações descritas no cabeçalho do reg\. 1400, e as regras específicas de RN: RN1400\-RN e RN1400\-RN\-“nn”\.

Lara Aline

21/03/2016

MFS3615

Criação do cálculo dos créditos extemporâneos de Bens com prazo de apropriação “normal” já ultrapassado \(opção de menu “Cálculo Créditos Extemporâneos\-Integral”\)\. Ver __RNG110\-10, RNG125__, __RNG125\-ESP__,__ RNG126__, __RNG130__ e __RNG140__\.

Vânia Dias Mattos

05/04/2016

CH5111\_2016

Alterada a regra de geração do registro E300 e E310 para que sejam gerados para todas as UF’s geradas no registro “0015\-Dados do Contribuinte Substituto”\. Ver __RNE300 e RNE310\.__

Lara Aline

03/05/2016

MFS\-1661

Alterada regra de geração do registro 0200 campo COD\_ITEM\.

Elenilson Coutinho

06/05/2016

MFS4106

Alterada regra de geração do registro H005\.

Lara Aline

20/05/2016

CH10645\_2016

<a id="OLE_LINK115"></a><a id="OLE_LINK116"></a><a id="OLE_LINK117"></a>Alterada regra de preenchimento do campo 03\-SERIE do Registro 1105\.

Julyana Perrucini

24/06/2016

MFS4992

Ato Cotepe 7/2016 – Novos Registros Bloco K \(K210, K215, K260 e K265\)

Vânia Dias Mattos

28/06/2016

MFS4993

Ato Cotepe 7/2016 – Novos Registros Bloco K \(K270, K275 e K280\)

Vânia Dias Mattos

04/10/2016

MFS5904

Alteração na geração da classe de consumo do registro 1500 \(ver __RN1500\-09__\)

Vânia Dias Mattos

11/11/2016

MFS3248

Alteração na geração do registro 1400 para atendimento à Orientação Técnica EFD nº 011/2016 – Versão 1\.10, de 11/02/2016 – SET\-RN\. Para periodicidade Anual\. Ver as observações descritas no cabeçalho do reg\. 1400, e as regras específicas de RN: RN1400\-RN e RN1400\-RN\-“nn”\.

Lara Aline

29/11/2016

MFS7082

Inclusão do campo CHV\_DOCe nos registros 1210 e 1923 \(ver __RN1210\-05__ e __RN1923\-10__\)\.

Vânia Mattos

09/12/2016

MFS7944

Alteração na geração do registro 1400 para o estado do RS\. Ver as observações descritas no cabeçalho do registro 1400, e as regras específicas do RS\.

Vânia Mattos

12/12/2016

MFS8332 \(ch24201\)

Alteração na geração do K220 \(informar fator de conversão entre produto origem e produto destino\) 

Vânia Mattos

16/12/2016

MFS8625

Alteração na geração do registro 1400 para o estado do RS: geração automática dos códigos 01, 02, 03 e 05\.

Vânia Mattos

03/01/2017

MFS8933

Alteração GP vrs 2\.0\.20: alterada chave do K235 e K255\. Para atender as novas regras, foi alterada a consolidação dos dados para a geração dos registros K235 e K255  \(ver __RNK235 __/ __RNK235\-05, __e__ RNK255 __/__ RNK255\-05__\)

Vânia Mattos

25/01/2017

MFS7449

Alteração do 1400 para SP\. Os códigos SPDIPAM23 e SPDIPAM24 passaram a tratar as deduções, para ficar de acordo com a GIA\-SP\. 

Vânia Mattos

02/02/2017

MFS6919

\(ch18552/16\)

Alteração na geração padrão do 1400 para o segmento de EE \(modelo 06\)\.

\(ver RN1400 e RN1400\-02\)

Vânia Mattos

03/03/2017

MFS8937

Alteração GP vrs 2\.0\.20: Alterado registro 1923 \(campo 10\) p/ o mod 67 \(RN

\-10\)\.

Andréa Rocha

07/03/2017

MFS9912

\(Ch 25325\_2016\)

Alteração na geração dos registros 1100 e 1105 em relação ao modelo do documento \(campo 17 da SAFX48\)\.

Vânia Mattos

16/03/2017

MFS10054

Alteração na geração dos registros do Bloco K, para usar o novo parâmetro que define se a concatenação Cód OP \+ Cód Dif OP será feita ou não\. 

Vânia Mattos

20/03/2017

MFS10057 \(CH3814\_2017\)

Alteração na geração do campo 03\-COD\_ITEM do registro K280 para que seja verificado o tipo do item na geração do mesmo \(ver RNK280\-03\)\. 

Lara Aline

28/03/2017

MFS9659

\(CH 1411/17\)

Ajuste na geração do registro 1110 devido à alteração no campo 22 da SAFX103\.

Vânia Mattos

04/05/2017

MFS10558

Ajustes na geração do registro 1100 devido à nova vrs 2\.3\.4 do PVA 

Vânia Mattos

10/03/2016

MFS2437

Alterada a geração do registro 1400 \(código SPDIPAM25\) para as empresas distribuidoras de energia elétrica \(ver __RN1400\-SP__, __RN1400\-SP\-07\-A __e__ RN1400\-SP\-07\-B__\)\.

Vânia Dias Mattos

07/08/2017

CH13531\_2017 \(MFS12315\)

Alteração do 1400 para RS\. O código 01 passa a tratar as deduções por conta da regra da SEFAZ que prevê a dedução das aquisições de serviço\.

Julyana Perrucini

23/08/2017

CH14722\_2017 \(MFS13143\)

Esse documento tem como objetivo alterar a geração dos Registros da obrigação SPED Fiscal que possuam o campo 03 \(Texto Livre\) para respeitar o limite de até 255 caracteres\.

Para os Registros 1922 e 1926 as informações de Observação constantes no campo TXT\_COMPL deverão ter um tamanho máximo de 255 caracteres\. Caso a informação a ser recuperada possua mais do que 255 caracteres, o restante da informação deve ser “truncada”\.

Julyana Perrucini

13/09/2017

CH14084\_2017 \(MFS13293\)

Utilizar município de destino para o registro 1400 Energia Elétrica quando UF= SC

Jorge Neto

18/09/2017

MFS13290

Ato Cotepe 48/2017: inclusão do campo 06\-QTD\_DEST no registro K220\.

Vânia Mattos

22/11/2017

MFS11655

Tratamento para itens de energia elétrica, telecom ou água para composição do Registro 1400 \(Ver __RN1400__\) a partir da parametrização de Exclusão\.

Julyana Perrucini

23/11/2017

MFS14303

Inclusão do código SPDIPAM27 a geração do registro 1400 para as empresas que fazem vendas presenciais com saídas em outro estabelecimento \(ver __RN1400\-SP__ e __RN1400\-SP\-12__\)\.

Julyana Perrucini

15/02/2018

MFS16603

Essa correção tem como finalidade permitir a geração do registro H020 \- Informação Complementar do Inventário mesmo quando o Motivo do Inventário for igual '01 \- No final do período' para os estabelecimentos do estado do 'RS'\.

João Henrique

26/02/2018

MFS14605

Alteração do 1400 para MG\. O código Produtos Agropecuários passa a tratar as deduções por conta da regra da SEFAZ que prevê a diferença a maior apurada entre os valores constantes da Nota Fiscal relativa à entrada dos produtos agropecuários no estabelecimento destinatário e a Nota Fiscal de Produtor ou Nota Fiscal Avulsa de Produtor, exceto quando ele emitir a nota fiscal complementar \(Ver __RN1400\-MG\-01__\)\.

Julyana Perrucini

29/03/2018

MFS16811

<a id="OLE_LINK163"></a><a id="OLE_LINK164"></a><a id="OLE_LINK165"></a>Alteração na geração do registro 1400 para o estado da BA: geração automática dos códigos BAE01, BAS01, BAE02, BAS02, BAE03, BAS03, BAE04 e BAS04\. 

Julyana Perrucini

03/04/2018

MFS17478

Criação de Parâmetro para inibir a geração das informações de PIS e COFINS

Andréa Rocha

17/04/2018

CH7744\_2018

MFS\-17914

Inclusão de modelo de documento fiscal para geração do registro SPDIPAM23 seguindo a legislação no que diz respeito ao segmento de transporte\.

João Henrique

24/04/2018

CH9368\_2018 \(MFS\-18062\)

Alteração do 1400 para SP\. O código DIPAM\-35 passa a considerar outros ajustes com relação ao CFOP 5927 \(Ver __RN1400\-SP\-10__\)\.

Julyana Perrucini

30/04/2018

MFS17764

Alteração na geração do registro 1400 para o estado de TO: geração automática dos códigos <a id="OLE_LINK87"></a><a id="OLE_LINK88"></a>TOIPME04, TOIPMS04, TOIPME06, TOIPMS06, TOIPME07, TOIPMS07, TOIPME08 e TOIPMS08\.

Julyana Perrucini

12/06/2018

MFS18797

Alteração na geração do registro 1400 para o estado de SP: criadas novas regras para o código SPDIPAM25 para as empresas geradoras de energia \(ver RN1400\-SP\-07\-C\)\.

Vânia Mattos

14/06/2018

MFS19151

Alteração na geração do registro 1400 para o estado de SP: alteração da regra para o código SPDIPAM22 para a forma de cálculo igual a “Valor Total NF – Revendedor Autônomo” \(ver RN1400\-SP\-04\)\.

Andréa Rocha

13/08/2018

MFS20147

Alteração na geração Padrão do Registro 1400 para Telecom, Energia Elétrica e Água para incluir filtro do novo parâmetro de exclusão de itens sem receita \(ver __RN1400__\) e alteração na geração específica por UF do RS para incluir filtro do novo parâmetro de exclusão de itens sem receita mais a seleção por CFOP ou CFOP/Natureza na totalização dos valores para o código 02 \(ver __RN1400\-RS\-02__\)\.

Julyana Perrucini

23/08/2018

MFS20216

Alteração na geração padrão do 1400 para o segmento de Telecom \(modelos 21 e 22\) \(ver RN1400 e RN1400\-02\)\.

Andréa Rocha

05/11/2018

MFS21914

Novos Campos no registro 1010 \(Guai Prático Vrs 3\.0\.1\)

Vânia Mattos

19/12/2018

MFS\-22404

Alteração na geração padrão do 1400 para operações de EPPP aos estabelecidos no Paraná \(ver __RN1400__ e __RN__\)\.

Julyana Perrucini

14/01/2019

MFS23500

Alteração na geração do registro 1400 para o estado de RJ\.

Andréa Rocha

21/03/2019

MFS25285

Alteração na geração do registro 1923, campo 02\-COD\_PART\.

Andréa Rocha

15/05/2019

MFS26339

Alteração na geração padrão do 1400 \- Aquisição de Produtos Primários para considerar o novo parâmetro

Andréa Rocha

29/05/2019

MFS14138

Alteração na geração do registro H010 para calcular o valor unitário na geração “normal”, da mesma forma já realizada para a geração por I\.E\.U\.

Vânia Mattos

30/05/2019

MFS27727

Alteração na geração do registro 1923, campo 04\-SER\.

Andréa Rocha

06/08/2019

MFS\-28753

Alteração na geração do registro 1400, para a UF MG, para operação “Produtos Agropecuários” \(__RN1400\-MG\-01\)\.__

Inclusão no filtro das notas de entrada, notas com o campo MOVTO\_E\_S = “1”\.

Alessandra Cristina Navatta

16/08/2019

MFS29417

Alteração da regra do registro 1400 para a UF BA, para tratar valores negativos

Andréa Rocha

21/08/2019

MFS25117

Alteração na geração padrão do 1400 para operações de EPPP aos estabelecidos no Paraná

Andréa Rocha

06/09/2019

MFS30223

Alteração na geração do registro 1400 para o estado de PE\.

Andréa Rocha

16/09/2019

MFS22946

Ressarcimento do ICMS ST \- RS \- Alteração na Geração dos registros 1920, 1921, 1923

Liliane Assaf

30/09/2019

MFS21172

Alteração na geração padrão do registro 1400 para a UF BA, para recuperar os valores da geração específica para Empresas de Água

Andréa Rocha

08/10/2019

MFS30891

Alteração na geração padrão e específica por UF do registro 1400, para utilizar a parametrização de deduções de CST x Produto, para energia elétrica\. E retirar a utilização da parametrização de CST x Produto da exclusão de itens sem receita\.

Andréa Rocha

28/10/2019

MFS31044

Alteração na geração específica do registro 1400 para a UF TO, para gerar o código TOIPME10 automaticamente\.

Andréa Rocha

20/12/2019

MFS33054

Inclusão de um Campo novo no registro 1010 \(Guia Prático Vrs 3\.0\.3\)

Andréa Rocha

23/12/2019

MFS31418

Alteraões no Bloco H para a versão 1\.13, a partir de JAN/2020: 

\- Geração do novo registro H030;

\- Inventário Mensal para o Motivo de Inventário = 6;

Vânia Mattos

#### Bloco 1 – Outras Informações 

# <a id="_Toc75782958"></a>Registro 1001 – Abertura do Bloco 1

RNC001

Um registro por arquivo\.

# <a id="_Toc75782959"></a>Registro 1010 – Obrigatoriedade De Registros Do Bloco 1

__RN1010__

__Regra Geral__

Deve ser apresentado por todos os contribuintes\. 

Caso exista movimentação no registro respectivo, então gerar a informação do campo como “S”, caso não exista movimentação, gerar como “N”\.

Registro deve ser gerado apenas a partir da versão EFD105 do leiaute \(Julho/2012\)

__RN1010\-02__

__Campo IND\_EXP__

Se houver movimentação para o período no registro 1100, então o sistema deve gerar automaticamente este campo com o valor “S”\. 

Se não houver movimentação, gerar como “N”\.

__RN1010\-03__

__Campo IND\_CCRF__

Se houver movimentação para o período no registro 1200, então o sistema deve gerar automaticamente este campo com o valor “S”\. 

Se não houver movimentação, gerar como “N”\.

__RN1010\-04__

__Campo IND\_COMB__

Se houver movimentação para o período no registro 1300, então o sistema deve gerar automaticamente este campo com o valor “S”\. 

Se não houver movimentação, gerar como “N”\.

__RN1010\-05__

__Campo IND\_USINA__

Se houver movimentação para o período no registro 1390, então o sistema deve gerar automaticamente este campo com o valor “S”\. 

Se não houver movimentação, gerar como “N”\.

__RN1010\-06__

__Campo IND\_VA__

Se houver movimentação para o período no registro 1400, então o sistema deve gerar automaticamente este campo com o valor “S”\. 

Se não houver movimentação, gerar como “N”\.

__RN1010\-07__

__Campo IND\_EE__

Se houver movimentação para o período no registro 1500, então o sistema deve gerar automaticamente este campo com o valor “S”\. 

Se não houver movimentação, gerar como “N”\.

__RN1010\-08__

__Campo IND\_CART__

__\[MFS74676\] __

- __Para Geração c/ leiaute anterior a EFD115 \(CAD\_LAYOUT – COD\_VERSAO<115\):__

Se houver movimentação para o período no registro __1600__, então o sistema deve gerar automaticamente este campo com o valor “S”\. 

Se não houver movimentação, gerar como “N”\.

- __Para Geração c/ leiaute a partir da EFD115 \(CAD\_LAYOUT – COD\_VERSAO>=115\):__

Se houver movimentação para o período no registro __1601__, então o sistema deve gerar automaticamente este campo com o valor “S”\. 

Se não houver movimentação, gerar como “N”\.

__RN1010\-09__

__Campo IND\_FORM__

Se houver movimentação para o período no registro 1700, então o sistema deve gerar automaticamente este campo com o valor “S”\. 

Se não houver movimentação, gerar como “N”\.

__RN1010\-10__

__Campo IND\_AER__

Se houver movimentação para o período no registro 1800, então o sistema deve gerar automaticamente este campo com o valor “S”\. 

Se não houver movimentação, gerar como “N”\.

__RN1010\-11__

__Campo IND\_GIAF1__

__MFS21914:__ Os campos 11, 12 e 13 serão gerados apenas a partir da versão de layout 112 \(código = 013\), válida a partir de 01/01/2019\.

Se houver movimentação para o período no registro __1960__ \(GIAF 1 \- Indústria\), então o sistema deve gerar automaticamente este campo com o valor “S”\. 

Se não houver movimentação, gerar como “N”\.

__ __

__RN1010\-12__

__Campo IND\_GIAF3__

__MFS21914:__ Os campos 11, 12 e 13 serão gerados apenas a partir da versão de layout 112 \(código = 013\), válida a partir de 01/01/2019\.

Se houver movimentação para o período no registro __1970__ \(GIAF 3 \- Importação\), então o sistema deve gerar automaticamente este campo com o valor “S”\. 

Se não houver movimentação, gerar como “N”\.

__RN1010\-13__

__Campo IND\_GIAF4__

__MFS21914:__ Os campos 11, 12 e 13 serão gerados apenas a partir da versão de layout 112 \(código = 013\), válida a partir de 01/01/2019\.

Se houver movimentação para o período no registro __1980__ \(GIAF 4 – Central de Distribuição\), então o sistema deve gerar automaticamente este campo com o valor “S”\. 

Se não houver movimentação, gerar como “N”\.

__RN1010\-14__

__Campo__ __IND\_REST\_RESSARC\_COMPL\_ICMS__

__MFS33054:__ O campo 14 será gerado apenas a partir da versão de layout 113 \(código = 014\), válida a partir de 01/01/2020\.

__MFS31423: __Preenchimento automático do campo

Se houver movimentação para o período no registro __1250__, então o sistema deve gerar automaticamente este campo com o valor “S”\. 

Se não houver movimentação, gerar como “N”\.

# <a id="_Toc75782960"></a>Registro 1100 – Registro de Informações sobre Exportação

CHAMADO:

CH51541

__      __

__       ALTERAÇÃO NA REGRA DE NEGÓCIO__

Será colocada uma regra dentro da geração do SPED fiscal, de forma, que quando o sistema ler o campo 04 da SAFX48 para gerar o registro 1100, este leve para o campo 06 desse registro as informações encontradas na SAFX48 sem caracteres especiais, ou seja, durante a geração do arquivo magnético, se o usuário tiver selecionado no perfil o registro 1100 \(Registro de Informação sobre Exportação\) do Bloco 1 \(Outras informações\), o sistema deverá alimentar o campo 06 desse registro com a informação do campo 04 da SAFX48, porém, levará para o “TXT” os valores sem caracteres especiais tipo “ – e / ”\.

      Solicitante: Elizangela Pereira   Requisitos –  \(11\) 2159 \- 0537

      Dia da solicitação: 18/11/2008

       Foi adotado mesmo procedimento para o campo 51 \(Número da DDE / DSE\) da SAFX48\.

          Documentado por: Adilson Gomes

RN1100

Selecionar na tabela SAFX48 todas as notas fiscais de exportação direta ou indireta que tenham concluído o processo de exportação no período de apuração solicitado\. 

Regra para Seleção:

  \- Modelo NF = “01 e 55”,    \(critério excluído pela __MFS9912__, Ch 25325/16\)

  \- Indicador de Averbação = “sim”,

  \- Indicador tipo de operação = D, I, DS, IS, U ou UI ou não preenchida\.  

__                                                                     __\(__MFS10558__: inclusão das opções U e UI\)   

  \- Data de Averbação >= campo 4 do registro 0000 e <= campo 5 do registro 0000,

A chave para seleção de cada registro 1100 deve seguir a ordenação do quadro em anexo, ou seja, deve\-se gerar um registro pai \(1100\) para cada CHAVE DA DECLARAÇÃO e para os registros filhos \(1105\) devem\-se gravar todos os itens das notas vinculadas a cada CHAVE DA DECLARAÇÃO\.

CHAVE DA DECLARAÇÃO:

CAMPO

DESCRIÇÃO DO CAMPO NO ATO COTEPE 11

CAMPO NA  TABELA SAFX48

NRO\_DE

Número da declaração 

51\-Número da DDE / DSE

DT\_DE

Data da declaração \(DDMMAAAA\)

52\-Data da DDE / DSE

NRO\_RE

Nº do registro de Exportação

Na base de dados este campo é preenchido com espaços se exportação for simplificada\.

04\-Número do RE

DT\_RE

Data do Registro de Exportação \(DDMMAAAA\)

Na base de dados este campo é preenchido com a data de 01/01/1900 se exportação for simplificada\.

03\-Data do RE

IND\_DOC

Informe o tipo de documento:

0 \- Declaração de Exportação;

1 – Declaração Simplificada de Exportação

Definido pela regra RN1100\-02 a partir das infomações do campo   71\-Indicador de Tipo de Operação

NAT\_EXP

Preencher com:

0 \- Exportação Direta;

1 \- Exportação indireta; 

Definido pela regra RN1100\-05 a partir das infomações do campo   71\-Indicador de Tipo de Operação

CHC\_EMB

Nº do conhecimento de embarque

DT\_CHC

Data do conhecimento de embarque

DT\_AVB

Data da averbação da Declaração de exportação

TP\_CHC

Informação do tipo de conhecimento de transporte

PAIS

Código do país de destino da mercadoria

Hierarquia dos registros de exportação\.\.\.

__Nível 1__ \- 1001 \- Registro de Abertura

       __Nível 2__ \-  1100 \- Registro de Informações sobre Exportação __\(1:N\)__

             __Nível 3__ \- 1105 \- Documentos Fiscais de Exportação  __\(1:N\)__

                   __Nível 4__ \- 1110 \- Operações de Exportação Indireta de Produtos não Industrializados

                                                                                                  pelo Estabelecimento Emitente __\(1:N\)__

__OBS1:__ Na geração por Inscrição Estadual Única, deve\-se considerar os documentos de todos os estabelecimentos envolvidos na centralização\.

__OBS2__: Na geração da opção “Geração – PIM” devem ser considerados apenas as notas fiscais da inscrição estadual em questão\. Para isso, considerar apenas as notas em que o campo “Inscrição Estadual \(PIM\)” da SAFX48 seja = inscrição estadual em questão \(ver detalhes nas __OS2388\-AM3__, que definiu a criação do campo inscrição estadual na SAFX48 e definiu as regras para a geração do Sped Fiscal com foco no módulo PIM\)\.

__OBS3__: Alteração realizada na OS2931\-G: a chave da tabela X48 foi alterada para incluir o campo CHC\_EMB \(número do conhecimento de embarque\)\. Como este campo é de preenchimento *não obrigatório*, passou a ser gravado com um caracter branco sempre que o conhecimento de embarque não for informado\. Desta forma, foi necessário alterar várias obrigações do Mastersaf que usam a X48 para considerar o campo nulo sempre que seu conteúdo for um branco\.  

RN1100\-02

__Campo: IND\_DOC__

Se “ind\_tp\_venda” = D ou I, gravar “0”,

        Se “ind\_tp\_venda” = DS ou IS, gravar “1”,

             Se “ind\_tp\_venda” = U ou UI, gravar “2”   \(__MFS10558__: inclusão das opções U e UI\)

                  Se campo não preenchido gravar ||\.

Origem da Informação:

__Tabela__

__Descrição do Campo:__

__Nº do Campo:__

__Nome do Campo:__

SAFX48

Indicador de Tipo de Operação

71

IND\_TP\_VENDA

Domínio do campo:

 D  \- Exportação Direta 

  I   \- Exportação Indireta                                                                                                                                                                                       DS \- Exportação direta simplificada                                                                                                                                                                         IS   \- Exportação indireta simplificada

U    \- Declaração Única de Exportação                \(opção incluída na __MFS10558__\)

UI  \- Declaração Única de Exportação Indireta    \(opção incluída na __MFS10558__\)

T    \-  Transferência de Crédito                                                                                                                                                       

RN1100\-03

__Campo: NRO\_DE__

Campo “51\-Número da DDE / DSE”\.

Alteração da __MFS10558__: A partir da vrs 2\.3\.4 do PVA \(Abr/2017\) o campo __03\-NRO\_DE__ foi alterado de Tipo N e Tamanho 011, para Tipo C e Tamanho 14\. Por isso, seu preenchimento foi adequado para o novo tipo do campo *\(lembrando que na SAFX48 o campo 51 sempre foi alfanumérico, e seu tamanho foi aumentado tb na MFS10558 de 12 para 14 posições, ficando desta forma, compatível com o novo layout do registro 1100\)*\.  

RN1100\-05

__Campo: NAT\_EXP__

Se “ind\_tp\_venda” = D, DS ou __U__, gravar “0”,             \(__MFS10558__: incluída a opção __“U”__\)

         Se “ind\_tp\_venda” = I, IS ou __UI__, gravar “1”,      \(__MFS10558__: incluída a opção __“UI”__\)

                     Se campo não preenchido gravar ||\.

Origem da Informação:

__Tabela__

__Descrição do Campo:__

__Nº do Campo:__

__Nome do Campo:__

SAFX48

Indicador de Tipo de Operação

71

IND\_TP\_VENDA

RN1100\-06

__Campo: NRO\_RE__

\[Alteração OS 3230\]

Se Indicador tipo de operação = DS ou IS;

Gravar ||\.\.\. 

Gravar a informação que estiver no campo 04 da SAFX48 \(NUM\_RE\) quando for diferente de nulo\.

RN1100\-07

__Campo: DT\_RE__

\[Alteração OS 3230\]

Se Indicador tipo de operação = DS ou IS;

Gravar ||\.\.\. 

Gravar a informação que estiver no campo 03 da SAFX48 \(Data\_RE\) quando for diferente de ‘01/01/1900’\.

RN1100\-12

__Campo: PAIS__

A partir do código do país informado na SAFX48 \(campo: 56 – PAIS\_DEST\), acessar a tabela de países \(TACES05, tabela PAIS\)\. montar o campo concatenando as três posições do código \+ o dígito verificador\.

Exemplo: Brasil è 105 \+ 8  è __1058__

__\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-__

Gravar o código do país informado na SAFX48\.

Exemplo: Brasil è 105

A regra de negócio foi alterada em função da nova redação dada pelo ato cotepe 09/2008, alteração do campo12 \(PAIS\) do registro 1100, de numérico de 4 para numérico de 3\.

 

# <a id="_Toc75782961"></a>Registro 1105 – Documentos Fiscais de Exportação

RN1105

Neste registro serão gravados todos __\(alt\. MFS9912\) __os itens das notas fiscais de exportação direta ou indireta concluídas no mês de geração do arquivo e selecionadas conforme regra do registro 1100\.

__MFS9912__ \(Ch 25325/2016\): *Não* serão consideradas as notas de modelo <> 01/55, conforme regra do Guia Prático\. Desta forma, quando o modelo da SAFX48 \(campo 17\) for <> 01/55, o registro “filho” 1105 *não* será gravado \(e consequentemente o 1110 também não, pois é ‘filho’ do 1105\)\.

__CH2034/13__ 

\(Este chamado corrigiu erro de duplicidade no 1105\)

\(A regra abaixo foi reescrita apenas p/não gerar dúvida\) 

Para gerar o registro 1105 o programa deve identificar se existe duplicidade de código do 

produto na mesma nota fiscal, caso ocorra, fazer sumarização por código do produto\.

Para gerar o registro 1105, os itens das notas fiscais selecionadas serão agrupados por nota fiscal e produto, e será gerado um registro 1105 para cada nota / produto\. Quando existir duplicidade de código do produto na mesma nota fiscal *\(nota que tenha itens diferentes com o mesmo produto\)*, ocorrerá o agrupamento citado acima, e será gerado um único registro 1105, para que não haja a repetição de produto para a mesma nota\.

\[OS3726\]

Se no registro de exportação da SAFX48 que deu origem ao 1105 o campo “Exportação com Operações de Serviço” estiver preenchido com conteúdo “S – Sim”, além das informações dos produtos disponíveis na SAFX48, deverá ser gerado um registro para cada Item de Serviço existente na SAFX09 que tenha correspondência com o registro de Exportação \(SAFX48\)\. Para encontrar os itens de serviço se faz necessário encontrar antes o mestre \(SAFX07\) para saber se a NF é ou não conjugada\. Identificando que se trata de uma NF Conjugada, o registro 1105 passa a ser gerado também com os itens de serviço \(SAFX09\) vinculados à NF\. Essa correspondência entre SAFX07 e SAFX48 é possível de ser identificada através dos campos:

__SAFX07__

__X__

__SAFX48__

Código da Empresa

=

Código da Empresa

Código do Estabelecimento

=

Código do Estabelecimento

Data de Emissão

=

Data da Nota Fiscal

Movimento Entrada/Saída

=

Será fixo: 9 \- Documento de Saída

Normal ou Devolução

=

Será fixo: 1 \- Normal

Tipo do Documento

=

Tipo de Documento

Indicador da Pessoa Física/Jurídica

=

Indicador da Pessoa Física/Jurídica

Código da Pessoa Física/Jurídica

=

Código da Pessoa Física/Jurídica

Número do Documento Fiscal

=

Número da Nota Fiscal

Classificação do Documento Fiscal

=

Será fixo: 3 \- Mercadorias e Serviços

Neste cenário de geração de informações com itens de serviço, os campos do 01 ao 06 do registro 1105 continuam gerando as informações com base na SAFX48 que está com o campo “Exportação com Operações de Serviço” preenchido com conteúdo “S – Sim”, porém, ocorrerá uma quebra no registro onde o campo 07 – COD\_ITEM será gerado com o código do serviço da SAFX09 ou natureza do serviço da SAFX2018, sendo gerado um registro para cada item de serviço encontrado, considerando que as informações dos campos 01 ao 06 serão sempre as mesmas\.

Este registro é uma listagem dos itens vinculados à exportação, seja serviço ou mercadoria\.

Para cada registro 1100 gerado poderão existir um ou vários registros 1105\.

RN1105\-03

__Campo SERIE__

__\[ALTERADA – CH10645\_2016\]__

Esse campo é de preenchimento obrigatório com três posições para NF\-e ou NFC\-e, então considerar na geração:

<a id="OLE_LINK113"></a><a id="OLE_LINK114"></a>Se o campo 02\-COD\_MOD for igual a “55” \(origem campo 17\-Modelo de Documento da SAFX48\), considerar as três posições do campo 09\-Série do Docto Fiscal, mas caso seja menor do que o esperado preencher com zeros à esquerda e ainda se não estiver preenchida preencher com zeros \(000\)\.

Se o campo 02\-COD\_MOD for igual a “65” \(origem campo 17\-Modelo de Documento da SAFX48\), considerar as três posições do campo 09\-Série do Docto Fiscal, mas caso seja menor do que o esperado preencher com zeros à esquerda e ainda se não estiver preenchida preencher com zeros \(000\)\.

<a id="OLE_LINK102"></a><a id="OLE_LINK103"></a><a id="OLE_LINK104"></a>RN1105\-07

__\[OS3726\]__

<a id="OLE_LINK105"></a><a id="OLE_LINK106"></a><a id="OLE_LINK107"></a><a id="OLE_LINK108"></a>__Campo COD\_ITEM__

Quando a origem da informação for a tabela de exportação \(SAFX48\), este campo será resultado da concatenação do indicador do produto \+ Código do produto, quando o parâmetro Considerar Indicador no Código do Item da tela de Dados Iniciais estiver selecionado\. Se não estiver selecionado o parâmetro Considerar Indicador no Código do Item, demonstrar apenas o Código do Produto\.

Quando for originado na tabela de Item de Serviços \(SAFX09\), será gerado com o conteúdo do campo Código do Serviço com o formato “S”  \+  “\-“  \+  Código do Serviço, sendo que este formato será utilizado quando o parâmetro Considerar Indicador no Código do Item da tela de Dados Iniciais estiver selecionado\. Se não estiver selecionado o parâmetro Considerar Indicador no Código do Item, demonstrar apenas o Código do Produto\.

Se o parâmetro “Substituir o Código do Serviço pela Natureza do Serviço das NF Conjugadas” estiver selecionado, substituir o código do serviço pelo Código da Natureza do Serviço \(COD\_NAT\_SERV\) informado na SAFX2018 correspondente ao código do serviço informado na SAFX09\.

Para cada item informado neste campo deverá ser gerado um registro 0200, gerando apenas um registro do cadastro, sem duplicidades\.

# <a id="_Toc75782962"></a>Registro 1110 – Operações de Exportação Indireta de Produtos não 

# <a id="_Toc75782963"></a>Industrializados pelo Estabelecimento Emitente

RN1110

Neste registro serão gravados apenas os documentos fiscais referentes a exportação indireta de produtos não industrializados pelo estabelecimento emitente\.

Através da SAFX481 \(tabela de relacionamento entre a SAFX48 e SAFX103\), o programa deve selecionar a nota na tabela SAFX103 para gerar o registro 1110, se a regra for atendida\.

Para cada registro 1105 gerado poderão existir um, vários ou nenhum registro 1110\.

A regra para geração do registro 1110 é:

- Se for exportação indireta; \(campo NAT\_EXP do registro 1100 = “1”\); 

         Obs: Na tabela SAFX481 existe uma regra de validação para permitir somente notas de exportação indireta\.

- Se registro existir na SAFX481;
- Se campo “produto não industrializado pelo estabelecimento” = S \(campo novo na tabela                       SAFX103\)\.
- Na geração considerar as três posições do campo 09\-Série do Docto Fiscal/06\-Série do Docto Fiscal, mas caso seja menor do que o esperado preencher com zeros à esquerda e ainda se não estiver preenchida preencher com zeros \(000\)\.

Deve\-se gerar o registro 1110\.

    

Para cada item gravado no registro 1105, verificar regra para geração do registro 1110,  se afirmativo a partir da chave da safx48 buscar o item correspondente na safx481, se encontrar o registro, ir na SAFX103 para gerar o registro 1110\.

	

OBS: O campo 9 do registro 1110 deve ser gerado a partir do campo 23 da SAFX481\.

__SAFX48__

Data da RE

Número do RE

Data da Nota Fiscal

Indicador de Pessoa Física/Jurídica

Código da Pessoa Física/Jurídica

Número da Nota Fiscal

Série da Nota Fiscal

Subsérie da Nota Fiscal

Indicador do Produto

Código do Produto

Número do Item da Nota Fiscal

__SAFX481__

Data da RE \(SAFX48\)

Número do RE \(SAFX48\)

Data Emissão da Nota Fiscal \(SAFX48\)

Indicador de Pessoa Física/Jurídica \(SAFX48\)

Código da Pessoa Física/Jurídica \(SAFX48\)

Número da Nota Fiscal de Exportação \(SAFX48\)

Série da Nota Fiscal de Exportação \(SAFX48\)

Subsérie da Nota Fiscal de Exportação \(SAFX48\)

Indicador do Produto \(SAFX48\)

Código do Produto da NF\. de Exportação \(SAFX48\)

Número do Item da Nota Fiscal  de Exportação \(SAFX48\)

Número do RE \(SAFX103\)

Data da Nota Fiscal com fins Específicos de Exportação \(SAFX103\)

Indicador de Pessoa Física/Jurídica \(SAFX103\)

Código da Pessoa Física/Jurídica \(SAFX103\)

Número da Nota Fiscal com fins Específicos de Exportação \(SAFX103\)

Série da Nota Fiscal com fins Específicos de Exportação \(SAFX103\)

Sub\-série da Nota Fiscal com fins Específicos de Exportação \(SAFX103\)

Indicador do Produto \(SAFX103\)

Código do Produto \(SAFX103\)

Quantidade Exportada do Produto

RN1110\-02

__Campo: COD\_PART__

O código do participante deve ser obtido na SAFX103 através das seguintes regras:

Regra 1 \-  Se o campo “Indicador de Movimento” for = 1 __ou 2;__ 

concatenar o indicador \+ código da pessoa e gravar o código do participante\.

Regra 2 \- Se o campo “Indicador de Movimento” for = 9;

com o estabelecimento \(campo: cod\_estab da safx103\) buscar na tabela “DWT\_PFJ\_ESTAB” o “ind\_fis\_jur” e o “cod\_fis\_jur” correspondente, concatenar os dois e gravar o código do participante\.

Alteração da __MFS9659__: Foi incluída a opção 2 no campo “Indicador de Movimento” da SAFX103\. A nova opção terá o mesmo tratamento da opção 1 \(entrada de terceiros\), pois nas duas situações o campo da pessoa fis/jur estará preenchido com o emitente do documento fiscal: seja um terceiro \(opção 1\), ou a pessoa fis/jur referente ao próprio estabelecimento \(opção 2\)\. 

__\[OS4747\]__ Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

# <a id="_Toc75782964"></a>Registro 1200 – Controle de Créditos Fiscais

RN1200

Os registros 1200  / 1210 são gerados a partir dos dados informados pelo usuário\. Para isso foram criadas telas de manutenção para que o usuário possa cadastrar a cada período de apuração, as informações a serem gravadas no Sped Fiscal\.

A manutenção destas informações é feita no módulo Sped Fiscal, através dos itens de menu:

*Parâmetros à Registros 1200/1210 \(Controle de Créditos\) \- Tipos de Utilização de Créditos Fiscais*

*Geração à Manutenção à Registros 1200/1210 \(Controle de Créditos\) à Registro 1200*

*Geração à Manutenção à Registros 1200/1210 \(Controle de Créditos\) à Registro 1210*

\(Inicialmente, não existe nenhum tipo de geração automática para os dados deste registro\)

Gravar um registro 1200 para cada código de ajuste informado para o período na tela de manutenção do item “Geração à Manutenção à Registros 1200/1210 \(Controle de Créditos\) à Registro 1200”\.

Poderão existir “n” registros 1200 para o período, diferenciados pelo código de ajuste\. 

__OBS1__: Para os códigos de ajuste em que existir valor de crédito utilizado no período \(campo 06\), o usuário deve informar os tipos de utilização para gerar os registros “filhos” 1210\. Caso contrário, o validador irá emitir mensagem de erro sobre a falta do\(s\) registro\(s\) filho\(s\)\.

__OBS2__: Na geração da opção “Geração – PIM”, deve\-se utilizar os dados cadastrados na opção própria dos usuários do PIM, no menu Geração – PIM à Manutenção à Registros 1200/1210 \(Controle de Créditos\), considerando apenas os dados cadastrados para a inscrição estadual em questão \(ver detalhes nas __OS2388\-AM\*__, que definiram a geração do Sped Fiscal para o PIM\)\.

# <a id="_Toc75782965"></a>Registro 1210 – Utilização de Créditos Fiscais

RN1210

Os registros 1200  / 1210 são gerados a partir dos dados informados pelo usuário\. Para isso foram criadas telas de manutenção para que o usuário possa cadastrar a cada período de apuração, as informações a serem gravadas no Sped Fiscal\.

A manutenção destas informações é feita no módulo Sped Fiscal, através dos itens de menu:

Geração à Manutenção à Registros 1200/1210 \(Controle de Créditos\) à Tipos de Utilização de Créditos Fiscais

Geração à Manutenção à Registros 1200/1210 \(Controle de Créditos\) à Registro 1200

Geração à Manutenção à Registros 1200/1210 \(Controle de Créditos\) à Registro 1210

Gravar “n” registros filhos 1210, para cada registro pai gravado no 1200\. Gravar todos os filhos informados no período, utilizando os dados informados na tela de manutenção do item “Geração à Manutenção à Registros 1200/1210 \(Controle de Créditos\) à Registro 1210”\.

Poderão existir “n” registros 1210 para cada registro 1200\. A diferença entre eles será o tipo de utilização de crédito \(campo 02\), o número do documento utilizado \(campo 03\) e a 

Chave do Documento Eletrônico \(campo 05\)\.

Obs: É obrigatória a informação do\(s\) registro\(s\) filho\(s\) 1210 nos casos em que existe valor de crédito utilizado no período \(campo 06 do registro 1200\)\.

RN1210\-05

Campo CHV\_DOCe:                \(campo criado pela __MFS7082__\) 

Este campo faz parte do registro 1210 apenas a partir da versão 1\.10 \(Jan/2017\)\.

O campo será preenchido com a informação do campo “Chave\-NFe” da tela de manutenção do registro 1210 \(conforme RN1210\)\.

# <a id="_Toc75782966"></a>Registro 1250 – Informações consolidadas de saldos de restituição,ressarcimento e complementação do ICMS

RN1250

Novo registro da versão 1\.13, Jan/2020 \(MFS31423\)\. Alterada pela \(MFS39109\)

Os registros 1250  / 1255 são gerados a partir dos dados informados pelo usuário ou pelo cálculo realizado no módulo Sped Fiscal através do item de Menu:Pré\-Geração *à *Ressarcimento ICMS\-ST \(Específico MG\)\. Para isso foi criada a tela de manutenção para que o usuário possa cadastrar/consultar a cada período de apuração, as informações a serem gravadas no Sped Fiscal\.

A manutenção destas informações é feita no módulo Sped Fiscal, através do item de menu:

*Geração à Manutenção à Registros 1255*

\(Inicialmente, não existe nenhum tipo de geração automática para os dados deste registro\)

Será gerado um registro por arquivo\.

RN1250\-02

Campo VL\_CREDITO\_ICMS\_OP:                

O campo será preenchido com o somatório do valor total do ICMS operação própria do registro 1255\.

Incluído \(MFS39109\)

Se o campo não possuir valor na tabela, preencher com zero\.

RN1250\-03

Campo VL\_ICMS\_ST\_REST:                

O campo será preenchido com o somatório do valor total do ICMS ST restituição do registro 1255\.

Incluído \(MFS39109\)

Se o campo não possuir valor na tabela, preencher com zero\.

RN1250\-04

Campo VL\_FCP\_ST\_REST:                

O campo será preenchido com o somatório do valor total do FCP\_ST restituição do registro 1255\.

Incluído \(MFS39109\)

Se o campo não possuir valor na tabela, preencher com zero\.

RN1250\-05

Campo VL\_ICMS\_ST\_COMPL:                

O campo será preenchido com o somatório do valor total do ICMS ST referente ao

complemento do imposto do registro 1255\.

Incluído \(MFS39109\)

Se o campo não possuir valor na tabela, preencher com zero\.

RN1250\-06

Campo VL\_FCP\_ST\_COMPL:                

O campo será preenchido com o somatório do valor total do FCP\_ST referente ao

complemento do imposto do registro 1255\.

Incluído \(MFS39109\)

Se o campo não possuir valor na tabela, preencher com zero\.

__Registro 1255 – Informações consolidadas de saldos de restituição, ressarcimento e complementação do ICMS por motivo__

RN1255

Novo registro da versão 1\.13, Jan/2020 \(MFS31423\)\. Alterada pela \(MFS39109\)

Os registros 1250  / 1255 são gerados a partir dos dados informados pelo usuário ou pelo cálculo realizado no módulo Sped Fiscal através do item de Menu:Pré\-Geração *à *Ressarcimento ICMS\-ST \(Específico MG\)\. Para isso foi criada a tela de manutenção para que o usuário possa cadastrar/consultar a cada período de apuração,  as informações a serem gravadas no Sped Fiscal\.

A manutenção destas informações é feita no módulo Sped Fiscal, através do item de menu:

*Geração à Manutenção à Registros 1255*

Gravar um registro 1255 para cada código de motivo informado para o período na tela de manutenção do item “Geração à Manutenção à Registros 1255”\.

Poderão existir “n” registros 1255 para o registro 1250\. A diferença entre eles será o código de motivo\.

RN1255\-3

Campo __VL\_CREDITO\_ICMS\_OP\_MOT__

Incluído \(MFS39109\)

Se o campo não possuir valor na tabela, preencher com zero\.

RN1255\-4

Campo __VL\_ICMS\_ST\_REST\_MOT__

Incluído \(MFS39109\)

Se o campo não possuir valor na tabela, preencher com zero\.

RN1255\-5

Campo __VL\_FCP\_ST\_REST\_MOT__

Incluído \(MFS39109\)

Se o campo não possuir valor na tabela, preencher com zero\.

RN1255\-6

Campo __VL\_ICMS\_ST\_COMPL\_MOT__

Incluído \(MFS39109\)

Se o campo não possuir valor na tabela, preencher com zero\.

RN1255\-7

Campo __VL\_FCP\_ST\_COMPL\_MOT__

Incluído \(MFS39109\)

Se o campo não possuir valor na tabela, preencher com zero\.

# <a id="_Toc75782967"></a>Registro 1300 – Movimentação Diária de Combustíveis

RN1300

Este registro será gerado a partir da nova tabela SAFX123\-Movimentação Diária por Tanque\.

Gerar um registro para cada dia e produto \(cada combustível\)\.

Este registro será a totalização da movimentação dos tanques que armazenam o mesmo produto\. Ou seja, será a totalização dos valores gravados no registro 1310, que demonstra a movimentação por tanque\. 

O produto gravado neste registro deverá ser gravado no registro 0200 \(Identificação dos Produtos\)\.

A identificação do produto armazenado no Tanque deve ser obtida na tabela dos tanques \(SAFX2060\), considerando a data de validade inicial, ou seja:

Produto = produto da linha da tabela de Tanques cuja validade seja a > data existente que seja <= a data da movimentação desejada \(data do movimento da SAFX123\); 

*\(Esta lógica da validade na SAFX2060 existe apenas para considerar a possibilidade de um Tanque passar a armazenar outro produto a partir de uma determinada data\. Esta possibilidade embora remota, pode acontecer\. Segundo consulta ao cliente Wall Mart esta alteração pode acontecer, mas é difícil e envolve vários procedimentos burocráticos\)\.*

__OBS1__: Os registros específicos dos revendedores varejistas de combustível \(1300 ao 1370, e o registro C171\) deverão ser selecionados no perfil de geração do Sped apenas no caso dos contribuintes deste segmento \(Postos de Gasolina\)\.

__OBS2__: este registro *não* tem o tratamento da Inscrição Estadual Única \(OS2388\-O1ge\), por entendermos que conceitualmente não se aplica\.

__OBS3__: Este registro não é gerado na opção “Geração – PIM” \(ver detalhes nas __OS2388\-AM\*__,  que definiram a geração do Sped Fiscal para o PIM\)\.

RN1300\-11

Campo FECH\_FISICO:

Este campo é o estoque final do dia\. Ele só deve ser calculado após a totalização da movimentação de todos os tanques do produto, ou seja, no momento de gravar o registro 1300, da seguinte forma:

FECH\_FISICO  = ESTQ\_ABERT \+  VOL\_ENTR – VOL\_SAIDAS – VAL\_AJ\_ PERDAS \+ VAL\_AJ\_GANHO

 

# <a id="_Toc75782968"></a>Registro 1310 – Movimentação Diária de Combustíveis por Tanque  

RN1310

Este registro será gerado a partir da nova tabela SAFX123\-Movimentação Diária por Tanque\.

Para cada registro 1300 \(data e produto\), o registro 1310 mostrará a movimentação detalhada por tanque\. 

Deverá ser gerado um registro para o detalhamento da movimentação de cada tanque\. Com a SAFX123 já tem a movimentação por data e tanque, deve\-se gerar um registro 1310 para cada registro da tabela\. 

O valor final do estoque no dia também não consta na tabela SAFX123, e deverá ser calculado da seguinte forma:

  Estoque Final  = Estoque Inicial \+ Entradas – Saídas – Perdas \+ Ganhos

__OBS__: Os registros específicos dos revendedores varejistas de combustível \(1300 ao 1370, e o registro C171\) deverão ser selecionados no perfil de geração do Sped apenas no caso dos contribuintes deste segmento \(Postos de Gasolina\)\.

RN1310\-10

Campo FECH\_FISICO:

Este campo é o estoque final do dia, a ser calculado da seguinte forma:

FECH\_FISICO  = ESTQ\_ABERT \+  VOL\_ENTR – VOL\_SAIDAS – VAL\_AJ\_ PERDAS \+ VAL\_AJ\_GANHO

RN1310\-11

Campo CAP\_TANQUE

__\[MFS861835\] Campo incluído pelo layout 1\.19 \(jan/2026\)\.__

__\[MFS861834\] Preenchimento do campo 11 com a Capacidade \(em litros\) da SAFX2060\.__

- __Para Geração c/ leiaute anterior a EFD119 \(CAD\_LAYOUT – COD\_VERSAO<119\):__

       Esse campo não deve ser gerado\.

- __Para Geração c/ leiaute a partir da EFD119 \(CAD\_LAYOUT – COD\_VERSAO>=119\):__

__       Campo incluído a partir da versão de layout 1\.19 \(jan/2026\)__

__       MFS861835__: 

       Inclusão do Campo 11 na estrutura do registro 1310\. 

__       MFS861834:__

       Preencher com o conteúdo do campo 07 \- Capacidade \(em litros\) da SAFX2060\.

       Caso o campo 07 \- Capacidade \(em litros\) da SAFX2060 não esteja preenchido, gravar 

        zero no campo 11 do registro 1310\.

# <a id="_Toc75782969"></a>Registro 1320 – Volume de Vendas

RN1320

Este registro será gerado a partir das novas tabelas SAFX122 – Relacionamento Tanques x Bicos e SAFX124 – Vendas Diárias\.

Este registro mostra os valores de abertura e fechamento de cada bico do tanque gravado no registro 1310\.

O relacionamento dos Bicos de cada Tanque deve ser obtido na SAFX122, que tem a informação de quais tanques alimentam os bicos\. Os valores de cada bico serão obtidos na SAFX124\. 

Para cada bico, poderão existir vários registros 1320, o que dependerá do número de procedimentos de abertura/fechamento realizados no dia\. 

\(em condições normais, haverá um único registro pode dia, mas no caso de qualquer intervenção na Bomba, poderá ocorrer mais de um procedimento no dia, como por exemplo em caso de manutenção ou fiscalização\)

O volume total das vendas \(campo 11\-VOL\_VENDAS\) não consta na tabela SAFX124, e deverá ser calculado da seguinte forma:

  Total Vendas  = Contador Final  –  Contador Inicial  –  Aferições 

__OBS__: Os registros específicos dos revendedores varejistas de combustível \(1300 ao 1370, e o registro C171\) deverão ser selecionados no perfil de geração do Sped apenas no caso dos contribuintes deste segmento \(Postos de Gasolina\)\.

RN1320\-11

Campo VOL\_VENDAS:

Este campo é o total das vendas do dia, a ser calculado da seguinte forma:

     Total Vendas = Contador Final  –  Contador Inicial  –  Aferições

             \(VOL\_VENDAS  =  VAL\_FECH  –  VAL\_ABERT  –  VOL\_AFERI\)

# <a id="_Toc75782970"></a>Registro 1350 \- Bombas

RN1350

Este registro será gerado a partir da nova tabela SAFX2061 – Bombas\.

Gerar um registro para cada bomba cadastrada na SAFX2061 p/o Estabelecimento\.

*O PVA não cita detalhes sobre a geração deste registro, então, inicialmente iremos gerar o registro para todas as Bombas existentes, independente de existir ou não movimentação para a mesma no período\.*

*Desconsiderar apenas as bombas com data de validade \(campo 4 da SAFX2061\) superior a data final do período de geração \(data final do registro 0000\-Abertura do Arquivo\)\.*

__Alteração da OS4139__:

A partir desta OS, este registro passa a apresentar *apenas* as Bombas com movimento no período\. Assim, para cada Bomba recuperada da SAFX2061 \(considerando a Empresa e o Estabelecimento em questão\), será verificada a ocorrência de movimento na tabela das vendas diárias \(SAFX124\), da seguinte forma:

SAFX124

Empresa – empresa da SAFX2061

Estabelecimento – estabelecimento da SAFX2061

Data do Movimento – deve ser uma data compreendida no período informado p/geração do SPED 

Número da Bomba – número da Bomba da SAFX2061  

Caso *não* seja identificado nenhum movimento no período, a Bomba *não* será gerada neste registro, e consequentemente, não haverão também os registros “filhos” 1360 e 1370\.

__OBS__: Os registros específicos dos revendedores varejistas de combustível \(1300 ao 1370, e o registro C171\) deverão ser selecionados no perfil de geração do Sped apenas no caso dos contribuintes deste segmento \(Postos de Gasolina\)\.

__OBS__: este registro *não* tem o tratamento da Inscrição Estadual Única \(OS2388\-O1ge\), por entendermos que conceitualmente não se aplica\.

# <a id="_Toc75782971"></a>Registro 1360 – Lacres da Bomba

RN1360

Este registro será gerado a partir da nova tabela SAFX121 – Lacres das Bombas\.

Para cada Bomba gravada no registro 1350, poderão existir ‘n’ lacres, conforme a relação entre a tabela de Bombas \(SAFX2061\) e a tabela dos lacres \(SAFX121\)\. 

Gerar um registro para cada lacre existente, considerando *apenas* os lacres com data  \(campo 04\-Data do Lacre da SAFX121\) menor ou igual à data final do período de geração \(data final gravada no registro 0000\-Abertura do Arquivo\)\. 

__OBS__: Os registros específicos dos revendedores varejistas de combustível \(1300 ao 1370, e o registro C171\) deverão ser selecionados no perfil de geração do Sped apenas no caso dos contribuintes deste segmento \(Postos de Gasolina\)\.

# <a id="_Toc75782972"></a>Registro 1370 – Bicos da Bomba

RN1370

Este registro será gerado a partir das novas tabelas SAFX2062 \- Bicos e SAFX122 \-Relacionamento Tanques x Bicos\.

Para cada Bomba gravada no registro 1350, poderão existir vários Bicos\. Deverá ser gerado um registro 1370 para cada bico da bomba existente na SAFX2062\. 

*Considerar apenas os registros com validade \(campo 5 da SAFX2062\) menor ou igual à data final do período de geração \(data fim do registro 0000\-Abertura do Arquivo\)\. *

__Alteração da OS4139__:

A partir desta OS, este registro passa a apresentar *apenas* os Bicos com movimento no período, junto com a Bomba em questão\. Assim, para cada Bico recuperado da SAFX2062 \(considerando a Empresa, o Estabelecimento e a Bomba\), será verificada a ocorrência de movimento na tabela das vendas diárias \(SAFX124\), da seguinte forma:

SAFX124

Empresa – empresa da SAFX2062

Estabelecimento – estabelecimento da SAFX2062

Data do Movimento – deve ser uma data compreendida no período informado p/geração do SPED 

Número da Bomba – número da Bomba do registro “pai” 1350

Número do Bico – número do Bico da SAFX2062  

Caso *não* seja identificado nenhum movimento no período \(para este Bico \+ Bomba do registro “pai”\), o Bico *não* será gerado neste registro\.

A informação do tanque e do combustível deverão ser obtidas na tabela de relacionamento entre Tanques x Bicos\. Considerando apenas os registros de relacionamento com validade \(campo 6 da SAFX122\) menor ou igual à data final do período de geração \(data fim do registro 0000\-Abertura do Arquivo\)\.  

__OBS__: Os registros específicos dos revendedores varejistas de combustível \(1300 ao 1370, e o registro C171\) deverão ser selecionados no perfil de geração do Sped apenas no caso dos contribuintes deste segmento \(Postos de Gasolina\)\.

# <a id="_Toc75782973"></a>Registro 1390 – CONTROLE DE PRODUÇÃO DE USINA

__			__

__RN1390__

__Regra Geral__

Estes registros serão gerados a partir dos produtos parametrizados em “__Módulo__: SPED à EFD – Escrituração Fiscal Digital, __Menu__: Parâmetros à Registro 1390/1391 à Produto” e também através das movimentações de produção diária do período\.

Gerar um registro 1390 sempre que houver produção ou saldo anterior de “Açúcar”, “Álcool Anidro” ou “Álcool Hidratado”\. 

O “Mel Residual” existe na parametrização acima citada, mas não gera registro1390 e sim compõe o registro 1391 do registro 1390 da “Açúcar”\.

__MFS\-34707\- Introdução: __cria os resíduos Bagaço da Cana, DDG, WDG na parametrização dos produtos \(__Menu__: Parâmetros à Registro 1390/1391 à Produto\), mas não geram registro1390 e sim compõe o registro 1391 do registro 1390 dos grupos de produtos \(“Açúcar”, “Álcool Anidro” ou “Álcool Hidratado”\)\. Algumas ponderações:

1. O Bagaço da Cana foi definido como um resíduo proveniente da produção de Açúcar, Álcool Anidro e Álcool Hidratado\. 
2. Já DDG e WDG foram definidos como resíduos apenas do processo produtivo de Álcool Anidro e Álcool Hidratado\. Para tal definição, me baseei em pesquisas realizadas na internet, mas não obtive informação de fontes oficiais\. A COSAN explicou que esses resíduos são da produção de etanol \(álcool\) quando usado milho como insumo\.

Se futuramente algum cliente solicitar alteração na solução para tratar esses resíduos oriundos da produção do Açúcar, essa definição deve ser reavaliada\.

1. As quantidades dos resíduos devem ser informadas separadamente para cada grupo de produto do registro pai 1390 \(“Açúcar”, “Álcool Anidro” e “Álcool Hidratado”\)\. Para isso, criamos três grupos para Bagaço de Cana \(Bagaço de Cana – Açúcar, Bagaço de Cana \- Anidro e Bagaço de Cana \- Hidratado\), dois para DDG \(DDG –Anidro e DDG Hidratado\) e dois para WDG \(WDG \- Anidro e WDG \- Hidratado\)\.  
2. As quantidades de resídulos do Bagaço da Cana, DDG e WDG devem ser carregadas na tabela Movimentação de Produção \(SAFX16\)\. Consultei dois clientes BIOSEV e COSAN para desenhar a solução e ambas só possuem resíduo de Bagaço da Cana e carregam\-o na SAFX16\. 

  

__Alteração da MFS1401__:  A partir desta OS o saldo anterior passou a ser também um critério para gravação do registro\. Assim, o registro passou a ser gravado para todos os grupos que tiverem movimentação no período \(produção/estoque\) __ou__ saldo inicial\. Desta forma, só não serão gravados os grupos que não apresentarem nem saldo inicial nem movimentação no período \(produção ou  estoque\)\.

A movimentação / produção diária do “grupo” gravado no 1390 será registrada no registro 1391, através das seguintes tabelas:

SAFX10 à Movimentação de Estoque

SAFX16 à Produção

SAFX17 à Insumos utilizados na Produção

SAFX52 à Inventário

Registro deve ser gerado apenas a partir da versão EFD105 do leiaute \(Julho/2012\)

__Alteração da MFS2232__:  A partir desta MFS o processo de produção da Cana Moída será gerada a partir da SAFX16/17 ou a partir da SAFX10\. Foi criada a parametrização “Gerar os registros a partir do movimento de estoque \(SAFX10\)” no item Registros 1390/1391 na tela de Dados Iniciais do módulo do SPED Fiscal para que o usuário defina a origem da informação dos dados, quando a opção estiver marcada serão considerados os dados da SAFX10, caso contrário considerará os dados das SAFX16/17, como é feito atualmente\. Assim, como o processo da Cana Moída por movimento de estoque não considera insumos, pois já trás o processo como um todo, foram criadas novas opções para Grupo Produto para distinguir a operação: Cana Moída – Anidro, Cana Moída – Hidratado e Cana Moída – Açucar\. Com isso, o Registro 1390 deve gravar um registro para cada “grupo” de produto\. O conceito de “grupo” para este registro é o seguinte:

\- Cana Moída – Açucar = Açúcar

\- Cana Moída – Anidro = Álcool Anidro

\- Cana Moída – Hidratado = Álcool Hidratado

__*Resumindo: *__

Temos os seguintes grupos de produtos:

AÇÚCAR

ÁLCOOL ANIDRO

ÁLCOOL HIDRATADO

CANA MOÍDA

MEL RESIDUAL

Bagaço da Cana – Açúcar 

Bagaço da Cana – Anidro

Bagaço da Cana – Hidratado

DDG – Anidro

DDG – Hidratado

WDG – Anidro

WDG – Hidratado

CANA MOÍDA \- ANIDRO

CANA MOÍDA \- HIDRATADO

CANA MOÍDA \- AÇUCAR

Para cada um destes “grupos” existirá uma relação de produtos associados\. Esta associação é feita através da parametrização do menu “Parâmetros à Registro 1390/1391 à Produtos”\.

A parametrização “Gerar os registros a partir do movimento de estoque \(SAFX10\)” determina uma diferença em relação ao uso do grupo de produto “Cana Móída”\. Se o parâmetro estiver desmarcado, considera\-se o grupo “Cana Móída”\. Se estiver marcado, considera\-se os grupos Cana Moída \- Açúcar 

Cana Moída – Anidro e Cana Moída – Hidratado\.

 Veja a relação dos grupos de produtos com o produto produzido apresentado no registro 1390:

Parâmetro “Gerar os registros a partir do movimento de estoque \(SAFX10\)”

Conjunto de Grupos de Produtos

\(disponíveis na parametrização do menu “Parâmetros à Registro 1390/1391 à Produtos”\)

Registro 1390

\(COD\_PROD\)

N \- Não

Açúcar 

Cana Móida

Mel Residual

Bagaço da Cana – Açúcar

03 \- Açúcar 

N \- Não

Álcool Anidro

Cana Móida

Bagaço da Cana – Anidro

DDG – Anidro

WDG – Anidro

02 \- Álcool Anidro

N \- Não

Álcool Hidratado

Cana Móida

Bagaço da Cana – Hidratado

DDG – Hidratado

WDG – Hidratado

01 \- Álcool Hidratado

S \- Sim

Açúcar 

Cana Moída \- Açúcar 

Mel Residual

Bagaço da Cana – Açúcar

03 \- Açúcar 

S \- Sim

Álcool Anidro

Cana Moída – Anidro

Bagaço da Cana –  Anidro

DDG – Anidro

WDG – Anidro

02 \- Álcool Anidro

S \- Sim

Álcool Hidratado

Cana Moída – Hidratado

Bagaço da Cana – Hidratado

DDG – Hidratado

WDG – Hidratado

01 \- Álcool Hidratado

Será gravado __um único registro 1390 para AÇÚCAR, ÁLCOOL ANIDRO e ÁLCOOL HIDRATADO__, a partir de um conjunto de “grupos”, mas *apenas* os grupos que tiverem movimentação no período, ou saldo inicial\. Ou seja, apenas os grupos cujos produtos apresentem movimentação de estoque no período \(SAFX10\), registro de produção no período \(SAFX16/17\), ou saldo inicial\.

__Alteração da MFS77290__:  O estado de __Alagoas__ divulgou novos produtos a serem apresentados no registro 1390\. O produto 03 \- AÇÚCAR a partir de __01/01/2022 __não deve ser gerado e no seu lugar entraram os produtos __04 – AÇUCAR MASCAVO, 05 – AÇÚCAR DEMERARA, 06 – AÇÚCAR CRISTAL, 07 – OUTROS AÇÚCARES__\. Também foram incluídos os produtos __08 – ÁLCOOL PARA OUTROS FINS__ e __09 – MEL__\. Foram mantidos os produtos __01 – ÁLCOOL HIDRATADO e 02\- ÁLCOOL ANIDRO\. No momento não faremos a geração do 09 – MEL\.__

Veja a relação dos grupos de produtos com os novos produtos incluídos para Alagoas a serem apresentados no registro 1390:

Parâmetro “Gerar os registros a partir do movimento de estoque \(SAFX10\)”

Conjunto de Grupos de Produtos

\(disponíveis na parametrização do menu “Parâmetros à Registro 1390/1391 à Produtos”\)

Registro 1390

\(COD\_PROD\)

N \- Não

Açúcar Mascavo

Cana Móida

Mel Residual – Açúcar Mascavo

Bagaço da Cana – Açúcar Mascavo

04 \- Açúcar Mascavo

N \- Não

Açúcar Demerara

Cana Móida

Mel Residual – Açúcar Demerara

Bagaço da Cana – Açúcar Demerara

05 \- Açúcar Demerara

N \- Não

Açúcar Cristal

Cana Móida

Mel Residual – Açúcar Cristal

Bagaço da Cana – Açúcar Cristal

06 \- Açúcar Cristal

N \- Não

Outros Açúcares 

Cana Móida

Mel Residual – Outros Açúcares

Bagaço da Cana – Outros Açúcares

07 – Outros Açúcares

N \- Não

Álcool para outros fins

Cana Móida

Bagaço da Cana – Álcool para outros fins

DDG – Álcool para outros fins

WDG – Álcool para outros fins

08 \- Álcool para outros fins

N \- Não

09 – Mel

\(por enquanto não vamos gerar\)

S \- Sim

Açúcar Mascavo

Cana Móida \- Açúcar Mascavo

Mel Residual – Açúcar Mascavo

Bagaço da Cana – Açúcar Mascavo

04 \- Açúcar Mascavo

S \- Sim

Açúcar Demerara

Cana Móida \- Açúcar Demerara

Mel Residual – Açúcar Demerara

Bagaço da Cana – Açúcar Demerara

05 \- Açúcar Demerara

S \- Sim

Açúcar Cristal

Cana Móida \- Açúcar Cristal

Mel Residual – Açúcar Cristal

Bagaço da Cana – Açúcar Cristal

06 \- Açúcar Cristal

S \- Sim

Outros Açúcares 

Cana Móida \- Outros Açúcares

Mel Residual – Outros Açúcares

Bagaço da Cana – Outros Açúcares

07 – Outros Açúcares

S \- Sim

Álcool para outros fins

Cana Móida \- Álcool para outros fins

Bagaço da Cana – Álcool para outros fins

DDG – Álcool para outros fins

WDG – Álcool para outros fins

08 \- Álcool para outros fins

S \- Sim

09 – Mel

\(por enquanto não vamos gerar\)

\[__MFS77290__\] – <a id="ACUCAR"></a>Tratamento da Vigência para o Açúcar \(Alagoas\)

Para o estabelecimento de __Alagoas__ será necessário verificar a data da geração, para determinar qual  produto será considerado na geração do 1390 para o açúcar: o 03\-AÇÚCAR ou os produtos 04\-AÇÚCAR MASCAVO, 05\-AÇÚCAR DEMERARA, 06\-AÇÚCAR CRISTAL e 07\-OUTROS AÇÚCARES\.

Se a Data Inicial informada na tela de geração for anterior a 01/01/2022, então:

   Considera o produto 03 – Açúcar na geração do 1390\.

   Não considerar os produtos 04 – Açúcar Mascavo, 05 – Açúcar Demerara, 06 – Açúcar Cristal, 07 – Outros Açúcares\.

Se a Data Inicial informada na tela de geração for maior ou igual a 01/01/2022, então:

   Não considerar o produto 03 – Açúcar na geração do 1390\.

   Considerar os produtos 04 – Açúcar Mascavo, 05 – Açúcar Demerara, 06 – Açúcar Cristal, 07 – Outros Açúcares\.

__RN1390\-02__

__Campo COD\_PROD__

Indicar a classificação do produto, cuja produção diária será registrada no registro 1391:

Gerar o código “01” para produção de “Álcool Etílico Hidratado Carburante”;

Gerar o código “02” para produção de “Álcool Etílico Anidro Carburante”;

Gerar o código “03” para produção de “Açúcar”\.

__Alteração da MFS77290__:  O estado de __Alagoas__ divulgou novos produtos a serem apresentados no registro 1390:

Gerar o código “04” para produção de “Açúcar Mascavo”\.

Gerar o código “05” para produção de “Açúcar Demerara”\.

Gerar o código “06” para produção de “Açúcar Cristal”\.

Gerar o código “07” para produção de “Outros Açúcares”\.

Gerar o código “08” para produção de  “Álcool para outros fins”\.

Gerar o código “09” para produção de  “Mel”\. \(por enquanto não vamos gerar\)

Sendo que o código 03 – Açúcar se mantém sendo gerado até 31/12/2021\. E a partir de 01/01/2022 passam a ser gerados os codigos 04\-Açúcar Mascavo, 05\- Açúcar Demerara, 06\-Açúcar Cristal e 07\- Outros Açúcares\.

__Alteração da MFS2232__:  

Esta classificação corresponde ao campo “Grupo Produto” da parametrização dos produtos \(menu Parâmetros à Registro 1390/1391 à Produtos\)\. 

\- O “Mel Residual” é considerado como 03 \- “Açúcar”\.

\- A “Cana Moída – Açucar” é considerado como 03 \- Açúcar

\- A “Cana Moída – Anidro” é considerado como 02 \- Álcool Anidro

\- A “Cana Moída – Hidratado” é considerado como 01 \- Álcool Hidratado

__MFS\-34707__:  

Os Grupos de Produtos relacionados aos resíduos, são gerados no registro 1390 com o seguinte código de produto:

\- O “Bagaço da Cana – Açúcar” é considerado como 03 \- Açúcar

\- O “Bagaço da Cana – Anidro” é considerado como 02 \-Álcool Anidro

\- O “Bagaço da Cana – Hidratado” é considerado como 01 \- Álcool Hidratado

\- O “DDG – Anidro” é considerado como 02 \- Álcool Anidro

\- O “DDG – Hidratado” é considerado como 01 \- Álcool Hidratado

\- O “WDG – Anidro” é considerado como 02 \- Álcool Anidro

\- O “WDG – Hidratado” é considerado como 01 \- Álcool Hidratado

__Alteração da MFS77290__:  

Novos Grupos de Produtos da parametrização dos produtos para Alagoas \(menu Parâmetros à Registro 1390/1391 à Produtos\), que serão gerados no registro 1390 com o seguinte código de produto:

\- Cana Móida \- Açúcar Mascavo é considerado como 04 \- Açúcar Mascavo

\- Mel Residual – Açúcar Mascavo é considerado como 04 \- Açúcar Mascavo

\- Bagaço da Cana – Açúcar Mascavo é considerado como 04 \- Açúcar Mascavo

\- Cana Móida \- Açúcar Demerara é considerado como 05 \- Açúcar Demerara

\- Mel Residual – Açúcar Demerara é considerado como 05 \- Açúcar Demerara

\- Bagaço da Cana – Açúcar Demerara é considerado como 05 \- Açúcar Demerara

\- Cana Móida \- Açúcar Cristal é considerado como 06 \- Açúcar Cristal

\- Mel Residual – Açúcar Cristal é considerado como 06 \- Açúcar Cristal

\- Bagaço da Cana – Açúcar Cristal é considerado como 06 \- Açúcar Cristal

\- Cana Móida \- Outros Açúcares é considerado como 07 – Outros Açúcares

\- Mel Residual – Outros Açúcares é considerado como 07 – Outros Açúcares

\- Bagaço da Cana – Outros Açúcares é considerado como 07 – Outros Açúcares

\- Cana Móida \- Álcool para outros fins é considerado como 08 \- Álcool para outros fins

\- Bagaço da Cana – Álcool para outros fins é considerado como 08 \- Álcool para outros fins

\- DDG – Álcool para outros fins é considerado como 08 \- Álcool para outros fins

\- WDG – Álcool para outros fins é considerado como 08 \- Álcool para outros fins

__Atenção:__ a opção do Grupo Produto Cana Moída permanecerá na listagem, porém será utilizada para o processo da SAFX16/17\.

# <a id="_Toc75782974"></a>Registro 1391 – PRODUÇÃO DIÁRIA DA USINA

__RN1391__

__Regra Geral__

Estes registros serão gerados a partir dos produtos parametrizados em “__Módulo__: SPED à EFD – Escrituração Fiscal Digital, __Menu__: Parâmetros à Registro 1390/1391 à “Produto” e “Operações”\. Além de também buscar as movimentações de produção diária do período\.

Este registro deve ser apresentado para detalhar a movimentação/produção diária de cada “grupo” de  produto especificado no registro 1390\.

Não pode haver mais de um registro com a mesma data de produção\.

__Alteração da MFS1401__: A partir desta OS o registro 1391 passou a ser gravado __diariamente__, mesmo para os dias em que *não* existir movimentação \(nem produção nem estoque\)\. Nesses casos, o registro é gravado apenas com a informação dos campos de saldo: campo 04\-ESTQ\_INI, campo 12\_ESTQ\_FIN, e campo 13\-ESTQ\_INI\_MEL \(no caso dos grupos 03\-Açúcar, \[__MFS77290__\] 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal, 07 – Outros Açúcares\)\. Demais campos, referentes à movimentação do período, serão gerados com zeros\.

Registro deve ser gerado apenas a partir da versão EFD105 do leiaute \(Julho/2012\)

__\[ALTERADA – CH24790\_2015\]__

__\[Alteração – CH25861\-A\_2012\] \- __Somente considerar o estoque quando o campo 05 – GRUPO\_CONTAGEM \(SAFX10\) = 1 e 3\.

__Alteração da MFS31407__: Incluídos os campos 18, 19 e 20 \(versão 1\.13 do Sped, Jan/2020\)

__Alteração da MFS34707__: Alteração os campos 19 e 20 \(versão 1\.13 do Sped, Jan/2020\)

__*Resumindo: *__

Este registro é “filho” do registro 1390\. 

Para cada registro “pai” 1390, poderão ser gravados ‘n’ registros 1391, sendo __um para cada dia do período__, desde que exista movimentação na data\.

Origem dos Dados:

         \- SAFX10 – Movimentação de Estoque

         \- SAFX16/SAFX17 – Produtos Fabricados e Insumos Utilizados

         \- SAFX52 – Inventário

__Para cada data__ será feita a totalização das quantidades movimentadas __ou__ produzidas no dia\.

Cada registro 1391 é referente a uma determinada data, e que conterá na verdade, as quantidades referentes à todos os produtos associados ao “grupo” do registro pai 1390\.  

*\(observar que em nenhum dos dois registros existe a informação da identificação dos produtos\)*

Em relação à movimentação de estoque \(__SAFX10__\), serão considerados *apenas* os movimentos cuja Operação e Produto constem na parametrização do Sped\.

Em relação ao registro da produção \(__SAFX16__/__SAFX17__\), serão considerados *apenas* os movimentos cujo Produto  conste na parametrização do Sped\. Os insumos da SAFX17 também serão considerados apenas quando constarem da parametrização\.

Assim, as quantidades solicitadas no registro 1391 ora virão da movimentação do estoque, ora da produção, dependendo do campo\. Para entender o conteúdo de cada campo, deve\-se verificar as regras específicas de cada um\.   O importante é entender que cada campo de quantidade será o resultado da totalização de quantidades específicas de ‘n’ produtos, que serão os produtos associados ao “grupo” do registro pai 1390\.

__RN1391\-02__

__Campo DT\_REGISTRO__

Recuperar a data conforme a movimentação do registro\.

__RN1391\-03__

__Campo QTD\_MOID__

__Alteração da MFS2232__:  

Dependendo da opção “Gerar os registros a partir do movimento de estoque \(SAFX10\)” escolhida, este campo será gerado de uma das origens:

\- Tabela de Movimentação da Produção \(SAFX16/SAFX17\), 

\- Tabela de Movimentação de Estoque \(SAFX10\)\. 

__ORIGEM 1:__

Quando a opção “Gerar os registros a partir do movimento de estoque \(SAFX10\)” no item Registros 1390/1391 na tela de Dados Iniciais estiver marcado, seguir com a seguinte verificação e geração:

O conteúdo deste campo será a totalização da quantidade da cana moída utilizada no processo de produção por grupo produto: Cana Moída – Anidro, Cana Moída – Hidratado ou Cana Moída – Açucar, \[__MFS77290__\] Cana Móida \- Açúcar Mascavo, Cana Móida \- Açúcar Demerara, Cana Móida \- Açúcar Cristal, Cana Móida \- Outros Açúcares, Cana Móida \- Álcool para outros fins\.

__*Resumindo: *__

__Origem dos Dados__: SAFX10

__Conteúdo__:

Verifica se existe, na data de geração do arquivo magnético, movimento de estoque com utilização de cana moída para produção de "Álcool Etílico Hidratado Carburante”, “Álcool Etílico Anidro Carburante” e “Açúcar” \(__SAFX10__\) de produtos parametrizados no Sped, e associados ao “grupo” do registro pai 1390\.

Caso existam produtos na __SAFX10__, totalizar a quantidade utilizada __\(\*\)__ da cana moída parametrizada no Sped com a classificação =  “__Cana Moída – Anidro”, “Cana Moída – Hidratado”, “Cana Moída – Açucar” ou __\[__MFS77290__\] Cana Móida \- Açúcar Mascavo, Cana Móida \- Açúcar Demerara, Cana Móida \- Açúcar Cristal, Cana Móida \- Outros Açúcares, Cana Móida \- Álcool para outros fins\.

__\[MFS77290__\]

Para o estabelecimento de __Alagoas__ será necessário verificar a data da geração, para determinar qual  produto será considerado na geração do 1390 para o açúcar: o 03\-AÇÚCAR ou os produtos 04\-AÇÚCAR MASCAVO, 05\-AÇÚCAR DEMERARA, 06\-AÇÚCAR CRISTAL e 07\-OUTROS AÇÚCARES\.

Se a Data Inicial informada na tela de geração for anterior a __01/01/2022__, então:

   Considera o produto __Cana Moída – Açucar__\.

   Não considerar os produtos Cana Móida \- Açúcar Mascavo, Cana Móida \- Açúcar Demerara, Cana Móida \- Açúcar Cristal e Cana Móida \- Outros Açúcares\.

Se a Data Inicial informada na tela de geração for maior ou igual a __01/01/2022__, então:

   Não considerar o produto Cana Moída – Açucar\.

   Considerar os produtos Cana Móida \- Açúcar Mascavo, Cana Móida \- Açúcar Demerara, Cana Móida \- Açúcar Cristal e Cana Móida \- Outros Açúcares\.

__\(\*\)__ campo “20 \- Quantidade” da SAFX10

A informação deste campo será considerada para o produto do campo 02 no registro 1390 igual a:

\- 01 \(Álcool Hidratado\) p/ o grupo produto “__Cana Moída – Hidratado”__

\- 02 \(Álcool Anidro\) p/ o grupo produto “__Cana Moída – Anidro”__

\- 03 \(açúcar\) p/ o grupo produto “__Cana Moída – Açucar__”

\- 04 \(Açúcar Mascavo\) p/ o grupo produto “Cana Móida \- Açúcar Mascavo”

\- 05 \(Açúcar Demerara\) p/ o grupo produto“Cana Móida \- Açúcar Demerara” 

\- 06 \(Açúcar Cristal\) p/ o grupo produto“Cana Móida \- Açúcar Cristal” 

\- 07 \(Outros Açúcares\) p/ o grupo produto “Cana Móida \- Outros Açúcares”

\- 08 \(Álcool para outros fins\) p/ o grupo produto “Cana Móida \- Álcool para outros fins”

Exemplo:

Emp

Docto

Item

Data

__Material__

__Qtde__

__Uni__

Mov

Prod

TESTE

49229

1

29/09/2015

__7AN__

__11418240000__

__T__

EWR261

3011402

TESTE

49229

2

29/09/2015

__7HI__

__25707040000__

__T__

EWR261

3011402

TESTE

49229

3

29/09/2015

__7AC__

__4578720000__

__T__

EWR261

3011402

Será separado por produção para corresponder corretamente a cada grupo pertencente no Registro 1390\.

__Alteração da OS4070 \(Conversão de Medida\):__

Caso a unidade de medida do insumo não seja tonelada \(campo “33\-Unidade de Medida” da SAFX10  <> ‘t’ e <> ‘T’\) será feita a conversão da quantidade para tonelada, *antes de totalizar o seu valor*\.

Verificar na __RN1391\-99__ as regras para conversão\.

__ORIGEM 2:__

Quando a opção “Gerar os registros a partir do movimento de estoque \(SAFX10\)” no item Registros 1390/1391 na tela de Dados Iniciais estiver desmarcado, seguir com a seguinte verificação e geração:

O conteúdo deste campo será a totalização da quantidade de todos os insumos utilizados na produção dos produtos parametrizados no Sped e associados ao “grupo” do registro pai 1390\. 

Nesta totalização são considerados *apenas* os insumos também parametrizados no Sped e classificados como "Cana moída"

__*Resumindo: *__

__Origem dos Dados__: SAFX16/SAFX17

__Conteúdo__:

__\[MFS34479\]__ Inclusão da validação da quantidade

Verifica se existem, na data, registros de produção \(__SAFX16__\) de produtos parametrizados no Sped, e associados ao “grupo” do registro pai 1390 e que a quantidade \(campo 07 \- Quantidade\) seja maior que zeros\. “Grupo” do registro pai 1390 = 01 \- “Álcool Etílico Hidratado Carburante”,  02 \- “Álcool Etílico Anidro Carburante”; 03\-Açúcar, \[__MFS77290__\] 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal, 07 – Outros Açúcares, 08 \- “Álcool para outros fins”\. Lembrando que para estabelecimentos de Alagoas, de acordo com a data da geração, será considerado ou o produto 03\-Açúcar ou os produtos 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal e 07 – Outros Açúcares \(vide regra [RN1390](#ACUCAR)\)\.

Caso existam produtos na __SAFX16__, serão pesquisados os insumos utilizados na produção desses produtos \(__SAFX17__\), e totalizada a quantidade utilizada __\(\*\)__ dos insumos parametrizados no Sped com a classificação =  “__Cana Moída__”\.

__\(\*\)__ campo “09\-Quantidade” da SAFX17

__Alteração da OS4070 \(Conversão de Medida\):__

Caso a unidade de medida do insumo não seja tonelada \(campo “08\-Unidade de Medida” da SAFX17  <> ‘t’ e <> ‘T’\) será feita a conversão da quantidade para tonelada, *antes de totalizar o seu valor*\.

Verificar na __RN1391\-99__ as regras para conversão\.

__Alteração da OS4446 \(Sobre a totalização das quantidades de cana utilizadas\):__

*\(esta OS retirou a obrigatoriedade da parametrização dos subprodutos componentes da fórmula para que eles sejam considerados na pesquisa da cana moída utilizada\)*

A pesquisa dos componentes para totalizar a quantidade de cana moída utilizada é feita considerando *todos* os componentes do produto final \(produto parametrizado como Álcool ou Açúcar\)\.

Os componentes \(sejam eles insumos ou subprodutos\), *não* precisam estar parametrizados no Sped\. Independente de parametrização, todos os componentes entram na pesquisa\. Os únicos componentes que precisam estar parametrizados, são aqueles que são cana moída, pois é desta forma que a geração identifica o que é cana moída\.

Exemplo:

Considerando a seguinte parametrização:

\-Produtos associados à classe do “Álcool Hidratado” à __Alcool Tipo1 __e__ Alcool Tipo2__

\-Produtos associados à classe “Cana Moída” à __CANA\-1__

          Composição dos produtos na SFAX16/SAFX17:

__Produto__

__Qtd__

__Produto__

__Qtd__

__Alcool Tipo1__     

500,00 lit

Água Destilada               

250,00 Lit

HBO

100,00 Lit

XYZ

150,00 Lit      

__Alcool Tipo2__     

1\.000,00 lit

Água Destilada               

850,00 Lit          

HBO

250,00 Lit

__CANA\-1__                           

2,50 Ton

XYZ

100,00 Lit

Água Destilada                

50,00 Lit

__CANA\-1__                            

0,50 Ton  

*\(ver detalhes e maiores explicações sobre este exemplo no item “1\-Informação” da OS4416\)*

	

Neste caso, a quantidade total da cana moída considera a cana utilizada como insumo “direto” do produto “__Álcool Tipo2__”, e também a cana utilizada na composição do produto XYZ, já que este produto XYZ é um componente do “__Álcool Tipo1”\.__

__RN1391\-04__

__Campo ESTQ\_INI__

__\[OS3736 – Alteração e OS3736\-A\]__

Para o primeiro dia do movimento, recuperar a Data do Saldo Inicial LPD \(Cotepe 41\) da tela de geração, considerando lançamento do inventário \(SAFX52\) com a mesma data indicada \(campo 3 DATA\_INVENTARIO\), para o estabelecimento e verificar a quantidade do produto, campo 13 da SAFX52 \(QUANTIDADE\)\.

Esta regra equivale as gerações do Meio Magnético Especial\.

__\[CH23602\_2012\]__

Quando não for encontrado registro correspondente no lançamento de Inventário \(situação em que não há estoque anterior\), gerar zero\.

Para o primeiro dia do movimento, recuperar a ÚLTIMA data de lançamento do inventário para o estabelecimento e verificar a quantidade do produto, campo 13 da SAFX52 \(QUANTIDADE\)\. 

Para os demais dias, recuperar o total do saldo do estoque final \(Campo 12\-ESTQ\_FIN do registro 1391\) do dia anterior\.

O produto, campo 07 \(COD\_PRODUTO\) deve estar  configurado através da tela de parametrização de PRODUTO do módulo SPED FISCAL, onde será identificado o grupo do produto, “Açúcar”, “Álcool Anidro”, “Álcool Hidratado”, \[__MFS77290__\] Açúcar Mascavo, Açúcar Demerara, Açúcar Cristal, Outros Açúcares, “Álcool para outros fins”\. Lembrando que para estabelecimentos de Alagoas, de acordo com a data da geração, será considerado ou o produto 03\-Açúcar ou os produtos 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal e 07 – Outros Açúcares \(vide regra [RN1390](#ACUCAR)\)\.

__\[Alteração – CH25861\-B\_2012\]/\[ALTERADA – CH165\_2016\]__

Somente considerar o inventário quando o campo 04 – GRUPO\_CONTAGEM \(SAFX52\) = 1 e 3	

__*Resumindo: *__

__Origem dos dados__: SAFX52

__Conteúdo__: Totalização da quantidade do inventário de todos os produtos parametrizados no Sped Fiscal\.

Para o primeiro dia do mês, recupera o valor do inventário da data informada em tela\.

  

Para os demais dias, é utilizado o conteúdo do campo “12\-ESTQ\_FIN” do dia anterior\.

__Alteração da OS4070 \(Conversão de Medida\):__

Se campo 02\-COD\_PROD do registro pai 1390 = 01 ou 02 ou 08 \(Álcool\) \[__MFS77290__\]

    Se a unidade de medida  __\(\*\)__ <> ‘l’ e <> ‘L’ e <> ‘lt’ e <> ‘LT’ e <> ‘Lt’

         Será feita a conversão da quantidade para __litro__, *antes de totalizar seu valor*\.

Se campo 02\-COD\_PROD do registro pai 1390 = 03 ou 04 ou 05 ou 06 ou 07 \(Açúcares\) \[__MFS77290__\]

    Se a unidade de medida __\(\*\)__ <> ‘kg’ e <> ‘KG’ e <> ‘Kg’

          Será feita a conversão da quantidade para __quilo__, *antes de totalizar o seu valor*\.

__\(\*\)__ campo “12\-Unidade de Medida” da SAFX52

Verificar na __RN1391\-99__ as regras para conversão\.

__RN1391\-05__

__Campo QTD\_PRODUZ__

__\[ALTERADA – CH24790\_2015/ CH24790\-C\_2015\]__

O cálculo total de produção será a soma de todos os lançamentos do campo 20 da SAFX10 \(QTD\_MOVTO\) 07 da SAFX16 \(QTD\_FABR\), onde:

A operação, campo 27 da SAFX10 \(COD\_OPERACAO\) esteja corretamente configurada como "QTD PRODUZIDA" através da tela de parametrização de OPERAÇÃO do módulo SPED FISCAL \(valendo para todos os tipos informados no campo “Obrigação Fiscal”\)

e

O produto, campo 04 12 da SAFX10 \(COD\_PRODUTO\) esteja corretamente configurado através da tela de parametrização de PRODUTO do módulo SPED FISCAL, onde é identificado o grupo do produto, “Açúcar”, “Álcool Anidro” ou “Álcool Hidratado” ou \[__MFS77290__\] 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal, 07 – Outros Açúcares, 08 \- “Álcool para outros fins”\. Lembrando que para estabelecimentos de Alagoas, de acordo com a data da geração, será considerado ou o produto 03\-Açúcar ou os produtos 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal e 07 – Outros Açúcares \(vide regra [RN1390](#ACUCAR)\)\.

__*Resumindo: *__

__Origem dos dados__: SAFX10 \(Movimentos de Entrada\)

__Conteúdo__:

Verifica se existem, na data, registros de produção com movimentações \(SAFX10\) de operações e produtos parametrizados no Sped, e associados ao “grupo” do registro pai 1390\. 

O conteúdo deste campo será a totalização da quantidade produzida \(campo “20 \-Quantidade”\) destes registros, que atendam ao seguinte critério:

\- Movimentos de entrada \(campo 03\-Movto E/S <> 9\);

__ALTERAÇÃO MFS1002797\] Tratamento dos movimentos de estorno no cálculo \(Movimentos de saída\)__

Se o parâmetro “Considerar os Movimentos de Estorno no Cálculo da Produção”  estiver marcado na tela de Dados Iniciais 

     __Origem dos dados__: SAFX10 \(Movimentos de Saída\)

    __Conteúdo__:

    Verifica se existem, na data, registros de produção com movimentações \(SAFX10\) de operações e    

    produtos parametrizados no Sped, e associados ao “grupo” do registro pai 1390\. 

    O conteúdo deste campo será a totalização da quantidade produzida \(campo “20\-Quantidade”\)   

    destes registros, que atendam ao seguinte critério:

    \- Movimentos de saída \(campo 03\-Movto E/S = 9\);

       O total dos movimentos de saída deve ser subtraído do total dos movimentos de entrada\.

       Obs\.:  Se o resultado total der um valor negativo, deve ser gravado zero\.

__Alteração da OS4070 \(Conversão de Medida\):__

Se campo 02\-COD\_PROD do registro pai 1390  = 01 ou 02 ou 08 \(Álcool\) \[__MFS77290__\]

    Se a unidade __\(\*\)__ <> ‘l’ e <> ‘L’ e <> ‘lt’ e <> ‘LT’ e <> ‘Lt’

         Será feita a conversão da quantidade para __litro__, *antes de totalizar o seu valor*\.

Se campo 02\-COD\_PROD do registro pai 1390 = 03 ou 04 ou 05 ou 06 ou 07 \(Açúcares\) \[__MFS77290__\]

    Se a unidade __\(\*\)__ <> ‘kg’ e <> ‘KG’ e <> ‘Kg’

          Será feita a conversão da quantidade para __quilo__, *antes de totalizar o seu valor*\.

__\(\*\)__ campo “33 06\-Unidade de Medida” da SAFX10 SAFX16

Verificar na __RN1391\-99__ as regras para conversão\.

__RN1391\-06__

__Campo ENT\_ANID\_HID__

\[Alteração OS\-3747\_2012\]

O cálculo do total de *Álcool Hidratado* resultante da transformação de Álcool Anidro será a soma de todos os lançamentos do campo 20 da SAFX10 \(QTD\_MOVTO\), onde:  
A operação, campo 27 da SAFX10 \(COD\_OPERACAO\) esteja corretamente configurado como "ENTRADAS \- REPROCESSO" através da tela de parametrização de OPERAÇÃO do módulo SPED FISCAL\.  
e  
O produto, campo 12 \(COD\_PRODUTO\) esteja parametrizado como "__Álcool Hidratado__" através da tela de parametrização de PRODUTO do módulo SPED FISCAL\.

Já para o cálculo do total de *Álcool Anidro* resultante da transformação de Álcool Hidratado será a soma de todos os lançamentos do campo 20 da SAFX10 \(QTD\_MOVTO\), onde:  
A operação, campo 27 \(COD\_OPERACAO\) esteja parametrizado como "ENTRADAS \- REPROCESSO" através da tela de parametrização de OPERAÇÃO do módulo SPED FISCAL  
e  
O produto, campo 12 \(COD\_PRODUTO\) esteja parametrizado como "__Álcool Anidro__" através da tela de parametrização de PRODUTO do módulo SPED FISCAL\.

__*Resumindo: *__

__Origem dos dados:__ SAFX10

__Conteúdo__:

Totalização da quantidade dos movimentos \(campo “20\-Quantidade”\) no dia, que atendam aos seguintes critérios:

\- Movimentos de entrada \(campo 03\-Movto E/S <> 9\);

\- O produto do movimento deve estar parametrizado no Sped como Álcool anidro ou Álcool Hidratado;

\- A operação \(campo 27\-Código da Operação\) deve estar  parametrizada no Sped como “__Entradas\-__

__   Reprocesso__” \(campo  “Obrigação Fiscal” da tela de parametrização das operações\);

__Alteração da OS4070 \(Conversão de Medida\):__

Caso a unidade de medida do movimento não seja litro \(campo “33\-Unidade de Medida” <> ‘l’ e <> ‘L’ e <> ‘lt’ e <> ‘LT’ e <> ‘Lt’\) será feita a conversão da quantidade para litro, *antes de totalizar o seu valor*\.

Verificar na __RN1391\-99__ as regras para conversão\.

__RN1391\-07__

__Campo OUT\_ENTR__

O cálculo do total de Outras entradas será a soma de todos os lançamentos do campo 20 da SAFX10 \(QTD\_MOVTO\), onde:  
  
A operação, campo 27 da SAFX10 \(COD\_OPERACAO\) esteja parametrizado como "Entrada \- Outras" através da tela de parametrização de OPERAÇÃO do módulo SPED FISCAL,  
e   
O produto, campo 12 \(COD\_PRODUTO\) esteja corretamente configurado através da tela de parametrização de PRODUTO do módulo SPED FISCAL, onde é identificado o grupo do produto, “Açúcar”, “Álcool Anidro” ou “Álcool Hidratado” ou \[__MFS77290__\] 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal, 07 – Outros Açúcares, 08 \- “Álcool para outros fins”\. 

\[Alteração OS\-3747\_2012\]

__\+\(mais\) __

O cálculo do total de todos os lançamentos do campo 20 da SAFX10 \(QTD\_MOVTO\), onde:  
  
A operação, campo 27 da SAFX10 \(COD\_OPERACAO\) esteja parametrizado como "__ENTRADAS \- REPROCESSO__" através da tela de parametrização de OPERAÇÃO do módulo SPED FISCAL\.  
e

O produto, campo 12 da SAFX10 \(COD\_PRODUTO\) esteja parametrizado como "__Açúcar__" ou \[__MFS77290__\] 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal, 07 – Outros Açúcares ou 08 \- “Álcool para outros fins, através da tela de parametrização de PRODUTO do módulo SPED FISCAL\.

__*Resumindo: *__

__Origem dos dados:__ SAFX10

__Conteúdo__:

Totalização diária da quantidade dos movimentos \(campo “20\-Quantidade”\) que atendam aos seguintes critérios:

\- Movimentos de entrada\(campo 03\-Movto E/S <> 9\);

\- O produto do movimento deve estar parametrizado no Sped como Açúcar, Álcool Anidro ou Álcool

    Hidratado ou \[__MFS77290__\] 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal, 07 – Outros Açúcares, 08 \- “Álcool para outros fins”\. Lembrando que para estabelecimentos de Alagoas, de acordo com a data da geração, será considerado ou o produto 03\-Açúcar ou os produtos 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal e 07 – Outros Açúcares \(vide regra [RN1390](#ACUCAR)\)\.

\- Se campo 02\-COD\_PROD do registro pai 1390 = 03 \(Açúcar\) ou \[__MFS77290__\] 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal, 07 – Outros Açúcares, 08 \- “Álcool para outros fins”:

     A operação \(campo 27\-Código da Operação\) deve estar parametrizada no Sped 

     como “__Entradas\-Outras__” ou “__Entradas \-Reprocesso__”;

\- Se campo 02\-COD\_PROD do registro pai 1390 = 01 ou 02 \(Álcool\):

    A operação \(campo 27\-Código da Operação\) deve estar  parametrizada no Sped 

    como “__Entradas\-Outras__”;

__Alteração da OS4070 \(Conversão de Medida\):__

Se campo 02\-COD\_PROD do registro pai 1390 = 01 ou 02 ou 08 \(Álcool\) \[__MFS77290__\]

    Se a unidade __\(\*\)__ <> ‘l’ e <> ‘L’ e <> ‘lt’ e <> ‘LT’ e <> ‘Lt’

         Será feita a conversão da quantidade para __litro__, *antes de totalizar o seu valor*\.

Se campo 02\-COD\_PROD do registro pai 1390 = 03 ou 04 ou 05 ou 06 ou 07 \(Açúcares\) \[__MFS77290__\]

    Se a unidade __\(\*\)__ <> ‘kg’ e <> ‘KG’ e <> ‘Kg’

          Será feita a conversão da quantidade para __quilo__, *antes de totalizar o seu valor*\.

__\(\*\)__ campo “33\-Unidade de Medida” da SAFX10

Verificar na __RN1391\-99__ as regras para conversão\.

__RN1391\-08__

__Campo PERDA__

"O cálculo do total de evaporação/Perda será a soma de todos os lançamentos do campo 20 da SAFX10 \(QTD\_MOVTO\), onde:  
  
A operação, campo 27 \(COD\_OPERACAO\) esteja parametrizado como "Saídas \- Evaporação/Perda" através da tela de parametrização de OPERAÇÃO do módulo SPED FISCAL,  
e  
O produto, campo 12 \(COD\_PRODUTO\) esteja corretamente configurado através da tela de parametrização de PRODUTO do módulo SPED FISCAL, onde é identificado o grupo do produto, “Açúcar”, “Álcool Anidro”, “Álcool Hidratado” ou \[__MFS77290__\] 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal, 07 – Outros Açúcares, 08 \- “Álcool para outros fins”\. Lembrando que para estabelecimentos de Alagoas, de acordo com a data da geração, será considerado ou o produto 03\-Açúcar ou os produtos 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal e 07 – Outros Açúcares \(vide regra [RN1390](#ACUCAR)\)\.

__*Resumindo: *__

__Origem dos dados:__ SAFX10

__Conteúdo__:

Totalização diária da quantidade dos movimentos \(campo “20\-Quantidade”\) que atendam aos seguintes critérios:

\- Movimentos de saída \(campo 03\-Movto E/S = 9\);

\- O produto do movimento deve estar parametrizado no Sped como Açúcar, Álcool Anidro ou Álcool 

   Hidratado;

\- A operação \(campo 27\-Código da Operação\) deve estar  parametrizada no Sped como 

   “__Saídas\-Evaporação/Perdas__”;

__Alteração da OS4070 \(Conversão de Medida\):__

Se campo 02\-COD\_PROD do registro pai 1390 = 01 ou 02 ou 08 \(Álcool\) \[__MFS77290__\]

    Se a unidade __\(\*\)__ <> ‘l’ e <> ‘L’ e <> ‘lt’ e <> ‘LT’ e <> ‘Lt’

         Será feita a conversão da quantidade para __litro__, *antes de totalizar o seu valor*\.

Se campo 02\-COD\_PROD do registro pai 1390 = 03 ou 04 ou 05 ou 06 ou 07 \(Açúcares\) \[__MFS77290__\]

    Se a unidade __\(\*\)__ <> ‘kg’ e <> ‘KG’ e <> ‘Kg’

          Será feita a conversão da quantidade para __quilo__, *antes de totalizar o seu valor*\.

__\(\*\)__ campo “33\-Unidade de Medida” da SAFX10

Verificar na __RN1391\-99__ as regras para conversão\.

__RN1391\-09__

__Campo CONS__

"O cálculo do total do consumo próprio será a soma de todos os lançamentos do campo 20 da SAFX10 \(QTD\_MOVTO\), onde:  
  
A operação, campo 27 \(COD\_OPERACAO\) esteja parametrizado como "Consumo" através da tela de parametrização de OPERAÇÃO do módulo SPED FISCAL,  
e  
O produto, campo 12 \(COD\_PRODUTO\) esteja corretamente configurado através da tela de parametrização de PRODUTO do módulo SPED FISCAL, onde é identificado o grupo do produto, “Açúcar”, “Álcool Anidro”, “Álcool Hidratado” ou \[__MFS77290__\] 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal, 07 – Outros Açúcares, 08 \- “Álcool para outros fins”\. Lembrando que para estabelecimentos de Alagoas, de acordo com a data da geração, será considerado ou o produto 03\-Açúcar ou os produtos 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal e 07 – Outros Açúcares \(vide regra [RN1390](#ACUCAR)\)\.

__*Resumindo: *__

__Origem:__ SAFX10

__Conteúdo__:

Totalização diária da quantidade dos movimentos \(campo “20\-Quantidade”\) que atendam aos seguintes critérios:

\- Movimentos de saída \(campo 03\-Movto E/S = 9\);

\- O produto do movimento deve estar parametrizado no Sped como  Açúcar, Álcool Anidro ou Álcool

   Hidratado;

\- A operação \(campo 27\-Código da Operação\) deve estar parametrizada no Sped como “__Consumo__”;

Tratamento conversão de medida: 

Se campo 02\-COD\_PROD do registro pai 1390 = 01 ou 02 ou 08 \(Álcool\) \[__MFS77290__\]

    Se a unidade __\(\*\)__ <> ‘l’ e <> ‘L’ e <> ‘lt’ e <> ‘LT’ e <> ‘Lt’

         Será feita a conversão da quantidade para __litro__, *antes de totalizar o seu valor*\.

Se campo 02\-COD\_PROD do registro pai 1390 = 03 ou 04 ou 05 ou 06 ou 07 \(Açúcares\) \[__MFS77290__\]

    Se a unidade __\(\*\)__ <> ‘kg’ e <> ‘KG’ e <> ‘Kg’

          Será feita a conversão da quantidade para __quilo__, *antes de totalizar o seu valor*\.

__\(\*\)__ campo “33\-Unidade de Medida” da SAFX10

Verificar na __RN1391\-99__ as regras para conversão\.

__RN1391\-10__

__Campo SAI\_ANI\_HID__

\[Alteração OS\-3747\_2012\]

O cálculo do total de Saída de *transformação de Álcool Hidratado para a produção de Álcool Anidro* será a soma de todos os lançamentos do campo 20 da SAFX10 \(QTD\_MOVTO\), onde:

A operação, campo 27 da SAFX10 \(COD\_OPERACAO\) esteja parametrizado como "Saída \- Produção Anidro"  "SAIDAS \- REPROCESSO" através da tela de parametrização de OPERAÇÃO do módulo SPED FISCAL\.

e

O produto, campo 12 da SAFX10 \(COD\_PRODUTO\) esteja parametrizado como "__Álcool Hidratado__" através da tela de parametrização de PRODUTO do módulo SPED FISCAL\.

Já para o cálculo do total de Saída de transformação *de Álcool Anidro para a produção de álcool hidratado* será a soma de todos os lançamentos do campo 20 da SAFX10 \(QTD\_MOVTO\), onde:

A operação, campo 27 da SAFX10 \(COD\_OPERACAO\) esteja parametrizado como “Saída – Produção Hidratado”  "SAIDAS \- REPROCESSO" através da tela de parametrização de OPERAÇÃO do módulo SPED FISCAL\.

E

O produto, campo 12 da SAFX10 \(COD\_PRODUTO\) esteja parametrizado como “__Álcool Anidro__” através da tela de parametrização de PRODUTO do módulo SPED FISCAL\.

__*Resumindo: *__

__Origem dos dados:__ SAFX10

__Conteúdo__:

Totalização diária da quantidade dos movimentos \(campo “20\-Quantidade”\) que atendam aos seguintes critérios:

\- Movimentos de saída \(campo 03\-Movto E/S = 9\);

\- O produto do movimento deve estar parametrizado no Sped como  Álcool Anidro ou Álcool 

   Hidratado;

\- A operação \(campo 27\-Código da Operação\) deve estar parametrizada no Sped como 

   “__Saídas\-Reprocesso__”;

__Alteração da OS4070 \(Conversão de Medida\):__

Caso a unidade de medida __\(\*\) __do movimento não seja litro \(seja <> ‘l’ e <> ‘L’ e <> ‘lt’ e <> ‘LT’ e <> ‘Lt’\) será feita a conversão da quantidade para litro, *antes de totalizar o seu valor*\.

__\(\*\)__ campo “33\-Unidade de Medida” da SAFX10

Verificar na __RN1391\-99__ as regras para conversão\. 

__RN1391\-11__

__Campo SAIDAS__

"O cálculo do total de saída  será a soma de todos os lançamentos do campo 20 da SAFX10 \(QTD\_MOVTO\), onde:  
  
A operação, campo 27 \(COD\_OPERACAO\) esteja parametrizado como "Saídas \- Outras" através da tela de parametrização de OPERAÇÃO do módulo SPED FISCAL,  
e  
O produto, campo 12 \(COD\_PRODUTO\) esteja corretamente configurado através da tela de parametrização de PRODUTO do módulo SPED FISCAL, onde é identificado o grupo do produto, “Açúcar”, “Álcool Anidro”, “Álcool Hidratado” ou \[__MFS77290__\] 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal, 07 – Outros Açúcares, 08 \- “Álcool para outros fins”\.

\[Alteração OS\-3747\_2012\]

__\+\(mais\) __

O cálculo do total de todos os lançamentos do campo 20 da SAFX10 \(QTD\_MOVTO\), onde:  
  
A operação, campo 27 da SAFX10 \(COD\_OPERACAO\) esteja parametrizado como "__SAIDAS \- REPROCESSO__" através da tela de parametrização de OPERAÇÃO do módulo SPED FISCAL\.  
e

O produto, campo 12 da SAFX10 \(COD\_PRODUTO\) esteja parametrizado como "__Açúcar__" ou \[__MFS77290__\] 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal, 07 – Outros Açúcares, 08 \- “Álcool para outros fins”, através da tela de parametrização de PRODUTO do módulo SPED FISCAL\.

__*Resumindo: *__

__Origem dos dados:__ SAFX10

__Conteúdo__:

Totalização diária da quantidade dos movimentos \(campo “20\-Quantidade”\) que atendam aos seguintes critérios:

\- Movimentos de saída \(campo 03\-Movto E/S = 9\);

\- O produto do movimento deve estar parametrizado no Sped como  Açúcar, Álcool Anidro ou Álcool

   Hidratado ou \[__MFS77290__\] 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal, 07 – Outros Açúcares, 08 \- “Álcool para outros fins”\. Lembrando que para estabelecimentos de Alagoas, de acordo com a data da geração, será considerado ou o produto 03\-Açúcar ou os produtos 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal e 07 – Outros Açúcares \(vide regra [RN1390](#ACUCAR)\)\.

\- Se campo 02\-COD\_PROD do registro pai 1390 = 03 \(Açúcar\) ou \[__MFS77290__\] 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal, 07 – Outros Açúcares, 08 \- “Álcool para outros fins”:

      A operação \(campo 27\-Código da Operação\) deve estar  parametrizada no Sped como 

      “__Saídas\-Outras__” ou “__Saídas\-Reprocesso__”;

\- Se campo 02\-COD\_PROD do registro pai 1390 = 01 ou 02 \(Álcool\):

      A operação \(campo 27\-Código da Operação\) deve estar  parametrizada no Sped como 

     “__Saídas\-Outras__”;

__Alteração da OS4070 \(Conversão de Medida\):__

Se campo 02\-COD\_PROD do registro pai 1390 = 01 ou 02 ou 08 \(Álcool\) \[__MFS77290__\]

    Se a unidade __\(\*\)__ <> ‘l’ e <> ‘L’ e <> ‘lt’ e <> ‘LT’ e <> ‘Lt’

         Será feita a conversão da quantidade para __litro__, *antes de totalizar o seu valor*\.

Se campo 02\-COD\_PROD do registro pai 1390 = 03 ou 04 ou 05 ou 06 ou 07 \(Açúcares\) \[__MFS77290__\]

    Se a unidade __\(\*\)__ <> ‘kg’ e <> ‘KG’ e <> ‘Kg’

          Será feita a conversão da quantidade para __quilo__, *antes de totalizar o seu valor*\.

__\(\*\)__ campo “33\-Unidade de Medida” da SAFX10

Verificar na __RN1391\-99__ as regras para conversão\.

__RN1391\-12__

__Campo ESTQ\_FIN__

A regra para o estoque final deve seguir a seguinte equação: "Estoque Inicial \+ Entradas \- Saídas", ou seja:  
  
Estoque Inicial \(Total do campo 04 deste registro do SPED Fiscal, 1391\)  
  
\+\(mais\)  
TOTAL DE ENTRADAS:  
  Soma dos seguintes lançamentos do campo 20 \(QTD\_MOVTO\) onde a operação, campo 27 \(COD\_OPERACAO\) esteja parametrizado como:  
 \- ENTRADAS \- PRODUÇÃO  
 \- ENTRADAS \- DESITRATAÇÃO HIDRATADO PRODUÇÃO  
 \- ENTRADAS \- OUTRAS  
  
\-\(menos\)  
TOTAL DE SAÍDAS:  
  Soma dos seguintes lançamentos do campo 20 \(QTD\_MOVTO\) onde a operação, campo 27 \(COD\_OPERACAO\) esteja parametrizado como:  
 \- SAIDAS \- EVAPORAÇÃO/PERDA  
 \- SAÍDAS \- PRODUÇÃO HIDRATADO  
 \- SAÍDAS \- OUTRAS\.  
  
\-\- Esta regra deve ser aplicada apenas quando o código do produto, campo 12 da SAFX10 \(COD\_PRODUTO\) estiver corretamente configurado através da tela de parametrização de PRODUTO do módulo SPED FISCAL, onde é identificado o grupo do produto, “Açúcar”, “Álcool Anidro” ou “Álcool Hidratado”\.

__\[Excluída – CH25861\-A\_2012\]__

__\[Alteração – CH25861\_2012\]__

Somente considerar o estoque quando o campo 05 – GRUPO\_CONTAGEM \(SAFX10\) = 1\.

__*Resumindo: *__

Este campo é gerado a partir do conteúdo gravado no campo 04\-ESTQ\_INI, mais as entradas e menos as saídas, ou seja:

àCampo  04\-ESTQ\_INI

àMais campos: \(05\-QTD\_PRODUZ \+ 06\-ENT\_ANID\_HID  \+ 07\-OUT\_ENTR\)

àMenos campos: \(08\-PERDA \+ 09\-CONS \+ 10\-SAI\_ANI\_HIR \+ 11\-SAIDAS\)

\(neste campo não é necessário tratar conversão de medida, pois ele é o resultado dos demais campos, onde já feita conversão\)

__\[ALTERADA – CH24790\-C\_2015\]__

__Crítica:__

Caso o resultado a ser gravado for negativo, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log \(nº 367 da planilha Sped\_Fiscal\_Log\_Erros\.xls\) com a seguinte descrição: *“O campo Estoque Final esta com conteúdo inválido \(valor negativo\), favor verificar a movimentação de entrada”\. *O log mostrará a identificação do registro \(Estab\+Grupo do Produto\+Data Registro\) para identificação do usuário\.

__0RN1391\-13__

__Campo ESTOQUE\_INI\_MEL__

Para o primeiro dia do movimento, recuperar a ÚLTIMA data de lançamento do inventário para o estabelecimento e verificar a quantidade do produto, campo 13 da SAFX52 \(QUANTIDADE\)\. 

Para os demais dias, recuperar o total do saldo do *estoque final de mel residual* do dia anterior\.

O *estoque final do mel residual* será calculado internamente pelo sistema, onde será utilizada a seguinte conta: 

Campo 13 \+\(mais\) 14  \-\(menos\) Campo 15 do registro 1391 do dia anterior\.

O produto, campo 07 \(COD\_PRODUTO\) deve estar parametrizado como "Mel Residual" ou \[__MFS77290__\] “Mel Residual \- Açúcar Mascavo”, “Mel Residual \- Açúcar Demerara”, “Mel Residual \- Açúcar Cristal”, “Mel Residual – Outros Açúcares” através da tela de parametrização de produto do módulo SPED FISCAL\.

Quando este campo for preenchido, considerar o produto do campo 02 no registro 1390 igual a:

\- 03 \(açúcar\) p/ o grupo produto “Mel Residual”

\- 04 \- Açúcar Mascavo p/ o grupo produto “Mel Residual \- Açúcar Mascavo”

\- 05 \- Açúcar Demerara p/ o grupo produto“Mel Residual \- Açúcar Demerara” 

\- 06 \- Açúcar Cristal p/ o grupo produto“Mel Residual \- Açúcar Cristal” 

\- 07 – Outros Açúcares p/ o grupo produto “Mel Residual – Outros Açúcares”

__\[Alteração – CH25861\-B\_2012\]__

Somente considerar o inventário quando o campo 04 – GRUPO\_CONTAGEM \(SAFX52\) = 1

__*Resumindo: *__

__Origem dos dados__: SAFX52

__Conteúdo__: Totalização da quantidade do inventário de todos os produtos parametrizados no Sped Fiscal com a classificação =  “__Mel Residual__”, \[__MFS77290__\] “Mel Residual \- Açúcar Mascavo”, “Mel Residual \- Açúcar Demerara”, “Mel Residual \- Açúcar Cristal”, “Mel Residual – Outros Açúcares”

__\[MFS77290__\]

Para o estabelecimento de __Alagoas__ será necessário verificar a data da geração, para determinar qual  produto será considerado na geração do 1390 para o açúcar: o 03\-AÇÚCAR ou os produtos 04\-AÇÚCAR MASCAVO, 05\-AÇÚCAR DEMERARA, 06\-AÇÚCAR CRISTAL e 07\-OUTROS AÇÚCARES\.

Se a Data Inicial informada na tela de geração for anterior a __01/01/2022__, então:

   Considera o produto Mel Residual\.

   Não considerar os produtos “Mel Residual \- Açúcar Mascavo”, “Mel Residual \- Açúcar Demerara”, “Mel Residual \- Açúcar Cristal”, “Mel Residual – Outros Açúcares”\.

Se a Data Inicial informada na tela de geração for maior ou igual a __01/01/2022__, então:

   Não considerar o produto Mel Residual\.

   Considerar os produtos “Mel Residual \- Açúcar Mascavo”, “Mel Residual \- Açúcar Demerara”, “Mel Residual \- Açúcar Cristal”, “Mel Residual – Outros Açúcares”\.

Para o primeiro dia do mês, recupera o valor do inventário da data informada em tela\.

  

Para os demais dias, o conteúdo será igual ao estoque final *do dia anterior*, calculado da seguinte forma:

                \[13\-ESTQ\_INI\_MEL \+ 14\-PROD\_DIA\_MEL – 15\-UTIL\_MEL \]

          \(considerando o registro do dia anterior, ou último dia anterior gravado\)

A informação deste campo será considerada para o produto do campo 02 no registro 1390 igual a:

\- 03 \(açúcar\) p/ o grupo produto “Mel Residual”

\- 04 \- Açúcar Mascavo p/ o grupo produto “Mel Residual \- Açúcar Mascavo”

\- 05 \- Açúcar Demerara p/ o grupo produto“Mel Residual \- Açúcar Demerara” 

\- 06 \- Açúcar Cristal p/ o grupo produto“Mel Residual \- Açúcar Cristal” 

\- 07 – Outros Açúcares p/ o grupo produto “Mel Residual – Outros Açúcares”

__Alteração da OS4070 \(Conversão de Medida\):__

Caso a unidade de medida__ __do inventário __\(\*\)__ não seja quilo \(seja <> ‘kg’ e <> ‘KG’ e <> ‘Kg’\) será feita a conversão da quantidade para quilo, *antes de totalizar o seu valor*\.

__\(\*\)__ campo “12\-Unidade de Medida” da SAFX52

Verificar na __RN1391\-99__ as regras para conversão\.

__RN1391\-14__

__Campo PROD\_DIA\_MEL__

__\[ALTERADA – CH24790\_2015\]__

O cálculo do total de mel residual produzido será:

A soma de todos os lançamentos do campo 07 da SAFX16 \(QTD\_FABR\), onde o produto, campo 04 \(COD\_PRODUTO\) esteja parametrizado como “Mel residual” através da tela de parametrização de produto do módulo SPED FISCAL\.

\[Alteração CH21598\-A\_2012\]

__\+\(mais\) __

O cálculo do total de todos os lançamentos do campo 20 da SAFX10 \(QTD\_MOVTO\), onde:  
  
A operação, campo 27 da SAFX10 \(COD\_OPERACAO\) esteja parametrizado como "__ENTRADAS OUTRAS \- MEL__" através da tela de parametrização de OPERAÇÃO do módulo SPED FISCAL\.  
e

O produto, campo 12 da SAFX10 \(COD\_PRODUTO\) esteja parametrizado como "__Mel Residual__",\[__MFS77290__\] “Mel Residual \- Açúcar Mascavo”, “Mel Residual \- Açúcar Demerara”, “Mel Residual \- Açúcar Cristal”, “Mel Residual – Outros Açúcares”  através da tela de parametrização de PRODUTO do módulo SPED FISCAL\.

Quando este campo for preenchido, considerar o produto do campo 02 no registro 1390 igual a:

\- 03 \(açúcar\) p/ o grupo produto “Mel Residual”

\- 04 \- Açúcar Mascavo p/ o grupo produto “Mel Residual \- Açúcar Mascavo”

\- 05 \- Açúcar Demerara p/ o grupo produto“Mel Residual \- Açúcar Demerara” 

\- 06 \- Açúcar Cristal p/ o grupo produto“Mel Residual \- Açúcar Cristal” 

\- 07 – Outros Açúcares p/ o grupo produto “Mel Residual – Outros Açúcares”

__*Resumindo: *__

__Origem dos dados__: SAFX10 e SAFX16

__Conteúdo__: Este campo é preenchido com a quantidade produzida de mel residual no dia, mais com a quantidade dos movimentos de entrada no estoque\.

Para identificar o mel residual, serão considerados todos os produtos parametrizados no Sped Fiscal com a classificação =  “__Mel Residual__”, \[__MFS77290__\] “Mel Residual \- Açúcar Mascavo”, “Mel Residual \- Açúcar Demerara”, “Mel Residual \- Açúcar Cristal”, “Mel Residual – Outros Açúcares”\.

__\[MFS77290__\]

Para o estabelecimento de __Alagoas__ será necessário verificar a data da geração, para determinar qual  produto será considerado na geração do 1390 para o açúcar: o 03\-AÇÚCAR ou os produtos 04\-AÇÚCAR MASCAVO, 05\-AÇÚCAR DEMERARA, 06\-AÇÚCAR CRISTAL e 07\-OUTROS AÇÚCARES\.

Se a Data Inicial informada na tela de geração for anterior a __01/01/2022__, então:

   Considera o produto Mel Residual\.

   Não considerar os produtos “Mel Residual \- Açúcar Mascavo”, “Mel Residual \- Açúcar Demerara”, “Mel Residual \- Açúcar Cristal”, “Mel Residual – Outros Açúcares”\.

Se a Data Inicial informada na tela de geração for maior ou igual a __01/01/2022__, então:

   Não considerar o produto Mel Residual\.

   Considerar os produtos “Mel Residual \- Açúcar Mascavo”, “Mel Residual \- Açúcar Demerara”, “Mel Residual \- Açúcar Cristal”, “Mel Residual – Outros Açúcares”\.

Assim, teremos:

Total da quantidade produzida no dia \(SAFX16, campo “07\- Quantidade”\)

\+

Total da quantidade das entradas no dia \(SAFX10, campo “20\-Quantidade”\)\.

Em relação aos movimentos da SAFX10 serão consideradas *apenas* as entradas cuja operação \(campo 27\-Código da Operação\) esteja parametrizada no Sped como “__Entradas Outras – Mel__”\.

A informação deste campo será considerada para o produto do campo 02 no registro 1390 igual a:

\- 03 \(açúcar\) p/ o grupo produto “Mel Residual”

\- 04 \- Açúcar Mascavo p/ o grupo produto “Mel Residual \- Açúcar Mascavo”

\- 05 \- Açúcar Demerara p/ o grupo produto“Mel Residual \- Açúcar Demerara” 

\- 06 \- Açúcar Cristal p/ o grupo produto“Mel Residual \- Açúcar Cristal” 

\- 07 – Outros Açúcares p/ o grupo produto “Mel Residual – Outros Açúcares”

__Alteração da OS4070 \(Conversão de Medida\):__

Caso a unidade de medida__ __da produção \(campo “06\-Unidade de Medida” da SAFX16\) __ou__ 

Se a unidade de medida do movimento \(campo “33\-Unidade de Medida” da SAFX10\), conforme o caso, não seja quilo \(seja <> ‘kg’ e <> ‘KG’ e <> ‘Kg’\) será feita a conversão da quantidade para quilo, *antes de totalizar o seu valor*\.

Verificar na __RN1391\-99__ as regras para conversão\.

__RN1391\-15__

__Campo UTIL\_MEL__

__\[Alteração CH16797\_2012\]__

\[Alteração CH21598\-A\_2012\]

“O cálculo do Total de mel residual utilizado será a soma de todos os lançamentos do campo 09 \(QTD\_USADA\) da SAFX17, onde:  
  
O insumo, campo 07 \(COD\_INSUMO\) esteja parametrizado como “Mel Residual”  
e   
O produto, campo 04 \(COD\_PRODUTO\) será identificado através do grupo do produto, “Açúcar”\.

O cálculo do Total de mel residual utilizado será a soma de todos os lançamentos do campo 20 da SAFX10 \(QTD\_MOVTO\), onde:

A operação, campo 27 da SAFX10 \(COD\_OPERACAO\) esteja parametrizado como "__CONSUMO__" \+ “"__SAÍDAS OUTRAS \- MEL__"   através da tela de parametrização de OPERAÇÃO do módulo SPED FISCAL\.

e

O produto, campo 12 da SAFX10 \(COD\_PRODUTO\) esteja parametrizado como "__Mel Residual__", \[__MFS77290__\] “Mel Residual \- Açúcar Mascavo”, “Mel Residual \- Açúcar Demerara”, “Mel Residual \- Açúcar Cristal”, “Mel Residual – Outros Açúcares” através da tela de parametrização de PRODUTO do módulo SPED FISCAL\.

Quando este campo for preenchido, considerar o produto do campo 02 no registro 1390 igual a:

\- 03 \(açúcar\) p/ o grupo produto “Mel Residual”

\- 04 \- Açúcar Mascavo p/ o grupo produto “Mel Residual \- Açúcar Mascavo”

\- 05 \- Açúcar Demerara p/ o grupo produto“Mel Residual \- Açúcar Demerara” 

\- 06 \- Açúcar Cristal p/ o grupo produto“Mel Residual \- Açúcar Cristal” 

\- 07 – Outros Açúcares p/ o grupo produto “Mel Residual – Outros Açúcares”

__*Resumindo: *__

__Origem dos dados__: SAFX10 

__Conteúdo__: 

Totalização diária da quantidade dos movimentos \(campo “20\-Quantidade”\) que atendam aos seguintes critérios:

\- Movimentos de saída \(campo 03\-Movto E/S = 9\);

\- O produto do movimento deve estar parametrizado no Sped com a 

  classificação = “__Mel Residual__”, \[__MFS77290__\] “Mel Residual \- Açúcar Mascavo”, “Mel Residual \- Açúcar Demerara”, “Mel Residual \- Açúcar Cristal”, “Mel Residual – Outros Açúcares”\.

__\[MFS77290__\]

Para o estabelecimento de __Alagoas__ será necessário verificar a data da geração, para determinar qual  produto será considerado na geração do 1390 para o açúcar: o 03\-AÇÚCAR ou os produtos 04\-AÇÚCAR MASCAVO, 05\-AÇÚCAR DEMERARA, 06\-AÇÚCAR CRISTAL e 07\-OUTROS AÇÚCARES\.

Se a Data Inicial informada na tela de geração for anterior a __01/01/2022__, então:

   Considera o produto Mel Residual\.

   Não considerar os produtos “Mel Residual \- Açúcar Mascavo”, “Mel Residual \- Açúcar Demerara”, “Mel Residual \- Açúcar Cristal”, “Mel Residual – Outros Açúcares”\.

Se a Data Inicial informada na tela de geração for maior ou igual a __01/01/2022__, então:

   Não considerar o produto Mel Residual\.

   Considerar os produtos “Mel Residual \- Açúcar Mascavo”, “Mel Residual \- Açúcar Demerara”, “Mel Residual \- Açúcar Cristal”, “Mel Residual – Outros Açúcares”\.

\- A operação \(campo 27\-Código da Operação\) deve estar

   parametrizada no Sped como “__Saídas Outras\-Mel__”ou“__Consumo__”;

A informação deste campo será considerada para o produto do campo 02 no registro 1390 igual a:

\- 03 \(açúcar\) p/ o grupo produto “Mel Residual”

\- 04 \- Açúcar Mascavo p/ o grupo produto “Mel Residual \- Açúcar Mascavo”

\- 05 \- Açúcar Demerara p/ o grupo produto“Mel Residual \- Açúcar Demerara” 

\- 06 \- Açúcar Cristal p/ o grupo produto“Mel Residual \- Açúcar Cristal” 

\- 07 – Outros Açúcares p/ o grupo produto “Mel Residual – Outros Açúcares”

__Alteração da OS4070 \(Conversão de Medida\):__

Caso a unidade de medida do movimento \(campo “33\-Unidade de Medida” da SAFX10\), não seja quilo \(seja <> ‘kg’ e <> ‘KG’ e <> ‘Kg’\) será feita a conversão da quantidade para quilo, *antes de totalizar o seu valor*\.

Verificar na __RN1391\-99__ as regras para conversão\.

__RN1391\-16__

__Campo PROD\_ALC\_MEL__

__\[Regra alterada conforme CH17962\_2012\]__

*"O cálculo do Total de Álcool produzido proveniente de mel residual será a soma de todos os lançamentos do campo 09 \(QTD\_USADA\) da SAFX17, onde:  
  
O insumo, campo 07 \(COD\_INSUMO\) esteja parametrizado como "Mel Residual"  
e   
O produto, campo 04 \(COD\_PRODUTO\) esteja corretamente configurado através da tela de parametrização de PRODUTO do módulo SPED FISCAL, onde é identificado o grupo do produto, “Álcool Anidro” ou “Álcool Hidratado”\.*

O cálculo do total de produção de *Álcool proveniente de mel* será a soma de todos os lançamentos do campo 20 da SAFX10 \(QTD\_MOVTO\), onde:

A operação, campo 27 da SAFX10 \(COD\_OPERACAO\) esteja parametrizado como "__Entradas – Álcool proveniente de mel__" através da tela de parametrização de OPERAÇÃO do módulo SPED FISCAL\.

e

O produto, campo 12 da SAFX10 \(COD\_PRODUTO\) esteja parametrizado como "Álcool Hidratado" ou “Álcool Anidro” \[__MFS77290__\] “Álcool para outros fins” através da tela de parametrização de PRODUTO do módulo SPED FISCAL\.

\[__MFS77290__\]

Já para o cálculo do total de produção de *Açúcar proveniente de mel* será a soma de todos os lançamentos do campo 20 da SAFX10 \(QTD\_MOVTO\), onde:

A operação, campo 27 da SAFX10 \(COD\_OPERACAO\) esteja parametrizado como " __Entradas – Açúcar proveniente de mel__ " através da tela de parametrização de OPERAÇÃO do módulo SPED FISCAL\.

E

O produto, campo 12 da SAFX10 \(COD\_PRODUTO\) esteja parametrizado como "__Açúcar__", Açúcar Mascavo, Açúcar Demerara, Açúcar Cristal, Outros Açúcares,  através da tela de parametrização de PRODUTO do módulo SPED FISCAL\.

__*Resumindo: *__

__Origem__: SAFX10 

__Conteúdo__: 

Totalização diária da quantidade dos movimentos \(campo “20\-Quantidade”\) que atendam aos seguintes critérios:

\- Movimentos de entrada \(campo 03\-Movto E/S <> 9\);

\- O produto do movimento deve estar parametrizado no Sped como Álcool Anidro ou Álcool

   Hidratado ou \[__MFS77290__\] Açúcar, ou Açúcar Mascavo, ou Açúcar Demerara, ou Açúcar Cristal, ou Outros Açúcares, ou “Álcool para outros fins”\. Lembrando que para estabelecimentos de Alagoas, de acordo com a data da geração, será considerado ou o produto 03\-Açúcar ou os produtos 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal e 07 – Outros Açúcares \(vide regra [RN1390](#ACUCAR)\)\.

\- Se campo 02\-COD\_PROD do registro pai 1390 = 01 \-"Álcool Hidratado" ou 02 \- “Álcool Anidro” ou \[__MFS77290__\] 08 \- “Álcool para outros fins”:

      A operação \(campo 27\-Código da Operação\) deve estar  parametrizada no Sped como 

     “<a id="_Hlk92134294"></a>__Entradas \- Álcool proveniente de mel__”;

\[__MFS77290__\]

\- Se campo 02\-COD\_PROD do registro pai 1390 = 03 \(Açúcar\) ou 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal, 07 – Outros Açúcares”:

      A operação \(campo 27\-Código da Operação\) deve estar  parametrizada no Sped como 

      “__Entradas – Açúcar proveniente de mel__”;

__Alteração da OS4070 \(Conversão de Medida\):__

Se campo 02\-COD\_PROD do registro pai 1390 = 01 ou 02 ou 08 \(Álcool\) \[__MFS77290__\]

    Se a unidade __\(\*\)__ <> ‘l’ e <> ‘L’ e <> ‘lt’ e <> ‘LT’ e <> ‘Lt’

         Será feita a conversão da quantidade para __litro__, *antes de totalizar o seu valor*\.

Se campo 02\-COD\_PROD do registro pai 1390 = 03 ou 04 ou 05 ou 06 ou 07 \(Açúcares\) \[__MFS77290__\]

    Se a unidade __\(\*\)__ <> ‘kg’ e <> ‘KG’ e <> ‘Kg’

          Será feita a conversão da quantidade para __quilo__, *antes de totalizar o seu valor*\.

__\(\*\)__ campo “33\-Unidade de Medida” da SAFX10

Verificar na __RN1391\-99__ as regras para conversão\.

__RN1391\-17__

__Campo OBS__

Recuperar a observação conforme a parametrização em SPED FISCAL à Parâmetros à Registro 1390/1391 à Observação\.

\[OS3423\-D\]

Campo com limite de 255 caracteres, conforme explicação do Guia prático: *“Todos os campos alfanuméricos terão tamanho máximo de 255 caracteres, exceto se houver indicação distinta, onde, neste caso, este tamanho distinto prevalecerá\.”*

<a id="_Hlk32324757"></a>__RN1391\-18__

__Campo COD\_ITEM__

\(MFS31407\)

Este campo é gerado somente a partir da versão 1\.13 da EFD\.

Geração do campo 18\-COD\_ITEM para solução inicial __\(MFS31407\)__:

__\[MFS72164\] __Adequação da regra

A princípio, enquanto a solução definitiva não é definida, e as Usinas estão no período da entressafra \(quando não há moagem de cana\), este campo será gerado da seguinte forma:

__Se__ parâmetro do 1391 do menu “Dados Iniciais” = marcado

__      Caso 1: __COD\_PROD do registro pai 1390 = “__01__” \(Álcool Hidratado\)

            Nesse caso, todos os registros filhos 1391 \(independente da data\) serão gerados com a

            informação do insumo parametrizado para o grupo “*Cana Moída – Hidratado*” ou “*Alcool *

           *Hidratado*”\.

__      Caso 2: __COD\_PROD do registro pai 1390 = “__02__” \(Álcool Anidro\)

            Nesse caso, todos os registros filhos 1391 \(independente da data\) serão gerados com a

            informação do insumo parametrizado para o grupo “*Cana Moída – Anidro*” ou “*Alcool Anidro*”\.

__      Caso 3: __COD\_PROD do registro pai 1390 = “__03__” \(Açúcar\)

            Nesse caso, todos os registros filhos 1391 \(independente da data\) serão gerados com a

            informação do insumo parametrizado para o grupo “*Cana Moída – Açúcar*” ou *“Acucar”* ou 

            “*Mel Residual*”\.

      \[__MFS77290__\]

__      Caso 4: __COD\_PROD do registro pai 1390 = “__04__” \(Açúcar Mascavo\)

            Nesse caso, todos os registros filhos 1391 \(independente da data\) serão gerados com a

            informação do insumo parametrizado para o grupo “*Cana Moída – Açúcar Mascavol*”\.

__      Caso 5: __COD\_PROD do registro pai 1390 = “__05__” \(Açúcar Demerara\)

            Nesse caso, todos os registros filhos 1391 \(independente da data\) serão gerados com a

            informação do insumo parametrizado para o grupo “*Cana Moída – Açúcar Demerara*”\.

__      Caso 6: __COD\_PROD do registro pai 1390 = “__06__” \(Açúcar Cristal\)

            Nesse caso, todos os registros filhos 1391 \(independente da data\) serão gerados com a

            informação do insumo parametrizado para o grupo “*Cana Moída – Açúcar Cristal*”\.

__      Caso 7: __COD\_PROD do registro pai 1390 = “__07__” \(Outros Açúcares\)

            Nesse caso, todos os registros filhos 1391 \(independente da data\) serão gerados com a

            informação do insumo parametrizado para o grupo “*Cana Moída – Outros Açúcares*”\.

__      Caso 8: __COD\_PROD do registro pai 1390 = “__08__” \(Álcool para outros fins\)

            Nesse caso, todos os registros filhos 1391 \(independente da data\) serão gerados com a

            informação do insumo parametrizado para o grupo “*Cana Moída – Álcool para outros fins*”\.

__Senão__ \(parâmetro do 1391 do menu “Dados Iniciais” = desmarcado

        Nesse caso, todos os registros 1391 serão sempre gerados com a informação do insumo

        parametrizado para o grupo “*Cana Moída*”, independente do COD\_PROD do registro pai

        1390 \.

Obs: Trata\-se da parametrização de produtos do módulo Sped Fiscal, menu “Parâmetros à Registro 1390/1391 à Produto”\. Se para cada um dos casos descritos acima, existir mais de um insumo parametrizado, será informado o primeiro insumo identificado \(de forma aleatória\)\.  

*Posteriormente, para uma solução definitiva, o insumo a ser gravado neste campo será recuperado da parametrização, junto com a movimentação existente no dia\. *

Obs: Conforme o padrão do Sped, todos os códigos de produto gravados neste campo, devem ser gravados no Bloco 0 \(registro 0200\)\. Além disso, deve\-se observar os parâmetros existentes para o tratamento do indicador e código do produto \(menu “Dados Iniciais”\)\.

__ __

__RN1391\-19__

__Campo TP\_RESIDUO__

\(MFS31407\)

Este campo é gerado somente a partir da versão 1\.13 da EFD\.

Este campo é gerado sempre com a opção “01” \(=Bagaço de Cana\)\.

__\(MFS\-34707\)__

A regra de preenchimento deste campo depende da RN1391\-20\. Sugiro primeiro ler a regra do campo 20, para facilitar o entendimento da definição a seguir\.

De acordo com o resíduo que foi produzido no dia, cuja quantidade é demonstrada no campo 20 – QTD\_RESIDUO \(vide RN1391\-20\), preencher esse campo com a seguinte regra:

Se resíduo foi do grupo __*Bagaço da Cana – Hidratado*__, então:

  Preencher com “01” \(=Bagaço de Cana\)\.

Se resíduo foi do grupo __*Bagaço da Cana – Anidro*__, então:

  Preencher com “01” \(=Bagaço de Cana\)\.

Se resíduo foi do grupo __*Bagaço da Cana – Açúcar*__, então:

  Preencher com “01” \(=Bagaço de Cana\)\.

Se resíduo foi do grupo __*DDG – Hidratado*__, então:

  Preencher com “02” \(=DDG\)\.

Se resíduo foi do grupo __*DDG – Anidro*__, então:

  Preencher com “02” \(=DDG\)\.

Se resíduo foi do grupo __*WDG – Hidratado*__, então:

  Preencher com “03” \(=WDG\)\.

Se resíduo foi do grupo __*WDG – Anidro*__, então:

  Preencher com “03” \(=WDG\)\.

\[__MFS77290__\]

Se resíduo foi do grupo __*Bagaço da Cana – Açúcar Mascavo*__,  então:

  Preencher com “01” \(=Bagaço de Cana\)\.

Se resíduo foi do grupo __*Bagaço da Cana – Açúcar Demerara*__, então:

  Preencher com “01” \(=Bagaço de Cana\)\.

Se resíduo foi do grupo __*Bagaço da Cana – Açúcar Cristal*__, então:

  Preencher com “01” \(=Bagaço de Cana\)\.

Se resíduo foi do grupo __*Bagaço da Cana – Outros Açúcares*__, então:

  Preencher com “01” \(=Bagaço de Cana\)\.

Se resíduo foi do grupo __*Bagaço da Cana – Álcool para outros fins*__, então:

  Preencher com “01” \(=Bagaço de Cana\)\.

Se resíduo foi do grupo __*DDG – Álcool para outros fins*__, então:

  Preencher com “02” \(=DDG\)\.

Se resíduo foi do grupo __*WDG – Álcool para outros fins*__, então:

  Preencher com “03” \(=WDG\)\.

\[__MFS577276__\]: versão 1\.17 – Jan/2024:

A versão 1\.17 criou tratamento quando há produção dos resíduos DDG e WDG no mesmo dia\. Não existe a produção de bagaço de cana juntamente com DDG e WDG, pois os dois últimos são produzidos quando o insumo utilizado é grão como milho e o bagaço é quando o insumo é a cana\-de\-açucar\.

\- Para gerações com leiaute anterior a EFD117:

  Ver RN1391\-20 onde o campo 19 é preenchido com o resíduo de maior quantidade, quando encontrado no dia registros da SAFX16 de mais de um tipo de resíduo\.

\- Para gerações com leiaute a partir da EFD117 \(CAD\_LAYOUT – COD\_VERSAO>=117\):

  Se os resíduos __DDG – Hidratado__ e __WDG – Hidratado__ foram produzidos no dia, então:

   Preencher com “04” \(= DDG \+ WDG\)\.

  Se os resíduos __DDG – Anidro__ e __WDG – Anidro__ foram produzidos no dia, então:

   Preencher com “04” \(= DDG \+ WDG\)\.

  Se os resíduos __DDG – Álcool para Outros Fins__ e __WDG – Álcool para Outros Fins__ foram produzidos no dia, então:

   Preencher com “04” \(= DDG \+ WDG\)\.

  Ver RN1391\-20 onde o campo 19 não é preenchido quando encontrado no dia a produção de Bagaço de Cana juntamente com DDG e/ou WDG

Se não houve produção de resíduo no dia \(nenhum movimento foi recuperado da tabela de origem SAFX16 \- vide RN1391\-20\), então:

   Preencher com “01” \(=Bagaço de Cana\)\.

__Observação:__ 

Esse campo é obrigatório, por isso quando não existe produção de resíduo no dia, estamos preenchendo\-o com “01” \(=Bagaço de Cana\)\.

Segundo o cliente BIOSEV não pode acontecer de, no mesmo dia, existir produção de mais de um tipo de resíduo para um produto do registro pai 1390 \(Açúcar, Álcool Anidro, Álcool Hidratado\)\. Exemplo resíduo de DDG e de Bagaço da CANA\. Mas a versão 1\.17 \(2024\) já está prevendo a produção de DDG e WDG juntos\.

__ RN1391\-20__

__Campo QTD\_RESIDUO__

\(MFS31407\)

Este campo é gerado somente a partir da versão 1\.13 da EFD\.

__\(MFS\-34707\)__

__Cálculo pela Origem Movimentação da Produção \(SAFX16\):__

Soma os lançamentos do dia, totalizando o campo 07 da __SAFX16 __\(QTD\_FABR\), onde:

- O produto, campo 04 \(COD\_PRODUTO\) esteja parametrizado através da tela de parametrização de produto do módulo SPED FISCAL, como:

\- __*Bagaço da Cana – Hidratado *__ou__* DDG – Hidratado *__ou__* WDG – Hidratado*__, caso o 

produto apresentado no registro pai 1390 seja 01 – Álcool Hidratado; __\(\*\)__

\- __*Bagaço da Cana – Anidro *__ou__* DDG – Anidro *__ou__* WDG – Anidro*__, caso o produto apresentado no registro pai 1390 seja 02 – Álcool Anidro; __\(\*\)__

\- __*Bagaço da Cana – Açúcar,*__ caso o produto apresentado no registro pai 1390 seja 03 – Açúcar

\[__MFS77290__\]

\- __*Bagaço da Cana – Açúcar Mascavo*__ caso o produto apresentado no registro pai 1390 seja 04 – Açúcar Mascavo

\- __*Bagaço da Cana – Açúcar*__ __*Demerara*__ caso o produto apresentado no registro pai 1390 seja 05 – Açúcar Demerara

\- __*Bagaço da Cana – Açúcar*__ __*Cristal*__ caso o produto apresentado no registro pai 1390 seja 06 – Açúcar Cristal

\- __*Bagaço da Cana – Outros Açúcares*__ caso o produto apresentado no registro pai 1390 seja 07 – Outros Açúcares

\- __*Bagaço da Cana – Álcool para outros fins *__ou__* DDG – Álcool para outros fins*__ ou__* WDG – Álcool para outros fins*__, caso o produto apresentado no registro pai 1390 seja 08 – Álcool para outros fins; __\(\*\)__

Lembrando que para estabelecimentos de Alagoas, de acordo com a data da geração, será considerado ou o produto 03\-Açúcar ou os produtos 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal e 07 – Outros Açúcares \(vide regra [RN1390](#ACUCAR)\)\.

Caso a consulta não retornar registro de movimento, então gravar zero no campo QTD\_RESIDUO\.

\[__MFS577276__\]: versão 1\.17 – Jan/2024:

A versão 1\.17 criou tratamento quando há produção dos resíduos DDG e WDG no mesmo dia\. Não existe a produção de bagaço de cana juntamente com DDG e WDG, pois os dois últimos são produzidos quando o insumo utilizado é grão como milho e o bagaço é quando o insumo é a cana\-de\-açucar\.

\- Para gerações com leiaute anterior a EFD117:

  Num dia de produção do produto apresentado no registro 1390, se forem encontrados registros da SAFX16 para diferentes tipos de resíduo, considerar o resíduo de maior quantidade, para preenchimento dos campos 19 e 20\.

\- Para gerações com leiaute a partir da EFD117 \(CAD\_LAYOUT – COD\_VERSAO>=117\): 

  Num dia de produção do produto apresentado no registro 1390, se forem encontrados registros da SAFX16 para diferentes tipos de resíduos, seguir o seguinte tratamento:

 a\) DDG juntamente com WDG,: preencher os campos 19 e 20 conforme regra:

   Campo 19 =4 – DDG \+ WDG

   Campo 20 = somatório das quantidades dos dois resíduos\.

b\) Bagaço de Cana juntamente com DDG e/ou WDG: não preencher o campo 19 e zerar os campos 20, 21, 22 e 23 e exibir mensagem de aviso:

*“Foram encontrados registros de produção dos resíduos Bagaço de Cana juntamente com DDG / WDG na tabela de Movimentação da Produção \(SAFX16\) para o dia DD/MM/AAAA do produto COD \- DESCRICAO\. Essa inconsistência impede que os campos 19 ao 23 do registro 1391 sejam gerados corretamente”\.*

Onde DD/MM/AAAA é o campo 02\- DT\_REGISTRO do 1391, e o COD – DESCRIÇÃO é o COD\_PROD do registro pai 1390 com sua descrição: “__01__” \-Álcool Hidratado, “__02__” \(Álcool Anidro\), __08__” \(Álcool para outros fins\)\.

Ver planilha de erros “Sped\_Fiscal\_Log\_Erros”, mensagem de número 385\.

A mensagem deve seguir o padrão do log de erros do Sped Fiscal, contendo as linhas “Erro”, “Origem” e “Dados do Registro”, que identificam o campo com erro, a descrição do erro, a origem do dado no Mastersaf e a identificação da chave da nota fiscal criticada\.

__\(Conversão de Medida\):__

Caso a unidade de medida__ __da produção \(campo “06\-Unidade de Medida” da SAFX16\) __ou__ 

Se a unidade de medida do movimento \(campo “33\-Unidade de Medida” da SAFX10\), conforme o caso, não seja tonelada \(<> ‘t’ e <> ‘T’\) será feita a conversão da quantidade para tonelada, *antes de totalizar o seu valor*\.

Verificar na __RN1391\-99__ as regras para conversão\.

__RN1391\-21__

__QTD\_RESIDUO\_ DDG __

\[__MFS577276__\]: versão 1\.17 – Jan/2024:

\- Para gerações com leiaute anterior a EFD117:

  Campo 21 não deve ser gerado\.

\- Para gerações com leiaute a partir da EFD117 \(CAD\_LAYOUT – COD\_VERSAO>=117\): 

__   Cálculo pela Origem Movimentação da Produção \(SAFX16\):__

Soma os lançamentos do dia, totalizando o campo 07 da __SAFX16 __\(QTD\_FABR\), onde:

- O produto, campo 04 \(COD\_PRODUTO\) esteja parametrizado através da tela de parametrização de produto do módulo SPED FISCAL, como:

\- __*DDG – Hidratado*__, caso o produto apresentado no registro pai 1390 seja 01 – Álcool Hidratado; __\(\*\)__

\- __*DDG – Anidro*__, caso o produto apresentado no registro pai 1390 seja 02 – Álcool Anidro; __\(\*\)__

\- __*DDG – Álcool para outros fins*__, caso o produto apresentado no registro pai 1390 seja 08 – Álcool para outros fins\.

Caso a consulta não retornar registro de movimento, então gravar zero no campo QTD\_RESIDUO\_DDG\.

Ver RN1391\-20 onde o campo 21 é zerado quando encontrado no dia a produção de Bagaço de Cana juntamente com DDG e/ou WDG\. 

__\(Conversão de Medida\):__

Caso a unidade de medida__ __da produção \(campo “06\-Unidade de Medida” da SAFX16\) __ou__ 

Se a unidade de medida do movimento \(campo “33\-Unidade de Medida” da SAFX10\), conforme o caso, não seja tonelada \(<> ‘t’ e <> ‘T’\) será feita a conversão da quantidade para tonelada, *antes de totalizar o seu valor*\.

Verificar na __RN1391\-99__ as regras para conversão\.

__RN1391\-22__

__QTD\_RESIDUO\_ WDG __

\[__MFS577276__\]: versão 1\.17 – Jan/2024:

\- Para gerações com leiaute anterior a EFD117:

  Campo 22 não deve ser gerado\.

\- Para gerações com leiaute a partir da EFD117 \(CAD\_LAYOUT – COD\_VERSAO>=117\): 

__   Cálculo pela Origem Movimentação da Produção \(SAFX16\):__

Soma os lançamentos do dia, totalizando o campo 07 da __SAFX16 __\(QTD\_FABR\), onde:

- O produto, campo 04 \(COD\_PRODUTO\) esteja parametrizado através da tela de parametrização de produto do módulo SPED FISCAL, como:

\- __*WDG – Hidratado*__, caso o produto apresentado no registro pai 1390 seja 01 – Álcool Hidratado; __\(\*\)__

\- __*WDG – Anidro*__, caso o produto apresentado no registro pai 1390 seja 02 – Álcool Anidro; __\(\*\)__

\- __*WDG – Álcool para outros fins*__, caso o produto apresentado no registro pai 1390 seja 08 – Álcool para outros fins\.

Caso a consulta não retornar registro de movimento, então gravar zero no campo QTD\_RESIDUO\_WDG\.

Ver RN1391\-20 onde o campo 22 é zerado quando encontrado no dia a produção de Bagaço de Cana juntamente com DDG e/ou WDG\. 

__\(Conversão de Medida\):__

Caso a unidade de medida__ __da produção \(campo “06\-Unidade de Medida” da SAFX16\) __ou__ 

Se a unidade de medida do movimento \(campo “33\-Unidade de Medida” da SAFX10\), conforme o caso, não seja tonelada \(<> ‘t’ e <> ‘T’\) será feita a conversão da quantidade para tonelada, *antes de totalizar o seu valor*\.

Verificar na __RN1391\-99__ as regras para conversão\.

__RN1391\-23__

__QTD\_RESIDUO\_ CANA __

\[__MFS577276__\]: versão 1\.17 – Jan/2024:

\- Para gerações com leiaute anterior a EFD117:

  Campo 21 não deve ser gerado\.

\- Para gerações com leiaute a partir da EFD117 \(CAD\_LAYOUT – COD\_VERSAO>=117\): 

__Cálculo pela Origem Movimentação da Produção \(SAFX16\):__

Soma os lançamentos do dia, totalizando o campo 07 da __SAFX16 __\(QTD\_FABR\), onde:

- O produto, campo 04 \(COD\_PRODUTO\) esteja parametrizado através da tela de parametrização de produto do módulo SPED FISCAL, como:

\- __*Bagaço da Cana – Hidratado*__, caso o produto apresentado no registro pai 1390 seja 01 – Álcool Hidratado; __\(\*\)__

\- __*Bagaço da Cana – Anidro*__, caso o produto apresentado no registro pai 1390 seja 02 – Álcool Anidro; __\(\*\)__

\- __*Bagaço da Cana – Açúcar,*__ caso o produto apresentado no registro pai 1390 seja 03 – Açúcar

\- __*Bagaço da Cana – Açúcar Mascavo*__ caso o produto apresentado no registro pai 1390 seja 04 – Açúcar Mascavo

\- __*Bagaço da Cana – Açúcar*__ __*Demerara*__ caso o produto apresentado no registro pai 1390 seja 05 – Açúcar Demerara

\- __*Bagaço da Cana – Açúcar*__ __*Cristal*__ caso o produto apresentado no registro pai 1390 seja 06 – Açúcar Cristal

\- __*Bagaço da Cana – Outros Açúcares*__ caso o produto apresentado no registro pai 1390 seja 07 – Outros Açúcares

\- __*Bagaço da Cana – Álcool para outros fins*__, caso o produto apresentado no registro pai 1390 seja 08 – Álcool para outros fins; __\(\*\)__

Lembrando que para estabelecimentos de Alagoas, de acordo com a data da geração, será considerado ou o produto 03\-Açúcar ou os produtos 04 \- Açúcar Mascavo, 05 \- Açúcar Demerara, 06 \- Açúcar Cristal e 07 – Outros Açúcares \(vide regra [RN1390](#ACUCAR)\)\.

Caso a consulta não retornar registro de movimento, então gravar zero no campo QTD\_RESIDUO\_CANA\.

Ver RN1391\-20 onde o campo 23 é zerado quando encontrado no dia a produção de Bagaço de Cana juntamente com DDG e/ou WDG\. 

__\(Conversão de Medida\):__

Caso a unidade de medida__ __da produção \(campo “06\-Unidade de Medida” da SAFX16\) __ou__ 

Se a unidade de medida do movimento \(campo “33\-Unidade de Medida” da SAFX10\), conforme o caso, não seja tonelada \(<> ‘t’ e <> ‘T’\) será feita a conversão da quantidade para tonelada, *antes de totalizar o seu valor*\.

Verificar na __RN1391\-99__ as regras para conversão\.

__RN1391\-99__

__Regras para Conversão de Medida:__

A conversão das unidades de medida será feita utilizando as tabelas de conversão de medida das seguintes opções de menu do Módulo DW:

\- ManutençãoàCadastrosàConversão das Unidades de Medidaà Padrão

\- ManutençãoàCadastrosàConversão das Unidades de Medidaà Por Produto

O fator de conversão é obtido conforme o procedimento padrão:

Primeiro, verificar se existe o fator de conversão na tabela de conversão por produto\. Se não existir, será utilizado o fator de conversão da tabela de conversão padrão\. 

Situação de erro na conversão de medida:

   Se o registro da conversão não for encontrado em nenhuma das situações \(conversão padrão ou

   conversão por produto\), será gravada uma mensagem de erro no log, e o dado a ser convertido não

   será considerado na geração \(seja inventário, movimento de estoque ou registro da SAFX16/X17\.

   Exempo:

    “*Fator de conversão de medida de XXX para XXX não encontrado\. O registro não será considerado*

*    na totalização dos valores”*

    Na coluna do log que mostra a chave do registro, será demonstrada a origem da informação, para

    facilitar o usuário na identificação do problema, da seguinte forma:

     Se origem = Inventário \(X52\):

*         “Inventário do produto X\-XXXXXXXXXXXXXXXXXXXXXXX \(X52\)”*

     Se origem = Estoque \(X10\):

*         “Movimento de estoque do produto X\-XXXXXXXXXXXXXXXXXXX na data 99/99/99 \(X10\)”*

     Se origem = Produto Fabricado \(X16\)

*         “Produto Fabricado: X\-XXXXXXXXXXXXXXXXXXX \(X16\)”*

     Se origem = Insumo utilizado \(X17\)

*        “Relação de Insumos: Produto X\-XXXXXXXXXXXXXX Insumo: X\-XXXXXXXXXXXXXX \(X17\)”*

Ao recuperar o fator de conversão, a busca deve ser feita para todos os códigos de unidade utilizados em cada caso\.

Exemplo:

No caso do campo “03\-QTD\_MOID”, supondo que o insumo da SAFX17 tenha unidade de medida = “KG”, então, será feita a conversão da quantidade para tonelada\. Para isso, a busca do fator de conversão deverá considerar todos os códigos utilizados na geração para identificar “tonelada”, ou seja:

Buscar conversão de ‘KG’ para ‘t’, se não existir, buscar de ‘KG’ para ‘T’\.

*\(isso porque na geração deste campo são utilizados os códigos ‘t’ e ‘T’ para identificar tonelada\)*

Como fazer a conversão:

Unidade destino = Unidade origem \* fator de conversão

Sendo:

unidade origem à é a unidade que consta no registro

unidade destino à é a unidade para qual se deseja converter a quantidade

Exemplos:

__Exemplo 1 \(conversão de kg para tonelada\)__:

Unidade do insumo na SAFX17 = kg

Quantidade do insumo na SAFX17 = 5\.000,00

Fator de conversão de kg para tonelada: 0,001

Aplicando a fórmula da conversão:

Quantidade em Tonelada = Quantidade em kg \* fator de conversão

Quantidade em Tonelada = 5\.000,00 \* 0,001 = 5,00

__Exemplo 2 \(conversão de tonelada para kg\)__:

Unidade do insumo na SAFX17 = tonelada

Quantidade do insumo na SAFX17 = 5,00

Fator de conversão de kg para tonelada: 1\.000,00

Aplicando a fórmula da conversão:

Quantidade em kg = Quantidade em tonelada \* fator de conversão

Quantidade em kg = 5,00 \* 1\.000,00 = 5\.000,00

__Observações importante__: 

\- Ao converter as unidades, utilizar campo com seis casas decimais \(como nas tabelas do Mastersaf\), assim como nos campos que farão a totalização do valor de cada campo do registro 1391\. O arredondamento para duas casas será feito __apenas no momento de gravar o registro__ \(observar que no arquivo todos os campos têm apenas 2 casas decimais\)\. Com esse procedimento, evitamos “perdas”, principalmente quando for necessário fazer conversão de medida\. 

\- Atenção ao efetuar a conversão de medidas, pois neste registro existem vários campos, que utilizam unidades diferenciadas, ora litro, ora kilo, ora tonelada, e alguns campos inclusive trabalham com duas unidades, dependendo do “grupo” do registro “pai” 1390, se for álcool ou açúcar\.__ __

# <a id="_Toc75782975"></a>Registro 1400 – Informação sobre Valores Agregados

As regras de geração do registro 1400 dependem do parâmetro “__Tipo de Geração__” da parametrização dos dados iniciais da EFD \(menu “Parâmetros à Dados Iniciais”\)\.

Existem dois tipos de geração:

__\-Padrão__ à É a geração original, feita na época da criação do registro 1400\. Não segue a regra específica de nenhuma UF, apenas as orientações do Guia Prático;

__\-Específico por UF__ à Modalidade de geração que atende as UF’s que possuem regras próprias para geração do 1400\. São as UF’s que divulgaram a tabela “*Tabela de Itens UF Índice de Participação dos Municípios*” no site da EFD\.

De acordo com o parâmetro “__Tipo de Geração__”, o 1400 será gerado \(quando marcado no perfil\) da seguinte forma:

*\(como as regras são bem diferentes, as definições de cada uma delas foram definidas separadamente\)*

__Parâmetro__

__Regras da Geração__

Opção “__Padrão__”

Neste caso será utilizada a geração original da criação do 1400\.

Consultar as seguintes regras:

RN1400, RN1400\-02, RN1400\-03 e RN1400\-04

Opção “__Específico por UF__”

Neste caso a geração será feita dependendo da UF do estabelecimento da geração:

__MFS43147__: incluído tratamento p/ o estado de AC

Se uf do Estabelecimento = “__AC__”:

       O 1400 será gerado de acordo com as regras específicas de AC\. 

       Consultar as regras no documento:

# MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_AC\.docx

__MFS94497__: incluído tratamento para o estado de AL\.

Se UF do Estabelecimento = “__AL__”: 

O 1400 será gerado de acordo com as regras específicas de MA\. 

Consultar as regras no documento:

__MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_AL\.docx__

<a id="OLE_LINK80"></a>

__MFS16811__: incluído tratamento p/o estado da BA

Se UF do Estabelecimento = “__BA__”:

     O 1400 será gerado de acordo com as regras específicas da BA\. 

     Consultar as regras no documento:

#               MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_BA\.docx

__MFS1507__: incluído tratamento p/o estado do ES

Se UF do Estabelecimento = “__ES__”:

     O 1400 será geração de acordo com as regras específicas do ES \(Portaria N\. 34\-R,

     Ago/2015\)\. Consultar as regras no documento:

__MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_ES\.docx__

__MFS47088__: incluído tratamento p/ o estado de MA

Se uf do Estabelecimento = “__MA__”:

       O 1400 será gerado de acordo com as regras específicas de MA\. 

       Consultar as regras no documento:

# MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_MA\.docx

__MFS45370:__ incluído tratamento p/o estado do MG

Se UF do Estabelecimento = “__MG__”:

       O 1400 será geração de acordo com as regras específicas de MG \(Resolução 4317, Dez/2014\)\. 

       Consultar as regras no documento:

__MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_MG\.docx__

__MFS30223__: incluído tratamento p/o estado de PE

Se UF do Estabelecimento = “__PE__”:

__MFS59468: __O 1400 será gerado de acordo com as regras específicas de PE \(Anexo 2 da Portaria SF Nº 126, de 30 de Agosto de 2018\)\. Consultar as regras no documento: 

# MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_PE\.docx

__MFS62608__: incluído tratamento p/o estado de PR

Se UF do Estabelecimento = “__PR__”:

     O 1400 será gerado de acordo com as regras específicas de PR\. Consultar as regras no documento:

MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_PR\.docx

__MFS23500: __incluído tratamento p/o estado de RJ

Se UF do Estabelecimento = “__RJ__”:

__MFS35221__: O 1400 será gerado de acordo com as regras específicas de RJ\. 

     Consultar as regras no documento:

__MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_RJ\.docx__

__MFS3132:__ incluído tratamento p/o estado do RN

Se UF do Estabelecimento = “__RN__”:

O 1400 será geração de acordo com as regras específicas do RN \(Orientação         Técnica EFD nº 011/2016, Jan/2016\)\. Consultar as regras no documento: 

__MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_RN\.docx__

__MFS7944__: incluído tratamento p/o estado do RS

Se UF do Estabelecimento = “__RS__”:

     O 1400 será geração de acordo com as regras específicas do RS *\(Obs: Até a*

*     liberação desta MFS ainda não havia sido divulgado nenhuma ato legal, apenas*

*     foi disponibilizada a tabela própria do RS no site da EFD\)\.*

     Consultar as regras no documento:

                __MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_RS\.docx__

<a id="OLE_LINK75"></a>

__MFS33871__: incluído tratamento p/o estado de SC

Se UF do Estabelecimento = “__SC__”:

__MFS40285: __O 1400 será gerado de acordo com as regras específicas de SC\. Consultar as regras no documento:

# MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_SC\.docx

Se UF do Estabelecimento = “__SP__”:

     O 1400 será geração de acordo com as regras específicas de SP \(Portaria CAT 137,

     Dez/2014\)\. Consultar as regras no documento:

                __MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_SP\.docx__

__MFS17764__: incluído tratamento p/o estado de TO

Se UF do Estabelecimento = “__TO__”:

     O 1400 será gerado de acordo com as regras específicas de TO \(<a id="OLE_LINK76"></a>Portaria nº 265,

# Mar/2018\)\. Consultar as regras no documento:

#               MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_TO\.docx

Se UF do Estabelecimento <> “__MG__” e <> “__SP__” e <> “__ES__” e <> “__RN__” e <> __“RS”__ <a id="OLE_LINK81"></a>e <> __“BA”__ e <> __“TO”__ e <> __“RJ” __e <> __“PE”__  e <> “__PR__” e <> “__AC__” e <> “__MA” e “AL”__\. 

     Nesse caso, o registro 1400 *não* será gerado, já que ainda *não* existem regras 

     específicas para nenhuma outra UF, além destas;

Não preenchido

 \(nulo\)

Nesse caso será considerada a opção “__Padrão__”

### <a id="_Toc75782976"></a>Regras da geração do 1400 para o tipo de geração = “Padrão”:

RN1400

Os valores a serem demonstrados neste registro são referentes aos seguintes segmentos:  Telecom, Energia Elétrica, Água, Transportes e também Aquisições de Produtos Primários\. Estes valores servirão para o cálculo do índice de participação dos municípios\.

__A geração deste registro é feita da seguinte forma: __

<a id="_Hlk68893159"></a>Total das Operações do período \(apurado automaticamente\)

\(\-\)

Deduções \(apurado automaticamente\)

\(\+\)

Outros Valores informados manualmente

\(\-\) 

Outras Deduções informadas manualmente

__Utilização do parâmetro “Calcular Valores por Produto” \(menu “Dados Iniciais”\):__

__Se__  parâmetro “Calcular Valores por Produto” = S 

      Calcula o VA por produto e município  

      Sobre o segmento de Transportes: os valores são calculados por produto *apenas*

      para os documento de modelo 07 \(NF de Serviços de Transportes\), que podem ter itens

      na SAFX08\. No caso dos conhecimentos de qualquer tipo \(notas com classificação = 4\) 

      os cálculos consideram apenas o município, já que estes documentos não têm itens na  

      SAFX08, aplicando neste caso, o parâmetro “Produto \(Telecom, Transporte, Energia Elétrica e EPPP\)”\. 

     __\[OS\-3417\]__ – \[MFS63191\]: Revisão da escrita da regra:

     __Se__ Conhecimento de Frete \(Notas com classificação = ‘4’\), então:

         Se o parâmetro “Produto \(Telecom, Transporte, Energia Elétrica e EPPP\)” for preenchido, então:

              Totalizar os valores por Município e informar no campo 02\-COD\_ITEM o produto parametrizado\.

         Se o parâmetro não for preenchido, então:

     Totalizar os valores por Município e o campo 02\-COD\_ITEM ficará nulo\.

     __Se__ NF de Serviços de Transportes \(Notas com classificação = ‘1’\), então:

          Não aplica o parâmetro “Produto \(Telecom, Transporte, Energia Elétrica e EPPP\)”\.

          Nota sem item – totalizar valores *apenas* por Município \(campo 182 da SAFX07\)\.

          Nota com item \- totalizar por produto \(produto da SAFX08\) e por Município \(campo 182 da SAFX07\)                                                                           

      Sobre o segmento de Energia Elétrica \(modelo 06\)__ \(MFS6919\)__: Para este segmento os 

      valores são totalizados por Produto e Município, mas, quando o  parâmetro “Produto

      \(Telecom,Transporte e Energia Elétrica \)” do menu “Dados Iniciais” for preenchido, os valores serão totalizados apenas por município, e no campo 02\-COD\_ITEM será informado sempre o produto parametrizado\. 

      Sobre o segmento de Telecom \(modelos 21, 22 e 62\)__ \(MFS20216\)__: Para este segmento os 

      valores são totalizados por Produto e Município, mas, quando o  parâmetro “Produto

      \(Telecom,Transporte e Energia Elétrica \)” do menu “Dados Iniciais” for preenchido, os valores serão totalizados apenas por município,  e no campo 02\-COD\_ITEM será informado sempre o produto parametrizado\. 

      Sobre Aquisição de Produtos Primários Próprios do Paraná \(EPPP\)__ \(MFS25117\)__: Para esta operação, os 

      valores são totalizados por Produto e Município, mas, quando o  parâmetro “Produto

      \(Telecom,Transporte e Energia Elétrica \)” do menu “Dados Iniciais” for preenchido, os valores serão  

      totalizados apenas por município, e no campo 02\-COD\_ITEM será informado sempre o produto 

     parametrizado\. 

__Se__  parâmetro “Calcular Valores por Produto” = N ou nulo

     Calcula o VA apenas por município \(para todos os casos\)

__Operações a serem tratadas:__

\-Aquisições de Produtos Primários

\-Telecom    \(saídas\)

\-EE            \(saídas\)

\-Água          \(saídas\)

\-Transporte  \(saídas\)

__Observações importantes__:

- A leitura das notas para totalização dos valores, deve tratar o conceito da Inscrição Estadual Única\. Assim, quando a geração for executada por __I\.E\.U__\., deve\-se considerar os documentos de todos os Estabelecimentos envolvidos na centralização; 
- As notas fiscais sem o __município __preenchido não serão processadas, e portanto, não irão compor o valor adicionado do município em questão \(para transportes e aquisição de produtos primários é o município de origem da SAFX07, e para Utilities é o município do ponto de consumo / terminal faturado da SAFX42\) \. Inicialmente, pensou\-se em gerar mensagens no log sobre estas notas, mas isso oneraria muito o processo da geração\. O ideal é fazer esta conferência no relatório a ser desenvolvido \(relatório de validação dos dados, que seria uma etapa prévia à geração do arquivo\)\.  

__Regras para a apuração dos valores:__

<a id="Etapa1"></a><a id="_Hlk68893320"></a>__Etapa 1:  Totalização do Valor das Operações do período__

<a id="_Hlk68893386"></a>Aquisição de Produtos Primários:

Totalizar o valor das notas de entrada gravadas no C100 que atendam as seguintes condições:

\(os critérios de filtro destas notas são os mesmos já definidos na RNC100, e deve\-se analisar a possibilidade de acumular estes valores durante a geração do C100\) 

 

__       *MFS\-22404, alterada pela MFS25117*__*: Esta MFS alterou a geração para contribuintes que praticam *<a id="_Hlk17301062"></a>*operações de Entrada de Produtos Primários Próprios, para utilizar o parâmetro “Produto \(Telecom, Transporte, Energia  Elétrica, EPPP \)”\.*

- Modelo \(campo 13\) =  01, 1B, 04 ou 55
- NFs Mercadoria \(Classificação 1 e 3\) 
- Somente notas com itens 
- Somente itens de mercadoria  
- Data Fiscal no período da geração ou data extemporânea no período de geração
- Movto\_E\_S <> ‘9’ \(somente entradas\)
- Situação = somente as não canceladas
- CFOP/Nat do item \- deve estar parametrizado no menu “Parâmetros à  Registro 1400 à Aquisição de Produtos Primários” __OU__

              CFOP/Nat do item \- deve estar parametrizado no menu “Parâmetros à  Registro 1400 à Aquisição de Produtos Primários \(EPPP\-PR\) e UF Estabelecimento = PR e parâmetro “Produto \(Telecom, Transporte, Energia Elétrica e EPPP \)” estiver preenchido no menu Parâmetros à Dados Iniciais”

- Município de origem \(campo 182 da SAFX07\) deve ser um município da UF do Estabelecimento
- Desconsiderar os registros de modelo 01 que são mapas resumos originados da movimentação de Utilities \(mesma regra usada no filtro do C100\)

OBS: Como as regras são as mesmas do C100, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR do registro analítico \(C190\)\.

__\[MFS26339\] __

__Se__ parâmetro “Considerar somente Pessoa Física para a geração da Aquisição de Produtos Primários” \(menu “Dados Iniciais”\): = S 

     Recuperar somente notas fiscais em que a Pessoa Física/Jurídica seja Pessoa 

     Física, verificando se o campo CPF/CNPJ \(campo 6 da SAFX04\) tem 11   

     caracteres

__Senão__

     Recuperar todas as notas fiscais, independente de ser Pessoa Física ou Jurídica\. 

Valor a ser totalizado = valor contábil do item

__Se__ parâmetro “Calcular Valores por Produto” = S 

       __Se__  UF Estabelecimento = PR __E__ CFOP/Nat do item \- deve estar   

             parametrizado no menu “Parâmetros à  Registro 1400 à Aquisição de 

             Produtos Primários \(EPPP\-PR\) __E__ parâmetro “Produto \(Telecom, Transporte,    

             Energia Elétrica e EPPP \)” estiver preenchido

            Neste caso os valores serão totalizados apenas por município, e o campo

            02\-COD\_ITEM será gerado sempre com o produto parametrizado \(ver

            RN1400\-02\. __*Obs\.:*__ Responsabilidade do usuário colocar como EPPP\)

       __Senão__

           Totalizar por Produto \(da SAFX08\) e Município \(campo 182 da SAFX07\)

__Senão__

     Totalizar por Município \(campo 182 da SAFX07\)

<a id="_Hlk68893406"></a>Telecom / Energia Elétrica / Água: 

Na prática, todas as notas fiscais __de saída__ gravadas nos registros específicos de Telecom \(D500, D600 e D695\), ou de EE/Água \(C500/C600/C700\) deverão ser totalizadas para geração dos valores do registro 1400\.

Obs: A exceção é o segmento de fornecimento de Gás, que até então não esta no escopo deste registro\. *Portanto, quando se tratar deste tipo de empresa não será necessário efetuar o procedimento de geração do 1400*\. As empresas de gás podem ser identificadas pelo CNAE do estabelecimento que deve ser = 4020701, 4020702, 3520401 ou 3520402 \(vide RNC500\)\. 

Obs: A solução de como totalizar estes valores deve ser estudada com cuidado, pois o registro 1400 será solicitado somente em algumas UF’s\.  

Independente de como será a solução técnica para gerar estes valores, segue critérios para filtro das notas na SAFX42/SAFX43\.

<a id="Criterios_Recuperacao_Notas"></a>__Critérios para Recuperação das Notas:__

__\[MFS95773\] Inclusão da utilização do modelo 66__

__MFS436036__ Inclusão das notas de modelo 62 \(NFCom\) nas Saídas \(SAFX42/43\)\. As notas de saída de modelo 62 consideradas para geração do 1400, são as apresentadas nos registros D700/D750\. Sendo assim, pelo menos um desses registros deve estar selecionado no perfil de geração para que essas notas venham a compor o 1400\.

Totalizar o valor do serviço das notas da SAFX42/SAFX43 que atendam aos seguintes critérios: 

\- Modelo \(campo 13 da SAFX42\) = todos \(01, 06, 21, 22, 29, ‘62’ e 66\)

  \(a única exceção é o Gás\)

\- Data Fiscal \(campo 03\) no período da geração ou data extemporânea no período de

   Geração

\- __\[ALTERADA – CH11946\_2013\]__ Somente itens de mercadoria \(no caso das notas 

  mistas, totalizar *apenas* o valor dos itens de mercadoria e serviço, pois o Guia

  Prático cita que os serviços  devem ser deduzidos da aquisição, ou seja, diferença

  entre os CFOPs de saída e os CFOPs de entrada conforme parametrização das

  deduções\)

\- Situação = somente as não canceladas

\- Não considerar os itens informativos \(itens da SAFX43 com o campo 10\-Tipo de

   Item = 1\)

\- Município de Terminal Faturado \(campo 76 da SAFX42\) deve ser um município da

  UF do Estabelecimento 

OBS: Como as regras são as mesmas dos registros específicos \(C500/C600/C700 para EE e Água, e D500/D600/D696 para Telecom\), além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR dos registros analíticos \(C590, C690 etc \.\.\.\)\.

__Totalização das Notas recuperadas :__

<a id="_Hlk68899133"></a>__Telecom / Água__: __\[MFS35568\]__:

Para Telecom e Água vale a regra a seguir, especificada pela __MFS35568__\.

A totalização das notas recuperadas passou a ser feita da seguinte forma: deve somar o Valor do Serviço dos itens de adição, e subtrair o Valor do Desconto dos itens de dedução, da seguinte forma:

	

Valor a ser totalizado = 

       Se item de adição, soma o __valor do serviço__ \(campo 19 SAFX43\);

       Se item de dedução, subtrai o __valor do desconto__ \(campo 18 da SAFX43\); 

        *\(ao subtrair o valor do desconto, considerar sempre o valor absoluto\)*

\(Itens de __adição__ são os itens com o campo “20\-Adição/Desconto” __nulo__ ou = “__A__”\);

\(Itens de __dedução__ são os itens com o campo “20\-Adição/Desconto” = “__D__”\);

Exemplo: supondo as notas abaixo para um mesmo município do ponto de Consumo:

   Nota 101: Item 1, Adição/ Desc\. = “__A__”, Valor do Serviço = 1\.000,00

                    Item 2, Adição/ Desc\. = “__A__”, Valor do Serviço = 500,00

   Nota 102: Item 1, Adição/ Desc\. = “__A__”, Valor do Serviço = 2\.000,00

                    Item 2, Adição/ Desc\. = “__D__”, Valor do Desconto = 300,00

   Valor totalizado = __3\.200,00__ \(1\.000,00 \+ 500,00 \+ 2\.000,00 – 300,00\)

__Energia Elétrica__ __\[MFS35568\]__  \[__MFS46087 e MFS58137\]__

__\[MFS95773\] Inclusão da utilização do modelo 66__

A regra especificada pela__ MFS35568__ foi definida pela CPFL, mas ao realizar a homologação, se deparou que esta não cobria alguns cenários\. O cliente revisou a regra e nos apresentou em duas reuniões realizadas em 14/09/2020 e 28/10/2020 \([https://web\.microsoftstream\.com/video/2caeaf7f\-d9ed\-4c2d\-a8c3\-ce91bf5a5612](https://web.microsoftstream.com/video/2caeaf7f-d9ed-4c2d-a8c3-ce91bf5a5612) e [https://web\.microsoftstream\.com/video/748955af\-413a\-45ac\-a8cd\-25dfb72f94b3](https://web.microsoftstream.com/video/748955af-413a-45ac-a8cd-25dfb72f94b3)\)\. A regra se aplica apenas a Energia Elétrica e está sendo implementada pelas __MFS46087 e MFS58137__\. 

Essa regra consiste em somar as bases de ICMS Tributada, Isenta e Outras, de acordo determinados códigos de Situação Tributária B e subtrair o Valor do Desconto dos itens de dedução\. Além disso os itens de Dedução tem tratamento particular para cada tipo de base\. Veja o cálculo de cada parcela que compõe o valor da Operação para Energia Elétrica\.

__>> Base Tributada de ICMS__:

Para calcular a Base Tributada de ICMS, recuperar os itens da SAFX43 que atendam aos critérios:

- [Critérios para recuperação de notas](#Criterios_Recuperacao_Notas), conforme definidos no início da regra;
- Modelo \(campo 13 da SAFX42\) = “06” e ‘66’;
- Código Situação Tributária B \(campo 33 da SAFX43\)= __“00__”;
- Base Tributada ICMS \(campo 23 da SAFX43\) > 0,00;

Para esses itens, recuperar os campos:

- Base Tributada ICMS \(campo 23 da SAFX43\); 
- Valor do Desconto \(campo 18 da SAFX43\);
- Adição/Desconto \(campo 20 da SAFX43\);

Base Tributada de ICMS = 

Somatório da Base Tributada ICMS de todos os itens acima recuperados,

Subtrair o Valor do Desconto dos itens com campo “20\-Adição/Desconto” = “__D__”, Subtrair o Valor do Desconto dos itens com campo “20\-Adição/Desconto” = “__D__”

Obs: 

O valor do Desconto é subtraído duas vezes, pois um é o próprio valor do desconto e o outro é a Base Tributada ICMS Negativada, que na prática é o mesmo valor do desconto\. Explicação dada na reunião de 14/09/2020: [https://web\.microsoftstream\.com/video/2caeaf7f\-d9ed\-4c2d\-a8c3\-ce91bf5a5612](https://web.microsoftstream.com/video/2caeaf7f-d9ed-4c2d-a8c3-ce91bf5a5612" \t "_blank)

Como o campo “20\-Adição/Desconto” não é obrigatório, caso esteja __nulo__ é considerado como item de Adição \(“__A__”\)\.

__>> Base Isenta de ICMS__:

Para calcular a Base Isenta de ICMS, recuperar os itens da SAFX43 que atendam aos critérios:

- [Critérios para recuperação de notas](#Criterios_Recuperacao_Notas), conforme definidos no início da regra;
- Modelo \(campo 13 da SAFX42\) = “06” e ‘66’;
- Código Situação Tributária B \(campo 33 da SAFX43\)= “__40__”;
- Base Isenta ICMS \(campo 24 da SAFX43\) > 0,00;
- __Desconsiderar__ os itens com Adição/Desconto = “__D__” \(campo 20 da SAFX43\);
- __MFS58137:__ Considerar todos os produtos ou apenas os Parametrizados com Isenção de ICMS, conforme regra a seguir:
- Caso a opção “__Utilizar a parametrização de produtos com Isenção de ICMS para Energia Elétrica__” esteja marcada na Tela de Dados Iniciais, então:

Considerar apenas itens da SAFX43 com Produtos \(campos 11 e 12\) pertencentes à Parametrização de Produtos com Isenção de ICMS \(menu: Parâmetros >> <a id="_Hlk59893211"></a>Registro 1400 >> Padrão >> Serviço de Energia Elétrica >> Produto com Isenção de ICMS\)

- Caso a opção “__Utilizar a parametrização de produtos com Isenção de ICMS para Energia Elétrica__” esteja desmarcada na Tela de Dados Iniciais, então:

Todos os produtos devem ser considerados, não aplicando a Parametrização de Produtos com Isenção de ICMS\.

Para esses itens, recuperar o campo:

- Base Isenta ICMS \(campo 24 da SAFX43\); 

Base Isenta de ICMS = Somatório Base Isenta ICMS dos itens recuperados

__>> Base Outras de ICMS \(CST de Diferimento\):__

Para calcular a Base Outras de ICMS, recuperar os itens da SAFX43 que atendam aos critérios:

- [Critérios para recuperação de notas](#Criterios_Recuperacao_Notas), conforme definidos no início da regra;
- Modelo \(campo 13 da SAFX42\) = “06” e ‘66’;
- Código Situação Tributária B \(campo 33 da SAFX43\)= “__51__”;
- Base Outras ICMS \(campo 25 da SAFX43\) > 0,00;
- __Desconsiderar__ os itens com Adição/Desconto = “__D__” \(campo 20 da SAFX43\);

Para esses itens, recuperar o campo:

- Base Outras ICMS \(campo 25 da SAFX43\); 

Base Outras de ICMS = Somatório Base Outras ICMS dos itens recuperados

__>> Desconto ST:__

Para calcular o Desconto ST, recuperar os itens da SAFX43 que atendam aos critérios:

- [Critérios para recuperação de notas](#Criterios_Recuperacao_Notas), conforme definidos no início da regra;
- Modelo \(campo 13 da SAFX42\) = “06” e ‘66’;
- itens com Adição/Desconto = “__D__” \(campo 20 da SAFX43\);
- __MFS58137:__ Considerar todos os produtos ou apenas os Parametrizados com Desconto, conforme regra a seguir:
- Caso a opção “__Utilizar a parametrização de produtos com Desconto para Energia Elétrica__” esteja marcada na Tela de Dados Iniciais, então:

Considerar apenas itens da SAFX43 com Produtos \(campos 11 e 12\) pertencentes à Parametrização de Produtos com Desconto \(menu: Parâmetros >> Registro 1400 >> Serviço de Energia Elétrica >> Produto com Desconto\)

- Caso a opção “__Utilizar a parametrização de produtos com Desconto para Energia Elétrica__” esteja desmarcada na Tela de Dados Iniciais, então:

Todos os produtos devem ser considerados, não aplicando a Parametrização de Produtos com Desconto\.

Para esses itens, recuperar o campo:

- Valor do Desconto \(campo 18 da SAFX43\); 

Desconto ST = Somatório do Valor do Desconto dos itens recuperados

__>> Valor final da Etapa 1__:

__Valor a ser totalizado__ = Base Tributada de ICMS \+ 

                                        Base Isenta de ICMS \+ 

                                        Base Outras de ICMS \- 

                                        Desconto ST

Obs:

A [Etapa 2](#Etapa2) \(Totalizar os valores de deduções\) continua sendo executada, apesar do tratamento das deduções já estar imbutido nessa regra\.  Como as deduções definidas na Etapa 2 são executadas com base na parametrização por CFOP/Nat, basta o cliente não utilizar tais parametrizações para que o cálculo do VA siga fielmente a regra especificada na Etapa1\.

__Totalizar Por Município, ou, Por Produto e Município:__

__Se__ parâmetro “Calcular Valores por Produto” = S 

__      MFS6919__ \(ch 18552/16\): Este MFS alterou a geração para o segmento de EE

      \(mod 06\), para utilizar o parâmetro “Produto \(Telecom, Transporte, Energia 

       Elétrica e EPPP \)”\.

__      MFS20216__: Este MFS alterou a geração para o segmento de Telecom

      \(mod 21 e 22\), para utilizar o parâmetro “Produto \(Telecom, Transporte, Energia 

       Elétrica e EPPP\)”\.

__      MFS436036__ Inclusão das notas de modelo 62 \(NFCom\) nas Saídas \(SAFX42/43\)

     __Se__ modelo dos documentos <> 06 e ‘66’ \(segmentos <> EE\) ou 

           modelo dos documentos <> 21, 22 e ‘62’ \(segmentos <> Telecom\): 

          Totalizar por Produto \(da SAFX43\) e Município \(campo 76 da SAFX42\);

     __Senão__ \(documentos de modelos 06, 66, 21, 22 e ‘62’\): 

           __Se__  parâmetro “Produto \(Telecom, Transporte, Energia Elétrica e EPPP \)” 

                 estiver preenchido,

                 Neste caso os valores serão totalizados apenas por município, e o campo

                 02\-COD\_ITEM será gerado sempre com o produto parametrizado \(ver

                 RN1400\-02\)\.

           __Senão__

               Totalizar por Produto \(da SAFX43\) e Município \(campo 76 da SAFX42\);

__Senão__

     Totalizar por Município \(campo 76 da SAFX42\)

__MFS\-20147:__ Essa alteração se faz necessária por conta de alguns critérios adotados pela CPFL, segue:

- Utilização de CST 090 para operações que não possuem fato gerador do ICMS \(CIP, Seguros, Juros, Multa, Atualização Monetária, etc\) e que precisam ser desconsiderados da composição do valor adicionado das operações que ocorrem fato gerador, pois não há legislação que determina uma situação tributária específica para esse cenário fiscal e pode acontecer com qualquer contribuinte que possui atividades ativas com energia elétrica, água e telecomunicaçãoes, porque são segmentos que não possuem cobranças, em Nota Fiscal, ausentes à sua operação, ou seja, não existem documentos de entrada escriturados para deduzir as saídas\.

__Exclusão Itens s/ Receita__

__Alterada \[MFS30891\]__

Para cada combinação de produto e município ou somente município conforme totalização a seguir, se houver parametrização de CST na tela de “Exclusão de Itens sem Receita – Por CST”, do módulo SPED à EFD\-Escrituração Fiscal Digital, item de menu: Parâmetros >> Registro 1400 >> Padrão >> Exclusão Itens S/ Receita >> Por CST, então:

- Nesse cenário em específico desconsiderar os itens de serviço na composição do valor da totalização\.

Obs: Com a reformulação da regra para Energia Elétrica definida pela CPFL, pelas __MFS46087 e MFS58137__, a Exclusão de Itens s/ Receita não tem mais aplicabilidade para o cálculo do __Valor das Operações do período__ \(__Etapa 1\)__\.

*Exemplo:*

NF 100

Município do Ponto de Consumo = PR 21802 \(RIBEIRAO CLARO\)

Item 1

Produto A

__CST 90__

Adição/ Desc\. = Adição

Valor do Serviço = 300,00

Item 2

Produto B

__CST 00__

Adição/ Desc\. = Adição

Valor do Serviço = 50,00

NF 101

Município do Ponto de Consumo = PR 21802 \(RIBEIRAO CLARO\)

Item 1

Produto A

__CST 00__

Adição/ Desc\. = Adição

Valor do Serviço = 200,00

Paramêtro de Exclusão = __CST 90__

Se totalização por município parâmetro “Produto \(Telecom, Transporte, Energia Elétrica e EPPP \)” = A

*Totalização por Município = *

*|1400|A|4121802|250,00| \(se for valor negativo ou 0 desconsiderar do arquivo, para valor negativo será emitida a mensagem de log descrita nessa RN\)*

*Totalização por Produto e Município = *

*|1400|A|4121802|200,00| \(se for valor negativo ou 0 desconsiderar do arquivo, para valor negativo será emitida a mensagem de log descrita nessa RN\)*

*|1400|B|4121802|50,00| \(se for valor negativo ou 0 desconsiderar do arquivo, para valor negativo será emitida a mensagem de log descrita nessa RN\)*

__MFS35568: __Desfaz o procedimento abaixo, implementado pela MFS30891, onde o valor do campo Desconto dos itens de dedução era subtraído do total das notas, com base na parametrização por CST e Produto \(menu “Dedução à Por CST x Produto”\)\. Esta parametrização *foi retirada do módulo*, e a dedução do Desconto dos itens de dedução passou a ser feita no junto com a totalização das notas, ou seja, a partir das próprias notas processadas \(vide regra acima, item “Totalização das Notas Recuperadas”\)\. 

OBS: a totalização das operações de Utilities não pode ser pela SAFX07/SAFX08 pois não há a informação do Terminal Faturado, pois este dado não é tratado na geração do Mapa Resumo\. \(a informação de terminal faturado que existe na SAFX07 foi incluída recentemente para atender ao AC 70, e é utilizado apenas para as notas de entrada\)\.

<a id="_Hlk68893792"></a>Energia Elétrica \(Operações Específicas – Modelo 55\):

A partir da OS4045, a geração do 1400 passou a totalizar também as operações especiais de venda de EE \(modelo 55\) para compor os valores do registro 1400:

*\(operações próprias de empresas cuja atividade final *não* é o fornecimento de EE\)*

*\(para maiores informações, vide item “Introdução” do requisito da OS4045\)*

 

Será feita a totalização do valor das operações definidas como venda de EE de modelo 55, que são as notas fiscais com CFOP ou CFOP/Nat parametrizadas no menu “Parâmetros à Registro 1400 àOperações Específicas de Venda de EE \(Modelo 55\):

\- Notas da __SAFX07__/__SAFX08__;

\- Movto\_E\_S = ‘9’ \(somente saídas\);

\- Situação = somente as não canceladas;

\- Classificação = 1 ou 3; 

\- Data Fiscal no período da geração ou data extemporânea no período de geração

\- Notas de modelo 55 \(NF\-e\);

\- CFOP ou CFOP/Natureza parametrizados no menu “Parâmetros à Registro 1400 à

  Operações Específicas de Venda de EE \(Modelo 55\); 

MFS13293

\- SE UF<> SC ENTÃO

  O município de origem \(\*\) deve estar preenchido \(campo 182 da SAFX07\), e deve ser

  um município da UF do estabelecimento;

  SENÃO

      UF= SC considerar o muncipio de destino \(campo 183 da SAFX07\), e a UF destino \(campo 122 da SAFX07\)

*\(\*\) Neste caso será utilizado o município do campo 182, pois o município do ponto de consumo \(campo 208\) da SAFX07 é utilizado para as notas de entrada de EE, conforme orientações do Manual de Layout\.*

Valor a ser totalizado:

- Valor contábil dos itens da SAFX08;

Utilização do parâmetro “Calcular Valores por Produto”:

      Se parâmetro “Calcular Valores por Produto” = S 

           Totalizar por Produto \(da SAFX08\) e Município \(campo 182 da SAFX07\)

      Senão

           Totalizar por Município \(campo 182 da SAFX07\)

<a id="_Hlk68893866"></a><a id="_Hlk68898150"></a>Transporte: 

Na prática, todas as notas fiscais __de saída__ gravadas no registro D100 deverão ser totalizadas para geração dos valores do registro 1400\.

Os critérios de filtro destas notas são as mesmas já definidas na RND100, e deve\-se analisar a possibilidade de acumular estes valores durante a geração do D100\. 

- Modelo \(campo 13\) = 07, 08, 8B, 09, 10, 11, 26, 27 e 57

              \(todos os modelos gravados no D100\)

              \(observar pelas regras de filtro do D100 que até hoje, 17/12/08, 

               os modelos 26 e 27 ainda não foram tratados no D100\)

- Classificação = 1 ou 4

             \(a nf de modelo 07 usa classificação 1 e os conhecimentos classificação 4\)

- Data Fiscal no período da geração ou data extemporânea no período de geração
- Movto\_E\_S = ‘9’ \(somente saídas\)
- Situação = somente as não canceladas
- Município de origem \(município onde ocorreu o início da prestação do serviço\)\. É o campo 182 da SAFX07, e deve ser um município da UF do Estabelecimento; 

OBS: Como as regras são as mesmas do D100, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR do registro analítico \(D190\)\.

Valor a ser totalizado:

- No caso da classificação 4 \(a nota não terá itens\),  utilizar o valor total da nota da SAFX07; 
- No caso da classificação 1 \(são as notas de modelo 07, que podem ou não ter itens\), Usar o procedimento padrão \(se tiver itens, totalizar pelo valor contábil do item, caso contrário, pelo valor total da capa\);

<a id="_Hlk68892476"></a>Sobre a utilização do parâmetro “Calcular Valores por Produto”:

 

Se parâmetro “Calcular Valores por Produto” = S 

     Se nota de modelo 07 \(notas com classificação = ‘1’\)

          Nota sem item \- totalizar *apenas* por Município \(campo 182 da SAFX07\)

          Nota com item \- totalizar por produto \(produto da SAFX08\) e por Município

                                                                                    \(campo 182 da SAFX07\)                                                                           

     Senão  \(conhecimentos de qualquer modelo\) \(notas com classificação = ‘4’\)

          Totalizar *apenas* por Município \(campo 182 da SAFX07\)

          __\[OS\-3417\]__ – \[MFS63191\]: Revisão da escrita da regra:

         Se o parâmetro “Produto \(Telecom, Transporte, Energia Elétrica e EPPP\)” for 

         preenchido, então:

              Informar no campo 02\-COD\_ITEM o produto parametrizado\.

         Se o parâmetro não for preenchido, então:

     O campo 02\-COD\_ITEM ficará nulo\.

__Senão__

\[__ALTERAÇÃO__\-__MFS67283__\] Tratamento cálculo *apenas* por Município\.

Tratamento:

Se parâmetro “Calcular Valores por Produto” = N 

 Totalizar *apenas* por Município \(campo 182 da SAFX07\)

    Se o parâmetro “Produto \(Telecom, Transporte, Energia Elétrica e EPPP\)” estiver 

         preenchido, então:

              Prencher o campo 02 \- COD\_ITEM com o produto parametrizado\.

         Se o parâmetro não estiver preenchido, então:

     O campo 02\-COD\_ITEM ficará nulo\.

OBS: Para o segmento de Transportes o produto só é utilizado nas notas fiscais de modelo 07, que não é um conhecimento, e sim uma nota fiscal, e portanto pode ter itens na SAFX08\. Os conhecimentos da SAFX07 não têm itens na SAFX08, e portanto não há produto a ser utilizado \(os itens dos CTRC’s ficam na SAFX51, e são, na realidade, as informações das notas fiscais transportadas nos conhecimentos de transporte\)\.

 

<a id="Etapa2"></a><a id="_Hlk68893902"></a>__Etapa 2:  Totalizar os valores de deduções__

<a id="_Hlk68895651"></a>Totalizar o valor das operações definidas como dedução, que são as notas fiscais com CFOP ou CFOP/Nat parametrizadas no menu “Parâmetros à Registro 1400 à Deduções”\.

O valor das deduções será subtraído do valor das operações apurado na etapa 1\. 

<a id="_Hlk68895623"></a>A idéia desta parametrização é permitir a dedução de alguma operação totalizada na etapa 1, que não possa ser considerada para compor o VA\.

<a id="_Hlk68895674"></a>As deduções devem ser pesquisadas tanto na SAFX07/SAFX08, como na SAFX42/SAFX43\. O motivo é o fato de diferentes UF’s poderem ter diferentes regras para a apuração do VA\. Assim, podemos prever que qualquer tipo de operação possa ser uma dedução\.

Considerar também que uma dedução pode ser uma operação tanto de entrada, como de saída\. 

__\[MFS99537\]  Inclusão do Modelo 62__

__MFS436036__ Inclusão das notas de modelo 62 \(NFCom\) nas Saídas \(SAFX42/43\)

__\[MFS710674\] __Inclusão do modelo de nota “66”

Para seleção das notas na __SAFX07/SAFX08__:

- Modelo \(campo 13\) =  os mesmos modelos tratados na Etapa1, ou seja, 01, 1B, 04,  55, 06, 66, 21, 22, 29, 07, 08, 8B, 09, 10, 11, 26, 27, 57 e 62 
- NFs Mercadoria ou Mista \(Classificação 1 ou 3\) 
- __\[ALTERADA – CH11946\_2013\]__  Somente itens de mercadoria \(no caso das notas mistas, totalizar apenas o valor dos itens de mercadoria e serviço, pois o Guia Prático cita que os serviços  devem ser deduzidos da aquisição, ou seja, diferença entre os CFOPs de saída e os CFOPs de entrada conforme parametrização das deduções\)
- Situação = somente as não canceladas
- Data Fiscal no período da geração ou data extemporânea no período de geração
- Movto\_E\_S = qualquer \(entradas e saídas\)
- CFOP/Nat do item \- deve estar parametrizado no menu “Parâmetros à  Registro 1400 à Deduções
- Para as notas com itens, totalizar o valor contábil do item \(SAFX08\)
- Para as notas sem itens, totalizar o valor total da nota \(SAFX07\)
- As notas que são mapa resumo de Utilities devem ser *desconsideradas*, pois estas notas serão contabilizadas a partir das tabelas SAFX42/SAFX43\. Se não for feito este procedimento, há risco de duplicação de valores\.
- Para as notas de mercadoria ou transporte, *utilizar o Município de Origem* \(campo 182 da SAFX07\), que deverá estar preenchido e deve ser um município da UF do Estabelecimento;
- Para as notas de entradas de Utilities \(as saídas não serão processadas\!\), ou seja, os modelos 06, 21, 22, 29 e ainda o modelo 01\(quando a pessoa fis/jur fornecedora estiver parametrizada como “Fornecedores de Gás Canalizado”\), *utilizar o Município do Terminal Faturado *\(campo 208 da SAFX07\), que deverá estar preenchido e deve ser um município da UF do Estabelecimento;

 Para seleção das notas na __SAFX42/SAFX43__:

- Modelo \(campo 13\) =  qualquer
- Situação = somente as não canceladas
- NFs Mercadoria ou Mista \(Classificação 1 ou 3\) 
- Data Fiscal no período da geração ou data extemporânea no período de geração
- CFOP/Nat do item \- deve estar parametrizado no menu “Parâmetros à  Registro 1400 à Deduções
- Município de Terminal Faturado \(campo 76 da SAFX42\) deve ser um município da UF do Estabelecimento 
- Totalizar o valor do serviço do item \(campo 19 da SAFX43\)

<a id="_Hlk68895781"></a>A <a id="_Hlk68896491"></a>totalização das notas por Produto/Município ou apenas Município, deve seguir a mesma lógica da [etapa 1](#Etapa1), ou seja:

__Notas da SAFX42/SAFX43__:

__Se__ parâmetro “Calcular Valores por Produto” = “S”

__      MFS6919__ \(ch 18552/16\): Este MFS alterou a geração para o segmento de EE

      \(mod 06\), para utilizar o parâmetro “Produto \(Telecom, Transporte, Energia Elétrica e EPPP\)”\.

__       MFS20216__: Este MFS alterou a geração para o segmento de Telecom

      \(mod 21 e 22\), para utilizar o parâmetro “Produto \(Telecom, Transporte, Energia  Elétrica e EPPP\)”\.

       

     __Se__ modelo dos documentos <> 06 \(segmentos <> EE\) ou 

           modelo dos documentos <> 21, 22 e ‘62’\(segmentos <> Telecom\) ou

          Totalizar por Produto \(da SAFX43\) e Município \(campo 76 da SAFX42\);

     __Senão__ \(documentos de modelos 06, 21, 22 e ‘62’\): 

           __Se__  parâmetro “Produto \(Telecom, Transporte, Energia Elétrica e EPPP\)” estiver 

                 preenchido,

                 Neste caso os valores serão totalizados apenas por município, e o campo

                 02\-COD\_ITEM será gerado sempre com o produto parametrizado \(ver

                 RN1400\-02\)\.

           __Senão__

               Totalizar por Produto \(da SAFX43\) e Município \(campo 76 da SAFX42\);

__Senão __

     totalizar por Município \(campo 76 da SAFX42\)

__Notas da SAFX07/SAFX08__:

è Para as notas de entradas de Utilities

     \(modelos 06, 21, 22, 28 ou 29 ou 62\)  ou

     \(modelo 01 e pessoa fis/jur parametrizada como “Fornecedores de Gás Canalizado”\) __\(\*\)__

   

      Se parâmetro “Calcular Valores por Produto” = S 

           Totalizar por Produto \(da SAFX08\) e Município Ponto Consumo/Terminal Faturado

                                                                                              \(campo 208 da SAFX07\)

            Obs: Considerar a mesma regra descrita acima \(__MFS6919 e MFS20216__\)

      Senão 

           Totalizar pelo Município Ponto Consumo/Terminal Faturado \(campo 208 da 

           SAFX07\)

<a id="_Hlk68898400"></a><a id="_Hlk68898427"></a>è Para as notas de Transportes \(modelo 07, 08, 8B, 09, 10, 11, 26, 27 e 57\)

       \[MFS63191\]: Revisão da escrita da regra:

     __OS\-3417: __Este MFS alterou a geração para o segmento de Transporte\. Nota de conhecimeno de frete passa a utilizar o parâmetro “Produto \(Telecom, Transporte, Energia Elétrica e EPPP\)”\.

     Se parâmetro “Calcular Valores por Produto” = S 

          Se nota de modelo 07 \(notas com classificação = ‘1’\)

               Nota sem item \- totalizar *apenas* por Município \(campo 182 da SAFX07\)

               Nota com item \- totalizar por produto \(produto da SAFX08\) e por Município

                                                                                        \(campo 182 da SAFX07\)                                                                           

          Senão  \(conhecimentos de qualquer modelo\)

               Totalizar *apenas* por Município \(campo 182 da SAFX07\)

               __\[OS\-3417\]__ – \[MFS63191\]: Revisão da escrita da regra:

              Se o parâmetro “Produto \(Telecom, Transporte, Energia Elétrica e EPPP\)” for 

              preenchido, então:

                 Informar no campo 02\-COD\_ITEM o produto parametrizado\.

              Se o parâmetro não for preenchido, então:

        O campo 02\-COD\_ITEM ficará nulo\.

     Senão

          Totalizar *apenas* por Município \(campo 182 da SAFX07\)

è Para qualquer outro tipo de nota

      \(modelos 01, 1B, 04 e  55\)

 

      Se parâmetro “Calcular Valores por Produto” = S

           Totalizar por Produto \(da SAFX08\) e Município \(campo 182 da SAFX07\)

__Senão__

\[__ALTERAÇÃO__\-__MFS67283__\] Tratamento cálculo *apenas* por Município\.

__Tratamento__:

Se parâmetro “Calcular Valores por Produto” = N 

      Totalizar *apenas* por Município \(campo 182 da SAFX07\)

__OBS: __Caso seja recuperado valor na [Etapa 2](#Etapa2), deverá ser gravado no quadro “Valores Calculados” no campo “Deduções” \(Campo VLR\_DED\_CALC da tabela EFD\_REG\_1400\), para o mesmo município calculado na [Etapa 1](#Etapa1), \(Valor gravado no Campo VLR\_AGREG\_CALC da tabela EFD\_REG\_1400\), caso contrário o sistema deverá seguir considerando somente os valores calculados na [Etapa 1](#Etapa1),  

__\(\*\)__ parametrização de Pessoa Fis/Jur x Ramos de Atividades \(módulo DW, menu  “Manutenção à Cadastro Parâmetros”\);

__OBS__: atenção às diferenças na totalização por produto/município entre os diferentes tipos de notas, que são basicamente:

__Etapa 3:  Subtrair as deduções apuradas__

Calcular o valor de cada Produto/Município ou Município \(conforme foi feita a totalização\), da seguinte forma:

                  \[VA =  valor das operações \([Etapa 1](#Etapa1)\) – deduções \([Etapa 2](#Etapa2)\)\]

__Etapa 4:  Considerar valores manuais e calcular o resultado final do VA__

Antes de gravar os valores calculados, deve\-se verificar se existem valores informados manualmente, através do menu “Geração à Manutenção – Registro 1400”\.

Nesta tela o usuário pode informar dois tipos de valores:

1\- “Outros Valores” – são valores para compor o VA \(devem ser somados ao VA calculado\) 

2\- “Outras Deduções” – são valores de deduções \(devem ser subtraídas do VA calculado\)

Os valores manuais também são informados por Produto / Município ou apenas Município, da mesma forma em que é feita a apuração automática\.

Logo, para os Produtos / Municípios ou Municípios que tiverem valores manuais, deve\-se contabilizá\-los da seguinte forma:

                       \[VA = VA \(Etapa 3\) \+ Outros Valores – Outras Deduções\]

__\[MFS40529\]__ Não gerar o registro 1400 quando o valor estiver negativo, só dar a mensagem de erro

No caso do resultado ser um valor negativo, deve ser gravada mensagem de erro no log \(msg de número 297 da planilha Sped\_Fiscal\_Log\_Erros\) e não gerar o registro\.

No caso do resultado ser = zero, a linha não deve ser gravada no arquivo do Sped\.

__OBS1__: Este registro não é gerado na opção “Geração – PIM” \(ver detalhes nas __OS2388\-AM\*__, que definiram a geração do Sped Fiscal para o PIM\)\.

RN1400\-02

Campo COD\_ITEM:

Gravar o indicador e o código do produto, quando for o caso, de acordo com as regras de cálculo do valor adicionado descritas na RN1400\.

\[Alteração – __OS 3417,__ __MFS6919, MFS20216, MFS\-22404 e MFS25117__\]

Se preenchido o campo “Produto \(Telecom, Transporte, Energia Elétrica e EPPP\)” em “SPED à EFD – Escrituração Fiscal Digital à __Menu__: Parâmetros à Dados iniciais”, então considerar como valor fixo o código do produto parametrizado, apenas para as operações de conhecimento de transporte, ou seja, classificação do documento = 4, para as operações de energia elétrica originadas da SAFX42/SAFX43 \(modelo 06\), para as operações de telecom originadas da SAFX42/SAFX43 \(modelos 21 e 22\), ou operações de Entrada de Produtos Primários Próprios – EPPP dos contribuintes estabelecidos no Paraná, ou seja, movimento E/S = 2 UF estabelecimento = PR\.

*\(o parâmetro “Produto \(Telecom, Transporte, Energia Elétrica e EPPP\)” é usado pelo segmento de Transportes, Energia Elétrica \(modelo 06\), Telecom \(modelos 21 e 22\) e para operações de Entrada de Produtos Primários Próprios – EPPP \(modelos 01, 1B, 04 ou 55\) dos estabelecidos no Paraná\)*

Quando não houver a informação do produto, ou seja, quando o valor for calculado apenas por município ou quando não houver parametrização em dados iniciais para transporte este campo não deverá ser preenchido e, deverá ser apresentada a mensagem de crítica no Log de Geração do SPED FISCAL conforme abaixo:

==1400============================

Erro: O Campo COD\_ITEM é de preenchimento obrigatório, e não foi informado

RN1400\-03

Campo MUN: 

Gravar o município do valor calculado, de acordo com as regras de cálculo do valor adicionado descritas na RN1400\.

 

Regra de gravação do campo município à Concatenação do Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código  do município \(para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\)\.

RN1400\-04

Campo VALOR:

Gravar o valor adicionado calculado, de acordo com as regras de cálculo do valor adicionado descritas na RN1400\.

Lembrar da validação a ser feita antes de gravar o resultado:

__\[MFS40529\]__ Não gerar o registro 1400 quando o valor estiver negativo, só dar a mensagem de erro

- No caso do resultado ser um valor negativo, deve ser gravada mensagem de erro no log \(msg de número 297 da planilha Sped\_Fiscal\_Log\_Erros\) e não gerar o registro\.
- No caso do resultado ser = zero, a linha não deve ser gravada no arquivo do Sped\.

### <a id="_Toc75782977"></a>Regras da geração do 1400 para o tipo de geração = “Específico por UF”,

### <a id="_Toc75782978"></a>e o Estabelecimento é de MG:

# Regras do 1400 – MG: Regras foram transferidas para o documento MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_MG\.docx

### <a id="_Toc75782979"></a>Regras da geração do 1400 para o tipo de geração = “Específico por UF”, 

### <a id="_Toc75782980"></a>e o Estabelecimento é de SP:

# Regras do 1400 – SP: Regras foram transferidas para o documento MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_SP

### <a id="_Toc75782981"></a>Regras da geração do 1400 para o tipo de geração = “Específico por UF”,

### <a id="_Toc75782982"></a>e o Estabelecimento é do ES:

# Regras do 1400 – ES: Regras foram transferidas para o documento MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_ES

### <a id="_Toc75782983"></a>Regras da geração do 1400 para o tipo de geração = “Específico por UF”,

### <a id="_Toc75782984"></a>e o Estabelecimento é de RN:

# Regras do 1400 – RN: Regras foram transferidas para o documento MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_RN

### <a id="_Toc75782985"></a>Regras da geração do 1400 para o tipo de geração = “Específico por UF”,

### <a id="_Toc75782986"></a>e o Estabelecimento é do RS:

# Regras do 1400 – RS: Regras foram transferidas para o documento MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_RS

### <a id="_Toc75782987"></a>Regras da geração do 1400 para o tipo de geração = “Específico por UF”, 

### <a id="_Toc75782988"></a>e o Estabelecimento é de BA:

# Regras do 1400 – BA: Regras foram transferidas para o documento MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_BA

### <a id="_Toc75782989"></a><a id="OLE_LINK73"></a><a id="OLE_LINK74"></a>Regras da geração do 1400 para o tipo de geração = “Específico por UF”, 

### <a id="_Toc75782990"></a>e o Estabelecimento é de TO:

# Regras do 1400 – TO: Regras foram transferidas para o documento MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_TO

### <a id="_Toc75782991"></a><a id="_Hlk18665975"></a>Regras da geração do 1400 para o tipo de geração = “Específico por UF”, 

### <a id="_Toc75782992"></a>e o Estabelecimento é de RJ:

# Regras do 1400 – RJ: Regras foram transferidas para o documento MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_RJ

### <a id="_Toc75782993"></a>Regras da geração do 1400 para o tipo de geração = “Específico por UF”, 

### <a id="_Toc75782994"></a>e o Estabelecimento é de PE:

# Regras do 1400 – PE: Regras foram transferidas para o documento MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_PE

### <a id="_Toc75782995"></a>Regras da geração do 1400 para o tipo de geração = “Específico por UF”, 

### <a id="_Toc75782996"></a>e o Estabelecimento é de SC:

# Regras do 1400 – SC: Regras foram transferidas para o documento MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_SC

### <a id="_Toc75782997"></a><a id="_Hlk75783039"></a>Regras da geração do 1400 para o tipo de geração = “Específico por UF”, 

### <a id="_Toc75782998"></a>e o Estabelecimento é de PR:

# 	

# <a id="_Toc75782999"></a>Regras do 1400 – UF: PR foram transferidas para o documento MTZ\_Sped\_Fiscal\_Regras\_Registro\_1400\_UF\_PR

# <a id="_Toc75783000"></a>Registro 1500 – NF/Conta EE \(Código 06\) – Operações Interestaduais

RN1500

Este registro foi criado *especificamente* para as operações de saídas interestaduais das empresas de energia elétrica \(modelo 06\) sujeitas ao Convênio ICMS 115\.

As regras de geração são as mesmas semelhantes as do registro C500 \(já que os registros são iguais\), sendo que para os registros 1500 e 1510 deve\-se considerar apenas:

- somente no caso das Empresas enquadradas no Convênio 115;
- somente as operações interestaduais da SAFX42/SAFX43 \(CFOP’s “6” e “7”\);
- somente modelo 06 \(somente Energia Elétrica\)

                \(Alteração OS2768\-P\):

- O filtro da data dos documentos dependerá do parâmetro "*84\-Escritura NF’s EE pela Data de Vencimento*" \(Módulo ICMS, item Manutenção à Parâmetros por UF\), da seguinte forma:

                 __Se __parâmetro "84\-Escritura NF’s EE pela Data de Vencimento" = "N"

                       A data fiscal do documento \(campo 03\) deve se enquadrar no período de geração;

                 __Se__ parâmetro "84\-Escritura NF’s EE pela Data de Vencimento" = "S"

                       A data de vencimento \(campo 32\) deve se enquadrar no período de geração;

*                      \(neste caso ao invés de usar a data fiscal, será utilizada a data do vencimento\)*

Para verificar se a Empresa é obrigada ou não a geração do Convênio 115, verificar o novo indicador criado na tela de cadastro do Estabelecimento \(módulo Parâmetros\)\. 

__OBS1__: Na geração por Inscrição Estadual Única, deve\-se considerar os documentos fiscais de todos os Estabelecimentos envolvidos na centralização \(OS2388\-O1ge\);

__OBS2__: Este registro não é gerado na opção “Geração – PIM” \(ver detalhes nas __OS2388\-AM\*__, que definiram a geração do Sped Fiscal para o PIM\)\. 

RN1500\-04

Campo COD\_PART

\[OS4747\] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

RN1500\-06

Campo COD\_SIT:

Se for nota cancelada \(campo 21\-Situação da nota  =  S\)

      gravar COD\_SIT = “02”

Senão, 

      Se for nota complementar \(novo campo “NF Complementar” = S\)

            gravar COD\_SIT = “06”

      Senão

            Se for nota baseada em regime especial \(novo campo “NF Regime Especial” = S\)

                  gravar COD\_SIT = “08”

            Senão gravar COD\_SIT = “00”

__Importante:__ 

Os testes devem ser executados exatamente nesta prioridade\. Assim, o teste deve ser encerrado na primeira regra atendida pela nota, e sempre que isto *não ocorrer*, será gravado o conteúdo “00”\.

RN1500\-09

Campo COD\_CONS

\[Alteração \- OS3557\]

\[Alteração – OS3744\]

Para as notas fiscais de energia elétrica \(modelo 06\), preencher o campo conforme DE\-PARA abaixo:

Se classe de consumo = '00', '01', '02', '03', '04',’06’ grava registro com informação '06'\.

Se classe de consumo = '20', '21', grava registro com informação '04'\.

Se classe de consumo= '40', '41', grava registro com informação '01'\.

Se classe de consumo= '60', '61',’07’ grava registro com informação '07'\.

Se classe de consumo= '70',’05’ grava registro com informação '05'\.

Se classe de consumo= '71', grava registro com informação '03'\.

Se classe de consumo= '72',’08’, grava registro com informação '08'\.

Se classe de consumo= '80', grava registro com informação '02'\.

Se classe de consumo= '90', grava registro com informação '90' \(não tem código novo de mesma definição\)\.

Se classe de consumo= '99', grava registro com informação '99' \(não tem código novo de mesma definição\)\.

__Alteração – MFS5904__ \(o De\-Para p/o segmento de EE *não* será mais utilizado\)

Para as notas fiscais de energia elétrica \(__modelo 06__\), o campo será preenchido normalmente, a partir do conteúdo do campo classe de consumo do documento\.

RN1500\-16

Campo VL\_SERV\_NT: valor dos serviços não tributados pelo ICMS

Este valor será composto da seguinte forma:

Valor das bases isenta/não tributada \+ base outras \+ base de redução dos *itens de mercadoria* da __SAFX43 __\+ valor do serviço dos *itens de serviço* da __SAFX43__:

\[campos 24\-Base Isenta/Não Tributada \+ campo 25\-Base Outras \+ campo 26\-Base de Redução dos itens de mercadoria \(campo 47 = “1”\) \]  \+ \[campo 19\-Valor do Serviço dos itens de serviço \(campo 47 = “2”\) \]

RN1500\-21

Campo VL\_BC\_ICMS\_ST:

Valor da base de cálculo do ICMS\-ST\. Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens \(SAFX43\)\.

RN1500\-22

Campo VL\_ICMS\_ST: 

Valor do ICMS\-ST\. Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens \(SAFX43\)

RN1500\-23

Campo COD\_INF

Recuperar a informação do campo 66 – Código da Observação da SAFX42\.

\[__ALTERAÇÃO \- MFS60545__\] Tratamento para o parâmetro – “Campo Código de Observação \(Considerar 6 caracteres\)” \- para truncar o campo com 6 posições, conforme Manual Guia Prático\.

__SE__ o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

__OU__

__SE__ o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

Este código deverá ser referenciado no registro 0450\.

RN1500\-24

Campo VL\_PIS:

__\[ALTERADO MFS17478\]__

Quando o parâmetro “Inibir a geração das informações constantes na EFD Contribuições \(Parâmetros > Dados Iniciais\)”  estiver marcado, este campo deve ser gerado em branco \(||\)\.

RN1500\-25

Campo VL\_COFINS:

__\[ALTERADO MFS17478\]__

Quando o parâmetro “Inibir a geração das informações constantes na EFD Contribuições \(Parâmetros > Dados Iniciais\)”  estiver marcado, este campo deve ser gerado em branco \(||\)\.

# <a id="_Toc75783001"></a>Registro 1510 – Itens da NF/Conta EE \(Código 06\) – Operações Interestaduais

RN1510

Este registro foi criado *especificamente* para as operações de saídas interestaduais das empresas de energia elétrica \(modelo 06\) sujeitas ao Convênio ICMS 115\.

Neste registro serão gravados os itens das notas fiscais gravadas no registro 1500\.

RN1510\-03

Campo 03\-COD\_ITEM:

Preencher com o código do produto ou o código do serviço, dependendo da classificação do item \(campo 47\-Classificação do Documento Fiscal da SAFX43\):

Se item de mercadoria à campos 11\-Indicador do Produto e 12\-Código do Produto 

Se item de serviço à campo 48\-Código do Serviço

Alteração feita na OS2667, EM Dez/2008, Release 32:

Se item de serviço à gravar o Código do Serviço \(campo 48\) ou a natureza do serviço \(campo 8 da SAFX2018\), conforme parâmetro que indica a informação a ser gravada \(“Dados Iniciais”\) 

O campo deve ser preenchido de acordo com a regra descrita para o registro C170 \(vide regra RNC170\-03\)\.

RN1510\-06

Campo 06\-UNID:

Preencher de acordo com o tipo de item da SAFX43, informação definida pelo campo 

“47\-Classificação do Documento Fiscal” \(1\-Mercadoria/2\-Serviço\):

Se item de mercadoria

      preencher com o código da unidade informada no campo 43\-Unidade de Medida

Senão \(item de serviço\)

        se o campo 43\-Unidade de Medida = nulo

              preencher com “UN” __\(\*\)__

        senão

              preencher com o código da unidade informada no campo 43\-Unidade de Medida

__\(\*\)__ seguindo a mesma lógica aplicada para os itens de serviço gravados no registro C170;

RN1510\-17

Conforme conteúdo do campo “57\-Especificação da Receita” , verificar:

Se conteúdo =  0, 1, 2, 3 ou 4 è preencher o campo com “0”

Senão è preencher o campo com “1”

Lista de valores:

0 \- Receita Própria \- serviços prestados;

1 \- Receita Própria \- cobrança de débitos;

2 \- Receita Própria \- venda de mercadorias;

3 \- Receita Própria \- venda de serviço pré\-pago;

4 \- Outras Receitas Próprias; 

5 \- Receitas de Terceiros \(co\-faturamento\);

9 \- Outras Receitas de Terceiros  

RN1510\-18

Campo COD\_PART

\[OS4747\] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

RN1510\-19

Campo VL\_PIS:

__\[ALTERADO MFS17478\]__

Quando o parâmetro “Inibir a geração das informações constantes na EFD Contribuições \(Parâmetros > Dados Iniciais\)”  estiver marcado, este campo deve ser gerado em branco \(||\)\.

RN1510\-20

Campo VL\_COFINS:

__\[ALTERADO MFS17478\]__

Quando o parâmetro “Inibir a geração das informações constantes na EFD Contribuições \(Parâmetros > Dados Iniciais\)”  estiver marcado, este campo deve ser gerado em branco \(||\)\.

# <a id="_Toc75783002"></a>Registro 1600 – Total das Operações com Cartão de Crédito e/ou Débito

__\[MFS74676\] Registro excluído pelo leiaute EFD115 \(vrs 1\.15 jan/2022\), sendo substituído pelo registro 1601\.__

<a id="_Hlk86158212"></a>RN1600

O registro 1600 tem por finalidade informar o valor total das operações realizadas pelo declarante cujo pagamento foi efetuado com cartão de débito ou crédito pelos clientes, estes valores devem ser segregados por administradora\.

__\[MFS74676\] __

- __Para Geração c/ leiaute anterior a EFD115 \(CAD\_LAYOUT – COD\_VERSAO<115\):__

Esse registro deve ser gerado conforme regra descrita a seguir __\(\*\)__\.

- __Para Geração c/ leiaute a partir da EFD115 \(CAD\_LAYOUT – COD\_VERSAO>=115\):__

__Registro excluído a partir da versão de layout 1\.15 \(jan/2022\)__

Registro não deve ser gerado

__\(\*\) Regra de Geração:__

Este registro será gerado a partir da tabela SAFX126\.

Se código da versão do layout for = ou > a “002” \(campo 02 do registro 0000\); selecionar na tabela SAFX126;

__Agrupamento 1:__

A aplicação deverá sumarizar os valores das operações recebidas com crédito e/ou débito

por administradora \(Indicador da pessoa  \+   Código da pessoa da Administradora\)\.

O período para seleção dos registros na tabela SAFX126 será o período definido no registro 0000 \(período informado nos campos 04 e 05\)\.

__Observações:__

Os clientes devem informar nos campos 06 e 07 da SAFX126, os valores __recebidos__ pelo declarante com cartão de CRÉDITO e/ou DÉBITO\.

 

O valor a ser informado deve corresponder às vendas líquidas, ou seja, o valor total das vendas efetuadas com cartão de crédito e/ou débito, deduzido os valores das vendas estornadas e canceladas\.

__OBS1__: Este registro não é gerado na opção “Geração – PIM” \(ver detalhes nas __OS2388\-AM\*__,  que definiram a geração do Sped Fiscal para o PIM\)\.

__\[MFS37872\] __Retirada da mensagem de erro dos campos 3 e 4, se pelo menos um deles estiver preenchido, de acordo com a informação do validador\. 

__Obs 2__: Se os campos TOT\_CREDITO e TOT\_DEBITO não estiverem preenchidos, dar a mensagem de erro para os 2 campos, conforme a planilha Sped\_Fiscal\_Log\_Erros\.xls\.  Se somente um deles estiver preenchido, não dar a mensagem de erro para o outro campo sem preenchimento\.

RN1600\-02

__Campo 02: COD\_PART__

Gravar o código da pessoa fís/jur da administradora \(campos 4 e 5 da SAFX126\) referente ao agrupamento por administradora do cartão de débito e/ou crédito\.

Na geração do arquivo observar as regras de gravação do campo que possui código e que devem possuir referências em outro registro\.

Registro e Nº do Campo

VALIDAÇÃO

Registro: 1600/Campo: 02

O valor informado no campo deverá existir no Registro 0150 

\[OS4747\] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

RN1600\-03

__Campo 03: TOT\_CREDITO__

Neste campo deve ser gravado  a sumarização do valor informado no campo 6 da tabela SAFX126 agrupado para cada administradora \(campo: 2\)\.

RN1600\-04

__Campo 04: TOT\_DEBITO__

Neste campo deve ser gravado  a sumarização do valor informado no campo 7 da tabela SAFX126 agrupado para cada administradora \(campo: 2\)\.

# Registro 1601 – Total das Operações com Cartão de Crédito e/ou Débito

__\[MFS74676\] Registro incluído pelo leiaute EFD115 \(vrs 1\.15 jan/2022\), em substituição ao registro 1601\.__

<a id="_Hlk86158229"></a>RN1601

O registro 1601 tem por finalidade identificar o valor total das operações realizadas pelo declarante por meio de instrumentos de pagamentos eletrônicos, discriminado por instituição financeira e de pagamento,\.

Este registro será gerado a partir da tabela __SAFX317__ \- Operações com Instrumentos de Pagamentos Eletrônicos\. Localização da tela de manutenção: Módulo: BÁSICOS > DATAWAREHOUSE > Manutenção > Operações com Instrumentos de Pagamentos Eletrônicos\.

- __Para Geração c/ leiaute anterior a EFD115 \(CAD\_LAYOUT – COD\_VERSAO<115\):__

Esse registro não deve ser gerado

- __Para Geração c/ leiaute a partir da EFD115 \(CAD\_LAYOUT – COD\_VERSAO>=115\):__

__Registro incluído a partir da versão de layout 1\.15 \(jan/2022\)__

Registro deve ser gerado conforme regra a seguir:

Consultar a tabela SAFX317 \- Operações com Instrumentos de Pagamentos Eletrônicos, com os seguintes critérios:

\- Estabelecimento: selecionado na tela de geração

\- Data de Movimento: compreendida no período da geração

Cada registro recuperado deve ser gravado um registro 1601\.

__OBS1__: Este registro não é gerado na opção “Geração – PIM” 

OBS2: Este registro não tem tratamento por Inscrição Estadual Única, pois os dados devem ser carregados diretamente na SAFX317 no estabelecimento centralizador \(idem ao registro 1600\)\.

RN1601\-02

__Campo 02: COD\_PART\_IP__

Gravar o código da Pessoa Física/Jurídica da Instituição Financeira e de pagamento \(campos 4 e 5 da SAFX317\)\.

Na geração do arquivo observar as regras de gravação do campo que possui código e que devem possuir referências em outro registro\.

Registro e Nº do Campo

VALIDAÇÃO

Registro: 1601/Campo: 02

O valor informado no campo deverá existir no Registro 0150 

Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, deve ser gerado no Cadastro do Participante \- registro 0150\.

RN1601\-03

__Campo 03: COD\_PART\_IT__

Gravar o código da Pessoa Física/Jurídica Intermediador da Transação \(campos 6 e 7 da SAFX317\)\.

Na geração do arquivo observar as regras de gravação do campo que possui código e que devem possuir referências em outro registro\.

Registro e Nº do Campo

VALIDAÇÃO

Registro: 1601/Campo: 03

O valor informado no campo deverá existir no Registro 0150 

Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, deve ser gerado no Cadastro do Participante \- registro 0150\.

RN1601\-04

__Campo 04: TOT\_VS__

Neste campo deve ser gravado com o valor Total das Operações com ICMS  \(campo 8 da tabela SAFX317\)\. 

Como o campo é de preenchimento obrigatório, se o valor Total das Operações com ICMS  não estiver preenchido, gravar zero\.

RN1601\-05

__Campo 05: TOT\_ISS__

Neste campo deve ser gravado com o valor Total das Operações com ISS \(campo 9 da tabela SAFX317\)\.

Como o campo é de preenchimento obrigatório, se o valor Total das Operações com ISS não estiver preenchido, gravar zero\.

RN1601\-06

__Campo 06: TOT\_OUTROS__

Neste campo deve ser gravado com o valor Total de Outras Operações \(campo 10 da tabela SAFX317\)\.

Como o campo é de preenchimento obrigatório, se o valor Total de Outras Operações não estiver preenchido, gravar zero\.

# <a id="_Toc75783003"></a>Registro 1700 – Documentos Fiscais Utilizados

__RN1700__

Este registro tem a função de informar os documentos fiscais por controle de dispositivo de segurança\.

Podem ocorrer vários registros por arquivo, e é de nível hierárquico 2, ou seja, só depende do registro de abertura do bloco 1\.

Deverá gerar a partir do layout 1\.0\.2\.

Os dados serão recuperados da tabela já existente safx106, com os seguintes filtros:

\- Data de Movimentação \(dat\_movto\) dentro do período *– na tela de manutenção, este campo se chama ‘Data de Ocorrência’*

\- Situação = 1 \(COD\_SITUACAO\)

\(OS\_2931\-E\) inclusão do filtro: Inscrição Estadual \(INSC\_ESTADUAL\)

Somente utilizaram este filtro os usuários do PIM que geram os dados por Inscrição Estadual\.

Premissa para utilização do filtro INSC\_ESTADUAL\. O parâmetro Registro 1700/1710 – Documentos Fiscais Utilizados, Cancelados e Inutilizados deve estar marcado\.

A data de movimento necessariamente deverá estar dentro do período informado em tela de geração \(data >= campo 04 e <= campo 05 no registro 0000\)\.

__RN1700\-02__

__Campo 02: COD\_DISP__

Deverá ser preenchido com o código dispositivo autorizado, conforme lista abaixo:

00 \- Formulário de Segurança

01 \- FS\-DA \- Formulário de Segurança para Impressão de DANFE

02 \- Formulário de segurança \- NF\-e

03 \- Formulário Contínuo

04 \- Blocos

05 \- Jogos Soltos

Esta informação será recuperada do campo 09 da safx106 \(COD\_TP\_DISP\_SEG\)\. Como os códigos já existentes nesse campo não são exatamente iguais aos que devem gerar acima, ficará desta forma a correspondência:

 

__Código SPED Fiscal__

__Código MasterSAF__

00 \- Formulário de Segurança

03 \- Formulário de Segurança 

01 \- FS\-DA – Formulário de Segurança para Impressão de DANFE

09 \- Formulário de Segurança DANFE

02 \- Formulário de segurança \- NF\-e

10 \- Formulário de segurança \- NF\-e

03 \- Formulário Contínuo

02 \- Formulário Contínuo 

04 \- Blocos

06 \- Blocos

05 \- Jogos Soltos

07 \- Jogos Soltos

Para a geração deste registro, não será considerado o tipo de dispositivo 05 \(ECF\)\.

__RN1700\-04__

__Campo 04: SER__

Gravar o conteúdo da série apenas quando seu conteúdo for <> branco, caso contrário, deixar o campo sem preenchimento \(gravar ||\)

__RN1700\-05__

__Campo 05: SUB__

Gravar o conteúdo da série apenas quando seu conteúdo for <> branco, caso contrário, deixar o campo sem preenchimento \(gravar ||\)

# <a id="_Toc75783004"></a>Registro 1710 – Documentos Fiscais Cancelados/Inutilizados

__RN1710__

Este registro é filho do registro 1710, e tem característica 1:N\.

Será gerado sempre que houver quebra da numeração das notas fiscais geradas no registro 1700, por motivo de inutilização ou cancelamento\.

Deverá ser gerado sempre que houver registro, e sempre que tiver registro 1700\.

Deverá gerar a partir do layout 1\.0\.2\.

Os dados serão recuperados da tabela já existente safx106, com os seguintes filtros:

\- Data de Movimentação \(dat\_movto\) dentro do período *– na tela de manutenção, este campo se chama ‘Data de Ocorrência’*

\- Situação = 2 e/ou 3 \(COD\_SITUACAO\)

\- Dispositivo de Segurança do documento cancelado/inutilizado = Dispositivo de Segurança do documento gravado no 1700 \(COD\_TP\_DISP\_SEG\)\.

\- Série de documento cancelado/inutilizado = Série do documento gravado no 1700 \(SERIE\_DOCFIS\)\.

\- SubSérie de documento cancelado/inutilizado = SubSérie do documento gravado no 1700 \(SERIE\_DOCFIS\)\.

\- Modelo do documento cancelado/inutilizado = Modelo do documento gravado no 1700 \(COD\_MODELO\)\.

\- “Tipo de Documento” do documento cancelado/inutilizado = “Tipo de Documento” do documento gravado no 1700 \(COD\_DOCTO\)\.

\- Número AIDF do documento cancelado/inutilizado = Número AIDF do documento gravado no 1700  \(NRO\_AIDF\)\.

\[CH78835\] inclusão dos seguintes filtros:

\- Número do Dispositivo de Segurança __Inicial__ do documento cancelado/inutilizado __>= __Número do Dispositivo de Segurança __Inicial__ do documento gravado no 1700 \(NUM\_CTR\_DISP\_INI\)

\- Número do Dispositivo de Segurança __Final__ do documento cancelado/inutilizado __<=__ Número do Dispositivo de Segurança __Final__ do documento gravado no 1700 \(NUM\_CTR\_DISP\_FIM\)\.

Porém só serão gravados os números de documento inicial e final neste registro\.

\(OS\_2931\-E\) inclusão do filtro: Inscrição Estadual \(INSC\_ESTADUAL\)

Somente utilizaram este filtro os usuários do PIM que geram os dados por Inscrição Estadual\.

Premissa para utilização do filtro INSC\_ESTADUAL\. O parâmetro Registro 1700/1710 – Documentos Fiscais Utilizados, Cancelados e Inutilizados deve estar marcado\.

Este registro deverá ser gravado após o 1700\.

Se houver mais de um cancelamento/inutilização para a mesma AIDF, poderá ser ordenada pelo número do documento inicial\.

A data de movimento necessariamente deverá estar dentro do período informado em tela de geração \(data >= campo 04 e <= campo 05 no registro 0000\)\.

# <a id="_Toc75783005"></a>Registro 1800 – DCTA – Demonstrativo de Crédito do ICMS sobre Transporte Aéreo

__RN1800__

Neste registro deverão ser informados os dados referentes ao DCTA\.

O DCTA é de escrituração obrigatória pelas empresas que prestem serviços de transporte aéreo de passageiros e de cargas e deve ser emitido ao final de cada período mensal em que tiverem sido prestados serviços de transporte aéreo de passageiros e serviços tributados de transporte aéreo de cargas, em ambas as modalidades\.

Esta obrigação já faz parte do dia\-a\-dia das companhias aéreas, conforme Anexo I da Portaria nº 14 de 19\.03\.2004\.

Este registro do SPED tem a função de registrar fielmente as informações de faturamento das companhias aéreas, portanto praticamente cada campo deste registro será recuperado de uma forma independente, conforme segue as regras de negócio a seguir\.

Para entender o cenário dos transportes aéreos, precisamos levar em consideração o seguinte cenário:

É possível às companhias aéreas tomar crédito de duas formas:

1. Crédito Presumido sobre as entradas \(a TAM faz desta forma\)
2. Porcentagem de crédito aplicada sobre as saídas tributadas \(a GOL faz desta forma\)

Todos os documentos para atendimento a este registro deverão ser recuperados de acordo com a data de geração \(data >= campo 04 e <= campo 05 no registro 0000\)\.

__RN1800\-02__

Campo VL\_CARGA 

Deverá conter o valor do faturamento relativo às prestações tributadas de serviços de transporte de carga\.

Recuperar, dentro do período de geração:

\- As notas fiscais de saída \(movimento entrada/saída = 9\)

\- Que devem ser modelo 10 e/ou modelo 57

\- Classificação = 4 \(cod\_class\_doc\_fis = 4\)

\- Não canceladas

Deverá ser sumarizado 

\- Valor total \(Valor contábil\) da Receita de Cargas → campo 23/safx07 \(VLR\_TOT\_NOTA\)

__RN1800\-03__

Campo VL\_PASS 

Deverá conter o valor do faturamento relativo às prestações de serviços de transporte de passageiros e às prestações não tributadas de serviço de transporte de carga\.

Recuperar, dentro do período de geração:

\- As notas fiscais de saída \(movimento entrada/saída = 9\)

\- Que devem ser modelo 18 ou 15

\(OS 2931\-E\) Inclusão de modelo:

Que devem ser modelo 10 ou 18 ou 15

\- Classificação = 1, 3 ou 4 \(cod\_class\_doc\_fis\)

\- Não canceladas

Deverá ser sumarizado:

\(OS 2931\-E\) Alteração da regra:

Quando a classificação for 4: Valor total \(Valor contábil\) da Receita de Cargas → campo 23/safx07 \(VLR\_TOT\_NOTA\) e para a classificação 4 \+ modelo 10: Valor Total da Receita de Cargas à campo 56/safx08 \(BASE\_ICMS\) \+ campo 55/SAFX08 \(TRIB\_ICMS\) = 2 ou pegar o valor da capa caso não houver itens \(campo 52/safx07\)\.

__Quando__ a classificação for 4: Valor total \(Valor contábil\) da Receita de Cargas → campo 23/safx07 \(VLR\_TOT\_NOTA\)

__Quando__ a classificação for 1 e/ou 3: Valor de isentas/não tributadas \(56 e 55/safx08 \(tributo 2\), ou pegar o valor da capa caso não houver itens \(campo 52/safx07\)\)\.

__RN1800\-04__

Campo VL\_FAT __\(campos 02 \+ 03\)__

Deverá ser calculado o valor total do faturamento pelo sistema, somando os campos \[\(VL\_CARGA\) \+ \(VL\_PASS\)\]\.

__RN1800\-05__

Campo IND\_RAT __\(campos 02 / 04\)__

Deverá ser calculado o índice de rateio, dividindo os campos \[\(VL\_CARGA\) / \(VL\_FAT\)\]\.

Alteração OS2388\-E23: Originalmente este cálculo era feito considerando o campo com 4 inteiros e dois decimais,  considerando   o layout do registro 1800, mas a partir do Ato Cotepe ICMS N\.2, de 16/03/2011, o valor passou a ser calculado considerando o novo layout do campo, com 2 inteiros e 6 decimais \(tamanho total  do campo = 8, sendo 6 decimais\)\.

__RN1800\-06__

Campo VL\_ICMS\_ANT 

Corresponde ao valor do crédito cobrado anteriormente a vendas de passagens e carga\. Os créditos são basicamente na entrada de Combustível e Material de Consumo usado no transporte\.

Este crédito será recuperado através das notas de entrada, conforme parametrização de CFOP ou CFOP/Natureza de Operação feita pelo usuário em um dos menus:

SPED Fiscal → Parâmetros → Registro 1800 → Créditos de ICMS \(Campo 06\) → CFOP

*Ou*

SPED Fiscal → Parâmetros → Registro 1800 → Créditos de ICMS \(Campo 06\) → CFOP/Natureza de Operação

Filtro:

\- As notas fiscais de entrada \(movimento entrada/saída = 1\) 

\- Que devem ter CFOP ou CFOP/Natureza parametrizados em um dos menus acima

\- Classificação = 1 \(cod\_class\_doc\_fis = 1\)

\- Não canceladas

Este campo deverá ser composto pela soma do valor do ICMS da safx08 \(campo 43 \- VLR\_ICMS\)

Em caso de não ter item na safx08, buscar o valor do campo 35 da safx07 \(VLR\_ICMS\)\.

__RN1800\-07__

Campo VL\_BC\_ICMS 

Corresponde ao valor da base de cálculo cobrada anteriormente a vendas de passagens e carga, os créditos são basicamente na entrada de Combustível e Material de Consumo usado no transporte\.

Este valor será recuperado através parametrização de CFOP ou CFOP/Natureza de Operação feita pelo usuário em um dos menus:

SPED Fiscal → Parâmetros → Registro 1800 → Base de Cálculo de ICMS \(Campo 07\) → CFOP

Ou

SPED Fiscal → Parâmetros → Registro 1800 → Base de Cálculo de ICMS \(Campo 07\) → CFOP/Natureza de Operação

Este campo deverá ser filtrado de duas formas diferentes:

__Quando__ forem parametrizados CFOP’s de entrada, filtrar:

\- As notas fiscais de entrada \(movimento entrada/saída = 1\)

\- Que devem ter CFOP ou CFOP/Natureza parametrizados em um dos menus acima

\- Classificação = 1 \(cod\_class\_doc\_fis = 1\)

\- Não canceladas

Este campo 07 deverá ser composto pela soma das base tributada de ICMS da safx08\.

\[campo 55/safx08 = 1 \(TRIB\_ICMS\) e campo 56/safx08\(BASE\_ICMS\)\]

Se não houver item na safx08, buscar os dados na safx07 

\[campo 51/safx07 \(BASE\_TRIB\_ICMS\)\]

__Quando__ forem parametrizados CFOP’s de saída, filtrar:

\- As notas fiscais de saída \(movimento entrada/saída = 9\)

\- Que devem ter CFOP ou CFOP/Natureza parametrizados em um dos menus acima

\- Classificação = 4 \(cod\_class\_doc\_fis = 4\)

\- Não canceladas

Este campo 07 deverá ser composto pela soma das base tributada de ICMS da safx07 \[campo 51/safx07 \(BASE\_TRIB\_ICMS\)\]

As duas situações não podem acontecer simultaneamente\.

__RN1800\-08__

Campo VL\_ICMS\_APUR __\(campos 05 \* 06\)__

Será o valor do ICMS apurado \(montante do crédito\), e deverá ser calculado pelo sistema, multiplicando os campos \[\(IND\_RAT\) \* \(VL\_ICMS\_ANT\)\]\.

__RN1800\-09__

Campo VL\_BC\_ICMS\_APUR __\(campos 05 \* 07\)__

Será o valor da base de cálculo do ICMS apurada, e este valor será obtido pela seguinte multiplicação: \[\(IND\_RAT\) \* \(VL\_BC\_ICMS\)\]\. 

__RN1800\-10__

Campo VL\_DIF __\(campos 06 \- 08\)__

É o valor da diferença a ser levada a estorno de crédito na apuração, que deve ser calculado pelo sistema: \[\(VL\_ICMS\_ANT\) \- \(VL\_ICMS\_APUR\)\]\.

# <a id="_Toc75783006"></a>Registro 1900 – Indicador de Sub Apuração do ICMS

__	__

RN1900

Deverá ser gerado um registro 1900 para cada Sub Apuração existente na base de dados do período em questão\.

O Sped Fiscal permite a existência de até três seis sub apurações, assim, para cada arquivo da EFD poderá existir um, dois ou três até seis registros 1900\. 

__Alteração da OS4261__: O Ato Cotepe 43/2013 aumentou a quantidade de sub\-apurações de três para seis\.

__Alteração da OS4593\-B__: Alterou a geração da opção “Geração – PIM” p/gerar as subapurações\.

__Alteração do CH15998\_2015:__ Altera o item “IMPORTANTE” sobre as UFs atendidas\.

__Alteração da MFS\-22946:__ Altera a geração do 1900 e filhos para considerar a Subapuração do Ressarcimento RS\.

A Sub Apuração é calculada numa etapa anterior à geração do SPED FISCAL\.  O MastersafDW disponibiliza a Sub Apuração nos seguintes módulos:

- Estadual >> ICMS \(onde originamente foi criada\)
- Específico >> PIM \(a Sub Apuração do módulo ICMS foi replicada para o PIM\)
- Estadual >> Ressarcimento ICMS\-ST RS \(Sub Apuração criada para atende a IN\-048/18, e diz respeito a ICMS\-ST, sendo completamente diferente das Sub Apurações dos módulos ICMS, PIM\)

Para gerar o registro 1900 é necessário identificar as Sub Apurações existentes, verificando as Tabelas das Sub Apurações existentes nos módulos acima relacionados\.  

Poderão existir de uma a seis Sub Apurações, identificadas no registro 1900 como 1, 2, 3, 4, 5 e 6\. 

Só deverão ser gerados os registros 1900 e “filhos” para as Sub Apurações que existam nas Tabelas das Sub Apurações\.

__IMPORTANTE__: 

- Segundo informações obtidas no site do Sped Fiscal \(GUIA PRÁTICO da Receita Federal\) estes registros atenderão ás UF’s do PA, ES, e também ao AM a partir de NOV/2014 \(Resolução 16/2014, Sefaz\-AM\), para tratar operações referentes a incentivos \(como o FUNDAP no ES por ex\.\) Pelas regras do Guia Prático, os valores das Sub Apurações devem ser “retirados” do Bloco E, e gerados separadamente nestes registros\. Por isso, os valores do registro __E110__ e do __1920__ são gerados numa etapa preliminar a geração do Sped Fiscal \(Módulo ICMS, item Apuração à Sub Apurações do Sped Fiscal, ou Módulo PIM, item Apuração à Sub Apurações do Sped Fiscal\), para que os usuários possam emitir relatórios e conferir os valores gerados\. Ver maiores detalhes no help do módulo ICMS / PIM\. Apesar de cada estado estabelecer uma data de obrigatoriedade dos registros 1900 e “filhos”, não há impedimento na geração por UF dentro do sistema Mastersaf DW, então a partir do momento que o usuário tiver registros e a parametrização no módulo deverão ser gerado os dados nos registros pertinentes\.
- As Sub Apurações deverão ser *geradas normalmente* tanto na geração “normal” como na geração por “*Inscrição Estadual Única*”, e também na geração “PIM” \(no caso do PIM, somente a partir de Nov/2014 quando a “Geração\-PIM” foi alterada para gerar as subapurações, atendendo à Resolução 16/2014, Sefaz\-AM\);
- __Alteração da MFS\-22946:__  Com a IN\-RE 048/18 do estado do Rio Grande do Sul, os registros 1900 e “filhos” passam a demonstrar as Sub Apurações referentes ao ressarcimento/complemento do ICMS\-ST, que no MastersafDW são calculadas no módulo Estadual >> Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\)\.  A IN\-RE 048/18 também determina que seja realizado um lançamento na Apuração do ICMS\-ST \(P9\-ST\) com o resultado da Sub Apuração do ICMS\-ST\. Tal lançamento será demonstrado no registro __E220__ do Sped Fiscal\. Tanto a geração da Sub Apuração quanto o lançamento de transferência são realizados no módulo Estadual >> Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\)\.  
- Não é correto ulitzar o mesmo número de identificação \(1, 2, 3, 4, 5, 6\) para Sub Apurações distintas\.
- As Sub Apurações *não serão geradas* na geração do Sped da opção de menu “*Geração – PIM*”, uma vez que este tipo de geração já trata os incentivos próprios do AM\. \(vide OBS anterior\)

RN1900\-02

Campo 02 – IND\_APUR\_ICMS:

Preencher com o conteúdo “3”, “4”, “5”, “6”, “7” ou “8”, dependendo da Sub Apuração em questão:

 

__Alteração da OS4261__: O Ato Cotepe 43/2013 aumentou a quantidade de sub\-apurações de três para seis\.

Gravar “3” quando se tratar da Sub Apuração 1

Gravar “4” quando se tratar da Sub Apuração 2

Gravar “5” quando se tratar da Sub Apuração 3

Gravar “6” quando se tratar da Sub Apuração 4

Gravar “7” quando se tratar da Sub Apuração 5

Gravar “8” quando se tratar da Sub Apuração 6

__RN1900\-03__

Campo 03 – DESCR\_COMPL\_OUT\_APUR:

Para as Sub Apurações do Sped Fiscal do Módulo ICMS:

Preencher com a descrição da Sub Apuração parametrizada na tela dos dados iniciais do Sped Fiscal \(item Parâmetros à Dados Iniciais\)\.

Alteração da __OS4593\-B__: 

Para as Sub Apurações do Sped Fiscal do Módulo PIM:

No caso da geração da opção “PIM”, as descrições serão recuperadas da parametrização do Módulo PIM, item Apuração à Sub Apurações do Sped Fiscal  à Sub Apurações por Inscrição Estadual\.

__Alteração da MFS\-22946:__

Para as Sub Apurações do RS, do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\):

Preencher com a descrição da Sub Apuração parametrizada na tela dos dados iniciais do Sped Fiscal \(item Parâmetros à Dados Iniciais\)\.

Quando a descrição da Sub Apuração não tiver sido informada, o registro será gravado sem a informação, e será gravada mensagem de erro no log de processo \(msg 360 da planilha das Mensagens de Erro\)\.

__Alteração da OS4261__: O Ato Cotepe 43/2013 aumentou a quantidade de sub\-apurações de três para seis\.

# <a id="_Toc75783007"></a>Registro 1910 – Período da Sub Apuração do ICMS

__RN1910__

Este registro é referente ao período da apuração do ICMS\. Como a Sub Apuração segue o período da apuração do ICMS, neste registro será gravada a mesma informação do registro “E100 – Período da Apuração do ICMS”\. 

# <a id="_Toc75783008"></a>Registro 1920 – Sub Apuração do ICMS

RN1920

Este registro é “filho” do 1900\. Para cada 1900, ou seja, para cada Sub Apuração, será gravado um registro 1920 com os valores resultantes da Sub Apuração\.

Origem dos dados:

- Tabela das Sub Apurações do módulo ICMS 

\(ICT\_SUB\_APURACAO\)

- Tabela das Sub Apurações do Módulo PIM \(quando for o caso da “Geração – PIM”\)	

\(ICT\_SUB\_APURACAO\_IES\)

- Tabela da Sub Apuração do RS do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\) \(ICT\_SUB\_APURACAO\_RS\)  

Os dados desta tabela são gerados nos seguintes itens:

- Módulo ICMS, menu “Apuração à Sub Apurações do Sped Fiscal à Apuração dos Resultados” 
- Módulo PIM, menu “Apuração à Sub Apurações do Sped Fiscal à Apuração dos Resultados”\.
- Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\), menu Geração à IN\-RE 048/18 à Geração dos Movimentos  e  menu Geração à IN\-RE 048/18 à Transferências entre Apurações __Alteração da MFS\-22946__

Critérios para seleção do registro a ser utilizado:

Estabelecimento   =  considerar o estabelecimento da geração 

Data da Apuração =  considerar a data final do período da geração

Sub Apuração       =  Sub Apuração 1, Sub Apuração 2, Sub Apuração 3, Sub Apuração 4, Sub Apuração 5 ou 

                                  Sub Apuração 6,  dependendo da Sub Apuração a ser gerada 

Tipo do Livro        = ‘108’ ou ‘165’\. Se a geração é por Inscrição Estadual Única, usar o livro ‘08’, senão considera o ‘165’\. 

*\(considerar também a inscrição estadual, no caso da geração da opção “PIM”\)*

Os dados do registro 1920 serão gerados a partir dos valores encontrados no registro selecionado, conforme as regras definidas para cada campo\.

Tratamento de erro:

Caso não existam dados referentes ao estabelecimento e período  \(ou estabelecimento, inscrição estaudl e período, quando se tratar da geração “PIM”\)  para nenhuma das Sub Apurações \(1, 2, 3, 4, 5 ou 6\), será gravada uma mensagem de erro no log com a descrição abaixo \(e neste caso, o registro 1920, assim como os seus registros “filhos” não deverão ser gerados\):

                    *“Não existem dados referentes às Sub Apurações do Sped Fiscal\. Favor *

*                         consultar help do menu “Dados Iniciais” do módulo Sped Fiscal”*

RN1920\-02

Campo 02\-VL\_TOT\_TRANSF\_DEBITOS\_OA:

Gravar com o conteúdo do campo “Débitos de Notas Fiscais” da Tabela das Sub Apurações\.

RN1920\-03

Campo 03\-VL\_TOT\_AJ\_DEBITOS\_OA:

Gravar com o conteúdo do campo “Outros Débitos” da Tabela das Sub Apurações\.

RN1920\-04

Campo 04\-VL\_ESTORNOS\_CRED\_OA:

Gravar com o conteúdo do campo “Estorno de Crédito” da Tabela das Sub Apurações\.

RN1920\-05

Campo 05\- VL\_TOT\_TRANSF\_CREDITOS\_OA:

Gravar com o conteúdo do campo “Créditos de Notas Fiscais” da Tabela das Sub Apurações\.

RN1920\-06

Campo 06\-VL\_TOT\_AJ\_CREDITOS\_OA:

Gravar com o conteúdo do campo “Outros Créditos” da Tabela das Sub Apurações\.

RN1920\-07

Campo 07\-VL\_ESTORNOS\_DEB\_OA:

Gravar com o conteúdo do campo “Estorno de Débito” da Tabela das Sub Apurações\.

RN1920\-08

Campo 08\-VL\_SLD\_CREDOR\_ANT\_OA:

Gravar com o conteúdo do campo “Saldo Credor Anterior” da Tabela das Sub Apurações\.

RN1920\-09

Campo 09\-VL\_SLD\_APURADO\_OA:

Preencher com base no seguinte resultado:

\(VL\_TOT\_TRANSF\_DEBITOS\_OA \+ VL\_TOT\_AJ\_DEBITOS\_OA \+ VL\_ESTORNOS\_CRED\_OA\)

__menos__

\(VL\_TOT\_TRANSF\_CREDITOS\_OA \+ VL\_AJ\_CREDITOS\_OA \+ VL\_ESTORNOS\_DEB\_OA \+ VL\_SLD\_CREDOR\_ANT\_OA\)

Se resultado obtido = zero ou > zero  à gravar o valor do resultado 

Se resultado obtido < zero à gravar zero

__Alteração da MFS\-22946:__

Para as Sub Apurações do RS do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\), o valor do campo 09 – VL\_SLD\_APURADO\_OA, já vem calculado, portando considera o conteúdo do campo “Saldo Apurado” da Tabela de Sub Apuração RS\.

RN1920\-10

Campo 10\-VL\_TOT\_DED:

Gravar com o conteúdo do campo “Deduções” da Tabela das Sub Apurações\.

RN1920\-11

Campo 11\-VL\_ICMS\_RECOLHER\_OA:

Preencher de acordo com o valor do campo 09\-VL\_SLD\_APURADO\_OA, da seguinte forma:

Se campo 09\-VL\_SLD\_APURADO\_OA > zero

      Gravar o resultado do saldo apurado menos as deduções, mas apenas quando este resultado for > zero, ou seja:

       Se \(09\-VL\_SLD\_APURADO\_OA \- 10\-VL\_TOT\_DED\)  > zero

             Gravar o resultado obtido;

      Senão 

             Gravar zero;

Senão 

     Gravar zero;

__Alteração da MFS\-22946:__

Para as Sub Apurações do RS do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\), o valor do campo 11 – VL\_ICMS\_RECOLHER\_OA, já vem calculado, portando considera o conteúdo do campo “ICMS a Recolher” da Tabela de Sub Apuração RS\.

RN1920\-12

Campo 12\-VL\_SLD\_CREDOR\_TRANSP\_OA:

Preencher com base no seguinte resultado:

\(VL\_TOT\_TRANSF\_CREDITOS\_OA \+ VL\_AJ\_CREDITOS\_OA \+ VL\_ESTORNOS\_DEB\_OA \+ VL\_SLD\_CREDOR\_ANT\_OA\)

__menos__

\(VL\_TOT\_TRANSF\_DEBITOS\_OA \+ VL\_TOT\_AJ\_DEBITOS\_OA \+ VL\_ESTORNOS\_CRED\_OA\) 

Se resultado obtido = zero ou > zero  à gravar o valor do resultado 

Se resultado obtido < zero à gravar zero

__Alteração da MFS\-22946:__

Para as Sub Apurações do RS do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\), o valor do campo 12 – VL\_SLD\_CREDOR\_TRANSP\_OA, já vem calculado, portando considera o conteúdo do campo “Saldo Credor a Transportar” da Tabela de Sub Apuração RS\.

RN1920\-13

Campo 13\-DEB\_ESP\_OA:

Gravar com o conteúdo do campo “Débitos Especiais” da Tabela das Sub Apurações\.

Crítica sobre os valores a recolher: 

Sempre que o total das guias de recolhimento do registro 1926 não coincidir com o resultado da soma dos campos \(11\-VL\_ICMS\_RECOLHER\_OA \+ 13\-DEB\_ESP\_OA\) do 1920, será gravada uma mensagem de aviso no log \(mensagem de número 363 da planilha Sped\_fiscal\_Log\_Erros\)\. 

# <a id="_Toc75783009"></a>Registro 1921 – Ajustes da Sub Apuração do ICMS

__RN1921__

A geração deste registro é feita a partir dos lançamentos complementares e dos débitos especiais cadastrados para o período de apuração \(abas “Lançamento de Valores” e “Débitos Especiais” da manutenção dos Lançamentos Complementares\)\.

Obs: As regras da geração são as mesmas do registro E111 do Bloco E, considerando que serão tratados apenas os dados referentes a Sub Apuração em questão\.

__Regras de Geração a partir dos Lançamentos Complementares__:  

Origem dos dados:

- Tabela dos Lançamentos Complementares da Apuração do ICMS do módulo ICMS 

\(ITEM\_APURAC\_DISCR\)

- Tabela dos Lançamentos Complementares da Apuração do ICMS do Módulo PIM 

\(ICT\_IT\_AP\_DSCR\_IES\)

- Tabela dos Lançamentos da Sub Apuração do RS do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\) \(ITEM\_APURAC\_SUBRS\)  

Os dados serão obtidos nas mesmas tabelas dos lançamentos complementares da apuração descritas para o registro E111\.

 

Cada lançamento complementar deve ser apresentado no registro no 1921 separadamente, ou seja, lançamento a lançamento\.

Considerar apenas os lançamentos que atendam aos seguintes critérios:

 \- Campo “Sub Apuração” = Sub Apuração 1, Sub Apuração 2, Sub Apuração 3, Sub Apuração 4, Sub Apuração 5 ou

                                              Sub Apuração 6,dependendo da Sub Apuração a ser gerada;

 \- Campo “Tipo do Lançamento” = “2” ou “3”;

Critica a ser realizada à Quando for encontrado algum lançamento em que o campo “Tipo do Lançamento” não esteja preenchido, o lançamento deverá ser gravado normalmente no 1921, e será gravada a seguinte mensagem no log de erros \(msg 361 do log de erros\): 

 “*O campo “Tipo de Lançamento” deve estar preenchido para a correta identificação do lançamento complementar do ICMS\.”*

\(esta msg já consta da planilha de erros “Sped\_Fiscal\_Log\_Erros” com o código 62\)   

Obs: Na leitura dos lançamentos, considerar os seguintes itens da apuração:

“002” – Outros Débitos

“003” – Estorno de Crédito

“006” – Outros Créditos

“007” – Estorno de Débito

“012” – Deduções

__Alteração da MFS\-22946:__

Para as Sub Apurações do RS do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\), a geração do registro 1921 é feita a partir dos lançamentos gravados pelas gerações dos movimentos e das transferências, menu Geração à IN\-RE 048/18  à Geração dos Movimentos  e  menu Geração à IN\-RE 048/18  à Transferências entre Apurações\. Tais lançamentos não podem ser alterados manualmente, mas podem ser conferidos através do relatório de Conferência da Sub Apuração, menu Relatórios à Conferência dos Móvimentos, disponível no módulo em questão\.

A Geração do Movimento pode gravar os seguintes lançamentos:

- Lançamento em Outros Débitos referente à saídas de mercadorias destinadas a Consumidor Final;
- Lançamento em Outros Créditos referente à entradas sujeitas a ST;
- Lançamento em Estorno de Créditos referente à saídas para outras Ufs, isentas ou não tributadas;
- Lançamento em Outros Créditos da Parcela do Crédito das Mercadorias em Estoque \[MFS81764\]
- Lançamento em Outros Créditos das Devoluções das Saídas de Mercadorias destinadas a Consumidor Final \[MFS81804\]

A Geração da Transferência pode gravar os seguintes lançamentos:

- Lançamento em Estorno de Créditos referente ao estorno do valor a restituir;
- Lançamento em Deduções referente a dedução do valor a complentar;

__Regras de Geração a partir dos Débitos Especiais__:  

Origem dos dados:

- Tabela dos Débitos Especiais da Apuração do ICMS do módulo ICMS 

\(ICT\_DEBITO\_ESP\)

- Tabela dos Débitos Especiais da Apuração do ICMS, do Módulo PIM 

\(ICT\_DEB\_ESP\_IES\)

Gravar um registro 1921 para cada débito especial cadastrado na aba “Débitos Especiais” \(manutenção dos Lançamentos Complementares\) para o período de apuração\.

Considerar apenas os débitos especiais que atendam aos seguintes critérios:

- Campo “Sub Apuração” = Sub Apuração 1, Sub Apuração 2, Sub Apuração 3, Sub Apuração 4, Sub Apuração 5,    

                                                              ou Sub Apuração 6, dependendo da Sub Apuração a ser gerada;

\(em caso de dúvidas sobre os Débitos Especiais ver observações descritas na RNE111\) 

__Alteração da MFS\-22946:__

As Sub Apurações do RS do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\) não gera o 1921 de Débitos Especiais\.

# <a id="_Toc75783010"></a>Registro 1922 – Informações Adicionais dos Ajustes \(DA e Processos\) 

__RN1922__

Neste registro são gravadas as informações sobre os Processos e Documentos de Arrecadação relacionados ao lançamento ou débito especial gravado no registro __1921__\. 

A manutenção desses dados é feita na manutenção dos lançamentos complementares, opção:

Lançamentos Complementares à aba “Lançamento de Valores”, opção  “Processos / Doc Arrecadação”; 

Débitos Especiais àaba “Débitos Especiais”, opção  “Processos / Doc Arrecadação”;   

__RN1922\-03__

Campo NUM\_PROC:

Campo preenchido com o número do processo associado ao lançamento complementar ou vinculado ao débito especial\. 

__\[MFS92607\] Versão de Layout 1\.16 \(jan/2023\)__

No layout 1\.16 o tamanho do campo passou de 15 para 60 posições\.

__Para Geração c/ leiaute anterior a EFD116 \(CAD\_LAYOUT – COD\_VERSAO<116\):__

- Caso o número do processo tenha mais de 15 caracteres, preencher esse campo com os 15 primeiros caracteres\.

__Para Geração c/ leiaute a partir da EFD116 \(CAD\_LAYOUT – COD\_VERSAO>=116\):__

- Preencher esse campo com o número do processo integral que foi inserido no sistema\.

# <a id="_Toc75783011"></a>Registro 1923 – Informações Adicionais dos Ajustes \(Doctos Fiscais\)

__RN1923__

Neste registro são gravadas as informações sobre os Documentos Fiscais relacionados ao lançamento ou débito especial gravado no registro __1921__\. Será gravado um registro para cada nota fiscal \(ou item de nota fiscal\) associado ao lançamento complementar ou débito especial do __1921__\.

Origem dos dados:

- Tabela dos Documentos vinculados aos Lançamentos Complementares da Apuração do ICMS do módulo ICMS 

\(ITEM\_APURAC\_DISCR\_AJUSTE\)

- Tabela dos Documentos vinculados aos Débitos Especiais da Apuração do ICMS do módulo ICMS 
- \(ICT\_DEBITO\_ESP\_AJ\) 
- Tabela dos Documentos vinculados aos Lançamentos Complementares da Apuração do ICMS do Módulo PIM 

\(ICT\_IT\_AP\_DSCR\_IES\_AJ\)

- Tabela dos Documentos vinculados aos Débitos Especiais da Apuração do ICMS do Módulo PIM 

\(ICT\_DEB\_ESP\_IES\_AJ\)

- Tabela dos Documentos vinculados aos Lançamentos da Sub Apuração do RS do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\) 

\(ITEM\_APURAC\_SUBRS\_AJUSTE\)  

A manutenção desses dados é feita na manutenção dos lançamentos complementares, opção:

Lançamentos Complementares àaba “Lançamento de Valores”, opção  “Documentos Fiscais Vinculados”; 

Débitos Especiais àaba “Débitos Especiais”, opção  “Documentos Fiscais Vinculados”;

 

Observar que a tabela dos documentos fiscais vinculados  tem apenas a identificação da nota fiscal relacionada e o valor do ajuste que será informado em tela pelo usuário \(já que nem sempre o valor de ajuste para a apuração será o próprio valor do ICMS destacado na nota\)\.

__Alteração da MFS\-22946 / MFS\-62000:__

Para as Sub Apurações do RS do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\), a geração do registro 1923 é feita a partir das notas e cupons fiscais que compuseram os lançamentos gravados pela geração do movimento, menu Geração à IN\-RE 048/18 à Geração dos Movimentos\.

Não há possibilidade incluir/alterar manualmente os documentos que compõe os lançamentos, mas estes podem ser conferidos através dos relatórios, menu Relatórios à IN\-RE 048/18 à Conferência dos Móvimentos, disponíveis no módulo em questão\.

Conforme explicado na regra RN1921, a Geração do Movimento grava os seguintes lançamentos:

- Lançamento em Outros Débitos referente à saídas de mercadorias destinadas a Consumidor Final;
- Lançamento em Outros Créditos referente à entradas sujeitas a ST;
- Lançamento em Estorno de Créditos referente à saídas para outras Ufs, isentas ou não tributadas;
- Lançamento em Outros Créditos da Parcela do Crédito das Mercadorias em Estoque \[MFS81764\]
- Lançamento em Outros Créditos das Devoluções das Saídas de Mercadorias destinadas a Consumidor Final \[MFS81804\]

Serão gravados registros 1923 para os documentos fiscais que compõe os seguintes lançamentos: 

- Lançamento em Outros Débitos referente à saídas de mercadorias destinadas a Consumidor Final;
- Lançamento em Outros Créditos referente à entradas sujeitas a ST;

__MFS\-62000__:

- Lançamento em Estorno de Créditos referente à saídas para outras Ufs, isentas ou não tributadas
- Lançamento em Outros Créditos das Devoluções das Saídas de Mercadorias destinadas a Consumidor Final \[MFS81804\]

A IN\-RE 048/18 determinava a gravação dos documentos ficais no registro 1923 apenas para os lançamentos de Outros Créditos e Outros Débitos\. Com a IN\-RE 006/19, o lançamento de Estorno de Créditos referente à saídas para outras Ufs, isentas ou não tributadas passa a gerar registro 1923\.

__Alteração da MFS36578 \(Regime Especial RS – Apuração Assistida\):__

Quando o parâmetro “Nota Fiscal de Consumidor Eletrônica \(NFC\-e\)” da parametrização dos Dados Iniciais do Sped Fiscal \(quadro “Apuração Assistida – RS”\) estiver marcado, os registros “filhos” 1923 __*não*__ serão gerados para todos os ajustes do 1921 cujo código de ajuste conste da seguinte parametrização:

   \- Módulo: Sped Fiscal

   \- Menu: Parâmetros > Apuração Assistida – RS

   \- Campo: Código de Ajuste utilizado na Sub\-Apuração p/as NFC\-e \(1921\) 

Trata\-se de orientação do Ato Declaratório dos contribuibntes do RS autorizados a escriturar as notas eletrônicas de forma consolidada\. Neste caso, o ajuste lançado na Sub\-Apuração que reflete o ICMS Efetivo das saídas, deve ser criado pelo usuário desmembrando o total que corresponde às notas do Modelo 65, e para este ajuste, os “filhos” 1923 não devem ser gerados, mesmo que o cliente gere a informação dos “filhos” \(para efeito de fiscalização por exemplo\.

__Obs__\.: As alterações da __MFS36578__ foram p/atender um regime especial do RS, do cliente ZAFFARI, e referente ao projeto “Apuração Assistida – RS”\. Importante ressaltar que o Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\) não fez parte do escopo, porque a ZAFFARI não tem este módulo\. Apesar disso, foi sinalizado um possível impacto nesse módulo\. 

RN1923\-02

Campo COD\_PART

__\[OS4747\]__ 

Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

__\[MFS25285\]__

__\[MFS95293\] __Alteração da regra para o modelo 65 e código de ajuste for igual a RS001920

__Se__ modelo do documento referenciado = 65 \(campo 13 da SAFX07\)

      __Se__ código de ajuste \(campo 02\- COD\_AJ\_APUR do registro 1921\) <> RS001920

            O campo será gravado sem informação \(“||”\)

     __Senão__

           O campo será gravado com o código da pessoa fis/jur associada ao estabelecimento da geração \(módulo DW, menu    

           Manutenção > Cadastro> Estabelecimento x Pessoa Física/Jurídica\)\.  Quando não existir a pessoa fis/jur associada ao 

           estabelecimento, o campo será gravado sem informação \(“||”\)

__Senão__

           O campo será gravado com a pessoa física/jurídica associado ao lançamento complementar ou débito especial\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

__MFS\-62000__

Para as Sub Apurações do RS do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\), preencher com a Pessoa Física/Jurídica resultante da Geração do Movimento \(campo IDENT\_FIS\_JUR da Tabela ITEM\_APURAC\_SUBRS\_AJUSTE\)\.

O registro lido da tabela ITEM\_APURAC\_SUBRS\_AJUSTE pode ser nota fiscal e cupom fiscal\. 

Para nota fiscal, o campo IDENT\_FIS\_JUR refere\-se ao identificador da Pessoa Fis/Jur da nota\. 

Para cupom fiscal, o campo IDENT\_FIS\_JUR refere\-se a identificador da Pessoa Fis/Jur parametrizada para o Estabelecimento referenciado no cupom, cadastrada no módulo Básicos >> Data Warehouse, menu Manutenção >> Cadastros >> Estabelecimentos x Pessoas Físicas/Jurídicas\.

As regras descritas acima, quanto ao parâmetro "Considerar o Indicador no Código do Participante"  e quanto ao tratamento para notas de modelo 65, valem para esta origem\.

RN1923\-03

Campo Modelo

Preencher com o Modelo do documento Fiscal \(campo 13 SAFX07\)

__MFS\-62000__

Para as Sub Apurações do RS do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\), preencher com o Modelo do Documento resultante da Geração do Movimento \(campo COD\_MODELO da Tabela ITEM\_APURAC\_SUBRS\_AJUSTE\)\.

O registro lido da tabela ITEM\_APURAC\_SUBRS\_AJUSTE pode ser nota fiscal e cupom fiscal\. 

Para nota fiscal, o campo COD\_MODELO refere\-se ao Modelo da nota \(SAFX07 campo 13\)\. 

Para cupom fiscal, o campo COD\_MODELO refere\-se ao Modelo do Cupom \(SAFX993 – campo 03\)\.

RN1923\-04

Campo SER

Preencher com a Série do documento Fiscal \(campo 09 SAFX07\)

__\[MFS27727\]__

Esse campo é de preenchimento obrigatório com três posições para NF\-e ou NFC\-e, então considerar na geração:

Se o documento fiscal for de emissão própria ou de terceiros \(origem campo 03\-Movimento Entrada/Saída da SAFX07 = 1, 2,3,4,5 ou 9\) e o campo 03\-COD\_MOD for igual a “55” \(origem campo 13\-Modelo de Documento da SAFX07 = 55\), considerar as três posições do campo 09\-Série do Docto Fiscal, mas caso seja menor do que o esperado preencher com zeros à esquerda e ainda se não estiver preenchida preencher com zeros \(000\)\.

Se o documento fiscal for de emissão própria \(origem campo 03\-Movimento Entrada/Saída da SAFX07 <> ‘1’\) e o campo 03\-COD\_MOD for igual a “65” \(origem campo 13\-Modelo de Documento da SAFX07 = 65\), considerar as três posições do campo 09\-Série do Docto Fiscal da SAFX07, mas caso seja menor do que o esperado preencher com zeros à esquerda e ainda se não estiver preenchida preencher com zeros \(000\)\.

__MFS\-62000__

Para as Sub Apurações do RS do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\), a Tabela ITEM\_APURAC\_SUBRS\_AJUSTE gravada pela Geração do Movimento, pode conter nota fiscal e cupom fiscal\. 

Se nota fiscal, o campo SER deve ser preenchido com o campo SERIE\_DOCFIS da ITEM\_APURAC\_SUBRS\_AJUSTE,  aplicando a regra acima que trata NF\-e NFC\-e\. Refere\-se a Série da  nota \(SAFX07 campo 09\)\. 

Se cupom fiscal, este campo não deve ser preenchido\.

RN1923\-05

Campo SUB

Preencher com a Subsérie do documento Fiscal \(campo 10 SAFX07\)

__MFS\-62000__

Para as Sub Apurações do RS do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\), a Tabela ITEM\_APURAC\_SUBRS\_AJUSTE gravada pela Geração do Movimento, pode conter nota fiscal e cupom fiscal\. 

Se nota fiscal, o campo SUB deve ser preenchido com o campo SUB\_SERIE\_DOCFIS da ITEM\_APURAC\_SUBRS\_AJUSTE, que é referente a Subsérie da nota \(SAFX07 campo 10\)\. 

Se cupom fiscal, este campo não é preenchido\.

RN1923\-06

Campo NUM\_DOC

Preencher com o Número do Documento Fiscal \(campo 08 SAFX07\)

__MFS\-62000__

Para as Sub Apurações do RS do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\), preencher com o Número do Documento resultante da Geração do Movimento \(campo NUM\_DOCFIS da Tabela ITEM\_APURAC\_SUBRS\_AJUSTE\)\.

O registro lido da tabela ITEM\_APURAC\_SUBRS\_AJUSTE pode ser nota fiscal e cupom fiscal\. 

Para nota fiscal, o campo NUM\_DOCFIS refere\-se ao Número do Documento Fiscal \(SAFX07 campo 08\)\.

Para cupom fiscal, o campo NUM\_DOCFIS refere\-se ao Número COO \(SAFX993 campo 05\)\.

RN1923\-07

Campo DT\_DOC

Preencher com a Data da Emissão Documento Fiscal \(campo 11 SAFX07\)

__MFS\-62000__

Para as Sub Apurações do RS do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\), a Tabela ITEM\_APURAC\_SUBRS\_AJUSTE gravada pela Geração do Movimento, pode conter nota fiscal e cupom fiscal\. 

Se nota fiscal, o campo DT\_DOC deve ser preenchido com a Data da Emissão Documento Fiscal \(campo 11 SAFX07\)\. 

Se cupom fiscal, o campo DT\_DOC deve ser preenchido com o campo DATA\_FISCAL da Tabela ITEM\_APURAC\_SUBRS\_AJUSTE, que é referente a Data da Emissão do Cupom Fiscal \(campo 06 SAFX993\)\.

RN1923\-08

Campo COD\_ITEM:

Para o preenchimento deste campo deve\-se verificar se no documento fiscal relacionado ao lançamento / débito especial foi informado ou não o número do item\. Nem sempre esta informação estará preenchida na tela dos “Documentos Fiscais Vinculados”\. 

Por isso, seguir a lógica:

Se o número do item do documento relacionado estiver preenchido:

      Gravar o código do produto do item informado

      \(concatenando indicador \+ código conforme regra de gravação do COD\_ITEM\)

Senão

      O campo não deve ser preenchido

__\[OS3543\-A\]__

Se parâmetro ‘Considerar o Indicador no Código do Item’, não concatenar o código, utilizando a mesma regra descrita no campo 02 do registro 0200

Obs: somente itens de mercadoria são tratados para ajuste\.

__MFS\-62000__

Para as Sub Apurações do RS do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\), preencher com o Produto resultante da Geração do Movimento \(campos IND\_PRODUTO e COD\_PRODUTO da Tabela ITEM\_APURAC\_SUBRS\_AJUSTE\)\.

O registro lido da tabela ITEM\_APURAC\_SUBRS\_AJUSTE pode ser nota fiscal e cupom fiscal\. 

Para nota fiscal, esse campo é preenchido com o Produto do Item de Mercadoria da Nota Fiscal \(campos 13 e 14 SAFX08\)

Para cupom fiscal, este campo é preenchido com o Produto do Item do Cupom \(SAFX994 – campos 08 e 09\)\.

A regra descrita acima, quanto ao parâmetro  "Considerar o Indicador no Código do Item"  vale para esta origem\.

RN1923\-09

Campo VL\_AJ\_ITEM

__MFS\-62000__

Para as Sub Apurações do RS do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\), preencher com o Valor do Ajuste resultante da Geração do Movimento \(campo VLR\_AJUSTE da Tabela ITEM\_APURAC\_SUBRS\_AJUSTE\)\.

O registro lido da tabela ITEM\_APURAC\_SUBRS\_AJUSTE pode ser nota fiscal e cupom fiscal\.  

Tanto para nota fiscal como para cupom fiscal, esse campo é preenchido com o valor do ajuste calculado\. Este valor pode ser consultado através dos Relatórios de Conferência disponíveis no Módulo Ressarcimento ICMS\-ST RS\.

RN1923\-10

Campo CHV\_DOCe:                \(campo criado pela __MFS7082__\) 

Este campo faz parte do registro 1923 apenas a partir da versão 1\.10 \(Jan/2017\)\.

Regra de preenchimento a partir de Jan/2017:

__Se__ modelo do documento referenciado = 55 ou 57 \(campo 13 da SAFX07\)

     __Se__ campo “226\-*Chave de Acesso da NF\-e”* da SAFX07 <> nulo

           O campo será preenchido com a informação do campo 226, utilizando as primeiras 44 posições

           \(conforme o formato da NF\-e nacional\);

__     Senão__

           Neste caso o campo será gravado sem informação \(“||”\), e no log será gravada a seguinte mensagem de erro,

            pois o campo é obrigatório para os documentos eletrônicos: *“O campo CHV\_DOCe é de preenchimento obrigatório,*

*           e não foi informado”*\. O log deve exibir a identificação do lançamento, e os dados suficientes para identificar a nota

           referenciada;

__Senão__

     O campo será gravado sem informação \(“||”\)\.

Alteração __MFS8937:__

Regra de preenchimento a partir de Abril/2017:

__Se__ modelo do documento referenciado = 55 ou 57  ou 67 \(campo 13 da SAFX07\)

     __Se__ campo “226\-*Chave de Acesso da NF\-e”* da SAFX07 <> nulo

           O campo será preenchido com a informação do campo 226, utilizando as primeiras 44 posições

           \(conforme o formato da NF\-e nacional\);

__     Senão__

           Neste caso o campo será gravado sem informação \(“||”\), e no log será gravada a seguinte mensagem de erro,

            pois o campo é obrigatório para os documentos eletrônicos: *“O campo CHV\_DOCe é de preenchimento obrigatório,*

*           e não foi informado”*\. O log deve exibir a identificação do lançamento, e os dados suficientes para identificar a nota

           referenciada;

__Senão__

     O campo será gravado sem informação \(“||”\)\.

__MFS\-62000__

Para as Sub Apurações do RS do Módulo Ressarcimento ICMS\-ST RS \(IN\-RE 048/18\), a Tabela ITEM\_APURAC\_SUBRS\_AJUSTE gravada pela Geração do Movimento, pode conter nota fiscal e cupom fiscal\. 

Para nota fiscal, esse campo é preenchido como descrito na regra acima considerando o campo 226 da SAFX07\.

Para cupom fiscal, este campo não é preenchido uma vez que estamos tratando apenas cupons de modelo 2D\.

# <a id="_Toc75783012"></a>Registro 1925 – Valores Declaratórios

__RN1925__

Este registro é “filho” do 1920, e é gerado a partir de dados informados pelo usuário\. Para isso foram criadas telas de manutenção para que o usuário possa cadastrar a cada período de apuração, as informações a serem gravadas no Sped Fiscal\.

A manutenção destas informações é feita no módulo Sped Fiscal, através dos itens de menu:

*Parâmetros à Registros E115 \(Valores Declaratórios\) \- Informações Adicionais da Apuração*

*Geração à Manutenção à Registros E115 \(Valores Declaratórios\)*

*Geração \- PIM à Manutenção à Registros E115 \(Valores Declaratórios\)*

Considerar *apenas* os valores declaratórios que atendam aos seguintes critérios:

- Campo “Sub Apuração” = Sub Apuração 1, Sub Apuração 2, Sub Apuração 3, Sub Apuração 4, Sub Apuração 5 ou Sub Apuração 6 dependendo da Sub Apuração a ser gerada;

Gravar um registro 1925 para cada registro informado pelo usuário para o período em questão\. O período informado deve ser o período da sub apuração gravado no registro 1910\. 

Poderão existir “n” registros 1925 para o período, inclusive com o mesmo código de informação adicional, campo 02\-COD\_INF\_ADIC \(este registro não tem chave, conforme documentação de Jan/2009, informação que foi confirmada pela Sefaz, em consulta feita em 09/Fev/2009\)\.

# <a id="_Toc75783013"></a>Registro 1926 – Obrigações a Recolher da Sub Apuração

__RN1926__

Este registro é “filho” do 1920, e é gerado a partir das guias de recolhimento de ICMS, cadastradas nos seguintes itens:

No Módulo ICMS:

“Apuração \- Apuração do ICMS \- Lançamentos Complementares – Apuração ICMS – Ajuste SINIEF \(aba Guia\)”

No Módulo PIM:

“Apuraçãoà Apuração dos Saldos de Impostois e Taxas à  Lançamentos Complementares à Apuração ICMS \(aba GUIA\)”

Considerar *apenas* as guias que atendam aos seguintes critérios:

- Campo “Sub Apuração” = Sub Apuração 1, Sub Apuração 2, Sub Apuração 3, Sub Apuração 4, Sub Apuração 5 ou Sub Apuração 6 dependendo da Sub Apuração a ser gerada;

Gravar um registro 1926 para cada guia informada pelo usuário para o período em questão\. O período informado deve ser o período da sub apuração gravado no registro 1910\. 

 \(pelo documento PVA\-RNG, este registro não tem chave\)

__RN1926\-05__

Campo COD\_REC:

__MFS33701__: A geração deste campo foi alterada para tratar as regras específicas de algunas UF’s, seguindo o mesmo procedimento realizado na geração do campo COD\_REC do registro E116\.

__Se UF do estabelecimento de geração for = SC,__

     O campo será preenchido com a concatenação da informação dos campos código de receita 

     \(4 caracteres\) e código de classe de vencimento \(5 caracteres\), num total de 9 caracteres\.

__Se UF do estabelecimento de geração for = ES,__

     O campo será preenchido com a inclusão de um __HÍFEN__ após o terceiro caractere do código\.

     De acordo com a tabela disponibilizada pela Receita, os códigos do estado do ES tem o padrão de

     4 dígitos, então a geração ficará da seguinte forma: o código __1015__ passaria a gerar __101\-5__\.

__Se UF do estabelecimento de geração for = SP,__

     O campo será preenchido com a inclusão de um __HÍFEN__ após o terceiro caractere do código\.

     De acordo com a tabela disponibilizada pela Receita, os códigos do estado do SP tem o padrão de

     4 dígitos, então a geração ficará da seguinte forma: o código __0462__ passaria a gerar __046\-2__\.

__Se UF do estabelecimento de geração for = RJ, __

     Se período da geração >= Maio/2014 e período da geração <= Dezembro/2018 \(campo 03\-DT\_FIN do 1910\)  

          Nesse caso, o campo será preenchido com a concatenação dos campos “Código de 

          Identificação do Débito \(RJ\)” \+ “Código da Receita”, no seguinte formato: \[DDDRRRR\], sendo:

            DDD – 3 dígitos referentes ao código de identificação do débito

            RRRR – 4 primeiros caracteres do código da receita

     Senão 

          O campo será preenchido apenas com o conteúdo do código da receita;

__Para as demais UF’s:__

     O campo será preenchido normalmente com o conteúdo do código da receita;

 

__RNE1926\-06__

Campo NUM\_PROC:

Campo preenchido com o número do processo da guia de recolhimento\. 

__\[MFS92607\] Versão de Layout 1\.16 \(jan/2023\)__

No layout 1\.16 o tamanho do campo passou de 15 para 60 posições\.

__Para Geração c/ leiaute anterior a EFD116 \(CAD\_LAYOUT – COD\_VERSAO<116\):__

- Caso o número do processo tenha mais de 15 caracteres, preencher esse campo com os 15 primeiros caracteres\.

__Para Geração c/ leiaute a partir da EFD116 \(CAD\_LAYOUT – COD\_VERSAO>=116\):__

- Preencher esse campo com o número do processo integral que foi inserido no sistema\.

__RN1926\-10__

Campo MES\_REF:

__Se__ o campo “Mês/Ano Referência” da guia de recolhimento estiver preenchido,

      Preencher o novo campo com o mês/ano de referência da guia;

__Senão__

      Preencher o novo campo com o mês/ano da apuração do ICMS \(mês/ano da DT\_FIM do 1910\);


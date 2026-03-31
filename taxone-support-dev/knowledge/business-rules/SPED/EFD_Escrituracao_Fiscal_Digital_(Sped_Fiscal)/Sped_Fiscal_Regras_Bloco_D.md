# Sped_Fiscal_Regras_Bloco_D

- **Fonte:** Sped_Fiscal_Regras_Bloco_D.docx
- **Modificado:** 2026-03-18
- **Tamanho:** 269 KB

---

Sped Fiscal – Bloco D

Quadro de Revisões

__                         Revisões realizadas a partir de 07/04/2016__

*            \(para consultar revisões anteriores, verificar o documento das revisões originais\)*

__Data__

__OS / Chamado__

__Descrição__

__Responsável__

24/10/2016

MFS7429

Alteração no campo NOM\_MEST do registro D695, ajustando o tratamento do tamanho do campo

Jefferson Mota

28/11/2016

MFS8257

Aumento do campo NOM\_MEST do registro D695 a partir da versão 1\.10 \(ver __RND695\-08__\)\. 

Vânia Mattos

06/03/2017

MFS8937

Alteração GP vrs 2\.0\.20: Alterados registros E113 \(campo 10\), E240 \(campo10\) e E313 \(campo 7\) p/ o mod 67 \(RNE113\-10, RNE240\-10 e RNE313\-07\)

Andréa Rocha

03/04/2018

MFS17478

Criação de Parâmetro para inibir a geração das informações de PIS e COFINS

Andréa Rocha

17/04/2018

MFS17511

Criação de Parâmetro para inibir a geração das informações de PIS e COFINS \(Parte 2\)

Andréa Rocha

24/07/2018

MFS\-18252

Alteração no preenchimento do campo 12 do Registro D190 para recuperar nas entradas a informação do campo 155 – Código da Observação da SAFX08, considerando o primeiro registro lido da combinação de itens selecionados nos critérios de agrupamento do registro\.

Julyana Perrucini

28/08/2018

CH21958\_2018

\(MFS20668\)

Inclusão do modelo de documento CT\-e OS, Modelo 67 no registro D100 do SPED Fiscal\.

João Henrique

08/10/2018

CH24606\_2018 \(MFS\-21413\)

Ajuste no preenchimento do campo 09 do Registro D190 e no preenchimento do campo 11 do Registro D590\.

Julyana Perrucini

21/03/2019

MFS25498

Alteração da regra do modelo 57 para o registro D100

Andréa Rocha

25/10/2019

MFS20217

Alterado o processo de geração do registro D696 para desconsiderar movimentos cancelados\. \(RND696\)\.

Alessandra Cristina Navatta

11/02/2019

MFS34070

Inclusão do modelo 63 na geração dos registros D100 e D101

Andréa Rocha

16/03/2021

MFS60545

Inclusão de tratamento do Campo COD\_INF do Registro D100 \(__RND100\-22__\) e D500 \(__RND500\-20__\)\.

Rogério Ohashi

15/07/2021

MFS69058

Inclusão de tratamento do Campo __COD\_OBS e COD\_INF\_OBS__\. 

Rogério Ohashi

03/08/2021

MFS69901

Inclusão de regra para considerar na regra os CST’s “não tributados” na geração do Campo 15 do Registro D500

Rogério Ohashi

21/10/2021

MFS73695

Alteração do campo 24 do registro D100, incluindo obrigatoriedade para notas de saída e mensagem de log\.

Aline Melo

22/12/2021

__MFS77885__

Alteração na regra geral, para o Registro D100, a partir do Layout EFD115 \(CAD\_LAYOUT– COD\_VERSAO>=115\) não gerar as Notas Fiscais Denegadas e Inutilizadas de Saídas\. Conforme ajuste Sinief nº 038 DOU de 08/10/2021 que altera o Ajuste Sinief nº 7/05\.

Rogério Ohashi

01/12/2022

MFS96211

__AC 21/2022, nova versão 1\.16, Jan/2023__

Inclusão da geração do registro D700 e filhos para notas de entradas\.

Liliane Assaf

21/03/2023

MFS523869

Inclusão do modelo 63 na tratativa dos campos do D100\.

Aline Melo

21/09/2023

MFS580250

__Versão 1\.17 – Jan/2024__

D700, D730, D731, D735, D737: tratamento para notas de Entrada modelo 62 \(NFCom\)\.

Liliane Assaf

21/09/2023

MFS577999

__Versão 1\.17 – Jan/2024__

D700, D730, D731, D735, D737: tratamento para notas de Saídas modelo 62 \(NFCom\)\.

Liliane Assaf

21/09/2023

MFS578013

__Versão 1\.17 – Jan/2024__

D750, D760, D761: tratamento para notas de saídas modelo 62 \(NFCom\)\.

Liliane Assaf

20/12/2023

MFS591806

Ajuste nos campos __Finalidade Emissão da Nfe__ e __Modelo Doc\. Fiscal NF Substituída __para atendimento ao __Modelo de Documento 57 __ atendimento ao Infolegis nº 198/23 – Z – 649 \- EFD ICMS/IPI – CT\-e Substituição – SPED Fiscal Registro D100 \- campo 14\.

Graciela Soares

27/12/2023

MFS592577

Ajuste na composição dos campos VL\_DOC \(Valor do documento\) dos registros D700, D730, D750 e D760, conforme atualização do Guia Prático Versão 3\.1\.6

Graciela Soares

16/02/2023

MFS611132

Ajuste na composição dos campos VL\_SERV e VL\_SERV\_NT dos registros D700 e D750\. 

Andréa Rocha

12/09/2023

MFS683935

Alteração da regra do campo 14\-CHV\_CTE\_REF do registro D100\. 

Andréa Rocha

02/10/2024

MFS690865

__Versão 1\.18 – Janeiro/2025__

Guia prático 3\.1\.7

Inclusão de campos:

__1\)__ D700: novo campo 32 – DED

__2\)__ D750: novo campo 17 – DED

Alteração nas regras de campos já existentes:

__1\)__ D700: campos 23\-FIN\_DOCe e 24\-TIP\_FAT tornam\-se obrigatórios\.

__2\)__ D700 e D750 campo VL\_DOC cálculo passa a considerar campo DED\.

__3\)__ D700: VL\_BC\_ICMS e VL\_ICMS atender a regra do guia prático *“Nas entradas, a informação dos campos VL\_DOC, VL\_DESC, VL\_SERV, VL\_SERV\_NT, VL\_TERC e VL\_DA não deve levar em conta os serviços com cClass 110, 120 e 130”*\.

Retirar a restrição dos campos VL\_BC\_ICMS e VL\_ICMS\.

__4\)__ D730 e D760: VL\_OPR só considerar serviços tributados de ICMS \(CST <> 30, 40, 41, 50, 51, 90\)\.  Mesma regra do campo VL\_SERV do D700 e D750\.

Escopo da MFS627011 unificada c/ MFS690865:

Considerar os itens informativos \(10\-Tipo de Item da SAFX43 = ‘1’\) que são itens sem CST, no campo VL\_SERV\_NT\. Veja:

__1\) __D700 e D750: Considerar valor do serviço dos itens sem CST no campo VL\_SERV\_NT e desconsiderar do VL\_SERV\. 

__2\) __D730 e D760: Não considerar valor do serviço dos itens sem CST no campo VL\_OPR\. Mesma regra do campo VL\_SERV do D700 e D750\.

__3\) __D700: MES\_DOC\_REF ajustar a regra p/ considerar os campos da SAFX07: 75\-DAT\_DI e 326 \- PERIOD\_APUR\_SUBST\.

Liliane Assaf

31/10/2024

MFS693897

__Versão 1\.18 – Janeiro/2025__

Guia prático 3\.1\.7

Graciela Soares

06/12/2024

MFS712819

__Versão 1\.18 – Janeiro/2025__

Guia prático 3\.1\.8 – Ajuste Registro D100

Graciela Soares

28/03/2025

MFS779959

NFCOM \- Tratamento da Devolução do Valor do Item \(SAFX43 \- 20\-IND\_ADIC\_DESC = D\) nos registros D700 e filhos\.

Os Documentos Fiscais Eletrônicos de modelo 62 \(NFCOM\) podem conter itens com devolução de valor\.  Tais itens são identificados pela tag 115\-indDevolucao = 1 \(XML da NFCOM\) e carregados na SAFX43 com campo 20 \- Adição/Desconto = 'D'\.

Na Geração dos registros D700/D750 e filhos, os itens com devolução de valor, terão efeito redutor, ou seja, seus valores são subtraídos e não somados na contabilização dos valores de Base ICMS, ICMS, Serviços, Terceiros, Descontos, Dedução, PIS, COFINS\.

Liliane Assaf

28/03/2025

MFS779975

NFCOM \- Tratamento da Devolução do Valor do Item \(SAFX43 \- 20\-IND\_ADIC\_DESC = D\) nos registros D750 e filhos

Os Documentos Fiscais Eletrônicos de modelo 62 \(NFCOM\) podem conter itens com devolução de valor\.  Tais itens são identificados pela tag 115\-indDevolucao = 1 \(XML da NFCOM\) e carregados na SAFX43 com campo 20 \- Adição/Desconto = 'D'\.

Na Geração dos registros D700/D750 e filhos, os itens com devolução de valor, terão efeito redutor, ou seja, seus valores são subtraídos e não somados na contabilização dos valores de Base ICMS, ICMS, Serviços, Terceiros, Descontos, Dedução, PIS, COFINS\.

Liliane Assaf

07/08/2025

MFS877470

Alteração da regra de geração dos campos 13 \- VL\_SERV do registro D700 e 05 – VLR\_OPR do registro D730, quando o CST for igual a 90\.  O código CST 90 pode indicar operações tributadas ou não tributadas pelo ICMS\.

Andréa Rocha

12/09/2025

MFS877174/MFS910283

Criação da tabela particionada DWT\_DOCTO\_FISCAL\_SPED espelho da DWT\_DOCTO\_FISCAL e utilização na geração dos registros C100, C500, D100, D500 e 1400 – UF = SP\.

Liliane Assaf

28/10/2025

MFS861832

Alteração da geração do código do participante do registro D100, para tratar a situação do DIFAL da EC 87/2015, que deve gerar um registro 0150 adicional indicando o código do município onde ocorrer a entrada física, mantidos os demais dados do adquirente ou tomador\.

Andréa Rocha

27/11/2025

MFS983144

Retirar a Execssão do registro D100 campo 25 \(Município de Destino\) aplicada para os documentos de Situação Especial, Cte Simplificado e Substituição de Cte Simplificado para atendimento ao ajuste do Guia Prático 3\.2\.1, onde não será utilizado o código “9999998”

Graciela Soares

02/12/2025

MFS989592

Alteração das regras do campo 04\-

ALIQ\_ICMS do registro D730 e do campo 04\-ALIQ\_ICMS do registro D760, para incluir a alíquota do FECEP na composição dos campos\.

Andréa Rocha

16/12/2025

MFS1000266

Alteração das regras dos campos 14\-

VL\_SERV\_NT e 32\-DED do registro D700, para tratar a situação de dedução\. 

Andréa Rocha

09/02/2026

MFS1039052

Alteração da regra dos campos 09\- VL\_SERV\_NT e 17\-DED do registro D750, para tratar a situação de dedução\. 

Andréa Rocha

#### Bloco D – Documentos Fiscais II – Serviços \(ICMS\) 

__Registro D001 – Abertura do Bloco D__

RND001

Um registro por arquivo\.

__Registro D100 \- Nota Fiscal de Serviço de Transporte \(Código 07\),__

__Conhecimentos de Transporte Rodoviário de Cargas \(Código 08\),__

__Conhecimentos de Transporte de Carga avulso \(Código 8B\),__

__Conhecimento de Transporte Aquaviário de Cargas  \(Código 09\),__

__Conhecimento Aéreo \(Código 10\), __

__Conhecimento de Transporte Ferroviário de Cargas \(Código 11\),__

__Conhecimento de Transporte Multimodal de Cargas \(Código 26\),__

__Nota Fiscal de Transporte Ferroviário de Carga \(Código 27\),__

__Conhecimento de Transporte Eletrônico – Cte \(Código 57\),__

__Conhecimento de Transporte Eletrônico para Outros Serviços \- CT\-e OS \(Código 67\) e Bilhete de Passagem Eletrônico \(código 63\)\. __

<a id="_Hlk130886017"></a>__RND100__

Este registro deve ser apresentado por todos os contribuintes adquirentes ou prestadores dos serviços que utilizem Nota Fiscal de Serviço de Transporte, Conhecimentos de Transporte Rodoviário, Transporte de Cargas Avulso, Aquaviário, Aéreo, Ferroviário ou Multimodal de Cargas\.

Devem ser gravados os documentos com modelos correspondentes aos seguintes códigos da tabela “4\.1\.1\-Tabela de Documentos Fiscais do ICMS” do Sped Fiscal:  

07 \- Nota Fiscal de Serviço de Transportes;

08 – Conhecimento de Transporte Rodoviário de Cargas;

8B – Conhecimento de Transporte de Carga Avulso;

09 \- Conhecimento de Transporte Aquaviário de Cargas;

10 \- Conhecimento Aéreo;

11 \- Conhecimento de Transporte Ferroviário de Cargas;

26 \- Conhecimento de Transporte Multimodal de Cargas, \(somente para fretes com Movimento Entrada/Saída = “1”\);

27 \- Nota Fiscal de Transporte Ferroviário de Cargas; \(somente para fretes com Movimento Entrada/Saída = “1”\);

57 – Conhecimento de Transporte Eletrônico \(CT\-e\);

63 – Bilhete de Passagem Eletrônico;

67 – Conhecimento de Transporte Eletrônico para Outros Serviços \(CT\-e OS\)\.

__Alteração feita em Nov/2009, OS2388\-E14:__

A partir da release 35, a geração do D100 foi alterada para considerar os dados da nova tabela SAFX130\. As regras da geração a partir desta SAFX130 se encontram descritas ao final da RND100\. 

__MFS877174/MFS910283__

Criação da tabela particionada DWT\_DOCTO\_FISCAL\_SPED espelho da DWT\_DOCTO\_FISCAL e utilização na geração dos registros C100, C500, D100, D500 e 1400 – UF = SP\.

__Geração a partir das notas da SAFX07/SAFX08__:

A identificação do código deve ser feita pelo campo “__13 – Modelo de Documento__” da SAFX07\.

__Critério para seleção das notas:__

__Notas de Entrada de Terceiros __à Selecionar na tabela SAFX07 as prestações de serviços de transportes/notas fiscais emitidas por terceiros:

Alteração CH21958\_2018:

MFS20668

      Movimento Entrada/Saída = “1”,

       Se Modelo de Documento = 07, 08, 8B, 09, 10, 11, 26, 27, 57 ou 67\.

              Classificação do Documento Fiscal = “1”,

                              Situação da Nota = “N” \(\*\)

Alteração CH8770\_2012:

      Movimento Entrada/Saída = “1”, NORM\_DEV = 1

       Se Modelo de Documento = 07, 67 

              Classificação do Documento Fiscal = “2”

                              Situação da Nota = “N” \(\*\)

\(\*\) desconsiderar as notas de terceiros canceladas, que por um erro qualquer podem estar na base de dados;

## Notas de Entrada  Emitidas pelo próprio Estabelecimento à Se código da versão do layout for = ou > a “002” \(campo 02 do registro 0000\)”; selecionar na tabela SAFX07 as prestações de serviços de transportes e/ou notas fiscais emitidas pelo estabelecimento com as seguintes condições:

Movimento Entrada/Saída = “2”; “3”; “4” ou “5”;

 Se Modelo de Documento = 07, 08, 8B, 09, 10, 11, 26, 27, 57 ou 67;

         Classificação do Documento Fiscal = “1”  à se for nota fiscal \(modelo = 07\);

                      Classificação do Documento Fiscal = “1” ou “4” à se for conhecimento \(modelo = 08, 8B, 09, 10, 11,  26, 27, 57 ou 67\)\.

## Notas de Saída à Se código da versão do layout for = ou > a “002” \(campo 02 do registro 0000\); selecionar na tabela SAFX07 as prestações de serviços de transportes e/ou notas fiscais emitidas com as seguintes condições:

Movimento Entrada/Saída = “9”;

Se Modelo de Documento = 07, 08, 8B, 09, 10, 11, 26, 27, 57, 67 e 63;

     Classificação do Docto Fiscal = “1”  à se for nota fiscal \(modelo = 07\) __OU__        

                                       Conhecimento de Modelo = 08 \(\*\) __OU__ modelo = 57 \[MFS25498\];

     Classificação do Documento Fiscal = “4” à se for conhecimento \(modelo= 08, 8B, 09, 10, 11, 26, 27, 57 ou 67\)\.

\(\*\*\) __\[MFS523869\] __conforme orientação do Guia Prático versão 3\.1\.3, o bilhete de passagem eletrônico \(BP\-e modelo 63\), não devem ser escriturados nas entradas\.

\(\*\) Alteração feita no chamado CH68490\-DHL devido à situação especial do cliente, que emite CTRC modelo 08 com dois valores de BC e diferentes alíquotas, e para isso, carrega o documento com classificação fiscal = ‘1’ para poder carregar os valores diferenciados na SAFX08 \(ver doc CH68490 com todo histórico da situação\);

__OBS:__ Na geração o aplicativo deverá apresentar mensagem informativa no log de processos se o código da versão do layout for =  “001” e o bloco D100 estiver selecionado no perfil\.

                    

__Descrição do Campo:__

__Nº do Campo:__

__Nome do Campo:__

Modelo de Documento

13

COD\_MODELO

Classificação do Documento Fiscal

12

COD\_CLASS\_DOC\_FIS

Movimento Entrada/Saída

3

MOVTO\_E\_S

Situação da Nota

30

SITUACAO

Situação Especial

125

IND\_SITUACAO\_ESP

__Algumas Considerações para Situações Especiais:__

1\)Documento Complementar:

Se campo COD\_SIT no registro D100 = “06” ou “07”, gerar somente D100 e D190 de acordo com a regra em anexo\.

__Escrituração MasterSAF__

O tratamento do documento nos livros P1/P2/P9 está associado ao parâmetro 48 \(“Tratamento das NFs de Complemento de ICMS”\)  da parametrização por UF\.

__P1/P2__ \- Se o parâmetro 48 estiver ativo, o documento não será considerado no LRE, LRS e no arquivo EFD\.

__P9__ \- Se o parâmetro 48 estiver ativo, o documento não será considerado no LRA e no arquivo EFD\.

__Geração do Reg\. D100__

Na geração do __D100__ se parâmetro 48 estiver ativo, gravar:

\-IND\_OPER

\-COD\_EMIT

\-COD\_PART

\-COD\_MOD

\-COD\-SIT

\-SER

\-SUB

\-NUM\_DOC

\-CHV\_CTE 

\-DT\_DOC

\-DT\_A\_P

\-TP\_CTe 

\-CHV\_CTE\_REF 

\-IND\_FRT 

\-COD\_INF

\-COD\_CTA

__Geração do Reg\. D190__

Na geração do __D190__ de acordo com parâmetro de escrituração do livro P2 e P2A:

Gravar D190 considerando a seguinte regra:

\- Se o parâmetro 48 estiver ativo, os valores referentes ao Docto \(Valor Operação,  Aliquota do ICMS, Base ICMS, ICMS e Base Reduzida\) não devem ser considerados na totalização dos itens\. 

\- Se o parâmetro 48 estiver desativado a totalização deve ser feita normalmente, e todos os campos do D190 serão preenchidos normalmente\.

2\)Conhecimento de Transporte Eletrônico – CTe \(modelo 57\) ou CTe OS \(modelo 67\)

Se campo COD\_SIT no registro D100 = “00” ou “01”, IND\_EMIT = 0

           Gerar registros D100 e D190 normalmente\. 

__           \[MFS693897\]__ E D130 quando o campo 125 \(Situação Especial\) da SAFX07 for igual a    

           “G” ou “H” \(CT\-e Simplificado\) ou “H” \(Substituição CT\-e Simplificado\)\.

Senão,

          Gravar os registros conforme cada regra definida para o campo COD\_SIT\.

Código

Descrição

00

Documento regular

01

Documento regular extemporâneo

02

Documento cancelado

03

Documento cancelado extemporâneo

04

NF\-e ou CT\-e \- denegado

05

NF\-e ou CT\-e \- Numeração inutilizada

06

Documento Fiscal Complementar

07

Documento Fiscal Complementar extemporâneo\.

08

Documento Fiscal emitido com base em Regime Especial ou Norma Específica

3\)Documento Fiscal emitido com base em Regime Especial ou Norma Específica 

Se campo COD\_SIT no registro D100 = “08”, 

        Gerar registros D100 e D190 normalmente\.

Alteração OS3526\-B:

Para os documentos com o campo 125 da SAFX07 \(IND\_SITUACAO\_ESP\) = “D” 

e CFOP’s  “1922, 2922, 3922, 1117, 2117, 3117, 5922, 6922, 7922, 5116, 6116 ou 7116” \(campos 14 da SAFX07, 22 da SAFX08 ou 17 da SAFX09 – COD\_CFOP\), 

Gerar este campo com valor “08”\.

O sistema deve considerar também a seguinte parametrização para a geração do D100:

__Módulo__: SPED à EFD – Escrituração Fiscal Digital 

__Menu__: Parâmetros à Dados Iniciais

__Parâmetro:__ “Situação Especial 08 – Faturamento Simples”

Se a opção ICMS estiver desmarcada, os campos ALIQ\_ICMS, VL\_BC\_ICMS, VL\_ICMS e VL\_RED\_BC devem apresentar o valor zero \(0,00\), tendo em vista que não serão considerados para os livros P1, P1A, P2, P2A e P9\.

Se estiver marcada, apresentar os valores normalmente\.

= = = fim Alteração OS3526\-B

4\) Documento Cancelado, Denegado ou Inutilizado

Se campo “Movimento Entrada/Saída” da SAFX07 <> “1”; 

\(Alteração – CH11564\_2012\)

Se campo COD\_SIT no registro D100 = “02”, “03” e “04”    

      Preencher somente os campos:  REG, IND\_OPER, IND\_EMIT, COD\_MOD, 

      COD\_SIT, SER, SUB e NUM\_DOC e CHV\_CT\-e

Se campo COD\_SIT no registro D100 = “05”,

     Devem ser informados todos os campos referidos acima, __exceto o campo CHV\_CT\-e\.__

Demais campos deverão ser apresentados com conteúdo = “||”\.

Não deverão ser informados registros filhos\. 

__Observação sobre as notas extemporâneas:__

Os documentos com datas extemporâneas serão tratadas normalmente, exatamente da mesma forma como é feito na versão atual do Mastersaf, ou seja, documentos com data extemporânea é lançada normalmente nos livros P1/P2/P9, sem nenhum tipo de tratamento especial\. A lógica para recuperação destas notas devem ser a mesma que é aplicada hoje nos livros:

*Se \(data\_fiscal entre data inicial e data final e data\_extemporânea não preenchida\) *

*ou data\_extemporânea entre data inicial e data final*

 \[Alteração – OS 3227\]: Exceção para notas fiscais extemporâneas de Saída: Não apresentar os valores de base e ICMS dos documentos extemporâneos de saída, tendo em vista que não serão considerados para os livros P2, P2A e P9\.

= = = = =

Na geração do arquivo observar as regras de gravação dos campos que gravam códigos e devem possuir referências em outro registro\.

D110/Campo: 02 à O valor informado deve existir no registro 0200, campo COD\_ITEM 

D100/Campo: 04 à O valor informado deve existir no registro 0150 

D130/Campo: 02 e 03 à O valor informado deve existir no registro 0150 

D140/Campo: 02 à O valor informado deve existir no registro 0150 

D100/Campo: 22 à O valor informado deve existir no registro 0450; 

= = = = =

__OBS1: __Sobre a geração por Inscrição Estadual Única:

Nas operações de entrada à considerar os documentos de todos os estabelecimentos envolvidos na centralização;

Nas operações de saída à o tratamento da I\.E\.U\. foi implementado para as operações de saída na OS2388\-E9, para atendimento ao cliente TAM que trabalha por I\.E\.U\. 

__OBS2__: Na geração por Inscrição Estadual p/os usuários do PIM \(Pólo Industrial de Manaus\), os documentos fiscais serão filtrados pela inscrição estadual \(campo 126 da SAFX07\)\. As empresas do PIM geram um arquivo para cada Inscrição Estadual\. Os  registros “filhos” do D100 são gerados normalmente, já que o filtro é feito apenas no registro pai \(nota gravada no D100\) \(ver detalhes nas __OS2388\-AM\*__, que definiram a geração do Sped Fiscal para o PIM\)\.

__OBS3__: A __VAF\-MG__ a partir de 2020 passou a ser gerada com base nas regras de vários registros do SPED FISCAL \(C190, D190\.\.\.\)\. Ao realizar uma alteração na regra de geração dos registros D100 e D190, como inclusão de um modelo, um critério de recuperação da nota, um tratamento de situação especial, a regra de geração da VAF\-MG deve ser revista \(tópico 2 do MTZ\-VAFMG\_Geracao\_Relatorio\_EFD\-Fiscal\.docx\)\.

= = = = =

__Para Geração c/ leiaute anterior a EFD115 \(CAD\_LAYOUT – COD\_VERSAO<115\):__ 

__Geração do D100 a partir das notas da SAFX130__:

\(alteração feita em Nov/2009, OS2388\-E14\)

Recuperar todas as notas da SAFX130 conforme os seguintes critérios:

\-Empresa               = empresa da geração

\-Estabelecimento  = estabelecimento da geração \(tratar a situação da geração p/ I\.E\.U\.\)

\-Data de Referência  = deve estar contida no período da geração do arquivo

\-Modelo                      =  __57__ \(CT\-e\) ou __67__ \(CT\-e OS\) 

\-Inscrição Estadual    = inscrição estadual da geração \(este critério é usado somente na opção “Geração – PIM”\) 

Para cada linha recuperada da SAFX130, gerar os dados no D100 da seguinte forma:

Se Número Documento Final *não preenchido*:

      Gravar *um único* D100, com os dados:

      \-REG           = ‘D100’

      \-IND\_OPER = se MOVTO\_E\_S = 2, 3, 4 ou 5, gravar “0”, senão gravar “1”

      \-IND\_EMIT   = 0 \(emissão própria\)

      \-COD\_MOD = modelo 

      \-COD\_SIT  = se situação da nota denegada \(1\) gravar 04, se inutilizada \(2\), gravar 05 

      \-SER          = gravar o conteúdo da série apenas quando seu conteúdo for <> branco,

                            caso contrário, deixar o campo sem preenchimento \(gravar ||\) 

      \-SUB          = gravar o conteúdo da subsérie apenas quando seu conteúdo for <> 

                            branco, caso contrário, deixar o campo sem preenchimento \(gravar ||\) 

      \-NUM\_DOC = número do documento fiscal inicial

Se Número Documento Final *preenchido*: 

      Gravar vários registros D100, desde o número do documento inicial até o número do

      documento final\. Ou seja, gravar um registro D100 para cada número contido na

      seqüência do número inicial até o número final\. Os dados devem ser gravados com as

      mesmas informações descritas acima, diferenciados apenas pelo número do

      documento\.

Obs: Estas notas gravadas no D100 a partir da SAFX130 não terão os registros filhos, e apenas alguns campos são preenchidos, da mesma forma que é feito para as notas denegadas e inutilizadas da SAFX07\.

\(os campos do D100 não citados acima não serão informados, e devem ser gravados apenas com ||\)  

__Para Geração c/ leiaute a partir da EFD115 \(CAD\_LAYOUT – COD\_VERSAO>=115\):__

__\[MFS77885\] __Tratamento p/ Notas Fiscais Denegadas e Inutilizadas com Origem da SAFX07 e SAFX130

__Origem SAFX130__

As notas gravadas no Registro D100 a partir da tabela SAFX130 \(notas denegadas ou inutilizadas\) não devem ser consideradas no arquivo meio magnético, a partir do layout versão 1\.15 \(Janeiro/2022\);__ __

__Origem SAFX07__

__Se__ o Campo 231 \- IND\_NFE\_DENEG\_INUT da tabela SAFX07 for igual à ‘1’ ou ‘2’;

    __Não preencher__ o Registro D100, Notas Fiscais denegadas ou inutilizadas __não devem ser consideradas__ no arquivo meio magnético, a partir do layout versão 1\.15 \(Janeiro/2022\)

1 \- Nota Fiscal Eletrônica denegada;

2 \- Nota Fiscal Eletrônica inutilizada\.

= = = = =

RND100\-FRT

Regras especiais para Conhecimento de Transporte Internacional\.

Conhecimento de Transporte Internacional:

Os conhecimentos de transportes internacionais devem ter um tratamento especial:

Alteração do Guia Prático vrs 1\.0\.4 \(OS2388\-E13, release 34\.1\):

Nas operações com destino ou origem em cidades fora do Brasil, os municípios devem ser preenchidos com “9999999” ao invés de “0000000”, como antes\. A alteração se refere *a todos* os campos de município dos registros D120, D130, D140, D150, D160 e D161\. 

Se UF Origem \(campo:117/SAFX07\) = EX,

     Se for o caso, na geração do arquivo do SPED, gravar o conteúdo do campo

     COD\_MUN\_ORIG com “0000000” __“9999999”__, de acordo com os campos

     definidos no DEPARA\.

 Se UF do Remetente \(campo: 24/SAFX51\) = EX,

       Se for o caso, na geração do arquivo do SPED, gravar o conteúdo do campo

       COD\_MUN\_ORIG e/ou COD\_MUN\_COL com “0000000” __“9999999”__, de

       acordo com os campos definidos no DEPARA\.

*  *

Se UF Destino \(campo:122/SAFX07\) = EX,

      Se for o caso, na geração do arquivo do SPED, gravar o conteúdo do campo

      COD\_MUN\_DEST com “0000000” __“9999999”__, de acordo com os campos

      definidos no DEPARA\.

 Se UF do Destinatário \(campo: 30/SAFX51\) = EX,

       Se for o caso, na geração do arquivo do SPED, gravar o conteúdo do campo

       COD\_MUN\_DEST e/ou COD\_MUN\_ENTG com “0000000” __“9999999”__, de

       acordo com os campos definidos no DEPARA\.

RND100\-02

__Campo IND\_OPER__:

A partir do conteúdo do indicador de Entrada/Saída da nota \(campo 03\-Movimento Entrada/Saída da SAFX07\), verificar:

Se campo “Movimento Entrada/Saída” = 9 à gravar 1 \(prestação\)

Se campo “Movimento Entrada/Saída” <> 9 à gravar 0 \(aquisição\)

RND100\-03

__Campo IND\_EMIT__:

A partir do conteúdo do indicador de Entrada/Saída da nota \(campo 03\-Movimento Entrada/Saída da SAFX07\), verificar:

Se campo “Movimento Entrada/Saída” = 1 à gravar 1 \(emissão terceiros\)

Se campo “Movimento Entrada/Saída” <> 1 à gravar 0 \(emissão própria\)

__OBS:__ Se este campo tiver valor igual a 1 \(terceiros\), então o campo IND\_OPER deve ser igual a 0 \(entradas\)\. Se este campo tiver valor igual a 0 \(emissão própria\), então o campo IND\_OPER poderá ser \*igual a 0 \(entradas\) ou 1 \(prestação\)\.

<a id="_Hlk130818689"></a>RND100\-04

__Campo __<a id="_Hlk130818701"></a>__COD\_PART__

__\[MFS 523869\] __Se o campo Modelo de Documento = 63 \(SAFX07\), campo não deve ser informado\.

__\[MFS861832\]__ Tratamento relativo ao DIFAL da EC 87/2015

Se Geração for c/ leiaute a partir da EFD119 \(CAD\_LAYOUT – COD\_VERSAO>=119\) e o parâmetro "Gerar registro 0150 com município destino relativo ao DIFAL da EC 87/2015" da tela de Dados Iniciais estiver selecionado, verificar

     Se nota fiscal de saída \(indicador de movimento E/S = 9\) e o Modelo do Documento for   

     igual “57” ou “”67 e um dos campos utilizados no registro D101 

      estiver preenchido \(Valor FCP UF Destino, Valor ICMS UF Destino ou Valor ICMS UF 

     Origem\)\*\*, verificar

           Se a UF destino da nota \(campo 122 da SAFX07\) for diferente da UF da PFJ da nota 

           \(campo 19 da SAFX04\)

                Considerar o município destino da nota \(campo 183 da SAFX07\) para gerar o   

                código do participante, que será gerado com a concatenação do código do 

                participante \+ ‘\-‘ \+ Código da UF \+ código do município destino 

                \(Ex\.: 1\-40254518000176\-3304557, sendo Código Participante = 1\-

                 40254518000176,  código UF= 33 e Código Município = 04557\)\.

   

                __Obs\.:__  Se o código da PFJ não possuir 14 posições, completar com espaços à direita para preencher as 14 posições e depois concatenar com o município para gravar na tabela temporária e posteriormente gerar o registro 0150\. Para gerar o COD\_PART no  registro C100, não precisa completar com espaço em branco\.

\[OS4747\] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

\*\* Campos utilizados no Registro D101:

   \- Notas com itens à  \(SAFX08, campos 221, 222 e 223\);

   \- Notas sem itens à  \(SAFX07, campos 283, 284 e 285\)

RND100\-06

__Campo: COD\_SIT__

Para o preenchimento deste campo deverão ser verificados alguns campos da SAFX07, conforme segue:

Se for nota eletrônica,  verificar:

     se a nota for denegada  à gravar “04”

     se a nota for  inutilizada à gravar “05”

Se for nota cancelada, verificar:

      se a nota é extemporânea           à gravar “03”

      se a nota é normal \(não extemp\.\) à gravar “02”

Se for nota extemporânea, verificar:

      se a nota é complementar          à gravar “07”

      se a nota é normal \(não compl\.\) à gravar “01”

Se for nota complementar, verificar:

      gravar “06”

Se nota tem Ato Normativo, Regime Especial etc\.\.\.

      gravar “08”

Se a nota não atende a nenhuma das opções anteriores:

      gravar “00”

__Importante:__ 

Os testes devem ser executados exatamente nesta prioridade\. Assim, o teste deve ser encerrado na primeira regra atendida pela nota, e sempre que isto *não ocorrer*, será gravado o conteúdo “00”\.

A lógica seria a seguinte:

__Se__ nota é eletrônica  e  foi  \(denegada ou inutilizada\)

        __Se__ nota é denegada

              gravar “04”

        __Senão__*  \(é inutilizada\)*

              gravar “05”

# Senão

        __Se__ nota é cancelada

             __Se__ nota é extemporânea

                   gravar “03”

             __Senão__

                   gravar “02”

#         Senão

              __Se__ nota é extemporânea

                    __Se__ nota é complementar

                         gravar “07”

                    __Senão__

                         gravar “01”

              __Senão__

                    __Se__ nota é complementar

                         gravar “06”

                    __Senão__

                         __Se__ nota tem Ato Normativo, Regime Especial etc

                              gravar “08”

                         __Senão__

                             gravar “00”;

__Campos da SAFX07 para verificação das regras:__

Nota cancelada à campo “30\-Situação da nota” =  “S”;

Nota extemporânea à campo “77\-Data Escrita Extemporânea” estará preenchido;

Nota complementar à campo “125\-Situação Especial” = “5”;

Nota Eletrônica à campo “13\-Modelo de Documento” =  “57”;

Nota Eletrônica denegada à campo “13\-Modelo de Documento” =  “57” e o campo “231\-Nfe Denegada/Inutilizada” = “1” \(denegada\);

Nota Eletrônica inutilizada à campo “13\-Modelo de Documento” =  “57” e o campo “231\-Nfe Denegada/Inutilizada” = “2” \(inutilizada\);

Nota com Ato Normativo, Regime Especial etc à o campo “232\-NF Baseada em Regime Especial ou Norma Específica” será = “S”;

__\[Alteração – OS3526\-B\] __

Documentos com o campo 125 da SAFX07 \(IND\_SITUACAO\_ESP\) = “D” e CFOP’s  “1922, 2922, 3922, 1117, 2117, 3117, 5922, 6922, 7922, 5116, 6116 ou 7116” \(campos 14 da SAFX07, 22 da SAFX08 ou 17 da SAFX09 – COD\_CFOP\), 

Gerar este campo com valor “08”\.

__RND100\-07__

__Campo 07\-SER__:

__\[ALTERADA – CH7058\_2015\]__

Alteração __MFS8937:__

Esse campo é de preenchimento obrigatório com três posições para CT\-e e CT\-e OS, então considerar na geração:

Se o documento fiscal for de emissão própria ou de terceiros campo 03\-IND\_EMIT igual a “0” ou “1” \(origem campo 03\-Movimento Entrada/Saída da SAFX07 ver RND100\-03\) e o campo 05\-COD\_MOD for igual a “57” ou “67” \(origem campo 13\-Modelo de Documento/09\-Modelo do Documento da SAFX07/SAFX130 = 57 ou 67\), considerar as três posições do campo 09\-Série do Docto Fiscal/06\-Série do Docto Fiscal, mas caso seja menor do que o esperado preencher com zeros à esquerda e ainda se não estiver preenchida preencher com zeros \(000\)\.

<a id="_Hlk130819186"></a>__RND100\-08__

<a id="_Hlk130819175"></a>__Campo 08\-SUB__:

__\[MFS 523869\]__ Se o campo Modelo de Documento = 63 \(SAFX07\), campo não deve ser informado\.

<a id="_Hlk130820600"></a>RND100\-10

<a id="_Hlk130820584"></a>__Campo: CHV\_CTE__

__\[MFS 523869\] __Inclusão do modelo 63 BP\-e\.

Alteração __MFS8937:__

Informar neste campo a chave do conhecimento de transporte eletrônico ou bilhete de eletrônico \(SAFX07\-Campo: 226\), se campo Modelo de Documento = 57, 67 ou 63 \(SAFX07\)\. 

DADOS INFORMATIVOS:

A Chave de Acesso do Conhecimento de Transporte Eletrônico é representada por uma seqüência de 44 caracteres numéricos, representados da seguinte forma:

__Nome do Campo__

__Quantidade de caracteres__

Código da UF

02

AAMM da emissão

04

CNPJ do Emitente

14

Modelo

02

Série

03

Número do CT\-e

09

Código Numérico

09

DV

01

O Dígito Verificador \(DV\) irá garantir a integridade da chave de acesso, protegendo\-a principalmente contra digitações erradas\.

<a id="_Hlk130821589"></a>RND100\-13

<a id="_Hlk130821576"></a>__Campo: TP\_CTe__

Informar neste campo o tipo do conhecimento de transporte eletrônico ou bilhete de passageiro eletrônico se: 

Tabela: SAFX07

Alteração __CH72944__ à o campo passou a ser preenchido tanto p/notas de emissão própria como terceiros;

Alteração __MFS8937:__

   Se Campo “Movimento Entrada/Saída” <> 1, e

   Se Modelo de Documento = “63” e campo Situação Especial” = F gravar “3”,

   Senão gravar “0”\.

          Se Modelo de Documento = “57”, “67” e

                  Se campo “situação especial” = 5 gravar “1”, ou

                          Se campo “situação especial” = B gravar “2”, ou

                                  Se campo “situação especial” = C gravar “3”, ou

                                       Se campo “situação especial” <> 5, B ou C, gravar “0”,

__               \[MFS693897\]__  Se campo “situação especial” = G , gravar “5”, ou

	                              Se campo “situação especial” = H , gravar “6”\. Ou

                                                Se campo “situação especial” = nulo ou espaços gravar “0”, ou

		                        Se campo “situação especial” <> 5, B, C, G, H,  gravar “0”\.

<a id="_Hlk130886159"></a>RND100\-14

__Campo: __<a id="_Hlk130886174"></a>__CHV\_CTE\_REF  __

__\[MFS 523869\]__ Informar a Chave do Bilhete de Passagem Eletrônico substituído 

__\[MFS683935\]__ Informar a Chave para CT\-e

__\[MFS693897\]__ Inclusão do ajuste \(Se o campo 13 \(<a id="_Hlk181095289"></a>__TP\_CTe__\) estiver preenchido com  “3” ou “6”\) 

Se Modelo de Documento = “63” e Situação Especial = “F” 

     Modelo de Docuemnto = “57” ou “67” e “situação especial” = “C” ou

     Modelo de Docuemnto = “57” ou “67” e “situação especial” = “H”

         Preencher com o campo Chave de Acesso da NFe Substituída \(301\- 

        NUM\_AUTENTIC\_NFE\_SUBST da SAFX07\)\.

Senão, campo não deve ser preenchido\.

Se o Modelo de Documento = “57”

     Preencher com o campo Chave de Acesso da NFe Substituída \(301\- NUM\_AUTENTIC\_NFE\_SUBST da SAFX07\)

RND100\-15

__Campo: VL\_DOC__

Para as notas de entrada:  será o valor total da nota mais o desconto, ou seja:

Notas sem item à campo 23 \(Valor Total\)  \+  campo 28  \(Desconto\) da SAFX07

Notas com item à total = campo 64 \(Valor Contábil\)  \+  campo 29 \(Desconto\) dos itens da SAFX08

Para as notas de saída: será o valor total da nota mais o desconto, considerando que no caso dos conhecimentos \(modelos 08, 8B, 09, 10, 11 e 57\), o valor deverá ser obtido sempre da SAFX07, exceto no caso dos documentos de modelo 08 e classificação fiscal = ‘1’ \(ver obs \(\*\)\):

Se Modelo de Documento = 07 \(notas fiscais\) ou Modelo de Documento = 08 com Classificação Fiscal = ‘1’ \(\*\):

      Idem ao procedimento feito para as notas de entrada;

Se Modelo de Documento = 08, 8B, 09, 10, 11 ou 57 \(conhecimentos\) \(\*\*\):

      Utilizar sempre o valor da capa \(campo 23 \- Valor Total \+  28 \- Desconto da SAFX07\)

\(\*\) alteração de regra feita no chamado 68490\-DHL \(ver observação na RND100 sobre este chamado\)

\(\*\*\) neste caso os documentos de modelo 08 serão os de classificação = ‘4’

RND100\-16

__Campo: VL\_DESC__

Para as notas de entrada:  valor do desconto da nota:

Notas sem item à campo “28 – Desconto” da SAFX07

Notas com item à total do campo “29 – Desconto” dos itens da SAFX08

Para as notas de saída: valor do desconto da nota, considerando que no caso dos conhecimentos \(modelos 08, 8B, 09, 10, 11 e 57\), o valor deverá ser obtido sempre da SAFX07, exceto no caso dos documentos de modelo 08 e classificação fiscal = ‘1’ \(ver obs \(\*\)\):

Se Modelo de Documento = 07 \(notas fiscais\) ou Modelo de Documento = 08 com Classificação Fiscal = ‘1’ \(\*\):

     Idem ao procedimento feito para as notas de entrada;

Se Modelo de Documento = 08, 8B, 09, 10, 11 e 57 \(conhecimentos\):  \(\*\*\)

      Utilizar sempre o valor da capa \(campo 28 – Desconto da SAFX07\)

\(\*\) alteração de regra feita no chamado 68490\-DHL \(ver observação na RND100 sobre este chamado\)

\(\*\*\) neste caso os documentos de modelo 08 serão os de classificação = ‘4’

<a id="_Hlk130819348"></a>RND100\-17

<a id="_Hlk130819334"></a>__Campo: IND\_FRT__

\[Alteração – OS3516\]

Se a data fiscal do documento for menor que 01/07/2012, gravar o Indicador do Tipo de Frete \(campo “72\-Indicador do Tipo do Frete” da SAFX07\): 

Se campo “situação especial” = 5 \(Campo: 125/SAFX07\), gravar = “9”,

     Se campo “situação especial” <> 5 \(Campo: 125/SAFX07\), e

            Se campo “Indicador do Tipo de Frete” = 0 gravar “0”; ou

                  Se campo “Indicador do Tipo de Frete” = 1 gravar “1”; ou

                         Se campo “Indicador do Tipo de Frete” = 2 gravar “2”; ou

                                   Se campo “Indicador do Tipo de Frete” = nulo/espaço gravar “9”;

Se a data fiscal do documento for maior ou igual á 01/07/2012, gravar o Indicador do Tipo de Frete \(campo “72\-Indicador do Tipo do Frete” da SAFX07\): 

Se campo “situação especial” = 5 \(Campo: 125/SAFX07\), gravar = “9”,

     Se campo “situação especial” <> 5 \(Campo: 125/SAFX07\), e

            Se campo “Indicador do Tipo de Frete” = 0 gravar “2”; ou

                  Se campo “Indicador do Tipo de Frete” = 1 gravar “0”; ou

                         Se campo “Indicador do Tipo de Frete” = 2 gravar “1”; ou

                                   Se campo “Indicador do Tipo de Frete” = nulo/espaço gravar “9”;

__\[MFS 523869\]__ Se o campo Modelo de Documento = 63 \(SAFX07\), campo não deve ser preenchido\.

RND100\-18

__Campo: VL\_SERV__

Para as notas de entrada:  será o valor total da nota, ou seja:

Notas sem item à campo 23 \- Valor Total da SAFX07

Notas com item à somatório do campo 64 \(Valor Contábil dos itens\) da SAFX08

Para as notas de saída: será o valor total da nota, considerando que no caso dos conhecimentos \(modelos 08, 8B, 09, 10, 11 e 57\), o valor deverá ser obtido sempre da SAFX07, exceto no caso dos documentos de modelo 08 e classificação fiscal = ‘1’ \(ver obs \(\*\)\):

Se Modelo de Documento = 07 \(notas fiscais\) ou Modelo de Documento = 08 com Classificação Fiscal = ‘1’ \(\*\):

     Idem ao procedimento feito para as notas de entrada;

Se Modelo de Documento: 08, 8B, 09, 10, 11 ou 57 \(conhecimentos\):   \(\*\*\)

      Utilizar sempre o valor da capa \(campo 23 \- Valor Total  da  SAFX07\)

__\[MFS693897\]__ Quando modelo nota 57 e situtuação especial = “G” ou “H” o valor do campo VL\_SERV do registro D100 deve ser igual ao valor do campo 13 VL\_FRT do regsitro D130

Como no registro do D100 utiliza a informação da tabela SAFX07 e no registro D130 utiliza a tabela SAFX50\. 

Realizar uma validação do conteúdo da informação que está neste registro com o comatório do campo do Registro D130, para a Situação do Cte Simplificado no documento de Saída e exibir mensagem de inconsitência na validação, se for o caso:

Mensagem “O valor do Campo VL\_SERV do registro D100 não corresponde ao somatório do valor do campo VL\_FRT do registro D130”

\(\*\) alteração de regra feita no chamado 68490\-DHL \(ver observação na RND100 sobre este chamado\)

\(\*\*\) neste caso os documentos de modelo 08 serão os de classificação = ‘4’

__RND100\-19__

__Campo: VL\_BC\_ICMS__

__Notas de entrada:__

Para as notas sem itens à o campo deve ser preenchido com o valor da base de cálculo do ICMS da SAFX07 \(campo 51\-Base ICMS\);

Para as notas com itens à neste caso deve\-se totalizar o __valor Base ICMS  __de todos os itens do documento em que o campo “56\-Base ICMS” da SAFX08 esteja com o código de tributação  igual a “1” operação tributada \(campo 55 da SAFX08\);

__Notas de saída:__

Se Modelo de Documento = 07 \(notas fiscais\) ou Modelo de Documento = 08 com Classificação Fiscal = ‘1’ \(\*\)

      Idem procedimento feito para as notas de entrada;

Se Modelo de Documento: 08, 8B, 09, 10, 11, ou 57 \(conhecimentos\):   \(\*\*\)

       Utilizar sempre o valor da capa \(campo 51\-Base ICMS da SAFX07\);

\(\*\) alteração de regra feita no chamado 68490\-DHL \(ver observação na RND100 sobre este chamado\)

\(\*\*\) neste caso os documentos de modelo 08 serão os de classificação = ‘4’

\[Alteração – OS 3227\]

Apresentar o valor zero \(0,00\) se o documento fiscal for extemporâneo de saída, ou seja, campo 03 da SAFX07 = ‘9’ para o documento que o campo COD\_SIT do registro D100 = ‘01’\.

\[Alteração – OS3526\-B\]

Para os documentos com o campo 125 da SAFX07 \(IND\_SITUACAO\_ESP\) = “D”, e CFOP’s  “1922, 2922, 3922, 1117, 2117, 3117, 5922, 6922, 7922, 5116, 6116 ou 7116” \(campos 14 da SAFX07, 22 da SAFX08 ou 17 da SAFX09 – COD\_CFOP\)\.

O sistema deve considerar a seguinte parametrização para a geração deste campo:

__Módulo__: SPED à EFD – Escrituração Fiscal Digital 

__Menu__: Parâmetros à Dados Iniciais

__Parâmetro:__ “Situação Especial 08 – Faturamento Simples”

Se a opção ICMS estiver desmarcada, apresentar o valor \(0,00\) neste campo\.

Se estiver marcada, apresentar o valor normalmente\.

__RND100\-20__

__Campo: VL\_ICMS__

__Notas de entrada:__

Para as notas sem itens à o campo deve ser preenchido com o valor do ICMS da SAFX07 \(campo 35\-Valor ICMS\);

Para as notas com itens à neste caso deve\-se totalizar o __valor do ICMS__ de todos os itens do documento em que o campo “43\- Valor ICMS” da SAFX08, esteja com o código de tributação  igual a “1” operação tributada \(campo 55 da SAFX08\);

Regra revista no chamado 70637\-Set/2009, onde foi retirada a condição de só carregar o valor do ICMS se existisse valor de BC, o que ocasionava problema nas notas complementares\. Além disso, devemos seguir as mesmas regras de escrituração dos livros fiscais\.

Para as notas com itens à neste caso deve\-se totalizar o __valor do ICMS__ de todos os itens do documento \(campo “43\- Valor ICMS”\);

__Notas de saída:__

Se Modelo de Documento = 07 \(notas fiscais\) ou Modelo de Documento = 08 com Classificação Fiscal = ‘1’ \(\*\):

      Idem procedimento feito para as notas de entrada;

Se Modelo de Documento: 08, 8B, 09, 10, 11 ou 57 \(conhecimentos\):   \(\*\*\)

       Utilizar sempre o valor da capa \(campo 35\-Valor ICMS da SAFX07\);

\(\*\) alteração de regra feita no chamado 68490\-DHL \(ver observação na RND100 sobre este chamado\)

\(\*\*\) neste caso os documentos de modelo 08 serão os de classificação = ‘4’

\[Alteração – OS 3227\]

Apresentar o valor zero \(0,00\) se o documento fiscal for extemporâneo de saída, ou seja, campo 03 da SAFX07 = ‘9’ para os documento que o campo COD\_SIT do registro D100 = ‘01’\.

\[Alteração – OS3526\-B\]

Para os documentos com o campo 125 da SAFX07 \(IND\_SITUACAO\_ESP\) = “D”,  e CFOP’s  “1922, 2922, 3922, 1117, 2117, 3117, 5922, 6922, 7922, 5116, 6116 ou 7116” \(campos 14 da SAFX07, 22 da SAFX08 ou 17 da SAFX09 – COD\_CFOP\)\.

O sistema deve considerar a seguinte parametrização para a geração deste campo:

__Módulo__: SPED à EFD – Escrituração Fiscal Digital 

__Menu__: Parâmetros à Dados Iniciais

__Parâmetro:__ “Situação Especial 08 – Faturamento Simples”

Se a opção ICMS estiver desmarcada, apresentar o valor \(0,00\) neste campo\.

Se estiver marcada, apresentar o valor normalmente\.

__RND100\-21__

__Campo: VL\_NT__

__Notas de entrada:__

Para as notas *sem* itens à o campo deve ser preenchido com o valor da Base ICMS Isenta \(campo 52\) \+ Base ICMS Outras \(campo 53\) \+ Base Redução ICMS \(campo 54\) da SAFX07;

Para as notas *com *itens à neste caso deve\-se totalizar o __valor Base ICMS  __de todos os itens do documento se o campo “56\-Base ICMS” da SAFX08 estiver com o código de tributação  igual a “2” ou “3” \(campo 55 da SAFX08\) e somar com __valor Base Redução ICMS__ \(campo 57 da SAFX08\)\.

__Notas de saída:__

Se Modelo de Documento = 07 \(notas fiscais\) ou Modelo de Documento = 08 com Classificação Fiscal = ‘1’ \(\*\):

      Idem procedimento feito para as notas de entrada;

Se Modelo de Documento: 08, 8B, 09, 10, 11 ou 57 \(conhecimentos\):   \(\*\*\)

       Utilizar sempre os valores da capa \(campo 52 \+ campo 53 \+ campo 54 da SAFX07\);

\(\*\) alteração de regra feita no chamado 68490\-DHL \(ver observação na RND100 sobre este chamado\)

\(\*\*\) neste caso os documentos de modelo 08 serão os de classificação = ‘4’

__RND100\-22__

Campo COD\_INF

Recuperar a informação do campo 178 – Código da Observação da SAFX07\.

\[__ALTERAÇÃO \- MFS60545__\] Tratamento para considerar o parâmetro – “Campo Código de Observação \(Considerar 6 caracteres\)” \- para truncar o campo com 6 posições, conforme Manual Guia Prático\.

__SE__ o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

__OU__

__SE__ o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

Este código deverá ser referenciado no registro 0450\.

__RND100\-23__

__RND100\-24__

Campo COD\_MUN\_ORIG

__Para período de geração até 31/12/2021:__

Concatenação do Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código  do município de origem da prestação do serviço \(para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\)\.

__\[ALTERAÇÃO – MFS73695\]__ Tratamento para obrigar o preenchimento do campo, a partir de Janeiro de 2022, de acordo com a orientação da versão de layout 1\.15:

__Para período de geração a partir de 01/01/2022:__

__Notas de saída: __

Para todos os modelos informados, o preenchimento do campo deve ser obrigatório\.

__SE__ o campo não estiver preenchido, o registro deverá ser gravado normalmente e no log deve ser gravada a seguinte mensagem de aviso:

  

Ver planilha de erros “Sped\_Fiscal\_Log\_Erros, mensagem de erro número __372__\.

__\[MFS693897\]__ No caso de Notas do modelo nota 57 e situação especial = “G” \(CT\-e Simplificado\) ou “H” \(Substituição CT\-e Simplificado\), preencher o campo com o código “9999998”\.

OBS: No Sped Fiscal 2025 foi inclusa na regra também o tratamento para preenchimento de código do Exterior “9999999”\. Foi verificado que este tratamento já existe para este campo quando identificado por “EX” através da Regra RND100\-FRT\.

__RND100\-25__

Campo COD\_MUN\_DEST

__Para período de geração até 31/12/2021:__

Concatenação do Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código  do município de origem da prestação do serviço \(para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\)\.

__\[ALTERAÇÃO – MFS73695\]__ Tratamento para obrigar o preenchimento do campo, a partir de Janeiro de 2022, de acordo com a orientação da versão de layout 1\.15:

__Para período de geração a partir de 01/01/2022:__

__Notas de saída: __

Para todos os modelos informados, o preenchimento do campo deve ser obrigatório\.

__SE__ o campo não estiver preenchido, o registro deverá ser gravado normalmente e no log deve ser gravada a seguinte mensagem de aviso:

  

Ver planilha de erros “Sped\_Fiscal\_Log\_Erros, mensagem de erro número __372__

__\[MFS983144\]__ Para atendimento a alteração do Guia Prático 3\.2\.1, que retira o código “9999998” de uso para o campo 25 \(Município Destino\) necessário retirar esta excessão, e informar para o modelo de nota 57 e situação especial “G” ou “H” a UF do estabelecimento, conforme regra do campo\.

__\[MFS693897\]__ No caso de Notas do modelo nota 57 e situação especial = “G” \(CT\-e Simplificado\) ou “H” \(Substituição CT\-e Simplificado\), preencher o campo com o código “<a id="_Hlk215152948"></a>9999998”\.

__OBS:__ No Sped Fiscal 2025 foi inclusa na regra também o tratamento para preenchimento de código do Exterior “9999999”\. Foi verificado que este tratamento já existe para este campo quando identificado por “EX”__ __através da Regra RND100\-FRT\.

__Registro D101 – Informação Complementar dos Documentos Fiscais – Prestações Interestaduais Destinadas a Consumidor Final Não Contribuinte EC 87/15 \(Códigos 57, 63 e 67\)__

__RND101__

Este registro é “filho” do D100, e será gerado para todos os documentos gravados no D100, nas seguintes condições:

 

Alteração __MFS8937:__

Somente devem ser gravados os documentos com modelos correspondentes aos seguintes códigos da tabela “4\.1\.1\-Tabela de Documentos Fiscais do ICMS” do Sped Fiscal:  

57 – Conhecimento de Transporte Eletrônico \(CT\-e\);

63 – Bilhete de Passagem Eletrônico;

67 – Conhecimento de Transporte Eletrônico para Outros Serviços \(CT\-e OS\)\.

E que tenham informações em algum dos seguintes campos:

\- Valor FCP UF Destino

\- Valor ICMS UF Destino

\- Valor ICMS UF Origem

Para cada documento do D100 será gravado um único registro D101, da seguinte forma:

Notas com itens à  os valores a serem gerados serão a totalização dos campos dos itens \(SAFX08, campos 221, 222 e 223\);

Notas sem itens à  os valores a serem gerados serão os campos da capa \(SAFX07, campos 283, 284 e 285\);

__Registro D110 – Itens do Documento \- NF Serviço de Transporte \(Código: 07\) __

RND110

Este registro deve ser apresentado para os documentos selecionados no D100 com as seguintes regras:

Tabela: SAFX07,

         Movimento Entrada/Saída = “9”,

                  Modelo de Documento = “07”\.

Para cada ítem existente na SAFX08 deve\-se gravar um registro D110\.

RND110\-03

Campo: COD\_ITEM

Gravar o código do produto \(SAFX2013\),  a partir das informações obtidas nos campos 13 e 14 \(produto\) da SAFX08\.

Aplicar a mesma regra de concatenação já definida no registro 0200\. 

__Registro D120 – Complemento da NF Serviço de Transporte \(Código: 07\) __

RND120

Este registro é filho do registro D110, deve ser apresentado um registro D120  para cada documento selecionado no D110 com as seguintes regras:

Tabela: SAFX07,

         Movimento Entrada/Saída = “9”,

                  Modelo de Documento = “07”\.

 Este registro deve ser apresentado para informar o complemento das Notas Fiscais de Serviço de Transporte com as informações de origem, destino e identificação do veículo\. 

As informações deste registro são provenientes das tabelas SAFX07, SAFX50 e SAFX2049\.

RND120\-04

Campo: VEIC\_ID

A placa do veículo poderá ser obtida na SAFX50, ou na SAFX2049, da seguinte forma:

__Se__ existir registro na SAFX50,

      __Se__ a placa do veículo estiver preenchida \(campo 23\-Placa do Veículo\),

             gravar o campo VEIC\_ID com a informação do campo 23\-Placa do Veículo

      __Senão__

              __Se__ o código do veículo estiver preenchido \(campo 45\-Cód do Veículo\),

                    acessar o cadastro do veículo na SAFX2049 e obter a placa do veículo

                     \(campo 09\-Identificação do Veículo\) p/preencher o campo VEIC\_ID\.

              __Senão__

                     o campo VEIC\_ID não será preenchido\.

RND120\-05

Campo: UF\_ID

A sigla da UF da placa do veículo poderá ser obtida na SAFX50, ou na SAFX2049, da seguinte forma:

__Se__ existir registro na SAFX50,

      __Se__ a UF da placa do veículo estiver preenchida \(campo 36\- UF da Placa do Veículo\),

             gravar o campo UF\_ID com a informação do campo 36\.

      __Senão__

              __Se__ o código do veículo estiver preenchido \(campo 45\-Cód do Veículo\)

                    acessar o cadastro do veículo na SAFX2049 e obter a UF da placa do veículo

                     \(campo 10\-UF da Identificação do Veículo\) p/preencher o campo UF\_ID\.

              __Senão__

                     o campo UF\_ID não será preenchido\.

__Registro D130 – Complemento do Conhecimento Rodov\. de Carga \(Cód 08, 8B e 57 \(Cte Simplificado\)\) __

RND130

Este registro é filho do registro D100, deve ser apresentado um registro D130  para cada documento selecionado no D100 com as seguintes regras:

Tabela: SAFX07,

         Movimento Entrada/Saída = “9”,

                  Modelo de Documento = “08”, “8B” e “57”

                       Para o modelo “57” filtrar apenas os documentos com situação especial “G” \(CT\-e Simplificado\) ou “H” \(Substituição CT\-e Simplificado\)      

As informações deste registro são provenientes das tabelas SAFX07, SAFX50 e SAFX2049\.

RND130\-02

Campo COD\_PART\_CONSG

\[OS4747\] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

RND130\-03

Campo COD\_PART\_RED

\[OS4747\] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

RND130\-04

Campo: IND\_FRETE\_RED

Se não existir pessoa fis/jur redespachante \(campo; 44/SAFX50\), consequentemente o “campo 03\-COD\_PART\_RED” do registro D130 estará com ||\.

      Então gravar “0” ;

Se modalidade de frete \(campo “Modalidade Frete Redespacho” da SAFX50\) = “1” 

      Gravar “1”; 

Se modalidade de frete \(campo “Modalidade Frete Redespacho”  da SAFX50\) = “2” 

      Gravar “2”;

Se modalidade de frete \(campo “Modalidade Frete Redespacho”  da SAFX50\) = “3”

      Gravar “9”;

 

Se existir pessoa fis/jur redespachante \(campo; 44/SAFX50\),

       Se modalidade de frete \(campo “Modalidade Frete Redespacho”  da SAFX50\) não estiver preenchido gravar nulo\.

Origem da Informação: Campo 75 \(Modalidade de Frete Redespacho\)/ SAFX50

RND130\-07

__Campo: VEIC\_ID__

A placa do veículo poderá ser obtida na SAFX50 ou na SAFX2049 da seguinte forma:

__Se__ existir registro na SAFX50,

      __Se__ a placa do veículo estiver preenchida \(campo 23\-Placa do Veículo\),

             Gravar o campo VEIC\_ID com a informação do campo 23\-Placa do Veículo

      __Senão__

              __Se__ o código do veículo estiver preenchido \(campo 45\-Cód do Veículo/SAFX50\),

                    Acessar o cadastro do veículo na SAFX2049 e obter a placa do veículo

                     \(campo 09\-Identificação do Veículo\) p/preencher o campo VEIC\_ID\.

              __Senão__

                     o campo VEIC\_ID não será preenchido\.

RND130\-14

__Campo: UF\_ID__

A sigla da UF da placa do veículo poderá ser obtida na SAFX50 ou na SAFX2049 da seguinte forma:

__Se__ existir registro na SAFX50,

      __Se__ a UF da placa do veículo estiver preenchida \(campo 36\- UF da Placa do Veículo\),

             Gravar o campo UF\_ID com a informação do campo 36\.

      __Senão__

              __Se__ o código do veículo estiver preenchido \(campo 45\-Cód do Veículo\)

                    Acessar o cadastro do veículo na SAFX2049 e obter a UF da placa do veículo

                      \(campo 10\-UF da Identificação do Veículo\) p/preencher o campo UF\_ID\.

              __Senão__

                     o campo UF\_ID não será preenchido\.

__Registro D140 – Complemento do Conhecimento Aquav\. de Carga \(Código: 09\) __

RND140

Este registro é filho do registro D100, deve ser apresentado um registro D140  para cada documento selecionado no D100 com as seguintes regras:

Tabela: SAFX07,

         Movimento Entrada/Saída = “9”,

                  Modelo de Documento = “09”\.

As informações deste registro são provenientes das tabelas SAFX07, SAFX50 e SAFX2049\.

RND140\-02

Campo COD\_PART\_CONSG

\[OS4747\] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

RND140\-05

Campo: IND\_VEIC

Preencher com o campo “11\-Tipo de Veículo Aquaviário” da SAFX2049\. 

Obter o tipo de veículo aquaviário na SAFX2049, a partir do código do veículo de transporte preenchido no campo 45\-Código do Veículo da SAFX50\.

RND140\-06

Campo: VEIC\_ID

A identificação da embarcação poderá ser obtida na SAFX50 ou na SAFX2049 da seguinte forma:

__Se__ existir registro na SAFX50,

      __Se__ a identificação da embarcação estiver preenchida \(campo 23\-Placa do Veículo\),

             Gravar o campo VEIC\_ID com a informação do campo 23\.

      __Senão__

              __Se__ a identificação da embarcação estiver preenchida \(campo 45\-Cód do Veículo\),

                    Acessar o cadastro do veículo na SAFX2049 e obter a identificação da embarcação

                     \(campo 09\-Identificação do Veículo\) p/preencher o campo VEIC\_ID\.

              __Senão__

                     o campo VEIC\_ID não será preenchido\.

__Registro D150 – Complemento do Conhecimento Aéreo de Carga \(Código: 10\) __

RND150

Este registro é filho do registro D100, deve ser apresentado um registro D150  para cada documento selecionado no D100 com as seguintes regras:

Tabela: SAFX07,

         Movimento Entrada/Saída = “9”,

                  Modelo de Documento = “10”\.

As informações deste registro são provenientes das tabelas SAFX07, SAFX50 e SAFX2049\.

RND150\-04

Campo: VEIC\_ID

A identificação da aeronave \(DAC\) poderá ser obtida na SAFX50 ou na SAFX2049 da seguinte forma:

__Se__ existir registro na SAFX50,

      __Se__ a identificação da aeronave \(DAC\) estiver preenchida \(campo 23\-Placa do Veículo\),

             Gravar o campo VEIC\_ID com a informação do campo 23\.

      __Senão__

              __Se__ a identificação da aeronave \(DAC\) estiver preenchida \(campo 45\-Cód do Veículo\),

                    Acessar o cadastro do veículo na SAFX2049 e obter a identificação da aeronave

                     \(campo 09\-Identificação do Veículo\) p/preencher o campo VEIC\_ID\.

              __Senão__

                     o campo VEIC\_ID não será preenchido\.

__Registro D160 – Carga Transportada \(Código: 08, 8B, 09, 10, 11, 26 e 27\)__

RND160

Neste registro deve ser apresentadas informações sobre a carga transportada de cada conhecimento de transporte selecionado no registro D100 com modelos 08, 8B, 09, 10, 11, 26 ou 27\.

Este registro é filho do registro D100, deve ocorrer um  ou vários registros para cada documento selecionado no D100\.

Estes registros ficam na SAFX51 que contém as informações sobre a carga transportada \(número da nota, volume etc \.\.\.\)\.

__Se__  CFOP do conhecimento de transporte \(SAFX07\) = 5359 ou 6359\.

     NÃO GERAR ESTE REGISTRO\.\.\.                      

Levando em consideração que cada conhecimento de transporte só deve conter notas fiscais do mesmo remetente e mesmo destinatário, concluímos que este registro é o agrupamento de: 

- Nº DO DESPACHO,
- CNPJ DO REMETENTE,
- INSCRIÇÃO ESTADUAL DO REMETENTE,
- CÓDIGO DO MUNÍCIPIO DO REMETENTE,
- CNPJ DO DESTINATÁRIO\.
- INSCRIÇÃO ESTADUAL DO DESTINATÁRIO,
- CÓDIGO DO MUNÍCIPIO DO DESTINATÁRIO,

__ __

__Registro D161 – Local da Coleta e Entrega \(Código: 08, 8B, 09, 10, 11 e 26\)__

RND161

__Este registro somente deve ser informado quando o local de coleta e/ou entrega  for diferente do endereço do remetente e/ou destinatário\.__

Este registro é “filho” do D160\. 

Para cada registro D160, deverá ser gravado um registro D161 com as informações de coleta e entrega, se satisfazerem as regras em anexo\.

Os dados serão obtidos na tabela SAFX51\.

Regra de geração:

Se Modelo de Documento: 08, 8B, 09, 10,11 ou 26 e

__            __Se CNPJ/CPF Coleta > 0, e

                      Se CNPJ/CPF Coleta  <> CGC/CPF do remetente, ou 

                           __    __Se CNPJ/CPF Entrega > 0, e 

                                             CNPJ/CPF Entrega for <> CGC/CPF do destinatário,

                                                          Gerar o registro D161;

__OBS1:__ Se o campo coleta não estiver preenchido, consideraremos que  o CNPJ da coleta é igual ao CNPJ do remetente\.

__OBS2:__ Se o campo entrega não estiver preenchido, consideraremos que  o CNPJ da entrega é igual ao CNPJ do destinatário\.

 

Modelo de documento – campo 13 da SAFX07

CNPJ/CPF Coleta – campo novo da SAFX51

CNPJ/CPF Entrega \- campo novo da SAFX51

CGC/CPF do remetente  \- campo 17 da SAFX51 

CGC/CPF do destinatário – campo 25 da SAFX51

__OBS3: __No registro D161 só deve ser gravado valor no campo que atender a regra de geração acima, se não atender gravar ||\.

RND161\-02

Campo: IND\_CARGA

Através do campo “32\-Via de Transporte” da SAFX51, verificar qual a via de transporte na tabela SAFX2047 \(campo: 07 \- Código de Via de Transporte SP\), e realizar um de/para considerando os códigos aceitos no Sped Fiscal:

 

__Código da SAFX2047__

__Código a ser gravado no campo 02\-IND\_CARGA__

1  \(Rodoviário\)

0  \(Rodoviário\)

2  \(Ferroviário\)

1  \(Ferroviário\)

3  \(Rodo\-Ferroviário\)

9  \(Outros\)

2 \(Rodo\-Ferroviário\)

4  \(Aquaviário\)

2  \(Aquaviário\)

3  \(Aquaviário\)

5  \(Dutoviário\)

3  \(Dutoviário\)

4  \(Dutoviário\)

6  \(Aéreo\)

4  \(Aéreo\)

5  \(Aéreo\)

7  \(Outros\) 

9  \(Outros\)

Alteração OS2388\-E13 \(GP vrs 1\.0\.4 e AC 29/09\): incluída a opção “Rodo\-Ferroviário” nos tipos de transporte do campo IND\_CARGA\.

RND161\-03

Campo 05 \- Código do Município do local de coleta

Através do chamado CH103949 foi solicitado um tratamento de erro neste campo pois não está sendo gerado quando o local do destinatário é diferente da entrega\.	

Não existe regra de exceção para este campo, logo, ele deve ser gerado em todos registros D161 conforme está no Guia Prático do SPED FISCAL, independente do local do destinatário e entrega\.

RND161\-04

Campo 08 \- Código do Município do local de entrega

Através do chamado CH103949 foi solicitado um tratamento de erro neste campo pois não está sendo gerado quando o local da coleta é diferente do remetente\.

Não existe regra de exceção para este campo, logo, ele deve ser gerado em todos registros D161 conforme está no Guia Prático do SPED FISCAL, independente do local da coleta e do remetente\.

__Registro D162 – Identificação dos Documentos Fiscais \(Cód 08, 8B, 09, 10, 11, 26 e 27\)__

RND162

Neste registro deve ser apresentados dados das notas fiscais que acobertam a carga transportada, objeto dos conhecimentos de transporte selecionados no registro D160\.

Para cada conhecimento de transporte \(D100\) pode existir nenhum, um ou vários registros D162\.

__Regra de geração:__

Se Modelo de Documento \(SAFX07\) = 08, 8B, 09, 10, 11, 26 ou 27, e

__           Se__ CFOP do conhecimento de transporte \(SAFX07\) = 5359 ou 6359\.

                       NÃO GERAR ESTE REGISTRO\.\.\.   

Se CFOP do conhecimento de transporte \(SAFX07\) <> 5359 ou 6359\.

          Gerar registro D162\.                   

__Registro D170 –  Complemento do Conhecimento Multimodal de Cargas \(Código 26\)__

RND170

Neste registro deve ser apresentado o complemento do Conhecimento Multimodal de Cargas \(código 26\)\.

Esse registro é filho do registro D100, por isso, para cada conhecimento de transporte \(D100\) pode existir nenhum, ou apenas um registro D170\.

__Regra de geração:__

Tabela: SAFX07,

         Movimento Entrada/Saída = “9”,

                  Modelo de Documento = “26”\.

As informações deste registro são provenientes das tabelas SAFX07, SAFX50 e SAFX2049\.

RND170\-02

Campo COD\_PART\_CONSG

\[OS4747\] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

RND170\-03

Campo COD\_PART\_RED

\[OS4747\] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

RND170\-13

Campo: VEIC\_ID

A identificação da placa do veículo poderá ser obtida na SAFX50 ou na SAFX2049 da seguinte forma:

__Se__ existir registro na SAFX50,

      __Se__ a placa do veículo estiver preenchida \(campo 23\-Placa do Veículo\),

             Gravar o campo VEIC\_ID com a informação do campo 23\.

      __Senão__

              __Se__ a identificação do veículo estiver preenchida \(campo 45\-Cód do Veículo\),

                    Acessar o cadastro do veículo na SAFX2049 e obter a identificação do veículo

                     \(campo 09\-Identificação do Veículo\) p/preencher o campo VEIC\_ID\.

              __Senão__

                     o campo VEIC\_ID não será preenchido\.

RND170\-14

Campo: UF\_ID

A identificação da UF da placa do veículo poderá ser obtida na SAFX50 ou na SAFX2049 da seguinte forma:

__Se__ existir registro na SAFX50,

      __Se__ a UF da placa do veículo estiver preenchida \(campo 36\- Unidade da Federação da Placa do Veículo\),

             Gravar o campo UF\_ID com a informação do campo 36\.

      __Senão__

              __Se__ a identificação do veículo estiver preenchida \(campo 45\-Cód do Veículo\),

                    Acessar o cadastro do veículo na SAFX2049 e obter a identificação do veículo

                     \(campo 09\-Identificação do Veículo\) p/preencher o campo UF\_ID\.

              __Senão__

                     o campo UF\_ID não será preenchido\.

__Registro D180 –  Modais \(Código 26\)__

RND180

Neste registro deve ser identificar todos os transportadores e seus documentos fiscais emitidos durante o transporte multimodal\.

Esse registro é filho do registro D100, por isso, para cada conhecimento de transporte \(D100\) pode existir nenhum, um ou vários registros D180\.

__Regra de geração:__

Tabela: SAFX07,

         Movimento Entrada/Saída = “9”,

                  Modelo de Documento = “26”\.

As informações deste registro são provenientes das tabelas SAFX07 e SAFX155\. 

Obs: O registro apenas será gerado se houver cadastro referente ao documento fiscal de modelo 26 na tabela de Informações de Modais \(SAFX155\)

RND180\-03

Campo: IND\_EMIT

Verificar se o campo 04 \(CNPJ\_CPF\_EMIT\) do registro D180 é igual ao campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento que está gerando o SPED\.

Se for igual, preencher com: 0 – Emissão própria;

Se não, preencher com: 1 – Terceiros\.

__Registro D190–Registro Analítico dos Documentos \(Cód 07, 08, 8B, 09, 10, 11, 26, 27, 57, 63 e 67\) __

RND190

Este registro tem por objetivo informar os valores totalizados por CFOP, CST e Alíquota, de todos os documentos gravados no registro D100\.

Quando se tratar de um Conhecimento de Frete, os dados serão os próprios dados da SAFX07, já que estes documentos não têm itens na SAFX08, exceto no caso dos conhecimento com  modelo 08 e classificação fiscal = ‘1’ \(ver obs \(\*\)\)\.

Quando se tratar de notas fiscais os valores deverão ser totalizados dos itens da SAFX08, ou da própria SAFX07, quando se tratar de notas sem itens\.

\(\*\) alteração de regra feita no chamado 68490\-DHL \(ver observação na RND100 sobre este chamado\)

= = = = =

\[Alteração – OS 3227\]

Exceção para notas fiscais extemporâneas de Saída:

Não apresentar os valores de base, alíquota e ICMS dos documentos extemporâneos de saída, tendo em vista que não serão considerados para os livros P2, P2A e P9\.

Os campos ALIQ\_ICMS, VL\_BC\_ICMS, VL\_ICMS e VL\_RED\_BC devem apresentar o valor zero \(0,00\) se o documento fiscal for extemporâneo de saída, ou seja, campo 03 da SAFX07 = ‘9’ para os documento que o campo COD\_SIT do registro D100 = ‘01’\.

= = = = =

\[Alteração – OS3526\-B\]

Para os documentos com o campo 125 da SAFX07 \(IND\_SITUACAO\_ESP\) = “D”,

 e CFOP’s  “1922, 2922, 3922, 1117, 2117, 3117, 5922, 6922, 7922, 5116, 6116 ou 7116” \(campos 14 da SAFX07, 22 da SAFX08 ou 17 da SAFX09 – COD\_CFOP\)\.

O sistema deve considerar a seguinte parametrização para a geração do D190:

__Módulo__: SPED à EFD – Escrituração Fiscal Digital 

__Menu__: Parâmetros à Dados Iniciais

__Parâmetro:__ “Situação Especial 08 – Faturamento Simples”

Se a opção ICMS estiver desmarcada, os campos ALIQ\_ICMS, VL\_BC\_ICMS, VL\_ICMS e VL\_RED\_BC devem apresentar o valor zero \(0,00\), tendo em vista que não serão considerados para os livros P1, P1A, P2, P2A e P9\.

Se estiver marcada, apresentar os valores normalmente\.

= = = = =

A totalização dos valores deverá ser feita por:

__CST\_ICMS__ \- Código de Situação Tributária do ICMS     

__CFOP__  \-  Código Fiscal de Operação                               

__ALIQ\_ICMS__ \- Alíquota ICMS                                            

 

__Valores do D190:__

__Totalização pelo item \(SAFX08\)__

__Totalização pela capa \(SAFX07\)__

CST\_ICMS

Concatenação dos códigos das tabelas de situação estadual  "A" e "B" \(código A \+ código B\)\. Campos 30 e 31\.

Concatenação dos códigos das tabelas de situação estadual  "A" e "B" \(código A \+ código B\)\. Campos 179 e 180\.

CFOP

Campo 22

Campo 14

ALIQ\_ICMS

Campo 42 quando o código de tributação  for igual a “1” \(campo 55\)\.

Utilizar o campo 42, de acordo com a seguinte lógica:

Se Base de Cálculo  __e__  ICMS = 0 

     Considerar alíquota = 0;

Senão 

     Considerar a alíquota do item;

Regra revista no chamado 70637 em Set/2009, para seguir as regras de escrituração dos livros fiscais\.

__Extração dos Dados:__

__Tabela:__ DWT\_ITENS\_MERC

__Campo: __ ALIQ\_TRIBUTO\_ICMS

Campo 34, de acordo com a seguinte lógica:

Se Base de Cálculo __e__ ICMS = 0 

     Considerar alíquota = 0;

Senão 

     Considerar a alíquota da capa;

Regra revista no chamado 70637 em Set/2009, para seguir as regras de escrituração dos livros fiscais\.

__Extração dos Dados:__

__Tabela:__ DWT\_DOCTO\_FISCAL

__Campo: __ ALIQ\_TRIBUTO\_ICMS

VL\_OPR

Totalização do campo 64

__Extração dos Dados:__

__Tabela:__ DWT\_ITENS\_MERC, __Campo: __ VLR\_CONTAB\_ITEM

Campo 23 

__Extração dos Dados:__

__Tabela:__ DWT\_DOCTO\_FISCAL

__Campo: __ VLR\_TOT\_NOTA

VL\_BC\_ICMS

Totalização do campo 56 \(Base ICMS\) quando o código de tributação  for igual a “1” \(campo 55\)\.

__Extração dos Dados:__

__Tabela:__ DWT\_ITENS\_MERC, __Campo: __ VLR\_BASE\_ICMS\_1

Campo 51

__Extração dos Dados:__

__Tabela:__ DWT\_DOCTO\_FISCAL

__Campo: __ VLR\_BASE\_ICMS\_1

VL\_ICMS

Totalização do campo 43 \(Valor ICMS\) quando o código de tributação  for igual a “1” \(campo 55\)\.

Totalização do campo 43 \(Valor ICMS\)\.

Regra revista no chamado 70637 em Set/2009, onde foi retirada a condição de só carregar o valor do ICMS se existisse valor de BC, o que ocasionava problema nas notas complementares\. Além disso, devemos seguir as mesmas regras de escrituração dos livros fiscais\.

__Extração dos Dados:__

__Tabela:__ DWT\_ITENS\_MERC, __Campo: __ VLR\_TRIBUTO\_ICMS

Campo 35

__Extração dos Dados:__

__Tabela:__ DWT\_DOCTO\_FISCAL

__Campo: __ VLR\_TRIBUTO\_ICMS

VL\_RED\_BC

Totalização do campo 57  \(Base Redução ICMS\)\.

__Extração dos Dados:__

__Tabela:__ DWT\_ITENS\_MERC, __Campo:__ VLR\_BASE\_ICMS\_4

Campo 54

__Extração dos Dados:__

__Tabela:__ DWT\_DOCTO\_FISCAL

__Campo: __ VLR\_BASE\_ICMS\_4

COD\_OBS

Campo COD\_OBS

Recuperar a informação do campo 155 – Código da Observação da SAFX08\.

Estabelecidos em SC o campo não será preenchido\.

\[__ALTERAÇÃO \- MFS69058__\] Tratamento para considerar o parâmetro – “Campo Código de Observação \(Considerar 6 caracteres\)” \- para truncar o campo com 6 posições, conforme Manual Guia Prático\.

__SE__ o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

__OU__

__SE__ o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

Este código deverá ser referenciado no registro 0460\.

Não se aplica

OBS1: Regra do PVA \(Programa Validador e Assinador\)

Tolerância entre valores calculados divergentes

Nas regras de validação que comparem valores produzidos por operações aritméticas calculadas pelo sistema com valores informados pelo contribuinte, as seguintes considerações deverão ser acatadas:

- Para regras que gerem ERRO  
  
Será permitida uma tolerância de discordância de valores nas duas últimas casas decimais do valor informado\.  

- Para regras que gerem ADVERTÊNCIA  
  
Deverão ter seus valores truncados após a realização da operação, não sendo permitida nenhuma discordância entre o valor informado e o calculado pelo sistema\. 

__OBS2__: A __VAF\-MG__ a partir de 2020 passou a ser gerada com base nas regras de vários registros do SPED FISCAL \(C190, D190\.\.\.\)\. Ao realizar uma alteração na regra de geração dos registros D100 e D190, como inclusão de um modelo, um critério de recuperação da nota, um tratamento de situação especial, a regra de geração da VAF\-MG deve ser revista \(tópico 2 do MTZ\-VAFMG\_Geracao\_Relatorio\_EFD\-Fiscal\.docx\)\.

RND190\-09

Campo COD\_OBS:

__\[ALTERADA \- MFS\-18252/ CH24606\_2018 \(MFS\-21413\)\]__

Quando a UF do estabelecimento <> ‘SC’:

__Para notas de entrada__ à Recuperar a informação do campo 155 – Código da Observação da SAFX08, considerando o primeiro registro lido da combinação de itens selecionados nos critérios de agrupamento do registro\.

Quando a UF do estabelecimento <> ‘SC’:

__Para notas de saída__ à não gerar a informação\. Recuperar a informação do campo 155 – Código da Observação da SAFX08, considerando o primeiro registro lido da combinação de itens selecionados nos critérios de agrupamento do registro\.

Este código deverá ser referenciado no registro 0460\.

__Registro D195 – Observações do Lançamento Fiscal __

RND195

Gravar um registro D195 para cada código de observação do lançamento fiscal existente para a nota fiscal gravada no D100\. Este registro deve ser gerado apenas quando a nota estiver gravada no D100\.

Estas observações ficam registradas na nova tabela SAFX112 \(“Observações da Nota Fiscal”\), e são as linhas com indicador = __“L”__ \(coluna IND\_ICOMPL\_LANCTO\)\.

Poderão existir “n” observações para uma mesma nota fiscal\.  

Registro deve ser gerado apenas a partir da versão EFD105 do leiaute \(Julho/2012\)

RND195\-02

__Campo: COD\_OBS__

Recuperar a informação do campo 155 – Código da Observação da SAFX08\.

\[__ALTERAÇÃO \- MFS69058__\] Tratamento para considerar o parâmetro – “Campo Código de Observação \(Considerar 6 caracteres\)” \- para truncar o campo com 6 posições, conforme Manual Guia Prático\.

__SE__ o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

__OU__

__SE__ o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

Este código deverá ser referenciado no registro 0460\.

__Registro D197 – Outras Obrigações Tributárias , Ajustes e Informações \.\.\.\.__

RND197

Neste registro devem constar os ajustes/outros valores vinculados à observação do lançamento fiscal gravada no registro D__195__\.

Estes dados devem ser obtidos na nova tabela SAFX113 – Ajustes / Outros Valores do Lançamento Fiscal, e poderão existir “n” ajustes vinculados a uma mesma observação\. 

__Regra criada p/ resolver problema de duplicidade de chave \(OS2388\-E10, Abr/2009\)__:

Quando para uma mesma observação, existir mais de um ajuste de *mesmo código de ajuste , mesmo produto *\(vide OBS abaixo\) *e mesma alíquota*, os valores devem ser totalizados para gerar um único D197\. Isso é possível quando na nota existirem dois itens de mesmo produto, para os quais existam ajustes de mesmo código\.  A possibilidade existe, já que a SAFX113 foi criada com o número do item da nota, e não com o produto\.

__Obs__: a alíquota foi incluída como fator de quebra apenas para alertar o usuário sobre a utilização de alíquotas diferentes para um mesmo código de ajuste\. Se ocorrer esta situação, gravaremos as linhas separadamente para possibilitar que o usuário verifique se é um erro na base de dados\. Analisando o layout do Sped, nestes casos a alíquota deveria ser a mesma\.

__OBS __\(alteração do chamado __5218/2014__\) àNo caso do D197 esta regra de consolidação não deve considerar o produto/item da SAFX113, uma vez que esta informação não é utilizada neste registro, como descrito na __RND197\-04__\.

Registro deve ser gerado apenas a partir da versão EFD105 do leiaute \(Julho/2012\)

RND197\-03

Campo DESCR\_COMPL\_AJ:

Será a descrição complementar da nova tabela SAFX113\. 

RND197\-04

Campo COD\_ITEM:

Gerar fixo nulo\.

# REGISTRO D300 \-  REGISTRO ANALÍTICO DOS BILHETES CONSOLIDADOS DE:

__BILHETES DE PASSAGEM RODOVIÁRIO \(CÓDIGO 13\),__

__BILHETES DE PASSAGEM AQUAVIÁRIO \(CÓDIGO 14\), __

__BILHETES DE PASSAGEM E NOTA DE BAGAGEM \(CÓDIGO 15\) e__

__BILHETES DE PASSAGEM FERROVIÁRIO \(CÓDIGO 16\)\.__

	

RND300

O registro D300 é um agrupamento diário dos bilhetes de passagem armazenados no DW com as  seguintes condições:

Tabela: SAFX07

__CONDIÇÃO 1:__

Se movimento entrada/saída = 9,

         Se classificação do documento fiscal = 1 ou 3,	

                      Se modelo de documento = 13, 14, 15 ou 16\.

Deve ser gerado um ou vários registros D300 para o período selecionado \(registro 0000 \- campo 04 e campo 05\) a partir do __agrupamento 1:__

Agrupamento 1 à è o agrupamento diário dos bilhetes em ordem crescente atendido na condição 1 descrita neste documento, a quebra do registro ocorrerá cada vez que diferenciar um ítem do agrupamento\.

__AGRUPAMENTO 1__

Data de Emissão,

Modelo de Documento__,__

Série do Documento Fiscal__,__

Subsérie do Documento Fiscal__,__

Concatena: Código Situação Tributária “A”/ Código Situação Tributária “B”__,__

Código Fiscal__,__

Alíquota ICMS__,__

Conta Contábil__,__

Não trataremos o campo COD\_OBS do registro D300 neste documento\.

A identificação dos códigos para preenchimento do campo 02 do registro D300 deve ser feita pelo campo “13 – Modelo de Documento” da SAFX07\.

__Descrição do Campo:__

__Nº do Campo:__

__Nome do Campo no MasterSAF:__

__Nome do Campo no Registro D300:__

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

Situação da Nota

30

SITUACAO

Data de Emissão

11

DATA\_EMISSAO

DT\_DOC

Série do Documento Fiscal

09

SERIE\_DOCFIS

SER

Subsérie do Documento Fiscal

10

SUB\_SERIE\_DOCFIS

SUB

Código Situação Tributária “A”/ Código Situação Tributária “B”

179/180

__Concatenar:__ COD\_SITUACAO\_A  \+  COD\_SITUACAO\_B

CST\_ICMS

Código Fiscal

14

COD\_CFO

CFOP

Conta Contábil

33

COD\_CONTA

COD\_CTA

Alíquota ICMS

34

VLR\_ALIQ\_ICMS

ALIQ\_ICMS

__Observação sobre as notas extemporâneas:__

Os bilhetes com datas extemporâneas serão tratadas normalmente, exatamente da mesma forma como é feito na versão atual do Mastersaf, ou seja, a nota extemporânea é lançada normalmente nos livros P1/P2/P9, sem nenhum tipo de tratamento especial\. A lógica para recuperação destas notas deve ser a mesma que é aplicada hoje nos livros:

*Se \(data\_fiscal entre data inicial e data final e data\_extemporânea não*

*       preenchida\) ou Data\_extemporânea entre data inicial e data final*

__\[ALTERADA – CH112751\]__

__OBS1__: Este registro passa a ter o tratamento de inscrição estadual única, onde devem ser apresentados no arquivo todos os registros de estabelecimentos centralizados\.

__OBS2__: Este registro não é gerado na opção “Geração – PIM” \(ver detalhes nas __OS2388\-AM\*__, que definiram a geração do Sped Fiscal para o PIM\)\.

__OBS3__: A __VAF\-MG__ a partir de 2020 passou a ser gerada com base nas regras de vários registros do SPED FISCAL \(C190, D190\.\.\.\)\. Ao realizar uma alteração na regra de geração do registro D300 como inclusão de um modelo, um critério de recuperação da nota, um tratamento de situação especial, a regra de geração da VAF\-MG deve ser revista \(tópico 2 do MTZ\-VAFMG\_Geracao\_Relatorio\_EFD\-Fiscal\.docx\)\.

RND300\-02

__Campo: COD\_MOD__:

De acordo com o agrupamento 1 gravar o conteúdo do campo “modelo de documento” \(campo 13 da SAFX07\) = 13, 14, 15 ou 16\.

REGISTRO ANALÍTICO DOS BILHETES CONSOLIDADOS DE:

BILHETES DE PASSAGEM RODOVIÁRIO \(CÓDIGO 13\),

BILHETES DE PASSAGEM AQUAVIÁRIO \(CÓDIGO 14\), 

BILHETES DE  PASSAGEM E NOTA DE BAGAGEM \(CÓDIGO 15\) E

BILHETES DE PASSAGEM FERROVIÁRIO  \(CÓDIGO 16\)\.

RND300\-03

__Campo: SER__

De acordo com o agrupamento 1 gravar o conteúdo do campo “série” \(campo: 09/SAFX07\)\.

RND300\-04

__Campo: SUB__

De acordo com o agrupamento 1 gravar o conteúdo do campo “sub\-série” \(campo: 10/SAFX07\)\.

RND300\-05

__Campo: NUM\_DOC\_INI__

De acordo com o __agrupamento 1__ gravar neste campo o número do primeiro bilhete de passagem emitido no dia independente de ser cancelado ou não \(campo: 08/SAFX07\)\. 

RND300\-06

__Campo: NUM\_DOC\_FIN__

De acordo com o __agrupamento 1__ gravar neste campo o número do último bilhete de passagem emitido no dia independente de ser cancelado ou não \(campo: 08/SAFX07\)\.

RND300\-07 

__Campo: CST\_ICMS__

De acordo com o agrupamento 1 gravar a concatenação dos campos  “Código Situação Tributária A” \+ “Código Situação Tributária B” \(campos: 179/180/SAFX07\)\.

RND300\-08

__Campo: CFOP__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Código Fiscal” \(campo: 14/SAFX07\)\.

RND300\-09

__Campo: ALIQ\_ICMS__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Alíquota ICMS” \(campo: 34/SAFX07\)\.

RND300\-10

__Campo: DT\_DOC__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Data de Emissão” \(campo: 11/SAFX07\)\.

RND300\-11

__Campo: VL\_OPR__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Valor Total do Documento Fiscal” \(campo: 23/SAFX07\)\.

Se o registro for cancelado, campo “SITUAÇÃO” = S gravar |0,00|\.

RND300\-12

__Campo: VL\_DESC__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Valor Descontos” \(campo: 28/SAFX07\)\.

Se o registro for cancelado, campo “SITUAÇÃO” = S gravar |0,00|\.

RND300\-13

__Campo: VL\_SERV__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Valor dos Produtos / Serviços” \(campo: 22/SAFX07\)\.

Se o registro for cancelado, campo “SITUAÇÃO” = S gravar |0,00|\.

RND300\-14

__Campo: VL\_SEG__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Valor do Seguro” \(campo: 25/SAFX07\)\.

Se o registro for cancelado, campo “SITUAÇÃO” = S gravar |0,00|\.

RND300\-15

__Campo: VL\_OUT\_DESP__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Valor de Outras Despesas” \(campo: 26/SAFX07\)\.

Se o registro for cancelado, campo “SITUAÇÃO” = S gravar |0,00|\.

RND300\-16

__Campo: VL\_BC\_ICMS__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Base ICMS Tributada” \(campo: 51/SAFX07\)\.

Se o registro for cancelado, campo “SITUAÇÃO” = S gravar |0,00|\.

RND300\-17

__Campo: VL\_ICMS__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Valor ICMS” \(campo: 35/SAFX07\)\.

Se o registro for cancelado, campo “SITUAÇÃO” = S gravar |0,00|\.

RND300\-18

__Campo: VL\_RED\_BC__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Base Redução ICMS” \(campo: 54/SAFX07\)\.

Se o registro for cancelado, campo “SITUAÇÃO” = S gravar |0,00|\.

RND300\-19

__Campo: COD\_OBS__

Recuperar a informação do campo 178 – Código da Observação da SAFX07\.

\[__ALTERAÇÃO \- MFS69058__\] Tratamento para considerar o parâmetro – “Campo Código de Observação \(Considerar 6 caracteres\)” \- para truncar o campo com 6 posições, conforme Manual Guia Prático\.

__SE__ o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

__OU__

__SE__ o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

Este código deverá ser referenciado no registro 0460\.

RND300\-20

__Campo: COD\_CONTA__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Conta Contábil” \(campo: 33/SAFX07\)\.  

__REGISTRO D301 \- DOCUMENTOS CANCELADOS DOS:__

__DE BILHETES DE PASSAGEM RODOVIÁRIO \(CÓDIGO 13\), __

__DE PASSAGEM AQUAVIÁRIO \(CÓDIGO 14\), __

__DE PASSAGEM E NOTA DE BAGAGEM \(CÓDIGO 15\) E __

__DE PASSAGEM FERROVIÁRIO \(CÓDIGO 16\)__

RND301

Este registro visa gravar somente os documentos cancelados para o intervalo de documentos selecionados no registro D300, ou seja, todos os documentos com campo “SITUAÇÃO” \(Campo: 30/SAFX07\) = S no intervalo informado entre os campos 04 e 05 do registro D300\.

Para cada registro D300 pode haver nenhum, um ou vários registros D301\.

RND301\-02

__Campo: NUM\_DOC\_CANC__

De acordo com o __agrupamento 1__ gravar neste campo o número de cada  bilhete de passagem cancelado \(campo: 08/SAFX07\)\. 

Campo “SITUAÇÃO” \(Campo: 30/SAFX07\) = S\.

__REGISTRO D310 \- COMPLEMENTO DOS BILHETES \(CÓDIGO 13, 14, 15 E 16\)__

RND310

Este registro tem por objetivo agrupar por município de origem  do serviço os valores dos documentos fiscais agrupados no Registro D300\.

__AGRUPAMENTO 2__

Data de Emissão,

Modelo de Documento__,__

Série do Documento Fiscal__,__

Subsérie do Documento Fiscal__,__

Concatena: Código Situação Tributária “A”/ Código Situação Tributária “B”__,__

Código Fiscal__,__

Alíquota ICMS__,__

Conta Contábil__,__

Concatena: UF Origem \+ Município Origem = __Código do Município__

__Situação da Nota = N\.__

Registro obrigatório se existir registro D300\.

RND310\-02

__Campo: COD\_MUN\_ORIG__

De acordo com o __agrupamento 2, __gravar neste campo a concatenação dos campos código da “UF ORIGEM” \(campo: 117/SAFX07\) \+ código do “MUNICIPIO ORIGEM” \(campo: 182/SAFX07\)\. 

O código do município deve existir na Tabela de Municípios do IBGE, sempre com 7 dígitos \(2 da UF \+ 5 do Município\), caso contrário será rejeitado pelo PVA\.

Será considerado registro duplicado se existir mais de um código de município para mesma data\.

RND310\-03

__Campo: VL\_SERV__

De acordo com o agrupamento 2 gravar o conteúdo do campo “Valor dos Produtos / Serviços” \(campo: 22/SAFX07\)\.

RND310\-04

__Campo: VL\_BC\_ICMS__

De acordo com o agrupamento 2 gravar o conteúdo do campo “Base ICMS Tributada” \(campo: 51/SAFX07\)\.

RND310\-05

__Campo: VL\_ICMS__

De acordo com o agrupamento 2 gravar o conteúdo do campo “Valor ICMS” \(campo: 35/SAFX07\)\.

# Registros D350 – Equipamento ECF

RND350

Este registro deverá ser apresentado para identificação dos equipamentos de ECF, por todos os contribuintes que utilizem este equipamento na emissão de Cupom Fiscal Bilhete de Passagem \(Código 2E\), Bilhete de Passagem Rodoviário \(13\), Bilhete de Passagem Aquaviário \(14\), Bilhete de Passagem e Nota de Bagagem \(15\) e Bilhete de Passagem Ferroviário \(13\)\. 

A seleção da chave do registro será:

Empresa;

Estabelecimento;

Modelo Documento;

Nº do Caixa;

Data Movimento;

Para cada data de movimento, por modelo \(2E, 13, 14, 15,16\) selecionar o Nº do caixa e ir na tabela SAFX2087 para obter as informações necessárias para geração deste registro\.

Se houver modificação no modelo documento,  no modelo ECF ou no nº de série do fabricante este registro será 1:N dentro do período selecionado\. 

Alteração OS2388O4\-GE \(Tratamento I\.E\.U\) 

Analista de Requisito: Adilson Gomes

Alterada geração dos registros C400 e D350 \(e filhos\) para geração por inscrição estadual única, solicitação efetuada pelas empresas de utilites que utilizam ECF de forma centralizada\.

Os documentos a serem recuperados na geração por I\.E\.U devem ser os documentos de todos os estabelecimentos envolvidos na centralização, ou seja, serão os cupons  fiscais do estabelecimento centralizador e de todos os centralizados; observar regras de geração para cupom ECF na OS2388M\-GE\.

__Regra do PVA:__

__Campo 05 do registro D350: __informar o número do caixa atribuído, pelo estabelecimento, ao equipamento emissor de documento fiscal\. Um mesmo valor do campo ECF\_CX não pode ser usado por dois equipamentos ECF ao mesmo tempo\. Contudo, se o uso de um número for cessado, este mesmo número pode ser atribuído a outro equipamento de ECF, no período\.

__Validação do Registro: __não podem ser informados dois ou mais registros D350 com a mesma combinação de valores dos campos COD\_MOD, ECF\_MOD e ECF\_FAB\.

__OBS1__: Este registro não é gerado na opção “Geração – PIM” \(ver detalhes nas __OS2388\-AM\*__, que definiram a geração do Sped Fiscal para o PIM\)\.

__OBS2__: A __VAF\-MG__ a partir de 2020 passou a ser gerada com base nas regras de vários registros do SPED FISCAL \(C190, D190\.\.\.\)\. Ao realizar uma alteração na regra de geração dos registros D350, D355 e D390 , como inclusão de um modelo, um critério de recuperação do cupom, um tratamento de situação especial, a regra de geração da VAF\-MG deve ser revista \(tópico 2 do MTZ\-VAFMG\_Geracao\_Relatorio\_EFD\-Fiscal\.docx\)\.

# Registros D355 – Redução Z

RND355

Este registro deverá ser apresentado com as informações da Redução Z de cada equipamento em funcionamento na data das prestações às quais se refere a redução\. Este registro inclui todos os documentos ficais da tabela SAFX991, totalizados na Redução Z, incluindo as prestações realizadas durante o período de tolerância do Equipamento ECF\. 

A seleção da chave do registro será:

Empresa;

Estabelecimento;

Modelo Documento;

Nº do Caixa;

Data Movimento;

CRZ;

Alteração OS2388M3\-GE ,  Data: 21/01/2009,  Analista de Requisito: Adilson Gomes

Solicitação: Redução Z com Venda Bruta = 0 \(zero\)\.

Apesar do PVA não validar este campo solicito implementar esta alteração nesta OS pois trata\-se de procedimentos operacionais para escrituração da redução Z na EFD\.

Condição: 1

A seleção da chave do registro será:

Empresa;

Estabelecimento;

Modelo Documento;

Nº do Caixa;

Data Movimento;

CRZ;

Se o campo 15 da SAFX991 estiver com “0” significa que o campo “VL\_BRT” no registro C405 será gravado com “0,00”, então:

Se o campo 15 \(venda bruta diária\) da SAFX991 = 0;

         Se campo 16 \(venda líquida diária\) = 0; 

                   Se o valor do campo 13 \(GT inicial\) for = ao valor do campo 14 \(GT final\),

                             Gravar registro D355, não gravar registros filhos e D390\.

= = = = =

__OBS1__: A __VAF\-MG__ a partir de 2020 passou a ser gerada com base nas regras de vários registros do SPED FISCAL \(C190, D190\.\.\.\)\. Ao realizar uma alteração na regra de geração dos registros D350, D355 e D390 , como inclusão de um modelo, um critério de recuperação do cupom, um tratamento de situação especial, a regra de geração da VAF\-MG deve ser revista \(tópico 2 do MTZ\-VAFMG\_Geracao\_Relatorio\_EFD\-Fiscal\.docx\)\.

# Registros D360 – PIS e COFINS totalizados no dia

RND360

Para cada data de movimento será gravado um registro D355, o registro D310 deverá ser apresentado sempre que houver produtos totalizados na Redução Z que acarretem valores de PIS e COFINS, os valores devem ser extraídos da tabela SAFX991\.

Desta forma podemos concluir que, podem existir zero ou um registro D360 para cada Registro D355\. 

# Registros D365 – Registro dos Totalizadores Parciais da Redução Z

RND365

Este registro deverá ser gerado para discriminar os valores por código de totalizador parcial da Redução Z conforme elencado na tabela 4\.4\.6 do ato cotepe 09 de 2008\.

Deve ser gerado um registro para cada totalizador parcial do ECF gravado na tabela SAFX992\.

RND365\-02

Campo: COD\_TOT\_PAR

O conteúdo deste campo será obtido através de seguinte regra:

Com a informação do campo 7 da tabela  SAFX992, acessar a tabela “SAFX99, campo 8” para buscar o depara do totalizador parcial utilizado pelo cliente e o totalizador exigido pela tabela 4\.4\.6 da obrigação , no caso SPED FISCAL\.

A seleção da chave do registro será:

Empresa;

Estabelecimento;

Modelo Documento;

Nº do Caixa;

Obrigação = 2;

Data Movimento;

Código do Totalizador Parcial do ECF:

 

       Se código do totalizador parcial das obrigações = T ou S,

       Buscar alíquota no campo 10 da tabela “Totalizador Parcial do ECF”;

       O COD\_TOT\_PAR será Tnnnn ou Snnnn, onde nnnn será a alíquota do imposto     encontrada no campo 10\.

     

        Se código do totalizador parcial das obrigações = F, I, N, FS, IS ou NS,

        Buscar sequencia do totalizador no campo 8 da tabela  “Totalizador Parcial do ECF”;

        O COD\_TOT\_PAR será Fn, In, Nn, FSn, ISn ou NSn onde n será a sequencia do totalizador \(sem o zero a esquerda\)\.

        Se código do totalizador parcial das obrigações = OPNF, DT, DS, DO, AT, AS, AO, Can\-T, Can\-S, Can\-O e IOF só devem ser gravados os códigos, sem sequencia ou alíquota do imposto\.

__RND365\-04__

Campo: NR\_TOT

         Gravar a sequencia do totalizador \(campo 8 da tabela  “Totalizador Parcial do ECF”\); quando  ocorrer mais de uma situação com a mesma carga tributária efetiva \(mesma alíquota\)\.

         Segundo anexo I \(guia prático\), Se o campo NR\_TOT estiver preenchido o Campo 02 \(COD\_TOT\_PAR\) deve ser um código de totalizador tributável pelo ICMS\.

Então,

         Se código do totalizador parcial das obrigações = T;

         Buscar alíquota no campo 10 da tabela “Totalizador Parcial do ECF”;

         O COD\_TOT\_PAR será Tnnnn onde nnnn será a alíquota do imposto encontrada no campo 10\.

         Se existir para mesma chave Tnnnn e alíquotas iguais os campos 4 e 5 devem ser preenchidos\.

__RND365\-05__

Campo: DESCR\_NR\_TOT

Descrição da situação tributária relativa ao totalizador parcial, quando houver mais de um com a mesma carga tributária efetiva, se o campo 04 \(NR\_TOT\) estiver preenchido este campo também deve ser preenchido\.

# Registro D370 – Complemento dos Documentos Informados

RND370

Este registro deverá informar dados complementares dos modelos de documentos fiscais referenciados, agrupando os valores por município de origem da prestação\. 

Selecionar na tabela SAFX991, COO inicial \(campo; 11\) e o COO final \(campo: 12\) emitido para cada data de movimento, por equipamento ECF,

 

= = = = = 	

Alteração OS2388\-???, 20/06/2009

Solicitação: Recuperação dos cupons na SAFX994 a partir do COO Inicial e Final informados na SAFX991\.

Foi criado campo 38 na SAFX2087 com o propósito dos clientes informarem o número máximo do COO emitido para o ECF, ao atingir este número a numeração do COO é reiniciada automaticamente no mesmo dia, neste caso não é necessário a intervenção técnica no equipamento\. 

Ex: 009999, 099999 ou 999999\.

Esta regra só deverá ser aplicada pelo programa na seguinte condição:

Se o COO Inicial for maior que o COO Final na SAFX991 para mesma data de movimento \(condição 2\)\.

        Condição 1:  COO Inicial = 000154

                             COO Final   = 008954

        Condição 2:  COO Inicial = 008954

                              COO Final  = 000154

Se condição = 1, as regras adotadas hoje continuam inalteradas\. ou seja, o programa busca o intervalo entre o cupom final e inicial\.

Se condição = 2, o programa deve ir na SAFX2087, buscar o número do COO FIN REINICIO, que corresponde ao número máximo do cupom para aquele ECF, que ao atingir este número a numeração do COO reinicia automaticamente no equipamento ECF\.

Desta forma o programa conseguirá identificar o intervalo dos cupons que deverão ser recuperados na SAFX994\.

Se condição = 2, se número do COO FIN REINICIO não preenchido, criticar\.\.\.

Mensagem: COO inicial maior que o COO Final e não foi informado o “Número do COO Final para Reinicio” na tabela Cadastro de Equipamento  ECF\.

= = = = =

Selecionar na tabela SAFX993\.\.\.

Empresa;

Estabelecimento;

Modelo Documento;

Nº do Caixa;

Intervalo do COO Inicial e COO final;

Situação do documento = 1

Tipo de documento = 1

Selecionar na tabela SAFX994\.\.\.

         Se,

                 se situação do Ítem do cupom = 1 e 3; e

                              código do totalizador parcial das obrigações = T, F, I, N\.

RND370\-02

Campo: COD\_MUN\_ORIG

Este campo é o agrupamento dos cupons por município de origem do  serviço \(campo: 21\)  da tabela SAFX993 por dia de cada ECF, 

Selecionar na tabela SAFX993\.\.\.

          Se, 

                situação do documento = 1; e

                        tipo de documento = 1; e

Selecionar na tabela SAFX994\.\.\.

         Se,

                 se situação do Ítem do cupom = 1 e 3;

Concatenar o Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código  do município de origem do  serviço \(para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\)  

O valor informado no campo 21 deverá existir na Tabela de Municípios do IBGE, possuindo 7 dígitos\.

RND370\-03

Campo: VL\_SERV

Este campo é o agrupamento por município \(campo: 21\) do Valor Total Líquido  \(campo: 25\) da tabela SAFX993 de um dia no ECF, 

Selecionar na tabela SAFX993\.\.\.

          Se, 

                situação do documento = 1; e

                        tipo de documento = 1; e

Selecionar na tabela SAFX994\.\.\.

         Se,

                 se situação do Ítem do cupom = 1 e 3;

RND370\-04

Campo: QTD\_BILH

Este campo é o agrupamento por município do total de cupons efetivamente vendidos no dia, por ECF

Selecionar na tabela SAFX993\.\.\.

          Se, 

                situação do documento = 1; e

                        tipo de documento = 1; e

Selecionar na tabela SAFX994\.\.\.

         Se,

                 se situação do Ítem do cupom = 1 e 3;

A Quantidade de bilhetes será a soma dos cupons na condição acima\.\.\.               

RND370\-05

Campo: VL\_BC\_ICMS

O conteúdo deste campo será obtido através de seguinte regra:

Com a informação do campo 7 da tabela  SAFX992, acessar a tabela “SAFX99, campo 8” para buscar o depara do totalizador parcial utilizado pelo cliente e o totalizador exigido pela tabela 4\.4\.6 da obrigação , no caso SPED FISCAL\.

A seleção da chave do registro será:

Empresa;

Estabelecimento;

Modelo Documento;

Nº do Caixa;

Obrigação = 2;

Data Movimento;

Código do Totalizador Parcial do ECF;

Selecionar na tabela SAFX993\.\.\.

          Se, 

                situação do documento = 1; e

                        tipo de documento = 1; e

Selecionar na tabela SAFX994\.\.\.

         Se,

                 se situação do Ítem do cupom = 1 e 3;

 

       Se código do totalizador parcial das obrigações = T ,

               

Ir na tabela SAFX994

         Gravar neste campo a soma do campo 28\.

     

RND370\-06

Campo: VL\_ICMS

Se campo VL\_BC\_ICMS > 0, gravar neste campo a soma do campo 29 da tabela SAFX994\.

# Registro D390 – Registro Analítico do Movimento Diário 

RND390

Este registro é um agrupamento dos valores das prestações de serviço do dia, utilizar a mesma regra de seleção do registro C470, este registro representa a escrituração dos itens dos cupons fiscais emitidos por ECF e totalizados pela combinação de: 

CST\_ICMS \- Código de Situação Tributária do ICMS 

CFOP  \-  Código Fiscal de Operação 

ALIQ\_ICMS \- Alíquota ICMS  

Estes registros devem ser obtidos na tabela SAFX994\.

O validador PVA não permite dois ou mais registros com a mesma combinação de valores dos Campos 02 \(CST\_ICMS\), 03 \(CFOP\) e 04 \(ALIQ\_ICMS\), caso ocorra inconsistência na base do cliente gere o registro errado e o validador irá rejeitar o arquivo\.

Selecionar na tabela SAFX993\.\.\.

          Se, 

                situação do documento = 1; e

                        tipo de documento = 1; e

Selecionar na tabela SAFX994\.\.\.

         Se,

                 se situação do Ítem do cupom = 1 e 3;

__OBS1__: A __VAF\-MG__ a partir de 2020 passou a ser gerada com base nas regras de vários registros do SPED FISCAL \(C190, D190\.\.\.\)\. Ao realizar uma alteração na regra de geração dos registros D350, D355 e D390 , como inclusão de um modelo, um critério de recuperação do cupom, um tratamento de situação especial, a regra de geração da VAF\-MG deve ser revista \(tópico 2 do MTZ\-VAFMG\_Geracao\_Relatorio\_EFD\-Fiscal\.docx\)\.

RND390\-02

Campo: CST\_ICMS

Este campo deve ser preenchido de 2 formas:

1\) Com o conteúdo do campo 15 da SAFX994 ir na tabela “Totalizador Parcial do ECF”, se preenchido concatenar campo 11\-Código Situação Tributária A \+12\-Código Situação Tributária B\. 

2\) Se regra do item 1 não atender, concatenar o conteúdo do campo 12\-Código Situação Tributária A \+13\-Código Situação Tributária B da  SAFX994\.

RND390\-03

Campo: CFOP

Este campo deve ser preenchido de 2 formas:

 1\) Com o conteúdo do campo 15 da SAFX994 ir na tabela “Totalizador Parcial do ECF”, se preenchido gravar conteúdo do campo13\-CFOP\. 

 2\) Se regra do item 1 não atender, gravar o conteúdo do campo  campo14\-CFOP da  SAFX994\.

RND390\-04

Campo: ALIQ\_ICMS

Este campo deve ser preenchido da seguinte forma:

1\) Com a informação do campo 15 da tabela  SAFX994, acessar a tabela “SAFX99,              campo 8” para buscar o depara do totalizador parcial utilizado pelo cliente e o   totalizador exigido pela tabela 4\.4\.6 da obrigação , no caso SPED FISCAL\.

 

2\)  Se código do totalizador parcial das obrigações = T;

              Buscar alíquota no campo 10 da tabela “Totalizador Parcial do ECF”;

RND390\-05

Campo: VL\_OPR

Este campo deve ser preenchido com agrupamento do campo 22 \(Valor Total Líquido\) da tabela SAFX994 para as combinações:

CST\_ICMS \- Código de Situação Tributária do ICMS 

CFOP  \-  Código Fiscal de Operação 

ALIQ\_ICMS \- Alíquota ICMS  

RND390\-06

Campo: VL\_BC\_ ISSQN 

O conteúdo deste campo deve ser obtido através da seguinte regra:

Com a informação do campo 7 da tabela  SAFX992, acessar a tabela “SAFX99, campo 8” para buscar o depara do totalizador parcial utilizado pelo cliente e o totalizador exigido pela tabela 4\.4\.6 da obrigação , no caso SPED FISCAL\.

A seleção da chave do registro será:

Empresa;

Estabelecimento;

Modelo Documento;

Nº do Caixa;

Obrigação = 2;

Data Movimento;

Código do Totalizador Parcial do ECF;

 

       Se código do totalizador parcial das obrigações = S,

               

Ir na tabela SAFX994

         Gravar neste campo a soma do campo 28\.

RND390\-07

Campo: ALIQ\_ISSQN

Este campo deve ser preenchido da seguinte forma:

1\)   Com a informação do campo 15 da tabela  SAFX994, acessar a tabela “SAFX99,            campo 8” para buscar o depara do totalizador parcial utilizado pelo cliente e o   totalizador exigido pela tabela 4\.4\.6 da obrigação , no caso SPED FISCAL\.

 

2\)    Se código do totalizador parcial das obrigações = S;

                Buscar alíquota no campo 10 da tabela “Totalizador Parcial do ECF”;

RND390\-08

Campo: VL\_ISSQN

Se campo VL\_BC\_ISSQN > 0, gravar neste campo a soma do campo 29 da tabela SAFX994

RND390\-09

Campo: VL\_BC\_ICMS

O conteúdo deste campo deve ser obtido através da seguinte regra:

Com a informação do campo 7 da tabela  SAFX992, acessar a tabela “SAFX99, campo 8” para buscar o depara do totalizador parcial utilizado pelo cliente e o totalizador exigido pela tabela 4\.4\.6 da obrigação , no caso SPED FISCAL\.

A seleção da chave do registro será:

Empresa;

Estabelecimento;

Modelo Documento;

Nº do Caixa;

Obrigação = 2;

Data Movimento;

Código do Totalizador Parcial do ECF;

 

       Se código do totalizador parcial das obrigações = T\.

               

Ir na tabela SAFX994

         Gravar neste campo a soma do campo 28\.

RND390\-10

Campo: VL\_ICMS

Se campo VL\_BC\_ICMS > 0, gravar neste campo a soma do campo 29 da tabela SAFX994\.

RND390\-11

__Campo: COD\_OBS__

Não tratado\.

__REGISTRO D400: RESUMO DE MOVIMENTO DIÁRIO \(CÓDIGO 18\)__

RND400

O registro D400 tem por objetivo a apresentação do resumo de movimento diário \(modelo 18\) emitido pelas agências, postos, filiais ou veículos de estabelecimentos que executam serviços de transporte de passageiros com inscrição centralizada\.

\[CH23730\_2012/OS3785 – Inclusão de crítica\] Quando selecionado o Perfil B:

Incluir a seguinte crítica no LOG de geração caso não tenha sido informado ao menos um registro D410 \(Filho\) para cada D400: *“Para cada registro D400, obrigatoriamente deve ser apresentado, pelo menos, um registro D410\.”*

O modelo 18 é um resumo do movimento diário dos bilhetes de passagem armazenados no DW e deve ser extraído se atender  as  seguintes condições:

Tabela: SAFX07

__CONDIÇÃO 1:__

Se movimento entrada/saída = 9,

         Se classificação do documento fiscal = 1 ou 3,	

                      Se modelo de documento = 18\.

Deve ser gerado um ou vários registros D400 para cada data de emissão, estas datas devem estar contidas no período selecionado no registro 0000 à \(data >= campo 04 e <= campo 05\)\. 

A identificação dos códigos para preenchimento do campo 03 do registro D400 deve ser feita pelo campo “13 – Modelo de Documento” da SAFX07\.

__Descrição do Campo:__

__Nº do Campo:__

__Nome do Campo no MasterSAF:__

__Nome do Campo no Registro D400:__

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

Situação da Nota

30

SITUACAO

Data de Emissão

11

DATA\_EMISSAO

DT\_DOC

Série do Documento Fiscal

09

SERIE\_DOCFIS

SER

Subsérie do Documento Fiscal

10

SUB\_SERIE\_DOCFIS

SUB

Aguardando confirmação do Tutomo…

__Observação 1:__ Se o documento estiver cancelado não gerar os filhos do registro D400\.

__Observação 2: __Se o documento estiver cancelado gravar no registro D400 somente os campos 01 ao 08\.

\(regra alterada em Set/2009 no chamado CH70055, devido a orientação do Guia Prático 1\.0\.5\)

__Observação 2: __Se o documento estiver cancelado gravar no registro D400 somente os campos relacionados abaixo:

\-REG \(campo 01\)

\-COD\_MOD \(campo 03\)

\-COD\_SIT \(campo 04\)

\-SER \(campo 05\)

\-SUB \(campo 06\)

\-NUM\_DOC \(campo 07\)

 

Os demais campos \(02 e 08 ao 15\) deverão ser apresentados com conteúdo __VAZIO__ ||\.

__Observação sobre as notas extemporâneas__

O RMD com data extemporânea será tratado normalmente, exatamente da mesma forma como é feito na versão atual do Mastersaf, ou seja, o documento com data extemporânea é lançada normalmente nos livros P1/P2/P9, sem nenhum tipo de tratamento especial\.

A lógica para recuperação destas notas deve ser a mesma que é aplicada hoje nos livros:

*Se \(data\_fiscal entre data inicial e data final e data\_extemporânea não*

*       preenchida\) *

*ou*

*     Data\_extemporânea entre data inicial e data final*

*= = = = =*

__OBS1__: este registro *não* tem o tratamento da Inscrição Estadual Única \(OS2388\-O1ge\), por entendermos que conceitualmente não se aplica\.

__OBS2__: Este registro não é gerado na opção “Geração – PIM” \(ver detalhes nas __OS2388\-AM\*__,  que definiram a geração do Sped Fiscal para o PIM\)\.

__OBS3__: A __VAF\-MG__ a partir de 2020 passou a ser gerada com base nas regras de vários registros do SPED FISCAL \(C190, D190\.\.\.\)\. Ao realizar uma alteração na regra de geração dos registros D400 e D410 , como inclusão de um modelo, um critério de recuperação do documento, um tratamento de situação especial, a regra de geração da VAF\-MG deve ser revista \(tópico 2 do MTZ\-VAFMG\_Geracao\_Relatorio\_EFD\-Fiscal\.docx\)\.

__RND400\-02__

Campo COD\_PART

\[OS4747\] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

__RND400\-04__

Campo: COD\_SIT

Para o preenchimento deste campo deverão ser verificados alguns campos da SAFX07, conforme segue:

Se for nota cancelada, verificar:

      se a nota é extemporânea           à gravar “03”

      se a nota é normal \(não extemp\.\) à gravar “02”

Se for nota extemporânea, verificar:

      se a nota é complementar          à gravar “07”

      se a nota é normal \(não compl\.\) à gravar “01”

Se for nota complementar, verificar:

      gravar “06”

Se nota tem Ato Normativo, Regime Especial etc\.\.\.

      gravar “08”

Se a nota não atende a nenhuma das opções anteriores:

      gravar “00”

__Importante:__ 

Os testes devem ser executados exatamente nesta prioridade\. Assim, o teste deve ser encerrado na primeira regra atendida pela nota, e sempre que isto *não ocorrer*, será gravado o conteúdo “00”\.

A lógica seria a seguinte:

        __Se__ nota é cancelada

             __Se__ nota é extemporânea

                   gravar “03”

             __Senão__

                   gravar “02”

#         Senão

              __Se__ nota é extemporânea

                    __Se__ nota é complementar

                         gravar “07”

                    __Senão__

                         gravar “01”

              __Senão__

                    __Se__ nota é complementar

                         gravar “06”

                    __Senão__

                         __Se__ nota tem Ato Normativo, Regime Especial etc

                              gravar “08”

                         __Senão__

                             gravar “00”;

__Campos da SAFX07 para verificação das regras:__

Nota cancelada à o campo “30\-Situação da nota” será =  “S”;

Nota extemporânea à o campo “77\-Data Escrita Extemporânea” estará preenchido;

Nota complementar à o campo “125\-Situação Especial” será = “5”;

 

__RND400\-14__

Campo VL\_PIS

__\[ALTERADO MFS17511\]__

Quando o parâmetro “Inibir a geração das informações constantes na EFD Contribuições \(Parâmetros > Dados Iniciais\)”  estiver marcado, este campo deve ser gerado em branco \(||\)\.

__RND400\-15__

Campo VL\_COFINS

__\[ALTERADO MFS17511\]__

Quando o parâmetro “Inibir a geração das informações constantes na EFD Contribuições \(Parâmetros > Dados Iniciais\)”  estiver marcado, este campo deve ser gerado em branco \(||\)\.

__REGISTRO D410 – DOCUMENTOS INFORMADOS  \(CÓDIGO 13, 14, 15 e 16\)__

RND410

O registro D410 é filho do D400 e tem por objetivo informar a  extratificação dos documentos consolidados no Resumo de Movimento Diário \(modelo 18\)\. Neste registro, deverão ser informados os documentos Bilhete de Passagem Rodoviário \(modelo 13\), Bilhete de Passagem Aquaviário \(modelo 14\), Bilhete de Passagem Ferroviário \(modelo 16\) e Bilhete de Passagem e Nota de Bagagem \(modelo 15\), quando não emitidos por ECF e obrigatoriamente devem utilizar o processo de inscrição centralizada\.

No DW os bilhetes de passagens devem ser armazenados no estabelecimento centralizador\.

O registro D410 é um agrupamento diário dos bilhetes de passagens e a geração deve obedecer  cronologicamente as regras descritas a seguir:

Tabela: SAFX07

__CONDIÇÃO 1:  Bilhetes armazenados no estabelecimento centralizador__

Para cada RMD buscar os bilhetes no próprio “COD\_ESTAB” da geração\.\.\.

     Se movimento entrada/saída do bilhete = 9,

              Se classificação do documento fiscal do bilhete = 9,	

                         Se modelo de documento = 13, 14, 15 ou 16\.

                         Se Número de Docto\. Fiscal de Ref\. do bilhete = Nº do RMD selecionado no registro D400

              Se Série e Sub\-série do Docto\. Fiscal de Ref\. do bilhete = Série e Sub\-série do RMD selecionado no registro D400

     Data da Declaração de Importação/Data Doc\. Original nas Oper\. de Devolução do bilhete =   Data de emissão do RMD   selecionado no registro D400 

Agrupamento 1 à é o agrupamento diário dos bilhetes em ordem crescente atendido na condição 1, a quebra do registro ocorrerá cada vez que diferenciar um ítem do agrupamento\.

__AGRUPAMENTO 1__

Data de Emissão,

Modelo de Documento__,__

Série do Documento Fiscal__,__

Subsérie do Documento Fiscal__,__

Concatena: Código Situação Tributária “A”/ Código Situação Tributária “B”__,__

Código Fiscal__,__

Alíquota ICMS__,__

__Descrição do Campo:__

__Nº do Campo:__

__Nome do Campo no MasterSAF:__

__Nome do Campo no Registro D410:__

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

Situação da Nota

30

SITUACAO

Data de Emissão

11

DATA\_EMISSAO

DT\_DOC

Série do Documento Fiscal

09

SERIE\_DOCFIS

SER

Subsérie do Documento Fiscal

10

SUB\_SERIE\_DOCFIS

SUB

Código Situação Tributária “A”/ Código Situação Tributária “B”

179/180

__Concatenar:__ COD\_SITUACAO\_A  \+  COD\_SITUACAO\_B

CST\_ICMS

Código Fiscal

14

COD\_CFO

CFOP

Alíquota ICMS

34

VLR\_ALIQ\_ICMS

ALIQ\_ICMS

__O aplicativo deverá emitir mensagem de erro no log de processos se, na utilização da condição 1 o aplicativo não conseguir associar o RMD ao bilhete\.__

RND410\-02

__Campo: COD\_MOD__:

De acordo com o agrupamento 1 gravar o conteúdo do campo “modelo de documento” \(campo 13 da SAFX07\) = 13, 14, 15 ou 16\.

REGISTRO ANALÍTICO DOS BILHETES CONSOLIDADOS DE:

BILHETES DE PASSAGEM RODOVIÁRIO \(CÓDIGO 13\),

BILHETES DE PASSAGEM AQUAVIÁRIO \(CÓDIGO 14\), 

BILHETES DE  PASSAGEM E NOTA DE BAGAGEM \(CÓDIGO 15\) ou

BILHETES DE PASSAGEM FERROVIÁRIO  \(CÓDIGO 16\)\.

RND410\-03

__Campo: SER__

De acordo com o agrupamento 1 gravar o conteúdo do campo “série” \(campo: 09/SAFX07\)\.

RND410\-04

__Campo: SUB__

De acordo com o agrupamento 1 gravar o conteúdo do campo “sub\-série” \(campo: 10/SAFX07\)\.

RND410\-05

__Campo: NUM\_DOC\_INI__

De acordo com o __agrupamento 1__ gravar neste campo o número do primeiro bilhete de passagem emitido no dia independente de ser cancelado ou não \(campo: 08/SAFX07\)\. 

RND410\-06

__Campo: NUM\_DOC\_FIN__

De acordo com o __agrupamento 1__ gravar neste campo o número do último bilhete de passagem emitido no dia independente de ser cancelado ou não \(campo: 08/SAFX07\)\.

RND410\-07

__Campo: DT\_DOC__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Data de Emissão” \(campo: 11/SAFX07\)\.

O valor no campo DT\_DOC do registro D410 deve ser igual ao valor do campo DT\_DOC do registro D400\.

RND410\-08 

__Campo: CST\_ICMS__

De acordo com o agrupamento 1 gravar a concatenação dos campos  “Código Situação Tributária A” \+ “Código Situação Tributária B” \(campos: 179/180/SAFX07\)\.

RND410\-09

__Campo: CFOP__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Código Fiscal” \(campo: 14/SAFX07\)\.

RND410\-10

__Campo: ALIQ\_ICMS__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Alíquota ICMS” \(campo: 34/SAFX07\)\.

RND410\-11

__Campo: VL\_OPR__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Valor Total do Documento Fiscal” \(campo: 23/SAFX07\)\.

Se o registro for cancelado, campo “SITUAÇÃO” = S gravar |0,00|\.

RND410\-12

__Campo: VL\_DESC__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Valor Descontos” \(campo: 28/SAFX07\)\.

Se o registro for cancelado, campo “SITUAÇÃO” = S gravar |0,00|\.

RND410\-13

__Campo: VL\_SERV__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Valor dos Produtos / Serviços” \(campo: 22/SAFX07\)\.

Se o registro for cancelado, campo “SITUAÇÃO” = S gravar |0,00|\.

RND410\-14

__Campo: VL\_BC\_ICMS__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Base ICMS Tributada” \(campo: 51/SAFX07\)\.

Se o registro for cancelado, campo “SITUAÇÃO” = S gravar |0,00|\.

OBS: Os campos 14 e 15 do registro D410 estão como obrigatórios no layout do arquivo, contudo solicito não exibir mensagem de erro no log de processos se um desses campos estiver com zero ou nulo\.

RND410\-15

__Campo: VL\_ICMS__

De acordo com o agrupamento 1 gravar o conteúdo do campo “Valor ICMS” \(campo: 35/SAFX07\)\.

Se o registro for cancelado, campo “SITUAÇÃO” = S gravar |0,00|\.

OBS: Os campos 14 e 15 do registro D410 estão como obrigatórios no layout do arquivo, contudo solicito não exibir mensagem de erro no log de processos se um desses campos estiver com zero ou nulo\.

__REGISTRO D411 \- DOCUMENTOS CANCELADOS DOS DOCTOS\. INFORMADOS:__

__DE BILHETES DE PASSAGEM RODOVIÁRIO \(CÓDIGO 13\), __

__DE PASSAGEM AQUAVIÁRIO \(CÓDIGO 14\), __

__DE PASSAGEM E NOTA DE BAGAGEM \(CÓDIGO 15\) E __

__DE PASSAGEM FERROVIÁRIO \(CÓDIGO 16\)__

RND411

Este registro visa gravar somente os documentos cancelados para o intervalo de documentos selecionados no registro D410, ou seja, todos os documentos com campo “SITUAÇÃO” \(Campo: 30/SAFX07\) = S no intervalo informado entre os campos 04 e 05 do registro 0000\.

Para cada registro D410 pode haver nenhum, um ou vários registros D411\.

RND411\-02

__Campo: NUM\_DOC\_CANC__

De acordo com o __agrupamento 1__ gravar neste campo o número de cada  bilhete de passagem cancelado \(campo: 08/SAFX07\)\. 

Campo “SITUAÇÃO” \(Campo: 30/SAFX07\) = S\.

__REGISTRO D420 \- COMPLEMENTO DOS DOCTOS\. INFORMADOS \(CÓDIGO 13, 14, 15 E 16\)__

RND420

Este registro tem por objetivo agrupar por município de origem  do serviço os valores dos documentos fiscais com modelo 18 agrupados no Registro D400\.

Ocorre que a informação “origem do serviço” encontra\-se disponibilizadas somente nos bilhetes de passagem \(modelo 13, 14, 15 e 16\), desta forma deve\-se buscar estas informações diretamente nos bilhetes\. 

__AGRUPAMENTO 2__

O registro D420 é o agrupamento por data da emissão dos valores por município de origem do serviço dos documentos fiscais com modelo 13, 14, 15 e 16 armazenados no DW com as  seguintes condições:

Tabela: SAFX07

__CONDIÇÃO 1:__

    Se movimento entrada/saída do bilhete = 9,

              Se classificação do documento fiscal do bilhete = 9,

                         Se modelo de documento = 13, 14, 15 ou 16\.

                         Se Número de Docto\. Fiscal de Ref\. do bilhete = Nº do RMD selecionado no registro D400

              Se Série e Sub\-série do Docto\. Fiscal de Ref\. do bilhete = Série e Sub\-série do RMD selecionado no registro D400

     Data da Declaração de Importação/Data Doc\. Original nas Oper\. de Devolução do bilhete =   Data de emissão do RMD selecionado no registro D400 

Concatena:__ __UF Origem \+ Município Origem__ = Código do Município__

__Situação da Nota = N\.__

RND420\-02

__Campo: COD\_MUN\_ORIG__

De acordo com o __agrupamento 2, __gravar neste campo a concatenação dos campos código da “UF ORIGEM” \(campo: 117/SAFX07\) \+ código do “MUNICIPIO ORIGEM” \(campo: 182/SAFX07\)\. 

O código do município deve existir na Tabela de Municípios do IBGE, sempre com 7 dígitos \(2 da UF \+ 5 do Município\), caso contrário será rejeitado pelo PVA\.

Será considerado registro duplicado se existir mais de um código de município para mesma data\.

RND420\-03

__Campo: VL\_SERV__

De acordo com o agrupamento 2 gravar o conteúdo do campo “Valor dos Produtos / Serviços” \(campo: 22/SAFX07\)\.

RND420\-04

__Campo: VL\_BC\_ICMS__

De acordo com o agrupamento 2 gravar o conteúdo do campo “Base ICMS Tributada” \(campo: 51/SAFX07\)\.

OBS: Os campos 04 e 05 do registro D420 estão como obrigatórios no layout do arquivo, contudo solicito não exibir mensagem de erro no log de processos se um desses campos estiver com zero ou nulo\.

RND420\-05

__Campo: VL\_ICMS__

De acordo com o agrupamento 2 gravar o conteúdo do campo “Valor ICMS” \(campo: 35/SAFX07\)\.

OBS: Os campos 04 e 05 do registro D420 estão como obrigatórios no layout do arquivo, contudo solicito não exibir mensagem de erro no log de processos se um desses campos estiver com zero ou nulo\.

__Registro D500  – NF Serviço de Comunicação \(Cód 21\) e Telecomunicação \(Cód 22\) __

RND500

A geração dos dados do sub\-bloco 500 \(500, 510, 520, 530 e 590\) tem origens distintas, dependendo do tipo da operação, se entrada ou saída\.

Neste sub\-bloco serão apresentadas as notas fiscais isoladamente \(não consolidadas\)\.

__MFS877174/MFS910283__:

Criação da tabela particionada DWT\_DOCTO\_FISCAL\_SPED espelho da DWT\_DOCTO\_FISCAL e utilização na geração dos registros C100, C500, D100, D500 e 1400 – UF = SP\.

Geração das Notas de Entrada à os dados serão recuperados nas tabelas SAFX07 e SAFX08, considerando apenas as notas com código de modelo = ’21’ ou ‘22’\.

\(para as entradas, alguns valores poderão ser recuperados da capa, caso a nota não tenha itens\)\. As notas que requerem tratamento especial estão descritas no documento “Notas Especiais D500\.doc”\.

Critérios de seleção das notas:

- Modelo \(campo “13 – Modelo de Documento” da SAFX07\) = 21 ou 22;
- Classificação \(campo “12 – Classificação do documento” da SAFX07\) = 1 ou 3;
- Notas de *entrada* de *terceiros* \(movto\_e\_s = 1\) e *canceladas*, *não* serão consideradas \(o objetivo é evitar que erros de procedimentos internos do cliente, possam prejudicar a escrituração\);
- Data \(data fiscal\) enquadrada no período de geração, ou notas com data extemporânea enquadrada no período de geração;

Observação sobre as notas extemporâneas:

As notas extemporâneas serão tratadas normalmente, exatamente da mesma forma como é feito na versão atual do Mastersaf, ou seja, a nota extemporânea é lançada normalmente nos livros P1/P2/P9, sem nenhum tipo de tratamento especial\.

A lógica para recuperação destas notas deve ser a mesma que é aplicada hoje nos livros:

*Se \(data\_fiscal entre data inicial e data final e data\_extemporânea não*

*       preenchida\) *

*ou*

*     Data\_extemporânea entre data inicial e data final*

__Obs importante à__ Notas de *terceiros *que estejam canceladas, e que por um problema de erro possam estar na base de dados, *não devem ser consideradas na geração*\. São as notas com MOVTO\_E\_S  =  “1”  e  SITUACAO  =  “S”;

Geração das Notas de Saída à os dados serão recuperados nas tabelas SAFX42 e SAFX43, considerando apenas modelo ‘21’ e ‘22’\. As notas de Utilities das tabelas SAFX42/43 sempre têm itens\. No caso das notas de saída, a única nota com situação de escrituração especial é a nota cancelada, que deve ser tratada da mesma forma descrita para as notas de entrada no documento “Notas Especiais D500\.doc”\.

Critérios de seleção das notas:

- Modelo \(campo “13 – Modelo de Documento”\) = 21 ou 22;
- Data Fiscal \(campo 03\) \- enquadrada no período de geração, ou notas com data extemporânea enquadrada no período de geração;
- Não considerar os itens informativos \(itens da SAFX43 com o campo 10\-Tipo de Item = 1\)

A geração das notas no D500 e “filhos” deve seguir a lógica:

Se Empresa *enquadrada* ao Convênio ICMS 115

                    Gerar apenas as notas emitidas em várias vias      

             Senão 

                    Gerar todas as notas;

Para verificar se a Empresa é obrigada ou não a geração do Convênio 115, verificar o novo indicador criado na tela de cadastro do Estabelecimento \(módulo Parâmetros\)\. 

Para melhor entendimento desta lógica, segue uma breve explicação sobre a existência de 3 sub\-blocos distintos para a movimentação de saída do segmento de Comunicação/Telecomunicação\. As regras descritas a seguir são importantes para a parametrização dos perfis de geração:   

__                  Entendimento dos sub\-blocos D500 x D600 x D695__

Sub\-bloco D500 \(movimento nota a nota\):

- Para as Empresas *obrigadas* ao Convênio ICMS 115, gerar apenas as notas emitidas em __*várias vias*__\. São as notas da X42/X43 com o campo “61\-Indicador de NF via única” = “N”;
- Para as Empresas *não obrigadas* ao Convênio ICMS 115, gerar todas as notas;

Sub\-bloco D600 \(movimento consolidado\):

- Somente para Empresas *não obrigadas* ao Convênio ICMS 115;
- Gerar todas as notas; 

Sub\-bloco D695 \(movimento consolidado\):

- Somente para Empresas *obrigadas* ao Convênio ICMS 115;
- Gerar os valores totalizados dos arquivos do Convênio ICMS 115; 

__Outra interpretação das regras considerando primeiro o tipo de Empresa__:

Empresas *não* enquadradas no Convênio ICMS 115: 

Se perfil = A à deve gerar todas as operações de saída, nota a nota no sub\-bloco D500;

Se perfil = B à deve gerar todas as operações de saída, consolidadas no sub\-bloco D600;

                           \(consolidação por modelo e município dos terminais faturados\)

Empresas enquadradas no Convênio ICMS 115:

Gerar as notas emitidas em várias vias no sub\-bloco D500;

Gerar o movimento totalizado dos arquivos do Convênio 115 no sub\-bloco D695;

Obs 07/04/2009 \(OS2388\-E8\) àEste conceito original foi contrariado pela Portaria SC 03/09\. De acordo com a Portaria, SC irá exigir *todas* as operações de Utilities nos registros C500 e D500 \(e “filhos”\)\. Os demais registros *não serão utilizados*, mesmo no caso das empresas obrigadas ao Convênio 115\. Neste caso, estas empresas *não deverão marcar o parâmetro* “Estabelecimento obrigado à entrega do arquivo do Convênio 115/03” \(ver help deste campo na tela de cadastro dos Estabelecimentos\)\. Conforme testes realizados em Abr/2009, a geração da EFD só não atendeu 100% a Portaria por um pequeno detalhe: os registros D510 e D530 *não* são habilitados no perfil B, já que conforme a regra original da EFD eles nunca seriam gerados neste perfil\. Os ajustes para solução deste problema foram feitos na OS2388\-E8\.     

Diferenças entre o D500 x D600:

\-D500 é movimento nota a nota, enquanto o D600 é consolidado p/ modelo e munic;

\-D500 é para empresas do perfil A, enquanto o D600 é para o perfil B;

O sub\-bloco D600 é para ser utilizado apenas pelas empresas enquadradas ao perfil B do Sped Fiscal;

__OBS1__:  a regra de geração dos registros de EE difere dos registros de Telecom, pois no caso de EE as operações interestaduais vão para o registro 1500 e “filhos”, além de constarem naturalmente no registro C700 \(já que este tem todo a movimento do arquivo Mestre do Convênio ICMS 115\)\. Este ponto foi esclarecido em call com Tutomo no dia 08/04/2008, cuja alteração de layout saiu no documente EXTRATO\_3\.doc \(Abril/2008, GT\-48 SPED\_FISCAL\)\. Maiores detalhes consultar documento sobre os pontos discutidos no call e o documento EXTRATO\_3\.

__OBS2__: Na geração por Inscrição Estadual Única, deve\-se considerar os documentos fiscais de todos os Estabelecimentos envolvidos na centralização \(OS2388\-O1ge\);

__OBS3: __Na geração da opção “Geração – PIM”, são tratadas apenas as operações de entrada deste registro\. São consideradas apenas as notas da inscrição estadual em questão, já que os usuários do PIM devem gerar um arquivo para cada inscrição estadual\. As operações de saídas não foram tratadas para este opção \(ver detalhes nas __OS2388\-AM\*__, que definiram a geração do Sped Fiscal para o PIM\)\.

__OBS4__: A __VAF\-MG__ a partir de 2020 passou a ser gerada com base nas regras de vários registros do SPED FISCAL \(C190, D190\.\.\.\)\. Ao realizar uma alteração na regra de geração dos registros D500 e D590, como inclusão de um modelo, um critério de recuperação da nota, um tratamento de situação especial, a regra de geração da VAF\-MG deve ser revista \(tópico 2 do MTZ\-VAFMG\_Geracao\_Relatorio\_EFD\-Fiscal\.docx\)\.

RND500\-03

Campo IND\_EMIT:

Para as notas de __entrada__, o conteúdo deste campo dependerá do indicador de Entrada/Saída da nota \(campo 03\-Movimento Entrada/Saída da SAFX07\), da seguinte forma:

Se indicador  = 1                  à gravar 1 \(emissão terceiros\)

Se indicador  = 2, 3, 4 ou 5  à gravar 0 \(emissão própria\)

Para as notas de __saída__ será sempre “0”\.

RND500\-04

Campo COD\_PART

\[OS4747\] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

RND500\-06

Campo COD\_SIT:

Para as notas de __entrada__, aplicar a mesma regra do registro C100, campo 06 \(RNC100\-06\)\.

Para as notas de __saída__, a regra é um pouco diferente, pois não há necessidade de tratar todos os casos\. Alguns casos não se aplicam às notas de modelo 21/22, como por exemplo, a situação da NF\-e denegada/inutilizada \(códigos 04 e 05\) e a situação de nota extemporânea \(códigos 01, 03 e 07\)\. \(Obs: o Msaf não trata extemporânea de Utilities\)

Para as notas de saída, com origem na SAFX42, aplicar a regra:

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

RND500\-15

Campo VL\_SERV\_NT: valor dos serviços não tributados pelo ICMS

\[__ALTERAÇÃO\-MFS69901__\] Inclusão de regra para considerar os CST’s “não tributados”

Para as notas de __entrada __à__ __Este valor será composto pela soma das bases isenta/outras/redução, relativo aos CST’s “não tributados” \. Para as notas de mercadoria será a soma destas bases, seja da capa \(notas sem item\), ou dos itens da SAFX08\. Para as notas mistas será a soma dos itens de mercadoria da SAFX08 \+ o valor dos serviços da SAFX09\.

__Notas *sem  *item:__

Valor das bases isenta/não tributada \+ base outras \+ base de redução da __SAFX07__: 

Preencher com a soma dos valores das bases isenta/não tributada \+ base outras \+ base de redução da __SAFX07__: \[campos 52 \+ 53 \+ 54\]

__  Se__ o Campo COD\_SITUACAO\_B da tabela __SAFX07__ for igual à “20”, “30”, “40”,”41”, “50”, “51” ou “90”\.

__Notas *com*  itens:__  

\(Classificação = “1”\)

Valor das bases isenta/não tributada \+ base outras \+ base de redução da __SAFX08__:

Preencher com a soma dos valores das bases isenta/não tributada \+ base outras \+ base de redução da __SAFX08__:

\[ campos 56 \(se campo 55 = 2 ou 3\)  \+ campo 57 \+ campo 83 \(se campo 82 = 2 ou 3\) \]

__ Se__ o Campo COD\_SITUACAO\_B da tabela __SAFX08__ for igual à “20”, “30”, “40”,”41”, “50”, “51” ou “90”\.

__Notas *mistas*__ \(itens na X08 e X09\) 

\(Classificação = “3”\)

Valor das bases isenta/não tributada \+ base outras \+ base de redução da __SAFX08__ \+ valor dos itens de serviço da __SAFX09__:

Preencher com a soma dos valores das bases isenta/não tributada \+ base outras \+ base de redução da __SAFX08__ \+ valor dos itens de serviço da __SAFX09__:

\[campos 56 \(se campo 55 = 2 ou 3\)  \+ campo 57 \+ campo 83 \(se campo 82 = 2 ou 3\)\] da SAFX08  \+  campo 14 da SAFX09

__ Se__ o Campo COD\_SITUACAO\_B da tabela __SAFX08__ for igual à “20”, “30”, “40”,”41”, “50”, “51” ou “90”\.

Para as notas de __saída __à este valor será composto da seguinte forma:

Valor das bases isenta/não tributada \+ base outras \+ base de redução dos *itens de mercadoria* da __SAFX43 __\+ valor do serviço dos *itens de serviço* da __SAFX43__:

\[campos 24\-Base Isenta/Não Tributada \+ campo 25\-Base Outras \+ campo 26\-Base de Redução dos itens de mercadoria \(campo 47 = “1”\) \]  \+ \[campo 19\-Valor do Serviço dos itens de serviço \(campo 47 = “2”\) \]

RND500\-20

Campo COD\_OBS

__Para notas de entrada__ à Recuperar a informação do campo 178 – Código da Observação da SAFX07\.

__Para notas de saída__ à Recuperar a informação do campo 66 – Código da Observação da SAFX42\.

\[__ALTERAÇÃO \- MFS60545__\] Tratamento para considerar o parâmetro – “Campo Código de Observação \(Considerar 6 caracteres\)” \- para truncar o campo com 6 posições, conforme Manual Guia Prático\.

__SE__ o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

__OU__

__SE__ o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

Este código deverá ser referenciado no registro 0450\.

RND500\-21

Campo VL\_PIS

__\[ALTERADO MFS17478\]__

Quando o parâmetro “Inibir a geração das informações constantes na EFD Contribuições \(Parâmetros > Dados Iniciais\)”  estiver marcado, este campo deve ser gerado em branco \(||\)\.

RND500\-22

Campo VL\_COFINS

__\[ALTERADO MFS17478\]__

Quando o parâmetro “Inibir a geração das informações constantes na EFD Contribuições \(Parâmetros > Dados Iniciais\)”  estiver marcado, este campo deve ser gerado em branco \(||\)\.

RND500\-24

Campo TP\_ASSINANTE: 

 Para as notas de __entrada, __não preencher o campo\.

 Alteração OS2388\-E20:

 Para as notas de __entrada__, preencher com o campo TIPO\_ASSINANTE da tabela   ESTABELECIMENTO

 Para as notas de __saída, __preencher com o campo 12 – Classe do Usuário da SAFX42\.

__Registro D510 – Itens do Documento \(Cód 21 e Cód 22\)__

RND510

Este registro deve ser gerado apenas nas operações de saída\. 

Neste registro serão gravados os itens da nota fiscal gravada no registro D500\.  

RND510\-03

Campo 03\-COD\_ITEM:

Preencher com o código do produto ou o código do serviço, dependendo da classificação do item \(campo 47\-Classificação do Documento Fiscal da SAFX43\):

Se item de mercadoria à campos 11/12 \(Indicador e Código do Produto\) da SAFX43

Se item de serviço à campo 48\-Código do Serviço da SAFX43

Alteração feita na OS2667, EM Dez/2008, Release 32:

Se item de serviço à gravar o Código do Serviço \(campo 48\) ou a natureza do serviço \(campo 8 da SAFX2018\), conforme parâmetro que indica a informação a ser gravada \(“Dados Iniciais”\) 

O campo deve ser preenchido de acordo com a regra descrita para o registro C170 \(vide regra RNC170\-03\)\.

\[Alteração – OS 3217\-A\]

Buscar a informação no campo  “Código da Natureza do Serviço – SPED FISCAL” da SAFX2018 quando houver preenchimento\.  

RND510\-06

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

RND510\-14

Campo 14 VL\_BC\_ICMS\_UF:

Se SAFX08, totalizar campo 56, mas *somente* quando a pessoa fis/jur da nota for de outra UF \(UF da SAFX04 <> UF do Estab\)

Alteração CH115852 

E somente para CFOPs de saída interestaduais <>’6301’

Se SAFX09, considerar zero;

Alteração OS3851 \(Junho/2012\):

Se CFOP do item for iniciado por “6” ou “7” *\(somente saídas interestaduais\)*

     O campo será preenchido com o valor da base de cálculo do ICMS devido a outra UF 

     \(campo “103\-Valor da BC do ICMS devido a Outra UF” criado na SAFX43 pela OS3851\) 

Obs: A condição do CFOP interestadual é apenas por uma questão de segurança, pois na verdade o campo 103 da SAFX43 foi criado especificamente para a carga da base do ICMS devido a outra UF nos termos do Conv 52/2005, e assim, só deve ser carregado nas prestações de serviço não\-medido de TV por assinatura via satélite para outra UF\)\.__ __

__ __

RND510\-15

Campo VL\_ICMS\_UF:

Se SAFX08, totalizar campo 43, mas *somente* quando a pessoa fis/jur da nota for de outra UF \(UF da SAFX04 <> UF do Estab\)

Alteração CH115852 

E somente para CFOPs de saída interestaduais <>’6301’

  
Se SAFX09, considerar zero;

Alteração OS3851 \(Junho/2012\):

Se CFOP do item for iniciado por “6” ou “7” *\(somente saídas interestaduais\)*

     O campo será preenchido com o valor do ICMS devido a outra UF 

     \(campo “104\-Valor do ICMS devido a Outra UF” criado na SAFX43 pela OS3851\) 

Obs: A condição do CFOP interestadual é apenas por uma questão de segurança, pois na verdade o campo 104 da SAFX43 foi criado especificamente para a carga do valor do ICMS devido a outra UF nos termos do Conv 52/2005, e assim, só deve ser carregado nas prestações de serviço não\-medido de TV por assinatura via satélite para outra UF\)\.

RND510\-17

Campo COD\_PART

\[OS4747\] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

RND510\-18

Campo VL\_PIS

__\[ALTERADO MFS17478\]__

Quando o parâmetro “Inibir a geração das informações constantes na EFD Contribuições \(Parâmetros > Dados Iniciais\)”  estiver marcado, este campo deve ser gerado em branco \(||\)\.

RND510\-19

Campo VL\_COFINS

__\[ALTERADO MFS17478\]__

Quando o parâmetro “Inibir a geração das informações constantes na EFD Contribuições \(Parâmetros > Dados Iniciais\)”  estiver marcado, este campo deve ser gerado em branco \(||\)\.

# Registro D520 – Complemento do Documento – Dados Adicionais \(Cód 21 e Cód 22\) 

RND520

Este registro deve ser gerado apenas nas operações de saída, e somente quando algum dos itens da nota gravada no registro D500,  tiver ICMS relativo ao valor de FECEP\. 

Gravar um único registro onde o campo 02\-VL\_FCP será a totalização do valor do imposto de todos os itens da nota\.

# Registro D530 – Terminal Faturado

RND530

Este registro deve ser gerado apenas nas operações de saída\.

Trata\-se da relação de todos os tipos de serviço que constam na nota fiscal gravada no registro __D500__\. Observar que este registro é “filho” do D500, e para gerá\-lo deverá ser feita um agrupamento dos itens conforme descrito a seguir:

Agrupar os itens da nota conforme a seguinte *combinação*:

- Tipo de Serviço                        \(novo campo da SAFX43\)
- Data Inicial da Prestação        \(novo campo da SAFX43\)
- Data Final da Prestação         \(novo campo da SAFX43\)
- Código da Área do Terminal   \(novo campo da SAFX43\)
- Terminal Faturado                   \(novo campo da SAFX43\)

Para cada combinação, gravar um registro D530\.

Nenhum desses campos é obrigatório na SAFX43\. Por isso, deve\-se ter cuidado no  tratamento dos campos, pois eles poderão estar nulos\.

Ao obter as combinações a serem gravadas no D530, deve\-se *considerar apenas *os itens que tenham* pelo menos* um dos seguintes campos preenchidos: Tipo de Serviço, Código da Área do Terminal  __ou__  Terminal Faturado \(os campos da data inicial / final podem estar nulos, pois eles não são obrigatórios no D530\)\.

Quando nenhum destes três campos estiverem preenchidos no item, o mesmo deverá ser desconsiderado do agrupamento\.  

Ao gravar o registro D530, os campos sem informação deverão ficar com ||\.  

Obs sobre o registro D530:

\-Nos documentos do GT\-Sped Fiscal não consta chave para este registro; 

\-De acordo com call realizado com Tutomo em 08/04/2008, o PVA será alterado para que os

  campos da data inicial e final da prestação deixem de ser obrigatórias; 

\-O novo campo “Indicador do Tipo de Serviço” tem relação com o código de  classificação do item \(campo 42 da SAFX43\)\. No entanto, não é seguro fazer um DE\-PARA, pois alguns códigos geram dúvida\. Por isso, a opção foi criar um novo campo para que a responsabilidade da informação fique por conta do cliente\.

RND530\-05

Campo PER\_FISCAL:

Este campo deve ser preenchido com o mês/ano da apuração do ICMS referente ao arquivo que esta sendo gerado\.

Pode\-se considerar o mês/ano da data final da escrituração, que é o campo 05\-DT\_FIN do registro de abertura do arquivo \(Registro 0000\)\.

Obs: até a versão 2\.0\.46 do PVA de teste, o Sped Fiscal deve ser gerado *para um único mês*, pois quando as datas inicial e final do registro de abertura são de meses diferentes, o validador critica\. 

# Registro D590 – Registro Analítico do Documento \(Cód 21 e Cód 22\)

RND590

Este registro é a totalização dos valores da nota fiscal, e deverá ser gerado a partir dos itens  da nota, ou no caso das notas sem item, a partir dos dados da  capa da nota\.

   

A totalização dos valores deve ser feita por:

CST\_ICMS \- Código de Situação Tributária do ICMS     

CFOP  \-  Código Fiscal de Operação                               

ALIQ\_ICMS \- Alíquota ICMS                                            

 

__Para as notas *de entrada*__* *à totalizar os valores gravados no registro D500 \(nas operações de entrada não são gerados os registros do item, o D510\), seja a partir dos itens, ou da capa, para o caso das notas sem item\.

__Valores do D590:__

__     Totalização pelo item __

__        \(SAFX08/SAFX09\)__

__     Totalização pela capa __

__               \(SAFX07\)__

CST\_ICMS

Se SAFX08 é a concatenação dos códigos das tabelas de situação estadual  "A" e "B" \(código A \+ código B\)\. Campos 30 e 31;

Se SAFX09, considerar o código  "090";

Concatenação dos códigos das tabelas de situação estadual  "A" e "B" \(código A \+ código B\)\. Campos 179 e 180\.

CFOP

Se SAFX08, campo 22;

Se SAFX09, campo 17;

Campo 14

ALIQ\_ICMS

Se SAFX08, campo 42;

Se SAFX09, considerar zero;

Campo 34

VL\_OPR

Se SAFX08, totalizar campo 64;

Se SAFX09, totalizar campo15;

Campo 23

VL\_BC\_ICMS

Se SAFX08, totalizar campo 56;

Se SAFX09, considerar zero;

Campo 51

VL\_ICMS

Se SAFX08, totalizar campo 43;

Se SAFX09, considerar zero;

Campo 35

VL\_BC\_ICMS\_ST

VL\_BC\_ICMS\_UF

Se SAFX08, totalizar campo 61;

Importante à a base de ST de cada item deve ser considerada na totalização, apenas quando o campo “78\-Apropria” da SAFX08  for =  “S”  \(IND\_CRED\_ICMSS\)\.

\(idem lógica da RNC170\-16\)

Alteração OS3471 \(Jul/11\):

Se SAFX08, totalizar campo 56, mas *somente* quando a pessoa fis/jur da nota for de outra UF \(UF da SAFX04 <> UF do Estab\)

 

E somente para CFOPs de saída interestaduais <>’6301’

Alteração CH115852 \(Jan/12\)

Se SAFX09, considerar zero;

Alteração OS3851 \(Jun/2012\):

Preencher com zero\.

\(este campo é utilizado somente  nas notas de saída\) 

Campo 64

Importante à a base  de ST deve ser considerada apenas quando o campo “82\-Apropria” da SAFX07  for =  “S”  \(IND\_CRED\_ICMSS\)

Alteração OS3471 \(Jul/11\):

Totalizar o campo 51, mas *somente* quando a pessoa fis/jur da nota for de outra UF \(UF da SAFX04 <> UF do Estab\);

E somente para CFOPs de saída interestaduais <>’6301’

Alteração CH115852 \(Jan/12\)

Alteração OS3851 \(Jun/2012\):

Preencher com zero\.

\(este campo é utilizado somente  nas notas de saída\) 

VL\_ICMS\_ST

VL\_ICMS\_UF

Se SAFX08, totalizar campo 52; 

Importante à o valor de ST de cada item deve ser considerado na totalização, apenas quando o campo “78\-Apropria” da SAFX08  for =  “S”  \(IND\_CRED\_ICMSS\)\.

\(idem lógica da RNC170\-18\)

Alteração OS3471 \(Jul/11\):

Se SAFX08, totalizar campo 43, mas *somente* quando a pessoa fis/jur da nota for de outra UF \(UF da SAFX04 <> UF do Estab\)

Alteração CH115852 

E somente para CFOPs de saída interestaduais <>’6301’

  
Se SAFX09, considerar zero;

Alteração OS3851 \(Jun/2012\):

Preencher com zero\.

\(este campo é utilizado somente  nas notas de saída\) 

Campo 48

Importante à o valor de ST deve ser considerado apenas quando o campo “82\-Apropria” da SAFX07  for =  “S”  \(IND\_CRED\_ICMSS\)\.

Alteração OS3471 \(Jul/11\):

Totalizar o campo 35, mas *somente* quando a pessoa fis/jur da nota for de outra UF \(UF da SAFX04 <> UF do Estab\);

Alteração CH115852 

E somente para CFOPs de saída interestaduais <>’6301’

Alteração OS3851 \(Jun/2012\):

Preencher com zero\.

\(este campo é utilizado somente  nas notas de saída\) 

VL\_RED\_BC

Se SAFX08, totalizar campo 57;

Se SAFX09, considerar zero;

Campo 54

 

__ Para as notas de saída__ à totalizar o valor dos itens gravados no registro D510, da

 seguinte forma:

__Valores do D590:__

__Totalização pelo item \(SAFX43\)__

CST\_ICMS

Concatenação dos códigos das tabelas de situação estadual  "A" e "B" \(código A \+ código B\)\. Campos 32 e 33\.

Obs: quando for item de serviço e os campos não estiverem preenchidos, considerar o código “090”

CFOP

Campo 13

ALIQ\_ICMS

Campo 21

VL\_OPR

Totalização do valor contábil dos itens que deverá ser calculado para cada item da seguinte forma:

Valor do serviço – Desconto \+ Outras Despesas

       \(campo 19 – campo 18 \+ campo 46\)

Observar que no registro D510 não existe campo para o valor contábil do item, pois o VL\_ITEM é apenas o valor do serviço\.Observar também que na SAFX43 não existe este valor, por isso ele terá que ser calculado \(é diferente da SAFX08, que tem os dois valores, o valor do item e o valor contábil do item\)\.

VL\_BC\_ICMS

Totalização do campo 23

VL\_ICMS

Totalização do campo 22

VL\_BC\_ICMS\_ST

VL\_BC\_ICMS\_UF

Totalização do campo 40

Obs à no caso da SAFX43 os valores de ST serão sempre totalizados, pois não existe o campo que indica se houve ou não apropriação, semelhante ao campo “78\-Apropria” da SAFX08\.

Alteração OS3471 \(Jul/11\):

Totalização do campo 23, mas *somente* quando a pessoa fis/jur da nota for de outra UF \(UF da SAFX04 <> UF do Estab\);

Alteração OS3851 \(Jun/2012\):

Totalização do campo “103\-Valor da BC do ICMS devido a outra UF”\. O campo deve ser considerado na totalização apenas quando se tratar de operação interestadual \(CFOP iniciados por “6” ou “7”, ou seja, apenas quando o mesmo for gravado no registro D510 \(vide RND510\-14\)\.

VL\_ICMS\_ST

VL\_ICMS\_UF

Totalização do campo 39 

Obs à no caso da SAFX43 os valores de ST serão sempre totalizados, pois não existe o campo que indica se houve ou não apropriação, semelhante ao campo “78\-Apropria” da SAFX08\.

Alteração OS3471 \(Jul/11\):

Totalização do campo 22, mas *somente* quando a pessoa fis/jur da nota for de outra UF \(UF da SAFX04 <> UF do Estab\);

Alteração OS3851 \(Jun/2012\):

Totalização do campo “104\-Valor do ICMS devido a outra UF”\. O campo deve ser considerado na totalização apenas quando se tratar de operação interestadual \(CFOP iniciados por “6” ou “7”, ou seja, apenas quando o mesmo for gravado no registro D510 \(vide RND510\-15\)\.

VL\_RED\_BC

Totalização do campo 26

__OBS1__: A __VAF\-MG__ a partir de 2020 passou a ser gerada com base nas regras de vários registros do SPED FISCAL \(C190, D190\.\.\.\)\. Ao realizar uma alteração na regra de geração dos registros D500 e D590, como inclusão de um modelo, um critério de recuperação da nota, um tratamento de situação especial, a regra de geração da VAF\-MG deve ser revista \(tópico 2 do MTZ\-VAFMG\_Geracao\_Relatorio\_EFD\-Fiscal\.docx\)\.

RND590\-11

\[CH31859\_2012\]

__\[ALTERADA \- CH24606\_2018 \(MFS\-21413\)\]__

Quando a UF do estabelecimento <> ‘SC’:

__Para notas de entrada__ à Recuperar a informação do campo 155 – Código da Observação da SAFX08, considerando o primeiro registro lido da combinação de itens selecionados nos critérios de agrupamento do registro\.

Quando a UF do estabelecimento <> ‘SC’:

__Para notas de saída__ à não gerar a informação\. Recuperar a informação do campo 155 – Código da Observação da SAFX08, considerando o primeiro registro lido da combinação de itens selecionados nos critérios de agrupamento do registro\.

__Campo: COD\_OBS__

\[__ALTERAÇÃO \- MFS69058__\] Tratamento para considerar o parâmetro – “Campo Código de Observação \(Considerar 6 caracteres\)” \- para truncar o campo com 6 posições, conforme Manual Guia Prático\.

__SE__ o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

__OU__

__SE__ o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

Este código deverá ser referenciado no registro 0460\.

__Registro D600 \- Consolidação da Prestação de Serviço \(Cód 21 e 22\)__

RND600

Os registros do sub\-bloco “600” \(600, 610, 620, 690\) serão gerados a partir da consolidação das notas fiscais de saída\. A origem destes registros é a mesma do sub\-bloco D500, a diferença é que no D600 o movimento será consolidado\. 

Obs: As notas canceladas não precisam ser consideradas na consolidação \(no D500 estas notas são escrituradas sem os valores\)\.

Para geração destes registros o movimento da SAFX42/SAFX43 deverá ser consolidado pelos seguintes critérios:

- Modelo \(campo 13 da SAFX42\)
- Município dos Terminais Faturados \(campo 76 da SAFX42\)
- Série \(campo 07 da SAFX42\)
- Subsérie \(campo 08 da SAFX42\)
- Classe de Consumo \(campo 63 da SAFX42\)
- Data de Emissão \(campo 03 da SAFX42\)

Assim, as notas emitidas numa mesma data que tenham o mesmo modelo, município faturado, série/subsérie e classe de consumo irão gerar um único registro D600\.

Critérios de seleção das notas:

- Modelo \(campo “13 – Modelo de Documento”\) = 21 ou 22;
- Data Fiscal \(campo 03\) \- enquadrada no período de geração, ou notas com data extemporânea enquadrada no período de geração;
- Não considerar os itens informativos \(itens da SAFX43 com o campo 10\-Tipo de Item = 1\)

Importante: Observar que os campos de modelo, município e classe de consumo não são obrigatórios, e por isso poderão estar nulos\. Neste caso, deve\-se considerar o registro numa linha de consolidação com a informação = “||’, ou seja, sem informação\. Além disso, deverá ser gravado no log uma mensagem informando a falta do dado no documento fiscal\. 

Exemplo:

- Campo “Modelo de Documento” não preenchido no documento fiscal\. Esta informação é essencial para gerar a consolidação dos documentos no registro D600\.
- Campo “Município do Ponto de Consumo” não preenchido no documento fiscal\. Esta informação é essencial para gerar a consolidação dos documentos no registro D600\.
- Campo “Classe de Consumo” não preenchido no documento fiscal\. Esta informação é essencial para gerar a consolidação dos documentos no registro D600\.

__OBS1__: Na geração por Inscrição Estadual Única, deve\-se considerar os documentos fiscais de todos os Estabelecimentos envolvidos na centralização \(OS2388\-O1ge\);

__OBS2__ Este registro não é gerado na opção “Geração – PIM” \(ver detalhes nas __OS2388\-AM\*__,  que definiram a geração do Sped Fiscal para o PIM\)\.

__OBS3__: A __VAF\-MG __a partir de 2020 passou a ser gerada com base nas regras de vários registros do SPED FISCAL \(C190, D190\.\.\.\)\. Ao realizar uma alteração na regra de geração dos registros D600 e D690, como inclusão de um modelo, um critério de recuperação da nota, um tratamento de situação especial, a regra de geração da VAF\-MG deve ser revista \(tópico 2 do MTZ\-VAFMG\_Geracao\_Relatorio\_EFD\-Fiscal\.docx\)\.

RND600\-17

Campo VL\_PIS

__\[ALTERADO MFS17478\]__

Quando o parâmetro “Inibir a geração das informações constantes na EFD Contribuições \(Parâmetros > Dados Iniciais\)”  estiver marcado, este campo deve ser gerado em branco \(||\)\.

RND600\-18

Campo VL\_COFINS

__\[ALTERADO MFS17478\]__

Quando o parâmetro “Inibir a geração das informações constantes na EFD Contribuições \(Parâmetros > Dados Iniciais\)”  estiver marcado, este campo deve ser gerado em branco \(||\)\.

__Registro D610 \- Itens do Documento Consolidado__

RND610

Neste registro serão gravados os itens dos documentos consolidados no registro D600\.

Todos os itens referentes ao registro consolidado gravado no D600 deverão ser  consolidados por produto/serviço \(COD\_ITEM\), e seus valores serão  totalizados\.

Importante: Apesar da chave deste registro ser apenas o código do produto/serviço, a consolidação deve considerar também outras informações, já que o mesmo produto/serviço poderá ter por exemplo CFOP’s diferentes em documentos distintos\. 

O layout, e também as regras do PVA, sugerem que o mesmo produto/serviço terá sempre o mesmo CFOP, código CST\_ICMS e código da classificação do ítem\. No entanto, isso pode não acontecer, e neste caso devemos registrar os diferentes CFOP’s, códigos CST ou códigos de classificação do item\. Desta forma, permitiremos ao usuário identificar um possível erro\. 

Assim, os itens de todos os documentos consolidados no registro D600 deverão ser  agrupados por:

- Produto/serviço \(COD\_ITEM\)
- Código de classificação do item \(COD\_CLASS\)
- Unidade de medida \(UNID\)
- CST\_ICMS
- CFOP
- Alíquota do ICMS \(ALIQ\_ICMS\)
- Código da Conta \(COD\_CTA\)

RND610\-03

Campo 03\-COD\_ITEM:

Preencher com o código do produto ou o código do serviço, dependendo da classificação do item \(campo 47\-Classificação do Documento Fiscal da SAFX43\):

Se item de mercadoria à campos 11/12 \(Indicador e Código do Produto\) da SAFX43

Se item de serviço à campo 48\-Código do Serviço da SAFX43

Alteração OS2667, Dez/2008:

Se item de serviço à gravar o Código do Serviço \(campo 48\) ou a natureza do serviço \(campo 8 da SAFX2018\), conforme parâmetro que indica a informação a ser gravada \(“Dados Iniciais”\) 

O campo deve ser preenchido de acordo com a regra descrita para o registro C170 \(vide regra RNC170\-03\)\.

\[Alteração – OS 3217\-A\]

Buscar a informação no campo  “Código da Natureza do Serviço – SPED FISCAL” da SAFX2018 quando houver preenchimento\.  

RND610\-05

Campo 05\-UNID:

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

RND610\-13

Campo 13\-VL\_BC\_ICMS\_UF:

Se SAFX08, totalizar campo 56, mas *somente* quando a pessoa fis/jur da nota for de outra UF \(UF da SAFX04 <> UF do Estab\)

 

Alteração CH115852 

E somente para CFOPs de saída interestaduais <>’6301’

Se SAFX09, considerar zero;

Alteração OS3851 \(Junho/2012\):

Se CFOP da consolidação for iniciado por “6” ou “7” *\(somente saídas interestaduais\)*

     O campo será preenchido com a totalização do campo “103\-Valor da BC do ICMS 

     devido a Outra UF” dos itens consolidados \(campo criado na SAFX43 pela OS3851\) 

Obs: A condição do CFOP interestadual é apenas por uma questão de segurança, pois na verdade o campo 103 da SAFX43 foi criado especificamente para a carga da base do ICMS devido a outra UF nos termos do Conv 52/2005, e assim, só deve ser carregado nas prestações de serviço não\-medido de TV por assinatura via satélite para outra UF\.__ __

RND610\-14

Campo 14\-VL\_ICMS\_UF:

Se SAFX08, totalizar campo 43, mas *somente* quando a pessoa fis/jur da nota for de outra UF \(UF da SAFX04 <> UF do Estab\)

Alteração CH115852 

E somente para CFOPs de saída interestaduais <>’6301’

  
Se SAFX09, considerar zero;

Alteração OS3851 \(Junho/2012\):

Se CFOP da consolidação for iniciado por “6” ou “7” *\(somente saídas interestaduais\)*

     O campo será preenchido com a totalização do campo “104\-Valor do ICMS devido

      a Outra UF” dos itens consolidados \(campo criado na SAFX43 pela OS3851\) 

Obs: A condição do CFOP interestadual é apenas por uma questão de segurança, pois na verdade o campo 104 da SAFX43 foi criado especificamente para a carga do valor do ICMS devido a outra UF nos termos do Conv 52/2005, e assim, só deve ser carregado nas prestações de serviço não\-medido de TV por assinatura via satélite para outra UF\.

RND610\-16

Campo VL\_PIS

__\[ALTERADO MFS17478\]__

Quando o parâmetro “Inibir a geração das informações constantes na EFD Contribuições \(Parâmetros > Dados Iniciais\)”  estiver marcado, este campo deve ser gerado em branco \(||\)\.

RND610\-17

Campo VL\_COFINS

__\[ALTERADO MFS17478\]__

Quando o parâmetro “Inibir a geração das informações constantes na EFD Contribuições \(Parâmetros > Dados Iniciais\)”  estiver marcado, este campo deve ser gerado em branco \(||\)\.

__Registro D620 \- Complemento do Documento – Dados Adicionais__

RND620

Este registro deve ser gerado apenas nas operações de saída, e somente quando algum dos itens dos documentos consolidadas no registro D600,  tiverem valor de ICMS relativo ao valor de FECEP\. 

Poderão ser gravados até dois registros D620:

- um com a totalização do valor do FECEP de todos os itens das notas cuja pessoa física/jurídica *é participante *do Programa Fome Zero totalizado;
- um com a totalização do valor do FECEP de todos os itens das notas cuja pessoa física/jurídica *não é participante* do Programa Fome Zero totalizado;

__Registro D690 \- Registro Analítico dos Documentos__

RND690

Este registro é a totalização dos valores dos documentos fiscais consolidados no registro D600, e deverá ser gerado a partir dos itens gravados no D610, agrupados por:

   

CST\_ICMS \- Código de Situação Tributária do ICMS     

CFOP  \-  Código Fiscal de Operação                               

ALIQ\_ICMS \- Alíquota ICMS                                            

Para a totalização dos valores seguir a mesma regra definida para o registro D590\.

__OBS1__: A __VAF\-MG__ a partir de 2020 passou a ser gerada com base nas regras de vários registros do SPED FISCAL \(C190, D190\.\.\.\)\. Ao realizar uma alteração na regra de geração dos registros D600 e D690, como inclusão de um modelo, um critério de recuperação da nota, um tratamento de situação especial, a regra de geração da VAF\-MG deve ser revista \(tópico 2 do MTZ\-VAFMG\_Geracao\_Relatorio\_EFD\-Fiscal\.docx\)\.

RND690\-08

Campo 08\-VL\_BC\_ICMS\_UF

Totalização do campo 23, mas *somente* quando a pessoa fis/jur da nota for de outra UF \(UF da SAFX04 <> UF do Estab\);

Alteração CH115852 

E somente para CFOPs de saída interestaduais <>’6301’

Alteração OS3851 \(Jun/2012\):

Totalização do campo “103\-Valor da BC do ICMS devido a outra UF”\. O campo deve ser considerado na totalização apenas quando se tratar de operação interestadual \(CFOP iniciados por “6” ou “7”, ou seja, apenas quando o mesmo for gravado no registro D610 \(vide RND610\-13\)\.

RND690\-09

Campo 09\-VL\_ICMS\_UF

Totalização do campo 22, mas *somente* quando a pessoa fis/jur da nota for de outra UF \(UF da SAFX04 <> UF do Estab\);

Alteração CH115852 

E somente para CFOPs de saída interestaduais <>’6301’

Alteração OS3851 \(Jun/2012\):

Totalização do campo “104\-Valor do ICMS devido a outra UF”\. O campo deve ser considerado na totalização apenas quando se tratar de operação interestadual \(CFOP iniciados por “6” ou “7”, ou seja, apenas quando o mesmo for gravado no registro D610 \(vide RND610\-14\)\.

RND690\-11

__Campo: COD\_OBS__

Recuperar a informação do campo 155 – Código da Observação da SAFX08\.

\[__ALTERAÇÃO \- MFS69058__\] Tratamento para considerar o parâmetro – “Campo Código de Observação \(Considerar 6 caracteres\)” \- para truncar o campo com 6 posições, conforme Manual Guia Prático\.

__SE__ o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

__OU__

__SE__ o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

Este código deverá ser referenciado no registro 0460\.

__Registros D695 \- Consolidação da Prestação de Serviço \(Cód 21 e 22\)__

RND695

Nos registros D695 e D696 serão demonstrados os dados das notas fiscais de saída, modelo 21 e 22, emitidas em via única, e somente das Empresas que são obrigadas a atender ao Convênio 115/03\.

As informações deste registro D695 são exatamente os dados de identificação de cada um dos volumes do arquivo Mestre gerados no Convênio 115\. 

Os dados para gravação deste registro serão obtidos a partir da tabela que armazena os dados sobre cada volume de arquivo “Mestre” gerado para o Convênio 115 \(tabela ICT\_MM\_CONV115\)\. Desta forma, será necessário que todos os procedimentos de geração do Convênio 115 sejam executados antes de gerar o Sped Fiscal\.

Deve ser gerado um registro D695 para cada volume de arquivo Mestre do Convênio 115\.

\(este registro equivale ao registro C700, só que trata as operações de Telecom\) 

__OBS1__: na geração por Inscrição Estadual Única, deve\-se recuperar os dados de identificação de cada um dos volumes de arquivo do Convênio 115 gerados por todos os estabelecimentos envolvidos na centralização\.

__OBS2__: Este registro não é gerado na opção “Geração – PIM” \(ver detalhes nas __OS2388\-AM\*__,  que definiram a geração do Sped Fiscal para o PIM\)\.

__OBS3:__ Alteração da __OS4786__: A partir desta OS, os arquivos do Conv\.115 passaram a ser gerados por Série e Modelo\. Como o modelo *não* faz parte do nome do arquivo, poderão existir arquivos de mesmo nome, mas conteúdo diferente, sendo um para cada modelo \(modelo 21 e 22 por exemplo\)\. Na prática, os procedimentos realizados na geração do Sped *não* tiveram alterações em seu funcionamento, apenas os ajustes internos, necessários p/o tratamento das tabelas que contém os dados do Convênio \(são as tabelas “ICT\_MM\_CONV115”\)\.

__OBS4__: A __VAF\-MG__ a partir de 2020 passou a ser gerada com base nas regras de vários registros do SPED FISCAL \(C190, D190\.\.\.\)\. Ao realizar uma alteração na regra de geração dos registros D695 e D696, como inclusão de um modelo, um critério de recuperação da nota, um tratamento de situação especial, a regra de geração da VAF\-MG deve ser revista \(tópico 2 do MTZ\-VAFMG\_Geracao\_Relatorio\_EFD\-Fiscal\.docx\)\.

__RND695\-08__

__Campo NOM\_MEST:__

__Alteração MFS7429__ \(Outubro/2016\): 

Por causa do tamanho do nome do arquivo, está gerando erro de processamento na geração do Sped, quando ultrapassado o tamanho de 15 posições\. Devido esse problema, o sistema deve efetuar o seguinte tratamento com mensagem no Log:

__Alteração MFS8257__ \(a mensagem passou a ser gerada apenas p/ períodos anteriores à Jan/2017\):

\- __Se __campo 8 “NOM\_MEST” for gerado com mais de 15 posições, e o período da geração for inferior à JAN/2017, o sistema deverá exibir a seguinte mensagem no Log:  

__        “O campo NOM\_MEST ultrapassou o tamanho máximo permitido \(15 posições\)”__

__Registros D696 \- Registro Analítico dos Documentos __

RND696

Este registro é “filho” do __D695__ e mostra a totalização dos valores dos documentos fiscais que constam no volume do arquivo Mestre do Convênio 115, agrupados por CST, CFOP e ALÍQUOTA\.

Observação sobre a totalização dos valores realizada na geração do Conv\. 115:

Para geração dos registros D696 e D697, a geração do Convênio 115 gera estes valores durante a leitura das notas de um volume de arquivo, para que os valores sejam acumulados por:

- CST\_ICMS \- Código de Situação Tributária do ICMS 
- CFOP  \-  Código Fiscal de Operação 
- ALIQ\_ICMS \- Alíquota ICMS  
- UF – UF da pessoa fis/jur

No registro D696 são apresentados os valores totalizados apenas por CST, CFOP e ALÍQUOTA, mas no D697 são apresentados valores totalizados por UF\. Por isso, a geração do Convênio faz a totalização dos valores considerando também a UF\.

Obs: Na OS3851 a geração do Convênio 115 foi novamente alterada para totalizar os valores dos novos campos 103 e 104 da SAFX43, para possibilitar a gravação dos campos 08\-VL\_BC\_ICMS\_UF e 09\-VL\_ICMS\_UF do registro D696\. 

\[Alterado MFS20217\]:

\[Alterado CH16400\_2013\]

Quando se tratar de documentos fiscais cancelados, cuja a data de cancelamento esteja compreendida dentro do mês de emissão do documento,esses registros devem ser desconsiderados e não deverão ser apresentados no registro D696\. somente devem ser gerados os campos 01, 02, 03 e 04 do registro D696\. Os campos 05, 06, 07, 08, 09 e 10 devem ser gerados com valor zero\.

Lembrando que este registro é um consolidador de informação por CST, CFOP e Alíquota, então, se tivermos informações que atendam ao mesmo critério de consolidação com documentos cancelados e não cancelados, os valores dos documentos cancelados devem ser zerados na totalização \(registro D695\)\.

__OBS1__: Alteração da __OS4786__: A partir desta OS, os arquivos do Conv\.115 passaram a ser gerados por Série e Modelo\. Como o modelo *não* faz parte do nome do arquivo, poderão existir arquivos de mesmo nome, mas conteúdo diferente, sendo um para cada modelo \(modelo 21 e 22 por exemplo\)\. Na prática, os procedimentos realizados na geração do Sped *não* tiveram alterações em seu funcionamento, apenas os ajustes internos, necessários p/o tratamento das tabelas que contém os dados do Convênio \(são as tabelas “ICT\_MM\_CONV115”\)\.

__OBS2__: A __VAF\-MG__ a partir de 2020 passou a ser gerada com base nas regras de vários registros do SPED FISCAL \(C190, D190\.\.\.\)\. Ao realizar uma alteração na regra de geração dos registros D695 e D696, como inclusão de um modelo, um critério de recuperação da nota, um tratamento de situação especial, a regra de geração da VAF\-MG deve ser revista \(tópico 2 do MTZ\-VAFMG\_Geracao\_Relatorio\_EFD\-Fiscal\.docx\)\.

RND696\-08

Campo 08\-VL\_BC\_ICMS\_UF

Alteração OS3471 \(Jul/11\):

Totalização do campo 23, mas *somente* quando a pessoa fis/jur da nota for de outra UF \(UF da SAFX04 <> UF do Estab\);

Alteração CH115852:

E somente para CFOPs de saída interestaduais <>’6301’

Alteração OS3851 \(Jun/2012\):

Totalização do campo “103\-Valor da BC do ICMS devido a outra UF”\. Na totalização dos valores \(que é realizada na geração do Conv\.115\) o conteúdo deste campo será considerado apenas nas operações interestaduais \(CFOP iniciados por “6” ou “7”\)\. \(ver comentário sobre essa condição na RND510\-14\)\.

RND696\-09

Campo 09\-VL\_ICMS\_UF

Alteração OS3471 \(Jul/11\):

Totalização do campo 22, mas *somente* quando a pessoa fis/jur da nota for de outra UF \(UF da SAFX04 <> UF do Estab\);

Alteração CH115852:

E somente para CFOPs de saída interestaduais <>’6301’

Alteração OS3851 \(Jun/2012\):

Totalização do campo “104\-Valor do ICMS devido a outra UF”\. Na totalização dos valores \(que é realizada na geração do Conv\.115\) o conteúdo deste campo será considerado apenas nas operações interestaduais \(CFOP iniciados por “6” ou “7”\)\. \(ver comentário sobre essa condição na RND510\-15\)\.

RND696\-11

__Campo: COD\_OBS__

__Para notas de entrada__ à Recuperar a informação do campo 178 – Código da Observação da SAFX07\.

__Para notas de saída__ à Recuperar a informação do campo 66 – Código da Observação da SAFX42\.

\[__ALTERAÇÃO \- MFS69058__\] Tratamento para considerar o parâmetro – “Campo Código de Observação \(Considerar 6 caracteres\)” \- para truncar o campo com 6 posições, conforme Manual Guia Prático\.

__SE__ o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

__OU__

__SE__ o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

Este código deverá ser referenciado no registro 0460\.

# Registros D697 – Informações do ICMS\-ST por UF

__Registros D697 – Registro de Informações de Outras UF’s, relativamente __

__aos serviços “não\-medidos” de TV por assinatura via satélite __

A descrição do D697 foi alterada no Guia Prático vrs 2\.0\.4, assim como o conteúdo das informações a serem demonstradas\. A alteração foi realizada pela OS3335\-A, Jul/2011\.

RND697

Este registro é “filho” do __D696__, e mostra a totalização dos valores de ICMS\-ST agrupados por UF\. Assim, para cada registro __D696__ poderão existir “n” registros __D697__, um para cada UF que tenha movimentação de ICMS\-ST\.

\(alteração do Guia Prático vrs 2\.0\.4, OS3335\-A, Jul/2011\)

\(ao invés de ICMS\-ST, esse registro passou a demonstrar os valores do ICMS\)

Este registro é “filho” do __D696__, e mostra a totalização dos valores de ICMS agrupados por UF\. Assim, para cada registro __D696__ poderão existir “n” registros __D697\.__

Alteração da OS3851, Jun/2012:

*\(ao invés dos valores do ICMS, esse registro passou a demonstrar os valores do ICMS devido a outras UF’s, utilizando os novos campos 103 e 104 da SAFX43\)*

 

Este registro é “filho” do __D696__, e mostra a totalização dos valores de *ICMS devido a outra UF* agrupados por UF\. Assim, para cada registro __D696__ poderão existir “n” registros __D697\.__

A UF a ser considerada na totalização é a UF da pessoa fis/jur do documento \(SAFX42\)

Para geração deste registro, a geração do Convênio 115 gera estes totais durante a leitura das notas de um volume de arquivo \( valores acumulados por CST/CFOP/ALIQ e UF\)\.

\(ver observação sobre a geração do Conv\. 115 na RND696\)\.

Alteração da __OS4786__: A partir desta OS, os arquivos do Conv\.115 passaram a ser gerados por Série e Modelo\. Como o modelo *não* faz parte do nome do arquivo, poderão existir arquivos de mesmo nome, mas conteúdo diferente, sendo um para cada modelo \(modelo 21 e 22 por exemplo\)\. Na prática, os procedimentos realizados na geração do Sped *não* tiveram alterações em seu funcionamento, apenas os ajustes internos, necessários p/o tratamento das tabelas que contém os dados do Convênio \(são as tabelas “ICT\_MM\_CONV115”\)\.

__Registro D700 – NF Fatura Eletrônica de Serviços de Comunicação – NFCom \(Cód 62\) __

RND700

__MFS96211 \- AC 21/2022, nova versão 1\.16, Jan/2023__

MFS580250 – versão 1\.17, Jan/2024: tratamento para notas de entradas\.

MFS577999 – versão 1\.17, Jan/2024: tratamento para notas de saídas\.

__MFS690865__: Valor do serviço dos Itens Informativos \(10\-Tipo de Item da SAFX43 = ‘1’\) deve compor o campo 14 – VL\_SERV\_NT

__MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

Versão 1\.16 cria os registros relacionados a NFCom \(nota eletrônica de serviços de comunicação, modelo 62\)\.

__Regras baseadas no D500 \(modelo 22\)__

__Sub\-blocos relacionados a NFCom:__

Os registros dos Sub\-blocos __D700__ e __D750__ pertencem aos dois perfis A e B, uma vez que os dois registros podem estar gerados simultaneamente\.

No sub\-bloco D700 \(D730, D731, D735, D737\) serão apresentadas as notas fiscais isoladamente \(não consolidadas\)\. Já no sub\-bloco D750 \(D760, D761\) são apresentadas as notas de saída emitidas com finalidade Normal de forma consolidadas, quando a UF determinar\. Uma nota não é gerada nos dois sub\-blocos simultaneamente\. Notas entradas, por exemplo, só podem ser geradas no D700 e filhos\. Apenas notas de saídas de finalidade Normal, __não__ sendo de regime especial ou norma específica e que __não__ possuam Ajustes de Apuração por Documento utilizando tabela 5\.3 do SPED, podem ser geradas no D700 ou no D750, a decisão para qual dos registros gerar, depende de cada UF\. 

A geração das notas no __D700 \(D730, D731, D735, D737\)__ deve seguir a lógica:

\- As notas de Entrada sempre são escrituradas individualizadas nos registros D700 e “filhos”\.

\- As notas Saídas com Finalidade da Emissão \(campo 126 da SAFX42\) = 2\-Substituição e 3\-Normal com ajustes, sempre são escrituradas individualizadas nos registros D700 e “filhos”\.

\[MFS577999\] versão 1\.17 – Jan/2024

\- As notas Saídas baseadas em regime especial ou norma específica \(campo 83 \- IND\_NF\_REG\_ESP da SAFX42 = ‘S’, COD\_SIT do D700 = “08”\), sempre são escrituradas individualizadas nos registros D700 e “filhos”\.

\- As notas Saídas que __tenham__ registros de Ajustes de Apuração por Documento utilizando tabela 5\.3 do SPED, sempre são escrituradas individualizadas nos registros D700 e “filhos”\.

\[MFS577999\] versão 1\.17 – Jan/2024

\- As notas de Saídas com Finalidade da Emissão \(campo 126 da SAFX42\) = 1 – Normal, que __não __sejam baseadas em regime especial ou norma específica \(campo 83 \- IND\_NF\_REG\_ESP da SAFX42  = ‘N’, COD\_SIT do D700 = “00”\) e que __não__ tenham registros de Ajustes de Apuração por Documento utilizando tabela 5\.3 do SPED, de acordo com a determinação das UF’s, podem ser escrituradas de forma consolidada nos registros D750 e “filhos” ou de forma individualizadas nos registros D700 e “filhos”\. Se o registro D750 estiver marcado no perfil, essas notas serão escrituradas no D750 e não no D700\.  Caso contrário, serão escrituradas no D700 junto com as demais notas de modelo 62\.

__Sub\-bloco D700 \(D730, D731, D735, D737\)__ __– Origem das Informações:__

A geração dos dados do sub\-bloco D700 \(D730, D731, D735, D737\) tem origens distintas, dependendo do tipo da operação, se entrada ou saída\.

Geração das Notas de Entrada à os dados serão recuperados nas tabelas SAFX07, SAFX08 e SAFX09, considerando apenas as notas com código de modelo = 62\.

\(para as entradas, alguns valores poderão ser recuperados da capa, caso a nota não tenha itens\)\. 

Critérios de seleção das notas:

- Modelo \(campo “13 – Modelo de Documento” da SAFX07\) = 62;
- Notas não canceladas \(campo “30 \- Situação da Nota” da SAFX07\) <> S;
- Movimento Entrada/Saída \(campo 03 da SAFX07\) <> ‘9’
- Classificação \(campo “12 – Classificação do documento” da SAFX07\) = 1 ou 3;
- Data \(data fiscal\) enquadrada no período de geração;

\[MFS580250\] versão 1\.17 – Jan/2024

- Aplicar esse critério para gerações com leiaute a partir da EFD117 \(CAD\_LAYOUT – COD\_VERSAO>=117\): não considerar notas fiscais onde todos os itens não tenham CST \(campos 30 e 31 da SAFX08 não preenchidos\); \(\*\)

Nota\-se que não estão sendo consideradas as datas extemporâneas pois o campo 06\- COD\_SIT do D700 não contempla o código de notas extemporâneas\. 

Geração das Notas de Saída à os dados serão recuperados nas tabelas SAFX42 e SAFX43, considerando apenas modelo ‘62’\. As notas de Utilities das tabelas SAFX42/43 sempre têm itens\. 

Critérios de seleção das notas:

- Modelo \(campo “13 – Modelo de Documento” da SAFX42\) = 62;
- Notas não canceladas \(campo “21 \- Situação da Nota” da SAFX42\) <> S;
- Data Fiscal \(campo 03 da SAFX42\) \- enquadrada no período de geração;

__             __

- Não considerar os itens informativos \(itens da SAFX43 com o campo 10\-Tipo de Item = 1\);    __MFS690865__: retira esse critério para que os itens informativos sejam recuperados para compor o valor do campo 14 – VL\_SERV\_NT

\[MFS577999\] versão 1\.17 – Jan/2024:

- Não considerar notas fiscais onde todos os itens não tenham CST \(campos 32 e 33 da SAFX43 não preenchidos\); \(\*\)
- Caso o registro __D750__ esteja selecionado no perfil para geração, __NÃO__ considerar as notas que serão consolidadas no D750, ou seja, aquelas que atendam aos três critérios abaixo:

              > Finalidade da Emissão \(campo 126 da SAFX42\) = 1 – Normal;

\[MFS577999\] versão 1\.17 – Jan/2024:

> __Não __seja baseada em regime especial ou norma específica \(campo 83 \- IND\_NF\_REG\_ESP da SAFX42  = ‘N’\); 

              > __Não__ tenha registros de Ajustes de Apuração por Documento utilizando tabela 

 5\.3 do SPED\. Ou seja, não tenha registros na tabela SAFX293 \(Observações do Documento Fiscal \- Utilities\), com indicador = “L” \(coluna IND\_ICOMPL\_LANCTO\)\.

__OBS1__: Na geração por Inscrição Estadual Única, deve\-se considerar os documentos fiscais de entrada \(SAFX07\) e saída \(SAFX42\) de todos os Estabelecimentos envolvidos na centralização;

__OBS2: __Na geração da opção “Geração – PIM”, são tratadas apenas as operações de entrada deste registro\. São consideradas apenas as notas da inscrição estadual em questão, já que os usuários do PIM devem gerar um arquivo para cada inscrição estadual\. As operações de saídas não foram tratadas para esta opção \(ver detalhes nas __OS2388\-AM\*__, que definiram a geração do Sped Fiscal para o PIM\)\.

\[MFS580250\] versão 1\.17 – Jan/2024:

__Tratamento Especial para NF Baseada em Regime Especial ou Norma Específica:__

Se o campo COD\_SIT = 08 \- NF Baseada em Regime Especial ou Norma Específica, somente os campos REG, IND\_OPER, IND\_EMIT, COD\_PART \(nas entradas\), COD\_MOD, COD\_SIT, SER, NUM\_DOC, DT\_DOC, VL\_BASE\_ICMS, VL\_ICMS serão preenchidos\. Os demais campos não serão preenchidos\. 

OBS: Os valores de base e ICMS precisam ser preenchidos, pois o validador critica quando esses não batem com o somatorio dos mesmos apresentados no D730\.

\(\*\) Versão 1\.17 – Jan/2024 diz: “A NFCom que contenha apenas itens sem a indicação de Código de Situação Tributária – CST não deve ser escriturada\.”

RND700\-03

Campo IND\_EMIT:

Para as notas de __entrada__, o conteúdo deste campo dependerá do indicador de Entrada/Saída da nota \(campo 03\-Movimento Entrada/Saída da SAFX07\), da seguinte forma:

Se indicador  = 1                  à gravar 1 \(emissão terceiros\)

Se indicador  = 2, 3, 4 ou 5  à gravar 0 \(emissão própria\)

Para as notas de __saída__ será sempre “0”\.

RND700\-04

Campo COD\_PART

Para as notas de __entrada__, origem SAFX07, campos 06/07 da SAFX07:

Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

Para as notas de __saída__, NÃO preencher o campo\.

RND700\-06

Campo COD\_SIT:

Campo preenchido com os seguintes valores:

  00 – Documento Regular;

  08 \- Documento Fiscal emitido com base em Regime Especial ou Norma Específica;

Para as notas de __entrada__, origem SAFX07, aplicar a regra:

__Se__ a nota for baseada em regime especial \(campo “232\-NF Baseada em Regime Especial ou Norma Específica” da SAFX07 = “S”\), então:

                  Gravar COD\_SIT = “08”

__Senão__:

                  Gravar COD\_SIT = “00”

Para as notas de __saída__, origem SAFX42, aplicar a regra:

__Se__ a nota for baseada em regime especial \(campo “83\- NF baseada em regime especial ou norma específica” = S\), então:

                Gravar COD\_SIT = “08”

__Senão__ 

                Gravar COD\_SIT = “00”

RND700\-10

Campo DT\_E\_S:

Para as notas de __entrada__, origem SAFX07, preencher com o campo 20\-Data Saída/Recebimento da SAFX07:

Para as notas de __saída__, NÃO preencher o campo\.

RND700\-11

Campo VL\_DOC:

MFS592577 – Retirada dos campos VL\_DA e VL\_DESC da composição do campo VL\_DOC\.

__MFS690865__: Para leiaute a partir da EFD118, considerar campo Deduções na composição do campo VL\_DOC\.

O valor do campo VL\_DOC deve ser preenchido com o resultado da expressão:

Para gerações com leiaute anterior a EFD118 \(CAD\_LAYOUT – COD\_VERSAO < 118\):

VL\_DOC = VL\_SERV \+ VL\_SERV\_NT \+ VL\_TERC

Para gerações com leiaute a partir da EFD118 \(CAD\_LAYOUT – COD\_VERSAO>=118\):

VL\_DOC = VL\_SERV \+ VL\_SERV\_NT \+ VL\_TERC \- DED

RND700\-12

Campo VL\_DESC:

Valor do Desconto\.

__MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

Para notas de __entrada__, origem SAFX07:

\- Para notas __com__ itens, totalizar o valor dos itens \(29\-Valor do Desconto da SAFX08\) \+ \(21\-Valor Desconto da SAFX09\); Desconsiderar os itens com “Grupo cClass Nfe” \(campo 264 da SAFX08\) = 110, 120 e 130\.

\- Para notas __sem__ itens, utilizar o valor da capa \(28\-Valor Descontos \- SAFX07\)\.

Para notas de __saída__, origem SAFX42:

\-  Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens\. \(18\-Valor do Desconto \- SAFX43\), considerando o IND\_ADIC\_DESC conforme regra a seguir:

__MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\):

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

      O sistema deverá  __subtrair__ do valor total o Campo 18\-Valor do Desconto \- SAFX43\.

__Senão __

      O sistema deverá __somar__ do valor total o Campo 18\-Valor do Desconto \- SAFX43\.

__Valor Negativo à  __Quando o cálculo do campo VL\_DESC resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_DESC*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

RND700\-13

Campo VL\_SERV: 

Valor do produto/serviço\. 

__\[MFS611132\] __Alteração da regra para considerar somente serviços tributados de ICMS

__MFS690865__: Valor do serviço dos Itens Informativos \(10\-Tipo de Item da SAFX43 = ‘1’\) deve compor o campo 14 – VL\_SERV\_NT e não o campo 13 – VL\_SERV\. Os itens informativos não possuem o CST preenchido\. O tratamento será aplicado aos itens sem CST, para que o valor de serviço não seja considerado no campo 13 e sim no campo 14\.

__MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

__\[MFS877470\] __Alteração da regra de preenchimento para o CST=90

Para notas de __entrada__, origem SAFX07:

\- Para notas __com__ itens, totalizar o valor dos itens \(28\-Preço do Item \- SAFX08\) \+ \(14\-Valor Serviço \-SAFX09, apenas os itens com campo COD\_SITUACAO\_B da tabela __SAFX08__ preenchido e __diferente__ de “30” ou “40” ou ”41” ou “50” ou “51” ou “90\*\*”\. Desconsiderar os itens com “Grupo cClass Nfe” \(campo 264 da SAFX08\) = 110, 120 e 130\.

\- Para notas __sem__ itens, utilizar o valor da capa \(22\-Valor do Produto/Serviço \- SAFX07\), apenas as notas com campo COD\_SITUACAO\_B da tabela __SAFX07__ preenchido e __diferente__ de “30” ou “40” ou ”41” ou “50” ou “51” ou “90\*\*”\.

\*\* CST=90 🡪 Se o COD\_SITUACAO\_B for igual a “90”, deve\-se verificar se o campo Valor do ICMS da capa ou do item está preenchido \(Campo 35\-VLR\_ICMS da SAFX07 ou Campo 43\-VLR\_ICMS da SAFX08\)\.  Se o valor do ICMS estiver preenchido, o campo VL\_SERV deve ser preenchido conforme as regras acima, mesmo quando o COD\_SITUACAO\_B for igual a “90”\. 

Para notas de __saída__, origem SAFX42:

\-  Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens \(19\-Valor dos Serviços \- SAFX43\), apenas as notas com campo COD\_SIT\_TRIB\_B da tabela __SAFX43__ preenchido e __diferente__ de “30” ou “40” ou ”41” ou “50” ou “51” ou “90\*\*\*”, considerando o IND\_ADIC\_DESC conforme regra a seguir:

__MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\):

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

      O sistema deverá  __subtrair__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

__Senão __

      O sistema deverá __somar__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

\*\*\* CST=90 🡪 Se o COD\_SITUACAO\_B for igual a “90”, deve\-se verificar se o campo Valor do ICMS do item está preenchido \(Campo 22\- VLR\_TRIB\_ICMS da SAFX43\)\.  Se o valor do ICMS estiver preenchido, o campo VL\_SERV deve ser preenchido conforme as regras acima, mesmo quando o COD\_SITUACAO\_B for igual a “90”\. 

__Valor Negativo à  __Quando o cálculo do campo VL\_SERV resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_SERV*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

RND700\-14

Campo VL\_SERV\_NT: valor dos serviços não tributados pelo ICMS

__\[MFS611132\] __Alteração da regra para considerar somente serviços tributados de ICMS\.  Conforme verificado com a área de informação, quando a nota tem redução de base de ICMS, é considerado tributado pelo ICMS\.  Portanto, o valor deve ser considerado no campo 13\-VL\_SERV\.

__MFS690865__: Valor do serviço dos Itens Informativos \(10\-Tipo de Item da SAFX43 = ‘1’\) deve compor o campo 14 – VL\_SERV\_NT e não o campo 13 – VL\_SERV\. Os itens informativos não possuem o CST preenchido\. O tratamento será aplicado aos itens sem CST, para que o valor de serviço não seja considerado no campo 13 e sim no campo 14\.

__MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

__\[MFS1000266\]__ Tratamento dos itens de dedução que não devem ser considerados no valor de serviço não tributado \(Grupo cClass Nfe” \(campo 264 da SAFX08\) = 590\)\.

Para notas de __entrada__, origem SAFX07:

\- Para notas __com__ itens, preencher com a soma dos valores dos itens de Mercadoria SAFX08 __\(a, b\) __e de Serviço SAFX09 __\(c\):__

__\(a\)__ Valores das bases isenta/não tributada \+ base outras da __SAFX08;__

__\+__

__\(b\)__ Valor do Item da __SAFX08;__

__\+__

__\(c\)__ Valor dos itens de serviço da __SAFX09;__

Onde:

 \- Para __\(a\)__, considerar \[campos 56 \(se campo 55 = 2 ou 3\) \+ campo 57\] da SAFX08, apenas quando o campo COD\_SITUACAO\_B da tabela __SAFX08__ __igual__ à “30”, “40”,”41”, “50”, “51” ou “90”\. Desconsiderar os itens com “Grupo cClass Nfe” \(campo 264 da SAFX08\) = 110, 120, 130 e 590\.

\- Para __\(b\)__, considerar campo 28\-Preço do Item \(VLR\_ITEM\) da SAFX08, apenas quando o campo COD\_SITUACAO\_B da tabela __SAFX08__ não estiver preenchido\. Desconsiderar os itens com “Grupo cClass Nfe” \(campo 264 da SAFX08\) = 110, 120, 130 e 590\.

 \- Para __\(c\)__ considerar o campo 14 da __SAFX09__\.

\- Para notas __sem__ itens, preencher com a soma dos valores das bases isenta/não tributada \+ base outras da capa \(campo 52 \+ 53 da SAFX07\), apenas quando o campo COD\_SITUACAO\_B da tabela __SAFX07__ for __igual__ à “30”, “40”,”41”, “50”, “51” ou “90”\. Se o campo COD\_SITUACAO\_B não estiver preenchido, utilizar o valor da capa \(22\-Valor do Produto/Serviço \- SAFX07\)\.

Para as notas de __saída __à este valor será composto da seguinte forma:

Preencher com a soma dos valores dos Itens da __SAFX43__:

__\(a\) __Valor das bases isenta/não tributada \+ base outras dos *itens de mercadoria* __SAFX43 __

__\+__

__\(b\) __Valor do serviço dos *itens de mercadoria* da __SAFX43, __

__\+__

__\(c\)__ Valor do serviço dos *itens de serviço* da __SAFX43,__

Onde:

 \- Para __\(a\)__, considerar campos 24\-Base Isenta/Não Tributada \+ campo 25\-Base Outras da __SAFX43__ dos itens de mercadoria \(campo 47 = “1”\), apenas quando o campo COD\_SITUACAO\_B da tabela __SAFX43__ for __igual__ a “30”, “40”,”41”, “50”, “51” ou “90”, considerando o IND\_ADIC\_DESC conforme regra abaixo\. Desconsiderar os itens com “Grupo cClass Nfe” \(campo 264 da SAFX08\) = 590\.

\- Para __\(b\)__, considerar campo 19\-Valor do Serviço da __SAFX43__ dos itens de mercadoria \(campo 47 = “1”\), apenas quando o campo COD\_SITUACAO\_B da tabela __SAFX43__ não estiver preenchido, considerando o IND\_ADIC\_DESC conforme regra abaixo\. Desconsiderar os itens com “Grupo cClass Nfe” \(campo 264 da SAFX08\) = 590\.

 

\- Para __\(c\)__ considerar o campo 19\-Valor do Serviço da __SAFX43__ dos itens de serviço \(campo 47 = “2”\), considerando o IND\_ADIC\_DESC conforme regra abaixo\.

__MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\):

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

       \- Para __\(a\)__:

         O sistema deverá  __subtrair__ do valor total os Campos 24\-Base Isenta/Não Tributada e

          campo 25\-Base Outras \- SAFX43\.

       \- Para __\(b\)__ e __\(c\)__:

         O sistema deverá  __subtrair__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

__Senão __

       \- Para __\(a\)__:

         O sistema deverá  __somar__ do valor total os Campos 24\-Base Isenta/Não Tributada e

          campo 25\-Base Outras \- SAFX43\.

       \- Para __\(b\)__ e __\(c\)__:

         O sistema deverá  __somar__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

__Valor Negativo à  __Quando o cálculo do campo VL\_SERV\_NT resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_SERV\_NT*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

RND700\-15

Campo VL\_TERC

__MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

__MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

Para notas de __entrada__, origem SAFX07:

\- Para notas __com__ itens, totalizar o valor dos itens \(164\-Valor de Terceiros \- SAFX08\)\. Desconsiderar os itens com “Grupo cClass Nfe” \(campo 264 da SAFX08\) = 110, 120 e 130\.

\- Para notas __sem__ itens, utilizar o valor da capa \(215\-Valor de Terceiros \- SAFX07\)\.

Para notas de __saída__, origem SAFX42:

\-  Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens \(75\-Valor de Terceiros \- SAFX43\), considerando o IND\_ADIC\_DESC conforme regra abaixo:

__MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\):

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

      O sistema deverá  __subtrair__ do valor total o Campo 75\-Valor de Terceiros \- SAFX43\.

__Senão __

      O sistema deverá __somar__ do valor total o Campo 75\-Valor de Terceiros \- SAFX43\.

__Valor Negativo à  __Quando o cálculo do campo VL\_TERC resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_TERC*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

RND700\-16

Campo VL\_DA

Para notas de __entrada__, origem SAFX07:

\- Utilizar o valor da capa \(26\-Valor de Outras Despesas \- SAFX07\)\.

Para notas de __saída__, origem SAFX42:

\-  Utilizar valor da capa \(18\-Valor Outras Despesas \- SAFX42\)\.

RND700\-17

Campo VL\_BC\_ICMS

__MFS690865__: A restrição para nas entradas desconsiderar os Grupo cClass 110, 120 e 130 não deve ser aplicada aos campos VL\_BC\_ICMS e VL\_ICMS\. Corrigir a regra retirando essa restrição\.

\[MFS580250\] versão 1\.17 – Jan/2024

Para notas de __entrada__, origem SAFX07:

\- Para notas __com__ itens, totalizar o valor dos itens \(56\-Base ICMS \- SAFX08\)\.  Desconsiderar os itens com “Grupo cClass Nfe” \(campo 264 da SAFX08\) = 110, 120 e 130\. Para gerações com leiaute a partir da EFD117 \(CAD\_LAYOUT – COD\_VERSAO>=117\), considerar apenas itens com CST preenchido \(campos 30 e 31 da SAFX08\) \(\*\)

\- Para notas __sem__ itens, utilizar o valor da capa \(51\-Base ICMS Tributada \- SAFX07\)\.

\(Regra baseada no C500\- campo 19\)

Para notas de __saída__, origem SAFX42: 

\-  Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens \(SAFX43\), considerando apenas os itens com CST preenchido \(campos 32 e 33 da SAFX43\) \(\*\), conforme regra de cálculo abaixo:

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

    __E se __o campo de CST\_ICMS for igual à ‘00’,’10’,’20’,’70’:

      O sistema deverá utilizar o Campo 23\-VLR\_BASE\_ICMS\_1 do Item para __subtrair__ do valor total do Campo VL\_BC\_ICMS\.

__Senão __

__   Se __o campo de CST\_ICMS for igual à ‘00’,’10’,’20’,’70’:

      O sistema deverá utilizar o Campo 23\-VLR\_BASE\_ICMS\_1 do Item para __somar__ ao valor total do Campo VL\_BC\_ICMS\.

__Considerar:__

IND\_ADIC\_DESC = __A__ \(O Item deverá ser somado\); 

IND\_ADIC\_DESC = __D__ \(O Item deverá ser subtraído\);

__Valor Negativo à  __Quando o cálculo do campo VL\_BC\_ICMS resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_BC\_ICMS*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

\(\*\) Versão 1\.17 – Jan/2024 determina que os itens sem CST não sejam considerados na geração dos registros D730 e D760\. Essa definição impacta os campos Base ICMS e Valor ICMS dos registros D700 e D750 que devem corresponder a soma dos valores apresentados nesses registros\. Por isso na definição desses campos, também não serão considerados os itens sem CST\.

RND700\-18

Campo VL\_ICMS

__MFS690865__: A restrição para nas entradas desconsiderar os Grupo cClass 110, 120 e 130 não deve ser aplicada aos campos VL\_BC\_ICMS e VL\_ICMS\. Corrigir a regra retirando essa restrição\.

\[MFS580250\] versão 1\.17 – Jan/2024

Para notas de __entrada__, origem SAFX07:

\- Para notas __com__ itens, totalizar o valor dos itens \(43\-Valor ICMS \- SAFX08\)\. Desconsiderar os itens com “Grupo cClass Nfe” \(campo 264 da SAFX08\) = 110, 120 e 130\. Para gerações com leiaute a partir da EFD117 \(CAD\_LAYOUT – COD\_VERSAO>=117\), considerar apenas itens com CST preenchido \(campos 30 e 31 da SAFX08\)\.

\- Para notas __sem__ itens, utilizar o valor da capa \(35\-Valor ICMS \- SAFX07\)\.

\(Regra baseada no C500\- campo 20\)

Para notas de __saída__, origem SAFX42:

\-  Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens \(SAFX43\), considerando apenas os itens com CST preenchido \(campos 32 e 33 da SAFX43\), conforme regra de cálculo abaixo:

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’;

__     E se __o campo de CST\_ICMS for igual à ‘00’,’10’,’20’,’70’:

        O sistema deverá utilizar a soma dos campos \[22\-Valor ICMS\] __\+__ \[103\-FECEP ICMS\] 

        do Item para __subtrair__ do valor total do Campo VL\_ICMS\.

__Senão __

__   Se __o campo de CST\_ICMS for igual à ‘00’,’10’,’20’,’70’:

      O sistema deverá utilizar a soma dos campos \[22\-Valor ICMS\] __\+__ \[103\-FECEP ICMS\] 

      do Item para __somar__ ao valor total do Campo VL\_ICMS\.

__Considerar:__

IND\_ADIC\_DESC = __A__ \(O Item deverá ser somado\); 

IND\_ADIC\_DESC = __D__ \(O Item deverá ser subtraído\);

__Valor Negativo à  __Quando o cálculo do campo VL\_ICMS resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_ICMS*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

RND700\-19

Campo COD\_OBS

__Para notas de entrada__ à Recuperar a informação do campo 178 – Código da Observação da SAFX07\.

__Para notas de saída__ à Recuperar a informação do campo 66 – Código da Observação da SAFX42\.

Tratamento para considerar o parâmetro – “Campo Código de Observação \(Considerar 6 caracteres\)” \- para truncar o campo com 6 posições, conforme Manual Guia Prático\.

__SE__ o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

__OU__

__SE__ o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

Este código deverá ser referenciado no registro 0450\.

RND700\-20

Campo VL\_PIS

__MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

Quando o parâmetro “Inibir a geração das informações constantes na EFD Contribuições \(Parâmetros > Dados Iniciais\)” estiver marcado, este campo deve ser gerado em branco \(||\)\. Caso contrário, o campo será preenchido conforme regra a seguir:

Para notas de __entrada__, origem SAFX07:

\- Para notas __com__ itens, totalizar o valor dos itens \(87\-Valor PIS \- SAFX08\) \+ \(48\-Valor Tributo PIS \-SAFX09\); 

\- Para notas __sem__ itens, utilizar o valor da capa \(103\-Valor PIS \- SAFX07\)\.

Para notas de __saída__, origem SAFX42:

\-  Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens \(77\-Valor PIS \- SAFX43\) considerando o IND\_ADIC\_DESC conforme regra abaixo:

__MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\):

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

      O sistema deverá  __subtrair__ do valor total o Campo 77\-Valor PIS \- SAFX43\.

__Senão __

      O sistema deverá __somar__ do valor total o Campo 77\-Valor PIS \- SAFX43\.

__Valor Negativo à  __Quando o cálculo do campo VL\_PIS resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_PIS*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

RND700\-21

Campo VL\_COFINS

__MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

Quando o parâmetro “Inibir a geração das informações constantes na EFD Contribuições \(Parâmetros > Dados Iniciais\)” estiver marcado, este campo deve ser gerado em branco \(||\)\. Caso contrário, o campo será preenchido conforme regra a seguir:

Para notas de __entrada__, origem SAFX07:

\- Para notas __com__ itens, totalizar o valor dos itens \(89\-Valor COFINS \- SAFX08\) \+ \(51\-Valor Tributo COFINS \-SAFX09\); 

\- Para notas __sem__ itens, utilizar o valor da capa \(105\-Valor COFINS \- SAFX07\)\.

Para notas de __saída__, origem SAFX42:

\-  Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens \(80\-Valor COFINS da SAFX43\), considerando o IND\_ADIC\_DESC conforme regra abaixo:

 __MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\):

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

      O sistema deverá  __subtrair__ do valor total o Campo 80\-Valor COFINS\- SAFX43\.

__Senão __

      O sistema deverá __somar__ do valor total o Campo 80\-Valor COFINS \- SAFX43\.

__Valor Negativo à  __Quando o cálculo do campo VL\_COFINS resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_COFINS*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

RND700\-23

Campo FIN\_DOCe

Para notas de __entrada__ à Preencher com a informação do campo 300\-Finalidade Emissão da Nfe da SAFX07 \(IND\_FIN\_EMISSAO\_NFE\)\.

Para notas de __saída__ à Preencher a informação do campo 126\-Finalidade Emissão da Nfe da SAFX42\.

De x Para para preenchimento do campo:

__SAFX07/ SAFX42 – campo 330/126__

__D700 – campo 23__

1\-Normal;

0 \- NFCom Normal;

2\-Substituição;

3 \- NFCom de Substituição;

3\-Normal com ajuste;

4 \- NFCom de Ajuste;

 

RND700\-25

Campo COD\_MOD\_DOC\_REF

\(Regra baseada no C500\- campo 34\)

Preencher apenas quando o campo 23 – FIN\_DOCe for igual a “3” \- NFCom de Substituição \(vide RND700\-23\), de acordo com a regra a seguir\.

Para notas de __entrada__ \(SAFX07\): 

Se o campo 300\-Finalidade Emissão da Nfe \(IND\_FIN\_EMISSAO\_NFE\) da SAFX07 for igual a “2” \-Substituição, então:

       Preencher com o campo 304\- Modelo do Documento Fiscal NF Substituída 

       \(COD\_MODELO\_NFE\_SUBST\) da SAFX07\.

       Caso o campo 304 não esteja preenchido, o registro deverá ser gravado normalmente

       e no log deve ser gravada a seguinte mensagem de aviso:

       Ver planilha de erros “Sped\_Fiscal\_Log\_Erros”, mensagem de número __375__\.

Para notas de __saída__ \(SAFX42\): 

Se o campo 126\-Finalidade Emissão da Nfe \(IND\_FIN\_EMISSAO\_NFE\) da SAFX42 for igual a “2”\- Substituição, então:

       Preencher com o campo 121\- Modelo do Documento Fiscal Substituído / 

       Complementado da SAFX42 \(COD\_MODELO\_SUBST\)\.

       Caso o campo 121 não esteja preenchido, o registro deverá ser gravado normalmente

       e no log deve ser gravada a seguinte mensagem de aviso:

       Ver planilha de erros “Sped\_Fiscal\_Log\_Erros”, mensagem de número __375__\.

Obs:

A mensagem deve seguir o padrão do log de erros do Sped Fiscal, contendo as linhas “Erro”, “Origem” e “Dados do Registro”, que identificam o campo com erro, a descrição do erro, a origem do dado no Mastersaf e a identificação da chave da nota fiscal criticada\.

RND700\-26

Campo CHV\_DOCe\_REF

\(Regra baseada no C500 – campo 30\)

Preencher apenas quando o campo 23 – FIN\_DOCe for igual a “3” \- NFCom de Substituição \(vide RND700\-23\), de acordo com a regra a seguir\.

Para notas de __entrada__ \(SAFX07\): 

Se o campo 300\-Finalidade Emissão da Nfe \(IND\_FIN\_EMISSAO\_NFE\) da SAFX07 for igual a “2” \-Substituição, então:

   Se o campo 304\- Modelo do Documento Fiscal NF Substituída 

  \(COD\_MODELO\_NFE\_SUBST\) da SAFX07 for “62” então:

       Preencher com o campo 301\-Chave de Acesso da NFe Substituída 

       \(NUM\_AUTENTIC\_NFE\_SUBST\) da SAFX07\.

       Caso o campo 301 não esteja preenchido, o registro deverá ser gravado normalmente

       e no log deve ser gravada a seguinte mensagem de aviso:

       Ver planilha de erros “Sped\_Fiscal\_Log\_Erros”, mensagem de número __376__\.

Para notas de __saída__ \(SAFX42\): 

Se o campo 126\-Finalidade Emissão da Nfe \(IND\_FIN\_EMISSAO\_NFE\) da SAFX42 for igual a “2”\- Substituição, então:

   Se o campo 121\- Modelo do Documento Fiscal Substituído / Complementado

   \(COD\_MODELO\_SUBST\) for “62”, então:

       Preencher com o campo 127\-Chave de Acesso da NFe Substituída 

      \(NUM\_AUTENTIC\_NFE\_SUBST\) da SAFX42\.

       Caso o campo 127 não esteja preenchido, o registro deverá ser gravado normalmente

       e no log deve ser gravada a seguinte mensagem de aviso:

       Ver planilha de erros “Sped\_Fiscal\_Log\_Erros”, mensagem de número __376__\.

Obs:

A mensagem deve seguir o padrão do log de erros do Sped Fiscal, contendo as linhas “Erro”, “Origem” e “Dados do Registro”, que identificam o campo com erro, a descrição do erro, a origem do dado no Mastersaf e a identificação da chave da nota fiscal criticada\.

RND700\-27

Campo HASH\_DOC\_REF

\(Regra baseada no C500 – campo 35\)

Código de autenticação digital do registro \(Convênio 115/2003\)\.

Preencher apenas quando o campo 23 – FIN\_DOCe for igual a “3” \- NFCom de Substituição \(vide RND700\-23\), de acordo com a regra a seguir\.

Para notas de __entrada__ \(SAFX07\): 

Se o campo 300\-Finalidade Emissão da Nfe \(IND\_FIN\_EMISSAO\_NFE\) da SAFX07 for igual a “2” \-Substituição, então:

   Se o campo 304\- Modelo do Documento Fiscal NF Substituída 

   \(COD\_MODELO\_NFE\_SUBST\) da SAFX07 for “21” ou “22” então:

      Se o campo 305\- Código de Autenticação Digital \(Convênio 115/2003\) NF Substituída

      \(COD\_AUTENTIC\_NFE\_SUBST\) da SAFX07, estiver preenchido então:

          Preencher com o campo 305\- Código de Autenticação Digital \(Convênio 115/2003\) 

          NF Substituída \(COD\_AUTENTIC\_NFE\_SUBST\) da SAFX07\.

Para notas de __saída__ \(SAFX42\): 

Se o campo 126\-Finalidade Emissão da Nfe \(IND\_FIN\_EMISSAO\_NFE\) da SAFX42 for igual a “2”\- Substituição, então:

   Se o campo 121\- Modelo do Documento Fiscal Substituído / Complementado 

  \(COD\_MODELO\_SUBST\) for “21” ou “22” então:

      Se o campo 128\- Código de Autenticação Digital \(Convênio 115/2003\) NF Substituída

      \(COD\_AUTENTIC\_NFE\_SUBST\) estiver preenchido então:

          Preencher com o campo 128\- Código de Autenticação Digital \(Convênio 115/2003\) 

          NF Substituída da SAFX42 \(COD\_AUTENTIC\_NFE\_SUBST\)\.

RND700\-28

Campo SER\_DOC\_REF

Série do documento fiscal referenciado\.

\(Regra baseada no C500 – campo 36\)

Preencher apenas quando o campo 23 – FIN\_DOCe for igual a “3” \- NFCom de Substituição \(vide RND700\-23\), de acordo com a regra a seguir\.

Para notas de __entrada__ \(SAFX07\): 

Se o campo 300\-Finalidade Emissão da Nfe \(IND\_FIN\_EMISSAO\_NFE\) da SAFX07 for igual a “2” \-Substituição, então:

   Se o campo 304\- Modelo do Documento Fiscal NF Substituída 

  \(COD\_MODELO\_NFE\_SUBST\) da SAFX07 for “21” ou “22” então:

      Se o campo 305\- Código de Autenticação Digital \(Convênio 115/2003\) NF Substituída

      \(COD\_AUTENTIC\_NFE\_SUBST\) da SAFX07 NÃO estiver preenchido então:

          Preencher com o campo 17\- Série do Docto\. Fiscal de Referência da SAFX07 

         \(SERIE\_DOCFIS\_REF\)\.

Para notas de __saída__ \(SAFX42\): 

Se o campo 126\-Finalidade Emissão da Nfe \(IND\_FIN\_EMISSAO\_NFE\) da SAFX42 for igual a “2”\- Substituição, então:

   Se o campo 121\- Modelo do Documento Fiscal Substituído / Complementado 

   \(COD\_MODELO\_SUBST\) for “21” ou “22” então:

      Se o campo 128\- Código de Autenticação Digital \(Convênio 115/2003\) NF Substituída

      \(COD\_AUTENTIC\_NFE\_SUBST\) NÃO estiver preenchido então:

          Preencher com o campo 120\- Série do Documento Fiscal Substituído 

         /Complementado da SAFX42 \(SERIE\_DOCFIS\_SUBST\)\.

RND700\-29

Campo NUM\_DOC\_REF

Número do documento fiscal referenciado\.

\(Regra baseada no C500 – campo 37\)

Preencher apenas quando o campo 23 – FIN\_DOCe for igual a “3” \- NFCom de Substituição \(vide RND700\-23\), de acordo com a regra a seguir\.

Para notas de __entrada__ \(SAFX07\): 

Se o campo 300\-Finalidade Emissão da Nfe \(IND\_FIN\_EMISSAO\_NFE\) da SAFX07 for igual a “2” \-Substituição, então:

   Se o campo 304\- Modelo do Documento Fiscal NF Substituída 

  \(COD\_MODELO\_NFE\_SUBST\) da SAFX07 for “21” ou “22”, então:

      Se o campo 305\- Código de Autenticação Digital \(Convênio 115/2003\) NF Substituída

      \(COD\_AUTENTIC\_NFE\_SUBST\) da SAFX07 NÃO estiver preenchido então:

          Preencher com o campo 16\- Número do Docto\. Fiscal de Referência da SAFX07 

         \(NUM\_DOCFIS\_REF\)\.

          Caso o campo 16 não esteja preenchido, o registro deverá ser gravado normalmente

          e no log deve ser gravada a seguinte mensagem de aviso:

       Ver planilha de erros “Sped\_Fiscal\_Log\_Erros”, mensagem de número __377__\.

Para notas de __saída__ \(SAFX42\): 

Se o campo 126\-Finalidade Emissão da Nfe \(IND\_FIN\_EMISSAO\_NFE\) da SAFX42 for igual a “2”\- Substituição, então:

   Se o campo 121\- Modelo do Documento Fiscal Substituído / Complementado 

  \(COD\_MODELO\_SUBST\) for “21” ou “22” então:

      Se o campo 128\- Código de Autenticação Digital \(Convênio 115/2003\) NF Substituída

      \(COD\_AUTENTIC\_NFE\_SUBST\) NÃO estiver preenchido então:

          Preencher com o campo 119\- Número do Documento Fiscal Substituído 

          /Complementado da SAFX42 \(NUM\_DOCFIS\_SUBST\)\.

          Caso o campo 119 não esteja preenchido, o registro deverá ser gravado normalmente

          e no log deve ser gravada a seguinte mensagem de aviso:

       Ver planilha de erros “Sped\_Fiscal\_Log\_Erros”, mensagem de número __377__\.

Obs:

A mensagem deve seguir o padrão do log de erros do Sped Fiscal, contendo as linhas “Erro”, “Origem” e “Dados do Registro”, que identificam o campo com erro, a descrição do erro, a origem do dado no Mastersaf e a identificação da chave da nota fiscal criticada\.

RND700\-30

Campo MES\_DOC\_REF

Mês e ano da emissão do documento fiscal referenciado\.

\(Regra baseada no C500 – campo 38\)

__MFS690865__: Nas entradas, passar a considerar o campo 326\-PERIOD\_APUR\_SUBST quando preenchido\. E se não preenchido, manter o uso do 75\-DAT\_DI da SAFX07\.

Preencher apenas quando o campo 23 – FIN\_DOCe for igual a “3” \- NFCom de Substituição \(vide RND700\-23\), de acordo com a regra a seguir\.

Para notas de __entrada__ \(SAFX07\): 

Se o campo 300\-Finalidade Emissão da Nfe \(IND\_FIN\_EMISSAO\_NFE\) da SAFX07 for igual a “2” \-Substituição, então:

   Se o campo 304\- Modelo do Documento Fiscal NF Substituída 

   \(COD\_MODELO\_NFE\_SUBST\) da SAFX07 for “21” ou “22” então:

      Se o campo 305\- Código de Autenticação Digital \(Convênio 115/2003\) NF Substituída

      \(COD\_AUTENTIC\_NFE\_SUBST\) da SAFX07 NÃO estiver preenchido então:

          Se o campo 326\-PERIOD\_APUR\_SUBST da SAFX07 estiver preenchido, então:

                   Preencher o MES\_DOC\_REF com 326\-PERIOD\_APUR\_SUBST da SAFX07

                   Formato: mmaaaa

          Senão:

                   Preencher o MES\_DOC\_REF com o mês e ano do campo 75\- DAT\_DI 

                  \(Data da Declaração de Importação/Data  Doc\. Original nas Oper\. de 

                   Devolução\) da SAFX07\. 

                  Formato: mmaaaa\.

Para notas de __saída__ \(SAFX42\): 

Se o campo 126\-Finalidade Emissão da Nfe \(IND\_FIN\_EMISSAO\_NFE\)  da SAFX42 for igual a “2”\- Substituição, então:

   Se o campo 121\- Modelo do Documento Fiscal Substituído / Complementado

   \(COD\_MODELO\_SUBST\) for “21” ou “22” então:

      Se o campo 128\- Código de Autenticação Digital \(Convênio 115/2003\) NF Substituída

      \(COD\_AUTENTIC\_NFE\_SUBST\) NÃO estiver preenchido então:

          Preencher com o mês e ano do campo 122\- Data Emissão do Documento Fiscal 

          Substituído/Complementado \(DAT\_EMIS\_SUBST\)\. 

          Formato: mmaaaa\.

RND700\-31

Campo 32 \- COD\_MUN\_DEST

Para notas de __entrada__ \(SAFX07\): Esse campo não deve ser preenchido\.

Para notas de __saída__ \(SAFX42\): 

Preencher com a concatenação do Código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código  do município \(para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

Código do município \- Campo 76\-Município do Ponto de Consumo da SAFX42\.

Caso o campo 76 não esteja preenchido, o registro deverá ser gravado normalmente e no log deve ser gravada a seguinte mensagem de aviso:

       Ver planilha de erros “Sped\_Fiscal\_Log\_Erros”, mensagem de número __382__\.

Obs:

A mensagem deve seguir o padrão do log de erros do Sped Fiscal, contendo as linhas “Erro”, “Origem” e “Dados do Registro”, que identificam o campo com erro, a descrição do erro, a origem do dado no Mastersaf e a identificação da chave da nota fiscal criticada\.

RND700\-32

Campo DED

__MFS690865:__ inclusão do campo DED, a partir do leiaute EFD118\.

__MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

__\[MFS1000266\]__ Tratamento do valor negativo da dedução\.

Para notas de __entrada__, origem SAFX07:

\- Para notas __com__ itens, totalizar o valor dos itens \(28\-Preço do Item \(VLR\_ITEM\) SAFX08\), cujo campo “Grupo cClass Nfe” \(264\-COD\_GRUPO\_CCLASS SAFX08\) seja igual a 590\.

\- Para notas __sem__ itens, utilizar o valor Outras Deduções da capa \(307\-VLR\_OUTRAS\_DED SAFX07\)\.

Para notas de __saída__, origem SAFX42:

\-  Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens \(19\-Valor dos Serviços \- SAFX43\), dos itens cujo campo “Grupo cClass Nfe” \(118\- COD\_GRUPO\_CCLASS SAFX43 ou cod\_cclass da SAFX43 \(3 primeiros digitos\) 

seja igual a __590__

, considerando o IND\_ADIC\_DESC conforme regra abaixo:

__MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\):

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

      O sistema deverá  __subtrair__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

__Senão __

      O sistema deverá __somar__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

__Valor Negativo à  __Quando o cálculo do campo VL\_DED resultar num valor negativo,  o campo deverá ser gravado com o valor absoluto, ou seja, sem sinal de negativo\. 

# Registro D730 – Registro Analítico do Documento NFCom \(Cód 62\)

RND730

__MFS96211 \- AC 21/2022, nova versão 1\.16, Jan/2023__

MFS580250 – versão 1\.17, Jan/2024: tratamento para notas de entradas\.

MFS577999 – versão 1\.17, Jan/2024: tratamento para notas de saídas\.

__\[MFS690865\] __Alteração da regra do campo VL\_OPR para considerar somente serviços tributados de ICMS \(CST <> 30, 40, 41, 50, 51, 90\), A MFS611132 corrigiu o VL\_SERV do D700 e nessa MFS ajustaremos campo VL\_OPR do D730 para que ambos tenham a mesma regra\.

__MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

Este registro é a totalização dos valores da nota fiscal, e deverá ser gerado a partir dos itens da nota, ou no caso das notas sem item, a partir dos dados da capa da nota\.

__Regras baseadas no D590 \(modelo 22\)__

A totalização dos valores deve ser feita por:

CST\_ICMS \- Código de Situação Tributária do ICMS     

CFOP \- Código Fiscal de Operação                               

ALIQ\_ICMS \- Alíquota ICMS

                                            

\[MFS580250\] versão 1\.17 – Jan/2024

__Para as notas *de entrada*__* *à totalizar os valores gravados no registro D700, a partir dos itens, ou da capa, para o caso das notas sem item\. Para gerações com leiaute a partir da EFD117 \(CAD\_LAYOUT – COD\_VERSAO>=117\), para o caso de notas com itens, considerar apenas os itens com CST preenchido \(campos 30 e 31 da SAFX08\)\.

__Valores do D730:__

__     Totalização pelo item __

__        \(SAFX08/SAFX09\)__

__     Totalização pela capa __

__               \(SAFX07\)__

CST\_ICMS

Se SAFX08 é a concatenação dos códigos das tabelas de situação estadual  "A" e "B" \(código A \+ código B\)\. Campos 30 e 31;

Se SAFX09, considerar o código  "090";

Concatenação dos códigos das tabelas de situação estadual  "A" e "B" \(código A \+ código B\)\. Campos 179 e 180\.

CFOP

Se SAFX08, campo 22;

Se SAFX09, campo 17;

Campo 14

ALIQ\_ICMS

Se SAFX08, campo 42;

Se SAFX09, considerar zero;

Campo 34

VL\_OPR

Valor do produto/serviço\.  

Para notas de __entrada__, origem SAFX07: 

\- Para notas __com__ itens, totalizar o valor dos itens \(28\-Preço do Item \- SAFX08\) \+ \(14\-Valor Serviço \-SAFX09\), apenas os itens com campo COD\_SITUACAO\_B da tabela __SAFX08__ preenchido e __diferente__ de “30” ou “40” ou ”41” ou “50” ou “51” ou “90\*\*”\.; Desconsiderar os itens com “Grupo cClass Nfe” \(campo 264 da SAFX08\) = 110, 120 e 130\. 

 

\*\* CST=90 🡪 Se o COD\_SITUACAO\_B for igual a “90”, deve\-se verificar se o campo Valor do ICMS do item está preenchido \(Campo 43\-VLR\_ICMS da SAFX08\)\.  Se o valor do ICMS estiver preenchido, o campo VL\_SERV deve ser preenchido conforme as regras acima, mesmo quando o COD\_SITUACAO\_B for igual a “90”\. 

__MFS592577 __– Ajuste na composição dos campos para entrada, utilizando como referência o D700 – campo VL\_SERV\.

__\[MFS690865\] __Considerar somente serviços tributados de ICMS \(CST preenchido e <> 30, 40, 41, 50, 51, 90\)\.

__\[MFS877470\] __Alteração da regra de preenchimento para o CST=90

Campo 22 \(Valor do Produto/Serviço\) apenas as notas com campo COD\_SITUACAO\_B da tabela __SAFX07__ preenchido e __diferente__ de “30” ou “40” ou ”41” ou “50” ou “51” ou “90\*\*”\.

\*\* CST=90 🡪 Se o COD\_SITUACAO\_B for igual a “90”, deve\-se verificar se o campo Valor do ICMS da capa está preenchido \(Campo 35\-VLR\_ICMS da SAFX07\)\.  Se o valor do ICMS estiver preenchido, o campo VL\_SERV deve ser preenchido conforme as regras acima, mesmo quando o COD\_SITUACAO\_B for igual a “90”\. 

__MFS592577__ – Ajuste na composição dos campos para entrada, utilizando como referência o D700  – campo VL\_SERV\.

__\[MFS690865\] __Considerar somente serviços tributados de ICMS \(CST preenchido  e <> 30, 40, 41, 50, 51, 90\)\.

__\[MFS877470\] __Alteração da regra de preenchimento para o CST=90

VL\_BC\_ICMS

Se SAFX08, totalizar campo 56;

Se SAFX09, considerar zero;

Campo 51

VL\_ICMS

Se SAFX08, totalizar campo 43;

Se SAFX09, considerar zero;

Campo 35

VL\_RED\_BC

Se SAFX08, totalizar campo 57;

Se SAFX09, considerar zero;

Campo 54

 

__\[MFS989592\] __Inclusão do campo Alíquota ICMS FECEP na composição campo Alíquota ICMS

__ Para as notas de saída__ à totalizar os valores gravados no registro D700, a partir dos itens com CST preenchido \(campos 32 e 33 da SAFX43\), da seguinte forma:

__Valores do D730:__

__Totalização pelo item \(SAFX43\)__

CST\_ICMS

Concatenação dos códigos das tabelas de situação estadual  "A" e "B" \(código A \+ código B\)\. Campos 32 e 33\.

Obs: quando for item de serviço e os campos não estiverem preenchidos, considerar o código “090”

CFOP

Campo 13

ALIQ\_ICMS

O sistema deverá utilizar a soma dos campos: \[21 \- Alíquota de ICMS\] \+ \[104 \- FECEP \- ALÍQUOTA ICMS\]

VL\_OPR

Totalizar campo 19\-Valor dos Serviços \- SAFX43, apenas dos itens com campo COD\_SIT\_TRIB\_B da tabela __SAFX43__ preenchido e diferente de “30” ou “40” ou ”41” ou “50” ou “51” ou “90\*\*\*”, considerando o IND\_ADIC\_DESC conforme regra abaixo:

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

      O sistema deverá  __subtrair__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

__Senão __

      O sistema deverá __somar__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

\*\*\* CST=90 🡪 Se o COD\_SITUACAO\_B for igual a “90”, deve\-se verificar se o campo Valor do ICMS do item está preenchido \(Campo 22\- VLR\_TRIB\_ICMS da SAFX43\)\.  Se o valor do ICMS estiver preenchido, o campo VL\_SERV deve ser preenchido conforme as regras acima, mesmo quando o COD\_SITUACAO\_B for igual a “90”\. 

__MFS592577__ – Retirada dos campos Desconto e Outras Despesas da composição do campo VL\_OPR\.

__\[MFS690865\] __Considerar somente serviços tributados de ICMS \(CST preenchido e <> 30, 40, 41, 50, 51, 90\)\.

__MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\)\.

__\[MFS877470\] __Alteração da regra de preenchimento para o CST=90

__Valor Negativo à  __Quando o cálculo do campo VL\_OPR resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_OPR*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

VL\_BC\_ICMS

Totalizar os itens, conforme regra de cálculo abaixo:

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

    __E se __o campo de CST\_ICMS for igual à ‘00’,’10’,’20’,’70’:

      O sistema deverá utilizar o Campo 23\-VLR\_BASE\_ICMS\_1 

      do Item para __subtrair__ do valor total do Campo VL\_BC\_ICMS\.

__Senão __

__   Se __o campo de CST\_ICMS for igual à ‘00’,’10’,’20’,’70’:

      O sistema deverá utilizar o Campo 23 \-VLR\_BASE\_ICMS\_1 

      do Item para __somar__ ao valor total do Campo VL\_BC\_ICMS\.

__Considerar:__

IND\_ADIC\_DESC = __A__ \(O Item deverá ser somado\); 

IND\_ADIC\_DESC = __D__ \(O Item deverá ser subtraído\);

__Valor Negativo à  __Quando o cálculo do campo VL\_BC\_ICMS resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_BC\_ICMS*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

VL\_ICMS

Totalizar os itens, conforme regra de cálculo abaixo:

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’;

__     E se __o campo de CST\_ICMS for igual à ‘00’,’10’,’20’,’70’:

        O sistema deverá utilizar a soma dos campos

        \[22\-Valor ICMS\] __\+__ \[103\-FECEP ICMS\] do Item para __subtrair__ 

        do valor total do Campo VL\_ICMS\.

__Senão __

__   Se __o campo de CST\_ICMS for igual à ‘00’,’10’,’20’,’70’:

      O sistema deverá utilizar a soma dos campos

      \[22\-Valor ICMS\] __\+__ \[103\-FECEP ICMS\] do Item para __somar__ 

      ao valor total do Campo VL\_ICMS\.

__Considerar:__

IND\_ADIC\_DESC = __A__ \(O Item deverá ser somado\); 

IND\_ADIC\_DESC = __D__ \(O Item deverá ser subtraído\);

__Valor Negativo à  __Quando o cálculo do campo VL\_ICMS resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_ICMS*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

VL\_RED\_BC

Totalização do campo 26 da SAFX43 considerando o IND\_ADIC\_DESC conforme regra abaixo:

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

      O sistema deverá  __subtrair__ do valor total o Campo 26\-Base de Redução \- SAFX43\.

__Senão __

      O sistema deverá __somar__ do valor total o Campo 26\-Base de Redução \- SAFX43\.

__MFS779959__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\)\.

__Valor Negativo à  __Quando o cálculo do campo VL\_RED\_BC resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_RED\_BC*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

RND730\-09

__Para notas de entrada__ à Quando a UF do estabelecimento <> ‘SC’, recuperar a informação do campo 155 – Código da Observação da SAFX08, considerando o primeiro registro lido da combinação de itens selecionados nos critérios de agrupamento do registro\.

__Para notas de saída__ à Quando a UF do estabelecimento <> ‘SC’, recuperar a informação do campo 121 – Código da Observação da SAFX43, considerando o primeiro registro lido da combinação de itens selecionados nos critérios de agrupamento do registro

__Campo: COD\_OBS__

Tratamento para considerar o parâmetro – “Campo Código de Observação \(Considerar 6 caracteres\)” \- para truncar o campo com 6 posições, conforme Manual Guia Prático\.

__SE__ o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

__OU__

__SE__ o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

Este código deverá ser referenciado no registro 0460\.

# Registro D731 – Informações de Fundo de Combate a Pobreza \(Cód 62\) 

RND731

__MFS96211 \- AC 21/2022, nova versão 1\.16, Jan/2023__

MFS580250 – versão 1\.17, Jan/2024: tratamento para notas de entradas\.

MFS577999 – versão 1\.17, Jan/2024: tratamento para notas de saídas\.

Este registro é filho do D730 e deve demonstrar o total do valor do FCP para a combinação de CST\_ICMS, CFOP e Alíquota ICMS\.

A totalização do valor do FCP da nota fiscal, e deverá ser a partir dos itens da nota\.

A totalização dos valores deve ser feita por:

CST\_ICMS \- Código de Situação Tributária do ICMS     

CFOP \- Código Fiscal de Operação                               

ALIQ\_ICMS \- Alíquota ICMS                                

            

\[MFS580250\] versão 1\.17 – Jan/2024

__Para as notas *de entrada*__* *à totalizar o valor do FCP a partir dos itens\.

Para gerações com leiaute a partir da EFD117 \(CAD\_LAYOUT – COD\_VERSAO>=117\), considerar apenas os itens com CST preenchido \(campos 30 e 31 da SAFX08\)\.

__Valores do D731:__

__     Totalização pelo item __

__        \(SAFX08\)__

CST\_ICMS

Concatenação dos códigos das tabelas de situação estadual  "A" e "B" \(código A \+ código B\)\. Campos 30 e 31 da SAFX08

CFOP

Campo 22 da SAFX08;

ALIQ\_ICMS

Campo 42 da SAFX08;

VL\_FCP\_OP

Totalização do campo 138 da SAFX08; 

__ Para as notas de saída__ à totalizar o valor do FCP a partir dos itens com CST preenchido \(campos 32 e 33 da SAFX43\):

__Valores do D731:__

__Totalização pelo item \(SAFX43\)__

CST\_ICMS

Concatenação dos códigos das tabelas de situação estadual  "A" e "B" \(código A \+ código B\)\. Campos 32 e 33\.

Obs: quando for item de serviço e os campos não estiverem preenchidos, considerar o código “090”

CFOP

Campo 13 da SAFX43;

ALIQ\_ICMS

Campo 21 da SAFX43;

VL\_FCP\_OP

Totalização do campo 103 da SAFX43, conforme regra de cálculo abaixo:

\(Regra baseada no C591\- campo 02\)

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’;

__     E se __o campo de CST\_ICMS for igual à ‘00’ ou ’20’:

        O sistema deverá utilizar o campo 103\-FECEP ICMS 

        do Item para __subtrair__ do valor total do Campo 

        VL\_FCP\_OP\.

__Senão __

__   Se __o campo de CST\_ICMS for igual à ‘00’ ou ’20’:

      O sistema deverá utilizar o campo 103\-FECEP ICMS do 

      Item para __somar__ ao valor total do Campo VL\_FCP\_OP\.

__Considerar:__

IND\_ADIC\_DESC = __A__ \(O Item deverá ser somado\); 

IND\_ADIC\_DESC = __D__ \(O Item deverá ser subtraído\);

__Valor Negativo à  __Quando o cálculo do campo VL\_FCP\_OP resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_FCP\_OP*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

__Registro D735 – Observações do Lançamento Fiscal \(Cód 62\)__

RND735

__MFS96211 \- AC 21/2022, nova versão 1\.16, Jan/2023__

MFS577999 – versão 1\.17, Jan/2024: tratamento para notas de saídas\.

Gravar um registro D735 para cada código de observação do lançamento fiscal existente para a nota fiscal gravada no D700 \(notas de modelo = 62\)\.

__Para as notas de entrada__ à  Estas observações ficam registradas na tabela SAFX112 \(“Observações da Nota Fiscal”\), e são as linhas com indicador = __“L”__ \(coluna IND\_ICOMPL\_LANCTO\)\.

__Para as notas de saída__ à Estas observações ficam registradas na tabela SAFX293 \(Observações do Documento Fiscal \- Utilities\), e são as linhas com indicador = “L” \(coluna IND\_ICOMPL\_LANCTO\)\.

Poderão existir “n” observações para uma mesma nota fiscal\.  

RND735\-02

__Campo: COD\_OBS__

__Para as notas de entrada__ à  preencher com o campo 12\-Código da Observação da SAFX112\.

__Para as notas de saída__ à preencher com o campo 9\-Código da Observação da SAFX293\.

Tratamento para considerar o parâmetro – “Campo Código de Observação \(Considerar 6 caracteres\)” \- para truncar o campo com 6 posições, conforme Manual Guia Prático\.

__SE__ o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

__OU__

__SE__ o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

Este código deverá ser referenciado no registro 0460\.

__Registro D737 – Outras Obrigações Tributárias, Ajustes e Informações \.\.\.\.__

RND737

__MFS96211 \- AC 21/2022, nova versão 1\.16, Jan/2023__

MFS577999 – versão 1\.17, Jan/2024: tratamento para notas de saídas\.

Neste registro devem constar os ajustes/outros valores vinculados à observação do lançamento fiscal gravada no registro D735\.

__Para as notas de entrada__ à  Esses ajustes ficam registrados na tabela SAFX113 – Ajustes / Outros Valores do Lançamento Fiscal

__Para as notas de saída__ à Esses ajustes ficam registrados na tabela SAFX294 – Ajustes/Outros Valores do Documento Fiscal – Utilities\.

Poderão existir “n” ajustes vinculados a uma mesma observação\.  

__Regra criada p/ resolver problema de duplicidade de chave \(OS2388\-E10, Abr/2009\)__:

Quando para uma mesma observação, existir mais de um ajuste de *mesmo código de ajuste, * *mesmo produto e mesma alíquota*, os valores devem ser totalizados para gerar um único D737\. Isso é possível quando na nota existirem dois itens de mesmo produto, para os quais existam ajustes de mesmo código\.  A possibilidade existe, já que a SAFX294 foi criada com o número do item da nota, e não com o produto\.  A mesma situação acontece para a tabela SAFX113\.

__Obs__: a alíquota foi incluída como fator de quebra apenas para alertar o usuário sobre a utilização de alíquotas diferentes para um mesmo código de ajuste\. Se ocorrer esta situação, gravaremos as linhas separadamente para possibilitar que o usuário verifique se é um erro na base de dados\. Analisando o layout do Sped, nestes casos a alíquota deveria ser a mesma\.

RND737\-03

Campo DESCR\_COMPL\_AJ:

__Para as notas de entrada à __preencher com a descrição complementar da nova tabela SAFX113\.

__Para as notas de saída__ à preencher com a descrição complementar da nova tabela SAFX294\. 

RND737\-04

Campo COD\_ITEM:

Este campo só deve ser preenchido quando o ajuste estiver relacionado a um produto\. Assim, o seu preenchimento segue a regra abaixo:

__Para as notas de entrada à__

Se o campo “Número do Item da NF” estiver preenchido \(na SAFX113 dos Ajustes\), então:

    O campo deve ser preenchido com a informação do código do Produto correspondente 

    ao item da nota fiscal informado no campo “Número do Item da NF”;

Senão, 

    O campo não terá informação;

__Para as notas de saída__ à

Se o campo “Número do Item da NF” estiver preenchido \(na nova SAFX294 dos Ajustes\), então:

    O campo deve ser preenchido com a informação do código do Produto correspondente 

    ao item da nota fiscal informado no campo “Número do Item da NF”;

Senão, 

    O campo não terá informação;

__Obs: __

- De acordo com a regra geral descrita no registro 0200, lembrar que ao gravar o código de um produto ou Bem, deve\-se concatenar \[indicador\+código do produto\] para os produtos;

Se parâmetro ‘Considerar o Indicador no Código do Item’, não concatenar o código, utilizando a mesma regra descrita no campo 02 do registro 0200

- Somente itens de mercadoria são tratados para ajuste; 

__Registro D750 – Escrituração consolidada da NF Fatura Eletrônica de Serviços de Comunicação – NFCom \(Código 62\)__

RND750

__AC 21/2022, nova versão 1\.16, Jan/2023__

MFS578013 versão 1\.17, Jan/2024: D750, D760, D761

Versão 1\.16 cria os registros relacionados a NFCom \(nota eletrônica de serviços de comunicação, modelo 62\)\.

__Regras baseadas no D700 \(modelo 62\)__

Os registros do sub\-bloco D750 \(D750, D760, D761\) serão gerados a partir da consolidação das notas fiscais de saída\. Já no sub\-bloco D700 \(D730, D731, D735, D737\) serão apresentadas as notas fiscais de entradas e saídas isoladamente \(não consolidadas\)\. 

As notas de modelo 62 não são geradas nos dois sub\-blocos simultaneamente\. 

As notas de Saídas com Finalidade da Emissão \(campo 126 da SAFX42\) = 1 – Normal, __não__ sendo de regime especial ou norma específica e que __não__ possuam Ajustes de Apuração por Documento utilizando tabela 5\.3 do SPED, serão geradas em apenas em um dos registros: D700 ou D750, de acordo com determinação da legislação de cada UF\. As demais notas sempre devem ser escrituradas individualizadas no D700\.

Veja a explicação completa da escrituração da NFCom na regra do D700 \(RND700\)\.

__Sub\-bloco D750 \(D760, D761\)__ __– Origem das Informações:__

A geração dos dados do sub\-bloco D750 e filhos tem origem nas notas de saída\.

Geração das Notas de Saída à os dados serão recuperados nas tabelas SAFX42 e SAFX43, considerando apenas modelo ‘62’\. As notas de Utilities das tabelas SAFX42/43 sempre têm itens\. 

Critérios de seleção das notas:

- Modelo \(campo “13 – Modelo de Documento” da SAFX42\) = 62;
- Notas não canceladas \(campo “21 \- Situação da Nota” da SAFX42\) <> S;
- Data Fiscal \(campo 03 da SAFX42\) \- enquadrada no período de geração;
- Não considerar os itens informativos \(itens da SAFX43 com o campo 10\-Tipo de Item = 1\);  __MFS690865__: retira esse critério para que os itens informativos sejam recuperados para compor o valor do campo 09 – VL\_SERV\_NT
- Não considerar notas fiscais onde todos os itens não tenham CST \(campos 32 e 33 da SAFX43 não preenchidos; \(\*\)
- Finalidade da Emissão \(campo 126 da SAFX42\) = 1 – Normal;
- __Não__ seja baseada em regime especial ou norma específica \(campo 83 \- IND\_NF\_REG\_ESP da SAFX42  = ‘N’\)
- __Não__ tenha registros de Ajustes de Apuração por Documento utilizando tabela 5\.3 do SPED\. Ou seja, não tenha registros na tabela SAFX293 \(Observações do Documento Fiscal \- Utilities\), com indicador = “L” \(coluna IND\_ICOMPL\_LANCTO\)\. 

                           

Consolidar as notas recuperadas pelos seguintes campos:

- Modelo \(campo 13 da SAFX42\)
- Série \(campo 07 da SAFX42\)
- Data de Emissão \(campo 03 da SAFX42\)
- Indicador de Serviço Pré\-Pago \(campo 59 da SAFX43\)

__OBS1__: Na geração por Inscrição Estadual Única, deve\-se considerar os documentos fiscais de entrada \(SAFX07\) e saída \(SAFX42\) de todos os Estabelecimentos envolvidos na centralização;

\(\*\) Versão 117 da EFD2024 diz: “A NFCom que contenha apenas itens sem a indicação de Código de Situação Tributária – CST não deve ser escriturada\.”

RND750\-05

Campo QTD\_CONS:

Totalizar a quantidade de documentos consolidados por Modelo, Série, Data de Emissão e Indicador de Serviço Pré\-Pago\.

RND750\-06

Campo IND\_PREPAGO

Se campo 59\-Indicador de Serviço Pré\-Pago da SAFX43 = ‘S’ então:

    Preencher com 0 – pré pago

Senão

    Preencher com 1 – pós pago

RND750\-07

Campo VL\_DOC:

MFS592577 – Retirada dos campos VL\_DA e VL\_DESC da composição do campo VL\_DOC\.

__MFS690865__: Para leiaute a partir da EFD118, considerar campo Deduções na composição do campo VL\_DOC\.

O valor do campo VL\_DOC deve ser preenchido com o resultado da expressão:

Para gerações com leiaute anterior a EFD118 \(CAD\_LAYOUT – COD\_VERSAO < 118\):

VL\_DOC = VL\_SERV \+ VL\_SERV\_NT \+ VL\_TERC

Para gerações com leiaute a partir da EFD118 \(CAD\_LAYOUT – COD\_VERSAO>=118\):

VL\_DOC = VL\_SERV \+ VL\_SERV\_NT \+ VL\_TERC \- DED

RND750\-08

Campo VL\_SERV: 

__\[MFS611132\] __Alteração da regra para considerar somente serviços tributados de ICMS

__MFS690865__: Valor do serviço dos Itens Informativos \(10\-Tipo de Item da SAFX43 = ‘1’\) deve compor o campo 09 – VL\_SERV\_NT e não o campo 08 – VL\_SERV\. Os itens informativos não possuem o CST preenchido\. O tratamento será aplicado aos itens sem CST, para que o valor de serviço não seja considerado no campo 08 e sim no campo 09\.

__MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

\-  Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens \(19\-Valor dos Serviços \- SAFX43\) \), apenas as notas com campo COD\_SIT\_TRIB\_B da tabela __SAFX43__ preenchido e diferente de “30” ou “40” ou ”41” ou “50” ou “51” ou “90” considerando o IND\_ADIC\_DESC conforme regra a seguir:

__MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\):

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

      O sistema deverá  __subtrair__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

__Senão __

      O sistema deverá __somar__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

__Valor Negativo à  __Quando o cálculo do campo VL\_SERV resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_SERV*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

RND750\-09

Campo VL\_SERV\_NT: valor dos serviços não tributados pelo ICMS

__\[MFS611132\] __Alteração da regra para considerar somente serviços tributados de ICMS

__MFS690865__: Valor do serviço dos Itens Informativos \(10\-Tipo de Item da SAFX43 = ‘1’\) deve compor o campo 09 – VL\_SERV\_NT e não o campo 08 – VL\_SERV\. Os itens informativos não possuem o CST preenchido\. O tratamento será aplicado aos itens sem CST, para que o valor de serviço não seja considerado no campo 08 e sim no campo 09\.

__MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

__\[MFS1039052\]__ Tratamento dos itens de dedução que não devem ser considerados no valor de serviço não tributado \(Grupo cClass Nfe” \(campo 264 da SAFX08\) = 590\)\.

Preencher com a soma dos valores dos Itens da __SAFX43__:

__\(a\) __Valor das bases isenta/não tributada \+ base outras dos *itens de mercadoria* __SAFX43 __

__\+__

__\(b\) __Valor do serviço dos *itens de mercadoria* da __SAFX43, __

__\+__

__\(c\)__ Valor do serviço dos *itens de serviço* da __SAFX43,__

Onde:

 \- Para __\(a\)__, considerar campos 24\-Base Isenta/Não Tributada \+ campo 25\-Base Outras da __SAFX43__ dos itens de mercadoria \(campo 47 = “1”\), apenas quando o campo COD\_SITUACAO\_B da tabela __SAFX43__ for __igual__ a “30”, “40”,”41”, “50”, “51” ou “90”, considerando o IND\_ADIC\_DESC conforme regra abaixo\. Desconsiderar os itens com “Grupo cClass Nfe” \(campo 264 da SAFX08\) = 110, 120, 130 e 590\.

\- Para __\(b\)__, considerar campo 19\-Valor do Serviço da __SAFX43__ dos itens de mercadoria \(campo 47 = “1”\), apenas quando o campo COD\_SITUACAO\_B da tabela __SAFX43__ não estiver preenchido, considerando o IND\_ADIC\_DESC conforme regra abaixo\. Desconsiderar os itens com “Grupo cClass Nfe” \(campo 264 da SAFX08\) = 110, 120, 130 e 590\.

 \- Para __\(c\)__ considerar o campo 19\-Valor do Serviço da __SAFX43__ dos itens de serviço \(campo 47 = “2”\) considerando o IND\_ADIC\_DESC conforme regra abaixo\.

__MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\):

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

       \- Para __\(a\)__:

         O sistema deverá  __subtrair__ do valor total os Campos 24\-Base Isenta/Não Tributada e

          campo 25\-Base Outras \- SAFX43\.

       \- Para __\(b\)__ e __\(c\)__:

         O sistema deverá  __subtrair__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

__Senão __

       \- Para __\(a\)__:

         O sistema deverá  __somar__ do valor total os Campos 24\-Base Isenta/Não Tributada e

          campo 25\-Base Outras \- SAFX43\.

       \- Para __\(b\)__ e __\(c\)__:

         O sistema deverá  __somar__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

__Valor Negativo à  __Quando o cálculo do campo VL\_SERV\_NT resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_SERV\_NT*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

RND750\-10

Campo VL\_TERC

__MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

\-  Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens \(75\-Valor de Terceiros \- SAFX43\), considerando o IND\_ADIC\_DESC conforme regra abaixo:

__MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\):

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

      O sistema deverá  __subtrair__ do valor total o Campo 75\-Valor de Terceiros \- SAFX43\.

__Senão __

      O sistema deverá __somar__ do valor total o Campo 75\-Valor de Terceiros \- SAFX43\.

__Valor Negativo à  __Quando o cálculo do campo VL\_TERC resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_TERC*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

RND750\-11

Campo VL\_DESC:

Valor do Desconto\.

__MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

\-  Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens \(18\-Valor do Desconto \- SAFX43\), considerando o IND\_ADIC\_DESC conforme regra a seguir:

__MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\):

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

      O sistema deverá  __subtrair__ do valor total o Campo 18\-Valor do Desconto \- SAFX43\.

__Senão __

      O sistema deverá __somar__ do valor total o Campo 18\-Valor do Desconto \- SAFX43\.

__Valor Negativo à  __Quando o cálculo do campo VL\_DESC resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_DESC*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

RND750\-12

Campo VL\_DA

__MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

\-  Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens \(46\-Valor Outras Despesas \- SAFX43\), considerando o IND\_ADIC\_DESC conforme regra a seguir:

__MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\):

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

      O sistema deverá  __subtrair__ do valor total o Campo 46\-Valor Outras Despesas \- SAFX43\.

__Senão __

      O sistema deverá __somar__ do valor total o Campo 46\-Valor Outras Despesas \- SAFX43\. 

__Valor Negativo à  __Quando o cálculo do campo VL\_DA resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_DA*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

RND750\-13

Campo VL\_BC\_ICMS

\(Regra baseada no C500\- campo 19\)

Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens \(SAFX43\), considerando apenas os itens com CST preenchido \(campos 32 e 33 da SAFX43\) \(\*\), conforme regra de cálculo abaixo:

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

    __E se __o campo de CST\_ICMS for igual à ‘00’,’10’,’20’,’70’:

      O sistema deverá utilizar o Campo 23\-VLR\_BASE\_ICMS\_1 do Item para __subtrair__ do valor total do Campo VL\_BC\_ICMS\.

__Senão __

__   Se __o campo de CST\_ICMS for igual à ‘00’,’10’,’20’,’70’:

      O sistema deverá utilizar o Campo 23\-VLR\_BASE\_ICMS\_1 do Item para __somar__ ao valor total do Campo VL\_BC\_ICMS\.

__Considerar:__

IND\_ADIC\_DESC = __A__ \(O Item deverá ser somado\); 

IND\_ADIC\_DESC = __D__ \(O Item deverá ser subtraído\);

__Valor Negativo à  __Quando o cálculo do campo VL\_BC\_ICMS resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_BC\_ICMS*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

\(\*\) Versão 117 da EFD2024 determina que os itens sem CST não sejam considerados na geração dos registros D730 e D760\. Essa definição impacta os campos Base ICMS e Valor ICMS dos registros D700 e D750 que devem corresponder a soma dos valores apresentados nesses registros\. Por isso na definição desses campos, também não serão considerados os itens sem CST\.

RND750\-14

Campo VL\_ICMS

\(Regra baseada no C500\- campo 20\)

Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens \(SAFX43\), considerando apenas os itens com CST preenchido \(campos 32 e 33 da SAFX43\), conforme regra de cálculo abaixo:

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’;

__     E se __o campo de CST\_ICMS for igual à ‘00’,’10’,’20’,’70’:

        O sistema deverá utilizar a soma dos campos \[22\-Valor ICMS\] __\+__ \[103\-FECEP ICMS\] 

        do Item para __subtrair__ do valor total do Campo VL\_ICMS\.

__Senão __

__   Se __o campo de CST\_ICMS for igual à ‘00’,’10’,’20’,’70’:

      O sistema deverá utilizar a soma dos campos \[22\-Valor ICMS\] __\+__ \[103\-FECEP ICMS\] 

      do Item para __somar__ ao valor total do Campo VL\_ICMS\.

__Considerar:__

IND\_ADIC\_DESC = __A__ \(O Item deverá ser somado\); 

IND\_ADIC\_DESC = __D__ \(O Item deverá ser subtraído\);

__Valor Negativo à  __Quando o cálculo do campo VL\_ICMS resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_ICMS*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

RND750\-15

Campo VL\_PIS

__MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

Quando o parâmetro “Inibir a geração das informações constantes na EFD Contribuições \(Parâmetros > Dados Iniciais\)” estiver marcado, este campo deve ser gerado em branco \(||\)\. Caso contrário, o campo será preenchido conforme regra a seguir:

\-  Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens \(77\-Valor PIS \- SAFX43\), considerando o IND\_ADIC\_DESC conforme regra abaixo:

__MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\):

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

      O sistema deverá  __subtrair__ do valor total o Campo 77\-Valor PIS \- SAFX43\.

__Senão __

      O sistema deverá __somar__ do valor total o Campo 77\-Valor PIS \- SAFX43\.

__Valor Negativo à  __Quando o cálculo do campo VL\_PIS resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_PIS*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

RND750\-16

Campo VL\_COFINS

__MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

Quando o parâmetro “Inibir a geração das informações constantes na EFD Contribuições \(Parâmetros > Dados Iniciais\)” estiver marcado, este campo deve ser gerado em branco \(||\)\. Caso contrário, o campo será preenchido conforme regra a seguir:

\-  Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens \(80\-Valor COFINS da SAFX43\), considerando o IND\_ADIC\_DESC conforme regra abaixo:

 __MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\):

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

      O sistema deverá  __subtrair__ do valor total o Campo 80\-Valor COFINS\- SAFX43\.

__Senão __

      O sistema deverá __somar__ do valor total o Campo 80\-Valor COFINS \- SAFX43

__Valor Negativo à  __Quando o cálculo do campo VL\_COFINS resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_COFINS*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

 

RND750\-17

Campo DED

__MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

__MFS690865:__ inclusão do campo DED, a partir do leiaute EFD118\.

__\[MFS1039052\]__ Tratamento do valor negativo da dedução\.

\-  Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens \(19\-Valor dos Serviços \- SAFX43\), dos itens cujo campo “Grupo cClass Nfe” \(118\- COD\_GRUPO\_CCLASS SAFX43\) seja igual a 590, considerando o IND\_ADIC\_DESC conforme regra abaixo:

__MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\):

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

      O sistema deverá  __subtrair__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

__Senão __

      O sistema deverá __somar__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

__Valor Negativo à  __Quando o cálculo do campo VL\_DED resultar num valor negativo,  o campo deverá ser gravado com o valor absoluto, ou seja, sem sinal de negativo\.

# Registro D760 – Registro Analítico do Documento NFCom \(Cód 62\)

RND760

__AC 21/2022, nova versão 1\.16, Jan/2023__

MFS578013 versão 1\.17, Jan/2024: D750, D760, D761

__\[MFS690865\] __Alteração da regra do campo VL\_OPR para considerar somente serviços tributados de ICMS \(CST preenchido e <> 30, 40, 41, 50, 51, 90\), A MFS611132 corrigiu o VL\_SERV do D750 e nessa MFS ajustaremos campo VL\_OPR do D760 para que ambos tenham a mesma regra\.

__MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\) devem reduzir o valor na gravação dos campos gerados pelo somatório dos itens da SAFX43\.

Este registro é a totalização dos valores dos itens dos documentos fiscais consolidados no registro D750, agrupados por:

   

CST\_ICMS \- Código de Situação Tributária do ICMS     

CFOP  \-  Código Fiscal de Operação                               

ALIQ\_ICMS \- Alíquota ICMS

                                            

Totalizar os valores gravados no registro D750, a partir dos itens com CST preenchido \(campos 32 e 33 da SAFX43\), da seguinte forma:

__\[MFS989592\] __Inclusão do campo Alíquota ICMS FECEP na composição campo Alíquota ICMS

__Valores do D760:__

__Totalização pelo item \(SAFX43\)__

CST\_ICMS

Concatenação dos códigos das tabelas de situação estadual  "A" e "B" \(código A \+ código B\)\. Campos 32 e 33\.

Obs: quando for item de serviço e os campos não estiverem preenchidos, considerar o código “090”

CFOP

Campo 13

ALIQ\_ICMS

O sistema deverá utilizar a soma dos campos: \[21 \- Alíquota de ICMS\] \+ \[104 \- FECEP \- ALÍQUOTA ICMS\]

VL\_OPR

Totalizar campo 19\-Valor dos Serviços \- SAFX43, apenas dos itens com campo COD\_SIT\_TRIB\_B da tabela __SAFX43__ preenchido e diferente de “30” ou “40” ou ”41” ou “50” ou “51” ou “90”, considerando o IND\_ADIC\_DESC conforme regra abaixo:

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

      O sistema deverá  __subtrair__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

__Senão __

      O sistema deverá __somar__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

__MFS592577__ – Retirada dos campos Desconto e Outras Despesas da composição do campo VL\_OPR\.

__\[MFS690865\] __Considerar somente serviços tributados de ICMS \(CST preenchido e <> 30, 40, 41, 50, 51, 90\)\.

__MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\)\.

__Valor Negativo à  __Quando o cálculo do campo VL\_OPR resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_OPR*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

VL\_BC\_ICMS

Totalizar os itens, conforme regra de cálculo abaixo:

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

    __E se __o campo de CST\_ICMS for igual à ‘00’,’10’,’20’,’70’:

      O sistema deverá utilizar o Campo 23\-VLR\_BASE\_ICMS\_1 

      do Item para __subtrair__ do valor total do Campo VL\_BC\_ICMS\.

__Senão __

__   Se __o campo de CST\_ICMS for igual à ‘00’,’10’,’20’,’70’:

      O sistema deverá utilizar o Campo 23 \-VLR\_BASE\_ICMS\_1 

      do Item para __somar__ ao valor total do Campo VL\_BC\_ICMS\.

__Considerar:__

IND\_ADIC\_DESC = __A__ \(O Item deverá ser somado\); 

IND\_ADIC\_DESC = __D__ \(O Item deverá ser subtraído\);

__Valor Negativo à  __Quando o cálculo do campo VL\_BC\_ICMS resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_BC\_ICMS*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

VL\_ICMS

Totalizar os itens, conforme regra de cálculo abaixo:

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’;

__     E se __o campo de CST\_ICMS for igual à ‘00’,’10’,’20’,’70’:

        O sistema deverá utilizar a soma dos campos

        \[22\-Valor ICMS\] __\+__ \[103\-FECEP ICMS\] do Item para __subtrair__ 

        do valor total do Campo VL\_ICMS\.

__Senão __

__   Se __o campo de CST\_ICMS for igual à ‘00’,’10’,’20’,’70’:

      O sistema deverá utilizar a soma dos campos

      \[22\-Valor ICMS\] __\+__ \[103\-FECEP ICMS\] do Item para __somar__ 

      ao valor total do Campo VL\_ICMS\.

__Considerar:__

IND\_ADIC\_DESC = __A__ \(O Item deverá ser somado\); 

IND\_ADIC\_DESC = __D__ \(O Item deverá ser subtraído\);

__Valor Negativo à  __Quando o cálculo do campo VL\_ICMS resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_ICMS*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

VL\_RED\_BC

Totalização do campo 26 da SAFX43 considerando o IND\_ADIC\_DESC conforme regra abaixo:

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

      O sistema deverá  __subtrair__ do valor total o Campo 26\-Base de Redução \- SAFX43\.

__Senão __

      O sistema deverá __somar__ do valor total o Campo 26\-Base de Redução \- SAFX43\.

__MFS779975__: Itens com devolução de valor \(20 \- Adição/Desconto da SAFX43 = ‘D’\)\.

__Valor Negativo à  __Quando o cálculo do campo VL\_RED\_BC resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_RED\_BC*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

RND760\-09

Quando a UF do estabelecimento <> ‘SC’, recuperar a informação do campo 121 – Código da Observação da SAFX43, considerando o primeiro registro lido da combinação de itens selecionados nos critérios de agrupamento do registro

__Campo: COD\_OBS__

Tratamento para considerar o parâmetro – “Campo Código de Observação \(Considerar 6 caracteres\)” \- para truncar o campo com 6 posições, conforme Manual Guia Prático\.

__SE__ o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

__OU__

__SE__ o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

Este código deverá ser referenciado no registro 0460\.

# Registro D761 – Informações de Fundo de Combate a Pobreza \(Cód 62\) 

RND761

__AC 21/2022, nova versão 1\.16, Jan/2023__

MFS578013 versão 1\.17, Jan/2024: D750, D760, D761

Este registro é filho do D760 e deve demonstrar o total do valor do FCP para a combinação de CST\_ICMS, CFOP e Alíquota ICMS\.

A totalização do valor do FCP da nota fiscal, e deverá ser a partir dos itens da nota\.

A totalização dos valores deve ser feita por:

CST\_ICMS \- Código de Situação Tributária do ICMS     

CFOP \- Código Fiscal de Operação                               

ALIQ\_ICMS \- Alíquota ICMS                         

Totalizar o valor do FCP a partir dos itens com CST preenchido \(campos 32 e 33 da SAFX43\):                   

 

__Valores do D761:__

__Totalização pelo item \(SAFX43\)__

CST\_ICMS

Concatenação dos códigos das tabelas de situação estadual  "A" e "B" \(código A \+ código B\)\. Campos 32 e 33\.

Obs: quando for item de serviço e os campos não estiverem preenchidos, considerar o código “090”

CFOP

Campo 13 da SAFX43;

ALIQ\_ICMS

Campo 21 da SAFX43;

VL\_FCP\_OP

Totalização do campo 103 da SAFX43, conforme regra de cálculo abaixo:

\(Regra baseada no C591\- campo 02\)

__Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’;

__     E se __o campo de CST\_ICMS for igual à ‘00’ ou ’20’:

        O sistema deverá utilizar o campo 103\-FECEP ICMS 

        do Item para __subtrair__ do valor total do Campo 

        VL\_FCP\_OP\.

__Senão __

__   Se __o campo de CST\_ICMS for igual à ‘00’ ou ’20’:

      O sistema deverá utilizar o campo 103\-FECEP ICMS do 

      Item para __somar__ ao valor total do Campo VL\_FCP\_OP\.

__Considerar:__

IND\_ADIC\_DESC = __A__ \(O Item deverá ser somado\); 

IND\_ADIC\_DESC = __D__ \(O Item deverá ser subtraído\);

__Valor Negativo à  __Quando o cálculo do campo VL\_FCP\_OP resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_FCP\_OP*__ __*esta com conteúdo inválido \(valor negativo\)”\.*__

= = = = = = = = = =


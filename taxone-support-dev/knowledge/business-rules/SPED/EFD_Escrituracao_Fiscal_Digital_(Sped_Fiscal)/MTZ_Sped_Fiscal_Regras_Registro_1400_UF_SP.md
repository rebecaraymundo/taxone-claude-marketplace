# MTZ_Sped_Fiscal_Regras_Registro_1400_UF_SP

- **Fonte:** MTZ_Sped_Fiscal_Regras_Registro_1400_UF_SP.docx
- **Modificado:** 2026-03-02
- **Tamanho:** 148 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Registro 1400 – Específico por UF \- SP

__Localização__: 

##### DOCUMENTO DE REQUISITO

__*Data*__

__Demanda__

__Descrição__

__Responsável__

21/05/2015

OS’s4728

OS’s4735

Alteração na geração do registro 1400 para atendimento à Resolução 4730/14\-MG e  Portaria CAT 137/2014\-SP\. Consultar as observações descritas no cabeçalho do reg\. 1400, e as regras específicas de MG e SP: __RN1400\-MG\-“nn” e RN1400\-SP\-“nn”__\.

Vânia Dias Mattos

10/03/2016

MFS2437

Alterada a geração do registro 1400 \(código SPDIPAM25\) para as empresas distribuidoras de energia elétrica \(ver __RN1400\-SP__, __RN1400\-SP\-07\-A __e__ RN1400\-SP\-07\-B__\)\.

Vânia Dias Mattos

23/11/2017

MFS14303

Inclusão do código SPDIPAM27 a geração do registro 1400 para as empresas que fazem vendas presenciais com saídas em outro estabelecimento \(ver __RN1400\-SP__ e __RN1400\-SP\-12__\)\.

Julyana Perrucini

24/04/2018

CH9368\_2018 \(MFS\-18062\)

Alteração do 1400 para SP\. O código DIPAM\-35 passa a considerar outros ajustes com relação ao CFOP 5927 \(Ver __RN1400\-SP\-10__\)\.

Julyana Perrucini

12/06/2018

MFS18797

Alteração na geração do registro 1400 para o estado de SP: criadas novas regras para o código SPDIPAM25 para as empresas geradoras de energia \(ver RN1400\-SP\-07\-C\)\.

Vânia Mattos

14/06/2018

MFS19151

Alteração na geração do registro 1400 para o estado de SP: alteração da regra para o código SPDIPAM22 para a forma de cálculo igual a “Valor Total NF – Revendedor Autônomo” \(ver RN1400\-SP\-04\)\.

Andréa Rocha

29/09/2023

MFS436036

Tratamento das notas de saída de modelo 62 \(NFCom\) na geração do registro 1400\.

Liliane Assaf

03/02/2025

MFS710672

Inclusão do modelo 66 na regra do código SPDIPAM25 \(Energia Elétrica – Geração\)

Graciela Soares

12/09/2025

MFS877174/MFS910283

Criação da tabela particionada DWT\_DOCTO\_FISCAL\_SPED espelho da DWT\_DOCTO\_FISCAL e utilização na geração dos registros C100, C500, D100, D500 e 1400 – UF = SP\.

Liliane Assaf

# <a id="_Toc75782997"></a>Registro 1400 para o tipo de geração – Específico por UF<a id="_Toc75782998"></a> – SP

__RN1400\-SP__

\(ver detalhes descritos no cabeçalho do registro 1400\)

A geração do 1400 para a modalidade “SP” foi desenvolvida de acordo com as mesmas regras utilizadas na geração da DIPAM\-B \(registro 30\) da GIA\-SP \(com apenas a diferença da inclusão de código 12\)\.

 

As regras estão organizadas da seguinte forma:

__RN1400\-SP\-01__ – geração para o código “SPDIPAM11”

__RN1400\-SP\-02__ – geração para o código “SPDIPAM12”

__RN1400\-SP\-03__ – geração para o código “SPDIPAM13”

__RN1400\-SP\-04__ – geração para o código “SPDIPAM22”

__RN1400\-SP\-05__ – geração para o código “SPDIPAM23”

__RN1400\-SP\-06__ – geração para o código “SPDIPAM24”

__RN1400\-SP\-07\-A__ – geração para o código “SPDIPAM25” \(Geração/Comércio EE\)

__RN1400\-SP\-07\-B__ – geração para o código “SPDIPAM25” \(Distribuidoras EE\)

__RN1400\-SP\-07\-C__ – geração para o código “SPDIPAM25” \(Geradoras EE\)

__RN1400\-SP\-08__ – geração para o código “SPDIPAM26”

__RN1400\-SP\-09__ – geração para o código “SPDIPAM31”

__RN1400\-SP\-10__ – geração para o código “SPDIPAM35”

__RN1400\-SP\-11__ – geração para o código “SPDIPAM36”

__RN1400\-SP\-12__ – geração para o código “SPDIPAM27”

Alteração__ MFS2437__: esta OS criou regras diferenciadas para o código SPDIPAM25, dependendo se a empresa de EE é distribuidora, ou geradora/comércio\.

Alteração MFS14303: esta MFS criou regras de geração para o código SPDIPAM27 para as empresas que fazem vendas presenciais com saídas em outro estabelecimento\.

Alteração __MFS18797__: esta MFS criou novas regras para geração do código SPDIPAM25 p/as ampresas geradoras de energia alétrica\. As regras referentes à comércio e distribuição não foram alteradas\.

__OBS__: O registro 1400 *não* é gerado na geração da EFD do menu “Geração\-PIM”, conforme consta na regra RN1400\.

__RN1400\-SP\-01__

__Código SPDIPAM11__ 

__\[MFS92120\] __Inclusão da regra para considerar somente notas de pessoa física

__MFS877174/MFS910283__

Criação da tabela particionada DWT\_DOCTO\_FISCAL\_SPED espelho da DWT\_DOCTO\_FISCAL e utilização na geração dos registros C100, C500, D100, D500 e 1400 – UF = SP\.

\(Compras escrituradas de mercadorias de produtores agropecuários\)

A geração deste código da DIPAM\-B segue as regras da GIA\-SP, onde o município utilizado é o município da SAFX04\. lembrando que a GIA\-SP *não* usa o parâmetro 67 na geração da DIPAM\-B\.

__Origem__: \- Notas Fiscais \(SAFX07 e SAFX08\)

             \- Valores informados manualmente 

             \- Parametrização de CFOP e CFOP/NAT

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UF\)

             \- Parametrização de Produtos 

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UFàDIPAM\-B x Produto\)

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração \(ver OBS\)

\- MOVTO\_E\_S – somente as notas de entradas \(MOVTO\_E\_S <> “9”\)

\- Data Fiscal \- no período da geração ou data extemporânea no período da geração 

\- Modelo \(campo 13\) =  01, 1B, 04 ou 55

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- Somente notas com itens 

\- Somente itens de mercadoria

\- Situação = somente as não canceladas

\- Somente notas que não sejam transferências \(IND\_TRANSF\_CRED = “0”\)

\- Somente notas com situação especial <> 1, 2 e 8 \(IND\_SITUACAO\_ESP <> 1, 2 e 8\) 

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no menu

  “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__SPDIPAM11__”

\- Somente notas em que o estado da pessoa fis/jur \(remetente\) seja = “SP”

\- Dependendo da parametrização dos dados iniciais \(ver campo “*Dados para a geração *

*  específica \(DIPAM\-B – SP\)*”\), serão considerados apenas os itens com produtos

  parametrizados no menu “Parâmetros à  Registro 1400 à Específico por UF à

  DIPAM\-B x Produto”, da seguinte forma:

     Se parâmetro “*Utilizar a parametrização de produtos*” __marcado__: 

        Nesse caso, serão considerados *apenas* os itens com o produto parametrizado;

     Se parâmetro “*Utilizar a parametrização de produtos*” __desmarcado__: 

        Nesse caso, serão considerados qualquer tipo de produto; 

\- Somente notas fiscais em que a Pessoa Física/Jurídica seja Pessoa Física,  verificando se atende a uma das condições abaixo:

  a\) Se o campo CPF/CNPJ \(campo 6 da SAFX04\) tem 11 caracteres __OU__

  b\) Se o campo Classe de Pessoa Física Jurídica \(campo 26 da SAFX04\) igual a 01 \(Pessoa Física\) e o campo Produtor Rural \(campo 80 da SAFX04\) igual a “S”\.

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Da mesma forma que é feito na geração padrão e na geração de MG do registro 1400, a totalização dos itens para geração deste código da DIPAM, pode ser feita \(se possível\), durante a geração do registro C100 e filhos, para uma melhor performance\. Mas,  observando que neste item trabalhamos com parametrização de CFOP e de produto \(opcionalmente\)\.

__Processamento das notas__:

Os itens recuperados conforme os critérios acima serão totalizados __por município da pessoa fis/jur \(\*\)__, e para cada município será gerado um registro 1400, da seguinte forma:

\(\*\) conforme regras da GIA\-SP

Valor a ser totalizado = valor contábil do item \(campo 64, SAFX08\)

 = = = = =

__Gravação do registro 1400:__

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                                     “__SPDIPAM11__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__SPDIPAM11__” 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                 \[Valor resultante da totalização\] 

                                              \(\+\)

              \[Campo “Outros Valores” informado manualmente\]

                                               \(\-\) 

             \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-SP\-02__

__Código SPDIPAM12__ 

\(Compras *não* escrituradas de mercadorias de produtores agropecuários\)

__\[MFS42617\]__ Inclusão da recuperação das notas fiscais escrituradas

\(este código não é gerado na GIA\-SP, mas será gerado no Sped seguindo as mesmas regras do SPDIPAM11, só que apenas com as notas __*não*__ escrituradas\)  
__MFS877174/MFS910283__

Criação da tabela particionada DWT\_DOCTO\_FISCAL\_SPED espelho da DWT\_DOCTO\_FISCAL e utilização na geração dos registros C100, C500, D100, D500 e 1400 – UF = SP\.

__Notas Fiscais não escrituradas:__

__Origem__: \- Notas Fiscais \(SAFX07 e SAFX08\)

             \- Valores informados manualmente 

             \- Parametrização de CFOP e CFOP/NAT

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UF\)

             \- Parametrização de Produtos 

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UFàDIPAM\-B x Produto\)

Como são notas não escrituradas, estas notas não constarão do C100\.

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração \(ver OBS\)

\- MOVTO\_E\_S – somente as notas de entradas \(MOVTO\_E\_S <> “9”\)

\- Data Fiscal \- no período da geração ou data extemporânea no período da geração 

\- Modelo \(campo 13\) =  01, 1B, 04 ou 55

__\- Classificação – somente notas não escrituradas \(Classificação = 7\)__

\- Somente notas com itens 

\- Somente itens de mercadoria

\- Situação = somente as não canceladas

\- Somente notas que não sejam transferências \(IND\_TRANSF\_CRED = “0”\)

\- Somente notas com situação especial <> 1, 2 e 8 \(IND\_SITUACAO\_ESP <> 1, 2 e 8\) 

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no menu  “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__SPDIPAM12__”  e o parâmetro  “Lançar NF Escrituradas” igual a “N”;

\- Somente notas em que o estado da pessoa fis/jur \(remetente\) seja = “SP”

\- Dependendo da parametrização dos dados iniciais \(ver campo “*Dados para a geração *

*  específica \(DIPAM\-B – SP\)*”\), serão considerados apenas os itens com produtos

  parametrizados no menu “Parâmetros à  Registro 1400 à Específico por UF à

  DIPAM\-B x Produto”, da seguinte forma:

     Se parâmetro “*Utilizar a parametrização de produtos*” __marcado__: 

        Nesse caso, serão considerados *apenas* os itens com o produto parametrizado;

     Se parâmetro “*Utilizar a parametrização de produtos*” __desmarcado__: 

        Nesse caso, serão considerados qualquer tipo de produto;

__Notas Fiscais escrituradas:__

__Origem__: \- Notas Fiscais \(SAFX07 e SAFX08\)

             \- Valores informados manualmente 

             \- Parametrização de CFOP e CFOP/NAT

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UF\)

             \- Parametrização de Produtos 

               \(menu “ParâmetrosàRegistro 1400à Código de DIPAM\-B \- Código 1\.2 x Produto\)

\- Código da empresa – código da empresa da geração;

\- Código do Estabelecimento – código do estabelecimento da geração \(ver abaixo Observação sobre Insc\. Estadual Única\);

\- MOVTO\_E\_S – somente as notas de entradas \(MOVTO\_E\_S <> “9”\);

\- Data Fiscal – a data fiscal, ou data extemporânea \(qdo for o caso\) do documento, deve ser uma data enquadrada no período da geração;

\- Modelo \(campo 13 da SAFX07\) =  01, 1B, 04 ou 55;

\- Classificação do documento \(campo 12 da SAFX07\) – somente notas escrituradas \(Classificação = 1 ou 3\);

\- Somente notas com itens; 

\- Situação = somente as notas não canceladas \(SITUAÇÃO <> “S”\);

\- Somente notas que não sejam transferências \(IND\_TRANSF\_CRED = “0”\);

\- Somente notas com situação especial <> 1, 2 e 8 \(IND\_SITUACAO\_ESP <> 1, 2 e 8\);

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no menu  “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__SPDIPAM12__”  e o parâmetro  “Lançar NF Escrituradas” igual a “S”;

\- Somente notas em que o estado da pessoa fis/jur \(remetente\) seja = “SP”

\- O Produto deve estar parametrizado na parametrização de produtos para o código 1\.2  

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

__Processamento das notas__:

Os itens recuperados conforme os critérios acima serão totalizados __por município da pessoa fis/jur \(\*\)__, e para cada município será gerado um registro 1400, da seguinte forma:

\(\*\) conforme regras da GIA\-SP

Valor a ser totalizado = valor contábil do item \(campo 64, SAFX08\)

 = = = = =

__Gravação do registro 1400:__

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                                     “__SPDIPAM12__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__SPDIPAM12__” 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                 \[Valor resultante da totalização\] 

                                              \(\+\)

              \[Campo “Outros Valores” informado manualmente\]

                                               \(\-\) 

             \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-SP\-03__

__Código SPDIPAM13__ 

\(Recebimentos, por cooperativas, de mercadorias remetidas por produtores rurais\)

A geração deste código da DIPAM\-B segue as regras da GIA\-SP, onde o município utilizado é o município da SAFX04\. lembrando que a GIA\-SP *não* usa o parâmetro 67 na geração da DIPAM\-B\.

__MFS877174/MFS910283__

Criação da tabela particionada DWT\_DOCTO\_FISCAL\_SPED espelho da DWT\_DOCTO\_FISCAL e utilização na geração dos registros C100, C500, D100, D500 e 1400 – UF = SP\.

__Origem__: \- Notas Fiscais \(SAFX07 e SAFX08\)

             \- Valores informados manualmente 

             \- Parametrização de CFOP e CFOP/NAT

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UF\)

             \- Parametrização de Produtos 

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UFàDIPAM\-B x Produto\)

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração \(ver OBS\)

\- MOVTO\_E\_S – somente as notas de entradas \(MOVTO\_E\_S <> “9”\)

\- Data Fiscal \- no período da geração ou data extemporânea no período da geração 

\- Modelo \(campo 13\) =  01, 1B, 04 ou 55

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- Somente notas com itens 

\- Somente itens de mercadoria

\- Situação = somente as não canceladas

\- Somente notas que não sejam transferências \(IND\_TRANSF\_CRED = “0”\)

\- Somente notas com situação especial <> 1, 2 e 8 \(IND\_SITUACAO\_ESP <> 1, 2 e 8\) 

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no menu

  “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__SPDIPAM13__”

\- Somente notas em que o estado da pessoa fis/jur \(remetente\) seja = “SP”

\- Dependendo da parametrização dos dados iniciais \(ver campo “*Dados para a geração *

*  específica \(DIPAM\-B – SP\)*”\), serão considerados apenas os itens com produtos

  parametrizados no menu “Parâmetros à  Registro 1400 à Específico por UF à

  DIPAM\-B x Produto”, da seguinte forma:

     Se parâmetro “*Utilizar a parametrização de produtos*” __marcado__: 

        Nesse caso, serão considerados *apenas* os itens com o produto parametrizado;

     Se parâmetro “*Utilizar a parametrização de produtos*” __desmarcado__: 

        Nesse caso, serão considerados qualquer tipo de produto;

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Da mesma forma que é feito na geração padrão e na geração de MG do registro 1400, a totalização dos itens para geração deste código da DIPAM, pode ser feita \(se possível\), durante a geração do registro C100 e filhos, para uma melhor performance\. Mas, observando que neste item trabalhamos com parametrização de CFOP e de produto \(opcionalmente\)\.

__Processamento das notas__:

Os itens recuperados conforme os critérios acima serão totalizados __por município da pessoa fis/jur \(\*\)__, e para cada município será gerado um registro 1400, da seguinte forma:

\(\*\) conforme regras da GIA\-SP

Valor a ser totalizado = valor contábil do item \(campo 64, SAFX08\)

 = = = = =

__Gravação do registro 1400:__

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                                     “__SPDIPAM13__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__SPDIPAM13__” 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                 \[Valor resultante da totalização\] 

                                              \(\+\)

              \[Campo “Outros Valores” informado manualmente\]

                                               \(\-\) 

             \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

*Observações sobre o código 13 na geração da DIPAM\-B da GIA\-SP*

Conforme a regra RN06 do documento “MTZ – GIA – SP \- Geração dos Registros”:

*\- Segundo esta regra serão recuperadas apenas notas com MOVTO\_E\_S = “2”, mas conforme testes realizados a geração recupera *todos* os CFOP’s parametrizados;*

*\- Segundo esta regra serão recuperadas apenas as notas cuja pessoa fis/jur tenha o campo “Classe de Pessoa Fis/Jur” = “2\-Cooperativa”\.  Mas conforme os testes realizados, esta regra não esta sendo aplicada\. *

*Conclusão à Em relação a estes dois pontos, a geração do 1400 para este código será desenvolvida conforme o funcionamento verificado na GIA\-SP, ou seja, estas regras não serão consideradas, já que não estão sendo utilizadas\.*

__RN1400\-SP\-04__

__\[MFS539087\]__ Inclusão do modelo 59 para recuperar as mesmas notas da GIA\-SP

__Código SPDIPAM22__ 

\(Vendas efetuadas por revendedores ambulantes autônomos, e outras operações\)

A geração deste código da DIPAM\-B segue as regras da GIA\-SP, onde o município utilizado é o município da SAFX04\. lembrando que a GIA\-SP *não* usa o parâmetro 67 na geração da DIPAM\-B\.

__MFS877174/MFS910283__

Criação da tabela particionada DWT\_DOCTO\_FISCAL\_SPED espelho da DWT\_DOCTO\_FISCAL e utilização na geração dos registros C100, C500, D100, D500 e 1400 – UF = SP\.

__Origem__: \- Notas Fiscais \(SAFX07 e SAFX08\)

               \- Valores informados manualmente 

               \- Parametrização de CFOP e CFOP/NAT

                 \(menu “ParâmetrosàRegistro 1400àEspecífico por UF\)

               \- Parametrização de Produtos 

                \(menu “ParâmetrosàRegistro 1400àEspecífico por UFàDIPAM\-B x Produto\)

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração \(ver OBS\)

\- MOVTO\_E\_S \- entradas __e__ saídas

\- Data Fiscal \- no período da geração ou data extemporânea no período da geração 

\- Modelo \(campo 13\) =  01, 1B, 04, 55 ou 59

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- Notas com __ou__ sem itens 

\- Se nota com itens, considerar apenas os itens de mercadoria

\- Situação = somente as não canceladas

\- Somente notas que não sejam transferências \(IND\_TRANSF\_CRED = “0”\)

\- Somente notas com situação especial <> 1, 2 e 8 \(IND\_SITUACAO\_ESP <> 1, 2 e 8\) 

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no menu

  “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__SPDIPAM22__”

\- Somente notas em que o estado da pessoa fis/jur \(remetente\) seja = “SP”

\- Dependendo da parametrização dos dados iniciais \(ver campo “*Dados para a geração *

*  específica \(DIPAM\-B – SP\)*”\), serão considerados apenas os itens com produtos

  parametrizados no menu “Parâmetros à  Registro 1400 à Específico por UF à

  DIPAM\-B x Produto”, da seguinte forma:

     Se parâmetro “*Utilizar a parametrização de produtos*” __marcado__: 

        Nesse caso, serão considerados *apenas* os itens com o produto parametrizado;

     Se parâmetro “*Utilizar a parametrização de produtos*” __desmarcado__: 

        Nesse caso, serão considerados qualquer tipo de produto;

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Da mesma forma que é feito na geração padrão e na geração de MG do registro 1400, a totalização dos itens para geração deste código da DIPAM, pode ser feita \(se possível\), durante a geração do registro C100 e filhos, para uma melhor performance\. Mas,  observando que neste item trabalhamos com parametrização de CFOP e de produto \(opcionalmente\)\.

__Processamento das notas__:

As notas recuperadas conforme os critérios acima serão agrupadas __por município da pessoa fis/jur \(\*\)__, e a totalização dos valores deste código __SPDIPAM22__ é feita da seguinte forma:

 \(conforme regras da GIA\-SP\)

Este código trabalha com o parâmetro “__Forma de Cálculo__” da tela de parametrização dos CFOP’s, e a totalização dos valores depende da opção escolhida pelo usuário para cada CFOP parametrizado\. 

 = = = = =

__Se forma de cálculo = Base de Cálculo ICMS Normal:__

    Neste caso, o total a ser apurado será o resultado abaixo, considerando todas as

    notas/itens com CFOP parametrizado para esta forma de cálculo:

Total \[Base de Cálculo \+ Isentas/Não Tributadas \+ Outras \+ Redução\] das saídas

  menos \(\-\) 

Total \[Base de Cálculo \+ Isentas/Não Tributadas \+ Outras \+ Redução\] das entradas

__Se forma de cálculo = Base de Cálculo ICMS Substituição Tributaria:__

    Neste caso, o total a ser apurado será o resultado abaixo, considerando todas as

    notas/itens com CFOP parametrizado para esta forma de cálculo:

Total \[Base de Cálculo ST\] das saídas

  menos \(\-\)

Total \[Base de Cálculo ST\] das entradas

 

__Se forma de cálculo = Valor Total NF – Revendedor Autônomo:__

    Neste caso, o total a ser apurado será o resultado abaixo, considerando todas as 

    notas/itens com CFOP parametrizado para esta forma de cálculo:

    \(esta forma de cálculo é apurada a partir *apenas* da notas de saída\) 

Alteração __MFS19151__: A geração do código 22 foi alterada para utilizar o valor contábil do item, em vez do valor total da nota, conforme a geração da GIA\-SP\.

   

Total das NFs de Saída \(Campo 64 \- VLR\_CONTAB\_ITEM – SAFX08\)  \* % IVA –RPA

     O percentual IVA\-RPA é a informação parametrizada nos dados iniciais\.

 = = = = =

Observar que poderão existir CFOP’s parametrizados com formas distintas de cálculo, e neste caso, o resultado final do código 22 para cada município, será a soma dos resultados obtidos para cada uma das formas de cálculo, conforme descrito acima\.

Exemplo:

NF

E/S

Item

CFOP

Vlr Contábil

Base

Isent/Out/Red

4

Entrada

1

1111

400,00

300,00

20,00

5

Saída

1

5111

2000,00

1800,00

50,00

2

5112

1000,00

600,00

50,00

      Resultados conforme a parametrização utilizada:

__CFOP__

__Forma de Cálculo__

__Teste 1 \- Resultado__:

\(1850\+ 650\) – 320 = __2180,00__

1111

Base de Cálculo Normal

5111

Base de Cálculo Normal

5112

Base de Cálculo Normal

__CFOP__

__Forma de Cálculo__

__Teste 2 \- Resultado__:

\[ \(1850 – 320\) \] \+ \[ \(1000 \* 40%\) \]

=

\[ 1530 \] \+ \[ 400 \] = __1930,00__

1111

Base de Cálculo Normal

5111

Base de Cálculo Normal

5112

Valor Total – Rever\. Autônomo

__CFOP__

__Forma de Cálculo__

__Teste 3 \- Resultado__:

\[  \(2000 \+ 1000\)  \* 40%\) \]

=

\[ 3000 \*  40% \] = __1200,00__

5111

Valor Total – Ver\. Autônomo

5112

Valor Total – Rever\. Autônomo

__CFOP__

__Forma de Cálculo__

__Teste 4 \- Resultado__:

\[ \(0 – 320\) \] \+  \[ \(2000 \+ 1000\)  \* 40%\) \]

=

\[ \-320 \] \+  \[ 3000 \*  40% \] = __880,00__

1111

Base de Cálculo Normal

5111

Valor Total – Rever\. Autônomo

5112

Valor Total – Rever\. Autônomo

= = = = =

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                                     “__SPDIPAM22__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__SPDIPAM22__” 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                 \[Valor resultante da totalização\] 

                                              \(\+\)

              \[Campo “Outros Valores” informado manualmente\]

                                               \(\-\) 

             \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-SP\-05__

__Código SPDIPAM23__ 

\(Transporte\)

<a id="OLE_LINK53"></a><a id="OLE_LINK54"></a><a id="OLE_LINK55"></a>Alteração __MFS7449__: A geração do código 23 foi alterada para tratar deduções, para ficar de acordo com a geração da GIA\-SP\.

Alteração __CH7744\_2018__: De acordo com a legislação uma das alterações promovidas pelo Ajuste SINIEF 10/2016 foi a substituição do modelo 7 para o modelo 67\. 

__MFS877174/MFS910283__

Criação da tabela particionada DWT\_DOCTO\_FISCAL\_SPED espelho da DWT\_DOCTO\_FISCAL e utilização na geração dos registros C100, C500, D100, D500 e 1400 – UF = SP\.

 

__Apuração dos valores das saídas:__

__   __

A geração deste código da DIPAM\-B segue as regras da GIA\-SP:

\-A geração recupera todos os documentos dos CFOP’s parametrizados, independente da classificação do documento\. Assim, serão recuperados tanto as notas fiscais de classificação 1 por exemplo, como os CTRC’s que têm a classificação = 4\.

\-O município utilizado no agrupamento é o município de origem da NF __ou__ o município de coleta dos itens de frete \(X51\), quando se tratar de notas de frete \(classificação 4/5/6\) em que o município origem da capa não esteja preenchido;

 

\(lembrando que a GIA\-SP *não* usa o parâmetro 67 na geração da DIPAM\-B\)

__Origem__: \- Notas Fiscais \(SAFX07 e SAFX08\)

             \- Valores informados manualmente 

             \- Parametrização de CFOP e CFOP/NAT

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UF\)

             \- Parametrização de Produtos 

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UFàDIPAM\-B x Produto\)

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração \(ver OBS\)

\- Somente notas de saída \(MOVTO\_E\_S = “9”\)

\- Data Fiscal \- no período da geração ou data extemporânea no período da geração 

\- Modelo \(campo 13\) =  __7, 8, 8B, 9, 10, 11, 26, 27, 57 ou 67;__

\- Classificação = __1, 3, 4, 5 ou 6__ 

\- No caso das notas de __classificação 1 ou 3__ à<a id="OLE_LINK41"></a><a id="OLE_LINK42"></a><a id="OLE_LINK43"></a> serão consideradas apenas as notas 

  em que a “*UF Origem*” da nota = “SP”;

\- No caso das notas de __classificação 4, 5 ou 6__ à serão consideradas apenas as 

  notas em que a “*UF Origem*” da nota  = “SP” __ou__, quando esta não for informada,  a 

  “UF de Coleta” dos itens de frete \(X51\) for = “SP”;   

\- Notas com ou sem itens 

\- Situação = somente as não canceladas

<a id="OLE_LINK44"></a><a id="OLE_LINK45"></a><a id="OLE_LINK46"></a>\- Somente notas que não sejam transferências \(IND\_TRANSF\_CRED = “0”\)

\- Somente notas com situação especial <> 1, 2 e 8 \(IND\_SITUACAO\_ESP <> 1, 2 e 8\) 

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no menu

  “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__SPDIPAM23__”

\- Assim como os demais códigos da DIPAM, a parametrização de produtos é 

  *opcional*, e quando utilizada, aplica\-se *apenas* aos itens da SAFX08 das notas com

   classificação 1 ou 3 \(já que as notas de classificação 4, 5 ou 6 nunca terão itens na

   SAFX08\);

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Da mesma forma que é feito na geração padrão e na geração de MG do registro 1400, a totalização das notas/itens para geração deste código da DIPAM, pode ser feita \(se possível\), durante a geração do registro D100 e filhos \(pois são notas de transporte\), para uma melhor performance\. Mas,  observando que neste item trabalhamos com parametrização de CFOP e de produto \(opcionalmente\)\.

<a id="OLE_LINK47"></a><a id="OLE_LINK48"></a><a id="OLE_LINK49"></a>__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados __por município \(\*\)__,__ __e para cada município será gerado um registro 1400\.

O município utilizado no agrupamento é o seguinte:

   \- Para as notas de classificação = 1 ou 3 à usa sempre o município de origem da

     NF \(SAFX07\);

   \- Para as notas de classificação = 4, 5 ou 6 à usa o município de origem da NF

     \(SAFX07\), __ou__, quando este não estiver preenchido, usa o município de coleta dos 

     itens de frete \(SAFX51\)\. Ao utilizar o município de coleta da SAFX51, caso exista 

     mais de um item de frete, e eles tiverem municípios de coleta *diferentes*, será

      gravada a seguinte mensagem no log, e o documento *não* será considerado:

*     “Existem na base de dados itens de frete para o documento com mais de um*

*      município de coleta\. O documento não será considerado na DIPAM\-B \(registro *

*     1400\)”*

     Caso o município da SAFX51 também não esteja preenhido, será gravada a 

     seguinte      mensagem no log, e o documento *não* será considerado: *“Para gerar *

*     a DIPAM\-B, cod 23, e necessário que o município de origem esteja preenchido *

*    \(UF/munic origem da SAFX07 ou munic Coleta da SAFX51\)\. O doc não será *

*    consid DIPAM\-B”*

*     \(são as mesmas mensagens utilizadas na geração da GIA\-ST\)*

Exemplo:

Nota fiscal: 25107

Classificação: 4 \(CTRC\)

CFOP: 5106

Município origem: Buri

Valor da Nota: 1\.000,00

Itens da X51: 1\-Município coleta: Pederneiras, Valor = 800,00; 

                      2\-Município coleta: Pederneiras, Valor = 200,00;

Neste cenário seria usado o município de origem da capa \(= Buri\)\.

Mas, se na capa o município de origem não estivesse preenchido, seria usado o município de Pederneiras;

Valor a ser totalizado:

\- Notas de classificação 1 ou 3 à valor contábil do item \(campo 64, SAFX08\) ou valor

   total da nota \(SAFX07\), no caso das notas sem itens;

\- Notas de classificação 4, 5 ou 6 à valor total da nota \(SAFX07\);

= = = = =

<a id="OLE_LINK38"></a><a id="OLE_LINK39"></a><a id="OLE_LINK40"></a><a id="OLE_LINK56"></a><a id="OLE_LINK57"></a><a id="OLE_LINK58"></a>__Apuração dos valores a serem deduzidos:     \(MFS7449\)__

O valor das deduções será apurado com base nas notas fiscais parametrizadas como dedução \(menu “Parâmetros à Registro 1400 à Especifico por UF à Deduções”\)\. 

Critérios de recuperação das notas para dedução \(SAFX07/SAFX08\):

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- MOVTO\_E\_S – somente notas de entrada \(MOVTO\_E\_S <> “9”\)

\- Data Fiscal  – deve ser uma data no período da geração \(ou notas com data

                          extemporânea no período da geração\)

\- Somente as notas não canceladas

\- Somente notas que não sejam transferências \(IND\_TRANSF\_CRED = “0”\)

\- Somente notas com situação especial <> 1, 2 e 8 \(IND\_SITUACAO\_ESP\) 

\- Somente as notas em que a “*UF Origem*” da nota = “SP”;

\- O CFOP ou CFOP e Natureza de Operação deve estar parametrizado no menu  

   “Parâmetros à  Registro 1400 à Específico p/UF à Deduções à CFOP ou 

    CFOP/Nat” para a operação do tipo “__SPDIPAM23__”

Para as notas com itens, será utilizado o CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP/Natureza da capa;

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados por município *de origem da nota* \(SAFX07\), utilizando os seguintes valores:

Valor a ser totalizado = valor contábil do item ou valor total da da nota:

\-Para as notas com itens, será totalizado o valor contábil dos itens;

\-Para as notas sem itens, será totalizado o valor total da nota;

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

= = = = =

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                                     “__SPDIPAM23__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__SPDIPAM23__” 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                             \[Valor resultante da totalização das saídas\]

<a id="OLE_LINK59"></a><a id="OLE_LINK60"></a><a id="OLE_LINK61"></a>                                                     \(\-\) 

                                 \[Valor resultante das deduções\]

                                                    \(\+\)

                  \[Campo “Outros Valores” informado manualmente\]

<a id="OLE_LINK50"></a><a id="OLE_LINK51"></a><a id="OLE_LINK52"></a>                                                    \(\-\) 

                 \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

__\[MFS45819\]__ Valor negativo não será gravado no arquivo, pois o validador critica\. Cliente demonstrou situação onde no mês não possui notas de saídas, mas possui notas de entrada classificadas como dedução, o que gerou valor negativo no 1400\.   O sistema interpretava que essa situação estaria incorreta, por isso o tratamento original era: dar mensagem no log e manter o resultado negativo no arquivo\. Dessa forma, o cliente poderia corrigir a base e regerar o meio magnético\.  Mas com esse novo cenário, entendemos que essa situação é possível, por isso retiramos a crítica e não levamos o registro 1400 com valor negativo pro arquivo, pois o validador rejeita\.

O ideal é que todas as regras do 1400 sejam revisadas para não gerar o registro com valor negativo no arquivo, e gerar uma mensagem no log sinalizando o ocorrido\. 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.

Resultado final negativo à O registro 1400 não será gravado para este município;

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, <a id="OLE_LINK62"></a><a id="OLE_LINK63"></a><a id="OLE_LINK64"></a>o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-SP\-06__

__Código SPDIPAM 24__ 

\(Comunicação\)

Alteração __MFS7449__: A geração do código 24 foi alterada para tratar deduções, para ficar de acordo com a geração da GIA\-SP\.

__MFS436036__ Inclusão das notas de modelo 62 \(NFCom\) nas Saídas \(SAFX42/43\)\. As notas de saída de modelo 62 consideradas para geração do 1400, são as apresentadas nos registros D700/D750\. Sendo assim, pelo menos um desses registros deve estar selecionado no perfil de geração para que essas notas venham a compor o 1400\.

__Apuração dos valores das saídas:__

__   __

*OBS: Na GIA\-SP, este código usa o parâmetro “*__*Considerar Município do Ponto de Consumo \(Utilities\)”*__*, e considera as notas da SAFX07/SAFX08 \(totalizando por munic\. da X04\) ou da SAFX42/SAFX43 \(totalizando p/munic\. do terminal faturado\), dependendo deste parâmetro\. No Sped não teremos este parâmetro\. A totalização das saídas será feita sempre pela SAFX42/SAFX43, considerando o município do ponto de consumo\.*

__Origem__: \- Notas Fiscais de Utilities \(__SAFX42 e SAFX43__\)

             \- Valores informados manualmente 

             \- Parametrização de CFOP e CFOP/NAT

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UF\)

             \- Parametrização de Produtos 

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UFàDIPAM\-B x Produto\)

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração \(ver OBS\)

\- MOVTO\_E\_S – notas de saídas \(na X42 só existem notas de saída\)

\- Data Fiscal \- no período da geração ou data extemporânea no período da geração 

\- Modelo =  21 ou 22 ou ‘62’

\- Classificação = 1 ou 3;

\- Somente notas com itens \(notas de utilities sempre terão itens\) 

\- No caso de nota mista \(classif\.= 3\), considerar *apenas* os itens de mercadoria

\- *Não* considera os itens informativos \(campo “10\-Tipo de Item” da SAFX43 = 1\)

\- Situação = somente as não canceladas

\- O município do terminal faturado \(campo 76 da SAFX42\) deve ser um município de 

  SP \(campo 75\-UF do Terminal Faturado deve ser “SP”\)

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no 

   menu

  “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__SPDIPAM24__”

\- Dependendo da parametrização dos dados iniciais \(ver campo “*Dados para a *

*  geração  específica \(DIPAM\-B – SP\)*”\), serão considerados apenas os itens com 

  produtos parametrizados no menu “Parâmetros à  Registro 1400 à Específico por 

  UF à DIPAM\-B x Produto”, da seguinte forma:

     Se parâmetro “*Utilizar a parametrização de produtos*” __marcado__: 

        Nesse caso, serão considerados *apenas* os itens com o produto parametrizado;

     Se parâmetro “*Utilizar a parametrização de produtos*” __desmarcado__: 

        Nesse caso, serão considerados qualquer tipo de produto;

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Da mesma forma que é feito na geração padrão e na geração de MG do registro 1400, a totalização das notas/itens para geração deste código da DIPAM, pode ser feita \(se possível\), durante a geração do registro D500/D600/D695 e filhos \(pois são notas de telecom\), para uma melhor performance\. Mas, observando que neste item trabalhamos com parametrização de CFOP e de produto \(opcionalmente\)\.

__Processamento das notas__:

Os itens recuperados conforme os critérios acima serão totalizados __por município do terminal faturado__,__ __e para cada município será gerado um registro 1400\.

Valor a ser totalizado: valor do serviço da SAFX43

= = = = =

__Apuração dos valores a serem deduzidos:     \(MFS7449\)__

O valor das deduções será apurado com base nas notas fiscais parametrizadas como dedução \(menu “Parâmetros à Registro 1400 à Especifico por UF à Deduções”\)\. 

Critérios de recuperação das notas para dedução \(SAFX07/SAFX08\):

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- MOVTO\_E\_S – somente notas de entrada \(MOVTO\_E\_S <> “9”\)

\- Data Fiscal  – deve ser uma data no período da geração \(ou notas com data

                          extemporânea no período da geração\)

\- Somente as notas não canceladas

\- Somente notas que não sejam transferências \(IND\_TRANSF\_CRED = “0”\)

\- Somente notas com situação especial <> 1, 2 e 8 \(IND\_SITUACAO\_ESP\) 

\- Serão consideradas somente as notas em que a UF da pessoa fis/jur emitente da

   nota \(SAFX04\) for = “SP” \(seguindo a mesma regra utilizada na GIA\-SP\);

\- O CFOP ou CFOP e Natureza de Operação deve estar parametrizado no menu  

   “Parâmetros à  Registro 1400 à Específico p/UF à Deduções à CFOP ou 

    CFOP/Nat” para a operação do tipo “__SPDIPAM24__”

Para as notas com itens, será utilizado o CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP/Natureza da capa;

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados por município *da pessoa fis/jur emitente*, utilizando os seguintes valores:

Valor a ser totalizado = valor contábil do item ou valor total da da nota:

\-Para as notas com itens, será totalizado o valor contábil dos itens;

\-Para as notas sem itens, será totalizado o valor total da nota;

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções *não* é obrigatória\. Sendo assim, quando *não* existirem dados parametrizados, __ou__, quando *não* existirem notas que atendam à parametrização, não haverá valor de dedução\.

= = = = =

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                                     “__SPDIPAM24__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__SPDIPAM24__” 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                           \[Valor resultante da totalização das saídas\] 

                                                     \(\-\) 

                                 \[Valor resultante das deduções\]

                                                    \(\+\)

                    \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                  \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-SP\-07\-A__

\(EE\-Comercialização\)

__Código SPDIPAM25__           \(Energia Elétrica – Comercialização\)

= = = = = =

__MFS2437__: Esta OS criou o parâmetro “Código 2\.5 \(Energia Elétrica\)” na tela dos “Dados Iniciais” e definiu regras diferenciadas para o segmento de energia elétrica\.

__MFS18797__: Esta MFS criou regras especificas para as empresas de geração de energia elétrica\. Assim, a  regra __RN1400\-SP\-07\-A__ será utilizada quando o parâmetro “Código 2\.5 \(Energia Elétrica\)” for = “Geração/Comercialização”, e para as empresas geradoras de energia \(opção “Geração”\), foi criada a __RN1400\-SP\-07\-C__\.

\(para opção do parâmetro = “Distribuição”, consultar a __RN1400\-SP\-07\-B__\) 

= = = = = =

   

A geração deste código da DIPAM\-B segue as regras da GIA\-SP: 

Se existir pelo menos um CFOP parametrizado para este código, será gravado apenas um registro 1400, com o município do Estabelecimento e o valor = 1,00\.

Obs: Este procedimento foi definido no 7195\_2013, e atende aos itens \(b\) e \(c\) descritos para o código 25 da DIPAM \(Geração e Comercialização de Energia Elétrica\)\. No caso dos distribuidores de energia \(item \(a\)\), não se aplica esta regra, no entanto, a GIA\-SP não tem tratamento para este tipo de contribuinte\.

 = = = = =

__Gravação do registro 1400:__

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                                     “__SPDIPAM25__” 

__03\-MUN__ à Este campo será preenchido considerando o município do Estabelecimento da geração\. Será gravada a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor 1,00\.

 = = = = =

No caso deste código, não haverá leitura de notas fiscais, e será gravado apenas um registro com o município do Estabelecimento\.

Mas, assim como para os demais códigos da DIPAM\-B, a geração irá considerar também a existência de valores incluídos manualmente na tela de manutenção do registro 1400, da seguinte forma:

Caso existam valores cadastrados para outros municípios \(<> munic do Estab\):

     Será gravado um registro 1400 para cada registro inserido na manutenção, além do

     registro do município do estabelecimento \(que será gravado com o valor 1,00\);

Caso exista valores cadastrados para o município do estabelecimento:

     Nesse caso, será gravado o registro 1400 para o município do estabelecimento com o

     valor informado na manutenção, e *não* será gravado o registro com valor 1,00;

 = = = = =

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__SPDIPAM25__” 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                 \[Valor resultante da totalização\] 

                        \(no caso deste código, este valor não existirá\)    

                                              \(\+\)

              \[Campo “Outros Valores” informado manualmente\]

                                               \(\-\) 

             \[Campo “Outras Deduções” informado manualmente\]

*\(a regra geral é essa, mas, no caso deste código SPDIPAM25 não existirá “Valor resultante da totalização”, pois não será feita nenhuma apuração dos valores\)*

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-SP\-07\-B__

\(EE\-Distribuição\)

__Código SPDIPAM25__           \(Energia Elétrica – Distribuição\)

= = = = = =

__MFS2437__: Esta OS criou o parâmetro “Código 2\.5 \(Energia Elétrica\)” na tela dos “Dados Iniciais” e definiu regras diferenciadas para o segmento de energia elétrica\.

A regra __RN1400\-SP\-07\-B__ será utilizada quando o parâmetro “Código 2\.5 \(Energia Elétrica\)” for = “Distribuição”\.

\(para opção do parâmetro = “Geração/Comercialização”, consultar a __RN1400\-SP\-07\-A__\) 

= = = = = =

Para as empresas de distribuição de energia elétrica os valores a serem gravados no registro 1400 serão recuperados do cálculo realizado no menu:  *“Pré\-Geração à Registro *__*1400*__* – Valores da DIPAM SP \- Energia Elétrica \(Distribuidores\) à Cálculo”*

Tabela: Tabela dos Valores Apurados por Município

Critérios para recuperação dos dados:

\- Código da empresa – código da empresa da geração;

\- Código do Estabelecimento – código do estabelecimento da geração;

\- Período – mês e ano do período referente a data final informada na tela da geração;

Na tabela existirão *várias linhas por período*, uma para cada município\. 

*Para cada município recuperado*, será gerado um registro 1400, da seguinte forma:

*\(caso não existam dados para o período, o registro será gerado apenas a partir dos dados inseridos manualmente, quando for o caso\)*

= = = = = =

__Gravação do registro 1400:__

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                                     “__SPDIPAM25__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o conteúdo do campo “*Valor Adicionado DIPAM*” da tabela, mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\), quando for o caso\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município em questão \(município a ser gravado no 1400\) 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__SPDIPAM25__” 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                \[Valor do campo “*Valor Adicionado DIPAM*” da tabela do cálculo\] 

*        \(os municípios em que este valor for negativo, será considerado o valor 1\)*

                                                         \(\+\)

                      \[Campo “Outros Valores” informado manualmente\]

                                                         \(\-\) 

                     \[Campo “Outras Deduções” informado manualmente\]

= = = = =

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor recuperado da tabela do cálculo \(“*Valor Adicionado DIPAM*”\), e também o valor final gravado no registro 1400, serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor recuperado da tabela do cálculo \(“*Valor Adicionado DIPAM*”\) será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-SP\-07\-C__

\(EE\-Geradoras\)

__Código SPDIPAM25__           \(Energia Elétrica – Geração\)

= = = = =

__MFS18797__: Esta OS criou regras especificas para a geração do código 2\.5 para as empresas geradoras de de energia elétrica\. A regra __RN1400\-SP\-07\-C__ será utilizada quando o parâmetro “Código 2\.5 \(Energia Elétrica\)” for = “Geração”\.

= = = = =

__\[MFS710672\] __Inclusão do modelo de nota “66”

__MFS877174/MFS910283__

Criação da tabela particionada DWT\_DOCTO\_FISCAL\_SPED espelho da DWT\_DOCTO\_FISCAL e utilização na geração dos registros C100, C500, D100, D500 e 1400 – UF = SP\.

A geração deste código da DIPAM\-B segue as regras da GIA\-SP\.

Para as geradoras serão totalizadas todas as operações de saída do período, e o resultado lançado para o município do estabelecimento\. A recuperação das notas será feita da SAFX07/SAFX08, considerando os CFOP/Nat parametrizados, produtos parametrizados e modelo = 06, 66 ou 55\.

*\(Obs: Nesse caso não é necessário ler as tabelas de Utilities, pois não será utilizado nenhum detalhamento de município, pessoa fis/jur, etc\.\)*

*= = = = =*

Origem dos dados: SAFX07 / SAFX08 

Critérios para recuperação das notas:

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração

   Obs: Quando se tratar de geração por inscrição estadual única, serão recuperadas

   as notas do estabelecimento selecionado em tela \(centralizador\), e também de

    todos os estabelecimentos centralizados por ele, considerando a parametrização

    da inscrição estadual única do módulo de controle das obrigações estaduais\.

\- Movimento E/S – apenas as notas de saída \(MOVTO\_E\_S = ‘9’\);

\- Data Emissão/Escrita Fiscal \(DATA\_FISCAL\) – deve ser uma data referente ao

   período solicitado em tela; 

\- Modelo = __06__ \(EE\), __66__ \(NF3e\) ou __55__ \(NFe\)

\- Situação \- apenas as notas *não* canceladas;

\- Classificação do documento = 1 ou 3;

\- Considerar *apenas* os itens com CFOP ou CFOP/Natureza parametrizados para o 

   código 2\.5 da DIPAM \(__\*\*\*__\)\. Para acessar a parametrização, considerar o

   estabelecimento da geração e o código DIPAM\-B = “__25__”;  

    \(__\*\*\*__\) Menu “*Parâmetros > Nova GIA \- V8\.0 \(V0210\) > DIPAM\-B \- Reg\. 30 > Código*

*           de DIPAM\-B x CFOP’s \- Reg\.30*” ou “*Código de DIPAM\-B x CFOP’s / Natureza*

*           de Operação \- Reg\.30*”\.

\- Dependendo da parametrização dos Dados Iniciais, serão considerados *apenas* os

   itens com produto parametrizado no item “*Parâmetros > Nova GIA\-V8\.0 \(V0210\) >*

*   DIPAM\-B\- Reg\. 30 > Código de DIPAM\-B x Produto”:*

     Se parâmetro “*Utilizar a parametrização de produtos*” __marcado__: 

        Nesse caso, serão considerados *apenas* os itens com o produto parametrizado;

     Se parâmetro “*Utilizar a parametrização de produtos*” __desmarcado__: 

        Nesse caso, será considerado qualquer tipo de produto;

A totalização dos valores será feita a partir do campo “Valor Contábil do Item” dos itens da SAFX08\. 

= = = = =

__Gravação do registro 1400:__

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                                     “__SPDIPAM25__” 

__03\-MUN__ à Este campo será preenchido considerando o município do Estabelecimento da geração\. Será gravada a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização das notas, mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município do estabelecimento \(conforme descrito acima\) 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__SPDIPAM25__” 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                 \[Valor resultante da totalização\] 

                                                   \(\+\)

                   \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                   \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-SP\-08__

__Código SPDIPAM26__ 

\(Produção agropecuária própria ou em propriedades arrendadas\)

A geração deste código da DIPAM\-B segue as regras da GIA\-SP, onde o município utilizado é o município da SAFX04\. lembrando que a GIA\-SP *não* usa o parâmetro 67 na geração da DIPAM\-B\.

__MFS877174/MFS910283__

Criação da tabela particionada DWT\_DOCTO\_FISCAL\_SPED espelho da DWT\_DOCTO\_FISCAL e utilização na geração dos registros C100, C500, D100, D500 e 1400 – UF = SP\.

__Origem__: \- Notas Fiscais \(SAFX07 e SAFX08\)

             \- Valores informados manualmente 

             \- Parametrização de CFOP e CFOP/NAT

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UF\)

             \- Parametrização de Produtos 

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UFàDIPAM\-B x Produto\)

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração \(ver OBS\)

\- MOVTO\_E\_S – somente as notas de entradas \(MOVTO\_E\_S <> “9”\)

\- Data Fiscal \- no período da geração ou data extemporânea no período da geração 

\- Modelo \(campo 13\) =  01, 1B, 04 ou 55

\- Classificação – notas de mercadoria \(Classificação 1 e 3\)

\- Somente notas com itens 

\- Somente itens de mercadoria

\- Situação = somente as não canceladas

\- Somente notas que não sejam transferências \(IND\_TRANSF\_CRED = “0”\)

\- Somente notas com situação especial <> 1, 2 e 8 \(IND\_SITUACAO\_ESP <> 1, 2 e 8\) 

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no menu

  “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__SPDIPAM26__”

\- Somente notas em que o estado da pessoa fis/jur \(remetente\) seja = “SP”

\- Dependendo da parametrização dos dados iniciais \(ver campo “*Dados para a geração *

*  específica \(DIPAM\-B – SP\)*”\), serão considerados apenas os itens com produtos

  parametrizados no menu “Parâmetros à  Registro 1400 à Específico por UF à

  DIPAM\-B x Produto”, da seguinte forma:

     Se parâmetro “*Utilizar a parametrização de produtos*” __marcado__: 

        Nesse caso, serão considerados *apenas* os itens com o produto parametrizado;

     Se parâmetro “*Utilizar a parametrização de produtos*” __desmarcado__: 

        Nesse caso, serão considerados qualquer tipo de produto;

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Da mesma forma que é feito na geração padrão e na geração de MG do registro 1400, a totalização dos itens para geração deste código da DIPAM, pode ser feita \(se possível\), durante a geração do registro C100 e filhos, para uma melhor performance\. Mas,  observando que neste item trabalhamos com parametrização de CFOP e de produto \(opcionalmente\)\.

	

__Processamento das notas__:

Os itens recuperados conforme os critérios acima serão totalizados __por município da pessoa fis/jur \(\*\)__, e para cada município será gerado um registro 1400, da seguinte forma:

\(\*\) conforme regras da GIA\-SP

Valor a ser totalizado = valor contábil do item \(campo 64, SAFX08\)

*Observações sobre o código 26 na geração da DIPAM\-B da GIA\-SP*

Conforme a regra RN07 do documento “MTZ – GIA – SP \- Geração dos Registros”:

*Segundo esta regra os valores totalizados seriam as bases de cálculo, mas conforme testes realizados a geração totaliza o valor contábil dos itens;*

*A geração do 1400 para este código será desenvolvida conforme o funcionamento verificado na GIA\-SP, ou seja, esta regra não será considerada, já que não esta sendo utilizada\.*

= = = = =

__Gravação do registro 1400:__

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                                     “__SPDIPAM26__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__SPDIPAM26__” 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                 \[Valor resultante da totalização\] 

                                              \(\+\)

              \[Campo “Outros Valores” informado manualmente\]

                                               \(\-\) 

             \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-SP\-09__

__Código SPDIPAM31__ 

\(Saídas não escrituradas e outros ajustes\)

__\[ALTERADA – CH14943\_2015\]	__

A geração deste código da DIPAM\-B segue as regras da GIA\-SP\. Diferente dos demais códigos, os códigos iniciados por “3” \(31, 35 e 36\) *não são apurados por município*\. 

No caso de preenchimento do código SPDIPAM31, efetuar rateio somente ao município onde está inscrito o estabelecimento, ou seja, o município correspondente aos três primeiros dígitos da Inscrição Estadual\.

O valor total resultante da apuração é lançado num único registro 1400, com o município igual a do estabelecimento\.

__MFS877174/MFS910283__

Criação da tabela particionada DWT\_DOCTO\_FISCAL\_SPED espelho da DWT\_DOCTO\_FISCAL e utilização na geração dos registros C100, C500, D100, D500 e 1400 – UF = SP\.

*OBS: Apesar do título deste código 31 ser “não escrituradas”, a geração da GIA\-SP não considera as notas parametrizadas com classificação “7”, e sim classificação 1, 2 ou 3\. Por isso, acredita\-se que a geração deste código na GIA\-SP tenha sido desenvolvida para atender a outro tipo de operação, já que a descrição deste código no manual da DIPAM\-B cita várias outras coisas além de saídas não escrituradas\.*

__Origem__: \- Notas Fiscais \(SAFX07 e SAFX08\)

             \- Valores informados manualmente 

             \- Parametrização de CFOP e CFOP/NAT

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UF\)

             \- Parametrização de Produtos 

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UFàDIPAM\-B x Produto\)

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração \(ver OBS\)

\- MOVTO\_E\_S \- entradas __e__ saídas

\- Data Fiscal \- no período da geração ou data extemporânea no período da geração 

\- Modelo \(campo 13\) =  01, 1B, 04 ou 55

\- Classificação = 1 ou 3

\- Notas com __ou__ sem itens 

\- Se nota com itens, considera apenas os itens de mercadoria

\- Situação = somente as não canceladas

\- Somente notas que não sejam transferências \(IND\_TRANSF\_CRED = “0”\)

\- Somente notas com situação especial <> 1, 2 e 8 \(IND\_SITUACAO\_ESP <> 1, 2 e 8\) 

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no menu

  “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__SPDIPAM31__”

__\[MFS34187\] __Retirar o filtro do estado, para possibilitar a recuperação das notas interestaduais

\- Dependendo da parametrização dos dados iniciais \(ver campo “*Dados para a geração *

*  específica \(DIPAM\-B – SP\)*”\), serão considerados apenas os itens com produtos

  parametrizados no menu “Parâmetros à  Registro 1400 à Específico por UF à

  DIPAM\-B x Produto”, da seguinte forma:

     Se parâmetro “*Utilizar a parametrização de produtos*” __marcado__: 

        Nesse caso, serão considerados *apenas* os itens com o produto parametrizado;

     Se parâmetro “*Utilizar a parametrização de produtos*” __desmarcado__: 

        Nesse caso, serão considerados qualquer tipo de produto;

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Da mesma forma que é feito na geração padrão e na geração de MG do registro 1400, a totalização dos itens para geração deste código da DIPAM, pode ser feita \(se possível\), durante a geração do registro C100 e filhos, para uma melhor performance\. Mas, observando que neste item trabalhamos com parametrização de CFOP e de produto \(opcionalmente\)\.

__Processamento das notas__:

A apuração deste código __SPDIPAM31__ é feita da seguinte forma:

*\(conforme regras da GIA\-SP, este código não é apurado por município\)   *

Este código trabalha com o parâmetro “__Forma de Cálculo__” da tela de parametrização dos CFOP’s, e a totalização dos valores depende da opção escolhida pelo usuário para cada CFOP parametrizado\. 

Assim com o código 22, o código 31 também trabalha com formas de cálculo variáveis, sendo que neste caso existem apenas duas opções: 

__Se forma de cálculo = Base de Cálculo ICMS Normal:__

    Neste caso, o total a ser apurado será o resultado abaixo, considerando todas as

    notas/itens com CFOP parametrizado para esta forma de cálculo:

Total \[Base de Cálculo \+ Isentas/Não Tributadas \+ Outras \+ Redução\] das saídas

  menos \(\-\) 

Total \[Base de Cálculo \+ Isentas/Não Tributadas \+ Outras \+ Redução\] das entradas

__Se forma de cálculo = Valor Total NF – Revendedor Autônomo:__

    Neste caso, o total a ser apurado será o resultado abaixo, considerando todas as 

    notas/itens com CFOP parametrizado para esta forma de cálculo:

    \(esta forma de cálculo é apurada a partir *apenas* da notas de saída\) 

   

Total das NFs de Saída \(Campo 23 \- VLR\_TOT\_NOTA – SAFX07\)  \* % IVA – RPA

     O percentual IVA\-RPA é a informação parametrizada nos dados iniciais\.

 = = = = =

Observar que poderão existir CFOP’s parametrizados com formas distintas de cálculo, e neste caso, o resultado final do código 31 será a soma dos resultados obtidos para cada uma das formas de cálculo, conforme descrito acima\.

Exemplo:  *\(aplica\-se o mesmo o exemplo descrito para o código 22\)* 

= = = = =

__Gravação do registro 1400:__

O resultado apurado será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                                     “__SPDIPAM31__” 

__03\-MUN__ à 

Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município do estabelecimento do contribuinte\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – brancos *\(ver OBS sobre o campo município\)*

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__SPDIPAM31__” 

\(__\*\*\*__\) Sobre o preenchimento do município: 

*Os códigos 31, 35 e 36 não são apurados por município, e por isso, existirá apenas um registro 1400 para cada um destes códigos, e sempre com o município*__* igual a do estabelecimento, pois o PVA da Receita não aceita código igual a zeros ou em branco por ser campo obrigatório e no manual da DIPAM 2015 fizeram alterações para contemplar tal crítica, em que esses códigos devem ser preenchidos com o código de município IBGE do estabelecimento*__*\. Para esses casos, a manutenção do registro 1400 deve preencher o campo “Município” automaticamente com o código de município do estabelecimento \(concatenando UF\+Código do Município\)\.\. *

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                 \[Valor resultante da totalização\] 

                                                  \(\+\)

                  \[Campo “Outros Valores” informado manualmente\]

                                                   \(\-\) 

                 \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estabelecimento\+Operação\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\.

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-SP\-10__

__Código SPDIPAM35__ 

\(Entradas não escrituradas e outros ajustes\)

__\[ALTERADA – CH14943\_2015\]	__

A geração deste código da DIPAM\-B segue as regras da GIA\-SP\. Diferente dos demais códigos, os códigos iniciados por “3” \(31, 35 e 36\) *não são apurados por município*\. 

No caso de preenchimento do código SPDIPAM35, efetuar rateio somente ao município onde está inscrito o estabelecimento, ou seja, o município correspondente aos três primeiros dígitos da Inscrição Estadual\.

O valor total resultante da apuração é lançado num único registro 1400, com o município igual a do estabelecimento\.

__MFS877174/MFS910283__

Criação da tabela particionada DWT\_DOCTO\_FISCAL\_SPED espelho da DWT\_DOCTO\_FISCAL e utilização na geração dos registros C100, C500, D100, D500 e 1400 – UF = SP\.

__Origem__: \- Notas Fiscais \(SAFX07 e SAFX08\)

             \- Valores informados manualmente 

             \- Parametrização de CFOP e CFOP/NAT

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UF\)

             \- Parametrização de Produtos 

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UFàDIPAM\-B x Produto\)

Como são notas não escrituradas, estas notas não constarão do C100\.

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração \(ver OBS\)

\- MOVTO\_E\_S \- somente entradas com MOVTO\_E\_S = __3, 4 ou 5__;

\- Data Fiscal \- no período da geração ou data extemporânea no período da geração 

\- Modelo \(campo 13\) =  01, 1B, 04 ou 55

\- Classificação = __7__ \(notas de mercadoria *não* escrituradas\)

*  \(Obs: O documento de regras da GIA\-SP cita classificação 7 ou 8 \(nota de serviço\),*

*   mas será tratada apenas a “7”, já que a regra do MOVTO\_E\_S \(= 3, 4 ou 5\) se refere a notas de entrada de mercadorias\) *

\- Notas com __ou__ sem itens 

\- Situação = somente as não canceladas

\- Somente notas que não sejam transferências \(IND\_TRANSF\_CRED = “0”\)

\- Somente notas com situação especial <> 1, 2 e 8 \(IND\_SITUACAO\_ESP <> 1, 2 e 8\) 

\- Somente operações internas \(CFOP deve ser iniciado por “1”\)  

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no menu

  “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__SPDIPAM35__”

\- Dependendo da parametrização dos dados iniciais \(ver campo “*Dados para a geração *

*  específica \(DIPAM\-B – SP\)*”\), serão considerados apenas os itens com produtos

  parametrizados no menu “Parâmetros à  Registro 1400 à Específico por UF à

  DIPAM\-B x Produto”, da seguinte forma:

     Se parâmetro “*Utilizar a parametrização de produtos*” __marcado__: 

        Nesse caso, serão considerados *apenas* os itens com o produto parametrizado;

     Se parâmetro “*Utilizar a parametrização de produtos*” __desmarcado__: 

        Nesse caso, serão considerados qualquer tipo de produto;

__\[ALTERADA – CH9368\_2018 \(MFS\-18062\)\]	__

Será necessário incluir uma exceção a partir dessa MFS para tratar outros ajustes, pois na DIPAM os valores lançados no CFOP 5927 cujas entradas originais foram lançadas em CFOP não relacionados no Anexo 1 do manual deverão ser declarados neste código, então, selecionar todos os documentos fiscais quê:

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração \(ver OBS\)

\- MOVTO\_E\_S \- somente saídas com MOVTO\_E\_S = __9__;

\- Data Fiscal \- no período da geração ou data extemporânea no período da geração 

\- Modelo \(campo 13\) =  01, 1B, 04 ou 55

\- Classificação = __1__ \(notas de mercadoria\)

\- Notas com __ou__ sem itens 

\- Situação = somente as não canceladas

\- Somente notas que não sejam transferências \(IND\_TRANSF\_CRED = “0”\)

\- Somente notas com situação especial <> 1, 2 e 8 \(IND\_SITUACAO\_ESP <> 1, 2 e 8\) 

\- Somente operação “5927” parametrizado no menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__SPDIPAM35__”

\- Dependendo da parametrização dos dados iniciais \(ver campo “*Dados para a geração específica \(DIPAM\-B – SP\)*”\), serão considerados apenas os itens com produtos parametrizados no menu “Parâmetros à  Registro 1400 à Específico por UF àDIPAM\-B x Produto”, da seguinte forma:

     Se parâmetro “*Utilizar a parametrização de produtos*” __marcado__: 

        Nesse caso, serão considerados *apenas* os itens com o produto parametrizado;

     Se parâmetro “*Utilizar a parametrização de produtos*” __desmarcado__: 

        Nesse caso, serão considerados qualquer tipo de produto;

__\[ALTERADA– MFS\-37408 \- CH9601/2020 \- MFS\-58410 \- Cliente Yamaha\] __

__\[ALTERADA– MFS\-85762\] __Alteração para tratar outros tipos de nota de entrada

__ __Tratamento nas Operações de Entradas de Remessa em Garantia \- Inclusão do MOVTO\_E\_S  igual a “1”

Para equiparar ao ajuste efetuado na GIA\-SP pela demanda “__MFS\-37408”__, conforme solicitação do cliente Yamaha, e conforme considerações da área de informação, reforçando que as operações de Entradas de Remessa em Garantia devem ser informado no Registro 35 da DIPAM\-B, diante ao exposto essa regra será replicada para o Registro 1400 para a operação “__SPDIPAM35”:__

*Tratamento: Considerar as Notas Fiscais de *Operações de Entradas de Remessa em Garantia\.

\- Código da empresa – código da empresa da geração;

\- Código do Estabelecimento – código do estabelecimento da geração;

\- MOVTO\_E\_S \- entradas com MOVTO\_E\_S = 1, 3, 4 ou 5;

\- Data Fiscal \- no período da geração ou data extemporânea no período da geração; 

\- Modelo \(campo 13\) =  01, 1B, 04 ou 55;

\- COD\_CLASS\_DOC\_FIS = 1;

\- Somente operações parametrizado no menu “Parâmetros à  Registro 1400 à Específico por UF” à CFOP / CFOP/Natureza de Operação para a operação “__SPDIPAM35__”\.

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados, e será gerado um único registro 1400, da seguinte forma:

*\(conforme regras da GIA\-SP, este código não é apurado por município\)   *

Valor a ser totalizado: valor contábil do item ou valor total da nota, se nota sem itens;

__Gravação do registro 1400:__

O resultado apurado será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                                     “__SPDIPAM35__” 

__03\-MUN__ à 

Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município do estabelecimento do contribuinte\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – brancos *\(ver OBS sobre o campo município\)*

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__SPDIPAM35__” 

\(__\*\*\*__\) Sobre o preenchimento do município: 

*Os códigos 31, 35 e 36 não são apurados por município, e por isso, existirá apenas um registro 1400 para cada um destes códigos, e sempre com o município*__* igual a do estabelecimento, pois o PVA da Receita não aceita código igual a zeros ou em branco por ser campo obrigatório e no manual da DIPAM 2015 fizeram alterações para contemplar tal crítica, em que esses códigos devem ser preenchidos com o código de município IBGE do estabelecimento*__*\. Para esses casos, a manutenção do registro 1400 deve preencher o campo “Município” automaticamente com o código de município do estabelecimento \(concatenando UF\+Código do Município\)\.\. *

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                 \[Valor resultante da totalização\] 

                                                  \(\+\)

                  \[Campo “Outros Valores” informado manualmente\]

                                                   \(\-\) 

                 \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estabelecimento\+Operação\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\.

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-SP\-11__

__Código SPDIPAM36__ 

\(Entradas não escrituradas de produtores não equiparados\)

__\[ALTERADA – CH14943\_2015\]	__

A geração deste código da DIPAM\-B segue as regras da GIA\-SP\. Diferente dos demais códigos, os códigos iniciados por “3” \(31, 35 e 36\) *não são apurados por município*\. 

No caso de preenchimento do código SPDIPAM36, efetuar rateio somente ao município onde está inscrito o estabelecimento, ou seja, o município correspondente aos três primeiros dígitos da Inscrição Estadual\.

O valor total resultante da apuração é lançado num único registro 1400, com o município igual a do estabelecimento\.

__MFS877174/MFS910283__

Criação da tabela particionada DWT\_DOCTO\_FISCAL\_SPED espelho da DWT\_DOCTO\_FISCAL e utilização na geração dos registros C100, C500, D100, D500 e 1400 – UF = SP\.

__Origem__: \- Notas Fiscais \(SAFX07 e SAFX08\)

             \- Valores informados manualmente 

             \- Parametrização de CFOP e CFOP/NAT

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UF\)

             \- Parametrização de Produtos 

               \(menu “ParâmetrosàRegistro 1400àEspecífico por UFàDIPAM\-B x Produto\)

Como são notas não escrituradas, estas notas não constarão do C100\.

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração \(ver OBS\)

\- MOVTO\_E\_S \- somente entradas com MOVTO\_E\_S = __2__;

\- Data Fiscal \- no período da geração ou data extemporânea no período da geração 

\- Modelo \(campo 13\) =  01, 1B, 04 ou 55

\- Classificação = __7__ \(notas de mercadoria *não* escrituradas\)

*  \(Obs: O documento de regras da GIA\-SP cita classificação 7 ou 8 \(nota de serviço\),*

*   mas será tratada apenas a “7”, já que a regra do MOVTO\_E\_S \(= 2\) se refere a*

*   notas de entrada de mercadorias\) *

\- Notas com __ou__ sem itens 

\- Situação = somente as não canceladas

\- Somente notas que não sejam transferências \(IND\_TRANSF\_CRED = “0”\)

\- Somente notas com situação especial <> 1, 2 e 8 \(IND\_SITUACAO\_ESP <> 1, 2 e 8\) 

\- Somente operações internas \(CFOP deve ser iniciado por “1”\);

\- A pessoa fis/jur da nota deve ter o campo “Classe da Pessoa Fis/Jur” <> 

  Cooperativa  \(campo 26 da SAFX04 <> 02\)

\- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no

  Menu   “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__SPDIPAM36__”

\- Dependendo da parametrização dos dados iniciais \(ver campo “*Dados para a *

*  Geração específica \(DIPAM\-B – SP\)*”\), serão considerados apenas os itens com 

  produtos parametrizados no menu “Parâmetros à  Registro 1400 à Específico por  

   UF à DIPAM\-B x Produto”, da seguinte forma:

     Se parâmetro “*Utilizar a parametrização de produtos*” __marcado__: 

        Nesse caso, serão considerados *apenas* os itens com o produto parametrizado;

     Se parâmetro “*Utilizar a parametrização de produtos*” __desmarcado__: 

        Nesse caso, serão considerados qualquer tipo de produto;

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

__Processamento das notas__:

As notas/itens recuperados conforme os critérios acima serão totalizados, e será gerado um único registro 1400, da seguinte forma:

*\(conforme regras da GIA\-SP, este código não é apurado por município\)   *

Valor a ser totalizado: valor contábil do item ou valor total da nota, se nota sem itens;

__Gravação do registro 1400:__

O resultado apurado será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                                     “__SPDIPAM36__” 

__03\-MUN__ à 

Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município do estabelecimento do contribuinte\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – brancos *\(ver OBS sobre o campo município\)*

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__SPDIPAM36__” 

\(__\*\*\*__\) Sobre o preenchimento do município: 

*Os códigos 31, 35 e 36 não são apurados por município, e por isso, existirá apenas um registro 1400 para cada um destes códigos, e sempre com o município*__* igual a do estabelecimento, pois o PVA da Receita não aceita código igual a zeros ou em branco por ser campo obrigatório e no manual da DIPAM 2015 fizeram alterações para contemplar tal crítica, em que esses códigos devem ser preenchidos com o código de município IBGE do estabelecimento*__*\. Para esses casos, a manutenção do registro 1400 deve preencher o campo “Município” automaticamente com o código de município do estabelecimento \(concatenando UF\+Código do Município\)\.\. *

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                 \[Valor resultante da totalização\] 

                                                  \(\+\)

                  \[Campo “Outros Valores” informado manualmente\]

                                                   \(\-\) 

                 \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estabelecimento\+Operação\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\.

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.

__RN1400\-SP\-12__

__Código SPDIPAM27__

\(vendas presenciais com saídas em outro estabelecimento\)

A geração deste código da DIPAM\-B segue as regras da GIA\-SP, onde o município utilizado é o município da SAFX04, lembrando que a GIA\-SP *não* usa o parâmetro 67 na geração da DIPAM\-B\.

__MFS877174/MFS910283__

Criação da tabela particionada DWT\_DOCTO\_FISCAL\_SPED espelho da DWT\_DOCTO\_FISCAL e utilização na geração dos registros C100, C500, D100, D500 e 1400 – UF = SP\.

__Origem__:

- Notas Fiscais \(SAFX07 e SAFX08\)
- Valores informados manualmente 
- Parametrização de CFOP e CFOP/NAT

\(menu “ParâmetrosàRegistro 1400àEspecífico por UF\)

- Parametrização de Produtos 

\(menu “ParâmetrosàRegistro 1400àEspecífico por UFàDIPAM\-B x Produto\)

__Recuperação das Informações:__

- Código da empresa – código da empresa da geração
- Código do Estabelecimento – código do estabelecimento da geração \(ver OBS\)
- MOVTO\_E\_S \- saídas
- Data Fiscal \- no período da geração ou data extemporânea no período da geração 
- Modelo \(campo 13\) =  01, 1B, 04, 55 ou 65
- Classificação – notas de mercadoria \(Classificação 1 e 3\)
- Notas com __ou__ sem itens 
- Se nota com itens, considerar apenas os itens de mercadoria
- Situação = somente as não canceladas
- Somente notas que não sejam de devolução \(NORM\_DEV <> 2\)
- Somente notas que não sejam transferências \(IND\_TRANSF\_CRED = “0”\)
- Somente notas com situação especial <> 1, 2 e 8 \(IND\_SITUACAO\_ESP <> 1, 2 e 8\) 
- O CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__SPDIPAM27__”
- Somente notas em que o estado da pessoa fis/jur \(remetente\) seja = “SP”
- Dependendo da parametrização dos dados iniciais \(ver campo “*Dados para a geração específica \(DIPAM\-B – SP\)*”\), serão considerados apenas os itens com produtos parametrizados no menu “Parâmetros à  Registro 1400 à Específico por UF à DIPAM\-B x Produto”, da seguinte forma:
	- Se parâmetro “*Utilizar a parametrização de produtos*” __marcado__: Nesse caso, serão considerados *apenas* os itens com o produto parametrizado;
	- Se parâmetro “*Utilizar a parametrização de produtos*” __desmarcado__: Nesse caso, serão considerados qualquer tipo de produto;

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Da mesma forma que é feito na geração padrão e na geração de MG do registro 1400, a totalização dos itens para geração deste código da DIPAM, pode ser feita \(se possível\), durante a geração do registro C100 e filhos, para uma melhor performance\. Mas,  observando que neste item trabalhamos com parametrização de CFOP e de produto \(opcionalmente\)\.

__Processamento das notas__:

As notas recuperadas conforme os critérios acima serão agrupadas __por município da pessoa fis/jur \(\*\)__, e a totalização dos valores deste código __SPDIPAM27__ é feita da seguinte forma:

\(conforme regras da GIA\-SP\)

Valor a ser totalizado = valor da Base de Cálculo ICMS, Base ICMS Isenta ou Base ICMS Outras \(campo 56 da SAFX08 de acordo com o tipo da tributação informado no campo 55 ou campo 51, 52 ou 53 da SAFX07 se não houver item na nota fiscal\) >> 

Não iremos utilizar o valor contábil por conta de neste campo constar outros valores que podem diferir do que o fisco exige como sendo “valor das saídas de mercadorias”\. É viável utilizar as colunas referente à incidência do ICMS \(Base de Cálculo, Isentas e Outras\) pois serão os valores que constarão no demonstrativo por CFOP´s na GIA SP e apuração do ICMS no bloco E da EFD ICMS/IPI\. 

= = = = =

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o seguinte conteúdo:

                                     “__SPDIPAM27__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\. 

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__SPDIPAM27__” 

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

                                 \[Valor resultante da totalização\] 

                                              \(\+\)

              \[Campo “Outros Valores” informado manualmente\]

                                               \(\-\) 

             \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR está com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, e o valor final será gravado no campo “Valor Total”\.


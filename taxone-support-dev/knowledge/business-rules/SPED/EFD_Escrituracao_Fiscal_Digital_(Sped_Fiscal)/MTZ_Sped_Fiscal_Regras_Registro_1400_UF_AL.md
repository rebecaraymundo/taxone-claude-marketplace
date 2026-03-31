# MTZ_Sped_Fiscal_Regras_Registro_1400_UF_AL

- **Fonte:** MTZ_Sped_Fiscal_Regras_Registro_1400_UF_AL.docx
- **Modificado:** 2024-12-05
- **Tamanho:** 89 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Registro 1400 – Específico por UF \- AL

__Localização__: 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS94497

Aline Melo

Criação do documento\.

Inclusão do código 1201 no processo automático do registro 1400, para o estado de Alagoas\.

19/10/2022

MFS436036

Liliane Assaf

Tratamento das notas de saída de modelo 62 \(NFCom\) na geração do registro 1400\.

29/09/2023

MFS607283

Graciela Soares

Inclusão dos códigos __1202 \(UF Alagoas\) __e __PI004 \(UF Piauí\)__ no processo automático do registro 1400 para Entradas\.

30/01/2024

MFS607284

Graciela Soares

Inclusão dos códigos __1202 \(UF Alagoas\) __e __PI004 \(UF Piauí\)__ no processo automático do registro 1400 para Saídas\.

06/02/2024

# <a id="_Toc75782997"></a>Registro 1400 para o tipo de geração \- Específico por UF<a id="_Toc75782998"></a> \- AL

__RN1400\-AL__

A geração do 1400 para a modalidade “AL” foi desenvolvida de acordo com os dados solicitados na Instrução Normativa n° 19/09\.

Para os códigos citados, os valores serão gerados <a id="_Hlk535225528"></a>apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração 🡪 Manutenção 🡪 Regitsro 1400”\)\.

Consultar os códigos no link: [http://www\.sped\.fazenda\.gov\.br/spedtabelas/AppConsulta/publico/aspx/](http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/)

ConsultaTabelasExternas\.aspx?CodSistema=SpedFiscal

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__Código selecionado \(\*\)__*”* 

Poderão existir vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ 🡪 este campo será preenchido com ”__ Código selecionado \(\*\)__” 

__03\-MUN__ 🡪 Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __🡪 Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

                  \[Campo “Outros Valores” informado manualmente\]

                                                    \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo 🡪 Será gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\.

Resultado final = zero 🡪 O registro 1400 não será gravado para este município;

__\(\*\) Código selecionado__ – o código será um dos códigos cadastrados na TACES89 para AL\.  

Exemplo: __1272__\. 

__OBS__: O registro 1400 *não* é gerado na geração da EFD do menu “Geração\-PIM”, conforme consta na regra RN1400\.

Para o código abaixo, o registro será gerado de forma automática e via tela de manutenção:

__1201__ – Comunicação  

Ver regra __RN1400\-AL\-01__

__RN1400\-AL\-01__

__Código 1201 – Comunicação \(valor total do fornecimento menos o custo\)__

__MFS94497:__ A partir dessa demanda, a geração do código “1201”, deve ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

__MFS436036__ Inclusão das notas de modelo 62 \(NFCom\) nas Saídas \(SAFX42/43\)\. As notas de saída de modelo 62 consideradas para geração do 1400, são as apresentadas nos registros D700/D750\.Sendo assim, pelo menos um desses registros deve estar selecionado no perfil de geração para que essas notas venham a compor o 1400\.

__Origem dos dados:__ Notas Fiscais \(SAFX42 e SAFX43\) 

                                  Valores informados manualmente 

                                  Parametrização de CFOP e CFOP/NAT

Este código será gerado a partir dos documentos de saídas de comunicação/telecomunicação \(identificados pelo modelo\)*\.*  

__Critérios de recuperação das notas na SAFX42/SAFX43:__ 

\- Código da empresa = código da empresa da geração; 

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de saída \(SAFX42 se aplica apenas para saídas\); 

\- Data Fiscal no período da geração ou data extemporânea no período de geração; 

\- Modelo do documento \(campo 13\-COD\_MODELO da SAFX42\) igual a 21 ou 22 ou ‘62’; 

\- Somente notas não canceladas \(campo 21\-SITUACAO da SAFX42 <> S\); 

\- Notas com itens \(documentos utilities sempre terão itens\); 

\- Classificação fiscal \(campo 50\-COD\_CLASS\_DOC\_FIS da SAFX42\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\); 

\- Não considerar itens informativos \(campo 10\-IND\_TP\_REGISTRO da SAFX43 <> 1\); 

\- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros > Registro 1400 > Específico por UF” para a operação “1201”; 

\- Município do terminal faturado \(campo 76\-COD\_MUNIC\_CONSUMO da SAFX42\) deve estar preenchido e deve ser um município de AL \(campo 75\-UF\_CONSUMO da SAFX42\);

 

__Processamento das notas: __

As notas/itens recuperados conforme os critérios acima serão totalizados *por município do terminal faturado\.*  

__Totalização dos valores:__ 

Será totalizado o Valor do Serviço \(campo 19\-VLR\_SERVICO da SAFX43\)\.

__OBS:__  

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

 

2\- Como as regras são as mesmas dos registros específicos \(C500/C600/C700 para EE e Água, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR dos registros analíticos \(C590, C690 etc \.\.\.\)\. 

__Apuração dos valores a serem deduzidos:__ 

O valor das deduções será apurado com base nas notas fiscais parametrizadas como dedução \(menu “Parâmetros à Registro 1400 à Específico por UF à Deduções”\)\.  

 

Critérios de recuperação das notas para dedução \(SAFX07/SAFX08\): 

 

\- Código da empresa = código da empresa da geração; 

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\); 

\- Data Fiscal no período da geração ou data extemporânea no período de geração; 

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\); 

\- Notas com ou sem itens; 

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar *apenas* os itens de mercadoria\); 

\- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros > Registro 1400 > Específico por UF > Deduções” para a operação “1201”; 

Município do ponto de consumo/ terminal faturado \(campo 208\-COD\_MUNIC\_CONSUMO da SAFX07\) deve estar preenchido e deve ser um município de AL \(campo 207\-UF\_CONSUMO da SAFX07\); 

As notas que são mapa resumo de Utilities devem ser desconsideradas, pois estas notas serão contabilizadas a partir das tabelas SAFX42/SAFX43\. Se não for feito este procedimento, há risco de duplicação de valores;

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item; 

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa; 

 

__Processamento das notas: __

 

As notas/itens recuperados conforme os critérios acima serão totalizados *por município do ponto de consumo/ terminal faturado\.*  

__Totalização dos valores:__ 

 

Notas com itens \- valor contábil do item \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\); 

Notas sem itens \- valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\); 

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.  

 

Obs: A parametrização das deduções não é obrigatória\. Sendo assim, quando __*não*__ existirem dados parametrizados, __ou__, quando __*não*__ existirem notas que atendam à parametrização, não haverá valor de dedução\. 

__Gravação do registro 1400:__ 

 

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma: 

 

__02\-COD\_ITEM\_IPM \-__ este campo será preenchido com o seguinte conteúdo: “1201”  

 

__03–MUN \-__ Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\. 

__04–VALOR \- __Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração > Manutenção > Registro 1400”\)\. 

 

Estes valores informados manualmente serão recuperados da seguinte forma: 

 

   \- Estabelecimento – estabelecimento da geração 

   \- Período – mesmo período da tela da geração \(data inicial e final\) 

   \- Município – município da totalização  

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =  

      “__1201__”  

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado: 

  

                                  \[Valor resultante da totalização\]  

                                                      \(\-\)  

                                 \[Valor resultante das deduções\] 

                                                      \(\+\) 

                  \[Campo “Outros Valores” informado manualmente\] 

                                                      \(\-\)  

                \[Campo “Outras Deduções” informado manualmente\] 

 

__Crítica:__ 

 

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte: 

 

Resultado final for negativo \- Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR está com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\. 

Resultado final for zero \- O registro 1400 não será gravado para este município; 

 

__Gravação dos valores para tela da manutenção:__ 

 

O valor resultante da totalização das notas fiscais, o valor das deduções, e o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\.  

 

O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\. 

 

 

 

__RN1400\-AL\-02__

__Código 1202 – TRANSPORTE \(Qualquer\_modal\_valor\_/\_total\_da\_prestacao\_menos\_o\_custo\)__

MFS607284: A partir dessa demanda, a geração do código “1202”, deve ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

Origem dos dados: Notas Fiscais \(SAFX07 e SAFX08\) 

                                  Valores informados manualmente 

                                  Parametrização de CFOP e CFOP/NAT

                            \(Parâmetros à Registro 1400 à Específico p/UF à CFOP ou CFOP/Nat\)

Este código será gerado a partir dos documentos de entradas dos Documentos de Prestação de Serviços de Transporte Rodoviário \(identificados pelo modelo\), totalizando o valor   contábil   das   entradas   e   aquisições   de   serviço   de   transporte intermunicipal e/ou interestadual, por município do estado do Piauí, excluindo\-se as operações dedutíveis

Apuração do valor referente a cada Aquisição ou Tomada de Serviço na SAFX07/SAFX08:

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de entrada gravadas no D100 que atendam aos seguintes critérios:

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de entrada \(campo 03\-MOVTO\_E\_S da SAFX07 <> 9\); \[MFS607284\]
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Modelo do documento \(campo 13\-COD\_MODELO da SAFX07\) igual a 07, 08, 8B, 09, 10, 11, 26, 27, 57 ou 67, 63;
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Notas com ou sem itens;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar apenas os itens de mercadoria\);
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “1202”;
- Serão consideradas apenas as notas em que o município de origem \(município onde ocorreu o início da prestação do serviço\) seja de PI \(campos 117\-UF\_ORIG\_DEST e 182\-COD\_MUNICIPIO\_ORIG da SAFX07\);

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

OBS: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

2\- Como as regras são as mesmas do D100, além destes critérios de filtro, deve\-se considerar também as notas com situações especiais, pois os valores a serem totalizados são os mesmos valores gravados no campo VL\_OPR do registro analítico \(D190\)\.

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados por município de origem\.

Valor a ser totalizado:

- Notas de classificação 1 ou 3 à valor contábil do item \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\) ou valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\), no caso das notas sem itens;

Apuração dos valores a serem deduzidos:

O valor das deduções será apurado com base nas notas fiscais parametrizadas como dedução \(menu “Parâmetros à Registro 1400 à Especifico por UF à Deduções”\)\. 

Critérios de recuperação das notas para dedução \(SAFX07/SAFX08\):

- Código da empresa igual da empresa informada na tela de geração;
- Código do estabelecimento igual do estabelecimento informado na tela de geração;
- Somente notas de saída \(campo 03\-MOVTO\_E\_S da SAFX07 = 9\);  
- Data Fiscal no período da geração ou data extemporânea no período de geração;
- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 ou 3 \(no caso de nota mista \(classif\. = 3\), considerar apenas os itens de mercadoria\);
- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);
- Somente notas que não sejam transferências \(campo 74\-IND\_TRANSF\_CRED da SAFX07 = 0\);
- Somente notas com situação especial \(campo 125\-IND\_SITUACAO\_ESP da SAFX07\) diferente de 1, 2 e 8;
- Somente as notas em que a UF de origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) seja igual a “PI”;
- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF à Deduções” para a operação “1202”;

Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

Processamento das notas:

As notas/itens recuperados conforme os critérios acima serão totalizados por município de origem\.

Valor a ser totalizado:

- Para as notas com itens, será totalizado o valor contábil dos itens \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);
- Para as notas sem itens, será totalizado o valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

Obs: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Obs: A parametrização das deduções não é obrigatória\. Sendo assim, quando não existirem dados parametrizados, ou, quando não existirem notas que atendam à parametrização, não haverá valor de dedução\.

Gravação do registro 1400:

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

02\-COD\_ITEM\_IPM à este campo será preenchido com o seguinte conteúdo: “1202” 

03\-MUN à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

04\-VALOR à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “1202” 

Assim, o valor a ser gravado no campo 04\-VALOR será o seguinte resultado:

 

                                  \[Valor resultante da totalização\] 

                                                      \(\-\) 

                                 \[Valor resultante das deduções\]

                                                      \(\+\)

                  \[Campo “Outros Valores” informado manualmente\]

                                                      \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

Crítica:

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: “O campo VALOR esta com conteúdo inválido \(valor negativo\) ”\. O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município;

Gravação dos valores para tela da manutenção:

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

O valor totalizado das notas será gravado no campo “Valor Apurado”, o valor das deduções no campo “Deduções”, e o valor final será gravado no campo “Valor Total”\.

 

 

 

 


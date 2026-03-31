# MTZ_Sped_Fiscal_Regras_Registro_1400_UF_PE

- **Fonte:** MTZ_Sped_Fiscal_Regras_Registro_1400_UF_PE.docx
- **Modificado:** 2025-02-06
- **Tamanho:** 97 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Registro 1400 – Específico por UF \- PE

__Localização__: 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS59468

Aline Melo

Alteração na geração do registro 1400, estado do Pernanbuco, geração automática para o código PEIPMS0\.

10/02/2021

MFS64779

\.Aline Melo

Inclusão do código PEIPMS4, para a geração automática do registro 1400 do Estado de Pernambuco

20/05/2021

MFS67705

Aline Melo

Alteração na geração do registro 1400, estado do Pernanbuco, geração automática para o código PEIPME3\.

28/06/2021

MFS59472

Aline Melo

Inclusão do código PEIPMS3 no processo de geração automática do registro 1400, para o estado de Pernambuco\.

20/08/2021

MFS651594

Liliane Assaf

Geração automática do código PEIPMS1

03/09/2024

MFS710625

Graciela Soares 

Inclusão do modelo 66 na regra do código PEIPMS4 –Distribuição de mercadoria de fornecimento continuado

03/02/2025

# <a id="_Toc75782997"></a>Registro 1400 para o tipo de geração \- Específico por UF<a id="_Toc75782998"></a> \- PE

__RN1400\-PE__

A geração do 1400 para a modalidade “PE” foi desenvolvida de acordo com os dados solicitados na Portaria SF nº147/2019\. 

A princípio os valores de todos os códigos serão gerados apenas a partir dos dados inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Os valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

      “__Código selecionado \(\*\)__*”* 

Poderão existir vários registros para este código, de diferentes municípios\.

*Para cada registro recuperado*, será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com ”__ Código selecionado \(\*\)__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o resultado descrito abaixo, a partir dos valores inseridos na manutenção:

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

*\(observar que a manutenção exibe uma mensagem de alerta, mas permite a gravação se resultados negativos\)*

 

Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição:*“O campo VALOR esta com conteúdo inválido \(valor negativo\)”*\. O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__\(\*\) Código selecionado__ – o código será um dos códigos cadastrados na TACES89 para PE\.  Exemplo: PEIPMS0\. 

__OBS__: O registro 1400 *não* é gerado na geração da EFD do menu “Geração\-PIM”, conforme consta na regra RN1400\.

Para os códigos abaixo, o registro será gerado de forma automática e via tela de manutenção:

__PEIPMS0__ \- Prestação de Serviço de Transporte Intermunicipal ou Interestadual;

Ver regra __RN1400\-PE\-01__; 

__PEIPMS4 \-__ Distribuição de mercadoria de fornecimento continuado; 

Ver regra __RN1400\-PE\-02__;

__PEIPME3__ \- Substituição pelas saídas, nas operações com não\-inscrito \(ENTRADAS: ST Saída\) 

Ver regra __RN1400\-PE\-03__;

__PEIPMS3:__ Substituição pelas saídas, nas operações com não\-inscrito \(SAÍDAS: ST projetada Saídas\) 

Ver regra __RN1400\-PE\-04\.__

__PEIPMS1__ \- Prestação de serviço oneroso de comunicação;

Ver regra __RN1400\-PE\-05__; \[MFS651594\]

__RN1400\-PE\-01__

__Código PEIPMS0 – Prestação de Serviço de Transporte Intermunicipal ou Interestadual __

__MFS59468:__ A partir dessa demanda, a geração do código “PEIPMS0, deve ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

*\*Seguindo as orientações do Anexo 2 da Portaria SF Nº 126, de 30 de Agosto de 2018 \(página 205\), o atendimento será feito baseado na situação informada no item 1\.1\. Para a situação do item 1\.2, o contribuinte deve informar os dados via tela de manutenção *__*\(RN1400\-PE\)\.*__

__Origem dos dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                  Valores informados manualmente 

                                  Parametrização de CFOP e CFOP/NAT

A apuração deste item é feita a partir das operações da SAFX07/SAFX08 para cada município do PE\. 

Este código será gerado a partir dos documentos de saída de transporte \(identificados pelo modelo\), totalizando os valores por município de origem\.

Para apurar o total das operações deste item, será feita a totalização dos itens das notas fiscais de __saída__ gravadas nos registros no __D100, D300 e D400\.__

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de saída \(campo 03\-MOVTO\_E\_S da SAFX07 = 9\);

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Modelo \(campo13\-MODELO da SAFX07\) = 07, 08, 8B, 09, 10, 11, 13, 14, 15, 16, 18,

26, 27, 57 e 67;

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1, 3 ou 4;

Para a correta geração dos registros baseados nos registros D100, D300 e D400 seguir a combinação abaixo:

__Baseado no registro D100 – Origem SAFX07 e SAFX08__

Classificação Fiscal = '1' E Modelo de Documento = ‘07’, ‘08’ ou ‘57’ OU

Classificação Fiscal = '4' E Modelo de Documento = '08’, ‘8B’, ‘09’, ‘10’, ‘11’, ‘26’, ‘27’, ‘57’ ou ‘67’\.

__Baseado no registro D300 – Origem SAFX07 __

Classificação Fiscal = '1' ou '3' E Modelo de Documento = ‘13’, ‘14’, ‘15’ ou ‘16’\.

__Baseado no registro D400 – Origem SAFX07 __

Classificação Fiscal = '1' ou '3' E Modelo de Documento = '18'\.

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu “Parâmetros à 

  Registro 1400 à Específico por UF” para o operação “PEIPMS0”;

\- UF de Origem \(campo 117\-UF\_ORIG\_DEST da SAFX07\) deve estar preenchido;

\- Município de Origem \(campo 182\-COD\_MUNICIPIO\_ORIG da SAFX07\) deve estar preenchido; 

\- Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

\- Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__Totalização dos valores:__

\- Para as notas com itens \(Classificação = ‘1’ ou ‘3’\): será totalizado o valor contábil dos itens \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\);

\- Para as notas sem itens \(Classificação = ‘1’ ou ‘4’\): será totalizado o valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\);

Os CTRC’s com classificação 4 não possuem itens da SAFX08\. 

__OBS__: 

1\- Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

__Gravação do registro 1400:__

As notas/itens recuperados conforme os critérios acima, serão totalizados __por município de origem__: 

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo ”__PEIPMS0__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__PEIPMS0__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

\[Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”:      será gravado zero;

No campo “Valor Total”:   será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\-PE\-02__

__Código __<a id="_Hlk72489757"></a>__PEIPMS4 –Distribuição de mercadoria de fornecimento continuado __

__MFS64779:__ A partir dessa demanda, a geração do código “PEIPMS4”, deve ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

*\*não será tratada a parametrização para Deduções, pois não tem ato legal com esclarecimentos para o código da UF “PE”\. Para fazer deduções do valor apurado para cada município, o usuário deve utilizar o campo de deduções da tela de manutenção do 1400\.*

__\[MFS710625\] __Inclusão do modelo de nota “66”

__Origem dos dados:__ Notas Fiscais de Utilities \(SAFX42 e SAFX43\)

                                  Valores informados manualmente

                                  Parametrização de CFOP e CFOP/NAT

               

A apuração deste item é feita a partir das operações da SAFX42/SAFX43 para cada município do PE\. 

Este código será gerado a partir dos documentos de saída de energia elétrica/agua encanada/gás natural, totalizando os valores por município de destino do fornecimento\.

Para apurar o total das operações deste item será feita a totalização dos itens das notas fiscais de __saída__ gravadas no C500, C600 ou C700 para o segmento de energia elétrica, água e gás natural\.

__Critérios de recuperação das notas na SAFX42/SAFX43:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

__Para notas de Energia elétrica__

\- Modelo \(campo “13\-Modelo do Documento” da SAFX42\) = “06 ou 66”

__Para notas de Água encanada__

\- Modelo \(campo “13\-Modelo do Documento” da SAFX42\) = “29”

__Para notas de Gas Natural__

\- Modelo \(campo “13\-Modelo do Documento” da SAFX42\) = “28”

\- Data \(campo “03\-Data Emissão”\) – deve ser uma data no período da geração; 

\- Somente notas de saída \(SAFX42 se aplica apenas para saídas\);

\- Somente as notas não canceladas \(campo “21\-Situação da Nota” <> “S”\);

\- O campo “75\-UF do Ponto de Consumo” da SAFX42 deve ser = “PE”;

\- O campo “76\-Município do Ponto de Consumo” da SAFX42 deve estar preenchido; 

\- Somente itens de mercadoria \(campo “47\-Classificação” da SAFX43 = 1\-Mercadoria\) 

\- Somente itens não informativos \(campo “10\-Tipo de Item” da SAFX43 <> 1\)

\- CFOP ou CFOP e Natureza de Operação do item deve estar parametrizado no Menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__PEIPMS4__”;

\(os documentos da X42/X43 sempre têm itens\)

__OBS__: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

__Processamento das notas da SAFX42/SAFX43__:

Valor a ser totalizado à valor do serviço do item \(campo “19\-Valor do Serviço” da SAFX43\)

A totalização dos valores será feita por *por município* da nota \(campo 76 da SAFX42\)\.

__Resultado a ser gravado no registro 1400 para cada município:__

Para cada município apurado será gerado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido c/o conteúdo ”__PEIPMS4__” 

__03\-MUN__ à Este campo informa o município do ponto de consumo, e será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor apurado para o município \(conforme descrito acima\), mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__PEIPMS4__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

\[Valor resultante da totalização – valor da dedução apurada\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

__Crítica:__

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

\- Resultado final negativo à Será  gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Código do item\) para identificação do usuário\.

\- Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais \(SAFX42/SAFX43\), o valor da dedução apurada, e também o valor final gravado no registro 1400, serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente \(menu “Geração à Manutenção à Registro 1400”\): 

\- No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

\- No campo “Deduções”:      será gravado zero;

\- No campo “Valor Total”:   será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\-PE\-03__

__Código PEIPME3 \- Substituição pelas saídas, nas operações com não\-inscrito \(ENTRADAS: ST Saída\)__

__MFS67705:__ A partir dessa demanda, a geração do código “PEIPME3”, deve ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

\* *Na  operação  de substituição  pelas  saídas para  contribuinte  não\-inscrito  será informado  como entrada \(PEIPME3\) o  valor da  operação  de  saída do declarante,  indicando\-se o código  do  município  para  onde  está  se  destinando  a  mercadoria  ou  serviço\.*

__Origem dos dados:__ Notas Fiscais \(SAFX07 e SAFX08\)	

                                  Valores informados manualmente

                                  Parametrização de CFOP e CFOP/NAT

A apuração deste item é feita a partir das operações da SAFX07/SAFX08 para cada município do PE\.

Este código será gerado a partir dos documentos de saída de mercadoria/serviço, totalizando os valores por município de destino da mercadoria\.

Para apurar o total das operações deste item, será feita a totalização dos itens das notas fiscais de __saída__ gravadas no __C100__ que atendam aos seguintes critérios:

		

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de saída \(campo 03\-MOVTO\_E\_S da SAFX07 = 9\);

\- Modelo \(campo 13\-MODELO da SAFX07\) = 01, 1B, 04 ou 55

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 e 3\.

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Inscrição Estadual da Pessoa Fis/Jur informada na nota \(campo INSC\_ESTADUAL da SAFX04\) preenchido como “ISENTO”;

\- UF de Destino \(campo 122\-UF\_DESTINO da SAFX07\) deve estar preenchido;

\- Município de Destino \(campo 183\-COD\_MUNICIPIO\_DEST da SAFX07\) deve estar preenchido; 

\- CFOP ou CFOP e Natureza de Operação da capa ou item deve estar parametrizado no menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__PEIPME3__”;

\- Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

\- Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__Totalização dos valores:__

\- Para as notas com itens \(Classificação = ‘1’ ou ‘3’\): será totalizado o valor contábil dos itens \(campo 64\-VLR\_CONTAB\_ITEM SAFX08\) __\(\-\)__ valor ICMS ST \(52\-VLR\_SUBST\_ICMS\)

\- Para as notas sem itens \(Classificação = ‘1’\): será totalizado o valor total da nota \(campo 23\-VLR\_TOT\_NOTA da SAFX07\) __\(\-\)__ valor ICMS\-ST \(48\-VLR\_SUBST\_ICM\)

__OBS__: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

__Gravação do registro 1400:__

As notas/itens recuperados conforme os critérios acima, serão totalizados __por município de destino: __ 

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo ”__PEIPME3__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__PEIPME3__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

\[Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\.

Resultado final = zero à O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”:      será gravado zero;

No campo “Valor Total”:   será gravado o valor final \(valor gravado no registro 1400\);

__RN1400\-PE\-04__

__Código PEIPMS3 \- Substituição  pelas  saídas,  nas  operações  com  não\-inscrito \(SAÍDAS: ST projetada Saídas\)__

__MFS59472:__ A partir dessa demanda, a geração do código “PEIPMS3”, deve ser feita de forma automática, considerando também os valores “outros” inseridos na tela de manutenção, quando for o caso, conforme todos os códigos do 1400\.

*\* O código trata\-se da substituição  pelas  saídas,  nas  operações  com  não\-inscrito    \(SAÍDAS: ST projetada Saídas\), onde o valor contábil projetado para a operação de saída subsequente deve ser informado com o valor da base para cálculo do ICMS\-ST, de acordo com percentual de agregação definido na legislação tributária aplicável\. Deve\-se ainda indicar o código do Município para onde está se destinando a mercadoria ou serviço\.*

__Origem dos dados:__ Notas Fiscais \(SAFX07 e SAFX08\)

                                  Valores informados manualmente

                                  Parametrização de CFOP e CFOP/NAT

A apuração deste item é feita a partir das operações da SAFX07/SAFX08 para cada município do PE\.

Este código será gerado a partir dos documentos de saída de mercadoria/serviço, totalizando os valores por município de destino da mercadoria\.

Para apurar o total das operações deste item, será feita a totalização dos itens das notas fiscais de __saída__ gravadas no __C100__ que atendam aos seguintes critérios:

		

__Critérios de recuperação das notas na SAFX07/SAFX08:__

\- Código da empresa = código da empresa da geração;

\- Código do estabelecimento = código do estabelecimento da geração;

\- Somente notas de saída \(campo 03\-MOVTO\_E\_S da SAFX07 = 9\);

\- Modelo \(campo 13\-MODELO da SAFX07\) = 01, 1B, 04 ou 55

\- Data Fiscal no período da geração ou data extemporânea no período de geração;

\- Classificação fiscal \(campo 12\-COD\_CLASS\_DOC\_FIS da SAFX07\) igual a 1 e 3\.

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Inscrição Estadual da Pessoa Fis/Jur informada na nota \(campo INSC\_ESTADUAL da SAFX04\) preenchido como “ISENTO”;

\- UF de Destino \(campo 122\-UF\_DESTINO da SAFX07\) deve estar preenchido;

\- Município de Destino \(campo 183\-COD\_MUNICIPIO\_DEST da SAFX07\) deve estar preenchido; 

\- CFOP ou CFOP e Natureza de Operação da capa ou item deve estar parametrizado no menu “Parâmetros à  Registro 1400 à Específico por UF” para a operação “__PEIPMS3__”;

\- Para as notas com itens, será utilizado o CFOP ou CFOP/Natureza do item;

\- Para as notas sem itens, será utilizado o CFOP ou CFOP/Natureza da capa;

__Totalização dos valores:__

\- Para as notas com itens \(Classificação = ‘1’ ou ‘3’\): será totalizado o valor da Base de Cálculo do ICMS\-ST \(campo 64\-BASE\_SUB\_TRIB\_ICMS da SAFX08\)\.

\- Para as notas sem itens \(Classificação = ‘1’\): será totalizado o valor da Base de Cálculo do ICMS\-ST \(campo 64\-BASE\_SUB\_TRIB\_ICMS da SAFX07\)\.

__OBS__: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\.

__Gravação do registro 1400:__

As notas/itens recuperados conforme os critérios acima, serão totalizados __por município de destino: __ 

__Para cada município__ apurado será gravado um registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ à este campo será preenchido com o conteúdo ”__PEIPMS3__” 

__03\-MUN__ à Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código  do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR __à Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Regitsro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios =

     ”__PEIPMS3__”

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

\[Valor resultante da totalização\]

\(\+\)

\[Campo “Outros Valores” informado manualmente\]

\(\-\)

\[Campo “Outras Deduções” informado manualmente\]

Se o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo à Será gravada uma mensagem de erro no log com a seguinte descrição: *“O campo VALOR esta com conteúdo inválido \(valor negativo\)”\. *O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero à O registro 1400 não será gravado para este município\.

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções, e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”:      será gravado zero;

No campo “Valor Total”:   será gravado o valor final \(valor gravado no registro 1400\)\.

__RN1400\-PE\-05__

__Código PEIPMS1 \- Prestação de serviço oneroso de comunicação__

\[MFS651594\]: Inclusão da geração automática do 1400 para o código PEIPMS1\.

Base Legal: ANEXO 2 DA PORTARIA SF Nº 126, DE 30 DE AGOSTO DE 2018

*\*não será tratada a parametrização para Deduções, pois a Portaria não fornece esclarecimentos\. Para fazer deduções do valor apurado para cada município, o usuário deve utilizar o campo de deduções da tela de manutenção do 1400\.*

__Origem dos dados:__ Notas Fiscais \(SAFX42 e SAFX43\)

                                  Valores informados manualmente 

Este código será gerado a partir dos documentos de saídas de comunicação/telecomunicação \(identificados pelo modelo\), totalizando os valores por município do Terminal Faturado\.

Apuração do valor referente a cada município na SAFX42/SAFX43:

Será totalizado o valor do serviço das notas da SAFX42/SAFX43 que atendam aos seguintes critérios: 

\(na prática, trata\-se das notas fiscais __de saída__ gravadas nos registros específicos de Telecom \(D500/D600/D700\)\)

\- Código da empresa – código da empresa da geração

\- Código do Estabelecimento – código do estabelecimento da geração 

\- Modelo \(campo “13\-Modelo do Documento” da SAFX42\) = “21” ou “22” ou “62”

\- Data \(campo “03\-Data Emissão / Escrita Fiscal”\) – deve ser uma data no período da

  geração 

\- Somente as notas não canceladas \(campo “21\-Situação da Nota” <> “S”\)

\- O campo “75\-UF do Ponto de Consumo” da SAFX42 deve ser = “PI”;

\- O campo “76\-Município do Ponto de Consumo” da SAFX42 deve estar preenchido; 

\- Somente itens de mercadoria \(campo “47\-Classificação” da SAFX43 = 1\-Mercadoria\) 

\- Somente itens não informativos \(campo “10\-Tipo de Item” da SAFX43 <> 1\)

\(os documentos da X42/X43 sempre têm itens\)

__OBS__: Seguindo o padrão do Sped Fiscal, quando se tratar de geração por I\.E\.U\., serão recuperadas as notas do estabelecimento selecionado \(centralizador\), e também de todos os estabelecimentos centralizados por ele, considerando a parametrização da I\.E\.U\. do módulo de controle das obrigações estaduais\. 

Processamento das notas da SAFX42/SAFX43:

Valor a ser totalizado à valor do serviço do item 

                                       \(campo “19\-Valor do Serviço” da SAFX43\)

A totalização dos valores será feita por município da nota \(campo 76 da SAFX42\)\.

__Gravação do registro 1400:__

O resultado apurado para cada município será gerado num registro 1400, da seguinte forma:

__02\-COD\_ITEM\_IPM__ 🡪 este campo será preenchido com o seguinte conteúdo: “__PEIPMS1__” 

__03\-MUN__ 🡪 Este campo será preenchido com a concatenação do código da UF \(campo COD\_UF da tabela MUNICIPIO\) \+ código do município\. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve\-se completar com zeros à esquerda quando necessário\.

__04\-VALOR__ 🡪 Este campo será preenchido com o valor resultante da totalização mais os valores inseridos na manutenção do registro 1400 \(menu “Geração à Manutenção à Registro 1400”\)\.

Estes valores informados manualmente serão recuperados da seguinte forma:

   \- Estabelecimento – estabelecimento da geração

   \- Período – mesmo período da tela da geração \(data inicial e final\)

   \- Município – município da totalização 

   \- Código do Item da Tabela de Itens p/o Índice de Participação dos Municípios = 

__      __“__PEIPMS1” __

Assim, o valor a ser gravado no campo __04\-VALOR__ será o seguinte resultado:

 

                                  \[Valor resultante da totalização\] 

                                                      \(\+\)

                  \[Campo “Outros Valores” informado manualmente\]

                                                      \(\-\) 

                \[Campo “Outras Deduções” informado manualmente\]

Crítica:

Caso o resultado a ser gravado for negativo ou zero, o procedimento será o seguinte:

Resultado final negativo 🡪 Será gravada uma mensagem de erro no log com a seguinte descrição: “*O campo VALOR esta com conteúdo inválido \(valor negativo\)*”\. O log mostrará a identificação do registro \(Estab\+Município\+Operação\) para identificação do usuário\. O registro 1400 não será gravado para este município\.

Resultado final = zero 🡪 O registro 1400 não será gravado para este município;

__Gravação dos valores para tela da manutenção:__

O valor resultante da totalização das notas fiscais, o valor das deduções e também o valor final gravado no registro 1400 serão armazenados na tabela utilizada na manutenção, e poderão ser consultados posteriormente\. 

No campo “Valor Apurado”: será gravado o valor resultante da totalização das notas;

No campo “Deduções”:      será gravado zero;

No campo “Valor Total”: será gravado o valor final \(valor gravado no registro 1400\);


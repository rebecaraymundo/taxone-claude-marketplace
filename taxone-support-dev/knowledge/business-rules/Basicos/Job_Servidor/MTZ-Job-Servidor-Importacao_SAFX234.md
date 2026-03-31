# MTZ-Job-Servidor-Importacao_SAFX234

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX234.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 74 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX234

Tabela das NFs dos Bens p/ Cálculo dos Créditos Extemporâneos \(Integral\) do CIAP

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS3615

Créditos Extemporâneos de Bens com Prazo de Apropriação “normal” já Ultrapassado

Criação de nova tabela SAFX para carga das notas fiscais dos Bens que terão todos os seus créditos calculados de forma extemporânea\. 

MFS4805

Novos campos

Criação de novos campos para tratamento dos Bens com baixa antes do término do período de apropriação\. Ver RN00 e RN16\.  

MFS31404

Novos campos

Inclusão de novos campos para atender a nova versão do Sped Fiscal \(vrs\. 1\.13, Jan/2020\), onde foram criados campos novos no G130 e G140\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

Esta tabela é “filha” da tabela SAFX233\. 

A SAFX233 contém as informações do Bem, e na SAFX234 ficam as notas fiscais relacionadas à aquisição do Bem, e a saída do Bem, nos casos de baixa antes do término do período de apropriação \(alteração da MFS4805\)\.

 

Para cada Bem da SAFX233 poderão existir várias notas/itens na SAFX234\.

Estrutura da tabela SAFX224 🡪 vide manual de layout

Campos que compõe a chave da tabela:

A chave é composta pelos campos chave da tabela “mãe” \(SAFX233\) \+ campos de identificação do item da nota fiscal\.

__         Código da Empresa \+ Código do Estabelecimento \+ Data da Apuração \+ Código do Bem \+ Código do Incorporador \+__

__   Indicador Pessoa Fis/Jur \+ Código Pessoa Fis/Jur \+ Data de Emissão  \+Número Documento \+ Série Documento \+ Número do Item __

A manutenção desta tabela é feita no Módulo CIAP, menu “Créditos Extemporâneos \(Integral\) 🡪 Manutenção dos Bens”, na aba “Informações das Notas Fiscais”\.

Sobre as mensagens de erro:

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação do Bem e da nota fiscal \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

__RN01__

__RN02__

__RN03__

__RN04__

__RN05__

__RN01\-Código da Empresa__

__RN02\-Código do Estabelecimento__

__RN03\-Data da Apuração__

__RN04\-Código do Bem __

__RN05\-Código do Incorporador __

Os campos 01 ao 05 são os campos que identificam a chave da tabela “mãe” SAFX233\.

Por isso, as críticas referentes a estes campos são exatamente as mesmas descritas para a SAFX233 \(ver documento de regras “*MTZ\-Job\-Servidor\-Importacao\_SAFX233*”\)\.

Quando algum destes campos for *invalidado* pela crítica, o registro não será importado e será gravada no log a mensagem de erro correspondente, conforme definido nas regras\.

Quando todos esses campos forem *validados*, será verificada a existência dos dados informados na tabela “mãe” SAFX233\.

Caso *não* exista o registro da SAFX233, o registro “filho” \(SAFX234\) não será importado e no log de erros será gravada a seguinte mensagem:

*                             “Bem não cadastrado na Tabela dos Bens p/ Cálculo dos Créditos Extemporâneos \(SAFX233\)” *

__RN06__

__Campo Indicador da Pessoa Fisica/Jurídica __

Campo de preenchimento __*obrigatório*__\.

Seu conteúdo deve ser um dos indicadores da Tabela de Pessoas Fis/Jur SAFX04 \(campo 01\)\.

Caso não preenchido ou inválido, o registro não será importado e no log de erros será gravada a seguinte mensagem:

\(pode ser aproveitada a mensagem 90088 da TFIX22\)\.

*                            “O indicador de Pessoa Fisica/Juridica não esta preenchido ou esta com informação invalida”*

__RN07__

__Campo Código da Pessoa Fisica/Jurídica __

Campo de preenchimento __*obrigatório*__\.

A pessoa informada deve estar cadastrada na Tabela de Pessoas Fis/Jur \(SAFX04\), com uma validade <= a data de emissão da nota \(data informada no campo 10\)\.

Caso o campo não esteja preenchido, o registro não será importado e no log de erros será gravada a seguinte mensagem:

\(pode ser aproveitada a mensagem 60831 da TFIX22\)\.

*                                         “O Código da Pessoa Fisica/Jurídica deve ser preenchido”*

Caso a pessoa não exista na SAFX04, considerando a regra da data de validade, o registro não será importado e no log de erros será gravada a seguinte mensagem:    \(pode ser aproveitada a mensagem 90124 da TFIX22\)\.

                                            *“O Código da Pessoa Fisica/Jurídica não está cadastrado”*

 

Obs: para obter o grupo da pessoa fis/jur será utilizada a data do campo “10\-Data de Emissão”\.

__RN08__

__Campo Número do Documento __

Campo de preenchimento __*obrigatório*__\.

Caso o campo não esteja preenchido, o registro não será importado e no log de erros será gravada a seguinte mensagem:

\(pode ser aproveitada a mensagem 60832 da TFIX22\)\.

*                                                      “O Número do Documento deve ser preenchido”*

*\(o documento informado não será validado na tabela de documentos fiscais \(SAFX07/SAFX08\), pois os documentos informados na tabela em questão \(SAFX234\) serão documentos de períodos antigos, ou muito antigos\) *

__RN09__

__Campo Série do Documento__

Campo de preenchimento __*não*__ __*obrigatório*__\.

Caso o campo não esteja preenchido, o campo da tabela de destino será gravado com um caracter branco\. 

__RN10__

__Campo Data de Emissão__

Campo de preenchimento __*obrigatório*__\.

Quando o campo não for informado, ou quando for uma data inválida, o registro não será importado e no log de erros será gravada a seguinte mensagem: 

                                                    *“Data de Emissão não preenchida ou inválida”*

__RN11__

__Campo Número do Item__

Campo de preenchimento __*obrigatório*__\.

Caso o campo não esteja preenchido, o registro não será importado e no log de erros será gravada a seguinte mensagem:

\(pode ser aproveitada a mensagem 90132 da TFIX22\)\.

*                                      “O Número do Item do Documento Fiscal não esta preenchido”*

__RN12__

__Campo Modelo do Documento__

Campo de preenchimento __*obrigatório*__\.

O modelo informado deve estar cadastrado na Tabela de Modelos de Documento Fiscal \(SAFX2024\), com uma validade <= a data de emissão da nota \(data informada no campo 10\)\.

Caso o campo não esteja preenchido, o registro não será importado e no log de erros será gravada a seguinte mensagem:

*                                                      “O Modelo do Documento deve ser preenchido”*

 

Caso o código informado não exista na SAFX2024, considerando a regra da data de validade, o registro não será importado e no log de erros será gravada a seguinte mensagem:

 

                                       *“O Modelo do Documento não está cadastrado na Tabela dos Modelos \(SAFX2024\)”*

 

Obs: para obter o grupo da SAFX2024 será utilizada a data do campo “10\-Data de Emissão”\.

__RN13__

__Campo Chave da NFe__

Campo de preenchimento __*não*__ __*obrigatório*__\.

__RN14__

__Campo Indicador do Produto__

Campo de preenchimento __*obrigatório*__\.

Seu conteúdo deve ser um dos indicadores da Tabela de Produtos SAFX2013 \(campo 01\)\.

Caso não preenchido, ou inválido, o registro não será importado e no log de erros será gravada a seguinte mensagem:

*                                                 “Indicador do Produto não preenchido ou inválido”*

__RN15__

__Campo Código do Produto__

Campo de preenchimento __*obrigatório*__\.

O código informado deve estar cadastrado na Tabela de Produtos \(SAFX2013\), com uma validade <= a data de emissão da nota \(data informada no campo 10\)\.

Caso o campo não esteja preenchido, o registro não será importado e no log de erros será gravada a seguinte mensagem:

\(pode ser aproveitada a mensagem 60855 da TFIX22\)\.

*                                                    “O Código do Produto deve ser preenchido”*

Caso o produto não exista na SAFX2013, considerando a regra da data de validade, o registro não será importado e no log de erros será gravada a seguinte mensagem:    \(pode ser aproveitada a mensagem 60861 da TFIX22\)\.

                                                       *“Código do Produto não cadastrado”*

 

Obs: para obter o grupo do produto será utilizada a data do campo “10\-Data de Emissão”\.

__RN16__

__Indicador de Entrada/Saída__                <a id="OLE_LINK20"></a><a id="OLE_LINK21"></a><a id="OLE_LINK22"></a>\(campo criado pela __MFS4805__\)

Campo de preenchimento __*obrigatório*__\.

Valores válidos: “E” ou “S”\.

Quando informado um valor diferente destas opções, o registro não será importado e no log de erros será gravada a seguinte mensagem:

                                                        *O Indicador de Entrada/Saída deve ser = “E” ou “S” *

Critica a ser realizada quando o Indicador = “__S__”:

O indicador “__S__” \(Saída\) só pode ser utilizado quando o Bem em questão tiver a informação de baixa na tabela “mãe” \(SAFX233\)\. Por isso, será realizada a seguinte crítica:

Quando o Indicador for = “__S__”, será verificado se o campo “Data da Baixa” da tabela “mãe” \(ver __RN01__\) esta preenchido\. Caso *não preenchido*, o registro não será importado e será gravada a seguinte mensagem de erro no log:

“*Indicador Entrada/Saída inválido\. Só é permitido informar uma nota de saída, quando for informada a Data da Baixa do Bem”*

__RN17__

__Campo Número do Documento de Arrecadação__

Campo de preenchimento __*não*__ obrigatório\.

__MFS31404__

__RN18__

__Campo Quantidade__

Campo de preenchimento __*não*__ obrigatório\.

*\(Campo criado na MFS31404 para a nova versão 1\.13 do Sped Fiscal\. Este campo será criado a princípio, sem nenhuma crítica, pois no GP consta como campo obrigatório, mas não está claro se deve ser informado tanto para as notas de entrada como de saída\. Posteriormente, quando forem realizados testes no novo PVA, para desenvolver a geração, será verificada essa questão, e se for o caso, poderão ser incluídas críticas na importação/manutenção\)\.*

__MFS31404__

__RN19__

__Campo Unidade de Medida__

Campo de preenchimento __*não*__ obrigatório\.

Quando preenchido, o código da unidade informado deve estar cadastrado na Tabela de Unidades de Medida \(SAFX2007\), com uma validade <= a data de emissão da nota \(data informada no campo 10\)\.

Caso a unidade não exista na SAFX2007, considerando a regra da data de validade, o registro não será importado e no log de erros será gravada a seguinte mensagem:  

                                                                  *“Unidade de Medida não cadastrada”*

 

Obs: para obter o grupo da unidade de medida será utilizada a data do campo “10\-Data de Emissão”\.

*\(Campo criado na MFS31404 para a nova versão 1\.13 do Sped Fiscal\. Este campo será criado a princípio, sem nenhuma crítica, pois no GP consta como campo obrigatório, mas não está claro se deve ser informado tanto para as notas de entrada como de saída\. Posteriormente, quando forem realizados testes no novo PVA, para desenvolver a geração, será verificada essa questão, e se for o caso, poderão ser incluídas críticas na importação/manutenção\)\.*

__MFS31404__

__RN20__

__Campo Valor ICMS__

Campo de preenchimento __*não*__ obrigatório\.

*\(Campo criado na MFS31404 para a nova versão 1\.13 do Sped Fiscal\. Este campo será criado a princípio, sem nenhuma crítica, pois no GP consta como campo obrigatório, mas não está claro se deve ser informado tanto para as notas de entrada como de saída\. Posteriormente, quando forem realizados testes no novo PVA, para desenvolver a geração, será verificada essa questão, e se for o caso, poderão ser incluídas críticas na importação/manutenção\)\.*

__MFS31404__

__RN21__

__Campo Valor ICMS\-ST__

Campo de preenchimento __*não*__ obrigatório\.

* \(Campo criado na MFS31404 para a nova versão 1\.13 do Sped Fiscal\. Este campo será criado a princípio, sem nenhuma crítica, pois no GP consta como campo obrigatório, mas não está claro se deve ser informado tanto para as notas de entrada como de saída\. Posteriormente, quando forem realizados testes no novo PVA, para desenvolver a geração, será verificada essa questão, e se for o caso, poderão ser incluídas críticas na importação/manutenção\)\.*

__MFS31404__

__RN22__

__Campo Valor ICMS Frete__

Campo de preenchimento __*não*__ obrigatório\.

*\(Campo criado na MFS31404 para a nova versão 1\.13 do Sped Fiscal\. Este campo será criado a princípio, sem nenhuma crítica, pois no GP consta como campo obrigatório, mas não está claro se deve ser informado tanto para as notas de entrada como de saída\. Posteriormente, quando forem realizados testes no novo PVA, para desenvolver a geração, será verificada essa questão, e se for o caso, poderão ser incluídas críticas na importação/manutenção\)\.*

__MFS31404__

__RN23__

__Campo Valor ICMS Dif\. Aliq\.__

Campo de preenchimento __*não*__ obrigatório\.

*\(Campo criado na MFS31404 para a nova versão 1\.13 do Sped Fiscal\. Este campo será criado a princípio, sem nenhuma crítica, pois no GP consta como campo obrigatório, mas não está claro se deve ser informado tanto para as notas de entrada como de saída\. Posteriormente, quando forem realizados testes no novo PVA, para desenvolver a geração, será verificada essa questão, e se for o caso, poderão ser incluídas críticas na importação/manutenção\)\.*

__MFS31404__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


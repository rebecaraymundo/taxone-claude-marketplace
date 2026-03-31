# MTZ-Job-Servidor-Importacao-SAFX294

- **Fonte:** MTZ-Job-Servidor-Importacao-SAFX294.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 72 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX294

Tabela dos Ajustes / Outros Valores do Documento Fiscal

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS31256

Criação de tabelas para a atualização legal do Sped Fiscal

Criação das tabelas SAFX293/SAFX294 para geração dos registros C595 e C597, da nova versão 1\.13 do Sped Fiscal \(vigência Jan/2020\)\. 

28/10/2019

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX294__ 🡪 vide manual de layout

A SAFX294 é uma tabela “filha” da SAFX293 \(Tabela de Observações do Documento Fiscal \- Utilities\)\.

__Campos que compõe a chave da tabela:__

                           __                        Campos chave da SAFX293 \(campo 01 ao 10\)__

__                                                                                 \+__

__                                                            Código de Ajuste \(campo 11\)__

__                                                                                 \+__

__                                                              Número do Item \(campo 13\) *\(opcional\)*__

A manutenção da tabela é feita na tela de manutenção dos documentos fiscais de Utilities, no módulo DW\.

Sobre o Número do Item:

Observar que o número do item compõe a chave da tabela\. Desta forma, quando *não* for informado um número de item, a coluna na tabela definitiva será preenchida com zero\.  

Quando o número do item for informado, o usuário poderá informar mais de um ajuste para o mesmo documento, observação e Código de Ajuste, desde que informe diferentes números de item\.

__RN01__

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

__RN03__

__Campo Data Emissão / Escrita Fiscal__

Campo de preenchimento __*obrigatório*__\.

Deve ser uma data válida\.

Quando não preenchida, ou data inválida, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(mensagem padrão código 92981: “*Data de Emissão não preenchida ou inválida”*\)\.

__RN04__

__Campo Indicador da Pessoa Física/Jurídica __

Campo de preenchimento __*obrigatório*__\.

Valores válidos: '1', '2', ‘3’, ‘4’, ‘5’\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(mensagem padrão\)\.

__RN05__

__Campo Código da Pessoa Física/Jurídica \(Destinatário/Emitente\) __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão\)\.

A partir do conteúdo dos campos 04 e 05 \(indicador e código da pessoa fis/jur\) será verificada a existência da pessoa informada na Tabela de Pessoas Fis/Jur \(SAFX04\)\. Quando não encontrada, o registro não será importado, e no log de erros será gravada uma mensagem informando que a pessoa não existe na tabela \(mensagem padrão\)\.

__RN06__

__Campo Número do Documento Fiscal__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão\)\.

Através dos campos que identificam o documento fiscal \(campos 01 ao 08\), será verificada a sua existência na __SAFX42__\. Caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                      “O documento fiscal informado não foi identificado na Tabela de Documentos Fiscais – Utilities \(SAFX42\)”*

No log aparecerão os dados de identificação do documento e o código de observação informados\.  

__RN07__

__Campo Série do Documento Fiscal__

Campo de preenchimento __*não*__ obrigatório\.

Quando este campo não for preenchido, será gravado um caracter branco \(“ “\), pois o campo compõe a chave da tabela\.

__RN08__

__Campo Subsérie do Documento Fiscal__

Campo de preenchimento __*não*__ obrigatório\.

Quando este campo não for preenchido, será gravado um caracter branco \(“ “\), pois o campo compõe a chave da tabela\.

__RN09__

__Campo Código da Observação__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido: “*O Código da Observação deve ser informado*”\. No log aparecerão os dados de identificação do documento informado\.

Crítica do código de observação informado na __SAFX2009__:

 

O código informado será validado na Tabela de Cadastro de Observações \(__SAFX2009__\)\.

Para acessar a SAFX2009, considerar o Grupo \(Relacionamento Tabelas x Grupo\) válido para o estabelecimento e data do documento informado\. Quanto à data de validade, considerar a maior data que seja <= a data do documento informado\.

Caso a observação não exista, o registro não será importado, e no log de erros será gravada uma mensagem informando que o código informado não existe na tabela \(mensagem padrão código 900031: “*Código da Observação não está cadastrado*”\)\.   

Crítica do código de observação informado na __SAFX293__:

Após a validação dos campos que identificam a observação \(campo 01 ao 10\), conforme as regras descritas, será verificado se a observação existe na base de dados \(__SAFX293__\)\. 

Caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*          “O código de observação informado não foi identificado na Tabela de Observações do Documento Fiscal – Utilities \(SAFX293\)”*

No log aparecerão os dados de identificação do documento e do código de observação informados\.  

__RN10__

<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

<a id="OLE_LINK32"></a><a id="OLE_LINK33"></a><a id="OLE_LINK34"></a>__Campo Tipo de Observação__

Campo de preenchimento __*obrigatório*__\.

Deve ser = “L”\. 

Quando não preenchido, ou <> “L”, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(mensagem padrão código 91629: “*A informação do campo Tipo de Observação é inválida*”\):

__Obs__\.: Este campo tem duas opções: “I” \(Observação referente às Informações Complementares da nota\) ou “L” \(Observação referente aos Lançamentos Fiscais da nota\)\. Mas a princípio, será tratada *apenas* a opção “__L__”, uma vez que o registro C500 não trabalha com Informações Complementares\.

__RN11__

__Campo Código do Ajuste__

Campo de preenchimento __*obrigatório*__\.

O código informado deve estar preenchido, e deve existir na Tabela dos Códigos de Ajuste Provenientes de NF’s \(módulo DW, tabela DWT\_COD\_AJUSTE\_SPED\)\.

Caso o campo não esteja preenchido, ou não exista na tabela, o registro não será importado, e no log de erros será gravada a seguinte mensagem de erro:

                “*Código de Ajuste não preenchido ou não cadastrado na tabela de Códigos de Ajuste proveniente de NF’s*”\.   

No log aparecerão os dados de identificação do documento, do código da observação e do código de ajuste informados\.  

__RN12__

__Campo Descrição Complementar do Ajuste__

Campo de preenchimento __*não*__ obrigatório\.

__RN13__

__Campo Número do Item do Documento__

Campo de preenchimento __*não*__ obrigatório\.

Observar que o número do item compõe a chave da tabela, conforme descrito na __RN00__\. 

Quando preenchido, deve ser um número de item que exista no documento fiscal informado \(ou seja, na __SAFX43__\)\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                          “Número do Item não identificado para o documento fiscal informado”*

No log aparecerão os dados de identificação do documento, código de observação, código de ajuste e número do item informados\.  

 

__RN14__

__Campo Base de Cálculo do ICMS__

Campo de preenchimento __*não*__ obrigatório\.

Pelo menos um dos valores dos campos “14\-Base de Cálculo do ICMS, “16\-Valor do ICMS” ou “17\-Outros Valores” deve estar preenchido com um valor > zeros\.  Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem: *“Ao menos um dos valores \(Base de Cálculo, Valor do ICMS, ou Outros Valores\) deve ser preenchido e maior que zero\.”*

No log aparecerão os dados de identificação do documento, código de observação, código de ajuste e número do item\.

__RN15__

__Campo Alíquota do ICMS__

Campo de preenchimento __*não*__ obrigatório\.

__RN16__

__Campo Valor do ICMS__

Campo de preenchimento __*não*__ obrigatório\.

Ver crítica sobre o preenchimento dos valores na __RN14__\. 

__RN17__

__Campo Outros Valores__

Campo de preenchimento __*não*__ obrigatório\.

Ver crítica sobre o preenchimento dos valores na __RN14__\. 

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


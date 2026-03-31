# MTZ-Job-Servidor-Importacao-SAFX293

- **Fonte:** MTZ-Job-Servidor-Importacao-SAFX293.docx
- **Modificado:** 2024-06-21
- **Tamanho:** 66 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX293

Tabela de Observações do Documento Fiscal \- Utilities

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação à Execução

\- Importação Batch à Programação à Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS31256

Criação de tabelas para a atualização legal do Sped Fiscal

Criação das tabelas SAFX293/SAFX294 para geração dos registros C595 e C597, da nova versão 1\.13 do Sped Fiscal \(vigência Jan/2020\)\. 

25/10/2019

MFS591922 

Alterações da NFCom 

Criação de Novos Campos – Tabela SAFX293 

08/04/2024 

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX293__ à vide manual de layout

A SAFX293 é uma tabela “filha” da SAFX42 \(Capa Documento Fiscal Utilities\)\.

__Campos que compõe a chave da tabela:__

                           __                        Campos chave da SAFX42 \(campo 01 ao 08\)__

__                                                                                 \+__

__                                                          Código da Observação \(campo 09\)__

__                                                                                 \+__

__                                                           Tipo da Observação \(campo 10\)__

A manutenção da tabela é feita na tela de manutenção dos documentos fiscais de Utilities, no módulo DW\.

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

Crítica da existência do documento na __SAFX42__:

Após a validação dos campos que identificam o documento fiscal \(campo 01 ao 08\), conforme as regras descritas, será verificado se o documento existe na base de dados \(SAFX42\)\. 

Caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                       “O documento fiscal informado não foi identificado na Tabela de Documentos Fiscais – Utilities \(SAFX42\)”*

No log aparecerão os dados de identificação do documento informado\.  

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

O código informado será validado na Tabela de Cadastro de Observações \(SAFX2009\)\.

Para acessar a SAFX2009, considerar o Grupo \(Relacionamento Tabelas x Grupo\) válido para o estabelecimento e data do documento informado\. Quanto à data de validade, considerar a maior data que seja <= a data do documento informado\.

Caso a observação não exista, o registro não será importado, e no log de erros será gravada uma mensagem informando que o código informado não existe na tabela \(mensagem padrão código 900031: “*Código da Observação não está cadastrado*”\)\.   

__RN10__

<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

<a id="OLE_LINK32"></a><a id="OLE_LINK33"></a><a id="OLE_LINK34"></a>__Campo Tipo de Observação__

Campo de preenchimento __*obrigatório*__\.

Deve ser = “L”\. 

Quando não preenchido, ou <> “L”, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(mensagem padrão código 91629: “*A informação do campo Tipo de Observação é inválida*”\):

__Obs__\.: Este campo tem duas opções: “I” \(Observação referente às Informações Complementares da nota\) ou “L” \(Observação referente aos Lançamentos Fiscais da nota\)\. Mas a princípio, será tratada *apenas* a opção “__L__”, uma vez que o registro C500 não trabalha com Informações Complementares\.

__RN11__

__Campo Descrição Complementar__

Campo de preenchimento __*não*__ obrigatório\.

__RN12__

__Campo Informações adicionais de interesse do Fisco __

Campo de preenchimento __*não*__ obrigatório\.

__RN13__

__Campo Informações complementares de interesse do Contribuinte __

Campo de preenchimento __*não*__ obrigatório\.

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


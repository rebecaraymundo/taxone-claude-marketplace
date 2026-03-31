# MTZ-Job-Servidor-Importacao_SAFX205

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX205.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 77 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX205

 Tabela das Formas de Pagamento do NFCe e NFe

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS10565

Tabela das Formas de Pagamento do NFCe e NFe\.

Criação da SAFX205 para carregar as informações referentes às Formas de Pagamento do NFCe e NFe para atendimento à Portaria CAT87/06\.

12/05/2017

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX205__ 🡪 vide manual de layout

A SAFX205 é uma tabela “filha” da SAFX07, e seu objetivo é informar para uma determinada nota fiscal \(identificada pelos campos 01 a 11\), as Formas de Pagamento do NFCe e NFe \(campos 12 a 17\)\. Para cada nota da SAFX07, poderão ser informadas uma ou várias formas de pagamento\.

Para detalhes sobre o objetivo e utilização desta tabela, consultar o manual de layout \(aba Indice e Tabelas SAFX\)\.

__Campos que compõe a chave da tabela:__

                           __                      Campos chave da SAFX07 \(campo 01 a 11\)__

__                                                                               \+__

__                                                        __

__                            Campos de identificação da forma de pagamento \(campo 12 e 13\)__

A manutenção da tabela é feita na tela de manutenção dos documentos fiscais, na aba “Capa”, através da opção “Formas de Pagamento”\.

__Crítica da existência do item na SAFX07:__

Após a validação dos campos que identificam a capa do documento fiscal \(campo 01 a 11\), conforme as regras descritas abaixo, será verificado se existe a nota fiscal na base de dados \(SAFX07\)\. 

Caso a nota não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                          “O documento fiscal informado não foi identificado na Tabela de Documentos Fiscais”*

Para facilitar a identificação do problema, o log deve informar os dados básicos da nota informado nos campos 01 ao 11\.  

 

MFS10565

__RN01__

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação da Empresa serão desconsiderados\)*

MFS10565

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento serão desconsiderados\)*

MFS10565

__RN03__

__Campo Data da Escrita Fiscal__

Campo de preenchimento __*obrigatório*__\.

Deve ser uma data válida\.

Quando não preenchido, ou quando for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “Data da Escrita Fiscal não preenchida ou inválida”*

MFS10565

__RN04__

__Campo Movimento Entrada/Saída __

Campo de preenchimento __*obrigatório*__\.

Valores válidos: '1', '2', '3', '4', '5', '9'\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(mensagem padrão\)\.

MFS10565

__RN05__

__Campo Normal ou Devolução __

Campo de preenchimento __*obrigatório*__\.

Valores válidos: '1', '2'\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(mensagem padrão\)\.

MFS10565

__RN06__

__Campo Tipo de Documento __

Campo de preenchimento __*obrigatório*__\.

Deve ser um código existente na Tabela de Tipos de Documento \(SAFX2005\)\.

Quando o campo não for preenchido, ou o código informado não existir na SAFX2005, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou que não foi encontrado na Tabela de Tipos de Documento \(mensagem padrão\)\.

MFS10565

__RN07__

__Campo Indicador da Pessoa Física/Jurídica \(Destinatário/Emitente\) __

Campo de preenchimento __*obrigatório*__\.

Valores válidos: '1', '2', ‘3’, ‘4’, ‘5’\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(mensagem padrão\)\.

MFS10565

__RN08__

__Campo Código da Pessoa Física/Jurídica \(Destinatário/Emitente\) __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão\)\.

A partir do conteúdo dos campos 07 e 08 \(indicador e código da pessoa fis/jur\) será verificada a existência da pessoa informada na Tabela de Pessoas Fis/Jur \(SAFX04\)\. Quando não encontrada, o registro não será importado, e no log de erros será gravada uma mensagem informando que a pessoa não existe na tabela \(mensagem padrão\)\.

MFS10565

__RN09__

__Campo Número do Documento Fiscal__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão\)\.

Ver na __RN00 __como será realizada a crítica de existência do documento\.

MFS10565

__RN10__

__CampoSérie do Documento Fiscal__

Campo de preenchimento __*não*__ __*obrigatório*__\.

Quando este campo não for preenchido, será gravado um caracter branco \(“ “\), pois o campo compõe a chave da tabela\.

MFS10565

__RN11__

__Campo Subsérie do Documento Fiscal__

Campo de preenchimento __*não*__ __*obrigatório*__\.

Quando este campo não for preenchido, será gravado um caracter branco \(“ “\), pois o campo compõe a chave da tabela\.

MFS10565

__RN12__

__Campo Código da Operação__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão\)\.

Será verificada a existência do código de operação informado na Tabela de Códigos de Operação \(SAFX2001\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que o código não existe na tabela \(mensagem padrão\)\.

MFS10565

__RN13__

<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

<a id="OLE_LINK32"></a><a id="OLE_LINK33"></a><a id="OLE_LINK34"></a>__Campo Comprovante de Pagamento__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*‘Comprovante do Pagamento deve ser preenchido\.’*

MFS10565

__RN14__

__Campo Natureza da Operação__

Campo de preenchimento __*obrigatório*__\.

Valores válidos: “1” ou “2” \(“1” para crédito; “2” para débito\)      

Quando não for preenchido ou o contéudo não for válido, o registro não será importado, e no log de erros será gravada uma mensagem informando que:

*“Campo Natureza de Operação deve ser preenchido com ”1” para crédito ou “2” para débito\.”*

MFS10565

__RN15__

__Campo Valor da Operação__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*‘Valor da Operação deve ser preenchido\.’*

MFS10565

__RN16__

__Campo CEP__

Campo de preenchimento __*não obrigatório*__\. 

MFS10565

__RN17__

__Campo Ponto de Venda__

Campo de preenchimento __*não obrigatório*__\.

MFS10565

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


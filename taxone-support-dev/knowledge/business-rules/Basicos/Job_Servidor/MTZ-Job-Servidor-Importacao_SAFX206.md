# MTZ-Job-Servidor-Importacao_SAFX206

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX206.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 79 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX206

Tabela de Boletim de Conformidade

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS11100

Andréa Rocha

Criação da SAFX206 para carregar o boletim de conformidade por produto da nota fiscal, para ser utilizado na geração do i\-SIMP\. 

27/06/2017

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX206__ 🡪 vide manual de layout

A SAFX206 é uma tabela “filha” da SAFX08, e seu objetivo é informar para um determinado item da nota fiscal \(identificado pelos campos 01 a 15\), o Boletim de Conformidade \(campos 16 a 20\)\. Para cada item da SAFX08, poderão ser informados um ou vários boletins de conformidade\.

__Campos que compõe a chave da tabela:__

                           __                      Campos chave da SAFX08 \(campo 01 a 15\)__

__                                                                               \+__

__                                                 Código da Característica Físico\-química \(campo 16\)__

A manutenção da tabela é feita na tela de manutenção dos documentos fiscais, na aba “Item Mercadoria”, através da opção “Boletim de Conformidade”\.

__Crítica da existência do item na SAFX08:__

Após a validação dos campos que identificam o item do documento fiscal \(campo 01 ao 15\), conforme as regras descritas abaixo, será verificado se o item existe na base de dados \(SAFX08\)\. 

Caso o item não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                          “O item do documento fiscal informado não foi identificado na Tabela de Itens de Documentos Fiscais”*

Para facilitar a identificação do problema, o log deve informar os dados básicos do item informado nos campos 01 a 15\.  

 

MFS11100

__RN01__

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação da Empresa serão desconsiderados\)*

MFS11100

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento serão desconsiderados\)*

MFS11100

__RN03__

__Campo Data da Escrita Fiscal__

Campo de preenchimento __*obrigatório*__\.

Deve ser uma data válida\.

Quando não preenchido, ou quando for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “Data da Escrita Fiscal não preenchida ou inválida”*

MFS11100

__RN04__

__Campo Movimento Entrada/Saída __

Campo de preenchimento __*obrigatório*__\.

Valores válidos: '1', '2', '3', '4', '5', '9'\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(mensagem padrão\)\.

MFS11100

__RN05__

__Campo Normal ou Devolução __

Campo de preenchimento __*obrigatório*__\.

Valores válidos: '1', '2'\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(mensagem padrão\)\.

MFS11100

__RN06__

__Campo Tipo de Documento __

Campo de preenchimento __*obrigatório*__\.

Deve ser um código existente na Tabela de Tipos de Documento \(SAFX2005\)\.

Quando o campo não for preenchido, ou o código informado não existir na SAFX2005, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou que não foi encontrado na Tabela de Tipos de Documento \(mensagem padrão\)\.

MFS11100

__RN07__

__Campo Indicador da Pessoa Física/Jurídica \(Destinatário/Emitente\) __

Campo de preenchimento __*obrigatório*__\.

Valores válidos: '1', '2', ‘3’, ‘4’, ‘5’\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(mensagem padrão\)\.

MFS11100

__RN08__

__Campo Código da Pessoa Física/Jurídica \(Destinatário/Emitente\) __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão\)\.

A partir do conteúdo dos campos 07 e 08 \(indicador e código da pessoa fis/jur\) será verificada a existência da pessoa informada na Tabela de Pessoas Fis/Jur \(SAFX04\)\. Quando não encontrada, o registro não será importado, e no log de erros será gravada uma mensagem informando que a pessoa não existe na tabela \(mensagem padrão\)\.

MFS11100

__RN09__

__Campo Número do Documento Fiscal__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão\)\.

Ver na __RN00 __como será realizada a crítica de existência do documento e item informados na SAFX08\.

MFS11100

__RN10__

__CampoSérie do Documento Fiscal__

Campo de preenchimento __*não*__ __*obrigatório*__\.

Quando este campo não for preenchido, será gravado um caracter branco \(“ “\), pois o campo compõe a chave da tabela\.

MFS11100

__RN11__

__Campo Subsérie do Documento Fiscal__

Campo de preenchimento __*não*__ __*obrigatório*__\.

Quando este campo não for preenchido, será gravado um caracter branco \(“ “\), pois o campo compõe a chave da tabela\.

MFS11100

__RN12__

__Campo Indicador do Produto__

Campo de preenchimento __*obrigatório*__\.

Valores válidos: '1', '2', '3', '4', '5', '6', '7', '8'\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(mensagem padrão\)\.

MFS11100

__RN13__

<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

<a id="OLE_LINK32"></a><a id="OLE_LINK33"></a><a id="OLE_LINK34"></a>__Campo Código do Produto__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão\)\.

A partir do conteúdo dos campos 12 e 13 \(indicador e código do produto\) será verificada a existência do produto informado na Tabela de Cadastro dos Produtos \(SAFX2013\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que o produto não existe na tabela \(mensagem padrão\)\.

MFS11100

__RN14__

__Campo Unidade Padrão__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão\)\.

O código informado deve existir na Tabela das Unidades de Medida Padrão \(SAFX2017\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que a unidade padrão não existe na tabela \(mensagem padrão\)\.

MFS11100

__RN15__

__Campo Item da Nota Fiscal__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão\)\.

MFS11100

__RN16__

__Campo Código da Característica Físico\-química__

Campo de preenchimento __*obrigatório*__\.

Deve ser um código existente na TACES95 e que data fiscal da nota esteja compreendida entre a data de validade inicial e final \(quando estiver preenchida\) do código\.

Quando o código informado não existir na TACES95 ou não for informado, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou que não foi encontrado na Tabela de Característica Físico\-Química \(mensagem padrão\)\.* *

*“Código da Característica Físico\-química não preenchido ou não cadastrado na tabela de Característica \(TACES95\)\."*

MFS11100

__RN17__

__Campo Número do Boletim de Conformidade__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido\.

“*Número do Boletim de Conformidade não preenchido\.*”

MFS11100

__RN18__

__Campo Código do Método __

Campo de preenchimento __*não*__ __*obrigatório*__\.

Quando preenchido, deve ser um código existente na TACES96 e que data fiscal da nota esteja compreendida entre a data de validade inicial e final \(quando estiver preenchida\) do código\.

Quando o código informado não existir na TACES96, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi encontrado na Tabela de Método de Aferição\.

*“Código do Método não cadastrado na tabela de Método de Aferição \(TACES96\)\."*

MFS11100

__RN19__

__Campo Valor da Característica__

Campo de preenchimento __*não*__ __*obrigatório*__\.

MFS11100

__RN20__

__Campo Massa Específica __

Campo de preenchimento __*não*__ __*obrigatório*__\.

MFS11100

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


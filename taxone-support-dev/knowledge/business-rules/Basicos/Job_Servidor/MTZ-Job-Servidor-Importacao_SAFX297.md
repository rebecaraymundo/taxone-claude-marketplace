# MTZ-Job-Servidor-Importacao_SAFX297

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX297.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 73 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX297

__                   Tabela das Informações Complementares das Operações Sujeitas ao ST __

__                                                                 \(Sped Fiscal – C480\)__

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS32521

Sped Fiscal – Atualização Legal da versão 1\.13, vigência Jan/2020

Criação da tabela SAFX297 para carga das informações complementares de ST, a serem utilizadas na geração do registro C480 do Sped Fiscal\. 

03/12/2019

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX297__ 🡪 vide manual de layout

A SAFX297 é uma tabela filha da SAFX993 \(Capa Cupom Fiscal\)\.

__Campos que compõe a chave da tabela: __Os campos chave da tabela definitiva são os mesmos campos que compõem a chave da X993 mais a identificação do produto:

                                                Chave do cupom \(SAFX993\) \+ Identificação do Produto

\- Empresa

\- Estabelecimento

\- Modelo \+ Número do Caixa \(X2087\)

\- COO \(Número do Documento\) 

\- Data da Emissão

\- Produto

Conforme define a chave da tabela definitiva, só poderá existir um registro de cada Produto, para um determinado cupom fiscal\.

A manutenção da tabela é feita no módulo DW, menu “*Manutenção 🡪 Cupom Fiscal \(EFD/REDF\) 🡪 Movimentos 🡪 Detalhe Informações Complementares Oper\. ST \(Sped Fiscal\)*”\.

As informações da SAFX297 são utilizadas na geração do Sped Fiscal, registro C480\.

*Obs\.: Se no SPED o registro “pai” C470 tivesse o número do item, a nova tabela poderia ser um complemento do item do cupom \(SAFX994\), assim como a SAFX296 é um complemento do item da nota \(SAFX08\)\. No entanto, o registro “pai” C470 não tem o campo NUM\_ITEM, e por isso, o C470 é gerado através de uma consolidação dos itens do cupom fiscal, de mesmo produto \(lembrando que é possível existir dois ou mais itens de mesmo código de produto\)\. Assim, a nova tabela também será por Produto, e por isso não pode ser um complemento do item do cupom\.*

__Crítica da existência do cupom fiscal:__

Por se tratar de uma tabela filha da SAFX993, só é permitida a inclusão de informações complementares na SAFX297 quando o cupom fiscal já existir\. Assim, após a validação dos campos de identificação do cupom \(campos 01 ao 06\) conforme as regras descritas abaixo, será verificado se o cupom em questão existe na SAFX993\. Caso não exista, o registro *não* será importado, e no log de erros será gravada uma mensagem de erro \(“*Cupom Fiscal não identificado na Tabela dos Cupons Fiscais \(SAFX993\)”*\)\.

__Sobre as mensagens de erro:__

Todas as mensagens gravadas no log de erros da importação, devem mostrar os dados de identificação do Cupom Fiscal, e do Produto, para permitir ao usuário a identificação do registro com erro\.

__RN01__

__Campo 01\-Código da Empresa__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

__RN02__

__Campo 02\-Código do Estabelecimento__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

__RN03__

__Campo 03\-Modelo do Documento__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(ex: mensagem padrão código 30079: “*Código do Modelo do Documento Fiscal não preenchido\. Favor verificar”*\)\.

__RN04__

__Campo 04\-Número do Caixa__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(ex: mensagem padrão código 91728: “*O campo* *Número do Caixa não está preenchido”*\)\.

Validação do número do equipamento na SAFX2087:

Através do Modelo do Documento e do Número do Caixa informados \(campos 03 e 04\), será verificada a existência do equipamento na Tabela de Equipamentos ECF \(SAFX2087\)\. Para obter o Grupo, considerar o mais atual em relação à data da emissão do documento \(campo 06\)\. Caso o equipamento não exista, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(ex: mensagem padrão código 91742: “*O Equipamento Emissor de Cupom Fiscal \(Modelo Documento \+ Número do Caixa\) não está cadastrado”*\)\. 

__RN05__

__Campo 05\-COO \(Contador de Ordem de Operação\)__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(ex: mensagem padrão código 91747: “*O campo* *Número do Contador de Ordem de Operação não está preenchido”*\)\.

__RN06__

__Campo 06\-Data de Emissão__

Campo de preenchimento __*obrigatório*__\.

Deve ser uma data válida\.

Quando não preenchida, o registro não será importado, e no log de erros será gravada uma mensagem, de acordo com o tipo do erro:

Caso não preenchida: “*O campo Data de Emissão deve ser preenchido” *\(mensagem padrão código 91521\);

Caso inválida: “*O campo Data de Emissão á inválido” *\(mensagem padrão código 91748\);

__RN07__

__Campo 07\-Indicador do Produto__

Campo de preenchimento __*obrigatório*__\.

Valores válidos: '1', '2', '3', '4', '5', '6', '7', '8'\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(mensagem padrão código 90035: “*Indicador do Produto \(Produto/Insumo/Embalagem/Consumo, etc\) não está preenchido ou preenchido com informação inválida*”\)\.

__RN08__

__Campo 08\-Código do Produto__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão código 60855: “*O Código do Produto deve ser preenchido*”\)\.

A partir do conteúdo dos campos 07 e 08 \(indicador e código do produto\) será verificada a existência do produto informado na Tabela de Cadastro dos Produtos \(SAFX2013\)\. Conforme o padrão, a pesquisa do produto na tabela deve considerar apenas as linhas do Grupo correto, e válidas em relação à data de emissão \(campo 06\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que o produto não existe na tabela \(mensagem padrão código 90034: “*Código do Produto não cadastrado*”\)\.

__RN09__

__Campo 10\-Código do Motivo:__

Campo de preenchimento __*obrigatório*__\.

Quando não informado, o registro não será importado, e no log de erros será gravada uma mensagem \(“*O campo Código do Motivo deve ser preenchido*\)\. 

O código informado será validado na “Tabela de Códigos de Motivo de Restituição / Complementação de ICMS” \(módulo DW\),      considerando apenas os códigos referentes à UF do estabelecimento \(as duas primeiras posições devem ser = UF do      Estabelecimento\)\. Quando não identificado na   tabela, o registro não será importado, e no log de erros será gravada uma      mensagem \(“*Código do Motivo não cadastrado na Tabela de Códigos de Motivo de Restituição/Complementação de ICMS”*\)\.

__RN10__

__Campo Quantidade Convertida__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido ou = zeros, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*A quantidade deve ser preenchida com valor maior que zero*”\)\.

__RN11__

__Campo Unidade de Medida__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão código 90149: “*O Campo Unidade de Medida não esta preenchido*\.”\)\.

O código informado deve existir na Tabela de Unidades de Medida \(SAFX2007\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que a unidade de medida não existe na tabela \(mensagem padrão código 90150: “*A Unidade de Medida não esta cadastrada*”\)\.

__RN12__

__Campo Valor Unitário Conv:__

Campo de preenchimento __*obrigatório*__\. Deve ser um valor > zeros\.

Quando não preenchido ou = zero, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem “*O campo Valor Unitário Conv\. deve ser preenchido com valor maior que zero*”\)\.

__RN13__

__Campo Valor Unitário ICMS na Oper\. Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN14__

__Campo Valor Unitário ICMS Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN15__

__Campo Valor Unitário ICMS Estoque Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN16__

__Campo Valor Unitário ICMS\-ST Estoque Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN17__

__Campo Valor Unitário FCP\-ST Estoque Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN18__

__Campo Valor Unitário ICMS\-ST Conv\. Rest\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN19__

__Campo Valor Unitário FCP\-ST Conv\. Rest\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN20__

__Campo Valor Unitário ICMS\-ST Conv\. Compl\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN21__

__Campo Valor Unitário FCP\-ST Conv\. Compl\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


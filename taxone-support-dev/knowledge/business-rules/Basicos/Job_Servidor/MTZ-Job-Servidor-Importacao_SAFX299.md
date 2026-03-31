# MTZ-Job-Servidor-Importacao_SAFX299

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX299.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 73 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX299

__                   Tabela das Informações Complementares das Operações Sujeitas ao ST __

__                                                                   \(EFD – C330\)__

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS32523

Sped Fiscal – Atualização Legal da versão 1\.13, vigência Jan/2020

Criação da tabela SAFX299 para carga das informações complementares de ST, a serem utilizadas na geração dos registros C330 do Sped Fiscal\. 

05/12/2019

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX299__ 🡪 vide manual de layout

A SAFX299 é uma tabela independente, cujo objetivo é gerar o registro C330 do Sped Fiscal\.

No Sped Fiscal, o registro “pai” do C330 é o resultado de uma consolidação \(C321\)\. Assim, a chave da SAFX999 é composta pelos campos da consolidação, considerando os registros “pais” \(C300, C320 e C321\):

 

__Campos que compõe a chave da tabela: __

\- Empresa

\- Estabelecimento

\- Data da Emissão                                *\(Chave C300\)*

\- Série dos Documentos                       *\(Chave C300\)*

\- Subsérie dos Documentos                 *\(Chave C300\)*

\- Número do Documento Inicial            *\(Chave C300\)*

\- Número do Documento Final             *\(Chave C300\)*

\- CST                                                    *\(Chave C320\)*

\- CFOP                                                 *\(Chave C320\)*

\- Alíquota                                              *\(Chave C320\)*

\- Produto                                              *\(Chave C321\)*

__Sobre as mensagens de erro:__

Todas as mensagens gravadas no log de erros da importação, devem mostrar os dados de identificação do registro \(campos chave\), para permitir ao usuário a identificação do erro\.

__RN01__

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

__RN03__

__Campo Data da Emissão__

Campo de preenchimento obrigatório\.

Deve ser uma data válida\.

Quando não preenchida ou inválida, o registro não será importado, e no log de erros será gravada uma mensagem, de acordo com o tipo do erro:

Caso não preenchida: “*O campo Data de Emissão deve ser preenchido” *\(mensagem padrão código 91521\);

Caso inválida: “*O campo Data de Emissão á inválido” *\(mensagem padrão código 91748\);

__RN04__

__Campo Série dos Documentos__

Campo de preenchimento obrigatório\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão código 90113: “*A Serie do Documento Fiscal deve ser preenchida*”\)\.

__RN05__

__Campo Subsérie dos Documentos__

Campo de preenchimento __*não*__ obrigatório\.

Quando não preenchido, será gravado um caracter branco \(“ “\), pois o campo compõe a chave da tabela\.

__RN06__

__Campo Número do Documento Inicial__

Campo de preenchimento obrigatório\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem de erro: “*O Número do Documento Inicial deve ser preenchido*”\.

__RN07__

__Campo Número do Documento Final__

Campo de preenchimento obrigatório\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem de erro: “*O Número do Documento Final deve ser preenchido*”\.

O número do documento final deve ser >= ao número do documento inicial\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem de erro: “*O Número do Documento Final deve ser maior ou igual ao Documento Inicial”\. *

__RN08__

__Código Situação Tributária A__

Campo de preenchimento obrigatório\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem de erro: “*O Código Situação Tributária A deve ser preenchido*”\.

O código informado deve existir na Tabela de Códigos de Situação Tributária Estadual A \(Y2025\_SIT\_TRB\_UF\_A\)\. Conforme o padrão, a pesquisa do código na tabela deve considerar apenas as linhas do Grupo correto, e válidas em relação à data de emissão \(campo 03\)\. Caso o código não seja identificado, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(mensagem padrão código 90397: “*O Código de Situação Tributária Estadual Tabela A não está cadastrado”*\.

__RN09__

__Código Situação Tributária B__

Campo de preenchimento obrigatório\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem de erro: “*O Código Situação Tributária B deve ser preenchido*”\.

O código informado deve existir na Tabela de Códigos de Situação Tributária Estadual B \(Y2026\_SIT\_TRB\_UF\_B\)\. Conforme o padrão, a pesquisa do código na tabela deve considerar apenas as linhas do Grupo correto, e válidas em relação à data de emissão \(campo 03\)\. Caso o código não seja identificado, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(mensagem padrão código 90398: “*O Código de Situação Tributária Estadual Tabela B não está cadastrado”*\.

__RN10__

__Código CFOP__

Campo de preenchimento obrigatório\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(mensagem padrão código 30005: “*CFOP não preenchido*”\)\.

O código informado deve existir na Tabela de Códigos Fiscais \(SAFX2012\), considerando apenas os códigos válidos em relação à data de emissão \(campo 03\)\. Caso o código não seja identificado, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(mensagem padrão código 90029: “*CFOP \- Código Fiscal de Operação e Prestação não cadastrado”\)*\.

__RN11__

__Código Alíquota__

Campo de preenchimento __*não*__ obrigatório\.

Quando não preenchido, o campo será gravado com zeros, pois compõe a chave da tabela\.

__RN12__

__Campo Indicador do Produto__

Campo de preenchimento obrigatório\.

Valores válidos: '1', '2', '3', '4', '5', '6', '7', '8'\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(mensagem padrão código 90035: “*Indicador do Produto \(Produto/Insumo/Embalagem/Consumo, etc\) não está preenchido ou preenchido com informação inválida*”\)\.

__RN13__

<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

<a id="OLE_LINK32"></a><a id="OLE_LINK33"></a><a id="OLE_LINK34"></a>__Campo Código do Produto__

Campo de preenchimento obrigatório\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão código 60855: “*O Código do Produto deve ser preenchido*”\)\.

A partir do conteúdo dos campos 12 e 13 \(indicador e código do produto\) será verificada a existência do produto informado na Tabela de Cadastro dos Produtos \(SAFX2013\)\. Conforme o padrão, a pesquisa do produto na tabela deve considerar apenas as linhas do Grupo correto, e válidas em relação à data de emissão \(campo 03\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que o produto não existe na tabela \(mensagem padrão código 90034: “*Código do Produto não cadastrado*”\)\.

__RN14__

__Campo Código do Motivo:__

Campo de preenchimento obrigatório\.

Quando não informado, o registro não será importado, e no log de erros será gravada uma mensagem \(“*O campo Código do Motivo deve ser preenchido*\)\. 

O código informado será validado na “Tabela de Códigos de Motivo de Restituição / Complementação de ICMS” \(módulo DW\),      considerando apenas os códigos referentes à UF do estabelecimento \(as duas primeiras posições devem ser = UF do      Estabelecimento\)\. Quando não identificado na   tabela, o registro não será importado, e no log de erros será gravada uma      mensagem \(“*Código do Motivo não cadastrado na Tabela de Códigos de Motivo de Restituição/Complementação de ICMS”*\)\.

__RN15__

__Campo Quantidade Convertida__

Campo de preenchimento obrigatório\.

Quando não preenchido ou = zeros, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*A quantidade deve ser preenchida com valor maior que zero*”\)\.

<a id="_Hlk25589382"></a>__RN16__

__Campo Unidade de Medida__

Campo de preenchimento obrigatório\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão código 90149: “*O Campo Unidade de Medida não esta preenchido*\.”\)\.

O código informado deve existir na Tabela das Unidades de Medida \(SAFX2007\)\. Conforme o padrão, a pesquisa do produto na tabela deve considerar apenas as linhas do Grupo correto, e válidas em relação à data de emissão \(campo 03\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que a unidade de medida não existe na tabela \(mensagem padrão código 90150: “*A Unidade de Medida não esta cadastrada*”\)\.

__RN17__

__Campo Valor Unitário Conv:__

Campo de preenchimento obrigatório\. Deve ser um valor > zeros\.

Quando não preenchido ou = zero, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem “*O campo Valor Unitário Conv\. deve ser preenchido com valor maior que zero*\.”\)\.

__RN18__

__Campo Valor Unitário ICMS na Oper\. Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN19__

__Campo Valor Unitário ICMS Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN20__

__Campo Valor Unitário ICMS Estoque Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN21__

__Campo Valor Unitário ICMS\-ST Estoque Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN22__

__Campo Valor Unitário FCP\-ST Estoque Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN23__

__Campo Valor Unitário ICMS\-ST Conv\. Rest\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN24__

__Campo Valor Unitário FCP\-ST Conv\. Rest\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN25__

__Campo Valor Unitário ICMS\-ST Conv\. Compl\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN26__

__Campo Valor Unitário FCP\-ST Conv\. Compl\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


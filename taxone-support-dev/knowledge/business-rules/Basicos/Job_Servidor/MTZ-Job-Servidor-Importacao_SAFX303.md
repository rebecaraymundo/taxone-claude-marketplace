# MTZ-Job-Servidor-Importacao_SAFX303

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX303.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 73 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX303

__                   Tabela das Informações Complementares das Operações Sujeitas ao ST __

__                                                                 \(Sped Fiscal – C880\)__

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS32525

Sped Fiscal – Atualização Legal da versão 1\.13, vigência Jan/2020

Criação da tabela SAFX303 para carga das informações complementares de ST, a serem utilizadas na geração do registro C880 do Sped Fiscal\. 

10/12/2019

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX303__ 🡪 vide manual de layout

A SAFX303 é uma tabela independente, cujo objetivo é gerar o registro C880 do Sped Fiscal\.

No Sped Fiscal, o registro “pai” do C880 é o resultado de uma consolidação dos itens dos cupons do resumo diário \(C860\), por Produto, CST e CFOP \(C870\)\. 

Estrutura da EFD dos resumos diários dos Cupons SAT:

__C860__ – Resumo Cupom SAT

    __C870__\-Itens do Resumo \(totais por produto/CST/CFOP\)   

         __C880__\-Informações Compl\. ST                                      

    __C890__\-Registro Analítico \(CST/CFOP/Aliq\)

__Campos que compõe a chave da tabela: __A__ __chave é composta pelos campos da consolidação, considerando os registros “pais” C860 e C870:

\- Empresa

\- Estabelecimento

\- Modelo dos Documentos                                   *\(chave da C860\)*

\- Número de Série do Equipamento SAT             *\(chave da C860\)*

\- Data de Emissão                                                *\(chave da C860\)*

\- Produto                                                                 *\(chave da C870\)*

\- CST                                                                      *\(chave da C870\)*

\- CFOP                                                                   *\(chave da C870\)*

A manutenção da tabela é feita no módulo DW, menu “*Manutenção 🡪 Cupom Fiscal Eletrônico 🡪 Resumo Diário \- Informações Complementares Oper\. ST \(Sped Fiscal\)*”\.

__Obs\.__: A importação da SAFX303 não faz nenhuma crítica referente a existência do resumo diário \(C860\), uma vez que não existe uma tabela para este resumo\. Os dados do resumo são gerados no momento da geração do meio magnético do Sped Fiscal, através da consolidação dos cupons fiscais da SAFX201\.

   

__Sobre as mensagens de erro:__

Todas as mensagens gravadas no log de erros da importação, devem exibir os dados que compõem a chave, para permitir ao usuário a identificação do registro com erro\.

__RN01__

__Campo 01\-Código da Empresa__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

__RN02__

__Campo 02\-Código do Estabelecimento__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

__RN03__

__Campo 03\-Modelo Documento__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(ex: mensagem padrão código 30079: “*Código do Modelo do Documento Fiscal não preenchido\. Favor verificar”*\)\.

__RN04__

__Campo 04\-Número do Equipamento SAT__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(mensagem padrão código 92455: “*Numero de serie do equipamento SAT deve ser preenchido”*\)\.

__RN05__

__Campo 05\-Data da Emissão__

Campo de preenchimento __*obrigatório*__\.

Deve ser uma data válida\.

Quando não preenchida, ou inválida, o registro não será importado, e no log de erros será gravada uma mensagem, de acordo com o tipo do erro:

Caso não preenchida: “*O campo Data de Emissão deve ser preenchido” *\(mensagem padrão código 91521\);

Caso inválida: “*O campo Data de Emissão é inválido” *\(mensagem padrão código 91748\);

__RN06__

__Campo 06\-Indicador do Produto__

Campo de preenchimento __*obrigatório*__\.

Valores válidos: '1', '2', '3', '4', '5', '6', '7', '8'\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(mensagem padrão código 90035: “*Indicador do Produto \(Produto/Insumo/Embalagem/Consumo, etc\) não está preenchido ou preenchido com informação inválida*”\)\.

__RN07__

__Campo 07\-Código do Produto__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão código 60855: “*O Código do Produto deve ser preenchido*”\)\.

A partir do conteúdo dos campos 06 e 07 \(indicador e código do produto\) será verificada a existência do produto informado na Tabela de Cadastro dos Produtos \(SAFX2013\)\. Conforme o padrão, a pesquisa do produto na tabela deve considerar apenas as linhas do Grupo correto, e válidas em relação à data de emissão \(campo 05\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que o produto não existe na tabela \(mensagem padrão código 90034: “*Código do Produto não cadastrado*”\)\.

__RN08__

__Campo 09\-Código Situação Tributária A__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem de erro: “*O Código Situação Tributária A deve ser preenchido*”\.

O código informado deve existir na Tabela de Códigos de Situação Tributária Estadual A \(Y2025\_SIT\_TRB\_UF\_A\)\. Conforme o padrão, a pesquisa do código na tabela deve considerar apenas as linhas do Grupo correto, e válidas em relação à data de emissão \(campo 05\)\. Caso o código não seja identificado, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(mensagem padrão código 90397: “*O Código de Situação Tributária Estadual Tabela A não está cadastrado”*\.

__RN09__

__Campo 10\-Código Situação Tributária B__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem de erro: “*O Código Situação Tributária B deve ser preenchido*”\.

O código informado deve existir na Tabela de Códigos de Situação Tributária Estadual B \(Y2026\_SIT\_TRB\_UF\_B\)\. Conforme o padrão, a pesquisa do código na tabela deve considerar apenas as linhas do Grupo correto, e válidas em relação à data de emissão \(campo 05\)\. Caso o código não seja identificado, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(mensagem padrão código 90398: “*O Código de Situação Tributária Estadual Tabela B não está cadastrado”*\.

__RN10__

__Campo 11\-CFOP__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(mensagem padrão código 30005: “*CFOP não preenchido*”\)\.

O código informado deve existir na Tabela de Códigos Fiscais \(SAFX2012\), considerando apenas os códigos válidos em relação à data de emissão \(campo 05\)\. Caso o código não seja identificado, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(mensagem padrão código 90029: “*CFOP \- Código Fiscal de Operação e Prestação não cadastrado”\)*\.

__RN11__

__Campo 12\-Código do Motivo:__

Campo de preenchimento __*obrigatório*__\.

Quando não informado, o registro não será importado, e no log de erros será gravada uma mensagem \(“*O campo Código do Motivo deve ser preenchido*\)\. 

O código informado será validado na “Tabela de Códigos de Motivo de Restituição / Complementação de ICMS” \(módulo DW\),      considerando apenas os códigos referentes à UF do estabelecimento \(as duas primeiras posições devem ser = UF do      Estabelecimento\)\. Quando não identificado na   tabela, o registro não será importado, e no log de erros será gravada uma      mensagem \(“*Código do Motivo não cadastrado na Tabela de Códigos de Motivo de Restituição/Complementação de ICMS”*\)\.

__RN12__

__Campo Quantidade Convertida__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido ou = zeros, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*A quantidade deve ser preenchida com valor maior que zero*”\)\.

__RN13__

__Campo Unidade de Medida__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão código 90149: “*O Campo Unidade de Medida não esta preenchido*\.”\)\.

O código informado deve existir na Tabela de Unidades de Medida \(SAFX2007\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que a unidade de medida não existe na tabela \(mensagem padrão código 90150: “*A Unidade de Medida não esta cadastrada*”\)\.

__RN14__

__Campo Valor Unitário Conv:__

Campo de preenchimento __*obrigatório*__\. Deve ser um valor > zeros\.

Quando não preenchido ou = zero, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem “*O campo Valor Unitário Conv\. deve ser preenchido com valor maior que zero*”\)\.

__RN15__

__Campo Valor Unitário ICMS na Oper\. Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN16__

__Campo Valor Unitário ICMS Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN17__

__Campo Valor Unitário ICMS Estoque Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN18__

__Campo Valor Unitário ICMS\-ST Estoque Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN19__

__Campo Valor Unitário FCP\-ST Estoque Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN20__

__Campo Valor Unitário ICMS\-ST Conv\. Rest\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN21__

__Campo Valor Unitário FCP\-ST Conv\. Rest\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN22__

__Campo Valor Unitário ICMS\-ST Conv\. Compl\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN23__

__Campo Valor Unitário FCP\-ST Conv\. Compl\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


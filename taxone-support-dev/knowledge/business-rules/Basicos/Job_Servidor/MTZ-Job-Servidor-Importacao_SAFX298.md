# MTZ-Job-Servidor-Importacao_SAFX298

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX298.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 71 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX298

__                   Tabela das Informações Complementares das Operações Sujeitas ao ST __

__                                                                 \(Sped Fiscal \- C815\)__

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS32287

Sped Fiscal – Atualização Legal da versão 1\.13, vigência Jan/2020

Criação da tabela SAFX298 para carga das informações complementares de ST, a serem utilizadas na geração do registro C815 do Sped Fiscal\. 

25/11/2019

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX296__ 🡪 vide manual de layout

A SAFX298 é uma tabela complementar da SAFX202 \(Itens do Cupom Fiscal Eletrônico SAT\)\.

__Campos que compõe a chave da tabela: __Os campos chave são os mesmos campos que compõem a chave da X202, por se tratar de uma tabela complementar, com ocorrência de apenas um registro para cada item da X202\.

A manutenção da tabela é feita na tela de manutenção dos Cupons Fiscais Eletrônicos \(módulo DW, menu Manutenção > Cupom Fiscal Eletrônico\), através da opção “__*Informações Complementares Oper\. ST \(Sped Fiscal\)*__” da aba “Detalhe Cupom Fiscal Eletrônico – SAT”\.

As informações da SAFX298 são utilizadas na geração do Sped Fiscal, registro C815\.

__Crítica da existência do item do cupom fiscal:__

Por se tratar de uma tabela complementar à SAFX202, só é permitida a inclusão de informações complementares na SAFX298 quando o item do cupom fiscal já existir\. Assim, após a validação dos campos de identificação do item \(campo 01 ao 06\) conforme as regras descritas abaixo, será verificado se o item em questão existe na SAFX202\. Caso não exista, o registro *não* será importado, e no log de erros será gravada uma mensagem de erro \(“*Item do cupom fiscal inexistente”*\)\.

__Sobre as mensagens de erro:__

Todas as mensagens gravadas no log de erros da importação, devem mostrar os dados de identificação do item do cupom fiscal, para permitir ao usuário a identificação do registro com erro\.

__RN01__

__Campo 01\-Código da Empresa__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

__RN02__

__Campo 02\-Código do Estabelecimento__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

__RN03__

__Campo 03\-Número do Equipamento SAT__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(mensagem padrão código 92455: “*Numero de serie do equipamento SAT deve ser preenchido”*\)\.

__RN04__

__Campo 04\-Número do Cupom Fiscal Eletrônico__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(mensagem padrão código 92457: “*Número do cupom fiscal eletrônico deve ser preenchido”*\)\.

__RN05__

__Campo 05\-Data da Emissão__

Campo de preenchimento __*obrigatório*__\.

Deve ser uma data válida\.

Quando não preenchida, o registro não será importado, e no log de erros será gravada uma mensagem, de acordo com o tipo do erro:

Caso não preenchida: “*O campo Data de Emissão deve ser preenchido” *\(mensagem padrão código 91521\);

Caso inválida: “*O campo Data de Emissão á inválido” *\(mensagem padrão código 91748\);

__RN06__

__Campo 06\-Número do Item__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(mensagem padrão código 91760: “*O Campo Número do Item não está preenchido*”\)\.

__RN07__

__Campo 07\-Código do Motivo:__

Campo de preenchimento __*obrigatório*__\.

Quando não informado, o registro não será importado, e no log de erros será gravada uma mensagem \(“*O campo Código do Motivo deve ser preenchido*\)\. 

O código informado será validado na “Tabela de Códigos de Motivo de Restituição / Complementação de ICMS” \(módulo DW\),      considerando apenas os códigos referentes à UF do estabelecimento \(as duas primeiras posições devem ser = UF do      Estabelecimento\)\. Quando não identificado na   tabela, o registro não será importado, e no log de erros será gravada uma      mensagem \(“*Código do Motivo não cadastrado na Tabela de Códigos de Motivo de Restituição/Complementação de ICMS”*\)\.

__RN08__

__Campo Quantidade Convertida__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido ou = zeros, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*A quantidade deve ser preenchida com valor maior que zero*”\)\.

__RN09__

__Campo Unidade de Medida__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão código 90149: “*O Campo Unidade de Medida não esta preenchido*\.”\)\.

O código informado deve existir na Tabela de Unidades de Medida \(SAFX2007\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que a unidade de medida não existe na tabela \(mensagem padrão código 90150: “*A Unidade de Medida não esta cadastrada*”\)\.

__RN10__

__Campo Valor Unitário Conv:__

Campo de preenchimento __*obrigatório*__\. Deve ser um valor > zeros\.

Quando não preenchido ou = zero, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem “*O campo Valor Unitário Conv\. deve ser preenchido com valor maior que zero*”\)\.

__RN11__

__Campo Valor Unitário ICMS na Oper\. Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN12__

__Campo Valor Unitário ICMS Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN13__

__Campo Valor Unitário ICMS Estoque Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN14__

__Campo Valor Unitário ICMS\-ST Estoque Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN15__

__Campo Valor Unitário FCP\-ST Estoque Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN16__

__Campo Valor Unitário ICMS\-ST Conv\. Rest\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN17__

__Campo Valor Unitário FCP\-ST Conv\. Rest\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN18__

__Campo Valor Unitário ICMS\-ST Conv\. Compl\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN19__

__Campo Valor Unitário FCP\-ST Conv\. Compl\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


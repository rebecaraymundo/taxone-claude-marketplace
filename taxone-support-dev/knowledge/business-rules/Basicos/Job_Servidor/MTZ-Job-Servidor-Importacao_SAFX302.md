# MTZ-Job-Servidor-Importacao_SAFX302

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX302.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 74 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX302

__                   Tabela das Informações Complementares das Operações Sujeitas ao ST __

__                                                                 \(Sped Fiscal – C430\)__

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS32524

Sped Fiscal – Atualização Legal da versão 1\.13, vigência Jan/2020

Criação da tabela SAFX302 para carga das informações complementares de ST, a serem utilizadas na geração do registro C430 do Sped Fiscal\. 

09/12/2019

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX302__ 🡪 vide manual de layout

A SAFX302 é uma tabela independente, cujo objetivo é gerar o registro C430 do Sped Fiscal\.

No Sped Fiscal, o registro “pai” do C430 é o resultado da consolidação da movimentação da Redução Z por item \(C425\)\. O novo registro C430 é apenas um complemento de C425\.

__Campos que compõe a chave da tabela: __A chave é composta pelos campos da consolidação, considerando os registros “pais” \(C400, C405, C420 e C425\):

 

Campos chave:

\- Modelo \+ Número do Caixa \(X2087\)                *\(Campo chave da X991\)*

\- CRZ \(Número Contador Redução Z\)               *\(Campo chave da X991\)*

\- Data do Movimento                                          *\(Campo chave da X991\)*

\- Código do Totalizador Parcial ECF                 *\(Campo chave da X992\)*

\- Produto 

Obs\.: *O Número Sequencial do Totalizador não compõe a chave, pois ele não faz parte da chave da X996 \(Totalizadores Parciais\)\.*

Conforme define a chave da tabela definitiva, só poderá existir um registro de cada Produto, para cada Redução Z \+ Código do Totalizador Parcial ECF\. 

A manutenção da tabela é feita no módulo DW, menu “*Manutenção 🡪 Cupom Fiscal \(EFD/REDF\) 🡪 Movimentos 🡪 Detalhe Informações Complementares Oper\. ST \(Sped Fiscal\) – Redução Z*”\.

__Sobre as mensagens de erro:__

Todas as mensagens gravadas no log de erros da importação, devem mostrar os dados de identificação da Redução Z, Código do Totalizador Parcial e o Produto, para permitir ao usuário a identificação do registro com erro\.

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

Através do Modelo do Documento e do Número do Caixa informados \(campos 03 e 04\), será verificada a existência do equipamento na Tabela de Equipamentos ECF \(SAFX2087\)\. Para obter o Grupo, considerar o mais atual em relação à data do movimento \(campo 06\)\. Caso o equipamento não exista, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(ex: mensagem padrão código 91742: “*O Equipamento Emissor de Cupom Fiscal \(Modelo Documento \+ Número do Caixa\) não está cadastrado”*\)\. 

__RN05__

__Campo 05\-CRZ:__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(ex: mensagem padrão código 91746: “*O Campo Número do CRZ não está preenchido”*\)\.

__RN06__

__Campo 06\-Data do Movimento:__

Campo de preenchimento __*obrigatório*__\.

Deve ser uma data válida\.

Quando não preenchida, o registro não será importado, e no log de erros será gravada uma mensagem, de acordo com o tipo do erro:

Caso não preenchida: “*O Campo Data do Movimento deve ser preenchido*”* *\(mensagem padrão código 90117\);

Caso inválida: “*O Data do Movimento não é válida” *\(mensagem padrão código 90010\);

__Validação da Redução Z na SAFX991__:

Após a validação dos campos que identificam a Redução Z \(campos 01 ao 06\), conforme as regras descritas, será verificado se a Redução Z existe na SAFX991\. Caso não exista, o registro *não* será importado, e no log de erros será gravada a seguinte mensagem de erro: *“A Redução Z \(campos 01 ao 06\) não foi identificada na Tabela Capa Redução Z \(SAFX991\)”\.*

__RN07__

__Campo 07\-Código do Totalizador Parcial ECF__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(ex: mensagem padrão código 91741: “*O Campo Código do Totalizador Parcial do ECF não está preenchido”*\)\.

__Validação do Totalizador Parcial na Tabela dos Totalizadores Parciais \(SAFX996\)__:

Após a validação dos campos que identificam o Totalizador Parcial \(Modelo, Número do Caixa e Código do Totalizador Parcial\), conforme as regras descritas, será verificado se ele existe na Tabela dos Totalizadores Parciais \(SAFX996\)\. Caso não exista, o registro *não* será importado, e no log de erros será gravada uma mensagem de erro \(ex: mensagem padrão código 91743: *“O Campo Código do Totalizador Parcial do ECF não está cadastrado”\.*

__Validação se o Totalizador Parcial foi cadastrado p/a Redução Z \(SAFX992\)__:

A partir dos campos 01 a 07, será verificado se o totalizador parcial informado está cadastrado para a Redução Z em questão, na Tabela Detalhe da Redução Z \(SAFX992\)\. Caso não exista, o registro *não* será importado, e no log de erros será gravada a seguinte mensagem de erro: *“Não existe registro do Código do Totalizador Parcial para a Redução Z informada \(SAFX992\)”\.*

__RN08__

__Campo 08\-Indicador do Produto__

Campo de preenchimento __*obrigatório*__\.

Valores válidos: '1', '2', '3', '4', '5', '6', '7', '8'\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido, ou está com conteúdo inválido \(mensagem padrão código 90035: “*Indicador do Produto \(Produto/Insumo/Embalagem/Consumo, etc\) não está preenchido ou preenchido com informação inválida*”\)\.

__RN09__

__Campo 09\-Código do Produto__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão código 60855: “*O Código do Produto deve ser preenchido*”\)\.

A partir do conteúdo dos campos 08 e 09 \(indicador e código do produto\) será verificada a existência do produto informado na Tabela de Cadastro dos Produtos \(SAFX2013\)\. Conforme o padrão, a pesquisa do produto na tabela deve considerar apenas as linhas do Grupo correto, e válidas em relação à data do movimento \(campo 06\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que o produto não existe na tabela \(mensagem padrão código 90034: “*Código do Produto não cadastrado*”\)\.

__RN10__

__Campo 11\-Código do Motivo:__

Campo de preenchimento __*obrigatório*__\.

Quando não informado, o registro não será importado, e no log de erros será gravada uma mensagem \(“*O campo Código do Motivo deve ser preenchido*\)\. 

O código informado será validado na “Tabela de Códigos de Motivo de Restituição / Complementação de ICMS” \(módulo DW\),      considerando apenas os códigos referentes à UF do estabelecimento \(as duas primeiras posições devem ser = UF do      Estabelecimento\)\. Quando não identificado na   tabela, o registro não será importado, e no log de erros será gravada uma      mensagem \(“*Código do Motivo não cadastrado na Tabela de Códigos de Motivo de Restituição/Complementação de ICMS”*\)\.

__RN11__

__Campo Quantidade Convertida__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido ou = zeros, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*A quantidade deve ser preenchida com valor maior que zero*”\)\.

__RN12__

__Campo Unidade de Medida__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem padrão código 90149: “*O Campo Unidade de Medida não esta preenchido*”\)\.

O código informado deve existir na Tabela de Unidades de Medida \(SAFX2007\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que a unidade de medida não existe na tabela \(mensagem padrão código 90150: “*A Unidade de Medida não esta cadastrada*”\)\.

__RN13__

__Campo Valor Unitário Conv:__

Campo de preenchimento __*obrigatório*__\. Deve ser um valor > zeros\.

Quando não preenchido ou = zero, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem “*O campo Valor Unitário Conv\. deve ser preenchido com valor maior que zero*”\)\.

__RN14__

__Campo Valor Unitário ICMS na Oper\. Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN15__

__Campo Valor Unitário ICMS Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN16__

__Campo Valor Unitário ICMS Estoque Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN17__

__Campo Valor Unitário ICMS\-ST Estoque Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN18__

__Campo Valor Unitário FCP\-ST Estoque Conv:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN19__

__Campo Valor Unitário ICMS\-ST Conv\. Rest\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN20__

__Campo Valor Unitário FCP\-ST Conv\. Rest\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN21__

__Campo Valor Unitário ICMS\-ST Conv\. Compl\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

__RN22__

__Campo Valor Unitário FCP\-ST Conv\. Compl\.:__

Campo *não* obrigatório \(quando não preenchido, gravar zeros\)\.

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


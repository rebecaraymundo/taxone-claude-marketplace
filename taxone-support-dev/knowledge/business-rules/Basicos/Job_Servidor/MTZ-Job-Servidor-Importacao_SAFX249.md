# MTZ-Job-Servidor-Importacao_SAFX249

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX249.docx
- **Modificado:** 2022-06-06
- **Tamanho:** 72 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX249

Tabela do Demonstrativo de Pagamento dos Autônomos – Pagamentos Parciais

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS14409

Criação da SAFX249 

Criação da SAFX249 para a importação dos dados dos pagamentos parciais dos demonstrativos de pagamento dos autônomos, para a geração do eSocial\. 

30/11/2017

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX249__ 🡪 vide manual de layout

A SAFX249 foi criada na __MFS14409__, para a importação dos dados dos pagamentos parciais d__o__s__ __demonstrativos de pagamento dos autônomos\. Estas informações são utilizadas na geração do evento S\-1210 do eSocial\.

Esta é uma tabela “filha” da SAFX247 \(Demonstrativo de Pagamento dos Autônomos\), onde serão informados os pagamentos parciais referentes ao demonstrativo informado na tabela “mãe”\. Essa tabela será utilizada apenas no caso de pagamentos parciais, ou seja, quando o campo “09\-Indicador de Pagamento Total” da tabela mãe \(SAFX247\) for = “N”, conforme as orientações do manual de layout\.  

__Campos que compõe a chave da tabela \(PK\):__

Os campos que compõe a chave de identificação da tabela serão os campos chave da tabela “mãe” \+ campos que identificam o pagamento parcial na tabela “filha”:

\- Código da Empresa 

\- Código do Estabelecimento 

\- Indicador Pessoa Fis/Jur 

\- Código Pessoa Fis/Jur 

\- Ano Competência

\- Mês Competência 

\- Identificador do Demonstrativo de Pagamento

   

    Campos chave da tabela mãe \(SAFX247\)

\- Data do Pagamento

\- Código da Tabela da Rubrica

\- Código da Rubrica

   Campos de identificação do pagamento parcial

__RN01__

__RN02__

__RN03__

__RN04__

__RN05__

__RN06__

__RN07__

__Campo Código da Empresa__

__Campo Código do Estabelecimento__

__Campo Ano Competência __

__Campo Mês Competência__

__Campo Indicador Pessoa Fis/Jur __

__Campo Código Pessoa Fis/Jur __

__Campo Identificador do Demonstrativo de Pagamento __

Estes são os campos chave da tabela “mãe” \(SAFX247\), e assim, a validação é a mesma feita na importação da SAFX247\.

Crítica da existência do demonstrativo na tabela mãe \(SAFX247\):

A partir dos dados informados nestes campos, será verificada a existência do registro na SAFX247\. Caso não exista, será gravada a seguinte mensagem de erro no log da importação:

*       “O Demonstrativo de Pagamento não existe na Tabela de Demonstrativo de Pagamento dos Autônomos \(SAFX247\)”*

Crítica sobre o campo “Indicador de Pagamento Total” do demonstrativo \(SAFX247\):

Quando o demonstrativo existir, será verificada a informação do campo “*09\-Indicador de Pagamento Total*”, pois os pagamentos parciais da SAFX249 só devem ser informados quando este campo for = “N”: 

Se campo “*09\-Indicador de Pagamento Total*” da SAFX247 <> “N”:

     Neste caso, será gravada a seguinte mensagem de erro no log da importação, e o registro não será importado:

*                 “Os Pagamentos Parciais \(SAFX249\) só devem ser informados quando o Indicador de Pagamento Total*

*                                do demonstrativo \(SAFX247\) for “N”, indicando que o pagamento não foi total”*

__RN08__

__Campo Data do Pagamento __

Campo de preenchimento obrigatório\.

Deve ser uma data válida\.

 

Quando não preenchida ou inválida, será gravada mensagem de erro padrão e o registro não será importado\.

__RN09__

__Campo Código da Tabela da Rubrica __

Campo de preenchimento obrigatório\.

Quando não preenchido, será gravada mensagem de erro padrão e o registro não será importado\.

\(Ver __RN10__\)

__RN10__

__Campo Código da Rubrica__

Campo de preenchimento obrigatório\.

Quando não preenchido, será gravada mensagem de erro padrão e o registro não será importado\.

Validação da Rubrica na SAFX2114:

O código da tabela da rubrica e o código da rubrica, informados nos campos 09 e 10, devem estar cadastrados na Tabela de Cadastro das Rubricas \(SAFX2114\)\.

Para pesquisar os códigos na SAFX2114, considerar:

\-Grupo – Grupo obtido conforme regra padrão __\(\*\*\*\)__;

\-Código da Tabela da Rubrica – código da tabela da rubrica informado no campo 09;

\-Código da Rubrica – código da rubrica informado no campo 10;

\-Data da Validade Inicial – maior data existente, cujo mês/ano seja <= ao mês/ano de competência informados nos campos 03 e 04;

__*\(\*\*\*\)*__* O *__*Grupo*__* a ser utilizado será obtido a partir da regra básica, considerando o Grupo \(Relacionamento Tabelas x Grupos\) de maior data de validade, cujo mês/ano seja <= ao mês/ano de competência informado, e para o qual a tabela SAFX2114 esteja associada\.*

Caso a rubrica não exista na SAFX2114, será gravada mensagem de erro padrão e o registro não será importado\.

__RN11__

__Campo Tipo de Pagamento__

Quando de preenchido obrigatório\.

Valores válidos:

01 \(Pagamento de remuneração, conforme apurado no evento S\-1200\)

02 \(Pagamento de verbas rescisórias conforme apurado no evento S\-2299\)

03 \(Pagamento de verbas rescisórias conforme apurado no evento S\-2399\)

05 \(Pagamento de remuneração conforme apurado no evento S\-1202\)

06 \(Pagamento de Benefícios Previdenciários, conforme apurado no evento S\-1207\)

07 \(Recibo de férias\)

09 \(Pagamento relativo a competências anteriores ao início de obrigatoriedade do eSocial\)

Quando o campo não for preenchido, ou for preenchido com um conteúdo inválido, será gravada mensagem de erro padrão e o registro não será importado\. 

__RN12__

__Campo Quantidade de Referência__

Campo de preenchimento obrigatório\.

Quando não preenchido, será gravada mensagem de erro padrão e o registro não será importado\.

__RN13__

__Campo Fator de Cálculo __

Campo de preenchimento obrigatório\.

Quando não preenchido, será gravada mensagem de erro padrão e o registro não será importado\.

__RN14__

__Campo Valor Unitário__

Campo de preenchimento obrigatório\.

Quando não preenchido, será gravada mensagem de erro padrão e o registro não será importado\.

__RN15__

__Campo Valor Total__

Campo de preenchimento obrigatório\.

Deve ser um valor > zeros\.

Quando não preenchido ou = zeros, será gravada a seguinte mensagem de erro e o registro não será importado\.

*                             “O valor total da rubrica deve ser preenchido com um valor maior que zero”\.*


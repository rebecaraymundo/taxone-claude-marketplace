# MTZ-Job-Servidor-Importacao_SAFX248

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX248.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 71 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX248

Tabela do Demonstrativo de Pagamento dos Autônomos \- Rubricas

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS14409

Criação da SAFX248 

Criação da SAFX248 para a importação dos dados das rubricas dos demonstrativos de pagamento dos trabalhadores autônomos, para a geração do eSocial\. 

30/11/2017

CH24140\_2018

\(MFS\-21209\)

João Henrique

Retirada da obrigatoriedade dos campos 54 – qtdRubr, 55 – fatorRubr e 56 – vrUnit, representados nos campos 10, 11 e 12 da SAFX248\.

25/09/2018

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX248__ 🡪 vide manual de layout

A SAFX248 foi criada na __MFS14409__, para a importação dos dados das rubricas d__o__s__ __demonstrativos de pagamento dos trabalhadores autônomos\. Estas informações são utilizadas na geração dos eventos S\-1200 e S\-1210 do eSocial\.

Esta é uma tabela “filha” da SAFX247 \(Demonstrativo de Pagamento dos Autônomos\), onde serão informadas as rubricas referentes ao demonstrativo informado na tabela “mãe”\.

__Campos que compõe a chave da tabela \(PK\):__

Desta forma, os campos que compõe a chave de identificação da tabela serão os campos chave da tabela “mãe” \+ campos que identificam a rubrica na tabela “filha”:

\- Código da Empresa 

\- Código do Estabelecimento 

\- Indicador Pessoa Fis/Jur 

\- Código Pessoa Fis/Jur 

\- Ano Competência

\- Mês Competência 

\- Identificador do Demonstrativo de Pagamento

   

    Campos chave da tabela mãe \(SAFX247\)

\- Código da Tabela da Rubrica

\- Código da Rubrica

     Campos de identificação da Rubrica

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

__RN08__

__Campo Código da Tabela da Rubrica __

Campo de preenchimento obrigatório\.

Quando não preenchido, será gravada mensagem de erro padrão e o registro não será importado\.

__RN09__

__Campo Código da Rubrica__

Campo de preenchimento obrigatório\.

Quando não preenchido, será gravada mensagem de erro padrão e o registro não será importado\.

Validação da Rubrica na SAFX2114:

O código da tabela da rubrica e o código da rubrica informados nos campos 08 e 09, devem estar cadastrados na Tabela de Cadastro das Rubricas \(SAFX2114\)\.

Para pesquisar os códigos na SAFX2114, considerar:

\-Grupo – Grupo obtido conforme regra padrão __\(\*\*\*\)__;

\-Código da Tabela da Rubrica – código da tabela da rubrica informado no campo 08;

\-Código da Rubrica – código da rubrica informado no campo 09;

\-Data da Validade Inicial – maior data existente, cujo mês/ano seja <= ao mês/ano de competência informados nos campos 03 e 04;

\-Data de Validade Final – a validade final deve estar nula, ou ser de um mês/ano > mês/ano de competência informados nos campos 03 e 04;

__*\(\*\*\*\)*__* O *__*Grupo*__* a ser utilizado será obtido a partir da regra básica, considerando o Grupo \(Relacionamento Tabelas x Grupos\) de maior data de validade, cujo mês/ano seja <= ao mês/ano de competência informado, e para o qual a tabela SAFX2114 esteja associada\.*

A verificação das datas de validade inicial e final da rubrica, têm por objetivo garantir que a rubrica é válida no mês de competência\.

Caso a rubrica não exista na SAFX2114, considerando as condições acima, será gravada mensagem de erro padrão e o registro não será importado\. Exemplo: “*A Rubrica não existe na Tabela de Cadastro das Rubricas \(SAFX2114\), ou não é válida para o período de competência”*\.

__RN10__

__Campo Quantidade de Referência__

Campo de preenchimento obrigatório\.

Quando não preenchido, será gravada mensagem de erro padrão e o registro não será importado\.

CH24140\_2018

\(MFS\-21209\)

__RN11__

__Campo Fator de Cálculo __

Campo de preenchimento obrigatório\.

Quando não preenchido, será gravada mensagem de erro padrão e o registro não será importado\.

CH24140\_2018

\(MFS\-21209\)

__RN12__

__Campo Valor Unitário__

Campo de preenchimento obrigatório\.

Quando não preenchido, será gravada mensagem de erro padrão e o registro não será importado\.

CH24140\_2018

\(MFS\-21209\)

__RN13__

__Campo Valor Total__

Campo de preenchimento obrigatório\.

Deve ser um valor > zeros\.

Quando não preenchido ou = zeros, será gravada a seguinte mensagem de erro e o registro não será importado\.

*                             “O valor total da rubrica deve ser preenchido com um valor maior que zero”\.*

__RN14__

__Campo Indicador do Tipo de Processo __

Campo de preenchimento não obrigatório\.

Quando preenchido, o conteúdo deve ser:

“1”     \(Administrativo\)

“2”     \(Judicial\)

Quando o campo for preenchido com um conteúdo inválido, será gravada mensagem de erro padrão e o registro não será importado\.

__RN15__

__Campo Número do Processo __

Campo de preenchimento não obrigatório\.

Quando informado, o número do processo deve existir na *Tabela de Cadastro de Processos Administrativos / Judiciais \(SAFX2058\)*\.

Para pesquisar os processos na SAFX2058, considerar:

\-Grupo – Grupo obtido conforme regra padrão __\(\*\*\*\)__;

\-Tipo Processo – tipo de processo informado no campo 14;

\-Número Processo – número do processo informado no campo 15;

\-Validade Inicial – maior data existente, cujo mês/ano seja <= ao mês/ano de competência informados nos campos 03 e 04; 

\-Validade Final – a validade final deve estar nula, ou ser de um mês/ano > mês/ano de competência informados nos campos 03 e 04;

__*\(\*\*\*\)*__* O *__*Grupo*__* a ser utilizado será obtido a partir da regra básica, considerando o Grupo \(Relacionamento Tabelas x Grupos\) de maior data de validade, cujo mês/ano seja <= ao mês/ano de competência informado, e para o qual a tabela SAFX2058 esteja associada\.*

A verificação das datas de validade inicial e final do processo, tem por objetivo garantir que o processo é válido no mês de competência\.

Caso o processo não exista na SAFX2058, considerando as condições acima, será gravada mensagem de erro padrão e o registro não será importado\. Exemplo: “*O Processo não existe na Tabela de Cadastro de Processos Administrativos/Judiciais \(SAFX2058\), ou não é válido para o período de competência”*\.

__RN16__

__Campo Código do Indicativo da Suspensão__

Campo de preenchimento não obrigatório\.

Quando informado, o código do indicativo da suspensão deve existir na *Tabela de Informações de Suspensão de Exigibilidade de Tributos \(SAFX2059\)*\.

Para pesquisar os códigos indicativos da suspensão na SAFX2059, considerar:

\-Considerar apenas os registros que sejam “filhos” do processo informado \(campos 14 e 15\); 

\-Código do Indicativo da Suspensão de Exigibilidade de Tributos – código informado no campo 16;

\-Data da Decisão – deve ser uma data cujo mês e ano seja < = ao mês e ano de competência informado nos campos 03 e 04;

Caso o código do indicativo da suspensão não exista na SAFX2059, considerando as condições acima, será gravada mensagem de erro padrão e o registro não será importado\. Exemplo: “*O Código do Indicativo da Suspensão não existe na Tabela de Informações de Suspensão de Exigibilidade de Tributos \(SAFX2059\), ou não é válido para o período de competência”*\.


# MTZ-Job-Servidor-Importacao_SAFX247

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX247.docx
- **Modificado:** 2022-06-06
- **Tamanho:** 72 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX247

Tabela do Demonstrativo de Pagamento dos Autônomos

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS14409

Criação da SAFX247 

Criação da SAFX247 para a importação dos dados dos demonstrativos de pagamento dos trabalhadores autônomos, para a geração do eSocial\. 

29/11/2017

MFS19608

Lara Aline

Inclusão do campo CBO\.

11/07/2018

MFS22087

Lara Aline

Inclusão do campo Setor\.

07/11/2018

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX247__ 🡪 vide manual de layout

A SAFX247 foi criada na __MFS14409__, para a importação dos dados d__o__s__ __demonstrativos de pagamento dos trabalhadores autônomos\. Estas informações são utilizadas na geração dos eventos S\-1200 e S\-1210 do eSocial\.

__Campos que compõe a chave da tabela \(PK\):__

                     Código da Empresa \+ Código do Estabelecimento \+ Indicador Pessoa Fis/Jur \+ Código Pessoa Fis/Jur \+ 

                               Ano Competência \+ Mês Competência \+ Identificador do Demonstrativo de Pagamento

__RN01__

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

* \(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

__RN03__

__Campo Ano Competência __

Campo de preenchimento obrigatório\.

Quando não preenchido ou inválido \(= zeros\), será gravada mensagem de erro padrão e o registro não será importado\.

__RN04__

__Campo Mês Competência__

Campo de preenchimento obrigatório\.

Deve ser um mês válido\.

Quando não preenchido ou inválido, será gravada mensagem de erro padrão e o registro não será importado\.

__RN05__

__Campo Indicador Pessoa Fis/Jur __

Campo de preenchimento obrigatório\.

Valores válidos \(= indicadores da SAFX04\):

1 \(Fornecedor\)

2 \(Cliente\)

3 \(Estabelecimento\)

4 \(Transportadora\)

5 \(Cliente/Fornecedor/Transportadora\)

Quando não preenchido ou inválido \(= zeros\), será gravada mensagem de erro padrão e o registro não será importado\.

__RN06__

__Campo Código Pessoa Fis/Jur __

Campo de preenchimento obrigatório\.

A pessoa fis/jur informada \(indicador \+ código\) deve existir na Tabela de Cadastro de Pessoas Físicas/Jurídicas, considerando o Grupo \(Relacionamento Tabela x Grupo\) a ser utilizado __\(\*\*\*\)__, e deve ter uma data de validade inicial cujo mês/ano seja <= ao mês/ano de competência informado\.

Quando o código não for preenchido, ou a pessoa fis/jur não existir na SAFX04 \(considerando as condições acima\), será gravada mensagem de erro padrão e o registro não será importado\.

__\(\*\*\*\) __Para obter o Grupo a ser utilizado na pesquisa da SAFX04:

*O Grupo a ser utilizado será obtido a partir da regra básica, considerando o Grupo \(Relacionamento Tabelas x Grupos\) de maior data de validade, cujo mês/ano seja <= ao mês/ano de competência informado, e para o qual a tabela SAFX04 esteja associada\.*

__RN07__

__Campo Identificador do Demonstrativo de Pagamento __

Campo de preenchimento obrigatório\.

Quando não preenchido, será gravada mensagem de erro padrão e o registro não será importado\.

__RN08__

__Campo Indicador de Desconto da Contribuição Previdenciária __

Campo de preenchimento *não* obrigatório\.

Quando preenchido, o conteúdo será validado a partir dos seguintes valores:

1 \(Contribuição descontada pelo primeiro empregador\) 

2 \(Contribuição descontada por outras empresas sobre valor inferior ao limite máximo do salário de contribuição\)

3 \(Contribuição sobre o limite máximo de salário de contribuição já descontada em outras empresas\)

Caso inválido, será gravada mensagem de erro padrão e o registro não será importado\.

__RN09__

__Campo Indicador de Pagamento Total__

Campo de preenchimento obrigatório\.

Valores válidos: \[S\] ou \[N\]\.

Quando não preenchido ou inválido, será gravada mensagem de erro padrão e o registro não será importado\.

__RN10__

__Campo Data do Pagamento__

Quando preenchido, deve ser uma data válida\.

Este campo deve ser informado apenas quando o indicador de pagamento total \(campo 09\) for = \[S\], e nesse caso, a informação é obrigatória\.

Caso contrário, não deve ser preenchido\.

__Validação e mensagens de erro:__

1 \- Sobre a validade da data informada:

  

     Quando a data for preenchida, __e__ o indicador de pagamento total = \[S\] __e__ for uma data inválida:

      Nesse caso, será gravada a seguinte mensagem de erro, e o registro não será importado: “Data do Pagamento inválida” 

2 \- Sobre a obrigatoriedade / não obrigatoriedade do campo:

     Se \(indicador de pagamento total = \[S\] e a data não for preenchida\) __ou__ 

          \(indicador de pagamento total = \[N\] e a data for preenchida\):

         Nesse caso, será gravada a mensagem de erro abaixo, e o registro não será importado:

          “A Data de Pagamento é obrigatória para pagamento total\. Caso contrário, não deve ser informada”

__RN11__

__Campo Tipo do Pagamento __

Quando preenchido, o conteúdo deve ser um dos seguintes valores:

01 \(Pagamento de remuneração, conforme apurado no evento S\-1200\)

02 \(Pagamento de verbas rescisórias conforme apurado no evento S\-2299\)

03 \(Pagamento de verbas rescisórias conforme apurado no evento S\-2399\)

05 \(Pagamento de remuneração conforme apurado no evento S\-1202\)

06 \(Pagamento de Benefícios Previdenciários, conforme apurado no evento S\-1207\)

07 \(Recibo de férias\)

09 \(Pagamento relativo a competências anteriores ao início de obrigatoriedade do eSocial\)

Este campo deve ser informado apenas quando o indicador de pagamento total \(campo 09\) for = \[S\], e nesse caso, a informação é obrigatória\.

Caso contrário, não deve ser preenchido\.

__Validação e mensagens de erro:__

1 \- Sobre a validade do conteúdo informado:

  

     Quando o campo for preenchido, __e__ o indicador de pagamento total = \[S\] __e__ for um conteúdo inválido \(conforme valores acima\):

      Nesse caso, será gravada a seguinte mensagem de erro, e o registro não será importado: “Tipo do Pagamento inválido” 

2 \- Sobre a obrigatoriedade / não obrigatoriedade do campo:

     Se \(indicador de pagamento total = \[S\] e o campo não for preenchida\) __ou__ 

          \(indicador de pagamento total = \[N\] e o campo for preenchida\):

         Nesse caso, será gravada a mensagem de erro abaixo, e o registro não será importado:

          “O Tipo do Pagamento é obrigatório para pagamento total\. Caso contrário, não deve ser informado”

__RN12__

__Campo CBO __

Campo de preenchimento não obrigatório\.

Quando preenchido, o código CBO deve existir na Tabela Códigos CBO's – __\(SAFX2029\)__, considerando o Grupo \(Relacionamento Tabela x Grupo\) a ser utilizado __\(\*\*\*\)__, e deve ter uma data de validade inicial cujo mês/ano seja <= ao mês/ano de competência informado\.

Caso inválido, será gravada mensagem de erro padrão e o registro não será importado\.

__\(\*\*\*\) __Para obter o Grupo a ser utilizado na pesquisa da SAFX2029:

*O Grupo a ser utilizado será obtido a partir da regra básica, considerando o Grupo \(Relacionamento Tabelas x Grupos\) de maior data de validade, cujo mês/ano seja <= ao mês/ano de competência informado, e para o qual a tabela SAFX2029 esteja associada\.*

MFS19608

__RN13__

__Campo Setor__

Campo de preenchimento *não* obrigatório\.

Quando preenchido, o conteúdo informado deve ser um código existente na Tabela de Setor \(SAFX2037\), considerando o Grupo \(Relacionamento Tabela x Grupo\) a ser utilizado __\(\*\*\*\)__, e deve ter uma data de validade inicial cujo mês/ano seja <= ao mês/ano de competência informado\.

Caso inválido, será gravada mensagem de erro padrão e o registro não será importado\.

__\(\*\*\*\) __Para obter o Grupo a ser utilizado na pesquisa da SAFX2037:

*O Grupo a ser utilizado será obtido a partir da regra básica, considerando o Grupo \(Relacionamento Tabelas x Grupos\) de maior data de validade, cujo mês/ano seja <= ao mês/ano de competência informado, e para o qual a tabela SAFX2037 esteja associada\.*

MFS22087


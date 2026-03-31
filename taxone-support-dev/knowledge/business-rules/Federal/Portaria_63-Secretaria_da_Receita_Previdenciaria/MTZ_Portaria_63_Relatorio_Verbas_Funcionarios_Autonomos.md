# MTZ_Portaria_63_Relatorio_Verbas_Funcionarios_Autonomos

- **Fonte:** MTZ_Portaria_63_Relatorio_Verbas_Funcionarios_Autonomos.docx
- **Modificado:** 2020-10-05
- **Tamanho:** 71 KB

---

THOMSON REUTERS

Portaria 63

Relatório de Verbas por Funcionários e Autônomos

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4217

Criação do Relatório de Verbas por Funcionários e Autônomos\.

Definição de regras do Relatório de Verbas por Funcionários e Autônomos\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral de Seleção__

- __Origem das informações__: para geração deste relatório, serão consideradas informações das seguintes origens:

SAFX03 \- Arquivo de Fornecedores \(Contas a Pagar\)

SAFX04 \- Arquivo de Cadastro de Pessoas Físicas/Jurídicas

SAFX07 \- Arquivo de Notas Fiscais

SAFX15 \- Arquivo Cadastro de Empregados

SAFX21 \- Arquivo de Ficha Financeira do Empregado

SAFX2003 \- Tabela de Centro de Custo

SAFX2037 \- Tabela de Setor

SAFX2036 \- Tabela de Código de Função

- __Regra de seleção__: o objetivo deste relatório é demonstrar para cada funcionário ou autônomo que está vinculado ao estabelecimento que está emitindo o relatório quais são as verbas \(valores\) que estão relacionadas a eles\. Ele será gerado, quando na tela de geração do relatório for selecionada na opção “Gerar Relatório” o critério “Detalhado”\.

A seleção se divide em funcionários e autônomos e devem ser observados os parâmetros indicados na tela de geração do relatório\.

Para seleção de Funcionários:

Serão geradas informações de funcionários quando na tela de geração for indicado no campo “Tipo” a opção “Ambos” ou “Funcionário”\. Atendendo este critério, buscar registros da tabela SAFX21 \- Arquivo de Ficha Financeira do Empregado que tenham o mesmo \(ou mesmos\) empresa, estabelecimento \(ou estabelecimentos\) indicado na tela de geração, cuja combinação de 05 \- Mês de Competência e 04 \- Ano de Competência esteja enquadrada na data inicial e final informada pelo usuário\.

Se for indicado na tela a necessidade de “Refinar seleção das informações para emissão do relatório”, observar o conteúdo informado nos campos Setor \(Lotação\), Função ou Centro de Custo, pois o relatório deve ser gerado apenas para os critérios indicados, que pode ser um ou mais \(combinação de códigos\)\.

Para seleção de Autônomos:

Serão geradas informações de autônomos quando na tela de geração for indicado no campo “Tipo” a opção “Ambos” ou “Autônomos”\.

Para geração das informações de autônomos temos duas opções: geração para um único código de rubrica e geração para múltiplas rubricas \(rubrica é o código de verba\)\. O que distingue uma geração da outra é a parametrização realizada no módulo da Portaria 63 e o seu impacto no relatório se dá no detalhamento das verbas\. Se for um único código, teremos apenas uma linha de detalhamento de verba por competência\. Se forem múltiplas rubricas, teremos várias linhas por autônomos\.

A distinção para saber se deve ser gerada uma opção ou outra será: Se __não existir__ cadastro na tela de “Parâmetros p/ Autônomos – Múltiplas Rubricas” \(Módulo: Portaria 63 / Menu: Parâmetros\) para o Perfil indicado na tela de geração, será gerado no relatório o detalhamento da rubrica com o código indicado no cadastro do Perfil \(Módulo: Portaria 63 / Menu: Parâmetros\)\. Se __existir__ cadastro na tela de “Parâmetros p/ Autônomos – Múltiplas Rubricas” \(Módulo: Portaria 63 / Menu: Parâmetros\) para o Perfil indicado na tela de geração, será gerado no relatório o detalhamento de cada um dos códigos de rubrica existentes para o perfil\.

Na seleção das informações serão considerados os registros da SAFX07 para a empresa e estabelecimento \(ou estabelecimentos\) parametrizadas pelo usuário, cuja data fiscal da NF compreenda o período de geração, que seja um documento de entrada \(campo MOVTO\_E\_S diferente de 9\), com classificação referente a serviços \(campo COD\_CLASS\_DOC\_FIS igual a 2 ou 3\) e que tenha como Cadastro de Pessoa Física/Jurídica uma Pessoa Física com os campos CBO e Ocorrência do Trabalhador e Função preenchidos\.

- __Campos\-chave__: CPF, Data de nascimento, Registro Trabalhador, Data admissão, Lotação \(código/descrição\), Centro de custo \(código/descrição\), Código de Verba e Data da Competência\.
- __Ordenação__: Nome do Trabalhador e Tipo\.

OS4217

RN01

__Informações padrão do cabeçalho__

__Página__: número da página do relatório

__Título__: Relatório de Verbas por Funcionários e Autônomos

__Período__: período parametrizado para geração no formato DD/MM/AAAA a DD/MM/AAAA

__Data de Emissão__: data de emissão do relatório, seguido do horário no formato DD/MM/AAAA às HH:MM:SS hs

__Estabelecimento__: código e razão social do estabelecimento que está emitindo o relatório

OS4217

RN02

__Informações do Trabalhador – Coluna CPF__

- Para geração de Funcionários:

Campo 12 – CPF da tabela SAFX15\.

- Para geração de Autônomos:

Campo 06 – CPF\-CGC da tabela SAFX04\.

OS4217

RN03

__Informações do Trabalhador – Coluna Nome do Trabalhador__

- Para geração de Funcionários:

Campo 05 – Nome do Funcionário da tabela SAFX15\.

- Para geração de Autônomos:

Campo 05 – Razão Social da tabela SAFX04\.

OS4217

RN04

__Informações do Trabalhador – Coluna Data de Nascimento__

- Para geração de Funcionários:

Campo 23 – Data de Nascimento da tabela SAFX15\.

- Para geração de Autônomos:

Campo 45 – Data de nascimento da tabela SAFX04\.

OS4217

RN05

__Informações do Trabalhador – Coluna Número NIT__

- Para geração de Funcionários:

Campo 16 – Número do PIS/PASEP da tabela SAFX15\.

- Para geração de Autônomos:

Campo 16 – Número do PIS/PASEP da tabela SAFX04\.

OS4217

RN06

__Informações do Trabalhador – Coluna Data admissão__

- Para geração de Funcionários:

Campo 07 – Data de Admissão da tabela SAFX15\.

- Para geração de Autônomos:

Não gerar informação\.

OS4217

RN07

__Informações do Trabalhador – Coluna Data demissão__

- Para geração de Funcionários:

Campo 45 – Data de Desligamento da tabela SAFX15\.

- Para geração de Autônomos:

Não gerar informação\.

OS4217

RN08

__Informações do Trabalhador – Coluna Registro Trabalhador__

- Para geração de Funcionários:

Campo 33 – Número do Registro da tabela SAFX15\.

- Para geração de Autônomos:

Campo 02 – Código Pessoa Física/Jurídica da tabela SAFX04\.

OS4217

RN09

__Informações do Trabalhador – Coluna CBO__

- Para geração de Funcionários:

Campo 58 – CBO da tabela SAFX15\.

- Para geração de Autônomos:

Campo 34 – CBO da tabela SAFX04\.

OS4217

RN10

__Informações do Trabalhador – Coluna Descrição do Cargo__

- Para geração de Funcionários:

Campo 03 – Descrição da Função da tabela SAFX2036, considerando a descrição do Cadastro da Função do Código informado no campo 08 – Código da Função da tabela SAFX15\.

- Para geração de Autônomos:

Campo 03 – Descrição da Função da tabela SAFX2036, considerando a descrição do Cadastro da Função do Código informado no campo 48 – Função da tabela SAFX04\.

OS4217

RN11

__Informações do Trabalhador – Coluna Tipo__

- Para geração de Funcionários:

Para funcionários, fixar: “Funcionário”\.

- Para geração de Autônomos:

Para funcionários, fixar: “Autônomo”\.

OS4217

RN12

__Área Funcional – Coluna Lotação \(código/descrição\)__

- Para geração de Funcionários:

Campo 61 – Código do Setor da tabela SAFX15, seguido da descrição do Setor, informado no campo 03 – Descrição do Setor da tabela SAFX2037\.

- Para geração de Autônomos:

Campo 38 – Código do Setor da SAFX03\*, seguido da descrição do Setor, informado no campo 03 – Descrição do Setor da tabela SAFX2037\.

*\*Na tabela SAFX03 estão os lançamentos de Contas a Pagar\. Para cada NF \(SAF07\) considerada na geração desta informação no registro K250 haverá um registro correspondente na SAFX03 e lá existe o campo Código do Setor \(COD\_SETOR\) que é justamente o código da lotação e que permitirá o vinculo com a SAFX2037\.*

OS4217

RN13

__Área Funcional – Coluna Centro de Custo \(código/descrição\)__

- Para geração de Funcionários:

Campo 60 – Código do Centro de Custo da tabela SAFX15, seguido da descrição do Centro de Custo, informado no campo 03 – Descrição do Centro de Custo da tabela SAFX2003\.

- Para geração de Autônomos:

Quando a geração do autônomo for realizada com base na parametrização do Cadastro do Perfil \(Módulo: Portaria 63 / Menu: Parâmetros\), será demonstrada aqui a informação do campo 17 – Centro de Custo da SAFX03\*, seguido da descrição do Centro de Custo, informado no campo 03 – Descrição do Centro de Custo da tabela SAFX2003\.

Quando a geração do autônomo for realizada com base na parametrização de Parâmetros p/ Autônomos – Múltiplas Rubricas \(Módulo: Portaria 63 / Menu: Parâmetros\), será demonstrada aqui a informação do campo Centro de Custo da tela, seguido da descrição do Centro de Custo, informado no campo 03 – Descrição do Centro de Custo da tabela SAFX2003\.

*\*Na tabela SAFX03 estão os lançamentos de Contas a Pagar\. Para cada NF \(SAF07\) considerada na geração desta informação no registro K250 haverá um registro correspondente na SAFX03 e lá existe o campo Código do Centro de Custo \(CENTRO\_CUSTO\) que é justamente o código do centro de custo que permitirá o vinculo com a SAFX2003\.*

OS4217

RN14

__Informações da Folha de Pagamento – Coluna Verba__

Esta coluna será quebrada em duas outras sub\-colunas: Código e Descrição\.

- Para geração de Funcionários:

Sub\-coluna Código: Campo 07 – Código da Verba da tabela SAFX21\.

Sub\-coluna Descrição: Campo 04 – Descrição da Verba da tabela SAFX2023, considerando o código da verba recuperado da tabela SAFX15\.

- Para geração de Autônomos:

Sub\-coluna Código: Quando a geração do autônomo for realizada com base na parametrização do Cadastro do Perfil \(Módulo: Portaria 63 / Menu: Parâmetros\), será demonstrada aqui a informação do Código da Verba\.

Quando a geração do autônomo for realizada com base na parametrização de Parâmetros p/ Autônomos – Múltiplas Rubricas \(Módulo: Portaria 63 / Menu: Parâmetros\), será demonstrada aqui a informação do Código da Verba\.

Sub\-coluna Descrição: para ambas as possibilidades, considerar o campo 04 – Descrição da Verba da tabela SAFX2023, considerando o código da verba recuperado da parametrização do Perfil ou Parâmetros p/ Autônomos – Múltiplas Rubricas\.

OS4217

RN15

__Informações da Folha de Pagamento – Coluna Data da Competência__

- Para geração de Funcionários:

Será gerado o último dia do mês seguido dos campos 05 \- Mês de Competência e 04 \- Ano de Competência da tabela SAFX21\.

- Para geração de Autônomos:

Será gerado o último dia do mês acompanhado do Mês e Ano da Data Fiscal informada na tabela SAFX07\.

OS4217

RN16

__Informações da Folha de Pagamento – Coluna Valor R$__

- Para geração de Funcionários:

Campo 09 – Valor da Verba da tabela SAFX21\. Se o conteúdo da coluna “Ind\. Provento \(P\) / Desconto \(D\) / Outro \(O\)” for igual a “D”, demonstrar o valor com sinal negativo\.

- Para geração de Autônomos:

Quando a geração do autônomo for realizada com base na parametrização do Cadastro do Perfil \(Módulo: Portaria 63 / Menu: Parâmetros\), será demonstrada aqui a informação do campo 23 – Valor Total do Documento Fiscal da tabela SAFX07\.

Quando a geração do autônomo for realizada com base na parametrização de Parâmetros p/ Autônomos – Múltiplas Rubricas \(Módulo: Portaria 63 / Menu: Parâmetros\), o sistema deverá recuperar a informação do campo “Campo a ser detalhado”, buscando o conteúdo informado na tabela SAFX07\.

OS4217

RN17

__Informações da Folha de Pagamento – Coluna Ind\. Provento \(P\) / Desconto \(D\) / Outro \(O\)__

- Tanto para geração de Funcionários quanto Autônomo:

Será gerado com base no campo 03 – Indicador de Verba da tabela SAFX2023, considerando o código da verba demonstrado na linha e realizando as seguintes conversões:

__Indicador de Verba__

__Gera no Relatório__

1 \- Verba Provento

P

2 \- Verba Desconto

D

3 \- Base de Cálculo IRRF

O

4 \- Verba Total Provento

P

5 \- Verba Total de Desconto

D

6 \- Verba Total Líquido

O

7 \- Outros

O

8 \- Base de Cálculo do INSS

O

 

OS4217

RN18

__Informações da Folha de Pagamento – Coluna Incide IRRF__

- Para geração de Funcionários:

Campo 07 – Tributação de IR da tabela SAFX2023, considerando o código de verba demonstrado na linha\. Se o conteúdo do campo for igual a “S”, gerar “Sim”\. Se for diferente de “S”, gerar “Não”\.

- Para geração de Autônomos:

Campo 07 – Tributação de IR da tabela SAFX2023, considerando o código de verba demonstrado na linha\. Se o conteúdo do campo for igual a “S”, gerar “Sim”\. Se for diferente de “S”, gerar “Não”\.

OS4217

RN19

__Informações da Folha de Pagamento – Coluna Incide INSS__

- Para geração de Funcionários:

Campo 12 – Indicador de Incidência para o INSS da tabela SAFX2023, considerando o código de verba demonstrado na linha\. Se o conteúdo do campo for igual a “S”, gerar “Sim”\. Se for diferente de “S”, gerar “Não”\.

- Para geração de Autônomos:

Campo 12 – Indicador de Incidência para o INSS da tabela SAFX2023, considerando o código de verba demonstrado na linha\. Se o conteúdo do campo for igual a “S”, gerar “Sim”\. Se for diferente de “S”, gerar “Não”\.

OS4217

RN20

__Informações da Folha de Pagamento – Linha Total__

Nesta linha serão somados os valores lançados na coluna “Valor R$”, desconsiderando os valores das linhas que tenham o “Ind\. Provento \(P\) / Desconto \(D\) / Outro \(O\)” igual a “O”\. Observar no cálculo que os valores relativos a descontos \(coluna “Ind\. Provento \(P\) / Desconto \(D\) / Outro \(O\)” igual a “D”\) são gerados com sinal negativo e este sinal tem relevância para esta totalização\.

OS4217

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


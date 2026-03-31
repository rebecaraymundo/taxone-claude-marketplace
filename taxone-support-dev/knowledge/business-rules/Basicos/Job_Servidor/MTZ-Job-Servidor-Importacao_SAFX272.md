# MTZ-Job-Servidor-Importacao_SAFX272

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX272.docx
- **Modificado:** 2020-08-27
- **Tamanho:** 76 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX272

Tabela de Parametrização do Produto para Informação Adicional do E115 do Sped Fiscal 

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__MFS24917__

Liliane Assaf

Criação de nova tabela SAFX para carga da parametrização do Produto para Informação Adicional\. 

O objetivo é relacionar os produtos que serão considerados na Pré\-Geração do Registro E115 do Sped Fiscal para Unidades da Federação diferentes do Rio Grande do Sul\. 

__MFS30407__

Andréa Rocha

Retirar a validação do campo estabelecimento para o estado igual a RS\.

__MFS32389__

Vânia Mattos

Alteração da X272\_PAR\_PROD\_E115 para inclusão do COD\_INF\_ADIC na PK\. Este alteração permitirá que o mesmo produto seja parametrizado para diferentes COD\_INF\_ADIC\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

Estrutura da tabela SAFX272 🡪 vide manual de layout

Tabela de Destino: A SAFX272 alimenta a tabela definitiva X272\_PAR\_PROD\_E115

Campos que compõe a chave da tabela:

__MFS32389:__ A chave da tabela foi alterada para permitir que o mesmo produto, seja parametrizado para diferentes COD\_INF\_ADIC\.

__      Código da Empresa \+ Código do Estabelecimento \+ Produto \+ Inicio Validade \+  Código da Informação Adicional__

A manutenção desta tabela é feita no Módulo EFD – Escrituração Fiscal Digital, menu Parâmetros 🡪 Registro E115/1925 🡪 Registro E115 \(Geral\) 🡪 Produtos 

Sobre as mensagens de erro:

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

MFS24917

MFS32389

__RN01__

__Campo 01 \-  Código da Empresa__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação da Empresa serão desconsiderados\)*

MFS24917

__RN02__

__Campo 02 \- Código do Estabelecimento__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento serão desconsiderados\)*

__\[MFS30407\]__

Crítica da UF do Estabelecimento

Esta parametrização não é válida para estabelecimentos do Rio Grande do Sul\.

  
Caso a UF do Estabelecimento seja igual a “RS”, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

*“A parametrização de Produto por Informações Adicionas E115 não é válida para Estabelecimentos do Rio Grande do Sul”*

MFS24917

MFS30407

__RN03__

__Campo 03 \- Indicador de Produto__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, ou quando for um indicador inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“Indicador do produto invalido ou nao preenchido”*

MFS24917

__RN04__

__Campo 04 – Código do Produto __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“O codigo do produto e de preenchimento obrigatorio e nao foi informado”*

Crítica da existência do produto na SAFX2013:

O produto informado será validado na Tabela de Produtos\. Como a X2013 é uma tabela que trabalha com GRUPO, será necessário obter o Grupo de Relacionamento a ser utilizado nesta validação\. A informação do Grupo será obtida a partir do Estabelecimento \(campo 02\), e considerando a maior data de validade que seja <= a Início Validade \(campo 05\) do registro foco da importação\. 

A busca na tabela de produtos irá considerar o Indicador de Produto \(campo 03\), o Código do Produto \(campo 04\) e o Grupo obtido conforme a regra descrita acima\. Caso o produto não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem: 

*“Indicador/Codigo do produto não cadastrado”*

MFS24917

__RN05__

__Campo 05 \- Início Validade __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “O campo Data Início Validade é de preenchimento obrigatório e não foi informado”*

Caso o campo esteja preenchido, se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “O campo Data Início Validade é invalido”*

MFS24917

__RN06__

__Campo 06 \- Fim Validade __

Campo de preenchimento não obrigatório\.

Caso o campo esteja preenchido, se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “O campo Data Fim Validade é invalido”*

Caso o campo esteja preenchido, se for uma data menor que a Data Início Validade, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“O campo Data Fim Validade, quando preenchido, deve ser maior ou igual a Data Início Validade”*

__Tratamento para não permitir Intervalos Intercalados de Datas__:

Vamos adotar tratamentos para evitar que um produto para uma determinada empresa, estabelecimento e código de informação adicional tenha parametrizações com intervalos de datas inicial e final que se intercalem\. Ou seja, não podemos permitir que uma parametrização do produto tenha Data Início ou Fim de Validade entre as datas Início e Fim Validade da parametrização já existente na base\.

__MFS32389:__ A chave da tabela foi alterada para inclusão da coluna COD\_INF\_ADIC, para permitir que o mesmo produto, seja parametrizado para diferentes COD\_INF\_ADIC\. Desta forma, este campo deve ser tratado junto com os demais campos chave, para as críticas referentes às datas de vigência da parametrização\.

__Exemplo1: Produto sem Data Fim de Validade__

Dado o produto 1\-A00 da Empresa ‘076’, Estabelecimento ‘001’ e Cód\.Inf\.Adic\. = “PR820043”\.

Parametrização já existente na base registrado com Início Validade 01/01/2018 e Fim Validade nulo

Registros a serem importados via SAFX272:

__Início Validade__

__Fim Validade__

__Resultado da Importação__

01/01/2017

31/12/2017

Ok importado com sucesso

01/01/2017

01/01/2018

Erro na importação\. Data Fim intercala o registro já existe na base\. Registro não importado

01/01/2017

Erro na importação\. Data Fim nula, intercalando com o registro já existe na base\. Registro não importado

02/01/2018

Erro na importação, Data Fim do registro existente na base é nula\. Registro não importado

__Exemplo2: Produto com Data Fim de Validade__

Dado o produto 1\-A00 da Empresa ‘076’, Estabelecimento ‘001’ e Cód\.Inf\.Adic\. = “PR820043”\.

Parametrização já existente na base registrado com Início Validade 01/01/2018 e Fim Validade 31/01/2018

Registros a serem importados via SAFX272:

__Início Validade__

__Fim Validade__

__Resultado da Importação__

01/01/2017

31/12/2017

Ok importado com sucesso

01/01/2017

01/01/2018

Erro na importação\. Data Fim intercala com o registro já existe na base\. Registro não importado

01/01/2017

Erro na importação\. Data Fim nula, intercalando com o registro já existe na base\. Registro não importado

02/01/2018

Erro na importação\. Data Início intercala com o registro já existe na base\.

01/02/2018

Ok importado com sucesso

<a id="_Hlk2188990"></a>

__Situações tratadas na importação__:

1. Dada a Empresa, Estabelecimento, Produto e Cód\.Inf\.Adic\. da parametrização que está sendo importada, buscar na base a parametrização de mesma Empresa, Estabelecimento, Produto e Cód\.Inf\.Adic\., com Data Início Validade imediatamente posterior à Data Início Validade do registro que está sendo importado\.

Caso o registro seja encontrado, comparar a Data Fim de Validade do registro que está sendo importado com a Data Início Validade do registro encontrado\.

Se Data Fim de Validade do registro que está sendo importado >= Data Início Validade do registro encontrado ou

     Data Fim de Validade do registro que está sendo importado for nula então:

O registro não será importado e no log de erros será gravada a seguinte mensagem:

*Já existe parametrização do Produto vigente nas datas Início e/ou Fim de Validade da parametrização informada\.*

1. Dada a Empresa, Estabelecimento, Produto e Cód\.Inf\.Adic\. da parametrização que está sendo importada, buscar na base a parametrização de mesma Empresa, Estabelecimento, Produto e Cód\.Inf\.Adic\., com Data Início Validade imediatamente anterior à Data Início Validade do registro que está sendo importado\.

Caso o registro seja encontrado, comparar a Data Fim de Validade do registro encontrado com a Data Início Validade do registro que está sendo importado\.

Se Data Fim de Validade do registro encontrado >= Data Início Validade do registro que está sendo importado ou

     Data Fim de Validade do registro encontrado for nula então:

O registro não será importado e no log de erros será gravada a seguinte mensagem:

*Já existe parametrização do Produto vigente nas datas Início e/ou Fim de Validade da parametrização informada\.*

Considerando a chave da tabela \(empresa, estabelecimento, produto, Início Validade e Cód\.Inf\.Adic\.\), uma inclusão tratar as situações __\(a\)__ e __\(b\)__\. Na atualização do registro basta tratar a situação __\(a\)__\.

MFS24917

__RN07__

__Campo 07 \- Código da Informação Adicional__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“O codigo da Informação Adicional e de preenchimento obrigatorio e nao foi informado”*

__Crítica da existência na Tabela de Origem:__

Verificar se o código informado se encontra cadastrado na Tabela de Informações Adicionais da Apuração para a UF do estabelecimento \(campo 02\) da importação\.

Localização do Cadastro:

Módulo: EFD\-Escrituração Fiscal Digital, 

Menu:    Parâmetros >> Registro E115/1925 >> Informações Adicionais da Apuração \(Registro E115/1925\)\.

Caso não esteja cadastrado, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“Código da Informação Adicional não cadastrado para a UF do Estabelecimento\.”*

*Solução: Cadastrar código no módulo EFD, menu Informações Adicionais da Apuração \(Registro E115/1925\)\.”*

MFS24917

__RN08__

__Campo 08 – Descrição Complementar do E115 __

Campo de preenchimento não obrigatório\.

MFS24917

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


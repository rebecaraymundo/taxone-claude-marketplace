# MTZ-Job-Servidor-Importacao_SAFX278

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX278.docx
- **Modificado:** 2022-12-21
- **Tamanho:** 120 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX

__Correlação entre Códigos de Itens Comercializados __

__           __

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

	

\- Importação à Execução

\- Importação Batch à Programação à Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS97666

Aline Melo

Inclusão da nova SAFX278 no processo do Job Servidor\. 

23/11/2022

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX278__ à vide manual de layout

A manutenção desta tabela é feita na tela de Parâmetros > Registro 0221 > Produtos, no módulo Módulo EFD \- Escrituração Fiscal Digital: 

As informações importadas devem ser gravadas nas seguintes tabelas:

- __EFD\_PAR\_PROD\_0221 __\(tabela que grava o produto principal\)

Campos que compõe a chave da tabela: COD\_EMPRESA \+ COD\_ESTAB \+ GRUPO \+ IND\_PRODUTO \+ COD\_PRODUTO \+ DATA\_INI 

- __EFD\_PAR\_PROD\_0221\_ASS \(__tabela que grava os produtos associados\)

Campos que compõe a chave da tabela: COD\_EMPRESA \+ COD\_ESTAB \+ GRUPO \+ IND\_PRODUTO \+ COD\_PRODUTO \+ DATA\_INI \+ IND\_PRODUTO\_ASS \+ COD\_PRODUTO\_ASS

__Gravação dos Dados: __

 

Segue a descrição do conteúdo a ser gravado em cada coluna das tabelas definitivas, e na sequencia, as críticas especificas de cada campo da tabela SAFX \(ver RN01 à RN10\): 

__EFD\_PAR\_PROD\_0221 __

__ __

__EFD\_PAR\_PROD\_0221\_ASS __

__ __

__ __

__              Conteúdo a ser gravado \(campos da SAFX278\) __

COD\_EMPRESA 

COD\_EMPRESA 

01\-Código da Empresa  

COD\_ESTAB 

COD\_ESTAB 

02\-Código do Estabelecimento 

IND\_PRODUTO 

IND\_PRODUTO 

03\-Indicador de Produto 

COD\_PRODUTO 

COD\_PRODUTO 

04\-Código do Produto 

DATA\_INI 

DATA\_INI 

05\-Data Inicial 

DATA\_FIM 

\-\-\-\-\-\-\-\- 

06\-Data Final 

\-\-\-\-\-\-\-\- 

\-\-\-\-\-\-\-\- 

Se campo “11\-Tipo de Registro” = 1 

     Os dados serão gravados na EFD\_PAR\_PROD\_C176 

Senão 

     Os dados serão gravados na EFD\_PAR\_PROD\_C176\_ASS 

\-\-\-\-\-\-\-\- 

IND\_PRODUTO\_ASS 

08\-Indicador de Produto 

\-\-\-\-\-\-\-\- 

COD\_PRODUTO\_ASS 

09\-Código do Produto 

QTDE\_CONTIDA

10\-Quantidade

Sobre as mensagens de erro: 

 

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.    

__Processo de Importação Automática de SAFX__

Esse processo ocorre somente no TAX ONE e o mesmo já está habilitado para contemplar as novas SAFX’s\.

Para verificar as adequações necessárias, utilizar como exemplo, a SAFX04\.

MFS97666

__RN01__

__Código da Empresa__

Campo COD\_EMPRESA

Campo de preenchimento __*obrigatório\.*__

*\(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

MFS97666

__RN02__

__Código do Estabelecimento__

Campo COD\_ESTAB

Campo de preenchimento __*obrigatório\.*__

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

MFS97666

__RN03 __

__Campo Indicador de Produto__

Campo IND\_PRODUTO

Campo de preenchimento __*obrigatório*__\. 

 

Quando não preenchido, ou quando for um indicador inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

*“Indicador do produto invalido ou nao preenchido”* 

MFS97666

__RN04__

__Código do Produto__

Campo COD\_PRODUTO

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido:

 “*O código do produto é de preenchimento obrigatório e não foi informado*\.”

Crítica da existência do produto na SAFX2013: 

 

O produto informado será validado na Tabela de Produtos\. Como a X2013 é uma tabela que trabalha com GRUPO, será necessário obter o Grupo de Relacionamento a ser utilizado nesta validação\. A informação do Grupo será obtida a partir do Estabelecimento \(campo 02\), e considerando a maior data de validade que seja <= a Início Validade \(campo 05\) do registro foco da importação\.  

 

A busca na tabela de produtos irá considerar o Indicador de Produto \(campo 03\), o Código do Produto \(campo 04\) e o Grupo obtido conforme a regra descrita acima\. Caso o produto não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem:  

 

*“Indicador/Codigo do produto não cadastrado”* 

MFS97666

__RN05__

__Campo \- Início Validade __ 

Campo DATA\_INI 

Campo de preenchimento __*obrigatório*__\. 

 

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

*                                                        “O campo Data Início Validade é de preenchimento obrigatório e não foi informado”* 

 

Caso o campo esteja preenchido, se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

*                                                        “O campo Data Início Validade é invalido”* 

MFS97666

__RN06__

__Campo Fim Validade__

Campo DATA\_FIM

Campo de preenchimento não obrigatório\. 

 

Quando o campo 11\-tipo de registro for igual a “2”, este campo não deve ser preenchido\. 

 

Caso o campo esteja preenchido, se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

*                                                        “O campo Data Fim Validade é invalido”* 

Caso o campo esteja preenchido, se for uma data menor que a Data Início Validade, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

*“O campo Data Fim Validade, quando preenchido, deve ser maior ou igual a Data Início Validade”* 

__Tratamento para não permitir Intervalos Intercalados de Datas__: 

Vamos adotar tratamentos para evitar que um produto para uma determinada empresa e estabelecimento tenha parametrizações com intervalos de datas inicial e final que se intercalem\. Ou seja, não podemos permitir que uma parametrização do produto tenha Data Início ou Fim de Validade entre as datas Início e Fim Validade da parametrização já existente na base\. 

 

__Exemplo1: Produto sem Data Fim de Validade__ 

Dado o produto 1\-A00 da Empresa ‘076’ e Estabelecimento ‘001’\. 

Parametrização já existente na base registrado com Início Validade 01/01/2018 e Fim Validade nulo 

 

Registros a serem importados via SAFX306: 

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

Dado o produto 1\-A00 da Empresa ‘076’ e Estabelecimento ‘001’\. 

Parametrização já existente na base registrado com Início Validade 01/01/2018 e Fim Validade 31/01/2018 

 

Registros a serem importados via SAFX306: 

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

 

 

__Situações tratadas na importação__: 

1. Dada a Empresa, Estabelecimento, Produto e Alíquota Interna da parametrização que está sendo importada, buscar na base a parametrização de mesma Empresa, Estabelecimento, Produto e Alíquota Interna com Data Início Validade imediatamente posterior à Data Início Validade do registro que está sendo importado\. 

Caso o registro seja encontrado, comparar a Data Fim de Validade do registro que está sendo importado com a Data Início Validade do registro encontrado\. 

Se Data Fim de Validade do registro que está sendo importado >= Data Início Validade do registro encontrado ou 

     Data Fim de Validade do registro que está sendo importado for nula então: 

O registro não será importado e no log de erros será gravada a seguinte mensagem: 

*Foi encontrada parametrizacao para o produto, com datas de vigencia em conflito com as datas de vigencia informadas\.* 

 

1. Dada a Empresa, Estabelecimento, Produto e Alíquota Interna da parametrização que está sendo importada, buscar na base a parametrização de mesma Empresa, Estabelecimento e Produto com Data Início Validade imediatamente anterior à Data Início Validade do registro que está sendo importado\. 

Caso o registro seja encontrado, comparar a Data Fim de Validade do registro encontrado com a Data Início Validade do registro que está sendo importado\. 

Se Data Fim de Validade do registro encontrado >= Data Início Validade do registro que está sendo importado ou 

     Data Fim de Validade do registro encontrado for nula então: 

O registro não será importado e no log de erros será gravada a seguinte mensagem: 

*Foi encontrada parametrizacao para o produto, com datas de vigencia em conflito com as datas de vigencia informadas\.* 

MFS97666

__RN08__

__Campo Indicador de Produto Associado __

Campo IND\_PRODUTO\_ASS

Informar o Indicador de Produto, de acordo com: 

1 \- Produto Acabado; 

2 \- Insumos; 

3 \- Embalagem; 

4 \- Consumo; 

5 \- Outros; 

6 \- Em Elaboração; 

7 \- Intermediário; 

8 \- Miscelâneas\. 

  

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

 

*“O indicador do produto associado e de preenchimento obrigatorio” *

 

Quando for preenchido, o seu conteúdo deve ser validado\.  Quando for um indicador inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

*“Indicador do produto invalido ou nao preenchido” *

MFS97666

__RN09__

__Código do Produto Associado__

Campo COD\_PRODUTO\_ASS

Campo de preenchimento obrigatório\.

 

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

 

*“O codigo do produto associado e de preenchimento obrigatorio” *

 

Crítica da existência do produto na SAFX2013: 

 

O produto informado será validado na Tabela de Produtos\. Como a X2013 é uma tabela que trabalha com GRUPO, será necessário obter o Grupo de Relacionamento a ser utilizado nesta validação\. A informação do Grupo será obtida a partir do Estabelecimento \(campo 02\), e considerando a maior data de validade que seja <= a Início Validade \(campo 05\) do registro foco da importação\.  

 

A busca na tabela de produtos irá considerar o Indicador de Produto \(campo 12\), o Código do Produto \(campo 13\) e o Grupo obtido conforme a regra descrita acima\. Caso o produto não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem:  

 

*“Indicador/Codigo do produto não cadastrado” *

MFS97666

__RN010__

__Quantidade __

Campo QTD\_CONTIDA 

Campo de preenchimento __*obrigatório\.*__

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido:

“*Quantidade deve ser maior que zero*\.”

Se preenchido com valor <> ‘1’ E COD\_PRODUTO = COD\_PRODUTO\_ASS, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido:

*“Para codigo de produto igual ao código de produto associado a quantidade informada deve ser igual a ‘1’\.”*

MFS97666

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


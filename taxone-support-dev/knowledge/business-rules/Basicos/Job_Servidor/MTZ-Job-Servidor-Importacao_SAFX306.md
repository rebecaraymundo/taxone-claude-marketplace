# MTZ-Job-Servidor-Importacao_SAFX306

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX306.docx
- **Modificado:** 2021-03-11
- **Tamanho:** 84 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX306

Tabela de Parametrização por Produto – Registro C176 do Sped Fiscal 

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS36503

Andréa Rocha

Criação de nova tabela SAFX para carga da parametrização por Produto do Registro C176 do SPED\-EFD, também usada no módulo do Ressarcimento de ICMS\-ST – PR\.

MFS43977

Andréa Rocha

Inclusão do campo % de Redução de BC\.

MFS47333

Andréa Rocha

Inclusão de 3 campos novos para tratar a nota tabela de Produtos Associados e alterar a regra de 3 campos também para tratar a mesma situação\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

Estrutura da tabela SAFX306 🡪 vide manual de layout

__\[MFS47333\] Inclusão dos Produtos Associados__

__A tabela SAFX306 irá conter informações para a parametrização do produto principal e para a parametrização dos produtos associados\.  O campo que irá definir para que tabela os dados serão carregados será o campo 11\-Tipo de Registro\.__

Campos que compõe a chave da tabela EFD\_PAR\_PROD\_C176:

__   Código da Empresa \+ Código do Estabelecimento \+ Produto \+ Alíquota Interna \+  Inicio Validade__

Campos que compõe a chave da tabela de EFD\_PAR\_PROD\_C176\_ASS:

__   Código da Empresa \+ Código do Estabelecimento \+ Produto \+ Alíquota Interna \+  Inicio Validade \+ Produto Associado__

A manutenção destas tabelas são feitas no Módulo EFD – Escrituração Fiscal Digital, menu Parâmetros 🡪 Produtos

__\[MFS47333\] Inclusão dos Produtos Associados__

Tabelas de Destino:

Se o Tipo de Registro \(campo 11\) for igual a 1 🡪 os dados serão gravados na tabela EFD\_PAR\_PROD\_C176

Se o Tipo de Registro \(campo 11\) for igual a 2 🡪 os dados serão gravados na tabela EFD\_PAR\_PROD\_C176\_ASS

__Gravação dos Dados__:

Segue a descrição do conteúdo a ser gravado em cada coluna das tabelas definitivas, e na sequencia, as críticas especificas de cada campo da tabela SAFX \(ver __RN01__ à __RN13__\):

EFD\_PAR\_PROD\_C176

EFD\_PAR\_PROD\_C176\_ASS

__              Conteúdo a ser gravado:__

__               \(campos da SAFX306\)__

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

VLR\_ALIQ\_INT

VLR\_ALIQ\_INT

05\-Alíquota Interna dos Produtos

DATA\_INI

DATA\_INI

06\-Data Inicial

DATA\_FIM

\-\-\-\-\-\-\-\-

07\-Data Final

IND\_FCP

\-\-\-\-\-\-\-\-

08\-Sujeito ao FCP

ALIQ\_FCP

\-\-\-\-\-\-\-\-

09\-Alíquota FCP

PRC\_REDUCAO\_BC

\-\-\-\-\-\-\-\-

10\-% de Redução de BC

\-\-\-\-\-\-\-\-

\-\-\-\-\-\-\-\-

Se campo “11\-Tipo de Registro” = 1

     Os dados serão gravados na EFD\_PAR\_PROD\_C176

Senão

     Os dados serão gravados na EFD\_PAR\_PROD\_C176\_ASS

\-\-\-\-\-\-\-\-

IND\_PRODUTO\_ASS

11\-Indicador de Produto

\-\-\-\-\-\-\-\-

COD\_PRODUTO\_ASS

12\-Código do Produto

Sobre as mensagens de erro:

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

MFS36503

MFS47333

__RN01__

__Campo 01 \-  Código da Empresa__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação da Empresa serão desconsiderados\)*

MFS36503

__RN02__

__Campo 02 \- Código do Estabelecimento__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento serão desconsiderados\)*

MFS36503

__RN03__

__Campo 03 \- Indicador de Produto__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, ou quando for um indicador inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“Indicador do produto invalido ou nao preenchido”*

MFS36503

__RN04__

__Campo 04 – Código do Produto __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“O codigo do produto e de preenchimento obrigatorio e nao foi informado”*

Crítica da existência do produto na SAFX2013:

O produto informado será validado na Tabela de Produtos\. Como a X2013 é uma tabela que trabalha com GRUPO, será necessário obter o Grupo de Relacionamento a ser utilizado nesta validação\. A informação do Grupo será obtida a partir do Estabelecimento \(campo 02\), e considerando a maior data de validade que seja <= a Início Validade \(campo 05\) do registro foco da importação\. 

A busca na tabela de produtos irá considerar o Indicador de Produto \(campo 03\), o Código do Produto \(campo 04\) e o Grupo obtido conforme a regra descrita acima\. Caso o produto não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem: 

*“Indicador/Codigo do produto não cadastrado”*

MFS36503

__RN05__

__Campo 05 – Alíquota Interna do Produto__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, ou quando for um valor inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“Alíquota Interna do Produto invalida ou nao preenchida”*

MFS36503

__RN06__

__Campo 06 \- Início Validade __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “O campo Data Início Validade é de preenchimento obrigatório e não foi informado”*

Caso o campo esteja preenchido, se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “O campo Data Início Validade é invalido”*

MFS36503

__RN07__

__Campo 07 \- Fim Validade __

Campo de preenchimento não obrigatório\.

Quando o campo 11\-tipo de registro for igual a “2”, este campo *não* deve ser preenchido\.

Caso o campo esteja preenchido, se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “O campo Data Fim Validade é invalido”*

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

<a id="_Hlk2188990"></a>

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

MFS36503

MFS47333

__RN08__

__Campo 08 \- Sujeito ao FCP__

Campo de preenchimento não obrigatório\.

Quando o campo 11\-tipo de registro for igual a “2”, este campo *não* deve ser preenchido\.

Quando preenchido, o registro deve ser preenchido com “S” ou “N”\. Caso não esteja não preenchido com “S” ou “N”, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“O campo Sujeito ao FCP deve ser preenchido com “S” ou “N”\.”*

MFS36503

MFS47333

__RN09__

__Campo 09 – Alíquota FCP__

Campo de preenchimento não obrigatório\.

Quando o campo 11\-tipo de registro for igual a “2”, este campo *não* deve ser preenchido\.

Este campo só deve ser preenchido se o campo 08 \- Sujeito ao FCP estiver preenchido com “S”\.  Caso não esteja preenchido com “S” e o campo Alíquota estiver preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“O campo Alíquota FCP somente deve ser preenchido quando o campo Sujeito ao FCP estiver preenchido com “S”\.”*

MFS36503

MFS47333

__RN10__

__Campo 10 – % de Redução de BC__

Campo de preenchimento não obrigatório\.

Quando o campo 11\-tipo de registro for igual a “2”, este campo *não* deve ser preenchido\.

MFS43977

MFS47333

__RN11__

__Campo 11 – Tipo de Registro__

Informar o Tipo de Registro, de acordo com:

1 \- Registro Mestre

2 \- Produtos Associados

Campo de preenchimento obrigatório\.

Quando não preenchido, ou quando for um tipo inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“O campo Tipo de Registro deve ser preenchido com “1” ou “2”\.”*

MFS47333

__RN12__

__Campo 12 \- Indicador de Produto Associado__

Informar o Indicador de Produto, de acordo com:

1 \- Produto Acabado;

2 \- Insumos;

3 \- Embalagem;

4 \- Consumo;

5 \- Outros;

6 \- Em Elaboração;

7 \- Intermediário;

8 \- Miscelâneas\.

Campo de preenchimento obrigatório quando o campo 11\-Tipo de Registro for igual a “2”\.

Quando o campo 11\-tipo de registro for igual a “1”, este campo *não* deve ser preenchido\.

Quando não preenchido e o campo 11\-tipo de registro for igual a “2”, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“O indicador do produto associado e de preenchimento obrigatorio e nao foi informado para o tipo de registro igual a 2”*

Quando for preenchido, o seu conteúdo deve ser validado\.  Quando for um indicador inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“Indicador do produto invalido ou nao preenchido”*

MFS47333

__RN13__

__Campo 13 – Código do Produto Associado __

Campo de preenchimento obrigatório quando o campo 11\-Tipo de Registro for igual a “2”\.

Quando não preenchido e o campo 11\-tipo de registro for igual a “2”, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“O codigo do produto associado e de preenchimento obrigatorio e nao foi informado para o tipo de registro igual a 2”*

Quando o campo 11\-tipo de registro for igual a “1”, este campo *não* deve ser preenchido\.

Crítica da existência do produto na SAFX2013:

O produto informado será validado na Tabela de Produtos\. Como a X2013 é uma tabela que trabalha com GRUPO, será necessário obter o Grupo de Relacionamento a ser utilizado nesta validação\. A informação do Grupo será obtida a partir do Estabelecimento \(campo 02\), e considerando a maior data de validade que seja <= a Início Validade \(campo 05\) do registro foco da importação\. 

A busca na tabela de produtos irá considerar o Indicador de Produto \(campo 12\), o Código do Produto \(campo 13\) e o Grupo obtido conforme a regra descrita acima\. Caso o produto não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem: 

*“Indicador/Codigo do produto não cadastrado”*

 MFS47333

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


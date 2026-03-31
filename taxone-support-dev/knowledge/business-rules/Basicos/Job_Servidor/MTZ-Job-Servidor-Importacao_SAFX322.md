# MTZ-Job-Servidor-Importacao_SAFX322

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX322.docx
- **Modificado:** 2023-03-28
- **Tamanho:** 78 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX322

Tabela de Parametrização do Produto x Produto ANP

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS433027

Andréa Rocha

Criação da nova tabela SAFX para carga da Parametrização Produto x Produto ANP, usada no módulo do i\-SIMP\.

MFS524333

Liliane Assaf

Criação do campo Data de Validade Final \(RN08\)

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

Estrutura da tabela SAFX322 🡪 vide manual de layout

Campos que compõe a chave da tabela:

__   Data Validade Inicial \+ Grupo do Produto \+ Indicador do Produto \+ código do Produto \+  Código do Módulo__

A manutenção desta tabela é feita no Módulo i\-SIMP, menu Parâmetros 🡪 Produto x Produto ANP

Tabela de Destino:

A SAFX322 alimenta a tabela definitiva PRT\_PROD\_MSAF\_OBRIG

Sobre as mensagens de erro:

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

__Obs__\.: Os campos de Grupo do Produto e Código de Módulo não existem na tabela SAFX, só existem na tabela definitiva \(PRT\_PROD\_MSAF\_OBRIG\), porque eles serão preenchidos automaticamente na importação\.  O campo Grupo do Produto será preenchido com o grupo utilizado na importação\. O campo Código de Módulo deve ser preenchido com o valor fixo igual a ‘361’\.

 

MFS433027

__RN01__

__Campo 01 \- Indicador de Produto__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, ou quando for um indicador inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“Indicador do produto invalido ou nao preenchido”*

Indicadores válidos:

1 \- Produto;

2 \- Matéria Prima/Insumo;

3 \- Embalagem;

4 \- Material Uso/Consumo;

5 \- Outros;

6 \- Em Elaboração;

7 \- Intermediário;

8 \- Miscelâneas\.

MFS433027

__RN02__

__Campo 02 – Código do Produto __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“O codigo do produto e de preenchimento obrigatorio e nao foi informado”*

Crítica da existência do produto na SAFX2013:

O produto informado será validado na Tabela de Produtos\. Como a X2013 é uma tabela que trabalha com GRUPO, será necessário obter o Grupo de Relacionamento a ser utilizado nesta validação\. A informação do Grupo será obtida a partir do Estabelecimento \(campo 02\), e considerando a maior data de validade que seja <= a Início Validade \(campo 05\) do registro foco da importação\. 

A busca na tabela de produtos irá considerar o Indicador de Produto \(campo 03\), o Código do Produto \(campo 04\) e o Grupo obtido conforme a regra descrita acima\. Caso o produto não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem: 

*“Indicador/Codigo do produto não cadastrado”*

MFS433027

__RN03__

__Campo 03 \- Data Validade Inicial__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “O campo Data Validade Inicial é de preenchimento obrigatório e não foi informado”*

Caso o campo esteja preenchido, se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “O campo Data Validade Inicial é invalido”*

MFS433027

__RN04__

__Campo 04 \- Código do Produto da Obrigação__

Campo de preenchimento obrigatório\.

O código deve ser validado na tabela de Cadastro de Produtos das Obrigações \(TFIX117 \- PRT\_PROD\_OBRIG\)\.  Caso o código não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem::

*“Código do Produto da Obrigação não cadastrado no Cadastro de Produtos das Obrigações \(TFIX117\)“*

MFS433027

__RN05__

__Campo 05 – Número do Certificado de Qualidade__

Campo de preenchimento não obrigatório e sem validação de conteúdo\.

MFS433027

__RN06__

__Campo 06 – Código do Recipiente GLP__

Campo de preenchimento não obrigatório\.

Quando preenchido, o código deve ser validado na tabela de Código de Vasilhames \(TACES97 \- PRT\_VASILHAME\)\.  Caso o código não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem:

*“Código do Recipiente GLP não cadastrado na tabela de Código de Vasilhames \(TACES97\)“*

MFS433027

__RN07__

__Campo 07 – Tipo de Avaliação__

Campo de preenchimento não obrigatório e sem validação de conteúdo\.

MFS433027

__RN08__

__Campo 08 – Data Validade Final __

Campo de preenchimento não obrigatório\.

Caso o campo esteja preenchido, se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “93359 \- O campo Data Fim Validade é invalido”*

Caso o campo esteja preenchido, se for uma data menor que a Data de Validade Inicial, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“93360 \- O campo Data Fim Validade, quando preenchido, deve ser maior ou igual a Data Inicio Validade”*

__Tratamento para não permitir Intervalos Intercalados de Datas__:

Vamos adotar tratamentos para impedir que um produto \(com ou sem tipo de avaliação\) tenha parametrizações para uma obrigação \(exemplo i\-SIMP cod\_modulo = 361\) com intervalos de datas inicial e final que se intercalem\. Para isso, três regras devem ser atendidas:

1\) Não é permitido existir mais de uma parametrização vigente para um determinado produto sem uso do tipo de avaliação\.

2\) Não é permitido existir mais de uma parametrização vigente para um determinado produto e tipo de avaliação\.

3\) Não é permitido existir mais de uma parametrização vigente para um determinado produto, uma com tipo de avaliação e outra sem tipo de avaliação\.

Internamente esse controle deve ser por Código de Módulo em que a parametrização está disponível\. Como hoje só o módulo i\-SIMP trabalha com essa parametrização, considerar o código módulo = __361__\.

Ou seja, se um__ Produto A__ é parametrizado para um __Produto ANP__ \(código modulo 361\) sem tipo de avaliação, e num determinado momento passa a utilizar o tipo de avaliação\.  Para isso, primeiro deve\-se encerrar a validade da parametrização já existente e depois criar a nova, com validade inicial maior que a validade final da anterior\.

Da mesma forma deve\-se proceder quando o Produto é parametrizado com tipo de avaliação e deixa de utilizar o tipo de avaliação\.

__Exemplo1: Produto sem Data Fim de Validade__

Dado o produto 1\-A00 e Sem Tipo de Avaliação a ser importado via SAFX322\.

Parametrização já existente na base, com ou sem tipo de avaliação, registrado com Início Validade 01/01/2018 e Fim Validade nulo

Registros a serem importados via SAFX322:

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

Dado o produto 1\-A00 e Sem Tipo de Avaliação a ser importado via SAFX322\.

Parametrização já existente na base, com ou sem tipo de avaliação, registrado com Início Validade 01/01/2018 e Fim Validade 31/01/2018

Registros a serem importados via SAFX322:

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

1. Dado Produto \(indicador e código\) da parametrização que está sendo importada, buscar na base as parametrizações que obedeçam aos critérios:

\- Produto \(indicador e código\) = Produto \(indicador e código\) da parametrização foco da importação;

\- Código Módulo \(361\)

\- Tipo Avaliação da parametrização existente na base não preenchida;

  Ou

  Tipo Avaliação da parametrização foco da importação não preenchida;

  Ou

  \(Tipo Avaliação da parametrização existente na base preenchida E 

   Tipo Avaliação da parametrização foco da importação preenchida E

   Tipo Avaliação da parametrização existente na base = Tipo Avaliação da parametrização foco da importação\)

\- Data Validade Inicial da parametrização existente na base posterior à Data Validade Inicial do registro que está sendo importado\.

Caso o registro seja encontrado, comparar a Data Validade Final do registro que está sendo importado com a Data Validade Inicial do registro encontrado\.

Se Data Validade Final do registro que está sendo importado >= Data Validade Inicial do registro encontrado ou

     Data Validade Final do registro que está sendo importado for nula então:

O registro não será importado e no log de erros será gravada a seguinte mensagem:

Se Tipo Avaliação da parametrização existente na base estiver preenchida, então:

*“92182 \- Divergencia nas datas informadas”*

*“Foi encontrada parametrização para o produto e tipo de avaliação IND\-COD/TP\_AVALIACAO com datas de vigências iguais a DATA\_INI e DATA\_FIM, que estão em conflito com as datas de vigência informadas\.”*

Senão:

*“92182 \- Divergencia nas datas informadas”*

*“Foi encontrada parametrização para o produto IND\-COD com datas de vigências iguais a DATA\_INI e DATA\_FIM, que estão em conflito com as datas de vigência informadas\.”*

Onde:

IND\_COD: informar o indicador \+ código do produto;

TP\_AVALIACAO: informar o Tipo Avaliação da parametrização existente na base\.

DATA\_INI: informar a data validade inicial da parametrização existente na base\.

DATA\_FIM: informar a data validade final da parametrização existente na base\.

1. Dado Produto \(indicador e código\) da parametrização que está sendo importada, buscar na base as parametrizações que obedeçam aos critérios:

\- Produto \(indicador e código\) = Produto \(indicador e código\) da parametrização foco da importação;

\- Código Módulo \(361\)

\- Tipo Avaliação da parametrização existente na base não preenchida;

  Ou

  Tipo Avaliação da parametrização foco da importação não preenchida;

  Ou

  \(Tipo Avaliação da parametrização existente na base preenchida E 

   Tipo Avaliação da parametrização foco da importação preenchida E

   Tipo Avaliação da parametrização existente na base = Tipo Avaliação da parametrização foco da importação\)

\- Data Validade Inicial da parametrização existente na base anterior à Data Validade Inicial do registro que está sendo importado\.

Caso o registro seja encontrado, comparar a Data Validade Final do registro encontrado com a Data Validade Inicial do registro que está sendo importado\.

Se Data Validade Final do registro encontrado >= Data Validade Inicial do registro que está sendo importado ou

     Data Validade Final do registro encontrado for nula então:

O registro não será importado e no log de erros será gravada a seguinte mensagem:

Se Tipo Avaliação da parametrização existente na base estiver preenchida, então:

*“92182 \- Divergencia nas datas informadas”*

*“Foi encontrada parametrização para o produto e tipo de avaliação IND\-COD/TP\_AVALIACAO com datas de vigências iguais a DATA\_INI e DATA\_FIM, que estão em conflito com as datas de vigência informadas\.”*

Senão:

*“92182 \- Divergencia nas datas informadas”*

*“Foi encontrada parametrização para o produto IND\-COD com datas de vigências iguais a DATA\_INI e DATA\_FIM, que estão em conflito com as datas de vigência informadas\.”*

Onde:

IND\_COD: informar o indicador \+ código do produto;

TP\_AVALIACAO: informar o Tipo Avaliação da parametrização existente na base\.

DATA\_INI: informar a data validade inicial da parametrização existente na base\.

DATA\_FIM: informar a data validade final da parametrização existente na base\.

MFS524333

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


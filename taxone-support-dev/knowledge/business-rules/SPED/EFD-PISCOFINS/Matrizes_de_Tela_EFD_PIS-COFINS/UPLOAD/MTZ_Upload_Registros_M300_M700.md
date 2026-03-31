# MTZ_Upload_Registros_M300_M700

- **Fonte:** MTZ_Upload_Registros_M300_M700.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 35 KB

---

<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>Upload –<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a> Contribuição Diferida em Períodos Anteriores \- Valores a Pagar no Período de PIS/PASEP e COFINS – Registros M300/M700

\(EFD\- Escrituração Fiscal Digital das Contribuições\)

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3554

Registros M300/M700 através da funcionalidade Upload

Carregar as Contribuição Diferida em Períodos Anteriores \- Valores a Pagar no Período de PIS/PASEP e COFINS \(Registros M300/M700\) utilizando a funcionalidade Upload\.

26/06/2012

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__REGISTRO FILHO – M300/M700__

__RN01__

__Campo 08 \- COD\_REG__

__Item: __08

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Código do registro

__Tipo:__ A

__Tamanho: __010

__Comentário: __Campo destinado ao código do registro

Valores Válidos:

M300

M700

__Chave Primária__

__Obrigatório__

OS3554

__RN02__

__Campo 09 \- __Valor da Contribuição Apurada, diferida em períodos anteriores\.

__Item: __09

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da Contribuição Apurada, diferida em períodos anteriores\.

__Tipo:__ N

__Tamanho: __015V002

__Comentário: __Campo destinado ao Valor da Contribuição Apurada, diferida em períodos anteriores\.

__Não Obrigatório__

OS3554

__RN03__

__Campo 10 \- __Natureza do Crédito Diferido, vinculado à receita tributada no mercado interno, a descontar\.

__Item: __10

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Natureza do Crédito Diferido, vinculado à receita tributada no mercado interno, a descontar\.

__Tipo:__ A

__Tamanho: __002

__Comentário:  __Campo destinado a Natureza do Crédito Diferido, vinculado à receita tributada no mercado interno, a descontar\.

Valores válidos:

01 – Crédito a Alíquota Básica

02 \- Crédito a Alíquota Diferenciada

03 \- Crédito a Alíquota por Unidade de Produto

04  \- Crédito  Presumido da Agroindústria

__Chave Primária__

__Não Obrigatório__

OS3554

__RN04__

__Campo 11 \- __Valor do credito a descontar, vinculado à  Contribuição diferida\.

__Item: __11

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do credito a descontar, vinculado à  Contribuição diferida\.

__Tipo:__ N

__Tamanho: __015V002

__Comentário: __Campo destinado ao Valor do credito a descontar, vinculado à  Contribuição diferida\.

__Não Obrigatório__

OS3554

__RN05__

__Campo 12 \- __Valor da  Contribuição  a Recolher, diferida em períodos anteriores\.

__Item: __12

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da  Contribuição  a Recolher, diferida em períodos anteriores\.

__Tipo:__ N

__Tamanho: __015V002

__Comentário:  __Campo destinado ao Valor da  Contribuição  a Recolher, diferida em períodos anteriores\.

__Não Obrigatório__

__ATENÇÃO: Este campo será calculado pelo sistema, caso seja enviado algum valor, o mesmo será desconsiderado\.__

OS3554

__RN06__

__Campo 13 \- __Período da Apuração da contribuição social e dos creditos diferidos

__Item: __13

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Período da Apuração da contribuição social e dos creditos diferidos 

__Tipo:__ N

__Tamanho: __006

__Comentário:  __Campo destinado ao Período da Apuração da contribuição social e dos creditos diferidos

\(Formato: AAAAMM\)

__Obrigatório__

__Chave Primária__

OS3554

__RN07__

__Campo 14 \- __Data de recebimento da receita, objeto de diferimento__ __

__Item: __14

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Data de recebimento da receita, objeto de diferimento

__Tipo:__ N

__Tamanho: __008

__Comentário: __Campo destinado a Data de recebimento da receita, objeto de diferimento

__Chave Primária__

__Não Obrigatório__

OS3554

__RN08__

Validação do Arquivo:

1. O campo COD\_REG  possui os seguintes valores válidos: M300,M700\.
2. O campo a Natureza do Crédito Diferido, vinculado à receita tributada no mercado interno, a descontar, possui os seguintes Valores válidos: ‘01 – Crédito a Alíquota Básica’, ‘02 \- Crédito a Alíquota Diferenciada’, ‘03 \- Crédito a Alíquota por Unidade de Produto’ e ‘04  \- Crédito  Presumido da Agroindústria’
3. Se algum dos campos obrigatórios \(Registro Filho: Campo 13 \- Período da Apuração da contribuição social e dos creditos diferidos\)  não for enviado, exibir a seguinte msg no log do processo: ‘O Campo <nome\_campo\_no\_layout> e obrigatorio\.’
4. Se  qualquer campo ultrapassar o tamanho definido no layout, só serão importada as primeiras posições até chegar ao tamanho definido no layout\.
5. Caso seja enviada uma informação inválida para o campo Natureza do Crédito Diferido, vinculado à receita tributada no mercado interno, a descontar, exibir a seguinte msg ao usuário: ‘O campo Natureza do Crédito Diferido, vinculado à receita tributada no mercado interno, a descontar enviado nao esta de acordo com o Manual de Layout\. Valor Informado: XXX’
6. Ao carregar as informações de um arquivo via UPLOAD e existir na base algum registro que não foi salvo, exibir a seguinte msg ao usuário: Existem dados que ainda não foram salvos\. Deseja continuar? Se sim, os registros que estão sendo carregados via Upload serão lidos e os registros não salvos, só serãoconsiderados após o usuário confirmar as informações na tela\. Se não, nada será carregado e o usuário poderá salvar os registros que ainda não foram salvos na tela\.
7. Ainda sobre o item acima, Se o usuário tentar carregar alguma informação já existente na base, a linha do registro enviada no arquivo deve sobrepor as informações já existentes\.
8. O campo 14\-  Data de recebimento da receita, objeto de diferimento , deve estar dentro do período de apuração escolhido, caso contrário exibir a seguinte msg ao usuário: A data de recebimento da receita devera estar compreendida no período atual da escrituração\. Favor verificar\.
9. O campo Campo 12 \- Valor da  Contribuição  a Recolher, diferida em períodos anteriores, será calculado pelo sistema, caso o cliente envie informação neste campo,o valor será desconsiderado\.

OS3554


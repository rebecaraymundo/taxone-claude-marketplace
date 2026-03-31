# MTZ_Upload_Registros_M230_M630

- **Fonte:** MTZ_Upload_Registros_M230_M630.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 35 KB

---

<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>Upload –<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a> Informações Adicionais de Diferimento de PIS/PASEP e COFINS – Registros M230/M630

\(EFD\- Escrituração Fiscal Digital das Contribuições\)

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3554

Registros M230/M630 através da funcionalidade Upload

Carregar as Informações Adicionais de Diferimento de PIS/PASEP e COFINS \(Registros M230/M630\) utilizando a funcionalidade Upload\.

26/06/2012

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__REGISTRO FILHO – M230/M630__

__RN01__

__Campo 08 \- COD\_REG__

__Item: __08

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Código do registro

__Tipo:__ A

__Tamanho: __010

__Comentário: __Campo destinado ao código do registro

Valores Válidos:

M230

M630

__Chave Primária__

__Obrigatório__

OS3554

__RN02__

__Campo 09 \- CNPJ__

__Item: __09

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __CNPJ da pessoa juridica de direito publico, empresa publica, sociedade de economia mista ou suas subsidiárias

__Tipo:__ A

__Tamanho: __014

__Comentário: __Campo destinado ao CNPJ da pessoa juridica de direito publico, empresa publica, sociedade de economia mista ou suas subsidiárias __Obrigatório__

__Campo Chave__

OS3554

__RN03__

__Campo 10 – Valor Total das Vendas__

__Item: __10

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor Total das Vendas no periodo__ __

__Tipo:__ N

__Tamanho: __015V002

__Comentário:  Campo destinado ao __Valor Total das Vendas no periodo 

__Não Obrigatório__

OS3554

__RN04__

__Campo 11 \- __Valor total não recebido no periodo

__Item: __11

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor total não recebido no periodo__ __

__Tipo:__ N

__Tamanho: __015V002

__Comentário: __Campo destinado ao Valor total não recebido no periodo

__Não Obrigatório__

OS3554

__RN05__

__Campo 12 \- __Valor da contribuição diferida no período

__ Item: __12

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor da contribuição diferida no periodo__ __

__Tipo:__ N

__Tamanho: __015V002

Sendo 015 inteiros e 2decimais

__Comentário:  __Campo destinado ao Valor da contribuição diferida no periodo__ __

__Não Obrigatório__

OS3554

__RN06__

__Campo 13  \- __Valor do credito diferido no período

__Item: __13

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do credito diferido no período 

__Tipo:__ N

__Tamanho: __015V002

__Comentário:  __Campo destinado ao Valor do credito diferido no período

__Não Obrigatório__

OS3554

__RN07__

__Campo 14 \- __Código do tipo de crédito diferido no período__ __

__Item: __14

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Código do tipo de crédito diferido no período

__Tipo:__ A

__Tamanho: __003

__Comentário: __Campo destinado ao Código do tipo de crédito diferido no período\. Conforme tabela 4\.3\.6\.

Valores Válidos:

101

Crédito vinculado à receita tributada no mercado interno – Alíquota Básica

102

Crédito vinculado à receita tributada no mercado interno – Alíquotas Diferenciadas

103

Crédito vinculado à receita tributada no mercado interno – Alíquota por Unidade de Produto

104

Crédito vinculado à receita tributada no mercado interno – Estoque de Abertura

105

Crédito vinculado à receita tributada no mercado interno – Aquisição Embalagens para revenda

106

Crédito vinculado à receita tributada no mercado interno – Presumido da Agroindústria

107

Crédito vinculado à receita tributada no mercado interno – Outros Créditos Presumidos

108

Crédito vinculado à receita tributada no mercado interno – Importação

109

Crédito vinculado à receita tributada no mercado interno – Atividade Imobiliária

199

Crédito vinculado à receita tributada no mercado interno – Outros

201

Crédito vinculado à receita não tributada no mercado interno – Alíquota Básica

202

Crédito vinculado à receita não tributada no mercado interno – Alíquotas Diferenciadas

203

Crédito vinculado à receita não tributada no mercado interno – Alíquota por Unidade de Produto

204

Crédito vinculado à receita não tributada no mercado interno – Estoque de Abertura

205

Crédito vinculado à receita não tributada no mercado interno – Aquisição Embalagens para revenda

206

Crédito vinculado à receita não tributada no mercado interno – Presumido da Agroindústria

207

Crédito vinculado à receita não tributada no mercado interno – Outros Créditos Presumidos

OS3554

__RN07__

208

Crédito vinculado à receita não tributada no mercado interno – Importação

299

Crédito vinculado à receita não tributada no mercado interno – Outros

301

Crédito vinculado à receita de exportação – Alíquota Básica

302

Crédito vinculado à receita de exportação – Alíquotas Diferenciadas

303

Crédito vinculado à receita de exportação – Alíquota por Unidade de Produto

304

Crédito vinculado à receita de exportação – Estoque de Abertura

305

Crédito vinculado à receita de exportação – Aquisição Embalagens para revenda

306

Crédito vinculado à receita de exportação – Presumido da Agroindústria

307

Crédito vinculado à receita de exportação – Outros Créditos Presumidos

308

Crédito vinculado à receita de exportação – Importação

399

Crédito vinculado à receita de exportação – Outros

__Obrigatório__

__Campo Chave__

OS3554

__RN08__

Validação do Arquivo:

1. O campo COD\_REG  possui os seguintes valores válidos: M230,M630\.
2. Se algum dos campos obrigatórios \(Registro Filho: Campo 09 \- CNPJ, Campo 14 \- Código do tipo de crédito diferido no período\) não for enviado, exibir a seguinte msg no log do processo: ‘O Campo <nome\_campo\_no\_layout> e obrigatorio\.’
3. Se  qualquer campo ultrapassar o tamanho definido no layout, só serão importada as primeiras posições até chegar ao tamanho definido no layout\.
4. Caso seja enviada uma informação inválida para o campo Código do tipo de crédito diferido no período, exibir a seguinte msg ao usuário: ‘O Código do tipo de crédito diferido no período enviado nao esta de acordo com o Manual de Layout\. Valor Informado:XXX’
5. Ao carregar as informações de um arquivo via UPLOAD e existir na base algum registro que não foi salvo, exibir a seguinte msg ao usuário: Existem dados que ainda não foram salvos\. Deseja continuar? Se sim, os registros que estão sendo carregados via Upload serão lidos e os registros não salvos, só serão considerados após o usuário confirmar as informações na tela\. Se não, nada será carregado e o usuário poderá salvar os registros que ainda não foram salvos na tela\.
6. Ainda sobre o item acima, Se o usuário tentar carregar alguma informação já existente na base, a linha do registro enviada no arquivo deve sobrepor as informações já existentes\.
7. Deve ser verificado se o CNPJ informado está valido ou não, considerando a mesma regra existente na tela\. Caso contrário, informar: ‘CNPJ inválido’

OS3554


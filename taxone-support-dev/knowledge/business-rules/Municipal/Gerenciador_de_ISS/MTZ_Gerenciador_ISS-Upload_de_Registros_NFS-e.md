# MTZ_Gerenciador_ISS-Upload_de_Registros_NFS-e

- **Fonte:** MTZ_Gerenciador_ISS-Upload_de_Registros_NFS-e.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 45 KB

---

<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>

__MUNICIPAL__

__Gerenciador ISS__

__Upload –__<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>__ Registros de NFS\-e __

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3888\-A

Gerenciador ISS \- Criação da opção de importação das informações dos arquivos de retorno das prefeituras

Criação da tabela das informações recuperadas através do upload\.

OS3888\-A1

Gerenciador ISS \- Criação da opção de importação das informações dos arquivos de retorno das prefeituras

Criação da funcionalidade de upload das NFS\-e exportadas do site das prefeituras\. Essas informações serão necessárias para a conciliação de notas de serviços\.

MFS3725

Gerenciador ISS \- Criação de novos campos na TFIX128

Criação de novos campos na TFIX128

##### REGRAS DE NEGÓCIO

#### Cód\.

__Descrição__

### DR

__RN00__

__Regras Gerais __

As informações importadas pelo processo de Upload devem ser armazenadas em uma determinada tabela\. 

O funcionamento do upload deve ser semelhante ao processo de importação de TFIX/TACES\.

__OS3888\-A1__

__RN01__

__Regras de validação__

1. Campos numéricos inválidos\. Não é permitido em campos numéricos, caracteres especiais e letras\. Exibir a seguinte msg no log: Nao foi possivel converter o valor informado no arquivo para um valor numerico valido\. Valor informado: XXXX
2. Campos de data devem ser enviados com a formatação ‘DDMMAAAA’ , caso contrário, exibir a seguinte msg: Nao foi possivel converter o valor informado no arquivo para uma data valida\. Valor informado: XXXXX
3. Campos alfanuméricos inválidos\. Exibir a seguinte msg: Não foi possível converter o valor informado no arquivo para um valor alfanumerico valido\. Valor informado: XXXX
4. Caso o usuário informar um valor maior que o determinado em layout, os caracteres que estiverem a mais serão descartados\. 
5. Todas as mensagens do log deve conter a linha do registro com o problema, facilitando assim a identificação da situação para o usuário\. A informação linha deve conter uma numeração sequencial \(que não pode ter repetição\) 
6. Caso o campo esteja obrigatorio e venha informação nula ou não seja informado no arquivo: O Campo XXXX é obrigatório\.

OS3888\-A

__RN02__

__Campo 01 – Data de Emissão da NFS\-e__

__Item: __01

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Data de Emissão da NFS\-e

__Tipo:__ D

__Tamanho: __14

__Formato:__ DDMMAAAA

__Comentário: __Campo destinado a data de emissão da NFS\-e

__Chave Primária__

__Obrigatório__

OS3888\-A

__RN03__

__Campo 02 – Número da NFS\-e__

__Item: __02

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Número da NFS\-e

__Tipo:__ A

__Tamanho: __12

__Comentário: __Campo destinado ao número da NFS\-e__ __

__Chave Primária__

__Obrigatório__

OS3888\-A

__RN04__

__Campo 03 – CNPJ/CPF do Prestador__

__Item: __03

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __CNPJ ou CPF do Prestador

__Tipo:__ A

__Tamanho: __14

__Comentário: __Campo destinado ao CNPJ ou CPF do prestador

__Chave Primária__

__Obrigatório__

OS3888\-A

__RN05__

__Campo 04 – Inscrição Municipal do Prestador__

__Item: __04

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Inscrição Municipal do Prestador

__Tipo:__ A

__Tamanho: __14

__Comentário: __Campo destinado à inscrição municipal do prestador

OS3888\-A

__RN06__

__Campo 05 – Razão Social do Prestador__

__Item: __05

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Razão Social do Prestador

__Tipo:__ A

__Tamanho: __75

__Comentário: __Campo destinado à razão social do prestador

__Obrigatório__

OS3888\-A

__RN07__

__Campo 06 – Código do Serviço__

__Item: __06

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Código do Serviço

__Tipo:__ A

__Tamanho: __20

__Comentário: __Campo destinado ao código do serviço

__Obrigatório__

OS3888\-A

__RN08__

__Campo 07 – Descrição do Serviço__

__Item: __07

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Descrição do Serviço

__Tipo:__ A

__Tamanho: __1000

__Comentário: __Campo destinado à descrição do serviço prestado

OS3888\-A

__RN09__

__Campo 08 – Alíquota__

__Item: __08

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Alíquota__ __

__Tipo:__ N

__Tamanho: __07__ __

__Formato: __003V004

__Comentário: __Campo destinado à alíquota do serviço prestado

OS3888\-A

__RN10__

__Campo 09 – Valor do Serviço__

__Item: __09

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do Serviço

__Tipo:__ N

__Tamanho: __15

__Formato: __013V002

__Comentário: __Campo destinado ao valor do serviço

__Obrigatório__

OS3888\-A

__RN11__

__Campo 10 – Valor do ISS__

__Item: __10

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor do ISS

__Tipo: __N 

__Tamanho: __15__ __

__Formato: __013V002

__Comentário: __Campo destinado ao valor do ISS

__Obrigatório__

OS3888\-A

__RN12__

__Campo 11 – Data Fiscal__

__Item: __11

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Data Fiscal da NFS\-e

__Tipo: __D

__Tamanho: __14

__Formato: __DDMMAAAA

__Comentário: __Campo destinado a data fiscal da NFS\-e

__Obrigatório__

MFS3725

__RN13__

__Campo 12 – Valor Total da NFS\-e__

__Item: 12__

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor Total da NFS\-e

__Tipo:__ N__ __

__Tamanho:__ 15__ __

__Formato:__ 013V002

__Comentário: __Campo destinado ao valor total da NFS\-e

MFS3725

__RN14__

__Campo 13 – Valor Base ISS__

__Item: __13

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor base ISS

__Tipo: __N__ __

__Tamanho: __15 

__Formato: __013V002

__Comentário: __Campo destinado ao valor da base ISS

MFS3725

__RN15__

__Campo 14 – Serie NFS\-e__

__Item: __14

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Serie NFS\-e

__Tipo: __A__ __

__Tamanho: __03 

__Comentário: __Campo destinado à série da NFS\-e

MFS3725

__RN16__

__Campo 15 – Sub Serie NFS\-e__

__Item: __15

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Sub Serie NFS\-e

__Tipo:__ A__ __

__Tamanho:__ 02

__Comentário: __Campo destinado à subsérie da NFS\-e

MFS3725

__RN17__

__Campo 16 – Valor Deduções__

__Item: __16

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Valor Deduções

__Tipo: __N__ __

__Tamanho: __15 

__Formato:__ 013V002

__Comentário: __Campo destinado ao valor deduções de ISS

MFS3725


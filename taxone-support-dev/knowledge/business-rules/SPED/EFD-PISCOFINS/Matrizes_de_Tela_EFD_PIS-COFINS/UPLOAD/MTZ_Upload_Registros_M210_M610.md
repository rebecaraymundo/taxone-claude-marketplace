# MTZ_Upload_Registros_M210_M610

- **Fonte:** MTZ_Upload_Registros_M210_M610.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 34 KB

---

<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>Upload –<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a> Ajustes do Crédito de PIS/PASEP e COFINS – Registros M210/M610

\(EFD\- Escrituração Fiscal Digital das Contribuições\)

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3619

Ajustes do crédito de PIS/PASEP e COFINS \(Registros M210/M610\)

Será criada a funcionalidade Upload para carregar as informações dos ajustes do crédito de PIS/PASEP e COFINS \(Registros M210/M610\)

25/05/2012

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__REGISTRO PAI – M210/M610__

__RN01__

__Campo 01 \- COD\_REG__

__Item: __01

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Código do registro

__Tipo:__ A

__Tamanho: __010

__Comentário: __Campo destinado ao código do registro

Valores Válidos:

M210

M610

__Chave Primária__

__Obrigatório__

OS3619

__RN02__

__Campo 02 \- COD\_CONTRIB__

__Item: __02

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Código da contribuição social apurada no período, conforme a Tabela 4\.3\.5\.

__Tipo:__ A

__Tamanho: __002

__Comentário: __Código da contribuição social apurada no período, conforme a Tabela 4\.3\.5\.

Valores válidos: 

Código

Descrição

01

Contribuição não\-cumulativa apurada a alíquota básica

02

Contribuição não\-cumulativa apurada a alíquotas diferenciadas

03

Contribuição não\-cumulativa apurada a alíquota por unidade de medida de produto

04

Contribuição não\-cumulativa apurada a alíquota básica – Atividade Imobiliária

31

Contribuição apurada por substituição tributária

32

Contribuição apurada por substituição tributária – Vendas à Zona Franca de Manaus

51

Contribuição cumulativa apurada a alíquota básica

52

Contribuição cumulativa apurada a alíquotas diferenciadas

53

Contribuição cumulativa apurada a alíquota por unidade de medida de produto

54

Contribuição cumulativa apurada a alíquota básica – Atividade Imobiliária

70

Contribuição apurada da Atividade Imobiliária \- RET

71

Contribuição apurada de SCP – Incidência Não Cumulativa

72

Contribuição apurada de SCP – Incidência Cumulativa

99 

Contribuição para o PIS/Pasep – Folha de Salários

__Chave Primária__

__Obrigatório__

OS3619

__RN03__

__Campo 03 \- VLR\_ALIQ\_PERC__

__Item: __04

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Alíquota \(em percentual\)

__Tipo:__ N

__Tamanho: __008

Sendo 4 inteiras e 4 decimais

__Comentário: __Campo destinado a Alíquota \(em percentual\)

__Chave Primária__

__Obrigatório__

__RN04__

__Campo 04 \- VLR\_ALIQ\_R__

__Item: __04

__Nome do Campo: __A ser definido pelo A&D

__Descrição: __Alíquota \(em reais\)

__Tipo:__ N

__Tamanho: __019

Sendo 15 inteiras e 4 decimais

__Comentário: __Campo destinado a Alíquota \(em reais\)

__Chave Primária__

__Obrigatório__

OS3619

__RN05__

__Validações__

1 \. Valores Válidos do campo COD\_REG: M210, M610

2\. Valores válidos do campo __COD\_CONTRIB__:

Código

Descrição

01

Contribuição não\-cumulativa apurada a alíquota básica

02

Contribuição não\-cumulativa apurada a alíquotas diferenciadas

03

Contribuição não\-cumulativa apurada a alíquota por unidade de medida de produto

04

Contribuição não\-cumulativa apurada a alíquota básica – Atividade Imobiliária

31

Contribuição apurada por substituição tributária

32

Contribuição apurada por substituição tributária – Vendas à Zona Franca de Manaus

51

Contribuição cumulativa apurada a alíquota básica

52

Contribuição cumulativa apurada a alíquotas diferenciadas

53

Contribuição cumulativa apurada a alíquota por unidade de medida de produto

54

Contribuição cumulativa apurada a alíquota básica – Atividade Imobiliária

70

Contribuição apurada da Atividade Imobiliária \- RET

71

Contribuição apurada de SCP – Incidência Não Cumulativa

72

Contribuição apurada de SCP – Incidência Cumulativa

99 

Contribuição para o PIS/Pasep – Folha de Salários

3\. Se o campo Vlr\_Aliq\_Perc estiver preenchido o campo Vlr\_Aliq\_R  não deve possuir informação\. Neste caso exibir a seguinte msg ao usuário: Se o campo Vlr\_Aliq\_Perc estiver preenchido o campo Vlr\_Aliq\_R nao deve estar preenchido\.

4\. Se o campo Vlr\_Aliq\_R estiver preenchido o campo Vlr\_Aliq\_Perc não deve possuir informação\. Neste caso exibir a seguinte msg ao usuário: Se o campo Vlr\_Aliq\_R estiver preenchido o campo Vlr\_Aliq\_Perc nao deve estar preenchido\.

5\.  Se o registro pai \(M210\), informado no arquivo lido, não existir na base, exibir a seguinte msg no log do processo: Nao foi encontrado registro pai com as seguintes informações chave \(Cod\_Contrib/Vlr\_Aliq\_Perc/Vlr\_Aliq\_R\):

6\.  Se o registro pai não for encontrado na base \(conforme citado no item 2\), automaticamente os seus filhos serão desconsiderados\.

7\.  Se algum dos campos obrigatórios \(__Registro Pai:__Campo 01 \- COD\_REG, Campo 02 \- __COD\_CONTRIB__, Campo 03 – Vlr\_Aliq\_Perc  ou Campo 04 \- Vlr\_Aliq\_R\. não for enviado, exibir a seguinte msg no log do processo: O Campo <nome\_campo\_no\_layout> e obrigatorio\.

8\. Se  qualquer campo ultrapassar o tamanho definido no layout, só serão importada as primeiras posições até chegar ao tamanho definido no layout\.

9 \. Se o campo código da contribuição  não possuir um valor válido: Codigo de Contribuicao enviado nao esta de acordo com o Manual de Layout\. Valor Informado:XXXX

10\. Se o registro pai não pertence à funcionalidade chamadora\(PIS/COFINS\) ou filhos não pertencem ao pai respectivo, exibir a seguinte msg: Atencao o registro filho <valor\_nivel2> nao pertence ao registro pai <valor\_nivel1> ou nao pertence ao conjunto de informacoes do <funcionalidade chamadora>\. O registro sera desconsiderado\.


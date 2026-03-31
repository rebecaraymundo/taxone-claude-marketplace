# MTZ-Upload_Registros_M300_M700

> Fonte: MTZ-Upload_Registros_M300_M700.docx




Upload – Contribuição Diferida em Períodos Anteriores - Valores a Pagar no Período de PIS/PASEP e COFINS – Registros M300/M700
(EFD- Escrituração Fiscal Digital das Contribuições)


DOCUMENTO DE REQUISITO


### REGRAS DE NEGÓCIO





| DR | Nome | Descrição | Data Alteração |
| --- | --- | --- | --- |
| OS3554 | Registros M300/M700 através da funcionalidade Upload | Carregar as Contribuição Diferida em Períodos Anteriores - Valores a Pagar no Período de PIS/PASEP e COFINS (Registros M300/M700) utilizando a funcionalidade Upload. | 26/06/2012 |
| CH19692_2016 | Lara Aline | Ajuste na Validação do Arquivo (RN08) incluindo validação para o Período da Apuração da contribuição social e dos créditos diferidos | 06/10/2016 |


| Cód. |  | DR |
| --- | --- | --- |
|  | REGISTRO FILHO – M300/M700 |  |
| RN01 | Campo 08 - COD_REG Item: 08 Nome do Campo: A ser definido pelo A&D Descrição: Código do registro Tipo: A Tamanho: 010 Comentário: Campo destinado ao código do registro Valores Válidos: M300 M700 Chave Primária Obrigatório | OS3554 |
| RN02 | Campo 09 - Valor da Contribuição Apurada, diferida em períodos anteriores. Item: 09 Nome do Campo: A ser definido pelo A&D Descrição: Valor da Contribuição Apurada, diferida em períodos anteriores. Tipo: N Tamanho: 015V002 Comentário: Campo destinado ao Valor da Contribuição Apurada, diferida em períodos anteriores. Não Obrigatório | OS3554 |
| RN03 | Campo 10 - Natureza do Crédito Diferido, vinculado à receita tributada no mercado interno, a descontar. Item: 10 Nome do Campo: A ser definido pelo A&D Descrição: Natureza do Crédito Diferido, vinculado à receita tributada no mercado interno, a descontar. Tipo: A Tamanho: 002 Comentário:  Campo destinado a Natureza do Crédito Diferido, vinculado à receita tributada no mercado interno, a descontar. Valores válidos: 01 – Crédito a Alíquota Básica 02 - Crédito a Alíquota Diferenciada 03 - Crédito a Alíquota por Unidade de Produto 04  - Crédito  Presumido da Agroindústria Chave Primária Não Obrigatório | OS3554 |
| RN04 | Campo 11 - Valor do credito a descontar, vinculado à  Contribuição diferida. Item: 11 Nome do Campo: A ser definido pelo A&D Descrição: Valor do credito a descontar, vinculado à  Contribuição diferida. Tipo: N Tamanho: 015V002 Comentário: Campo destinado ao Valor do credito a descontar, vinculado à  Contribuição diferida. Não Obrigatório | OS3554 |
| RN05 | Campo 12 - Valor da  Contribuição  a Recolher, diferida em períodos anteriores.  Item: 12 Nome do Campo: A ser definido pelo A&D Descrição: Valor da  Contribuição  a Recolher, diferida em períodos anteriores. Tipo: N Tamanho: 015V002 Comentário:  Campo destinado ao Valor da  Contribuição  a Recolher, diferida em períodos anteriores. Não Obrigatório  ATENÇÃO: Este campo será calculado pelo sistema, caso seja enviado algum valor, o mesmo será desconsiderado. | OS3554 |
| RN06 | Campo 13 - Período da Apuração da contribuição social e dos creditos diferidos Item: 13 Nome do Campo: A ser definido pelo A&D Descrição: Período da Apuração da contribuição social e dos creditos diferidos  Tipo: N Tamanho: 006 Comentário:  Campo destinado ao Período da Apuração da contribuição social e dos creditos diferidos (Formato: AAAAMM) Obrigatório Chave Primária | OS3554 |
| RN07 | Campo 14 - Data de recebimento da receita, objeto de diferimento  Item: 14 Nome do Campo: A ser definido pelo A&D Descrição: Data de recebimento da receita, objeto de diferimento Tipo: N Tamanho: 008 Comentário: Campo destinado a Data de recebimento da receita, objeto de diferimento Chave Primária Não Obrigatório | OS3554 |
| RN08 | Validação do Arquivo:  O campo COD_REG  possui os seguintes valores válidos: M300,M700. O campo a Natureza do Crédito Diferido, vinculado à receita tributada no mercado interno, a descontar, possui os seguintes Valores válidos: ‘01 – Crédito a Alíquota Básica’, ‘02 - Crédito a Alíquota Diferenciada’, ‘03 - Crédito a Alíquota por Unidade de Produto’ e ‘04  - Crédito  Presumido da Agroindústria’ Se algum dos campos obrigatórios (Registro Filho: Campo 13 - Período da Apuração da contribuição social e dos creditos diferidos)  não for enviado, exibir a seguinte msg no log do processo: ‘O Campo <nome_campo_no_layout> e obrigatorio.’ Se  qualquer campo ultrapassar o tamanho definido no layout, só serão importada as primeiras posições até chegar ao tamanho definido no layout. Caso seja enviada uma informação inválida para o campo Natureza do Crédito Diferido, vinculado à receita tributada no mercado interno, a descontar, exibir a seguinte msg ao usuário: ‘O campo Natureza do Crédito Diferido, vinculado à receita tributada no mercado interno, a descontar enviado nao esta de acordo com o Manual de Layout. Valor Informado: XXX’ Ao carregar as informações de um arquivo via UPLOAD e existir na base algum registro que não foi salvo, exibir a seguinte msg ao usuário: Existem dados que ainda não foram salvos. Deseja continuar? Se sim, os registros que estão sendo carregados via Upload serão lidos e os registros não salvos, só serãoconsiderados após o usuário confirmar as informações na tela. Se não, nada será carregado e o usuário poderá salvar os registros que ainda não foram salvos na tela. Ainda sobre o item acima, Se o usuário tentar carregar alguma informação já existente na base, a linha do registro enviada no arquivo deve sobrepor as informações já existentes. O campo 13- Período da Apuração da contribuição social e dos creditos diferidos deve ser de um período anterior ao período de apuração escolhido, caso contrário exibir a seguinte msg ao usuário: Período da Apuração da Contribuicao e dos Creditos Diferidos não pertence a um período anterior ao período da apuração. Favor verificar. O campo 14- Data de recebimento da receita, objeto de diferimento , deve estar dentro do período de apuração escolhido, caso contrário exibir a seguinte msg ao usuário: A data de recebimento da receita devera estar compreendida no período atual da escrituração. Favor verificar. O campo Campo 12 - Valor da  Contribuição  a Recolher, diferida em períodos anteriores, será calculado pelo sistema, caso o cliente envie informação neste campo,o valor será desconsiderado. | OS3554 CH19692_2016 |

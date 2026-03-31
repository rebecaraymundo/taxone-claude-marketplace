# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX275

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX275.docx
- **Modificado:** 2022-09-21
- **Tamanho:** 73 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX275 – Dependentes sem Vínculo

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

MFS\-27019

Alessandra Cristina Navatta

Definição das regras de importação, online e Batch, da SAFX275\.

MFS\-79885

Alessandra Cristina Navatta

Alteração da lista de valores válidos do campo Relação de Dependência, conforme versão 2\.1\.1 do REINF\.

Inclusão de validação no campo Descrição

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX275 – Dependentes sem Vínculo, que deve ser criada com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Indicador de Pessoa Física/Jurídica

A

001

SIM

SIM

Código Pessoa Física/Jurídica

A

014

SIM

SIM

Data Início/Inclusão/Alteração

N

008

SIM

SIM

Data Início de Vigência

N

008

SIM

SIM

Data Final de Vigência

N

008

NÃO

NÃO

CPF do Dependente

A

011

SIM

SIM

Nome do Dependente

A

060

SIM

NÃO

Data Nascimento do Dependente

N

008

SIM

NÃO

Relação de dependência

N

002

SIM

NÃO

Descrição 

A

060

NÃO

NÃO

Ind\. Pensão Alimentícia

A

001

SIM

NÃO

Ind\. Plano de Saúde

A

001

SIM

NÃO

 

MFS\-27019

RN02

__Sobre as mensagens de erro:__

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

MFS\-27019

RN03

__Mensagens Gerais:__

No processo de carga:

- Se algum campo de preenchimento obrigatório não for enviado, exibir a mensagem: <a id="_Hlk8738371"></a>“<<Nome Funcional do campo>> nao esta preenchido”
- Se algum campo receber formato de campo diferente do esperado, exibir a mensagem: “<<Nome Funcional do campo>> com formato invalido\.”
- Se algum campo possuir tamanho maior que o esperado, exibir a mensagem: “A informação do campo <<Nome Funcional do campo>> esta maior do que o tamanho maximo definido”

MFS\-27019

RN04

__Verificação de existência do registro pai__

Por ser esta tabela filha da SAFX04, no momento da importação deve ser verificada a existência de registro correspondente na tabela pai, considerando como chave de relacionamento os campos Indicador de Pessoa Física/Jurídica, Código Pessoa Física/Jurídica, Data Início/Inclusão/Alteração\. Caso não encontre, retornar a mensagem de código 90124: “O Codigo da Pessoa Fisica/Juridica nao esta cadastrado”\.

MFS\-27019

RN05

__Campo Data Início de Vigência__

Data Início de vigência deve ser igual ou superior a data de inicio de validade do cadastro da PF vinculada\. Caso contrário, exibir a mensagem: “<<Nome funcional>> deve ser igual ou maior que a data inicial da Pessoa Física/Jurídica\.”

MFS\-27019

RN06

__Campo Data Final de Vigência__

Data Final de Vigência deve ser maior que Data Início de Vigência\. Caso data final seja menor que a data início de vigência, exibir a mensagem: “A data de validade final deve ser maior que a data de validade inicial\.”

MFS\-27019

RN07

__Campo Indicador Pessoa Física/Jurídica__

Indicador de Pessoa Física/Jurídica relacionada \(SAFX04\), conforme segue:

1 – Fornecedor;

2 – Cliente;

3 – Estabelecimento;

4 – Transportadora;

5 – Cliente/Fornecedor/Transportadora\.

Caso a informação esteja diferente dos valores válidos, exibir a mensagem: O campo deve ser preenchido com 1,2,3,4 ou 5

MFS\-27019

RN08

__Campo Código Pessoa Física/Jurídica__

Só será permitido códigos de pessoa física\. Caso seja informado um código cujo o campo CPF/CNPJ for igual a CNPJ, exibir a mensagem “Não é permitido vincular dependentes à Pessoa Jurídica”\.

FS\-27019

RN09

__Campo CPF do Dependente__

Validar se é um CPF válido, caso contrário, exibir a mensagem: “<<Nome Funcional do campo>> nao e valido\.”

MFS\-27019

RN10

__Campo Relação de Dependência__

Lista de Valores Válidos:

1, 2, 3, 4, 5, 6, 7, 99\.

__\[Alteração MFS\-79885\]__ Atualização da lista de valores válidos

Lista de Valores Válidos:

1, 2, 3, 6, 8,9,10,11,12, 99\.

Caso o valor seja diferente da lista de valores válidos, exibir a mensagem: “O campo <<nome funcional do campo>> deve ser preenchido com uma das opções validas: <1>, <2>, <3>, <6>, <8>, <9>, <10> , <11> , <12> ou <99>”

MFS\-27019

MFS\-79885

RN11

__Campo Descrição__

Este campo é de preenchimento obrigatório e exclusivo se o campo Relação de Dependência estiver preenchido com ‘99’\.

- Caso o campo Relação de Dependência estiver preenchido com ‘99’ e não existir informação neste campo, exibir a mensagem: “<<Nome Funcional do campo>> nao esta preenchido”
- Caso o campo Relação de Dependência estiver preenchido com informação diferente de ‘99’ e existir informação neste campo, exibir a mensagem: “<<Nome Funcional do campo>> nao pode ser preenchido, quando Relacao de Dependencia for diferente de ’99’”

MFS\-79885

RN12

__Campo Ind Pensão Alimentícia__

Lista de valores válidos:

S – Sim

N \- Não

Caso o valor seja diferente da lista de valores válidos, exibir a mensagem: “O campo <<nome funcional do campo>> deve ser preenchido com uma das opções validas: <S> ou <N>”

MFS\-27019

RN13

__Campo Ind\. Plano Saúde__

Lista de valores válidos:

S – Sim

N – Não

Caso o valor seja diferente da lista de valores válidos, exibir a mensagem: “O campo <<nome funcional do campo>> deve ser preenchido com uma das opções validas: <S> ou <N>”

Outras Validações:

Pelo menos um dos campos Ind Pensão Alimentícia ou Ind\. Plano Saúde, deve estar com a informação igual a ‘S’\. 

Se o campo Ind Pensão Alimentícia estiver preenchido com ‘N’, verificar se o campo Ind Pensão Alimentícia também está preenchido com ‘N’, em caso afirmativo, exibir a mensagem ““Pelo menos um dos indicadores de tipo de dependente deve ser ‘S’\.”

MFS\-27019

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


# MTZ_JOB_SERVIDOR_Carga_Exportacao_Importacao_SAFX283

- **Fonte:** MTZ_JOB_SERVIDOR_Carga_Exportacao_Importacao_SAFX283.docx
- **Modificado:** 2023-04-27
- **Tamanho:** 75 KB

---

THOMSON REUTERS

Regras de Carga, Exportação e Importação \(Online e Batch\) SAFX283 – Retenção no Recebimento \(Evento R\-4080\)

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

Carga 🡪 Programação 🡪 Execução

 Importação 🡪 Programação 🡪 Execução     

 Importação batch 🡪 Programação 🡪 Execução

 Exportação de Dados 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

MFS\-79907

Alessandra Cristina Navatta

Definição das regras de carga, exportação e importação \(online e Batch\) da SAFX283 – Retenção no Recebimento \(Evento R\-4080\)

MFS\-99558

Inclusão de validação 

Inclusão de validação no campo Natureza de Rendimento\.\(RN09\)

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN01

As rotinas de Carga, Importação \(Online e Batch\) e Exportação do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX283 – Retenção no Recebimento \(Evento R\-4080\), que deve ser criada com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Código da Empresa

A

003

SIM

SIM

Código do Estabelecimento

A

006

SIM

SIM

Data do Recebimento

N

008

SIM

SIM

Indicador Pessoa Jurídica

A

001

SIM

SIM

Fonte Pagadora

A

014

SIM

SIM

Natureza do Rendimento

N

005

SIM

SIM

Observações

A

200

NÃO

NÃO

Valor Bruto

N

015V002

SIM

NÃO

Valor Base IR

N

015V002

SIM

NÃO

Valor do Imposto de Renda Retido na Fonte

N

015V002

SIM

NÃO

 

MFS\-79907

RN02

__Sobre as mensagens de erro:__

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

MFS\-79907

RN03

__Mensagens Gerais:__

No processo de carga:

- Se algum campo de preenchimento obrigatório não for enviado, exibir a mensagem: <a id="_Hlk8738371"></a>“<<Nome Funcional do campo>> nao informado”
- Se algum campo receber formato de campo diferente do esperado, exibir a mensagem: “<<Nome Funcional do campo>> com formato invalido\.”
- Se algum campo possuir tamanho maior que o esperado, exibir a mensagem: “A informação do campo <<Nome Funcional do campo>> esta maior do que o tamanho maximo definido”

__Atenção: As mensagens acima, são apenas sugestões\. Pode ser utilizadas mensagens já existentes na tfix22 \(se tiverem o mesmo sentido do cenário exposto\)\.__

MFS\-79907

RN04

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-79907

RN05

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-79907

RN06

__Campo Data do Recebimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão, caso não seja preenchido\.

MFS\-79907

RN07

__Campo Indicador Pessoa Jurídica__

Indicador de Pessoa Física/Jurídica relacionada \(SAFX04\), conforme segue:

1 \- Fornecedor;

2 \- Cliente;

3 \- Estabelecimento;

4 \- Transportadora;

5 \- Cliente/Fornecedor/Transportadora\.

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Indicador Pessoa Jurídica não informado”\. 

MFS\-79907

RN08

__Campo Fonte Pagadora__

Deve ser aceito pessoa jurídica cadastrada na SAFX04 \(campo CPF\_CGC com 14 posições\)\. 

Validações: 

Caso a pessoa não esteja cadastrada na SAFX04, exibir a mensagem: “Registro nao cadastrado na Tabela de Arquivo de Cadastro de Pessoas Físicas/Jurídicas\.“

Caso a pessoa esteja cadastrada, mas, for pessoa física \(campo CPF\_CGC diferente de 14 posições\), exibir a mensagem: “Nao e aceito informacoes de Pessoa Fisica”

MFS\-79907

RN09

__Natureza do Rendimento:__

__Lista de Valores Válidos:__

__Disponibilizar todos os códigos do grupo 20 da taces101:__

20001

Rendimento de Serviços de propaganda e publicidade

20002

Importâncias a título de comissões e corretagens relativas a colocação ou negociação de títulos de renda fixa

20003

Importâncias a título de comissões e corretagens relativas a operações realizadas em Bolsas de Valores e em Bolsas de Mercadorias

20004

Importâncias a título de comissões e corretagens relativas a distribuição de emissão de valores mobiliários, quando a pessoa jurídica atuar como agente da companhia emissora

20005

Importâncias a título de comissões e corretagens relativas a operações de câmbio

20006

Importâncias a título de comissões e corretagens relativas a vendas de passagens, excursões ou viagens

20007

Importâncias a título de comissões e corretagens relativas a administração de cartões de crédito

20008

Importâncias a título de comissões e corretagens relativas a prestação de serviços de distribuição de refeições pelo sistema de refeições\-convênio

20009

Importâncias a título de comissões e corretagens relativas a prestação de serviço de administração de convênios

20010

Demais Importâncias a título de comissões, corretagens, ou qualquer outra importância paga/creditada pela representação comercial ou pela mediação na realização de negócios civis e comerciais

Caso o valor seja diferente da lista de valores válidos, exibir a mensagem: “O campo <<nome funcional do campo>> deve ser preenchido com uma das opções validas: < 20001 > ou <20002 > ou <20003 > ou <20004 > ou <20005 > ou <20006 > ou <20007 > ou <20008 > ou <20009 > ou <20010 >”

Só serão aceitos estes valores e eles devem estar previamente cadastrados na TACES101\. Caso não estejam, exibir a mensagem: “Registro nao cadastrado na Tabela de Natureza de Rendimentos\. “ 

__\[ALTERAÇÃO MFS\-99558\]__ \- Se existir mais de um registro com o mesmo Código da Natureza de Rendimento na taces101, gravar a informação do primeiro registro gravado no banco\. Esta definição de regra foi dada, pois, não estamos considerando neste momento do processo os demais campos chave da taces\.

MFS\-79907

MFS\-99558

RN10

__Campo Observações__

Campo de preenchimento não obrigatório

RN11

__Valor Bruto:__

Este campo deve ser preenchido e com valor maior que zero\. Caso contrário, exibir a mensagem “O campo <<Nome Funcional>> deve ser preenchido com um valor maior que zero\.”

MFS\-79907

RN12

__Valor Base IR:__

Este campo deve ser preenchido e com valor maior que zero\. Caso contrário, exibir a mensagem “O campo <<Nome Funcional>> deve ser preenchido com um valor maior que zero\.”

MFS\-79907

RN13

__Valor do Imposto de Renda Retido na Fonte:__

Este campo deve ser preenchido 

MFS\-79907

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


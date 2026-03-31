# MTZ_JOB_SERVIDOR_Carga_Exportacao_Importacao_SAFX284

- **Fonte:** MTZ_JOB_SERVIDOR_Carga_Exportacao_Importacao_SAFX284.docx
- **Modificado:** 2023-01-04
- **Tamanho:** 76 KB

---

THOMSON REUTERS

 – Processos Administrativos/Judiciais relacionados a não retenção de tributos ou a depósitos judiciais \(Evento R\-4080\)\.

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

MFS\-79907

Alessandra Cristina Navatta

Definição das regras de Carga, Exportação e importação \(Online e Batch\) da SAFX284\.

MFS\-99558

Inclusão de validação 

Inclusão de validação no campo Natureza de Rendimento\.\(RN10\)

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN01

A rotina de carga, exportação e importação \(online e batch\), do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX282 \- Processos Administrativos/Judiciais com Decisão Referente aos Beneficiários não Identificados, que deve ser criada com a seguinte estrutura:

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

A

005

SIM

SIM

Tipo do Processo

A

001

SIM

SIM

Número do Processo

A

021

SIM

SIM

Código do Indicativo da Suspensão de Exigibilidade de Tributos

A

014

NÃO

NÃO

Valor da Base com Exigibilidade Suspensa

N

015V002

NÃO

NÃO

Valor da Retenção que Deixou de ser Efetuada

N

015V002

NÃO

NÃO

 Valor do Depósito Judicial 

N

015V002

NÃO

NÃO

 

A tela de manutenção está disponível em: Módulo: BÁSICOS > DATA WAREHOUSE > Manutenção > Retenção > Retenção no Recebimento / Ícone "Processos R\-4080"

MFS\-[79907](https://jira.thomsonreuters.com/browse/MFS-79893)

RN02

__Sobre as mensagens de erro:__

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

MFS\-79907

RN03

__Mensagens Gerais:__

No processo de carga:

- Se algum campo de preenchimento obrigatório não for enviado, exibir a mensagem: <a id="_Hlk8738371"></a>“<<Nome Funcional do campo>> nao esta informado”
- Se algum campo receber formato de campo diferente do esperado, exibir a mensagem: “<<Nome Funcional do campo>> com formato invalido\.”

Se algum campo possuir tamanho maior que o esperado, exibir a mensagem: “A informação do campo <<Nome Funcional do campo>> esta maior do que o tamanho maximo definido”

__Atenção: As mensagens acima, são apenas sugestões\. Pode ser utilizadas mensagens já existentes na tfix22 \(se tiverem o mesmo sentido do cenário exposto\)\.\.__

MFS\-79907

RN04

__Verificação de existência do registro pai__

Por ser esta tabela filha da SAFX283, no momento da importação deve ser verificada a existência de registro correspondente na tabela pai, considerando as mesmas informações dos campos chave da tabela de origem\. Caso não encontre, retornar a mensagem: “SAFX283 correspondente a SAFX284 não localizada”\.

__Exclusão de Registros__

Ao excluir o registro, todos os registros filhos serão excluídos também\. 

MFS\-79907

RN05

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-[79907](https://jira.thomsonreuters.com/browse/MFS-79893)

RN06

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-[79907](https://jira.thomsonreuters.com/browse/MFS-79893)

RN07

__Campo Data do Recebimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-[79907](https://jira.thomsonreuters.com/browse/MFS-79893)

RN08

__Campo Indicador Pessoa Jurídica__

Indicador de Pessoa Física/Jurídica relacionada \(SAFX04\), conforme segue:

1 \- Fornecedor;

2 \- Cliente;

3 \- Estabelecimento;

4 \- Transportadora;

5 \- Cliente/Fornecedor/Transportadora\.

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Indicador Pessoa Jurídica não informado”\. 

MFS\-[79907](https://jira.thomsonreuters.com/browse/MFS-79893)

RN09

__Campo Fonte Pagadora__

Deve ser aceito pessoa jurídica cadastrada na SAFX04 \(campo CPF\_CGC com 14 posições\)\. 

Validações: 

Caso a pessoa não esteja cadastrada na SAFX04, exibir a mensagem: “Registro nao cadastrado na Tabela de Arquivo de Cadastro de Pessoas Físicas/Jurídicas\.“

Caso a pessoa esteja cadastrada, mas, for pessoa física \(campo CPF\_CGC diferente de 14 posições\), exibir a mensagem: “Nao e aceito informacoes de Pessoa Fisica”

MFS\-[79907](https://jira.thomsonreuters.com/browse/MFS-79893)

RN10

__Campo Natureza do Rendimento__

Lista de Valores Válidos:

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

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

Os códigos devem estar previamente cadastrado na TACES101, caso contrário exibir msg ao usuário\.

__\[ALTERAÇÃO MFS\-99558\]__ \- Se existir mais de um registro com o mesmo Código da Natureza de Rendimento na taces101, gravar a informação do primeiro registro gravado no banco\. Esta definição de regra foi dada, pois, não estamos considerando neste momento do processo os demais campos chave da taces\.

MFS\-[79907](https://jira.thomsonreuters.com/browse/MFS-79893)

MFS\-99558

RN11

__Campo Tipo do Processo__

Tipo do Processo, sendo:

1 \- Administrativo;

2 – Judicial\.

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Tipo do Processo não informado”\. 

O cadastro do processo deve existir na tabela de Processo Administrativo/Judicial \(SAFX2058\), caso contrário exibir msg ao usuário\.

MFS\-[79907](https://jira.thomsonreuters.com/browse/MFS-79893)

RN12

__Campo Número do Processo__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Número do Processo não informado”\. 

O número do processo deve existir na tabela de Processo Administrativo/Judicial \(SAFX2058\), caso contrário exibir msg ao usuário\.

MFS\-[79907](https://jira.thomsonreuters.com/browse/MFS-79893)

RN13

__Campo Código do Indicativo da Suspensão de Exigibilidade de Tributos __

Campo de preenchimento não obrigatório\. 

Caso informado, o Código do Indicativo da Suspensão de Exigibilidade de Tributos deve existir na tabela de Informação de Suspensão de Exigibilidade de Tributos \(SAFX2059\), caso contrário exibir msg ao usuário\. 

MFS\-[79907](https://jira.thomsonreuters.com/browse/MFS-79893)

RN14

__Campo Valor da Base com Exigibilidade Suspensa __

Campo de preenchimento não obrigatório\. Este campo quando preenchido, não pode ser maior que o valor bruto da SAFX283\. Caso o valor seja maior que o valor bruto, exibir a mensagem: “O valor do campo “Valor da Base com Exigibilidade Suspensa” não pode ser maior que o valor do campo “Valor Bruto” da SAFX283 – Retenção no Recebimento

MFS\-[79907](https://jira.thomsonreuters.com/browse/MFS-79893)

RN15

__Campo Valor da Retenção que Deixou de ser Efetuada__

Campo de preenchimento não obrigatório\. 

Validação: Este campo é de preenchimento obrigatório se o campo IND\_DEPOSITO da SAFX2059 for igual a ‘N’\. Caso o campo na safx2059 esteja preenchido com ‘N’ e este campo não seja preenchido, exibir a mensagem: “O campo ‘Valor da Retenção que Deixou de ser Efetuada’ deve ser informado, quando o campo Indicador de Depósito da SAFX2059 for ‘N’\.”

MFS\-[79907](https://jira.thomsonreuters.com/browse/MFS-79893)

Rn16

__Campo Valor do Depósito Judicial__

Campo de preenchimento não obrigatório\. 

Validação: Este campo é de preenchimento obrigatório se o campo IND\_DEPOSITO da SAFX2059 for igual a ‘S’\. Caso o campo na safx2059 esteja preenchido com ‘S’ e este campo não seja preenchido, exibir a mensagem: “O campo ‘Valor do Depósito’ deve ser informado, quando o campo Indicador de Depósito da SAFX2059 for ‘S’\.”

MFS\-[79907](https://jira.thomsonreuters.com/browse/MFS-79893)

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


# MTZ_JOB_SERVIDOR_Carga_Exportacao_Importacao_SAFX282

- **Fonte:** MTZ_JOB_SERVIDOR_Carga_Exportacao_Importacao_SAFX282.docx
- **Modificado:** 2023-01-04
- **Tamanho:** 74 KB

---

THOMSON REUTERS

Regras de Carga, Exportação e Importação \(Online e Batch\) SAFX282 – Processos Relacionados a não Retenção de Tributos \(Evento R\-4040\)

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

Carga à Programação à Execução

 Importação à Programação à Execução     

 Importação batch à Programação à Execução

 Exportação de Dados à Programação à Execução

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

MFS\-[79893](https://jira.thomsonreuters.com/browse/MFS-79893)

Alessandra Cristina Navatta

Definição das regras de Carga, Exportação e importação \(Online e Batch\) da SAFX282\.

MFS\-99558

Inclusão de validação 

Inclusão de validação no campo Natureza de Rendimento\.\(RN08\)

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN01

A rotina de carga, exportação e importação \(online e batch\), do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX282 \- Processos Relacionados a não Retenção de Tributos \(Evento R\-4040\), que deve ser criada com a seguinte estrutura:

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

Data do Movimento

N

008

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

 

A tela de manutenção está disponível em: Módulo: BÁSICOS > DATA WAREHOUSE > Manutenção > Retenção  > Beneficiários Não Identificados  / Ícone "Processos R\-4040"

MFS\-[79893](https://jira.thomsonreuters.com/browse/MFS-79893)

RN02

__Sobre as mensagens de erro:__

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.    

MFS\-[79893](https://jira.thomsonreuters.com/browse/MFS-79893)

RN03

__Mensagens Gerais:__

No processo de carga:

- Se algum campo de preenchimento obrigatório não for enviado, exibir a mensagem: <a id="_Hlk8738371"></a>“<<Nome Funcional do campo>> nao informado”
- Se algum campo receber formato de campo diferente do esperado, exibir a mensagem: “<<Nome Funcional do campo>> com formato invalido\.”
- Se algum campo possuir tamanho maior que o esperado, exibir a mensagem: “A informação do campo <<Nome Funcional do campo>> esta maior do que o tamanho maximo definido”

__Atenção: As mensagens acima, são apenas sugestões\. Pode ser utilizadas mensagens já existentes na tfix22 \(se tiverem o mesmo sentido do cenário exposto\)\.__

MFS\-[79893](https://jira.thomsonreuters.com/browse/MFS-79893)

RN04

__Verificação de existência do registro pai__

Por ser esta tabela filha da SAFX282, no momento da importação deve ser verificada a existência de registro correspondente na tabela pai, considerando as mesmas informações dos campos chave da tabela de origem\. Caso não encontre, retornar a mensagem: “SAFX279 correspondente a SAFX282 não localizada”\.

__Exclusão de Registros__

Ao excluir o registro, todos os registros filhos serão excluídos também\. 

MFS\-[79893](https://jira.thomsonreuters.com/browse/MFS-79893)

RN05

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-[79893](https://jira.thomsonreuters.com/browse/MFS-79893)

RN06

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-[79893](https://jira.thomsonreuters.com/browse/MFS-79893)

RN07

__Campo Data do Movimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Data do Movimento não informada”\. 

MFS\-[79893](https://jira.thomsonreuters.com/browse/MFS-79893)

RN08

__Campo Natureza do Rendimento__

Lista de Valores Válidos:

- 19001;
- 19009’ 

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Natureza do Rendimento não informada”\. 

Os códigos devem estar previamente cadastrado na TACES101, caso contrário exibir msg ao usuário\.

__\[ALTERAÇÃO MFS\-99558\]__ \- Se existir mais de um registro com o mesmo Código da Natureza de Rendimento na taces101, gravar a informação do primeiro registro gravado no banco\. Esta definição de regra foi dada, pois, não estamos considerando neste momento do processo os demais campos chave da taces\.

MFS\-[79893](https://jira.thomsonreuters.com/browse/MFS-79893)

MFS\-99558

RN09

__Campo Tipo do Processo__

Tipo do Processo, sendo:

1 \- Administrativo;

2 – Judicial\.

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Tipo do Processo não informado”\. 

O cadastro do processo deve existir na tabela de Processo Administrativo/Judicial \(SAFX2058\), caso contrário exibir msg ao usuário\.

MFS\-[79893](https://jira.thomsonreuters.com/browse/MFS-79893)

RN10

__Campo Número do Processo__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Número do Processo não informado”\. 

O número do processo deve existir na tabela de Processo Administrativo/Judicial \(SAFX2058\), caso contrário exibir msg ao usuário\.

MFS\-[79893](https://jira.thomsonreuters.com/browse/MFS-79893)

RN11

__Campo Código do Indicativo da Suspensão de Exigibilidade de Tributos __

Campo de preenchimento não obrigatório\. 

Caso informado, o Código do Indicativo da Suspensão de Exigibilidade de Tributos deve existir na tabela de Informação de Suspensão de Exigibilidade de Tributos \(SAFX2059\), caso contrário exibir msg ao usuário\. 

MFS\-[79893](https://jira.thomsonreuters.com/browse/MFS-79893)

RN12

__Campo Valor da Base com Exigibilidade Suspensa __

Campo de preenchimento não obrigatório\. 

MFS\-[79893](https://jira.thomsonreuters.com/browse/MFS-79893)

RN13

__Campo Valor da Retenção que Deixou de ser Efetuada__

Campo de preenchimento não obrigatório\. 

Validação: Este campo é de preenchimento obrigatório se o campo IND\_DEPOSITO da SAFX2059 for igual a ‘N’\. Caso o campo na safx2059 esteja preenchido com ‘N’ e este campo não seja preenchido, exibir a mensagem: “O campo ‘Valor da Retenção que Deixou de ser Efetuada’ deve ser informado, quando o campo Indicador de Depósito da SAFX2059 for ‘N’\.”

MFS\-[79893](https://jira.thomsonreuters.com/browse/MFS-79893)

RN14

__Campo Valor do Depósito Judicial__

Campo de preenchimento não obrigatório\. 

Validação: Este campo é de preenchimento obrigatório se o campo IND\_DEPOSITO da SAFX2059 for igual a ‘S’\. Caso o campo na safx2059 esteja preenchido com ‘S’ e este campo não seja preenchido, exibir a mensagem: “O campo ‘Valor do Depósito’ deve ser informado, quando o campo Indicador de Depósito da SAFX2059 for ‘S’\.”

MFS\-[79893](https://jira.thomsonreuters.com/browse/MFS-79893)

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


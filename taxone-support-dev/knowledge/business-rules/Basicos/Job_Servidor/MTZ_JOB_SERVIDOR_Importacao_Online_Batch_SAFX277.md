# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX277

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX277.docx
- **Modificado:** 2023-04-27
- **Tamanho:** 75 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX277 – Valor de Pagamento e Reeembolsos do Plano de Saúde referente aos Dependentes

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

MFS\-27763

Alessandra Cristina Navatta

Definição das regras de importação, online e Batch, da SAFX277\.

MFS\-79885

Alessandra Cristina Navatta

Alteração do label do campo “Valor Pago ao Plano de Saúde” para “Valor de Dedução do Rendimento Tributável”, esta alteração se faz necessário, para ficar conforme versão 2\.1\.1 do REINF e inclusão de validação sobre a existência de registro pai

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX277 –   Valor de Pagamento e Reembolsos do Plano de Saúde referente aos Dependentes, que deve ser criada com a seguinte estrutura:

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

Código do Fornecedor

A

014

SIM

SIM

Data Início/Inclusão/Alteração \(SAFX04\)

N

008

SIM

SIM

Data Início de Vigência

N

008

SIM

SIM

CPF do Dependente

A

011

SIM

SIM

Número do CNPJ da Operadora

A

014

SIM

SIM

Ind\. Movimento

A

001

SIM

SIM

Data do Pagamento/Apuração

N

008

SIM

SIM

Tipo de Inscrição do Prestador de Serviço

A

001

NÃO

NÃO

Numero de Inscricao do Prestador de Serviço

N

014

NÃO

SIM

Valor de Dedução do Rendimento Tributável 

N

015V002

NÃO

NÃO

Valor do Reembolso do período 

N

015V002

NÃO

NÃO

Valor do Reembolso de anos anteriores 

N

015V002

NÃO

NÃO

 

MFS\-27763

MFS\-79885

RN02

__Sobre as mensagens de erro:__

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

MFS\-27763

RN03

__Mensagens Gerais:__

- Se algum campo de preenchimento obrigatório não for enviado, exibir a mensagem: <a id="_Hlk8738371"></a>“<<Nome Funcional do campo>> nao esta preenchido”
- Se algum campo receber formato de campo diferente do esperado, exibir a mensagem: “<<Nome Funcional do campo>> com formato invalido\.”
- Se algum campo possuir tamanho maior que o esperado, exibir a mensagem: “A informação do campo <<Nome Funcional do campo>> esta maior do que o tamanho áximo definido”

MFS\-27763

RN03\.1

__Verificação de existência do registro pai__

Por ser esta tabela filha da SAFX276, no momento da importação deve ser verificada a existência de registro correspondente na tabela pai, considerando as mesmas informações dos campos chave da tabela de origem\. Caso não encontre, retornar a mensagem: “SAFX276 correspondente a SAFX277 não localizada”\.

__Exclusão de Registros__

Ao excluir o registro, todos os registros filhos serão excluídos também\. 

MFS\-79885

RN04

__Indicador de Pessoa Física/Jurídica__

__Lista de Valores Válidos:__

1 \- Fornecedor;

2 \- Cliente;

3 \- Estabelecimento;

4 \- Transportadora;

5 \- Cliente/Fornecedor/Transportadora\.

Caso o valor seja diferente da lista de valores válidos, exibir a mensagem: “O campo <<nome funcional do campo>> deve ser preenchido com uma das opções validas: <1> , <2>, <3>, <4> ou <5>”

MFS\-27763

RN05

__Campo Código Pessoa Física/Jurídica__

Este campo deve estar previamente na tabela de pessoa física/jurídica \(SAFX04\), além de estar vigente na data Início/Inclusão/Alteração\. Caso o código digitado não exista na Tabela, apresentar a mensagem: “<<Nome funcional do campo>> não está cadastrado na Tabela de Pessoa Física/Jurídica”\.

Só será permitido códigos de pessoa física\. Caso seja informado um código cujo o campo CPF/CNPJ for igual a CNPJ, exibir a mensagem “Não é permitido vincular pagamentos ou reembolsos de Pessoa Jurídica”\.

MFS\-27763

RN06

__Data Início de Vigência__

A data inicio de vigência do dependente deve ser igual ou menor que a data de pagamento\.

Caso contrário, exibir a mensagem: “<<Nome funcional>> deve ser igual ou menor que a data de Pagamento\.”

MFS\-27763

RN07

__Campo CPF do Dependente:__

Validar se é um CPF válido, caso contrário, exibir a mensagem: “<<Nome Funcional do campo>> nao e valido\.”

O CPF do dependente deve estar cadastrado na tabela SAFX275 – Dependentes sem Vínculo e possuir o IND\_PLANO igual a ‘Sim’, caso contrário, exibir a mensagem: “<<Nome funcional do campo>> nao esta cadastrado na Tabela Dependentes sem Vínculo, ou registro nao  possui Ind\. Plano de Saude igual a ‘S’\.” 

MFS\-27763

RN08

__Campo Número do CNPJ da Operadora:__

A operadora deve estar cadastrada na tabela DWT\_OPERADORA\_SAUDE, caso contrário, exibir a mensagem:“<<Nome funcional do campo>> não está cadastrado na Tabela DWT\_OPERADORA\_SAUDE”\.

MFS\-27763

RN09

__Campo Ind\. do Movimento__

__Lista de Valores Válidos:__

P – Pagamento

R – Reembolso

Caso o valor seja diferente da lista de valores válidos, exibir a mensagem: “O campo <<nome funcional do campo>> deve ser preenchido com uma das opções validas: <P> ou <R>”

MFS\-27763

RN10

__Campo Tipo de Inscrição do Prestador de Serviço__

__Lista de Valores Válidos:__

‘‘ – nulo

‘1’ \- Pessoa Jurídica;

‘2’ \- Pessoa Física\. 

Caso o campo não esteja informado corretamente, exibir as mensagens abaixo:

- Caso o valor seja diferente da lista de valores válidos, exibir a mensagem: “O campo <<nome funcional do campo>> deve ser preenchido com uma das opções validas: <’‘>, <’1’>, ou <’2’>”

Se o campo Campo Ind\. do Movimento igual a ‘P’, este campo deve ser branco\. Se o campo Ind\. do Movimento igual a ‘R’, o campo não pode ser branco\.

- Se Campo Ind\. do Movimento igual a ‘P’ e campo diferente de branco\. Exibir a mensagem: “O campo <<nome funcional do campo>> deve ser preenchido com a opção válida: <nulo>\.
- Se Campo Ind\. do Movimento igual a ‘R’ e campo diferente de <’1’> ou <’2’>\. Exibir a mensagem “O campo <<nome funcional do campo>> deve ser preenchido com uma das opções: <’1’> ou <’2’>\.”

MFS\-27763

RN11

__Campo Número de Inscrição do Prestador de Serviço__

Este campo só deve ser preenchido e obrigatório se o campo Tipo de Inscrição do Prestador de Serviço estiver preenchido com 1 ou 2\. Neste cenário, se o campo não estiver preenchido, exibir a mensagem: “<<Nome Funcional do campo>> nao esta preenchido”

Se o campo Ind\. do Movimento = “P” e este campo estiver preenchido, exibir a mensagem: “Campo <<nome funcional do campo>> nao pode ser preenchido com Indicador do Movimento <’P’>\.”

__Outras Validações:__

Se o campo Tipo de Inscrição do Prestador de Serviço for igual a ‘1’, a informação deve conter um CNPJ válido\. Caso o CNPJ esteja inválido, exibir a mensagem <<Nome funcional esta preenchido com CNPJ invalido>>

Se o campo Tipo de Inscrição do Prestador de Serviço for igual a ‘2’, a informação deve conter um CPF válido\. Caso o CPF esteja inválido, exibir a mensagem <<Nome funcional esta preenchido com CPF invalido>>

MFS\-27763

RN12

__Campo Valor Pago ao Plano de Saúde__

Se o campo Ind\. Movimento estiver preenchido com ‘P’ este campo deve ser preenchido\. Caso contrário exibir a mensagem: “<<Nome Funcional do campo>> nao esta preenchido”

Se o campo Ind\. Movimento estiver preenchido com ‘R’, este campo não pode ser preenchido\. Caso o campo esteja preenchido e ind\. movimento igual a ‘R’ exibir a mensagem “O campo <<Nome funcional>> não pode ser preenchido com Ind\. Movimento igual a R”\.

MFS\-27763

RN13

__Campos Valor do Reembolso do período e Valor do Reembolso de anos anteriores__

Se o campo Ind\. Movimento estiver preenchido com ‘R’ pelo menos um dos campos ‘Valor do Reembolso do período’ ou ‘Valor do Reembolso de anos anteriores’ devem ser preenchidos\. Caso contrário exibir a mensagem: “Pelo menos um dos campos Valor do Reembolso do período ou Valor do Reembolso de anos anteriores devem estar preenchidos\.

Se o campo Ind\. Movimento estiver preenchido com ‘P’, nenhum dos campos Valor do Reembolso do período e Valor do Reembolso de anos anteriores devem ser preenchidos\. Caso qualquer dos campos Valor do Reembolso do período e Valor do Reembolso de anos anteriores estiverem preenchidos e ind\. movimento igual a ‘P’ exibir a mensagem: “Campos <<nome funcional do campo>> e <<nome funcional do campo>> não podem ser preenchidos com Ind\. Movimento igual a P”\.

MFS\-27763

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


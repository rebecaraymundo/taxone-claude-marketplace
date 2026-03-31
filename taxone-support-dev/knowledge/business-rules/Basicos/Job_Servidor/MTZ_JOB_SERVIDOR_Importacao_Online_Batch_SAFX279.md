# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX279

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX279.docx
- **Modificado:** 2023-05-23
- **Tamanho:** 75 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX279 – Retenções na Fonte \- Beneficiários Não Identificados

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

Carga à Programação à Execução

 Importação à Programação à Execução     

 Importação batch à Programação à Execução

 Exportação de Dados à Programação à Execução

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

MFS\-27021

Alessandra Cristina Navatta

Definição das regras de carga, exportação e importação \(online e Batch\) da SAFX279 \- Retenções na Fonte \- Beneficiários Não Identificados

MFS\-79893

Alessandra Cristina Navatta

Adequação da SAFX, considerando o layout 2\.1 do REINF

- Aumento do campo Natureza do Rendimento
- Ajuste na lista de valores válidos do campo Natureza do Rendimento
- Inclusão de validação, considerando a lista válida e os códigos devem estar na taces101

MFS\-99558

Inclusão de validação 

Inclusão de validação no campo Natureza de Rendimento\.\(RN07\)

MFS\-535741

Inclusão de campo, validações, alteração de domínio de campo e obrigatoriedades de campos

Para o atendimento do layout 2\.1\.2 do REINF, nesta demanda, ajustamos os seguintes pontos na importação, carga e exportação:

- Inclusão de domínio no campo Natureza de Rendimento, 
- Inclusão de validações nos campos Valor Líquido, Valor Reajustado\. Mudança de label do campo Valor Reajustado para Valor Base IR
- Valor Líquido deixou de ser obrigatório
- Inclusão do campo Data da Escrituração Contábil e validações\. 

Inclusão de validações no botão Confirma

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN01

As rotinas de Carga, Importação \(Online e Batch\) e Exportação do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX279 –   Retenções na Fonte \- Beneficiários Não Identificados, que deve ser criada com a seguinte estrutura:

__\[ALTERAÇÃO MFS\-79983\]__ – Aumento do campo Natureza do Rendimento

__\[ALTERAÇÃO MFS\-535741\]__ – Inclusão do campo Data da Escrituração Contábil

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

N

005

SIM

SIM

Valor Líquido

N

015V002

NÂO

NÃO

Valor Reajustado Valor Base IR

N

015V002

SIM

NÃO

Valor do Imposto de Renda Retido na Fonte

N

015V002

NÃO

NÃO

Descrição 

C

200

SIM

NÃO

Data da Escrituração Contábil

N

008

NÃO

NÃO

 

MFS\-27021

MFS\-79893

MFS\-535741

RN02

__Sobre as mensagens de erro:__

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

MFS\-27021

RN03

__Mensagens Gerais:__

No processo de carga:

- Se algum campo de preenchimento obrigatório não for enviado, exibir a mensagem: <a id="_Hlk8738371"></a>“<<Nome Funcional do campo>> nao informado”
- Se algum campo receber formato de campo diferente do esperado, exibir a mensagem: “<<Nome Funcional do campo>> com formato invalido\.”
- Se algum campo possuir tamanho maior que o esperado, exibir a mensagem: “A informação do campo <<Nome Funcional do campo>> esta maior do que o tamanho maximo definido”

__Atenção: As mensagens acima, são apenas sugestões\. Pode ser utilizadas mensagens já existentes na tfix22 \(se tiverem o mesmo sentido do cenário exposto\)\.__

MFS\-27021

RN04

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-27021

RN05

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-27021

RN06

__Campo Data do Movimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão, caso não seja preenchido\.

MFS\-27021

RN07

__Natureza do Rendimento:__

__\[ALTERAÇÃO MFS\-535741\] – Inclusão da Natureza de Rendimento__

__\[MFS\-79893\] Lista de Valores Válidos:__

1 \- Rendimentos do trabalho;

9 \- Demais rendimentos\.

12052 \- Juros sobre o Capital Próprio cujos beneficiários não estejam identificados no momento do registro contábil

19001 \- Pagamento de remuneração indireta a Beneficiário não identificado

19009 \- Pagamento a Beneficiário não identificado

Caso o valor seja diferente da lista de valores válidos, exibir a mensagem: “O campo <<nome funcional do campo>> deve ser preenchido com uma das opções validas: <12052>,  <19001 > ou <19009> “

Só serão aceitos estes valores e eles devem estar previamente cadastrados na TACES101\. Caso não estejam, exibir a mensagem: “Registro nao cadastrado na Tabela de Natureza de Rendimentos\. “ 

__\[ALTERAÇÃO MFS\-99558\]__ \- Se existir mais de um registro com o mesmo Código da Natureza de Rendimento na taces101, gravar a informação do primeiro registro gravado no banco\. Esta definição de regra foi dada, pois, não estamos considerando neste momento do processo os demais campos chave da taces\.

MFS\-27021

MFS\-79893

MFS\-99558

MFS\-535741

RN08

__Valor Líquido:__

__\[ALTERAÇÃO MFS\-535741\] – Inclusão de validação de acordo com a natureza de rendimento:__

__Natureza de rendimento diferente de ‘19001‘ ou ‘19009’:__

Este campo não deve ser preenchido, quando a natureza de rendimento for diferente de ‘19001‘ ou ‘19009’\. Caso preenchido exibir a mensagem: “O campo <<Nome Funcional>> deve ser preenchido, quando a natureza de rendimento for igual a <19001 > ou <19009>\.”

__Natureza de rendimento igual a ‘19001‘ ou ‘19009’:__

Este campo deve ser preenchido e com valor maior que zero\. Caso contrário, exibir a mensagem “O campo <<Nome Funcional>> deve ser preenchido com um valor maior que zero\.”

MFS\-27021

RN09

__Valor Reajustado Valor Base IR:__

__ALTERAÇÃO MFS\-535741\] – Inclusão de validação de acordo com a natureza de rendimento:__

__Natureza de rendimento diferente de ‘19001‘ ou ‘19009’:__

Quando a natureza de rendimento for diferente de ‘19001’ ou ‘19009’, o campo Valor Base IR, deve ser preenchido e com valor maior que zero\. Caso contrário, exibir a mensagem “O campo <<Nome Funcional>> deve ser preenchido com um valor maior que zero\.”

__Natureza de rendimento igual a ‘19001‘ ou ‘19009’:__

Este campo deve ser preenchido e com valor igual ao resultado da expressão: \(Valor Líquido/0,65\)\. Caso contrário, exibir a mensagem “O campo <<Nome Funcional>> deve ser preenchido com o valor igual a <<Resultado da expressão Valor Líquido/0,65>> \(Valor Líquido/0,65\)\.”

MFS\-27021

MFS\-535741

RN10

__Data da Escrituração Contábil__

Este campo é de preenchimento obrigatório e exclusivo se a natureza de rendimento for igual a ‘12052’\. 

Caso o campo esteja preenchido e a natureza de rendimento for diferente de ‘12052’, exibir a mensagem: “ O campo <<Nome Funcional>> deve ser preenchido quando a natureza de rendimento for igual a ‘12052’”\. 

Caso o campo esteja sem preenchimento e a natureza de rendimento for igual a ‘12052’, exibir a mensagem: “ O campo <<Nome Funcional>> deve ser preenchido\. 

Quando preenchido, a data deve estar compreendida no mês da data do movimento, caso contrário, exibir a mensagem: a data da escrituração contábil deve estar compreendida no período da apuração

MFS\-535741

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


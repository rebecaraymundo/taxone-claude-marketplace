# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX537

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX537.docx
- **Modificado:** 2025-12-22
- **Tamanho:** 86 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX537 – Ficha de Débito 

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

Carga à Programação à Execução

 Importação à Programação à Execução     

 Importação batch à Programação à Execução

 Exportação de Dados à Programação à Execução

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

MFS\-526768

Alessandra Cristina Navatta

Definição das regras de carga, exportação e importação \(online e Batch\) da SAFX537 – Ficha de débito\. Essas informações estarão disponíveis para consulta/edição na tela Digitação da Ficha de Débito, localização DW: Federal >> Obrigações de Tributos Federais >> Outras Obrigações >> DCTF >> DCTF Mensal \(a partir de 01/01/2006\)

localização TAXONE: Federal >> Obrigações de Tributos Federais >> Outras Obrigações >> DCTF Mensal >>

MFS\-543009

Alessandra Cristina Navatta

Inclusão do campo DAT\_PERIOD\_APUR\. Este campo não existe no layout da SAFX \(apenas na tabela definitiva\) e será gerado pelo sistema – RN15

Inclusão de regra para considerar apenas o ano \(no campo de período de referência\) na importação e exportação dos registros da SAFX537\. \(RN01\)

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN01

As rotinas de Carga, Importação \(Online e Batch\) e Exportação do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX537 – Ficha de Débito, que deve ser criada com a seguinte estrutura:

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

Grupo Tributo

A

002

SIM

SIM

Código Receita

A

006

SIM

SIM

Ano Período Apuração

A

004

SIM

SIM

Mês Período Apuração

A

002

NÃO

SIM

Dia Período Apuração

A

002

NÃO

SIM

Valor Débito

N

015V002

SIM

NÃO

Indicador Balanço Redução

N

001

SIM

NÃO

Saldo Dividido 

N

002

SIM

NÃO

Status Operação

A

001

SIM

NÃO

 

__\[ALTERAÇÃO MFS\-543009\]__ __– Período de Referência__

Para a importação e exportação desta SAFX não será considerada a data completa indicada no período de referência destas funcionalidades\. Será considerado apenas o Ano indicado para a importação e exportação destes registros\.

Uma vez importada, as informações poderão ser consultadas na tela: Digitação da Ficha de Débito, 

localização DW: Federal >> Obrigações de Tributos Federais >> Outras Obrigações >> DCTF >> DCTF Mensal \(a partir de 01/01/2006\)

localização TAXONE: Federal >> Obrigações de Tributos Federais >> Outras Obrigações >> DCTF Mensal>> 

MFS\-526768

MFS\-543009

RN02

__Sobre as mensagens de erro:__

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

MFS\-526768

RN03

__Mensagens Gerais:__

No processo de carga:

- Se algum campo de preenchimento obrigatório não for enviado, exibir a mensagem: <a id="_Hlk8738371"></a>“<<Nome Funcional do campo>> nao informado”
- Se algum campo receber formato de campo diferente do esperado, exibir a mensagem: “<<Nome Funcional do campo>> com formato invalido\.”
- Se algum campo possuir tamanho maior que o esperado, exibir a mensagem: “A informação do campo <<Nome Funcional do campo>> esta maior do que o tamanho maximo definido”

__Atenção: As mensagens acima, são apenas sugestões\. Pode ser utilizadas mensagens já existentes na tfix22 \(se tiverem o mesmo sentido do cenário exposto\)\.__

MFS\-526768

RN04

__Verificação de existência de declaração default__

No momento da importação, verificar a existência de um registro de declaração default, de periodicidade mensal, para a empresa \(na tabela dct\_dados\_gerais, campo ind\_decl\_default\)\. 

 Caso não encontre, retornar a mensagem: “Não foi encontrado registro de declaração default, com periodicidade mensal para esta empresa”\.

__Validação de ano competência igual ou maior que 2006__

Ao encontrar a declaração se o ano competência for menor que 2006, exibir a mensagem: “A declaração default, com periodicidade mensal deve ter o ano competência igual ou maior que 2006”\.

MFS\-526768

RN05

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS\-526768

RN06

__Campo Código do Estabelecimento__

O campo é de preenchimento obrigatório, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

Validações:

- Quando o código do tributo for diferente de ‘03’ ou ‘29’, o estabelecimento indicado deve ser o estabelecimento matriz da declaração \(dct\_dados\_gerais\), caso contrário, exibir a mensagem: “Informar o código do estabelecimento matriz da declaração quando o grupo do tributo for diferente de ‘03 – IPI’ ou ‘29 – CIDE’\.” 

MFS\-526768

RN07

__Campo Grupo Tributo__

Campo de preenchimento obrigatório, , deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

O código deve estar previamente cadastrado na TACES15 \- DWT\_TRIBUTO e estar de acordo com a lista de valores válidos\. 

__Lista de Valores Válidos:__

'01\-IRPJ',

'02\-IRRF',

'03\- IPI',

'04\-IOF',

'05\-CSLL',

'06\- PIS/PASEP',

'07\-COFINS',

'08\-CPMF',

'10\-RET/PA',

'29\-CIDE',

'31\-CSRF',

'32\- COSIRF',

'33\- CPSSS',

'34\- CPRB '

Validações:

- Caso não seja encontrado, exibir a mensagem: “<Campo Funcional> não está cadastrado na TACES15 \- DWT\_TRIBUTO\. Localização: BÁSICOS > FERRAMENTAS > Tabelas Internas > Manter > Tabelas > Tributo DCTF”

Caso esteja na tabela, mas, o grupo seja diferente dos valores válidos, exibir a mensagem: “<Campo Funcional> deve ser '01','02','03','04','05','06','07','08','10','29','31','32','33' ou '34'\.”

RN08

__Campo Código Receita__

Campo de preenchimento obrigatório, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\. 

Validações

- O código deve estar previamente cadastrado na Taces14 \(DWT\_CODIGO\_RECEITA\)\. Caso não seja encontrado, exibir a mensagem: “<Campo Funcional> não está cadastrado na TACES14 \- DWT\_CODIGO\_RECEITA\. Localização: BÁSICOS > FERRAMENTAS > Tabelas Internas > Manter > Tabelas > Código de Receita”
- Caso seja encontrado, mas, o código do tributo da DWT\_CODIGO\_RECEITA, não for o mesmo que o informado no campo grupo tributo, exibir a mensagem: “O tributo do código de receita não é igual ao informado no campo Grupo Tributo”
- Se o campo estiver cadastrado na Taces14, o código do tributo do código da receita for igual ao indicado no campo grupo tributo, mas, o campo periodicidade da receita \(campo ind\_periodic, da DWT\_CODIGO\_RECEITA\), estiver sem preenchimento, exibir a mensagem: “<<Campo funcional>>, não possui o indicador de periodicidade informado na TACES14\-DWT\_CODIGO\_RECEITA\. Localização: BÁSICOS > FERRAMENTAS > Tabelas Internas > Manter > Tabelas > Código de Receita”

MFS\-526768

RN09

__Dia Período Apuração__

Este campo é de preenchimento obrigatório e exclusivo se o código de receita tiver periodicidade 'D\-Diário' ou 'S\-Semanal' ou 'X\-Decendial' ou 'Q\-Quinzenal'\.

__Lista de Valores Válidos: __

'01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20', '21','22','23','24','25','26','27','28','29','30', '31'\.

 

Validações:

- Caso periodicidade igual de ‘D\-Diário’ ou ‘S\-Semanal’ ou ‘X\-Decendial’ ou ‘Q\-Quinzenal’ e o campo não estiver preenchido, exibir a mensagem: “<Campo Funcional> deve ser preenchido se a periodicidade for ‘D\-Diário’ ou ‘S\-Semanal’ ou ‘X\-Decendial’ ou ‘Q\-Quinzenal’\.
- Caso periodicidade diferente de ‘D\-Diário’ ou ‘S\-Semanal’ ou ‘X\-Decendial’ ou ‘Q\-Quinzenal’ e o campo estiver preenchido, exibir a mensagem: “<Campo Funcional> não deve ser preenchido se a periodicidade for ‘D\-Diário’ ou ‘S\-Semanal’ ou ‘X\-Decendial’ ou ‘Q\-Quinzenal’
- Se informado um valor diferente do permitido \(de acordo com a lista de valores válidos\), exibir a mensagem: <<Campo funcional>> com valor inválido\!
- Se o dia informado não existir para o mês em questão, exibir a mensagem: <<Campo funcional>> com valor inválido\!

MFS\-526768

RN10

__Mês Período Apuração__

Este campo é de preenchimento obrigatório e exclusivo quando a periodicidade do código de receita for igual D\-Diário’ ou ‘S\-Semanal’ ou ‘X\-Decendial’ ou ‘Q\-Quinzenal’ ou ‘M\-Mensal’

__Lista de Valores Válidos:__

'01', '02', '03', '04', '05', '06', '07', '08', ’09’, '10',’11’ ou ‘12’\.”

Validações:

- Caso periodicidade igual ‘D\-Diário’ ou ‘S\-Semanal’ ou ‘X\-Decendial’ ou ‘Q\-Quinzenal’ ou ‘M\-Mensal’ e o campo não estiver preenchido, exibir a mensagem: “<Campo Funcional> deve ser preenchido se a periodicidade for ‘D\-Diário’ ou ‘S\-Semanal’ ou ‘X\-Decendial’ ou ‘Q\-Quinzenal’ ou ‘M\-Mensal’\.
- Caso periodicidade diferente de ‘D\-Diário’ ou ‘S\-Semanal’ ou ‘X\-Decendial’ ou ‘Q\-Quinzenal’ ou ‘M\-Mensal’ e o campo estiver preenchido, exibir a mensagem: “<Campo Funcional> não deve ser preenchido se a periodicidade for diferente de ‘D\-Diário’ ou ‘S\-Semanal’ ou ‘X\-Decendial’ ou ‘Q\-Quinzenal’ ou ‘M\-Mensal’\.
- Se o valor informado, não estiver na lista dos valores válidos, exibir a mensagem: “<Campo Funcional> deve ser '01', '02', '03', '04', '05', '06', '07', '08', ’09’, '10',’11’ ou ‘12’\.”

MFS\-526768

RN11

__Valor Débito__

Este campo deve ser maior que zero, caso contrário, exibir a mensagem: “<Campo Funcional> deve ser maior que 0\(zero\)\."

MFS\-526768

RN12

__Balanço Redução__

Este campo é de preenchimento obrigatório, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\. 

__Lista de Valores Válidos:__

0 – Sem Balanço de Redução

1 \- Com Balanço de Redução

Validação:

- Se o valor informado, não estiver na lista dos valores válidos, exibir a mensagem: “<Campo Funcional> deve ser ‘0’ ou  ‘1’\.”

Se o grupo do tributo for diferente de 01 ou 05 e a periodicidade do código da receita for diferente de M\-Mensal e o campo for preenchido com 1 – Com balanço, caso contrário, exibir a mensagem: “<<Campo Funcional>> só é permitido ser ‘1’, quando o grupo do tributo for 01\-IRPJ ou 05\-CSLL com periodicidade do código de receita igual a mensal”\.

MFS\-526768

RN13

__Status da Operação__

Campo de preenchimento obrigatório, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\. 

__Lista de Valores Válidos:__

1 – Pendente

2 – Em andamento

3 \- Liquidado

- Se o valor informado, não estiver na lista dos valores válidos, exibir a mensagem: “<Campo Funcional> deve ser '1', '2' ou ‘3’\.”

MFS\-526768

RN14

__Saldo Dividido__

Campo de preenchimento obrigatório, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\. 

__Lista de Valores Válidos:__

0 – Sem divisão em quotas

1 \- Com divisão em quotas

Validação:

- Se o valor informado, não estiver na lista dos valores válidos, exibir a mensagem: “<Campo Funcional> deve ser ‘0’ ou  ‘1’\.”
- Só pode informado ‘1 \- Com divisão em quotas’ quando o Grupo Tributo \(grp\_tributo\) for igual a ‘01’ ou ‘05’, com periodicidade do código de receita ‘Trimestral’ e o valor do débito for maior ou igual a R$2\.000,00, caso contrário, exibir a mensagem: “<<campo funcional>> pode ser ‘1\-Com divisao em quotas’,quando o Grupo Tributo for ‘01\-IRPJ’ ou ‘05\-CSLL’,com period\. cod\. receita ‘Trimestral’ e o valor do debito for maior ou igual a R$2\.000,00

MFS\-526768

RN15

__Criar o campo DAT\_PERIOD\_APUR apenas na tabela definitiva__

Este campo não faz parte do layout da SAFX, apenas será criado na tabela definitiva\. Ele foi criado para permitir a exclusão dos registros da tabela definitiva\(__Localização__: Menu Básico, módulo Ferramentas, menu Rotinas Acessórias 🡪 Inicialização 🡪 Exclusão de Tabelas Definitivas 🡪 Movimentos\)\.

Tipo: Data

Formato: DDMMAAAA

Tamanho:08

Este campo será gerado pelo sistema, de acordo com as informações dos campos: Dia Período Apuração, Mês Período Apuração e Ano Período Apuração, seguindo as regras:

__Se os campos Dia Período Apuração, Mês Período Apuração estiverem preenchidos com valores diferentes de ‘00’, gravar o campo com as informações dos campos: __

‘Informação do Dia Período Apuração’‘Informação do Mês Período Apuração’‘Informação do Ano Período Apuração’

__Se o campo Dia Período Apuração estiver preenchido com ‘00’ e os campos Mês Período Apuração e Ano Período estiverem preenchidos com informação diferente de ‘00’ e ‘0000’, respectivamente, gravar o campo com:__

‘01’‘Informação do Mês Período Apuração’‘Informação do Ano Período Apuração’

__Se os campos Dia Período Apuração e Mês Período Apuração estiverem preenchidos com ‘00’, gravar o campo com:__

‘01‘01‘Informação do Ano Período Apuração’

__Orientações para a Limpeza dos Registros da tabela: __

A exclusão dos registros não será pela data da declaração e sim pelo período do movimento do registro \(campos Dia Período Apuração, Mês Período Apuração, Ano Período Apuração\)\.

Para os registros que não são informados o dia, para concretizar a exclusão, obrigatoriamente deverá ser indicado o campo \(dia\) como ‘01’\.

Já os registros que não possuem as informações de dia e mês, obrigatoriamente esses campos deverão ser indicados com ‘01’\.

MFS\-543009

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX539

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX539.docx
- **Modificado:** 2025-01-09
- **Tamanho:** 97 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX539 – Pagamentos dos Débitos 

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

Carga à Programação à Execução

 Importação à Programação à Execução     

 Importação batch à Programação à Execução

 Exportação de Dados à Programação à Execução

	

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

MFS\-661904

Alessandra Cristina Navatta

Definição das regras de carga, exportação e importação \(online e Batch\) da SAFX539 –Pagamentos dos Débitos\. Essas informações estarão disponíveis para consulta/edição na tela Pagamento de Débitos, localização DW: Federal >> Obrigações de Tributos Federais >> Outras Obrigações >> DCTF >> DCTF Mensal \(a partir de 01/01/2006\)

localização TAXONE: Federal >> Obrigações de Tributos Federais >> Outras Obrigações >> DCTF Mensal >>

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN01

As rotinas de Carga, Importação \(Online e Batch\) e Exportação do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX539 – Pagamentos dos Débitos, que deve ser criada com a seguinte estrutura:

__Campos__

__Tam\.__

__Tipo__

__Obrig\.__

__Chave__

Código da Empresa

003

A

S

S

Código do Estabelecimento

006

A

S

S

Grupo Tributo

002

A

S

S

Código Receita

006

A

S

S

Ano Período Apuração

004

A

S

S

Mês Período Apuração

002

A

N

S

Dia Período Apuração

002

A

N

S

Pagamento

001

A

S

S

Seq

005

N

N

S

Data Apuração

008

N

N

N

CPF/CNPJ

014

A

N

N

DARF

004

A

N

N

Data Venc\.

008

N

N

N

Quitação

008

N

N

N

Vlr Principal

015V002

N

N

N

Vlr Multa

015V002

N

N

N

Vlr Juros

015V002

N

N

N

Vlr Operação

015V002

N

S

N

Num Ref

017

A

N

N

Formalização Pedido

001

A

N

N

Processo/Dcomp

024

A

N

N

Motivo Suspensão

002

N

N

N

Cód\. Vara

002

A

N

N

Estado

002

A

N

N

Município

005

N

N

N

Depósito

001

N

N

N

Identificação do Depósito

020

A

N

N

 

Uma vez importada, as informações poderão ser consultadas na tela: Pagamento de Débitos, 

localização DW: Federal >> Obrigações de Tributos Federais >> Outras Obrigações >> DCTF >> DCTF Mensal \(a partir de 01/01/2006\)

localização TAXONE: Federal >> Obrigações de Tributos Federais >> Outras Obrigações >> DCTF Mensal>> 

MFS\-661904

RN02

__Sobre as mensagens de erro:__

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

MFS\-661904

RN03

__Mensagens Gerais:__

No processo de carga:

<a id="_Hlk8738371"></a>

- Se algum campo numérico receber formato de campo diferente do esperado, exibir a mensagem <<90461>>: “Valor decimal ou numérico com formato invalido\.”

__Atenção: A mensagem acima, é apenas uma sugestão\. Pode ser utilizadas mensagens já existentes na tfix22 \(se tiverem o mesmo sentido do cenário exposto\)\.__

MFS\-661904

RN04

__Verificação de existência de declaração default__

- No momento da importação, verificar a existência de um registro da ficha de débito para o estabelecimento e período de apuração em questão\.

 Caso não encontre, retornar a mensagem <<93683>>: “Não foi encontrado registro de ficha de débito para esta apuração e estabelecimento”\.

- Se não for encontrada declaração default com periodicidade mensal, exibir a mensagem <<93577>>: “Nao foi encontrado registro de declaracao default, com periodicidade mensal para esta empresa\.”

MFS\-661904

RN05

__Campo Código da Empresa__

Validação

- Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão <<90001>> caso esse campo não esteja preenchido\.

MFS\-661904

RN06

__Campo Código do Estabelecimento__

Validações

- O campo é de preenchimento obrigatório, deve ser exibida mensagem de erro padrão <<90002>> caso esse campo não esteja preenchido\.
- Quando o código do tributo for diferente de ‘03’ ou ‘29’, o estabelecimento indicado deve ser o estabelecimento matriz da declaração \(dct\_dados\_gerais\), caso contrário, exibir a mensagem <<93581>>: “Informar o código do estabelecimento matriz da declaração quando o grupo do tributo for diferente de ‘03 – IPI’ ou ‘29 – CIDE’\.” 

MFS\-661904

RN07

__Campo Grupo Tributo__

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

Validações

- Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão <<93578>>caso esse campo não esteja preenchido\.
- Caso não seja encontrado, exibir a mensagem<<93580>>: “<Nome Funcional do Campo> não está cadastrado na TACES15 \- DWT\_TRIBUTO\. Localização: BÁSICOS > FERRAMENTAS > Tabelas Internas > Manter > Tabelas > Tributo DCTF”

Caso esteja na tabela, mas, o grupo seja diferente dos valores válidos, exibir a mensagem<<93579>>: “<Nome Funcional do Campo> deve ser '01','02','03','04','05','06','07','08','10','29','31','32','33' ou '34'\.”

MFS\-661904

RN08

__Campo Código Receita__

Validações

- Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.
- O código deve estar previamente cadastrado na Taces14 \(DWT\_CODIGO\_RECEITA\)\. Caso não seja encontrado, exibir a mensagem <<93585>>: “<Nome Funcional do Campo> não está cadastrado na TACES14 \- DWT\_CODIGO\_RECEITA\. Localização: BÁSICOS > FERRAMENTAS > Tabelas Internas > Manter > Tabelas > Código de Receita”
- Caso seja encontrado, mas, o código do tributo da DWT\_CODIGO\_RECEITA, não for o mesmo que o informado no campo grupo tributo, exibir a mensagem<<93583>>: “O tributo do código de receita não é igual ao informado no campo Grupo Tributo”
- Se o campo estiver cadastrado na Taces14, o código do tributo do código da receita for igual ao indicado no campo grupo tributo, mas, o campo periodicidade da receita \(campo ind\_periodic, da DWT\_CODIGO\_RECEITA\), estiver sem preenchimento, exibir a mensagem<<93584>>: “<<Nome Funcional do Campo>>, não possui o indicador de periodicidade informado na TACES14\-DWT\_CODIGO\_RECEITA\. Localização: BÁSICOS > FERRAMENTAS > Tabelas Internas > Manter > Tabelas > Código de Receita”

MFS\-661904

RN09

__Ano Período Apuração__

Este campo é de preenchimento obrigatório, caso não preenchido, exibir a mensagem<<93590>>: “"<<Nome Funcional do Campo>> deve ser preenchido”

MFS\-661904

RN10

__Mês Período Apuração__

__Lista de Valores Válidos:__

'01', '02', '03', '04', '05', '06', '07', '08', ’09’, '10',’11’ ou ‘12’\.”

Validações

- Este campo é de preenchimento obrigatório e exclusivo quando a periodicidade do código de receita for igual D\-Diário’ ou ‘S\-Semanal’ ou ‘X\-Decendial’ ou ‘Q\-Quinzenal’ ou ‘M\-Mensal’
- Caso periodicidade igual ‘D\-Diário’ ou ‘S\-Semanal’ ou ‘X\-Decendial’ ou ‘Q\-Quinzenal’ ou ‘M\-Mensal’ e o campo não estiver preenchido, exibir a mensagem<<93588>>: “<Nome Funcional do Campo> deve ser preenchido se a periodicidade for ‘D\-Diário’ ou ‘S\-Semanal’ ou ‘X\-Decendial’ ou ‘Q\-Quinzenal’ ou ‘M\-Mensal’\.
- Caso periodicidade diferente de ‘D\-Diário’ ou ‘S\-Semanal’ ou ‘X\-Decendial’ ou ‘Q\-Quinzenal’ ou ‘M\-Mensal’ e o campo estiver preenchido, exibir a mensagem<<93606>>: “<Nome Funcional do Campo> não deve ser preenchido se a periodicidade for diferente de ‘D\-Diário’ ou ‘S\-Semanal’ ou ‘X\-Decendial’ ou ‘Q\-Quinzenal’ ou ‘M\-Mensal’\.
- Se o valor informado, não estiver na lista dos valores válidos, exibir a mensagem <<93589>>: “<Nome Funcional do Campo> com valor inválido”

MFS\-661904

RN11

__Dia Período Apuração__

__Lista de Valores Válidos: __

'01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20', '21','22','23','24','25','26','27','28','29','30', '31'\.

 

Validações

- Este campo é de preenchimento obrigatório e exclusivo se o código de receita tiver periodicidade 'D\-Diário' ou 'S\-Semanal' ou 'X\-Decendial' ou 'Q\-Quinzenal'\.
- Caso periodicidade igual de ‘D\-Diário’ ou ‘S\-Semanal’ ou ‘X\-Decendial’ ou ‘Q\-Quinzenal’ e o campo não estiver preenchido, exibir a mensagem<<93586>>: “<Nome Funcional do Campo> deve ser preenchido se a periodicidade for ‘D\-Diário’ ou ‘S\-Semanal’ ou ‘X\-Decendial’ ou ‘Q\-Quinzenal’\.
- Caso periodicidade diferente de ‘D\-Diário’ ou ‘S\-Semanal’ ou ‘X\-Decendial’ ou ‘Q\-Quinzenal’ e o campo estiver preenchido, exibir a mensagem<<93607>>: “<Nome Funcional do Campo> não deve ser preenchido se a periodicidade for ‘D\-Diário’ ou ‘S\-Semanal’ ou ‘X\-Decendial’ ou ‘Q\-Quinzenal’
- Se informado um valor diferente do permitido \(de acordo com a lista de valores válidos\), exibir a mensagem<<93587>>: <<Nome Funcional do Campo>> com valor inválido\!
- Se o dia informado não existir para o mês em questão, exibir a mensagem<<93587>>: <<Nome Funcional do Campo>> com valor inválido\!

MFS\-661904

RN12

__Pagamento__

__Opções Válidas:__

1\- Compensacoes;

2 \- Deducao com DARF;

3 \-  Pagamento do Debito Parcial;

4 \-  Pagamento do Debito Total;

5 \- Parcelamento do Debito;

6 \- Suspensao do Debito\.

Validações

- Como o campo é obrigatório de preenchimento, deve ser exibida mensagem <<93671>> de erro padrão caso esse campo não esteja preenchido\.
- Quando o campo estiver preenchido com uma opção não válida, exibir a mensagem <<93672>>: "<<Nome Funcional do Campo>> deve ser preenchido com <<1>> ou <<2>> ou <<3>> ou <<4>> ou <<5>> ou <<6>>"
- Quando Pagamento = 2, Grupo Tributo diferente de 29' OU Código Receita diferente de ‘933101’ E ‘874101’, exibir a mensagem<<93673>>: "Pagamento inválido para este grupo de tributo"\. 

Atenção\! Ao importar um registro com Pagamento = Pagamento do Debito Parcial ou Pagamento do Debito Total, se for informado o campo Seq = 1 e Vlr Principal igual ao Valor Débito, será considerado ‘Pagamento do Debito Total’, na importação e recuperação/consulta do registro na tela\. Essa necessidade surgiu, pois, a tabela que armazena esses registros é única e na tela, estava sendo exibido nos dois pagamentos: “Pagamento do Debito Parcial” e “Pagamento do Debito Total”, dando a impressão de duplicidade de registros\.

MFS\-661904

RN13

__Seq__

Validações

- Este campo é de preenchimento obrigatório e deve ser maior que zero, quando o Pagamento igual a <<1>>, e/ou <<2>>, e/ou <<3>>, e/ou <<6>>\. Se o pagamento for igual a <<1>>, e/ou <<2>>, e/ou <<3>>, e/ou <<6>> e o campo não estiver preenchido ou não for maior que zero, exibir a mensagem <<93674>>: <<Nome Funcional do Campo>> deve ser preenchido com número maior que zero\. 
- Se o pagamento for diferente de <<1>>, e/ou <<2>>, e/ou <<3>>, e/ou <<6>>  e estiver preenchido com informação maior que zero, exibir a mensagem <<93675>>: <<Nome Funcional do Campo>> só deve ser preenchido e com número maior que zero, quando pagamento for <<1>>, e/ou <<2>>, e/ou <<3>>

MFS\-661904

RN14

__Data Apuração__

Validações

- Se a data não for válida, exibir a mensagem <<92676>>: “<< Nome funcional do Campo>> inválida\.”
- Este campo não deve ser preenchimento quando Pagamento igual a <<5>>\. Se preenchido, exibir a mensagem<<93676>>: <<Nome Funcional do Campo>> não pode ser preenchida, quando Pagamento igual a <<5>>
- Este campo deve ser preenchimento quando Pagamento igual a 2, 3 e/ou 4\. Se não preenchido, exibir a mensagem<<93677>>: <<Nome Funcional do Campo>> deve ser preenchida, quando Pagamento igual a <<2>> ou <<3>> ou <<4>>\.
- Quando pagamento = 6, este campo só deve ser preenchido se Depósito igual a 2\. Caso não seja atendida a condição, exibir a mensagem<<93678>>: “Quando o Pagamento for igual a <<6>>, Data da Apuracao só deve ser preenchida quando Depósito igual a <<2>>”

MFS\-661904

RN15

__CPF/CNPJ__

Regra: Quando Pagamento = 3 ou 4, considerar a informação do campo 05 \- CGC da tabela estabelecimento \(SAFX2064\)

Validações

- Este campo só deve ser preenchido, quando Pagamento igual a 1, 2 ou 6 \. Se o campo estiver preenchido e pagamento for diferente de 1,2 ou 6, exibir a mensagem <<93679>>: "<<Nome Funcional do Campo>> só deve ser preenchido, quando o campo Pagamento estiver preenchido com <<1>> ou << 2>> ou <<6>>"\.
- Este campo deve ser preenchido, quando Pagamento igual a  1, 2 ou 6, caso não esteja preenchido,  exibir a mensagem <<93680>>: "<<Nome Funcional do Campo>>  deve ser preenchido, quando o campo Pagamento estiver preenchido com <<1>> ou << 2>> ou <<6>>"\.
- Quando preenchido o CPF, este  deve ser um valor válido, caso contrário, exibir a mensagem: <<90063>>
- Quando preenchido o CNPJ  , este deve ser um valor válido, caso contrário, exibir a mensagem: <<90082>>
- Quando pagamento = 6, este campo só deve ser preenchido se Depósito igual a 2\. Caso não seja atendida a condição, exibir a mensagem<<93681>>: “Quando o Pagamento for igual a <<6>>, <<Nome Funcional do Campo>> só deve ser preenchida quando Depósito igual a <<2>>”

MFS\-661904

RN16

__DARF__

Validações

- Este campo só deve ser preenchido, quando Pagamento igual 1,2,3,4 e 6\.   
Se o campo estiver preenchido e pagamento for 5, exibir a mensagem <<93682>>: "<<Nome Funcional do Campo>> só deve ser preenchido, quando o campo Pagamento estiver preenchido com <<1>> ou << 2>> ou <<3>> ou <<4>> ou <<6>>"\.
- Se Pagamento igual a 1,3 ou 4 e o campo não estiver preenchido, exibir a mensagem<<90120>>: "<<Nome Funcional do Campo>> deve ser preenchido”

Quando Pagamento = 1, 3 ou 4

- Se não encontrar um grupo válido para o Darf, relacionado com a empresa, estabelecimento, tabela X2019\_COD\_DARF e data da apuração, exibir a mensagem<<90476>>: “Não foi possível recuperar para o estabelecimento o grupo de centralização do Código de Receitas \- DARF\.”
- Se não encontrar o Darf informado, para o grupo recuperado, exibir a mensagem <<90126>>: “O Código do DARF não esta cadastrado\.”

Quando Pagamento = 6

- Este campo só deve ser preenchido se Depósito igual a 2\. Caso não seja atendida a condição, exibir a mensagem<<93684>>: “Quando o Pagamento for igual a <<6>>, <<Nome Funcional do Campo>> só deve ser preenchida quando Depósito igual a <<2>>”

MFS\-661904

RN17

__Data Venc__

Validações

- Campo de preenchimento obrigatório, quando Pagamento igual a 1,2,3,4\. Neste caso,  se não estiver preenchido este campo, exibir a Mensagem<<90524>>: "Data de Vencimento deve ser preenchida"
- Se o campo estiver preenchido e pagamento igual a 5, exibir a mensagem <<93685>>: “<<Nome Funcional do Campo>> só deve ser preenchida quando o campo Pagamento estiver preenchido com <<1>> ou <<2>> ou <<3>> ou <<4>> ou <<6>>"\.
- Quando Pagamento = 6, este campo só deve ser preenchido se Depósito igual a 2\. Caso não seja atendida a condição, exibir a mensagem<<93686>>: “Quando o Pagamento for igual a <<6>>, a Data de Vencimento so deve ser preenchida quando Deposito igual a <<2>>”
- Se o campo tiver um formato inválido, exibir a mensagem <<90923>>: “O Campo Data de Vencimento e invalido”

MFS\-661904

RN18

__Quitação__

Validação

- Se o campo estiver preenchido e pagamento igual a 5 ou 6, exibir a mensagem <<93687>>: "<<Nome Funcional do Campo>> só deve ser preenchida quando o campo Pagamento estiver preenchido com <<1>> ou <<2>> ou <<3>> ou <<4>>"
- Se o campo for preenchido, com formato inválido, exibir a mensagem<<93720>>: “O campo Quitacao e invalido”

MFS\-661904

RN19

__Vlr Principal__

Validações

- Este campo só deve ser preenchido, quando Pagamento igual a 1 ,2,3,4 ou 6  
Se o campo estiver preenchido e pagamento for igual a 5, exibir a mensagem <<93688>>: "<<Nome Funcional do Campo>>  só deve ser preenchido, quando o campo Pagamento estiver preenchido com <<1>> ou <<2>> ou <<3>> ou <<4>> ou <<6>>"
- Se Pagamento igual a 2 e não estiver preenchido, ou menor que zero exibir a mensagem <<93689>>: "<<Nome Funcional do Campo>> deve ser deve ser maior que Zero\.” 
- Quando Pagamento = 3 ou 4 e Quota maior que zero e Vlr Principal menor que 1000, exibir a mensagem<<93690>>: “<<Nome Funcional do Campo>> por Quota, não pode ser inferior a 1\.000,00\.”

Quando Pagamento = 6

- Este campo só deve ser preenchido se Depósito igual a 2\. Caso não seja atendida a condição, exibir a mensagem<<93691>>: “Quando o Pagamento for igual a <<6>>, o Valor Principal so deve ser preenchida quando Deposito igual a <<2>>”

MFS\-661904

RN20

__Vlr Multa__

Validação

- Este campo só deve ser preenchido, quando Pagamento igual a 1, 2, 3, 4 ou 6  
Se o campo estiver preenchido e pagamento for igual a 5, exibir a mensagem<<93692>>: "<<Nome Funcional do Campo>> só deve ser preenchido, quando o campo Pagamento estiver preenchido com <<1>> ou <<2>> ou <<3>> ou <<4>> ou <<6>>"

Quando Pagamento = 6

- Este campo só deve ser preenchido se Depósito igual a 2\. Caso não seja atendida a condição, exibir a mensagem<<93693>>: “Quando o Pagamento for igual a <<6>>, o Valor Multa so deve ser preenchida quando Deposito igual a <<2>>”

MFS\-661904

RN21

__Vlr Juros__

Validação

- Este campo só deve ser preenchido, quando Pagamento igual a 1 ,2,3,4 ou 6  
Se o campo estiver preenchido e pagamento for igual a 5, exibir a mensagem <<93694>>: "<<Nome Funcional do Campo>> só deve ser preenchido, quando o campo Pagamento estiver preenchido com <<1>> ou <<2>> ou <<3>> ou <<4>> ou <<6>>"

Quando Pagamento = 6

- Este campo só deve ser preenchido se Depósito igual a 2\. Caso não seja atendida a condição, exibir a mensagem<<93695>>: “Quando o Pagamento for igual a <<6>>, o Valor dos Juros so deve ser preenchida quando Deposito igual a <<2>>”

MFS\-661904

RN22

__Vlr Operação__

Orientações de Preenchimento:

Conforme orientações abaixo:

Quando, Pagamento igual a '1\- Compensacoes', o valor é referente a compensação; 

Quando, Pagamento igual a '2 \- Deducao com DARF', o valor é referente ao valor deduzido do débito;

Quando, Pagamento igual a '3 \-  Pagamento do Debito Parcial';o valor é referente ao valor do pagamento;

Quando, Pagamento igual a '4 \-  Pagamento do Debito Total';o valor é referente ao valor do pagamento;

Quando, Pagamento igual a '5 \- Parcelamento do Debito';o valor é referente ao valor do parcelamento;

Quando, Pagamento igual a '6 \- Suspensao do Debito'o valor é referente ao valor de suspensão\.

Validações

- Quando pagamento = 1 ,3 ou 4 e o campo estiver sem preenchimento ou menor que zero, exibir a mensagem<<93696>>: “<<Nome Funcional do Campo>> \(Vlr Principal \+ Vlr Multa \+ Vlr Juros\) tem que ser maior que Zero\.”
- Quando pagamento = 2, 5 ou 6, se o campo não preenchido ou menor que zero, exibir a mensagem<<93697>>: “<<Nome Funcional do Campo>> tem que ser maior que Zero\.” 
- Quando Pagamento = 3 ou 4 e Quota maior que zero e Vlr Operação menor que 1000, exibir a mensagem<<93698>>: “<<Nome Funcional do Campo>> por Quota, não pode ser inferior a 1\.000,00\.”

MFS\-661904

RN23

__Num Ref__

Validação

- Se o campo estiver preenchido e pagamento igual a 5 ou 6, exibir a mensagem <<93699>>: "<<Nome Funcional do Campo>> só deve ser preenchido quando o campo Pagamento estiver preenchido com <<1>> ou <<2>> ou <<3>> ou <<4>>"

MFS\-661904

RN24

__Formalização Pedido__

Se Pagamento igual a 1 \- Compensacoes:

Opções Válidas:

1 \- Processo Administrativo

3 \- DComp

4 \- DComp com Direito Creditório Reconhecido em Processo

Se Pagamento = 5 \- Parcelamento do Debito

Opções Válidas:

1 \- Processo Administrativo

5\- Parcelamento

Validações

- Este campo só deve ser preenchido, quando Pagamento igual a 1 ou 5\. Caso preenchido e Pagamento diferente de 1 ou 5, exibir a mensagem <<93700>>: "<<Nome Funcional do Campo>> só deve ser preenchido quando o campo Pagamento estiver preenchido com <<1>> ou <<5>>"

Validação das informações válidas:  

- Se for Pagamento igual a 1, e for preenchido com informação inválida, exibir a mensagem <<93701>>: "<<Nome Funcional do Campo>> deve ser preenchido com <<1>> ou <<3>> ou <<4>> "
- Se for Pagamento igual a 5, e for preenchido com informação inválida, exibir a mensagem <<93702>>: "<<Nome Funcional do Campo>> deve ser preenchido com <<1>> ou <<5>>”
- Quando Pagamento = 1 e Formalização Pedido for igual a '3 \- DComp,' valida:

Validar o DV do CPF ou CNPJ\. Caso o DV não esteja correto, mensagem <<93703>>: “CPF/CNPJ do DARF Inválido\.”

MFS\-661904

RN25

__Processo/Dcomp__

Validações

- Campo de preenchimento obrigatório quando Pagamento igual a 1 ou 5\. Caso Pagamento igual a 1, 5 e não preenchido, exibir a mensagem <<93704>>: "<<Nome Funcional do Campo>> deve ser preenchido "
- Se o campo estiver preenchido e pagamento for diferente de 1, 5 ou 6, exibir a mensagem <<93705>>: "<<Nome Funcional do Campo>> só deve ser preenchido, quando o campo Pagamento estiver preenchido com 1, 5 ou 6"\.
- Quando Pagamento = 6 e Motivo Suspensão diferente de 7: 

Se Processo estiver nulo ou zerado, mensagem<<93704>>: “ <<Nome Funcional do Campo>> deve ser preenchido\.’ 

- Quando pagamento = 6 , Motivo Suspensão igual a 7 e Processo/Dcomp preenchido, exibir a mensagem <<93706>>: “Quando o Pagamento for igual a <<6>>, o Processo/DComp nao deve ser preenchido quando Motivo de Suspensao igual a <<7>>”

MFS\-661904

RN26

__Motivo Suspensão__

Opções Válidas:

1 \- Liminar em Mandado de Segurança  

2 \- Depósito Judicial do Montante Integral 

3 \- Antecipação de Tutela 

4 \- Liminar em Medida Cautelar 

5 \- Depósito Administrativo do Montante Integral 

6 \- Outros 

7 \- Medida Judicial em que o declarante não é o autor  

8 \- Sentença em Mandado de Segurança favorável ao contribuinte 

9 \- Sentença em Ação Ordinária favorável ao contribuinte e confirmada pelo TRF 

10 \- Acórdão do TRF favorável ao contribuinte 

11 \- Acórdão do STJ em Recurso Especial favorável ao contribuinte 

12 \- Acórdão do STF em Recurso Extraordinário favorável ao contribuinte

Validações

- Este campo só pode ser preenchido se Pagamento = 6, caso preenchido com informação diferente de 6, exibir a mensagem<<93707>>: “<<Nome Funcional do Campo>> só deve ser preenchido, quando Pagamento igual a <<6>>\.”
- Se o campo for preenchido, com uma opção inválida, exibir a mensagem <<93708>>: “<<Nome Funcional do Campo>> deve ser preenchido com <<1>> ou <<2>> ou <<3>> ou <<4>> ou <<5>> ou <<6>> ou <<7>> ou <<8>> ou <<9>> ou <<10>> ou <<11>> ou <<12>>\.”
- Se ano\_compet \+ trim\_compet >= 2014\-08: motivo suspensão não pode ser 5 e 6 neste caso, exibir a mensagem <<93709>>: “"A partir de Agosto/2014, as opções de <<Nome do Campo Funcional>> <<5>> ou <<6>> não devem ser utilizadas\."
- Se ano\_compet \+ trim\_compet < 2014\-08: motivo suspensão não pode ser 8, 9, 10, 11 e 12

neste caso, exibir a mensagem<<93710>>: Antes de Ago/2014, não pode ser usada as opções  de <<Nome do Campo Funcional>> <<08>> ou <<9>> ou <<10>> ou <<11>> ou <<12>>\.

MFS\-661904

RN27

__Cód Vara__

Validações

- Este campo só pode ser preenchido se Pagamento = 6 e motivo Suspensão diferente de 5 ou 7, caso contrário, exibir a mensagem <<93711>>: “<<Nome Funcional do Campo>> só deve ser preenchido, quando Pagamento igual a <<6>> e Motivo Supensao diferente de <<5>> ou <<7>>
- Este campo deve ser preenchido se Pagamento = 6 e motivo Suspensão diferente 5 e 7, caso contrário, exibir a mensagem <<93719>>: “<<Nome Funcional do Campo>> só deve ser preenchido, quando Pagamento igual a <<6>> e Motivo Supensao diferente de  <<5>> ou <<7>>

MFS\-661904

RN28

__Estado __

Validações

- Este campo só pode ser preenchido se Pagamento = 6 e Motivo Suspensão diferente de 5 ou 7, caso contrário, exibir a mensagem <<93712>: “<<Nome Funcional do Campo>> só deve ser preenchido, quando Pagamento igual a <<6>> e Motivo Supensao diferente de <<5>> ou <<7>>\.”
- Quando preenchido, deve estar previamente cadastrado na tabela de estado \(TFIX04\), caso contrário exibir a mensagem <<60935>>: “<<Nome Funcional do Campo>> deve estar cadastrado na tabela de Estado\.”
- Quando se Motivo Suspensão diferente de 5 ou 7: 

Se Estado nulo ou zerado, mensagem <<92140>>: “<<O codigo do estado e obrigatorio\.”

MFS\-661904

RN29

__Município__

Validações

- Este campo só pode ser preenchido se Pagamento = 6 e motivo de suspensão diferente de 5 e 7 , caso contrário, exibir a mensagem <<93713>>: “<<Nome Funcional do Campo>>só deve ser preenchido, quando Pagamento igual a <<6>> e Motivo Supensao diferente de <<5>> ou <<7>>
- Se o município não é válido para o estado em questão, exibir a mensagem <<91759>>: “O Codigo do Municipio e invalido para o Estado correspondente”
- Quando se Motivo Suspensão diferente de 5 ou 7: 

Se município nulo ou zerado, mensagem <<90552>>: “<<O codigo do município deve ser preenchido\.”

MFS\-661904

RN30

__Depósito__

Opções Válidas: 

1\- Sem Depósito

2 \-Com Depósito

Validações

- Este campo só pode ser preenchido se Pagamento = 6, caso contrário, exibir a mensagem <<93714>>: “<<Nome Funcional do Campo>> só deve ser preenchido, quando Pagamento igual a <<6>>\.”
- Se o campo for preenchido, com uma opção inválida, exibir a mensagem<<93715>>: “<<Nome Funcional do Campo>> deve ser preenchido com <<1>> ou <<2>>\.”
- Se motivo igual a 2 ou 5 e Depósito igual a 1, exibir a mensagem <<93717>: “Quando Motivo de Suspensao igual a <<2>> ou <<5>>, o Deposito obrigatoriamente deve ser igual a <<2>>”
- Se motivo igual a 7 Depósito igual a 2, exibir a mensagem <<93718>: Quando Motivo de Suspensao igual a <<7>>, o Deposito obrigatoriamente deve ser igual a <<1>>

RN31

__Identificação do Depósito__

- Este campo só pode ser preenchido se Pagamento = 6 e Depósito igual a 2, caso contrário, exibir a mensagem<<93716>>: “<<Nome Funcional do Campo>> só deve ser preenchido, quando Pagamento igual a <<6>> e Depósito = <<2>>\.”

MFS\-661904

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


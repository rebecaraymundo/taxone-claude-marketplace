# MTZ-Job-Servidor-Importacao-SAFX2037

- **Fonte:** MTZ-Job-Servidor-Importacao-SAFX2037.docx
- **Modificado:** 2022-11-04
- **Tamanho:** 72 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX2037

Tabela dos Setores

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação à Execução

\- Importação Batch à Programação à Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS\-15147

Alteração da SAFX2037 

Criação de campos para o eSocial \(ver RN05 a RN15\)\. 

07/12/2017

\(criação do docto\)

__MFS\-88130__

Elisabete Costa

Criação dos campos “Alíquota RAT” e “Fator Acidentário de Prevenção FAP” – S\-1020

22/06/2022

__MFS\-96008__

Elisabete Costa

Retirada do Módulo: Informações para o E\-Social do T1

04/11/2022

__Devido ao end\-of\-support da mensageria OS E\-Social, e a não utilização de clientes no Tax One integrados, o módulo Informações para o E\-Social será retirado do TAX ONE e deverá permanecer no DW\.__

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

A SAFX2037 \(Setores\) foi alterada na __MFS\-15147__ para a criação de campos para atender à geração do eSocial, evento S\-1020 \(Cadastro de Lotações\)\. Foram criados os campos 05 ao 17\.

__RN05__

__Campo Data de Validade Final         __             

Campo de preenchimento não obrigatório\.

Se preenchida, deve ser uma data válida, que seja >= a validade inicial \(campo 02\)\.

Quando a data for preenchida e não atender aos critérios acima, será gravada uma mensagem de erro padrão no log e o registro não será importado\.

Campo criado na MFS\-15147

__RN06__

__Campo Tipo de Lotação Tributária         __            

Campo de preenchimento não obrigatório\.

Valores válidos: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 21, 24, 90 ou 91\.

Quando preenchido com um conteúdo inválido, será gravada uma mensagem de erro padrão no log e o registro não será importado\.

Obs: Estes códigos correspondem à Tabela 10 \(“Tipos de Lotação Tributária”\) do eSocial\. Para verificar o significado de cada código, consultar o documento de regras da manutenção, ou o próprio manual do eSocial \(Anexo I \- Tabelas\)\.

Campo criado na MFS\-15147

__RN07__

__Campo Tipo de Inscrição da Lotação         __            

Campo de preenchimento não obrigatório\.

Valores válidos: “1” \(CNPJ\), “2” \(CPF\), “4” \(CNO\)

Quando preenchido com um conteúdo inválido, será gravada uma mensagem de erro padrão no log e o registro não será importado\.

__Outras validações sobre os campos 06, 07 e 08: __

\- Crítica sobre o tipo da lotação \(campo 06\) x tipo e número da inscrição \(campos 07 e 08\):

Os campos 07 e 08 \(*Tipo de Inscrição da Lotação *e *Número de Inscrição da Lotação*\) só devem ser informados quando o campo 06 \(*Tipo de Lotação Tributária\)* for preenchido com uma das seguintes opções: 02\-03\-04\-05\-06\-07\-08\-09\. Caso contrário, não devem ser informado\.

Assim, quando esta regra não for atendida, será gravada no log de erros uma das mensagens a seguir \(conforme o caso\), e o registro não será importado:

      Se não estiver preenchido, quando deveria estar:

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>      *“O Tipo e o Número de Inscrição da Lotação devem ser informados para os Tipos de Lotação = 02\-03\-04\-05\-06\-07\-08\-09”*

      Se estiver preenchido indevidamente:

      *“O Tipo e o Número de Inscrição da Lotação não devem ser informados para os Tipos de Lotação = 01\-10\-21\-24\-90\-91”*

\- Crítica sobre o tipo de inscrição \(campo 07\)  x número de inscrição \(campo 08\):

Ao informar o campo 07, deverá ser informado também o campo 08, ou vice\-versa\. Sempre que um for informado e o outro não, será gravada a seguinte mensagem de erro no log e o registro não será importado:

                 *“Ao informar o Número de Inscrição da Lotação, deve\-se informar também o Tipo de Inscrição”*

 

Campo criado na MFS\-15147

__RN08__

__Campo Número de Inscrição da Lotação         __             

Campo de preenchimento não obrigatório\.

Neste campo o usuário informará o número correspondente à opção informada no campo anterior\. Ou seja, o número informado pode ser um CNPJ, um CPF ou um número CNO\.

Se for um CNPJ:

     Nesse caso, será verificada a validade do CNPJ informado, e caso inválido, será gravada uma mensagem de erro padrão no log 

     e o registro não será importado; 

Se for um CPF:

     Nesse caso, será verificada a validade do CPF informado, e caso inválido, será gravada uma mensagem de erro padrão no log 

     e o registro não será importado; 

Se for um CNO:

     Neste caso, o conteúdo não será validado; 

__Obs__: Ver na __RN07 __as críticas sobre os campos 06, 07 e 08 \(tipo da lotação, tipo de inscrição da lotação, e número de inscrição da lotação\)

Campo criado na MFS\-15147

__RN09__

__Campo Código FPAS         __                                

Campo de preenchimento não obrigatório\.

Obs: A princípio, esta informação não será validada\. Trata\-se dos códigos da tabela 04 do eSocial \(Códigos e Alíquotas de FPAS / Terceiros\), conforme orientação do manual de layout e help\.

Campo criado na MFS\-15147

__RN10__

__Campo Código Terceiros                     __                     

Campo de preenchimento não obrigatório\.

Obs: A princípio, esta informação não será validada\. Trata\-se dos códigos da tabela 04 do eSocial \(Códigos e Alíquotas de FPAS / Terceiros\), conforme orientação do manual de layout e help\.

Campo criado na MFS\-15147

__RN11__

__Campo Código Combinado de Terceiros \(Recolhimento Suspenso\)  __             

Campo de preenchimento não obrigatório\.

Obs: A princípio, esta informação não será validada\. Trata\-se dos códigos da tabela 04 do eSocial \(Códigos e Alíquotas de FPAS / Terceiros\), conforme orientação do manual de layout e help\.

Campo criado na MFS\-15147

__RN12__

__Campo Código Terceiros – Processo         __                                                   

__                          __

Campo de preenchimento não obrigatório

Obs: A princípio, esta informação não será validada\. Trata\-se dos códigos da tabela 04 do eSocial \(Códigos e Alíquotas de FPAS / Terceiros\), conforme orientação do manual de layout e help\.

Obs 2: Quando o código do campo “Cód\. Combinado de Terceiros” for uma combinação de códigos de mais de um terceiro, poderá haver mais de um processo a ser informado, ou seja, um para cada terceiro da combinação \(conforme previsto no layout do eSocial\)\. No entanto, durante o desenvolvimento do eSocial foi decidido que a princípio *não* trataríamos a possibilidade de mais de um processo\. No futuro, caso algum cliente reporte este cenário, poderá ser criada uma tabela filha, para possibilitar a inclusão de ‘n’ processos\.

Campo criado na MFS\-15147

__RN13__

__Campo Indicador do Tipo de Processo         __                                                     

Campo de preenchimento não obrigatório\.

Valores válidos:      “1”     \(Administrativo\)

                                 “2”     \(Judicial\)

Quando preenchido com um conteúdo inválido, será gravada uma mensagem de erro padrão no log e o registro não será importado\.

Campo criado na MFS\-15147

__RN14__

__Campo Número do Processo         __                                                                    

Campo de preenchimento não obrigatório\.

Quando informado, o número do processo deve existir na *Tabela de Cadastro de Processos Administrativos / Judiciais \(SAFX2058\)*\.

Para pesquisar os processos na SAFX2058, considerar:

\-Grupo – mesmo Grupo do Setor \(\*\*\*\);

\-Tipo Processo – tipo de processo informado no campo 13;

\-Número Processo – número do processo informado neste campo \(campo 14\);

\-Validade Inicial – maior data que seja <= data de validade inicial do setor;

\-Validade Final – deve ser nula ou >= data de validade inicial do Setor;

 

\(\*\*\*\) O __Grupo__ a ser utilizado será obtido a partir da regra básica, considerando o Grupo \(Relacionamento Tabelas x Grupos\) de maior data de validade, que seja <= a data de validade inicial do Setor, para o qual a tabela SAFX2037 esteja associada\.

Caso o processo não exista na SAFX2058, considerando as condições acima, o registro não será importado, e será gerada mensagem de erro no log da importação\.

Ex: “*O Número do Processo não existe na Tabela de Cadastro de Processos Administrativos/Judiciais \(SAFX2058\), ou não é válido para o Setor em questão”*\.

Campo criado na MFS\-15147

__RN15__

__Campo Código do Indicativo da Suspensão         __                                        

Campo de preenchimento não obrigatório\.

Quando informado, o código do indicativo da suspensão deve existir na *Tabela de Informações de Suspensão de Exigibilidade de Tributos \(SAFX2059\)*\.

Para pesquisar os códigos indicativos da suspensão na SAFX2059, considerar:

\-Considerar apenas os registros que sejam “filhos” do processo informado \(campos 13 e 14\); 

\-Código do Indicativo da Suspensão de Exigibilidade de Tributos – código informado neste campo \(campo 15\);

Caso o código do indicativo da suspensão não exista na SAFX2059, considerando as condições acima, será gravada mensagem de erro e o registro não será importado\. 

Ex: “*O Código do Indicativo da Suspensão não existe na Tabela de Informações de Suspensão de Exigibilidade de Tributos \(SAFX2059\), ou não é válido para o Setor em questão”*\.

Campo criado na MFS\-15147

__RN16__

__Campo Alíquota RAT__

Campo de preenchimento não obrigatório\.

Valores válidos: 1, 2 e 3

Quando preenchido com um conteúdo inválido, será gravada uma mensagem de erro padrão no log e o registro não será importado\.

Campo criado na __MFS\-88130__

__RN17__

__Campo Fator Acidentário de Prevenção FAP__

Campo de preenchimento não obrigatório\.

Deve ser um número maior ou igual a 0,5000 e menor ou igual a 2,0000\.

Quando preenchido com um conteúdo inválido, será gravada uma mensagem de erro padrão no log e o registro não será importado\.

Campo criado na __MFS\-88130__


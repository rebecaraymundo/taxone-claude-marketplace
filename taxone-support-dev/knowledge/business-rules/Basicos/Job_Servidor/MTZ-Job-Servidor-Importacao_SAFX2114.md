# MTZ-Job-Servidor-Importacao_SAFX2114

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX2114.docx
- **Modificado:** 2022-11-04
- **Tamanho:** 74 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX2114

Tabela de Cadastro das Rubricas \(eSocial\)

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS14409

Criação da SAFX2114 

Criação da SAFX2114 para a importação das rubricas do evento S\-1010 do eSocial\. 

28/11/2017

__MFS\-87292__

Elisabete Costa

Criação do campo “Tipo de apuração de IR” para o S\-1200

04/06/2021

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

__Estrutura da tabela SAFX2114__ 🡪 vide manual de layout

A SAFX2114 foi criada na __MFS14409__, para a importação dos dados de cadastro das rubricas do eSocial \(evento S\-1010 do eSocial\)\.

__Campos que compõe a chave da tabela \(PK\):__

                                  Grupo \+ Código da Tabela da Rubrica \+ Código da Rubrica \+ Data de Validade Inicial

Esta tabela é uma tabela de códigos, conforme o padrão das tabelas de código de DW \(ex: SAFX2013\. SAFX2023, \.\.\.\)\.

O __Grupo__ a ser utilizado será obtido a partir da regra básica, considerando o Grupo \(Relacionamento Tabelas x Grupos\) de maior data de validade, que seja <= a data de validade inicial da rubrica, para o qual a tabela SAFX2114 esteja associada\.

 

__RN01__

__Campo Código da Tabela de Rubricas__

Campo de preenchimento obrigatório\.

__RN02__

__Campo Código da Rubrica__

Campo de preenchimento obrigatório\.

__RN03__

__Campo Data de Validade Inicial __

Campo de preenchimento obrigatório\.

Deve ser uma data válida\.

__RN04__

__Campo Data de Validade Final__

Campo de preenchimento *não* obrigatório\.

Quando preenchido, deve ser uma data válida\.

__RN05__

__Campo Descrição__

Campo de preenchimento obrigatório\.

__RN06__

__Campo Natureza da Rubrica__

Campo de preenchimento obrigatório\.

O conteúdo informado deve ser um código existente na “*Tabela de Natureza das Rubricas da Folha de Pagamento – eSocial*”  __\(TACES64\)__\.

__RN07__

__Campo Tipo de Rubrica __

Campo de preenchimento obrigatório\.

Valores válidos:     “1”     \(Vencimento, provento ou pensão\)

                                  “2”     \(Desconto\)

                                  “3”     \(Informativa\)

                                  “4”     \(Informativa dedutora\)

__RN08__

__Campo Tipo Incidência Previdência Social __

Campo de preenchimento obrigatório\.

Valor válido: 1

__RN09__

__Campo Código Incidência Previdência Social __

Campo de preenchimento obrigatório\.

O conteúdo informado deve ser um código existente na “*Tabela de Códigos de Incidência Tributária das Rubricas – eSocial*” __\(TACES62\)__, considerando apenas os códigos da tabela cujo campo TIPO seja = __1__ \(códigos referentes à Contribuição Previdenciária\)\.

__RN10__

__Campo Tipo Incidência IRRF __

Campo de preenchimento obrigatório\.

Valor válido: 2

__RN11__

__Campo Código Incidência IRRF __

Campo de preenchimento obrigatório\.

O conteúdo informado deve ser um código existente na “*Tabela de Códigos de Incidência Tributária das Rubricas – eSocial*” __\(TACES62\)__, considerando apenas os códigos da tabela cujo campo TIPO seja = __2__ \(códigos referentes ao IRRF\)\.

__RN12__

__Campo Indicador do Tipo de Processo \(CP\)__

Campo de preenchimento obrigatório em algumas condições\.

Valores válidos:     “1”     \(Administrativo\)

                               “2”     \(Judicial\)

Os campos 10, 11 e 12 indicam um processo relacionado à contribuição previdenciária\. 

A informação deste tipo de processo é obrigatória quando o campo “08\-Incidência Previdência Social” for = 91, 92, 93, 94, 95, 96, 97 ou 98\. 

Neste caso, se os campos 10, 11, 12 e 13 não forem informados, o registro não será salvo, e será gerada mensagem de erro no log da importação\.

Ex: “*Quando o código de incidência p/a Previdência Social for iniciado por “9”, é obrigatório informar um processo \(campos 10/11/12/13\)*”

__RN13__

__Campo Número do Processo \(CP\)__

Campo de preenchimento obrigatório em algumas condições \(ver __RN10__\)\.

Quando informado, o número do processo deve existir na *Tabela de Cadastro de Processos Administrativos / Judiciais \(SAFX2058\)*\.

Para pesquisar os processos na SAFX2058, considerar:

\-Grupo – Grupo obtido conforme RN00 \(mesmo Grupo da rubrica\);

\-Tipo Processo – tipo de processo informado no campo 10;

\-Número Processo – número do processo informado neste campo \(campo 11\);

\-Validade Inicial – maior data que seja <= data de validade inicial da rubrica \(data informada no campo 03\);

\-Validade Final – deve ser nula ou >= data de validade inicial da rubrica \(data informada no campo 03\);

 

Caso o processo não exista na SAFX2058, considerando as condições acima, o registro não será importado, e será gerada mensagem de erro no log da importação\.

Ex: “*O Número do Processo \(CP\)  não existe na Tabela de Cadastro de Processos Administrativos/Judiciais \(SAFX2058\), ou não é válido para a Rubrica em questão”*\.

__RN14__

__Campo Código do Indicativo da Suspensão \(CP\)__

Campo de preenchimento obrigatório em algumas condições \(ver __RN10__\)\.

Quando informado, o código do indicativo da suspensão deve existir na *Tabela de Informações de Suspensão de Exigibilidade de Tributos \(SAFX2059\)*\.

Para pesquisar os códigos indicativos da suspensão na SAFX2059, considerar:

\-Grupo – Grupo obtido conforme RN00 \(mesmo Grupo da rubrica\);

\-Tipo Processo – tipo de processo informado no campo 10;

\-Número Processo – número do processo informado no campo 11;

\-Validade Inicial – maior data que seja <= data de validade inicial da rubrica \(data informada no campo 03\);

\-Validade Final – deve ser nula ou >= data de validade inicial da rubrica \(data informada no campo 03\);

\-Código do Indicativo da Suspensão de Exigibilidade de Tributos – código informado neste campo \(campo 12\);

\(desta forma, serão considerados apenas os códigos da SAFX2059 que sejam “filhos” do processo informado no campo 11\)

Caso o código do indicativo da suspensão não exista na SAFX2059, considerando as condições acima, será gravada mensagem de erro e o registro não será importado\. 

Ex: “*O Código do Indicativo da Suspensão\(CP\) não existe na Tabela de Informações de Suspensão de Exigibilidade de Tributos \(SAFX2059\), ou não é válido para a Rubrica em questão”*\.

__RN15__

__Campo Extensão da Decisão/Sentença  \(CP\)__

Campo de preenchimento obrigatório em algumas condições \(ver __RN10__\)\.

Valores válidos:      “1”     \(Contribuição Previdenciária Patronal\)

                                “2”     \(Contribuição Previdenciária Patronal \+ Descontada dos Segurados\)

__RN16__

__Campo Indicador do Tipo de Processo \(IRRF\)__

Campo de preenchimento obrigatório em algumas condições\.

Valores válidos:     “1”     \(Administrativo\)

                               “2”     \(Judicial\)

Os campos 13, 14 e 15 indicam um processo relacionado ao IRRRF\. 

A informação deste tipo de processo é obrigatória quando o campo “*09\-Incidência IRRF*” for = 91, 92, 93, 94 e 95\. 

Neste caso, se os campos 13, 14 e 15 não forem informados, o registro não será salvo, e será gerada mensagem de erro no log da importação\.

Ex: “*Quando o código de incidência p/o IRRF for iniciado por “9”, é obrigatório informar um processo \(campos 14/15/16\)*”

__RN17__

__Campo Número do Processo \(IRRF\)__

Campo de preenchimento obrigatório em algumas condições \(ver __RN14__\)\.

Quando informado, o número do processo deve existir na *Tabela de Cadastro de Processos Administrativos / Judiciais \(SAFX2058\)*\.

Para pesquisar os processos na SAFX2058, considerar:

\-Grupo – Grupo obtido conforme RN00 \(mesmo Grupo da rubrica\);

\-Tipo Processo – tipo de processo informado no campo 14;

\-Número Processo – número do processo informado neste campo \(campo 15\);

\-Validade Inicial – maior data que seja <= data de validade inicial da rubrica \(data informada no campo 03\);

\-Validade Final – deve ser nula ou >= data de validade inicial da rubrica \(data informada no campo 03\);

 

Caso o processo não exista na SAFX2058, considerando as condições acima, o registro não será importado, e será gerada mensagem de erro no log da importação\.

Ex: “*O Número do Processo \(IRRF\) não existe na Tabela de Cadastro de Processos Administrativos/Judiciais \(SAFX2058\), ou não é válido para a Rubrica em questão”*\.

__RN18__

__Campo Código do Indicativo da Suspensão \(IRRF\)__

Campo de preenchimento obrigatório em algumas condições \(ver __RN14__\)\.

Quando informado, o código do indicativo da suspensão deve existir na *Tabela de Informações de Suspensão de Exigibilidade de Tributos \(SAFX2059\)*\.

Para pesquisar os códigos indicativos da suspensão na SAFX2059, considerar:

\-Grupo – Grupo obtido conforme RN00 \(mesmo Grupo da rubrica\);

\-Tipo Processo – tipo de processo informado no campo 14;

\-Número Processo – número do processo informado neste campo \(campo 15\);

\-Validade Inicial – maior data que seja <= data de validade inicial da rubrica \(data informada no campo 03\);

\-Validade Final – deve ser nula ou >= data de validade inicial da rubrica \(data informada no campo 03\);

\-Código do Indicativo da Suspensão de Exigibilidade de Tributos – código informado neste campo \(campo 16\);

\(desta forma, serão considerados apenas os códigos da SAFX2059 que sejam “filhos” do processo informado no campo 15\)

Caso o código do indicativo da suspensão não exista na SAFX2059, considerando as condições acima, será gravada mensagem de erro e o registro não será importado\. 

Ex: “*O Código do Indicativo da Suspensão\(IRRF\) não existe na Tabela de Informações de Suspensão de Exigibilidade de Tributos \(SAFX2059\), ou não é válido para a Rubrica em questão”*\.

__RN22__

__Tipo de apuração de IR__

Valores válidos:

__0__ \- Normal \(apuração sob a folha de pagamento declarada no eSocial\); 

__1__ \- Situação especial de apuração de IR\.

__MFS\-87292__

__RN196__

__Campo Observação __

Campo de preenchimento *não* obrigatório\.


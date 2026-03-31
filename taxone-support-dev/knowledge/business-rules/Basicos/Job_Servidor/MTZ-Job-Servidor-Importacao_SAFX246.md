# MTZ-Job-Servidor-Importacao_SAFX246

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX246.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 71 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX246

Tabela de Operações de Intermediação Comercial / Comércio Eletrônico \(Port\.CAT 156/2010\)

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS11593

Criação da SAFX246 

Criação da SAFX246 para a importação dos dados da Portaria CAT 156/2010\. 

12/07/2017

MFS23115

Atendimento à Portaria CAT 156/2010

Criação de novos campos na SAFX246 para a geração do registro 5030\.

19/12/2018

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX246__ 🡪 vide manual de layout

A SAFX246 foi criada na __MFS11593__, para a importação dos dados referentes à prestação dos serviços de intermediação comercial em ambiente virtual, e serviços relacionados ao comércio eletrônico\.

Estas informações são utilizadas na geração do meio magnético da Portaria CAT 156/2010\.

Campos que compõem a chave da tabela \(campo 01 ao campo 07\):

\[ Código da Empresa \+ Código do Estabelecimento \+ Data da Operação  \+ Indicador da Pessoa Fis/Jur \+ Código da Pessoa Fis/Jur \+ Tipo do Serviço \+ Código da Operação \]  

 

Alteração __MFS23115__: Originalmente, a obrigação da Portaria CAT 156 foi criada para tratar apenas os tipos de serviço 1300 \(Gateway de Pagamentos\) e 1400 \(Intermediação Financeira\), que são os registros 5050 e 5070\. Nesta MFS foi incluído o tratamento do tipo de serviço 1000\-Internediação Comercial \(registro 5030\), e para isso foi necessária incluir novos campos na SAFX246: “Comissão \(S/N\)”, “Unidade de Medida”, “Quantidade”, “Valor Unitário” e “Valor Desconto”\. 

__RN01__

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

* \(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

__RN03__

__Campo Data da Operação__

Campo de preenchimento obrigatório\.

Deve ser uma data válida\.

Quando não preenchido ou, quando for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

                                                        *“Data da Operação não preenchida ou inválida”\.*

__RN04__

__Campo Indicador da Pessoa Física/Jurídica __

Campo de preenchimento obrigatório\.

Conteúdo válido conforme indicadores da SAFX04: 1, 2, 3, 4 ou 5\.

Quando não preenchido ou inválido, o registro não será importado, e será gravada a seguinte mensagem de erro no log:

            *“Indicador da Pessoa Física/Jurídica inválido\. Preencher de acordo com o indicador de pessoa a fis/jur da SAFX04”*

__RN05__

__Campo Código da Pessoa Física/Jurídica __

Campo de preenchimento obrigatório\.

Quando não preenchido, o registro não será importado, e será gravada a seguinte mensagem de erro no log:

                                        *“O Código da Pessoa Física/Jurídica é de preenchimento obrigatório”*

A pessoa física/jurídica informada deve existir na Tabela de Pessoas Físicas/Jurídicas \(SAFX04\)\. Caso contrário, o registro não será importado e será gravada a seguinte mensagem de erro no log:

                               *“Pessoa Fisica /Juridica nao existente na Tabela de Pessoas Fis/Jur \(SAFX04\)”*

Para pesquisar a SAFX04, usar o Grupo de Relacionamento \(Estabelecimento x Grupo x Tabela\) de maior data de validade, que seja <= a data da operação informada \(campo 03\)\.

__RN06__

__Campo Tipo do Serviço__

Campo de preenchimento obrigatório\.

Conteúdo válido: “1000”, “1100”,  “1200”,  “1300”,  “1400” ou  “1500”\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*            “Tipo do Serviço inválido\. Preencher de acordo com a tabela dos códigos de serviço previstos na Portaria CAT 156/2010”*

__RN07__

__Campo Código da Operação __

Campo de preenchimento obrigatório\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

                                                *“O Código da Operação é de preenchimento obrigatório”*

__RN08__

__Campo Descrição do Produto __

Campo de preenchimento obrigatório quando o Tipo de Serviço for = ‘1000’ ou ‘1400’\.

Quando a condição acima não for atendida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

*                      “A Descrição do Produto é de preenchimento obrigatório quando Tipo de Serviço = 1000 ou 1400”*

__RN09__

__Campo Valor Total da Operação __

Campo de preenchimento obrigatório quando o Tipo de Serviço for = ‘1000’ ou ‘1400’\.

Quando a condição acima não for atendida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

*                            “O Valor da Operação é de preenchimento obrigatório quando Tipo de Serviço = 1000 ou 1400”*

__RN10__

__Campo Tipo de Pagamento __

Campo de preenchimento obrigatório quando o Tipo de Serviço for = ‘1000’, ‘1300’ ou ‘1400’\.

Se preenchido, o conteúdo válido deve ser = “01”, “02”, “03”,  “04”,  “05”, “06” ou  “99”\.

Quando as duas condições acima não forem atendidas, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

*                 “O Tipo de Pagamento é de preenchimento obrigatório quando Tipo de Serviço = 1000, 1300 ou 1400”\.*

*                  Preencher de acordo com a tabela das formas de pagamento previstas na Portaria CAT 156/2010”*

__RN11__

__Campo UF do Comprador __

Campo de preenchimento obrigatório quando o Tipo de Serviço for = ‘1000’, ‘1300’, ‘1400’ ou ‘1500’

Se preenchido, deve ser uma UF válida\.

Quando as duas condições acima não forem atendidas, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

* “UF do Comprador inválida ou não preenchida\. Este campo é de preenchimento obrigatório quando Tipo de Serviço = 1000, 1300, 1400 ou 1500”\.*

__RN12__

__Campo Data Inicial do Contrato __

Campo de preenchimento obrigatório quando o Tipo de Serviço for = ‘1100’, ‘1300’ ou ‘1500’\.

Deve ser uma data válida\.

Quando as duas condições acima não forem atendidas, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

*                         “Data Inicial do Contrato inválida ou não informada\. O preenchimento do campo é obrigatório quando *

*                                                                   Tipo de Serviço = ‘1100, 1300 ou 1500”*

__RN13__

__Campo Data Final do Contrato __

Campo de preenchimento *não* obrigatório\.

Quando preenchido, deve ser uma data válida e >= a data inicial do contrato \(campo 12\)\. Caso contrário, o registro não será importado, e será gravada a seguinte mensagem de erro no log:

                  *“A Data Final do Contrato deve ser uma data válida, igual ou superior a Data Inicial do Contrato\.”*

__RN14__

__Campo Comissão__ \(campo criado na MFS23115\)

Campo de preenchimento obrigatório quando o Tipo de Serviço for = ‘1000’\. 

Nesse caso, quando não informado, o registro não será importado, e será gravada a seguinte mensagem de erro no log:          

                              “*O campo Comissão é de preenchimento obrigatório quando Tipo de Serviço = 1000” * 

Quando preenchido, seu conteúdo deve ser = “0” ou “1” \(Não / Sim\)\. Caso contrário, o registro não será importado, e será gravada a seguinte mensagem de erro no log: 

                                       *“Campo Comissão inválido\. Preencher com “0” \(Não\) ou “1” \(Sim\)”*

MFS23115

__RN15__

__Campo Unidade de Medida __\(campo criado na MFS23115\)__  __

Campo de preenchimento obrigatório quando o Tipo de Serviço for = ‘1000’\.

Nesse caso, quando não informado, o registro não será importado, e será gravada a seguinte mensagem de erro no log: 

                                   “A* Unidade de Medida é de preenchimento obrigatório quando Tipo de Serviço = 1000” * 

Quando preenchido, deve ser um código de medida existente na Tabela de Unidades de Medida \(SAFX2007\), e com validade <= a data da operação informada \(campo 03\)\. Caso contrário, o registro não será importado e será gravada a seguinte mensagem de erro no log:

                         *“Unidade de Medida inválida\. Preencher de acordo com a Tabela de Unidades de Medida \(SAFX2007\)\.”*

Para pesquisar a SAFX2007, usar o Grupo de Relacionamento \(Estabelecimento x Grupo x Tabela\) de maior data de validade, que seja <= a data da operação informada \(campo 03\)\.

MFS23115

__RN16__

__Campo Quantidade __\(campo criado na MFS23115\)

Campo de preenchimento obrigatório quando o Tipo de Serviço for = ‘1000’\.

Nesse caso, quando não informado, o registro não será importado, e será gravada a seguinte mensagem de erro no log: 

                                       “A *Quantidade é de preenchimento obrigatório quando Tipo de Serviço = 1000” * 

MFS23115

__RN17__

__Campo Valor Unitário __\(campo criado na MFS23115\)

Campo de preenchimento obrigatório quando o Tipo de Serviço for = ‘1000’\.

Nesse caso, quando não informado, o registro não será importado, e será gravada a seguinte mensagem de erro no log: 

                                    “*O Valor Unitário é de preenchimento obrigatório quando Tipo de Serviço = 1000” * 

MFS23115

__RN18__

__Campo Valor Desconto __\(campo criado na MFS23115\)

Campo de preenchimento *não* obrigatório\.

MFS23115


# MTZ-OTF-Geracao_do_Relatorio_de_Rastreabilidade_das_Retencoes_e_DARFs

- **Fonte:** MTZ-OTF-Geracao_do_Relatorio_de_Rastreabilidade_das_Retencoes_e_DARFs.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 51 KB

---

<a id="OLE_LINK6"></a><a id="OLE_LINK7"></a># Obrigações de Tributos Federais \- Geração do Relatório de Rastreabilidade das Retenções e DARF's

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3267\-C

Obrigações de Tributos Federais \- Geração do Relatório de Rastreabilidade das Retenções e DARF's

Será desenvolvida uma rotina para que o usuário possa realizar a geração de um relatório que contenha toda a rastreabilidade dos DARF’s e se os mesmos possuíram algum Crédito ou Compensação, além das Retenções e Retificações caso existam\.

#### Cód\.

### Descrição

### DR

# RN01

Deverá ser criada uma nova tela chamada “Relatório de Rastreabilidade de Retenções e DARF’s”\. Essa tela deverá ser disponibilizada no menu Outras Obrigações >> DARF’s >> Relatório de Rastreabilidade de Retenções/DARF’s do módulo Obrigações de Tributos Federais\. 

Esse menu deverá ser disponibilizado após o menu “Emissão”\.

OS3267\-C

# RN02

Essa tela deverá ser uma tela de filtros para a geração do relatório de rastreabilidade de retenções e DARF’s\. Serão disponibilizados nessa tela, os seguintes filtros para geração do relatório:

- __Empresa:__ nesse campo o usuário deverá informar a Empresa para a geração do relatório\. Será informada a Empresa selecionada no Manager\. Caso o usuário não tenha selecionado nenhuma Empresa no Manager, esse campo estará vazio para seleção\. O usuário só poderá escolher uma Empresa para geração\. As informações serão recuperadas da tabela EMPRESA e nesse campo serão exibidas as informações dos campos COD\_EMPRESA e RAZAO\_SOCIAL separados por “\-“\. Campo obrigatório de preenchimento\.
- __Estabelecimento:__ nesse campo o usuário deverá informar o Estabelecimento para a geração do relatório\. Será informado o Estabelecimento selecionado no Manager\. Caso o usuário não tenha selecionado nenhum Estabelecimento no Manager, esse campo estará vazio para seleção\. O usuário só poderá escolher um Estabelecimento para geração\. As informações serão recuperadas da tabela ESTABELECIMENTO e nesse campo serão exibidas as informações dos campos COD\_ESTAB e RAZAO\_SOCIAL separados por “\-“\. Campo obrigatório de preenchimento\.
- __Período:__ nesse campo o usuário deverá informar o período para geração do relatório\. A informação irá recuperar os DARF’s Originais da tabela X75\_DCTF a partir da chave da tabela X75\_DCTF\. A partir desse campo as informações filhas desse DARF também serão recuperadas \- DARF's Complementares, Créditos, Compensações, Retenções e Retificações – PS: as regras para recuperação dessas informações constam nas outras regras de negócio desse Documento Matriz\. Além disso, o campo constará sempre o Período do mês corrente como default\.
- __Código DARF:__ nesse campo o usuário irá selecionar o Código DARF para a geração do relatório\. Essa informação será recuperada da tabela X2019\_COD\_DARF\. O usuário poderá selecionar apenas um Código DARF\. Campo não obrigatório de preenchimento\.
- __Código Receita:__ nesse campo o usuário irá selecionar o Código Receita para a geração do relatório\. Essa informação será recuperada da tabela DWT\_COD\_RECEITA\. O usuário poderá selecionar apenas um Código Receita\. Campo não obrigatório de preenchimento\.
- __Código Operação:__ nesse campo o usuário irá selecionar o Código Operação para a geração do relatório\. Essa informação será recuperada da tabela X2001\_OPERACAO\. O usuário poderá selecionar apenas um Código Operação\. Campo não obrigatório de preenchimento\.
- __Prestador:__ nesse campo o usuário irá selecionar o Prestador do Serviço para a geração do relatório\. Essa informação será recuperada da tabela X04\_PESSOA\_FIS\_JUR\. O usuário poderá selecionar apenas um Prestador\.

O usuário poderá limpar algumas informações que foram preenchidas\. As informações que poderão ser “limpas” pelo usuário são: Código DARF, Código Receita, Código Operação e Prestador\.

OS3267\-C

# RN03

Após informar os parâmetros para geração do relatório, o sistema irá gerar o relatório com base nas seguintes premissas para recuperação das informações:

- Serão recuperados todos os DARF’s das tabelas X75\_DCTF e X751\_DCTF\_COMPL cujo campo “Data de Apuração” esteja dentro do período informado na tela de filtros\.
- Os DARF’s serão recuperados independente do Status dos mesmos – Em aberto ou Pago\.
- A partir dos DARF’s recuperados, deverão ser recuperadas todas as retenções da X53\_RETENCAO\_IRRF que compuseram os DARF’s e caso essas retenções possuam registros de retificação na tabela X530\_RETIFICACAO\_IRRF os mesmos deverão ser recuperados também\.
- As retenções canceladas, ou seja, as retenções da tabela X53\_RETENCAO\_IRRF cujo campo “Cancelado” esteja selecionado e o campo Data de Cancelamento esteja preenchido, também deverão ser recuperadas\.
- Serão recuperados primeiramente os DARF’s que possuem DARF’s com retificações para depois serem recuperados os DARF’s que possuem retenções sem retificações\.
- Caso um Prestador seja informado serão recuperados somente os DARF’s em que aquele prestador esteve presente, porém os valores do DARF serão os que estão tanto na X75\_DCTF quanto na X751\_DCTF\_COMPL\. As retenções e retificações exibidas dos DARF’s serão de todos os prestadores que compuseram aquele DARF\.
- Os DARF’s divididos em Quotas da tabela X75\_DCTF não serão gerados no relatório, visto que a solução não permite a divisão de um DARF em Quotas\.
- O relatório permitirá a geração das informações por Empresa\. Nesse caso as informações serão centralizadas no Estabelecimento Matriz\.

OS3267\-C

# <a id="RN04"></a>RN04

O cabeçalho do relatório deverá exibir as seguintes informações:

- No canto superior esquerdo do relatório, deverá ser exibido o Código e a Razão Social da Empresa e embaixo o Código e a Razão Social do Estabelecimento\.
- Na mesma linha onde é exibido o Código e a Razão Social da Empresa, deverá ser exibido o Número da Página do mesmo\.
- Na mesma linha onde é exibido o Código e a Razão Social do Estabelecimento, deverá ser exibida a Data e a Hora em que o relatório foi gerado\.
- No centro do relatório deverá ser exibido o nome do relatório que é “Relatório de Rastreabilidade das Retenções e DARF’s”\.
- Abaixo do título do relatório deverá ser exibido o período de geração do relatório, de acordo com a informação preenchida na tela de filtro\.
- Cada início das informações do Estabelecimento deverá ser iniciado em uma nova página do relatório\.

OS3267\-C

# RN05

Após as informações do cabeçalho detalhadas na [RN04](#RN04), a primeira parte irá exibir a descrição “DARF Original”\. Serão recuperadas as informações dos DARF’s Originais contidos na tabela X75\_DCTF independente do Status do mesmo \(Em Aberto ou Pago\)\. Serão recuperados os DARF’s cujo campo “Data de Apuração” esteja no período informado na tela de filtro\.

Serão exibidas as informações do DARF Original um de cada vez, ou seja, caso existam mais de um registro na X75\_DCTF – o que é comum e natural – será exibido apenas o primeiro registro recuperado e a partir desse registro serão recuperadas as outras informações\. O DARF Original seguinte será exibido nas páginas futuras do relatório\.

OS3267\-C

# RN06

Do DARF Original citado anteriormente serão recuperadas as seguintes informações:

- __Código DARF: __será recuperado o Código DARF do DARF\. Essa informação será recuperada a partir do campo COD\_DARF da X75\_DCTF\.
- __Código Receita:__ será recuperado o Código de Receita do DARF\. Essa informação será recuperada a partir do campo COD\_RECEITA da X75\_DCTF\.
- __Código Operação: __será recuperado o Código Operação do DARF\. Essa informação será recuperada a partir do campo COD\_OPERACAO da X75\_DCTF\.
- __Data Pagamento: __será recuperado a Data de Vencimento do DARF\. Essa informação será recuperada a partir do campo DATA\_PAGTO da X75\_DCTF\.
- __Valor Principal: __será recuperado o Valor Principal do DARF\. Essa informação será recuperada a partir do campo VLR\_PRINCIPAL da X75\_DCTF\.
- __Valor Juros: __será recuperado o Valor de Juros do DARF\. Essa informação será recuperada a partir do campo VLR\_JUROS da X75\_DCTF\.
- __Valor Multa: __será recuperado o Valor da Multa do DARF\. Essa informação será recuperada a partir do campo VLR\_MULTA da X75\_DCTF\.
- __Valor Total: __será recuperado o Valor Total do DARF\. Essa informação será recuperada a partir do campo VLR\_TOTAL da X75\_DCTF\.
- __Compensação: __será recuperado o valor da Compensação referente a esse DARF\. Essa informação será recuperada a partir do campo VLR\_PRINC\_DEVIDO\_COMP da tabela CTRL\_COMPENSACAO\_CRED\.

A ordenação dos DARF’s será a seguinte:

- Código DARF
- Código Receita
- Código Operação
- Data Pagamento

OS3267\-C

# RN07

A segunda parte do relatório irá exibir a descrição “DARF Complementar”\. Serão recuperadas as informações dos DARF’s Complementares contidos na tabela X751\_DCTF\_COMPL cujo campo IND\_DEB\_CRED = “D” independente do Status do mesmo \(Em Aberto ou Pago\)\. Serão recuperados os DARF’s Complementares pertencentes ao DARF Original independente do período do DARF Complementar\.

Serão exibidas as informações referentes ao DARF Complementar pertencentes à cada DARF Original exibido anteriormente\.

OS3267\-C

# RN08

Caso o DARF Original possua DARF’s Complementares os mesmos deverão ser recuperados a partir da tabela X751\_DCTF\_COMPL\. Deverão ser exibidas as seguintes informações\.

- __Código DARF: __será recuperado o Código DARF do DARF\. Essa informação será recuperada a partir do campo COD\_DARF da X751\_DCTF\_COMPL\.
- __Código Receita:__ será recuperado o Código de Receita do DARF\. Essa informação será recuperada a partir do campo COD\_RECEITA da X751\_DCTF\_COMPL\.
- __Código Operação: __será recuperado o Código Operação do DARF\. Essa informação será recuperada a partir do campo COD\_OPERACAO da X751\_DCTF\_COMPL\.
- __Data Pagamento: __será recuperado a Data de Vencimento do DARF\. Essa informação será recuperada a partir do campo DATA\_PAGTO da X751\_DCTF\_COMPL\.
- __Valor Principal: __será recuperado o Valor Principal do DARF\. Essa informação será recuperada a partir do campo VLR\_PRINCIPAL da X751\_DCTF\_COMPL\.
- __Valor Juros: __será recuperado o Valor de Juros do DARF\. Essa informação será recuperada a partir do campo VLR\_JUROS da X751\_DCTF\_COMPL\.
- __Valor Multa: __será recuperado o Valor da Multa do DARF\. Essa informação será recuperada a partir do campo VLR\_MULTA da X751\_DCTF\_COMPL\.
- __Valor Total: __será recuperado o Valor Total do DARF\. Essa informação será recuperada a partir do campo VLR\_TOTAL da X751\_DCTF\_COMPL\.
- __Compensação: __será recuperado o valor da Compensação referente a esse DARF\. Essa informação será recuperada a partir do campo VLR\_PRINC\_DEVIDO\_COMP da tabela CTRL\_COMPENSACAO\_CRED\.

Em todos os DARF’s Originais informados, serão exibidos seus respectivos DARF’s Complementares – caso existam\.

A ordenação dos DARF’s Complementares será a seguinte:

- Código DARF
- Código Receita
- Código Operação
- Data Pagamento

OS3267\-C

# RN09

A terceira parte do relatório irá exibir a descrição “Créditos Provenientes de DARF”\. Serão recuperadas as informações dos DARF’s de Crédito contidos na tabela X751\_DCTF\_COMPL cujo campo IND\_DEB\_CRED = “C” independente do Status do mesmo \(Em Aberto ou Pago\)\. Serão recuperados os DARF’s de Crédito pertencentes ao DARF Original independente do período do DARF de Crédito\.

Serão exibidas as informações referentes ao DARF de Crédito pertencentes à cada DARF Original exibido anteriormente\.

OS3267\-C

# RN10

Caso o DARF Original possua DARF’s de Crédito, os mesmos deverão ser recuperados a partir da tabela X751\_DCTF\_COMPL\. Deverão ser exibidas as seguintes informações\.

- __Código DARF: __será recuperado o Código DARF do DARF\. Essa informação será recuperada a partir do campo COD\_DARF da X751\_DCTF\_COMPL\.
- __Código Receita:__ será recuperado o Código de Receita do DARF\. Essa informação será recuperada a partir do campo COD\_RECEITA da X751\_DCTF\_COMPL\.
- __Código Operação: __será recuperado o Código Operação do DARF\. Essa informação será recuperada a partir do campo COD\_OPERACAO da X751\_DCTF\_COMPL\.
- __Crédito: __será recuperado o valor do Crédito remanescente desse DARF\. Essa informação será recuperada a partir do campo VLR\_TOTAL da X751\_DCTF\_COMPL referente à esse DARF quando o campo IND\_DEB\_CRED = “C” do mesmo\.

Em todos os DARF’s Originais informados, serão exibidos seus respectivos DARF’s Complementares – caso existam\.

A ordenação dos DARF’s de Crédito será a seguinte:

- Código DARF
- Código Receita
- Código Operação

OS3267\-C

# RN11

Para o DARF informado deverão ser informados as retenções vinculadas à esse DARF na seção “Retenções Vinculadas a esse DARF”\. Nessa seção serão recuperadas todas as retenções originais que compuseram o DARF Original da X75\_DCTF\. As retenções originais serão recuperadas da tabela X53\_RETENCAO\_IRRF\. Deverão ser exibidas as seguintes informações:

- __Núm\. Doc\. Fiscal: __será recuperado o Número do Documento Fiscal\. Essa informação será recuperada a partir do campo NUM\_DOCFIS da tabela X53\_RETENCAO\_IRRF\.
- __Tipo Documento: __será recuperado o Tipo do Documento Fiscal\. Essa informação será recuperada a partir do campo COD\_DOCTO da tabela X53\_RETENCAO\_IRRF\.
- __Prestador: __será recuperado o Código e a Descrição do Prestador do Serviço\. Essa informação será recuperada a partir do campo IND\_FIS\_JUR da tabela X53\_RETENCAO\_IRRF\.
- __Data Movimento: __será recuperado a Data de Movimento do Documento Fiscal\. Essa informação será recuperada a partir do campo DATA\_MOVTO da tabela X53\_RETENCAO\_IRRF\.
- __Valor Bruto: __será recuperado o Valor Bruto do Documento Fiscal\. Essa informação será recuperada a partir do campo VLR\_BRUTO da tabela X53\_RETENCAO\_IRRF\.
- __Valor Retenção: __será recuperado o Valor da Retenção do Documento Fiscal\. Essa informação será recuperada a partir do campo VLR\_IR\_RETIDO da tabela X53\_RETENCAO\_IRRF\.
- __Cancelado: __será informado se o Documento Fiscal é Cancelado ou Não\. Essa informação será recuperada a partir do campo IND\_CANCELAMENTO da tabela X53\_RETENCAO\_IRRF\. Caso o campo seja “N” será informado “Não”\. Caso o campo seja “S”, será informado “Sim”\.
- __Data Cancelamento: __será informado a Data de Cancelamento do Documento Fiscal\. Essa informação será recuperada do campo DATA\_CANCELAMENTO da tabela X53\_RETENCAO\_IRRF\.

A ordenação das Retenções será a seguinte:

- Data Movimento
- Número Documento Fiscal
- Prestador

OS3267\-C

# RN12

Para a Retenção informada deverão ser informados também as retificações vinculadas à cada Retenção\. A seção será chamada de “Retificações da Retenção Vinculadas a esse DARF” e as informações serão recuperadas da tabela X530\_RETIFICACAO\_IRRF para cada retenção anterior informada\. Caso a retenção não possua retificações, as informações dessa seção não serão exibidas\.

- __Número da Retificação: __será informado o Número da Retificação\. Essa informação será gerada pelo próprio relatório e será gerada de acordo com a Data de Retificação da Retificação\. A Retificação mais antiga começa pelo número “1” e assim por diante\.
- __Data Retificação: __será informado a Data de Retificação da Retificação\. Essa informação será recuperada a partir do campo DATA\_RETIFICACAO da tabela X530\_RETIFICACAO\_IRRF\.
- __Valor Bruto: __será informado o Valor Bruto da Retificação\. Essa informação será recuperada a partir do campo VLR\_BRUTO da tabela X530\_RETIFICACAO\_IRRF\.
- __Valor Retenção: __será informado o Valor da Retenção da Retificação\. Essa informação será recuperada a partir do campo VLR\_IR\_RETIDO da tabela X530\_RETIFICACAO\_IRRF\.
- __Núm\. Doc\. Fiscal: __será recuperado o Número do Documento Fiscal\. Essa informação será recuperada a partir do campo NUM\_DOCFIS da tabela X53\_RETENCAO\_IRRF\.
- __Tipo Documento: __será recuperado o Tipo do Documento Fiscal\. Essa informação será recuperada a partir do campo COD\_DOCTO da tabela X53\_RETENCAO\_IRRF\.

A ordenação das Retificações será de acordo com o campo “Número da Retificação”\.

OS3267\-C

Considerações deste modelo: 

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


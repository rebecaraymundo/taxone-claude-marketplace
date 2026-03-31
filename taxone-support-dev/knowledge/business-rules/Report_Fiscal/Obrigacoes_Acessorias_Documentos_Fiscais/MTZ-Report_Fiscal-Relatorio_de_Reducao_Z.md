---
source: "MTZ-Report_Fiscal-Relatorio_de_Reducao_Z.doc"
category: Report_Fiscal
converted: auto
---

Report Fiscal - Geração do Relatório de Redução Z 


DOCUMENTO DE REQUISITO 

DR
Nome
Descrição
OS2943
Report Fiscal - Geração do Relatório de Redução Z
O cliente Ferramentas Gerais solicitou a elaboração de um relatório em que as informações da Redução Z X Cupons Fiscais X SAFX07/SAFX08 sejam confrontados a partir das tabelas de Cupom Fiscal criadas a partir do advento do projeto do SPED Fiscal - X991_CAPA_REDUCAO_ECF, X992_ITEM_REDUCAO_ECF, SAFX993, SAFX994, SAFX995 e SAFX996.

Ocorre que para um melhor atendimento dessa demanda, foi decidido em conjunto com o Sr. Marcos de Paula que seriam desenvolvidos dois relatórios, um para a Redução Z (objeto dessa OS) e outro para os Cupons Fiscais (OS2943-A).


REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN01
Deverá ser criada a tela de geração do relatório de conferência da Redução Z a partir das informações contidas nas tabelas X991_CAPA_REDUCAO_ECF e X992_ITEM_REDUCAO_ECF. Para a geração do relatório serão exibidos os seguintes campos para geração:

* Estabelecimento: nesse campo serão listados os estabelecimentos cadastrados no sistema, que estejam licenciados e que o usuário possua direito de acesso no módulo Segurança. As informações serão recuperadas da tabela ESTABELECIMENTO. Os estabelecimentos serão exibidos nesse campo através do "Código Estabelecimento" e "Descrição Estabelecimento" separados por um "-" (hífen). Campo obrigatório de preenchimento.
* Período: nesse campo o usuário deverá informar o Período para geração do relatório. O período informado irá recuperar as informações da tabela X991_CAPA_REDUCAO_ECF a partir do campo "Data de Movimento" dessa tabela. A data deverá ser informada duas vezes ("DE" e "ATÉ") e no formato DD/MM/AAAA. Campo obrigatório de preenchimento.
* Modelo do Documento: nesse campo o usuário deverá informar o Modelo do Documento relacionado ao Cupom Fiscal. O Modelo do Documento informado irá recuperar as informações da tabela X991_CAPA_REDUCAO_ECF a partir do campo "Modelo". Campo não obrigatório de preenchimento.
* Número do Caixa: nesse campo o usuário deverá informar o Número do Caixa relacionado ao Cupom Fiscal. O Número do Caixa informado irá recuperar as informações da tabela X991_CAPA_REDUCAO_ECF a partir do campo "Número do Caixa". Campo não obrigatório de preenchimento.
OS2943
RN02
Ao informar os campos para geração do relatório citados na RN01, o sistema irá gerar o relatório de Redução Z de acordo com os critérios abaixo:

* Serão recuperados os registros das tabelas X991_CAPA_REDUCAO_ECF e X992_ITEM_REDUCAO_ECF.
* As informações contidas na tabela X992_ITEM_REDUCAO_ECF serão recuperadas de acordo com a informação-pai da tabela X991_CAPA_REDUCAO_ECF, ou seja, para cada registro informado na X991_CAPA_REDUCAO_ECF será informado seus registros filhos na tabela X992_ITEM_REDUCAO_ECF se houver.
* Caso um registro recuperado da tabela X991_CAPA_REDUCAO_ECF possua mais de um registro na X992_ITEM_REDUCAO_ECF, todas as informações serão exibidas para o mesmo pai, ou seja, as informações recuperadas da X991_CAPA_REDUCAO_ECF não serão informadas em várias linhas.
* A correlação das informações da Redução Z com o Cupom Fiscal não será desenvolvida nessa OS.
OS2943
RN03
O relatório será gerado da seguinte maneira:

* No início do relatório, especificamente no canto superior esquerdo, será exibido o código e a descrição da empresa para o qual o relatório foi gerado;
* Na mesma linha do item anterior, será exibida no centro da página a Data e Hora em que o relatório foi emitido, ou seja, o momento em que o relatório foi gerado. A data será informada no formato DD/MM/AAAA (dia/mês/ano) e a hora no formato HH:MM:SS (hora/minuto/segundo).
* Na mesma linha dos itens anteriores, será informada a página do relatório.
* No centro do relatório será exibido o título do relatório. O título do relatório será "Relatório da Redução Z".
* Abaixo do título do relatório será exibido o período das informações geradas no relatório. As informações serão exibidas no formato DD/MM/AAAA (mês/ano). Essas informações serão recuperadas de acordo com o "Número de Processo" informado.
* Será informado o Código e a Descrição do Estabelecimento no relatório.
* Será informado o Código e a Descrição do Modelo do Documento no relatório.
* Será informado o Código e a Descrição do Número do Caixa no relatório.
* Serão exibidas as seguintes informações no relatório:
o Data Emissão: será exibida a Data da Emissão da Redução Z. Essa informação será recuperada do campo "Data Emissão" da tela Capa Redução Z (menu: Manutenção >> Cupom Fiscal (EFD/REDF) >> Movimentos >> Capa Redução Z) do módulo DW.
o Contadores
* CRZ: será exibida o CRZ da Redução Z. Essa informação será recuperada do campo "CRZ (Contador de Redução Z)" da tela Capa Redução Z (menu: Manutenção >> Cupom Fiscal (EFD/REDF) >> Movimentos >> Capa Redução Z) do módulo DW.
* COO: será exibida o COO da Redução Z. Essa informação será recuperada do campo "COO (Contador de Ordem de Operação)" da tela Capa Redução Z (menu: Manutenção >> Cupom Fiscal (EFD/REDF) >> Movimentos >> Capa Redução Z) do módulo DW.
* CRO: será exibida o CRO da Redução Z. Essa informação será recuperada do campo "CRO (Contador de Reinício de Operação)" da tela Capa Redução Z (menu: Manutenção >> Cupom Fiscal (EFD/REDF) >> Movimentos >> Capa Redução Z) do módulo DW.
o Cupons do Dia
* COO Inicial: será exibida o COO Inicial da Redução Z. Essa informação será recuperada do campo "COO Inicial" da tela Capa Redução Z (menu: Manutenção >> Cupom Fiscal (EFD/REDF) >> Movimentos >> Capa Redução Z) do módulo DW.
* COO Final: será exibida o COO Final da Redução Z. Essa informação será recuperada do campo "COO Final" da tela Capa Redução Z (menu: Manutenção >> Cupom Fiscal (EFD/REDF) >> Movimentos >> Capa Redução Z) do módulo DW.
o Totalizador: será exibido o Totalizador da Redução Z. Essa informação será recuperada do campo "Totalizador" da tela Detalhe da Redução Z (menu: Manutenção >> Cupom Fiscal (EFD/REDF) >> Movimentos >> Detalhe da Redução Z) do módulo DW.
o Descrição: será exibida a Descrição da Redução Z. Essa informação será recuperada do campo "Descrição" da tela Detalhe da Redução Z (menu: Manutenção >> Cupom Fiscal (EFD/REDF) >> Movimentos >> Detalhe da Redução Z) do módulo DW.
o Valor da Operação: será exibido o Valor da Operação da Redução Z. Essa informação será recuperada do campo "Valor da Operação" da tela Detalhe da Redução Z (menu: Manutenção >> Cupom Fiscal (EFD/REDF) >> Movimentos >> Detalhe da Redução Z) do módulo DW.
o Valor Base: será exibido o Valor Base da Redução Z. Essa informação será recuperada do campo "Valor Base" da tela Detalhe da Redução Z (menu: Manutenção >> Cupom Fiscal (EFD/REDF) >> Movimentos >> Detalhe da Redução Z) do módulo DW.
o Valor do Imposto: será exibido o Valor do Imposto da Redução Z. Essa informação será recuperada do campo "Valor do Imposto" da tela Detalhe da Redução Z (menu: Manutenção >> Cupom Fiscal (EFD/REDF) >> Movimentos >> Detalhe da Redução Z) do módulo DW.
OS2943
RN04
Apenas para conhecimento, seguem as tabelas de acordo com os campos que serão recuperados:

* X991_CAPA_REDUCAO_ECF: Manutenção >> Cupom Fiscal (EFD/REDF) >> Movimentos >> Capa Redução Z do módulo DW.
* X992_ITEM_REDUCAO_ECF: Manutenção >> Cupom Fiscal (EFD/REDF) >> Movimentos >> Detalhe da Redução Z do módulo DW.
OS2943


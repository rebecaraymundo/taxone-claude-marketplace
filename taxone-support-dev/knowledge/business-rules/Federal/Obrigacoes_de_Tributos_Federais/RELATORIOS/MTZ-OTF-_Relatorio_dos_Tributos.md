# MTZ-OTF- Relatorio dos Tributos

- **Fonte:** MTZ-OTF- Relatorio dos Tributos.docx
- **Modificado:** 2022-11-10
- **Tamanho:** 33 KB

---

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a># Obrigações de Tributos Federais \- Relatório dos Tributos

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3822

Obrigações de Tributos Federais \- Relatório dos Tributos

O objetivo dessa OS é gerar o relatório analítico e sintético dos tributos da tabela de Controle de Tributos\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

Deverá ser criado uma tela de filtros para a geração do relatório analítico e sintético de Tributos\. Essa tela deverá ser disponibilizada no menu: Relatórios >> Relatório de Tributos\.

__OS3822__

__RN02__

Serão disponibilizados os seguintes campos na tela:

- __Empresa:__ nesse campo, o usuário deverá selecionar a Empresa desejada\. Essa informação será recuperada do cadastro de Empresas \(tabela: EMPRESA\)\. Será exibido o Código da Empresa e a Razão Social da Empresa, separados por hífen\. O usuário só poderá selecionar apenas uma empresa\. Campo obrigatório de preenchimento\. Por default, esse campo irá exibir a Empresa selecionada no Manager\.
- __Estabelecimento:__ nesse campo, o usuário deverá selecionar o Estabelecimento desejado\. Essa informação será recuperada do cadastro de Estabelecimento \(menu: Preliminares >> Empresa/Estabelecimento\) do módulo Parâmetros\. Será exibido o Código do Estabelecimento e a Razão Social do Estabelecimento, separados por hífen\. O usuário só poderá selecionar apenas um estabelecimento\. Campo obrigatório de preenchimento\. Por default, esse campo irá exibir o Estabelecimento selecionado no Manager\. Caso o Manager não esteja com nenhum Estabelecimento selecionado, o usuário poderá selecionar a Estabelecimento\.
- __Período:__ nesse campo, o usuário deverá informar o período \(de e até\) para a geração do relatório\. A data deverá ser informada no formato DD/MM/AAAA \(dia, mês e ano\)\.
- __Código DARF:__ nesse campo, o usuário deverá selecionar ou digitar o Código DARF\. A informação será recuperada do cadastro de Códigos de DARF do sistema \(menu: Manutenção >> Códigos >> Código do DARF\) do módulo DW\. Campo obrigatório de preenchimento\.
- __Tipo do Relatório:__ nesse campo, o usuário irá escolher o tipo de relatório que deseja gerar\. Serão disponibilizadas duas opções para o cliente, sendo que o mesmo só pode selecionar uma delas\. Campo obrigatório de preenchimento\.
	- __Analítico:__ nesse campo, o usuário irá gerar o relatório no formato analítico\.
	- __Sintético:__ nesse campo, o usuário irá gerar o relatório no formato sintético\.
- __Replicar para o\(s\) Estabelecimento\(s\):__ nesse campo, o usuário poderá replicar a geração do relatório para outros estabelecimentos\. Os estabelecimentos serão recuperados do cadastro de Estabelecimento \(menu: Preliminares >> Empresa/Estabelecimento\) do módulo Parâmetros\. Será exibido o Código do Estabelecimento e a Razão Social do Estabelecimento, separados por hífen\. O usuário poderá selecionar um ou mais estabelecimentos\.

__OS3822__

__RN03__

Após preencher os campos para a geração do relatório, o relatório será gerado considerando os seguintes critérios de recuperação:

- Deverão ser recuperados de acordo as retenções do Controle de Tributos \(menu: Manutenção >> Controle de Tributos – aba: Retenções\) do módulo DW ou as retificações das retenções \(aba: Retificações\) caso existam\. Caso exista somente a retenção, deverá ser considerada a mesma\. Caso exista uma retificação a informação recuperada deverá ser a da retificação e caso exista mais de uma retificação deverá ser recuperada a mais recente de acordo com a Data de Retificação informada\.
- Os registros das retenções/retificações deverão ser recuperados a partir do campo “Período” informado\. O campo “Período” irá se basear na Data de Movimento da tela de Controle de Tributos \(menu: Manutenção >> Controle de Tributos – aba: Retenções\) do módulo DW\.
- Caso a retenção esteja com o campo “Cancelado” selecionado, a mesma não será considerada no relatório\.

__OS3822__

__RN04__

Independente do tipo de relatório selecionado para geração – analítico ou sintético – as informações do cabeçalho e rodapé do relatório serão geradas conforme regras abaixo:

- O relatório deverá exibir o Código e a Descrição da Empresa no canto superior esquerdo do relatório\.
- O relatório deverá exibir a Data de Emissão do relatório \(data em que foi gerado\) na parte superior central do mesmo\.
- No canto superior direito deverá ser exibida o número da Página do relatório\.
- No centro do relatório deverá ser exibido o nome do relatório\. O nome do relatório será “Relatório Sintético de Tributos”, caso o relatório seja Sintético\. Caso a opção escolhida seja “Analítico” será exibido “Relatório Analítico de Tributos”\.
- Abaixo do nome do relatório deverá ser exibido o período das informações que estão sendo geradas no relatório\. O período será o mesmo que foi informado no campo “Período” da RN02\.

__OS3822__

__RN04__

No relatório Sintético a quebra será por Código do Estabelecimento, Data do Movimento e Código DARF\. Esses três campos serão exibidos tanto no relatório sintético quanto no relatório analítico\.

__OS3822__

__ RN05__

Após o sistema realizar a quebra por Código do Estabelecimento, Data do Movimento e Código DARF, o sistema irá exibir as colunas “Valor Tributável” e “Valor Retido”\. Esses campos irão exibir o valor tributável e o valor retido de acordo com Código do Estabelecimento, Data do Movimento e Código DARF informados\. 

- __Valor Tributável:__ essa informação deverá ser um somatório do campo 14 – VLR\_BRUTO da tabela X53\_RETENCAO\_IRRF ou X530\_RETIFICACAO\_IRRF caso exista\. Caso exista mais de um registro na tabela X530\_RETIFICACAO\_IRRF, considerar o mais recente\.
- __Valor Retido:__ essa informação deverá ser um somatório do campo 15 – VLR\_IR\_RETIDO da tabela X53\_RETENCAO\_IRRF ou X530\_RETIFICACAO\_IRRF caso exista\. Caso exista mais de um registro na tabela X530\_RETIFICACAO\_IRRF, considerar o mais recente\.

Caso as retenções possuam uma data de movimento que esteja dentro do período de geração do relatório – ver campo “Período” da RN02 – o Valor Tributável e o Valor Retido deverá ser deduzido\. Isso é válido para os documentos que estejam com o campo “Estorno” selecionado\.

As colunas “Valor Tributável” e “Valor Retido” são válidas tanto para o relatório sintético quanto o analítico\.

__OS3822__

__RN06__

Após exibir o Valor Tributável e o Valor Retido, o sistema deverá exibir os totalizadores\. Os totalizadores são:

- __Total Valor Tributável – Data dd/mm/aaaa \(1\): __será exibido o valor total do Valor Tributável para a Data do Movimento em questão\.
- __Total Valor Retido – Data dd/mm/aaaa \(1\): __será exibido o valor total do Valor Retido para a Data do Movimento em questão\.
- __Total Valor Tributável – Código DARF \(1\): __será exibido o valor total do Valor Tributável para o Código DARF em questão\.
- __Total Valor Retido – Código DARF \(1\): __será exibido o valor total do Valor Retido para o Código DARF em questão\.

Os totalizadores são válidos tanto para o relatório sintético quanto o analítico\.

__OS3822__

__RN07__

A tela de detalhe no relatório analítico será exibida quando as retenções possuam uma data de movimento que esteja fora do período de geração do relatório – ver campo “Período” da RN02 – o Valor Tributável e o Valor Retido NÃO deverá ser deduzido\. Isso é válido para os documentos que estejam com o campo “Estorno” selecionado\.

Além disso, o sistema deverá exibir as seguintes informações dos documentos:

- __Pessoa Física/Jurídica:__ essa informação deverá ser recuperada dos campos IND\_FIS\_JUR e COD\_FIS\_JUR da tabela de Controle de Tributos\.
- __Número Documento Fiscal/Série/Subsérie:__ essa informação deverá ser recuperada dos campos NUM\_DOCFIS, SERIE\_DOCFIS e SUB\_SERIE\_DOCFIS da tabela de Controle de Tributos\.
- __Código Operação:__ essa informação deverá ser recuperada do campo COD\_OPERACAONUM\_DOCFIS, SERIE\_DOCFIS e SUB\_SERIE\_DOCFIS da tabela de Controle de Tributos\.
- __Data Retificação:__ essa informação deverá ser recuperada do campo DATA\_RETIFICACAO da tabela de Controle de Tributos\.

__OS3822__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


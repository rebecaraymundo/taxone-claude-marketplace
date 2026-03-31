# MTZ-OTF-Relatorio_de_DARFs

- **Fonte:** MTZ-OTF-Relatorio_de_DARFs.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 50 KB

---

# Obrigações de Tributos Federais \- Relatório de DARF's

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3695

Obrigações de Tributos Federais \- Relatório de DARF's

O cliente PDG Realty gostaria de um relatório que contivesse a relação dos DARF’s existentes no sistema, para que o mesmo pudesse realizar uma conferência desse relatório com as guias geradas no sistema\.

No dia 09/09/2013 \(ver interação 22 do chamado 18578/2012\) solicitamos ao cliente relatórios de exemplo com essas informações e obtivemos retorno do mesmo no dia 01/10/2013 \(ver interação 26\)\. O cliente enviou exemplos para IR e INSS\.

Vale salientar que como a solicitação do usuário foca em um relatório de DARF’s e as retenções de INSS fazem parte de outro tipo de guia de recolhimento – GPS – Guia da Previdência Social – a parte do INSS não será tratada como escopo dessa OS\.

#### Cód\.

### Descrição

###     DR

# RN01

Deverá ser criado no menu: Outras Obrigações >> DARF’s >> Relatórios >> Relatório de DARF’s um novo menu para emissão do relatório de conferência de DARF’s\. Esse menu será disponibilizado no módulo Obrigações de Tributos Federais e será disponibilizado abaixo do menu Outras Obrigações >> DARF’s >> Relatórios >> DARF’s Estornados\.

OS3695

# RN02

Para a geração do relatório, o usuário deverá informar os seguintes campos:

- __Empresa:__ nesse campo, o usuário deve selecionar a Empresa para a geração do relatório\. As informações deverão ser recuperadas da tabela EMPRESA, e deverão ser exibidas da seguinte forma: “Código da Empresa” \+ “Descrição da Empresa”, separadas por hífen \(\-\)\. Além das empresas listadas, deve ser disponibilizada uma opção chamada “Todas”, para que o usuário gere o relatório para todas as empresas\. Campo obrigatório de preenchimento\.
- __Estabelecimento:__ nesse campo, o usuário deve selecionar o Estabelecimento para a geração do relatório\. As informações deverão ser recuperadas da tabela ESTABELECIMENTO de acordo com a Empresa informada no campo anterior e deverão ser exibidas da seguinte forma: “Código do Estabelecimento” \+ “Descrição do Estabelecimento”, separadas por hífen \(\-\)\. Além dos estabelecimentos listados, deve ser disponibilizada uma opção chamada “Todos”, para que o usuário gere o relatório por todos os estabelecimentos da empresa selecionada\. Caso no campo “Empresa” o usuário seleciona a opção “Todas”, esse campo ficará desabilitado para seleção\. Campo obrigatório de preenchimento\.
- __Período:__ nesse campo o usuário deverá informar o período para geração do relatório de DARF’s\. Campo obrigatório de preenchimento\. Esse campo deverá ser informado no formato DD/MM/AAAA\.
- __Códigos DARF:__ nesse campo, o usuário poderá selecionar um ou mais de um Código DARF cadastrados no sistema em sua tabela definitiva \(tabela: SAFX2019\)\. Na abertura da tela, por default, todos os códigos serão exibidos selecionados\. Caso o relatório seja gerado sem nenhum Código DARF selecionado, o relatório não será gerado e será exibida a seguinte mensagem de erro: “Deve ser selecionado pelo menos um Código DARF para a geração do relatório”\.

OS3695

# RN03

Ao informar os dados acima da RN02, o sistema irá recuperar os registros gravados na tela de Manutenção de DARF’s \(menu: Outras Obrigações >> DARF’s >> Manutenção\) do módulo Obrigações de Tributos Federais da seguinte forma:

- Devem ser recuperados todos os registros cadastrados de acordo com a Empresa, Estabelecimento, Período e Código DARF da tela “Manutenção de DARF’s” \(menu: Outras Obrigações >> DARF’s >> Manutenção\) do módulo Obrigações de Tributos Federais\. Caso algum Código DARF não seja selecionado, o mesmo não será considerado no relatório\.
- Caso o usuário selecione todas as Empresas, o relatório será gerado para todas as empresas e todos os estabelecimentos – que o usuário logado possua direito de permissão no módulo Segurança – e respectivamente todos os estabelecimentos\.
- A empresa e o estabelecimento serão recuperados a partir dos campos “Empresa” e “Estabelecimento” da tela “Manutenção de DARF’s” \(menu: Outras Obrigações >> DARF’s >> Manutenção\) do módulo Obrigações de Tributos Federais\.
- O Período informado \(inicial e final\) será recuperado a partir do campo “Data Apuração” da tela “Manutenção de DARF’s” \(menu: Outras Obrigações >> DARF’s >> Manutenção\) do módulo Obrigações de Tributos Federais\.
- O Código DARF será recuperado a partir do campo “DARF” da tela “Manutenção de DARF’s” \(menu: Outras Obrigações >> DARF’s >> Manutenção\) do módulo Obrigações de Tributos Federais\.

Vale salientar que conforme informado anteriormente, os registros serão recuperados da tela de Manutenção dos DARF’s \(tabela: X75\_DCTF\)\. Caso o cliente possua um registro na tabela X751\_DCTF\_COMPL \(que é uma tabela filha da X75\_DCTF\) será recuperado esse registro da tabela filha\. Caso exista mais de um registro na tabela filha \- X751\_DCTF\_COMPL – será recuperado o registro mais recente\.

OS3695

# RN04

As informações do cabeçalho do relatório serão geradas da seguinte forma:

- Na parte superior do relatório, serão geradas as informações da Empresa selecionada, Data e Hora de emissão do relatório e Página do mesmo\.
	- No canto superior esquerdo do relatório, serão informadas as informações da empresa\. A empresa será informada de acordo com a Empresa selecionada\. A Empresa será informada através do Código e Descrição separados por um “\-“\.
	- Na parte central superior será informada a “Data Emissão” do relatório\. Essa informação irá exibir a data e hora que o relatório foi gerado\.
	- No canto direito será exibido o número da página do relatório, que deverá ser sequencial, da primeira página gerada até a última página gerada\. 
- Na parte central do relatório, deverá ser exibido o título do mesmo\. O título do relatório é “Relatório de DARF’s”\.
- Abaixo do título do relatório, deverá ser exibido no formato dd/mm/aaaa, o período de geração do relatório\. Essa informação será recuperada do campo “Período” citado na RN02\.
- Logo mais abaixo será informado o Código do Estabelecimento\. Essa é a primeira quebra do relatório\.

OS3695

# RN05

As informações dos DARF’s serão exibidas através dos seguintes campos:

- __Data Apuração:__ essa informação será recuperada do campo “Data Apuração” da tela “Manutenção de DARF’s” \(menu: Outras Obrigações >> DARF’s >> Manutenção\) do módulo Obrigações de Tributos Federais\.
- __Código DARF: __essa informação será recuperada do campo “DARF” da tela “Manutenção de DARF’s” \(menu: Outras Obrigações >> DARF’s >> Manutenção\) do módulo Obrigações de Tributos Federais\.
- __Código Receita: __essa informação será recuperada do campo “Cód\. Receita” da tela “Manutenção de DARF’s” \(menu: Outras Obrigações >> DARF’s >> Manutenção\) do módulo Obrigações de Tributos Federais\.
- __Valor Base: __essa informação será recuperada do campo “Valor Base” da tela “Manutenção de DARF’s” \(menu: Outras Obrigações >> DARF’s >> Manutenção\) do módulo Obrigações de Tributos Federais\.
- __Alíquota: __essa informação será recuperada do campo “Alíquota” da tela “Manutenção de DARF’s” \(menu: Outras Obrigações >> DARF’s >> Manutenção\) do módulo Obrigações de Tributos Federais\.
- __Valor Total: __essa informação será recuperada do campo “Valor Total” da tela “Manutenção de DARF’s” \(menu: Outras Obrigações >> DARF’s >> Manutenção\) do módulo Obrigações de Tributos Federais\.
- __Data Pagamento: __essa informação será recuperada do campo “Data Pagamento” da tela “Manutenção de DARF’s” \(menu: Outras Obrigações >> DARF’s >> Manutenção\) do módulo Obrigações de Tributos Federais\.
- __Data Pagamento: __essa informação será recuperada do campo “Data Pagamento” da tela “Manutenção de DARF’s” \(menu: Outras Obrigações >> DARF’s >> Manutenção\) do módulo Obrigações de Tributos Federais\.
- __Status: __essa informação será recuperada do campo “Status” da tela “Manutenção de DARF’s” \(menu: Outras Obrigações >> DARF’s >> Manutenção\) do módulo Obrigações de Tributos Federais\. Só poderão ser exibidos as opções “Em Aberto” e “Pago”\.

Ao final do relatório, o sistema deverá exibir os totalizadores:

- __Valor Total de DARF’s por Empresa:__ nesse totalizador deverá ser exibido o Valor Total de DARF’s por consolidados por Empresa\.
- __Valor Total de DARF’s por Estabelecimento:__ nesse totalizador deverá ser exibido o Valor Total de DARF’s por consolidados por Estabelecimento\.
- __Valor Total de DARF’s por Código DARF:__ nesse totalizador deverá ser exibido o Valor Total de DARF’s por consolidados por Código DARF\.
- __Valor Total de DARF’s por Código Receita:__ nesse totalizador deverá ser exibido o Valor Total de DARF’s por consolidados por Código de Receita\.

OS3695

# RN06

A quebra do relatório deverá ser por Empresa, Estabelecimento, Código DARF e Código Receita\.

O início de uma nova página só deve ocorrer quando houver uma nova Empresa e/ou Estabelecimento for iniciado\.

OS3695

# RN07

O relatório poderá ser salvo em Excel, respeitando as tabulações das informações geradas de acordo com o layout do relatório desenhado no requisito\.

OS3695

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


# MTZ-OTF-Relatorio_de_Conferencia_de_INSS

- **Fonte:** MTZ-OTF-Relatorio_de_Conferencia_de_INSS.docx
- **Modificado:** 2021-03-05
- **Tamanho:** 51 KB

---

# Obrigações de Tributos Federais \- Relatório de Conferência de INSS

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3693

Obrigações de Tributos Federais \- Relatório de Conferência de INSS

Os clientes ABB e PDG Realty gostariam de um relatório que listasse as informações das GPS’s – Guia da Previdência Social\. O cliente vai precisar que nesse relatório em específico, sejam listadas as informações das Empresas, Estabelecimentos, Periodo de Geração, Código de Retenção e dos Valores que compõem a GPS\. 

O relatório de Dados para Emissão da GPS informado no chamado 18579\_2012, não atende o cliente, visto que é um relatório de conferência e não pode ser salvo em Excel com as colunas para visualização do cliente\.

CH2359\_2013

Obrigações de Tributos Federais \- Relatório de Conferência de INSS

Complementação do cabeçalho com a inclusão da descrição “Valor INSS retido”

#### Cód\.

### Descrição

###     DR

# RN01

Deverá ser criado no menu Relatórios >> Relatório de Conferência de INSS um novo menu para emissão do relatório de conferência de INSS\. Esse menu será disponibilizado no módulo Obrigações de Tributos Federais e será disponibilizado abaixo do menu Relatório >> Relatório de Inconsistências INSS\.

OS3693

# RN02

Para a geração do relatório, o usuário deverá informar os seguintes campos:

- __Empresa:__ nesse campo, o usuário deve informar a Empresa para a geração do relatório\. As informações deverão ser recuperadas da tabela EMPRESA, e deverão ser exibidas da seguinte forma: “Código da Empresa” \+ “Descrição da Empresa”, separadas por hífen \(\-\)\. Além das empresas listadas, deve ser disponibilizada uma opção chamada “Todas”, para que o usuário gere o relatório por todas as empresas\. Campo obrigatório de preenchimento\.

__Estabelecimento:__ nesse campo, o usuário deve informar o Estabelecimento para a geração do relatório\. As informações deverão ser recuperadas da tabela ESTABELECIMENTO de acordo com a Empresa informada no campo anterior e deverão ser exibidas da seguinte forma: “Código do Estabelecimento” \+ “Descrição do Estabelecimento”, separadas por hífen \(\-\)\. Além dos estabelecimentos listados, deve ser disponibilizada uma opção chamada “Todos”, para que o usuário gere o relatório por todos os estabelecimentos da empresa selecionada\. Caso no campo “Empresa” o usuário seleciona a opção “Todas”, esse campo ficará desabilitado para seleção\. Campo obrigatório de preenchimento\.

- __Período:__ nesse campo o usuário deverá informar o período para geração das GPS’s\. Campo obrigatório de preenchimento\. Esse campo deverá ser informado no formato DD/MM/AAAA\.
- __Código Pagamento INSS:__ nesse campo o usuário poderá pesquisar todos os Códigos de Pagamento de INSS cadastrados no sistema \(tabela: IRT\_COD\_PG\_INSS\) para pesquisa\. Os Códigos de INSS deverão ser exibidos através dos campos “Código Pagamento” \+ “Descrição Pagamento” separados por hífen \(\-\)\. Campo não obrigatório de preenchimento\.

Ao informar os dados acima, o sistema irá recuperar os registros gravados na tela de Manutenção de Dados de INSS  da seguinte forma:

- Devem ser recuperados todos os registros cadastrados de acordo com a Empresa, Estabelecimento, Período e Código Pagamento INSS \(se aplicável\) da tela Digitação GPS do módulo Obrigações de Tributos Federais \(menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> GPS >> Digitação\);
- O período informado irá respeitar o campo “Mês/Ano Competência” da tela Digitação GPS do módulo Obrigações de Tributos Federais \(menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> GPS >> Digitação\);

Vale salientar que serão recuperados os registros da tela Digitação GPS independente se o registro foi gerado automaticamente – através da rotina de geração da GPS – ou se a mesma foi incluída manualmente\.

OS3693

# RN03

As informações do cabeçalho do relatório serão geradas da seguinte forma:

- Na parte superior do relatório, serão geradas as informações da Empresa selecionada, Data e Hora de emissão do relatório e Página do mesmo\.
	- No canto superior esquerdo do relatório, serão informadas as informações da empresa\. A empresa será informada de acordo com a Empresa selecionada\. A Empresa será informada através do Código e Descrição separados por um “\-“\.
	- Na parte central superior será informada a “Data Emissão” do relatório\. Essa informação irá exibir a data e hora que o relatório foi gerado\.
	- No canto direito será exibido o número da página do relatório, que deverá ser sequencial\. 
- Na parte central do relatório, deverá ser exibido o título do mesmo\. O título do relatório é “Relatório de Conferência dos INSS”\.
- Abaixo do título do relatório, deverá ser exibido no formato dd/mm/aaaa, o período de geração do relatório\. Essa informação será recuperada do campo “Período” citado na RN02\.
- Logo mais abaixo será informado o Código do Estabelecimento\. Essa é a primeira quebra do relatório\.
- Abaixo do Código Estabelecimento será informado o Código de Pagamento do INSS\. A primeira quebra do relatório é por Estabelecimento, seguida do Código de Pagamento do INSS\.

OS3693

# RN04

As informações da GPS serão exibidas através dos seguintes campos:

- __Prestador__
	- __CNPJ: __essa informação será recuperada a partir do CNPJ da SAFX04, de acordo com o campo “Pessoa Física/Jurídica” da tela Digitação GPS\.
	- __Razão Social: __essa informação será recuperada a partir da Razão Social da SAFX04, de acordo com o campo “Pessoa Física/Jurídica” da tela Digitação GPS\.
- __Mês/Ano Competência:__ essa informação será recuperada a partir do campo “Mês/Ano Competência” da tela Digitação GPS\.
- __Valor INSS: __essa informação será recuperada a partir do campo “Valor INSS” da tela Digitação GPS\.
- __Valor Outras Entidades: __essa informação será recuperada a partir do campo “Valor Outras Entidades” da tela Digitação GPS\.
- __Valor Juros: __essa informação será recuperada a partir do campo “Juros” da tela Digitação GPS\.
- __Valor Multa: __essa informação será recuperada a partir do campo “Multa” da tela Digitação GPS\.
- __Valor Total Recolhimento: __essa informação será recuperada a partir do campo “Total Recolhimento” da tela Digitação GPS\.

Ao final do relatório, o sistema deverá exibir os totalizadores:

- __Total do Código Pagamento:__ nesse totalizador deverá ser exibido o Valor Total Recolhimento por Código de Pagamento INSS por Código de Pagamento\.
- __Total do Estabelecimento:__ nesse totalizador deverá ser exibido o Valor Total Recolhimento por Código de Pagamento INSS por Estabelecimento\.
- __Total da Empresa:__ nesse totalizador deverá ser exibido o Valor Total Recolhimento por Código de Pagamento INSS por Empresa\.

OS3693

# RN05

A quebra do relatório deverá ser por Empresa, Estabelecimento e Código de Pagamento INSS\.

O início de uma nova página só deve ocorrer quando houver uma nova Empresa e/ou Estabelecimento for iniciado\.

OS3693

# RN06

O relatório poderá ser salvo em Excel, respeitando as tabulações das informações geradas de acordo com o layout do relatório desenhado no requisito\.

OS3693

# RN07

Inclusão do nome “Valor INSS retido” na coluna respectiva à retenção do imposto\.

CH2359\_2013

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


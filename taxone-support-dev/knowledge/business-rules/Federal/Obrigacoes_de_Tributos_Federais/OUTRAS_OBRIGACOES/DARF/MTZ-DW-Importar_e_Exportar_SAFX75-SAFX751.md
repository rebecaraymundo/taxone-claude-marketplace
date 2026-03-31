# MTZ-DW-Importar_e_Exportar_SAFX75-SAFX751

- **Fonte:** MTZ-DW-Importar_e_Exportar_SAFX75-SAFX751.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 46 KB

---

# Obrigações de Tributos Federais \- Gerar DARF's Complementares e Compensações de Créditos

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3267\-A1

Obrigações de Tributos Federais \- Gerar DARF's Complementares e Compensações de Créditos

Será desenvolvida nessa OS uma rotina que permita que após os DARF’s com status “Em Aberto” e “Pago” visualizados através de telas de manutenção do DARF Original e Complementar\. Os valores dos créditos gerados por esses DARF’s, além das compensações que esses DARF’s por ventura tenham utilizado também serão objeto dessa OS\.

Além disso, essa OS irá tratar o pagamento dos DARF’s Originais e Complementares através da alteração da rotina de Importação Online e Importação Batch para as tabelas X75\_DCTF e X751\_DCTF\_COMPL\.

#### Cód\.

### Descrição

### DR

# RN01

Deverá ser criado o parâmetro “Importar DARF’s Complementares”\. Esse parâmetro será disponibilizado na tela de programação da Importação Online\. Serão exibidas duas opções: “Sim” e “Não”\.

O parâmetro “Importar DARF’s Complementares” será criado após o campo “Importar Retificações de Retenções”\. A atualização acontecerá na rotina de Execução da Importação Online\.

OS3267\-A1

# RN02

Ao executar a rotina de Importação Online, o sistema deverá verificar o parâmetro “Importar DARF’s Complementares”\. Nesse caso a regra para importação é a seguinte:

- Caso seja selecionada a opção “Sim”, todos os DARF’s que estiverem sendo importados serão atualizados na tabela X75\_DCTF desde que o campo STATUS = “A”, assim como os DARF’s que estiverem na tabela X751\_DCTF\_COMPL desde que o campo STATUS = “A” e IND\_DEB\_CRED = “D”\. Dessa forma os DARF’s da tabela X75\_DCTF e X751\_DCTF\_COMPL serão atualizados normalmente\. Esse parâmetro só será disponibilizado para a tabela SAFX75\. 
- Caso seja selecionada a opção “Não”, os DARF’s só serão atualizados na tabela X75\_DCTF desde que o campo STATUS = “A”\. Dessa forma para que os DARF’s existentes na tabela X751\_DCTF\_COMPL sejam considerados como pagos, a opção “Sim” sempre deve ser selecionada\.

Serão atualizados os campos “Data Pagamento”, “Observação”, “Data Envio Bancário” e “Autenticação Bancária”\. Para que os DARF’s sejam considerados Pagos \(STATUS = “P”\) deverão ser considerados preenchidos os campos de “Data Pagamento” e “Autenticação Bancária”\.

OS3267\-A1

# RN03

Deverá ser criado o parâmetro “Importar DARF’s Complementares”\. Esse parâmetro será disponibilizado na tela de programação da Importação Batch\. Serão exibidas duas opções: “Sim” e “Não”\.

O parâmetro “Importar DARF’s Complementares” será criado após o campo “Importar Retificações de Retenções”\. A atualização acontecerá na rotina de Execução da Importação Batch\.

OS3267\-A1

# RN04

Ao executar a rotina de Importação Batch, o sistema deverá verificar o parâmetro “Importar DARF’s Complementares”\. Nesse caso a regra para importação é a seguinte:

- Caso seja selecionada a opção “Sim”, todos os DARF’s que estiverem sendo importados serão atualizados na tabela X75\_DCTF desde que o campo STATUS = “A”, assim como os DARF’s que estiverem na tabela X751\_DCTF\_COMPL desde que o campo STATUS = “A” e IND\_DEB\_CRED = “D”\. Dessa forma os DARF’s da tabela X75\_DCTF e X751\_DCTF\_COMPL serão atualizados normalmente\. Esse parâmetro só será disponibilizado para a tabela SAFX75\. 
- Caso seja selecionada a opção “Não”, os DARF’s só serão atualizados na tabela X75\_DCTF desde que o campo STATUS = “A”\. Dessa forma para que os DARF’s existentes na tabela X751\_DCTF\_COMPL sejam considerados como pagos, a opção “Sim” sempre deve ser selecionada\.

Serão atualizados os campos “Data Pagamento”, “Observação”, “Data Envio Bancário” e “Autenticação Bancária”\. Para que os DARF’s sejam considerados Pagos \(STATUS = “P”\) deverão ser considerados preenchidos os campos de “Data Pagamento” e “Autenticação Bancária”\.

OS3267\-A1

# RN05

Deverá ser criado o parâmetro “Exportar DARF’s Complementares”\. Esse parâmetro será disponibilizado na tela de programação da Exportação de Dados, após a coluna “Importar Retificações de Retenções”\. Serão exibidas duas opções: “Sim” e “Não”\.

O parâmetro “Exportar DARF’s Complementares” será criado após o campo “Importar Retificações de Retenções”\. A atualização acontecerá na rotina de Execução da Exportação de Dados\.

OS3267\-A1

# RN06

A regra da utilização do parâmetro no processo de exportação é o seguinte:

- Caso o parâmetro “Exportar DARF’s Complementares” esteja selecionado com a opção “Sim” na tela de Programação para a Exportação de Dados da tabela SAFX75, a exportação irá considerar os DARF’s existentes na tabela X75\_DCTF e os da tabela X751\_DCTF\_COMPL com o campo IND\_DEB\_CRED = “D” no arquivo exportado\.
- Caso o parâmetro “Exportar DARF’s Complementares” esteja selecionado com a opção “Não” na tela de Programação para a Exportação de Dados da tabela SAFX75, a exportação irá considerar apenas os DARF’s existentes na X75\_DCTF e __NÃO IRÁ CONSIDERAR__ os DARF’s Complementares existentes na tabela X751\_DCTF\_COMPL com o campo IND\_DEB\_CRED = “D” no arquivo exportado\.

Além disso, os campos DATA\_APURACAO\_X751 e NRO\_REFERENCIA\_X751 serão informados nos registros gerados da tabela X751\_DCTF\_COMPL\. No caso da tabela X75\_DCTF, esses campos serão informados com @\.

OS3267\-A1

# RN07

A rotina de Carga deverá ser alterada para contemplar os novos campos criados na tabela SAFX75\. Os campos criados são:

- DATA\_APURACAO\_COMPL: deverá ser um campo alfanumérico de 8 posições não obrigatório\.
- NRO\_REFERENCIA\_COMPL: deverá ser um campo alfanumérico de 15 posições não obrigatório\.

OS3267\-A1

# RN08

As rotinas de Importação Online e Importação Batch deverão ser alteradas para contemplar os novos campos criados na tabela SAFX75\. Os campos criados são:

- DATA\_APURACAO\_COMPL: deverá ser um campo alfanumérico de 8 posições não obrigatório\.
- NRO\_REFERENCIA\_COMPL: deverá ser um campo alfanumérico de 15 posições não obrigatório\.

OS3267\-A1

# RN09

A rotina de Exportação deverá ser alterada para contemplar os novos campos criados na tabela SAFX75\. Os campos criados são:

- DATA\_APURACAO\_COMPL: deverá ser um campo alfanumérico de 8 posições não obrigatório\.
- NRO\_REFERENCIA\_COMPL: deverá ser um campo alfanumérico de 15 posições não obrigatório\.

OS3267\-A1

# RN10

As rotinas de Importação Online ou Importação Batch devem importar com sucesso o registro de DARF Complementar caso os campos DATA\_APURACAO\_X751 e NRO\_REFERENCIA\_X751 estejam preenchidos\. Além disso, somente é permitido importar o registro de DARF Complementar caso o registro do DARF Original esteja pago \(campo STATUS = P da X75\_DCTF\)\.

Algumas críticas devem ser consideradas durante esse processo de importação\.

- Caso o campo DATA\_APURACAO\_COMPL esteja preenchido e o campo NRO\_REFERENCIA\_COMPL não esteja preenchido não deverá ser permitida a importação e deverá ser exibida mensagem de erro:
	- O campo de Data de Apuracao Complementar preenchido e o Numero de Referencia Complementar nao preenchido\. Nao e possivel tratar o DARF Complementar\.
- Caso o campo DATA\_APURACAO\_COMPL não esteja preenchido e o campo NRO\_REFERENCIA\_COMPL esteja preenchido não deverá ser permitida a importação e deverá ser exibida mensagem de erro:
	- O campo de Data de Apuracao Complementar nao preenchida e o Numero de Referencia Complementar preenchido\. Nao e possivel tratar o DARF Complementar\.
- Caso o campo NUM\_QUOTA > 0
	- O DARF Complementar nao pode estar associado a um DARF parcelado em Quotas\.
- O DARF Complementar nao possui um DARF Original – registro na X75\_DCTF – com campo STATUS = “P”\.
	- DARF não encontrado na base de dados\. Somente e possível importar informações de DARFs Complementares a partir da DARFs pagos
- Não existe na X751\_DCTF\_COMPL registro referente ao proprio DARF Complementar que está se tentando importar\.
	- DARF Complementar não encontrado na base de dados

OS3267\-A1

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


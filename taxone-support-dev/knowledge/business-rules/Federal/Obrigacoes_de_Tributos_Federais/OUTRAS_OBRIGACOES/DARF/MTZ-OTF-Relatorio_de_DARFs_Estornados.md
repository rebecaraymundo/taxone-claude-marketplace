# MTZ-OTF-Relatorio_de_DARFs_Estornados

- **Fonte:** MTZ-OTF-Relatorio_de_DARFs_Estornados.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 50 KB

---

# Obrigações de Tributos Federais \- Relatório de DARF's Estornados

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3753

Obrigações de Tributos Federais \- Relatório de DARF's Estornados

O cliente Caixa Seguradora possui um processo interno de estorno de retenções\. O conceito de estorno de retenções é quando o cliente deseja reaver o valor de uma retenção indevida\. Isso pode ocorrer em três momentos distintos no produto:

- __Retenção sem DARF Gerado:__ esse é o caso mais simples, o cliente importou uma retenção no produto, porém antes mesmo de gerar o DARF referente a essa retenção, o cliente percebeu o erro\. 
- __Retenção com DARF Gerado e Não Pago:__ esse caso é o cenário principal do cliente, pois ele envia o DARF para pagamento e por motivos de erro no sistema bancário – exemplo: conta inválida ou encerrada, CPF inválido, entre outros – o pagamento não é processado\. Nesse caso o cliente tem que estornar o valor no ERP \(SAP\) para que essa retenção não seja considerada em nenhuma obrigação acessória\.
- __Retenção com DARF Gerado e Pago: __esse cenário já está resolvido dentro do sistema, pois se o cliente pagou um DARF indevidamente – a maior ou a menor – o cliente pode resolver essa situação através da funcionalidade de Tributos Ajustados já disponibilizada no produto\.

A solução proposta inicialmente seria a criação de dois campos de identificação na tabela de Controle de Tributos: “Estorno” e “Data do Estorno”\. Esses campos iriam identificar a retenção estornada e não permitir que a mesma seja considerada nas obrigações acessórias federais e relatórios de conferência do sistema\. São eles:

- Obrigações Acessórias
	- DCTF
	- DIRF
	- Informe de Rendimentos
- Relatórios Gerenciais
	- Relatório de Tributos Federais
	- Relatório de Rastreabilidade

Hoje a rotina de importação do produto não permite a importação de uma retenção que tenha um DARF vinculado à mesma e que esteja Gerado/Não Pago ou Pago\. Isso é um controle do sistema para garantir que um DARF fique diferente da retenção, ocasionando erros críticos para o cliente\. Esse controle funciona assim de longa data e no passado já foram dados NO GO para que isso fosse permitido\.

Com esse cenário do cliente, o sistema deverá permitir que na rotina de importação da tabela de Controle de Tributos – SAFX53 – o sistema ao identificar os campos “Estorno” e “Data do Estorno” preenchidos, o sistema deverá fazer a seguinte identificação:

- __Retenção sem DARF Gerado:__ nesse caso a retenção será atualizada sem maiores ônus\. 
- __Retenção com DARF Gerado e Não Pago:__ nesse caso, o sistema irá identificar o DARF dessa retenção e irá à tabela X75\_DCTF apagar esse DARF\. Essa retenção e as outras associadas ao DARF que foi deletado, terão seu status alterado para “Não Gerado”\. Essas retenções terão o campo “Estorno” e “Data do Estorno” informados\.
- __Retenção com DARF Pago:__ nesse caso o cliente deverá utilizar o sistema de acordo com a funcionalidade de Tributos Ajustados já existente no sistema\. 

É importante que no segundo ponto o DARF seja deletado, porque as retenções com Estorno não serão consideradas nas obrigações federais\. Se isso não for desenvolvido ao gerar a DCTF o cliente irá ter uma Ficha de Pagamento \(R11\) sem uma Ficha de Débito vinculada\.

Vale salientar que o escopo da OS3753 será somente em cima da importação e do relatório de DARF’s estornados\. O fato das obrigações acessórias e dos relatórios gerenciais do sistema não considerarem as retenções com estorno, as mesmas serão desenvolvidas posteriormente\.

#### Cód\.

### Descrição

###     DR

# RN01

Deverá ser criado no menu Outras Obrigações >> DARF’s >> Relatórios >> DARF’s Estornados um novo menu para emissão do relatório de DARF’s estornados\. Esse menu será disponibilizado no módulo Obrigações de Tributos Federais, abaixo do menu do Relatório de Rastreabilidade\.

OS3753

# RN02

Para a geração do relatório, o usuário deverá informar os seguintes campos:

- __Empresa:__ nesse campo, o usuário deve informar a Empresa para a geração do relatório\. As informações deverão ser recuperadas da tabela EMPRESA, e deverão ser exibidas da seguinte forma: “Código da Empresa” \+ “Descrição da Empresa”, separadas por hífen \(\-\)\. Campo obrigatório de preenchimento\.
- __Estabelecimento:__ nesse campo, o usuário deve informar o Estabelecimento para a geração do relatório\. As informações deverão ser recuperadas da tabela ESTABELECIMENTO de acordo com a Empresa informada no campo anterior e deverão ser exibidas da seguinte forma: “Código do Estabelecimento” \+ “Descrição do Estabelecimento”, separadas por hífen \(\-\)\. Campo obrigatório de preenchimento\.
- __Data de Apuração:__ nesse campo, o usuário deve informar a Data de Apuração, no formato DD/MM/AAAA\. O usuário deverá informar um período DE e outro ATÉ\. Campo obrigatório de preenchimento\.
- __Código DARF:__ nesse campo, o usuário deverá informar o Código DARF\. O sistema irá recuperar a informação a partir dos DARF’s estornados que constarem na tabela HIST\_X75\_DCTF\. O sistema irá permitir que mais de um Código DARF seja selecionado\. Campo obrigatório de preenchimento\.

Ao informar os dados acima, o sistema irá recuperar os registros gravados na tabela\-clone da X75\_DCTF, aonde serão gravados os DARF’s que foram excluídos da tabela X75\_DCTF durante a rotina de importação das retenções estornadas\.

*OBS: o nome da tabela\-clone será definido no documento de A&D\.*

- Devem ser recuperados todos os registros cadastrados de acordo com a Empresa, Estabelecimento, Data de Apuração e Código DARF \(se aplicável\) da tabela\-clone da X75\_DCTF\.

OS3753

# RN03

As informações do cabeçalho do relatório serão geradas da seguinte forma:

- Na parte superior do relatório, serão geradas as informações da Empresa selecionada, Data e Hora de emissão do relatório e Página do mesmo\.
	- No canto superior esquerdo do relatório, serão informadas as informações da empresa\. A empresa será informada de acordo com a Empresa selecionada\. A Empresa será informada através do Código e Descrição separados por um “\-“\.
	- Na parte central superior será informada a “Data Emissão” do relatório\. Essa informação irá exibir a data e hora que o relatório foi gerado\.
	- No canto direito será exibido o número da página do relatório, que deverá ser sequencial\. 
- Na parte central do relatório, deverá ser exibido o título do mesmo\. O título do relatório é “Relatório de DARF’s Estornados”\.
- Abaixo do título do relatório, deverá ser exibido no formato dd/mm/aaaa, o período de geração do relatório\. Essa informação será recuperada do campo “Data de Apuração” citado na RN02\.
- Logo mais abaixo será informado o Código do Estabelecimento\. Essa é a primeira quebra do relatório\.
- Abaixo do Código Estabelecimento será informado o Código DARF\. A primeira quebra do relatório é por Estabelecimento, seguida do Código DARF\.

OS3753

# RN04

As informações da GPS serão exibidas através dos seguintes campos:

- __Data da Apuração: __essa informação será recuperada a partir do campo “Data Apuração” da tabela\-clone da X75\_DCTF\.
- __Grupo Tributo: __essa informação será recuperada a partir do campo “Grupo Tributo” da tabela\-clone da X75\_DCTF\.
- __Código Receita: __essa informação será recuperada a partir do campo “Cod\. Receita” da tabela\-clone da X75\_DCTF\.
- __Código Operação: __essa informação será recuperada a partir do campo “Cod\. Operação” da tabela\-clone da X75\_DCTF\.
- __Valor Principal: __essa informação será recuperada a partir do campo “Valor Principal” da tabela\-clone da X75\_DCTF\.
- __Valor Multa: __essa informação será recuperada a partir do campo “Valor Multa” da tabela\-clone da X75\_DCTF\.
- __Valor Juros: __essa informação será recuperada a partir do campo “Valor Juros” da tabela\-clone da X75\_DCTF\.
- __Valor Total: __essa informação será recuperada a partir do campo “Valor Total” da tabela\-clone da X75\_DCTF\.

Ao final do relatório, o sistema deverá exibir os totalizadores:

- __Total do Código DARF:__ nesse totalizador deverá ser exibido o Valor Total por Código DARF, ou seja, será totalizado a partir do campo “Valor Total” por Código DARF\.
- __Total do Estabelecimento:__ nesse totalizador deverá ser exibido o Valor Total por Estabelecimento, ou seja, será totalizado a partir do campo “Valor Total” por Estabelecimento\.
- __Total da Empresa:__ nesse totalizador deverá ser exibido o Valor Total por Empresa, ou seja, será totalizado a partir do campo “Valor Total” por Empresa\.

OS3753

# RN05

A quebra do relatório deverá ser por Empresa, Estabelecimento e Código DARF\.

OS3753

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


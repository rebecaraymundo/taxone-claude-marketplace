# MTZ-OTF-Rotina_de_Compensacao

- **Fonte:** MTZ-OTF-Rotina_de_Compensacao.docx
- **Modificado:** 2022-02-02
- **Tamanho:** 56 KB

---

# Obrigações de Tributos Federais \- Rotina de Compensação dos Créditos/Débitos, Relatório de Débitos/Créditos e Emissão dos DARF's Complementares

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3267\-B

Obrigações de Tributos Federais \- Rotina de Compensação dos Créditos/Débitos, Relatório de Débitos/Créditos e Emissão dos DARF's Complementares

Será desenvolvida uma rotina que permita que o usuário realize a compensação dos créditos com os débitos e vice\-versa e emita os DARF’s Complementares gerados a partir da tabela X751\_RETIFICACAO\_IRRF\.

OS3916

Obrigações de Tributos Federais – Alterar Forma de Compensação dos Tributos Federais

O objetivo deste documento de requisito é permitir que os valores informados nos campos “Valor Principal Devido Compensado \(2\)”, “Multas \(3\)” e “Juros \(4\)” não possua críticas caso sua soma seja igual a soma dos campos “Valor Original Compensado Crédito \(5\)” e “Valor Monetário Compensado \(6\)”, no momento da compensação dos valores dos DARF’s\.

#### Cód\.

### Descrição

### DR

# RN01

Na aba “Compensações/Créditos de Tributos Federais”, deverá ser criado a tela de “Compensações de Créditos/DARF’s Complementares”\. Nessa tela será permitida a compensação dos créditos com os débitos, assim como dos débitos com os créditos\. 

Essa tela será disponibilizada após o usuário gerar a prévia dos DARF’s \(registros na tabela X751\_DCTF\_COMPL com campo STATUS = “G”\)\.

__OBS: __essa tela substitui a aba de mesmo nome criada na OS3267\-A\.

OS3267\-B

# RN02

O usuário poderá filtrar as informações para geração\. Serão recuperados todos os créditos que estiverem nas seguintes condições:

- Créditos da tabela X751\_DCTF\_COMPL quando o campo IND\_DEB\_CRED = “C” e que ainda possua créditos a serem utilizados;
- Registros da tela de Saldos Credores cujo campo “Saldo” > 0\.

Serão exibidos a Empresa e o Estabelecimento informados na tela de parâmetros para geração\.

- __Empresa: __nesse campo será exibida a Empresa para filtro da informação\. Campo obrigatório de preenchimento\.
- __Estabelecimento: __nesse campo será exibido o Estabelecimento para filtro da informação\. Campo obrigatório de preenchimento\. O usuário poderá selecionar a opção “Todos”\.
- __Código DARF: __nesse campo o usuário deverá digitar o Código DARF do Crédito\. Campo numérico de 4 posições não obrigatório de preenchimento\.

OS3267\-B

# RN03

Os créditos serão disponibilizados conforme regra abaixo:

- __Empresa:__ será exibida a Empresa detentora do Crédito\. Só será exibida a Empresa que o usuário tenha selecionado na tela de geração dos DARF’s\.
- __Estabelecimento:__ serão exibidos todos os Estabelecimentos relacionados à empresa que possui crédito\. 
- __Código DARF:__ serão exibidos os Códigos DARF dos Créditos da tabela X751\_DCTF\_COMPL cujo campo IND\_DEB\_CRED = “C” e que ainda possuam créditos, além dos Saldos Credores cujo Saldo seja maior que 0 \(zero\)\. 
- __Número Documento Pagamento:__ serão exibidos os Números de Documento de Pagamento \(campo: NRO\_PAGTO\) dos Créditos da tabela de Saldos Credores e que ainda possuam créditos\.
- __Código Operação:__ serão exibidos os Códigos de Operação do Crédito\. Essa informação será recuperada a partir do campo “Código Operação” da X751\_DCTF\_COMPL cujo campo IND\_DEB\_CRED = “C”\. No caso dos Saldos Credores não será exibida informação nesse campo, pois o mesmo não é preenchido na manutenção de Saldo Credor\.
- __Valor a Compensar:__ será exibido o Valor Total do DARF dos Créditos da tabela X751\_DCTF\_COMPL cujo campo IND\_DEB\_CRED = “C” e que ainda possuam créditos, além dos Saldos Credores cujo Saldo seja maior que 0 \(zero\)\. Para os Saldos Credores, a informação deverá ser recuperada do campo “Valor a Compensar”\.
- __Valor Compensado:__ será exibido o Valor Compensado dos Créditos da tabela X751\_DCTF\_COMPL cujo campo e IND\_DEB\_CRED = “C” e que ainda possuam créditos, além dos Saldos Credores cujo Saldo seja maior que 0 \(zero\)\. Caso o Crédito que esteja selecionado tenha sido associado a um ou mais Débitos na parte de Detalhes das Compensações de Tributos Federais, o valor utilizado no campo \(5\) deverá ser adicionado nessa coluna\.
- __Saldo:__ será exibido o Saldo dos Créditos da tabela X751\_DCTF\_COMPL cujo campo IND\_DEB\_CRED = “C” e que ainda possuam créditos, além dos Saldos Credores cujo Saldo seja maior que 0 \(zero\)\.\. O Saldo será “Valor a Compensar” – “Valor Compensado”\.
- __Origem:__ será exibida a origem do Saldo Credor\. Caso seja da tabela X751\_DCTF\_COMPL cujo campo IND\_DEB\_CRED = “C” e que ainda possuam créditos deverá ser exibido “DARF com Crédito”\. Caso seja da tela de manutenção do Saldo Credor, deverá ser exibido “Saldo Credor”\.

Caso o usuário ao visualizar o crédito selecione o mesmo, na parte de baixo da tela – Detalhes das Compensações dos Tributos Federais – serão exibidos os débitos que estão associados ao crédito selecionado\. Serão exibidos esses vínculos somente do período de apuração corrente, ou seja, do período de apuração em que a compensação está ocorrendo\. As vinculações ocorridas em períodos de apuração anteriores, não serão exibidas\. Essa informação será exibida mais tarde em um relatório de rastreabilidade\.

Os créditos que por ventura não possuam mais créditos passíveis de compensação, não deverão ser exibidos\.

Só deverão ser exibidos os créditos do período informado na tela de geração\. Créditos de período posteriores não deverão ser exibidos\. Para que os créditos sejam recuperados com sucesso deverão ser considerados os seguintes campos

- No caso de Saldo Credor, deve\-se recuperar a partir da Data de Pagamento
- No caso de Crédito de DARF – X751\_DCTF\_COMPL – deve\-se recuperar a partir da Data da Apuração da X751 \(DATA\_APURACAO\_X751\)\.

OS3267\-B

# RN04

Ao escolher um Crédito, serão exibidos os confrontos \(Débitos\)\. Nessa visualização serão exibidos todos os Débitos das tabelas X75\_DCTF cujo campo STATUS = “G” e X751\_DCTF\_COMPL cujo campo STATUS = “G” e IND\_DEB\_CRED = “D”\. 

O usuário poderá filtrar os Débitos pelos campos “Estabelecimento” e “Código DARF”\. As informações exibidas desses DARF’s serão Estabelecimento, Código DARF e Valor Principal – isso ocorre, pois o DARF ainda não tem incidência de Juros e Multa\. Os DARF’s da parte de Confrontos serão filtrados através da Empresa informada no filtro principal da RN02\.

Os confrontos serão exibidos logo após a pesquisa dos Créditos\. Serão listados os primeiros confrontos, cabendo ao utilizar a barra de rolagem para visualizar outros débitos\. Caberá ao usuário também fazer a pesquisa através dos campos “Estabelecimento” e “Código DARF”\.

O usuário poderá escolher apenas um Crédito, porém na parte de Confrontos \(Débitos\) poderão ser escolhidos quantos Débitos o mesmo desejar\.

Não será permitida que para um débito sejam associados mais de um crédito\.

O usuário ao escolher o Débito na parte de Confrontos deverá enviá\-lo para a parte de Detalhes da Compensação de Créditos de Tributos Federais\. Uma vez lá, esse Débito \(DARF\) não será exibido na parte de Confrontos para nenhum outro crédito selecionado\.

OS3267\-B

# RN05

Ao selecionar o Crédito e o\(s\) Débito\(s\) o usuário poderá determinar quais débitos vão ter seu valor abatido pelo Crédito\. Na parte inferior da tela serão exibidos os seguintes campos:

- __Código DARF:__ será exibido o Código DARF do DARF da tabela X75\_DCTF cujo campo STATUS = “G” ou da tabela X751\_DCTF\_COMPL cujo campo STATUS = “G” e IND\_DEB\_CRED = “D”\. Campo não editável\.
- __Código Receita:__ será exibido o Código Receita do DARF da tabela X75\_DCTF cujo campo STATUS = “G” ou da tabela X751\_DCTF\_COMPL cujo campo STATUS = “G” e IND\_DEB\_CRED = “D”\. Campo não editável\.
- __Período:__ será exibido o período do DARF\. O período vai ser formato pelo mês/ano de acordo com a Data de Apuração do DARF\. Essa informação será recuperada da tabela X75\_DCTF cujo campo STATUS = “G” ou da tabela X751\_DCTF\_COMPL cujo campo STATUS = “G” e IND\_DEB\_CRED = “D”\. Campo não editável\.
- __Valor Principal Devido \(1\):__ será exibido o Valor Total do DARF \(Valor do Principal\) da tabela X75\_DCTF cujo campo STATUS = “G” ou da tabela X751\_DCTF\_COMPL cujo campo STATUS = “G” e IND\_DEB\_CRED = “D”\. Campo não editável\. Esse campo não tem incidência de Juros e Multa, pois os mesmos não foram calculados ainda\.
- __Valor Principal Devido Compensado \(2\):__ o usuário deverá informar o Valor do Principal Devido Compensado\. Trata\-se do valor que ele está querendo compensar do débito\. Esse campo deverá ser numérico de 17 posições, sendo 15 inteiras e 2 decimais\. Campo editável\.
	- Caso o valor informado nesse campo seja maior do que o campo “Saldo” do Crédito selecionado deverá ser exibida mensagem de erro “Valor Principal Devido Compensado não pode ser maior do que o Saldo do Crédito\. Por gentileza corrigir o valor\.”\. O sistema não deverá permitir a continuação da compensação até que o usuário corrija o valor\.
	- Caso o valor informado nesse campo seja = 0 \(zero\), deverá ser exibida mensagem de erro “Valor Principal Devido Compensado não pode ser igual a 0\. Por gentileza corrigir o valor\.”\. O sistema não deverá permitir a continuação da compensação até que o usuário corrija o valor\.
- __Multas \(3\):__ o usuário poderá informar o valor das multas sob o crédito\. Esse campo deverá ser numérico de 17 posições, sendo 15 inteiras e 2 decimais\. O valor de Multas é informativo, ou seja, trata\-se do valor de Multa sob o crédito caso o mesmo já esteja vencido\. Campo editável\.
- __Juros \(4\):__ o usuário poderá informar o valor dos juros sob o crédito\. Esse campo deverá ser numérico de 17 posições, sendo 15 inteiras e 2 decimais\. O valor de Juros é informativo, ou seja, trata\-se do valor de Juros sob o crédito caso o mesmo já esteja vencido\. Campo editável\.
- __Valor Original Compensado do Crédito \(5\):__ o usuário deverá informar o Valor Original Compensado\. Esse campo deverá ser numérico de 17 posições, sendo 15 inteiras e 2 decimais\. Esse campo ao ser informado deverá ser utilizado para abater o valor do crédito selecionado na parte superior da tela\. Para abater o valor do crédito selecionado, o valor informado nesse campo \(5\) irá compor o valor do campo “Valor Compensado” do crédito selecionado\. Campo editável\.
	- Caso o valor informado nesse campo seja maior do que o valor do Crédito selecionado, deverá ser exibida mensagem de erro “Valor Original Compensado do Crédito não pode ser maior do que o Valor a Compensar do Crédito selecionado\. Por gentileza corrigir o valor\.”\. O sistema não deverá permitir a continuação da compensação até que o usuário corrija o valor\.
	- Caso o valor informado nesse campo seja menor do que o valor informado no campo \(2\) deverá ser exibida mensagem de erro “Valor Original Compensado do Crédito não pode ser menor do que o valor informado no campo Valor Principal Devido Compensado\. Por gentileza corrigir o valor\.”\. O sistema não deverá permitir a continuação da compensação até que o usuário corrija o valor\.
	- Caso o valor informado nesse campo seja maior do que o valor informado no campo “Saldo” do Crédito selecionado deverá ser exibida mensagem de erro “Valor Original Compensado do Crédito não pode ser maior do que o Saldo do Crédito\. Por gentileza corrigir o valor\.”\. O sistema não deverá permitir a continuação da compensação até que o usuário corrija o valor\.
- __Valor Monetário Compensado \(6\): __o usuário deverá informar o Valor Monetário Compensado\. Esse campo deverá ser numérico de 17 posições, sendo 15 inteiras e 2 decimais\. Campo editável\.
- __Valor Principal Recolher \(7\):__ será exibido o Valor Principal a Recolher, ou seja, o Valor que o DARF será gerado\. Esse campo não deverá ser editável e o mesmo será resultado do campo \(1\) – \(2\)\. Os valores OFICIAIS de Juros e Multa – não se trata dos campos 3 e 4 informados nessa mesma tela – não deverão ser considerados nesse campo, somente após a confirmação da geração do DARF\.

Caso o usuário tenha enviado um Débito para a parte de Detalhes da Compensação de Créditos de Tributos Federais e já tenha informado os valores de compensação nos campos \(2\) e/ou \(5\), o usuário poderá excluir esse débito do crédito selecionado\. Nesse caso ao excluir o mesmo, esse débito irá voltar a aparecer na parte de Confrontos \(Débitos\) e todos os valores utilizados anteriormente para o Débito e para o Crédito previamente selecionado deverão ser desfeitos para os valores originais do mesmo – para tanto se deve levar em conta os valores informados nos campos \(2\) para Débitos e \(5\) para Créditos\.

Caso o valor informado nos campos \(2\), \(3\) e \(4\) não sejam iguais o valor informado nos campos \(5\) e \(6\), deverá ser exibida mensagem de erro “Valor Principal Devido Compensado, Multas e Juros não podem ser menores ou maiores do que o Valor Original Compensado do Crédito e Valor Monetário Compensado\. Por gentileza corrigir o valor\.”\. O sistema não deverá permitir a continuação da compensação até que o usuário corrija o valor\.

OS3267\-B

OS3916

# RN06

Após o preenchimento dos campos da compensação, o usuário irá confirmar a operação clicando no botão “Confirmar/Gerar DARF’s”\. Ao clicar nesse botão, os DARF’s irão considerar como Valor Total o valor informado no campo \(7\) e o campo STATUS tanto da X75\_DCTF quanto da X751\_DCTF\_COMPL irão mudar de “G” para “A”\.

Ao mudar o STATUS para “A” serão calculados os Juros e Multa DO DÉBITO de acordo com a parametrização de DARF/GPS da tabela PRT\_JUROS\_MULTA\. Os valores de Juros e Multa informados na tela de Compensação __NÃO DEVERÃO SER CONSIDERADOS NESSE CÁLCULO__\.

O cálculo deve ser realizado com base no Valor Principal da X75\_DCTF ou X751\_DCTF\_COMPL\.

No caso do DARF ser compensado totalmente, não haverá calculo de Juros e Multa\.

Caso o DARF seja compensado totalmente, o DARF será gerado na X75\_DCTF ou X751\_DCTF\_COMPL da seguinte forma:

- A Data de Pagamento será a Data de Apuração informada na X75\_DCTF ou X751\_DCTF\_COMPL\.
- A Data de Envio Bancária será a Data Apuração informada na X75\_DCTF ou X751\_DCTF\_COMPL\.
- No campo Autenticação Bancária será informada a palavra “COMPENSACAO”\.

OS3267\-B

# RN07

Na rotina de emissão dos DARF’s a mesma deverá contemplar os DARF’s nas seguintes condições:

- DARF’s da tabela X75\_DCTF cujo campo STATUS = “A” ou “P”
- DARF’s da tabela X751\_DCTF\_COMPL cujo campo STATUS = “A” ou “P” e campo IND\_DEB\_CRED = “D”

Salvaguardadas essas condições, os DARF’s devem ser emitidos com sucesso\.

OS3267\-B

# RN08

Os DARF’s emitidos que forem recuperados da tabela X751\_DCTF\_COMPL deverão seguir as mesmas regras das informações do DARF da X75\_DCTF\.

OS3267\-B

# RN09

Deverá ser criado na aba “Crédito” da tela de Manutenção dos DARF’s o campo “Saldo do Crédito”\. Esse campo irá recuperar as informações do campo VLR\_TOTAL da tabela X751\_DCTF\_COMPL\. 

OS3267\-B

# RN10

O cliente ao tentar excluir ou reabrir um DARF Original ou DARF Complementar que possua uma compensação associada ao mesmo deverá permitir a exclusão exibindo a seguinte mensagem:

“Os Tributos relacionados a este DARF serão desconsiderados da Situação=Gerado, se este é um DARF referente a uma parte da divisão em quotas dos Tributos todas as quotas serão excluídas, havendo a necessidade de re\-processar rotina \(Geração de DARF a partir da Retenção\)\. Caso o usuário confirme essa operação, todas as compensações realizadas para o DARF serão desfeitas, liberando assim os valores utilizados novamente como créditos”\.

OS3267\-B

# RN11

Caso o usuário compense um débito totalmente ou parcialmente o mesmo poderá reabrir o débito\. A reabertura do débito já pago implica na exclusão das informações da “Data de Pagamento” e “Autenticação Bancária”\.

Caso o usuário exclua as informações dos campos “Data de Pagamento” e “Autenticação Bancária”, o sistema deverá:

- O DARF deverá mudar o status de “Pago” para “Em Aberto” no campo “Status” da aba “DARF Original” ou “DARF Complementar” da tela de Manutenção de DARF – menu: Outras Obrigações >> DARF’s >> Manutenção\.
- A aba “Compensação” da tela de Manutenção de DARF – menu: Outras Obrigações >> DARF’s >> Manutenção deverá ficar desabilitada\.
- O campo “Valor Utilizado” da aba “Compensação” deverá ter o valor diminuído visto que não existe mais crédito sendo utilizado\.

O crédito utilizado para a compensação do DARF Original ou Complementar existente também deve ser devolvido\. Nesse caso podem ocorrer duas situações:

- Caso o crédito utilizado seja de um registro da tela de manutenção do Saldo Credor – menu: Outras Obrigações >> DARF’s >> Saldo Credor para Compensação dos Tributos Federais, o valor do DARF que foi reaberto deverá ser acrescido no campo “Valor Compensado”\. Nesse caso, automaticamente o campo “Saldo” também será atualizado\.
- Caso o crédito utilizado seja de um registro da tela de créditos da X751\_DCTF\_COMPL – menu: Outras Obrigações >> DARF’s >> Manutenção, o valor do DARF que foi reaberto deverá ser acrescido no campo “Valor do Crédito”\. Nesse caso, automaticamente o campo “Saldo do Crédito” também será atualizado e o campo “Status” será atualizado do status “Compensado” para “Em aberto” caso a compensação anterior tenha sido total\.

É importante salientar que os Valores de Juros e Multa que foram calculados nos DARF’s reabertos, são zerados pois não podem mais ser considerados, uma vez que o DARF foi reaberto\.

OS3267\-B

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


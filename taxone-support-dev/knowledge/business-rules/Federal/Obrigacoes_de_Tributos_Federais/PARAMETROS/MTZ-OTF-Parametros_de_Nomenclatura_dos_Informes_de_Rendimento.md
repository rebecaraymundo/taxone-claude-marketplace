# MTZ-OTF-Parametros_de_Nomenclatura_dos_Informes_de_Rendimento

- **Fonte:** MTZ-OTF-Parametros_de_Nomenclatura_dos_Informes_de_Rendimento.docx
- **Modificado:** 2020-08-31
- **Tamanho:** 33 KB

---

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a># Obrigações de Tributos Federais – Parâmetros de Nomenclatura dos Informes de Rendimento

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS4000

Obrigações de Tributos Federais – Parâmetros de Nomenclatura dos Informes de Rendimento

Essa OS tem por objetivo, permitir a geração dos informes de rendimento individualizados, ou seja, que para cada informe de rendimento seja gerado um arquivo PDF diferente\. Além disso, será permitido que o usuário parametrize a forma como o nome do informe será disponibilizado\. Para essa OS foram solicitados diversos itens nos documentos de visão, que por sua vez foram segregados em diversas OS’s\. Abaixo seguem essas divisões:

Os itens solicitados no documento de visão foram:

__Item__

__Descrição__

__Solução__

1

Criação de uma tabela auxiliar no cadastro de pessoas onde será informado para cada CPF ou CNPJ a suas respectivas classificações\. Exemplo:1 – corretor, 2\- prestador, 3 \- beneficiário\), lembrando que o CPF/CNPJ poderá ter mais de uma classificação\. Tratar e disponibilizar ao usuário a seleção das classificações em tempo de geração dos informes\.

O cliente poderá tratar pelo Código de Operação, conforme informações do Marcos Paula\.

__2__

__PDF Individual: Necessidade de que os informes sejam gerados em PDF individualmente  por CPF/CNPJ, e que o nome do arquivo seja parametrizável\.__

__Será tratado na OS\-4000\.__

3

Logotipo nos informes: Ter funcionalidade de inserir a imagem do logotipo de cada empresa nos informes de forma parametrizável

Será tratado na OS\-3997\.

4

Configuração do Envelope: Ter funcionalidade de definir a cor do fundo do envelope, de forma a não deixar transparecer nenhuma informação sigilosa e também possibilitar a configuração das dobras do envelope, pois dependendo a impressora, a dobra poderá sofrer ajustes\.

Será tratado na OS\-3996\.

5

Informação de Isenção: Alguns beneficiários possuem Isenção em parte da tributação do IRRF a ser apresentado no Informe e Dirf, para composição do valor a ser demonstrado, é preciso ter campos específicos nas retenções para que o tratamento seja feito\.

Tipos de Isenção: Aposentado maior de 65 anos, beneficiário associado a cooperativa de transporte \(Taxi\) e beneficiário portador de moléstia grave\. Este item aplica\-se somente ao Informe de Rendimentos de terceiros \(Pessoa Física\) e aos Registros da Dirf especificos para estas informações\.

Será tratado na OS\-3999\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

Deverá ser criada no módulo “Obrigações de Tributos Federais” uma nova tela chamada “Parâmetros de Nomenclatura de dos Informes de Rendimento”\.

O menu dessa tela ficará abaixo do menu Parâmetros DARF/GPS, ou seja, será o último sub\-menu do menu Parâmetros\.

__OS4000__

__RN02__

Essa tela permitirá a inclusão, consulta, alteração e exclusão de registros\.

__OS4000__

__RN03__

Deverá ser criado um relatório de conferência para essa tela\.

__OS4000__

__RN04__

Para incluir uma parametrização, o usuário deverá preencher/visualizar os seguintes campos:

- __Estabelecimento:__ nesse campo, o usuário deverá selecionar o estabelecimento para a parametrização\. Por default, será exibido o mesmo estabelecimento selecionado no Manager, porém se no Manager não existir estabelecimento selecionado, nesse caso, não será exibido nenhum estabelecimento por default\. Em relação ao estabelecimento será exibido o código e a descrição do mesmo, separados por – \(hífen\)\. Campo obrigatório de preenchimento\.
- __Nomenclatura do Arquivo:__ nesse campo, o usuário irá definir de que forma a nomenclatura \(nome\) do arquivo será definido\. Serão exibidas para o usuário, as seguintes opções:
	- CNPJ da Pessoa Física/Jurídica \+ CNPJ do Estabelecimento
	- CNPJ da Pessoa Física/Jurídica \+ CNPJ do Estabelecimento \+ Código DARF
	- CNPJ da Pessoa Física/Jurídica \+ CNPJ do Estabelecimento \+ Código DARF \+ Ano Calendário

Esse campo é obrigatório de preenchimento\.

- __Tipos de Informe:__ nesse campo, o usuário deve definir quais informes de rendimento serão parametrizados para a nomenclatura do arquivo definida\. O usuário deve selecionar pelo menos 1 \(um\) tipo de informe\. As opções a serem definidas são:
	- Empregados
	- Outros
	- Clientes
	- Financeiros – IN 698/06
	- Juros Remuneratórios do Capital Próprio
	- PIS/COFINS/CSLL
	- PIS/COFINS/CSLL – IN 594/05
- __Diretório:__ nesse campo, o usuário deverá selecionar um diretório \(File Server\) local ou na rede para gravar os informes de rendimento\. 
- __Replicar para o\(s\) Estabelecimento\(s\):__ nesse campo o usuário irá selecionar qual ou quais estabelecimentos ele deseja replicar a parametrização feita\. Só serão exibidos os estabelecimentos que o usuário possui direito de acesso na empresa selecionada no Manager\.
- __Botões “Selecionar Todos/Desmarcar Todos”: __nesses botões, o usuário poderá selecionar todos ou desmarcar todas as empresas ou estabelecimentos\.

__OS4000__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


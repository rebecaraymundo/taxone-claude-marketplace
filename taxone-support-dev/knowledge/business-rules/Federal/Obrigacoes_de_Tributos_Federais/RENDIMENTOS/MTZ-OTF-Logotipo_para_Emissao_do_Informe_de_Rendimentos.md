# MTZ-OTF-Logotipo_para_Emissao_do_Informe_de_Rendimentos

- **Fonte:** MTZ-OTF-Logotipo_para_Emissao_do_Informe_de_Rendimentos.docx
- **Modificado:** 2020-08-31
- **Tamanho:** 35 KB

---

# Módulo: Obrigações de Tributos Federais

# Logotipo para Emissão do Informe de Rendimentos

# *Menu: Parâmetros >> Logotipo para Emissão do Informe de Rendimentos*

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3996

Obrigações de Tributos Federais – Inclusão de Logotipo nos Informes de Rendimento

Essa OS tem por objetivo, permitir a inclusão do logotipo da empresa nos Informes de Rendimento\. Conforme documento de visão da OS3996, foram solicitados os seguintes itens, porém conforme alinhamento com o Sr\. Marcos Paula em 08/10/2013, só será desenvolvido na OS\-3997 a inclusão do logotipo nos informes de rendimento\.

Os itens solicitados no documento de visão foram:

__Item__

__Descrição__

__Solução__

1

Criação de uma tabela auxiliar no cadastro de pessoas onde será informado para cada CPF ou CNPJ a suas respectivas classificações\. Exemplo:1 – corretor, 2\- prestador, 3 \- beneficiário\), lembrando que o CPF/CNPJ poderá ter mais de uma classificação\. Tratar e disponibilizar ao usuário a seleção das classificações em tempo de geração dos informes\.

O cliente poderá tratar pelo Código de Operação, conforme informações do Marcos Paula\.

2

PDF Individual: Necessidade de que os informes sejam gerados em PDF individualmente  por CPF/CNPJ, e que o nome do arquivo seja parametrizável\.

Será tratado na OS\-4000\.

__3__

__Logotipo nos informes: Ter funcionalidade de inserir a imagem do logotipo de cada empresa nos informes de forma parametrizável__

__Será tratado na OS\-3997\.__

4

Configuração do Envelope: Ter funcionalidade de definir a cor do fundo do envelope, de forma a não deixar transparecer nenhuma informação sigilosa e também possibilitar a configuração das dobras do envelope, pois dependendo a impressora, a dobra poderá sofrer ajustes\.

Será tratado na OS\-3996\.

5

Informação de Isenção: Alguns beneficiários possuem Isenção em parte da tributação do IRRF a ser apresentado no Informe e Dirf, para composição do valor a ser demonstrado, é preciso ter campos específicos nas retenções para que o tratamento seja feito\.

Tipos de Isenção: Aposentado maior de 65 anos, beneficiário associado a cooperativa de transporte \(Taxi\) e beneficiário portador de moléstia grave\. Este item aplica\-se somente ao Informe de Rendimentos de terceiros \(Pessoa Física\) e aos Registros da Dirf especificos para estas informações\.

Será tratado na OS\-3999\.

Vale salientar que o controle de margem solicitado no item 4, já foi solicitado por outros clientes \(vide OS\-3956\) e há dificuldade técnica para implementação dessa demanda\. Logo esse item não será desenvolvido nessa OS\-3996 \(ver e\-mail sobre a margem anexo junto à demanda\)\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

Deverá ser criado no menu Parâmetros >> Logotipo para Emissão do Informe de Rendimentos a tela para inclusão do logotipo no Informe de Rendimentos\. Esse menu deverá ser disponibilizado após o menu “Parâmetros DARF/GPS”\.

__OS3997__

__RN02__

Essa tela deverá permitir a inclusão, consulta, alteração e exclusão do cadastro do logotipo\.

__OS3997__

__RN03__

Para incluir o logotipo, o cliente deverá preencher os seguintes campos:

- __Empresa:__ nesse campo, serão exibidas as empresas licenciadas do produto Mastersaf DW e que o usuário possua direito de acesso\. Só será permitida a seleção de uma única empresa\. Será exibido o Código e a Descrição da Empresa separados por um “\-“ hífen\. Campo obrigatório de preenchimento\.
- __Estabelecimento:__ nesse campo, serão exibidos os estabelecimentos do produto Mastersaf DW que o usuário possua direito de acesso\. Só será permitida a seleção de um único estabelecimento\. Será exibido o Código e a Descrição do Estabelecimento separados por um “\-“ hífen\. Campo obrigatório de preenchimento\.
- __Logotipo:__ nesse campo, o usuário deverá procurar o arquivo com o logotipo para a empresa e estabelecimento selecionados\. Vale salientar, que o logotipo uma vez selecionado, a imagem do mesmo será exibida\. O logotipo deverá ser recuperado de alguma pasta local ou da rede e deverá em um dos seguintes formatos:
	- BMP
	- JPG
	- JPEG
	- GIF
	- PNG

O campo será obrigatório de preenchimento\.

- __Replicar para o\(s\) Estabelecimento\(s\):__ nesse campo, o usuário poderá replicar o logotipo para os outros estabelecimentos que ele possua permissão de acesso\. O usuário poderá selecionar todos os estabelecimentos através do botão “Selecionar Todos” e desmarcar todos através do botão “Desmarcar Todos”\. Campo não obrigatório de preenchimento\.

__OS3997__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


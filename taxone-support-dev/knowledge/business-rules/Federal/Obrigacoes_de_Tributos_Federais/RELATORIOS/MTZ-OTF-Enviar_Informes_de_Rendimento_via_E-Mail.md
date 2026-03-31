# MTZ-OTF-Enviar_Informes_de_Rendimento_via_E-Mail

- **Fonte:** MTZ-OTF-Enviar_Informes_de_Rendimento_via_E-Mail.docx
- **Modificado:** 2022-10-26
- **Tamanho:** 36 KB

---

# Módulo – Obrigações de Tributos Federais

# Enviar Informes de Rendimento via e\-mail

__Localização das telas:__ 

Módulo: Federal >> Obrigações de Tributos Federais

Menus:

Rendimentos >> Rendimentos Empregados >> Emissão Declaração de Rendimentos >> Por Código/ Por Nome/ Por Centro de Custo

Rendimentos >> Rendimentos Outros >> Emissão Declaração de Rendimentos >> Pessoa Jurídica >> Por CNPJ/ Por Nome

Rendimentos >> Rendimentos Outros >> Emissão Declaração de Rendimentos >> Pessoa Física >> Por CPF/ Por Nome

Rendimentos >> Rendimentos de Clientes >> Emissão Declaração de Rendimentos

Rendimentos >> Relatórios >> Comprovante Anual de Retenção PIS/COFINS/CSLL

Rendimentos >> Relatórios >> Comprovante Mensal de Retenção PIS/COFINS IN 594/05

__Título da tela: __Enviar informe de Rendimentos por E\-Mail

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

CH3324\_2012

OTF \- DIRF \- Criação de campo para envio de Informe de Rendimentos por e\-mail

Este chamado de alteração de regra de negócio tem por objetivo permitir que o usuário informe a “Porta” para envio dos Informes de Rendimento através de Winsock\. A funcionalidade prevista hoje no produto está com erros e a criação desse campo no processo de envio irá resolver essa situação\.

CH2173\_2012

OTF – Controle dos Informes de Rendimentos enviados e não enviados

O objetivo deste documento de requisito é criar uma regra de negócio para que ao abrir a tela do envio do informe de rendimentos por e\-mail, o mesmo não aparece como “enviado” até ser efetivamente enviado\.

Ocorre que conforme histórico do chamado 2173\_2013 foi questionado que esse problema passou a ocorrer após a aplicação do pacote do CH3324\_2012 e que isso deveria ser classificado como erro\. O QA informou que só consegue testar se a regra estiver definida, porém a visão do Requisito é que esse chamado deve ser classificado como erro\. Vale salientar também que o CH3324\_2012 não tinha por objetivo mexer no controle dos informes enviados ou não\.

OS4720

OTF \- DIRF \- Criação de parâmetros para envio de Informe de Rendimentos por e\-mail

Este documento tem como objetivo incluir dois novos parâmetros para identificação de autenticação de usuário e senha do servidor de e\-mail e definição de porta\.

MFS95638

OTF \- Criação de parâmetros para incluir Razão Social no Assunto do e\-mail

Este documento tem como objetivo incluir o parâmetro para incluir o Campo de Assunto do e\-mail a Razão Social do Beneficiário: Comprovante de Rendimentos – Razão Social\.

## REGRAS DE NEGÓCIO

#### Cód\.

####                                                                                                  Descrição

### DR

__RN01__

Na tela de Envio de Informe de Rendimentos por E\-mail deverá ser criado o campo “Porta”\. Esse campo ficará localizado entre os campos “SMTP” e “De”\.

Para que esse campo seja acessível a opção selecionada deverá ser “Envio usando o Winsock”\. Caso a opção selecionada seja “Envio usando Outlook”, esse campo não poderá ser visualizado\.

__CH3324\_2012__

__RN02__

O campo “Porta” deverá ser numérico de 4 \(quatro\) posições e obrigatório de preenchimento\. Caso o campo não seja preenchido e tente se enviar o Informe, deverá ser exibida mensagem de erro informando do fato\.

__CH3324\_2012__

__RN03__

A rotina de envio dos Informes de Rendimento por e\-mail deverá considerar a porta de envio informada no campo “Porta” para que a transmissão da informação ocorra com sucesso\.

Além da Porta as informações do servidor de SMTP, Usuário e Senha continuarão a ser consideradas\.

__CH3324\_2012__

__RN04__

Ao abrir a funcionalidade do envio do Informe de Rendimentos via e\-mail – Empregados, Outros, Clientes e PIS/COFINS – caso o cliente ainda não tenha enviado o informe de rendimentos do beneficiário, o campo “Status” deverá estar vazio – caso a opção selecionada seja “Exibir somente não enviadas”\.

Ao enviar o informe do beneficiário, o campo “Status” deverá ser alterado para a data e hora do envio do informe de rendimentos, caso a opção escolhida seja “Exibir todos os informes emitidos”\.

__CH2173\_2012__

__RN05__

__Parâmetro “SMTP Server requires userid/password”__

Tipo: Texto

Obrig: Não

Ed: Sim

Formato: Check Box

Default: De acordo com a última parametrização do usuário\.

__Tratamento:__

- Quando o parâmetro estiver marcado deve exigir usuário e senha se o envio for utilizado como Winsock e o servidor de e\-mail utilizar de autenticação, caso não seja preenchido emitir a mensagem na tela: “Favor informar o email de onde será enviado”;
- Quando o parâmetro estiver marcado e for informado usuário e senha corretamente manter tratamento atual;
- Quando o parâmetro estiver desmarcado e for informado usuário e senha o mesmo será desconsiderado;
- Quando o parâmetro estiver desmarcado e o servidor utilizar de autenticação será ignorado a validação trazendo uma mensagem de “timed out” para mostrar que operação não completou;
- Quando o parâmetro estiver desmarcado e o servidor não utilizar de autenticação o processo do envio será o mesmo por autenticação\.

Observação: O Mastersaf DW tem essa rotina homologada para informar dados da autenticação do servidor de e\-mail, a solicitação de melhoria para não validar a autenticação foi feita pela BASF através do chamado 28957/2014 e somente esse cliente possui esse cenário\.

__OS4720__

__RN06__

__Parâmetro “SMTP Server Encryption”__

Tipo: Texto

Obrig: Sim

Ed: Sim

Formato: Radio Button Group

Default: De acordo com a última parametrização do usuário \(para nunca parametrizado levará “None”\)\.

Essa opção será de responsabilidade do usuário para verificação de habilitação da porta do servidor de e\-mail\.

Observação: O Mastersaf DW tem essa rotina homologada para informar dados da autenticação do servidor de e\-mail, a solicitação de melhoria para não validar a autenticação foi feita pela BASF através do chamado 28957/2014 e somente esse cliente possui esse cenário\.

__OS4720__

__RN07__

Na tela de Envio de Informe de Rendimentos por E\-mail deverá ser criado o campo “__*Incluir Beneficiário ao Assunto do e\-mail*__”\. Esse campo ficará localizado abaixo dos campos “Exibir somente não Enviados”, “Exibir todos os informes emitidos” e “Declarações alteradas \- Reenviar”\.

Formato: Check Box

Default: De acordo com a última parametrização do usuário\.

Caso esse parâmetro esteja marcado, o sistema deverá incluir no Campo “Assunto” a informação da Razão Social do beneficiário, concatenando da seguinte forma:

__Comprovante de Rendimentos – *Razão Social*__

__*Campo: RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR*__

Caso o parâmetro esteja desmarcado, o sistema deverá seguir conforme regras atuais, informando no Campo Assunto somente:

__Comprovante de Rendimentos__

__MFS95638__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


# MTZ-OTF-Emissao_de_DARFs

- **Fonte:** MTZ-OTF-Emissao_de_DARFs.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 49 KB

---

# Obrigações de Tributos Federais \- Emissão de DARF's 

##### DOCUMENTO DE REQUISITO 

###### DR

###### Nome

__Descrição__

CH179\_2013

Obrigações de Tributos Federais \- Emissão de DARF's

O objetivo deste documento de requisito é permitir que no campo 11 – Autenticação Bancária do DARF ao ser emitido, seja impressa a informação que estiver contida no campo Autenticação Bancária da tela de Manutenção de DARF\.

CH7452/2013

Obrigações de Tributos Federais \- Emissão de DARF's

Conforme Chamado nº 7452/2013, o cliente solicitou a inclusão de um filtro na tela abaixo:

Tela “Emissão de Tributos – Por Empresa”\.

A inclusão de um fitro, solucionaria a questão do cliente em poupar o tempo gasto em selecionar os código DARF que hoje é relizado pela barra de rolagem\.

Um botão “Pesquisar” faria o processo do filtro da tela acima\.

CH73194

Alteração da sigla 'CGC' para 'CNPJ' na emissão de DARF

Alterar as descrições “CGC”  e “Secretaria da Receita Federal” para adequação ao novo layout\.

OS2796

Obrigações de Tributos Federais \- Criar Parâmetro para Gerar DARF's Pagos e Não Pagos

- Criar parâmetro “Gerar DARF’s” na tela Emissão de DARF’s \(módulo: Obrigações de Tributos Federais – menu Outras Obrigações >> DARF’s >> Emissão\)\.
- Incluir Data de Pagamento e Código de Autenticação Bancária no DARF impresso\.

CH79473

Emissão do DARF com o CNPJ da Matriz

Criar opção na tela de emissão do DARF para permitir a emissão do DARF com o CNPJ da matriz\.

#### Cód\.

### Descrição

### DR

# RN01

O usuário ao clicar no menu: Outras Obrigações >> DARF’s >> Emissão e emitir o DARF, será exibido no campo 11 – Autenticação Bancária do DARF emitido, a informação que estiver contida no campo 23 – AUTENT\_BANCARIA da tabela X75\_DCTF \(Manutenção do DARF\) ou X751\_DCTF\_COMPL \(Manutenção do DARF – nesse caso o DARF Complementar\)\.

CH179\_2013

# RN02

Criar um botão “Pesquisar” para fazer o filtro dos códigos DARF na tela de “Emissão de Tributos – Por Empresa”, no campo “Código de Retenção”\.

OS4155

__RN03__

O campo *03\. NÚMERO do CPF ou CGC *deverá ser trocado para *03\. NÚMERO do CPF ou *__*CNPJ*__*, *apartir de 10/05/2007, de acordo com a *Instrução Normativa RFB nº 736\.*

CH73194

__RN04__

O campo *01\. *abaixo da palavra __ATENÇÃO__,  deverá ser alterada a descrição *“Secretaria da Receita Federal \(RFB\)”* para *“Secretaria da Receita Federal *__*do Brasil*__* \(RFB\)”, *apartir de 10/05/2007, de acordo com a *Instrução Normativa RFB nº 736\.*

CH73194

__RN05__

Deverá ser criado o parâmetro “Gerar DARF’s” na tela Emissão de DARF’s\. Essa tela está disponível no menu Outras Obrigações >> DARF’s >> Emissão do módulo Obrigações de Tributos Federais\.

OS2796

__RN06__

O parâmetro exibirá os valores em uma lista restrita\. Os valores do parâmetro são:

- Em aberto \(essa opção deve ser a default\)
- Pagos
- Todos

OS2796

__RN07__

Caso o parâmetro esteja com a opção “Em aberto” selecionada, o sistema deverá adotar o seguinte comportamento:

- Recuperar e exibir somente os DARF’s não pagos na tabela X75\_DCTF\. Para isso o campo STATUS <> “P”\.

Caso a DARF esteja dividido em quotas, a mesma só será considerada não paga, quando pelo menos uma das referências da mesma na tabela X75\_DCTF esteja com o campo STATUS seja diferente de “P”\.

OS2796

__RN08__

Caso o parâmetro esteja com a opção “Pagos” selecionada, o sistema deverá adotar o seguinte comportamento:

- Recuperar e exibir somente os DARF’s pagos na tabela X75\_DCTF\. Para isso o campo STATUS = “P”\.

__ __

Caso a DARF esteja dividido em quotas, a mesma só será considerada paga, caso todas as referências da mesma na tabela X75\_DCTF estejam com o campo STATUS = “P”\.

OS2796

__RN09__

Caso o parâmetro esteja com a opção “Todos” selecionada, o sistema deverá adotar o seguinte comportamento:

- Recuperar e exibir todos os DARF’s – pagos e em aberto \(não pagos\)\. Para identificá\-los utilizar os mesmos critérios das regras RN02 e RN03\.

OS2796

__RN10__

Informar na coluna “AUTENTICAÇÃO BANCÁRIA”, a Data de Pagamento do DARF\. Recuperar essa informação do campo DATA\_PAGTO da tabela X75\_DCTF\.

OS2796

__RN11__

Informar na coluna “AUTENTICAÇÃO BANCÁRIA”, o código de autenticação bancária\. Recuperar essa informação do campo AUTENT\_BANCARIA da coluna X75\_DCTF\.

OS2796

__RN12__

Deve ser criado um campo do tipo checkbox com a descrição “Emite DARF com CNPJ Matriz” na tela de emissão do DARF\.

Esse campo deverá ser criado acima do quadro “Receitas” e deve possuir default desmarcado\.

CH79473

__RN13__

Quando na emissão do DARF a opção “Emite DARF com CNPJ Matriz” estiver marcada, a informação a ser apresentada nos quadros “CNPJ” e “Nome/Telefone” do DARF deve ser recuperada do estabelecimento Matriz daquela empresa, e não mais do estabelecimento a que aquele DARF pertence\.

Quando a opção “Emite DARF com CNPJ Matriz” estiver desmarcada a regra atual de emissão do DARF não será alterada\.

CH79473

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


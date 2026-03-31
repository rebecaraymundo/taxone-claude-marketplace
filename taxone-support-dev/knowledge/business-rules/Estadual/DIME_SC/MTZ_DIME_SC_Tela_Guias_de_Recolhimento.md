# MTZ_DIME_SC_Tela_Guias_de_Recolhimento

- **Fonte:** MTZ_DIME_SC_Tela_Guias_de_Recolhimento.docx
- **Modificado:** 2024-04-01
- **Tamanho:** 75 KB

---

THOMSON REUTERS

Guias de Recolhimento

DIME\-SC

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-16778

Julyana Perrucini

Redefinir a regra de preenchimento do campo Classe de Vencimento\.

MFS\-76214

Rogério Ohashi

Criação do campo “Nª Discriminação”, para permitir ao usuário criar mais de uma Guia Recolhimento com as mesmas informações de código de receita e classe de vencimento para o mesmo dia\.

 

MFS\-81287

Andréa Rocha

Inclusão do campo IND\_DIG\_CALC, que vai indicar se um registro foi inserido pela tela de manutenção ou se foi inserido pela geração dos registros\.

MFS91937

Aline Melo

Inclusão da opção 4\-Valores Devidos ou Saldo Credor de Fundos

Sumário

[1\.	Regras dos Campos	3](#_Toc507774109)

[2\.	Sugestão de Layout	8](#_Toc507774110)

# <a id="_Toc350763252"></a><a id="_Toc507774109"></a>Regras dos Campos 

__Localização da tela:__ Estadual\\ DIME\-SC\\ Obrigações\\ Guias de Recolhimento

__Título da tela: __Guias de Recolhimento

__Regra Geral Botões:__

__NOVO – __Permite inserir novo registro\.

__ABRE – __Permite abrir seleção de registros inseridos\.

__EXCLUI – __Permite excluir registro inserido\.

__CONFIRMA – __Permite salvar registro\.

__RELATÓRIO – __Permite emitir relatório listando todos os registros existentes na base de dados ou de acordo com a Empresa e Estabelecimento selecionados na tela de login \(mostrar apenas os campos obrigatórios como critério de busca\)\.

__FECHA – __Permite sair da tela\.

__\[ALTERADA – MFS\-16778\]__

__Considerações:__

Nessa tela pode existir a combinação do mesmo código de receita para várias classes de vencimento podendo repetir ou não a sua data de vencimento\. 

*Exemplo prático:*

Guia Recolhimento 1

Competência: 01/2018

Origem: 3\-Débitos Específicos

Código Receita: 3000

Data Vencimento: 10/02/2018

Valor: 1000,00

Classe de Vencimento: 10243

Guia Recolhimento 2

Competência: 01/2018

Origem: 3\-Débitos Específicos

Código Receita: 3000

Data Vencimento: 10/02/2018

Valor: 500,00

Classe de Vencimento: 10405

A tabela EST\_SC\_GUIA\_RECOL que corresponde a essa tela de “Guias de Recolhimento” do módulo da DIME\-SC possuía como campos chave: Código da Empresa, Código do Estabelecimento, Data Competência, Substitutiva \(indicador\), Data Vencimento e o Código Receita\.

Através da __MFS\-16778__ alteramos a estrutura da tabela incluindo também como chave o campo Classe de Vencimento, e além disso, foi preciso incluir um tratamento para que o campo seja preenchido com espaço em branco ao gravar o registro na tabela caso não haja informação, pois, esse campo não é obrigatório e por ter sido desenvolvido dessa forma vamos mantê\-lo\. 

\[__ALTERADA – MFS\-76214__\] Tratamento p/ os clientes que possuem a necessidade de emitir Guias de Recolhimento com as mesmas informações de código de receita e classe de vencimento para o mesmo dia\.

Através da MFS\-76214 será criado o campo “NUM\_DISCRIMINACAO” \(Nª Discriminação\)  na tabela EST\_SC\_GUIA\_RECOL, como __Campo Chave__, preenchido internamente pelo sistema, para permitir ao usuário criar tantas Guias forem necessárias com um número sequencial, com as mesmas informações de código de receita e classe de vencimento para o mesmo dia\.

__Nª Discriminação:__ Na inclusão de novas Guias de Recolhimento, este campo deverá ser preenchido com sequencial gerado de forma automática ‘1’ \(\+1\), a partir do maior número já existente, para a Empresa, Estabelecimento, Código de Receita, Classe de Vencimento e Data Vencimento/Pagamento da Guia de Recolhimento para o mesmo dia\.

__                         Obs\.:__ Campo não editável, e a primeira Guia de Recolhimento gravar “1”\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Estabelecimento

Texto

S

N

Formato: 

Combo Box

Default:

\(ver tratamento\)

Permitir mostrar estabelecimento a ser mantido\.

__Tratamento:__

- O campo será bloqueado e caso o usuário entre com um estabelecimento no Login, o mesmo será apresentado e não haverá opção de modificar;
- O campo será apresentado de forma desbloqueada e caso o usuário não entre com um estabelecimento no Login, deverá apresentar a lista dos estabelecimentos de UF igual a SC;
- Se o campo não for preenchido, emitir a mensagem na tela: *“Estabelecimento deve ser preenchido”*\.

MFS\-XXXX

Data Competência

Data

S

N

Formato:

Text Input DD/MM/AAAA

Default:

Habilitado

Nesse campo o usuário deverá informar a data de competência da guia de recolhimento\.

__Tratamento:__

- Ao salvar o registro esse campo não poderá ser alterado;
- Se o campo não for preenchido, emitir a mensagem na tela: *“Data de Competência deve ser preenchida”*\.

MFS\-XXXX

Nª Discriminação

Numérico

S

N

Formato:

1

Default: 

Desabilitado

Campo Obrigatório

Na inclusão de novas Guias de Recolhimento, este campo deverá ser preenchido com sequencial gerado de forma automática, a partir do maior número já existente ‘1’ \(\+1\), para a Empresa, Estabelecimento, Código de Receita, Classe de Vencimento e Data Vencimento/Pagamento da Guia de Recolhimento para o mesmo dia\.

__Obs\.:__ Campo não editável, e a primeira Guia de Recolhimento gravar “1”\.

Formato do Campo: NUMBER\(12\)\.

MFS76214

Substitutiva

Texto

N

N

Formato:

Check Box

Default:

Habilitado

Nesse campo o usuário deverá informar se a guia de recolhimento se trata de uma guia que será substituída\.

__Tratamento:__

- Ao salvar o registro esse campo não poderá ser alterado\.

MFS\-XXXX

Origem do Recolhimento

Texto

N

S

Formato:

Combo Box

Default:

Habilitado

Nesse campo o usuário deverá informar a origem do recolhimento, sendo:

1 \- ICMS \(para pagamento relativo ao ICMS a recolher calculado no Quadro 09\);

2 \- Substituição Tributária \(para imposto relativo a substituição tributária apurada no Quadro 11\); 

3 \- Débitos Específicos \(para débitos informados no Quadro 10\); e

4 – Valores Devidos ou Saldo Credor  \(para valores de Fundos apurados no Quadro 16\)\.

__Conteúdo:__

1\-ICMS;  
2\-Substituição Tributária;  
3\-Débitos Específicos;

4\-Valores de Fundos\.

MFS\-XXXX

MFS\-91937

Código Receita

Texto

S

N

Formato:

Text Input/ Pasta Seleção \(Códigos de Receitas Estaduais do Parâmetros da DIME\-SC\)

Default:

Habilitado

Nesse campo o usuário deverá informar o código de receita para a guia de recolhimento\.

__Tratamento:__

- Ao salvar o registro esse campo não poderá ser alterado;
- Caso o registro seja inserido e não esteja cadastrado, será emitida a mensagem no campo: *“Código da Receita Estadual Não Encontrado”*;
- Se o campo não for preenchido, emitir a mensagem na tela: *“Código da Receita deve ser preenchido”*\.

MFS\-XXXX

Data Vencimento/ Pagamento

Data

S

N

Formato:

Text Input DD/MM/AAAA

Default:

Habilitado

Nesse campo o usuário deverá informar a data de competência da guia de recolhimento\.

__Tratamento:__

- Ao salvar o registro esse campo não poderá ser alterado;
- Se o campo não for preenchido, emitir a mensagem na tela: *“Data de Vencimento deve ser preenchida”*\.

MFS\-XXXX

Valor Receita

Numérico

N

S

Formato:

0,00

Default:

Habilitado

Nesse campo o usuário deverá informar o valor da receita para a guia de recolhimento\.

MFS\-XXXX

Classe de Vencimento

Texto

N

S

Formato:

Text Input

Default:

Habilitado

Nesse campo o usuário deverá informar o código da classe de vencimento conforme Portaria do Secretário de Estado da Fazenda referente ao conteúdo a ser gerado no campo 07 do Registro Tipo 33 da DIME\.

__\[ALTERADA – MFS\-16778\]__

__Tratamento:__

- Gravar com espaço em branco quando não for inserida nenhuma informação devido ser campo chave na tabela\.

MFS\-16778

Número do Acordo

Numérico

N

S

Formato:

Text Input

Default:

Habilitado

Nesse campo o usuário deverá informar o número do registro do acordo de Tratamento Tributário Diferenciado – TTD ou Regime Especial\.

MFS\-XXXX

IND\_DIG\_CALC

Texto

S

N

\-\-\-\-\-\-

Este campo não será mostrado em tela, servirá somente para controle se o registro foi inserido manualmente, ou gerado, ou gerado e atualizado\.

Valores Válidos:

1 \- Digitado;

2 \- Gerado;

3 \- Gerado / atualizado por digitação\.

Obs\.: A tela irá gravar “1” quando o registro for incluído ou incluído e depois alterado pela tela\.  

A opção “2” só é gravado pela rotina de geração dos registros\.

A tela irá gravar “3” quando registro for gerado \(opção=2\) e depois alterado pela tela\.    

MFS\-81287

# <a id="_Toc507774110"></a>Sugestão de Layout


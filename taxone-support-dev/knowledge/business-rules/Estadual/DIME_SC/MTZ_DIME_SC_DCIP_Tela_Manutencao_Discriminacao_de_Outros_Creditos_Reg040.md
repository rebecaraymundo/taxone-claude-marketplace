# MTZ_DIME_SC_DCIP_Tela_Manutencao_Discriminacao_de_Outros_Creditos_Reg040

- **Fonte:** MTZ_DIME_SC_DCIP_Tela_Manutencao_Discriminacao_de_Outros_Creditos_Reg040.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 67 KB

---

THOMSON REUTERS

Manutenção Discriminação de Outros Créditos \(Reg 040\)

DIME\-SC DCIP Registros “040”

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS1229

Julyana Perrucini

Este documento tem como objetivo alterar o tipo do campo “Número de S@T” para chave primária\.

Sumário

[1\.	Regras dos Campos	3](#_Toc428894838)

# <a id="_Toc350763252"></a><a id="_Toc428894838"></a>Regras dos Campos 

__Localização da tela:__ Estadual\\ DIME\-SC\\ Obrigações\\ Manutenção\\ Discriminação de Outros Créditos

__Título da tela: __Manutenção Discriminação de Outros Créditos \(Reg 040\)

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

Text Area

Default:

Habilitado

Permite o usuário informar o estabelecimento que será entregue na DCIP\.

__Tratamento:__

- Se o usuário entrar com estabelecimento no login, demonstrar o mesmo e não permitir a modificação;
- Se o usuário não entrar com estabelecimento no login, demonstrar o campo em branco e permitir a seleção dos estabelecimentos de UF = SC;
- Caso o campo não esteja selecionado, emitir a mensagem na tela: “Estabelecimento deve ser informado\.”\. 

__Características do campo:__

Campo Chave

Tamanho 6

MFS1229

Período Referência

Data

S

N

Formato: 

MM/AAAA

Default:

Habilitado

Permite o usuário informar a referência para utilização do crédito que será entregue na DCIP\.

__Tratamento:__

- Caso o campo não esteja preenchido, emitir a mensagem na tela: “Data da Apuração deve ser informada\.”\.
- Caso o campo não esteja preenchido no formato padrão, emitir a mensagem na tela: “Valor Inválido\.”\. 

__Características do campo:__

Campo Chave

Tamanho 8

MFS1229

Tipo de Crédito

Numérico

S

N

Formato: 

Text Area

Default:

Habilitado

Permite o usuário informar o tipo de crédito que será entregue na DCIP\.

__Tratamento:__

- Caso o campo não esteja preenchido, emitir a mensagem na tela: “Tipo de Crédito deve ser informado\.”\.

__Características do campo:__

Campo Chave

Tamanho 3

MFS1229

Valor do Crédito

Numérico

N

S

Formato: 

Text Area

Default:

Habilitado

Permite o usuário informar o valor do crédito utilizado que será entregue na DCIP\.

__Características do campo:__

Tamanho 15V2

MFS1229

Número do S@T

Numérico

N

N

Formato: 

Text Area

Default:

Habilitado

Permite o usuário informar o número s@t disponibilizado pela SEFAZ para utilização do crédito que será entregue na DCIP\.

__Tratamento:__

- Após salvar o campo deve ficar desabilitado para alteração;
- Caso o campo não esteja preenchido, gravar zero \(0\) na tabela\.

__\[ALTERADA – MFS1229\]__

__Características do campo:__

Campo Chave

Tamanho 15

MFS1229

Lançamento Complementar

Texto

S

S

Formato: 

Text Area

Default:

Habilitado

Permite o usuário informar uma breve descrição do motivo da utilização do crédito que será entregue na DCIP\.

__Tratamento:__

- Caso o campo não esteja preenchido, emitir a mensagem na tela: “Tentativa de inserir informação\(ões\) nula\(s\)\!”\.

__Características do campo:__

Tamanho 150

MFS1229


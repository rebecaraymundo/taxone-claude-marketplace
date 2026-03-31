# MTZ-DW-Manutencao_SAFX701

- **Fonte:** MTZ-DW-Manutencao_SAFX701.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 67 KB

---

THOMSON REUTERS

Informações de Voo – Ato Cotepe ICMS 70/05

Mastersaf DW

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

CH17082\_2015

Julyana Perrucini

Este documento tem como objetivo alterar a verificação das informações de voo incluindo o modelo de documento 15 para o Ato Cotepe\.

Sumário

[1\.	Regras dos Campos	3](#_Toc443499207)

# <a id="_Toc350763252"></a><a id="_Toc443499207"></a>Regras dos Campos 

__Localização da tela:__ Básicos\\ Mastersaf DW\\ Manutenção\\ Documento Fiscal\\ Novo Documento Fiscal\\ Informações de Voo – Ato Cotepe ICMS 70/05

__Título da tela: __Informações de Voo – Ato Cotepe ICMS 70/05

__\[ALTERADA – CH17082\_2015\]__

__Regra Geral:__

- Essa tela será habilitada quando os modelos de documentos fiscais \(Código Modelo NF\) da SAFX07 forem iguais 15, 29 e 30\.
- As mensagens de erro são as mesmas utilizadas na importação da SAX701, verificar documento MTZ\_JOB\_SERVIDOR\_Importacao\_Online\_Batch\_SAFX701\.docx, em \\MsafDW\\documentacao funcional\\Documento Matriz\\Basicos\\Job Servidor\.

__ABA MANIFESTO/BILHETE__

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Voo

Texto

N

S

Formato:

Text Input

Default:

Habilitado

Neste campo o usuário poderá informar o Número do Voo\.

__Tratamento:__

Esse campo será habilitado para os modelos de documento: 15 29 e 30\.

CH17082\_2015

Conexão

Texto

N

S

Formato:

Text Input

Default:

Habilitado

Neste campo o usuário poderá informar a Conexão do Voo\.

__Tratamento:__

Esse campo será habilitado para os modelos de documento: 30\.

CH17082\_2015

Qtd\. Passageiros Voo

Texto

N

S

Formato:

Text Input

Default:

Habilitado

Neste campo o usuário poderá informar a quantidade de passageiros no voo\.

__Tratamento:__

Esse campo será habilitado para os modelos de documento: 15 e 29\.

CH17082\_2015

UF Emitente DocFis

Texto

N

S

Formato:

Text Input

Default:

Habilitado

Neste campo o usuário poderá informar a UF emitente do Documento Fiscal\.

__Conteúdo:__

UF \(cod\_estado\) da tabela Estado\.

__Tratamento:__

Esse campo será habilitado para os modelos de documento: 15 e 29\.

CH17082\_2015

CPF

Texto

N

S

Formato:

Text Input

Default:

Habilitado

Neste campo o usuário poderá informar o CPF do passageiro referente a este bilhete\.

__Tratamento:__

Esse campo será habilitado para os modelos de documento: 30\.

CH17082\_2015

Num\. Poltrona

Texto

N

S

Formato:

Text Input

Default:

Habilitado

Neste campo o usuário poderá informar o número da poltrona deste passageiro\.

__Tratamento:__

Esse campo será habilitado para os modelos de documento: 30\.

CH17082\_2015

Classe da Passagem

Texto

N

S

Formato:

Text Input

Default:

Habilitado

Neste campo o usuário poderá selecionar a classe da passagem\.

Conteúdo:

0 – Econômico

1 – Executivo

2 – Primeira Classe

__Tratamento:__

Esse campo será habilitado para os modelos de documento: 30\.

CH17082\_2015

Nome

Texto

N

S

Formato:

Text Input

Default:

Habilitado

Neste campo o usuário poderá informar o nome do passageiro referente a este bilhete\.

__Tratamento:__

Esse campo será habilitado para os modelos de documento: 30\.

CH17082\_2015


# MTZ_EFD_Parametros_Registro_E115_1925_Inf_Adicionais

- **Fonte:** MTZ_EFD_Parametros_Registro_E115_1925_Inf_Adicionais.docx
- **Modificado:** 2026-03-12
- **Tamanho:** 63 KB

---

THOMSON REUTERS

__                      Módulo Sped Fiscal – Parametrização dos Códigos das Informações __

__                                       Adicionais da Apuração p/os Registros E115 e 1925__

__MFS\-13074: __Essa demanda serve para reformular o item de menu que atende a parametrização do Registro E115, acrescentando o item de menu Registros E115/1925, em que haverá outras opções além da  Informações Adicionais da Apuração \(Registro E115/1925\)\.

__Localização__: Menu SPED, Módulo EFD – Escrituração Fiscal Digital, item Parâmetros 🡪 Registros E115/1925 🡪 Informações Adicionais da Apuração \(Registro E115/1925\)

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4593\-A

Vânia Mattos

Correção de erro na chamada da geração do mapa das entradas

17/09/2014

\(criação do docto\)

MFS\-13074

Julyana Perrucini

Alteração na estrutura do item de menu Parâmetros \- Informações Adicionais da Apuração \(Registro E115/1925\)\.

19/10/2017

MFS693829

Andréa Rocha

Criação de um campo para indicar se a descrição complementar do ajuste \(campo 04\-

DESCR\_COMPL\_AJ\) deve ser informada na geração do registro E115\.

10/10/2024

MFS1019580

Rogério Ohashi

Criação de um campo para indicar se o Valor de Informação Adicional \(campo 3\-

VL\_INF\_ADIC\) deve ser informada na geração do registro E115\.

13/01/2026

	

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

Esta parametrização foi criada pela OS2388\-N2ge \(Fev/2009\)\.

Nesta tela são cadastrados os códigos da Tabela das Informações Adicionais da Apuração, utilizada nos registros E115 e 1925 \(Valores Declaratórios\) do arquivo do Sped Fiscal\.

Os códigos são definidos por UF, assim como várias tabelas do Sped, como por exemplo:

\- Códigos de Ajustes provenientes de NF’s \(módulo DW – Manutenção – Cadastros\) 

\- Código de Ajuste Sped Fiscal \(módulo ICMS \- Apuração – Apuração do ICMS – Lanctos Complementares\)

\- Códigos de Tipos de Utilização de Crédito \(módulo Sped – Geração – Manutenção\) \(OS2388\-Vge\)

 

__RN01__

__                                                              Campo UF__

__UF:__

Este campo é uma lista das unidades da federação \(tabela ESTADO\), para seleção do usuário\.

Default: \(sem preenchimento\) 

__RN02__

__                                        Campo Código da Informação Adicional__

__Código da Informação Adicional__

Tamanho: 8 posições

Tipo: alfanumérico

\- Os dois primeiros caracteres do código são a própria sigla da UF, e na inserção de novos registros ficam sempre “fixos” com a sigla da

  UF selecionada no campo “UF”;

\- Os seis últimos caracteres são a parte “livre” do código, que são específicos de cada UF\. Na inserção de novos registros esta parte

  será informada pelo usuário, e terá obrigatoriamente um conteúdo numérico\);

Ao salvar a operação, será verificada se a parte “livre” do código tem realmente um conteúdo numérico\. Caso não, será exibida a seguinte mensagem de erro e a operação não será salva:  

                                              *“A parte final do código da informação  adicional deve ser um número”*

OS4593\-B \(correção de erro\): A descrição do campo foi corrigida para o nome correto \(“Código da Informação Adicional”\), definido na criação da tela, ao invés do nome “Tipo de Utilização de Crédito ”que aparecia na tela\.

__RN03__

__                                                        Campo Descrição__

__Descrição__

Tamanho: 250 posições

Tipo: alfanumérico

Campo de preenchimento obrigatório

Ao salvar a operação, será verificado o preenchimento do campo, e se não informado, será exibida a seguinte mensagem de erro e a operação não será salva:

                                                           *“O campo Descrição deve ser informado”*

__RN04__

__Campo Não Preencher Descrição Complementar do Ajuste__

__\[MFS693829\] __Inclusão do campo

__Não Preencher Descrição Complementar do Ajuste__

Tamanho: 1 posição

Tipo: checkbox

Campo de preenchimento não obrigatório\.  Default desmarcado\.

__RN05__

__Campo Não Preencher Valor de Informação Adicional__

__\[MFS1019580\] __Inclusão do campo

__Não Preencher Valor de Informação Adicional__

Tamanho: 1 posição

Tipo: checkbox

Campo de preenchimento não obrigatório\.  Default desmarcado\.

= = = = = 


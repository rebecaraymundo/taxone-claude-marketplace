# MTZ-Parametrizacao-das-Naturezas-do-ModeloIII

- **Fonte:** MTZ-Parametrizacao-das-Naturezas-do-ModeloIII.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 64 KB

---

THOMSON REUTERS

__                                 Módulo Ressarcimento & Complemento de ICMS\-ST__

__                      Parametrização das Naturezas de Operação para o Modelo III__

__Localização:__ Menu Estadual, Módulo: Ressarcimento e Complemento de ICMS\-ST,  item Parâmetros 🡪 CAT 17/1999 e CAT 99/2005 🡪 CFOP/Natureza para o Modelo III 🡪 Por Natureza de Operação

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4699

Alterações no tratamento da coluna “12 – Saídas com  Isenção ou Não Incidência” do Modelo III 

Alterações no tratamento da coluna “12 – Saídas com  Isenção ou Não Incidência” do Modelo III \(ver __RN01__\)

22/12/2014

\(criação do docto\)

	

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

__RN01__

__                                                   Campo Valor de Confronto__

__Alteração da OS4699__: \(inclusão do campo “Valor de Confronto”\)

__Valor de Confronto__ 🡪 Este campo exibe o tipo de valor de confronto a ser gerado no relatório Modelo III, dependendo da operação selecionada no campo “Parâmetro”\.

O campo é uma lista com as seguintes opções:

VC na coluna 15

VC na coluna 16

Para a opção “VC na coluna 15” 🡪 será gravado o conteúdo “1”

Para a opção “VC na coluna 16” 🡪 será gravado o conteúdo “2”

O campo será habilitado __*apenas*__ quando o parâmetro informado no campo “Parâmetro” for uma das seguintes opções:

      \- Saídas com Isenção ou Não Incidência

      \- Saídas com Isenção ou Não Incidência \(Devolução de Vendas\)

Para qualquer uma das demais opções, o campo será sempre inicializado com o valor default do sistema \(vide tabela abaixo\), e o usuário __não__ poderá alterar o seu conteúdo, pois o campo ficará __desabilitado__\. 

O valor default a ser exibido na inclusão de novos CFOP’s/Naturezas é o seguinte:

__Tipo do Parâmetro__

__COD\_PARAM__

__\(coluna que identifica o parâmetro na tabela\)__

__Conteúdo default a ser exibido no campo “Valor de Confronto”__

__Conteúdo gravado na tabela __

Saída a Consumidor ou Usuário Final

344

__VC na coluna 15 __

__“1”__

Saída a Consumidor ou Usuário Final \(Devolução de Vendas\)

345

__VC na coluna 15__

__“1”__

Saídas com Isenção ou Não Incidência

348

__VC na coluna 15 __

__“1”__

Saídas com Isenção ou Não Incidência \(Devolução de Vendas\)

349

__VC na coluna 15__

__“1”__

Saídas para Outros Estados

350

__VC na coluna 16__

__“2”__

Saídas para Outros Estados \(Devolução de Vendas\)

351

__VC na coluna 16__

__“2”__

Fato Gerador Não Realizado

346

__VC na coluna 16__

__“2”__

Fato Gerador Não Realizado \(Devolução de Vendas\)

347

__VC na coluna 16__

__“2”__

__Demais tipos de parâmetro não citados acima__

\(outros\)

__\(vazio\)__

__\(nulo\)__

Desta forma, teremos:

No caso do campo “Parâmetro” = “Saídas com Isenção ou Não Incidência” 

                                                 __ou__ “Saídas com Isenção ou Não Incidência \(Devolução de Vendas\)”:

      Na inclusão de novos CFOP’s/Naturezas, o campo terá o default = “VC na coluna 15”, conforme a tabela cima, mas o usuário poderá alterá\-lo;

 No caso do campo “Parâmetro” = qualquer uma das demais opções \(exceto as duas citadas na condição anterior\):

      Na inclusão de novos CFOP’s/Naturezas, o campo mostrará sempre o conteúdo default do sistema, __conforme a tabela acima__, e o usuário __não__ 

      poderá alterá\-lo, já que o campo ficará desabilitado nesses casos;

= = = = = 


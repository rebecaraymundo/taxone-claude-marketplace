---
source: "MTZ-Report_Fiscal-Mercadorias_IPI_nao_Escriturado.doc"
category: Report_Fiscal
converted: auto
---

                          Relatório Mercadorias - IPI não Escriturado
 
Localização: Menu Básicos, Módulo Report Fiscal, menu Gerenciais --> Documentos Fiscais --> Analítico --> Mercadoria - IPI não Escriturado

                                           Documento de Requisito

Doc
Alteração
Data
Resp
OS4031
Alteração no relatório para permitir a geração multiestabelecimento com filtro por UF, e também a geração por inscrição estadual única.
10/06/2013
Vânia Mattos


RN00

Parâmetros de Tela:

Alteração OS4031 (Jun/13):
Incluídos os parâmetros de geração por I.E.U. e UF, e o campo Estabelecimento passou para a parte inferior da tela, passando a demonstrar vários estabelecimentos para  permitir a geração multiestabelecimento. Além disso, o campo da pessoa/is/jur ficará desabilitado para digitação.

Pessoa Fis/Jur --> Este campo funciona da seguinte forma:

Se campo "Critério" for = "Período/Pessoa Física ou Jurídica":
     Neste caso, o usuário poderá escolher uma pessoa fis/jur, mas, não será permitida a digitação
     do código. Apenas a pastinha amarela ficará habilitada, e para informar ou selecionar uma
     pessoa, o usuário deverá fazê-lo obrigatoriamente através da janela de seleção que é aberta
     por esta pasta;
Senão
     Neste caso o usuário não poderá selecionar uma pessoa fis/jur (nem digitando nem através da
     pastinha); 

Geração por Inscrição Estadual Única --> campo do tipo S/N, default = desmarcado

UF --> este campo exibe a lista das UF's da tabela dos estados + opção "Todas" 

Estabelecimentos --> Neste quadro serão demonstrados os estabelecimentos da Empresa do login, de acordo com as seguintes regras:

     - Apenas os estabelecimentos da UF selecionada no campo "UF";

     - Caso o parâmetro "Geração por Inscrição Estadual Única" tenha sido selecionado, então
       serão demonstrados apenas os estabelecimentos centralizadores (conforme parametrização
       do módulo Controle das Obrigações Estaduais, menu Obrigações --> Estabelecimentos c/
       I.E.U.);


RN01
 
Processamento:

Alteração OS4031 (Jun/13):
O relatório passou a possibilitar a geração para vários estabelecimentos simultaneamente (geração multiestabelecimento), e também a trabalhar com emissão por I.E.U.

Para cada estabelecimento selecionado em tela, será emitido um relatório.

Utilização do parâmetro "Geração por Inscrição Estadual Única":

Quando este parâmetro for = "S", a geração será centralizada, e desta forma, para cada relatório, serão recuperados os documentos fiscais do estabelecimento selecionado (centralizador ) + os documentos de todos os estabelecimentos centralizados. Para identificar os estabelecimentos centralizados, será verificada a parametrização do módulo Controle das Obrigações Estaduais, menu Obrigações --> Estabelecimentos c/.I.E.U.



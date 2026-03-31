# MTZ-Job_Servidor-Importacao_Batch-Historico_das_Importacoes

- **Fonte:** MTZ-Job_Servidor-Importacao_Batch-Historico_das_Importacoes.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 64 KB

---

THOMSON REUTERS

                                                                                     __Módulo Job Servidor__

__   __

__                                             Relatório do Histórico da Importação Batch__

__Localização__: Menu Básicos, Módulo Job Servidor, item Importação Batch 🡪 Relatórios 🡪 Histórico das Importações”

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4538

Programação multiempresa

Inclusão do código da empresa no coluna dos estabelecimentos \(ver __RN02__\)

29/08/2014

\(criação do docto\)

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

*Levantamento dos parâmetros feito em 29/08/2014*:

__Empresa__: O usuário pode escolher uma única empresa, ou escolher a opção = “Todas”;

__Período__: Data inicial e final do período de execução da importação batch;

__Programação__: O usuário poderá selecionar uma única programação, ou deixar o campo sem preenchimento;

__RN01__

__                                           Origem e Recuperação dos Dados__

*Levantamento da utilização dos parâmetros feito em 29/08/2014*:

__Origem dos dados__: tabela que armazena os dados da execução da importação batch \(IBT\_HISTORICO\)\. 

O relatório recupera os dados de acordo com os parâmetros informados em tela, da seguinte forma:

__Utilização do parâmetro Empresa__:

Uma empresa 🡪 Serão considerados apenas os dados da empresa informada\. As programações executadas no período informado são demonstradas em ordem de *estabelecimento e data da importação*\.

Todas 🡪 Serão considerados os dados de todas as empresas\. As programações executadas no período informado são demonstradas em ordem de *empresa, estabelecimento e data da importação*\. No entanto, *não é gerado um relatório para cada empresa*, ou seja, ao finalizar os dados de uma empresa, o relatório começa a mostrar na sequencia os estabelecimentos da próxima empresa, seguindo a ordenação\.

__Utilização do parâmetro Período__: Serão demonstradas apenas as programações executadas no período informado\. O filtro é feito pela data da coluna DT\_IMPORT;

__Utilização do parâmetro Programação__: Se o campo não for preenchido, serão consideradas todas as programações registradas na tabela\. Caso contrário, serão considerados apena os dados da programação informada;

__RN02__

__                                                  Preenchimento dos Dados__

__Coluna Empresa / Estabelecimento: __

Originalmente esta coluna exibia apenas o estabelecimento, mas foi alterada na __OS4538__ para mostrar também o código da empresa,__ __ com objetivo de facilitar a identificação da origem dos estabelecimentos, quando o relatório for gerado com o parâmetro “Empresa” = Todas\.

*\(já que neste caso os dados são demonstrados em ordem de empresa, estabelecimento e data da importação, mas sem gerar um relatório para cada empresa, e sem saltar de página\)*

Esta coluna é preenchida com o código da empresa \+ código do estabelecimento \+ razão social do estabelecimento\. Enquanto se tratar da mesma empresa, estabelecimento e página, a informação *não* se repete nas demais linhas, até que mude a empresa, o estabelecimento, ou na mudança de página\.

= = = = = 


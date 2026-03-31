# MTZ-LAICMS-Relat_Cred_Presumido-SC

- **Fonte:** MTZ-LAICMS-Relat_Cred_Presumido-SC.docx
- **Modificado:** 2021-06-17
- **Tamanho:** 68 KB

---

THOMSON REUTERS

                                                          __Módulo Lançamentos Automáticos de ICMS__

__  __

__                                    Relatório do Lançamento de Crédito Presumido – SC__

__Localização__: Menu Estadual, Módulo Lançamentos Automáticos ICMS, item Relatórios 🡪 Crédito Presumido – SC 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS2837

Melhorias 

Inclusão das duas datas no layout \(fiscal e emissão\) e inclusão de opção para salvar o relatório em Excel mostrando todas as colunas do layout \(ver __RN00__ e __RN04__\)\.

25/08/2014

\(criação do docto\)

MFS46704

Andréa Rocha 

Alteração de duas colunas no relatório, que devem ser utilizadas de acordo com um novo parâmetro criado em tela\.

25/02/2021

MFS66742

Andréa Rocha 

Alteração da forma de gerar o relatório quando se utiliza o parâmetro “Valor Utilizado para o Cálculo” igual a “Base ICMS”, para tratar a situação da nota fiscal que não tem Base de ICMS destacado\.

17/06/2021

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

Alteração da __OS2837__: inclusão da opção <Excel>

Opção <Excel> da barra de menu 🡪 esta opção permite que o relatório gerado seja salvo em formato Excel, onde aparecerão todas as colunas do relatório, inclusive as quatro últimas colunas do layout que demonstram os valores calculados para cada item\.

__RN01__

__                                                        Parâmetros de Tela__

\[MFS46704\] Incluir o parâmetro abaixo, depois do último parâmetro da tela:

Campo: Valor Utilizado para o Cálculo

Será um campo do tipo Radiobutton, com as opções:

\- Valor Contábil do Item

\- Base ICMS

A opção “Valor Contábil do Item” deve vir por marcada por default\.

__RN02__

__                                                    Recuperação dos Dados__

__RN03__

__                                                         Processamento __

__RN04__

__                                                Preenchimento dos Dados __

Regras de preenchimento dos campos:

__Linhas de Detalhe__:

__Dt\. XXXXX__

\(coluna 2\) 

Título da coluna:

Se a data selecionada em tela = Data Fiscal 🡪 o título da coluna será = “__Dt\. Fiscal__”

Se a data selecionada em tela = Data Emissão 🡪 o título da coluna será = “__Dt\. Emissão__”

Conteúdo:

Se a data selecionada em tela = Data Fiscal 🡪 o conteúdo será a data fiscal do documento \(SAFX07\)

Se a data selecionada em tela = Data Emissão 🡪 o conteúdo será a data de emissão do documento \(SAFX07\)

__Dt\. XXXXX__

\(coluna 3\) 

Alteração da __OS2837__: Esta OS criou a segunda coluna de data, e assim, o relatório passou a exibir sempre as duas datas \(fiscal e emissão\)\. Na primeira coluna aparece a data selecionada em tela, e na segunda, aparece a outra \(observar que a regra de preenchimento do título e do conteúdo da coluna é o inverso da coluna anterior\)\. 

Título da coluna:

Se a data selecionada em tela = Data Fiscal 🡪 o título da coluna será = “__Dt\. Emissão__”

Se a data selecionada em tela = Data Emissão 🡪 o título da coluna será = “__Dt\. Fiscal__”

Conteúdo:

Se a data selecionada em tela = Data Fiscal 🡪 o conteúdo será a data de emissão do documento \(SAFX07\)

Se a data selecionada em tela = Data Emissão 🡪 o conteúdo será a data fiscal do documento \(SAFX07\)

__% Recup__

\(coluna 9\)

Título da coluna: __% Recup__

Se o parâmetro Seleção = CFOP/Produto

      Preencher com a coluna Percentual Recuperado da tela de parametrização por Produto \(Parâmetros 🡪  

      Parâmetros p/ Cálculos e Relatórios 🡪 Parâmetros de Relatórios p/ Produto\)\.

Se o parâmetro Seleção = CFOP/NBM

      Preencher com a coluna Percentual Recuperado da tela de parametrização por NBM \(Parâmetros 🡪  

      Parâmetros p/ Cálculos e Relatórios 🡪 Parâmetros de Relatórios p/ NBM\)\.

__Valor Mercadoria__

__       OU__

__Base ICMS__

\(coluna 10\)

Alteração da MFS46704 – Alteração no valor utilizado para o cálculo do lançamento, de acordo com o novo parâmetro de tela

O título da coluna será preenchido de acordo com o parâmetro “Valor Utilizado para o Cálculo”\. \(Vide Parâmetros de Tela\) 

Título da coluna:

Se o parâmetro “Valor Utilizado para o Cálculo” = Valor Contábil do Item 

     O título da coluna será = “__Valor Mercadoria__”

Se o parâmetro “Valor Utilizado para o Cálculo” = Base ICMS

     O título da coluna será = “__Base ICMS__”

Conteúdo:

Se o parâmetro = __Valor Mercadoria__ 

     Preencher com o Valor Contábil do Item \(campo 64 da SAFX08\)\.

__\[MFS66742\]__ Alteração da forma de cálculo para o parâmetro “Valor Utilizado para o Cálculo” igual a “Base ICMS”, para tratar a situação da nota fiscal que não tem Base de ICMS destacado

Se o parâmetro = __Base ICMS__ 

     Preencher com a Base ICMS \(campo 56 da SAFX08\)\.

     Se a Base ICMS não estiver preenchida ou estiver preenchida com zero e o CST = ‘51’ \(campo 31 da SAFX08\)

          Preencher  com o Valor Contábil do Item 

        

__Valor Calculado__

\(coluna 11\)

Alteração da MFS46704 – Alteração no valor utilizado para o cálculo do lançamento, de acordo com o novo parâmetro de tela

O título da coluna será preenchido de acordo com o parâmetro “Valor Utilizado para o Cálculo”\. \(Vide Parâmetros de Tela\) 

Título da coluna:

Se o parâmetro “Valor Utilizado para o Cálculo” = Valor Contábil do Item 

     O título da coluna será = “__Valor Calculado \(Valor Mercadoria \* % Recup\.\)__”

Se o parâmetro “Valor Utilizado para o Cálculo” = Base ICMS

     O título da coluna será = “__Valor Calculado \(Base ICMS \* % Recup\.\)__”

Conteúdo:

Se o parâmetro = __Valor Mercadoria__ 

     Preencher com o Valor Contábil do Item \(campo 64 da SAFX08\) \* % Recup \(coluna 9 do relatório\)\.

__\[MFS66742\]__ Alteração da forma de cálculo para o parâmetro “Valor Utilizado para o Cálculo” igual a “Base ICMS”, para tratar a situação da nota fiscal que não tem Base de ICMS destacado

Se o parâmetro = __Base ICMS__ 

     Preencher com a Base ICMS \(campo 56 da SAFX08\) \* % Recup \(coluna 9 do relatório\)\.

     Se a Base ICMS não estiver preenchida ou estiver preenchida com zero e o CST = ‘51’ \(campo 31 da SAFX08\)

          Preencher  com o Valor Contábil do Item \(campo 64 da SAFX08\) \* % Recup \(coluna 9 do relatório\)\.


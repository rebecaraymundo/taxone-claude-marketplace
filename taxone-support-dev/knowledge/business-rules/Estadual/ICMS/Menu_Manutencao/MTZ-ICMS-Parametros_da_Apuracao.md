# MTZ-ICMS-Parametros_da_Apuracao

- **Fonte:** MTZ-ICMS-Parametros_da_Apuracao.docx
- **Modificado:** 2024-08-16
- **Tamanho:** 82 KB

---

THOMSON REUTERS

                                                                                          __Módulo ICMS__

__   __

__                               Parametrização dos Lançamentos Automáticos da Apuração__

__Localização__: Menu Estadual, Módulo ICMS, item Manutenção à Parâmetros p/ Lançamentos Automáticos à Parâmetros da Apuração

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS3571

Diferencial de alíquota do Frete

Inclusão de parâmetro para o diferencial de alíquota referente às operações de aquisição de serviços de frete \(ver __RN01__ e __RN02__\)\.

10/07/2014

\(criação do docto\)

MFS6407

Difal referente às operações sujeitas à alíquota de 4% 

Inclusão de parâmetro para o diferencial de alíquota referente às operações de aquisição de produtos importados, em operações sujeitas à alíquota de 4% \(ver __RN01__ e __RN02__\)\.

07/06/2017

MFS4142

Novos Campos na Parametrização 

Criação de novos campos na parametrização para possibilitar o lançamento dos valores do DIFAL em débitos especiais \(ao invés de gerar lançamentos complementares no P9\)\. 

06/07/2017

MFS27431

Novos Campos na Parametrização

Criação de novos campos na parametrização para possibilitar o lançamento dos valores do DIFAL em débitos especiais para o registro E111/E113 do Sped Fiscal\.\.

25/07/2019

MFS22260

Ajuste na parametrização de código de ajuste\. 

Ajuste na tela de parametrização, para considerar o código de ajuste informativo \(Diferencial de Aliquota Recolhido Fora da Conta Gráfica\) para o estado de Rondonia\.

06/04/2020

MFS76802

Rogério Ohashi

Inclusão de parâmetro para o diferencial de alíquota para manter os registros da SAFX113, importado/ ou incluído manualmente nos lançamentos automáticos\. \(atendimento ao Registro C197/D197\)\.

21/03/2022

MFS88010

Liliane Assaf

Inclusão do parâmetro ICMS de Diferença de Alíquotas \- Frete \- Débito/Crédito \(RN01, RN03, RN04\)

04/07/2022

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

Esta parametrização é utilizada para a geração automática de lançamentos complementares da Apuração do ICMS\. Os lançamentos de diversas modalidades são calculados durante a apuração do ICMS, e os resultados obtidos gravados como lançamentos complementares da apuração\.

Serão calculados apenas os lançamentos parametrizados pelo usuário, e na geração de cada lançamento, são utilizados os dados parametrizados nesta manutenção\.

Alteração __MFS4142__: A parametrização foi alterada para possibilitar que os valores apurados sejam lançados na Apuração de duas formar distintas:

     \- Lançamento complementar na Apuração do ICMS *\(conforme feito na versão original\);*

     \- Lançamento como Débito Especial \(valores extra apuração\);

Para isso foram criados novos campos: “*Forma de lançamento dos valores*” e campos do quadro “*Parâmetros p/ Geração de Débitos Especiais*”\. A opção de lançamento será feita através do campo “*Forma de lançamento dos valores*”\. 

\(Verificar detalhes sobre o funcionamento do campo, e impactos nos demais campos da tela na __RN02__\)

Alteração __MFS27431__: A parametrização foi alterada para possibilitar que os valores apurados e lançados como Débitos Especiais possam ser gerados através do C195/C197, conforme feito na __MFS4142__, ou, através do E111/E113\. Lembrando que, os débitos especiais não interferem na Apuração do ICMS gerada no módulo ICMS \(livro P9\), e são tratados no sistema apenas para a geração do Sped Fiscal\.

__RN01__

__                                                        Campo ‘Parâmetro’:__

O campo “__Parâmetro__” indica o tipo de lançamento a ser calculado, com as seguintes opções:

 

     » ICMS Devolução e Remessa Interestadual/ST \- Resolução 119/04 SER\-RJ \- Crédito   
     » ICMS de Diferença de Alíquotas Material de Consumo \- Débito/Crédito   
     » ICMS de Diferença de Alíquotas Material de Consumo \- Débito   
     » ICMS de Diferença de Alíquotas Ativo Imobilizado \- Débito   
     » ICMS de Diferença de Alíquotas Ativo Imobilizado \- Débito/Crédito   
     » ICMS de Diferença de Alíquotas Ativo Imobilizado \- Regime Especial   
     » Transferência de Crédito / Débito de ICMS \- Ind\. NF Transf\. \- 1 e 3       
     » Transferência de Crédito de ICMS da Mesma Empresa \- Ind\. NF Transf \- 6   
     » Transferência de Crédito de ICMS de Empresa Independente \- Ind\. NF Transf \- 7   
     » Transferência de Débito de ICMS da Mesma Empresa \- Ind\. NF Transf – 3

     » ICMS de Diferença de Alíquotas – Frete 

     » ICMS de Diferença de Alíquotas \- Frete \- Débito/Crédito

     » ICMS de Diferença de Alíquotas Produtos Importados \- Op\. Sujeitas à Alíquota de 4%

     » ICMS de Diferença de Alíquotas Material de Consumo – Débito \(extras\)   
     » ICMS de Diferença de Alíquotas Ativo Imobilizado \- Débito \(extras\)  


*\(alteração da *__*OS3571*__* \(Jul/2014\): incluído o parâmetro “ICMS de Diferença de Alíquotas – Frete”\);*

*\(alteração da *__*MFS6407*__* \(Jun/2017\): incluído o parâmetro “ICMS de Diferença de Alíquotas Produtos Importados \- Op\. Sujeitas à Alíquota de 4%”\);*

*	*

*\(alteração da *__*MFS27431*__* \(Jul/2019\): incluídos os parâmetros “ICMS de Diferença de Alíquotas Material de Consumo – Débito \(extras\)” e “ICMS de Diferença de Alíquotas Ativo Imobilizado – Débito \(extras\)”;*

*\(alteração da *__*MFS88010*__* \(Jul/2022\): incluído o parâmetro ICMS de Diferença de Alíquotas \- Frete \- Débito/Crédito\)*

__RN02__

__                                          Campo ‘Forma de Lançamento dos Valores’:__

\(campo criado pela __MFS4142__\) 

O campo “__Forma de Lançamento dos Valores__” indica a forma como os valores apurados serão lançados na Apuração do ICMS do período, com as seguintes opções:

     \- Lançamento na Apuração do ICMS 

     \- Lançamento em Débito Especial \(extra apuração\)

Na inclusão de um novo registro, a opção default é sempre = “Lançamento na Apuração do ICMS”\.

A opção “__Lançamento em Débito Especial__” será habilitada *apenas* para os seguintes tipos de parâmetros \(campo “Parâmetro”\):

<a id="_Hlk15389249"></a>        \- ICMS de Diferença de Alíquotas Material de Consumo \- Débito   
        \- ICMS de Diferença de Alíquotas Ativo Imobilizado \- Débito   
        \- ICMS de Diferença de Alíquotas – Frete

        \- ICMS de Diferença de Alíquotas Produtos Importados – Op\. Sujeitas à Alíquota de 4%

        \- ICMS de Diferença de Alíquotas Material de Consumo – Débito \(extras\)   
        \- ICMS de Diferença de Alíquotas Ativo Imobilizado \- Débito \(extras\)  


A opção “__Lançamento na Apuração do ICMS__” será habilitada para *todos* os tipos de parâmetros \(campo “Parâmetro”\), exceto para os seguintes tipos:

        \- ICMS de Diferença de Alíquotas Material de Consumo – Débito \(extras\)   
        \- ICMS de Diferença de Alíquotas Ativo Imobilizado \- Débito \(extras\)  


 

Para os demais tipos de parâmetro \(não citados acima\), o usuário *não* poderá optar, e a geração será sempre lançamento na apuração do ICMS\. Por isso, as duas opções ficam desabilitadas para alteração, sendo mantido o valor default \(“Lançamento na Apuração do ICMS”\)\.

__Sobre o preenchimento dos demais campos da tela__:

  

\- __Quando for selecionada a opção “Lançamento na Apuração do ICMS”:__

Neste caso, os campos do quadro “Parâmetros p/ Geração de Débitos Especiais” ficarão desabilitados, e o usuário deverá preencher as informações dos seguintes quadros, de acordo com a modalidade informada no campo “Parâmetro”\.

   “Operação a Débito”

   “Operação a Crédito”

   “Lançamentos de Transferência de Crédito/Débito”

   “Tipo de Lançamento p/o Sped Fiscal”

OBS: Todas as críticas e mensagens realizadas para os campos destes 4 quadros continuam válidas, mas serão realizadas apenas quando se tratar desta opção \(opção = Lançamento na Apuração do ICMS\)\.

 

\- __Quando for selecionada a opção “Lançamento em Débito Especial__”:

Neste caso, os campos dos quadros citados acima ficarão desabilitados, e o usuário deverá preencher as informações do quadro “Parâmetros p/ Geração de Débitos Especiais”\. 

__RN03__

__                                                 Quadro ‘Operação a Débito’__

Alteração __MFS4142__: Esta MFS criou o campo “Forma de Lançamento dos Valores” \(__RN02__\), e quando a opção do usuário for = “Lançamento em Débito Especial”, os campos deste quadro *não* serão habilitados\.

Assim, a regra para habilitar ou não este quadro é a seguinte:

Se opção do campo “Forma de Lançamento dos Valores” = “Lançamento em Débito Especial”

     Neste caso os campos deste quadro permanecerão desabilitados\.

Senão

     Neste caso os campos deste quadro serão habilitados ou não, dependendo do parâmetro informado, conforme definido a seguir\.

Dependendo do tipo do parâmetro, será efetuado um lançamento a débito, a crédito, ou os dois\.

Assim, os campos deste quadro serão habilitados ou não, dependendo do parâmetro, da seguinte forma:

				

__Parâmetro__

__Operação a Débito__

ICMS Devolução e Remessa Interestadual/ST \- Resolução 119/04 SER\-RJ \- Crédito

ICMS de Diferença de Alíquotas Material de Consumo \- Débito/Crédito

X

ICMS de Diferença de Alíquotas Material de Consumo \- Débito

X

ICMS de Diferença de Alíquotas Ativo Imobilizado \- Débito

X

ICMS de Diferença de Alíquotas Ativo Imobilizado \- Débito/Crédito

X

ICMS de Diferença de Alíquotas Ativo Imobilizado \- Regime Especial

X

Transferência de Crédito / Débito de ICMS \- Ind\. NF Transf\. \- 1 e 3     

Transferência de Crédito de ICMS da Mesma Empresa \- Ind\. NF Transf \- 6

Transferência de Crédito de ICMS de Empresa Independente \- Ind\. NF Transf \- 7 

Transferência de Débito de ICMS da Mesma Empresa \- Ind\. NF Transf – 3

X

ICMS de Diferença de Alíquotas – Frete

X

<a id="_Hlk107832058"></a>ICMS de Diferença de Alíquotas \- Frete \- Débito/Crédito

X

ICMS de Diferença de Alíquotas Produtos Importados \- Op\. Sujeitas à Alíquota de 4%

X

ICMS de Diferença de Alíquotas Material de Consumo – Débito \(extras\)

ICMS de Diferença de Alíquotas Ativo Imobilizado – Débito \(extras\)

OBS\.: Os parâmetros do tipo “*ICMS de Diferença de Alíquotas Material de Consumo – Débito \(extras\)*” e “*ICMS de Diferença de Alíquotas Ativo Imobilizado – Débito \(extras\)*”, apesar de serem débitos, não serão tratados neste quadro\. Estes itens foram criados para atender à legislação de GO \(DIFAL das notas extemporâneas\), e por definição, serão tratados apenas como débitos especiais\.

 

__RN04__

__                                              Quadro ‘Operação a Crédito’__

Alteração __MFS4142__: Esta MFS criou o campo “Forma de Lançamento dos Valores” \(__RN02__\), e quando a opção do usuário for = “Lançamento em Débito Especial”, os campos deste quadro *não* serão habilitados\.

Assim, a regra para habilitar ou não este quadro é a seguinte:

Se opção do campo “Forma de Lançamento dos Valores” = “Lançamento em Débito Especial”

     Neste caso os campos deste quadro permanecerão desabilitados\.

Senão

     Neste caso os campos deste quadro serão habilitados ou não, dependendo do parâmetro informado, conforme definido a seguir\.

Dependendo do tipo do parâmetro, será efetuado um lançamento a débito, a crédito, ou os dois\.

Assim, os campos deste quadro serão habilitados ou não, dependendo do parâmetro, da seguinte forma:

__Parâmetro__

__Operação a Crédito__

ICMS Devolução e Remessa Interestadual/ST \- Resolução 119/04 SER\-RJ \- Crédito

X

ICMS de Diferença de Alíquotas Material de Consumo \- Débito/Crédito

X

ICMS de Diferença de Alíquotas Material de Consumo \- Débito

ICMS de Diferença de Alíquotas Ativo Imobilizado \- Débito

ICMS de Diferença de Alíquotas Ativo Imobilizado \- Débito/Crédito

X

ICMS de Diferença de Alíquotas Ativo Imobilizado \- Regime Especial

X

Transferência de Crédito / Débito de ICMS \- Ind\. NF Transf\. \- 1 e 3     

Transferência de Crédito de ICMS da Mesma Empresa \- Ind\. NF Transf \- 6

Transferência de Crédito de ICMS de Empresa Independente \- Ind\. NF Transf \- 7 

Transferência de Débito de ICMS da Mesma Empresa \- Ind\. NF Transf – 3

X

ICMS de Diferença de Alíquotas – Frete

ICMS de Diferença de Alíquotas \- Frete \- Débito/Crédito

X

ICMS de Diferença de Alíquotas Produtos Importados \- Op\. Sujeitas à Alíquota de 4%

ICMS de Diferença de Alíquotas Material de Consumo – Débito \(extras\)

ICMS de Diferença de Alíquotas Ativo Imobilizado – Débito \(extras\)

__RN05__

__                          Quadro ‘Lançamentos de Transferência de Crédito/Débito’__

Alteração __MFS4142__: Esta MFS criou o campo “Forma de Lançamento dos Valores” \(__RN02__\), e quando a opção do usuário for = “Lançamento em Débito Especial”, os campos deste quadro *não* serão habilitados\.

__RN06__

__                                   Quadro ‘Tipo de Lançamento p/o Sped Fiscal’__

Alteração __MFS4142__: Esta MFS criou o campo “Forma de Lançamento dos Valores” \(__RN02__\), e quando a opção do usuário for = “Lançamento em Débito Especial”, os campos deste quadro *não* serão habilitados\.

__\[MFS76802\] __Inclusão de parâmetro “Associar os registros SAFX113 \- Via importação/manual \(Reg C197/D197\)” – Lançamento na Apuração do ICMS

Este parâmetro deverá ser habilitado caso o cliente escolha considerar no processo de geração dos Lançamentos Automáticos, \(*1\-Lançamentos a ser demonstrado no Bloco C/D \(RegC197/D197*\) a tabela SAFX113 importada via interface ou incluída manualmente,  caso esse parâmetro seja habilitado o sistema passará a considerar o registro x113\_ajuste\_apur da Nota Fiscal, não *criando* no processo de Lançamentos Automáticos\.

 

- *Esse parâmetro deverá ser incluído logo após o parâmetro *__*1\-Lançamentos a ser demonstrado no Bloco C/D \(RegC197/D197*\)__*\.*

Opções:  

       \[  \] Manter registros SAFX113 – via importação/manual \(Reg C197/D197\)

__Obs:\.__ O parâmetro somente deverá ser habilitado para seleção se o parâmetro “__*1\-Lançamentos a ser demonstrado no Bloco C/D \(RegC197/D197*\)__*\.” Estiver habilitado\.*

Default = desmarcado

__RN07__

__                     Quadro ‘__<a id="_Hlk14967749"></a>__Parâmetros p/ Geração de Débitos Especiais \(Dif\. Alíquota\)’__

Alteração __MFS4142__: Esta MFS criou este quadro para parametrizar os dados necessários p/a geração de débitos especiais\.  

Alteração __MFS27431__: Esta MFS incluiu novos campos neste quadro para parametrizar os dados necessários p/a geração de débitos especiais no registro E111 do Sped Fiscal;  

Os campos deste quadro serão habilitados apenas quando a opção selecionada pelo usuário no campo “Forma de Lançamento dos Valores” \(__RN02__\) for = “Lançamento em Débito Especial”\. Caso contrário, os campos deste quadro *não* serão habilitados\.

Campo “__Tipo de Débito Especial”:__                                        \(Campo incluído na __MFS27431__\)

Este campo apresenta duas opções:       

__  ![XXX](data:image/png;base64,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)__

As opções são alternativas, e a opção default é = C197/D197 \(forma original de geração dos débitos especiais\)\.

Se opção escolhida = “C197/D197”:

      Serão habilitados os campos “Cód\.Ajuste \(Sped Fiscal \- Reg\.C197/D197\)” e “Cód\.Observação \(Sped Fiscal \- Reg\.C195/D195\)”;

      Os demais serão desabilitados;

Se opção escolhida = “E111/E113”:

      Serão habilitados os campos “Cód\.Ajuste \(Sped Fiscal \- Reg\.E111\)” e “Descrição Complementar do Débito \- Reg\. E111\)”;

      Os demais serão desabilitados;

Campo “__Cód\.Ajuste \(Sped Fiscal – Reg\. C197/D197\)__”:

Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste Provenientes de Documentos Fiscais\.

A manutenção da “Tabela dos Códigos de Ajuste Provenientes de Documentos Fiscais” é feita no __Módulo DW__, menu “Manutenção à Cadastros à Códigos de Ajuste provenientes de NF’s \(Sped Fiscal\)”\.

É campo obrigatório \(no caso do campo “Forma de Lançamento dos Valores” = “Lançamento em Débito Especial” e o campo “Tipo de Débito Especial” = C197/D197\)\.

Serão disponibilizados para seleção apenas os códigos que atendam aos seguintes critérios:

     \- Terceiro caracter = “7” \(= Débitos Especiais\)

     \- Quarto caracter = “0” \(= Apuração do ICMS próprio\)

__\[MFS22260\]__

Quando a UF do estabelecimento = ‘RO’, será também disponibilizado para a seleção o código que atende ao seguinte critério:

\- Terceiro caracter = “9” \(Para essa condição, tem previsto somente o código RO90000002 \- Ajuste Informativo \- Diferença de Alíquota recolhido fora da conta gráfica\)\.

Campo “__Cód\.Observação \(Sped Fiscal – Reg\.C195/D195\)__”:

Este campo trabalha com janela de seleção da Tabela de Cadastro de Observações \(SAFX2009\)\. 

É campo obrigatório \(no caso do campo “Forma de Lançamento dos Valores” = “Lançamento em Débito Especial” e o campo “Tipo de Débito Especial” = C197/D197\)\.

Serão disponibilizados para seleção apenas as observações do Grupo selecionado pelo usuário na abertura da tela\.

Obs: A manutenção do cadastro de observações é feito no Módulo DW, menu  “Manutenção à Códigos àCadastro de Observações”\)

Campo “__Cód\.Ajuste \(Sped Fiscal – Reg\. E111\)__”:                                                 \(Campo incluído na __MFS27431__\)

Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste do Sped Fiscal\.

A manutenção da “Tabela dos Códigos de Ajuste do Sped Fiscal” é feita no __Módulo ICMS__, menu “Apuração à Apuração do ICMS à Lançamentos Complementares à Código de Ajuste SPED FISCAL”\.

É campo obrigatório \(no caso do campo “Forma de Lançamento dos Valores” = “Lançamento em Débito Especial” e o campo “Tipo de Débito Especial” = E111/E113\)\.

Serão disponibilizados para seleção apenas os códigos que atendam aos seguintes critérios:

     \- Terceiro caracter = “0” \(= Apuração Própria \- ICMS\)

     \- Quarto caracter = “5” \(= Débito Especial\)

Campo “__Descrição Complementar do Débito \(E111\)__”:                                                 \(Campo incluído na __MFS27431__\)

Campo não obrigatório\.

Tipo/Tamanho: Alfanumérico, 250 posições \(de acordo com *a coluna DSC\_DEBITO da tabela ICT\_DEBITO\_ESP\)\.*

__\[MFS76802\] __Inclusão de parâmetro “Associar os registros SAFX113 \- Via importação/manual \(Reg C197/D197\)” – Lançamento em Débitos Especiais \(extra\-apuração\)

Este parâmetro deverá ser habilitado caso o cliente escolha considerar no processo de geração dos Lançamentos Automáticos, \(__C197/D197__\) a tabela SAFX113 importada via interface ou incluída manualmente,  caso esse parâmetro seja habilitado o sistema passará a considerar o registro x113\_ajuste\_apur da Nota Fiscal, não *criando* no processo de Lançamentos Automáticos\.

 

- *Esse parâmetro deverá ser incluído no final do “quadro” *__*Parâmetros p/ Geração de Débitos Especiais \(Dif\.Alíquota\)*__*, habilitar somente quando a opção “C197/D197” for selecionado\.*

Opções:  

       \[  \] Manter registros SAFX113 – via importação/manual \(Reg C197/D197\)

Default = desmarcado

= = = = = 


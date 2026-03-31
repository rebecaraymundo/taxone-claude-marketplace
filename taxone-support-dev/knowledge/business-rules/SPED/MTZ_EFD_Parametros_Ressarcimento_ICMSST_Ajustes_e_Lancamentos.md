# MTZ_EFD_Parametros_Ressarcimento ICMSST_Ajustes_e_Lancamentos

> Fonte: MTZ_EFD_Parametros_Ressarcimento ICMSST_Ajustes_e_Lancamentos.docx






THOMSON REUTERS

Módulo Sped Fiscal

Manutenção dos Parâmetros p/a Geração de Ajustes e Lançamentos Complementares referente ao Ressarcimento ICMS-ST MG


Localização: Menu Sped, Módulo: Escrituração Fiscal Digital à Parâmetros à Ressarcimento ICMS-ST à Parâmetros p/ Geração dos Ajustes e Lançamentos


DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
3.	Regras de Funcionamento dos Campos	3


























## Regras Gerais



Os dados parametrizados neste item são utilizados na rotina de pré-geração do Ressarcimento ICMS-ST MG, realizada no menu “Pré-Geração à Ressarcimento ICMS-ST (Específico MG).

Estas informações servem para a geração dos ajustes (C195/C197) e lançamentos complementares da Apuração do ICMS-ST, a partir dos valores apurados para o registro C181 de acordo com as orientações do Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo.

A definição dessa tela está voltada apenas para o atendimento do ressarcimento de MG.  Caso no futuro, venhamos a desenvolver um ressarcimento de outra UF dentro do módulo Sped Fiscal, esta janela não será aproveitada.

Tabela para armazenar a parametrização: EFD_PAR_RESSARC_MG


## Layout da Tela


Estabelecimento: [ xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx ]

Parâmetros para Geração dos Ajustes (C195/C197) -----------------------------------------------------------------------------------------------------------------------------
Estorno de Restituição/Ressarcimento de ICMS-ST
Cód Observação (C195):                                                                                      [grupo] [pastinha] [cod ] [ descrição ]
Cód Ajuste p/ Estorno de Restituição/Ressarcimento de ICMS-ST +FEM (C197)            [pastinha] [cod ] [ descrição              ]
Cód Ajuste p/ Estorno do FEM adicionado ao ICMS-ST (C197)                                       [pastinha] [cod ] [ descrição              ]
Cód Ajuste Informativo FEM adicionado ao ICMS-ST (C197)                                           [pastinha] [cod ] [ descrição              ]
Estorno de Complemento de ICMS-ST
Cód Observação (C195):                                                                                      [grupo] [pastinha] [cod ] [ descrição  ]
Cód Ajuste p/ Estorno do Complemento de ICMS-ST (C197)                                          [pastinha] [cod ] [ descrição               ]
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Parâmetros para Geração dos Lançamentos da Apuração do ICMS-ST ----------------------------------------------------------------------------------------------------
Lançamento de Estorno de Restituição/Ressarcimento de ICMS-ST +FEM:
Item da Apuração                                                                                                  [cod ] [ descrição              ]
Descrição do Lançamento                                                                                     [ descrição                       ]
Classe de Lançamento                                                                         [pastinha] [cod ] [ descrição              ]
Lançamento de Estorno do FEM adicionado ao ICMS-ST
Item da Apuração                                                                                                  [cod ] [ descrição              ]
Descrição do Lançamento                                                                                     [ descrição                       ]
Lançamento de Estorno do Complemento de ICMS-ST
Item da Apuração                                                                                                 [cod ] [ descrição              ]
Descrição do Lançamento                                                                                    [ descrição                       ]

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





Botões da barra de menu:



Na abertura da tela, será verificado se foi informado estabelecimento no login do Manager.

Caso seja informado estabelecimento de login, e este não esteja cadastrado com UF = MG, então exibir a mensagem abaixo, e não abrir a tela de Parâmetros p/ Geração dos Ajustes e Lançamentos:
Este estabelecimento não pertence a Minas Gerais.

Caso contrário, o sistema segue para a abertura da janela da opção “GRUPO” (vide barra de menu), obrigando o usuário a selecionar o grupo desejado. Os critérios para exibição dos grupos serão os mesmos descritos acima. O Grupo selecionado será exibido nos campos “Cód. Observação (C195)”, referentes ao “Estorno de Restituição/Ressarcimento de ICMS-ST” e ao “Estorno de Complemento de ICMS-ST”.


## Regras de Funcionamento dos Campos






Parâmetros para geração dos ajustes (C195/C197):


– Estorno de Restituição/Ressarcimento de ICMS-ST:







– Estorno de Complemento de ICMS-ST:






Parâmetros para Geração dos Lançamentos da Apuração do ICMS-ST:


– Lançamento de Estorno de Restituição/Ressarcimento de ICMS-ST +FEM:





– Lançamento de Estorno do FEM adicionado ao ICMS-ST:






– Lançamento de Estorno do Complemento de ICMS-ST:










= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS67658 | Liliane Assaf | Criação da parametrização para geração dos registros C195/C197 e lançamentos complementares na Apuração do ICMS-ST – Ressarcimento ICMS-ST MG | 27/07/2021 |
| MFS560863 | Liliane Assaf | Ajustes e lançamentos relacionados ao FEM deixam de ser obrigatórios | 24/08/2023 |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


| GRUPO | Ao clicar nesta opção será aberta a janela de seleção dos grupos de relacionamento (relacionamento Tabela x Grupos), e o usuário poderá selecionar o grupo desejado. Caso o usuário tenha informado um estabelecimento no login, serão disponibilizados apenas os grupos relacionados ao estabelecimento em questão, caso contrário, serão exibidos os grupos de todos os estabelecimentos da empresa cadastrados para UF = MG.    O Grupo selecionado será exibido nos campos “Cód. Observação (C195)”, referentes ao “Estorno de Restituição/Ressarcimento de ICMS-ST” e ao “Estorno de Complemento de ICMS-ST”. |
| --- | --- |
| NOVO | Ao clicar nesta opção, as informações dos campos serão limpas e o usuário poderá incluir um novo registro. |
| ABRE | Ao clicar nesta opção, será aberta a janela para seleção das parametrizações já cadastradas para consulta ou manutenção. |
| EXCLUI | Esta opção permite a exclusão da parametrização do estabelecimento em questão. |
| CONFIRMA | Opção para salvar as informações incluídas ou alteradas. |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | N |  | Nesse campo será exibido o código e a razão social do estabelecimento do Grupo selecionado pelo usuário na abertura da tela, ou através da opção “GRUPO” da barra de menu.  Campo se mantém desabilitado. |  |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados. Serão demonstrados para replicação todos os estabelecimentos da mesma empresa e UF do estabelecimento parametrizado. |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Cód. Observação (C195) | Alfanumérico | S | S |  | Este campo trabalha com janela de seleção da Tabela de Cadastro de Observações (*). Serão disponibilizados para seleção apenas as observações do Grupo selecionado pelo usuário na abertura da tela.  Campo de preenchimento obrigatório.  Ao salvar o registro realizar as validações: Se não estiver preenchido, exibir a mensagem: “Cód. Observação (c195) do Estorno de Restituição/Ressarcimento de ICMS-ST deve ser preenchido.” Se for um código não cadastrado, exibir a mensagem: “Cód. Observação (c195) do Estorno de Restituição/Ressarcimento de ICMS-ST não cadastrado.”  (*) Módulo DW, menu  “Manutenção à Códigos àCadastro de Observações” (SAFX2009); Tabela: X2009_OBSERVACAO |  |
| Cód. Ajuste p/ Estorno de Restituição/Ressarcimento de ICMS-ST +FEM (C197) | Alfanumérico | S | S |  | Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste Provenientes de Documentos Fiscais (*)  Serão disponibilizados para seleção apenas os códigos que iniciem com a seguinte formação: - Dois primeiros caracteres = UF do estabelecimento em questão; - terceiro caracter = “4” (=Outros Débitos); - quarto caracter = “1” (=Apuração do ICMS-ST), considerando apenas os códigos. Ex: MG41000016.  Campo de preenchimento obrigatório.  Ao salvar o registro realizar as validações: Se não estiver preenchido, exibir a mensagem: “Cód. Ajuste p/ Estorno de Restituição/Ressarcimento de ICMS-ST +FEM (C197) deve ser preenchido.” Se for um código não cadastrado, ou que não atenda a regra de formação acima especificada, exibir a mensagem: “Cód. Ajuste p/ Estorno de Restituição/Ressarcimento de ICMS-ST +FEM (C197) inválido não cadastrado.”  (*) Módulo DW, menu “Manutenção à Cadastros à Códigos de Ajuste provenientes de NF’s (Sped Fiscal)”; Tabela: DWT_COD_AJUSTE_SPED |  |
| Cód. Ajuste p/ Estorno do FEM adicionado ao ICMS-ST (C197) | Alfanumérico | S | S |  | Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste Provenientes de Documentos Fiscais (*)  Serão disponibilizados para seleção apenas os códigos que iniciem com a seguinte formação: - Dois primeiros caracteres = UF do estabelecimento em questão; - terceiro caracter = “2” (=Estorno Débitos); - quarto caracter = “1” (=Apuração do ICMS-ST), considerando apenas os códigos. Ex: MG21000018. MFS560863: Campo deixou de ser obrigatório Campo de preenchimento obrigatório.  Ao salvar o registro realizar as validações: Se não estiver preenchido, exibir a mensagem: “Cód. Ajuste p/ Estorno do FEM adicionado ao ICMS-ST (C197) deve ser preenchido.” Se for um código não cadastrado, ou que não atenda a regra de formação acima especificada, exibir a mensagem: “Cód. Ajuste p/ Estorno do FEM adicionado ao ICMS-ST (C197) inválido não cadastrado.”  (*) Módulo DW, menu “Manutenção à Cadastros à Códigos de Ajuste provenientes de NF’s (Sped Fiscal)”; Tabela: DWT_COD_AJUSTE_SPED |  |
| Cód. Ajuste Informativo FEM adicionado ao ICMS-ST (C197) | Alfanumérico | S | S |  | Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste Provenientes de Documentos Fiscais (*)  Serão disponibilizados para seleção apenas os códigos que iniciem com a seguinte formação: - Dois primeiros caracteres = UF do estabelecimento em questão; - terceiro caracter = “9” (=Informativo); - quarto caracter = “1” (=Apuração do ICMS-ST), considerando apenas os códigos. Ex: MG91000018. MFS560863: Campo deixou de ser obrigatório Campo de preenchimento obrigatório.  Ao salvar o registro realizar as validações: Se não estiver preenchido, exibir a mensagem: “Cód. Ajuste Informativo FEM adicionado ao ICMS-ST (C197) deve ser preenchido.” Se for um código não cadastrado, ou que não atenda a regra de formação acima especificada, exibir a mensagem: “Cód. Ajuste Informativo FEM adicionado ao ICMS-ST (C197) inválido não cadastrado.”  (*) Módulo DW, menu “Manutenção à Cadastros à Códigos de Ajuste provenientes de NF’s (Sped Fiscal)”; Tabela: DWT_COD_AJUSTE_SPED |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Cód. Observação (C195) | Alfanumérico | S | S |  | Este campo trabalha com janela de seleção da Tabela de Cadastro de Observações (*). Serão disponibilizados para seleção apenas as observações do Grupo selecionado pelo usuário na abertura da tela.  Campo de preenchimento obrigatório.  Ao salvar o registro realizar as validações: Se não estiver preenchido, exibir a mensagem: “Cód. Observação (c195) do Estorno de Complemento de ICMS-ST deve ser preenchido.” Se for um código não cadastrado, exibir a mensagem: “Cód. Observação (c195) do Estorno de Complemento de ICMS-ST não cadastrado.” Se o código de observação preenchido nesse campo for igual ao informado no campo Cód Observação para Estorno de Restituição/Ressarcimento de ICMS-ST, exibir a mensagem: “Códigos de Observações informados para Estornos de Restituição/Ressarcimento de ICMS-ST e de Complemento ICMS-ST devem ser distintos.”  (*) Módulo DW, menu  “Manutenção à Códigos àCadastro de Observações” (SAFX2009); Tabela: X2009_OBSERVACAO |  |
| Cód. Ajuste p/ Estorno do Complemento de ICMS-ST (C197) | Alfanumérico | S | S |  | Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste Provenientes de Documentos Fiscais (*)  Serão disponibilizados para seleção apenas os códigos que iniciem com a seguinte formação: - Dois primeiros caracteres = UF do estabelecimento em questão; - terceiro caracter = “1” (=Outros Créditos); - quarto caracter = “1” (=Apuração do ICMS-ST), considerando apenas os códigos. Ex: MG11000016.  Campo de preenchimento obrigatório.  Ao salvar o registro realizar as validações: Se não estiver preenchido, exibir a mensagem: “Cód. Ajuste p/ Estorno de Complemento de ICMS-ST (C197) deve ser preenchido.” Se for um código não cadastrado, ou que não atenda a regra de formação acima especificada, exibir a mensagem: “Cód. Ajuste p/ Estorno de Complemento de ICMS-ST (C197) inválido ou não cadastrado.”  (*) Módulo DW, menu “Manutenção à Cadastros à Códigos de Ajuste provenientes de NF’s (Sped Fiscal)”; Tabela: DWT_COD_AJUSTE_SPED |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Item da Apuração | Alfanumérico | S | N | Código + Descrição  Default: 002 | Este campo tem como origem o Cadastro de Operações da Apuração – tabela OPERACAO_APURACAO (TFIX18).  Apresentar o Código e a Descrição relacionada à operação “002”, cadastrada na tabela OPERACAO_APURACAO considerando o livro 108. Com isso, no campo será apresentado a seguinte informação:   Manter o campo desabilitado.  Futuramente, caso a legislação determine outro código de operação para realização do lançamento, basta habilitarmos este campo para que o usuário possa selecionar o código da operação adequado. |  |
| Descrição do Lançamento | Alfanumérico | S | S |  | Neste campo será informada a descrição do lançamento (tamanho: 150 caracteres, conforme tabela dos lançamentos complementares, ITEM_APURAC_SUBST).  Ao salvar o registro realizar as validações: Se não estiver preenchido, exibir a mensagem: “Descrição do Lançamento de Estorno de Restituição/Ressarcimento de ICMS-ST +FEM deve ser preenchido.” |  |
| Classe de Lançamento | Alfanumérico | N | S | Pastinha + cod + descrição | Este campo trabalha com janela de seleção da Tabela de Classes de Lançamento por UF (*), considerando apenas as classes da UF do estabelecimento em questão. (Ex: classe 980 usada na DAPI)  (*) Módulo Ferramentas, menu “Tabelas Internas à Manter àClasses por UF”; Tabela: PRT_CLASSE_UF_MSAF  OBS: Foi criado o campo classe de lançamento, pois o módulo da DAPI gera o campo 77.1 da DAPI através da recuperação do lançamento da Apuração do ICMS-ST com classe 980. Segundo o Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo, o valor desse estorno deve ser apresentado no campo 77.1 da DAPI. Parametrizando a classe 980 o valor gerado no lançamento, automaticamente será gerado no campo 77.1 da DAPI. |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Item da Apuração | Alfanumérico | S | N | Código + Descrição  Default: 007 | Este campo tem como origem o Cadastro de Operações da Apuração – tabela OPERACAO_APURACAO (TFIX18).  Apresentar o Código e a Descrição relacionada à operação “007”, cadastrada na tabela OPERACAO_APURACAO considerando o livro 108. Com isso, no campo será apresentado a seguinte informação:   Manter o campo desabilitado.  Futuramente, caso a legislação determine outro código de operação para realização do lançamento, basta habilitarmos este campo para que o usuário possa selecionar o código da operação adequado. |  |
| Descrição do Lançamento | Alfanumérico | S | S |  | Neste campo será informada a descrição do lançamento (tamanho: 150 caracteres, conforme tabela dos lançamentos complementares, ITEM_APURAC_SUBST). MFS560863: Campo deixou de ser obrigatório Ao salvar o registro realizar as validações: Se não estiver preenchido, exibir a mensagem: “Descrição do Lançamento de Estorno do FEM adicionado ao ICMS-ST deve ser preenchido.” |  |
| Obs: não foi criada classe de lançamento, pois o módulo da DAPI gera o campo 82.1 da DAPI através da leitura dos ajustes de lançamentos fiscais (SAFX113). Não recupera o valor desse lançamento da apuração do ICMS-ST. Segundo o Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo, o valor desse estorno deve ser apresentado no campo 82.1 da DAPI. | Obs: não foi criada classe de lançamento, pois o módulo da DAPI gera o campo 82.1 da DAPI através da leitura dos ajustes de lançamentos fiscais (SAFX113). Não recupera o valor desse lançamento da apuração do ICMS-ST. Segundo o Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo, o valor desse estorno deve ser apresentado no campo 82.1 da DAPI. | Obs: não foi criada classe de lançamento, pois o módulo da DAPI gera o campo 82.1 da DAPI através da leitura dos ajustes de lançamentos fiscais (SAFX113). Não recupera o valor desse lançamento da apuração do ICMS-ST. Segundo o Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo, o valor desse estorno deve ser apresentado no campo 82.1 da DAPI. | Obs: não foi criada classe de lançamento, pois o módulo da DAPI gera o campo 82.1 da DAPI através da leitura dos ajustes de lançamentos fiscais (SAFX113). Não recupera o valor desse lançamento da apuração do ICMS-ST. Segundo o Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo, o valor desse estorno deve ser apresentado no campo 82.1 da DAPI. | Obs: não foi criada classe de lançamento, pois o módulo da DAPI gera o campo 82.1 da DAPI através da leitura dos ajustes de lançamentos fiscais (SAFX113). Não recupera o valor desse lançamento da apuração do ICMS-ST. Segundo o Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo, o valor desse estorno deve ser apresentado no campo 82.1 da DAPI. | Obs: não foi criada classe de lançamento, pois o módulo da DAPI gera o campo 82.1 da DAPI através da leitura dos ajustes de lançamentos fiscais (SAFX113). Não recupera o valor desse lançamento da apuração do ICMS-ST. Segundo o Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo, o valor desse estorno deve ser apresentado no campo 82.1 da DAPI. |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Item da Apuração | Alfanumérico | S | N | Código + Descrição  Default: 006 | Este campo tem como origem o Cadastro de Operações da Apuração – tabela OPERACAO_APURACAO (TFIX18).  Apresentar o Código e a Descrição relacionada à operação “006”, cadastrada na tabela OPERACAO_APURACAO considerando o livro 108. Com isso, no campo será apresentado a seguinte informação:   Manter o campo desabilitado.  Futuramente, caso a legislação determine outro código de operação para realização do lançamento, basta habilitarmos este campo para que o usuário possa selecionar o código da operação adequado. |  |
| Descrição do Lançamento | Alfanumérico | S | S |  | Neste campo será informada a descrição do lançamento (tamanho: 150 caracteres, conforme tabela dos lançamentos complementares, ITEM_APURAC_SUBST).  Ao salvar o registro realizar as validações: Se não estiver preenchido, exibir a mensagem: “Descrição do Lançamento de Estorno do Complemento de ICMS-ST deve ser preenchido.” |  |
| Obs: não foi criada classe de lançamento, pois o módulo da DAPI gera o campo 80 da DAPI através da leitura dos documentos fiscais de devolução. Não recupera o valor desse lançamento da apuração do ICMS-ST. Segundo o Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo, o valor desse estorno deve ser apresentado no campo 80 da DAPI. | Obs: não foi criada classe de lançamento, pois o módulo da DAPI gera o campo 80 da DAPI através da leitura dos documentos fiscais de devolução. Não recupera o valor desse lançamento da apuração do ICMS-ST. Segundo o Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo, o valor desse estorno deve ser apresentado no campo 80 da DAPI. | Obs: não foi criada classe de lançamento, pois o módulo da DAPI gera o campo 80 da DAPI através da leitura dos documentos fiscais de devolução. Não recupera o valor desse lançamento da apuração do ICMS-ST. Segundo o Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo, o valor desse estorno deve ser apresentado no campo 80 da DAPI. | Obs: não foi criada classe de lançamento, pois o módulo da DAPI gera o campo 80 da DAPI através da leitura dos documentos fiscais de devolução. Não recupera o valor desse lançamento da apuração do ICMS-ST. Segundo o Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo, o valor desse estorno deve ser apresentado no campo 80 da DAPI. | Obs: não foi criada classe de lançamento, pois o módulo da DAPI gera o campo 80 da DAPI através da leitura dos documentos fiscais de devolução. Não recupera o valor desse lançamento da apuração do ICMS-ST. Segundo o Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo, o valor desse estorno deve ser apresentado no campo 80 da DAPI. | Obs: não foi criada classe de lançamento, pois o módulo da DAPI gera o campo 80 da DAPI através da leitura dos documentos fiscais de devolução. Não recupera o valor desse lançamento da apuração do ICMS-ST. Segundo o Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo, o valor desse estorno deve ser apresentado no campo 80 da DAPI. |  |

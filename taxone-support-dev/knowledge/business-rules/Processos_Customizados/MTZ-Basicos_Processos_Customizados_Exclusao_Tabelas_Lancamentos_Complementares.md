---
source: "MTZ-Basicos_Processos Customizados_Exclusao_Tabelas_Lançamentos Complementares.docx"
category: Processos_Customizados
converted: auto
---

# Processo Customizado – Exclusão de Tabelas Lançamentos Complementares


DOCUMENTO DE REQUISITO


## REGRAS DE NEGÓCIO

Localização: Menu Básico, módulo Processos Customizados



---

| DR | Nome | Descrição |
| --- | --- | --- |
| OS3431 | Limpeza das Tabelas Definitivas X216, X217, X218, X219 e X220. | O objetivo dessa demanda é criar um processo customizado que possibilite a exclusão dos Lançamentos Complementares. |


---

| Cód. | Descrição | DR |
| --- | --- | --- |
|  | Objetivo do Framework  Este documento tem por finalidade especificar o processo customizado referente à exclusão das tabelas de Lançamentos Complementares para o Livro 108. Devido diversos problemas de performance e “quedas no serviço” decorrente a alta utilização da tela de manutenção dos Lançamentos Complementares, (ICMS Normal), a tela foi retirada do Tax One. A implementação da nova tela de Lançamentos Complementares está em fase de Estudo. Enquanto isso, para mitigar possíveis problemas (pela falta da tela), será liberado um processo customizado possibilitando ao usuário excluir os lançamentos complementares para efetuar posteriormente a importação das tabelas SAFX216, SAFX217, SAFX218, SAFX219 e SAFX220, à princípio esse processo será implementado, somente, para o ICMS-Normal (Livro 108).  Obs.: Os lançamentos referentes ao ICMS-ST e IPI não serão considerados, pois o usuário poderá efetuar a manutenção via tela de Manutenção. Mas poderão ser incluídos posteriormente. |  |
|  | Regras Gerais – Aba Parâmetros:  Criar tela do tipo “Framework”, conforme Regras Abaixo:  A tela do processo customizado deverá ter os  campos que serão utilizados como filtro para seleção dos registros das tabelas de Lançamentos Complementares para exclusão:    Período: Esse campo deve ser um textbox e deve permitir a digitação da data do Período para a limpeza. Formato: MM/AAAA.    - Recuperar o campo de ‘DAT_APURACAO’ da tabela ‘ITEM_APURAC_DISCR’ Campo obrigatório.  Somente Listar: Esse campo deve ser um checktbox, que se marcado permitirá ao usuário gerar um relatório com a listagem dos registros existentes nas tabelas de Lançamentos Complementares.  Listar e Excluir: Esse campo deve ser um checktbox, que se marcado, será executado a rotina de exclusão e será apresentado um relatório com a listagem dos registros excluídos das tabelas de Lançamentos Complementares.  Estabelecimento: Listar os estabelecimentos relacionados a empresa de login.    - Recuperar o campo ‘COD_ESTAB’ da tabela ‘ITEM_APURAC_DISCR’ Campo obrigatório.  O processo customizado deverá ser liberado na solução Tax One >> Módulo ‘Processos Customizados’ |  |
|  | Funcionamento (Regra Principal):   No início do processo, serão feitas as consistências:  Verificação se pelo menos um estabelecimento foi selecionado Verificação se campo de Período está preenchido. O processo customizado deverá excluir somente o Tipo de Livro igual à 108 (ICMS-Normal)  Caso todos esses critérios estejam válidos, a rotina dá início ao processo de exclusão das seguintes tabelas:    ITEM_APURAC_DISCR (SAFX216) ITEM_APURAC_DISCR_PROC (SAFX217) ITEM_APURAC_DISCR_AJUSTE (SAFX218) ITEM_APURAC_DISCR_X113 (SAFX219) ITEM_APURAC_DISCR_DAPI (SAFX220) |  |
|  | Log,  Caso o campo de Período não esteja preenchido, exibir a seguinte mensagem: Informe o Período  Caso nenhum estabelecimento seja selecionado, exibir a seguinte mensagem: Selecione pelo menos um estabelecimento. |  |
|  | Aba Relatório de Conferência  Caso a opção “ Somente Listar” esteja marcado, então:  O relatório deverá listar todos os Registros de Lançamentos Complementares, apresentando as seguintes colunas:  Empresa                             Estabelecimento Período Tipo de Livro Código de Operação Nº Discriminação Valor do Item  Caso a opção “Listar e Excluir” esteja marcado, o processo customizado executará a rotina de exclusão e deverá apresentar a listagem dos Lançamentos Complementares, conforme as seguintes colunas:  Empresa                             Estabelecimento Período Tipo de Livro Código de Operação Nº Discriminação Valor do Item |  |

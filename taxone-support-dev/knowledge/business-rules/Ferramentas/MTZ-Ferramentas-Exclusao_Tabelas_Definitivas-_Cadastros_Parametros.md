---
source: "MTZ-Ferramentas-Exclusao_Tabelas_Definitivas- Cadastros Parâmetros.doc"
category: Ferramentas
converted: auto
---

Ferramentas - Rotinas Acessórias - Inicialização - Exclusão de Tabelas Definitivas - Cadastros Parâmetros


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
MFS74955
Criar processo de limpeza de tabelas de Cadastro de Parâmetros relacionadas a SAFX
Inclusão das tabelas definitivas de cadastros de parâmetros, relacionadas a SAFX, quando: 
- Parâmetros com código de estabelecimento; 
- Parâmetros que não possuam campo de data.
MFS-573179
Inclusão da tabela SAFX2117
Inclusão da tabela SAFX2117. 

REGRAS DE NEGÓCIO

Localização: Menu Básico, módulo Ferramentas, menu Rotinas Acessórias --> Inicialização --> Exclusão de Tabelas Definitivas --> Cadastros Parâmetros


Cód.
Descrição
DR
RN00
Regras Gerais

Criar tela do tipo FrameWork, com as abas Parâmetros, Processo, Log e Relatório de Conferência.

Esta rotina tem como objetivo realizar a remoção dos registros de uma tabela de cadastro de parâmetros. 

Pré-Requisito:

Para o correto funcionamento, as seguintes TFIX devem ser importadas:
* TFIX11- Catálogo Prioridade de Importação (Tabela CAT_PRIOR_IMP)
* TFIX96 - Tabela com o layout da carga para tabelas SAFX, conforme manual de layout. (Tabela CAT_LAYOUT_IMP)

As tabelas disponíveis para exclusão são:
- Tabelas de Cadastro importadas por SAFX, que contenham campo código do estabelecimento e que NÃO contenham um campo de Data, a ser utilizado como filtro, ou seja, a exclusão será em massa por Estabelecimento;

As tabelas de Cadastro de Parâmetros que contenham código do estabelecimento e sem Data, serão excluídas na opção de menu: Exclusão de Tabelas Definitivas --> Cadastros Parâmetros.

MFS74955
RN01
Aba Parâmetros:

Nesta tela, serão disponibilizados os seguintes campos necessários para a execução da limpeza:

Estabelecimento:

Listar os estabelecimentos relacionados a empresa de login.
Campo obrigatório.

Campo Limpar também os dados de TABELAS VINCULADAS à tabela selecionada?

Esta opção possibilita que registros do Cadastro Referenciados por outras tabelas, possam ser excluídos. 
Caso a opção seja selecionada, tanto os registros do cadastro quanto os registros que o referenciam serão excluídos.
Caso contrário, os registros do cadastro que sejam referenciados por outras tabelas, não serão excluídos. 

Campo Nome Tabela

Esse campo deve exibir as tabelas de cadastro de Parâmetros habilitadas para exclusão.
A lista deve ser disponibilizada em tela, conforme tabelas abaixo: 
- SAFX146; -SAFX156;- SAFX199;- SAFX200;- SAFX2050;- SAFX2089;- SAFX2093;- SAFX2099;- SAFX2108;- SAFX2109/SAFX2112;- SAFX2110;- SAFX2111; - SAFX215;- SAFX45.
campo obrigatório.(*) Tabelas de cadastro relacionadas à SAFX, que contenham campo Código do Estabelecimento em sua estrutura, estão disponíveis para exclusão na opção de menu Exclusão de Tabelas Definitivas --> Cadastros Parâmetros.
Obs.: Será realizado a manutenção do campo DATA_REF_TAB_DEF da tabela CAT_PRIOR_IMP (TFIX11) para as tabelas SAFX que possuem data, porém está com o campo "DATA_REF_TAB_DEF" sem preenchimento;

Campo Limpar também os dados de TABELAS VINCULADAS à tabela selecionada?

Esta opção possibilita que registros do Cadastro Referenciados por outras tabelas, possam ser excluídos. 
Caso a opção seja selecionada, tanto os registros do cadastro quanto os registros que o referenciam serão excluídos.
Caso contrário, os registros do cadastro que sejam referenciados por outras tabelas, não serão excluídos. 


MFS74955
RN02
Funcionamento (Regra Principal): 

- Verificação se pelo menos um estabelecimento foi selecionado.
- Verificação se Quantidade de Registros a serem excluídos na tabela indicada no campo "Nome Tabela" não ultrapassa o limite de 100mil registros.
- Nesse processo a exclusão será em massa, conforme seleção de um ou mais Estabelecimentos ou "TODOS". 


Relação das Tabelas SAFX de Cadastro de Parâmetros que serão excluídas:

Conjunto de tabelas que serão excluídas nos itens de menu Exclusão de Tabelas Definitivas --> Movimentos e Exclusão de Tabelas Definitivas --> Cadastros Parâmetros.

NOM_TAB_WORK (Temporária)
NOM_TAB_DEF (Definitiva)
SAFX156	        
X156_CAD_INSC_MUN
SAFX199	        
EST_DIA_AM_PAR_PROD
SAFX200	        
EST_DIA_AM_PAR_PROD_IES
SAFX215	        
EST_DIA_AM_PROD_ACAB_IES
SAFX2108	
PRT_ID_TIPO_SERV_ESOCIAL
SAFX2109 / SAFX2112	
PRT_SERV_MSAF
SAFX2110	
PRT_OPER_MSAF
SAFX2111	
PRT_NBM_ATIV_CONT_PREV
SAFX146	        
PRT_PROD_MSAF  
SAFX2050	
ICT_AM_LINHAP_PRD
SAFX45	        
PRT_PFJ_MSAF
SAFX2089	
DIPI_BEB_PAUTA_PRD
SAFX2093	
X2093_ARV_PRD_DRBK
SAFX2099	
X2099_EQUIPAMENTO
SAFX2117*
PRT_IDENTIFICA_NAT_REND

[ALTERAÇÃO MFS-573179] (*) A tabela não possui empresa e estabelecimento. Como na tela o estabelecimento é de preenchimento obrigatório, qualquer estabelecimento selecionado excluirá os dados existentes na tabela definitiva.
MFS74955
MFS573179
RN03
Tratamento para Registros Vinculados:

Durante a exclusão dos registros da tabela especificada no campo "Nome Tabela", podem ser encontrados registros de outras tabelas referenciando os registros a serem excluídos.  Nesta situação, o tratamento varia de acordo com o campo "Limpar também os dados de TABELAS VINCULADAS à tabela selecionada?".

Caso a opção "Limpar também os dados de TABELAS VINCULADAS à tabela selecionada?" esteja marcada, então:

Serão excluídos os registros:
* Os registros da tabela principal, especificada no campo "Nome Tabela";
* Os registros de outras tabelas que referenciam os registros excluídos da tabela especificada no campo "Nome Tabela";
Neste caso, no Relatório de Conferência, será demonstrada a quantidade de registros excluídos tanto da tabela principal quanto das referenciadas (ditas vinculadas).

Caso a opção "Limpar também os dados de TABELAS VINCULADAS à tabela selecionada?" esteja desmarcada, então:

* Serão excluídos apenas os registros da tabela principal, especificada no campo "Nome Tabela", que não sejam referenciados por nenhuma outra tabela.

Caso seja encontrado um registro de outra tabela que referencie um registro a ser excluídos da tabela principal, o processo de exclusão será interrompido, e será exibido a seguinte mensagem no log:
        Erro: Violação de Integridade de dados na tentativa de excluir registro da tabela XXXXXXX
        Dados do Registro:  Apresentar os campos de identificação do registro que não pode ser excluído.
        Mensagem de Banco: Apresentar o nome da FK e o nome da tabela vinculada, onde foram encontrados registros com referencia para o principal.
MFS74955
RN04
Log

Caso existam mais de 100mil registros na tabela principal, especificada no campo "Nome Tabela", exibir a seguinte mensagem:
Foram selecionados mais de 100.000 registros para exclusão, execute o processo por Estabelecimento para reduzir o escopo.

Caso o usuário da aplicação não tenha acesso a tabelas de cadastro do banco de dados Oracle como USER_TAB_COLUMNS, exibir a seguinte mensagem:
O usuário da aplicação não consegue acessar tabelas de catálogos do BD Oracle. Exemplo: User_Tab_Columns. Consulte o DBA.


RN05
Relatório de Conferência

Caso a opção "Limpar também os dados de TABELAS VINCULADAS à tabela selecionada?" esteja marcada, então:
O relatório deve apresentar as seguintes colunas:
Tabela:                            tabela principal, especificada no campo "Nome Tabela",
Qtd Registros Lidos:        quantidade de registros da tabela principal, especificada no campo "Nome Tabela",
Qtd Registros Excluídos: quantidade de registros excluídos da tabela principal, especificada no campo "Nome Tabela",
Tabela Vinculada:            Nome da tabela que faz referência à tabela Principal
Qtd. Reg. Vinculados:      quantidade de registros excluídos da tabela Vinculada, por referenciarem a registros da tabela principal.

Caso a opção "Limpar também os dados de TABELAS VINCULADAS à tabela selecionada?" esteja desmarcada, então:
O relatório deve apresentar as seguintes colunas:
Tabela:                            tabela principal, especificada no campo "Nome Tabela",
Qtd Registros Lidos:        quantidade de registros da tabela principal, especificada no campo "Nome Tabela",
Qtd Registros Excluídos: quantidade de registros excluídos da tabela principal, especificada no campo "Nome Tabela",
Caso existam registros referenciados por outras tabelas, a quantidade demonstrada em "Qtd Registros Excluídos" será menor que a "Qtd Registros Lidos".  No log de erro será possível identificar os registros que não foram excluídos e por quais tabelas eles estavam sendo referenciados.

MFS74955
RN06
Não está sendo atendido pela MFS-74955:

- Tabelas que possuem campo de Data na tabela definitiva, não serão consideradas na exclusão.
- Tabelas que não possuem o campo de Código de Estabelecimento. 
- Veja planilha com o conjunto de tabelas que não estão sendo excluídas nos itens de menu Exclusão de Tabelas Definitivas --> Movimentos e Exclusão de Tabelas Definitivas --> Cadastros Parâmetros.


Obs.: As tabelas SAFX relacionadas na planilha "Tabelas_Fora_Escopo_Cadastros Parâmetros" serão reavaliadas posteriormente, conforme particularidades descritos na Aba "Detalhes".
MFS74955



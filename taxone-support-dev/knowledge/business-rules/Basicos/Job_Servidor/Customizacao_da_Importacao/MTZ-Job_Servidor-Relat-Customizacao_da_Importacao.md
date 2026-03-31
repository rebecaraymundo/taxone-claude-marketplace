# MTZ-Job Servidor-Relat-Customizacao da Importacao

- **Fonte:** MTZ-Job Servidor-Relat-Customizacao da Importacao.docx
- **Modificado:** 2022-03-07
- **Tamanho:** 69 KB

---

THOMSON REUTERS

                                                                                     __Módulo Job Servidor__

__  __

__Relatório das Regras de Customização para Importação__

__Localização__: Menu Básicos, Módulo Job Servidor, item Importação 🡪 Customização da Importação 🡪 Relatório das Regras para Importação

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS35770

Andréa Rocha

Este documento tem como objetivo criar o relatório das Regras para Importação

09/07/2020

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

Seu objetivo é um relatório para a conferência das Regras de Customização para Importação, que será gerado em formato XLS\.

As regras de Customização para Importação são definidas no menu \(Importação <a id="OLE_LINK28"></a><a id="OLE_LINK32"></a>🡪 Customização da Importação 🡪 Regras para Importação\) e gravadas na Tabela de Cadastro das Regras \(CAD\_IMP\_REGRA\)\.

__RN01__

__                                                        Parâmetros de Tela__

__Tabelas __– Quadro das tabelas SAFX’s cadastradas, com as opções de selecionar uma tabela e marcar/desmarcar todas as tabelas\.  Serão demonstradas todas as tabelas SAFX’s cadastradas na tabela de Catálogo Prioridade de Importação \(TFIX11\), ordenadas pelo código da SAFX \(campo NOM\_TAB\_WORK\)\.  Serão demostrados o código da SAFX \(campo NOM\_TAB\_WORK\) e sua descrição \(campo DESCRICAO\_ARQUIVO\) para a seleção\.

__Exibir apenas campos com regra__ –__ __Campo do tipo checkbox, default desabilitado\.

__RN02__

__                                                        Layout de Tela__

          Tabelas                                                                                                                                 Selecionar        Marcar Todas          

\[\] SAFX01   Lançamentos Contábeis

\[\] SAFX02   Saldos Mensais

\[\] SAFX03   Arquivo de Contas a Pagar

         \[\] Exibir apenas campos com regra       

__RN03__

__                                                    Recuperação dos Dados__

__Origem dos dados__: Tabela de Cadastro das Regras \(CAD\_IMP\_REGRA\), tabela de Catálogo Prioridade de Importação \(TFIX11\) e tabela de layout das tabelas SAFX \(TFIX96\)\.

Critérios de recuperação:

     \- NOM\_TAB\_WORK – código da SAFX selecionada em tela\.

__RN04__

__                                                         Processamento __

Os dados serão recuperados da tabela de Cadastro das Regras, tabela de Catálogo Prioridade de Importação e da tabela de layout das tabelas SAFX, e serão demonstrados de acordo com o parâmetro “Exibir apenas campos com regra”\. 

Se parâmetro “Exibir apenas campos com regra” estiver marcado

     Serão mostrados no relatório somente os campos \(NOME\_CAMPO\) que estiverem na tabela de Cadastro das Regras para a 

     SAFX

Senão

     Serão mostrados no relatório todos os campos \(NOME\_CAMPO\) que estiverem na tabela de layout das tabelas SAFX para a 

     SAFX

Os dados serão ordenados por Código da SAFX \(NOM\_TAB\_WORK\) e Número do campo \(NUM\_CAMPO\)\.

__RN05__

__                                                Preenchimento dos Dados __

__Tabela__

Código da SAFX \(NOM\_TAB\_WORK\) da tabela de Cadastro das Regras\.

__Nome__

Descrição da SAFX \(DESCRICAO\_ARQUIVO\) da tabela de Catálogo Prioridade de Importação\.

__Item __

Número do campo \(NUM\_CAMPO\) da tabela de layout das tabelas SAFX\.

__Obrigatório__

Indicador de campo Obrigatório \(IND\_OBRIG\) da tabela de layout das tabelas SAFX\.

__Descrição__

Descrição do campo \(DESCRICAO\) da tabela de layout das tabelas SAFX\.

__Nome Campo__

Nome do campo \(NOME\_CAMPO\) da tabela de Cadastro das Regras\.

__Tamanho__

Tamanho do campo \(TAMANHO\) da tabela de layout das tabelas SAFX\.

__Tipo__

Tipo do campo \(TIPO\) da tabela de layout das tabelas SAFX\.

__Ordem__

Ordem de execução das regras \(NUM\_ORDEM\) da tabela de Cadastro das Regras\.

__Sobrepõe__

Indicador de sobreposição do registro \(IND\_SOBREPOE\) da tabela de Cadastro das Regras\.

__Regra__

Definição da regra de importação \(DSC\_REGRA\) da tabela de Cadastro das Regras\.


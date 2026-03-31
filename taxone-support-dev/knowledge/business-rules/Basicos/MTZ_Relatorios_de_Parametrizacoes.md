# MTZ_Relatórios de Parametrizações

> Fonte: MTZ_Relatórios de Parametrizações.docx






THOMSON REUTERS

Matriz da tela Contabilização

Relatório de Parametrização Contábeis




DOCUMENTO DE REQUISITO


Sumário

1.	INTRODUÇÃO	3
2.	Documento de Referência	3
3.	Fluxo Principal Seleção de dados – Relatório de Parametrização	3
2.3	Prótotipo Relatório Parametrização	5
2.4	Lista de campos:	5
2.5	Exemplos de Relatórios:	8


## INTRODUÇÃO


O objetivo é criar um relatório que reflita os parâmetros configurados na tela de "Parâmetros de Apuração de Ajustes e Outros Lançamentos da Apuração", permitindo que o usuário visualize os parâmetros existentes relacionados às contas contábeis nestes relatórios.

## Documento de Referência


MTZ _Tela Seleção de dados
MTZ _ Tela de Parâmetros Ajustes da Apuração Contábeis
MTZ_Tela de Parâmetros de Outros Lançamentos Contábeis

## Fluxo Principal Seleção de dados – Relatório de Parametrização













Localização da Tela:
- Agrupamentos: Básico
- Módulo: Manutenção >> Contabilização Apuração >>Relatórios de Parametrização
- Menu: Acesso Principal >> Seleção de Dados





## Prótotipo Relatório Parametrização










## Lista de campos:







## Exemplos de Relatórios:


Relatório de Parametrizações Contábeis.xlsx















| OS/CH | Nome | Descrição |
| --- | --- | --- |
| ADO - 797249 | Millys Lopes | Relatório de Parametrização Contábeis |
|  |  |  |


| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | Usuário do sistema |
| Pré- Condições | O usuário deve configurar os parâmetros na tela "Contabilização da Apuração > Parâmetro” |
| Pós-Condições | Após a configuração dos parâmetros, o usuário terá dados para visualizar no Relatório de Parâmetros. |


| Ações do Ator | Ações do Sistema |
| --- | --- |
| Acesso a Tela Seleção de Dados | O usuário acessa a funcionalidade clicando na opção "Relatórios de Parâmetros" no menu do sistema ou interface. |
| Pesquisa de Parametrizações | Após acessar a tela de seleção, o usuário insere os critérios de pesquisa, como o período específico para o qual deseja visualizar os parâmetros. |
| Solicitar a Geração do Relatório | O usuário seleciona a opção de exportar o relatório no formato Excel. |
| Filtros para geração | O sistema permite ao usuário configurar filtros como período, categorias :Tudo, Ajustes da Apuração, Outros Lançamentos da Apuração |
| Confirmar a Geração | O usuário confirma a geração do relatório clicando no botão "Gerar Relatório". |
| Processar os Dados | O sistema realiza a consulta e organiza os dados conforme os critérios definidos. |
| Exportar Relatório | O sistema gera o arquivo no formato Excel (.xlsx) e disponibiliza o download ou salva o arquivo em uma localização definida. |


| Cód. | Campo | Tipo | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- |
| RN00 | EMPRESA | Alfanúmerico | Código Descrição | Exibe o código e a descrição da empresa que foi recuperada. | ADO-797249 |
| RN01 | ESTABELECIMENTO | Alfanúmerico | Código Descrição | Exibe o código e a descrição das filiais para seleção de acordo com a empresa selecionada | ADO-797249 |
| RN02 | UF | Texto | UF | Exibe as UFs dos estabelecimentos ou todas as UFs, conforme a seleção realizada, e recupera os dados correspondentes | ADO-797249 |
| RN03 | GRUPO_IMPOSTO | Dropdown | Texto | Seleciona  todos ou  Federal ou Estadual. | ADO-797249 |
| RN04 | TIPO PARAMETRO | Dropdown | Alfanúmerico | Sistema deve apresentar ao usuário as seguintes opções de seleção: 01 - Todos os Parâmetros: Exibe todas as informações disponíveis, incluindo ajustes da apuração e outros lançamentos contábeis. 02 - Ajustes da Apuração: Exibe apenas os dados relacionados aos ajustes realizados na apuração do período selecionado. 03 - Outros Lançamentos Contábeis: Exibe somente os outros lançamentos contábeis do período selecionado. | ADO-797249 |
| RN05 | IMPOSTO | Texto | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN06 | REFERENCIA | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN07 | LOCAL_NEGÓCIO | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN08 | DIVISAO | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN09 | CENTRO | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN10 | TIPO_PARAMETRO | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro | ADO-797249 |
| RN11 | Código de Ajustes | Alfanúmerico |  | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro = Ajuste do da Apuração | ADO-797249 |
| RN12 | OUTRO LANCAMENTOS CONTABEIS | Texto | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro =Outros Lançamentos | ADO-797249 |
| RN13 | CODIGO DA NATUREZA OP OU F100 | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro= Outros Lançamentos | ADO-797249 |
| RN14 | INDICADOR DA CONTA_D | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN15 | CONTA CONTABIL_ D | Númerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN16 | DESCRICAO DA CONTA_D | Texto | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN17 | CHAVE DE LANÇAMENTOS_D | Númerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN18 | CENTRO DE CUSTOS_D | Númerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN19 | CENTRO DE LUCRO_D | Númerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN20 | TEXTO HISTÓRICO_D | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN21 | OBSERVAÇÕES LANÇAMENTOS_D | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN22 | INDICADOR DE CONTA_C | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN23 | CONTA CONTABIL_C | Númerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN24 | DESCRICAO DA CONTA_C | Texto | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN25 | CHAVE DE LANÇAMENTOS_C | Númerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN26 | CENTRO DE CUSTOS_C | Númerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN27 | CENTRO DE LUCRO_C | Númerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN28 | TEXTO HISTÓRICO_C | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN29 | OBSERVAÇÕES LANÇAMENTOS_C | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN30 | USUARIO | Alfanúmerico | - | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN31 | DATA INCLUSAO | DATA | DD/MM/AAAA | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN32 | DATA ALTERAÇÃO | DATA | DD/MM/AAAA | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |
| RN35 | DATA DE EXCLUSÃO | DATA | DD/MM/AAAA | Recupere os dados conforme os critérios selecionados: Data, Grupo de Imposto e Tipo de Parâmetro. | ADO-797249 |

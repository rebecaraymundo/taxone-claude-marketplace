# MTZ-Tela_Relatorio_Livro_Razao_Auxiliar

> Fonte: MTZ-Tela_Relatorio_Livro_Razao_Auxiliar.docx


DOCUMENTO DE REQUISITO


### REGRAS DE NEGÓCIO




| DR | Nome | Descrição |
| --- | --- | --- |
| OS3853 | ECD– Tela ‘Relatório Livro Razão Auxiliar’. | Criação da Tela |


| Cód. | Descrição | DR |
| --- | --- | --- |
| RN00 | Criação do Relatório Livro Razão Auxiliar, no Menu: Relatórios do Módulo SPED / ECD – Escrituração Contábil Digital. Esta opção ficará abaixo de ‘Conferencia de Empresas Coligadas’ | OS3853 |
| RN01 | Quando a importação do arquivo, na tela ‘Livro Razão Auxiliar’, localizada no Módulo: SPED / ECD – Escrituração Contábil Digital, Menu: Manutenção, finalizar com sucesso, o sistema deve armazenar os dados em uma tabela.   O usuário poderá ter acesso aos dados a qualquer momento no  ‘Relatório Livro Razão Auxiliar, no Menu Relatórios.  Será gravado na base sempre a ultima importação do layout por período (e estabelecimento), independente do nome do arquivo importado. | OS3853 |
| RN02 | Ao selecionar o Relatório, será apresentada uma tela ‘Selecionar Relatório Razão Auxiliar’, que mostrará os campos Cod. Estab., Livro (Cod./Descr.), Período Escrituracao, Data Importacao.  Serão disponibilizadas todas as importações que foram realizadas com sucesso. | OS3853 |
| RN03 | O relatório apresentado será o mesmo que é apresentado na tela ‘Livro Razão Auxiliar’ | OS3853 |
| RN04 | A barra de ação terá as opções Abrir, Excluir e Fecha. | OS3853 |
| RN05 | Os dados importados poderão ser excluídos, desde que não tenha sido criado nenhum processo no meio magnético, utilizando o layout e período em questão.  Caso contrário, exibir a seguinte msg ao usuário: ‘Os dados não serão excluídos, pois essas informações já estão sendo consideradas em uma geração no meio magnético’ e não excluir os dados. | OS3853 |

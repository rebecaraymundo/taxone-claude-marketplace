# MTZ-Tela_Livro_Razao_Auxiliar

> Fonte: MTZ-Tela_Livro_Razao_Auxiliar.docx


DOCUMENTO DE REQUISITO



### REGRAS DE NEGÓCIO





| DR | Nome | Descrição |
| --- | --- | --- |
| OS3853 | ECD– Tela ‘Livro Razão Auxiliar’. | Inclusão do campo Livro (Cód./Desc.). |
| MFS-43789 | Alessandra Cristina Navatta | Inclusão de validação |


| Cód. | Descrição | DR |
| --- | --- | --- |
| RN00 | Inclusão do campo Livro (Cód./Desc.), logo abaixo do campo Estabelecimento, na tela “Livro Razão Auxiliar” localizada no Módulo: SPED >> ECD – Escrituração Contábil Digital / Menu: Manutenção.  A regra de exibição do campo Estabelecimento deve ser alterada, de modo que sejam demonstrados na listagem de estabelecimentos apenas o estabelecimento que tenha layout cadastrado na tela de “Impressão do Livro Razão Auxiliar”, localizada no Módulo: SPED >> ECD – Escrituração Contábil Digital / Menu: Parâmetros.  No acesso à tela, quando não há estabelecimento cadastrado para a empresa de acesso o sistema retorna a mensagem: “Não há Estabelecimentos cadastrados para esta empresa”. Se, existir cadastro de estabelecimento para a empresa, mas não existir estabelecimento cadastrado na tela de “Impressão do Livro Razão Auxiliar” para a empresa de acesso, retornar a mensagem: “Não há estabelecimentos cadastrados na tela de Impressão do Livro Razão Auxiliar”. | OS3853 |
| RN01 | O campo Livro (Cód./Desc.) deverá demonstrar em um dropdownlist no formato “COD – DESCRICAO” os livros que foram cadastrados na Tela “Impressão do Livro Razão Auxiliar”, localizada no Módulo: SPED >> ECD – Escrituração Contábil Digital / Menu: Parâmetros para o estabelecimento selecionado. | OS3853 |
| RN02 | No relatório da tela, incluir o campo Livro (Cód./Desc.), ao lado do campo Período da Escrituração. | OS3853 |
| RN03 | Ao importar um arquivo, o sistema deve verificar se o mesmo está compatível com o layout definido na tela “Impressão do Livro Auxiliar”, localizada no Módulo: SPED >> ECD – Escrituração Contábil Digital / Menu: Parâmetros, realizando as seguintes verificações:  Se a quantidade de campos do arquivo importado for diferente da quantidade definida na parametrização do layout na tela “Impressão do Livro Auxiliar”, não realizar a importação e retornar a mensagem:  "Layout Difere da Estrutura do arquivo informado no campo <Importar Arquivo Externo> do Menu: Manutenção > Livro Razão Auxiliar (Número de Campos). Favor verificar os campos cadastrados no Menu Parâmetros > Impressão do Livro Razão Auxiliar para que a visualização do arquivo possa ser gerada corretamente"  Se a quantidade de decimais dos campos numéricos do arquivo importado for diferente da quantidade definida na parametrização do layout na tela “Impressão do Livro Auxiliar”, coluna Nº Casas Decimais, não realizar a importação e retornar a mensagem:  "Layout Difere da Estrutura do arquivo informado no campo <Importar Arquivo Externo> do Menu: Manutenção > Livro Razão Auxiliar (Número de Decimais). Favor verificar os campos cadastrados no Menu Parâmetros > Impressão do Livro Razão Auxiliar para que a visualização do arquivo possa ser gerada corretamente"  Se o tamanho de um dos campos do arquivo importado for diferente do tamanho definido na parametrização do layout na tela “Impressão do Livro Auxiliar”, Coluna Tamanho, não realizar a importação e retornar a mensagem:  "Layout Difere da Estrutura do arquivo informado no campo <Importar Arquivo Externo> do Menu: Manutenção > Livro Razão Auxiliar (Tamanho do Campo). Favor verificar os campos cadastrados no Menu Parâmetros > Impressão do Livro Razão Auxiliar para que a visualização do arquivo possa ser gerada corretamente"  [ALTERAÇÃO MFS-43789] – Inclusão de validação:  Quando o parâmetro ‘Importa Arquivo’ estiver selecionado, e for selecionado no campo ‘Importar Arquivo Externo no Formato “texto separado p/ Tabulações” (*.txt)’, apenas um diretório e não um arquivo, exibir a mensagem: “Favor selecionar um arquivo” | OS3853 MFS-43789 |
| RN04 | Se a importação do arquivo finalizar com sucesso, o sistema deve armazenar os dados em uma tabela.   O usuário poderá ter acesso aos dados a qualquer momento na tela “Relatório Livro Razão Auxiliar”, no Menu Relatórios.  Deve ser gravado na base o arquivo importação por estabelecimento, livro e período. Em caso de reimportação de um novo arquivo com os mesmos critérios de estabelecimento, livro e período, o sistema deve retornar a mensagem: “Já existe arquivo importado para o estabelecimento, livro e período indicados. Deseja sobrepor as informações?” com as opções “Sim” e “Não”. Se indicar “Sim”, gravar o novo arquivo. Se clicar em “Não”, abortar a importação. | OS3853 |

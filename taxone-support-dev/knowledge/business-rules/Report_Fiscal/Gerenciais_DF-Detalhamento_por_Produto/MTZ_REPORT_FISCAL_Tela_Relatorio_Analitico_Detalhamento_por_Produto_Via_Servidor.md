---
source: "MTZ_REPORT_FISCAL_Tela_Relatorio_Analitico_Detalhamento_por_Produto_Via_Servidor.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS

Relatório Analítico – Detalhamento por Produto (Via Servidor)
Detalhamento por Produto



DOCUMENTO DE REQUISITO


Sumário

**1.	Regras dos Campos	3**
2.	Sugestão de Layout	5

# Regras dos Campos

Localização da tela: Básicos\ Report Fiscal\ Gerenciais\ Documentos Fiscais\ Analíticos\ Detalhamento por Produto (Via Servidor)

Título da tela: Relatório Analítico – Detalhamento por Produto (Via Servidor)

**Regra Geral:**

Inicialmente esta tela de geração só apresenta as opções de Parâmetros e Processos, após a execução, será disponibilizada mais a opção: Arquivo;
Na aba Parâmetros o usuário deverá preencher informações relevantes para geração do relatório.
Na aba Processos permite o usuário visualizar os processos gerados de acordo com a quantidade de dias informados. Sendo exibido o Número do Processo, Descrição, Início e Fim da Execução, Usuário e Situação do Processo. O usuário ao selecionar um processo, poderá emitir o relatório e até fazer a sua exclusão.
Na aba Arquivo o usuário poderá salvar em disco o arquivo gerado com as informações do relatório de produto, indicando o tamanho máximo do volume a ser gerado, bem como escolher o diretório onde o mesmo será gravado;
Para geração do Relatório o usuário deverá preencher todos os campos de preenchimento obrigatório e o sistema deve informar os campos onde falta informação;
Não haverá seleção por CFOP igual à geração normal e de grandes volumes, gerará com todos os CFOPs que estiver dentro do período e estabelecimento preenchidos na tela de execução;

**Botões Relatório:**

Relatório. – Permite executar a geração do relatório e o sistema deverá gravar o arquivo no diretório escolhido pelo usuário criando o arquivo com o nome padrão “detalhamentoProduto_xxxxxx”:

detalhamentoProduto: O nome padrão do arquivo;

xxxxxx: O número de processo da geração de cada relatório;

.txt ou TXT: Será a extensão do arquivo indicando o programa do qual o relatório será gravado.

Exemplo: detalhamentoProduto_123456.txt

Fecha – Permite o usuário finalizar a tela.

Marcar Todos – Esse botão estará disponível para seleção dos estabelecimentos, devendo marcar todos caso seja utilizado.

Desmarcar Todos – Esse botão estará disponível para seleção dos estabelecimentos, devendo desmarcar todos caso seja utilizado.



# Sugestão de Layout










---

| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4774 | Julyana Perrucini | Este documento tem como objetivo criar a tela de geração do relatório analítico Detalhamento por Produto (Via Servidor). |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Tipo de Execução | Texto | S | S | Formato: Radio Button  Default: Habilitado e Imediata Selecionada | Permite o usuário selecionar como deseja gerar o relatório:  Conteúdo: Imediata: Ao acionar esta opção, o sistema executa a geração de imediato. Programada: Ao acionar esta opção, o usuário programará a execução da geração, indicando a data e o horário desejado para iniciar execução, em "Data/Hora de Execução". | OS4774 |
| Data/Hora de Execução | Texto | N | S | Formato: DD/MM/AAAA 00:00  Default: Desabilitado | Nesse campo o usuário deverá informar a data e hora que deseja fazer a execução do processamento.   Tratamento: Este campo estará disponível, caso o usuário tenha selecionado a opção "Programada" no campo Tipo de Execução. | OS4774 |
| Período Inicial | Texto | S | S | Formato: DD/MM/AAAA  Default: Habilitado | Permite o usuário informar o período inicial que deseja extrair as informações para o relatório.  Observação: Ver regra geral. | OS4774 |
| Período Final | Texto | S | S | Formato: DD/MM/AAAA  Default: Habilitado | Permite o usuário informar o período final que deseja extrair as informações para o relatório.  Observação: Ver regra geral. | OS4774 |
| Pesquisa UF | Texto | N | S | Formato: Combo Box  Default: Habilitado e Sem Seleção | Permite o usuário informar qual estado ele deseja para seleção dos estabelecimentos. | OS4774 |
| Estabelecimentos | Texto | S | S | Formato: Check Box  Default: Habilitado e Desmarcado | Permite listar os estabelecimentos de acordo com a UF selecionada, caso o campo UF não seja preenchido, listará todos os estabelecimentos.  Observação: Ver regra de botões do relatório. | OS4774 |
| Executar | Texto | S | N | Formato: Button  Default: Habilitado | Permite o usuário acionar o processamento das informações. | OS4774 |

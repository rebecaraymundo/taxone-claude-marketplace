---
source: "MTZ_Report_Fiscal_Tela_Relatorio_Analitico_Detalhamento_de_Produto_Grandes_Volumes.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS

Report Fiscal – Relatório Analítico – Detalhamento de Produto (Grandes Volumes)


Localização: Report Fiscal\ Gerenciais\ Documentos Fiscais\ Analíticos\ Detalhamento por Produto (Grandes Volumes)

DOCUMENTO DE REQUISITO


Sumário

**1.	Regras dos Campos	3**

# Regras dos Campos

**Localização da tela:**
Modulo: Básicos >> REPORT FISCAL
Menu: Gerenciais >> Documentos Fiscais >> Analíticos >> “Detalhamento por Produto (Grandes Volumes)”

Título da tela: Relatório Analítico – Detalhamento por Produto (Grandes Volumes)

**Aba Serviços:**
- Botão Relatório: Para geração do Relatório o usuário deverá preencher todos os campos de preenchimento obrigatório, o sistema deve informar os campos onde falta informação, após preencher todos os campo preenchidos o sistema deverá gerar o arquivos em diretório escolhido pelo usuário criando o arquivo com nome padrão “detalhamentoProduto_numero do processo_sequencial.xsl” onde:

detalhamentoProduto: O nome padrão dado a todo arquivo;

numero do processo: O número de processo da geração de cada relatório;

sequencial:  Será o sequencial atribuído a cada quebra de arquivo;

.xsl: Será a extensão do arquivo indicando o programa do qual o relatório será gravado.

Exemplo: detalhamentoProduto_123456_1.xsl
detalhamentoProduto_123456_2.xsl
detalhamentoProduto_123456_3.xsl




- Botão Sair: Para o usuário finalizar a tela.




**Nesta tela estarão disponíveis os campos:**

- Período
- Diretório
- Quebrar Arquivos por Quantidade de Registro
- Seleção de CFOP’s
- UF
- Estabelecimentos


Funcionamento da tela: Nessa tela o usuário poderá emitir o relatório Analítico por Produto, considerando para sua geração os parâmetros de empresa filial, período e CFOP.
Devido à grande quantidade de registros, esse relatório será gerado em arquivos Execel, o mesmo deverá ser quebrado por quantidade de registro parametrizado pelo usuário, o sistema trama como default para quebra a cada 500.000 mil registros.

Campos do Relatório: Serão demonstrados todos os campos como é demonstrado no relatório padrão, verificar documento matriz: MTZ_Report_Fiscal_Relatorio_Analitico_Detalhamento_de_Produto.docx


* Descrição não disponível em tela





---

| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS_4603 | Marcelo Silva | Criação da tela Relatório Analítico – Detalhamento de Produto (Grandes Volumes), esse Grandes volumes ira salvar relatório em um arquivo Excel quebrando o por quantidade de registro. |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | TextField | S | S | - | O usuário deverá informar a data inicial e a data final do Período desejado para a extração das informações. | OS_4603 |
| Diretório | TextField | S | S | - | Neste campo o usuário deverá informar o diretório aonde será gravado o arquivo gerado. | OS_4603 |
| Quebrar Arquivo por Quantidade de Registros | TextField | S | S | - | Nesse campo o usuário deverá informar a quantidade de registro que o sistema deverá realizar a quebra de arquivos. O sistema deverá trazer como Default o campo preenchido com 250.000, para quebra de arquivos a cada 250 Mil registros. | OS_4603 |
| Seleção de CFOP's | Seleção de RadioButton | S | S | - | Esse campo irá lista todos os CFOP's cadastrados, para que o usuário selecione quais os CFOP's que deseja emitir o relatório. Incluir botão “Marcar Todos” permitindo ao usuário selecionar todos os códigos CFOP's, e “Desmarcar Todos” para o usuário desmarcar os códigos CFOP’s selecionados.  Incluir botão “Marcar Entradas” permitindo ao usuário selecionar todos os códigos CFOP's de entrada e “Desmarcar Entradas” para o usuário desmarcar todos os códigos CFOP’s de entrada.   Incluir botão “Marcar Saídas” permitindo ao usuário selecionar todos os códigos CFOP's de saída e “Desmarcar Saídas” para o usuário desmarcar todos os códigos CFOP’s de saída. | OS_4603 |
| UF | DropDown | S | S | - | O usuário deverá informar qual Estado ele deseja selecionar, para das informações. | OS_4603 |
| Estabelecimentos | Seleção de RadioButton | S | S | - | Nesse campo o usuário terá a possibilidade de informar os estabelecimentos para gerar o relatório, tendo a opção do botão “Marcar Todos” e “Desmarcar Todos”. | OS_4603 |

# MTZ-REINF-Relatorio-R5011-Valores-Consolidados-por-Periodo-Texto

> Fonte: MTZ-REINF-Relatorio-R5011-Valores-Consolidados-por-Periodo-Texto.docx






THOMSON REUTERS

Módulo REINF

Relatório de Conferência do Evento R-5011 (Valores Consolidados por Período) – Formato TXT


Localização: Menu SPED, módulo EFD – Reinf, menu Relatórios   Conferência dos Eventos   R-5011 (Valores Consolidados por Período)  Formato TXT




DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	3
2.	Layout da Tela	4
3.	Regras de Funcionamento dos Campos	5
4.	Regras da Recuperação dos Dados	6
5.	Layout e Preenchimento dos Campos	6

## Regras Gerais


Relatório criado com o objetivo de possibilitar a consulta dos valores calculados pelo Fisco no fechamento do período.
Trata-se de um relatório para salvar os dados em um arquivo .TXT, devido à necessidade de sumarizar os valores gerados em uma planilha excel.













## Layout da Tela









## Regras de Funcionamento dos Campos





## Regras da Recuperação dos Dados


A origem dos dados para emissão do relatório tem como base os eventos R-2099 e R-5011:

As regras de recuperação dos dados para o relatório estão definidas no documento MTZ-REINF-Relatorio-R5011-Valores-Consolidados-por-Periodo.doc.

## Layout e Preenchimento dos Campos


O Relatório será gerado em arquivo texto, deverão ser gravadas todas as informações que são mostradas no Relatório de Conferência do Evento R-5011 (Valores Consolidados por Período), menu Relatórios  Conferência dos Eventos  R-5011 (Valores Consolidados por Período).

O arquivo texto deve ser gerado com o cabeçalho das colunas existentes no relatório e deve ser incluída uma coluna no início do arquivo, que irá identificar o evento, como por exemplo, R-2020.  Como existem vários layouts de relatório, um para cada evento, o cabeçalho de cada relatório deve ser gerado no arquivo, por este motivo a primeira coluna deve ser o identificador do evento.


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS21696 | Andréa Rocha | Criação do relatório de conferência do evento R-5011 (Valores Consolidados por Período)  - Formato TXT | 30/05/2019 |
|  |  |  |  |
|  |  |  |  |


| Sobre o evento R-5011:  Estes valores estarão no evento R-5011, evento gerado pelo Fisco, e enviado aos contribuintes após o recebimento do evento R-2099 (junto com a mensagem de retorno).  O Fisco envia o R-5011 sempre que um evento R-2099 é recepcionado com sucesso (status de retorno do Onesource = “Evento recebido pelo Fisco com sucesso” ou “Evento recebido pelo Fisco com advertência”). O Onesource processa estes dados e retorna para o MSAF um XML (através da STG_EVENTOS_REINF_IN), que contém entre outras informações, estes valores gerados pelo Fisco.  No módulo REINF (DW) estes dados são recuperados para emissão do relatório.  Cada evento R-5011 é vinculado a um evento R-2099 (através da tabela de ocorrências). |
| --- |


| Campo | Tipo | Obrig | Ed | Formato / Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Período | Data (mês e ano) | S | S | (MM/AAAA) | Mês e ano do período para emissão do relatório.  Deve ser um mês válido. |
| Multiempresas | Alfanumérico | N | S | Default:  Desmarcado | Na abertura da tela esta opção aparecerá sempre desmarcada. |
| Empresa / Estabelecimento | Alfanumérico | S | S |  | Neste campo será exibida a lista dos estabelecimentos para seleção do usuário.  A lista dos estabelecimentos depende do período e da opção “Multiempresas”. Por isso, será montada somente após o usuário informar o período.  Obs.: Sempre que o período ou a opção de multiempresa forem alterados, esta lista será refeita automaticamente.   Regra dos estabelecimentos a serem exibidos:   Será feita a pesquisa de todos os eventos R-2099 existentes para o período informado, cujo status indique que o evento já foi recebido pelo Fisco com sucesso/advertência.  (A pesquisa é baseada na tabela “OC” do R-2099,  e a partir dela, se obtém a empresa, estab. e período na PGER_APUR)   Serão disponibilizados para seleção apenas os estabelecimentos dos eventos R-2099 encontrados conforme a condição acima.  Além das condições acima, deve-se observar também a opção de multiempresas:  Se opção “Multiempresas” desmarcada:      Considera apenas os estabelecimentos da empresa do login; Senão      Considera os estabelecimentos de todas as empresas;  Para cada estabelecimento a ser exibido, será mostrado:  - Código da empresa; - Código do estabelecimento; - Razão Social do estabelecimento; |
| Selecionar todos / Desmarcar todos | Alfanumérico | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados. |

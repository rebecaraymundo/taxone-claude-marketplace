# MTZ_Relatorio_Sintetico_Analitico_DLPA_ou_DMPL_J210_J215

> Fonte: MTZ_Relatorio_Sintetico_Analitico_DLPA_ou_DMPL_J210_J215.docx






THOMSON REUTERS

Módulo SPED

Relatório Sintético e Analítico – Demonstração DLPA e DMPL – J210 e J215



Localização: MastersafDW >> SPED >> ECD – Escrituração Contábil Digital >> Geração >> Demonstrações Contábeis







DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	3
2.	Definição do Relatório	3
4.1 – Recuperação dos Registros:	3
4.2 – Layout e Preenchimento dos Campos:	3
4.2.1 – Visão Sintética:	3
4.2.2 – Visão Analítica	5





















## Regras Gerais


Este relatório tem por objetivo exibir as informações das demonstrações de DLPA e DMPL geradas no Menu SPED >> ECD – Escrituração Contábil Digital >> Geração >> Demonstrações Contábeis.


## Definição do Relatório



### 4.1 – Recuperação dos Registros:


As regras do processamento das demonstrações de resultado estão disponíveis no arquivo ‘MTZ_Processamento_Geracao_das_Demonstracoes_Contabeis.doc’

As regras de preenchimento das colunas no relatório estão descritas no item a seguir.


### 4.2 – Layout e Preenchimento dos Campos:


Layout: vide planilha “Layout-Relatorios-BP-DRE-DMPL-DLPA.xlsx”, abas “Relatório DMPL_DLPA – Sintético” e “Relatório DMPL_DLPA – Analítico”.

Na tela de Geração das Demonstrações será gerada uma aba com o título ‘Relatório Sintético – ‘DLPA’ ou ‘Relatório Sintético – ‘DMPL’ e outra ‘Arquivos’ (nesta última serão apresentados os arquivos das demonstrações em formato , nas duas visões Sintética e Analítica) conforme regras abaixo:

#### 4.2.1 – Visão Sintética:


DLPA ou DMPL
Visão Sintética será apresentada em tela (Aba Relatório Sintético – DLPA ou Aba Relatório Sintético – DMPL), se a demonstração DLPA ou DMPL estiverem marcadas na tela de geração:


(*) Não apresentar no relatório.


- A visão sintética (apresentada acima), também será gerada na aba Arquivos, ou seja, em formato (apresentando todos os campos do agrupamento ‘Conteúdo do Relatório – Movimento’além dos campos de identificação: Empresa, Estab e período). Os labels dos campos deste formato de relatório, devem considerar os indicados no item 4.2.2 Visão Analítica.


#### 4.2.2 – Visão Analítica




Será gerado na aba Arquivos em formato .

DLPA ou DMPL

(*) Não apresentar no relatório.




| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS31026 | Alessandra Cristina Navatta | Criação dos Relatórios (Sintético e Analítico) da Demonstração DLPA e DMPL – J210 e J215. | 13/11/2019 |


| Campo | Campo | Tipo | Formato / Default | Regra |
| --- | --- | --- | --- | --- |
| Cabeçalho | Cabeçalho | Cabeçalho | Cabeçalho | Cabeçalho |
| Título | Título | Texto |  | Se DLPA: “DLPA – Relatório Sintético” Se DMPL: “DMPL – Relatório Sintético” |
| Empresa | Empresa | Texto | Cód. – Razão Social | Exibir o código e a razão social da empresa. |
| Data | Data | Data | DD/MM/AAAA às HH:MM:SS hs | Exibir a data e hora da geração da demonstração |
| Página | Página | Texto |  | Exibir o número da página do relatório |
| Estabelecimento | Estabelecimento | Texto | Cód. – Razão Social | Exibir o código e a razão social do estabelecimento. |
| CNPJ | CNPJ | Texto | 00.000.000/0000-00 | Exibir o CNPJ do estabelecimento. |
| Período do demonstrativo | Período do demonstrativo | Texto | DD/MM/AAAA | Exibir o período de geração do demonstrativo (data inicial e final da tela de geração). |
| Conteúdo do Relatório – Movimento (*) | Conteúdo do Relatório – Movimento (*) | Conteúdo do Relatório – Movimento (*) | Conteúdo do Relatório – Movimento (*) | Conteúdo do Relatório – Movimento (*) |
| Ordem | Ordem | Texto |  | Exibir o número da ordem das informações.  Apresentar em ordem crescente. |
| Nível | Nível | Texto |  | Exibir o nível das informações. Apresentar em ordem crescente. |
| Cód. Aglutinação | Cód. Aglutinação | Texto | Cód. | Exibir o código das contas aglutinadoras. |
| Descrição | Descrição | Texto | Descrição | Exibir a descrição das contas aglutinadoras. |
| Moeda Corrente | Saldo Inicial | Texto | 0,00 | Exibir o saldo inicial da conta aglutinadora (referente a moeda corrente). |
| Moeda Corrente | Ind. D/C | Texto | D/C | Exibir o indicador do saldo inicial da conta aglutinadora (referente a moeda corrente). |
| Moeda Corrente | Saldo Final | Texto | 0,00 | Exibir o saldo final da conta aglutinadora (referente a moeda corrente). |
| Moeda Corrente | Ind. D/C | Texto | D/C | Exibir o indicador do saldo final da conta aglutinadora (referente a moeda corrente). |
| Moeda Funcional | SaldoInicial | Texto | 0,00 | Exibir o saldo inicial da conta aglutinadora (referente a moeda corrente). |
| Moeda Funcional | Ind. D/C | Texto | D/C | Exibir o indicador do saldo inicial da conta aglutinadora (referente a moeda funcional). |
| Moeda Funcional | Saldo Final | Texto | 0,00 | Exibir o saldo final da conta aglutinadora (referente a moeda corrente). |
| Moeda Funcional | Ind. D/C | Texto | D/C | Exibir o indicador do saldo final da conta aglutinadora (referente a moeda funcional). |


| Campo | Tipo | Formato / Default | Regra | Regra |
| --- | --- | --- | --- | --- |
| Empresa | Texto | Cód. – Razão Social | Cód. – Razão Social | Exibir o código e a razão social da empresa. |
| Estab | Texto | Cód. – Razão Social | Cód. – Razão Social | Exibir o código e a razão social do estabelecimento. |
| Período | Texto | DD/MM/AAAA | DD/MM/AAAA | Exibe o período das informações de saldo recuperadas. |
| Conteúdo do Relatório – Movimento(*) | Conteúdo do Relatório – Movimento(*) | Conteúdo do Relatório – Movimento(*) | Conteúdo do Relatório – Movimento(*) | Conteúdo do Relatório – Movimento(*) |
| Ordem | Texto |  |  | Exibir o número da ordem das informações.  Apresentar em ordem crescente. |
| Nível | Texto |  |  | Exibir o nível das informações. Apresentar em ordem crescente. |
| Cód. Aglutinação | Texto | Cód. | Cód. | Exibir o código das contas aglutinadoras. |
| Descrição | Texto | Descrição | Descrição | Exibir a descrição das contas aglutinadoras. |
| Cod Conta | Texto | Cód. | Cód. | Exibir o código das contas contábeis. |
| Saldo Ini | Texto | 0,00 | 0,00 | Exibir o saldo inicial da conta aglutinadora/conta contábil (referente a moeda corrente). |
| D/C Inicial | Texto | D/C | D/C | Exibir o indicador do saldo inicial da conta aglutinadora/conta contábil (referente a moeda corrente). |
| Saldo Final | Texto | 0,00 | 0,00 | Exibir o saldo final da conta aglutinadora/conta contábil (referente a moeda corrente). |
| D/C Final | Texto | D/C | D/C | Exibir o indicador do saldo final da conta aglutinadora/conta contábil (referente a moeda corrente). |
| Saldo Ini MF | Texto | 0,00 | 0,00 | Exibir o saldo inicial da conta aglutinadora/conta contábil (referente a moeda corrente). |
| D/C Inicial MF | Texto | D/C | D/C | Exibir o indicador do saldo inicial da conta aglutinadora/conta contábil (referente a moeda funcional). |
| Saldo Final MF | Texto | 0,00 | 0,00 | Exibir o saldo final da conta aglutinadora/conta contábil (referente a moeda corrente). |
| D/C Final MF | Texto | D/C | D/C | Exibir o indicador do saldo final da conta aglutinadora/conta contábil (referente a moeda funcional). |
| Detalhamento J215(*) | Detalhamento J215(*) | Detalhamento J215(*) | Detalhamento J215(*) | Detalhamento J215(*) |
| Cod Hist Fat | Texto |  |  | Exibir o código do histórico do fato contábil. |
| Descrição | Texto |  |  | Exibir a descrição do fato contábil/. |
| Valor Fat Cont | Texto | 0,00 | 0,00 | Exibir o valor do fato contábil referente a moeda corrente. |
| D/C Fat | Texto | D/C | D/C | Exibir o indicador do fato contábil referente a moeda corrente. |
| Valor Fat Cont MF | Texto | 0,00 | 0,00 | Exibir o valor do fato contábil referente a moeda funcional. |
| D/C Fat MF | Texto | D/C | D/C | Exibir o indicador do fato contábil referente a moeda funcional. |

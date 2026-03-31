# MTZ-eSocial-Geracao-Movimentos

> Fonte: MTZ-eSocial-Geracao-Movimentos.docx






THOMSON REUTERS

Módulo eSocial

Geração dos Movimentos


Localização: Menu SPED, módulo Informações para o eSocial, menu Geração à Geração dos Movimentos


DOCUMENTO DE REQUISITO



Sumário

1.	Parâmetros da Tela	2
2.	Processamento	5





Devido ao end-of-support da mensageria OS E-Social, e a não utilização de clientes no Tax One integrados, o módulo Informações para o E-Social será retirado do TAX ONE e deverá permanecer no DW.
















## Parâmetros da Tela
















## Processamento


Nesta geração os dados serão armazenados em tabelas, já com o formato e hierarquia exigidos no layout do eSocial, para posterior conferência do usuário, e geração dos arquivos XML.

O sistema deve verificar a disponibilidade de data x versão x ambiente de cada Estabelecimento selecionado, de acordo com a tabela abaixo:


Caso seja selecionada uma versão não disponível para o ambiente e versão na data, o sistema não deve executar a geração para o estabelecimento incompatível, e apresentar a mensagem:
“Versão do Layout e o Tipo de Ambiente parametrizado para o estabelecimento, está indisponível para geração.' Estabelecimento: <<Estabelecimento>> Versão selecionada: <<Versão Selecionada>> Tipo Ambiente: <<Tipo Ambiente>>. Verifique a disponibilidade das versões no site "https://www.gov.br/esocial/pt-br"

As regras de geração de cada um dos eventos estão descritas em documentos separados, da seguinte forma:



MFS16762]
Importante: Na tela Geração dos Movimentos serão gerados APENAS os eventos Originais, os eventos de Retificação deverão ser gerados diretamente pelo Painel de Controle de Eventos pela opção ‘Reprocessar Evento’.

= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS15870 | Vânia Mattos | Criação da geração dos eventos de movimentos, com os eventos S-1200 e S-1210. | 19/12/2017  (criação do documento) |
| MFS15871 | Vânia Mattos | Alteração da geração dos movimentos p/inclusão do evento S-1300 | 08/01/2018 |
| MFS18065 | Vânia Mattos | Alteração da versão demonstrada no campo “Versão” da tela da geração | 07/06/2018 |
| MFS16762 | Lara Aline | Inclusão rotina de Reprocessar Evento | 27/08/2018 |
| MFS-87292 | Elisabete Costa | Alterações para versão S-1.0. | 06/06/2022 |
| MFS-87543 | Elisabete Costa | Exclusão do Evento S-1300 versão S-1.0 | 06/06/2022 |
| MFS-96008 | Elisabete Costa | Retirada do Módulo: Informações para o E-Social do T1 | 04/11/2022 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período (MM/AAAA) | Data (mês/ano) | S | S | (MM/AAAA) | Mês e ano para a geração dos movimentos. |  |
| Versão | Alfanumérico | S | N | Listbox | Este campo é uma lista, com as opções: [2.4.01]  [2.4.02] 2.5.00 S-1.0  (MFS18065: Alteração para versão 2.4.02) (MFS-87292: Alteração para a versão S-1.0) |  |
| Eventos | Alfanumérico | S | N | Checkbox | Neste quadro são exibidos os eventos de movimento para seleção do usuário:  S-1200 - Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social  S-1210 - Pagamentos de Rendimentos do Trabalho [MFS-87543] S-1300 - Contribuição Sindical Patronal  O Evento S-1300 não deve ser exibido a partir da versão S-1.0. |  |
| Estabelecimentos | Alfanumérico | S | N | Checkbox | Neste campo será exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário.  Serão disponibilizados para seleção apenas os estabelecimentos da Empresa cadastrados na parametrização dos dados iniciais do eSocial (menu “Parâmetros > Dados Iniciais”).  (lembrando que esta parametrização só trabalha com os estabelecimentos centralizadores das obrigações federais) |  |
| Selecionar | Alfanumérico | N | N |  | Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos.  O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimento”:  - Somente Estabelecimentos da empresa do login;  - Somente Estabelecimentos parametrizados nos Dados Iniciais;  Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimento” já marcados. |  |
| Marcar todos | Alfanumérico | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimento”. |  |


| Ambiente | Versão | Data Inicial | Data Final |
| --- | --- | --- | --- |
| Produção Restrita | 2.5.00 | - | 22/05/2022 |
| Produção Restrita | S1.0 | 23/05/2022 | - |
| Produção | 2.5.00 | - | 22/05/2022 |
| Produção | S1.0 | 23/05/2022 | - |


| Evento | Origem das informações | Documento de Regras |
| --- | --- | --- |
| S-1200 – Remuneração do Trabalhador | SAFX04 (Pessoa Fis/Jur) SAFX247 (Demonstrativo) SAFX248 (Rubricas) SAFX250 (Outros Vínculos) | MTZ-eSocial-Geracao-Evento-S1200-Remuneracao |
| S-1210 - Pagamentos de Rendimentos | SAFX04 (Pessoa Fis/Jur) SAFX247 (Demonstrativo) SAFX248 (Rubricas) SAFX249 (Pagamentos Parciais) | MTZ-eSocial-Geracao-Evento-S1210-Pagamentos |
| S-1300 – Contribuição Sindical | SAFX251 (Contribuições Sindicais) | MTZ-eSocial-Geracao-Evento-S1300-ContribSindical |

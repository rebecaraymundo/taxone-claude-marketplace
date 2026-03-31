# MTZ-eSocial-Geracao-Cadastros

> Fonte: MTZ-eSocial-Geracao-Cadastros.docx






THOMSON REUTERS

Módulo eSocial

Geração dos Cadastros


Localização: Menu SPED, módulo Informações para o eSocial, menu Geração  Geração dos Cadastros


DOCUMENTO DE REQUISITO








Sumário

1.	Parâmetros da Tela	2
2.	Processamento	5



Devido ao end-of-support da mensageria OS E-Social, e a não utilização de clientes no Tax One integrados, o módulo Informações para o E-Social será retirado do TAX ONE e deverá permanecer no DW.













## Parâmetros da Tela




OBS: Esta geração dos cadastros considera apenas os estabelecimentos centralizadores, pois todos os cadastros disponíveis para geração são tabelas de códigos, que trabalham com Grupo. Por isso, não faria sentido disponibilizar geração isolada por estabelecimento.









## Processamento



Nesta geração os dados serão armazenados em tabelas, já com o formato e hierarquia exigidos no layout do eSocial, para posterior conferência do usuário e geração dos arquivos XML.

O sistema deve verificar a disponibilidade de data x versão x ambiente de cada Estabelecimento selecionado, de acordo com a tabela abaixo:

Caso seja selecionada uma versão não disponível para o ambiente e versão na data, o sistema não deve executar a geração para o estabelecimento incompatível, e apresentar a mensagem:
“Versão do Layout e o Tipo de Ambiente parametrizado para o estabelecimento, está indisponível para geração.' Estabelecimento: <<Estabelecimento>> Versão selecionada: <<Versão Selecionada>> Tipo Ambiente: <<Tipo Ambiente>>. Verifique a disponibilidade das versões no site "https://www.gov.br/esocial/pt-br"

As regras de geração de cada um dos eventos estão descritas em documentos separados, da seguinte forma:

= = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS15868 | Geração dos eventos de cadastro | Geração dos eventos de cadastro | 12/12/2017  (criação do documento) |
| MFS15869 | Geração dos eventos de cadastro | Alteração da geração dos cadastros p/inclusão dos eventos S-1020 e S-1070 | 08/01/2018 |
| MFS18065 | Atualização do eSocial para versão 2.4.02. | Alteração da versão demonstrada no campo “Versão” da tela da geração | 07/06/2018 |
| MFS-88128 | Elisabete Costa | Alterações para versão S1.0. | 15/06/2022 |
| MFS-96008 | Elisabete Costa | Retirada do Módulo: Informações para o E-Social do T1 | 04/11/2022 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período Inicial | Data (mês e ano) | S | S | (MM/AAAA) | Mês e ano inicial para a geração dos cadastros.  Deve ser um mês válido. |  |
| Período Final | Data (mês e ano) | S | S | (MM/AAAA) | Mês e ano final para a geração dos cadastros.  Deve ser um mês válido e >= ao mês/ano inicial. |  |
| Versão | Alfanumérico | S | N | Listbox | Este campo é uma lista, com as opções: [2.4.01]  2.4.02 2.5.00 S-1.0 (MFS18065: Alteração para versão 2.4.02) (MFS-88128: Alteração para a versão S-1.0) | MFS-88128 |
| Eventos | Alfanumérico | S | N | Checkbox | Neste quadro são exibidos os eventos de cadastro para seleção do usuário:  S-1005 - Estabelecimentos S-1010 - Rubricas S-1020 - Lotações  S-1070 - Processos Administrativos / Judiciais |  |
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
| S-1005 - Cadastro de Estabelecimento | Tabela dos de Estabelecimento e parametrização das informações do contribuinte | MTZ-eSocial-Geracao-Evento-S1005-Estabelecimentos |
| S-1010 - Cadastro de Rubricas | SAFX2114 | MTZ-eSocial-Geracao-Evento-S1010-Rubricas |
| S-1020 - Cadastro de Lotações | SAFX2037 | MTZ-eSocial-Geracao-Evento-S1020-Lotacoes |
| S-1070 - Cadastro de Processos | SAFX2058 / SAFX2059 | MTZ-eSocial-Geracao-Evento-S1070-Processos |

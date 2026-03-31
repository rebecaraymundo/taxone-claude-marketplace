# MTZ-eSocial-Dados-Iniciais

> Fonte: MTZ-eSocial-Dados-Iniciais.docx






THOMSON REUTERS

Módulo eSocial

Manutenção dos Dados Iniciais


Localização: Menu SPED, módulo Informações para o eSocial, menu Parâmetros  Dados Iniciais




DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
3.	Regras de Funcionamento dos Campos	3



Devido ao end-of-support da mensageria OS E-Social, e a não utilização de clientes no Tax One integrados, o módulo Informações para o E-Social será retirado do TAX ONE e deverá permanecer no DW.















## Regras Gerais


A parametrização dos dados iniciais foi criada na MFS15509 (criação do módulo eSocial).

Estrutura da tabela:


Campos que compõe a chave da tabela: Código da Empresa + Código do Estabelecimento

Obs: A princípio existirá apenas um parâmetro na tela, mas futuramente, é provável que sejam incluídas novas informações.




















## Layout da Tela






Botões da barra de menu:



## Regras de Funcionamento dos Campos








= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS15509 | Criação do módulo eSocial | Criação da parametrização “Dados Iniciais” do módulo eSocial. | 20/12/2017 |
| MFS22083 | Lara Aline | Inclusão do parâmetro “Gerar evento S-1250 a partir da SAFX63 – Arquivo de Contribuição Rural - INSS” | 08/11/2018 |
| MFS-87543 | Elisabete Costa | Exclusão do Evento S-1250 – Para a versão S-1.0 | 07/06/2022 |
| MFS-96008 | Elisabete Costa | Retirada do Módulo: Informações para o E-Social do T1 | 04/11/2022 |


| Descrição | Tamanho | Tipo |
| --- | --- | --- |
| Código da Empresa | 003 | A |
| Código do Estabelecimento | 006 | A |
| Tipo de Ambiente | 001 | N |


| NOVO | Ao clicar nesta opção, as informações dos campos serão limpas e o usuário poderá incluir um novo registro. |
| --- | --- |
| ABRE | Ao clicar nesta opção, será aberta a janela para seleção dos registros já cadastrados para consulta ou manutenção. |
| EXCLUI | Esta opção permite a exclusão do registro. |
| CONFIRMA | Opção para salvar as informações do registro incluído ou alterado. |
| RELATÓRIO | Esta opção permite imprimir os dados da tabela. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato / Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | N | Listbox | Neste campo será exibida a lista dos estabelecimentos da empresa para seleção do usuário.   Serão disponibilizados para seleção apenas os estabelecimentos centralizadores da parametrização das obrigações federais (módulo Parâmetros, menu Preliminares > Centralização da Escrituração de Obrigações Federais). |  |
| Tipo de ambiente | Alfanumérico | S | N | Listbox | Este campo é uma lista com as seguintes opções:  1 - Produção 2 - Produção restrita |  |


| Evento S-1210 – Pagamentos de Rendimento do Trabalho: |
| --- |


| Valor da dedução por dependente (IRRF) | Numérico | N | S |  | Neste campo será informado o valor da dedução da base de cálculo do IRRF por dependente, previsto na legislação do imposto de renda.   Este valor é utilizado na geração do evento S-1210, registro “deps”, campo 18-vrDedDep. |  |
| --- | --- | --- | --- | --- | --- | --- |


| Evento S-1250 – Aquisição de Produção Rural: |
| --- |


| Gerar evento S-1250 a partir da SAFX63 – Arquivo de Contribuição Rural - INSS | Checkbox | N | S | Default: Não selecionado | Nesse campo o usuário poderá selecionar se deseja gerar o evento S-1250 a partir da SAFX63. A partir da versão S-1.0 não deve ser gerado o evento S-1250 | MFS22083 [MFS87292] |
| --- | --- | --- | --- | --- | --- | --- |

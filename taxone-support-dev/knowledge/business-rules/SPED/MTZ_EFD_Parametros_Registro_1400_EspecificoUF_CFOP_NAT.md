# MTZ_EFD_Parametros_Registro_1400_EspecificoUF_CFOP_NAT

> Fonte: MTZ_EFD_Parametros_Registro_1400_EspecificoUF_CFOP_NAT.docx




THOMSON REUTERS

Módulo Sped Fiscal

Parametrização de Natureza de Operação p/ Geração do Registro 1400
(a partir das regras específicas de cada UF)


Localização: Módulo EFD - Escrituração Fiscal DigitaI, item Parâmetros  Registro 1400  Específico por UF  CFOP / Natureza de Operação

DOCUMENTO DE REQUISITO


REGRAS DE NEGÓCIO



Esta parametrização foi criada nas OS’s4728 e 4735 com objetivo de atender a geração do registro 1400 de acordo com as orientações da Sefaz-MG (Resolução 4.730, Dez/14) e Sefaz-SP (Portaria CAT 137, Dez/2014).

Na MFS1513 (Set/2015) foram incluídas as operações solicitadas pela Sefaz-ES (Portaria n. 43-R, de Ago/2015).

Na MFS3132/MFS3248 (Fev/Nov2016) foram incluídas as operações solicitadas pela Sefaz-RN (Orientação Técnica EFD nº 011/2016, de Fev/2016).

Na MFS8625 (Dez/2016) foram incluídas as operações solicitadas pelo RS (sem ato legal, liberada apenas a tabela no site da EFD);

Na MFS16364 (Fev/2018) foram habilitadas todas as operações aos estabelecimentos obrigados ao Convênio ICMS 52/2005 porque serão gerados os arquivos da EFD para as UF’s nas quais os estabelecimentos tenham prestado serviços de TV por assinatura via satélite.

Na MFS16811 (Mar/2018) foram incluídas as operações solicitadas pela Sefaz-BA (sem ato legal, liberada apenas a tabela no site da EFD);

Na MFS17764 (Abr/2018) foram incluídas as operações solicitadas pela Sefaz-TO (Portaria nº 265, de 23 de março de 2018).

Na MFS31044 (Out/2019) foi incluída a operação TOIPME10 para TO.

Na MFS35133 (Jun/2020) foram incluídas as operações TOIPME05 e TOIPMS05 para TO.

Na MFS59468 (Fev/2021) foi incluída a operação PEIPMS0 para PE.

Na MFS61948 (Mar/2021) foram incluidas as operações BAE07, BAE13 e BAE14 para BA.

Na MFS61950 (Abr/2021) foram incluídas as operações BAE05 e BAS05 para BA.

Na MFS61951 (Abr/2021) foram incluídas as operações BAE06 e BAS06 para BA.

Na MFS64052 (Abr/2021) foi incluída a operação IPM 3.5 para RN.

Na MFS64779 (Maio/2021) foi incluída a operação PEIPMS4 para PE.

Na MFS67705 (Junho/2021) foi incluida a operação PEIPME3 para PE.

Na MFS68577 (Julho/2021) foi incluida a operação BAE20 para BA.

Na MFS43147 (Agosto/2021) foi incluida a operação ACIPMS04 para AC.

Na MFS35318 (Agosto/2021) foi incluida a operação TOIPMS10 para TO.

Na MFS59472 (Agosto/2021) foi incluida a operação PEIPMS3 para PE.

Na MFS40285 (Setembro/2021) foi incluida a operação 06 para SC.

Na MFS35221 (Setembro/2021) foram incluidas as operações RJVAF20002 e RJVAF20003 para RJ.

Na MFS47088 (Outubro/2021) foram incluídas as operações MAVAF005, MAVAF006 e MAVAF007 para MA.

Na MFS86117 (Maio/2022) foram incluídas as operações RJVAF00006 e RJVAF10006 para RJ.

Na MFS86203 (Junho/2022) foi incluída a operação IPM 3.6 para RN.

Na MFS94497 (Outubro/2022) foi incluída a operação 1201 para AL.

Na MFS402300 (Março/2023) foram incluídas as operações BAE80 e BAS80 para BA.

Na MFS402301 (Março/2023) foram incluídas as operações BAE81 e BAS81 para BA.

Na MFS547634 (Julho/2023) foram incluídas as operações RJVAF00005 e RJVAF10005 para RJ.

Na MFS556958 (Agosto/2023) foram incluídas as operações RJVAF00009 e RJVAF10009 para RJ.

Na MFS551008 (Agosto/2023) foram incluídas as operações RJVAF00007 e RJVAF10007 para RJ.

Na MFS663539 (Julho/2024) foram incluídas as operações BAE21, BAE22, BAE23, BAE24, BAS21, BAS22, BAS23,BAS24 para BA.

Na MFS672643 (Janeiro/2025) foi incluída a operação “Outras_Entradas_a_Detalhar_por_Municipio (especifico para 3.6.14)”, para MG.


Opções da barra de menu:

Seleciona Grupo  Ao clicar nesta opção, abrirá uma janela de seleção dos grupos de relacionamento das tabelas do Mastersaf, e o usuário deverá selecionar o grupo e estabelecimento. Na abertura da tela esta janela será exibida automaticamente, obrigando o usuário a selecionar o Grupo e Estabelecimento. O grupo e estabelecimento selecionados serão exibidos nos campos “Estabelecimento” e “Grupo Natureza”.

Caso tenha sido informado um estabelecimento no login, serão disponibilizados apenas os grupos aos quais este estabelecimento esteja associado. Caso contrário, serão disponibilizados todos os grupos e estabelecimentos da Empresa do login.

Confirma  salva os dados incluídos ou alterados para o estabelecimento e operação em questão;

Relatório  Esta opção permite a emissão de relatório de conferência dos dados parametrizados, conforme padrão das telas de manutenção. Os critérios para emissão do relatório são Estabelecimento e Operação. O usuário deverá obrigatoriamente selecionar um estabelecimento, e opcionalmente escolher uma operação específica, se desejar. Serão listados todos os dados parametrizados para os critérios selecionados;

Fecha  fecha a janela da parametrização;


Estabelecimento  Neste campo será exibido o estabelecimento selecionado na janela de seleção do Grupo.



Grupo Natureza  Este campo exibe o grupo selecionado pelo usuário na abertura da tela, ou alterado pelo usuário na opção “Seleciona Grupo” da barra de menu.



Operação  Este campo é uma lista onde serão exibidos os seguintes tipos de operação:



Os códigos exibidos nesta lista correspondem aos códigos da TACES89, tabela que contém todos os itens da tabela “Tabela de Itens UF Índice de Participação dos Municípios”, criada por algumas UF’s para a geração do registro 1400, e disponível no site da EFD.

O campo “Operação” exibe apenas os códigos gerados de forma automática pelo sistema, e cuja geração utiliza esta parametrização. Isso significa que os códigos da TACES89 que não possuem geração automática, ou possuem, mas a geração não usa esta parametrização, não serão visualizados nesta lista.

Até o momento, apenas MG, SP, ES, RN, RS, BA, PE, TO, AC, MA, RJ e AL disponibilizaram tabela de códigos específicos.

A lista exibirá apenas os códigos referentes à UF do estabelecimento informado, conforme aparece no quadro acima, exceto quando se tratar de estabelecimento obrigado ao Convênio ICMS 52/2005 (informação essa selecionada no campo “Obrigado ao Convênio ICMS 52/2005” da tela Dados Iniciais do item de menu Parâmetros do módulo da EFD), pois nesse caso deverão ser demonstradas todas as operações de comunicação/telecomunicação devido o estabelecimento possuir inscrição virtual em várias UF’s, então serão demonstrados os códigos: SPDIPAM24, Outras_Entradas_a_Detalhar_por_Municipio e IPM 4.6.

Após exibir o estabelecimento e grupo escolhidos, e o usuário selecionar um tipo de operação, o sistema exibirá no campo “CFOP / Natureza de Operação” a lista dos cfop’s e naturezas disponíveis para cada tipo de operação (*), onde estarão marcados os itens já selecionados anteriormente, quando for o caso.

(*) Conforme descrito na RN04 a lista de CFOP’s a serem disponibilizados para seleção, depende do tipo de operação.

[MFS30891]
Incluir uma observação no final da tela referente ao campo Operação:
“A exibição do conteúdo para o campo Operação dependerá da UF do Estabelecimento selecionado. Apenas os Estabelecimentos cuja UF determina uma forma específica de geração apresentarão conteúdo para o campo. Verifique as orientações específicas de cada UF no Manual do Produto.”



CFOP / Natureza de Operação  Neste campo será demonstrada a lista dos cfop’s / naturezas de operação que poderão ser selecionados pelo usuário.

O tipo dos cfop’s a serem disponibilizados (entrada ou saída), depende do tipo da operação do campo “Operação”, da seguinte forma:



As operações não citadas acima, são as que ainda não estão disponíveis para a geração automática (conforme RN02), e estarão disponíveis apenas na tela de manutenção do registro 1400, para inserção manual dos valores.

Serão demonstradas todas as naturezas de operação associadas aos cfop’s permitidos, dependendo da operação.

Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”, para marcar ou desmarcar todos os cfop’s simultaneamente.




Forma de Cálculo  Este campo é uma lista fixa de opções, utilizado apenas na operação “SPDIPAM22” e “SPDIPAM31”:

Opções do código “SPDIPAM22”:


Opções do código “SPDIPAM31”:



Default: nenhum

O preenchimento é obrigatório para estes códigos, e nesse caso, quando não preenchido a operação não será salva e será exibida a seguinte mensagem de erro:

“Para utilizar o código 22 ou 31 da DIPAM-B a forma de cálculo deverá ser parametrizada para cada CFOP e Natureza”

Como é utilizado apenas para os códigos 22 e 31 de SP, este campo funciona da seguinte forma:

- Quando o estabelecimento não for de SP  nesse caso o campo não aparece na tela (fica invisível);

- Quando o estabelecimento for de SP  nesse caso o campo será apresentado, mas apenas para os códigos 22 e 31;


[MFS42617] Inclusão do parâmetro “Lançar NF Escrituradas”.

Lançar NF Escrituradas  Este campo é uma lista fixa de opções, utilizado apenas na operação “SPDIPAM12”:


Opções do código “SPDIPAM12”:


Default: Não


Como é utilizado apenas para o código 12 de SP, este campo funciona da seguinte forma:

- Quando o estabelecimento não for de SP  nesse caso o campo não aparece na tela (fica invisível);

- Quando o estabelecimento for de SP  nesse caso o campo será apresentado, mas apenas para o código 12;



A opção “Replicar para os estabelecimento” é um checkbox que permite ao usuário replicar a parametrização em questão para outros estabelecimentos, conforme o padrão de diversas telas de parametrização do Mastersaf.

Como default, o campo estará desmarcado na abertura da tela.

Para replicação estarão disponíveis todos os estabelecimentos da empresa do login, que forem da mesma UF do estabelecimento informado.

Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”, para marcar ou desmarcar todos os estabelecimentos.


= = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| OSs4728 OSs4735 | Atendimento:  Resolução 4.730, de 17/12/14, SEF-MG Portaria CAT 137, de Dez/2014, Sefaz-SP | Criação de parametrização de CFOP’s para geração do registro 1400 de acordo com as regras específicas dos estados de MG e SP. | 04/02/2015 (criação do docto) |
| MFS1513 | Portaria N. 34-R, Sefaz-ES | Inclusão dos códigos 01, 02 e 03 para o estado do ES (ver RN03 e RN04) | 08/09/20915 |
| MFS3132 | Orientação Técnica EFD nº 011/2016 – Versão 1.10 | Inclusão dos códigos 3.1, 3.2 e 3.3 para o estado do RN (ver RN03 e RN04) | 16/02/2016 |
| MFS3248 | Orientação Técnica EFD nº 011/2016 – Versão 1.10 | Inclusão dos códigos anuais para o estado do RN (ver RN02 e RN03) | 11/11/2016 |
| MFS8625 | Alteração do 1400 p/o RS | Inclusão dos códigos da tabela do RS (ver RN03 e RN04) | 16/12/2016 |
| MFS16364 | Convênio ICMS 52/05 | Habilitar todas as operações para o estabelecimento obrigado ao Convênio ICMS 52/2005 (Ver RN03). | 23/02/2018 |
| MFS16811 | Alteração do 1400 p/a BA | Inclusão de códigos para o estado da BA (ver RN03 e RN04). | 07/03/2018 |
| MFS17764 | Alteração do 1400 p/o TO | Inclusão de códigos para o estado de TO (ver RN03 e RN04) | 25/04/2018 |
| MFS20147 | Alteração do 1400 p/o RS | Inclusão de código para o estado do RS (ver RN03 e RN04). | 13/08/2018 |
| MFS30891 | Inclusão da observação | Inclusão da observação para o campo Operação. | 09/10/2019 |
| MFS31044 | Alteração do 1400 p/o TO | Inclusão de um código para o estado de TO (ver RN02 e RN03). | 29/10/2019 |
| MFS35133 | Inclusão de códigos | Inclusão dos códigos TOIPME05 e TOIPMS05 para o estado do Tocantis | 22/06/2020 |
| MFS42617 | Alteração do 1400 p/ SP | Inclusão de uma coluna nova para o código 12 da DIPAM-B | 04/09/2020 |
| MFS59468 | Inclusão de código | Inclusão do código PEIPMS0 para o estado de Pernambuco. | 08/02/2021 |
| MFS61948 | Inclusão de códigos | Inclusão dos códigos BAE07, BAE13 e BAE14 para o estado da Bahia. | 19/03/2021 |
| MFS61950 | Inclusão de códigos | Inclusão dos códigos BAE05 e BAS05 para o estado da Bahia. | 01/04/2021 |
| MFS61951 | Inclusão de códigos | Inclusão dos códigos BAE06 e BAS06 para o estado da Bahia. | 07/04/2021 |
| MFS64052 | Inclusão de código | Inclusão do código IPM 3.5 para o estado do Rio Grande do Norte. | 28/04/2021 |
| MFS64779 | Inclusão de código | Inclusão do código PEIPMS4 para o estado de Pernambuco. | 21/05/2021 |
| MFS67705 | Inclusão de código | Inclusão do código PEIPME3 para o estado do Pernambuco. | 29/06/2021 |
| MFS68577 | Inclusão de código | Inclusão do código BAE20 para o estado da Bahia. | 08/07/2021 |
| MFS43147 | Inclusão de código | Inclusão do código ACIPMS04 para o estado do Acre. | 10/08/2021 |
| MFS35318 | Inclusão de código | Inclusão do código TOIPMS10 para o estado de Tocantis. | 18/08/2021 |
| MFS59472 | Inclusão de código | Inclusão do código PEIPMS3 para o estado de Pernambuco. | 23/08/2021 |
| MFS40285 | Inclusão de código | Inclusão do código 06 para o estado de Santa Catarina. | 02/09/2021 |
| MFS35221 | Inclusão de código | Inclusão dos códigos RJVAF20002 e RJVAF20003 para o estado do Rio de Janeiro. | 22/09/2021 |
| MFS47088 | Inclusão de códigos | Inclusão dos códigos MAVAF005, MAVAF006 e MAVAF007 para o estado de Maranhão. | 15/10/2021 |
| MFS86117 | Inclusão de códigos | Inclusão dos códigos RJVAF00006 e RJVAF10006 para o estado do Rio de Janeiro. | 27/05/2022 |
| MFS86203 | Inclusão de código | Inclusão do código IPM 3.6 para o estado do Rio Grande do Norte. | 06/06/2022 |
| MFS94497 | Inclusão de código | Inclusão do código 1201 para o estado de Alagoas. | 20/10/2022 |
| MFS402300 | Inclusão de código | Inclusão dos códigos BAE80 e BAS80 para o estado da Bahia. | 08/03/2023 |
| MFS402301 | Inclusão de código | Inclusão dos códigos BAE81 e BAS81 para o estado da Bahia. | 16/03/2023 |
| MFS547634 | Inclusão de código | Inclusão dos códigos RJVAF00005 e RJVAF10005 para o estado do Rio de Janeiro | 21/07/2023 |
| MFS556958 | Inclusão de código | Inclusão dos códigos RJVAF00009 e RJVAF10009 para o estado do Rio de Janeiro | 07/08/2023 |
| MFS551008 | Inclusão de código | Inclusão dos códigos RJVAF00007 e RJVAF10007 para o estado do Rio de Janeiro | 13/09/2023 |
| MFS663539 | Inclusão de códigos | Inclusão de códigos BAE21... BAE24, BAS21...BAS24 | 30/07/2024 |
| MFS672643 | Inclusão de códigos | Inclusão do código Outras Entradas a Detalhar por Municipio (especifico para 3.6.14) | 17/01/2025 |


| RN00 | Regras Gerais |
| --- | --- |


| RN01 | Campo Estabelecimento: |
| --- | --- |


| RN02 | Campo Grupo Natureza: |
| --- | --- |


| RN03 | Campo Operação: |
| --- | --- |


| Códigos de MG: | Produtos_Agropecuarios |
| --- | --- |
| Códigos de MG: | Transporte_Tomado |
| Códigos de MG: | Cooperativas |
| Códigos de MG: | Prestação_de_Serviço_de_Transporte_Rodoviário |
| Códigos de MG: | Outras_Entradas_a_Detalhar_por_Municipio |
| Códigos de MG: | Outras_Entradas_a_Detalhar_por_Municipio (especifico para 3.6.14) |
| Códigos de SP: | SPDIPAM11 |
| Códigos de SP: | SPDIPAM12 |
| Códigos de SP: | SPDIPAM13 |
| Códigos de SP: | SPDIPAM22 |
| Códigos de SP: | SPDIPAM23 |
| Códigos de SP: | SPDIPAM24 |
| Códigos de SP: | SPDIPAM25 |
| Códigos de SP: | SPDIPAM26 |
| Códigos de SP: | SPDIPAM31 |
| Códigos de SP: | SPDIPAM35 |
| Códigos de SP: | SPDIPAM36 |
| Códigos do ES: | ESIPM01 |
| Códigos do ES: | ESIPM02 |
| Códigos do ES: | ESIPM03 |
| Códigos do RN: | IPM 3.1 |
| Códigos do RN: | IPM 3.2 |
| Códigos do RN: | IPM 3.3 |
| Códigos do RN: | IPM 3.5 |
| Códigos do RN: | IPM 3.6 |
| Códigos do RN: | IPM 4.1 |
| Códigos do RN: | IPM 4.2 |
| Códigos do RN: | IPM 4.3 |
| Códigos do RN: | IPM 4.5 |
| Códigos do RN: | IPM 4.6 |
| Códigos do RN: | IPM 5.1 |
| Códigos do RS: | 01-Transporte |
| Códigos do RS: | 02-Energia Elétrica (Distribuição) |
| Códigos do RS: | 05-Vendas for a do estabelecimento |
| Códigos da BA: | BAE01 |
| Códigos da BA: | BAS01 |
| Códigos da BA: | BAE02 |
| Códigos da BA: | BAS02 |
| Códigos da BA: | BAE03 |
| Códigos da BA: | BAS03 |
| Códigos da BA: | BAE04 |
| Códigos da BA: | BAS04 |
| Códigos da BA: | BAE05 |
| Códigos da BA: | BAS05 |
| Códigos da BA: | BAE06 |
| Códigos da BA: | BAS06 |
| Códigos da BA: | BAE07 |
| Códigos da BA: | BAE13 |
| Códigos da BA: | BAE14 |
| Códigos da BA: | BAE20 |
| Códigos da BA: | BAE80 |
| Códigos da BA: | BAS80 |
| Códigos da BA: | BAE81 |
| Códigos da BA: | BAS81 |
| Códigos da BA: | BAE21 |
| Códigos da BA: | BAS21 |
| Códigos da BA: | BAE22 |
| Códigos da BA: | BAS22 |
| Códigos da BA: | BAE23 |
| Códigos da BA: | BAS23 |
| Códigos da BA: | BAE24 |
| Códigos da BA: | BAS24 |
| Códigos de TO: | TOIPME04 |
| Códigos de TO: | TOIPMS04 |
| Códigos de TO: | TOIPME05 |
| Códigos de TO: | TOIPMS05 |
| Códigos de TO: | TOIPME06 |
| Códigos de TO: | TOIPMS06 |
| Códigos de TO: | TOIPME07 |
| Códigos de TO: | TOIPMS07 |
| Códigos de TO: | TOIPME08 |
| Códigos de TO: | TOIPMS08 |
| Códigos de TO: | TOIPME10 |
| Códigos de TO: | TOIPMS10 |
| Códigos de PE: | PEIPMS0 |
| Códigos de PE: | PEIPMS4 |
| Códigos de PE: | PEIPME3 |
| Códigos de PE: | PEIPMS3 |
| Códigos de AC: | ACIPMS04 |
| Códigos de SC: | 06 |
| Códigos do RJ: | RJVAF20002 |
| Códigos do RJ: | RJVAF20003 |
| Códigos do RJ: | RJVAF00006 |
| Códigos do RJ: | RJVAF10006 |
| Códigos do RJ: | RJVAF00005 |
| Códigos do RJ: | RJVAF10005 |
| Códigos do RJ: | RJVAF00007 |
| Códigos do RJ: | RJVAF10007 |
| Códigos do RJ: | RJVAF00009 |
| Códigos do RJ: | RJVAF10009 |
| Códigos de MA: | MAVAF005 |
| Códigos de MA: | MAVAF006 |
| Códigos de MA: | MAVAF007 |
| Códigos de AL: | 1201 |


| RN04 | Campo CFOP / Natureza de Operação: |
| --- | --- |


| Operação | Operação | CFOP’s a serem exibidos |
| --- | --- | --- |
| UF | Código | CFOP’s a serem exibidos |
| MG | Produtos_Agropecuarios | Apenas os CFOP’s de entrada |
| MG | Transporte_Tomado | Apenas os CFOP’s de saída |
| MG | Cooperativas | Apenas os CFOP’s de saída |
| MG | Prestação_de_Serviço_de_Transporte_Rodoviário | Apenas os CFOP’s de saída |
| MG | Outras_Entradas_a_Detalhar_por_Municipio | Apenas os CFOP’s de saída |
| MG | Outras_Entradas_a_Detalhar_por_Municipio (especifico para 3.6.14) | Apenas os CFOP’s de saída |
| SP | SPDIPAM11 | Apenas os CFOP’s de entrada |
| SP | SPDIPAM12 | Apenas os CFOP’s de entrada |
| SP | SPDIPAM13 | Apenas os CFOP’s de entrada |
| SP | SPDIPAM22 | Entradas e Saídas |
| SP | SPDIPAM23 | Apenas os CFOP’s de saída |
| SP | SPDIPAM24 | Apenas os CFOP’s de saída |
| SP | SPDIPAM25 | Apenas os CFOP’s de saída |
| SP | SPDIPAM26 | Apenas os CFOP’s de entrada |
| SP | SPDIPAM31 | Entradas e Saídas |
| SP | SPDIPAM35 | Apenas os CFOP’s de entrada |
| SP | SPDIPAM36 | Apenas os CFOP’s de entrada |
| ES | ESIPM01 | Apenas os CFOP’s de entrada |
| ES | ESIPM02 | Apenas os CFOP’s de entrada |
| ES | ESIPM03 | Apenas os CFOP’s de entrada |
| RN | IPM 3.1 | Apenas os CFOP’s de entrada |
| RN | IPM 3.2 | Apenas os CFOP’s de saída |
| RN | IPM 3.3 | Apenas os CFOP’s de saída |
| RN | IPM 3.5 | Apenas os CFOP’s de saída |
| RN | IPM 3.6 | Entradas e Saídas |
| RN | IPM 4.1 | Apenas os CFOP’s de saída |
| RN | IPM 4.2 | Apenas os CFOP’s de saída |
| RN | IPM 4.3 | Apenas os CFOP’s de saída |
| RN | IPM 4.5 | Apenas os CFOP’s de saída |
| RN | IPM 4.6 | Apenas os CFOP’s de saída |
| RN | IPM 5.1 | Apenas os CFOP’s de saída |
| RS | 01 | Apenas os CFOP’s de saída |
| RS | 02 | Apenas os CFOP’s de saída |
| RS | 05 | Apenas os CFOP’s de saída |
| BA | BAE01 | Apenas os CFOP’s de entrada |
| BA | BAS01 | Apenas os CFOP’s de saída |
| BA | BAE02 | Apenas os CFOP’s de entrada |
| BA | BAS02 | Apenas os CFOP’s de saída |
| BA | BAE03 | Apenas os CFOP’s de entrada |
| BA | BAS03 | Apenas os CFOP’s de saída |
| BA | BAE04 | Apenas os CFOP’s de entrada |
| BA | BAS04 | Apenas os CFOP’s de saída |
| BA | BAE05 | Apenas os CFOP’s de entrada |
| BA | BAS05 | Apenas os CFOP’s de saída |
| BA | BAE06 | Apenas os CFOP’s de entrada |
| BA | BAS06 | Apenas os CFOP’s de saída |
| BA | BAE07 | Apenas os CFOP’s de entrada |
| BA | BA013 | Apenas os CFOP’s de entrada |
| BA | BA014 | Apenas os CFOP’s de entrada |
| BA | BAE20 | Apenas os CFOP’s de entrada |
| BA | BAE80 | Apenas os CFOP’s de entrada |
| BA | BAS80 | Apenas os CFOP’s de saída |
| BA | BAE81 | Apenas os CFOP’s de entrada |
| BA | BAS81 | Apenas os CFOP’s de saída |
| TO | TOIPME04 | Apenas os CFOP’s de entrada |
| TO | TOIPMS04 | Apenas os CFOP’s de saída |
| TO | TOIPME05 | Apenas os CFOP’s de entrada |
| TO | TOIPMS05 | Apenas os CFOP’s de saída |
| TO | TOIPME06 | Apenas os CFOP’s de entrada |
| TO | TOIPMS06 | Apenas os CFOP’s de saída |
| TO | TOIPME07 | Apenas os CFOP’s de entrada |
| TO | TOIPMS07 | Apenas os CFOP’s de saída |
| TO | TOIPME08 | Apenas os CFOP’s de entrada |
| TO | TOIPMS08 | Apenas os CFOP’s de saída |
| TO | TOIPME10 | Apenas os CFOP’s de entrada |
| TO | TOIPMS10 | Apenas os CFOP’s de saída |
| PE | PEIPMS0 | Apenas os CFOP’s de saída |
| PE | PEIPMS4 | Apenas os CFOP’s de saída |
| PE | PEIPME3 | Apenas os CFOP’s de saída |
| PE | PEIPMS3 | Apenas os CFOP’s de saída |
| AC | ACIPMS04 | Apenas os CFOP’s de saída |
| SC | 06 | Apenas os CFOP’s de saída |
| RJ | RJVAF20002 | Apenas os CFOP’s de entrada |
| RJ | RJVAF20003 | Apenas os CFOP’s de saída |
| RJ | RJVAF00006 | Apenas os CFOP’s de entrada |
| RJ | RJVAF10006 | Apenas os CFOP’s de saída |
| RJ | RJVAF00005 | Apenas os CFOP’s de entrada |
| RJ | RJVAF10005 | Apenas os CFOP’s de saída |
| RJ | RJVAF00007 | Apenas os CFOP’s de entrada |
| RJ | RJVAF10007 | Apenas os CFOP’s de saída |
| RJ | RJVAF00009 | Apenas os CFOP’s de entrada |
| RJ | RJVAF10009 | Apenas os CFOP’s de saída |
| MA | MAVAF005 | Apenas os CFOP’s de saída |
| MA | MAVAF006 | Apenas os CFOP’s de saída |
| MA | MAVAF007 | Apenas os CFOP’s de entrada |
| AL | 1201 | Apenas os CFOP’s de saída |


| RN05 | Campo Forma de Cálculo: |
| --- | --- |


| Base de Cálculo ICMS Normal |
| --- |
| Base de Cálculo ICMS Substituição Tributária |
| Valor Total NF – Revendedor Autônomo |


| Base de Cálculo ICMS Normal |
| --- |
| Valor Total NF – Revendedor Autônomo |


| RN05 | Campo Lançar NF Escrituradas: |
| --- | --- |


| Sim |
| --- |
| Não |


| RN07 | Campo Replicar para os estabelecimentos: |
| --- | --- |

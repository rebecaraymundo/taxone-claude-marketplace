# MTZ_EFD_Parametros_Ressarcimento_ICMSST_Saida_CFOP

> Fonte: MTZ_EFD_Parametros_Ressarcimento_ICMSST_Saida_CFOP.docx






THOMSON REUTERS

Módulo Sped Fiscal

Parametrização de CFOP com Direito à Restituição


Localização: Menu Sped, Módulo: Escrituração Fiscal Digital  Parâmetros  Ressarcimento ICMS-ST  Saídas com Direito à Restituição  CFOP
Menu Sped, Módulo: Escrituração Fiscal Digital  Parâmetros  Ressarcimento ICMS-ST  Operações  CFOP



DOCUMENTO DE REQUISITO

Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2




## Regras Gerais



Os dados parametrizados neste item (Módulo: Escrituração Fiscal Digital  Parâmetros  Ressarcimento ICMS-ST  Operações  CFOP) são utilizados na rotina de pré-geração para os registros de Ressarcimento de ICMS-ST, realizada no menu “Pré-Geração  Ressarcimento ICMS-ST (Específico MG)” do módulo Sped Fiscal. Esta parametrização será utilizada na geração dos registros com direito à restituição de ICMS-ST (C180, C185, C186, C330, C430).

Esta parametrização foi criada como cópia da existente no módulo Estadual / Meio Magnético / Parâmetros / Minas Gerais / Estoque de Produtos ICMS-ST (88STEST e 88STITNF)/ Saídas com Direito à Restituição / CFOP, onde os CFOPs parametrizados são gravados na tabela PRT_CFO_MSAF com o código parâmetro = 443.

[MFS70215] Inclusão da opção de devolução de entrada interestadual
[MFS73772] Inclusão da opção de entrada (e devolução)

Com a MFS-47079, esta tela passa a traballhar com uma lista de Operações. Veja:
- Saída Interna para Consumidor Final (art 31-A - Anexo XV do RICMS/02) - Código parâmetro = 766
- Saída para Outras Unidade da Federação  (art 23 - Anexo XV do RICMS/02) - Código parâmetro = 767
- Saída com Isenção ou não Incidência (art 23 - Anexo XV do RICMS/02) - Código parâmetro = 768
- Perecimento, Furto, Roubo ou qualquer outro Tipo de Perda (art 23 - Anexo XV do RICMS/02) - Código parâmetro = 769
- Devolução de Entrada Interestadual - Código parâmetro = 815
- Entrada (e Devolução) - Código parâmetro = 824


Cada operação acima é um código de parâmetro novo.  Portanto, deixamos de utilizar o código parâmetro 443 oriundo da tela do módulo Meio Magnético (Estoque de Produtos ICMS-ST (88STEST e 88STITNF)/ Saídas com Direito à Restituição). Para não exigir que os clientes refaçam a parametrização de CFOP já gravadas na PRT_CFO_MSAF com o código parâmetro 443, vamos criar um sprint na MFS-47079 para copiar essa parametrização para o novo código da operação “Saída Interna para Consumidor Final (art 31-A - Anexo XV do RICMS/02)”.



## Layout da Tela







Botões da barra de menu:



## Regras de Funcionamento dos Campos






Ao salvar os dados será feita a seguinte verificação:

RN01 – CFOP já parametrizado para outra operação:

O CFOP a ser incluído não pode constar na parametrização de outra operação (campo “Operação”).

Quando ocorrer esta situação, a inclusão será efetuada apenas para os CFOP’s “corretos” (não parametrizados para outra operação).

Os CFOP’s inválidos não serão incluídos, e será exibida a seguinte mensagem:

“O CFOP XXXX já foi parametrizado para outra operação”

Onde “XXXX” é o código do CFOP inválido.

OBS: Caso existam vários CFOP’s inválidos a mensagem deve exibir o código de apenas um deles, já que não haveria como mostrar todos simultaneamente.


= = = = = =



| MFS | Descrição | Nome | Data |
| --- | --- | --- | --- |
| MFS-33977 | Criação da parametrização de CFOP para as Saídas com Direito à Restituição de ICMS-ST. | Alessandra Cristina Navatta | 13/03/2020 |
| MFS-47079 | Inclusão do campo Operação sendo uma lista com quatro opções: - Saída Interna para Consumidor Final (art 31-A - Anexo XV do RICMS/02) - Saída para Outras Unidade da Federação  (art 23 - Anexo XV do RICMS/02) - Saída com Isenção ou não Incidência (art 23 - Anexo XV do RICMS/02) - Perecimento, Furto, Roubo ou qualquer outro Tipo de Perda (art 23 - Anexo XV do RICMS/02) | Liliane Assaf | 01/12/2020 |
| MFS70215 | Inclusão de um novo tipo de operação: Devolução de Entrada Interestadual. | Andréa Rocha | 20/08/2021 |
| MFS73772 | Inclusão de um novo tipo de operação: Entrada (e Devolução).  Alterar a descrição do item de menu, pois deixarão de ser parametrizadas somente as operações de saída, conforme a informação na localização do menu acima. | Andréa Rocha | 05/10/2021 |


| CONFIRMA | Opção para salvar as informações da parametrização do estabelecimento e operação. |
| --- | --- |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S |  | Este campo é uma lista dos estabelecimentos de MG, da empresa do login para seleção do usuário.  Quando for informado um estabelecimento de MG no login, o campo mostrará fixo este estabelecimento, e usuário não poderá alterá-lo. |  |
| Operações | Alfanumérico | S | S | Listbox | Este campo é uma lista com as seguintes opções para seleção do usuário:  [MFS70215] Inclusão da opção de devolução de entrada interestadual [MFS73772] Inclusão da opção de entrada (e devolução)  Saída Interna para Consumidor Final (art 31-A - Anexo XV do RICMS/02) Saída para Outras Unidade da Federação  (art 23 - Anexo XV do RICMS/02) Saída com Isenção ou não Incidência (art 23 - Anexo XV do RICMS/02) Perecimento, Furto, Roubo ou qualquer outro Tipo de Perda (art 23 - Anexo XV do RICMS/02) Devolução de Entrada Interestadual Entrada (e Devolução) | MFS47079 MFS70215 MFS73772 |
| CFOP’s | Alfanumérico | S | S |  | Neste campo é exibida a lista dos CFOP’s (SAFX2012) para seleção do usuário.  Quando existir mais de uma ocorrência do mesmo CFOP, com  validades diferentes, será considerado para exibição apenas o registro de maior data de validade (para não exibir códigos repetidos).  Como facilitador, poderão ser utilizados os botões “Selecionar todos”, “Desmarcar todos”, “Marcar Entradas”, Desmarcar Entradas, Marcar Saídas e Desmarcar Saídas.  Ver abaixo (RN01) a crítica efetuada ao salvar a operação. |  |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados.  Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado.  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |

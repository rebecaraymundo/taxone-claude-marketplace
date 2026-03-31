# MTZ_EFD_Parametros_Ressarcimento_ICMSST_Saida_Natureza_Operacao

> Fonte: MTZ_EFD_Parametros_Ressarcimento_ICMSST_Saida_Natureza_Operacao.docx






THOMSON REUTERS

Módulo Sped Fiscal

Parametrização de Natureza de Operação com Direito à Restituição


Localização: Menu Sped, Módulo: Escrituração Fiscal Digital  Parâmetros  Ressarcimento ICMS-ST  Saídas com Direito à Restituição  Natureza de Operação
Menu Sped, Módulo: Escrituração Fiscal Digital  Parâmetros  Ressarcimento ICMS-ST  Operações  Natureza de Operação

DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2




## Regras Gerais



Os dados parametrizados neste item (Módulo: Escrituração Fiscal Digital  Parâmetros  Ressarcimento ICMS-ST  Operações  Natureza de Operação) são utilizados na rotina de pré-geração para os registros de Ressarcimento de ICMS-ST, realizada no menu “Pré-Geração  Ressarcimento ICMS-ST (Específico MG)” do módulo Sped Fiscal. Esta parametrização será utilizada na geração dos registros de saída com direito à restituição de ICMS-ST (C180, C185, C186, C330, C430).

Esta parametrização foi criada como cópia da existente no módulo Estadual / Meio Magnético / Parâmetros / Minas Gerais / Estoque de Produtos ICMS-ST (88STEST e 88STITNF)/ Saídas com Direito à Restituição / Natureza de Operação, onde os CFOPs/Naturezas de Operação parametrizados são gravados na tabela PRT_EXTCFO_MSAF com o código parâmetro = 443.

[MFS70215] Inclusão da opção de devolução de entrada interestadual
[MFS73772] Inclusão da opção de entrada (e devolução)

Com a MFS-47079, esta tela passa a traballhar com uma lista de Operações. Veja:
- Saída Interna para Consumidor Final (art 31-A - Anexo XV do RICMS/02) - Código parâmetro = 766
- Saída para Outras Unidade da Federação  (art 23 - Anexo XV do RICMS/02) - Código parâmetro = 767
- Saída com Isenção ou não Incidência (art 23 - Anexo XV do RICMS/02) - Código parâmetro = 768
- Perecimento, Furto, Roubo ou qualquer outro Tipo de Perda (art 23 - Anexo XV do RICMS/02) - Código parâmetro = 769
- Devolução de Entrada Interestadual - Código parâmetro = 815
- Entrada (e Devolução) - Código parâmetro = 824


Cada operação acima é um código de parâmetro novo.  Portanto, deixamos de utilizar o código parâmetro 443 oriundo da tela do módulo Meio Magnético (Estoque de Produtos ICMS-ST (88STEST e 88STITNF)/ Saídas com Direito à Restituição). Para não exigir que os clientes refaçam a parametrização de Natureza de Operação já gravadas na PRT_EXTCFO_MSAF com o código parâmetro 443, vamos criar um sprint na MFS-47079 para copiar essa parametrização para o novo código da operação “Saída Interna para Consumidor Final (art 31-A - Anexo XV do RICMS/02)”.


## Layout da Tela







Botões da barra de menu:



## Regras de Funcionamento dos Campos





Ao salvar os dados será feita a seguinte verificação:

RN01 – CFOP/Natureza já parametrizado para outra operação:

O CFOP/Natureza a ser incluído não pode constar na parametrização de outra operação (campo “Operação”).

Quando ocorrer esta situação, a inclusão será efetuada apenas para os CFOP’s/Naturezas “corretos” (não parametrizados para outra operação).

Os CFOP’s/Naturezas inválidos não serão incluídos, e será exibida a seguinte mensagem:

“O CFOP/Natureza XXXX-XXX  já foi parametrizado para outra operação”

Onde “XXXX-XXX” é o código do CFOP/Natureza inválido.

OBS: Caso existam vários CFOP’s/Naturezas inválidos a mensagem deve exibir o código de apenas um deles, já que não haveria como mostrar todos simultaneamente.



= = = = = =


| MFS | Descrição | Nome | Data |
| --- | --- | --- | --- |
| MFS-33977 | Criação da parametrização de Natureza de Operação para as Saídas com Direito à Restituição. | Alessandra Cristina Navatta | 13/03/2020 |
| MFS-47079 | Inclusão do campo Operação sendo uma lista com quatro opções: - Saída Interna para Consumidor Final (art 31-A - Anexo XV do RICMS/02) - Saída para Outras Unidade da Federação  (art 23 - Anexo XV do RICMS/02) - Saída com Isenção ou não Incidência (art 23 - Anexo XV do RICMS/02) - Perecimento, Furto, Roubo ou qualquer outro Tipo de Perda (art 23 - Anexo XV do RICMS/02) | Liliane Assaf | 01/12/2020 |
| MFS70215 | Inclusão de novo tipo de operação: Devolução de Entrada Interestadual | Andréa Rocha | 20/08/2021 |
| MFS73772 | Inclusão de um novo tipo de operação: Entrada (e Devolução).  Alterar a descrição do item de menu, pois deixarão de ser parametrizadas somente as operações de saída, conforme a informação na localização do menu acima. | Andréa Rocha | 05/10/2021 |


| CONFIRMA | Opção para salvar os dados informados para a parametrização do estabelecimento e operação. |
| --- | --- |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S |  | Este campo é uma lista dos estabelecimentos de MG, da empresa do login para seleção do usuário.  Quando for informado um estabelecimento de MG no login, o campo mostrará fixo este estabelecimento, e usuário não poderá alterá-lo. |  |
| Operações | Alfanumérico | S | S | Listbox | Este campo é uma lista com as seguintes opções para seleção do usuário:  [MFS70215] Inclusão da opção de devolução de entrada interestadual [MFS73772] Inclusão da opção de entrada (e devolução)  Saída Interna para Consumidor Final (art 31-A - Anexo XV do RICMS/02) Saída para Outras Unidade da Federação  (art 23 - Anexo XV do RICMS/02) Saída com Isenção ou não Incidência (art 23 - Anexo XV do RICMS/02) Perecimento, Furto, Roubo ou qualquer outro Tipo de Perda (art 23 - Anexo XV do RICMS/02) Devolução de Entrada Interestadual Entrada (e Devolução) | MFS47079 MFS70215 MFS73772 |
| CFOP / Natureza de Operação | Alfanumérico | S | S |  | Neste campo é exibida a lista da combinação CFOP + Natureza de Operação da tabela SAFX2081, para seleção do usuário.  Os critérios para filtro dos dados da SAFX2081 são:  CFOP - tanto os CFOP’s de entrada como de saída, para que o usuário informe os CFOP’s da operação principal e também de suas devoluções;  Natureza de Operação - serão consideradas apenas as Natureza do GRUPO escolhido pelo usuário;  Como facilitador, poderá ser utilizado o botão “Marcar todos” que marca ou desmarca todos os CFOP’s/Naturezas simultaneamente.  Ver abaixo (RN01) a crítica efetuada ao salvar a operação. |  |
| Replicar para os Estabelecimentos | Alfanumérico | N | S |  | Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados.  Serão exibidos para seleção apenas os estabelecimentos da mesma empresa do estabelecimento parametrizado.  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. |  |

# MTZ_EFD_Manutencao_Registro_1400_Inf_Valores_Agregados

> Fonte: MTZ_EFD_Manutencao_Registro_1400_Inf_Valores_Agregados.doc

Módulo Sped Fiscal – Manutenção do Registro 1400
(Informação de Valores Agregados)


Localização: Menu SPED, Módulo EFD – Escrituração Fiscal Digital, item Geração ( Manutenção ( Registro 1400 

DOCUMENTO DE REQUISITO

DR	Nome	Descrição	Data Alteração		OS4728
OS4735	Atendimento a:
Resolução 4.730/14, SEF-MG e 
Portaria CAT 137, de Dez/2014, Sefaz-SP	Criação do campo “Código da Tabela de Itens p/o Índice de Participação dos Municípios” (ver RN01)	05/02/2015
(Criação do docto) 		CH14943_2015	Alteração do campo Município para Ajustes SPDIPAM31, SPDIPAM35 ou SPDIPAM36	Este documento tem como objetivo alterar o tratamento do campo município para os ajustes SPDIPAM31, SPDIPAM35 ou SPDIPAM36 (ver RN02).	22/07/2015		MFS-15153	Inclusão dos campos de valores calculados para o Convênio 52/05	Este documento tem como objetivo incluir o grupo “Valores Conv. ICMS 52/05” para levar os valores apurados e as deduções de acordo com o Convênio 52/05 (ver RN03).	29/01/2018		MFS-17077	Alteração do campo Valor Total específico para estabelecidos na Bahia	Este documento tem como objetivo alterar o tratamento do campo Valor Total especificamente aos estabelecidos na unidade federada da Bahia (ver RN04). 	24/04/2018		MFS577274	Alteração para contemplar a nova tabela IPM 5.9.2.	Inclusão dos campos UF e tabela IPM e impacto nas regras dos campos já existentes: Município, Produto e “Código da Tabela de Itens UF e UF-ST p/ o Índice de Participação dos Municípios”	17/11/2023		
LAYOUT DA TELA


     Estabelecimento:  [xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx]

     Período:                 [99/99/9999]  a  [99/99/9999]

     UF:                         [      \/]

     Município:               [        ]  [                                                                                          ]

     Produto (Ind/Cód):  [    ]  [                                                        ]
                                      [                                                                                                     ]
     Tabela p/ IPM:         (o) 5.9.1          ( ) 5.9.2
     Código da Tabela de Itens UF e UF-ST p/ o Índice de Participação dos Municípios:
     [                                                                                                            \/]

     Valores Calculados:
     
     Valor Apurado:         [                                     ]
      Deduções:                [                                     ]                

     Valores Conv ICMS 52/05:
     
     Valor Apurado:         [                                     ]
      Deduções:                [                                     ]     
    
      Valores Informados:

      Outros Valores:       [                                     ]
      Outras Deduções:    [                                     ]

      Valor Total:              [                                     ] 

  
 		


REGRAS DE NEGÓCIO


Regra 	Descrição	DR		RN00	
Regras gerais

(espaço reservado para regras genéricas, que não dizem respeito a campos específicos)

Só poderá ser informado um registro por Empresa, Estabelecimento, Período, UF/Município, Produto e Código da Tabela de Itens”

Por isso, quando este campo for preenchido, será feita a seguinte crítica antes de salvar a operação:

Caso já exista registro para a mesma Empresa, Estabelecimento, Período, UF/Município, Produto e Código da Tabela de Itens, o registro não será salvo e será exibida uma mensagem de erro informando que já existe registro com a chave informada (mensagem padrão de registro já existente).
		RN01	Campo Estabelecimento
Campo obrigatório.
Funcionamento padrão (exibir o Estabelecimento informado no login,ou a lista dos Estabelecimentos da Empresa, caso o Estabelecimento não tenha sido informado no login). O Estabelecimento informado deve ter a UF preenchida no seu cadastro. Caso não tenha, deve ser dada a seguinte mensagem:
 
Estabelecimento sem UF preenchida. A informação da UF do estabelecimento é pré-requisito para a manutenção do registro 1400.

                                                 <OK>


A mensagem vale tanto nos casos do estabelecimento “fixo” (por ter sido informado no login), como para o caso em que o usuário escolhe um estabelecimento na lista.

		RN02	Campo Período 
Campo obrigatório.
Período da geração do Sped Fiscal
		RN03	Campo UF
Campo obrigatório.
Lista dos Códigos das Unidades Federativas oriundos da tabela ESTADO (TFIX04).
A Lista é composta pelos códigos das UF’s considerando:
- UF do Cadastro do Estabelecimento;
- UF’s das Inscrições Estaduais do Estabelecimento (menu “Preliminares >> Inscrições Estaduais” do módulo Parâmetros). Tabela REGISTRO_ESTADUAL

Ao salvar o registro, caso o campo não esteja preenchido, a operação não será salva e será exibida a mensagem: “UF é campo mandatório”	MFS577274		RN04	Campo Município
Campo obrigatório. 
MFS577274: Município passa a depender da UF selecionada na lista e não mais da UF do Estabelecimento:
Trabalhar com janela de seleção da tabela de municípios do IBGE, exibindo apenas os municípios da UF do Estabelecimento selecionada na lista descrita na RN03.

Alteração do CH14943_2015: 
O município deve ser preenchido automaticamente com o Município do Estabelecimento, quando o campo “Código da Tabela de Itens p/ o Índice de Participação dos Municípios” for preenchido com uma das seguintes opções SPDIPAM31, SPDIPAM35 ou SPDIPAM36 e a UF selecionada na lista for a UF do Estabelecimento.

Assim, antes de salvar a operação, serão feitas as seguintes críticas em relação ao preenchimento do município:

Se o campo “Código da Tabela de Itens p/o Índice de Participação dos Municípios” estiver preenchido com um dos seguintes códigos “SPDIPAM31” ou “SPDIPAM35” ou “SPDIPAM36” e a UF selecionada na lista for a UF do Estabelecimento, então:

Gravar concatenando a informação da UF+Cód. Município do Estabelecimento.

Se o campo “Código da Tabela de Itens p/o Índice de Participação dos Municípios” não preenchido, ou preenchido com um código diferente dos três códigos citados acima, ou UF for diferente da UF do Estabelecimento, então:

      Nesse caso o município é obrigatório, e quando não informado, a operação não será salva e será exibida a mensagem: “Município é campo mandatório”

	MFS577274		RN05	Campo Produto
MFS577274: Produto passa a ser habilitado apenas para UF do Estabelecimento:
Campo de preenchimento não obrigatório. 
Trabalhar com janela de seleção de dados da Tabela de Produtos (SAFX2013).
Este campo deve estar disponível apenas quando o parâmetro “Calcular Valores por Produto” (do menu “Parâmetros ( Dados Iniciais”) estiver marcado e a UF selecionada na lista for a UF do Estabelecimento. Caso contrário deve-se limpar e bloquear o campo.	MFS577274		RN06	Campo Tabela IPM
Campo de preenchimento não obrigatório. 
Radio Button com as seguintes opções:
5.9.1 
5.9.2
Este campo depende da UF selecionada na lista.
Se a UF selecionada for a UF do Estabelecimento, então habilita as duas opções 5.9.1 e 5.9.2, Default é a opção 5.9.1.
Se a UF selecionada for diferente da UF do Estabelecimento, então desabilita e marca a opção 5.9.2.

Quando um registro estiver sendo consultado na tela (botão abre), apresentar marcada a opção da tabela ao qual o Código IPM pertence. Vide TACES89 - Códigos dos Itens de Participação dos Municípios (PRT_COD_PART_MUN_EFD – campo COD_TABELA).	MFS577274		RN07	Campo “Código da Tabela de Itens UF e UF-ST p/o Índice de Participação dos Municípios”:
  
Campo incluído pela OS4728, em Fev/2015
MFS577274: Lista de códigos passa a depender da tabela IPM (RN06) e da UF selecionada na lista de UF’s (RN03) e não mais da UF do Estabelecimento 

O campo é de preenchimento não obrigatório.
Default ( <branco> 

Este campo será utilizado para informar um código da tabela “Tabela de Itens p/o Índice de Participação dos Municípios” da EFD, onde cada UF disponibiliza seus códigos específicos.

Neste campo será exibida a lista dos códigos referentes à UF do município informado (campo “Município”) selecionada na lista descrita na RN03 e à opção de tabela 5.9.1 ou 5.9.2 selecionada (RN06). 

Os códigos apresentados são carregados pela TACES89 (Códigos dos Itens de Participação dos Municípios – Sped Fiscal) – tabela PRT_COD_PART_MUN_EFD. 

O campo fica habilitado sempre, e na lista serão exibidos apenas os códigos referentes à UF selecionada no campo UF e ao Código de Tabela IPM + opção “branco”. Para isso, os códigos da TACES serão filtrados pelos campos “UF” e “Tabela IPM”.
	


OS4728
OS4735
MFS577274		RN08	Grupo Valores Calculados:
Grupo composto pelos seguintes campos:
     Valor Apurado
      Deduções   
	


OS4735		RN09	Grupo “Valores Conv. ICMS 52/05”:

O grupo Valores Conv. ICMS 52/05 deve compor os campos:
Valor Apurado 
Deduções

Esses campos deverão ser apresentados abaixo do grupo “Valores Calculados” no formato 0,00 e desbloqueados por default, pois só serão preenchidos quando executada a pré-geração da rotina Registro 1400 – Conv. ICMS 52/05 do item de menu Pré-Geração e quando houver dados.	MFS-15153		RN10	Grupo Valores Informados:
Grupo composto pelos seguintes campos:
      Outros Valores
      Outras Deduções		RN11	Campo “Valor Total”:

Exibir o valor adicionado final, resultante dos valores calculados e dos valores informados manualmente, da seguinte forma:

“Valor Apurado – Deduções + Outros Valores – Outras Deduções”

[ALTERADA – MFS-17077]
Tratamento:
Se o estabelecimento selecionado no campo “Estabelecimento” for de unidade federada igual a BA, o campo “Valor Total” não deverá ser recalculado quando o campo “Código da Tabela de Itens p/o Índice de Participação dos Municípios” for igual a 01, 02, 03 ou 04, o usuário deverá refazer o cálculo por ser um rateio que envolve a porcentagem dos valores em relação às saídas.	MFS-17077
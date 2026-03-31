# Tela_Entrada_Manual_de_Valores

> Fonte: Tela_Entrada_Manual_de_Valores.doc

THOMSON REUTERS

Tela de Entrada Manual de Valores 
ECF - Escrituração Contábil Fiscal (DW)


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		01/11/2017	MFS-14487	Criação do Documento.	Alessandra Cristina Navatta		20/02/2018	MFS-12695	Inclusão de regra dos registros N620 e N660	Alessandra Cristina Navatta		06/03/2018	MFS-17047	Inclusão do filtro Visão por Tipo de Receita 
Demonstrar na tela as linhas do tipo CNA (desabilitadas para edição)	Alessandra Cristina Navatta		19/03/2018	MFS-17180	Inclusão de filtro Status (no botão Abre)	Alessandra Cristina Navatta		03/04/2018	MFS-17658	Liberado o modal de percentual de receita bruta, linha 2 dos registros N500/N650	Alessandra Cristina Navatta		28/05/2018	MFS-18704	Excluir os valores calculados no PAT, se existir ajuste manual na linha 9 do registro N620 ou linha 8 do registro N630. 	Alessandra Cristina Navatta		




Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc511209866" 1.	INTRODUÇÃO	 PAGEREF _Toc511209866 \h 3
 HYPERLINK \l "_Toc511209867" 2.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc511209867 \h 3
 HYPERLINK \l "_Toc511209868" 3.	TELA/MODAIS	 PAGEREF _Toc511209868 \h 3
 HYPERLINK \l "_Toc511209869" 3.1 Pesquisa de Registros	 PAGEREF _Toc511209869 \h 3
 HYPERLINK \l "_Toc511209870" 3.2	Regras dos Campos Tela Principal	 PAGEREF _Toc511209870 \h 5
 HYPERLINK \l "_Toc511209871" 3.3	Modais	 PAGEREF _Toc511209871 \h 18


INTRODUÇÃO

Objetivo desta especificação é criar uma tela que permita a entrada manual de valores diretamente nas linhas das tabelas dinâmicas processadas pela rotina de processamento em lote.

DOCUMENTOS DE REFERÊNCIA
Mensagens_Sistema_DWECF.xlsx
Regras_Gerais_DWECF.docx
MTZ_Processamento_em_Lote.docx
Tela_ Abertura_ de_ Apuracao.doc

TELA/MODAIS

3.1 Pesquisa de Registros

Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Apuração>> Ajustes Manuais>> Entrada Manual de Valores

Título da tela: Entrada Manual de Valores 

Condições Gerais: Quando o usuário acessar a tela de consulta, apresentar todos os registros contidos na tabela de abertura da apuração.
 
Obs. As opções dos campos de pesquisa e suas opções, podem ter alguma divergência na escrita e tipo, pois serão apresentados como cadastradas no banco.

Campo	Tipo	Regra		Estabelecimento	LOV
(Tipo - Código – Descrição)	Permite que o usuário busque o registro pelo Código do Estabelecimento.		Exercício	Texto
(AAAA)
	O usuário poderá informar o exercício. 


		Data Inicial	Data
DD/MM/AAAA	O usuário poderá informar a data inicial da Informação ECF.		Versão	Lista
(Código -Descrição)	Aplicar a RNG00004-Versão de Layout		Forma de Tributação	Lista
(Código -Descrição)	Exibe as opções abaixo:

- Lucro Real
- Lucro Presumido,
-Lucro Arbitrado
-Imune de IRPJ 
-Isento do IRPJ 		Apuração	Lista
(Código -Descrição)	Exibe as opções abaixo:

- Anual
- Trimestral
		Período de Apuração	Lista
(Código -Descrição)	Selecionar um item da lista.

Para apuração igual a Anual, exibir o conteúdo abaixo: 
- Janeiro
- Fevereiro
- Março
- Abril
- Maio
- Junho
- Julho
- Agosto
- Setembro
- Outubro
- Novembro
- Dezembro

Para apuração igual a trimestral, exibir o conteúdo abaixo:
- 1º Trimestre 
-  2º Trimestre
 - 3º Trimestre
 - 4º Trimestre		Status	Lista
(Código)	Exibe a lista de Status:

- Importação dos Saldos Realizada- Cálculo Realizado- Reapurar- Alteração Manual Realizada- Aguardando Alteração Manual

		
Regras dos Campos Tela Principal

Localização da tela: ECF - Escrituração Contábil Fiscal >> Apuração>> Ajustes Manuais>> Entrada Manual de Valores

Título da tela: Entrada Manual de Valores 

Recuperar apenas as aberturas com status diferente de “Apuração em Aberto” e A00.

Permitir edição do registro apenas quando o status da abertura de apuração correspondente ao registro for diferente de “Aguardando Alteração Manual” e “Cálculo Realizado”. Caso contrário, aplicar a RNG00018 - Alteração de tela com controle de status da abertura da apuração. 

Recuperar todas as linhas do registro que são diferentes do tipo R (rótulo). As linhas do tipo CNA (cálculo não alterável), não devem ficar habilitadas para edição, as demais que forem recuperadas devem ser habilitadas para edição.

Para os registros N630 e N670 com Apuração Anual, exibir o último período processado. Se o usuário inserir uma entrada manual em uma abertura e depois processar um novo período (dentro desta escrituração), a entrada manual realizada anterior será desprezada. Só será mantida os dados do último período. 

Para os registros N620 e N660, aplicar RNG00048 – Registros N620 e N660.

Se houver ajuste manual na linha 9 do registro N620, ou linha 8 do registro N630, desconsiderar todos os valores calculados para o PAT (RNC018, RNC19 e RNC20, do documento MTZ_Processamento_em_Lote.docx), inclusive o valor utilizado no período e de períodos anteriores. Vale ressaltar que o PAT utilizado dos períodos anteriores (calculado neste período) deve voltar para o período anterior.

As regras destacadas em amarelo (e com fonte vermelha), não serão implementadas neste momento.


Campo	Tipo	Obrig	Ed	Formato/Default	Regra	MFS		Fechar	Botão	-	-	-	Permite que o usuário inclua/altera as informações.

Tratamentos:

 - Aplicar a RNG00012 - Salvar
  
Após a edição dos valores nesta tela, o status da abertura da apuração deve ser alterado para “Alteração Manual Realizada”.
	MFS-14487		Mensagem Explicativa fixa na tela(*)	Texto	S	N	-	Após efetuar e salvar qualquer alteração nesta tela será necessário refazer a execução do cálculo no Processamento em Lote, para que as atualizações dos registros tenham efeito nos resultados da apuração.	MFS-14487		DADOS GERAIS
As informações são referentes ao registro selecionado na Abertura de Apuração. (*)
		Estabelecimento
	Texto
	S	N		Permite que o usuário visualize o Estabelecimento da apuração que foi recuperada	MFS-14487		Exercício	Texto
	S	N		Permite que o usuário visualize o exercício.	MFS-14487		Data Inicial	Texto
	S	N		Permite que o usuário visualize a data inicial 

	MFS-14487		Versão	Texto	S	N		Permite que o usuário visualize a Versão do Layout utilizada para o processamento do registro.

Valores válidos:

Aplicar RNG00004 - Versão de Layout.	MFS-14487		Forma de Tributação	Texto
	S	N		Permite que o usuário visualize a forma de tributação.
	MFS-14487		Apuração	Texto
	S	N		Permite que o usuário visualize a Apuração.	MFS-14487		Período de Apuração	Texto	S	N	-	Permite que o usuário visualize o período de apuração.	MFS-14487		ENTRADA MANUAL PARA OS REGISTROS PROCESSADOS		Apenas Registros Alterados	Check-box	S	S	Desmarcado	Permite que o usuário selecione a forma de visualização dos registros na grid. 

Tratamentos:

Se desmarcado, todos os registros serão exibidos na grid. Se marcado, apenas os registros com entrada manual e os que foram descartados, serão exibidos.

	

MFS-14487		Visão por Tipo de Receita	Lista	N	S	 Balanço de Suspensão/Redução 	Permite que o usuário visualize/altere as informações do registro por tipo de receita.


Tratamentos:

Opções Válidas:
Receita Bruta
Balanço de Suspensão/Redução 


Só demonstrar esse campo se a opção ‘Não se Aplica’, não estiver selecionada no campo tipo de receita da tela de Abertura de apuração.

Para as condições acima, apresentar este campo habilitado e possível de alteração se:

Na tela “Abertura da Apuração” o usuário optar por tipo de receita “Comparativo” e não efetuar a escolha por um tipo de receita (seja por meio da Tela “Comparativo entre Receita Bruta X Balanço de Suspensão/Redução”, ou pelo parâmetro “Considerar automaticamente o menor valor de imposto no comparativo”).

Se for definido um tipo de receita, mostrar este campo desabilitado com a opção escolhida selecionada (seja na tela de abertura pelo campo tipo de receita, pelo parâmetro “Considerar automaticamente o menor valor de imposto no comparativo” ou pela tela do comparativo).

Para os registros N620 e N660:

Quando o usuário escolher a opção “Receita Bruta”, atualizar a grid dos Registros N620 e/ou N660, considerando os valores correspondente ao tipo de receita “Receita Bruta”.

Quando o usuário escolher a opção “Balanço de Suspensão/Redução”, atualizar a grid dos Registros N620 e/ou N660 considerando os valores correspondente ao tipo de receita “Balanço de Suspensão/Redução”.

- Quando o usuário fizer a opção por um tipo de receita no período através da tela de “Comparativo entre Receita Bruta X Balanço de Suspensão/Redução”, ou marcar a opção “Considerar automaticamente o menor valor de imposto no comparativo”, este campo deve ficar desabilitado, com a escolha definida e devem ser demonstradas as informações do registro conforme o tipo de receita escolhido pelo usuário.

	MFS- 17047		Botões (*)		Importar Valores de um Arquivo	Botão	-	-	Habilitado	Permite que o usuário faça o upload de um arquivo txt, cujos valores serão atualizados na grid.

Tratamentos:

Esta funcionalidade só estará disponível, se a importação de saldos foi realizada.

Aplicar a regra de negócio geral <<RNG00263>>.

Validações:
Duplicidade de registros somente quando o dado está duplicado no arquivo(RNG00004), 
Campos Obrigatórios (RNG00003)
Validação de valores nos campos (RNG00011)
Validação de cadastros correspondentes (RNG00021)
Validação de campos numéricos (RNG00030)
Validação de tamanho de campo (RNG00032)
Validação de conteúdo de data (RNG00033)
Considerar a versão da tabela dinâmica, utilizada na apuração que está sendo incluídos os registros. Caso, não seja identificado a linha correspondente na tabela, exibir a seguinte msg TR00715 (Código, Descrição).

Não deve ser aceito os registros do Bloco M,X, Y e os que não foram criados pela importação de saldos, caso o arquivo tenha esses registros, exibir a msg TR00717 (Código, Descrição)

Se o tipo de linha carregado no arquivo for de Rótulo ou Cálculo Não Alterável (campo tipo = ‘R’ ou ‘CNA’  da tabela dinâmica) exibir a msg TR00716 (Código, Descrição).

Se o campo correspondente ao Valor possuir sinal negativo “-” e a linha corresponde ao valor possuir formato diferente de NS, exibir a msg TR00666 (Código, Descrição).Esta msg não deve ser exibida quando se tratar de linhas correspondentes ao registro L210 a partir da versão 2.00.

Linha 2 dos Registros N500 e N650:
 
Ao carregar valor para a linha (através do arquivo), considerar o valor para a linha e os campos do modal: Valor da Receita Bruta Sujeita a X, X%, Valor Calculado, Valor Total da Receita Bruta e Somatório do Valor Calculado, devem ser apagados.

Se for carregado um arquivo para uma ou mais linhas dos registros que já estejam selecionadas para serem descartadas, substituir os dados dessa linha com o novo valor e habilitar novamente o ícone de descarte (apenas para as linhas informadas no arquivo).
		Descartar as Alterações Manuais	Botão	-	-	Habilitado	

Permite ao usuário descartar os valores de entrada manual de um ou mais registros.


Tratamentos:

Ao acionar este botão, se não houver no mínimo um registro com entrada manual realizada exibir a mensagem DW00123.

Se o usuário clicar neste botão apresentar a mensagem DW00121 apenas uma vez.

Após acionar este botão, os registros que foram considerados no descarte, deverão ser atualizados (alterar o ícone da coluna Status).
_	MFS-14487		Justificar	Botão		Permite ao usuário informar a justificativa para os registros que foram selecionados e que possuam valores de entrada manual.


Tratamentos:

Todos os registros que possuírem entrada manual podem ser justificados. 

Apenas serão gravadas justificativas se o registro possuir entrada manual. Se nenhum registro selecionado possuir entrada manual, exibir a mensagem DW00123 e não abrir o modal “ HYPERLINK  \l "ModalJustificar" Justificar Valor(es) Informado”

	MFS-14487		Percentual de Receita Bruta	Botão		Permite ao usuário informar na linha 2 dos registros N500 e N650 os valores de percentual de receita bruta.


Tratamentos:

Ao acionar este botão se for selecionado uma linha diferente da linha2 dos registros N500 ou do N650, exibir a mensagem DW00209.

Se nenhuma linha for selecionada, exibir a mensagem DW00041.

Ao selecionar o a linha dois do registro N500, abrir o  HYPERLINK  \l "ModalPercentualdeReceitaBrutaN500" modal de percentual do registro N500.

Ao selecionar o a linha dois do registro N650, abrir o  HYPERLINK  \l "ModalPercentualdeReceitaBrutaN650" modal de percentual do registro N650.

	MFS-17658		Exportar	Botão	-	-	-	 Realiza a exportação dos dados dos registros no formato CSV, conforme padrão do framework.

		Grid (*)
Na edição, deve ser permitida a visualização de todas as linhas da grid armazenadas de acordo o conteúdo selecionado na grid de consulta.(*)		Ações 		Pesquisar	Ícone		Permite ao usuário efetuar a pesquisa de registros. 

Tratamentos:

A pesquisa poderá ser feita pelos campos:Registro, Cód. Do Registro e Desc. do Registro.	MFS-14487		Check-box	Botão	S	-	-	Seleciona um ou mais registro da GRID 

Tratamentos:

O(s) registro(s) selecionado(s) ficará(ão) disponível(eis) para serem Justificados ou Descartar Entrada Manual. 	MFS-14487		Status
	Ícone do Status
+ícones de formato de linha
	-	-	Em branco	Tooltip:

Ícones de Status Permitidos:

Em branco: Não foi realizada uma entrada manual.

Ícone Justificar em Vermelho: Realizada entrada manual e o valor não foi justificado.

Ícone Justificar em Verde: Realizada entrada manual e o valor foi justificado.

Ícone Descartar Entrada Manual: Realizada entrada manual (com ou sem justificativa) e o valor foi descartado.

Ícones de Formato de Linhas: 

Para as linhas aplicáveis de acordo com a descrição das regras no quadro abaixo, exibir os ícones dentro do campo:


Ìcone
Descrição


Exibir este ícone do lado direito do ícone de status, para os campos de valor com formato ‘NS’ com o tooltip:
“Esta linha aceita valores negativos”.


Exibir este ícone do lado direito do ícone de status, para as linhas 2 dos registros N500 e N650 (que podem conter informações de percentuais de receita bruta), com o Tooltip:
‘Percentuais de Receita Bruta’. 


Tratamentos:

Se o usuário selecionar os ícones, exibir o tooltip conforme regras abaixo:

Ícone Justificar em Vermelho: Insira a justificativa.
Ícone Justificar em Verde: Apresenta a descrição da justificativa. Formato: ‘Justificativa: XXX’.
Ícone Descartar Entrada Manual: Valor será descartado, após um novo processamento.

Ordem de exibição dos ícones no campo:

Status + + 
	MFS-14487
MFS-17658		Registro	Texto	-	N		Exibe os registros de todas as linhas das tabelas dinâmicas existentes na grid.

Tratamento:

Não deve ser permitida a visualização dos registros do Bloco M.	
MFS-14487		Cód. do Registro	Texto	S	N		Exibe os códigos de todas as linhas das tabelas dinâmicas existentes na grid corresponde ao conteúdo do campo Registro.	MFS-14487		
Desc. do Registro	Texto	S	N		Exibe a descrição das linhas das tabelas dinâmicas ou a descrição da conta do usuário corresponde ao código exibido no campo Cód. do Registro.	MFS-14487		Ordem	Texto	S	N		Exibe a ordem de cada linha da tabela dinâmica.	MFS-14487		Linha da ECF	Texto	S	N		Exibe a ordem de cada linha da tabela dinâmica.	MFS-14487		Valor	Texto	S	N		

Permite que o usuário informe o valor das linhas das tabelas dinâmicas. 

Tratamentos:

- O valor informado neste campo será utilizado como saldo das linhas das tabelas dinâmicas.


Todos os Registros:
Ao mudar de linha, verificar se o formato da linha está compatível com o valor informado. Se o valor da linha é negativo e o formato diferente de ‘NS’, exibir a mensagem: DW00126


Registro L210:
Para as linhas de formato ‘NS’, verificar se o valor é negativo, em caso afirmativo, exibir a mensagem DW00130.


- Para os registros N500 e N650 – Linha 2, que possuam valores preenchidos no  HYPERLINK  \l "ModalPercentualdeReceitaBruta" modal Percentuais de Receita Bruta, considerar as orientações abaixo:

Se o usuário alterar o valor através do campo “Valor” e se este for diferente do “Somatório do Valor Calculado” dentro do campo ‘Percentuais da Receita Bruta’ 

Exibir a mensagem DW00204.

Se selecionar a opção ‘Sim’, limpar o conteúdo dos campos:  “Valor da Receita Bruta Sujeita à X, X%”,  “Valor Calculado”,  “Valor Total da Receita Bruta”,
 “Somatório do Valor Calculado”. 

Se selecionar a opção ‘Não’, o campo “Valor” não será atualizado com a nova informação.

	MFS-14487
MFS-17658		


Modais


Modal (*) 
Título: Justificar Valor(es) Informado


Voltar  HYPERLINK  \l "justificar" botão Justificar		Justificativa 	Texto	S	S	-	O usuário poderá informar a Justificativa.

Tratamento: 

Essa informação poderá ter como origem o arquivo importado por meio do botão Importar Ocorrências de um Arquivo.	MFS-14487		Justificar	Botão	-	-	-	Ao acionar o botão Justificar, o sistema deverá atualizar as informações e fechar o modal. 

Tratamento:

Atualizar o campo Status. Caso não seja informada nenhuma informação, exibir a mensagem DW00124.

Quando ao conteúdo do campo Justificar tiver como origem a importação do arquivo por meio do botão Importar Ocorrências de um Arquivo a ação desse botão deverá ocorrer de forma automática.	MFS-14487		Cancelar 	Botão	-	-	-	Ao acionar esse botão o sistema fecha o modal e volta para tela anterior.	MFS-14487		     (*) Não exibir a descrição na tela.

Percentual de Receita do Registro N500:


MODAL (*) Entrada Manual – Percentual de Receita Bruta		PERCENTUAIS DE RECEITA BRUTA		IRPJ		Mensagem Fixa*		N	S		Ao confirmar a alteração/inserção de valores nesta tela, o valor totalizado no campo ‘Somatório do Valor Calculado’, será atribuído à linha 2 do registro N500 (na tela principal).	MFS-17658		Valor da Receita Bruta Sujeita a 1,6%	Texto	N	S	0,00	Permite ao usuário informar o valor da receita bruta.
	MFS-17658		Valor Calculado	Texto	N	N	0,00	Permite ao usuário visualizar o valor correspondente à receita bruta aplicada ao percentual.

Tratamentos:
Campo calculado pelo sistema. Será exibido o valor do campo ‘Valor da Receita Bruta Sujeita a 1,6%’ * 0,016
O valor deve ser arredondado.
	MFS-17658		Valor da Receita Bruta Sujeita a 8%	Texto	N	S	0,00	Permite ao usuário informar o valor da receita bruta.	MFS-17658		Valor Calculado	Texto	N	N	0,00	Permite ao usuário visualizar o valor correspondente à receita bruta aplicada ao percentual.

Tratamentos:
Campo calculado pelo sistema. Será exibido o valor do campo ‘Valor da Receita Bruta Sujeita a 8%’ * 0,08
O valor deve ser arredondado.
	MFS-17658		Valor da Receita Bruta Sujeita a 16%	Texto	N	S	0,00	Permite ao usuário informar o valor da receita bruta.	MFS-17658		Valor Calculado	Texto	N	N	0,00	Permite ao usuário visualizar o valor correspondente à receita bruta aplicada ao percentual.

Tratamentos:
Campo calculado pelo sistema. Será exibido o valor do campo ‘Valor da Receita Bruta Sujeita a 16%’ * 0,16
O valor deve ser arredondado.
	MFS-17658		Valor da Receita Bruta Sujeita a 32%	Texto	N	S	0,00	Permite ao usuário informar o valor da receita bruta.	MFS-17658		Valor Calculado	Texto	N	N	0,00	Permite ao usuário visualizar o valor correspondente à receita bruta aplicada ao percentual.

Tratamentos:
Campo calculado pelo sistema. Será exibido o valor do campo ‘Valor da Receita Bruta Sujeita a 32%’ * 0,32
O valor deve ser arredondado.
	MFS-17658		Valor da Receita Bruta Sujeita a 100%	Texto	N	S	0,00	Permite ao usuário informar o valor da receita bruta.	MFS-17658		Valor Calculado	Texto	N	N	0,00	Permite ao usuário visualizar o valor correspondente à receita bruta aplicada ao percentual.

Tratamentos:
Campo calculado pelo sistema.
Será exibido o valor do campo “Valor da Receita Bruta Sujeita à 100%” * 1,00
O valor deve ser arredondado.	MFS-17658		TOTAL DAS RECEITAS		MFS-17658		Valor Total da Receita Bruta	Texto	N	N	0,00	Permite ao usuário visualizar o total informado das receitas bruta.

Tratamentos:
Campo calculado pelo sistema. Será exibido o somatório dos campos:

“Valor da Receita Bruta Sujeita a 1,6%” + “Valor da Receita Bruta Sujeita a 08%” +
”Valor da Receita Bruta Sujeita a 16%” +
”Valor da Receita Bruta Sujeita a 32%” +
“Valor da Receita Bruta Sujeita a 100%”
	MFS-17658		Somatório do Valor Calculado	Texto	N	N	0,00	Permite ao usuário visualizar o total informado das receitas bruta (aplicado os percentuais).

Tratamentos:
Campo calculado pelo sistema. Será exibido o somatório dos campos 
“Valor Calculado” (da Receita Bruta Sujeita a 1,6%) + 
“Valor Calculado” (da Receita Bruta Sujeita a 8%) +
”Valor Calculado” (da Receita Bruta Sujeita a 16%) +
”Valor Calculado” (da Receita Bruta Sujeita a 32%) +
“Valor Calculado” (da Receita Bruta Sujeita a 100%)
Este valor deve ser informado na grid “Entrada manual para os registros processados”, na linha 2 do registro N500.	MFS-17658		OK	Botão		Permite ao usuário confirmar a inclusão/alteração da informação.

Tratamentos:

Se todos os valores incluídos do modal, forem zerados, ao acionar este botão, exibir a mensagem DW00210, se o usuário selecionar a opção ‘Não’, nada será alterado, se ‘Sim’, o valor será atualizado na linha do registro.	MFS-17658		Cancelar	Botão		Permite ao usuário cancelar a operação e voltar para a tela principal.	MFS-17658		

Percentual de Receita do Registro N650:


MODAL (*) Entrada Manual – Percentual de Receita Bruta		PERCENTUAIS DE RECEITA BRUTA		CSLL		Mensagem Fixa*		N	S		Ao confirmar a alteração/inserção de valores nesta tela, o valor totalizado no campo ‘Somatório do Valor Calculado’, será atribuído à linha 2 do registro N650 (na tela principal).	MFS-17658		Valor da Receita Bruta Sujeita a 12%	Texto	N	S	0,00	Permite ao usuário informar o valor da receita bruta.	MFS-17658		Valor Calculado	Texto	N	N	0,00	Permite ao usuário visualizar o valor correspondente à receita bruta aplicada ao percentual.

Tratamentos:
Campo calculado pelo sistema. Será exibido o valor do campo ‘Valor da Receita Bruta Sujeita a 12%’ * 0,12
O valor deve ser arredondado.
	MFS-17658		Valor da Receita Bruta Sujeita a 32%	Texto	N	S	0,00	Permite ao usuário informar o valor da receita bruta.	MFS-17658		Valor Calculado	Texto	N	N	0,00	Permite ao usuário visualizar o valor correspondente à receita bruta aplicada ao percentual.

Tratamentos:
Campo calculado pelo sistema. Será exibido o valor do campo ‘Valor da Receita Bruta Sujeita a 32%’ * 0,32
O valor deve ser arredondado.
	MFS-17658		Valor da Receita Bruta Sujeita a 100%	Texto	N	S	0,00	Permite ao usuário informar o valor da receita bruta.	MFS-17658		Valor Calculado	Texto	N	N	0,00	Permite ao usuário visualizar o valor correspondente à receita bruta aplicada ao percentual.

Tratamentos:
Campo calculado pelo sistema.
Será exibido o valor do campo “Valor da Receita Bruta Sujeita a 100%” * 1,00
O valor deve ser arredondado.	MFS-17658		TOTAL DAS RECEITAS		MFS-17658		Valor Total da Receita Bruta	Texto	N	N	0,00	Permite ao usuário visualizar o total informado das receitas bruta.

Tratamentos:
Campo calculado pelo sistema. Será exibido o somatório dos campos: 
“Valor da Receita Bruta Sujeita a 12% + “Valor da Receita Bruta Sujeita a 32%” + 
“Valor da Receita Bruta Sujeita a 100%
	MFS-17658		Somatório do Valor Calculado	Texto	N	N	0,00	Permite ao usuário visualizar o total informado das receitas bruta (aplicado os percentuais).

Tratamentos:
Campo calculado pelo sistema. 
Será exibido o somatório dos campos “Valor Calculado” (da Receita Bruta Sujeita a 12%) +
” Valor  Calculado” (da Receita Bruta Sujeita a 32%) + 
“Valor Calculado” (da Receita Bruta Sujeita 

Este valor deve ser informado na grid “Entrada manual para os registros processados”, na linha 2 do registro N650.	MFS-17658		OK	Botão		Permite ao usuário confirmar a inclusão/alteração da informação.

Tratamentos:

Se todos os valores incluídos do modal, forem zerados, ao acionar este botão, exibir a mensagem DW00210, se o usuário selecionar a opção ‘Não’, nada será alterado, se ‘Sim’, o valor será atualizado na linha do registro.	MFS-17658		Cancelar	Botão		Permite ao usuário cancelar a operação e voltar para a tela principal.	MFS-17658
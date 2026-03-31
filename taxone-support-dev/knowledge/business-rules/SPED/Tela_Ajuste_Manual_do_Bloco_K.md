# Tela_Ajuste_Manual_do_Bloco_K

> Fonte: Tela_Ajuste_Manual_do_Bloco_K.doc

THOMSON REUTERS

Tela Balanço/DRE (Bloco K)
ECF - Escrituração Contábil Fiscal (DW)


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		04/10/2017	MFS-12713	Criação do Documento	Alessandra Cristina Navatta		01/11/2017	MFS-14483	Inclusão da Aba de Atividades Mistas	Alessandra Cristina Navatta		20/03/2018	MFS-17180	Inclusão de filtro Status (no botão Abre)	Alessandra Cristina Navatta		11/09/2018	MFS-20762	Atualmente, a tela só atualiza o status da apuração se a tela for fechada. Inserido as regras de atualização de status nos botões de Justificar, Validar Rateio na(s) Conta(s).	Alessandra Cristina Navatta		


Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc524451868" 1 INTRODUÇÃO	 PAGEREF _Toc524451868 \h 3
 HYPERLINK \l "_Toc524451869" 2 DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc524451869 \h 3
 HYPERLINK \l "_Toc524451870" 3 TELA/MODAIS	 PAGEREF _Toc524451870 \h 3
 HYPERLINK \l "_Toc524451871" 3.1 Pesquisa de Registros	 PAGEREF _Toc524451871 \h 3
 HYPERLINK \l "_Toc524451872" 3.2	Regras dos Campos Tela Principal	 PAGEREF _Toc524451872 \h 6
 HYPERLINK \l "_Toc524451873" 3.3	Modais	 PAGEREF _Toc524451873 \h 32


	


1 INTRODUÇÃO

Objetivo desta especificação é criar a tela Ajuste Manual do Balanço/DRE (Bloco K).

2 DOCUMENTOS DE REFERÊNCIA


Mensagens_Sistema_DWECF.xlsx
Regras_Gerais_DWECF.docx
MTZ_Processamento_em_Lote.docx
Tela_Abertura_de_Apuracao.doc


3 TELA/MODAIS


3.1 Pesquisa de Registros

Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Apuração >> Ajustes Manuais >> Balanço/DRE (Bloco K)


Título da tela: Balanço/DRE (Bloco K)

Condições Gerais: Quando o usuário acessar a tela de consulta, apresentar todos os registros contidos na tabela de abertura da apuração.

Obs. As opções dos campos de pesquisa e suas opções, podem ter alguma divergência na escrita e tipo, pois serão apresentados como cadastradas no banco.


 

Campo	Tipo	Regra		Estabelecimento	LOV
(Tipo - Código – Descrição)	Permite que o usuário busque o registro pelo Código do  Estabelecimento.		Exercício	Texto
(AAAA)
	O usuário poderá informar o exercício. 


		Data Inicial	Data
DD/MM/AAAA	O usuário poderá informar a data inicial da Informação ECF.		Versão	Lista
(Código - Descrição)	Aplicar a RNG00004 (Versão de Layout)		Forma de Tributação	Lista
(Código - Descrição)	Exibe as opções abaixo:

- Lucro Real
- Lucro Presumido,
-Lucro Arbitrado
-Imune de IRPJ 
-Isento do IRPJ 		Apuração	Lista
(Código - Descrição)	Exibe as opções abaixo:

- Anual
- Trimestral
		Período de Apuração	Lista
(Código - Descrição)	Selecionar um item da lista.

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

Localização da tela: ECF - Escrituração Contábil Fiscal >> Apuração>> Ajustes Manuais>>Balanço/DRE (Bloco K)

Título da tela: Balanço/DRE (Bloco K)

Considerações: Desabilitar os botões “Novo” e “Excluir” na toolbar.

Recuperar apenas as aberturas com status diferente de “Apuração em Aberto” e A00.
Permitir edição do registro apenas quando o status da abertura de apuração correspondente ao registro for diferente de “Cálculo Realizado”. Se o status da apuração  for igual a “Cálculo Realizado”,  aplicar a RNG00018 (Alteração de tela com controle de status da abertura da apuração).

Considerações: Se durante o processamento em lote, for selecionada a opção “Manter Ajustes Manuais Realizados” os dados incluídos os alterados manualmente nesta tela deverão ser visualizados conforme ajuste manual realizado antes da nova importação dos saldos com a opção manter ajustes manuais realizados desde que os critérios definidos na RNI10.01 sejam atendidos. 


Campo	Tipo	Obrig	Ed	Formato/Default	Regra	OS/CH/WI		Fechar	Botão	-	-		Botão que submete a ação de fechar a tela.

Tratamentos:

Se o campo Validar estiver com o ícone Validar “Verde, o sistema deverá fechar a tela.
Se uma ou mais contas estiverem com o ícone “Vermelho” no campo Justificar, o sistema deverá abrir o modal “ HYPERLINK  \l "PendenciasIdentificadas" Pendências Identificadas”.

Atualização de Status:

Se houver alteração no registro, ajustar os status conforme regras abaixo:

Status = “Importação dos Saldos Realizada”:

Se status = “Importação dos Saldos Realizada” e houver contas com pendência de rateio, Alterar  status para “Aguardando Ajuste Manual”.
Se status = “Importação dos Saldos Realizada” e não houver contas com pendência de rateio: Alterar para “Alteração Manual Realizada”.


Status = “Alteração Manual Realizada”:

Se status = “Alteração Manual Realizada” e houver contas com pendência de rateio, Alterar status para “Aguardando Ajuste Manual”.
Se status = “Alteração Manual Realizada” e não houver contas com pendência de rateio, Manter.


Status = “Aguardando Ajuste Manual”:

Se status = “Aguardando Ajuste Manual” e houver contas com pendência de rateio, manter status em “Aguardando Ajuste Manual”.
Se status = “Aguardando Ajuste Manual” e não houver contas com pendência de rateio, alterar para “Alteração Manual Realizada”.


Status = “Reapurar”:

Se status = “Reapurar” e houver contas com pendência de rateio, alterar para em “Aguardando Ajuste Manual”.
Se status = “Reapurar” e não houver contas com pendência de rateio, alterar para “Alteração Manual Realizada”.


Status = “Cálculo Realizado”:
Não poderá ser editada apurações com esse status.


Apurações Posteriores:

Se for alterado o valor de Saldo Inicial do primeiro período de apuração anual, ou de qualquer período trimestral, o sistema deve verificar se existem aberturas de apuração para períodos posteriores com status diferente de “Apuração em Aberto”, se encontrar, exibir a mensagem: DW00079.
	MFS-12713		Mensagem Explicativa (*)	Texto	S	N	-	
Ao abrir a tela, exibir a mensagem abaixo:

"Ao efetuar a alteração dos valores exibidos na grid, será necessário efetuar a execução do cálculo no Processamento em Lote para a atualização dos registros com os valores informados”.
	MFS-12713		DADOS GERAIS
As informações são referentes ao registro selecionado na Abertura de Apuração. (*)
		Estabelecimento
	Texto
	S	N		Permite que o usuário visualize o Estabelecimento da apuração que foi recuperada	MFS-12713		Exercício	Texto
	S	N		Permite que o usuário visualize o exercício.	MFS-12713		Data Inicial	Texto
	S	N		Permite que o usuário visualize a data inicial 

	MFS-12713		Versão	Texto	S	N		Permite que o usuário visualize a Versão do Layout utilizada para o processamento do registro.

Valores válidos:

Aplicar RNG00004 (Versão de Layout).	MFS-12713		Forma de Tributação	Texto
	S	N		Permite que o usuário visualize a forma de tributação.
	MFS-12713		Apuração	Texto
	S	N		Permite que o usuário visualize a Apuração.	MFS-12713		Período de Apuração	Texto	S	N	-	Permite que o usuário visualize o período de apuração.	MFS-12713		Aba(*) 

Rateio		Título (*)
RATEIO DO SALDO DE CONTA CONTÁBIL PARA MAIS DE UMA CONTA REFERENCIAL		Pesquisar	Botão	-	-	-	Permitir pesquisar um registro por código da conta contábil e do centro de custo.	MFS-12713		Validar Rateio na(s) Conta(s)

	Botão		Ao acionar o botão “Validar Rateio na Conta” o sistema deverá validar a(s) conta(s) selecionada(s).

Tratamento: 

Todos os registros da aba Rateio devem ser validados. Esta validação pode ser realizada pelo botão “Validar Rateio na(s) Conta(s)” ou quando o usuário mudar o foco do registro da  tabela referencial (este ultimo é acionado automaticamente pelo sistema)

Ao validar um registro efetuar as seguintes ações: 
Se o campo “Validar” estiver vazio, o sistema deverá realizar a totalização dos valores informados no campo “Saldo Final Informado” levando em consideração os lançamentos a débito e a crédito do campo “Indicador do Saldo Final Informado”, bem como nos campos de Saldo Inicial (quando possível), localizados na GRID Conta Referencial e exibir o valor resultante nos campos “Saldo Final Informado” e “Saldo Inicial Informado” na grid Conta Contábil.

Se o “Saldo Final Calculado” for igual o “Saldo Final Informado” e “Saldo Inicial Calculado” for igual o “Saldo Inicial Informado”, o campo Validar deverá ficar com o ícone validar “Verde”.

Se o “Saldo Final Calculado” for diferente do “Saldo Final Informado” ou “Saldo Inicial Calculado” for diferente do “Saldo Inicial Informado” o campo Validar deverá ficar com o ícone Justificar “Vermelho”. A partir do momento, que for inserida uma justificativa “através do modal  HYPERLINK  \l "ModalJustificar" Justificar Valor(es) Informado, o ícone Justificar passa a ser “verde”.

Aplicar as regras de  HYPERLINK  \l "AtualizacaoStatus" Atualização de Status


-------------------------------------------------------------------------------------
Voltar para  HYPERLINK  \l "checkbox_contacontabil" Check-box (Aba Rateio)
Voltar para o campo  HYPERLINK  \l "CampoValidar_ContaContabil" Validar (Aba Rateio)
Voltar para o campo  HYPERLINK  \l "ValidarDemaisRateio" Validar (Aba Demais Ajustes)

	MFS-12713
MFS-20762		Justificar	Botão		Permite ao usuário informar a justificativa para os registros que foram selecionados e que possuam divergências de informações entre os saldos (inicial ou final) calculado com o informado.


Tratamentos:

Todos os registros que possuírem diferença entre os campos de saldo (inicial ou final) calculado com o informado, devem ser justificados (ícone Justificar “em vermelho” do campo Validar).

Apenas serão gravadas justificativas se o registro possuir diferenças entre o saldo (inicial ou final) calculado com o informado. Se nenhum registro selecionado possuir diferenças, apresentar a mensagem DW00036 e não abrir o modal “ HYPERLINK  \l "ModalJustificar" Justificar Valor(es) Informado”


Aplicar as regras de  HYPERLINK  \l "AtualizacaoStatus" Atualização de Status
	MFS-12713
MFS-20762		Mostrar Apenas Pendentes de Justificativa	Check-box	-	-	desmarcado	Permite ao usuário mostrar apenas os registros que devem ser justificados.	MFS-12713		Grid CONTA CONTÁBIL(*)
Devem ser exibidas todas as contas contábeis que possuem associação em mais de uma conta referencial (*)
As informações das contas contábeis devem ser recuperadas da tabela de Ajuste do Balanço/DRE (Bloco K).(*)		Check-box	Check-box	-	-	-	Seleciona um ou mais registro da GRID Conta Contábil.

Tratamentos:

O(s) registro(s) selecionado(s) ficará(ão) disponível(eis) para serem Validados (caso o botão  HYPERLINK  \l "ValidarRateio" Validar Rateio na(s) Conta(s) for selecionado)	MFS-12713		Marcar Todos	Check-box	-	-	-	Permite ao usuário selecionar todas as contas contábeis da grid de contas contábeis.	MFS-12713		VALIDAR
	Ícone Validar	-	-	-	
Apresentar os ícones no campo.

Tratamento:

- O campo poderá ser preenchido de quatro formas-
Em branco
Ícone Validar (em Verde)
Ícone Justificar (em Vermelho)
Ícone Justificar (em Verde)

- Ao entrar na tela pela primeira vez o sistema deverá apresentar o campo sem os ícones, ou seja, em branco.
- Se o usuário passar pelo processo de Validar Rateio e não houver necessidade de ser Justificado, apresentar o ícone Validar (em Verde). Caso seja necessário justificar apresentar apenas o ícone Justificar (em Vermelho), caso, a justificativa seja informada , apresentar o ícone Justificar (em Verde) conforme regras existentes no botão  HYPERLINK  \l "ValidarRateio" Validar Rateio na(s) Conta(s)

Se o campo estiver preenchido com:
- Ícone Validar (em verde), ou sem preenchimento e o usuário clicar no campo, nada será realizado, Caso o ícone Justificar estiver sendo exibido e o usuário selecionar este campo, seguir conforme regras abaixo: 

- Se o ícone Justificar “Verde” o sistema deverá apresentar um tooltip, exibindo a justificativa que foi inserida no modal “ HYPERLINK  \l "ModalJustificar" Justificar Valor(es) Informado”.
- Se o ícone Justificar “Vermelho”, o sistema deverá abrir o modal “ HYPERLINK  \l "ModalJustificar" Justificar Valor(es) Informado”.


	MFS-12713
		Ícone Justificar	-	-	-		CONTA CONTÁBIL	Texto	S	N	-	Permite ao usuário visualizar os códigos das contas contábeis. 	MFS-12713		CENTRO DE CUSTO	Texto	S	N	-	Permite ao usuário visualizar os códigos dos centros de custos.	MFS-12713		SALDO INICIAL CALCULADO 	
Texto	
S	
N	
00,00C	Permite ao usuário visualizar o saldo Inicial Calculado.

Tratamentos:

Concatenar com o indicador do saldo.

	
MFS-12713		SALDO INICIAL INFORMADO 	
Texto	
S	
N	
0,00C	Permite ao usuário visualizar o total das contas referenciais editada no campo “Saldo Inicial Informado” na GRID “Conta Referencial” para cada item selecionado.


  Tratamentos:

Concatenar o valor com o indicador do saldo.


	
MFS-12713		SALDO FINAL CALCULADO 	Texto
	S
	N
	0,00C
	
Permite ao usuário visualizar o Saldo Final Calculado.

Tratamentos:
Concatenar o valor com o indicador do saldo.

	MFS-12713
		SALDO FINAL INFORMADO 	Texto
	S
	N
	0,00C
	
Permite ao usuário visualizar o total das contas referenciais editada no campo “Saldo Final Informado” na GRID “Conta Referencial” para cada item selecionado. 


Tratamentos: 

O indicador deve refletir o balanço entre o(s) crédito(s) e débito(s) do(s) Saldo(s) Informado(s) da Conta Referencial. 


Conta Referencial 
Saldo Informado
Indicador 

Plano 1
110,00
C

Plano 2
10,00
D


Logo, os campos “Saldo Final Informado” e o “Indicador do Saldo Final Informado” serão “100,00” e “C” respectivamente.  
	
MFS-12713		Grid  CONTA REFERENCIAL(*)

Devem ser exibidas todas as contas referenciais que possuem associação com a conta contábil (*)
As informações das contas contábeis devem ser recuperadas da tabela de Ajuste do Balanço/DRE (Bloco K).(*)		pesquisar
	botão	-	-	-	Permite pesquisar um registro pelo código e descrição da conta referencial.	MFS-12713		CÓD. DA CONTA REFERENCIAL	Texto	S	N	-	Permite ao usuário visualizar o código da Conta Referencial.	MFS-12713		DESC. DA CONTA REFERENCIAL	Texto	S	N	-	Permite ao usuário visualizar a descrição da Conta Referencial.	MFS-12713		SALDO INICIAL CALCULADO	Texto	S	N	-	Permite ao usuário visualizar o saldo inicial calculado.

Tratamentos:

Concatenar o valor com o indicador do saldo.	MFS-12713		SALDO INICIAL INFORMADO	Texto	S	S	0,00	Exibe o saldo inicial calculado da Conta Contábil e permite que o usuário edite o valor exibido.

Tratamentos: 

Esse campo só deve ficar editável em caso de Apuração Trimestral ou para o primeiro Período de Apuração da Anual e  para as contas de natureza patrimonial (ativo(1), passivo (2) e patrimônio líquido (7)). Para contas de natureza diferente de Patrimonial o campo deve ficar nulo e desabilitado para edição.


Se estiver selecionada uma conta contábil no GRID Conta Contábil onde o campo Validar esteja com o ícone “Verde” e for alterado o valor deste campo:
O sistema deverá alterar automaticamente o campo Validar, ajustando os ícones (validar / justificar), com base nos novos valores, ou seja, caso no registro anterior tenha sido informado uma justificativa, a mesma será excluída.


	MFS-12713		INDICADOR DO SALDO INICIAL INFORMADO	Lista	S	S	Código - Descrição	Permite ao usuário visualizar ou editar o indicador do saldo inicial (débito ou crédito) para o valor do campo “Saldo Inicial Informado”.

Valores válidos:
nulo
D - Débito
C - Crédito

Tratamentos: 

Esse campo só deve ficar editável em caso de Apuração Trimestral ou para o primeiro Período de Apuração da Anual e  para as contas de natureza patrimonial (ativo(1), passivo (2) e patrimônio líquido (7)). Para contas de natureza diferente de Patrimonial o campo deve ficar nulo e desabilitado para edição.


Se estiver selecionada uma conta contábil no GRID Conta Contábil e o campo Validar estiver preenchido e for alterado o valor deste campo:
O sistema deverá alterar automaticamente o campo Validar, ajustando os ícones (validar / justificar), com base nos novos valores, ou seja, caso no registro anterior tenha sido informado uma justificativa, a mesma será excluída.

Este campo ficará em branco, se o valor Saldo Inicial Informado, não for ajustado pelo usuário. Exceto se, para uma determinada conta contábil, existir mais de uma referencial e pelo menos um registro possuir valor no campo ‘Saldo Inicial Informado’, neste caso, em todos os demais registros desta conta contábil, que estavam com o campo vazio, passarão a ter o campo com a opção ‘Crédito’.


Se o campo ‘Saldo Inicial Informado’ for maior que zero, este campo é de preenchimento obrigatório. Caso não seja preenchido, exibir a DW00001.  


		SALDO FINAL CALCULADO	Texto	S	N	-	Permite ao usuário visualizar o saldo final calculado.

Tratamentos:

Concatenar o valor com o indicador do saldo.	MFS-12713		SALDO FINAL INFORMADO	Texto	S	S	0,00	Exibe o saldo final calculado da Conta Contábil e permite que o usuário edite o valor exibido.

Tratamento:

Se estiver selecionada uma conta contábil no GRID Conta Contábil onde o campo Validar preenchido e for alterado o valor deste campo:
O sistema deverá alterar automaticamente o campo Validar, ajustando os ícones (validar e justificar), com base nos novos valores, ou seja, caso no registro anterior tenha sido informado uma justificativa, a mesma será excluída.

	MFS-12713		INDICADOR DO SALDO FINAL INFORMADO	Lista	S	S	Código - Descrição
	Permite ao usuário visualizar ou editar o indicador do saldo (débito ou crédito) para o valor do campo “Saldo Final Informado”.


Valores válidos:
nulo
D - Débito
C - Crédito

Tratamento: 


Se estiver selecionada uma conta contábil no GRID Conta Contábil e o campo Validar estiver preenchido e for alterado o valor deste registro:
O sistema deverá alterar automaticamente o campo Validar, ajustando os ícones (validar / justificar), com base nos novos valores, ou seja, caso no registro anterior tenha sido informado uma justificativa, a mesma será excluída.

Este campo ficará em branco, se o valor Saldo Inicial Informado, não for ajustado pelo usuário. Exceto se, para uma determinada conta contábil, existir mais de uma referencial e pelo menos um registro possuir valor no campo ‘Saldo Final Informado’, neste caso, em todos os demais registros desta conta contábil, que estavam com o campo vazio, passarão a ter o campo com a opção ‘Crédito’.

Se o campo ‘Saldo Final Informado’ for maior que zero, este campo é de preenchimento obrigatório. Caso não seja preenchido, exibir a DW00001.  

	MFS-12713		Aba(*) Demais Ajustes		Título(*)
AJUSTE DO SALDO DE UMA CONTA CONTÁBIL PARA UMA CONTA REFERENCIAL		Pesquisar


	botão	-	-	-	Permitir pesquisar um registro por código da conta contábil e do centro de custo.	MFS-12713		Justificar	Botão		Permite ao usuário informar a justificativa para os registros que foram selecionados e que possuam divergências de informações entre os saldos (incial ou final) calculado com o informado.

Tratamentos:

Todos os registros que possuírem diferença entre os campos de saldo (inicial ou final) calculado com o informado, devem ser justificados.

Apenas serão gravadas justificativas se o registro possuir diferenças entre o saldo (inicial ou final) calculado com o informado. Se nenhum registro selecionado possuir diferenças, apresentar a mensagem DW00036 e não abrir o modal “Justificar Valor(es) Informado”.

Aplicar as regras de  HYPERLINK  \l "AtualizacaoStatus" Atualização de Status
	MFS-12713
MFS-20762		Mostrar Apenas Pendentes de Justificativa	Check-box	-	-	desmarcado	Permite ao usuário mostrar apenas os registros que devem ser justificados.	MFS-12713		Grid (*)		Check-box	Check-box	-	-	-	Seleciona um ou mais registro da GRID.

Tratamentos:

O(s) registro(s) selecionado(s) ficará(ão) disponível(eis) para serem Justificados (caso o botão  HYPERLINK  \l "Justificar_DemaisAjustes" Justificar for selecionado)	MFS-12713		Marcar Todos	Check-box	-	-	-	Permite ao usuário selecionar todas as contas contábeis da grid de contas contábeis.	MFS-12713		VALIDAR	Ícone Validar	-	-	-	


Apresentar os ícones no campo.

Tratamento:

- O campo poderá ser preenchido de quatro formas-
Em branco
Ícone Validar (em Verde)
Ícone Justificar (em Vermelho)
Ícone Justificar (em Verde)

- Ao entrar na tela pela primeira vez o sistema deverá apresentar o campo sem os ícones, ou seja, em branco.
- Se o usuário passar pelo processo de  HYPERLINK  \l "ValidarRateio" Validar Rateio na(s) Conta(s) (mas nesta aba, essa funcionalidade não poderá ser acionada através de botão, apenas automaticamente pelo sistema, mudando o foco do registro que está sendo alterado) e não houver necessidade de ser Justificado, apresentar o ícone Validar (em Verde). Caso seja necessário justificar apresentar apenas o ícone Justificar (em Vermelho), caso, a justificativa seja informada , apresentar o ícone Justificar (em Verde).

- Se o campo estiver preenchido com Ícone Validar (em verde), ou sem preenchimento e o usuário clicar no campo, nada será realizado, Caso o ícone Justificar estiver sendo exibido e o usuário selecionar este campo, seguir conforme regras abaixo: 

- Se o ícone Justificar “Verde” o sistema deverá apresentar um tooltip, exibindo a justificativa que foi inserida no modal “ HYPERLINK  \l "ModalJustificar" Justificar Valor(es) Informado”.
- Se o ícone Justificar “Vermelho”, o sistema deverá abrir o modal “ HYPERLINK  \l "ModalJustificar" Justificar Valor(es) Informado”.


Aplicar as regras de  HYPERLINK  \l "AtualizacaoStatus" Atualização de Status
	MFS-12713
MFS-20762		Ícone Justificar	-	-	-		CONTA CONTÁBIL	Texto	S	N	-	Permite ao usuário visualizar os códigos das contas contábeis.	MFS-12713		CENTRO DE CUSTO	Texto	S	N	-	Permite ao usuário visualizar os códigos dos centros de custos.	MFS-12713		SALDO INICIAL CALCULADO	Texto	S	N	0,00C	Permite ao usuário visualizar o valor do Saldo Inicial Calculado.

Tratamentos:

Concatenar com o indicador do saldo.

	MFS-12713		SALDO INICIAL INFORMADO	Texto	S	N	0,00C	Permite ao usuário visualizar o total das contas referenciais editada no campo “Saldo Inicial Informado” na GRID “Conta Referencial” para cada item selecionado.


  Tratamentos:

Concatenar o valor com o indicador do saldo.
	MFS-12713		SALDO FINAL CALCULADO 	Texto
	S
	N
	0,00C
	
Permite ao usuário visualizar o Saldo Final Calculado.

Tratamentos:
Concatenar o valor com o indicador do saldo.

	MFS-12713
		SALDO FINAL INFORMADO 	Texto
	S
	N
	0,00C
	
Permite ao usuário visualizar o total das contas referenciais editada no campo “Saldo Final Informado” na GRID “Conta Referencial” para cada item selecionado. 


Tratamentos: 

O indicador deve refletir o balanço entre o(s) crédito(s) e débito(s) do(s) Saldo(s) Informado(s) da Conta Referencial. 


Conta Referencial 
Saldo Informado
Indicador 

Plano 1
110,00
C

Plano 2
10,00
D


Logo, os campos “Saldo Final Informado” e o “Indicador do Saldo Final Informado” serão “100,00” e “C” respectivamente.  
	MFS-12713		Grid  CONTA REFERENCIAL(*)

Devem ser exibidas todas as contas referenciais que possuem associação com a conta contábil (*)
As informações das contas contábeis devem ser recuperadas da tabela de Ajuste do Balanço/DRE (Bloco K).(*)		pesquisar
	botão	-	-	-	Permite pesquisar um registro pelo código e descrição da conta referencial.	MFS-12713		CÓD. DA CONTA REFERENCIAL	Texto	S	N	-	Permite ao usuário visualizar o código da Conta Referencial.	MFS-12713		DESC. DA CONTA REFERENCIAL	Texto	S	N	-	Permite ao usuário visualizar a descrição da Conta Referencial.	MFS-12713		SALDO INICIAL CALCULADO	Texto	S	N	-	Permite ao usuário visualizar o saldo inicial calculado.

Tratamentos:

Concatenar o valor com o indicador do saldo.	MFS-12713		SALDO INICIAL INFORMADO	Texto	S	S	0,00	Exibe o saldo inicial calculado da Conta Contábil e permite que o usuário edite o valor exibido.

Tratamentos: 

Esse campo só deve ficar editável em caso de Apuração Trimestral ou para o primeiro Período de Apuração da Anual e  para as contas de natureza patrimonial (ativo(1), passivo (2) e patrimônio líquido (7)). Para contas de natureza diferente de Patrimonial o campo deve ficar nulo e desabilitado para edição.


Se estiver selecionada uma conta contábil no GRID Conta Contábil onde o campo Validar esteja com o ícone “Verde” e for alterado o valor deste campo:
O sistema deverá alterar automaticamente o campo Validar, ajustando os ícones (validar / justificar), com base nos novos valores, ou seja, caso no registro anterior tenha sido informado uma justificativa, a mesma será excluída.


	MFS-12713		INDICADOR DO SALDO INICIAL INFORMADO	Lista	S	S	Código - Descrição	Permite ao usuário visualizar ou editar o indicador do saldo inicial (débito ou crédito) para o valor do campo “Saldo Inicial Informado”.

Valores válidos:
nulo
D - Débito
C - Crédito

Tratamentos: 

Esse campo só deve ficar editável em caso de Apuração Trimestral ou para o primeiro Período de Apuração da Anual e  para as contas de natureza patrimonial (ativo(1), passivo (2) e patrimônio líquido (7)). Para contas de natureza diferente de Patrimonial o campo deve ficar nulo e desabilitado para edição.


Se estiver selecionada uma conta contábil no GRID Conta Contábil e o campo Validar estiver preenchido e for alterado o valor deste campo:
O sistema deverá alterar automaticamente o campo Validar, ajustando os ícones (validar / justificar), com base nos novos valores, ou seja, caso no registro anterior tenha sido informado uma justificativa, a mesma será excluída.

Este campo ficará em branco, se o valor Saldo Inicial Informado, não for ajustado pelo usuário. Exceto se, para uma determinada conta contábil, existir mais de uma referencial e pelo menos um registro possuir valor no campo ‘Saldo Inicial Informado’, neste caso, em todos os demais registros desta conta contábil, que estavam com o campo vazio, passarão a ter o campo com a opção ‘Crédito’.


Se o campo ‘Saldo Inicial Informado’ for maior que zero, este campo é de preenchimento obrigatório. Caso não seja preenchido, exibir a DW00001.  


	MFS-12713		SALDO FINAL CALCULADO	Texto	S	N	-	Permite ao usuário visualizar o saldo final calculado.

Tratamentos:

Concatenar o valor com o indicador do saldo.	MFS-12713		SALDO FINAL INFORMADO	Texto	S	S	0,00	Exibe o saldo final calculado da Conta Contábil e permite que o usuário edite o valor exibido.

Tratamento:

Se estiver selecionada uma conta contábil no GRID Conta Contábil onde o campo Validar preenchido e for alterado o valor deste campo:
O sistema deverá alterar automaticamente o campo Validar, ajustando os ícones (validar e justificar), com base nos novos valores, ou seja, caso no registro anterior tenha sido informado uma justificativa, a mesma será excluída.

	MFS-12713		INDICADOR DO SALDO FINAL INFORMADO	Lista	S	S	Código - Descrição
	Permite ao usuário visualizar ou editar o indicador do saldo (débito ou crédito) para o valor do campo “Saldo Final Informado”.


Valores válidos:
nulo
D - Débito
C - Crédito

Tratamento: 


Se estiver selecionada uma conta contábil no GRID Conta Contábil e o campo Validar estiver preenchido e for alterado o valor deste registro:
O sistema deverá alterar automaticamente o campo Validar, ajustando os ícones (validar / justificar), com base nos novos valores, ou seja, caso no registro anterior tenha sido informado uma justificativa, a mesma será excluída.

Este campo ficará em branco, se o valor Saldo Inicial Informado, não for ajustado pelo usuário. Exceto se, para uma determinada conta contábil, existir mais de uma referencial e pelo menos um registro possuir valor no campo ‘Saldo Final Informado’, neste caso, em todos os demais registros desta conta contábil, que estavam com o campo vazio, passarão a ter o campo com a opção ‘Crédito’.

Se o campo ‘Saldo Final Informado’ for maior que zero, este campo é de preenchimento obrigatório. Caso não seja preenchido, exibir a DW00001.  

	MFS-12713		SALDO FINAL INFORMADO	Texto	S	S	0,00C	Permite ao usuário informar/editar o saldo final da Conta Contábil.

Tratamentos:

Se o campo Validar estiver preenchido e for alterado o valor deste campo:
O sistema deverá alterar automaticamente o campo Validar, ajustando os ícones (validar / justificar), com base nos novos valores, ou seja, caso no registro anterior tenha sido informado uma justificativa, a mesma será excluída.
	MFS-12713		INDICADOR DO SALDO FINAL INFORMADO	Texto	S	S	-
	Permite ao usuário visualizar ou editar o indicador do saldo (débito ou crédito) para o valor do campo “Saldo Final Informado”.


Valores válidos:
nulo
D => Débito
C => Crédito

Tratamentos:

Se o campo Validar estiver preenchido e for alterado o valor deste campo:
O sistema deverá alterar automaticamente o campo Validar, ajustando os ícones (validar / justificar), com base nos novos valores, ou seja, caso no registro anterior tenha sido informado uma justificativa, a mesma será excluída.

Este campo ficará em branco, se o valor Saldo Inicial Informado, não for ajustado pelo usuário.

Se o campo ‘Saldo Final Informado’ for maior que zero, este campo é de preenchimento obrigatório. Caso não seja preenchido, exibir a DW00001.  
	MFS-12713		Aba(*) Lançamento de Encerramento
Se não foi criado o registro de Lançamento de Encerramento na importação essa aba não deverá ser apresentada (*)		INFORMAÇÕES PARA A CRIAÇÃO DO LANÇAMENTO DE ENCERRAMENTO		Cód. da Conta Contábil	Texto	S	N	-	Permite que o usuário visualize o Código da Conta Contábil.
	MFS-12713		Desc. da Conta Contábil	Texto	S	N	-	Permite que o usuário visualize a Descrição da Conta Contábil.
	MFS-12713		Cód. do Centro de Custo	Texto	S	N	-	Permite que o usuário visualize o Código do Centro de Custo. 	MFS-12713		Desc. do Centro de Custo	Texto	S	N	-	Permite que o usuário visualize a descrição do Centro de Custo.	MFS-12713		DADOS DO LANÇAMENTO		Valor	Texto	S	N	-	Exibe o valor do lançamento contábil que foi considerado como saldo da conta contábil	MFS-12713		Ind. do Valor	Texto	S	N	-	Exibe o indicador de débito ou crédito do lançamento contábil	MFS-12713		Aba(*) Atividades Mistas
Se não foi rodada a rotina de percentuais de rateio das atividades mistas essa aba não deverá ser apresentada (*)		INFORMAÇÕES DOS PERCENTUAIS DE RATEIO DAS ATIVIDADES MISTAS		ATIVIDADE GERAL		Cód. da Conta Referencial	Texto	S	N	-	Permite que o usuário visualize o Código da Conta Referencial da atividade Geral

Tratamento: 
Considerar a informação do campo Cód. da Conta Referencial da atividade Geral da tela ‘Percentuais de Rateio das Atividades Mistas’
	MFS-14483		Desc. da Conta Referencial	Texto	S	N	-	Permite que o usuário visualize a Descrição da Conta Referencial da atividade Geral

Tratamento: 
Considerar a informação do campo Desc.da Conta Referencial da atividade Geral da tela ‘Percentuais de Rateio das Atividades Mistas’

	MFS-14483		Saldo Calculado	Texto	S	N	0,00	Permite que o usuário visualize o Valor do Saldo Calculado na importação de saldos (da atividade geral). 

Tratamento:

Considerar a informação do campo Saldo Calculado (da atividade geral) da tela ‘Percentuais de Rateio das Atividades Mistas’

	MFS-14483		Ind. do Saldo Calculado 	Texto	S	N	-	Permite que o usuário visualize o Indicador do Saldo Calculado (da atividade geral).

Tratamento:

Considerar a informação do campo Ind. do Saldo Calculado (da atividade geral) da tela ‘Percentuais de Rateio das Atividades Mistas’.

	MFS-14483		Percentual Calculado	Texto	S	N	0,00%	Permite que o usuário visualize o percentual da atividade geral calculado pela rotina de percentuais de rateio das atividades mistas.


Tratamento:

Considerar a informação do campo Percentual Calculado (da atividade geral) da tela ‘Percentuais de Rateio das Atividades Mistas’

	MFS-14483		Percentual Ajustado	Texto	S	N	0,00%	Permite que o usuário visualize o percentual ajustado da atividade geral.


Tratamento:

Considerar a informação do campo Percentual Ajustado (da atividade geral) da tela ‘Percentuais de Rateio das Atividades Mistas’

Se o campo Percentual Ajustado (da atividade geral) da tela ‘Percentuais de Rateio das Atividades Mistas’, não estiver preenchido, não exibir este campo na tela,

	MFS-14483		ATIVIDADE RURAL		Cód. da Conta Referencial	Texto	S	N	-	Permite que o usuário visualize o Código da Conta Referencial da atividade rural.

Tratamento: 
Considerar a informação do campo Cód. da Conta Referencial da atividade Rural da tela ‘Percentuais de Rateio das Atividades Mistas’
	MFS-14483		Desc. da Conta Referencial	Texto	S	N	-	Permite que o usuário visualize a Descrição da Conta Referencial da atividade rural

Tratamento: 
Considerar a informação do campo Desc. da Conta Referencial da atividade rural da tela ‘Percentuais de Rateio das Atividades Mistas’	MFS-14483		Saldo Calculado	Texto	S	N	0,00	Permite que o usuário visualize o Valor do Saldo Calculado na importação de saldos (da atividade rural). 

Tratamento:

Considerar a informação do campo Saldo Calculado (da atividade rural) da tela ‘Percentuais de Rateio das Atividades Mistas’

	MFS-14483		Ind. do Saldo Calculado	Texto	S	N	-	Permite que o usuário visualize o Indicador do Saldo Calculado (da atividade rural).

Tratamento:

Considerar a informação do campo Ind. do Saldo Calculado (da atividade geral) da tela ‘Percentuais de Rateio das Atividades Mistas’.

	MFS-14483		Percentual Calculado	Texto	S	N	0,00%	Permite que o usuário visualize o percentual da atividade rural calculado pela rotina de percentuais de rateio das atividades mistas.

Tratamento:

Considerar a informação do campo Percentual Calculado (da atividade rural) da tela ‘Percentuais de Rateio das Atividades Mistas’
	MFS-14483		Percentual Ajustado	Texto	S	N	0,00%	Permite que o usuário visualize o percentual ajustado da atividade rural.


Tratamento:

Considerar a informação do campo Percentual Ajustado (da atividade rural) da tela ‘Percentuais de Rateio das Atividades Mistas’

Se o campo Percentual Ajustado (da atividade rural) da tela ‘Percentuais de Rateio das Atividades Mistas’, não estiver preenchido, não exibir este campo na tela,

	MFS-14483		Percentuais de Rateio das Atividades Mistas 	Texto	N	N	Desabilitado	Permite que o usuário visualize se o registro foi alterado pela rotina de percentuais de rateio das atividades mistas.

Tratamentos:

Este campo deve ser sempre desabilitado, Este campo é preenchido pelo sistema, conforme as regras abaixo:
Se os percentuais de rateio das atividades mistas foram calculados pelo sistema, através da rotina, devem ter o campo atualizado para: ‘Gerado pelo Sistema’.
Caso os valores dos percentuais, tenham sido alterados pelo usuário, o campo deve ser atualizado para: ‘Gerado pelo Sistema e Alterado pelo Usuário’.

	MFS-14483		     (*) Não exibir a descrição na tela.


Modais

   


Aba Rateio e Demais Rateio

Modal (*) 
Título: Justificar Valor(es) Informado

--------------------------------------------------------------------------

Voltar para o campo  HYPERLINK  \l "JustificarRateio" Justificar (Aba Rateio)
Voltar para o campo  HYPERLINK  \l "ValidarRateio" Validar (Aba Rateio)
Voltar para o campo  HYPERLINK  \l "ValidarDemaisRateio" Validar (Aba Demais Ajustes)


		Mensagem Fixa: Só deve ser inserida justificativa para as contas que possuem divergências de valores entre os saldos (inicial ou final) calculado com o informado. Contas selecionadas que não possuem essa diferença, não será gravada justificativa para as mesmas.		Justificativa 	Texto	S	S	-	O usuário poderá informar a Justificativa.
	MFS-12713		Justificar	Botão	-	-	-	Ao acionar o botão Justificar, o sistema deverá atualizar as informações e fechar o modal. 

Tratamento:


Se o campo Validar estiver preenchido e gravado, o sistema deverá alterar o ícone “Justificar” para “Verde” na GRID conta contábil, campo Validar. Caso não seja informada nenhuma informação no campo Validar, exibir a mensagem DW00081.
	MFS-12713		Cancelar 	Botão	-	-	-	Ao acionar esse botão o sistema fecha o modal e volta para tela anterior.	MFS-12713		     (*) Não exibir a descrição na tela.


Modal apresentado no Botão Fechar


Modal(*) Pendências Identificadas

--------------------------------------------------------------------------
Voltar para o botão  HYPERLINK  \l "Fechar" Fechar
		Aba(*) Rateio 
Apresentar esta aba, se existir registros com o campo Validar nulo ou com o ícone Justificar em “Vermelho” aba Rateio.(*)		Você fez o Rateio de Valores em Contas Referenciais pertencentes a Conta(s) Contábil(eis) que geraram diferenças entre o Saldo Calculado e o Saldo Informado de suas respectivas contas e que ainda não foram feitas justificativas para tais diferenças.		Aba(*) Demais Ajustes
Apresentar esta aba se existir registro com o campo Validar nulo ou com o ícone Justificar em “Vermelho” na aba Demais Ajustes.(*)		Você fez o Ajuste de Valores em Contas Referenciais pertencentes a Conta(s) Contábil(eis) que geraram diferenças entre o Saldo Calculado e o Saldo Informado de suas respectivas contas e que ainda não foram feitas justificativas para tais diferenças.		Você tem as opções abaixo, o que deseja fazer?		Salvar Agora e Justificar Depois	Botão	-	-	-	Ao acionar esse botão o sistema deverá submeter as informações parametrizadas na Aba Rateio e Demais Ajustes.	MFS-12713		Cancelar e Corrigir Pendências	Botão	-	-	-	Ao acionar esse botão o sistema fecha o modal e volta para tela anterior.	MFS-12713		
     (*) Não exibir a descrição na tela.
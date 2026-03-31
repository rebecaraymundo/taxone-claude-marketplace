# Tela_Copia_de_Abertura_em_Lote

> Fonte: Tela_Copia_de_Abertura_em_Lote.doc

THOMSON REUTERS

Tela Cópia de Abertura em Lote
ECF - Escrituração Contábil Fiscal (DW)


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		11/10/2017	MFS-12678	Criação do Documento 	Alessandra Cristina Navatta		

Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc497322550" 1.	INTRODUÇÃO	 PAGEREF _Toc497322550 \h 3
 HYPERLINK \l "_Toc497322551" 2.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc497322551 \h 3
 HYPERLINK \l "_Toc497322552" 3.	TELAS	 PAGEREF _Toc497322552 \h 3
 HYPERLINK \l "_Toc497322553" 3.1.	Regras dos Campos Tela Principal	 PAGEREF _Toc497322553 \h 3
 HYPERLINK \l "_Toc497322554" 3.2.	Demais Regras	 PAGEREF _Toc497322554 \h 9


	


INTRODUÇÃO

Objetivo desta especificação é criar a tela que permite copiar as aberturas de apuração em lote.

DOCUMENTOS DE REFERÊNCIA


Mensagens_Sistema_DWECF.xlsx

Regras_Gerais_DWECF.docx

Tela_Abertura_de_Apuracao.doc


TELAS


Regras dos Campos Tela Principal


Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Parâmetros >> Critérios de Apuração>>Cópia de Abertura em Lote
Título da tela: Cópia de Abertura em Lote


Campo	Tipo	Obrig	Ed	Formato/Default	Regra	MFS		Processar	Botão	-	-	Default desabilitado-	Ver regra  HYPERLINK  \l "rn000" RN000 	MFS-12678		Tela: Principal(*)Titulo: Cópia de Abertura de Apuração em Lote		Texto explicativo(*): Selecione abaixo os dados de referência que servirão como base para a cópia. 		Título: Parâmetros		Apuração	RadioButton	S	S	Anual	Permite selecionar o tipo de apuração da abertura que será utilizada de referência para o processo de cópia. (Esta informação será recuperada da Informação ECF)Valores Válidos:AnualTrimestral	MFS-12678		Forma de Tributação	Lista	S	S	Lucro Real, Lucro Presumido, Lucro Arbitrado.	Permite selecionar a forma de tributação da abertura que será utilizada de referência para o processo de cópia. (Esta informação será recuperada da Informação ECF)Lista de Valores Válidos:-Lucro Real, Lucro Presumido, Lucro Arbitrado.-Imune de IRPJ -Isento do IRPJ 	MFS-12678		Período de Apuração de Origem	Lov	S	S	Código Estab - CGC - Exercício -  Data Inicial da Escrituração -  Código Abertura - Descrição da Aberura da Apuração(076 - XXXXXXXXXXX - 2017 -01/03/2017 - A1 - Janeiro)	Permite que o usuário selecione uma abertura de apuração para utilizar como referência para cópia.Tratamentos:Apresentar na pesquisa apenas os registros de abertura de apuração que atendam os parâmetros Apuração e Forma de Tributação informados na tela, cujo campo “Situação Especial no Período” seja igual a “Não” e o período da apuração seja diferente de A00 (Anual criado automaticamente pelo sistema). Caso esses critérios não forem respeitados, não apresentar nenhuma abertura de apuração.Campos de Pesquisa do Modal 'Selecionar Períodos de Apuração de Origem:Descrição'Botões do Modal 'Selecionar Períodos de Apuração de Origem': Critério, Cancelar, OK e Salvar- Permite a seleção de apenas um registro.- Ao entrar no modal, pelo menos um registro deve ser selecionado, se for selecionado o botão 'Ok', caso contrário, exibir a mensagem DW00053.- Ao selecionar o botão 'Cancelar', nada será feito e o modal será fechado. - Ao selecionar o botão 'Critério', as apurações que foram recuperadas poderão ser filtradas,pelos campos: 'Estabelecimento' e 'Identificação da Abertura da Apuração', este ultimo campo o formato das informações serão apresentadas com "Código Estab - CGC - Exercício -  Data Inicial da Escrituração -  Código Abertura - Descrição da Aberura da Apuração".-Ao confirmar a seleção do registro, apresentá-los no componente  " Períodos de Apuração de Origem” da tela Principal-Ao selecionar o botão salvar, o sistema salva as informações recuperadas das apurações em formato txt (no diretório local que o usuário informar).	MFS-12678		Texto explicativo(*):Selecione abaixo os dados de período e estabelecimentos que receberão a cópia.		Título: Períodos e Informações ECF de Destino		Inicial	Lista	S	S	Default:Em branco e desabilitado	Permite que o usuário selecione um período inicial para cópia das informações.Conteúdos Válidos:Meses de Janeiro a Dezembro ou;1º trimestre a 4º trimestre.Tratamentos:Quando a apuração de origem selecionada  for “Anual”, exibir a descrição de todos os meses.Quando a apuração de origem selecionada no passo for “Trimestral”, exibir a descrição de todos os trimestres.	MFS-12678		Final	Lista	S	S	Default:Em branco e desabilitado	Permite que o usuário selecione um período final para cópia das informações.Conteúdos Válidos:Meses de Janeiro a Dezembro ou;1º trimestre a 4º trimestre.Tratamentos:Habilitar este campo apenas quando o usuário selecionar um período inicial. Quando a apuração de origem selecionada ” for “Anual”, exibir a descrição de todos os meses a partir do mês selecionado no campo “Inicial”.Exemplo: Se o usuário selecionar como período inicial o mês de abril, apresentar nesta lista os meses de abril a dezembro.Quando a apuração de origem selecionada  for “Trimestral”, exibir a descrição de todos os trimestres a partir do trimestre selecionado no campo “Inicial”.Exemplo: Se o usuário selecionar o 2º trimestre, apresentar nesta lista do 2º trimestre ao 4º trimestre.	MFS-12678		Exercício	Texto	S	S	Default:Em branco e desabilitado	Permite que o usuário informe para qual exercício as informações devem ser copiadas.	MFS-12678		Componente Informações ECF (*)Título:  Informações ECF		Selecionar	Botão	-	-	-	Permite que o usuário selecione os registros de destino (Informações ECF).Tratamentos:Recuperar todas as Informações ECF, conforme descrito abaixo.Campos de Pesquisa do Modal 'Selecionar Estabelecimentos':Botões do Modal 'Selecionar Selecionar Estabelecimentos': Critério, Cancelar, OK e Salvar- Permite a seleção de vários registros por vez.- Ao entrar no modal, pelo menos um registro deve ser selecionado, se for selecionado o botão 'Ok', caso contrário, exibir a mensagem DW00053.- Ao selecionar o botão 'Cancelar', nada será feito e o modal será fechado. - Ao selecionar o botão 'Critério', Informações que foram recuperadas poderão ser filtradas,pelos campos: 'Estabelecimento' e 'Identificação da Informação ECF', este ultimo campo o formato das informações serão apresentadas com "Código do Estabelecimento - CGC - Exercício - Data Inicial da Informação ECF ".-Ao confirmar a seleção dos registros, apresentá-los no componente  " Estabelecimento” da tela Principal-Ao selecionar o botão salvar, o sistema salva as informações recuperadas das infformações ecf em formato txt (no diretório local que o usuário informar).	MFS-12678		Sobrepor aberturas existentes com status "Apuração em Aberto"	CheckBox	Check-box	S	Desmarcado	Permite que o usuário sobrescreva as aberturas de apuração que possuam status igual a “Apuração em Aberto".Tratamentos:Quando esta opção estiver marcada e a abertura de apuração correspondente ao estabelecimento que estiver sendo processado estiver com status “Apuração em Aberto”, sobrescrever a abertura de apuração existente pelos dados da abertura que foi selecionada como referência (considerar apenas o(s) item(ns) que atender(em) a regra de processamento).	MFS-12678		Marcar Todos	CheckBox	Check-box	S	Desmarcado	Permite selecionar todos os registros da grid do componente "Informações ECF". 	MFS-12678		Informações ECF GRID(*)		(CheckBox)	-	-	-	Default Selecionado	Permite que o usuário selecione uma ou mais linhas do componente “Informações ECF”.	MFS-12678		Informações ECF (*)	Texto	S	N	Código Estab - CGC - Exercício -  Data Inicial da Escrituração (076 - XXXXXXXXXXX - 2017 -01/03/2017)	Apresenta as informações ecf que foram recuperadas.	MFS-12678		
Demais Regras

Número	Regras	MFS		RN000	Permite que o usuário realize a cópia de aberturas de apuração em lote.Tratamentos:Se não tiver registros selecionados na grid Informações ECF, emitir a seguinte  mensagem: DW00057Se o período que está sendo processado for diferente do primeiro período da escrituração (recuperada), para cada escrituração selecionada, buscar o registro de abertura da apuração correspondente ao período imediatamente anterior (mês ou trimestre respectivamente). Se não for encontrado registro, apresentar a seguinte mensagem : DW00061.Se o mês que está sendo processado for anterior a data inicial da informações ECF recuperada, emitir a seguinte mensagem: DW00059Se o mês que está sendo processado for posterior a data final da informação ECF recuperada, emitir a seguinte mensagem: DW00060 Devem ser copiadas todas as informações do registro de referência, alterando apenas os campos de estabelecimento (quando este for diferente do estabelecimento de registro de referência) e período (quando houver mais de um período selecionado). A cópia das aberturas deve ser realizada com base nos períodos Inicial e Final (informados no agrupamento Períodos e Informações ECF de Destino), limitado a data final da Informação ECF (destino) selecionada.Situação Especial na ECF de destino Se parâmetro “Sobrepor ..” estiver desmarcado, não realizar a cópia e exibir a DW00058Se o parâmetro “Sobrepor ...” estiver marcado, copiar e criar as aberturas pelo período determinado na parametrização, respeitando as demais regras desse documento.Criação:Quando a abertura de apuração não existir no período de processamento, criá-la com base na abertura de referência (origem).Alteração e campo Sobrepor aberturas existentes com status "Apuração em Aberto" selecionado:Quando a abertura de apuração existire no período de processamento, porém, com status de “Apuração em Aberto” e o campo “Sobrepor...” estiver selecionado, sobrescrever essasas informações  com base na abertura de referência  (origem).Alteração e campo “Sobrepor aberturas e complementares existentes com status "Apuração em Aberto" não selecionado ou Status diferente de “Apuração em Aberto”:Quando a abertura de apuração possuir status diferente de “Apuração em Aberto” no período de processamento ou quando a abertura de apuração possuir status igual a “Apuração em Aberto” e o campo “Sobrepor...” não estiver selecionado, apresentar a seguinte mensagem DW00058.


Voltar botão  HYPERLINK  \l "processar" Processar	MFS-12678
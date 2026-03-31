# Relatorio_de_Conferencia_da_Declaracao_Pais_a_Pais-Bloco_W

> Fonte: Relatorio_de_Conferencia_da_Declaracao_Pais_a_Pais-Bloco_W.doc

THOMSON REUTERS

Relatório de Conferência da Declaração País a País - Bloco W


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		21/08/2018	MFS-20554	Criação do documento	Alessandra Cristina Navatta		


Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc525055891" 1.	INTRODUÇÃO	 PAGEREF _Toc525055891 \h 3
 HYPERLINK \l "_Toc525055892" 2.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc525055892 \h 3
 HYPERLINK \l "_Toc525055898" 3.	Tela de Parâmetros	 PAGEREF _Toc525055898 \h 3
 HYPERLINK \l "_Toc525055904" 4.	LEIAUTE	 PAGEREF _Toc525055904 \h 6
 HYPERLINK \l "_Toc525055905" 4.1 Regras dos Campos do Relatório (Leiaute)	 PAGEREF _Toc525055905 \h 7
 HYPERLINK \l "_Toc525055906" 4.2 Exemplos do Relatório	 PAGEREF _Toc525055906 \h 9

INTRODUÇÃO

Objetivo desta especificação é criar uma tela para permitir ao usuário parametrizar dados e gerar o relatório de Conferência da Declaração País-a-País -Bloco W. Este bloco foi disponibilizado na versão 3.0 do manual leiaute do fisco.

DOCUMENTOS DE REFERÊNCIA

Tela_Declaracao_Pais_a_Pais.doc
Layout_ECF.xlsx
Validacao_Bloco_W.xlsx


Tela de Parâmetros

Localização: ECF - Escrituração Contábil Fiscal >>Relatórios >> Conferência da Declaração País a País – Bloco W
Título da tela: Conferência da Declaração País a País -Bloco W


 
Campo	Tipo	Formato/Default	Obrig. 	Editável	Regra	MFS		Exercício	Texto	AAAA 	Sim	Sim	Informar o exercício que será utilizado para recuperar as Informações ECF.

Tratamentos:

Trazer o campo preenchido, com o ano atual.
Se o campo exercício, for alterado, os demais campos devem ser limpos (inclusive os campos de opções definidas com default), para serem novamente definidos.
	MFS-20554		Versão	Lista	Código - Descrição	Sim 	Sim	Permite ao usuário indicar a versão que será utilizada para recuperar as Informações ECF.

Lista de Opções Válidas:

Exibir a lista de versões da RNG00004 – Versão de layout, (a partir da versão 3.00)

Atenção: Para recuperar a versão, considerar a versão compatível com o período ‘01/01 do ano anterior’ até ‘01/01 do ano informado no exercício’.


Tratamentos:

Se este campo for alterado, os demais campos, exceto o campo exercício, devem ser limpos (inclusive os campos de opções definidas com default), para serem novamente definidos

	MFS-20554		Gravar Arquivos	Radio-Button	Arquivo Único	Sim
	Sim	Opções Válidas:

Quebra por Informações ECF
Arquivo Único

Tratamentos:

Se selecionada a opção ‘Quebra por Estabelecimentos’, será gerado um relatório por Informações ECF, com todos os registros selecionados.
Se selecionada a opção ‘Arquivo Único’, será gerado em um único relatório, contendo todas as Informações ECF recuperadas, com os dados de todos os registros selecionados.
Se este campo for alterado, os demais campos não devem ser limpos.
	MFS-20554		Informações ECF dos Estabelecimentos		
Informações ECF(*)	Check-box	Código Estab - CGC - Exercício -  Data Inicial da Escrituração (076 - XXXXXXXXXXXXXX -  01/03/2017)	-	-	Permite ao usuário selecionar um ou mais registros de Informações ECF.

Tratamento:

Recuperar apenas as Informações ECF que estão compatíveis com as opções de filtro preenchidas na tela de parametrização do relatório.
	MFS-20554		Marcar Todos	Check-box	Desmarcado	-	-	Permite ao usuário selecionar todas ou desmarcar todas as Informações ECF.

Tratamentos:

Se selecionar o check-box, todos os registros exibidos no componente de Informações serão marcados. 
Se desmarcar o check-box, o sistema deve desmarcar todos os registros de Informações ECF selecionados.
	MFS-20554		Registros
		Registros (*)	Check-box	Código - Descrição	-	-	Permite ao usuário selecionar um ou mais registros do bloco W para gerar o relatório.

Tratamentos:

Só deve ser exibido os registros, quando o campo versão estiver preenchido.
Recuperar todos os registros do bloco W de nível 2, compatível com a versão que foi indicada na tela de parâmetros do relatório, verificar os documentos Validacao_Bloco_W.xlsx 	MFS-20554		Marcar Todos	Check-box	Desmarcado	-	-	Permite ao usuário selecionar todos ou desmarcar todos os registros.

Tratamentos:

Se selecionar o check-box, todos os registros exibidos no componente de Registros serão marcados. 
Se desmarcar o check-box, o sistema deve desmarcar todos os registros do componente de Registros.
	MFS-20554		OK	Botão		-	-	Permite ao usuário gerar um relatório de conferência dos registros do Bloco W.

Tratamentos:
Se o usuário clicar em OK, sem ter selecionado pelo menos uma Informação ECF, exibir a mensagem DW00057.
Aplicar RNG00010 – Campo Obrigatório
Se não houver dados para a composição do relatório, exibir a mensagem DW00274.

Gerar o relatório conforme tópico “ HYPERLINK  \l "leiaute" 4. LEIAUTE”.	MFS-20554		Cancelar	Botão		-	-	Permite ao usuário fechar a tela e não executar o relatório.	MFS-20554		

LEIAUTE 


Origem das informações para geração do relatório:

Registros da Tela Bloco W – Declaração País a País.
Registros W100, W300


Regra de agrupamento: 
Agrupar por Informação do ECF e por registro (nível 2). 

Ordenação: 
Ordenar por código do estabelecimento, data inicial Informação ECF, código do registro (seguindo a hierarquia dos registros de acordo com o arquivo Layout_ECF.xlsx).

Quebra de Página: 
A cada quebra de página, exibir a descrição das colunas do registro.  Não deve ser feito quebra de página por registro, se o usuário parametrizar a geração para mais de um registro.
Os registros de nível maior que 2, devem ser apresentados, logo em seguida ao registro de nível imediatamente anterior (sem quebra de página).

Hierarquia:
A hierarquia dos registros deverá ser respeitada (Layout_ECF.xlsx). Uma vez que houver seleção do registro “Pai”, e este possuir registros ‘Filhos’, todas as informações serão exibidas no relatório (respeitando a ordem dos registros). Não haverá seleção individual de registros filhos para que tal hierarquia seja atendida.

Registros que devem ser exibidos e quando exibí-los:
Deve ser exibido apenas os registros que foram selecionados na parametrização e que possuam informações.

Tipos de Leiaute:
Neste relatório será gerado um tipo de leiaute: registros que não possuem tabela dinâmica.

Campos dos registros:
A disposição dos campos do registro deve ser apresentada por coluna (ordem e labels definidos nos documentos Validacao_Bloco_W.xlsx) e as informações de ocorrência em linhas.
Se na geração do relatório, for identificado que um determinado registro possui uma grande quantidade de campos, efetuar quantas quebras por linhas forem necessárias, possibilitando a exibição de todos os campos do registro. Neste cenário, se existirem mais de uma ocorrência do registro, os labels das colunas, só se repetirão se existir quebra de página (para este registro).

Formato:
Paisagem


Regras específicas:

Exibição das Informações:
Todos os campos que possuírem código e descrição devem ser exibidos concatenados. Exemplo: 4-Brasil. 


4.1 Regras dos Campos do Relatório (Leiaute)

Campo/Coluna	Tipo	Formato/Default	Regra	MFS		Cabeçalho(*)		Empresa(*)	Texto	Código - Descrição	Apresenta no lado superior esquerdo do cabeçalho, a empresa do estabelecimento, que está sendo gerado os dados do relatório. 	MFS-20554		Página X de Y	Texto	Página X de Y	Apresenta no lado superior direito do cabeçalho, o número da página atual (X) e a quantidade total de páginas do relatório (Y).	MFS-20554		Data 	Data	DD/MM/AAAAA às HH:MM:SS hs	Apresenta no lado superior direito do cabeçalho, a data, hora, minuto e segundo em que o relatório foi gerado.	MFS-20554		Título1: 
Relatório de Conferência da Declaração País a País – Bloco W		Estabelecimento	Texto	Código - Descrição	Exibe o estabelecimento de cada Informações ECF que foi recuperada.	MFS-20554		Exercício	Texto	AAAA	Exibe o exercício correspondente a cada Informações ECF, que foi recuperada.	MFS-20554		Data Inicial	Texto	DD/MM/AAAA	Exibe a data inicial correspondente a cada Informações ECF que foi recuperada.	MFS-20554		Versão	Texto	Código - Descrição	Exibe a versão correspondente a cada Informações ECF recuperada.
	MFS-20554		Forma de Tributação	Texto	Descrição	Exibe a forma de tributação correspondente a cada Informações ECF que foi recuperada.
	MFS-20554		Apuração	Texto	Descrição	Exibe a apuração correspondente a cada Informação ECF que foi recuperada.	MFS-20554		Subtítulo: 
RegistroCód Registro – Descrição do Registo		Campos do Registro “X”	Texto	- 	Exibe o nome do campo do registro que está sendo demonstrado (os campos do registro devem ser apresentados em coluna).

Tratamentos:

Apresentar todos os campos do registro (conforme o documento Validacao_Bloco_W.xlsx)

	MFS-20554		Informações das Ocorrências do Registro “X”	Texto	- 	Recupera as informações preenchidas pelo usuário em cada campo do registro (as informações das ocorrências do registro, deverão ser apresentadas em linhas).

Tratamento:
 “X” - Representa a quantidade de ocorrências que um registro pode ter. A variável “X” deverá ser substituída por uma sequência numérica iniciada pelo número 1.
	MFS-20554		Rodapé(*)		MasterSaf – Atendimento Fiscal	Texto	-	Apresentar o texto do lado inferior esquerdo.	MFS-20554		ECF – Escrituração Contábil Fiscal	Texto	-	Apresentar o texto do lado inferior direito.	MFS-20554		
4.2 Exemplos do Relatório 


Registros sem filho:


Exibição do relatório para registros que possui a hierarquia “Pai” e “Filhos” onde os filhos possuem informações:

Será apresentado as informações do registro pai e depois as informações dos registros filhos.
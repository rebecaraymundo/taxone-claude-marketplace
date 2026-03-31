# Tela_Declaracao_DEREX

> Fonte: Tela_Declaracao_DEREX.doc

THOMSON REUTERS

Tela DEREX (Bloco V)
ECF - Escrituração Contábil Fiscal (DW)

DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		14/08/2018	MFS-20276	Criação do Documento 	Alessandra Cristina Navatta		
Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc522265894" 1.	INTRODUÇÃO	 PAGEREF _Toc522265894 \h 3
 HYPERLINK \l "_Toc522265895" 2.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc522265895 \h 3
 HYPERLINK \l "_Toc522265896" 3.	TELA/MODAIS	 PAGEREF _Toc522265896 \h 3
 HYPERLINK \l "_Toc522265897" 3.1	Pesquisa de Registros	 PAGEREF _Toc522265897 \h 3
 HYPERLINK \l "_Toc522265898" 3.2	Regras dos Campos Tela Principal	 PAGEREF _Toc522265898 \h 4
 HYPERLINK \l "_Toc522265899" 3.3 Modais	 PAGEREF _Toc522265899 \h 11
 HYPERLINK \l "_Toc522265900" 4.	Permissão de exibição dos registros na tela	 PAGEREF _Toc522265900 \h 12


INTRODUÇÃO

Objetivo deste documento é criar uma tela que permita a inclusão das informações da Declaração DEREX (Bloco V). Essas informações poderão ser incluídas manualmente na tela ou por importação.

DOCUMENTOS DE REFERÊNCIA


Layout_ECF.xlsx
Regras_Gerais_DWECF.docx
Tela_Informacoes_ECF.docx
Mensagens_Sistema_DWECF.xlsx

TELA/MODAIS

Pesquisa de Registros
Localização da tela: ECF - Escrituração Contábil Fiscal >> Apuração >> Bloco V - Declaração DEREX >> Manutenção

Título da tela: Declaração DEREX (Bloco V)

Obs. As opções dos campos de pesquisa e suas opções, podem ter alguma divergência na escrita e tipo, pois serão apresentados como cadastradas no banco.

Campo	Tipo	Regra		Estabelecimento	LOV
(Tipo - Código – Descrição)	Permite que o usuário busque o registro pelo Código do Estabelecimento.		Exercício	Texto
AAAA	O usuário poderá informar o exercício. 		Data Inicial	Data
DD/MM/AAAA	O usuário poderá informar a data inicial da Informação ECF.		Versão	Lista
(Código -Descrição)	Aplicar a RNG00004 -Versão de Layout		Forma de Tributação	Lista
(Código -Descrição)	Exibe as opções abaixo:

-Lucro Real, Lucro Presumido, Lucro Arbitrado
-Imune de IRPJ 
-Isento do IRPJ 
		Apuração	Lista
(Código -Descrição)	Exibe as opções abaixo:

- Anual
- Trimestral		

Regras dos Campos Tela Principal
Localização da tela: ECF - Escrituração Contábil Fiscal >> Apuração >> Bloco V - Declaração DEREX >> Manutenção

Título da tela: Declaração DEREX (Bloco V)

Condições Gerais: Quando o usuário acessar a tela de consulta, apresentar todos os registros da tela Informações ECF.
Desabilitar os botões “Novo”, “Excluir” e “Copiar” na toolbar.


Campo	Tipo	Obrig	Ed	Formato/Default	Regra	MFS		DADOS GERAIS
As informações são referentes a um registro cadastrado na tela Informações ECF. (*)
		Estabelecimento	Texto	S	N	Tipo - Código - Descrição	Permite que o usuário visualize o estabelecimento correspondente ao registro selecionado na tabela de Informações ECF.	MFS-20276		Exercício	Texto
	S	N		Permite que o usuário visualize o exercício.	MFS-20276		Data Inicial	Texto
	S	N		Permite que o usuário visualize a data inicial.	MFS-20276		Versão	Texto	S	N		Permite que o usuário visualize a Versão do Layout utilizada para o processamento do registro.

Valores válidos:

Aplicar RNG00004 - Versão de Layout.	MFS-20276		Forma de Tributação	Texto
	S	N		Permite que o usuário visualize a forma de tributação.
	MFS-20276		Apuração	Texto
	S	N		Permite que o usuário visualize a Apuração.	MFS-20276		Registro Nível 2 - V010 – Tabela Interna (*)		Título do Registro (*)	Texto	S	N	‘OCORRÊNCIAS DO REGISTRO V10 - DEREX - Instituição	Tratamento:

-Exibir o Título ‘OCORRÊNCIAS DO REGISTRO XXXX– DSC REGISTRO’, onde o XXXX é o código do registro apresentado na grid. 
A grid principal sempre conterá o registro V010
(único registro de nível 2) (ver a hierarquia no documento: Layout_ECF.xlsx).

Se o usuário escolher um registro de Informação ECF que não teve condições prévias satisfeitas para sua ocorrência, (conforme informado no tópico  HYPERLINK  \l "Permissaodeexibicaodosreg" 4. Permissão de exibição dos registros na tela), exibir a mensagem DW00203.
	MFS-20276		Pesquisar/Filtrar	Botão		Permite ao usuário pesquisar os registros.
	MFS-20276		Adicionar	Botão		Permite ao usuário adicionar uma linha no registro.

Tratamentos:
Este botão deve ser habilitado apenas quando o campo Registro estiver preenchido.

Ao selecionar este botão exibir o  HYPERLINK  \l "modalAddeAlter" modal de adicionar.
	MFS-20276		Alterar	Botão		Permite ao usuário altere uma linha no registro.

Tratamentos:
Este botão deve ser habilitado apenas quando o campo Registro estiver preenchido e quando apenas um registro estiver marcado na grid.

Ao selecionar este botão exibir o  HYPERLINK  \l "modalAddeAlter" modal de alterar.
	MFS-20276		Remover	Botão		Permite ao usuário remover uma ou mais linhas do registro.

Tratamentos:

- Pelo menos, um registro da grid deve ser selecionado, caso contrário, exibir a mensagem DW00149.
- Ao selecionar o botão, se pelo menos um registro for selecionado na grid, aplicar a RG00041 – Botão Remover. Se o registro selecionado possuir filhos, exibir a mensagem DW00211. Se a opção selecionada for ‘Sim’, apaga o registro pai e seus filhos. Se a opção for ‘Não’, os registros não serão apagados.	MFS-20276		GRID Principal (*)


		Check-box	botão		Desmarcados	Permite ao usuário selecionar um ou mais registros, para ser (em) excluído(s) da base.
Tratamentos:
Este campo será exibido em todas as linhas que serão apresentadas na grid.
Quando um ou mais registro for selecionado e o botão ‘Remover’, acionado, os registros marcados serão removidos e excluídos da grid.
	MFS-20276		Campos (*)	Texto	S	N		
A grid será exibida com todos os campos listados nas tabelas “Validacao_Bloco_V.xlsx”, com exceção do campo “REG”, considerando como filtro a seleção do campo Versão e Registro. O label dos campos deve corresponder com a informação da coluna Rótulo.	MFS-20276		Registros Filhos	Texto	S	N	(V020: XXXXXX, V030: XXXXXX)	Exibir a quantidade de registros filhos que o registro selecionado possui

Tratamentos:

Exibir este campo apenas para os registros que na hierarquia possuem registros filhos.
(V020: XXXXXX, V030: XXXXXX)
	MFS-20276		Componentes Registros Filho – Tabela Interna e de Tabela Dinâmica (*)		Filtro de Registros		Registro	Lista	S	S	 (Código -Descrição)	Permite que usuário selecione um registro correspondente do bloco V de acordo com a versão.

Tratamento: 


Valores Válidos:

V020 - XXX
V030 - XXX

Onde ’XXX’ é a descrição do registro	MFS-20276		Título do Registro (*)	Texto	S	N		Tratamento:

- Exibir o Título ‘OCORRÊNCIAS DO REGISTRO XXXX– DSC REGISTRO’, onde o XXXX– DSC REGISTRO’ é o código e a descrição do registro apresentado na grid. 
Ex.nome a ser Exibido ‘OCORRÊNCIAS DO REGISTRO V10 - DEREX - Instituição)’.
	MFS-20276		Registro V020 (*)		Pesquisar/Filtrar	Botão		Permite ao usuário pesquisar os registros.
	MFS-20276		Adicionar	Botão		Permite ao usuário adicionar uma linha no registro.

Tratamentos:
Este botão deve ser habilitado apenas quando o campo Registro estiver preenchido.

Ao selecionar este botão exibir o  HYPERLINK  \l "modalAddeAlter" modal de adicionar.
	MFS-20276		Alterar	Botão		Permite ao usuário altere uma linha no registro.

Tratamentos:
Este botão deve ser habilitado apenas quando o campo Registro estiver preenchido e quando apenas um registro estiver marcado na grid.

Ao selecionar este botão exibir o  HYPERLINK  \l "modalAddeAlter" modal de alterar.
	MFS-20276		Remover	Botão		Permite ao usuário remover uma ou mais linhas do registro.

Tratamentos:

- Pelo menos, um registro da grid deve ser selecionado, caso contrário, exibir a mensagem DW00149.
- Ao selecionar o botão, se pelo menos um registro for selecionado na grid, aplicar a RG00041 – Botão Remover. Se o registro selecionado possuir filhos, exibir a mensagem DW00211. Se a opção selecionada for ‘Sim’, apaga o registro pai e seus filhos. Se a opção for ‘Não’, os registros não serão apagados.	MFS-20276		Check-box	botão		Desmarcados	Permite ao usuário selecionar um ou mais registros, para ser(em) excluído(s) da base.

Tratamentos:
Este campo será exibido em todas as linhas que serão apresentadas na grid.
Quando um ou mais registro for selecionado e o botão ‘Remover’, acionado, os registros marcados serão removidos e excluídos da grid.
	MFS-20276		Campos (*)	Texto	S	N		
A grid será exibida com todos os campos listados do registro V020 do arquivo “Validacao_Bloco_V.xlsx”, com exceção do campo “REG”, considerando como filtro a seleção do campo Versão e Registro. O label dos campos deve corresponder com a informação da coluna Rótulo.
	MFS-20276		Registro V030 (*):		Períodos(*)	Lista	S	N		Tratamentos:

Criar todos os meses a partir do mês da data inicial da informação ECF até dezembro.	MFS-20276		GRID dos Períodos(*)
		Campos do Registro V100 (*)	Texto	S	S		
Em cada período criado, disponibilizar os campos listados no arquivo “Validacao_Bloco_V.xlsx”, do registro V100.
 	MFS-20276		Fórmula	Texto	S	N		Em cada período criado, exibir a coluna ‘Fórmula’, após a última indicada no arquivo “Validacao_Bloco_V.xlsx”, do registro V100.	MFS-20276		Linhas(*)		
-Carregar em cada período as informações de todas as linhas do registro V100 de tabela dinâmica (conteúdo da tabela dinâmica).

Ajustes em campos:

Apenas será possível efetuar ajustes pelo usuário, no campo de Valor, desde que as regras abaixo devem sejam respeitadas:
As linhas de tipo ‘R’, não terão valor (serão sempre desabilitadas e nulas).
As linhas do tipo ‘CNA’, serão calculadas pelo sistema (de acordo com o campo fórmula da tabela dinâmica), com a ação de Salvar. 

Nos demais tipos de linha, o campo valor poderão ser alterados pelo usuário.

Coluna Fórmula:

Esta coluna deve ser preenchida, com base na coluna fórmula da tabela dinâmica do registro V100 e deve ficar nula, nas linhas que não possuírem fórmula.
	MFS-20276		     (*) Não exibir a descrição na tela.

3.3 Modais

Modal Adicionar/Alterar 

Este modal deve ser exibido se for selecionado os botões Adicionar ou Alterar na grid da tela principal ou do registro filho(*)

Ao selecionar o botão Adicionar, apresentar o título: Adicionar 
Ao selecionar o botão Alterar, apresentar o título: Alterar 

Voltar ao  HYPERLINK  \l "botaoadd" botão Adicionar
Voltar ao  HYPERLINK  \l "botaoalter" botão Alterar 
		Campos (*)		A grid será exibida com todos os campos listados nas tabelas “Validacao_Bloco_V.xlsx”, com exceção do campo “REG” considerando como filtro a seleção do campo Versão e Registro. O label dos campos deve corresponder com a informação da coluna Rótulo.

Se o usuário acessar o modal pelo botão adicionar, os campos devem ser exibidos sem informação, caso a seleção seja pelo alterar, trazer os dados já preenchidos, para que o usuário efetue a alteração desejada.	MFS-20276		OK	Botão		Habilitado	Permite ao usuário vincular (adicionar) os dados na grid

Validações:
Aplicar as regras abaixo:
RNG00011 - Duplicidade de registro;
E as validações dos campos recuperados conforme arquivos “Validacao_Bloco_V.xlsx” 

	MFS-20276		Cancelar	Botão		Habilitado	Permite ao usuário cancelar as informações que não foram vinculadas na tela.
	MFS-20276		     (*) Não exibir a descrição na tela.


Permissão de exibição dos registros na tela


Reg.	Descrição	Regra de Exibição do Registro na Tela	MFS		V010	DEREX - Instituição	Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘Declaração sobre utilização dos recursos em moeda estrangeira decorrentes do recebimento de exportações (DEREX)’ estiver desmarcado.
	MFS-20276		V020	Responsável pela Movimentação	Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘Declaração sobre utilização dos recursos em moeda estrangeira decorrentes do recebimento de exportações (DEREX)’ estiver desmarcado.
	MFS-20276		V030	DEREX – Período - Mês	Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘Declaração sobre utilização dos recursos em moeda estrangeira decorrentes do recebimento de exportações (DEREX)’ estiver desmarcado.
	MFS-20276		V100	Demonstrativo dos recursos em moeda estrangeira decorrentes do recebimento de exportações	Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘Declaração sobre utilização dos recursos em moeda estrangeira decorrentes do recebimento de exportações (DEREX)’ estiver desmarcado.
	MFS-20276
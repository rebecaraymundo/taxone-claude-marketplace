# Tela_Declaracao_Pais_a_Pais

> Fonte: Tela_Declaracao_Pais_a_Pais.doc

THOMSON REUTERS

Tela Declaração País a País (Bloco W)
ECF - Escrituração Contábil Fiscal (DW)

DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		12/06/2018	MFS-19131	Criação do Documento 	Alessandra Cristina Navatta		16/08/2018	MFS-20275	Inclusão da mensagem DW00203 nos registros W200 e W250	Alessandra Cristina Navatta		
Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc521055538" 1.	INTRODUÇÃO	 PAGEREF _Toc521055538 \h 3
 HYPERLINK \l "_Toc521055539" 2.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc521055539 \h 3
 HYPERLINK \l "_Toc521055540" 3.	TELA/MODAIS	 PAGEREF _Toc521055540 \h 3
 HYPERLINK \l "_Toc521055541" 3.1	Pesquisa de Registros	 PAGEREF _Toc521055541 \h 3
 HYPERLINK \l "_Toc521055542" 3.2	Regras dos Campos Tela Principal	 PAGEREF _Toc521055542 \h 4
 HYPERLINK \l "_Toc521055543" 3.3 Modais	 PAGEREF _Toc521055543 \h 10
 HYPERLINK \l "_Toc521055544" 4.	Permissão de exibição dos registros na tela	 PAGEREF _Toc521055544 \h 12
 HYPERLINK \l "_Toc521055545" 5.	Permissão de exibição dos registros de nível 3	 PAGEREF _Toc521055545 \h 12


INTRODUÇÃO

Objetivo deste documento é criar uma tela que permita a inclusão das informações da Declaração País a País (Bloco W). Essas informações poderão ser incluídas manualmente na tela ou por integração.

DOCUMENTOS DE REFERÊNCIA


Layout_ECF.xlsx
Regras_Gerais_DWECF.docx
Tela_Informacoes_ECF.docx
Mensagens_Sistema_DWECF.xlsx

TELA/MODAIS

Pesquisa de Registros
Localização da tela: ECF - Escrituração Contábil Fiscal >> Apuração >> Bloco W - Declaração País a País >> Manutenção

Título da tela: Declaração País a País (Bloco W)


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
Localização da tela: ECF - Escrituração Contábil Fiscal >> Apuração >> Bloco W - Declaração País a País >> Manutenção

Título da tela: Declaração País a País (Bloco W)

Condições Gerais: Quando o usuário acessar a tela de consulta, apresentar todos os registros da tela Informações ECF.
Desabilitar os botões “Novo”, “Excluir” e “Copiar” na toolbar.

As regras destacadas em amarelo (e com fonte vermelha), não serão implementadas neste momento.


Campo	Tipo	Obrig	Ed	Formato/Default	Regra	MFS		DADOS GERAIS
As informações são referentes a um registro cadastrado na tela Informações ECF. (*)
		Estabelecimento	Texto	S	N	Tipo - Código - Descrição	Permite que o usuário visualize o estabelecimento correspondente ao registro selecionado na tabela de Informações ECF.	MFS-19131		Exercício	Texto
	S	N		Permite que o usuário visualize o exercício.	MFS-19131		Data Inicial	Texto
	S	N		Permite que o usuário visualize a data inicial.	MFS-19131		Versão	Texto	S	N		Permite que o usuário visualize a Versão do Layout utilizada para o processamento do registro.

Valores válidos:

Aplicar RNG00004 - Versão de Layout.	MFS-19131		Forma de Tributação	Texto
	S	N		Permite que o usuário visualize a forma de tributação.
	MFS-19131		Apuração	Texto
	S	N		Permite que o usuário visualize a Apuração.	MFS-19131		SELEÇÃO DO REGISTRO
		Registro	Lista	S	S	 (Código -Descrição)	Permite que usuário selecione um registro correspondente do bloco W de acordo com a versão.

Tratamento: 

Valores Válidos:

W100 - XXX
W300 -XXX

Onde ’XXX’ é a descrição do registro

-Apenas os registros de nível 2 devem ser apresentados na grid principal. (ver a hierarquia no documento: Layout_ECF.xlsx).

Se o usuário escolher um registro que não teve condições prévias satisfeitas para sua ocorrência, (conforme informado no tópico  HYPERLINK  \l "Permissaodeexibicaodosreg" 4. Permissão de exibição dos registros na tela), exibir a mensagem DW00203 para cada registro encontrado.

	MFS-19131		Título do Registro (*)	Texto	S	N		Tratamento:

-O título só deve ser exibido, se for selecionada uma versão e um registro de na tela principal.  

-Exibir o Título ‘OCORRÊNCIAS DO REGISTRO XXXX– DSC REGISTRO’, onde o XXXX é o código do registro apresentado na grid. 
Ex. Selecionado o registro W100, nome a ser Exibido ‘OCORRÊNCIAS DO REGISTRO W100 - Informações sobre o Grupo Multinacional e a Entidade Declarante – Declaração País-a-País)’.	MFS-19131		Pesquisar	Botão		Permite ao usuário pesquisar os registros.
	MFS-19131		Adicionar	Botão		Permite ao usuário adicionar uma linha no registro.

Tratamentos:
Este botão deve ser habilitado apenas quando o campo Registro estiver preenchido.

Ao selecionar este botão exibir o  HYPERLINK  \l "modalAddeAlter" modal de adicionar.
	MFS-19131		Alterar	Botão		Permite ao usuário altere uma linha no registro.

Tratamentos:
Este botão deve ser habilitado apenas quando o campo Registro estiver preenchido e quando apenas um registro estiver marcado na grid.

Ao selecionar este botão exibir o  HYPERLINK  \l "modalAddeAlter" modal de alterar.
	MFS-19131		Remover	Botão		Permite ao usuário remover uma ou mais linhas do registro.

Tratamentos:

- Pelo menos, um registro da grid deve ser selecionado, caso contrário, exibir a mensagem DW00149.
- Ao selecionar o botão, se pelo menos um registro for selecionado na grid, aplicar a RG00041 – Botão Remover. Se o registro selecionado possuir filhos, exibir a mensagem DW00211. Se a opção selecionada for ‘Sim’, apaga o registro pai e seus filhos. Se a opção for ‘Não’, os registros não serão apagados.	MFS-19131		GRID Principal (*)


		Check-box	botão		Desmarcados	Permite ao usuário selecionar um ou mais registros, para ser(em) excluído(s) da base.

Tratamentos:
Este campo será exibido em todas as linhas que serão apresentadas na grid.
Quando um ou mais registro for selecionado e o botão ‘Remover’, acionado, os registros marcados serão removidos e excluídos da grid.
	MFS-19131		Campos (*)	Texto	S	N		
A grid será exibida com todos os campos listados nas tabelas “Validacao_Bloco_W.xlsx”, com exceção do campo “REG”, considerando como filtro a seleção do campo Versão e Registro. O label dos campos deve corresponder com a informação da coluna Rótulo.
	MFS-19131		Registros Filhos	Texto	S	N		Exibir a quantidade de registros filhos que o registro selecionado possui

Tratamentos:

Exibir este campo apenas para os registros que na hierarquia possuem registros filhos.	MFS-19131		Componentes Registros Filho (*)		Pesquisar	Botão		Permite ao usuário pesquisar os registros.
	MFS-19131		Adicionar	Botão		Permite ao usuário adicionar uma linha no registro.

Tratamentos:
Este botão deve ser habilitado apenas quando o campo Registro estiver preenchido.

Ao selecionar este botão exibir o  HYPERLINK  \l "modalAddeAlter" modal de adicionar.
	MFS-19131		Alterar	Botão		Permite ao usuário altere uma linha no registro.

Tratamentos:
Este botão deve ser habilitado apenas quando o campo Registro estiver preenchido e quando apenas um registro estiver marcado na grid.

Ao selecionar este botão exibir o  HYPERLINK  \l "modalAddeAlter" modal de alterar.
	MFS-19131		Remover	Botão		Permite ao usuário remover uma ou mais linhas do registro.

Tratamentos:

- Pelo menos, um registro da grid deve ser selecionado, caso contrário, exibir a mensagem DW00149.
- Ao selecionar o botão, se pelo menos um registro for selecionado na grid, aplicar a RG00041 – Botão Remover. Se o registro selecionado possuir filhos, exibir a mensagem DW00211. Se a opção selecionada for ‘Sim’, apaga o registro pai e seus filhos. Se a opção for ‘Não’, os registros não serão apagados.	MFS-19131		Grid Registros Filhos (*)		Check-box	botão		Desmarcados	Permite ao usuário selecionar um ou mais registros, para ser(em) excluído(s) da base.

Tratamentos:
Este campo será exibido em todas as linhas que serão apresentadas na grid.
Quando um ou mais registro for selecionado e o botão ‘Remover’, acionado, os registros marcados serão removidos e excluídos da grid.
	MFS-19131		Campos (*)	Texto	S	N		
A grid será exibida com todos os campos listados nas tabelas “Validacao_Bloco_W.xlsx”, com exceção do campo “REG”, considerando como filtro a seleção do campo Versão e Registro. O label dos campos deve corresponder com a informação da coluna Rótulo.
	MFS-19131		Registros Filhos	Texto	S	N		Exibir a quantidade de registros filhos que o registro selecionado possui

Tratamentos:

Exibir este campo apenas para os registros que na hierarquia possuem registros filhos.	MFS-19131		     (*) Não exibir a descrição na tela.

3.3 Modais

Modal Adicionar/Alterar 

Este modal deve ser exibido se for selecionado os botões Adicionar ou Alterar na grid da tela principal ou do registro filho(*)

Ao selecionar o botão Adicionar, apresentar o título: Adicionar 
Ao selecionar o botão Alterar, apresentar o título: Alterar 

Voltar ao  HYPERLINK  \l "botaoadd" botão Adicionar
Voltar ao  HYPERLINK  \l "botaoalter" botão Alterar 
		Campos (*)		A grid será exibida com todos os campos listados nas tabelas “Validacao_Bloco_W.xlsx”, com exceção do campo “REG” considerando como filtro a seleção do campo Versão e Registro. O label dos campos deve corresponder com a informação da coluna Rótulo.

Se o usuário acessar o modal pelo botão adicionar, os campos devem ser exibidos sem informação, caso a seleção seja pelo alterar, trazer os dados já preenchidos, para que o usuário efetue a alteração desejada.	MFS-19131		OK	Botão		Habilitado	Permite ao usuário vincular (adicionar) os dados na grid

Validações:
Aplicar as regras abaixo:
RNG00011 - Duplicidade de registro;
E as validações dos campos recuperados conforme arquivos “Validacao_Bloco_W.xlsx” 

Para o registro W100:

Botão Alterar:
-No momento de alterar o dado (tela ou importação), se o registro não cumprir mais as regras de exibição dos registros de nível 3, e estes já existirem na base, exibir a mensagem DW00180 e não alterar o registro.

-No momento de alterar o dado (tela ou importação), se for identificado alteração no campo Moeda do registro W100 de real (‘BRL’) para qualquer outra moeda ou de uma moeda estrangeira para real (‘BRL’) e se existir registro filho W200 para este registro, exibir a mensagem DW00180 e não alterar o registro.

Para o registro W200:

Botão Adicionar:
Verificar se as condições prévias foram satisfeitas para sua ocorrência, (conforme informado no tópico  HYPERLINK  \l "Permissaodeexibicaodosreg" 5. Permissão de exibição dos registros de nível 3), caso não tenha sido atendida (tela e importação), exibir a mensagem DW00271 e não permitir gravar o registro.
	MFS-19131		Cancelar	Botão		Habilitado	Permite ao usuário cancelar as informações que não foram vinculadas na tela.
	MFS-19131		     (*)Não exibir a descrição na tela.


Permissão de exibição dos registros na tela


Reg.	Descrição	Regra de Exibição do Registro na Tela	MFS		HYPERLINK \l "RX280"W100	Informações Sobre o Grupo Multinacional e a Entidade Declarante	Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘Entidade Integrante de Grupo Multinacional estiver desmarcado.
	MFS-19131		W200	Declaração País-a-País 	Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘Entidade Integrante de Grupo Multinacional estiver desmarcado.
	MFS-20275		W250	Declaração País-a-País – Entidades Integrantes	Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘Entidade Integrante de Grupo Multinacional estiver desmarcado.
	MFS-20275		W300	
Observações Adicionais	Apresentar a mensagem DW00203 se na tela Informações ECF, o campo ‘Entidade Integrante de Grupo Multinacional estiver desmarcado.
	MFS-19131		

Permissão de exibição dos registros de nível 3

Reg.	Descrição	Regra de Exibição do Registro na Tela	MFS		HYPERLINK \l "RX280"W200	Declaração País a País	Apresentar a mensagem DW00271 se as regras abaixo não forem atendidas:

- Campo IND_CONTROLADORA - Indicador de Entidade Controladora Final do registro W100 for igual a S e se o campo IND_ENTREGA - Entidade Responsável pela Entrega for igual a 2,ou
- Se o campo IND_ENTREGA - Entidade Responsável pela Entrega for igual a 3.	MFS-19131
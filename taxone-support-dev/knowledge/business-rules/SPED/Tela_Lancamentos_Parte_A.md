# Tela_Lancamentos_Parte_A

> Fonte: Tela_Lancamentos_Parte_A.doc

THOMSON REUTERS

Tela de Lançamentos da Parte A (M300, M350)
ECF - Escrituração Contábil Fiscal (DW)


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		27/11/2017	MFS-14939	Criação do Documento	Alessandra Cristina Navatta		18/01/2018	MFS-15810	Inclusão da aba Contas da Parte B	Alessandra Cristina Navatta		19/03/2018	MFS-17180	Inclusão de filtro Status (no botão Abre) 	Alessandra Cristina Navatta		


Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc505681456" 1.	INTRODUÇÃO	 PAGEREF _Toc505681456 \h 3
 HYPERLINK \l "_Toc505681457" 2.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc505681457 \h 3
 HYPERLINK \l "_Toc505681458" 3.	TELA/MODAIS	 PAGEREF _Toc505681458 \h 3
 HYPERLINK \l "_Toc505681459" 3.1 Pesquisa de Registros	 PAGEREF _Toc505681459 \h 3
 HYPERLINK \l "_Toc505681460" 3.2	Regras dos Campos Tela Principal	 PAGEREF _Toc505681460 \h 5
 HYPERLINK \l "_Toc505681461" 3.3	Modais	 PAGEREF _Toc505681461 \h 29



INTRODUÇÃO

Objetivo desta especificação é criar a tela de Lançamentos da Parte A (M300, M350) 
Através da tela de Lançamentos da Parte A (M300, M350), o usuário pode realizar e ou/ visualizar os seguintes relacionamentos:
- Lançamentos da Parte A (M300, M350) com Contas e Lançamentos da Parte B (M410)
- Lançamentos da Parte A (M300, M350) com contas contábeis (apenas visualizar)
- Lançamentos da Parte A (M300, M350) com Lançamentos contábeis 
- Lançamentos da Parte A (M300, M350) com Processos Administrativos ou Judiciais


DOCUMENTOS DE REFERÊNCIA


Mensagens_Sistema_DWECF.xlsx
Regras_Gerais_DWECF.docx
MTZ_Processamento_em_Lote.docx
Tela_Abertura_de_Apuracao.doc
Tela_Associacao_da_Tabela_Dinamica_com_o_Plano_Empresa.doc
Tela_Lancamentos_da_Parte_B-M410.doc


TELA/MODAIS


3.1 Pesquisa de Registros

Localização da tela: 
ECF - Escrituração Contábil Fiscal >> Apuração >> Ajustes Manuais >> Lançamentos da Parte A (M300, M350)

Título da tela: Lançamentos da Parte A (M300, M350)

Condições Gerais: Recuperar apenas as aberturas com status diferente de “Apuração em Aberto” e A00.

Obs. As opções dos campos de pesquisa e suas opções, podem ter alguma divergência na escrita e tipo, pois serão apresentados como cadastradas no banco.


Campo	Tipo	Regra		Estabelecimento	LOV
(Tipo - Código – Descrição)	Permite que o usuário busque o registro pelo Código do Estabelecimento.		Exercício	Texto
(AAAA)
	O usuário poderá informar o exercício. 


		Data Inicial	Data
DD/MM/AAAA	O usuário poderá informar a data inicial da Informação ECF.		Versão	Lista
(Código -Descrição)	Aplicar a RNG00004 (Versão de Layout)		Forma de Tributação	Lista
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

Localização da tela: ECF - Escrituração Contábil Fiscal >> Apuração >> Ajustes Manuais >> Lançamentos da Parte A (M300, M350)

Título da tela: Lançamentos da Parte A (M300, M350)

Considerações: Desabilitar os botões “Novo” e “Excluir” na toolbar.

Recuperar apenas as aberturas com status diferente de “Apuração em Aberto” e A00, apresentando todos os registros correspondentes aos registros abaixo processados pela rotina de processamento em lotes cujo campo “Tipo” da tabela dinâmica seja igual a “E” ou “CA” a forma de tributação calculada no processamento em lotes:
M300A – PJ em Geral
M300B - Financeiras
M300C - Seguradoras ou Entidades Abertas de Previdência Complementar
M350A – PJ em Geral
M350B – Financeiras
M350C - Seguradoras ou Entidades Abertas de Previdência Complementar

Permitir edição do registro apenas quando o status da abertura de apuração correspondente ao registro for diferente de “Aguardando Alteração Manual” e “Cálculo Realizado”. Caso contrário, aplicar a RNG00018 - Alteração de tela com controle de status da abertura da apuração.

Se durante o processamento em lote, for selecionada a opção “Manter Ajustes Manuais Realizados” os dados incluídos os alterados manualmente nesta tela deverão ser visualizados conforme ajuste manual realizado antes da nova importação dos saldos com a opção manter ajustes manuais realizados desde que os critérios definidos na RNI10.03 (do documento MTZ_Processamento_em_Lote.docx) sejam atendidos. 

Aplicar RNG00010- Campo Obrigatório.

As regras destacadas em amarelo (e com fonte vermelha), não serão implementadas neste momento.


Campo	Tipo	Obrig	Ed	Formato/Default	Regra	OS/CH/WI		Mensagem Explicativa (*)	Texto	S	N	-	
Ao abrir a tela, exibir a mensagem abaixo:

"Ao efetuar qualquer alteração nesta tela, será necessário executar o cálculo no Processamento em Lote para a atualização dos registros com os dados informados”.
	MFS-14939		DADOS GERAIS		Estabelecimento	Texto	S	N	Tipo - Código – Descrição	Permite que o usuário visualize o Estabelecimento da apuração que foi recuperada 	MFS-14939		Exercício 	Texto	S	N	AAAA	Exibe o exercício correspondente a abertura da apuração que deu origem ao lançamento”.
	MFS-14939		Data Inicial	Texto	S	N	DD/MM/AAAA	Exibe a Data Inicial correspondente a abertura da apuração que deu origem ao lançamento”
	MFS-14939		Versão	Texto	S	N		Permite que o usuário visualize a Versão do Layout utilizada para o processamento do registro.

Valores válidos:

Aplicar RNG00004 (Versão de Layout).	MFS-14939		Forma de Tributação	Texto	S	N		Exibe a forma de tributação do registro selecionado.

Conteúdos Válidos:
- Lucro Real
- Lucro Presumido,
-Lucro Arbitrado
-Imune de IRPJ 
-Isento do IRPJ 
	MFS-14939		Apuração	Texto	S	N		Exibe a apuração do registro selecionado.

Conteúdos Válidos:
- Anual
- Trimestral
	MFS-14939		Período de Apuração	Texto	S	N		Exibe o Período de apuração do registro selecionado.

Conteúdos Válidos:
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
- 1º Trimestre
- 2º Trimestre
- 3º Trimestre
- 4º Trimestre
	MFS-14939		Registro	Lista	S	S		Conteúdos Válidos:
M300A - *(Inserir descrição do registro)
M300B - *(Inserir descrição do registro)
M300C - *(Inserir descrição do registro)
M350A - *(Inserir descrição do registro)
M350B - *(Inserir descrição do registro)
M350C - *(Inserir descrição do registro)

Tratamento:

-Recuperar os dados da tabela dinâmica, considerando como filtro os campos: Registro e DSC_RECORD.
OBS: Onde contem o símbolo (*) Inserir a descrição do registro correspondente, concatenado com o número do Registro (Ex: M300 – Lançamentos da Parte A do e-Lalur .)

	MFS-14939		Linha do Registro	LOV	S	S	Código - Descrição	Permite o usuário selecionar a linha (com sua respectiva descrição) da tabela dinâmica 

Tratamentos:

Recupera o registro pela linha ou descrição.	MFS-14939		Tributo	Texto	S	N	Desabilitado	Exibe o tipo de tributo.

Tratamentos:

Opções válidas:

 -Imposto de Renda Pessoa Jurídica
-Contribuição Social sobre o Lucro Líquido

- Este campo deve ser preenchido pelo sistema, com base no preenchimento do campo Registro.

- Se o campo Registro iniciar com M300, exibir “Imposto de Renda Pessoa Jurídica”, se o registro iniciado com M350, apresentar “Contribuição Social sobre o Lucro Líquido”. 
	MFS-14939		INFORMAÇÕES DO LANÇAMENTO DA PARTE A (M300, M350)		Tipo de Lançamento	Texto	S	N		Exibe a Descrição do tipo de lançamento do registro selecionado

Conteúdos Válidos:
-Adição
-Exclusão
-Compensação de Prejuízo
–Lucro	MFS-14939		Tipo de Relacionamento	Texto	S	N		Exibe o tipo de relacionamento do Lançamento da Parte A (M300, M350) com a parte B e plano de contas.

Conteúdos Válidos:

Com Conta da Parte B
Com Conta Contábil
Com Conta da Parte B e Conta Contábil
Sem Relacionamento

Tratamentos:

Se existir somente conta da parte B associada ao Lançamento da Parte A (M300, M350):Preencher com “Com Conta da Parte B”

Se existir somente conta contábil associada ao Lançamento da Parte A (M300, M350):Preencher com “Com Conta Contábil”

Se existir conta da parte B e conta contábil associada ao Lançamento da Parte A (M300, M350): Preencher com “Com conta da Parte B e Conta Contábil”

Se não existir conta da parte B e conta contábil associada ao Lançamento da Parte A (M300, M350):Preencher com “Sem Relacionamento”


Quando o Tipo de Relacionamento “Com Conta da parte B e Conta Contábil” efetuar a validação abaixo:

- Se o parâmetro ‘Validar se o Somatório das Contas da Parte B é igual ao Somatório das Contas Contábeis’ na tela de Informações ECF aba (LALUR e LACS), estiver marcado, e se o tipo de relacionamento do lançamento for ‘Com Conta da Parte B e Conta Contábil’ verificar se os campos ‘Somatório das Contas da Parte B’ e ‘Somatório das Contas Contábeis’ são iguais. Caso diferentes, apresentar a mensagem DW00147. 
 	MFS-14939
MFS-15810		Exibição do conteúdo do campo Valor	Lista	N	S	Default (quando o campo for habilitado): Somatório das Contas da Parte B	Permite selecionar como será composto o valor que será exibido no campo “Valor (da parte A)*”.

Tratamentos:


Somente deve estar habilitado e possível de alteração, se o Tipo de Relacionamento for “Com conta da Parte B e Conta Contábil”. Neste caso, o campo tem valor default Somatório das Contas da Parte B.
Caso o campo esteja desabilitado, nenhuma opção deve estar selecionada.

Importante: Esta regra não altera o calculo do somatório das contas contábeis e das contas da parte B. Apenas altera a composição do Valor da parte A, com base na escolha do usuário.

Opções Validas:

Somatório das Contas da Parte B
Somatório das Contas Contábeis
Somatório das Contas Contábeis com o somatório das Contas da Parte B

Se o tipo de relacionamento for alterado, limpar a informação deste campo.		Valor (da parte A)*	Texto	S	S	Default: Desabilitado

Formato:
xxx.xxx,xx	
Exibe o total calculado ou informado para o Lançamento da Parte A (M300, M350).

Este campo corresponde ao total utilizado de todas as contas contábeis que foram processadas na rotina de importação dos saldos do processamento ou, corresponde ao valor digitado pelo usuário.


Tratamentos:

- Se o Tipo de Relacionamento for igual “Sem Relacionamento”, habilitar o campo para edição permitindo que o usuário informe ou altere o valor. Para os demais tipo de relacionamento, este campo deve ficar desabilitado.

 - Para este campo deve ser exibido do lado direito do campo, o ícone  EMBED PBrush   e o tooltip ‘Para valores negativos, insira o sinal ‘-‘’.


Preenchimento do campo valor:

Se tipo de relacionamento = “Sem Relacionamento”: 
Valor digitado no campo.

Se tipo de relacionamento = “Com Conta da Parte B”:
Valor informado no campo “Somatório das Contas da Parte B”.

Se tipo de relacionamento = “Com Conta Contábil”:
Valor informado no campo “Somatório das Contas Contábeis”

Se tipo de relacionamento = “Com Conta da Parte B e Conta Contábil”, verificar a informação do campo “Exibição do conteúdo do campo Valor”: 


Se a opção Somatório das Contas da Parte B estiver selecionada, exibir no campo Valor, o resultado das contas da parte B (valor informado no campo “Somatório das Contas da Parte B”). 

Se a opção Somatório das Contas Contábeis com o somatório das Contas da Parte B estiver selecionada, exibir no campo Valor a soma dos campos “Somatório das Contas da Parte B” e “Somatório das Contas Contábeis”.

Se a opção Somatório das Contas Contábeis estiver selecionada, exibir no campo Valor, o resultado do campo “Somatório das Contas Contábeis”. 	MFS-14939
MFS-15810		Somatório das Contas da Parte B	Texto	S	N	Default: Desabilitado

Formato:
xxx.xxx,xx	Exibe a somatória do valor referente às Contas da Parte B associadas na aba ‘Contas da Parte B – Ajustes (M305/M355)’.


Tratamentos:

Este campo deve ser exibido sempre desabilitado e será preenchido pelo sistema.

Quando o tipo de relacionamento for ‘Com Conta da Parte B’ ou ‘Com Conta da Parte B e Conta Contábil’ e existir dados na aba ‘Contas da Parte B – Ajustes (M305/M355)’, somar o valor das contas da parte B associadas à linha da tabela dinâmica.
Para os demais tipos de relacionamento, ou se não existir dados na aba ‘Contas da Parte B – Ajustes (M305/M355)’, o campo deve ficar desabilitado e sem preenchimento.
	MFS-15810		Somatório das Contas Contábeis	Texto	S	N	Default: Desabilitado

Formato:
xxx.xxx,xx	Exibe a somatória do valor referente às Contas Contábeis associadas na aba ‘Conta Contábil’.


Tratamentos:

Este campo deve ser exibido sempre desabilitado e será preenchido pelo sistema.

Quando o tipo de relacionamento for ‘Com Conta Contábil’ ou ‘Com conta da Parte B e Conta Contábil’ e existir dados na aba ‘Conta Contábil’, somar o valor da coluna  HYPERLINK  \l "Saldo" Saldo somente para as contas que não possuem valor na coluna Lançamentos/Ajustes com o valor das linhas que possuem a coluna  HYPERLINK  \l "Lançamentos_Ajustes" Lançamentos/Ajustes preenchida.
Para os demais tipos de relacionamento, ou se não existir dados na aba ‘Conta Contábil’, o campo deve ficar desabilitado e sem preenchimento.
	MFS-14939		Histórico	Texto	N	S		Exibe o Histórico do Lançamento da Parte A (M300, M350)


Tratamentos:

Se o Valor (da parte A)* for diferente de zero o campo Histórico deve ser obrigatório. 
	MFS-14939		Aba: Contas da Parte B – Ajustes (M305/M355)		Adicionar	Botão	-	-	Default:
Habilitado	Cria um registro na aba Contas da Parte B – Ajustes (M305/M355).

Tratamentos:

Ao acionar este botão, abrir o modal “ HYPERLINK  \l "modalAdicionarParteB" Adicionar Contas da Parte B - Ajustes (M305/M355)” 

Se o Valor (da parte A)* for diferente de zero o campo Histórico deve ser obrigatório. 

	MFS-15810		Alterar	Botão	-	-	Default:
Desabilitado	Permite alterar um registro selecionado na grid da aba Contas da Parte B – Ajustes (M305/M355).

Tratamentos:


Ao acionar este botão, abrir o modal  HYPERLINK  \l "modalAdicionarParteB" “Alterar Contas da Parte B - Ajustes (M305/M355)” e aplicar a RNG00016 - Acesso à Tela .

Se nenhum registro da grid for selecionado, exibir a mensagem DW00149.

Se o Valor (da parte A)* for diferente de zero o campo Histórico deve ser obrigatório. 

	MFS-15810		Remover	Botão	-	-	L	Permite remover um ou mais registros que foram selecionados na grid da aba Contas da Parte B – Ajustes (M305/M355).

Tratamentos:

Se nenhum registro da grid for selecionado, exibir a mensagem DW00149.


Ao remover um ajuste, exibir a mensagem DW00169.

Se o usuário selecionar ‘Sim’, o ajuste será excluído. Se ‘Não’, o registro não será excluído da base.

Após a remoção do ajuste, deve ser efetuada a atualização dos valores seguindo as regras da RNG00044 - Cálculo do Registro M500 
	MFS-15810		Grid de CONTAS DA PARTE B - AJUSTES (M305/M355)	MFS-15810		Check-Box		Permite ao usuário selecionar um ou mais registros.	MFS-15810		Cód. da Conta da Parte B 	Texto	S	N	Código e Descrição	Permite que o usuário visualize a conta e descrição da parte B cadastrada.


	MFS-15810		Valor 	Texto	S	N	xxx.xxx,xx	Exibe o Valor da conta da parte B .

	MFS-15810		Ind. do Valor	Texto	S	N		Exibe a Descrição do indicador do valor do ajuste da conta da parte B”

Conteúdos Válidos:
- Débito
–Crédito	MFS-15810		Histórico	Texto	S	N		Exibe o histórico do ajuste da parte B.
	MFS-15810		Aba: Contas Contábeis		Mensagem Explicativa (*)

Para as Contas Contábeis que possuem o status “Contas Contábeis com Lançamentos”, será necessário remover os Lançamentos Contábeis vinculados para que o status seja alterado para “Desconsiderar Movimento”.		Pesquisar	botão	-	-	-	Permite ao usuário pesquisar um ou mais registros.

Tratamento:

Permitir pesquisa pelos campos: Staus, Código da Conta Contábil, Descrição da Conta Contábil, Código do Centro de Custo, Descrição do Centro de Custo, Saldo, Lançamentos/Ajustes, Valor à Considerar e Justificativa. 
	MFS-14939		Adicionar Lançamentos Contábeis	Botão	-	-	Default: Desabilitado	Permite que o usuário associe lançamentos contábeis às contas contábeis selecionadas na grid e/ou informe valores 

Tratamentos:

Se não existir nenhuma conta contábil selecionada ou houver a seleção de mais de uma conta contábil, desabilitar este botão.

Se o usuário selecionar alguma conta contábil, habilitar este botão.

Quando acionado, abrir o  HYPERLINK  \l "ModalAdicionarLancamento" modal “Adicionar Lançamentos Contábeis”. 

Se o Valor (da parte A)* for diferente de zero o campo Histórico deve ser obrigatório. 


Para as contas contábeis associadas a linha da tabela dinâmica cujo tipo de relacionamento foi criado com base na parametrização realizada na tela Informações ECF na aba LALUR e LACS  campo  Incluir Lançamento automático com relacionamento selecionado, para tais contas contábeis, não será permitida a inclusão de qualquer tipo de ajuste manual, neste cenário este botão deve estar desabilitado. Para maiores esclarecimentos verificar MTZ_Processamentos (RNC03).	MFS-14939		Alterar Valores	Botão	-	-	Default: Desabilitado	
Permite ao usuário alterar os valores que serão considerados para a conta contábil.

Tratamentos:

Este botão deverá estar habilitado para seleção quando uma conta for selecionada na grid.

Quando acionado habilita o  HYPERLINK  \l "ModalAlterarValores" modal Alterar Valores 

Se o Valor (da parte A)* for diferente de zero o campo Histórico deve ser obrigatório. 

	MFS-14939		Desconsiderar Movimento	Botão	-	-	
	Permite alterar o status da conta contábil para desconsiderar movimento.

Tratamento:

Se nenhuma conta for selecionada, e for acionado este botão, exibir a mensagem DW00149.
Se o Valor (da parte A)* for diferente de zero o campo Histórico deve ser obrigatório. 


Funcionamento dos Status:

O status inicial das linhas após a Importação dos Saldos deve ser “Considerar Movimento”. 

Após a seleção das contas e da ação do botão ”Desconsiderar Movimento” o status das linhas da grid poderá ser alterado para “Desconsiderar Movimento”, se as regras abaixo forem atendidas:


O status será alterado se não houver Lançamentos Contábeis vinculados (modal Adicionar Lançamentos Contábeis) para estas contas e se o status inicial delas estiverem como “Considerar Movimento”. Para as contas selecionadas que não possuem lançamentos contábeis vinculados, mas que já estão com o status de “Desconsiderar Movimento”, nada será alterado. 

Se pelo menos uma conta contábil que está selecionada na grid, estiver com status igual a considerar movimento e possuir pelo menos um lançamento contábil  associado exibir a mensagem DW00148. 
Se for escolhida a opção “Não”: Fechar a mensagem e retornar à tela principal, deixando as contas contábeis que possuem lançamentos contábeis vinculados, sem alteração de status (ou seja, igual a Considerar Movimento), e as demais que não possuem lançamentos vinculados (com o status ajustado, para Desconsiderar Movimento).
Se for escolhida a opção “Sim”: Remover todos os lançamentos associados das contas com lançamentos contábeis, com status inicial de considerar movimento (atualizando o campo Status, para Desconsiderar Movimento de todas as contas).


Criar mensagem para o cenário: Para as contas contábeis associadas a linha da tabela dinâmica cujo tipo de relacionamento foi criado com base na parametrização realizada na tela Informações ECF na aba LALUR e LACS  campo  Incluir Lançamento automático com relacionamento selecionado, para tais contas contábeis, não será permitida a inclusão de qualquer tipo de ajuste manual, neste cenário este botão deve estar desabilitado. Para maiores esclarecimentos verificar MTZ_Processamentos (RNC03).	MFS-14939		Considerar Movimento	Botão	-	-		Permite alterar o status da conta contábil para considerar movimento.

Tratamento:

Se nenhuma conta for selecionada, e for acionado este botão, exibir a mensagem DW00149.
Se o Valor (da parte A)* for diferente de zero o campo Histórico deve ser obrigatório. 


Funcionamento dos Status:
O status inicial das linhas após a Importação dos Saldos deve ser “Considerar Movimento”. 

Após a seleção das contas e da ação do botão ”Considerar Movimento” o status das linhas da grid poderá ser alterado para “Considerar Movimento”, se as regras abaixo forem atendidas:
O status será alterado se não houver Lançamentos Contábeis vinculados (modal Adicionar Lançamentos Contábeis) para estas contas e se o status inicial delas estiverem como “Desconsiderar Movimento”. Para as contas selecionadas que não possuem lançamentos contábeis vinculados, mas que já estão com o status de “Considerar Movimento”, nada será alterado. 
Se pelo menos uma conta contábil que está selecionada na grid, estiver com status igual a Desconsiderar movimento e possuir pelo menos um lançamento contábil associado exibir a mensagem DW00148. 
Se for escolhida a opção “Não”: Fechar a mensagem e retornar à tela principal, deixando as contas contábeis que possuem lançamentos contábeis vinculados, sem alteração de status (ou seja, igual a Desconsiderar Movimento), e as demais que não possuem lançamentos vinculados (com o status ajustado, para Considerar Movimento).
Se for escolhida a opção “Sim”: Remover todos os lançamentos associados das contas com lançamentos contábeis, com status inicial de Desconsiderar movimento (atualizando o campo Status, para Considerar Movimento de todas as contas).


Criar mensagem para o cenário: Para as contas contábeis associadas a linha da tabela dinâmica cujo tipo de relacionamento foi criado com base na parametrização realizada na tela Informações ECF na aba LALUR e LACS  campo  Incluir Lançamento automático com relacionamento selecionado, para tais contas contábeis, não será permitida a inclusão de qualquer tipo de ajuste manual, neste cenário este botão deve estar desabilitado. Para maiores esclarecimentos verificar MTZ_Processamentos (RNC03).
	MFS-14939		Exportar Lançamentos do Período	Botão	-	-	Default: Desabilitado	Permite que o usuário exporte os lançamentos contábeis, associados ao lançamento da Parte A

Tratamento:

Quando acionado, exportar em formato CSV os registros de lançamentos contábeis, do período em questão.

Este botão só deve ficar habilitado se em algum período de apuração, for informado manualmente lançamentos contábeis no período. Neste caso, todos os períodos anteriores ou posteriores deste exercício o botão ficara habilitado.
Exemplo: Janeiro a Outubro, não foi utilizado lançamento: o botão ficara desabilitado. Em novembro foi utilizado lançamentos, a partir deste mês, o botão ficara habilitado de janeiro a novembro.


Identificação do Período:

O período a ser exportado é com base na data inicial da tela de informações ECF, até o ultimo dia da apuração selecionada na tela ‘Lançamentos da Parte A (M300, M350).


Ordenação das Informações no arquivo:

Deve ser ordenado por  CNPJ do estabelecimento/SCP e período.

Para os períodos que possuem lançamentos contábeis, incluir na ordenação os campos:  data, cód. da conta contábil, cód. do centro de custo e numero do lançamento.

Recuperação dos Lançamentos do período

Para os meses (abertura de apuração) com a utilização do saldo:

Recuperar todos os lançamentos contábeis do mês/trimestre das contas (considerando a informação do parâmetro ‘ Recuperação dos Valores’ da tela ‘Recuperação dos Valores - Apuração IR/CSLL’, para a conta ) informadas na grid da aba de Contas Contábeis,. Ex. parâmetro cadastrado com ‘Total de Débito’, recuperar somente os lançamentos a debito.

Para os meses/trimestres (abertura de apuração) com utilização parcial dos saldos (Lançamentos):
Recuperar apenas os lançamentos associados na aba de Contas Contábeis/ Lançamentos Contábeis, para este mês/trimestre.

Se algum mês do período, não for encontrado lançamentos contábeis, exibir a mensagem em tela: TR00702 (Descrição)

Exibição de colunas a serem apresentadas no arquivo:

CNPJ Matriz,CNPJ do Estabelecimento/SCP, Período, Data, Cód. da Conta Contábil, Desc. da Conta Contábil, Cód. do Centro de Custo, Desc. do Centro de Custo, Numero do Lançamento, Valor, Ind. do Valor.

Formatação do campo Período: Jan, Fev, Mar, Abr, Mai, Jun, Jul, Ago, Set, Out, Nov, Dez

Obs. Para os períodos que não foram carregadas informações na tabela de lançamentos contábeis, apresentar para o período, uma linha com todas as colunas em branco (exceto os campos CNPJ Matriz e Período, que devem ser informados sempre).

Nome do arquivo gerado:

‘CNPJ Matriz’_’Período Inicial’_’Período Final’_’Lanc_Contabeis’.CSV, onde :

CNPJ Matriz: CNPJ do estabelecimento Matriz/SCP
Período Inicial é a data inicial da informação ECF;
Período final é a data final do período da apuração, informado na tela. Se a empresa tiver uma situação especial no período a data final será a data que ocorreu a situação especial.
Lanc_Contabeis: texto fixo ‘Lanc_Contabeis’
		Grid de Contas Contábeis	Exibe as contas contábeis relacionadas ao Lançamento da Parte A (M300, M350).

Ordenar os registros pelos campos ”CÓDIGO DA CONTA CONTÁBIL” e “CÓDIGO DO CENTRO DE CUSTOS”
	MFS-14939		Checkbox (*)	Botão	-	-	Default: 
Habilitado	Exibir quando houver contas contábeis na grid.	MFS-14939		Status	Texto/AutoFiltro
	S	-	Default: Considerar Movimento	Exibir o status para as linhas.

Conteúdos Válidos:

Considerar Movimento
Desconsiderar Movimento

	MFS-14939		CONTA CONTÁBIL	Texto
	N	N	Código - Descrição	Exibe o Código e a Descrição da Conta Contábil calculado na rotina de importação dos saldos do processamento em lote

	MFS-14939		NATUREZA DA CONTA CONTÁBIL	Texto
	N	N	Descrição	Exibe a natureza da conta contábil.	MFS-14939		CENTRO DE CUSTO	Texto
	N	N	Código - Descrição	Exibe o Código e a Descrição do Centro de Custos calculado na rotina de importação dos saldos do processamento em lote
	MFS-14939		SALDO	Texto
	N	N	xxx.xxx,xxC
ou
xxx.xxx,xxD 	Exibe o valor calculado + ind. do saldo na rotina de importação dos saldos do processamento em lote

Ind. do Saldo = “C” quando o indicador for Crédito ou “D” quando o indicador for Débito.

	MFS-14939		LANÇAMENTOS/AJUSTES	Texto
	N	N	xxx.xxx,xxC
ou
xxx.xxx,xxD	Exibe o valor total calculado + Ind. dos Lançamentos/Ajustes para os lançamentos/ajustes associados à conta contábil, somado ao valor do período anterior.

Ind. dos Lançamentos/Ajustes = “C” quando o indicador for Crédito ou “D” quando o indicador for Débito.

Tratamentos

Se não existirem lançamentos associados à conta contábil/ajustes informado, deixar este campo com a máscara (0,00 e indicador nulo).

Caso contrário, exibir o valor calculado para o campo “Vlr. a Utilizar” do modal de Associação de Lançamentos Contábeis.
	MFS-14939		Valor à Considerar	Texto    	N	N	xxx.xxx,xxC
ou
xxx.xxx,xxD	Exibe o valor real que será considerado na composição do campo “Valor”  de acordo com a natureza da conta contábil conforme tabela RNG00039 - Conversão de valores para totalização  HYPERLINK  \l "ValorParteA" existente na regra do campo Valor da Parte A .	MFS-14939		JUSTIFICATIVA	Texto   	N	N		Exibe a justificativa referente a utilização do saldo  parcial dos lançamentos e dos ajustes.
	MFS-14939		*Grid de Lançamentos Contábeis	Exibe os Lançamentos Contábeis selecionados através do botão “Filtrar”

Ordenar pelos campos  NÚMERO DO LANÇAMENTO, DATA e INDICADOR.
	MFS-14939		Remover	Botão	-	-		Permite que o usuário remova um lançamento ou mais lançamentos contábeis da grid.

Tratamentos:

- Habilitar este botão somente se for selecionada na grid pelo menos um lançamento contábil. 

- Quando acionado este botão emitir a mensagem DW00140.
Se for escolhida a opção não: Retornar à tela sem alterar informações.
Se for escolhida a opção “Sim”: Remover os lançamentos que foram selecionados.
Ajustar o conteúdo dos campos LANÇAMENTOS e IND. (LANÇAMENTOS) conforme regras do  HYPERLINK  \l "ValoraUtilizar" campo Vlr. a Utilizar
Atualizar o conteúdo do campo Valor (da Parte A) conforme  HYPERLINK  \l "ValorParteA" regras do campo Valor da Parte A  

Aplicar RNG00041 – Remover.
	MFS-14939		Ckeck-box	-	-	-		Permite selecionar um ou mais registros.	MFS-14939		ESTABELECIMENTO	Texto	N	N	Tipo - Código – Descrição	
Exibe o Estabelecimento do Lançamento contábil selecionado.

	MFS-14939		NÚMERO DO LANÇAMENTO	Texto	N	N		Exibe Número do Lançamento Contábil selecionado

	MFS-14939		DATA	Texto	N	N	DD/MM/AAAA	Exibe a Data do Lançamento Contábil selecionado

	MFS-14939		CENTRO DE CUSTO	Texto
	N	N	Código - Descrição	Exibe o Código e a Descrição do Centro de Custo do Lançamento Contábil selecionado

	MFS-14939		VALOR	Texto	N	N	xxx.xxx,xxD
ou 
xxx.xxx,xxC
	Exibe o Valor do Lançamento Contábil e seu indicador. 


Conteúdo Válidos para o indicador:
Débito apresentar D
Crédito apresentar C


	MFS- 14939		ARQUIVAMENTO	Texto
	N	N		Exibe o numero do arquivamento do lançamento.	MFS-14939		HISTÓRICO PADRÃO	Texto
	N	N		Exibe o histórico do lançamento.	MFS-14939		HISTÓRICO COMPLEMENTAR	Texto
	N	N		Exibe o histórico complementar do lançamento.	MFS-14939		Aba: Processos		Pesquisar	Botão	-	-		Permite que o usuário pesquise os processos.

Tratamento:

A pesquisa pode ser feita pelos campos tipo de processo e número de processo	MFS-14939		Adicionar	Botão	-	-		Permite que o usuário adicione o registro na grid.

Tratamentos:
Ao ser inserido, o sistema deve salvar as informações do novo registro (na grid).
Aplicar RNG00011 - Duplicidade de Registro 
	MFS-14939		Remover	Botão	-	-		Permite que o usuário exclua registros da grid.

Tratamento
Aplicar regra de negócio geral  RNG00041 - Remover	MFS-14939		Grid		Tipo de Processo	Texto	N	N		Permite que o usuário visualize o tipo de processo.

Conteúdos Válidos:

- Judicial
- Administrativo
	MFS-14939		Número do Processo	Texto	N	N		Permite que o usuário visualize o número do processo a ser cadastrado.
	MFS-14939		

 (*) Não exibir a descrição na tela.


Modais
Modal: Adicionar Contas da Parte B - Ajustes (M305/M355) ou Alterar Contas da Parte B - Ajustes (M305/M355)

Voltar para o  HYPERLINK  \l "adiiconarParteB" Botão Adicionar

Voltar para o  HYPERLINK  \l "alterarParteB" Botão Alterar		Grupo (Cód/Descr)	LOV	S	S	Código - Descrição	Permite que o usuário selecione/visualize o código e a descrição do grupo do cadastro que a conta da parte B foi cadastrada.


Tratamentos:

Só habilitar este campo se for aberto através do modal Adicionar Contas da Parte B - Ajustes (M305/M355)
	MFS-15810		Conta da Parte B 	LOV	S	S		Permite que o usuário selecione/visualize as contas da parte B cadastradas para inserir os valores correspondentes, 

Tratamentos:

Se for aberto o modal Adicionar Contas da Parte B- Ajustes (M305/M355), permitir a seleção de uma conta da parte B conforme regras abaixo, caso seja aberto o modal Alterar Contas da Parte B - Ajustes (M305/M355), este campo não deve ser editável.


Recuperação dos Registros:


Recuperar as contas da parte B, do grupo, Estabelecimento, Tipo de Tributo cuja data de criação e limite da conta estejam vigentes no período da apuração recuperada, e que possuam saldo no período da escrituração
Só habilitar este campo, se o campo Grupo estiver preenchido.

Apresentar os conteúdos, de Código e Descrição da conta da parte B como filtro. 
	MFS-15810		Descrição	Texto	S	N		Exibe a descrição da conta da parte B selecionada através do LOV “Conta da parte B”

	MFS-15810		Data de Criação da Conta	Texto
	S
	N
	DD/MM/AAAA
Desabilitado
	

Permite que o usuário visualize a data de criação da conta da parte B que foi selecionada.

	MFS-15810		Data Limite	Texto
	N
	N
	DD/MM/AAAA
Desabilitado
	Permite que o usuário visualize a data de limite da conta da parte B que foi selecionada.
	MFS-15810		Saldo Inicial da Escrituração	Texto	S	N	xxx.xxx,xx D ou 
xxx.xxx,xx C	Saldo Inicial da Escrituração

Permite que o usuário visualize o saldo inicial da escrituração da conta selecionada. Valor e indicador.


	MFS-15810		Valor 	Texto	S	S	xxx.xxx,xx	Permite que o usuário informe/altere o valor do ajuste na parte B


Tratamentos:

Ao selecionar a Conta da Parte B, o sistema deve preencher o campo Valor e Ind. do Valor com os dados correspondentes ao Saldo Final e Ind. do Saldo Final da Conta da Parte B para o Período de Apuração do Lançamento da Parte A, porém, permitir a alteração do mesmo. 	MFS-15810		Ind. do Valor	Lista	S	S		Permite que o usuário informe/altere o indicador do Lançamento Contábil selecionada através do LOV “Conta da parte B”

Tratamentos: 

Conteúdos Válidos:
Débito
Crédito


Ao selecionar a Conta da Parte B, o sistema deve preencher o campo Valor e Ind. do Valor com os dados correspondentes ao Saldo Final e Ind. do Saldo Final da Conta da Parte B para o Período de Apuração do Lançamento da Parte A, porém, permitir a alteração do mesmo. 	MFS-15810		Histórico	Texto	N	S		
Permite que o usuário informe/altere o histórico do Ajuste da Parte B 	MFS-15810		OK	Botão	-	-		Permite que o usuário salve as informações cadastradas para o Ajuste da Parte B.

Tratamentos:


Se o Ind. do Valor não for compatível com o tipo de lançamento conforme tabela abaixo emitir a seguinte mensagem DW00168

Tipo de Lançamento
Indicador do lançamento de ajuste da parte B

Adição ou Lucro
D – Devedor

Exclusão ou Compensação de Prejuízo
C – Credor


Se for escolhida a opção “Sim”
O Sistema deve manter o Valor e Ind. do Valor preenchidos pelo usuário.

Se for escolhida a opção “Não” 
O Sistema volta para o modal e aguarda uma ação do usuário.


Ao ser inserido/alterado um ajuste, somar todos os ajustes da parte B (Considerando que os valores a Crédito devem subtrair os valores a Débito e o sinal de acordo com a RNG00047 - Recalculo do Valor) e preencher o campo ‘Valor’ das ‘Informações do Lançamento da Parte A’, considerando o sinal de acordo com o Indicador do somatório de todos os ajustes da parte B e o Tipo de Lançamento 

Após a inclusão/alteração do ajuste, deve ser efetuada a atualização dos valores seguindo as regras da RNG00044 - Cálculo do Registro M500 
	MFS-15810		Cancelar	Botão	-	-		Permite que o usuário cancele as informações que ainda não foram salvas do lançamento da parte B

Tratamento:
Aplicar RNG00020 – Botão Cancelar.	MFS-15810		


Modal Adicionar Lançamentos Contábeis		Associar Lançamentos Contábeis

Voltar ao  HYPERLINK  \l "BotãoAdicionarLancamento" botão Adicionar Lançamentos Contábeis		Estabelecimento	Lista
	S	S	Tipo - Código – Descrição	Permite que o usuário selecione o estabelecimento que possui o lançamento contábil.

Tratamento:

Buscar na tabela de Estabelecimento o Código da Empresa correspondente ao CNPJ da Empresa informado no Lançamento da Parte A (M300, M350). 

Caso a escrituração corresponda ao estabelecimento matriz (centralizador), então:
Selecionar o CNPJ de todos os Estabelecimentos cadastrados para o centralizador.
Caso a escrituração corresponda a uma SCP (estabelecimento descentralizado), então:
Considerar na busca apenas os lançamentos pertencentes ao estabelecimento descentralizador, desconsiderando todos os demais lançamentos de outros estabelecimentos existentes para a empresa encontrada.
	MFS-14939		Data Inicial	Texto	S	S	DD/MM/AAAA	Permite que o usuário preencha um período para o qual deseja filtrar os lançamentos contábeis que deseja associar à conta contábil.

Tratamentos:

Validação de obrigatoriedade:

Ao acionar o botão ”Filtrar”, os campos Data Inicial e Data Final devem ser obrigatórios. 
Aplicar regra  RNG00010 - Campo Obrigatório 

No momento da abertura do modal Adicionar Lançamentos Contábeis preencher os campos conforme abaixo:

Data Inicial = Data Inicial da Abertura da Apuração vinculada ao Lançamento Parte A.

Se “Data inicial” e/ou “Data Final” preenchida for anterior à “Data Inicial” da tela de “Informações ECF” e/ou
“Data inicial” e/ou “Data Final” preenchida for posterior à “Data Final” da “Abertura da Apuração”. Apresentar a mensagem DW00141 e apagar o conteúdo do campo “Data Inicial” e/ou “Data Final”.
	MFS-14939		Data Final	Texto	S	S	DD/MM/AAAA	Permite que o usuário preencha um período para o qual deseja filtrar os lançamentos contábeis que deseja associar à conta contábil.

Tratamentos:

Validação de obrigatoriedade:

Ao acionar o botão ”Filtrar”, os campos Data Inicial e Data Final devem ser obrigatórios. 
Aplicar regra RNG00010 - Campo Obrigatório 
No momento da abertura do modal Adicionar Lançamentos Contábeis preencher os campos conforme abaixo:

Data Final = Data Final da Abertura da Apuração vinculada ao Lançamento Parte A.


Se “Data Inicial:” e “Data Final:” forem diferentes de nulo e o valor informado no campo “Data Final:” é menor que o valor informado no campo “Data Inicial:” apresentar a mensagem DW00010 e apagar o conteúdo do campo “Data Final”

Se “Data inicial” e/ou “Data Final” preenchida for anterior à “Data Inicial” da tela de “Informações ECF” e/ou
“Data inicial” e/ou “Data Final” preenchida for posterior à “Data Final” da “Abertura da Apuração”. Apresentar a mensagem DW00141 e apagar o conteúdo do campo “Data Inicial” e/ou “Data Final”.

	MFS-14939		Intervalo de Lançamentos		Opção de Pesquisa	Lista	S	S	Valor default: “entre”	Permite que o usuário selecione a opção de pesquisa para a qual deseja filtrar os lançamentos contábeis que deseja associar à conta contábil.

Valores válidos:
entre
igual a
	MFS-14939		Nº do Lançamento	Texto	N	S		Permite que o usuário informe o número do lançamento contábil que deseja associar à conta contábil.

Tratamentos:

O campo só deve ser exibido se o campo Opção de Pesquisa for igual a “igual a”.
	MFS-14939		
De:	
Texto	
N	
S		Permite que o usuário informe o intervalo de lançamentos contábeis que deseja associar à conta contábil.

Tratamentos:

- O campo só deve ser exibido se o campo Opção de Pesquisa for igual a “entre”.

- Se o valor informado no campo “Até” for menor que o valor informado no campo “De:” apresentar a mensagem DW00144 e apagar o conteúdo do campo “Até”
	MFS-14939		Até:	Texto	N	S		MFS-14939		Arquivamento	Texto	N	S		Exibe no grid os lançamentos recuperados com base parâmetros informados a realização da seleção.

	MFS-14939		Ind. de Lançamento	Lista	N	S		Permite que o usuário informe o indicador do lançamento contábil que deseja associar à conta contábil.

Valores válidos:
Crédito
Débito

Tratamentos:

Verificar o parâmetro Recuperação dos Valores da Conta Contábil do Plano Empresa selecionada.

Se parâmetro = Total de Crédito:

Preencher o campo Ind. de Lançamento = Crédito.
Desabilitar o campo Ind. de Lançamento para edição.

Se parâmetro = Total de Débito: 

Preencher o campo Ind. de Lançamento = Débito.
Desabilitar o campo Ind. de Lançamento para edição.

Senão:

Disponibiliza as duas opções para o usuário efetuar  a escolha.
 	MFS-14939		Filtrar	Botão	-	-		Exibe no grid os lançamentos recuperados com base nos parâmetros informados na realização da seleção.

Tratamentos: 

Se Opção de Pesquisa for igual a “entre”:

- Se o usuário preencher os campos “De”, “Até”, Data Inicial e Data Final corretamente, exibir a mensagem DW00145.

Se for escolhida a opção “Não”:
Fechar a mensagem e retornar à tela de seleção de lançamentos contábeis

Se for escolhida a opção “Sim”:

Buscar na tabela de Lançamentos Contábeis todos os registros correspondentes ao *Estabelecimento, Conta Contábil, Centro de Custos, cuja Data do Lançamento esteja entre a Data Inicial e a Data Final  informadas na tela de Lançamentos contábeis, Arquivamento (quando preenchido), Ind. de Lançamento (quando preenchido), Histórico (quando preenchido) e o Número do Lançamento seja igual ou esteja compreendido entre os valores “De:” e “Até” informados pelo usuário. Apresentar na grid todos os registros selecionados.

Se não forem encontrados registros, exibir a mensagem DW00146.

Se Opção de Pesquisa for igual a “igual a”:

- Se o usuário preencher os campos Nº do Lançamento, Data Inicial e Data Final corretamente:

Buscar na tabela de Lançamentos Contábeis todos os registros correspondentes ao *Estabelecimento, Conta Contábil, Centro de Custos, cuja Data do Lançamento esteja entre a Data Inicial e a Data Final  informadas na tela de Lançamentos contábeis, Arquivamento (quando preenchido) , Ind. de Lançamento (quando preenchido), Histórico (quando preenchido)  e o Número do Lançamento seja igual ao Nº do Lançamento informados pelo usuário. Apresentar na grid todos os registros selecionados.

Se não forem encontrados registros, exibir a seguinte mensagem DW00146.

	MFS-14939		Limpar	-	-	-	-	Apagar os parâmetros informados para a recuperação dos dados.	MFS-14939		Cancelar	-	-	-	-	
Permite que o usuário cancele as ações efetuadas no modal.

Tratamentos:

Aplicar RNG00020 – Botão Cancelar.	MFS-14939		*Grid de Lançamentos Contábeis	Exibe os Lançamentos Contábeis selecionados através do botão “Filtrar”

Ordenar pelos campos  NÚMERO DO LANÇAMENTO, DATA e INDICADOR.
	MFS-14939		Remover	Botão	-	-		Permite que o usuário remova um lançamento ou mais lançamentos contábeis da grid.

Tratamentos:

Aplicar RNG00041 – Remover.
	MFS-14939		Ckeck-box	-	-	-		Permite selecionar um ou mais registros.	MFS-14939		ESTABELECIMENTO	Texto	N	N	Tipo - Código – Descrição	
Exibe o Estabelecimento do Lançamento contábil selecionado.
	MFS-14939		NÚMERO DO LANÇAMENTO	Texto	N	N		Exibe Número do Lançamento Contábil selecionado
	MFS-14939		DATA	Texto	N	N	DD/MM/AAAA	Exibe a Data do Lançamento Contábil selecionado
	MFS-14939		CENTRO DE CUSTO	Texto
	N	N	Código - Descrição	Exibe o Código e a Descrição do Centro de Custo do Lançamento Contábil selecionado
	MFS-14939		VALOR	Texto	N	N	xxx.xxx,xxC ou
xxx.xxx,xxD	Exibe o Valor do Lançamento Contábil 
e seu indicador. 


Conteúdo Válidos para o indicador:
Débito apresentar D
Crédito apresentar C
	MFS-14939		ARQUIVAMENTO	Texto
	N	N		Exibe o numero do arquivamento do lançamento.	MFS-14939		HISTÓRICO PADRÃO	Texto
	N	N		Exibe o histórico padrão do lançamento.	MFS-14939		HISTÓRICO COMPLEMENTAR	Texto
	N	N		Exibe o histórico complementar do lançamento.	MFS-14939		Selecionar	Botão	-	-		Os lançamentos contábeis selecionados serão considerados para composição do campo Vlr. Total.	MFS-14939		Cancelar	Botão	-	-		Permite que o usuário cancele as ações efetuadas na aba ‘Contas Contábeis’.

Tratamentos:
Aplicar RNG00020 – Botão Cancelar.	MFS-14939		

Modal Alterar Valores


Voltar ao  HYPERLINK  \l "BotãolAlterarValores" botão Alterar Valores		Vlr. Períodos Anteriores	Texto	S	N	Default: Desabilitado
0,00	Exibe o total calculado dos lançamentos/ajustes do período anterior.

Tratamentos:

Só apresentar valor neste campo, a partir do segundo período (mês/trimestre), referente a apuração processada na base. No primeiro mês/trimestre, este campo deve ficar sem informação (apenas com a máscara: 0,00).

Realizar o cálculo abaixo para contas contábeis que possuem o status “Considerar Movimento”:

Total de Créditos: Somar o valor calculado para esta conta de todos campos ‘Lançamentos/Ajustes’ com o indicador igual a Crédito

Total de Débitos: Somar o valor calculado para esta conta de todos campos ‘Lançamentos/Ajustes’ com o indicador igual a Débito

Se status =  “Desconsiderar Movimento”, compor o campo conforme abaixo:

Valor do Saldo da Conta Contábil (do Período Anterior) e Indicador + Vlr. dos Ajustes e Ind. do Vlr. dos Ajustes  (se houver).

Apresentar neste campo o valor absoluto do resultado abaixo:

Total = Total de Créditos – Total de Débitos
	MFS-14939		Ind. do Vlr. Períodos Anteriores	Texto	N	N	Default: Desabilitado	Exibe o indicador do total calculado para os valores dos lançamentos/ajustes do período anterior.

Se o total de Créditos calculado  HYPERLINK  \l "VlrPeríodosAnteriores" no campo Vlr. Períodos Anteriores for maior que o Total de Débitos: Apresentar “C- Crédito”

Caso contrário: Apresentar “D - Débito”

Se não existir valor no campo Vlr. Períodos Anteriores, o indicador deve ser nulo.
	MFS-14939		Vlr. Total	Texto	S	N	xxx.xxx,xx	Exibe o total calculado para todos os lançamentos disponíveis na grid.

Tratamentos:

Realizar o cálculo abaixo:

Total de Créditos: Somar o valor de todos os lançamentos com o indicador igual a Crédito

Total de Débitos: Somar o valor de todos os lançamentos com o indicador igual a Débito

Apresentar neste campo o valor absoluto do resultado abaixo:

Total = Total de Créditos – Total de Débitos

Este campo deve sempre ficar desabilitado. Só deve ser preenchido se algum lançamento for adicionado na grid  Lançamentos Contábeis’ da modal Adicionar Lançamentos Contábeis, caso contrário, deve ficar desabilitado e apenas com a informação da máscara (0,00).
		Ind. do Vlr. Total 	Texto	S	N		Exibe o indicador do total calculado para os lançamentos selecionados.

Tratamentos:

Se o total de Créditos calculado  HYPERLINK  \l "VlrTotal" no campo Vlr. Total for maior que o Total de Débitos, apresentar “C - Crédito”. Caso contrário, apresentar “D- Débito”

Este campo só deve ser habilitado se o campo Vlr. Total for preenchido pelo usuário, caso contrário deve ficar desabilitado e nulo.

	MFS-14939		Vlr. Parcial	Texto	N	S	xxx.xxx,xx
	Permite ao usuário informar o valor parcial dos lançamentos que será utilizado para o lançamento.

Tratamentos:

Este campo só deve ser habilitado se o campo Vlr. Total estiver preenchido , caso contrário, deve ficar desabilitado.	MFS-14939		Ind. do Vlr. Parcial	Lista	N	S	Default: Desabilitado	Permite ao usuário informar o indicador valor do lançamento parcial que será utilizado.

Tratamentos:

Este campo só deve ser habilitado e de preenchimento obrigatório, aplicar RNG00010- Campo Obrigatório, se o campo Vlr. Parcial, for preenchido pelo usuário, caso contrário deve ficar desabilitado.

Conteudo Válidos:
Nulo
C - Crédito
D - Débito

Se a opção nula for selecionada, apagar o valor do campo Vlr. Parcial.

	MFS-14939		Vlr. dos Ajustes	Texto	N	S	xxx.xxx,xx
	Permite ao usuário informar o valor dos ajustes será adicionado aos valores dos lançamentos .	MFS-14939		Ind. do Vlr. dos Ajustes	Lista	N	S	Default: Desabilitado	Permite ao usuário informar o indicador valor do ajuste será adicionado aos valores dos lançamentos.

Tratamentos:

Este campo só deve ser habilitado e de preenchimento obrigatório, aplicar RNG00010- Campo Obrigatório, se o campo Vlr. dos Ajustes , for preenchido pelo usuário, caso contrário deve ficar desabilitado.
Conteudo Válidos:
Nulo
C - Crédito
D - Débito

Se a opção nula for selecionada, apagar o valor do campo Vlr. dos Ajustes.
	MFS-14939		Total de Débito	Texto	-	-	Default: Desabilitado	O valor exibido corresponde ao movimento devedor total da conta contábil no período.  	MFS-14939		Total de Crédito	Texto	-	-	Default: Desabilitado	O valor exibido corresponde ao movimento credor total da conta contábil no período.  	MFS-14939		Vlr. a Utilizar	Texto	S	N	xxx.xxx,xx
Default Desabilitado
	Permite ao usuário visualizar o valor que será utilizado para o lançamento/ajuste.

Tratamentos:

Este campo deve ficar sempre desabilitado e deve ser preenchido automaticamente pelo sistema, considerando os campos Vlr. Períodos Anteriores, Vlr.Parcial, Vlr. dos Ajustes e Vlr Total (com os respectivos indicadores) e as regras abaixo:

Regras para o status igual “Considerar Movimento”:

Se o campo ‘Vlr. Parcial’, estiver preenchido:
Considerar o somatório dos campos: ‘Vlr. Períodos Anteriores’, ‘Vlr. Parcial’ e ‘Vlr. dos Ajustes’ (com os respectivos  indicadores). O indicador deve ser informado conforme  HYPERLINK  \l "IndVlraUtilizar" Ind. do Vlr. a Utilizar
Se o campo ‘Vlr. Total’ estiver preenchido e o Vlr. Parcial sem preenchimento:
Considerar o somatório dos campos ‘Vlr. Períodos Anteriores’, ‘Vlr. Total’ e ‘Vlr. dos Ajustes’ (com os respectivos  indicadores). O indicador, deve ser informado conforme  HYPERLINK  \l "IndVlraUtilizar" Ind. do Vlr. a Utilizar
 Se os campos ‘Vlr. dos Ajustes’ e ‘Vlr. Períodos Anteriores’ estiverem preenchidos e o campo ‘Vlr. Total’ sem preenchimento:
Considerar a movimentação da conta (importação dos saldos da conta), mais os valores dos campos ‘Vlr. Períodos Anteriores’ e ‘Vlr. dos Ajustes’ (com os respectivos  indicadores). O indicador, deve ser informado conforme  HYPERLINK  \l "IndVlraUtilizar" Ind. do Vlr. a Utilizar
Se o Vlr. dos Ajustes estiver Sem preenchimento e o campo ‘Vlr. Total’ sem preenchimento e  existir no período anterior o Vlr. a Utilizar (preenchido), considerar a movimentação da conta (importação dos saldos da conta), mais os valores dos campos ‘Vlr. Períodos Anteriores’, se não, o campo deve ficar sem preenchimento.
Se o campo ‘Vlr. dos Ajustes’ estiver preenchido, o campo ‘Vlr. Períodos Anteriores’ sem preenchimento e o campo ‘Vlr. Total’ sem preenchimento: Considerar o valor calculado para a conta no período, mais o valor do campo ‘Vlr. dos Ajustes’ (com os respectivos  indicadores). O indicador, deve ser informado conforme  HYPERLINK  \l "IndVlraUtilizar" Ind. do Vlr. a Utilizar
Atenção: Considerar a movimentação para as informações de ‘Saldo’ e ‘Movimento’ no parâmetro ‘Recuperação dos Valores’. Se o parâmetro estiver com as informações ‘Total de Débito’ ou ‘Total de Crédito’, considerar a movimentação a débito ou a crédito (respectivamente).

Regras para o status igual “Desconsiderar Movimento”:

O campo  Vlr. A Utilizar e Ind. do Vlr. A Utilizar, deverá ser preenchido com o somatório abaixo:

Vlr. Períodos Anteriores e Ind. do Vlr. Períodos Anteriores + Vlr. dos Ajustes e Ind. do Vlr. dos Ajustes  (se houver).
O conteúdo do campo Vlr. a Utilizar será exibido na coluna Lançamentos/Ajustes e este valor será utilizado na composição do campo Valor (Parte A)*.
	MFS-14939		Ind. do Vlr. a Utilizar	Lista	S	N	Default: Desabilitado	Permite ao usuário visualizar o indicador do valor a utilizar.

Tratamentos:

Este campo deve ficar sempre desabilitado e deve ser preenchido automaticamente pelo sistema., considerando o indicador do valor calculado  HYPERLINK  \l "VlraUtilizar" no campo Vlr. a Utilizar.

Conteudo Válidos:
C-Crédito
D-Débito
	MFS-14939		Justificativa	Texto	N	S	Default: Desabilitado	Justificativa

Permite ao usuário informar a justificativa para a utilização do valor parcial dos lançamentos e dos ajustes.

Tratamentos:

Este campo só deve ser habilitado e de preenchimento obrigatório (aplicar RNG00010- Campo Obrigatório) se o campo Vlr. Parcial for preenchido e seu indicador for diferente de nulo ou Vlr. dos Ajustes estiver preenchido e seu  indicador diferente de nulo,  caso contrário deve ficar desabilitado.

Se os indicadores dos campos Vlr. Parcial e Vlr. dos  Ajustes, forem alterados para nulo, limpar o campo justificativa.

	MFS-14939
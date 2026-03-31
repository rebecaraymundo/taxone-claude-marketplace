# MTZ_Tela_Manutenção_Bloco 0_Identificacao_dos_Periodos_Dispensados_0120

> Fonte: MTZ_Tela_Manutenção_Bloco 0_Identificacao_dos_Periodos_Dispensados_0120.doc

SPED - EFD-Contribuições – Manutenção – Registro 0120 (Tela)


Localização
Módulo: SPED ( EFD – Escrituração Fiscal Digital das Contribuições
Menu: Manutenção ( Registro do Bloco 0 ( Identificação dos períodos dispensados (0120)


Documentos Matrizes Relacionados:
RNG-0_V14.docx
DEPARA EFD CONTRIBUICOES_BLOCOP_LUCRO_REAL_LUCRO_PRESUMIDO.xlsx


DOCUMENTO DE REQUISITO

DR	Nome	Descrição		OS-3845	Criação do documento
	Criação da Tela e do registro 0120 no Mastersaf DW.
		
REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN00	
Regra Geral

As informações cadastradas nesta tela farão parte do registro 0120 (Identificação dos períodos dispensados) do EFD-Contribuições. Vide documentos matrizes relacionados deste documento.

	OS-3845		RN01	
Ano Calendário

Valor default: Nulo
Obrigatoriedade: Sim
Tipo: Data (Formato AAAA)

Neste campo o usuário deverá informar o ano calendário que será considerado para a parametrização e geração dos períodos dispensados. 

Este campo é chave única do registro, ou seja, não podem haver mais do que um registro cadastrado para o mesmo ano calendário.

Se não for informado, o sistema deve emitir seguinte mensagem de crítica na tela:
“O campo Ano Calendário é de preenchimento obrigatório e não foi informado.”

Somente permitir a gravação do registro se o ano informado for maior ou igual á 2012. Se for informado um ano anterior á 2012, então emitir seguinte mensagem de crítica:
“Ano Calendário inválido. Somente é permitida a geração deste registro a partir de 2012.”

	OS-3845		RN02	
Meses de dispensa

Valor default: Nulo
Obrigatoriedade: Pelo menos um dos meses deve ser marcado.
Tipo: Checkbox

Nesta funcionalidade o usuário deve marcar os meses em que não tenha realizado operações representativas de receitas auferidas ou recebidas, e operações com direito a crédito, ou seja, os meses dispensados da transição do EFD-Contribuições).

Se nenhum mês for marcado, então emitir seguinte mensagem de crítica na tela:
“É obrigatório o preenchimento de ao menos um mês de dispensa.”

	OS-3845		RN03	
Informação Complementar

Valor default: Nulo
Obrigatoriedade: Não
Tipo: Texto
Tamanho: 90 caracteres

Neste campo, o usuário poderá informar a descrição complementar do mês de dispensa, caso seja necessário. 
Obs.: Esta informação é limitada á 90 caracteres conforme a limitação do layout do EFD-Contribuições.

	OS-3845		RN04	
Mês de Apresentação

Valor default: Nulo
Obrigatoriedade: Sim
Tipo: Lista
Valor: Apresentar uma lista com os meses de Janeiro á Dezembro.

Neste campo o usuário deverá informar em qual mês o registro 0120 deve ser informado no arquivo EFD-Contribuições.

Se não for informado, apresentar seguinte mensagem de crítica na tela:
“O campo Mês de Apresentação é obrigatório e não foi informado.”

Se for selecionado um mês no qual não foi marcado no campo “Mês de dispensa” (RN02), apresentar seguinte mensagem de crítica na tela:
“O Mês de apresentação escolhido precisa ser selecionado em “Mês de dispensa””.
	OS-3845		


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN
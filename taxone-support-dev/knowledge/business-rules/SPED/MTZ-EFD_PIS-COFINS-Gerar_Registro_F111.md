# MTZ-EFD_PIS-COFINS-Gerar_Registro_F111

> Fonte: MTZ-EFD_PIS-COFINS-Gerar_Registro_F111.doc

TITLE   \* MERGEFORMAT EFD PIS/COFINS - Gerar Registro F111


DOCUMENTO DE REQUISITO

DR	Nome	Descrição		OS3169-GE15	 TITLE   \* MERGEFORMAT EFD PIS/COFINS - Gerar Registro F111	Trata-se da demanda para a geração do registro F111 – Processo Referenciado. Esse registro é específico para informar os processos administrativos ou judiciais. 

O cliente Camargo Corrêa possui medidas cautelares sobre os valores apurados pela contabilidade. Dessa forma o cliente entende que essas informações devem ser no registro F111. Além disso, o cliente informou que o volume não é muito grande.		
REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN00	Deverá ser incluído o registro F111 – Processo Referenciado na tela de manutenção do perfil.

Reg             Nível                              Descrição                                                                               Obrig (Entr/Saída)
F111            4                                    Processo Referenciado                                                           OE/OE

O relatório de conferência dessa tela deverá ser alterado para contemplar esse novo registro.	OS3169-GE15		RN01	Na tela de manutenção do registro F100 (menu: Manutenção >> Registro do Bloco F >> Demais Documentos e Operações Geradoras de Contribuição e Créditos (F100)) do módulo EFD – Escrituração Fiscal Digital – PIS/PASEP-COFINS deverá ser criado um novo botão chamado “Registro F111 – Processo Referenciado”.	OS3169-GE15		RN02	Esse novo botão deverá ser disponibilizado entre os botões “Confirma” e “Relatório”. O usuário só poderá visualizar essa tela caso um registro F100 seja aberto previamente.	OS3169-GE15		RN03	O cliente poderá incluir na tela “Processo Referenciado (F111)” quantos registros forem necessários para cada registro F100 previamente selecionado. O relacionamento de 1:N entre os registros F100 e F111 é permitido pelo Guia Prático do EFD PIS/COFINS.	OS3169-GE15		RN04	O relatório de conferência da tela de manutenção do registro F100 deverá ser alterado para que as informações do registro F111 sejam exibidas.	OS3169-GE15		RN05	Serão exibidos na tela os seguintes campos:

Número do Processo: deverá ser selecionado o Número do Processo que foi cadastrado na tela de Cadastro de Processo Referenciado. 
Indicador da Origem do Processo: deverá ser uma lista de escolha fechada, onde o usuario deverá escolher uma dentre 3 opções. Campo obrigatório de preenchimento. As opções listadas são:
1 – Justiça Federal
3 – Secretaria da Receita Federal do Brasil
9 – Outros	OS3169-GE15		RN06	Caso o cliente tente cadastrar um Processo Referenciado (F111) com mesmo Número de Processo e mesmo Indicador de Origem de Processo, deverá ser exibida a seguinte mensagem de erro:

“Não será possível a inclusão de um mesmo Número de Processo com mesma Origem de Processo”.

Após exibir a mensagem de erro, o sistema não deve permitir a gravação do registro. Essa crítica é necessária porque para a geração do registro F111, os campos 002 – NUM_PROC e 003 – IND_PROC são campos obrigatórios.	OS3169-GE15		

Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN
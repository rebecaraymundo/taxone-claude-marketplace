# MTZ_Tela_Parametros_Tipo_de_Credito_Natureza_de_Credito

> Fonte: MTZ_Tela_Parametros_Tipo_de_Credito_Natureza_de_Credito.doc

THOMSON REUTERS

Tela Tipo de Crédito x Natureza de Crédito
Localização: 
MastersafDW >> SPED >>  EFD-Escrituração Fiscal Digital das Contribuições >> Parâmetros
SPED
TAXONE >> SPED >>  EFD-Escrituração Fiscal Digital das Contribuições >> Parâmetros
SPED


	
Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc92465735" 1.	CONTROLE DE ALTERAÇÕES	 PAGEREF _Toc92465735 \h 3
 HYPERLINK \l "_Toc92465736" 2.	INTRODUÇÃO	 PAGEREF _Toc92465736 \h 4
 HYPERLINK \l "_Toc92465737" 3.	DOCUMENTOS DE REFERÊNCIA	 PAGEREF _Toc92465737 \h 4
 HYPERLINK \l "_Toc92465738" 4.	DEFINIÇÃO DAS REGRAS	 PAGEREF _Toc92465738 \h 4
 HYPERLINK \l "_Toc92465739" 4.1.	Botões da Toolbar	 PAGEREF _Toc92465739 \h 4
 HYPERLINK \l "_Toc92465740" 4.2.	Layout e Campos – Tela	 PAGEREF _Toc92465740 \h 4


CONTROLE DE ALTERAÇÕES


Data	Demanda	Descrição	Autor		06/01/2022	MFS-42923	Criação da tela Tipo de Crédito x Natureza de Crédito	Alessandra Cristina Navatta		


	 

INTRODUÇÃO 
Criar uma tela para o usuário efetuar a parametrização de tipo de crédito com natureza de crédito para que possa ser usado no processo de rateio das receitas cumulativas e não cumulativas.

DOCUMENTOS DE REFERÊNCIA
Não se aplica.
DEFINIÇÃO DAS REGRAS
	
Botões da Toolbar 

Confirma, Relatório e Fecha.

Layout e Campos – Tela 


Localização da tela: 
Módulo: SPED ( EFD-Escrituração Fiscal Digital das Contribuições
Menu:    Parâmetros

Título da tela: Tipo de Crédito x Natureza de Crédito


Campos de preenchimento obrigatório: Estabelecimento, Tipo de Crédito e Natureza de Crédito. Caso um desses campos não esteja preenchidos, verificar a mensagem a ser exibida, nas regras abaixo.


Campo	Regra	Demanda		Estabelecimento	Exibir o estabelecimento centralizador ou descentralizado da empresa/estabelecimento logado no sistema.	MFS-42923		Tipo de Crédito	Exibir as informações da TFIX93 - Tabela Código de Tipo de Crédito da obrigação acessória SPED Contribuições

Ao confirmar, se nenhum tipo de crédito estiver preenchido, exibir a mensagem: Informar Tipo de Crédito!	MFS-42923		Natureza de Crédito	Apresentar as opções abaixo (check-box):

1 -Aquisição de bens para revenda
2-Aquisição de bens utilizados como insumo
3-Aquisição de serviços utilizados como insumo
4-Energia elétrica e térmica, inclusive sob a forma de vapor
5-Aluguéis de prédios
6-Aluguéis de máquinas e equipamentos
7-Armazenagem de mercadoria e frete na operação de venda
8-Contraprestações de arrendamento mercantil
9-Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado (crédito sobre encargos de depreciação).
10-Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado (crédito com base no valor de aquisição).
11-Amortização e Depreciação de edificações e benfeitorias em imóveis
12-Devolução de Vendas Sujeitas à Incidência Não-Cumulativa
13-Outras Operações com Direito a Crédito
14-Atividade de Transporte de Cargas – Subcontratação
15-Atividade Imobiliária – Custo Incorrido de Unidade Imobiliária
16-Atividade Imobiliária – Custo Orçado de unidade não concluída
17-Atividade de Prestação de Serviços de Limpeza, Conservação e Manutenção – vale-transporte, vale-refeição ou vale-alimentação, fardamento ou uniforme.
18-Estoque de abertura de bens

Ao confirmar, se nenhuma natureza de crédito estiver preenchida, exibir a mensagem: Informar Natureza de Crédito!	MFS-42923		Grid Estabelecimentos	Exibir todos os estabelecimentos centralizadores e descentralizados, que o usuário tem acesso.


	MFS-42923		
Selecionar	Permite que o usuário selecione os Estabelecimentos que serão considerados para replicar a parametrização.

Tratamentos:

Modal 'Selecionar Estabelecimentos‘
Ao ser acionado abrir o Modal 'Selecionar Estabelecimentos‘. Apresentando os campos Cód. Estab e DescriçãoBotões do Modal 'Selecionar Estabelecimentos': Critério, Cancelar, OK e Salvar...


Botões Critério, Cancelar, OK e Salvar- Ao selecionar o botão 'Cancelar', nada será feito e o Modal 'Selecionar Estabelecimentos‘ será fechado. - Ao selecionar o botão 'Critério', os estabelecimentos poderão ser filtrados e no novo modal serão exibidos habilitado os botões Pesquisar e Cancelar. 
-Ao confirmar a seleção dos registros, acionando o botão ‘OK’, apresentar os estabelecimentos no componente “Estabelecimentos” da tela Principal
- Permite a seleção de vários registros por vez.
- Ao entrar no modal, pelo menos um registro deve ser selecionado, se for selecionado o botão 'Ok', caso contrário, exibir a mensagem “Selecionar pelo menos um registro”.
-Ao selecionar o botão ’Salvar’, o sistema salva as informações recuperadas dos estabelecimentos (no diretório local e formato que o usuário informar).
	MFS-42923		Marcar Todos	Permite ao usuário selecionar ou desmarcar todos os registros da grid Estabelecimentos.
	MFS-42923
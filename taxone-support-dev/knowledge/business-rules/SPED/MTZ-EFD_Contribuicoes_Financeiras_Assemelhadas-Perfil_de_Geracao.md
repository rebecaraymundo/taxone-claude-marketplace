# MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Perfil_de_Geracao

> Fonte: MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Perfil_de_Geracao.doc

TITLE   \* MERGEFORMAT EFD - Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas - Perfil de Geração 


DOCUMENTO DE REQUISITO 

DR	Nome	Descrição		OS3810-A1	EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas – Perfil de Geração	Essa OS tem por objetivo a geração dos dados do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas. Trata-se da escrituração digital dos tributos PIS e COFINS para as instituições financeiras, seguradoras, entidades de previdência privada, operadoras de planos de assistência à saúde e assemelhadas, conforme Ato Declaratório Executivo nº. 65 de 20/12/12.		MFS33127	Andréa Rocha	Inclusão do novo layout.		


Cód.	


Descrição	


DR		RN01	Deverá ser criada uma tela chamada “Perfil de Geração – EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas”. Essa tela é semelhante a tela do Perfil do módulo EFD – Escrituração Fiscal Digital das Contribuições.

Essa tela será responsável pela parametrização dos perfis de geração do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas.	OS3810-A1		RN02	Serão disponibilizados na tela os seguintes campos:

Leiaute: nesse campo, o usuário deverá selecionar o Leiaute para a geração da EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas. A informação exibida nesse campo será da tabela CAD_LAYOUT (TFIX67.TXT). Campo obrigatório de preenchimento. Conteúdo do campo:
- Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas -  Versão 2.0.1A;
- Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas -  Versão 3.1.0A;
[MFS33127] Inclusão do leiaute 2020
- Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas -  Versão 3.2.0A;

Perfil: nesse campo, o usuário irá informar o Código e a Descrição do Perfil que está sendo parametrizado.
Código do Perfil: nesse campo, o usuário irá informar o Código do Perfil. O campo deverá ser alfanumérico de 3 posições. Campo obrigatório de preenchimento.
Descrição do Perfil: nesse campo, o usuário irá informar a Descrição do Perfil. O campo deverá ser alfanumérico de 50 posições. Campo obrigatório de preenchimento.
Definição dos Blocos: nessa parte o usuário poderá selecionar o bloco para parametrização. Os blocos exibidos são os seguintes:
0 – Abertura, Identificação e Referência
A – Documentos Fiscais – Serviços (ISS)
C – Documentos Fiscais I – Mercadorias (ICMS/IPI)
D – Documentos Fiscais II – Mercadorias (ICMS)
F – Demais Documentos e Operações
I – Operações das Instituições Financeiras
M – Apuração da Contribuição e Credito de PIS/PASEP e da COFINS
9 – Controle e Encerramento do Arquivo Digital
Definição dos Registros: nessa parte, o usuário poderá selecionar os registros para parametrização. Os registros serão exibidos conforme a seleção do bloco. Os registros exibidos são os seguintes:
0 – Abertura, Identificação e Referência
0000 – Abertura do Arquivo Digital e Identificação da Pessoa Jurídica
0001 – Abertura do Bloco 0
0100 – Dados do Contabilista
0110 – Regimes de Apuração da Contribuição Social e de Apropriação do Crédito
0140 – Tabela de Cadastro do Estabelecimento
0500 – Plano de Contas Contábeis
0990 – Encerramento do Bloco 0

(CONTINUA)	OS3810-A1
OS3810-B
MFS33127		(CONTINUA)

A – Documentos Fiscais – Serviços (ISS)
A001 – Abertura do Bloco A
A990 – Encerramento do Bloco A
C – Documentos Fiscais I – Mercadorias (ICMS/IPI)
C001 – Abertura do Bloco C
C990 – Encerramento do Bloco C
D – Documentos Fiscais II – Mercadorias (ICMS)
D001 – Abertura do Bloco D
D990 – Encerramento do Bloco D
F – Demais Documentos e Operações
F001 – Abertura do Bloco F
F600 – Contribuição Retida na Fonte
F700 – Deduções Diversas
F990 – Encerramento do Bloco F
I – Operações das Instituições Financeiras
I001 – Abertura do Bloco I
I010 – Identificação da Pessoa Jurídica/Estabelecimento
I100 – Consolidação das Operações do Período
I200 – Composição das Receitas, Deduções e/ou Exclusões do Período
I300 – Complemento das Operações – Detalhamento das Receitas, Deduções e/ou Exclusões do Período
I990 – Encerramento do Bloco I
M – Apuração da Contribuição e Credito de PIS/PASEP e da COFINS
M001 – Abertura do Bloco M
M200 – Consolidação da Contribuição para o PIS/PASEP do Período
M210 – Detalhamento da Contribuição para o PIS/PASEP do Período
M211 – Sociedades Cooperativas – Composição da Base de Cálculo – PIS/PASEP
M220 – Ajustes da Contribuição para o PIS/PASEP Apurada
M230 – Informações Adicionais do Período
M300 – Contribuição de PIS/PASEP Diferida em Períodos Anteriores – Valores a Pagar no Período
M350 – PIS/PASEP – Folha de Salários
M400 – Receitas Isentas, não alcançadas pela incidência da Contribuição, Sujeitas a Alíquota Zero ou de Vendas com Suspensão – PIS/PASEP
M410 – Detalhamento das Receitas Isentas, não alcançadas pela incidência da Contribuição, Sujeitas a Alíquota Zero ou de Vendas com Suspensão – PIS/PASEP
M600 – Consolidação da Contribuição para a Seguridade Social – COFINS do Período
M610 – Detalhamento da Contribuição para a Seguridade Social – COFINS do Período
M630 – Informações Adicionais do Período
M611 – Sociedades Cooperativas – Composição da Base de Cálculo – COFINS
M620 – Ajustes da COFINS Apurada
M700 – COFINS Diferida em Períodos Anteriores – Valores a Pagar no Período
M800 – Receitas Isentas, não alcançadas pela incidência da Contribuição, Sujeitas a Alíquota Zero ou de vendas com suspensão
M810 – Detalhamento das Receitas Isentas, não alcançadas pela incidência da Contribuição, Sujeitas a Alíquota Zero ou de vendas com suspensão
M990 – Encerramento do Bloco M
1 – Compl. da Escrituração – Sld. de Créditos e Retenções
1001 – Abertura do Bloco 1
1300 – Controle dos Valores Retidos na Fonte – PIS/PASEP
1700 – Controle dos Valores Retidos na Fonte – COFINS
1990 – Encerramento do Bloco 1
P – Apuração da Contribuição Previdenciária sobre Receita Bruta
P001 – Abertura do Bloco P
P990 – Encerramento do Bloco P
9 – Controle e Encerramento do Arquivo Digital
9001 – Abertura do Bloco 9
9900 – Registros do Arquivo
9990 – Encerramento do Bloco 9
9999 – Encerramento do Arquivo Digital	OS3810-B
OS3810-E		RN03	Os registros poderão ser marcados e desmarcados para serem gerados. Os registros a seguir deverão sempre estar selecionados e nunca poderão ser desmarcados:

0000 – Abertura do Arquivo Digital e Identificação da Pessoa Jurídica
0001 – Abertura do Bloco 0
0110 – Regimes de Apuração da Contribuição Social e de Apropriação do Crédito
0140 – Tabela de Cadastro do Estabelecimento
0990 – Encerramento do Bloco 0
A001 – Abertura do Bloco A
A990 – Encerramento do Bloco A
C001 – Abertura do Bloco C
C990 – Encerramento do Bloco C
D001 – Abertura do Bloco D
D990 – Encerramento do Bloco D
F001 – Abertura do Bloco F
F990 – Encerramento do Bloco F
I001 – Abertura do Bloco I
I990 – Encerramento do Bloco I
M001 – Abertura do Bloco M
M990 – Encerramento do Bloco M
P001 – Abertura do Bloco P
P990 – Encerramento do Bloco P
1001 – Abertura do Bloco 1
1990 – Encerramento do Bloco 1
9001 – Abertura do Bloco 9
9900 – Registros do Arquivo
9990 – Encerramento do Bloco 9
9999 – Encerramento do Arquivo Digital
	OS3810-A1
OS3810-B
OS3810-E		RN04	Deverá ser criado um relatório de conferência para essa tela de parametrização.	OS3810-A1		

Considerações deste modelo:


Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN
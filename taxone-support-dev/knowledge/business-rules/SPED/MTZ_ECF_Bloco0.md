# MTZ_ECF_Bloco0

> Fonte: MTZ_ECF_Bloco0.doc

THOMSON REUTERS

ECF – Geração do Arquivo
Bloco 0


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		07/03/2018	MFS-17083	Criação do Documento	Alessandra Cristina Navatta		24/08/2018	MFS-20563	Alterações para atender a versão 4.00

Ajustes na Regra: RNG0000-03
Inclusão da Regra: RNG0020-33	Heloísa Mirthes		25/09/2018	MFS-20964	Inclusão de mensagem de obrigatoriedade de campos (7, 9,10) no registro 0030 	Alessandra Cristina Navatta		

 TOC \o "1-5" \h \z \u  HYPERLINK \l "_Toc508281047" 1.	INTRODUÇÃO	 PAGEREF _Toc508281047 \h 3
 HYPERLINK \l "_Toc508281048" 2.	Regras de Negócio	 PAGEREF _Toc508281048 \h 3
 HYPERLINK \l "_Toc508281049" 2.1	Informações gerais de seleção e processamento	 PAGEREF _Toc508281049 \h 3
 HYPERLINK \l "_Toc508281050" 2.2	Registros Identificadores	 PAGEREF _Toc508281050 \h 3
 HYPERLINK \l "_Toc508281051" 2.2.1	Registro 0000: Abertura do Arquivo Digital e Identificação da Pessoa Jurídica	 PAGEREF _Toc508281051 \h 5
 HYPERLINK \l "_Toc508281052" 2.2.2	Registro 0001: Abertura do Bloco 0	 PAGEREF _Toc508281052 \h 9
 HYPERLINK \l "_Toc508281053" 2.2.3	Registro 0010: Abertura do Arquivo Digital e Identificação da Entidade	 PAGEREF _Toc508281053 \h 9
 HYPERLINK \l "_Toc508281054" 2.2.4	Registro 0020: Parâmetros Complementares	 PAGEREF _Toc508281054 \h 17
 HYPERLINK \l "_Toc508281055" 2.2.5	Registro 0021: Parâmetros de Identificação dos Tipos de Programa	 PAGEREF _Toc508281055 \h 26
 HYPERLINK \l "_Toc508281056" 2.2.6	Registro 0030: Dados Cadastrais	 PAGEREF _Toc508281056 \h 30
 HYPERLINK \l "_Toc508281057" 2.2.7	Registro 0035: Identificação das SCP	 PAGEREF _Toc508281057 \h 32
 HYPERLINK \l "_Toc508281058" 2.2.8	Registros 0930: Identificação dos Signatários da ECF	 PAGEREF _Toc508281058 \h 33
 HYPERLINK \l "_Toc508281059" 2.2.9	Registros 0990: Encerramento do Bloco 0	 PAGEREF _Toc508281059 \h 34

 DOCPROPERTY  Comments  \* MERGEFORMAT INTRODUÇÃO
Este bloco tem o objetivo de mostrar a abertura do arquivo, identificar a entidade e referenciar o período da ECF.
Regras de Negócio
Informações gerais de seleção e processamento
CÓD	DESCRIÇÃO	MFS		RNG-0	Para a geração deste bloco, o sistema deve recuperar os dados das tabelas de Estabelecimento, Informações ECF, Abertura da Apuração e Responsáveis. Considerando a data inicial e final da tela de geração.

Aplicar a RNG00004 - Versão de Layout. 

Aplicar a RNG00051 – Geração dos Registros, com exceção das validações abaixo, que se caso apresentarem erro devem interromper a geração:

O Sistema deve se as escriturações estão com a versão correta de Layout conforme RNG00003 - Versão da Escrituração. Se não for atendida da RNG acima, exibir a mensagem DW00018 para as escriturações com situação especial e a DW00019 sem situação especial no período.

Na tela de Perfil de geração o registro deve estar selecionado para a geração.


		MFS-17083		
Registros Identificadores
Relação de Registros a serem gerados:

Reg.	Nível	Descrição	Obrigatoriedade Entrada 	Obrigatoriedade Saída	Ocorrência		0000	0	Abertura do Arquivo Digital e Identificação da Pessoa Jurídica	O	O	[1:1]		0001	1	Abertura do Bloco 0
	O	O	[1:1]		0010	2	Parâmetros de Tributação
	O	O	[1:1]		0020	2	Parâmetros Complementares
	O	O	[1:1]		0021	2	Parâmetros de Identificação dos Tipos de Programa	F	A partir da Versão 3.00

OC

Obrigatório se 0020.IND_PJ_HAB = S
N
Senão, não deve existir 	[0:1]		0030	2	Dados Cadastrais 	O	O	[1:1]		0035	2	Identificação das SCP	F	OC
Obrigatório se 0000.TIP_ECF = 1
N
Senão, não deve existir	Se 0000.TIP_ECF = 1 [1:N]
Senão [0]
		0930	2	Identificação dos Signatários da ECF
	F	O	Até versão 2.00
[2:N]

A partir da versão 3.00:

[1:N]

		0990	1	Encerramento do Bloco 0	O	O	[1:1]		


Registro 0000: Abertura do Arquivo Digital e Identificação da Pessoa Jurídica 
Campo Chave: REG
Ocorrência: 1:1
Nível Hierárquico: 0

CÓD	DESCRIÇÃO		RNG0000	Para a geração deste bloco, o sistema deve recuperar os dados das tabelas de Estabelecimento, Informações ECF e Tela de Geração.

Para as tabelas de Estabelecimento, considerar sempre o registro mais atual.

Para a abertura da Apuração, considerar as Aberturas da Apuração correspondentes ao registro de “Informação ECF” selecionado na tela de Geração da ECF cuja Data Inicial e Data Final estejam dentro do período informado na tela (Data Inicial e Data Final da tela de Opções de Geração).
	MFS-17083		RNG0000-01	REG-Tipo de Registro

Gerar fixo ‘0000’	MFS-17083		RNG0000-02	Nome_ESC – Identificação do Tipo de Sped

Gerar fixo ‘LECF’
	MFS-17083		RNG0000-03	COD_VER – Código da versão do layout 

Se a Versão da Informações ECF do registro for igual a 1.00:
Gerar fixo ‘0001’

Se a Versão da Informações ECF do registro for igual a 2.00:
Gerar fixo ‘0002’

Se a Versão da Informações ECF do registro for igual a 3.00:
Gerar fixo ‘0003’


Se a Versão da Informações ECF do registro for igual a 4.00:
Gerar fixo ‘0004’
	MFS-17083/MFS-20563		RNG0000-04	CNPJ - CNPJ


Se na tela de Informações ECF, o Tipo da ECF a ser gerada for “0 - ECF de empresa não sócia ostensiva”, neste campo deverá ser exibido o CNPJ do Estabelecimento correspondente à escrituração que está sendo processada.

Se na tela de Informações ECF, o Tipo da ECF a ser gerada for “1 - ECF de sócia ostensiva”, neste campo deverá ser gerado o CNPJ do Estabelecimento Centralizador que possui SCPS vinculadas.

Se na tela de Informações ECF, o Tipo da ECF a ser gerada for “2 – ECF da SCP”, neste campo deverá ser exibido o CNPJ da Sócia Ostensiva (Estabelecimento centralizador da SCP).

Tratamentos:

Se o campo estiver sem preenchimento, exibir a mensagem DW00001.

Orientações: 

As SCPs vinculadas ao CNPJ da Sócia Ostensiva deverão ser identificadas por meio do estabelecimento da Informação ECF e o estabelecimento indicado na tela de Cadastros de SCP (módulo MastersafDW).
	MFS-17083		RNG0000-05	NOME- Nome empresarial

Recuperar na tabela de informações ecf, a razão social correspondente ao conteúdo informado no campo RNG0000-04.

Tratamentos:

Se o campo estiver sem preenchimento, exibir a mensagem DW00001.

	MFS-17083		RNG0000-06	IND_SIT_INI_PER – Indicador de início do período

Considerar a informação do campo ‘Indicador do Início do Período’ da tela de Geração.

Se a Versão da Informações ECF do registro for igual a 2.00, se o campo Indicador de Início do Período for igual à ‘3 – Resultante de Transformação, exibir a mensagem DW00179.

	MFS-17083		RNG0000-07	SIT_ESPECIAL - Indicador de situação especial e outros eventos

Considerar as regras abaixo:

Se no último período da abertura da apuração, do estabelecimento da escrituração selecionada para geração, não existir situação especial no período, este campo deve ser gerado com ‘0’. Se o campo situação especial no período estiver com ‘Sim’, o campo deve ser gerado, conforme as regras abaixo:

Gerar ‘1’ se o campo ‘Tipo da Situação Especial’, estiver preenchido com ‘Extinção’;
Gerar ‘2’ se o campo ‘Tipo da Situação Especial’, estiver preenchido com ‘Fusão’;
Gerar ‘3’ se o campo ‘Tipo da Situação Especial’, estiver preenchido com ‘Incorporação \ Incorporada’;
Gerar ‘4‘ se o campo ‘Tipo da Situação Especial’, estiver preenchido com ‘Incorporação \ Incorporadora’;
Gerar ‘5’ se o campo ‘Tipo da Situação Especial’, estiver preenchido com ‘Cisão Total’;
Gerar ‘6’ se o campo ‘Tipo da Situação Especial’, estiver preenchido com ‘Cisão Parcial’;
Gerar ‘7’ se o campo ‘Tipo da Situação Especial’, estiver preenchido com ‘Transformação’;
Gerar ‘8’ se o campo ‘Tipo da Situação Especial’, estiver preenchido com ‘Desenquadramento de Imune / Isenta’ ou 
Gerar ‘9’ se o campo ‘Tipo da Situação Especial’, estiver preenchido com ‘Inclusão no Simples Nacional’

	MFS-17083		RNG0000-08	PAT_REMAN_CIS - Patrimônio Remanescente Em Caso De Cisão (%)

Se o campo 07- SIT_ESPECIAL do registro 0000 estiver preenchido com informação diferente de ‘6’, este campo deve ser gerado com ||. Caso contrário, gerar este campo com a informação que está cadastrada na tela de Abertura da Apuração (último período da abertura da apuração), campo Patrimônio Remanescente em Caso de Cisão (%).


	MFS-17083		RNG0000-09	DT_SIT_ESP – Data da Situção Especial / Evento

Se o campo SIT_ESPECIAL (campo 07 do Registro 0000), estiver preenchido com informação diferente de ‘0’, este campo deve ser preenchido com a ‘data do evento’ informada na tela de “Abertura da Apuração’. Caso contrário, este campo deve ser gerado ||.
	MFS-17083		RNG0000-10	DT_INI – Data Inicial

Este campo deve ser preenchido com a Data Inicial da Abertura da Apuração que tenha a menor Data Inicial dentre as que foram recuperadas. 

	MFS-17083		RNG0000-11	DT_FIN – Data Final

Este campo deve ser preenchido com a Data Final da Abertura da Apuração que tenha a maior Data Inicial dentre as que foram recuperadas. 

	MFS-17083		RNG0000-12	RETIFICADORA – ESCRITURAÇÃO RETIFICADORA?

Considerar a informação do campo ”RETIFICADORA” da tela de Geração da ECF, 
Se a Opção “S – ECF retificadora” estiver selecionada, gerar “S”
Se a Opção “N – ECF original” estiver selecionada, gerar “N”
Se a opção F – ECF original com mudança de forma de tributação (Art. 5o da Instrução Normativa no 166/1999) estiver selecionada, gerar “F”	MFS-17083		RNG0000-13	NUM_REC – Número do Recibo Anterior

Considerar a informação do campo ‘Número do Recibo Anterior ’ na tela de Geração.

Se o campo 12 – RETIFICADORA estiver com ‘N’, este campo deve ser gerado ||. 

	MFS-17083		RNG0000-14	TIP_ECF -  Tipo da ECF


Recupera o conteúdo contido no campo Tipo da ECF do estabelecimento que está sendo processado.

Gerar “0” quando o campo “Tipo da ECF” estiver preenchido com “0 - ECF de empresa não sócia ostensiva”.
Gerar “1” quando o campo “Tipo da ECF” estiver preenchido com “1 - ECF de sócia ostensiva”.
Gerar “2” quando o campo “Tipo da ECF” estiver preenchido com “2 – ECF da SCP”.	MFS-17083		RNG0000-15	COD_SCP- Identificação da SCP


Este campo deve ser preenchido com o código da SCP somente quando na tela de geração o campo Tipo da ECF for igual a “2 – ECF”.

Se o valor informado para este campo possuir menos de 14 posições, completar as 14 posições com zeros à esquerda.

	MFS-17083		Registro 0001: Abertura do Bloco 0
Campo Chave: REG
Ocorrência: 1:1
Nível Hieráquivo: 1


CÓD	DESCRIÇÃO	MFS		RNG0001-01	REG – Tipo de  Registro

Gerar fixo ‘0001’
	MFS-17083		RNG0001-02	IND_DAD - Indicador de Movimento

Caso existirem informações nos registros do bloco 0 (registros 0010,0020,0021,0030,0035,0930), preencher com “0”, caso contrário, preencher com “1”.
	MFS-17083		
Registro 0010: Abertura do Arquivo Digital e Identificação da Entidade
Campo Chave: REG
Ocorrência: 1:1
Nível Hierárquico: 2


CÓD	DESCRIÇÃO	MFS		RNG0010	Para a geração deste bloco, o sistema deve recuperar os dados das tabelas de Estabelecimento, Informações ECF e Abertura da  Apuração, considerando os parâmetros informados na tela de geração.

Para a abertura da Apuração, considerar as Aberturas da Apuração correspondentes ao registro de “Informação ECF” selecionado na tela de Geração da ECF cuja Data Inicial e Data Final estejam dentro do período informado na tela (Data Inicial e Data Final da tela de Opções de Geração).
	MFS-17083		
RNG0010-01	REG – Tipo de Registro

Gerar fixo ‘0010’	MFS-17083		RNG0010-02	HASH_ECF_ANTERIOR – Hashcode da ECF do Período Imediatamente Anterior

Este campo é gerado pelo PVA, gerar ||.
	MFS-17083		RNG0010-03	OPT_REFIS - Indicador de Optante pelo Refis

Se o campo ‘Indicador de optante pelo REFIS’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.
	MFS-17083		RNG0010-04	OPT_PAES - Indicador de Optante pelo Paes

Se o campo ‘Indicador de optante pelo PAES’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

	MFS-17083		RNG0010-05	FORMA_TRIB - Forma de Tributação do Lucro

Se existir no ano exercício, aberturas de período de apuração com forma de tributação igual a “Lucro Real”, gerar “1”.
Se existir no ano exercício, aberturas de período de apuração com forma de tributação igual a “Lucro Real” e “Lucro Arbitrado”, gerar “2”.
Se existir no ano exercício, aberturas de período de apuração com forma de tributação igual a “Lucro Real” e “Lucro Presumido”, gerar “3”.
Se existir no ano exercício, aberturas de período da apuração com forma de tributação igual a “Lucro Real”, “Lucro Presumido” e “Lucro Arbitrado”, gerar “4”.
Se existir no ano exercício, aberturas de período de apuração com forma de tributação igual a “Lucro Presumido”, gerar “5”.
Se existir no ano exercício, aberturas de período de apuração com forma de tributação igual a “Lucro Arbitrado”, gerar “6”.
Se existir no ano exercício, aberturas de período de apuração com forma de tributação igual a “Lucro Arbitrado” e “Lucro Presumido”, gerar “7”.
Se existir no ano exercício aberturas de período de apuração com forma de tributação igual a “Imune de IRPJ”, gerar “8”.
S existir no ano exercício aberturas de período de apuração com forma de tributação igual a “Isento do IRPJ”, gerar “9 

Tratamentos:

Se o campo estiver sem preenchimento, exibir a mensagem DW00001.
	MFS-17083		RNG0010-06	FORMA_APUR – Período da Apuração do IRPJ e CSLL

Se o campo ‘Apuração’ da tela Informações ECF, estiver preenchido com:
‘Trimestral’, preencher este campo com ‘T’
‘Anual’, preencher este campo com ‘A’

Tratamentos:

Verifica quando campo FORMA_APUR (registro 0010) estiver preenchido com ‘A’ se FORMA_TRIB (registro 0010) diferente de ‘1’, ’2’,(’3’ e OPT_REFIS = ‘S’) ou (‘4’ e OPT_REFIS = ‘S’), neste caso, exibir a mensagem DW00174.

- Quando o campo RNG0010-05 for igual a 8 - “Imune de IRPJ” ou 9 - “Isento do IRPJ” este campo não deve ser gerado, logo, deverá ser gerado ||.
	MFS-17083		RNG0010-07	COD_QUALIF_PJ – Qualificação da Pessoa Jurídica

Se o campo ‘Qualificação da Pessoa Jurídica’ da tela Informações ECF, estiver preenchido com:

‘PJ em Geral’, preencher este campo com‘01’
‘PJ Componente do Sistema Financeiro’, preencher este campo com ‘02’
‘Sociedades Seguradoras, de Capitalização ou Entidade Aberta de Previdência Complementar’, preencher este campo com‘03’

Tratamento até a versão 2.00:
Verifica, quando FORMA_TRIB (registro 0010) igual a “3” ou “4” ou “5” ou “7”, se o campo COD_QUALIF_PJ (registro 0010) é diferente de “01” (PJ em geral) neste caso, exibir a mensagem DW00175.


Tratamento a partir da versão 3.00:

Verifica, quando FORMA_TRIB (registro 0010) igual a “3” ou “4” ou “5” ou “7”, se o campo COD_QUALIF_PJ (registro 0010) é diferente de “01” (PJ em geral) ou “02” (PJ componente do sistema financeiro). Neste caso, exibir a mensagem DW00178.
	MFS-17083		RNG0010-08	FORMA_TRIB_PER - Forma de Tributação no Período

- Quando o campo RNG0010-05 for igual a 8 - “Imune de IRPJ” ou 9 - “Isento do IRPJ” este campo não deve ser gerado, logo, deverá ser gerado ||.

Se o campo ‘Apuração’ da tela de “Informações ECF” for igual a “Trimestral” ou “Anual”, verificar na tela de Período da Abertura de Apuração qual é a forma de tributação correspondente a cada trimestre e gerar a informação “XXXX” no arquivo, onde cada “X” deve ser gerado conforme regras abaixo.

0 - ZERO (não informado – trimestre não compreendido no período de apuração)
R(Real)
P (Presumido)
A (Arbitrado)
E (Real Estimativa)

Se não houver movimentação no período ou não houver abertura de apuração correspondente, gerar “0”.
Se houver apuração do lucro presumido no período, gerar “P”.
Se houver apuração do lucro arbitrado no período, gerar “A”.
Se o campo FORMA_TRIB (RNG0010-05) for igual a “1” ou “2” e houver apuração do lucro real no período, gerar “R”.
Se o campo FORMA_TRIB (RNG0010-05) for igual a “3” ou “4”, o campo “Indicador de optante pelo REFIS” não estiver selecionado e houver apuração do lucro real no período, gerar “R”.
Se o campo FORMA_TRIB (RNG0010-05) for igual a “3” ou “4”, o campo “Indicador de optante pelo REFIS” estiver selecionado, o campo Apuração (RNG0010-06) for “Trimestral” e houver apuração do lucro real no período, gerar “R”.
Se o campo FORMA_TRIB (RNG0010-05) for igual a “3” ou “4”, o campo “Indicador de optante pelo REFIS” estiver selecionado, o campo Apuração (RNG0010-06) for “Anual” e houver apuração do lucro real no período, gerar “E”.
Exemplo:
1º Trimestre: Sem movimentação no período
2º Trimestre: Real
3º Trimestre: Real
4º Trimestre: Arbitrado

Resultado: 0RRA 

	MFS-17083		RNG0010-09	MÊS_BAL_RED – Indicação da Forma de Apuração da Estimativa

- Quando o campo RNG0010-05 for igual a 8 - “Imune de IRPJ” ou 9 - “Isento do IRPJ” este campo não deve ser gerado, logo, deverá ser gerado ||.

Se o campo Apuração for igual a “Anual”, na tela de Informações ECF e na tela de abertura da apuração, os períodos com o campo Forma de Tributação for igual a ‘Lucro Real’, verificar na tela Abertura da Apuração, a informação do Tipo de Receita de cada mês e gerar a informação “XXXXXXXXXXXX” no arquivo, onde cada “X” deve ser gerado conforme regras abaixo.

0 – Fora do Período: Fora do período de apuração/ Forma de tributação diferente de “R” ou “E”
E – Receita Bruta: Estimativa com base na receita bruta e acréscimos
B – Balanço ou Balancete: Estimativa com base no balanço ou balancete de suspensão/redução

Se não houver movimentação no período ou não houver abertura de apuração correspondente, gerar “0”.
Se houver apuração do lucro estimado no período e o cliente tiver optado por ela (Tipo de Receita da tela Abertura da Apuração = Receita Bruta), gerar “E”.
Se houver apuração do lucro real no período e o cliente tiver optado por ela (Tipo de Receita da tela Abertura da Apuração = Balanço Suspensão ou Redução), gerar “B”.

Exemplo:
Janeiro: Sem movimentação no período
Fevereiro: Lucro Estimado
Março: Lucro Estimado
Abril: Lucro Real
...

Resultado: 0EEB...


Se Tipo de Receita da tela Abertura da Apuração = ‘Comparativo’ e não tiver sido escolhida uma opção de Receita na tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução para a Abertura de Apuração correspondente, exibir a mensagem DW00184.
	MFS-17083		RNG0010-10	TIP_ESC_PRE – Tipo de Escrituração

Se o campo ‘05- Forma de Tributação’ do registro 0010 for igual a ‘3’, ’4’,‘5’, ‘7’,’8’ ou ‘9’ e o campo ‘Escrituração’ da tela Informações ECF, estiver preenchido com:
‘Livro Caixa ou Sem Escrituração’, preencher este campo com ‘L’
‘Contábil’, preencher este campo com ‘C’

Caso o campo esteja com informação = ‘Não se aplica’, exibir a mensagem DW00173.

Se o campo ‘05- Forma de Tributação’ do registro 0010 for igual a ‘1’,’2’,‘6’: 

Preencher este campo com ‘||’

	MFS-17083		RNG0010-11	TIP_ENT – Tipo de Pessoa Jurídica Imune ou Isenta


Se o campo ‘05- Forma de Tributação’ do registro 0010 for diferente de ‘8’ ou ‘9’, este campo deve ficar nulo.

Se o campo ‘05- Forma de Tributação’ do registro 0010 for ‘8’ ou ‘9’, 
Preencher este campo com o Tipo de Entidade da tela de Informação ECF.

	MFS-17083		RNG0010-12	FORMA_APUR_I – Existência de Atividade Tributada pelo IRPJ para Imunes ou Isentas


Se o campo ’05- Forma de Tributação’ do registro 0010 for igual a ‘8’ ou ‘9’, e o campo ‘Apuração do IRPJ’ da tela de Informações ECF, estiver preenchido com:

‘Anual’, preencher este campo com ‘A’;
‘Trimestral’, preencher este campo com ‘T’;
‘Desobrigada’, preencher este campo com ‘D’;


Se o campo ’05- Forma de Tributação’ do registro 0010 for diferente de ‘8’ ou ‘9, este campo deve ficar nulo.

	MFS-17083		RNG0010-13	APUR_CSLL – Apuração da CSLL para Imunes e Isentas


Se o campo ’05- Forma de Tributação’ do registro 0010 for igual a ‘8’ ou ‘9’, e o campo ‘Apuração da CSLL’ da tela de Informações ECF, estiver preenchido com:

‘Anual’, preencher este campo com ‘A’;
‘Trimestral’, preencher este campo com ‘T’;
‘Desobrigada’, preencher este campo com ‘D’;


Se o campo ’05- Forma de Tributação’ do registro 0010 for diferente de ‘8’ ou ‘9, este campo deve ficar nulo.
	MFS-17083		RNG00010-14	OPT_EXT_RTT - Optante pela  extinção do RTT no Ano Calendário 2014

Se a Versão da Informações ECF do registro for igual a 1.00:

- Quando o campo RNG0010-05 for igual a 5 - “Lucro Presumido” ou 6 - “Lucro Arbitrado” ou 8 - “Imune de IRPJ” ou 9 - “Isento do IRPJ” este campo não deve ser gerado, logo, deverá ser gerado ||.

Se o campo ‘Optante pela extinção do RTT no Ano-Calendário 2014’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Se a Versão da Informações ECF do registro igual a 2.00:

Se o campo ‘Optante pela extinção do RTT no Ano-Calendário 2014’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Se a Versão da Informações ECF do registro igual a 3.00 ou maior:

Não gerar este campo
	MFS-17083		RNG0010-15	DIF_FCONT – Diferenças entre a contabilidade societária e FCONT

Se a Versão da Informações ECF do registro for igual a 1.00:

- Quando o campo RNG0010-05 for igual a 5 - “Lucro Presumido” ou 6 - “Lucro Arbitrado” ou 8 - “Imune de IRPJ” ou 9 - “Isento do IRPJ” este campo não deve ser gerado, logo, deverá ser gerado ||.

Se o campo OPT_EXT_RTT - Optante pela extinção do RTT no Ano_Calendário 2014 for igual a “N” e não houver Situação Especial no período, Gerar || 

Se o campo OPT_EXT_RTT - Optante pela extinção do RTT no Ano_Calendário 2014 for igual a “N” e houver Situação Especial no período, Gerar |N|

Caso contrário, preencher com a informação do campo ‘Diferenças entre a Contabilidade Societária e FCONT’, na tela de Informações ECF, ou seja, se o campo estiver marcado gerar “S”, senão gerar “N”.

Se a Versão da Informações ECF do registro igual a 2.00:

Se o campo ‘Optante pela extinção do RTT no Ano-Calendário 2014’ estiver marcado na tela de Informações ECF, Gerar ||

Caso contrário, preencher com a informação do campo ‘Diferenças entre a Contabilidade Societária e FCONT’, na tela de Informações ECF, ou seja, se o campo estiver marcado gerar “S”, senão gerar “N”.


Se a Versão da tela de Informações ECF for igual a 3.00 ou maior:

Não gerar este campo
	MFS-17083		RNG0010-14_	IND_REC_RECEITA – Critério de Reconhecimento de Receitas

Se a Versão da tela de Informações ECF for menor que 3.00:

Não gerar este campo


Se a Versão da tela Informações ECF for igual a 3.00 ou maior:

Se o campo Critério de Reconhecimento de Receitas na tela de Informações ECF estiver nulo ou preenchido com ‘Não se aplica’, gerar ||
Se preenchido com ‘Regime de Caixa’, gerar ‘1’, se preenchido com ‘Regime de Competência’ gerar ‘2’. 

Validações:

Se existir abertura de apuração com forma de tributação igual a Lucro Presumido e se o campo não está preenchido com uma das opções ‘Regime de Caixa’ ou ‘Regime de Competência’, exibir a mensagem DW00176.

Se existir abertura de apuração com forma de tributação diferente de Lucro Presumido e se o campo está preenchido com uma das opções ‘Regime de Caixa’ ou ‘Regime de Competência’, exibir a exibir a mensagem DW00177.

	MFS-17083		

Registro 0020: Parâmetros Complementares
Campo Chave: REG
Ocorrência: 1:1
Nível Hierárquico: 2


CÓD	DESCRIÇÃO	MFS		RNG0020	Considerar as informações da tela de Informações ECF	MFS-17083		
RNG0020-01	REG – Tipo de Registro

Gerar fixo ‘0020’	MFS-17083		RNG0020-02	IND_ALIQ_CSLL - PJ Sujeita a Alíquota da CSLL 


Preencher de acordo com o valor de domínio preenchido no campo ‘PJ Sujeita à Alíquota da CSLL, na tela Informações ECF:
Domínio - Descrição
N - 9%
S - 15%
1 - 9%
2 - 17% 
3 - 20%


Se o campo não estiver habilitado na tela de Informações ECF, gerar nulo. 
	MFS-17083		RNG0020-03	IND_QTE_SCP - Quantidade de SCP da PJ


Quantidade de SCP da PJ - Sócio Ostensivo de SCP - Total de SCP.
Exibir a quantidade de SCPs geradas no registro 0035. 

Este campo deverá ser gerado quando o campo Tipo da ECF for igual a “1 - ECF de sócia ostensiva” na tela de geração da ECF.
	MFS-17083		RNG0020-04	IND_ADM_FUN_CLU - Administradora de Fundos e Clubes de Investimento

Se o campo ‘Administradora de Fundos e Clubes de Investimento’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo FORMA_TRIB (registro 0010) é igual a “8” e o campo TIP_ENT (registro 0010) é diferente de “06”, ”11” e “12” e se campo IND_ADM_FUN_CLU (registro 0020) é diferente de “N”, neste caso, exibir a mensagemDW00172.

	MFS-17083		RNG0020-05	IND_PART_CONS - Participações em Consórcios de Empresas

Se o campo ‘Participações em Consórcios de Empresas’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo TIP_ENT (registro 0010) é igual a “13”, se o campo IND_PART_CONS (registro 0020) é diferente de “N”, neste caso, exibir a mensagem DW00172.

	MFS-17083		RNG0020-06	IND_OP_EXT - Operações com o Exterior

Se o campo ‘Operações com o Exterior’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo FORMA_TRIB (registro 0010) é igual a “8” ou “9”, se o campo IND_OP_EXT (registro 0020) é diferente de “N”, neste caso, exibir a mensagem DW00172.

	MFS-17083		RNG0020-07	IND_OP_VINC - Operações com Pessoa Vinculada/Interposta Pessoa / Pais com Tributação Favorecida

Se o campo ‘Operações com Pessoa Vinculada/Interposta Pessoa / Pais com Tributação Favorecida’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo IND_OP_EXT (registro 0020) é igual a “N”, se o campo IND_OP_VINC (registro 0020) é diferente de “N”, neste caso, exibir a mensagem DW00172.

	MFS-17083		RNG0020-08	IND_PJ_ENQUAD - PJ Enquadrada no art. 48 ou 49 da IN RFB no 1.312/2012

Se o campo ‘PJ Enquadrada nos artigos 48 ou 49 da IN RFB no 1.312/2012’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.
	MFS-17083		RNG0020-09	IND_PART_EXT - Participações no Exterior

Se o campo ‘Participações no Exterior’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:

Verifica quando o campo FORMA_TRIB (registro 0010) igual a “8” ou “9”, se campo IND_PART_EXT (registro 0020) diferente de “N”, neste caso, exibir a mensagem: DW00172.

Se o campo FORMA_TRIB (registro 0010) [é igual a “5” ou “7” e OPT_REFIS (registro 0010) igual a “N”], então o campo IND_PART_EXT (registro 0020) deve ser igual a “N”, caso contrário, exibir a mensagem DW00172.

	MFS-17083		RNG0020-10	IND_ATIV_RURAL - Atividade Rural

Se o campo ‘Atividade Rural’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:

Se a Versão da Informações ECF do registro for igual a 1.00:

Verifica quando campo COD_QUALIF_PJ (registro 0010) é diferente de “01” ou campo FORMA_TRIB (registro 0010) é diferente de “1”, “2”, “3” ou “4”, se o campo IND_ATIV_RURAL (registro 0020) é diferente de “N”, neste caso, exibir a mensagem DW00172.

Se a Versão da Informações ECF do registro for maior ou igual a 2.00
Não há validação.
	MFS-17083		RNG0020-11	IND_LUC_EXP - Lucro da Exploração

Se o campo ‘Lucro da Exploração’ na tela informações ECF para o estabelecimento (matriz) estiver selecionado, gerar “S”. Caso contrário, gerar “N”.

Tratamento:

Verifica quando campo COD_QUALIF_PJ (registro 0010) é diferente de “01” ou campo FORMA_TRIB (registro 0010) é diferente de “1”, “2”, “3” ou “4”, se o campo IND_LUC_EXP (registro 0020) é diferente de “N”, neste caso, exibir a mensagem DW00172.
	MFS-17083		RNG0020-12	IND_RED_ISEN - Isenção e Redução do Imposto para Lucro Presumido

Se o campo ‘Isenção e Redução do Imposto para Lucro Presumido’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamento:

Verifica quando campo OPT_REFIS (registro 0010) é diferente de “S” e campo COD_QUALIF_PJ (registro 0010) é diferente de “01” e campo FORMA_TRIB (registro 0010) é diferente de “5”, ou “7”, e o campo IND_RED_ISEN (registro 0020) é diferente de “N”, neste caso, exibir a mensagem DW00172.
	MFS-17083		RNG0020-13	IND_FIN - FINOR/FINAM/FUNRES

Se o campo ‘FINOR/FINAM/FUNRES’ na tela informações ECF estiver marcado, gerar “S”. Caso contrário, gerar “N”.

Tratamento:

Verifica quando campo FORMA_TRIB (registro 0010) é diferente de “1”, “2”,”3”, ou “4”, se o campo IND_FIN (registro 0020) é diferente de “N”, neste caso, exibir a mensagem DW00172.

	MFS-17083		RNG0020-14	IND_DOA_ELEIT - Doações a Campanhas Eleitorais

Se o campo ‘Doações a Campanhas Eleitorais’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

	MFS-17083		RNG0020-15	IND_PART_COLIG - Participação Permanente em Coligadas ou Controladas

Se o campo ‘Participação Permanente em Coligadas ou Controladas’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo TIP_ENT (registro 0010) é igual a “13”, se o campo IND_PART_COLIG (registro 0020) é diferente de “N”, neste caso, exibir a mensagemDW00172.

	MFS-17083		RNG0020-16	IND_VEND_EXP - PJ Efetuou Vendas a Empresa Comercial Exportadora com Fim Especifico de Exportação
Se o campo ‘PJ Efetuou Vendas a Empresa Comercial Exportadora com Fim Especifico de Exportação’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:

Verifica quando o campo FORMA_TRIB (registro 0010) igual a “8” ou “9”, se campo IND_VEND_EXP (registro 0020) diferente de “N”, neste caso, exibir a mensagem DW00172.

Verifica quando campo COD_QUALIF_PJ (registro 0010) é diferente de “01”, se campo IND_VEND_EXP (registro 0020) diferente de “N”, neste caso, exibir a mensagem DW00172.
	MFS-17083		RNG0020-17	IND_ REC_EXT - Rendimentos do Exterior ou de Não Residentes

Se o campo ‘Rendimentos do Exterior ou de Não Residentes’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo TIP_ENT (registro 0010) é igual a “13”, se o campo IND_REC_EXT (registro 0020) é diferente de “N”, neste caso, exibir a mensagem DW00172.

	MFS-17083		RNG0020-18	IND_ATIV_EXT - Ativos no Exterior

Se o campo ‘Ativos no Exterior’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo TIP_ENT (registro 0010) é igual a “13”, se o campo IND_ATIV_EXT (registro 0020) é diferente de “N”, neste caso, exibir a mensagem DW00172.

Verifica quando o campo COD_QUALIF (registro 0010) é diferente de “01”, se o campo IND_ATIV_EXT (registro 0020) é diferente de “N”, neste caso, exibir a mensagem DW00172.

	MFS-17083		RNG0020-19	IND_COM_EXP - PJ Comercial Exportadora

Se o campo ‘PJ Comercial Exportadora’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo FORMA_TRIB (registro 0010) igual a “8” ou “9”,se campo IND_COM_EXP (registro 0020) diferente de “N”, neste caso, exibir a mensagem DW00172.

Verifica quando campo COD_QUALIF_PJ (registro 0010) é diferente de “01”, se campo IND_COM_EXP (registro 0020) diferente de “N”, neste caso, exibir a mensagem DW00172.
	MFS-17083		RNG0020-20	IND_PGTO_EXT - Pagamentos ao Exterior ou a Não Residentes

Se o campo ‘Pagamentos ao Exterior ou a Não Residentes’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo TIP_ENT (registro 0010) é igual a “13”, se o campo IND_PAG_EXT (registro 0020) é diferente de “N”, neste caso, exibir a mensagem DW00172.

	MFS-17083		RNG0020-21	IND_E-COM_TI - Comércio Eletrônico e Tecnologia da Informação

Se o campo ‘Comércio Eletrônico e Tecnologia da Informação’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo TIP_ENT (registro 0010) é igual a “13”, se o campo IND_E-COM_TI (registro 0020) é diferente de “N”, neste caso, exibir a mensagem DW00172.

	MFS-17083		RNG0020-22	IND_ROY_REC - Royalties Recebidos do Brasil e do Exterior

Se o campo ‘Royalties Recebidos do Brasil e do Exterior’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo TIP_ENT (registro 0010) é igual a “13”, se o campo IND_ROY_REC (registro 0020) é diferente de “N”, neste caso, exibir a mensagem DW00172.


	MFS-17083		RNG0020-23	IND_ROY_PAG - Royalties Pagos a Beneficiários do Brasil e do Exterior

Se o campo ‘Royalties Pagos a Beneficiários do Brasil e do Exterior’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo TIP_ENT (registro 0010) é igual a “13”, se o campo IND_ROY_PAG (registro 0020) é diferente de “N”, neste caso, exibir a mensagem DW00172.

	MFS-17083		RNG0020-24	IND_REND_SERV - Rendimentos Relativos a Serviços, Juros e Dividendos Recebidos do Brasil e do Exterior

Se o campo ‘Rendimentos Relativos a Serviços, Juros e Dividendos Recebidos do Brasil e do Exterior’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo TIP_ENT (registro 0010) é igual a “13”, se o campo IND_REND_SERV (registro 0020) é diferente de “N”, neste caso, exibir a mensagem DW00172.

	MFS-17083		RNG0020-25	IND_PGTO_REM - Pagamentos ou Remessas a Titulo de Serviços, Juros e Dividendos a Beneficiários do Brasil e do Exterior

Se o campo ‘Pagamentos ou Remessas a Titulo de Serviços, Juros e Dividendos a Beneficiários do Brasil e do Exterior’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo TIP_ENT (registro 0010) é igual a “13”, se o campo IND_PAG_REM (registro 0020) é diferente de “N”, neste caso, exibir a mensagem DW00172.
	MFS-17083		RNG0020-26	IND_INOV_TEC - Inovação Tecnológica e Desenvolvimento Tecnológico

Se o campo ‘Inovação Tecnológica e Desenvolvimento Tecnológico’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo FORMA_TRIB (registro 0010) igual a “8” ou “9” e campo IND_INOV_TEC (registro 0020) diferente de “N”, neste caso, exibir a mensagem DW00172.

	MFS-17083		RNG0020-27	IND_CAP_INF - Capacitação de Informática e Inclusão Digital

Se o campo ‘Capacitação de Informática e Inclusão Digital’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo FORMA_TRIB (registro 0010) igual a “8” ou “9”, se o campo IND_CAP_INF (registro 0020) diferente de “N”, neste caso, exibir a mensagem DW00172.

	MFS-17083		RNG0020-28	IND_PJ_HAB - PJ Habilitada no Repes, Recap, Padis, PATVD, Reidi, Repenec, Reicomp, Retaero, Recine, Resíduos Sólidos, Recopa, Copa do Mundo, Retid, REPNBL-Redes, Reif e Olimpíadas

Se o campo ‘PJ Habilitada no Repes, Recap, Padis, ... (vide ícone “i”)’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’. 

Tratamentos:

Para Versão anterior a 3.00
Verifica quando o campo FORMA_TRIB (registro 0010) igual a “8” ou “9”, se o campo IND_PJ_HAB (registro 0020) diferente de “N”, neste caso, exibir a mensagemDW00172.

Para Versão A partir da 3.00

Verifica quando o campo FORMA_TRIB (registro 0010) igual a “8” ou “9” e se TIP_ENT (registro 0010) é diferente de “14” (CIO e Entidades Relacionadas), se o campo IND_PJ_HAB (registro 0020) diferente de “N”, neste caso, exibir a mensagem: DW00172).

Quando selecionado, indica que o registro 0021 deve ser gerado.


	MFS-17083		RNG0020-29	IND_POLO_AM - Polo Industrial de Manaus e Amazônia Ocidental

Se o campo ‘Polo Industrial Manaus e Amazônia Ocidental’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo FORMA_TRIB (registro 0010) igual a “8” ou “9”, se o campo IND_POLO_AM (registro 0020) diferente de “N”, neste caso, exibir a mensagem: DW00172.

	MFS-17083		RNG0020-30	IND_ZON_EXP - Zonas de Processamento de Exportação

Se o campo ‘Zonas de Processamento de Exportação’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo FORMA_TRIB (registro 0010) igual a “8” ou “9”, se o campo IND_ZON_EXP (registro 0020) diferente de “N”, neste caso, exibir a mensagem DW00172.

	MFS-17083		RNG0020-31	IND_AREA_COM - Áreas de Livre Comércio

Se o campo ‘Áreas de Livre Comércio’ estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.

Tratamentos:
Verifica quando o campo FORMA_TRIB (registro 0010) igual a “8” ou “9”, se o campo IND_AREA_COM (registro 0020) diferente de “N”, neste caso, exibir a mensagem DW00172.

	MFS-17083		RNG0020-32	IND_PAIS_A_PAIS – Entidade Integrante de Grupo Multinacional

Para Informações ECF com versão anterior a 3.00:

Não gerar este campo

Para Informações ECF com versão a partir de 3.00

Se o campo ‘Entidade Integrante de Grupo Multinacional’ na tela de Informações ECF estiver desmarcado, gerar como ‘N’, se marcado gerar com ‘S’.


	MFS-17083		RNG0020-33	IND_DEREX - Declaração sobre utilização dos recursos em moeda estrangeira decorrentes do recebimento de exportações (DEREX)

Obs.: Exibir este campo para versões a partir da 4.00

Se o campo “Declaração sobre utilização dos recursos em moeda estrangeira decorrentes do recebimento de exportações (DEREX)” estiver marcado na tela de Informações ECF, gerar este campo com ‘S’, caso contrário com ‘N’.
	MFS-20563		
Registro 0021: Parâmetros de Identificação dos Tipos de Programa 
Campo Chave: REG
Ocorrência: 0:1
Nível Hierárquico: 2


CÓD	DESCRIÇÃO	MFS		RNG0021	Considerar as informações da tela de Informações ECF (aba Parâmetros dos Tipos de Programa) e quando no registro 0020 o campo RNG0020-28 - IND_PJ_HAB - PJ Habilitada no Repes, Recap, Padis, PATVD, Reidi, Repenec, Reicomp, Retaero, Recine, Resíduos Sólidos, Recopa, Copa do Mundo, Retid, REPNBL-Redes, Reif e Olimpíadas estiver selecionado.

Este registro só deve ser gerado para escriturações (Informações ECF) com versão a partir de 3.00.
	MFS-17083		
RNG0021-01	REG – Tipo de Registro

Gerar fixo ‘0021’	MFS-17083		RNG0021-02	IND_REPES - Regime Especial de Tributação para a Plataforma de Exportação de Serviços de Tecnologia da Informação (Repes)

Se o campo Regime Especial de Tributação para a Plataforma de Exportação de Serviços de Tecnologia da Informação (Repes) estiver desmarcado, gerar como ‘N’, se marcado gerar com ‘S’.	MFS-17083		RNG0021-03	IND_RECAP - Regime Especial de Aquisição de  Bens  de  Capital  para  Empresas Exportadoras (Recap)

Se o campo Regime Especial de Aquisição de Bens de  Capital  para  Empresas Exportadoras (Recap) estiver desmarcado, gerar como ‘N’, se marcado gerar com ‘S’.
	MFS-17083		RNG0021-04	IND_PADIS - Programa de Apoio ao Desenvolvimento Tecnológico da Indústria de Semicondutores (Padis)

Se o campo Programa de Apoio ao Desenvolvimento Tecnológico da Indústria de Semicondutores (Padis) estiver desmarcado, gerar como ‘N’, se marcado gerar com ‘S’.
	MFS-17083		RNG0021-05	IND_PATVD – Programa de Apoio ao Desenvolvimento Tecnológico da Indústria de Equipamentos para TV Digital (PATVD)

Se o campo Programa de Apoio ao Desenvolvimento Tecnológico da Indústria de Equipamentos para TV Digital (PATVD) estiver desmarcado, gerar como ‘N’, se marcado gerar com ‘S’.
	MFS-17083		RNG0021-06	IND_REIDI – Regime Especial de Incentivos para o Desenvolvimento da Infraestrutura (Reidi)

Se o campo Regime Especial de Incentivos para o Desenvolvimento da Infraestrutura (Reidi) estiver desmarcado, gerar como ‘N’, se marcado gerar com ‘S’.
	MFS-17083		RNG0021-07	IND_REPENEC – Regime Especial de Incentivos para o  Desenvolvimento da Infraestrutura  da  Indústria  Petrolífera  das  Regiões  Norte,  Nordeste e Centro-Oeste (Repenec)

Se o campo Regime Especial de Incentivos para o  Desenvolvimento da Infraestrutura  da  Indústria  Petrolífera  das  Regiões  Norte,  Nordeste e Centro-Oeste (Repenec) estiver desmarcado, gerar como ‘N’, se marcado gerar com ‘S’.
	MFS-17083		RNG0021-08	IND_REICOMP – Regime Especial de Incentivo a Computadores para Uso Educacional (Reicomp)

Se o campo Regime Especial de Incentivo a Computadores para Uso Educacional (Reicomp) estiver desmarcado, gerar como ‘N’, se marcado gerar com ‘S’.
	MFS-17083		RNG0021-09	IND_RETAERO – Regime Especial para a Indústria Aeronáutica Brasileira (Retaero)

Se o campo Regime Especial para a Indústria Aeronáutica Brasileira (Retaero) estiver desmarcado, gerar como ‘N’, se marcado gerar com ‘S’.
	MFS-17083		RNG0021-10	IND_RECINE – Regime Especial de Tributação para Des envolvimento da Atividade de Exibição Cinematográfica (Recine)

Se o campo Regime Especial de Tributação para Des envolvimento da Atividade de Exibição Cinematográfica (Recine) estiver desmarcado, gerar como ‘N’, se marcado gerar com ‘S’.
	MFS-17083		RNG0021-11	IND_RESIDUOS_SOLID – Estabelecimentos industriais que façam jus a crédito presumido do IPI na aquisição de resíduos sólidos, de que trata a Lei nº 12.375, de 30 de dezembro de 2010

Se o campo Estabelecimentos industriais que façam jus a crédito presumido do IPI na aquisição de resíduos sólidos, de que trata a Lei nº 12.375, de 30 de dezembro de 2010 estiver desmarcado, gerar como ‘N’, se marcado gerar com ‘S’.
	MFS-17083		RNG0021-12	IND_RECOPA – Regime Especial de Tributação para construção, ampliação, reforma ou modernização de estádios de futebol (Recopa)

Se o campo Regime Especial de Tributação para construção, ampliação, reforma ou modernização de estádios de futebol (Recopa) estiver desmarcado, gerar como ‘N’, se marcado gerar com ‘S’.
	MFS-17083		RNG0021-13	IND_COPA_DO_MUND – Habilitada para fins de fruição dos benefícios fiscais, não abrangidos na alínea anterior, relativos à realização, no Brasil, da Copa das Confederações FIFA ... (vide ícone "i")

Se o campo Habilitada para fins de fruição dos benefícios fiscais, não abrangidos na alínea anterior, relativos à realização, no Brasil, da Copa das Confederações FIFA ... (vide ícone "i") estiver desmarcado, gerar como ‘N’, se marcado gerar com ‘S’.
	MFS-17083		RNG0021-14	IND_RETID – Regime Especial Tributário para a Indústria de Defesa (Retid)

Se o campo Regime Especial Tributário para a Indústria de Defesa (Retid) estiver desmarcado, gerar como ‘N’, se marcado gerar com ‘S’.
	MFS-17083		RNG0021-15	IND_REPNBL_REDES – Regime Especial de Tributação do Programa Nacional de Banda Larga para Implantação de Redes de Telecomunicações (REPNBL-Redes)

Se o campo Regime Especial de Tributação do Programa Nacional de Banda Larga para Implantação de Redes de Telecomunicações (REPNBL-Redes) estiver desmarcado, gerar como ‘N’, se marcado gerar com ‘S’.
	MFS-17083		RNG0021-16	IND_REIF – Regime Especial de Incentivo ao Des envolvimento da Infraestrutura da Indústria de Fertilizantes (REIF)

Se o campo Regime Especial de Incentivo ao Des envolvimento da Infraestrutura da Indústria de Fertilizantes (REIF) estiver desmarcado, gerar como ‘N’, se marcado gerar com ‘S’.
	MFS-17083		RNG0021-17	IND_OLIMPIADAS – Habilitada para fins de fruição dos benefícios fiscais,  relativos  à realização,   no  Brasil,  dos  Jogos   Olímpicos   de   2016  e  dos  Jogos Paraolímpicos de 2016, de que trata a Lei nº 12.780, de 2013

Se o campo Habilitada para fins de fruição dos benefícios  fiscais,  relativos   à realização,   no  Brasil,  dos  Jogos   Olímpicos   de   2016  e  dos  Jogos Paraolímpicos de 2016, de que trata a Lei nº 12.780, de 2013 estiver desmarcado, gerar como ‘N’, se marcado gerar com ‘S’.
	MFS-17083		


	Registro 0030: Dados Cadastrais
Campo Chave: REG
Ocorrência: 1:1
Nível Hieráquivo: 2


CÓD	DESCRIÇÃO	MFS		RNG0030	Para a geração deste bloco, o sistema deve recuperar os dados das tabelas de Estabelecimento, da pessoa jurídica.	MFS-17083		
RNG0030-01	REG – Tipo de Registro

Gerar Fixo ‘0030’	MFS-17083		RNG0030-02	COD_NAT -  Natureza Jurídica 

Considerar a informação do campo Natureza Jurídica.
	MFS-17083		RNG0030-03	CNAE_FISCAL – Código da Atividade Econômica (CNAE-Fiscal) 

Considerar a informação do campo CNAE.
	MFS-17083		RNG0030-04	ENDEREÇO- Endereço

Considerar a informação do campo Tipo de Logradouro e Endereço. Formato: Logradouro Endereço.

	MFS-17083		RNG0030-05	NUM – Número 

Considerar a informação do campo Número.
Tratamento: 

Este campo é de preenchimento obrigatório, caso não esteja preenchido, preencher com “S/N”.

	MFS-17083		RNG0030-06	COMPL- Complemento

Considerar a informação do campo Complemento.
	MFS-17083		RNG0030-07	BAIRRO – Bairro/Distrito

Considerar a informação do campo Bairro.

Este campo é de preenchimento obrigatório, caso não esteja preenchido, exibir a mensagem DW00001.


	MFS-17083
MFS-20964		RNG0030-08	UF-UF

Considerar a informação do campo UF.
	MFS-17083		RNG0030-09	COD_MUN –Código do Município

Considerar a informação do campo Município (código do IBGE).

Este campo é de preenchimento obrigatório, caso não esteja preenchido, exibir a mensagem DW00001.

	MFS-17083
MFS-20964		RNG0030-10	CEP – CEP

Considerar a informação do campo CEP.

Este campo é de preenchimento obrigatório, caso não esteja preenchido, exibir a mensagem DW00001.


	MFS-17083
MFS-20964		RNG0030-11	NUM_TEL – Telefone 


Considerar a informação do campo DDD+ Telefone. Formato DDD Telefone
	MFS-17083		RNG0030-12	EMAIL-Correio Eletrônico

Considerar a informação do campo E-mail.
Tratamento: 

Este campo é de preenchimento obrigatório, caso não esteja preenchido, exibir a mensagem DW00001.

	MFS-17083		

Registro 0035: Identificação das SCP
Campo Chave: COD_SCP
Ocorrência: 1:N
Nível Hierárquico: 2

CÓD	DESCRIÇÃO	MFS		RNG0035	Este registro deverá ser gerado somente se na tela Informações ECF o campo Tipo da ECF = “1 - ECF de sócia ostensiva”.

Com base com o critério acima, recuperar as SCPs vinculadas ao CNPJ da Sócia Ostensiva parametrizada para a geração que possuam o campo Tipo da ECF = “2 – ECF da SCP”.

Identificação das SCPs vinculadas a uma Sócia Ostensiva:

As SCPs vinculadas ao CNPJ da Sócia Ostensiva deverão ser identificadas por meio do estabelecimento da Informação ECF e o estabelecimento indicado na tela de Cadastros de SCP (módulo MastersafDW).
	MFS-17083		RNG0035-01	REG – Tipo de Registro
Gerar Fixo ‘0035’
	MFS-17083		RNG0035-02	COD_SCP -Identificação da SCP 
(CNPJ – Art. 52 da Instrução Normativa RFB no 1.470, de 30 de maio de 2014)

Recuperar o conteúdo do campo Código da SCP.

Se o valor informado para este campo possuir menos de 14 posições, completar as 14 posições com zeros à esquerda.
	MFS-17083		RNG0035-03	NOME_SCP – Descrição da SCP
Recuperar o conteúdo do campo Descrição da SCP.
	MFS-17083		

	Registros 0930: Identificação dos Signatários da ECF
Campo Chave: IDENT_CPF_CNPJ + IDENT_QUALIF
Ocorrência: 2:N, a partir da versão 3.00 1:N
Nível Hierárquico: 2


CÓD	DESCRIÇÃO	MFS		RNG0930	Considerar as informações dos Signatários (tela Responsáveis), informados na tela de Informações ECF.

Gerar dois registros da tabela de responsáveis correspondentes aos campos “Signatário (contador) e Signatário (outros) na seguinte ordem:

1º signatário (contador)
2º signatário (outros)
	MFS-17083		RNG0930-01	REG – Tipo de Registro

Gerar fixo ‘0930’	MFS-17083		RNG0930-02	
IDENT_NOM – Nome Signatário

Considerar o nome do Signatário informado na tela de Informações ECF.
	MFS-17083		RNG0930-03	IDENT_CPF_CNPJ – CPF/CNPJ

Considerar o CPF/CNPJ do signatário informado na tela de Informações ECF.	MFS-17083		RNG0930-04	IDENT_QUALIF- Qualificação do Assinante

Considerar a qualificação do Assinante do signatário informado na tela de Informações ECF.

Exibir no arquivo primeiramente o registro cujo código da qualificação do assinante = ‘900’	MFS-17083		RNG0930-05	IND_CRC – Inscrição Contabilista
Considerar a Inscrição do Contabilista do signatário informado na tela de Informações ECF.	MFS-17083		RNG0930-06	EMAIL – Email

Considerar E-mail do signatário informado na tela Responsáveis.	MFS-17083		RNG0930-07	FONE-Fone 
Considerar o DDD + Telefone do signatário informado na tela Responsáveis.	MFS-17083		

Registros 0990: Encerramento do Bloco 0
Campo Chave: REG
Ocorrência: 1:1
Nivel Hierárquico: 1


CÓD	DESCRIÇÃO	MFS		RNG0990-01	REG – Tipo de Registro

Gerar fixo ‘0990’
	MFS-17083		RNG0990-02	QTD_LIN – Quantidade Total de Registro do Bloco 0

Para geração desse registro o sistema deverá internamente contar quantas linhas existem no arquivo no bloco 0 e informar o total.
Considerando que Campo 1: Texto fixo contendo "0990", e campo 2: Quantidade total de linhas do bloco0.

Exemplo: |0990|8|	MFS-17083		


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN
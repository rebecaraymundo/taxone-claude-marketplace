# MTZ_EFD_PIS-COFINS-Gerar_Ajustes_Creditos_NF_Mercantil

> Fonte: MTZ_EFD_PIS-COFINS-Gerar_Ajustes_Creditos_NF_Mercantil.doc

EFD PIS/COFINS – Gerar Ajustes de Créditos a partir de NF Mercantil


DOCUMENTO DE REQUISITO

DR	Nome	Descrição		MFS-46981	Ajustes automáticos para EFD-Contribuições	Automação para criar os registros de documentos fiscais nos registros M110 e M510 da EFD Contribuições buscando da SAFX08 para a apuração do PIS/COFINS. Característica: Cálculo		MFS-92367	Rogério Ohashi / Elisabete Costa	Inclusão de Alíquotas PIS/COFINS - Tratamento da regra de cálculo para considerar as Alíquotas de 1% para Pis e 4,6% para Cofins, que devem gerados com a Natureza de Crédito igual à 102.		MFS-94240	Elisabete Costa	Inclusão de Condição por CFOP - Tratamento da regra de cálculo para considerar as Alíquotas de 2,2% para Pis e 10,3% para Cofins, que devem gerados de acordo com o CFOP para as naturezas de crédito 102 e 202		MFS-97032	Elisabete Costa	Desconsiderar as regras fixas no código (Hardcode) PIS e COFINS (CST 49 e 98) e passar a considerar conforme parâmetros.		MFS-782970	Rosemeire Santos	Tratamento da regra para considerar todos os tipos de créditos disponíveis de acordo com a Tabela “4.3.6 – Tabela Código de Tipo de Crédito.		
REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN00	Deverá ser incluído o menu Obrigações ( Automação Ajustes de Crédito – Nota Mercantil. Esse item estará disponível exclusivamente para o Tax One.

Ao acionar o menu, deverá ser apresentado a tela de geração com as seguintes informações:
Apenas simular – campo do tipo checkbox, marcado por padrão. Será utilizado para indicar para o processo se deverá ser realizado o processo completo (incluindo gravação de dados) ou apenas simulado (demonstração dos dados em planilha Excel para conferência).
Apuração – campo do tipo multiprocessamento, onde deverão ser listadas todas as apurações atualmente abertas da empresa selecionada no login. Nessa listagem serão apresentadas as informações: Empresa / Estabelecimento – Data Inicial da Apuração a Data Final da Apuração. Além das informações formatadas anteriormente, deverão ser apresentados no quadro de seleção os campos : Layout, Situação da Apuração e Perfil.
	MFS-46981		RN01	Após selecionar as informações em tela e solicitar a execução do processo, a geração será iniciada com os seguintes passos:
Carregar dados de apuração – detalhado na RN02
Limpar registros manuais – detalhado na RN03
Processar dados PIS – detalhado na RN04
Processar dados COFINS – detalhado na RN05
Recalcula Apuração – detalhado na RN06
Gravação do arquivo de Conferência (Excel) – detalhado na RN07
	MFS-46981		RN02	Carregar dados da apuração - recuperar os dados da tabela EPC_APURACAO considerando ID_REG igual ao selecionado na janela de seleção (RN00).
	MFS-46981		RN03	Limpar registros manuais – caso na janela de seleção a opção de “Apenas Simular” estiver desmarcado, efetuar a limpeza da tabela EPC_REST_AJT_M110_M510 de todos os registros que atendam ao seguinte critério:
Empresa igual ao código da empresa da apuração selecionada na RN02;
Estabelecimento igual ao código do estabelecimento da apuração selecionada na RN02;
Tipo de Livro igual ao código do tipo de livro da apuração selecionada na RN02;
Dt. Inicial igual a data inicial da apuração selecionada na RN02;
Dt. Final igual a data final da apuração selecionada na RN02;
Indicador de gravação igual ao valor ‘5’ (geração);

[MFS-97032]
O Indicador de gravação (IND_GRAVACAO) passará a ser recuperado da RN06 do Menu Parâmetro de Ajustes de Crédito dos Registro M110/M510
	MFS-46981
MFS-97032		RN04	Processar dados PIS – deverão ser recuperados todos os documentos fiscais de mercadoria (com itens), base Datamart, considerando os seguintes critérios:
Empresa igual ao código da empresa da apuração selecionada na RN02;
Estabelecimento pertencente a relação de estabelecimentos centralizados pelo estabelecimento da apuração selecionada na RN02. Considerar o próprio estabelecimento da apuração na seleção;
Data fiscal compreendida entre a data inicial e final da apuração selecionada na RN02;
Nota fiscal não cancelada identificada através do campo Situação diferente de “S”;
Situação PIS deverá ser igual a ‘49’ ou ‘98’;
Deverá ter valor de PIS maior que zero;

[MFS-92367]
Alíquota de PIS deverá ser 1, 1.65, 2.1, 2.2 ou 3.52;

A partir dos documentos recuperados e agrupando por Data Fiscal, Movimento E/S, Número e Série do Documento, CFOP, Descrição do CFOP, Estabelecimento e Alíquota PIS, selecionar as seguintes informações:
COD_CRED_M100_M500 – correspondente a seguinte regra:
Se alíquota for 1.65 então 101
Se alíquota for 1 então 102
Se alíquota for 2.20 então 202
Demais casos deverá ser 108

[MFS-97032]
A alíquota PIS passará a ser recuperado da RN03 do Menu Parâmetro de Ajustes de Crédito dos Registro M110/M510

ALIQ_M100_M500 – igual a Alíquota de PIS
IND_AJ – correspondente a seguinte regra:
Se movimento E/S for saída então 0
Demais casos será 1
DT_REF – corresponde ao valor da Data Fiscal da nota
VL_AJ – corresponde ao valor de PIS
NUM_DOC – corresponde ao Número do Documento Fiscal concatenado com a Série do documento fiscal. Utilizar ‘/’ para separar as informações.
DSC_AJ – corresponde a concatenação das seguintes informações: 
“Ajuste em Decorrência”
Descrição do CFOP (CFOP)
“Filial” (Código do Estabelecimento)

[MFS-94240]
Alíquota de PIS 2.2;
COD_CFO – corresponde ao Código de CFOP da nota
Se CFOP iniciado com 1,2,5,6 então 102
Se CFOP iniciado com 3 e 7 então 202

Gravar os dados recuperados na tabela EPC_REST_AJT_M110_M510 conforme RN08
	MFS-46981
MFS-92367
MFS-94240
MFS-97032		RN05	Processar dados COFINS – deverão ser recuperados todos os documentos fiscais de mercadoria (com itens), base Datamart, considerando os seguintes critérios:
Empresa igual ao código da empresa da apuração selecionada na RN02;
Estabelecimento pertencente a relação de estabelecimentos centralizados pelo estabelecimento da apuração selecionada na RN02. Considerar o próprio estabelecimento da apuração na seleção;
Data fiscal compreendida entre a data inicial e final da apuração selecionada na RN02;
Nota fiscal não cancelada identificada através do campo Situação diferente de “S”;
Situação COFINS deverá ser igual a ‘49’ ou ‘98’;
Deverá ter valor de COFINS maior que zero;

[MFS-92367]
Alíquota de COFINS deverá ser 4.6, 7.6, 9.65, 10.30, 16.48;


A partir dos documentos recuperados e agrupando por Data Fiscal, Movimento E/S, Número e Série do Documento, CFOP, Descrição do CFOP, Estabelecimento e Alíquota COFINS, selecionar as seguintes informações:
COD_CRED_M100_M500 – correspondente a seguinte regra:
Se alíquota for 7.6 então 101
Se alíquota for 4.6 então 102
Se alíquota for 10.30 então 202
Demais casos deverá ser 108
[MFS-97032]
A alíquota COFINS passará a ser recuperado da RN04 do Menu Parâmetro de Ajustes de Crédito dos Registro M110/M510

ALIQ_M100_M500 – igual a Alíquota de COFINS
IND_AJ – correspondente a seguinte regra:
Se movimento E/S for saída então 0
Demais casos será 1
DT_REF – corresponde ao valor da Data Fiscal da nota
VL_AJ – corresponde ao valor de COFINS
NUM_DOC – corresponde ao Número do Documento Fiscal concatenado com a Série do documento fiscal. Utilizar ‘/’ para separar as informações.
DSC_AJ – corresponde a concatenação das seguintes informações: 
“Ajuste em Decorrência”
Descrição do CFOP (CFOP)
“Filial” (Código do Estabelecimento)
[MFS-94240]
Alíquota de COFINS 10.30;
COD_CFO – corresponde ao Código de CFOP da nota
Se CFOP iniciado com 1,2,5,6 então 102
Se CFOP iniciado com 3 e 7 então 202

Gravar os dados recuperados na tabela EPC_REST_AJT_M110_M510 conforme RN08
	MFS-46981
MFS-92367
MFS-94240
MFS-97032		RN06	Recalcula Apuração – executar o processo Restauração dos Lançamentos Manuais, selecionando o período de apuração obtido na RN01, estabelecimento da apuração e marcando os registros M110 e M510
	MFS-46981		RN07	Gravação do arquivo de Conferência (Excel) – deverá ser salvo um arquivo em formato Excel com todos os dados de ajustes recuperados na RN04 e RN05 para conferência do usuário.
	MFS-46981		RN08	Gravar movimentos – caso a opção de “Apenas Simular” informada na RN00 estiver desmarcado, efetuar a gravação dos dados da tabela EPC_REST_AJT_M110_M510 conforme definição abaixo:
COD_EMPRESA – igual ao código da Empresa recuperado da apuração na RN01;
COD_ESTAB – igual ao código de estabelecimento recuperado da apuração na RN01;
COD_TIPO_LIVRO – igual ao código do tipo de livro recuperado da apuração na RN01;
DAT_APUR_INI – igual a data inicial da apuração recuperado da apuração na RN01;
DAT_APUR_FIM – igual a data final da apuração recuperado da apuração na RN01;
COD_REG_M100_M500 – em se tratando de PIS deve-se gravar o valor 100, sendo COFINS gravar 500;
IND_CRED_ORI_M100_M500 – gravar fixo o valor ‘0’;
COD_REG – em se tratando de PIS gravar 110, sendo COFINS gravar 510;
COD_AJ – gravar fixo o valor ‘05’(Ajuste Oriundo de Outras Situações);
IND_GRAVACAO – gravar fixo o valor ‘5’ (Geração);

[MFS-97032]
COD_AJ e IND_GRAVACAO - Passará a ser recuperado da RN06 Cód Ajustes de Contribuição do menu Parâmetros.

COD_CRED_M100_M500 – gravar com o valor da coluna recuperada na RN04 e 05;
ALIQ_M100_M500 - gravar com o valor da coluna recuperada na RN04 e 05;
IND_AJ - gravar com o valor da coluna recuperada na RN04 e 05;
DT_REF - gravar com o valor da coluna recuperada na RN04 e 05;
VL_AJ - gravar com o valor da coluna recuperada na RN04 e 05;
NUM_DOC - gravar com o valor da coluna recuperada na RN04 e 05;
DSC_AJ - gravar com o valor da coluna recuperada na RN04 e 05;
ID_REST_M110_M510 – recuperar e gravar o próximo valor da sequência SEQ_EPC_REST_AJT_M110_M510;
	MFS-46981
MFS-97032		RN09	Alterar a regra para o Cód. Tipo Crédito, buscando todos os códigos de acordo com a TFIX93 - Tabela Código de Tipo de Crédito da obrigação acessória SPED Contribuições (EPC_COD_CRED_TRANS) de acordo com a parametrização da tela Parâmetros > Ajustes Automáticos M110/M510 > Regras

Código 
4.3.6 – Tabela Código de Tipo de Crédito - Descrição 

CÓDIGOS VINCULADOS À RECEITA TRIBUTADA NO MERCADO INTERNO – Grupo 100

101
Crédito vinculado à receita tributada no mercado interno – Alíquota Básica

102
Crédito vinculado à receita tributada no mercado interno – Alíquotas Diferenciadas

103
Crédito vinculado à receita tributada no mercado interno – Alíquota por Unidade de Produto

104
Crédito vinculado à receita tributada no mercado interno – Estoque de Abertura

105
Crédito vinculado à receita tributada no mercado interno – Aquisição Embalagens para revenda

106
Crédito vinculado à receita tributada no mercado interno – Presumido - agroindústria e aquisição combustível

107
Crédito vinculado à receita tributada no mercado interno – Outros Créditos Presumidos

108
Crédito vinculado à receita tributada no mercado interno – Importação

109
Crédito vinculado à receita tributada no mercado interno – Atividade Imobiliária

CÓDIGOS VINCULADOS À RECEITA NÃO TRIBUTADA NO MERCADO INTERNO – Grupo 200

201
Crédito vinculado à receita não tributada no mercado interno – Alíquota Básica

202
Crédito vinculado à receita não tributada no mercado interno – Alíquotas Diferenciadas

203
Crédito vinculado à receita não tributada no mercado interno – Alíquota por Unidade de Produto

204
Crédito vinculado à receita não tributada no mercado interno – Estoque de Abertura

205
Crédito vinculado à receita não tributada no mercado interno – Aquisição Embalagens para revenda

206
Crédito vinculado à receita não tributada no mercado interno – Presumido - agroindústria e aquisição combustível

207
Crédito vinculado à receita não tributada no mercado interno – Outros Créditos Presumidos

208
Crédito vinculado à receita não tributada no mercado interno – Importação

CÓDIGOS VINCULADOS À RECEITA DE EXPORTAÇÃO – Grupo 300

301
Crédito vinculado à receita de exportação – Alíquota Básica

302
Crédito vinculado à receita de exportação – Alíquotas Diferenciadas

303
Crédito vinculado à receita de exportação – Alíquota por Unidade de Produto

304
Crédito vinculado à receita de exportação – Estoque de Abertura

305
Crédito vinculado à receita de exportação – Aquisição Embalagens para revenda

306
Crédito vinculado à receita de exportação – Presumido -agroindústria e aquisição combustível

307
Crédito vinculado à receita de exportação – Outros Créditos Presumidos

308
Crédito vinculado à receita de exportação – Importação

	MFS-782970
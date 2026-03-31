# MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Parametrizacao_por_Conta_Contabil

> Fonte: MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Parametrizacao_por_Conta_Contabil.doc

TITLE   \* MERGEFORMAT EFD-Contribuições Financeira/Assemelhada - Parametrização por Conta Contábil 

Localização da tela: 
        Módulo: SPED - EFD-Contribuições Financeira/Assemelhada
        Menu: Parâmetros ( Parametrização por Conta Contábil


DOCUMENTO DE REQUISITO 

DR	Nome	Descrição		OS3810
	EFD-Contribuições Financeira/Assemelhada – Parametrização por Conta Contábil	Essa OS tem por objetivo a criação do módulo EFD-Contribuições Financeira/Assemelhada. Trata-se da escrituração digital dos tributos PIS e COFINS para as instituições financeiras, seguradoras, entidades de previdência privada, operadoras de planos de assistência à saúde e assemelhadas, conforme Ato Declaratório Executivo nº. 65 de 20/12/12.		OS3810-C	EFD-Contribuições Financeira/Assemelhada - Criação de SAFX para tela de Parametrização por Conta Contábil, Criação da tela de manutenção do registro F600 e Crítica da Natureza da Receita	Essa OS tem por objetivo permitir as seguintes alterações no módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas:

Criar uma nova tabela SAFX para permitir a importação dos dados de parametrização da Conta Contábil;
Criar tela do registro F600 para posterior geração do registro;
Ajustar críticas da Natureza da Receita na tela de Parametrização da Conta Contábil.		OS4499	Inclusão do campo Data de Validade na SAFX144	Criar campo data inicial e final de validade na tabela SAFX144 para validar a data limite para a parametrização das contas contábil;
Criar botão para retorno de conta contábil parametrizadas;
Alterar a regra para seleção de conta contábil.       		MFS61556	Andréa Rocha	Inclusão de novos códigos (02 a 05) para os campos de Código de Situação Tributária do PIS e Código de Situação Tributária do COFINS, de acordo com os códigos disponibilizados no Guia Prático.		


Cód.	


Descrição	


DR		RN01	Deverá ser criada uma tela chamada “Parametrização por Conta Contábil” no módulo EFD-Contribuições Financeira/Assemelhada.

Essa parametrização será do tipo CRUD (Create/Read/Update/Delete), ou seja, será permitida a inclusão, consulta, alteração e exclusão dos registros.	OS3810		RN02	[ALTERADO – OS3810-C] A tela disponibilizará os seguintes campos:

Estabelecimento: será exibido o estabelecimento selecionado no Manager. Caso nenhum estabelecimento esteja selecionado no Manager, o sistema permitirá que o usuário selecione o Estabelecimento de acordo com a Empresa previamente selecionada no Manager. O estabelecimento será exibido/selecionado no formato Código do Estabelecimento + Descrição do Estabelecimento. Exemplo: 001 – Estabelecimento 001. Campo obrigatório de preenchimento.

Código Situação Tributária PIS: o usuário deverá selecionar o Código da Situação Tributária PIS cadastrado no Mastersaf DW. Será permitida a seleção de apenas um Código Situação Tributária PIS. Campo obrigatório de preenchimento. As informações serão recuperadas da tabela Y2027_SIT_TRIBUTARIA, quando o campo IND_TRIBUTACAO = “1”. Só serão exibidos os seguintes códigos:

[MFS61556] Inclusão dos códigos 02, 03, 04 e 05, conforme a lista de códigos disponibilizada pelo Guia Prático

1 – Operação Tributável com Alíquota Básica
2 - Operação Tributável com Alíquota Diferenciada
3 - Operação Tributável com Alíquota por Unidade de Medida de Produto
4 - Operação Tributável Monofásica - Revenda a Alíquota Zero
5 - Operação Tributável por Substituição Tributária
6 – Operação Tributável a Alíquota Zero
7 – Operação Isenta da Contribuição
8 – Operação sem Incidência da Contribuição
9 – Operação com Suspensão da Contribuição
49 – Outras Operações de Saída
99 – Outras Operações
Alíquota PIS: o usuário deverá informar a Alíquota referente ao PIS. O campo deverá ser numérico de 7 posições, sendo 3 inteiras e 4 decimais. Campo não obrigatório de preenchimento.

Código Situação Tributária COFINS: o usuário deverá selecionar o Código da Situação Tributária COFINS cadastrado no Mastersaf DW. Será permitida a seleção de apenas um Código Situação Tributária PIS. Campo obrigatório de preenchimento. As informações serão recuperadas da tabela Y2027_SIT_TRIBUTARIA, quando o campo IND_TRIBUTACAO = “2”. Só serão exibidos os seguintes códigos:

[MFS61556] Inclusão dos códigos 02, 03, 04 e 05, conforme a lista de códigos disponibilizada pelo Guia Prático

1 – Operação Tributável com Alíquota Básica
2 - Operação Tributável com Alíquota Diferenciada
3 - Operação Tributável com Alíquota por Unidade de Medida de Produto
4 - Operação Tributável Monofásica - Revenda a Alíquota Zero
5 - Operação Tributável por Substituição Tributária
6 – Operação Tributável a Alíquota Zero
7 – Operação Isenta da Contribuição
8 – Operação sem Incidência da Contribuição
9 – Operação com Suspensão da Contribuição
49 – Outras Operações de Saída
99 – Outras Operações

Alíquota COFINS: o usuário deverá informar a Alíquota referente ao COFINS. O campo deverá ser numérico de 7 posições, sendo 3 inteiras e 4 decimais. Campo não obrigatório de preenchimento.

Código Receita/Dedução/Exclusão: o usuário deverá selecionar o Código da Receita/Dedução/Exclusão que foi importado através da TACES82. Será permitida a seleção de apenas um Código Receita/Dedução/Exclusão. Caso o Código de Receita/Dedução/Exclusão possua um Código de Atributo o mesmo deverá ser informado no mesmo conjunto de campos. Caso contrário, não será necessário informar esse dado. Vale frisar que o Código Receita/Dedução/Exclusão possui o Atributo. O Atributo é um campo chave e não obrigatório na tela. O campo Código Receita/Dedução/Exclusão é obrigatório de preenchimento, enquanto que o Atributo não é obrigatório de preenchimento.


Código Complemento Receita/Dedução/Exclusão: o usuário deverá selecionar o Código de Complemento da Receita/Dedução/Exclusão que foi importado através da TACES83. Será permitida a seleção de apenas um Código de Complemento da Receita/Dedução/Exclusão. Campo obrigatório de preenchimento.
OBS: vale frisar que o conteúdo desse campo será definido a partir das tabelas 7.1.3 e 7.1.4 que ainda não foram disponibilizadas pela RFB. Estamos no aguardo dessa definição. Enquanto isso, a tabela foi criada com um conteúdo fake para agilizar o processo de desenvolvimento e homologação.

Código Natureza Receita: o usuário deverá selecionar o Código de Natureza da Receita que foi importado através da TACES72 (tabela: DWT_NAT_REC). Será permitida a seleção de apenas um Código de Natureza de Receita. Campo obrigatório de preenchimento. Caso o cliente preencha a Natureza da Receita, porém não defina o “Código Situação Tributária PIS” ou “Código Situação Tributária COFINS”, o sistema deverá exibir a seguinte mensagem de erro: “CST PIS/COFINS não definido. Será necessário informá-lo para a seleção da Natureza Receita.”

Informar Conta/Descrição para Pesquisa: nesse campo o usuário poderá realizar uma pesquisa através do Código da Conta Contábil ou da Descrição da Conta Contábil. As informações serão recuperadas da tabela X2002_PLANO_CONTAS. Esse critério de seleção não é obrigatório de preenchimento. Ao clicar em “Pesquisar”, as contas exibidas em “Conta Contábil” serão alteradas de acordo com a informação preenchida.

Conta Contábil: serão exibidas somente as contas contábeis cadastradas no Plano de Contas da Empresa, desconsiderando as contas sintéticas. As contas contábeis analíticas serão recuperadas da tabela X2002_PLANO_CONTAS. Será obrigatória a seleção de pelo menos uma conta contábil analítica.


Período Inicial: Nesse campo o usuário poderá colocar uma data inicio para a conta selecionada.
Campo de preenchimento obrigatório. 

Período Final: Nesse campo o usuário poderá colocar uma data de validade para o parâmetro selecionado, após a data limite o parâmetro será desconsiderado.

Não serão permitidos cadastros de período intermitente quando os seguintes campos se repetirem:
TABELA
ITEM
DESCRIÇÂO
NOME DO CAMPO

SAFX144
01
Código da Empresa
COD_EMPRESA

SAFX144
02
Código do Estabelecimento
COD_ESTAB

SAFX144
03
Código da situação tributária PIS
COD_SIT_TRIB_PIS

SAFX144
05
Código da Situação Tributária COFINS
COD_SIT_TRIB_COFINS

SAFX144
07
Código da Receita/Dedução/Exclusão
COD_REC_DED_EXC

SAFX144
09
Código do Complemento da Receita/Dedução/Exclusão
COD_REC_DED_EXC_COMPL

SAFX144
11
Código da Conta Contábil
COD_CONTA


O sistema não poderá permitir novo registro sem preenchimento da data final de validade para a mesma conta e critério de parametrização, quando já existir a mesma conta e critérios de parametrização com data final de validade vazia.  Botão Mostrar Parametrizadas: irá mostrar somente ás contas que se encontram parametrizado, levando em consideração a identificação do parâmetro selecionado. 


Replicar para os Estabelecimentos: nessa parte, o usuário poderá replicar a parametrização para os outros estabelecimentos da empresa. Campo não obrigatório de preenchimento.


Na abertura da tela, o sistema deverá permitir que o usuário selecione o Grupo de Validade que está utilizando.	OS3810
OS3810-C
OS4499
MFS61556		RN03	A chave dessa tabela deverá ser composta pelos seguintes campos:

Estabelecimento
Código Situação Tributária PIS
Alíquota PIS
Código Situação Tributária COFINS
Alíquota COFINS
Código Receita/Dedução/Exclusão
Atributo Receita/Dedução/Exclusão
Código Complemento Receita/Dedução/Exclusão
Código Natureza Receita
Conta Contábil
Data Inicial – A ser definido pelo A&D

	OS3810
OS4499
		RN04	Deverá ser criado um relatório de conferência para essa tela.	OS3810		RN05	A inclusão de CST de PIS e do CST de COFINS deverá possuir o mesmo código no momento da inclusão ou alteração do registro. Caso o CST de PIS e COFINS sejam diferentes, o sistema não deverá permitir a gravação e deverá exibir a seguinte mensagem de erro:

“Não é permitida a inclusão de CST de PIS e COFINS diferentes para a parametrização da Conta Contábil.”	OS3810		RN06	[EXCLUÍDO – OS3810-C] Caso o usuário informe um “Código Situação Tributária PIS” ou “Código Situação Tributária COFINS” que não possua Código Natureza Receita, o sistema deverá exibir a seguinte mensagem:

“Não existe Natureza Receita para o Código de Situação Tributária PIS/COFINS. Por gentileza corrigir a informação”.

Além de a mensagem ser exibida, o sistema não permitirá a gravação dessa informação.	OS3810
OS3810-C		
Considerações deste modelo:


Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN
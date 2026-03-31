---
source: "MTZ-ICMS-Geracao_GUIA_ICMS-ST (1).doc"
category: Tax Payments
converted: auto
---

	ICMS-ST - Geração da Guia de Pagamento


OBS: As regras referentes a Geração da Guia do ICMS-ST 

MTZ - INTEGRA_DOOTAX_GERAÇÃO

DOCUMENTO DE REQUISITO -LAYOUT SAIDA
Campos para geração do JSON:

CAMPO
NOME
FORMATO
TAMANHO
OBRIG.
CHAVE
Grupo de Imposto
        ICMS-ST
Texto

SIM
(*)
Código da Empresa
COD_EMPRESA
N
003
SIM
(*)
Código Do Estabelecimento
COD_ESTABELECIMENTO
N
006
SIM
(*)
Periodo da Apuração
PERIODO
DD/MM/AAAA
008
SIM
(*)
Código de Arrecadação
COD_ARRECADACAO
N
020
SIM
(*)
Código da Receita
COD_RECEITA
N
020
SIM
(*)
UF
UF
TEXTO
002
NÃO

Documento de Origem

NUM_DOC_ORIGEM

A
019
SIM

Série
SERIE
N
030
NÃO

Detalhamento da Receita
DET_RECEITA
N
020
NÃO

Data de Vencimento
DATA_VENCIMENTO
DD/MM/AAAA
008
NÃO

Data de Pagamento
DATA_PAGAMENTO
DD/MM/AAAA
008
NÃO

Valor
VL_PRINCIPAL
N
15,2
SIM


REGRAS DE NEGÓCIO

Cód.
Descrição

RN00
Empresa - Dados da Empresa: Informações cadastrais da empresa responsável pela apuração.

ADO 743264
RN01
Estabelecimento - Dados dos Estabelecimentos: Detalhes dos estabelecimentos vinculados à empresa
ADO 743264
RN02
Preenchimento do campo UF_FAVORECIDA
O campo UF_FAVORECIDA será preenchido conforme os valores apresentados na tabela Resumo_APUR_ST. Para isso, será utilizado o conteúdo do campo IDENT_ESTADO como referência para realizar a consulta na tabela ESTADO, retornando o valor correspondente do campo COD_ESTADO.

ADO 743264
ADO1037079
RN03
Exibe o período selecionado pelo usuário para realizar a busca na Apuração do ICMS-ST.CAMPO DAT_APURACAO
ADO 743264
RN04
Preenchimento do Campo Grupo de Imposto = ICMS-ST
ADO 743264
RN05
Preenchimento do Campo "COD_ARRECADACAO":

O campo "COD_ARRECADACAO" será preenchido com base na tabela TACE (Tabela de Código Tax Payments - DOOTAX). Este campo deve exibir uma lista de códigos de arrecadação aplicáveis, permitindo que o usuário selecione o código apropriado para cada tipo de imposto e regime tributário. A configuração é detalhada da seguinte forma:
* ICMS-ST
o Fonte: TACE (Tabela de Código Tax Payments - DOOTAX)
o Campo: COD_ARRECADACAO -
o Ação: Exibir lista de códigos de arrecadação aplicáveis.

ADO 743264
RN06
Regra de Preenchimento do Campo COD_RECEITA:


O campo COD_RECEITA deve ser preenchido de acordo com o tipo de imposto IPI. A configuração específica é a seguinte:
Configuração por Tipo de Imposto e Regime Tributário:

ICMS-ST
 COD_RECEITA 
* Regras de Validação:
1. Consistência dos Dados:
o O valor do campo COD_RECEITA deve ser atribuído exclusivamente de acordo com o tipo de imposto e regime tributário selecionado.
o Caso o tipo de imposto ou regime não seja identificado, o campo não deve ser preenchido.
2. Mensagem de Erro:
o Se o preenchimento estiver incorreto, exibir a seguinte mensagem:
"Seleção inválida: O valor do campo COD_RECEITA não corresponde ao tipo de imposto ou regime tributário selecionado."

ADO 743264
RN07
Preenchimento do campo Detalhamento da Receita :

1. Interação do Usuário:
o O usuário deverá selecionar um valor no campo COD_RECEITA. Após a seleção, o sistema deve carregar automaticamente o detalhamento correspondente no campo DET_RECEITA.
2. O campo "DET_RECEITA" será preenchido com base na tabela TACE (Tabela de Código Tax Payments - DOOTAX). O conteúdo deste campo deve ser relacionado diretamente ao valor selecionado no campo "COD_RECEITA", garantindo a consistência entre os códigos de receita e seus respectivos detalhamentos. A configuração para cada tipo de imposto e regime tributário é definida da seguinte forma:
* ICMS-ST:
o Fonte: TACE (Tabela de Código Tax Payments - DOOTAX)
o Campo: DET_RECEITA
o Regra: Este campo será automaticamente relacionado ao valor selecionado no campo COD_RECEITA.

* A integração entre os campos COD_RECEITA e DET_RECEITA deve garantir que o detalhamento correto seja exibido, eliminando inconsistências e erros de preenchimento.
* Caso o campo COD_RECEITA não seja preenchido ou esteja inválido, o sistema deve impedir o preenchimento do campo DET_RECEITA e exibir uma mensagem de validação como:
"Selecione um código de receita válido para visualizar o detalhamento correspondente."

ADO 743264
RN08
Regra para Preenchimento do Valor da Guia de Pagamento
Campo: Valor

Regras de Negócio
* Descrição Geral:
O campo "Valor da Guia de Pagamento" exibirá os valores do imposto ICMS-ST apurados para o período selecionado. Esses valores são atualizados dinamicamente conforme as ações do usuário na tela de busca do período de apuração.
* Fonte dos Dados:
Os valores apresentados são provenientes da tabela Resumo_APUR_ST, considerando os seguintes filtros:
o COD_TIPO_DO_LIVRO igual a 108 ou 165
o COD_ESTADO = UF FAVORECIDA
o COD_OPER_APURAR igual a 013
o Campo considerado: VLR_ICMS

ADO 743264
ADO 1037079
RN09
Regra de Composição do ID
Sempre que o campo num_doc_origem for preenchido, o sistema deverá compor o ID utilizando os seguintes elementos, com tamanhos ajustados:
1. Cod_Empresa: 3 caracteres (Exemplo: "001").
2. Cod_Estabelecimento: 6 caracteres (Exemplo: "000001").
3. Cod_Receita: 6 caracteres (Exemplo: "131701").
4. Hora de Geração: 4 caracteres (Exemplo: "1536").
Estrutura do ID:
[Cod_Empresa][Cod_Estabelecimento][Cod_Receita][Hora]
Exemplo Final:
0010000011317011536

ADO 743264
RN09
1. Data de Vencimento Interação do Usuário:
o O usuário deve selecionar o tipo de imposto (PIS ou COFINS) e o regime tributário (Cumulativo ou Não Cumulativo).
o O usuário deve informar quantidade de dias que deseja antecipar ou dias uteis
2. Cálculo Automático:
o O sistema identifica o vencimento regular do tributo com  data final da apuração.
o O sistema calcula o vencimento antecipado, subtraindo a quantidade de dias úteis especificada pelo usuário.
o O sistema considera apenas dias úteis (segunda a sexta-feira), excluindo feriados nacionais e regionais.
* Regra: Dias úteis.
* Cálculo: O vencimento ocorre após a contagem de dias úteis (segunda a sexta, excluindo feriados nacionais) a partir da data final da apuração.

ADO 743264


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN


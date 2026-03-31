# REQUISITO_MTZ-ICMS-Geracao_Guia de Pagamento - SCANC

- **Fonte:** REQUISITO_MTZ-ICMS-Geracao_Guia de Pagamento - SCANC.docx
- **Modificado:** 2026-01-13
- **Tamanho:** 43 KB

---

# 	SCANC – Geração da Guia de Pagamento

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>OBS: As regras referentes a Geração da Guia do SCANC 

MTZ – INTEGRA\_DOOTAX\_GERAÇÃO

##### DOCUMENTO DE REQUISITO \-LAYOUT SAIDA

Campos para geração do JSON:

###### CAMPO

###### NOME

__FORMATO__

__TAMANHO__

__OBRIG\.__

__CHAVE__

Grupo de Imposto

SCANC

Texto

SIM

\(\*\)

Código da Empresa

COD\_EMPRESA

N

003

SIM

\(\*\)

Código Do Estabelecimento

COD\_ESTABELECIMENTO

N

006

SIM

\(\*\)

Periodo da Apuração

PERIODO

DD/MM/AAAA

008

SIM

\(\*\)

Código de Arrecadação

COD\_ARRECADACAO

N

020

SIM

\(\*\)

Código da Receita

COD\_RECEITA

N

020

SIM

\(\*\)

UF

UF

TEXTO

002

NÃO

Documento de Origem

NUM\_DOC\_ORIGEM

A

019

SIM

Série

SERIE

N

030

NÃO

Detalhamento da Receita

DET\_RECEITA

N

020

NÃO

Data de Vencimento

DATA\_VENCIMENTO

DD/MM/AAAA

008

NÃO

Data de Pagamento

DATA\_PAGAMENTO

DD/MM/AAAA

008

NÃO

Valor

VL\_PRINCIPAL

N

15,2

SIM

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

__RN00__

Empresa \- Dados da Empresa: Informações cadastrais da empresa responsável pela SAFX 348\.

Na SAFX 348 \(SCANC \- Dados Guias de Pagamentos e Contabilização\), a Empresa corresponde ao campo COD\_EMPRESA, que possui 3 caracteres, deve ser preenchido conforme o cadastro de estabelecimento elegíveis, é um campo chave primária e obrigatório\.

Exemplo de preenchimento: “001”

Localização: Vide campo 1 da SAFX 348

__RN01__

Estabelecimento \- Dados dos Estabelecimentos__:__ Detalhes dos estabelecimentos vinculados à empresa\.

Na SAFX 348 \(SCANC \- Dados Guias de Pagamentos e Contabilização\), o Estabelecimento corresponde ao campo COD\_ESTABELECIMENTO, que possui 6 caracteres, deve ser preenchido conforme o cadastro de estabelecimentos elegíveis, é um campo chave primária e obrigatório\.

Exemplo de preenchimento: “000001”

Localização: Vide campo 2 da SAFX 348

__RN02__

Preenchimento do Campo "UF" do Estabelecimento\.

De acordo com a SAFX 348 \(SCANC – Dados Guias de Pagamento e Contabilização\), a UF informa a Unidade Federativa \(Estado\), este campo possui 2 caracteres e é obrigatório ser preenchido\.

Exemplo de preenchimento: “RJ”

Localização: Vide campo 18 da SAFX 348

__RN03__

Exibe o período selecionado pelo usuário para realizar a busca na Apuração na SAFX 348\.

De acordo com a SAFX 348 \(SCANC \- Dados Guias de Pagamentos e Contabilização\), o Período corresponde ao campo PERIODO, que possui 6 caracteres, deve ser preenchido conforme cadastro de estabelecimento elegível, é um campo chave primária e é obrigatório\.

Exemplo de preenchimento: "202401" → "31/01/2024" \(último dia do mês\)

Localização: Vide campo 3 da SAFX 348

__RN04__

Preenchimento do Campo Grupo de Imposto = SCANC

O campo Grupo de Imposto está presente na SAFX como GRUPO\_IMPOSTO, possui 10 caracteres, é obrigatório e chave primária\. Deve ser preenchido informando se o imposto pertence ao âmbito Estadual ou Federal\.

O campo GRUPO\_IMPOSTO deve ser preenchido com o valor fixo "SCANC" para identificar que a guia de pagamento se refere ao Sistema de Controle e Acompanhamento de Combustíveis, relacionado ao ICMS\-ST \(Imposto sobre Circulação de Mercadorias e Serviços \- Substituição Tributária\)\.

__Âmbito do Imposto:  __

• SCANC está relacionado ao ICMS\-ST, que é um imposto de ÂMBITO ESTADUAL  

• O ICMS\-ST incide sobre operações interestaduais com combustíveis e   

  derivados de petróleo  

__RN05__

Preenchimento do Campo "COD\_ARRECADACAO":

O campo "COD\_ARRECADACAO" será preenchido com base na tabela TACE \(Tabela de Código Tax Payments \- DOOTAX\)\. Este campo deve exibir uma lista de códigos de arrecadação aplicáveis, permitindo que o usuário selecione o código apropriado para cada tipo de imposto e regime tributário\. A configuração é detalhada da seguinte forma:

- ICMS\-ST \(SCANC\)
	- Fonte: TACE \(Tabela de Código Tax Payments \- DOOTAX\)
	- Campo: COD\_ARRECADACAO \-
	- Ação: Exibir lista de códigos de arrecadação aplicáveis\.

__RN06__

Regra de Preenchimento do Campo COD\_RECEITA:

  


O campo COD\_RECEITA deve ser preenchido de acordo com o tipo de imposto SCANC\. A configuração específica é a seguinte:

Configuração por Tipo de Imposto e Regime Tributário:

SCANC

 COD\_RECEITA 

- Regras de Validação:

1. Consistência dos Dados:
	- O valor do campo COD\_RECEITA deve ser atribuído exclusivamente de acordo com o tipo de imposto e regime tributário selecionado\.
	- Caso o tipo de imposto ou regime não seja identificado, o campo não deve ser preenchido\.
2. Mensagem de Erro:
	- Se o preenchimento estiver incorreto, exibir a seguinte mensagem:  
"Seleção inválida: O valor do campo COD\_RECEITA não corresponde ao tipo de imposto ou regime tributário selecionado\."

__RN07__

Preenchimento do campo Detalhamento da Receita :

1. Interação do Usuário:
	- O usuário deverá selecionar um valor no campo COD\_RECEITA\. Após a seleção, o sistema deve carregar automaticamente o detalhamento correspondente no campo DET\_RECEITA\.
2. O campo "DET\_RECEITA" será preenchido com base na tabela TACE \(Tabela de Código Tax Payments \- DOOTAX\)\. O conteúdo deste campo deve ser relacionado diretamente ao valor selecionado no campo "COD\_RECEITA", garantindo a consistência entre os códigos de receita e seus respectivos detalhamentos\. A configuração para cada tipo de imposto e regime tributário é definida da seguinte forma:

- ICMS\-ST \(SCANC\):
	- Fonte: TACE \(Tabela de Código Tax Payments \- DOOTAX\)
	- Campo: DET\_RECEITA
	- Regra: Este campo será automaticamente relacionado ao valor selecionado no campo COD\_RECEITA\.
- A integração entre os campos COD\_RECEITA e DET\_RECEITA deve garantir que o detalhamento correto seja exibido, eliminando inconsistências e erros de preenchimento\.
- Caso o campo COD\_RECEITA não seja preenchido ou esteja inválido, o sistema deve impedir o preenchimento do campo DET\_RECEITA e exibir uma mensagem de validação como:  
"Selecione um código de receita válido para visualizar o detalhamento correspondente\."

__RN08__

Regra para Preenchimento do Valor da Guia de Pagamento

Campo: Valor

Regras de Negócio

- Descrição Geral:  
O campo "Valor da Guia de Pagamento" exibirá os valores do imposto ICMS\-ST \(SCANC\) apurados para o período selecionado\. Esses valores são atualizados dinamicamente conforme as ações do usuário na tela de busca do período de apuração\.
- Fonte dos Dados:  
Os valores apresentados são provenientes da SAFX 348, considerando os seguintes filtros:
	- Campo considerado: ICMS\_DESTINO\_GUIA\_COMPL
		- Na SAFX 348, o campo ICMS\_DESTINO\_GUIA\_COMPL informa o valor do ICMS no destino quando for necessário gerar a API para integração com o sistema DOOTAX\. 
		- Quando preenchido, indica que será necessário gerar uma guia de pagamento por meio do envio de JSON para o sistema DOOTAX\. 
		- Ele é um campo obrigatório, numérico e possui 015V002 como tamanho\.

__RN09__

Regra de Composição do ID

Sempre que o campo num\_doc\_origem for preenchido, o sistema deverá compor o ID utilizando os seguintes elementos, com tamanhos ajustados:

1. Cod\_Empresa: 3 caracteres \(Exemplo: "001"\)\.
2. Cod\_Estabelecimento: 6 caracteres \(Exemplo: "000001"\)\.
3. Cod\_Receita: 6 caracteres \(Exemplo: "131701"\)\.
4. Hora de Geração: 4 caracteres \(Exemplo: "1536"\)\.

Estrutura do ID:  
\[Cod\_Empresa\]\[Cod\_Estabelecimento\]\[Cod\_Receita\]\[Hora\]

Exemplo Final:  
0010000011317011536

__RN10__

1. Data de Vencimento Interação do Usuário:
	- O usuário deve selecionar o tipo de imposto \(SCANC\) 
	- O usuário deve informar quantidade de dias que deseja antecipar ou dias uteis
	- Este campo é obrigatório e composto por 8 caracteres \(formato: __DDMMAAAA\)__
	- Exemplo de preenchimento: 31012024  
		- Dia: 31
		- Mês: 01 \(Janeiro\)
		- Ano: 2024
2. Cálculo Automático:
	- O sistema identifica o vencimento regular do tributo com  data final da apuração\.
	- O sistema calcula o vencimento antecipado, subtraindo a quantidade de dias úteis especificada pelo usuário\.
	- O sistema considera apenas dias úteis \(segunda a sexta\-feira\), excluindo feriados nacionais e regionais\.

- Regra: Dias úteis\.
- Cálculo: O vencimento ocorre após a contagem de dias úteis \(segunda a sexta, excluindo feriados nacionais\) a partir da data final da apuração\.

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


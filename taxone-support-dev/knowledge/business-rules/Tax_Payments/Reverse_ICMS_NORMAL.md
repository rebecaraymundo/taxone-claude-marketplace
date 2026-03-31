---
source: "Reverse_ICMS_NORMAL.docx"
category: Tax Payments
converted: auto
---

**Função EXECUTAR**

**Contexto inicial da função**
p_periodo: Representa um período de tempo, usado em cálculos ou consultas relacionadas.
p_grp_imp: Um grupo de imposto, sugerindo que a função trabalha com regras fiscais ou tributárias.
p_uf_estab: Unidade federativa de um estabelecimento, indicando que a função pode ter lógica dependente da localização.
p_cod_estab: Um código relacionado a estabelecimentos, de um tipo específico Lib_Proc.Vartab.
Dentro da função, é inicializado um identificador de processo mproc_id.
A função cria ou registra um novo processo no sistema, usando a biblioteca interna chamada LIB_PROC.
A função EXECUTAR realiza diversas operações importantes. Aqui estão as principais etapas e chamadas encontradas:
**Detalhes da função EXECUTAR**
Criação de um processo:
Adição de logs:
Recuperação de parâmetros:
Validação de módulo e diretório:
Recupera valores do módulo para uso no processamento:
Valida se o módulo e o diretório existem, emitindo logs de atenção se não forem encontrados:
Inserções em tabelas temporárias:
Insere dados de estabelecimentos em uma tabela temporária:
**Dependências Identificadas:**
LIB_PROC: Provavelmente uma biblioteca interna para criação de processos, adição de logs e manipulação de parâmetros.
LIB_PARAMETROS: Biblioteca para recuperar e salvar parâmetros específicos, como códigos de empresas e usuários.
Funções SQL (SELECT): Usadas para buscar valores de tabelas de configuração (FPAR_PARAMETROS, PRT_DIRETORIOS_SERVIDOR).
Tabela temporária: FLUX_HEINEKEN_ESTAB_TEMP_CPROC, usada para armazenar dados relacionados a estabelecimentos.

**Procedure GERA_ICMS_NORMAL**

**1. Função Interna json**
Objetivo: Auxiliar na formatação de strings como campos JSON.
Uso: Essa função é usada para estruturar os dados processados no formato JSON para geração de arquivos ou logs.
Retorna uma string formatada como JSON, baseada nos parâmetros fornecidos:
Parâmetros:
nome_campo: Nome do campo no JSON.
valor: Valor associado ao campo.
ultimo: Indica se é o último campo (evita vírgulas no final).


**2. Declarações de Variáveis e Cursores**
**Variáveis Locais:**
**Cursor geraJSON1:**
Realiza consultas detalhadas em várias tabelas relacionadas a dados fiscais.
Campos Selecionados:
Informações de impostos, como grupo, códigos de arrecadação e receita.
Período e identificação do estabelecimento (ex.: COD_ESTAB).
Valores de apuração (VALOR_PRINCIPAL), vencimento (DATA_VENCIMENTO) e pagamento (DATA_PAGAMENTO).
Regras e convenções fiscais específicas, como REGRA_IMPOSTO.

**3. Processamento Principal**
**Iterações sobre o Cursor geraJSON1:**
Para cada registro obtido, os dados são processados, validados e, formatados para saída (JSON ou tabela).
Campos Calculados:
Exemplo: Data de vencimento é calculada com base em uma função chamada calcula_data_vencimento.
**Validações e Logs:**
Verifica a integridade dos dados e gera mensagens de erro ou sucesso.
Exemplo: Logs são gerados para monitorar a ausência de configurações esperadas.
**Inserção de Dados:**
Os registros processados são inseridos em tabelas específicas:

**4. Regras Específicas**
**Mapeamentos de Parâmetros:**
Utiliza tabelas de parâmetros como fpar_parametros e fpar_param_det para determinar valores relevantes.
**Integração com Outras Funções/Procedures:**
Exemplo: A procedure ou função calcula_data_vencimento é chamada para determinar as datas de vencimento de obrigações fiscais.

**Conclusão**
A procedure realiza um processamento fiscal completo, envolvendo:
Consulta e validação de dados fiscais.
Aplicação de regras tributárias e empresariais.
Registro e log de erros ou eventos.
Possível geração de arquivos JSON ou inserção de dados em tabelas específicas.

**Função calcula_data_vencimento**
A função calcula_data_vencimento realiza cálculos complexos para determinar datas de vencimento baseadas em regras específicas, estados, municípios e tipos de dias (úteis ou feriados). Aqui está um detalhamento das principais operações:

**Parâmetros da Função**
pCod_Tp_Dt: Tipo de cálculo para a data (ex.: "DU" para dia útil, "DF" para data fixa).
pDia_Vc: Dia base para cálculo.
pMesano: Período no formato mês/ano.
pIdent_estado: Identificador do estado.
pCod_Municipio: Código do município.

**Lógica da Função**
**Cálculo para Dia Útil (DU):**
Busca a data de vencimento baseada no número de dias úteis (pDia_Vc).
Usa a tabela FLUX_VW_CALENDARIO_CPROC, que armazena o calendário fiscal, incluindo dias úteis e feriados.
**Condições:**
Se apenas o estado é especificado:
Se o município também é especificado:
**Cálculo para Data Fixa (DF):**
Constrói uma data fixa com base no dia e mês/ano fornecidos:
**Cálculo para Feriados Específicos (DA ou FA):**
Determina a data de vencimento considerando ajustes para feriados municipais ou estaduais:

**Tabelas Envolvidas**
**FLUX_VW_CALENDARIO_CPROC:**
Contém os dias úteis, feriados, e informações relacionadas ao calendário fiscal.
**Saída da Função**
Retorna WData_Pgto, que contém a data de vencimento calculada.




Grupo Imposto: É preenchido de acordo com a empresa, de acordo com a view ZFLUX_VW_UF_CD_RC_GP_IMP_CPROC,
UF Estabelecimento: É preenchido de acordo com a empresa e grupo_imposto, de acordo com a view ZFLUX_VW_UF_CD_RC_GP_IMP_CPROC,
Estabelecimento: É preenchido de acordo com a empresa, grupo_imposto e UF, de acordo com as view ZFLUX_VW_UF_CD_RC_GP_IMP_CPROC e FLUX_VW_ESTABELECIMENTO.

Views importantes:



**Fluxo principal**

O Cursor principal apenas le os três selects abaixo e grava as iformações no arquivo:
**Select 1**
**Tabelas:**
- ITEM_APURAC_CALC APU
- ZFLUX_VW_UF_CD_RC_GP_IMP_CPROC FLX
**Condições:**
COD_TIPO_LIVRO 	= '108'
COD_OPER_APUR  	= '013'
APU.VAL_APURACAO   > 0
GRUPO_IMPOSTO)  	= 'ICMS_NORMAL'
REGRA_IMPOSTO  	= 'REGRA_ICMS_NORMAL_1'

**Select 2**
**Tabelas:**
- ITEM_APURAC_CALC
- ZFLUX_VW_UF_CD_RC_GP_IMP_CPROC
- ITEM_APURAC_DISCR
**Condições:**

COD_TIPO_LIVRO 	= '108'
COD_OPER_APUR  	= '013'
VAL_APURACAO   	> 0
GRUPO_IMPOSTO)  	= 'ICMS_NORMAL'
Item COD_OPER_APUR  = '012'
VAL_ITEM_DISCRIM  	> 0
REGRA_IMPOSTO  	= 'REGRA_ICMS_NORMAL_2'

**Select 3**
**Tabelas:**
- ITEM_APURAC_CALC
- ZFLUX_VW_UF_CD_RC_GP_IMP_CPROC
- FLUX_HEINEKEN_ESTAB_TEMP_CPROC

**Condições:**

COD_TIPO_LIVRO 	= '108'
COD_OPER_APUR  	= '013'
VAL_APURACAO   	> 0
GRUPO_IMPOSTO  	= 'ICMS_NORMAL'
last_day(dT_PERIODO) = PERIODO
GRP_IMP                	= GRUPO_IMPOSTO
UF_FAVORECIDA 	= uf_estab,

**Fluxos**






---

| ZFLUX_VW_UF_CD_RC_GP_IMP_CPROC  COD_EMPRESA GRUPO_FISCAL COD_ESTAB UF COD_ARRECADACAO GRUPO_IMPOSTO TIPO_IMPOSTO COD_RECEITA DETALHE_RECEITA CONVENIO PRODUTO INF_COMPLEMENTAR DIA_VENCTO REGRA_VENCTO CRITERIO_VENCTO REGRA_IMPOSTO DESCR_REGRA_IMPOSTO | FLUX_VW_ESTABELECIMENTO  COD_EMPRESA COD_ESTAB RAZAO_SOCIAL NOME_FANTASIA UF COD | FLUX_HEINEKEN_ESTAB_TEMP_CPROC  ID_PROC EMPRESA ESTAB DT_PERIODO GRP_IMP TAX UF_ESTAB SAIDA |
| --- | --- | --- |


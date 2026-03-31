---
source: "MTZ-GUIAS DE PAGAMENTO_INTEGRAÇÃO_DOOTAX _EXECUTAR_ ICMS ANTECIPADO.docx"
category: Tax Payments
converted: auto
---





THOMSON REUTERS

Novo Módulo Integração Guias de Pagamento DOOTAX

















DOCUMENTO DE REQUISITO

Sumário

**1.	Objetivo	4**
2.	Introdução da função Executar	5
3.	Contexto Inicial da Função EXECUTAR	5
4.	Detalhamento da Função EXECUTAR	6
5.	Inserção de dados em tabelas temporárias	6
5.1. Dependências	6
6.	Procedure GERA_ICMS_NORMAL	7
7.1 Função Interna json	7
7.2 Declaração de Variáveis e Cursores	7
7.3 Processamento Principal	8
7.4. Regras Específicas	8
8. Função calcula_data_vencimento	8
8.1. Lógica de Cálculo	9
9. Fluxo Principal	9
9.1. Select 1	9
9.2. Select 2	10
9.3. Select 3	10
10. Campos Necessários para Requisição de Envio	11
10.1 De/PARA integração DOOTAX – Campos para Requisição de Envio:	11
11. Melhorias e Diferenciais na Jornada do Usuário	16
11.1. Controle de Versão	16
11.2. Segurança na Integração	16
11.3. Detalhamento de Requisições e Respostas	17
11.4. Monitoramento e Suporte	17
12. Conclusão	17






















# Objetivo

O novo módulo de “Guia de Pagamento” foi desenvolvido com base na estrutura de um processo customizado já existente “DOOTAX”. Essa estrutura será reaproveitada e integrada a outro menu dentro do Onesource Tax One e Onesource BR.

O reaproveitamento visa otimizar a implementação, mantendo a lógica de negócio previamente validada e adaptando-a às especificidades do menu onde será inserido. Essa abordagem visa reduzir esforços de implementação, garantir a consistência operacional e facilitar a manutenção futura, assegurando que o novo módulo atenda às necessidades específicas de processamento de Guias de Pagamento.

Deverá transformar a funcionalidade customizada em um módulo produtizável (Produtização = Preparado para comercialização), garantindo que não contenha dados ou referências específicas ao cliente original.

Todas as tabelas, procedures, views e outros objetos do banco de dados relacionados à funcionalidade deverão ser renomeados para evitar conflitos e manter a independência do novo módulo. Os dados existentes associados ao cliente original deverão ser descartados ou tratados para garantir que a nova função seja limpa e genérica. É necessário garantir que nenhuma referência explícita aos dados ou padrões do cliente original permaneça na implementação. Desta forma, é necessário ajustar todas as chamadas de procedures, tabelas e views para refletir os novos nomes, garantindo compatibilidade total com o novo módulo.










# Introdução da função Executar

A função EXECUTAR tem como objetivo principal processar guias de pagamento de impostos, registrando processos e manipulando informações fiscais. Esta documentação detalha sua estrutura, dependências e funcionamento.


# Contexto Inicial da Função EXECUTAR

A função recebe os seguintes parâmetros de entrada:


Dentro da função, é inicializado um identificador de processo (mproc_id), e um novo processo é criado no sistema por meio da biblioteca interna LIB_PROC.









# Detalhamento da Função EXECUTAR

A função EXECUTAR realiza as seguintes operações:

**Criação de um processo**
**Adição de logs**
**Recuperação de parâmetros**
**Validação de módulo e diretório**

Recupera valores do módulo para uso no processamento.
Valida se o módulo e o diretório existem, gerando logs de atenção quando não encontrados.


# Inserção de dados em tabelas temporárias

Insere dados de estabelecimentos na tabela temporária FLUX_HEINEKEN_ESTAB_TEMP_CPROC.


# 5.1. Dependências

A função depende das seguintes bibliotecas e tabelas:


# Procedure GERA_ICMS_ANTECIPADO

A procedure GERA_ICMS_ANTECIPADO tem como objetivo processar dados fiscais e estruturá-los no formato JSON ou armazená-los em tabelas específicas.

GERA_ICMS_ANTECIPADO
GRUPO_IMPOSTO: ICMS_ANTECIPADO
COD_OPER_APUR: 006
Filtragem: DSC_ITEM_APURACAO = Antecipação compra para comercialização


# 7.1 Função Interna json

Formata strings como campos JSON.
Parâmetros:
nome_campo: Nome do campo JSON.
valor: Valor do campo.
último: Indica se é o último campo (para evitar vírgulas).

# 7.2 Declaração de Variáveis e Cursores

Cursor geraJSON1: Consulta várias tabelas fiscais e retorna informações como:
Grupo de imposto, códigos de arrecadação e receita.
Período, código do estabelecimento.
Valores de apuração, vencimento e pagamento.
Regras tributárias e empresariais.









# 7.3 Processamento Principal

Itera sobre o cursor geraJSON1.
Valida e estrutura os dados para JSON ou tabela.
Insere registros processados em tabelas específicas.


# 7.4. Regras Específicas

Mapeamento de Parâmetros: Utiliza fpar_parametros e fpar_param_det.
Integração com Outras Procedures: Como calcula_data_vencimento.



# 8. Função calcula_data_vencimento

Calcula datas de vencimento baseadas em regras tributárias e empresariais.





# 8.1. Lógica de Cálculo

**Dia Útil (DU)**
Usa a tabela FLUX_VW_CALENDARIO_CPROC para identificar dias úteis.
**Data fixa (DF)**
Constrói uma data fixa com base nos parâmetros.
**Feriados (DA ou FA)**

Ajusta vencimentos considerando feriados municipais ou estaduais.












# 9. Fluxo Principal


PROCEDURE GERA_ICMS_ANTECIPADO(v_mcod_id         number,
v_cod_empresa     varchar2,
v_cod_estab       varchar2,
v_periodo         date,
v_grupo_imposto   varchar2,
v_uf              varchar2,
v_tipo_saida      varchar2) IS
FUNCTION json(nome_campo varchar2, valor varchar2, ultimo boolean default false) return varchar2 IS
v_retorno varchar2(200) := '';
BEGIN
IF ultimo THEN
v_retorno := '"'||nome_campo||'":"'||valor||'"';
ELSE
v_retorno := '"'||nome_campo||'":"'||valor||'",';
END IF;
return v_retorno;
END json;
BEGIN
DECLARE
vPalet_Count NUMBER := 0;
vCount NUMBER := 0;
v_arq NUMBER :=0;
v_grp VARCHAR2(30) := '';
cursor geraJSON3 is
SELECT GRUPO_IMPOSTO,
DECODE((SELECT TRIM(VALOR)
from fpar_parametros f,  fpar_param_det d
where nome_framework  = 'GP_DE_MSAF_PARA_SAP_CPAR'
AND f.id_parametros = d.id_parametro
AND NOME_PARAM      = 'DEPARA_EMPR'
AND TRIM(CONTEUDO)  = COD_EMPRESA),NULL,COD_EMPRESA,(SELECT TRIM(VALOR)
from fpar_parametros f,  fpar_param_det d
where nome_framework  = 'GP_DE_MSAF_PARA_SAP_CPAR'
AND f.id_parametros = d.id_parametro
AND NOME_PARAM      = 'DEPARA_EMPR'
AND TRIM(CONTEUDO)  = COD_EMPRESA))   COD_EMPRESA,
GRUPO_FISCAL,
DECODE((SELECT TRIM(VALOR)
from fpar_parametros f,  fpar_param_det d
where nome_framework    = 'GP_DE_MSAF_PARA_SAP_CPAR'
AND f.id_parametros   = d.id_parametro
AND NOME_PARAM        = 'DEPARA_ESTAB'
AND TRIM(CONTEUDO)    = COD_ESTAB
AND TRIM(D.DESCRICAO) = COD_EMPRESA),NULL,COD_ESTAB, (SELECT TRIM(VALOR)
from fpar_parametros f,  fpar_param_det d
where nome_framework    = 'GP_DE_MSAF_PARA_SAP_CPAR'
AND f.id_parametros   = d.id_parametro
AND NOME_PARAM        = 'DEPARA_ESTAB'
AND TRIM(CONTEUDO)    = COD_ESTAB
AND TRIM(D.DESCRICAO) = COD_EMPRESA)) COD_ESTAB,
PERIODO,
COD_ARRECADACAO,
COD_RECEITA,
NUM_DOC_ORIGEM,
SERIE,
CHAVE_NFE,
UF_FAVORECIDA,
v_tipo_saida P_TIPO_SAIDA,
CONVENIO,
DETALHAMENTO_RECEITA,
PRODUTO,
INF_COMPLEMENTAR,
VALOR_PRINCIPAL,
DATA_VENCIMENTO,
DATA_PAGAMENTO,
REGRA_IMPOSTO,
VALOR_FECP,
NULL CNPJ_FAVORECIDO,
NULL IE_FAVORECIDO,
0 VLR_MULTA,
0 VLR_JUROS,
0 VLR_FECP_MULTA,
0 VLR_FECP_JUROS,
NULL DATA_EMISSAO
FROM (
SELECT GRUPO_IMPOSTO,
COD_EMPRESA,
GRUPO_FISCAL,
COD_ESTAB,
PERIODO,
COD_ARRECADACAO,
COD_RECEITA,
NUM_DOC_ORIGEM,
SERIE,
CHAVE_NFE,
DATA_EMISSAO,
SUM(VALOR_PRINCIPAL) VALOR_PRINCIPAL,
MAX(DATA_VENCIMENTO) DATA_VENCIMENTO,
DATA_PAGAMENTO,
CONVENIO,
DETALHAMENTO_RECEITA,
PRODUTO,
INF_COMPLEMENTAR,
VALOR_FECP,
REGRA_IMPOSTO,
UF_FAVORECIDA
FROM (
SELECT
'ICMS_ANTECIPADO'                                         GRUPO_IMPOSTO,
APU.COD_EMPRESA                                           COD_EMPRESA,
REPLACE(FLX.GRUPO_FISCAL,'','')                           GRUPO_FISCAL,
APU.COD_ESTAB                                             COD_ESTAB,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')                     PERIODO,
FLX.COD_ARRECADACAO                                       COD_ARRECADACAO,
FLX.COD_RECEITA                                           COD_RECEITA,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')||FLX.COD_RECEITA||1 NUM_DOC_ORIGEM,
NULL                                                      SERIE,
NULL                                                      CHAVE_NFE,
NULL                                                      DATA_EMISSAO,
STD.COD_ESTADO                                            UF_FAVORECIDA,
apu.val_item_discrim                                      VALOR_PRINCIPAL,
TO_CHAR(GP_DT_GERA_GUIAS_CPROC.calcula_data_vencimento(FLX.REGRA_VENCTO,FLX.DIA_VENCTO,(TO_CHAR((APU.DAT_APURACAO +1),'MMYYYY')),EST.IDENT_ESTADO,EST.COD_MUNICIPIO),'YYYYMMDD') DATA_VENCIMENTO,
NULL                                                      DATA_PAGAMENTO,
FLX.CONVENIO                                              CONVENIO,
FLX.DETALHE_RECEITA                                       DETALHAMENTO_RECEITA,
FLX.PRODUTO                                               PRODUTO,
FLX.INF_COMPLEMENTAR                                      INF_COMPLEMENTAR,
null                                                      VALOR_FECP,
'REGRA_ICMS_ANTECIPADO_1'                                 REGRA_IMPOSTO
FROM ITEM_APURAC_DISCR APU, ZGP_VW_UF_CD_RC_GP_IMP_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD
WHERE APU.COD_TIPO_LIVRO = '108'
AND APU.COD_OPER_APUR  = '006'
--AND UPPER(APU.DSC_ITEM_APURACAO) LIKE UPPER('Antecipa  o compra para comercializa  o%')
AND UPPER(APU.DSC_ITEM_APURACAO) = UPPER('Antecipa  o compra para comercializa  o')
AND apu.val_item_discrim    > 0
AND APU.COD_EMPRESA    = FLX.cod_empresa
AND APU.COD_ESTAB      = FLX.cod_estab
AND UPPER(FLX.GRUPO_IMPOSTO)  = UPPER('ICMS_ANTECIPADO')
AND APU.COD_EMPRESA    = EST.COD_EMPRESA
AND APU.COD_ESTAB      = EST.COD_ESTAB
AND EST.IDENT_ESTADO   = STD.IDENT_ESTADO
AND STD.COD_ESTADO     = FLX.UF
AND FLX.REGRA_IMPOSTO  = 'REGRA_ICMS_ANTECIPADO_1')

GROUP BY GRUPO_IMPOSTO,
COD_EMPRESA,
GRUPO_FISCAL,
COD_ESTAB,
PERIODO,
UF_FAVORECIDA,
COD_ARRECADACAO,
COD_RECEITA,
NUM_DOC_ORIGEM,
SERIE,
CHAVE_NFE,
DATA_EMISSAO,
DATA_PAGAMENTO,
CONVENIO,
DETALHAMENTO_RECEITA,
PRODUTO,
INF_COMPLEMENTAR,
VALOR_FECP,
REGRA_IMPOSTO) J, GP_ESTAB_TEMP_CPROC TM
where TM.EMPRESA                             = J.COD_EMPRESA
and TM.ESTAB                               = J.COD_ESTAB
and J.COD_EMPRESA                          = MCOD_EMPRESA
and to_char(last_day(tm.dT_PERIODO), 'YYYYMMDD') = J.PERIODO
and upper(TRIM(TM.GRP_IMP))                = upper(J.GRUPO_IMPOSTO)
and J.UF_FAVORECIDA                LIKE DECODE(tm.uf_estab, 'TD', '%', tm.uf_estab)
and J.COD_EMPRESA   = v_cod_empresa
and tm.saida        = v_tipo_saida
and tm.id_proc      = v_mcod_id;
REG geraJSON3%rowtype;
v_arquivo sys.utl_file.file_type;
vs_arquivo          varchar2(32767);
mLinha              Varchar2(2000);
v_saida             varchar2(1);
BEGIN

loga('GERA_ICMS ANTECIPADO',FALSE);

FOR r_pallet IN geraJSON3 LOOP
vPalet_Count := geraJSON3%ROWCOUNT;
v_saida      := r_pallet.p_tipo_saida;
END LOOP;

loga('Qtde Registros:'||vPalet_Count,FALSE);

IF vPalet_Count = 0 then
lib_proc.add_log('SEM DADOS PARA GERACAO DO ARQUIVO NO PERIODO E GRUPO SELECIONADO',1);
lib_proc.add_log('PERIODO: '||TO_CHAR(v_periodo, 'MM/YYYY') ,1);
lib_proc.add_log('GRUPO DE IMPOSTO: '||v_grupo_imposto,1);
else
FOR REG in geraJSON3 loop
vCount := vCount+1;
If geraJSON3%ROWCOUNT = 1 Then
if reg.p_tipo_saida = 1 then
v_arquivo := SYS.utl_file.fopen(VS_DIRETORIO,mproc_id||'_DOOTAX_'|| REG.GRUPO_IMPOSTO||'_'||to_char(trunc(sysdate), 'YYYYMMDD') ||'.txt', 'W',32767);
SYS.utl_file.put_line(v_arquivo,('{"contas_a_pagar":[')||CHR(10));
SYS.utl_file.put_line(v_arquivo, ('{')||CHR(10));
vs_arquivo := '{';
elsif reg.p_tipo_saida = 2 then
LIB_PROC.ADD_TIPO(MPROC_ID, 1, mproc_id||'_'|| REG.GRUPO_IMPOSTO||'_'||to_char(trunc(sysdate), 'YYYYMMDD') ||'.txt', 2);
vs_arquivo := ('{"contas_a_pagar":[');
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
vs_arquivo := ('{');
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
end if;
lib_proc.add_log('  |Geracao arquivo JSON | NOME DO ARQUIVO: ''  |Geracao arquivo JSON | NOME DO ARQUIVO: '||mproc_id||'_'|| REG.GRUPO_IMPOSTO||'_'||to_char(trunc(sysdate), 'YYYYMMDD') ||'.txt   '||'DIRETORIO: '||VS_DIRETORIO   ,1);
lib_proc.add_log('{"contas_a_pagar":[',1);
lib_proc.add_log('{',1);
Else
if reg.p_tipo_saida = 1 then
SYS.utl_file.put_line(v_arquivo, ('{')||CHR(10));
vs_arquivo := ('{');

elsif reg.p_tipo_saida = 2 then
vs_arquivo := ('{');
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
end if;
lib_proc.add_log('{',1);
End If;
if reg.p_tipo_saida = 1 then
sys.utl_file.put_line(v_arquivo, (json('cod_empresa'    , reg.cod_empresa))||CHR(10));

sys.utl_file.put_line(v_arquivo, (json('cod_estab'      , reg.cod_estab))||CHR(10));

sys.utl_file.put_line(v_arquivo, (json('periodo'        , reg.periodo))||CHR(10));

sys.utl_file.put_line(v_arquivo, (json('cod_arrecadacao', reg.cod_arrecadacao))||CHR(10));

sys.utl_file.put_line(v_arquivo, (json('cod_receita'    , reg.cod_receita))||CHR(10));

sys.utl_file.put_line(v_arquivo, (json('uf_favorecida'  , reg.uf_favorecida))||CHR(10));
if reg.num_doc_origem is not null then
sys.utl_file.put_line(v_arquivo, (json('num_doc_origem' , reg.num_doc_origem))||CHR(10));
end if;
IF REG.SERIE IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('serie' , reg.serie))||CHR(10));
END IF;
IF REG.DETALHAMENTO_RECEITA IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('det_receita' , reg.detalhamento_receita))||CHR(10));
END IF;
IF REG.PRODUTO IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('cod_produto' , reg.produto))||CHR(10));
END IF;
IF REG.CONVENIO IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('convenio' , reg.convenio))||CHR(10));
END IF;
IF REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' then
sys.utl_file.put_line(v_arquivo, (json('vlr_principal' , replace(trim(to_char(reg.valor_principal,'999999990D99')),',','.'),true))||CHR(10));
ELSE
sys.utl_file.put_line(v_arquivo, (json('vlr_principal' , replace(trim(to_char(reg.valor_principal,'999999990D99')),',','.')))||CHR(10));
END IF;
IF REG.CHAVE_NFE IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('chave_dfe' , reg.chave_nfe))||CHR(10));
END IF;
-----
CASE WHEN REG.VALOR_FECP IS NOT NULL AND REG.VALOR_FECP > 0 THEN
CASE WHEN REG.INF_COMPLEMENTAR IS NOT NULL THEN
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , reg.data_vencimento))||CHR(10));
END CASE;
CASE WHEN REG.DATA_PAGAMENTO IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , reg.data_vencimento))||CHR(10));
ELSE NULL;
END CASE;
sys.utl_file.put_line(v_arquivo, (json('vlr_fecp' , replace(trim(to_char(reg.valor_fecp,'999999990D99')),',','.'),true))||CHR(10));
ELSE
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento))||CHR(10));
ELSE
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , reg.data_vencimento))||CHR(10));
END CASE;
CASE WHEN REG.DATA_PAGAMENTO IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('data_pagamento' , reg.data_pagamento))||CHR(10));
ELSE NULL;
END CASE;
sys.utl_file.put_line(v_arquivo, (json('vlr_fecp' , replace(trim(to_char(reg.valor_fecp,'999999990D99')),',','.')))||CHR(10));
sys.utl_file.put_line(v_arquivo, (json('inf_complementar' , to_char(reg.inf_complementar),true))||CHR(10));
END CASE;
ELSE
CASE WHEN REG.INF_COMPLEMENTAR IS NULL THEN
CASE WHEN REG.DATA_PAGAMENTO IS NULL THEN
IF REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , to_char(reg.data_vencimento),TRUE))||CHR(10));
END IF;
ELSE
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' then
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , to_char(reg.data_vencimento)))||CHR(10));
END CASE;
sys.utl_file.put_line(v_arquivo, (json('data_pagamento' , to_char(reg.data_pagamento),TRUE))||CHR(10));
END CASE;
ELSE
CASE WHEN REG.UF_FAVORECIDA = 'AM'  AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , to_char(reg.data_vencimento)))||CHR(10));
END CASE;
CASE WHEN REG.DATA_PAGAMENTO IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , to_char(reg.data_pagamento)))||CHR(10));
ELSE NULL;
END CASE;
sys.utl_file.put_line(v_arquivo, (json('inf_complementar' , to_char(reg.inf_complementar),TRUE))||CHR(10));
END CASE;
END CASE;
-- SERVIDOR LOCAL
elsif reg.p_tipo_saida = 2 then
vs_arquivo := (json('cod_empresa'    , reg.cod_empresa));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
vs_arquivo := (json('cod_estab'      , reg.cod_estab));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
IF REG.REGRA_IMPOSTO = 'REGRA_DIFAL_2' THEN
vs_arquivo := (json('periodo'        , reg.data_emissao));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
ELSE
vs_arquivo := (json('periodo'        , reg.periodo));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
vs_arquivo := (json('cod_arrecadacao', reg.cod_arrecadacao));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
vs_arquivo := (json('cod_receita'    , reg.cod_receita));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
vs_arquivo := (json('uf_favorecida'  , reg.uf_favorecida));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
if reg.num_doc_origem is not null then
vs_arquivo := (json('num_doc_origem' , reg.num_doc_origem));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
end if;
IF REG.SERIE IS NOT NULL THEN
vs_arquivo := (json('serie'  , reg.serie));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
IF REG.DETALHAMENTO_RECEITA IS NOT NULL THEN
vs_arquivo := (json('det_receita'  , reg.detalhamento_receita));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
IF REG.PRODUTO IS NOT NULL THEN
vs_arquivo := (json('cod_produto'  , reg.produto));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
IF REG.CONVENIO IS NOT NULL THEN
vs_arquivo := (json('convenio'  , reg.convenio));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
IF REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' then
vs_arquivo := (json('vlr_principal'  , replace(trim(to_char(reg.valor_principal,'999999990D99')),',','.'),true));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
ELSE
vs_arquivo := (json('vlr_principal'  , replace(trim(to_char(reg.valor_principal,'999999990D99')),',','.')));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
IF REG.CHAVE_NFE IS NOT NULL THEN
vs_arquivo := (json('chave_dfe'  , reg.chave_nfe));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
CASE WHEN REG.VALOR_FECP IS NOT NULL AND REG.VALOR_FECP > 0 THEN
CASE WHEN REG.INF_COMPLEMENTAR IS NOT NULL THEN
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_vencimento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
CASE WHEN REG.DATA_PAGAMENTO IS NOT NULL THEN
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_pagamento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
ELSE NULL;
END CASE;
vs_arquivo := (json('vlr_fecp'  , replace(trim(to_char(reg.valor_fecp,'999999990D99')),',','.'),true));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
ELSE
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_vencimento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
CASE WHEN REG.DATA_PAGAMENTO IS NOT NULL THEN
vs_arquivo := (json('data_pagamento'  , to_char(reg.data_pagamento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
ELSE NULL;
END CASE;
vs_arquivo := (json('vlr_fecp'  , replace(trim(to_char(reg.valor_fecp,'999999990D99')),',','.')));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
vs_arquivo := (json('inf_complementar'  , to_char(reg.inf_complementar),true));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
ELSE
CASE WHEN REG.INF_COMPLEMENTAR IS NULL THEN
CASE WHEN REG.DATA_PAGAMENTO IS NULL THEN
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_vencimento),TRUE));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
ELSE
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' then
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_vencimento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
vs_arquivo := (json('data_pagamento'  , to_char(reg.data_pagamento),TRUE));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
ELSE
CASE WHEN REG.UF_FAVORECIDA = 'AM'  AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_vencimento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
CASE WHEN REG.DATA_PAGAMENTO IS NOT NULL THEN
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_pagamento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
ELSE NULL;
END CASE;
vs_arquivo := (json('inf_complementar'  , to_char(reg.inf_complementar),TRUE));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
END CASE;
end if;
lib_proc.add_log(json('cod_empresa'    , reg.cod_empresa),1);
lib_proc.add_log(json('cod_estab'      , reg.cod_estab),1);
lib_proc.add_log(json('periodo'        , reg.periodo),1);
lib_proc.add_log(json('cod_arrecadacao', reg.cod_arrecadacao),1);
lib_proc.add_log(json('cod_receita'    , reg.cod_receita),1);
lib_proc.add_log(json('uf_favorecida'  , reg.uf_favorecida),1);
if reg.num_doc_origem is not null then
lib_proc.add_log(json('num_doc_origem' , reg.num_doc_origem),1);
end if;
if reg.serie is not null then
lib_proc.add_log(json('serie' , reg.serie),1);
end if;
if reg.data_vencimento is not null then
lib_proc.add_log(json('data_vencimento' , reg.data_vencimento),1);
end if;
if reg.data_pagamento is not null then
lib_proc.add_log(json('data_pagamento' , reg.data_pagamento),1);
end if;
if reg.convenio is not null then
lib_proc.add_log(json('convenio' , reg.convenio),1);
end if;
if reg.produto is not null then
lib_proc.add_log(json('produto' , reg.produto),1);
end if;
if reg.detalhamento_receita is not null then
lib_proc.add_log(json('det_receita' , reg.detalhamento_receita),1);
end if;
if reg.inf_complementar is not null then
lib_proc.add_log(json('inf_complementar' , reg.inf_complementar),1);
end if;
if reg.chave_nfe is null then
if reg.valor_fecp is not null then
lib_proc.add_log(json('vlr_principal'  , reg.valor_principal),1);
lib_proc.add_log(json('valor_fecp' , reg.valor_fecp,true),1);
else
lib_proc.add_log(json('vlr_principal'  , reg.valor_principal,true),1);
end if;
else
if reg.valor_fecp is not null then
lib_proc.add_log(json('vlr_principal'  , reg.valor_principal),1);
lib_proc.add_log(json('valor_fecp' , reg.valor_fecp),1);
else
lib_proc.add_log(json('vlr_principal'  , reg.valor_principal,true),1);
end if;
lib_proc.add_log(json('vlr_principal'  , reg.valor_principal),1);
lib_proc.add_log(json('chave_dfe' , reg.chave_nfe,true),1);
end if;
if reg.p_tipo_saida = 1 then
--Se houver mais de 1 bloco no json insere virgula ao final do bloco, exceto no ultimo registro.
if vCount < vPalet_Count then
sys.utl_file.put_line(v_arquivo, ('},'));
else
sys.utl_file.put_line(v_arquivo, ('}'));
end if;
elsif reg.p_tipo_saida = 2 then
--Se houver mais de 1 bloco no json insere virgula ao final do bloco, exceto no ultimo registro.
if vCount < vPalet_Count then
vs_arquivo := ('},');
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
lib_proc.add_log('},',1);
else
vs_arquivo := ('}');
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
lib_proc.add_log('}',1);
end if;
end if;
insert into GP_LOGS_JSON_DT_CPROC  values (mproc_id,
musuario,
TO_CHAR(SYSDATE, 'DD/MM/YYYY HH24:MI:SS'),
reg.cod_empresa,
reg.cod_estab,
reg.periodo,
reg.grupo_imposto,
reg.cod_arrecadacao,
reg.cod_receita,
reg.uf_favorecida,
reg.num_doc_origem,
reg.serie,
reg.chave_nfe,
reg.valor_principal,
reg.valor_fecp,
reg.data_vencimento,
reg.data_pagamento,
reg.inf_complementar,
reg.detalhamento_receita,
reg.convenio,
reg.produto);
--commit;
end loop;

if v_saida = 1 then
sys.utl_file.put_line(v_arquivo, (']}'||CHR(13)));
elsif v_saida = 2 then
vs_arquivo := (']}');
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
end if;
lib_proc.add_log(']}',1);
sys.utl_file.fclose(v_arquivo);
end if;
delete from GP_ESTAB_TEMP_CPROC where id_proc = mproc_id;
COMMIT;
END;
END GERA_ICMS_ANTECIPADO;
PROCEDURE GERA_ICMS_INCENTIVADO(v_mcod_id         number,
v_cod_empresa     varchar2,
v_cod_estab       varchar2,
v_periodo         date,
v_grupo_imposto   varchar2,
v_uf              varchar2,
v_tipo_saida      varchar2) IS
FUNCTION json(nome_campo varchar2, valor varchar2, ultimo boolean default false) return varchar2 IS
v_retorno varchar2(200) := '';
BEGIN
IF ultimo THEN
v_retorno := '"'||nome_campo||'":"'||valor||'"';
ELSE
v_retorno := '"'||nome_campo||'":"'||valor||'",';
END IF;
return v_retorno;
END json;
BEGIN
DECLARE
vPalet_Count NUMBER := 0;
vCount NUMBER := 0;
v_arq NUMBER :=0;
v_grp VARCHAR2(30) := '';
cursor geraJSON4 is
SELECT GRUPO_IMPOSTO,
DECODE((SELECT TRIM(VALOR)
from fpar_parametros f,  fpar_param_det d
where nome_framework  = 'GP_DE_MSAF_PARA_SAP_CPAR'
AND f.id_parametros = d.id_parametro
AND NOME_PARAM      = 'DEPARA_EMPR'
AND TRIM(CONTEUDO)  = COD_EMPRESA),NULL,COD_EMPRESA,(SELECT TRIM(VALOR)
from fpar_parametros f,  fpar_param_det d
where nome_framework  = 'GP_DE_MSAF_PARA_SAP_CPAR'
AND f.id_parametros = d.id_parametro
AND NOME_PARAM      = 'DEPARA_EMPR'
AND TRIM(CONTEUDO)  = COD_EMPRESA))   COD_EMPRESA,
GRUPO_FISCAL,
DECODE((SELECT TRIM(VALOR)
from fpar_parametros f,  fpar_param_det d
where nome_framework    = 'GP_DE_MSAF_PARA_SAP_CPAR'
AND f.id_parametros   = d.id_parametro
AND NOME_PARAM        = 'DEPARA_ESTAB'
AND TRIM(CONTEUDO)    = COD_ESTAB
AND TRIM(D.DESCRICAO) = COD_EMPRESA),NULL,COD_ESTAB, (SELECT TRIM(VALOR)
from fpar_parametros f,  fpar_param_det d
where nome_framework    = 'GP_DE_MSAF_PARA_SAP_CPAR'
AND f.id_parametros   = d.id_parametro
AND NOME_PARAM        = 'DEPARA_ESTAB'
AND TRIM(CONTEUDO)    = COD_ESTAB
AND TRIM(D.DESCRICAO) = COD_EMPRESA)) COD_ESTAB,
PERIODO,
COD_ARRECADACAO,
COD_RECEITA,
NUM_DOC_ORIGEM,
SERIE,
CHAVE_NFE,
UF_FAVORECIDA,
v_tipo_saida P_TIPO_SAIDA,
CONVENIO,
DETALHAMENTO_RECEITA,
PRODUTO,
INF_COMPLEMENTAR,
VALOR_PRINCIPAL,
DATA_VENCIMENTO,
DATA_PAGAMENTO,
REGRA_IMPOSTO,
VALOR_FECP,
NULL CNPJ_FAVORECIDO,
NULL IE_FAVORECIDO,
0 VLR_MULTA,
0 VLR_JUROS,
0 VLR_FECP_MULTA,
0 VLR_FECP_JUROS,
NULL DATA_EMISSAO
FROM (
SELECT GRUPO_IMPOSTO,
COD_EMPRESA,
GRUPO_FISCAL,
COD_ESTAB,
PERIODO,
COD_ARRECADACAO,
COD_RECEITA,
NUM_DOC_ORIGEM,
SERIE,
CHAVE_NFE,
DATA_EMISSAO,
UF_FAVORECIDA,
SUM(VALOR_PRINCIPAL) VALOR_PRINCIPAL,
MAX(DATA_VENCIMENTO) DATA_VENCIMENTO,
DATA_PAGAMENTO,
CONVENIO,
DETALHAMENTO_RECEITA,
PRODUTO,
INF_COMPLEMENTAR,
VALOR_FECP,
REGRA_IMPOSTO
FROM (
SELECT
'ICMS_INCENTIVADO'                                        GRUPO_IMPOSTO,
APU.COD_EMPRESA                                           COD_EMPRESA,
REPLACE(FLX.GRUPO_FISCAL,'','')                           GRUPO_FISCAL,
APU.COD_ESTAB                                             COD_ESTAB,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')                     PERIODO,
FLX.COD_ARRECADACAO                                       COD_ARRECADACAO,
FLX.COD_RECEITA                                           COD_RECEITA,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')||FLX.COD_RECEITA||1 NUM_DOC_ORIGEM,
NULL                                                      SERIE,
NULL                                                      CHAVE_NFE,
NULL                                                      DATA_EMISSAO,
STD.COD_ESTADO                                            UF_FAVORECIDA,
ROUND((apu.val_item_discrim * 0.1),2)                     VALOR_PRINCIPAL,
TO_CHAR(GP_DT_GERA_GUIAS_CPROC.calcula_data_vencimento(FLX.REGRA_VENCTO,FLX.DIA_VENCTO,(TO_CHAR((APU.DAT_APURACAO +1),'MMYYYY')),EST.IDENT_ESTADO,EST.COD_MUNICIPIO),'YYYYMMDD') DATA_VENCIMENTO,
NULL                                                      DATA_PAGAMENTO,
FLX.CONVENIO                                              CONVENIO,
FLX.DETALHE_RECEITA                                       DETALHAMENTO_RECEITA,
FLX.PRODUTO                                               PRODUTO,
FLX.INF_COMPLEMENTAR                                      INF_COMPLEMENTAR,
null                                                      VALOR_FECP,
'REGRA_ICMS_INCENTIVADO_1'                                 REGRA_IMPOSTO
FROM ITEM_APURAC_DISCR APU, ZGP_VW_UF_CD_RC_GP_IMP_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD
WHERE APU.COD_TIPO_LIVRO = '108'
AND APU.COD_OPER_APUR  = '012'
AND apu.val_item_discrim    > 0
AND APU.COD_EMPRESA    = FLX.cod_empresa
AND APU.COD_ESTAB      = FLX.cod_estab
AND UPPER(FLX.GRUPO_IMPOSTO)  = UPPER('ICMS_INCENTIVADO')
AND APU.COD_EMPRESA    = EST.COD_EMPRESA
AND APU.COD_ESTAB      = EST.COD_ESTAB
AND EST.IDENT_ESTADO   = STD.IDENT_ESTADO
AND STD.COD_ESTADO     = FLX.UF
--AND UPPER(APU.DSC_ITEM_APURACAO) LIKE '%VLR_ADIC_INCENT%'
AND UPPER(APU.DSC_ITEM_APURACAO) LIKE 'VLR_ADIC_INCENT'
AND FLX.REGRA_IMPOSTO  = 'REGRA_ICMS_INCENTIVADO_1')

GROUP BY GRUPO_IMPOSTO,
COD_EMPRESA,
GRUPO_FISCAL,
COD_ESTAB,
PERIODO,
COD_ARRECADACAO,
COD_RECEITA,
NUM_DOC_ORIGEM,
SERIE,
CHAVE_NFE,
UF_FAVORECIDA,
DATA_EMISSAO,
DATA_PAGAMENTO,
CONVENIO,
DETALHAMENTO_RECEITA,
PRODUTO,
INF_COMPLEMENTAR,
VALOR_FECP,
REGRA_IMPOSTO
UNION
SELECT GRUPO_IMPOSTO,
COD_EMPRESA,
GRUPO_FISCAL,
COD_ESTAB,
PERIODO,
COD_ARRECADACAO,
COD_RECEITA,
NUM_DOC_ORIGEM,
SERIE,
CHAVE_NFE,
DATA_EMISSAO,
uf_favorecida,
SUM(VALOR_PRINCIPAL) VALOR_PRINCIPAL,
MAX(DATA_VENCIMENTO) DATA_VENCIMENTO,
DATA_PAGAMENTO,
CONVENIO,
DETALHAMENTO_RECEITA,
PRODUTO,
INF_COMPLEMENTAR,
VALOR_FECP,
REGRA_IMPOSTO
FROM (
SELECT
'ICMS_INCENTIVADO'                                        GRUPO_IMPOSTO,
APU.COD_EMPRESA                                           COD_EMPRESA,
REPLACE(FLX.GRUPO_FISCAL,'','')                           GRUPO_FISCAL,
APU.COD_ESTAB                                             COD_ESTAB,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')                     PERIODO,
FLX.COD_ARRECADACAO                                       COD_ARRECADACAO,
FLX.COD_RECEITA                                           COD_RECEITA,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')||FLX.COD_RECEITA||1 NUM_DOC_ORIGEM,
NULL                                                      SERIE,
NULL                                                      CHAVE_NFE,
NULL                                                      DATA_EMISSAO,
STD.COD_ESTADO                                            UF_FAVORECIDA,
ROUND((apu.val_item_discrim  * 0.05),2)                   VALOR_PRINCIPAL,
TO_CHAR(GP_DT_GERA_GUIAS_CPROC.calcula_data_vencimento(FLX.REGRA_VENCTO,FLX.DIA_VENCTO,(TO_CHAR((APU.DAT_APURACAO +1),'MMYYYY')),EST.IDENT_ESTADO,EST.COD_MUNICIPIO),'YYYYMMDD') DATA_VENCIMENTO,
NULL                                                      DATA_PAGAMENTO,
FLX.CONVENIO                                              CONVENIO,
FLX.DETALHE_RECEITA                                       DETALHAMENTO_RECEITA,
FLX.PRODUTO                                               PRODUTO,
FLX.INF_COMPLEMENTAR                                      INF_COMPLEMENTAR,
null                                                      VALOR_FECP,
'REGRA_ICMS_INCENTIVADO_2'                                 REGRA_IMPOSTO
FROM ITEM_APURAC_DISCR APU, ZGP_VW_UF_CD_RC_GP_IMP_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD
WHERE APU.COD_TIPO_LIVRO = '108'
AND APU.COD_OPER_APUR  = '012'
AND apu.val_item_discrim    > 0
AND APU.COD_EMPRESA    = FLX.cod_empresa
AND APU.COD_ESTAB      = FLX.cod_estab
AND UPPER(FLX.GRUPO_IMPOSTO)  = UPPER('ICMS_INCENTIVADO')
AND APU.COD_EMPRESA    = EST.COD_EMPRESA
AND APU.COD_ESTAB      = EST.COD_ESTAB
AND EST.IDENT_ESTADO   = STD.IDENT_ESTADO
AND STD.COD_ESTADO     = FLX.UF
--AND UPPER(APU.DSC_ITEM_APURACAO) LIKE '%VLR_PRO_MARANHAO%'
AND UPPER(APU.DSC_ITEM_APURACAO) = 'VLR_PRO_MARANHAO'
AND FLX.REGRA_IMPOSTO  = 'REGRA_ICMS_INCENTIVADO_2')

GROUP BY GRUPO_IMPOSTO,
COD_EMPRESA,
GRUPO_FISCAL,
COD_ESTAB,
PERIODO,
COD_ARRECADACAO,
COD_RECEITA,
NUM_DOC_ORIGEM,
SERIE,
CHAVE_NFE,
UF_FAVORECIDA,
DATA_EMISSAO,
DATA_PAGAMENTO,
CONVENIO,
DETALHAMENTO_RECEITA,
PRODUTO,
INF_COMPLEMENTAR,
VALOR_FECP,
REGRA_IMPOSTO
) J, GP_ESTAB_TEMP_CPROC TM
where TM.EMPRESA                             = J.COD_EMPRESA
and TM.ESTAB                               = J.COD_ESTAB
and J.COD_EMPRESA                          = MCOD_EMPRESA
and to_char(last_day(tm.dT_PERIODO), 'YYYYMMDD') = J.PERIODO
and upper(TRIM(TM.GRP_IMP))                = upper(J.GRUPO_IMPOSTO)
and J.UF_FAVORECIDA                LIKE DECODE(tm.uf_estab, 'TD', '%', tm.uf_estab)
and J.COD_EMPRESA   = v_cod_empresa
and tm.saida        = v_tipo_saida
and tm.id_proc      = v_mcod_id;
REG geraJSON4%rowtype;
v_arquivo sys.utl_file.file_type;
vs_arquivo          varchar2(32767);
mLinha              Varchar2(2000);
v_saida             varchar2(1);
BEGIN

loga('GERA_ICMS_INCENTIVADO',FALSE);

FOR r_pallet IN geraJSON4 LOOP
vPalet_Count := geraJSON4%ROWCOUNT;
v_saida      := r_pallet.p_tipo_saida;
END LOOP;

loga('Qtde Registros:'||vPalet_Count,FALSE);

IF vPalet_Count = 0 then
lib_proc.add_log('SEM DADOS PARA GERACAO DO ARQUIVO NO PERIODO E GRUPO SELECIONADO',1);
lib_proc.add_log('PERIODO: '||TO_CHAR(v_periodo, 'MM/YYYY') ,1);
lib_proc.add_log('GRUPO DE IMPOSTO: '||v_grupo_imposto,1);
else
FOR REG in geraJSON4 loop
vCount := vCount+1;
If geraJSON4%ROWCOUNT = 1 Then
if reg.p_tipo_saida = 1 then
v_arquivo := SYS.utl_file.fopen(VS_DIRETORIO,mproc_id||'_DOOTAX_'|| REG.GRUPO_IMPOSTO||'_'||to_char(trunc(sysdate), 'YYYYMMDD') ||'.txt', 'W',32767);
SYS.utl_file.put_line(v_arquivo,('{"contas_a_pagar":[')||CHR(10));
SYS.utl_file.put_line(v_arquivo, ('{')||CHR(10));
vs_arquivo := '{';
elsif reg.p_tipo_saida = 2 then
LIB_PROC.ADD_TIPO(MPROC_ID, 1, mproc_id||'_'|| REG.GRUPO_IMPOSTO||'_'||to_char(trunc(sysdate), 'YYYYMMDD') ||'.txt', 2);
vs_arquivo := ('{"contas_a_pagar":[');
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
vs_arquivo := ('{');
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
end if;
lib_proc.add_log('  |Geracao arquivo JSON | NOME DO ARQUIVO: ''  |Geracao arquivo JSON | NOME DO ARQUIVO: '||mproc_id||'_'|| REG.GRUPO_IMPOSTO||'_'||to_char(trunc(sysdate), 'YYYYMMDD') ||'.txt   '||'DIRETORIO: '||VS_DIRETORIO   ,1);
lib_proc.add_log('{"contas_a_pagar":[',1);
lib_proc.add_log('{',1);
Else
if reg.p_tipo_saida = 1 then
SYS.utl_file.put_line(v_arquivo, ('{')||CHR(10));
vs_arquivo := ('{');

elsif reg.p_tipo_saida = 2 then
vs_arquivo := ('{');
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
end if;
lib_proc.add_log('{',1);
End If;
if reg.p_tipo_saida = 1 then
sys.utl_file.put_line(v_arquivo, (json('cod_empresa'    , reg.cod_empresa))||CHR(10));

sys.utl_file.put_line(v_arquivo, (json('cod_estab'      , reg.cod_estab))||CHR(10));

sys.utl_file.put_line(v_arquivo, (json('periodo'        , reg.periodo))||CHR(10));

sys.utl_file.put_line(v_arquivo, (json('cod_arrecadacao', reg.cod_arrecadacao))||CHR(10));

sys.utl_file.put_line(v_arquivo, (json('cod_receita'    , reg.cod_receita))||CHR(10));

sys.utl_file.put_line(v_arquivo, (json('uf_favorecida'  , reg.uf_favorecida))||CHR(10));
if reg.num_doc_origem is not null then
sys.utl_file.put_line(v_arquivo, (json('num_doc_origem' , reg.num_doc_origem))||CHR(10));
end if;
IF REG.SERIE IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('serie' , reg.serie))||CHR(10));
END IF;
IF REG.DETALHAMENTO_RECEITA IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('det_receita' , reg.detalhamento_receita))||CHR(10));
END IF;
IF REG.PRODUTO IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('cod_produto' , reg.produto))||CHR(10));
END IF;
IF REG.CONVENIO IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('convenio' , reg.convenio))||CHR(10));
END IF;
IF REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' then
sys.utl_file.put_line(v_arquivo, (json('vlr_principal' , replace(trim(to_char(reg.valor_principal,'999999990D99')),',','.'),true))||CHR(10));
ELSE
sys.utl_file.put_line(v_arquivo, (json('vlr_principal' , replace(trim(to_char(reg.valor_principal,'999999990D99')),',','.')))||CHR(10));
END IF;
IF REG.CHAVE_NFE IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('chave_dfe' , reg.chave_nfe))||CHR(10));
END IF;
-----
CASE WHEN REG.VALOR_FECP IS NOT NULL AND REG.VALOR_FECP > 0 THEN
CASE WHEN REG.INF_COMPLEMENTAR IS NOT NULL THEN
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , reg.data_vencimento))||CHR(10));
END CASE;
CASE WHEN REG.DATA_PAGAMENTO IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , reg.data_vencimento))||CHR(10));
ELSE NULL;
END CASE;
sys.utl_file.put_line(v_arquivo, (json('vlr_fecp' , replace(trim(to_char(reg.valor_fecp,'999999990D99')),',','.'),true))||CHR(10));
ELSE
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento))||CHR(10));
ELSE
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , reg.data_vencimento))||CHR(10));
END CASE;
CASE WHEN REG.DATA_PAGAMENTO IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('data_pagamento' , reg.data_pagamento))||CHR(10));
ELSE NULL;
END CASE;
sys.utl_file.put_line(v_arquivo, (json('vlr_fecp' , replace(trim(to_char(reg.valor_fecp,'999999990D99')),',','.')))||CHR(10));
sys.utl_file.put_line(v_arquivo, (json('inf_complementar' , to_char(reg.inf_complementar),true))||CHR(10));
END CASE;
ELSE
CASE WHEN REG.INF_COMPLEMENTAR IS NULL THEN
CASE WHEN REG.DATA_PAGAMENTO IS NULL THEN
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , to_char(reg.data_vencimento),TRUE))||CHR(10));
END CASE;
ELSE
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' then
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , to_char(reg.data_vencimento)))||CHR(10));
END CASE;
sys.utl_file.put_line(v_arquivo, (json('data_pagamento' , to_char(reg.data_pagamento),TRUE))||CHR(10));
END CASE;
ELSE
CASE WHEN REG.UF_FAVORECIDA = 'AM'  AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , to_char(reg.data_vencimento)))||CHR(10));
END CASE;
CASE WHEN REG.DATA_PAGAMENTO IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , to_char(reg.data_pagamento)))||CHR(10));
ELSE NULL;
END CASE;
sys.utl_file.put_line(v_arquivo, (json('inf_complementar' , to_char(reg.inf_complementar),TRUE))||CHR(10));
END CASE;
END CASE;
-- SERVIDOR LOCAL
elsif reg.p_tipo_saida = 2 then
vs_arquivo := (json('cod_empresa'    , reg.cod_empresa));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
vs_arquivo := (json('cod_estab'      , reg.cod_estab));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
IF REG.REGRA_IMPOSTO = 'REGRA_DIFAL_2' THEN
vs_arquivo := (json('periodo'        , reg.data_emissao));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
ELSE
vs_arquivo := (json('periodo'        , reg.periodo));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
vs_arquivo := (json('cod_arrecadacao', reg.cod_arrecadacao));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
vs_arquivo := (json('cod_receita'    , reg.cod_receita));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
vs_arquivo := (json('uf_favorecida'  , reg.uf_favorecida));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
if reg.num_doc_origem is not null then
vs_arquivo := (json('num_doc_origem' , reg.num_doc_origem));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
end if;
IF REG.SERIE IS NOT NULL THEN
vs_arquivo := (json('serie'  , reg.serie));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
IF REG.DETALHAMENTO_RECEITA IS NOT NULL THEN
vs_arquivo := (json('det_receita'  , reg.detalhamento_receita));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
IF REG.PRODUTO IS NOT NULL THEN
vs_arquivo := (json('cod_produto'  , reg.produto));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
IF REG.CONVENIO IS NOT NULL THEN
vs_arquivo := (json('convenio'  , reg.convenio));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
IF REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' then
vs_arquivo := (json('vlr_principal'  , replace(trim(to_char(reg.valor_principal,'999999990D99')),',','.'),true));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
ELSE
vs_arquivo := (json('vlr_principal'  , replace(trim(to_char(reg.valor_principal,'999999990D99')),',','.')));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
IF REG.CHAVE_NFE IS NOT NULL THEN
vs_arquivo := (json('chave_dfe'  , reg.chave_nfe));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
CASE WHEN REG.VALOR_FECP IS NOT NULL AND REG.VALOR_FECP > 0 THEN
CASE WHEN REG.INF_COMPLEMENTAR IS NOT NULL THEN
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_vencimento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
CASE WHEN REG.DATA_PAGAMENTO IS NOT NULL THEN
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_pagamento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
ELSE NULL;
END CASE;
vs_arquivo := (json('vlr_fecp'  , replace(trim(to_char(reg.valor_fecp,'999999990D99')),',','.'),true));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
ELSE
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_vencimento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
CASE WHEN REG.DATA_PAGAMENTO IS NOT NULL THEN
vs_arquivo := (json('data_pagamento'  , to_char(reg.data_pagamento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
ELSE NULL;
END CASE;
vs_arquivo := (json('vlr_fecp'  , replace(trim(to_char(reg.valor_fecp,'999999990D99')),',','.')));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
vs_arquivo := (json('inf_complementar'  , to_char(reg.inf_complementar),true));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
ELSE
CASE WHEN REG.INF_COMPLEMENTAR IS NULL THEN
CASE WHEN REG.DATA_PAGAMENTO IS NULL THEN
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_vencimento),TRUE));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
ELSE
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' then
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_vencimento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
vs_arquivo := (json('data_pagamento'  , to_char(reg.data_pagamento),TRUE));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
ELSE
CASE WHEN REG.UF_FAVORECIDA = 'AM'  AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_vencimento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
CASE WHEN REG.DATA_PAGAMENTO IS NOT NULL THEN
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_pagamento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
ELSE NULL;
END CASE;
vs_arquivo := (json('inf_complementar'  , to_char(reg.inf_complementar),TRUE));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
END CASE;
end if;
lib_proc.add_log(json('cod_empresa'    , reg.cod_empresa),1);
lib_proc.add_log(json('cod_estab'      , reg.cod_estab),1);
lib_proc.add_log(json('periodo'        , reg.periodo),1);
lib_proc.add_log(json('cod_arrecadacao', reg.cod_arrecadacao),1);
lib_proc.add_log(json('cod_receita'    , reg.cod_receita),1);
lib_proc.add_log(json('uf_favorecida'  , reg.uf_favorecida),1);
if reg.num_doc_origem is not null then
lib_proc.add_log(json('num_doc_origem' , reg.num_doc_origem),1);
end if;
if reg.serie is not null then
lib_proc.add_log(json('serie' , reg.serie),1);
end if;
if reg.data_vencimento is not null then
lib_proc.add_log(json('data_vencimento' , reg.data_vencimento),1);
end if;
if reg.data_pagamento is not null then
lib_proc.add_log(json('data_pagamento' , reg.data_pagamento),1);
end if;
if reg.convenio is not null then
lib_proc.add_log(json('convenio' , reg.convenio),1);
end if;
if reg.produto is not null then
lib_proc.add_log(json('produto' , reg.produto),1);
end if;
if reg.detalhamento_receita is not null then
lib_proc.add_log(json('det_receita' , reg.detalhamento_receita),1);
end if;
if reg.inf_complementar is not null then
lib_proc.add_log(json('inf_complementar' , reg.inf_complementar),1);
end if;
if reg.chave_nfe is null then
if reg.valor_fecp is not null then
lib_proc.add_log(json('vlr_principal'  , reg.valor_principal),1);
lib_proc.add_log(json('valor_fecp' , reg.valor_fecp,true),1);
else
lib_proc.add_log(json('vlr_principal'  , reg.valor_principal,true),1);
end if;
else
if reg.valor_fecp is not null then
lib_proc.add_log(json('vlr_principal'  , reg.valor_principal),1);
lib_proc.add_log(json('valor_fecp' , reg.valor_fecp),1);
else
lib_proc.add_log(json('vlr_principal'  , reg.valor_principal,true),1);
end if;
lib_proc.add_log(json('vlr_principal'  , reg.valor_principal),1);
lib_proc.add_log(json('chave_dfe' , reg.chave_nfe,true),1);
end if;
if reg.p_tipo_saida = 1 then
--Se houver mais de 1 bloco no json insere virgula ao final do bloco, exceto no ultimo registro.
if vCount < vPalet_Count then
sys.utl_file.put_line(v_arquivo, ('},'));
else
sys.utl_file.put_line(v_arquivo, ('}'));
end if;
elsif reg.p_tipo_saida = 2 then
--Se houver mais de 1 bloco no json insere virgula ao final do bloco, exceto no ultimo registro.
if vCount < vPalet_Count then
vs_arquivo := ('},');
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
lib_proc.add_log('},',1);
else
vs_arquivo := ('}');
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
lib_proc.add_log('}',1);
end if;
end if;
insert into GP_LOGS_JSON_DT_CPROC  values (mproc_id,
musuario,
TO_CHAR(SYSDATE, 'DD/MM/YYYY HH24:MI:SS'),
reg.cod_empresa,
reg.cod_estab,
reg.periodo,
reg.grupo_imposto,
reg.cod_arrecadacao,
reg.cod_receita,
reg.uf_favorecida,
reg.num_doc_origem,
reg.serie,
reg.chave_nfe,
reg.valor_principal,
reg.valor_fecp,
reg.data_vencimento,
reg.data_pagamento,
reg.inf_complementar,
reg.detalhamento_receita,
reg.convenio,
reg.produto);
--commit;
end loop;


if v_saida = 1 then
sys.utl_file.put_line(v_arquivo, (']}'||CHR(13)));
elsif v_saida = 2 then
vs_arquivo := (']}');
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
end if;
lib_proc.add_log(']}',1);
sys.utl_file.fclose(v_arquivo);
end if;
delete from GP_ESTAB_TEMP_CPROC where id_proc = mproc_id;
COMMIT;
END;
END GERA_ICMS_INCENTIVADO;
PROCEDURE GERA_FUNDO_ICMS_NORMAL(v_mcod_id         number,
v_cod_empresa     varchar2,
v_cod_estab       varchar2,
v_periodo         date,
v_grupo_imposto   varchar2,
v_uf              varchar2,
v_tipo_saida      varchar2) IS
FUNCTION json(nome_campo varchar2, valor varchar2, ultimo boolean default false) return varchar2 IS
v_retorno varchar2(200) := '';
BEGIN
IF ultimo THEN
v_retorno := '"'||nome_campo||'":"'||valor||'"';
ELSE
v_retorno := '"'||nome_campo||'":"'||valor||'",';
END IF;
return v_retorno;
END json;
BEGIN
DECLARE
vPalet_Count NUMBER := 0;
vCount NUMBER := 0;
v_arq NUMBER :=0;
v_grp VARCHAR2(30) := '';

cursor geraJSON5 is
SELECT GRUPO_IMPOSTO,
DECODE((SELECT TRIM(VALOR)
from fpar_parametros f,  fpar_param_det d
where nome_framework  = 'GP_DE_MSAF_PARA_SAP_CPAR'
AND f.id_parametros = d.id_parametro
AND NOME_PARAM      = 'DEPARA_EMPR'
AND TRIM(CONTEUDO)  = COD_EMPRESA),NULL,COD_EMPRESA,(SELECT TRIM(VALOR)
from fpar_parametros f,  fpar_param_det d
where nome_framework  = 'GP_DE_MSAF_PARA_SAP_CPAR'
AND f.id_parametros = d.id_parametro
AND NOME_PARAM      = 'DEPARA_EMPR'
AND TRIM(CONTEUDO)  = COD_EMPRESA))   COD_EMPRESA,
GRUPO_FISCAL,
DECODE((SELECT TRIM(VALOR)
from fpar_parametros f,  fpar_param_det d
where nome_framework    = 'GP_DE_MSAF_PARA_SAP_CPAR'
AND f.id_parametros   = d.id_parametro
AND NOME_PARAM        = 'DEPARA_ESTAB'
AND TRIM(CONTEUDO)    = COD_ESTAB
AND TRIM(D.DESCRICAO) = COD_EMPRESA),NULL,COD_ESTAB, (SELECT TRIM(VALOR)
from fpar_parametros f,  fpar_param_det d
where nome_framework    = 'GP_DE_MSAF_PARA_SAP_CPAR'
AND f.id_parametros   = d.id_parametro
AND NOME_PARAM        = 'DEPARA_ESTAB'
AND TRIM(CONTEUDO)    = COD_ESTAB
AND TRIM(D.DESCRICAO) = COD_EMPRESA)) COD_ESTAB,
PERIODO,
COD_ARRECADACAO,
COD_RECEITA,
NUM_DOC_ORIGEM,
SERIE,
CHAVE_NFE,
UF_FAVORECIDA,
v_tipo_saida P_TIPO_SAIDA,
CONVENIO,
DETALHAMENTO_RECEITA,
PRODUTO,
INF_COMPLEMENTAR,
VALOR_PRINCIPAL,
DATA_VENCIMENTO,
DATA_PAGAMENTO,
REGRA_IMPOSTO,
VALOR_FECP,
NULL CNPJ_FAVORECIDO,
NULL IE_FAVORECIDO,
0 VLR_MULTA,
0 VLR_JUROS,
0 VLR_FECP_MULTA,
0 VLR_FECP_JUROS,
NULL DATA_EMISSAO
FROM (
SELECT
'FUNDO_ICMS_NORMAL'                                       GRUPO_IMPOSTO,
APU.COD_EMPRESA                                           COD_EMPRESA,
REPLACE(FLX.GRUPO_FISCAL,'','')                           GRUPO_FISCAL,
APU.COD_ESTAB                                             COD_ESTAB,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')                     PERIODO,
FLX.COD_ARRECADACAO                                       COD_ARRECADACAO,
FLX.COD_RECEITA                                           COD_RECEITA,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')||FLX.COD_RECEITA||1 NUM_DOC_ORIGEM,
NULL                                                      SERIE,
NULL                                                      CHAVE_NFE,
NULL                                                      DATA_EMISSAO,
STD.COD_ESTADO                                            UF_FAVORECIDA,
sum(nvl(apu.val_item_discrim,0))                                         VALOR_PRINCIPAL,
TO_CHAR(GP_DT_GERA_GUIAS_CPROC.calcula_data_vencimento(FLX.REGRA_VENCTO,FLX.DIA_VENCTO,(TO_CHAR((APU.DAT_APURACAO +1),'MMYYYY')),EST.IDENT_ESTADO,EST.COD_MUNICIPIO),'YYYYMMDD') DATA_VENCIMENTO,
NULL                                                      DATA_PAGAMENTO,
FLX.CONVENIO                                              CONVENIO,
FLX.DETALHE_RECEITA                                       DETALHAMENTO_RECEITA,
FLX.PRODUTO                                               PRODUTO,
FLX.INF_COMPLEMENTAR                                      INF_COMPLEMENTAR,
null                                                      VALOR_FECP,
'REGRA_FUNDO_ICMS_NORMAL_1'                                 REGRA_IMPOSTO
FROM ITEM_APURAC_DISCR APU, ZGP_VW_UF_CD_RC_GP_IMP_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD
WHERE APU.COD_TIPO_LIVRO = '108'
AND APU.COD_OPER_APUR  = '007'
AND apu.val_item_discrim    > 0
AND APU.COD_EMPRESA    = FLX.cod_empresa
AND APU.COD_ESTAB      = FLX.cod_estab
AND UPPER(FLX.GRUPO_IMPOSTO)  = UPPER('FUNDO_ICMS_NORMAL')
--AND UPPER(DSC_ITEM_APURACAO)  LIKE '%FUNDO%DE%COMBATE%A%POBREZA%'
AND UPPER(DSC_ITEM_APURACAO)  like '%REF. FUNDO DE COMBATE A POBREZA%'
AND APU.COD_EMPRESA    = EST.COD_EMPRESA
AND APU.COD_ESTAB      = EST.COD_ESTAB
AND EST.IDENT_ESTADO   = STD.IDENT_ESTADO
AND STD.COD_ESTADO     = FLX.UF
AND FLX.REGRA_IMPOSTO  = 'REGRA_FUNDO_ICMS_NORMAL_1'
group by 'FUNDO_ICMS_NORMAL',
APU.COD_EMPRESA,
REPLACE(FLX.GRUPO_FISCAL,'',''),
APU.COD_ESTAB,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD'),
FLX.COD_ARRECADACAO,
FLX.COD_RECEITA,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')||FLX.COD_RECEITA||1,
NULL, NULL, NULL,
STD.COD_ESTADO,
TO_CHAR(GP_DT_GERA_GUIAS_CPROC.calcula_data_vencimento(FLX.REGRA_VENCTO,FLX.DIA_VENCTO,(TO_CHAR((APU.DAT_APURACAO +1),'MMYYYY')),EST.IDENT_ESTADO,EST.COD_MUNICIPIO),'YYYYMMDD'),
NULL, FLX.CONVENIO,
FLX.DETALHE_RECEITA,
FLX.PRODUTO, FLX.INF_COMPLEMENTAR, null, 'REGRA_FUNDO_ICMS_NORMAL_1'
UNION
SELECT
'FUNDO_ICMS_NORMAL'                                       GRUPO_IMPOSTO,
APU.COD_EMPRESA                                           COD_EMPRESA,
REPLACE(FLX.GRUPO_FISCAL,'','')                           GRUPO_FISCAL,
APU.COD_ESTAB                                             COD_ESTAB,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')                     PERIODO,
FLX.COD_ARRECADACAO                                       COD_ARRECADACAO,
FLX.COD_RECEITA                                           COD_RECEITA,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')||FLX.COD_RECEITA||1 NUM_DOC_ORIGEM,
NULL                                                      SERIE,
NULL                                                      CHAVE_NFE,
NULL                                                      DATA_EMISSAO,
STD.COD_ESTADO                                            UF_FAVORECIDA,
ROUND((apu.val_item_discrim * 0.1),2)                     VALOR_PRINCIPAL,
TO_CHAR(GP_DT_GERA_GUIAS_CPROC.calcula_data_vencimento(FLX.REGRA_VENCTO,FLX.DIA_VENCTO,(TO_CHAR((APU.DAT_APURACAO +1),'MMYYYY')),EST.IDENT_ESTADO,EST.COD_MUNICIPIO),'YYYYMMDD') DATA_VENCIMENTO,
NULL                                                      DATA_PAGAMENTO,
FLX.CONVENIO                                              CONVENIO,
FLX.DETALHE_RECEITA                                       DETALHAMENTO_RECEITA,
FLX.PRODUTO                                               PRODUTO,
FLX.INF_COMPLEMENTAR                                      INF_COMPLEMENTAR,
null                                                      VALOR_FECP,
'REGRA_FUNDO_ICMS_NORMAL_2'                               REGRA_IMPOSTO
FROM ITEM_APURAC_DISCR APU, ZGP_VW_UF_CD_RC_GP_IMP_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD
WHERE APU.COD_TIPO_LIVRO = '108'
AND APU.COD_OPER_APUR  = '012'
AND apu.val_item_discrim    > 0
AND APU.COD_EMPRESA    = FLX.cod_empresa
AND APU.COD_ESTAB      = FLX.cod_estab
AND UPPER(FLX.GRUPO_IMPOSTO)  = UPPER('FUNDO_ICMS_NORMAL')
--AND UPPER(DSC_ITEM_APURACAO)  LIKE '%VLR_FEEF%'
AND UPPER(DSC_ITEM_APURACAO)  LIKE UPPER('%INCENTIVO FISCAL%')
AND APU.COD_EMPRESA    = EST.COD_EMPRESA
AND APU.COD_ESTAB      = EST.COD_ESTAB
AND EST.IDENT_ESTADO   = STD.IDENT_ESTADO
AND STD.COD_ESTADO     = FLX.UF
AND FLX.REGRA_IMPOSTO  = 'REGRA_FUNDO_ICMS_NORMAL_2'
UNION
SELECT
'FUNDO_ICMS_NORMAL'                                       GRUPO_IMPOSTO,
APU.COD_EMPRESA                                           COD_EMPRESA,
REPLACE(FLX.GRUPO_FISCAL,'','')                           GRUPO_FISCAL,
APU.COD_ESTAB                                             COD_ESTAB,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')                     PERIODO,
FLX.COD_ARRECADACAO                                       COD_ARRECADACAO,
FLX.COD_RECEITA                                           COD_RECEITA,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')||FLX.COD_RECEITA||1 NUM_DOC_ORIGEM,
NULL                                                      SERIE,
NULL                                                      CHAVE_NFE,
NULL                                                      DATA_EMISSAO,
STD.COD_ESTADO                                            UF_FAVORECIDA,
apu.val_item_discrim                                      VALOR_PRINCIPAL,
TO_CHAR(GP_DT_GERA_GUIAS_CPROC.calcula_data_vencimento(FLX.REGRA_VENCTO,FLX.DIA_VENCTO,(TO_CHAR((APU.DAT_APURACAO +1),'MMYYYY')),EST.IDENT_ESTADO,EST.COD_MUNICIPIO),'YYYYMMDD') DATA_VENCIMENTO,
NULL                                                      DATA_PAGAMENTO,
FLX.CONVENIO                                              CONVENIO,
FLX.DETALHE_RECEITA                                       DETALHAMENTO_RECEITA,
FLX.PRODUTO                                               PRODUTO,
FLX.INF_COMPLEMENTAR                                      INF_COMPLEMENTAR,
null                                                      VALOR_FECP,
'REGRA_FUNDO_ICMS_NORMAL_3'                                 REGRA_IMPOSTO
FROM ITEM_APURAC_DISCR APU, ZGP_VW_UF_CD_RC_GP_IMP_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD
WHERE APU.COD_TIPO_LIVRO = '108'
AND APU.COD_OPER_APUR  = '012'
AND apu.val_item_discrim    > 0
AND APU.COD_EMPRESA    = FLX.cod_empresa
AND APU.COD_ESTAB      = FLX.cod_estab
AND UPPER(FLX.GRUPO_IMPOSTO)  = UPPER('FUNDO_ICMS_NORMAL')
--AND UPPER(DSC_ITEM_APURACAO)  LIKE '%DEDU%REFERENTE%AO%FECOP%ICMS%'
AND UPPER(DSC_ITEM_APURACAO)  = 'DEDU  ES REFERENTE AO FECOP ICMS'
AND APU.COD_EMPRESA    = EST.COD_EMPRESA
AND APU.COD_ESTAB      = EST.COD_ESTAB
AND EST.IDENT_ESTADO   = STD.IDENT_ESTADO
AND STD.COD_ESTADO     = FLX.UF
AND FLX.REGRA_IMPOSTO  = 'REGRA_FUNDO_ICMS_NORMAL_3'
UNION
SELECT
'FUNDO_ICMS_NORMAL'                                       GRUPO_IMPOSTO,
APU.COD_EMPRESA                                           COD_EMPRESA,
REPLACE(FLX.GRUPO_FISCAL,'','')                           GRUPO_FISCAL,
APU.COD_ESTAB                                             COD_ESTAB,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')                     PERIODO,
FLX.COD_ARRECADACAO                                       COD_ARRECADACAO,
FLX.COD_RECEITA                                           COD_RECEITA,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')||FLX.COD_RECEITA||1 NUM_DOC_ORIGEM,
NULL                                                      SERIE,
NULL                                                      CHAVE_NFE,
NULL                                                      DATA_EMISSAO,
STD.COD_ESTADO                                            UF_FAVORECIDA,
ROUND((apu.val_item_discrim * 0.1),2)                     VALOR_PRINCIPAL,
TO_CHAR(GP_DT_GERA_GUIAS_CPROC.calcula_data_vencimento(FLX.REGRA_VENCTO,FLX.DIA_VENCTO,(TO_CHAR((APU.DAT_APURACAO +1),'MMYYYY')),EST.IDENT_ESTADO,EST.COD_MUNICIPIO),'YYYYMMDD') DATA_VENCIMENTO,
NULL                                                      DATA_PAGAMENTO,
FLX.CONVENIO                                              CONVENIO,
FLX.DETALHE_RECEITA                                       DETALHAMENTO_RECEITA,
FLX.PRODUTO                                               PRODUTO,
FLX.INF_COMPLEMENTAR                                      INF_COMPLEMENTAR,
null                                                      VALOR_FECP,
'REGRA_FUNDO_ICMS_NORMAL_4'                                 REGRA_IMPOSTO
FROM ITEM_APURAC_DISCR APU, ZGP_VW_UF_CD_RC_GP_IMP_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD
WHERE APU.COD_TIPO_LIVRO = '108'
AND APU.COD_OPER_APUR  = '012'
AND apu.val_item_discrim    > 0
AND APU.COD_EMPRESA    = FLX.cod_empresa
AND APU.COD_ESTAB      = FLX.cod_estab
AND UPPER(FLX.GRUPO_IMPOSTO)  = UPPER('FUNDO_ICMS_NORMAL')
--AND UPPER(DSC_ITEM_APURACAO)  LIKE '%VLR_PROTEGE_15%'
AND UPPER(DSC_ITEM_APURACAO)  LIKE '%INCENTIVO PRO GOIAS%'
AND APU.COD_EMPRESA    = EST.COD_EMPRESA
AND APU.COD_ESTAB      = EST.COD_ESTAB
AND EST.IDENT_ESTADO   = STD.IDENT_ESTADO
AND STD.COD_ESTADO     = FLX.UF
AND FLX.REGRA_IMPOSTO  = 'REGRA_FUNDO_ICMS_NORMAL_4'
UNION
SELECT GRUPO_IMPOSTO,
COD_EMPRESA,
GRUPO_FISCAL,
COD_ESTAB,
PERIODO,
COD_ARRECADACAO,
COD_RECEITA,
NUM_DOC_ORIGEM,
SERIE,
CHAVE_NFE,
DATA_EMISSAO,
UF_FAVORECIDA,
SUM(VALOR_PRINCIPAL) VALOR_PRINCIPAL,
DATA_VENCIMENTO,
DATA_PAGAMENTO,
CONVENIO,
DETALHAMENTO_RECEITA,
PRODUTO,
INF_COMPLEMENTAR,
VALOR_FECP,
REGRA_IMPOSTO
FROM (
SELECT
'FUNDO_ICMS_NORMAL'                                       GRUPO_IMPOSTO,
APU.COD_EMPRESA                                           COD_EMPRESA,
REPLACE(FLX.GRUPO_FISCAL,'','')                           GRUPO_FISCAL,
APU.COD_ESTAB                                             COD_ESTAB,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')                     PERIODO,
FLX.COD_ARRECADACAO                                       COD_ARRECADACAO,
FLX.COD_RECEITA                                           COD_RECEITA,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')||FLX.COD_RECEITA||1 NUM_DOC_ORIGEM,
NULL                                                      SERIE,
NULL                                                      CHAVE_NFE,
NULL                                                      DATA_EMISSAO,
STD.COD_ESTADO                                            UF_FAVORECIDA,
DECODE(apu.dsc_item_apuracao,'FEM ( Fundo de Erradica  o da Mis ria )',apu.val_item_discrim,apu.val_item_discrim * -1)  VALOR_PRINCIPAL,
TO_CHAR(GP_DT_GERA_GUIAS_CPROC.calcula_data_vencimento(FLX.REGRA_VENCTO,FLX.DIA_VENCTO,(TO_CHAR((APU.DAT_APURACAO +1),'MMYYYY')),EST.IDENT_ESTADO,EST.COD_MUNICIPIO),'YYYYMMDD') DATA_VENCIMENTO,
NULL                                                      DATA_PAGAMENTO,
FLX.CONVENIO                                              CONVENIO,
FLX.DETALHE_RECEITA                                       DETALHAMENTO_RECEITA,
FLX.PRODUTO                                               PRODUTO,
FLX.INF_COMPLEMENTAR                                      INF_COMPLEMENTAR,
null                                                      VALOR_FECP,
'REGRA_FUNDO_ICMS_NORMAL_5'                                 REGRA_IMPOSTO
FROM ITEM_APURAC_DISCR APU, ZGP_VW_UF_CD_RC_GP_IMP_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD
WHERE APU.COD_TIPO_LIVRO = '108'
AND (UPPER(apu.dsc_item_apuracao) =  UPPER('D BITO ESPECIAL - FUNDO ERRADICA  O A MIS RIA - ESTORNO FEM%')
OR  UPPER(apu.dsc_item_apuracao) =  UPPER('%FEM ( Fundo de Erradica  o da Mis ria )%'))
AND APU.COD_OPER_APUR  IN ('003','007')
AND apu.val_item_discrim    > 0
AND APU.COD_EMPRESA    = FLX.cod_empresa
AND APU.COD_ESTAB      = FLX.cod_estab
AND UPPER(FLX.GRUPO_IMPOSTO)  = UPPER('FUNDO_ICMS_NORMAL')
AND APU.COD_EMPRESA    = EST.COD_EMPRESA
AND APU.COD_ESTAB      = EST.COD_ESTAB
AND EST.IDENT_ESTADO   = STD.IDENT_ESTADO
AND STD.COD_ESTADO     = FLX.UF
AND APU.COD_ESTAB      = 'K530'
AND FLX.REGRA_IMPOSTO  = 'REGRA_FUNDO_ICMS_NORMAL_5' )

HAVING SUM(VALOR_PRINCIPAL) > 0

GROUP BY GRUPO_IMPOSTO,
COD_EMPRESA,
GRUPO_FISCAL,
COD_ESTAB,
PERIODO,
COD_ARRECADACAO,
COD_RECEITA,
NUM_DOC_ORIGEM,
SERIE,
CHAVE_NFE,
DATA_EMISSAO,
UF_FAVORECIDA,
DATA_VENCIMENTO,
DATA_PAGAMENTO,
CONVENIO,
DETALHAMENTO_RECEITA,
PRODUTO,
INF_COMPLEMENTAR,
VALOR_FECP,
REGRA_IMPOSTO
UNION

SELECT GRUPO_IMPOSTO,
COD_EMPRESA,
GRUPO_FISCAL,
COD_ESTAB,
PERIODO,
COD_ARRECADACAO,
COD_RECEITA,
NUM_DOC_ORIGEM,
SERIE,
CHAVE_NFE,
DATA_EMISSAO,
UF_FAVORECIDA,
SUM(VALOR_PRINCIPAL) VALOR_PRINCIPAL,
DATA_VENCIMENTO,
DATA_PAGAMENTO,
CONVENIO,
DETALHAMENTO_RECEITA,
PRODUTO,
INF_COMPLEMENTAR,
VALOR_FECP,
REGRA_IMPOSTO
FROM (
SELECT
'FUNDO_ICMS_NORMAL'                                       GRUPO_IMPOSTO,
APU.COD_EMPRESA                                           COD_EMPRESA,
REPLACE(FLX.GRUPO_FISCAL,'','')                           GRUPO_FISCAL,
APU.COD_ESTAB                                             COD_ESTAB,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')                     PERIODO,
FLX.COD_ARRECADACAO                                       COD_ARRECADACAO,
FLX.COD_RECEITA                                           COD_RECEITA,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')||FLX.COD_RECEITA||1 NUM_DOC_ORIGEM,
NULL                                                      SERIE,
NULL                                                      CHAVE_NFE,
NULL                                                      DATA_EMISSAO,
STD.COD_ESTADO                                            UF_FAVORECIDA,
apu.val_item_discrim                                      VALOR_PRINCIPAL,
TO_CHAR(GP_DT_GERA_GUIAS_CPROC.calcula_data_vencimento(FLX.REGRA_VENCTO,FLX.DIA_VENCTO,(TO_CHAR((APU.DAT_APURACAO +1),'MMYYYY')),EST.IDENT_ESTADO,EST.COD_MUNICIPIO),'YYYYMMDD') DATA_VENCIMENTO,
NULL                                                      DATA_PAGAMENTO,
FLX.CONVENIO                                              CONVENIO,
FLX.DETALHE_RECEITA                                       DETALHAMENTO_RECEITA,
FLX.PRODUTO                                               PRODUTO,
FLX.INF_COMPLEMENTAR                                      INF_COMPLEMENTAR,
null                                                      VALOR_FECP,
'REGRA_FUNDO_ICMS_NORMAL_6'                                 REGRA_IMPOSTO
FROM ITEM_APURAC_DISCR APU, ZGP_VW_UF_CD_RC_GP_IMP_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD
WHERE APU.COD_TIPO_LIVRO = '108'
AND APU.COD_OPER_APUR  = '012'
AND apu.val_item_discrim    > 0
AND APU.COD_EMPRESA    = FLX.cod_empresa
AND APU.COD_ESTAB      = FLX.cod_estab
AND UPPER(FLX.GRUPO_IMPOSTO)  = UPPER('FUNDO_ICMS_NORMAL')
AND UPPER(DSC_ITEM_APURACAO)  = upper('Fundo de Combate e Erradica  o da Pobreza- FECEP')
AND APU.COD_EMPRESA    = EST.COD_EMPRESA
AND APU.COD_ESTAB      = EST.COD_ESTAB
AND EST.IDENT_ESTADO   = STD.IDENT_ESTADO
AND STD.COD_ESTADO     = FLX.UF
AND FLX.REGRA_IMPOSTO  = 'REGRA_FUNDO_ICMS_NORMAL_6')

GROUP BY GRUPO_IMPOSTO, COD_EMPRESA, GRUPO_FISCAL, COD_ESTAB, PERIODO,
COD_ARRECADACAO, COD_RECEITA, NUM_DOC_ORIGEM, SERIE, CHAVE_NFE,
UF_FAVORECIDA, CONVENIO, DETALHAMENTO_RECEITA, PRODUTO, INF_COMPLEMENTAR,
DATA_VENCIMENTO, DATA_PAGAMENTO, REGRA_IMPOSTO, VALOR_FECP
UNION
SELECT
'FUNDO_ICMS_NORMAL'                                       GRUPO_IMPOSTO,
APU.COD_EMPRESA                                           COD_EMPRESA,
REPLACE(FLX.GRUPO_FISCAL,'','')                           GRUPO_FISCAL,
APU.COD_ESTAB                                             COD_ESTAB,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')                     PERIODO,
FLX.COD_ARRECADACAO                                       COD_ARRECADACAO,
FLX.COD_RECEITA                                           COD_RECEITA,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')||FLX.COD_RECEITA||1 NUM_DOC_ORIGEM,
NULL                                                      SERIE,
NULL                                                      CHAVE_NFE,
NULL                                                      DATA_EMISSAO,
STD.COD_ESTADO                                            UF_FAVORECIDA,
ROUND((apu.val_item_discrim * 0.1),2)                     VALOR_PRINCIPAL,
TO_CHAR(GP_DT_GERA_GUIAS_CPROC.calcula_data_vencimento(FLX.REGRA_VENCTO,FLX.DIA_VENCTO,(TO_CHAR((APU.DAT_APURACAO +1),'MMYYYY')),EST.IDENT_ESTADO,EST.COD_MUNICIPIO),'YYYYMMDD') DATA_VENCIMENTO,
NULL                                                      DATA_PAGAMENTO,
FLX.CONVENIO                                              CONVENIO,
FLX.DETALHE_RECEITA                                       DETALHAMENTO_RECEITA,
FLX.PRODUTO                                               PRODUTO,
FLX.INF_COMPLEMENTAR                                      INF_COMPLEMENTAR,
null                                                      VALOR_FECP,
'REGRA_FUNDO_ICMS_NORMAL_7'                                 REGRA_IMPOSTO
FROM ITEM_APURAC_DISCR APU, ZGP_VW_UF_CD_RC_GP_IMP_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD
WHERE APU.COD_TIPO_LIVRO = '108'
AND APU.COD_OPER_APUR  = '012'
AND apu.val_item_discrim    > 0
AND APU.COD_EMPRESA    = FLX.cod_empresa
AND APU.COD_ESTAB      = FLX.cod_estab
AND UPPER(FLX.GRUPO_IMPOSTO)  = UPPER('FUNDO_ICMS_NORMAL')
--AND UPPER(DSC_ITEM_APURACAO)  LIKE '%VLR_FEEF%'
AND UPPER(DSC_ITEM_APURACAO)  LIKE UPPER('%BENEFICIO INCENTIVO DESENVOLVE 90% - CONF. RESOLUCAO 72/2010%')
AND APU.COD_EMPRESA    = EST.COD_EMPRESA
AND APU.COD_ESTAB      = EST.COD_ESTAB
AND EST.IDENT_ESTADO   = STD.IDENT_ESTADO
AND STD.COD_ESTADO     = FLX.UF
AND FLX.REGRA_IMPOSTO  = 'REGRA_FUNDO_ICMS_NORMAL_7'
UNION
SELECT GRUPO_IMPOSTO,
COD_EMPRESA,
GRUPO_FISCAL,
COD_ESTAB,
PERIODO,
COD_ARRECADACAO,
COD_RECEITA,
NUM_DOC_ORIGEM,
SERIE,
CHAVE_NFE,
DATA_EMISSAO,
UF_FAVORECIDA,
SUM(VALOR_PRINCIPAL) VALOR_PRINCIPAL,
DATA_VENCIMENTO,
DATA_PAGAMENTO,
CONVENIO,
DETALHAMENTO_RECEITA,
PRODUTO,
INF_COMPLEMENTAR,
VALOR_FECP,
REGRA_IMPOSTO
FROM (
SELECT
'FUNDO_ICMS_NORMAL'                                       GRUPO_IMPOSTO,
APU.COD_EMPRESA                                           COD_EMPRESA,
REPLACE(FLX.GRUPO_FISCAL,'','')                           GRUPO_FISCAL,
APU.COD_ESTAB                                             COD_ESTAB,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')                     PERIODO,
FLX.COD_ARRECADACAO                                       COD_ARRECADACAO,
FLX.COD_RECEITA                                           COD_RECEITA,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')||FLX.COD_RECEITA||1 NUM_DOC_ORIGEM,
'001'                                                     SERIE,
NULL                                                      CHAVE_NFE,
NULL                                                      DATA_EMISSAO,
STD.COD_ESTADO                                            UF_FAVORECIDA,
apu.val_item_discrim                                      VALOR_PRINCIPAL,
TO_CHAR(GP_DT_GERA_GUIAS_CPROC.calcula_data_vencimento(FLX.REGRA_VENCTO,FLX.DIA_VENCTO,(TO_CHAR((APU.DAT_APURACAO +1),'MMYYYY')),EST.IDENT_ESTADO,EST.COD_MUNICIPIO),'YYYYMMDD') DATA_VENCIMENTO,
NULL                                                      DATA_PAGAMENTO,
FLX.CONVENIO                                              CONVENIO,
FLX.DETALHE_RECEITA                                       DETALHAMENTO_RECEITA,
FLX.PRODUTO                                               PRODUTO,
FLX.INF_COMPLEMENTAR                                      INF_COMPLEMENTAR,
null                                                      VALOR_FECP,
'REGRA_FUNDO_ICMS_NORMAL_8'                                 REGRA_IMPOSTO
FROM ITEM_APURAC_DISCR APU, ZGP_VW_UF_CD_RC_GP_IMP_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD
WHERE APU.COD_TIPO_LIVRO = '108'
AND APU.COD_OPER_APUR  = '012'
AND apu.val_item_discrim    > 0
AND APU.COD_EMPRESA    = FLX.cod_empresa
AND APU.COD_ESTAB      = FLX.cod_estab
AND UPPER(FLX.GRUPO_IMPOSTO)  = UPPER('FUNDO_ICMS_NORMAL')
AND UPPER(DSC_ITEM_APURACAO)  like  '%FECEP 2% (INCENTIVO B01%'
AND APU.COD_EMPRESA    = EST.COD_EMPRESA
AND APU.COD_ESTAB      = EST.COD_ESTAB
AND EST.IDENT_ESTADO   = STD.IDENT_ESTADO
AND STD.COD_ESTADO     = FLX.UF
AND FLX.REGRA_IMPOSTO  = 'REGRA_FUNDO_ICMS_NORMAL_8')

GROUP BY GRUPO_IMPOSTO, COD_EMPRESA, GRUPO_FISCAL, COD_ESTAB, PERIODO,
COD_ARRECADACAO, COD_RECEITA, NUM_DOC_ORIGEM, SERIE, CHAVE_NFE,
UF_FAVORECIDA, CONVENIO, DETALHAMENTO_RECEITA, PRODUTO, INF_COMPLEMENTAR,
DATA_VENCIMENTO, DATA_PAGAMENTO, REGRA_IMPOSTO, VALOR_FECP
UNION
SELECT GRUPO_IMPOSTO,
COD_EMPRESA,
GRUPO_FISCAL,
COD_ESTAB,
PERIODO,
COD_ARRECADACAO,
COD_RECEITA,
NUM_DOC_ORIGEM,
SERIE,
CHAVE_NFE,
DATA_EMISSAO,
UF_FAVORECIDA,
SUM(VALOR_PRINCIPAL) VALOR_PRINCIPAL,
DATA_VENCIMENTO,
DATA_PAGAMENTO,
CONVENIO,
DETALHAMENTO_RECEITA,
PRODUTO,
INF_COMPLEMENTAR,
VALOR_FECP,
REGRA_IMPOSTO
FROM (
SELECT
'FUNDO_ICMS_NORMAL'                                       GRUPO_IMPOSTO,
APU.COD_EMPRESA                                           COD_EMPRESA,
REPLACE(FLX.GRUPO_FISCAL,'','')                           GRUPO_FISCAL,
APU.COD_ESTAB                                             COD_ESTAB,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')                     PERIODO,
FLX.COD_ARRECADACAO                                       COD_ARRECADACAO,
FLX.COD_RECEITA                                           COD_RECEITA,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')||FLX.COD_RECEITA||1 NUM_DOC_ORIGEM,
'002'                                                     SERIE,
NULL                                                      CHAVE_NFE,
NULL                                                      DATA_EMISSAO,
STD.COD_ESTADO                                            UF_FAVORECIDA,
apu.val_item_discrim                                      VALOR_PRINCIPAL,
TO_CHAR(GP_DT_GERA_GUIAS_CPROC.calcula_data_vencimento(FLX.REGRA_VENCTO,FLX.DIA_VENCTO,(TO_CHAR((APU.DAT_APURACAO +1),'MMYYYY')),EST.IDENT_ESTADO,EST.COD_MUNICIPIO),'YYYYMMDD') DATA_VENCIMENTO,
NULL                                                      DATA_PAGAMENTO,
FLX.CONVENIO                                              CONVENIO,
FLX.DETALHE_RECEITA                                       DETALHAMENTO_RECEITA,
FLX.PRODUTO                                               PRODUTO,
FLX.INF_COMPLEMENTAR                                      INF_COMPLEMENTAR,
null                                                      VALOR_FECP,
'REGRA_FUNDO_ICMS_NORMAL_8'                                 REGRA_IMPOSTO
FROM ITEM_APURAC_DISCR APU, ZGP_VW_UF_CD_RC_GP_IMP_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD
WHERE APU.COD_TIPO_LIVRO = '108'
AND APU.COD_OPER_APUR  = '012'
AND apu.val_item_discrim    > 0
AND APU.COD_EMPRESA    = FLX.cod_empresa
AND APU.COD_ESTAB      = FLX.cod_estab
AND UPPER(FLX.GRUPO_IMPOSTO)  = UPPER('FUNDO_ICMS_NORMAL')
--AND UPPER(DSC_ITEM_APURACAO)  LIKE '%FECEP 2%'
AND UPPER(DSC_ITEM_APURACAO)  like  '%FECEP 2% (INCENTIVO B02%'
AND APU.COD_EMPRESA    = EST.COD_EMPRESA
AND APU.COD_ESTAB      = EST.COD_ESTAB
AND EST.IDENT_ESTADO   = STD.IDENT_ESTADO
AND STD.COD_ESTADO     = FLX.UF
AND FLX.REGRA_IMPOSTO  = 'REGRA_FUNDO_ICMS_NORMAL_8')

GROUP BY GRUPO_IMPOSTO, COD_EMPRESA, GRUPO_FISCAL, COD_ESTAB, PERIODO,
COD_ARRECADACAO, COD_RECEITA, NUM_DOC_ORIGEM, SERIE, CHAVE_NFE,
UF_FAVORECIDA, CONVENIO, DETALHAMENTO_RECEITA, PRODUTO, INF_COMPLEMENTAR,
DATA_VENCIMENTO, DATA_PAGAMENTO, REGRA_IMPOSTO, VALOR_FECP
UNION

SELECT
'FUNDO_ICMS_NORMAL'                                       GRUPO_IMPOSTO,
APU.COD_EMPRESA                                           COD_EMPRESA,
REPLACE(FLX.GRUPO_FISCAL,'','')                           GRUPO_FISCAL,
APU.COD_ESTAB                                             COD_ESTAB,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')                     PERIODO,
FLX.COD_ARRECADACAO                                       COD_ARRECADACAO,
FLX.COD_RECEITA                                           COD_RECEITA,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')||FLX.COD_RECEITA||1 NUM_DOC_ORIGEM,
NULL                                                      SERIE,
NULL                                                      CHAVE_NFE,
NULL                                                      DATA_EMISSAO,
STD.COD_ESTADO                                            UF_FAVORECIDA,
ROUND((apu.val_item_discrim * 0.02),2)                    VALOR_PRINCIPAL,
TO_CHAR(GP_DT_GERA_GUIAS_CPROC.calcula_data_vencimento(FLX.REGRA_VENCTO,FLX.DIA_VENCTO,(TO_CHAR((APU.DAT_APURACAO +1),'MMYYYY')),EST.IDENT_ESTADO,EST.COD_MUNICIPIO),'YYYYMMDD') DATA_VENCIMENTO,
NULL                                                      DATA_PAGAMENTO,
FLX.CONVENIO                                              CONVENIO,
FLX.DETALHE_RECEITA                                       DETALHAMENTO_RECEITA,
FLX.PRODUTO                                               PRODUTO,
FLX.INF_COMPLEMENTAR                                      INF_COMPLEMENTAR,
null                                                      VALOR_FECP,
'REGRA_FUNDO_ICMS_NORMAL_9'                                 REGRA_IMPOSTO
FROM ITEM_APURAC_DISCR APU, ZGP_VW_UF_CD_RC_GP_IMP_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD
WHERE APU.COD_TIPO_LIVRO = '108'
AND APU.COD_OPER_APUR  = '012'
AND apu.val_item_discrim    > 0
AND APU.COD_EMPRESA    = FLX.cod_empresa
AND APU.COD_ESTAB      = FLX.cod_estab
AND UPPER(FLX.GRUPO_IMPOSTO)  = UPPER('FUNDO_ICMS_NORMAL')
AND UPPER(DSC_ITEM_APURACAO)  like upper('%INCENTIVO FISCAL%')
AND APU.COD_EMPRESA    = EST.COD_EMPRESA
AND APU.COD_ESTAB      = EST.COD_ESTAB
AND EST.IDENT_ESTADO   = STD.IDENT_ESTADO
AND STD.COD_ESTADO     = FLX.UF
AND FLX.REGRA_IMPOSTO  = 'REGRA_FUNDO_ICMS_NORMAL_9'
UNION
SELECT
'FUNDO_ICMS_NORMAL'                                       GRUPO_IMPOSTO,
APU.COD_EMPRESA                                           COD_EMPRESA,
REPLACE(FLX.GRUPO_FISCAL,'','')                           GRUPO_FISCAL,
APU.COD_ESTAB                                             COD_ESTAB,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')                     PERIODO,
FLX.COD_ARRECADACAO                                       COD_ARRECADACAO,
FLX.COD_RECEITA                                           COD_RECEITA,
TO_CHAR(APU.DAT_APURACAO, 'YYYYMMDD')||FLX.COD_RECEITA||1 NUM_DOC_ORIGEM,
NULL                                                      SERIE,
NULL                                                      CHAVE_NFE,
NULL                                                      DATA_EMISSAO,
STD.COD_ESTADO                                            UF_FAVORECIDA,
apu.val_item_discrim                                      VALOR_PRINCIPAL,
TO_CHAR(GP_DT_GERA_GUIAS_CPROC.calcula_data_vencimento(FLX.REGRA_VENCTO,FLX.DIA_VENCTO,(TO_CHAR((APU.DAT_APURACAO +1),'MMYYYY')),EST.IDENT_ESTADO,EST.COD_MUNICIPIO),'YYYYMMDD') DATA_VENCIMENTO,
NULL                                                      DATA_PAGAMENTO,
FLX.CONVENIO                                              CONVENIO,
FLX.DETALHE_RECEITA                                       DETALHAMENTO_RECEITA,
FLX.PRODUTO                                               PRODUTO,
FLX.INF_COMPLEMENTAR                                      INF_COMPLEMENTAR,
null                                                      VALOR_FECP,
'REGRA_FUNDO_ICMS_NORMAL_10'                                 REGRA_IMPOSTO
FROM ITEM_APURAC_DISCR APU, ZGP_VW_UF_CD_RC_GP_IMP_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD
WHERE APU.COD_TIPO_LIVRO = '108'
AND APU.COD_OPER_APUR  = '006'
AND apu.val_item_discrim    > 0
AND APU.COD_EMPRESA    = FLX.cod_empresa
AND APU.COD_ESTAB      = FLX.cod_estab
AND UPPER(FLX.GRUPO_IMPOSTO)  = UPPER('FUNDO_ICMS_NORMAL')
AND UPPER(apu.dsc_item_apuracao) =  'ART. 56 DO RICMS/00 FECOEP'
AND APU.COD_EMPRESA    = EST.COD_EMPRESA
AND APU.COD_ESTAB      = EST.COD_ESTAB
AND EST.IDENT_ESTADO   = STD.IDENT_ESTADO
AND STD.COD_ESTADO     = FLX.UF
AND FLX.REGRA_IMPOSTO  = 'REGRA_FUNDO_ICMS_NORMAL_10') J, GP_ESTAB_TEMP_CPROC TM
where TM.EMPRESA                             = J.COD_EMPRESA
and TM.ESTAB                               = J.COD_ESTAB
and J.COD_EMPRESA                          = MCOD_EMPRESA
and to_char(last_day(tm.dT_PERIODO), 'YYYYMMDD') = J.PERIODO
and upper(TRIM(TM.GRP_IMP))                = upper(J.GRUPO_IMPOSTO)
and J.UF_FAVORECIDA                LIKE DECODE(tm.uf_estab, 'TD', '%', tm.uf_estab)
and J.COD_EMPRESA   = v_cod_empresa
and tm.saida        = v_tipo_saida
and tm.id_proc      = v_mcod_id;

REG geraJSON5%rowtype;
v_arquivo sys.utl_file.file_type;
vs_arquivo          varchar2(32767);
mLinha              Varchar2(2000);
v_saida             varchar2(1);
BEGIN

loga('GERA_FUNDO_ICMS_NORMAL',FALSE);

FOR r_pallet IN geraJSON5 LOOP
vPalet_Count := geraJSON5%ROWCOUNT;
v_saida      := r_pallet.p_tipo_saida;
END LOOP;

loga('Qtde Registros:'||vPalet_Count,FALSE);

IF vPalet_Count = 0 then
lib_proc.add_log('SEM DADOS PARA GERACAO DO ARQUIVO NO PERIODO E GRUPO SELECIONADO',1);
lib_proc.add_log('PERIODO: '||TO_CHAR(v_periodo, 'MM/YYYY') ,1);
lib_proc.add_log('GRUPO DE IMPOSTO: '||v_grupo_imposto,1);
else
FOR REG in geraJSON5 loop
vCount := vCount+1;
If geraJSON5%ROWCOUNT = 1 Then
if reg.p_tipo_saida = 1 then
v_arquivo := SYS.utl_file.fopen(VS_DIRETORIO,mproc_id||'_DOOTAX_'|| REG.GRUPO_IMPOSTO||'_'||to_char(trunc(sysdate), 'YYYYMMDD') ||'.txt', 'W',32767);
SYS.utl_file.put_line(v_arquivo,('{"contas_a_pagar":[')||CHR(10));
SYS.utl_file.put_line(v_arquivo, ('{')||CHR(10));
vs_arquivo := '{';
elsif reg.p_tipo_saida = 2 then
LIB_PROC.ADD_TIPO(MPROC_ID, 1, mproc_id||'_'|| REG.GRUPO_IMPOSTO||'_'||to_char(trunc(sysdate), 'YYYYMMDD') ||'.txt', 2);
vs_arquivo := ('{"contas_a_pagar":[');
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
vs_arquivo := ('{');
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
end if;
lib_proc.add_log('  |Geracao arquivo JSON | NOME DO ARQUIVO: ''  |Geracao arquivo JSON | NOME DO ARQUIVO: '||mproc_id||'_'|| REG.GRUPO_IMPOSTO||'_'||to_char(trunc(sysdate), 'YYYYMMDD') ||'.txt   '||'DIRETORIO: '||VS_DIRETORIO   ,1);
lib_proc.add_log('{"contas_a_pagar":[',1);
lib_proc.add_log('{',1);
Else
if reg.p_tipo_saida = 1 then
SYS.utl_file.put_line(v_arquivo, ('{')||CHR(10));
vs_arquivo := ('{');

elsif reg.p_tipo_saida = 2 then
vs_arquivo := ('{');
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
end if;
lib_proc.add_log('{',1);
End If;
if reg.p_tipo_saida = 1 then
sys.utl_file.put_line(v_arquivo, (json('cod_empresa'    , reg.cod_empresa))||CHR(10));

sys.utl_file.put_line(v_arquivo, (json('cod_estab'      , reg.cod_estab))||CHR(10));

sys.utl_file.put_line(v_arquivo, (json('periodo'        , reg.periodo))||CHR(10));

sys.utl_file.put_line(v_arquivo, (json('cod_arrecadacao', reg.cod_arrecadacao))||CHR(10));

sys.utl_file.put_line(v_arquivo, (json('cod_receita'    , reg.cod_receita))||CHR(10));

sys.utl_file.put_line(v_arquivo, (json('uf_favorecida'  , reg.uf_favorecida))||CHR(10));
if reg.num_doc_origem is not null then
sys.utl_file.put_line(v_arquivo, (json('num_doc_origem' , reg.num_doc_origem))||CHR(10));
end if;
IF REG.SERIE IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('serie' , reg.serie))||CHR(10));
END IF;
IF REG.DETALHAMENTO_RECEITA IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('det_receita' , reg.detalhamento_receita))||CHR(10));
END IF;
IF REG.PRODUTO IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('cod_produto' , reg.produto))||CHR(10));
END IF;
IF REG.CONVENIO IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('convenio' , reg.convenio))||CHR(10));
END IF;
IF REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' then
sys.utl_file.put_line(v_arquivo, (json('vlr_principal' , replace(trim(to_char(reg.valor_principal,'999999990D99')),',','.'),true))||CHR(10));
ELSE
sys.utl_file.put_line(v_arquivo, (json('vlr_principal' , replace(trim(to_char(reg.valor_principal,'999999990D99')),',','.')))||CHR(10));
END IF;
IF REG.CHAVE_NFE IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('chave_dfe' , reg.chave_nfe))||CHR(10));
END IF;
-----
CASE WHEN REG.VALOR_FECP IS NOT NULL AND REG.VALOR_FECP > 0 THEN
CASE WHEN REG.INF_COMPLEMENTAR IS NOT NULL THEN
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , reg.data_vencimento))||CHR(10));
END CASE;
CASE WHEN REG.DATA_PAGAMENTO IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , reg.data_vencimento))||CHR(10));
ELSE NULL;
END CASE;
sys.utl_file.put_line(v_arquivo, (json('vlr_fecp' , replace(trim(to_char(reg.valor_fecp,'999999990D99')),',','.'),true))||CHR(10));
ELSE
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento))||CHR(10));
ELSE
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , reg.data_vencimento))||CHR(10));
END CASE;
CASE WHEN REG.DATA_PAGAMENTO IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('data_pagamento' , reg.data_pagamento))||CHR(10));
ELSE NULL;
END CASE;
sys.utl_file.put_line(v_arquivo, (json('vlr_fecp' , replace(trim(to_char(reg.valor_fecp,'999999990D99')),',','.')))||CHR(10));
sys.utl_file.put_line(v_arquivo, (json('inf_complementar' , to_char(reg.inf_complementar),true))||CHR(10));
END CASE;
ELSE
CASE WHEN REG.INF_COMPLEMENTAR IS NULL THEN
CASE WHEN REG.DATA_PAGAMENTO IS NULL THEN
IF REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , to_char(reg.data_vencimento),TRUE))||CHR(10));
END IF;
ELSE
IF REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' then
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , to_char(reg.data_vencimento)))||CHR(10));
END IF;
sys.utl_file.put_line(v_arquivo, (json('data_pagamento' , to_char(reg.data_pagamento),TRUE))||CHR(10));
END CASE;
ELSE
CASE WHEN REG.UF_FAVORECIDA = 'AM'  AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , to_char(reg.data_vencimento)))||CHR(10));
END CASE;
CASE WHEN REG.DATA_PAGAMENTO IS NOT NULL THEN
sys.utl_file.put_line(v_arquivo, (json('data_vencimento' , to_char(reg.data_pagamento)))||CHR(10));
ELSE NULL;
END CASE;
sys.utl_file.put_line(v_arquivo, (json('inf_complementar' , to_char(reg.inf_complementar),TRUE))||CHR(10));
END CASE;
END CASE;
-- SERVIDOR LOCAL
elsif reg.p_tipo_saida = 2 then
vs_arquivo := (json('cod_empresa'    , reg.cod_empresa));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
vs_arquivo := (json('cod_estab'      , reg.cod_estab));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
IF REG.REGRA_IMPOSTO = 'REGRA_DIFAL_2' THEN
vs_arquivo := (json('periodo'        , reg.data_emissao));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
ELSE
vs_arquivo := (json('periodo'        , reg.periodo));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
vs_arquivo := (json('cod_arrecadacao', reg.cod_arrecadacao));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
vs_arquivo := (json('cod_receita'    , reg.cod_receita));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
vs_arquivo := (json('uf_favorecida'  , reg.uf_favorecida));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
if reg.num_doc_origem is not null then
vs_arquivo := (json('num_doc_origem' , reg.num_doc_origem));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
end if;
IF REG.SERIE IS NOT NULL THEN
vs_arquivo := (json('serie'  , reg.serie));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
IF REG.DETALHAMENTO_RECEITA IS NOT NULL THEN
vs_arquivo := (json('det_receita'  , reg.detalhamento_receita));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
IF REG.PRODUTO IS NOT NULL THEN
vs_arquivo := (json('cod_produto'  , reg.produto));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
IF REG.CONVENIO IS NOT NULL THEN
vs_arquivo := (json('convenio'  , reg.convenio));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
IF REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' then
vs_arquivo := (json('vlr_principal'  , replace(trim(to_char(reg.valor_principal,'999999990D99')),',','.'),true));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
ELSE
vs_arquivo := (json('vlr_principal'  , replace(trim(to_char(reg.valor_principal,'999999990D99')),',','.')));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
IF REG.CHAVE_NFE IS NOT NULL THEN
vs_arquivo := (json('chave_dfe'  , reg.chave_nfe));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END IF;
CASE WHEN REG.VALOR_FECP IS NOT NULL AND REG.VALOR_FECP > 0 THEN
CASE WHEN REG.INF_COMPLEMENTAR IS NOT NULL THEN
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_vencimento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
CASE WHEN REG.DATA_PAGAMENTO IS NOT NULL THEN
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_pagamento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
ELSE NULL;
END CASE;
vs_arquivo := (json('vlr_fecp'  , replace(trim(to_char(reg.valor_fecp,'999999990D99')),',','.'),true));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
ELSE
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_vencimento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
CASE WHEN REG.DATA_PAGAMENTO IS NOT NULL THEN
vs_arquivo := (json('data_pagamento'  , to_char(reg.data_pagamento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
ELSE NULL;
END CASE;
vs_arquivo := (json('vlr_fecp'  , replace(trim(to_char(reg.valor_fecp,'999999990D99')),',','.')));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
vs_arquivo := (json('inf_complementar'  , to_char(reg.inf_complementar),true));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
ELSE
CASE WHEN REG.INF_COMPLEMENTAR IS NULL THEN
CASE WHEN REG.DATA_PAGAMENTO IS NULL THEN
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_vencimento),TRUE));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
ELSE
CASE WHEN REG.UF_FAVORECIDA = 'AM' AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' then
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_vencimento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
vs_arquivo := (json('data_pagamento'  , to_char(reg.data_pagamento),TRUE));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
ELSE
CASE WHEN REG.UF_FAVORECIDA = 'AM'  AND REG.GRUPO_IMPOSTO = 'ICMS_NORMAL' THEN
SYS.DBMS_OUTPUT.PUT_LINE(json('data_vencimento', to_char(reg.data_vencimento)));
ELSE
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_vencimento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
CASE WHEN REG.DATA_PAGAMENTO IS NOT NULL THEN
vs_arquivo := (json('data_vencimento'  , to_char(reg.data_pagamento)));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
ELSE NULL;
END CASE;
vs_arquivo := (json('inf_complementar'  , to_char(reg.inf_complementar),TRUE));
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
END CASE;
END CASE;
end if;
lib_proc.add_log(json('cod_empresa'    , reg.cod_empresa),1);
lib_proc.add_log(json('cod_estab'      , reg.cod_estab),1);
lib_proc.add_log(json('periodo'        , reg.periodo),1);
lib_proc.add_log(json('cod_arrecadacao', reg.cod_arrecadacao),1);
lib_proc.add_log(json('cod_receita'    , reg.cod_receita),1);
lib_proc.add_log(json('uf_favorecida'  , reg.uf_favorecida),1);
if reg.num_doc_origem is not null then
lib_proc.add_log(json('num_doc_origem' , reg.num_doc_origem),1);
end if;
if reg.serie is not null then
lib_proc.add_log(json('serie' , reg.serie),1);
end if;
if reg.data_vencimento is not null then
lib_proc.add_log(json('data_vencimento' , reg.data_vencimento),1);
end if;
if reg.data_pagamento is not null then
lib_proc.add_log(json('data_pagamento' , reg.data_pagamento),1);
end if;
if reg.convenio is not null then
lib_proc.add_log(json('convenio' , reg.convenio),1);
end if;
if reg.produto is not null then
lib_proc.add_log(json('produto' , reg.produto),1);
end if;
if reg.detalhamento_receita is not null then
lib_proc.add_log(json('det_receita' , reg.detalhamento_receita),1);
end if;
if reg.inf_complementar is not null then
lib_proc.add_log(json('inf_complementar' , reg.inf_complementar),1);
end if;
if reg.chave_nfe is null then
if reg.valor_fecp is not null then
lib_proc.add_log(json('vlr_principal'  , reg.valor_principal),1);
lib_proc.add_log(json('valor_fecp' , reg.valor_fecp,true),1);
else
lib_proc.add_log(json('vlr_principal'  , reg.valor_principal,true),1);
end if;
else
if reg.valor_fecp is not null then
lib_proc.add_log(json('vlr_principal'  , reg.valor_principal),1);
lib_proc.add_log(json('valor_fecp' , reg.valor_fecp),1);
else
lib_proc.add_log(json('vlr_principal'  , reg.valor_principal,true),1);
end if;
lib_proc.add_log(json('vlr_principal'  , reg.valor_principal),1);
lib_proc.add_log(json('chave_dfe' , reg.chave_nfe,true),1);
end if;
if reg.p_tipo_saida = 1 then
--Se houver mais de 1 bloco no json insere virgula ao final do bloco, exceto no ultimo registro.
if vCount < vPalet_Count then
sys.utl_file.put_line(v_arquivo, ('},'));
else
sys.utl_file.put_line(v_arquivo, ('}'));
end if;
elsif reg.p_tipo_saida = 2 then
--Se houver mais de 1 bloco no json insere virgula ao final do bloco, exceto no ultimo registro.
if vCount < vPalet_Count then
vs_arquivo := ('},');
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
lib_proc.add_log('},',1);
else
vs_arquivo := ('}');
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
lib_proc.add_log('}',1);
end if;
end if;
insert into GP_LOGS_JSON_DT_CPROC  values (mproc_id,
musuario,
TO_CHAR(SYSDATE, 'DD/MM/YYYY HH24:MI:SS'),
reg.cod_empresa,
reg.cod_estab,
reg.periodo,
reg.grupo_imposto,
reg.cod_arrecadacao,
reg.cod_receita,
reg.uf_favorecida,
reg.num_doc_origem,
reg.serie,
reg.chave_nfe,
reg.valor_principal,
reg.valor_fecp,
reg.data_vencimento,
reg.data_pagamento,
reg.inf_complementar,
reg.detalhamento_receita,
reg.convenio,
reg.produto);
--commit;
end loop;


if v_saida = 1 then
sys.utl_file.put_line(v_arquivo, (']}'||CHR(13)));
elsif v_saida = 2 then
vs_arquivo := (']}');
mLinha := LIB_STR.w('', vs_arquivo, 1);
LIB_PROC.add(mLinha, null, null, 1);
end if;
lib_proc.add_log(']}',1);
sys.utl_file.fclose(v_arquivo);
end if;
delete from GP_ESTAB_TEMP_CPROC where id_proc = mproc_id;
COMMIT;
END;
END GERA_FUNDO_ICMS_NORMAL;

FUNCTION fn_ret_last_ddl_time
RETURN VARCHAR2 IS
VS_LAST_DDL_TIME VARCHAR2(30);
BEGIN

SELECT TO_CHAR(MAX(AO.LAST_DDL_TIME),'DD/MM/YYYY HH24:MI')
INTO VS_LAST_DDL_TIME
FROM ALL_OBJECTS AO
WHERE OBJECT_NAME = $$PLSQL_UNIT;

RETURN VS_LAST_DDL_TIME;

END;



FUNCTION executar(p_periodo        date,
p_grp_imp       varchar2,
p_uf_estab      varchar2,
--p_saida         varchar2,
p_cod_estab      Lib_Proc.Vartab
) return integer is
cont_estab NUMBER;

V_MODULO_PRT   VARCHAR2(100);

BEGIN
-- Cria Processo / Procedure
--mproc_id := LIB_PROC.new('GP_DT_GERA_GUIAS_CPROC', 47, 150);
mproc_id := LIB_PROC.new($$PLSQL_UNIT, 47, 150);
LIB_PROC.add_log('V:'||V_VERSAO||'-'||fn_ret_last_ddl_time,1);
commit;

mcod_empresa := LIB_PARAMETROS.RECUPERAR('EMPRESA');
mcod_estab   := LIB_PARAMETROS.recuperar('ESTABELECIMENTO');
musuario     := LIB_PARAMETROS.Recuperar('USUARIO');
loga('Usu rio: '||musuario,false);
LIB_PARAMETROS.Salvar('USUARIO','');

SELECT MAX(A.VALOR)
INTO V_MODULO_PRT
FROM FPAR_PARAM_DET  A,
FPAR_PARAMETROS B
WHERE A.ID_PARAMETRO = B.ID_PARAMETROS
AND B.NOME_FRAMEWORK = 'HNK_ZFI412_ARQUIVO_CPAR'
AND B.DESCRICAO = 'DOOTAX'
AND A.NOME_PARAM = 'MOD_PRT_DIR_SERV';


IF V_MODULO_PRT IS NULL THEN
LOGA('ATENCAO: MODULO NAO CADASTRADO NO PERFIL DOOTAX DOS PARAMETROS GERAIS GERACAO ARQUIVO', FALSE);
COMMIT;
END IF;


SELECT max(DIRECTORY_NAME)
into VS_DIRETORIO
FROM PRT_DIRETORIOS_SERVIDOR
WHERE COD_MODULO = V_MODULO_PRT;--'JOB SERVIDOR';


--   VS_DIRETORIO := 'DOOTAX_DIR';

if VS_DIRETORIO is null then
loga('ATENCAO: DIRETORIO NAO CADASTRADO',false);
commit;
end if;


--FOR cont_estab IN 1 .. p_cod_estab.COUNT LOOP
cont_estab := 0;
WHILE P_COD_ESTAB.COUNT > cont_estab
LOOP
cont_estab := cont_estab + 1;
insert into GP_ESTAB_TEMP_CPROC  values (mproc_id, mcod_empresa, p_cod_estab(cont_estab),p_periodo,p_grp_imp,null,p_uf_estab,'1');
--commit;

end loop;
commit;
begin

IF UPPER(p_grp_imp) =  'ICMS_NORMAL' THEN
gera_icms_normal(mproc_id,mcod_empresa, mcod_estab, p_periodo, p_grp_imp, p_uf_estab, '1');
ELSIF UPPER(p_grp_imp) =  'DIFAL' THEN
gera_difal(mproc_id,mcod_empresa, mcod_estab, p_periodo, p_grp_imp, p_uf_estab, '1');
ELSIF UPPER(p_grp_imp) =  'ICMS_ANTECIPADO' THEN
gera_icms_antecipado(mproc_id,mcod_empresa, mcod_estab, p_periodo, p_grp_imp, p_uf_estab, '1');
ELSIF UPPER(p_grp_imp) =  'ICMS_INCENTIVADO' THEN
gera_icms_incentivado(mproc_id,mcod_empresa, mcod_estab, p_periodo, p_grp_imp, p_uf_estab, '1');
ELSIF UPPER(p_grp_imp) =  'FUNDO_ICMS_NORMAL' THEN
gera_fundo_icms_normal(mproc_id,mcod_empresa, mcod_estab, p_periodo, p_grp_imp, p_uf_estab, '1');
END IF;

END;








# 10. Campos Necessários para Requisição de Envio

Abaixo estão os campos obrigatórios e opcionais exigidos para a integração, com seus respectivos formatos e origens na base de dados da Tax One.

# 10.1 De/PARA integração DOOTAX – Campos para Requisição de Envio:




# 11. Melhorias e Diferenciais na Jornada do Usuário

Para otimizar a experiência dos usuários, recomendamos implementar os seguintes itens:

# 11.1. Controle de Versão
Registrar a versão da API e manter um histórico de atualizações.
Exemplo: Versão 1.0 - Lançamento inicial - Versão 1.1 - Inclusão do campo "cod_mun_favorecido"


# 11.2. Segurança na Integração

Utilizar tokens de autenticação para garantir acesso seguro.
Aplicar validação de dados para evitar ataques como SQL Injection.
Restringir acessos via IP autorizado ou credenciais personalizadas.





# 11.3. Detalhamento de Requisições e Respostas

Indicar os métodos HTTP utilizados (POST, GET, etc.).
Exemplificar as respostas da API para sucesso e erro.

# 11.4. Monitoramento e Suporte
Possibilitar acompanhamento dos envios através de logs e dashboards.


# 12. Conclusão

A integração da API do Tax One com o Dootax oferece um fluxo automatizado e eficiente para a importação e processamento de guias de pagamento de tributos. A padronização dos campos de requisição e a implementação de validações estruturadas garantem maior confiabilidade e segurança na transmissão dos dados, reduzindo erros operacionais.

A funcionalidade Executar desempenha um papel essencial ao permitir a automação do processamento das guias importadas, reduzindo a necessidade de intervenção manual e agilizando o cumprimento das obrigações fiscais.

Além disso, as melhorias sugeridas, como feedback em tempo real, logs detalhados e flexibilidade no envio de dados, aprimoram a experiência do usuário, tornando o sistema mais intuitivo e transparente.

Com essas otimizações, espera-se um ganho expressivo em produtividade, segurança e conformidade fiscal, proporcionando uma solução robusta e alinhada às necessidades das empresas.




= = = = = =

---

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS XXX | Paloma Dias Brondi | Novo Módulo Integração Guias de Pagamento DOOTAX - Função EXECUTAR e Procedures Relacionadas | 13.02.2025 |
|  |  |  |  |


---

| Parâmetro | Descrição |
| --- | --- |
| p_periodo | Representa um período de tempo para cálculos ou consultas. |
| p_grp_imp | Grupo de imposto utilizado na execução de regras fiscais. |
| p_uf_estab | Unidade federativa do estabelecimento. |
| p_cod_estab | Código do estabelecimento, do tipo Lib_Proc.Vartab. |


---

| Dependência | Finalidade |
| --- | --- |
| LIB_PROC | Criação de processos, logs e manipulação de parâmetros. |
| LIB_PARAMETROS | Recupera e salva parâmetros como códigos de empresas e usuários. |
| FPAR_PARAMETROS | Tabela de configurações usada em consultas SQL. |
| PRT_DIRETORIOS_SERVIDOR | Valida existência de diretórios. |
| FLUX_HEINEKEN_ESTAB_TEMP_CPROC | Armazena dados temporários de estabelecimentos. |


---

| Parâmetro | Descrição |
| --- | --- |
| pCod_Tp_Dt | Tipo de cálculo para a data (ex.: "DU" para dia útil, "DF" para data fixa). |
| pDia_Vc | Dia base para o cálculo. |
| pMesano | Período no formato mês/ano. |
| pIdent_estado | Identificador do estado. |
| pCod_Municipio | Código do município. |


---

| Campos DOOTAX | Dados do campo | Formato | Obrig. | DE/PARA TAX ONE |
| --- | --- | --- | --- | --- |
| cod_empresa | Código da empresa conforme informado no cadastro da empresa no Dootax | Alfanumérico | Sim | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos  SAFX 09-Itens Notas Fiscais de Serviços  Tabelas de Apurações |
| cod_estab | Código do estabelecimento conforme informado no cadastro da empresa no Dootax | Alfanumérico |  | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos  SAFX 09-Itens Notas Fiscais de Serviços  Tabelas de Apurações |
| periodo | Data da ocorrência ou do encerramento do período | Data | Sim | SAFX07 - Arquivo de Notas Fiscais  SAFX08 - Itens Notas Fiscais Mercadorias e Produtos  SAFX09 - Itens Notas Fiscais de Serviços  Tabelas de Apurações   SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração. |
| cod_arrecadacao | Tipo de documento utilizado na arrecadação, conforme cadastro no Dootax. (ex.: DARF; GNRE) | Número | Sim | SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração do ICMS |
| cod_receita | Código da receita que está sendo paga, de acordo com o tipo de documento de arrecadação. | Número | Sim | SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração do ICMS |
| det_receita | Código do detalhamento da receita. | Alfanumérico | Sim | SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração. |
| num_doc_origem | Número do documento que deu origem ao pagamento. | Número |  | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos  SAFX 09-Itens Notas Fiscais de Serviços  Tabelas de Apurações |
| Serie | Série do documento | Alfanumérico |  | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos  SAFX 09-Itens Notas Fiscais de Serviços |
| uf_favorecida | Sigla da UF favorecida. | Texto | Sim | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos |
| cnpj_favorecido | CNPJ do favorecido. Esse campo é usado para identificar o favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros. | Número |  | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos  SAFX 09-Itens Notas Fiscais de Serviços |
| ie_favorecida | Inscrição Estadual do favorecido.  Esse campo é usado para identificar o favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros. | Número |  | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos |
| vlr_principal | Valor principal do título. | Número | Sim | SAFX07 - Arquivo de Notas Fiscais  SAFX08 - Itens Notas Fiscais Mercadorias e Produtos  SAFX09 - Itens Notas Fiscais de Serviços  Tabelas de Apurações   SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração. |
| data_vencimento | Data do Vencimento. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração. | Data | Sim | SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração. |
| data_pagamento | Data do Pagamento. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração. | Data |  | SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração. |
| vlr_multa | Valor da multa quando o pagamento ocorrer em atraso. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração. | Número |  | SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração. |
| vlr_juros | Valor dos juros quando o pagamento ocorrer em atraso. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração. | Número |  | SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração. |
| info_complementar | Informação complementar a ser incluída na emissão do título a pagar. | Alfanumérico |  | SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração |
| vlr_fecp | Valor do recolhimento ao Fundo Estadual de Combate à Pobreza. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr_principal com o valor da guia excluído o valor do recolhimento ao FECP. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr_principal. | Número |  | SAFX 08 - Itens Notas Fiscais Mercadorias e Produtos |
| vlr_fecp_multa | Valor da multa sobre o recolhimento ao Fundo Estadual de Combate à Pobreza, quando o pagamento ocorrer em atraso. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr_multa com o valor da multa excluído o valor da multa referente ao FECP. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr_multa. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração. | Número |  | SAFX 08 - Itens Notas Fiscais Mercadorias e Produtos |
| vlr_fecp_juros | Valor dos juros sobre o recolhimento ao Fundo Estadual de Combate à Pobreza, quando o pagamento ocorrer em atraso. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr_juros com o valor dos juros excluído o valor dos juros referente ao FECP. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr_juros. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração. | Número |  | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos |
| convenio | Convênio ou protocolo ICMS que regulamenta a forma de recolhimento do tributo. Esse campo é utilizado na geração da GNRE por apuração. | Número |  | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos |
| cod_produto | Na emissão da GNRE, algumas UFs exigem o preenchimento do código do produto no recolhimento do ICMS por apuração. Consulte a UF para obter a lista de códigos de produtos válidos. | Alfanumérico |  | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos |
| chave_dfe | Chave de acesso do documento fiscal:  Para documentos fiscais eletrônicos, informar a chave com 44 dígitos. | Alfanumérico |  | SAFX 07-Arquivo de Notas Fiscais |
| cad_part | Informações do participante (destinatário, emitente, transportador, etc). Esse campo deve ser informado quando os dados do participante são exigidos na emissão ou visualização da guia.  Ver layout do campo na aba "Cadastros", tabela "cad_part". | Alfanumérico |  | SAFX04-Arquivo de Cadastro de Pessoas Físicas/Jurídicas  SAFX 07-Arquivo de Notas Fiscais  SAFX 08- Itens Notas Fiscais Mercadorias e Produtos  SAFX 09 -Itens Notas Fiscais de Serviços |
| cod_mun_favorecido | Código do municipio - Este campo deve ser informado quando a guia a ser emitida utilize o código de município diferente do que está no cadastro da empresa | Número |  | SAFX 07-Arquivo de Notas Fiscais  SAFX 09 -Itens Notas Fiscais de Serviços |
| vlr_outros | Valor de outras despesas que devam ser utilizadas na geração da guia | Número |  | SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração |
| vlr_base_calc | Valor de base de cálculo. Utilizado nas guias que utilizam deste valor para calcular o valor da guia | Número |  | SAFX 07- Arquivo de Notas Fiscais  SAFX 08 -Itens Notas Fiscais Mercadorias e Produtos  SAFX 09 - Itens Notas Fiscais de Serviços  Tabela de Apuração |
| campos_extras | Utilizado para enviar um json com campos adicionais | Alfanumérico |  | SAFX07 - Arquivo de Notas Fiscais  SAFX08 - Itens Notas Fiscais Mercadorias e Produtos  SAFX09 - Itens Notas Fiscais de Serviços  Tabelas de Apurações   SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração. |
| conta_contabil | Código da empresa conforme informado no cadastro da empresa no Dootax | Alfanumérico |  | SAFX 2002- Tabela do Plano de Contas |

# Solutions Index

Documentacao de solucoes implementadas (Compound Engineering).

## Solucoes

| WI | PR | Modulo | Titulo | Data |
|----|-----|--------|--------|------|
| [951077](951077.md) | #12155 | Municipal/NFSE | Natureza operacao ABACO Manaus 16→19 | 2026-03-08 |
| [1036825](1036825.md) | #12156 | Federal/OTF | Email+PDF Comprovante Retencao | 2026-03-08 |
| [1037321](1037321.md) | #12157 | Basicos/Admin | Universal ID extenso VARCHAR2(40→100) | 2026-03-08 |
| [1060768](1060768.md) | #12159 | SPED Fiscal/CIAP | G126 duplicacao extemporaneo integral | 2026-03-08 |
| [1061569](1061569.md) | #12158 | Federal/IR | Informe PF cod 5204+3208 agrupamento | 2026-03-08 |
| [1053341](1053341.md) | #12160 | Estadual/GIA-ST | Jasper: YYYY vs yyyy, Campo 13 ICMS-ST, width datas | 2026-03-08 |
| [1053976](1053976.md) | #12161 | Basicos/Import | SAFX236 rejeita IND_TP_CORRECAO=1 (Bloco K) | 2026-03-08 |
| [1053380](1053380.md) | #12162 | SPED/ECD/Balancete | Balancete XLSX saldo anterior sit. especial + anual | 2026-03-08 |
| [1058919](1058919.md) | #160 (t1dw) | Basicos/DW/Java | X08ItensMerc faltando VLR_BASE_ICMSS | 2026-03-08 |
| [1046488](1046488.md) | - (investigado) | Federal/OTF/IR | Informe 3208+1889 separados (aguarda OK funcional) | 2026-03-08 |
| [1058225](1058225.md) | #12163 | SPED/ECD/I200-I250 | RAISE escapa loops aninhados (conta inativa) | 2026-03-08 |
| [1064546](1064546.md) | #12169 | SPED/EFD-PIS-COFINS | CSTs 55/61 ausentes nas views de credito | 2026-03-09 |
| [910525](910525.md) | #12180 | SPED/ECD/Livro Razao | UTL_FILE.FOPEN com path local Windows | 2026-03-09 |
| [1039643](1039643.md) | #12184 | Basicos/Import/OBI | MERGE dupla-contagem tot_lidos no log OBI | 2026-03-09 |
| [1058225](1058225.md) | #12163 | SPED/ECD/I200-I250 | RAISE escapa loops aninhados (flag+GOTO fix) | 2026-03-09 |
| [1062301](1062301.md) | #12185 | Basicos/Relatorios | Balancete saldo anterior MAX→LAST_DAY | 2026-03-09 |
| [1052913](1052913.md) | #12186 | Federal/DMED | UNION→UNION ALL performance (15 conversoes) | 2026-03-09 |
| [1028814](1028814.md) | #12189 | SPED/EFD-PIS-COFINS | UNION→UNION ALL performance (6 conversoes) | 2026-03-10 |
| [1030785](1030785.md) | #12190 | Basicos/SAFCOMP/X100 | String(NULL) NullPointerException Appeon | 2026-03-10 |
| [1052042](1052042.md) | #12194 | Basicos/DocFiscal | Flag CAPA ib_recuperado → ind_ins_del UPDATE | 2026-03-10 |
| [1058668](1058668.md) | #12195 | Basicos/LIB_IMPORT | UNION→UNION ALL cursor c_prog Job Servidor | 2026-03-10 |
| [1066543](1066543.md) | - (sem PR) | Basicos/Import/SAFX3007 | Mapeamento UF/MUN invertido — procedures desatualizadas | 2026-03-10 |
| [1066293](1066293.md) | - (sem PR) | Basicos/Import/SAFX3009 | Erro Codigo Servico nao cadastrado — procedures desatualizadas (DDL_MFS848597) | 2026-03-11 |
| [1067285](1067285.md) | #12221 | Estadual/CtrlMerc | to_date(DATE,'dd/mm/yy') → trunc() em relatórios prazos vencidos | 2026-03-11 |
| [1062650](1062650.md) | #12164 | Estadual/CIAP | DIFAL negativo GREATEST(...,0) em SAF_CIAP_AQUISICAO | 2026-03-12 |
| [1062781](1062781.md) | #12258 | Basicos/ReportFiscal | Performance SAF_RF_NF_ICMS_DIFAL (SUBSTR,NVL,FORALL,indice) | 2026-03-12 |
| [1071002](1071002.md) | #12261 | Municipal/DMS Manaus | Filtrar prestadores do mesmo município do estabelecimento | 2026-03-12 |
| [831923](831923.md) | #12285 | SPED/EFD-PIS-COFINS | Mensagem aviso Automacao Devolucao Venda Reg Cumulativo (re-trabalho) | 2026-03-14 |
| [1058914](1058914.md) | - (PL/SQL+DDL) | Federal/IPI/DataMart | Reemissao IPI nao encontra livros (ict_lvr_reimp) | 2026-03-14 |

## Patterns Recorrentes

### Produto Cartesiano em JOINs
- **WI 1060768**: JOIN entre tabelas com granularidades diferentes (Efd_Bem_Ciap x APT_CALC_BEM_EXTEMP)
- **Fix**: Adicionar subquery MIN() para garantir 1 linha por chave

### Chave de Agrupamento Incompleta
- **WI 1061569**: Agrupamento por CPF sem considerar grupo_retencao
- **Fix**: Incluir TODOS os campos que definem unicidade

### Truncamento Silencioso de VARCHAR2
- **WI 1037321**: cod_usuario VARCHAR2(40) truncando IDs de 46+ chars
- **Fix**: Expandir para VARCHAR2(100) em variaveis, tipos e tabelas

### Verificacao de Pre-condicoes
- **WI 1036825**: enviarEmail() sem verificar se PDF existe
- **Fix**: Checar retorno de gravarRel() antes de enviar

### YYYY vs yyyy em Java SimpleDateFormat
- **WI 1053341**: pattern "MM/YYYY" (week-based year) mostra ano errado na virada dez→jan
- **Fix**: Usar "yyyy" (calendar year). Grep por YYYY em todos os Jasper

### Variavel Jasper com campo errado
- **WI 1053341**: Campo 13 usava vlr_icms (proprio) ao inves de vlr_icmss_ret (ST)
- **Fix**: Verificar formula da variavel vs campo esperado na tabela

### Width insuficiente em campos Jasper
- **WI 1053341**: width=36 trunca dd/MM/yyyy com font size 8
- **Fix**: Minimo ~50px para datas completas

### Inconsistencia entre validacoes de capa/item
- **WI 1053976**: X235 aceita IND_TP_CORRECAO='1', X236 nao aceita
- **Fix**: Comparar validacoes de ambas procedures ao alterar. Usar NOT IN com cuidado

### LAST_DAY() assume meses completos
- **WI 1053380/1062301**: Subqueries de saldo usavam LAST_DAY(pDataIni) que falha em periodos parciais ou anuais
- **Fix**: Usar data real (Pdatafim) ou MIN(DATA_SALDO) dentro do periodo

### Campo JPA faltando entre Tmp e permanente
- **WI 1058919**: TmpX08ItensMerc tinha VLR_BASE_ICMSS mas X08ItensMerc nao
- **Fix**: Manter models Tmp* e permanentes sincronizados em campos

### BETWEEN com DATE Oracle em execucao por dia
- **WI 1058225**: `BETWEEN date AND date` (mesmo dia) exclui registros com hora > 00:00:00
- **Fix**: Usar `>= date AND < date + 1` para incluir dia inteiro. Preserva uso de indice

### Consolidacao vs Separacao de codigos de retencao
- **WI 1046488**: Codigos 3208+1889 devem ser consolidados no mesmo informe (vs 3208+5204 que devem ser separados)
- **Fix**: Logica condicional na camada Java (CedulaDDAO) para normalizar grupo_retencao por codigo

### Valores duplicados em listas IN (CSTs/codigos)
- **WI 1064546**: CST 51 duplicado + CSTs 55/61 ausentes no filtro de 3 views de credito EFD
- **Fix**: Verificar sequencia completa e ordenada. Comparar contra tabela oficial (Guia Pratico EFD)
- **Atencao**: Views irmas (SERV/PROD/FRET) compartilham mesmo filtro — corrigir TODAS

### UTL_FILE.FOPEN com path local em vez de Oracle Directory
- **WI 910525**: PB passa path Windows local (C:\Users\...) ao UTL_FILE.FOPEN que espera Oracle Directory Object
- **Fix**: Consultar `PRT_DIRETORIOS_SERVIDOR` (COD_MODULO = 'JOB SERVIDOR') para obter DIRECTORY_NAME
- **Padrao**: Mesmo usado em SAF_ATUALIZA_DIRECTORY_TAXBR, JD_FNC_GET_DIR_CPROC, e integradores
- **Atencao**: Manter assinatura da procedure para backward compatibility com tela PB

### MERGE com multiplos SET inflando contadores
- **WI 1039643**: MERGE somava qtde_regs_dupl em tot_lidos E tot_ignorados, mas tot_lidos ja estava correto
- **Fix**: Verificar se CADA campo no SET realmente precisa da mesma soma. Duplicados → ignorados, nao lidos
- **Padrao**: Ao corrigir MERGE, buscar TODOS os blocos similares no package (grep pelo pattern)

### RAISE em loops aninhados propagando alem do esperado
- **WI 1058225**: RAISE Prox_Lancto_w dentro do loop INTERNO escapava para handler do loop EXTERNO
- **Fix**: Usar flag (Exist_w) + GOTO no nivel do loop. GOTO nao pode estar dentro de EXCEPTION block
- **Regra**: NULL; obrigatorio apos label antes de END LOOP em PL/SQL
- **Atencao**: Fixes sobre fixes — MFS534383 adicionou logica correta, mecanismo errado

### UNION vs UNION ALL em subqueries ESTAB
- **WI 1052913**: Subqueries ESTAB com lCentralizador sao mutuamente exclusivas (0 ou 1)
- **WI 1028814**: EFD PIS/COFINS — ROWIDs (unicos por definicao), ind_ajuste P/N, registro tipos
- **WI 1058668**: LIB_IMPORT cursor c_prog — ind_multi_empresa NULL/'N' vs 'S'
- **Fix**: Converter para UNION ALL. Pattern recorrente em DMED, DIRF, EFD, e Job Servidor
- **Regra de decisao**: Condicoes exclusivas → UNION ALL; GROUP BY com SUM → UNION ALL; ROWIDs → UNION ALL; linhas individuais com sobreposicao → manter UNION
- **Excecao**: SELECT UNIQUE com window functions (ex: EPC_DEM_APUR_EXCEL) — duplicatas genuinas, manter
- **Impacto**: Elimina SORT UNIQUE, reduz consumo de TEMP tablespace

### String(NULL) em Appeon Web (NullPointerException)
- **WI 1030785**: String(NULL, 'yyyymmdd') funciona em PB Desktop, NPE em Appeon Web (Java runtime)
- **Fix**: Sempre inicializar variavel datetime antes de String(). Usar fallback para data_ini/data_fim
- **Atencao**: Verificar consistencia com server-side PL/SQL (ix100.sql ja tinha fallback)

### Desalinhamento posicional apos ALTER TABLE (DDL)
- **WI 1066543**: DDL_MFS848597 adicionou colunas MUN apos UF na SAFX3007/X3007_DOCTO_FISCAL_RT
- SAF_IB_X3007 (leitura posicional via SAF_IB_PROC_LINHA) ficou desalinhada sem recompilacao
- **WI 1066293**: DDL_MFS848597 adicionou parametros P_ALIQ_TRIB_REG_IBS_MUN e P_VLR_TRIB_REG_TRIB_IBS_MUN a OL_IMP_X3009 (posicoes 49-50)
- Sintoma diferente: erro "Codigo de Servico nao cadastrado" em vez de inversao UF/MUN; SAFX3009%ROWTYPE protege dados mas nao protege assinatura da procedure
- **Fix**: Recompilar procedures na ordem bottom-up (folhas→orquestradores)
- **Prevencao**: Preferir named parameters em chamadas a OL_IMP. Acesso por nome (l_row(i).campo) e imune
- **Atencao**: DDL_MFS848597 afeta TODA a familia X3007/X3008/X3009 — se uma falhar, verificar as demais
- **Atencao**: Verificar DDL anterior vs atual para entender parametros/colunas adicionadas

### X3008 (Mercadorias/UF) vs X3009 (Servicos/MUN) — BY DESIGN
- **WI 1066543**: Gap de colunas ALIQ_IBS_TRIB_REG_UF / VLR_TRIB_REG_TRIB_IBS_UF no X3009
- Reforma Tributaria IBS/CBS: mercadorias = IBS UF (estadual), servicos = IBS MUN (municipal)
- Consistente em todas as 6 camadas: DDL, DDL TMP, SAFX, OL_IMP, SAF_IMP, PKG_FPROC
- **Regra**: Antes de assumir bug, verificar se diferenca entre X3008/X3009 e intencional

### to_date() sobre campo DATE no Oracle
- **WI 1067285**: `to_date(campo_DATE, 'dd/mm/yy')` em DataWindows causava DATE→VARCHAR2→DATE com perda de século
- **Fix**: Substituir por `trunc(campo_DATE)` — remove parte horária sem conversão intermediária
- **Regra**: NUNCA usar to_date() em coluna que já é DATE. Usar trunc() para aritmética de datas
- **Diagnóstico**: Comparar relatório irmão que funciona (Pendências usava trunc, Vencidos usava to_date)
- **Atencao**: DataWindow filter client-side (`date(campo) < date(Today())`) descarta silenciosamente — verificar query E filter

### DIFAL negativo por formula de base dupla (CIAP)
- **WI 1062650**: SAF_CIAP_AQUISICAO calcula VLR_DIF_ALIQ_W com subtracao que pode resultar negativo
- **Fix**: GREATEST(..., 0) em TODAS as formulas de calculo. DIFAL nunca e negativo por definicao legal
- **Atencao**: MS com FECP precisa de duplo GREATEST (base + subtracao FECP)
- **Atencao**: IND_BASE_W='4' atribui diretamente BASE_DIF_W (VLR_OUTROS1) — avaliar se precisa protecao
- **Impacto**: Valor negativo propaga para APT_CRED_CFO_102 e SPED Fiscal Bloco G

### Performance: SUBSTR/NVL em WHERE impedem indice
- **WI 1062781**: `substr(COD_CFO,1,1) in ('2','6')` e `NVL(SITUACAO,'N') <> 'S'` forcavam full scan
- **Fix**: SUBSTR → `LIKE 'X%'` (range scan); NVL → `(col IS NULL OR col <> val)` (indexavel)
- **Atencao**: Qualquer funcao aplicada a coluna no WHERE impede uso de indice. Reescrever sem funcao

### Performance: DELETE/INSERT row-by-row em tabelas temporarias de relatorio
- **WI 1062781**: Cursor FOR + DELETE individual; WHILE loop + INSERT individual (FORALL comentado)
- **Fix**: DELETE unico com WHERE; FORALL SAVE EXCEPTIONS com bulk_errors handler
- **Regra**: FORALL precisa de bloco BEGIN...EXCEPTION...END explicito. COMMIT fora do bloco
- **Atencao**: Ao reabilitar FORALL comentado, verificar se handler bulk_errors estava correto

### Filtro ausente em cursor consumidor
- **WI 1071002**: Cursor retornava COD_MUNICIPIO_PFJ e COD_MUNICIPIO_ESTAB mas procedure não comparava
- **Fix**: Adicionar verificação na procedure consumidora, seguindo pattern existente (IgnorarRegistro)
- **Regra**: Quando cursor já tem os campos necessários, o filtro deve ser na procedure, não no cursor

### Flag propagacao INSERT vs UPDATE em telas PB
- **WI 1052042**: ib_uo_item_alterado so setado para itens, nao para CAPA
- **Fix**: Incluir ib_recuperado (documento existente) na condicao
- **Regra**: Em telas de manutencao, ib_recuperado=TRUE → qualquer gravacao deve ser UPDATE
- **Atencao**: Testar cenarios isolados (so CAPA, so ITENS, ambos, novo documento)

### SELECT-INTO para forcar refresh de UI em loops longos (PB)
- **WI 831923**: Loop de geracao de ajustes congelava tela por horas sem feedback
- **Fix**: `select :var into :var from empresa where rownum = 1;` forca round-trip e libera message queue
- **Frequencia**: Mod(10) para loops com centenas/milhares de iteracoes (~1ms overhead por round-trip)
- **Regra**: NUNCA commitar MessageBox de debug — trava processo silenciosamente em producao

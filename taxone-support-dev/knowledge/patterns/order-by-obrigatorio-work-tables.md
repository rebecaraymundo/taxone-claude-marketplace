# Pattern: ORDER BY Obrigatorio em Work Tables

## Classificacao
**Regra defensiva** — Prevencao de bugs nao-deterministicos

## Descricao

O Oracle NAO garante a ordem dos registros retornados por uma query sem clausula
`ORDER BY`, mesmo que:
- A query tenha `GROUP BY` (agrupa, mas nao ordena)
- Exista indice nas colunas (Oracle PODE usar o indice, mas nao e obrigado)
- Em execucoes anteriores os dados vieram "na ordem certa"

Em work tables temporarias (como `SPED_I310_I355_WORK`, `TMP_*`), a ordem pode variar
entre execucoes dependendo de:
- Carga do servidor
- Reorganizacao de dados em memoria (PGA/SGA)
- Estatisticas do otimizador
- Paralelismo

## Sintoma

- Resultado "as vezes" correto, "as vezes" incorreto
- Impossivel reproduzir consistentemente
- O mesmo processo roda N vezes, algumas com sucesso e outras nao
- Nenhum log de erro (falha silenciosa)

## Regra

**Todo cursor FOR ou OPEN que leia de work tables DEVE ter ORDER BY explicito,
usando as mesmas colunas do GROUP BY (quando aplicavel).**

```sql
-- ERRADO:
FOR r IN (SELECT ... FROM WORK_TABLE
           WHERE proc_id = p_proc_id
           GROUP BY col1, col2, col3) LOOP

-- CORRETO:
FOR r IN (SELECT ... FROM WORK_TABLE
           WHERE proc_id = p_proc_id
           GROUP BY col1, col2, col3
           ORDER BY col1, col2, col3) LOOP
```

## Impacto de Performance

**Zero ou negligivel** quando:
- O indice ja cobre as colunas do ORDER BY (INDEX RANGE SCAN sem SORT adicional)
- O GROUP BY ja obriga o Oracle a agrupar (SORT GROUP BY)
- O ORDER BY usa as mesmas colunas do GROUP BY (SORT GROUP BY NOSORT)

## Verificacao

```sql
-- Verificar se o indice cobre as colunas do ORDER BY:
SELECT index_name, column_name, column_position
  FROM all_ind_columns
 WHERE table_name = 'SPED_I310_I355_WORK'
 ORDER BY index_name, column_position;
```

## Ocorrencias no TAX ONE

| WI | Cursor | Tabela | Fix |
|----|--------|--------|-----|
| #1027128 | c_Encerr | SPED_I310_I355_WORK | Adicionado ORDER BY Data_Lancto, Cod_Conta, Grupo_Conta, Cod_Custo, Grupo_Custo |

## Como Detectar

Buscar cursores com GROUP BY sem ORDER BY em work tables:
```bash
# No repo taxone_dw, buscar packages com GROUP BY sem ORDER BY subsequente
grep -B5 "GROUP BY" artifacts/sp/**/*.pck | grep -v "ORDER BY"
```

Nota: Nem todo GROUP BY precisa de ORDER BY — apenas quando a ORDEM de processamento
importa para o resultado (ex: geracao de arquivo sequencial, acumuladores, flags dependentes
da sequencia de leitura).

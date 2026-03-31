# Pattern: RAISE em Loops Aninhados PL/SQL

## Classificacao
**Anti-pattern** — Bug recorrente no TAX ONE

## Descricao

Em PL/SQL, `RAISE` propaga a excecao ate o handler `EXCEPTION` mais proximo que a capture.
Quando usado dentro de loops aninhados com `BEGIN/EXCEPTION/END`, o RAISE pode escapar
mais niveis do que o pretendido, descartando iteracoes validas.

## Sintoma

- Registros "desaparecem" do resultado sem nenhum log de erro
- Comportamento intermitente (depende da ordem de processamento)
- Impossivel reproduzir em ambiente de suporte (dados diferentes)

## Exemplo (bug real)

```sql
-- Loop EXTERNO: lancamentos
WHILE c_lancto%FOUND LOOP
  BEGIN
    -- Loop INTERNO: partidas do lancamento
    WHILE r_lancto.num_lancamento = lancamento_atual LOOP
      BEGIN
        SELECT count(1) INTO Exist_w FROM tabela WHERE condicao;
        IF Exist_w = 0 THEN
          RAISE Prox_Lancto_w;  -- BUG: escapa ambos os loops!
        END IF;
      EXCEPTION
        WHEN NO_DATA_FOUND THEN
          RAISE Prox_Lancto_w;  -- BUG: idem
      END;
      -- ... processamento da partida ...
    END LOOP;
  EXCEPTION
    WHEN Prox_Lancto_w THEN  -- Handler no loop EXTERNO
      FETCH c_lancto INTO r_lancto;  -- Pula para proximo lancamento
  END;
END LOOP;
```

O RAISE dentro do loop INTERNO propaga para o handler do loop EXTERNO,
descartando TODAS as partidas restantes do lancamento.

## Correcao (pattern correto)

```sql
-- Usar flag + GOTO ao inves de RAISE
WHILE r_lancto.num_lancamento = lancamento_atual LOOP
  BEGIN
    SELECT count(1) INTO Exist_w FROM tabela WHERE condicao;
  EXCEPTION
    WHEN NO_DATA_FOUND THEN
      Exist_w := 0;
  END;

  IF Exist_w = 0 THEN
    FETCH c_lancto INTO r_lancto;  -- Avanca cursor antes do GOTO
    GOTO skip_partida;  -- Pula apenas esta partida
  END IF;

  -- ... processamento da partida ...

  <<skip_partida>>
  NULL;  -- Obrigatorio: label nao pode ser ultima instrucao antes de END LOOP
END LOOP;
```

## Regras

1. **Nunca usar RAISE para skip de iteracao** em loops aninhados com BEGIN/EXCEPTION/END
2. **Separar SELECT em bloco proprio** — GOTO nao pode estar dentro de EXCEPTION handler
3. **Sempre FETCH antes do GOTO** — se o cursor e manual (nao FOR), avancar antes de pular
4. **NULL; apos label** — PL/SQL exige statement apos label antes de END LOOP

## Ocorrencias no TAX ONE

| WI | Package | Descricao |
|----|---------|-----------|
| #1058225 | SAF_SPED_CONTABIL_FPROC | RAISE descartava I200/I250 (lancamentos) |
| #1027128 | SAF_SPED_CONTABIL_FPROC | Mesmo RAISE descartava lancamentos de encerramento (I350/I355) |

## Como Detectar

Grep no repo:
```bash
grep -n "RAISE.*Prox_Lancto\|RAISE.*next_record\|RAISE.*skip" artifacts/sp/**/*.pck
```

Se o RAISE estiver dentro de um loop WHILE/FOR que esta dentro de outro loop,
e o handler EXCEPTION estiver no loop externo → provavelmente bug.

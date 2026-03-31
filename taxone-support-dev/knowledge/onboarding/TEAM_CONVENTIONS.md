# Convencoes do Time TAX ONE

Regras universais que todo desenvolvedor deve seguir ao usar o taxone-support-dev.

## Branch Naming

- Formato: `MFS{work-item-id}` a partir de DEV (no repo taxone_dw)
- Exemplo: `MFS1058668`
- Correcoes adicionais na mesma WI: `MFS{WI_ID}a`, `MFS{WI_ID}b`, etc.
- Vale para todos os repositorios (taxone_dw, taxone-support-dev, etc.)

## Formato de Commit e PR (GitHub)

| Campo | Formato | Exemplo |
|-------|---------|---------|
| Titulo do commit | `MFS{WI_ID} - {descricao}` | `MFS1058668 - Performance LIB_IMPORT cursor c_prog` |
| Titulo da PR | `[DEV] MFS{WI_ID} - {descricao}` | `[DEV] MFS1058668 - Performance LIB_IMPORT cursor c_prog` |
| Ultima linha do body | `AB#{WI_ID}` | `AB#1058668` |

**Nota**: `[DEV]` aparece SOMENTE no titulo da PR, NAO no commit.

## RC Baseline (Obrigatorio)

Antes de implementar qualquer mudanca no taxone_dw:
1. Criar branch a partir de DEV: `git checkout -b MFS{WI_ID} DEV`
2. Verificar divergencia: `git diff --stat RC..DEV -- "path/do/arquivo"`
3. Se diverge: restaurar versao RC: `git show RC:"path" > "path"`
4. Implementar sobre a versao RC (producao estavel)

**Motivo**: DEV pode conter codigo nao testado. RC e o estado de producao validado.

## Compilacao e Testes

1. **SEMPRE compilar PL/SQL** no banco (porta 1521) antes de qualquer teste
2. **SEMPRE rodar SuiteAutomation** apos implementacao
3. **SEMPRE executar testes** — Bug, Feature, qualquer tipo. Fluxo minimo:
   - Cenario base (comportamento atual preservado)
   - Cenario com a alteracao ativa
   - Nao-regressao
4. **Evidencias na WI do ADO**: Anexar como Attachments + postar na Discussion

## Tags ADO

| Tag | Quando usar |
|-----|-------------|
| `SUST-IA-CLAUDE` | Toda WI atualizada por analise da IA |
| `SUST-IA-CLAUDE-NOT-BUG` | WI avaliada como "Not a Bug" |
| `SUST-IA-CLAUDE-ANALISE` | WI precisa de analise adicional |
| `SUST-IA-CLAUDE-REGRA` | WI envolve regra de negocio |

## Release Notes

- Campo: `Custom.DescriptionofReleaseNotes` no ADO
- Formato: Carta do Patch (texto simples, bold nos labels, `<br>` para quebras)
- **Somente descricao funcional** — sem detalhes tecnicos (variaveis, px, nomes de campo)
- Nao sobrescrever se ja estiver preenchido

## PR Reviewers (round-robin)

Ao criar PR no taxone_dw, adicionar UM reviewer em rotacao:
- Daniel Oliveira (`DanielOliveira73`)
- Renato Ramos (`RenatoRamosTR`)
- Marcus Britto (`marcusbrittoTR`)

Verificar quem revisou por ultimo e escolher quem esta ha mais tempo sem revisar.

## DDL

- NUNCA alterar DDL antiga
- Sempre criar DDL nova: `DDL_MFS{WI_ID}.sql`
- DDLs sao imutaveis apos criacao

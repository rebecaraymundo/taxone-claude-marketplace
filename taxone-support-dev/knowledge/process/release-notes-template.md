# Template: Carta do Patch - Release Notes

Template para o campo `Custom.DescriptionofReleaseNotes` no Azure DevOps.
Formato texto simples com tags minimas de formatacao (campo e rich text).

## Formato

```
<b>Carta do Patch: DW e TAX ONE</b><br><br> <b>Modulo:</b> {{MODULO}}<br> <b>Menu:</b> {{MENU}}<br>        {{DESCRICAO}}
```

## Variaveis

- `{{MODULO}}` - Ex: Municipal > Manaus, SPED > EFD - Escrituracao Fiscal Digital das Contribuicoes
- `{{MENU}}` - Ex: Obrigacoes > Meio Magnetico, Obrigacoes > Geracao dos Registros
- `{{DESCRICAO}}` - Descricao funcional do ajuste/correcao (indentado com 8 espacos)

## Regras

- `<b>` nos labels: "Carta do Patch: DW e TAX ONE", "Modulo:", "Menu:"
- `<br><br>` (linha em branco) apos o titulo
- `<br>` para cada quebra de linha
- Modulo e Menu com 1 espaco de indentacao apos `<br>`
- Descricao com 8 espacos de indentacao apos `<br>`
- Separador de caminho: `>`
- Extrair modulo/menu/descricao dos dados da WI (titulo, descricao, componente)
- **SOMENTE descricao funcional sucinta** — SEM detalhes tecnicos (nomes de variaveis, px, nomes de campos Jasper, patterns, nomes de arquivos)
- Se campo ja preenchido na WI, NAO sobrescrever

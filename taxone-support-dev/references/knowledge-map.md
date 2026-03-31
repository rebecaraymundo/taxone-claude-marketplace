# Mapeamento AreaPath/Keywords -> Feature Knowledge

## Como inferir a feature

Para cada work item, analisar `WORK_ITEM_AREA` (Area Path) e keywords no titulo/descricao/repro steps.
Usar a tabela abaixo para mapear para o arquivo de knowledge correto.

## Area Path do TAX ONE Suporte

Base: `Mastersaf Fiscal Solutions\MFS\TAX ONE\Suporte`

Sub-areas possiveis (verificar conforme projeto):
- `...\Suporte\Apuracao`
- `...\Suporte\Obrigacoes`
- `...\Suporte\Cadastro`
- `...\Suporte\Importacao`
- `...\Suporte\Calculo`
- `...\Suporte\Relatorios`

## Tabela de Mapeamento

| Keyword no AreaPath/Titulo | Knowledge File |
|---------------------------|----------------|
| Apuracao / ICMS / IPI / PIS / COFINS / ISS | apuracao.md |
| Obrigacao / SPED / EFD / GIA / DCTF / DIRF | obrigacoes-acessorias.md |
| Nota Fiscal / NF-e / NFS-e / CT-e | notas-fiscais.md |
| Cadastro / Empresa / Filial / Participante | cadastro.md |
| Importacao / XML / Arquivo / Leitura | importacao.md |
| Calculo / Imposto / Aliquota / Base / Tribut | calculo-impostos.md |
| Relatorio / Consulta / Livro Fiscal | relatorios.md |
| Integracao / API / Web Service / ERP | integracao.md |
| Performance / Lento / Timeout / Index | (usar taxone-dba) |

## Knowledge Disponiveis

Todos os arquivos estao em `${CLAUDE_PLUGIN_ROOT}/knowledge/features/`:

> **NOTA:** A base de conhecimento de features esta vazia inicialmente.
> Usar `/taxone-doc-gen` para gerar documentacao de cada feature incrementalmente.
> Usar `/taxone-compound` para documentar solucoes implementadas.

## Knowledge de Arquitetura

Sempre disponiveis em `${CLAUDE_PLUGIN_ROOT}/knowledge/architecture/`:

- `overview.md` - Visao geral da arquitetura TAX ONE
- `tech-stack.md` - Stack tecnologica completa
- `patterns.md` - Padroes de codigo PL/SQL/PB/Java

## Knowledge de Convencoes

Sempre disponiveis em `${CLAUDE_PLUGIN_ROOT}/knowledge/conventions/`:

- `code-standards.md` - Padroes de codigo da squad
- `naming.md` - Convencoes de nomenclatura

---

## Documentos Matriz de Regras de Negocio (OneDrive)

**Caminho base:** `%USERPROFILE%/Thomson Reuters Incorporated/Requisitos - Mastersaf DW TaxOne/Documento_Matriz/`

Documentos de requisitos e regras de negocio do Mastersaf DW / TAX ONE.
Contem **3.894 documentos** organizados por modulo fiscal.

| Categoria | Docs | Conteudo |
|-----------|------|----------|
| **Basicos** | 983 | Ferramentas, Job Servidor, MasterSAF DW, Parametros, Report Fiscal, Seguranca |
| **Estadual** | 1.037 | Regras por UF (ICMS, ICMS-ST, DIFAL, GIA, SINTEGRA) |
| **SPED** | 765 | EFD Fiscal, EFD Contribuicoes, ECD, ECF, Bloco K |
| **Municipal** | 495 | ISS, NFS-e, GISS, DES |
| **Federal** | 334 | PIS/COFINS, IRPJ/CSLL, DCTF, DIRF, IPI |
| **Especificos** | 176 | Customizacoes por cliente |
| **Gestao_Estrategica** | 63 | Dashboards, KPIs |
| **Conexao_com_Onesource_BR** | 22 | Integracao Onesource |
| **Reforma_Tributaria** | 19 | IBS/CBS, Split Payment |

### Mapeamento Keyword → Documento Matriz

| Keyword no WI | Subcategoria Documento Matriz |
|----------------|-------------------------------|
| DataWarehouse / DW / Consulta / Itens | `Basicos/MasterSAF_DW/` |
| Servico / ISS / NFS-e | `Municipal/` + `Basicos/MasterSAF_DW/Tela_Documento_Fiscal_Servico_TAXONE/` |
| ICMS / ICMS-ST / DIFAL | `Estadual/` |
| PIS / COFINS / Contribuicoes | `Federal/` |
| SPED / EFD / ECD | `SPED/` |
| Importacao / SAFX / Job | `Basicos/Job_Servidor/` |
| Parametros | `Basicos/Parametros/` |
| Relatorio / Report | `Basicos/Report_Fiscal/` |
| Reforma / IBS / CBS | `Reforma_Tributaria/` |

### Documentos Convertidos para Markdown

Para acesso rapido, os documentos MasterSAF_DW foram convertidos para markdown:

**Caminho:** `${CLAUDE_PLUGIN_ROOT}/knowledge/business-rules/MasterSAF_DW/`

- **190 documentos** convertidos (126 tabelas SAFX + 64 outros)
- Indice: `INDEX.md` com mapeamento arquivo → tabela SAFX
- Tabelas principais: SAFX01-SAFX994 (cadastros, documentos fiscais, itens, servicos)
- Subdiretorios: `Tela_Controle_de_Tributos__TAXONE/`, `Tela_Documento_Fiscal_Servico_TAXONE/`

**Prioridade de consulta:** Sempre consultar o markdown primeiro (mais rapido). Se nao encontrar, buscar no OneDrive (caminho base acima).

### Como Usar

Ao analisar impacto em regras de negocio (Fase 4.5), o **taxone-architect** deve:
1. Identificar o modulo fiscal afetado pelo bug/feature
2. Buscar documentos relevantes em `${CLAUDE_PLUGIN_ROOT}/knowledge/business-rules/MasterSAF_DW/`
3. Se nao encontrar em markdown, buscar no OneDrive (caminho base acima)
4. Ler o documento para entender a regra de negocio esperada
5. Comparar com o comportamento do codigo

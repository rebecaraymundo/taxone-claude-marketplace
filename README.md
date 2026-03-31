# TAX ONE Claude Marketplace

Marketplace interno de plugins do Claude Code para o time **TAX ONE** (Mastersaf Fiscal Solutions - Thomson Reuters).

## Plugins Disponiveis

| Plugin | Versao | Descricao |
|--------|--------|-----------|
| [taxone-support-dev](./taxone-support-dev/) | 1.0.0 | Plugin multi-agente para suporte e desenvolvimento TAX ONE. 21 agentes, 9 pipelines, base de conhecimento com 4028 tabelas. |

## Instalacao

### 1. Clonar o repositorio

```bash
git clone https://github.com/tr/taxone_claude_marketplace.git
```

### 2. Instalar o plugin

```bash
claude --plugin-dir ./taxone_claude_marketplace/taxone-support-dev
```

### 3. Verificar

No Claude Code, os slash commands estarao disponiveis:

```
/taxone-auto-fix 1083740
/taxone-bug-fix 1058668
/taxone-us-implement 1079124
```

## Estrutura do Marketplace

```
taxone_claude_marketplace/
├── .claude-plugin/
│   └── marketplace.json        # Registry central de plugins
├── README.md                   # Este arquivo
└── taxone-support-dev/         # Plugin principal
    ├── .claude-plugin/
    │   └── plugin.json         # Metadata do plugin
    ├── agents/                 # 21 agentes especializados
    ├── commands/               # 10 slash commands
    ├── skills/                 # 9 pipelines automatizados
    ├── scripts/                # 45 scripts Python
    ├── knowledge/              # Base de conhecimento
    └── references/             # Documentacao compartilhada
```

## Requisitos

- **Claude Code** (CLI ou IDE extension)
- **Python 3.13+** (para scripts de automacao)
- **Repositorio taxone_dw** clonado localmente
- **Variaveis de ambiente**: `GITHUB_TOKEN`, `ADO_PAT`, `DD_API_KEY`, `DD_APP_KEY`

## Contribuicao

Para adicionar um novo plugin ao marketplace:

1. Criar diretorio na raiz com o nome do plugin
2. Adicionar `.claude-plugin/plugin.json` com metadata
3. Seguir a estrutura: `agents/`, `commands/`, `skills/`, `scripts/`, `knowledge/`
4. Registrar o plugin em `.claude-plugin/marketplace.json`
5. Abrir PR para revisao

## Licenca

Uso interno Thomson Reuters - TAX ONE.

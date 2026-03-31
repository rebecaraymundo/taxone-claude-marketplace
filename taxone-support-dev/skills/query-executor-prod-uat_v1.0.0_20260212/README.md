# Query Executor - Skill Distribution Package

## 📦 Conteúdo do Pacote

Este pacote contém a skill **Query Executor** completa para distribuição.

### Estrutura:
```
query-executor-prod-uat/
  ├── SKILL.md                    # Documentação da skill
  ├── README_INSTALLATION.md      # Guia de instalação detalhado
  ├── VERSION.md                  # Histórico de versão
  ├── install.ps1                 # Script de instalação automatizada
  ├── config.yaml                 # Arquivo de configuração (template)
  ├── resources/
  │   └── TENANT_LOOKUP.txt       # Lookup de empresas/schemas
  └── scripts/
      ├── run_query.py            # Orquestrador principal
      ├── tenant_lookup.py        # Busca de tenant
      ├── patch_generator.py      # Gerador de patch
      ├── jfrog_upload.py         # Upload JFrog
      └── gha_dispatch.py         # Disparo GitHub Actions
```

## 🚀 Instalação Rápida

### Opção 1: Script Automatizado (Recomendado)

```powershell
# Extrair o ZIP em algum lugar
# Navegar até a pasta query-executor-prod-uat
cd caminho\para\query-executor-prod-uat

# Executar o instalador
.\install.ps1
```

Para forçar reinstalação sem confirmação:
```powershell
.\install.ps1 -Force
```

### Opção 2: Instalação Manual

1. Extrair o arquivo ZIP
2. Copiar a pasta `query-executor-prod-uat` para `%USERPROFILE%\.cursor\skills\`
3. Editar `config.yaml` e preencher usuário JFrog e email
4. Configurar variáveis de ambiente JFROG_TOKEN e GITHUB_TOKEN
5. Reiniciar o Cursor

## ⚙️ Configuração

### Variáveis de Ambiente Obrigatórias

```powershell
# JFROG_TOKEN
[Environment]::SetEnvironmentVariable("JFROG_TOKEN", "cmVmdGtuOjAxOjE4MDMwNjA0MjA6SnBmVVN6Q1pqbWdpSWoyVWdhRXBqVXZZcGRV", "User")

# GITHUB_TOKEN
[Environment]::SetEnvironmentVariable("GITHUB_TOKEN", "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", "User")
```

### Arquivo config.yaml

Edite e preencha:
- `jfrog.user` - Seu usuário do JFrog
- `user.email` - Seu email para notificações

## 📖 Documentação

- **SKILL.md** - Documentação completa de uso
- **README_INSTALLATION.md** - Guia de instalação detalhado
- **VERSION.md** - Informações de versão e changelog

## 🎯 Como Usar

Após instalar, use no Cursor com comandos como:

```
"Executa essa query em UAT para a ACHE: SELECT * FROM DUAL"
"Roda esse SQL em prod para a FEMSA"
```

## 🆘 Suporte

Para problemas ou dúvidas:
1. Consulte o **README_INSTALLATION.md** (seção Troubleshooting)
2. Verifique o **SKILL.md** para exemplos de uso
3. Entre em contato com a equipe de desenvolvimento

## 📝 Versão

- **Version**: 1.0.0
- **Build Date**: 2026-02-12
- **Python**: 3.7+
- **Platform**: Windows (PowerShell)

---

**Thomson Reuters - Uso Interno**

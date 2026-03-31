# Query Executor - Guia de Instalação

## 📦 Instalação

### 1. Copiar a skill para o diretório de skills do Cursor

```powershell
# Caminho padrão de skills do Cursor
$skillsPath = "$env:USERPROFILE\.cursor\skills"

# Copiar esta pasta para o diretório de skills
Copy-Item -Path "query-executor-prod-uat" -Destination "$skillsPath\" -Recurse -Force
```

### 2. Configurar variáveis de ambiente

Você precisa configurar as seguintes variáveis de ambiente do sistema:

#### JFROG_TOKEN
Token de autenticação do JFrog Artifactory

```powershell
# PowerShell (temporário - apenas para a sessão atual)
$env:JFROG_TOKEN = "seu-token-aqui"

# PowerShell (permanente - variável de usuário)
[Environment]::SetEnvironmentVariable("JFROG_TOKEN", "seu-token-aqui", "User")
```

#### GITHUB_TOKEN
Token do GitHub com permissão para disparar workflows

```powershell
# PowerShell (temporário - apenas para a sessão atual)
$env:GITHUB_TOKEN = "seu-token-aqui"

# PowerShell (permanente - variável de usuário)
[Environment]::SetEnvironmentVariable("GITHUB_TOKEN", "seu-token-aqui", "User")
```

**Importante**: Após configurar variáveis permanentes, reinicie o Cursor para que elas sejam carregadas.

### 3. Configurar o arquivo config.yaml

Edite o arquivo `config.yaml` e preencha suas informações:

```yaml
jfrog:
  user: "SEU_USUARIO_JFROG"  # ← Preencher com seu usuário

user:
  email: "SEU_EMAIL@empresa.com"  # ← Preencher com seu email
```

Os demais campos já vêm pré-configurados, mas podem ser ajustados conforme necessário.

### 4. Verificar a instalação

Após instalar, a skill deve aparecer automaticamente no Cursor. Teste com um comando:

```
Executa essa query em UAT para a ACHE: SELECT * FROM DUAL
```

## 🔧 Requisitos

- Python 3.7+ instalado
- Acesso ao JFrog Artifactory
- Token do GitHub com permissão de workflow dispatch
- Cursor instalado com suporte a Agent Skills

## 📚 Como Usar

Veja exemplos de uso no arquivo `SKILL.md` principal.

### Exemplos rápidos:

```
"Executa essa query em UAT para a ACHE: SELECT * FROM DUAL"
"Roda esse SQL em prod para a FEMSA"
"Envia essa query para produção da BMW"
```

## 🆘 Troubleshooting

### Erro de autenticação no JFrog
- Verifique se `JFROG_TOKEN` está configurado corretamente
- Confirme se o `jfrog.user` no `config.yaml` está correto

### Erro de autenticação no GitHub
- Verifique se `GITHUB_TOKEN` está configurado corretamente
- Confirme se o token tem permissão de `workflow:dispatch`

### Empresa não encontrada
- Verifique se a empresa existe no arquivo `resources/TENANT_LOOKUP.txt`
- O nome da empresa deve ser exatamente como aparece no lookup

### Skill não aparece no Cursor
- Verifique se o caminho de instalação está correto: `$env:USERPROFILE\.cursor\skills\query-executor-prod-uat`
- Reinicie o Cursor após a instalação

## 📁 Estrutura de Arquivos

```
query-executor-prod-uat/
  ├── SKILL.md                    # Documentação principal
  ├── README_INSTALLATION.md      # Este arquivo
  ├── config.yaml                 # Configurações (EDITAR)
  ├── resources/
  │   └── TENANT_LOOKUP.txt       # Mapeamento empresa/schema/ambiente
  └── scripts/
      ├── run_query.py            # Orquestrador principal
      ├── tenant_lookup.py        # Busca de tenant
      ├── patch_generator.py      # Gerador de patch ZIP
      ├── jfrog_upload.py         # Upload para JFrog
      └── gha_dispatch.py         # Disparo de workflow GitHub
```

## 🔒 Segurança

- **NUNCA** commite tokens ou senhas no config.yaml
- Use sempre variáveis de ambiente para credenciais
- O arquivo `config.yaml` deve conter apenas configurações não sensíveis
- Tokens devem ser gerenciados de forma segura

## 📝 Licença

Uso interno - Thomson Reuters

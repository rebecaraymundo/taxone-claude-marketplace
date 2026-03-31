# Query Executor - Notas de Distribuição

## 📦 Informações do Build

- **Versão**: 1.0.0
- **Data do Build**: 2026-02-12 18:41:38
- **Arquivo ZIP**: `query-executor-prod-uat_v1.0.0_20260212.zip`
- **Tamanho**: ~29 KB

## 🎯 Para o Destinatário

### Passo 1: Extrair o ZIP
Extraia o arquivo `query-executor-prod-uat_v1.0.0_20260212.zip` em algum local temporário.

### Passo 2: Executar o Instalador
Navegue até a pasta extraída `query-executor-prod-uat` e execute:

```powershell
.\install.ps1
```

O script irá:
- ✅ Verificar se o Cursor está configurado
- ✅ Copiar a skill para `%USERPROFILE%\.cursor\skills\`
- ✅ Validar todos os arquivos necessários
- ✅ Oferecer editar o `config.yaml` imediatamente

### Passo 3: Configurar Credenciais

#### 3.1 Variáveis de Ambiente

```powershell
# JFROG_TOKEN - Token do JFrog Artifactory
[Environment]::SetEnvironmentVariable("JFROG_TOKEN", "SEU_TOKEN_AQUI", "User")

# GITHUB_TOKEN - Token do GitHub com permissão de workflow
[Environment]::SetEnvironmentVariable("GITHUB_TOKEN", "SEU_TOKEN_AQUI", "User")
```

#### 3.2 Arquivo config.yaml

Edite `%USERPROFILE%\.cursor\skills\query-executor-prod-uat\config.yaml`:

```yaml
jfrog:
  user: "SEU_USUARIO_JFROG"  # ← Preencher

user:
  email: "SEU_EMAIL@thomsonreuters.com"  # ← Preencher
```

### Passo 4: Reiniciar o Cursor
Feche e abra novamente o Cursor para carregar a skill.

### Passo 5: Testar
Use um comando de teste:

```
Executa essa query em UAT para a ACHE: SELECT * FROM DUAL
```

## 📋 Checklist de Instalação

- [ ] ZIP extraído
- [ ] Script `install.ps1` executado
- [ ] `JFROG_TOKEN` configurado
- [ ] `GITHUB_TOKEN` configurado
- [ ] `config.yaml` editado (usuário e email)
- [ ] Cursor reiniciado
- [ ] Skill testada com comando de exemplo

## 🔧 Requisitos do Sistema

- **Sistema Operacional**: Windows 10/11
- **PowerShell**: 5.1 ou superior
- **Python**: 3.7 ou superior
- **Cursor IDE**: Versão com suporte a Agent Skills
- **Acesso**: JFrog Artifactory e GitHub (com tokens)

## 📖 Documentação Incluída

1. **README.md** (raiz do ZIP)
   - Visão geral do pacote
   - Instruções de instalação rápida

2. **README_INSTALLATION.md** (dentro da pasta da skill)
   - Guia detalhado de instalação
   - Seção de troubleshooting
   - Exemplos de uso

3. **SKILL.md** (dentro da pasta da skill)
   - Documentação completa da skill
   - Todos os parâmetros e opções
   - Exemplos avançados

4. **VERSION.md** (dentro da pasta da skill)
   - Histórico de versões
   - Changelog de features

## 🛡️ Segurança

⚠️ **IMPORTANTE**:
- NUNCA commite ou compartilhe o arquivo `config.yaml` com tokens preenchidos
- Use sempre variáveis de ambiente para credenciais sensíveis
- Os tokens devem ser pessoais e intransferíveis

## 🆘 Suporte

### Problemas Comuns

1. **Skill não aparece no Cursor**
   - Verifique se está em `%USERPROFILE%\.cursor\skills\query-executor-prod-uat`
   - Reinicie o Cursor
   - Verifique se a pasta não foi renomeada

2. **Erro de autenticação JFrog**
   - Confirme `JFROG_TOKEN` nas variáveis de ambiente
   - Verifique `jfrog.user` no `config.yaml`

3. **Erro de autenticação GitHub**
   - Confirme `GITHUB_TOKEN` nas variáveis de ambiente
   - Verifique se o token tem permissão `workflow:dispatch`

4. **Empresa não encontrada**
   - Verifique o nome exato no `resources/TENANT_LOOKUP.txt`
   - O nome deve ser case-sensitive

### Contato
Para questões ou problemas, entre em contato com a equipe de desenvolvimento.

## 📜 Licença
Uso interno - Thomson Reuters

---

**Build gerado em**: 2026-02-12 18:41:38  
**Build por**: Automated Build System

# Query Executor - Version History

## Version 1.0.0 (2026-02-12)

### Features
- ✅ Execução de queries SQL em ambientes Production e UAT
- ✅ Suporte para queries inline e arquivos .sql
- ✅ Upload automático para JFrog Artifactory
- ✅ Disparo automático de workflow no GitHub Actions
- ✅ Lookup automático de tenant/empresa
- ✅ Geração de patch ZIP com header SQL
- ✅ Limpeza automática de arquivos antigos no JFrog
- ✅ Modo dry-run para testes

### Scripts Incluídos
- `run_query.py` - Orquestrador principal (9.3 KB)
- `tenant_lookup.py` - Busca de tenant (3.2 KB)
- `patch_generator.py` - Gerador de patch (4.6 KB)
- `jfrog_upload.py` - Upload JFrog (5.4 KB)
- `gha_dispatch.py` - Disparo GitHub Actions (4.4 KB)

### Resources
- `TENANT_LOOKUP.txt` - 63.6 KB com mapeamento de empresas

### Configuration
- `config.yaml` - Configuração centralizada
- Suporte para variáveis de ambiente (JFROG_TOKEN, GITHUB_TOKEN)

### Documentation
- `SKILL.md` - Documentação completa da skill
- `README_INSTALLATION.md` - Guia de instalação
- `VERSION.md` - Este arquivo

## Build Information
- Build Date: 2026-02-12
- Build Time: 18:41:38
- Python Version: 3.7+
- Platform: Windows (PowerShell)

## Requirements
- Cursor IDE with Agent Skills support
- Python 3.7 or higher
- JFrog Artifactory access
- GitHub token with workflow dispatch permission

## Installation Path
Default: `%USERPROFILE%\.cursor\skills\query-executor-prod-uat`

## Support
For issues or questions, contact the development team.

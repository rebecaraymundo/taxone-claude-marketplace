# =============================================================================
# Query Executor - Script de Instalação Automatizada
# =============================================================================
# Este script instala a skill Query Executor no Cursor automaticamente
# =============================================================================

param(
    [switch]$Force = $false
)

Write-Host "`n==============================================================================" -ForegroundColor Cyan
Write-Host "Query Executor - Instalação Automatizada" -ForegroundColor Cyan
Write-Host "==============================================================================`n" -ForegroundColor Cyan

# Determinar o caminho de destino
$skillsPath = "$env:USERPROFILE\.cursor\skills"
$destPath = "$skillsPath\query-executor-prod-uat"
$sourcePath = $PSScriptRoot

Write-Host "📁 Caminho de origem: $sourcePath" -ForegroundColor Gray
Write-Host "📁 Caminho de destino: $destPath`n" -ForegroundColor Gray

# Verificar se o diretório de skills existe
if (-not (Test-Path $skillsPath)) {
    Write-Host "⚠️  Diretório de skills não encontrado: $skillsPath" -ForegroundColor Yellow
    Write-Host "   Criando diretório..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path $skillsPath -Force | Out-Null
    Write-Host "✅ Diretório criado com sucesso`n" -ForegroundColor Green
}

# Verificar se a skill já está instalada
if (Test-Path $destPath) {
    if ($Force) {
        Write-Host "⚠️  Skill já instalada. Removendo versão anterior (flag -Force detectada)..." -ForegroundColor Yellow
        Remove-Item -Path $destPath -Recurse -Force
        Write-Host "✅ Versão anterior removida`n" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Skill já instalada em: $destPath" -ForegroundColor Yellow
        $response = Read-Host "   Deseja sobrescrever? (S/N)"
        if ($response -ne "S" -and $response -ne "s") {
            Write-Host "`n❌ Instalação cancelada pelo usuário." -ForegroundColor Red
            exit 1
        }
        Remove-Item -Path $destPath -Recurse -Force
        Write-Host "✅ Versão anterior removida`n" -ForegroundColor Green
    }
}

# Copiar arquivos
Write-Host "📦 Instalando Query Executor..." -ForegroundColor Cyan
try {
    Copy-Item -Path $sourcePath -Destination $destPath -Recurse -Force
    Write-Host "✅ Arquivos copiados com sucesso`n" -ForegroundColor Green
} catch {
    Write-Host "❌ Erro ao copiar arquivos: $_" -ForegroundColor Red
    exit 1
}

# Verificar instalação
$requiredFiles = @(
    "SKILL.md",
    "config.yaml",
    "README_INSTALLATION.md",
    "VERSION.md",
    "scripts\run_query.py",
    "resources\TENANT_LOOKUP.txt"
)

Write-Host "🔍 Verificando instalação..." -ForegroundColor Cyan
$allFilesPresent = $true
foreach ($file in $requiredFiles) {
    $filePath = Join-Path $destPath $file
    if (Test-Path $filePath) {
        Write-Host "   ✓ $file" -ForegroundColor Green
    } else {
        Write-Host "   ✗ $file (não encontrado)" -ForegroundColor Red
        $allFilesPresent = $false
    }
}

if (-not $allFilesPresent) {
    Write-Host "`n❌ Instalação incompleta. Alguns arquivos não foram encontrados." -ForegroundColor Red
    exit 1
}

Write-Host "`n==============================================================================`n" -ForegroundColor Cyan

# Verificar configuração
Write-Host "⚙️  PRÓXIMOS PASSOS:`n" -ForegroundColor Yellow

Write-Host "1. Configure as variáveis de ambiente:" -ForegroundColor White
Write-Host "   [Environment]::SetEnvironmentVariable('JFROG_TOKEN', 'seu-token', 'User')" -ForegroundColor Gray
Write-Host "   [Environment]::SetEnvironmentVariable('GITHUB_TOKEN', 'seu-token', 'User')`n" -ForegroundColor Gray

Write-Host "2. Edite o arquivo de configuração:" -ForegroundColor White
Write-Host "   notepad `"$destPath\config.yaml`"`n" -ForegroundColor Gray

Write-Host "3. Preencha seu usuário JFrog e email no config.yaml`n" -ForegroundColor White

Write-Host "4. Reinicie o Cursor para carregar a skill`n" -ForegroundColor White

# Perguntar se deseja editar o config agora
$editNow = Read-Host "Deseja editar o config.yaml agora? (S/N)"
if ($editNow -eq "S" -or $editNow -eq "s") {
    notepad "$destPath\config.yaml"
}

Write-Host "`n✅ Instalação concluída com sucesso!" -ForegroundColor Green
Write-Host "`n==============================================================================`n" -ForegroundColor Cyan

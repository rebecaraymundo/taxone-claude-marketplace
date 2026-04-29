#!/bin/bash

# Script rápido para criar repositório GitHub
# Uso: ./quick_github_create.sh [TOKEN]

set -e

# Configurações
REPO_NAME="taxone-claude-marketplace"
REPO_DESCRIPTION="TAX ONE Claude Marketplace - Automated RCA Report Generation System"

echo "🚀 Criando repositório GitHub: $REPO_NAME"

# Token via parâmetro ou variável de ambiente
if [ ! -z "$1" ]; then
    GITHUB_TOKEN="$1"
elif [ -z "$GITHUB_TOKEN" ]; then
    echo "❌ Token necessário!"
    echo "Uso: ./quick_github_create.sh ghp_your_token"
    echo "Ou: export GITHUB_TOKEN='ghp_your_token' && ./quick_github_create.sh"
    echo ""
    echo "🔗 Obtenha seu token em: https://github.com/settings/tokens"
    exit 1
fi

# Obter nome de usuário
echo "🔍 Verificando autenticação..."
USERNAME=$(curl -s -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user | grep '"login"' | cut -d'"' -f4)

if [ -z "$USERNAME" ]; then
    echo "❌ Falha na autenticação. Verifique seu token."
    exit 1
fi

echo "✅ Autenticado como: $USERNAME"

# Criar repositório
echo "🔨 Criando repositório..."
RESPONSE=$(curl -s -X POST -H "Authorization: token $GITHUB_TOKEN" \
    -H "Accept: application/vnd.github.v3+json" \
    https://api.github.com/user/repos \
    -d "{\"name\":\"$REPO_NAME\",\"description\":\"$REPO_DESCRIPTION\",\"private\":false}")

if echo "$RESPONSE" | grep -q '"clone_url"'; then
    echo "✅ Repositório criado!"

    # Configurar remote e push
    git remote remove origin 2>/dev/null || true
    git remote add origin "https://github.com/$USERNAME/$REPO_NAME.git"
    git push -u origin main

    echo ""
    echo "🎉 SUCESSO!"
    echo "🌐 Repositório: https://github.com/$USERNAME/$REPO_NAME"
    echo "📋 Clone: git clone https://github.com/$USERNAME/$REPO_NAME.git"
else
    echo "❌ Erro na criação:"
    echo "$RESPONSE"
    exit 1
fi
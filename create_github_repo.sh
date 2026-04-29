#!/bin/bash

# Script para criar repositório no GitHub automaticamente
# Autor: Claude Code AI Assistant

set -e

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 GitHub Repository Creator - TAX ONE Claude Marketplace${NC}"
echo -e "${BLUE}================================================================${NC}\n"

# Verificar se o token foi fornecido
if [ -z "$GITHUB_TOKEN" ]; then
    echo -e "${YELLOW}⚠️  GITHUB_TOKEN não encontrado!${NC}"
    echo -e "${YELLOW}Por favor, configure seu Personal Access Token:${NC}\n"
    echo -e "1. Acesse: ${BLUE}https://github.com/settings/tokens${NC}"
    echo -e "2. Clique em 'Generate new token' > 'Generate new token (classic)'"
    echo -e "3. Selecione os escopos: ${GREEN}repo, workflow, write:packages${NC}"
    echo -e "4. Configure o token:"
    echo -e "   ${GREEN}export GITHUB_TOKEN='ghp_...'${NC}"
    echo -e "5. Execute novamente este script\n"
    exit 1
fi

# Configurações do repositório
REPO_NAME="taxone-claude-marketplace"
REPO_DESCRIPTION="TAX ONE Claude Marketplace - Automated RCA Report Generation System for Thomson Reuters"
REPO_PRIVATE=false  # Altere para true se quiser privado

echo -e "${YELLOW}📋 Configurações do Repositório:${NC}"
echo -e "   Nome: ${GREEN}${REPO_NAME}${NC}"
echo -e "   Descrição: ${GREEN}${REPO_DESCRIPTION}${NC}"
echo -e "   Visibilidade: ${GREEN}$([ "$REPO_PRIVATE" = true ] && echo "Privado" || echo "Público")${NC}\n"

# Obter informações do usuário GitHub
echo -e "${BLUE}🔍 Verificando autenticação GitHub...${NC}"
USER_INFO=$(curl -s -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user)

if echo "$USER_INFO" | grep -q "message"; then
    echo -e "${RED}❌ Erro na autenticação. Verifique seu GITHUB_TOKEN${NC}"
    echo -e "${RED}Resposta da API: $USER_INFO${NC}"
    exit 1
fi

USERNAME=$(echo "$USER_INFO" | grep '"login"' | cut -d'"' -f4)
echo -e "${GREEN}✅ Autenticado como: ${USERNAME}${NC}\n"

# Verificar se o repositório já existe
echo -e "${BLUE}🔍 Verificando se o repositório já existe...${NC}"
REPO_CHECK=$(curl -s -o /dev/null -w "%{http_code}" -H "Authorization: token $GITHUB_TOKEN" \
    "https://api.github.com/repos/$USERNAME/$REPO_NAME")

if [ "$REPO_CHECK" = "200" ]; then
    echo -e "${YELLOW}⚠️  Repositório $REPO_NAME já existe!${NC}"
    echo -e "${YELLOW}URL: https://github.com/$USERNAME/$REPO_NAME${NC}\n"

    read -p "Deseja continuar e apenas configurar o remote? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi

    REPO_URL="https://github.com/$USERNAME/$REPO_NAME.git"
else
    # Criar o repositório
    echo -e "${BLUE}🔨 Criando repositório no GitHub...${NC}"

    CREATE_REPO_RESPONSE=$(curl -s -X POST -H "Authorization: token $GITHUB_TOKEN" \
        -H "Accept: application/vnd.github.v3+json" \
        https://api.github.com/user/repos \
        -d "{
            \"name\": \"$REPO_NAME\",
            \"description\": \"$REPO_DESCRIPTION\",
            \"private\": $REPO_PRIVATE,
            \"has_issues\": true,
            \"has_projects\": true,
            \"has_wiki\": false
        }")

    # Verificar se a criação foi bem-sucedida
    if echo "$CREATE_REPO_RESPONSE" | grep -q '"clone_url"'; then
        REPO_URL=$(echo "$CREATE_REPO_RESPONSE" | grep '"clone_url"' | cut -d'"' -f4)
        echo -e "${GREEN}✅ Repositório criado com sucesso!${NC}"
        echo -e "${GREEN}URL: https://github.com/$USERNAME/$REPO_NAME${NC}\n"
    else
        echo -e "${RED}❌ Erro ao criar repositório:${NC}"
        echo -e "${RED}$CREATE_REPO_RESPONSE${NC}"
        exit 1
    fi
fi

# Configurar o remote e fazer push
echo -e "${BLUE}🔗 Configurando remote origin...${NC}"

# Remover remote existente se houver
git remote remove origin 2>/dev/null || true

# Adicionar novo remote
git remote add origin "$REPO_URL"

echo -e "${BLUE}📤 Fazendo push do código...${NC}"

# Push do código
git push -u origin main

echo -e "\n${GREEN}🎉 SUCESSO! Repositório criado e código enviado!${NC}"
echo -e "${GREEN}================================================================${NC}"
echo -e "${GREEN}🌐 URL do Repositório: https://github.com/$USERNAME/$REPO_NAME${NC}"
echo -e "${GREEN}📋 Para clonar: git clone https://github.com/$USERNAME/$REPO_NAME.git${NC}"
echo -e "${GREEN}👥 Para compartilhar, envie o link acima para outras pessoas${NC}"
echo -e "\n${BLUE}💡 Próximos passos:${NC}"
echo -e "   1. Acesse o repositório no GitHub"
echo -e "   2. Configure colaboradores em Settings > Collaborators (se privado)"
echo -e "   3. Revise as configurações de segurança"
echo -e "   4. Considere adicionar topics/tags para facilitar a descoberta"

echo -e "\n${GREEN}✅ Processo concluído com sucesso!${NC}"
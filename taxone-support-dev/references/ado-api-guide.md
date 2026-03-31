# Azure DevOps REST API - Guia para TAX ONE Suporte

Guia completo da API REST do Azure DevOps para os pipelines automatizados do TAX ONE Suporte.

**Usado por:**
- `/taxone-auto-fix` (Bugs)
- `/taxone-us-auto-implement` (User Stories/Features)

---

## Autenticacao

Todas as chamadas usam Basic Auth com PAT token via header `Authorization`.

**Padrao correto:**
```bash
AUTH=$(printf '%s' ":$ADO_PAT" | base64 -w0)
curl -s -H "Authorization: Basic $AUTH" ...
```

Ou inline em cada chamada:
```bash
curl -s -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" ...
```

O username e vazio (string vazia antes do `:`), o password e o PAT. O valor e codificado em base64 e passado no header `Authorization: Basic`.

> **IMPORTANTE:** NAO usar `-u ":$ADO_PAT"` — este formato pode falhar em alguns ambientes. Sempre usar o header `Authorization: Basic` com o valor codificado em base64.

---

## Configuracao do Projeto

| Parametro | Valor |
|-----------|-------|
| **Org URL** | `https://dev.azure.com/tr-ggo` |
| **Project** | `Mastersaf Fiscal Solutions` |
| **Project (URL encoded)** | `Mastersaf%20Fiscal%20Solutions` |
| **Area Path (Suporte)** | `Mastersaf Fiscal Solutions\MFS\TAX ONE\Suporte` |
| **API Version** | `7.0` |

---

## Endpoints

### 1. Executar Query Salva

```bash
curl -s -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/wiql/{QUERY_ID}?api-version=7.0"
```

**Resposta (estrutura):**
```json
{
  "queryType": "flat",
  "asOf": "2026-03-06T...",
  "workItems": [
    { "id": 1045123, "url": "..." },
    { "id": 1045456, "url": "..." }
  ]
}
```

**Extrair IDs:** `workItems[].id`

---

### 2. Buscar Detalhes de Work Items (Batch)

```bash
curl -s -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems?ids=1045123,1045456&\$expand=none&fields={FIELDS}&api-version=7.0"
```

**Campos comuns:**
- `System.Id`
- `System.Title`
- `System.Description`
- `System.WorkItemType`
- `System.State`
- `System.AreaPath`
- `Microsoft.VSTS.Common.Priority`
- `System.Tags`

**Campos especificos por tipo:**

| Work Item Type | Campos Adicionais |
|----------------|-------------------|
| Bug | `Microsoft.VSTS.TCM.ReproSteps`, `Microsoft.VSTS.Common.Severity` |
| User Story, Feature | `Microsoft.VSTS.Common.AcceptanceCriteria` |

**Resposta (estrutura):**
```json
{
  "count": 2,
  "value": [
    {
      "id": 1045123,
      "fields": {
        "System.Id": 1045123,
        "System.Title": "...",
        "System.WorkItemType": "Bug",
        "System.State": "New",
        "System.AreaPath": "Mastersaf Fiscal Solutions\\MFS\\TAX ONE\\Suporte",
        "System.Description": "<div>HTML...</div>",
        "Microsoft.VSTS.Common.Priority": 2,
        "System.Tags": "Tag1; Tag2"
      }
    }
  ]
}
```

**Nota:** Limpar tags HTML antes de passar para os agentes.

**Limite:** Maximo 200 work items por chamada GET batch.

---

### 3. Buscar Work Item Individual (por ID)

```bash
curl -s -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems/{WORK_ITEM_ID}?\$expand=none&fields={FIELDS}&api-version=7.0"
```

---

### 4. Buscar Work Items por WIQL (POST)

```bash
curl -s -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/wiql?api-version=7.0" \
  -H "Content-Type: application/json" \
  --data-raw '{"query":"SELECT [System.Id],[System.Title] FROM WorkItems WHERE [System.WorkItemType] = '"'"'Bug'"'"' AND [System.AreaPath] UNDER '"'"'Mastersaf Fiscal Solutions\\MFS\\TAX ONE\\Suporte'"'"' AND [System.Title] CONTAINS '"'"'{KEYWORD}'"'"' ORDER BY [System.ChangedDate] DESC"}'
```

**IMPORTANTE:**
- Usar `--data-raw` (NAO `-d`) para evitar problemas com aspas simples no WIQL
- As aspas simples na query WIQL devem ser escapadas com `'"'"'` no bash
- Filtrar por Area Path `UNDER 'Mastersaf Fiscal Solutions\MFS\TAX ONE\Suporte'`
- Esta chamada e OPCIONAL. Se falhar (302/401), ignorar e prosseguir

---

### 5. Atualizar Work Item (PATCH)

```bash
curl -s -X PATCH \
  -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  -H "Content-Type: application/json-patch+json" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitems/{WORK_ITEM_ID}?api-version=7.0" \
  -d '[
    {
      "op": "add",
      "path": "/fields/System.State",
      "value": "{NEW_STATE}"
    },
    {
      "op": "add",
      "path": "/fields/System.Tags",
      "value": "{EXISTING_TAGS}; {NEW_TAG}"
    }
  ]'
```

**IMPORTANTE:**
- O `Content-Type` para PATCH de work items e `application/json-patch+json` (NAO `application/json`)
- `System.Tags`: Concatenar tags existentes com nova tag
- Se o PATCH falhar por transicao de estado invalida, tentar estados intermediarios

**Campos customizados do projeto Mastersaf Fiscal Solutions (verificados):**

| Campo | Reference Name | Descricao |
|-------|---------------|-----------|
| Solutions | `Custom.Solutions` | Campo de comunicacao interna / solucoes (equivalente ao `LegalOne.InternalCom`) |
| Developer Text | `Custom.DeveloperText` | Campo de texto do desenvolvedor / reviewer (equivalente ao `Custom.L1_Bug_DevreviewName`) |
| AI Powered | `TR.WOW.AIPowered` | Flag indicando que o work item foi processado por IA |

> **NOTA:** Estes campos foram verificados via API e estao confirmados como validos no projeto Mastersaf Fiscal Solutions.

---

## Estados Validos para Transicao

### Bugs
- New -> Active -> Resolved -> Closed
- New -> Resolved (direto, quando fix e imediato)

**Recomendado:**
- Se Bug ja estiver em "Active", mudar para "Resolved"
- Se estiver em "New", mudar para "Resolved" direto
- Se falhar, tentar "Active" primeiro, depois "Resolved"

### User Stories / Features
- New -> Active -> Committed -> Done
- New -> Committed -> Active -> Done

**Recomendado:**
- Apos implementacao, mudar para "Active" (pronto para review/teste)
- Se falhar, nao alterar e reportar erro (mas nao bloquear - PR ja foi criado)

---

## Parse de URL do Work Item

Se o usuario informar URL do ADO:
```
https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/1045123
```

Extrair WORK_ITEM_ID:
```bash
WORK_ITEM_ID=$(echo "$URL" | grep -oP '(?<=/_workitems/edit/)\d+')
```

---

## Campos por Tipo de Work Item

### Bug (para `/taxone-auto-fix`)

**Campos importantes:**
- `System.Title`: Titulo do bug
- `Microsoft.VSTS.TCM.ReproSteps`: **CAMPO PRINCIPAL** - Passos para reproduzir
- `System.Description`: Descricao complementar
- `System.AreaPath`: Area path (filtrar por TAX ONE\Suporte)
- `Microsoft.VSTS.Common.Priority`: 1-4
- `Microsoft.VSTS.Common.Severity`: "1 - Critical" a "4 - Low"
- `System.State`: Validar e atualizar
- `System.Tags`: Preservar ao adicionar tag

**Tags:**
- Bug Real: `AI-Fixed`
- As Designed: `AI-AsDesigned`

**State:**
- Bug Real: `Resolved`
- As Designed: **NAO alterar**

### User Story / Feature (para `/taxone-us-auto-implement`)

**Campos importantes:**
- `System.Title`: Titulo
- `System.WorkItemType`: "User Story" ou "Feature"
- `Microsoft.VSTS.Common.AcceptanceCriteria`: **CAMPO PRINCIPAL**
- `System.Description`: Contexto adicional
- `System.AreaPath`: Area path
- `Microsoft.VSTS.Common.Priority`: 1-4
- `System.State`: Validar (deve ser "New" ou "Active")
- `System.Tags`: Preservar ao adicionar tag

**Tag:** `AI-Implemented`
**State:** `Active`

---

## Validacoes por Tipo

### Bugs (`/taxone-auto-fix`)
1. **Validar WorkItemType:** DEVE ser "Bug"
2. **Validar AreaPath:** DEVE estar sob `Mastersaf Fiscal Solutions\MFS\TAX ONE\Suporte`
3. **Validar ReproSteps:** Se vazio, avisar mas prosseguir

### User Stories / Features (`/taxone-us-auto-implement`)
1. **Validar WorkItemType:** DEVE ser "User Story" ou "Feature"
2. **Validar State:** DEVE estar em "New" ou "Active"
3. **Validar AcceptanceCriteria:** Se vazio, avisar

---

## Rate Limits

- 200 requests/minuto por PAT
- Maximo 200 work items por chamada GET batch

---

## Troubleshooting

| Erro | Causa | Solucao |
|------|-------|---------|
| 401 Unauthorized | PAT expirado ou invalido | Renovar PAT no ADO |
| 404 Not Found | Work item/query nao existe ou sem permissao | Verificar ID e permissoes |
| 302 Found | Redirect (comum em WIQL POST) | Ignorar se opcional |
| 400 Bad Request | Estado invalido na transicao | Tentar estados intermediarios |
| 400 Bad Request | Campo obrigatorio faltando | Adicionar campo requerido |
| Rate limit exceeded | Muitas requisicoes | Aguardar 1 minuto |

---

## Descobrir Campos Customizados

Para listar TODOS os campos customizados de um tipo de work item:

```bash
# Listar campos de Bug
curl -s -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitemtypes/Bug/fields?api-version=7.0"

# Listar campos de User Story
curl -s -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitemtypes/User%20Story/fields?api-version=7.0"
```

**Filtrar campos customizados:**
```bash
curl -s -H "Authorization: Basic $(printf '%s' ":$ADO_PAT" | base64 -w0)" \
  "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_apis/wit/workitemtypes/Bug/fields?api-version=7.0" | \
  python3 -c "
import sys, json
data = json.load(sys.stdin)
for f in data.get('value', []):
    name = f.get('referenceName', '')
    if 'custom' in name.lower() or not name.startswith(('System.', 'Microsoft.')):
        print(f'{name} -> {f.get(\"name\", \"\")}')
"
```

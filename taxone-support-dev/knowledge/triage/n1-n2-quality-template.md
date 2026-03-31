# Template de Feedback para N1/N2

Utilizado pelo agente `taxone-pm` quando o veredicto e `INCOMPLETE_ANALYSIS`.
Este template estrutura o feedback para devolver Work Items com analise incompleta ao N1/N2.

---

## Template de Feedback

```
## Analise Incompleta - WI #{ID}: {TITULO}

O work item foi analisado pelo pipeline de triagem automatica e identificou-se que
as informacoes fornecidas sao insuficientes para uma analise tecnica N3.

### Itens Faltantes

{Para cada item faltante, incluir a secao correspondente abaixo}

#### Passos de Reproducao (ReproSteps)
**Status:** AUSENTE / INCOMPLETO
**O que e necessario:**
- Passo a passo detalhado para reproduzir o problema
- Incluir: menu de acesso, tela, campos preenchidos, botao clicado
- Exemplo:
  1. Acessar Menu > [modulo] > [tela]
  2. Informar filtros: [empresa], [periodo], [tipo de nota]
  3. Clicar em [botao/acao]
  4. Observar o erro: [mensagem exata]

#### Identificacao do Ambiente
**Status:** AUSENTE
**O que e necessario:**
- Ambiente: Producao / Homologacao / Desenvolvimento
- Versao do TAX ONE (ex: 12.5.3, 13.0.1)
- Versao do banco Oracle (ex: 19c, 21c)
- Sistema operacional do servidor (se relevante)

#### Evidencias
**Status:** AUSENTE
**O que e necessario:**
- Screenshot da tela mostrando o erro
- Log do servidor com a mensagem de erro completa (stack trace)
- Mensagem de erro exata (copiar texto, nao apenas screenshot)
- Se erro Oracle: codigo ORA-XXXXX completo

#### Dados de Teste
**Status:** AUSENTE
**O que e necessario:**
- CNPJ / Empresa afetada
- Periodo fiscal (mes/ano)
- Tipo de nota fiscal / documento
- Codigo do item / produto (se aplicavel)
- Qualquer filtro especifico usado

#### Descricao do Erro
**Status:** VAGO
**O que e necessario:**
- Mensagem de erro exata (nao apenas "da erro" ou "nao funciona")
- Comportamento observado vs comportamento esperado
- Frequencia: sempre acontece ou intermitente?
- Desde quando: regressao recente ou problema antigo?

### Passos Esperados Antes de Escalar para N3

1. **Reproduzir o problema** em ambiente controlado (preferencialmente homologacao)
2. **Documentar passos** de reproducao com detalhes suficientes
3. **Capturar evidencias** (screenshots, logs, mensagens de erro)
4. **Identificar escopo** (afeta todos os clientes ou caso especifico?)
5. **Verificar FAQ** - Consultar base de conhecimento para solucoes conhecidas
6. **Verificar parametrizacao** - Validar se os parametros do cliente estao corretos

### Artigos FAQ Relevantes

{Se o faq_triage.py retornou artigos, listar aqui:}
- [{titulo_artigo}]({caminho_artigo}) - {resumo}

### Proximos Passos

Apos complementar as informacoes acima, reabrir o work item para nova triagem.
A analise tecnica N3 sera retomada com os dados completos.
```

---

## Niveis de Incompletude

| Nivel | Score | Acao |
|-------|-------|------|
| **Leve** (25-34) | 1-2 itens faltantes | Mencionar itens faltantes, mas prosseguir se possivel |
| **Moderado** (35-44) | 3-4 itens faltantes | Recomendar complemento, perguntar ao usuario se deseja prosseguir |
| **Grave** (45+) | 5+ itens faltantes ou ReproSteps vazio | Devolver para N1/N2 obrigatoriamente |

---

## Exemplos de Feedback

### Exemplo 1 - Apenas ReproSteps ausente
```
O work item precisa de passos de reproducao detalhados.
Atualmente a descricao diz apenas "Erro ao gerar apuracao ICMS" sem informar:
- Qual empresa/CNPJ
- Qual periodo
- Quais parametros usados
- Qual a mensagem de erro exata

Por favor, complementar com os passos de reproducao e reabrir.
```

### Exemplo 2 - Multiplos itens faltantes
```
O work item necessita das seguintes informacoes para analise N3:

1. ReproSteps: Apenas "nao calcula" - precisa de passo a passo
2. Ambiente: Nao informado (producao? homologacao? versao?)
3. Evidencias: Sem screenshots ou logs de erro
4. Dados: Sem CNPJ/empresa para verificacao

Recomendacao: Reproduzir o cenario em homologacao, capturar evidencias
e reabrir com informacoes completas.
```

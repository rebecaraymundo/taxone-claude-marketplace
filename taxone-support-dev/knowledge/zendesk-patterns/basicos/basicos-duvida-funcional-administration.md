---
pattern_id: "basicos-duvida-funcional-administration"
vertical: basicos
root_cause: duvida_funcional
module: administration
ticket_count: 86
ticket_ids: [83933, 87666, 87931, 88710, 88595, 89854, 90321, 90221, 94348, 95458, 96141, 96083, 97332, 98148, 100422, 103850, 104419, 104977, 105873, 109561, 111157, 111618, 112477, 112292, 112088, 114014, 118701, 121480, 126026, 125812, 126572, 126567, 126518, 127418, 126950, 131531, 134238, 134541, 137924, 137913, 138783, 138775, 138772, 139911, 139688, 140517, 142345, 143496, 143043, 146532, 147462, 147110, 151060, 150984, 156019, 155696, 155691, 155618, 157200, 156655, 158029, 159137, 161679, 161408, 162825, 163525, 163446, 165195, 165010, 166528, 166372, 166345, 166341, 166293, 167555, 168303, 168238, 167633, 169297, 168836, 168720, 170295, 170179, 170006, 172398, 172373]
last_occurrence: "2026-03-06"
keywords: ["aplica\u00e7\u00e3o", "n\u00e3o", "mostra", "estabelecimento", "ecf", "erro", "abrir", "aplicacao", "mastersaf", "email"]
is_not_bug: true
---

# ADMINISTRATION: Duvida Funcional

## Descricao do Padrao
Clientes reportam problemas relacionados a:  Sua sessão excedeu o limite de tempo e você foi desconectado automaticamente; AF - Senha do Usuário Integrador; AUTOLIV - Acesso inválido com Admin no TAXONE

## Causa Raiz
Duvida Funcional — classificacao baseada em 86 tickets resolvidos.

## Resolucao / Orientacao
Resolucoes aplicadas nos tickets de referencia:
Bom dia, espero que esteja bem.
&nbsp;
Identificamos que tanto o acesso em inglês quanto em português utilizam os mesmos domínios, portas (443/HTTPS) e infraestrutura de rede. O comportamento diferente entre os idiomas não está relacionado a rotas ou IPs distintos, mas provavelmente a alguma restrição de rede (firewall, proxy, whitelist de IPs/domínios/URLs) aplicada no ambiente do cliente.
&nbsp;
Recomendamos a revisão da política de bloqueio/restrição da rede, garantindo que:
&nbsp;
  Todo o...

## Tickets de Referencia
| TKT | Data | Resumo |
|-----|------|--------|
| 172398 | 2026-02-02 | Relatórios estão sendo gerados incompletos |
| 172373 | 2026-02-02 | Erro na Criação de Usuário |
| 170295 | 2026-01-19 | TUPPERWARE - SENHA DE USÁRIO |
| 170179 | 2026-01-19 | Eventos - Reforma Tributaria |
| 170006 | 2026-01-16 | TAXONE - Problema com Atribuição de Acesso em Grupo |
| 169297 | 2026-01-13 | relação de IPs, URLs e portas utilizadas pela plataforma -... |
| 168836 | 2026-01-11 | Falha Básica na Gestão de Acesso |
| 168720 | 2026-01-09 | estamos com problemas de acesso ao site da TAX One em nossa... |
| 168303 | 2026-01-07 | Licenciamento TaxOne - TIKTOK LOGISTICS BRAZIL LTDA. |
| 168238 | 2026-01-07 | Evoltz - SSO para o Tax One |

## Keywords para Matching
aplicação, não, mostra, estabelecimento, ecf, erro, abrir, aplicacao, mastersaf, email

---
source: "MTZ-Report_Fiscal-Demonstrativo_Sintetico_p_Funcionario.doc"
category: Report_Fiscal
converted: auto
---

Report Fiscal - Demonstrativo Sintético p/ Funcionário


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
CH55947
Melhoria no relatório Folha de Pagamento > Demonstrativo Sintético por Funcionário
Incluir quebra de página por estabelecimento e ajustar a totalização do relatório demonstrativo sintético por funcionário

REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN01
Quando o usuário seleciona um estabelecimento específico na tela de geração do relatório existente no menu: 'Gerenciais > Folha de Pagamento > Demonstrativo Sintético p/ Funcionário', o relatório apresenta uma linha denominada 'Totalização' para apresentar os totais daquele estabelecimento. Essa linha deve passar a se chamar 'Total do Estabelecimento <cod_estab>:'
CH55947
RN02
Caso o usuário selecione a opção "Todos" na tela de geração do relatório existente no menu: 'Gerenciais > Folha de Pagamento > Demonstrativo Sintético p/ Funcionário', o sistema deve:

- Apresentar cada estabelecimento que possua dados para geração do relatório em uma página separada;
- Nos campos 'Filial', 'Insc Estadual' e 'CNPJ', preencher as informações de acordo com o estabelecimento que está sendo demonstrado naquela página;
- Incluir ao final da última página das informações de cada estabelecimento a linha 'Total do Estabelecimento <cod_estab>:', e totalizar nessa linha os valores daquele estabelecimento (isso já é feito atualmente mas a linha está descrita apenas como 'Totalização', dificultando o entendimento do relatório);
- Incluir na última página do relatório a linha 'Total da Empresa:' e totalizar nessa linha as informações de todos os estabelecimentos presentes no relatório;
CH55947


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN


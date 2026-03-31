# Impactos_Mapeados_Layout_9

> Fonte: Impactos_Mapeados_Layout_9.docx


REGISTRO I051: PLANO DE CONTAS REFERENCIAL

Estimativa para tratar o escopo referente os itens 1, 2 e 3

1 - Chave alterada de  para




O que fazer no sistema: criar uma validação onde seja possível notificar quais contas referenciais possuem mais de um centro de custo associado. O objetivo é que o cliente ajuste o mapeamento dele com essa validação, pois partimos do princípio de que não será possível ajustar a chave no mapeamento e também já dados cadastrados na tabela de referencial.


2 - Validação da natureza:  Regra na versão anterior REGRA_



O que fazer no sistema: Se não existir tal validação, que seja criada dentro do mesmo contexto da validação acima. A justificativa é a mesma para a criação da validação.


TABELA DE QUALIFICAÇÃO DO ASSINANTE – DISPONIBILIZAR A OPÇÃO NO COMBO DE DADOS INICIAIS NA ABA SIGNATÁRIOS

3 - O que fazer no sistema: Incluir na tabela a opção destacada. Ajuste na view converte o código na descrição ou vice versa (avaliado com o Jorge)



Estimativas para tratar o I051 e a Tabela de Qualificação do Assinante.

Escopo estimado

Disponibilizar uma funcionalidade dentro do DW que hoje está somente no T1;
Criar validações para identificar quais são as contas referenciais que estão associadas a mais de um centro de custo;
Criar validações para identificar quais são as contas referenciais que estão com contas contábeis com natureza divergente;
Ajustar uma view incluindo um código 940 referentes a nova qualificação do assinante;

BA – 6h
DEV- 12h
QA - 20h (estimativa realizada com base no comportamento padrão do Time de QA onde o esforço de uma demanda é equivalente ao estimado pelo Time de DEV).



REGISTRO I151: Deixa de ser gerado a partir do layout 9 – NÃO GERAMOS ESTE REGISTRO NA ECD



O que fazer no sistema: Nada, pois não geramos este registro.



REGISTRO J801: Termo DE Verificação para Fins de SUBSTITUIÇÃO DA ECD – NÃO IMPACTA NO PRODUTO

.

O que fazer no sistema: Nada, a validação é realizado olhando o conteúdo do arquivo, o DW apenas armazena o arquivo e gera na obrigação o conteúdo existente não é validado. Esta função será realizada pelo PVA.



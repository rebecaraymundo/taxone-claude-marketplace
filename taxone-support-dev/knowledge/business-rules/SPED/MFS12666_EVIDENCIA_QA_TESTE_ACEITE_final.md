# MFS12666_EVIDENCIA_QA_TESTE_ACEITE_final

> Fonte: MFS12666_EVIDENCIA_QA_TESTE_ACEITE_final.docx



Tela Incentivos Fiscais






- Ao excluir a base de cálculo, os valores não são apagados, conforme regra
- Se for ajustado o valor da base, (recalcular o o campo Valor Limite 6%) e apagar os demais valores e percentuais.







2.




3.Inicialmente continuava não sendo efetuada a regra abaixo:


Se o valor informado no campo Valor Líquido (FINOR) + Valor Líquido (FINAM)* for maior que o valor informado no campo “Valor Limite 6%, exibir a  mensagem DW00196.





Estamos validando o somatório dos valores liquido (finor + Finan) com a base de cálculo e não com o valor limite de 6%.


Aplicado a nova correção, solução validada com sucesso.




4.



- Menu ajustado conforme abaixo:

Lucro Real>>
Comparativo
Incentivos Fiscais
Demonstração



- Erro ao pesquisar uma Informação ECF (ESTE ERRO JÁ FOI CORRIGIDO PELA LILI)




- Encontrado problema no processamento em lote (erro pre-existente), será tratado na MFS-17798

| Data | MFS | Descrição | Autor |
| --- | --- | --- | --- |
| 10/04/2018 | MFS-12666 | Criação do documento | Alessandra Cristina Navatta |

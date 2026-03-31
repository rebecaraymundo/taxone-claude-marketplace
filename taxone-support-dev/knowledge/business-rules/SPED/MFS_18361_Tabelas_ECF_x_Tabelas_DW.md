# MFS_18361_Tabelas_ECF_x_Tabelas_DW

> Fonte: MFS_18361_Tabelas_ECF_x_Tabelas_DW.docx


Estudo tabelas dos Registros X300 e X310




- NCM não está sendo consistido, apenas quantidade de posição




Conclusão: Não recupera de tabela, só valida 8 posições

- Unidade de medida – PVA
Receita:


Select * from X2007_MEDIDA





select * from PRT_UND_MEDIDA_FCI


select * from IPT_EMB_UND_MEDIDA

select * from IPT_EMB_NCM_MEDIDA



Conclusão: Tabelas diferentes

- MOEDA

Receita:




Conclusão: Tabelas semelhantes, mas na tabela liberada pela Receita (ECF), existe data de início e data fim, as descrições um pouco diferente e o código das moedas não necessariamente possuem 3 posições.

- CNC

Conclusão: Não foi encontrada tabela correspondente no DW

- PAÍS

Conclusão: Tabela encontrada no DW

| Data | MFS | Descrição | Autor |
| --- | --- | --- | --- |
| 15/05/2018 | MFS-18357 | Criação do documento | Alessandra Cristina Navatta |
|  |  |  |  |

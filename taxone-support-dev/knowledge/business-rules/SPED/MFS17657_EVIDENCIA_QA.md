# MFS17657_EVIDENCIA_QA

> Fonte: MFS17657_EVIDENCIA_QA.docx


Receita Bruta



- Erro ao tentar selecionar um perfil na tela de Informações ECF

Este erro está sendo atendido pelo Marcus na demanda 17490



- Está exibindo a msg dw00017 indevidamente:
- Aberto task 18089





Obs, Não está incompatível, não foi preenchido.

- A validação da mensagem dw00017 deve ser considerando os registros que possuem quebra e a quebra está errada.
Na base, só existia parametrização para N500 e N650 que não possui quebra.
Aberto task18089




- Não está sendo exibida a msg dw00050 na tela de associação. Aberto task 18097

- Não está sendo aplicado os percentuais, o valor da receita está igual ao valor calculado.






- Valores a débito não devem ser aplicados percentuais e deve ser exibido dw00156
- 9 – Sobrou na descrição da mensagem o texto código do registro




- Ajustar a descrição da msgDW00156

A receita bruta sujeita ao percentual <<informar percentual formato X,X%>> foi zerada, pois o valor das associações estava com o indicador a débito. Favor avaliar. Registro:<<exibir código do registro>>, Linha:<<2>>



- O valor de 32% está sendo desprezado no total da linha do registro N650. Acredito que esta situação esteja ocorrendo, pois, o percentual de 32 do N500 está com o indicador a debito. Os percentuais devem ser tratados de forma independentes.



10 – Na identificação da msg 208 está sendo exibido os dois registros, na base, este cenário ocorre apenas no n650



11.

O percentual foi calculado corretamente na linha do registro N650, porem no detalhamento está errado.








12. O valor do N500 foi calculado corretamente, porém não atualizou a linha com o somatório do valor total calculado.



| Data | MFS | Descrição | Autor |
| --- | --- | --- | --- |
| 24/04/2018 | MFS-17657 | Criação do documento | Alessandra Cristina Navatta |

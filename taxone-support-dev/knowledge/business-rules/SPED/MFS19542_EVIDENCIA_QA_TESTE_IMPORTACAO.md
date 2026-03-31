# MFS19542_EVIDENCIA_QA_TESTE_IMPORTACAO

> Fonte: MFS19542_EVIDENCIA_QA_TESTE_IMPORTACAO.docx


Importação Bloco W



- Não está sendo possivel importar o arquivo para o Estabelecimento ECF020,  recebo a msg que o CNPJ nao está correto.





Foi necessário ajustar o CNPJ da empresa, pois o mesmo estava sendo utilizado por outras empresas

- Não está sendo exibida corretamente a mensagem DW00255 (está cortando a mensagem)





DW00255: Se a PJ declarante é a controladora final, então o campo <<nome do campo funcional>> só pode ser preenchido com a opção '1' <<descrição da opção>> ou com a opção '2' <<descrição da opção>>.

Ajustamos a descrição da mensagem, pois há uma limitação de 200 caracteres
- A msg DW00214 está sendo exibida uma parte sem acentuação e outra com acentos



CORRIGIDO
- Apresentar apenas o campo jurisdição em Dados do Registro (w300)







- Registro W300 nao está validando a lista de valores válidos dos campos 3 a 12






- Ao importar um registro w300 o mesmo está sendo apresentado mais de uma vez na tela




- Não deve ser exibida a msg DW00261 se o campo 7 está com a soma dos campos 3 e 5 e o campo 8 com a soma dos campos 4 e 6 (w200)









- Campo 8 receita total não é de preenchimento obrigatorio , mas devemos calcular para o usuário, se a informação não for enviada na importação (W200)





Registro W200:
9. Não está sendo identificado corretamente os registros na mensagem DW00271


- Este item está relacionado aos itens 15 e 17

A identificação do registro está correta, mas deve ser implementado a regra indicada no item 17.






- Não está sendo feita a regra destacada em amarelo. Campo obrigatorio condicional.








Registro W100:
- Não está sendo feita a validação destacada do campo modalidade




- Não está sendo feita a validação destacada em amarelo


Registro W250
- O campo ‘Jurisdição de Emissão do TIN’ não é de preenchimento obrigatorio. As validações com o campo ‘4-tax identification number’ preenchido com NOTIN ou diferente de NOTIN devem considerar maiúsculo e minusculo.



W100:

- O campo idioma não está sendo validado conforme as regras







- Não está sendo identificado o registro corretamento no log. Estamos exibindo X200 e X100 o inves de W200 e w100
- Ainda continua com erro


- Este item está relacionado aos itens 9 e 17

- A validação do campo 11 tin_substituta (no registro w100), no cenário abaixo não está sendo feita, pois a tela só aceita 13 posições:
-Se o campo 10 (Jurisdição de Residência da Entidade Substituta), estiver preenchido com 'BR', validar se a informação do campo 11 (Tax Identification Number (TIN) da Entidade Substituta ) é um CNPJ válido.

ESTE ITEM FOI TRATADO EM TELA.


- 17. não está sendo exibida a msg DW00271 qdo o w200 não é permitido




- Este item está relacionado aos itens 9 e 15


18. Por consequência do item 17, implementar a msg DW00180 (para os dois cenários citados na regra abaixo).

Não implementado



19. não está sendo exibido corretamente os labels dos campos (3 e 5 na msg dw00261, do registro W200)











20. O sistema calcula o campo, mas não popula com o valor calculado (campos 7 e 8 do W200)



21. Não está sendo apresentada a msg de forma completa.Ainda continua com erro, conforme item 26 – arquivo w200_3.txt.


Solução mensagem DW00261 alterada para:
Campo VL_REC_TOTAL_EST:
A 'Receita Total em Moeda Estrangeira', deve ser a soma das 'Receitas Partes Nao Relacionadas em Moeda Estrangeira' e 'Receitas Partes Relacionadas em Moeda Estrangeira'. Vlr Calculado: 999999,00

Campo VL_REC_TOTAL:
A 'Receita Total', deve ser a soma das 'Receitas Provenientes de Partes Nao Relacionadas' e 'Receitas Provenientes de Partes Relacionadas'. Vlr Calculado: 999999,00


22. Os campos do W300 de lista, devem ser obrigatórios.

23.  exibindo a mensagem de erro não tratado




24 . registro w200 e w250 não está sendo identificado corretamente




25. Não está sendo possível inserir o w200 e por consequência o w250





OBS. Na tela está sendo possivel inserir w200 . O W250 não ocorre erro ao salvar, mas não é possivel visualizá-lo na tela.




26. continua com erro a descrição da mensagem DW00261

27. taces31 sem o codigo BRL



28. não deveria ser dada a msg de bloqueio do w200.

Indicador de Entidade Controladora Final = S e
Entidade Responsável pela Entrega = 2



29. erro no log





Aceite:
7. Corrigido conforme arquivos w200_3calculadocorretamente.txt e W200_nacional.txt
8. Corrigido arquivo w200_4.txt
9.Corrigido conforme:


10. Corrigido, conforme arquivo W200_Item10_estrangeira_certo.txt
11. Corrigido, conforme arquivo W100_item11_certo.txt
12. Corrigido, conforme arquivo W100_item12_certo.txt
13. Corrigido, conforme arquivo W200_2.txt
14. Corrigido
15. Corrigido conforme item 9
16. ESTE ITEM FOI TRATADO EM TELA.
17.Corrigido confirme itens 9 e 15
18. Corrigido, conforme arquivos W200_nacional.txt e W200_Item10_estrangeira_certo.txt



19. Corrigido, arquivo w200_4.txt
20. Corrigido, arquivo w200_4.txt
21. Corrigido no item 26
22. Corrigido
23. Corrigido conforme :








24. Corrigido conforme:



25. Corrigido
26. Corrigido, conforme arquivos w200_3.txt e w200_nacional_errado.txt
27. Corrigido, conforme arquivo w200_nacional.txt
28.Corrigido, conforme arquivo w200_nacional.txt
29. Corrigido, conforme arquivo w200_nacional.txt






| Data | MFS | Descrição | Autor |
| --- | --- | --- | --- |
| 17/07/2018 | MFS-19542 | Criação do documento | Alessandra Cristina Navatta |

# MTZ-Upload_Registros_M230_M630

> Fonte: MTZ-Upload_Registros_M230_M630.docx



Upload – Informações Adicionais de Diferimento de PIS/PASEP e COFINS – Registros M230/M630
(EFD- Escrituração Fiscal Digital das Contribuições)


DOCUMENTO DE REQUISITO


### REGRAS DE NEGÓCIO





| DR | Nome | Descrição | Data Alteração |
| --- | --- | --- | --- |
| OS3554 | Registros M230/M630 através da funcionalidade Upload | Carregar as Informações Adicionais de Diferimento de PIS/PASEP e COFINS (Registros M230/M630) utilizando a funcionalidade Upload. | 26/06/2012 |


| Cód. |  | DR |
| --- | --- | --- |
|  | REGISTRO FILHO – M230/M630 |  |
| RN01 | Campo 08 - COD_REG Item: 08 Nome do Campo: A ser definido pelo A&D Descrição: Código do registro Tipo: A Tamanho: 010 Comentário: Campo destinado ao código do registro Valores Válidos: M230 M630 Chave Primária Obrigatório | OS3554 |
| RN02 | Campo 09 - CNPJ Item: 09 Nome do Campo: A ser definido pelo A&D Descrição: CNPJ da pessoa juridica de direito publico, empresa publica, sociedade de economia mista ou suas subsidiárias Tipo: A Tamanho: 014 Comentário: Campo destinado ao CNPJ da pessoa juridica de direito publico, empresa publica, sociedade de economia mista ou suas subsidiárias Obrigatório Campo Chave | OS3554 |
| RN03 | Campo 10 – Valor Total das Vendas Item: 10 Nome do Campo: A ser definido pelo A&D Descrição: Valor Total das Vendas no periodo  Tipo: N Tamanho: 015V002 Comentário:  Campo destinado ao Valor Total das Vendas no periodo  Não Obrigatório | OS3554 |
| RN04 | Campo 11 - Valor total não recebido no periodo Item: 11 Nome do Campo: A ser definido pelo A&D Descrição: Valor total não recebido no periodo  Tipo: N Tamanho: 015V002 Comentário: Campo destinado ao Valor total não recebido no periodo Não Obrigatório | OS3554 |
| RN05 | Campo 12 - Valor da contribuição diferida no período  Item: 12 Nome do Campo: A ser definido pelo A&D Descrição: Valor da contribuição diferida no periodo  Tipo: N Tamanho: 015V002 Sendo 015 inteiros e 2decimais Comentário:  Campo destinado ao Valor da contribuição diferida no periodo  Não Obrigatório | OS3554 |
| RN06 | Campo 13  - Valor do credito diferido no período Item: 13 Nome do Campo: A ser definido pelo A&D Descrição: Valor do credito diferido no período  Tipo: N Tamanho: 015V002 Comentário:  Campo destinado ao Valor do credito diferido no período Não Obrigatório | OS3554 |
| RN07 | Campo 14 - Código do tipo de crédito diferido no período  Item: 14 Nome do Campo: A ser definido pelo A&D Descrição: Código do tipo de crédito diferido no período Tipo: A Tamanho: 003 Comentário: Campo destinado ao Código do tipo de crédito diferido no período. Conforme tabela 4.3.6.  Valores Válidos: | OS3554 |
| RN07 | Obrigatório Campo Chave | OS3554 |
| RN08 | Validação do Arquivo:  O campo COD_REG  possui os seguintes valores válidos: M230,M630. Se algum dos campos obrigatórios (Registro Filho: Campo 09 - CNPJ, Campo 14 - Código do tipo de crédito diferido no período) não for enviado, exibir a seguinte msg no log do processo: ‘O Campo <nome_campo_no_layout> e obrigatorio.’ Se  qualquer campo ultrapassar o tamanho definido no layout, só serão importada as primeiras posições até chegar ao tamanho definido no layout. Caso seja enviada uma informação inválida para o campo Código do tipo de crédito diferido no período, exibir a seguinte msg ao usuário: ‘O Código do tipo de crédito diferido no período enviado nao esta de acordo com o Manual de Layout. Valor Informado:XXX’ Ao carregar as informações de um arquivo via UPLOAD e existir na base algum registro que não foi salvo, exibir a seguinte msg ao usuário: Existem dados que ainda não foram salvos. Deseja continuar? Se sim, os registros que estão sendo carregados via Upload serão lidos e os registros não salvos, só serão considerados após o usuário confirmar as informações na tela. Se não, nada será carregado e o usuário poderá salvar os registros que ainda não foram salvos na tela. Ainda sobre o item acima, Se o usuário tentar carregar alguma informação já existente na base, a linha do registro enviada no arquivo deve sobrepor as informações já existentes. Deve ser verificado se o CNPJ informado está valido ou não, considerando a mesma regra existente na tela. Caso contrário, informar: ‘CNPJ inválido’ | OS3554 |

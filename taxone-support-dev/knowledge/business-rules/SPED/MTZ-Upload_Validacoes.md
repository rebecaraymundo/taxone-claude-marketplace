# MTZ-Upload_Validacoes

> Fonte: MTZ-Upload_Validacoes.docx



Upload – Ajustes do Crédito de PIS/PASEP e COFINS – Validações
(EFD- Escrituração Fiscal Digital das Contribuições)


DOCUMENTO DE REQUISITO


### REGRAS DE NEGÓCIO





| DR | Nome | Descrição | Data Alteração |
| --- | --- | --- | --- |
| OS3619 | Validações Ajustes do crédito de PIS/PASEP e COFINS | Validações da funcionalidade Upload para carregar as informações dos ajustes do crédito de PIS/PASEP e COFINS (Registros M220/M620) | 11/06/2012 |


| RN01 | Estrutura do Arquivo:  A primeira linha do arquivo lido deve ter a informação <?xml version="1.0" encoding="ISO-8859-1"?>, caso contrário exibir a seguinte msg de erro: Arquivo lido inválido Se for aberta uma tag e não foi fechada,  exibir a seguinte msg de erro: Arquivo lido inválido Os nomes das tags serão os nomes dos campos na tabela. Necessariamente deverão ser informadas em maiúsculo, (nas tag´s e seus atributos - nivel1/nivel2). Só serão aceitas as tags definidas no layout. Caso seja enviada uma tag que não foi definida, a mesma será desprezada na leitura do arquivo. Caso seja enviada em um arquivo a mesma tag para o mesmo registro, iremos considerar a informação da última tag encaminhada.  Campos numéricos inválidos. Não é permitido em campos numéricos, caracteres especiais e letras. Exibir a seguinte msg no log: Nao foi possivel converter o valor informado no arquivo para um valor numerico valido. Valor informado: XXXX Campos de data devem ser enviados com a formatação ‘AAAAMMDD’ , caso contrário, exibir a seguinte msg: Nao foi possivel converter o valor informado no arquivo para uma data valida. Valor informado: XXXXX Campos alfanuméricos inválidos.Exibir a seguinte msg: Nao foi possivel converter o valor informado no arquivo para um  valor alfanumerico valido. Valor informado: XXXX Caso o usuário informar um valor maior que o determinado em layout, os caracteres que estiverem a mais serão descartados.  Todas as mensagens do log deve conter a linha do registro com o problema, facilitando assim a identificação da situação para o usuário. A informação linha deve conter uma numeração sequencial (que não pode ter repetição) independente da quebra de pai/filho Caso o campo esteja obrigatorio e venha informação nula ou não seja informado no arquivo: O Campo <nome_campo_no_layout> e obrigatorio. | OS3169 |
| --- | --- | --- |

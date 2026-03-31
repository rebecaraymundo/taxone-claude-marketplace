# MFS14482_EVIDENCIA_QA

> Fonte: MFS14482_EVIDENCIA_QA.docx


Tela Informações ECF





- Ao pesquisar registros no botão abre, não está sendo exibido os labels dos campos com nome funcional. E estão sendo exibidos mais campos que os existentes na tela.



Regra Requisito





- Não estamos respeitando a regra abaixo no campo versão:

Se o resultado da recuperação trouxer mais de uma versão, apresentar a de Data Inicial mais atual.




- A aba Parametros dos Tipos de Programa se utilizada a versão 3.00, não está sendo habilitada




- Colocar o título Lançamento de Encerramento


- A descrição da mensagem correta é ‘Já existe na base um registro com as mesmas informações’, ao tentar inserir um registro na base com os mesmos dados.


- Não está dando a mensagem de registro inserido com sucesso, desta maneira, o usuário não sabe se o registro foi ou não inserido na base. Exibir a descrição da
- DW00008: Registro inserido com sucesso!





- A regra abaixo não está sendo aplicada corretamente. Parece que ela respeita o intervalo do ano anterior mas, não atende o trecho até o ultimo dia do ano do exercício. Favor verificar



- A busca das associações devem ser feitas pelo código e descrição das associações. Considerando a versão igual da parametrização.

- A busca do perfil devem ser feita pelo código e descrição do perfil. Considerando a versão igual da parametrização.


- A lista de valores válidos para o campo Escrituração são
- Lista – Valores Válidos:
- -Não se aplica
- -Livro Caixa ou Sem Escrituração
- -Contábil

- A busca da conta contábil e centro de custo devem ser feitas pelo código e descrição dos mesmos. Considerando as contas da parametrização da associação de tabela referencial com o plano empresa e natureza Patrimônio liquido (para a conta contábil).

- Ocorreu o erro abaixo, ao tentar salvar o registro. Acredito que esteja relacionado ao parâmetro PJ Habilitada no Repes, Recap, Padis, ... (vide ícone “i”), não estar marcado.



13 – Ao tentar gravar um registro está dando a mensagem de campo obrigatório não preenchido, mas não consegui identificar o campo




14 – Ao gravar um registro na base, ao efetuar a consulta do mesmo, consegui marcar um tipos de programa, mesmo sem marcar o parâmetro PJ Habilitada no Repes, Recap, Padis, ... (vide ícone “i”)





15 – o parâmetro Regime Especial de Incentivos para o Desenvolvimento da Infraestrutura (Reidi), vem antes do Regime Especial de Incentivos para  o  Desenvolvimento da Infraestrutura  da  Indústria  Petrolífera  das  Regiões  Norte,  Nordeste e Centro-Oeste (Repenec)



16 – Consegui gravar um registro de forma de tributação igual a Lucro Real, Lucro Presumido, Lucro Arbitrado, sem ter preenchido o campo PJ Sujeita à Alíquota da CSLL






17 . o campo qualificação do assinante (signatários outros) não está como obrigatório.




18. Tentei salvar o registro como o parâmetro PJ Habilitada no Repes, Recap, Padis, ... (vide ícone “i”) marcado, mas não habilitou a aba Tipos de Programas, desmarquei o parâmetro PJ Habilitada no Repes, Recap, Padis, ... (vide ícone “i”) e ao salvar, exibiu o erro abaixo:







18 – mesmo possuindo uma abertura, o campo forma de tributação pode ser alterado. Além disso, foi permitido gravar uma informação ECF com o campo Apuração preenchido com Anual, sendo que a alteração foi para Forma de Trubutação  Imune de IRPJ e o campo tipo de entidade em branco.







19. Nos dois campos de associações (tabela dinâmica e referencial),  foi inserida a validação:

Na edição do registro, este campo deve estar não editável:
- Se existir uma abertura de apuração criada para esta Informação ECF com status diferente de Apuração em Aberto.


20. Não está sendo respeitada a regra na exclusão do registro:

Ao clicar no botão e o sistema encontrar uma Informação ECF sem criação de abertura da apuração, permitir a exclusão do registro, exibindo a mensagem de confirmação padrão do sistema e se o usuário confirmar, mostrar a mensagem do sistema de Registro Excluído com Sucesso. Caso o usuário selecione ‘Não’, o registro não deve ser excluído.

Sem abertura de apuração:

Exclui o registro direto sem dar mensagem de confirmação.

Com abertura de apuração:
Criada a msg DW00125

Se existirem aberturas da apuração com status igual:
“Apuração em Aberto” ou “Importação de Saldos Realizada” ou “Alteração Manual Realizada” ou “Aguardando Alteração Manual” ou “Reapurar” , permitir a exclusão do registro, se o usuário clicar em Sim para a mensagem DW00125 e depois mostrar a mensagem do sistema de Registro Excluído com Sucesso. Caso o usuário selecione ‘Não’, o registro não deve ser excluído.



21 – Não estamos considerando o campo escrituração como campo obrigatório. E a regra abaixo não está sendo atendida




Se o campo  Se “Forma de Tributação” estiver preenchida com a opção ‘Lucro Real, Lucro Presumido, Lucro Arbitrado’ e o campo _ Critério de Reconhecimento de Receitas igual a ‘Regime de Caixa’,o campo escrituração só pode ser preenchio com as opções ‘Livro Caixa ou Sem Escrituração’ e  ‘Contábil ‘, caso contrário, exibir a mensagem DW00065.


22 – Ao tentar excluir uma informações ecf recebemos a mensagem abaixo




| Data | MFS | Descrição | Autor |
| --- | --- | --- | --- |
| 09/11/2017 | MFS-14482 | Criação do documento | Alessandra Cristina Navatta |


| RNG00009 | Data Inicial x Exercício | O campo data inicial deve estar compreendida no intervalo do ano anterior até o último dia do ano do exercício, caso contrário, exibir a seguinte msg ao usuário: DW00029.  Exemplo: Exercício 2014 Data Inicial: (entre 01/01/2013 à 31/12/2014) |
| --- | --- | --- |

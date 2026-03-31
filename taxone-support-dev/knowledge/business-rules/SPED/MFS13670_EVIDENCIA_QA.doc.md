# MFS13670_EVIDENCIA_QA.doc

> Fonte: MFS13670_EVIDENCIA_QA.doc.docx


Tela de Associação da Tabela Dinâmica com o Plano Empresa

- Não está sendo gravado a informação de data inicial e final das contas quando a informação é inserida diretamente na grid.
Aplicar a mesma solução para a tela de Associação do plano referencial com o Plano Empresa.

- Ao clicar no botão pesquisar , deixando o campo “Informar Código/Descrição para Pesquisa” sem preenchimento, é exibido o erro abaixo:




- Quando o registro possui informação de data (vigência da conta) , ao selecionar o botão “Adicionar Informação Adicional”, essas datas não são recuperadas no modal
Este item não será tratado





- Sugestao de modal

Mensagem fixa da tela :

Poderá ser incluído um Percentual de Receita Bruta para a linha 2 dos registros N500 e N650. Se uma conta contábil associada a esta linha utilizar o percentual , tal informação deve ser adicionada a todas as demais contas. Caso a conta possua detalhamento por centro de custo, o percentual deve ser informado por centro de custo, e o valor por conta, se informado, será descartado.





- Deixar o campo Percentual com o fundo cinza (deixando realmente claro na abertura da tela, que o campo está desabilitado), para as linhas 2 dos registros diferente de N500 e N650 ?

Padrão do DW exibir o campo em branco quando desabilitado. Este item não será ajustado.


Aplicar a mesma coisa na grid:



- Não exibir o botão de adicionar Informação Adicional no componente de centro de custo para registros diferente de N500 e N650 (linha 2).

- Tem um ponto de interrogação nos campos de pesquisa do centro de custo


- Ao pesquisar um centro de custo que não existe o sistema está se perdendo. Só reaparece a associação se trocar a linha da tabela dinâmica.
















- Se pesquiso um código de conta que não existe e o primeiro registro na base tem centro de custo, não estamos limpando as informações do componente de centro de custo


- Filtro na pesquisa um código de conta que não existe, não está sendo limpo as informações do componente de centro de custo.


- 10 – tooltip correto Adicionar Informação Complementar (nos dois componentes)



- 11- Nome do modal Adicionar Informação Complementar na Conta da Empresa
- Este item deve ser feito também para a tela de Associação do plano referencial com o Plano Empresa.





- 12- Nome do modal Adicionar Informação Complementar no Centro de Custo


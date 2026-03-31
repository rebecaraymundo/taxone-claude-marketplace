# MFS12706_EVIDENCIA_QA.doc

> Fonte: MFS12706_EVIDENCIA_QA.doc.docx



1 – Alterar o label do campo Plano de Contas para Grupo

2 -  Na grid do plano referencial alterar o label do campo Associações para Associação de Contas Contábeis. No resultado apresentar apenas a quantidade das contas contábeis.

3 – Ajustar o Nome do componente e dê “Plano de Contas Referenciais” para “Plano de Contas Referencial”

4 – Ajustar a o nome da opção “Remover” da barra de ação para “Remover Associação” e “Pesquisar/filtrar” para “Pesquisar” (nos 3 componentes: Plano Referencial, Plano de Contas Empresa e Centro de Custo)

5- Existem contas de natureza nula a ser inserida no Componente de Plano de Contas da Empresa

6 –  Colocar o campo registro acima da barra de ações do componente de Plano de Contas Referencial



7 – Erro ao selecionar uma conta de natureza nula.





8 – Não está sendo possível alterar a data inicial, grupo e versão antes de salvar um registro.

9 – Não está exibindo a msg DW00001 qdo campos obrigatórios não foram preenchidos. (Verificar item 48) Continua não sendo respeitada.



10 – O sistema está permitindo incluir uma data de vigência anterior a data da associação. Não está respeitando a regra abaixo



11  - Título da janela da Tela coincidir com o titulo do Menu : Associação do Plano Referencial com o Plano Empresa

12 – Se uma conta contábil estiver associada a uma conta referencial, ela pode ser associada a uma outra conta referencial. Isto não está sendo permitido.

13 – Barra de rolagem nos componentes de Plano de Contas da Empresa e Centro de Custo.

14 – Alterar o nome do modal “Selecionar Contas Empresas”, para “Associar Contas da Empresa”

15 – Alterar o nome da opção “Adicionar Informação Compl.” da barra de ação, para “Associar Informação Complementar” (componente de Plano de Contas da Empresa)

16 – Alterar o nome do modal “Selecionar Centro de Custo para “Associar Centro de Custo”

17 – No componente de Centro de Custo, ter apenas o label Centro de Custo (na grid). Na apresentação do resultado exibir o código- descrição do centro de custo.


18 – Utilização de filtros na janela de seleção


19 – Corrigir a quantidade da coluna associações (plano de contas referenciais e empresa)

20- Retirar colunas ident das pesquisas


21 – Ao escolher uma parametrização pelo “Abre”, o sistema apresenta o cabeçalho atualizado com a parametrização selecionada, mas não limpa os quadros seguintes “Plano de Contas Referenciais”, “Plano de Contas Empresa” e “Centro de Custo”. Esses quadros estão apresentado dados da parametrização anterior a nova escolha pelo “Abre”.



22 – A mensagem exibida não tem a descrição da DW00010




23  - Na inclusão do registro quando o campo data inicial é alterado não está sendo limpo a informação de todos os campos do cadastro.

24 – A regra abaixo não está sendo realizada:
Se não for encontrado nenhum grupo de estabelecimento  vigente na data inicial da parametrização, exibir a mensagem DW00046. Continua com problema, verificar item 53 e 62

25 - A regra abaixo não está sendo realizada:
-Na inclusão de registro, se for alterado o grupo, o cabeçalho seguirá com os mesmos dados cadastrados anteriormente, exceto o campo Versão. O campo Registro se preenchido, também será limpo.
Ajustada a regra. Se o grupo for alterado, os campos não devem ser apagados.

26 – Não está sendo limpo o campo registro ao mudar a versão da parametrização:
-Na inclusão de registro, se for alterado a versão da tabela referencial, o cabeçalho seguirá com os mesmos dados cadastrados anteriormente. O campo Registro será limpo, se preenchido. Problema novo pontuado no item 52

27 - A regra abaixo não está sendo realizada:
Se não for encontrado nenhuma versão de tabela referencial vigente na data inicial da parametrização, exibir a mensagem DW00005.

28 – Não sei se este item está relacionado ao item 19...
Ao inserir uma associação nova, as contas referenciais já estão sinalizando associações de contas contábeis.



29 – Ao excluir associações (contas contábeis), o erro abaixo é exibido e a tela é fechada



30- Avaliar possível problema de performance ao inserir todos os centro de custo na conta contábil (mais de dois minutos para salvar os registros)

Não foi identificado problema de performance por dev



31 – Apresentar na funcionalidade “Abre” o campo Grupo e não Grupo Conta





32 – a ação de remover associação, só deve ser habilitada se uma conta referencial for selecionada. (Componente de Plano de Contas Referencial)
Essa regra deve ser respeitada em todos os componentes.
Item classificado como melhoria

33- Só habilitar a barra de ação se o campo Registro for preenchido (componente de Plano de Contas Referencial)
Item classificado como melhoria


34- Só habilitar a barra de ação se pelo menos uma conta contábil for inserida (componente de Plano de Contas da Empresa)
Item classificado como melhoria

35- Só habilitar a barra de ação se pelo menos um centro de custo for inserido (componente de Centro de Custo)
Item classificado como melhoria

36 – No modal de associar contas da empresa, na grid, apresentar o label Código e não Código Conta



37 – O sistema está permitindo salvar uma associação sem nenhum registro de conta contábil

(-Se não existir pelo menos uma conta contábil associada em uma conta da tabela de conta referencial, exibir a DW00009 e não gravar o registro.)



38 – Ao gravar um registro a msg DW00008 não está sendo exibida.


39. Criada as msgs abaixo, para validação da funcionalidade de remover associações. Problema novo pontuado no item 50.

40 – O sistema não permite excluir uma associação.



41 – Modal de Pesquisa do Plano de Contas da Empresa, apresentar apenas os campos (respeitando os labels) Código, Descrição e Natureza



42 – Modal de Pesquisa do Centro de Custo, apresentar apenas os campos (respeitando os labels) Código, Descrição. Continua com erro, verificar item 57



43 – Erro ao tentar pesquisar conta contábil



44   - A mensagem abaixo está sendo exibida, mesmo quando há associações em outras contas referenciais. Melhoria

Atualmente não está sendo permitido efetuar esta validação por associação, apenas por conta referencia que está sendo selecionada.




45 – Ocorreu esse erro ao entrar na opção Associar Centro de Custo


46 – O alterar o nome do componente “Centro de Custo Empresa” para “Centro de Custo”

47 – O alterar o nome do componente “Plano de Contas Empresa” para “Plano de Contas da Empresa”

48 – Não está dando a mensagem de campo obrigatório não preenchido Ainda não foi corrigido verificar item 67.



49 – Incluir o botão de remover associação, para a ultima opção da barra de ação (nos três componentes)
Este item, por enquanto não foi possível ser implementado.

50 – Ajustar a descrição da msg conforme DW00041 - Atenção! Nenhuma linha foi selecionada. Ainda não foi corrigido.



51 – Alterar o nome da opção “Associar Informação Complementar”  da barra de ação, para “Adicionar Informação Complementar” (componente de Plano de Contas da Empresa)

52 - Não está sendo limpo as informações das contas referenciais ao mudar a versão da parametrização:





53 – Ao invés de exibir a mensagem DW00046 está sendo exibida a msg abaixo Ainda não está correto, verificar item 62


54 – Ao preencher o campo de data final (vigência da conta contábil), ocorre o erro abaixo:



55- Ao tentar selecionar o pesquisar, sem colocar nenhuma informação de conta  ou descrição ocorre o erro abaixo



56- Ao tentar excluir uma associação existente na base (se não selecionar o registro), ocorre a msg abaixo indevidamente. Melhoria
Atualmente não está sendo permitido a exclusão de uma associação por completo.Foi inserido uma msg pedindo ao usuário selecionar um registro (conforme telas abaixo)




Mensagem implementada solicitando o registro:



57 –

Modal de Pesquisa do Centro de Custo, apresentar apenas os campos (respeitando os labels) Código, Descrição (grid de resultados).
Alterar o label do campo ’Informar Conta/Descrição para Pesquisa’ por ’Informar Código/Descrição para Pesquisa’ e ‘Conta’ para ‘Código’



58 – Componente Plano de Contas Referencial

Alterar o label do campo ’Informar Conta/Descrição para Pesquisa’ por ’Informar Código/Descrição para Pesquisa’ e ‘Conta’ para ‘Código’




59 – Ao entrar na opção Associar centro de custo e fechar pelo X, ocorre o erro abaixo




60 – Ao incluir conta em qualquer associação, recebo o erro abaixo, mas a conta acaba sendo inserida na base.



61 – Ao tentar associar conta contábil ocorre o erro abaixo Verificar item 63




62 – Ainda não está sendo apresentado a mensagem DW000046 quando não há grupo vigente na data inicial



63 – Ocorre o erro abaixo, ao entrar no modal de Associar Conta Contábil, fechar a tela pelo X e depois entrar novamente no modal de Associar Conta Contábil



64 – Ocorre o erro abaixo, ao entrar no modal de Associar Centro de Custo fechar a tela pelo X e depois entrar novamente no modal de Associar Centro de Custo



65 – Ao entrar no modal de Associar Informações Adicionais sem selecionar nenhuma linha e depois entrar no Remover Associação, ocorre o erro abaixo




66 – Ao excluir a associação da conta referencial, o sistema não está atualizando o campo Associação de Contas Contábeis.



67 – Não está dando a mensagem de campo obrigatório não preenchido



68 – Ao criar uma associação na conta referencial e depois efetuar a exclusão das contas contábeis associadas nesta referencial, o sistema exibe a msg abaixo, mas, o registro é salvo na base. Melhoria
Criar validação ao excluir todas as associações (pelo remover do componente de Contas Referenciais), informando ao usuário que se a exclusão for realizada, será excluída tb a associação.








Consultando o registro na base:





69 – Encontrado erro abaixo:







| Data Inicial | N | DD/MM/AAAA | A data inicial da vigencia da conta,  deve ser igual ou maior que a data inicial da parametrização. Caso contrário, exibir a mensagem DW00010. |
| --- | --- | --- | --- |


| DW00041 | Atenção! Nenhuma linha foi selecionada. | Aviso | DW-ECF | Informações ECF | 12706 |
| --- | --- | --- | --- | --- | --- |
| DW00042 | Atenção! Não existe nenhuma associação a ser removida. | Aviso | DW-ECF | Informações ECF | 12706 |

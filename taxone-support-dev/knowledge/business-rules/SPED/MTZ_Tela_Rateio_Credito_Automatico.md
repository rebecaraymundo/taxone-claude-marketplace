# MTZ_Tela_Rateio_Credito_Automatico

> Fonte: MTZ_Tela_Rateio_Credito_Automatico.docx



## (EFD-PIS/PASEP – COFINS) – Ajustes no Crédito do Rateio Proporcional dos Registros M105/M505 - Receita Cumulativa


DOCUMENTO DE REQUISITO





REGRAS DE NEGÓCIO








| MFS | Nome | Descrição | Data alteração |
| --- | --- | --- | --- |
| MFS-758276 | Rosemeire Santos | Criação da Tela de Parâmetro | 06/03/2025 |


| Cód. |  | MFS |
| --- | --- | --- |
| RN01 | Criação da Tela de parâmetro no Módulo: EFD_Escrituração Fiscal Digital das Contribuições Menu: Parâmetros > Ajustes no Crédito do Rateio Proporcional dos Registros M105/M505 – Receita Cumulativa | MFS-758276 |
| RN02 | Inclusão Campos:  Estabelecimento Centralizador*: seleção de estabelecimento. Alíquota PIS (em %) *: Campo de preenchimento da Alíquota do PIS Alíquota COFINS (em %) *: Campo de preenchimento da Alíquota do COFINS CST PIS*: Campo de seleção de Código de Situação Tributária do PIS CST COFINS*: Campo de seleção de Código de Situação Tributária do COFINS Cód. Tipo de Crédito*: Campo de seleção do código do tipo de crédito Nat. da Base de Crédito*: Campo de seleção da Nat. da Base de Crédito | MFS-758276 |
| RN03 | Botões/Ícones Tela:  Confirmar: Opção para salvar a regras que está sendo criada no sistema, caso tente salvar as informações sem preencher todos os campos obrigatórios, o sistema apresentará uma mensagem indicando que há campos obrigatórios não preenchidos.  Limpar: Opção para limpar os parâmetros que foram preenchidos na tela, caso tenha ao menos um campo obrigatório preenchido, é apresentada a mensagem "Atenção! Existem dados salvos não confirmados que serão perdidos. Deseja continuar?" com opções de "Sim" e "Não". Se sim, a tela é "limpa". Se não, nada ocorre.  Copiar: Opção para copiar uma regra já pronta e fazer os ajustes necessários para uma próxima ação, sem precisar digitar todos os dados novamente. Esta opção não vai ser via botão em tela, e sim uma opção na própria GRID da exibição das regras  Remover: Opção para exclusão de alguma regra disponível. Esta opção não vai ser via botão em tela, e sim uma opção na própria GRID da exibição das regras  Limpar o formulário ao salvar: Opção limpa todos os parâmetros que foram preenchidos na tela, para iniciar nova parametrização.  Mensagens: Ação: REMOVER| Texto da mensagem: "Confirma a exclusão?"| Tipo de mensagem/componente: Popup | É apresentada a mensagem "Confirma a exclusão?" com opções de "Sim" e "Não". Se sim, formulário é limpo e grid atualizada. Se não, nada ocorre. Ação:  CONFIRMAR | Texto da mensagem: "Dados salvo com sucesso" | Tipo de mensagem/componente: Popup Ação:  FECHAR | Texto da mensagem: Caso tenha dados que foram editados “Atenção! Existem dados salvos não confirmados que serão perdidos. Deseja continuar?" | Tipo de mensagem/componente: Popup | É apresentada a mensagem “Atenção! Existem dados salvos não confirmados que serão perdidos. Deseja continuar?" com opções de "Sim" e "Não". Se sim, a tela é "fechada". Se não, nada ocorre.  Ação:  LIMPAR | Texto da mensagem: Caso tenha dados que foram editados “Atenção! Existem dados salvos não confirmados que serão perdidos. Deseja continuar?" | Tipo de mensagem/componente: Popup | É apresentada a mensagem “Atenção! Existem dados salvos não confirmados que serão perdidos. Deseja continuar?" com opções de "Sim" e "Não". Se sim, a tela é "limpa". Se não, nada ocorre.   Processo Tela de parâmetro:  Os parâmetros criados em tela para Ajustes no Crédito do Rateio Proporcional dos Registros M105/M505 – Receita Cumulativa, não é permitido terem campos repetidos por serem chaves, pelo menos um deve ser diferente. | MFS-758276 |

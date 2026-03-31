# MTZ_Tela_Razao_Auxiliar_Subcontas

> Fonte: MTZ_Tela_Razao_Auxiliar_Subcontas.docx






THOMSON REUTERS

Matriz da tela do Livro Razão Auxiliar das Subcontas



DOCUMENTO DE REQUISITO


Sumário

1.	TELA A SER DESENVOLVIDA	3
1.1.	Diagrama de Casos de Uso	3
1.1.1.	UC001 – Manutenção da Estrutura Padrão	3
1.1.1.1.1.	Fluxo Principal	4
1.1.1.1.2.	Fluxo Alternativo 1 – Novo Registro	4
2.	Regras dos Campos	4

## TELA A SER DESENVOLVIDA


[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir]

### Diagrama de Casos de Uso




### UC001 – Manutenção da Estrutura Padrão


[Descrever a ação deste caso de uso.

Ex.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão.]



#### Fluxo Principal



#### Fluxo Alternativo 1 – Novo Registro




## Regras dos Campos


Localização da tela:
Módulo: SPED >> ECD – Escrituração Contábil Digital
Menu: Manutenção

Título da tela: Razão Auxiliar das Subcontas

Funcionamento da tela: esta tela foi criada para armazenar e manutenir as informações referentes à SAFX179 – Livro Razão Auxiliar das Subcontas.

No acesso à tela o sistema deve exibir a tela padrão de seleção de Estabelecimento/Grupo/Validade:



Na barra de ferramentas, deve existir o botão de seleção de Grupo:


* Descrição não disponível em tela



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-2711 | Marcos G. de Paula | Definição das regras da tela do Livro Razão Auxiliar das Subcontas. |
|  |  |  |


| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | Usuário do Sistema. |
| Pré- Condições | Estar logado no produto MasterSAF DW. |
| Pós-Condições | Não se aplica. |


| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  |  |


| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  | Fim do fluxo Alternativo |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento: | Dropdown | S | S |  | Será preenchido com o código + razão social do estabelecimento que foi selecionado na tela de Estabelecimento/Grupo/Validade no acesso à parametrização. | MFS-2711 |
| Cód. Livro Auxiliar | Pasta de Seleção padrão + Editbox | S | S |  | Deve possibilitar a seleção do Código do Livro Auxiliar que foi cadastrado na Tela “Livros Auxiliares ao Diário” (Módulo: SPED >> ECD – Escrituração Contábil Digital / Menu: Parâmetros), cujo tipo de livro esteja preenchido com a opção “Z – Razão Auxiliar (Livro Contábil Auxiliar conforme leiaute definido nos registros I500 a I555)” E que não tenha sido cadastrado na Tela  “Impressão do Livro Auxiliar” (Módulo: SPED / ECD – Escrituração Contábil Digital, Menu: Parâmetros).   Caso o usuário digite um código que não atenda aos critérios acima indicados, retornar mensagem no campo: “Não existe cadastro na tela de “Livros Auxiliares ao Diário” com Tipo “Z – Razão Auxiliar” para o Código do Livro indicado”.  Como o campo é de preenchimento obrigatório, deve ser exibida mensagem de erro caso não esteja preenchido: “Código do Livro Auxiliar não informado”. | MFS-2711 |
| Natureza da Subconta | Pasta de Seleção padrão + Editbox | S | S |  | Deve possibilitar a seleção do Código da Natureza da Subconta na TACES90, considerando registro cuja data de atualização da taces seja menor ou igual à Data do Lançamento Contábil informada no registro que está sendo importado.  Caso o usuário digite um código que não atenda aos critérios acima indicados, retornar mensagem no campo: “Código da Natureza da Subconta Correlata não cadastrado na TACES90”.  Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Natureza da Subconta não preenchida”. | MFS-2711 |
| Código da Subconta (Grupo/Cód./Descrição) | Pasta de Seleção padrão + Editbox | S | S |  | Deve possibilitar a seleção do Código da Subconta na tabela SAFX2002, com Data Início/Inclusão/Alteração menor ou igual a Data do Lançamento Contábil e que pertença ao grupo selecionado no acesso à tela.  Caso o usuário digite um código que não atenda aos critérios acima indicados, retornar mensagem no campo: “Plano de Contas não encontrado”.  Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Código da Subconta correlata não preenchida”. | MFS-2711 |
| Centro de Custos (Grupo/Cód./Descrição) | Pasta de Seleção padrão + Editbox | N | S |  | Deve possibilitar a seleção do Código do Centro de Custos na tabela SAFX2003, com Data Início/Inclusão/Alteração menor ou igual a Data do Lançamento Contábil e que pertença ao grupo selecionado no acesso à tela.  Caso o usuário digite um código que não atenda aos critérios acima indicados, retornar mensagem no campo: “Centro de Custo não encontrado”. | MFS-2711 |
| CNPJ da Empresa Investida | Editbox | N | S | Formato: XX.XXX.XXX/XXXX-XX | Caso seja informado um CNPJ, verificar se o código informado é válido, conforme função padrão de validação de CNPJ. Caso não seja, retornar mensagem de erro: “CNPJ inválido”. | MFS-2711 |
| Cód. Item (ativo/passivo) | Editbox | S | S |  | Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Código do Item (ativo/passivo) não preenchido”. | MFS-2711 |
| Código Individualizado do Bem | Editbox | S | S |  | Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Código Individualizado do Bem não preenchido”. | MFS-2711 |
| Desc. Resumida do Bem | Editbox | N | S |  |  | MFS-2711 |
| Data Reconhecimento Contábil do Item | Editbox | S | S | Formato: DD/MM/AAA | Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Data do Reconhecimento Contábil do Item não informada”. | MFS-2711 |
| Data do Lançamento Contábil | Editbox | S | S | Formato: DD/MM/AAA | Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “O Campo de Data do Lançamento Contábil deve ser preenchido”. | MFS-2711 |
| Número do Lançamento | Editbox | S | S |  | Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “O Número do Lançamento não pode ser nulo”. | MFS-2711 |
| Quantidade Inicial do Item | Editbox | N | S | Formato: 0,00 |  | MFS-2711 |
| Saldo Inicial da Conta que Reg. o Item | Editbox | N | S | Formato: 0,00 |  | MFS-2711 |
| Débito / Crédito | Radio Button | N | S | Default: Débito | Opções disponíveis: Débito Crédito | MFS-2711 |
| Realização do Item | Editbox | N | S | Formato: 0,00 |  | MFS-2711 |
| Débito / Crédito | Radio Button | N | S | Default: Débito | Opções disponíveis: Débito Crédito | MFS-2711 |
| Saldo Final da Conta que Reg. o Item | Editbox | N | S | Formato: 0,00 |  | MFS-2711 |
| Débito / Crédito | Radio Button | N | S | Default: Débito | Opções disponíveis: Débito Crédito | MFS-2711 |
| Saldo Inicial na Subconta Antes do LC | Editbox | N | S | Formato: 0,00 |  | MFS-2711 |
| Débito / Crédito | Radio Button | N | S | Default: Débito | Opções disponíveis: Débito Crédito | MFS-2711 |
| Débitos da Subconta | Editbox | N | S | Formato: 0,00 |  | MFS-2711 |
| Créditos da Subconta | Editbox | N | S | Formato: 0,00 |  | MFS-2711 |
| Saldo Final na Subconta Após do LC | Editbox | N | S | Formato: 0,00 |  | MFS-2711 |
| Débito / Crédito | Radio Button | N | S | Default: Débito | Opções disponíveis: Débito Crédito | MFS-2711 |
| Valor do Lançamento Contábil | Editbox | N | S | Formato: 0,00 |  | MFS-2711 |
| Débito / Crédito | Radio Button | N | S | Default: Débito | Opções disponíveis: Débito Crédito | MFS-2711 |
| Indicador de Registro Relativo a Adoção Inicial | Radio Button | N | S | Default: SIM | Opções disponíveis: 1 – SIM 2 – NÃO | MFS-2711 |

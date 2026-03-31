# MTZ_REINF_Tela_Lancamento_Deducoes_Comercializacao_Producao_Rural

> Fonte: MTZ_REINF_Tela_Lancamento_Deducoes_Comercializacao_Producao_Rural.docx






THOMSON REUTERS

Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria

EFD-REINF

Localização: Menu SPED, módulo EFD - REINF, menu Parâmetros  Lançamento de Deduções da Comercialização da Produção por Produtor Rural PJ/Agroindústria
Localização: Menu SPED, módulo EFD - REINF, menu Parâmetros  Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria


DOCUMENTO DE REQUISITO


Sumário

1.	Layout da Tela	3
2.	Regras dos Campos	5
3.	Regras dos Campos - Processos	9


























## Layout da Tela


Título da tela: Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria

Alteração MFS21937: Originalmente, esta manutenção trabalhava apenas com valores de dedução. Nesta MFS foi criado o campo “Tipo de Ajuste”, para permitir o lançamento de valores tanto de dedução como de adição. Para isso, o menu foi renomeado para “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”.

Alteração MFS27483: Inclusão do botão “Processos”, cuja função será abrir uma janela e permitir a manutenção dos processos associados ao Período, Indicativo de Comercialização e Tipo de Ajuste informados.

Campos chave: Empresa, Estabelecimento, Competência (Mês/Ano), Indicativo de Comercialização e Tipo de Ajuste (MFS21937)

A tabela “filha” (botão Processos) segue a chave da tabela principal + dados de identificação do Processo




Processos:









## Regras dos Campos



Regra Geral Botões:

NOVO – Permite inserir novo registro.

ABRE – Permite abrir seleção de registros inseridos.

EXCLUI – Permite excluir registro inserido.

CONFIRMA – Permite salvar registro.

RELATÓRIO – Permite emitir relatório listando todos os registros existentes na base de dados ou de acordo com a Empresa e Estabelecimento selecionados na tela de login (mostrar apenas os campos obrigatórios como critério de busca).

FECHA – Permite sair da tela.

Regra Geral:

Podem existir vários cadastros




## Regras dos Campos - Processos


(A opção “Processos” foi incluída na manutenção dos ajustes na MFS27483 - Out/2019)

Na janela “Processos” o usuário poderá informar ‘n’ processos, e os respectivos valores, para o Período, Indicativo de Comercialização e Tipo de Ajuste em questão.

O objetivo é permitir ajustes nos valores das contribuições com exigibilidade suspensa. As informações cadastradas nesta opção, serão utilizadas na Geração Prévia dos Movimentos, para ajustes no registro infoProc do evento R-2050.







= = = = = =

| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS17263 | Lara Aline | Inclusão da Tela de Lançamento de Deduções da Comercialização da Produção por Produtor Rural PJ/Agroindústria do EFD – Reinf |
| MFS20930 | Lara Aline | Inclusão do novo tipo de comercialização, de acordo com o Layout 1.4. |
| MFS21937 | Vânia Mattos | Alteração da manutenção das deduções do evento R-2050 para permitir lançamentos tanto de dedução, como de adição. Devido à alteração, o nome do menu também foi alterado. |
| MFS27483 | Vânia Mattos | Alteração na manutenção dos ajustes do evento R-2050 para inclusão do botão “Processos”. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | TextBox | S | S | Default = Não selecionado | Nesse campo serão listados todos os estabelecimentos da empresa logada, que usuário tenha permissão de acesso e que possuam o cadastro das Informações do Contribuinte preenchido  Caso não preenchido exibir a seguinte mensagem: O Estabelecimento deve ser informado. | MFS17263 |
| Competência (Mês/Ano) | Data | S | S | MM/AAAAA | Caso não preenchido exibir a seguinte mensagem: “Competência (Mês/Ano) deve ser informado” | MFS17263 |
| Tipo de Ajuste  (campo criado na MFS21937) | Radio Button | S | S | Opção “Dedução” | Este campo apresenta as opções “Adição” e Dedução” para escolha do usuário.  As opções são alternativas, e o default é a opção “Dedução”.  Internamente o campo é gravado com o seguinte conteúdo:  “1” – Para a opção “Adição”; “2” – Para a opção “Dedução”; | MFS21937 |
| Indicativo de Comercialização | DropDown | S | S | Default = Não selecionado | Informar o Tipo de comercialização, conforme lista a seguir:  1 - Comercialização da Produção por Prod. Rural PJ/Agroindústria, exceto para entidades executoras do PAA; 7 - Comercialização da Produção com Isenção de Contribuição Previdenciária, de acordo com a Lei n° 13.606/2018; 8 - Comercialização da Produção para Entidade inscrita no PAA; 9 - Comercialização da Produção no Mercado Externo.   Caso não preenchido exibir a seguinte mensagem: “Indicativo de Comercialização deve ser informado”. | MFS17263 MFS20930 |
| Valor da Receita Bruta | Text Box | S | S |  | Informar o Valor da Receita Bruta.  Caso não preenchido exibir a seguinte mensagem: “Valor da Receita Bruta deve ser informado”. | MFS17263 |
| Valor da Contribuição Previdenciária | Text Box | N | S |  | Informar o Valor da Contribuição Previdenciária | MFS17263 |
| Valor do GILRAT | Text Box | N | S |  | Informar o Valor do GILRAT | MFS17263 |
| Valor do SENAR | Text Box | N | S |  | Informar o Valor do SENAR | MFS17263 |
| Processos | Button | N | S |  | Ao clicar no botão <Processos> será aberta uma janela onde o usuário poderá informar os valores dos processos relacionados ao Período, Indicativo de Comercialização e Tipo de Ajuste em questão.  Ver regras de funcionamento da janela “Processos” no item 3-Regras dos Campos - Processos”. | MFS27483 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Tipo do Processo | Alfanumérico | S | S |  | Este campo é uma lista com as seguintes opções:  1-Administrativo 2-Judiciário |
| Número do Processo | Alfanumérico | S | S |  | Este campo trabalha com janela de seleção da Tabela de Cadastro de Processos Administrativos / Judiciais (SAFX2058).   Serão disponibilizados para seleção apenas os processos que atendam aos seguintes critérios:  -Grupo = grupo a ser utilizado (ver OBS); - Tipo do Processo = tipo informado em tela; - Validade Inicial = deve ser de um mês/ano <=    ao mês/ano de competência; - Validade Final = deve estar nula, ou ser de um    mês/ano >  mês/ano de competência;  OBS: O Grupo a ser utilizado será obtido a partir da regra básica, considerando o Grupo de maior data de validade, cujo mês/ano seja <= ao mês/ano de competência informado, e para o qual a tabela SAFX2058 esteja associada.  Caso o número do processo seja digitado, ao invés de selecionado na janela de seleção, será validada a sua existência na SAFX2058, considerando as condições descritas acima. Se o processo não existir, será exibida mensagem padrão e a operação não será salva:  “Processo Administrativo/Judicial não               cadastrado ou inválido” |
| Código Suspensão | Alfanumérico | S | S |  | Este campo trabalha com janela de seleção da Tabela de Informações de Suspensão de Exigibilidade de Tributos (SAFX2059).  Serão disponibilizados para seleção apenas os códigos de suspensão da SAFX2059 que sejam “filhos” do processo informado.   Caso o código de suspensão seja digitado, ao invés de selecionado na janela de seleção, será validada a sua existência na SAFX2059, considerando as condições descritas acima. Se o código de suspensão não existir, será exibida mensagem padrão e a operação não será salva:  “Código Suspensão não cadastrado ou inválido” |
| Valor da Contribuição Previdenciária não Retida | Numérico | N | S |  | Nesse campo será informado o valor da contribuição previdenciária não retida (exigibilidade suspensa).  Para salvar a operação, ao menos um dos três valores da tela deve ser informado. Caso isso não aconteça, a operação não será salva e será exibida mensagem de erro. |
| Valor da Contribuição GILRAT não Retida | Numérico | N | S |  | Nesse campo será informado o valor da contribuição GILRAT não retida (exigibilidade suspensa).  Para salvar a operação, ao menos um dos três valores da tela deve ser informado. Caso isso não aconteça, a operação não será salva e será exibida mensagem de erro. |
| Valor da Contribuição SENAR não Retida | Numérico | N | S |  | Nesse campo será informado o valor da contribuição SENAR não retida (exigibilidade suspensa).  Para salvar a operação, ao menos um dos três valores da tela deve ser informado. Caso isso não aconteça, a operação não será salva e será exibida mensagem de erro. |
| Novo | Button |  |  |  | Através desta opção o usuário poderá incluir um novo registro de processo para o Período, Indicativo de Comercialização e Tipo de Ajuste em questão. |
| Exclui | Button |  |  |  | Através desta opção o usuário poderá excluir um processo já cadastrado para o Período, Indicativo de Comercialização e Tipo de Ajuste em questão. |
| < > | Button |  |  |  | Através das setas o usuário poderá visualizar todos os processos existentes para o Período, Indicativo de Comercialização e Tipo de Ajuste em questão. |
| Confirma | Button |  |  |  | Através desta opção o usuário poderá salvar as operações realizadas. |
| Fecha | Button |  |  |  | Fecha a janela dos Processos. |

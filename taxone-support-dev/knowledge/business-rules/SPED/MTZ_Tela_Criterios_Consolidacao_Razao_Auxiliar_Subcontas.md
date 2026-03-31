# MTZ_Tela_Criterios_Consolidacao_Razao_Auxiliar_Subcontas

> Fonte: MTZ_Tela_Criterios_Consolidacao_Razao_Auxiliar_Subcontas.docx






THOMSON REUTERS

Matriz da tela de Definição dos Critérios de Consolidação do
Livro Razão Auxiliar das Subcontas



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
Menu: Parâmetros

Título da tela: Critérios de Consolidação – Razão Auxiliar das Subcontas

Funcionamento da tela: esta tela foi criada para permitir ao usuário definir os critérios consolidação que serão atribuídos na geração do Registro I555: Totais no Livro Razão Auxiliar com Leiaute Parametrizável. Este registro é uma totalização do que é demonstrado no I550 e para a geração do Livro Razão Auxiliar das Subcontas, tivemos a seguinte orientação da RFB em relação a geração deste registro: “O mais importante é que disseram que o conteúdo é absolutamente irrelevante, cabendo ao usuário estabelecer os níveis de totais convenientes. Assim, tanto a chave quanto os campos que vão ser totalizados ficam a critério do usuário”. Através desta parametrização vamos permitir ao usuário informar quais campos serão agrupadores e quais serão totalizadores.

A parametrização será realizada com os campos carregados na TFIX78 – Critérios de Consolidação do Razão Auxiliar das Subcontas. Para cada campo da TFIX, caberá ao usuário indicar o tratamento que será aplicado.

Para cada combinação de Estabelecimento, Cód. Livro Auxiliar e Leiaute ECD o usuário deverá indicar o tratamento do Campo do Livro Razão Auxiliar que foi carregado na TFIX78 e demonstrado na tela.



* Descrição não disponível em tela



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-2926 | Marcos G. de Paula | Definição das regras da tela do Livro Razão Auxiliar das Subcontas. |
| MFS-11310 | Jorge Neto | Alteração no campo Layout ECD. |
| MFS-22528 | Julyana Perrucini | Alteração do conteúdo do campo Layout ECD. |
| MFS-58480 | Alessandra Cristina Navatta | Incluir a regra do campo Estabelecimento, quando o estabelecimento logado no sistema, for um estabelecimento centralizado. |


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
| Estabelecimento: | Dropdown | S | S |  | Este campo sempre deve ser preenchido pelo sistema, mas pode ser alterado pelo usuário, de acordo com as regras abaixo:  Serão demonstrados os estabelecimentos Centralizadores (conforme parametrização realizada no módulo Parâmetros / Menu: Preliminares >> Centralização da Escrituração de Obrigações Federais) e os Descentralizados (os que não foram associados a nenhuma centralização).  Ao logar com um estabelecimento centralizador ou descentralizado, o mesmo deve ser apresentado no campo. Caso o estabelecimento logado for centralizado, no campo, deve ser apresentado o estabelecimento centralizador do estabelecimento logado.  Como o campo é de preenchimento obrigatório, deve ser exibida mensagem de erro caso não esteja preenchido: “Código do Estabelecimento não informado”. | MFS-2926 MFS-58480 |
| Cód. Livro Auxiliar | Pasta de Seleção padrão + Editbox | S | S |  | Deve possibilitar a seleção do Código do Livro Auxiliar que foi cadastrado na Tela “Livros Auxiliares ao Diário” (Módulo: SPED >> ECD – Escrituração Contábil Digital / Menu: Parâmetros), cujo tipo de livro esteja preenchido com a opção “Z – Razão Auxiliar (Livro Contábil Auxiliar conforme leiaute definido nos registros I500 a I555)” E que não tenha sido cadastrado na Tela  “Impressão do Livro Auxiliar” (Módulo: SPED / ECD – Escrituração Contábil Digital, Menu: Parâmetros).   Caso o usuário digite um código que não atenda aos critérios acima indicados, retornar mensagem no campo: “Não existe cadastro na tela de “Livros Auxiliares ao Diário” com Tipo “Z – Razão Auxiliar” para o Código do Livro indicado”.  Como o campo é de preenchimento obrigatório, deve ser exibida mensagem de erro caso não esteja preenchido: “Código do Livro Auxiliar não informado”. | MFS-2926 |
| Leiaute ECD: | Dropdown | S | S | Default: sem conteúdo selecionado | Exibir a opção: - Escrituração Contábil Digital – A partir da Versão 4.00 / 5.00  Como o campo é de preenchimento obrigatório, deve ser exibida mensagem de erro caso não esteja preenchido: “Leiaute ECD não informado”.  Obs: estou criando o campo como dropdown já prevendo futuras mudanças em layout. Inicialmente teremos apenas uma opção de versão, mas podemos criar neste formato para facilitar a manutenção no futuro. | MFS-2926 MFS-11310 MFS-22528 |
| Critérios de Consolidação | Critérios de Consolidação | Critérios de Consolidação | Critérios de Consolidação | Critérios de Consolidação | Critérios de Consolidação | Critérios de Consolidação |
| Campo do Livro Razão Auxiliar | Checkbox | N | S | Formato: <Código do Item> - <Descrição> | Será exibido o conteúdo da TFIX78, considerando a versão do “Leiaute ECD” selecionado e a versão informada na TFIX.  Se a versão do leiaute for “4.00”, considerar registros da TFIX78 cuja versão seja igual a “400”. | MFS-2926 |
| Tratamento a ser aplicado | Pasta de Seleção padrão + Editbox | N | S | Default: desabilitado para edição | O conteúdo deste campo será habilitado somente quando o “Campo do Livro Razão Auxiliar” for selecionado.  Se o “Campo do Livro Razão Auxiliar” selecionado estiver com formato na TFIX78 preenchido com a opção “A”, exibir através da pasta de seleção as opções:  - Agrupador; - Não demonstrar conteúdo;  Se o “Campo do Livro Razão Auxiliar” selecionado estiver com formato na TFIX78 preenchido com a opção “N”, exibir através da pasta de seleção as opções:  - Agrupador; - Não demonstrar conteúdo; - Sumarizar; - Considerar primeiro valor do período; - Considerar último valor do período;  Ao menos um item deve ser definido como “Agrupador”. Se nenhum tiver esta definição, não permitir a gravação e retornar mensagem de erro: “Informe ao menos um item com Tratamento de Agrupamento”. | MFS-2926 |
| Replicar para os estabelecimentos | Dropdown | N | S |  | Tratamento padrão da opção “Replicar para os estabelecimentos”.  Como estamos trabalhando com estabelecimentos centralizadores e descentralizados, na caixa de seleção dos estabelecimentos serão demonstrados os estabelecimentos Centralizadores (conforme parametrização realizada no módulo Parâmetros / Menu: Preliminares >> Centralização da Escrituração de Obrigações Federais) e os Descentralizados (os que não foram associados a nenhuma centralização). | MFS-2926 |

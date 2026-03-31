# MTZ_Tela_Parâmetros_Identificador da Devolução de Venda Reg Cumulativo_NCM

> Fonte: MTZ_Tela_Parâmetros_Identificador da Devolução de Venda Reg Cumulativo_NCM.docx






THOMSON REUTERS

Matriz da tela de Parametrização por NCM



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
Módulo: SPED >> EFD – Escrituração Fiscal Digital das Contribuições
Menu: Parâmetros >> Identificador Devolução de Venda - Reg. Cumulativo (Segmento Cigarro)

Título da tela: Por NCM

Funcionamento da tela: esta tela foi criada para possibilitar ao usuário a parametrização de NCMs que estão submetidos ao regime cumulativo de apuração do PIS e da COFINS. Os NCMs aqui informados serão considerados na geração do arquivo para identificar quais itens das NFs de devolução que deverão ter suas bases de cálculo zeradas e que o valor será demonstrado como ajuste na apuração da contribuição.



* Descrição não disponível em tela



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-1876 | Marcos G. de Paula | Definição das regras da tela de Parametrização por NCM. |
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


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Dropdown | S | S |  | Será preenchido com o código + razão social do estabelecimento que acessou o módulo, conforme informado no manager. Se não for informado nenhum estabelecimento, deve estar habilitado para edição. | MFS-1876 |
| Informar Código/Descrição para Pesquisa | Editbox / Radiobutton | N | S | Default: Radiobutton Código selecionado | Neste campo teremos opções de pesquisa que irão refletir no resultado demonstrado na Relação de NCMs. Será um campo Editbox + Radiobutton com as opções Código e Descrição. | MFS-1876 |
| Pesquisar | Botão | N | S |  | Quando acionado, deve pesquisar o NCM através do código ou descrição, conforme selecionado pelo usuário, e atualizar a Relação de NCMs com o resultado encontrado. | MFS-1876 |
| Relação de NCMs | Checkbox | S | S | Default: Não Selecionado | Neste campo será exibida a relação de NCMs (SAFX2043).  Caso o usuário utilize as opções de pesquisa, o conteúdo deste campo será atualizado para que seja demonstrado o NCM (ou NCMs) reflexo da pesquisa realizada, considerando sempre informação do grupo de acesso.  Caso o usuário tente salvar a informação considerando os NCMs demonstrados, deverá selecionar ao menos um registro da parametrização. Caso não seja selecionado nenhum, retornar a mensagem: “Selecione pelo menos um código de NCM”. | MFS-1876 |
| Selecionar Todos | Botão | N | S |  | Quando acionado este botão, todos os registros da relação de NCMs que estão com status “Não Selecionado” mudarão o status para “Selecionado”. | MFS-1876 |
| Desmarcar Todos | Botão | N | S |  | Quando acionado este botão, todos os registros da relação de NCMs que estão com status “Selecionado” mudarão o status para “Não Selecionado”. | MFS-1876 |
| Replicar para os estabelecimentos | Checkbox | N | S | Default: Não selecionado | Quando selecionado este parâmetro, será habilitada a caixa de seleção de estabelecimentos para que o usuário indique os estabelecimentos para os quais deseja copiar a parametrização.  Neste campo serão exibidos os estabelecimentos pertencentes a mesma empresa que acessou o módulo e grupo que acessou a tela. | MFS-1876 |

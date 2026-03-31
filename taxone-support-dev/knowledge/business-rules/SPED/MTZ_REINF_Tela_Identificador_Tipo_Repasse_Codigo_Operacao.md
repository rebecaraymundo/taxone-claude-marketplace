# MTZ_REINF_Tela_Identificador_Tipo_Repasse_Codigo_Operacao

> Fonte: MTZ_REINF_Tela_Identificador_Tipo_Repasse_Codigo_Operacao.docx






THOMSON REUTERS

Identificador do Tipo de Repasse por Código de Operação
SPED – Reinf



DOCUMENTO DE REQUISITO



Sumário

1.	TELA A SER DESENVOLVIDA	3
1.1.	Diagrama de Casos de Uso	3
1.1.1.	UC001 – Manutenção da Estrutura Padrão	3
1.1.1.1.1.	Fluxo Principal	4
1.1.1.1.2.	Fluxo Alternativo 1 – Localizar registros (Exemplo)	4
2.	Regras dos Campos	5

## TELA A SER DESENVOLVIDA


[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir]

### Diagrama de Casos de Uso





### UC001 – Manutenção da Estrutura Padrão


[Descrever a ação deste caso de uso.

Ex.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão.]


#### Fluxo Principal


[Descrever a ação principal que será realizada na tela especificada.

Ex.: O usuário deseja realizar o cadastro de uma estrutura padrão.



#### Fluxo Alternativo 1 – Localizar registros (Exemplo)




## Regras dos Campos


Localização da tela: Módulo: SPED >> EFD – Reinf
Menu: REINF >> Parâmetros >> Identificador do Tipo de Repasse >> Por Código de Operação

Título da tela: Identificador do Tipo de Repasse por Código de Operação

Obs: Ao abrir a tela de conferência deverá abrir uma subtela para seleção do Grupo.





| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS12777 | Elenilson Coutinho | Inclusão da Tela de Identificador do Tipo de Repasse por Código de Operação |
| MFS13367 | Lara Aline | Inclusão da opção Patrocínio no campo Tipo de Repasse |


| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | [Quem executará o evento. Ex.: Usuário do sistema]. |
| Pré- Condições | [Condições necessárias para execução. Ex.: Estabelecimento cadastrado] |
| Pós-Condições | [Resultado após executar caso de uso. Ex.: Informação armazenada no banco de dados] |


| Ações do Ator | Ações do Sistema |
| --- | --- |
| [Descrever a interação do ator com o sistema.  Ex.: O usuário acessa a tela de estrutura padrão]. | [Descrever a ação esperada do sistema Ex.:O sistema apresenta a tela, conforme as regras definidas no tópico “Regras dos Campos”.] |
| [Ex.:O usuário preenche os campos da Manutenção de Estrutura do Produto. <<Fluxo Alternativo 1>> | [Ex.:O sistema apresenta os campos preenchidos.] |


| Ações do Ator | Ações do Sistema |
| --- | --- |
| O usuário clica no botão “Localizar”. | O sistema apresenta os registros cadastrados, de acordo com os parâmetros informados. |
|  | Fim do fluxo Alternativo |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Grupo Serviço | TextBox | S | N | Default: Desabilitado | Deverá apresentar o grupo conforme apresentado no modal ao abrir a tela. | MFS-12777 |
| Estabelecimento | Texto | S | N | Default: Desabilitado | Deverá apresentar o estabelecimento conforme apresentado no modal ao abrir a tela. | MFS-12777 |
| Tipo de Repasse | Drop Down | S | S |  | Deverá listar as seguintes opções:  [Alteração MFS13367] - Patrocínio - Licenciamento de Marcas e Símbolos - Publicidades - Propaganda - Transmissão de Espetáculo  Caso não preenchido deverá apresentar a seguinte mensagem: “Tipo de Repasse deve ser preenchido” | MFS-12777 MFS-13367 |
| Informar Código/Descrição para Pesquisa por: Código Descrição | Radio Button | N | S | Default Selecionado: Código |  | MFS-12777 |
| Código de Operação | Checkbox | S | S |  | Deverá listar os códigos de Operação conforme SAFX2001.  Caso não preenchido deverá apresentar a seguinte mensagem: “Ao menos um código de Operação deve ser selecionado” | MFS-12777 |
| Selecionar Todos | Button | N | N |  | Se selecionado irá selecionar todos os estabelecimentos listados em tela. | MFS-12777 |
| Desmarcar Todos | Button | N | N |  | Se selecionado irá desmarcar todos os estabelecimentos listados em tela. | MFS-12777 |
| Replicar para os Estabelecimentos | Checkbox | S | S |  | Quando selecionado deverá permitir replicar a parametrização para outros estabelecimentos. | MFS-12777 |
| Selecionar Todos | Button | N | N |  | Se selecionado irá selecionar todos os estabelecimentos listados em tela. | MFS-12777 |
| Desmarcar Todos | Button | N | N |  | Se selecionado irá desmarcar todos os estabelecimentos listados em tela. | MFS-12777 |

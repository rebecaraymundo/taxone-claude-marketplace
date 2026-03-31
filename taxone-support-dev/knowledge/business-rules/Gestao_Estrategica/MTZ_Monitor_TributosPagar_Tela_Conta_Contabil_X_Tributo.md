# MTZ_Monitor_TributosPagar_Tela_Conta_Contábil_X_Tributo

> Fonte: MTZ_Monitor_TributosPagar_Tela_Conta_Contábil_X_Tributo.docx






THOMSON REUTERS

Conta Contábil X Tributo
Inclusão da tela “Conta Contábil X Tributo”



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


Localização da tela: Módulo: Solução Complementar >> Gestão Estratégica
Menu: Parâmetros >> Conta Contábil X Tributo

Título da tela: Conta Contábil X Tributo

No acesso à tela o sistema deve exibir a tela padrão de seleção de Estabelecimento/Grupo/Validade:



Na barra de ferramentas, deve existir o botão de seleção de Grupo:

A pesquisa da conta irá considerar o grupo selecionado no momento da entrada na tela.





| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-5051 | Conta Contábil X Tributo | Inclusão da tela “Conta Contábil X Tributo“ |
|  |  |  |


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
| Grupo Tributo | Dropdown | S | S | Default: Não preenchido | Preencher conforme abaixo:  Federal Estadual  Municipal  Previdenciário  Caso não preenchido, exibir a seguinte mensagem: “Grupo Tributo dever ser informado”. | MFS-5051 |
| Tributo(s) | Checkbox | S | S | Default: Não selecionado | Este campo será apresentado apenas quando selecionado o “Grupo Tributo”   Caso preenchido “Federal” deverão listar os seguintes tributos:  IRPJ IRRF CSLL PIS/PASEP COFINS IPI PIS/PASEP (PRÓPRIO) COFINS (PRÓPRIO)        Caso preenchido “Municipal” deverá listar o seguinte tributo: ISS  Caso preenchido “Previdenciário” deverá listar o seguinte tributo: INSS  Ao menos um registro deve ser selecionado, caso contrário exibir a seguinte mensagem de erro: “Tributo deve ser informado”. | MFS-5051 |
| Grupo Conta | Text | S | N |  | Irá apresentar o grupo da conta conforme definido no acesso a tela. | MFS-5051 |
| Informar Código / Descrição da Conta para Pesquisa: | Text | N | S |  | Preencher com o Código ou Descrição da Conta Contábil.  Caso não preenchido exibir a seguinte mensagem: “Conta deve ser informada”. | MFS-5051 |
| Código | Radio Button | N | S | Default: Selecionado | Caso selecionado, a pesquisa pela conta contábil (SAFX2002 – COD_CONTA) será por código. | MFS-5051 |
| Descrição | Radio Button | N | S |  | Caso selecionado, a pesquisa pela conta contábil (SAFX-2002 - DESCRICAO) será por Descrição. | MFS-5051 |
| Pesquisar | Button | N | N |  | Quando acionado irá realizar a pesquisa da(s) conta(s) conforme parâmetros de seleção. | MFS-5051 |
| Contas | Checkbox | S | S |  | Este campo irá listar todas as contas (SAFX2002) somente analíticas (IND_CONTA = ‘A’).  Ao menos uma conta deverá ser selecionada, caso contrário exibir a seguinte mensagem: “Conta deve ser informada”.  Obs: Será possível a seleção de uma conta por tributo.  Uma vez relacionada, esta não poderá ser listada ou pesquisada para outros grupos e tributos.  Só serão apresentadas contas onde o campo SAFX2002 - IND_SITUACAO = A | MFS-5051 |

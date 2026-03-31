# MTZ_Tela_Subcontas_Correlatas

> Fonte: MTZ_Tela_Subcontas_Correlatas.docx






THOMSON REUTERS

Matriz da tela de Subcontas Correlatas



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

Título da tela: Identificador do Tipo de Serviço

Funcionamento da tela: esta tela foi criada para possibilitar ao usuário que associe para uma determinada conta contábil (SAFX2002) outras contas que são relacionadas a ela, chamadas de contas correlatas. Para cada conta contábil indicada pelo usuário o sistema deve permitir o relacionamento com “N” contas distintas.

Na tabela também existirá o campo de “Código de identificação do grupo de conta-subconta” e a identificação da “Natureza da Subconta Correlata”, porém, a chave da tabela será apenas o código da Subconta Correlata (código da conta contábil da SAFX2002).

No acesso à tela o sistema deve exibir a tela padrão de seleção de Estabelecimento/Grupo/Validade:



Na barra de ferramentas, deve existir o botão de seleção de Grupo:

A pesquisa de contas contábeis da conta irá considerar o grupo selecionado no momento da entrada na tela. Para que haja o relacionamento entre a conta contábil e a subconta correlata o usuário deverá posicionar o cursor sobre a conta e indicar na parte de baixo da tela, na caixa de Subcontas Correlatas, uma ou mais contas que estão relacionadas com a conta selecionada. Para inserção de mais de uma subconta correlata utilizar a funcionalidade de inserção de registros da barra de ferramentas padrão do Mastersaf.



* Descrição não disponível em tela




| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4745 | Marcos G. de Paula | Definição das regras da tela de Subcontas Correlatas. |
| MFS6498 | Jorge Neto | Alteração para permitir associação da mesma conta como subconta correlata |
| CH18547/2016 | Lara Aline | Ajuste no campo Grupo Conta-Subconta para não permitir parametrizar o mesmo grupo para mais de uma conta contábil, conforme solicita regra do PVA versão 3.3.8 |


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
| Conta (Grupo/Cód./Desc.) | Pasta de seleção + caixa de texto | S | N |  | Permitir acesso à lista de seleção das contas contábeis (SAFX2002). Na leitura dos registros o sistema deve demonstrar todas as contas analíticas (aquelas cujo Indicador de Conta (IND_CONTA) da SAFX2002 seja igual a “A”) pertencentes ao grupo indicado. | OS4745 |
| Gr. Conta-Subconta | Texto | S | S |  | Este campo é de parametrização do usuário. Será um campo do tipo alfanumérico e deve permitir no máximo 6 caracteres. Por ser um campo obrigatório, caso não seja informado, retornar mensagem de erro ao tentar gravar a informação: “Gr. Conta-Subconta não informado”.  [ALTERADO CH18547/2016] Não deve ser permitida a parametrização de um mesmo “Grupo Conta-Subconta” para mais de uma “Conta Contábil”. Caso o usuário informe o mesmo código de grupo para mais de uma conta, não permitir a gravação e retornar a mensagem: “Não é permitido utilizar o mesmo Gr. Conta-Subconta para mais de uma Conta Contábil”.  Não deve ser permitida a parametrização de mais de um “Gr. Conta-Subconta” por “Conta (Grupo/Cód./Desc.)”. Caso o usuário informe um código de grupo distinto para a mesma conta, não permitir a gravação e retornar a mensagem: “Não é permitido mais de um Gr. Conta-Subconta por Conta Contábil”. | OS4745 CH18547/2016 |
| Subcontas Correlatas | Subcontas Correlatas | Subcontas Correlatas | Subcontas Correlatas | Subcontas Correlatas | Subcontas Correlatas | Subcontas Correlatas |
| Natureza da Subconta | Pasta de seleção + caixa de texto | S | S |  | Deverá permitir acesso através da pasta de seleção à listagem de códigos informados na TACES90. Por ser um campo obrigatório, caso não seja informado, retornar mensagem de erro ao tentar gravar a informação: “Natureza da Subconta não informada”. | OS4745 |
| Subconta Correlata | Pasta de seleção + caixa de texto | S | S |  | Deverá permitir acesso através da pasta de seleção à listagem de registro do Plano de Contas (SAFX2002), demonstrando apenas as contas analíticas (aquelas cujo Indicador de Conta (IND_CONTA) da SAFX2002 seja igual a “A”), considerando como critério para pesquisa o grupo indicado no acesso à tela. Esta informação não poderá se repetir para a conta contábil indicada na “Conta (Grupo/Cód./Desc.)”. Caso seja repetida a informação, retornar a mensagem: “Código da Subconta Correlata não deve ser igual à Conta pai informada e não pode se repetir por Conta Pai”.  Por ser um campo obrigatório, caso não seja informado, retornar mensagem de erro ao tentar gravar a informação: “Subconta Correlata não informada”.  Este campo deve pertencer à chave da tabela que será criada. | OS4745 MFS6498 |

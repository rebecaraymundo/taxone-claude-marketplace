# MTZ_ECD_Tela_Mapeamento_Plano_Contas_Empresas_Consolidadas

> Fonte: MTZ_ECD_Tela_Mapeamento_Plano_Contas_Empresas_Consolidadas.docx






THOMSON REUTERS

Mapeamento para Planos de Contas das Empresas Consolidadas
Bloco K – Sped Contábil



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Layout da Tela:	5


## Regras dos Campos


Localização da tela: Módulo: SPED >> EFD – Escrituração Contábil Digital
Menu: Manutenção >> Bloco K  >> Mapeamento para Planos de Contas das Empresas Consolidadas

Título da tela: Mapeamento para Planos de Contas das Empresas Consolidadas





























## Layout da Tela:







| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-10358 | Tela Mapeamento para Planos de Contas das Empresas Consolidadas | Criação da Tela “Mapeamento para Planos de Contas das Empresas Consolidadas” |
| MFS-18238 | João Henrique de Araujo | Essa alteração tem como finalidade incluir o campo “Código da Conta Consolidadora” na tela. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento Controlador | Text Box | S | S | Default: Habilitado | Este campo exibe a lista dos estabelecimentos da empresa para seleção do usuário. Quando o estabelecimento for informado no login do sistema, o campo mostrará fixo o estabelecimento do login, e o usuário não poderá alterá-lo.   Demonstrar na frente do código e nome do estabelecimento se o mesmo é centralizado ou descentralizado. | MFS9667 |
| Data Inicial (Período da Consolidação) | Text Box | S | S | Default: Desabilitado | Neste campo será demonstrado o período inicial da consolidação de acordo com o Código/Nome da Empresa Participante selecionado. | MFS9667 |
| Data Final (Período da Consolidação) | Text Box | S | S | Default: Desabilitado | Neste campo será demonstrado o período final da consolidação de acordo com o Código/Nome da Empresa Participante selecionado. | MFS9667 |
| Código/Nome da Empresa Participante | Text Box | S | S | Default: Habilitado | Este campo trabalha com janela de seleção da tabela SAFX240 – Relação das Empresas Consolidadas que correspondam ao Estabelecimento Controlador selecionado. De acordo com o código selecionado na SAFX240 será demostrados também os respectivos campos Data Inicial e Final do Período de Consolidação.  Caso não preenchido exibir a seguinte mensagem: “O Campo Código da Empresa Participante é obrigatório - deve ser preenchido”. | MFS9667 |
| Código da Conta da Empresa Participante | Text Box | S | S | Default: Habilitado | Este campo trabalha com janela de seleção da tabela SAFX2002 – Tabela do Plano de Contas. Filtrando para que sejam demostrados apenas as contas contábeis analítico cujo o indicador: IND_CONTA_CONSOLID for = “S” e o campo 04 - IND_CONTA = “A”, na tabela SAFX2002 – Tabela do Plano de Contas.  Validar se a conta existe com data < ou igual a data inicial da consolidação  Caso não preenchido exibir a seguinte mensagem: “O Código da conta da Empresa Participante não esta cadastrada”. | MFS9667 |
| Código da Conta Consolidadora | Pasta | N | S | Default: Desabilitado | Este campo é utilizado para informar a Conta Analítica consolidadora cadastrada previamente no Plano de Contas SAFX2002.  Tratamentos: Deve exibir apenas às contas analíticas, ou seja, quando o campo 14 - IND_CONTA_CONSOLID for = “S” e o campo 04 - IND_CONTA = “A”, na tabela SAFX2002 – Tabela do Plano de Contas.  Validar se a conta existe com data < ou igual a data inicial da consolidação  Observação: A descrição e a data da conta devem ser exibidas na tela somente para visualização. | MFS18238 |

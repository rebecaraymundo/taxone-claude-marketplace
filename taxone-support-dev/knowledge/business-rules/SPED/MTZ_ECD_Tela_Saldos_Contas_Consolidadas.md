# MTZ_ECD_Tela_Saldos_Contas_Consolidadas

> Fonte: MTZ_ECD_Tela_Saldos_Contas_Consolidadas.docx






THOMSON REUTERS

Saldos das Contas Consolidadas
Bloco K – Sped Contábil



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3


## Regras dos Campos


Localização da tela: Módulo: SPED >> EFD – Escrituração Contábil Digital
Menu: Manutenção >> Bloco K  >> Saldos das Contas Consolidadas

Título da tela: Saldos das Contas Consolidadas














Sugestão de Tela







| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-9667 | Tela Saldos das Contas Consolidadas | Criação da Tela “Saldos das Contas Consolidadas” |
| MFS26488 | Andréa Rocha | Retirar a regra de validação da empresa da contrapartida em relação a empresa detentora. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Aba Saldos Consolidados | Aba Saldos Consolidados | Aba Saldos Consolidados | Aba Saldos Consolidados | Aba Saldos Consolidados | Aba Saldos Consolidados | Aba Saldos Consolidados |
| Estabelecimento Controlador | Text Box | S | S | Default: Habilitado | Este campo exibe a lista dos estabelecimentos da empresa para seleção do usuário. Quando o estabelecimento for informado no login do sistema, o campo mostrará fixo o estabelecimento do login, e o usuário não poderá alterá-lo.   Demonstrar na frente do código e nome do estabelecimento se o mesmo é centralizado ou descentralizado. | MFS9667 |
| Data do Saldo Consolidado | Text Box | S | S | Default: Habilitado | Neste campo o usuário informará à data do saldo consolidado.  Caso não preenchido exibir a seguinte mensagem: “O Campo Data do saldo consolidado é obrigatória - deve ser preenchida”. | MFS9667 |
| Código da Conta Consolidada | Text Box | S | S | Default: Habilitado | Este campo trabalha com janela de seleção da tabela SAFX2002 – Tabela do Plano de Contas. Filtrando para que sejam demostrados apenas as contas contábeis analíticas cujo campo 04 - Indicador de Conta = ‘A’.  Caso não preenchido exibir a seguinte mensagem: “O Código da conta consolidada não esta cadastrada”. | MFS9667 |
| Valor Absoluto Aglutinado | Text Box | S | S | Default: Habilitado | Caso não preenchido exibir a seguinte mensagem: “O Campo Valor absoluto aglutinado é obrigatório - deve ser preenchido”. | MFS9667 |
| Débito/Crédito | Text Box | S | S | Default: Débito |  | MFS9667 |
| Valor Absoluto das Eliminações | Text Box | S | S | Default: Habilitado | Caso não preenchido exibir a seguinte mensagem: “O Campo Valor absoluto das eliminações é obrigatório - deve ser preenchido”. | MFS9667 |
| Débito/Crédito | Text Box | S | S | Default: Débito |  | MFS9667 |
| Valor Absoluto Consolidado | Text Box | S | S | Default: Habilitado | Caso não preenchido exibir a seguinte mensagem: “O Campo Valor absoluto consolidado é obrigatório - deve ser preenchido”. | MFS9667 |
| Débito/Crédito | Text Box | S | S | Default: Débito |  | MFS9667 |
| Aba Parcela do Valor Eliminado | Aba Parcela do Valor Eliminado | Aba Parcela do Valor Eliminado | Aba Parcela do Valor Eliminado | Aba Parcela do Valor Eliminado | Aba Parcela do Valor Eliminado | Aba Parcela do Valor Eliminado |
| Código/Nome da Empresa Detentora do Valor Aglutinado | Text Box | S | S | Default: Habilitado | Este campo trabalha com janela de seleção da tabela SAFX240 – Relação das Empresas Consolidadas demostrando apenas as informações dos campos Código da Empresa Participante e Nome da Empresa Participante sem repetições.   Caso não preenchido exibir a seguinte mensagem: “O Campo Código Empresa Detentora do Valor Aglutinado é obrigatório - deve ser preenchido”. | MFS9667 |
| Parcela do Valor Eliminado Total | Text Box | S | S | Default: Habilitado | Caso não preenchido exibir a seguinte mensagem: “O Campo Parcela do Valor Eliminado Total é obrigatório - deve ser preenchido”. | MFS9667 |
| Débito/Crédito | Text Box | S | S | Default: Débito |  | MFS9667 |
| Código/Nome da Empresa da Contrapartida | Text Box | S | S | Default: Habilitado | Este campo trabalha com janela de seleção da tabela SAFX240 – Relação das Empresas Consolidadas demostrando apenas as informações dos campos Código da Empresa Participante e Nome da Empresa Participante sem repetições.   [MFS26488] – Retirar o tratamento abaixo, já que o validador do ECD só dá um aviso para esta situação:  Tratamento:   O código informado nesse campo não poderá ser igual ao informado no campo Código/Nome da Empresa Detentora do Valor Aglutinado. Caso o código seja igual, retornar mensagem de erro: “O Código da empresa da contrapartida não pode ser igual ao Código da empresa detentora do valor aglutinado informado”.   Caso não preenchido exibir a seguinte mensagem: “O Campo Código da Empresa da Contrapartida é obrigatório - deve ser preenchido”. | MFS9667/ MFS26488 |
| Código da Conta Consolidada da Contrapartida | Text Box | S | S | Default: Habilitado | Este campo trabalha com janela de seleção da tabela SAFX2002 – Tabela do Plano de Contas. Filtrando para que sejam demostrados apenas as contas contábeis analíticas cujo campo 04 - Indicador de Conta = ‘A’.  Caso não preenchido exibir a seguinte mensagem: “O Código da conta consolidada da Contrapartida não esta cadastrada”. | MFS9667 |
| Parcela da Contrapartida do Valor Eliminado | Text Box | S | S | Default: Habilitado | Caso não preenchido exibir a seguinte mensagem: “O Campo Parcela da Contrapartida do Valor Eliminado é obrigatório - deve ser preenchido”. | MFS9667 |
| Débito/Crédito | Text Box | S | S | Default: Débito |  | MFS9667 |

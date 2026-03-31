# MTZ_ECD_Tela_Relacao_Empresas_Consolidadas

> Fonte: MTZ_ECD_Tela_Relacao_Empresas_Consolidadas.docx






THOMSON REUTERS

Relação das Empresas Consolidadas
Bloco K – Sped Contábil

DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3


## Regras dos Campos


Localização da tela: Módulo: SPED >> EFD – Escrituração Contábil Digital
Menu: Manutenção >> Bloco K  >> Relação das Empresas Consolidadas

Título da tela: Relação das Empresas Consolidadas



























Sugestão de Tela




| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-9667 | Tela Relação das Empresas Consolidadas | Criação da Tela “Relação das Empresas Consolidadas” |
| CH5963_2018 (MFS-17214) | João Henrique | Inclusão de tratamento para os campos: % de Consolidação no Final do Período e % de Participação Total. |
| CH6965_2018 (MFS- 17573) | João Henrique | Permitir que o usuário possa cadastrar a empresa consolidada em períodos distintos “2016” e “2017”. |
| MFS17883 | João Henrique | Essa alteração se faz necessária para permitir que os campos 06 PER_PART e 08 PER_CONS recebam valores maior ou igual a 0 e < que 100. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento Controlador | Text Box | S | S | Default: Habilitado | Este campo exibe a lista dos estabelecimentos da empresa para seleção do usuário. Quando o estabelecimento for informado no login do sistema, o campo mostrará fixo o estabelecimento do login, e o usuário não poderá alterá-lo.   Demonstrar na frente do código e nome do estabelecimento se o mesmo é centralizado ou descentralizado. | MFS9667 |
| Data Inicial (Período da Consolidação) | Text Box | S | S | Default: Habilitado | Neste campo o usuário informará a data inicial do período de consolidação.  Caso não preenchido exibir a seguinte mensagem: “O Campo Data Início do período consolidado é obrigatório - deve ser preenchido”.   Observação:  O sistema deverá permitir o cadastro da empresa consolidada em mais de um período, por exemplo: 2016 e 2017. | MFS9667 |
| Data Final (Período da Consolidação) | Text Box | S | S | Default: Habilitado | Neste campo o usuário informará a data final do período de consolidação.  Caso não preenchido exibir a seguinte mensagem: “O Campo Data Final do período consolidado é obrigatório - deve ser preenchido”.   A data informada neste campo deve ser maior ou igual à data informada no campo Data Início da Consolidação. Caso seja menor, retornar mensagem de erro: “A Data Final do período consolidado não pode ser menor que a Data Inicial do período consolidado”.  Observação:  O sistema deverá permitir o cadastro da empresa consolidada em mais de um período, por exemplo: 2016 e 2017. | MFS9667 |
| Código da Empresa Participante | Text Box | S | S | Default: Habilitado | Caso não preenchido exibir a seguinte mensagem: “O Campo Código da Empresa Participante é obrigatório - deve ser preenchido”.  A empresa participante só poderá pertencer a um período de consolidação, ou seja, será necessário verificar se o código cadastrado já não está cadastrado para outro período de consolidação, caso sim exibir a seguinte mensagem: “Já existe um período de consolidação cadastrado para essa empresa participante”. | MFS9667 |
| Nome da Empresa Participante | Text Box | S | S | Default: Habilitado | Caso não preenchido exibir a seguinte mensagem: “O Campo Nome da Empresa Participante é obrigatório - deve ser preenchido”. | MFS9667 |
| CNPJ da Empresa Participante | Text Box | N | S | Default: Habilitado | CNPJ da Empresa Participante.  Quando informado se for um CNPJ inválido, a operação não será salva e será exibida a seguinte mensagem de erro: “Numero de CNPJ informado nao e valido, conforme regras da Secretaria de Fazenda.”. | MFS9667 |
| Evento Ocorrido no Período? | Text Box | S | S | Default: N - Não | Campo para informar se houve algum evento ocorrido no período.  Opções válidas: S – Sim N – Não  Default = N – Não. | MFS9667 |
| % de Participação Total | Text Box | S | S | Default: Habilitado | Caso não preenchido exibir a seguinte mensagem: “O Campo Percentual de Participação Total é obrigatório - deve ser preenchido”.  Tratamento: O percentual informado no campo deverá ser > = que “0” E < = que “100”. Se o usuário informar um valor diferente da regra, apresentar uma mensagem de aviso na tela: “O valor do percentual de Participação Total deverá estar entre 0 e 100%”. | MFS9667 (CH5963_2018) MFS-17214 MFS17883 |
| % de Consolidação no Final do Período | Text Box | S | S | Default: Habilitado | Caso não preenchido exibir a seguinte mensagem: “O Campo Percentual de Consolidação no Final Período é obrigatório - deve ser preenchido”.  Tratamento: O percentual informado no campo deverá ser > = que “0” E < = que “100”. Se o usuário informar um valor diferente da regra, apresentar uma mensagem de aviso na tela: “O valor do percentual de Consolidação no Final do Período deverá estar entre 0 e 100%”. | MFS9667 (CH5963_2018) MFS-17214 MFS17883 |
| Data Inicial da Consolidação | Text Box | S | S | Default: Habilitado | Neste campo o usuário informará a data inicial da consolidação.  A data informada nesse campo deve pertencer ao período informado nos campos Data Inicial e Data Final do Período de Consolidação, caso for uma data fora do período exibir a seguinte mensagem: “A Data Início da Consolidação não pode ser menos que a Data Inicial do período consolidado”.  Caso não preenchido exibir a seguinte mensagem: “O Campo Data Início da Consolidação é obrigatório - deve ser preenchido”. | MFS9667 |
| Data Final da Consolidação | Text Box | S | S | Default: Habilitado | Neste campo o usuário informará a data final da consolidação.  A data informada nesse campo deve pertencer ao período informado nos campos Data Inicial e Data Final do Período de Consolidação, caso for uma data fora do período exibir a seguinte mensagem: “A Data Final da Consolidação não pode ser maior que a Data Final do período consolidado”.  A data informada neste campo deve ser maior ou igual à data informada no campo Data Início da Consolidação. Caso seja menor, retornar mensagem de erro: “A Data Final da Consolidação não pode ser maior que a Data Final do período consolidado”.  Caso não preenchido exibir a seguinte mensagem: “O Campo Data Final da Consolidação é obrigatório - deve ser preenchido”. | MFS9667 |
| País | Text Box | S | S | Default: Habilitado | Serão listados os países existentes na tabela ‘PAIS’ e caso não preenchido exibir a mensagem: “Código do Pais deve ser preenchido”.  Tratamento:  Caso o campo “CNPJ da Empresa Participante” estiver preenchido, esse campo será preenchido automaticamente com o código = “105 - Brasil”, sem possibilidade de alteração. |  |

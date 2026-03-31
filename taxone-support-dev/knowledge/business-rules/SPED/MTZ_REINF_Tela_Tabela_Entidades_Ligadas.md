# MTZ_REINF_Tela_Tabela_Entidades_Ligadas

> Fonte: MTZ_REINF_Tela_Tabela_Entidades_Ligadas.docx






THOMSON REUTERS

Tela Tabela de Entidades Ligadas
SPED - REINF



DOCUMENTO DE REQUISITO


Sumário

1.	Tela	3
2.	Regras dos Campos	4



























## Tela




## Regras dos Campos


Localização da tela: Módulo: SPED >> REINF
Menu: Parâmetros >> Tabela de Entidades Ligadas

Título da tela: Tabela de Entidades Ligadas


Opções da barra de menu:

NOVO – Limpa todos os campos da tela, com exceção do estabelecimento, permitindo a inclusão de um novo registro.

ABRE – Ao clicar nesta opção, serão exibidos para seleção do usuário todos os dados já parametrizados.

EXCLUI – Permite a exclusão dos dados.

CONFIRMA – Salva os dados incluídos ou alterados.

RELATÓRIO – Para emitir o relatório o usuário poderá selecionar um estabelecimento, e serão listados todos os dados parametrizados para o estabelecimento selecionado.

FECHA – Fecha a janela da parametrização.









| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-79881 | Alessandra Cristina Navatta | Criação da tela, para atendimento do evento R-1050, versão 2.1 do REINF |
| MFS-90001 | Alessandra Cristina Navatta | Alteração da versão 2.1 para 2.1.1 |
| MFS-584211 | Alessandra Cristina Navatta | Ajustes referente a nota técnica 04/2023, conforme INFOLEGIS 1740/23 - Z - 089 - EFD REINF_NT 04/2023:  Retirar a validação ‘ser de raiz diferente do CNPJ do contribuinte declarante’ no campo CNPJ da Entidade Ligada |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Dropdown | S | S | Empresa/Centralizador – XXX-XXXXXXXXXXXXXXXXX (Cód. Empresa /Centralizador - cód. - razão social do estabelecimento) Ou Empresa/Descentralizado – XXX-XXXXXXXXXXXXXXXXX (Cód. Empresa/Descentralizado - cód. - razão social do estabelecimento) | Na lista será demonstrado código e a razão social de cada estabelecimento centralizador*, somente da empresa que acessou o módulo.  Empresa/Centralizador – XXX-XXXXXXXXXXXXXXXXX (Cód. Empresa/Centralizador - cód. - razão social do estabelecimento)  Caso algum estabelecimento não tenha sido associado a uma centralização, este será demonstrado na listagem de estabelecimentos precedido da palavra “Descentralizado”:  Empresa/Descentralizado – XXX-XXXXXXXXXXXXXXXXX (Cód. Empresa/Descentralizado + cód. - razão social do estabelecimento)  * Entende-se Estabelecimento Centralizador aquele que foi cadastrado como tal na tela de “Centralização da Escrituração de Obrigações Federais”, no módulo Parâmetro / menu Preliminares. Caso não exista nenhum estabelecimento cadastrado como centralizador nesta tela para a empresa serão demonstrados os estabelecimentos como descentralizados. | MFS-79881 |
| Classificação da Entidade Ligada | Dropdown | S | S | Defaulf: Não preenchido | Lista de Valores válidos:  1 - Fundo de investimento;  2 - Fundo de investimento imobiliário;  3 - Clube de investimento;  4 - Sociedade em conta de participação. | MFS-79881 |
| CNPJ da Entidade Ligada | Texto | S | S |  | Validações:  Deve ser um CNPJ válido.   [EXCLUSÃO MFS-584211] Ser de raiz (oito primeiras posições) diferente do CNPJ do contribuinte declarante. Exibir a mensagem: ‘A raiz do CNPJ não pode ser igual a raiz do CNPJ do declarante.’  O CNPJ não pode ser igual ao CNPJ do declarante., caso igual, exibir a mensagem: ‘O CNPJ da Entidade Ligada não pode ser igual ao do CNPJ do declarante’.  Se campo ‘Classificação da Entidade Ligada’ for igual a 1,2 ou 3 o CNPJ do FCI deve ter o número de ordem 0001. Caso contrário exibir a mensagem: ‘Quando o campo ‘Classificação da Entidade Ligada’ for igual a 1,2 ou 3 o CNPJ do FCI deve ter o número de ordem 0001’  Composição do CNPJ:   CNPJ: 99.202.320/0001-91  Raiz: 99.202.320 Ordem: 0001 Dígito Verificador: 91 | MFS-79881 MFS-584211 |
| Validade Inicial | Data | S | S | DD/MM/AAAA |  | MFS-79881 |
| Validade Final | Data | N | S | DD/MM/AAAA | O campo Validade Final da Tabela de Entidades Ligadas, deve ser igual ou maior que o campo Validade Inicial. | MFS-79881 |
| Confirma | Botão | - | - |  | Ao tentar gravar um registro:  se existir registro na base com Data Validade Final em aberto e a data Validade Inicial menor que a do novo registro, não gravar o registro e exibir a mensagem: “Já existe na base, registro com o campo ‘Validade Final’ em aberto, compreendida neste mesmo período de validade. Favor verificar!” se existir registro na base com Data Validade Final em aberto e a data Validade Final do novo registro também estiver em aberto e a Data Validade Inicial for menor que a do registro gravado, não gravar o registro e exibir a mensagem: “Já existe na base, registro com o campo ‘Validade Final’ em aberto, compreendida neste mesmo período de validade. Favor verificar!” | MFS-79881 |

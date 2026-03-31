# MTZ_Tela_Relatorio_Conferencia_ContasxReferencial

> Fonte: MTZ_Tela_Relatorio_Conferencia_ContasxReferencial.docx






THOMSON REUTERS

ECD – Escrituração Contábil Digital / Validação Plano de Contas x Plano 
Referêncial


DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3


## Documentos de Referência


MTZ_Relatorio_Conferencia_ContasxReferencial.doc

## Regras dos Campos


[ALTERAÇÃO MFS-58039] Esta funcionalidade deve ser disponibilizada inclusive no produto DW.

Localização da tela: Módulo: SPED >> EFD – Escrituração Contábil Digital
SPED à  ECD à Relatório de Conferência das Contas da Empresa x Plano Referencial
Título da tela: 	Relatório -> Conferência Contas x Referencial












Sugestão de Tela:









Especificação:

Quando o usuário clicar no botão executar, com a opção ‘Contas movimentadas que não estão Parametrizadas’ marcada, o sistema deverá:



Recuperar a relação do plano de contas da empresa, conforme critério abaixo:

- Se selecionado a opção tipo de origem, saldo por centro de conta serão recuperadas as contas do plano de contas, a partir dos saldos contábeis da x02, conforme RN01 do arquivo MTZ_Relatorio_Conferencia_ContasxReferencial.doc.
- Se selecinado a opção tipo de origem, saldo por centro de custo serão recuperadas as contas do centro de custo, a partir da x080, conforme RN02.
- Se selecionado a opção todas as contas, serão recuperados todas as contas do plano de contas pertencentes dos grupos válidos no período selecionado, conforme RN03 do arquivo MTZ_Relatorio_Conferencia_ContasxReferencial.doc.

A partir das contas recuperadas deverão ser verificadas todas as contas que estão relacionadas a alguma conta do plano referencial da versão escolhida em tela, conforme RN04 do arquivo MTZ_Relatorio_Conferencia_ContasxReferencial.doc.
Listar em um arquivo de saída no formato excel a lista de contas que não estão relacionadas no plano referencial conforme RN05 do arquivo MTZ_Relatorio_Conferencia_ContasxReferencial.doc.
‘

Quando o usuário clicar no botão executar, com a opção ‘Contas com Naturezas Distintas nas Contas Referencial e Contas da Empresa’ marcada, o sistema deverá: seguir as regras indicadas na RN06 do arquivo MTZ_Relatorio_Conferencia_ContasxReferencial.doc

Quando o usuário clicar no botão executar, com a opção ‘Centro de Custo em mais de uma Conta do Plano Referencial
’ marcada, o sistema deverá: seguir as regras indicadas na RN07 do arquivo MTZ_Relatorio_Conferencia_ContasxReferencial.doc


| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-46980 | ECD – Validação Plano de Contas x Plano Referêncial | Incluído no Tax One a funcionalidade de conferência do plano referêncial x plano de contas da empresa. |
| MFS-58039 | Alessandra Cristina Navatta | Incluir a tela no DW. Ajustar a tela, incluindo mais validações (e alterar o layout da tela, demonstrando as validações que são permitidas na tela) |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Empresa | Combo Box | S | S | Default: Código da empresa informada no login | Este campo exibe a lista de empresas para seleção do usuário.  Demonstrar na frente o código e nome de empresa. Deverão ser demonstradas apenas as empresas que o usuário tem acesso. | MFS46980 |
| Data Inicial | Text Box | S | S | Formato: Dia, Mês e Ano | Neste campo será informado o período inicial o processamento do saldo por centro de custo. | MFS46980 |
| Data Final | Text Box | S | S | Formato: Dia, Mês e Ano | Neste campo será informado o período final o processamento do saldo por centro de custo. | MFS46980 |
| Versão | Combo Box | S | S | Default: Maior versão disponivel | Este campo exibe a lista de versões do plano referencial. | MFS46980 |
| Tipo de Origem | Radio Button | S | S | Default: Saldos por Conta | Deverá estar disponivel os 3 valores:Saldos por conta, Saldos por Centro de Custo e Todas as Contas. | MFS46980 |
| Validações | Ckeck-box | S | S | - | Lista de opções válidas:  - Contas Movimentadas que não estão parametrizadas -Contas com Naturezas Distintas nas Contas Referencial e Contas da Empresa - Centro de Custo em mais de uma Conta do Plano Referencial   Obs. A opção ‘- Centro de Custo em mais de uma Conta do Plano Referencial‘, só será habilitada se as opções ‘Saldos por Centro de Custo’ e ‘Todas as Contas’ no campo ‘Tipo de Origem’  estiver selecionada. | MFS-58039 |
| Estabelecimento | Multi Select | S | S |  | Serão exibidas as listas de estabelecimentos pertencentes a empresa selecionada anteriormente. | MFS46980 |

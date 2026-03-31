# MTZ_REINF_Tela_Relatorio_de_Conferencia_do_Evento_Familia4000

> Fonte: MTZ_REINF_Tela_Relatorio_de_Conferencia_do_Evento_Familia4000.docx






THOMSON REUTERS

Módulo EFD - REINF
Tela Relatório de Conferência dos Eventos - Família 4000

Localização: Menu SPED, Módulo: EFD - REINF, item de menu Relatórios à Conferência dos Eventos à Família 4000



DOCUMENTO DE REQUISITO

Sumário

1.	Objetivo	3
2.	Tela	3
3.	REGRAS DOS CAMPOS	6
4.	Abas Geradas (APENAS NO PRODUTO TAXONE)	12

## Objetivo

Criar uma tela de geração única, para os relatórios da família 4000 do REINF.


## Tela


Produto DW




Produto TAXONE (sem o agrupamento Diretório e no formato de Framework, com a exibição das abas de parâmetros, processos)




## REGRAS DOS CAMPOS


Localização da tela: Menu: SPED, Módulo: EFD - REINF, item de menu Relatórios > Conferência dos Eventos > Família 4000 >
Título da tela: Relatório de Conferência do Evento - Família 4000

## Abas Geradas (APENAS NO PRODUTO TAXONE)



| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-79885 | Alessandra Cristina Navatta | Criação de relatório de conferência do evento R-4010 | 12/09/2022 |
| MFS-578044 | Alessandra Cristina Navatta | Alteração da Tela de geração do Relatório de Conferência dos Eventos – Família 4000.  Reestruturação do Menu | 25/10/2023 |
| MFS-594002 | Alessandra Cristina Navatta | Disponibilizar o evento R-4020 no campo Evento da tela ‘Relatório de Conferência do Evento - Família 4000’ | 12/12/2023 |
| MFS-594004 | Alessandra Cristina Navatta | Disponibilizar o evento R-4080 no campo Evento da tela ‘Relatório de Conferência do Evento - Família 4000’. Inclusão de regra no campo Razão Social (o parâmetro deve ficar desabilitado se selecionado o evento R-4080, no campo ‘Evento’) | 21/12/2023 |
| MFS-594003 | Alessandra Cristina Navatta | Disponibilizar o evento R-4040 no campo Evento da tela ‘Relatório de Conferência do Evento - Família 4000’. Inclusão de regra no campo Razão Social (o parâmetro deve ficar desabilitado se selecionado o evento R-4040, no campo ‘Evento’) | 14/02/2024 |
| MFS626907 | Andréa Rocha | Inclusão do campo Tipo de arquivo , que vai definir como deve ser gerado o relatório. | 20/05/2024 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Evento | Lista | S | S | Código -Descrição | Listar os eventos da família 4000  R-4010 – Pagamentos/Créditos a Beneficiário Pessoa Física  R-4020 – Pagamentos/Créditos a Beneficiário Pessoa Jurídica  R-4040 – Pagamentos/Créditos a Beneficiários não Identificados   R-4080 – Retenção no Recebimento | MFS-578044  MFS-594002  MFS-594004 MFS-594003 |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Informar o mês/ano que o sistema deverá considerar para seleção das informações para a criação do relatório. | MFS-79885 |
| Versão | Lista | S | S | Default: Versão atual | Este campo exibe as versões de layout do Reinf. A partir da versão 2.1.2 | MFS-79885 |
| Tipo de Ambiente | Checkbox | S | S | Default: Produção | Permitir que o usuário informe qual o tipo de ambiente entre as opções:  - Produção - Produção Restrita | MFS-79885 |
| Tipo do Relatório | Checkbox | S | S | Default: Sintético | Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:  - Sintético - Analítico | MFS-79885 |
| Tipo do Arquivo | Listbox | S | S | Default: Arquivo PDF | Esse campo só deve ser apresentado no DW.  Permitir que o usuário informe qual o tipo de arquivo será gerado entre as opções:  - Arquivo PDF - Excel (XLSX) | MFS-626907 |
| Filtro de Pesquisa | Filtro de Pesquisa | Filtro de Pesquisa | Filtro de Pesquisa | Filtro de Pesquisa | Filtro de Pesquisa | Filtro de Pesquisa |
| CPF/CNPJ | Texto | N | S |  | Permite pesquisar pelo CPF/CNPJ. Só serão aceitos números.  Atenção: A pesquisa só recuperará os registros, se for encontrado evento com o mesmo CPF/CNPJ que foi indicado neste campo. | MFS-578044 |
| Razão Social | Texto | N | S |  | Permite pesquisar pela Razão Social. Serão aceitos números e texto  Atenção: A pesquisa só recuperará os registros, se for encontrado evento com a mesma Razão Social que foi indicada neste campo.  [ALTERAÇÃO MFS-594004 e MFS-504003] Este campo deve ficar desabilitado se for selecionado o evento R-4080 ou R-4040, no campo ‘Evento’ | MFS-578044 MFS-594004 |
| Tipo Geração | Lista | S | S | Arquivo PDF | Este campo só deve ser apresentado no produto TAXONE. Permite escolher a opção de geração. Lista de valores válidos: Arquivo PDF  Excel (XLSX) | MFS-578044 |
| Diretório (Este agrupamento, só deve ser apresentado no produto DW, ou seja, não será apresentado no TAXONE.) | Diretório (Este agrupamento, só deve ser apresentado no produto DW, ou seja, não será apresentado no TAXONE.) | Diretório (Este agrupamento, só deve ser apresentado no produto DW, ou seja, não será apresentado no TAXONE.) | Diretório (Este agrupamento, só deve ser apresentado no produto DW, ou seja, não será apresentado no TAXONE.) | Diretório (Este agrupamento, só deve ser apresentado no produto DW, ou seja, não será apresentado no TAXONE.) | Diretório (Este agrupamento, só deve ser apresentado no produto DW, ou seja, não será apresentado no TAXONE.) | Diretório (Este agrupamento, só deve ser apresentado no produto DW, ou seja, não será apresentado no TAXONE.) |
| Local | Pasta | N | S |  | Este campo só deve ser apresentado no produto DW. Permite selecionar um diretório local. | MFS-578044 |
| Utilizar Diretório do Servidor | Check-box |  |  | Default: desmarcado | Este campo só deve ser apresentado no produto DW. Se marcado, o campo Local, ficará desabilitado e o campo Servidor será habilitado e de preenchimento obrigatório. | MFS-578044 |
| Servidor | Lista | N | S |  | Este campo só deve ser apresentado no produto DW. O campo só será habilitado, se o Check-box ‘Utilizar Diretório do Servidor’, estiver marcado.  Serão apresentados os diretórios que foram criados no servidor. | MFS-578044 |
| Considerar R-4010/R-4020 Arquivos Externos (JCP) | CheckBox |  |  | Default: não selecionado | Só ficará habilitado se os eventos selecionados na tela de geração do relatório for R-4010 e/ou R-4020.  Quando marcado, serão demonstrados os eventos R-4010 e/ou R-4020 de origem externa (JCP), além dos de origem SAFX53. | MFS-578044 |
| Multiempresas | CheckBox |  |  | Default: não selecionado | Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, os estabelecimentos de todas as empresas que o usuário tem acesso e que geraram o evento. Se o parâmetro estiver desmarcado, apenas os estabelecimentos da empresa logada que geraram o evento serão demonstrados. | MFS-79885 |
| Estabelecimentos | CheckBox | S | S | XXX / XXXXX-XXXXXXXXXXXXXXXXX  (cód. empresa + cód. e razão social do estabelecimento centralizador) ou  XXX / XXXXX-XXXXXXXXXXXXXXXXX  (cód. empresa + cód. e razão social do estabelecimento descentralizado)    Default: não selecionado | - Caso o parâmetro “Multiempresas” estiver desmarcado: Na lista será demonstrado os estabelecimentos que fizeram a geração do evento apenas da empresa que acessou o módulo.      - Caso o parâmetro “Geração Multiempresa” estiver marcado: Na lista será demonstrado o estabelecimento de todas as empresas que geraram o evento e que o usuário tem acesso:          O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”  Como facilitador, poderá ser utilizada a opção “Marcar todos”. Por default, a opção será desmarcada. | MFS-79885 MFS-542897 |
| Geração de Dados (no produto DW)  Confirma (no produto TAXONE) | Botão |  |  |  | Campos Obrigatórios:  Ao selecionar, se não for informado o evento, exibir a mensagem: “Informe o evento”.  Ao selecionar, se não for informado o período, exibir a mensagem: “Informe o período”.   Ao selecionar, se o check-box ‘Utilizar Diretório do Servidor’, estiver desmarcado e não for informado o Diretório Local, exibir a mensagem: “Diretório Local deve ser preenchido”.  Ao selecionar, se o check-box ‘Utilizar Diretório do Servidor’, estiver marcado, e se não for informado o Diretório Servidor, exibir a mensagem: “Diretório Servidor deve ser preenchido”.   Ao selecionar, se não for informado o Estabelecimento, exibir a mensagem: “Favor selecionar ao menos um estabelecimento.”  O relatório será gravado no local indicado na tela (conforme os campos Diretório Local e/ou Diretório Servidor). | MFS-578044 |


| Parâmetros | Esta aba apresenta a tela de geração do relatório (apenas para o produto TAXONE). Conforme mockup e regras definidas nos itens 1. Telas (Produto TAXONE) e 2. Regras dos Campos. | MFS-578044 |
| --- | --- | --- |
| Processos | Esta aba será gerada sempre que for criado um processo (apenas para o produto TAXONE). Deve conter o número do processo, os parâmetros, a situação do processo, as datas Início Execução e Fim Execução, além da informação do Usuário que fez a execução do processo, conforme print abaixo: | MFS-578044 |
| Logs | Esta aba deve demonstrar os logs do processo (apenas para o produto TAXONE). | MFS-578044 |

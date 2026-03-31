# MTZ_REINF_Relatorio_Demonstrativo_Evento_R-2055

> Fonte: MTZ_REINF_Relatorio_Demonstrativo_Evento_R-2055.docx






THOMSON REUTERS

Módulo EFD - REINF
Demonstrativo Evento R-2055
Localização: Menu SPED, Módulo: EFD - REINF, item de menu Relatórios Demonstrativo Evento R-2055


DOCUMENTO DE REQUISITO

Sumário

1.	REGRAS DOS CAMPOS	3
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	6
2.1.	Layout do Relatório	14

## REGRAS DOS CAMPOS


Localização da tela: Menu: SPED, Módulo: EFD - REINF, item de menu Relatórios >
Título da tela: Demonstrativo Evento R-2055




























## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:

Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:

Para geração deste relatório, serão consideradas as informações da seguinte origem:

Evento R-2055 (SAFX07, SAFX63, Cadastro do Estabelecimento e tela “Devoluções de Aquisição de Produtor Rural”).
- Tabela compõem os valores das aquisições (por produtor rural) R-2055 (REINF_PGER_R2055_DETAQUIS);
- Criar uma tabela para armazenar as notas que totalizaram os valores das aquisições, no momento da geração do evento R-2055 (essas informações não impactará a geração do evento R-2055. Elas serão utilizadas para demonstrar ao cliente as notas que foram consideradas para compor o valor total das aquisições, apenas neste relatório).

Regra de seleção:

A geração do relatório será de acordo com os critérios de filtro informados na tela de geração.

-Empresa = empresa do login
-Período = período informado em tela
- Versão = versão informada em tela
- Tipo de Ambiente = Tipo de Ambiente informado em tela
-Estabelecimento = estabelecimento informado em tela


Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura (apenas o header), porém será exibida a mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no log.


Regra de processamento:

O arquivo gerado será em formato csv.
Será gerado um arquivo por empresa.
Serão recuperadas as informações do evento R-2055 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado, acrescidas das notas dos produtores rurais. Relatório demonstrará as informações por Estabelecimento, Produtor Rural, Tipo de Aquisição e Processos. Será recuperado sempre a última ocorrência do evento R-2055 por tipo de número de inscrição do contribuinte.


Ordenação:
Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

- Empresa
- Estabelecimento
- Produtor Rural
Data Emissão ou Fiscal (se origem for SAFX07). Caso a origem seja SAFX63, considerar a Data do Movimento
Número da nota
- Tipo de Aquisição

Nomenclatura do Arquivo

Empresa_Periodo_Versão.CSV

Segue regras do preenchimento dos dados no relatório:


Preenchimento dos Dados do Relatório













| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-74311 | Alessandra Cristina Navatta | Criação de um relatório de demonstrativo do evento R-2055. Relatórios  “Demonstrativo Evento R-2055”. | 01/11/2021 |
|  |  |  |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Local para digitação do período de referência para a geração do relatório (formato de MM/AAAA).  Este campo servirá para parametrizar o período de apuração que o sistema deverá considerar para a seleção das informações do evento R-2055. Na geração do relatório, serão exibidas as notas que foram consideradas para compor o valor do evento em questão. | MFS-74311 |
| Versão | Combo Box | S | S | Default: Versão atual | Este campo exibe as versões de layout do Reinf. A partir da versão 1.5.1 | MFS-74311 |
| Tipo de Ambiente | Radio Button | S | S | Default: Produção Restrita | Permitir que o usuário informe qual o tipo de ambiente entre as opções:  - Produção Restrita - Produção | MFS-74311 |
| Geração Multiempresa | CheckBox | S | S | Default: não selecionado | Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, todas as empresas, contendo o código da empresa, código e a razão social de cada estabelecimento. | MFS-74311 |
| Geração por Estabelecimento | Checkbox | N | S | Default: não selecionado | Quando selecionado pelo usuário, a geração por Estabelecimento.  Este campo interfere na montagem da lista dos estabelecimentos para seleção do usuário, conforme especificado no campo abaixo “Relação de Estabelecimentos”. Na listagem de estabelecimentos devem ser demostrados os estabelecimentos vinculados ao centralizador parametrizado em Dados Iniciais | MFS-74311 |
| Selecionar | Pasta de Seleção | N | S |  | Pasta padrão que permite seleção de um estabelecimento específico. | MFS-74311 |
| Marcar Todos | Checkbox | N | S | Default: não selecionado | Quando selecionado, deve mudar o status dos estabelecimentos para “selecionado”. | MFS-74311 |
| Empresa/Estabelecimento | Checkbox | S | S | Default: não selecionado | Nesse campo deverá apresentar todos os estabelecimentos da empresa do login que possuam o cadastro dos Dados Iniciais preenchido e devido à inclusão do campo Geração Multiempresa, seguir a seguinte regra:  Se parâmetro “Geração Multiempresa” estiver marcado  Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão demonstradas todas as empresas, sendo que, o código do estabelecimento deve ser precedido pela palavra “Centralizador”:  XXX / Centralizador - XXX-XXXXXXXXXXXXXXXXX (cód. empresa + Centralizador + cód. e razão social do estabelecimento)  Se parâmetro “Geração Multiempresa” estiver desmarcado  Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento centralizador*, somente da empresa que acessou o módulo.  Caso algum estabelecimento não tenha sido associado a uma centralização, este será demonstrado na listagem de estabelecimentos precedido da palavra “Descentralizado”:  XXX / Descentralizado - XXX-XXXXXXXXXXXXXXXXX (cód. empresa + Descentralizado + cód. e razão social do estabelecimento)   Se parâmetro “Geração por Estabelecimento” estiver marcado  Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento vinculado ao centralizador.  Quando marcado, na listagem de estabelecimentos devem ser demostrados os estabelecimentos vinculados ao centralizador parametrizado em Dados Iniciais e o sistema deverá permitir a geração por estabelecimento.  XXX / XXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento)   Obs: No caso da geração multiempresa, as regras da geração do arquivo não se modificam. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do arquivo existirão estabelecimentos de empresas distintas.  * Entende-se Estabelecimento Centralizador aquele que foi aquele que foi cadastrado como tal na tela de “Centralização da Escrituração de Obrigações Federais”, no módulo Parâmetro / menu Preliminares. Caso não exista nenhum estabelecimento cadastrado como centralizador nesta tela para a empresa (ou empresas, no caso de geração multiempresa), serão demonstrados os estabelecimentos como descentralizados.  Ao menos uma Empresa/Estabelecimento deverá ser selecionada, caso contrário exibir a seguinte mensagem: Ao menos uma Empresa/Estabelecimento deve ser selecionada. | MFS-74311 |
| Estabelecimentos | CheckBox | S | S | Default: não selecionado | Este campo exibe todos os estabelecimentos da empresa que acessou o módulo do EFD-Reinf.   A partir do parâmetro “Geração Multiempresa”, a lista passou a funcionar da seguinte forma:  - Caso o parâmetro “Geração Multiempresa” estiver desmarcado: Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo. XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento).       - Caso o parâmetro “Geração Multiempresa” estiver marcado: Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão mostradas todas as empresas: XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento)         Obs: No caso da geração multiempresa, as regras da geração do relatório não se modificam. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do relatório existirão estabelecimentos de empresas distintas.  O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”  Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS-74311 |


| Empresa | Código da empresa |
| --- | --- |
| Estabelecimento | Código de Estabelecimento |
| Tipo Arquivo | Tipo de Arquivo gerado no evento R-2055 |
| Nº Recibo | N º Recibo gerado no evento R-2055 |
| Tipo do Amb. | Tipo de Ambiente gerado no evento R-2055 |
| Processo de Emissão | Processo de Emissão gerado no evento R-2055 |
| Versão do Processo de Emissão | Versão do Processo de Emissão gerado no evento R-2055 |
| Indicativo de Retificação do Evento S-1250 | Indicativo de Retificação do Evento S-1250 gerado no evento R-2055 |
| Tipo de Inscrição Estabelecimento | Tipo de Inscrição do Estabelecimento gerado no evento R-2055 |
| Número Inscrição Estabelecimento | Número de Inscrição do Estabelecimento gerado no evento R-2055 |
| Tipo de Inscrição Produtor Rural | Tipo de Inscrição do Produtor Rural gerado no evento R-2055 |
| Número de Inscrição Produtor Rural | Número de Inscrição do Produtor Rural gerado no evento R-2055 |
| Forma de Tributação da Contribuição Previdenciária (Produtor Rural) | Forma de Tributação da Contribuição Previdenciária (Produtor Rural) gerado no evento R-2055 |
| Indicador de Aquisição | Tipo de Aquisição gerado no evento R-2055 |
| Data Emissão da Nota | Data de emissão da nota gerada no evento R-2055 (só apresentar a informação neste campo, se a origem for SAFX07) |
| Data Fiscal da Nota | Data fiscal da nota gerada no evento R-2055 (se a origem for SAFX07, preencher com a informação da data fiscal, se a origem for SAFX63, apresentar a informação da data do movimento) |
| Número da Nota | Número da Nota gerado no evento R-2055 |
| Série | Informar a série da nota que foi considerada para compor o evento R-2055 |
| SubSérie | Informar a subsérie da nota que foi considerada para compor o evento R-2055 |
| Movimento Entrada/Saída | Informar o movimento da nota que foi considerada para compor o evento R-2055 |
| Normal ou Devolução | Informar se a nota é Normal ou de Devolução |
| Valor da Receita Bruta | Valor da Receita Bruta (da nota) gerado para compor o valor da receita total gerado no evento R-2055 |
| Valor da Contribuição Previdenciária | Valor da Contribuição Previdenciária (da nota) gerado para compor o valor total gerado no evento R-2055 |
| Valor da Contribuição Previdenciária GILRAT | Valor da Contribuição Previdenciária GILRAT (da nota) gerado para compor o valor total gerado no evento R-2055 |
| Valor da Contribuição Previdenciária SENAR | Valor da Contribuição Previdenciária SENAR (da nota) gerado para compor o valor total gerado no evento R-2055 |
| Número Processo | Número do Processo gerado no evento R-2055 |
| Código Suspensão | Código Suspensão gerado no evento R-2055 |
| Valor da Contribuição Previdenciária Não Retida | Valor da Contribuição Previdenciária Não Retida (do processo judicial) gerado para compor o valor total gerado no evento R-2055 |
| Valor da Contribuição Previdenciária GILRAT Não Retida | Valor da Contribuição Previdenciária GILRAT Não Retida (do processo judicial) gerado para compor o valor total gerado no evento R-2055 |
| Valor da Contribuição Previdenciária SENAR Não Retida | Valor da Contribuição Previdenciária SENAR Não Retida (do processo juducial) gerado para compor o valor total gerado no evento R-2055 |

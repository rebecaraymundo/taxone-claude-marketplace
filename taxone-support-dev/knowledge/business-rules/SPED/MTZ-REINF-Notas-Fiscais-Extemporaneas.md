# MTZ-REINF-Notas-Fiscais-Extemporaneas

> Fonte: MTZ-REINF-Notas-Fiscais-Extemporaneas.docx






THOMSON REUTERS

Módulo REINF

Relatório das NF’s Extemporâneas não Demonstradas no R-2010



Localização: Menu SPED, módulo EFD – Reinf, menu Relatórios à NF’s Extemporâneas não Demonstradas no R-2010



DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
3.	Regras de Funcionamento dos Campos	3
4.	Regras da Recuperação dos Dados	6
5.	Layout e Preenchimento dos Campos no Relatório	9




















## Regras Gerais


Relatório criado na MFS17629, com objetivo de possibilitar a consulta das notas fiscais extemporâneas que não foram levadas para o REINF, evento R-2010.

## Layout da Tela





## Regras de Funcionamento dos Campos






## Regras da Recuperação dos Dados


Origem dos dados: Documentos Fiscais (SAFX07 / SAFX08 / SAFX09);
Tabelas auxiliares geradas no menu “Geração dos Movimentos”;

Será gerado um relatório para cada um dos estabelecimentos selecionados no campo “Estabelecimentos”.

Quando se tratar de um estabelecimento centralizador, será gerado um relatório para cada um dos estabelecimentos envolvidos na centralização. Ou seja, o relatório sempre demonstrará as notas separadamente para cada estabelecimento. Para facilitar a consulta, os estabelecimentos aparecerão ordenados pelo código.

Para cada estabelecimento a ser gerado, a recuperação dos documentos fiscais será feita da seguinte forma:

Obs.: O filtro para a recuperação das notas é semelhante ao da geração prévia do evento R-2010, exceto no tratamento da Data Fiscal. E além disso, o relatório também tem outras condições a serem atendidas, como por exemplo, o filtro por Prestador do Serviço, e o fato do relatório trazer apenas as notas que não constam no evento R-2010 do REINF.

COD_EMPRESA = código da empresa do login;

COD_ESTAB = código do estabelecimento em questão

MOVTO_E_S <> “9” - somente notas fiscais de entrada;

SITUACAO <> “S” - Apenas as notas não canceladas;

COD_CLASS_DOC_FIS = todas (Mercadoria, Serviço ou Mista);      (Obs: p/os itens de mercadoria, ver condição abaixo)

Os itens de mercadoria (SAFX08), sejam de notas de mercadoria, ou notas mistas (COD_CLASS_DOC_FIS = 1 ou 3), serão considerados apenas se o Modelo da nota = “07” ou “67” (transportes);

[MFS20473]
Se informado no campo Indicação de Período a opção ‘Competência’:
A Data de Emissão da nota deve ser do período informado em tela no campo ‘Período de Competência’ E a Data Fiscal (Data Entrada/Saída) da nota deve ser de período posterior ao período de competência informado em tela;

Se informado no campo Indicação de Período a opção ‘Data Fiscal’:
A Data Fiscal (Data Entrada/Saída) da nota deve ser do período informado em tela no campo ‘Período de Data Fiscal’ E a Data de Emissão da nota deve ser de período anterior ao Período de Data Fiscal informado em tela;

Apenas notas com itens (na SAFX08 e/ou SFAX09);

Quando o CNPJ do prestador do serviço for informado em tela, serão consideradas apenas as notas fiscais cuja pessoa fis/jur tenha o CNPJ = CNPJ informado;

Se item de mercadoria (SAFX08), o produto deve constar na parametrização dos identificadores de tipo de serviço (menu “Parâmetros à Retenções Previdenciárias à Identificador do Tipo de Serviço à Por Código de Produto”);

Se item de serviço (SAFX09), o serviço deve constar na parametrização dos identificadores de tipo de serviço (menu “Parâmetros à Retenções Previdenciárias à Identificador do Tipo de Serviço à Por Código de Serviço”);

[MFS19991]
Se o parâmetro “Desconsiderar NFs sem Valor de Retenção informado” estiver selecionado nos Dados Iniciais, serão recuperadas apenas as notas fiscais que tenham o Valor Base INSS (VLR_BASE_INSS da SAFX08/SAFX09) e Valor de INSS Retido (VLR_INSS_RETIDO da SAFX08/SAFX09) informado.

A nota fiscal não deve constar no evento R-2010 (não deve constar na tabela da geração prévia dos dados do evento R-2010);





Consolidação dos Itens da Nota:

Para cada nota fiscal, será feita a consolidação dos seus itens por Tipo de Serviço. Trata-se do tipo de serviço para o qual os itens (produto ou serviço) são parametrizados.

Convém lembrar que pelas regras definidas, serão considerados apenas os itens (seja da SAFX08 ou SAFX09) cujo produto/serviço esteja associado a um Tipo de Serviço da parametrização do módulo REINF (menu “Parâmetros à Retenções Previdenciárias à Identificador do Tipo de Serviço”).

Para cada Tipo de Serviço, serão totalizados os seguintes valores dos itens para apresentação no relatório:



Critérios de ordenação dos dados para apresentação no relatório:

Para o relatório de cada estabelecimento, as notas recuperadas serão ordenadas por:

- Código da Pessoa Fis/Jur (Indicador e Código da pessoa fis/jur da nota fiscal);
- Data de emissão;
- Número do Documento Fiscal;

No relatório as notas aparecerão agrupadas por Indicador e Código da Pessoa Fis/Jur.

OBS: Observar que mesmo quando o usuário solicitar o relatório para um único prestador (informando o CNPJ na tela), poderá existir mais de um registro na SAFX04 do mesmo CNPJ.  Por isso. o relatório mostrará as notas separadas por Indicador e Código da pessoa fis/jur, com objetivo de facilitar a conferência do usuário.


## Layout e Preenchimento dos Campos no Relatório


Layout: Vide planilha “Layout Relatório NFs Extemporâneas”.


Preenchimento dos campos do relatório:


Linhas do cabeçalho:




Linhas de detalhe do prestador (“Prestador do Serviço”):





Linhas de detalhe das notas fiscais:

Conforme a regra de consolidação dos itens da nota (descrita no item “4-Regras da Recuperação dos Dados”), uma nota poderá ocupar uma única linha ou várias linhas, dependendo da quantidade de Tipos de Serviço para os quais os seus itens estiverem parametrizados.

Para cada Tipo de Serviço, será impressa uma linha com a totalização dos valores dos itens associados a este Tipo de Serviço.

No caso das notas que terão mais de um Tipo de Serviço, e consequentemente, mais de uma linha, as informações das colunas abaixo serão preenchidas apenas na primeira linha. As próximas linhas impressas, referentes à mesma nota fiscal, ficarão com estas colunas em branco. Este procedimento ajuda a identificar que se trata da mesma nota.

- Data de Emissão
- Número do Documento
- Série
- Data Fiscal



= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS17629 | Vania Mattos | Criação do relatório das notas fiscais extemporâneas não demonstradas no R-2010 | 18/04/2018 |
| MFS19991 | Lara Aline | Inclusão de verificação do parâmetro ‘Desconsiderar NFs sem Valor de Retenção informado’ | 01/08/2018 |
| MFS20473 | Lara Aline | Inclusão de possibilidade de filtrar o período de emissão do relatório | 11/10/2018 |
|  |  |  |  |


| Campo | Tipo | Obrig | Ed | Formato / Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Indicação de Período | Checkbox | S | S | Default: Competência | Este parâmetro define qual a período será usado na emissão do relatório.  Deverão ser listadas as seguintes opções:   1 – Competência 2 – Data Fiscal |
| Período de  Competência | Data (mês e ano) | N | S | (MM/AAAA) | [MFS20473] Esse campo será habilitado apenas se no campo Indicação de Período for selecionado a opção ‘1 – Competência.  Mês e ano de competência para a emissão do relatório.  Deve ser um mês válido.  Caso não preenchido exibir a seguinte mensagem:   O campo Período de Competência deve ser informado. |
| Período de  Data Fiscal | Data (dia, mês e ano) | N | S | DD/MM/AAAA à DD/MM/AAAA | Esse campo será habilitado apenas se no campo Indicação de Período for selecionado a opção ‘2 – Data Fiscal’.  A informação será formada de 2 campos para informar o período DE x ATÉ.  XX/XX/XXXX a XX/XX/XXXX  Caso o usuário preencher somente a data inicial a data final será obrigatória e caso não preenchida será apresentada a mensagem:  Data Final deve ser preenchida.  Caso a Data Final preenchida for menor que a Data Inicial será apresentada a mensagem abaixo:  Data Inicial não deve ser maior que a Data Final.  Caso o usuário informar um período ‘de x até’ maior que 1 mês será apresentada a mensagem:  O período informado deve ser no máximo um (1) mês.  Caso não preenchido nenhuma data exibir a seguinte mensagem:   O campo Período de Data Fiscal deve ser informado. |
| Período de  Competência | Data (mês e ano) | S | S | (MM/AAAA) | Mês e ano de competência para a emissão do relatório.  Deve ser um mês válido. |
| Prestador do Serviço – Todos | Alfanumérico | N | S | Default: Opção “Todos” marcada | Na abertura da tela a opção “Todos” aparecerá sempre marcada, e o campo “CNPJ” fica desabilitado;  Caso o usuário desmarque a opção “Todos”, o campo “CNPJ” será habilitado, e o usuário poderá informar o CNPJ do prestador. |
| Prestador do Serviço – CNPJ | Alfanumérico | N | S |  | Na abertura da tela este campo aparecerá sempre desabilitado;  Será habilitado apenas quando o usuário desmarcar a opção “Todos”.  Quando preenchido, deve ser um CNPJ válido, caso contrário, será exibida uma mensagem (ex: “CNPJ inválido”).  Sempre que a opção “Todos” estiver desmarcada, será obrigatório informar o CNPJ do prestador antes de solicitar a emissão do relatório. Caso contrário, será exibida uma mensagem (ex: “Informar o CNPJ do Prestador do Serviço”).  Obs: O prestador também poderia ser informado através do Grupo/Ind/Cód. da SAFX04, e neste caso a tela só mostraria os estabelecimentos associados ao Grupo informado. No entanto, isso poderia ser complicado, pois a lista dos estabelecimentos é variável, de acordo com o parâmetro “Geração por Estabelecimento”. Quando o estabelecimento demonstrado na lista fosse um Centralizador associado ao Grupo, ele poderia ter centralizados trabalhando com outro Grupo, e o relatório teria que tratar estes centralizados de outros Grupos para não serem considerados no relatório. Como isso ficaria confuso para os usuários, a opção foi trabalhar com o CNPJ. |
| Geração por Estabelecimento | Alfanumérico | N | S | Default: Desmarcado | Este checkbox indica se a emissão do relatório será feita por estabelecimento centralizador (padrão), ou estabelecimento a estabelecimento.  O conteúdo deste campo interfere na forma de exibição dos estabelecimentos para seleção do usuário, conforme explicado no campo a seguir. |
| Empresa / Estabelecimento | Alfanumérico | S | S |  | Neste campo será exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário.  A relação de estabelecimentos a ser demonstrada depende de dois fatores: do parâmetro “Geração por Estabelecimento”, e da parametrização “Informações do Contribuinte”, da seguinte forma:  Se “Geração por Estabelecimento” desmarcado:  Neste caso serão exibidos:  - Estabelecimentos centralizadores que constem na        parametrização “Informações do Contribuinte”;  - Estabelecimentos descentralizados que constem na parametrização “Informações do Contribuinte”;  Se “Geração por Estabelecimento” marcado:  Neste caso serão exibidos:  - Estabelecimentos centralizados, de todos os centralizadores que constem na parametrização “Informações do Contribuinte”;  - Estabelecimentos descentralizados que constem na parametrização “Informações do Contribuinte”;     Obs.: Um estabelecimento “descentralizado” é aquele que não consta em nenhuma parametrização, nem como centralizador, nem como centralizado.  As informações dos estabelecimentos serão editadas da seguinte forma:  Se for um estabelecimento centralizador:  XXX / Centralizador: XXX-XXXXXXXXXXXXXXXXX  (código da empresa + “/” +  “Centralizador:” +  código do estabelecimento + “-“ + razão social do estabelecimento)  Se for um estabelecimento centralizado:  XXX / Centralizador: XXX / Centralizado: XXX - XXXXXXXXXXX   (código da empresa + “/” +  “Centralizador:” +  código do estabelecimento centralizador + “/” + “Centralizado:” + código do estabelecimento centralizado + “-“ + razão social do estabelecimento centralizado)  Se for um estabelecimento descentralizado:  XXX / Descentralizado: XXX-XXXXXXXXXXXXXXXXX  (código da empresa + “/” +  “Descentralizado:” + código do estabelecimento + “-“ + razão social do estabelecimento) |
| Selecionar todos / Desmarcar todos | Alfanumérico | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimento”. |


| Sobre a parametrização dos identificadores de tipo de serviço:  Esta parametrização pode ser efetuada para qualquer Estabelecimento, sendo ou não o Estabelecimento Centralizador.   Na geração prévia dos movimentos, quando o estabelecimento não consta da parametrização, é utilizada a parametrização do centralizador. Esta mesma lógica será utilizada na recuperação das notas para este relatório.  Desta forma, ao pesquisar se o produto (SAFX08) ou o serviço (SAFX09) está parametrizado, o procedimento é o seguinte:       - Em primeiro lugar, o produto/serviço será pesquisado na parametrização do próprio estabelecimento da nota;       - Quando não encontrado, caso o estabelecimento da nota conste como “centralizado” de algum estabelecimento “centralizador” (***), então será            feita a pesquisa na parametrização deste estabelecimento centralizador;  (***) Centralização de Estabelecimentos das Obrigações Federais   O objetivo da regra é utilizar a parametrização especifica do estabelecimento da nota, caso exista. E caso não exista, será utilizada a parametrização considerada “padrão”, que é a do estabelecimento centralizador. |
| --- |


| Valor | Campo a ser utilizado, se item de mercadoria (SAFX08) | Campo a ser utilizado, se item de serviço (SAFX09) |
| --- | --- | --- |
| Base de Cálculo Retenção | 238 (VLR_BASE_INSS) | 76 (VLR_BASE_INSS) |
| Valor Retenção | 239 – 244  (VLR_INSS_RETIDO – VLR_RET_SERV) | 77 – 96  (VLR_INSS_RETIDO – VLR_RET_SERV) |
| Valor Retenção Adicional | 240 (VLR_TOT_ADIC) | 92 (VLR_TOT_ADIC) |
| Valor Retenção Não Efetuada | 241 (VLR_N_RET_PRINC) | 99 (VLR_N_RET_PRINC) |
| Valor Retenção Adicional Não Efetuada | 242 (VLR_N_RET_ADIC) | 100 (VLR_N_RET_ADIC) |


| Primeira linha | Razão social da empresa; Data da emissão do relatório; Página; |
| --- | --- |
| Segunda linha | Informações do estabelecimento em questão: -Código e razão social -Inscrição estadual -CNPJ |
| Terceira e quarta linha | Título do relatório (“Notas Fiscais Extemporâneas não Demonstradas no Evento R-2010”); Período – Mês a Ano informados na tela da geração |


| Prestador do Serviço | Indicador, código e razão social da pessoa fis/jur referente ao prestador do serviço (SAFX04); |
| --- | --- |
| CNPJ | CNPJ da pessoa fis/jur referente ao prestador do serviço (SAFX04); |


| Data Emissão | Data de Emissão do documento fiscal |
| --- | --- |
| Número Documento | Número do documento fiscal |
| Série | Série do documento fiscal |
| Data Fiscal | Data fiscal do documento fiscal |
| Tipo de Serviço | Tipo de serviço conforme a consolidação dos itens da nota descrito “4-Regras da Recuperação dos Dados” |
| Base de Cálculo Retenção | Total da BC da Retenção, conforme a consolidação dos itens da nota descrita no item “4-Regras da Recuperação dos Dados”) |
| Vlr Retenção | Total do Valor da Retenção, conforme a consolidação dos itens da nota descrita no item “4-Regras da Recuperação dos Dados” |
| Vlr Retenção Adicional | Total do Valor da Retenção Adicional, conforme a consolidação dos itens da nota descrita no item “4-Regras da Recuperação dos Dados” |
| Vlr Retenção Não Efetuada | Total do Valor da Retenção Não Efetuada, conforme a consolidação dos itens da nota descrita no item “4-Regras da Recuperação dos Dados” |
| Vlr Retenção Adicional Não Efetuada | Total do Valor da Retenção Adicional Não Efetuada, conforme a consolidação dos itens da nota descrita no item “4-Regras da Recuperação dos Dados” |

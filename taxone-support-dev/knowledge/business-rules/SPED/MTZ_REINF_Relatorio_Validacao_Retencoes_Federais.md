# MTZ_REINF_Relatorio_Validacao_Retencoes_Federais

> Fonte: MTZ_REINF_Relatorio_Validacao_Retencoes_Federais.docx






THOMSON REUTERS

Módulo EFD Reinf
Relatório de Cruzamento de Retenções com Documento Fiscal
Relatório de Cruzamento de Retenções com Contas a Pagar
Retenções não Referenciadas em Documentos Fiscais ou Contas a Pagar
Divergência de Valores entre Retenções e Documento Fiscal/Contas a Pagar

Localização: Menu SPED, Módulo: EFD - REINF, item de menu Retenções Federais  Gerações





DOCUMENTO DE REQUISITO


Sumário

TELA A SER DESENVOLVIDA	3
1.	REGRAS DOS CAMPOS	3
1.1.	LAYOUT DA TELA:	5
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	6
2.1.	Layout do Relatório	11

## TELA A SER DESENVOLVIDA


## REGRAS DOS CAMPOS


Localização da tela: Menu, MasterSAF DW >> SPED >> EFD Reinf, menu: Retenções Federais >> Geração

Título da tela: Geração de Relatórios – EFD Reinf






### LAYOUT DA TELA:





## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:
Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.


Origem das informações para geração:
Para geração deste relatório, serão consideradas informações das seguintes origens:

SAFX07 - Tabela dos Documentos Fiscais (Capa);
SAFX03 - Tabela de Fornecedores (Contas a Pagar);
SAFX53 - Tabela da Controle de Tributos.

Regra de seleção:

- Criação do Relatório de Cruzamento de Retenções com Documento Fiscal (SAFX53 X SAFX07) com finalidade de identificar Documento Correspondente e não correspondente.

- Este relatório servirá para listar quais registros da SAFX53 têm correspondentes na SAFX07, considerando registros da SAFX53 que tenham o Tipo de Documento parametrizado na Parametrização por Tipo de Documento associado à vinculação “Documento Fiscal” e apenas os registros com Código de Tributo igual a 02 - IRRF, 05 - CSLL, 06 - PIS/PASEP ou 07 - COFINS;

- Para estabelecer o cruzamento, considerar os seguintes campos:



- Criação do Relatório de Cruzamento de Retenções com Contas a Pagar (SAFX53 X SAFX03) com finalidade de identificar Documento Correspondente e não correspondente.

Este relatório servirá para listar quais registros da SAFX53 têm correspondentes na SAFX03, considerando registros da SAFX53 que tenham o Tipo de Documento parametrizado na Parametrização por Tipo de Documento associado à vinculação “Contas a Pagar”;

Para estabelecer o cruzamento, considerar os seguintes campos:

[Alterado MFS15160]




- Criar o relatório com estrutura de cabeçalho padrão;
- Exibir no relatório as informações dos registros que tem Correspondente e os que não têm Correspondentes;
- Considerar as seguintes colunas da SAFX53 para a listagem:

- Estabelecimento;
- Data do Movimento;
- Indicador + Código da Pessoa Física/Jurídica;
- Razão Social da Pessoa Física/Jurídica;
- Tipo do Documento;
- Número do Documento;
- Série;
- Código do DARF
- Código Tributo (02 - IRRF, 05 - CSLL, 06 - PIS/PASEP e 07 - COFINS)
- Código Operação

Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a 	mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.

- A partir dos dados recuperados, conforme descrito na Origem das informações para geração e Regra de Seleção, será gerado o relatório conforme layout anexo. Ver layout do relatório na planilha anexa.

Ordenação:
Para o  tipo de relatório selecionado em tela, os dados serão ordenados da seguinte forma:

- Data do movimento, Codigo Pessoa Fis/Jur e Número de Documento.





### Layout do Relatório



Exemplo do Relatório:





## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:
Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:
Para geração deste relatório, serão consideradas informações das seguintes origens:

SAFX07 - Tabela dos Documentos Fiscais (Capa);
SAFX03 - Tabela de Fornecedores (Contas a Pagar);
SAFX53 - Tabela da Controle de Tributos.

Regra de seleção:

- Criação do Relatório de Retenções não Referenciadas em Documentos Fiscais ou Contas a Pagar (SAFX07 e SAFX03)

- Este relatório servirá para listar quais registros da SAFX53 não têm correspondentes na SAFX07 e/ou SAFX03, considerando registros da SAFX53 que cujo Tipo de Documento não tenha sido parametrizado na Parametrização por Tipo de Documento.

- Criar o relatório com estrutura de cabeçalho padrão;
- Considerar as seguintes colunas da SAFX53 para a listagem:

- Estabelecimento;
- Data do Movimento;
- Indicador + Código da Pessoa Física/Jurídica;
- Razão Social da Pessoa Física/Jurídica;
- Tipo do Documento;
- Número do Documento;
- Série;
- Código do DARF
- Código Tributo (02 - IRRF, 05 - CSLL, 06 - PIS/PASEP e 07 - COFINS)
- Código Operação

Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a 	mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.

- A partir dos dados recuperados, conforme descrito na Origem das informações para geração e Regra de Seleção, será gerado o relatório conforme layout anexo. Ver layout do relatório na planilha anexa.

Ordenação:
Para o  tipo de relatório selecionado em tela, os dados serão ordenados da seguinte forma:

- Data do movimento, Codigo Pessoa Fis/Jur e Número de Documento.




### Layout do Relatório


Exemplo do Relatório:



## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:
Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:
Para geração deste relatório, serão consideradas informações das seguintes origens:

SAFX07 - Tabela dos Documentos Fiscais (Capa);
SAFX03 - Tabela de Fornecedores (Contas a Pagar);
SAFX53 - Tabela da Controle de Tributos.

Regra de seleção:

- Criação do Relatório de Divergência de Valores entre Retenções e Documento Fiscal/Contas a Pagar (SAFX53 X SAFX07 e SAFX53 X SAFX03)

- Este relatório servirá para cruzar os registros da SAFX53 cujo Código de Tributo seja igual a 02 - IRRF, 05 - CSLL, 06 - PIS/PASEP ou 07 - COFINS e que têm correspondentes na SAFX07 e/ou SAFX03 (considerando parametrização de Tipo de Documento) com a finalidade de encontrar divergência de valores.

Para estabelecer o cruzamento, considerar os seguintes campos:



[Alterado MFS15160]




- Criar o relatório com estrutura de cabeçalho padrão;
- Exibir no relatório as informações dos registros que tem correspondente;
- Considerar as seguintes colunas da SAFX53 para a listagem:

- Estabelecimento;
- Data do Movimento;
- Indicador + Código da Pessoa Física/Jurídica;
- Razão Social da Pessoa Física/Jurídica;
- Tipo do Documento;
- Número do Documento;
- Série;
- Código do DARF
- Código Tributo (02 - IRRF, 05 - CSLL, 06 - PIS/PASEP e 07 - COFINS)
- Código Operação
- Colunas de Comparação de valores:
- SAFX53 X SAFX07:


- SAFX53 X SAFX03:



Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a 	mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.

- A partir dos dados recuperados, conforme descrito na Origem das informações para geração e Regra de Seleção, será gerado o relatório conforme layout anexo. Ver layout do relatório na planilha anexa.

Ordenação:
Para o  tipo de relatório selecionado em tela, os dados serão ordenados da seguinte forma:

- Data do movimento, Codigo Pessoa Fis/Jur e Número de Documento.





### Layout do Relatório



Exemplo do Relatório:



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS6646 | Jefferson Mota | Definição das regras da tela de Geração dos Relatórios para o EFD Reinf. |
| MFS6647 | Jefferson Mota | Definição das regras do Relatório de Retenções não Referenciadas em Documentos Fiscais ou Contas a Pagar para o EFD Reinf. |
| MFS6648 | Jefferson Mota | Definição das regras do Relatório de Divergência de Valores entre Retenções e Documento Fiscal/Contas a Pagar para o EFD Reinf. |
| MFS15160 | Lara Aline | Ajuste na validação onde passamos a considerar a Data de Movimento da SAFX03 deve ser menor ou igual a Data de Movimento da SAFX53. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data | S | S | DD/MM/AAAA | Local para digitação do período inicial e final de referencia da geração do relatório, no formato de DD/MM/AAAA.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório.  Obs: No campo do Período final, o usuário deverá informar um período maior ou igual ao período inicial. Caso informe um período menor do que o período inicial retornar a mensagem:  “O período final informado deve ser maior ou igual ao período inicial”. | MFS6646 |
| Tipo de Relatório | Dropdown | S | S | Default: não selecionado | Campo tipo lista, contendo três opções de tipos de relatórios disponível para geração. O usuário ao clicar no campo, o sistema deve exibir as seguintes opções:  - Cruzamento de Retenções com Documento      Fiscal  - Cruzamento de Retenções com Contas a Pagar  - Retenções não Referenciadas em Documentos Fiscais ou Contas a Pagar | MFS6646 |
| Geração Multiempresa | CheckBox | S | S | Default: não selecionado | Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, todas as empresas, contendo o código da empresa, código e a razão social de cada estabelecimento. | MFS6646 |
| Estabelecimentos | CheckBox | S | S | Default: não selecionado | Este campo exibe todos os estabelecimentos da empresa que acessou o módulo do EFD-Reinf.   A partir da inclusão do parâmetro “Geração Multiempresa”, a lista passou a funcionar da seguinte forma:  - Caso o parâmetro “Geração Multiempresa” estiver desmarcado: Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo. XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento).      - Caso o parâmetro “Geração Multiempresa” estiver marcado: Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão mostradas todas as empresas: XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento)         Obs: No caso da geração multiempresa, as regras da geração do relatório não se modificam. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do relatório existirão estabelecimentos de empresas distintas.  O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”.   Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS6646 |


| SAFX53 | X | SAFX07 |
| --- | --- | --- |
| 001 - Código da Empresa | = | 01 - Código da Empresa |
| 002 - Código do Estabelecimento | = | 02 - Código do Estabelecimento |
|  |  | 03 - Movimento Entrada/Saída Considerar apenas documentos de Entrada |
|  |  | 04 - Normal ou Devolução Considerar apenas documentos Normais |
| 003 - Data do Movimento | >= | Data Fiscal |
| 004 - Indicador de Pessoa Física/Jurídica | = | 06 - Indicador Pessoa Física/Jurídica |
| 005 - Código do Fornecedor | = | 07 - Código/Destinatário/Emitente/ Remetente |
| 006 - Tipo do Documento | = | 05 - Tipo do Documento |
| 007 - Número do Documento | = | 08 - Número do Documento Fiscal |
| 008 - Série do Documento | = | 09 - Série do Documento Fiscal |
| 009 - Subsérie do Documento | = | 10 - Subsérie do Documento Fiscal |
|  |  | 12 - Classificação do Documento Fiscal Considerar apenas NFs de Serviço ou Mistas |


| SAFX53 | X | SAFX03 |
| --- | --- | --- |
| 001 - Código da Empresa | = | 01 - Código da Empresa |
| 002 - Código do Estabelecimento | = | 02 - Código do Estabelecimento |
| 003 - Data do Movimento | >= | 03 - Data do Movimento |
| 004 - Indicador de Pessoa Física/Jurídica | = | 04 - Indicador Pessoa Física/Jurídica |
| 005 - Código do Fornecedor | = | 05 - Código/Destinatário/Emitente/ Remetente |
| 006 - Tipo do Documento | = | 06 - Tipo do Documento |
| 007 - Número do Documento | = | 07 - Número do Documento Fiscal |
| 008 - Série do Documento | = | 08 - Série do Documento Fiscal |
| 009 - Subsérie do Documento | = | 09 - Subsérie do Documento Fiscal |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS6646 |
| Empresa | Texto |  | Razão social da empresa. | MFS6646 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS6646 |
| Filial | Texto |  | Código e a razão social do estabelecimento em questão (estabelecimento informado em tela). | MFS6646 |
| CNPJ | Alfanumérico |  | Deverá ser exibido o CNPJ do Estabelecimento. | MFS6646 |
| Título | Texto |  | Título do relatório | MFS6646 |
| Período | Numérico | Formato: DD/MM/AAAA | Período de Referência da geração do relatório. Essa informação será recuperada de acordo com o campo “Período” da tela de Geração. | MFS6646 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Data Movimento | Data | Formato: DD/MM/AAAA | Quando Tipo de Relatório for “cruzamento com Documento Fiscal”:  - Nesta coluna deve exibir a data de movimento, referente ao campo DATA_MOVTO da tabela SAFX53, desde que a data seja >= a data fiscal da SAFX07.  Quando Tipo de Relatório for “cruzamento com Contas a Pagar”:  - Nesta coluna deve exibir a data de movimento, referente ao campo DATA_MOVTO da tabela SAFX53, desde que a data seja >= a data movimento da SAFX03. | MFS6646 |
| Indicador + Cod. Pessoa Física/Jurídica | Alfanumérico |  | Quando Tipo de Relatório for “cruzamento com Documento Fiscal”: Deve exibir o Indicador + Cod.Pessoa Física / Jurídica da SAFX53, quando for igual ao Indicador + Cod.Pessoa Física / Jurídica da SAFX07.   Quando Tipo de Relatório for “cruzamento com Contas a Pagar”: Deve exibir o Indicador + Cod.Pessoa Física / Jurídica da SAFX53, quando for igual ao Indicador + Cod.Pessoa Física / Jurídica da SAFX03. | MFS6646 |
| Razão Social Pessoa FIS/JUR | Alfanumérico |  | Deve exibir a razão social da pessoa FIS/JUR em questão da tabela Safx53. | MFS6646 |
| Tipo do Documento | Alfanumérico |  | Deve exibir o Tipo de Documento da Safx53, obedecendo a regra de associação da tela de "Parametrização por Tipo de Documento", onde devem estar associados a vinculação "Documento Fiscal", quando Tipo de Relatório for “cruzamento com Documento Fiscal”  OU  vinculado a “Contas a Pagar”, quando Tipo de Relatório for “cruzamento com Contas a Pagar”. | MFS6646 |
| Número Documento | Alfanumérico |  | Quando Tipo de Relatório for “cruzamento com Documento Fiscal”: Deve exibir o número de documento da tabela Safx53, quando for igual ao campo NUM_DOCFIS da tabela Safx07.  Quando Tipo de Relatório for “cruzamento com Contas a Pagar”: Deve exibir o número de documento da tabela Safx53, quando for igual ao campo NUM_DOCFIS da tabela Safx03. | MFS6646 |
| Série | Numérico  Alfanumérico |  | Quando Tipo de Relatório for “cruzamento com Documento Fiscal”:  Deve exibir a série do campo SERIE_DOCFIS da tabela Safx53, quando for igual ao campo SERIE_DOCFIS da tabela Safx07.  Quando Tipo de Relatório for “cruzamento com Contas a Pagar”: Deve exibir a série do campo SERIE_DOCFIS da tabela Safx53, quando for igual ao campo SERIE_DOCFIS da tabela Safx03. | MFS6646 |
| Código do DARF | Numérico  Alfanumérico |  | Deve exibir o Código DARF, referente ao campo COD_DARF da tabela SAFX53. | MFS6646 |
| Código Tributo | Numérico  Alfanumérico |  | Este campo será informado com o Código tributo ( campo COD_TRIBUTO da SAFX53), respeitando a regra de seleção, onde apenas será considerado os registros com Código de Tributo igual a 02 - IRRF, 05 - CSLL, 06 - PIS/PASEP ou 07 - COFINS. | MFS6646 |
| Código Operação | Numérico |  | Este campo será informado com a informação do campo COD_OPERACAO DA safx53. | MFS6646 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS6647 |
| Empresa | Texto |  | Razão social da empresa. | MFS6647 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS6647 |
| Filial | Texto |  | Código e a razão social do estabelecimento em questão (estabelecimento informado em tela). | MFS6647 |
| CNPJ | Alfanumérico |  | Deverá ser exibido o CNPJ do Estabelecimento. | MFS6647 |
| Título | Texto |  | Título do relatório | MFS6647 |
| Período | Numérico | Formato: DD/MM/AAAA | Período de Referência da geração do relatório. Essa informação será recuperada de acordo com o campo “Período” da tela de Geração. | MFS6647 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Data Movimento | Data | Formato: DD/MM/AAAA | Nesta coluna deve exibir a data de movimento, referente ao campo DATA_MOVTO da tabela SAFX53. | MFS6647 |
| Indicador + Cod. Pessoa Física/Jurídica | Alfanumérico |  | Deve exibir o Indicador + Cod.Pessoa Física / Jurídica, campo IND_FIS_JUR da Safx53 | MFS6647 |
| Razão Social Pessoa FIS/JUR | Alfanumérico |  | Deve exibir a razão social da pessoa FIS/JUR em questão da tabela Safx53. | MFS6647 |
| Tipo do Documento | Alfanumérico |  | Deve exibir o Tipo de Documento da Safx53, obedecendo a regra da tela de "Parametrização por Tipo de Documento", onde não deverá estar associados a nenhum dos tipos de vinculação". | MFS6647 |
| Número Documento | Alfanumérico |  | Deve exibir o número de documento do campo NUM_DOCFIS da tabela Safx53. | MFS6647 |
| Série | Numérico  Alfanumérico |  | Deve exibir a série do campo SERIE_DOCFIS da tabela Safx53. | MFS6647 |
| Código do DARF | Numérico  Alfanumérico |  | Deve exibir o Código DARF, referente ao campo COD_DARF da tabela SAFX53. | MFS6647 |
| Código Tributo | Numérico  Alfanumérico |  | Este campo será informado com o Código tributo ( campo COD_TRIBUTO da SAFX53), respeitando a regra de seleção, onde apenas será considerado os registros com Código de Tributo igual a 02 - IRRF, 05 - CSLL, 06 - PIS/PASEP ou 07 - COFINS. | MFS6647 |
| Código Operação | Numérico |  | Este campo será informado com a informação do campo COD_OPERACAO DA safx53. | MFS6647 |


| SAFX53 | X | SAFX07 |
| --- | --- | --- |
| 001 - Código da Empresa | = | 01 - Código da Empresa |
| 002 - Código do Estabelecimento | = | 02 - Código do Estabelecimento |
|  |  | 03 - Movimento Entrada/Saída Considerar apenas documentos de Entrada |
|  |  | 04 - Normal ou Devolução Considerar apenas documentos Normais |
| 003 - Data do Movimento | >= | Data Fiscal |
| 004 - Indicador de Pessoa Física/Jurídica | = | 06 - Indicador Pessoa Física/Jurídica |
| 005 - Código do Fornecedor | = | 07 - Código/Destinatário/Emitente/ Remetente |
| 006 - Tipo do Documento | = | 05 - Tipo do Documento |
| 007 - Número do Documento | = | 08 - Número do Documento Fiscal |
| 008 - Série do Documento | = | 09 - Série do Documento Fiscal |
| 009 - Subsérie do Documento | = | 10 - Subsérie do Documento Fiscal |
|  |  | 12 - Classificação do Documento Fiscal Considerar apenas NFs de Serviço ou Mistas |


| SAFX53 | X | SAFX03 |
| --- | --- | --- |
| 001 - Código da Empresa | = | 01 - Código da Empresa |
| 002 - Código do Estabelecimento | = | 02 - Código do Estabelecimento |
| 003 - Data do Movimento | >= | 03 - Data do Movimento |
| 004 - Indicador de Pessoa Física/Jurídica | = | 04 - Indicador Pessoa Física/Jurídica |
| 005 - Código do Fornecedor | = | 05 - Código/Destinatário/Emitente/ Remetente |
| 006 - Tipo do Documento | = | 06 - Tipo do Documento |
| 007 - Número do Documento | = | 07 - Número do Documento Fiscal |
| 008 - Série do Documento | = | 08 - Série do Documento Fiscal |
| 009 - Subsérie do Documento | = | 09 - Subsérie do Documento Fiscal |


| SAFX53 | X | SAFX07 |
| --- | --- | --- |
| 014 - Valor Bruto | = | 23 - Valor Total do Documento Fiscal |
| 015 - Valor do Tributo | = | Se Código de Tributo igual a 02 – IRRF Comparar com o campo 44 - Valor IR da SAFX07  Se Código de Tributo igual a 05 – CSLL Comparar com o campo 163 - Valor Tributo CSLL da SAFX07  Se Código de Tributo igual a 06 - PIS/PASEP Comparar com o campo 245 - Valor PIS Retido da SAFX07  Se Código de Tributo igual a 07 – COFINS Comparar com o campo 246 - Valor COFINS Retido da SAFX07 |


| SAFX53 | X | SAFX03 |
| --- | --- | --- |
| 014 - Valor Bruto | = | 14 - Valor da Operação |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS6648 |
| Empresa | Texto |  | Razão social da empresa. | MFS6648 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS6648 |
| Filial | Texto |  | Código e a razão social do estabelecimento em questão (estabelecimento informado em tela). | MFS6648 |
| CNPJ | Alfanumérico |  | Deve exibir o CNPJ do Estabelecimento. | MFS6648 |
| Título | Texto |  | Título do relatório | MFS6648 |
| Período | Numérico | Formato: DD/MM/AAAA | Período de Referência da geração do relatório. Essa informação será recuperada de acordo com o campo “Período” da tela de Geração. | MFS6648 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Data Movimento | Data | Formato: DD/MM/AAAA | Nesta coluna deve exibir a data de movimento, referente ao campo DATA_MOVTO da tabela SAFX53. | MFS6648 |
| Indicador + Cod. Pessoa Física/Jurídica | Alfanumérico |  | Deve exibir o Indicador + Cod.Pessoa Física / Jurídica, campo IND_FIS_JUR da Safx53 | MFS6648 |
| Razão Social Pessoa FIS/JUR | Alfanumérico |  | Deve exibir a razão social da pessoa FIS/JUR em questão da tabela Safx53. | MFS6648 |
| Tipo do Documento | Alfanumérico |  | Deve exibir o Tipo de Documento da Safx53, obedecendo a regra da tela de "Parametrização por Tipo de Documento". | MFS6648 |
| Número Documento | Alfanumérico |  | Deve exibir o número de documento do campo NUM_DOCFIS da tabela Safx53. | MFS6648 |
| Série | Numérico  Alfanumérico |  | Deve exibir a série do campo SERIE_DOCFIS da tabela Safx53. | MFS6648 |
| Código do DARF | Numérico  Alfanumérico |  | Deve exibir o Código DARF, referente ao campo COD_DARF da tabela SAFX53. | MFS6648 |
| Código Tributo | Numérico  Alfanumérico |  | Este campo será informado com o Código tributo ( campo COD_TRIBUTO da SAFX53), respeitando a regra de seleção, onde apenas será considerado os registros com Código de Tributo igual a 02 - IRRF, 05 - CSLL, 06 - PIS/PASEP ou 07 - COFINS. | MFS6648 |
| Código Operação | Numérico |  | Este campo será informado com a informação do campo COD_OPERACAO DA safx53. | MFS6648 |
| Valor Bruto | Numérico |  | Neste campo será informado as divergências  entre retenções e documento fiscal/contas a pagar, quando houver, conforme definido nas regras de geração. | MFS6648 |
| Valor do Tributo | Numérico |  | Neste campo será informado as divergências  entre retenções e documento fiscal/contas a pagar, quando houver, conforme definido nas regras de geração | MFS6648 |
|  |  |  |  |  |

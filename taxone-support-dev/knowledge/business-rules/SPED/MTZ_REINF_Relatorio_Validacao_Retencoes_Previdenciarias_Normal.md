# MTZ_REINF_Relatorio_Validacao_Retencoes_Previdenciarias_Normal

> Fonte: MTZ_REINF_Relatorio_Validacao_Retencoes_Previdenciarias_Normal.docx






THOMSON REUTERS

Módulo EFD Reinf
Relatório Previdenciário

Localização: Menu SPED, Módulo: EFD – REINF >  Relatórios> Previdenciário> Validação de Retenções Previdenciárias  Normal



DOCUMENTO DE REQUISITO


Sumário

1.	REGRAS DOS CAMPOS	3
2.	REGRAS DE GERAÇÃO DO RELATÓRIO	8
2.1.	Layout do Relatório	14

























## REGRAS DOS CAMPOS


Localização da tela: Menu: SPED, Módulo: EFD-REINF, item de menu Relatórios > Previdenciário > Validação de Retenção Previdenciária
Título da tela: Retenções Previdenciárias





















## REGRAS DE GERAÇÃO DO RELATÓRIO


Regra Geral:
Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório.

Origem das informações para geração:
Para geração deste relatório, serão consideradas informações das seguintes origens:

SAFX07 - Tabela dos Documentos Fiscais (Capa);
SAFX08 - Tabela dos Documentos Fiscais de Mercadorias e Produtos (Itens);
SAFX09 - Tabela dos Documentos Fiscais de Serviços (Itens);

[MFS18748]
A recuperação das notas do relatório irá obedecer ao campo ‘Origem’ informado na tela de emissão do relatório, ou seja:

Caso o usuário informar a opção = Entrada de Serviço, nós iremos considerar os documentos que possuam o campo MOVTO_E_S <> 9 e o campo COD_CLASS_DOC_FIS = "1" ou "2" ou “3”;
Caso o usuário informar a opção = Saída de Serviço, nós iremos considerar os documentos que possuam o campo MOVTO_E_S = 9 e o campo COD_CLASS_DOC_FIS = "2” ou “3”;

- OBS.: Para a geração de todos os relatórios, não serão considerados documentos Cancelados.

Regra de seleção dos Relatórios:

Deve existir na tela de geração de relatório, quatro opções para o relatório previdenciário, conforme critérios de geração de cada um deles como descrito
abaixo. O usuário poderá escolher uma das seguintes opções de geração possíveis do relatório:

-  “Listagem de Serviços Sujeitos à Retenção Previdenciária”;
-  “Listagem de Serviços com Retenção destacada, mas sem vinculação com um Tipo de Serviço”;
-  “Serviços com Valor de Retenção Previdenciária e com Processo indicado”;
-  “Serviços sem Valor de Retenção Previdenciária e sem Processo indicado”.
-  “Listagem com Base de INSS maior que o Valor Total Bruto”;
-  “Cálculo da Base de INSS pela Alíquota diferente do Valor de INSS informado”;
-  “Listagem de Alíquota de INSS não válida de acordo com a Legislação”.
[MFS23191]
1 - Nome do relatório:  Listagem de Serviços Sujeitos à Retenção Previdenciária

- Este relatório servirá para listar os registros da SAFX07 que tenham itens de Serviço/Produto associados (SAFX08/SAFX09) cujo código de serviço tenha sido indicado na parametrização de Identificação do Tipo de Serviço ou Identificação do Tipo de Repasse; No caso de Produto (SAFX08) serão recuperadas APENAS as notas fiscais cujo COD_MODELO seja igual a ‘07’ ou ‘67’

- Devem ser considerados os registros de NFs de Entrada da SAFX07/SAFX08/SAFX09 (inclusive notas mistas), cuja Data de Emissão compreenda o período parametrizado na tela de emissão do relatório e que sejam do estabelecimento indicado pelo usuário, além dos critérios indicador no item anterior;

Obs.: Ao final do relatório deve ser realizada uma totalização dos valores por Tipo de Serviço, conforme indicado na parametrização de
Identificação do Tipo de Serviço ou Identificação do Tipo de Repasse + Alíquota (o campo Alíquota não deve ser totalizado);

[ALTERAÇÃO MFS-866581] - Inclusão de dois totalizadores na última página do relatório:

Exibir o total de repasses e serviços por estabelecimento na última página de cada estabelcimento (label: Total dos Repasses do Estabelecimento e label: Total dos Serviços do Estabelecimento), independentemente do Tipo de Serviço. Em ambos os cenários, o campo Alíquota não deve ser totalizado. Além disso, criar um total do estabelecimento (considerando o total de Repasse + Total de Serviço, por estabelecimento)
No final de cada página do último estabelecimento de cada empresa, um total por empresa, considerando os mesmos totalizadores, só que na visão de empresa. (Label: Total dos Repasses da Empresa , Total dos Serviços da Empresa e Total Geral da Empresa).

2 - Nome do relatório: Listagem de Serviços com Retenção destacada, mas sem vinculação com um Tipo de Serviço

- Este relatório servirá para listar os registros da SAFX07 que tenham itens de Serviço/Produto associados (SAFX09/SAFX08) cujo código de serviço não tenha sido indicado na parametrização de Identificação do Tipo de Serviço ou Identificação do Tipo de Repasse, mas que tenha Valor de INSS Retido maior que zero; No caso de Produto (SAFX08) as notas fiscais deverão ser COD_MODELO seja igual a ‘07’ ou ‘67’ além do Valor de INSS Retido maior que zero.

- Devem ser considerados os registros de NFs de Entrada da SAFX07/ SAFX08/SAFX09 (inclusive notas mistas), cuja Data de Emissão compreenda o período
parametrizado na tela de emissão do relatório e que sejam do estabelecimento indicado pelo usuário, além dos critérios indicador no item anterior;

3 - Nome do relatório: Serviços com Valor de Retenção Previdenciária e com Processo indicado

- Este relatório servirá para listar os registros da SAFX07 que tenham itens de Serviço/Produto associados (SAFX08/SAFX09) cujo código de serviço tenha sido indicado na parametrização de Identificação do Tipo de Serviço ou Identificação do Tipo de Repasse, que tenha o campo Valor do INSS maior que zero E que tenha o campo Número do Processo preenchido; No caso de Produto (SAFX08) as notas fiscais também deverão ser COD_MODELO seja igual a ‘07’ ou ‘67’.

- Devem ser considerados os registros de NFs de Entrada da SAFX07/SAFX08/SAFX09 (inclusive notas mistas), cuja Data de Emissão compreenda o período parametrizado na tela de emissão do relatório e que sejam do estabelecimento indicado pelo usuário, além dos critérios indicador no item anterior;

4 - Nome do relatório: Serviços sem Valor de Retenção Previdenciária e sem Processo indicado

- Este relatório servirá para listar os registros da SAFX07 que tenham itens de Serviço/Produto associados (SAFX08/SAFX09) cujo código de serviço tenha sido indicado na parametrização de Identificação do Tipo de Serviço ou Identificação do Tipo de Repasse, que tenha o campo Valor do INSS igual a zero e que o campo Número do Processo não tem sido preenchido; No caso de Produto (SAFX08) as notas fiscais também deverão ser COD_MODELO seja igual a ‘07’ ou ‘67’.

- Devem ser considerados os registros de NFs de Entrada da SAFX07/SAFX08/SAFX09 (inclusive notas mistas), cuja Data de Emissão compreenda o período parametrizado na tela de emissão do relatório e que sejam do estabelecimento indicado pelo usuário, além dos critérios indicador no item anterior;

[MFS14863]
5 - Nome do relatório: Listagem com Base de INSS maior que o Valor Total Bruto

- Este relatório servirá para listar os registros da SAFX07 que tenham itens de Serviço/Produto associados (SAFX08/SAFX09) cujo código de serviço tenha sido indicado na parametrização de Identificação do Tipo de Serviço ou Identificação do Tipo de Repasse, que tenha o campo Base de INSS (VLR_BASE_INSS SAFX08/09) maior que o campo Valor Total Bruto (VLR_TOT_NOTASAFX07). No caso de Produto (SAFX08) as notas fiscais também deverão ser COD_MODELO seja igual a ‘07’ ou ‘67’.

- Devem ser considerados os registros de NFs de Entrada da SAFX07/SAFX08/SAFX09 (inclusive notas mistas), cuja Data de Emissão compreenda o período parametrizado na tela de emissão do relatório e que sejam do estabelecimento indicado pelo usuário, além dos critérios indicador no item anterior;

6 - Nome do relatório: Cálculo da Base de INSS pela Alíquota diferente do Valor de INSS informado

- Este relatório servirá para listar os registros da SAFX07 que tenham itens de Serviço/Produto associados (SAFX08/SAFX09) cujo código de serviço tenha sido indicado na parametrização de Identificação do Tipo de Serviço ou Identificação do Tipo de Repasse, que o resultado do cálculo da Base de INSS * Alíquota (VLR_BASE_INSS * VLR_ALIQ_INSS SAFX08/09) seja diferente do valor encontrado no campo Valor do INSS (VLR_INSS_RETIDO SAFX08/09) informado; No caso de Produto (SAFX08) as notas fiscais também deverão ser COD_MODELO seja igual a ‘07’ ou ‘67’.

- Devem ser considerados os registros de NFs de Entrada da SAFX07/SAFX08/SAFX09 (inclusive notas mistas), cuja Data de Emissão compreenda o período parametrizado na tela de emissão do relatório e que sejam do estabelecimento indicado pelo usuário, além dos critérios indicador no item anterior;

7 - Nome do relatório: Listagem de Alíquota de INSS não válida de acordo com a Legislação

- Este relatório servirá para listar os registros da SAFX07 que tenham itens de Serviço/Produto associados (SAFX08/SAFX09) cujo código de serviço tenha sido indicado na parametrização de Identificação do Tipo de Serviço ou Identificação do Tipo de Repasse, que o valor da Alíquota de INSS (VLR_ALIQ_INSS SAFX08/09) não seja uma alíquota válida de acordo com a legislação (Alíquotas válidas: 3,5 % ou 11%); No caso de Produto (SAFX08) as notas fiscais também deverão ser COD_MODELO seja igual a ‘07’ ou ‘67’.

- Devem ser considerados os registros de NFs de Entrada da SAFX07/SAFX08/SAFX09 (inclusive notas mistas), cuja Data de Emissão compreenda o período parametrizado na tela de emissão do relatório e que sejam do estabelecimento indicado pelo usuário, além dos critérios indicador no item anterior;


- Para todas as possibilidades de geração do relatório previdenciário, devem ser exibidos os seguintes campos no relatório:

[MFS21682]
- Estabelecimento
- Tipo do Documento
- Indicador + Código PFJ
- CNPJ da PFJ
- Número do Documento Fiscal
- Série / Subsérie do Documento Fiscal
- Data de Emissão
- Data Fiscal
- Classificação do Documento Fiscal
- Código Serviço/Produto
- Valor Total do Documento Fiscal
- Valor Total Serviços
- Valor Base INSS
- Valor Alíquota INSS
- Valor INSS Retido
- Tipo do Processo Principal
- Número do Processo Principal
- Tipo do Processo Adicional
- Número do Processo Adicional


- Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a
mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório.

- A partir dos dados recuperados, conforme descrito na Origem das informações para geração e Regra de Seleção, será gerado o relatório conforme layout anexo. Ver layout do relatório na planilha anexa.













### Layout do Relatório


Exemplo do Relatório :











Exemplo do Relatório TAXONE:



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS7084 | Jefferson Mota | Definição das regras de criação dos Relatórios Previdenciários para o EFD Reinf. |
| MFS12751 | Elenilson Coutinho | Alteração na busca das informações para geração do relatório que era a partir da SAFX07 e passou a ser da SAFX09. |
| MFS16773 | Lara Aline | Inclusão da origem da informação pelas notas de serviço de transporte (SAFX08) |
| MFS17891 | Lara Aline | Ajuste na geração do campo Pessoa Física/Juridica, para considerar apenas Pessoa Juridica (CNPJ). |
| MFS17634 | Lara Aline | Inclusão das colunas Tipo Processo Adicional e Número Processo Adicional. |
| MFS15748 | Lara Aline | Inclusão das colunas Código e Descrição do item do serviço/produto. |
| MFS18748 | Lara Aline | Inclusão das notas de saída de serviço na origem do relatório. |
| MFS14863 | Lara Aline | Inclusão de 3 novas validações no relatório. |
| MFS21682 | Lara Aline | Inclusão da coluna CNPJ da Pessoa Juridica. |
| MFS23191 | Lara Aline | Alteração na regra de emissão de todos os modelos de relatórios incluindo a verificação também pelo Identificação do Tipo de Repasse. |
| MFS-866581 | Alessandra Cristina Navatta | Apenas Produto TAXONE: Incluir três totalizadores na última página do relatório ‘Listagem de Serviços Sujeitos à Retenção Previdenciária’ (de cada estabelecimento): Total dos Repasses do Estabelecimento. Total dos Serviços do Estabelecimento. Total Geral do Estabelecimento E no final do último estabelecimento de cada empresa, colocar os mesmos totalizadores por empresa: Total dos Repasses da Empresa. Total dos Serviços da Empresa. Total Geral da Empresa |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data | S | S | Formato: MM/AAAA  Default: Habilitado | Local para digitação do período inicial e final de referencia da geração do relatório, no formato de DD/MM/AAAA.  Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório.  Obs: No campo do Período final, o usuário deverá informar um período maior ou igual ao período inicial. Caso informe um período menor do que o período inicial retornar a mensagem:  “O período final informado deve ser maior ou igual ao período inicial”. | MFS18748 |
| Tipo do Relatório | ComboBox | S | S | Default: Habilitado | Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:   Listagem de Serviços Sujeitos à Retenção Previdenciária; Listagem de Serviços com Retenção destacada, mas sem vinculação com um Tipo de Serviço;  Serviços com Valor de Retenção Previdenciária e com Processo indicado; Serviços sem Valor de Retenção Previdenciária e sem Processo indicado;  Listagem com Base de INSS maior que o Valor Total Bruto Cálculo da Base de INSS pela Alíquota diferente do Valor de INSS informado Listagem de Alíquota de INSS não válida de acordo com a Legislação | MFS18748 MFS14863 |
| Origem | Checkbox | S | S | Default: Entrada de Serviço | Permitir que o usuário informe qual origem que será emitido o relatório, Serão listadas as seguintes opções:  Entrada de Serviço Saída de Serviço  O usuário só poderá escolher uma das opções. | MFS18748 |
| Multiempresas | Checkbox | N | S | Default: Desmarcado | Na abertura da tela esta opção aparecerá sempre desmarcada. | MFS18748 |
| Estabelecimentos | CheckBox | S | S | Default: não selecionado | Este campo exibe todos os estabelecimentos da empresa que acessou o módulo do EFD-Reinf.   A partir da inclusão do parâmetro “Geração Multiempresa”, a lista passou a funcionar da seguinte forma:  - Caso o parâmetro “Geração Multiempresa” estiver desmarcado: Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo. XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento).      - Caso o parâmetro “Geração Multiempresa” estiver marcado: Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão mostradas todas as empresas: XXXXX / XXXXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento)         Obs: No caso da geração multiempresa, as regras da geração do relatório não se modificam. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do relatório existirão estabelecimentos de empresas distintas.  O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”.   Como facilitador, poderão ser utilizadas as opções “Selecionar todos” e “Desmarcar todos”. | MFS18748 |
| Selecionar Todos | Botão | N | S | Default: desabilitado | Neste campo é possível selecionar todos os estabelecimentos demostrados no campo Estabelecimento.  Quando acionado, muda o status dos códigos de estabelecimento que não estão selecionados para selecionado. | MFS18748 |
| Desmarcar Todos | Botão | N | S | Default: desabilitado | Neste campo é possível desmarcar todos os estabelecimentos que estão selecionados no campo Estabelecimento.  Quando acionado, muda o status dos códigos de estabelecimento que estão selecionados para não selecionado. | MFS18748 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| Data | Data | DD/MM/AAAA às HH:MM:SS hs | Data de emissão e hora do relatório | MFS7084 |
| Empresa | Texto |  | Razão social da empresa. | MFS7084 |
| Página | Numérico |  | Número da página sequencial do relatório | MFS7084 |
| Estabelecimento | Texto |  | Código e a razão social do estabelecimento em questão (estabelecimento informado em tela). | MFS7084 |
| CNPJ | Alfanumérico |  | Deve exibir o CNPJ do Estabelecimento. | MFS7084 |
| Título | Texto |  | Título do relatório | MFS7084 |
| Período | Numérico | Formato: DD/MM/AAAA | Período de Referência da geração do relatório. Essa informação será recuperada de acordo com o campo “Período” da tela de Geração. | MFS7084 |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |
| Estabelecimento | Alfanumérico |  | Nesta coluna deve exibir o estabelecimentos selecionado na tela de geração. | MFS7084 |
| Tipo do Documento | Alfanumérico |  | Deve exibir o Tipo de Documento do campo COD_DOCTO da SAFX08/SAFX09. | MFS7084 MFS16773 |
| Indicador + Cod. Pessoa Jurídica | Alfanumérico |  | Deve exibir o Indicador + Cod. Pessoa Jurídica, campo IND_FIS_JUR da SAFX07.  Serão considerados apenas as Pessoas Jurídicas ou seja, código Pessoa Física/ Jurídica com 14 posições. | MFS7084 MFS17891 |
| CNPJ da Pessoa Jurídica | Alfanumérico |  | Deve exibir o CNPJ Pessoa Jurídica, campo CPF_CGC da SAFX04 que corresponde ao Indicador + Cod. Pessoa Jurídica da SAFX07 do campo Indicador + Cod. Pessoa Jurídica.  Serão considerados apenas as Pessoas Jurídicas, ou seja, CPF-CGC Pessoa Física/ Jurídica com 14 posições. | MFS21682 |
| Número Documento | Alfanumérico |  | Deve exibir o número de documento do campo NUM_DOCFIS da tabela SAFX07 | MFS7084 MFS12751 |
| Série/SubSérie | Numérico  Alfanumérico |  | Deve exibir a série  e subSérie do campo SERIE_DOCFIS e SUB_SERIE_DOCFIS da tabela SAFX07 | MFS7084 MFS12751 |
| Data Emissão | Data | Formato: DD/MM/AAAA | Nesta coluna deve exibir a data de Emissão, referente ao campo DATA_EMISSAO da tabela SAFX07. | MFS7084 |
| Data Fiscal | Data | Formato: DD/MM/AAAA | Nesta coluna deve exibir a data de Emissão, referente ao campo DATA_FISCAL da tabela SAFX08/SAFX09. | MFS7084 MFS12751 MFS16773 |
| Classificação do Documento Fiscal | Numérico  Alfanumérico |  | Deve exibir a classificação do documento fiscal, campo COD_CLASS_DOC_FIS da tabela SAFX07. | MFS7084 |
| Código Serviço/Produto | Alfanumérico |  | Deve exibir o Código do Serviço ou Produto + Descrição respectiva, campo COD_SERVICO da SAFX09 ou COD_PRODUTO da SAFX08.  Caso Serviço, a descrição correspondente ao código será recuperada da tabela SAFX2018.  Caso Produto, a descrição correspondente ao código será recuperada da tabela SAFX2013. | MFS15748 |
| Valor Total do Documento Fiscal | Numérico  Alfanumérico |  | Deve exibir o valor total do documento fiscal, campo VLR_TOT_NOTA da tabela SAFX07. | MFS7084 |
| Valor Serviços | Numérico |  | Este campo deve informar o valor do serviço destacados na nota. Campo VLR_ITEM/VLR_SERVICO da tabela SAFX08/SAFX09. | MFS7084 MFS12751 MFS16773 |
| Valor Base INSS | Numérico |  | Este campo deve informar o valor Base do INSS, campo VLR_BASE_INSS da tabela SAFX08/SAFX09. | MFS7084 MFS12751 MFS16773 |
| Valor Alíquota INSS | Numérico |  | Este campo deve informar o valor da alíquota do INSS, campo VLR_ALIQ_INSS da tabela SAFX08/SAFX09. | MFS7084 MFS12751 MFS16773 |
| Valor INSS Retido | Numérico |  | Este campo deve informar o valor do INSS retido, campo VLR_INSS_RETIDO da tabela SAFX08/SAFX09. | MFS7084 MFS12751 MFS16773 |
| Tipo do Processo Principal | Numérico  Alfanumérico |  | Este campo deve informar o tipo de processo referente ao campo IND_TP_PROC_ADJ_PRINC da tabela SAFX08/SAFX09. | MFS7084 MFS12751 MFS16773 MFS17634 |
| Número do Processo Principal | Numérico  Alfanumérico |  | Este campo deve informar o número do processo do campo NUM_PROC_ADJ_PRINC da tabela SAFX08/SAFX09. | MFS7084 MFS12751 MFS16773 MFS17634 |
| Tipo do Processo Adicional | Numérico  Alfanumérico |  | Este campo deve informar o tipo de processo referente ao campo IND_TP_PROC_ADJ_ADIC da tabela SAFX08/SAFX09. | MFS17634 |
| Número do Processo Adicional | Numérico  Alfanumérico |  | Este campo deve informar o número do processo do campo NUM_PROC_ADJ_ADIC da tabela SAFX08/SAFX09. | MFS17634 |

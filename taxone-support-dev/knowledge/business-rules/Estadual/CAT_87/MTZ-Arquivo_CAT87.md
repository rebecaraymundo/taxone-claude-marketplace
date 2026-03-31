# MTZ-Arquivo_CAT87

- **Fonte:** MTZ-Arquivo_CAT87.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 80 KB

---

THOMSON REUTERS

<a id="OLE_LINK1"></a>Portaria CAT87/06 – Protocolo ECF 04\-01

Documento Matriz \- Arquivo do Meio Magnético

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4817

Jefferson Mota

Definição de regras para geração do arquivo magnético para Portaria CAT87/06

MFS11281

Andrea Rocha

Inclusão das tabelas SAFX204 e SAFX205 para gerar o meio magnético e alteração do layout do arquivo gerado\.

MFS17730

João Henrique

Alteração na regra geral da geração do arquivo\. Essa modificação tem como finalidade gerar o registro 65 – Operações Realizadas mesmo quando o contribuinte não possui movimento no período\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral de Geração do Arquivo do Meio Magnético – CAT87/06\.__

O arquivo magnético da CAT87/06, tem por objetivo gerar informações dos dados do Estabelecimento, Cupom Fiscal e Informações de Notas Fiscais, referente a vendas com cartões de crédito e débito\. 

Observar orientações existentes no arquivo "DE\_PARA\_CAT87\.xlsx"\.

- __Origem das informações__: Cadastro do Estabelecimento, Detalhes do Meio de Pagamento \(SAFX995\), Tabela das Formas de Pagamento do CFe\.\(SAFX204\) e Tabela das Formas de Pagamento do NFCe e NFe \(SAFX205\)\.
- __Regra de seleção__: há uma regra de seleção específica para cada registro do arquivo da CAT87, porém, de forma geral, o arquivo será gerado com informações de cadastros do estabelecimentos, SAFX995, SAFX204 e SAFX205\.

Deve ser gerado um arquivo por estabelecimento administrador de cartão de crédito, contendo dados de todos os estabelecimentos credenciados associados ao estabelecimento administrador \(menu: Parâmetros >> Identificação da Administradora\) selecionado em questão, gerado sempre que na tela de Geração do Meio Magnético, a opção “Quebrar Arquivo por Estabelecimento Credenciado” estiver desmarcada, considerando os critérios de geração dos registros\.

Se no período informado da geração do arquivo magnético CAT87/06 o contribuinte não possuir dados nas tabelas para gerar o registro 65 – Operações Realizadas, o sistema deverá gerar o arquivo com as informações dos registros 10,11 e 90\.

Quando a opção de “Quebrar Arquivo por Estabelecimento Credenciado” estiver “Marcada”, deverá gerar um arquivo por cada estabelecimento credenciado associado ao estabelecimento administrador\. 

O arquivo gerado será do tipo Texto, respeitando o tamanho fixo de cada campo, utilizando espaços em brancos a direita para campos alfanuméricos,  ou zeros a esquerda para campos do tipo numérico quando for necessário\. Para os valores, será informado com __2__ decimais\. 

- __Nome do Arquivo__: O arquivo será gerado com a seguinte nomenclatura:

– Para os casos de geração do arquivo normal, sem a opção de “Quebrar Arquivo por Estabelecimento Credenciado”, estar Selecionada, deverá ficar da seguinte forma:

__MMAAAA\_CNPJ da Administradora\.TXT __

__MMAAAA:__ Mês e Ano do período de geração\.

__       CNPJ da Administradora:__ CNPJ do estabelecimento administradora parametrizado para a geração\.

– Para os casos de geração do arquivo com a opção de “Quebrar Arquivo por Estabelecimento Credenciado” “Selecionada”, deverá ficar da seguinte forma:

__MMAAAA\_CNPJ da Administradora\_CNPJ do Estabelecimento Credenciado\.TXT __

__MMAAAA:__ Mês e Ano do período de geração\.

__       CNPJ da Administradora:__ CNPJ do estabelecimento Administradora parametrizado para a geração\.

__       CNPJ do Estabelecimento Credenciado:__ CNPJ do estabelecimento Credenciado pela administradora\.

OS4817

MFS17730

- __Registro Tipo 10 – Mestre da Administradora__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN\_10\-00

- __Origem das informações__: Cadastro do Estabelecimento\.
- __Regra de seleção__: As informações de cadastro que serão informadas para a composição do registro tipo __10__, deverão ser referentes a empresa que foi selecionada no campo “Estabelecimento/Administradora”, da tela de “Identificação da administradora”, localizada no menu “Parâmetros” do módulo  Portaria CAT87/06 – Protocolo ECF 04\-01\.
- __Campos\-Chave__:  CNPJ/MF, Enscrição Estadual e Data Inicial do Período
- __Nível hierárquico do registro__: não se aplica\.
- __Ordenação__: primeiro registro da estrutura\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: Um por arquivo\.

OS4817

RN\_10\-03

__Regra para o campo Inscrição Estadual__

Inscrição estadual do estabelecimento \(administradora\) no Estado de domicílio:

\- Deverá preencher com a informação do campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL, referente ao estabelecimento que está na geração da carga de dados\.

Obs\.: O campo Inscrição Estadual é alfanumérico com uma característica especial, devendo ser informados todos os caracteres da Inscrição Estadual, inclusive os numéricos não significativos \(zeros à esquerda\), deixando\-se em branco as posições à direita\.

Tamanho do campo: 14 posições

Tipo: Alfanumérico

OS4817

RN\_10\-07

__Regra para o campo Unidade da Federação__

Deverá preencher com a informação do campo COD\_ESTADO da tabela ESTADO,  referente ao campo IDENT\_ESTADO da tabela ESTABELECIMENTO\.

Tamanho do campo: 02 posições

Tipo: Alfanumérico

OS4817

RN\_10\-09

__Regra para o campo Data Inicial__

Este campo deverá ser preenchido com a informação do campo “Data Inicial” da tela de geração do Meio Magnético, localizada

em:  “MasterSAF DW >> Estadual >> Portaria CAT87/06 – Protocolo ECF 04\-01, Menu:__ __Obrigações >> Geração do Meio Magnético”\.

Obs\.: As datas deverão ser expressas no formato ano, mês e dia __\(AAAAMMDD\)\.__

Tamanho do campo: 08 posições

Tipo: Numérico

OS4817

RN\_10\-10

__Regra para o campo Data Final__

Este campo deverá ser preenchido com a informação do campo “Data Final” da tela de geração do Meio Magnético, localizada

em:  “MasterSAF DW >> Estadual >> Portaria CAT87/06 – Protocolo ECF 04\-01, Menu:__ __Obrigações >> Geração do Meio Magnético”\.

Obs\.: As datas deverão ser expressas no formato ano, mês e dia __\(AAAAMMDD\)\.__

Tamanho do campo: 08 posições

Tipo: Numérico

OS4817

RN\_10\-12

__Regra para o campo Código da Identificação da Natureza das Operações__

Este campo deverá ser preenchido com a informação que foi selecionada no campo “Código das Operações” , localizado na tela de Geração do Meio Magnético em:  “MasterSAF DW >> Estadual >> Portaria CAT87/06 – Protocolo ECF 04\-01, Menu:__ __Obrigações >> Geração do Meio Magnético”\.

Tamanho do campo: 01 posição

Tipo: Alfanumérico

OS4817

RN\_10\-13

__Regra para o campo Código da finalidade do arquivo__

Este campo deverá ser preenchido com a informação que foi selecionada no campo “Tipo  de Declaração” , localizado na tela de Geração do Meio Magnético em:  “MasterSAF DW >> Estadual >> Portaria CAT87/06 – Protocolo ECF 04\-01, Menu:__ __Obrigações >> Geração do Meio Magnético”\.

Tamanho do campo: 01 posição

Tipo: Alfanumérico

OS4817

- __Registro Tipo 11 – Dados Complementares da Administradora__

RN\_11\-00

- __Origem das informações__: Cadastro do Estabelecimento e Cadastro do Responsável Legal\.
- __Regra de seleção__: As informações de cadastro que serão informadas para a composição do registro tipo __11__, também são referentes a empresa que foi selecionada no campo “Estabelecimento/Administradora”, da tela de “Identificação da administradora”, localizada no menu “Parâmetros” do módulo  Portaria CAT87/06 – Protocolo ECF 04\-01\. O registro tipo 11, é um complemento do registro 10, contendo algumas informações adicionais de local, contato e nome do responsavel pela geração\.
- __Campos\-Chave__: não se aplica\.
- __Nível hierárquico do registro__: não se aplica\.
- __Ordenação__: segundo registro da estrutura\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: Um por arquivo\.

OS4817

RN\_11\-07

__Regra para o campo Nome do Contato__

Este campo deverá ser preenchido com a informação do responsável para contato,  que foi selecionado no campo “Responsável Legal” , localizado na tela: “ Módulo: MasterSAF DW >> Estadual >> Portaria CAT87/06 – Protocolo ECF 04\-01, Menu:__ __Parâmetros >> Dados Iniciais>>Responsável Legal”\.

A informação a ser gerada é do campo Nome/Razão Social do Cadastro do Responsável Legal que foi associado ao estabelecimento administrador que está gerando o arquivo\.

Tamanho Máximo do campo: 28 posições

Tipo: Alfanumérico

OS4817

- __Registro Tipo 65 – Registro das Operações Realizadas__

RN\_65\-00

- __Origem das informações__: Tabela Detalhe Meio de Pagamento \(SAFX995\), Tabela das Formas de Pagamento do CFe\.\(SAFX204\), Tabelas dos Documentos Fiscais \(SAFX07\) e Tabela das Formas de Pagamento do NFCe e NFe \(SAFX205\)\.
- __Regra de seleção SAFX995__: As informações para a composição do registro tipo __65__ são referentes aos registros da  tabela SAFX995, para todos os estabelecimentos que foram selecionados na lista, da tela de “Identificação da administradora”, localizada no menu “Parâmetros” do módulo  Portaria CAT87/06 – Protocolo ECF 04\-01\. 

Devem ser considerados os registros da SAFX995 dos estabelecimentos credenciados parametrizados, considerando que a data de emissão \(DATA\_EMISSAO\) compreenda o período informado e o Código do Meio de Pagamento \(COD\_MEIO\_PAGTO\) tenha sido parametrizado na tela de Parametrização do Meio de Pagamento \(considerar a composição completa da parametrização: Empresa, Estabelecimento, Modelo Documento, Número do Caixa e Código do meio de Pagamento\)\.

- __Regra de seleção SAFX204__: As informações para a composição do registro tipo __65__ são referentes aos registros da  tabela SAFX204, para todos os estabelecimentos que foram selecionados na lista, da tela de “Identificação da administradora”, localizada no menu “Parâmetros” do módulo  Portaria CAT87/06 – Protocolo ECF 04\-01\. 

Devem ser considerados os registros da SAFX204 dos estabelecimentos credenciados parametrizados, considerando que a data de emissão \(DATA\_EMISSAO\) compreenda o período informado\. 

- __Regra de seleção SAFX205__: As informações para a composição do registro tipo __65__ são referentes aos registros das tabelas SAFX07 e SAFX205, para todos os estabelecimentos que foram selecionados na lista, da tela de “Identificação da administradora”, localizada no menu “Parâmetros” do módulo  Portaria CAT87/06 – Protocolo ECF 04\-01\. 

Devem ser considerados os registros da SAFX07 e SAFX205 que atendam aos seguintes critérios:

\- Estabelecimentos credenciados parametrizados,

\- Data fiscal \(DATA\_FISCAL\) compreenda o período informado,

\- Somente documentos fiscais de mercadoria \(classificação do documento = ‘1’ ou ‘3’\),

\- Somente notas não canceladas,

\- Modelo de documento = ‘55’ ou ‘65’,

\-Somente notas de saída \(MOVTO\_E\_S = ‘9’\)\.

- __Campos\-Chave__: CNPJ/MF, Inscrição Estadual, Número do Documento Fiscal e Data de Emissão/Data Fiscal\.
- __Nível hierárquico do registro__: não se aplica\.
- __Ordenação__: terceiro registro da estrutura\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: Vários por arquivo\.

RN\_65\-02

__Regra para o campo CNPJ/MF__

Este campo deve ser preenchido com a informação do  campo CGC da tabela ESTABELECIMENTO, referente ao estabelecimento credenciado que foi selecionado na lista de estabelecimentos da tela de Identificação da Administradora , localizado em: “Módulo: MasterSAF DW >> Estadual >> Portaria CAT87/06 – Protocolo ECF 04\-01, Menu:__ __Parâmetros >> Identificação da Administradora”

Tamanho do campo: 14 posições

Tipo: Numérico

OS4817

RN\_65\-03

__Regra para o campo Inscrição Estadual__

Este campo deve ser preenchido com a informação da  INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL, referente ao estabelecimento credenciado que foi selecionado na lista de estabelecimento da na tela de Identificação da Administradora, localizado em: “Módulo: MasterSAF DW >> Estadual >> Portaria CAT87/06 – Protocolo ECF 04\-01, Menu:__ __Parâmetros >> Identificação da Administradora”\.

Obs\.: O campo Inscrição Estadual é alfanumérico com uma característica especial, devendo ser informados todos os caracteres da Inscrição Estadual, inclusive os numéricos não significativos \(zeros à esquerda\), deixando\-se em branco as posições à direita\.

Tamanho do campo: 14 posições

Tipo: Alfanumérico

OS4817

RN\_65\-06

__Regra para o campo Natureza da Operação__

__Origem SAFX995:__

Este campo deve ser preenchido com a informação do campo 12 \(Natureza da Operação\) da tabela SAFX995\.

__Origem SAFX204:__

Este campo deve ser preenchido com a informação do campo 08 \(Natureza da Operação\) da tabela SAFX204\.

__Origem SAFX205:__

Este campo deve ser preenchido com a informação do campo 14 \(Natureza da Operação\) da tabela SAFX205\.

Tamanho do campo: 01 posição

Tipo: Numérico

OS4817/ MFS11281

RN\_65\-06

__Campo Excluído__

__Regra para o campo Número de Cadastro do Estabelecimento Comercial__

Este campo deve ser preenchido com a informação do campo “N° de Cadastro do Estabelecimento Comercial”, criado na tela de “Identificação da Administradora”, localizado em: “Módulo: MasterSAF DW >> Estadual >> Portaria CAT87/06 – Protocolo ECF 04\-01, Menu:__ __Parâmetros >> Identificação da Administradora”

Tamanho do campo: 20 posições

Tipo: Alfanumérico

OS4817/ MFS11281

RN\_65\-07

__Regra para o campo Tipo da Operação__

__Origem SAFX995:__

Este campo deve ser preenchido com a informação do campo 13 \(Natureza da Operação\) da tabela SAFX995\.

__Origem SAFX204:__

Este campo deve ser preenchido com a informação do campo Tipo de Operação da <a id="_Toc483384700"></a>Parametrização Código de Operação X Tipo da Operação\.  A partir do campo Código de Operação \(campo 06\) da tabela SAFX204, recuperar o Tipo de Operação correspondente ao Código da Operação da parametrização,  localizada em: Módulo: MasterSAF DW >> Estadual >> Portaria CAT87/06 – Protocolo ECF 04\-01, Menu:__ __Parâmetros >> Código de Operação X Tipo da Operação\.

__Origem SAFX205:__

Este campo deve ser preenchido com a informação do campo Tipo de Operação da Parametrização Código de Operação X Tipo da Operação\.  A partir do campo Código de Operação \(campo 12\) da tabela SAFX205, recuperar o Tipo de Operação correspondente ao Código da Operação da parametrização,  localizada em: Módulo: MasterSAF DW >> Estadual >> Portaria CAT87/06 – Protocolo ECF 04\-01, Menu:__ __Parâmetros >> Código de Operação X Tipo da Operação\.

Tamanho do campo: 01 posição

Tipo: Numérico

OS4817/ MFS11281

RN\_65\-09

__Regra para o campo Modelo de Documento Fiscal__

__Origem SAFX995:__

Este campo deve ser preenchido com a informação do campo 03 \(Modelo Documento\) da tabela SAFX995\.

__Origem SAFX204:__

Este campo deve ser preenchido com a informação do campo 06 \(Modelo Documento\) da tabela SAFX201, correspondente ao registro da tabela SAFX204\.

__Origem SAFX205:__

Este campo deve ser preenchido com a informação do campo 13 \(Modelo Documento\) da tabela SAFX07, correspondente ao registro da tabela SAFX205\.

Tamanho do campo: 02 posições

Tipo: Alfaumérico

OS4817/ MFS11281

RN\_65\-14

__Regra para o campo UF __

Este campo deve ser preenchido com a informação do campo ESTADO da tabela ESTABELECIMENTO, referente ao estabelecimento credenciado que foi selecionado na lista de estabelecimentos da tela de Identificação da Administradora , localizado em: “Módulo: MasterSAF DW >> Estadual >> Portaria CAT87/06 – Protocolo ECF 04\-01, Menu:__ __Parâmetros >> Identificação da Administradora”

Tamanho do campo: 2 posições

Tipo: Alfanumérico

MFS11281

RN\_65\-15

__Regra para o campo Código do Município __

Este campo deve ser preenchido com a informação do  campo COD\_UF \+ campo COD\_MUNICIPIO da tabela MUNICIPIO, referente o IDENT\_ESTADO e COD\_MUNICIPIO da tabela ESTABELECIMENTO, referente ao estabelecimento que foi selecionado na lista de estabelecimentos da  tela de Identificação da Administradora, localizado em: “Módulo: MasterSAF DW >> Estadual >> Portaria CAT87/06 – Protocolo ECF 04\-01, Menu:__ __Parâmetros >> Identificação da Administradora”

Tamanho do campo: 14 posições

Tipo: Numérico

OS4817

- __Registro Tipo 66 – Total por Estabelecimento Credenciado__

RN\_66\-00

- __Origem das informações__: Registro Tipo 65, Tabela Detalhe Meio de Pagamento \(SAFX995\), Tabela das Formas de Pagamento do CFe\.\(SAFX204\) e Tabela das Formas de Pagamento do NFCe e NFe \(SAFX205\)\.
- __Regra de seleção__: As informações que serão informadas para a composição do registro tipo __66__, são os somatórios dos valores de alguns campos do registros tipo 65\. Ele é um consolidado das informações dos estabelecimentos credenciados cujo detalhe foi demonstrado no registro 65\. 
- __Campos\-Chave__: CNPJ/MF, Inscrição Estadual e Período de Referência
- __Nível hierárquico do registro__: não se aplica
- __Ordenação__: quarto registro da estrutura\.
- __Agrupamento__: CNPJ/MF, Inscrição Estadual e Período de Referência\.
- __Ocorrência__: Vários por arquivo\.

OS4817/ MFS11281

RN\_66\-02

__Regra para o campo CNPJ/MF__

Este campo deve ser preenchido com a informação do  campo CGC da tabela ESTABELECIMENTO, referente ao estabelecimento credenciado que foi selecionado na lista de estabelecimentos da tela de Identificação da Administradora , localizado em: “Módulo: MasterSAF DW >> Estadual >> Portaria CAT87/06 – Protocolo ECF 04\-01, Menu:__ __Parâmetros >> Identificação da Administradora”

Tamanho do campo: 14 posições

Tipo: Numérico

OS4817

RN\_66\-04

__Regra para o campo Período de Referencia__

Este campo deve ser preenchido com o Ano e mês, no formato __AAAAMM__ do campo “Data Inicial” da tela de geração do Meio Magnético, localizada em:  “MasterSAF DW >> Estadual >> Portaria CAT87/06 – Protocolo ECF 04\-01, Menu:__ __Obrigações >> Geração do Meio Magnético”\.

Tamanho do campo: 06 posições

Tipo: Numérico

OS4817

RN\_66\-05

__Regra para o campo Montante de Cartão de Crédito__

Este campo deve ser preenchido  com o valor total das operações realizadas no período, referente a Cartão de Crédito\. 

Deve ser o somatório dos campos “Valor da Operação” dos registros Tipo 65, desde que,  o campo “Natureza da Operação” dos registros tipo 65, esteja informado com o valor __“1”__\.

Tamanho do campo: 18 posições \(com 2 decimais\)

Tipo: Numérico

OS4817

RN\_66\-06

__Regra para o campo Montante de Cartão de Débito__

Este campo deve ser preenchido  com o valor total das operações realizadas no período, referente a Cartão de Débito\. 

Deve ser o somatório dos campos “Valor da Operação” dos registros Tipo 65, desde que,  o campo “Natureza da Operação” dos registros tipo 65, esteja informado com o valor __“2”__\.

Tamanho do campo: 18 posições \(com 2 decimais\)

Tipo: Numérico

OS4817

- __Registro Tipo 90 – Totalização do Arquivo__

RN\_90\-00

- __Origem das informações__: Registros Tipo65 e Tipo 66\.
- __Regra de seleção__: As informações que serão informadas para a composição do registro tipo __90__, são os totais de registros incluídos no arquivo\. O campo “CNPJ/MF” que está no registro, é referente a empresa que foi selecionada no campo “Estabelecimento/Administradora”, da tela de “Identificação da administradora”, localizada no menu “Parâmetros” do módulo  Portaria CAT87/06 – Protocolo ECF 04\-01\.
- __Campos\-Chave__: 
- __Nível hierárquico do registro__: pai
- __Ordenação__: não se aplica\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: Um por arquivo\.

OS4817

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


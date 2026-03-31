# MTZ-eGoverno-Geracao_Meio_Magnetico-sit_especial

- **Fonte:** MTZ-eGoverno-Geracao_Meio_Magnetico-sit_especial.docx
- **Modificado:** 2026-01-23
- **Tamanho:** 35 KB

---

#  EGoverno \- Geração do meio magnético p/ estabelecimentos fora do município em questão 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3627

Geração do Meio Magnético EGoverno

Este documento tem como objetivo criar o novo módulo que permita a geração do meio magnético de EGoverno que irá conter as informações de serviços prestados e tomados\.

MFS\-917253

Rafael Fabiano

Inclusão do parâmetro ‘Quebrar Arquivo por Data de Emissão’ na tela de geração\.

MFS\-988401

Rosemeire Santos

Alteração da geração do arquivo para desconsiderar as notas fiscais de prestadores de dentro do município para notas fiscais eletrônicas\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Regra p/ Tela de Geração do Meio Magnético

A tela deve ser do tipo framework, contendo todas as funcionalidades padrão\.

__OS3627__

__RN01__

__Regra p/ Tela de Geração do Meio Magnético – Campos Data Inicial e Data Final__

Deverá ser um textbox, onde serão informadas a data inicial e final para a geração\. Formato DD/MM/AAAA\.

__OS3627__

__RN02__

__Regra p/ Tela de Geração do Meio Magnético – Campo Estabelecimento __

Esse campo deverá exibir somente os estabelecimentos que não pertencem ao município de EGoverno e que estejam devidamente licenciados e cadastrados no menu: MasterSAF DW – Manutenção – Cadastros – Inscrições Municipais com uma ou mais inscrições municipais eventuais válidas para o município de EGoverno\.

__OS3627__

<a id="_Hlk216012322"></a>__RN03__

__Regra p/ Geração do Meio Magnético__

__\[MFS988401\] __Tratamento das notas fiscais eletrônicas

Recuperar as notas fiscais com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou \(cód\_class\_doc\_fis = ‘9’ e tipo do documento = “RPA”\)
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Notas não canceladas \(situacao <> ‘S’\)
- Apenas notas que foram retidas pelo tomador, de acordo com a regra abaixo:

 \- Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se

o local da prestação do serviço = município do módulo selecionado OU 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

- Para considerar notas fiscais eletrônicas verificar:
- Se o parâmetro “Desconsiderar Notas Fiscais Eletrônicas de Entrada”\*\* estiver marcado
- Se o município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for __DIFERENTE__ do município do da inscrição eventual \(x156\) selecionado para geração, recuperar os documentos com uma das situações abaixo:
- Modelo do Documento \(campo COD\_MODELO da tabela DWT\_DOCTO\_FISCAL = ‘55’ ou 70\) __OU__
- Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal\.

 

__OS3627__

__MFS\-988401__

O arquivo deve conter apenas os registros de entradas\. \(Vide MTZ \- eGoverno \- Geracao do Meio Magnetico\.doc\)

Obs: O arquivo deve conter apenas notas cujo código do município ISS da capa da nota fiscal esta preenchido com o município referente a EGoverno\.

Os itens de serviço serão consolidados pelos campos do layout:

\- Aliquota da tag <nota\_retencao>

\- Atividade\_desenvolvida da tag <nota\_retencao>

\- numero\_serviço da tag  <nota\_retencao>  

\*\* “Parâmetro “Desconsiderar Notas Fiscais Eletrônicas de Entrada” \- Menu: Parâmetros por Município > Parâmetros > Notas Fiscais Eletrônicas\.

__RN04__

__Regra do parâmetro  ‘Quebrar Arquivo por Data de Emissão’__

Este parâmetro deve ser inserido após o parâmetro ‘Data Final’ e será um check\-box\. Esse campo terá as seguintes opções “S” ou “N”\. Por default, o campo deve ser exibido desmarcado \(“N”\)\.

Quando o parâmetro __“Quebrar Arquivo por Data de Emissão”__ estiver marcado, deve ser realizada a seguinte verificação: 

- Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. 
- Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\_MMAAAA\.XML__, onde:

__       \.XML__: extensão do arquivo\.

       __DDMMAAAA__: representa a data inicial da geração\.   

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       ST__: representa o arquivo é de serviço tomado\.

Ex:136180\_T\_EGOVERNO\_01072025\.XML

Neste caso o arquivo normal também deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__MFS\-917253__


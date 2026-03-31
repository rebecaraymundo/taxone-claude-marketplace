# MTZ-AtendeNet-Geracao_meio_magnetico-sit_especial

- **Fonte:** MTZ-AtendeNet-Geracao_meio_magnetico-sit_especial.docx
- **Modificado:** 2026-03-06
- **Tamanho:** 34 KB

---

# ATENDE\.NET \- Geração do meio magnético p/ estabelecimentos fora do município em questão 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3926\-I

DW \- MUNICIPAL \- ATENDE\.NET \- Atendimento a constução civil/telecom/utilities

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para os municípios atendidos pelo validador ATENDE\.NET\. 

OS3341\-A1

Geração do Meio Magnético para notas fiscais com número de documento com mais de 12 posições\.

Ajuste para considerar o novo campo NUM\_DOCFIS\_SERV

MFS893154

Andréa Rocha

Inclusão do parâmetro ‘Quebrar Arquivos por Data de Emissão’ na tela de geração\.

MFS915475

Andréa Rocha

Alteração da geração do arquivo para desconsiderar as notas fiscais de prestadores de dentro do município para notas fiscais eletrônicas\.

 

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Regra p/ Tela de Geração do Meio Magnético

A tela deve ser do tipo framework, contendo todas as funcionalidades padrão\.

OS3926\-I

__RN01__

__Regra dos campos Data Inicial e Data Final da tela Obrigações – Meio Magnético:__

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

OS3926\-I

__RN02__

__Regra p/ Tela de Geração do Meio Magnético – Campo Estabelecimento __

Esse campo deverá exibir somente os estabelecimentos que não pertencem ao município em questão do validador  ATENDE\.NET e que estejam devidamente licenciados e cadastrados no menu: MasterSAF DW – Manutenção – Cadastros – Inscrições Municipais com uma ou mais inscrições municipais eventuais válidas para o município em questão\.

OS3926\-I

__	__

__RN03__

__Regra p/ Geração do Meio Magnético__

__\[MFS915475\] __Tratamento das notas fiscais eletrônicas

Recuperar as notas fiscais para a geração do registro de serviços tomados com as seguintes características:

- Notas de entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou Classificação do documento \(cód\_class\_doc\_fis = ‘9’\) e codigo do documento \(cód\_docto = ‘RPA’\)
- Código do Município Msaf referente ao Código do município ISS da capa da nota fiscal \(COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS\) = ao município referente ao município em questão
- Nota não cancelada \(SITUACAO <> S\)
- Data Fiscal dentro do período informado
- Empresa igual a selecionada no manager
- Estabelecimento igual ao selecionado na tela de geração
- Para considerar notas fiscais eletrônicas verificar:
- Se o parâmetro “Desconsiderar Notas Fiscais Eletrônicas de Entrada”\*\* estiver marcado
- Se o município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for __DIFERENTE__ do município do da inscrição eventual \(x156\) selecionado para geração, recuperar os documentos com uma das situações abaixo:
- Modelo do Documento \(campo COD\_MODELO da tabela DWT\_DOCTO\_FISCAL = ‘55’ ou 70\) __OU__
- Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal\.

O arquivo deve conter apenas o registro de serviços tomados com a mesma estrutura do layout\. \(vide MTZ \- ATENDE\.NET \- Geracao do Meio Magnético\.doc\)

Obs: O arquivo deve conter apenas notas cujo código do município ISS da capa da nota fiscal esta preenchido com o município referente ao município em questão\. 

\*\* “Parâmetro “Desconsiderar Notas Fiscais Eletrônicas de Entrada” \-  Menu: Parâmetros por Município > Parâmetros > Notas Fiscais Eletrônicas\.

OS3926\-I

MFS915475

__RN04__

__Regra p/ o campo Número do Documento__

__Tela\-A__ 🡸__  Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

  __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ __ __  

  __E __

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __ 

Então, Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL, __se o campo for menor que 15 posições preencher o restante em brancos até completar 15 caracteres 

Se não, 

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL, se o campo for menor que 15 posições preencher o restante em brancos até completar 15 caracteres

OS3341\-A1

__RN05__

__Regra do parâmetro  ‘Quebrar Arquivos por Data de Emissão’__

Este parâmetro deve ser inserido após o parâmetro ‘Data Final’ e será um check\-box\. Esse campo terá as seguintes opções “S” ou “N”\. Por default, o campo deve ser exibido desmarcado \(“N”\)\.

Quando o parâmetro __“Quebrar Arquivos por Data de Emissão”__ estiver marcado, deve ser realizada a seguinte verificação: 

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

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_012010\.XML

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

MFS893154

 


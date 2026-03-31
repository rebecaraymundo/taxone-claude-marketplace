# MTZ_SIMPLISS_Geracao_Meio_Magnetico_Situacao_Especial

- **Fonte:** MTZ_SIMPLISS_Geracao_Meio_Magnetico_Situacao_Especial.docx
- **Modificado:** 2026-03-11
- **Tamanho:** 66 KB

---

THOMSON REUTERS

SIMPLISS

Geração do meio magnético p/ estabelecimentos fora do município em questão

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

OS3470\-D

\-

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para o validador SIMPLISS\.

MFS906454

Andréa Rocha

Inclusão do parâmetro ‘Quebrar Arquivos por Data de Emissão’ na tela de geração\.

MFS961812

Andréa Rocha

Alteração da geração do arquivo para desconsiderar as notas fiscais de prestadores de dentro do município para notas fiscais eletrônicas\.

MFS\-1015365

Alessandra Navatta

Movido o trecho da regra 68\.b que refere\-se a geração de construção civil para este documento \(RN06\)\. Esta regra foi criada pela MFS\-978069\.

Ajustada a regra \(RN06\), para considerar na comparação do município do módulo com o município do documento fiscal o campo COD\_MUNIC\_MSAF da SAFX2097 que está atrelado ao COD\_MUNIC\_ISS

__MFS\-1048012__

Rosemeire Santos

Este documento tem como objetivo ajustar a regra RN06, para geração de construção civil para o município de Blumenau\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN01

__Regra p/ Tela de Geração do Meio Magnético:__

A tela deve ser do tipo framework, contendo todas as funcionalidades padrão\.

OS3470\-D

RN02

__Regra dos campos Data Inicial e Data Final da tela Obrigações – Meio Magnético:__

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

OS3470\-D

RN03

__Regra p/ Tela de Geração do Meio Magnético – Campo Estabelecimento:__

Esse campo deverá exibir somente os estabelecimentos que não pertencem ao município em questão do validador PRESCON e que estejam devidamente licenciados e cadastrados no menu: *MasterSAF DW – Manutenção – Cadastros – Inscrições Municipais *com uma ou mais inscrições municipais eventuais válidas para o município em* questão*\.

OS3470\-D

RN04

__Regra p/ Geração do Meio Magnético:__

__\[MFS961812\] __Tratamento das notas fiscais eletrônicas

Recuperar as notas fiscais para a geração do registro de serviços tomados com as seguintes características:

- Notas de entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou Classificação do documento \(cód\_class\_doc\_fis = ‘9’\) e codigo do documento \(cód\_docto = ‘RPA’\)
- Código do Município Msaf referente ao Código do município ISS da capa da nota fiscal \(COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS\) = ao município referente ao município em questão
- Nota não cancelada \(SITUACAO <> S\)
- Data Fiscal dentro do período informado
- Estabelecimento igual ao selecionado na tela de geração
- Para considerar notas fiscais eletrônicas verificar:
- Se o parâmetro “Desconsiderar Notas Fiscais Eletrônicas de Entrada”\*\* estiver marcado
- Se o município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for __DIFERENTE__ do município do da inscrição eventual \(x156\) selecionado para geração, recuperar os documentos com uma das situações abaixo:
- Modelo do Documento \(campo COD\_MODELO da tabela DWT\_DOCTO\_FISCAL = ‘55’ ou 70\) __OU__
- Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal\.

O arquivo deve conter apenas o registro de serviços tomados com a mesma estrutura do layout \(vide MTZ\-SIMPLISS\-Geracao\_do\_Meio\_Magnetico\.doc\), e obedecer inclusive a regra de negócio para gravação do arquivo\.

__*Obs\.:*__ O arquivo deve conter apenas notas fiscais cujo código do município ISS da capa da nota fiscal está preenchido com o município referente ao município em questão\.

\*\* “Parâmetro “Desconsiderar Notas Fiscais Eletrônicas de Entrada” \- Menu: Parâmetros por Município > Parâmetros > Notas Fiscais Eletrônicas\.

OS3470\-D

MFS961812

RN05

__Regra do parâmetro  ‘Quebrar Arquivos por Data de Emissão’__

Este parâmetro deve ser inserido após o parâmetro ‘Data Final’ e será um check\-box\. Esse campo terá as seguintes opções “S” ou “N”\. Por default, o campo deve ser exibido desmarcado \(“N”\)\.

Quando o parâmetro __“Quebrar Arquivos por Data de Emissão”__ estiver marcado, deve ser realizada a seguinte verificação: 

- Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. 
- Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ MMAAAA\_MMAAAA\.XML__, onde:

__       \.XML__: extensão do arquivo\.

       __MMAAAA__: representa a data inicial da geração\.   

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       ST__: representa o arquivo é de serviço tomado\.

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\_012010\.XML

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

MFS906454

__RN06__

__Regra p/ o campo Tomador de Serviços – Corpo – Código da Natureza de Operação – Específico para o município de Blumenau e Presidente Prudente\.__

Preencher com:

3, Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”\.

4, Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07”\.

5, Verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “09”\.

6, Verificar se o  campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “11”\.

__\[ALTERAÇÃO MFS\-1015365\] A comparação dos municípios deve ser pelo campo COD\_MUNIC\_MSAF da SAFX2097 e não pelo COD\_MUNIC\_ISS__

__Atenção:__ A regra de verificação das naturezas 1 e 2 para SITUAÇÃO ESPECIAL, geração do arquivo magnético pelo menu “Arquivo de Entradas de Serviços \(Consti\. Civil/Utilities/Telecom\)”, deve preencher da seguinte forma:

2, Verificar se o campo COD\_MUNIC\_MSAF da SAFX2097 \(atrelado ao COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL\) <> ao município em questão \(município do módulo\)

__Ou __

Verificar se o__ __cod\_municipio\_pfj <> cod\_municipio\_estab __E__ ind\_tp\_ret = 2

1, Verificar se o campo COD\_MUNIC\_MSAF da SAFX2097 \(atrelado ao COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL\) = ao município em questão \(município do módulo\)\.

*Observação: *O campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL para esse caso sempre estará preenchido, pois para seleção da situação especial o campo é obrigatório\. 

__\[ALTERAÇÃO MFS\-1048012\] Específica para o município de Blumenau\.__

__Atenção:__ A regra de verificação das naturezas 1 e 2 para SITUAÇÃO ESPECIAL, geração do arquivo magnético pelo menu “Arquivo de Entradas de Serviços \(Consti\. Civil/Utilities/Telecom\)”, deve preencher da seguinte forma:

2, Verificar se o campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL <> ao município em questão\. 

__Ou __

Verificar se o__ __cod\_municipio\_pfj <> cod\_municipio\_estab __E__ ind\_tp\_ret = 2

1, Verificar se o campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL = ao município em questão*\. Se o campo *COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL não estiver preenchido, verificar o município cadastrado no estabelecimento\. 

*Observação: *O campo COD\_MUNIC\_ISS da tabela DWT\_DOCTO\_FISCAL para esse caso sempre estará preenchido, pois para seleção da situação especial o campo é obrigatório\. 

__MFS\-978069__

__MFS\-1015365__

__MFS\-1048012__

	

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN


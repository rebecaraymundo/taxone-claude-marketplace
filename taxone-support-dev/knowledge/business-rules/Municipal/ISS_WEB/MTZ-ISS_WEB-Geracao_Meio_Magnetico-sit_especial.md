# MTZ-ISS_WEB-Geracao_Meio_Magnetico-sit_especial

- **Fonte:** MTZ-ISS_WEB-Geracao_Meio_Magnetico-sit_especial.docx
- **Modificado:** 2026-02-19
- **Tamanho:** 33 KB

---

# ISS WEB \- Geração do meio magnético p/ estabelecimentos fora do município em questão 

__Arquivos de Entradas de Serviços \(Construção Civil / Utilities / Telecom\)__

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3470\-B1

DW \- MUNICIPAL \- ISS WEB \- Inclusão de Municípios e item de menu estabs centralizadores\.

Essa OS tem como objetivo permitir que os usuários desses ramos possam gerar a obrigação municipal a partir de um ou mais estabelecimentos que não são do município do validador ISS WEB, desde que licenciados corretamente para o município da mesma\.

Além disso, essa OS visas incluir novos municípios a serem atendidos pelo validador ISS WEB\.

__CH28697\_2018__

__\(MFS22636\)__

DW \- MUNICIPAL \- MOGI DAS CRUZES – Ajuste na regra de recuperação das Notas Fiscais\.

Essa alteração tem como finalidade não considerar as notas fiscais canceladas para os serviços tomados do município de Mogi das Cruzes\-SP\.

__MFS880247__

Andréa Rocha

Inclusão do parâmetro ‘Quebrar Arquivos por Data de Emissão’ na tela de geração\.

__MFS\-980385__

Rosemeire Santos

Alteração da geração do arquivo para desconsiderar as notas fiscais de prestadores de dentro do município para notas fiscais eletrônicas\.

__MFS\-980385__

Klemer Monteiro

Reescrita da regra para os estabelecimentos a ser desconsiderados se estiver marcado com as opções de entrada diferente da regra de exclusão dentro do município para as notas fiscais eletrônicas\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Regra p/ Tela de Geração do Meio Magnético

A tela deve ser do tipo framework, contendo todas as funcionalidades padrão\.

__As gerações dos registros de entrada devem seguir as regras já estabelecidas para a geração normal\.__

__OS3470\-B1__

__RN01__

__Regra p/ Tela de Geração do Meio Magnético – Campos Data Inicial e Data Final__

Deverá ser um textbox, onde serão informadas as datas iniciais e final para a geração\. Formato DD/MM/AAAA\.

__OS3470\-B1__

__RN02__

__Regra p/ Tela de Geração do Meio Magnético – Campo Estabelecimento __

Esse campo deverá exibir somente os estabelecimentos que não pertencem ao município do validador ISS WEB em questão e que estejam devidamente licenciados e cadastrados no menu: MasterSAF DW – Manutenção – Cadastros – Inscrições Municipais com uma ou mais inscrições municipais eventuais válidas para o município do validador ISS WEB em questão\.

__OS3470\-B1__

__RN03__

__Regra p/ Geração do Meio Magnético__

__\[MFS980385\] __Tratamento das notas fiscais eletrônicas

Recuperar as notas fiscais com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou Classificação do documento \(cód\_class\_doc\_fis = ‘9’\) e codigo do documento \(cód\_docto = ‘RPA’\)
- Código do Município Msaf referente ao Código do município ISS da capa da nota fiscal \(COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS\) = ao município referente a ISS WEB
- Data Fiscal dentro do período informado
- Empresa igual a selecionada no manager
- Estabelecimento igual ao selecionado na tela de geração
- CH28697\_2018 \- Mogi das Cruzes/SP: Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)
- Para desconsiderar notas fiscais eletrônicas verificar:
- Se o parâmetro “Desconsiderar Notas Fiscais Eletrônicas de Entrada – Prestador Dentro do Município” estiver marcado, __ignorar __a nota quando for NF\-e \(Modelo 55/70 ou ind\_inf\_Eletrônica = “S”\), e emitida pelo prestador com UF e município iguais aos da inscrição eventual selecionada \(x156\_cad\_insc\_mun\)\.   


O arquivo deve conter apenas os registros de entradas\.

As gerações dos registros de entrada devem seguir as regras já estabelecidas para a geração normal\.

Obs: O arquivo deve conter apenas notas cujo código do município ISS da capa da nota fiscal esta preenchido com o município referente a ISS WEB em questão\. 

\*\* “Parâmetro “Desconsiderar Notas Fiscais Eletrônicas de Entrada” \-  Menu: Parâmetros por Município > Parâmetros > Notas Fiscais Eletrônicas\.

__OS3470\-B1__

__CH28697\_2018__

__\(MFS22636\)__

__MFS\-980385__

__RN04__

__Regra do parâmetro  ‘Quebrar Arquivos por Data de Emissão’__

Este parâmetro deve ser inserido após o parâmetro ‘Tipo Referência’ e será um check\-box\. Esse campo terá as seguintes opções “S” ou “N”\. Por default, o campo deve ser exibido desmarcado \(“N”\)\.

Quando o parâmetro __“Quebrar Arquivos por Data de Emissão”__ estiver marcado, deve ser realizada a seguinte verificação: 

- Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. 
- Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

Ex: ST\_ISSWEB\_01012010\_122009\.txt

__ST\_ISSWEB\_DDMMAAAA\_MMAAAA\.txt__, onde:

     __ST\_ISSWEB__: representa a obrigação que está sendo gerada\.

     __DDMMAAAA__: data inicial da geração

__     MMAAAA:__ mês da competência referente à nota gerada

    \.__txt__: extensão do arquivo\.

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__Obs\.: Este parâmetro \(Quebrar Arquivos por Data de Emissão\) será válido, apenas para Notas de Serviços Tomados\.__

MFS880247


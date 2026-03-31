# MTZ_ISSWEB_V9_Geracao_Meio_Magnetico_sit_especial

- **Fonte:** MTZ_ISSWEB_V9_Geracao_Meio_Magnetico_sit_especial.docx
- **Modificado:** 2021-07-06
- **Tamanho:** 64 KB

---

THOMSON REUTERS

ISSWeb V9

Geração do meio magnético p/ estabelecimentos fora do município em questão

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-14969

Julyana Perrucini

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para os municípios atendido pelo validador ISSWeb V9\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN01

__Regra p/ Tela de Geração do Meio Magnético:__

A tela deve ser do tipo framework, contendo todas as funcionalidades padrão\.

MFS\-14969

RN02

__Regra dos campos Data Inicial e Data Final da tela Obrigações – Meio Magnético:__

__Data Inicial: __deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Enviar NF por E\-mail__: deve ser exibido através de um CheckBox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

MFS\-14969

RN03

__Regra p/ Tela de Geração do Meio Magnético – Campo Estabelecimento:__

Esse campo deverá exibir somente os estabelecimentos que não pertencem ao município em questão do validador ISSWeb V9 e que estejam devidamente licenciados e cadastrados no menu: *MasterSAF DW – Manutenção – Cadastros – Inscrições Municipais *com uma ou mais inscrições municipais eventuais válidas para o município em* *questão\.

MFS\-14969

RN04

__Regra p/ Geração do Meio Magnético:__

Recuperar as notas fiscais para a geração do registro de serviços tomados com as seguintes características:

- Notas de entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou Classificação do documento \(cód\_class\_doc\_fis = ‘9’\) e codigo do documento \(cód\_docto = ‘RPA’\)
- Código do Município Msaf referente ao Código do município ISS da capa da nota fiscal \(COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS\) = ao município referente ao município em questão
- Nota não cancelada \(SITUACAO <> S\)
- Data Fiscal dentro do período informado
- Estabelecimento igual ao selecionado na tela de geração

Quando a nota não tiver itens não deve ser recuperada\.

O agrupamento das notas fiscais deverá ser realizado pelos campos __CodAtividade, ImpRetido e Aliquota__\.

O arquivo deve conter apenas o registro de serviços tomados com a mesma estrutura do layout\. \(vide MTZ\_ISSWEB\_V9\_Geracao\_Meio\_Magnetico\.docx\)

__*Obs\.:*__ O arquivo deve conter apenas notas cujo código do município ISS da capa da nota fiscal esta preenchido com o município referente ao município em questão\. 

MFS\-14969

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN


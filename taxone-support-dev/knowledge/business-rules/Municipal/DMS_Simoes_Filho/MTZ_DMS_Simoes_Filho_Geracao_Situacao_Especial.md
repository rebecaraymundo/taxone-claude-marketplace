# MTZ_DMS_Simoes_Filho_Geracao_Situacao_Especial

- **Fonte:** MTZ_DMS_Simoes_Filho_Geracao_Situacao_Especial.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 63 KB

---

THOMSON REUTERS

DMS Simões Filho

Geração do meio magnético p/ estabelecimentos fora do município em questão

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-19829

João Henrique

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para o validador DMS Simões Filho\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN01

__Regra p/ Tela de Geração do Meio Magnético:__

A tela deve ser do tipo framework, contendo todas as funcionalidades padrão\.

MFS\-19829

RN02

__Regra dos campos Data Inicial e Data Final da tela Obrigações – Meio Magnético:__

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

MFS\-19829

RN03

__Regra p/ Tela de Geração do Meio Magnético – Campo Estabelecimento:__

Esse campo deverá exibir somente os estabelecimentos que não pertencem ao município em questão do validador DMS Simões Filho e que estejam devidamente licenciados e cadastrados no menu: *MasterSAF DW – Manutenção – Cadastros – Inscrições Municipais *com uma ou mais inscrições municipais eventuais válidas para o município em* questão*\.

MFS\-19829

RN04

__Regra p/ Geração do Meio Magnético:__

Recuperar as notas fiscais para a geração do registro de serviços tomados com as seguintes características:

- Notas de entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou Classificação do documento \(cód\_class\_doc\_fis = ‘9’\) e codigo do documento \(cód\_docto = ‘RPA’\)
- Código do Município Msaf referente ao Código do município ISS da capa da nota fiscal \(COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS\) = ao município referente ao município em questão
- Nota não cancelada \(SITUACAO <> S\)
- Data Fiscal dentro do período informado
- Estabelecimento igual ao selecionado na tela de geração

O arquivo deve conter apenas o registro de serviços tomados com a mesma estrutura do layout \(vide MTZ\_DMS\_Simoes\_Filho\_Geracao\_do\_Meio\_Magnetico\.docx\), e obedecer inclusive a regra de negócio para gravação do arquivo\.

__*Obs\.:*__ O arquivo deve conter apenas notas fiscais cujo código do município ISS da capa da nota fiscal está preenchido com o município referente ao município em questão\.

MFS\-19829

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN


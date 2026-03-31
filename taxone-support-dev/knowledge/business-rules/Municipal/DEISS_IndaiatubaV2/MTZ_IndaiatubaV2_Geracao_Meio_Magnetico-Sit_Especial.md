# MTZ_IndaiatubaV2_Geracao_Meio_Magnetico-Sit_Especial

- **Fonte:** MTZ_IndaiatubaV2_Geracao_Meio_Magnetico-Sit_Especial.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 64 KB

---

THOMSON REUTERS

IndaiatubaV2

Geração do meio magnético p/ estabelecimentos fora do município em questão

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-18414

João Henrique de Araujo

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para o validador IndaiatubaV2\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN01

__Regra p/ Tela de Geração do Meio Magnético:__

A tela deve ser do tipo framework, contendo todas as funcionalidades padrão\.

MFS\-18414

RN02

__Regra dos campos Data Inicial e Data Final da tela Obrigações – Meio Magnético:__

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a><a id="OLE_LINK9"></a>Regime de Lucro Presumido ou Real: deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = desmarcado\)\.

A Data Final não poderá ser __menor__ que a Data Inicial\. Caso o usuário informe, o sistema deverá exibir a mensagem de aviso: “Data Final digitada não pode ser menor que a Data Inicial informada”\.                                  

MFS\-18414

RN03

__Regra p/ Tela de Geração do Meio Magnético – Campo Estabelecimento:__

Esse campo deverá exibir somente os estabelecimentos que não pertencem ao município em questão do validador IndaiatubaV2 e que estejam devidamente licenciados e cadastrados no menu: *MasterSAF DW – Manutenção – Cadastros – Inscrições Municipais *com uma ou mais inscrições municipais eventuais válidas para o município em* questão*\.

MFS\-18414

RN04

__Regra p/ Geração do Meio Magnético:__

Recuperar as notas fiscais para a geração do registro de serviços tomados com as seguintes características:

- Notas de entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou Classificação do documento \(cód\_class\_doc\_fis = ‘9’\) e código do documento \(cód\_docto = ‘RPA’\)
- Código do Município Msaf referente ao Código do município ISS da capa da nota fiscal \(COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS\) = ao município referente ao município em questão
- Nota não cancelada \(SITUACAO <> S\)
- Data Fiscal dentro do período informado
- Estabelecimento igual ao selecionado na tela de geração

O arquivo deve contero registro de serviços Prestados e/ou Tomados com a mesma estrutura do layout\. \(Vide: MTZ\_IndaiatubaV2\_Geracao\_Meio\_Magneticoo\.docx\)\.

__*Obs\.:*__ O arquivo deve conter apenas notas cujo código do município ISS da capa da nota fiscal está preenchido com o município referente ao município em questão\. 

MFS\-18414

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN


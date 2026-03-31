# MTZ_NFSE_CENTI_Geracao_meio_magnetico-sit_especial

- **Fonte:** MTZ_NFSE_CENTI_Geracao_meio_magnetico-sit_especial.docx
- **Modificado:** 2022-02-17
- **Tamanho:** 71 KB

---

THOMSON REUTERS

 NFS\-e \- CENTI \- Geração do Meio Magnético p/ estabelecimentos fora do município em questão

	

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS35958

Andréa Rocha

Este documento tem como objetivo criar o novo módulo que permita a geração do meio magnético CENTI, que irá conter as informações de serviços prestados e de serviços contratados, assim como serviços bancários\.\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

__RN01__

__Regra p/ Tela de Geração do Meio Magnético__

A tela deve ser do tipo framework, contendo todas as funcionalidades padrão__\.__

__MFS35958__

__RN02__

__Regra p/ Tela de Geração do Meio Magnético – Campos Data Inicial e Data Final__

Deverá ser um textbox, onde serão informadas as data inicial e final para a geração\. Formato DD/MM/AAAA\.

__MFS35958__

__RN03__

__Regra p/ Tela de Geração do Meio Magnético – Campo Cód\. de Cidade__

Deverá ser exibido através de um ListBox, contendo as seguintes opções: “IBGE” e “SIAFI”\.

__MFS35958__

__RN04__

__Regra p/ Tela de Geração do Meio Magnético – Campo Tipo de Serviço__

Deverá ser exibido através de um ListBox, contendo as seguintes opções: “Cod\. Serviço Lei 116/2003” e “Cod\. de Atividade CNAE”\.

__MFS35958__

__RN04__

__Regra p/ Tela de Geração do Meio Magnético – Campo Estabelecimento __

Esse campo deverá exibir somente os estabelecimentos que não pertencem ao município do validador CENTI em questão e que estejam devidamente licenciados e cadastrados no menu: MasterSAF DW – Manutenção – Cadastros – Inscrições Municipais com uma ou mais inscrições municipais eventuais válidas para o município do validador CENTI em questão\.

__MFS35958__

__RN05__

__Regra p/ Geração do Meio Magnético__

Recuperar as notas fiscais com as seguintes características:

- Notas de entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou Classificação do documento \(cód\_class\_doc\_fis = ‘9’\) e codigo do documento \(cód\_docto = ‘RPA’\)
- Código do Município Msaf referente ao Código do município ISS da capa da nota fiscal \(COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS\) = ao município referente a CENTI
- Data Fiscal dentro do período informado
- Empresa igual a selecionada no manager
- Estabelecimento igual ao selecionado na tela de geração

O arquivo deve conter apenas os registros de entradas\.

A geração dos registros de entrada devem seguir as regras já estabelecidas para a geração normal\.

Obs: O arquivo deve conter apenas notas cujo código do município ISS da capa da nota fiscal esta preenchido com o município referente a CENTI em questão\. 

__MFS35958__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN


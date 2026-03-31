# MTZ-SIGISS-Geracao_meio_magnetico-sit_especial

- **Fonte:** MTZ-SIGISS-Geracao_meio_magnetico-sit_especial.docx
- **Modificado:** 2026-03-05
- **Tamanho:** 27 KB

---

# SIGISS \- Geração do meio magnético p/ estabelecimentos fora do município em questão 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3474\-B

DW \- MUNICIPAL \- SIGISS \- Incluir Item de menu de geração para estabelecimentos centralizadores \(Construção Civil/Utilities\.\.\.\)

Essa OS tem como objetivo permitir que os usuários desses ramos possam gerar o SIGISS a partir de um ou mais estabelecimentos que não são do município do SIGISS, desde que licenciados corretamente para o município da mesma\.

MFS\-1012100

Rosemeire Santos

Alteração da geração do arquivo para desconsiderar as notas fiscais de prestadores de dentro do município para notas fiscais eletrônicas\.

 

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Regra p/ Tela de Geração do Meio Magnético

A tela deve ser do tipo framework, contendo todas as funcionalidades padrão\.

__OS3474\-B__

__RN01__

__Regra p/ Tela de Geração do Meio Magnético – Campos Data Inicial e Data Final__

Deverá ser um textbox, onde serão informadas as datas iniciais e final para a geração\. Formato DD/MM/AAAA\.

__OS3474\-B__

__RN02__

__Regra p/ Tela de Geração do Meio Magnético – Campo Estabelecimento __

Esse campo deverá exibir somente os estabelecimentos que não pertencem ao município da SIGISS em questão e que estejam devidamente licenciados e cadastrados no menu: MasterSAF DW – Manutenção – Cadastros – Inscrições Municipais com uma ou mais inscrições municipais eventuais válidas para o município da SIGISS em questão\.

__OS3474\-B__

__RN03__

__Regra p/ Geração do Meio Magnético__

__\[MFS1012100\] __Tratamento das notas fiscais eletrônicas

Recuperar as notas fiscais com as seguintes características:

- Notas de entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou Classificação do documento \(cód\_class\_doc\_fis = ‘9’\) e codigo do documento \(cód\_docto = ‘RPA’\)
- Código do Município Msaf referente ao Código do município ISS da capa da nota fiscal \(COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS\) = ao município referente a SIGISS
- Data Fiscal dentro do período informado
- Empresa igual a selecionada no manager
- Estabelecimento igual ao selecionado na tela de geração
- Se o parâmetro “Desconsiderar Notas Fiscais Eletrônicas de Entrada”\*\* estiver marcado

Se o município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for __DIFERENTE__ do município do da inscrição eventual \(x156\) selecionado para geração, recuperar os documentos com uma das situações abaixo:

Modelo do Documento \(campo COD\_MODELO da tabela DWT\_DOCTO\_FISCAL = ‘55’ ou 70\) __OU__

Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal\.

O arquivo deve conter apenas os registros de serviços tomados\.

A geração dos registros de entrada deve seguir as regras já estabelecidas para a geração normal\. \(vide MTZ \- SIGISS \- Geração do Meio Magnetico\.doc\)

Obs: O arquivo deve conter apenas notas cujo código do município ISS da capa da nota fiscal está preenchido com o município referente a SIGISS em questão\. 

\*\* “Parâmetro “Desconsiderar Notas Fiscais Eletrônicas de Entrada” \-  Menu: Parâmetros por Município > Parâmetros > Notas Fiscais Eletrônicas\.

__OS3474\-B__

__MFS\-1012100__


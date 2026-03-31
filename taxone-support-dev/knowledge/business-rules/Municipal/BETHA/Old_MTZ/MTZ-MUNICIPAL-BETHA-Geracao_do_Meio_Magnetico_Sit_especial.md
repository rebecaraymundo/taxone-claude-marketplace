# MTZ-MUNICIPAL-BETHA-Geracao_do_Meio_Magnetico_Sit_especial

- **Fonte:** MTZ-MUNICIPAL-BETHA-Geracao_do_Meio_Magnetico_Sit_especial.docx
- **Modificado:** 2021-08-11
- **Tamanho:** 30 KB

---

# BETHA \- Geração do meio magnético p/ estabelecimentos fora do município em questão  

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3470\-G1

__DW \- MUNICIPAL \- BETHA \- Inclusão de Municípios e Item de menu estabs centralizadores__

Essa OS tem como objetivo permitir que os usuários desses ramos possam gerar a obrigação municipal a partir de um ou mais  estabelecimentos que não são do município do validador BETHA, desde que licenciados corretamente para o município da mesma\.

Além disso, essa OS visa incluir novos municípios a serem atendidos pelo validador BETHA\.

__OS4554__

DW \- MUNICIPAL \- BETHA – Correção do tipo de recuperação de dados para o Campo Código Serviço/CNAE\.

O objetivo desta OS, é realizar os ajustes para o correto preenchimento do campo “i\_cnae/i\_lista\_serviços” do registro Serviços, para os dois tipos de dados permitidos pelo campo, pelo motivo de que alguns municípios exigirem o cód\. Serviço Lei 116/2003 e outros exigirem o cód\. CNAE

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Regra p/ Tela de Geração do Meio Magnético

A tela deve ser do tipo framework, contendo todas as funcionalidades padrão\.

__OS3470\-G1__

__RN01__

__Regra p/ Tela de Geração do Meio Magnético – Campos Data Inicial e Data Final__

Deverá ser um textbox, onde serão informadas as data inicial e final para a geração\. Formato DD/MM/AAAA\.

__OS3470\-G1__

__RN02__

__Regra p/ Tela de Geração do Meio Magnético – Campos Tipo de Serviço__

Deverá ser exibido através de um ListBox, contendo as seguintes opções: “Cod\. Serviço Lei 116/2003” e “Cod\. de Atividade CNAE”\.

__OS4554__

__RN03__

__Regra p/ Tela de Geração do Meio Magnético – Campo Estabelecimento__

Esse campo deverá exibir somente os estabelecimentos que não pertencem ao município do validador BETHA em questão e que estejam devidamente licenciados e cadastrados no menu: MasterSAF DW – Manutenção – Cadastros – Inscrições Municipais com uma ou mais inscrições municipais eventuais válidas para o município do validador BETHA em questão\.

__OS3470\-G1__

__RN04__

__Regra p/ Geração do Meio Magnético__

Recuperar as notas fiscais com as seguintes características:

- Notas de entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou Classificação do documento \(cód\_class\_doc\_fis = ‘9’\) e codigo do documento \(cód\_docto = ‘RPA’\)
- Código do Município Msaf referente ao Código do município ISS da capa da nota fiscal \(COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS\) = ao município referente a BETHA
- Data Fiscal dentro do período informado
- Empresa igual a selecionada no manager
- Estabelecimento igual ao selecionado na tela de geração

O arquivo deve conter apenas os registros de entradas\.

A geração dos registros de entrada devem seguir as regras já estabelecidas para a geração normal\.

Obs: O arquivo deve conter apenas notas cujo código do município ISS da capa da nota fiscal esta preenchido com o município referente a BETHA em questão\.

__OS3470\-G1__


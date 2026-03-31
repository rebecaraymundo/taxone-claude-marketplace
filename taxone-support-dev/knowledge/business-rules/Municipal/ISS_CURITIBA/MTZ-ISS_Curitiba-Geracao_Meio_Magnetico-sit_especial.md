# MTZ-ISS_Curitiba-Geracao_Meio_Magnetico-sit_especial

- **Fonte:** MTZ-ISS_Curitiba-Geracao_Meio_Magnetico-sit_especial.docx
- **Modificado:** 2025-11-17
- **Tamanho:** 33 KB

---

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3926\-D1

DW \- MUNICIPAL \- ISS Curitiba \- Atendimento a constução civil/telecomunicações/utilities

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para os municípios atendidos pelo validador ISS CURITIBA\.      

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Regra p/ Tela de Geração do Meio Magnético

A tela deve ser do tipo framework, contendo todas as funcionalidades padrão\.

OS3926\-D1

<a id="_Hlk410833794"></a>__RN01__

__Regra dos campos Data Inicial e Data Final da tela Obrigações – Meio Magnético:__

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

OS3926\-D1

__RN03__

__Regra do campo Tipo Arquivo da tela Obrigações – Meio Magnético:__

Deverá possuir dois Radio Buttom:

- Normal\. Deve ser exibido marcado como default\.
- Teste\. Deve ser exibido desmarcado como default\.

<a id="OLE_LINK39"></a><a id="OLE_LINK40"></a><a id="OLE_LINK41"></a><a id="OLE_LINK42"></a><a id="OLE_LINK43"></a>OS3926\-D1

__RN04__

__Regra do campo “Quebrar arquivo por Data de Emissão” da tela Obrigações – Geração Meio Magnético:__

O campo__ __deve ser exibido através de um checkbox\. <a id="OLE_LINK32"></a><a id="OLE_LINK33"></a><a id="OLE_LINK34"></a><a id="OLE_LINK35"></a><a id="OLE_LINK36"></a>Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)\.

OS3926\-D1

__RN05__

__Regra p/ Tela de Geração do Meio Magnético – Campo Estabelecimento __

Esse campo deverá exibir somente os estabelecimentos que não pertencem ao município em questão do validador  ISS Curitiba e que estejam devidamente licenciados e cadastrados no menu: MasterSAF DW – Manutenção – Cadastros – Inscrições Municipais com uma ou mais inscrições municipais eventuais válidas para o município em questão\.

OS3926\-D1

__	__

__RN06__

__Regra p/ Geração do Meio Magnético__

Recuperar as notas fiscais para a geração do registro de serviços tomados com as seguintes características:

- Notas de entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) __OU__ campo COD\_CLASS\_DOC\_FIS  da tabela DWT\_DOCTO\_FISCAL = ‘9’’ __E__ campo COD\_DOCTO da tabela DWT\_DOCTO\_FISCAL = ‘RPA’ __OU__ 

campo COD\_CLASS\_DOC\_FIS da tabela DWT\_DOCTO\_FISCAL = ‘9’ __E__ o campo COD\_DOCTO da tabela DWT\_DOCTO\_FISCAL estiver parametrizado na tela Tipo de documento MSaf x Tipo de documento ISS Curitiba = ‘3\. RPA \- Recibo Pagamento Autônomo’\.

- Código do Município Msaf referente ao Código do município ISS da capa da nota fiscal \(COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS\) = ao município referente ao município em questão
- Nota não cancelada \(SITUACAO <> S\)
- Data Fiscal dentro do período informado
- Empresa igual a selecionada no manager
- Estabelecimento igual ao selecionado na tela de geração

O arquivo deve conter apenas o registro de serviços tomados com a mesma estrutura do layout\. \(vide MTZ\-ISS\_Curitiba\-Geracao\_do\_Meio\_Magnetico\.doc\)

Obs: O arquivo deve conter apenas notas cujo código do município ISS da capa da nota fiscal esta preenchido com o município referente ao município em questão\.

OS3926\-D1


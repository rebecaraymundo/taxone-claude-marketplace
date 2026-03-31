# MTZ-Joinville-Geracao_meio_magnetico-sit_especial

- **Fonte:** MTZ-Joinville-Geracao_meio_magnetico-sit_especial.docx
- **Modificado:** 2022-04-14
- **Tamanho:** 35 KB

---

# JOINVILLE \- Geração do meio magnético p/ estabelecimentos fora do município em questão 

__Arquivos de Entradas de Serviços \(Construção Civil / Utilities / Telecom\)__

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3926\-X

DW \- MUNICIPAL \- JOINVILLE \- Atendimento a constução civil/telecomunicações/utilities

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para o município atendido pelo validador JOINVILLE\. 

CH15374\_2015

DW \- MUNICIPAL \- JOINVILLE – Retirada do range da data inicial e final

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Regra p/ Tela de Geração do Meio Magnético

A tela deve ser do tipo framework, contendo todas as funcionalidades padrão\.

__As gerações dos registros de entrada devem seguir as regras já estabelecidas para a geração normal\.__

OS3926\-X

__RN01__

__Regra dos campos Data Inicial e Data Final da tela Obrigações – Meio Magnético:__

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__\[ALTERADA – CH15374\_2015\]__

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

OS3926\-X

CH15374\_2015

__RN02__

__Regra do campo Nº Arquivo da tela Obrigações – Meio Magnético:__

Deve ser exibido através de um textbox onde usuário indicará o número do arquivo que está sendo gerado\. Esse campo deve ter 6 posições\.

OS3926\-X

__RN03__

__Regra p/ Tela de Geração do Meio Magnético – Campo Estabelecimento __

Esse campo deverá exibir somente os estabelecimentos que não pertencem ao município em questão do validador  JOINVILLE e que estejam devidamente licenciados e cadastrados no menu: MasterSAF DW – Manutenção – Cadastros – Inscrições Municipais com uma ou mais inscrições municipais eventuais válidas para o município em questão\.

OS3926\-X

__	__

__RN04__

__Regra p/ Geração do Meio Magnético__

Recuperar as notas fiscais para a geração do registro de serviços tomados com as seguintes características:

- Notas de entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou Classificação do documento \(cód\_class\_doc\_fis = ‘9’\) e codigo do documento \(cód\_docto = ‘RPA’\)
- Código do Município Msaf referente ao Código do município ISS da capa da nota fiscal \(COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS\) = ao município referente ao município em questão
- Nota não cancelada \(SITUACAO <> S\)
- Data Fiscal dentro do período informado
- Empresa igual a selecionada no manager
- Estabelecimento igual ao selecionado na tela de geração

O arquivo deve conter apenas o registro de serviços tomados com a mesma estrutura do layout\. \(vide MTZ \- Joinville \- Geracao do Meio Magnetico\.docx\)

Obs: O arquivo deve conter apenas notas cujo código do município ISS da capa da nota fiscal esta preenchido com o município referente ao município em questão\. 

OS3926\-X


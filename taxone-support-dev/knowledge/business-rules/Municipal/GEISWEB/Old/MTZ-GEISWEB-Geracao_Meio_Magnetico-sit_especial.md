# MTZ-GEISWEB-Geracao_Meio_Magnetico-sit_especial

- **Fonte:** MTZ-GEISWEB-Geracao_Meio_Magnetico-sit_especial.docx
- **Modificado:** 2026-01-30
- **Tamanho:** 36 KB

---

# GEISWEB \- Geração do meio magnético p/ estabelecimentos fora do município em questão 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3926\-N

DW \- MUNICIPAL \- GEISWEB \- Atendimento a constução civil/telecom/utilities

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para os municípios atendidos pelo validador GEISWEB\. 

MFS37837

Andréa Rocha

Alteração da regra de recuperação dos dados para o município de Itatinga

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Regra p/ Tela de Geração do Meio Magnético

A tela deve ser do tipo framework, contendo todas as funcionalidades padrão\.

OS3926\-N

__RN01__

__Regra dos campos Data Inicial e Data Final da tela Obrigações – Meio Magnético:__

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

OS3926\-N

__RN02__

__Regra do flag Gerar Movimento a Partir – Geração Meio Magnético:__

O campo “Gerar Movimento a partir” tem duas opções:

\( x\) Data de Emissão

\(   \) Data do Fato Gerador

O sistema deve permitir que apenas uma das opções seja marcada pelo usuário\. 

Por padrão deve estar marcada a opção ‘Data de Emissão’ e desmarcada a opção ‘Data do Fato gerador’\.

OS3926\-N

__RN03__

__Regra p/ Tela de Geração do Meio Magnético – Campo Estabelecimento __

Esse campo deverá exibir somente os estabelecimentos que não pertencem ao município em questão do validador  GEISWEB e que estejam devidamente licenciados e cadastrados no menu: MasterSAF DW – Manutenção – Cadastros – Inscrições Municipais com uma ou mais inscrições municipais eventuais válidas para o município em questão\.

OS3926\-N

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

__\[MFS37837\] – Para o município de Itatinga:__

- Desconsiderar os itens das notas que não possuírem Valor de Base ISS, deve\-se verificar as 2 bases de ISS \(quando a tributação for igual a 1 – Normal ou 2 – Isento\)\.

O arquivo deve conter apenas o registro de serviços tomados com a mesma estrutura do layout\. \(vide MTZ \- Municipal \- GEISWEB \- Geração Meio Magnetico \- Lote\.doc\)

Obs: O arquivo deve conter apenas notas cujo código do município ISS da capa da nota fiscal esta preenchido com o município referente ao município em questão\. 

OS3926\-N

MFS37837


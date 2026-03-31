# MTZ-SPE-Geracao_meio_magnetico-sit_especial

- **Fonte:** MTZ-SPE-Geracao_meio_magnetico-sit_especial.docx
- **Modificado:** 2026-01-23
- **Tamanho:** 31 KB

---

# SPE \- Geração do meio magnético p/ estabelecimentos fora do município em questão 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3926\-L

DW \- MUNICIPAL \- SPE \- Atendimento a constução civil/telecom/utilities

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para os municípios atendidos pelo validador SPE\. 

MFS942203

Andréa Rocha

Inclusão do parâmetro ‘Quebrar Arquivos por Data de Emissão’ na tela de geração

 

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Regra p/ Tela de Geração do Meio Magnético

A tela deve ser do tipo framework, contendo todas as funcionalidades padrão\.

OS3926\-L

__RN01__

__Regra dos campos Data Inicial e Data Final da tela Obrigações – Meio Magnético:__

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

OS3926\-L

__RN02__

__Regra p/ Tela de Geração do Meio Magnético – Campo Estabelecimento __

Esse campo deverá exibir somente os estabelecimentos que não pertencem ao município em questão do validador  SPE e que estejam devidamente licenciados e cadastrados no menu: MasterSAF DW – Manutenção – Cadastros – Inscrições Municipais com uma ou mais inscrições municipais eventuais válidas para o município em questão\.

OS3926\-L

__	__

__RN03__

__Regra p/ Geração do Meio Magnético__

Recuperar as notas fiscais para a geração do registro de serviços tomados com as seguintes características:

- Notas de entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou Classificação do documento \(cód\_class\_doc\_fis = ‘9’\) e codigo do documento \(cód\_docto = ‘RPA’\) \(não deve ser recuperado RPA\)
- Código do Município Msaf referente ao Código do município ISS da capa da nota fiscal \(COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS\) = ao município referente ao município em questão
- Nota não cancelada \(SITUACAO <> S\)
- Data Fiscal dentro do período informado
- Empresa igual a selecionada no manager
- Estabelecimento igual ao selecionado na tela de geração

O arquivo deve conter apenas o registro de serviços tomados com a mesma estrutura do layout\. \(vide MTZ \- Municipal \- SPE \- Geração do Meio Magnético\.doc\)

Obs: O arquivo deve conter apenas notas cujo código do município ISS da capa da nota fiscal esta preenchido com o município referente ao município em questão\. 

OS3926\-L

__RN04__

__Regra do parâmetro  ‘Quebrar Arquivos por Data de Emissão’__

Este parâmetro deve ser inserido após o parâmetro ‘Data Final’ e será um check\-box\. Esse campo terá as seguintes opções “S” ou “N”\. Por default, o campo deve ser exibido desmarcado \(“N”\)\.

Quando o parâmetro __“Quebrar Arquivos por Data de Emissão”__ estiver marcado, deve ser realizada a seguinte verificação: 

- Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. 
- Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__ST\_ EMPRESA\_ ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\_MMAAAA\.txt__, onde:

     __ST:__ representa o tipo de serviço informado no arquivo\. Nesse caso serviços tomados\.

     __EMPRESA: __Representa o prestador de serviço

     __ESTABELECIMENTO: __Representa o prestador de serviço

__     MUNICIPIO__: representa o município que está sendo gerado\. Deve ser preenchido com o nome do município selecionado no manager\.

__     MMAAAA__: representa a mês inicial da geração

__     MMAAAA__: representa o mês da competência referente à nota gerada

     __\.txt__: extensão do arquivo\.

__Ex:__ ST\_EMPRESA\_ESTABELECIMNTO\_BARRAMANSA\_012010\_122009\.txt

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

MFS942203


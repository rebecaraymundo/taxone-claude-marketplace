# MTZ-Sao_Paulo-Geracao_meio_magnetico-sit_especial

- **Fonte:** MTZ-Sao_Paulo-Geracao_meio_magnetico-sit_especial.docx
- **Modificado:** 2026-03-02
- **Tamanho:** 29 KB

---

# NFTS \- Geração do meio magnético p/ estabelecimentos fora do município em questão 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__OS3926\-S__

DW \- MUNICIPAL \- NFTS \- Atendimento a constução civil/telecomunicações/utilities

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para os municípios atendidos pelo validador NFTS\. 

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Regra p/ Tela de Geração do Meio Magnético

A tela deve ser do tipo framework, contendo todas as funcionalidades padrão\.

OS3926\-S

__RN01__

__Regra dos campos Data Inicial e Data Final da tela Obrigações – Meio Magnético:__

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

OS3926\-S

__RN02__

__Regra dos campos Data Emissão e Data do Fato Gerador – Meio Magnético:__

Considerar no campo data da prestação dos serviços: Essa opção permite que o usuário selecione o campo da SAFX07 para recuperar a informação do campo "05 – Data da prestação dos serviços" no arquivo texto\. As opções de

geração do movimento são:

- *Data de Emissão:* Se esta opção for selecionada, será considerada a data de emissão \(Campo 11 da SAFX07\)\.
- *Data do Fato gerador:* Se esta opção for selecionada, será considerada a data do fato gerador \(Campo 93 daSAFX07\)\.

Obs\.: Somente uma das opções pode ser selecionada\.

OS3926\-S

__RN03__

__Regra dos campos Quebrar Arquivo por Centro de Custo e Gerar Arquivo de Prestadores Novos – Meio Magnético:__

Quebrar Arquivo por Centro de Custo: Se esta opção for selecionada, será gerado o arquivo separado por centro de custo\. Será considerado os dados do Centro de Custo \(Campo 84 da SAFX09\)\.

Gerar Arquivo de Prestadores Novos: Esse flag deve ser marcado para que o sistema gere o arquivo que deve ser composto por todos os prestadores de serviços do segmento de seguradoras, que possuem estabelecimentos fora do município de São Paulo\. Trata – se de um arquivo em formato TXT, de envio mensal, que deve ser importado e validado no site da Prefeitura de São Paulo\.

OS3926\-S

__RN04__

__Regra p/ Tela de Geração do Meio Magnético – Campo Estabelecimento __

Esse campo deverá exibir somente os estabelecimentos que não pertencem ao município em questão do validador  NFTS e que estejam devidamente licenciados e cadastrados no menu: MasterSAF DW – Manutenção – Cadastros – Inscrições Municipais com uma ou mais inscrições municipais eventuais válidas para o município em questão\.

OS3926\-S

__	__

__RN05__

__Regra p/ Geração do Meio Magnético__

Recuperar as notas fiscais para a geração do registro de serviços tomados com as seguintes características:

- Notas de entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou Classificação do documento \(cód\_class\_doc\_fis = ‘9’\) e codigo do documento \(cód\_docto = ‘RPA’\)
- Código do Município Msaf referente ao Código do município ISS da capa da nota fiscal \(COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS\) = ao município referente ao município em questão
- Nota não cancelada \(SITUACAO <> S\)
- Data Fiscal dentro do período informado
- Empresa igual a selecionada no manager
- Estabelecimento igual ao selecionado na tela de geração

O arquivo deve conter apenas o registro de serviços tomados com a mesma estrutura do layout\. \(vide MTZ \- Municipal \- São Paulo \- Geração Meio Magnetico \- Lote NFTS\_SP1\.doc\) 

Obs: O arquivo deve conter apenas notas cujo código do município ISS da capa da nota fiscal esta preenchido com o município referente ao município em questão\. 

OS3926\-S


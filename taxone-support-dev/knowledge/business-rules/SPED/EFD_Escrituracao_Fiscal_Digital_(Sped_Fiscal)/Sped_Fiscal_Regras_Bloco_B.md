# Sped_Fiscal_Regras_Bloco_B

- **Fonte:** Sped_Fiscal_Regras_Bloco_B.docx
- **Modificado:** 2022-11-10
- **Tamanho:** 80 KB

---

Sped Fiscal – Bloco B

Quadro de Revisões

__                                                                          __

__Data__

__OS / Chamado__

__Descrição__

__Responsável__

25/10/2018

MFS\-20989

Atendimento ao Ato COTEPE nº 44/2018

Julyana Perrucini

13/11/2018

MFS\-20992

Atendimento ao Ato COTEPE nº 44/2018

Julyana Perrucini

20/08/2019

MFS29820

Alteração na regra de preenchimento do campo VL\_ISNT\_ISSQN dos registros B020, B025, B030, B035\.

Andréa Rocha

07/11/2019

MFS31873

Alteração na regra de recuperação do registro B020\.

Andréa Rocha

21/11/2019

MFS32212

Alteração na geração do registro B470\.

Andréa Rocha

15/07/2021

MFS69058

Inclusão de tratamento do Campo __COD\_INF\_OBS__\. 

Rogério Ohashi

18/08/2021

MFS70562

Alteração da definição da chave do registro B020, conforme informação do Guia Prático\.

Andréa Rocha

01/11/2021

MFS73700

Inclusão do documento fiscal NF3\-e \(código 66\) e ajustes de seus respectivos campos\.

Aline Melo

21/12/2021

MFS77681

Alteração na regra geral, para tratamento de serviços tomados dos contribuintes do Distrito Federal, para recuperar as Notas Fiscais pelo campo de data do pagamento e retenção do ISS\.

Rogério Ohashi

22/12/2021

MFS77885

Alteração na regra geral, para o Registro B020, a partir do Layout EFD115 \(CAD\_LAYOUT– COD\_VERSAO>=115\) não gerar as Notas Fiscais Denegadas e Inutilizadas de Saídas\. Conforme ajuste Sinief nº 038 DOU de 08/10/2021 que altera o Ajuste Sinief nº 7/05\.

Rogério Ohashi

10/11/2022

MFS95924

Alteração na geração do Bloco B, devido a desobrigação da entrega do mesmo com a implantação do novo Sistema de Gerenciamento do Imposto sobre Serviços – ISS, a partir de 01/01/2023 para os contribuintes do DF\.

Aline Melo

#### Bloco B – Escrituração e Apuração do ISS 

__Registro B001 – Abertura do Bloco B__

RNB001

Um registro por arquivo\.

__Registro B020 – Nota Fiscal \(Código 01\), Nota Fiscal de Serviços \(Código 03\), Nota Fiscal de Serviços Avulsa \(Código 3B\), Nota Fiscal de Produtor \(Código 04\), Conhecimento de Transporte Rodoviário de Cargas \(Código 08\), NF\-e \(Código 55\), NFC\-e \(Código 65\) e NF3e \(Código 66\)__

RNB020

<a id="_Hlk118979789"></a>__\[MFS95924\] Dispensa dos registros Bloco B__

__Devido a implantação do novo Sistema de Gerenciamento do Imposto sobre Serviços – ISS, pela Secretaria de Fazenda do Distrito Federal, para fatos geradores ocorridos a partir de 01/01/2023, não haverá a escrituração de prestações no Bloco B da EFD \- ICMS/ISS/IPI \- SPED, referente ao Imposto Sobre Serviços \- ISS \(o Bloco B deverá apenas ser aberto e encerrado, sem informação de valores\)\.__

Para o período a partir de __01/01/2023__ e UF do Estabelecimento = “__DF__”:

A geração deste registro passa a ser __NÃO OBRIGATÓRIO__\.

A escolha em informar o registro, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro B020 será gerado ou não\.

Para período de geração anterior a __01/01/2023__, o registro __DEVE__ ser gerado conforme as regras já existentes:

Neste registro devem ser gravadas as notas fiscais dos modelos que correspondem aos seguintes códigos da tabela “4\.1\.3\- Tabela Documentos Fiscais do ISS” do Ato COTEPE 44:

01 – Nota Fiscal                                                                          à Modelo 1/ 1A

03 – Nota Fiscal de Serviços                                                      à Modelo 3

3B – Nota Fiscal de Serviços \- Modelo Avulso                           à Modelo 3\-B

04 – Nota Fiscal de Produtor                                                      à Modelo 4

08 – Conhecimento de Transporte Rodoviário de Cargas          à Modelo 8

55 – Nota Fiscal Eletrônica                                                         à Modelo 55

65 – Nota Fiscal de Consumidor Eletrônica\- NFC\-e                   à Modelo 65

66 \- Nota Fiscal de Energia Elétrica Eletrônica \- NF3e               à Modelo 66__\*__

__\*\[MFS73700\] Inclusão do novo modelo “66”, válido a partir do layout 1\.15 \(Janeiro/2022\)\.__

             

__Recuperação dos Dados__

__Geração a partir das notas da SAFX07/SAFX09__:

Este processo será realizado apenas para os itens de documento fiscal de serviço que atendam aos seguintes critérios:

- Empresa igual a empresa selecionada na geração;
- Estabelecimento igual ao estabelecimento selecionado na geração;

__\[MFS77681\]__

- Se a UF do Estabelecimento = “DF” e a nota for de entrada \(serviços tomados campo 03\-MOVTO\_E\_S <> ‘9’ da tabela SAFX07\), considerar:

A data do pagamento \(campo 175\-DT\_PAGTO\_NF da tabela SAFX07\) deve ser preenchida e referente ao período informado em tela \(>= data inicial e <= data final\) __E__

Indicador Tipo Retenção = “RETIDO PELO TOMADOR” \(campo 141\-IND\_TP\_RET = ‘1’ da tabela SAFX07\)

Se as condições de Data de Pagamento e Tipo de Retenção acima não forem atendidas, as notas não devem ser consideradas no registro\.

- Senão, considerar:
- A data fiscal da nota deve ser referente ao período informado em tela \(>= data inicial e <= data final\);
- Classificação fiscal 2 e 3 \(nota fiscal de serviço e nota fiscal mista campo 12\-COD\_CLASS\_DOC\_FIS = 2, 3 da tabela SAFX07\);
- Modelo 01, 03, 3B, 04, 08, 55, 65 e 66 \(campo 13\-COD\_MODELO = 01, 03, 3B, 04, 08, 55, 66 da tabela SAFX07\);
- Modelo 65 \(campo 13\-COD\_MODELO = 65 da tabela SAFX07\) deverá ser considerado apenas nas saídas, ou seja, será apresentada apenas as prestações de serviço \(campo 03\-MOVTO\_E\_S = 9\);
- Modelo 66 \(campo 13\-COD\_MODELO = 66 da tabela SAFX07\) deve ser considerado a partir do layout versão 1\.15 \(Janeiro/2022\) __\[MFS73700\]__
- Desconsiderar itens das notas ficais cujo serviço foi realizado por intermediário e não tenha incidência do ISS ou Isenção \(campo 39\-BASE\_ISS da tabela SAFX09 quando campo 38\-TRIB\_ISS da tabela SAFX09 = 3\); __\[MFS31873\]__
- Não considerar notas fiscais de serviço sem itens;
- Na geração por Inscrição Estadual Única, devem ser considerados os documentos fiscais de todos os Estabelecimentos envolvidos na centralização\.

__Para Geração c/ leiaute anterior a EFD115 \(CAD\_LAYOUT – COD\_VERSAO<115\):__ 

__Geração a partir das notas da SAFX130__:

Recuperar todas as notas da SAFX130 conforme os seguintes critérios:

- Empresa igual a empresa selecionada na geração;
- Estabelecimento igual ao estabelecimento selecionado na geração;
- A data de referência deve ser referente ao período informado em tela \(>= data inicial e <= data final\);
- Modelo 55 \(campo 09\-COD\_MODELO = 55 da tabela SAFX130\);
- Modelo 65 \(campo 13\-COD\_MODELO = 65 da tabela SAFX07\) deverá ser considerado apenas nas saídas, ou seja, será apresentada apenas as prestações de serviço \(campo 03\-MOVTO\_E\_S = 9\);

Para cada linha recuperada da SAFX130, gerar os dados no B020 da seguinte forma:

Se Número Documento Final *não preenchido*:

Gravar *um único* B020, com os dados:

REG           

B020

IND\_OPER

Se MOVTO\_E\_S = 2, 3, 4 ou 5, gravar “0”, senão gravar “1”

IND\_EMIT   

0 \(emissão própria\)

COD\_MOD

Campo 09\-COD\_MODELO

COD\_SIT    

Se situação da nota denegada \(1\) gravar 04, se inutilizada \(2\), gravar 05

SER

Gravar o conteúdo da série, campo 06\-SERIE\_DOCFIS apenas quando seu conteúdo for <> branco, caso contrário, deixar o campo sem preenchimento \(gravar ||\)

NUM\_DOC

Campo 04\-NUM\_DOCFIS\_INI

Se Número Documento Final *preenchido*:

Gravar vários registros B020, desde o número do documento inicial até o número do documento final\. Ou seja, gravar um registro B020 para cada número contido na sequência do número inicial até o número final\. Os dados devem ser gravados com as mesmas informações descritas acima, diferenciados apenas pelo número do documento\.

*Observação:* Estas notas gravadas no B020 a partir da tabela SAFX130, não terão os registros filhos, e apenas alguns campos são preenchidos, da mesma forma que é feito para as notas denegadas e inutilizadas da tabela SAFX07 \(ver item importante dessa RN\)\.

__Para Geração c/ leiaute a partir da EFD115 \(CAD\_LAYOUT – COD\_VERSAO>=115\):__

As notas gravadas no B020 a partir da tabela SAFX130 \(notas denegadas ou inutilizadas\) não devem ser consideradas no arquivo meio magnético, a partir do layout versão 1\.15 \(Janeiro/2022\)__ \[MFS73700\]__

__\[MFS77885\] __Tratamento p/ Notas Fiscais Denegadas e Inutilizadas com Origem da SAFX07

__Se__ o Campo 231 \- IND\_NFE\_DENEG\_INUT da tabela SAFX07 for igual à ‘1’ ou ‘2’;

   __Não preencher__ o Registro B020, Notas Fiscais denegadas ou inutilizadas __não devem ser consideradas__ no arquivo meio magnético, a partir do layout versão 1\.15 \(Janeiro/2022\)

1 \- Nota Fiscal Eletrônica denegada;

2 \- Nota Fiscal Eletrônica inutilizada\.

__Processamento__

__\[MFS70562\] __Inclusão do cam po COD\_PART na chave do registro B020

__Gravação a partir das notas da SAFX07/SAFX09__:

Não podem ser informados, em um mesmo arquivo, dois ou mais registros B020 com a mesma combinação de valores dos campos formadores da chave do registro\. A chave do registro B020 é: IND\_OPER, COD\_PART, COD\_MOD, SER, NUM\_DOC e DT\_DOC\. Então os itens das notas fiscais deverão ser agrupados por esses campos de acordo com a recuperação: 03\-MOVTO\_E\_S, 6\-IDENT\_FIS\_JUR \+ 7\-COD\_FIS\_JUR, 13\-COD\_MODELO, 09\-SERIE\_DOCFIS, 08\-NUM\_DOCFIS e 11\-DATA\_EMISSAO da tabela SAFX07\.

__Tratamento:__

- Como o campo Indicador do Tipo de Operação é um indicador único para aquisição \(notas fiscais de entrada\), então é necessário tratar para agrupar as entradas para cada participante \(ver layout da EFD ICMS/IPI\), ou seja, todas as entradas que serão recuperadas precisam ter um indicador único\.

__Gravação a partir das notas da SAFX130__:

Não podem ser informados, em um mesmo arquivo, dois ou mais registros B020 com a mesma combinação de valores dos campos formadores da chave do registro\. A chave do registro B020 é: IND\_OPER, COD\_PART, COD\_MOD, SER, NUM\_DOC e DT\_DOC\. Então os itens das notas fiscais deverão ser agrupados por esses campos de acordo com a recuperação: 03\-MOVTO\_E\_S, 6\-IDENT\_FIS\_JUR \+ 7\-COD\_FIS\_JUR, 09\-COD\_MODELO, 06\-SERIE\_DOCFIS, 04\-NUM\_DOCFIS e 08\-DATA\_REF da tabela SAFX130\.

__Tratamento:__

- Como o campo Indicador do Tipo de Operação é um indicador único para aquisição \(notas fiscais de entrada\), então é necessário tratar para agrupar as entradas para cada participante \(ver layout da EFD ICMS/IPI\), ou seja, todas as entradas que serão recuperadas precisam ter um indicador único\.

__*Importante:*__ Para documentos com código de situação \(campo COD\_SIT\) cancelado \(código “02”\), Nota Fiscal Eletrônica \(NF\-e\) denegada \(código “04”\), preencher somente os campos REG, IND\_OPER, IND\_EMIT, COD\_MOD, COD\_SIT, SER, NUM\_DOC e CHV\_NFE\. Para COD\_SIT = 05 \(numeração inutilizada\), todos os campos referidos anteriormente devem ser preenchidos, exceto o campo CHV\_NFE\. Demais campos deverão ser apresentados com conteúdo VAZIO “||”\. Não informar registros filhos\.

RNB020\-02

Campo IND\_OPER:

A partir do conteúdo do indicador de Entrada/Saída da nota \(campo 03\-MOVTO\_E\_S da tabela SAFX07\), verificar:

Se indicador de movimento E/S = 9 à gravar 1 \(Prestação \- Saída\)

Se indicador de movimento E/S <> 9 à gravar 0 \(Aquisição \- Entrada\)

RNB020\-03

Campo IND\_EMIT:

A partir do conteúdo do indicador de Entrada/Saída da nota \(campo 03\-MOVTO\_E\_S da tabela SAFX07\), verificar:

Se indicador de movimento E/S = 1 à gravar 1 \(emissão terceiros\)

Se indicador de movimento E/S = 2,3,4,5,9 à gravar 0 \(emissão própria\)

RNB020\-04

Campo <a id="_Hlk86675708"></a>COD\_PART:

__\[MFS73700\] Inclusão do novo modelo “66” válido a partir do layout 1\.15 \(Janeiro/2022\)\.__ 

__Para Geração c/ leiaute anterior a EFD115 \(CAD\_LAYOUT – COD\_VERSAO<115\):__ 

Quando o Modelo do Documento for igual a “65” \(NFe para Consumidor Final\), campo 13\-COD\_MODELO = 65 da tabela SAFX07, este campo não deve ser preenchido\.

Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais do módulo EFD estiver selecionado, este campo será gerado com o Código de identificação da pessoa FIS/JUR \(SAFX04\), concatenando o Indicador \(campo 02\-IND\_FIS\_JUR\) com o Código da PFJ \(campo 02\-COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais do módulo EFD NÃO estiver selecionado, este campo será gerado apenas com o Código da PFJ \(02\-COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

__Para Geração c/ leiaute a partir da EFD115 \(CAD\_LAYOUT – COD\_VERSAO>=115\), considerar regra já existente e o novo tratamento abaixo: __

Quando o modelo do documento for igual a “66” \(Nota Fiscal de Energia Elétrica Eletrônica\), campo 13\- COD\_MODELO = 66 da tabela SAFX07, o preenchimento do campo deve ser obrigatório nas seguintes situações:

__SE__ o documento fiscal for de aquisição de serviços \(campo 03\-MOVTO\_E\_S da tabela SAFX07 = ”0”\) 

__E/OU__ 

__SE__ houver retenção de ISS pelo tomador \(campo 57\- VLR\_BASE\_ISS\_RETIDO da tabela SAFX09 > “0”\)\.

RNB020\-06

Campo COD\_SIT:

Para o preenchimento deste campo deverão ser verificados alguns campos da SAFX07, conforme segue:

Se for nota eletrônica, verificar:

     se a nota foi denegada      à gravar “04”

     se a nota foi ou inutilizada à gravar “05”

Se for nota cancelada, verificar:

      se a nota é normal \(não se aplica NF extemporânea\) à gravar “02”

Se for nota complementar:

      gravar “06”

Se nota tem Ato Normativo, Regime Especial etc

      gravar “08”

Se a nota não atende a nenhuma das opções anteriores:

      gravar “00”

__Importante:__ 

- Os testes devem ser executados exatamente nesta prioridade\. Assim, o teste deve ser encerrado na primeira regra atendida pela nota, e sempre que isto *não ocorrer*, será gravado o conteúdo “00”;
- Diferentemente das notas fiscais de mercadoria, nesse caso, não existe situação extemporânea e nem compra e venda para entrega futura\.

A lógica seria a seguinte:

__Se__ nota é eletrônica ou nota eletrônica para consumidor final e foi \(denegada ou inutilizada\)

        __Se__ nota é denegada

              gravar “04”

        __Senão__* \(é inutilizada\)*

              gravar “05”

# __Senão__

        __Se__ nota é cancelada

                   gravar “02”

              __Senão__

                    __Se__ nota é complementar

                         gravar “06”

                    __Senão__

                         __Se__ nota tem Ato Normativo, Regime Especial etc

                              gravar “08”

                         __Senão__

                             gravar “00”;

__Campos da SAFX07 para verificação das regras:__

__\[MFS73700\] Inclusão do novo modelo “66” válido a partir do layout 1\.15 \(Janeiro/2022\)\.__ 

__Para Geração c/ leiaute anterior a EFD115 \(CAD\_LAYOUT – COD\_VERSAO<115\):__ 

Nota cancelada à o campo 30\-SITUACAO = “S”;

Nota complementar à o campo 125\-IND\_SITUACAO\_ESP será = “5”;

Nota Eletrônica ou nota eletrônica para consumidor final à o campo 13\-COD\_MODELO = 55 ou 65, respectivamente;

Nota Eletrônica denegada ou nota eletrônica para consumidor final denegada à  o campo 13\-COD\_MODELO = 55 ou 65, respectivamente, e o campo 231\-IND\_NFE\_DENEG\_INUT = 1 \(denegada\);

Nota Eletrônica inutilizada ou nota eletrônica para consumidor final inutilizada à o campo “13\-Modelo de Documento” será = “55” ou “65”, respectivamente, e o campo 231\-IND\_NFE\_DENEG\_INUT = 2 \(inutilizada\);

Nota com Ato Normativo, Regime Especial etc à o campo 232\-IND\_NF\_REG\_ESPECIAL = S\.

__Para Geração c/ leiaute a partir da EFD115 \(CAD\_LAYOUT – COD\_VERSAO>=115\), considerar o tratamento abaixo:__

__*Obs\.: tratam\-se das regras acima, excluíndo a tratativa para a*__*s *__*notas denegadas e inutilizadas e inclusão do novo modelo 66\.*__

Nota cancelada à o campo 30\-SITUACAO = “S”;

Nota complementar à o campo 125\-IND\_SITUACAO\_ESP  = “5” __E__ campo 13\-COD\_MODELO = 55 ou 65 \(Conforme consta no Guia Prático, documento modelo “66” não pode ser declarada como nota complementar\)

Nota Eletrônica ou nota eletrônica para consumidor final à o campo 13\-COD\_MODELO = 55 ou 65, respectivamente;

Nota Fiscal de Energia Elétrica Eletrônica – NF3\-e > o campo 13\-COD\_MODELO = 66\.

Nota com Ato Normativo, Regime Especial etc à o campo 232\-IND\_NF\_REG\_ESPECIAL = S\.

RNB020\-07

Campo SER:

__\[MFS73700\] Inclusão do novo modelo “66” válido a partir do layout 1\.15 \(Janeiro/2022\)\.__

__Para Geração c/ leiaute anterior a EFD115 \(CAD\_LAYOUT – COD\_VERSAO<115\):__ 

Esse campo é de preenchimento obrigatório com três posições para NF\-e ou NFC\-e, então considerar na geração:

Se o documento fiscal for de emissão própria ou de terceiros campo 03\-IND\_EMIT igual a “0” ou “1” \(origem campo 03\-MOVTO\_E\_S da tabela SAFX07 ver RNB020\-03\) e o campo 05\-COD\_MOD for igual a “55” \(origem campo 13\-COD\_MODELO/09\-COD\_MODELO da tabela SAFX07/SAFX130 = 55\), considerar as três posições do campo 09\-SERIE\_DOCFIS/06\-SERIE\_DOCFIS da tabela SAFX07, mas caso seja menor do que o esperado preencher com zeros à esquerda e ainda se não estiver preenchida preencher com zeros \(000\)\.

Se o documento fiscal for de emissão própria campo 03\-IND\_EMIT igual a “0” \(origem campo 03\-MOVTO\_E\_S da tabela SAFX07 ver RNB020\-03\) e o campo 05\-COD\_MOD for igual a “65” \(origem campo 13\-COD\_MODELO/09\-COD\_MODELO da tabela SAFX07/SAFX130 = 65\), considerar as três posições do campo 09\-SERIE\_DOCFIS/06\-SERIE\_DOCFIS da tabela SAFX07, mas caso seja menor do que o esperado preencher com zeros à esquerda e ainda se não estiver preenchida preencher com zeros \(000\)\.

__Para Geração c/ leiaute a partir da EFD115 \(CAD\_LAYOUT – COD\_VERSAO>=115\), considerar regra já existente e o novo tratamento abaixo: __

Se o documento fiscal for de emissão própria ou de terceiros campo 03\-IND\_EMIT igual a “0” ou “1” \(origem campo 03\-MOVTO\_E\_S da tabela SAFX07 ver RNB020\-03\) e o campo 05\-COD\_MOD for igual a “66” \(origem campo 13\-COD\_MODELO da tabela SAFX07 = 66\), considerar as três posições do campo 09\-SERIE\_DOCFIS/06\-SERIE\_DOCFIS da tabela SAFX07, mas caso seja menor do que o esperado preencher com zeros à esquerda e ainda se não estiver preenchida preencher com zeros \(000\)\.

RNB020\-09

<a id="_Hlk86679133"></a>Campo CHV\_NFE:

__\[MFS73700\] Inclusão do novo modelo “66” válido a partir do layout 1\.15 \(Janeiro/2022\)\.__

O campo será preenchido apenas nas notas eletrônicas ou nas notas eletrônicas para consumidor final \(notas com o campo 13\-COD\_MODELO/09\-COD\_MODELO da tabela SAFX07/SAFX130 = 55, 65 ou 66\)\. 

Modelo 66 \(campo 13\-COD\_MODELO = 66 da tabela SAFX07\) deve ser considerado a partir do layout versão 1\.15 \(Janeiro/2022\) __\[MFS73700\]__

O preenchimento do campo depende se a nota é de emissão própria ou não \(campo 03\-MOVTO\_E\_S\), como segue:

Se __emissão própria__ \(03\-MOVTO\_E\_S = 2,3,4,5 ou 9\) 

       Se campo 226/12\-NUM\_AUTENTIC\_NFE <> nulo

             Preencher o campo com o conteúdo da chave \(utilizar as primeiras 44 posições,

             seguindo o formato da NF\-e nacional\) 

       Senão

            O campo será gravado sem informação, e no log será gravada mensagem de

            erro, conforme padrão do Sped Fiscal: 

            *“O campo CHV\_NFE  é de preenchimento obrigatório, e não foi informado”*

             \(mensagem de número 32 da planilha de erros Sped\_Fiscal\_Log\_Erros\)

Senão __emissão de terceiros __\(03\-MOVTO\_E\_S = 1\)

             Se campo 226/12\-NUM\_AUTENTIC\_NFE <> nulo

                  Preencher o campo com o conteúdo da chave \(utilizar as primeiras 44 posições,

                  seguindo o formato da NF\-e nacional\) 

                    Senão

            O campo será gravado sem informação, e no log será gravada mensagem de

            erro, conforme padrão do Sped Fiscal: 

            *“O campo CHV\_NFE  é de preenchimento obrigatório, e não foi informado”*

             \(mensagem de número 32 da planilha de erros Sped\_Fiscal\_Log\_Erros\)

Esse campo é de preenchimento obrigatório para NF\-e, campo 13\-COD\_MODELO/09\-COD\_MODELO da SAFX07/SAFX130 = 55, no caso de emissão própria ou de terceiros\.

Esse campo é de preenchimento obrigatório para NF\-e, campo 13\-COD\_MODELO/09\-COD\_MODELO da SAFX07/SAFX130 = 65, no caso de emissão própria\.

Esse campo é de preenchimento obrigatório para NF3\-e, campo 13\-COD\_MODELO/09\-COD\_MODELO da SAFX07/SAFX130 = 66, no caso de emissão própria ou de terceiros, a partir do layout versão 1\.15 \(Janeiro/2022\) __\[MFS73700\]__

A regra não se aplica para NF\-e ou NFC\-e com numeração inutilizada \(COD\_SIT = 05\)\.

RNB020\-11

Campo COD\_MUN\_SERV:

Esse campo deverá ser preenchido com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo 73\-COD\_MUNICIPIO da tabela SAFX07\.

*Observação:* O município precisa ser devidamente cadastrado na Tabela de Município \(SAFX2097\)\.

RNB020\-15

Campo VL\_ISNT\_ISS:

\[ALTERADA – MFS29820\]

Se o campo Tributação ISS \(campo 38 da SAFX09\) for igual a ‘2’

      Preencher com a Base ISS \(campo 39 da SAFX09\)

Senão

      Preencher com o Valor do Desconto \(campo 21 da SAFX09\)\.

RNB020\-17

Campo VL\_BC\_ISS:

Esse campo deverá ser preenchido com a informação do campo 39\-BASE\_ISS da tabela SAFX09 quando campo 38\-TRIB\_ISS da tabela SAFX09 = 1\.

RNB020\-19

Campo VL\_ISS\_RT:

Se o campo 13\-COD\_MODELO = “65”, o valor informado deve ser igual a zero\.

RNB020\-21

__Campo: COD\_INF\_OBS__

\[__ALTERAÇÃO \- MFS69058__\] Tratamento para considerar o parâmetro – “Campo Código de Observação \(Considerar 6 caracteres\)” \- para truncar o campo com 6 posições, conforme Manual Guia Prático\.

__SE__ o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

__OU__

__SE__ o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

Este código deverá ser referenciado no registro 0460\.

__Registro B025 – Detalhamento por Combinação de Alíquota e Item da Lista de Serviços da LC 116/2003__

RNB025

__\[MFS95924\] Dispensa dos registros Bloco B__

__Devido a implantação do novo Sistema de Gerenciamento do Imposto sobre Serviços – ISS, pela Secretaria de Fazenda do Distrito Federal, para fatos geradores ocorridos a partir de 01/01/2023, não haverá a escrituração de prestações no Bloco B da EFD \- ICMS/ISS/IPI \- SPED, referente ao Imposto Sobre Serviços \- ISS \(o Bloco B deverá apenas ser aberto e encerrado, sem informação de valores\)\.__

Para o período a partir de __01/01/2023__ e UF do Estabelecimento = “__DF__”:

A geração deste registro passa a ser __NÃO OBRIGATÓRIO__\.

A escolha em informar o registro, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro B025 será gerado ou não\.

Para período de geração anterior a __01/01/2023__, o registro __DEVE__ ser gerado conforme as regras já existentes:

Neste registro devem ser gravadas as notas fiscais dos modelos que correspondem aos seguintes códigos da tabela “4\.1\.3\- Tabela Documentos Fiscais do ISS” do Ato COTEPE 44:

01 – Nota Fiscal                                                                          à Modelo 1/ 1A

03 – Nota Fiscal de Serviços                                                      à Modelo 3

3B – Nota Fiscal de Serviços \- Modelo Avulso                           à Modelo 3\-B

04 – Nota Fiscal de Produtor                                                      à Modelo 4

08 – Conhecimento de Transporte Rodoviário de Cargas          à Modelo 8

55 – Nota Fiscal Eletrônica                                                         à Modelo 55

65 – Nota Fiscal de Consumidor Eletrônica\- NFC\-e                   à Modelo 65

Este registro deve ser gerado para registrar de forma detalhada, por combinação de alíquota de incidência do ISS e Item da Lista de Serviços da Lei Complementar 116/2003, os valores informados no registro B020 “pai” \(ou seja, o registro B020 que o antecede no arquivo\)\.

__Recuperação dos Dados__

- Empresa igual a empresa selecionada na geração;
- Estabelecimento igual ao estabelecimento selecionado na geração;

__\[MFS77681\]__

- Se a UF do Estabelecimento = “DF” e a nota for de entrada \(serviços tomados campo 03\-MOVTO\_E\_S <> ‘9’ da tabela SAFX07\), considerar:

A data do pagamento \(campo 175\-DT\_PAGTO\_NF da tabela SAFX07\) deve ser preenchida e referente ao período informado em tela \(>= data inicial e <= data final\) __E__

Indicador Tipo Retenção = “RETIDO PELO TOMADOR” \(campo 141\-IND\_TP\_RET = ‘1’ da tabela SAFX07\)

Se as condições de Data de Pagamento e Tipo de Retenção acima não forem atendidas, as notas não devem ser consideradas no registro\.

- Senão, considerar:
- A data fiscal da nota deve ser referente ao período informado em tela \(>= data inicial e <= data final\);
- Classificação fiscal 2 e 3 \(nota fiscal de serviço e nota fiscal mista campo 12\-COD\_CLASS\_DOC\_FIS = 2, 3 da tabela SAFX07\);
- Modelo 01, 03, 3B, 04, 08, 55 e 65 \(campo 13\-COD\_MODELO = 01, 03, 3B, 04, 08, 55 da tabela SAFX07\);
- Modelo 65 \(campo 13\-COD\_MODELO = 65 da tabela SAFX07\) deverá ser considerado apenas nas saídas, ou seja, será apresentada apenas as prestações de serviço \(campo 03\-MOVTO\_E\_S = 9\);
- Não considerar notas fiscais canceladas \(campo 30\-SITUACAO <> S da tabela SAFX07\);
- Desconsiderar itens das notas ficais cujo serviço foi realizado por intermediário e não tenha incidência do ISS ou Isenção \(campo 39\-BASE\_ISS da tabela SAFX09 quando campo 38\-TRIB\_ISS da tabela SAFX09 = 3\);
- Não considerar notas fiscais de serviço sem itens;
- Na geração por Inscrição Estadual Única, devem ser considerados os documentos fiscais de todos os Estabelecimentos envolvidos na centralização\.

__Processamento__

Não pode ser informado no registro a mesma combinação de valores dos campos Alíquota ISS e Código do Serviço LC 116, então os itens das notas fiscais deverão ser agrupados por esses campos de acordo com a recuperação: 32\-VLR\_ALIQ\_ISS da tabela SAFX09 e COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 \(TFIX60\) de acordo com 20\-COD\_SERV\_LEI\_116 da tabela SAFX2018 do 01\-COD\_SERVICO da tabela SAFX2018 vinculada a tabela SAFX09\.

__Tratamento:__

- O campo 20\-COD\_SERV\_LEI\_116 da tabela SAFX2018 não tem preenchimento obrigatório, então se na movimentação das notas fiscais de serviços prestados o campo estiver em branco ou nulo, será preenchido com zero na geração e deverá apresentar uma mensagem de log: *“O campo Código do Serviço Lei 116/03 do Serviço \(SAFX2018\) não está preenchido e é obrigatório para geração do Registro B420\. Favor verificar\! <<apresentar os dados da nota fiscal: Nº NF, Série NF, Data de Emissão, PFJ, Modelo>>”\.*

RNB025\-03

Campo VL\_BC\_ISS\_P:

Esse campo deve ser gerado com a informação do campo 39\-BASE\_ISS da tabela SAFX09 quando campo 38\-TRIB\_ISS da tabela SAFX09 = 1\.

RNB025\-04

Campo ALIQ\_ISS:

Esse campo deve ser gerado no formato 0,00, ou seja, o campo deve truncar as casas decimais\. Exemplo: 123,4567 gerar 123,45\.

RNB025\-06

Campo VL\_ISNT\_ISS\_P:

\[ALTERADA – MFS29820\]

Se o campo Tributação ISS \(campo 38 da SAFX09\) for igual a ‘2’

      Preencher com a Base ISS \(campo 39 da SAFX09\)

Senão

      Preencher com o Valor do Desconto \(campo 21 da SAFX09\)\.

RNB025\-07

Campo COD\_SERV:

Esse campo deve ser gerado com a informação do campo 20\-COD\_SERV\_LEI\_116 da tabela SAFX2018 do 01\-COD\_SERVICO da tabela SAFX2018 vinculada a tabela SAFX09\.

Essas informações do código de serviço da LC estão na TFIX60, é necessário importá\-la no módulo Ferramentas e cadastrá\-la na SAFX2018\.

__Registro B030 – Nota Fiscal de Serviços Simplificada \(Código 3A\)__

RNB030

__\[MFS95924\] Dispensa dos registros Bloco B__

__Devido a implantação do novo Sistema de Gerenciamento do Imposto sobre Serviços – ISS, pela Secretaria de Fazenda do Distrito Federal, para fatos geradores ocorridos a partir de 01/01/2023, não haverá a escrituração de prestações no Bloco B da EFD \- ICMS/ISS/IPI \- SPED, referente ao Imposto Sobre Serviços \- ISS \(o Bloco B deverá apenas ser aberto e encerrado, sem informação de valores\)\.__

Para o período a partir de __01/01/2023__ e UF do Estabelecimento = “__DF__”:

A geração deste registro passa a ser __NÃO OBRIGATÓRIO__\.

A escolha em informar o registro, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro B030 será gerado ou não\.

Para período de geração anterior a __01/01/2023__, o registro __DEVE__ ser gerado conforme as regras já existentes:

Neste registro devem ser gravadas as notas fiscais dos modelos que correspondem aos seguintes códigos da tabela “4\.1\.3\- Tabela Documentos Fiscais do ISS” do Ato COTEPE 44:

3A – Nota Fiscal de Serviços \- Modelo Simplificado                   à Modelo 3\-A

__Recuperação dos Dados__

Este processo será realizado apenas para os itens de documento fiscal de serviço que atendam aos seguintes critérios:

- Empresa igual a empresa selecionada na geração;
- Estabelecimento igual ao estabelecimento selecionado na geração;
- Nota fiscal de saída \(somente prestação de serviço campo 03\-MOVTO\_E\_S = 9 da tabela SAFX07\);
- A data fiscal da nota deve ser referente ao período informado em tela \(>= data inicial e <= data final\);
- Classificação fiscal 2 e 3 \(nota fiscal de serviço e nota fiscal mista campo 12\-COD\_CLASS\_DOC\_FIS = 2, 3 da tabela SAFX07\);
- Modelo 3A \(campo 13\-COD\_MODELO = 3A da tabela SAFX07\);
- Desconsiderar itens das notas ficais cujo serviço foi realizado por intermediário e não tenha incidência do ISS ou Isenção \(campo 39\-BASE\_ISS da tabela SAFX09 quando campo 38\-TRIB\_ISS da tabela SAFX09 = 3\);
- Não considerar notas fiscais de serviço sem itens;
- Na geração por Inscrição Estadual Única, devem ser considerados os documentos fiscais de todos os Estabelecimentos envolvidos na centralização\.

__Processamento__

Não podem ser informados, em um mesmo arquivo, dois ou mais registros B030 com a mesma combinação de valores dos campos formadores da chave do registro\. A chave do registro B030 é: COD\_MOD, SER, NUM\_DOC\_INI, NUM\_DOC\_FIN e DT\_DOC\. Então os itens das notas fiscais deverão ser agrupados por esses campos de acordo com a recuperação: 13\-COD\_MODELO, 09\-SERIE\_DOCFIS, 08\-NUM\_DOCFIS e 11\-DATA\_EMISSAO da tabela SAFX07\.

As notas fiscais de serviço canceladas recuperadas no período, devem servir apenas para a contagem da quantidade, pois elas estarão contabilizadas no range da numeração inicial e final do documento fiscal, mas seus valores deverão ser desconsiderados no caso da totalização do imposto\.

RNB030\-04

Campo NUM\_DOC\_INI:

Deverá ser considerado para a geração do campo em questão o número informado no campo “08\-Número do Documento Fiscal/ Número do Mapa Resumo de Caixa” da tabela SAFX07 do primeiro documento fiscal emitido diariamente \(considerando a data de emissão\) no período informado na tela de geração do arquivo magnético\.

RNB030\-05

Campo NUM\_DOC\_FIN:

Deverá ser considerado para a geração do campo em questão o número informado no campo “08\-Número do Documento Fiscal/ Número do Mapa Resumo de Caixa” da tabela SAFX07 do último documento fiscal emitido diariamente \(considerando a data de emissão\) no período informado na tela de geração do arquivo magnético\.

RNB030\-07

Campo QTD\_CANC:

Sumarizar a quantidade de documentos cancelados no período, considerando o campo “30\-Situação da Nota” = S\.

Essa quantidade deve compreender as notas fiscais informadas no campo NUM\_DOC\_INI e no campo NUM\_DOC\_FIN\.

RNB030\-08

Campo VL\_CONT:

Deverão ser considerados para a geração do campo em questão os itens de serviço do documento fiscal, com isso, o sistema deve realizar a soma do campo “15\-Valor Total do Serviço” de todos os itens da tabela SAFX09, desconsiderando no valor acumulado as notas fiscais de serviço que estiverem canceladas, ou seja, campo “30\-Situação do documento = S da tabela SAFX07\.

Essa totalização deve compreender as notas fiscais informadas no campo NUM\_DOC\_INI e no campo NUM\_DOC\_FIN\.

RNB030\-09

Campo VL\_ISNT\_ISS:

Deverão ser considerados para a geração do campo em questão os itens de serviço do documento fiscal, com isso, o sistema deve realizar a soma do campo:

 \[ALTERADA – MFS29820\]

Se o campo Tributação ISS \(campo 38 da SAFX09\) for igual a ‘2’

      Preencher com a Base ISS \(campo 39 da SAFX09\)

Senão

      Preencher com o Valor do Desconto \(campo 21 da SAFX09\)\.

Desconsiderando no valor acumulado as notas fiscais de serviço que estiverem canceladas, ou seja, campo “30\-Situação do documento = S da tabela SAFX07\.

Essa totalização deve compreender as notas fiscais informadas no campo NUM\_DOC\_INI e no campo NUM\_DOC\_FIN\.

RNB030\-10

Campo VL\_BC\_ISS:

Deverão ser considerados para a geração do campo em questão os itens de serviço do documento fiscal, com isso, o sistema deve realizar a soma do campo “39\-Base ISS” dos itens da tabela SAFX09 quando o campo “38\-Tributação = 1, desconsiderando no valor acumulado as notas fiscais de serviço que estiverem canceladas, ou seja, campo “30\-Situação do documento = S da tabela SAFX07\.

Essa totalização deve compreender as notas fiscais informadas no campo NUM\_DOC\_INI e no campo NUM\_DOC\_FIN\.

RNB030\-11

Campo VL\_ ISS:

Deverão ser considerados para a geração do campo em questão os itens de serviço do documento fiscal, com isso, o sistema deve realizar a soma do campo “33\-Valor ISS” dos itens da tabela SAFX09, desconsiderando no valor acumulado as notas fiscais de serviço que estiverem canceladas, ou seja, campo “30\-Situação do documento = S da tabela SAFX07\.

Essa totalização deve compreender as notas fiscais informadas no campo NUM\_DOC\_INI e no campo NUM\_DOC\_FIN\.

RNB030\-12

Campo COD\_INF\_OBS:

Recuperar a informação do campo “53\-Código da Observação” da tabela SAFX09, considerando o primeiro registro lido da combinação de itens selecionados nos critérios de agrupamento do registro\.

\[__ALTERAÇÃO \- MFS69058__\] Tratamento para considerar o parâmetro – “Campo Código de Observação \(Considerar 6 caracteres\)” \- para truncar o campo com 6 posições, conforme Manual Guia Prático\.

__SE__ o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

__OU__

__SE__ o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

Este código deverá ser referenciado no registro 0460\.

__Registro B035 – Detalhamento por Combinação de Alíquota e Item da Lista de Serviços da LC 116/2003__

RNB035

__\[MFS95924\] Dispensa dos registros Bloco B__

__Devido a implantação do novo Sistema de Gerenciamento do Imposto sobre Serviços – ISS, pela Secretaria de Fazenda do Distrito Federal, para fatos geradores ocorridos a partir de 01/01/2023, não haverá a escrituração de prestações no Bloco B da EFD \- ICMS/ISS/IPI \- SPED, referente ao Imposto Sobre Serviços \- ISS \(o Bloco B deverá apenas ser aberto e encerrado, sem informação de valores\)\.__

Para o período a partir de __01/01/2023__ e UF do Estabelecimento = “__DF__”:

A geração deste registro passa a ser __NÃO OBRIGATÓRIO__\.

A escolha em informar o registro, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro B035 será gerado ou não\.

Para período de geração anterior a __01/01/2023__, o registro __DEVE__ ser gerado conforme as regras já existentes:

Neste registro devem ser gravadas as notas fiscais dos modelos que correspondem aos seguintes códigos da tabela “4\.1\.3\- Tabela Documentos Fiscais do ISS” do Ato COTEPE 44:

3A – Nota Fiscal de Serviços \- Modelo Simplificado                   à Modelo 3\-A

Este registro deve ser gerado para registrar de forma detalhada, por combinação de alíquota de incidência do ISS e Item da Lista de Serviços da Lei Complementar 116/2003, os valores informados no registro B030 “pai” \(ou seja, o registro B030 que o antecede no arquivo\)\.

__Recuperação dos Dados__

Este processo será realizado apenas para os itens de documento fiscal de serviço que atendam aos seguintes critérios:

- Empresa igual a empresa selecionada na geração;
- Estabelecimento igual ao estabelecimento selecionado na geração;
- Nota fiscal de saída \(somente prestação de serviço campo 03\-MOVTO\_E\_S = 9 da tabela SAFX07\);
- A data fiscal da nota deve ser referente ao período informado em tela \(>= data inicial e <= data final\);
- Classificação fiscal 2 e 3 \(nota fiscal de serviço e nota fiscal mista campo 12\-COD\_CLASS\_DOC\_FIS = 2, 3 da tabela SAFX07\);
- Modelo 3A \(campo 13\-COD\_MODELO = 3A da tabela SAFX07\);
- Não considerar notas fiscais canceladas \(campo 30\-SITUACAO <> S da tabela SAFX07\);
- Desconsiderar itens das notas ficais cujo serviço foi realizado por intermediário e não tenha incidência do ISS ou Isenção \(campo 39\-BASE\_ISS da tabela SAFX09 quando campo 38\-TRIB\_ISS da tabela SAFX09 = 3\);
- Não considerar as notas fiscais de serviço sem itens;
- Na geração por Inscrição Estadual Única, devem ser considerados os documentos fiscais de todos os Estabelecimentos envolvidos na centralização\.

__Processamento__

Não pode ser informado no registro a mesma combinação de valores dos campos Alíquota ISS e Código do Serviço LC 116, então os itens das notas fiscais deverão ser agrupados por esses campos de acordo com a recuperação: 32\-VLR\_ALIQ\_ISS da tabela SAFX09 e COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 \(TFIX60\) de acordo com 20\-COD\_SERV\_LEI\_116 da tabela SAFX2018 do 01\-COD\_SERVICO da tabela SAFX2018 vinculada a tabela SAFX09\.

__Tratamento:__

- O campo 20\-COD\_SERV\_LEI\_116 da tabela SAFX2018 não tem preenchimento obrigatório, então se na movimentação das notas fiscais de serviços prestados o campo estiver em branco ou nulo, será preenchido com zero na geração e deverá apresentar uma mensagem de log: *“O campo Código do Serviço Lei 116/03 do Serviço \(SAFX2018\) não está preenchido e é obrigatório para geração do Registro B420\. Favor verificar\! <<apresentar os dados da nota fiscal: Nº NF, Série NF, Data de Emissão, PFJ, Modelo>>”\.*

RNB035\-03

Campo VL\_BC\_ISS\_P:

Esse campo deve ser gerado com a informação do campo 39\-BASE\_ISS da tabela SAFX09 quando campo 38\-TRIB\_ISS da tabela SAFX09 = 1\.

RNB035\-04

Campo ALIQ\_ISS:

Esse campo deve ser gerado no formato 0,00, ou seja, o campo deve truncar as casas decimais\. Exemplo: 123,4567 gerar 123,45\.

RNB035\-06

Campo VL\_ISNT\_ISS\_P:

\[ALTERADA – MFS29820\]

Se o campo Tributação ISS \(campo 38 da SAFX09\) for igual a ‘2’

      Preencher com a Base ISS \(campo 39 da SAFX09\)

Senão

      Preencher com o Valor do Desconto \(campo 21 da SAFX09\)\.

RNB035\-07

Campo COD\_SERV:

Esse campo deve ser gerado com a informação do campo 20\-COD\_SERV\_LEI\_116 da tabela SAFX2018 do 01\-COD\_SERVICO da tabela SAFX2018 vinculada a tabela SAFX09\.

Essas informações do código de serviço da LC estão na TFIX60, é necessário importá\-la no módulo Ferramentas e cadastrá\-la na SAFX2018\.

__Registro B350 – Serviços Prestados por Instituições Financeiras__

RNB350

__\[MFS95924\] Dispensa dos registros Bloco B__

__Devido a implantação do novo Sistema de Gerenciamento do Imposto sobre Serviços – ISS, pela Secretaria de Fazenda do Distrito Federal, para fatos geradores ocorridos a partir de 01/01/2023, não haverá a escrituração de prestações no Bloco B da EFD \- ICMS/ISS/IPI \- SPED, referente ao Imposto Sobre Serviços \- ISS \(o Bloco B deverá apenas ser aberto e encerrado, sem informação de valores\)\.__

Para o período a partir de __01/01/2023__ e UF do Estabelecimento = “__DF__”:

A geração deste registro passa a ser __NÃO OBRIGATÓRIO__\.

A escolha em informar o registro, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro B350 será gerado ou não\.

Para período de geração anterior a __01/01/2023__, o registro __DEVE__ ser gerado conforme as regras já existentes:

Este registro deve ser gerado para registrar os valores das receitas auferidas com prestação de serviços por instituições financeiras com base no Plano Contábil das Instituições do Sistema Financeiro Nacional – COSIF disponibilizado pelo Banco Central do Brasil\.

Deverão ser lançadas no registro B350 todas as receitas referentes a serviços \(classificação 7\.1\.7\.00\.00\-9 do COSIF\), ainda que não incluídos no anexo da LC 116/2003\. Só deverão ser excluídas destas receitas as prestações acobertadas por Notas Fiscais de Serviço\.

Para os serviços prestados pelas instituições financeiras sujeitos à retenção do ISS pelo tomador, será necessária a emissão da Nota Fiscal de Serviços que será informada no registro B020\. Estas prestações não serão informadas no registro B350, para que não sejam consideradas em duplicidade para os cálculos do ISS devido e do faturamento\.

__Recuperação dos Dados__

Este processo será realizado apenas para os itens que atendam aos seguintes critérios:

- Empresa igual a empresa selecionada na geração;
- Estabelecimento igual ao estabelecimento selecionado na geração;
- A data fiscal da nota deve ser referente ao período informado em tela \(>= data inicial e <= data final\);
- Na geração por Inscrição Estadual Única, devem ser considerados os itens de todos os Estabelecimentos envolvidos na centralização\.

__Processamento__

Não podem ser informados, em um mesmo arquivo, dois ou mais registros B350 com a mesma combinação de valores dos campos formadores da chave do registro, que no caso são: Código da conta do plano de contas, Código COSIF a que está subordinada a conta do ISS das instituições financeiras, Item da lista de serviços e Alíquota do ISS\. Então os itens da tabela SAFX269 deverão ser agrupados por esses campos de acordo com a recuperação: 04\-Conta Contábil, 05\-Código COSIF, 06\-Código de Serviço da Lei 116 e 11\-Valor do ISS\.

RNB350\-11

__Campo: COD\_INF\_OBS__

\[__ALTERAÇÃO – MFS69058__\] Tratamento para considerar o parâmetro – “Campo Código de Observação \(Considerar 6 caracteres\)” – para truncar o campo com 6 posições, conforme Manual Guia Prático\.

__SE__ o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

__OU__

__SE__ o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

Este código deverá ser referenciado no registro 0460\.

__Registro B420 – Totalização dos valores de serviços prestados por combinação de alíquota e item da lista de serviços da Lei Complementar nº 116/2003__

RNB420

__\[MFS95924\] Dispensa dos registros Bloco B__

__Devido a implantação do novo Sistema de Gerenciamento do Imposto sobre Serviços – ISS, pela Secretaria de Fazenda do Distrito Federal, para fatos geradores ocorridos a partir de 01/01/2023, não haverá a escrituração de prestações no Bloco B da EFD \- ICMS/ISS/IPI \- SPED, referente ao Imposto Sobre Serviços \- ISS \(o Bloco B deverá apenas ser aberto e encerrado, sem informação de valores\)\.__

Para o período a partir de __01/01/2023__ e UF do Estabelecimento = “__DF__”:

A geração deste registro passa a ser __NÃO OBRIGATÓRIO__\.

A escolha em informar o registro, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro B420 será gerado ou não\.

Para período de geração anterior a __01/01/2023__, o registro __DEVE__ ser gerado conforme as regras já existentes:

Este registro deve ser gerado para registrar de forma detalhada, por combinação de alíquota de incidência do ISS e Item da Lista de Serviços da Lei Complementar 116/2003, os valores totais das prestações de serviços realizadas no período\.

As informações serão recuperadas da pré\-geração executada antes da geração do arquivo magnético, sendo obrigatória sua execução caso necessite gerar o Bloco B\.

__Recuperação dos Dados__

Este processo será realizado apenas para os itens que atendam aos seguintes critérios:

- Empresa igual a empresa selecionada na geração;
- Estabelecimento igual ao estabelecimento selecionado na geração;

__\[MFS77681\]__

- Se a UF do Estabelecimento = “DF” e a nota for de entrada \(serviços tomados campo 03\-MOVTO\_E\_S <> ‘9’ da tabela SAFX07\), considerar:

A data do pagamento \(campo 175\-DT\_PAGTO\_NF da tabela SAFX07\) deve ser preenchida e referente ao período informado em tela \(>= data inicial e <= data final\) __E__

Indicador Tipo Retenção = “RETIDO PELO TOMADOR” \(campo 141\-IND\_TP\_RET = ‘1’ da tabela SAFX07\)

Se as condições de Data de Pagamento e Tipo de Retenção acima não forem atendidas, as notas não devem ser consideradas no registro\.

- Senão, considerar:
- A data fiscal da nota deve ser referente ao período informado em tela \(>= data inicial e <= data final\);
- Na geração por Inscrição Estadual Única, devem ser considerados os itens de todos os Estabelecimentos envolvidos na centralização\.

RNB440\-03

Campo COD\_PART:

Quando o Modelo do Documento for igual a “65” \(Nfe para Consumidor Final\), campo 13\-COD\_MODELO = 65 da tabela SAFX07, este campo não deve ser preenchido\.

Quando o parâmetro “Considerar o Indicador no Código do Participante” da tela de Dados Iniciais do módulo EFD estiver selecionado, este campo será gerado com o Código de identificação da pessoa FIS/JUR \(SAFX04\), concatenando o Indicador \(campo 02\-IND\_FIS\_JUR\) com o Código da PFJ \(campo 02\-COD\_FIS\_JUR\), considerando a formatação: Indicador \+ “\-“ \+ Código\.

Se o parâmetro “Considerar o Indicador no Código do Participante” da tela de Dados Iniciais do módulo EFD NÃO estiver selecionado, este campo será gerado apenas com o Código da PFJ \(02\-COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

__Registro B440 – Totalização dos Valores Retidos__

RNB440

__\[MFS95924\] Dispensa dos registros Bloco B__

__Devido a implantação do novo Sistema de Gerenciamento do Imposto sobre Serviços – ISS, pela Secretaria de Fazenda do Distrito Federal, para fatos geradores ocorridos a partir de 01/01/2023, não haverá a escrituração de prestações no Bloco B da EFD \- ICMS/ISS/IPI \- SPED, referente ao Imposto Sobre Serviços \- ISS \(o Bloco B deverá apenas ser aberto e encerrado, sem informação de valores\)\.__

Para o período a partir de __01/01/2023__ e UF do Estabelecimento = “__DF__”:

A geração deste registro passa a ser __NÃO OBRIGATÓRIO__\.

A escolha em informar o registro, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro B440 será gerado ou não\.

Para período de geração anterior a __01/01/2023__, o registro __DEVE__ ser gerado conforme as regras já existentes:

Este registro deve ser gerado para registrar os valores retidos tanto referentes às prestações \(declarante na condição de prestador\) quanto às aquisições \(declarante na condição de tomador\)\. Os valores são informados por tomador e/ou prestador conforme o tipo de operação\.

 

As informações serão recuperadas da pré\-geração executada antes da geração do arquivo magnético, sendo obrigatória sua execução caso necessite gerar o Bloco B\.

__Recuperação dos Dados__

Este processo será realizado apenas para os itens que atendam aos seguintes critérios:

- Empresa igual a empresa selecionada na geração;
- Estabelecimento igual ao estabelecimento selecionado na geração;

__\[MFS77681\]__

- Se a UF do Estabelecimento = “DF” e a nota for de entrada \(serviços tomados campo 03\-MOVTO\_E\_S <> ‘9’ da tabela SAFX07\), considerar:

A data do pagamento \(campo 175\-DT\_PAGTO\_NF da tabela SAFX07\) deve ser preenchida e referente ao período informado em tela \(>= data inicial e <= data final\) __E__

Indicador Tipo Retenção = “RETIDO PELO TOMADOR” \(campo 141\-IND\_TP\_RET = ‘1’ da tabela SAFX07\)

Se as condições de Data de Pagamento e Tipo de Retenção acima não forem atendidas, as notas não devem ser consideradas no registro\.

- Senão, considerar:
- A data fiscal da nota deve ser referente ao período informado em tela \(>= data inicial e <= data final\);
- Na geração por Inscrição Estadual Única, devem ser considerados os itens de todos os Estabelecimentos envolvidos na centralização\.

RNB440\-03

Campo COD\_PART:

Quando o Modelo do Documento for igual a “65” \(Nfe para Consumidor Final\), campo 13\-COD\_MODELO = 65 da tabela SAFX07, este campo não deve ser preenchido\.

Quando o parâmetro “Considerar o Indicador no Código do Participante” da tela de Dados Iniciais do módulo EFD estiver selecionado, este campo será gerado com o Código de identificação da pessoa FIS/JUR \(SAFX04\), concatenando o Indicador \(campo 02\-IND\_FIS\_JUR\) com o Código da PFJ \(campo 02\-COD\_FIS\_JUR\), considerando a formatação: Indicador \+ “\-“ \+ Código\.

Se o parâmetro “Considerar o Indicador no Código do Participante” da tela de Dados Iniciais do módulo EFD NÃO estiver selecionado, este campo será gerado apenas com o Código da PFJ \(02\-COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

__Registro B460 – Deduções do ISS__

RNB460

__\[MFS95924\] Dispensa dos registros Bloco B__

__Devido a implantação do novo Sistema de Gerenciamento do Imposto sobre Serviços – ISS, pela Secretaria de Fazenda do Distrito Federal, para fatos geradores ocorridos a partir de 01/01/2023, não haverá a escrituração de prestações no Bloco B da EFD \- ICMS/ISS/IPI \- SPED, referente ao Imposto Sobre Serviços \- ISS \(o Bloco B deverá apenas ser aberto e encerrado, sem informação de valores\)\.__

Para o período a partir de __01/01/2023__ e UF do Estabelecimento = “__DF__”:

A geração deste registro passa a ser __NÃO OBRIGATÓRIO__\.

A escolha em informar o registro, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro B460 será gerado ou não\.

Para período de geração anterior a __01/01/2023__, o registro __DEVE__ ser gerado conforme as regras já existentes:

Este registro deve ser gerado para registrar as deduções do ISS que irão influenciar na apuração dos valores a recolher do ISS Próprio, ISS substituto \(devido pelas retenções referentes às aquisições do declarante\) e ISS Uniprofissional, conforme o caso\.

__Recuperação dos Dados__

Este processo será realizado apenas para os itens que atendam aos seguintes critérios:

- Empresa igual a empresa selecionada na geração;
- Estabelecimento igual ao estabelecimento selecionado na geração;
- A data fiscal da nota deve ser referente ao período informado em tela \(>= data inicial e <= data final\);
- Na geração por Inscrição Estadual Única, devem ser considerados os itens de todos os Estabelecimentos envolvidos na centralização\.

RNB460\-07

__Campo: COD\_INF\_OBS__

\[__ALTERAÇÃO \- MFS69058__\] Tratamento para considerar o parâmetro – “Campo Código de Observação \(Considerar 6 caracteres\)” \- para truncar o campo com 6 posições, conforme Manual Guia Prático\.

__SE__ o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

__OU__

__SE__ o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

Este código deverá ser referenciado no registro 0460\.

__Registro B470 – Apuração do ISS__

RNB470

__\[MFS95924\] Dispensa dos registros Bloco B__

__Devido a implantação do novo Sistema de Gerenciamento do Imposto sobre Serviços – ISS, pela Secretaria de Fazenda do Distrito Federal, para fatos geradores ocorridos a partir de 01/01/2023, não haverá a escrituração de prestações no Bloco B da EFD \- ICMS/ISS/IPI \- SPED, referente ao Imposto Sobre Serviços \- ISS \(o Bloco B deverá apenas ser aberto e encerrado, sem informação de valores\)\.__

__Em atendimento a essa implantação:__

Para período de geração a partir de __01/01/2023 __e UF do Estabelecimento = “DF”, este registro __DEVE__ ser gerado atendendo as seguintes condições:

\- Registro B470 é obrigatório, então deve ser gerado com todos os campos de valores zerados\. Os valores devem ser gerados com zero, mesmo que exista dados gerados na rotina de pré\-geração do registro B470\.

Para período de geração anterior a __01/01/2023__, o registro __DEVE__ ser gerado conforme as regras já existentes:

Este registro deve ser gerado para registrar os totais referentes às prestações de serviço do declarante e para apurar os valores a recolher do ISS próprio, do ISS retido pelo declarante na condição de tomador e do ISS Uniprofissional\.

As informações serão recuperadas da pré\-geração executada antes da geração do arquivo magnético, sendo obrigatória sua execução caso necessite gerar o Bloco B\.

__Recuperação dos Dados__

Este processo será realizado apenas para os itens que atendam aos seguintes critérios:

- Empresa igual a empresa selecionada na geração;
- Estabelecimento igual ao estabelecimento selecionado na geração;

__\[MFS77681\]__

- Se a UF do Estabelecimento = “DF” e a nota for de entrada \(serviços tomados campo 03\-MOVTO\_E\_S <> ‘9’ da tabela SAFX07\), considerar:

A data do pagamento \(campo 175\-DT\_PAGTO\_NF da tabela SAFX07\) deve ser preenchida e referente ao período informado em tela \(>= data inicial e <= data final\) __E__

Indicador Tipo Retenção = “RETIDO PELO TOMADOR” \(campo 141\-IND\_TP\_RET = ‘1’ da tabela SAFX07\)

Se as condições de Data de Pagamento e Tipo de Retenção acima não forem atendidas, as notas não devem ser consideradas no registro\.

- Senão, considerar:
- A data fiscal da nota deve ser referente ao período informado em tela \(>= data inicial e <= data final\);
- Na geração por Inscrição Estadual Única, devem ser considerados os itens de todos os Estabelecimentos envolvidos na centralização\.

__\[MFS32212\]__

__Obs\.:__ Quando o estabelecimento da geração for do estado igual a “DF” e não houver dados gerados na rotina de pré\-geração, o registro B470 é obrigatório, então deve ser gerado com todos os campos de valores zerados\.

__Registro B500 – Apuração do ISS Sociedade Uniprofissional__

RN500

__\[MFS95924\] Dispensa dos registros Bloco B__

__Devido a implantação do novo Sistema de Gerenciamento do Imposto sobre Serviços – ISS, pela Secretaria de Fazenda do Distrito Federal, para fatos geradores ocorridos a partir de 01/01/2023, não haverá a escrituração de prestações no Bloco B da EFD \- ICMS/ISS/IPI \- SPED, referente ao Imposto Sobre Serviços \- ISS \(o Bloco B deverá apenas ser aberto e encerrado, sem informação de valores\)\.__

Para o período a partir de __01/01/2023__ e UF do Estabelecimento = “__DF__”:

A geração deste registro passa a ser __NÃO OBRIGATÓRIO__\.

A escolha em informar o registro, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro B500 será gerado ou não\.

Para período de geração anterior a __01/01/2023__, o registro __DEVE__ ser gerado conforme as regras já existentes:

Este registro deve ser gerado para registrar o valor das receitas, a quantidade de profissionais habilitados e o valor do ISS a recolher das Sociedades Uniprofissionais\.

__Recuperação dos Dados__

Este processo será realizado apenas para os itens que atendam aos seguintes critérios:

- Empresa igual a empresa selecionada na geração;
- Estabelecimento igual ao estabelecimento selecionado na geração;
- A data fiscal da nota deve ser referente ao período informado em tela \(>= data inicial e <= data final\);
- Na geração por Inscrição Estadual Única, devem ser considerados os itens de todos os Estabelecimentos envolvidos na centralização\.

__Registro B510 – Uniprofissional – Empregados e Sócios__

RN510

__\[MFS95924\] Dispensa dos registros Bloco B__

__Devido a implantação do novo Sistema de Gerenciamento do Imposto sobre Serviços – ISS, pela Secretaria de Fazenda do Distrito Federal, para fatos geradores ocorridos a partir de 01/01/2023, não haverá a escrituração de prestações no Bloco B da EFD \- ICMS/ISS/IPI \- SPED, referente ao Imposto Sobre Serviços \- ISS \(o Bloco B deverá apenas ser aberto e encerrado, sem informação de valores\)\.__

Para o período a partir de __01/01/2023__ e UF do Estabelecimento = “__DF__”:

A geração deste registro passa a ser __NÃO OBRIGATÓRIO__\.

A escolha em informar o registro, fica sob responsabilidade do declarante, que deve informar na tela de Perfil, se o registro B510 será gerado ou não\.

Para período de geração anterior a __01/01/2023__, o registro __DEVE__ ser gerado conforme as regras já existentes:

Este registro deve ser gerado para registrar as informações de cada um dos profissionais \(sócios, empregados habilitados e empregados não habilitados\) da sociedade uniprofissional\.

__Recuperação dos Dados__

Este processo será realizado apenas para os itens que atendam aos seguintes critérios:

- Empresa igual a empresa selecionada na geração;
- Estabelecimento igual ao estabelecimento selecionado na geração;
- A data fiscal da nota deve ser referente ao período informado em tela \(>= data inicial e <= data final\);
- Na geração por Inscrição Estadual Única, devem ser considerados os itens de todos os Estabelecimentos envolvidos na centralização\.

__Processamento__

- Não podem ser informados, em um mesmo arquivo, dois ou mais registros B510 com o mesmo valor do campo CPF, CPF do Profissional da tabela SAFX222;
- O número de sócios tem de ser maior ou igual a um \(ou seja, se existir no arquivo registros B510, pelo menos um deles tem de ter o campo “IND\_SOC” com valor “0”\);
- O número de profissionais não habilitados não pode ser maior que o dobro do número de sócios \(ou seja, a quantidade de registros B510 com o campo “IND\_PROF” preenchido com “1” tem de ser menor ou igual ao dobro da quantidade de registros B510 com o campo “IND\_SOC” preenchido com “0”\)\.

RNB510\-02

Campo IND\_PROF:

Quando não houver informação no campo 05\-Indicador de habilitação da tabela SAFX222, emitir uma mensagem no log: *“O campo Indicador de habilitação é obrigatório e não foi preenchido, favor verificar\! <<CPF>>, <<Nome do Profissional ou Nulo>>, <<Período>>”\.*

RNB510\-03

Campo IND\_ESC:

Quando não houver informação no campo 06\-Indicador de escolaridade da tabela SAFX222, emitir uma mensagem no log: *“O campo Indicador de escolaridade é obrigatório e não foi preenchido, favor verificar\! <<CPF>>, <<Nome do Profissional ou Nulo>>, <<Período>>”\.*

RNB510\-04

Campo IND\_SOC:

Quando não houver informação no campo 07\-Indicador da participação societária da tabela SAFX222, emitir uma mensagem no log: *“O campo Indicador da participação societária é obrigatório e não foi preenchido, favor verificar\! <<CPF>>, <<Nome do Profissional ou Nulo>>, <<Período>>”\.*

RNB510\-06

Campo NOME:

Quando não houver informação no campo 08\-Nome do Profissional da tabela SAFX222, emitir uma mensagem no log: *“O campo Nome do profissional é obrigatório e não foi preenchido, favor verificar\! <<CPF>>, <<Nome do Profissional ou Nulo>>, <<Período>>”\.*

__Registro B990 – Encerramento do Bloco B__

RNB990

Um registro por arquivo, informando a quantidade total de linhas do Bloco B gravadas no arquivo\.


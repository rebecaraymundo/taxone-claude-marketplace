# MTZ_DEST_Geracao_Meio_Magnetico

- **Fonte:** MTZ_DEST_Geracao_Meio_Magnetico.docx
- **Modificado:** 2025-11-25
- **Tamanho:** 91 KB

---

THOMSON REUTERS

Municipal

DEST \- Declaração Eletrônica dos Serviços Tomados

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-12392

Julyana Perrucini

Criação do validador DEST \- Declaração Eletrônica dos Serviços Tomados\. 

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN01

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo Parauapebas deve ficar localizado no grupo “Municipal”\.

Descrição do módulo Parauapebas: “*Consiste na entrega das informações sobre os serviços prestados e tomados do município de Parauapebas*”\.

MFS\-12392

RN02

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “PA” e ao código de município do IBGE igual a “5536” \(Parauapebas\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Parauapebas, Pará\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

MFS\-12392

RN03

__Estrutura de menus do módulo DEST:__

Deverão ser criados os seguintes menu e sub\-menus no módulo DEST:

- Arquivo    
- Obrigações
	- __Geração do Meio Magnético__
	- __Arquivo de Entradas de Serviços \(Const\. Civil/ Utilities/ Telecom\)__
- Janela
- Ajuda

MFS\-12392

RN04

__Regra de criação do nome do arquivo__

__Serviços Prestados:__

__       SP\_DEST\_MUNICIPIO\_DDMMAAAA\.TXT__, onde:

       __SP\_DEST__: representa a obrigação que está sendo gerada\. Apenas registros de serviços prestados

       __MUNICIPIO__: representa o município que está sendo gerado

       __DDMMAAAA__: representa a data inicial da geração

       __\.TXT__: extensão do arquivo\.

*Exemplo:* SP\_DEST\_PARAUAPEBAS\_01012010\.TXT

__Serviços Tomados:__

__       ST\_DEST\_MUNICIPIO\_DDMMAAAA\.TXT__, onde:

       __ST\_DEST__: representa a obrigação que está sendo gerada\. Apenas registros de serviços tomados

       __MUNICIPIO__: representa o município que está sendo gerado

       __DDMMAAAA__: representa a data inicial da geração

       __\.TXT__: extensão do arquivo\.

*Exemplo:* ST\_DEST\_PARAUAPEBAS\_01012010\.TXT

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__ST\_DEST\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.TXT__, onde:

__        ST\_DEST__: representa a obrigação que está sendo gerada\. Apenas registros de serviços tomados

__        MUNICIPIO__: representa o município que está sendo gerado

        __DDMMAAAA__: representa a data inicial da geração

__        MMAAAA:__ mês da competência referente à nota gerada

        __\.TXT__: extensão do arquivo\.

Ex: ST\_DEST\_PARAUAPEBAS\_01012014\_122013\.TXT

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.__

MFS\-12392

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Gerar Serviços Prestados:__ deve ser exibido através de um CheckBox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Gerar Serviços Tomados:__ deve ser exibido através de um CheckBox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)\.

__Estabelecimento:__ o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__*Tratamentos:* __

- Cada campo padrão deverá exibir mensagens existentes caso de não preenchimento\.

 

MFS\-12392

RN06

__Regras referentes à formatação dos registros gerados no meio magnético:__

Abaixo seguem algumas formatações de dados que devem ser seguidas para geração correta na estrutura dos arquivos:

O arquivo a ser gerado para importação dever ser no formato __‘TXT’\.__

- Os campos do tipo Texto devem ser alinhados a esquerda e ser completados por caracteres de espaço a direita até completar seu tamanho máximo;
- Os campos do tipo Numérico devem ser alinhados a direita e ser completados com zero a esquerda até completar seu tamanho máximo;
- Os campos de valor, informar sem ponto milhar e decimal e sem o símbolo da moeda, informando sempre os centavos\.

MFS\-12392

RN07

__Regra p/ Recuperação das notas fiscais de serviços prestados__

Esse arquivo deve ser gerado apenas quando o campo “Gerar Serviços Prestados” estiver marcado e deve conter todas as notas fiscais com as seguintes características:

- Notas fiscais de saída \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL = 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência

O agrupamento deve ocorrer por Código de Serviço, Forma de Tributação e Alíquota\.

*Observação: *Quando a nota fiscal não tiver itens não deve ser considerada\.

MFS\-12392

RN08

__Regra p/ Registro 1 – Notas Fiscais Prestadas – Campo Registro__

Preencher com fixo “1”\.

Campo obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-12392

RN09

__Regra p/ Registro 1 – Notas Fiscais Prestadas – Campo Documento do Prestador__

Preencher com o conteúdo do campo CGC da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

Campo obrigatório

Formato: XX\.XXX\.XXX/XXXX\-XX

Tipo: Texto

Tamanho: 18

MFS\-12392

RN10

__Regra p/ Registro 1 – Notas Fiscais Prestadas – Campo Exercício/ Mês de Referência__

Preencher com o __ano__ e o __mês__ do conteúdo do campo Data Inicial preenchido na tela de geração do arquivo magnético\.

Campo obrigatório

Formato: AAAAMM

Tipo: Numérico

Tamanho: 6

MFS\-12392

RN11

__Regra p/ Registro 1 – Notas Fiscais Prestadas – Campo Código do Serviço__

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, gerar com zeros e emitir mensagem padrão de log\.

Campo obrigatório

Formato: 9999

Tipo: Numérico

Tamanho: 4

MFS\-12392

RN12

__Regra p/ Registro 1 – Notas Fiscais Prestadas – Campo Inscrição Municipal\*__

Preencher com o conteúdo do campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 7 primeiras posições\.
- Se o campo ultrapassar 7 posições, emitir a mensagem de log:* “O campo Inscrição Municipal da filial ultrapassou o tamanho máximo permitido \(7 posições\) <<NF>>, <<Série>>, <<Data Emissão>>*\.*”*\.

Campo não obrigatório

Formato: XXXXXXX

Tipo: Texto

Tamanho: 7

MFS\-12392

RN13

__Regra p/ Registro 1 – Notas Fiscais Prestadas – Campo Documento do Tomador__

Preencher com o conteúdo do campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR \(campo 06 da SAFX04\) referente ao prestador vinculado a nota fiscal\.

Campo obrigatório

Formato: XX\.XXX\.XXX/XXXX\-XX

Tipo: Texto

Tamanho: 18

MFS\-12392

RN14

__Regra p/ Registro 1 – Notas Fiscais Prestadas – Campo Razão Social do Tomador__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR \(campo 05 da SAFX04\) referente ao prestador vinculado a nota fiscal\.

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 100

MFS\-12392

RN15

__Regra p/ Registro 1 – Notas Fiscais Prestadas – Campo Situação do Tomador__

Preencher com:

0 – Do Município, se o município do tomador preenchido no campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) for igual ao município do módulo;

1 – Outro Município, se o município do tomador preenchido no campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) for diferente do município do módulo;

2 – Exterior, se a UF do tomador preenchido no campo UF da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) for igual a “EX”\.

__Tratamento:__

- Se o município do tomador não estiver preenchido, gravar com zero e emitir a seguinte mensagem de log: *“O município do tomador não está preenchido no cadastro de Pessoa Física/Jurídica, favor verificar\! <<NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”*;
- Se a UF do tomador não estiver preenchido, gravar com zero e emitir a seguinte mensagem de log: *“A UF do tomador não está preenchida no cadastro de Pessoa Física/Jurídica, favor verificar\! <<NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”*\.

Campo obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-12392

RN16

__Regra p/ Registro 1 – Notas Fiscais Prestadas – Campo Forma de Tributação__

Preencher com:

2 \(Cancelado\), se o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL \(campo 30 da SAFX07\) for igual a “S”;

3 \(Isento\), se o campo VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV \(campo 39 da SAFX09 quando o campo 38 for igual a 2\) for maior que zero OU se o campo IND\_ISS da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal for igual a “04” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “433” na tela Classificação de Serviços de Parâmetros para Município;

4 \(Imune\), se o campo IND\_ISS da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal for igual a “01” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “420” na tela Classificação de Serviços de Parâmetros para Município;

5 \(Outro Município\), se o serviço cadastrado na nota fiscal estiver parametrizado igual a “465” na tela Classificação de Serviços de Parâmetros para Município OU se o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) <> do município do estabelecimento E o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL \(campo 73 da SAFX07\) <> do município do estabelecimento E o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) <> COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL \(campo 73 da SAFX07\) E o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV \(campo 58 da SAFX09\) estiver preenchido OU se o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) <> do município do estabelecimento E o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL \(campo 73 da SAFX07\) <> do município do estabelecimento E o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) <> COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL \(campo 73 da SAFX07\) E o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) for igual a “1 \- RETIDO PELO TOMADOR”;

1 \(Retido na Fonte\), se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_ISS da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal for igual a “05” OU se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) for igual a “2 \- RETIDO PELO PRESTADOR” e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL \(campo 73 da SAFX07\) for igual ao município do módulo selecionado;

7 \(Não Incidência\), se o campo IND\_ISS da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal for igual a “06” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “432” na tela Classificação de Serviços de Parâmetros para Município;

8 \(Estimado\), se o campo IND\_ISS da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal for igual a “02” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “421” na tela Classificação de Serviços de Parâmetros para Município;

9 \(Autônomo Fixo\), se o serviço cadastrado na nota fiscal estiver parametrizado igual a “468” na tela Classificação de Serviços de Parâmetros para Município;

B \(Simples Nacional\), se o campo IND\_ISS da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal for igual a “07”;

0 \(Normal\), se nenhuma das regras anteriores forem atendidas\.

*Atenção:* Os códigos 6 \(Extraviado\) e A \(Exclusão Lógica\) não serão tratados nesse momento\.

Campo obrigatório

Formato: X

Tipo: Texto

Tamanho: 1

MFS\-12392

RN17

__Regra p/ Registro 1 – Notas Fiscais Prestadas – Campo Tipo de Documento__

Preencher com o conteúdo do campo Tipo Docto da parametrização no módulo Parâmetros para Município – Parâmetros – Tipo Docto Msaf x Tipo Docto referente ao código de tipo de documento cadastrado na nota fiscal emitida e ao município que está sendo gerado\.

__Tratamento:__

- Se não houver parametrização, gravar com zero e emitir a seguinte mensagem de log: *“Não existe parametrização de Tipo Docto em Parâmetros para Município, favor verificar\! <<NF>>, <<Série>>, <<Data Emissão>>*\.

Campo obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-12392

RN18

__Regra p/ Registro 1 – Notas Fiscais Prestadas – Campo Nota Inicial__

Preencher com o conteúdo do campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\)\.

__Tratamento:__

- Considerar as 9 primeiras posições\.
- Se o campo ultrapassar 9 posições, emitir a mensagem de log:* “O campo número do documento ultrapassou o tamanho máximo permitido \(9 posições\) para Nota Inicial e Final <<NF>>, <<Série>>, <<Data Emissão>>*\.*”*\.

Campo obrigatório

Formato: 999999999

Tipo: Numérico

Tamanho: 9

MFS\-12392

RN19

__Regra p/ Registro 1 – Notas Fiscais Prestadas – Campo Nota Final__

Preencher com o conteúdo do campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\)\.

__Tratamento:__

- Considerar as 9 primeiras posições\.
- Se o campo ultrapassar 9 posições, emitir a mensagem de log:* “O campo número do documento ultrapassou o tamanho máximo permitido \(9 posições\) para Nota Inicial e Final <<NF>>, <<Série>>, <<Data Emissão>>*\.*”*\.

Campo obrigatório

Formato: 999999999

Tipo: Numérico

Tamanho: 9

MFS\-12392

RN20

__Regra p/ Registro 1 – Notas Fiscais Prestadas – Campo Data de Emissão da Nota__

Preencher com o conteúdo do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAFX07\)\.

Campo obrigatório

Formato: AAAAMMDD

Tipo: Data

Tamanho: 8

MFS\-12392

RN21

__Regra p/ Registro 1 – Notas Fiscais Prestadas – Campo Valor Contábil__

Preencher com o conteúdo do campo VLR\_TOT da tabela DWT\_ITENS\_SERV \(campo 15 da SAFX09\)\.

__Tratamento:__

- Truncar campo pela esquerda considerando o tamanho exigido pelo layout sem considerar vírgulas ou pontos\.

Campo obrigatório

Formato: 999999999999

Tipo: Numérico

Tamanho: 12 \(10 inteiros com 2 decimais\)

MFS\-12392

RN22

__Regra p/ Registro 1 – Notas Fiscais Prestadas – Campo Valor Tributável__

Preencher com o conteúdo do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV \(campo 33 da SAFX09\)\.

__Tratamento:__

- Truncar campo pela esquerda considerando o tamanho exigido pelo layout sem considerar vírgulas ou pontos\.
- Se o valor do ISS não estiver preenchido, gravar com zeros e emitir a seguinte mensagem de log: *“O valor do ISS não está preenchido no item da nota fiscal, favor verificar\! <<NF>>, <<Série>>, <<Data Emissão>>”*\.

Campo obrigatório

Formato: 999999999999

Tipo: Numérico

Tamanho: 12 \(10 inteiros com 2 decimais\)

MFS\-12392

RN23

__Regra p/ Registro 1 – Notas Fiscais Prestadas – Campo Observações__

Preencher com o conteúdo do campo OBS\_INF\_ADIC\_NF da tabela DWT\_DOCTO\_FISCAL \(campo 150 da SAFX07\)\.

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 255

MFS\-12392

RN24

__Regra p/ Registro 1 – Notas Fiscais Prestadas – Campo Alíquota__

Preencher com o conteúdo do campo ALIQ\_TRIBUTO\_ISS da DWT\_ITENS\_SERV \(campo 32 da SAFX09\)\.

__Tratamento:__

- Truncar campo pela esquerda considerando o tamanho exigido pelo layout sem considerar vírgulas ou pontos\.
- Se a alíquota do ISS não estiver preenchida, gravar com zeros e emitir a seguinte mensagem de log: *“A alíquota do ISS não está preenchida no item da nota fiscal, favor verificar\! <<NF>>, <<Série>>, <<Data Emissão>>”*\.

Campo obrigatório

Formato: 99999

Tipo: Numérico

Tamanho: 5 \(3 inteiros com 2 decimais\)

MFS\-12392

RN25

__Regra p/ Recuperação das notas fiscais de serviços tomados__

Esse arquivo deve ser gerado apenas quando o campo “Gerar Serviços Tomados” estiver marcado e deve conter todas as notas fiscais com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)

O agrupamento deve ocorrer por Código de Serviço, Forma de Tributação e Alíquota\.

*Observação: *Quando a nota fiscal não tiver itens não deve ser considerada\.

MFS\-12392

RN26

__Regra p/ Registro 2 – Notas Fiscais Tomadas – Campo Registro__

Preencher com fixo “2”\.

Campo obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-12392

RN27

__Regra p/ Registro 2 – Notas Fiscais Tomadas – Campo Documento do Tomador__

Preencher com o conteúdo do campo CGC da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

Campo obrigatório

Formato: XX\.XXX\.XXX/XXXX\-XX

Tipo: Texto

Tamanho: 18

MFS\-12392

RN28

__Regra p/ Registro 2 – Notas Fiscais Tomadas – Campo Exercício/ Mês de Referência__

Preencher com o __ano__ e o __mês__ do conteúdo do campo Data Inicial preenchido na tela de geração do arquivo magnético\.

Campo obrigatório

Formato: AAAAMM

Tipo: Numérico

Tamanho: 6

MFS\-12392

RN29

__Regra p/ Registro 2 – Notas Fiscais Tomadas – Campo Código do Serviço__

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido, gerar com zeros e emitir mensagem padrão de log\.

Campo obrigatório

Formato: 9999

Tipo: Numérico

Tamanho: 4

MFS\-12392

RN30

__Regra p/ Registro 2 – Notas Fiscais Tomadas – Campo Inscrição Municipal\*__

Preencher com o conteúdo do campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO referente a filial cadastrada na nota fiscal\.

__Tratamento:__

- Considerar as 7 primeiras posições\.
- Se o campo ultrapassar 7 posições, emitir a mensagem de log:* “O campo Inscrição Municipal da filial ultrapassou o tamanho máximo permitido \(7 posições\) <<NF>>, <<Série>>, <<Data Emissão>>*\.*”*\.

Campo não obrigatório

Formato: XXXXXXX

Tipo: Texto

Tamanho: 7

MFS\-12392

RN31

__Regra p/ Registro 2 – Notas Fiscais Tomadas – Campo Documento do Prestador__

Preencher com o conteúdo do campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR \(campo 06 da SAFX04\) referente ao prestador vinculado a nota fiscal\.

Campo obrigatório

Formato: XX\.XXX\.XXX/XXXX\-XX

Tipo: Texto

Tamanho: 18

MFS\-12392

RN32

__Regra p/ Registro 2 – Notas Fiscais Tomadas – Campo Razão Social do Prestador__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR \(campo 05 da SAFX04\) referente ao prestador vinculado a nota fiscal\.

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 100

MFS\-12392

RN33

__Regra p/ Registro 2 – Notas Fiscais Tomadas – Campo Situação do Prestador__

Preencher com:

0 – Do Município, se o município do prestador preenchido no campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) for igual ao município do módulo;

1 – Outro Município, se o município do prestador preenchido no campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) for diferente do município do módulo;

2 – Exterior, se a UF do prestador preenchido no campo UF da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) for igual a “EX”\.

__Tratamento:__

- Se o município do prestador não estiver preenchido, gravar com zero e emitir a seguinte mensagem de log: *“O município do prestador não está preenchido no cadastro de Pessoa Física/Jurídica, favor verificar\! <<NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”*;
- Se a UF do prestador não estiver preenchido, gravar com zero e emitir a seguinte mensagem de log: *“A UF do tomador não está preenchida no cadastro de Pessoa Física/Jurídica, favor verificar\! <<NF>>, <<Série>>, <<Data Emissão>>, <<PFJ>>”*\.

Campo obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-12392

RN34

__Regra p/ Registro 2 – Notas Fiscais Tomadas – Campo Forma de Tributação__

Preencher com:

3 \(Isento\), se o campo VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV \(campo 39 da SAFX09 quando o campo 38 for igual a 2\) for maior que zero OU se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) referente a pessoa física/jurídica cadastrada na nota fiscal for igual a “10” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “433” na tela Classificação de Serviços de Parâmetros para Município;

4 \(Imune\), se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) referente a pessoa física/jurídica cadastrada na nota fiscal for igual a “07” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “420” na tela Classificação de Serviços de Parâmetros para Município;

5 \(Outro Município\), se o serviço cadastrado na nota fiscal estiver parametrizado igual a “465” na tela Classificação de Serviços de Parâmetros para Município OU se o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) <> do município do estabelecimento E o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL \(campo 73 da SAFX07\) <> do município do estabelecimento E o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) <> COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL \(campo 73 da SAFX07\) E o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV \(campo 58 da SAFX09\) estiver preenchido OU se o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) <> do município do estabelecimento E o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL \(campo 73 da SAFX07\) <> do município do estabelecimento E o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) <> COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL \(campo 73 da SAFX07\) E o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) for igual a “2 \- RETIDO PELO PRESTADOR”;

1 \(Retido na Fonte\), se o serviço cadastrado no item da nota fiscal estiver parametrizado igual a “454” na tela Classificação de Serviços de Parâmetros para Município OU se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\)  referente a pessoa física/jurídica cadastrada na nota fiscal for igual a “05” OU se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) for igual a “1 \- RETIDO PELO TOMADOR” e o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL \(campo 73 da SAFX07\) for igual ao município do módulo selecionado;

7 \(Não Incidência\), se o serviço cadastrado na nota fiscal estiver parametrizado igual a “432” na tela Classificação de Serviços de Parâmetros para Município;

8 \(Estimado\), se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) referente a pessoa física/jurídica cadastrada na nota fiscal for igual a “08” OU se o serviço cadastrado na nota fiscal estiver parametrizado igual a “421” na tela Classificação de Serviços de Parâmetros para Município;

9 \(Autônomo Fixo\), se o serviço cadastrado na nota fiscal estiver parametrizado igual a “468” na tela Classificação de Serviços de Parâmetros para Município;

B \(Simples Nacional\), se o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR \(campo 43 da SAFX04\) referente a pessoa física/jurídica cadastrada na nota fiscal for igual a “S”;

0 \(Normal\), se nenhuma das regras anteriores forem atendidas\.

*Atenção:* Os códigos 6 \(Extraviado\) e A \(Exclusão Lógica\) não serão tratados nesse momento\. O código 2 não é atendido para notas tomadas, porque essas não serão consideradas na seleção\.

Campo obrigatório

Formato: X

Tipo: Texto

Tamanho: 1

MFS\-12392

RN35

__Regra p/ Registro 2 – Notas Fiscais Tomadas – Campo Tipo de Documento__

Preencher com o conteúdo do campo Tipo Docto da parametrização no módulo Parâmetros para Município – Parâmetros – Tipo Docto Msaf x Tipo Docto referente ao código de tipo de documento cadastrado na nota fiscal recebida e ao município que está sendo gerado\.

__Tratamento:__

- Se não houver parametrização, gravar com zero e emitir a seguinte mensagem de log: *“Não existe parametrização de Tipo Docto em Parâmetros para Município, favor verificar\! <<NF>>, <<Série>>, <<Data Emissão>>*\.

Campo obrigatório

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-12392

RN36

__Regra p/ Registro 2 – Notas Fiscais Tomadas – Campo Nota Inicial__

Preencher com o conteúdo do campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\)\.

__Tratamento:__

- Considerar as 9 primeiras posições\.
- Se o campo ultrapassar 9 posições, emitir a mensagem de log:* “O campo número do documento ultrapassou o tamanho máximo permitido \(9 posições\) para Nota Inicial e Final <<NF>>, <<Série>>, <<Data Emissão>>*\.*”*\.

Campo obrigatório

Formato: 999999999

Tipo: Numérico

Tamanho: 9

MFS\-12392

RN37

__Regra p/ Registro 2 – Notas Fiscais Tomadas – Campo Nota Final__

Preencher com o conteúdo do campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\)\.

__Tratamento:__

- Considerar as 9 primeiras posições\.
- Se o campo ultrapassar 9 posições, emitir a mensagem de log:* “O campo número do documento ultrapassou o tamanho máximo permitido \(9 posições\) para Nota Inicial e Final <<NF>>, <<Série>>, <<Data Emissão>>*\.*”*\.

Campo obrigatório

Formato: 999999999

Tipo: Numérico

Tamanho: 9

MFS\-12392

RN38

__Regra p/ Registro 2 – Notas Fiscais Tomadas – Campo Data de Emissão da Nota__

Preencher com o conteúdo do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAFX07\)\.

Campo obrigatório

Formato: AAAAMMDD

Tipo: Data

Tamanho: 8

MFS\-12392

RN39

__Regra p/ Registro 2 – Notas Fiscais Tomadas – Campo Valor Contábil__

Preencher com o conteúdo do campo VLR\_TOT da tabela DWT\_ITENS\_SERV \(campo 15 da SAFX09\)\.

__Tratamento:__

- Truncar campo pela esquerda considerando o tamanho exigido pelo layout sem considerar vírgulas ou pontos\.

Campo obrigatório

Formato: 999999999999

Tipo: Numérico

Tamanho: 12 \(10 inteiros com 2 decimais\)

MFS\-12392

RN40

__Regra p/ Registro 2 – Notas Fiscais Tomadas – Campo Valor Tributável__

Preencher com o conteúdo do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV \(campo 33 da SAFX09\)\.

__Tratamento:__

- Truncar campo pela esquerda considerando o tamanho exigido pelo layout sem considerar vírgulas ou pontos\.
- Se o valor do ISS não estiver preenchido, gravar com zeros e emitir a seguinte mensagem de log: *“O valor do ISS não está preenchido no item da nota fiscal, favor verificar\! <<NF>>, <<Série>>, <<Data Emissão>>”*\.

Campo obrigatório

Formato: 999999999999

Tipo: Numérico

Tamanho: 12 \(10 inteiros com 2 decimais\)

MFS\-12392

RN41

__Regra p/ Registro 2 – Notas Fiscais Tomadas – Campo Observações__

Preencher com o conteúdo do campo OBS\_INF\_ADIC\_NF da tabela DWT\_DOCTO\_FISCAL \(campo 150 da SAFX07\)\.

Campo obrigatório

Formato: XXXXXX\.\.\.

Tipo: Texto

Tamanho: 255

MFS\-12392

RN42

__Regra p/ Registro 2 – Notas Fiscais Tomadas – Campo Alíquota__

Preencher com o conteúdo do campo ALIQ\_TRIBUTO\_ISS da DWT\_ITENS\_SERV \(campo 32 da SAFX09\)\.

__Tratamento:__

- Truncar campo pela esquerda considerando o tamanho exigido pelo layout sem considerar vírgulas ou pontos\.
- Se a alíquota do ISS não estiver preenchida, gravar com zeros e emitir a seguinte mensagem de log: *“A alíquota do ISS não está preenchida no item da nota fiscal, favor verificar\! <<NF>>, <<Série>>, <<Data Emissão>>”*\.

Campo obrigatório

Formato: 99999

Tipo: Numérico

Tamanho: 5 \(3 inteiros com 2 decimais\)

MFS\-12392

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN


# MTZ_ICMS_Convenio_ICMS_201_Geracao_Meio_Magnetico_Fatura

- **Fonte:** MTZ_ICMS_Convenio_ICMS_201_Geracao_Meio_Magnetico_Fatura.docx
- **Modificado:** 2025-10-22
- **Tamanho:** 79 KB

---

THOMSON REUTERS

Geração Arquivo Magnético  
Convênio ICMS 201/2017 – Fatura de Serviços de Comunicação e de Telecomunicações

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-16140

Julyana Perrucini

Este documento tem como objetivo incluir a geração do arquivo magnético auxiliar contendo informações relativas às faturas comerciais, cujos valores superem os respectivos documentos fiscais emitidos, em atendimento ao Convênio ICMS 201/2017\.

MFS25989

Andréa Rocha

Alterar a nomenclatura do arquivo para os clientes que tem o cenário de itens financeiros \(itens que compõe apenas fatura comercial e não compõe nenhuma nota fiscal\)\.

MFS35741

Andréa Rocha

Incluir a geração de faturas para as UFs referenciadas no item da fatura\.

MFS38312

Andréa Rocha

Alterar a forma de gerar as faturas devido à alteração da chave das tabelas SAFX259/SAFX260\.

MFS585776

Andréa Rocha

Alterar a regra de preenchimento dos campos 11\-CNPJ DO PARTICIPANTE e 12\-RAZÃO SOCIAL DO PARTICIPANTE\.

MFS642283

Andréa Rocha

Alteração da geração do arquivo de fatura para tratar o parâmetro criado, que vai definir quais as faturas que devem ser geradas no arquivo\.  Essa alteração está sendo feita para atender a legislação do Convênio 201, que diz que quando as faturas comerciais corresponderem exatamente aos valores dos respectivos documentos fiscais emitidos, não devem ser geradas no arquivo\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN00

__Regras Gerais__

A geração de o arquivo magnético auxiliar referente a fatura de serviços de comunicação e de telecomunicações foi criada pela MFS\-16140 para contribuintes prestadores de serviços de comunicação que emitem seus documentos fiscais nos termos do Convênio ICMS 115/03, que dispõe sobre a uniformização e disciplina a emissão, escrituração, manutenção e prestação das informações dos documentos fiscais emitidos em via única por sistema eletrônico de processamento de dados para contribuintes prestadores de serviços de comunicação e fornecedores de energia elétrica\.

Esse arquivo somente será gerado quando o campo Convênio ICMS 201 – Fatura no item “Gerar Arquivo Auxiliar” estiver marcado na tela de Geração dos Arquivos Magnéticos para o Convênio 115, do módulo ICMS\.

MFS\-16140

RN01

__Dados Técnicos da Geração dos Arquivos__

__*Formato do Arquivo:*__

- Formatação: compatível com MS\-DOS;
- Tamanho do arquivo: 238 bytes, acrescidos de CR/LF \(Carriage Return/Line Feed\) ao final de cada registro;
- Organização: sequencial;
- Codificação: ASCII \- ISO 8859\-1 \(Latin\-1\)\.

MFS\-16140

RN02

__Regra para Identificação do Arquivo__

Se o__ __item “Gerar Arquivo Auxiliar” da tela de Geração dos Arquivos Magnéticos para o Convênio 115 do módulo ICMS estiver marcado com a opção igual a Convênio ICMS 201 – Fatura, os arquivos serão identificados no formato:

__UUCCCCCCCCCCCCCCAAMMMMSSSFCSV\.TXT__

- __UU:__ UF – preencher com sigla da unidade federada do emitente dos documentos fiscais;
- __CCCCCCCCCCCCCC: __CNPJ – preencher com o CNPJ do contribuinte emitente dos documentos fiscais;
- __AA: __Ano – preencher com o ano de emissão dos documentos fiscais;
- __MM: __Mês – preencher com o mês do período de apuração dos documentos fiscais;
- __MM: __Modelo – preencher com o modelo dos documentos fiscais \(verificar observação abaixo\);
- __SSS: __Série – preencher com a série dos documentos fiscais \(verificar observação abaixo\);
- __FC: __Tipo – informação fixa “FC”, significando fatura comercial;
- __S: __Situação – indica se o arquivo é normal \(N\) ou substituto \(S\) de acordo com o status do arquivo principal;
- __V: __Volume – quantidade de registros do arquivo, em que cada volume será composto por até um milhão de faturas comerciais, devendo o volume ser indicado em ordem crescente a partir de 1;
- __\.TXT: __Extensão – a extensão do arquivo deverá ser TXT\.

A quebra do arquivo magnético seguirá com a mesma regra aplicada para o Convênio 60, em que é demonstrada por estabelecimento e Modelo do Documento\. Neste contexto, não se aplica a “Geração para Empresas c/ Inscrição Estadual Única”, uma vez que será gerado um arquivo para cada estabelecimento\. Podemos ter o cenário de seleção do campo “Modelo de Documento para geração” a opção “Todos”\. Se isso ocorrer, deverá ser gerado um arquivo para cada estabelecimento e modelo\. Sempre ocorrerá a quebra do arquivo considerando os campos que compõe a nomenclatura do mesmo\. Será considerada a série e o modelo da SAX42 para essa quebra, sendo que o arquivo gerado deverá conter as faturas que possuírem este modelo e esta série, mas deverá ser gerada a fatura completa, mesmo que um dos itens da fatura não tenha o modelo ou a série, ele tem que ser gerado no arquivo\.  Ou seja, a fatura sempre será gerada no arquivo com todos os seus itens da fatura, mesmo que um dos itens não tenha modelo ou série preenchidos ou com modelo ou série diferentes da quebra do arquivo\.

Obs\.: Para os clientes que possuem o cenário de itens financeiros \(itens que compõe apenas fatura comercial e não compõe nenhuma nota fiscal\), ou seja, para os clientes que não possuírem informação da Nota Fiscal \(número, série e modelo da nota fiscal\) o arquivo deve ser gerado\.  E a nomenclatura do arquivo deverá ser alterada para os dois campos abaixo:

 

- __MM: __Modelo – preencher com ‘00’;
- __SSS: __Série – preencher com ‘000’\.

MFS\-16140/

MFS\-25989

RN03

__Regra p/ Recuperação dos Dados__

__*Origem das Informações para geração:*__

- Tela de Empresa/Estabelecimento do módulo Básicos – Parâmetros \(tabela estabelecimento\), localizado no item de menu: Preliminares >> Empresa/Estabelecimento;
- SAFX259 – aba Capa da tela Fatura de Serviços de Comunicação/Telecomunicações do módulo Básicos – MasterSAF DW, localizado no item de menu: Manutenção Telecom;
- SAFX260 – aba Item da tela Fatura de Serviços de Comunicação/Telecomunicações do módulo Básicos – MasterSAF DW, localizado no item de menu: Manutenção Telecom\.

__*Passo 1: Regra de seleção geral \(SAFX259 e SAFX260\):  *__

Selecionar os registros processados das tabelas dadas como origem, com os seguintes filtros:

- Código da Empresa = Código da Empresa \(relacionado ao Estabelecimento selecionado na tela de geração\);
- Código do Estabelecimento = Código do Estabelecimento selecionado na tela de geração;
- Data de emissão da fatura enquadrada no mês e ano da apuração informada na tela de geração \(campo 04\-DATA\_EMISSAO da SAFX259\);

__\[MFS642283\] __Inclusão da regra para tratar o novo parâmetro criado “Gerar Fatura com o mesmo valor do Doc\. Fiscal”

Se o parâmetro “Gerar Fatura com o mesmo valor do Doc\. Fiscal \(Fatura\)” estiver marcado

      O arquivo será gerado conforme as regras atuais já definidas

Senão

      A fatura só será gerada no arquivo se o Valor Total da Nota Fiscal \(campo 17 da SAFX260\) for diferente do Valor do Item \(campo 18 da SAFX260\)\.

__\[MFS35741\] Inclusão da regra para as UFs referenciadas__

__*Passo 2 : Regra de geração para cada uma das UFs referenciadas no item da fatura \(SAFX260\):*__

A geração do arquivo é feita por UF, então depois de se recuperar todos as faturas do estabelecimento da geração \(passo 1\), deve\-se recuperar as faturas das UFs referenciadas \(passo 2\)\.

A geração será feita para as UFs referenciadas, ou seja, irá gerar as faturas das filiais de outras UFs como faturamento próprio\.  Por exemplo, a fatura \(campo 03 \- Número da Fatura Comercial da SAFX259\) emitida pelo estabelecimento de SP, pode conter faturas oriundas de SP, RJ, PE e PR, para verificar as faturas de outras UFs, utiliza\-se a UF da pessoa física/jurídica do terceiro \(Campos 11 e 12 – Indicador e Código da Pessoa Física/Jurídica do Terceiro da SAFX260\), quando for uma UF igual a da UF do estabelecimento será considerada\.  

Como exemplo, quando se estiver gerando um arquivo para um estabelecimento \(informado em tela\), cuja UF=RJ, deve\-se recuperar todas as faturas do estabelecimento da geração que é feita no passo 1\.  Depois no passo 2, deve\-se recuperar as faturas das UFs referenciadas, ou seja, todas as faturas em que a UF da pessoa física/jurídica do terceiro \(Campos 11 e 12 – Indicador e Código da Pessoa Física/Jurídica do Terceiro da SAFX260\) for igual a “RJ”\.

Selecionar os registros processados das tabelas dadas como origem, com os seguintes filtros:

- Código da Empresa = Código da Empresa;
- Código do Estabelecimento <> Código do Estabelecimento selecionado na tela de geração;
- Data de emissão da fatura enquadrada no mês e ano da apuração informada na tela de geração \(campo 04\-DATA\_EMISSAO da SAFX259\);
- UF da pessoa física/jurídica do terceiro for igual a UF do estabelecimento da geração

Obs\.: Vide exemplo da geração do arquivo para os dois passos na regra RNFS\-Exemplo\.

__*Regra de gravação geral:* __Verificar documento de DEPARA\_Convenio\_ICMS\_201\_Fatura\_e\_Pre\-Pago\.xls \(aba DExPARA FATURA\) para obtenção dos resultados, as regras contidas a seguir são campos que necessitam de tratamento e mensagem de log\.

__*Regra de agrupamento:* __Não se aplica\.

__*Ordenação:* __Ordem crescente por número da fatura e item da fatura\.

__*Considerações:*__ Não se aplica\.

MFS\-16140/

MFS35741/

MFS642283

<a id="_Hlk506977248"></a>RNFS\-02

__Campo 02\-UF__

Se for a geração a partir do passo 1

      Será informado o campo 19\-UF da SAFX04 referente à PFJ informada nos campos 05 \+ 06 da tabela SAFX259 SAFX260

Senão \(passo 2\)

      Será informado o campo UF estabelecimento da geração

__Tratamento:__

- Se o campo UF não estiver preenchido, emitir a seguinte mensagem de log: “O campo da UF não foi preenchido, favor verificar\! <<Nº Fatura>>, <<Data de Emissão>>, <<PFJ Usuário>>\.”\.

MFS\-<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>16140/

MFS35741

MFS38312

<a id="_Hlk506977735"></a>RNFS\-03

__Campo 03\-NOME/RAZÃO SOCIAL DO USUÁRIO__

__Tratamento:__

- Considerar as 35 primeiras posições\.

MFS\-16140

RNFS\-06

__Campo 06\-N° DE ORDEM DO ITEM__

__Tratamento:__

- Considerar as 3 primeiras posições e preencher com zeros à esquerda\.

MFS\-16140

<a id="_Hlk506978187"></a>RNFS\-07

__Campo 07\-CÓDIGO DO ITEM__

__Tratamento:__

- Considerar as 10 primeiras posições\.

MFS\-16140

RNFS\-08

__Campo 08\-DESCRIÇÃO DO ITEM__

__Tratamento:__

- Considerar as 40 primeiras posições\.

MFS\-16140

RNFS\-10

__Campo 10\-ORIGEM DO ITEM__

Se for a geração a partir do passo 1

      Será informado o campo 10\-IND\_ORIGEM\_ITEM da tabela SAFX260

Senão \(passo 2\)

      Se a UF \(referente à PFJ informada nos campos 11 \+ 12 da tabela SAFX260\) for igual a UF do arquivo \(RNFS\-02\)

            O campo será preenchido com “1”

      Senão

           Se PFJ informada nos campos 11 \+ 12 da tabela SAFX260 não estiver preenchida

                  O campo será preenchido com “2”

           Senão

                  Será informado o campo 10\-IND\_ORIGEM\_ITEM da tabela SAFX260

MFS35741

RNFS\-11

__Campo 11\-CNPJ DO PARTICIPANTE__

__\[MFS585776\] __Alteração da regra de preenchimento quando o campo 10 – Origem do Item for igual a “1”

Se o campo 10 – Origem do Item for igual a “1”

      O campo será preenchido com zeros

Senão 

      Se for a geração a partir do passo 1

            Será informado o campo 06\-CPF\_CGC da SAFX04 referente à PFJ informada nos campos 11 \+ 12 da tabela SAFX260

      Senão \(passo 2\)

         Se a UF \(referente à PFJ informada nos campos 11 \+ 12 da tabela SAFX260\) for igual a UF do arquivo \(RNFS\-02\)

                O campo não será preenchido

         Senão

              Se a PFJ informada nos campos 11 \+ 12 da tabela SAFX260 não estiver preenchida

                  Será informado o campo CGC da tabela Estababelecimento referente ao código do estabelecimento \(campo 2 da SAFX259\)

              Senão

                  Será informado o campo 06\-CPF\_CGC da SAFX04 referente à PFJ informada nos campos 11 \+ 12 da tabela SAFX260

MFS35741/

MFS585776

RNFS\-12

__Campo 12\-RAZÃO SOCIAL DO PARTICIPANTE__

__\[MFS585776\] __Alteração da regra de preenchimento quando o campo 10 – Origem do Item for igual a “1”

Se o campo 10 – Origem do Item for igual a “1”

      O campo será preenchido com zeros

Senão

    Se for a geração a partir do passo 1

          Será informado o campo 05\-RAZAO\_SOCIAL da SAFX04 referente à PFJ informada nos campos 11 \+ 12 da tabela SAFX260

    Senão \(passo 2\)

       Se a UF \(referente à PFJ informada nos campos 11 \+ 12 da tabela SAFX260\) for igual a UF do arquivo \(RNFS\-02\)

            O campo não será preenchido

      Senão

            Se a PFJ informada nos campos 11 \+ 12 da tabela SAFX260 não estiver preenchida

                  Será informado o campo RAZAO\_SOCIAL da tabela Estababelecimento referente ao código do estabelecimento \(campo   

                  2 da SAFX259\)

            Senão               

                  Será informado o campo 05\-RAZAO\_SOCIAL da SAFX04 referente à PFJ informada nos campos 11 \+ 12 da tabela   

                  SAFX260

__Tratamento:__

- Considerar as 35 primeiras posições\.

MFS\-16140/

MFS35741/

MFS585776

<a id="_Hlk506992248"></a>RNFS\-16

__Campo 16\-SÉRIE__

__Tratamento:__

- Esse campo deve ser preenchido a partir da esquerda\. *Exemplo:* “A  “\.

MFS\-16140

RNFS\-17

__Campo 17\-N° DA NOTA FISCAL__

__Tratamento:__

- Se o campo estiver preenchido com mais de 10 posições, truncar considerando apenas as 10 primeiras e emitir a mensagem de log: “O campo Nº da Nota Fiscal precisa ter até 10 posições, favo verificar <<Nº Fatura>>, <<Data de Emissão>>, <<PFJ Usuário>>” \.

MFS\-16140

RNFS\-

Exemplo

__Exemplo da geração do arquivo:__

SAFX259:

Estabelecimento da fatura \(Campo 2\) = 001SP, CNPJ = 11\.111\.111/1111\-11, Razão Social= Estabelecimento 001SP e UF = SP

Número da fatura \(Campo 3\) = 001

SAFX260:

Pessoa física/jurídica \(Campos 5 e 6\) = CNPJ 40\.432\.544/0001\-47, Razão Social= Empresa SP e UF = SP

SAFX260:

__ITEM 1 – UF PE__  
Campo 10 \- Origem do Item: 2 \(= Receita de Terceiros\)  
Campo 11 \- Indicador da Pessoa Física/Jurídica do Terceiro: 3 \(= Estabelecimento\)  
Campo 12 \- Código da Pessoa Física/Jurídica do Terceiro: Código da filial 40\.432\.544/0102\-90 

__ITEM 2 – UF PR__  
Campo 10 \- Origem do Item: 2  
Campo 11 \- Indicador da Pessoa Física/Jurídica do Terceiro: 3 \(= Estabelecimento\)  
Campo 12 \- Código da Pessoa Física/Jurídica do Terceiro: Código da filial 40\.432\.544/02224\-69 

__ITEM 3 – UF RJ__  
Campo 10 \- Origem do Item: 2  
Campo 11 \- Indicador da Pessoa Física/Jurídica do Terceiro: 3 \(= Estabelecimento\)  
Campo 12 \- Código da Pessoa Física/Jurídica do Terceiro: Código da filial 40\.432\.544/0062\-69 

__ITEM 4 – UF SP__  
Campo 10 \- Origem do Item: 1  
Campo 11 \- Indicador da Pessoa Física/Jurídica do Terceiro: Vazio  
Campo 12 \- Código da Pessoa Física/Jurídica do Terceiro: Vazio

__ITEM 5 – UF SP__  
Campo 10 \- Origem do Item: 1  
Campo 11 \- Indicador da Pessoa Física/Jurídica do Terceiro: Vazio  
Campo 12 \- Código da Pessoa Física/Jurídica do Terceiro: Vazio

__Geração do arquivo para a UF=SP \(passo 1\): __

Estabelecimento da geração = 001SP

Razão Social = Estabelecimento do SP

CNPJ = 11\.111\.111/1111\-11

UF = SP

Campo 1 \- CPF/CNPJ DO USUÁRIO = 40\.432\.544/0001\-47

__Campo 2 – UF = SP__

Campo 3 \- Razão Social= Empresa SP

Campo 5 – Número da fatura = 001

\.\.\.\.

__ITEM 1 – UF PE__  
Campo 10 \- Origem do Item: 2 \(= Receita de Terceiros\)  
Campo 11 \- CNPJ do participante =__ __40\.432\.544/0102\-90  
Campo 12 \- Razão Social__ __do participante = Código da Pessoa Física/Jurídica do Terceiro: Código da filial 40\.432\.544/0102\-90 

__ITEM 2 – UF PR__  
Campo 10 \- Origem do Item: 2  
Campo 11 \- CNPJ do participante = 40\.432\.544/02224\-69  
Campo 12 \- Razão Social__ __do participante = Código da Pessoa Física/Jurídica do Terceiro: Código da filial 40\.432\.544/02224\-69 

__ITEM 3 – UF RJ__  
Campo 10 \- Origem do Item = 2  
Campo 11 – CNPJ do participante = 40\.432\.544/0062\-69  
Campo 12 \- Razão Social__ __do participante = Código da Pessoa Física/Jurídica do Terceiro: Código da filial 40\.432\.544/0062\-69

__ITEM 4 – UF SP__  
Campo 10 \- Origem do Item: 1  
Campo 11 \- CNPJ do participante = sem preenchimento  
Campo 12 – Razão Social__ __do participante = sem preenchimento__ __

__ITEM 5 – UF SP__  
Campo 10 \- Origem do Item: 1  
Campo 11 \- CNPJ do participante = sem preenchimento  
Campo 12 \- Razão Social__ __do participante = sem preenchimento

__Geração do arquivo para a UF=RJ \(passo 2\):__

Estabelecimento da geração = 001RJ

Razão Social = Estabelecimento do RJ

CNPJ = 22\.222\.222/2222\.22

UF = RJ

Campo 1 \- CPF/CNPJ DO USUÁRIO = 40\.432\.544/0001\-47

__Campo 2 – UF = RJ__

Campo 3 \- Razão Social= Empresa SP

Campo 5 – Número da fatura = 001

\.\.\.\.

__ITEM 1 – UF PE__  
Campo 10 \- Origem do Item: 2 \(= Receita de Terceiros\)  
Campo 11 \- CNPJ do participante =__ __40\.432\.544/0102\-90  
Campo 12 \- Razão Social__ __do participante = Código da Pessoa Física/Jurídica do Terceiro: Código da filial 40\.432\.544/0102\-90 

__ITEM 2 – UF PR__  
Campo 10 \- Origem do Item: 2  
Campo 11 \- CNPJ do participante = 40\.432\.544/02224\-69  
Campo 12 \- Razão Social__ __do participante = Código da Pessoa Física/Jurídica do Terceiro: Código da filial 40\.432\.544/02224\-69 

__ITEM 3 – UF RJ__  
Campo 10 \- Origem do Item = 1  
Campo 11 – CNPJ do participante = sem preenchimento  
Campo 12 \- Razão Social__ __do participante = sem preenchimento

__ITEM 4 – UF SP__  
Campo 10 \- Origem do Item: 2  
Campo 11 \- CNPJ do participante = 11\.111\.111/1111\-11 \(este é o CNPJ da Empresa 001SP de SP que emitiu a fatura principal\)  
Campo 12 – Razão Social__ __do participante = Estabelecimento 001SP \(este é a razão social do estabelecimento que emitiu a fatura principal\)

__ITEM 5 – UF SP__  
Campo 10 \- Origem do Item: 2  
Campo 11 \- CNPJ do participante = 11\.111\.111/1111\-11 \(este é o CNPJ da Empresa A de SP que emitiu a fatura principal\)  
Campo 12 \- Razão Social__ __do participante = Estabelecimento 001SP \(este é a razão social do estabelecimento que emitiu a fatura principal\)

MFS35741

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN


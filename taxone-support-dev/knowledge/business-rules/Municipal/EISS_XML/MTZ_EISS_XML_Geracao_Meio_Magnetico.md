# MTZ_EISS_XML_Geracao_Meio_Magnetico

- **Fonte:** MTZ_EISS_XML_Geracao_Meio_Magnetico.docx
- **Modificado:** 2022-12-28
- **Tamanho:** 92 KB

---

THOMSON REUTERS

Municipal 

 Serviços Tomados 

	Geração do Meio Magnético – EISS\_XML 	

	

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-12581

João Henrique

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Este documento tem como objetivo tratar a geração do meio magnético de serviços tomados em atendimento ao novo validador EISS\_XML\.

MFS\-17809

João Henrique

Este documento tem como objetivo incluir o município de Arapiraca\-AL no validador EISS\_XML\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

__RN01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “São Miguel dos Campos” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: __“Consiste no envio e processamento em lote da declaração das notas de serviços tomados do município de São Miguel dos Campos”\.__

__MFS\-12581__

__RN02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “AL” e ao código de município do IBGE igual a “8600” \(São Miguel dos Campos\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de São Miguel dos Campos, Alagoas\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-12581__

__RN03__

__Estrutura de menus do módulo EISS\_XML__

Deverão ser criados os seguintes menu e sub\-menus no módulo EISS\_XML:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
	- __Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)__
- Janela
- Ajuda 

__MFS\-12581__

__RN04__

__Regra de criação do nome do arquivo:__

__Serviços Tomados:__

__       EISS\_MUNICIPIO\_DDMMAAAA\. XML__, onde:

__       EISS__: representa a obrigação que está sendo gerada\. 

__       MUNICIPIO__: representa o município que está sendo gerado\.

       __DDMMAAAA__: representa a data inicial da geração

       __\.XML__: extensão do arquivo\.

*Exemplo:* EISS\_SAOMIGUELDOSCAMPOS\_01012017\.xml

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__   EISS\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.XML__, onde:

__               EISS__: representa a obrigação que está sendo gerada\.    

__               MUNICIPIO__: representa o município que está sendo gerado\.   

               __DDMMAAAA__: representa a data inicial da geração\.   

__               MMAAAA:__ mês da competência referente à nota gerada

               __\.XML__: extensão do arquivo\.

*Exemplo:* EISS\_SAOMIGUELDOSCAMPOS\_01012017\_122016\.xml 

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.__

__MFS\-12581__

__RN05__

__Regra p/ tela da Geração do Meio Magnético:__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__MFS\-12581__

__RN06__

__Regra p/ Geração do Arquivo Magnético__

- Campos de valor que não houver preenchimento, gravar “0”;
- Campos numéricos que não houver preenchimento, gravar “0”;
- Campos que não possuírem informação deixar TAGS vazias;
- Formato XML

__MFS\-12581__

__RN07__

__Regra p/ Recuperar Notas Fiscais \(o arquivo conterá apenas serviços tomados\):__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)
- Não deve recuperar notas fiscais sem itens\.
- O agrupamento das Notas fiscais será feito através dos campos: __ALIQ\_TRIBUTO\_ISS, ALIQ\_TRIBUTO\_IR, VLR\_ALIQ\_INSS e COD\_SERV\_LEI\_116\.__

__MFS\-12581__

__RN08__

__Estrutura do Arquivo:__

<?xml version="1\.0" encoding="ISO\-8859\-1"?>

<[importacao>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_12581%20-%20SÃO%20MIGUEL%20DOS%20CAMPOS_AL/declaracao_tomador.xml)

      [<nota>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_12581%20-%20SÃO%20MIGUEL%20DOS%20CAMPOS_AL/declaracao_tomador.xml)

            <versao\_xml>1\.1</versao\_xml>

            <doc\_numero>10</doc\_numero>

            <doc\_data>2012\-09\-13</doc\_data>

            <tomador\_nome>NOME EXEMPLO</tomador\_nome>

            <tomador\_cnpjcpf>99\.999\.999/9999\-99</tomador\_cnpjcpf>

            <tomador\_inscrmunicipal>99999</tomador\_inscrmunicipal>

            <tomador\_logradouro>RUA TESTE</tomador\_logradouro>

            <tomador\_numero>99</tomador\_numero>

            <tomador\_complemento>LOT\. TESTE</tomador\_complemento>

            <tomador\_bairro>NOME BAIRRO</tomador\_bairro>

            <tomador\_cep>57000\-000</tomador\_cep>

            <tomador\_municipio>NOMEMUINCIPIO</tomador\_municipio>

            <tomador\_uf>AL</tomador\_uf>

            <simples>S</simples>

            <tomador\_email>[teste@hotmail\.com</tomador\_email](mailto:teste@hotmail.com%3c/tomador_email)>

            <discriminacao>TESTE00000000000000000000</discriminacao>

            <observacao>TESTE11111111111111111111111</observacao>

            <aliqinss>0\.00</aliqinss>

            <aliqirrf>0\.00</aliqirrf>

            <deducaoirrf>0</deducaoirrf>

            <valordeducoes>15\.00</valordeducoes>

            <estado>N</estado>

            [<codservico>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_12581%20-%20SÃO%20MIGUEL%20DOS%20CAMPOS_AL/declaracao_tomador.xml)

                   <codservico>1\.02</codservico>

                   <basecalculo>500\.00</basecalculo>

                   <aliqiss>2\.00</aliqiss>

                   <ssretido>3\.50</ssretido>

             </codservico>

         </nota>

</importação

__MFS\-12581__

__RN09__

__Regra p/ o cabeçalho do arquivo:__

Preencher com a tag <?xml version="1\.0" encoding="ISO\-8859\-1"?> TAG obrigatória\. – Cada arquivo possui uma única declaração\.

__MFS\-12581__

__RN10__

__Regra para o campo <importacao> __Tag relacionada à abertura da formatação do arquivo que deve receber as informações das notas de serviços tomados declaradas pelo município com o texto fixo: __<importacao>__

TAG obrigatória\.

__MFS\-12581__

__RN11__

__Regra para o campo <nota> __Tag relacionada à abertura das informações da nota fiscal com o texto fixo: __<nota>__

TAG obrigatória\.

__MFS\-12581__

__RN12__

__Regra para o campo <versao\_xml> __Tag relacionada à versão com o texto fixo: __”1\.1”__ __</versao\_xml >__

TAG obrigatória\.

__MFS\-12581__

__RN14__

__Regra para o campo <doc\_numero> da TAG </doc\_numero>__

Identifica o número do documento fiscal\. Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL __\(campo 08 da SAFX07\)__

            

Formato: 999999999999

Tipo: Numérico

Tamanho: Não possui tamanho determinado OU manual layout, utilizaremos o campo do MastersafDW\.

__MFS\-12581__

__RN15__

__Regra para o campo <doc\_data> da TAG </doc\_data>__

Identifica a Data da emissão da nota\. Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL __\(campo 11 da SAX07\)__

            

Formato: YYYY\-MM\-DD exemplo: 2017\-10\-27

Tipo: Data

Tamanho: 10 posições 

__MFS\-12581__

__RN16__

__Regra para o campo <tomador\_nome> da TAG </tomador\_nome>__

Identifica o Nome ou a Razão Social do tomador\. Preencher com o campo RAZAO\_SOCIAL da tabela __ESTABELECIMENTO\.__

Formato: XXXXXXXXXXXXXXX\.\.\./ 

Tipo: Alfanumérico

Tamanho: Não possui tamanho determinado OU manual layout, utilizaremos o campo do MastersafDW\.

__MFS\-12581__

__RN17__

__Regra para o campo <tomador\_cnpjcpf> da TAG </tomador\_cnpjcpf>__

Identifica o CNPJ do tomador\. Preencher com o campo CGC da tabela __ESTABELECIMENTO__

__Tratamento:__

- Preencher o campo utilizando a máscara: 99\.999\.999/9999\-99 

Formato: 99\.999\.999/9999\-99 

Tipo: Alfanumérico\. 

Tamanho: 14 posições

__MFS\-12581__

__RN18__

__Regra para o campo <tomador\_inscrmunicipal> da TAG </tomador\_inscrmunicipal>__

Identifica a Inscrição Municipal do tomador\. Preencher com o campo INSC\_MUNICIPAL da tabela __ESTABELECIMENTO\.__

Formato: 99999999999999\.\.\./

Tipo: Numérico

Tamanho: Não possui tamanho determinado OU manual layout, utilizaremos o campo do MastersafDW\.

__MFS\-12581__

__RN19__

__Regra para o campo <tomador\_lougradouro> da TAG </tomador\_lougradouro>__

Identifica o endereço do tomador\. Preencher com o campo ENDERECO da tabela __ESTABELECIMENTO\.__

Formato: XXXXXXXXXXXXXXX *\.\.\.\]*

Tipo: Alfanumérico

Tamanho: Não possui tamanho determinado OU manual layout, utilizaremos o campo do MastersafDW\.

__MFS\-12581__

__RN20__

__Regra para o campo <tomador\_numero> da TAG </tomador\_numero>__

Identifica o número do endereço do tomador\. Preencher com o campo NUM\_ENDERECO da tabela __ESTABELECIMENTO\.__

Formato: XXXXXXXXXX

Tipo: Alfanumérico

Tamanho: Não possui tamanho determinado OU manual layout, utilizaremos o campo do MastersafDW\.

__MFS\-12581__

__RN21__

__Regra para o campo <tomador\_complemento> da TAG </tomador\_complemento>__

Identifica o complemento do endereço do tomador\. Preencher com o campo COMPL\_ENDERECO da tabela __ESTABELECIMENTO\.__

Formato: XXXXXXXXXX *\.\.\.\]*

Tipo: Alfanumérico

Tamanho: Não possui tamanho determinado OU manual layout, utilizaremos o campo do MastersafDW\.

__MFS\-12581__

__RN22__

__Regra para o campo <tomador\_bairro> da TAG </tomador\_bairro>__

Identifica o bairro do tomador\. Preencher com o campo BAIRRO da tabela __ESTABELECIMENTO\.__

Formato: XXXXXXXXXX *\.\.\.\]*

Tipo: Alfanumérico

Tamanho: Não possui tamanho determinado OU manual layout, utilizaremos o campo do MastersafDW\.

__MFS\-12581__

__RN23__

__Regra para o campo <tomador\_cep> da TAG </tomador\_cep>__

Identifica o CEP do tomador\. Preencher com o campo CEP da tabela __ESTABELECIMENTO\.__

__Tratamento:__

- Utilizar máscara no preenchimento do CEP, “99999\-999”\.

Formato: 99999\-999

Tipo: Numérico

Tamanho: 8 posições

__MFS\-12581__

__RN24__

__Regra para o campo <tomador\_municipio> da TAG </tomador\_municipio>__

Identifica o nome do município do tomador\. Através do COD\_MUNICIPIO da tabela __ESTABELECIMENTO__, preencher com a DESCRICAO da tabela MUNICIPIO\.

Formato: XXXXXXXXXX *\.\.\.\]*

Tipo: Alfanumérico

Tamanho: Não possui tamanho determinado OU manual layout, utilizaremos o campo do MastersafDW\.

__MFS\-12581__

__RN25__

__Regra para o campo <tomador\_uf> da TAG </tomador\_uf>__

Identifica a unidade federativa do tomador\. Através do IDENT\_ESTADO da tabela __ESTABELECIMENTO__, preencher com o COD\_ESTADO da tabela ESTADO\.

Formato: XX

Tipo: Alfanumérico

Tamanho: 2 posições

__MFS\-12581__

__RN26__

__Regra para o campo <simples> da TAG </simples>__

Esse campo identifica se o prestador é optante do Simples Nacional\. 

Preencher com:

__“S” \- Sim\.__

Se o campo __IND\_SIMPLES\_NAC__ da tabela X04\_PESSOA\_FIS\_JUR __\(campo 43 da SAFX04\)__ for igual “S” referente o prestador cadastrado na nota fiscal\.

Senão, preencher com:

__“N” \- Não\.__

Formato: 9

Tamanho: 1

Tipo: Numérico

__MFS\-12581__

__RN27__

__Regra p/ tag <tomador\_email> da TAG </tomador\_email>__

Identifica o E\-mail do tomador\. Preencher com o campo E\_MAIL da tabela __ESTABELECIMENTO\.__

Formato: XXXXXXXXXXXXXXXXXXXX *\.\.\.\]*

Tipo: Alfanumérico

Tamanho: Não possui tamanho determinado, utilizaremos o campo do MastersafDW\.

__MFS\-12581__

__RN28__

__Regra para o campo <discriminacao> da TAG </discriminacao> __

Identifica as informações do serviço\. Preencher com o campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao\(s\) serviço\(s\) cadastrado\(s\) no item da nota fiscal\.

Formato: XXXXXXXXXXXXXXXXXX\(\.\.\.\)

Tamanho: 2000 posições \- É permitida a quebra de linha para este campo\.

Tipo: Alfanumérico

__MFS\-12581__

__RN29__

__Regra para o campo <observacao> da TAG </observacao> __

Identifica as observações da nota fiscal\. Preencher com o campo OBS\_INF\_ADIC\_NF da tabela DWT\_DOCTO\_FISCAL __\(campo 150 da SAX07\)__

Formato: XXXXXXXXXXXXXXXXXXXX *\.\.\.\]*

Tipo: Alfanumérico

Tamanho: Não possui tamanho determinado, utilizaremos o campo do MastersafDW\.

__MFS\-12581__

__RN30__

__Regra para o campo <aliqinss> da TAG </aliqinss> __

Identifica a alíquota do INSS\. Preencher com o campo __VLR\_ALIQ\_INSS__ da tabela DWT\_ITENS\_SERV __\(Campo 78 da SAFX09\)__

__Tratamento:__ 

- Nossa tabela permite gravar no tamanho de 7 posições \(3 inteiros/ 4 decimais\), então para atender a obrigação deverá ser desconsiderada a primeira posição do número inteiro e as duas últimas da parte decimal para atender o tamanho normalmente atendido em outras obrigações municipais\.

Formato: 99\.99 

*Exemplo:* 10\.00, 3\.50, utilizar ponto como separador decimal\.

Tamanho: 5 posições 

Tipo: Numérico

__MFS\-12581__

__RN31__

__Regra para o campo <aliqirrf> da TAG </aliqirrf> __

Identifica a alíquota do IRRF\. Preencher com o campo __ALIQ\_TRIBUTO\_IR__ da tabela DWT\_ITENS\_SERV __\(Campo 30 da SAFX09\)__

__Tratamento:__ 

- Nossa tabela permite gravar no tamanho de 7 posições \(3 inteiros/ 4 decimais\), então para atender a obrigação deverá ser desconsiderada a primeira posição do número inteiro e as duas últimas da parte decimal para atender o tamanho normalmente atendido em outras obrigações municipais\.

Formato: 99\.99 

*Exemplo:* 10\.00, 3\.50, utilizar ponto como separador decimal\.

Tamanho: 5 posições 

Tipo: Numérico

__MFS\-12581__

__RN32__

__Regra para o campo <deducaoirrf> da TAG </deducaoirrf> __

__Observação:__ Não será tratado na demanda, gravar com o valor __“0”__ conforme o exemplo do XML\.

__MFS\-12581__

__RN33__

__Regra para o campo <valordeducoes> da TAG </valordeducoes> __

Identifica o valor de deduções da Nota fiscal\. Preencher com o somatório do campo __VLR\_DEDUCAO\_ISS __da tabela DWT\_ITENS\_SERV __\(Campo 59 da SAFX09\)\.__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), como não possui manual de layout para construção do validador, vamos considerar o tamanho da nossa tabela\.

 

Formato: 999999999999999\.99 \- utilizar ponto como separador decimal\.

Tamanho: Não possui tamanho determinado, utilizaremos o campo do MastersafDW

Tipo: Numérico\.

__MFS\-12581__

__RN34__

__Regra para o campo <estado> da TAG </estado> __

__Observação:__ Como não temos apoio e layout da obrigação enviado pelo cliente/prefeitura para esse campo gerar fixo com o valor __“N”, __conforme XML enviado\.

__MFS\-12581__

__RN35__

__Regra para o campo <codservico> __Tag relacionada á abertura das informações do serviço da nota fiscal com o texto fixo: __<codservico>__

TAG obrigatória\.

__MFS\-12581__

__RN36__

__Regra para o campo <codservico> da TAG </codservico> __

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\.

__Tratamento:__

Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, deverá ser gravado com 00\.00 \(zeros\) e emitida à mensagem de log: O código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal não está preenchido, favor verificar\.

Formato: 99\.99

Tipo: Numérico

Tamanho: 5

__MFS\-12581__

__RN37__

__Regra para o campo <basecalculo> da TAG </basecalculo> __

Esse campo identifica a base de cálculo do serviço\. Preencher com o somatório do campo __VLR\_BASE\_ISS\_1 OU VLR\_BASE\_ISS\_2__ da tabela __DWT\_ITENS\_SERV__\.

__Observação:__ No item da NF não permite o preenchimento das duas bases, ou seja, será preenchida uma ou outra\.

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), como não possui manual de layout para construção do validador, vamos considerar o tamanho da nossa tabela\.

 

Formato: 999999999999999\.99 \- utilizar ponto como separador decimal\.

Tamanho: Não possui tamanho determinado, utilizaremos o campo do MastersafDW

Tipo: Numérico

__MFS\-12581__

__RN38__

__Regra para o campo <aliqiss> da TAG </aliqiss>__

Esse campo identifica a alíquota do ISS\. Preencher com o campo __ALIQ\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV\.__

__Tratamento:__ 

- Nossa tabela permite gravar no tamanho de 7 posições \(3 inteiros/ 4 decimais\), então para atender a obrigação deverá ser desconsiderada a primeira posição do número inteiro e as duas últimas da parte decimal para atender o tamanho normalmente atendido em outras obrigações municipais\.

Formato: 99\.99 

*Exemplo:* 10\.00, 3\.50, utilizar ponto como separador decimal\.

Tamanho: 5 posições 

Tipo: Numérico

__MFS\-12581__

__RN39__

__Regra para o campo <ssretido> da TAG </ssretido>__

Esse campo identifica o valor do ISSQN retido\. Preencher com o somatório do campo __VLR\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV__\.

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), como não possui manual de layout para construção do validador, vamos considerar o tamanho da nossa tabela\.

 

Formato: 999999999999999\.99 \- utilizar ponto como separador decimal\.

Tamanho: Não possui tamanho determinado, utilizaremos o campo do MastersafDW

Tipo: Numérico

__MFS\-12581__

__RN40__

__Regra para o campo </codservico> __Tag relacionada ao encerramento das informações do serviço da nota fiscal com o texto fixo: __</codservico>__

TAG obrigatória\.

__MFS\-12581__

__RN41__

__Regra para o campo </nota> __Tag relacionada ao encerramento das informações da nota fiscal com o texto fixo: __</nota>__

TAG obrigatória\.

__MFS\-12581__

__RN42__

__Regra para o campo </importacao> __Tag relacionada ao encerramento da formatação do arquivo que deve receber as informações das notas de serviços tomados declaradas pelo município com o texto fixo: __</importacao>__

TAG obrigatória\.

__MFS\-12581__

__RN43__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Arapiraca” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: __“Consiste no envio e processamento em lote da declaração das notas de serviços tomados do município de Arapiraca”\.__

__MFS\-17809__

__RN44__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “AL” e ao código de município do IBGE igual a “300” \(Arapiraca\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Arapiraca, Alagoas\. Alguns dados não estarão disponíveis\. Deseja continuar? ”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-17809__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

	


# MTZ_DES_e_Geracao_Meio_Magnetico

- **Fonte:** MTZ_DES_e_Geracao_Meio_Magnetico.docx
- **Modificado:** 2026-02-13
- **Tamanho:** 85 KB

---

THOMSON REUTERS

Municipal 

 Serviços Tomados 

                                    Geração do Meio Magnético – DES\-e	

	

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS26915

Andréa Rocha

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Este documento tem como objetivo tratar a geração do meio magnético de serviços tomados em atendimento ao novo validador DES\-e\.

MFS\-907296

Rosemeire Santos

Este documento tem como objetivo incluir o município São Gonçalo/RJ, na geração do meio magnético de serviços tomados no validador DES\-e\.

MFS\-922990

Rosemeire Santos

Este documento tem como objetivo incluir o município Governador Valadares/MG, na geração do meio magnético de serviços tomados no validador DES\-e\.

MFS\-978755

Rafael Fabiano

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para os municípios atendidos pelo validador DES\-e\.

__MFS\-1041437__

Rosemeire Santos

Este documento tem como objetivo ajustar a regra __RN14__, do campo __Código do Serviço \(LC116__\), para desconsiderar os zeros a esquerda no preenchimento para código serviço da Lei, do validador DES\-e\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

__RN01__

__Regra p/ inclusão dos novos módulos no Manager:__

O novo módulo: “Ilhéus” devem ficar localizados no grupo “Municipal”\.

A descrição funcional do módulo será: __*“Consiste na entrega das informações sobre os serviços tomados do município de Ilhéus”\.*__

__MFS26915__

__RN02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “BA” e ao código de município do IBGE igual a: “13606” \(Ilhéus\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

__Exemplo:__ “Este estabelecimento não pertence ao município de Ilhéus\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS26915__

__RN03__

__Estrutura de menus do módulo __

Deverão ser criados os seguintes menus e sub\-menus no módulo DES\-e:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
	- <a id="_Hlk207011407"></a>__Arquivo de Entradas de Serviços \(Const\. Civil/Utilities /Telecom\)__
- Janela
- Ajuda 

__MFS26915__

__MFS\-978755__

__RN04__

__Regra de criação do nome do arquivo:__

__Serviços Tomados:__

__   EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\.CSV__, onde:

       __MMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __ESTABELECIMENTO: __representa estabelecimento do Tomador\.

       __EMPRESA__: representa a empresa do Tomador\. 

       __\.CSV__: extensão do arquivo\.

*Exemplo:* Empresa\_Estabelecimento\_Municipio\_012010\.CSV

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO \_MMAAAA\_MMAAAA\.CSV__, onde:

       __MMAAAA: __representa a mês da geração

__       MMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __ESTABELECIMENTO: __representa estabelecimento do Tomador\.

       __EMPRESA__: representa a empresa do Tomador\. 

       __\.CSV__: extensão do arquivo\.

*Exemplo:* Empresa\_Estabelecimento\_Municipio\_012010\_012010\.CSV

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__MFS26915__

__MFS\-907296__

__RN05__

__Regra p/ tela da Geração do Meio Magnético:__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__MFS26915__

__RN06__

__Regra p/ Geração do Arquivo Magnético__

1. O formato do arquivo será em CSV\. Neste formato, os campos são separados por “;” \(ponto e vírgula\)\.
2. Todos os campos do tipo \(Data\) têm o formado no padrão DDMMAAAA\.
3. Todos os campos do tipo \(Alfanumérico\) são preenchidos com espaços em branco à direita quando não alcançar o tamanho exato do campo\.
4. Todos os campos do tipo \(Numérico\) são preenchidos com zeros à esquerda quando não alcançar o tamanho exato do campo\.

__*Observação:*__ Para os campos numéricos nenhum separador de milhar e decimal devem ser informados\.

__MFS26915__

__RN06\.a__

__Regra p/ Geração do Arquivo Magnético – Município de São Gonçalo/RJ e Governador Valadares/MG\.__

O formato do arquivo deve ser no formato CSV, e todos os campos deverão ser separados por “,” \(vírgula\) e devem ser individualmente, envolvidos por “ ” \(aspas duplas\)\.

__A ordem dos campos deve ser a seguinte:__

1 – CPF ou CNPJ do Prestador de Serviços – Apenas números

2 – Nome ou Razão Social do Prestador

3 – Tipo do Documento

	 nf

	 rps

	 rpa

4 – Número Inicial da Nota Fiscal \- Apenas números

5 – Séries da Nota Fiscal – Não é campo obrigatório

6 – Data do Serviço – No formato DD/MM/YYYY

7 – Código do Serviço \(LC116\) – com pontuacao, ex: 7\.02

8 – Alíquota \- Padrão Nacional, decimal separado por vírgula\.

9 – Valor do Serviço \(Base de Cálculo\) \- Padrão Nacional, decimal separado por vírgula\.

10 – Situação da Nota Fiscal

	 t  =  Tributada

	 r  =  Retida

	 i  =  Isenta

11 – Serviço Prestado por empresa no exterior

	 s  =  Sim

	 n  =  Não

__NOTA:__ Todos os campos são obrigatórios, exceto o campo 5 \(Série da Nota Fiscal\), se o campo não for informado, é necessário que o mesmo seja enviado em branco, ou seja, na posição 6, deve vir duas vírgulas “,”\.

__Exemplos:__

1\) Linha com todos os campos preenchidos

	

	"50275182000181","razao social teste","nf","1","A","01/05/2020","3\.02","5","45,8","t","n"

2\) Linha SEM campo ‘Série da Nota Fiscal’

	"50275182000181","razao social teste","nf","1",,"01/05/2020","1\.01","5","100,99","t","n"

__MFS\-907296__

__MFS\-922990__

__RN07__

__Regra p/ Recuperar Notas Fiscais \(o arquivo conterá apenas serviços tomados\):__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)
- Não deve recuperar notas fiscais sem itens\.
- Recuperar apenas notas fiscais com retenção do ISS \(campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV > 0\)

__MFS26915__

__MFS\-907296__

__RN08__

__Regra para o campo CNPJ Prestador__

Preencher com o conteúdo do campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Tipo: Numérico

Campo Obrigatório

__MFS26915__

__MFS\-907296__

__RN09__

__Regra para o campo Nome Prestador__

Preencher com o conteúdo campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente <a id="OLE_LINK18"></a><a id="OLE_LINK19"></a><a id="OLE_LINK20"></a>a pessoa fis/jur cadastrada na nota\.__ __

Tipo: Alfanumérico

Campo Obrigatório

__MFS26915__

__MFS\-907296__

__RN10__

__Regra p/ campo Registro de Serviços Tomados – Tipo do Documento__

Preencher com o campo Tipo Documento da tela de parametrização: __\(TFIX84\) __Parâmetros por município – Tipo Docto Msaf x Tipo Docto\.

Campo Obrigatório

__MFS\-907296__

__RN11__

__Regra para o campo Número do Documento Número Inicial da Nota Fiscal__

Preencher com o campo __08 \- NUM\_DOCFIS \(SAFX07\)__ da tabela __DWT\_DOCTO\_FISCAL\.__

Tipo: Numérico

Campo Obrigatório

__MFS26915__

__MFS\-907296__

__RN12__

__Regra para o campo Séries da Nota Fiscal__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. 

Campo alfanumérico\.

Campo não obrigatório

__MFS\-907296__

__RN13__

__Regra para o campo Data do serviço__ 

Preencher com o campo __11 \-__ __DATA\_EMISSAO \(SAFX07\)__ da tabela __DWT\_DOCTO\_FISCAL\.__

Formato: DD/MM/AAAA

Tipo: Data

Campo Obrigatório

__MFS26915__

__MFS\-907296__

__RN14__

__Regra para o campo Código do Serviço \(LC116\)__

Preencher com o campo __COD\_SERV\_LEI\_116__ da tabela __DWT\_SERVICO\_LEI\_116__ referente ao serviço cadastrado no item da nota fiscal\. Sem os zeros a esquerda\.

Formato: 7\.02

Tipo: Numérico

Campo Obrigatório

__MFS\-907296__

__MFS\-1041437__

__RN15__

__Regra para o campo Alíquota__

Nesse campo será informado o valor da Alíquota do ISS, Padrão Nacional, decimal separado por vírgula\. Preencher com o campo __ALIQ\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV__\. 

Tipo: Numérico Decimal

Campo Obrigatório

__MFS\-907296__

__RN16__

__Regra para o campo Valor do Serviço \(Base de Cálculo\)__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. Formato: Decimal separado por vírgula\. 

Campo numérico\.

Campo Obrigatório

Nesse campo será informado o valor da NF, valor com duas casas decimais, sem separador de milhar e decimal\. Preencher com o campo __VLR\_TOT__ da tabela __DWT\_ITENS\_SERV\.__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

Tipo: Numérico Decimal

__MFS26915__

__MFS\-907296__

__RN13__

__Regra para o campo Valor Deduções __

Nesse campo será informado o valor das deduções, valor com duas casas decimais, sem separador de milhar e decimal\.  Preencher com o conteúdo do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV \(campo 59 da SAFX09\)\.

Formato: 999999999999999

Tamanho: 15 posições

Tipo: Numérico Decimal__ __

__MFS26915__

__RN14__

__Regra para o campo Alíquota__

Nesse campo será informado o valor da Alíquota do ISS, Padrão Nacional, decimal separado por vírgula\. Preencher com o campo __ALIQ\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV__\. 

Tipo: Numérico Decimal

__MFS26915__

__RN15__

__Regra para o campo Item de Serviço__ 

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado no item da nota fiscal\.

Formato: Com pontuacao, ex: 7\.02

Tamanho: 4 posições 

Tipo: Numérico

__MFS26915__

__RN16__

__Regra para o campo Discriminação dos Serviços__

Preencher com o conteúdo do campo DESCRICAO da tabela X2018\_SERVICOS referente ao serviço cadastrado no item da nota\.

Formato: XXXXXXXXXXXXXXXXXXXXX 

Tamanho: 50 posições 

Tipo: Alfanumérico

__MFS26915__

__RN17__

__Regra para o campo – Situação da Nota Fiscal __

Preencher com:

__r __\- \(Retida\), quando pelo menos umas das seguintes opções seja verdadeira:

- Verificar se o campo __IND\_TP\_RET__ da tabela __DWT\_DOCTO\_FISCAL__ está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”\.
- Verificar se na tabela __X2098\_ALIQ\_SERVICO__, o campo __IND\_TOM\_TRIBUT\_ISS = “S”__ para o serviço cadastrado na nota e utilizando o campo __COD\_MUNIC\_ISS__ da tabela __ESTABELECIMENTO\.__
- Verificar se o campo __VLR\_ISS\_RETIDO__ da tabela __DWT\_ITENS\_SERV__ está preenchido\.

__t __\- \(Tributada\), quando o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota está parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “445”\.

__i __\- \(Isenta\), quando o campo __IND\_CLASSE\_PFJ__ da tabela __X04\_PESSOA\_FIS\_JUR = “10”, __se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\. 

Campo Obrigatório

__MFS\-907296__

__RN18__

__Regra para o campo \- Serviço Prestado por empresa no exterior__

Se o município informado no campo __COD\_MUNICIPIO__ da __DWT\_DOCTO\_FISCAL__ for diferente da UF = ‘EX’ – Preencher N = Não

Se o município informado no campo __COD\_MUNICIPIO__ da __DWT\_DOCTO\_FISCAL__ for igual a UF = ‘EX’ – Preencher S = Sim

Campo: Obrigatório 

__MFS\-907296__

__RN19__

__Regra p/ inclusão dos novos módulos no Manager:__

__Modulo existente__

O módulo: “São Gonçalo” devem ficar localizados no grupo “Municipal”\.

A descrição funcional do módulo será: __“Consiste na entrega das informações sobre os serviços tomados do município de São Gonçalo”\.__

__MFS\-907296__

__RN20__

__Regra p/ abertura do módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RJ” e ao código de município do IBGE igual a: “4904” \(São Gonçalo\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

__Exemplo:__ “Este estabelecimento não pertence ao município de São Gonçalo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-907296__

__RN21__

__Regra p/ inclusão dos novos módulos no Manager:__

__Modulo existente__

O módulo: “Governador Valadares” devem ficar localizados no grupo “Municipal”\.

A descrição funcional do módulo será: __“Consiste na entrega das informações sobre os serviços tomados do município de Governador Valadares”\.__

__MFS\-922990__

__RN22__

__Regra p/ abertura do módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “MG” e ao código de município do IBGE igual a: “27701” \(Governador Valadares\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

__Exemplo:__ “Este estabelecimento não pertence ao município de Governador Valadares\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-922990__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN


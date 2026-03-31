# MTZ-Porto_Alegre_Geracao_Meio_Magnetico

- **Fonte:** MTZ-Porto_Alegre_Geracao_Meio_Magnetico.docx
- **Modificado:** 2026-01-23
- **Tamanho:** 94 KB

---

# 	

# ISSQN Porto Alegre \- Geração do Meio Magnético

__Atenção: Regras ajustadas estão no novo documento de regras dos módulos municipais – DE\-PARA – Municipal\.xls\.__

__Documento disponível no diretório do CVS: documentacao funcional\\Documento Matriz\\Municipal\\Regras Gerais__

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS2542

Geração do Meio Magnético ISSQN Porto Alegre

Deverá ser criado um novo módulo que permita a geração do meio magnético ISSQN Porto Alegre em que serão informados os documentos fiscais de serviço prestados \(emitidos\) e tomados \(recebidos\), assim como a geração de um Relatório de Conferência e o Log de Processos\.

OS3119

Atualização de versão

Este documento tem por objetivo atualizar o módulo “ISSQN Porto alegre” para a versão 8\.28\.00\.

OS3192\-G

ISSQN Porto Alegre \- Permitir geração do meio magnético por data inicial e final

Este documento tem por objetivo alterar a tela de geração do meio magnético da ISSQN Porto Alegre permitindo ao usuário realizar a geração informando a data inicial e data final da apuração\.

CH88137

Gerar inscrição municipal e CNPJ do substituto\.

Este documento tem o objetivo de preencher os campos Inscrição Municipal e CNPJ do substituto de acordo com o manual de layout tanto para registros de serviços tomados quanto para os registros de serviços prestados\.

CH42079\-B

DW \- Municipal \- ISSQN Porto Alegre \- Geração Incorreta do CNPJ Substituto Tributário e Valor do imposto retido por ST

O objetivo deste documento é realizar o preenchimento correto dos campos referentes a substituição tributária dos registros de serviços prestados e tomados\.

CH96094

Alteração nas Regras de Geração do arquivo para Serviços Prestados e tomadores\.

Esse chamado tem por objetivo alterar a geração do meio magnético para que quando os itens da nota fiscal tiverem a mesma alíquota, devem ser agrupados em um único registro\.

CH101934

Alteração na série do documento

Esse chamado tem por objetivo alterar a série do documento fiscal quando o campo for preenchido como “U”\.

CH115151

DW \- MUNICIPAL \- ISS \- ISSQN Porto Alegre alteração de versão 8\.47\.00\.

Alterar a geração do Meio Magnético para incluir as alterações previstas na atualização 8\.47\.00 do manual de layout

CH119713

Alteração na regra de recuperação do campo Data do documento e inclusão de regra geral para recuperação dos dados

Este chamado tem por objetivo alterar a forma de recuperação dos documentos no período filtrando por data fiscal e alterar a regra para geração do campo ‘Data do documento’, preenchendo com a data de emissão\.

OS3537

DW \- MUNICIPAL \- ISS \- Atualização legal ISSQNDec versão 8\.49\.00\.

Este documento tem como objetivo alterar a geração do Meio Magnético do município de Porto Alegre para que o mesmo passe a considerar as alterações da versão 8\.49\.00\. 

OS3537\-A

DW \- MUNICIPAL \- ISS – Reestruturação do módulo Porto Alegre

Este documento tem como objetivo alterar a geração do Meio Magnético do município de Porto Alegre para que o mesmo passe a considerar as alterações da versão 8\.49\.00\. Além disso, a geração será reestruturada para que a mesma fique de acordo com a nova estrutura do grupo Municipal\.

CH8304\_2012

MUNICIPAL \- PORTO ALEGRE \- Geração campo Imposto Retido por Substituição Tributária incorreto

Este documento tem como objetivo ajustar a regra de geração das informações referentes ao imposto retido dos serviços tomados\.

OS3626

Ajuste para quebra de arquivo por data de competência

Este documento tem por objetivo alterar a geração do meio magnético de Porto Alegre para permitir que se dentro do período gerado, existam notas com data de emissão fora do mês gerado a geração deve criar arquivos magnéticos separados para essas notas, sendo um arquivo para cada mês \(competência\)\.

CH17758

Geração campos Imposto Retido e Aliquota de imposto retido incorreta\.

Este documento tem como objetivo ajustar a regra para recuperação de valor de imposto e alíquota para ST e CPOM\.

OS3537\-B

Ajuste da regra do campo Matricula da obra de Serviços Tomados e atendimento a situação de CPOM\.

Este documento tem como objetivo ajustar a regra para a geração da Matricula da Obra de Serviços Tomados e também a regra de recuperação dos campos de Imposto e Alíquota ST e 

Imposto e Alíquota sem cadastro no CPOM\. 

CH19076

Ajuste da regra Alíquota Substituição Tributária

Este documento tem como objetivo ajustar a regra para a geração da alíquota de Substituição Tributária para os serviços tomados, deve ser considerada duas casas decimais após a vígula no caso de prestadores optantes pelo simples nacional, no caso de não optantes, deve ser considerada apenas uma casa decimal\.

Ch19076\-A

Ajuste da regra Alíquota Substituição Tributária

Este documento tem como objetivo ajustar a regra de geração d alíquota, quando for do Simples Nacional, para que arredonde o valor, de acordo com o validador\.

CH22331

Alteração na geração da Data de pagamento

Este documento tem como objetivo ajustar a geração do campo Data de Pagamento do registro de serviços tomados\.

CH19076\-B

Ajuste do Campo Alíquota de imposto retido por falta de cadastramento no CPOM para Empresas Optantes pelo Simples Nacional

Este documento tem como objetivo ajustar a geração do campo Alíquota de imposto retido por falta de cadastramento no CPOM para Optantes pelo Simples Nacional\.

CH1705\_2013

DW \- MUNICIPAL \- PORTO ALEGRE \- Os campos 12 \- inscrição municipal  e 14 CNPJ\_ST devem ser gerado igual a vazio

Este chamado tem por objetivo alterar o preenchimento dos campos Inscrição Municipal do Substituto e CNPJ do Substituto para que o mesmo passe a ser preenchido com brancos quando não houver retenção do ISS na fonte pelo tomador\.

CH17298\_2014

DW \- MUNICIPAL \- PORTO ALEGRE – Alteração do campo Série do Documento da Relação de Serviços Prestados

Este documento tem como objetivo alterar o campo Série do Documento da relação de Serviços Prestados para considerar também como “ÚNICA” quando não houver o preenchimento da série no sistema\.

CH17460\_2014

DW \- MUNICIPAL \- PORTO ALEGRE – Alteração do campo Data de Pagamento da Relação de Serviços Tomados

Este documento tem como objetivo alterar o campo Data de Pagamento da relação de Serviços Tomados considerando a data de competência de envio\.

OS4815

DW \- MUNICIPAL \- PORTO ALEGRE – Alteração geral para Tipo de Escrituração

<a id="OLE_LINK29"></a><a id="OLE_LINK30"></a>Este documento tem como objetivo alterar a geração do arquivo magnético do módulo Municipal >> Porto Alegre, em atendimento ao ISSQNDec, para casos em que o contribuinte possui mais de um tipo de escrituração a declarar\.

CH19353\_2015

DW \- MUNICIPAL \- PORTO ALEGRE – Alteração para desconsiderar nota eletrônica para prestadores de Porto Alegre

Este documento tem como objetivo alterar a geração da declaração para desconsiderar nota eletrônica para prestadores de Porto Alegre\.

MFS\_2071

DW \- MUNICIPAL – ISSQN Porto Alegre – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

CH20610\_2016

DW \- MUNICIPAL \- PORTO ALEGRE – Alteração do preenchimento dos campos: Alíquota da substituição tributária, Imposto retido por substituição tributária, Inscrição Municipal do Substituído/Prestador, Imposto retido por falta de cadastro no CPOM e Alíquota de imposto retido por falta de cadastramento no CPOM

Este documento tem como objetivo alterar o preenchimento dos campos: Alíquota da substituição tributária, Imposto retido por substituição tributária, Inscrição Municipal do Substituído/Prestador, Imposto retido por falta de cadastro no CPOM e Alíquota de imposto retido por falta de cadastramento no CPOM; da Relação de Serviços Tomados\.

CH20512\_2017

\(MFS\-14614\)

DW \- MUNICIPAL \- PORTO ALEGRE – Alteração no preenchimento do campo Inscrição Municipal do Substituído/Prestador da Relação de Serviços Tomados

Este documento tem como objetivo alterar o preenchimento do campo Inscrição Municipal do Substituído/Prestador da Relação de Serviços Tomados para considerar somente aos estabelecidos no município de Porto Alegre\.

MFS\-46492

DW \- MUNICIPAL \- PORTO ALEGRE – Inclusão do código 16\.02\.

Este documento tem o objetivo de incluir o código 16\.02 na regra de preenchimento de serviços Tomados para as regras:  RN43 e RN44 / RN54 e RN55\.

__Obs\*__ O código, 16\.02, foi incluído pela Lei Complementar nº 157, de 2016\.

MFS\-94101

Rogério Ohashi

Este documento tem o objetivo de incluir o tratamento para preencher com zeros, os Campos \(RN54\) Imposto retido por falta de cadastro no CPOM e \(RN55\) Alíquota de imposto retido por falta de cadastramento no CPOM, que foram descontinuados pelo layout \(CPOM\)\.

MFS\-534050

Rogério Ohashi

Este documento tem o objetivo de incluir o parâmetro “*Tratamento p/ Empresas Substituto Tributário no município \(Art\. 1ª Lei Complementar 306/93*” e readequar a regra de geração dos Campos de Alíquota e Valor de ISS Retido de Substituição Tributária\. \(__RN43 e RN44\)\.__

MFS\-874080

Andréa Rocha

Este documento tem o objetivo de incluir o parâmetro “*Tratamento p/ Empresas Substituto Tributário no município – Construção Civil*” e readequar a regra de geração dos Campos de Alíquota e Valor de ISS Retido de Substituição Tributária\. \(__RN43 e RN44\)\.__

MFS\-829438     

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Porto Alegre” deve ficar localizado no grupo “Municipal”\.

OS3537\-A/OS2542

__RN02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RS” e ao código de município do IBGE igual a “14902” \(Porto Alegre\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Porto Alegre, Rio Grande do Sul\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS3537\-A/OS2542__

__RN03__

__Estrutura de menus do módulo Porto Alegre:__

__\[ALTERADA – OS4815\]__

Deverão ser criados os seguintes menus e sub\-menus no módulo Porto Alegre:

- Arquivo
- Parâmetros
- Tipo Docto Msaf x Tipo Docto ISSQN
- Tipo Docto Msaf x Tipo Docto ISSQN – Ded\. Material
- Classificação de Serviços
- Canal Distrib\./Obras x Seqüencial
- Remessa
	- 
		- Tipo de Escrituração p/ Serviços Prestados
		- Tipo de Escrituração p/ Serviços Tomados
- Obrigações
	- Geração do Meio Magnético
	- Arquivo de Entradas de Serviços \(Const\. Civil/Utilities/Telecom\)
- Janela
- Ajuda

__OS3537\-A/OS2542__

__OS4815__

__RN04__

__Regra de criação do nome do arquivo__

Deverá ser gerado um arquivo para cada tipo de registro\. Um para serviços prestados e outro para serviços tomados\.

O arquivo deverá ser gerado da seguinte forma:

Para serviços prestados:

__SP\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ MMAAAA\.TXT__, onde:

       __SP__: Apenas registros de serviços prestados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: SP\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\.TXT

     __SP\_PORTOALEGRE\_DDMMAAAA\.txt__, onde:

     __SP__: significa que é um arquivo de serviços prestados

__     PORTOALEGRE: __indica que  é um arquivo da ISSQN Porto Alegre

     __DDMMAAAA__: data inicial da geração

    \.__txt__: extensão do arquivo

Para serviços tomados:

Se dentro do período de geração apenas houverem notas fiscais com data de emissão dentro do período, a nomenclatura do arquivo deve ser:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\.TXT

     __ST\_ PORTOALEGRE \_DDMMAAAA\.txt__, onde:

     __ST__: significa que é um arquivo de serviços tomados

__     PORTOALEGRE: __indica que  é um arquivo da ISSQN Porto Alegre

     __DDMMAAAA__: data inicial da geração

    \.__txt__: extensão do arquivo

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente a data de emissão da nota fiscal\. Esse arquivo deve conter todas as notas fiscais que tenham a mesma competência \(mesmo mês referente a data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deve ser:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\_ MMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial da geração

__MMAAAA:__ mês da competência referente à nota gerada\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_012010\.TXT

__     ST\_ PORTOALEGRE \_DDMMAAAA\_MMAAAA\.txt__, onde:

     __ST__: significa que é um arquivo de serviços tomados

__     PORTOALEGRE: __indica que  é um arquivo da ISSQN Porto Alegre

     __DDMMAAAA__: data inicial da geração

__     MMAAAA:__ mês da competência referente a nota gerada

    \.__txt__: extensão do arquivo

__OS3537\-A/OS2542__

__/__

__OS3626__

__MFS\-829438      __

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

__Tipo de Escrituração:__ deve ser exibido através de um ListBox, com as seguintes opções: 

1      Receita Bruta

2      Agencia de Publicidade e Propaganda

3      Agencia de Viagem e Operadora de Turismo

4      Subst\. Trib\. Não Prestador de Serviços \- Seg\./Cia\.Aérea e Outros

5      Órgão da Adm\. Pública \(não prestador de serviços\)

1. Sociedade de Profissionais
2. Táxi e Transporte Escolar
3.  Regime especial de Emissão \- Banco/Financeira/Corretora e outros

10      Emissor de Cupom Fiscal

11     Construção Civil / Incorporação Imobiliária

1. Entidade Imune / Isenta
2. Demais Empresas

14     Regime de Estimativa

15     Receita Bruta com Redução de Base de Cálculo

16     Simples Nacional

17     Planos de saúde

18     Salões de beleza, barbearias e congêneres

1. Escritório de Contabilidade – Simples Nacional

__Gerar Serviços Prestados:__ deve ser exibido através de um checkbox com as seguintes opções: “S” – Marcado, irá gerar os registros de serviços prestados e “N” – Desmarcado, não irá gerar os registros de serviços prestados\.

__Gerar Serviços Tomados:__ deve ser exibido através de um checkbox com as seguintes opções: “S” – Marcado, irá gerar os registros de serviços tomados e “N” – Desmarcado, não irá gerar os registros de serviços tomados\.

__Tratamento p/ Empresas Substituto Tributário no município \(Art\. 1ª Lei Complementar 306/93\):__ deve ser exibido através de um checkbox com as seguintes opções: “S” – Marcado, irá gerar os valores dos Campos de Alíquota e Valor de ISS Retiro da Substituição Tributária para todos os Código de Serviço da Lei Complementar 116, se desmarcado o sistema deverá continuar gerando conforme regra atual\.

Default: Desmarcado

__\[MFS874080\] Tratamento para particularidade da Construção Civil na geração normal__

__Tratamento p/ Empresas Substituto Tributário – Construção Civil:__ deve ser exibido através de um checkbox com as seguintes opções: “S” – Marcado, não irá preencher os valores dos Campos de Alíquota e Valor de ISS Retido da Substituição Tributária, quando o município da nota fiscal for diferente de Porto Alegre\. Se desmarcado, o sistema deverá continuar gerando conforme regra atual\.

Default: Desmarcado

Se o parâmetro “Tratamento p/ Empresas Substituto Tributário no município \(Art\. 1ª Lei Complementar 306/93\)” estiver marcado, o parâmetro “Tratamento p/ Empresas Substituto Tributário – Construção Civil” vai ficar desabilitado\. Ou vice\-versa, ou seja, os dois parâmetros não podem ser utilizados juntos na mesma geração\.

 __Estabelecimento:__ o sistema deve exibir os estabelecimentos pertencentes ao município de Porto Alegre, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__OS3537\-A/OS2542__

__MFS\_2071__

__MFS\-534050__

__MFS874080__

__RN06__

__Regras p/ Geração do Meio Magnético:__

Ao gerar o arquivo devem ser exibidas as abas “Log”, “Arquivo” e “Relatório de Conferência”\. 

A aba “Log” deve exibir a mensagem “Processo concluído com sucesso” quando o arquivo for gerado com sucesso\. 

Na aba “Arquivo” deve ser exibido o arquivo que poderá ser salvo localmente\. 

A aba “Relatório de Conferência” deve exibir um relatório que contenha os dados gerados no arquivo, para que o usuário possa realizar a conferência\.

__OS3537\-A/OS2542__

__RN07__

__Regras p/ formatação do Arquivo:__

Os arquivos gerados devem ter formato texto com seus campos separados por TAB, inclusive após o último campo de cada registro\.

Os campos numéricos que contenham valores em R$ ou alíquotas devem ser informados sem utilizar separadores de milhares\. Contudo necessariamente deverão apresentar uma vírgula para separação de casas decimais\. Exemplos:

         R$ 50\.000,00          deverá ser informado como           50000,00

         Alíquota de 2,5%    deverá ser informada como           2,5

Os campos numéricos que não estão preenchidos devem ser informados com um  0 \(zero\)\.

Os campos alfanuméricos que não estão preenchidos devem ser informados com um  ‘ ‘ \(branco\)\.

Campos do tipo Data deverão ser preenchidos no formato AAAAMMDD\.

Todos os campos deverão obedecer rigorosamente o tamanho e a formatação definido neste layout\. Caso um campo no Mastersaf exceda o tamanho definido no layout, a geração deve truncar o campo exibindo apenas as primeiras posições até completar o tamanho definido no layout\.

__OS3537\-A/OS2542__

__RN08__

__Regra geral p/ Registro de Serviços Prestados__

__\[ALTERADA – CH19353\_2015\]__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Considerar nota fiscal eletrônica nas seguintes condições:
	- Se o município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for DIFERENTE do município do contribuinte \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\), recuperar os documentos com uma das situações abaixo:
		- Modelo do Documento \(campo COD\_MODELO da tabela DWT\_DOCTO\_FISCAL = ‘55’\) OU
		- Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal\.

__OS3537\-A/OS2542__

__CH19353\_2015__

__RN09__

__Regra p/ campo Relação de Serviços Prestados – Inscrição Municipal__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na tela de geração\.

__OS3537\-A/OS2542__

__RN10__

__Regra p/ o campo Relação de Serviços Prestados – Competência__

Preencher com ano e o mês do campo Data Inicial da tela de geração do Meio Magnético\. Formato: AAAAMM\.

__OS3537\-A/OS2542__

__RN11__

__Regra p/ o campo Relação de Serviços Prestados – Tipo de Escrituração__

__\[ALTERADA – OS4815\]__

Se o usuário não apresentar a parametrização “Tipo de Escrituração p/ Serviços Prestados”, em Módulo: Municipal >> Porto Alegre, Menu: Parâmetros >> Remessa:

- Preencher com a opção escolhida no campo “Tipo de Escrituração” na tela de Geração do Meio Magnético\.

Se o usuário apresentar a parametrização “Tipo de Escrituração p/ Serviços Prestados”, em Módulo: Municipal >> Porto Alegre, Menu: Parâmetros >> Remessa:

- Preencher com a opção escolhida no campo “Tipo de Escrituração” na tela de Tipo de Escrituração p/ Serviços Prestados de acordo com o serviço parametrizado e cadastrado na NF\.

__*Exemplo:*__

__Notas fiscais de Serviços__

__Capa__

NF 001

Movimento = saída

Classificação fiscal do documento = 2

Estabelecimento = XPTO

Data fiscal = 01/06/2015

__Item__

Nº Item = 1

Serviço = SERV\_001

Serviço no Cadastro da SAFX2018 = SERV\_001 c/ Código da Lei 116 = 1401

__Capa__

NF 002

Movimento = saída

Classificação fiscal do documento = 2

Estabelecimento = XPTO

Data fiscal = 01/06/2015

__Item__

Nº Item = 1

Serviço = SERV\_002

Serviço no Cadastro da SAFX2018 = SERV\_002 c/ Código da Lei 116 = 0702

*Observação: *Conforme verificado, o validador da Prefeitura, não aceita a mesma NF, isso mesmo se houver tipo de escrituração diferente, um dos motivos do problema da abertura dessa demanda\.

__Novo parâmetro “Tipo de Escrituração p/ Serviços Prestados”__

Estabelecimento = XPTO

Período de Prestação = 01/01/2015 a 00/00/0000

Tipo de Escrituração = Construcao Civil \\ Incorporacao Imobiliaria

Serviços Lei 116 = 0702

__Tela de geração do arquivo magnético__

Data Inicial = 01/06/2015

Data Final = 30/06/2015

Tipo de Escrituração = 01 – Receita Bruta

Gerar Serviços Prestados = marcado

Gerar Serviços Tomados = desmarcado

Estabelecimento = XPTO

__Arquivo magnético gerado__

Para NF 001 foi gerado o campo Tipo de escrituração: 24722820	201506	__01__	000000000	P

Para NF 002 foi gerado o campo Tipo de escrituração: 24722820	201506	__11__	000000000	P

Ordem dos campos: 01\.Inscrição municipal, 02\.Competência, __03\.Tipo de escrituração__, 04\.Número sequencial da obra e 05\.Tipo de lançamento\. __*Observação:*__ foram colocados alguns campos apenas para demonstração de como esse campo será gerado

Nesse caso será gerada uma única remessa de arquivo, incluindo as exceções de tipo de escrituração de acordo com o serviço vinculado na nova parametrização\.

<a id="OLE_LINK9"></a><a id="OLE_LINK10"></a><a id="OLE_LINK11"></a>__Atenção:__ A partir do momento que existir uma parametrização por Tipo de Escrituração p/ Serviços Prestados, deve ser considerada na verificação a data final do campo “Período de Prestação” da parametrização para aqueles serviços cadastrados, ou seja, verifica a data inicial e final preenchida na tela de geração do arquivo magnético, se tiver data de parâmetro dentro desse período, mesmo que não preenchida a data final considera o parâmetro, caso contrário não\.

__OS3537\-A/OS2542__

__OS4815__

__RN12__

__Regra p/ o campo Relação de Serviços Prestados – Número Seqüencial da obra__

Se o tipo de escrituração = 11, preencher com o campo Seqüencial ISSQNDec da tela Parâmetros – Canal Distrib\./Obras x Seqüencial referente ao canal de distribuição cadastrado na tela\.

Para os demais tipos de escrituração, preencher com 0 \(zero\)\.

__OS3537\-A/OS2542__

__RN13__

__Regra p/ o campo Relação de Serviços Prestados – Tipo de Lançamento__

Verificar a regra:

Recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\. 

Se o código do município recuperado for igual a Porto Alegre, Preencher com:

P, quando tipo de escrituração = 1, 2, 3, 11, 15, 17, 18

S, quando tipo de escrituração = 7, 12, 16, 08, 19

C, quanto tipo de escrituração = 10

Senão, preencher com:

M, quando tipo de escrituração = 11, 13, 16, 2, 7, 12, 18, 17, 15

__\[ALTERADA – OS4815\]__

Considerar o Tipo de Escrituração do parâmetro “Tipo de Escrituração p/ Serviços Prestados”, em Módulo: Municipal >> Porto Alegre, Menu: Parâmetros >> Remessa ou da tela de geração do arquivo magnético\.

Obs: Os tipos de escrituração 4 e 5 não podem ser utilizados para prestadores de serviços, dessa forma os mesmos não estão previstos nessa regra\.

Também não estão previstos os tipos 9 e 14\. Quando um desses tipos for selecionado, campo deve ser preenchido em branco\.

__OS3537\-A/OS2542__

__OS4815__

__RN14__

__Regra p/ o campo Relação de Serviços Prestados – Situação do Documento__

Preencher com:

 “S”, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL \(campo 30 da safx07\) for cancelada \(situacao = S\)

 “N”, quando o mesmo for normal \(situacao <> S\)\. 

Quando o campo na tabela estiver nulo, preencher com “N”\.

__OS3537\-A/OS2542__

__RN15__

__Regra p/ o campo Relação de Serviços Prestados – Data__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da safx07\)\. No formato AAAAMMDD\.

__OS3537\-A/OS2542__

__/__

__CH119713__

__/__

__CH88137__

__RN16__

__Regra p/ o campo Relação de Serviços Prestados – Tipo de Documento__

Preencher com o campo Tipo Docto referente ao tipo de documento cadastrado na nota fiscal, através da parametrização realizada no menu Parâmetros \-> Tipo de Docto MSAF x Tipo de Docto, quando o município que está sendo gerado for igual a Porto Alegre\.

__OS3537\-A/OS2542__

__/__

__OS3119__

__RN17__

__Regra p/ o campo Relação de Serviços Prestados – Série do Documento__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 09 da safx07\)

__\[ALTERADA – CH17298\_2014\]__

Se o campo SERIE\_DOCFIS \(campo 09 da safx07\) da tabela DWT\_DOCTO\_FISCAL for preenchido com “U” ou “UN” ou “UNI” ou estiver branco, atribuir ao campo o valor “ÚNICA”\.

__OS3537\-A/OS2542__

__/__

__CH101934__

__/__

__CH17298\_2014__

__RN18__

__Regra p/ o campo Relação de Serviços Prestados – Número do Documento__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da safx07\)

__OS3537\-A/OS2542__

__RN19__

__Regra p/ o campo Relação de Serviços Prestados – Valor Total do Documento__

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

Caso o documento não possua item de serviço, preencher com o valor total da nota referente à tabela safx07 \(capa do documento\)\.

Se o campo Situação do documento = “S”, preencher com zeros\.

__OS3537\-A/OS2542__

__/__

__CH115151__

__RN20__

__Regra p/ o campo Relação de Serviços Prestados – Aliquota__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 32 da safx09\)\.

Se tipo de lançamento = ‘S’ ou “M”, preencher com 0\. Preencher com apenas uma casa decimal\.

__OS3537\-A/OS2542__

__/__

__CH115151__

__RN21__

__Regra p/ o campo Relação de Serviços Prestados – Imposto Retido por Substituição Tributária__

Recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\. 

Com o município do local da prestação recuperado, verificar as seguintes opções:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “2" e se o local da prestação do serviço = município do módulo selecionado  
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado 
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV, com duas casas decimais quando:

- 
	- Nenhuma das opções acima forem verdadeiras e Tipo de Lançamento = “P”
	- Nenhuma das opções acima forem verdadeiras e Tipo de Lançamento = “S” quando Tipo de Escrituração = “16”

Caso contrário, preencher com zeros\.

Quando o tipo de lançamento = “M” ou “C”, preencher com zeros\.

__\[ALTERADA – OS4815\]__

Considerar o Tipo de Escrituração do parâmetro “Tipo de Escrituração p/ Serviços Prestados”, em Módulo: Municipal >> Porto Alegre, Menu: Parâmetros >> Remessa ou da tela de geração do arquivo magnético\.

__Obs\.: Regra ajustada no documento DE\-PARA – Municipal\.xls \(E1\-RN0001\)__

__OS3537\-A/OS2542__

__CH115151/OS4815__

__RN22__

__Regra p/ o campo Relação de Serviços Prestados – Inscrição Municipal do Substituto__

Recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\. 

Com o município do local da prestação recuperado, verificar as seguintes opções:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “2" e se o local da prestação do serviço = município do módulo selecionado  
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado 
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR, quando:

- 
	- Nenhuma das opções acima forem verdadeiras e Tipo de Lançamento = “P”
	- Nenhuma das opções acima forem verdadeiras e Tipo de Lançamento = “S” quando Tipo de Escrituração = “16”

Caso contrário, preencher com brancos\.

__\[ALTERADA – OS4815\]__

Considerar o Tipo de Escrituração do parâmetro “Tipo de Escrituração p/ Serviços Prestados”, em Módulo: Municipal >> Porto Alegre, Menu: Parâmetros >> Remessa ou da tela de geração do arquivo magnético\.

__Obs\.: Regra ajustada no documento DE\-PARA – Municipal\.xls \(E1\-RN0001\)__

__OS3537\-A/OS2542__

__CH88137/__

__CH1705/2013/__

__OS4815__

__RN23__

__Regra p/ o campo Relação de Serviços Prestados – CNPJ do Substituto__

Recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\. 

Com o município do local da prestação recuperado, verificar as seguintes opções:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “2" e se o local da prestação do serviço = município do módulo selecionado  
- Se na tabela X2098\_ALIQ\_SERVICO, o campo  IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo  COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado 
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado \.

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR, quando:

- 
	- Nenhuma das opções acima forem verdadeiras e Tipo de Lançamento = “P”
	- Nenhuma das opções acima forem verdadeiras e Tipo de Lançamento = “S” quando Tipo de Escrituração = “16”
	- Tipo de Lançamento = “M”

Caso contrário, preencher com brancos\.

__\[ALTERADA – OS4815\]__

Considerar o Tipo de Escrituração do parâmetro “Tipo de Escrituração p/ Serviços Prestados”, em Módulo: Municipal >> Porto Alegre, Menu: Parâmetros >> Remessa ou da tela de geração do arquivo magnético\.

__Obs\.: Regra ajustada no documento DE\-PARA – Municipal\.xls \(E1\-RN0001\)__

__OS3537\-A/OS2542__

__CH88137/__

__CH1705/2013/__

__OS4815__

__RN24__

__Regra p/ o campo Relação de Serviços Prestados – Número do Tíquete__

Preencher com zeros\.

__OS3537\-A/OS2542__

__RN25__

__Regra p/ o campo Relação de Serviços Prestados – Município de Prestação do Serviço__

Se o tipo de lançamento = “M”, verificar:

Recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

Gravar no arquivo o campo DESCRICAO da tabela MUNICIPIO referente ao código do município recuperado anteriormente\.

Obs: se o código do município recuperado for o da tabela DWT\_DOCTO\_FISCAL, será necessário verificar o COD\_MUNIC\_MSAF correspondente para poder recuperar a descrição na tabela de município\.

__OS3537\-A/OS2542__

__RN26__

__Regra p/ o campo Relação de Serviços Prestados – UF do Município de Prestação do Serviço__

Se o tipo de lançamento = “M”, recuperar o campo COD\_ESTADO da tabela ESTADO, referente ao IDENT\_ESTADO relacionado com o município a ser recuperado de acordo com a regra:

Recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

__OS3537\-A/OS2542__

__RN27__

__Regra p/ o campo Relação de Serviços Prestados – Dedução Turismo – Passagens Aéreas__

Preencher com zeros\.

__OS3537\-A/OS2542__

__RN28__

__Regra p/ o campo Relação de Serviços Prestados – Dedução Turismo \- Diárias__

Preencher com zeros\.

__OS3537\-A/OS2542__

__RN29__

__Regra p/ o campo Relação de Serviços Prestados – Percentual de Redução de Base de Cálculo__

Preencher com o “40” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços com o parâmetro “Serviços com redução de base de cálculo à 40%” para o município de Porto Alegre \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. Caso o serviço não esteja parametrizado, preencher com branco\.

Esse campo apenas deve ser preenchido se o campo “Tipo de Escrituração” = 15\. Senão preencher com branco\.

__\[ALTERADA – OS4815\]__

Considerar o Tipo de Escrituração do parâmetro “Tipo de Escrituração p/ Serviços Prestados”, em Módulo: Municipal >> Porto Alegre, Menu: Parâmetros >> Remessa ou da tela de geração do arquivo magnético\.

__OS3537\-A/OS2542__

__CH96094/OS4815__

__RN30__

__Regra geral p/ Registro de Serviços Tomados__

__\[ALTERADA – CH19353\_2015\]__

- Nota de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Nota não cancelada \(SITUACAO <> S\)
- Considerar nota fiscal eletrônica nas seguintes condições:
	- Se o município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for DIFERENTE do município do contribuinte \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\), recuperar os documentos com uma das situações abaixo:
		- Modelo do Documento \(campo COD\_MODELO da tabela DWT\_DOCTO\_FISCAL = ‘55’\) OU
		- Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal\.

Quando, dentro do período de geração, houver nota fiscal com data de emissão fora do período, a geração deve realizar a quebra de arquivo por competência \(data de emissão\), agrupando pelo mês e ano\. 

__OS3537\-A/OS2542__

__OS3626__

__CH19353\_2015__

__RN31__

__Regra p/ o campo Registro de Serviços Tomados – Inscrição Municipal__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na tela de geração\.

__OS3537\-A/OS2542__

__RN32__

__Regra p/ o campo Registro de Serviços Tomados \- Competência__

Preencher com ano e o mês do campo Data Inicial da tela de geração do Meio Magnético\. Formato: AAAAMM\.

Preencher com o ano e mês do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da safx07\)\. 

Formato: AAAAMM\.

__OS3537\-A/OS2542__

__RN56__

__Regra p/ o campo Registro de Serviços Tomados – Tipo de Escrituração__

__\[ALTERADA – OS4815\]__

Se o usuário não apresentar a parametrização “Tipo de Escrituração p/ Serviços Tomados”, em Módulo: Municipal >> Porto Alegre, Menu: Parâmetros >> Remessa:

- Preencher com a opção escolhida no campo “Tipo de Escrituração” na tela de Geração do Meio Magnético\.

Se o usuário apresentar a parametrização “Tipo de Escrituração p/ Serviços Tomados”, em Módulo: Municipal >> Porto Alegre, Menu: Parâmetros >> Remessa:

- Preencher com a opção escolhida no campo “Tipo de Escrituração” na tela de Tipo de Escrituração p/ Serviços Tomados de acordo com o serviço parametrizado e cadastrado na NF\.

__*Exemplo:*__

__Notas fiscais de Serviços__

__Capa__

NF 001

Movimento = entrada

Classificação fiscal do documento = 2

Estabelecimento = XPTO

Data fiscal = 01/06/2015

__Item__

Nº Item = 1

Serviço = SERV\_001

Serviço no Cadastro da SAFX2018 = SERV\_001 c/ Código da Lei 116 = 1401

__Capa__

NF 002

Movimento = entrada

Classificação fiscal do documento = 2

Estabelecimento = XPTO

Data fiscal = 01/06/2015

__Item__

Nº Item = 1

Serviço = SERV\_002

Serviço no Cadastro da SAFX2018 = SERV\_002 c/ Código da Lei 116 = 0702

*Observação: *Conforme verificado, o validador da Prefeitura, não aceita a mesma NF, isso mesmo se houver tipo de escrituração diferente, um dos motivos do problema da abertura dessa demanda\.

__Novo parâmetro “Tipo de Escrituração p/ Serviços Tomados”__

Estabelecimento = XPTO

Período de Recebimento = 01/01/2015 a 00/00/0000

Tipo de Escrituração = Construcao Civil \\ Incorporacao Imobiliaria

Serviços Lei 116 = 0702

__Tela de geração do arquivo magnético__

Data Inicial = 01/06/2015

Data Final = 30/06/2015

Tipo de Escrituração = 01 – Receita Bruta

Gerar Serviços Prestados = desmarcado

Gerar Serviços Tomados = marcado

Estabelecimento = XPTO

__Arquivo magnético gerado__

Para NF 001 foi gerado o campo Tipo de escrituração: 24722820	201506	__01__	000000000	P

Para NF 002 foi gerado o campo Tipo de escrituração: 24722820	201506	__11__	000000000	P

Ordem dos campos: 01\.Inscrição municipal, 02\.Competência, __03\.Tipo de escrituração__, 04\.Número sequencial da obra e 05\.Tipo de lançamento\. __*Observação:*__ foram colocados alguns campos apenas para demonstração de como esse campo será gerado

Nesse caso será gerada uma única remessa de arquivo, incluindo as exceções de tipo de escrituração de acordo com o serviço vinculado na nova parametrização\.

__Atenção:__ A partir do momento que existir uma parametrização por Tipo de Escrituração p/ Serviços Tomados, deve ser considerada na verificação a data final do campo “Período de Recebimento” da parametrização para aqueles serviços cadastrados, ou seja, verifica a data inicial e final preenchida na tela de geração do arquivo magnético, se tiver data de parâmetro dentro desse período, mesmo que não preenchida a data final considera o parâmetro, caso contrário não\.

__OS4815__

__RN33__

__Regra p/ o campo Registro de Serviços Tomados – Número Seqüencial da Obra__

Se o tipo de escrituração = 11, preencher com o campo Seqüencial ISSQNDec da tela Parâmetros – Canal Distrib\./Obras x Seqüencial referente ao canal de distribuição cadastrado na tela\. \(campo COD\_CANAL\_DISTRIB da tabela DWT\_DOCTO\_FISCAL\)

Para os demais tipos de escrituração, preencher com 0 \(zero\)\.

__\[ALTERADA – OS4815\]__

Considerar o Tipo de Escrituração do parâmetro “Tipo de Escrituração p/ Serviços Tomados”, em Módulo: Municipal >> Porto Alegre, Menu: Parâmetros >> Remessa ou da tela de geração do arquivo magnético\.

__OS3537\-A/OS2542__

__OS4815__

__RN34__

__Regra p/ o campo Registro de Serviços Tomados – Tipo de Lançamento__

Preencher com:

N, quando tipo de escrituração = 1, 2, 3, 4, 7, 9, 10, 12, 15, 16, 17, 18, 19, \(11 e o campo das regras RN51 e RN52 = 0\)

P, quando tipo de escrituração = 17 e o campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV estiver preenchido\.

T, quando tipo de escrituração = 5

M, quando tipo de escrituração = 11 e o campo da regra RN51 for <> 0\.

S, quando tipo de escrituração = 11 e o campo da regra RN52 for <> 0\.

__\[ALTERADA – OS4815\]__

Considerar o Tipo de Escrituração do parâmetro “Tipo de Escrituração p/ Serviços Tomados”, em Módulo: Municipal >> Porto Alegre, Menu: Parâmetros >> Remessa ou da tela de geração do arquivo magnético\.

__OS3537\-A/OS2542__

__CH88137/OS4815__

__RN35__

__Regra p/ o campo Registro de Serviços Tomados – Data do Documento__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da safx07\)\. No formato AAAAMMDD\.

__OS3537\-A/OS2542__

__RN36__

__Regra p/ o campo Registro de Serviços Tomados – Data de Pagamento__

__\[ALTERADA – CH17460\_2014\]__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da safx07\)\. 

__OS3537\-A/OS2542__

__CH22331/__

__CH17460\_2014__

__RN37__

__Regra p/ o campo Registro de Serviços Tomados – Tipo de Documento__

Se o campo “Tipo de Lançamento” = “M”

        Recupera o tipo de documento – Ded\. Material relacionado com o tipo de documento cadastrado na nota fiscal, através da parametrização realizada no menu: Parâmetros \-> Tipo de Docto MSAF x Tipo de Docto – Ded\. Material, quando o município que está sendo gerado for igual a Porto Alegre\.

Senão

Recupera o tipo de documento relacionado com o tipo de documento cadastrado na nota fiscal, através da parametrização realizada no menu: Parâmetros \-> Tipo de Docto MasterSAF x Tipo de Docto, quando o município que está sendo gerado for igual a Porto Alegre\.

__OS3537\-A/OS2542__

__RN38__

__Regra p/ o campo Registro de Serviços Tomados – Série do Documento__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 09 da safx07\)

Se o campo SERIE\_DOCFIS \(campo 09 da safx07\) da tabela DWT\_DOCTO\_FISCAL for preenchido com “U” ou “UN” ou “UNI” atribuir ao campo o valor “ÚNICA”\.

__OS3537\-A/OS2542__

__RN39__

__Regra p/ o campo Registro de Serviços Tomados – Número do Documento__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da safx07\)

__OS3537\-A/OS2542__

__RN40__

__Regra p/ o campo Registro de Serviços Tomados – Tipo de Serviço__

Preencher com zeros\.

__OS3537\-A/OS2542__

__RN41__

__Regra p/ o campo Registro de Serviços Tomados – Valor Total do Documento__

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

Caso o documento não possua item de serviço, preencher com o valor total da nota referente à tabela safx07 \(capa do documento\)\.

__OS3537\-A/OS2542__

__RN42__

__Regra p/ o campo Registro de Serviços Tomados – Valor Dedutível__

Preencher com o campo VLR\_DEDUCAO\_ISS da tabela DWT\_DOCTO\_FISCAL \(campo 190 da safx07\)\. Se tipo de lançamento = “S”, preencher conforme a regra RN52\.

__OS3537\-A/OS2542__

__RN43__

__Regra p/ o campo Registro de Serviços Tomados – Alíquota da Substituição Tributária__

__\[ALTERADA – CH20610\_2016/__[__MFS\-46492__](https://jira.thomsonreuters.com/browse/MFS-46492)__\] Inclusão do código 16\.02\.__

__\[ALTERADA – MFS\-534050\] Readequação da Regra para considerar o parâmetro __Tratamento p/ Empresas Substituto Tributário no município \(Art\. 1ª Lei Complementar 306/93\)

__\[ALTERADA – MFS\-874080\] __Readequação da Regra para considerar o parâmetro Tratamento p/ Empresas ST – Construção Civil

__*Tratamento para Notas Fiscais de Serviço com item:*__

__ Regra Parâmetro: __Parâmetro p/ __“__Tratamento p/ Empresas Substituto Tributário no município \(Art\. 1ª Lei Complementar 306/93\)”\.

__Parâmetro Marcado: __Se o parâmetro__ “__Tratamento p/ Empresas Substituto Tributário no município \(Art\. 1ª Lei Complementar 306/93\)”  estiver marcado, o sistema deverá gerar a informação de Alíquota da Substituição Tributária para todos os Código de Serviço da Lei Complementar 116\.

__Preencher__ com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.  __Ou__

            __Se __o campo ALIQ\_TRIBUTO\_ISS não estiver preenchido ou preenchido com zeros

       __Preencher__ com o campo VLR\_ALIQ\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\.

__   __

__Senão__ __preencher__ com zero       

__Parâmetro Desmarcado: __Se o parâmetro__ “__Tratamento p/ Empresas Substituto Tributário no município \(Art\. 1ª Lei Complementar 306/93\)” estiver desmarcado, o sistema deverá gerar a informação de Alíquota da Substituição Tributária conforme regra atual, seguindo a regra abaixo:

Se a nota fiscal possuir item, então se o Código de Serviço da Lei Compl\. 116/03 informado no serviço cadastrado no item pertencer a seguinte lista de códigos:

3\.05, 7\.02, 7\.04, 7\.05, 7\.09, 7\.10, 7\.11, 7\.12, 7\.16, 7\.17, 7\.18, 7\.19, 10\.08, 11\.01, 11\.02, 11\.04, 12\.01, 12\.02, 12\.03, 12\.04, 12\.05, 12\.06, 12\.07, 12\.08, 12\.09, 12\.10, 12\.11, 12\.12, 12\.14, 12\.15, 12\.16, 12\.17, 16\.01, 16\.02, 17\.05, 17\.06 17\.10, 20\.01, 20\.02 e 20\.03;

__Preencher__ com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.  __Ou__

__    Se __o campo ALIQ\_TRIBUTO\_ISS não estiver preenchido ou preenchido com zeros

       __Preencher__ com o campo VLR\_ALIQ\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\.

__Senão__ __preencher__ com zero       

__Regra Parâmetro: __Parâmetro p/ __“__Tratamento p/ Empresas Substituto Tributário – Construção Civil

__Parâmetro Marcado: __Se o parâmetro__ “__Tratamento p/ Empresas Substituto Tributário – Construção Civil” estiver marcado, o sistema não deverá gravar a informação de Alíquota da Substituição Tributária, quando o município da nota fiscal for diferente de Porto Alegre\. 

Recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\. 

__Se__ o município da nota fiscal for diferente do município do estabelecimento, o campo Alíquota da Substituição Tributária deve ser preenchido com zero\.

__   __

__Senão__ __preencher__ com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.  Ou

    Se o campo ALIQ\_TRIBUTO\_ISS não estiver preenchido ou preenchido com zeros

       Preencher com o campo VLR\_ALIQ\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\.

__Parâmetro Desmarcado: __Se o parâmetro__ “__Tratamento p/ Empresas Substituto Tributário – Construção Civil”  estiver desmarcado, o sistema deverá gerar a informação de Alíquota da Substituição Tributária conforme regra atual, seguindo a regra abaixo:

Se a nota fiscal possuir item, então se o Código de Serviço da Lei Compl\. 116/03 informado no serviço cadastrado no item pertencer a seguinte lista de códigos:

3\.05, 7\.02, 7\.04, 7\.05, 7\.09, 7\.10, 7\.11, 7\.12, 7\.16, 7\.17, 7\.18, 7\.19, 10\.08, 11\.01, 11\.02, 11\.04, 12\.01, 12\.02, 12\.03, 12\.04, 12\.05, 12\.06, 12\.07, 12\.08, 12\.09, 12\.10, 12\.11, 12\.12, 12\.14, 12\.15, 12\.16, 12\.17, 16\.01, 16\.02, 17\.05, 17\.06 17\.10, 20\.01, 20\.02 e 20\.03;

__Preencher__ com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.  __Ou__

__    Se __o campo ALIQ\_TRIBUTO\_ISS não estiver preenchido ou preenchido com zeros

       __Preencher__ com o campo VLR\_ALIQ\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\.

__Senão__ __preencher__ com zero\.       

__Observação sobre os parâmetros: __os dois parâmetros não podem ser utilizados juntos na mesma geração\.

__*Tratamento para Notas Fiscais de Serviço sem item:*__

Se a nota fiscal não possuir item, então se o campo Recolhim\. ISS for igual a Subst\. Tributária:

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_DOCTO\_FISCAL\.

Se nenhuma condição acima for atendida, preencher com zeros\.

Além disso, para a formatação correta do preenchimento do campo, considerar duas casas decimais, se o campo IND\_SIMPLES\_NAC da tabela X04\_lPESSOA\_FIS\_JUR da Pessoa Física/Jurídica cadastrada na nota fiscal for igual a “S” e a alíquota informada for < 1, senão considerar somente uma casa decimal\.

Se a alíquota informada for >= 10, o sistema deve exibir no log a seguinte mensagem: “Alíquota da nota superou o tamanho máximo permitido \(um inteiro e um decimal\)\.  Nota Fiscal: XXXXXXXXX \- Alíquota: 999,9999\.”\.

__OU__

\- Município do prestador deve ser IGUAL ao município do módulo \(campo COD\_MUNIC da tabela X04\_PESSOA\_FIS\_JUR = Porto Alegre \) __E__

\- Recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\. 

\- Código do serviço da Lei Complementar 116/03 associado ao código informado na nota fiscal estiver parametrizado na tela de Classificação de Serviços – ST __OU__

\- Município do prestador deve ser IGUAL ao município do módulo \(campo COD\_MUNIC da tabela X04\_PESSOA\_FIS\_JUR = Porto Alegre\) __E __prestador NÃO deve possuir cadastro no CPOM \(campo “CPOM \- Cadastro de Prestadores de Serviços de Outros Municípios” da tabela X04\_PESSOA\_FIS\_JUR  = desmarcado\) __OU__ 

\- Município do prestador deve ser DIFERENTE do município do módulo \(campo COD\_MUNIC da tabela X04\_PESSOA\_FIS\_JUR = Porto Alegre\) __E__ prestador deve possuir cadastro no CPOM \(campo “CPOM \- Cadastro de Prestadores de Serviços de Outros Municípios” da tabela X04\_PESSOA\_FIS\_JUR  = marcado\)

\- Atendida uma das regras acima, recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\. 

Com o município do local da prestação recuperado, verificar as seguintes opções:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado __OU__  
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo  COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado __OU__
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Se o campo IND\_SIMPLES\_NAC = ‘S’ da tabela X04\_PESSOA\_FIS\_JU, esse campo deve ser preenchido com duas casas decimais\.

 __Obs\.: Regra ajustada no documento DE\-PARA – Municipal\.xls \(R1\-RN0001\) __

__Obs\.:__ Na regra foram inseridos os códigos de serviços, como forma paliativa de identificar quando o prestador não está enquadrado como cadastrado no CPOM\. Será criada uma OS para tratar essa regra em um formato mais adequado\.

__OS3537\-A/OS2542__

__/__

__CH42079\-B__

__/__

__CH8304\_2012__

__/__

__CH17758__

__OS3537\-B__

__CH19076__

__CH19076\-A__

__CH20610\_2016__

__MFS\-46492__

__MFS\-534050__

__MFS874080__

__RN44__

__Regra p/ o campo Registro de Serviços Tomados – Imposto Retido por Substituição Tributária__

__\[ALTERADA – CH20610\_2016 / __[__MFS\-46492__](https://jira.thomsonreuters.com/browse/MFS-46492)__\] Inclusão do código 16\.02\.__

__\[ALTERADA – MFS\-534050\] __Readequação da Regra para considerar o parâmetro \- Tratamento p/ Empresas Substituto Tributário no município \(Art\. 1ª Lei Complementar 306/93\)

__\[ALTERADA – MFS\-874080\] Readequação da Regra para considerar o parâmetro Tratamento p/ Empresas ST – Construção Civil__

__*Tratamento para Notas Fiscais de Serviço com item:*__

__Regra Parâmetro: __Parâmetro p/ __“__Tratamento p/ Empresas Substituto Tributário no município \(Art\. 1ª Lei Complementar 306/93\)”\.

__Parâmetro Marcado: __Se o parâmetro__ “__Tratamento p/ Empresas Substituto Tributário no município \(Art\. 1ª Lei Complementar 306/93\)” estiver __marcado__, o sistema deverá gerar a informação de Valor de ISS Retido de Substituição Tributária para todos os Código de Serviço da Lei Complementar 116\.

  __Preencher__ com o  campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. __Ou__ __ __

       __Se __o campo VLR\_TRIBUTO\_ISS não estiver preenchido ou preenchido com zeros

         __Preencher__ com o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\.

__Senão__ __preencher__ com zero       

__Parâmetro Desmarcado: __Se o parâmetro__ “__Tratamento p/ Empresas Substituto Tributário no município \(Art\. 1ª Lei Complementar 306/93\)”  estiver __desmarcado__, o sistema deverá gerar a informação de Valor de ISS Retido da Substituição Tributária seguindo a regra abaixo:

Se a nota fiscal possuir item, então se o Código de Serviço da Lei Compl\. 116/03 informado no serviço cadastrado no item pertencer a seguinte lista de códigos:

3\.05, 7\.02, 7\.04, 7\.05, 7\.09, 7\.10, 7\.11, 7\.12, 7\.16, 7\.17, 7\.18, 7\.19, 10\.08, 11\.01, 11\.02, 11\.04, 12\.01, 12\.02, 12\.03, 12\.04, 12\.05, 12\.06, 12\.07, 12\.08, 12\.09, 12\.10, 12\.11, 12\.12, 12\.14, 12\.15, 12\.16, 12\.17, 16\.01, 16\.02, 17\.05, 17\.06 17\.10, 20\.01, 20\.02 e 20\.03;

__Preencher__ com o campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. __Ou__ __ __

       __Se __o campo VLR\_TRIBUTO\_ISS não estiver preenchido ou preenchido com zeros

         __Preencher__ com o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\.

__Senão__ __preencher__ com zero       

__Regra Parâmetro: __Parâmetro p/ __“__Tratamento p/ Empresas Substituto Tributário – Construção Civil”\.

__Parâmetro Marcado: __Se o parâmetro__ “__Tratamento p/ Empresas Substituto Tributário – Construção Civil” estiver __marcado__, o sistema não deverá gravar a informação de Valor de ISS Retido de Substituição Tributária, quando o município da nota fiscal for diferente de Porto Alegre\.

Recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.  

__Se__ o município da nota fiscal for diferente do município do estabelecimento, o campo Imposto Retido da Substituição Tributária deve ser preenchido com zero\.

__Senão__ __preencher__ com o  campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. __Ou__ __ __

       __Se __o campo VLR\_TRIBUTO\_ISS não estiver preenchido ou preenchido com zeros

         __Preencher__ com o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV

__Parâmetro Desmarcado: __Se o parâmetro__ “__Tratamento p/ Empresas Substituto Tributário – Construção Civil”  estiver __desmarcado__, o sistema deverá gerar a informação de Valor de ISS Retido da Substituição Tributária seguindo a regra abaixo:

Se a nota fiscal possuir item, então se o Código de Serviço da Lei Compl\. 116/03 informado no serviço cadastrado no item pertencer a seguinte lista de códigos:

3\.05, 7\.02, 7\.04, 7\.05, 7\.09, 7\.10, 7\.11, 7\.12, 7\.16, 7\.17, 7\.18, 7\.19, 10\.08, 11\.01, 11\.02, 11\.04, 12\.01, 12\.02, 12\.03, 12\.04, 12\.05, 12\.06, 12\.07, 12\.08, 12\.09, 12\.10, 12\.11, 12\.12, 12\.14, 12\.15, 12\.16, 12\.17, 16\.01, 16\.02, 17\.05, 17\.06 17\.10, 20\.01, 20\.02 e 20\.03;

__Preencher__ com o campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. __Ou__ __ __

       __Se __o campo VLR\_TRIBUTO\_ISS não estiver preenchido ou preenchido com zeros

         __Preencher__ com o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\.

__Senão__ __preencher__ com zero\.       

__Observação sobre os parâmetros: __os dois parâmetros não podem ser utilizados juntos na mesma geração\.

__*Tratamento para Notas Fiscais de Serviço sem item:*__

Se a nota fiscal não possuir item, então se o campo Recolhim\. ISS for igual a Subst\. Tributária:

preencher com o campo VLR\_TRIBUTO\_ISS da tabela DWT\_DOCTO\_FISCAL\.

Se nenhuma das situações acima for atendida, preencher com zeros\.

Preencher com o campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV, ou campo VLR\_ISS\_RETIDO da tabela DWT\_DOCTO FISCAL caso a nota fiscal não possua item de serviço, com duas casas, se uma das regras abaixo for atendida:

\- Código de serviço da Lei Compl\. 116/03 informado na nota fiscal DEVE pertencer a seguinte lista de códigos:

“3\.05”, “7\.02”, “7\.19”, “7\.04”, “7\.05”, “7\.09”, “7\.10”, “7\.11”, “7\.12”, “7\.16”, “7\.17”, “7\.18”, “11\.01”\. “11\.02”, “11\.04”, “12\.01” a “12\.12” e “12\.14” a “12\.17”, “16\.01”, “17\.05”, “17\.10” e “20\.01” a “20\.03” __OU__

\- Município do prestador deve ser IGUAL ao município do módulo \(campo COD\_MUNIC da tabela X04\_PESSOA\_FIS\_JUR = Porto Alegre \) __E__

\- Recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\. 

\- Código do serviço da Lei Complementar 116/03 associado ao código informado na nota fiscal estiver parametrizado na tela de Classificação de Serviços – ST __OU__

\- Município do prestador deve ser IGUAL ao município do módulo \(campo COD\_MUNIC da tabela X04\_PESSOA\_FIS\_JUR = Porto Alegre\) __E __prestador NÃO deve possuir cadastro no CPOM \(campo “CPOM \- Cadastro de Prestadores de Serviços de Outros Municípios” da tabela X04\_PESSOA\_FIS\_JUR  = desmarcado\) __OU__ 

\- Município do prestador deve ser DIFERENTE do município do módulo \(campo COD\_MUNIC da tabela X04\_PESSOA\_FIS\_JUR = Porto Alegre\) __E__ prestador deve possuir cadastro no CPOM \(campo “CPOM \- Cadastro de Prestadores de Serviços de Outros Municípios” da tabela X04\_PESSOA\_FIS\_JUR  = marcado\)

Atendida uma das regras acima, recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\. 

Com o município do local da prestação recuperado, verificar as seguintes situações:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado __OU__
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo  COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado __OU__
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

__Obs\.: Regra ajustada no documento DE\-PARA – Municipal\.xls \(R1\-RN0001\)__

__Obs\.:__ Na regra foram inseridos os códigos de serviços, como forma paliativa de identificar quando o prestador não está enquadrado como cadastrado no CPOM\. Será criada uma OS para tratar essa regra em um formato mais adequado\.

__OS3537\-A/OS2542__

__/__

__CH42079\-B__

__/__

__CH8304\_2012__

__/__

__CH17758__

__OS3537\-B__

__CH20610\_2016__

__MFS\-46492__

__MFS\-534050__

__MFS874080__

__RN45__

__Regra p/ o campo Registro de Serviços Tomados – Imposto Retido por Responsabilidade Solidária__

Preencher com zeros\.

__OS3537\-A/OS2542__

__RN46__

__Regra p/ o campo Registro de Serviços Tomados – Inscrição Municipal do Substituído/Prestador__

__\[ALTERADA – CH20610\_2016/ CH20512\_2017 \(MFS\-14614\)\]__

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR da pessoa fis/jur cadastrada na nota fiscal quando o campo COD\_MUNICIPIO for igual a do estabelecimento, pois só serão aceitas as IM de prestadores de Porto Alegre\.

__Tratamento:__

- Se o campo COD\_MUNICIPIO for diferente do estabelecimento, preencher com zeros\.
- Se o campo COD\_MUNICIPIO for igual a nulo ou branco, preencher com zeros\.

Preencher com o campo INSCRICAO\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR da pessoa fis/jur cadastrada na nota fiscal, quando pelo menos uma das opções abaixo for verdadeira:

Recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\. 

Com o município do local da prestação recuperado, verificar as seguintes opções:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado  
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo  COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado 
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Caso contrário, preencher com zeros\.

Se o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR =   Porto Alegre, preencher com o campo de Inscrição Municipal\.

Se o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR <>  Porto Alegre ou o campo INSCRICAO\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR não estiver preenchido, preencher com zeros\., preencher com brancos\.

__OS3537\-A/OS2542__

__/__

__CH88137__

__/__

__CH8304\_2012__

__CH17706__

__CH20610\_2016__

__CH20512\_2017__

__\(MFS\-14614\)__

__RN47__

__Regra p/ o campo Registro de Serviços Tomados – CNPJ do Substituído/Prestador__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR da pessoa fis/jur cadastrada na nota fiscal\.

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR da pessoa fis/jur cadastrada na nota fiscal, quando pelo menos uma das opções abaixo for verdadeira:

Recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\. 

Com o município do local da prestação recuperado, verificar as seguintes opções:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado  
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo  COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado 
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Caso contrário, preencher com zeros\.

__OS3537\-A/OS2542__

__/__

__CH88137__

__/__

__CH42079\-B__

__/__

__CH8304\_2012__

__RN48__

__Regra p/ o campo Registro de Serviços Tomados – CC__

Preencher com CC\.

__OS3537\-A/OS2542__

__RN49__

__Regra p/ o campo Registro de Serviços Tomados – Matricula da obra __

Se o tipo de escrituração = ‘11’ e o campo Tipo lançamento <> ‘S, ’preencher com o campo COD\_CANAL\_DISTRIB da tabela DWT\_DOCTO\_FISCAL\.

Se o campo tipo de escrituração = ‘11’ e o campo Tipo lançamento = ‘S’, preencher com 0 \(zero\)\.

Para os demais tipos de escrituração, preencher com 0 \(zero\)\.

Se o tipo de escrituração = ‘11’ e o campo Tipo lançamento = ‘S’ __OU__ ‘M’ __OU__ ‘N’ preencherem com o campo COD\_CANAL\_DISTRIB da tabela DWT\_DOCTO\_FISCAL\.

Se o campo tipo de escrituração = ‘11’ e o campo Tipo lançamento <> ‘S’ __OU__ ‘M’ __OU__ ‘N’, preencher com brancos\.

Se o tipo de escrituração = ‘11’ e o campo Tipo lançamento = ‘S, ’preencher com o campo COD\_CANAL\_DISTRIB da tabela DWT\_DOCTO\_FISCAL\.

Se o campo tipo de escrituração = ‘11’ e o campo Tipo lançamento <> ‘S’, preencher com brancos\.

Para os demais tipos de escrituração, preencher com brancos\.

Para o Tipo de Lançamento = ‘M’ não será atendida em futura demanda\.

__\[ALTERADA – OS4815\]__

Considerar o Tipo de Escrituração do parâmetro “Tipo de Escrituração p/ Serviços Tomados”, em Módulo: Municipal >> Porto Alegre, Menu: Parâmetros >> Remessa ou da tela de geração do arquivo magnético\.

__OS3537/OS2542__

__CH17701__

__OS3537\-B__

__OS4815__

__RN50__

__Regra p/ o campo Registro de Serviços Tomados – Percentual de redução de base de calculo__

Preencher com o “40” se o serviço cadastrado na nota estiver parametrizado na tela Parâmetros – Classificação de Serviços com o parâmetro “Serviços com redução de base de cálculo à 40%” para o município da Pessoa Fis/Jur \(COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\)\. Caso o serviço não esteja parametrizado, preencher com 0 \(zero\)\.

Esse campo apenas deve ser preenchido se o campo “Tipo de Escrituração” = 15\. Senão preencher com zeros\.

__\[ALTERADA – OS4815\]__

Considerar o Tipo de Escrituração do parâmetro “Tipo de Escrituração p/ Serviços Tomados”, em Módulo: Municipal >> Porto Alegre, Menu: Parâmetros >> Remessa ou da tela de geração do arquivo magnético\.

__OS3537\-A/OS2542__

__OS4815__

__RN51__

__Relação de Serviços Tomados – Valor de materiais utilizado pela subempreitada e Valor terceirizado pela subempreitada quando cliente lança itens de material e serviço separados:__

__*O sistema deve prever as duas situações de preenchimento, pois só podemos ter uma das duas situações: RN51 ou RN52, dependendo de como o cliente alimenta a base dele\. Para o preenchimento correto dos campos o sistema deve verificar se o registro se enquadra em uma das situações pelo menos\. *__

Nota fiscal deve ter mais de 1 item de serviços com códigos de serviços diferentes\. Para esses itens, verificar se o serviço informado é equiparado a construção civil \(ind\_tp\_serviço <>‘0’\), se sim:

Preencher o campo __Valor de materiais utilizado pela subempreitada__, recuperando o somatório do campo  VLT\_TOT da tabela DWT\_ITENS\_SERV para todos os itens do mesmo serviço que tenha o campo IND\_MAT\_SERV = ‘1’

Preencher o campo __Valor terceirizado pela subempreitada__, recuperando o somatório do campo  VLT\_TOT da tabela DWT\_ITENS\_SERV para todos os itens do mesmo serviço que tenha o campo IND\_MAT\_SERV = ‘2’

Se o serviço não for equiparado a construção civil \(ind\_tp\_serviço =  ‘0’\), preencher com zeros\.

Esse campo apenas deve ser preenchido se o Tipo de Escrituração = 11

__Obs\.:__ Essa situação somente será atendida quando houver mais de 1 item de serviço na nota e para 1 item o campo IND\_MAT\_SERV = ‘1’ e para o outro item o campo IND\_MAT\_SERV = ‘2’, ou seja, a nota deve ter itens de serviços classificados como Equiparado a Construção Civil com itens de material e serviço\.

__\[ALTERADA – OS4815\]__

Considerar o Tipo de Escrituração do parâmetro “Tipo de Escrituração p/ Serviços Tomados”, em Módulo: Municipal >> Porto Alegre, Menu: Parâmetros >> Remessa ou da tela de geração do arquivo magnético\.

__OS3537\-A/OS2542__

__OS4815__

__RN52__

__Relação de Serviços Tomados – Valor de materiais utilizado pela subempreitada e Valor terceirizado pela subempreitada quando cliente lança apenas itens de serviço:__

__*O sistema deve prever as duas situações de preenchimento, pois só podemos ter uma das duas situações: RN51 ou RN52, dependendo de como o cliente alimenta a base dele\. Para o preenchimento correto dos campos o sistema deve verificar se o registro se enquadra em uma das situações pelo menos\.*__

Verificar se o serviço cadastrado na nota é equiparado a construção civil \(ind\_tp\_serviço <> ‘0’\), se sim:

Preencher o campo __Valor de materiais utilizado pela subempreitada__, recuperando o somatório do campo  VLR\_MAT\_TERC da tabela DWT\_ITENS\_SERV para todos os itens de serviço da NF com IND\_MAT\_SERV = '2\.

Preencher o campo __Valor terceirizado pela subempreitada__, recuperando o somatório do campo  VLR\_SUBEMPR\_ISS da tabela DWT\_ITENS\_SERV para todos os itens de serviço da NF com IND\_MAT\_SERV = '2\.

Se o serviço não for equiparado a construção civil \(ind\_tp\_serviço = ‘0’\), preencher com zeros\.

Esse campo apenas deve ser preenchido se o Tipo de Escrituração = 11

__\[ALTERADA – OS4815\]__

Considerar o Tipo de Escrituração do parâmetro “Tipo de Escrituração p/ Serviços Tomados”, em Módulo: Municipal >> Porto Alegre, Menu: Parâmetros >> Remessa ou da tela de geração do arquivo magnético\.

__OS3537\-A/OS2542__

__OS4815__

__RN53__

__Regra p/ o campo Registro de Serviços Tomados – Imposto pago pelas terceirizadas__

Recuperar o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV para todos os itens\.

Preencher apenas se tipo de escrituração = 11 e tipo de lançamento  = ‘S’

__\[ALTERADA – OS4815\]__

Considerar o Tipo de Escrituração do parâmetro “Tipo de Escrituração p/ Serviços Tomados”, em Módulo: Municipal >> Porto Alegre, Menu: Parâmetros >> Remessa ou da tela de geração do arquivo magnético\.

__OS3537\-A/OS2542 CH17703__

__OS4815__

__RN54__

__Regra p/ o campo Registro de Serviços Tomados – Imposto retido por falta de cadastro no CPOM__

__\[ALTERADA \- MFS\-94101\] __Tratamento para preencher com zeros, devido campo descontinuado pelo layout \(CPOM\)

          __Preencher__ com zeros\.

__Obs\.: __Conforme aviso no site da Prefeitura e Layout de serviços Tomados de Porto Alegre, os campos "Imposto retido por falta de cadastro no CPOM" e "Alíquota de imposto retido por falta de cadastramento no CPOM" foram descontinuados\. \(Ver: *Layout Serviços Tomados\.pdf\)*

__\[ALTERADA – CH20610\_2016\] / \[__[__MFS\-46492__](https://jira.thomsonreuters.com/browse/MFS-46492)__\] Inclusão do código 16\.02\.__

__*Tratamento para Notas Fiscais de Serviço com item:*__

Se a nota fiscal possuir item, então se o Código de Serviço da Lei Compl\. 116/03 informado no serviço cadastrado no item NÃO pertencer a seguinte lista de códigos:

3\.05, 7\.02, 7\.04, 7\.05, 7\.09, 7\.10, 7\.11, 7\.12, 7\.16, 7\.17, 7\.18, 7\.19, 11\.01, 11\.02, 11\.04, 12\.01, 12\.02, 12\.03, 12\.04, 12\.05, 12\.06, 12\.07, 12\.08, 12\.09, 12\.10, 12\.11, 12\.12, 12\.14, 12\.15, 12\.16, 12\.17, 16\.01, 16\.02, 17\.05, 17\.10, 20\.01, 20\.02, 20\.03, 4\.03, 4\.17, 5\.02, 5\.03, 6\.05, 8\.01, 8\.02 e 9\.01;

preencher com o campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. 

__*Tratamento para Notas Fiscais de Serviço sem item:*__

Se a nota fiscal não possuir item, então recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. Com o município do local da prestação recuperado, verificar as seguintes opções:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do estabelecimento selecionado __OU__
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_DOCTO\_FISCAL estiver preenchido e se o local da prestação do serviço = município do estabelecimento selecionado\.

Se uma das opções acima for atendida, então se o município do prestador for DIFERENTE do município do estabelecimento da geração \(campo COD\_MUNIC da tabela X04\_PESSOA\_FIS\_JUR <> Porto Alegre\) e se o campo Recolhim\. ISS for igual a Normal ou nulo:

preencher com o campo VLR\_TRIBUTO\_ISS da tabela DWT\_DOCTO\_FISCAL\.

Se nenhuma condição acima for atendida, preencher com zeros\.

Preencher com o campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV, ou valor do ISS retido na tabela safx07 caso a nota fiscal não possua item de serviço, com duas casas, se uma das regras abaixo for atendida:

\- Código de serviço da Lei Compl\. 116/03 informado na nota fiscal, NÃO deve pertencer a seguinte lista de códigos:

“3\.05”, “7\.02”, “7\.19”, “7\.04”, “7\.05”, “7\.09”, “7\.10”, “7\.11”, “7\.12”, “7\.16”, “7\.17”, “7\.18”, “11\.01”\. “11\.02”, “11\.04”, “12\.01” a “12\.12” e “12\.14” a “12\.17”, “16\.01”, “17\.05”, “17\.10” e “20\.01” a “20\.03” __E__

\- Município do prestador deve ser DIFERENTE do município do módulo \(campo COD\_MUNIC da tabela X04\_PESSOA\_FIS\_JUR <> Porto Alegre \) __E__

\- Código do serviço da Lei Complementar 116/03 associado ao código informado na nota fiscal NÃO estiver parametrizado na tela de Classificação de Serviços – ST __OU__

\- Município do prestador deve ser DIFERENTE do município do módulo \(campo COD\_MUNIC da tabela X04\_PESSOA\_FIS\_JUR = Porto Alegre\) __E__ prestador NÃO deve possuir cadastro no CPOM \(campo “CPOM \- Cadastro de Prestadores de Serviços de Outros Municípios” da tabela X04\_PESSOA\_FIS\_JUR  =desmarcado\)

Atendida uma das regras acima, recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

__Obs\.:__ Na regra foram inseridos os códigos de serviços, como forma paliativa de identificar quando o prestador não está enquadrado como cadastrado no CPOM\. Será criada uma OS para tratar essa regra em um formato mais adequado\.

__OS3537\-A/OS2542__

__CH17758__

__OS3537\-B__

__CH20610\_2016__

__MFS\-46492__

__MFS\-94101__

__RN55__

__Regra p/ o campo Registro de Serviços Tomados – Alíquota de imposto retido por falta de cadastramento no CPOM__

__\[ALTERADA \- MFS\-94101\] __Tratamento para preencher com zeros, devido campo descontinuado pelo layout \(CPOM\)

          __Preencher__ com zeros\.

__Obs\.: __Conforme aviso no site da Prefeitura e Layout de serviços Tomados de Porto Alegre, os campos "Imposto retido por falta de cadastro no CPOM" e "Alíquota de imposto retido por falta de cadastramento no CPOM" foram descontinuados\. \(Ver: *Layout Serviços Tomados\.pdf\)*

__\[ALTERADA – CH20610\_2016\] / \[__[__MFS\-46492__](https://jira.thomsonreuters.com/browse/MFS-46492)__\] Inclusão do código 16\.02\.__

__*Tratamento para Notas Fiscais de Serviço com item:*__

Se a nota fiscal possuir item, então se o Código de Serviço da Lei Compl\. 116/03 informado no serviço cadastrado no item NÃO pertencer a seguinte lista de códigos:

3\.05, 7\.02, 7\.04, 7\.05, 7\.09, 7\.10, 7\.11, 7\.12, 7\.16, 7\.17, 7\.18, 7\.19, 11\.01, 11\.02, 11\.04, 12\.01, 12\.02, 12\.03, 12\.04, 12\.05, 12\.06, 12\.07, 12\.08, 12\.09, 12\.10, 12\.11, 12\.12, 12\.14, 12\.15, 12\.16, 12\.17, 16\.01, 16\.02, 17\.05, 17\.10, 20\.01, 20\.02, 20\.03, 4\.03, 4\.17, 5\.02, 5\.03, 6\.05, 8\.01, 8\.02 e 9\.01;

preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. 

__*Tratamento para Notas Fiscais de Serviço sem item:*__

Se a nota fiscal não possuir item, então recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. Com o município do local da prestação recuperado, verificar as seguintes opções:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do estabelecimento selecionado __OU__
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_DOCTO\_FISCAL estiver preenchido e se o local da prestação do serviço = município do estabelecimento selecionado\.

Se uma das opções acima for atendida, então se o município do prestador for DIFERENTE do município do estabelecimento da geração \(campo COD\_MUNIC da tabela X04\_PESSOA\_FIS\_JUR <> Porto Alegre\) e se o campo Recolhim\. ISS for igual a Normal ou nulo:

preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_DOCTO\_FISCAL\.

Se nenhuma condição acima for atendida, preencher com zeros\.

Além disso, para a formatação correta do preenchimento do campo, considerar duas casas decimais, se o campo IND\_SIMPLES\_NAC da tabela X04\_lPESSOA\_FIS\_JUR da Pessoa Física/Jurídica cadastrada na nota fiscal for igual a “S”, senão considerar somente uma casa decimal\.

Se a alíquota informada for >= 10, o sistema deve exibir no log a seguinte mensagem: “Alíquota da nota superou o tamanho máximo permitido \(um inteiro e um decimal\)\.  Nota Fiscal: XXXXXXXXX \- Alíquota: 999,9999\.”\.

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV ou campo alíquota de serviço da tabela safx07 caso a nota fiscal não possua item de serviço, com uma casa decimal, se uma das regras abaixo for atendida:

\- Código de serviço da Lei Compl\. 116/03 informado na nota fiscal, NÃO deve pertencer a seguinte lista de códigos:

“3\.05”, “7\.02”, “7\.19”, “7\.04”, “7\.05”, “7\.09”, “7\.10”, “7\.11”, “7\.12”, “7\.16”, “7\.17”, “7\.18”, “11\.01”\. “11\.02”, “11\.04”, “12\.01” a “12\.12” e “12\.14” a “12\.17”, “16\.01”, “17\.05”, “17\.10” e “20\.01” a “20\.03” __E__

\- Município do prestador deve ser DIFERENTE do município do módulo \(campo COD\_MUNIC da tabela X04\_PESSOA\_FIS\_JUR <> Porto Alegre \) __E__

\- Código do serviço da Lei Complementar 116/03 associado ao código informado na nota fiscal NÃO estiver parametrizado na tela de Classificação de Serviços – ST __OU__

\- Município do prestador deve ser DIFERENTE do município do módulo \(campo COD\_MUNIC da tabela X04\_PESSOA\_FIS\_JUR = Porto Alegre\) __E__ prestador NÃO deve possuir cadastro no CPOM \(“CPOM \- Cadastro de Prestadores de Serviços de Outros Municípios” da tabela X04\_PESSOA\_FIS\_JUR = desmarcado\)

__Obs\.:__ Na regra foram inseridos os códigos de serviços, como forma paliativa de identificar quando o prestador não está enquadrado como cadastrado no CPOM\. Será criada uma OS para tratar essa regra em um formato mais adequado\.

__OS3537\-A/OS2542__

__/__

__CH17758__

__OS3537\-B__

__CH19076\-B__

__CH20610\_2016__

__MFS\-46492__

__MFS\-94101__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


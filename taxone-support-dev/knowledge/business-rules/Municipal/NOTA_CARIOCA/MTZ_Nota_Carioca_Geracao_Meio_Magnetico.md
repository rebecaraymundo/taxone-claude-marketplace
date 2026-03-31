# MTZ_Nota_Carioca_Geracao_Meio_Magnetico

- **Fonte:** MTZ_Nota_Carioca_Geracao_Meio_Magnetico.docx
- **Modificado:** 2026-03-02
- **Tamanho:** 87 KB

---

# Nota Carioca \- Geração do Meio Magnético

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3208

Nota Carioca \- Geração do Meio Magnético

Este documento tem por objetivo criar o novo módulo “Nota Carioca – Declaração de Notas Convencionais Recebidas” que irá gerar o meio magnético permitindo a importação de notas fiscais convencionais recebidas para o Sistema de Notas Fiscais de Serviço Eletrônicas\.

CH114061

DW \- MUNICIPAL \- RIO DE JANEIRO \- NOTA CARIOCA \- Está gerando inscrição municipal para prestadores fora do Municipio do RJ

O objetivo dessa demanda é preencher corretamente o campo “Inscrição Municipal do Prestador”, para pessoas Físicas/Jurídicas que são fora do Município “RIO DE JANEIRO”, para essa situação o campo deve ser preenchido com zeros\.

CH4804\_2012

DW \- MUNICIPAL \- NOTA CARIOCA \- Geração de prestadores dento do municipio indevidamente

O objetivo deste chamado é recuperar apenas notas fiscais recebidas que não sejam do tipo NFES – Nota Fiscal Eletrônica de Serviço\.

CH1191\_2012

DW \- MUNICIPAL \- RIO DE JANEIRO \- NOTA CARIOCA \- Filtro para notas fiscais com situação de cancelada\.

O objetivo desta demanda é não permitir que o módulo Nota Carioca gere notas fiscais recebidas que estejam canceladas\.

CH4804\-A\_2012

DW \- MUNICIPAL \- NOTA CARIOCA \- Geração de prestadores dento do municipio indevidamente

Esse chamado tem o objetivo de alterar a geração de registros de serviços tomados para que apenas carregue no arquivo notas fiscais eletrônicas \(modelo 55\) em que o município da Pessoa fis/jur cadastrada na nota fiscal seja diferente do município do estabelecimento escolhido na tela de geração\.

CH14104

DW \- MUNICIPAL \- NOTA CARIOCA \- Alteração na Regra de Negócio para correta recuperação do Tipo de Tributação

Alteração do campo de tipo de tributação para passar a comparar o local da prestação de serviços com o responsável pela retenção\.

CH15536

DW \- MUNICIPAL \- NOTA CARIOCA \- Alteração na Regra de Negócio para correta recuperação do campo ISS Retido

Alteração da regra de recuperação do campo ‘ISS Retido’ do registro tipo 40 para passar a verificar se existe cadastro do CEPOM para os prestadores de serviço de fora do município\.

CH19775

DW \- MUNICIPAL \- NOTA CARIOCA \- Alteração na Regra de Negócio para correta recuperação do campo Opção pelo simples

Alteração da regra de recuperação do campo ‘Opção pelo simples’ do registro tipo 40\.

CH19374

DW \- MUNICIPAL \- NOTA CARIOCA \- Alteração na Regra de Negócio para correta recuperação do campo Tipo de Tributação de Serviços

Alteração da regra de recuperação do campo ‘Tipo de Tributação de Serviços’ do registro tipo 40\.

OS3723

DW \- MUNICIPAL \- Parâmetros por Municipio \- Melhoria para que o relacionamento dos códigos do Município seja feito diretamente com os códigos correspondentes à Lei compl\.116/03

Este documento tem por objetivo permitir que o cliente possa realizar a parametrização de serviços também pelo código do serviço da Lei 116\.

CH24039

DW \- MUNICIPAL \- RIO DE JANEIRO \- NOTA CARIOCA \- Geração do Registro Tipo 40 para notas Eletrônicas

Alterar a geração da obrigação Nota Carioca para atender a seguinte situação: As notas fiscais eletrônicas cujo prestador \(SAFX04\) é do Rio de Janeiro não devem ser geradas no arquivo\.

OS3842

DW – MUNICIPAL – RIO DE JANEIRO NOTA CARIOCA

Inclusão de novos campos no Registro Tipo 40 para notas Eletrônicas

CH30809/2012

DW \- MUNICIPAL \- NOTA CARIOCA \- Gerar campo codigo da obra registro tipo 40

Alterar a geração do Registro Tipo 40 para que o campo Código da Obra seja preenchido corretamente\.

OS3985

DW \- MUNICIPAL \- NOTA CARIOCA \- Ajuste na geração do campo 22 \- Tipo de Tributação de Serviços para gerar o 02 \- Tributação Fora do Município

Ajustar a geração do campo Tipo de Tributação do Registro 40\.

CH29819\_2013

<a id="OLE_LINK25"></a><a id="OLE_LINK26"></a><a id="OLE_LINK27"></a><a id="OLE_LINK28"></a>DW – MUNICIPAL – RIO DE JANEIRO NOTA CARIOCA – Regra do Registro Tipo 40 – Campo 32 ISS Retido

<a id="OLE_LINK29"></a><a id="OLE_LINK30"></a><a id="OLE_LINK31"></a><a id="OLE_LINK32"></a><a id="OLE_LINK36"></a>Ajuste na regra de geração do campo ISS Retido do Registro Tipo 40 para contemplar quando o prestador tem estabelecimento fora do município e não possui cadastro no CPOM\.

OS4430

DW \- MUNICIPAL \- NOTA CARIOCA \- Inclusão do Registro 50 \(REMAS Eletrônico\)\.

Inclusão do registro de Declaração de Materiais \(REMAS\)

OS4337

Novo Parâmetro – Quebra do Arquivo por Data de Emissão

Implementar novo parâmetro para que seja possível realizar a quebra do arquivo por data de emissão, para Serviços Tomados\.

CH9872\_2014

DW – MUNICIPAL – RIO DE JANEIRO NOTA CARIOCA – Regra do Registro Tipo 40 – Campo 32 ISS Retido

<a id="OLE_LINK41"></a><a id="OLE_LINK42"></a><a id="OLE_LINK43"></a>Foi excluída uma parte da regra para CPOM, pois campo CPOM – Cadastro de Prestadores de Serviços de Outros Municípios da SAFX04 não existe e para o atendimento deve ser utilizada a regra: “Para os casos de prestador NÃO cadastrado no CPOM”, que foi criada pelo CH29819\_2013\.

OS4558

DW \- MUNICIPAL \- RIO DE JANEIRO \- NOTA CARIOCA \- Alteração para possibilidade de efetuar a geração pela Data de Pagamento

Ajuste no critério de seleção para geração do arquivo para considerar a Data do Pagamento, para a situação onde o ISS é Retido pelo Tomador\.

Ajuste na regra de geração do campo "Tipo de Tributação de Serviços", para situações tributadas dentro e fora do município;

Ajustes na regra do campo "ISS Retido"\.

OS3341\-A3

Geração do Meio Magnético para notas fiscais com número de documento com mais de 12 posições\.

Ajuste para considerar o novo campo NUM\_DOCFIS\_SERV

MFS3631

DW \- MUNICIPAL \- NOTA CARIOCA \- Atualização do Registro 50 \(REMAS Eletrônico\)\.

Ajustes nas regras do registro de Declaração de Materiais Tipo 50 \(REMAS\), para atender notas fiscais de mercadoria no momento da recuperação das notas\.

CH11904\_2016

DW \- MUNICIPAL \- NOTA CARIOCA \- Atualização do Registro 50 \(REMAS Eletrônico\)\.

Este documento tem como objetivo alterar a geração do registro de Declaração de Materiais Tipo 50 \(REMAS\) para considerar apenas notas fiscais com valor de dedução do ISS\.

CH23373\_2016

DW – MUNICIPAL – RIO DE JANEIRO NOTA CARIOCA – Regra geral de recuperação do Registro Tipo 40

Este documento tem como objetivo alterar a recuperação das notas fiscais de serviços tomados para geração do “Registro Tipo 40 \- Declaração de Notas Convencionais Recebidas” em que será considerada somente as notas que são de fora do município do Rio de Janeiro\.

CH13996\_2017

\(MFS\-12425\)

DW – MUNICIPAL – RIO DE JANEIRO NOTA CARIOCA – Regra geral de recuperação do Registro Tipo 40

Este documento tem como objetivo alterar a recuperação das notas fiscais de serviços tomados para geração do “Registro Tipo 40 \- Declaração de Notas Convencionais Recebidas” para não considerar fornecedores com MEI \(Microempreendedor Individual\) na geração do meio magnético\.

MFS\-21923

DW – MUNICIPAL – RIO DE JANEIRO NOTA CARIOCA – Regra para geração das Notas Invoices\.

Essa alteração tem como finalidade incluir um novo parâmetro para gerar as notas fiscais do exterior, ou seja, as NF’s Invoices serão consideradas a partir da data de emissão da nota para os serviços tomados\.

MFS\-72456

Andréa Rocha

Ajuste na regra de geração do campo "Tipo de Tributação de Serviços" para tratar a PFJ cadastrada no “CEPOM”, que na situação do cliente tem que gerar como “Tributado no Município” e estava gerando como “Tributado fora do Município”\. Foi criada mais uma classe da PFJ para identificar a PFJ cadastrada no CEPOM\.

Inclusão de mais uma opção para identificar a situação de “Tributado no Município”\.

MFS\-86017

Elisabete Costa

Ajuste na regra de geração do campo "Data de referência para definição da competência" para utilizar a data de emissão para ISS Retido e Não Retido\.

MFS\-90229

Elisabete Costa

Ajuste na regra de ISS Retido, pois não estava sendo preenchido no arquivo as informações do Registro Tipo 40\.

MFS\-91197

Elisabete Costa

Número de nota convencional limitada a 15 posições de acordo com layout

MFS\-98578

Elisabete Costa

Ajuste na regra de geração do campo "Data de referência para definição da competência" \(RN72\) para utilizar a data de emissão para ISS não retido, e a data do fato gerador para ISS retido\.\.

MFS\-98910

Elisabete Costa

Comentado do código o Registro Tipo 20 – Notas Fiscais de Saída \- RPS

MFS\-656575

Denílson André Santos

Este documento, tem o objetivo de, readequar a regra a seguir: Alíquota, RN66, para o município do Rio de Janeiro\-RJ

MFS\-766555

Rogério Ohashi

Este documento tem o objetivo de incluir 3 novos parâmetros para gerar Todas as Notas Fiscais de Serviço Tomados, ou somente Notas com Retenção ou Notas sem Retenção de ISS \(Somente Notas Fiscais de Serviço Tomados\)\. 

MFS865358

Andréa Rocha

Alteração da regra de geração do campo Código do Benefício, para preencher o campo de acordo com o campo Tipo de Tributação\.

MFS\-901113

Alessandra Navatta

Excluir os parâmetros na tela de geração para gerar Todas as Notas Fiscais de Serviço Tomados, ou somente Notas com Retenção ou Notas sem Retenção de ISS \(Somente Notas Fiscais de Serviço Tomados\) \(RN27\)\.Criada uma tela de parâmetro para contemplar esse filtro por validador\.

MFS\-906939

Rafael Fabiano

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para os municípios atendidos pelo validador nota carioca\.

MFS\-829438

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

MFS\-1018598

Klemer Monteiro

Desconsiderar notas fiscais eletrônicas, em que o município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for IGUAL do município do estabelecimento selecionado para geração \(COD\_MUNICIPIO da tabela ESTABELECIMENTO

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

Regra p/ criação do novo módulo

O novo módulo “Nota Carioca” deve ficar localizado no grupo “Municipal” abaixo do módulo “ISSQN Porto Alegre”\.

A descrição funcional do módulo será: “O módulo Nota Carioca – Declaração de Notas Convencionais Recebidas irá gerar o meio magnético permitindo a importação de notas fiscais convencionais recebidas para o Sistema de Notas Fiscais de Serviço Eletrônicas\.”

__OS3208__

__RN02__

__Regra p/ abertura do novo módulo__

Se o estabelecimento selecionado no Manager não pertencer ao estado do Rio de Janeiro \(UF = “RJ”\) e ao município do Rio de Janeiro \(Cod Município IBGE = 4557\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município do Rio de Janeiro, Rio de Janeiro\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Serão exibidos os botões “Sim” e “Não” \(default\)\. Se o usuário clicar no botão “Sim”, o módulo será aberto normalmente, senão o módulo será fechado\.

__OS3208__

__RN03__

__Regra p/ hierarquia de menus__

Deverão ser criados os seguintes menus e sub\-menus no módulo Nota Carioca:

- Arquivo
- Parâmetros
	- Tipo Docto\. Msaf x Tipo Docto\.Nota Carioca
	- Serviços 
	- Serviços Msaf x Serviços Municipais 
	- Serviços Lei 116 x Serviços Municipais
	- Classificação de Serviços
	- Serviços Msaf x Benefício Fiscal
- <a id="_Hlk216983380"></a>Manutenção
	- Materiais
- Obrigações
	- Geração do Meio Magnético
	- <a id="_Hlk207011407"></a>Arquivo de Entradas de Serviços \(Const\. Civil/Utilities /Telecom\)
- Janela
- Ajuda

__OS3208__

__/__

__OS3723__

__/__

__OS4430__

MFS\-906939

__RN04__

__Regra p/ importação da TFIX85 \- Cadastro dos Códigos de Serviços Municipais \(PRT\_SERVICO\_OBRIG\)__

A rotina de importação de tabelas fixas e acessórias deve ser alterada para que a mesma passe a considerar a importação da nova __TFIX85__\.

__OS3208__

RN05

__Regra p/ abertura da tela Parâmetros – Tipo Docto Msaf x Tipo Docto Nota Carioca:__

Ao clicar no menu Parâmetros – Tipo Docto Msaf x Tipo Docto Nota Carioca, o sistema deve exibir a tela de seleção de Estabelecimento/Grupo/Validade para que o usuário possa escolher as informações referentes aos tipos de documentos que serão parametrizados\.

__OS3208__

__RN06__

__Regra do campo Tipo Documento MasterSAF da tela Parâmetros – Tipo Docto Msaf x Tipo Docto Nota Carioca:__

Deverá recuperar as informações da tabela X2005\_TIPO\_DOCTO\. Somente serão recuperadas informações cadastradas no grupo escolhido\. A recuperação dos documentos deve ser realizado através da pastinha amarela\.

__OS3208__

__RN07__

__Regra do campo Tipo Documento Nota Carioca da tela Parâmetros – Tipo Docto Msaf x Tipo Docto Nota Carioca:__

Deverá exibir os tipos de documento definidos no “Manual de Layout”\. Exibir as opções da tabela \- \(__TFIX84__\) \- Cadastro dos Tipos de Documento das Obrigações \- PRT\_TP\_DOCTO\_OBRIG referentes a esse módulo\.

__OS3208__

__RN08__

__Regra do campo Validade da tela Parâmetros – Tipo Docto Msaf x Tipo Docto Nota Carioca:__

Irá permitir que diferentes tipos de documentos cadastrados no MasterSAF possam ser relacionados com o mesmo tipo de documento da Nota Fiscal para diferentes períodos\. A data de validade é do tipo “a partir de”\. Deve conter a máscara DD/MM/AAAA\. 

__OS3208__

__RN09__

__Regra da tela Parâmetros – Tipo Docto Msaf x Tipo Docto Nota Carioca:__

O sistema não permite que os mesmos tipos de documento sejam relacionados com a mesma data de validade\. Nessa situação o sistema deverá exibir a seguinte mensagem de erro: “Não é permitido que os mesmos tipos de documento sejam relacionados com a mesma data de validade”\.

A tela deve conter as seguintes funcionalidades: 

Grupo: ao clicar nesse botão, o sistema abrirá a tela de seleção de Estabelecimento/Grupo/Validade\.

Novo: o sistema criará um novo registro\.

Abrir: o sistema abrirá todos os registros existentes\.

Excluir: o sistema excluirá um registro existente\.

Confirmar: o sistema salvará as informações cadastradas\.

Ordenar: o sistema irá ordenar as informações de acordo com o escolhido\. Deve ser possível realizar a ordenação por todos os campos da tela\.

Relatório: o sistema chamará o relatório de conferência da tela de classificação de serviços\.

Sair: o sistema fechará a tela\.

__OS3208__

__RN10__

__Regra do relatório da tela Parâmetros – Tipo Docto Msaf x Tipo Docto Nota Carioca:__

Deve existir um relatório de conferência que informe os relacionamentos existentes entres os tipos de documentos cadastrados no MasterSAF e os tipos de documentos solicitados pela Nota Carioca\.

__OS3208__

	

RN11

__Regra p/ abertura da tela Parâmetros – Serviços Msaf x Serviços Municipais:__

Ao clicar no menu Parâmetros – Serviços Msaf x Serviços Municipais o sistema deve exibir a tela de seleção de Estabelecimento/Grupo/Validade para que o usuário possa escolher as informações referentes aos serviços que serão parametrizados\.

__OS3208__

__RN12__

__Regra do campo Serviços MasterSAF da tela Parâmetros – Serviços Msaf x Serviços Municipais:__

Deverá recuperar as informações da tabela X2018\_SERVICOS\. Somente serão recuperadas informações cadastradas no grupo escolhido\. A recuperação dos serviços deve ser realizada através da pastinha amarela\.

__OS3208__

__RN13__

__Regra do campo Serviços Municipais da tela Parâmetros – Serviços Msaf x Serviços Municipais:__

Deverá exibir os serviços definidos no “Manual de Layout”\. Exibir as opções da tabela PRT\_SERVICO \_OBRIG \(TFIX85\) referentes a esse módulo\.

__OS3208__

__RN14__

__Regra do campo Validade da tela Parâmetros – Serviços Msaf x Serviços Municipais:__

Irá permitir que diferentes serviços cadastrados no MasterSAF possam ser relacionados com o mesmo código de serviço municipal para diferentes períodos\. A data de validade é do tipo “a partir de”\. Deve conter a máscara DD/MM/AAAA\.

 

__OS3208__

__RN15__

__Regra da tela Parâmetros – Serviços Msaf x Serviços Municipais:__

O sistema não permite que os mesmos serviços sejam relacionados com a mesma data de validade\. Nessa situação o sistema deverá exibir a seguinte mensagem de erro: “Não é permitido que os mesmos serviços sejam relacionados com a mesma data de validade”\.

A tela deve conter as seguintes funcionalidades: 

Grupo: ao clicar nesse botão, o sistema abrirá a tela de seleção de Estabelecimento/Grupo/Validade\.

Novo: o sistema criará um novo registro\.

Abrir: o sistema abrirá todos os registros existentes\.

Excluir: o sistema excluirá um registro existente\.

Confirmar: o sistema salvará as informações cadastradas\.

Ordenar: o sistema irá ordenar as informações de acordo com o escolhido\. Deve ser possível realizar a ordenação por todos os campos da tela\.

Relatório: o sistema chamará o relatório de conferência da tela de classificação de serviços\.

Sair: o sistema fechará a tela\.

__OS3208__

__RN16__

__Regra do relatório da tela Parâmetros – Serviços Msaf x Serviços Municipais:__

Deve existir um relatório de conferência que informe os relacionamentos existentes entres os serviços cadastrados no MasterSAF e os serviços municipais solicitados pela Nota Carioca\.

__OS3208__

__RN17__

__Regra p/ abertura da tela Parâmetros –  Classificação de Serviços:__

Ao clicar no menu Parâmetros – Classificação de Serviços, o sistema deve exibir a tela de seleção de Estabelecimento/Grupo/Validade para que o usuário possa escolher as informações referentes aos serviços que serão classificados\.

__OS3208__

__RN18__

__Regra p/ tela Parâmetros –  Classificação de Serviços:__

Após a seleção do Estabelecimento/Grupo/Validade, o sistema deve exibir a tela de classificação de serviços, contendo os seguintes campos: UF, município, Parâmetro, Serviços, Selecionar Todos e Desmarcar Todos\. Essa tela deve armazenar os dados cadastrados na tabela PRT\_SERVICO\_MUNIC\_MSAF\.

__OS3208__

__RN19__

__Regra p/ opções da tela Parâmetros – Classificação de Serviços:__

Essa tela deve oferecer as seguintes opções ao usuário: 

Grupo: ao clicar nesse botão, o sistema abrirá a tela de seleção de Estabelecimento/Grupo/Validade\.

Novo: o sistema criará um novo registro\.

Abrir: o sistema abrirá um registro existente\. A tela de critério de seleção deve conter todos dos campos da tabela PRT\_SERVICO\_MUNIC\_OBRIG\.

Excluir: o sistema excluirá um registro existente\.

Confirmar: o sistema salvará as informações cadastradas\.

Relatório: o sistema chamará o relatório de conferência da tela de classificação de serviços\.

Sair: o sistema fechará a tela\.

__OS3208__

__RN20__

__Regra p/ campo UF da tela Parâmetros –  Classificação de Serviços:__

O campo “UF” deve ser um combo Box e deve exibir todas as UFs cadastradas na tabela ESTADO\. 

__OS3208__

	

__RN21__

__Regra p/ campo Município da tela Parâmetros –  Classificação de Serviços:__

O campo “Município” deve ser composto por um text Box que permitirá a digitação do código do município \+ pasta amarela para seleção de municípios \+ um text Box desabilitado que irá exibir a descrição do município informado\.

Quando o usuário clicar na pastinha amarela, o sistema de recuperar todos os municípios correspondentes a UF previamente selecionada\. 

__OS3208__

__RN22__

__Regra p/ campo Parâmetro da tela Parâmetros \-  Classificação de Serviços:__

O campo Parâmetro deve ser exibido através de um ListBox e deve exibir as seguintes opções:

- Serviços Isentos – cod\_param = 433
- Serviços Imunes – cod\_param = 420
- Serviços sujeitos a Decisão Judicial – cod\_param = 427
- Serviços sujeitos a Procedimento Administrativo – cod\_param = 470
- Serviços Tributados no Município – cod\_param = 471
- Serviços Tributados Fora do Município – cod\_param = 472

__OS3208__

__RN23__

__Regra p/ campo Serviço da tela Parâmetros –  Classificação de Serviços:__

O campo Serviços deve permitir que o usuário marque quantos serviços forem necessários para a classificação desejada\. O campo deve exibir os campos COD\_SERVICO \+ ‘ – ’ \+ DESCRICAO da tabela X2018\_SERVICOS\.

__OS3208__

__RN24__

__Regra p/ botão Selecionar Todos da tela Parâmetros –  Classificação de Serviços:__

O botão Selecionar Todos deve permitir que o usuário possa selecionar todos os serviços de uma vez\.

__OS3208__

__RN25__

__Regra p/ botão Desmarcar Todos da tela Parâmetros –  Classificação de Serviços:__

O botão Desmarcar Todos deve permitir que o usuário possa desmarcar todos os serviços de uma vez\.

__OS3208__

__RN26__

__Regra de criação do nome do arquivo__

Quando o parâmetro Quebrar Arquivos por Data de Emissão estiver desmarcado será gerado o arquivo com a nomenclatura do arquivo normal indicado abaixo\.

Cada arquivo corresponderá a apenas uma DMS e será identificado por:

__Serviços Tomados:__

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\.TXT__, onde:

       __MMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\.TXT

__NOTA\_CARIOCA\_DDMMAAAA\.txt__, onde:

       __NOTA\_CARIOCA__: representa a obrigação que está sendo gerada\.

       __DDMMAAAA__: representa a data inicial da geração do meio magnético

      __ \.txt__: extensão do arquivo\.   

Quando o parâmetro Quebrar Arquivos por Data de Emissão estiver marcado, deve ser realizado a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente a data de emissão\)\.

Se o parâmetro “Considerar Data do Pagamento para Serviços Tomados com Retenção pelo Tomador” estiver selecionado, esta comparação de diferença de períodos entre Data Fiscal e Data de Emissão deve ocorrer somente para as notas de entrada que tenham o campo Indicador Tipo Retenção \(IND\_TP\_RET\) preenchido com conteúdo diferente de “1” – Retido pelo Tomador, pois para conteúdo igual a “1” será considerada a Data do Pagamento como competência\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverão ser:

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ MMAAAA\_MMAAAA\.TXT__, onde:

       __MMAAAA__: representa a data inicial da geração\.   

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\_012010\.TXT

__NOTA\_CARIOCA\_DDMMAAAA\_MMAAAA\.txt__, onde:

- __NOTA\_CARIOCA__: representa a obrigação que está sendo gerada\.       
- __DDMMAAAA__: representa a data inicial da geração do meio magnético
- __MMAAAA: __mês da competência referente à nota gerada\.
- __\.txt__: extensão do arquivo\.   

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__OBS\.: Este novo parâmetro \(Quebrar Arquivos por Data de Emissão\) será válido, apenas para Notas de Serviços Tomados\.__

__OS3208__

__OS4337__

__OS4558__

__MFS\-21923  
__MFS\-829438

__RN27__

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE\.

__Data Final:__ O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE\. 

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)\.

__Considerar Data do Pagamento para Serv\. Tomados com Retenção pelo Tomador:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = desmarcado\)\.

__Observação:__ Se este parâmetro for marcado, o parâmetro “Considerar Data Emissão para Serv\. Tomados Notas Fiscais Invoices” deve ficar desabilitado para seleção na tela de geração do meio magnético\.

__Considerar Data Emissão para Serv\. Tomados Notas Fiscais Invoices:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = desmarcado\)\. 

__Observação:__ Se este parâmetro for marcado, o parâmetro “Considerar Data do Pagamento para Serv\. Tomados com Retenção pelo Tomador” e o “Quebrar arquivo por Data de Emissão” devem ficar desabilitados para seleção na tela de geração do meio magnético\.

Estabelecimento: o sistema deve exibir os estabelecimentos pertencentes ao município do Rio de Janeiro, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__\[EXCLUSÃO MFS\-901113\]__ Esses campos devem ser um Radiobutton, com as seguintes opções:

__Todas as Notas: __

__Somente Notas com Retenção de ISS: __

__Somente Notas sem Retenção de ISS: __

Por default, a opção __“Todas as Notas”__ deve vir marcada\. 

__Se__ a opção selecionada for igual a __“Todas as Notas”__

    Devem ser geradas todas as notas fiscais no arquivo, “ISS Retido“

__Senão __Se a opção selecionada for igual a __“Somente Notas com Retenção de ISS”__

    Devem ser geradas somente as notas fiscais em que o campo “ISS Retido“  for igual a “1   

    \(ISS Retido\)” no arquivo

__Senão__ Se a opção selecionada for igual a __“Somente Notas sem Retenção de ISS”__

   Devem ser geradas somente as notas fiscais em que o campo  “ISS Retido“ for igual a “0 – 

   \(sem ISS Retido\)” no arquivo\.

 

__Obs\.:__ As notas fiscais que serão geradas no arquivo serão recuperadas conforme as regras de recuperação já existentes\.  Este parâmetro serve para gerar as notas separadamente, conforme a opção escolhida, mas somente para a geração dos serviços tomados \(notas de entrada\)\.

__OS3208__

__OS4337__

__OS4558__

__MFS\-21923__

__MFS\-766555__

MFS\-901113

__RN28__

__Regra de Estrutura e Disposição de cada registro no arquivo__

Registro Tipo 10 \(Obrigatório\): Uma linha de cabeçalho\. Primeira linha do arquivo\.

Registro Tipo 40 \(Opcional\): Zero ou mais linhas de detalhe\. Cada linha corresponde a uma Nota Fiscal Convencional Recebida\.

Registro Tipo 90 \(Obrigatório\): Uma linha de rodapé\. Última linha do arquivo\.

__OS3208__

__RN29__

__Regra de formatação do arquivo__

Todos os campos numéricos deverão ser preenchidos alinhados pela direita e sem formatação \(sem ponto e sem vírgula\)\. Se necessário, preencher com zeros à esquerda até completar seu tamanho máximo\. Quando o campo for opcional, ou seja, o conteúdo do campo não seja fornecido, este deverá ser preenchido com zeros até completar seu tamanho máximo\.

Todos os campos alfanuméricos deverão ser preenchidos alinhados pela esquerda\. Se necessário, preencher com espaços em branco à direita até completar seu tamanho máximo, com exceção do campo de Discriminação dos Serviços da linha de detalhe do registro 40\. Quando o campo for opcional, ou seja, quando o conteúdo do campo não é fornecido, este deverá ser preenchido com espaços em branco até completar seu tamanho máximo\.

__OS3208__

__RN30__

__Regra do Registro Tipo 10 – Cabeçalho__

Esse registro deve conter informações referentes ao estabelecimento contribuinte escolhido na tela de geração do meio magnético

__OS3208__

__RN31__

__Regra do Registro Tipo 10 – Campo Tipo de Registro__

Preencher com “10”\.

__OS3208__

__RN32__

__Regra do Registro Tipo 10 – Campo Versão do Arquivo__

Preencher com “003”\.

__OS3208__

__RN33__

__Regra do Registro Tipo 10 – Campo Identificação CPF ou CNPJ do Contribuinte__

Preencher com:

1, quando o campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento escolhido da geração do meio magnético tiver 11 posições\.

2, quando o campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento escolhido da geração do meio magnético tiver 14 posições\.

__OS3208__

__RN34__

__Regra do Registro Tipo 10 – Campo CPF ou CNPJ do Contribuinte__

Preencher com o campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento escolhido da geração do meio magnético\.

__OS3208__

__RN35__

__Regra do Registro Tipo 10 – Campo Inscrição Municipal do Contribuinte__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO referente ao estabelecimento escolhido da geração do meio magnético\.

__OS3208__

__RN36__

__Regra do Registro Tipo 10 – Campo Data de Início do Período Transferido no Arquivo__

Preencher com o campo “Data Inicial” da tela de geração do meio magnético\. Formato AAAAMMDD\.

__OS3208__

__RN37__

__Regra do Registro Tipo 10 – Campo Data de Fim do Período Transferido no Arquivo__

Preencher com o campo “Data Final” da tela de geração do meio magnético\. Formato AAAAMMDD\.

__OS3208__

__RN38__

__Regra do Registro Tipo 10 – Campo Caractere de Fim de Linha__

Preencher com caractere de fim de linha “Enter” \(Chr\(13\) \+ Chr\(10\)\)\.

__OS3208__

__RN39__

__Regra do Registro Tipo 40 – Declaração de Notas Convencionais Recebidas__

Recuperar notas com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3

MFS21923 \- Seleção do Parâmetro: “Considerar Data de Emissão para Serv\. Tomados Notas Fiscais Invoices”\.

- Se o parametro “Considerar Data de Emissão para Serv\. Tomados Notas Fiscais Invoices” estiver selecionado na tela de geração, considerar as notas fiscais cujo o campo Clas\. Doc\.Fiscal \(COD\_CLASS\_DOC\_FIS\) = “I”, Indicador Tipo Retenção \(IND\_TP\_RET\) tenha conteúdo igual a “1” – Retido pelo Tomador, considerar como critério de seleção o campo Data de Emissão \(DATA\_EMISSAO\)\.
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência quando o parâmetro “Considerar Data do Pagamento para Serv\. Tomados com Retenção pelo Tomador” não estiver selecionado\. Se o parametro “Considerar Data do Pagamento para Serv\. Tomados com Retenção pelo Tomador” estiver selecionado na tela de geração, considerar a Data Fiscal para as notas cujo campo Indicador Tipo Retenção \(IND\_TP\_RET\) tenha conteúdo diferente de “1” – Retido pelo Tomador\. Para as notas cujo campo Indicador Tipo Retenção \(IND\_TP\_RET\) tenha conteúdo igual a “1” – Retido pelo Tomador, considerar como critério de seleção o campo Data do Pagamento \(DT\_PAGTO\_NF\)\.
- Data fiscal dentro do período de referência
- Notas não canceladas \(SITUACAO <> ‘S’\)
- Não recuperar documentos fiscais equiparados à construção civil \(IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota\) e que cujo campo Tipo da Nota Convencional seja = ‘6’ \(Nota Fiscal Remessa de Material e Equipamento\)

__\[ALTERADA – CH23373\_2016/ MFS\-1018598\] __

- Desconsiderar notas fiscais eletrônicas, em que o município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for IGUAL do município do estabelecimento selecionado para geração \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\(\*\) 

__\[ALTERADA – CH13966\_2017\]__

Não recuperar as notas fiscais cujo prestador de serviço estiver enquadrado como MEI campo 27 \(IND\_CLASSE\_EMP\) da SAFX 04 = ‘5’ na geração do meio magnético da Nota Carioca\.

Observações: __\(\*\) __*A Prefeitura do Rio de Janeiro não permite mais a emissão de nota fiscal convencional, portanto todas as notas são emitidas eletronicamente\. *

*Em regra no Mastersaf DW utilizamos a verificação por meio de modelo ou se o tipo do documento corresponde a NF\-e, porém o contribuinte do ISS não possui modelo para nota de serviços, teoricamente ele não é obrigado a preencher com um modelo específico na SAFX07, esse parâmetro foi criado anteriormente e instruido aos clientes para conseguir diferenciar a nota eletrônica de serviço das notas convencionais para saber o que seria enviado no arquivo magnético conforme exigência da Prefeitura\.*

*Vamos levar para o arquivo magnético as notas de serviços tomados independente do modelo ou tipo do documento, mas que sejam de fora do município do Rio de Janeiro, pois as de dentro, por já existirem no portal da nota eletrônica, não precisam ser declaradas\.*

As notas fiscais eletrônicas cujo prestador \(SAFX04\) é do Rio de Janeiro não devem ser geradas no arquivo\. Para identificar notas fiscais eletrônicas, o mastersaf possui duas formas:

1. Através do modelo 55
2. Através o campo NF\-e \(Nota Fiscal Eletrônica\) da tela de cadastro de tipos de documentos marcado

Dessa forma deve\-se primeiro identificar se a nota é uma nota fiscal eletrônica e depois verificar se o prestador é ou não do RJ e assim gerar ou não a nota no arquivo\. Conforme regra abaixo:

Se o campo IND\_NF\_ELETRONICA da SAFX2005 = “S”, verificar \(independente do modelo da nota fiscal\):

       Se o município da pessoa fis/jur for __IGUAL__ ao município do estabelecimento

             A nota __NÃO__ deve ser gerada no arquivo magnético

       Se o município da pessoa fis/jur for __DIFERENTE__ do município do estabelecimento  

            A nota deve ser gerada no arquivo magnético

                                                       OU

Se o modelo da nota fiscal for igual a 55, verificar:

       Se o município da pessoa fis/jur for __IGUAL__ ao município do estabelecimento

             A nota __NÃO__ deve ser gerada no arquivo magnético

       Se o município da pessoa fis/jur for __DIFERENTE__ do município do estabelecimento  

            A nota deve ser gerada no arquivo magnético

__OS3208__

__CH4804\_2012__

CH1191\_2012

__CH4804\_2012\-A__

__CH4804\_2012\-B__

__CH24039__

__OS4430__

__OS4558__

__CH23373\_2016__

__CH13996\_2017__

__MFS\-21923__

__MFS\-1018598__

__RN40__

__Regra do Registro Tipo 40 – Campo Tipo de Registro__

Preencher com “40”

__OS3208__

__RN41__

__Regra do Registro Tipo 40 – Campo Tipo da Nota Convencional__

Preencher com o campo Tipo Docto Nota Carioca da tela Parâmetros – Tipo Docto Msaf x Tipo Docto Nota Carioca referente ao tipo de documento cadastrado na nota fiscal\.

__OS3208__

__RN42__

__Regra do Registro Tipo 40 – Campo Série da Nota Convencional__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 09 da SAFX07\)

__OS3208__

__RN43__

__Regra do Registro Tipo 40 – Campo Número da Nota Convencional__

__Tela\-A__ __ Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Campo deverá ser limitado a 15 posições conforme layout, caso ultrapasse emitir log de erro alertando o tamanho do campo: Log “__Campo limitado a 15 posições de acordo com layout__” 

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

  __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ __ __  

  __E__

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __ 

Então, Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL__

Se não,

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\)

__OS3208__

__OS3341\-A3__

__MFS\-91197__

__RN44__

__Regra do Registro Tipo 40 – Campo Data de Emissão da Nota Convencional__

 Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAFX07\)\. Formato AAAAMMDD\.

__OS3208__

__RN45__

__Regra do Registro Tipo 40 – Campo Status da Nota Convencional__

Preencher com:

1, quando campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> ‘S’ \(campo 30 da SAFX07\)

2, quando campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = ‘S’ \(campo 30 da SAFX07\)

__OS3208__

__RN46__

__Regra do Registro Tipo 40 – Campo Identificação de CPF ou CNPJ do Prestador__

Preencher com:

1, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal tiver 11 posições\. \(campo 06 da SAFX04\)

2, quando o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal tiver 14 posições\. \(campo 06 da SAFX04\)

3, quando não se enquadrar nas situações acima

__OS3208__

__RN47__

__Regra do Registro Tipo 40 – Campo CPF ou CNPJ do Prestador__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 06 da SAFX04\)\. 

Sem formatação \(ponto, traço, barra, \.\.\.\)

Se o campo “Identificação de CPF ou CNPJ do Prestador” for preenchido com “3”, preencher com zeros\.

__OS3208__

__RN48__

__Regra do Registro Tipo 40 – Campo Inscrição Municipal do Prestador__

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 09 da SAFX04\)

Se o campo COD\_MUNIICIPIO da X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal for diferente do município do Rio de Janeiro, esse campo deve ser preenchido com zeros\.

__OS3208__

__/__

CH114061

__RN49__

__Regra do Registro Tipo 40 – Campo Inscrição Estadual do Prestador__

Preencher com o campo INSC\_ESTADUAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 08 da SAFX04\)

__OS3208__

__RN50__

__Regra do Registro Tipo 40 – Campo Nome ou Razão Social do Prestador__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 05 da SAFX04\)

__OS3208__

__RN51__

__Regra do Registro Tipo 40 – Campo Tipo do Endereço do Prestador \(Rua, Av, \.\.\.\)__

Preencher com o campo TP\_LOGRADOURO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 42 da SAFX04\)

__OS3208__

__RN52__

__Regra do Registro Tipo 40 – Campo Endereço do Prestador__

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 12 da SAFX04\)

__OS3208__

__RN53__

__Regra do Registro Tipo 40 – Campo Número do Endereço do Prestador__

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 13 da SAFX04\)

__OS3208__

__RN54__

__Regra do Registro Tipo 40 – Campo Complemento do Endereço do Prestador__

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 14 da SAFX04\)

__OS3208__

__RN55__

__Regra do Registro Tipo 40 – Campo Bairro do Prestador__

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 15 da SAFX04\)

__OS3208__

__RN56__

__Regra do Registro Tipo 40 – Campo Cidade do Prestador__

Preencher com o campo DESCRICAO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 25 da SAFX04\)

__OS3208__

__RN57__

__Regra do Registro Tipo 40 – Campo UF do Prestador__

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao campo IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 19 da SAFX04\)

__OS3208__

__RN58__

__Regra do Registro Tipo 40 – Campo CEP do Prestador__

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 20 da SAFX04\)

__OS3208__

__RN59__

__Regra do Registro Tipo 40 – Campo Telefone de Contato do Prestador__

Preencher com o campo TELEFONE da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 23 da SAFX04\)

__OS3208__

__RN60__

__Regra do Registro Tipo 40 – Campo E\-mail do Prestador__

Preencher com o campo E\_MAIL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\. \(campo 40 da SAFX04\)

__OS3208__

__RN61__

__Regra do Registro Tipo 40 – Campo Tipo de Tributação de Serviços__

Preencher com:

01, quando o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “471”\.

02, quando o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “472”\.

03, quando o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

__Isenta__

03, quando o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433” ou campo Base Isenta ISS da capa do documento fiscal \(safx07\) estiver > zero

__Tributado no município__

01, se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1” e se o local da prestação do serviço = município do módulo selecionado

__OU__ 

se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado 

__OU__

se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado__ __

__OU__

se os campos Valor da Base de ISS Retido \(VLR\_BASE\_ISS\_RETIDO\) e Valor do ISS Retido \(VLR\_ISS\_RETIDO\) da SAFX09 igual a zero __E__ o campo Indicador Tipo Retenção \(IND\_TP\_RET\) da SAFX07 estiver preenchido com “2” __E__ o Código do Município do Prestador \(COD\_MUNICIPIO\) na SAFX04 for igual ao município do módulo

__\[MFS72456\]__ Tratamento para a PFJ cadastrada no CEPOM, que deve gerar o campo Tipo de Tributação de Serviços como Tributado no município\.  E inclusão de mais um tratamento para a situação de Tributado no município\.

__OU__

se os campos Valor da Base de ISS Retido \(VLR\_BASE\_ISS\_RETIDO\) e Valor do ISS Retido \(VLR\_ISS\_RETIDO\) da SAFX09 igual a zero __E__ o campo Indicador Tipo Retenção \(IND\_TP\_RET\) da SAFX07 estiver preenchido com “2” __E__ o Código do Município do Prestador \(COD\_MUNICIPIO\) na SAFX04 for diferente do município do módulo e o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “14” \(CEPOM\)

__OU__

se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “471”\.

__Tributado fora do município__

__\[Alterado OS3985\]__

02, quando o campo IND\_TP\_RET = “1” ou “2” e COD\_MUNICIPIO da capa do documento fiscal \(safx07\) for diferente ao município de geração da obrigação \(Rio de Janeiro\), 

OU

se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “472”\.

OU

se os campos Valor da Base de ISS Retido \(VLR\_BASE\_ISS\_RETIDO\) e Valor do ISS Retido \(VLR\_ISS\_RETIDO\) da SAFX09 igual a zero __E__ o campo Indicador Tipo Retenção \(IND\_TP\_RET\) da SAFX07 estiver preenchido com “2” __E__ o Código do Município do Prestador \(COD\_MUNICIPIO\) na SAFX04 for diferente do município do módulo 

__Imune__

04, quando o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”\.

__Operação Suspensa por Decisão Judicial__

05, quando o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “09”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427”\.

__Operação Suspensa por Decisão Administrativa__

06, quando o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “470”\.

__OS3208__

__CH14104__

__CH19374__

__OS3985__

__OS4558__

__MFS\-72456__

__RN62__

__Regra do Registro Tipo 40 – Campo Reservado__

Preencher com brancos\.

__OS3208__

__RN63__

__Regra do Registro Tipo 40 – Campo Opção pelo Simples__

__\[EXCLUIDO\] CH19775__

Preencher com:

0, quando o campo IND\_ISS da tabela ESTABELECIMENTO <> “07”

1, quando o campo IND\_ISS da tabela ESTABELECIMENTO = “07”

\[ALTERADO\] CH19775

Preencher com:

0, quando o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR <> “S”

1, quando o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR = “S”

__OS3208__

__CH19775__

__RN64__

__Regra do Registro Tipo 40 – Campo Código do Serviço Federal__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao campo IDENT\_SERV\_LEI\_116 relacionado ao serviço cadastrado na nota fiscal\.

O campo deve ser preenchido sem formatação\. Ex: “07\.20” será “0720”\.

__OS3208__

__RN64A__

__Regra do Registro Tipo 40 – Campo Reservado__

Preencher com brancos\.

__OS3842__

__RN64B__

__Regra do Registro Tipo 40 – Campo Código do Benefício__

__\[MFS865358\] __Alteração da regra de preenchimento do campo para verificar o campo Tipo de Tributação de Serviços

Se o campo Tipo de Tributação de Serviços for igual a “03” ou “04”

     Preencher com o campo Benefício Fiscal da tela Parâmetros – Serviço x Benefício Fiscal referente ao serviço                          

     cadastrado na nota fiscal

Senão 

     O campo não deve ser preenchido\.

__OS3842__

__MFS865358__

__RN65__

__Regra do Registro Tipo 40 – Campo Código do Serviço Municipal__

Se o serviço cadastrado na nota fiscal está parametrizado na tela Parâmetros – Serviços – Serviços Msaf x Serviços Municipais\. 

	Preencher com o campo Serviços da tela Parâmetros – Serviços – Serviços Msaf x Serviços Municipais

Senão

Verificar se o serviço da lei 116 relacionado ao serviço cadastrado na nota fiscal está parametrizado na tela  Parâmetros – Serviços – Serviços Lei 116 x Serviços Municipais

		Se sim, preencher com o campo Serviços da tela Parâmetros – Serviços – Serviço Lei 116 x Serviços Municipais\.

		Se não, deve\-se gerar o campo em branco e exibir a mensagem no log: “O serviço cadastrado na nota fiscal e o código do serviço da Lei 116 referente ao mesmo, não estão parametrizados no menu Parâmetros – Serviços”\.

Se o mesmo serviço cadastro na nota fiscal estiver parametrizado nas duas telas, deve\-se considerar o que está parametrizado na tela Serviços da tela Parâmetros – Serviços – Serviços Msaf x Serviços Municipais e deve\-se exibir uma mensagem no log informando ao usuário que será considerado o que está parametrizado na tela Parâmetros – Serviços – Serviços Msaf x Serviços Municipais\.

O campo deve ser preenchido sem formatação\. Ex: “07\.20\.10” será “00000000000000072010”\.

__OS3208__

__OS3723__

__RN66__

__Regra do Registro Tipo 40 – Campo Alíquota__

__Se__ DWT\_ITENS\_SERV\-__VLR\_ALIQ\_ISS\_RETIDO__ > 0 __Então__ 

    Preencher o campo Alíquota, com os dados da coluna DWT\_ITENS\_SERV\-__VLR\_ALIQ\_ISS\_RETIDO__

__Senão se__ DWT\_ITENS\_SERV\-__ALIQ\_TRIBUTO\_ISS__ > 0 __Então__ 

    Preencher o campo Alíquota, com os dados da coluna DWT\_ITENS\_SERV\-__ALIQ\_TRIBUTO\_ISS__

__Senão__

__    __Exibir a mensagem: Atenção, a alíquota não foi preenchida\.

__Fim Se__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 32 da SAFX09\)

IMPORTANTE: Incluir duas casas decimais \(sem ponto, sem vírgula e sem %\)\.

__OS3208__

__MFS\-656575__

__RN67__

__Regra do Registro Tipo 40 – Campo Valor dos Serviços__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. \(campo 14 da SAFX09\)

Incluindo os centavos \(sem ponto decimal e sem R$\)

Caso o campo “Status da Nota” = “2” \(Cancelada\), preencher com zeros\.

__OS3208__

__RN68__

__Regra do Registro Tipo 40 – Campo Valor das Deduções__

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 59 da SAFX09\)

Incluindo os centavos \(sem ponto decimal e sem R$\)

__OS3208__

__RN69__

__Regra do Registro Tipo 40 – Campo Reservado__

Preencher com brancos\.

__OS3208__

__RN70__

__Regra do Registro Tipo 40 – Campo Valor do ISS__

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 33 da SAFX09\)

Incluindo os centavos \(sem ponto decimal e sem R$\)

__OS3208__

__RN71__

__Regra do Registro Tipo 40 – Campo ISS Retido__

Preencher com “1”, quando pelo menos umas das seguintes opções seja verdadeira:

__\[EXCLUÍDA – CH9872\_2014\]:__

Atendidas uma das regras acima, recuperar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\. 

Com o município do local da prestação recuperado, verificar as seguintes opções:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1” e se o local da prestação do serviço = município do módulo selecionado __OU__  
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado __OU__
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

<a id="OLE_LINK33"></a><a id="OLE_LINK34"></a><a id="OLE_LINK35"></a>Para os casos de prestador __NÃO__ cadastrado no __CEPOM__:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1” e se o município do módulo <> município do prestador \(campo COD\_MUNIC da tabela X04\_PESSOA\_FIS\_JUR\)__ E__ os campos Valor da Base de ISS Retido \(VLR\_BASE\_ISS\_RETIDO\) e Valor do ISS Retido \(VLR\_ISS\_RETIDO\) da SAFX09 foram maiores que zero\.\.

Caso nenhuma das opões seja verdadeira, preencher com “0”\.

__OS3208__

__CH15536__

__CH29819\_2013__

__CH9872\_2014__

__OS4558__

__MFS\-90229__

__RN72__

__Regra do Registro Tipo 40 – Campo Data de Competência  Data de Referência para Definição da Competência\.__

Preencher com o campo DAT\_FATO GERADOR da tabela DWT\_DOCTO\_FISCAL \(campo 93 da SAFX07\), quando as condições abaixo forem verdadeiras:

Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL está preenchido\. 

Se estiver preenchido, verificar se está preenchido com “1”\.

Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.

Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

Se o campo DAT\_FATO GERADOR da tabela DWT\_DOCTO\_FISCAL está preenchido\.

E se a data do campo DAT\_FATO GERADOR é menor que a DATA\_FISCAL da tabela DWT\_DOCTO\_FISCAL

E se a data do campo DAT\_FATO GERADOR é igual ou menor que a DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. \(campo 11 da SAFX07\)

Preencher com o campo DAT\_FATO GERADOR da tabela DWT\_DOCTO\_FISCAL \(campo 93 da SAFX07\),

Caso nenhuma das opões seja verdadeira, preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. \(campo 11 da SAFX07\)

Obs\.: O campo DAT\_FATO GERADOR da tabela DWT\_DOCTO\_FISCAL será considerado como a data da prestação do serviço e deve ser igual ou menor que à data de emissão da NFS, conforme layout 

Preencher com o campo __DT\_PAGTO\_NF__ __DATA\_EMISSÃO __da tabela __DWT\_DOCTO\_FISCAL__ 

Preencher com o campo DT\_PAGTO\_NF da tabela DWT\_DOCTO\_FISCAL \(campo da SAFX07\), quando pelo menos umas das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.

Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

Caso nenhuma das opões seja verdadeira, preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. \(campo da SAFX07\)

__OS3208__

__MFS\-86017__

__MFS\-98578__

__RN73__

__Regra do Registro Tipo 40 – Campo Código da Obra__

Preencher com o campo COD\_CEI da tabela DWT\_DOCTO\_FISCAL\. Caso o campo COD\_CEI não esteja informado na nota, esse campo deve ser preenchido com o campo COD\_CANAL\_DISTRIB da tabela DWT\_DOCTO\_FISCAL\.

__OS3842__

__CH30809/2012__

__RN73A__

__Regra do Registro Tipo 40 – Anotação de Responsabilidade Técnica__

Preencher com brancos\. 

__OS3842__

__CH30809/2012__

__RN74__

__Regra do Registro Tipo 40 – Campo Discriminação dos Serviços__

Preencher com brancos\.

__OS3208__

__RN75__

__Regra do Registro Tipo 40 – Campo Caractere de Fim de Linha__

Preencher com caractere de fim de linha “Enter” \(Chr\(13\) \+ Chr\(10\)\)\.

__OS3208__

__RN75\.a__

__Regra do Registro Tipo 50 – Declaração de Materiais __

__\[ALTERADA – MFS3631\]__

\- Para que esse registro 50 seja gerado, a nota fiscal recebida deverá ser __de construção civil \(IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota\)__ parametrizada na tela de Tipo Docto Msaf x Tipo Docto Nota Carioca como tipo = __‘6’__ \(Nota Fiscal Remessa de Material e Equipamento\)\. Esta tela fica localizada no módulo Rio de Janeiro – Nota Carioca, menu Parâmetros\.

__\[ALTERADA – CH11904\_2016\]__

\- O sistema deverá considerar notas fiscais de classificação do documento igual a 1, 2 e 3 \(campo COD\_CLASS\_DOC\_FIS da tabela SAFX07\); e a classificação do documento igual a 1 \(campo COD\_CLASS\_DOC\_FIS da tabela SAFX07\) quando o campo Valor da Dedução do ISS \(campo VLR\_DEDUCAO\_ISS da tabela SAFX07\) for maior que zero; 

\- A geração deve verificar se existe dedução de material para as notas no Menu: Manutenção>>Materiais\. Não deverá existir restrição de modelo de documento, considerando também nota fiscal eletrônica de modeloc\.

Se para o documento fiscal não for preenchido os campos obrigatórios da aba Materiais, sistema deve exibir no log a seguinte mensagem: “Existem campos do registro 50 que não foram informados\. Favor verificar a aba Materiais da tela de Manutenção de Materiais\.”\.

__OS4430__

__MFS3631__

__CH11904\_2016__

__RN75\.b__

__Regra do Registro Tipo 50 – Campo Tipo do registro__

Preencher com “50”\.

__OS4430__

__RN75\.c__

__Regra do Registro Tipo 50 – Campo Espécie__

Para o documento fiscal parametrizado em manutenção de declaração de materiais, verificar:

Se opção do campo Espécie = “000 \- Nota Fiscal de Materiais \(NFM\)”, preencher com ‘000’\.

Se opção do campo Espécie = “001 \- Nota de Remessa de Materiais e Equipamentos \(NRME\)”, preencher com ‘001’\.

Campo obrigatório\.

__OS4430__

__RN75\.d__

__Regra do Registro Tipo 50 – Campo Série__

Preencher com o campo Série Doc\. Fiscal informada na aba Documento Fiscal da tela de Manutenção de Materiais\.

Campo obrigatório\.

__OS4430__

__RN75\.e__

__Regra do Registro Tipo 50 – Campo Número__

Preencher com o campo Número Doc\. Fiscal informada na aba Documento Fiscal da tela de Manutenção de Materiais\.

Campo obrigatório\.

__OS4430__

__RN75\.f__

__Regra do Registro Tipo 50 – Campo Data Emissão__

Preencher com o campo Data Emissão informada na aba Documento Fiscal da tela de Manutenção de Materiais\.

Formato: AAAAMMDD

Campo obrigatório\.

__OS4430__

__RN75\.g__

__Regra do Registro Tipo 50 – Campo Status__

Preencher com:

1, quando campo SITUAÇÃO da tabela DWT\_DOCTO\_FISCAL relacionado ao documento fiscal selecionado na aba Documento Fiscal estiver preenchido com a opção “N”\.

2, quando campo SITUAÇÃO da tabela DWT\_DOCTO\_FISCAL relacionado ao documento fiscal selecionado na aba Documento Fiscal estiver preenchido com a opção “S”\.

Campo obrigatório\.

__OS4430__

__RN75\.h__

__Regra do Registro Tipo 50 – Campo CNPJ do Emissor da Nota de Materiais/Remessa__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur informada no campo Pessoa Fis/Jur, na aba Documento Fiscal da tela de Manutenção de Materiais\.

Sem formatação \(ponto, traço, barra, \.\.\.\)\.

Campo obrigatório\.

__OS4430__

__RN75\.i__

__Regra do Registro Tipo 50 – Campo Razão Social do Emissor da Nota de Materiais/Remessa__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur informada no campo Pessoa Fis/Jur, na aba Documento Fiscal da tela de Manutenção de Materiais\.

Campo obrigatório\.

__OS4430__

__RN75\.j__

__Regra do Registro Tipo 50 – Campo Tipo do Endereço do Emissor da Nota de Materiais/Remessa__

Preencher com o campo TP\_LOGRADOURO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur informada no campo Pessoa Fis/Jur, na aba Documento Fiscal da tela de Manutenção de Materiais\.

Campo obrigatório\.

__OS4430__

__RN75\.k__

__Regra do Registro Tipo 50 – Campo Endereço do Emissor da Nota de Materiais/Remessa__

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur informada no campo Pessoa Fis/Jur, na aba Documento Fiscal da tela de Manutenção de Materiais\.

Campo obrigatório\.

__OS4430__

__RN75\.l__

__Regra do Registro Tipo 50 – Campo Número Endereço do Emissor da Nota de Materiais/Remessa__

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur informada no campo Pessoa Fis/Jur, na aba Documento Fiscal da tela de Manutenção de Materiais\.

Campo obrigatório\.

__OS4430__

__RN75\.m__

__Regra do Registro Tipo 50 – Campo Complemento do Endereço do Emissor da Nota de Materiais/Remessa__

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur informada no campo Pessoa Fis/Jur, na aba Documento Fiscal da tela de Manutenção de Materiais\.

Campo obrigatório\.

__OS4430__

__RN75\.n__

__Regra do Registro Tipo 50 – Campo Bairro do Emissor da Nota de Materiais/Remessa__

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur informada no campo Pessoa Fis/Jur, na aba Documento Fiscal da tela de Manutenção de Materiais\.

Campo obrigatório\.

__OS4430__

__RN75\.o__

__Regra do Registro Tipo 50 – Campo Cidade do Emissor da Nota de Materiais/Remessa__

Preencher com o campo DESCRICAO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur informada no campo Pessoa Fis/Jur, na aba Documento Fiscal da tela de Manutenção de Materiais\.

Campo obrigatório\.

__OS4430__

__RN75\.p__

__Regra do Registro Tipo 50 – Campo UF Emissor da Nota de Materiais/Remessa__

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao campo IDENT\_ESTADO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur informada no campo Pessoa Fis/Jur, na aba Documento Fiscal da tela de Manutenção de Materiais\.

Campo obrigatório\.

__OS4430__

__RN75\.q__

__Regra do Registro Tipo 50 – Campo CEP emissor da Nota de Materiais/Remessa__

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur informada no campo Pessoa Fis/Jur, na aba Documento Fiscal da tela de Manutenção de Materiais\.

Campo obrigatório\.

__OS4430__

__RN75\.r__

__Regra do Registro Tipo 50 – Campo Código da Obra Origem__

Preencher com o campo Cód\. Obra Origem da aba Materiais da tela de Manutenção de Materiais\.

__OS4430__

__RN75\.s__

__Regra do Registro Tipo 50 – Campo Código da Obra Destino__

Preencher com o campo Cód\. Obra Destino da aba Materiais da tela de Manutenção de Materiais\.

__OS4430__

__RN75\.t__

__Regra do Registro Tipo 50 – Campo Valor Incorporado__

Preencher com o campo Valor Incorporado, da aba Documento Fiscal da tela de Manutenção de Materiais 

Campo obrigatório\.

__OS4430__

__RN75\.u__

__Regra do Registro Tipo 50 – Campo Valor Uso e Consumo__

Preencher com o campo Valor Uso e Consumo, da aba Materiais da tela de Manutenção de Materiais\.

Campo obrigatório\.

__OS4430__

__RN75\.v__

__Regra do Registro Tipo 50 – Campo Valor Total da Nota__

Preencher com o campo VLR\_TOT\_NOTA da tabela DWT\_DOCTO\_FISCAL\.

Campo obrigatório\.

__OS4430__

__RN75\.x__

__Regra do Registro Tipo 50 – Campo Caractere de Fim de Linha __

Preencher com caractere de fim de linha “Enter” \(Chr\(13\) \+ Chr\(10\)\)\.

__OS4430__

__RN76__

__Regra do Registro Tipo 90 – Rodapé__

Preencher com o total dos valores informados no registro tipo 40\.

__OS3208__

__RN77__

__Regra do Registro Tipo 90 – Campo Tipo de Registro__

Preencher com “90”\.

__OS3208__

__RN78__

__Regra do Registro Tipo 90 – Campo Número de linhas do detalhe do arquivo__

Preencher com a quantidade de registros do tipo 40 e do tipo 50 gerados no arquivo\.

__OS3208__

__OS4430__

__RN79__

__Regra do Registro Tipo 90 – Campo Valor total dos serviços contidos no arquivo__

Preencher com o somatório dos valores dos serviços dos registros do tipo 40 e com o somatório do campo Valor Total da Nota dos registros do tipo 50\.

__OS3208__

__OS4430__

__RN80__

__Regra do Registro Tipo 90 – Campo Valor total das deduções contidas no arquivo__

Preencher com o somatório dos valores das deduções dos registros do tipo 40\.

__OS3208__

__RN81__

__Regra do Registro Tipo 90 – Campo Valor total dos descontos condicionados contidos no arquivo__

 Preencher com zeros\.

__OS3208__

__RN82__

__Regra do Registro Tipo 90 – Campo Valor total dos descontos incondicionados contidos no arquivo__

Preencher com zeros\.

__OS3208__

__RN83__

__Regra do Registro Tipo 90 – Campo Caractere de Fim de Linha__

Preencher com caractere de fim de linha “Enter” \(Chr\(13\) \+ Chr\(10\)\)\.

__OS3208__

RN84

__Regra do campo Serviços Lei 116 da tela Parâmetros – Serviços – Serviços Lei 116 x Serviços Municipais:__

Deverá recuperar as informações da tabela DWT\_SERVICO\_LEI\_116\. A recuperação dos serviços deve ser realizada através da pastinha amarela\.

__OS3723__

__RN85__

__Regra do campo Serviços Municipais da tela Parâmetros – Serviços – Serviços Lei 116 x Serviços Municipais:__

Deverá exibir os serviços definidos no “Manual de Layout”\. Exibir as opções da tabela PRT\_SERVICO \_OBRIG \(TFIX85\) referentes a esse módulo\.

__OS3723__

__RN86__

__Regra do campo Validade da tela Parâmetros – Serviços – Serviços Lei 116 x Serviços Municipais:__

Irá permitir que o mesmo serviço da Lei 116 possa ser relacionado à diferentes códigos de serviços municipais para diferentes períodos\. A data de validade é do tipo “a partir de”\. Deve conter a máscara DD/MM/AAAA\. 

__OS3723__

__RN87__

__Regra da tela Parâmetros – Serviços – Serviços Lei 116 x Serviços Municipais:__

O sistema não permite que os mesmos serviços Lei 116 sejam relacionados com a mesma data de validade\. Nessa situação o sistema deverá exibir a seguinte mensagem de erro: “Não é permitido que os mesmos serviços Lei 116 sejam relacionados com a mesma data de validade”\.

A tela deve conter as seguintes funcionalidades: 

Novo: o sistema criará um novo registro\.

Abrir: o sistema abrirá todos os registros existentes\.

Excluir: o sistema excluirá um registro existente\.

Confirmar: o sistema salvará as informações cadastradas\.

Ordenar: o sistema irá ordenar as informações de acordo com o escolhido\. Deve ser possível realizar a ordenação por todos os campos da tela\.

Relatório: o sistema chamará o relatório de conferência da tela de classificação de serviços\.

Sair: o sistema fechará a tela\.

__OS3723__

__RN88__

__Regra do relatório da tela Parâmetros – Serviços – Serviços Lei 116 x Serviços Municipais:__

Deve existir um relatório de conferência que informe os relacionamentos existentes entres os serviços cadastrados no MasterSAF e os serviços municipais solicitados pela Nota Carioca\.

__OS3723__

__RN89__

__Regra da tela Parâmetros – Serviço Msaf x Benefício Fiscal:__

O sistema não permite que os mesmos serviços sejam relacionados com a mesma data de validade\. Nessa situação o sistema deverá exibir a seguinte mensagem de erro: “Não é permitido que os mesmos serviços sejam relacionados com a mesma data de validade”\.

A tela deve conter as seguintes funcionalidades: 

Grupo: ao clicar nesse botão, o sistema abrirá a tela de seleção de Estabelecimento/Grupo/Validade\.

Novo: o sistema criará um novo registro\.

Abrir: o sistema abrirá todos os registros existentes\.

Excluir: o sistema excluirá um registro existente\.

Confirmar: o sistema salvará as informações cadastradas\.

Ordenar: o sistema irá ordenar as informações de acordo com o escolhido\. Deve ser possível realizar a ordenação por todos os campos da tela\.

Relatório: o sistema chamará o relatório de conferência da tela de parametrização

Sair: o sistema fechará a tela\.

__OS3842__

__RN90__

__Regra p/ abertura da tela Parâmetros – Serviço Msaf x Benefício Fiscal – Grupo do Serviço:__

Ao clicar no menu Parâmetros – Série x Benefício Fiscal__ __o sistema deve exibir a tela de seleção de grupos para que o usuário possa escolher o grupo do serviço a ser parametrizado\.

__OS3842__

__RN91__

__Regra do campo Validade da tela Parâmetros – Serviço Msaf x Benefício Fiscal:__

Irá permitir que diferentes serviços cadastrados no MasterSAF possam ser relacionados com o mesmo código de benefício fiscal da prefeitura do Rio de Janeiro para diferentes períodos\. A data de validade é do tipo “a partir de”\. Deve conter a máscara DD/MM/AAAA\.

__OS3842__

__RN92__

__Regra do campo Serviço MasterSAF da tela Parâmetros – Serviço Msaf x Benefício Fiscal:__

Deverá ser formado por: textbox \+ pastinha amarela\. O usuário poderá preencher esse campo de duas formas: digitando o código do serviço no textbox ou clicando na pastinha amarela\. Quando o cliente optar por clicar na pastinha amarela deve\-se abrir uma tela de seleção com os campos da tabela X2018\_SERVICOS\.

__OS3842__

__RN93__

__Regra do campo Benefício Fiscal da tela Parâmetros – Serviço Msaf x Benefício Fiscal:__

Deverá ser exibido em um listbox, onde as informações serão recuperadas da TFIX122\.

__OS3842__

__RN94__

__Regra do relatório da tela Parâmetros – Serviço Msaf x Benefício Fiscal:__

Deve existir um relatório de conferência que informe os relacionamentos existentes entres os serviços cadastrados no MasterSAF e os códigos de benefício solicitados pela prefeitura do Rio de Janeiro\. 

__OS3842__

__RN95__

__Regra p/ criação da tela de manutenção de declaração de materiais – campos __

Criar a tela de manutenção de declaração de materiais da seguinte maneira:

__\[Alterado MFS3631\]__

Ao abrir a tela deve ser exibida uma janela de seleção, com os principais campos das notas fiscais recebidas\. Devem ser exibidas notas fiscais recebidas \(MOVTO\_E\_S da DWT\_DOCTO\_FISCAL<> ‘9’\), devendo considerar também Notas Fiscais de Mercadoria\. Considerar classificação do documento 1, 2 e 3 \(COD\_CLASS\_DOC\_FIS da tabela SAFX07\) de construção civil \(IND\_TP\_SERVICO da SAFX2018= ‘1’\) e que estejam parametrizadas na tela de Tipo Docto Msaf x Tipo Docto Nota Carioca como tipo = ‘6’ \(Nota Fiscal Remessa de Material e Equipamento\)\.

A tela deve conter duas abas: 

Aba Documento Fiscal: que exibirá as informações da nota fiscal recebida\. Os campos que devem ser exibidos nessa aba são: 

Declarante – Estabelecimento: Deve exibir o campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO referente ao estabelecimento selecionado no manager\.

Declarante – CPF/CNPJ: Deve exibir o campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento selecionado no manager\.

Tipo de Nota Fiscal: Deve exibir o código do tipo de nota fiscal referente ao IDENT\_DOCTO cadastrado na nota selecionada\.

Número Doc\. Fiscal: Deve exibir campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL referente a nota selecionada

Série Doc\. Fiscal: Deve exibir campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL referente a nota selecionada

Data Emissão: Deve exibir campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL referente a nota selecionada

Pessoa Fis/Jur: Deve exibir o código e a razão social referente ao IDENT\_FIS\_JUR cadastrado na nota selecionada\.

Valor Total da Nota: Deve exibir campo VLR\_TOT\_NOTA da tabela DWT\_DOCTO\_FISCAL referente a nota selecionada

Obs: Todos os campos dessa aba devem ser exibidos desabilitados\.

Aba Materiais: que exibirá as informações dos materiais adquiridos para a obra executada\.

Espécie: Deve ser uma list Box e deve exibir as opções: “000 – Nota Fiscal de Materiais \(NFM\)” e “001 – Nota de Remessa de Materiais e Equipamentos \(NRME\)”\. Campo obrigatório\.

Cód\. Obra Origem: Deve ser um text Box\.

Cód\. Obra Destino: Deve ser um text Box\.

Valor de Uso e Consumo: Deve ser um text Box e deve exibir a máscara ,00\. Campo obrigatório\. 

Valor Incorporado: Deve ser um text Box e deve exibir a máscara ,00\. Campo obrigatório\. 

__OS4430__

__MFS3631__

__RN96__

__Regra p/ criação da tela de manutenção de declaração de materiais __

Essa tela deverá ser as seguintes opções:

Aba Documento Fiscal:

__\[Alterado MFS3631\]__

Novo: exibir uma janela de seleção, com os principais campos das notas fiscais recebidas\. Devem ser exibidas notas fiscais recebidas \(MOVTO\_E\_S da DWT\_DOCTO\_FISCAL <> ‘9’\), devendo considerar também Notas Fiscais de Mercadoria\. Considerar classificação do documento 1, 2 e 3 \(COD\_CLASS\_DOC\_FIS da tabela SAFX07\) de construção civil \(IND\_TP\_SERVICO da SAFX2018= ‘1’\) e que estejam parametrizadas na tela de Tipo Docto Msaf x Tipo Docto Nota Carioca como tipo = ‘6’ \(Nota Fiscal Remessa de Material e Equipamento\)\.

Abrir: exibir uma janela de seleção, com os principais campos da tabela da tela de manutenção de declaração de materiais\.

Relatório: exibir um relatório de conferência demonstrando todos os campos da tela de manutenção

Sair: sair da tela

Aba Materiais:

Abrir: exibir uma janela de seleção, com os principais campos da tabela da tela de manutenção de declaração de materiais\.

Excluir: excluir a manutenção da linha corrente\.

Confirmar: salvar a manutenção da linha corrente\.

Relatório: exibir um relatório de conferência demonstrando todos os campos da tela de manutenção

Sair: sair da tela

__OS4430__

__MFS3631__

Obs\.: __CONSIDERAÇÕES SOBRE O REGISTRO TIPO 20__

Atualmente no código consta as regras para a geração do Registro Tipo 20 solicitada pela __MFS\-13467__, porém essa demanda foi cancelada, porque o cliente mudou de município, mas não foi excluído o registro do código\. 

\- Adicinado o select "C\_SERV\_RECEB\_TOMAD\_ISS\_DIGT\_RJ\_SAIDA" na "PKG\_MMAG\_ISSQN" para buscar RPS de saída\. Regra: Considera o campo COD\_TP\_RPS\_NFE nos valores de RPS e RPS\-M como filtro para gerar o registro 20\.

\- Adicionado na "IsIss\_RJ\_mm\_Fproc" a inserção do registro 20\.

Tivemos um ticket __\#56898__ através da __MFS\-98910__ solicitando a retirada do __Registro 20__ 

__Em alinhamento, as informações do Registro 20 será comentado do código e não será mais gerado__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


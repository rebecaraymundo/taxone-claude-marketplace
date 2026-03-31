# MTZ_DES_Florianopolis_Geracao_Meio_Magnetico

- **Fonte:** MTZ_DES_Florianopolis_Geracao_Meio_Magnetico.docx
- **Modificado:** 2026-02-02
- **Tamanho:** 111 KB

---

# DES Florianópolis\- Geração do Meio Magnético

##### DOCUMENTO DE REQUISITO 

###### DR

###### Nome

__Descrição__

OS2755

Este documento tem por objetivo criar o novo módulo “DES Florianópolis” que irá gerar o meio magnético com as informações de documentos fiscais emitidos e recebidos no mês de referência\. Este documento visa atender a versão 2\.00\.0002 da SefinNet\.

OS3192\-N

Este documento tem por objetivo alterar a tela de geração do meio magnético da DES Florianópolis permitindo ao usuário realizar a geração informando a data inicial e data final da apuração\.

OS3285\-D

Essa OS tem o objetivo de permitir que os registros da DES Florianópolis sejam gerados de acordo com as opções de geração selecionadas pelo usuário\.

OS3279

DES Florianópolis – Registro I,J e A referente a GIF\.

Essa OS tem o objetivo de gerar os registros I, J e A para atendimento a GIF\. Cria também o Quadro de Ajustes \(GIF\-AJ\) que permitirá a manutenção do registro A\.

OS3279

DES Florianópolis – Registro I,J e A referente a GIF\.

Complementação da descrição dos registros da GIF\.

OS3279

DES Florianópolis – Registro I e J

Alteração do escopo da OS\. Tratar somente os registros I e J\.

OS3279

DES Florianópolis – Alteração no campo CNAE

Alteração do tamanho CNAE conforme layout 3\.00\.0001\.

CH6412\_2012

<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a><a id="OLE_LINK5"></a>DES Florianópolis – Registro R – Ajuste do campo CNAE\.

<a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>Ajuste da regra de recuperação código CNAE do registro de notas recebidas\.

CH8249\_2014

DES Florianópolis – Registro R – Ajuste do campo CNAE\.

<a id="OLE_LINK9"></a><a id="OLE_LINK10"></a><a id="OLE_LINK11"></a>Ajuste da regra de recuperação código CNAE do registro de notas recebidas quando não houver preenchimento do campo\.

OS3341\-A3

Geração do Meio Magnético para nota fiscais com número de documento com mais de 12 posições\.  

Ajuste para considerar o novo campo NUM\_DOCFIS\_SERV

OS4667

DES Florianópolis – Alteração do campo CST – Registro R

Alteração do local de onde é recuperado as informações do código CST\.

OS4713

DES Florianópolis – Novo Parâmetro Quebra do Arquivo por Data de Emissão

Este documento tem como objetivo incluir o parâmetro na tela de geração um novo parâmetro para que seja possível realizar a quebra do arquivo por data de emissão\.

CH26275\_2015

DES Florianópolis – Alteração da seleção do Registro Tipo T

Este documento tem como objetivo incluir as notas de entrada na seleção do Registro Tipo T\.

MFS\_2071

DW \- MUNICIPAL – DES Florianópolis  – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

CH20110\_2016

DES Florianópolis – Alteração do campo CNAE – Registro J

Este documento tem como objetivo alterar o preenchimento do campo CNAE do Registro J\.

__CH24968\_2016__

DW \- MUNICIPAL – DES Florianópolis – Registro E e F\.

Este documento tem como objetivo alterar a recuperação dos documentos ficais nos registros E e F\.

__CH21046\_2016__

DW \- MUNICIPAL – DES Florianópolis – Registro E, F, R e J\.

Este documento tem como objetivo alterar a recuperação do campo __CNAE\.__

__MFS\-32260__

Atendimento a versão para 1\.03\.0001 do layout SefinNet\.

Volta a versão __1\.03\.0001__, do layout SefinNet\.  Versão anterior era __3\.00\.0001\. __Orientação passada pela prefeitura do município ao cliente\.

__MFS\-61899__

Atualização da Documentação\. 

Atualização da Documentação\. Não foi implementada as regras da MFS\-32260 

__MFS\-92178__

Elisabete Costa – 26/08/2022

Correção do Registro J : Alíquota e valor do ISS \(RN142/RN143\) 

__Demanda foi cancelada, pois a prefeitura mudou de validador\.__

__MFS609796__

Rogério Ohashi

Este documento tem como objetivo alterar a Regra de recuperação das Notas Fiscal para atendimento a GIF\-ST e GIF\-PJ para considerar somente as Notas Fiscais com retenção de ISS\.

__MFS\-829438      __

Graciela Soares

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

 

## REGRAS DE NEGÓCIO

__Atendimento pelo SefinNet – versão 1\.03\.0001__

#### Cód\.

### Descrição

### DR

__RN01__

Regra p/ criação do novo módulo

O novo módulo __“DES Florianópolis”__ deve ficar localizado no grupo “Municipal” abaixo do módulo __“DES Cuiabá”\.__

A descrição funcional do módulo será: __“O objetivo desse módulo é gerar o meio magnético com as informações de documentos fiscais emitidos e recebidos no mês de referência para contribuintes de Florianópolis\.”__ Essa descrição deve ser exibida no resumo do módulo no Manager\.

__OS2755__

__RN02__

__Regra p/ abertura do novo módulo__

Se o estabelecimento selecionado no Manager não pertencer ao estado de Santa Catarina \(UF = “SC”\) e ao município de Florianópolis \(Cod Município IBGE = 5407\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

__“Este estabelecimento não pertence ao município de Florianópolis, Santa Catarina\. Alguns dados não estarão disponíveis\. Deseja continuar?”__

Serão exibidos os botões “Sim” e “Não” \(default\)\. Se o usuário clicar no botão “Sim”, o módulo será aberto normalmente, senão o módulo será fechado\.

__OS2755__

__RN03__

__Regra p/ hierarquia de menus__

Deverão ser criados os seguintes menus e sub\-menus no módulo DES Florianópolis:

- Arquivo
	- Salvar Como
	- Visualizar Relatórios
	- Configura Impressão
	- Sair
- Parâmetros
	- Atividade CNAE
- Obrigações
	- Geração do Meio Magnético
- Janela
- Ajuda

__OS2755__

RN04

A tela de parametrização de atividade CNAE deve exibir os seguintes campos: Atividade CNAE Msaf, Atividade CNAE DES Florianópolis e Validade\. Essa tela deve armazenar os dados cadastrados na tabela PRT\_CNAE\_MSAF \(sugestão do nome da tabela\)\. Essa tela deve ser do tipo multi\-registros\.

__OS2755__

__RN05__

Essa tela deve oferecer as seguintes opções ao usuário: 

Novo: o sistema criará um novo registro\.

Abrir: o sistema exibirá todos os registros já cadastrados\.

Excluir: o sistema excluirá um registro existente\.

Confirmar: o sistema salvará as informações cadastradas\.

Relatório: o sistema chamará o relatório de conferência da tela de parametrização de Atividade CNAE\.

Sair: o sistema fechará a tela\.

__OS2755__

__RN06__

__Regra do campo Atividade CNAE Msaf da tela Parâmetros – Atividade CNAE:__

Deverá recuperar as informações da tabela ATIV\_ECONOMICA\. A recuperação dos documentos deve ser realizado através da pastinha amarela\. 

__OS2755__

__RN07__

__Regra do campo Atividade CNAE DES Florianópolis da tela Parâmetros – Atividade CNAE:__

O campo será do tipo text Box e permitirá a digitação livre para o usuário\. Deve aceitar apenas números e ter o tamanho máximo de 7 posições\.

__OS2755__

__RN08__

__Regra do campo Validade da tela Parâmetros – Atividade CNAE:__

Irá permitir que a mesma Atividade CNAE DES Florianópolis possa ser relacionada com diferentes atividades CNAE cadastradas no MasterSAF para diferentes períodos\. A data de validade é do tipo “a partir de”\. Deve conter a máscara DD/MM/AAAA\. 

__OS2755__

__RN09__

__Regra da tela Parâmetros – Atividade CNAE:__

O sistema não permite que a mesma Atividade CNAE DES Florianópolis seja relacionada com a mesma data de validade\. Nessa situação o sistema deverá exibir a seguinte mensagem de erro: “Não é permitido que a mesma Atividade CNAE DES Florianópolis seja relacionada com a mesma data de validade”\.

A tela deve conter as seguintes funcionalidades: Incluir, Abrir, Alterar, Excluir, Relatório e Sair\.

__OS2755__

__RN10__

__Regra do relatório da tela Parâmetros – Atividade CNAE:__

Deve existir um relatório de conferência que informe os relacionamentos existentes entre as atividades CNAE\.

__OS2755__

__RN11__

__Regra p/ Geração do Meio Magnético__

A tela Obrigações – Geração do Meio Magnético deve ser feita através de framework\. E deve conter as abas: 

Parâmetros: o sistema deve exibir os parâmetros de entrada da geração\.

Processos: o sistema deve exibir os processos já executados para essa geração\.

Log de Processo: o sistema deve exibir o log gerado durante a geração\.

Arquivo: o sistema deve exibir o arquivo que será gravado\. O nome do arquivo deve ser composto da seguinte maneira:

- Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver desmarcado será gerado apenas um arquivo com a nomenclatura do arquivo normal indicado abaixo\.

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.TXT__, onde:

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.TXT

__SefinNet\_DDMMAAAA\.txt__

     Onde:

__           SefinNet__            __Obrigação que está sendo gerada__

__           DDMMAAAA__     __Data inicial da geração__

__           \.txt                      Extensão do arquivo__

      Exemplo: SefinNet\_01012010\.txt \(Ano: 2010, Mês: 01, Dia: 01\)

- Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado deve ser realizado a seguinte verificação:

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverão ser:

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\_MMAAAA\.TXT__, onde:

       __DDMMAAAA__: representa a data inicial da geração\.   

__       MMAAAA:__ mês da competência referente à nota gerada

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_012010\.TXT

__SefinNet\_DDMMAAAA\_MMAAAA\.txt__

     Onde:

__           SefinNet__            __Obrigação que está sendo gerada__

__           DDMMAAAA__     __Data inicial da geração__

__           MMAAAA           Mês da competência referente à nota gerada__

__           \.txt                      Extensão do arquivo__

        Exemplo: SefinNet\_01012010\_122009\.txt \(Ano: 2010, Mês: 01, Dia: 01 – Competência Mês: 12, Ano: 2009\)

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

OBS\.: Devido o validador gerar apenas um arquivo, este novo parâmetro \(Quebrar Arquivos por Data de Emissão\) será válido para todos os tipos de geração\.

__OS2755/__

__OS3192\-N__

__MFS\-829438      __

__RN12__

__Regra p/ Tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

Data Inicial: O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE\.

Data Final: O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE\. 

Gerar Registro P \- Prestadores, Tomadores e Gráficas: check\-box\. Por default, o campo deve ser exibido marcado \(“S”\)\.

Gerar Registro T \- Talonário dos Contribuintes: check\-box\. Por default, o campo deve ser exibido marcado \(“S”\)\. 

Gerar Registro E \- Nota Fiscal Emitida: check\-box\. Por default, o campo deve ser exibido marcado \(“S”\)\.

Gerar Registro F \- Nota Fiscal Emitida p/ Pessoa Física: check\-box\. Por default, o campo deve ser exibido marcado \(“S”\)\.

Gerar Registro R \- Nota Fiscal Recebida: check\-box\. Por default, o campo deve ser exibido marcado \(“S”\)\.

Quebrar Arquivo por Data de Emissão: check\-box\. Por default, o campo deve ser exibido desmarcado \(“N”\)\.

GIF – Guia de Informações Fiscais: quadro contendo os seguintes campos:

- Gerar GIF\-PJ: check\-box\. Por default, o campo deve ser exibido marcado \(“S”\)\.
	- Sem Movimento: check\-box\. Por default, o campo deve ser exibido desmarcado \(“N”\)\.
	- Retificadora: check\-box\. Por default, o campo deve ser exibido desmarcado \(“N”\)\.  

__\[EXCLUÍDA MFS\-61899\]__\(excluído com a versão “__1\.03\.0001__”\)\.

- Gerar GIF\-ST: check\-box\. Por default, o campo deve ser exibido marcado \(“S”\)\.
	- Sem Movimento: check\-box\. Por default, o campo deve ser exibido desmarcado \(“N”\)\.
	- Retificadora: check\-box\. Por default, o campo deve ser exibido desmarcado \(“N”\)\. 

__\[EXCLUÍDA MFS\-61899\]__ \(excluído com a versão “__1\.03\.0001__”\)

- Despesas com Funcionários: campo texto numérico aceitando 16 inteiros e 2 decimais\.
- Número de Funcionários: campo texto numérico aceitando 10 inteiros\.

Estabelecimento: o sistema deve exibir os estabelecimentos pertencentes ao município de Florianópolis, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__OS2755/ OS3192\-N__

__OS3285\-D__

__MFS\_2071__

__MFS\-32260__

__MFS\-61899__

__RN12\.A__

__\[EXCLUÍDA MFS\-61899\]Observação sobre a GIF – Guia de Informações Fiscais: \(versão 1\.03\.0001\):__

A versão 1\.03\.0001 não possui o campo Tipo da Declaração no registro J\. Esse campo só foi incluído na versão 2\.00\.0001\. Logo, como retrocedemos a geração do meio magnético para atender a versão 1\.03\.0001, orientamos para o contribuinte gere a GIF\-PJ separadamente da GIF\-ST\. Não gerar as duas juntas, pois o registro J não terá a identificação de qual declaração ele pertence\.

__MFS\-32260__

__MFS\-61899__

__RN12\.B__

__Regra do campo “Quebrar Arquivo por Data de Emissão” da tela Obrigações – Geração Meio Magnético:__

Deverá ser exibido através de um checkbox\. Deve ser exibido e desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)\.

__OS4713__

__RN13__

__Regra p/ geração do arquivo magnético__

Cada registro especificado abaixo corresponde a uma linha de arquivo texto\. 

Este arquivo deverá ter na primeira linha um registro do tipo H \(Header ou cabeçalho\) e terminar com o registro do tipo L \(Trailler ou fim do arquivo\)\.

Cada linha deve terminar com o caracter de fim de linha ASC13 \+ ASC10\.

__RN14__

__Regra p/ preenchimento dos campos do arquivo magnético__

A forma de preenchimento dos campos no arquivo deve ser realizada da seguinte maneira:

Os campos com asterisco \(\*\) ao lado do tipo, são de preenchimento obrigatório\.

Os campos do tipo TEXTO devem ter o tamanho especificado, preenchidos com brancos à direita\. Se o campo for nulo deve ser preenchido com brancos\.

Os campos do tipo NUMÉRICO devem ser preenchidos com zeros a esquerda, e em casos de campos decimais, não será utilizado vírgula ou ponto, devendo ser informado o valor de acordo com a precisão identificada no conteúdo\.

                Exemplo: valor N16,2 = R$ 1525,34 \-> 0000000000152534\.

Os campos do tipo DATA devem seguir o formato DDMMAAAA, 2 caracteres para dia, 2 para mês e 4 para ano, sem barras, totalizando 8 caracteres\.

                 Exemplo: 17012003

__OS2755__

__RN15__

__Regra p/ Registro Tipo H__

Sempre deve ser o primeiro registro do arquivo, apenas deve existir um registro deste tipo por arquivo\.

__OS2755__

__RN16__

__Registro H – Tipo do Registro: __Preencher com o texto fixo “H”\.

Formato: Texto

Campo: Obrigatório

Tamanho: 1

__OS2755__

__RN17__

__Registro H – Versão SefinNet: __Preencher com o texto fixo __“3\.00\.0001”__ 

__\[EXCLUÍDA MFS\-61899\]__ “__1\.03\.0001__”\.

Formato: Texto

Campo: Obrigatório

Tamanho: 9

__OS2755__

__OS3279__

__MFS\-32260__

__MFS\-61899__

__RN18__

__Regra p/ Registro Tipo C__

Deve haver um registro deste tipo por contribuinte e devem vir logo após o registro do tipo Header\.

Deve apresentar as informações do estabelecimento escolhido na tela de parâmetros da geração do meio magnético\.

__OS2755__

__RN19__

__Registro C – Tipo do Registro: __Preencher com o texto fixo “C”\.

Formato: Texto

Campo: Obrigatório

Tamanho: 1

__OS2755__

__RN20__

__Registro C – CMC:__ Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\.

Se contribuinte não tiver CMC e precisar enviar declarações como substituto tributário o CMC deve ser informado com zeros\.

Formato: N

Campo: Obrigatório

Tamanho: 7

__OS2755__

__RN21__

__Registro C – CNPJ: __Preencher com o campo CGC da tabela ESTABELECIMENTO\.

Preencher apenas se CMC igual a zeros\.

Formato: Texto

Campo: Obrigatório

Tamanho: 14

__OS2755__

__RN22__

__Registro C – Razão: __Preencher com o campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO\.

Preencher apenas se CMC igual a zeros\.

Formato: Texto

Campo: Obrigatório

Tamanho: 80

__OS2755__

__RN23__

__Registro C – Nome: __Preencher com o campo NOME\_FANTASIA da tabela ESTABELECIMENTO\.

Preencher apenas se CMC igual a zeros\.

Formato: Texto

Campo: Obrigatório

Tamanho: 50

__OS2755__

__RN24__

__Registro C – Inscrição Estadual: __Preencher com o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL referente ao estabelecimento escolhido\.

Preencher apenas se CMC igual a zeros e se o estabelecimento possuir inscrição estadual\.

Formato: Texto

Campo: Não Obrigatório

Tamanho: 20

__OS2755__

__RN25__

__Registro C – Junta Comercial: __Preencher com brancos\.

__OS2755__

__RN26__

__Registro C – Endereço: __Preencher com os campos TP\_LOGRADOURO e ENDERECO concatenados da tabela ESTABELECIMENTO\.

Preencher apenas se CMC igual a zeros\.

Formato: Texto

Campo: Não Obrigatório

Tamanho: 80

__OS2755__

__RN27__

__Registro C – Número: __Preencher com o campo NUM\_ENDERECO da tabela ESTABELECIMENTO\.

Preencher apenas se CMC igual a zeros\.

Formato: Texto

Campo: Não Obrigatório

Tamanho: 10

__OS2755__

__RN28__

__Registro C – Complemento: __Preencher com o campo COMPL\_ENDERECO da tabela ESTABELECIMENTO\.

Preencher apenas se CMC igual a zeros\.

Formato: Texto

Campo: Não Obrigatório

Tamanho: 30

__OS2755__

__RN29__

__Registro C – Bairro: __Preencher com o campo BAIRRO da tabela ESTABELECIMENTO\.

Preencher apenas se CMC igual a zeros\.

Formato: Texto

Campo: Não Obrigatório

Tamanho: 50

__OS2755__

__RN30__

__Registro C – Cidade: __Preencher com o campo CIDADE da tabela ESTABELECIMENTO\.

Preencher apenas se CMC igual a zeros\.

Formato: Texto

Campo: Obrigatório

Tamanho: 50

__OS2755__

__RN31__

__Registro C – UF: __Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao campo IDENT\_ESTADO cadastrado para o estabelecimento escolhido\.

Preencher apenas se CMC igual a zeros\.

Formato: Texto

Campo: Obrigatório

Tamanho: 2

__OS2755__

__RN32__

__Registro C – CEP Nome: __Preencher com o campo CEP da tabela ESTABELECIMENTO\.

Preencher apenas se CMC igual a zeros\.

Formato: Texto

Campo: Não Obrigatório

Tamanho: 8

__OS2755__

__RN33__

__Registro C – DDD: __Preencher com os dois últimos dígitos do campo DDD da tabela ESTABELECIMENTO\.

Preencher apenas se CMC igual a zeros\.

Formato: Texto

Campo: Não Obrigatório

Tamanho: 2

__OS2755__

__RN34__

__Registro C – Fone: __Preencher com o campo TELEFONE da tabela ESTABELECIMENTO\.

Preencher apenas se CMC igual a zeros\.

Formato: Texto

Campo: Não Obrigatório

Tamanho: 8

__OS2755__

__RN35__

__Registro C – Fax: __Preencher com o campo FAX da tabela ESTABELECIMENTO\.

Preencher apenas se CMC igual a zeros\.

Formato: Texto

Campo: Não Obrigatório

Tamanho: 8

__OS2755__

__RN36__

__Registro C – Email: __Preencher com o campo EMAIL da tabela ESTABELECIMENTO\.

Preencher apenas se CMC igual a zeros\.

Formato: Texto

Campo: Não Obrigatório

Tamanho: 80

__OS2755__

__RN37__

__Regra p/ Registro Tipo P __

O registro P será gerado se o campo “Gerar Registro P \- Prestadores, Tomadores e Gráficas” estiver marcado, na tela de geração\.

Este registro serve somente para Prestadores, Tomadores\.

Deve apresentar as informações da pessoa fis/jur cadastrada na nota fiscal\.

O registro deve apresentar apenas os prestadores e tomadores referentes as notas fiscais apresentadas no arquivo\. 

__Obs:__ __Para pessoa fis/jur de fora de Florianópolis todas as informações são obrigatórias__\.

__OS2755__

__OS3285\-D__

__RN38__

__Registro P – Tipo do Registro: __Preencher com o texto fixo __“P”\.__

Formato: Texto

Campo: Obrigatório

Tamanho: 1

__OS2755__

__RN39__

__Registro P – CMC: __Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR\.

__\[EXCLUÍDA MFS\-61899\]__ Campo excluído com a versão “__1\.03\.0001__”\.

Formato: N

Campo: Não Obrigatório

Tamanho: 7

__OS2755__

__MFS\-32260__

__MFS\-61899__

__RN40__

__Registro P – CNPJ: __Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR\.

Formato: Texto

Campo: Obrigatório

Tamanho: 14

__OS2755__

__RN41__

__Registro P – Razão: __Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\.

Formato: Texto

Campo: Obrigatório

Tamanho: 80

__OS2755__

__RN42__

__Registro P – Nome: __Preencher com o campo NOME\_FANTASIA da tabela X04\_PESSOA\_FIS\_JUR\.

Formato: Texto

Campo: Obrigatório

Tamanho: 50

__OS2755__

__RN43__

__Registro P – Endereço: __Preencher com os campos TP\_LOGRADOURO e ENDERECO concatenados da tabela X04\_PESSOA\_FIS\_JUR\.

Formato: Texto

Campo: Não Obrigatório

Tamanho: 80

__OS2755__

__RN44__

__Registro P – Número: __Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

Formato: Texto

Campo: Não Obrigatório

Tamanho: 10

__OS2755__

__RN45__

__Registro P – Complemento: __Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR\.

Formato: Texto

Campo: Não Obrigatório

Tamanho: 30

__OS2755__

__RN46__

__Registro P – Bairro: __Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR\.

Formato: Texto

Campo: Não Obrigatório

Tamanho: 50

__OS2755__

__RN47__

__Registro P – Cep: __Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR\.

Formato: N

Campo: Não Obrigatório

Tamanho: 8

__OS2755__

__RN48__

__Registro P – Cidade: __Preencher com o campo CIDADE da tabela X04\_PESSOA\_FIS\_JUR\.

Formato: Texto

Campo: Obrigatório

Tamanho: 50

__OS2755__

__RN49__

__Registro P – UF: __Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao campo IDENT\_ESTADO cadastrado para a pessoa fis/jur escolhida\.

Formato: N

Campo: Obrigatório

Tamanho: 2

__OS2755__

__RN50__

__Registro P – DDD: __Preencher com os dois últimos dígitos do campo DDD da tabela X04\_PESSOA\_FIS\_JUR\.

Formato: N

Campo: Não Obrigatório

Tamanho: 2

__OS2755__

__RN51__

__Registro P – Fone: __Preencher com o campo TELEFONE da tabela X04\_PESSOA\_FIS\_JUR\.

Formato: Texto

Campo: Não Obrigatório

Tamanho: 8

__OS2755__

__RN52__

__Registro P – Gráfica: __Preencher com:

1, se o IDENT\_FIS\_JUR da tabela X04\_PESSOA\_FIS\_JUR estiver sendo utilizado para algum registro da tabela X68\_IMPRESSAO\_AIDF\.

0, quando o IDENT\_FIS\_JUR da tabela X04\_PESSOA\_FIS\_JUR não estiver sendo utilizado para algum registro da tabela X68\_IMPRESSAO\_AIDF\.

Formato: N

Campo: Não Obrigatório

Tamanho: 1

__OS2755__

__RN53\.a__

__Regra p/ Registro Tipo T \(Talonário\)__

O registro T será gerado se o campo “Gerar Registro T \- Talonário dos Contribuintes” estiver marcado, na tela de geração\.

Este registro deve conter todas as notas com as seguintes características:

- Nota de Entrada e Saída
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data Fiscal dentro do periodo de referência
- AIDF cadastrado na SAFX68 referenciada com Nº da AIDF na SAFX07

__Atenção: Esse registro só será gerado quando tiver os registros E, F ou R\.__

__OS3285\-D__

__CH26275\_2015__

__RN53__

__Registro T – Tipo do Registro: __Preencher com o texto fixo __“T”__

Formato: Texto

Campo: Obrigatório

Tamanho: 1

__OS2755__

__RN54__

__Registro T – CMC do Contribuinte: __Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\.

Formato: N

Campo: Não Obrigatório

Tamanho: 7

__OS2755__

__RN55__

__Registro T – CNPJ do Contribuinte: __Preencher com o campo CGC da tabela ESTABELECIMENTO\.

__\[EXCLUÍDA MFS\-61899\]__ Campo excluído com a versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 14

__OS2755__

__MFS\-32260__

__MFS\-61899__

__RN56__

__Registro T – Branco / Série: __Preencher com o campo SERIE\_DOC da tabela X68\_IMPRESSAO\_AIDF\.

Formato: Texto

Campo: Obrigatório

Tamanho: 10

__OS2755__

__RN56A__

__\[ EXCLUÍDA MFS\-61899\] Registro T – Município da Gráfica: __Indica se a Gráfica é ou não de Florianópolis\.

Recuperar o Código do Estado e o Código do Munícípio do Cadastro da Pessoa Física Jurídica \(tabela X04\_PESSOA\_FIS\_JUR\), referente ao campo IDENT\_FIS\_JUR cadastrado na tabela X68\_IMPRESSAO\_AIDF\.

__Se __Cod\_Estado = “SC” e Cod\_Município = “5407”, Então: 

     Preencher com “1” \- Gráfica for de Florianópolis

__Senão__

     Preencher com “0” \- Gráfica de outros municípios\.

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

__RN57__

__Registro T – CNPJ/CMC Gráfica: __Preencher o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente ao campo IDENT\_FIS\_JUR cadastrado na tabela X68\_IMPRESSAO\_AIDF\.

Formato: Texto

Campo: Obrigatório

Tamanho: 14

__OS2755__

__RN58__

__Registro T – AIDF: __Preencher com o campo NRO\_AIDF da tabela X68\_IMPRESSAO\_AIDF\.

Formato: N

Campo: Obrigatório

Tamanho: 40

__OS2755__

__RN58A__

__\[EXCLUÍDA MFS\-61899\] Registro T – Branco: __Preencher com 20 espaços em branco\.

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

__RN58B__

__\[EXCLUÍDA MFS\-61899\] Registro T – Branco: __Preencher com 8 espaços em branco\.

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

__RN58C__

__\[EXCLUÍDA MFS\-61899\] Registro T – Branco: __Preencher com 8 espaços em branco\.

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

__RN59__

__Registro T – Número NF Inicial: __Preencher com o campo NRO\_INICIAL da tabela X68\_IMPRESSAO\_AIDF\.

__\[EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 15 para 10 pela versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 15

__OS2755__

__MFS\-32260__

__MFS\-61899__

__RN60__

__Registro T – Número NF Final: __Preencher com o campo NRO\_FINAL da tabela X68\_IMPRESSAO\_AIDF\.

__\[EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 15 para 10 pela versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 15

__OS2755__

__MFS\-32260__

__MFS\-61899__

__RN61__

__Regra p/ Registro Tipo E__

O registro E será gerado se o campo “Gerar Registro E \- Nota Fiscal Emitida” estiver marcado, na tela de geração\.

Este registro deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data da Emissão do RPS da Nota Fiscal Eletrônica dentro do período de referência e se não estiver preenchido considerar pela Data Fiscal\.

__OS2755__

__OS3279__

__OS3285\-D__

__CH24968\_2016__

__RN62__

__Registro E – Tipo do Registro: __Preencher com o texto fixo __“E”\.__

Formato: Texto

Campo: Obrigatório

Tamanho: 1

__OS2755__

__RN63__

__Registro E – CMC do Contribuinte: __Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\.

Formato: N

Campo: Obrigatório

Tamanho: 7

__OS2755__

__RN64__

__Registro E – CNPJ do Contribuinte: __Preencher com o campo CGC da tabela ESTABELECIMENTO\.

__\[EXCLUÍDA MFS\-61899\]__  Campo excluído com a versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 14

__OS2755__

__MFS\-32260__

__MFS\-61899__

__RN65__

__Registro E – Série / Branco: __Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Formato: Texto

Campo: Obrigatório

Tamanho: 10

__OS2755__

__RN66__

__Registro E – Numero NF inicial do talonário: __Preencher com o campo NRO\_INICIAL da tabela X68\_IMPRESSAO\_AIDF quando:

- COD\_EMPRESA da tabela X68\_IMPRESSAO\_AIDF     = COD\_EMPRESA da tabela DWT\_DOCTO\_FISCAL 
- COD\_ESTAB da tabela X68\_IMPRESSAO\_AIDF          = COD\_ESTAB da tabela DWT\_DOCTO\_FISCAL
- NRO\_AIDF da tabela X68\_IMPRESSAO\_AIDF               = NRO\_AIDF\_NF da tabela DWT\_DOCTO\_FISCAL
- DATA\_ENTREGA da tabela X68\_IMPRESSAO\_AIDF    = DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL__ __
- SERIE\_DOC da tabela X68\_IMPRESSAO\_AIDF            = SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL
- SUB\_SERIE\_DOC da tabela X68\_IMPRESSAO\_AIDF   = SUB\_SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL

__\[EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 15 para 10 pela versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 15

__OS2755__

__MFS\-32260__

__MFS\-61899__

__RN67__

__Registro E – Data da Nota Fiscal: __Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Formato: Data

Campo: Obrigatório

Tamanho: 8

__OS2755__

__RN68__

__Registro E – Numero da Nota Fiscal: __

__Tela\-A__ ç__  Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

  __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ __ __  

  __E__

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __ 

Então, Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL__

Se não,

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__\[EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 15 para 10 pela versão “1\.03\.0001”\.

Formato: N

Campo: Obrigatório

Tamanho: 15

__OS2755__

__OS3341\-A3__

__MFS\-32260__

__MFS\-61899__

__RN68A__

__\[EXCLUÍDA MFS\-61899\] Registro E – Município do Tomador do Serviço: __Indica se o tomador é ou não de Florianópolis\.

Recuperar o Código do Estado e o Código do Munícípio do Cadastro da Pessoa Física Jurídica \(tabela X04\_PESSOA\_FIS\_JUR\), referente ao campo IDENT\_FIS\_JUR cadastrado na tabela DWT\_DOCTO\_FISCAL\.

__Se __Cod\_Estado = “SC” e Cod\_Município = “5407”, Então: 

     Preencher com “1” – Tomador de Florianópolis

__Senão__

     Preencher com “0” \- Tomador de outros municípios\.

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

__RN69__

__Registro E – CMC do Tomador do Serviço: __Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR\.

\[__EXCLUÍDA MFS\-61899\]__ Campo excluído com a versão “__1\.03\.0001__”\.

Formato: N

Campo: Não Obrigatório

Tamanho: 7

__OS2755__

__MFS\-32260__

__MFS\-61899__

__RN70__

__Registro E – CNPJ do Tomador do Serviço: __Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR\.

Formato: Texto

Campo: Obrigatório

Tamanho: 14

__OS2755__

__RN71__

__Registro E – CNAE:__ Preencher com o conteúdo do campo “Atividade CNAE DES Florianópolis” da tela Parâmetros – Atividade CNAE referente ao campo__ __COD\_ATIVIDADE da tabela CÓDIGO DE SERVIÇOS \(SAFX2018\)\. Se o campo não estiver preenchido, preencher com brancos\.

Preencher com o conteúdo do campo COD\_ATIVIDADE da tabela CÓDIGO DE SERVIÇOS \(SAFX2018\)\.

\[__EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 11 para 7 pela versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 11

__OS2755__

__CH21046\_2016__

__MFS\-32260__

__MFS\-61899__

__RN71A__

__\[EXCLUÍDA MFS\-61899\] Registro E – Branco: __Preencher com 2 espaços em branco\.

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

__RN72__

__Registro E – Tipo: __Preencher com:

E, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> ‘S’

C, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = ‘S’

X, quando o campo IND\_NOTA\_SERVICO da tabela DWT\_DOCTO\_FISCAL = ‘E’

Formato: Texto

Campo: Obrigatório

Tamanho: 1

__OS2755__

__RN73__

__Registro E – Valor Contábil: __Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\.

Formato: N

Campo: Obrigatório

Tamanho: 18

__OS2755__

__RN74__

__Registro E – Base de Cálculo: __Preencher com o somatório do campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV\.

Formato: N

Campo: Obrigatório

Tamanho: 18

__OS2755__

__RN75__

__Registro E – Obs: __Quando o campo Tipo <> “E”, preencher com o campo DESCRICAO da tabela OBS\_MOTIVO\_NOTA referente ao campo COD\_MOTIVO cadastrado na nota\.

Formato: Texto

Campo: Obrigatório

Tamanho: 50

__OS2755__

__RN76__

__Registro E – CFPS: __Preencher com o campo COD\_CFPS da tabela DWT\_DOCTO\_FISCAL\.

Formato: N

Campo: Obrigatório

Tamanho: 4

__OS2755__

__RN77__

__Registro E – CST: __

Preencher com o campo COD\_SITUACAO\_A da tabela Y2025\_SIT\_TRB\_UF\_A referente ao campo IDENT\_SITUACAO\_A concatenado com o COD\_SITUACAO\_B da tabela Y2026\_SIT\_TRB\_UF\_B referente ao campo IDENT\_SITUACAO\_B\.

__ALTERADA \[OS4667\]__

Preencher com a informação do campo “Código Situação Tributária ISS” criado na tabela SAFX09, referente ao código da Situação Tributária do ISS\.

OBS\.: Caso não seja informado valor para o campo CST, deverá preencher com “00”\. Devido à falta de contato com a Prefeitura, vamos manter a regra que já é utilizada desde a criação do validador\. 

A lista de CST’s disponibilizada pela prefeitura é carregada na TACES 88 \- Código Situação Tributária ISS \(Validador DES\-Florianópolis\) – tabela DWT\_COD\_SIT\_TRIB\_ISS\.

\[__EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 3 para 2 pela versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 3

__OS2755__

__/__

__OS4667__

__MFS\-32260__

__MFS\-61899__

__RN78__

__Registro E – Alíquota: __Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

\[__EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 18 para 7 pela versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 18

__OS2755__

__MFS\-32260__

__MFS\-61899__

__RN79__

__Registro E – Valor do ISS: __Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

Formato: N

Campo: Obrigatório

Tamanho: 18

__OS2755__

__RN80__

__Regra p/ Registro Tipo F__

O registro F será gerado se o campo “Gerar Registro F \- Nota Fiscal Emitida p/ Pessoa Física” estiver marcado, na tela de geração\.

Este registro deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Pessoa Fis/Jur cadastrada na nota deve ser uma pessoa física \(campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR com 11 posições\)
- Data da Emissão do RPS da Nota Fiscal Eletrônica dentro do período de referência e se não estiver preenchido considerar pela Data Fiscal\.

As notas fiscais deverão ser agrupadas por data de emissão\. As notas fiscais serão por faixa e o valor será a soma dessa faixa\.

__OS2755__

__OS3279__

__OS3285\-D__

__CH24968\_2016__

__RN81__

__Registro F – Tipo do Registro: __Preencher com o texto fixo __“F”\.__

Formato: Texto

Campo: Obrigatório

Tamanho: 1

__OS2755__

__RN82__

__Registro F – CMC do Contribuinte Prestador: __Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\.

Formato: N

Campo: Obrigatório

Tamanho: 7

__OS2755__

__RN83__

__Registro F – CNPJ do Contribuinte Prestador: __Preencher com o campo CGC da tabela ESTABELECIMENTO\.

__\[EXCLUÍDA MFS\-61899\]__ Campo excluído com a versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 14

__OS2755__

__MFS\-32260__

__MFS\-61899__

__RN84__

__Registro F – Série / Branco: __Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL

Formato: Texto

Campo: Obrigatório

Tamanho: 10

__OS2755__

__RN85__

__Registro F – Numero NF inicial do talonário: __Preencher com o campo NRO\_INICIAL da tabela X68\_IMPRESSAO\_AIDF quando:

- COD\_EMPRESA da tabela X68\_IMPRESSAO\_AIDF     = COD\_EMPRESA da tabela DWT\_DOCTO\_FISCAL 
- COD\_ESTAB da tabela X68\_IMPRESSAO\_AIDF          = COD\_ESTAB da tabela DWT\_DOCTO\_FISCAL
- NRO\_AIDF da tabela X68\_IMPRESSAO\_AIDF               = NRO\_AIDF\_NF da tabela DWT\_DOCTO\_FISCAL
- DATA\_ENTREGA da tabela X68\_IMPRESSAO\_AIDF    >= DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL__ __
- SERIE\_DOC da tabela X68\_IMPRESSAO\_AIDF            = SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL

      \-      SUB\_SERIE\_DOC da tabela X68\_IMPRESSAO\_AIDF   = SUB\_SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL

__\[EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 15 para 10 pela versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 15

__OS2755__

__MFS\-32260__

__MFS\-61899__

__RN86__

__Registro F – Data da Nota Fiscal: __Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Formato: Data

Campo: Obrigatório

Tamanho: 8

__OS2755__

__RN87__

__Registro F – Numero da Nota Fiscal Inicial: __

__Tela\-A__ ç__  Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

  __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ __ __  

  __E__

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __ 

Então, Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL__

Se não,

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL da primeira nota da faixa\.

__\[EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 15 para 10 pela versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 15

__OS2755__

__OS3341\-A3__

__MFS\-32260__

__MFS\-61899__

__RN88__

__Registro F – Numero da Nota Fiscal Final: __

__Tela\-A__ ç__  Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

  __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ __ __  

  __E__

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __ 

Então, Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL__

Se não,

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL da última nota da faixa\.

__\[EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 15 para 10 pela versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 15

__OS2755__

__OS3341\-A3__

__MFS\-32260__

__MFS\-61899__

__RN89__

__Registro F – CNAE:__ Preencher com o conteúdo do campo “Atividade CNAE DES Florianópolis” da tela Parâmetros – Atividade CNAE referente ao campo__ __COD\_ATIVIDADE da tabela CÓDIGO DE SERVIÇOS \(SAFX2018\)\. Se o campo não estiver preenchido, preencher com brancos\.

Preencher com o conteúdo do campo COD\_ATIVIDADE da tabela CÓDIGO DE SERVIÇOS \(SAFX2018\)\.

__\[EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 11 para 7 pela versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 11

__OS2755__

__CH21046\_2016__

__MFS\-32260__

__MFS\-61899__

__RN89A__

__Registro F – Branco: __Preencher com 2 espaços em branco\.

__\[EXCLUÍDA MFS\-61899\] __Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

__RN90__

__Registro F – Tipo: __Preencher com:

__E__, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> ‘S’

__C__, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = ‘S’

__X__, quando o campo IND\_NOTA\_SERVICO da tabela DWT\_DOCTO\_FISCAL = ‘E’

Formato: Texto

Campo: Obrigatório

Tamanho: 1

__OS2755__

__RN91__

__Registro F – Valor Contábil: __Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\.

Formato: N

Campo: Obrigatório

Tamanho: 18

__OS2755__

__RN92__

__Registro F – Base de Cálculo: __Preencher com o somatório do campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV\.

Formato: N

Campo: Obrigatório

Tamanho: 18

__OS2755__

__RN93__

__Registro F – Obs: __Quando o campo Tipo <> “E”, preencher com o campo DESCRICAO da tabela OBS\_MOTIVO\_NOTA referente ao campo COD\_MOTIVO cadastrado na nota\.

Formato: Texto

Campo: Obrigatório

Tamanho: 50

__OS2755__

__RN94__

__Registro F – CFPS: __Preencher com o campo COD\_CFPS da tabela DWT\_DOCTO\_FISCAL\.

Formato: N

Campo: Obrigatório

Tamanho: 4

__OS2755__

__RN95__

__Registro F – CST: __

Preencher com o campo COD\_SITUACAO\_A da tabela Y2025\_SIT\_TRB\_UF\_A referente ao campo IDENT\_SITUACAO\_A concatenado com o COD\_SITUACAO\_B da tabela Y2026\_SIT\_TRB\_UF\_B referente ao campo IDENT\_SITUACAO\_B\.

__ALTERADA \[OS4667\]__

Preencher com a informação do campo “Código Situação Tributária ISS” criado na tabela SAFX09, referente ao código da Situação Tributária do ISS\.

OBS\.: Caso não seja informado valor para o campo CST, deverá preencher com  “000”\. Devido à falta de contato com a Prefeitura, vamos manter a regra que já é utilizada desde a criação do validador\. __ __

__\[EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 3 para 2 pela versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 3

__OS2755__

__/__

__OS4667__

__MFS\-32260__

__MFS\-61899__

__RN96__

__Registro F – Alíquota: __Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

__\[EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 18 para 7 pela versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 18

__OS2755__

__MFS\-32260__

__MFS\-61899__

__RN97__

__Registro F – Valor do ISS: __Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

Formato: N

Campo: Obrigatório

Tamanho: 18

__OS2755__

__RN98__

__Regra p/ Registro Tipo R__

O registro R será gerado se o campo “Gerar Registro R \- Nota Fiscal Recebida” estiver marcado, na tela de geração\.

Este registro deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data Fiscal dentro do periodo de referencia \(Atualmente é considerado a data fiscal e não data de emissão\.

__OS2755__

__OS3279__

__OS3285\-D__

__RN99__

__Registro R – Tipo do Registro: __Preencher com o texto fixo “R”\.

Formato: Texto

Campo: Obrigatório

Tamanho: 1

__OS2755__

__RN100__

__Registro R – CMC do Contribuinte: __Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO\.

Formato: N

Campo: Obrigatório

Tamanho: 14

__OS2755__

__RN101__

__Registro R – CNPJ do Contribuinte: __Preencher com o campo CGC da tabela ESTABELECIMENTO\.

__\[EXCLUÍDA MFS\-61899\]__ Campo excluído com a versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 14

__OS2755__

__MFS\-32260__

__MFS\-61899__

__RN102__

__Registro R – CMC do Prestador: __Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR\.

__\[EXCLUÍDA MFS\-61899\]__ Campo excluído com a versão “__1\.03\.0001__”\.

Formato: N

Campo: Não Obrigatório

Tamanho: 7

__OS2755__

__MFS\-32260__

__MFS\-61899__

__RN102A__

__\[EXCLUÍDA MFS\-61899\]__ __Registro R – Município do Prestador: __Indica se o prestador é ou não de Florianópolis\.

Recuperar o Código do Estado e o Código do Munícípio do Cadastro da Pessoa Física Jurídica \(tabela X04\_PESSOA\_FIS\_JUR\), referente ao campo IDENT\_FIS\_JUR cadastrado na tabela DWT\_DOCTO\_FISCAL\.

__Se __Cod\_Estado = “SC” e Cod\_Município = “5407”, Então: 

     Preencher com “1” – prestador de Florianópolis

__Senão__

     Preencher com “0” \- prestador de outros municípios\.

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

__RN103__

__Registro R – CMC / CNPJ do Prestador: __Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR\.

Formato: Texto

Campo: Obrigatório

Tamanho: 14

__OS2755__

__RN104__

__Registro R – Numero da Nota Fiscal: __

__Tela\-A__ ç__  Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

  __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ __ __  

  __E__

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __ 

Então, Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL__

Se não,

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 15 para 10 pela versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 15

__OS2755__

__OS3341\-A3__

__MFS\-32260__

__MFS\-61899__

__RN105__

__Registro R – Série: __Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL

__\[EXCLUÍDA MFS\-61899\]__ Campo excluído com a versão “__1\.03\.0001__”\.

Formato: Texto

Campo: Obrigatório

Tamanho: 10

__OS2755__

__MFS\-32260__

__MFS\-61899__

__RN105A__

__\[EXCLUÍDA MFS\-61899\]__ __Registro R – Branco: __Preencher com 10 espaços em branco\.

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

__RN106__

__Registro R – CNAE: __Preencher com o conteúdo do campo “Atividade CNAE DES Florianópolis” da tela Parâmetros – Atividade CNAE associado ao campo__ __COD\_ATIVIDADE da tabela de CÓDIGO DE SERVIÇOS \(SAFX2018\)\. Se o campo não estiver preenchido, preencher com brancos\. 

Preencher com o conteúdo do campo COD\_ATIVIDADE da tabela CÓDIGO DE SERVIÇOS \(SAFX2018\)\.

__\[EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 11 para 7 pela versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 11

__OS2755__

__CH6412\_2012__

__CH8249\_2014__

__CH21046\_2016__

__MFS\-32260__

__MFS\-61899__

__RN106A__

__\[EXCLUÍDA MFS\-61899\]__ __Registro R – Branco: __Preencher com 2 espaços em branco\.

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

__RN107__

__Registro R – Data Emissão da Nota Fiscal: __Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

Formato: Data

Campo: Obrigatório

Tamanho: 8

__OS2755__

__RN108__

__Registro R – Valor Contábil: __Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\.

Formato: N

Campo: Obrigatório

Tamanho: 18

__OS2755__

__RN109__

__Registro R – Base de Cálculo: __Preencher com o somatório do campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV\.

Formato: N

Campo: Obrigatório

Tamanho: 18

__OS2755__

__RN110__

__Registro R – Obs: __Preencher com 50 espaços em brancos\.

__OS2755__

__RN110A__

__\[EXCLUÍDA MFS\-61899\]__ __Registro R – CNPJ Contribuinte Tomador: __

__Se __o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO não estiver preenchido, então:

     Preencher o campo com o CGC da tabela ESTABELECIMENTO\.

__Senão__

     Preencher o campo com 14 zeros\.

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

__RN111__

__Registro R – CFPS: __Preencher com o campo COD\_CFPS da tabela DWT\_DOCTO\_FISCAL\.

Formato: N

Campo: Obrigatório

Tamanho: 4

__OS2755__

__RN112__

__Registro R – CST:__ 

Preencher com o campo COD\_SITUACAO\_A da tabela Y2025\_SIT\_TRB\_UF\_A referente ao campo IDENT\_SITUACAO\_A concatenado com o COD\_SITUACAO\_B da tabela Y2026\_SIT\_TRB\_UF\_B referente ao campo IDENT\_SITUACAO\_B\.

__ALTERADA \[OS4667\]__

Preencher com a informação do campo “Código Situação Tributária ISS” criado na tabela SAFX09, referente ao código da Situação Tributária do ISS\.

OBS\.: Caso não seja informado valor para o campo CST, deverá preencher com “00”\. Devido à falta de contato com a Prefeitura, vamos manter a regra que já é utilizada desde a criação do validador\. __  __

__\[EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 3 para 2 pela versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 3

__OS2755__

__/__

__OS4667__

__MFS\-32260__

__MFS\-61899__

__RN113__

__Registro R – Alíquota:__ Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.__ __

__\[EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 18 para 7 pela versão “__1\.03\.0001__”\.

Formato: N

Campo: Obrigatório

Tamanho: 18

__OS2755__

__MFS\-32260__

__MFS\-61899__

__RN114__

__Registro R – Valor do ISS: __Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

Formato: N

Campo: Obrigatório

Tamanho: 18

__OS2755__

__RN115__

__Registro G – GIF\-PJ e GIF\-PF__

Este registro __não__ será gerado, pois segundo orientações do layout da versão “__1\.03\.0001__”, ele deve ser utilizado apenas para as apurações de janeiro a junho de 2004\.

__MFS\-32260__

__RN116__

__Registro S – GIF – Guia de Informações Fiscais__

Este registro __não__ será gerado, pois segundo orientações do layout da versão “__1\.03\.0001__”, ele é para ser gerado para contribuintes Pessoa Jurídica de Sociedade Simples e Pessoa Física\. Nossos clientes não se enquadram nessas categorias\.

__MFS\-32260__

__RN117__

__Regra p/ Registro Tipo L__

Sempre deve ser o último registro do arquivo, apenas deve existir um registro deste tipo por arquivo\.

__OS2755__

__RN118__ 

__Registro L – Tipo do Registro: __Preencher com o texto fixo “L”\.

Formato: Texto

Campo: Obrigatório

Tamanho: 1

__OS2755__

__RN119__

__Registro L – Total de Linhas: __Preencher com o total de linhas do arquivo, considerando todas as linhas inclusive o Header e o Trailler\.

Formato: N

Campo: Obrigatório

Tamanho: 10

__OS2755__

RN120

__Regras para a geração do Registro I – Guia de Informações Fiscais__

O registro I será gerado se pelo menos um dos campos “Gerar GIF\-PJ” ou “Gerar GIF\-ST” estiver marcado, na tela de geração\.

Registro principal para atendimento a GIF\-PJ e GIF\-ST\. 

GIF\-PJ: *notas fiscais de saída, com pessoa jurídica de prestação de serviços do município de Florianópolis\.*

GIF\-ST: *para notas fiscais de entrada, com contribuintes tomadores de serviços de prestadores do município de Florianópolis ou de fora do município\.*

No arquivo deve ser gerado 1 registro “I” para cada tipo de declaração \(ST ou PJ\)\.

Se campos “Gerar GIF\-PJ” estiver marcado então:

     Gerar no arquivo um registro “I” para a GIF\-PJ\.

Se campos “Gerar GIF\-ST” estiver marcado então:

     Gerar no arquivo um registro “I” para a GIF\-ST\.

__OS3279__

RN121

__Registro I – Tipo do Registro:__ Preencher com o texto fixo “I”\.

Formato: Texto

Campo: Obrigatório

Tamanho: 1

__OS3279__

RN122

__Registro I – CMC__: Preencher com o CMC do contribuinte\.

Campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO

Tipo: Numérico

Campo: obrigatório

Tamanho: 7

Chave Primária

__\[EXCLUÍDA MFS\-61899\]__ Campo excluído com a versão “__1\.03\.0001__”\.

__OS3279__

__MFS\-32260__

__MFS\-61899__

RN123

__Registro I – CNPJ:__ Preencher com o CNPJ do contribuinte\.

Campo CGC da tabela ESTABELECIMENTO\.

Tipo: Texto

Campo: Obrigatório

Tamanho: 14

Chave Primária

__OS3279__

RN123A

__\[EXCLUÍDA MSF61899\] Registro I – Identificação:__ Preencher fixo com “01”\.

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

RN124

__Registro I – Mês:__ Preencher com o mês da apuração\.

Tipo: Numérico

Campo: Obrigatório

Tamanho: 2

Chave Primária

__OS3279__

RN125

__Registro I – Ano:__  Preencher com o ano da apuração\.

Tipo: Numérico

Campo: Obrigatório

Tamanho: 4

Chave Primária

__OS3279__

RN126

__Registro I – Notas Canceladas:__ Preencher com a relação de notas canceladas no período referente ao tipo da declaração\.

Regra de recuperação para GIF\-PJ:

O registro I da GIF\-PJ, deve considerar as notas com as seguintes características:

\- Notas fiscais de serviço emitidas \(campo MOVTO\_E\_S = ”9” da SAFX07\)

\- Município ISS \(SAFX07\) = Florianópolis \(local da prestação do serviço\)

\- Classificação do Documento fiscal = 2 ou 3

\- Empresa e estabelecimentos escolhidos na tela de geração

\- Data Fiscal dentro do periodo de referencia \(Atualmente é considerado a data fiscal e não data de emissão\)\.

\- Notas __canceladas__ \(campo SITUACAO = “S” da SAFX07\)

Regra de recuperação para GIF\-ST:

Este registro I da GIF\-ST deve considerar as notas com as seguintes características:

\- Notas fiscais de serviço recebidas \(campo MOVTO\_E\_S <> ”9” da SAFX07\)

\- Classificação do Documento fiscal = 2 ou 3

\- Empresa e estabelecimentos escolhidos na tela de geração

\- Data Fiscal dentro do periodo de referencia \(Atualmente é considerado a data fiscal e não data de emissão\)\.

\- Notas __canceladas__ \(campo SITUACAO = “S” da SAFX07\)

__\[ALTERAÇÃO\- MFS609796\] __Alteração da Regra para desconsiderar as Notas Fiscais sem Retenção

Recuperar a Nota Fiscal somente se um dos Campos abaixo estiver preenchido:

Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV __> 0__

__ Ou__

     Se o campo VLR\_ISS da tabela DWT\_ITENS\_SERV __> 0__

__        Gerar __a Nota Fiscal para o Registro GIF\-ST ou GIF\-PJ

__Senão __desconsiderar a Nota Fiscal

Para os casos em que o número da nota fiscal tiver hífen, o mesmo deverá ser retirado na recuperação da informação\.

Regra de preenchimento:

*\- Campo deverá ser preenchido apenas com dígitos, hífen ou vírgula\. *

*\- Para intervalos adjacentes deve\-se usar hífen\.*

*\- Para intervalos não adjacentes deve\-se usar vírgula*\.

*Ex*\.: Notas fiscais 1,2,3,4,6 e 8 podem ser informadas como 1\-4,6,8\.

Tipo: Texto

Campo: Não Obrigatório

Tamanho: 255

__OS3279__

__MFS609796__

RN126A

__\[EXCLUÍDA MSF\-61899\] Registro I – Despesa com Funcionário: __Preencher com o conteúdo informado no campo “Despesa com Funcionários” na Tela de Geração\.

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

RN126B

__\[EXCLUÍDA MSF\-61899\] Registro I – Número de Funcionários: __Preencher com o conteúdo informado no campo “Número de Funcionários” na Tela de Geração\.

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

RN127

__Registro I – Indicador Sem Movimento: __Indicar se contribuinte não prestou e nem contratou serviços no período\.

Regra para preenchimento do campo: 

\- Para GIF\-ST: 

Se *flag “GIF\-ST” e “Sem movimento”  estiver *__*marcado,*__*  preencher com “1”\.*

Se flag* “GIF\-ST” e “Sem movimento”  estiver *__*desmarcado*__*, preencher com “0”\.*

*\- Para GIF\-PJ:*

Se *flag “GIF\-PJ” e “Sem movimento”  estiver *__*marcado,*__*  preencher com “1”\.*

Se flag* “GIF\-PJ” e “Sem movimento”  estiver *__*desmarcado*__*, preencher com “0”\.*

Tipo: Numérico

Campo: Obrigatório

Tamanho: 1

__OS3279__

RN128

__Registro I – Indicador de PJ ou ST: __Indicar se tipo da GIF é PJ ou ST\.

Regra de preenchimento:

      \- Para GIF\-PJ preencher com “0”

\- Para GIF\-ST preencher com “1”

Tipo: Numérico

Campo: Obrigatório

Tamanho: 1

Chave Primária

__OS3279__

RN128A

__\[EXCLUÍDA MSF61899\] Registro I – Zero: __Preencher com um zero\.

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

RN129

__Registro I – Retificadora: __Indicar se declaração é retificadora\.

Regra de preenchimento: 

\- Para GIF\-ST: 

Se flag* “GIF\-ST” e “Retificadora” estiver *__*marcado*__*, preencher com “1”\.*

Se flag* “GIF\-ST” e “Retificadora” estiver *__*desmarcado,*__* preencher com “0”\.*

*\- Para GIF\-PJ:*

Se flag* “GIF\-PJ” e “Retificadora” estiver *__*marcado*__*, preencher com “1”\.*

Se flag* “GIF\-PJ” e “Retificadora” estiver *__*desmarcado,*__* preencher com “0”\.*

Tipo: Numérico

Campo: Obrigatório

Tamanho: 1

Chave Primaria

__\[EXCLUÍDA MSF61899\] __Campo excluído com a versão “__1\.03\.0001__”\.

__OS3279__

__MFS\-32260__

__MFS\-61899__

RN129A

__\[EXCLUÍDA MFS\-61899\]__ __Registro I – Lista de Notas Fiscais Retidas: __

Observação:

Para definir esse campo, eu, Liliane, consultei a área de informação \(Paulo Silva\)\. Chegamos a uma interpretação que, tanto a GIF\-PF quando a GIF\-PJ, este campo deve demonstrar as notas cujo ISS foi retido pelo tomador\. Sendo assim defini este campo com aplicação das regras do documento “__Regras de Negócios\.doc__”:

__ 1 – Tipo de Recolhimento \(Retenção de ISS\) __para notas recebidas__\.__

 __2\. Tipo de Recolhimento \(Retenção na fonte\) __para notas emitidas\.

Regra de recuperação para GIF\-PJ:

O registro I da GIF\-PJ, deve considerar as notas com as seguintes características:

\- Notas fiscais de serviço emitidas \(campo MOVTO\_E\_S = ”9” da SAFX07\)

\- Município ISS \(SAFX07\) = Florianópolis \(local da prestação do serviço\)

\- Classificação do Documento fiscal = 2 ou 3

\- Empresa e estabelecimentos escolhidos na tela de geração

\- Data Fiscal dentro do periodo de referencia \(Atualmente é considerado a data fiscal e não data de emissão\)\.

\- Notas __não canceladas__ \(campo SITUACAO <> “S” da SAFX07\)

 \- Pelo menos umas das seguintes opções seja verdadeira: <a id="recolhimento_fonte_emit_prestador"></a>\(função __recolhimento\_fo\_emit\_prestador __= S\)

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “1” \(Retido pelo Tomador\)\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV __não__ está preenchido\.

Regra de recuperação para GIF\-ST:

O registro I da GIF\-ST deve considerar as notas com as seguintes características:

\- Notas fiscais de serviço recebidas \(campo MOVTO\_E\_S <> ”9” da SAFX07\)

\- Município ISS \(SAFX07\) = Florianópolis \(local da prestação do serviço\)

\- Classificação do Documento fiscal = 2 ou 3

\- Empresa e estabelecimentos escolhidos na tela de geração

\- Data Fiscal dentro do periodo de referencia \(Atualmente é considerado a data fiscal e não data de emissão\)\.

\- Notas __não canceladas__ \(campo SITUACAO =<> “S” da SAFX07\)

\- Pelo menos umas das seguintes opções seja verdadeira: \(função __recolhimento\_receb\_tomador __= S\)

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL está preenchido\. Se estiver preenchido, verificar se está preenchido com “1” \(Retido pelo Tomador\)\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV __está__ preenchido\.

Para os casos em que o número da nota fiscal tiver hífen, o mesmo deverá ser retirado na recuperação da informação\.

Regra de preenchimento:

*\- Campo deverá ser preenchido apenas com dígitos, hífen ou vírgula\. *

*\- Para intervalos adjacentes deve\-se usar hífen\.*

*\- Para intervalos não adjacentes deve\-se usar vírgula*\.

*Ex*\.: Notas fiscais 1,2,3,4,6 e 8 podem ser informadas como 1\-4,6,8\.

Tipo: Texto

Tamanho: 255

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

RN129B

__\[EXCLUÍDA MFS\-61899\]__ __Registro I – ISS Total de Notas Fiscais Retidas: __Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV dos itens das notas fiscais que compõe o campo “__Lista de Notas Fiscais Retidas__”

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

RN129C 

__\[EXCLUÍDA MFS\-61899\]__ __Registro I – Lista de Notas Fiscais Estornadas:__ 

__\[MFS\-32260\]:__

__Este campo foi incluído no layout 1\.03\.0001\. Não consegui fechar uma regra para definição do seu preenchimento\. Por enquanto será gerado com branco\.__

Tipo: Texto

Tamanho: 255

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

RN129D

__\[EXCLUÍDA MFS\-61899\]__ __Registro I – ISS Total de Notas Fiscais Estornadas: __Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV dos itens das notas fiscais que compõe o campo “__Lista de Notas Fiscais Estornadas__”\.

__MFS\-32260\]:__

__Este campo foi incluído no layout 1\.03\.0001\. Não consegui fechar uma regra para definição do seu preenchimento\. Por enquanto será gerado com zeros\.__

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

__MFS\-61899__

RN130

__Regras para a geração do Registro J – GIF\-PJ e GIF\-ST – Itens da Guia de Informações Fiscais__

Registro para geração dos itens da GIF\-PJ e GIF\-ST\.

O registro J será gerado se pelo menos um dos campos “Gerar GIF\-PJ” ou “Gerar GIF\-ST” estiver marcado, na tela de geração e o campo Sem Movimento correspondente estiver desmarcado\.  Se o campo Sem Movimento correspondente estiver marcado, o registro J não será gerado\.

Esse registro identifica a nova codificação CNAE \+ CFPS \+ CST, informando o total apurado no mês para cada contribuinte\.

Para a geração deste registro é necessário, como pré\-requisito, o registro I\.

Por outro lado, o registro I sem pelo menos 1 registro J não tem sentido, exceto nos casos de sem movimento\.

GIF\-PJ: *notas fiscais de saída, com pessoa jurídica de prestação de serviços do município de Florianópolis\.*

GIF\-ST: *para notas fiscais de entrada, com contribuintes tomadores de serviços de prestadores do município de Florianópolis ou de fora do município\.*

Para cada registro I, podem ser gerados vários registros J, onde cada um deve ter um enquadramento CNAE\+CFPS\+CST\.

Se campos “Gerar GIF\-PJ” estiver marcado então:

     Gerar no arquivo um registro “I” para a GIF\-PJ\.

     Gerar no arquivo N registro “J” para a GIF\-PJ, caso o campo Sem Movimento esteja desmarcado\.

Se campos “Gerar GIF\-ST” estiver marcado então:

     Gerar no arquivo um registro “I” para a GIF\-ST\.

     Gerar no arquivo N registro “J” para a GIF\-ST, caso o campo Sem Movimento esteja desmarcado\.

Para GIF\-PJ:

O registro J da GIF\-PJ, deve considerar as notas com as seguintes características:

\- Notas fiscais de serviço emitidas \(campo MOVTO\_E\_S = ”9” da SAFX07\)

\- Município ISS \(SAFX07\) = Florianópolis

\- Classificação do Documento fiscal = 2 ou 3

\- Empresa e estabelecimentos escolhidos na tela de geração

\- Data Fiscal dentro do periodo de referencia \(Atualmente é considerado a data fiscal e não data de emissão\)\.

\- Não devem ser consideradas as notas canceladas\.

Para GIF\- ST:

Este registro I da GIF\-ST deve considerar as notas com as seguintes características:

\- Notas fiscais de serviço recebidas \(campo MOVTO\_E\_S <> ”9” da SAFX07\)

\- Classificação do Documento fiscal = 2 ou 3

\- Empresa e estabelecimentos escolhidos na tela de geração

\- Data Fiscal dentro do periodo de referencia \(Atualmente é considerado a data fiscal e não data de emissão\)\.

\- Não devem ser consideradas as notas canceladas\.

__OS3279__

RN131

__Registro J – Tipo do Registro: __Preencher com o valor fixo “J”\.

Tipo: Texto

Campo: Fixo

Tamanho: 1

__OS3279__

RN132

__Registro J – CMC: __Preencher com o CMC do contribuinte\.

Campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO

Tipo: Numérico

Campo: Obrigatório

Tamanho: 7

Chave Primaria

__\[EXCLUÍDA MFS\-61899\]__ Campo excluído com a versão “__1\.03\.0001__”\.

__OS3279__

__MFS\-32260__

__MFS\-61899__

RN133

__Registro J – CNPJ:__ Preencher com o CNPJ do contribuinte\.

Campo CGC da tabela ESTABELECIMENTO\.

Tipo: Numérico

Campo: Obrigatório

Tamanho: 14

Chave Primaria

__OS3279__

RN133A

__\[EXCLUÍDA MFS\-61899\]__ __Registro J – Identificação:__ Preencher fixo com “01”\.

Campo incluído pela versão “__1\.03\.0001__”\.

__MFS\-32260__

RN134

__Registro J__ __– Mês:__ Preencher com o mês da apuração\.

Tipo: Numérico

Campo: Obrigatório

Tamanho: 2

Chave Primaria

__OS3279__

RN135

__Registro J – Ano:__ Preencher com o ano da apuração\.

Tipo: Numérico

Campo: Obrigatório

Tamanho: 4

Chave Primaria

__OS3279__

RN136

__Registro J – Tipo da Declaração: __Indica tipo da GIF é PJ ou ST\.

__ __

Regra de preenchimento:

      \- Para GIF\-PJ preencher com “0”

Notas fiscais de serviço emitidas \(campo MOVTO\_E\_S=”9” da SAFX07\)

Município ISS \(SAFX07\) = Florianópolis

\- Para GIF\-ST preencher com “1”

Notas fiscais de serviço recebidas \(campo MOVTO\_E\_S<>”9” da SAFX07\)

Tipo: Numérico

Campo: Obrigatório

Tamanho: 1

Chave Primaria

__\[EXCLUÍDA MFS\-61899\]__ Campo excluído com a versão “__1\.03\.0001__”\.

__OS3279__

__MFS\-32260__

RN137

__Registro J – CNAE:__ Preencher com o conteúdo do campo “Atividade CNAE DES Florianópolis” da tela Parâmetros – Atividade CNAE referente ao campo__ __COD\_ATIVIDADE da tabela CÓDIGO DE SERVIÇOS \(SAFX2018\)\. Se o campo não estiver preenchido, preencher com brancos\.

Tipo: Numérico

Campo: Obrigatório

Tamanho: 11

Chave Primaria

Preencher com o conteúdo do campo COD\_ATIVIDADE da tabela CÓDIGO DE SERVIÇOS \(SAFX2018\)\.

__\[EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 11 para 7 pela versão “__1\.03\.0001__”\.

__CH20110\_2016__

__CH21046\_2016__

__MFS\-32260__

__MFS\-61899__

RN138

__Registro J – CFPS:__ Preencher com o CFPS do item da nota fiscal de serviço\.

Campo Código Fiscal de Prestação de Serviço da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico

Campo: Obrigatório

Tamanho: 4

Chave Primaria

__OS3279__

RN139

__Registro J – CST:__ Preencher com o CST do item da nota fiscal de serviço\. 

Campo Código Tributação ISS da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico

Campo: Obrigatório

Tamanho: 3

Chave Primaria

__\[EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 3 para 2 pela versão “__1\.03\.0001__”\.

__OS3279__

__MFS\-32260__

__MFS\-61899__

RN140

__Registro J – Valor Contábil Total:__ Preencher com o somatório do Valor Contábil de todos os serviços das notas fiscais relacionadas no campo Notas Emitidas ou Recebidas \(RN142\)\.

Campo Vlr\. Serviço \(VLR\_SERVICO\) da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico

Campo: Obrigatório

Tamanho: 18

Formato: 016V002

__OS3279__

RN141

__Registro J – Base de Cálculo Total:__ Preencher com o somatório da Base de Cálculo de todos os serviços das notas fiscais relacionadas no campo Notas Emitidas ou Recebidas \(RN142\)\.

Deve ser sempre inferior ou igual ao campo Valor Contábil Total \(RN138\)\.

Campo Base ISS \(VLR\_BASE\_ISS\_1\) da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico

Campo: Obrigatório

Tamanho: 18

Formato: 016V002

__OS3279__

RN142

__Registro J – Alíquota de ISS:__ Preencher com a Aliquota do ISS\.

Campo Aliquota ISS \(ALIQ\_TRIBUTO\_ISS\) da tabela DWT\_ITENS\_SERV\.

__Preencher__ com o campo VLR\_ALIQ\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\.  __Ou__

         __Se __o campo VLR\_ALIQ\_ISS\_RETIDO não estiver preenchido ou preenchido com zeros

             __Preencher__ com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

Senão preenchido não gerar o registro\.

Tipo: Numérico

Campo: Obrigatório

Tamanho: 18  

Formato: 016V002 

__\[EXCLUÍDA MFS\-61899\]__ Campo sofreu alteração de tamanho de 18 para 6 pela versão “__1\.03\.0001__”\.

__OS3279__

__MFS\-32260__

__MFS\-61899__

__MFS\-92178__

RN143

__Registro J – Valor do ISS:__ Preencher com o somatório do Valor do ISS de todos os serviços das notas fiscais \.

Campo Vlr\. ISS \(VLR\_TRIBUTO\_ISS\) da tabela DWT\_ITENS\_SERV

__Preencher__ com o somatório do campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\. __Ou__ __ __

         __Se __o campo VLR\_ISS\_RETIDO não estiver preenchido ou preenchido com zeros

            __Preencher__ com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

Senão preenchido não gerar o registro\.

Tipo: Numérico

Campo: Obrigatório

Tamanho: 18

Formato: 016V002

__OS3279__

__MFS\-92178__

RN144

__Registro J – Notas Emitidas ou Recebidas: __Preencher com o número das notas Emitidas ou Recebidas que estejam enquadradas na CNAE, CFPS e CST\.

__Tela\-A__ __Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

  __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ __ __  

  __E__

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __ 

Então, Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL__

Se não, 

Campo Número do Documento Fiscal \(NUM\_DOCFIS\) da SAFX07

Este campo consiste em uma listagem de todas as notas fiscais enquadradas na CNAE, CFPS e CST anteriormente informadas neste registro usando apenas dígitos, hífen ou vírgula\. 

*Para intervalos adjacentes utilizar hífen\. *

*Para intervalos não adjacentes utilize vírgula\. *

*Ex\.: notas fiscais 1,2,3,4,6 e 8 podem ser informadas como 1\-4,6,8*

Tipo: Numérico

Campo: Obrigatório

Tamanho: 4000

__OS3279__

__OS3341\-A3__

RN145

__Registro J – Matricula CEI: __Preencher com a Matricula CEI do Cadastro de Obras\.

Regra de preenchimento:

Para as Notas Emitidas:

Preencher com o campo Cod\. CEI \(campo COD\_CEI da SAFX07\)\.

Para as Notas Recebidas:

Deixar o campo em branco\.

Tipo: Texto

Campo: Não Obrigatório

Tamanho: 12

__\[EXCLUÍDA MFS\-61899\]__ Campo excluído com a versão “__1\.03\.0001__”\.

__OS3279__

__MFS\-32260__

__MFS\-61899__

RN146

__Ordem de geração dos  registros__

Os registros referentes à GIF deverão ser gerados na seguinte ordem:

H, C, P, T, E, F, R, I, J e L\.

__OS3279__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


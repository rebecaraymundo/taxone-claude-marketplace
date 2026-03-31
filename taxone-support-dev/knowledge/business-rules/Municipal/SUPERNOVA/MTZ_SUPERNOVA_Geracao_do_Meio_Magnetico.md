# MTZ_SUPERNOVA_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_SUPERNOVA_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2025-10-07
- **Tamanho:** 63 KB

---

THOMSON REUTERS

Geração do Meio Magnético 

##### DOCUMENTO DE REQUISITO

__DR__

__Nome__

__Descrição__

OS3473

ISS Nova Lima – Criação do Novo Módulo Nova Lima

Será criado um novo módulo “Nova Lima” dentro do grupo de obrigações “Municipal”, que permitirá a geração de um meio magnético onde serão informados documentos fiscais de serviço emitidos declarados e cancelados e recebidos declarados para o período e estabelecimento escolhidos, onde apenas estabelecimentos sediados em Nova Lima poderão ser escolhidos\.

CH2212/2016

Ajuste nos campos 05 – ‘Competência’ e 09\-‘Dia’

Ajuste na informação gravada nos campos 05 – ‘Competência’ e 09 – ‘Dia’\.

MFS3966

Inclusão de item de menu

<a id="OLE_LINK37"></a><a id="OLE_LINK38"></a><a id="OLE_LINK39"></a>Será criado um novo item de menu para a inclusão da tela de Cadastro de Prestadores/Tomadores Eventuais 

Visualizar Documento: \(MTZ\_SUPERNOVA\_Cadastro\_Prestadores\_Tomadores\_Eventuais\)\.

MFS4206

DW \- MUNICIPAL \- SuperNova – Inclusão de novo município\.

Este documento tem como objetivo incluir o município de Santa Luzia/MG para ser atendido pelo validador SuperNova\.

MFS\_2071

DW \- MUNICIPAL – Meio Magnético – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

CH7821\_2016

Alteração no preenchimento do campo 10 para Serviços Tomados

Este documento tem como objetivo alterar o preenchimento do campo “10 \- Tipo de Lançamento” do registro 3 para Serviços Tomados\.

CH7821\-A\_2016

Alteração no preenchimento do campo 10 para Serviços Tomados e Prestados

Este documento tem como objetivo alterar o preenchimento do campo “10 \- Tipo de Lançamento” do registro 3 para Serviços Tomados e Prestados para situação “R”\.

MFS8132

DW \- MUNICIPAL \- SuperNova – Inclusão de novo município\.

Este documento tem como objetivo incluir o município de Sabará/MG para ser atendido pelo validador SUPERNOVA\.

MFS16576

DW \- MUNICIPAL \- SuperNova – Inclusão de novo município\.

Este documento tem como objetivo incluir o município de Cabo Frio/RJ para ser atendido pelo validador SUPERNOVA\.

MFS19797

DW \- MUNICIPAL \- SuperNova – Inclusão de novos municípios\.

Este documento tem como objetivo incluir o município de Conselheiro Lafaiete e Itabirito\-MG para ser atendido pelo validador SUPERNOVA\.

MFS25950

DW \- MUNICIPAL \- SuperNova – Inclusão de novo município\.

Este documento tem como objetivo incluir o município de Ribeirão das Neves/MG para ser atendido pelo validador SUPERNOVA\.

MFS829438

DW \- MUNICIPAL \- SuperNova – Ajuste Nomenclatura

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

__REGRAS DE NEGÓCIO__

__Cód\.__

__Descrição__

__DR__

__RN00__

__Regra para Criação do novo módulo “Nova Lima”:__

O novo módulo “Nova Lima” deve ficar localizado no grupo “Municipal” abaixo do módulo “Natal”\.

A descrição funcional do módulo será: O objetivo deste módulo é a geração do meio magnético para atendimento ao ISS digital Nova Lima, realizando a escrituração de todos os serviços prestados e/ou tomados pelo declarante, baseados ou não em documentos fiscais emitidos ou recebidos em razão da prestação de serviços, sujeitos ou não à incidência do ISSQN, seja o imposto devido ou não do Município\.

__OS3473__

__RN01__

__Regra para abertura do módulo:__

Se o estabelecimento selecionado no Manager não pertencer ao estado de Minas Gerais \(UF = “MG”\) e ao município de Nova Lima \(código do município IBGE = “44805”\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Nova Lima, Minas Gerais\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Serão exibidos os botões “Sim” e “Não” \(default\)\. Se o usuário clicar no botão “Sim”, o módulo será aberto normalmente, senão o módulo não será aberto\.

__OS3473__

__RN02__

__Regra p/ hierarquia de menus__

Deverão ser criados os seguintes menus e sub\-menus no SuperNova:

- Obrigações
	- Geração do Meio Magnético
	- Arquivo de Entradas de Serviço \(Const\. Civil/ utilities/ Telecom\)
	- <a id="OLE_LINK32"></a><a id="OLE_LINK33"></a>Cadastro de Prestadores/Tomadores Eventuais
- Janela

Ajuda

*Obs\.:* A rotina de geração do cadastro está localizada no documento matriz MTZ\_SUPERNOVA\_Cadastro\_Prestadores\_Tomadores\_Eventuais\.

__OS3473__

__MFS3966__

__RN03__

__Regra para geração do Meio Magnético:__

A geração do meio magnético deve ser feita no padrão Framework\. Caso o usuário selecione mais de um estabelecimento na geração, o sistema irá gerar um arquivo para cada estabelecimento\.

__OS3473__

__RN04__

__Regra do campo Data Inicial da tela Obrigações – Geração Meio Magnético:__

O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE\.

__OS3473__

__RN05__

__Regra do campo Data Final da tela Obrigações – Geração Meio Magnético:__

O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE\. 

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.”

__OS3473__

__MFS\_2071__

__  RN06__

__Regra do campo Tipo do Arquivo da tela de Obrigações – Geração Meio Magnético:__

O campo deve ser um checkbox, com as opções: Produção e Teste\.

Por padrão, trazer selecionado Produção\.

Somente um pode ser selecionado\.

__OS3473__

__RN07__

__Regra do campo Sequencial de Arquivo da tela de Obrigações – Geração Meio Magnético:__

O campo deve permitir que o usuário digite o sequencial desejado, com no máximo 6 posições\.

Campo de preenchimento obrigatório, caso o usuário não informe valor para este campo, exibir mensagem de preenchimento obrigatório\.

__OS3473__

__RN08__

__Regra do campo Número do Arquivo da tela de Obrigações – Geração Meio Magnético:__

O campo deve permitir que o usuário digite o número do arquivo desejado, com no máximo 6 posições\.

Campo de preenchimento obrigatório, caso o usuário não informe valor para este campo, exibir mensagem de preenchimento obrigatório\.

__OS3473__

__RN09__

__Regra para exibição dos Estabelecimentos na tela de geração:__

O\(s\) Estabelecimento\(s\) exibido\(s\) na tela de geração obedecer as seguintes premissas:

- Que esteja licenciado;
- Que o usuário possua direito de acesso no PowerLock;
- Que pertença à ao estado de Minas gerais \(UF = “MG”\) e ao município de Nova Lima \(código IBGE = “44805”\)
- Que pertença à ao estado de Minas Gerais \(UF = “MG”\) e ao município de Santa Luzia \(código IBGE = “57807”\)
- Que pertença à ao estado de Minas Gerais \(UF = “MG”\) e ao município de Sabará \(código IBGE = “56700”\)
- Que pertença à ao estado do Rio de Janeiro \(UF = “RJ”\) e ao município de Cabo Frio \(código IBGE = “704”\)
- Que pertença à ao estado do Minas Gerais \(UF = “MG”\) e ao município de Minas Gerais \(código IBGE = “18304”\)
- Que pertença à ao estado do Minas Gerais \(UF = “MG”\) e ao município de Minas Gerais \(código IBGE = “31901”\)

__MFS3966__

__MFS4206__

__MFS8132__

__MFS16576__

__MFS19797__

__RN10__

__Regra para abas existentes na geração do meio magnético:__

Ao gerar o meio magnético devem ser exibidas as abas “Log”, “Arquivo”, “Processos” e “Relatório”\. A aba “Arquivo” deve exibir o arquivo que poderá ser salvo localmente\. A aba “Log” deve exibir a mensagem “Processo concluído com sucesso” quando o arquivo for gerado corretamente, caso contrário exibir a mensagem  “Processo concluído com erros”\.

__OS3473__

__RN11__

__Regra p/ nomenclatura do arquivo magnético:__

O nome do arquivo deve seguir a seguinte regra:

__EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ AAAAMMDD\.REM__, onde:

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.REM__: extensão do arquivo\.

Ex: EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.REM

ESC<Inscr\. Municipal \(sem máscara\)>\_<AAAAMMDD>\_<Recuperar o campo digitado na tela de geração “Número do arquivo”>\.REM   

Exemplos:	ESC10350056\_20080805\_01\.REM

	ESC30225586\_20080704\_01\.REM

__OS3473__

__MFS\-829438      __

__RG00__

__Regras Gerais para geração do Meio Magnético:__

O primeiro registro deve ser obrigatoriamente, um registro do tipo “0”\. Este registro deverá ser único no arquivo\.

Campos numéricos deverão ser alinhados à direita, preenchidos com zeros a esquerda, devendo completar com zeros as posições não preenchidas\. Não deverão ser colocados vírgula ou ponto\. Ex: Campo Numérico\(10\) cujo valor seja 45222,00 deverá ser formatado = 0004522200\.

Campos alfanuméricos \(Tipo X\) devem ser alinhados à ESQUERDA e preenchidos com espaços à direita\.

Campos do tipo Data deverão ser preenchidos no formato DDMMAAAA\.

Todos os campos deverão obedecer rigorosamente o tamanho e a formatação definidos pelo layout\.

__OS3473__

__RG01__

__Regra para recuperação dos registros:__

Serão listados todos os registros de documentos de Entrada e Saída de serviço \(código de classificação ‘2’ ou ‘3’\), emitidos \(cancelados e declarados\) e recebidos declarados com data fiscal dentro do período de referência, para a empresa e o estabelecimento escolhidos na tela de geração\. Apenas serão gerados arquivos para estabelecimentos diferentes do Município selecionado\.

Deve se consolidar em uma única linha, valores dos itens de um mesmo documento fiscal, há quebra em mais linhas quando os campos 

Tipo de Lançamento, Tipo de Escrituração, Alíquota ref\. ao Super Simples ou Código de Obra possuírem valores diferentes dentre os itens\.

__OS3473__

__RN12__

__Regra para geração dos dados:__

As tabelas de Capas de Documentos Fiscais e Itens de Serviço \(DATAMART\), assim como a tabela de Cadastro de Pessoas Físicas/Jurídicas devem estar devidamente povoadas\. 

__OS3473__

__RN13__

__Header \(Remessa/Retorno\):__

__Regra para o preenchimento do campo 01 \-‘ Identificador do Header’:__

Deverá ser informado o caractere fixo ‘0’\.

__Obs: __ Campo obrigatório\.

__OS3473__

__RN14__

__Regra para o preenchimento do campo 02 – ‘Data de Geração do Arquivo’:__

Recuperar a data de geração do Meio Magnético\.

__Obs:__ Campo obrigatório\.

__OS3473__

__RN15__

__Regra para o preenchimento do campo 03 – ‘Inscrição Municipal do Contribuinte’:__

Recuperar a informação do campo INSCR\_MUNICIPAL da tabela ESTABELECIMENTO, referente ao estabelecimento selecionado na tela de geração\.

__Obs: Alinhar campo à esquerda, não preencher com zeros à esquerda __

Formato: 9999999999 – Campo obrigatório\.

__OS3473__

__RN16__

__Regra para o preenchimento do campo 04 – ‘CNPJ/CPF do Contribuinte’:__

Recuperar o campo CGC na tabela ESTABELECIMENTO referente ao estabelecimento selecionado na tela de geração

__Obs: Alinhar campo à esquerda, não preencher com zeros à esquerda __

Campo Obrigatório\.

Formato: 9999999999

__OS3473__

__RN17__

__Regra para o preenchimento do campo 05 – ‘Nome do Contribuinte’:__

Recuperar o campo__ __RAZAO\_SOCIAL da tabela ESTABELECIMENTO para o estabelecimento selecionado na tela de geração\.

__Obs: Alinhar campo à esquerda, não preencher com zeros à esquerda __

Campo obrigatório\.

__OS3473__

__RN18__

__Regra para o preenchimento do campo 06 – ‘Sequencial de Arquivo’:__

Deve recuperar a informação digitada na tela de geração, campo ‘Sequencial de Arquivo’\.

Seqüencial numérico por arquivo gerado, preenchido com zeros à esquerda, exemplo: ‘00001’ \(00001, 00002,\.\.\.\.\)  deve ser alinhado à direita\.

__Obs:__ __Alinhar campo à direita, preencher com zeros à esquerda\.__

Campo obrigatório\.

__OS3473__

__RN19__

__Regra para o preenchimento do campo 07 – ‘Versão do Arquivo’:__

Preencher com ‘0202’  

__Obs: __ Campo obrigatório\.

__OS3473__

__RN20__

__Regra para o preenchimento do campo 08 – ‘Arquivo Produção ou Teste:__

Recuperar a informação do parâmetro __Tipo Arquivo__ informado na tela de __Geração do Meio Magnético__\. Seguindo a seguinte regra:

P – Produção

T – Teste 

__Obs: __ Campo obrigatório\.

__OS3473__

__RN21__

__Regra para o preenchimento do campo 09 – ‘Nome do Sistema’:__

Preencher com ‘ISSDigital’  

__Obs: __ Campo obrigatório\.

__OS3473__

__RN22__

__Regra para o preenchimento do campo 10 – ‘Brancos’:__

Preencher com Brancos  

__Obs: __ Campo obrigatório\.

__OS3473__

__RN23__

__Regra para o preenchimento do campo 11 – ‘Sequencial de Registro’:__

Preencher com__ __00001

__Obs: __ Campo obrigatório\.

__OS3473__

__RN24__

__Trailer \(Remessa/Retorno\): __

__Regra para o preenchimento do campo 01 – ‘Identificador do Trailer’:__

Preencher com__ __9

__Obs: __ Campo obrigatório\.

__OS3473__

__RN25__

__Regra para o preenchimento do campo 02 – ‘Brancos’:__

Preencher com__ __Brancos

__Obs: __ Campo obrigatório\.

__OS3473__

__RN26__

__Regra para o preenchimento do campo 03 – ‘Sequencial de Registro’:__

O trailer terá por seqüencial o total de numero de linhas do arquivo\.  

__Obs:__ __Alinhar campo à direita, preencher com zeros à esquerda\.__

Campo obrigatório\.

__OS3473__

__RN27__

__Detalhe \(Remessa/Retorno\) = Escrituração:__

__Regra para o preenchimento do campo 01 – ‘Identificador de Detalhe’:__

Preencher com__ __1

__Obs: __ Campo obrigatório\.

__OS3473__

__RN28__

__Regra para o preenchimento do campo 02 – ‘Inscrição Municipal do Prestador/Tomador’:__

Recuperar a informação do campo __INSRC\_MUNICIPAL__ __\(campo 09\)__ da tabela __X04\_PESSOA\_FIS\_JUR__\.

__Obs: Alinhar campo à esquerda, não preencher com zeros à esquerda __

Campo obrigatório\.

__OS3473__

__RN29__

__Regra para o preenchimento do campo 03 – ‘CNPJ/CPF do Prestador/Tomador’:__

Recuperar a informação do campo __CPF\_CGC \(campo 06\)__ da tabela __X04\_PESSOA\_FIS\_JUR __

Deve conter 11 \(para CPF\) ou 14 \(para CNPJ\)

__Obs: Alinhar campo à esquerda, não preencher com zeros à esquerda __

Campo obrigatório\.

__OS3473__

__RN30__

__Regra para o preenchimento do campo 04 – ‘Enquadramento do Contribuinte’:__

Preencher com:

Preencher com ‘P’ \(Prestador\) quando a nota for de saída \(movto\_e\_s = ‘9’\)

Preencher com ‘T’ \(Tomador\) quando a nota for de Entrada \(movto\_e\_s <> ‘9’\)

__Obs:__ Campo obrigatório\.

__OS3473__

__RN31__

__Regra para o preenchimento do campo 05 – ‘Competência’:__

__\[ALTERADO CH2212/2016\]__

Preencher com o período de referência informado na tela de geração do Meio Magnético\.

Recuperar a informação do mês e ano do campo  __DATA\_EMISSAO__ __\(campo 12\) __da tabela  __DWT\_DOCTO\_FISCAL__\.

__Obs:__ campo no formato AAAAMM

Campo obrigatório\.

__OS3473__

__CH2212/2016__

__RN32__

__Regra para o preenchimento do campo 06 – ‘Nota Fiscal Inicial’:__

Recuperar a informação do campo __NUM\_DOCFIS__ __\(campo 08\) __da tabela __DWT\_DOCTO\_FISCAL__\.

__Obs:__ __Alinhar campo à direita, preencher com zeros à esquerda\.__

Campo obrigatório\.

__OS3473__

__RN33__

__Regra para o preenchimento do campo 07 – ‘Série’:__

Recuperar a informação do campo SERIE\_DOCFIS __\(campo 09\) __da tabela __DWT\_DOCTO\_FISCAL__\.

__Obs: Alinhar campo à esquerda, não preencher com zeros à esquerda __

Campo obrigatório\.

__OS3473__

__RN34__

__Regra para o preenchimento do campo 08 – ‘Nota Fiscal Final’:__

Recuperar a informação do campo __NUM\_DOCFIS__ __\(campo 08\) __da tabela __DWT\_DOCTO\_FISCAL__\.

__Obs:__ __Alinhar campo à direita, preencher com zeros à esquerda\.__

Campo obrigatório\.

__OS3473__

__RN35__

__Regra para o preenchimento do campo 09 – ‘Dia’:__

__\[ALTERADO CH2212/2016\]__

Recuperar somente o dia do campo __DATA\_FISCAL__ __\(campo 04\) DATA\_EMISSAO__ __\(campo 12\) __da tabela  __DWT\_DOCTO\_FISCAL__\.

__Obs:__ __Alinhar campo à direita, preencher com zeros à esquerda\.__

Campo obrigatório\.

__OS3473__

__CH2212/2016__

__RN36__

__Regra para o preenchimento do campo 10 – ‘Tipo de Lançamento’: __

__Deve se utilizar a parametrização de serviços por município, localizado no seguinte caminho:__

Módulo: Municipal > Parâmetros por Município

Menu: Parâmetros > Classificação de Serviços

__*Para notas Emitidas:*__* *

__Preencher com ‘C’ __

__SE__ o campo SITUACAO da tabela DWT\_DOCT\_FISCAL for igual a = ‘S’ 

__Preencher com ‘O’ __

Para que esse campo seja preenchido com ‘O’, é necessário fazer a seguinte checagem:

1\-Localizar COD\_MUNIC\_ISS da tabela SAFX2097 referente ao COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL 

2\-Localizar COD\_MUNIC\_MSAF da SAFX2097 correspondente 

Se o COD\_MUNIC\_MSAF for diferente de ‘44805’ preencher com ‘O’

__Preencher com ‘I’ __

__SE__ o campo IND\_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

__Preencher com ‘T’ __

__SE__ o campo IND\_ISS da tabela ESTABELECIMENTO = “10”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “445”\.

__\[ALTERADA – CH7821\-A\_2016\]__

__Preencher com ‘R’ __

Para que esse campo seja preenchido com “R”, é necessário que pelo menos umas das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “2” e verificar se o campo COD\_MUNICIPIO é igual ao município do estabelecimento selecionado\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\. E1\-RN0001

__Preencher com ‘N’__

Caso nenhuma das opões acima, __\(Regra para preenchimento com ‘N’\) __seja verdadeira\.

__Preencher com ‘A’__

Não será tratada nesta OS

__*Para notas Recebidas:*__

__\[ALTERADA – CH7821\_2016/ CH7821\-A\_2016\]__

__Preencher com ‘C’ __

__SE__ o campo SITUACAO da tabela DWT\_DOCT\_FISCAL for igual a = ‘S’ 

__Preencher com ‘O’ __

Para que esse campo seja preenchido com ‘O’, é necessário fazer a seguinte checagem:

1\-Localizar COD\_MUNIC\_ISS da tabela SAFX2097 referente ao COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL 

2\-Localizar COD\_MUNIC\_MSAF da SAFX2097 correspondente 

Se o COD\_MUNIC\_MSAF for diferente de ‘44805’ preencher com ‘O’

__Preencher com ‘I’ __

__SE__ o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10”, se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

__Preencher com ‘T’ __

Verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota está parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “445”\.

__Preencher com ‘R’__

Para que esse campo seja preenchido com “R”, é necessário que pelo menos umas das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL está preenchido\. Se estiver preenchido, verificar se está preenchido com “1” e verificar se o campo COD\_MUNICIPIO é igual ao município do estabelecimento selecionado\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\. R1\-RN0001

__Preencher com ‘N’__

Caso nenhuma das opões acima, __\(Regra para preenchimento com ‘N’\) __seja verdadeira\.

__Preencher com ‘A’__

Não será tratada nesta OS

__Obs: Alinhar campo à esquerda, não preencher com zeros à esquerda __

Campo obrigatório\.

__OS3473__

__OS3470\-I1C__

__CH7821\_2016__

__CH7821\-A\_2016__

__RN37__

__Regra para o preenchimento do campo 11 – ‘Valor da Nota Fiscal’:__

Recuperar a informação do campo VLR\_TOT  __\(campo 15\) __da tabela DWT\_ITENS\_SERV\.

__Obs:__ __Alinhar campo à direita, preencher com zeros à esquerda\.__

Campo obrigatório\.

__OS3473__

__RN38__

__Regra para o preenchimento do campo 12 – ‘Atividade Cadastrada na Prefeitura’:__

__Quando Enquadramento = Prestador __

Recuperar a informação do campo__ __COD\_ATIVIDADE__ __da tabela ESTABELECIMENTO\.

__Obs:__ Considerar os dois últimos digitos do COD\_ATIVIDADE como subclasse, preenchendo o tamanho conforme regra abaixo, considerar os outros digitos como classe, preenchendo o tamanho conforme formato descrito abaixo \(regra E1 do layout\)\.

__Quando Enquadramento = Tomador__

Recuperar a informação do campo__ __COD\_ATIVIDADE__ __da tabela X04\_PESSOA\_FIS\_JUR\.

__Obs:__ Considerar os dois últimos digitos do COD\_ATIVIDADE como subclasse, preenchendo o tamanho conforme regra abaixo, considerar os outros digitos como classe, preenchendo o tamanho conforme formato descrito abaixo \(regra E1 do layout\)\.

__Formato:__

Atividade cadastrada na prefeitura composta de duas partes: Classe e SubClasse\. Sendo assim o preenchimento ficará da seguinte forma: CCCCCSSSS = 5 dígitos ref\. à Classe \+ 4 dígitos ref\. à SubClasse, devendo ambos serem preenchidos com ‘zeros’ à esquerda caso não se complete o campo\.

Exemplo:

 Atividade  236/1          ficará da seguinte forma:  002360001

 Atividade  00445/01    ficará da seguinte forma:  004450001

 Atividade 99999/0201 ficará da seguinte forma:  999990201

Campo obrigatório\.

__OS3473__

__RN39__

__Regra para o preenchimento do campo 13 – ‘Código da Obra’:__

Se \(IND\_TP\_SERVICO da SAFX2018= ‘1’\)

Recuperar a informação do campo __Canal de Distribuição/Código \(campo 81\)__ da tabela__ DWT\_DOCTO\_FISCAL__\.

__Obs:__ __Alinhar campo à direita, preencher com zeros à esquerda\.__

Campo não obrigatório\. Caso não haja obra deverá ficar em branco

__OS3473__

__RN40__

__Regra para o preenchimento do campo 14 – ‘Tipo de Escrituração’:__

__Preencher com:__

D = Não será tratado nessa OS

C = Preencher se \(IND\_TP\_SERVICO da SAFX2018= ‘1’\)

B = Não será tratado nesta OS

N = Preencher em todos os outros casos

__Obs: Alinhar campo à esquerda, não preencher com zeros à esquerda __

Campo obrigatório\.

__OS3473__

__RN41__

__Regra para o preenchimento do campo 15 – ‘Status \(Retorno\)’:__

Preencher o campo com espaços em branco

__OS3473__

__RN42__

__Regra para o preenchimento do campo 16 – ‘Mensagem \(Retorno\)’:__

Preencher o campo com espaços em branco

__OS3473__

__RN43__

__Regra para o preenchimento do campo 17 – ‘Número da Guia Avulsa’:__

Preencher o campo com espaços em branco

__OS3473__

__RN44__

__Regra para o preenchimento do campo 18 – ‘Alíquota Referente ao Super Simples’:__

__Documentos Emitidos:__

__SE__ o campo ISS  \(tabela Estabelecimento\) estiver marcado como ‘07’\.

Recuperar a informação do campo __Alíquota ISS __VLR\_ALIQ\_ISS  __\(campo 32\) __da tabela DWT\_ITENS\_SERV

__Documentos Recebidos:__

__SE__ o campo Simples Nacional \- IND\_SIMPLES\_NAC \(posição 43 da SAFX04\) estiver marcado como ‘S’ referente ao prestador\.

Recuperar a informação do campo __Alíquota ISS __VLR\_ALIQ\_ISS  __\(campo 32\) __da tabela DWT\_ITENS\_SERV

__Obs:__ __Alinhar campo à direita, preencher com zeros à esquerda\.__

Campo não Obrigatório

__OS3473__

__RN45__

__Regra para o preenchimento do campo 19 – ‘Brancos’:__

Preencher o campo com espaços em branco

__Obs: Campo Obrigatório__

__OS3473__

__RN46__

__Regra para o preenchimento do campo 20 – ‘Sequencial de Registro’:__

O trailer terá por seqüencial o total de numero de linhas do arquivo\.  

__Obs:__ __Alinhar campo à direita, preencher com zeros à esquerda\.__

Campo Obrigatório

__OS3473__

__RN47__

__Regra para Criação do novo módulo “Santa Luzia”:__

O novo módulo “Santa Luzia” deve ficar localizado no grupo “Municipal” abaixo do módulo “Sabará”\.

A descrição funcional do módulo será: O objetivo deste módulo é a geração do meio magnético para atendimento ao ISS digital Santa Luzia, realizando a escrituração de todos os serviços prestados e/ou tomados pelo declarante, baseados ou não em documentos fiscais emitidos ou recebidos em razão da prestação de serviços, sujeitos ou não à incidência do ISSQN, seja o imposto devido ou não do Município\.

__MFS4206__

__RN48__

__Regra para abertura do módulo:__

Se o estabelecimento selecionado no Manager não pertencer ao estado de Minas Gerais \(UF = “MG”\) e ao município de Santa Luzia \(código do município IBGE = “57807”\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Santa Luzia, Minas Gerais\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Serão exibidos os botões “Sim” e “Não” \(default\)\. Se o usuário clicar no botão “Sim”, o módulo será aberto normalmente, senão o módulo não será aberto\.

__MFS4206__

__RN49__

Regra para Criação do novo módulo “Sabará”:

O módulo “Sabará” fica localizado no grupo “Municipal” abaixo do módulo “Ribeirão das Neves”\.

A descrição funcional do módulo será: O objetivo deste módulo é a geração do meio magnético para atendimento ao ISS digital Sabará, realizando a escrituração de todos os serviços prestados e/ou tomados pelo declarante, baseados ou não em documentos fiscais emitidos ou recebidos em razão da prestação de serviços, sujeitos ou não à incidência do ISSQN, seja o imposto devido ou não do Município\.

__MFS8132__

__RN50__

Regra para abertura do módulo:

Se o estabelecimento selecionado no Manager não pertencer ao estado de Minas Gerais \(UF = “MG”\) e ao município de Sabará \(código do município IBGE = “56700”\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Sabará, Minas Gerais\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Serão exibidos os botões “Sim” e “Não” \(default\)\. Se o usuário clicar no botão “Sim”, o módulo será aberto normalmente, senão o módulo não será aberto\.

__MFS8132__

__RN51__

Regra para Criação do novo módulo “Cabo Frio”:

O módulo “Cabo Frio” fica localizado no grupo “Municipal” 

A descrição funcional do módulo será: O objetivo deste módulo é a geração do meio magnético para atendimento ao ISS digital Cabo Frio, realizando a escrituração de todos os serviços prestados e/ou tomados pelo declarante, baseados ou não em documentos fiscais emitidos ou recebidos em razão da prestação de serviços, sujeitos ou não à incidência do ISSQN, seja o imposto devido ou não do Município\.

__MFS16576__

__RN52__

Regra para abertura do módulo:

Se o estabelecimento selecionado no Manager não pertencer ao estado do Rio de Janeiro \(UF = “RJ”\) e ao município de Cabo Frio \(código do município IBGE = “704”\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta: “Este estabelecimento não pertence ao município de Cabo Frio, Rio de Janeiro\. Alguns dados não estarão disponíveis\. Deseja continuar? ”

Serão exibidos os botões “Sim” e “Não” \(default\)\. Se o usuário clicar no botão “Sim”, o módulo será aberto normalmente, senão o módulo não será aberto\.

__MFS16576__

__RN53__

Regra para Criação do novo módulo “Conselheiro Lafaiete”:

O módulo “Conselheiro Lafaiete” fica localizado no grupo “Municipal” 

A descrição funcional do módulo será: O objetivo deste módulo é a geração do meio magnético para atendimento ao ISS digital Conselheiro Lafaiete, realizando a escrituração de todos os serviços prestados e/ou tomados pelo declarante, baseados ou não em documentos fiscais emitidos ou recebidos em razão da prestação de serviços, sujeitos ou não à incidência do ISSQN, seja o imposto devido ou não do Município\.

__MFS19797__

__RN54__

Regra para abertura do módulo:

Se o estabelecimento selecionado no Manager não pertencer ao estado de Minas Gerais \(UF = “MG”\) e ao município de Conselheiro Lafaiete \(código do município IBGE = “18304”\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta: “Este estabelecimento não pertence ao município de Conselheiro Lafaiete, Minas Gerais\. Alguns dados não estarão disponíveis\. Deseja continuar? ”

Serão exibidos os botões “Sim” e “Não” \(default\)\. Se o usuário clicar no botão “Sim”, o módulo será aberto normalmente, senão o módulo não será aberto\.

__MFS19797__

__RN55__

Regra para Criação do novo módulo “Itabirito”:

O módulo “Itabirito” fica localizado no grupo “Municipal” 

A descrição funcional do módulo será: O objetivo deste módulo é a geração do meio magnético para atendimento ao ISS digital Itabirito, realizando a escrituração de todos os serviços prestados e/ou tomados pelo declarante, baseados ou não em documentos fiscais emitidos ou recebidos em razão da prestação de serviços, sujeitos ou não à incidência do ISSQN, seja o imposto devido ou não do Município\.

__MFS19797__

__RN56__

Regra para abertura do módulo:

Se o estabelecimento selecionado no Manager não pertencer ao estado de Minas Gerais \(UF = “MG”\) e ao município de Ribeirão das Neves \(código do município IBGE = “54606”\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta: “Este estabelecimento não pertence ao município de Ribeirão das Neves, Minas Gerais\. Alguns dados não estarão disponíveis\. Deseja continuar? ”

Serão exibidos os botões “Sim” e “Não” \(default\)\. Se o usuário clicar no botão “Sim”, o módulo será aberto normalmente, senão o módulo não será aberto\.

__MFS25950__

__RN57__

Regra para Criação do novo módulo “Ribeirão das Neves”:

O módulo “Ribeirão das Neves” fica localizado no grupo “Municipal” 

A descrição funcional do módulo será: O objetivo deste módulo é a geração do meio magnético para atendimento ao ISS digital Ribeirão das Neves, realizando a escrituração de todos os serviços prestados e/ou tomados pelo declarante, baseados ou não em documentos fiscais emitidos ou recebidos em razão da prestação de serviços, sujeitos ou não à incidência do ISSQN, seja o imposto devido ou não do Município\.

__MFS25950__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


# MTZ-eGoverno-Geracao_Meio_Magnetico

- **Fonte:** MTZ-eGoverno-Geracao_Meio_Magnetico.docx
- **Modificado:** 2026-01-30
- **Tamanho:** 60 KB

---

#                                      EGoverno \- Geração do Meio Magnético

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

Descrição

OS3627

Geração do Meio Magnético EGoverno

Este documento tem como objetivo criar o novo módulo que permita a geração do meio magnético de EGoverno que irá conter as informações de serviços prestados e tomados\.

OS3789

Geração do Meio Magnético EGoverno

Este documento tem como objetivo a inclusão de um novo município para a geração do meio magnético de EGoverno que irá conter as informações de serviços prestados e tomados\.

Taquara – RS

OS4613

Novo Parâmetro – Quebra do Arquivo por Data de Emissão

Implementa novo parâmetro para que seja possível realizar a quebra do arquivo por data de emissão\.

CH18086\_2016

Geração do Meio Magnético EGoverno – Seleção Específica para o município de São Leopoldo\.

Este documento tem como objetivo alterar a seleção dos registros do município de São Leopoldo, retirando o tratamento que havia para levar somente notas fiscais de serviços com retenção pelo tomador dentro do próprio município\.

CH14367\_2017

MFS\-12519

Geração do Meio Magnético EGoverno

Esse documento tem como objetivo alterar a geração do campo série do meio magnético\.

MFS46569

Andréa Rocha

Alteração da regra de preenchimento do campo data\_informacao para o município de São Leopoldo\.

MFS46567

Andréa Rocha

Alteração da regra de recuperação dos serviços tomados para o município de São Leopoldo\.

MFS46564

Andréa Rocha

Alteração da regra de preenchimento do campo valor\_tributavel para o município de São Leopoldo\.

MFS78506

Andréa Rocha

Inclusão do parâmetro “Gerar arquivo por Data de Emissão” na tela de geração\.

MFS80058

Rogério Ohashi

Este documento tem como objetivo ajustar a regra de geração do campo Valor de ISS para o município de Passo Fundo\.

MFS\-792030

Bruna Ribeiro

Alteração da regra de preenchimento do __campo número\_servico da tag <nota> __para o município de São Leopoldo\.

__MFS\-839887__

Rosemeire Santos

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

__MFS\-992587__

Rosemeire Santos

Este documento tem como objetivo ajustar as regras de geração dos campos __Valor Tributável__ e __Alíquota__, para os municípios Esteio, Lajeado, Passo Fundo, Santo Antonio da Patrulha, São Leopoldo e Taquara\.

__MFS\-1023036__

Klemer Monteiro

Aplicação __da regra RN 67\.a__ para o campo “__Valor Tributável__” especifica para o município de São Leopoldo/RS no validador EGoverno\. 

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Esteio” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços prestados e tomados no município de Esteio”\.

OS3627

__RN02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RS” e ao código de município do IBGE igual a “7708” \(Esteio\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Esteio, Rio Grande do Sul\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS3627__

__RN03__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Lajeado” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços prestados e tomados no município de Lajeado”\.

OS3627

__RN04__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RS” e ao código de município do IBGE igual a “11403” \(Lajeado\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Lajeado, Rio Grande do Sul\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

OS3627

__RN05__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Santo Antonio da Patrulha” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços prestados e tomados no município de Santo Antonio da Patrulha”\.

OS3627

__RN06__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RS” e ao código de município do IBGE igual a “17608” \(Santo Antonio da Patrulha\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Santo Antonio da Patrulha, Rio Grande do Sul\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

OS3627

__RN07__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “São Leopoldo” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços prestados e tomados no município de São Leopoldo”\.

OS3627

__RN08__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RS” e ao código de município do IBGE igual a “18705” \(São Leopoldo\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de São Leopoldo, Rio Grande do Sul\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

OS3627

__RN08\-A__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Taquara” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços prestados e tomados no município de Taquara”\.

OS3789

__RN08\-B__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RS” e ao código de município do IBGE igual a “21204” \(Taquara\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Taquara, Rio Grande do Sul\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

OS3789

__RN09__

__Estrutura de menus do módulo EGoverno:__

Deverão ser criados os seguintes menus e sub\-menus no módulo EGoverno:

- Arquivo
- <a id="_Hlk215995419"></a>Geração
	- Meio Magnético
	- Geração do Arquivo de Entradas de Serviços \(Const\. Civil/Utilities/Telecom\)
- Janela
- Ajuda

__OS3627__

__RN10__

__Regra de criação do nome do arquivo__

Serviços Prestados:

__SP\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\.xml__, onde:

       __MMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o prestador de serviço

__       EMPRESA: __Representa o prestador de serviço

__       SP__: representa o arquivo é de serviço prestado\.

       __\.xml__: extensão do arquivo\.

Ex: SP\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\.xml

__P\_EGOVERNO\_DDMMAAAA\.XML__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __P\_EGOVERNO__: representa a obrigação que está sendo gerada, no caso EGoverno\.

       __\.XML__: extensão do arquivo\.

Ex: P\_EGOVERNO\_01012010\.XML

Serviços Tomados:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\.xml__, onde:

       __MMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o prestador de serviço

__       EMPRESA: __Representa o prestador de serviço

__       ST__: representa o arquivo é de serviço tomados\.

       __\.xml__: extensão do arquivo\.

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\.xml

__OS3627__

__OS4613__

__MFS78506__

__MFS\-839887__

__T\_EGOVERNO\_DDMMAAAA\.XML__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __T\_EGOVERNO__: representa a obrigação que está sendo gerada, no caso EGoverno\.

       __\.XML__: extensão do arquivo\.

Ex: T\_EGOVERNO\_01012010\.XML

__\[MFS78506\] __Inclusão do parâmetro “Gerar arquivo por Data de Emissão” na tela de geração

Caso o parâmetro Gerar Arquivo por Data de Emissão estiver marcado, não será possível marcar o parâmetro Quebrar Arquivos por Data de Emissão e deverá ser realizada a seguinte verificação: 

Este arquivo deverá conter todas as notas fiscais com data de emissão dentro do período de referência\.

Quando o parâmetro Quebrar Arquivo por Data de Emissão estiver marcado, não será possível marcar o parâmetro Gerar Arquivos por Data de Emissão e deve ser realizada a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente a data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. As nomenclaturas desses arquivos deverão ser:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\_MMAAAA\.xml__, onde:

      __DDMMAAAA: __Representa a data inicial da geração

      __MMAAAA__: Representa a mês da geração

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o prestador de serviço

__       EMPRESA: __Representa o prestador de serviço

__       ST__: representa o arquivo é de serviço tomados\.

       __\.xml__: extensão do arquivo\.

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\_012010\.xml

__T\_EGOVERNO\_DDMMAAAA\_MMAAAA\.XML__, onde:

__T\_EGOVERNO__: representa a obrigação que está sendo gerada, no caso EGoverno\.

__DDMMAAAA__: representa a data inicial da geração

__MMAAAA__: representa a data do período de geração, mês e ano\.

__\.XML__: extensão do arquivo\.

__Ex:__ T\_EGOVERNO\_01022014\.XML\_012014\.txt

__OBS\.: Este novo parâmetro \(Quebrar Arquivos por Data de Emissão\) será válido, apenas para Notas de Serviços Tomados__

RN11

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Obs: O usuário poderá informar mais de um mês para a geração do meio magnético\.

Gerar Serviços Prestados: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Gerar Serviços Tomados: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Quebrar arquivo por Data de Emissão: deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. A opção S = “Marcado” e N = “Desmarcado"\.

__\[MFS78506\] __Inclusão do parâmetro “Gerar Arquivo por Data de Emissão” na tela de geração

Gerar Arquivo por Data de Emissão: deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Caso o parâmetro Gerar Arquivo por Data de Emissão estiver marcado, não será possível marcar o parâmetro Quebrar Arquivos por Data de Emissão e vice\-versa\.

Estabelecimento: o sistema deve exibir os estabelecimentos pertencentes ao município de EGoverno, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__OS3627__

__OS4613__

__MFS78506__

__RN12__

__Regras referentes à estrutura do Arquivo:__

Verificar documentos Exemplo do lay\-out escrituração prestador \(escriturações enviadas a partir de 01\.06\.09\)\.pdf

                                   Exemplo do Lay\-Out Escrituração Tomador\.pdf

__OS3627__

__RN13__

__Regras referentes à formatação do Arquivo de serviços prestados e tomados:__

- Todos os campos devem estar entre aspas, conforme o exemplo acima
- OS campos de valores não devem conter pontos ou vírgulas e considera as últimas 2 \(duas\) casas como decimais, por exemplo, 1000 representa o número 10,00
- Deverá ser respeitado o tamanho máximo dos campos
- Campos de data devem conter separador “/”\. Ex: 15/02/1998
- O CPF/CNPJ não deve conter separadores, como pontos, traços, etc;
- O número da nota não deve conter separadores, como pontos, traços, etc\.
- Caso o tamanho dos campos de valores for maior que o estabelecido pelo layout, a geração deve truncar o valor, exibindo apenas as primeiras posições do campo\.

OS3627

__RN14__

__Regra geral p/ recuperar serviços prestados__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração

__\[MFS78506\] __Inclusão do parâmetro “Gerar arquivo por Data de Emissão” na tela de geração

- Data fiscal dentro do período de referência, __exceto__ quando o parâmetro “Gerar Arquivos por Data de Emissão” na tela de geração estiver marcado, que deverá ser considerada a Data de Emissão dentro do período de referência

Obs: Quando não houver notas fiscais para o período,não preencher o tag <nota>

Os itens de serviço serão consolidados pelos campos do layout:

\- Aliquota da tag <informação>

\- Situacao da tag <nota>

\- numero\_servio da tag  <nota>

__\- __atividade\_desenvolvida da tag <informacao>

__OS3627__

__MFS78506__

__RN15__

__Regra p/ o cabeçalho do arquivo__

Preencher com o tag <?xml version=”1\.0” encoding=”Iso\-8859\-1” standalone=”yes” ?>

OS3627

__RN16__

__Regra p/ tag <declaração>__

Essa tag indica o início da Declaração

__OS3627__

__RN17__

__Regra p/ tag <empresa__

Abertura da guia por empresa

__OS3627__

__RN18__

__Regra p/ o campo nome da tag <empresa>__

Preencher com o campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO referente ao estabelecimento escolhido\. Tamanho máximo: 100 caracteres\.

__OS3627__

__RN19__

__Regra p/ o campo inscrição da tag <empresa>__

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO referente ao estabelecimento escolhido\. Tamanho máximo: 10 caracteres\.

__OS3627__

__RN20__

__Regra p/ o campo cpfcnpj da tag <empresa>__

Preencher com o campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento escolhido\. Tamanho máximo: 14 caracteres\.

__OS3627__

__RN21__

__Regra p/ tag <informacao__

Abertura do movimento informado

__OS3627__

__RN22__

__Regra p/ o campo exercicio da tag <informacao>__

Preencher com ano do campo Data Inicial da tela de geração do Meio Magnético\. Formato: AAAA\. Tamanho máximo: 4 caracteres\.

__OS3627__

__RN23__

__Regra p/ o campo mes da tag <informacao>__

Preencher com mes do campo Data Inicial da tela de geração do Meio Magnético\. Formato: MM\. Tamanho máximo: 2 caracteres\.

__OS3627__

__RN24__

__Regra p/ o campo aliquota da tag <informacao>__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. Tamanho máximo: 4 caracteres\.

__OS3627__

RN25

__Regra p/ o campo quantidade\_issfixo da tag <informacao>__

Preencher com brancos\.

__OS3627__

__RN26__

__Regra p/ o campo observacao da tag <informacao>__

Preencher com brancos\. Tamanho máximo: 120 caracteres\.

__OS3627__

__RN27__

__Regra p/ o campo basecalculo da tag <informacao>__

Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “02”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “421”\.

Se uma das opções acima forem verdadeiras, preencher com o somatório do campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV\. Caso contrário, esse campo não deverá ser preenchido\. Tamanho máximo: 15 caracteres\.

__OS3627__

__RN28__

__Regra p/ o campo atividade\_desenvolvida da tag <informacao>__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na nota fiscal\. Sem zeros a esquerda e sem ponto\. Tamanho máximo: 6 caracteres\.

__OS3627__

__RN29__

__Regra p/ tag <nota__

Todas as notas fiscais 

__OS3627__

__RN30__

__Regra p/ o campo data\_emissao da tag <nota>__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. Tamanho máximo: 10 caracteres\.

__OS3627__

__RN31__

__Regra p/ o campo numero da tag <nota>__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. Tamanho máximo: 10 caracteres\.

Se o tamanho da nota fiscal no mastersaf for maior que o tamanho especificado por este layout, deve ser exibida a seguinte mensagem: “O tamanho da nota fiscal é maior que o especificado pelo layout\. Favor verificar”

__OS3627__

__RN32__

__Regra p/ o campo serie da tag <nota>__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. Tamanho máximo: 2 caracteres\.

__\[MFS\-12519 \- CH14367\_2017\] __

__Tratamento:__

__      __\- Gravar as duas primeiras posições do campo SERIE\_DOCFIS

     __ \- __Se o tamanho da série no mastersaf for maior que o tamanho especificado por este layout, a geração deve ser exibir a seguinte mensagem de alertar para o usuário: “O tamanho da série é maior que o especificado pelo layout\. Favor verificar”\.

__OS3627__

__CH14367\_2017__

__RN33__

__Regra p/ o campo subserie da tag <nota>__

Preencher com o campo SUB\_SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. Tamanho máximo: 2 caracteres\.

__OS3627__

__RN34__

__Regra p/ o campo observacao da tag <nota>__

Preencher com brancos\. Tamanho máximo: 200 caracteres\.

__OS3627__

__RN35__

__Regra p/ o campo valor\_tributavel da tag <nota>__

Preencher com o somatório do  campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.\. Tamanho máximo: 15 caracteres\.

__OS3627__

__RN36__

__Regra p/ o campo situacao da tag <nota>__

Preencher com,

N, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = ‘S’

E, quando o campo IND\_NOTA\_SERVICO da tabela DWT\_DOCTO\_FISCAL = ‘E’

R, é necessário que pelo menos umas das seguintes opções seja verdadeira:

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.  
  
\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “2" e se  
o local da prestação do serviço = município do módulo selecionado OU

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado

A, quando nenhumas das opções acima forem verdadeiras

P, não será tratada

Tamanho máximo: 1 caractere\.

__OS3627__

__RN37__

__Regra p/ o campo valor\_bruto da tag <nota>__

Preencher com o somatório do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\. Tamanho máximo: 15 caracteres\.

__OS3627__

__RN38__

__Regra p/ o campo valor\_deducao da tag <nota>__

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV\. Tamanho máximo: 15 caracteres\.

__OS3627__

__RN39__

__Regra p/ o campo modelo da tag <nota>__

Preencher com o campo Modelo da tela Parâmetros por Município – Parâmetros – Modelo Msaf x Modelo referente ao modelo cadastrado na nota fiscal\. Tamanho máximo: 2 caracteres\.

__OS3627__

__RN40__

__Regra p/ o campo numero\_servico da tag <nota>__

Preencher com o campo serviço da tela Parâmetros por Município – Parâmetros – Serviços Msaf x Serviços referente ao serviço cadastrado na nota fiscal\. Tamanho máximo: 2 caracteres\.

Se não houver parametrização para o serviço cadastrado na nota fiscal, deve ser exibida a seguinte mensagem: “O serviço não foi parametrizado na tela Parâmetros por Município – Parâmetros – Serviço Msaf x Serviço\. Favor verificar”

__OS3627__

__RN41__

__Regra p/ o campo cnpj\_tomador da tag <nota>__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\. Tamanho máximo: 14 caracteres\.

__OS3627__

__RN42__

__Regra p/ tag </nota>__

Indica o fechamento da nota

__OS3627__

__RN43__

__Regra p/ tag </informacao>__

Indica o fechamento do movimento informado

__OS3627__

__RN44__

__Regra p/ tag </empresa>__

Indica o fechamento da declaração da empresa

__OS3627__

__RN45__

__Regra p/ tag </declaracao>__

Indica o fechamento da declaracao

__OS3627__

__RN46__

__Regra geral p/ recuperar serviços tomados__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou \(cód\_class\_doc\_fis = ‘9’ e tipo do documento = “RPA”\)
- Empresa e estabelecimentos escolhidos na tela de geração

__\[MFS78506\] __Inclusão do parâmetro “Gerar arquivo por Data de Emissão” na tela de geração

- Data fiscal dentro do período de referência, __exceto__ quando o parâmetro “Gerar Arquivos por Data de Emissão” na tela de geração estiver marcado, que deverá ser considerada a Data de Emissão dentro do período de referência
- Notas não canceladas \(situacao <> ‘S’\)
- Apenas notas que foram retidas pelo tomador, de acordo com a regra abaixo:

 \- Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido ,

recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se

o local da prestação do serviço = município do módulo selecionado OU 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Obs: O arquivo poderá conter quantas retenções forem necessárias, desde que sigam este padrão descrito\. Conforme exemplo demonstrado no documento Exemplo do Lay\-Out Escrituração Tomador\.pdf

Os itens de serviço serão consolidados pelos campos do layout:

\- Aliquota da tag <nota\_retencao>

\- Atividade\_desenvolvida da tag <nota\_retencao>

\- numero\_serviço da tag  <nota\_retencao> 

__OS3627__

__MFS78506__

__RN46\.a__

__Regra geral p/ recuperar serviços tomados \(específico para município de SÃO LEOPOLDO\)__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou \(cód\_class\_doc\_fis = ‘9’ e tipo do documento = “RPA”\)
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Notas não canceladas \(situacao <> ‘S’\)

__\[MFS46567\]__ Inclusão da regra para desconsiderar as notas quando o prestador for do Municipio de São Leopoldo

- Não selecionar os documentos fiscais desse município quando o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal __E__ \(o campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S” referente ao tipo de documento da nota fiscal\)\.

Obs: O arquivo poderá conter quantas retenções forem necessárias, desde que sigam este padrão descrito\. Conforme exemplo demonstrado no documento Exemplo do Lay\-Out Escrituração Tomador\.pdf

Os itens de serviço serão consolidados pelos campos do layout:

\- Aliquota da tag <nota\_retencao>

\- Atividade\_desenvolvida da tag <nota\_retencao>

\- numero\_serviço da tag  <nota\_retencao> 

__CH18086\_2016__

__MFS46567__

__RN47__

__Regra p/ tag <declaração>__

Essa tag indica o início da Declaração

__OS3627__

__RN48__

__Regra p/ tag <retencao__

Início da declaração para determinado contribuinte

__OS3627__

__RN49__

__Regra p/ o campo cpfcnpj da tag <retencao>__

Preencher com o campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento escolhido\. Tamanho máximo: 14 caracteres\.

__OS3627__

__RN50__

__Regra p/ tag <info\_retencao__

Início das informações da retenção, indica a competência, pode\-se ter mais de uma por declaração

__OS3627__

__RN51__

__Regra p/ o campo data\_informacao da tag <info\_retencao>__

Preencher com o campo DT\_PAGTO\_NF da tabela DWT\_DOCTO\_FISCAL\. Tamanho máximo: 10 caracteres\.

__OS3627__

__RN51\.a__

__Regra p/ o campo data\_informacao da tag <info\_retencao> \(específico para município de SÃO LEOPOLDO\)__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. Tamanho máximo: 10 caracteres\.

__MFS46569__

__RN52__

__Regra p/ o campo exercicio da tag <info\_retencao>__

Preencher com o ano campo Data Inicial da tela de geração\. Formato: AAAA\. Tamanho máximo: 4 caracteres\.

__OS3627__

__RN53__

__Regra p/ o campo mes da tag <info\_retencao>__

Preencher com o mes campo Data Inicial da tela de geração\. Formato: MM\. Tamanho máximo: 2 caracteres\.

__OS3627__

__RN54__

__Regra p/ o campo observacao da tag <info\_retencao>__

Preencher com brancos\. Tamanho máximo: 300 caracteres\.

__OS3627__

__RN55__

__Regra p/ o campo aplicacao da tag <info\_retencao>__

Preencher com “N”\. Tamanho máximo: 1 caractere\.

__OS3627__

__RN56__

__Regra p/ tag <nota\_retencao__

Início das informações sobre as notas fiscais retidas na competência

__OS3627__

__RN57__

__Regra p/ o campo data\_emissao da tag < nota\_retencao>__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. Tamanho máximo: 10 caracteres\.

__OS3627__

__RN58__

__Regra p/ o campo modelo da tag < nota\_retencao >__

Preencher com o campo Modelo da tela Parâmetros por Município – Parâmetros – Modelo Msaf x Modelo referente ao modelo cadastrado na nota fiscal\. Tamanho máximo: 2 caracteres\.

__OS3627__

__RN59__

__Regra p/ o campo numero da tag < nota\_retencao >__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. Tamanho máximo: 10 caracteres\.

Se o tamanho da nota fiscal no mastersaf for maior que o tamanho especificado por este layout, deve ser exibida a seguinte mensagem: “O tamanho da nota fiscal é maior que o especificado pelo layout\. Favor verificar”

__OS3627__

__RN60__

__Regra p/ o campo serie da tag <nota\_retencao >__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. Tamanho máximo: 2 caracteres\.

Se o tamanho da série no mastersaf for maior que o tamanho especificado por este layout, a geração deve ser exibir a seguinte mensagem: “O tamanho da série é maior que o especificado pelo layout\. Favor verificar”

__OS3627__

__RN61__

__Regra p/ o campo cpfcnpj\_prestador da tag <nota\_retencao >__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\. Tamanho máximo: 14 caracteres\.

__OS3627__

__RN62__

__Regra p/ o campo descrição\_atividade da tag <nota\_retencao>__

Preencher com o campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na nota fiscal\. Tamanho máximo: 200 caracteres\.

__OS3627__

__RN63__

__Regra p/ o campo atividade\_desenvolvida da tag <nota\_retencao>__

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na nota fiscal\. Sem zeros a esquerda e sem ponto\. Tamanho máximo: 6 caracteres\.

__OS3627__

__RN64__

__Regra p/ o campo numero\_servico da tag <nota>__

   Preencher com o campo serviço da tela Parâmetros por Município – Parâmetros – Serviços Msaf x Serviços referente ao serviço cadastrado na nota fiscal\. Tamanho máximo: 2 caracteres\.

Se não houver parametrização para o serviço cadastrado na nota fiscal, deve ser exibida a seguinte mensagem: “O serviço não foi parametrizado na tela Parâmetros por Município – Parâmetros – Serviço Msaf x Serviço\. Favor verificar”

__OS3627__

__RN64a__

__Regra p/ o campo numero\_servico da tag <nota>__

__Se__ município igual a Esteio __e__ São Leopoldo __então__

   __Se__ tipo de retenção = 1 \(Tomador\) e Estado da X04\_PESSOA\_FIS\_JUR  = 'EX' \(Exterior\) __Então__

          33

       __Senão se__ pCursor\.Ind\_Classe\_Pfj in \('10', '11'\) __e__ Estado do Estabelecimento <> Estado da PFJ ou Municipio do estabelecimento  <>  Municipio da PFJ __Então__

          28

       __Senão se __tipo de retenção = 2 \(Prestador\) __e__ VLR\_RETIDO\_ISS da tabela DWT\_ITENS\_SERV > 0 __e__ Estado do Estabelecimento <> Estado da PFJ ou Municipio do estabelecimento  <>  Municipio da PFJ __Então__

          24

       __Senão se__ tipo de retenção = 1 \(Tomador\) __e__ VLR\_RETIDO\_ISS da tabela DWT\_ITENS\_SERV > 0 __e__ Estado do Estabelecimento <> Estado da PFJ ou Municipio do estabelecimento  <>  Municipio da PFJ __Então__

          23

       __Senão se__ tipo de retenção = 2 \(Prestador\) __e__ Estado do Estabelecimento <> Estado da PFJ ou Municipio do estabelecimento  <>  Municipio da PFJ __Então__

          22

       __Senão se__ tipo de retenção = 1 \(Tomador\) __e__ Estado do Estabelecimento <> Estado da PFJ ou Municipio do estabelecimento  <>  Municipio da PFJ __Então__

          21

       __Senão se__ pCursor\.Ind\_Classe\_Pfj in \('10', '11'\) __e__ Estado do Estabelecimento = Estado da PFJ __e__ Municipio do estabelecimento  =  Municipio da PFJ __Então__

          18

       __Senão se__ tipo de retenção = 2 \(Prestador\) __e__ Estado do Estabelecimento = Estado da PFJ __e__ Municipio do estabelecimento  =  Municipio da PFJ __Então__

          12

       __Senão se__ tipo de retenção = 1 \(Tomador\) __e__ Estado do Estabelecimento = Estado da PFJ __e__ Municipio do estabelecimento  =  Municipio da PFJ __Então__

         11 

Deverá ser exibida a seguinte mensagem:

O Serviço <Campo Cod\_Servico preenchido na SAFX09> selecionado no documento não atende aos critérios necessários para o preenchimento do campo NUMERO\_SERVICO\. Favor verificar\.

__MFS792030__

__RN65__

__Regra p/ o campo valor\_bruto da tag <nota\_retencao>__

Preencher com o somatório do  campo VLR\_TOT da tabela DWT\_ITENS\_SERV\. Tamanho máximo: 15 caracteres\.

__OS3627__

__RN66__

__Regra p/ o campo valor\_deducao da tag <nota\_retencao>__

Preencher com o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV\. Tamanho máximo: 15 caracteres\.

__OS3627__

<a id="_Hlk215996084"></a>__RN67__

__Regra p/ o campo __<a id="_Hlk215995514"></a>__valor\_tributável da tag <nota\_retencao__

Preencher com o somatório do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. 

Se o campo VLR\_TRIBUTO\_ISS não estiver preenchido ou estiver com zeros, então

Preencher com o somatório do campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV\. 

Se o campo VLR\_BASE\_ISS\_1 não estiver preenchido ou estiver com zeros, então

          Preencher com a somatória do campo VLR\_BASE\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\.

Tamanho máximo: 15 caracteres\.

__OS3627__

__MFS\-992587__

__RN67\.a__

__Regra p/ o campo valor\_tributável da tag <nota\_retencao> específico para município de SÃO LEOPOLDO__

Preencher com o somatório do campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV\. 

Tamanho máximo: 15 caracteres\.

__MFS46564__

__MFS1023036__

<a id="_Hlk215996098"></a>__RN68__

__Regra p/ o campo alíquota da tag <nota\_retencao> __

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. 

Se o campo ALIQ\_TRIBUTO\_ISS não estiver preenchido ou estiver com zeros, então

     Preencher com o campo VLR\_ALIQ\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV\.

Tamanho máximo: 10 caracteres\.

__OS3627__

__MFS\-992587__

__RN69__

__Regra p/ o campo valor\_retido da tag <nota\_retencao>__

Preencher com o campo VLR\_RETIDO\_ISS da tabela DWT\_ITENS\_SERV\. Tamanho máximo: 15 caracteres\.

__OS3627__

__RN69\.a__

__Regra p/ o campo valor\_retido da tag <nota\_retencao> \(específico para município de Passo Fundo\)__

__\[MFS80058\]__

Preencher com o campo VLR\_RETIDO\_ISS da tabela DWT\_ITENS\_SERV\.

  __Se__ o campo VLR\_ISS\_RETIDO não estiver preenchido ou preenchido com zeros

__Preencher__ com o valor do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. 

Tamanho máximo: 15 caracteres\.

__MFS80058__

__RN70__

__Regra p/ tag </nota\_retencao>__

Indica o fechamento das informações da nota

__OS3627__

__RN71__

__Regra p/ tag </info\_retencao>__

Indica o fechamento das informações da retenção

__OS3627__

__RN72__

__Regra p/ tag </retencao>__

Indica o fechamento da declaração da retenção

__OS3627__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


# MTZ_SUPERNOVA_Cadastro_Prestadores_Tomadores_Eventuais

- **Fonte:** MTZ_SUPERNOVA_Cadastro_Prestadores_Tomadores_Eventuais.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 79 KB

---

THOMSON REUTERS

Geração do Meio Magnético 

Cadastro de Prestadores/Tomadores Eventuais

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS3966

ISS Nova Lima – Criação de Nova Geração\.

Será criada uma nova geração dentro do menu de obrigações do módulo “Nova Lima”, permitirá a criação do meio magnético que exibirá os dados do cadastro dos prestadores/tomadores de serviços para o período e estabelecimento selecionados nos parâmetros\.

MFS4206

DW \- MUNICIPAL \- SUPERNOVA – Inclusão de novo município\.

Este documento tem como objetivo incluir o município de Santa Luzia/MG para ser atendido pelo validador SuperNova\.

MFS8132

DW \- MUNICIPAL \- SUPERNOVA – Inclusão de novo município\.

Este documento tem como objetivo incluir o município de Sabará/MG para ser atendido pelo validador SuperNova\.

MFS16576

DW \- MUNICIPAL \- SUPERNOVA – Inclusão de novo município\.

Este documento tem como objetivo incluir o município de Cabo Frio/RJ para ser atendido pelo validador SuperNova\.

MFS19797

DW \- MUNICIPAL \- SUPERNOVA – Inclusão de novo município\.

Este documento tem como objetivo incluir o município de Conselheiro Lafaiete e Itabirito/MG para ser atendido pelo validador SuperNova\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MSF/CH__

__RN00__

__Regra para geração do Meio Magnético:__

A geração do meio magnético deve ser feita no Framework\. Caso o usuário selecione mais de um estabelecimento na geração, o sistema irá gerar um arquivo para cada estabelecimento\.

__MFS3966__

__RN01__

__Regra do campo Data Inicial: Tela Obrigações – Geração Meio Magnético__

O campo deve ser um text Box com a seguinte __máscara: DD/MM/AAAA__\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE \(data mais atual\)\.

__MFS3966__

__RN02__

__Regra do campo Data Final: Tela Obrigações – Geração Meio Magnético __

O campo deve ser um text Box com a seguinte __máscara: DD/MM/AAAA__\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE \(data mais atual\)\. 

A Data Final não poderá ser __menor__ que a Data Inicial\. Caso o usuário informe, o sistema deverá exibir a mensagem de aviso: “Data Final digitada não pode ser menor que a Data Inicial informada”\.                                  

__MFS3966__

__RN03__

__Regra do campo Tipo do Arquivo da tela de Obrigações – Geração Meio Magnético__

- O campo deve ser um __RadioButton__ com as opções: __Produção __e __Teste__\.
- Por padrão, trazer selecionado __‘Produção’__\.
- Somente um poderá ser selecionado\.

__MFS3966__

__RN04__

__Regra do campo Prestador/Tomador da tela de Obrigações – Geração Meio Magnético__

- O campo deve ser um __RadioButton__ com as opções:__ Movimentados no Período __e__ Novos Prestadores__
- Por padrão, trazer selecionado __‘Movimentados no Período’__\.
- Somente um poderá ser selecionado\.

__MFS3966__

__RN05__

__Regra do campo Sequencial de Arquivo:__

O campo deve permitir que o usuário digite o sequencial desejado, com no máximo 5 posições\. 

Este campo é de preenchimento __obrigatório__\. Caso o usuário não informe valor para este campo, o sistema deverá exibir a mensagem de preenchimento obrigatório\.

__MFS3966__

__RN06__

__Regra do campo Número do Arquivo:__

O campo deve permitir que o usuário digite o número do arquivo desejado, com no máximo 6 posições\.

Este campo é de preenchimento __obrigatório__\. Caso o usuário não informe valor para este campo, o sistema deverá exibir a mensagem de preenchimento obrigatório\.

__MFS3966__

__RN07__

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

__RN08__

__Regra para abas existentes na geração do meio magnético:__

Após processar o meio magnético devem ser exibidas as abas “Log”, “Arquivo”, “Processos” e “Relatório”\. 

A aba “Arquivo” deve exibir o arquivo que poderá ser salvo localmente\.

A aba “Log” deve exibir a mensagem “Processo concluído com sucesso” quando o arquivo for gerado corretamente, caso contrário exibir a mensagem “Processo concluído com erros”\.

__MFS3966__

__RN09__

__Regra p/ nomenclatura do arquivo magnético:__

O nome do arquivo deverá ser composto obrigatoriamente da regra:

EVEN<Inscr\. Municipal \(sem máscara\)>\_<AAAAMMDD>\_<Recuperar o campo digitado na tela de geração “Número do arquivo”>\.REM   

Exemplos:         EVEN10350056\_20080805\_01\.REM

		EVEN30225586\_20080704\_01\.REM

		EVEN30225586\_20080704\_02\.REM \(este exemplo indica que dois arquivos forma transmitidos no mesmo dia\)\.

__MFS3966__

__RG00__

__Regras Gerais para geração do Meio Magnético:__

O primeiro registro deve ser obrigatoriamente, um registro do tipo “0”\. Este registro deverá ser único no arquivo\.

Campos numéricos do __\(Tipo 9\)__ devem ser alinhados à DIREITA, preenchidos com zeros à esquerda, devendo completar com zeros as posições não preenchidas\. Nos campos não deverão ser inseridos os caracteres vírgula ou ponto\. Ex: Campo Numérico \(10\) cujo valor seja 45222,00 deverá ser formatado = 0004522200\.

Campos alfanuméricos __\(Tipo X\)__ devem ser alinhados à ESQUERDA e preenchidos com espaços à direita\.

Campos do __\(Tipo Data\)__ devem ser preenchidos no formato DDMMAAAA \(DD = dia, MM = mês e AAAA = ano\)\.

Todos os campos deverão obedecer rigorosamente o tamanho e a formatação definidos pelo layout\.

__MFS3966__

__RN10__

__Header \(Remessa/Retorno\):__

__Regras para o preenchimento do campo 01 \-‘ Identificador do Header’:__

- Deverá ser informado o caractere fixo ‘0’\.
- Campo obrigatório\.

__MFS3966__

__RN11__

__Regras para o preenchimento do campo 02 – ‘Data de Geração do Arquivo’:__

- Recuperar a data de geração do Meio Magnético\.
- Campo obrigatório\.

__MFS3966__

__RN12__

__Regras para o preenchimento do campo 03 – ‘Inscrição Municipal do Contribuinte’:__

- Recuperar a informação do campo INSCR\_MUNICIPAL da tabela ESTABELECIMENTO, referente ao estabelecimento selecionado na tela de geração\.
- Campo obrigatório\. 

__MFS3966__

__RN13__

__Regras para o preenchimento do campo 04 – ‘CNPJ/CPF do Contribuinte’:__

- Recuperar o campo CGC na tabela ESTABELECIMENTO referente ao estabelecimento selecionado na tela de geração\.
- Campo obrigatório\. 

__MFS3966__

__RN14__

__Regras para o preenchimento do campo 05 – ‘Nome do Contribuinte’:__

- Recuperar o campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO para o estabelecimento selecionado na tela de geração\.
- Campo obrigatório\.

__MFS3966__

__RN15__

__Regra para o preenchimento do campo 06 – ‘Sequencial de Arquivo’:__

- Deve recuperar a informação digitada na tela de geração, campo __‘Sequencial de Arquivo’__\. Sequencial numérico por arquivo gerado, preenchido com zeros à esquerda, exemplo: ‘00001’ \(00001, 00002,\.\.\.\)\.

__MFS3966__

__RN16__

__Regra para o preenchimento do campo 07 – ‘Versão do Arquivo’:__

- Preencher com ‘0100’\. 

__MFS3966__

__RN17__

__Regras para o preenchimento do campo 08 – ‘Arquivo Produção ou Teste:__

- Recuperar a informação do parâmetro Tipo Arquivo informado na tela de Geração do Meio Magnético\. Seguindo a seguinte regra:

__   P – Produção__

__   T – Teste __

- Campo obrigatório

__MFS3966__

__RN18__

__Regra para o preenchimento do campo 09 – ‘Nome do Sistema’:__

- Preencher com ‘ISSDigital’\.  

\.

__MFS3966__

__RN19__

__Regra para o preenchimento do campo 10 – ‘Brancos’:__

- Preencher com Brancos\.  

__MFS3966__

__RN20__

__Regra para o preenchimento do campo 11 – ‘Sequencial de Registro’:__

- Preencher com 00001

__MFS3966__

__RN21__

__Trailer \(Remessa/Retorno\): __

__Regras para o preenchimento do campo 01 – ‘Identificador do Trailer’:__

- Preencher com 9\.
- O campo é obrigatório

__MFS3966__

__RN22__

__Regra para o preenchimento do campo 02 – ‘Brancos’:__

- Preencher com Brancos

__MFS3966__

__RN23__

__Regras para o preenchimento do campo 03 – ‘Sequencial de Registro’:__

- O trailer terá por sequencial o total de numero de linhas do arquivo\.  

__MFS3966__

__RN24__

__Regras para Recuperação dos Registros:__

- <a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>Se o parâmetro Prestador/Tomador da tela de geração estiver com a opção “Movimentados no Período” marcada, considerar o cadastro da pessoa física/ jurídica \(tabela SAFX04\) quando houver movimentação de documento fiscal, verificando os seguintes pontos:
- <a id="OLE_LINK11"></a><a id="OLE_LINK12"></a><a id="OLE_LINK13"></a>Nota fiscal de entrada, exceto cancelada, que seja de classificação fiscal 2 e 3 e a data <a id="OLE_LINK17"></a><a id="OLE_LINK18"></a><a id="OLE_LINK19"></a><a id="OLE_LINK20"></a>fiscal esteja dentro do período informado na tela de geração \(tabela SAFX07\);
- <a id="OLE_LINK21"></a><a id="OLE_LINK22"></a><a id="OLE_LINK23"></a>Considerar apenas o Estabelecimento informado na tela de geração;
- <a id="OLE_LINK9"></a><a id="OLE_LINK10"></a>Será recuperado apenas o cadastro da pessoa física/jurídica cujo município do prestador seja diferente de Nova Lima \(tabela SAFX04\)\.
- Se o parâmetro Prestador/Tomador da tela de geração estiver com a opção “Novo Prestador” marcada, considerar o cadastro da pessoa física/ jurídica \(tabela SAFX04\), verificando os seguinte ponto:
- Será recuperado apenas o cadastro da pessoa física/jurídica cujo município do prestador seja diferente de Nova Lima e a data início da prestação de serviço esteja preenchida  dentro  do período informado na tela de geração \(tabela SAFX04\)\.

__*Atenção: *__Considerar cadastro de maior validade\.

__MFS3966__

__RN25__

__Detalhe \(Remessa/Retorno\) = Escrituração:__

__Regra para o preenchimento do campo 01 – ‘Identificador de Detalhe’:__

- Preencher com 1\.
- O campo é obrigatório

__MFS3966__

__RN26__

__Regra para o preenchimento do campo 02 – ‘CNPJ/CPF do Prestador/Tomador’:__

- Recuperar a informação do campo CPF\_CGC __\(campo 06\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__ Deve conter __11 \(para CPF\) ou 14 \(para CNPJ\)\.__
- Campo obrigatório\.

__MFS3966__

__RN27__

__Regra para o preenchimento do campo 03 – ‘Nome/Razão Social’: __

- Recuperar a informação dos campos: RAZAO\_SOCIAL __\(Campo 05\)__ da tabela __X04\_PESSOA\_FIS\_JUR\. __
- Campo obrigatório\.

__MFS3966__

__RN28__

__Regra para o preenchimento do campo 04 – ‘Tipo do Logradouro’: __

- Recuperar a informação do campo TP\_LOGRADOURO __\(campo 42\)__ da tabela __X04\_PESSOA\_FIS\_JUR, __pegar as 03 primeiras posições\. 

Exemplos tipos de Logradouro: RUA, AVN, PÇA, ROD, etc\.

- Campo obrigatório\.

__MFS3966__

__RN29__

__Regra para o preenchimento do campo 05 – ‘Nome do Logradouro’:__

- Recuperar a informação do campo ENDERECO __\(campo 12\)__ da tabela __X04\_PESSOA\_FIS\_JUR__ 
- Campo obrigatório\.

__MFS3966__

__RN30__

__Regra para o preenchimento do campo 06 – ‘Número’: __

- Recuperar a informação do campo NUM\_ENDERECO __\(campo 13\)__ da tabela __X04\_PESSOA\_FIS\_JUR, __pegar as 06 primeiras posições\. 
- Campo obrigatório\.

__MFS3966__

__RN31__

__Regra para o preenchimento do campo 07 – ‘Complemento’: __

- Recuperar a informação do campo COMPL\_ENDERECO __\(campo 14\)__ da tabela __X04\_PESSOA\_FIS\_JUR__ 
- Campo obrigatório\.

__MFS3966__

__RN32__

__Regra para o preenchimento do campo 08 – ‘Nome do Bairro’: __

- Recuperar a informação do campo BAIRRO __\(campo 15\)__ da tabela __X04\_PESSOA\_FIS\_JUR__
- Campo obrigatório\. 

__MFS3966__

__RN33__

__Regra para o preenchimento do campo 09 – ‘CEP’: __

- Recuperar a informação do campo CEP __\(campo 20\)__ da tabela __X04\_PESSOA\_FIS\_JUR__ 
- Campo obrigatório\.

__MFS3966__

__RN34__

__Regra para o preenchimento do campo 10 – ‘Cidade’:__

- Recuperar a informação do campo CIDADE __\(campo 16\)__ da tabela __X04\_PESSOA\_FIS\_JUR__ 
- Campo obrigatório\.

__MFS3966__

__RN35__

__Regra para o preenchimento do campo 11 – ‘Estado’:__

- Recuperar a informação do campo UF __\(campo 19\)__ da tabela __X04\_PESSOA\_FIS\_JUR__ 
- Campo obrigatório\.

__MFS3966__

__RN36__

__Regra para o preenchimento do campo 12 – ‘País’:__

- Recuperar a informação do campo PAIS\_DESC da tabela PAISES de acordo com o campo COD\_PAIS __\(campo 21\)__ da tabela __X04\_PESSOA\_FIS\_JUR__ 
- Campo obrigatório\.

__MFS3966__

__RN37__

__Regra para o preenchimento do campo 13 – ‘Telefone’:__

- Recuperar a informação do campo TELEFONE __\(campo 23\)__ da tabela __X04\_PESSOA\_FIS\_JUR__ 
- Campo obrigatório\.

__MFS3966__

__RN38__

__Regra para o preenchimento do campo 14 – ‘Enquadramento como Simples Nacional’:__

- Recuperar a informação do campo IND\_SIMPLES\_NAC __\(campo 43\)__ da tabela __X04\_PESSOA\_FIS\_JUR__ 

As opções para esse campo são S = ‘Sim’ e N = ‘Não’\. 

- Campo obrigatório\.

__MFS3966__

__RN39__

__Regra para o preenchimento do campo 15 – ‘Atividade cadastrada na Prefeitura’:__

- Quando Enquadramento = __Tomador__

Recuperar a informação do campo COD\_ATIVIDADE __\(Campo 07\)__ da tabela X04\_PESSOA\_FIS\_JUR\.

- Considerar os dois últimos digitos do COD\_ATIVIDADE como subclasse, preenchendo o tamanho conforme regra abaixo, considerar os outros digitos como classe, preenchendo o tamanho conforme formato descrito abaixo \(regra E1 do layout\)\.

__Formato:__ Atividade cadastrada na prefeitura composta de duas partes: Classe e SubClasse\. Sendo assim o preenchimento ficará da seguinte forma: CCCCCSSSS = 5 dígitos ref\. à Classe \+ 4 dígitos ref\. à SubClasse, devendo ambos serem preenchidos com ‘zeros’ à esquerda caso não se complete o campo\.

__Exemplo:__

Atividade  236/1          ficará da seguinte forma:  002360001

Atividade  00445/01    ficará da seguinte forma:  004450001

Atividade 99999/0201 ficará da seguinte forma:  999990201

- Campo obrigatório\.

__MFS3966__

__RN40__

__Regra para o preenchimento do campo 16 – ‘Tipo de Empresa’:__

- Preencher fixo “D”\.
- Campo obrigatório\.

*Observação:* Não trataremos no momento Construção Civil para o cadastro\.

__MFS3966__

__RN41__

__Regra para o preenchimento do campo 17 – ‘E\-mail’:__

- Recuperar a informação do campo E\_MAIL __\(campo 40\)__ da tabela __X04\_PESSOA\_FIS\_JUR__ 
- Campo obrigatório\.

__MFS3966__

__RN42__

__Regra para o preenchimento do campo 18– ‘Status \(Retorno\)’:__

- Preencher o campo com espaços em branco

__MFS3966__

__RN43__

__Regra para o preenchimento do campo 19– ‘Mensagem \(Retorno\)’:__

- Preencher o campo com espaços em branco

__MFS3966__

__RN44__

__Regra para o preenchimento do campo 20– ‘Inscrição Eventual atribuída pela Prefeitura \(Retorno\):__

- <a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>Preencher o campo com espaços em branco

__MFS3966__

__RN45__

__Regra para o preenchimento do campo 21– ‘Data de Cadastro \(Retorno\)’:__

- Preencher o campo com espaços em branco

__MFS3966__

__RN46__

__Regra para o preenchimento do campo 22 – ‘Brancos’:__

- Preencher o campo com espaços em branco\.
- Campo Obrigatório\.

__MFS3966__

__RN47__

__Regra para o preenchimento do campo 23 – ‘Sequencial de Registro’:__

- O ‘sequencial de registro’ refere\-se às linhas do arquivo \(aqui considerados como registros\) e não se repete dentro do arquivo\. O Detalhe será, obrigatoriamente, ‘00002’ e assim sucessivamente\.  
- Campo Obrigatório\.

__MFS3966__

 


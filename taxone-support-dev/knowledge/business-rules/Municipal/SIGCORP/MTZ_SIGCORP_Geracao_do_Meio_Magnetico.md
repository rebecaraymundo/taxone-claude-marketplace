# MTZ_SIGCORP_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_SIGCORP_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2025-12-21
- **Tamanho:** 115 KB

---

THOMSON REUTERS

		

Municipal 

 Serviços Prestados 

	Geração do Meio Magnético \- SIGCORP	

##### 	DOCUMENTO DE REQUISITO		

__MFS/CH__

__Nome__

__Descrição__

MFS13248

João Henrique de Araujo\.

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Este documento tem como objetivo tratar a geração do meio magnético de serviços prestados em atendimento ao novo validador SIGCORP\. 

MFS\-35861

Alessandra Cristina Navatta

Esta demanda tem como objetivo incluir o município de Mogi Mirim/ SP na estrutura do validador “SIGCORP”\. 

__Para o Layout de Serviços Prestados:__

Serão atendidos os tipos de registros 1, 2 e 9\. Os registros tipo 1 e 9 obedecem a mesma estrutura e ordem de apresentação das colunas que a do município de Marília \(podendo apenas alterar alguma regra específica de alguma coluna\. Neste caso, estará identificada no respectivo campo e indicado com o número desta demanda \(no campo MFS/CH\)\.

Já o registro de tipo 2, foram incluídos colunas e a ordem de exibição no arquivo magnético, foi alterada \(para o município de Mogi Mirim\), por isso, considerar as regras nos respectivos campos e a ordenação está indicada na tabela criada na RN49\. Caso alguma coluna, tenha alguma regra específica para o município, ela estará contemplada no respectivo campo já criado nos municípios anteriores\.

__Para o Layout de Serviços Tomados__

Criar o layout para o município de Mogi Mirim

__O Layout de serviços tomados não foi desenvolvido\.__

MFS36741

Andréa Rocha

Esta demanda tem como objetivo incluir o município de Pouso Alegre/MG na estrutura do validador “SIGCORP”\. 

MFS46300

Andréa Rocha

Esta demanda tem como objetivo incluir o município de Cabo Frio/RJ na estrutura do validador “SIGCORP”\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MSF/CH__

__RN01__

__Regra para inclusão do módulo no Manager:__

O módulo “Marília” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo:__ “O arquivo consiste na entrega das notas fiscais emitidas pelo contribuinte para os tomadores de serviço referente ao município de Marília”\.__

__MFS13248__

__RN02__

__Regra para abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “29005” \(Marília\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Marília, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS13248__

__RN03__

__Estrutura de menus do módulo:__

- Arquivo
- Obrigações
	- __Geração do Meio Magnético __
- Janela
- Ajuda

__MFS13248__

__MFS\-35861__

__RN04__

__Regra de nomenclatura do arquivo:__

O arquivo será importado pelo SIGISS e deverá seguir a nomenclatura utilizando a codificação da ISSO\-8859\-1 no formato txt\. Conforme exemplo a seguir:

__       NFE\_LOTEAAAAMMDD\.txt__, onde:

       __NFE\_LOTE__: representa a obrigação que está sendo gerada\. 

       __AAAAMMDD__: representa a data inicial da geração do arquivo\.

       __\.txt:__ extensão do arquivo\.

*Exemplo:* NFE\_LOTE20170906\.txt

__MFS13248__

__MFS\-35681__

__RN05__

__Regra dos campos da Tela Obrigações – Geração Meio Magnético:__

__Menu:__  Obrigações >> Geração do Meio Magnético:

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial: __O campo deve ser um text Box com a seguinte __máscara: DD/MM/AAAA__\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE \(data mais atual\)\.

__Data Final: __O campo deve ser um text Box com a seguinte __máscara: DD/MM/AAAA__\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE \(data mais atual\)\. 

A Data Final não poderá ser __menor__ que a Data Inicial\. Caso o usuário informe, o sistema deverá exibir a mensagem de aviso: “Data Final digitada não pode ser menor que a Data Inicial informada”\.                                  

__Identificador Sistema Legado:__ O campo deve ser um text Box\. Não virá com default preenchido, o usuário poderá inserir a informação de acordo com a sua necessidade\. Campo é do tipo alfanumérico com no máximo 12 posições e __não obrigatório__\.

__Estabelecimento:__ O sistema deve exibir os estabelecimentos pertencentes ao município de Gaspar, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__\[MFS36741\] A alíquota do simples nacional vai ser recuperada da nota fiscal__

__Para o Município de Mogi Mirim __

Incluir o campo ‘__Alíquota Simples Nacional__’\.

Este campo deve ser inserido abaixo do campo ‘Identificador Sistema Legado’: O campo deve ser um text Box\. Não virá com default preenchido\. Campo é do tipo numérico de 3 posições e obrigatório__\. __ 

Validações: Se o campo não estiver preenchido, ou se o valor não estiver compreendido entre 200 à 500, exibir a mensagem “O campo Alíquota Simples Nacional é de preenchimento obrigatório e deve estar preenchido com alíquota de 2,00 a 5,00%\. O campo deve ser preenchido sem virgula e com 3 posições”

__MFS13248__

__MFS35681__

__MFS36741__

__RN06__

__Regra para abas existentes na geração do meio magnético:__

Após processar o meio magnético devem ser exibidas as abas “Log”, “Arquivo”, “Processos” e “Relatório”\. 

A aba “Arquivo” deve exibir o arquivo que poderá ser salvo localmente\.

A aba “Log” deve exibir a mensagem “Processo concluído com sucesso” quando o arquivo for gerado corretamente, caso contrário exibir a mensagem “Processo concluído com erros”\.

__MFS13248__

__MFS\-35681__

__RN07__

__Regras para geração do Meio Magnético:__

__Regras referentes à formatação dos registros gerados no meio magnético:__

A seguir formatações de dados que devem ser seguidas para geração do meio magnético na estrutura do arquivo:

O arquivo gerado para importação deve ser no formato __‘txt’\.__

- __Campo Caractere:__ Devem ser alinhados a esquerda\. Preencher com espaços em branco à direita, caso seja necessário\.
- __Campo Numérico:__ Devem ser alinhados a direita\. Preencher com zeros à esquerda caso seja necessário ou não possua valor
- __O arquivo será com colunas delimitadas por tamanho fixo__

__MFS13248__

__MFS\-35681__

__RN08__

__Regra p/ Recuperação das notas fiscais de Serviços Prestados__

Contemplar todas as notas fiscais de serviço com as seguintes particularidades:

- Notas fiscais de saída \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL = 9\);
- Classificação da nota fiscal = 2 ou 3;
- Empresa e estabelecimento escolhidos na tela de geração;
- Data fiscal da nota dentro do período de referência informado na tela de geração;

__MFS13248__

__RN09__

__Registro Tipo 1 Cabeçalho – Regra para o campo Tipo de Registro__

Esse campo indica a linha do cabeçalho\. Preencher com o valor fixo = __“1”__\. 

Campo obrigatório\.

Formato: 9

Tamanho: 1 posição

Tipo: Numérico

__MFS13248__

__RN10__

__Registro Tipo 1 Cabeçalho – Regra para o campo Tipo do Arquivo__

Esse campo referencia o tipo do arquivo\. Preencher com o valor fixo = __“NFE\_LOTE”__\. 

__Observação: __Apesar de o campo possuir 12 posições, o catálogo de erro do manual layout informa que deve ser preenchido com o valor fixo\.

Campo obrigatório\.

Formato: XXXXXXXXXXXX

Tamanho: 12 posições

Tipo: Texto 

__MFS13248__

__RN11__

__Registro Tipo 1 Cabeçalho – Regra para o campo Inscrição do Prestador__

Esse campo indica a inscrição Municipal do Prestador\. Preencher com a informação do campo INSC\_MUNICIPAL __\(campo 09 da tabela SAFX04\)__

Campo obrigatório\.

Formato: 99999999

Tamanho: 8 posições

Tipo: Numérico

__Município de Mogi Mirim, Pouso Alegre e Cabo Frio__

Considerar a mesma regra, porém o tamanho de 15 posições\.

__MFS13248__

__MFS\-35861__

__MFS36741__

__MFS46300__

__RN12__

__Registro Tipo 1 Cabeçalho – Regra para o campo Versão do Arquivo__

Esse campo indica a versão do layout a ser gerado\. Preencher com o valor fixo = __“010”__\. 

Campo obrigatório\.

Formato: 999

Tamanho: 3 posições

Tipo: Numérico

__Município de Mogi Mirim, Pouso Alegre e Cabo Frio__

Preencher com o valor fixo = ‘030’

__MFS13248__

__MFS\-35861__

__MFS36741__

__MFS46300__

__RN13__

__Registro Tipo 1 Cabeçalho – Regra para o campo Data do Arquivo__

Esse campo a data em que o arquivo foi gerado\. Preencher com a Data Inicial da tela de geração do meio magnético\.

Campo obrigatório\.

Formato: AAAAMMDD

Tamanho: 8 posições

Tipo: Data

__MFS13248__

__RN14__

__Registro Tipo 1 Cabeçalho – Regra para o campo Caractere de Fim de linha__

Esse campo representa o fim da linha \(Chr\(13\) \+ Chr\(10\)\) – Fim da linha e Retorno para uma nova linha\.

__MFS13248__

__RN15__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Tipo de Registro__

Esse campo indica a informação da Nota Fiscal\. Preencher com o valor fixo = __“2”__\. 

Campo obrigatório\.

Formato: 9

Tamanho: 1 posição

Tipo: Numérico

__MFS13248__

__RN16__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Identificador Sistema Legado__

Esse campo será preenchido com a informação inserida pelo usuário na tela de parametrização da geração do arquivo magnético, caso ele possua um sistema legado e queira informar o número da nota naquele sistema\.

Formato: XXXXXXXXXXXX

Tamanho: 12 posições

Tipo: Alfanumérico 

__MFS13248__

__RN17__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Tipo de codificação__

Esse campo indica o tipo de codificação utilizada para descrever o serviço\. Preencher com o valor fixo = __“1”__\. 

Campo obrigatório\.

Formato: 9

Tamanho: 1 posição

Tipo: Numérico

__MFS13248__

__RN18__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Código do serviço__

Esse campo indica o código do serviço na Nota Fiscal\. Preencher com o campo __COD\_SERV\_LEI\_116__ da tabela __DWT\_SERVICO\_LEI\_116__ referente ao serviço cadastrado no item da nota fiscal\.

__Tratamentos:__

Se o campo não estiver preenchido, no log do sistema deve ser exibida a mensagem: “O código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal não está preenchido, favor verificar”\.

Nossa tabela permite gravar o tamanho de 4 posições, então para atender a obrigação deverão ser incluídos zeros a esquerda do código lei serviço, ou seja, o código 0704 deverá gravar “0000704”

*Exemplos: *0101 deverá ficar ‘0000101”

                1415 deverá ficar “0001415”

Campo obrigatório\.

Formato: 9999999

Tamanho: 7 posições

Tipo: Numérico

__MFS13248__

__RN19__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Situação da Nota Fiscal__

Esse campo indica a situação da Nota Fiscal\. 

Preencher com:

__“C”__ – Cancelada: 

Se na nota fiscal o campo __SITUACAO__ da __SAFX07__ estiver preenchido com __“S”\.__

__“R”__ – Retida: 

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “2" e se o local da prestação do serviço = município do módulo selecionado __OU__ 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado __OU__

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

__“U”__ – Imune: 

Se o campo __IND\_ISS__ da tabela ESTABELECIMENTO = __“01”__, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”\.__ __

__“I”__ – Isenta: 

Se o campo __IND\_ISS__ da tabela ESTABELECIMENTO = __“04”__, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433”\.

__“N” __– Não Tributada: 

Se o campo __IND\_ISS__ da tabela ESTABELECIMENTO = __“09”__, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “444”\.

__“T__”– Tributada: 

Caso nenhuma das opções acima seja verdadeira\.

Campo obrigatório\.

Formato: X

Tamanho: 1 posição

Tipo: Caractere 

__Para o município de Mogi Mirim__

__Lista de Valores Válidas:__

T = Tributada; R = Retida; C = Cancelada; I = Isenta; N = Não Tributada; U = Imune; F = Não Tributado – Retido

__F = Não Tributado – Retido__

Se as condições “N” e “R” forem atendidas simultaneamente, considerar “F”\. Caso contrário, considerar as opções “N” ou “R”\.

__MFS13248__

__MFS\-35861__

__RN20__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Valor dos serviços__

Esse campo indica o valor do serviço\. Preencher com a informação do campo __VLR\_TOT__ da tabela __DWT\_ITENS\_SERV \(Campo 15 da SAFX09\)__\.

__Tratamentos:__            

Se o campo exceder o número de caracteres permitido ou não estiver preenchido, emitir a mensagem de log: “O campo Valor dos serviços está com tamanho acima do máximo permitido \(15 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar”\. Esse campo deverá ser informado sem pontos ou vírgula\. 

Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*Exemplos:* Para o valor de 100,55 deverá ser informado “000000000010055”

                  Para o valor de 123456789123456,45 deverá ser informado “345678912345645”\.

Campo obrigatório\.

Formato: 999999999999999

Tamanho: 15 posições

Tipo: Numérico

__MFS13248__

__RN21__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Valor da base de cálculo__

Esse campo indica o valor da base de cálculo\. Preencher com o somatório do campo __VLR\_BASE\_ISS\_1 OU VLR\_BASE\_ISS\_2__ da tabela __DWT\_ITENS\_SERV__\.

__Observação:__ No item da NF não permite o preenchimento das duas bases, ou seja, será preenchida uma ou outra\.

__Tratamentos:__            

Se o campo exceder o número de caracteres permitido ou não estiver preenchido, emitir a mensagem de log: “O campo Valor da base de cálculo está com tamanho acima do máximo permitido \(15 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar”\. Esse campo deverá ser informado sem pontos ou vírgula\. 

Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*Exemplos:* Para o valor de 100,55 deverá ser informado “000000000010055”

                  Para o valor de 123456789123456,45 deverá ser informado “345678912345645”\.

Campo obrigatório\.

Formato: 999999999999999

Tamanho: 15 posições

Tipo: Numérico

__Para o município de Mogi Mirim:__

Este campo não é de preenchimento obrigatório, caso não exista, preencher com zeros\.

__MFS13248__

__RN22__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo CPF/CNPJ do tomador__

Esse campo indica o CPF/CNPJ do tomador de serviços\. Preencher com a informação do campo CPF/__CGC__ da tabela __de Cadastro de Pessoas Físicas/Jurídicas\.__

Campo Obrigatório

Formato: CNPJ: 99999999999999 

Tamanho: 14 posições

Tipo: Alfanumérico

__Município de Mogi Mirim, Pouso Alegre e Cabo Frio__

Tamanho 15 posições

Este campo é o de número 16 do layout do município de Mogi Mirim,__ Pouso Alegre e Cabo Frio__

__MFS13248__

__MFS\-35681__

__MFS36741__

__MFS46300__

__RN23__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Inscrição municipal do tomador__

Esse campo indica a inscrição municipal do tomador de serviços\. Preencher com a informação __INSC\_MUNICIPAL__ da tabela__ de Cadastro de Pessoas Físicas/Jurídicas__

Formato: 99999999

Tamanho: 8 posições

Tipo: Numérico

__Município de Mogi Mirim, Pouso Alegre e Cabo Frio __ 

Tamanho 15 posições

Campo Opcional

Se não preenchido, gerar em branco\.

Este campo é o de número 17 do layout do município de Mogi Mirim,__ Pouso Alegre e Cabo Frio __\.

__MFS13248__

__MFS\-35681__

__MFS36741__

__MFS46300__

__RN24__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Inscrição estadual do tomador__

Esse campo indica a inscrição estadual do tomador de serviços\. Preencher com a informação do campo __INSCRIÇÃO ESTADUAL__ de Cadastro de Pessoas Físicas/Jurídicas__ __

Formato: 99999999

Tamanho: 8 posições

Tipo: Numérico

__Município de Mogi Mirim, Pouso Alegre e Cabo Frio__

Tamanho 15 posições

Campo Opcional

Se não preenchido, gerar em branco\.

Este campo é o de número 18 do layout do município de Mogi Miri,__ Pouso Alegre e Cabo Frio__

__MFS13248__

__MFS\-35681__

__MFS36741__

__MFS46300__

__RN25__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Nome/Razão social do tomador__

Esse campo indica a razão social do tomador de serviços\. Preencher com a informação __RAZAO\_SOCIAL__ da __tabela de Cadastro de Pessoas Físicas/Jurídicas__

Campo obrigatório

Formato: XXXXXX\.\.\.\./

Tamanho: 100 posições

Tipo: Texto

__Para o município de Mogi Mirim, Pouso Alegre e Cabo Frio__ 

Este campo será ignorado \(pelo validador\) caso seja fornecido um CPF / CNPJ ou inscrição do tomador que esteja no cadastro mobiliário deste Município\.

Este campo é o de número 19 do layout do Município de Mogi Mirim, __Pouso Alegre e Cabo Frio__\.

__MFS13248__

__MFS\-35861__

__MFS36741__

__MFS46300__

__RN26__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Endereço do tomador__

Esse campo indica o endereço do tomador de serviços\. Preencher com a informação __ENDERECO__ da tabela __de Cadastro de Pessoas Físicas/Jurídicas__

__Tratamento:__            

Se o campo não estiver preenchido, emitir a mensagem de log: “O campo Endereço não está preenchido\. Campo de preenchimento obrigatório, favor verificar”\. 

Campo Obrigatório

Formato: XXXXXX\.\.\.\./

Tamanho: 50 posições

Tipo: Texto

__Para o município de Mogi Mirim, Pouso Alegre e Cabo Frio__

Este campo será ignorado \(pelo validador\) caso seja fornecido um CPF / CNPJ ou inscrição do tomador que esteja no cadastro mobiliário deste Município\. 

Este campo é o de número 20 do layout do Município de Mogi Mirim, __Pouso Alegre e Cabo Frio __

__MFS13248__

__MFS\-35861__

__MFS36741__

__MFS46300__

__RN27__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Numero do endereço__

Esse campo indica o número do endereço do tomador de serviços\. Preencher com a informação __NUM\_ENDERECO__ da tabela __de Cadastro de Pessoas Físicas/Jurídicas__

__Tratamento:__            

Se o campo não estiver preenchido, emitir a mensagem de log: “O campo Número do endereço não está preenchido\. Campo de preenchimento obrigatório, favor verificar”\. 

Campo Obrigatório

Formato: XXXXXX\.\.\.\./

Tamanho: 10 posições

Tipo: Texto

__Para o município de Mogi Mirim, Pouso Alegre e Cabo Frio__ 

Este campo será ignorado \(pelo validador\) caso seja fornecido um CPF / CNPJ ou inscrição do tomador que esteja no cadastro mobiliário deste Município\.

Este campo é o de número 21 do layout do Município de Mogi Mirim, __Pouso Alegre e Cabo Frio__\.

__MFS13248__

__MFS\-35861__

__MFS36741__

__MFS46300__

__RN28__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Complemento do endereço__

Esse campo indica o complemento do endereço do tomador de serviços\. Preencher com a informação __COMPL\_ENDERECO__ da tabela __de Cadastro de Pessoas Físicas/Jurídicas__

Formato: XXXXXX\.\.\.\./

Tamanho: 30 posições

Tipo: Texto

__Para o município de Mogi Mirim, Pouso Alegre e Cabo Frio__

Este campo será ignorado \(pelo validador\) caso seja fornecido um CPF / CNPJ ou inscrição do tomador que esteja no cadastro mobiliário deste Município\.

Este campo é o de número 22 do layout do Município de Mogi Mirim, __Pouso Alegre e Cabo Frio__\.

__MFS13248__

__MFS\-35861__

__MFS36741__

__MFS46300__

__RN29__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Bairro do tomador__

Esse campo indica o bairro do tomador de serviços\. Preencher com a informação __BAIRRO__ da tabela __de Cadastro de Pessoas Físicas/Jurídicas__

__Tratamento:__            

Se o campo não estiver preenchido, emitir a mensagem de log: “O campo Bairro não está preenchido\. Campo de preenchimento obrigatório, favor verificar”\. 

Campo Obrigatório

Formato: XXXXXX\.\.\.\./

Tamanho: 30 posições

Tipo: Texto

__Para o município de Mogi Mirim, Pouso Alegre e Cabo Frio__

Este campo será ignorado \(pelo validador\) caso seja fornecido um CPF / CNPJ ou inscrição do tomador que esteja no cadastro mobiliário deste Município\.

Este campo é o de número 23 do layout do Município de Mogi Mirim__, Pouso Alegre e Cabo Frio__\.

__MFS13248__

__MFS\-35861__

__MFS36741__

__MFS46300__

__RN30__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Cidade do tomador__

Esse campo indica a cidade do tomador\. Preencher com a informação __CIDADE__ da tabela de Cadastro de Pessoas Físicas/Jurídicas

__Tratamento:__            

Se o campo não estiver preenchido, emitir a mensagem de log: “O campo Cidade do tomador não está preenchido\. Campo de preenchimento obrigatório, favor verificar”\. 

Campo Obrigatório

Formato: XXXXXX\.\.\.\./

Tamanho: 30 posições

Tipo: Texto

__Para o município de Mogi Mirim, Pouso Alegre e Cabo Frio__

Preencher com o código da UF \+ o código do município da tabela MUNICIPIO referente ao município cadastrado na pessoa fis/jur\.

O código deve ser composto por 7 caracteres e caso o código do município tenha menos do que 5 caracteres, deve ser completado com zeros à esquerda, conforme exemplo:   

UF \+ Município = 42 \+ 4202 = 4204202

Estes campos serão ignorados caso seja fornecido um CPF / CNPJ ou inscrição do tomador que esteja no cadastro mobiliário deste Município\.

Tamanho: 7 posições

Este campo é o de número 24 do layout do Município de Mogi Mirim__, Pouso Alegre e Cabo Frio__\.

__MFS13248__

__MFS36741__

__MFS46300__

__RN31__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Unidade Federal do tomador__

Esse campo indica a unidade federal do tomador de serviços\. Preencher com a informação __COD\_ESTADO__ da tabela __ESTADO __referente ao __IDENT\_ESTADO __de Cadastro de Pessoas Físicas/Jurídicas

Campo Obrigatório

Formato: XX

Tamanho: 2 posições

Tipo: Texto

__Para o município de Mogi Mirim, Pouso Alegre e Cabo Frio__

Este campo será ignorado \(pelo validador\) caso seja fornecido um CPF / CNPJ ou inscrição do tomador que esteja no cadastro mobiliário deste Município\.

Este campo é o de número 25 do layout do Município de Mogi Mirim__, Pouso Alegre e Cabo Frio__\.

__MFS13248__

__MFS\-35861__

__MFS36741__

__MFS46300__

__RN32__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo CEP do tomador__

Esse campo indica o CEP do tomador de serviços\. Preencher com a informação __CEP__ da tabela __de Cadastro de Pessoas Físicas/Jurídicas__

__Observação: __Sem pontos, sem traços, sem espaços\.

__Tratamento:__            

Se o campo não estiver preenchido, emitir a mensagem de log: “O campo CEP do tomador não está preenchido\. Campo de preenchimento obrigatório, favor verificar”\. 

Campo Obrigatório

Formato: 99999999

Tamanho: 8 posições

Tipo: Numérico

__Para o município de Mogi Mirim, Pouso Alegre e Cabo Frio__ 

Este campo será ignorado \(pelo validador\) caso seja fornecido um CPF / CNPJ ou inscrição do tomador que esteja no cadastro mobiliário deste Município\.

Este campo é o de número 26 do layout do Município de Mogi Mirim, __Pouso Alegre e Cabo Frio__\.

__MFS13248__

__MFS\-35861__

__MFS36741__

__MFS46300__

__RN33__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo E\-mail do tomador__

Esse campo indica o E\-mail do tomador de serviços\. Preencher com a informação __EMAIL__ da tabela __de Cadastro de Pessoas Físicas/Jurídicas__\.

__Tratamento:__            

Se o campo não estiver preenchido, emitir a mensagem de log: “O campo E\-mail do tomador não está preenchido\. Campo de preenchimento obrigatório, favor verificar”\. 

Campo Obrigatório

Formato: XXXXXXX\.\.\./

Tamanho: 39 posições

Tipo: Texto

__Município de Mogi Mirim, Pouso Alegre e Cabo Frio__

Para o município de Mogi Mirim, considerar tamanho: 100 posições

Este campo é o de número 27 do layout do Município de Mogi Mirim, __Pouso Alegre e Cabo Frio__

__MFS13248__

__MFS\-35861__

__MFS36741__

__MFS46300__

__RN34__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Valor do PIS__

Esse campo indica o valor do PIS\. Preencher com o somatório do campo __VLR\_PIS\_RETIDO__ da tabela __DWT\_ITENS\_SERV__\.

__Tratamentos:__            

Se o campo exceder o número de caracteres permitido ou não estiver preenchido, emitir a mensagem de log: “O campo Valor do PIS está com tamanho acima do máximo permitido \(10 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar”\. Esse campo deverá ser informado sem pontos ou vírgula\. 

Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*Exemplos:* Para o valor de 100,55 deverá ser informado “0000010055”

                  Para o valor de 123456789123456,45 deverá ser informado “8912345645”\.

Campo obrigatório\.

Formato: 9999999999\. 

Tamanho: 10 posições

Tipo: Numérico

__Para o município de Mogi Mirim, Pouso Alegre e Cabo Frio__

Tamanho 15 posições

Campo Opcional

*Exemplos:* Para o valor de 100,55 deverá ser informado “000000000010055”

Se o campo na tabela estiver sem preenchimento, preencher com zeros\.

__Tratamentos:__            

Se o campo exceder o número de caracteres permitido pela obrigação, emitir a mensagem de log: “O campo Valor do PIS está com tamanho acima do máximo permitido \(15 posições\) para a obrigação\. Favor verificar”\. 

Este campo é o de número 12 do layout do município de Mogi Mirim, __Pouso Alegre e Cabo Frio__\.

__MFS13248__

__MFS36741__

__MFS46300__

__RN35__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Valor do COFINS__

Esse campo indica o valor do COFINS\. Preencher com o somatório do campo __VLR\_COFINS\_RETIDO__ da tabela __DWT\_ITENS\_SERV__\.

__Tratamentos:__            

Se o campo exceder o número de caracteres permitido ou não estiver preenchido, emitir a mensagem de log: “O campo Valor do COFINS está com tamanho acima do máximo permitido \(10 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar”\. Esse campo deverá ser informado sem pontos ou vírgula\. 

Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*Exemplos:* Para o valor de 100,55 deverá ser informado “0000010055”

                  Para o valor de 123456789123456,45 deverá ser informado “8912345645”\.

Campo obrigatório\.

Formato: 9999999999\. 

Tamanho: 10 posições

Tipo: Numérico

__Para o município de Mogi Mirim, Pouso Alegre e Cabo Frio:__

Tamanho 15 posições

Campo Opcional

*Exemplos:* Para o valor de 100,55 deverá ser informado “000000000010055”

Se o campo na tabela estiver sem preenchimento, preencher com zeros\.

__Tratamentos:__            

Se o campo exceder o número de caracteres permitido pela obrigação, emitir a mensagem de log: “O campo Valor do COFINS está com tamanho acima do máximo permitido \(15 posições\) para a obrigação\. Favor verificar”\. 

Este campo é o de número 11 do layout do município de Mogi Mirim __e Pouso Alegre__\.

__MFS13248__

__MFS36741__

__MFS46300__

__RN36__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Valor do INSS__

Esse campo indica o valor do INSS\. Preencher com o somatório do campo __VLR\_INSS\_RETIDO__ da tabela __DWT\_ITENS\_SERV__\.

__Tratamentos:__            

Se o campo exceder o número de caracteres permitido ou não estiver preenchido, emitir a mensagem de log: “O campo Valor do INSS está com tamanho acima do máximo permitido \(10 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar”\. Esse campo deverá ser informado sem pontos ou vírgula\. 

Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*Exemplos:* Para o valor de 100,55 deverá ser informado “0000010055”

                  Para o valor de 123456789123456,45 deverá ser informado “8912345645”\.

Campo obrigatório\.

Formato: 9999999999\. 

Tamanho: 10 posições

Tipo: Numérico

__Para o município de Mogi Mirim, Pouso Alegre e Cabo Frio:__

Tamanho 15 posições

Campo Opcional

*Exemplos:* Para o valor de 100,55 deverá ser informado “000000000010055”

Se o campo na tabela estiver sem preenchimento, preencher com zeros\.

__Tratamentos:__            

Se o campo exceder o número de caracteres permitido pela obrigação, emitir a mensagem de log: “O campo Valor do INSS está com tamanho acima do máximo permitido \(15 posições\) para a obrigação\. Favor verificar”\. 

Este campo é o de número 10 do layout do município de Mogi Mirim, __Pouso Alegre e Cabo Frio__

__MFS13248__

__MFS36741__

__MFS46300__

__RN37__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Valor do IRRF__

Esse campo indica o valor do IRRF\. Preencher com o somatório do campo __VLR\_TRIBUTO\_IR__ da tabela __DWT\_ITENS\_SERV__\.

__Tratamentos:__            

Se o campo exceder o número de caracteres permitido ou não estiver preenchido, emitir a mensagem de log: “O campo Valor do IRRF está com tamanho acima do máximo permitido \(10 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar”\. Esse campo deverá ser informado sem pontos ou vírgula\. 

Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*Exemplos:* Para o valor de 100,55 deverá ser informado “0000010055”

                  Para o valor de 123456789123456,45 deverá ser informado “8912345645”\.

Campo obrigatório\.

Formato: 9999999999\. 

Tamanho: 10 posições

Tipo: Numérico

__Para o município de Mogi Mirim, Pouso Alegre e Cabo Frio__

Tamanho 15 posições

Campo Opcional

*Exemplos:* Para o valor de 100,55 deverá ser informado “000000000010055”

Se o campo na tabela estiver sem preenchimento, preencher com zeros\.

__Tratamentos:__            

Se o campo exceder o número de caracteres permitido pela obrigação, emitir a mensagem de log: “O campo Valor do IRFF está com tamanho acima do máximo permitido \(15 posições\) para a obrigação\. Favor verificar”\. 

Este campo é o de número 13 do layout do município de Mogi Mirim, __Pouso Alegre e Cabo Frio__

__MFS13248__

__MFS36741__

__MFS46300__

__RN38__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Valor do CSLL__

Esse campo indica o valor do CSLL\. Preencher com o somatório do campo __VLR\_CSLL__ da tabela __DWT\_ITENS\_SERV__\.

__Tratamentos:__            

Se o campo exceder o número de caracteres permitido ou não estiver preenchido, emitir a mensagem de log: “O campo Valor do CSLL está com tamanho acima do máximo permitido \(10 posições\) ou não está preenchido\. Campo de preenchimento obrigatório, favor verificar”\. Esse campo deverá ser informado sem pontos ou vírgula\. 

Nossa tabela permite gravar no tamanho de 15,2 \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*Exemplos:* Para o valor de 100,55 deverá ser informado “0000010055”

                  Para o valor de 123456789123456,45 deverá ser informado “8912345645”\.

Campo obrigatório\.

Formato: 9999999999\. 

Tamanho: 10 posições

Tipo: Numérico

__Para o município de Mogi Mirim, Pouso Alegre e Cabo Frio __

Tamanho 15 posições

Campo Opcional

*Exemplos:* Para o valor de 100,55 deverá ser informado “000000000010055”

__Tratamentos:__            

Se o campo exceder o número de caracteres permitido pela obrigação, emitir a mensagem de log: “O campo Valor do CSLL está com tamanho acima do máximo permitido \(15 posições\) para a obrigação\. Favor verificar”\. 

Se o campo na tabela estiver sem preenchimento, preencher com zeros\.

Este campo é o de número 14 do layout do município de Mogi Mirim, __Pouso Alegre e Cabo Frio__

__MFS13248__

__MFS36741__

__MFS46300__

__RN39__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Discriminação dos serviços__

Esse campo descreve o texto do serviço prestado\. Preencher com o campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado no item da nota fiscal\.

O conjunto de caracteres correspondentes ao código ASC 13 e ASC 10 \(Chr\(13\) \+ Chr\(10\)\) deverá ser substituído pelo caracter | \(pipe ou barra vertical\. ASC 124\)\. 

__Exemplo: __

Digitado na NF "Lavagem de carro com lavagem de motor\." Preenchimento do arquivo: "Lavagem de carro|com lavagem de motor" 

Não serão colocados espaços neste campo para completar seu tamanho máximo \(que é de 1000 caracteres\)\. 

Campo obrigatório

Formato: XXXXXXXXXXXXXXXXXX\(\.\.\.\)

Tamanho: N<1000 posições 

Tipo: Texto

__MFS13248__

__RN39\.1__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Valor do ISS __

__Este campo deve ser incluído apenas para o município de Mogi Mirim, Pouso Alegre e Cabo Frio:__

Esse campo indica o valor do ISS Retido\. Preencher com o somatório do campo __VLR\_ISS\_RETIDO __da tabela __DWT\_ITENS\_SERV__\.

*Exemplos:* Para o valor de 100,55 deverá ser informado “000000000010055”

                  

Formato: 999999999999999\. 

Tamanho: 15 posições

Tipo: Numérico

Se o campo na tabela estiver sem preenchimento, preencher com zeros\.

__Tratamentos:__            

Se o campo exceder o número de caracteres permitido pela obrigação, emitir a mensagem de log: “O campo Valor do ISS está com tamanho acima do máximo permitido \(15 posições\) para a obrigação\. Favor verificar”\. 

Este campo é o de número 9 do layout do município de Mogi Mirim__, Pouso Alegre e Cabo Frio__\.

__MFS\-35861__

__MFS36741__

__MFS46300__

__RN39\.2__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Valor Aproximado Tributos__

__Este campo deve ser incluído apenas para o município de Mogi Mirim, Pouso Alegre e Cabo Frio:__

Esse campo indica o valor aproximado dos tributos\. Preencher com o somatório dos campos de 9 a 14 do layout do município de Mogirim: Valor Retenção ISS \+ Valor Retenção INSS \+ Valor Retenção COFINS \+ Valor Retenção IR \+Valor Retenção PIS \+ Valor Retenção CSLL

*Exemplos:* Para o valor de 100,55 deverá ser informado “000000000010055”

                  

Formato: 999999999999999\. 

Tamanho: 15 posições

Tipo: Numérico

__Tratamentos:__            

Se o campo exceder o número de caracteres permitido pela obrigação, emitir a mensagem de log: “O campo Valor Aproximado dos Tributos está com tamanho acima do máximo permitido \(15 posições\) para a obrigação\. Favor verificar”\. 

Se não houver tributos, preencher com zeros\.

Este campo é o de número 15 do layout do município de Mogi Mirim__, Pouso Alegre e Cabo Frio__\.

__MFS\-35861__

__MFS36741__

__MFS46300__

__RN39\.3__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Código da Cidade de Local de Prestação do Serviço__

__Este campo deve ser incluído apenas para o município de Mogi Mirim, Pouso Alegre e Cabo Frio:__

Este campo é de preenchimento obrigatório e só deve ser preenchido com a informação do campo COD\_MUNIC\_MSAF da tabela de municípios vinculado ao código do campo COD\_MUNICIPIO da DWT\_DOCTO\_FISCAL, se o campo ‘Situação da Nota’ estiver preenchido com “N” – Não Tributada\. Neste cenário, se o código não estiver preenchido, exibir a mensagem “Deve ser informado o local de prestação do serviço, para as notas não tributada”\.

Quando o campo ‘Situação da Nota’ estiver preenchido diferente de “N” – Não Tributada, preencher este campo com brancos\.

Formato: 9999999\. 

Tamanho: 7 posições

Tipo: Numérico

Este campo é o de número 28 do layout do município de Mogi Mirim__, Pouso Alegre e Cabo Frio__\.

__MFS\-38681__

__MFS36741__

__MFS46300__

__RN39\.4__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Alíquota Simples Nacional__

Se o campo IND\_ISS da tabela Estabelecimento for = “07”, recuperar a informação do campo 32\-VLR\_ALIQ\_ISS da tabela DWT\_ITENS\_SERV\.

Senão, preencher com zeros\.

Campo obrigatório\.

Formato: 999

Tamanho: 3 posições

Tipo: Numérico

__Tratamentos:__            

            A Alíquota deve estar entre 2,00 e 5,00 %, se não estiver, emitir a mensagem de log: “O campo Aliquota Simples Nacional não está com o valor entre 2,00 e 5,00%\. Favor verificar\.”\. 

Este campo deve ser incluído no layout de Mogi Mirim, __Pouso Alegre e Cabo Frio__ \(campo de número 8\)

__MFS\-35681__

__MFS36741__

__MFS46300__

__RN40__

__Registro Tipo 2 Nota Fiscal do Sistema Legado – Regra para o campo Caractere de fim de linha__

Esse campo representa o fim da linha \(Chr\(13\) \+ Chr\(10\)\) – Fim da linha e Retorno para uma nova linha\.

__MFS13248__

__RN41__

__Registro Tipo 9 Rodapé – Regra para o campo Tipo de Registro__

Esse campo indica a linha do rodapé\. Preencher com o valor fixo = __“9”__\. 

Campo obrigatório\.

Formato: 9

Tamanho: 1 posição

Tipo: Numérico

__MFS13248__

__RN42__

__Registro Tipo 9 Rodapé – Regra para o campo Número de linhas detalhe__

Esse campo indica a quantidade de linhas contidas no arquivo\.

Campo obrigatório\.

Formato: 9999999999

Tamanho: 10 posições

Tipo: Numérico

__MFS13248__

__RN44__

__Registro Tipo 9 Rodapé – Regra para o campo Valor total dos serviços contidos no arquivo__

Esse campo indica a soma dos valores dos serviços das Notas Fiscais do arquivo\.

Campo obrigatório\.

Formato: 999999999999999

Tamanho: 15 posições

Tipo: Numérico

__RN45__

__Registro Tipo 9 Rodapé – Regra para o campo Valor total do valor base contido no arquivo__

Esse campo indica a soma dos valores do valor base das linhas detalhe contido no arquivo\.

Campo obrigatório\.

Formato: 999999999999999

Tamanho: 15 posições

Tipo: Numérico

__MFS13248__

__RN46__

__Registro Tipo 9  Rodapé – Regra para o campo Caractere de fim de linha__

Esse campo representa o fim da linha \(Chr\(13\) \+ Chr\(10\)\) – Fim da linha e Retorno para uma nova linha\.

__MFS13248__

__RN47__

__Regra para inclusão do módulo no Manager:__

O módulo “Mogi Mirim” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo:__ “O arquivo consiste na entrega das notas fiscais emitidas pelo contribuinte para os tomadores de serviço referente ao município de Mogi Mirim”\.__

__MFS\-35861__

__RN47\.1__

__Regra para inclusão do módulo no Manager:__

O módulo “Pouso Alegre” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo:__ “O arquivo consiste na entrega das notas fiscais emitidas pelo contribuinte para os tomadores de serviço referente ao município de Pouso Alegre”\.__

__MFS36741__

__RN47\.2__

__Regra para inclusão do módulo no Manager:__

O módulo “Cabo Frio” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo:__ “O arquivo consiste na entrega das notas fiscais emitidas pelo contribuinte para os tomadores de serviço referente ao município de Cabo Frio”\.__

__MFS46300__

__RN48__

__Regra para abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “30805” \(Mogi Mirim\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Mogi Mirim, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-35861__

__RN48\.1__

__Regra para abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “MG” e ao código de município do IBGE igual a “52501” \(Pouso Alegre\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Pouso Alegre, Minas Gerais\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS36741__

__RN48\.2__

__Regra para abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RJ” e ao código de município do IBGE igual a “704” \(Cabo Frio\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Cabo Frio, Rio de Janeiro\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS46300__

__RN49__

__Para o município de Mogi Mirim:__

Considerar o mesmo layout, ordem de exibição das colunas dos registros tipo 1 e 9, incluindo as regras de recuperação dos registros já criadas para o município de Marilia\)\. Se houver alguma exceção, está detalhado no respectivo campo, desses registros\. 

 

Para o registro de tipo 2, considerar as regras citadas em cada campo \(criados para o município de Marília, ou através desta própria demanda\)\. Porém a ordem das colunas deste registro para o município de Mogi Mirim deve seguir a tabela abaixo:

__Ordem__

__Campos__

__Número da Regra de Negócio__

1

Tipo de Registro

RN15

2

Identificador Sistema Legado

RN16

3

Tipo de Codificação

RN17

4

Código do Serviço

RN18

5

Situação da Nota Fiscal 

RN19

6

Valor dos Serviços

RN20

7

Valor da Base de Cálculo

RN21

8

Alíquota Simples Nacional

RN39\.4

9

Valor Retenção ISS

RN39\.1

10

Valor Retenção INSS

RN36

11

Valor Retenção COFINS

RN35

12

Valor Retenção PIS

RN34

13

Valor Retenção IR

RN37

14

Valor Retenção CSLL

RN38

15

Valor Aproximado Tributos

RN39\.2

16

CPF/CNPJ do tomador

RN22

17

Inscrição Municipal do Tomador

RN23

18

Inscrição Estadual do Tomador

RN24

19

Nome/Razão Social do Tomador

RN25

20

Endereço do Tomador

RN26

21

Número do Endereço

RN27

22

Complemento do Endereço

RN28

23

Bairro do Tomador

RN29

24

Cidade do Tomador

RN30

25

Unidade Federal do Tomador

RN31

26

CEP do Tomador

RN32

27

E\-mail do Tomador

RN33

28

Código da Cidade de Local de Prestação do Serviço

RN39\.3

29

Discriminação dos Serviços

RN39

30

Caracter de Fim de linha

RN40

__MFS\-35861__

__RN50__

__Serviços Tomados \- Para o município de Mogi Mirim__

Criar o layout de Serviços Tomados\.

O arquivo deve ser no formato TXT separados por TAB

__Recuperação das Notas: __

- Notas de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 e 3 OU classificação do documento \(cód\_class\_doc\_fis = ‘9’\) e codigo do documento \(cód\_docto = ‘RPA’\)
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Não deve recuperar notas canceladas\.
- Quando a nota não tiver itens não deve ser recuperada\. 

__MFS\-35861__

__RN51__

__Serviços Tomados – Para o município de Mogi Mirim__

Campos e regras que devem ser apresentados no arquivo do Layout de Tomados

__Campos__

__Obrigatório__

__Formato__

__Regras__

__CPF ou CNPJ do Prestador de Serviços__

SIM

Numérico

\(99999999999999\)

Informar o CPF ou CNPJ da pessoa prestadora do serviço\. 

Preencher com a informação do campo CPF/CGC da tabela de Cadastro de Pessoas Físicas/Jurídicas\.

__Número Inicial da Nota Fiscal__

SIM

Numérico

Considerar o campo NUM\_DOC\_FIS da DWT\_DOCTO\_FISCAL

__Séries da Nota Fiscal__

Não

Alfanumérico

Considerar o campo SERIE\_DOC\_FIS da DWT\_DOCTO\_FISCAL

__Subsérie da Nota fiscal__

Não

Alfanumérico

Considerar o campo SUB\_SERIE\_DOC\_FIS da DWT\_DOCTO\_FISCAL

__Dia de Emissão__

SIM

DDMMAAAA

Considerar o campo DATA\_EMISSAO da DWT\_DOCTO\_FISCAL

__Código de serviço__

SIM

Alfanumérico

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao campo IDENT\_SERV\_LEI\_116 relacionado ao serviço cadastrado na nota fiscal\.

__Situação da Nota Fiscal__

SIM

Alfanumérico

Lista de Valores Válidos:

tp, tt, nt, is, im

Esse campo indica a situação da Nota Fiscal\. 

Lista de Valores Válidos:

tp, tt, nt, is, im

Preencher com:

__“is” – Isenta: __

Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “10” \(Isento\), se não estiver preenchido verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433” ou campo Base Isenta ISS da capa do documento fiscal \(safx07\) estiver > zero

__“im” – Imune: __

Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “07”; __OU__

Se não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420” no módulo: Parâmetros para Município\.

__R = Retido no tomador__

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

\- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado OU 

\- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo 

COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU

\- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado 

__N – Retido Fora__

quando o campo IND\_ISS da tabela ESTABELECIMENTO = “05” e se o município do estabelecimento é diferente de Mogi Mirim\.

__Valor do serviço \(base de cálculo\)__

SIM

Numérico

Esse campo indica o valor da base de cálculo\. Preencher com o campo VLR\_BASE\_ISS\_1 OU VLR\_BASE\_ISS\_2 da tabela DWT\_ITENS\_SERV\.

__IM do Tomador__

Não

Numérico

Esse campo indica a inscrição municipal do tomador de serviços\. Preencher com a informação __INSC\_MUNICIPAL__ da tabela __Estabelecimentos__

__Tipo de Nota Fiscal: __

SIM

Alfanumérico

Lista de Valores Válidos:

T = talão, 

F = Formulário, 

J = Jogo Solto, 

R = Recibo, 

E ou EL = Eletrônica

Preencher com o campo Tipo Documento da tela Parâmetros por Município – Parâmetros – Tipo Docto Msaf x Tipo Docto referente ao COD\_DOCTO cadastrado na nota\. 

Caso o tipo de documento não esteja parametrizado na tela, exibir mensagem no log “”

Se existir parametrização, verificar se a opção está na lista de valores válidos, caso não esteja, exibir a mensagem no log\. “O tipo de nota fiscal não está de acordo com a lista válida: “T, F, J, R, E ou EL\)\. Favor verificar”

__Alíquota SuperSimples: __

Não

Numérico

Se o prestador de Serviço for Optante do Simples, este campo é de preenchimento obrigatório\.

Se o campo IND\_SIMPLES\_NAC da tabela SAFX04 for igual a “S”, referente a PFJ da SAFX07

     Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV

Senão

     Preencher com zero\.

__MFS\-35861__


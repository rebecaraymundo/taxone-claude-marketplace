# MTZ_Porto_Velho_GIMOline_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_Porto_Velho_GIMOline_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 86 KB

---

THOMSON REUTERS

Municipal – Porto Velho

“Porto Velho\-GIM Online”

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS2085

Jefferson Mota

Este documento tem como objetivo tratar a geração do meio magnético para atendimento ao município de Porto Velho através do validador Porto Velho Gim Online\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

__RN01__

__Regra p/ inclusão do novo módulo no Manager:__

O módulo “Porto Velho\-Gim Online” deve manter localizado no grupo “Municipal”\. 

Descrição no Manager: “*Consiste na entrega das informações sobre os serviços tomados na Gim Oline do município de Porto Velho*”\.

MFS2085

__RN02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RO” e ao código de município do IBGE igual a “205” \(Porto Velho\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Porto Velho, Rôndonia\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

MFS2085

__RN03__

__Estrutura de menus do módulo “Porto Velho\-Gim Online” para validador Gim Online:__

Deverão ser criados os seguintes menus e sub\-menus no módulo Porto Velho\-Gim Online para validador Gim Online:

- Arquivo
- Obrigações
	- Geração do Meio Magnético
- Janela

Ajuda

MFS2085

__RN04__

__Geração do Meio Magnético __

__Menu:__  Obrigações >> Geração do Meio Magnético

A geração do meio magnético deve ser feita no padrão Framework\.

Essa tela será composta pelas seguintes abas:

Parâmetros: o sistema deve exibir os parâmetros de entrada da geração\.

Processos: o sistema deve exibir os processos já executados para essa geração\.

Log de Processo: o sistema deve exibir o log gerado durante a geração\.

Arquivo: o sistema deve exibir o arquivo que será gravado\. 

Conferência do Meio Magnético: o sistema deve exibir um relatório de conferência das informações geradas no meio magnético\.

MFS2085

__RN05__

__Regra de criação do nome do arquivo__

Esse módulo gera apenas as notas fiscais de serviços tomados, pois a Importação de documentos de serviços prestados não está mais disponível na versão 2\.4 do validador\.

O arquivo pode ser gerado com qualquer nome, a critério do contribuinte, então colocaremos a nomenclatura padrão\.

__ST\_GIM\_MUNICIPIO\_NNNNN\_DDMMAAAA\.XML__, onde:

       __ST\_GIM:__ representa a obrigação que está sendo gerada\. Apenas registros de serviços tomados\.

       __MUNICIPIO:__ representa o município que está sendo gerado\.

__       NNNNN: __representa o valor da aliquota utilizada\.

       __DDMMAAAA:__ representa a data inicial da geração

       __\.XML:__ extensão do arquivo\.

Caso o parâmetro Quebrar Arquivos por Data de Emissão estiver marcado deverá ser realizada a seguinte verificação: 

- Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal;
- Esse arquivo deve conter todas as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas e a nomenclatura desses arquivos deverão ser:

__ST\_GIM\_MUNICIPIO\_ NNNNN\_DDMMAAAA\_MMAAAA\.XML__, onde:

     __ST\_GIM:__ representa a obrigação que está sendo gerada\.

__     MUNICIPIO: __representa o município para o qual está sendo gerado\.

__     NNNNN: __representa o valor da aliquota utilizada\.

     __DDMMAAAA:__ representa a data inicial da geração\.

__     MMAAAA:__ representa o mês da competência referente à nota gerada\.

    \.__txt:__ extensão do arquivo\.

Ex: ST\_GIM\_FORTALEZA\_01250\_01012010\_122009\.txt

MFS2085

__RN06__

__Regra p/ tela da Geração do Meio Magnético__

__Menu:__  Obrigações >> Geração do Meio Magnético

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\. 

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Quebrar Arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)\.

__Estabelecimento:__ neste campo devem ser listados todos os estabelecimentos que deverão ser considerados na geração do arquivo\.

MFS2085

__RN07__

__Regra do campo Estabelecimento da tela Obrigações – Meio Magnético:__

O sistema deve exibir os estabelecimentos pertencentes ao município em questão, que estejam licenciados e que o usuário possua acesso no PowerLock\.

MFS2085

__RN08__

__Regras referentes à formatação dos registros gerados no meio magnético__

Abaixo seguem algumas formatações de dados que devem ser seguidas para geração correta na estrutura dos arquivos\.

O arquivo a ser gerado para importação dever ser no formato __‘XML’;__

Não incluir comentários no arquivo XML;

Não incluir anotação e documentação no arquivo XML \(TAG annotation e TAG documentation\);

Não incluir caracteres de formatação no arquivo XML \("line\-feed", "carriage return", "tab", caractere de "espaço" entre as TAGs\);

Acentos e caracteres especiais devem ser suprimidos do arquivo, conforme exigência do validador\.

__Campo tipo Data \(date\)__

Campos tipo Data devem ser preenchidos no seguinte formato: AAAA\-MM\-DD ;

__Campo de Valores Decimais__

Os valores decimais devem ser no formato: “__0\.00”__\.

Não deve ser utilizado separador de milhar\. O ponto \(__\.__\) deve ser utilizado para separar a parte inteira da fracionária:

Exemplo: 48\.562,25 = 48562\.25 / 1,00 = 1\.00 ou 1 / 0,50 = 0\.50 ou 0\.5

__Campo de Valores Percentuais__

Os valores percentuais devem ser preenchidos no formato: “0\.0000”\.

O formato em percentual presume o valor percentual em sua forma fracionária, contendo 5 dígitos\. O ponto \(\.\) separa a parte inteira da fracionária\.

Exemplo: 62% = 62 / 150% = 150 / 25,32% = 25\.32

__Campo tipo Numérico__

Não incluir “zeros não significativos” para campos numéricos;

Não incluir “espaços” no início ou no final de campos numéricos

A posição do campo é definida na estrutura do documento XML através de TAGs \(<tag>conteúdo</tag>\);

__Campo tipo Texto__

Não deve ser inseridos espaços em branco após o preenchimento

Não inserir espaços no inicio ou fim dos campos;

A posição do campo é definida na estrutura do documento XML através de TAGs \(<tag>conteúdo</tag>\);

As tags que permitirem valores nulos devem ser omitidas da estrutura XML a ser enviada quando seus valores forem nulos\.

MFS2085

__RN09__

__Regra geral p/ recuperar serviços tomados \(só geraremos serviços tomados no arquivo\)__

O arquivo deve conter todas as notas com as seguintes características:

- Notas de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento de Serviço e Mista \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou classificação do documento de Recebibos \(cód\_class\_doc\_fis = ‘9’\) e codigo do documento \(cód\_docto = ‘RPA’\)
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência

*Observação:* 

- Arquivo conterá apenas informações de serviços tomados;
- Recuperar apenas notas fiscais com itens de serviços;
- Pode ter serviços diferentes para o mesmo documento fiscal\.
- O arquivo poderá ser quabrado por aliquota, caso exista aliquotas diferentes\.

MFS2085

__RN10__

__<?xml version="1\.0" encoding="utf\-8"?>__

Tag relacionada à formatação do arquivo deve conter o texto fixo: __‘<?xml version="1\.0" encoding="utf\-8"?>’\.__

Campo obrigatório\.

MFS2085

__RN11__

__Regra p/ tag <gim versao="1\.0">__

TAG onde deve conter os dados da estrutura da gim de Notas Fiscais para fila de processamento\.

Deve ser gerada somente 1 vez no arquivo e encerrada com o formato __</gim>__

Campo obrigatório\.

MFS2085

__RN12__

__Regra para TAG <declarante>__

TAG que indica as informações do declarante\.

TAG obrigatória\.

MFS2085

__RN13__

__Regra p/ tag <tipo>P</tipo>__

Preencher com o valor fixo “__P__”\.

Sequencial numérico por arquivo gerado\. 

Tipo: Texto 

 Tamanho: 1

Campo obrigatório\.

MFS2085

<a id="_Hlk433297870"></a>__RN14__

__Regra para tag <inscricaoMunicipal> </inscricaoMunicipal>__

Campo pertencente à tag <declarente>\. Será gerado com o conteúdo do campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO, considerando as 9 últimas posições do campo\. 

Se o tamanho do campo tiver mais de 9 posições e for aplicada a regra de seleção das 9 últimas, retornar a mensagem no log: 

“A tag “__<inscricaoMunicipal>__” foi gerada com as 9 últimas posições do campo Inscrição Municipal na tabela ESTABELECIMENTO\.

Tipo: Numerico

Tamanho máximo: 09

MFS2085

__RN15__

__Regra para tag <numeroDocumento>  </numeroDocumento>__

Campo pertencente à tag <declarente>\. Preencher com o campo CGC da tabela ESTABELECIMENTO do estabelecimento de geração do arquivo\.

Tipo: Numerico

Tamanho máximo: 14

MFS2085

__RN16__

__Regra para tag <tipoDocumento> </tipoDocumento>__

Campo pertencente à tag <declarente>\. 

Preencher com texto fixo __“1”__ 

Tipo: Numerico

Tamanho máximo: 01

MFS2085

__RN17__

__Regra para tag <valorAliquota> </valorAliquota>__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.

Tipo: Numerico

Tamanho máximo: 18

MFS2085

__RN18__

__Regra para TAG </declarante>__

TAG que indica o fechamento da tag declarante\.

TAG obrigatória\.

MFS2085

<a id="_Hlk434873295"></a>__RN19__

__Regra para TAG <competencia>__

TAG que indica as informações de data de competencia\.

TAG obrigatória\.

MFS2085

__RN20__

__Regra para tag <mes>  </mes> __

Campo pertencente à tag <competencia__>\. __

Será gerado com o Mês de geração parametrizado na Data Inicial da  tela de Geração\.

Tipo: Numerico

Tamanho máximo: 02

MFS2085

__RN21__

__Regra para tag <ano>  </ano>__

Campo pertencente à tag <competencia__>\. __

Será gerado com o ano de geração parametrizado na Data Inicial da tela de geração\.

Tipo: Numerico

Tamanho máximo: 04

MFS2085

__RN22__

__Regra para TAG </competencia>__

TAG que indica o fechamento da tag competencia\.

TAG obrigatória\.

MFS2085

__RN23__

__Regra para TAG <notasFiscais>__

TAG que indica o Elemento que contém um ou vários elementos do Grupo E \(notaFiscal\)\. 

TAG obrigatória\.

MFS2085

__RN24__

__Regra para TAG <notaFiscal>__

TAG que indica os elementos que contém os dados das Notas Fiscais\. Este é o único elemento que poderá ter múltiplas ocorrências\. 

TAG obrigatória\.

MFS2085

__RN25__

__Regra para tag <numero> </numero>__

Campo pertencente à tag __<notaFiscal>\. __Será preenchido com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Tipo: Numerico

Tamanho máximo: 09

MFS2085

__RN26__

__Regra para tag <atividade>  </atividade>__

Campo pertencente à tag __<notaFiscal>\. __

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado no item da nota\. Formato “00000”\. 

Tipo: Numerico

Tamanho máximo: 05

MFS2085

__RN27__

__Regra para tag <dataEmissao>2010\-10\-01</dataEmissao>__

Campo pertencente à tag __<notaFiscal>\. __Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.

 Formato: AAAA\-MM\-DD\.

Tamanho máximo: 10

MFS2085

__RN28__

__Regra para tag <valor>  </valor>__

Campo pertencente à tag __<notaFiscal>\. __Preencher com o somatório do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\. Valor com duas casas decimais\.

Tipo: Numerico

Tamanho máximo: 18

MFS2085

__RN29__

__Regra para tag <localEmissao> </localEmissao>__

Campo pertencente à tag __<notaFiscal>\. __

Preencher com o Local de emissão da Nota Fiscal\. 

__F__ = Notas Fiscais emitidas fora do Município\. Para preencher com “F”, verificar se o campo COD\_MUNICIPIO da tabela  DWT\_DOCTO\_FISCAL  é diferente do município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO e caso o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não estiver preenchido, o COD\_MUNICIPIO da tabela ESTABELECIMENTO deverá ser diferente do município em questão\.

__D__ = Notas Fiscais emitidas dentro do Município\. Se o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL  for igual ao município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO e caso o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não estiver preenchido, o COD\_MUNICIPIO da tabela ESTABELECIMENTO deverá ser Igual do município em questão\. 

Tipo: Texto

Tamanho máximo: 01

MFS2085

__RN30__

__Regra para tag <situacao> </situacao>__

Campo numérico de preenchimento não obrigatório de tamanho máximo 1\.

Preencher com:

__RTD =  __Verificar se__ __o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV <> 0\. __ __

__CAN = __ __Q__uando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL \(campo 30 da SAFX07\) = ‘S’

__NRM = __Quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL \(campo 30 da SAFX07\) <> ‘S’

Tipo: Texto

Tamanho máximo: 01

MFS2085

__RN31__

__Regra para tag <valorDeducao>  </valorDeducao> __

Preencher com o campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV\.

Tipo: Numérico

Tamanho máximo: 18

MFS2085

__RN32__

__Regra para tag <recebedor>__

TAG que indica os Elemento que contém os dados do Recebedor da Nota Fiscal\.

TAG obrigatória\.

MFS2085

__RN33__

__Regra para tag <nome>  </nome>  __

Preencher com o campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO\.

Tipo: Texto

Tamanho máximo: 100

MFS2085

__RN34__

__Regra para tag <numeroDocumento> </numeroDocumento>__

Preencher com o campo CGC\_CPF da tabela ESTABELECIMENTO\.

Tipo: Numérico

Tamanho máximo: 14

MFS2085

__RN35__

__Regra para tag <tipoDocumento> </tipoDocumento>__

Preencher com __“1”\.__

Tipo: Numérico

Tamanho máximo: 01

MFS2085

__RN36__

__Regra para tag <cidade> </cidade>__

Preencher com o campo CIDADE da tabela ESTABELECIMENTO\.\. 

Tipo: Texto

Tamanho máximo: 60

MFS2085

__RN37__

__Regra para tag <estado>  </estado> __

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao IDENT\_ESTADO preenchido na tabela ESTABELECIMENTO\.

Tipo: Texto

Tamanho máximo: 02

MFS2085

__RN38__

__Regra para tag <endereco>__

TAG que indica os Elemento que contém os dados do Logradouro do Recebedor da Nota Fiscal\.

TAG obrigatória\.

MFS2085

__RN39__

__Regra para tag <tipo>  </tipo> __

Preencher com o campo TP\_LOGRADOURO da tabela ESTABELECIMENTO\.

Tipo: Texto

Tamanho máximo: 20

MFS2085

__RN40__

__Regra para tag <logradouro> </ logradouro >__

Preencher com o campo ENDERECO da tabela ESTABELECIMENTO\.

Tipo: Texto

Tamanho máximo: 100

MFS2085

__RN41__

__Regra para tag <numero>  </numero>__

Preencher com o campo NUM\_ENDERECO da tabela ESTABELECIMENTO\.

Tipo: Texto

Tamanho máximo: 10

MFS2085

__RN42__

__Regra para tag <bairro> </bairro>__

Preencher com o campo BAIRRO da tabela ESTABELECIMENTO\.

Tipo: Texto

Tamanho máximo: 60

MFS2085

__RN43__

__Regra para tag <complemento>  </complemento>__

Preencher com o campo CAMPL\_ENDERECO da tabela ESTABELECIMENTO\.

Tipo: Texto

Tamanho máximo: 100

MFS2085

__RN44__

__Regra para tag <cep>  </cep> __

Preencher com o campo CEP da tabela ESTABELECIMENTO\.

Tipo: Numérico

Tamanho máximo: 08

MFS2085

__RN45__

__Regra para tag </endereco>__

Indica o fechamento da TAG <endereco>

TAG obrigatória\.

MFS2085

__RN46__

__Regra para tag </recebedor>__

Indica o fechamento da TAG </recebedor>

TAG obrigatória\.

MFS2085

__RN47__

__Regra para tag </notaFiscal>__

Indica o fechamento da TAG </notaFiscal>

TAG obrigatória\.

MFS2085

__RN48__

__Regra para tag </notasFiscais>__

Indica o fechamento da TAG </notasFiscais>

TAG obrigatória\.

MFS2085

__RN49__

__Regra para tag </gim>__

Indica o fechamento da TAG </gim>

TAG obrigatória\.

MFS2085

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN


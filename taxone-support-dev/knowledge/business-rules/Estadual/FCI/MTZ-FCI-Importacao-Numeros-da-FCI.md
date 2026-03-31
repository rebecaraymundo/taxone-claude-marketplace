# MTZ-FCI-Importacao-Numeros-da-FCI

- **Fonte:** MTZ-FCI-Importacao-Numeros-da-FCI.docx
- **Modificado:** 2026-02-12
- **Tamanho:** 38 KB

---

                __FCI – Importação dos Arquivos retornados da Sefaz __

__                                    com os Números da FCI__

__Localização__: Menu Estadual, Módulo FCI 🡪 Obrigações 🡪 Importação dos Números da FCI

##                                            Documento de Requisito

__Doc__

__Alteração__

__Data__

__Resp__

OS3874\-G

Importação dos Números da FCI

13/09/2013	

\(Criação do doc\)

Vânia Mattos

OS4417

Inclusão do parâmetro “Nomenclatura a ser utilizada p/identificação dos arquivos”

26/05/2014

Vânia Mattos

__RN00 – Regras Gerais__

__Resumo do processo realizado neste menu:__

*O objetivo desta rotina é atualizar na SAFX214 os números de FCI gerados pela Sefaz\.*

*Estes números são gerados após a transmissão dos arquivos, e gravados no campo “10\-Código FCI” dos registros 5020\. Depois que a Sefaz gera a informação, os arquivos atualizados são disponibilizados no site para acesso do usuário\. *

*O usuário poderá então, obter estes arquivos e executar esta rotina para atualizar os números FCI na base de dados do Mastersaf\.*

*Esta atualização é importante, pois o sistema irá utilizá\-los posteriormente para verificar os produtos que já têm número de FCI\. Por isso, caso o usuário não faça a atualização através desta rotina, deverá providenciá\-la de alguma outra forma, podendo utilizar também a tela de manutenção do menu: “Obrigações à Manutenção >> Movimentação de Produtos Sujeitos ao FCI”\.*

	

__RN01 – Parâmetros de Tela__

__Período de referência da geração dos arquivos  🡪 __Neste campo o usuário informará o mês e ano \(MMAAAA\) dos arquivos a serem processados\. 

__Alteração da OS4417:__ este parâmetro foi renomeado de “Período de referência dos arquivos” para “Período de referência da geração dos arquivos”\. 

__Selecione o diretório dos arquivos a serem processados __ 🡪 Este campo trabalha com janela de seleção que exibirá a árvore de diretórios, considerando os diretórios da máquina local, como também das unidades mapeadas __\(\*\)__\. O usuário irá selecionar o diretório dos arquivos a serem processados\.

__\(\*\) __Semelhante ao menu “Obrigações 🡪 Importação dos Arquivos da Sefaz\-AM” do módulo DIA\-AM\.

__Alteração da OS4417:   __\(criação do parâmetro “Nomenclatura a ser utilizada p/identificação dos arquivos”\)

__Nomenclatura a ser utilizada p/identificação dos arquivos __ 🡪 Este campo oferece duas opções para seleção do usuário:

\- Nomenclatura utilizada na geração dos arquivos

\- Nomenclatura utilizada no retorno dos arquivos pela Sefaz

As opções são alternativas, e a opção default = “Nomenclatura utilizada na geração dos arquivos”\.

Quando a opção “Nomenclatura utilizada no retorno dos arquivos pela Sefaz” for selecionada, o campo 

“Mês/Ano do retorno” será habilitado\. Caso contrário, ficará desabilitado\.

__Mês/Ano do retorno__ 🡪Este campo é referente à opção “Nomenclatura utilizada no retorno dos arquivos pela Sefaz” do parâmetro descrito acima, e o usuário informará o mês/ano em que a Sefaz retornou os arquivos\. 

Este campo será sempre inicializado com o mês a e ano informado no campo “Período de referência da geração dos arquivos”, mas só será habilitado para alteração do usuário quando a opção “Nomenclatura utilizada no retorno dos arquivos pela Sefaz”\.

Sendo assim, o seu funcionamento depende do campo anterior, da seguinte forma:

__Se__ opção = “Nomenclatura utilizada na geração dos arquivos”

      Neste caso, o campo mostrará o mesmo mês/ano do campo “Período de referência da geração dos

      arquivos”, e ficará *desabilitado*;

__Se__ opção = “Nomenclatura utilizada no retorno dos arquivos pela Sefaz”

      Neste caso, o campo também exibirá, a princípio, o mesmo mês/ano do campo “Período de referência da 

      geração dos  arquivos”, mas será *habilitado* para alteração do usuário\.  Quando alterado, o mês e ano

      informado deverá ser superior ao mês e ano informado no campo “Período de referência da geração dos

      arquivos”\. Caso contrário, será mostrada a seguinte mensagem de aviso:

              *“O mês e ano do retorno dos arquivos deve ser igual ou superior ao mês e ano da geração”*

__Estabelecimentos__ 🡪Neste campo é exibida a lista dos estabelecimentos da Empresa do login\. 

Após o usuário informar os parâmetros e clicar no botão que inicia o processo, será exibida a seguinte mensagem:

Dependendo do volume de dados dos arquivos, e da quantidade de estabelecimentos selecionados, o processo poderá ser muito demorado\. Deseja prosseguir?

                              <Sim>           <Não>

<Sim> 🡪 Apaga a mensagem e inicia o processamento

<Não> 🡪 Apaga a mensagem e aguarda decisão do usuário, que poderá alterar algum parâmetro e solicitar novamente a execução, ou sair da rotina\. 

__RN02 – Processamento dos Dados__

__Origem dos Dados__:  Arquivos FCI já validados, transmitidos e retornados pela Sefaz

__Destino: __Atualização do campo “10\-Número da FCI” da SAFX214 \(Tabela do FCI\) 

__Para cada Estabelecimento selecionado em tela, serão realizados os seguintes procedimentos__:

No diretório informado, identificar o\(s\) arquivo\(s\) do estabelecimento e mês/ano solicitado em tela\. considerando a nomenclatura utilizada na sua geração:

__Alteração da OS4417:__

Esta OS criou o parâmetro “*Nomenclatura a ser utilizada p/identificação dos arquivos*”, e assim a identificação dos arquivos passou a ser feita de duas formas diferentes \(a opção 1 é a forma original utilizada no processo\)\.

A identificação dos arquivos de cada Estabelecimento depende do parâmetro “*Nomenclatura a ser utilizada p/identificação dos arquivos”*, da seguinte forma:

__Opção 1 __= “Nomenclatura utilizada na geração dos arquivos”:       *\(opção original\)*

      Neste caso os arquivos serão identificados considerando a nomenclatura utilizada na geração \(menu

      “Obrigações 🡪 Geração do Meio Magnético”\), e o período informado no campo “Período de referência da 

      geração dos arquivos”\.

      Nomenclatura =   Número do Processo \+ Código do Estab \+ “\_FCI\_” \+ MMAAAA \+ “\_” \+ Volume \+ “__\.__txt”

      Como a utilização do número do processo é opcional, o arquivo pode ter sido gerado __com ou sem__ esta

      informação \(conforme o parâmetro “Gera Arq sem N\. Processo” do framework\)\.

      Serão considerados todos os arquivos do diretório nas condições abaixo, e poderão existir ‘n’ arquivos a

      serem processados\.

      

      \- Número do Processo = pode existir ou não, e quando existir, poderá ser qualquer um;

      \- Código do Estab   = código do estabelecimento selecionado em tela;

      \- MMAAAA             = mês e ano informado no campo “Período de referência da geração dos arquivos”;

      \- Volume                = poderá ser qualquer um, pois todos os volumes serão considerados;

__Opção 2__ = “Nomenclatura utilizada no retorno dos arquivos pela Sefaz”:      *\(opção criada na OS4417\)*

      Neste caso os arquivos serão identificados considerando a nomenclatura utilizada pela Sefaz ao retornar

      os arquivos, e o período informado no campo “Mês/Ano do retorno”\.

       Nomenclatura =      CNPJ \+ “\_” \+ AAAAMMDD \+ “\_” \+ HHMMSS

      Serão considerados todos os arquivos do diretório nas condições abaixo, e poderão existir ‘n’ arquivos a

      serem processados\.

      \- CNPJ  = CNPJ do estabelecimento selecionado em tela, recuperado do cadastro dos estabelecimentos;

      \- AAAAMM  = ano e mês informado no campo “Mês/Ano do retorno”;

      \- DD            = poderá ser qualquer dia;

      \- HHMMSS \(hora, minuto e segundo do retorno do arquivo\) = poderá ser qualquer conteúdo;

__Detalhes sobre a nomenclatura dos arquivos__:

     \- No caso da opção \(1\), os arquivos devem manter o nome original com o qual foram gerados, tendo o mês

       e ano = mês e ano do período de geração informado em tela;

     \- No caso da opção \(2\), o mês e ano do nome do arquivo indica apenas a data em que a Sefaz fez o envio

       do arquivo, e podem *não* indicar exatamente o mês/ano da geração original do arquivo\. Isso acontecerá 

       quando a Sefaz só retornar o arquivo em dia posterior ao mês e ano que consta no nome do arquivo\.

       Exemplo: arquivo gerado e enviado para a Sefaz no dia 31/05/2014\. A Sefaz processa e retorna o arquivo

       somente no dia seguinte \(= 01/06/2014\);

	

     \- O sequencial é utilizado para “quebrar” o arquivo em mais de um volume, quando a quantidade de linhas

       ultrapassa 100\.000\. Sendo assim, a rotina deve prever que *poderão existir vários volumes de arquivo*

*       para um mesmo estabelecimento*, e neste caso, todos deverão ser processados;

__Para cada volume de arquivo identificado, o processo se resume no seguinte:__

Todos os arquivos identificados conforme as regras acima serão processados\. 

\- Para cada linha do registro “*5020\-Informações dos Produtos/Mercadorias*” do arquivo, é feita a identificação 

  do produto/unidade na tabela SAFX214, da seguinte forma:

__Dados chave da SAFX214__

   

COD\_EMPRESA

= Código da empresa do login

COD\_ESTAB

= Código do estabelecimento em processamento

DATA\_REFERENCIA

= data do último dia do período de referência informado em tela 

\(campo “Período de referência da geração dos arquivos”\)

*OBS: A data a ser utilizada para identificar o registro da SAFX214 será sempre de acordo com esta regra, independente do parâmetro “Nomenclatura a ser utilizada p/identificação dos arquivos”\.*

IDENT\_PRODUTO

= IDENT da SAFX2013 referente ao produto gravado no campo

“04\-CODIGO\_MERCADORIA” do registro 5020 \(*ver OBS abaixo*\)

COD\_MEDIDA\_FCI

= Campo  “06\-UNIDADE\_MERCADORIA”  do registro 5020

\- Identificado o registro da SAFX214, o campo “10\-Número do FCI” será atualizado com o conteúdo do campo

 “10\-Código FCI” do registro 5020 em processamento;

\- Os produtos *não* identificados na SAFX2013/SAFX214 serão registrados no relatório de acompanhamento \(vide __RN03__\) para que o usuário possa identificar o problema;

__Pontos de atenção a serem considerados na obtenção do IDENT do produto:__

Observar que a SAFX214 trabalha com o IDENT do produto, logo, o produto deverá ser identificado na SAFX2013 para obtenção do IDENT a ser utilizado na pesquisa\. 

Os critérios para identificar o produto na SAFX2013 devem ser os mesmos critérios utilizados pela rotina que grava os produtos na SAFX214 no momento de obter na SAFX2013 o IDENT do produto a ser gravado na SAFX214\. A gravação dos produtos na SAFX214 é feita na rotina “*Cálculo do Valor Médio das Saídas*”, ou na importação da SAFX214 \(no caso dos clientes que não utilizam o cálculo pelo Módulo FCI\)\. 

Caso o produto não seja identificado na primeira tentativa:

Normalmente, o padrão é utilizar o IDENT do produto de maior data de validade que seja <= data final do período em questão\. Mas para evitar problemas, caso o produto tenha sido reimportado após a geração do cálculo \(ou seja, foi gerado um novo IDENT do produto no mesmo período, mas depois da execução do cálculo\), deve\-se considerar na pesquisa uma forma de pesquisar os IDENT’s anteriores, até identificar o produto na SAFX214\.

Conteúdo que estará gravado no campo “04\-CODIGO\_MERCADORIA” do registro 5020:

 Conforme definido na regra RN5020\-04 do documento de regras da geração do arquivo da FCI, este campo poderá ter dois tipos de conteúdo:

\- Indicador do produto  \+ ‘\-‘ \+ Código do produto \(ex: “1\-123456789”\)

\- Apenas o código do produto                               \(ex: “123456789”\)

Ao identificar que o campo *não* contém o indicador do produto, a pesquisa do produto na SAFX2013 será feita apenas com o Grupo e o Código do Produto\. Mas caso seja identificada a existência de produtos de mesmo código e indicadores diferentes, o registro da SAFX214 *não* será atualizado, para evitar erros\.

__RN03 – Relatórios de Acompanhamento__

Durante o processamento, serão registradas *para cada estabelecimento processado* \(__*considerando todos os volumes do estabelecimento*__\), as seguintes informações:

\- Quantidade de registros atualizados na SAFX214;

\- Quantidade de produto/unidade *não* identificados na SAFX214;

\- Quantidade de registros 5020 processados;

\- Produtos *não* identificados;

Estas informações serão exibidas na aba “Relatório” do framework, da seguinte forma:

__                                                       Totais do Estabelecimento__

__       Estab__

__Qtd prod\./unid\.__

__atualizados \( SAFX214\)__

__Qtd prod\./unid\. não identificados na SAFX214__

__Qtd de vol\. processados__

__Qtd de reg\. 5020 processados__

XXXXXX

999\.999\.999

999\.999\.999

999

999\.999\.999

XXXXXX

999\.999\.999

999\.999\.999

999

999\.999\.999

XXXXXX

999\.999\.999

999\.999\.999

999

999\.999\.999

XXXXXX

999\.999\.999

999\.999\.999

999

999\.999\.999

XXXXXX

999\.999\.999

999\.999\.999

999

999\.999\.999

XXXXXX

999\.999\.999

999\.999\.999

999

999\.999\.999

__                                                       Produtos não Identificados__

Os produtos lidos no arquivo texto, e não identificados na SAFX214, serão listados num log de erros para que o usuário possa verificar caso a caso\. 

A mensagem deve indicar o Estabelecimento, o nome do arquivo, o indicador e o código do produto, e o problema ocorrido\.

Exemplo:

Log para o Estabelecimento XXXXXX \- XXXXXXXXXXXX – Arquivo: XXXXXXXXXXXXXXXXX

Produto não identificado na SAFX2013: X \- XXXXXXXXX

Produto não identificado na SAFX2013: X \- XXXXXXXXX

Produto não identificado na SAFX214 \(identificador SAFX2013 x SAFX214 não confere\): X \- XXXXXXXXX

Produto não identificado na SAFX214 \(identificador SAFX2013 x SAFX214 não confere\): X \- XXXXXXXXX

O arq foi gerado apenas c/o código, e na SAFX2013 existe o código p/ diferentes indicadores:  XXXXXXXXX

Neste exemplo, aparecem três tipos de erro que poderão ocorrer na identificação do produto:

\- O indicador/ código do produto \(ou apenas o código, conforme o caso\), não foi encontrado na SAFX2013;

\- O indicador/ código do produto \(ou apenas o código, conforme o caso\), foi encontrado na SAFX2013, mas nenhum dos IDENT’s pesquisados existe na SAFX214;

\- Na pesquisa do código do produto na SAFX2013 \(quando no arquivo só tiver sido gravado o código\), foram encontrados diferentes indicadores para o mesmo código;

*OBS:  A *__*RN03*__* prevê que esta rotina seja desenvolvida no framework\.*


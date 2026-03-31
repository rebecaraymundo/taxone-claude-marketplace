# MTZ-STM-Geracao_do_Meio_Magnetico

- **Fonte:** MTZ-STM-Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2025-11-17
- **Tamanho:** 101 KB

---

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>

THOMSON REUTERS

Municipal

STM – Sistema Tributário Municipal \- Está sendo utilizado pelo ISS DIGITAL

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS7444

Geração do Meio Magnético STM 

Este documento tem como objetivo criar a geração para os municípios que são atendidos pelo STM – Sistema Tributário Municipal\. 

A Geração do Meio Magnético trata serviços tomados e deduções de material\.

No Manager, quando o cliente clicar em um município da atendido pelo validador STM, o módulo deste município disponibilizará a geração do Meio Magnético validador STM\. 

O módulo de Parâmetros por Município servirá para o usuário realizar as parametrizações necessárias para esta geração\. 

Nesta MFS o município de São Luiz/MA passa a ser atendido pelo validador STM\.

A Geração do Meio Magnético STM gera um arquivo txt\., cujo layout está definido no __“Manual – São Luís\.pdf”__, disponibilizado pelo Setor de Informação da nossa empresa\.

O layout do validador STM \(__“Manual – São Luís\.pdf”__\) é quase igual ao do ISS DIGITAL \(__“Manual Importacao DIM\.pdf”\)__\. 

__\- “Manual – São Luís\.pdf”__ :vamos utilizar este manual como definição da estrutura do arquivo\. 

__“Manual Importacao DIM\.pdf”__: vamos utilizar este manual para definir a relação das séries e modelos\.

[http://www\.semfaz\.saoluis\.ma\.gov\.br/](http://www.semfaz.saoluis.ma.gov.br/)

*Observação não há necessidade de fazer a geração de situação especial \(Arquivo de Entradas de Serviços\), pois o cliente não é do ramo de Construção Civil\.*

MFS\-30540

Alessandra Cristina Navatta

Ajuste na regra do campo 5 – Modelo da Nota Fiscal, do registro tipo R \(Notas Fiscais Recebidas\), dos Serviços Tomados \(RN44\)

\[EM CONSTRUÇÃO 25/11/2016\]

PENDÊNCIAS

1. Prefeitura lista de serviço
2. Prefeitura lista de modelo\.
3. Prefeitura lista se série\.

Dois itens com msm código:

RP: Recibo Pagamento Autonomo

RP: RPA – Recibo profissional autonomo

1. Ver na package o grupamento dos itens de serviço para o Registro R\.
2. Ver na package o grupamento para o Registro D\.
3. Ver na package os campos obrigatórios as mensagens\.
4. Finalizar adição de tamanho, tipo\.
5. Carga das TFIX da PRT\_VALIDADOR, PRT\_VALIDADOR\_MUNIC, PRT\_SERVICO\_OBRIG, PRT\_SERIE\_OBRIG
6. Carta do patch\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

__RN01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “São Luís” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços contratados e/ou prestados do município de São Luís”\.

MFS7444

__RN02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “MA” e ao código de município do IBGE igual a “11300” \(São Luís\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de São Luís, Maranhão\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

MFS7444

__RN03__

__Estrutura de menus do módulo São Luís:__

Deverão ser criados os seguintes menus e sub\-menus no módulo São luís:

- Arquivo
- Manutenção
	- Deduções
- Obrigações
	- __Geração do Meio Magnético__
- Janela
- Ajuda

MFS7444

__RN04__

__Regra de criação do nome do arquivo__

O arquivo tem o formato texto, e sua nomenclatura obedece a seguinte regra: 

- Quando o parâmetro __Quebrar Arquivos por Data de Emissão estiver desmarcado__ será gerado apenas um arquivo com a nomenclatura do arquivo normal indicado abaixo\.

__STM\_MUNICIPIO\_00000000000000\_DDMMAAAA\.txt__, onde:

- __STM__: representa a obrigação que está sendo gerada\.
- __MUNICIPIO__: representa o município que está sendo gerado\.
- __00000000000000: __CNPJ do Contribuinte \(numérico sem ponto e sem hífen\)\. Recuperar o campo CGC da tabela ESTABELECIMENTO\.
- __DDMMAAAA__: representa a data inicial da geração\.
- __\.txt__: extensão do arquivo\.

Ex: STM\_SAOLUIZ\_0123456\_01112016\.txt

- Caso o parâmetro Gerar Arquivos por Data de Emissão estiver marcado, não será possível marcar o parâmetro Quebrar Arquivos por Data de Emissão e deverá ser realizado o seguinte procedimento: 

O arquivo deverá conter __todas__ as notas fiscais com data de emissão dentro do período de referência\.

- Caso o parâmetro __Quebrar Arquivos por Data de Emissão estiver marcado__, não será possível marcar o parâmetro Gerar Arquivos por Data de Emissão e deverá ser realizado o seguinte procedimento: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente a data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverão ser:

__STM\_MUNICIPIO\_00000000000000\_DDMMAAAA \_MMAAAA\.txt__, onde:

- __STM__: representa a obrigação que está sendo gerada\.
- __MUNICIPIO__: representa o município que está sendo gerado\.
- __00000000000000: __CNPJ do Contribuinte \(numérico sem ponto e sem hífen\)\. Recuperar o campo CGC da tabela ESTABELECIMENTO\.
- __DDMMAAAA__: representa a data inicial da geração\.
- __MMAAAA: __mês da competência referente à nota gerada\.
- __\.txt__: extensão do arquivo\.

Ex: STM\_SAOLUIZ\_0123456\_01112016\_102016\.txt

Obs\.: Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

MFS7444

__RN05__

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final: __deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Gerar Registro Tipo “D”__ __– Dedução de Materiais da NF Emitidas de Constr\. Civil__: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Gerar Registro Tipo “R” – Notas Recebidas__: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Quebrar arquivo por Data de Emissão__: deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Gerar arquivo por Data de Emissão__: deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento__: o sistema deve exibir os estabelecimentos que pertençam ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

MFS7444

__RN06__

__Regra para abas existentes na Tela Obrigações – Meio Magnético:__

Após processar o meio magnético devem ser exibidas as abas “Log”, “Arquivo”, “Processos” e “Relatório”\. 

A aba “Arquivo” deve exibir o arquivo que poderá ser salvo localmente\.

A aba “Log” deve exibir a mensagem “Processo concluído com sucesso” quando o arquivo for gerado corretamente, caso contrário exibir a mensagem “Processo concluído com erros”\.

__RN06__

__Regras Gerais de formatação do arquivo__

Layout do arquivo está definido no __“Manual – São Luís\.pdf”__\.

O arquivo a ser gerado deverá estar no formato texto, e os campos devem se preenchidos seguindo as orientações abaixo\.

1. Campos do tipo N \(numéricos\) como CNPJ, CPF, Número da Nota Fiscal, Valores, Alíquota devem ser preenchidos com zeros à esquerda até atingir o tamanho exato do campo\.

Quando o campo for opcional, ou seja, o conteúdo do campo não for fornecido, este deverá ser preenchido com zeros até completar seu tamanho máximo\. 

- 
	1.  Campos de Valor 

Campo numérico com15 posições, sendo o ponto “\.” utilizado como separador de casas decimais e 02 posições para a parte decimal\. 

Valor no formato “999999999999\.99”

Exemplo: Para um valor de R$ 2\.500,00 no arquivo deverá estar gravado assim: 000000002500\.00

- 
	1. Campos Alíquota 

Campo tipo numérico com 4 posições, sendo o ponto “\.” utilizado como separador de casas decimais e 02 posições para a parte decimal\.\.\. 

Valor no formato “__00\.00__”\. 

1. Campos do tipo A \(alfanumérico\) deverão ser preenchidos alinhados pela esquerda, se necessário, preencher com espaços em branco à direita até completar seu tamanho máximo\.
2. Campos do tipo D \(Data\) deverão ser preenchidos no formato DD/MM/AAAA\.

Todos os campos deverão obedecer ao tamanho e a formatação definido no layout “Manual – São Luís\.pdf”

MFS7444

__Regras de preenchimento do Registro Tipo “D” – Dedução__

__RN33__

__Regra geral p/ Registro Tipo D – Dedução de Materiais e Subempreitadas das NF Emitidas de Const\. Civil__

Para que esse registro seja gerado a nota fiscal emitida deverá ser de construção civil \(IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota\)\.

Para cada dedução de uma nota deverá ser informado um registro D\. Não há limites de registro D por arquivo, desde que haja um registro E relacionado\.

Quando a nota for de construção civil, a geração deve verificar se existe dedução de material ou subempreitada para essa nota no menu Manutenção – Deduções\. Se houver a geração deve apresentar um registro para a nota emitida \(tipo E\) e tantos quantos forem os registros de dedução \(tipo D\)\.

__Faltar definir se um registro LIDO da tabela é um registro D gravado, ou se haverá grupamento\.__

?

__RN34__

__Regra do Registro Tipo D \- Campo 01 \- Identificação do registro__

Preencher com texto fixo “D”

__RN35__

__Regra do Registro Tipo D \- Campo 02 \- Data da emissão da NF emitida \(de qual deve deduzir\)__

Preencher com o campo Data Emissão da nota fiscal que será deduzida na tela Manutenção – Deduções\. \(mestre\) 

Tipo: 

Tamanho: 

__RN36__

__Regra do Registro Tipo D \- Campo 03 \- Serie da NF emitida \(De qual deve deduzir\)__

Preencher com o campo Série da tela Parâmetros – Modelo Msaf x Série referente ao tipo de documentos cadastrado na nota\. \(mestre\)

A lista de séries \(segundo o __“Manual São Luís\.pdf”__, tópico 3\.1\) que este campo pode assumir, carregada na __TFIX83__ \(Cadastro das Séries/Modelos das Obrigações \- PRT\_SERIE\_OBRIG\) é:

- A: Serviço 
- B: Material e Serviço
- M1 Material e Serviço 
- P: Propaganda e Publicidade 
- RP: Recibo Pagamento Autônomo 
- U: Série Única 
- V: Nota Fiscal Avulsa 
- VT Vale Transporte 
- I: Bilhete de Ingresso 

__Regra de Preenchimento:__

__Parametrização de Modelo Msaf x Série__

Preencher com o campo Série da tela “Modelo Msaf x Série” em “Municipal > Parâmetros por Município > Parâmetros > Modelo Msaf x Série” referente ao Modelo cadastrado na nota\.

__Mensagem no Log:__

Se não existir parametrização para o modelo da nota, sistema deve exibir no log a seguinte mensagem: 

“Para o Modelo XX do Documento “NNNNNNNNNNNN \-SSS", não foi localizada a parametrização de Modelo Msaf x Série\. Efetuar a parametrização no menu Parâmetros \-\-> Modelo Msaf x Série no módulo: Parâmetros para Município\.”

Tipo: 

Tamanho:

__RN37__

__Regra do Registro Tipo D \- Campo 04 \- Modelo da NF Emitida \(de qual deve deduzir\)__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL da nota fiscal que será deduzida na tela Manutenção – Deduções\. \(mestre\)

Tipo: 

Tamanho:

__RN38__

__Regra do Registro Tipo D \- Campo 05 \- Número de identificação da NF emitida \(de qual deve deduzir\)__

Preencher com o campo Número Doc\. Fiscal da nota fiscal que será deduzida na tela Manutenção – Deduções\. \(mestre\)

Na geração deste campo, deve ser consideradas 9 posições da direita para a esquerda do número da NF, considerando que os caracteres que serão suprimidos à esquerda \(da posição 10 a 12\) devem ser zeros\. Se o conteúdo do campo NUM\_DOCFIS tiver mais de 9 posições significativas \(sem zeros à esquerda\), gerar o número truncado, mas retornar no log a seguinte mensagem: “O campo Número do Documento \(NUM\_DOCFIS\) ultrapassou o tamanho máximo permitido \(9 posições\)\.”

\(Ex para esta situação: Nº de NF 12345678900 será gerado 345678900\)\.

Tipo: 

Tamanho:

__RN39__

__Regra do Registro Tipo D \- Campo 06 \- Valor bruto da NF emitida \(de qual deve deduzir\)__

Preencher com o campo Valor Total da Nota da nota fiscal que será deduzida na tela Manutenção – Deduções\. \(mestre\)

Tipo: 

Tamanho:

__RN40__

__Regra do Registro Tipo D \- Campo 07 \- Tipo da Dedução__

Preencher fixo com ‘M’ \(Orientação do próprio “__Manual São Luís\.pdf__”\)\.

Tipo: 

Tamanho:

__RN41__

__Regra do Registro Tipo D \- Campo 08 \- Número de Identificação da NF \(a deduzir\)__

Preencher com o campo Nº Nota Fiscal da nota fiscal que será deduzida na tela Manutenção – Deduções\. \(detalhe\)

Tipo: 

Tamanho:

__RN42__

__Regra do Registro Tipo D \- Campo 09 \- Valor bruto da NF \(a deduzir\)__

Preencher com o campo Valor da Nota da nota fiscal que será deduzida na tela Manutenção – Deduções \(detalhe\)

Tipo: 

Tamanho:

__RN43__

__Regra do Registro Tipo D \- Campo 10 \- Valor do material a deduzir__

Preencher com o campo Valor Dedução da nota fiscal que será deduzida na tela Manutenção – Deduções\. \(detalhe\)

Tipo: 

Tamanho:

__RN44__

__Regra do Registro Tipo D \- Campo 11 \- CNPJ do prestador do serviço__

Preencher com o campo CGC da tabela ESTABELECIMENTO quando tiver 14 posições\.

Quando for pessoa física ou estrangeiro, preencher com zeros\.

Tipo: 

Tamanho:

__RN45__

__Regra do Registro Tipo D \- Campo 12 \- CPF do prestador do serviço__

Preencher com o campo CGC da tabela ESTABELECIMENTO quando tiver 11 posições\.

Quando for pessoa jurídica ou estrangeiro, preencher com zeros\.

Tipo: 

Tamanho:

__RN46__

__Regra do Registro Tipo D \- Campo 13 \- Nome do prestador do serviço__

Preencher com o campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO 

Tipo: 

Tamanho:

__RN47__

__Regra do Registro Tipo D \- Campo 14 \- Código SIAFI do município do tomador de serviços__

Preencher com o campo COD\_MUNIC\_SIAFI da tabela PRT\_MUNIC\_SIAFI referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR referente ao campo Pessoa Fis/Jur da nota fiscal a ser deduzida\. \(campo 25 da safx04\)\. O campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR deve ser igual ao campo COD\_MUNIC\_MSAF da tabela PRT\_MUNIC\_SIAFI\. 

Gravar '9999' se a PFJ for estrangeira\.

Tipo: 

Tamanho:

__Regras de preenchimento do Registro Tipo “R” – Notas Fiscais Recebidas__

__RN41__

__Regra geral p/ Registro de Serviços Tomados__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\);
- Classificação do Documento fiscal = 2 ou 3;

ou

Classificação da nota fiscal = 9 e código do documento \(cód\_docto = ‘RPA’\);

- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência informado na tela de geração, __exceto__ quando o parâmetro “Gerar Arquivos por Data de Emissão” na tela de geração estiver marcado\.

Caso o parâmetro esteja marcado deverá ser considerado a Data de Emissão dentro do período de referência\.

- Nota não cancelada \(SITUACAO <> ‘S’\)

\-     Tratamento para Nota Eletrônica:

Nota eletrônica do próprio município da obrigação não deve ser gerada no arquivo\.

Ou seja, se a nota for eletrônica, considerá\-la geração do arquivo APENAS se o município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for __DIFERENTE__ do município do módulo selecionado para geração \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\.

A nota é eletrônica caso um dos critérios seja verdadeiro:

\- Modelo do Documento \(campo COD\_MODELO da tabela DWT\_DOCTO\_FISCAL = ‘55’\) __OU__

\- Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal\.

- Não será considerado documento sem item\.

__Falta definir o grupamento dos itens de serviço na nota para gerar um registro R__

__Considerações importantes:__

- __ \(CAMPINAS\) __Os registos devem ser agrupados pelos campos Código do Serviço \(verificar condições de geração deste campo na RN68\) e Valor da Alíquota ISS \(verificar condições de geração deste campo na RN58\)\.

MFS7444

__RN42__

__Regra do Registro Tipo R \- Campo 01 \- Tipo do Registro:__

Preencher com o texto fixo __“R”, __indicando a linha do registro\.

Tipo: Alfanumérico

Tamanho: 01 caracter

MFS7444

__RN43__

__Regra do Registro Tipo R  \- Campo 02 \- Data de retenção do ISS:__

Indica a data de retenção do ISS, quando o imposto foi retido na fonte\.

Preencher com o campo __DT\_PAGTO\_NF __da tabela DWT\_DOCTO\_FISCAL\. \(campo 175 da SAFX07\), quando pelo menos uma das opções abaixo seja verdadeira:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “__1__”\. 

__OU__

- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\.

 __OU__

- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido\.

__Se Não__

Se nenhuma das opções anteriores for verdadeira, ou se o campo __DT\_PAGTO\_NF__ estiver vazio, preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAFX07\)\.

Tipo: Data no formato __99/99/9999__

Tamanho: 10 caracteres

MFS7444

__RN43__

__Regra do Registro Tipo R \- Campo 03 \- Data de emissão da nota fiscal:__

Preencher com a Data do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAFX07\)\.

Tipo: Data no formato __99/99/9999__

Tamanho: 10 caracteres

MFS7444

__RN43__

__Regra do Registro Tipo R \- Campo 04 \- Série da Nota Fiscal:__

A lista de séries \(segundo o __“Manual São Luís\.pdf”__, tópico 3\.1\) que este campo pode assumir, carregada na __TFIX83__ \(Cadastro das Séries/Modelos das Obrigações \- PRT\_SERIE\_OBRIG\) é:

- A: Serviço 
- B: Material e Serviço 
- M1 Material e Serviço 
- P: Propaganda e Publicidade 
- RP: Recibo Pagamento Autônomo 
- U: Série Única 
- V: Nota Fiscal Avulsa 
- VT Vale Transporte 
- E: NF de Estacionamento 
- I: Bilhete de Ingresso 
- RP: RPA \- Recibo de Profissional Autônomo 
- RS: Recibo Provisório de Serviços \(RPS\) 
- OT: Outros Documentos \(Pessoa Jurídica\) 
- OM: Nota fiscal de outro município  

__Regra de Preenchimento:__

__Parametrização de Modelo Msaf x Série__

Preencher com o campo Série da tela “Modelo Msaf x Série” em “Municipal > Parâmetros por Município > Parâmetros > Modelo Msaf x Série” referente ao Modelo cadastrado na nota\.

__Mensagem no Log:__

Se não existir parametrização para o modelo da nota, sistema deve exibir no log a seguinte mensagem: 

“Para o Modelo XX do Documento “NNNNNNNNNNNN \-SSS", não foi localizada a parametrização de Modelo Msaf x Série\. Efetuar a parametrização no menu Parâmetros \-\-> Modelo Msaf x Série no módulo: Parâmetros para Município\.”

Tipo: Alfanumérico

Tamanho: 02 caracteres

MFS7444

__RN44__

__Regra do Registro Tipo R \- Campo 05 – Modelo da nota fiscal:__

<a id="OLE_LINK9"></a><a id="OLE_LINK10"></a><a id="OLE_LINK11"></a>Preencher com espaços em branco\. Orientação no “__Manual Importação DIM\.pdf__”, tópico 4\.2 – Relação de Modelos

Tipo: Alfanumérico 

Tamanho: 01 caracteres

__Tentar confirmar com a prefeitura\.__

\[Alteração MFS\-30540\] Preencher com o texto fixo ‘U’ 

MFS7444

MFS30540

__RN44__

__Regra do Registro Tipo R \- Campo 06 \- Motivo da Retenção / Não Retenção __

Preencher com espaço em branco\.  Orientação do próprio “__Manual São Luís\.pdf__”\.

Tipo: Alfanumérico 

Tamanho: 01 caracteres

MFS7444

__RN49__

__Regra do Registro Tipo R \- Campo 07 \- Número de Identificação da Nota Fiscal:__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. \(campo 08 da SAFX07\)\.

__Considerações:__

- Se for gerado apenas o NUM\_DOCFIS, devem ser consideradas 9 posições da direita para a esquerda do número da NF, considerando que os caracteres que serão suprimidos à esquerda \(da posição 10 a 12\) devem ser zeros\. 

Se o conteúdo do campo NUM\_DOCFIS tiver mais de 9 posições significativas \(sem zeros à esquerda\), gerar o número truncado, mas retornar no log a seguinte mensagem: 

“O campo Número do Documento \(NUM\_DOCFIS\) ultrapassou o tamanho máximo permitido \(9 posições\)\.”

\(Ex\.: para esta situação: Nº de NF 12345678900 será gerado 345678900\)\. Tipo: Numérico

Tipo: Numérico

Tamanho: 09 caracteres

MFS7444

__RN50__

__Regra do Registro Tipo R \- Campo 08 \- Valor Bruto da Nota Fiscal:__

Se o campo COD\_CLASS\_DOC\_FIS da tabela DWT\_DOCTO\_FISCAL = ‘2’

      Preencher com o somatório do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\. 

Se o campo COD\_CLASS\_DOC\_FIS da tabela DWT\_DOCTO\_FISCAL = ‘3’

      Preencher com o campo VLR\_TOT\_NOTA da tabela DWT\_DOCTO\_FISCAL

Tipo: Numérico

Tamanho: Valor com 15 posições \(999999999999\.99\)

MFS7444

__RN51__

__Regra do Registro Tipo R \- Campo 09 \- Valor do Serviço lançado na nota fiscal recebida:__

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. 

Tipo: Numérico

Tamanho: Valor com 15 posições \(999999999999\.99\)

MFS7444

__RN52__

__Regra do Registro Tipo R \- Campo 10 \- Alíquota de ISS:__

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 32 da SAFX09\), quando pelo menos uma das opções abaixo seja verdadeira:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado 

__OU __

- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado 

__OU__

- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Caso nenhumas das opções acima sejam verdadeiras, preencher com zeros\.

Tipo: Numérico

Tamanho: Valor com __05 __posições com zeros a esquerda com ponto\. 

Exemplo: 5,00% = 05\.00 ou 2,75% = 02\.75

MFS7444

__RN52__

__Regra do Registro Tipo R \- Campo 11 \- Número da Parcela de Pagamento da NF:__

Preencher com zeros\. Orientação do próprio “__Manual São Luís\.pdf__”\.

Tipo: Numérico

Tamanho: __06 __caracteres

MFS7444

__RN52__

__Regra do Registro Tipo R \- Campo 12 \- Quantidade da Parcela de Pagamento da NF:__

Preencher com zeros\. Orientação do próprio “__Manual São Luís\.pdf__”\.

Tipo: Numérico

Tamanho: __06 __caracteres

MFS7444

__RN52__

__Regra do Registro Tipo R \- Campo 13 \- Motivo da não retenção:__

Preencher com espaço em branco\.  Orientação do próprio “__Manual São Luís\.pdf__”\.

Tipo: Alfanumérico 

Tamanho: 30 caracteres

MFS7444

__      RN62__

__Regra do Registro Tipo R \- Campo 14 \- CNPJ do prestador do serviço: __

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR quando o tamanho do campo for igual a 14\. \(campo 06 da SAFX04\)

Se o campo tiver 11 posições ou o tomador for estrangeiro, preencher com zeros\. Orientação do próprio “__Manual São Luís\.pdf__”\.

Tipo: Numérico

Tamanho: 14 caracteres

__     RN63__

__Regra do Registro Tipo R \- Campo 15 \- CPF do prestador do serviço:__ 

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR quando o tamanho do campo for igual a 11\. \(campo 06 da SAFX04\)

Se o campo tiver 14 posições ou o tomador for estrangeiro, preencher com zeros\. Orientação do próprio “__Manual São Luís\.pdf__”\.

Tipo: Numérico

Tamanho: 11 caracteres

__RN64__

__Regra do Registro Tipo R \- Campo 16 \- Nome do prestador do serviço: __

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\. \(campo 05 da SAFX04\)

Tipo: Alfanumérico 

Tamanho: 40 caracteres

__      RN65__

__Regra do Registro Tipo R \- Campo 17 \- Código SIAFI do município do prestador do serviço: __

Preencher com o campo COD\_MUNIC\_SIAFI da tabela PRT\_MUNIC\_SIAFI referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\. \(campo 25 da safx04\)\. O campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR deve ser igual ao campo COD\_MUNIC\_MSAF da tabela PRT\_MUNIC\_SIAFI\. 

Se prestador for estrangeiro usar “9999” e não informar CPF ou CNPJ\. Orientação do próprio “__Manual São Luís\.pdf__”\.

Tipo: Alfanumérico 

Tamanho: 10 caracteres

__      RN66__

__Regra do Registro Tipo R \- Campo 18 \- Enquadramento no Simples Nacional do prestador: __

Preencher com o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR\. \(campo 43 da SAFX04\)

Tipo: Alfanumérico 

Tamanho: 1 caracter

     __RN68__

__Regra do Registro Tipo R \- Campo 19 \- Código do serviço prestado:__

A lista de Serviços \(segundo o __“Manual Importação DIM\.pdf”__, tópico 4\.7 ?\) que este campo pode assumir, carregada na __TFIX85__ \(Cadastro de Códigos de Serviços Municipais \- PRT\_SERVICO\_OBRIG\) é:

__Regra de Preenchimento:__

__Parametrização de Serviços Msaf x Serviços__

Preencher com o campo Serviço da tela “Serviços Msaf x Serviços” em “Municipal > Parâmetros por Município > Parâmetros > Serviços Msaf x Serviços” referente ao Serviço cadastrado na nota\.

O campo deverá ser gerado sem o separador \(ponto\) e alinhado à esquerda com as demais posições preenchidas com espaço\.

Preencher com brancos à direita até completar o tamanho do campo\.

__Mensagem no Log:__

Se não existir parametrização para o serviço do item da nota, sistema deve exibir no log a seguinte mensagem: 

“Para o Serviço XX do Documento “NNNNNNNNNNNN \-SSS", não foi localizada a parametrização de Serviço Msaf x Serviço\. Efetuar a parametrização no menu Parâmetros \-\-> Serviço Msaf x Serviço no módulo: Parâmetros para Município\.”

Tipo: Alfanumérico 

Tamanho: 10 caracteres

__Verificar com a prefeitura__

__RN69__

__Regra do Registro Tipo R \- Campo 20 \- Código SIAFI do município do local da prestação do serviço: __

Esse campo será preenchido com o campo COD\_MUNIC\_SIAFI da tabela PRT\_MUNIC\_SIAFI referente ao campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\. 

Caso o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL não esteja preenchido, esse campo será preenchido com o campo COD\_MUNIC\_SIAFI da tabela PRT\_MUNIC\_SIAFI referente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\. 

*Obs\.: O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS\.*

Tipo: Alfanumérico 

Tamanho: 10 caracteres

__RN70__

__Regra do Registro Tipo R \- Campo 21 \- Operação da nota fiscal recebida \(Demais Municípios\): __

A – Sem Dedução 

B – Com Dedução/Materiais 

C – Imune/Isenta de ISSQN 

D – Devolução/Simples Remessa 

J – Intermediação 

Preencher com:

D, quando o campo NORM\_DEV da tabela DWT\_DOCTO\_FISCAL = ‘2’ \(campo 04 da SAFX07\)

B, quando o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV > 0\.

C, verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07” ou “10”, se não estiver preenchido verificar se o serviço e o município da pessoa fis/jur cadastrados na nota está parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420” ou “433”\.

A, quando o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV = 0 ou quando não estiver preenchido\. \(campo 190 da SAFX07\)

J – Intermediação: não será tratado na MFS7444\.

Tipo: Alfanumérico 

Tamanho: 1 caractere

__RN70\.e__

__Regra do Registro Tipo R \- Campo 22 \- CPF/CNPJ do Cliente:__

Preencher com o campo CGC da tabela ESTABELECIMENTO\.

Tipo: Numérico

Tamanho: 14 caracteres

Considerações deste modelo:

__Quando uma Regra de Negócio for excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo descrita abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo descrita abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


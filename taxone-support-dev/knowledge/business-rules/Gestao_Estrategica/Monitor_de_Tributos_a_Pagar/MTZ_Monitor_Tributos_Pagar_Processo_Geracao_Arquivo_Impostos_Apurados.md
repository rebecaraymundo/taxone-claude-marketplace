# MTZ_Monitor_Tributos_Pagar_Processo_Geracao_Arquivo_Impostos_Apurados

- **Fonte:** MTZ_Monitor_Tributos_Pagar_Processo_Geracao_Arquivo_Impostos_Apurados.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 91 KB

---

THOMSON REUTERS

Monitor de Tributos

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3962\-A

Definição dos Processos de geração do arquivo através do Monitor de Tributos

Possibilitar a geração do arquivo conforme layout definido pelo usuário;

Armazenar as informações para controle de status dos arquivos gerados;

Gerar informações que permitam a rastreabilidade das informações geradas\.

OS3962\-B

Definição dos Processos de geração do arquivo através do Monitor de Tributos

Possibilitar a geração do arquivo a partir do layout definido pelo usuário contendo as informações dos tributos federais gerados nos DARF’s\.

OS3962\-C

Definição dos Processos de geração do arquivo através do Monitor de Tributos 

Inclusão da opção “Previdenciário” no campo “Grupo Tributo” e da opção “INSS” no campo “Tributo da tela de parametrização de layout, além da alteração do processo de geração\.

OS3962\-D

Definição dos Processos de geração do arquivo através do Monitor de Tributos

O objetivo deste documento de requisito é definir a solução funcional para a geração dos arquivos de retorno ao ERP realizados pelo módulo Monitor de Tributos, no formato XML\. Atualmente, essa geração ocorre somente no formato texto\.

A geração deverá abranger os tributos especificados nas OS’s da família 3962, especificamente das autarquias Federal, Previdenciário e Municipal\. Os tributos relacionados ao fisco Estadual não fazem parte do escopo dessa OS\.

MFS\-1687

Inclusão dos novos impostos no processo de geração\.

Inclusão dos tributos ICMS, ICMS\-ST, IPI, PIS/PASEP \(Próprio\) e Cofins \(Próprio\) no processo de geração do arquivo\.

MFS\-1688

Definição do processo de armazenamento dos dados gerados\.

Ao gerar o arquivo de tributos os dados serão armazenados em uma tabela\.

MFS\-2832

Filtro dos impostos no processo de geração

Considerar o filtro de seleção de tela para geração dos impostos federais apurados e alteração na nomenclatura do arquivo\.

MFS\-5046

Alteração no status do arquivo gerado

Se a geração for realizada para mais de um estabelecimento o campo estabelecimento na tela de status deverá apresentar a palavra “Consolidado”\.

MFS\-6310

Alteração na recuperação dos valores para o tributo IPI

Alteração do no filtro na busca do valor da apuração do tributo IPI\.

MFS\-6310

Alteração geração do tributo ICMS

Retirado os impostos ICMS e ICMS\-ST do processo de geração do arquivo de Impostos Apurados\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral__

O Processo de Geração do Arquivo de Tributos Apurados foi criado com as seguintes finalidades:

- Gerar o arquivo TXT ou XML conforme layout definido pelo usuário para determinado tributo \(RN01\);
- Alimentar a tela de Status dos Arquivos Gerados \(RN02\);
- Gerar identificador nas tabelas de origem da informação que vão permitir a rastreabilidade do que foi demonstrado no arquivo \(RN03\)\.

Estes processos serão executados através da tela de Arquivo de Tributos Apurados \(Monitor de Tributos, menu Geração > Arquivo de Tributos Apurados\)\.

OS3962\-A

OS3962\-D

RN01

__Regras de Geração do Arquivo TXT__

O arquivo txt deve ser gerado conforme layout definido pelo usuário na tela de Parametrização do Layout \(Monitor de Tributos, menu Parâmetros > Parametrização do Layout\), considerando como origem da informação a tabela vinculada ao tributo\*, considerando os Parâmetros de seleção indicados pelo usuário na Parametrização do Layout e os parâmetros fixos, que estarão na tela de Geração do Arquivo de Tributos Apurados, que são empresa \(a logada\), estabelecimento e período\. 

Na Parametrização do Layout o usuário deverá indicar qual data será utilizada como critério de seleção\. Na geração, além dos critérios definidos pelo usuário como Parâmetros de Seleção, serão considerados os registros para a empresa \(logada\) e estabelecimento selecionado, no formato definido no layout\.

Não deverão ser considerados na seleção das informações da tabela origem os registros que já foram gerados em outro momento, ou seja, aqueles que já têm os identificadores de geração preenchidos conforme critérios definidos na RN03\.

Para o Tributo ISS, devem ser considerados apenas os registros que atenderam aos critérios de seleção e que tenham sido apurados em um período cujo Status do Fechamento do ISS esteja como “Fechado”\.

Caso o usuário escolha o Grupo Tributo = Federal e um dos Tributos informados \(IRPJ, IRRF, CSLL, PIS/PASEP e COFINS\), a geração deverá recuperar os seguintes tributos mantidos nos DARF’s:

- Campo Tributo = 01 – IRPJ
- Campo Tributo = 02 – IRRF
- Campo Tributo = 05 – CSLL
- Campo Tributo = 06 – PIS/PASEP
- Campo Tributo = 07 – COFINS

Serão considerados para os tributos IRPJ, IRRF, PIS/PASEP, COFINS e CSLL, os registros da tabela de manutenção dos DARF’s \(menu: Outras Obrigações >> DARF’s >> Manutenção\), ou seja, da tabela X75\_DCTF ou X751\_DCTF\_COMPL\. A recuperação de informações dessa tabela será da seguinte maneira:

- Caso exista 1 \(um\) registro na tabela X75\_DCTF:
	- Recuperar o registro da tabela X75\_DCTF\.
- Caso exista 1 \(um\) registro na tabela X75\_DCTF e 1 \(um\) registro na tabela X751\_DCTF\_COMPL:
	- Recuperar o registro da X751\_DCTF\_COMPL que possui identificador de Débito;
- Caso exista 1 \(um\) registro na tabela X75\_DCTF e mais de 1 \(um\) registro na tabela X751\_DCTF\_COMPL:
	- Recuperar esse registro mais recente da X751\_DCTF\_COMPL que possui o identificador de Débito;

Deverão ser considerados somente os DARF’s com status diferente de “Pago”\.

Para filtro dos tributos deverá levar em consideração a regra de seleção da tela “Arquivo de Tributos Apurados”\.

IPI: 

Deverão ser recuperados os registros da tabela ITEM\_APURAC\_CALC \(Módulo: Federal >> IPI Menu: DATA MART >> apuração do IPI\) quando campo COD\_TIPO\_LIVRO = 002 e COD\_OPER\_APUR = 016

PIS/PASEP \(Próprio\): 

Deverão ser recuperados os registros da tabela EPC\_REG\_AJT\_M200\_M600 \(SPED >> EFD \- Contribuições >> Obrigações >> Manutenção >> Apuração PIS/PASEP\) – de acordo com os critérios de seleção, quando código do registro M200\.

COFINS \(Próprio\):

Deverão ser recuperados os registros da tabela EPC\_REG\_AJT\_M200\_M600 \(SPED >> EFD \- Contribuições >> Obrigações >> Manutenção >> COFINS\) – de acordo com os critérios de seleção, quando código do registro M600\.

\[Alterada MFS\-6310\]

INSS: 

Deverão ser recuperados os registros da tela “Consolidação das Retenções” \(menu: Outras Obrigações >> Retenções de INSS – Serviços Prestados >> Manutenção da Consolidação das Retenções\) – tabela: IRT\_GPS – de acordo com o critério de data informada, que deverá recuperar a partir do Mês/Ano de Competência\.

Os registros que estiverem fora dos critérios informados para recuperação não serão gerados no arquivo de retorno do ERP\.

- Sobre o agrupamento das informações na geração:

Os campos numéricos indicados pelo usuário no layout como “Agrupado” devem ser somados na geração do arquivo e os campos alfanuméricos ou numéricos que não tenham sido selecionados, serão agrupados para demonstração da informação consolidada\.

__Exemplo__:

Na Parametrização do Layout teremos:

__Agrupado__

__Ordem__

__Descrição__

__Tipo__

__Conteúdo Variável__

01

Código do Município

Alfanumérico

Campo Código do Município da tabela origem

02

Código do Serviço

Alfanumérico

Campo Código do Serviço da tabela origem

03

Data do Pagamento

DATA\(DDMMAAAA\)

Campo Data do Pagamento da tabela origem

SIM

04

BC do ISS

Numérico

Campo BC do ISS da tabela origem

05

Alíquota do ISS

Numérico

Campo Alíquota do ISS da tabela origem

SIM

06

Valor do ISS

Numérico

Campo Valor do ISS da tabela origem

SIM

07

Valor Contábil

Numérico

Campo Valor Contábil da tabela origem

Na tabela origem teremos:

__Código do Município__

__Código do Serviço__

__Código do Prestador__

__Data do Pagamento__

__BC do ISS__

__Alíquota do ISS__

__Valor do ISS__

__Valor Contábil__

35038

1701

XPTO

15/02/2013

1000,00

7,00

70,00

1000,00

35038

1701

XYZ

15/02/2013

1000,00

7,00

70,00

1000,00

35038

1701

XPTO

15/02/2013

1000,00

7,00

70,00

1000,00

35038

1702

XYZ

16/02/2013

1000,00

7,00

70,00

1000,00

35039

1701

XYZ

15/02/2013

1000,00

7,00

70,00

1000,00

No arquivo nós teremos:

__Código do Município__

__Código do Serviço__

__Data do Pagamento__

__BC do ISS__

__Alíquota do ISS__

__Valor do ISS__

__Valor Contábil__

35038

1701

15/02/2013

3000,00

7,00

210,00

3000,00

35038

1702

16/02/2013

1000,00

7,00

70,00

1000,00

35039

1701

15/02/2013

1000,00

7,00

70,00

1000,00

- Sobre o nome do arquivo gerado e quebras no arquivo:

Por padrão, deverá ser gerado um arquivo por layout selecionado, considerando a seguinte nomenclatura:

COD\-LAYOUT\_GPO\-TRIBUTO\_TRIBUTO\_DT\-INICIO\_DT\-FIM\.txt, onde:

             ID\_GER = ID de Geração dos arquivos

             COD\_TIPO\_ARQ = Código do Tipo do Arquivo

COD\-LAYOUT = código do layout selecionado;

GPO\-TRIBUTO = grupo tributo vinculado ao layout \(ex\.: FEDERAL, MUNICIPAL, etc\);

TRIBUTO = tributo vinculado ao layout \(ex\.: IRPJ, ISS, etc\);

DT\-INICIO = Data Inicial parametrizada na geração;

DT\-FIM = Data Final parametrizada na geração;

\.txt = extensão do arquivo

Neste formato, será gerado um único arquivo consolidando as informações de todos os estabelecimentos selecionados pelo usuário e que tiveram os critérios de seleção do layout atendidos\.

Caso, na geração, o usuário selecione o parâmetro “Realizar a quebra de arquivo por Estabelecimento”, deve ser gerado um arquivo por layout e estabelecimento selecionado, considerando a seguinte nomenclatura:

COD\-ESTAB\_COD\-LAYOUT\_GPO\-TRIBUTO\_TRIBUTO\_DT\-INICIO\_DT\-FIM\.txt, onde:

             ID\_GER = ID de Geração dos arquivos

             COD\_TIPO\_ARQ = Código do Tipo do Arquivo

COD\-ESTAB = código do estabelecimento selecionado;

COD\-LAYOUT = código do layout selecionado;

GPO\-TRIBUTO = grupo tributo vinculado ao layout \(ex\.: FEDERAL, MUNICIPAL, etc\);

TRIBUTO = tributo vinculado ao layout \(ex\.: IRPJ, ISS, etc\);

DT\-INICIO = Data Inicial parametrizada na geração;

DT\-FIM = Data Final parametrizada na geração;

\.txt = extensão do arquivo

Neste formato, será gerado um arquivo para cada estabelecimento selecionado pelo usuário e que tiveram os critérios de seleção do layout atendidos\.

Se o critério de seleção não for atendido para algum layout selecionado, não deve ser gerado arquivo\. Haverá mensagem no log\.

- Mensagens para o LOG:

Caso para algum layout o critério de seleção não seja atendido, retornar a seguinte mensagem no log: “Não existem registros que se enquadram nos critérios de seleção para o Layout: <COD\-LAYOUT>, <COD\-ESTAB>, <GPO\-TRIBUTO>, <TRIBUTO>, <DT\-INICIO> e <DT\-FIM>

Caso tenha sido indicado para geração um arquivo para tributo “ISS” e que na tabela do Gerenciador o Status do Fechamento do ISS esteja diferente de “Fechado”, retornar mensagem no log: “Não existem registros com período Fechado para o ISS: <COD\-LAYOUT>, <COD\-ESTAB>, <GPO\-TRIBUTO>, <TRIBUTO>, <DT\-INICIO> e <DT\-FIM>”

__*\*Relação Tributo X Tabela*__

__Tributo__

__Tabela__

ISS

Fechamento do ISS – Gerenciador do ISS

IRPJ

Manutenção de DARF’s – Obrigações de Tributos Federais

IRRF

Manutenção de DARF’s – Obrigações de Tributos Federais

PIS/PASEP

Manutenção de DARF’s – Obrigações de Tributos Federais

COFINS

Manutenção de DARF’s – Obrigações de Tributos Federais

CSLL

Manutenção de DARF’s – Obrigações de Tributos Federais

IPI

IPI >> DATA MART >> Apuração do IPI

PIS/PASEP \(Próprio\)

SPED >> EFD – Contribuições >> Obrigações >> Manutenção >> Apuração PIS/PASEP

COFINS \(Próprio\)

SPED >> EFD – Contribuições >> Obrigações >> Manutenção >> Apuração COFINS

 

OS3962\-A

OS3962\-B

MFS\-1687

MFS\-2832

MFS\-1689

MFS\-6310

RN02

__Geração do Status dos Arquivos Gerados__

A partir da geração do arquivo deverão ser criados registros para o Status dos Arquivos Gerados\.

Será gerada a informação somente se houver arquivo gerado para os critérios de Estabelecimento, Data Inicial, Data Final, Grupo Tributo, Tributo e Código do Layout, considerando as seguintes regras para composição da informação:

__Campo__

__Regra__

Estabelecimento

Será criado com o código do estabelecimento selecionado na geração, se houver geração para mais de um estabelecimento deverá ser apresentada a palavra “Consolidado”

Data Inicial

Será criado com a Data Inicial informada na geração\.

Data Final

Será criado com a Data Final informada na geração\.

Grupo Tributo

Será criado com o Grupo Tributo vinculado ao layout\.

Tributo

Será criado com o Tributo vinculado ao layout\.

Código do Layout

Será criado com o código do layout\.

Lote

Será criada uma numeração sequencial por arquivo gerado\.

ID Geração

ID de geração do arquivo

Status

Será gerado com a opção “1 – Enviado”

 

OS3962\-A

MFS\-5046

RN03

__Geração dos Identificadores na Origem__

Deverá ser criada nas tabelas de origem da informação para geração do arquivo a possibilidade de identificar quando um determinado registro foi gerado no arquivo, com os seguintes critérios: Estabelecimento, Data Inicial, Data Final, Grupo Tributo, Tributo, Código do Layout e Lote\.

Esta identificação deve ser preenchida no registro que foi considerado na origem momento da geração do arquivo para que seja possível identificar em qual momento a informação foi gerada, possibilitando a rastreabilidade da informação e identificação de um registro já gerado\.

Esse identificador de origem deve ser criado para qualquer origem de qualquer tributo – Federal, Municipal ou Previdenciário, conforme descrição das tabelas abaixo:

- ISS = GPE\_FECHAMENTO\_ISS
- IRPJ, IRRF, PIS/PASEP, COFINS ou CSLL = X75\_DCTF ou X751\_DCTF\_COMPL
- INSS = IRT\_GPS
- IPI = ITEM\_APURAC\_CALC
- PIS/PASEP \(Próprio\) = EPC\_REG\_AJT\_M200\_M600 \(Registro M200\)
- COFINS \(Próprio\) = EPC\_REG\_AJT\_M200\_M600 \(Registro M600\)

Para cada geração do arquivo, esse identificador será atualizado\.

OS3962\-A

OS3962\-C

OS3962\-D

MFS\-1687

RN04

Conforme RN03, caso o DARF da tabela X75\_DCTF ou X751\_DCTF\_COMPL, possua o identificador preenchido, o sistema não irá permitir a exclusão desse DARF via tela de manutenção \(menu: Outras Obrigações >> DARF’s >> Manutenção\) ou via reprocessamento do DARF via tela de geração com o parametro “Não Excluir DARF’s” desmarcado\. Será exibida a mensagem de erro: “Não é permitida a exclusão de DARF’s que possuem Número de Lote e que ainda não retornaram do ERP”\.

Embora não seja permitida a exclusão desse DARF via tela de manutenção ou via reprocessamento dos DARF’s, o sistema permitirá que os campos “Data Pagamento”, “Observação”\. “Envio Bancário” e “Autenticação Bancária” possam ser preenchidos\. Para que o usuário possa excluir o DARF, o mesmo deverá cancelar primeiramente o lote e depois excluir o DARF\.

OBS: as regras acima estão detalhadas logo abaixo na tabela:

__Critérios de Aceitação__:

__Situação__

__Resultado Esperado__

Exclusão do DARF com status “Em Aberto” com identificador informado

Será semelhante aos DARF’s pagos, onde não será permitido a exclusão do DARF e será exibida mensagem de erro “Não é permitida a exclusão de DARF’s que possuem Número de Lote e que ainda não retornaram do ERP\.”\.

Será permitida a alteração dos campos “Data Pagamento”, “Observação”\. “Envio Bancário” e “Autenticação Bancária”\.

Reprocessamento do DARF com identificador informado e com parâmetro “Não excluir DARF’s” selecionado

Só serão consideradas as retenções novas

Reprocessamento do DARF com identificador informado e com parâmetro “Não excluir DARF’s” desmarcado

Só serão excluídos os DARF’s e reprocessados os DARF’s que não possuem identificador preenchido\. Para os outros será exibida mensagem de erro no log de erros: “Não é permitida a exclusão de DARF’s que possuem Número de Lote e que ainda não retornaram do ERP\.”\.Junto ao log de erros será exibida a chave da tabela X75\_DCTF ou X751\_DCTF\_COMPL\.

OS3962\-B

RN05

Caso um DARF da X75\_DCTF ou X751\_DCTF\_COMPL possua créditos vinculados à ele – ou seja, tenham sido gerados por esse DARF – o saldo desse DARF não poderá ser utilizado para compensação caso o DARF esteja com status “Em Aberto” e possua um identificador\.

Esse crédito só poderá ser utilizado caso o DARF já tenha sido pago\.

OS3962\-B

RN06

Caso seja dada uma seleção válida de período, layout e estabelecimento, analisar os registros marcados na tabela de origem \(considerando que não ocorreu fechamento do período\)\. Nesse caso, deve ser exibida uma mensagem de erro no log: “Não existe Fechamento para o ISS no período parametrizado: <COD\-EMPRESA>, <COD\-ESTAB>, <GPO\-TRIBUTO>, <TRIBUTO>, <DT\-INICIO> e <DT\-FIM>”\.

OS3962\-A

RN07

Caso seja dada uma seleção válida de período, layout e estabelecimento, analisar os registros marcados na tabela de origem \(considerando que não foram encontrados registros que atendam aos filtros do layout em processamento\)\. Nesse caso, deve ser exibida uma mensagem de erro no log: “Não existem registros que se enquadram nos critérios de seleção para o Layout: <COD\-LAYOUT>, <COD\-ESTAB>, <GPO\-TRIBUTO>, <TRIBUTO>, <DT\-INICIO> e <DT\-FIM>”

OS3962\-A

RN08

Conforme RN03, caso a retenção de INSS da tabela IRT\_GPS possua o identificador preenchido, o sistema não irá permitir a exclusão da mesma via tela de manutenção \(menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> GPS >> Digitação\) ou via reprocessamento da GPS  via tela de geração \(menu: Outras Obrigações >> Retenção de INSS – Serviços Prestados >> Geração de Retenções de INSS\)\. Nesse caso, será exibida a mensagem de erro: “Não é permitida a exclusão de GPS’s que possuem Número de Lote e que ainda não retornaram do ERP”\.

Para que o usuário possa excluir a GPS, o mesmo deverá cancelar primeiramente o lote e depois excluir a GPS\.

OS3962\-C

RN09

__Regras de Geração do Arquivo XML__

O arquivo XML deve ser gerado conforme layout definido pelo usuário na tela de Parametrização do Layout XML\(Monitor de Tributos, menu Parâmetros > Layout do arquivo XML\), considerando como origem da informação a tabela vinculada ao tributo\*, considerando os Parâmetros de seleção indicados pelo usuário na Parametrização do Layout XML e os parâmetros fixos, que estarão na tela de Geração do Arquivo de Tributos Apurados, que são empresa \(a logada\), estabelecimento e período\.

Na Parametrização do Layout XML o usuário deverá indicar qual data será utilizada como critério de seleção\. Na geração, além dos critérios definidos pelo usuário como Parâmetros de Seleção, serão considerados os registros para a empresa \(logada\) e estabelecimento selecionado, no formato definido no layout\.

Não deverão ser considerados na seleção das informações da tabela origem os registros que já foram gerados em outro momento, ou seja, aqueles que já têm os identificadores de geração preenchidos conforme critérios definidos na regra de Geração de Identificadores na Origem\.

Para o Tributo ISS, devem ser considerados apenas os registros que atenderam aos critérios de seleção e que tenham sido apurados em um período cujo Status do Fechamento do ISS esteja como “Fechado”\.

Caso o usuário escolha o Grupo Tributo = Federal e um dos Tributos informados \(IRPJ, IRRF, CSLL, PIS/PASEP e COFINS\), a geração deverá recuperar os seguintes tributos mantidos nos DARF’s:

- Campo Tributo = 01 – IRPJ
- Campo Tributo = 02 – IRRF
- Campo Tributo = 05 – CSLL
- Campo Tributo = 06 – PIS/PASEP
- Campo Tributo = 07 – COFINS

Serão considerados para os tributos IRPJ, IRRF, PIS/PASEP, COFINS e CSLL, os registros da tabela de manutenção dos DARF’s \(menu: Outras Obrigações >> DARF’s >> Manutenção\), ou seja, da tabela X75\_DCTF ou X751\_DCTF\_COMPL\. A recuperação de informações dessa tabela será da seguinte maneira:

- Caso exista 1 \(um\) registro na tabela X75\_DCTF:
	- Recuperar o registro da tabela X75\_DCTF\.
- Caso exista 1 \(um\) registro na tabela X75\_DCTF e 1 \(um\) registro na tabela X751\_DCTF\_COMPL:
	- Recuperar o registro da X751\_DCTF\_COMPL que possui identificador de Débito;
- Caso exista 1 \(um\) registro na tabela X75\_DCTF e mais de 1 \(um\) registro na tabela X751\_DCTF\_COMPL:
	- Recuperar esse registro mais recente da X751\_DCTF\_COMPL que possuei o identificador de Débito;

Deverão ser considerados somente os DARF’s com status diferente de “Pago”\.

Para filtro dos tributos deverá levar em consideração a regra de seleção da tela “Arquivo de Tributos Apurados”\.

IPI: 

Deverão ser recuperados os registros da tabela ITEM\_APURAC\_CALC \(Módulo: Federal >> IPI Menu: DATA MART >> apuração do IPI\) quando campo COD\_TIPO\_LIVRO = 002 e COD\_OPER\_APUR = 016

PIS/PASEP \(Próprio\): 

Deverão ser recuperados os registros da tabela EPC\_REG\_AJT\_M200\_M600 \(SPED >> EFD \- Contribuições >> Obrigações >> Manutenção >> Apuração PIS/PASEP\) – de acordo com os critérios de seleção, quando código do registro M200\.

COFINS \(Próprio\):

Deverão ser recuperados os registros da tabela EPC\_REG\_AJT\_M200\_M600 \(SPED >> EFD \- Contribuições >> Obrigações >> Manutenção >> COFINS\) – de acordo com os critérios de seleção, quando código do registro M600\.

INSS: 

Deverão ser recuperados os registros da tela “Consolidação das Retenções” \(menu: Outras Obrigações >> Retenções de INSS – Serviços Prestados >> Manutenção da Consolidação das Retenções\) – tabela: IRT\_GPS – de acordo com o critério de data informada, que deverá recuperar a partir do Mês/Ano de Competência\.

Os registros que estiverem fora dos critérios informados para recuperação não serão gerados no arquivo de retorno do ERP\.

- Sobre o agrupamento das informações na geração:

Os campos numéricos indicados pelo usuário no layout como “Agrupado” devem ser somados na geração do arquivo e os campos alfanuméricos ou numéricos que não tenham sido selecionados, serão agrupados para demonstração da informação consolidada\.

- Sobre o nome do arquivo gerado e quebras no arquivo:

Por padrão, deverá ser gerado um arquivo por layout selecionado, considerando a seguinte nomenclatura:

COD\-LAYOUT\_GPO\-TRIBUTO\_TRIBUTO\_DT\-INICIO\_DT\-FIM\.txt, onde:

             

             ID GER = ID de Geração do Arquivo

             COD\_TIPO\_ARQ = Código do Tipo do Arquivo

COD\-LAYOUT = código do layout selecionado;

GPO\-TRIBUTO = grupo tributo vinculado ao layout \(ex\.: FEDERAL, MUNICIPAL, etc\);

TRIBUTO = tributo vinculado ao layout \(ex\.: IRPJ, ISS, etc\);

DT\-INICIO = Data Inicial parametrizada na geração;

DT\-FIM = Data Final parametrizada na geração;

\.xml = extensão do arquivo

Neste formato, será gerado um único arquivo consolidando as informações de todos os estabelecimentos selecionados pelo usuário e que tiveram os critérios de seleção do layout atendidos\.

Caso, na geração, o usuário selecione o parâmetro “Realizar a quebra de arquivo por Estabelecimento”, deve ser gerado um arquivo por layout e estabelecimento selecionado, considerando a seguinte nomenclatura:

COD\-ESTAB\_COD\-LAYOUT\_GPO\-TRIBUTO\_TRIBUTO\_DT\-INICIO\_DT\-FIM\.txt, onde:

             ID GER = ID de Geração do Arquivo

             COD\_TIPO\_ARQ = Código do Tipo do Arquivo

COD\-ESTAB = código do estabelecimento selecionado;

COD\-LAYOUT = código do layout selecionado;

GPO\-TRIBUTO = grupo tributo vinculado ao layout \(ex\.: FEDERAL, MUNICIPAL, etc\);

TRIBUTO = tributo vinculado ao layout \(ex\.: IRPJ, ISS, etc\);

DT\-INICIO = Data Inicial parametrizada na geração;

DT\-FIM = Data Final parametrizada na geração;

\.xml = extensão do arquivo

Neste formato, será gerado um arquivo para cada estabelecimento selecionado pelo usuário e que tiveram os critérios de seleção do layout atendidos\.

Se o critério de seleção não for atendido para algum layout selecionado, não deve ser gerado arquivo\. Haverá mensagem no log\.

- Mensagens para o LOG:

Caso para algum layout o critério de seleção não seja atendido, retornar a seguinte mensagem no log: “Não existem registros que se enquadram nos critérios de seleção para o Layout: <COD\-LAYOUT>, <COD\-ESTAB>, <GPO\-TRIBUTO>, <TRIBUTO>, <DT\-INICIO> e <DT\-FIM>

Caso tenha sido indicado para geração um arquivo para tributo “ISS” e que na tabela do Gerenciador o Status do Fechamento do ISS esteja diferente de “Fechado”, retornar mensagem no log: “Não existem registros com período Fechado para o ISS: <COD\-LAYOUT>, <COD\-ESTAB>, <GPO\-TRIBUTO>, <TRIBUTO>, <DT\-INICIO> e <DT\-FIM>”

__*\*Relação Tributo X Tabela*__

__Tributo__

__Tabela__

ISS

Fechamento do ISS – Gerenciador do ISS

IRPJ

Manutenção de DARF’s – Obrigações de Tributos Federais

IRRF

Manutenção de DARF’s – Obrigações de Tributos Federais

PIS/PASEP

Manutenção de DARF’s – Obrigações de Tributos Federais

COFINS

Manutenção de DARF’s – Obrigações de Tributos Federais

CSLL

Manutenção de DARF’s – Obrigações de Tributos Federais

INSS

Outras Obrigações – Retenções de INSS – Serviços Prestados – Manutenção da Consolidação das Retenções

IPI

IPI >> DATA MART >> Apuração do IPI

PIS/PASEP \(Próprio\)

SPED >> EFD – Contribuições >> Obrigações >> Manutenção >> Apuração PIS/PASEP

COFINS \(Próprio\)

SPED >> EFD – Contribuições >> Obrigações >> Manutenção >> Apuração COFINS

OS3962\-D

MFS\-1687

MFS\-2832

RN10

<a id="OLE_LINK15"></a><a id="OLE_LINK16"></a><a id="OLE_LINK17"></a>De acordo com a definição do campo “Tipo da Tag” da tela de Parametrização de Layout, o usuário poderá selecionar as seguintes opções nesse campo:

- Raiz = Elemento raiz que envolve todo o documento XML\.
	- Só poderá ser definido como Raiz, o primeiro campo do layout\. Abaixo dele obrigatoriamente, o campo deverá ser parametrizado como “Grupo”\. O campo definido como “Raiz” sempre terá como identificador o nome definido no campo “Identificação do Campo XML”\. O conteúdo desse campo ficará entre tags <>\. Exemplo: <NOME\_DO\_CAMPO>\.
- Grupo
	- Só poderá ser definido como Grupo, um campo cujo campo anterior seja “Raiz” respeitando a hierarquia\. Abaixo dele obrigatoriamente, o campo deverá ser parametrizado como “Atributo” ou “Elemento” respeitando a hierarquia\. O campo definido como “Grupo” sempre terá como identificador o nome definido no campo “Identificação do Campo XML”\. O conteúdo desse campo ficará entre tags <>\. Exemplo: <NOME\_DO\_CAMPO>\. O campo definido como “Grupo” sempre começará como <NOME DO CAMPO> e o mesmo será encerrado quando as informações pertencentes ao mesmo forem encerradas com a expressão </NOME DO CAMPO>\.
- Atributo
	- Só poderá ser definido como Atributo, um campo cujo campo anterior seja “Grupo”\. Abaixo dele obrigatoriamente, o campo deverá ser parametrizado como “Grupo” ou “Elemento”\. O campo definido como “Atributo” sempre terá como identificador o nome definido no campo “Identificação do Campo XML”\. O conteúdo desse campo ficará entre <>\. O campo do tipo Atributo terá valor associado na mesma linha e será finalizado posteriormente\. Exemplo: <FUNCIONARIO ID = “001”>\.

                             

                         Elemento               Atributo

                                                      

- Elemento
	- Só poderá ser definido como Elemento, o último \(ou últimos\) campo\(s\) do layout\. Abaixo dele obrigatoriamente, não deverá existir nenhum outro tipo de campo respeitando a hierarquia\. O campo definido como “Elemento” sempre terá como identificador o nome definido no campo “Identificação do Campo XML”\. O conteúdo desse campo ficará entre <> e sempre irá começar e finalizar na mesma linha\. Exemplo: <NOME\_DO\_CAMPO>100\.00</NOME\_DO\_CAMPO>\.

Exemplo de estrutura válida XML\.

<?xml version="1\.0"?>

<funcionarios>

     <funcionario ID = ''2101''>

        <nome>Alessandra</nome>

        <salario>2000</salario>

     </funcionario>

     <funcionario ID = ''2102''>

        <nome>Andressa</nome>

        <salario>3000</salario>

     </funcionario>

</funcionários>

OS3962\-D

MFS\-3268

RN11

Vale salientar que os campos do arquivo XML com tags sempre começarão com <NOME\_DO\_CAMPO> e terminarão com </NOME\_DO\_CAMPO>\.

OS3962\-D

RN12

Caso o cliente cancele o lote ao qual o arquivo XML está associado, o sistema irá apagar o arquivo XML da tabela temporária em que o mesmo está armazenado\.

OS3962\-D

RN13

Os dados de geração deverão ser armazenados, serão criados os campos “ID\_GER”, “SEQ\_GER\_ARQ” e TXT\_GER\_ARQ nas tabelas ITEM\_APURAC\_CALC, RESUMO\_APUR\_ST e EPC\_REG\_AJT\_M200\_M600 para cruzamento com os dados importados\(Retorno\)\.

Obs: Quando cancelado lote na tela de status \(Módulo: Soluções Complementares >> Monitor de Tributos Menu: Geração >> Status dos Arquivos\) a respectiva informação deverá ser deletada das tabelas\. 

MFS\-1688

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


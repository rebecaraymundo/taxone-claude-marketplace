# MTZ-Job_Servidor-Exportacao-execucao

- **Fonte:** MTZ-Job_Servidor-Exportacao-execucao.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 74 KB

---

# Módulo – Job Servidor – Exportação – execução

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

CH56743

Incluir novo código de situação no processo

Na tabela safx08 foi incluído novo código de situação tributária de PIS e de Cofins\.

OS3507

Job Servidor – Apresentar as tabelas \(Safx\) em ordem crescente tanto a Programação quanto na Execução

O objetivo deste requisito é reorganizar a apresentação das informações das tabelas SAFX e ordená\-las pelo nome da tabela SAFX\. Além disso, será disponibilizado uma forma do cliente escolher a seqüência de ordenação dos campos\.

OS4302

Job Servidor – Gerar arquivo TXT do Plano de Contas, Centro de Custos e Saldos Contábeis para importação no EFD\-IRPJ

O objetivo dessa OS é permitir a geração de arquivos no formato TXT das informações de Plano de Contas, Centro de Custo e Saldos Contábeis para posterior importação no EFD\-IRPJ\.

OS4302\-A

Job Servidor – Gerar arquivo TXT dos Saldos Contábeis para importação no EFD\-IRPJ

O objetivo dessa OS é permitir a geração de arquivos no formato TXT das informações dos Saldos Contábeis para posterior importação no EFD\-IRPJ\.

OS4302\-B

Job Servidor – Recomposição dos Saldos Contábeis e dos Saldos Contábeis por Centro de Custo para importação no EFD\-IRPJ

O objetivo dessa OS é permitir a recomposição dos Saldos Contábeis e dos Saldos Contábeis por Centro de Custo para a geração da EFD\-IRPJ\.

OS4302\-C

Job Servidor e Parâmetros \- Gravação dos dados de Saldos Contábeis, Saldos Contábeis por Centro de Custo, Plano de Contas e Centro de Custo em tabela

Essa OS tem por objetivo que os dados de Saldos Contábeis \(SAFX02\), Saldos Contábeis por Centro de Custo \(SAFX80\), Plano de Contas \(SAFX2002\) e Centro de Custo \(SAFX2003\) sejam gravados em uma tabela\.

Através da OS’s 4302, 4302\-A e 4302\-B, foram criados mecanismos que permitem que as informações dessas tabelas sejam geradas em arquivo TXT no formato da vindoura obrigação acessória ECF \(antigo EFD\-IRPJ\) para que a própria obrigação armazene essas informações\. Devido à novas possibilidades de solução, e que o ECF e o DW ficarão no mesmo banco de dados, será permitida essa integração\.

Será tratado também nessa OS a alteração na nomenclatura para OneSource ECF\.

OS4302\-D

Job Servidor – Inclusão do campo “Código SCP” no arquivo de Saldos Contábeis

Criar “Código da SCP”

OS4302\-D1 

Programação, Exportação execução da tabela SAFX2057

Atualizar tela de programação, exportação execução para exportação da OneSource ECF\. 

OS4025

Serviço de Diretório Oracle Directory

Incluir na tela de execução o parâmetro “__Serviço de Diretório” __que for__ __selecionado na Programação da Exportação 

OS4302\-E

Execução da Exportação da SAFX2101

Atualizar tela de execução da exportação, opção OneSource ECF, para que passe a exportar dados da tabela SAFX2101 

OS4302\-F

Execução da Exportação da SAFX2002 e SAFX2003\.

Atualizar a execução da exportação da SAFX2002 e SAFX2003 no padrão OneSource ECF para contemplar as regras para seleção do parâmetro “Considerar apenas Contas Contábeis e Centros de Custo movimentadas na exportação dos Cadastros”\.

OS4302\-H

Job Servidor – Exclusão do campo “Código SCP” no arquivo de Saldos Contábeis

Excluir “Código da SCP”

OS4302\-I

Execução da Exportação da SAFX01

Atualizar tela de execução da exportação, opção OneSource ECF, para que passe a exportar dados da tabela SAFX01\.

CH4603/2015

Atualização na regra de seleção da exportação da SAFX2002 para o ECF

Inclusão da regra para desconsiderar contas inativas na exportação da SAFX2002 para o Onesource\.

OS4302\-J

Job Servidor – Exportação de Dados 

Exclusão da coluna chamada “Exportar Dados para  OneSource ECF”\. O check\-box será retirado\.

__OS4302\-L__

Job Servidor – Exportação de Dados 

Exclusão da coluna chamada “Exportar Dados para  OneSource ECF” da tela “Execução de Jobs de Exportação”\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

No processo de execução da Exportação, o sistema deve realizar a exportação considerando o novo item 05 incluído na lista do campo 175 \- Código de situação tributária do PIS e no campo 178 do Código de Situação Tributária Cofins na tabela SAFX08\.

Deverá existir na tela de Execução de Jobs de Exportação o parâmetro “__Serviço de Diretório__” igual ao existente na tela de __Programação de Jobs de Exportação de Dados__ mostrando ao usuário o serviço de diretório escolhido na __Programação de Jobs de Exportação de Dados__\.

Serviço de Diretório

- Diretório Servidor
- Oracle Directory

O parâmetro servirá como demonstração, o mesmo não poderá ser alterado\.

__CH56743__

__OS4025__

__RN01__

__Regras gerais__

A lista de tabelas SAFX deve ser ordenada pelo campo Tabela Temp\. Ou seja, as tabelas SAFX’s deverão ser exibidas em ordem crescente\.

__OS3507__

__RN03__

\[__EXCLUÍDA \- OS4302\-J\]__

Deve ser retirado da tela “Execução de Jobs de Exportação de Dados os check\-box da coluna chamada “Exportar Dados para  OneSource ECF”, referente as SAFX2002, SAFX2002, SAFX01 e SAFX02\. Esta funcionalidade foi migrada para o novo módulo “ECF \- Escrituração Contábil Fiscal”, localizada em:  “MasterSAF\-DW 🡪 Conexão Onesource BR 🡪 ECF \- Escrituração Contábil Fiscal”\.

__EXCLUÍDA OS4302\-L\]__

Deve ser excluída da tela “Execução de Jobs de Exportação”, a coluna chamada “Exportar Dados para  OneSource ECF”\. Esta funcionalidade foi migrada para o novo módulo “ECF \- Escrituração Contábil Fiscal”, localizada em:  “MasterSAF\-DW 🡪 Conexão Onesource BR 🡪 ECF \- Escrituração Contábil Fiscal”\.

Deverá ser incluído na tela “Execução de Jobs de Exportação de Dados” uma coluna chamada “Exportar Dados para OneSource ECF”\. Essa coluna irá disponibilizar um check\-box para todas as tabelas que podem ser exportadas, porém somente as tabelas abaixo poderão ser exibidas selecionadas:

- SAFX80 – Saldos Contábeis por Centro de Custo
- SAFX2002 – Plano de Contas
- SAFX2003 – Centro de Custo 
- SAFX02 – Saldos Contábeis
- SAFX2057 – Cadastro da SCP
- SAFX2101 – Contas Referenciais x Plano de Contas

Esse check\-box será herdado da tela de Programação de Exportação de Dados do mesmo módulo \(menu: Exportação Dados >> Programação\)\. Todas as tabelas do tipo SAFX terão essa coluna no Job Servidor com esse check\-box\. 

__OS4302__

__OS4302\-A__

__OS4302D1__

__OS4302\-E__

__OS4302\-J__

__OS4302\-L__

__RN04__

\[__EXCLUÍDA \- OS4302\-J\]__

Este processo será cancelado da tela “Execução de Jobs de Exportação de Dados”\. Esta funcionalidade foi migrada para o novo módulo “ECF \- Escrituração Contábil Fiscal”, localizada em:  “MasterSAF\-DW 🡪 Conexão Onesource BR 🡪 ECF \- Escrituração Contábil Fiscal”\.

__EXCLUÍDA OS4302\-L\]__

Este processo deve ser excluído da tela “Execução de Jobs de Exportação”\. Esta funcionalidade foi migrada para o novo módulo “ECF \- Escrituração Contábil Fiscal”, localizada em:  “MasterSAF\-DW 🡪 Conexão Onesource BR 🡪 ECF \- Escrituração Contábil Fiscal”\.

Ao exportar as tabelas com o parâmetro “Exportar Dados para OneSource ECF” selecionado, o sistema irá gerar um arquivo para cada tabela exportada\. Os arquivos gerados serão das seguintes tabelas:

- SAFX80 – Saldos Contábeis por Centro de Custo
- SAFX2002 – Plano de Contas
- SAFX2003 – Centro de Custo
- SAFX02 – Saldos Contábeis
- SAFX2057 – Cadastro da SCP
- SAFX2101 – Contas Referenciais x Plano de Contas

Os arquivos serão gerados nos diretórios de acordo com a parametrização deDiretórios do OneSource ECF\.

O sistema só irá exportar para os grupos cadastrados\.

__OS4302__

__OS4302\-A__

__OS4302\-C__

__OS4302D1__

__OS4302\-E__

__OS4302\-J__

__OS4302\-L__

__RN05__

Para o correto desenvolvimento do arquivo que será exportado, o Manual de Layout da OneSource ECF deverá ser considerado, a separação dos campos, formato dos mesmos deverão ser consultadas nessa planilha, além de outras informações inerentes à estrutura do arquivo em si\.

__OS4302__

__RN06__

Para a geração do arquivo de Centro de Custo, as informações serão recuperadas da tela de Centro de Custo \(menu: Manutenção >> Códigos >> Centro de Custo\) do módulo Mastersaf DW\.

Caso o parâmetro “Considerar apenas Contas Contábeis e Centros de Custo movimentadas na exportação dos Cadastros” da tela de Parametrização para Recomposição dos Saldos Contábeis do OneSource ECF \(__Módulo:__ Básicos >> Parâmetros / __Menu:__ Preliminares\) estiver selecionado, no momento da exportação do arquivo de Centro de Custos devem ser gerados apenas os registros de centro de custo cujo código tenha sido informado na SAFX80 do período, sendo que o cadastro demonstrado em um período não pode ser demonstrado novamente em outro, assim evitamos duplicidade no arquivo\.

<a id="OLE_LINK4"></a><a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a>O nome do arquivo de Centro de Custo é \[PREFIXO\]\_CENTRO\_CUSTO\_\[SUFIXO\]\.TXT\. Caso não exista Prefixo parametrizado, o nome vai ser IRPJ\_CENTRO\_CUSTO\. 

O prefixo é definido no menu: Exportação Dados >> Prefixos de Arquivos do módulo Job Servidor\. O sufixo é definido através do campo “Nome do Arquivo” da tela Programação de Jobs de Exportação de Dados \(menu: Exportação Dados >> Programação\) do módulo Job Servidor\.

__OS4302__

__OS4302\-F__

__RN07__

No campo 001 – Código do Tipo de Registro será gerado o valor fixo “CAD2003”\.

__OS4302__

__RN08__

No campo 002 – CNPJ \(Código da Central de Cadastros\) será gerado o conteúdo do campo “CNPJ” para o Grupo parametrizado na tela de Cadastro de CNPJ do OneSource ECF\(menu: Preliminares >> Cadastro de CNPJ do OneSource ECF\)\. Para cada grupo, será gerado um arquivo diferente\.

Para que isso ocorra, o campo “Tipo do Cadastro” deverá ser “Centro de Custo”\.

__OS4302__

__OS4302\-C__

__RN09__

No campo 003 – Indicador de Exclusão será gerado o valor fixo “N”\.

__OBS: é importante salientar que em 10/12/2013, em conversa entre Marcos Oliveira, Marcos Paula e Jaime Nakamura que por enquanto essa informação será gerada dessa forma\. O valor “S” conforme Manual de Layout doOneSource ECF, não será tratado nesse momento\.__

__OS4302__

__OS4302\-C__

__RN10__

No campo 004 – Código do Centro de Custo, será gerado o conteúdo do campo COD\_CUSTO da tabela de Centro de Custo \(SAFX2003\)\.

__OS4302__

__RN11__

No campo 005 – Data de Início de Validade será gerado o conteúdo do campo DATA\_X2003 da tabela de Centro de Custo \(SAFX2003\)\.

__OS4302__

__RN12__

No campo 006 – Descrição do Centro de Custo será gerado o conteúdo do campo DESCRICAO da tabela de Centro de Custo \(SAFX2003\)\.

__OS4302__

__RN13__

Para a geração do arquivo de Plano de Contas, as informações serão recuperadas da tela de Plano de Contas \(menu: Manutenção >> Códigos >> Plano de Contas\) do módulo Mastersaf DW, \[__CH4643/2015__\] desconsiderando os registros das contas cujo Indicador de Situação da Conta \(IND\_SITUACAO\) seja igual a I – Inativa\.

Caso o parâmetro “Considerar apenas Contas Contábeis e Centros de Custo movimentadas na exportação dos Cadastros” da tela de Parametrização para Recomposição dos Saldos Contábeis do OneSource ECF \(__Módulo:__ Básicos >> Parâmetros / __Menu:__ Preliminares\) estiver selecionado, no momento da exportação do arquivo de Plano de Contas devem ser gerados apenas os registros de Contas Contábeis cujo código tenha sido informado na SAFX02 e SAFX80 do período, sendo que o cadastro demonstrado em um período não pode ser demonstrado novamente em outro, assim evitamos duplicidade no arquivo\.

Para este cenário, deve ser gerado no arquivo as informações do cadastro das contas sintéticas \(campo COD\_CONTA\_SINT da SAFX2002\) associada à conta movimentada encontrada e também o cadastro de todas as outras contas vinculadas, de nível superior, de forma que tenhamos o plano completo\. Exemplo:

No movimento \(SAFX02 ou SAFX80\) temos a conta: 0001\.0001\.0001\.0001, que no cadastro tem:

__Código de Conta__

__Código de Conta Sintética__

__Nível__

0001\.0001\.0001\.0001

0001\.0001\.0001

4

0001\.0001\.0001

0001\.0001

3

0001\.0001

0001

2

0001

1

Neste exemplo, apenas a conta 0001\.0001\.0001\.0001 foi movimentada, porém, no arquivo gerado para o OneSource devem ser demonstradas informações das contas "0001\.0001\.0001\.0001", "0001\.0001\.0001", "0001\.0001" e "0001"\.

O nome do arquivo de Centro de Custo é \[PREFIXO\]\_PLANO\_CONTAS\_\[SUFIXO\]\.TXT\. Caso não exista Prefixo parametrizado, o nome vai ser IRPJ\_PLANO\_CONTAS\.

O prefixo é definido no menu: Exportação Dados >> Prefixos de Arquivos do módulo Job Servidor\. O sufixo é definido através do campo “Nome do Arquivo” da tela Programação de Jobs de Exportação de Dados \(menu: Exportação Dados >> Programação\) do módulo Job Servidor\.

__OS4302__

__OS4302\-F__

__CH4643/2015__

__RN14__

No campo 001 – Código do Tipo de Registro será gerado o valor fixo “CAD2002”\.

__OS4302__

__RN15__

No campo 002 – CNPJ \(Código da Central de Cadastros\) será gerado o conteúdo do campo “CNPJ” para o Grupo parametrizado na tela de Cadastro de CNPJ do OneSource ECF\(menu: Preliminares >>Cadastro de CNPJ da OneSource ECF\)\. Para cada grupo, será gerado um arquivo diferente\.

Para que isso ocorra, o campo “Tipo do Cadastro” deverá ser “Plano de Contas”\.

__OS4302__

__RN16__

No campo 003 – Indicador de Exclusão será gerado o valor fixo “N”\. 

__OBS: é importante salientar que em 10/12/2013, em conversa entre Marcos Oliveira, Marcos Paula e Jaime Nakamura que por enquanto essa informação será gerada dessa forma\. O valor “S” conforme Manual de Layout doOneSource ECF, não será tratado nesse momento\.__

__OS4302__

__RN17__

No campo 004 – Código da Conta Contábil será gerado o conteúdo do campo COD\_CONTA da tabela de Plano de Contas \(SAFX2002\)\.

__OS4302__

__RN18__

No campo 005 – Data de Início da Validade será gerado o conteúdo do campo DATA\_X2002 da tabela de Plano de Contas \(SAFX2002\)\.

__OS4302__

__RN19__

No campo 006 – Descrição da Conta Contábil será gerado o conteúdo do campo DESCRICAO da tabela de Plano de Contas \(SAFX2002\)\.

__OS4302__

__RN20__

No campo 007 – Indicador do Tipo de Natureza da Conta será gerado o conteúdo do campo IND\_NATUREZA da tabela de Plano de Contas \(SAFX2002\), de acordo com a tabela abaixo:

- Caso o conteúdo seja “0”, gravar “0”;
- Caso o conteúdo seja “1”, gravar “1”;
- Caso o conteúdo seja “2”, gravar “2”;
- Caso o conteúdo seja “3”, gravar “3”;
- Caso o conteúdo seja “4”, gravar “4”;
- Caso o conteúdo seja “5”, gravar “5”;
- Caso o conteúdo seja “6”, gravar “6”;
- Caso o conteúdo seja “7”, gravar “7”;
- Caso o conteúdo seja “8”, gravar “8”;
- Caso o conteúdo seja “9”, gravar “9”\.

__OS4302__

__RN21__

No campo 008 – Indicador do Tipo de Conta Contábil será gerado o conteúdo do campo IND\_CONTA da tabela de Plano de Contas \(SAFX2002\)\.

__OS4302__

__RN22__

No campo 009 – Nível da Conta na Estrutura do Plano de Contas da Empresa será gerado o conteúdo do campo NIVEL da tabela de Plano de Contas \(SAFX2002\), de acordo com a tabela abaixo:

- Caso o conteúdo seja “1”, gravar “1”;
- Caso o conteúdo seja “2”, gravar “2”;
- Caso o conteúdo seja “3”, gravar “3”;

Vale salientar que no processo de exportação do arquivo, só serão exportados os arquivos com os códigos 1, 2 ou 3\.

__OS4302__

__RN23__

No campo 010 – Código da Conta Sintética de Nível Superior o conteúdo do campo COD\_CONTA\_SINT da tabela de Plano de Contas \(SAFX2002\)\.

__OS4302__

__RN24__

Para a geração do arquivo de Saldos Contábeis \(SAFX02\) ou Saldos Contábeis por Centro de Custo \(SAFX80\), as informações serão recuperadas da tela de Saldos Contábeis \(menu: Manutenção >> Contabilidade >> Diário Geral >> Saldos >> Por Estabelecimento\) ou Saldos Contábeis por Centro de Custo \(menu: Manutenção >> Contabilidade >> Saldos p/ Centro de Custo\) do módulo Mastersaf DW\.

A nomenclatura do arquivo de Saldos Contábeis \(SAFX02\) é \[PREFIXO\]\_SALDOS\_CONTABEIS\_\[SUFIXO\]\.TXT\. Caso não exista Prefixo parametrizado, o nome vai ser IRPJ\_SALDOS\_CONTABEIS\.

A nomenclatura do arquivo de Saldos Contábeis por Centro de Custo \(SAFX80\) é \[PREFIXO\]\_SALDOS\_CONTABEIS\_CC\_\[SUFIXO\]\.TXT\. Caso não exista Prefixo parametrizado, o nome vai ser IRPJ\_SALDOS\_CONTABEIS\_CC\.

O prefixo é definido no menu: Exportação Dados >> Prefixos de Arquivos do módulo Job Servidor\. O sufixo é definido através do campo “Nome do Arquivo” da tela Programação de Jobs de Exportação de Dados \(menu: Exportação Dados >> Programação\) do módulo Job Servidor\.

__OS4302__

__OS4302\-A__

__RN25__

No campo 001 – Código do Tipo de Registro será gerado o conteúdo fixo “MOV0002”\.

__OS4302__

__RN26__

No campo 002 – Indicador de Exclusão será gerado o valor fixo “N”\. 

__OBS: é importante salientar que em 10/12/2013, em conversa entre Marcos Oliveira, Marcos Paula e Jaime Nakamura que por enquanto essa informação será gerada dessa forma\. O valor “S” conforme Manual de Layout doOneSource ECF, não será tratado nesse momento\.__

__OS4302__

__RN27__

No campo 003 – CNPJ do Centro de Custo será gerado o CNPJ que está contido o conteúdo do campo “CNPJ” do Estabelecimento do Saldo Contábil por Centro de Custo ou Saldo Contábil \(campo: Estabelecimento\) que está cadastrado no cadastro de Empresa/Estabelecimento do módulo Parâmetros \(ver campo CNPJ do menu: Preliminares >> Empresa/Estabelecimento\)\.

Essa regra é válida somente para os Saldos Contábeis por Centro de Custo da SAFX80 e Saldos Contábeis da SAFX02\.

__OS4302__

__OS4302\-A__

__RN27\-A__

__\[EXCLUÍDA – OS4302\-H\]__

No campo 004 – Código da SCP será gerado o conteúdo nulo\.

__OBS: é importante salientar que a definição do conteúdo desse campo como nulo foi definido pela equipe do projeto conforme e\-mail em anexo à OS4302\-D\.__

__OS4302\-D__

__/__

__OS4302\-H__

__RN29__

No campo 005 – Código do Centro de Custo será gerado o conteúdo do campo “Centro Custo” da tela Novo Saldo por Centro de Custo do módulo DW \(menu: Manutenção >> Contabilidade >> Saldos p/ Centro de Custo\)\. 

Essa regra é válida somente para os Saldos Contábeis por Centro de Custo\. Caso a informação seja oriunda da SAFX02, será gravado nulo nesse campo\.

__OS4302__

__OS4302\-A__

__RN30__

No campo 006 – Código da Conta Contábil será gerado o conteúdo do campo “Conta” da tela Novo Saldo por Centro de Custo do módulo DW \(menu: Manutenção >> Contabilidade >> Saldos p/ Centro de Custo\) ou do campo “Conta” da tela Novo Saldo Contábil por Estabelecimento \(menu: Manutenção >> Contabilidade >> Diário Geral >> Saldos >> Por Estabelecimento\.

__OS4302__

__OS4302\-A__

__RN31__

No campo 007 – Data de Apuração do Saldo será gerado o conteúdo do campo “Data do Saldo” da tela Novo Saldo por Centro de Custo do módulo DW \(menu: Manutenção >> Contabilidade >> Saldos p/ Centro de Custo\) ou do campo “Data do Saldo” da tela Novo Saldo Contábil por Estabelecimento \(menu: Manutenção >> Contabilidade >> Diário Geral >> Saldos >> Por Estabelecimento\.

__OS4302__

__OS4302\-A__

__RN32__

No campo 008 – Valor do Saldo da Conta do Início do Período será gerado o conteúdo do campo “Saldo Contábil Anterior” da tela Novo Saldo por Centro de Custo do módulo DW \(menu: Manutenção >> Contabilidade >> Saldos p/ Centro de Custo\) ou do campo “Saldo Inicial” da tela Novo Saldo Contábil por Estabelecimento \(menu: Manutenção >> Contabilidade >> Diário Geral >> Saldos >> Por Estabelecimento\.

__OS4302__

__OS4302\-A__

__RN33__

No campo 009 – Indicador de Saldo Inicial será gerado o conteúdo do campo IND\_DEB\_CRED\_ANT da tabela SAFX80 \(Saldos Contábeis por Centro de Custo\) – tela Novo Saldo por Centro de Custo do módulo DW \(menu: Manutenção >> Contabilidade >> Saldos p/ Centro de Custo\) ou do campo “Débito/Crédito” da tela Novo Saldo Contábil por Estabelecimento \(menu: Manutenção >> Contabilidade >> Diário Geral >> Saldos >> Por Estabelecimento\.

__OS4302__

__OS4302\-A__

__RN34__

No campo 010 – Valor Total dos Créditos Registrados será gerado o conteúdo do campo “Total Créditos” da tela Novo Saldo por Centro de Custo do módulo DW \(menu: Manutenção >> Contabilidade >> Saldos p/ Centro de Custo\) ou do campo “Total Créditos” da tela Novo Saldo Contábil por Estabelecimento \(menu: Manutenção >> Contabilidade >> Diário Geral >> Saldos >> Por Estabelecimento\.

__OS4302__

__OS4302\-A__

__RN35__

No campo 011 – Valor Total dos Débitos Registrados será gerado o conteúdo do campo “Total Débitos” da tela Novo Saldo por Centro de Custo do módulo DW \(menu: Manutenção >> Contabilidade >> Saldos p/ Centro de Custo\) ou do campo “Total Débitos” da tela Novo Saldo Contábil por Estabelecimento \(menu: Manutenção >> Contabilidade >> Diário Geral >> Saldos >> Por Estabelecimento\.

__OS4302__

__OS4302\-A__

__RN36__

No campo 012 – Valor do Saldo da Conta Apurado na Data Informada será gerado o conteúdo do campo “Saldo Final” da tela Novo Saldo por Centro de Custo do módulo DW \(menu: Manutenção >> Contabilidade >> Saldos p/ Centro de Custo\) ou do campo “Saldo Final” da tela Novo Saldo Contábil por Estabelecimento \(menu: Manutenção >> Contabilidade >> Diário Geral >> Saldos >> Por Estabelecimento\.

__Recomposição do Saldo__:

Caso exista parametrização para o estabelecimento que sendo exportado na tela “Parametrização para a Recomposição dos Saldos Contábeisdo OneSource ECF” do módulo Parâmetros, o sistema irá recompor o saldo da seguinte maneira:

- __Apuração “Anual” e Encerramento “Anual”__:
	- Será recuperado o lançamento de Encerramento da SAFX01 cujo campo 17 – TIPO\_LANCTO = ‘E’ no mês de Dezembro e esse valor terá o sinal invertido \(débito para crédito e crédito para débito\) e o valor do lançamento será informado no campo 011 do Layout de Importaçãodo OneSource ECF\. Caso o valor seja crédito, o mesmo será subtraído no campo 009, caso contrário \(débito\) será subtraído no campo 010\.
- __Apuração “Anual” e Encerramento “Semestral”__:
	- Será recuperado o lançamento de Encerramento da SAFX01 cujo campo 17 – TIPO\_LANCTO = ‘E’ nos meses de Junho e Dezembro e esse valor terá o sinal invertido \(débito para crédito e crédito para débito\) e o valor do lançamento será informado no campo 011 do Layout de Importação do OneSource ECF\. Caso o valor seja crédito, o mesmo será subtraído no campo 009, caso contrário \(débito\) será subtraído no campo 010\. Para o meses subsequentes o saldo inicial deverá ser recomposto com o valor “0”\.
- __Apuração “Trimestral” e Encerramento “Anual”__:
	- Será recuperado o lançamento de Encerramento da SAFX01 cujo campo 17 – TIPO\_LANCTO = ‘E’ no mês de Dezembro e esse valor terá o sinal invertido \(débito para crédito e crédito para débito\) e o valor do lançamento será informado no campo 011 do Layout de Importação do OneSource ECF\. Caso o valor seja crédito, o mesmo será subtraído no campo 009, caso contrário \(débito\) será subtraído no campo 010\.
- __Apuração “Trimestral” e Encerramento “Semestral”__:
	- Será recuperado o lançamento de Encerramento da SAFX01 cujo campo 17 – TIPO\_LANCTO = ‘E’ no mês de Junho e Dezembro e esse valor terá o sinal invertido \(débito para crédito e crédito para débito\) e o valor do lançamento será informado no campo 011 do Layout de Importação do OneSource ECF\. Caso o valor seja crédito, o mesmo será subtraído no campo 009, caso contrário \(débito\) será subtraído no campo 010\.
- __Apuração “Trimestral” e Encerramento “Trimestral”__:
	- Será recuperado o lançamento de Encerramento da SAFX01 cujo campo 17 – TIPO\_LANCTO = ‘E’ no mês de Março, Junho, Setembro e Dezembro e esse valor terá o sinal invertido \(débito para crédito e crédito para débito\) e o valor do lançamento será informado no campo 011 do Layout de Importação do OneSource ECF\. Caso o valor seja crédito, o mesmo será subtraído no campo 009, caso contrário \(débito\) será subtraído no campo 010\.

Nos casos em que o Encerramento for “Trimestral” ou “Semestral” o Saldo Inicial deverá ser recomposto em conjunto com o Saldo Final que foi apurado anteriormente\.

__OS4302__

__OS4302\-A__

__OS4302\-B__

__OS4302\-C__

__RN37__

No campo 013 – Indicador de Saldo Final será gerado o conteúdo do campo Indicador do Saldo Final da tela Novo Saldo por Centro de Custo do módulo DW \(menu: Manutenção >> Contabilidade >> Saldos p/ Centro de Custo\) ou do campo Indicador do Saldo Final da tela Novo Saldo Contábil por Estabelecimento \(menu: Manutenção >> Contabilidade >> Diário Geral >> Saldos >> Por Estabelecimento\.

__OS4302__

__OS4302\-A__

__RN38__

Para a geração do arquivo de Cadastro da SCP, as informações serão recuperadas da tabela x2057\_cod\_scp\.

O nome do arquivo de Centro de Custo é \[PREFIXO\]\_CADASTRO\_SCP\_\[SUFIXO\]\.TXT\. Caso não exista Prefixo parametrizado, o nome vai ser IRPJ\_CADASTRO\_SCP\. 

O prefixo é definido no menu: Exportação Dados >> Prefixos de Arquivos do módulo Job Servidor\. O sufixo é definido através do campo “Nome do Arquivo” da tela Programação de Jobs de Exportação de Dados \(menu: Exportação Dados >> Programação\) do módulo Job Servidor\.

Caso esteja parametrizado para integração dos dados como __“Banco de Dados”__, não realizar a exportação, e exibir a seguinte mensagem ao usuário __“Exportação Banco a Banco não disponível”__\.

__OS4302D1__

__RN39__

No campo 001 – Código do Tipo de Registro será gerado o valor fixo “CAD2057”\.

__OS4302D1__

__RN40__

No campo 002 – Indicador de Exclusão indicar se é uma operação de exclusão\. 

Indicador de Exclusão será gerado o valor fixo “N”\.

__OBS: é importante salientar que em 10/12/2013, em conversa entre Marcos Oliveira, Marcos Paula e Jaime Nakamura que por enquanto essa informação será gerada dessa forma\. O valor “S” conforme Manual de leiaute OneSource ECF\_Manual\_Layout, não será tratado nesse momento\.__

 

__OS4302D1__

__RN41__

No campo 003 – CNPJ do Estabelecimento

O CNPJ do estabelecimento será gerado considerando a seguinte regra:

A partir do Código da Empresa campo \(COD\_EMPRESA\) \+ Código do estabelecimento campo \(COD\_ESTAB\) da tabela SAFX2057, recupera o CNPJ do estabelecimento vinculado na X2057   

__OS4302D1__

__RN42__

No campo 004 – Data de Inicio da validade

Data de início da validade das informações cadastrais dos códigos SCP\.

Formato Ano\-Mês\-Dia \(YYYY\-MM\-DD\)\.

Data de Início da Validade será gerado o conteúdo do campo DATA\_X2057 da tabela de Cadastro da SCP \(SAFX2057\)\.

__OS4302D1__

__RN43__

No campo 005 – Código da SCP

Código de Identificação da SCP será gerado a partir do campo \(COD\_SCP\) da tabela SAFX2057 

__OS4302D1__

__RN44__

No campo 006 – Descrição SCP \(Descrição da Sociedade em Conta de Participação\)

Será gerado a partir do campo \(DSC\_SCP\) da tabela SAFX2057 

__OS4302D1__

__RN45__

No campo 007 – Informação complementar referente á SCP

Será gerado a partir do campo Informação \(DSC\_INF\_COMPL\) da tabela SAFX2057

__OS4302D1__

__RN46__

Ao executar o Job de Exportação de Dados das tabelas SAFX02, SAFX80, SAFX2002 e SAFX2003, caso o parâmetro “Exportar Dados paraOneSource ECF” esteja selecionado para o estabelecimento selecionado e esse mesmo estabelecimento esteja parametrizado na tela “Parametrização de Integração do ECF” \(menu: Preliminares >> Parametrização de Integração do ECF\) do módulo Parâmetros com a opção “Banco de Dados” selecionada, o sistema não exportará o arquivo em formato texto e gravará as informações das tabelas de acordo com o DE/PARA abaixo:

- SAFX02 ou SAFX80: as informações dessas tabelas serão gravadas na tabela TBR\_INT\_0002
- SAFX2002: as informações dessas tabelas serão gravadas na tabela TBR\_INT\_2002
- SAFX2003: as informações dessas tabelas serão gravadas na tabela TBR\_INT\_2003
- SAFX2101: as informações dessas tabelas serão gravadas na tabela TBR\_INT\_2101

__OS4302\-C__

__OS4302\-E__

__RN47__

Ao executar o Job de Exportação de Dados das tabelas SAFX02, SAFX80, SAFX2002, SAFX2003, SAFX2057 ou SAFX2101, caso o parâmetro “Exportar Dados para OneSource ECF” esteja selecionado para o estabelecimento selecionado e esse mesmo estabelecimento esteja parametrizado na tela “Parametrização de Integração do ECF” \(menu: Preliminares >> Parametrização de Integração do ECF\) do módulo Parâmetros com a opção “Arquivo Texto” selecionada, o sistema exportará o arquivo em formato texto conforme definições das OS’s 4302, 4302\-A, 4302\-B, 4302\-D__OS4302\-H, __4302\-D1 e 4302\-E contidas nesse documento matriz\.

__OS4302\-C__

__OS4302\-D1__

__OS4302\-E__

__OS4302\-H__

__RN48__

Para a geração do arquivo de Parametrização do Plano de Contas Referencial X Plano de Contas da Empresa \(PAR2101\), teremos os seguintes critérios:

__Origem das Informações__: SAFX2101 – Contas Referenciais x Plano de Contas

__Regra de seleção__: consideraremos os registros da tabela SAFX2101 cuja Versão da Conta Referencial seja maior ou igual a “3\.00” e considerando os registros cuja Conta Referencial \(COD\_CONTA\_REF\) informada da SAFX2101 __não tenha__ a Data Final de Validade \(DAT\_VALIDADE\_FIM\) preenchida na TFIX64 __OU__ se tiver data final preenchida, que seja uma Data Final maior ou igual a 01/01/2014\.

__Nomenclatura do arquivo__: a nomenclatura do arquivo de Parametrização do Plano de Contas Referencial X Plano de Contas da Empresa será: \[PREFIXO\]\_PLANO\_CONTAS\_PLANO\_REFERENCIAL\_\[SUFIXO\]\.TXT\. Caso não exista Prefixo parametrizado, o nome vai ser IRPJ\_PLANO\_CONTAS\_PLANO\_REFERENCIAL\.

O prefixo é definido no menu: Exportação Dados >> Prefixos de Arquivos do módulo Job Servidor\. O sufixo é definido através do campo “Nome do Arquivo” da tela Programação de Jobs de Exportação de Dados \(menu: Exportação Dados >> Programação\) do módulo Job Servidor\.

O arquivo de Parametrização do Plano de Contas Referencial X Plano de Contas da Empresa \(PAR2101\) tem uma estrutura diferente dos demais, pois é um arquivo hierárquico\. Nele teremos a seguinte estrutura:

__Registro PAR2101\_01 \- Nível 1__: este registro será uma demonstração de informações por CNPJ do Estabelecimento, Data Inicial de Validade, Código da Entidade que Identifica o Plano de Contas Referencial e Versão do Plano de Contas Referencial

__Registro PAR2101\_02 \- Nível 2, filho do PAR2101\_01__: este registro será uma demonstração de informações por Código da Conta do Plano de Contas Referencial\. Como teremos no registro pai, PAR2101\_01, as informações do estabelecimento, aqui teremos a relação das Contas Referenciais que pertencem à parametrização do estabelecimento\.

__Registro PAR2101\_03 \- Nível 3, filho do PAR2101\_02__: este registro será uma demonstração de informações por Código da Conta Contábil do Plano de Contas Empresarial\. No registro pai, PAR2101\_02, temos a conta referencial e neste registro teremos a demonstração das contas contábeis do plano de contas da empresa associadas à conta referencial apresentada no registro pai\.

__Registro PAR2101\_04 \- Nível 4, filho do PAR2101\_03__: este registro será uma demonstração de informações por Código do Centro de Custos\. No registro pai, PAR2101\_03, teremos a demonstração das contas contábeis e aqui todos os centros de custo associados a conta\. Este registro não é obrigatório e não será gerado quando o campo centro de custo da SAFX2101 não estiver preenchido\.

__Formatação dos campos__: observar as seguintes regras de formatação dos campos:

\- Os campo tipo Data devem ser informados no formato AAAA\-MM\-DD;

\- Os campo tipo Numérico devem ser informados com ponto "\." para separação de decimais;

Sobre a formação específica do arquivo txt, observar a aba “Considerações” do Manual de Layout do Onesource\.

__Ordenação das informações__: não há regra de ordenação para geração do PAR2101\.

__OS4302\-E__

__RN49__

__Arquivo PAR21021, Registro PAR2101\_01, Campo 001 \- COD\_RECORD__

Informação fixa “PAR2101\_01”\.

__OS4302\-E__

__RN50__

__Arquivo PAR21021, Registro PAR2101\_01, Campo 002 \- NUM\_FED\_TAX__

Será gerado o conteúdo do campo “CNPJ” para o Grupo parametrizado na tela de Cadastro de CNPJ do OneSource ECF\(menu: Preliminares >>Cadastro de CNPJ da OneSource ECF\)\. Para cada grupo, será gerado um arquivo diferente\.

Para que isso ocorra, o campo “Tipo do Cadastro” deverá ser “Plano de Contas”\.

__OS4302\-E__

__RN51__

__Arquivo PAR21021, Registro PAR2101\_01, Campo 003 \- IND\_DELETE__

Informação fixa “N”\.

__OS4302\-E__

__RN52__

__Arquivo PAR21021, Registro PAR2101\_01, Campo 004 \- DAT\_STARTUP\_EFFECTIVE__

Não será preenchido, pois, conforme acordado com A&D do ECF este campo será gerado no processo de integração, considerando a data da versão do Plano Referencial importada\.

__OS4302\-E__

__RN53__

__Arquivo PAR21021, Registro PAR2101\_01, Campo 005 \- DAT\_END\_EFFECTIVE__

Não será preenchido, pois, conforme acordado com A&D do ECF este campo será gerado no processo de integração, considerando a data da versão do Plano Referencial importada\.

__OS4302\-E__

__RN54__

__Arquivo PAR21021, Registro PAR2101\_01, Campo 006 \- COD\_REF\_LIST__

Será gerado com o Código da Entidade \(COD\_ENTIDADE\_RESP\) informado na SAFX2101\.

__OS4302\-E__

__RN55__

__Arquivo PAR21021, Registro PAR2101\_01, Campo 007 \- COD\_REF\_LIST\_VERSION__

Será gerado com a Versão do Plano Referencial \(VERSAO\_REF\) informado na SAFX2101\.

__OS4302\-E__

__RN56__

__Arquivo PAR21021, Registro PAR2101\_02, Campo 001 \- COD\_RECORD__

Informação fixa “PAR2101\_02”\.

__OS4302\-E__

__RN57__

__Arquivo PAR21021, Registro PAR2101\_02, Campo 002 \- IND\_DELETE__

Informação fixa “N”\.

__OS4302\-E__

__RN58__

__Arquivo PAR21021, Registro PAR2101\_02, Campo 003 \- COD\_REF\_LEDGER\_ACCOUNT__

Será gerado com o Código da Conta Referencial \(COD\_CONTA\_REF\) informado na SAFX2101\.

__OS4302\-E__

__RN59__

__Arquivo PAR21021, Registro PAR2101\_03, Campo 001 \- COD\_RECORD__

Informação fixa “PAR2101\_03”\.

__OS4302\-E__

__RN60__

__Arquivo PAR21021, Registro PAR2101\_03, Campo 002 \- COD\_LEDGER\_ACCOUNT__

Será gerado com o Código da Conta Contábil \(COD\_CONTA\) informado na SAFX2101\.

__OS4302\-E__

__RN61__

__Arquivo PAR21021, Registro PAR2101\_04, Campo 001 \- COD\_RECORD__

Informação fixa “PAR2101\_04”\.

__OS4302\-E__

__RN62__

__Arquivo PAR21021, Registro PAR2101\_04, Campo 002 \- COD\_COST\_CENTER__

Será gerado com o Código do Centro de Custos \(COD\_CUSTO\) informado na SAFX2101\.

__OS4302\-E__

__RN63__

Conforme RN46, será possível a integração banco a banco, considerando parametrização realizada pelo usuário\. Para gravação da tabela TBR\_INT\_2101, será considerada a mesma Regra de Seleção prevista na RN48 e teremos a seguinte estrutura e regras de geração:

__Item__

__Atributo__

__Campo da Tabela__

__TP__

__TAM__

__DEC__

__Formato__

__PK__

__OB__

__Orientação Mastersaf DW__

001

CNPJ do Estabelecimento

NUM\_FED\_TAX

N

014

S

S

Observar regra disposta na RN50 deste arquivo\.

002

Data Inicial de Validade

DAT\_STARTUP\_EFFECTIVE

D

S

Observar regra disposta na RN52 deste arquivo\.

003

Data Final de Validade

DAT\_END\_EFFECTIVE

D

S

Observar regra disposta na RN53 deste arquivo\.

004

Código da Entidade que Identifica o Plano de Contas Referencial

COD\_REF\_LIST

A

020

S

S

Observar regra disposta na RN54 deste arquivo\.

005

Versão do Plano de Contas Referencial

COD\_REF\_LIST\_VERSION

A

010

S

S

Observar regra disposta na RN55 deste arquivo\.

006

Indicador de Exclusão

IND\_DELETE\_ALL

A

001

Observar regra disposta na RN51 deste arquivo\.

007

Indicador de Exclusão

IND\_DELETE\_REF\_LEDGER\_ACC

A

001

Observar regra disposta na RN57 deste arquivo\.

008

Código da Conta do Plano de Contas Referencial

COD\_REF\_LEDGER\_ACCOUNT

A

070

S

S

Observar regra disposta na RN58 deste arquivo\.

009

Código da Conta Contábil do Plano de Contas Empresarial

COD\_LEDGER\_ACCOUNT

A

070

S

S

Observar regra disposta na RN60 deste arquivo\.

010

Código do Centro de Custos

COD\_COST\_CENTER

A

050

S

Observar regra disposta na RN62 deste arquivo\.

011

Data da Última Atualização do Registro

D\_LAST\_UPDATE\_DATE

D

N

Será gerada com a informação da Data do Sistema no dia da realização da exportação\.

012

Responsável pela Última Atualização

S\_LAST\_UPDATE\_BY

A

250

N

Será gerado com o Código do Usuário do Mastersaf que está realizando o processo de exportação\.

013

Data da Criação do Registro

D\_CREATION\_DATE

D

S

Será gerada com a informação da Data do Sistema no dia da realização da exportação\.

014

Responsável pela Criação

S\_CREATED\_BY

A

250

N

Será gerado com o Código do Usuário do Mastersaf que está realizando o processo de exportação\.

__OS4302\-E__

__RN64__

__Regra Geral de Geração do Arquivo MOV0001\.__

O arquivo MOV0001 do Onesource ECF tem por objetivo gerar informações dos Lançamentos Contábeis\. 

Observar orientações existentes no arquivo "Manual\_Layout\_TXT\_DE\_PARA\.xlsx", abas "Layout TXT" e "Orientações\_Evento\_Periódico"\.

- __Origem das informações__: Arquivo Contábil\.
- __Regra de seleção__: há uma regra de seleção específica para cada registro do arquivo MOV0001, porém, de forma geral, o arquivo será gerado com informações dos Lançamentos Contábeis\.

O arquivo vai ser gerado quando o parâmetro da tela de programação de exportação estiver marcado

O arquivo não precisa respeitar o tamanho fixo de cada campo, sendo necessário apenas respeitar o tamanho máximo do campo, utilizando pipe no final de cada registro\.  

- __Nome do Arquivo__:  O nome do arquivo de Lançamentos Contábeis é \[PREFIXO\]\_CONTABIL\[SUFIXO\]\.TXT\. Caso não exista Prefixo parametrizado, o nome vai ser IRPJ\_CONTABIL\. 

O prefixo é definido no menu: Exportação Dados >> Prefixos de Arquivos do módulo Job Servidor\. O sufixo é definido através do campo “Nome do Arquivo” da tela Programação de Jobs de Exportação de Dados \(menu: Exportação Dados >> Programação\) do módulo Job Servidor\.

Será possível a integração banco a banco, considerando a parametrização realizada pelo usuário\.

 Para isso, devemos verificar se o estabelecimento está parametrizado na tela “Parametrização de Integração do ECF” \(menu: Preliminares >> Parametrização de Integração do ECF\) do módulo Parâmetros com a opção “Banco de Dados” selecionada, neste caso o sistema não exportará o arquivo em formato texto e gravará as informações das tabelas de acordo com o DE/PAR abaixo:

\- SAXF01: as informações dessa tabela será gravada na tabela TBR\_INT\_0001\. 

__OS4302\-I__

__RN65__

__Registro MOV0001\-01 – Lançamento Contábil__

- __Origem das informações__: Lançamento Contábil \(SAFX01\)\.

__Regra de seleção__: Deve ser gerado um arquivo por estabelecimento selecionado e será gerado sempre que, na tela de Geração dos Dados do integrador a opção “MOV0001 – Lançamentos Contábeis” estiver selecionada, considerando os critérios de geração dos registros\. 

Na geração, deverão ser considerados todos os lançamentos contábeis registrados na SAFX01 cuja Data da Operação \(DATA\_OPERACAO\) compreenda o período parametrizado, que tenha o Tipo de Lançamento \(TIPO\_LANCTO\) diferente de “E” e que tenha a Conta Contábil \(CONTA\_DEB\_CRED\) __OU__ Conta \(CONTA\_DEB\_CRED\) e Centro de Custo \(CENTRO\_CUSTO\) parametrizado na Parametrização das Contas Contábeis \(Módulo: Federal >> Integrador Onesource ECF / Menu: Parâmetros>> Parametrização das Contas Contábeis\)\.

- __Campos\-Chave__: CNPJ do Estabelecimento, Data do Lançamento e Número do Lançamento\.
- __Nível hierárquico do registro__: Pai
- __Ordenação__: não se aplica\.
- __Agrupamento__: CNPJ do Estabelecimento, Data do Lançamento e Número do Lançamento\.
- __Ocorrência__: vários por arquivo\.

__OS4302\-I__

__RN66__

__Campo CNPJ do Estabelecimento__

CNPJ do Estabelecimento:

Deverá preencher com a informação do campo CGC da tabela ESTABELECIMENTO, referente ao código do estabelecimento que está registrado na tabela SAFX01\. 

__OS4302\-I__

__RN67__

__Campo Número do Lançamento__

Deverá preencher com a informação do campo NUM\_LANCAMENTO da tabela SAFX01, referente ao número de lançamento que está registrado na tabela SAFX01\. 

__OBS\.:__ Quando não houver o preenchimento do campo Número do Lançamento na SAFX01, deverá ser exportado com pipe, espaço e pipe __\(| |\)__\. Essa Regra deverá ser válida, tanto para a geração do Arquivo TXT, como também para a geração Banco à Banco\. 

__OS4302\-I__

__RN68__

__Registro MOV0001\-02 – Partidas do Lançamento Contábil__

- __Origem das informações__: Lançamento Contabil \(SAFX01\)\.

__Regra de seleção__: o objetivo deste registro é detalhar os lançamentos contábeis correspondentes ao agrupamento realizado no registro pai, MOV0001\_01\. Deve considerar a mesma regra de seleção do registro pai\. 

- __Campos\-Chave__: não se aplica\.
- __Nível hierárquico do registro__: filho do MOV0001\_01
- __Ordenação__: não se aplica\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: vários por arquivo\.

__OS4302\-I__

__RN69__

__Indicador do Lançamento __

Indicador do lançamento\.  Preencher de acordo com: 

“D” – Débito\. Quando o campo IND\_DEB\_CRE da tabela SAFX01 estiver preenchido com a opção “D” \- Débito\.

“C” – Crédito\. Quando o campo IND\_DEB\_CRE da tabela SAFX01 estiver preenchido com a opção “C” \- Débito\.

__OS4302\-I__

__RN70__

__Estrutura para Integração Banco a Banco__

Conforme comentado na RN64, será possível a integração banco a banco, considerando a parametrização realizada pelo usuário\. Para gravação da tabela TBR\_INT\_0001, será considerada a mesma Regra de Seleção prevista na RN65 e teremos a seguinte estrutura e regras de geração:

__Item__

__Atributo__

__TP__

__TAM__

__DEC__

__Formato__

__PK__

__OB__

__Orientação Mastersaf DW__

001

CNPJ do Estabelecimento

A

014

S

S

Observar regra disposta na RN66 deste arquivo\.

002

Indicador de Exclusão

A

001

Observar regra disposta no arquivo de DE/PARA: “Manual\_Layout\_TXT\_DE\_PARA\.xlsx

003

Data do Lançamento

D

010

YYYY\-MM\-DD

S

S

Observar regra disposta no arquivo de DE/PARA: “Manual\_Layout\_TXT\_DE\_PARA\.xlsx

004

Número do Lançamento

A

020

S

S

Observar regra disposta no arquivo de DE/PARA: “Manual\_Layout\_TXT\_DE\_PARA\.xlsx

005

Valor do Lançamento

N

017

002

Observar regra disposta no arquivo de DE/PARA: “Manual\_Layout\_TXT\_DE\_PARA\.xlsx

006

Tipo de Lançamento

A

001

S

Observar regra disposta no arquivo de DE/PARA: “Manual\_Layout\_TXT\_DE\_PARA\.xlsx

007

Código da Conta Contábil

A

070

S

Observar regra disposta no arquivo de DE/PARA: “Manual\_Layout\_TXT\_DE\_PARA\.xlsx

008

Código do Centro de Custo

A

050

Observar regra disposta no arquivo de DE/PARA: “Manual\_Layout\_TXT\_DE\_PARA\.xlsx

009

Código da Conta de Contrapartida

A

070

Observar regra disposta no arquivo de DE/PARA: “Manual\_Layout\_TXT\_DE\_PARA\.xlsx

010

Número de Arquivamento

A

050

S

S

Observar regra disposta no arquivo de DE/PARA: “Manual\_Layout\_TXT\_DE\_PARA\.xlsx

011

Indicador do Lançamento

A

001

S

Observar regra disposta na RN68 deste arquivo\.

012

Valor da Partida

N

017

002

S

Observar regra disposta no arquivo de DE/PARA: “Manual\_Layout\_TXT\_DE\_PARA\.xlsx

013

Data da Última Atualização do Registro

N

Será gerada com a informação da Data do Sistema no dia da realização da exportação\.

014

Responsável pela Última Atualização

250

250

N

Será gerado com o Código do Usuário do Mastersaf que está realizando o processo de exportação\.

015

Data da Criação do Registro

S

Será gerada com a informação da Data do Sistema no dia da realização da exportação\.

‘Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

 


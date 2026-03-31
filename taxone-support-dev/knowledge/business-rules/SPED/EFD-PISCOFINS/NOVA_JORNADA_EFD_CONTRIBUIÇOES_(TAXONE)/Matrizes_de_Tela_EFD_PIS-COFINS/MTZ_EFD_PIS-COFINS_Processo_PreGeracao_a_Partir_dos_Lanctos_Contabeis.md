# MTZ_EFD PIS-COFINS_Processo_PreGeracao_a_Partir_dos_Lanctos_Contabeis

- **Fonte:** MTZ_EFD PIS-COFINS_Processo_PreGeracao_a_Partir_dos_Lanctos_Contabeis.docx
- **Modificado:** 2023-04-27
- **Tamanho:** 103 KB

---

THOMSON REUTERS

Módulo Sped Contribuições

Pré\-Geração a Partir dos Lanctos Contábeis \(PROCESSO\)

__Localização__: Menu Sped, Módulo: EFD Escrituração Fiscal Digital das Contribuições 🡪 Manutenção🡪 Registro do Bloco F 🡪 Demais Documentos e Operações Geradoras de Contribuição e Créditos \(F100\) 🡪Pré\-Geração a Partir dos Lanctos Contábeis

Sumário

[1\.	CONTROLE DE ALTERAÇÕES	2](#_Toc72497612)

[2\.	INTRODUÇÃO	3](#_Toc72497613)

[3\.	DOCUMENTOS DE REFERÊNCIA	3](#_Toc72497614)

[4\.	DEFINIÇÃO DAS REGRAS	4](#_Toc72497615)

# <a id="_Toc462320891"></a><a id="_Toc27038219"></a><a id="_Toc72497612"></a>CONTROLE DE ALTERAÇÕES

__Data__

__Demanda__

__Descrição__

__Autor__

19/05/2021

MFS\-64743

Criação do processo que será acionado na tela ‘Pré\-Geração a Partir dos Lanctos Contábeis’, que a partir dos lançamentos contábeis existente na base e a parametrização definida para a geração do registro F100 do SPED Contribuições \(em dados iniciais do módulo\), grava as informações na x147\_oper\_cred\.

Alessandra Cristina Navatta

21/05/2021

MFS\-64744

Criação do processo de limpeza dos registros gerados pelo sistema\.

Alessandra Cristina Navatta

# <a id="_Toc462320892"></a><a id="_Toc27038220"></a><a id="_Toc72497613"></a>INTRODUÇÃO* *

Criar o processamento de geração automática das informações da x147\_oper\_cred\. Esse processo será acionado através da tela Pré\-Geração a Partir dos Lantos Contábeis, no módulo de SPED/ EFD\-Escrituração Fiscal Digital das Contribuições\.

A pré\-geração é uma opção para os clientes que não querem carregar as informações através da importação da tabela SAFX147\- Demais documentos e Operações Geradoras de Crédito, pois possuem carregados dados na X01 e utilizam na tela de Dados Iniciais, a opção ‘‘Utilizar a parametrização da

‘Conta Contábil X Centro de Custo/CST/Operação/Nat\. Base de Crédito’, para a geração do registro F100\.

As informações que foram processadas por essa rotina, serão utilizadas para a geração do registro F100 do SPED Contribuições\.

# <a id="_Toc27038221"></a><a id="_Toc72497614"></a>DOCUMENTOS DE REFERÊNCIA

*MTZ\_Tela\_Parâmetros\_Dados\_Iniciais\.docx*

*MTZ\_SPED\_EFD\_CONTRIBUICOES\_Tela\_Parametrizacao\_F100\_Conta\_ContabilxCentro\_de\_Custo\_CST\_Oper\_Nat\.docx*

*MTZ\_EFD PIS\-COFINS\_Tela\_PreGeracao\_a\_Partir\_dos\_Lanctos\_Contabeis\.docx\.docx*

# <a id="_Toc27038222"></a><a id="_Toc72497615"></a>DEFINIÇÃO DAS REGRAS

__Número__

__Regra__

__Demanda__

RP00

Esta funcionalidade tem o propósito de preencher as informações na tabela x147\_oper\_cred, considerando as informações de lançamentos contábeis, existente na base, compreendidos no período da geração do processo, levando em consideração a opção ‘Utilizar a parametrização da  Conta Contábil X Centro de Custo/CST/Operação/Nat\. Base de Crédito’ definida em Dados Iniciais para a geração do registro F100 do produto Sped Contribuições\.

Este processo será executado através da tela Pré\-Geração a Partir dos Lanctos Contábeis, localizada no Menu: SPED, Módulo: Escrituração Fiscal Digital das Contribuições🡪 Manutenção🡪 Registro do Bloco F 🡪 Demais Documentos e Operações Geradoras de Contribuição e Créditos \(F100\) 🡪Pré\-Geração a Partir dos Lanctos Contábeis\.

Para o processamento, serão consideradas as informações dos parâmetros da tela \(Período,  Informações para o Registro F100, Empresa/Estabelecimento\), além da recuperação dos  lançamentos contábeis, quando a configuração da empresa/estabelecimento possuir na tela de Dados Iniciais, a opção ‘‘Utilizar a parametrização da Conta Contábil X Centro de Custo/CST/Operação/Nat\. Base de Crédito’, marcada,  para a geração do registro F100\.

Vale ressaltar que as informações da tabela x147\_oper\_cred, são utilizadas para a geração do SPED Contribuições registro F100\.

Caso já exista informações nas tabelas \(registros importados através da SAFX147\- Demais Documentos e Operações Geradoras de Crédito e ou digitados\), para o período processado, não iremos executar o processo\. A rotina apenas será executada se não houver registro no período ou se o registro existente foi gerado pelo próprio processo de pré\-geração \(neste caso, todos os registros serão sobrepostos\)\. 

Todos os registros criados por este processo, ficaram identificados que foram criados pelo sistema \(campo ind\_gravação igual a 7\)\.

MFS\-64743

RP01

__Processo de Geração:__

O objetivo é recuperar os registros de lançamentos contábeis que possuem direito a crédito de PIS/COFINS, consolidando os valores dos lançamentos por período, conta contábil e centro de custo\. Serão gravados registros na x147\_oper\_cred, quando essa consolidação de valores for um valor a crédito\. Os registros gravados, posteriormente, serão considerados na geração do registro F100 \- Demais documentos e Operações Geradoras de crédito\), no SPED Contribuições\.

O processo será realizado caso o campo ‘Informações para Registro F100’ na tela de pré\-geração, esteja com a opção ‘Gerar’ marcado

__Atenção:__ Consideraremos  lançamentos contábeis com direito ao crédito, os lançamentos que se enquadrarem nos filtros das parametrizações indicadas pelo usuário \(SPED> EFD\- Escrituração Fiscal Digital das Contribuições > Parâmetros > Registro F100 > Conta Contábil X Centro de Custo/CST/Operação/Nat\. Base de Crédito\)\. 

__Critérios da recuperação:__

- Empresa/Estabelecimento selecionado na tela de pré\-geração; 
- Período \(mês/ano\) indicado na tela de pré\-geração;
- Configuração do parâmetro ‘Registro F100 – Demais Documentos e Operações Geradoras de Contribuição e Crédito’ com a opção igual a ‘Utilizar a parametrização da Conta Contábil X Centro de Custo/CST/Operação/Nat\. Base de Crédito’ em Dados Iniciais para a empresa/estabelecimento indicado na tela de pré\-geração;
- Parametrização por ‘Conta Contábil X Centro de Custo/CST/Operação/Nat\. Base de Crédito’ para a empresa/estabelecimento, indicado na tela de pré\-geração;
- Lançamentos Contábeis \(SAFX01 \- Arquivo Contábil\-\), com o campo 17\-TIPO\_LANCTO diferente de ‘E\-Encerramento’ da empresa/estabelecimento indicado na tela de pré\-geração\.

__Recuperando os lançamentos contábeis com direito ao crédito de PIS/COFINS:__

- 
	- 
		1. Dados Iniciais e Parametrização

A partir do período indicado na tela da pré\-geração, verificar se há, para a empresa/estabelecimento que estamos executando o processo, parametrização configurada em dados iniciais igual a ‘Utilizar a parametrização da Conta Contábil X Centro de Custo/CST/Operação/Nat\. Base de Crédito’, para o parâmetro  Registro F100 – Demais Documentos e Operações Geradoras de Contribuição e Crédito:

Dados Iniciais:

- Se o parâmetro estiver marcado com: ‘Utilizar a parametrização do Tipo de Documento X CST/Operação/Nat\. Base de Crédito’, o processo será interrompido e exibiremos a mensagem no log \(indicada na regra do botão executar do documento ‘MTZ\_EFD PIS\-COFINS\_Tela\_PreGeracao\_a\_Partir\_dos\_Lanctos\_Contabeis\.docx’\);
- Caso o parâmetro esteja marcado com ‘Utilizar a parametrização da Conta Contábil X Centro de Custo/CST/Operação/Nat\. Base de Crédito’, consideraremos a parametrização que está no caminho: ‘ SPED> EFD\- Escrituração Fiscal Digital das Contribuições > Parâmetros > Registro F100>  Conta Contábil X Centro de Custo/CST/Operação/Nat\. Base de Crédito’\. Neste caso, verificar a parametrização, conforme regras abaixo:

Parametrização

- Se não existir parametrização por ‘Conta Contábil X Centro de Custo/CST/Operação/Nat\. Base de Crédito’

 Localizada em SPED> EFD\- Escrituração Fiscal Digital das Contribuições > Parâmetros > Registro F100> Conta Contábil X Centro de Custo/CST/Operação/Nat\. Base de Crédito, o processo será interrompido e exibiremos a mensagem no log \(indicada na regra do botão executar do documento ‘MTZ\_EFD PIS\-COFINS\_Tela\_PreGeracao\_a\_Partir\_dos\_Lanctos\_Contabeis\.docx’\)\. Encontrando a parametrização, seguir para o item 2 desta regra\.

- 
	- 
		1. Lançamentos Contábeis

Após verificar a existência da parametrização atendida por este processo, indicada nesta regra no item 1, deve ser verificado se existem lançamentos contábeis na base \(com o campo 17\-TIPO\_LANCTO diferente de ‘E\-Encerramento’\), para o período e empresa/estabelecimento indicados na tela de pré geração, conforme abaixo:

Caso não exista lançamentos contábeis no período, o processo será interrompido e exibiremos a mensagem no log \(indicada na regra do botão executar do documento ‘MTZ\_EFD PIS\-COFINS\_Tela\_PreGeracao\_a\_Partir\_dos\_Lanctos\_Contabeis\.docx’\)\. Encontrando a parametrização, seguir para o item 3 desta regra\.

- 
	- 
		1. Possíveis Lançamentos Contábeis elegíveis para x147\_oper\_cred

Após verificar a existência da parametrização e dos lançamentos contábeis na base, indicados nesta regra nos itens 1 e 2 desta regra, devemos filtrar os lançamentos que serão considerados para o PIS/COFINS, de acordo com a parametrização criada pelo usuário\.

- Apenas os lançamentos enquadrados pela parametrização serão considerados na gravação da x147\_oper\_cred\. Vale ressaltar que serão desprezados lançamentos do tipo de encerramento\.
	- 
		1. Consolidação dos Lançamentos Contábeis e criação do registro na x147\_oper\_cred

Considerando os lançamentos enquadrados pela parametrização \(item 3 desta regra\), consolidar os valores dos lançamentos contábeis por conta e centro de custo \(este último, quando existir\), referente ao período da geração e da empresa/estabelecimento selecionado na tela de pré\-geração\. Para a consolidação, efetuar a soma de todos os lançamentos a crédito __MENOS__ a soma de todos os lançamentos a débito, se o resultado for um valor a __crédito__, um registro será gravado na x147\_oper\_cred \(as regras da criação do registro, estão disponíveis na [RP02](#RP02)\), se o resultado for um valor a débito, nenhum registro desta conta e centro de custo será gravado pelo processo\. 

 

__Validações__

- Considerar as validações na [RP04](#RP04) \(Mensagens que devem ser apresentadas no Log do processamento e as \(indicadas na regra do botão executar do documento ‘MTZ\_EFD PIS\-COFINS\_Tela\_PreGeracao\_a\_Partir\_dos\_Lanctos\_Contabeis\.docx’\)\.

MFS\-64743

<a id="RP02"></a>RP02

Conforme informado anteriormente, após a consolidação dos valores dos lançamentos por conta e centro de custo, se o valor do lançamento consolidado for um valor a crédito, um registro será criado na x147\_oper\_cred\.

Gravar os registros na tabela x147\_oper\_cred, conforme regras indicadas nos respectivos campos indicado na tabela abaixo\.

Os dados gravados podem ser consultados na tela:   Menu Sped, Módulo: EFD Escrituração Fiscal Digital das Contribuições > Manutenção> Registro do Bloco F > Demais Documentos e Operações Geradoras de Contribuição e Créditos \(F100\) > Manutenção dos Registros\.

\(Tabela de Gravação dos Registros\)

Tabela

Obr

Item

Nome do Campo/Layout

Regra

SAFX147

\(\*\)

01

COD\_EMPRESA

Preencher com a informação do campo 01\-COD\_EMPRESA dos lançamentos recuperados da SAFX01\.

SAFX147

\(\*\)

02

COD\_ESTAB

Preencher com a informação do campo 02\-COD\_ESTAB dos lançamentos recuperados da SAFX01\.

SAFX147

\(\*\)

03

COD\_DOCTO

Gravar a informação fixa ’NF100’\.

SAFX147

 

04

IND\_FIS\_JUR

Não preencher\.

SAFX147

 

05

COD\_FIS\_JUR

Não preencher\.

SAFX147

 

06

IND\_PRODUTO

Não preencher\.

SAFX147

 

07

COD\_PRODUTO

Não preencher\.

SAFX147

\(\*\)

08

DATA\_OPER

Preencher com a data do último dia do mês indicado na tela de pré\-geração do processo\.

SAFX147

 

09

VLR\_OPER

Preencher com o valor consolidado dos lançamentos da conta e centro de custo que foram enquadrados pela parametrização\.

SAFX147

 

10

VLR\_BASE\_PIS

Preencher com o valor que foi consolidado para os lançamentos da conta e centro de custo \(que foram enquadrados pela parametrização\)\. Caso na parametrização tenha sido informado valor de PIS\.

SAFX147

 

11

VLR\_ALIQ\_PIS

Preencher com a informação da alíquota de PIS indicada na parametrização, cujos lançamentos foram enquadrados\. 

SAFX147

 

12

VLR\_PIS

Preencher com o resultado da multiplicação do campo 10\- VLR\_BASE\_PIS \(dos lançamentos consolidados\) \* campo 11 \- VLR\_ALIQ\_PIS

SAFX147

 

13

VLR\_BASE\_COFINS

Preencher com o valor que foi consolidado para os lançamentos da conta e centro de custo \(que foram enquadrados pela parametrização\)\. Caso na parametrização tenha sido informado valor de COFINS\.

SAFX147

 

14

VLR\_ALIQ\_COFINS

Preencher com a informação da alíquota de COFINS indicada na parametrização, cujos lançamentos foram enquadrados\. 

SAFX147

 

15

VLR\_COFINS

Preencher com o resultado da multiplicação do campo 13\- VLR\_BASE\_COFINS \(dos lançamentos consolidados\) \* campo 14 \- VLR\_ALIQ\_COFINS\.

SAFX147

 

16

IND\_ORIGEM\_CRED

Não preencher\.

SAFX147

 

17

COD\_CONTA

Preencher com a informação do campo 04\-CONTA\_DEB\_CRED dos lançamentos que foram recuperados\.

SAFX147

 

18

CENTRO\_CUSTO

Preencher com a informação do campo 09\-CENTRO\_CUSTO dos lançamentos que foram recuperados\.

SAFX147

 

19

DESC\_COMPL

Gerar fixo ‘Geracao Automatica Registro F100’\.

SAFX147

 

20

NUM\_DOCTO

Não preencher\.

SAFX147

 

21

SERIE

Não preencher\.

SAFX147

 

22

SUB\_SERIE

Não preencher\.

SAFX147

 

23

NUM\_LANCTO

Gerar o campo com a informação ‘GERAUT\_F100\_\_LANCTO\_<SEQ>’

Onde SEQ é um sequencial criado pelo sistema\.

SAFX147

 

24

COD\_NAT\_REC

Preencher com o Código da Natureza da Receita da parametrização que os lançamentos foram enquadrados\.

SAFX147

 

25

COD\_SCP

Não preencher\.

SAFX147

 

26

COD\_SITUACAO\_PIS

Preencher com o Código da Situação Tributária de PIS da parametrização que os lançamentos foram enquadrados\.

SAFX147

 

27

COD\_SITUACAO\_COFINS

Preencher com o Código da Situação Tributária de COFINS da parametrização que os lançamentos foram enquadrados\.

MFS\-64743

RP03

Todos os registros gravados na tabela x147\_oper\_cred , através deste processo \([RP02](#RP02)\), devem ser identificados que foram gerados pelo sistema, pois os registros importados \( SAFX147\- Demais Documentos e Operações Geradoras de Crédito \) não podem ser alterados \(por esse processo\)\. 

__Sugestão:__ utilizar o campo ind\_gravacao, com os domínios 

6\.  Gerado pelo Sistema

7\.  Gerado pelo Sistema / Atualizado por Digitação

8\. Gerado pelo Sistema / Atualizado por Importação

O domínio 7 deve ser considerado, quando o usuário ajustar uma informação que foi gerada pelo sistema\.

__Domínio completo do campo ind\_gravacao:__

		

Tipo/tamanho: CHAR\(1\)

Valores padrão do campo:

1\.  Incluído por Importação

2\.  Atualizado por Importação

3\.  Incluído por Importação / Atualizado por Digitação

4\.  Incluído por Digitação

5\.  Incluído por Digitação / Atualizado por Digitação

6\.  Gerado pelo Sistema

7\.  Gerado pelo Sistema  / Atualizado por Digitação

8\. Gerado pelo Sistema  / Atualizado por Importação

9\. Atualizado pelo Sistema

__Serão considerados registros oriundos de Importação os domínios:__

1\.  Incluído por Importação  
2\.  Atualizado por Importação  
3\.  Incluído por Importação / Atualizado por Digitação

  
 __ Serão considerados registros oriundos de Digitação os domínios:__

4\. Incluído por Digitação

5\.  Incluído por Digitação / Atualizado por Digitação

MFS\-64743

<a id="Sugestao_Ind_Gravacao"></a><a id="RP04"></a>RP04

__Mensagens que devem ser apresentadas no Log do processamento:__

- Se existir informações no período para a tabela x147\_oper\_cred \(registros de origem via importação ou digitação\), o processo não será realizado\. Exibir a mensagem: “Existem dados importados através da SAFX147\- Demais documentos e Operações Geradoras de crédito, ou que foram digitados, para o período por isso, o processo não será realizado”\.

Atenção: Para identificarmos que um registro foi importado pela SAFX147 ou inserido via manutenção, consideraremos a regra a seguir:

- 
	- Tipo de Documento deve ser diferente de ‘NF100’ e o ind\_gravação diferente de 6,7, e 8\.

MFS\-64743

RP05

__Processo de Exclusão:__

O processo será realizado caso o campo ‘Informações para Registro F100’ na tela de pré\-geração, esteja com a opção ‘Gerar’ ou ‘Limpar’ marcado\.

Quando a opção gerar estiver selecionada, a exclusão ficará transparente para o usuário\. Esta funcionalidade será necessária, para evitarmos eventuais divergências de informações\.

O processo consiste em apagar da base, todos os registros que foram gerados automaticamente por este processo, considerando o período e a empresa/estabelecimento indicado na tela de pré\-geração\. 

MFS\-64744


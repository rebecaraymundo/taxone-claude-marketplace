# MTZ-PIM-Apuracao-Transporte_Saldos_Credito_Estimulo_Calculo

- **Fonte:** MTZ-PIM-Apuracao-Transporte_Saldos_Credito_Estimulo_Calculo.docx
- **Modificado:** 2021-03-30
- **Tamanho:** 66 KB

---

THOMSON REUTERS

PIM \- Gestão do Controle de Incentivos Fiscais do Pólo Industrial de Manaus

Rotina de Cálculo do Transporte de Saldos/ Crédito Estímulo

 

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS2006

Julyana Perrucini

Este documento tem como objetivo alterar a rotina de cálculo do Transporte de Saldos/ Crédito Estímulo da obrigação acessória Gestão de Controle de Incentivos Fiscais Pólo Industrial de Manaus \(Apuração do Amazonas\) passando a considerar os valores dos lançamentos complementares via parametrização\.

		REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN01

__Funcionalidade:__

Nesta rotina são realizadas duas tarefas, inicialmente são efetuados os transportes dos saldos credores remanescentes do período anterior, em que é importante que este transporte seja efetuado em rateio entre as linhas de incentivo credoras, uma vez que o crédito final apurado sempre representa a totalização de todas as apurações\. Para que seja possível o transporte do saldo, deve\-se indicar a estrutura e item pertencente aos componentes 02 e 04, correspondentes às entradas incentivadas e não\-incentivadas, e que estejam associadas a conta gráfica 009, Saldo Credor do Período Anterior do RAICMS\. Após o transporte dos saldos, será feito o cálculo do crédito estímulo, conforme a legislação vigente, e é importante que, para efetivo cálculo conforme enquadramento de cada contribuinte, deve\-se indicar a Lei na qual o estabelecimento está enquadrado, esta informação é indicada no menu Cadastros >> Linhas de Incentivo >> Parâmetros de Cálculo por Linha\.

MFS2006

RN02

__Operação:__

Nesta rotina o usuário irá informar o período para geração e os códigos de estruturas e itens relacionados aos Saldos Credores apurados nos livros: incentivado e não incentivado, ou seja, informar:

Componente 02 – Entradas Incentivadas

Estrutura\-item: 02\-001 – Saldo Credor do Período Anterior

Componente 04 – Entradas Não\-incentivadas

Estrutura\-item: 02\-001 – Saldo Credor do Período Anterior

MFS2006

RN03

__Definição:__

Esta rotina realiza três funções, a saber:

__Transporte do Saldo:__

Nesta primeira fase o objetivo será recuperar o saldo da apuração anterior na tabela ICT\_AM\_SLD\_APUR, no menu Apuração >> Transp\. Saldos/ Crédito Estímulo >> Cadastro, para gravação na tabela ICT\_AM\_AP\_E\_S, esta tabela contém os totais do ICMS por Componente/Estrutura/Item apurados mensalmente\. Os componentes tratados nesta rotina são 01, 02, 03 e 04 \(Entradas e Saídas incentivadas e não incentivadas\)\.

__\[ALTERADA – MFS2006\]__

__Cálculo do ICMS a Restituir:__

Esta rotina realiza o cálculo do componente 33, totalizando os valores da tabela ICT\_AM\_AP\_E\_S \(campo VLR\_ICMS\) para os componentes 01 \(débitos\) e 02 \(créditos\), este cálculo é realizado para cada linha de incentivo existente na tabela\. 

O saldo apurado considera \(crédito\-débito\) mais os valores dos lançamentos complementares, quando o campo “Considerar Lançamento para Cálculo de Transp\. Saldos/ Crédito Estímulo” estiver marcado, no menu Apuração >> Apuração dos Saldos de Impostos e Taxas >> Lançamentos Complementares >> Apuração ICMS \(Aba Lançamento de Valores\), e são gravados na tabela ICT\_AM\_SLD\_APUR, seguindo a regra abaixo:

__Saldo Negativo \(débito > crédito\):__

Neste Caso será recuperado da tabela ICT\_AM\_LINHAP os percentuais mínimo e máximo de incentivo \(campos VLR\_PERC\_REDUC e VLR\_PERC\_MAX\) para a inscrição e linha de incentivo gerada, em seguida o tipo de incentivo será recuperado da tabela ICT\_AM\_PAR\_ESTAB, este tipo de incentivo define a Lei na qual o cliente está enquadrado\. 

__Atenção:__ A rotina de cálculo do Crédito Estímulo não considerava os Lançamentos Complementares realizados manualmente na Apuração do ICMS, o que dava diferença entre o saldo calculado na opção Crédito Estímulo e o saldo apresentado na Apuração do ICMS\. Nesse caso, se o usuário tinha um lançamento, que não estava contemplado nos Mapas Acessórios, e o mesmo utilizava a opção de Lançamentos Complementares, estes lançamentos não eram considerados no Cálculo do Crédito Estímulo, somente na Apuração do ICMS\. A partir da alteração realizada pela MFS2006 o usuário poderá optar pela informação de incluir os lançamentos complementares no cálculo do Crédito Estímulo, mas deverá ser feita uma parametrização ou outra, ou seja, por lançamento ou por mapas acessórios, para que não ocorra duplicidade nos valores a serem apresentados\. Esse ponto de atenção será colocado no manual de orientação do módulo\.

MFS2006

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN


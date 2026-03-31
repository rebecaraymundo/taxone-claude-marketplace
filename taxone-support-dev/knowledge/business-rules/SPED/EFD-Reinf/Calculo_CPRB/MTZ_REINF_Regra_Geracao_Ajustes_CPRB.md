# MTZ_REINF_Regra_Geracao_Ajustes_CPRB

- **Fonte:** MTZ_REINF_Regra_Geracao_Ajustes_CPRB.docx
- **Modificado:** 2025-10-20
- **Tamanho:** 87 KB

---

 

THOMSON REUTERS

Módulo EFD\-REINF

Regra de recuperação dos Ajustes – SAFX252

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS15093

Lara Aline

Regra de recuperação das informações dos ajustes\. Primeiramente para o Ajustes 6 \- Vendas Canceladas e os descontos incondicionais concedidos\. \(SAFX252\)\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN00

__Regras Gerais__

Essa rotina tem por finalidade efetuar a geração automática dos ajustes da CPRB\. Esses ajustes serão lançados na SAFX252 da mesma forma que é feito atualmente se incluído o ajuste manualmente pela tela de manutenção da CPRB\.

\- Deverão ser consideradas todas as validações abaixo para compor o Log do Processo:

__1 –__ Caso o valor do ajuste de redução encontrado seja maior que o Valor da Receita Bruta do Estabelecimento \(VLR\_REC\_BRT\_ATIV da SAFX185\), será gravada a seguinte mensagem de erro no log do processo:

*“O valor do ajuste de redução é maior que o valor da Receita Bruta do Estabelecimento\. Nesse caso será gravado o valor 0 \- zero\.”\. *

O log exibirá os dados de identificação da nota fiscal em questão \(Número de nota fiscal/Série/SubSérie e Data fiscal\), para que o usuário possa conferir os dados\.

MFS15093

RN01

__Processamento dos Dados__

__Origem dos Dados:__ Tabela dos Documentos Fiscais \(SAFX08/SAFX09\)

                                  Parametrização dos Ajustes da CPRB \(menu Parâmetros > CPRB > Parametrização dos Ajustes da CPRB > Por CFOP ou CFOP/Natureza __\(\*\)__

                                  Parametrização dos Ajustes da CPRB \(menu Parâmetros > CPRB > Parametrização dos Ajustes da CPRB > Serviço __\(\*\*\)__

__Destino:__ Tabela SAX252 \- Ajuste da Contribuição Previdenciária Apurada__\.__

__               __Tabela SAX185 \- Apuração da Contribuição Previdenciária sobre a Receita Bruta – Bloco P__\.__

__O processamento é por Estabelecimento\.__

Para cada Estabelecimento, será calculado o valor total de cada ajuste\. 

O Processamento é de acordo com as notas do período de referência informado em tela\.

__Origem das informações para SAFX252:__

01

COD\_EMPRESA

Será a informação da empresa do login, vinculada ao estabelecimento carregado na tela “Geração dos Ajustes da CPRB”\.

02

COD\_ESTAB

Será a informação do estabelecimento carregado na tela “Geração dos Ajustes da CPRB”\.

03

DATA\_INI

Será a informação da data inicial carregado na tela “Geração dos Ajustes da CPRB”\.

04

COD\_ATIV\_CONT\_PREV

Será o Código de Atividade vinculado na parametrização dos ajustes __\(\*\) \(\*\*\)__\.

05

COD\_RECEITA

Será o Código de Receita vinculado na parametrização dos ajustes __\(\*\) \(\*\*\)__\.

06

COD\_CONTA

Essa informação não será gerada, como se trata de informação chave gravar nulo \(espaço branco\)\.

07

IND\_AJ\_REINF

Será a informação de Tipo de Ajustes vinculado na parametrização dos ajustes __\(\*\) \(\*\*\)__\.

08

COD\_AJ\_REINF

Será a informação de Código de Ajuste carregado na tela “Geração dos Ajustes da CPRB”\.

09

VL\_AJ\_REINF

Será o valor encontrado na totalização dos ajustes descritos nas regras de recuperação dos documentos

10

DSC\_AJ\_REINF

Gravar a descrição de acordo com o código de ajuste conforme abaixo:

1 \- Adoção Reg\. Caixa

2 – Dif\. Val\. a recolher

3 \- Adição Dif\. Per Ant

4 \- Exportações diretas

5 \- Transp Inter Cargas

6 \- Vendas Canc e Desc\.

7 \- IPI, Receita Bruta

8 \- ICMS, cob vendedor

9 \- Rec\.bruta rec const

10 \- Valor aporte recur\.

11 \- Demais Ajustes

Obs: Caso o código de ajuste for 12 ou 13 deverá gravar a mesma descrição do código 11 \- Demais Ajustes\.

11

DT\_REF\_REINF

Será a informação da data inicial carregado na tela “Geração dos Ajustes da CPRB”\.

12

VLR\_ALIQ\_CONT\_PREV

Será o valor de alíquota gravado na SAFX185 através do Calculo da CPRB\.

__Importante__: Sempre que o processo for efetuado pela rotina automática dos ajustes, as informações e ajustes encontrados irão sobrescrever as informações anteriormente carregadas para o ajuste, período e atividade que o usuário efetuar a geração\. Ou seja, o ajuste efetuado anteriormente pelo processo manual será descartado e substituído pelo ajuste no processo automático\.

A seguir serão definidas as regras desse processamento\.

MFS15093

RN02

__Critérios para a recuperação dos documentos__

__Tipo de Ajuste: Ajuste de redução __

__Código do Ajuste = 6 \- Vendas canceladas e os descontos incondicionais concedidos:__

    \- Empresa = código da empresa do login;

    \- Estabelecimento = código do estabelecimento da geração; 

    \- Data Emissão = deve ser uma data referente ao período informado em tela;

    \- Somente notas não canceladas;

    \- Classificação fiscal = 1, 2 ou 3;

    \- Considerar todas as notas que:

- O CFOP ou CFOP/Natureza estejam cadastrados na Parametrização dos Ajustes da CPRB __\(\*\)__ para a Tipo de Ajuste = ‘Ajuste de redução’ e Código do Ajuste = ‘6 \- Vendas canceladas e os descontos incondicionais concedidos’ __ou__
- O Serviço estejam cadastrados na Parametrização dos Ajustes da CPRB __\(\*\*\)__ para a Tipo de Ajuste = ‘Ajuste de redução’ e Código do Ajuste = ‘6 \- Vendas canceladas e os descontos incondicionais concedidos’\.

Obs\.: Essa rotina de recuperação será efetuada após o cálculo da CPRB, ou seja, as informações serão previamente levantadas para o período/estabelecimento e a partir dela encontraremos a informação do/s Código de Atividade para geração do R\-2060 \(SAFX185\)\.

Para cada CFOP ou CFOP/Natureza e Serviço parametrizado o usuário vinculará o Código de Atividade pertencente, e a totalização dessas notas se fará pelo código de Atividade parametrizado\.

__Totalização do Valor de Ajuste:__

Para cada item a ser totalizado por Código de Atividade:

Caso encontrado valor informado no campo* *VLR\_DESCONTO da SAFX08/SAFX09 será recuperado o valor do campo VLR\_DESCONTO SAFX08/SAFX09\.

Caso contrário, será recuperado o valor do \(campo VLR\_CONTAB\_ITEM das notas de saída SAFX08 \(CFOP/CFOP/Natureza __\(\*\)__\) ou campo VLR\_TOT das notas de saída SAFX09 \(Serviço __\(\*\*\)__\)\)\. 

Esse valor será gravado no campo Valor de Ajuste \(VL\_AJ\_REINF – SAFX252\)\.

     

__Cálculo do Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta \(SAFX185\):__

     

Para cada item processado, calcular o Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta da seguinte forma: 

       Valor totalizado da Ajuste por Atividade = Será o valor recuperado da Totalização do Valor de Ajuste descrita acima\. 

       *Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta* = Valor da Receita Bruta do Estabelecimento \(VLR\_REC\_BRT\_ATIV – SAFX185\) – Valor totalizado da Ajuste por Atividade\.  

__Importante__: Para esse ajuste como se trata de um ajuste de redução o valor será deduzido da Receita da Atividade, mas deverão ser totalizados ao final todos os ajustes de redução encontrados para a atividade e período, tanto via processo manual quanto via processo automático para popular a informação do campo \(VLR\_EXC\_REC\_BRT \- SAFX185\) e o campo Valor Ajuste Exclusão do quadro Valores EFD\-REINF da tela de manutenção da CPRB \- Contribuição Previdenciária Sobre a Receita Bruta\. 

Após essa totalização esse será o valor final totalizado que será deduzido do campo \(VLR\_REC\_BRT\_ATIV \- SAFX185\) para encontrarmos o Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta \(VLR\_BASE\_CONT\_PREV – SAFX185\)\.

__Cálculo do Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta na tela de manutenção da CPRB:__

*Campo Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta do quadro ‘Valores EFD – Contribuições’: *

Nesse campo serão apenas deduzidos os ajustes de redução, ajustes de acréscimo não serão considerados no cálculo desse campo\.

Valor totalizado da Ajuste por Atividade = Será o valor recuperado da Totalização do Valor de Ajuste descrita acima\.

*Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta* = Valor da Receita Bruta do Estabelecimento \(VLR\_REC\_BRT\_ATIV – SAFX185\) – Valor totalizado da Ajuste por Atividade

*Campo Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta do quadro ‘Valores EFD – REINF’: *

Nesse campo serão considerados todos os ajustes, deduzidos os ajustes de redução e somados os ajustes de acréscimo no cálculo desse campo\.

Valor totalizado da Ajuste por Atividade = Será o valor recuperado da Totalização do Valor de Ajuste descrita acima\.

*Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta* = Valor da Receita Bruta do Estabelecimento \(VLR\_REC\_BRT\_ATIV – SAFX185\) – Valor totalizado da Ajuste por Atividade

MFS15093

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


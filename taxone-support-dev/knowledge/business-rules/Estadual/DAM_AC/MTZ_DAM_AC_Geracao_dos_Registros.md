# MTZ_DAM_AC_Geracao_dos_Registros

- **Fonte:** MTZ_DAM_AC_Geracao_dos_Registros.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 78 KB

---

THOMSON REUTERS

DAM\-AC

Geração dos Registros

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS1680

Julyana Perrucini

Este documento tem como objetivo criar o módulo DAM\-AC\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN00

__Regra Geral__

__Origem das informações para geração:__ 

- Tela de Empresa/Estabelecimento do módulo Básicos – Parâmetros \(tabela estabelecimento\), localizado no item de menu: Preliminares >> Empresa/Estabelecimento\.
- Tela de Inscrições Estaduais do módulo Básicos – Parâmetros \(tabela registro\_estadual\), localizado no item de menu: Preliminares >> Inscrições Estaduais\.
- Tela de <a id="OLE_LINK13"></a><a id="OLE_LINK14"></a><a id="OLE_LINK15"></a>Empresas/Estabelecimentos c/ Insc\. Estadual Única do módulo Estadual – <a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a>Controle de Obrigações Acessórias \(tabela icp\_insc\_est\_centr\), localizado no item de menu: Obrigações >> Empresas/Estabelecimentos c/ Insc\. Estadual Única\.
- Parâmetros p/Geração dos Dados Acessórios do módulo Estadual – DAM\-AC \(tabela est\_par\_dados\_acs\), localizado no item de menu: Parâmetros >> Parâmetros p/Geração dos Dados\.
- Resumo das Operações por CFOP/Alíquota do módulo Estadual – Obrigações Acessórias \(tabela est\_res\_uf\_01\), localizado no item de menu: Relatórios >> Resumo das Operações;
- Resumo do item de Apuração do ICMS do módulo Estadual – ICMS \(tabela item\_apurac\_calc\), localizado no item de menu: DATA MART >> Apuração do ICMS >> Ajuste SINIEF/ Ajuste SINIEF – Multiempresa ou se for por “__Geração centralizada por Inscrição Estadual Única__” considerar o Resumo do item de Apuração do ICMS por Inscrição Estadual Única, localizado no item de menu: DATA MART >> Livros Fiscais p/ Empresas c/ Insc\. Estadual Única >> Apuração do ICMS – Convênio ICMS;
- Lançamentos Complementares da Apuração do ICMS do módulo Estadual – ICMS \(tabela item\_apurac\_discr\), localizado no item de menu: Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF ou se for por “__Geração centralizada por Inscrição Estadual Única__” considerar os Lançamentos Complementares da Apuração do ICMS por Inscrição Estadual Única, localizado no item de menu: localizado no item de menu: Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Empresas c/ Insc\. Estadual Única\.

__Regra de seleção geral: __

- <a id="OLE_LINK8"></a><a id="OLE_LINK9"></a>Resumo das Operações por CFOP/Alíquota:
	- A empresa e o estabelecimento devem compreender a empresa e o estabelecimento preenchidos na tela de geração dos registros;
	- A data de apuração do resumo deve compreender a data inicial e final preenchidas na tela de geração dos registros;
- Quando o parâmetro “__Geração centralizada por Inscrição Estadual Única__” estiver selecionado, recuperar as informações de todos os estabelecimentos cadastrados na tabela icp\_insc\_est\_centr referentes ao estabelecimento centralizador escolhido na tela de geração\.
- Resumo do Item de Apuração do ICMS e Lançamentos Complementares da Apuração do ICMS:
	- A empresa e o estabelecimento devem compreender a empresa e o estabelecimento preenchidos na tela de geração dos registros;
	- A data de apuração do resumo deve compreender a data inicial e final preenchidas na tela de geração dos registros;
- Quando o parâmetro “__Geração centralizada por Inscrição Estadual Única__” estiver selecionado, recuperar as informações de todos os estabelecimentos cadastrados na tabela icp\_insc\_est\_centr referentes ao estabelecimento centralizador escolhido na tela de geração\.

__Regra de gravação geral: __Verificar as RN a seguir para obtenção dos resultados, os dados a ser considerados são do estabelecimento em questão, exceto se a geração for por Inscrição Estadual Única, pois nesse caso de geração, os dados cadastrais a ser considerados são do estabelecimento centralizador e deverão ser realizados os acúmulos de valores de seus centralizados\.

__Regra de agrupamento: __Não se aplica\.

__Ordenação: __Não se aplica\.

__Considerações:__ Não é obrigatório o cliente ter o módulo “Obrigações Acessórias”, então o intuito é executar a geração a partir do DAM\-AC, de acordo com o parâmetro Gerar Dados Acessórios da tela de geração dos registros, para obtenção das informações do Resumo das Operações por CFOP/Alíquota \(tabela est\_res\_cfo\_ali\_01\), sendo necessária a parametrização em Parâmetros p/Geração dos Dados Acessórios do módulo Estadual – DAM\-AC, pois essa rotina é padrão e utilizada nas demais obrigações estaduais\. Por esse motivo, no preenchimento dos campos utilizaremos a forma “funcional” e “técnica”, ou seja, resumo e a tabela do resumo\.

MFS1680

__Regra detalhada para recuperação no Resumo das Operações por CFOP/Alíquota:__

RN01

__Regra Entradas do Estado a 17% e 25%__

Para recuperar as informações de entradas do estado deverão ser considerados os seguintes critérios:

- CFOP iniciado com 1;
- Valor Alíquota deve ser igual a 17,00 e 25,00;
- Valor Isenta deve ser igual a zero;
- Valor Outras deve ser igual a zero;
- Valor ICMSS deve ser igual a zero;

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma dos valores por CFOP e Alíquota, ou seja, para 17% e 25% de acordo com o CFOP pré\-determinado, considerando também na soma os campos de Valor Contábil, Base de Cálculo, Isentas ou Não Tributadas, Outras e Valor do Imposto das operações internas geradas\.

__Regra de agrupamento: __CFOP, Valor Alíquota\.

__Ordenação: __Não se aplica\.

MFS1680

RN02

__Regra Entradas do Estado Substituição Tributária__

Para recuperar as informações de entradas do estado com Substituição Tributária deverão ser considerados os seguintes critérios:

- CFOP iniciados com 1;
- Valor ICMSS deve ser maior que zero;

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma dos valores de Substituição Tributária por CFOP de acordo com o CFOP pré\-determinado, considerando também na soma os campos de Valor Contábil, Base de Cálculo, Isentas ou Não Tributadas, Outras e Valor do Imposto das operações internas geradas\.

__Regra de agrupamento: __CFOP\.

__Ordenação: __Não se aplica\.

MFS1680

RN03

__Regra Entradas do Estado Outras__

Para recuperar as informações de entradas do estado com Outras operações deverão ser considerados os seguintes critérios:

- CFOP iniciados com 1;
- Valor Isenta deve ser maior que zero;
- Valor Outras deve ser maior que zero;

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma dos valores de Isentas ou Não Tributadas e Outras por CFOP de acordo com o CFOP pré\-determinado, considerando também na soma os campos de Valor Contábil, Base de Cálculo e Valor do Imposto das operações internas geradas\.

__Regra de agrupamento: __CFOP\.

__Ordenação: __Não se aplica\.

MFS1680

RN04

__Regra Entradas de Outros Estados a 7% e 12%__

Para recuperar as informações de entradas de outros estados deverão ser considerados os seguintes critérios:

- CFOP iniciado com 2;
- Valor Alíquota deve ser igual a 7,00 e 12,00;
- Valor Isenta deve ser igual a zero;
- Valor Outras deve ser igual a zero;

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma dos valores por CFOP e Alíquota, ou seja, para 7% e 12% de acordo com o CFOP pré\-determinado, considerando também na soma os campos de Valor Contábil, Base de Cálculo, Isentas ou Não Tributadas, Outras e Valor do Imposto das operações interestaduais geradas\.

__Regra de agrupamento: __CFOP, Valor Alíquota\.

__Ordenação: __Não se aplica\.

MFS1680

RN05

__Regra Entradas de Outros Estados Substituição Tributária a 7% e 12%__

Para recuperar as informações de entradas de outros estados com Substituição Tributária deverão ser considerados os seguintes critérios:

- CFOP iniciado com 2;
- Valor Alíquota deve ser igual a 7,00 e 12,00;
- Valor Isenta deve ser igual a zero;
- Valor Outras deve ser igual a zero;
- Valor ICMSS deve ser igual a zero;

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma dos valores de Substituição Tributária por CFOP e Alíquota, ou seja, para 7% e 12% de acordo com o CFOP pré\-determinado, considerando também na soma os campos de Valor Contábil, Base de Cálculo, Isentas ou Não Tributadas, Outras e Valor do Imposto das operações interestaduais geradas\.

__Regra de agrupamento: __CFOP, Valor Alíquota\.

__Ordenação: __Não se aplica\.

MFS1680

RN06

__Regra Entradas de Outros Estados Outras__

Para recuperar as informações de entradas de outros estados com Outras operações deverão ser considerados os seguintes critérios:

- CFOP iniciado com 2;
- Valor Isenta deve ser maior que zero;
- Valor Outras deve ser maior que zero;

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma dos valores de Isentas ou Não Tributadas e Outras por CFOP de acordo com o CFOP pré\-determinado, considerando também na soma os campos de Valor Contábil, Base de Cálculo e Valor do Imposto das operações interestaduais geradas\.

__Regra de agrupamento: __CFOP\.

__Ordenação: __Não se aplica\.

MFS1680

RN07

__Regra Entradas do Exterior__

Para recuperar as informações de entradas de operações do exterior deverão ser considerados os seguintes critérios:

- CFOP iniciado com 3;

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma dos valores por operações do Exterior por CFOP de acordo com o CFOP pré\-determinado, considerando também na soma os campos de Valor Contábil, Base de Cálculo, Isentas ou Não Tributadas, Outras e Valor do Imposto das operações geradas\.

__Regra de agrupamento: __CFOP\.

__Ordenação: __Não se aplica\.

MFS1680

RN08

__Regra Saídas para o Estado a 17% e 25%__

Para recuperar as informações de saídas para o estado deverão ser considerados os seguintes critérios:

- CFOP iniciado com 5;
- Valor Alíquota deve ser igual a 17,00 e 25,00;
- Valor Isenta deve ser igual a zero;
- Valor Outras deve ser igual a zero;
- Valor ICMSS deve ser igual a zero;

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma dos valores por CFOP e Alíquota, ou seja, para 17% e 25% de acordo com o CFOP pré\-determinado, considerando também na soma os campos de Valor Contábil, Base de Cálculo, Isentas ou Não Tributadas, Outras e Valor do Imposto das operações internas geradas\.

__Regra de agrupamento: __CFOP, Valor Alíquota\.

 

__Ordenação: __Não se aplica\.

MFS1680

RN09

__Regra Saídas para o Estado Substituição Tributária__

Para recuperar as informações de saídas para o estado com Substituição Tributária deverão ser considerados os seguintes critérios:

- CFOP iniciados com 5;
- Valor ICMSS deve ser maior que zero;

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma dos valores de Substituição Tributária por CFOP de acordo com o CFOP pré\-determinado, considerando também na soma os campos de Valor Contábil, Base de Cálculo, Isentas ou Não Tributadas, Outras e Valor do Imposto das operações internas geradas\.

__Regra de agrupamento: __CFOP\.

__Ordenação: __Não se aplica\.

MFS1680

RN10

__Regra Saídas para o Estado Outras__

Para recuperar as informações de saídas para o estado com Outras operações deverão ser considerados os seguintes critérios:

- CFOP iniciados com 5;
- Valor Isenta deve ser maior que zero;
- Valor Outras deve ser maior que zero;
- Valor ICMSS deve ser igual a zero;

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma dos valores de Isentas ou Não Tributadas e Outras por CFOP de acordo com o CFOP pré\-determinado, considerando também na soma os campos de Valor Contábil, Base de Cálculo e Valor do Imposto das operações internas geradas\.

__Regra de agrupamento: __CFOP\.

__Ordenação: __Não se aplica\.

MFS1680

RN11

__Regra Saídas para Outros Estados a 12%__

Para recuperar as informações de saídas para outros estados deverão ser considerados os seguintes critérios:

- CFOP iniciado com 6;
- Valor Alíquota deve ser igual a 12,00;
- Valor Isenta deve ser igual a zero;
- Valor Outras deve ser igual a zero;
- Valor ICMSS deve ser igual a zero;

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma dos valores de Alíquota a 12% por CFOP de acordo com o CFOP pré\-determinado, considerando também na soma os campos de Valor Contábil, Base de Cálculo, Isentas ou Não Tributadas, Outras e Valor do Imposto das operações interestaduais geradas\.

__Regra de agrupamento: __CFOP\.

__Ordenação: __Não se aplica\.

MFS1680

RN12

__Regra Saídas para Outros Estados Substituição Tributária__

Para recuperar as informações de saídas para outros estados com Substituição Tributária deverão ser considerados os seguintes critérios:

- CFOP iniciados com 6;
- Valor ICMSS deve ser maior que zero;

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma dos valores de Substituição Tributária por CFOP de acordo com o CFOP pré\-determinado, considerando também na soma os campos de Valor Contábil, Base de Cálculo, Isentas ou Não Tributadas, Outras  e Valor do Imposto das operações interestaduais geradas\.

__Regra de agrupamento: __CFOP\.

__Ordenação: __Não se aplica\.

MFS1680

RN13

__Regra Saídas para Outros Estados Devolução__

Para recuperar as informações de saídas para outros estados de devolução deverão ser considerados os seguintes critérios:

- CFOP parametrizados em Parâmetros >> Devolução >> CFOP do módulo do DAM;

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma dos valores de operações de Devolução por CFOP de acordo com o CFOP pré\-determinado, considerando na soma os campos de Valor Contábil, Base de Cálculo, e Isentas ou Não Tributadas, Outras e Valor do Imposto das operações interestaduais geradas\.

__Regra de agrupamento: __CFOP\.

__Ordenação: __Não se aplica\.

MFS1680

RN14

__Regra Saídas para o Estado Outras__

Para recuperar as informações de saídas para o estado com Outras operações deverão ser considerados os seguintes critérios:

- CFOP iniciados com 6;
- Valor Isenta deve ser maior que zero;
- Valor Outras deve ser maior que zero;
- Valor ICMSS deve ser igual a zero;

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma dos valores de Isentas ou Não Tributadas e Outras por CFOP de acordo com o CFOP pré\-determinado, considerando também na soma os campos de Valor Contábil, Base de Cálculo e Valor do Imposto das operações interestaduais geradas\.

__Regra de agrupamento: __CFOP\.

__Ordenação: __Não se aplica\.

MFS1680

RN15

__Regra Saídas para o Exterior__

Para recuperar as informações de saídas de operações do exterior deverão ser considerados os seguintes critérios:

- CFOP iniciado com 7;

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma dos valores por operações para o Exterior por CFOP de acordo com o CFOP pré\-determinado, considerando também na soma os campos de Valor Contábil, Base de Cálculo, Isentas ou Não Tributadas, Outras e Valor do Imposto das operações geradas\.

__Regra de agrupamento: __CFOP\.

__Ordenação: __Não se aplica\.

MFS1680

__Regra detalhada para recuperação no Resumo do Item de Apuração do ICMS \(Livros 108 e 165\):__

RN16

__Regra Crédito do Imposto – Entrada c/ Créditos__

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma do valor da apuração de código de operação igual a “005”\.

__Regra de agrupamento: __Não se aplica\.

__Ordenação: __Não se aplica\.

MFS1680

RN17

__Regra Crédito do Imposto – Saldo Credor do Mês Anterior__

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma do valor da apuração de código de operação igual a “009”\.

__Regra de agrupamento: __Não se aplica\.

__Ordenação: __Não se aplica\.

MFS1680

RN18

__Regra Débito do Imposto – Saída c/ Débito__

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma do valor da apuração de código de operação igual a “001”\.

__Regra de agrupamento: __Não se aplica\.

__Ordenação: __Não se aplica\.

MFS1680

__Regra detalhada para recuperação nos Lançamentos Complementares \(Livros 108 e 165\):__

RN19

__Regra Crédito do Imposto – Outros Créditos__

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma do valor do lançamento complementar da apuração de código de operação igual a “006”\.

__Regra de agrupamento: __Não se aplica\.

__Ordenação: __Não se aplica\.

MFS1680

RN20

__Regra Crédito do Imposto – Estorno de Débito__

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma do valor do lançamento complementar da apuração de código de operação igual a “007”\.

__Regra de agrupamento: __Não se aplica\.

__Ordenação: __Não se aplica\.

MFS1680

RN21

__Regra Débito do Imposto – Estorno de Crédito__

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma do valor do lançamento complementar da apuração de código de operação igual a “003”\.

__Regra de agrupamento: __Não se aplica\.

__Ordenação: __Não se aplica\.

MFS1680

RN22

__Regra Débito do Imposto – Outros Débitos__

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma do valor do lançamento complementar da apuração de código de operação igual a “002”\.

__Regra de agrupamento: __Não se aplica\.

__Ordenação: __Não se aplica\.

MFS1680

RN23

__Regra Débito do Imposto – Deduções__

__Regra de gravação:__ Deverá ser armazenada em uma tabela a soma do valor do lançamento complementar da apuração de código de operação igual a “012”\.

__Regra de agrupamento: __Não se aplica\.

__Ordenação: __Não se aplica\.

MFS1680

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN


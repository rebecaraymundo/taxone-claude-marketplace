# MTZ_Tela_Calculo_Automacao_Dev_Venda

> Fonte: MTZ_Tela_Calculo_Automacao_Dev_Venda.docx






THOMSON REUTERS

Matriz da tela de Parametrização por Produto



DOCUMENTO DE REQUISITO


Sumário

1.	TELA A SER DESENVOLVIDA	3
1.1.	Diagrama de Casos de Uso	3
1.1.1.	UC001 – Manutenção da Estrutura Padrão	3
1.1.1.1.1.	Fluxo Principal	4
1.1.1.1.2.	Fluxo Alternativo 1 – Novo Registro	4
2.	Regras dos Campos	4

## TELA A SER DESENVOLVIDA


[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir]

### Diagrama de Casos de Uso




### UC001 – Manutenção da Estrutura Padrão


[Descrever a ação deste caso de uso.

Ex.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão.]



#### Fluxo Principal



#### Fluxo Alternativo 1 – Novo Registro




## Regras dos Campos


Localização da tela:
Módulo: SPED >> EFD – Escrituração Fiscal Digital das Contribuições
Menu: Obrigações >> Automação Devolução de Venda – Regime Cumulativo (Segmento Cigarro)

Título da tela: Automação Devolução de Venda – Regime Cumulativo (Segmento Cigarro)

Funcionamento da tela: esta tela foi criada para possibilitar ao usuário a identificação das NFs de devolução de produtos do regime cumulativo para posterior geração de ajustes na apuração da contribuição do PIS e da COFINS (M220/M225 e M620/M625).

No acesso à tela o sistema deve exibir a tela padrão de seleção da apuração que será ajustada:



O sistema deve demonstrar apenas as apurações com Situação “Realizada”
Na barra de ferramentas, deve existir o botão de seleção  que abre a tela “Selecionar Apuração”, caso o usuário queira alternar entre as apurações.

No momento do acesso à tela, após ter selecionado a apuração que será ajustada o sistema já deve demonstrar no frame de “Informação das Devoluções do Período” as informações relativas às NFs de Devolução existentes nas tabelas SAFX07 e SAFX08, considerando o seguinte critério para seleção das informações:

- Documentos fiscais do estabelecimento selecionado (ou estabelecimentos, pois, no caso de ser um centralizador deverão ser considerados os centralizados) E
- Que tenham Data de Lançamento do PIS/COFINS que compreenda o Período de Apuração E
- Que tenha CST PIS ou CST COFINS igual a “99” E
- Que o CFOP ou CFOP + Natureza da NF (campo 22 ou 22 + 23 da SAFX08) esteja parametrizado na parametrização de Identificador do Tipo de Operação (menu Parâmetros) com Tipo de Operação igual a “1 – Devolução de Venda” E
- Que o Produto (campos 13 e 14 da SAFX08) ou NCM do Produto indicado NF (campo 05 da SAFX2013) tenha sido indicado na Parametrização por Produto ou por NCM (Parâmetros >> Identificador Devolução de Venda - Reg. Cumulativo (Segmento Cigarro)) E
- Que o campo BC de PIS ou COFINS (campos 86 e 88 da SAFX08) sejam maiores que zero E
- Que o campo Alíquota de PIS ou COFINS (campos 129 e 130 da SAFX08) sejam maiores que zero E

Caso não seja encontrada nenhuma NF que atenda este critério de seleção, retornar a mensagem: “Não existem NFs de Devolução para o período de apuração indicado”.

A regra de cada campo será detalhado abaixo:


* Descrição não disponível em tela

Informações Adicionais – Critérios de demonstração das informações no frame “Informações das Devoluções do Período”:

A regra de seleção das informações que serão demonstradas no frame de “Informações das Devoluções do Período” está definida no botão “Buscar NFs de Devolução”, mas a demonstração da informação no frame deve considerar:

A regra de seleção das informações que serão demonstradas no frame de “Informações das Devoluções do Período” está definida no momento do acesso à tela, mas a demonstração da informação no frame deve considerar:

Dados da NF de Devolução:
Irá demonstrar as informações da NF de Devolução encontrada. Nestas colunas vamos demonstrar os dados básicos da NF + a informação do Produto. No filtro nós consideramos apenas NFs que tenham o Produto ou NCM parametrizados na Parametrização por Produto ou por NCM (Parâmetros >> Identificador Devolução de Venda - Reg. Cumulativo (Segmento Cigarro)) e neste contexto devemos mostrar apenas informação dos produtos que se enquadrem na parametrização.

Dados da NF de Saída:
Irá demonstrar as informações da NF Referenciada indicada na SAFX116 que está associada à NF de devolução. Como vamos demonstrar a informação de Dados da NF de Devolução por Produto, aqui vamos demonstrar a informação da NF Referenciada considerando o produto correspondente na NF de Devolução. Podemos ter um cenário onde, para uma NF de Devolução temos mais de uma NF Referenciada, e a referência do produto esteja em mais de uma NF de saída referenciada. Neste caso, devemos considerar apenas uma NF de Saída para demonstrar e o sistema deve eleger uma delas.

Valores PIS e Valores COFINS:
Irá demonstrar os valores lançados no Item Devolvido (SAFX08) para o produto que foi demonstrado na informação de Dados da NF de Devolução.

Esboço da tela:




## Processos de Cálculo


### Geração Automática dos Registros M220/M225 e M620/M625



Os registros M220, M225, M620 e M625 serão gerados automaticamente quando o usuário acionar o botão “Gerar Ajustes” da tela de “Automação Devolução de Venda - Regime Cumulativo (Segmento de Cigarros)”.

O registro M220 e M620 são filhos do M210 e M610, respectivamente. No momento da geração esta filiação deverá ser levada em conta, sendo que vamos ter a geração automática dos referidos registros apenas para os pais M210 e M610 que tenham o “Código da Contribuição Social Apurada no Período” igual a 51 – Contribuição Cumulativa Apurada a Alíquota Básica e igual a 31 – Contribuição Apurada por Substituição Tributária.

Para o M220 e M620 filho do M210 e M610 com “Código da Contribuição Social Apurada no Período” igual a 51 – Contribuição Cumulativa Apurada a Alíquota Básica, geraremos os ajustes com base nas informações das NFs de Devolução selecionadas na tela de “Automação Devolução de Venda - Regime Cumulativo (Segmento de Cigarros)” cuja NF de saída associada tenha CST igual a “01”.

Para o M220 e M620 filho do M210 e M610 com “Código da Contribuição Social Apurada no Período” igual a 31 – Contribuição Apurada por Substituição Tributária, geraremos os ajustes com base nas informações das NFs de Devolução selecionadas na tela de “Automação Devolução de Venda - Regime Cumulativo (Segmento de Cigarros)” e que geraram Ajuste da Contribuição apurada por ST cuja NF de saída associada tenha CST igual a “05”.

[ALTERADA – CH28520_2015]
Para cada NF selecionada será gerada uma linha de Ajuste. Teremos neste contexto os valores de PIS e COFINS sumarizados, uma vez que na tela de “Automação Devolução de Venda - Regime Cumulativo (Segmento de Cigarros)” estes valores estão abertos por “Produto”. O detalhamento por item vai ocorrer nos registros M225 e M625, que são filhos do M220 e M620, mas deverão ser agrupados, quando lançados na tabela de apuração para geração do arquivo magnético, pelos campos chave: DET_VALOR_AJ, CST_PIS, DET_ALIQ, DT_OPER_AJ e COD_CTA; e seus valores devem ser consolidados, ou seja, DET_VALOR_AJ e DET_BC_CRED.

As telas que serão alimentadas e onde será possível visualizar os ajustes gerados, estão disponíveis em:

Módulo: SPED >> EFD – Escrituração Fiscal Digital

Menu: Obrigações >> Manutenção >> Apuração PIS/PASEP >> Contribuição para o PIS/PASEP no Período – M200 >> Aba Detalhamento da Contribuição – M210 >> Aba Ajustes da Contribuição para o PIS/PASEP Apurada – M220

Menu: Obrigações >> Manutenção >> Apuração COFINS >> Contribuição para a COFINS no Período – M600 >> Aba Detalhamento da Contribuição – M610 >> Aba Ajustes da Contribuição para a COFINS Apurada – M620

As regras para geração de cada campo dos registros M220 e M620 são:


Para geração do M225 e M625 na tela de “Automação Devolução de Venda - Regime Cumulativo (Segmento de Cigarros)”, teremos um detalhamento para cada item (produto) selecionado. A informação da NF (capa) estará no M220 e M620 e o detalhe dos valores por item (produto), estará neste registro.

As telas que serão alimentadas e onde será possível visualizar o detalhamento dos ajustes gerados, estão disponíveis em:

Módulo: SPED >> EFD – Escrituração Fiscal Digital

Menu: Obrigações >> Manutenção >> Apuração PIS/PASEP >> Contribuição para o PIS/PASEP no Período – M200 >> Aba Detalhamento da Contribuição – M210 >> Aba Ajustes da Contribuição para o PIS/PASEP Apurada – M220 >> Aba Detalhamento dos Ajustes da Contribuição do PIS/PASEP Apurada – M225

Menu: Obrigações >> Manutenção >> Apuração COFINS >> Contribuição para a COFINS no Período – M600 >> Aba Detalhamento da Contribuição – M610 >> Aba Ajustes da Contribuição para a COFINS Apurada – M620 >> Aba Detalhamento dos Ajustes da Contribuição para a COFINS Apurada – M625

As regras para geração de cada campo dos registros M225 e M625 são:


Favor verificar o documento RNG - M211_M220_M225_M230_M300_M350_M611_M620_M625_M630_M700.doc, localizado no diretório ...\MsafDW\documentacao funcional\EFD-PISCOFINS\Requisito\Registros\Apuração, as regras RNG-M225 e RNG-M625, pois a forma de demonstração das informações na automação será por produto para conferência do usuário, mas na geração do arquivo magnético será necessário o agrupamento por ser uma regra determinada na validação do PVA.


| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-1980 | Marcos G. de Paula | Definição das regras da tela de Parametrização por Produto para geração das informações do regime cumulativo. |
| CH28520_2015 | Julyana Perrucini | Este documento tem como objetivo definir a regra de agrupamento dos Registros M225 e M625. |


| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | Usuário do Sistema. |
| Pré- Condições | Estar logado no produto MasterSAF DW. |
| Pós-Condições | Não se aplica. |


| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  |  |


| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  | Fim do fluxo Alternativo |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Editbox | S | N | Formato: <COD_ESTAB> - <Razão Social> | Será demonstrado o Código + Razão Social do Estabelecimento da apuração selecionada no momento do acesso à tela. | MFS-1980 |
| Situação | Editbox | S | N |  | Será demonstrada a Situação da apuração selecionada no momento do acesso à tela. | MFS-1980 |
| Data Inicial | Editbox | S | N | Formato: DD/MM/AAAA | Será demonstrada a Data Inicial da apuração selecionada no momento do acesso à tela. | MFS-1980 |
| Data Final | Editbox | S | N | Formato: DD/MM/AAAA | Será demonstrada a Data Final da apuração selecionada no momento do acesso à tela. | MFS-1980 |
| Data da Realização da Apuração | Editbox | S | N | Formato: DD/MM/AAAA | Será demonstrada a Data da Realização da apuração selecionada no momento do acesso à tela. | MFS-1980 |
| Buscar NFs de Devolução   (este botão foi removido conforme alinhamento com a fábrica e a busca será realizada no momento da abertura da tela) | Botão | N | S |  | Quando acionado este botão, o sistema deverá realizar uma pesquisa na SAFX07 e SAFX08 considerando:  Documentos fiscais do estabelecimento selecionado (ou estabelecimentos, pois, no caso de ser um centralizador deverão ser considerados os centralizados) E Que tenham Data de Lançamento do PIS/COFINS que compreenda o Período de Apuração E Que tenha CST PIS ou CST COFINS iguais a “98” ou “99” E Que o CFOP ou CFOP + Natureza da NF (campo 22 ou 22 + 23 da SAFX08) esteja parametrizado na parametrização de Identificador do Tipo de Operação (menu Parâmetros) com Tipo de Operação igual a “1 – Devolução de Venda” E Que o Produto (campos 13 e 14 da SAFX08) ou NCM do Produto indicado NF (campo 05 da SAFX2013) tenha sido indicado na Parametrização por Produto ou por NCM (Parâmetros >> Identificador Devolução de Venda - Reg. Cumulativo (Segmento Cigarro)) E Que o campo BC de PIS ou COFINS (campos 86 e 88 da SAFX08) sejam maiores que zero E Que tenha NF Referenciada (SAFX116) e que está NF esteja com o campo Movimento de Entrada / Saída (campo 16 da SAFX116) preenchido com conteúdo igual a “9” E Que o CST da NF Referenciada encontrada na SAFX116 seja igual a “01” ou “05”*.  O resultado dessa pesquisa será demonstrado no frame de “Informação das Devoluções do Período”. Caso não seja encontrada nenhuma NF que atenda este critério de seleção, retornar a mensagem: “Não existem NFs de Devolução para o período de apuração indicado”.  * Para encontrar a NF original da NF Referenciada, considerar: | MFS-1980 |
| Informação das Devoluções do Período | Informação das Devoluções do Período | Informação das Devoluções do Período | Informação das Devoluções do Período | Informação das Devoluções do Período | Informação das Devoluções do Período | MFS-1980 |
| Dados da NF de Devolução | Dados da NF de Devolução | Dados da NF de Devolução | Dados da NF de Devolução | Dados da NF de Devolução | Dados da NF de Devolução | MFS-1980 |
| * Checkbox de seleção da NF | Checkbox | N | S | Default: não selecionado |  | MFS-1980 |
| Estab. | Editbox | S | N |  | Irá demonstrar o código do estabelecimento (campo COD_ESTAB da SAFX07) da NF de devolução encontrada. | MFS-1980 |
| Nº da NF / Série / Subsérie | Editbox | S | N |  | Irá demonstrar o Nº da NF / Série / Subsérie (campos NUM_DOCFIS, SERIE_DOCFIS e SUB_SERIE_DOCFIS da SAFX07) da NF de devolução encontrada. | MFS-1980 |
| Dt. Fiscal | Editbox | S | N | Formato: DD/MM/AAAA | Irá demonstrar a Data Fiscal da NF de devolução encontrada. | MFS-1980 |
| Participante | Editbox | S | N |  | Irá demonstrar o Indicador + o Código da PFJ (campo IDENT_FIS_JUR e COD_FIS_JUR da SAFX07) da NF de devolução encontrada. Se o parâmetro “Considerar o Indicador no Código do Participante” da tela de Dados Iniciais do estabelecimento centralizador não estiver selecionado, demonstrar apenas o Código da PFJ. | MFS-1980 |
| Produto | Editbox | S | N |  | Irá demonstrar o Indicador + o Código do Produto (campo IND_PRODUTO e COD_PRODUTO da SAFX08) da NF de Devolução encontrada. Se o parâmetro “Considerar o Indicador no Código do Item” da tela de Dados Iniciais do estabelecimento centralizador não estiver selecionado, demonstrar apenas o Código do Produto. | MFS-1980 |
| Dados da NF de Saída | Dados da NF de Saída | Dados da NF de Saída | Dados da NF de Saída | Dados da NF de Saída | Dados da NF de Saída | MFS-1980 |
| Nº da NF / Série / Subsérie  (campo removido por solicitação do cliente Souza Cruz) | Editbox | S | N |  | Irá demonstrar o Nº da NF / Série / Subsérie (campos NUM_DOCFIS_REF, SERIE_DOCFIS_REF e SUB_SERIE_DOCFIS_REF da SAFX116) da NF saída associada à NF de devolução encontrada. | MFS-1980 |
| Dt. Fiscal  (campo removido por solicitação do cliente Souza Cruz) | Editbox | S | N | Formato: DD/MM/AAAA | Irá demonstrar a Data Fiscal (campo DATA_FISCAL_REF da SAFX116) da NF saída associada à NF de devolução encontrada. | MFS-1980 |
| CST  (campo removido por solicitação do cliente Souza Cruz) | Editbox | S | N |  | Para gerar esta informação o sistema deverá localizar na SAFX08 o Item da NF de saída que corresponde ao produto devolvido e que está sendo demonstrado na coluna “Produto” dos Dados da NF de Devolução. Para localizar a NF de saída original, o sistema deve considerar:   Localizando a NF, considerar o item que tenha o mesmo código de produto da NF de devolução.  O sistema deverá demonstrar neste campo o conteúdo do campo CST PIS (campo COD_SITUACAO_PIS da SAFX08) do Item encontrado. | MFS-1980 |
| Valores PIS | Valores PIS | Valores PIS | Valores PIS | Valores PIS | Valores PIS | MFS-1980 |
| CST | Editbox | S | N |  | Irá demonstrar o CST do PIS (campo COD_SITUACAO_PIS da SAFX08) da NF de devolução encontrada. | MFS-1980 |
| Base | Editbox | S | N |  | Irá demonstrar a Base de Cálculo do PIS (campo VLR_BASE_PIS da SAFX08) da NF de devolução encontrada. | MFS-1980 |
| Aliq. | Editbox | S | N |  | Irá demonstrar a Alíquota do PIS (campo VLR_ALIQ_PIS da SAFX08) da NF de devolução encontrada. | MFS-1980 |
| Valor | Editbox | S | N |  | Irá demonstrar o Valor do PIS (campo VLR_PIS da SAFX08) da NF de devolução encontrada. | MFS-1980 |
| Valores COFINS | Valores COFINS | Valores COFINS | Valores COFINS | Valores COFINS | Valores COFINS | MFS-1980 |
| CST | Editbox | S | N |  | Irá demonstrar o CST da COFINS (campo COD_SITUACAO_COFINS da SAFX08) da NF de devolução encontrada. | MFS-1980 |
| Base | Editbox | S | N |  | Irá demonstrar a Base de Cálculo da COFINS (campo VLR_BASE_COFINS da SAFX08) da NF de devolução encontrada. | MFS-1980 |
| Aliq. | Editbox | S | N |  | Irá demonstrar a Alíquota da COFINS (campo VLR_ALIQ_COFINS da SAFX08) da NF de devolução encontrada. | MFS-1980 |
| Valor | Editbox | S | N |  | Irá demonstrar o Valor da COFINS (campo VLR_COFINS da SAFX08) da NF de devolução encontrada. | MFS-1980 |
| Selecionar Todos | Botão | N | N |  | Quando acionado, irá selecionar todas as NFs que estão com status não selecionado no frame de “Informação das Devoluções do Período”. | MFS-1980 |
| Desmarcar Todos | Botão | N | N |  | Quando acionado, irá desmarcar todas as NFs que estão com status selecionado no frame de “Informação das Devoluções do Período”. | MFS-1980 |
| Calcular Prévia de Ajustes | Botão | N | N |  | Quando acionado este botão, haverá atualização do cálculo dos valores de PIS e COFINS dos frames de Ajustes da Contribuição Apurada por Substituição Tributária e Ajustes da Contribuição Cumulativa Apuração a Alíquota Básica. | MFS-1980 |
| Gerar Ajustes | Botão | N | N |  | Quando acionado este botão, o sistema deve verificar:  Se os valores de PIS e COFINS apurados para o frame de Ajustes da Contribuição Apurada por Substituição Tributária são maiores que os valores de PIS e COFINS apurados para o frame de Contribuição Apurada por Substituição Tributária E  Se os valores de PIS e COFINS apurados para o frame de Ajustes da Contribuição Cumulativa Apuração a Alíquota Básica são maiores que os valores de PIS e COFINS apurados para o frame de Contribuição Cumulativa Apuração a Alíquota Básica.  Se for maior, retornar a mensagem: “Valor de ajuste calculado excede o valor da contribuição. Ajuste a relação de NFs selecionadas”.  Se o valor for menor ou igual, o sistema deverá gerar os registros M220/M225 e M620/M625 com base nas NFs selecionadas, considerando as regras definidas no item “3.1. Geração Automática dos Registros M220/M225 e M620/M625” deste documento. | MFS-1980 |
| Contribuição Apurada por Substituição Tributária | Contribuição Apurada por Substituição Tributária | Contribuição Apurada por Substituição Tributária | Contribuição Apurada por Substituição Tributária | Contribuição Apurada por Substituição Tributária | Contribuição Apurada por Substituição Tributária | MFS-1980 |
| Valor PIS | Editbox | S | N | Default: 0,00 | Neste campo deve ser demonstrado o valor apurado para a linha “Valor Total da Contribuição Social Apurada” do registro M210 do período que tenha o “Código da Contribuição Social Apurada no Período” igual a 31 – Contribuição Apurada por Substituição Tributária. | MFS-1980 |
| Valor COFINS | Editbox | S | N | Default: 0,00 | Neste campo deve ser demonstrado o valor apurado para a linha “Valor Total da Contribuição Social Apurada” do registro M610 do período que tenha o “Código da Contribuição Social Apurada no Período” igual a 31 – Contribuição Apurada por Substituição Tributária. | MFS-1980 |
| Ajustes da Contribuição Apurada por Substituição Tributária | Ajustes da Contribuição Apurada por Substituição Tributária | Ajustes da Contribuição Apurada por Substituição Tributária | Ajustes da Contribuição Apurada por Substituição Tributária | Ajustes da Contribuição Apurada por Substituição Tributária | Ajustes da Contribuição Apurada por Substituição Tributária | MFS-1980 |
| Valor PIS | Editbox | S | N | Default: 0,00 | Este campo será atualizado sempre que o usuário clicar no botão “Calcular Prévia de Ajustes”. Ele será resultado da Somatória do campo Valor do PIS das NFs selecionadas pelo usuário. e cuja NF de Saída associada tenha CST igual a “05”. | MFS-1980 |
| Valor COFINS | Editbox | S | N | Default: 0,00 | Este campo será atualizado sempre que o usuário clicar no botão “Calcular Prévia de Ajustes”. Ele será resultado da Somatória do campo Valor da COFINS das NFs selecionadas pelo usuário. e cuja NF de Saída associada tenha CST igual a “05”. | MFS-1980 |
| Contribuição Cumulativa Apuração a Alíquota Básica (campo removido por solicitação do cliente Souza Cruz) | Contribuição Cumulativa Apuração a Alíquota Básica (campo removido por solicitação do cliente Souza Cruz) | Contribuição Cumulativa Apuração a Alíquota Básica (campo removido por solicitação do cliente Souza Cruz) | Contribuição Cumulativa Apuração a Alíquota Básica (campo removido por solicitação do cliente Souza Cruz) | Contribuição Cumulativa Apuração a Alíquota Básica (campo removido por solicitação do cliente Souza Cruz) | Contribuição Cumulativa Apuração a Alíquota Básica (campo removido por solicitação do cliente Souza Cruz) | MFS-1980 |
| Valor PIS | Editbox | S | N | Default: 0,00 | Neste campo deve ser demonstrado o valor apurado para a linha “Valor Total da Contribuição Social Apurada” do registro M210 do período que tenha o “Código da Contribuição Social Apurada no Período” igual a 51 – Contribuição Cumulativa Apurada a Alíquota Básica. | MFS-1980 |
| Valor COFINS | Editbox | S | N | Default: 0,00 | Neste campo deve ser demonstrado o valor apurado para a linha “Valor Total da Contribuição Social Apurada” do registro M610 do período que tenha o “Código da Contribuição Social Apurada no Período” igual a 51 – Contribuição Cumulativa Apurada a Alíquota Básica. | MFS-1980 |
| Ajustes da Contribuição Cumulativa Apuração a Alíquota Básica (campo removido por solicitação do cliente Souza Cruz) | Ajustes da Contribuição Cumulativa Apuração a Alíquota Básica (campo removido por solicitação do cliente Souza Cruz) | Ajustes da Contribuição Cumulativa Apuração a Alíquota Básica (campo removido por solicitação do cliente Souza Cruz) | Ajustes da Contribuição Cumulativa Apuração a Alíquota Básica (campo removido por solicitação do cliente Souza Cruz) | Ajustes da Contribuição Cumulativa Apuração a Alíquota Básica (campo removido por solicitação do cliente Souza Cruz) | Ajustes da Contribuição Cumulativa Apuração a Alíquota Básica (campo removido por solicitação do cliente Souza Cruz) | MFS-1980 |
| Valor PIS | Editbox | S | N | Default: 0,00 | Este campo será atualizado sempre que o usuário clicar no botão “Calcular Prévia de Ajustes”. Ele será resultado da Somatória do campo Valor do PIS das NFs selecionadas pelo usuário e cuja NF de Saída associada tenha CST igual a “01”. | MFS-1980 |
| Valor COFINS | Editbox | S | N | Default: 0,00 | Este campo será atualizado sempre que o usuário clicar no botão “Calcular Prévia de Ajustes”. Ele será resultado da Somatória do campo Valor da COFINS das NFs selecionadas pelo usuário e cuja NF de Saída associada tenha CST igual a “01”. | MFS-1980 |


| Descrição do Campo | Registro M220 | Registro M620 |
| --- | --- | --- |
| Tipo de Ajuste | Será gerado um conteúdo fixo: “0 – Ajuste de Redução” | Será gerado um conteúdo fixo: “0 – Ajuste de Redução” |
| Valor do Ajuste | Para o M220 filho do M210 com “Código da Contribuição Social Apurada no Período” igual a 51 – Contribuição Cumulativa Apurada, realizar a soma, por NF de devolução selecionada, do Valor do PIS dos registros cuja NF de Saída tenha CST igual a “01”.  Para o M220 filho do M210 com “Código da Contribuição Social Apurada no Período” igual a 31 – Contribuição Apurada por Substituição Tributária, realizar a soma, por NF de devolução selecionada, do Valor do PIS dos registros considerados para composição do Ajuste da Contribuição apurada por ST cuja NF de Saída tenha CST igual a “05”. | Para o M620 filho do M610 com “Código da Contribuição Social Apurada no Período” igual a 51 – Contribuição Cumulativa Apurada, realizar a soma, por NF de devolução selecionada, do Valor da COFINS dos registros cuja NF de Saída tenha CST igual a “01”.  Para o M620 filho do M610 com “Código da Contribuição Social Apurada no Período” igual a 31 – Contribuição Apurada por Substituição Tributária, realizar a soma, por NF de devolução selecionada, do Valor da COFINS dos registros considerados para composição do Ajuste da Contribuição apurada por ST cuja NF de Saída tenha CST igual a “05”. |
| Código do Ajuste | Será gerado um conteúdo fixo: “05 – Ajuste Oriundo de Outras Situações”. | Será gerado um conteúdo fixo: “05 – Ajuste Oriundo de Outras Situações”. |
| Número do processo, documento ou ato concessório | Será gerada a seguinte informação: Cód. Participante: <<Código de Participante da NF de Devolução, conforme informado na tela de automação>> / N. NF: <<Número da NF de Devolução, conforme informado na tela de automação>> / Série: <<Série da NF de Devolução, conforme informado na tela de automação>>.  Exemplo: Cód. Participante: 1-86663725000197 / N. NF: 006365 / Série: 1 | Será gerada a seguinte informação: Cód. Participante: <<Código de Participante da NF de Devolução, conforme informado na tela de automação>> / N. NF: <<Número da NF de Devolução, conforme informado na tela de automação>> / Série: <<Série da NF de Devolução, conforme informado na tela de automação>>.  Exemplo: Cód. Participante: 1-86663725000197 / N. NF: 006365 / Série: 1 |
| Descrição Resumida | Será gerado um conteúdo fixo: “ÑF de Devolução de Venda do Regime Cumulativo”. | Será gerado um conteúdo fixo: “ÑF de Devolução de Venda do Regime Cumulativo”. |
| Data Referência | Será gerado com a Data Fiscal da NF de Devolução. | Será gerado com a Data Fiscal da NF de Devolução. |


| Descrição do Campo | Registro M225 | Registro M625 |
| --- | --- | --- |
| Detalhamento do Valor | Será gerado com o Valor do PIS do item da NF de Devolução selecionada e que foi sumarizada no M220. | Será gerado com o Valor da COFINS do item da NF de Devolução selecionada e que foi sumarizada no M620. |
| CST | Será gerado com o CST do PIS do item da NF de Devolução selecionada e que foi sumarizada no M220. | Será gerado com o CST da COFINS do item da NF de Devolução selecionada e que foi sumarizada no M620. |
| Detalhamento da BC | Será gerado com o valor da BC do PIS do item da NF de Devolução selecionada e que foi sumarizada no M220. | Será gerado com o valor da BC da COFINS do item da NF de Devolução selecionada e que foi sumarizada no M620. |
| Detalhamento da Alíquota | Será gerado com a Alíquota do PIS do item da NF de Devolução selecionada e que foi sumarizada no M220. | Será gerado com a Alíquota da COFINS do item da NF de Devolução selecionada e que foi sumarizada no M620. |
| Data da Operação | Será gerado com a Data Fiscal da NF de Devolução. | Será gerado com a Data Fiscal da NF de Devolução. |
| Descrição da Operação | Será gerado um conteúdo fixo: “ÑF de Devolução de Venda do Regime Cumulativo”. | Será gerado um conteúdo fixo: “ÑF de Devolução de Venda do Regime Cumulativo”. |
| Conta Contábil | Não será gerado conteúdo. | Não será gerado conteúdo. |
| Informação Complementar | Não será gerado conteúdo. | Não será gerado conteúdo. |

# MTZ-OTF-Listagem_Conferência de Códigos IRRF 

- **Fonte:** MTZ-OTF-Listagem_Conferência de Códigos IRRF .docx
- **Modificado:** 2022-05-02
- **Tamanho:** 44 KB

---

# 		Obrigações de Tributos Federais – Relatórios de Conferência de Códigos IRRF	

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3370 

Relatório de Conferência de Códigos IRRF

Corrigir na rotina de geração dos Relatórios de Conferência de Códigos IRRF \(Por Data, Por Beneficiário e Por Número de Controle\) o cálculo dos Campos ‘Total do dia’, Total do beneficiário, Total Geral \(respectivamente\)\.

 Adequação dos relatórios para ficar coerente com a DIRF \(retirando a condição de gerar apenas informações dos códigos de retenção de IRRF\), alteração do título das telas dos critérios de seleção, dos cabeçalhos e do Menu desses relatórios\.

Inclusão dos Campos Grupo de Retenção e Códigos de Retenção na tela dos critérios de Seleção dos relatórios\.

Alteração das ordens das colunas mostradas nos três relatórios\.

Alteração do nome da coluna Valor IR Retido \(dos três relatórios\), para Valor Retido\.

## 		REGRAS DE NEGÓCIO	

	

#### Cód\.

### Descrição

### DR

__RN00__

Alterar na rotina do Relatório Conferência de Códigos IRRF / Por Data, \(no módulo: Federal / Obrigações de Tributos Federais, Menu: DIRF / Listagens\) o critério de seleção dos registros para compor o valor do campo ‘Total do dia’ \.

Quando existir mais de um código de retenção para uma determinada nota, o campo ‘Valor Bruto’, não deve ser somado mais de uma vez, no Total do dia\. \(se os campos Nº/Série/Subserie, Data do Movimento e Beneficiário forem iguais, considere apenas 1 vez o valor Bruto\)\. Os campos __Valor Dedução__ e __Valor IR Retido__ devem continuar sendo somados, independente da quantidade de códigos de retenção informado por nota\. Além disso, a partir do segundo código \(da mesma nota\), o relatório deverá mostrar apenas os campos Nº do Controle, Operação, Código Retenção, Valor Dedução, Alíquota e Valor Retido e os demais campos devem ficar em branco\.

Exemplo: 

Nota fiscal 125478 com dois códigos de retenção:

Hoje a rotina está sumarizando erroneamente no campo Valor Bruto de todas as linhas que está sendo apresentada por data, sem considerar o número do documento\.

OS3370

__RN01__

Alterar a rotina de geração do Relatório por Data, ordenando os registros por Data do Movimento, Nº/Série/Subserie e depois por Código de Retenção\.

OS3370

__RN02__

Incluir nos critérios de geração do relatório \(Por Data\), os campos Grupo de Retenção  e Códigos de retenção\.

Exibir os Códigos de Retenção  \(COD\_DARF da tabela X2019\_COD\_DARF\), em ordem crescente\.

OS3370

__RN03__

Retirar da rotina do Relatório Por Data, a condição X53\_RETENCAO\_IRRF"\."COD\_TRIBUTO" = '02', pois o relatório é para a conferência da DIRF e não apenas do tributo IRRF

OS3370

__RN04__

Na tela da geração \(critérios de seleção\), do relatório Por Data, alterar o Título:  ‘Relatório de Conferência de Códigos de IRRF por Data’ para ‘Relatório de Conferência de Códigos de Retenção por Data’

OS3370

__RN05__

Alterar a ordem das colunas que serão apresentadas no relatório ‘Por Data’\.

A ordem será:

__Data  Movimento__

__Doc\.__

__Nº/Série/Subsérie__

__Mês/Ano__

__Nº Controle__

__Operação__

__Código Retenção__

__Valor Bruto__

__Valor Dedução__

__Alíquota__

__Valor IR Retido__

__Beneficiário__

OS3370

__RN06__

No cabeçalho do relatório Por Data, alterar o Texto:  ‘Conferência de Códigos de IRRF por Data’ para ‘Conferência de Códigos de Retenção por Data’

OS3370

__RN07__

Alterar na rotina do Relatório Conferência de Códigos IRRF / Por Beneficiário, \(no módulo: Federal / Obrigações de Tributos Federais, Menu: DIRF / Listagens\) o critério de seleção dos registros para compor o valor do campo ‘Total do beneficiário’ \.

Quando existir mais de um código de retenção para uma determinada nota, o campo ‘Valor Bruto’, não deve ser somado mais de uma vez, no Total do beneficiário\. \(se os campos Nº/Série/Subserie, Data do Movimento e Beneficiário forem iguais, considere apenas 1 vez o valor Bruto\)\. Os campos __Valor Dedução__ e __Valor IR Retido__ devem continuar sendo somados, independente da quantidade de códigos de retenção informado por nota\. Além disso, a partir do segundo código \(da mesma nota\), o relatório deverá mostrar apenas os campos Nº do Controle, Operação, Código Retenção, Valor Dedução, Alíquota e Valor Retido e os demais campos devem ficar em branco\.

Exemplo: 

Nota fiscal 125478 com dois códigos de retenção:

Hoje a rotina está sumarizando erroneamente no campo Valor Bruto todas as linhas que está sendo apresentada por beneficiário, sem considerar o número do documento\.

OS3370

__RN08__

Alterar a rotina de geração do relatório Por Beneficiário ordenando os registros por Beneficiário, Data do Movimento, Nº/Série/Subserie e depois por Código de Retenção\.

OS3370

__RN09__

Incluir nos critérios de geração do relatório \(Por Beneficiário\), os campos Grupo de Retenção  e Códigos de retenção\.

Exibir os Códigos de Retenção  \(COD\_DARF da tabela X2019\_COD\_DARF\), em ordem crescente\.

OS3370

__RN10__

Retirar da rotina do Relatório Por Beneficiário, a condição X53\_RETENCAO\_IRRF"\."COD\_TRIBUTO" = '02', pois o relatório é para a conferência da DIRF e não apenas do tributo IRRF

OS3370

__RN11__

Na tela da geração \(critérios de seleção\), do relatório Por Beneficiário, alterar o Título:  ‘Relatório de Conferência de Códigos de IRRF por Beneficiário’ para ‘Relatório de Conferência de Códigos de Retenção por Beneficiário’

OS3370

__RN12__

Alterar a ordem das colunas que serão apresentadas no relatório ‘Por Beneficiário’\.

A ordem será:

__Beneficiário__

__Data  Movimento__

__Doc\.__

__Nº/Série/Subsérie__

__Mês/Ano__

__Nº Controle__

__Operação__

__Código Retenção__

__Valor Bruto__

__Valor Dedução__

__Alíquota__

__Valor IR Retido__

OS3370

__RN13__

No cabeçalho do relatório Por Beneficiário, alterar o Texto: ‘Conferência de Códigos de IRRF por Beneficiário’ para ‘Conferência de Códigos de Retenção por Beneficiário’

OS3370

__RN14__

Alterar na rotina do Relatório Conferência de Códigos IRRF / Por Controle, \(no módulo: Federal / Obrigações de Tributos Federais, Menu: DIRF / Listagens\) o critério de seleção dos registros para compor o valor do campo ‘Total Geral’ \.

Quando existir mais de um código de retenção para uma determinada nota, o campo ‘Valor Bruto’, não deve ser somado mais de uma vez, no Total Geral\. \(se os campos Nº/Série/Subserie, Data do Movimento e Beneficiário forem iguais, considere apenas 1 vez o valor Bruto\)\. Os campos __Valor Dedução__ e __Valor IR Retido__ devem continuar sendo somados, independente da quantidade de códigos de retenção informado por nota\. Além disso, a partir do segundo código \(da mesma nota\), o relatório deverá mostrar apenas os campos Nº do Controle, Operação, Código Retenção, Valor Dedução, Alíquota e Valor Retido e os demais campos devem ficar em branco\.

Exemplo: 

Nota fiscal 125478 com dois códigos de retenção:

Hoje a rotina está sumarizando erroneamente no campo Valor Bruto todas as linhas que está sendo apresentada por controle, sem considerar o número do documento\.

OS3370

__RN15__

Alterar a rotina de geração do relatório Por Número de Controle, ordenando os registros por Nº Controle, Data Movimento e Código de Retenção

OS3370

__RN16__

Incluir nos critérios de geração do relatório \(Por Controle\), os campos Grupo de Retenção  e Códigos de retenção\.

Exibir os Códigos de Retenção  \(COD\_DARF da tabela X2019\_COD\_DARF\), em ordem crescente\.

OS3370

__RN17__

Retirar da rotina do Relatório Por Controle, a condição X53\_RETENCAO\_IRRF"\."COD\_TRIBUTO" = '02', pois o relatório é para a conferência da DIRF e não apenas do tributo IRRF

OS3370

__RN18__

Na tela da geração \(critérios de seleção\), do relatório Por Número de Controle, alterar o Texto:  ‘Relatório de Conferência de Códigos de IRRF por Número de Controle’ para ‘Relatório de Conferência de Códigos de Retenção por Número de Controle’

OS3370

__RN19__

Alterar a ordem das colunas que serão apresentadas no relatório ‘Por Número de Controle’,  para manter o padrão dos demais relatórios\.

A ordem será:

__Nº Controle __

__Data  Movimento__

__Doc\.__

__Nº/Série/Subsérie__

__Beneficiário__

__Mês/Ano__

__Operação__

__Código Retenção__

__Valor Bruto__

__Valor Dedução__

__Alíquota__

__Valor IR Retido__

OS3370

__RN20__

No cabeçalho do relatório Por Número de Controle, alterar o Texto: ‘Conferência de Códigos de IRRF por Número de Controle’ para ‘Conferência de Códigos de Retenção por Número de Controle’\.

OS3370

__RN21__

Alterar o menu ‘Conferência de Códigos IRRF’ para ‘Conferência de Códigos de Retenção’ \(no módulo: Federal / Obrigações de Tributos Federais, Menu: DIRF / Listagens\)\.

OS3370

	


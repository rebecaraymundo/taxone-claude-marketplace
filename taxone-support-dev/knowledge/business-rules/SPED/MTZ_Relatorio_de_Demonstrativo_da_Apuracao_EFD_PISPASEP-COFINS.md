# MTZ_Relatorio_de_Demonstrativo_da_Apuracao_EFD_PISPASEP-COFINS

> Fonte: MTZ_Relatorio_de_Demonstrativo_da_Apuracao_EFD_PISPASEP-COFINS.doc

THOMSON REUTERS

Relatório de Demonstrativo da Apuração EFD PIS/PASEP-COFINS


Localização:
Módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições
Menus: Obrigações >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Tipo de Crédito
           Obrigações >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Tipo de Contribuição
           Obrigações >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Tipo de Natureza da Receita
           Obrigações SCP>> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração Tipo de Natureza da Receit >> Tipo de Crédito
           Obrigações SCP>> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração Tipo de Natureza da Receit >> Tipo de Contribuição
           Obrigações SCP>> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração Tipo de Natureza da Receit >> Tipo de Natureza da Receita
           Relatórios ( Demonstrativo da Apuração (Crédito / Contribuição / Natureza da Receita)    


DOCUMENTO DE REQUISITO

OS/CH	Nome	Descrição		OS3169-GE13D	Relatório de Demonstrativo da Apuração EFD PIS/PASEP-COFINS	Desenvolvimentos dos Relatórios de Demonstrativo da Apuração por Tipo de Crédito e por Tipo de Contribuição EFD PIS/PASEP-COFINS		OS3583	Relatório de Demonstrativo da Apuração EFD Contribuições	Desenvolvimento do Relatório de Demonstrativo da Apuração por Tipo Natureza da Receita		OS3631	Relatório de Demonstrativo da Apuração EFD Contribuições – Por tipo de Contribuição	Adequação do relatório com relação as quebras.		OS3821	Relatório de Demonstrativo da Apuração EFD Contribuições – Por tipo de Contribuição	Inclusão dos campos Código da Unidade Imobiliária e Adquirente no relatório Analítico - Demonstrativo da Apuração por Tipo de Contribuição. Esses campos serão incluídos no detalhamento dos registros (parte Registros Vinculados ao Tipo de Contribuição).		OS4110	Incluir o código NCM 	Incluir o código NCM no demonstrativo de apuração por tipo de natureza da receita 		MFS20227	Julyana Perrucini	Inclusão dos campos “Vlr Tot. Ajustes Acréscimo BC”, “Vlr Tot. Ajustes Redução BC” e “Vlr BC da Contribuição” nos registros M210, e M610.  
Os registros filhos dos M210, e M610 hoje não são apresentados no relatório. Logo os novos registros filhos M215 e M615 não serão demonstrados no relatório.		MFS37761	Relatórios Demonstrativo da Apuração (Crédito / Contribuição / Natureza da Receita)	Inclusao da opção de menu “Relatórios ( Demonstrativo da Apuração (Crédito / Contribuição / Natureza da Receita)” para disponibilizar a geração dos relatórios analíticos em arquivo formato Excel.		


Sumário
 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc46856179" 1 - Relatório de Demonstrativo de Apuração por Tipo de Crédito	 PAGEREF _Toc46856179 \h 1
 HYPERLINK \l "_Toc46856180" 2 - Relatório de Demonstrativo de Apuração por Tipo de Contribuição	 PAGEREF _Toc46856180 \h 1
 HYPERLINK \l "_Toc46856181" 3 - Relatório de Demonstrativo da Apuração por Tipo de Natureza da Receita	 PAGEREF _Toc46856181 \h 1


1 - Relatório de Demonstrativo de Apuração por Tipo de Crédito


REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN00	Relatório de Demonstrativo da Apuração por Tipo de Crédito 

Pré-requisito:
É necessário realizar a Geração dos Registros disponíveis nas opções de menu Obrigações >> Geração dos Registros e Obrigações SCP >> Geração dos Registros, com o parâmetro “Demonstrativo da Apuração por Tipo de Crédito” selecionado.
 
Processamento 
Origem dos dados:
Informações dos registros M100, M105, M500 e M500 ( tabela interna que armazena os dados da apuração do Crédito do Período (registros M100, M105 e M500 e M505) calculados conforme regras descritas no documento “RNG - M100_105_110_500_505_510_V11.doc” a partir da geração dos registros. 

Informações dos Registros vinculados ao tipo de crédito ( tabela interna que armazena os dados das gerações dos registros do Bloco A, C, D e F.  

Critérios de recuperação dos dados para geração do relatório: Se no parâmetro ‘’Gerar Relatório Demonstrativo da Apuração no Período Informado’’ a opção ‘’Tipo de Crédito’’ estiver marcado na tela de Geração dos Registros 

Critérios dos filtros na tela de Emissão do Relatório da Apuração por Tipo de Crédito:
O relatório Demonstrativo da Apuração no Período por Tipo de Crédito deverá ser emitido de acordo com os filtros selecionados na Tela, localizada no módulo: SPED ( EFD-PIS/PASEP-COFINS, menu: Obrigações ( Demonstrativos ( Emissão do Relatório Demonstrativo da Apuração ( por Tipo de Crédito 

Ordenação: 
Linhas dos Registros M100/M500 ( Deverá seguir a mesma ordenação gerada no meio magnético
Linhas dos Registros vinculado ao tipo de crédito ( Registro + Nº Documento, Linha do Registro CFOP e Nat. Base Crédito
Linhas dos Registros M105/M505( Deverá seguir a mesma ordenação gerada no meio magnético. 	OS3169-GE13D		RN01	O relatório Demonstrativo da Apuração por tipo de Crédito - Analítico será gerado com base nas seguintes regras:

Se na tela de Emissão do Relatório por Tipo de Crédito somente a opção ‘’M100’’ do campo Tipo de Registro estiver marcado:
  Listar as informações de cada documento fiscal gerado nos registros A100/A170, C100/C170, C190/C191, C395/C396, C500/C501, D100/D101, D500/D501 e de cada linha gerada no registro F100, F120, F130, F150, F205, F210 e F800 que compôs o tipo de Crédito (campo 02 do registro M100). Considerar todos os registros, mesmo aqueles que estejam associados aos registros M105, conforme segue:

REGISTRO M100
    <REGISTROS VINCULADOS AO REGISTRO M100 + REGISTROS VINCULADOS AOS REGISTROS M105>

Nesta forma de emissão a totalização dos registros (informada na regra RN21) deverá ser feita para cada registro M100 existente, demonstrando a totalização de todos os registros vinculados direta ou indiretamente do registro M100.


Se na tela de Emissão do Relatório por Tipo de Crédito as opções: ‘’M100’’ e ‘’M105’’ do campo Tipo de Registro estiverem marcados:
  Listar os registros M100 e, abaixo deste, listar os registros vinculados diretamente ao M100, ou seja, registros que não possuam associação com registros M105.  Em seguida serão listados os registros M105 pertencentes ao registro M100 e seus registros vinculados, conforme demonstrado a seguir:
REGISTRO M100
    <REGISTROS VINCULADOS AO REGISTRO M100 E QUE NÃO ESTEJAM ASSOCIADOS A NENHUM REGISTRO M105>
  REGISTRO M105
    <REGISTROS VINCULADOS AO REGISTRO M105 >
  REGISTRO M105
    <REGISTROS VINCULADOS AO REGISTRO M105 >


Se na tela de Emissão do Relatório por Tipo de Crédito somente a opção ‘’M500’’ do campo Tipo de Registro estiver marcado:
  Listar as informações de cada documento fiscal gerado nos registros A100/A170, C100/C170, C190/C195, C395/C396, C500/C505, D100/D105, D500/D505 e de cada linha gerada no registro F100, F120, F130, F150, F205, F210 e F800 que compôs o tipo de Crédito (campo 02 do registro M500). Considerar todos os registros, mesmo aqueles que estejam associados aos registros M105, conforme segue:

REGISTRO M500
    <REGISTROS VINCULADOS AO REGISTRO M500 + REGISTROS VINCULADOS AOS REGISTROS M505>

Se na tela de Emissão do Relatório por Tipo de Crédito as opções: ‘’M500’’ e ‘’M505’’ do campo Tipo de Registro estiverem marcados:
 Listar os registros M500 e, abaixo deste, listar os registros vinculados diretamente ao M500, ou seja, registros que não possuam associação com registros M505.  Em seguida serão listados os registros M505 pertencentes ao registro M500 e seus registros vinculados, conforme demonstrado a seguir:

REGISTRO M500
    <REGISTROS VINCULADOS AO REGISTRO M100 E QUE NÃO ESTEJAM ASSOCIADOS A NENHUM REGISTRO M505>
  REGISTRO M505
    <REGISTROS VINCULADOS AO REGISTRO M505 >
  REGISTRO M505
    <REGISTROS VINCULADOS AO REGISTRO M505 >


Importante:
Na tela de Emissão do relatório demonstrativo da apuração por tipo de crédito não será permitido no campo Registro marcar somente a opção M105 e/ou M505.

Não será desenvolvimento o relatório da Apuração por tipo de crédito sintético nesta OS (3169-GE13D)


   	OS3169-GE13D		RN02	Conteúdo das colunas do Relatório - Registro M100

As colunas referentes às informações do registro M100 deverão ser preenchidas com os seguintes valores deste registro:

Tipo de Crédito => Deve recuperar o conteúdo do campo 02-Código Tipo de Crédito.
Base do Crédito => Deve recuperar o valor do campo 04- Valor da Base de Cálculo do Crédito. Se neste campo não houver informação, preencher com o conteúdo do campo 06- Quantidade – Base de cálculo PIS
Alíquota PIS => Deve recuperar o valor do campo 05- Alíquota do PIS/PASEP (em Percentual). Se neste campo não houver informação, deve preencher com o valor do campo 07- Alíquota do PIS (em reais).
Vlr  do Crédito => recuperar o valor do campo 08- Valor total do crédito apurado no período.
Vlr Ajuste Créscimo => recuperar o valor do campo 09- Valor total dos ajustes de acréscimo.
Vlr Ajuste Redução => recuperar o valor do campo 10-Valor total dos ajustes de redução.
Vlr Crédito Diferido => recuperar o valor do campo 11- Valor total do crédito diferido no período.
Vlr Crédito Disponível =>recuperar o valor do campo 12- Valor Total do Crédito Disponível relativo ao Período.
Vlr Crédito Descontado => recuperar o valor do campo 14 - Valor do Crédito disponível, a descontar, da contribuição apurada no próprio período.  
Saldo do Crédito => recuperar o valor do campo 15- Saldo de créditos a utilizar em períodos futuros. 
	OS3169-GE13D		RN03	Conteúdo das colunas do Relatório – Registro M105
As colunas referentes às informações do registro M105 deverão ser preenchidas com os seguintes valores deste registro:

Nat. Base Crédito => recuperar o conteúdo do campo 02-Código da Base de Cálculo do Crédito apurado no período
CST PIS => recuperar o conteúdo do campo 03- CST PIS      
Base PIS Total => recuperar o valor do campo 04- Valor Total da Base de Cálculo escriturada nos documentos e operações.   
Parc. Base PIS Cumulativa => recuperar o valor do campo 05- Parcela do Valor Total da Base de Cálculo informada vinculada a receitas com incidência cumulativa.
Vl. Total Base Crédito => recuperar o valor do campo 06- Valor Total da Base de Cálculo do Crédito, vinculada as receitas com incidência não-cumulativa
Vl. Base do Crédito => recuperar o valor do campo 07- Valor da Base de Cálculo do Crédito, vinculada ao tipo de Crédito escriturado em M100.  
Quant. Total Base do PIS => recuperar o valor do campo 08- Quantidade Total da Base de Cálculo do Crédito apurado em Unidade de Medida de Produto
 Parc.  Quant Base => recuperar o valor do campo 09 - Parcela da base de cálculo do crédito em quantidade (campo 08) vinculada ao tipo de crédito escriturado em M100.		RN04	Colunas referentes aos Registros Vinculados ao Tipo de Crédito no Relatório Analítico 
As colunas referentes aos Registros Vinculados ao Tipo de Crédito PIS/PASEP no relatório analítico serão as seguintes:
 Registro
Nº Documento
Linha do registro
Participante
Orig. Crédito
CFOP
Nat. Base Crédito
CST PIS 
Base do PIS
Alíquota PIS
Quantidade Base PIS
Alíquota PIS em reais
Valor PIS
Percentual do Rateio
Valor da Base PIS vinculado ao tipo de Crédito
Valor do PIS vinculado ao tipo de crédito	OS3169-GE13D		RN05	Conteúdo da Coluna
Registro=> Preencher com o número do registro vinculado ao tipo de crédito.
	OS3169-GE13D		RN06	Conteúdo da Coluna
Nº Documento => Deve recuperar o número do documento quando o registro for igual A100/A170, C100/C170, C190/C191, C395/C396, C500/C501, D100/D101, D500/D501, F100 que compôs o Tipo de Crédito. 	OS3169-GE13D / CH1244/2012		RN07	Conteúdo da Coluna
Linha do registro => Deve recuperar o número da linha do registro, se for o registro F100, F120, F130, F150, F205, F210 e F800 que compôs o tipo de crédito.
		RN08	Conteúdo da Coluna
Participante => Deve recuperar o código do participante (07-IND_FIS_JUR + 08-COD_FIS_JUR da SAFX07) do documento fiscal gerado no registro que compôs o tipo de crédito. Essa coluna preenchida somente quando o registro for igual A100/A170, C100/C170, C190/C191, C395/C396, C500/C501, D100/D101, D500/D501, F100		RN09	Conteúdo da Coluna
Orig. Crédito => Deve recuperar o conteúdo do campo indicador da origem do crédito (IND_ORIG_CRED) gerado no registro que compôs o tipo de crédito. Essa coluna será preenchida somente quando o registro for igual A170, F100, F120 e F130.
	OS3169-GE13D		RN10	Conteúdo da Coluna
CFOP => Deverá recuperar o CFOP do documento fiscal gerado no registro que compôs o tipo de crédito. Essa coluna será preenchida somente quando o registro for igual A100/A170 C100/C170, C190/C191, C395/C396, C500/C501, D100/D101 e D500/D501.
	OS3169-GE13D		RN11	Conteúdo da Coluna
Nat. Base Crédito=> Deve recuperar o Código da Base de Crédito (campo NAT_BC_CRED) gerado no registro que compôs o tipo de crédito. Para os registros que não houver essa informação, esse campo será preenchido a partir da regra RNM105-02 do documento RNG - M100_105_110_500_505_510_V11.
	OS3169-GE13D		RN12	Conteúdo da Coluna
CST PIS => CST PIS (campo CST_PIS) gerado no registro que compôs o tipo de crédito.
	OS3169-GE13D		RN13	Conteúdo da Coluna
Base do PIS => Deve recuperar o Valor da Base de Cálculo do Crédito (campo VL_BC_PIS) gerado no registro que compôs o tipo de crédito. 	OS3169-GE13D		RN14	Conteúdo da Coluna:
Alíquota PIS => Deve recuperar o valor da Alíquota PIS em percentual (campo ALIQ_PIS) gerada no registro que compôs o tipo de crédito. 	OS3169-GE13D		RN15	Conteúdo da Coluna:
Quantidade Base PIS => Deve recuperar o valor da Quantidade Base PIS (campo QUANT_BC_PIS) gerada no registro que compôs o tipo de crédito.	OS3169-GE13D		RN16	Conteúdo da Coluna:
Alíquota PIS em reais => Deve recuperar o valor da Alíquota PIS - em reais (campo ALIQ_PIS_QUANT) gerada no registro que compôs o Tipo de crédito		RN17	Conteúdo da Coluna:
Valor PIS => Deve recuperar o Valor PIS (campo VL_PIS) gerado no registro que compôs o tipo de crédito.     	OS3169-GE13D		RN18	Conteúdo da Coluna:
Percentual do Rateio => Nesta coluna deve ser recuperar o percentual do rateio calculado no registro que esteja com o CST PIS igual 53, 54, 55, 56, 63, 64, 65 e 66 que é armazenado para calcular o valor do campo 07 do registro M105.
	OS3169-GE13D		RN19	Conteúdo da Coluna:
Valor da Base PIS vinculado ao tipo de crédito => Deve preencher com o resultado do valor da coluna Base PIS multiplicado pelo o valor da coluna Percentual do Rateio, quando o campo CST PIS for igual 53, 54, 55, 56, 63, 64, 65 e 66, armazenado para calcular o valor do campo 07 do registro M105.  Se o CST PIS for igual 50, 51, 52, 60, 61 e 62, deve preencher com o valor da coluna Base PIS, armazenado para calcular o valor do campo 07 do registro M105.
	OS3169-GE13D		RN20	Conteúdo da Coluna:
Valor do PIS vinculado ao tipo de crédito => Deve preencher com o resultado do valor da coluna Valor PIS multiplicado pelo o valor da coluna Percentual do Rateio, quando o CST PIS for igual 53, 54, 55, 56, 63, 64, 65 ou 66, armazenado para calcular o valor do campo 08 do registro M100. Se o CST PIS for igual 50, 51, 52, 60, 61 e 62, deve preencher com o valor da coluna Valor PIS, armazenado para calcular o valor do campo 08 do registro M100 .
	OS3169-GE13D		RN21	Totalização dos valores - Registros Vinculados ao Tipo de Crédito PIS 
Deverá efetuar a totalização das colunas: ‘’Base do PIS’’, ‘’Quantidade Base PIS’’, ‘’Valor do PIS’’, Valor Base PIS vinculado ao tipo de crédito’’ e ‘’Valor PIS vinculado ao tipo de crédito’’.
		RN22	Conteúdo das colunas do Relatório - Registro M500:

As colunas referentes às informações do registro M500 deverão ser preenchidas com os seguintes valores deste registro:
Tipo de Crédito => Deve recuperar o conteúdo do campo 02-Código Tipo de Crédito
Base do Crédito => Deve recuperar o valor do campo 04- Valor da Base de Cálculo do Crédito. Se neste campo não houver informação, preencher com o conteúdo do campo 06- Quantidade – Base de cálculo COFINS
Alíquota COFINS => Deve recuperar o valor do campo 05- Alíquota da COFINS (em Percentual). Se neste campo não houver informação, deve preencher com o valor do campo 07- Alíquota da COFINS (em reais).
Vlr  do Crédito => recuperar o valor do campo 08- Valor total do crédito apurado no período
Vlr Ajuste Créscimo => recuperar o valor do campo 09- Valor total dos ajustes de acréscimo
Vlr Ajuste Redução => recuperar o valor do campo 10-Valor total dos ajustes de redução
Vlr Crédito Diferido => recuperar o valor do campo 11- Valor total do crédito diferido no período
Vlr Crédito Disponível =>recuperar o valor do campo 12- Valor Total do Crédito Disponível relativo ao Período
Vlr Crédito Descontado => recuperar o valor do campo 14 - Valor do Crédito disponível, a descontar, da contribuição apurada no próprio período. 
Saldo do Crédito => recuperar o valor do campo 15- Saldo de créditos a utilizar em períodos futuros	OS3169-GE13D		RN23	Conteúdo das colunas do Relatório – Registro M505
As colunas referentes às informações do registro M505 deverão ser preenchidas com os seguintes valores deste registro:

Nat. Base Crédito => recuperar o conteúdo do campo 02-Código da Base de Cálculo do Crédito apurado no período
CST COFINS => recuperar o conteúdo do campo 03- CST COFINS      
Base COFINS Total => recuperar o valor do campo 04- Valor Total da Base de Cálculo escriturada nos documentos e operações.   
Parc. Base COFINS Cumulativa => recuperar o valor do campo 05- Parcela do Valor Total da Base de Cálculo informada vinculada a receitas com incidência cumulativa.
Vl. Total Base Crédito => recuperar o valor do campo 06- Valor Total da Base de Cálculo do Crédito, vinculada as receitas com incidência não-cumulativa
Vl. Base do Crédito => recuperar o valor do campo 07- Valor da Base de Cálculo do Crédito, vinculada ao tipo de Crédito escriturado em M100.  
Quant. Total Base do PIS => recuperar o valor do campo 08- Quantidade Total da Base de Cálculo do Crédito apurado em Unidade de Medida de Produto
 Parc.  Quant Base => recuperar o valor do campo 09 - Parcela da base de cálculo do crédito em quantidade (campo 08) vinculada ao tipo de crédito escriturado em M500.		RN24	Colunas referentes aos Registros Vinculados ao Tipo de Crédito da COFINS no relatório analítico
As colunas referentes aos Registros Vinculados ao Tipo de Crédito no relatório analítico serão os seguintes:
 Registro
Nº Documento
Linha do registro
Participante
Orig. Crédito
CFOP
Nat. Base Crédito
CST COFINS
Base da COFINS
Alíquota COFINS
Quantidade Base COFINS
Alíquota COFINS em reais
Valor COFINS
Percentual do Rateio
Valor da Base COFINS vinculado ao tipo de Crédito
Valor da COFINS vinculado ao tipo de crédito	OS3169-GE13D		RN25	Conteúdo da Coluna
Registro=> Preencher com o número do registro vinculado ao tipo de crédito.
	OS3169-GE13D		RN26	Conteúdo da Coluna
Nº Documento => Deve recuperar o número do documento quando o registro for igual A100/A170, C100/C170, C190/C195, C395/C396, C500/C505, D100/D105, D500/D505 que compôs o Tipo de Crédito. 	OS3169-GE13D		RN27	Linha do registro => Deve recuperar o número da linha do registro, se for o registro F100, F120, F130, F150, F205, F210 e F800 que compôs o tipo de crédito.		RN28	Conteúdo da Coluna
Participante => Deve recuperar o código do participante (07-IND_FIS_JUR + 08-COD_FIS_JUR da SAFX07) do documento fiscal gerado no registro que compôs o tipo de crédito. Essa coluna preenchida somente quando o registro for igual A100/A170, C100/C170, C190/C195, C395/C396, C500/C505, D100/D105, D500/D505.		RN29	Conteúdo da Coluna
Orig. Crédito => O indicador da origem do crédito (campo IND_ORIG_CRED) gerado no registro que compôs o tipo de crédito. Essa coluna será preenchida quando os registros (A170, F100, F120 e F130) que compôs o tipo de crédito foram a partir dos documentos que não tem o Código Fiscal.
	OS3169-GE13D		RN30	Conteúdo da Coluna
CFOP => Deverá recuperar o CFOP do documento fiscal gerado no registro que compôs o tipo de crédito. Essa coluna será preenchida somente quando o registro for igual A100/A170 C100/C170, C190/C195, C395/C396, C500/C501, D100/D105 e D500/D505.	OS3169-GE13D		RN31	Conteúdo da Coluna
Nat. Base Crédito=> Código da Base de Crédito (campo NAT_BC_CRED) gerado no registro que compôs o tipo de crédito. Para os registros que não houver essa informação, esse campo será preenchido a partir da regra RNM505-02 do documento RNG - M100_105_110_500_505_510_V11.
	OS3169-GE13D		RN32	Conteúdo da Coluna
CST COFINS => CST COFINS (campo CST_COFINS) gerado no registro que compôs o tipo de crédito.
	OS3169-GE13D		RN33	Conteúdo da Coluna
Base da COFINS => Deve ser preenchida com Valor da Base de Cálculo do Crédito (campo VL_BC_COFINS) gerado no registro que compôs o tipo de crédito. Se neste campo não houver informação, preencher com o conteúdo do campo Quantidade – Base de cálculo COFINS (campo QUANT_BC_COFINS).	OS3169-GE13D		RN34	Conteúdo da Coluna:
Alíquota COFINS => Deve ser preenchida com Alíquota COFINS (campo ALIQ_COFINS) gerada no registro que compôs o tipo de crédito. 	OS3169-GE13D		RN35	Conteúdo da Coluna
Quantidade Base COFINS=> Deve ser recuperado o valor da Quantidade Base COFINS (QUANT_BC_COFINS) gerada no registro que compôs o tipo de crédito. 	OS3169-GE13D		RN36	Conteúdo da Coluna
Alíquota COFINS em reais => Deve ser recuperado o valor da Alíquota COFINS em reais (campo ALIQ_COFINS_QUANT) gerada no registro que compôs o tipo de crédito	OS3169-GE13D		RN37	Conteúdo da Coluna:
Valor COFINS => Deve ser preenchido com o Valor COFINS (campo VL_COFINS) gerado no registro que compôs o tipo de crédito.     	OS3169-GE13D		RN38	Conteúdo da Coluna:
Percentual do Rateio => Nesta coluna deve ser recuperar o percentual do rateio calculado no registro com o campo CST_COFINS igual 53, 54, 55, 56, 63, 64, 65 e 66, armazenado para calcular o valor do campo 07 do registro M505.
	OS3169-GE13D		RN39	Conteúdo da Coluna:
Valor da Base COFINS vinculado ao tipo de crédito => Deve preencher com o resultado do valor da coluna Base COFINS multiplicado pelo o valor da coluna Percentual do Rateio, quando o campo CST COFINS for igual 53, 54, 55, 56, 63, 64, 65 e 66, armazenado para calcular o valor do campo 07 do registro M505.  Se o CST COFINS for igual 50, 51, 52, 60, 61 e 62 de preencher com o valor da coluna BASE COFINS,  armazenado para calcular o valor do campo 07 do registro M505.
	OS3169-GE13D		RN40	Conteúdo da Coluna:
Valor do PIS vinculado ao tipo de crédito => Deve preencher com o resultado do valor da coluna Valor COFINS multiplicado pelo o valor da coluna Percentual do Rateio, quando o CST COFINS for igual  53, 54, 55, 56, 63, 64, 65 ou 66,  armazenado para calcular o valor do campo 08 do registro M500. Se o CST COFINS for igual 50, 51, 52, 60, 61 e 62 deve preencher com o valor da coluna Valor COFINS, armazenado para calcular o valor do campo 08 do registro M500.
	OS3169-GE13D		RN41	Totalização dos valores das colunas ref. aos Registros Vinculados ao Tipo de Crédito COFINS (relatório analítico) 
Deverá efetuar a totalização das colunas: ‘’Base da COFINS’’, ‘’Quantidade Base COFINS” e ‘’Valor da COFINS’’, ‘’Valor da Base COFINS vinculado ao tipo de crédito’’ e ‘’Valor COFINS vinculado ao tipo de crédito’’
		


2 - Relatório de Demonstrativo de Apuração por Tipo de Contribuição


REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN42	Relatório de Demonstrativo da Apuração por Tipo de Contribuição 

Pré-requisito:
É necessário realizar a Geração dos Registros disponíveis nas opções de menu Obrigações >> Geração dos Registros e Obrigações SCP >> Geração dos Registros, com o parâmetro “Demonstrativo da Apuração por Tipo de Contribuição” selecionado.

 Processamento 
Origem dos dados:
Informações dos registros M200, M210, M600 e M610 ( tabela interna que armazena os dados da apuração da Contribuição do Período (registros M200, M210 e M600 e M610) calculados conforme regras descritas no documento “RNG- M200_210_211_600_610_611_v11.doc” a partir da geração dos registros. 

Informações dos Registros vinculados ao tipo de contribuição ( tabela interna que armazena os dados das gerações dos registros do Bloco A, C, D e F.  

Critérios de recuperação dos dados para geração do relatório: Se no parâmetro ‘’Gerar Relatório Demonstrativo da Apuração no Período Informado a opção ‘’Tipo de Contribuição’’ estiver marcado na tela de Geração dos Registros. 

Critérios dos filtros na tela de Emissão do Relatório da Apuração por Tipo de Contribuição:
O relatório Demonstrativo da Apuração no Período por Tipo de Contribuição deverá ser emitido de acordo com os filtros selecionados na Tela, localizada no módulo: SPED ( EFD-PIS/PASEP-COFINS, menu: Obrigações ( Demonstrativos ( Emissão do Relatório Demonstrativo da Apuração ( por Tipo de Contribuição 

Ordenação: 
Linhas dos Registros M200/M600 ( Deverá seguir a mesma ordenação gerada no meio magnético.
Linhas dos Registros vinculado ao tipo de contribuição ( registro + Nº Documento, CFOP e Nat. Base Crédito.
Linhas dos Registros M210/M610( Deverá seguir a mesma ordenação gerada no meio magnético.

	OS3169-GE13D		RN43	Relatório Demonstrativo da Apuração por Tipo de Contribuição - Analítico com base na regra abaixo.


Se na tela de Emissão do Relatório por Tipo de Contribuição somente a opção ‘’M200’’ do campo Registro estiver marcado:
  Listar as informações de cada documento fiscal gerado nos registros A100/A170, C100/C170, C180/C181, C380/C381, C405/C481, C490/C491, C600/C601, D200/D201, D300, D350, D600/D601, F100, F200 que compôs todos os tipos de contribuição, ou seja, considerar todos os registros associados aos registros M210, conforme segue:

REGISTRO M200
   < REGISTROS VINCULADOS AOS REGISTROS M210>


Nesta forma de emissão a totalização dos registros (informada na regra RN63) deverá ser feita, demonstrando a totalização de todos os registros vinculados de todos os registros M210.

 Se na tela de Emissão do Relatório por Tipo de Contribuição somente a opção ‘’M200’ e ‘’M210’’ do campo Registro estiver marcado:
    Listar o registro M200, em seguida será listado os registros M210 pertencentes ao registro M200 e seus registros vinculados, conforme demonstrado a seguir

REGISTRO M200
      REGISTRO M210
    <REGISTROS VINCULADOS AO REGISTRO M210 >
  REGISTRO M200
    <REGISTROS VINCULADOS AO REGISTRO M210 >

Nesta forma de emissão a totalização dos registros (informada na regra RN83) deverá ser feita para cada quebra realizada no relatório, ou seja, deverá ser feita a cada listagem de registros vinculados pertencente ao um registro M210.

Se na tela de Emissão do Relatório por Tipo de Contribuição somente a opção ‘’M600’’ do campo Registro estiver marcado:
  Listar as informações de cada documento fiscal gerado nos registro A100/A170, C100/C170, C180/C185, C380/C385, C405/C485, C490/C495, C600/C605, D200/D205, D300, D350, D600/D605, F100, F200 que compôs todos os tipos de contribuição, ou seja, considerar todos os registros associados aos registros M210, conforme segue:

REGISTRO M600
   < REGISTROS VINCULADOS AOS REGISTROS M610>


Importante:
O relatório sintético não será desenvolvido na OS3169-GE13D 
		
Nesta forma de emissão a totalização dos registros (informada na regra RN63) deverá ser feita, demonstrando a totalização de todos os registros vinculados de todos os registros M610.

Se na tela de Emissão do Relatório por Tipo de Contribuição somente a opção ‘’M600’ e ‘’M610’’ do campo Registro estiver marcado:
    Listar o registro M600, em seguida será listado os registros M610 pertencentes ao registro M600 e seus registros vinculados, conforme demonstrado a seguir

REGISTRO M600
      REGISTRO M610
    <REGISTROS VINCULADOS AO REGISTRO M610 >
  REGISTRO M600
    <REGISTROS VINCULADOS AO REGISTRO M610 >

Nesta forma de emissão a totalização dos registros (informada na regra RN83) deverá ser feita para cada quebra realizada no relatório, ou seja, deverá ser feita a cada listagem de registros vinculados pertencente ao um registro M610.
		RN44	
Conteúdo das colunas do Relatório (Analítico e Sintético) - Registro M200:

As colunas referentes às informações do registro M200 deverão ser preenchidas com os seguintes valores deste registro:

Vlr Total Contrib N.Cum => recuperar o valor do campo 02- Valor Total da Contribuição Não Cumulativo no Período
 Vlr Crédito Descto Período => recuperar o valor do campo 03- Valor Total do Crédito Descontado, Apurado no Próprio Período da Escrituração
 Vlr. Crédito Descto Período Anterior => recuperar o valor do campo 04- Valor Total do Crédito Descontado, Apurado em Período da Apuração Anterior
 Total Contrib. N. Cum. =>recuperar o valor do campo 05- Valor Total da Contribuição Não Cumulativa Devida.   
 Vlr Retido na Fonte => recuperar o valor do campo 06- Valor Retido na Fonte Deduzido no Período     
 Outras Deduções Período =>recuperar o valor do campo 07- Outras Deduções no Período  
 Vlr. Total Contrib. N. Cum.  a Recolher/Pagar =>recuperar o valor do campo 08- Valor da Contribuição Não Cumulativa a Recolher/Pagar
  Vlr Total Contrib. Cum.  =>recuperar o valor do campo 09- Valor Total da Contribuição Cumulativa do Período 
  Vlr Retido=>recuperar o valor do campo 10- Valor Retido na Fonte Deduzido no Período 
  Outras Deduções no Período => recuperar o valor do campo 11-Outras Deduções no Período      
Vlr Total Contrib. Cum. a Recolher/Pagar => recuperar  o valor do campo 12- Valor da Contribuição a Recolher/Pagar no Período
 Vlr Total Contrib a Pagar no Período => recuperar o valor do campo 13- Valor Total da Contribuição a Recolher/Pagar no Período
                                                                                                        	OS3169-GE13D		RN45	Conteúdo das colunas do Relatório (Analítico e Sintético) - Registro M210 

As colunas referentes às informações do registro M210 deverão ser preenchidas com os seguintes valores deste registro:

Tipo Contrib. => Deve recuperar o conteúdo do campo 02-Código da contribuição social apurada no período 
 Vlr. Receita Bruta =>recuperar o valor do campo 03- Valor da Receita Bruta
 Vlr. Base de Cálculo => recuperar o valor do campo 04-Valor da Base de Cálculo da Contribuição
Vlr Tot. Ajustes Acréscimo BC
Vlr Tot. Ajustes Redução BC
Vlr BC da Contribuição
Alíquota PIS (Percentual) => recuperar o valor do campo 05- Alíquota do PIS/PASEP (em percentual)    
Quant. Base PIS => recuperar o valor do campo 06- Quantidade – Base de cálculo PIS  
Alíquota do PIS (reais) => recuperar o valor do campo 07- Alíquota do PIS (em reais) 
Vlr total Contrib. => recuperar o valor do campo 08- Valor total da contribuição social apurada       
Vlr total Ajustes Acréscimo => recuperar o valor do campo 09- Valor total dos ajustes de acréscimo  
Vlr total Ajustes Redução => recuperar o valor do campo 10- Valor total dos ajustes de redução    
 Vlr. Total Contrib. Diferir no Período => recuperar o valor do campo 11- Valor total da contribuição a diferir no período     
Vlr. Contrib Diferida no Período Anterior => recuperar o valor do campo 12- Valor da contribuição diferida em períodos anteriores   
 Vlr Total da Contribuição => recuperar o valor do campo 13- Valor Total da Contribuição do Período                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                      
	OS3169-GE13D
MFS20227		RN46	Colunas referentes aos Registros Vinculados ao Tipo de Contribuição PIS/PASEP - (Relatório Analítico) 
As colunas referentes aos Registros Vinculados ao Tipo de Crédito no relatório analítico serão os seguintes:
 Registro
Linha do registro
Nº/Serie/Subserie
Cód. da Unidade Imobiliária
Adquirente
Cod. Item
CFOP
CST PIS
Valor do Item
Valor Total Docto
Valor Venda Bruta         
Valor da Operação     
Valor Total da Receita (Unid. Imobiliária)        
Base do PIS
Alíquota PIS
Quantidade Base PIS
Alíquota PIS em reais
Valor PIS	OS3169-GE13D/
OS3821		RN47	Conteúdo da Coluna:
Registro=> Preencher com o número do registro vinculado ao tipo de contribuição.	OS3169-GE13D		RN48	Conteúdo da Coluna
Nº /Série /Subserie => Deve recuperar o número do documento, quando o registro for A100/A170, C100/C170, C180/C181 que compôs o tipo de contribuição.	OS3169-GE13D		RN49	Conteúdo da Coluna
Nº Linha do Registro=> Deve recuperar o número da linha do registro para os registros C381, C481, C491, C601, D201, D300, D350, D601, F100, F200. Para os demais registros esse campo não deve ser preenchido	OS3169-GE13D		RN49.01	Conteúdo da Coluna
Cód. da Unidade Imobiliária => Deve recuperar o campo referente ao código da Unidade Imobiliária do registro F200. Para os demais registros esse campo não deve ser preenchido	OS3821		RN49.02	Conteúdo da Coluna
Adquirente => Deve recuperar o campo referente ao adquirente do registro F200. Para os demais registros esse campo não deve ser preenchido	OS3821		RN50	Conteúdo da Coluna:
Cod. Item => Deve recuperar o conteúdo do campo COD_ITEM, quando o registro for igual A170, C170, C181, C381, C481, C491 e o registro F100 que compôs o Tipo de Contribuição. 
		RN51	Conteúdo da Coluna:
CFOP=> Deve recuperar o código fiscal do campo CFOP gerado no registro que compôs o tipo de Contribuição. Essa coluna será preenchida quando os registros que compôs o tipo de contribuição foram gerados a partir de documentos fiscais
	OS3169-GE13D		RN52	Conteúdo da Coluna:
CST PIS => Deverá recuperar o conteúdo do campo CST_PIS nos registros que compôs o Tipo de Contribuição. 
	OS3169-GE13D		RN53	Conteúdo da Coluna:
Valor Item => Deve recuperar o valor do campo VLR_ITEM, quando registro for A170, C170, C185, C381, C481, C491, C601, D201 e D601 ser preenchido.	OS3169-GE13D		RN54	Conteúdo da Coluna:
Valor Total do Docto. => Deve recuperar o valor do campo VL_DOC do registro D300. Esse campo não deve ser preenchido para os demais registros	OS3169-GE13D		RN55	Conteúdo da Coluna:
Valor Venda Bruta => Deve recuperar o valor do campo VL_BRT do registro D350. Esse campo não deve ser preenchido para os demais registros       
	OS3169-GE13D		RN56	Conteúdo da Coluna
Valor da Operação => Deve recuperar o valor do campo VL_OPER do registro F100. Esse campo não deve ser preenchido para os demais registros	OS3169-GE13D		RN57	Conteúdo da Coluna
Valor Total da Receita (Unid. Imobiliária) => Deve recuperar o valor do campo VL_TOT_REC. Esse campo não deve ser preenchido para os demais registros.      
	OS3169-GE13D		RN58	Conteúdo da Coluna:
Base do PIS=> Deve recuperar o valor do campo VL_BC_PIS do registro que compôs o tipo de contribuição. 	OS3169-GE13D		RN59	Alíquota PIS => Deve recuperar o valor do campo ALIQ_PIS do registro que compôs o tipo de contribuição. 	OS3169-GE13D		RN60	Quantidade Base PIS => Deve recuperar o valor do campo QUANT_BC_PIS do registro que compôs o tipo de contribuição	OS3169-GE13D		RN61	Alíquota PIS em reais => Deve recuperar o valor do campo ALIQ_PIS_QUANT do registro que compôs o tipo de contribuição.
	OS3169-GE13D		RN62	Conteúdo da Coluna:
Valor PIS => Deve recuperar o valor do campo VL_PIS gerado no registro que compôs o tipo de contribuição.	OS3169-GE13D		RN63	Totalização das colunas referentes aos Registros Vinculados ao Tipo de Contribuição PIS/PASEP - Relatório Analítico

Deverá efetuar a totalização dos valores das colunas: ‘’Valor Item’’, ‘’Valor Total do Docto’’, ’’Valor da Venda Bruta’’ e ‘’Valor da Operação”,  ‘’Valor Total da Receita (Unid. Imobiliária)’’, ‘’ Base do PIS’’, ‘’Quantidade Base PIS’’, ‘’Alíquota PIS em Reais’’ e  ‘’Valor PIS’’.
	OS3169-GE13D		
RN64	
Conteúdo das colunas do Relatório - Registro M600 

As colunas referentes às informações do registro M600 deverão ser preenchidas com os seguintes valores deste registro:

Vlr Total Contrib N.Cum => recuperar o valor do campo 02- Valor Total da Contribuição Não Cumulativo no Período
 Vlr Crédito Descto Período => recuperar o valor do campo 03- Valor Total do Crédito Descontado, Apurado no Próprio Período da Escrituração
 Vlr. Crédito Descto Período Anterior => recuperar o valor do campo 04- Valor Total do Crédito Descontado, Apurado em Período da Apuração Anterior
 Total Contrib. N. Cum. =>recuperar o valor do campo 05- Valor Total da Contribuição Não Cumulativa Devida.   
 Vlr Retido na Fonte => recuperar o valor do campo 06- Valor Retido na Fonte Deduzido no Período     
 Outras Deduções Período =>recuperar o valor do campo 07- Outras Deduções no Período  
 Vlr. Total Contrib. N. Cum.  a Recolher/Pagar =>recuperar o valor do campo 08- Valor da Contribuição Não Cumulativa a Recolher/Pagar
  Vlr Total Contrib. Cum.  =>recuperar o valor do campo 09- Valor Total da Contribuição Cumulativa do Período 
  Vlr Retido=>recuperar o valor do campo 10- Valor Retido na Fonte Deduzido no Período 
  Outras Deduções no Período => recuperar o valor do campo 11-Outras Deduções no Período      
Vlr Total Contrib. Cum. a Recolher/Pagar => recuperar  o valor do campo 12- Valor da Contribuição a Recolher/Pagar no Período
 Vlr Total Contrib a Pagar no Período => recuperar o valor do campo 13- Valor Total da Contribuição a Recolher/Pagar no Período
                                                                                                        	OS3169-GE13D		RN65	Conteúdo das colunas do Relatório - Registro M610 

As colunas referentes às informações do registro M610 deverão ser preenchidas com os seguintes valores deste registro:

Tipo Contrib. => Deve recuperar o conteúdo do campo 02-Código da contribuição social apurada no período 
 Vlr. Receita Bruta =>recuperar o valor do campo 03- Valor da Receita Bruta
 Vlr. Base de Cálculo => recuperar o valor do campo 04-Valor da Base de Cálculo da Contribuição
Vlr Tot. Ajustes Acréscimo BC
Vlr Tot. Ajustes Redução BC
Vlr BC da Contribuição
 Alíquota COFINS (Percentual) => recuperar o valor do campo 05- Alíquota da COFINS (em percentual)    
Quant. Base COFINS => recuperar o valor do campo 06- Quantidade – Base de cálculo COFINS  
Alíquota da COFINS (reais) => recuperar o valor do campo 07- Alíquota da COFINS (em reais) 
Vlr total Contrib. => recuperar o valor do campo 08- Valor total da contribuição social apurada       
Vlr total Ajustes Acréscimo => recuperar o valor do campo 09- Valor total dos ajustes de acréscimo  
Vlr total Ajustes Redução => recuperar o valor do campo 10- Valor total dos ajustes de redução    
 Vlr. Total Contrib. Diferir no Período => recuperar o valor do campo 11- Valor total da contribuição a diferir no período     
Vlr. Contrib Diferida no Período Anterior => recuperar o valor do campo 12- Valor da contribuição diferida em períodos anteriores   
 Vlr Total da Contribuição => recuperar o valor do campo 13- Valor Total da Contribuição do Período                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                      
	OS3169-GE13D
MFS20227		RN66	Colunas referentes aos Registros Vinculados ao Tipo de Contribuição COFINS - Relatório Analítico
As colunas referentes aos Registros Vinculados ao Tipo de Contribuição no relatório analítico serão os seguintes (devem ser apresentados na seguinte ordem):
 Registro
Linha do registro
Nº/Serie/Subserie
Cód. da Unidade Imobiliária
Adquirente
Cod. Item
CFOP
CST COFINS
Valor do Item
Valor Total Docto
Valor Venda Bruta         
Valor da Operação     
Valor Total da Receita (Unid. Imobiliária)        
Base da COFINS
Alíquota COFINS
Quant. Base COFINS
Alíquota COFINS em Reais
Valor COFINS
	OS3169-GE13D/ OS3821		RN67	Conteúdo da Coluna:
Registro=> Preencher com o número do registro vinculado ao tipo de contribuição.	OS3169-GE13D		RN68	Conteúdo da Coluna
Nº Documento => Deve recuperar o número do documento gerado no registro A100/A170, C100/C170 e C180/C185 que compôs o tipo de contribuição. Para os demais registros esse campo não deve ser preenchido.	OS3169-GE13D		RN69	Conteúdo da Coluna
Linha do Registro=> Deve recuperar o número da linha do registro, se for o registro C385, C485, C495, C605, D205, D300, D350, D605, F100 e F200. Para os demais registros esse campo não deve ser preenchido. 	OS3169-GE13D		RN69.01	Conteúdo da Coluna
Cód. da Unidade Imobiliária => Deve recuperar o campo referente ao código da Unidade Imobiliária do registro F200. Para os demais registros esse campo não deve ser preenchido	OS3821		RN69.02	Conteúdo da Coluna
Adquirente => Deve recuperar o campo referente ao adquirente do registro F200. Para os demais registros esse campo não deve ser preenchido	OS3821		RN70	Conteúdo da Coluna:
CST COFINS => Deverá recuperar o conteúdo do campo CST_COFINS nos registros que compôs o Tipo de Contribuição. 
		RN71	Conteúdo da Coluna:
CFOP=> Deve recuperar o código fiscal do campo CFOP, quando o registro for C100/C170, C180/C185, D200/D205, C400/C495 que compôs o tipo de Contribuição.  Para os demais registros esse campo não deve ser preenchido.	OS3169-GE13D		RN72	Conteúdo da Coluna:
Cod. Item => Deve recuperar o conteúdo do campo COD_ITEM, quando o registro for igual A170, C170, C185, C385, C485, C495 e F100 compôs o Tipo de Contribuição. 
	OS3169-GE13D		RN73	Conteúdo da Coluna:
Valor Item => Deve recuperar o valor do campo VLR_ITEM, quando registro for A170, C170, C185, C385, C485, C495, C605, D205 e D605. Para os demais registros esse campo não deve ser preenchido.	OS3169-GE13D		RN74	Conteúdo da Coluna:
Valor Total do Docto. => Deve recuperar o valor do campo VL_DOC do registro D300. Esse campo não deve ser preenchido para os demais registros	OS3169-GE13D		RN75	Conteúdo da Coluna:
Valor Venda Bruta => Deve recuperar o valor do campo VL_BRT do registro D350. Esse campo não deve ser preenchido para os demais registros       
	OS3169-GE13D		RN76	Conteúdo da Coluna
Valor da Operação => Deve recuperar o valor do campo VL_OPER do registro F100. Esse campo não deve ser preenchido para os demais registros	OS3169-GE13D		RN77	Conteúdo da Coluna
Valor Total da Receita (Unid. Imobiliária) => Deve recuperar o valor do campo VL_TOT_REC do registro F200 que compôs o tipo de contribuição. Esse campo não deve ser preenchido para os demais registros.   
	OS3169-GE13D		RN78	Conteúdo da Coluna:
Base da COFINS=> Deve recuperar o valor do campo VL_BC_COFINS do registro que compôs o tipo de contribuição. 	OS3169-GE13D		RN79	Alíquota COFINS => Deve recuperar o valor do campo ALIQ_COFINS gerada no registro que compôs o tipo de contribuição. 	OS3169-GE13D		RN80	Quantidade Base COFINS => Deve recuperar o valor do campo QUANT_BC_COFINS que compôs o tipo de contribuição. 		RN81	Alíquota COFINS em reais  => Deve recuperar o valor do campo ALIQ_COFINS_QUANT no registro que compôs o tipo de contribuição.		RN82	Conteúdo da Coluna:
Valor COFINS => Deve recuperar o valor do campo VL_COFINS gerado no registro que compôs o tipo de contribuição.	OS3169-GE13D		RN83	Totalização das colunas referentes aos Registros Vinculados ao Tipo de Contribuição COFINS - Relatório Analítico

Deverá efetuar a totalização dos valores das colunas: ‘’Valor Item’’, ‘’Valor Total do Docto’’, ’’Valor da Venda Bruta’’ e ‘’Valor da Operação”,  ‘’Valor Total da Receita (Unid. Imobiliária)’’, ‘’ Base da COFINS’’, ‘’ Quantidade Base COFINS’’ e  ‘’Valor COFINS’’.
	OS3169-GE13D		


3 - Relatório de Demonstrativo da Apuração por Tipo de Natureza da Receita

REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN84	Relatório de Demonstrativo da Apuração por Tipo de Natureza da Receita

Pré-requisito:
É necessário realizar a Geração dos Registros disponíveis nas opções de menu Obrigações >> Geração dos Registros e Obrigações SCP >> Geração dos Registros, com o parâmetro “Demonstrativo da Apuração por Tipo de Natureza da Receita” selecionado.

 Processamento 
Origem dos dados:
Informações dos registros M400, M410, M800 e M810 ( tabela interna que armazena os dados dos registros M400, M410,M800 e M810) calculados conforme regras descritas no documento “RNG - M400_M410_M800_M810_v7.doc” a partir da geração dos registros. 

Informações dos Registros vinculados ( tabela interna que armazena os dados das gerações dos registros do Bloco A, C, D e F.  

Critérios de recuperação dos dados para geração do relatório: Se no parâmetro ‘’Gerar Relatório Demonstrativo da Apuração no Período Informado’’ a opção ‘’Tipo de Natureza da Receita’’ estiver marcado na tela de Geração dos Registros 

Critérios dos filtros na tela de Emissão do Relatório da Apuração por Tipo de Natureza da Receita:
O relatório Demonstrativo da Apuração no Período por Tipo de Natureza da Receita deverá ser emitido de acordo com os filtros selecionados na Tela, localizada no módulo: SPED ( EFD – Escrituração Fiscal Digital das Contribuições, menu: Obrigações ( Demonstrativos ( Emissão do Relatório Demonstrativo da Apuração ( por Tipo de Natureza da Receita

Ordenação: 
Linhas dos Registros M400/M800 ( Deverá ser ordenado por CST (ordem crescente)
Linhas dos Registros M410/M810( Deverá ser ordenado por Código da Natureza da Receita + Registro + Nº Documento 

OBS. Considere a regra acima paras as opções Sintética e Analítica do relatório.	OS3583		RN85	O relatório Demonstrativo da Apuração por tipo de Natureza da Receita - Analítico será gerado com base nas seguintes regras:

Se na tela de Emissão do Relatório por Tipo de Natureza da Receita  somente a opção ‘’M400’’ do campo Tipo de Registro estiver marcado:
  Listar as informações de cada documento fiscal gerado nos registros , C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 com base nos CST específicos (04, 05 - com alíquota zero, 06, 07, 08 e 09). Considerar todos os registros, mesmo aqueles que estejam associados aos registros M410.
Nesta forma de emissão a totalização dos registros  deverá ser feita para cada CST existente, demonstrando a totalização de todos os registros vinculados direta ou indiretamente do registro M400.


Se na tela de Emissão do Relatório por Tipo de Natureza da Receita as opções: ‘’M400’’ e ‘’M410’’ do campo Tipo de Registro estiverem marcados:
  Listar os registros M400 e, abaixo deste, listar os registros vinculados diretamente ao M400, ou seja, registros que não possuam associação com registros M410.  Em seguida serão listados os registros M410 pertencentes ao registro M400 e seus registros vinculados.

Se na tela de Emissão do Relatório por Tipo de Natureza da Receita  somente a opção ‘’M800’’ do campo Tipo de Registro estiver marcado:
  Listar as informações de cada documento fiscal gerado nos registros , C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 com base nos CST específicos (04, 05 - com alíquota zero, 06, 07, 08 e 09). Considerar todos os registros, mesmo aqueles que estejam associados aos registros M810.
Nesta forma de emissão a totalização dos registros  deverá ser feita para cada CST existente, demonstrando a totalização de todos os registros vinculados direta ou indiretamente do registro M800.

Se na tela de Emissão do Relatório por Tipo de Natureza da Receita as opções: ‘’M800’’ e ‘’M810’’ do campo Tipo de Registro estiverem marcados:
  Listar os registros M800 e, abaixo deste, listar os registros vinculados diretamente ao M800, ou seja, registros que não possuam associação com registros M810.  Em seguida serão listados os registros M810 pertencentes ao registro M800 e seus registros vinculados.

Importante:
Na tela de Emissão do relatório demonstrativo da apuração por tipo de natureza da receita não será permitido no campo Registro marcar somente a opção M410 e/ou M810.   	OS3583		RN86	Analítico: Conteúdo das colunas do Relatório - Registro M400

As colunas referentes às informações do registro M400 deverão ser preenchidas com os seguintes valores deste registro:

CST => Deve recuperar o conteúdo do campo 02 do registro M400.
Valor Total da Receita Bruta => Deve recuperar o valor do campo 03 do registro M400
Conta Analítica Contábil=> Deve recuperar o valor do campo 04 do registro M400
Descrição Complementar da Natureza da Receita => Deve recuperar o valor do campo 05 do registro M400	OS3583		RN87	

Analítico: Conteúdo das colunas do Relatório – Registro M410
As colunas referentes às informações do registro M410 deverão ser preenchidas com os seguintes valores deste registro:


Natureza da Receita => Deve recuperar o conteúdo do campo 02 do registro M410.
Valor da Receita Bruta no Período   => Deve recuperar o conteúdo do campo 03 do registro M410.
Conta Analítica Contábil => Deve recuperar o conteúdo do campo 04 do registro M410.
 Descrição Complementar da Natureza da Receita => Deve recuperar o conteúdo do campo 04 do registro M410.
Item: Registros Vinculados à Natureza da Receita
Registro => Preencher com o número do registro gerado.
Nº Documento =>  Deve recuperar o número do documento gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M400.
Participante => Deve recuperar o código do participante / cliente gerado no registro for C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M400.
CFOP => Deve recuperar o código fiscal gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M400.


NCM => Deve recuperar o NCM gerado nos registros C170, C181, C381, C481, C491, C601, F100, F200 que compôs a geração do Registro M400 


Os registros que não existirem código NCM (COD_NCM), utilizar o código do item (COD_ITEM) para identificar o NCM do produto na tabela de produto item 06 da SAFX2013 conforme tabela abaixo. 

Registro
Campo

C180
COD_NCM


C381
COD_ITEM


C385
COD_ITEM


C481
COD_ITEM


C485
COD_ITEM


C491
COD_ITEM


C495
COD_ITEM


F100
COD_ITEM


Observação: O registro F525 não é utilizado para o lucro presumido.  
 
Base PIS => Deve recuperar campo Base PIS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M400.
Alíq. PIS => Deve recuperar o campo Alíquota PIS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M400.
Quant.Base PIS => Deve recuperar o campo Quant. Base PIS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M400.
Alíq. PIS em Reais => Deve recuperar o campo Alíq. PIS em Reais gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M400.
Valor PIS => Deve recuperar o campo Valor PIS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M400.	OS3583
OS4110		RN88	Analítico: Conteúdo das colunas do Relatório - Registro M800

As colunas referentes às informações do registro M400 deverão ser preenchidas com os seguintes valores deste registro:

CST => Deve recuperar o conteúdo do campo 02 do registro M800.
Valor Total da Receita Bruta => Deve recuperar o valor do campo 03 do registro M800
Conta Analítica Contábil=> Deve recuperar o valor do campo 04 do registro M800
Descrição Complementar da Natureza da Receita => Deve recuperar o valor do campo 05 do registro M800
	OS3583		RN89	

Analítico: Conteúdo das colunas do Relatório – Registro M810
As colunas referentes às informações do registro M810 deverão ser preenchidas com os seguintes valores deste registro:


Natureza da Receita => Deve recuperar o conteúdo do campo 02 do registro M810.
Valor da Receita Bruta no Período   => Deve recuperar o conteúdo do campo 03 do registro M810.
Conta Analítica Contábil => Deve recuperar o conteúdo do campo 04 do registro M810.
 Descrição Complementar da Natureza da Receita => Deve recuperar o conteúdo do campo 04 do registro M810.
Item Registros Vinculados à Natureza da Receita
Registro => Preencher com o número do registro gerado.
Nº Documento =>  Deve recuperar o número do documento gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M800.
Participante => Deve recuperar o código do participante / cliente gerado no registro for C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M800.
CFOP => Deve recuperar o código fiscal gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M800.


NCM => Deve recuperar o NCM gerado nos registros C170, C181, C381, C481, C491, C601, F100, F200 que compôs a geração do Registro M800 

Os registros que não existirem código NCM (COD_NCM), utilizar o código do item (COD_ITEM) para identificar o NCM do produto na tabela de produto item 06 da SAFX2013 conforme tabela abaixo. 

Registro
Campo

C180
COD_NCM


C381
COD_ITEM


C385
COD_ITEM


C481
COD_ITEM


C485
COD_ITEM


C491
COD_ITEM


C495
COD_ITEM


F100
COD_ITEM


Observação: O registro F525 não é utilizado para o lucro presumido.  


Base COFINS => Deve recuperar campo Base COFINS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M800.
Alíq. COFINS => Deve recuperar o campo Alíquota COFINS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M800.
Quant.Base COFINS => Deve recuperar o campo Quant. Base COFINS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M800.
Alíq.COFINS em Reais => Deve recuperar o campo Alíq. COFINS em Reais gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M800.
Valor COFINS => Deve recuperar o campo Valor COFINS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M800.
	OS3583
OS4110		RN90	O relatório Demonstrativo da Apuração por tipo de Natureza da Receita - Sintético será gerado com base nas seguintes regras:

Se na tela de Emissão do Relatório por Tipo de Natureza da Receita  somente a opção ‘’M400’’ do campo Tipo de Registro estiver marcado:
  Listar as informações de cada documento fiscal gerado nos registros , C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 com base nos CST específicos (04, 05 - com alíquota zero, 06, 07, 08 e 09). Considerar todos os registros, mesmo aqueles que estejam associados aos registros M410.
Nesta forma de emissão a totalização dos registros  deverá ser feita para cada CST existente, demonstrando a totalização de todos os registros vinculados direta ou indiretamente do registro M400.


Se na tela de Emissão do Relatório por Tipo de Natureza da Receita as opções: ‘’M400’’ e ‘’M410’’ do campo Tipo de Registro estiverem marcados:
  Listar os registros M400 e, abaixo deste, listar os registros vinculados diretamente ao M400, ou seja, registros que não possuam associação com registros M410.  Em seguida serão listados os registros M410 pertencentes ao registro M400 e seus registros vinculados.

Se na tela de Emissão do Relatório por Tipo de Natureza da Receita  somente a opção ‘’M800’’ do campo Tipo de Registro estiver marcado:
  Listar as informações de cada documento fiscal gerado nos registros , C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 com base nos CST específicos (04, 05 - com alíquota zero, 06, 07, 08 e 09). Considerar todos os registros, mesmo aqueles que estejam associados aos registros M810.
Nesta forma de emissão a totalização dos registros  deverá ser feita para cada CST existente, demonstrando a totalização de todos os registros vinculados direta ou indiretamente do registro M800.

Se na tela de Emissão do Relatório por Tipo de Natureza da Receita as opções: ‘’M800’’ e ‘’M810’’ do campo Tipo de Registro estiverem marcados:
  Listar os registros M800 e, abaixo deste, listar os registros vinculados diretamente ao M800, ou seja, registros que não possuam associação com registros M810.  Em seguida serão listados os registros M810 pertencentes ao registro M800 e seus registros vinculados.

Importante:
Na tela de Emissão do relatório demonstrativo da apuração por tipo de natureza da receita não será permitido no campo Registro marcar somente a opção M410 e/ou M810.   	OS3583		RN91	Sintético: Conteúdo das colunas do Relatório - Registro M400

As colunas referentes às informações do registro M400 deverão ser preenchidas com os seguintes valores deste registro:

CST => Deve recuperar o conteúdo do campo 02 do registro M400.
Valor Total da Receita Bruta => Deve recuperar o valor do campo 03 do registro M400
Conta Analítica Contábil=> Deve recuperar o valor do campo 04 do registro M400
Descrição Complementar da Natureza da Receita => Deve recuperar o valor do campo 05 do registro M400	OS3583		RN92	Sintético: Conteúdo das colunas do Relatório – Registro M410
As colunas referentes às informações do registro M410 deverão ser preenchidas com os seguintes valores deste registro:

Natureza da Receita => Deve recuperar o conteúdo do campo 02 do registro M410.
Valor da Receita Bruta no Período   => Deve recuperar o conteúdo do campo 03 do registro M410.
Conta Analítica Contábil => Deve recuperar o conteúdo do campo 04 do registro M410.
Descrição Complementar da Natureza da Receita => Deve recuperar o conteúdo do campo 04 do registro M410.
Item Registros Vinculados à Natureza da Receita
Registro => Preencher com o número do registro gerado.
Base PIS => Deve recuperar campo Base PIS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M400.
Alíq. PIS => Deve recuperar o campo Alíquota PIS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M400.
Quant.Base PIS => Deve recuperar o campo Quant. Base PIS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M400.
Alíq. PIS em Reais => Deve recuperar o campo Alíq. PIS em Reais gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M400.
Valor PIS => Deve recuperar o campo Valor PIS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M400.
	OS3583		RN93	Sintético: Conteúdo das colunas do Relatório - Registro M800

As colunas referentes às informações do registro M400 deverão ser preenchidas com os seguintes valores deste registro:

CST => Deve recuperar o conteúdo do campo 02 do registro M800.
Valor Total da Receita Bruta => Deve recuperar o valor do campo 03 do registro M800
Conta Analítica Contábil=> Deve recuperar o valor do campo 04 do registro M800
Descrição Complementar da Natureza da Receita => Deve recuperar o valor do campo 05 do registro M800
	OS3583		RN94	Sintético: Conteúdo das colunas do Relatório – Registro M810
As colunas referentes às informações do registro M810 deverão ser preenchidas com os seguintes valores deste registro:

Natureza da Receita => Deve recuperar o conteúdo do campo 02 do registro M810.
Valor da Receita Bruta no Período   => Deve recuperar o conteúdo do campo 03 do registro M810.
Conta Analítica Contábil => Deve recuperar o conteúdo do campo 04 do registro M810.
 Descrição Complementar da Natureza da Receita => Deve recuperar o conteúdo do campo 04 do registro M810.
Item Registros Vinculados à Natureza da Receita
Registro => Preencher com o número do registro gerado.
Base COFINS => Deve recuperar campo Base COFINS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M800.
Alíq. COFINS => Deve recuperar o campo Alíquota COFINS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M800.
Quant.Base COFINS => Deve recuperar o campo Quant. Base COFINS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M800.
Alíq.COFINS em Reais => Deve recuperar o campo Alíq. COFINS em Reais gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M800.
Valor COFINS => Deve recuperar o campo Valor COFINS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M800.	OS3583		RN95	Relatório de Demonstrativo da Apuração por Tipo de Contribuição – Analítico
A quebra do relatório será por cod_registro + cod_contribuicao + CST + aliq_perc + aliq_quant 	OS3631		RN96	Relatório de Demonstrativo da Apuração por Tipo de Contribuição – Sintético
A quebra do relatório será por cod_registro + cod_contribuicao + CST + aliq_perc + aliq_quant
	OS3631		

RN97	[INCLUÍDA – OS4344] Relatório Demonstrativo da Apuração – por Tipo de Crédito (Analítico) 
Incluído a coluna ‘Razão Social ‘ entre as colunas “Participantes” e “Cfop” no arquivo em Excel no momento da exportação, (disponível na SAFX04).	

OS4344		


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN
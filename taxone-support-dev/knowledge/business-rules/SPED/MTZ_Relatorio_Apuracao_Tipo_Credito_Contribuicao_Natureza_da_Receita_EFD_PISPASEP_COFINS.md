# MTZ_Relatorio_Apuracao_Tipo_Credito_Contribuicao_Natureza da Receita_EFD_PISPASEP_COFINS

> Fonte: MTZ_Relatorio_Apuracao_Tipo_Credito_Contribuicao_Natureza da Receita_EFD_PISPASEP_COFINS.doc

THOMSON REUTERS

Relatório da Apuração (Crédito / Contribução / Natureza da Receita) - EFD PIS/PASEP-COFINS


Localização:
Módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições
Menus:  Relatórios ( Demonstrativo da Apuração (Crédito / Contribuição / Natureza da Receita)    


DOCUMENTO DE REQUISITO

OS/CH	Nome	Descrição		MFS-61786	Elisabete Costa	Inclusao da opção de menu “Relatórios ( Demonstrativo da Apuração (Crédito / Contribuição / Natureza da Receita)” para disponibilizar a geração dos relatórios analíticos/sintéticos em arquivo formato Excel.		


Sumário
 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc73448160" 1 - Relatório de Demonstrativo de Apuração por Tipo de Crédito	 PAGEREF _Toc73448160 \h 2
 HYPERLINK \l "_Toc73448161" 2 - Relatório de Demonstrativo de Apuração por Tipo de Contribuição	 PAGEREF _Toc73448161 \h 10
 HYPERLINK \l "_Toc73448162" 3 - Relatório de Demonstrativo da Apuração por Tipo de Natureza da Receita	 PAGEREF _Toc73448162 \h 22


1 - Relatório de Demonstrativo de Apuração por Tipo de Crédito


REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN00	Relatório de Demonstrativo da Apuração por Tipo de Crédito 

Pré-requisito:
É necessário realizar a Geração dos Registros disponíveis nas opções de menu Obrigações >> Geração dos Registros e Obrigações SCP >> Geração dos Registros, com o parâmetro “Demonstrativo da Apuração por Tipo de Crédito” selecionado.
 
Processamento 
Origem dos dados:
Informações dos registros M100, M105, M500 e M505 ( tabela interna que armazena os dados da apuração do Crédito do Período (registros M100, M105 e M500 e M505) calculados conforme regras descritas no documento “RNG - M100_105_110_500_505_510_V11.doc” a partir da geração dos registros. 

Informações dos Registros vinculados ao tipo de crédito ( tabela interna que armazena os dados das gerações dos registros do Bloco A, C, D e F.  

Critérios de recuperação dos dados para geração do relatório: Se no parâmetro ‘’Gerar Relatório Demonstrativo da Apuração no Período Informado’’ a opção ‘’Tipo de Crédito’’ estiver marcado na tela de Geração dos Registros 

		RN01	Layout do Relatório Demonstrativo da Apuração Tipo de Crédito   

Empresa	
Estabelecimento	
data_apuracao_ini
data_apuracao_fim	
registro_m100_m500	
registro_m105_m505	
registro_vinculado	
tipo_credito	
natureza_base_credito	
cst	

                             SEPARADOR DE BLOCO DE INFORMAÇÕES
base_credito	
aliq_pis_cofins	
qtd_base_pis_cofins	
aliq_pis_cofins_reais	
vlr_credito	
vlr_ajuste_acrescimo	
vlr_ajuste_reducao	
vlr_credito_diferido	
vlr_credito_disponivel	
vlr_credito_descontado	
saldo_creditos		

                           SEPARADOR DE BLOCO DE INFORMAÇÕES
base_pis_cofins	
parc_base_pis_cofins_cum	
vlr_total_base_credito	
vlr_base_credito	
qtd_total_base_pis_cofins	
parc_qtd_base_credito		

                          SEPARADOR DE BLOCO DE INFORMAÇÕES


base_pis_cofins	
aliq_pis_cofins	
qtd_base_pis_cofins	
aliq_pis_cofins_reais	
vlr_pis_cofins	
vlr_perc_rateio	
vlr_base_cofins_vinc_tipo_cred	
vlr_pis_vinc_tipo_credito
		RN02	O relatório Demonstrativo da Apuração por tipo de Crédito - Sintético será gerado com base nas seguintes regras:

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

Ordenação: 
Linhas dos Registros M100/M500 ( Deverá seguir a mesma ordenação gerada no meio magnético
Linhas dos Registros vinculado ao tipo de crédito ( Registro e Nat. Base Crédito
Linhas dos Registros M105/M505( Deverá seguir a mesma ordenação gerada no meio magnético.
   		RN03	Conteúdo das colunas do Relatório
DADOS CHAVE DO REGISTRO

Empresa: Exibir o código da empresa
Estabelecimento: Exibir o código do establecimento
Data_Apuracao_Ini: Exibir o período inicial
Data_Apuracao_fim: Exibir o período final
Registro_M100_M500: Exibir o registro M100 ou M500
Registro_M105_M505: Exibir o registro M105 ou M505
Registro_vinculado: -  Informações dos Registros vinculados ao tipo de crédito à tabela interna que armazena os dados das gerações dos registros do Bloco A, C, D e F.  
Tipo_credito: O relatório Demonstrativo da Apuração no Período por Tipo de Crédito deverá ser emitido de acordo com os filtros selecionados na Tela, localizada no módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições, menu: Relatórios ( Demonstrativo da Apuração (Crédito / Contribuição / Natureza da Receita)     
Natureza_base_credito: => recuperar o conteúdo do campo 02-Código da Base de Cálculo do Crédito apurado no período
CST: => recuperar o conteúdo do campo 03- CST PIS		RN04	Conteúdo das colunas do Relatório - Registro M100 (Registro Pai)

As colunas referentes às informações do registro M100 deverão ser preenchidas com os seguintes valores deste registro:

base_credito => Deve recuperar o valor do campo 02- Valor da Base de Cálculo do Crédito. 
aliq_pis_cofins => Deve recuperar o valor do campo 03- Alíquota do PIS/PASEP (em Percentual).
qtd_base_pis_cofins => recuperar o valor do campo 04- Quantidade Total da Base de Cálculo do Crédito apurado em Unidade de Medida de Produto
aliq_pis_cofins_reais => Recuperar com o valor do campo 05- Alíquota do PIS (em reais).
vlr_credito => recuperar o valor do campo 06- Valor total do crédito apurado no período.
vlr_ajuste_acrescimo => recuperar o valor do campo 07- Valor total dos ajustes de acréscimo.
vlr_ajuste_reducao => recuperar o valor do campo 08-Valor total dos ajustes de redução.
vlr_credito_diferido => recuperar o valor do campo 09- Valor total do crédito diferido no período.
vlr_credito_disponivel =>recuperar o valor do campo 10- Valor Total do Crédito Disponível relativo ao Período.
vlr_credito_descontado=> recuperar o valor do campo 11 - Valor do Crédito disponível, a descontar, da contribuição apurada no próprio período.  
saldo_creditos => recuperar o valor do campo 12- Saldo de créditos a utilizar em períodos futuros. 
		RN05	Conteúdo das colunas do Relatório – Registro M105 (Registro Filho)
As colunas referentes às informações do registro M105 deverão ser preenchidas com os seguintes valores deste registro:

base_pis_cofins => recuperar o valor do campo 02- Valor Total da Base de Cálculo escriturada nos documentos e operações.   
parc_base_pis_cofins_cum => recuperar o valor do campo 03- Parcela do Valor Total da Base de Cálculo informada vinculada a receitas com incidência cumulativa.
vlr_total_base_credito => recuperar o valor do campo 04- Valor Total da Base de Cálculo do Crédito, vinculada as receitas com incidência não-cumulativa
vlr_base_credito => recuperar o valor do campo 05- Valor da Base de Cálculo do Crédito, vinculada ao tipo de Crédito escriturado em M100.  
qtd_total_base_pis_cofins => recuperar o valor do campo 06- Quantidade Total da Base de Cálculo do Crédito apurado em Unidade de Medida de Produto
parc_qtd_base_credito => recuperar o valor do campo 07.
		RN06	Colunas referentes aos Registros Vinculados ao Tipo de Crédito no Relatório Sintético 
As colunas referentes aos Registros Vinculados ao Tipo de Crédito PIS/PASEP no relatório analítico serão as seguintes:
base_pis_cofins
aliq_pis_cofins
qtd_base_pis_cofins
aliq_pis_cofins_reais
vlr_pis_cofins
vlr_perc_rateio
vlr_baser_pis_vinc_tipo_cred
vlr_pis_vinc_tipo_credito
		RN07	Conteúdo da Coluna
base_pis_cofins => Deve recuperar o Valor da Base de Cálculo do Crédito gerado no registro que compôs o tipo de crédito. 
		RN08	Conteúdo da Coluna:
aliq_pis_cofins => Deve recuperar o valor da Alíquota PIS em percentual gerada no registro que compôs o tipo de crédito. 
		RN09	Conteúdo da Coluna:
qtd_base_pis_cofins => Deve recuperar o valor da Quantidade Base PIS gerada no registro que compôs o tipo de crédito.
		RN10	Conteúdo da Coluna:
aliq_pis_cofins_reais => Deve recuperar o valor da Alíquota PIS - em reais gerada no registro que compôs o Tipo de crédito
		RN11	Conteúdo da Coluna:
vlr_pis_cofins => Deve recuperar o Valor PIS gerado no registro que compôs o tipo de crédito.   
  		RN12	Conteúdo da Coluna:
vlr_perc_rateio => Nesta coluna deve ser recuperar o percentual do rateio calculado no registro M105.
		RN13	Conteúdo da Coluna:
vlr_baser_pis_vinc_tipo_cred => Deve preencher com o resultado do valor da coluna Base PIS multiplicado pelo o valor da coluna Percentual do Rateio do registro M105.  		RN14	Conteúdo da Coluna:
vlr_pis_vinc_tipo_credito => Deve preencher com o resultado do valor da coluna Valor PIS multiplicado pelo o valor da coluna Percentual do Rateio do registro M100..
		RN15	Conteúdo das colunas do Relatório - Registro M500: (Registro Pai)

As colunas referentes às informações do registro M500 deverão ser preenchidas com os seguintes valores deste registro:

base_credito => Deve recuperar o valor do campo 02- Valor da Base de Cálculo do Crédito. Se neste campo não houver informação, preencher com o conteúdo do campo 06- Quantidade – Base de cálculo COFINS
aliq_pis_cofins => Deve recuperar o valor do campo 03- Alíquota da COFINS (em Percentual). Se neste campo não houver informação, deve preencher com o valor do campo 07- Alíquota da COFINS (em reais).
qtd_base_pis_cofins => recuperar o valor do campo 04- Quantidade Total da Base de Cálculo do Crédito apurado em Unidade de Medida de Produto
aliq_pis_cofins_reais => recuperar o valor do campo 05- aliquota do COFINS em reais
vlr_credito => recuperar o valor do campo 06- Valor total do crédito apurado no período
vlr_ajuste_acrescimo => recuperar o valor do campo 07- Valor total dos ajustes de acréscimo
vlr_ajuste_reducao => recuperar o valor do campo 08-Valor total dos ajustes de redução
vlr_credito_diferido => recuperar o valor do campo 09- Valor total do crédito diferido no período
vlr_credito_disponivel =>recuperar o valor do campo 10- Valor Total do Crédito Disponível relativo ao Período
vlr_credito_descontado => recuperar o valor do campo 11 - Valor do Crédito disponível, a descontar, da contribuição apurada no próprio período. 
saldo_creditos => recuperar o valor do campo 12- Saldo de créditos a utilizar em períodos futuros
		RN16	Conteúdo das colunas do Relatório – Registro M505 – (Registro Filho)
As colunas referentes às informações do registro M505 deverão ser preenchidas com os seguintes valores deste registro:

base_pis_cofins => recuperar o valor do campo 02- Valor Total da Base de Cálculo escriturada nos documentos e operações.   
parc_base_pis_cofins_cum => recuperar o valor do campo 03- Parcela do Valor Total da Base de Cálculo informada vinculada a receitas com incidência cumulativa.
vlr_total_base_credito => recuperar o valor do campo 04- Valor Total da Base de Cálculo do Crédito, vinculada as receitas com incidência não-cumulativa
vlr_base_credito => recuperar o valor do campo 05- Valor da Base de Cálculo do Crédito, vinculada ao tipo de Crédito escriturado em M100.  
qtd_total_base_pis_cofins => recuperar o valor do campo 06- Quantidade Total da Base de Cálculo do Crédito apurado em Unidade de Medida de Produto
parc_qtd_base_credito => recuperar o valor do campo 07 - Parcela da base de cálculo do crédito em quantidade (campo 08) vinculada ao tipo de crédito escriturado em M500.

		RN17	Colunas referentes aos Registros Vinculados ao Tipo de Crédito da COFINS no Relatório Sintético
As colunas referentes aos Registros Vinculados ao Tipo de Crédito no relatório sintético serão os seguintes:
base_pis_cofins
aliq_pis_cofins
qtd._base_pis_cofins
aliq_pis_cofins_reais
vlr_pis_cofins
vlr_perc_rateio
vlr_baser_pis_vinc_tipo_cred
vlr_pis_vinc_tipo_credito
		RN18	Conteúdo da Coluna
Base_pis_cofins => Deve ser preenchida com Valor da Base de Cálculo do Crédito gerado no registro que compôs o tipo de crédito. Se neste campo não houver informação, preencher com o conteúdo do campo Quantidade – Base de cálculo COFINS.
		RN19	Conteúdo da Coluna:
aliq_pis_cofins => Deve ser preenchida com Alíquota COFINS gerada no registro que compôs o tipo de crédito. 
		RN20	Conteúdo da Coluna
qtd_base_pis_cofins=> Deve ser recuperado o valor da Quantidade Base COFINS gerada no registro que compôs o tipo de crédito. 		RN21	Conteúdo da Coluna
Aliq_pis_cofins_reais => Deve ser recuperado o valor da Alíquota COFINS em reais gerada no registro que compôs o tipo de crédito
		RN22	Conteúdo da Coluna:
Vlr_pis_cofins => Deve ser preenchido com o Valor COFINS gerado no registro que compôs o tipo de crédito.  
   		RN23	Conteúdo da Coluna:
vlr_perc_rateio => Nesta coluna deve ser recuperar o percentual do rateio calculado no registro M505.
		RN24	Conteúdo da Coluna:
 vlr_baser_pis_vinc_tipo_cred => Deve preencher com o resultado do valor da coluna Base COFINS multiplicado pelo o valor da coluna Percentual do Rateio  do registro M505. 
		RN25	Conteúdo da Coluna:
vlr_pis_vinc_tipo_credito => Deve preencher com o resultado do valor da coluna Valor COFINS multiplicado pelo o valor da coluna Percentual do Rateio do registro M500. 		2 - Relatório de Demonstrativo de Apuração por Tipo de Contribuição


REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN26	

Relatório de Demonstrativo da Apuração por Tipo de Contribuição

Pré-requisito:
É necessário realizar a Geração dos Registros disponíveis nas opções de menu Obrigações >> Geração dos Registros e Obrigações SCP >> Geração dos Registros, com o parâmetro “Demonstrativo da Apuração por Tipo de Contribuição” selecionado.

 Processamento 
Origem dos dados:

Informações dos registros M200, M210, M600 e M610 ( tabela interna que armazena os dados da apuração da Contribuição do Período (registros M200, M210 e M600 e M610) calculados conforme regras descritas no documento “RNG- M200_210_211_600_610_611_v11.doc” a partir da geração dos registros. 

Informações dos Registros vinculados ao tipo de contribuição ( tabela interna que armazena os dados das gerações dos registros do Bloco A, C, D e F.  

Critérios de recuperação dos dados para geração do relatório: Se no parâmetro ‘’Gerar Relatório Demonstrativo da Apuração no Período Informado a opção ‘’Tipo de Contribuição’’ estiver marcado na tela de Geração dos Registros. 


		RN27	Layout do Relatório Demonstrativo da Apuração Tipo de Contribuição   

Empresa	
Estabelecimento	
data_apuracao_ini
data_apuracao_fim	
registro_m200_m600	
registro_m210_m610	
registro_vinculado	
tipo_contribuicao	
cst	

                             SEPARADOR DE BLOCO DE INFORMAÇÕES

vlr_tot_contrib_n_cum_per	
vlr_tot_cred_desc_per	
vlr_tot_cred_desc_per_ant
vlr_tot_contrib_n_cum_devida
vlr_ret_fonte_deduzida_per
vlr_outras_deducoes_per
vlr_tot_contrib_n_cum_rec_pag
vlr_tot_contrib_cum_per
vlr_ret_fonte_ded_per
vlr_outras_ded_per
vlr_tot_contrib_n_cum_a_rec_pag
vlr_tot_contrib_a_rec_pag


                          SEPARADOR DE BLOCO DE INFORMAÇÕES


vlr_receita_bruta	
vlr_base_calculo	
aliq_pis_cofins_perc	
qtd_base_pis_cofins	
aliq_pis_cofins_reais
vlr_tot_contrib
vlr_tot_ajt_acres
vlr_tot_ajt_reducao
vlr_tot_contrib_difer_per
vlr_tot_contrib_difer_per_ant
vlr_tot_contrib_per
vlr_tot_ajt_acres_bc_contrib
vlr_tot_ajt_red_bc_contrib
vlr_bc_contrib_apos_ajt		

                          SEPARADOR DE BLOCO DE INFORMAÇÕES
vlr_item	
vlr_tot_docto	
vlr_venda_bruta
vlr_operacao
vlr_tot_receita
vl_bc_pis_cofins
aliq_pis_cofins
quant_bc_pis_cofins
aliq_pis_cofins_quant
vl_pis_cofins
		Relatório Demonstrativo da Apuração por Tipo de Contribuição

Se na tela de Emissão do Relatório por Tipo de Contribuição somente a opção ‘’M200’’ do campo Registro estiver marcado:
  Listar as informações de cada documento fiscal gerado nos registros A100/A170, C100/C170, C180/C181, C380/C381, C405/C481, C490/C491, C600/C601, D200/D201, D300, D350, D600/D601, F100, F200 que compôs todos os tipos de contribuição, ou seja, considerar todos os registros associados aos registros M210, conforme segue:

REGISTRO M200
   < REGISTROS VINCULADOS AOS REGISTROS M210>

Nesta forma de emissão a totalização dos registros deverá ser feita, demonstrando a totalização de todos os registros vinculados de todos os registros M210.

 Se na tela de Emissão do Relatório por Tipo de Contribuição somente a opção ‘’M200’ e ‘’M210’’ do campo Registro estiver marcado:
    Listar o registro M200, em seguida será listado os registros M210 pertencentes ao registro M200 e seus registros vinculados, conforme demonstrado a seguir

REGISTRO M200
      REGISTRO M210
    <REGISTROS VINCULADOS AO REGISTRO M210 >
      REGISTRO M200
    <REGISTROS VINCULADOS AO REGISTRO M210 >

Nesta forma de emissão a totalização dos registros deverá ser feita para cada quebra realizada no relatório, ou seja, deverá ser feita a cada listagem de registros vinculados pertencente ao um registro M210.

Se na tela de Emissão do Relatório por Tipo de Contribuição somente a opção ‘’M600’’ do campo Registro estiver marcado:
  Listar as informações de cada documento fiscal gerado nos registro A100/A170, C100/C170, C180/C185, C380/C385, C405/C485, C490/C495, C600/C605, D200/D205, D300, D350, D600/D605, F100, F200 que compôs todos os tipos de contribuição, ou seja, considerar todos os registros associados aos registros M210, conforme segue:

REGISTRO M600
   < REGISTROS VINCULADOS AOS REGISTROS M610>


		RN28	
Nesta forma de emissão a totalização dos registros deverá ser feita, demonstrando a totalização de todos os registros vinculados de todos os registros M610.

Se na tela de Emissão do Relatório por Tipo de Contribuição somente a opção ‘’M600’ e ‘’M610’’ do campo Registro estiver marcado:
    Listar o registro M600, em seguida será listado os registros M610 pertencentes ao registro M600 e seus registros vinculados, conforme demonstrado a seguir

REGISTRO M600
      REGISTRO M610
    <REGISTROS VINCULADOS AO REGISTRO M610 >
      REGISTRO M600
    <REGISTROS VINCULADOS AO REGISTRO M610 >

Nesta forma de emissão a totalização dos registros  deverá ser feita para cada quebra realizada no relatório, ou seja, deverá ser feita a cada listagem de registros vinculados pertencente ao um registro M610.

Ordenação: 
Linhas dos Registros M200/M600 ( Deverá seguir a mesma ordenação gerada no meio magnético.
Linhas dos Registros vinculado ao tipo de contribuição ( registro + Nº Documento, CFOP e Nat. Base Crédito.
Linhas dos Registros M210/M610( Deverá seguir a mesma ordenação gerada no meio magnético.

		RN29	Conteúdo das colunas do Relatório
DADOS CHAVE DO REGISTRO

Empresa: Exibir o código da empresa
Estabelecimento: Exibir o código do establecimento
Data_Apuracao_Ini: Exibir o período inicial
Data_Apuracao_fim: Exibir o período final
Registro_M200_M600: Exibir o registro M200 ou M600
Registro_M210_M610: Exibir o registro M210 ou M610
Registro_vinculado: -  Informações dos Registros vinculados ao tipo de crédito à tabela interna que armazena os dados das gerações dos registros do Bloco A, C, D e F.  
Natureza_base_credito: => recuperar o conteúdo do campo 02-Código da Base de Cálculo do Crédito apurado no período
CST: => recuperar o conteúdo do campo 03- CST PIS
		RN30	
Conteúdo das colunas do Relatório (Analítico e Sintético) - Registro M200 (Registro Pai)

As colunas referentes às informações do registro M200 deverão ser preenchidas com os seguintes valores deste registro:

vlr_tot_contrib_n_cum_per => recuperar o valor do campo 02- Valor Total da Contribuição Não Cumulativo no Período
vlr_tot_cred_desc_per => recuperar o valor do campo 03- Valor Total do Crédito Descontado, Apurado no Próprio Período da Escrituração
vlr_tot_cred_desc_per_ant => recuperar o valor do campo 04- Valor Total do Crédito Descontado, Apurado em Período da Apuração Anterior
 vlr_tot_contrib_n_cum_devida =>recuperar o valor do campo 05- Valor Total da Contribuição Não Cumulativa Devida.   
 vlr_ret_fonte_deduzida_per => recuperar o valor do campo 06- Valor Retido na Fonte Deduzido no Período     
 vlr_outras_deducoes_per =>recuperar o valor do campo 07- Outras Deduções no Período  
 vlr_tot_contrib_n_cum_rec_pag =>recuperar o valor do campo 08- Valor da Contribuição Não Cumulativa a Recolher/Pagar
 vlr_tot_contrib_cum_per  =>recuperar o valor do campo 09- Valor Total da Contribuição Cumulativa do Período 
 vlr_ret_fonte_ded_per=>recuperar o valor do campo 10- Valor Retido na Fonte Deduzido no Período 
 vlr_outras_ded_per => recuperar o valor do campo 11-Outras Deduções no Período      
 vlr_tot_contrib_n_cum_a_rec_pag => recuperar  o valor do campo 12- Valor da Contribuição a Recolher/Pagar no Período
 vlr_tot_contrib_a_rec_pag => recuperar o valor do campo 13- Valor Total da Contribuição a Recolher/Pagar no Período
                                                                                                        		RN31	Conteúdo das colunas do Relatório (Analítico e Sintético) - Registro M210 (Registro Filho)

As colunas referentes às informações do registro M210 deverão ser preenchidas com os seguintes valores deste registro:

vlr_receita-bruta =>recuperar o valor do campo 03- Valor da Receita Bruta
vlr_base_calculo => recuperar o valor do campo 04-Valor da Base de Cálculo da Contribuição
aliq_pis_cofins_perc => recuperar o valor do campo 05- Alíquota do PIS/PASEP (em percentual)    
qtd_base_pis_cofins => recuperar o valor do campo 06- Quantidade – Base de cálculo PIS  
aliq_pis_cofins_reais => recuperar o valor do campo 07- Alíquota do PIS (em reais) 
vlr_tot_contrib => recuperar o valor do campo 08- Valor total da contribuição social apurada       
vlr_tot_ajt_acres => recuperar o valor do campo 09- Valor total dos ajustes de acréscimo  
vlr_tot_ajt_reducao => recuperar o valor do campo 10- Valor total dos ajustes de redução    
vlr_tot_contrib_difer_per => recuperar o valor do campo 11- Valor total da contribuição a diferir no período     
vlr_tot_contrib_difer_per_ant => recuperar o valor do campo 12- Valor da contribuição diferida em períodos anteriores   
vlr_tot_contrib_per => recuperar o valor do campo 13- Valor Total da Contribuição do Período                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
vlr_tot_ajt_acres_bc_contrib => recuperaro valor do campo 13-Valor Total dos ajustes e acréscimos da base de cálculo do valor da contribuiçao. 
vlr_tot_ajt_red_bc_contrib => recuperaro valor do campo 14-Valor Total dos ajustes e redução da base de cálculo do valor da contribução.
vlr_bc_contrib_apos_ajt => recuperaro valor do campo 15-Valor da base de cálculo do valor da contribuição após ajustes.                                                                                                                                                                                                                                                                                                                                                                     
		RN32	Colunas referentes aos Registros Vinculados ao Tipo de Contribuição PIS/PASEP - (Relatório Sintético) 

As colunas referentes aos Registros Vinculados ao Tipo de Crédito no relatório sintético serão os seguintes:

vlr_item
vlr_tot_docto
vlr_venda_bruta
vlr_operacao
vlr_tot_receita
vlr_bc_pis_cofins
aliq_pis_cofins
quant_bc_pis_cofins
aliq_pis_cofins_quant
vl_pis_cofins

		RN33	Conteúdo da Coluna:
vlr_item => Deve recuperar o valor quando registro for A170, C170, C185, C381, C481, C491, C601, D201 e D601 ser preenchido.		RN34	Conteúdo da Coluna:
vlr_tot_docto => Deve recuperar o valor do campo do registro D300. Esse campo não deve ser preenchido para os demais registros		RN35	Conteúdo da Coluna:
vlr_venda_bruta => Deve recuperar o valor do campo do registro D350. Esse campo não deve ser preenchido para os demais registros      		RN36	Conteúdo da Coluna
vlr_operacao => Deve recuperar o valor do campo do registro F100. Esse campo não deve ser preenchido para os demais registros		RN37	Conteúdo da Coluna
vlr_tot_receita => Deve recuperar o valor do campo. Esse campo não deve ser preenchido para os demais registros.      
		RN38	Conteúdo da Coluna:
vl_bc_pis_cofins => Deve recuperar o valor do campo do registro que compôs o tipo de contribuição. 		RN39	aliq_pis_cofins => Deve recuperar o valor do campo do registro que compôs o tipo de contribuição. 		RN40	quant_bc_pis_cofins => Deve recuperar o valor do campo do registro que compôs o tipo de contribuição		RN41	aliq_pis_cofins_quant => Deve recuperar o valor do campo do registro que compôs o tipo de contribuição.
		RN42	Conteúdo da Coluna:
vl_pis_cofins => Deve recuperar o valor do campo VL_PIS gerado no registro que compôs o tipo de contribuição.		RN43	
Conteúdo das colunas do Relatório (Analítico e Sintético) - Registro M600 (Registro Pai)

As colunas referentes às informações do registro M600 deverão ser preenchidas com os seguintes valores deste registro:

vlr_tot_contrib_n_cum_per => recuperar o valor do campo 02- Valor Total da Contribuição Não Cumulativo no Período
vlr_tot_cred_desc_per => recuperar o valor do campo 03- Valor Total do Crédito Descontado, Apurado no Próprio Período da Escrituração
vlr_tot_cred_desc_per_ant => recuperar o valor do campo 04- Valor Total do Crédito Descontado, Apurado em Período da Apuração Anterior
 vlr_tot_contrib_n_cum_devida =>recuperar o valor do campo 05- Valor Total da Contribuição Não Cumulativa Devida.   
 vlr_ret_fonte_deduzida_per => recuperar o valor do campo 06- Valor Retido na Fonte Deduzido no Período     
 vlr_outras_deducoes_per =>recuperar o valor do campo 07- Outras Deduções no Período  
 vlr_tot_contrib_n_cum_rec_pag =>recuperar o valor do campo 08- Valor da Contribuição Não Cumulativa a Recolher/Pagar
 vlr_tot_contrib_cum_per  =>recuperar o valor do campo 09- Valor Total da Contribuição Cumulativa do Período 
 vlr_ret_fonte_ded_per=>recuperar o valor do campo 10- Valor Retido na Fonte Deduzido no Período 
 vlr_outras_ded_per => recuperar o valor do campo 11-Outras Deduções no Período      
 vlr_tot_contrib_n_cum_a_rec_pag => recuperar  o valor do campo 12- Valor da Contribuição a Recolher/Pagar no Período
 vlr_tot_contrib_a_rec_pag => recuperar o valor do campo 13- Valor Total da Contribuição a Recolher/Pagar no Período
                                                                                                        		RN44	Conteúdo das colunas do Relatório (Analítico e Sintético) - Registro M610 (Registro Filho)

As colunas referentes às informações do registro M610 deverão ser preenchidas com os seguintes valores deste registro:

vlr_receita-bruta =>recuperar o valor do campo 02- Valor da Receita Bruta
vlr_base_calculo => recuperar o valor do campo 03-Valor da Base de Cálculo da Contribuição
aliq_pis_cofins_perc => recuperar o valor do campo 04- Alíquota do PIS/PASEP (em percentual)    
qtd_base_pis_cofins => recuperar o valor do campo 05- Quantidade – Base de cálculo PIS  
aliq_pis_cofins_reais => recuperar o valor do campo 06- Alíquota do PIS (em reais) 
vlr_tot_contrib => recuperar o valor do campo 07- Valor total da contribuição social apurada       
vlr_tot_ajt_acres => recuperar o valor do campo 08- Valor total dos ajustes de acréscimo  
vlr_tot_ajt_reducao => recuperar o valor do campo 09- Valor total dos ajustes de redução    
vlr_tot_contrib_difer_per => recuperar o valor do campo 10- Valor total da contribuição a diferir no período     
vlr_tot_contrib_difer_per_ant => recuperar o valor do campo 11- Valor da contribuição diferida em períodos anteriores   
vlr_tot_contrib_per => recuperar o valor do campo 12- Valor Total da Contribuição do Período                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
vlr_tot_ajt_acres_bc_contrib => recuperaro valor do campo 13-Valor Total dos ajustes e acréscimos da base de cálculo do valor da contribuiçao. 
vlr_tot_ajt_red_bc_contrib => recuperaro valor do campo 14-Valor Total dos ajustes e redução da base de cálculo do valor da contribução.
vlr_bc_contrib_apos_ajt => recuperaro valor do campo 15-Valor da base de cálculo do valor da contribuição após ajustes. 


                                                                                                                                                                                                                                                                                                                                                                      
		RN45	Colunas referentes aos Registros Vinculados ao Tipo de Contribuição COFINS - Relatório Sintético

As colunas referentes aos Registros Vinculados ao Tipo de Contribuição no relatório sintético serão os seguintes: 

vlr_item
vlr_tot_docto
vlr_venda_bruta
vlr_operacao
vlr_tot_receita
vlr_bc_pis_cofins
aliq_pis_cofins
quant_bc_pis_cofins
aliq_pis_cofins_quant
vl_pis_cofins

		RN46	Conteúdo da Coluna:
vlr_item => Deve recuperar o valor do campo quando registro for A170, C170, C185, C385, C485, C495, C605, D205 e D605. Para os demais registros esse campo não deve ser preenchido.
		RN47	Conteúdo da Coluna:
vlr_tot_docto => Deve recuperar o valor do campo do registro D300. Esse campo não deve ser preenchido para os demais registros
		RN48	Conteúdo da Coluna:
vlr_venda_bruta => Deve recuperar o valor do campo do registro D350. Esse campo não deve ser preenchido para os demais registros   
		RN49	Conteúdo da Coluna
vlr_operacao => Deve recuperar o valor do campo do registro F100. Esse campo não deve ser preenchido para os demais registros
		RN50	Conteúdo da Coluna
vlr_tot_receita => Deve recuperar o valor do campo do registro F200 que compôs o tipo de contribuição. Esse campo não deve ser preenchido para os demais registros.   
		RN51	Conteúdo da Coluna:
vlr_bc_pis_cofins => Deve recuperar o valor do campo do registro que compôs o tipo de contribuição. 		RN52	Conteúdo da Coluna:
aliq_pis_cofins => Deve recuperar o valor do campo gerada no registro que compôs o tipo de contribuição. 		RN53	Conteúdo da Coluna:
quant_bc_pis_cofins => Deve recuperar o valor do campo que compôs o tipo de contribuição. 		RN54	Conteúdo da Coluna:
aliq_pis_cofins_quant => Deve recuperar o valor do campo no registro que compôs o tipo de contribuição.		RN55	Conteúdo da Coluna:
vl_pis_cofins => Deve recuperar o valor do campo gerado no registro que compôs o tipo de contribuição.		


3 - Relatório de Demonstrativo da Apuração por Tipo de Natureza da Receita

REGRAS DE NEGÓCIO

CÓD.	DESCRIÇÃO	DR		

RN56	Relatório de Demonstrativo da Apuração por Tipo de Natureza da Receita

Pré-requisito:
É necessário realizar a Geração dos Registros disponíveis nas opções de menu Obrigações >> Geração dos Registros e Obrigações SCP >> Geração dos Registros, com o parâmetro “Demonstrativo da Apuração por Tipo de Natureza da Receita” selecionado.

 Processamento 
Origem dos dados:
Informações dos registros M400, M410, M800 e M810 ( tabela interna que armazena os dados dos registros M400, M410,M800 e M810) calculados conforme regras descritas no documento “RNG - M400_M410_M800_M810_v7.doc” a partir da geração dos registros. 

Informações dos Registros vinculados ( tabela interna que armazena os dados das gerações dos registros do Bloco A, C, D e F.  

Critérios de recuperação dos dados para geração do relatório: Se no parâmetro ‘’Gerar Relatório Demonstrativo da Apuração no Período Informado’’ a opção ‘’Tipo de Natureza da Receita’’ estiver marcado na tela de Geração dos Registros 

Ordenação: 
Linhas dos Registros M400/M800 ( Deverá ser ordenado por CST (ordem crescente)
Linhas dos Registros M410/M810( Deverá ser ordenado por Código da Natureza da Receita + Registro 

		RN57	Layout do Relatório Demonstrativo da Apuração Tipo Natureza de Receita   


Empresa	
Estabelecimento	
data_apuracao_ini
data_apuracao_fim	
registro_m400_m800	
registro_m410_m810	
registro_vinculado	
natureza_receita	
cst	

                             SEPARADOR DE BLOCO DE INFORMAÇÕES
vlr_tot_receita_brt
conta_analitica	
desc_compl_nat_rec

                          SEPARADOR DE BLOCO DE INFORMAÇÕES

vlr_receita_brt_per	
conta_analitica	
desc_compl_nat_rec	
		

                          SEPARADOR DE BLOCO DE INFORMAÇÕES

vl_bc_pis_cofins
aliq_pis_cofins
quant_bc_pis_cofins
aliq_pis_cofins_quant
vl_pis_cofins
		RN57	O relatório Demonstrativo da Apuração por tipo de Natureza da Receita - Sintético será gerado com base nas seguintes regras:

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
		RN58	Conteúdo das colunas do Relatório
DADOS CHAVE DO REGISTRO

Empresa: Exibir o código da empresa
Estabelecimento: Exibir o código do establecimento
Data_Apuracao_Ini: Exibir o período inicial
Data_Apuracao_fim: Exibir o período final
Registro_M400_M800: Exibir o registro M400 ou M800
Registro_M410_M810: Exibir o registro M410 ou M810
Registro_vinculado: -  Informações dos Registros vinculados ao tipo de crédito à tabela interna que armazena os dados das gerações dos registros do Bloco A, C, D e F.  
Natureza_base_credito: => recuperar o conteúdo do campo 02-Código da Base de Cálculo do Crédito apurado no período
CST: => recuperar o conteúdo do campo 03- CST PIS
		RN59	Conteúdo das colunas do Relatório (Analítico e Sintético)  - Registro M400 (Registro Pai)

As colunas referentes às informações do registro M400 deverão ser preenchidas com os seguintes valores deste registro:

vlr_tot_receita_brt => Deve recuperar o valor do campo 02 do registro M400
conta_analitica => Deve recuperar o valor do campo 03 do registro M400
desc_compl_nat_rec => Deve recuperar o valor do campo 04 do registro M400
		RN60	Conteúdo das colunas do Relatório (Analítico e Sintético)  – Registro M410 (Registro Filho)

As colunas referentes às informações do registro M410 deverão ser preenchidas com os seguintes valores deste registro:

vlr_receita_brt_per => Deve recuperar o conteúdo do campo 02 do registro M410.
conta_analitica => Deve recuperar o conteúdo do campo 03 do registro M410.
desc_compl_nat_rec => Deve recuperar o conteúdo do campo 04 do registro M410.
vlr_bc_pis_cofins => Deve recuperar campo Base PIS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M400.
aliq_pis_cofins => Deve recuperar o campo Alíquota PIS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M400.
quant_bc_pis_cofins => Deve recuperar o campo Quant. Base PIS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M400.
aliq_pis_cofins_quant => Deve recuperar o campo Alíq. PIS em Reais gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M400.
vl_pis_cofins => Deve recuperar o campo Valor PIS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M400.		RN61	Conteúdo das colunas do Relatório (Analítico e Sintético) - Registro M800 (Registro Pai)

As colunas referentes às informações do registro M800 deverão ser preenchidas com os seguintes valores deste registro:

vlr_tot_receita_brt => Deve recuperar o valor do campo 02 do registro M800
conta_analitica => Deve recuperar o valor do campo 03 do registro M800
desc_compl_nat_rec => Deve recuperar o valor do campo 04 do registro M800
		RN62	Conteúdo das colunas do Relatório (Analítico e Sintético)  – Registro M810 (Registro Filho)

As colunas referentes às informações do registro M810 deverão ser preenchidas com os seguintes valores deste registro:

vlr_receita_brt_per => Deve recuperar o conteúdo do campo 02 do registro M810.
conta_analitica => Deve recuperar o conteúdo do campo 03 do registro M810.
desc_compl_nat_rec => Deve recuperar o conteúdo do campo 04 do registro M810.
vl_bc_pis_cofins => Deve recuperar campo Base COFINS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M800.
aliq_pis_cofins => Deve recuperar o campo Alíquota COFINS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M800.
quant_bc_pis_cofins => Deve recuperar o campo Quant. Base COFINS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M800.
aliq_pis_cofins_quant => Deve recuperar o campo Alíq. COFINS em Reais gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M800.
vl_pis_cofins => Deve recuperar o campo Valor COFINS gerado no registro C170, C181, C381, C481, C491, C601, D201, D601 D300, D350, F100, F200 que compôs a geração do Registro M800.		
Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN
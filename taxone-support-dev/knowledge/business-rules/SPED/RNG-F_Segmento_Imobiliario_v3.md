# RNG-F_Segmento_Imobiliario_v3

> Fonte: RNG-F_Segmento_Imobiliario_v3.doc

Registro F200 – Operações da Atividade Imobiliária - Unidade Imobiliária Vendida
RNG-F200
	Gerar um registro F200 para cada registro gravado na tabela SAFX150 no período:

Competência: (campo 05 da SAFX150)
     Entre a data inicial e final geração do arquivo. 

[OS4316-A] Tratamento para Geração de SCPs

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados (considerando a regra padrão de seleção) e que não tenham o campo Código do SCP preenchido.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados (considerando a regra padrão de seleção) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento (considerando a regra padrão de seleção) e que não tenham o campo Código do SCP preenchido.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento (considerando a regra padrão de seleção) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração.

[OS4316-C] Observar a parametrização de "Dados Iniciais" (menu: Parâmetros >> Dados Iniciais) para geração ou não do registro. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo (Código da SCP não informada) como valido também para a SCP para o qual o arquivo está sendo gerado.

Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido.
		RNF200-02	Campo IND_OPER:

Gravar o contéudo do campo “05- Indicador do Tipo de operação ” da tabela SAFX149  que está relacionada ao movimento na tabela SAFX150. 		RNF200-03	Campo UNID_IMOB:

Neste campo deve gravar o conteúdo do campo 05- Indicador do Tipo da Unidade Imobiliária da tabela SAFX2054 referente ao código da unidade imobiliária (campo 03) informada na tabela SAFX150.		RNF200-04	Campo IDENT_EMP:

Neste campo deve gravar o conteúdo do campo 06- Identificação/Nome do Empreendimento da tabela SAFX2054 referente ao código da unidade imobiliária (campo 03) informada na tabela SAFX150. 		RNF200-05	Campo DESC_UNID_IMOB:
Neste campo deve gravar o conteúdo do campo 07- Descrição resumida da unidade imobiliária da tabela SAFX2054 referente ao código da unidade imobiliária (campo 03) informada na tabela SAFX150.
		RNF200-06	Campo NUM_CONT:
Gravar o contéudo do campo “06- Número de Contrato ” da tabela SAFX149  que está relacionada ao movimento na tabela SAFX150.
		RNF200-07	Campo CPF_CNPJ_ADQU:

Esta informação deve ser gerada a partir do campo 07“ Indicador da Pessoa Fis/Jur Adquirente” e o campo  08 ‘’Código da Pessoa Fis/Jur Adquirente’’ na SAFX149.
Buscar o CNPJ na SAFX04 a partir da pessoa fis/jur. informada. 
		RNF200-08	Campo DT_OPER:
Gravar o conteúdo do campo 04- Data da Operação da venda da unidade imobiliária da tabela SAFX149 que está relacionada ao movimento na tabela SAFX150.
		RNF200-20	Campo PERC_REC_RECEB:

Gravar o conteúdo do campo Percentual da receita total recebida até o mês, da unidade imobiliária vendida da tabela X150.

[ALTERADA – CH23678_2015]
Tratamento:
Quando houver erro no cálculo do percentual emitir a seguinte mensagem no log:
“Mensagem: Erro ao calcular o Percentual da receita total recebida até o mês (F200). Dados do Registro: (Informar Empresa, Estabelecimento, Data Operação, CPF/CNPJ e Contrato).”
Não interromper o processo.
		RNF200-21	Campo IND_NAT_EMP:

Neste campo deve gravar o conteúdo do campo 08- Indicador da natureza específica do empreendimento da tabela SAFX2054 referente ao código da unidade imobiliária (campo 03) informada na tabela SAFX150.
		
Registro F205 – Custo Incorrido da Unidade Imobiliária
RNGF205	Neste registro deverão ser gravadas as informações de custo incorrido da unidade imobiliária da SAFX151 associadas à unidade imobiliária gravada no registro F200 que atenda o critério abaixo.

Competência: (campo 05 da SAFX151)
     Entre a data inicial e final geração do arquivo

[ALTERADA – CH846_2016]
Os valores não devem ser arredondados e o que for gravado na tabela da SAFX151 deverá gerar no arquivo magnético no seu respectivo campo, de acordo com o DExPARA: DEPARA EFD CONTRIBUICOES_BLOCOP_LUCRO_REAL_LUCRO_PRESUMIDO.xlsx; localizado em \MsafDW\documentacao funcional\EFD-PISCOFINS.
		RNF205-02	Campo: VL_CUS_INC_ACUM_ANT

Gravar o conteúdo do campo Valor total do custo Incorrido acumulado até mês anterior ao da escrituração da tabela X151.
		RNF205-03	Campo: VL_CUS_INC_PER_ESC

Gravar o conteúdo do campo Valor Total do Custo Incorrido da unidade imobiliária no mês da escrituração da tabela X151.
		RNF205-04	Campo: VL_CUS_INC_ACUM

Gravar o conteúdo do campo Valor Total do Custo Incorrido da unidade imobiliária acumulado até o mês da escrituração da tabela X151.
Esse campo corresponde à soma dos campos 02 e 03 (campo calculado automaticamente pelo Mastersaf).
		RNF205-05	Campo: VL_EXC_BC_CUS_INC_ACUM

Gravar o conteúdo do campo Parcela do custo incorrido sem direito ao crédito acumulado até período da tabela X151.
		RNF205-06	Campo: VL_BC_CUS_INC

Gravar o conteúdo do campo Valor da Base de Cálculo do Crédito sobre o Custo Incorrido, acumulado até o período da escrituração da tabela X151.

Esse campo corresponde à subtração dos campos 04 e 05 (campo calculado automaticamente pelo Mastersaf, mas também possui importação).
		RNF205-07	Campo: CST_PIS

Gravar o conteúdo do campo Código da Situação Tributária – PIS da tabela X151.
		RNF205-08	Campo: ALIQ_PIS

Gravar o conteúdo do campo Alíquota – PIS da tabela X151.
		RNF205-09	Campo: VL_CRED_PIS_ACUM

Gravar o conteúdo do campo Valor total do crédito acumulado sobre o custo incorrido - PIS/PASEP da tabela X151.

Esse campo corresponde à multiplicação dos campos 06 e 08 (campo calculado automaticamente pelo Mastersaf, mas também possui importação).
		RNF205-10	Campo: VL_CRED_PIS_DESC_ANT

Gravar o conteúdo do campo Parcela do crédito descontada até o período anterior da escrituração – PIS/PASEP da tabela X151.
		RNF205-11	Campo: VL_CRED_PIS_DESC

Gravar o conteúdo do campo Parcela a descontar no período da escrituração – PIS/PASEP da tabela X151.
		RNF205-12	Campo: VL_CRED_PIS_DESC_FUT 

Gravar o conteúdo do campo Parcela a descontar em períodos futuros – PIS/PASEP da tabela X151.
Esse campo corresponde à subtração dos campos 09, 10 e 11 (campo calculado automaticamente pelo Mastersaf).
		RNF205-13	Campo: CST_COFINS

Gravar o conteúdo do campo Código da Situação Tributária – COFINS da tabela X151.		RNF205-14	Campo: ALIQ_COFINS

Gravar o conteúdo do campo Alíquota – Cofins da tabela X151.		RNF205-15	Campo: VL_CRED_COFINS_ACUM

Gravar o conteúdo do campo Valor total do crédito acumulado sobre o custo incorrido – COFINS da tabela X151.
Esse campo corresponde à multiplicação dos campos 06 e 14 (campo calculado automaticamente pelo Mastersaf, mas também possui importação).
		RNF205-16	Campo: VL_CRED_COFINS_DESC_ANT

Gravar o conteúdo do campo Parcela do crédito descontada até o período anterior da escrituração – COFINS da tabela X151.		RNF205-17	Campo: VL_CRED_COFINS_DESC

Gravar o conteúdo do campo Parcela a descontar no período da escrituração – COFINS da tabela X151.		RNF205-18	Campo: VL_CRED_COFINS_DESC_FUT

Gravar o conteúdo do campo Parcela a descontar em períodos futuros – COFINS da tabela X151.
Esse campo corresponde à subtração dos campos 15, 16 e 17 (campo calculado automaticamente pelo Mastersaf).
		
Registro F210 – Custo Orçado da Unidade Imobiliária Vendida
RNGF205	Neste registro deverão ser gravadas as informações de custo orçado da unidade imobiliária da SAFX152 associadas à unidade imobiliária gravada no registro F200 que atenda ao critério abaixo.

Competência: (campo 05 da SAFX152)
     Entre a data inicial e final geração do arquivo
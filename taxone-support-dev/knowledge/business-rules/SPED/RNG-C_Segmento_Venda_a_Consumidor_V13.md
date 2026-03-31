# RNG-C_Segmento_Venda_a_Consumidor_V13

> Fonte: RNG-C_Segmento_Venda_a_Consumidor_V13.doc

Regras de Recuperação para os registros do bloco C:
REGISTRO C380: NOTA FISCAL DE VENDA A CONSUMIDOR (CÓDIGO 02) - CONSOLIDAÇÃO DE DOCUMENTOS EMITIDOS 
RNG-C380	
Este registro deve ser apresentado pelos contribuintes que utilizam notas fiscais de venda ao consumidor quando não emitidas por ECF. 

OBS: Não deverão existir notas fiscais sem itens na base de dados do cliente quando for gerado este conjunto de registros (C380, C381 e C385).
Gerar um registro para cada grupo* de notas fiscais (SAFX07) que atendam os critérios abaixo:

Movimento Entrada/Saída: (campo 03 da SAFX07)
		Igual a “9 – Documento de Saída”

Seleção Documentos/Operações Geradoras de Receita: (parâmetro nos dados iniciais da obrigação)
                            SE for igual ‘’Data de Lançamento PIS/COFINS’’ (campo 196 da SAFX08 / campo 81 da SAFX09)
                                                Entre a Data Inicial e Data Final de geração do arquivo
                           SENÃO (igual ‘’Data de Emissão’’)   
                                               Data de Emissão: (campo 11 da SAFX07)
		        Entre a Data Inicial e Data Final de geração do arquivo

Classificação: (campo “12 – Classificação do Documento” da SAFX07)
		Igual a “1 – Mercadoria”  e Se o parâmetro Notas Fiscais de Mercadoria Não Escrituradas estiver marcado em Dados Iniciais, as notas fiscais de saída com Classificação ‘7 – Notas Fiscais de Mercadoria não Escrituradas’, (campo 12 da safx07) e que possuam CST´s de PIS e COFINS (SAFX07 ou 08), deverão ser considerados na EFD-Contribuições.


Modelo: (campo “13 – Modelo de Documento” da SAFX07)
		Igual a “02”
                                 
Crédito/Contribuição Extemporânea: * (campo novo da SAFX08)
		Somente documentos não extemporâneos (campo novo = “N”)

CFOP (ou CFOP+Natureza) (campos 22 e 23 da SAFX08)
		Relacionado no parâmetro “CFOP x Tipo de Operação” com tipo de
		operação igual a “Geradora de Receita”

* Se qualquer um dos itens da NF atender às regras de geração desse registro, então a NF deve ser gerada.

** O agrupamento das notas fiscais a serem geradas nesse registro deve ser feito com base na data de emissão desses documentos.


OBS3: Validação do Registro C300 pelo PVA: não podem ser informados dois ou mais registros com a mesma combinação de valores dos campos DT_DOC_INI, DT_DOC_FIN, NUM_DOC_INI e NUM_DOC_FIN. Não é permitida a intersecção (sobreposição) de intervalos entre os registros C380 informados com a mesma combinação de valores dos campos _DOC_INI, DT_DOC_FIN, NUM_DOC_INI e NUM_DOC_FIN.
[OS4316-A] Tratamento para Geração de SCPs

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados (considerando a regra padrão de seleção) e que não tenham o campo Código do SCP preenchido.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados (considerando a regra padrão de seleção) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento (considerando a regra padrão de seleção) e que não tenham o campo Código do SCP preenchido.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento (considerando a regra padrão de seleção) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração.
[OS4316-C] Observar a parametrização de "Dados Iniciais" (menu: Parâmetros >> Dados Iniciais) para geração ou não do registro. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo (Código da SCP não informada) como valido também para a SCP para o qual o arquivo está sendo gerado.
Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido.		RNC380-03	Campo: DT_DOC_INI
Este campo deve ser preenchido com a data de emissão do primeiro documento fiscal agrupado neste de registro.		mRNC380-04	Campo: DT_DOC_FIN
Este campo deve ser preenchido com a data de emissão do último documento fiscal agrupado neste registro.		RNC380-05	Campo: NUM_DOC_INI
De acordo com a regra RNG-C380, gravar neste campo o número do primeiro documento fiscal emitido no dia (campo: 08/SAFX07). 		RNC380-06	Campo: NUM_DOC_FIN
De acordo com a regra RNG-C380, gravar neste campo o número do último documento fiscal emitido no dia (campo: 08/SAFX07).		RNC380-07	Campo VL_DOC:

Este campo deve ser preenchido com o somatório do valor contábil dos itens (campo: 64/SAFX08) das notas fiscais agrupadas, que não estejam canceladas. 
Caso a NF seja cancelada (campo 04 – SITUACAO = “S” da SAFX07) esse campo não deverá considerar os valores dos documentos cancelados, somente dos documentos normais. Nesse caso, deverá ser informado |0|.		RNC380-08	Campo: VL_DOC_CANC:
Este campo deve ser preenchido com o somatório do valor contábil dos itens (campo: 64/SAFX08) das notas fiscais agrupadas, que estejam canceladas (campo 04 – SITUACAO = “S” da SAFX07).
Caso a NF não seja cancelada (campo 04 – SITUACAO diferente “S” da SAFX07), então neste campo deverá ser informado zero |0|. 		
REGISTRO C381: DETALHAMENTO DA CONSOLIDAÇÃO – PIS/PASEP

RNG-C381	Consolidar as informações dos itens dos documentos fiscais gerados no registro C380 com base nas seguintes informações:

- Código de Situação Tributária PIS
- Código do Item
- Alíquota do PIS (ou Alíquota do PIS em reais)
- Conta Contábil

Este registro é filho do C380, para cada registro C380 pode ocorrer 1 ou vários registros C381.
No caso de ocorrência de venda com CST’s distintos, deve ser gerado um registro para cada CST. 

Obs.: Os itens dos documentos fiscais cancelados, os itens que não passaram pela regra de geração do registro C380 e os itens que não possuírem informação de CST PIS/Cofins, não devem ser considerados no agrupamento.
		RNC381-03	Campo: COD_ITEM
Este campo deve ser preenchido com o código do item das notas fiscais agrupadas no C380.
Se parâmetro ‘Considerar o Indicador no Código do Item’, na tela de Dados Iniciais estiver marcado:
OBS1: Observar regra de gravação do código do item no registro 0200 (concatenar indicador + código do item conforme regra de gravação do COD_ITEM).
Se parâmetro ‘Considerar o Indicador no Código do Item’, na tela de Dados Iniciais estiver desmarcado:
OBS: Observar regra de gravação do código do item no registro 0200 ( código do item )		

REGISTRO C385: DETALHAMENTO DA CONSOLIDAÇÃO – COFINS 
RNG-C385	Consolidar as informações dos itens dos documentos fiscais gerados no registro C380 com base nas seguintes informações:

- Código de Situação Tributária Cofins
- Código do Item
- Alíquota da Cofins (ou Alíquota da COFINS em reais)
- Conta Contábil

Este registro é filho do C380, para cada registro C380 pode ocorrer 1 ou vários registros C385.
No caso de ocorrência de venda com CST’s distintos, deve ser gerado um registro para cada CST. 

Obs.: Os itens dos documentos fiscais cancelados, os itens que não passaram pela regra de geração do registro C380 e os itens que não possuírem informação de CST PIS/Cofins, não devem ser considerados no agrupamento.
		RNC385-03	Campo: COD_ITEM
Se parâmetro ‘Considerar o Indicador no Código do Item’, na tela de Dados Iniciais estiver marcado:
Este campo deve ser preenchido com o indicador+código do item das notas fiscais agrupadas no C380.
OBS1: Observar regra de gravação do código do item no registro 0200 (concatenar indicador + código do item conforme regra de gravação do COD_ITEM).

Se parâmetro ‘Considerar o Indicador no Código do Item’, na tela de Dados Iniciais estiver desmarcado:
OBS: Observar regra de gravação do código do item no registro 0200 ( código do item )

		

REGISTRO C395: NOTAS FISCAIS DE VENDA A CONSUMIDOR (CÓDIGOS 02, 2D, 2E, 59, 60 e 65) – AQUISIÇÕES/ENTRADAS COM CRÉDITO
RNG-C395	Este registro deve ser apresentado pelos contribuintes que utilizam notas fiscais de venda ao consumidor quando não emitidas por ECF. No Registro C395 a pessoa jurídica poderá escriturar eventuais aquisições com direito a crédito (aquisição de bens a serem utilizados como insumos, por exemplo) cuja operação esteja documentada por nota fiscal de venda a consumidor.

OBS: Não deverá existir notas fiscais sem itens na base de dados do cliente quando for gerado este conjunto de registros (C395 e C396).

Normal ou Devolução: (campo 04 da SAFX07 = “1 – Normal”)

Movimento Entrada/Saída: (campo 03 da SAFX07)
		Diferente de “9” - Documento de Saída”

Classificação: (campo “12 – Classificação do Documento” da SAFX07)
		Igual a “1 – Mercadoria” 

Modelo: (campo “13 – Modelo de Documento” da SAFX07)
		Igual a “02”, “2D”, “2E”, “59”, “60” ou “65”
	
Situação: (campo “30 – Situação da Nota” da SAFX07)
		Somente documentos não cancelados (Situação = “N”) 

Crédito/Contribuição Extemporânea: (campo novo da SAFX08)
		Somente documentos não extemporâneos (campo novo = “N”)

Não serão consideradas NFs sem item.

[ALTERAÇÃO – CH28382 / CH6594/2015 / OS4816]
Data de Lançamento PIS/COFINS: o campo Data do Lançamento (campo 247 - DAT_LANC_PIS_COFINS da SAFX07 ou campo 196 - DAT_LANC_PIS_COFINS da SAFX08)* deve estar preenchido com uma data que esteja entre a Data Inicial e Data Final de geração do arquivo.

* Para recuperação das notas de entrada considerar o informado no parâmetro “Registro A100, C100, C190, C395, C500, D100 e D500 - Seleção das Operações Geradoras de Crédito / Considerar para filtro da Data de Lançamento do EFD PIS/COFINS” disponível na tela de Dados Iniciais.

Se no parâmetro indicado for preenchida a opção “Capa NF”, serão selecionados os registros considerando como critério a Data de Lançamento informada na SAFX07.

Se no parâmetro indicado for preenchida a opção “Item NF”, serão selecionados os registros considerando como critério a Data de Lançamento informada na SAFX08. Neste caso, se for identificada alguma NF cuja data não tenha sido preenchida na SAFX08, mas esteja preenchida na SAFX07 e esteja no período, também deve ser considerada.

Observação: Quando houver o preenchimento da data de lançamento na capa e no item da nota fiscal com períodos distintos não haverá tratamento pelo sistema, não pode haver lançamento na capa nesse caso, apenas no item, ou seja, será aceito na geração apenas conteúdo VAZIO ou IGUAL, se houver preenchimento o sistema considerará e a geração estará incorreta, por esse motivo essa orientação será feita ao usuário no manual de layout de importação dos documentos fiscais e no manual operacional.
Exemplo: Data do Lançamento PIS/COFINS 15/07/2013 / Período de Geração: JUL/2013 – Neste exemplo a nota será gerada.

SE parâmetro Gera NF’s de Entrada sem Crédito = “Não” (parâmetro da tela de geração), considerar apenas registros cujo CST PIS ou CST COFINS (campos 175 e 178 da SAFX08, campos 68 e 69 da SAFX09 ou campos 249 e 250 da SAFX07) estejam preenchidos com conteúdo igual a 50, 51, 52, 53, 54, 55, 56, 60, 61, 62, 63, 64, 65, 66 ou 67. Senão, considerar todos os CSTs.
 
[OS4316-A] Tratamento para Geração de SCPs

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados (considerando a regra padrão de seleção) e que não tenham o campo Código do SCP preenchido.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados (considerando a regra padrão de seleção) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento (considerando a regra padrão de seleção) e que não tenham o campo Código do SCP preenchido.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento (considerando a regra padrão de seleção) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração.
[OS4316-C] Observar a parametrização de "Dados Iniciais" (menu: Parâmetros >> Dados Iniciais) para geração ou não do registro. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo (Código da SCP não informada) como valido também para a SCP para o qual o arquivo está sendo gerado.
Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido.		RNG-C395-02	Campo COD_PART
[OS4751] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais estiver selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador (IND_FIS_JUR) com o Código da PFJ (COD_FIS_JUR), considerando a formatação: Indicador + "-" + Código.
Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais NÃO estiver selecionado, este campo será gerado apenas com o Código da PFJ (COD_FIS_JUR).
Para o código aqui informado, será demonstrado o Cadastro no registro 0150.
		
REGISTRO C396: ITENS DO DOCUMENTO (CÓDIGOS 02, 2D, 2E, 59, 60 e 65) – AQUISIÇÕES/ENTRADAS COM CRÉDITO
RNG-C396	Deve ser gerado um registro para cada item constante na nota fiscal de venda a consumidor relacionada no registro C395.


Obs.: Os itens dos documentos fiscais cancelados, os itens que não passaram pela regra de geração do registro C380 e os itens que não possuírem informação de CST PIS/Cofins, não devem ser considerados.
		RNC396-02	Campo: COD_ITEM

Se parâmetro ‘Considerar o Indicador no Código do Item’, na tela de Dados Iniciais estiver marcado:
Este campo deve ser preenchido com o indicador+código do item das notas fiscais agrupadas no C395.
Se parâmetro ‘Considerar o Indicador no Código do Item’, na tela de Dados Iniciais estiver desmarcado:
Este campo deve ser preenchido com o código do item das notas fiscais agrupadas no C395.
		RNC396-05	Campo: NAT_BC_CRED

Se o parâmetro “Considerar a Natureza da Base de Crédito a partir dos Documentos” estiver marcado (nos dados iniciais):
Gravar o conteúdo do campo Natureza da Base de Crédito (campo novo/SAFX08) informada no documento fiscal.   

Se o parâmetro “Considerar a Natureza da Base de Crédito a partir dos Documentos” estiver desmarcado (nos dados iniciais):
Gravar o código da natureza da base de crédito que consta na parametrização feita no menu: Parâmetros > Identificador da Nat. da Base de Crédito (por CFOP e por CFOP/Natureza), de acordo com o CFOP (campo 14 da 22 da SAFX08) informado no documento fiscal. 


Incluir crítica no log do processo:
Origem:
O novo campo Natureza da Base de Crédito na SAFX08 esteja sem preenchimento e o parâmetro ‘‘Considerar a Natureza da Base de Crédito a partir dos Documentos” esteja  marcado nos dados iniciais’’

Mensagem:
O campo NAT_BC_CRED é de preenchimento obrigatório, quando o parâmetro ’’Considerar a Natureza da Base de Crédito a partir dos Documentos” esteja  marcado nos dados iniciais’’
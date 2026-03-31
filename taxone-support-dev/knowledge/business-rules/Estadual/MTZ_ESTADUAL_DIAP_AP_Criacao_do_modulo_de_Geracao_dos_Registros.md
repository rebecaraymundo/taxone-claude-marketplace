# MTZ_ESTADUAL_DIAP_AP_Criacao_do_modulo_de_Geraçao_dos_Registros

> Fonte: MTZ_ESTADUAL_DIAP_AP_Criacao_do_modulo_de_Geraçao_dos_Registros.doc

DIAP AP


DOCUMENTO DE REQUISITO

DR	Nome	Descrição		OS2456	DIAP AP	Regras para Geração do Meio Magnético.		OS2456-A	DIAP AP	Complementação Novo Produto.		OS4286	Ajuste da geração DIAP Mensal e DIAP AP – ANUAL	Geração separada dos registros conforme DIAP Mensal e DIAP Anual.		CH28364_2014	Ajuste da geração DIAP Mensal e DIAP AP – ANUAL	Este documento tem como objetivo ajustar a geração dos campos N° de Funcionários Inicial e N° de Funcionários Final da DIAP Mensal e DIAP AP – ANUAL.		CH28354_2014	Ajuste da geração DIAP Mensal	Este documento tem como objetivo alterar os campos 56-Valor do Detalhamento Recolhido ou a recolher no prazo legal para a coluna Normal/Estimativa/Simples e 71-Valor do Detalhamento Imposto total a recolher/Normal para a coluna Normal/Estimativa/Simples.		
      OBS: Quando não houver informação para determinado tipo de registro, não há a necessidade de informá-lo mesmo zerado.


REGRAS DE NEGÓCIO
Arquivo geral da declaração
RN00	Regra geral para recuperação das informações:

Buscar as informações dentro do período preenchido na tela de geração desde que:
Se campo de período da tela “Informações Iniciais da Declaração” for mensal, considerar o campo mês e ano para geração;
 OU 
Se o campo de período da tela “Informações Iniciais da Declaração” for anual, considerar o campo ano para geração (ignorando o campo mês/ano informado e buscar o ano todo informado).

Somente executar a geração do arquivo magnético quando a tela “Informações Iniciais da Declaração” for preenchida com o período inserido na tela de geração, caso contrário emitir uma mensagem de log “Falta Cadastrar informações para geração DIAP-AP em Declaração -> Informações Iniciais da Declaração.”	OS4286		RN01	DIAPPR (identificação da tabela principal da DIAP Eletronica)

Preencher fixo “DIAPPR”	OS2456		RN02	Inscrição Estadual com máscara
Preencher  com o número da Inscrição Estadual referente ao estabelecimento selecionado na geração. Ex.Formato: 99.999999-9	OS2456	11	C	Inscrição Estadual com máscara	Mascara 99.999999-9		RN03	Motivo

Preencher com “1”. Completar com zero à esquerda.
	OS2456	2	C	Motivo	Preencher com zero a esquerda, tabela basica DIAPMOT		RN04	Seqüência Geral do DIAP para o Contribuinte

Preencher com zero à esquerda.	OS2456		RN05	Sequencia Parcial para DIAP

Preencher om zero à esquerda.		RN06	Tipo da DIAP
Preencher com “1” quando na tela de geração estiver flegada a opção “Original”
Preencher com “2” quando na tela de geração estiver flegada a opção “Retificadora”

Completar com zero à esquerda. 		RN07	Periodicidade da DIAP
Preencher com “1”.
Completar com zero à esquerda.

[ALTERADA – OS4286]
Tratamento:
Preencher com “1” completando com zeros à esquerda quando na tela de geração for selecionada a opção Periodicidade: MENSAL. Os registros a serem considerados para essa periodicidade são todos que foram especificados menos os registros DIAPUE (identificação para a tabela de Entradas da UF) e o DIAPUS (identificação para a tabela de Saídas da UF) que servem apenas para período anual (tratamento a seguir).

Preencher com “3” completando com zeros à esquerda quando na tela de geração for selecionada a opção Periodicidade: ANUAL. Os registros a serem considerados para essa periodicidade são DIAPPR (identificação da tabela principal da DIAP Eletronica) diferenciado*, DIAPUE (identificação para a tabela de Entradas da UF) e o DIAPUS (identificação para a tabela de Saídas da UF), os outros registros não devem ser considerados.
*Considerar os seguintes campos para o registro DIAPPR de periodicidade ANUAL:
DIAPPR 
Inscrição Estadual com máscara
Motivo
Sequencia Geral do DIAP para o Contribuinte
Sequencia Parcial para DIAP
Tipo da DIAP
Periodicidade da DIAP
Periodo Inicial 
Periodo Final
Municipio de Origem 
Municipio de Destino
N° de Funcionários Inicial
N° de Funcionários Final
Valor da Disponibilidade de Caixa Inicial
Valor da Disponibilidade de Caixa Final
Houve Movimentação de Entrada/Saída? 
Houve Redução de Base de Cálculo? 
Houve Operações Interestaduais?	OS2456
OS4286		RN08	Periodo Inicial 
Preencher com a data inicial do conteúdo digitado na tela de geração no formato EX: aaaammdd	OS2456		RN09	Periodo Final
Preencher com a data final do conteúdo digitado na tela de geração no formato EX: aaaammdd	OS2456		RN10	Municipio de Origem 

Para notas de saída preencher o código do município do estabelecimento declarante – para recuperar a máscara do código verificar a tabela de parâmetros do menu Parâmetros > Municípios IBGE x Município DIAP

Para notas de entrada preencher o código do município da pessoa Fis/Jur da tabela safx04 – para recuperar a máscara do código verificar a tabela de parâmetros do menu Parâmetros > Municípios IBGE x Município DIAP

	OS2456		RN11	Municipio de Destino

Para notas de saída preencher o código do município da pessoa Fis/Jur da tabela safx04 – para recuperar a máscara do código verificar a tabela de parâmetros do menu Parâmetros > Municípios IBGE x Município DIAP

Para notas de entrada preencher o código do município do estabelecimento declarante – para recuperar a máscara do código verificar a tabela de parâmetros do menu Parâmetros > Municípios IBGE x Município DIAP

	OS2456		RN12	N° de Funcionários Inicial

[ALTERADA – CH28364_2014]
Preencher com valor digitado pelo usuário na tela de manutenção. Vide docto MTZ - ESTADUAL - DIAP AP - Criação de Tela Informações Iniciais da Declaração.doc

Origem:
Estadual >> DIAP-AP >> Declaração >> Informações Iniciais da Declaração.

Tratamento:
Preencher de acordo com o conteúdo preenchido no campo Nr. Inicial do item Funcionários do Período;
Completar com zeros a esquerda;
Quando o campo não estiver preenchido, preencher com zeros.
	OS2456
CH28364_2014		RN13	N° de Funcionários Final

[ALTERADA – CH28364_2014]
Preencher com valor digitado pelo usuário na tela de manutenção. Vide docto MTZ - ESTADUAL - DIAP AP - Criação de Tela Informações Iniciais da Declaração.doc

Origem:
Estadual >> DIAP-AP >> Declaração >> Informações Iniciais da Declaração.

Tratamento:
Preencher de acordo com o conteúdo preenchido no campo Nr. Final do item Funcionários do Período;
Completar com zeros a esquerda;
Quando o campo não estiver preenchido, preencher com zeros.
	OS2456
CH28364_2014		RN14	Valor da Disponibilidade de Caixa Inicial
Preencher com valor digitado pelo usuário na tela de manutenção. Vide docto MTZ - ESTADUAL - DIAP AP - Criação de Tela Informações Iniciais da Declaração.doc	OS2456		RN15	Valor da Disponibilidade de Caixa Final
Preencher com valor digitado pelo usuário na tela de manutenção. Vide docto MTZ - ESTADUAL - DIAP AP - Criação de Tela Informações Iniciais da Declaração.doc	OS2456		RN16	Houve Movimentação de Entrada/Saída? 

Preencher  com S> caso o flag da tela de geração dos dados acessórios esteja ativado.
Preencher  com N> caso o flag da tela de geração dos dados acessórios não esteja ativado.
Vide docto MTZ - ESTADUAL - DIAP AP - Criação de Tela Informações Iniciais da Declaração.doc
	OS2456		RN17	Houve Redução de Base de Cálculo? 


Preencher com S> caso o flag da tela de geração dos dados acessórios esteja ativado.
Preencher com N> caso o flag da tela de geração dos dados acessórios não esteja ativado.

Vide docto MTZ - ESTADUAL - DIAP AP - Criação de Tela Informações Iniciais da Declaração.doc
	OS2456		RN18	Houve Operações Interestaduais? 


Preencher  com S> caso o flag da tela de geração dos dados acessórios esteja ativado.
Preencher  com N> caso o flag da tela de geração dos dados acessórios não esteja ativado.
	OS2456		RN19	Valor do Estoque Inicial de Matéria Prima e Outros Insumos para a coluna Tributação Normal
Este campo não será atendido nesta OS.
Preencher com zeros.

	OS2456		RN20	Valor do Estoque Inicial de Matéria Prima e Outros Insumos para a coluna Isentas

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN21	Valor do Estoque Inicial de Matéria Prima e Outros Insumos para a coluna Outros

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN22	Valor do Estoque Inicial de Mercadoria para Revenda para a coluna de Tributação Normal

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN23	Valor do Estoque Inicial de Mercadoria para Revenda para a coluna de Isentas

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN24	Valor do Estoque Inicial de Mercadoria para Revenda para a coluna de Outras

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN25	Valor do Estoque Inicial de Produtos de Fabricação Própria (Acabados) para a coluna Tributação Normal

Este campo não será atendido nesta OS.
Preencher com zeros.

	OS2456		RN26	Valor do Estoque Inicial de Produtos de Fabricação Própria (Acabados) para a coluna Isentas


Para Este campo não será atendido nesta OS.
Preencher com zeros.


	OS2456		RN27	Valor do Estoque Inicial de Produtos de Fabricação Própria (Acabados) para a coluna de Outras


Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN28	Valor do Estoque Inicial de Produtos de Fabricação Própria (em elaboração) para a coluna Tributação Normal

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN29	Valor do Estoque Inicial de Produtos de Fabricação Própria (em elaboração) para a coluna Isentas


Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN30	Valor do Estoque Inicial de Produtos de Fabricação Própria (em elaboração) para a coluna de Outras

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN31	Valor do Estoque Inicial de Materiais de Uso e Consumo para a coluna Outras

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN32	Valor do Estoque Inicial de Bens do ativo imobilizado para a coluna Outras

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN33	Valor do Estoque Inicial de Estoque de Terceiros para a coluna Outras

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN34	Valor do Estoque Final de Matéria Prima e Outros Insumos para a coluna Tributação Normal

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN35	Valor do Estoque Final de Matéria Prima e Outros Insumos para a coluna Isentas

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN36	Valor do Estoque Final de Matéria Prima e Outros Insumos para a coluna Outras

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN37	Valor do Estoque Final de Mercadoria para Revenda para a coluna Tributação Normal

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN38	Valor do Estoque Final de Mercadoria para Revenda para a coluna Isentas

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN39	Valor do Estoque Final de Mercadoria para Revenda para a coluna Outras

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN40	Valor do Estoque Final de Produtos de Fabricação Própria (Acabados) para a coluna Tributação Normal

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN41	Valor do Estoque Final de Produtos de Fabricação Própria (Acabados) para a coluna Isentas

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN42	Valor do Estoque Final de Produtos de Fabricação Própria (Acabados) para a coluna Outras

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN43	Valor do Estoque Final de Produtos de Fabricação Própria (em elaboração) para a coluna Tributação Normal

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN44	Valor do Estoque Final de Produtos de Fabricação Própria (em elaboração) para a coluna Isentas

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN45	Valor do Estoque Final de Produtos de Fabricação Própria (em elaboração) para a coluna Outras

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN46	Valor do Estoque Final de Materiais de Uso e Consumo para a coluna Outras

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN47	Valor do Estoque Final de Bens do ativo imobilizado para a coluna Outras

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN48	Valor do Estoque Final de Estoque de Terceiros para a coluna Outras

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN49	Valor dos Débitos pelas Saídas


Preencher neste campo o valor contábil total correspondente ao livro de apuração do ICMS modelo P9 – módulo ICMS referente às saídas (CFOPs iniciados com 5,6 e 7)	OS2456		RN50	Valor de Outros Débitos

Preencher neste campo o valor do campo “outros débitos” total correspondente ao livro de apuração do ICMS modelo P9 – módulo ICMS .	OS2456		RN51	Valor de Estorno de Créditos


Preencher neste campo o valor do campo “estorno de créditos” total correspondente ao livro de apuração do ICMS modelo P9 – módulo ICMS .	OS2456		RN52	Valor de Crédito pelas Entradas

Preencher neste campo o valor contábil total correspondente ao livro de apuração do ICMS modelo P9 – módulo ICMS referente às entradas (CFOPs iniciados com 1,2 e 3 )	OS2456		RN53	Valor de Outros Créditos


Preencher neste campo o valor do campo “estorno de créditos” total correspondente ao livro de apuração do ICMS modelo P9 – módulo ICMS .	OS2456		RN54	Valor de Estorno de Débitos

Preencher neste campo o valor do campo “estorno de débitos” total correspondente ao livro de apuração do ICMS modelo P9 – módulo ICMS .	OS2456		RN55	Valor do Saldo Credor do Período Anterior

Preencher neste campo o valor do campo “saldo credor do período anterior” total correspondente ao livro de apuração do ICMS modelo P9 – módulo ICMS .
	OS2456		RN56	Valor do Detalhamento Recolhido ou a recolher no prazo legal para a coluna Normal/Estimativa/Simples

[ALTERADA – CH28354_2014]
Preencher com zeros. Este campo será preenchido automaticamente pelo sistema da DIAP.
Preencher com o valor do campo “011-Saldo Devedor (Débito menos Crédito)” total da apuração do saldo correspondente ao livro de apuração do ICMS modelo P9 – módulo ICMS.
	OS2456
CH28354_2014		RN57	Valor do Detalhamento Recolhido ou a recolher no prazo legal para a coluna Importação

Preencher com zeros.	OS2456		RN58	Valor do Detalhamento Recolhido ou a recolher no prazo legal para a coluna Diferencial de Aliquota Imobilizado

Preencher com zeros.	OS2456		RN59	Valor do Detalhamento Recolhido fora do prazo para a coluna Normal/Estimativa/Simples

Preencher com zeros.
	OS2456		RN60	Valor do Detalhamento Recolhido fora do prazo para a coluna Importação
Preencher com zeros.
	OS2456		RN61	Valor do Detalhamento Recolhido fora do prazo para a coluna Diferencial de Aliquota Imobilizado

Preencher com zeros.
	OS2456		RN62	Valor do Detalhamento Vencido e não recolhido para a coluna Normal/Estimativa/Simples

Preencher com zeros.
	OS2456		RN63	Valor do Detalhamento Vencido e não recolhido para a coluna Importação

Preencher com zeros.
	OS2456		RN64	Valor do Detalhamento Vencido e não recolhido para a coluna Diferencial de Aliquota Imobilizado

Preencher com zeros.
	OS2456		RN65	Valor do Detalhamento Benefício Fiscal para a coluna Normal/Estimativa/Simples

Preencher com zeros.
	OS2456		RN66	Valor do Detalhamento Benefício Fiscal para a coluna Importação

Preencher com zeros.
	OS2456		RN67	Valor do Detalhamento Benefício Fiscal para a coluna Diferencial de Aliquota Imobilizado

Preencher com zeros.
	OS2456		RN68	Valor do Detalhamento Estimativas pagas no Período para a coluna Normal/Estimativa/Simples
Preencher com zeros.
	OS2456		RN69	Valor do Detalhamento Imposto total a recolher/Estimativa para a coluna Normal/Estimativa/Simples

Preencher com zeros.
	OS2456		RN70	Campo Vago	OS2456		RN71	Valor do Detalhamento Imposto total a recolher/Normal para a coluna Normal/Estimativa/Simples

[ALTERADA – CH28354_2014]
Preencher com zeros.
Preencher com o valor do campo “013-Imposto a Recolher” total da apuração do saldo correspondente ao livro de apuração do ICMS modelo P9 – módulo ICMS.
	OS2456
CH28354_2014		RN72	Valor do Detalhamento Imposto total a recolher/Simples para a coluna Normal/Estimativa/Simples

Preencher com zeros.
	OS2456		RN73	Valor do Detalhamento Recolhido ou a recolher no prazo legal para a coluna ICMS Diferencial de Aliquota Material de Consumo

Preencher com zeros.
	OS2456		RN74	Valor do Detalhamento Recolhido ou a recolher no prazo legal para a coluna ICMS Substituição Tributária

Preencher com zeros.
	OS2456		RN75	Valor do Detalhamento Recolhido fora do prazo para a coluna ICMS Diferencial de Aliquota Material de Consumo

Preencher com zeros.
	OS2456		RN76	Valor do Detalhamento Recolhido fora do prazo para a coluna ICMS Substituição Tributária

Preencher com zeros.
	OS2456		RN77	Valor do Detalhamento Vencido e não recolhido para a coluna de ICMS Diferencial de Aliquota Material de Consumo
Preencher com zeros.
	OS2456		RN78	Valor do Detalhamento Vencido e não recolhido para a coluna de ICMS Substituição Tributária

Preencher com zeros.
	OS2456		RN79	GIA-ST Valor do Produto da coluna Substituição do Estado
Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN80	GIA-ST Valor IPI da coluna Substituição do Estado

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN81	GIA-ST Valor Despesas Acessórias da coluna Substituição do Estado

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN82	GIA-ST Valor da Base de Cálculo do ICMS próprio da coluna Substituição do Estado
Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN83	GIA-ST Valor do ICMS próprio da coluna Substituição do Estado

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN84	GIA-ST Valor da Base de Cálculo do ICMS - Substituição Tributária da coluna Substituição do Estado

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN85	GIA-ST Valor do ICMS retido por Substituição Tributária da coluna Substituiçao do Estado

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN86	GIA-ST Valor ICMS Devoluções de Mercadorias da coluna Substituição do Estado

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN87	GIA-ST Valor ICMS Ressarcimentos apropriados da coluna Substituição do Estado
Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN88	GIA-ST Valor Crédito do período anterior da coluna Substituição do Estado

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN89	GIA-ST Valor Crédito para o período seguinte da coluna Substituição do Estado
Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN90	GIA-ST Valor Total ICMS - Substituição Tributária a recolher da coluna Substituição do Estado

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN91	GIA-ST Valor dos Produtos da coluna Retido na Entrada

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN92	GIA-ST Valor IPI da coluna Retido na Entrada
Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN93	GIA-ST Valor Despesas Acessórias da coluna Retido na Entrada

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN94	GIA-ST Valor da Base de Cálculo do ICMS próprio da coluna Retido na Entrada

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN95	GIA-ST Valor do ICMS próprio da coluna Retido na Entrada

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN96	GIA-ST Valor da Base de Cálculo do ICMS - Substituição Tributária da coluna Retido na Entrada

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN97	GIA-ST Valor do ICMS retido por Substituição Tributária da coluna Retido na Entrada

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN98	GIA-ST Valor do Produto da coluna Retido na Fonte

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN99	GIA-ST Valor IPI da coluna Retido na Fonte

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN100	GIA-ST Valor Despesas Acessórias da coluna Retido na Entrada
Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN101	GIA-ST Valor da Base de Cálculo do ICMS próprio da coluna Retido na Fonte

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN102	GIA-ST Valor do ICMS próprio da coluna Retido na Fonte

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN103	GIA-ST Valor da Base de Cálculo do ICMS - Substituição Tributária da coluna Retido na Fonte

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN104	GIA-ST Valor do ICMS retido por Substituição Tributária da coluna Retido na Fonte

Este campo não será atendido nesta OS.
Preencher com zeros.
	OS2456		RN105	Valor do Saldo Credor Apurado no final do Período


Preencher neste campo o valor do campo “saldo credor (crédito menos débito) a transportar para o período seguinte”  total correspondente ao livro de apuração do ICMS modelo P9 – módulo ICMS .
	OS2456		RN106	Valor do Saldo Devedor Apurado no final do Período
Preencher neste campo o valor do campo “saldo devedor (débito menos crédito)”  total correspondente ao livro de apuração do ICMS modelo P9 – módulo ICMS .

	OS2456		RN107	Valor da Base de Cálculo do ICMS Simples
Preencher com zeros.
	OS2456		RN108	Valor do ICMS Simples a Recolher


Preencher neste campo o valor do campo “Imposto a Recolher”  total correspondente ao livro de apuração do ICMS modelo P9 – módulo ICMS .
	OS2456		RN109	Valor da Importação FOB

Soma dos campos 20 da safx50 quando CFOP iniciar com 3 e campo 14 (modalidade de frete) da safx50 for igual a 2.	OS2456		RN110	Valor da Despesa com Frete FOB

Soma dos campos 20 da safx50 quando CFOP iniciar com 1,2,5 e 6 e campo 14 (modalidade de frete) da safx50 for igual a 2.	OS2456		RN111	Valor da Despesa com Seguro FOB


Soma dos campos 21 da safx50 e campo 14 (modalidade de frete) da safx50 for igual a 2	OS2456		RN112	Valor da Despesa com Impostos Federais FOB
Preencher com zeros.
	OS2456		RN113	Valor da Despesa Aduaneira FOB


Soma dos campos 20 da safx50 quando CFOP iniciar com 7 e campo 14 (modalidade de frete) da safx50 for igual a 2.	OS2456		RN114	Valor da Outras Despesas FOB

Preencher com zeros.	OS2456		RN115	Valor da Base de Cálculo do ICMS Importação FOB

Preencher com zeros.	OS2456		RN116	Valor do ICMS Importação

Preencher com valor da coluna “Imposto Creditado” para CFOP iniciado com 3 no ao livro de apuração do ICMS modelo P9 – módulo ICMS .
	OS2456		RN117	Valor da Importação CIF

Soma dos campos 20 da safx50 quando CFOP iniciar com 3 e campo 14 (modalidade de frete) da safx50 for igual a 1.	OS2456		RN118	Valor da Despesa com Frete CIF

Soma dos campos 20 da safx50 quando CFOP iniciar com 1,2,5 e 6 e campo 14 (modalidade de frete) da safx50 for igual a 1.
	OS2456		RN119	Valor da Despesa com Seguro CIF


Soma dos campos 21 da safx50 e campo 14 (modalidade de frete) da safx50 for igual a 1.	OS2456		RN120	Valor da Despesa com Impostos Federais CIF
Preencher com zeros.
	OS2456		RN121	Valor da Despesa Aduaneira CIF

Soma dos campos 20 da safx50 quando CFOP iniciar com 7 e campo 14 (modalidade de frete) da safx50 for igual a 1.	OS2456		RN122	Valor da Outras Despesas CIF
Preencher com zeros.	OS2456		RN123	Margem do Valor Agregado CIF

Preencher com zeros.	OS2456		RN124	Valor da Base de Cálculo do ICMS Importação CIF

Preencher com zeros.	OS2456		RN125	Valor ICMS Antecipação de Importação CIF

Preencher com zeros.	OS2456		RN126	Valor do ICMS Antecipação de Importação a Recolher CIF

Preencher com zeros.	OS2456		RN127	Data da geração do arquivo 

Preencher a data da geração do arquivo no formato ex: aaaammdd	OS2456		RN128	Hora da geração do arquivo

Preencher hora de geração do arquivo no formato ex: hh:mm:ss	OS2456		RN129	Forma de Cadastro

Preencher fixo “I”	OS2456		


Arquivo de Entradas

Neste registro recuperar no módulo ICMS valores do livro de Entradas modelo P1 – Resumo por CFOP 
Para cada linha do registro, carregar um código de CFOP agrupado por UF.
RN130	DIAPEN

Preencher fixo “DIAPEN”	OS2456		RN131	CFOP com mascara 
Verificar campo código fiscal do Resumo por CFOP do livro modelo P1 – módulo ICMS.
	OS2456		RN132	UF de entrada
Verificar Campo UF Origem.
	OS2456		RN133	Valor Contábil 
Verificar campo Valor Contábil referente ao CFOP indicado na RN131 do Resumo por CFOP do livro modelo P1 – módulo ICMS quando a coluna ICMS/IPI for igual a “ICMS”.

	OS2456		RN134	Valor base de cálculo
Verificar campo Base de Cálculo referente ao CFOP indicado na RN131 do Resumo por CFOP do livro modelo P1 – módulo ICMS quando a coluna ICMS/IPI for igual a “ICMS”.
	OS2456		RN135	Valor do Imposto creditado 

Verificar campo Imposto Creditado referente ao CFOP indicado na RN131 do Resumo por CFOP do livro modelo P1 – módulo ICMS quando o campo cod(a) estiver = 1 e quando a coluna ICMS/IPI for igual a “ICMS”.
	OS2456		RN136	Valor de Isentas e não Tributadas

Verificar campo Base de Cálculo referente ao CFOP indicado na RN131 do Resumo por CFOP do livro modelo P1 – módulo ICMS quando o campo cod(a) estiver = 2 e quando a coluna ICMS/IPI for igual a “ICMS”.
	OS2456		RN137	Valor de Outras

Verificar campo Base de Cálculo referente ao CFOP indicado na RN131 do Resumo por CFOP do livro modelo P1 – módulo ICMS quando o campo cod(a) estiver = 3 e quando a coluna ICMS/IPI for igual a “ICMS”.
	OS2456		RN138	Valor de IPI
Verificar campo Imposto Creditado referente ao CFOP indicado na R131 do Resumo por CFOP do livro modelo P1 – módulo ICMS quando o campo cod(a) estiver = 1 e quando a coluna ICMS/IPI for igual a “IPI”.

	OS2456		RN139	Valor de Imposto Retido

Verificar campo Imposto Creditado referente ao CFOP indicado na RN131 do Resumo por CFOP do livro modelo P1 – módulo ICMS quando o campo cod(a) estiver = 1 e quando a coluna ICMS/IPI for igual a “ST”.

	OS2456		


Arquivo de Saídas
Neste registro recuperar no módulo ICMS valores do livro de Entradas modelo P2 – Resumo por CFOP 
Para cada linha do registro, carregar um código de CFOP agrupado por UF.
RN140	DIAPSA

Preencher fixo “DIAPSA”	OS2456		RN141	CFOP com mascara 
Verificar campo código fiscal do Resumo por CFOP do livro modelo P2 – módulo ICMS.

	OS2456		RN142	UF de Saida
Verificar Campo UF destino.
	OS2456		RN143	Valor Contábil 

Verificar campo Valor Contábil referente ao CFOP indicado na RN141 do Resumo por CFOP do livro modelo P2 – módulo ICMS quando a coluna ICMS/IPI for igual a “ICMS”.
	OS2456		RN144	Valor base de cálculo
Verificar campo Base de Cálculo referente ao CFOP indicado na RN141 do Resumo por CFOP do livro modelo P2 – módulo ICMS quando a coluna ICMS/IPI for igual a “ICMS”.
	OS2456		RN145	Valor do Imposto Debitado
Verificar campo Imposto Debitado referente ao CFOP indicado na RN141 do Resumo por CFOP do livro modelo P2– módulo ICMS quando o campo cod(a) estiver = 1 e quando a coluna ICMS/IPI for igual a “ICMS”.

	OS2456		RN146	Valor de Isentas e não Tributadas

Verificar campo Base de Cálculo referente ao CFOP indicado na RN141 do Resumo por CFOP do livro modelo P2 – módulo ICMS quando o campo cod(a) estiver = 2 e quando a coluna ICMS/IPI for igual a “ICMS”.

	OS2456		RN147	Valor de Outras

Verificar campo Base de Cálculo referente ao CFOP indicado na RN141 do Resumo por CFOP do livro modelo P2 – módulo ICMS quando o campo cod(a) estiver = 3 e quando a coluna ICMS/IPI for igual a “ICMS”.

	OS2456		RN148	Valor de IPI

Verificar campo Imposto Creditado referente ao CFOP indicado na RN141 do Resumo por CFOP do livro modelo P2 – módulo ICMS quando o campo cod(a) estiver = 1 e quando a coluna ICMS/IPI for igual a “IPI”.
	OS2456		RN149	Valor de Imposto Retido

Verificar campo Imposto Creditado referente ao CFOP indicado na RN141 do Resumo por CFOP do livro modelo P2 – módulo ICMS quando o campo cod(a) estiver = 1 e quando a coluna ICMS/IPI for igual a “ST”.
	OS2456		


Arquivo Outros Créditos

Neste registro recuperar no módulo ICMS valores do livro de Apuração do ICMS – Modelo P9
RN150	DIAPOC

Preencher fixo “DIAPOC”	OS2456		RN151	Código de Outros Créditos
Recuperar do quadro de Crédito do Imposto – coluna “Outros Créditos” os códigos lançados nos lançamentos complementares.
	OS2456		RN152	Valor de Outros Créditos
Recuperar valor da coluna “Somas” do quadro de Crédito do Imposto – campo “Outros Créditos”
	OS2456		


Arquivo de Benefício Fiscal
RN153	DIAPBF

Preencher fixo “DIAPBF”	OS2456		RN154	Código do Benefício Fiscal
Preencher com zeros.

[Alterada – OS2456-A]
Recuperar a informação do campo Código do Benefício Fiscal (DIAP AP > Manutenção > Beneficio Fiscal), que por default será ‘300’.
	OS2456/ OS2456-A		RN155	Valor do Benefício Fiscal
Preencher com zeros.

[Alterada – OS2456-A]
Recuperar a informação do campo Valor para Anexo I (DIAP AP > Manutenção > Beneficio Fiscal).
	OS2456/ OS2456-A		

Arquivo Anexo I
RN156	DIAPA1

Preencher fixo “DIAPA1”	OS2456		RN157	Código do Anexo I
Preencher com zeros.

[Alterada – OS2456-A]
Recuperar a informação do campo Código Anexo I (DIAP AP > Manutenção > Anexo I).
Esse campo tem 6 posições e deve ser completado com zeros à esquerda.
	OS2456/ OS2456-A		RN158	Código do Município
Preencher com zeros.

[Alterada – OS2456-A]
Recuperar a informação do campo Código do Município (DIAP AP > Manutenção > Anexo I).
	OS2456/ OS2456-A		RN159	Valor para Anexo I
Preencher com zeros.

[Alterada – OS2456-A]
Recuperar a informação do campo Valor para Anexo I (DIAP AP > Manutenção > Anexo I).

	OS2456/ OS2456-A		


Arquivo Anexo II
RN160	DIAPA2

Preencher fixo “DIAPA2”	OS2456		RN161

	Código do Anexo II
Preencher com zeros.

[Alterada – OS2456-A]
Recuperar a informação do campo Código Anexo II (DIAP AP > Manutenção > Anexo II).
Esse campo tem 6 posições e deve ser completado com zeros à esquerda.
	OS2456/ OS2456-A		RN162


	Código do Município
Preencher com zeros.

[Alterada – OS2456-A]
Recuperar a informação do campo Código do Município (DIAP AP > Manutenção > Anexo II).
	

OS2456/ OS2456-A


		RN163	Valor para Anexo II
Preencher com zeros.

[Alterada – OS2456-A]
Recuperar a informação do campo Valor para Anexo II (DIAP AP > Manutenção > Anexo II).
	OS2456/ OS2456-A		


Arquivo Entradas UF
RN164	DIAPUE

Preencher fixo “DIAPUE”	OS2456		RN165	UF
Recuperar UF da Passoa Fis/Jur da nota (safx04).
	OS2456		RN166	Valor Contábil

Coluna Valor Contábil do Resumo por UF do livro de Entradas modelo P1 – módulo ICMS.

	OS2456		RN167	Valor da Base de Cálculo
Coluna Base de Cálculo do Resumo por UF do livro de Entradas modelo P1 – módulo ICMS.

	OS2456		RN168	Valor de Outras
Coluna Outras do Resumo por UF do livro de Entradas modelo P1 – módulo ICMS.

	OS2456		RN169	Valor de Demais Valores
Verificar na parte principal do Livro de Entradas modelo P1 – módulo ICMS:
- Agrupar os valores por UF da coluna Base de Cálculo Valor da Operação quando a coluna cod(a) for igual a 2 e coluna ICMS/IPI for igual a ICMS ou IPI.

	OS2456		RN170	Valor de Petróleo + energia
Coluna Petroleo/Energia do Resumo por UF do livro de Entradas modelo P1 – módulo ICMS.
	OS2456		RN171	Valor de Outros Produtos
Coluna Outros Produtos do Resumo por UF do livro de Entradas modelo P1 – módulo ICMS.

	OS2456		


Arquivo Saídas UF
RN172	DIAPUS

Preencher fixo “DIAPUS”	OS2456		RN173	UF

Recuperar UF da Passoa Fis/Jur da nota (safx04).	OS2456		RN174	Valor Contábil Contribuinte

Somar valores da coluna Valor Contábil do livro de saídas – Modelo P2 módulo ICMS 	OS2456		RN175	Valor Contábil Não Contribuinte 

Somar valores da coluna Base de Cálculo do livro de saídas – Modelo P2 módulo ICMS 	OS2456		RN176	Valor base de Cálculo Contribuinte
Somar valores da coluna Base de Cálculo do livro de saídas – Modelo P2 módulo ICMS 
	OS2456		RN177	Valor base de Cálculo Não Contribuinte

Valor base de Cálculo Contribuinte
Somar valores da coluna Base de Cálculo do livro de saídas – Modelo P2 módulo ICMS 
	OS2456		RN178	Valor Outras

Coluna Outras do Resumo por UF do livro de Saídas modelo P2 – módulo ICMS.

	OS2456		RN179	Valor Demais Valores
Verificar na parte principal do Livro de Saídas modelo P2 – módulo ICMS:
- Agrupar os valores por UF da coluna Base de Cálculo Valor da Operação quando a coluna cod(a) for igual a 2 e coluna ICMS/IPI for igual a ICMS ou IPI.
	OS2456		RN180	Valor Substituição Tributária
	OS2456		


Isenções
RN181	DIAPIS

Preencher fixo “DIAPIS”	OS2456		RN182	Código da Isenção
Preencher com zeros.
	OS2456		RN183	Valor da Isenção

Preencher com zeros.	OS2456		
D.I.
RN184	DIAPDI

Preencher fixo “DIAPDI”	OS2456		RN185	Número da D.I

Campo 4 
NUM_DI
Safx49
Relacionada à nota fiscal	OS2456		RN186	Data da D.I.

Campo 3
DAT_DI
Safx49
Relacionada à nota fiscal	OS2456		RN187	Código Moeda de Origem
Campo 50
MOEDA_ORIG
Safx49
Relacionada à nota fiscal	OS2456		RN188	Valor da Moeda Origem

Campo 26 
VLR_UNIT
safx49 
Relacionada à nota fiscal.
	OS2456		RN188	Valor da Conversão da Moeda
Campo 53
VLR_MERC_MOEDA
Safx49
Relacionada à nota fiscal.
	OS2456		


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN
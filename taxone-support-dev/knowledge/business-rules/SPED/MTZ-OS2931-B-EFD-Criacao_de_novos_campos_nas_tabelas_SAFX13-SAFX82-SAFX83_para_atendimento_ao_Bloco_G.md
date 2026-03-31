# MTZ-OS2931-B-EFD-Criacao_de_novos_campos_nas_tabelas_SAFX13-SAFX82-SAFX83_para_atendimento_ao_Bloco_G

> Fonte: MTZ-OS2931-B-EFD-Criacao_de_novos_campos_nas_tabelas_SAFX13-SAFX82-SAFX83_para_atendimento_ao_Bloco_G.doc

TITLE   \* MERGEFORMAT SPED Fiscal - Criação de novos campos nas tabelas SAFX13-SAFX82-SAFX83 para atendimento ao Bloco G - CIAP


DOCUMENTO DE REQUISITO

DR	Nome	Descrição		OS2931-B
	Criação de novos campos nas tabelas SAFX13 / SAFX82 / SAFX83 para atendimento ao Bloco G do SPED Fiscal	Módulo: Ativo Permanente
Criação dos seguintes campos na tela de Aquisição (menu: Movimento – Manutenção dos Movimentos – Aquisições)
Data da Emissão
Código Modelo NF
Chave NF-e
Número Item
Identificador Produto
Código Produto
Criação dos seguintes campos na tela de Alienação (menu: Movimento – Manutenção dos Movimentos – Alienações)
Chave NF-e
Número Item
Identificador Produto
Código Produto
Alteração da tela de Modelo de Documento Fiscal do módulo Ativo Permanente para permitir uma associação dos modelos já cadastrados com os Modelos da tabela SAFX2024.
Módulo: DW

Criação dos seguintes campos na tela de Bem Patrimonial (menu: Manutenção – Cadastros – Bem Patrimonial)
Tipo do Bem
Bem Oriundo do Ativo Circulante
Vida Útil

Job Servidor
Alteração dos processos de Carga, Importação, Importação Batch e Exportação para contemplar os novos campos criados nas tabelas abaixo:
SAFX13 / X13_BEM_ATIVO
Tipo do Bem
Bem Oriundo do Ativo Circulante
Vida Útil
SAFX82 / APT_AQUISICAO
Data da Emissão
Código Modelo NF
Chave NF-e
Número Item
Identificador Produto
Código Produto
SAFX83 / APT_ALIENACAO
Chave NF-e
Número Item
Identificador Produto
Código Produto		
REGRAS DE NEGÓCIO


Cód.	Descrição	DR		RN01	As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar os campos listados abaixo nas tabelas SAFX13 / X13_BEM_ATIVO.

Tipo do Bem: esse campo deverá ser do tipo alfanumérico e deverá possuir 1 (uma) posição. Esse campo é do tipo obrigatório. Serão exibidas três opções: “Bem Individual”, “Bem Componente” e “Bem Resultante”. Caso a opção escolhida seja “Bem Individual” deve ser gravado “1”. Caso a opção escolhida seja “Bem Componente” deve ser gravado “2”. Caso a opção escolhida seja “Bem Resultante” deve ser gravado “3”. 
Bem Oriundo do Ativo Circulante: esse campo deverá ser do tipo alfanumérico e deverá possuir 1 (uma) posição. Esse campo não é obrigatório. O campo pode ser marcado ou desmarcado. Caso o campo esteja desmarcado, será gravado “N”. Caso o mesmo esteja marcado, será gravado “S”. Esse campo não é obrigatório.
Vida Útil: esse campo deverá ser do tipo numérico e deverá possuir 3 (três) posições. Esse campo é do tipo obrigatório.	OS2931-B		RN02	As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alteradas para contemplar os campos listados abaixo nas tabelas SAFX82 / APT_AQUISICAO e SAFX83 / APT_ALIENACAO.

SAFX82 / APT_AQUISICAO 
Data da Emissão: esse campo deverá ser do tipo numérico e deverá possuir 8 (oito) posições. Esse campo é do tipo obrigatório.
Código Modelo NF: esse campo deverá ser do tipo alfanumérico e deverá possuir 2 (duas) posições. Esse campo é do tipo obrigatório.
Chave NF-e: esse campo deverá ser do tipo numérico e deverá possuir 80 (oitenta) posições. Esse campo não é obrigatório. Caso o mesmo venha “em branco” o mesmo não deve ser informado.
Número Item: esse campo deverá ser do tipo numérico e deverá possuir 5 (cinco) posições. Esse campo é obrigatório.
Identificador Produto: esse campo deverá ser do tipo alfanumérico e deverá possuir 1 (uma) posição. Esse campo é obrigatório.
Código Produto: esse campo deverá ser do tipo alfanumérico e deverá possuir 35 (trinta e cinco) posições. Esse campo é obrigatório.
SAFX83 / APT_ALIENACAO
Chave NF-e: esse campo deverá ser do tipo numérico e deverá possuir 80 (oitenta) posições. Esse campo não é obrigatório. Caso o mesmo venha “em branco” o mesmo não deve ser informado.
Número Item: esse campo deverá ser do tipo numérico e deverá possuir 5 (cinco) posições. Esse campo é obrigatório.
Identificador Produto: esse campo deverá ser do tipo alfanumérico e deverá possuir 1 (uma) posição. Esse campo é obrigatório.
Código Produto: esse campo deverá ser do tipo alfanumérico e deverá possuir 35 (trinta e cinco) posições. Esse campo é obrigatório.	OS2931-B		RN03	Deverão ser criados 2 (dois) novos campos na tela de Bem Patrimonial. O menu a ser alterado é:

Bem Patrimonial
Módulo: Básicos – MasterSAF DW
Menu: Manutenção – Cadastros – Bem Patrimonial	OS2931-B		RN04	De acordo com a RN03 os seguintes campos deverão ser criados:

Bem Patrimonial
Módulo: Básicos – MasterSAF DW
Menu: Manutenção – Cadastros – Bem Patrimonial

Tipo do Bem: esse campo deverá ser do tipo alfanumérico e deverá possuir 1 (uma) posição. Esse campo é do tipo obrigatório. Serão exibidas três opções: “Bem Individual”, “Bem Componente” e “Bem Resultante”. Caso a opção escolhida seja “Bem Individual” deve ser gravado “1”. Caso a opção escolhida seja “Bem Componente” deve ser gravado “2”. Caso a opção escolhida seja “Bem Resultante” deve ser gravado “3”. 
Bem Oriundo do Ativo Circulante: esse campo deverá ser do tipo alfanumérico e deverá possuir 1 (uma) posição. Esse campo não é obrigatório. O campo pode ser marcado ou desmarcado. Caso o campo esteja desmarcado, será gravado “N”. Caso o mesmo esteja marcado, será gravado “S”. Esse campo não é obrigatório.
Vida Útil: esse campo deverá ser do tipo numérico e deverá possuir 3 (três) posições. Esse campo é do tipo obrigatório.	OS2931-B		RN05	Deverão ser criados 3 (três) novos campos nas telas de Aquisições e Alienações do módulo Ativo Permanente. Os menus a serem alterados são:

Novo Registro de Entradas do CIAP
Módulo: Estadual – Ativo Permanente
Menu: Movimento – Manutenção dos Movimentos – Aquisições

Novo Registro de Saídas do CIAP
Módulo: Estadual – Ativo Permanente
Menu: Movimento – Manutenção dos Movimentos – Alienações	OS2931-B		RN06	De acordo com a RN05 os seguintes campos deverão ser criados:

Novo Registro de Entradas do CIAP
Módulo: Estadual – Ativo Permanente
Menu: Movimento – Manutenção dos Movimentos – Aquisições

Data da Emissão: esse campo deverá ser do tipo data e deverá possuir 8 (oito) posições. Esse campo é do tipo obrigatório. A data deverá ser informada no formato dd/mm/aaaa.
Código Modelo NF: esse campo deverá ser do tipo alfanumérico e deverá possuir 2 (duas) posições. Esse campo é do tipo obrigatório. A informação vai ser recuperada da tabela X2024.
Chave NF-e: esse campo deverá ser do tipo numérico e deverá possuir 80 (oitenta) posições. Esse campo não é obrigatório. Esse campo não é obrigatório. Caso o mesmo não esteja preenchido o mesmo não deve ser informado. A informação vai ser recuperada do campo NUM_AUTENTIC_NFE da tabela X07.
Número Item: esse campo deverá ser do tipo numérico e deverá possuir 5 (cinco) posições. Esse campo é obrigatório. Essa informação vai ser recuperada do campo NUM_ITEM da tabela X08.
Produto: esse campo deverá ser do tipo alfanumérico e deverá possui 35 (trinta e cinco) posições. Esse campo é obrigatório. IND_PRODUTO e COD_PRODUTO

Novo Registro de Saídas do CIAP
Módulo: Estadual – Ativo Permanente
Menu: Movimento – Manutenção dos Movimentos – Alienações

Chave NF-e: esse campo deverá ser do tipo numérico e deverá possuir 80 (oitenta) posições. Esse campo não é obrigatório. Esse campo não é obrigatório. Caso o mesmo não esteja preenchido o mesmo não deve ser informado. A informação vai ser recuperada do campo NUM_AUTENTIC_NFE da tabela X07.
Número Item: esse campo deverá ser do tipo numérico e deverá possuir 5 (cinco) posições. Esse campo é obrigatório. Essa informação vai ser recuperada do campo NUM_ITEM da tabela X08.
Produto: esse campo deverá ser do tipo alfanumérico e deverá possui 35 (trinta e cinco) posições. Esse campo é obrigatório. IND_PRODUTO e COD_PRODUTO	OS2931-B		RN07	A rotina de Geração das Aquisições a partir das NFs do módulo Ativo Permanente (menu: Movimento – Geração das Aquisições a partir das NFs) quando executada, deve recuperar as informações dos Documentos Fiscais e informar as mesmas na tabela APT_AQUISICAO. As informações a serem recuperadas são:

Data da Emissão: recuperar essa informação do campo DATA_EMISSAO da tabela DWT_DOCTO_FISCAL.
Código Modelo NF: recuperar essa informação do campo COD_MODELO da tabela DWT_DOCTO_FISCAL.
Chave NF-e: recuperar essa informação do campo NUM_AUTENTIC_NFE da tabela DWT_DOCTO_FISCAL.
Número Item: recuperar essa informação do campo NUM_ITEM da tabela DWT_ITENS_MERC.
Identificador Produto: recuperar essa informação do campo IND_PRODUTO da tabela DWT_ITENS_MERC.
Produto: recuperar essa informação do campo COD_PRODUTO da tabela DWT_ITENS_MERC.	OS2931-B		RN08	Deverá ser criado um campo chamado “Modelo Doc” na tela de Modelo de Documento Fiscal do módulo Ativo Permanente (módulo Ativo Permanente – menu: Cadastros >> Modelo de Documento Fiscal).	OS2931-B		RN09	O campo “Modelo Doc.” deverá recuperar as informações da tabela X2024_MODELO_DOCTO.	OS2931-B		RN10	Para cada Modelo de Documento Fiscal cadastrado o mesmo deverá ser associado ao Modelo Documento da tabela X2024_MODELO_DOCTO.	OS2931-B		RN11	O relatório de conferência da tela de Modelo de Documento Fiscal deverá ser alterado para contemplar o novo campo criado.	OS2931-B		

Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN
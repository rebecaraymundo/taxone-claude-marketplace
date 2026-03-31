# MTZ_FEDERAL_OTF_CFEM_Geracao_Tribruto_Recolhido_Mes

- **Fonte:** MTZ_FEDERAL_OTF_CFEM_Geracao_Tribruto_Recolhido_Mes.docx
- **Modificado:** 2025-03-03
- **Tamanho:** 106 KB

---

THOMSON REUTERS

Módulo Obrigações de Tributos Federais 

\(CFEM\) 

Geração do Tributo Recolhido no Mês 

__Localização__: Menu Federal, módulo Obrigações Tributos Federais, menu Outras Obrigações 🡪 CFEM 🡪 Anexo II 🡪 Geração do Tributo Recolhido no Mês

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS22684

MFS22770

Geração do Tributo Recolhido no Mês

Tratamento de Notas de Devolução e Conversão de Unidades de Medidas

24/01/2019 

\(criação do documento\)

Sumário

[1\.	Objetivo	2](#_Toc536183396)

[2\.	Parâmetros da Tela	3](#_Toc536183397)

[3\.	Processamento	5](#_Toc536183398)

# <a id="_Toc536183396"></a>Objetivo

Esta geração tem dois objetivos:

- Gerar o Tributo Recolhido no Mês
- Gerar o Total das Operações CFEM

As informações geradas são demonstradas no Anexo II do CFEM e são base para a geração da Guia de Recolhimento\.

Para Geração do Tributo Recolhido no Mês, os valores dos tributos ICMS e PIS/COFINS são recuperados da Movimentação CFEM das Operações de Vendas e consolidados valores por Produto\.  

O resultado pode ser consultado e manipulado via Tela de Tributo Recolhido no Mês\.

Para a Geração dos Totais por Operações CFEM, os valores de operação e quantidade são recuperados da Movimentação CFEM e consolidados por Operação de Venda, Transformação, Consumo e Utilização considerando o Produto e a Data Fiscal\.

Veja os quadros do A e B do Anexo II, preenchidos por essa geração:

![](data:image/png;base64,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)

# <a id="_Toc536183397"></a>Parâmetros da Tela 

Mês/Ano Apuração:  \[00/0000\]

\[ \] Excluir Registros Digitados

\[ \] Considerar devoluções de venda como dedução do faturamento

\[ \] Aplicar a Conversão de Unidade de Medida

Estabelecimentos:

\[ \] Código – Razão Social

\[ \] Código – Razão Social

\[ \] Código – Razão Social

Funcionamento dos campos:

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

<a id="_Hlk517437550"></a>Mês/Ano Apuração

Data 

__S__

S

MM/AAAA

Neste campo o usuário informa o mês e o ano do período da apuração CFEM\.

Devem ser um mês e ano válidos

Excluir Registros Digitados

Check\-box

__N__

S

Caso esta opção seja selecionada, a geração elimina os registros de “Tributo Recolhido no Mês” que foi incluído manualmente via tela de Tributo Recolhido no Mês\.

Caso contrário, só elimina os registros de “Tributo Recolhido no Mês” gerados através desta rotina\.

Considerar devoluções de venda como dedução do faturamento

Check\-box

__N__

S

Caso esta opção seja selecionada, a geração irá recuperar a Movimentação CFEM de devolução e abater no faturamento das Vendas, deduzindo a quantidades, o valor e o tributo das Vendas\.

Caso esta opção não seja selecionada, a Movimentação CFEM de devolução não são consideradas na geração\.

Aplicar a Conversão de Unidade de Medida

Check\-box

__N__

S

Caso esta opção seja selecionada, quantidade da Movimentação CFEM é convertida tanto na unidade de medida presente no Cadastro do Produto, quanto na unidade de medida do Cadastro da Substância\. 

Estabelecimentos

Alfanumérico 

__S__

S

Neste campo é exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário\.

Selecionar Todos

Desmarcar Todos

N

N

Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos”\.

# <a id="_Toc536183398"></a>Processamento

__Origem dos dados__: 	Movimentação CFEM \(tabela TFT\_MOVTO\_CFEM\);

            		Tributos \(TACES 15\) \(tabela DWT\_TRIBUTO\)	

			Conversão de Unidade de Medida \(por Produto e Padrão\)

__Dados Gerados__: “Tributo Recolhido no Mês” \(tabela TFT\_TRIB\_RECOL\_MES\)  \- Quadro B do Anexo II

                            “Totais por Operação CFEM \(tabela TFT\_TOT\_OPER\_CFEM\) \- Quadro A do Anexo II

__Etapa 1\) Geração dos Tributos Recolhidos no Mês:__

Este processamento consiste na leitura da Movimentação CFEM \(tabela TFT\_MOVTO\_CFEM\) e consolidação dos valores de ICMS e PIS/COFINS por produto\. 

O resultado pode ser consultado e alterado via Tela de Tributo Recolhido no Mês e é apresentado no quadro B do Anexo II titulado “TRIBUTOS RECOLHIDOS NO MÊS”\. 

Tabela que armazena o resultado deste processamento é a TFT\_TRIB\_RECOL\_MES\.

Critérios de Recuperação da Movimentação CFEM

Ler a Movimentação CFEM \(tabela TFT\_MOVTO\_CFEM\) considerando:

- Empresa de login do Manager
- Estabelecimento selecionado na Tela de Geração
- Data fiscal compreendida no Mês/Ano informado na Tela de Geração\.
- Operação CFEM = Venda

Recuperar as informações de Valor do ICMS, Valor do Pis/Cofins, Produto\.

Tratamento dos Movimentos CFEM de Devolução:

Para os movimentos recuperados aplicar o seguinte tratamento:

Se “Considerar devoluções de venda como dedução do faturamento” igual a “__Sim__”:

Se o registro de Movimentação CFEM \(tabela TFT\_MOVTO\_CFEM\) for Normal \(campo NORM\_DEV = ‘1’\) então:

	Somar o Valor do ICMS ao total de ICMS por produto

	Somar o Valor do PIS/COFINS ao total de PIS/COFINS por produto

Se o registro de Movimentação CFEM \(tabela TFT\_MOVTO\_CFEM\) for Devolução \(campo NORM\_DEV = ‘2’\) então:

	Subtrair o Valor do ICMS ao total de ICMS por produto

	Subrair o Valor do PIS/COFINS ao total de PIS/COFINS por produto

Se “Considerar devoluções de venda como dedução do faturamento” igual a “__Não__”:

Se o registro de Movimentação CFEM \(tabela TFT\_MOVTO\_CFEM\) for Normal \(campo NORM\_DEV = ‘1’\) então:

	Somar o Valor do ICMS ao total de ICMS por produto

	Somar o Valor do PIS/COFINS ao total de PIS/COFINS por produto

Se o registro de Movimentação CFEM \(tabela TFT\_MOVTO\_CFEM\) for Devolução \(campo NORM\_DEV = ‘2’\) então:

	Desconsidera o registro de devolução\. Ou seja:

Não considera o Valor do ICMS do registro no total de ICMS por produto\.

Não considera o Valor do PIS/COFINS do registro no total de PIS/COFINS por produto\.

Gravar as Informações em “Tributo Recolhido no Mês” \(tabela TFT\_TRIB\_RECOL\_MES\) \.

__Tributo Recolhido no Mês__

__\(TFT\_TRIB\_RECOL\_MES\)__

__Regra de Preenchimento__

Empresa \(COD\_EMPRESA\)

Empresa de Login do Manager

Estabelecimento \(COD\_ESTAB\)

Estabelecimento selecionado na Tela de Geração

Mês/Ano \(DAT\_APUR\)

Último dia do Mês/Ano da Apuração

Estado \(IDENT\_ESTADO\)

Uf do Estabelecimento

Município \(COD\_MUNICIPIO\)

Municipio do Estabelecimento

Produto \(IDENT\_PRODUTO\)

Identificador do Produto do Movimento CFEM\.

Como o grupo, Indicador e Código do Produto recuperar Identificador do Produto, do registro de máxima validade menor ou igual a Data Fim do Mês/Ano Apuração\. \(tabela SAFX2013\)

Tipo de Tributo

Para o Valor do PIS/COFINS, gravar 1 \- Federal

Para o Valor do ICMS, gravar 2 \- Estadual

Código de Tributo

Origem: Tributos \(TACES 15\) \(tabela DWT\_TRIBUTO\)

Para o Valor do PIS/COFINS, gravar o Código do Tributo referente ao PIS/COFINS

Para o Valor do ICMS, gravar o Código do Tributo referente ao ICMS

Valor do Tributo

Valor do PIS/COFINS ou Valor do ICMS do Movimento CFEM\.

__Etapa 2\) Geração dos Totais por Operação CFEM no Mês:__

Este processamento que consiste na leitura da Movimentação CFEM \(tabela TFT\_MOVTO\_CFEM\), consolidando a quantidade e do valor da operação pelas Operações CFEM, por Data fiscal e Produto\. O resultado é apresentado no quadro A do Anexo II\. 

Tabela que armazena o resultado deste processamento é a <a id="_Hlk536179603"></a>TFT\_TOT\_OPER\_CFEM\.

Neste processamento vamos fazer o tratamento para as devoluções, considerando o parâmetro “Considerar devoluções de venda como dedução do faturamento” e a conversão de unidades de medida, considerando o parâmetro “Aplicar a Conversão de Unidade de Medida”\.

Critérios de Recuperação da Movimentação CFEM:

Ler a Movimentação CFEM \(tabela TFT\_MOVTO\_CFEM\) considerando os seguintes critérios:

- Empresa de login do Manager
- Estabelecimento selecionado na Tela de Geração
- Data fiscal compreendida no Mês/Ano informado na Tela de Geração\.
- Operação CFEM  = Todas as Operações, ou seja, Venda, Transformação, Consumo e Utilização

Recuperar o Produto, a Data Fiscal e a Quantidade e o Valor Operação separada pelas Operações CFEM:

- Quantidade e Valor Operação das Venda
- Quantidade e Valor Operação Transformação
- Quantidade e Valor Operação Consumo
- Quantidade e Valor Operação Utilização

Tratamento dos Movimentos CFEM de Devolução:

Para os movimentos recuperados aplicar o seguinte tratamento:

Se “Considerar devoluções de venda como dedução do faturamento” igual a “__Sim__”:

Se o registro de Movimentação CFEM \(tabela TFT\_MOVTO\_CFEM\) for Normal \(campo NORM\_DEV = ‘1’\) então:

	Somar a Quantidade lida ao Total da Quantidade da Operação CFEM

	Somar o Valor da Operação lido ao Total do Valor da Operação CFEM

Se o registro de Movimentação CFEM \(tabela TFT\_MOVTO\_CFEM\) for Devolução \(campo NORM\_DEV = ‘2’\) então:

	Subtrair a Quantidade lida ao Total da Quantidade da Operação CFEM

	Subtrair o Valor da Operação lido ao Total do Valor da Operação CFEM

Se “Considerar devoluções de venda como dedução do faturamento” igual a “__Não__”:

Se o registro de Movimentação CFEM \(tabela TFT\_MOVTO\_CFEM\) for Normal \(campo NORM\_DEV = ‘1’\) então:

	Somar a Quantidade lida ao Total da Quantidade da Operação CFEM

	Somar o Valor da Operação lido ao Total do Valor da Operação CFEM

Se o registro de Movimentação CFEM \(tabela TFT\_MOVTO\_CFEM\) for Devolução \(campo NORM\_DEV = ‘2’\) então:

	Desconsiderar o registro de devolução\. Ou seja:

Não considerar nem a Quantidade nem o Valor da Operação do registro lido\. 

Tratamento da Conversão de Unidades de Medida dos Movimentos CFEM:

Para os movimentos recuperados aplicar o seguinte tratamento:

Se “__Aplicar a Conversão de Unidade de Medida__” igual a “__Sim__”, então:

Considerar a quantidade do registro de Movimentação CFEM, convertida para as unidades de medidas do Produto e da Substância\.

Pelo fato do sistema permitir a emissão do Anexo II por Produto ou por Substância, temos que aplicar a conversão para as duas unidades de medidas \(do Produto e da Substância\)\. Sendo assim internamente armazenamos as seguintes informações:

- Quantidade convertida para a Unidade de Medida do Produto 
- Unidade de Medida do Produto
- Quantidade convertida para a Unidade de Medida da Substância
- Unidade de Medida da Substância\.

A seguir a explicação da regra de conversão\.

	__\(\*\)__ Conversão para a Unidade de Medida do Produto:

Comparar a Unidade de Medida do Cadastro do Produto x Unidade de Medida da Movimentação CFEM\.

Se Unidade de Medida do Cadastro do Produto __é igual a__ Unidade de Medida da Movimentação CFEM, então:

	Não há necessidade de aplicar a conversão\.

A Quantidade e a Unidade de medida lidas do registro de Movimentação CFEM são considerados para a consolidação e gravação da nova tabela TFT\_TOT\_OPER\_CFEM\.

__Totais por Operação CFEM \(TFT\_TOT\_OPER\_CFEM\)__

__Regra de Preenchimento__

IDENT\_MEDIDA\_PROD

IDENT\_MEDIDA da Movimentação CFEM \(TFT\_MOVTO\_CFEM\)

QTD\_VENDA\_PROD ou QTD\_TRANSFORMACAO\_PROD ou QTD\_CONSUMO\_PROD ou QTD\_UTILIZACAO\_PROD

QUANTIDADE da Movimentação CFEM \(TFT\_MOVTO\_CFEM\)

Se Unidade de Medida do Cadastro do Produto __é diferente da__ Unidade de Medida da Movimentação CFEM, então:

	Há necessidade de aplicar a conversão\.

Primeiro verificar se existe __*Conversão de Unidade de Medida por Produto \(DW\_CONV\_MEDIDA2\)*__, \(*Módulo DW menu* “*Manutenção 🡪 Cadastros 🡪 Conversão de Unidades de Medida 🡪 Produto*”\),  considerando:

- 
	- 
		- 
			- Produto: Produto do registro lido da Movimentação CFEM
			- Medida Origem: Medida do registro lido da Movimentação CFEM \(TFT\_MOVTO\_CFEM\)
			- Medida Destino: Medida do Cadastro do Produto \(SAFX2013\)

Caso exista, então:

Aplica\-se o Fator de Conversão a Quantidade lida do registro de Movimentação CFEM para a consolidação e gravação da nova tabela TFT\_TOT\_OPER\_CFEM\.

__Totais por Operação CFEM \(TFT\_TOT\_OPER\_CFEM\)__

__Regra de Preenchimento__

IDENT\_MEDIDA\_PROD

IDENT\_MEDIDA do Produto \(SAFX2013\)

QTD\_VENDA\_PROD ou QTD\_TRANSFORMACAO\_PROD ou QTD\_CONSUMO\_PROD ou QTD\_UTILIZACAO\_PROD

QUANTIDADE da Movimentação CFEM \(TFT\_MOVTO\_CFEM\) \* Fator de Conversão

Caso não exista, então:

Verificar a existência da __*Conversão de Unidade de Medida Padrão \(DW\_CONV\_MEDIDA\)*__, \(*Módulo DW menu* “*Manutenção 🡪 Cadastros 🡪 Conversão de Unidades de Medida 🡪 Padrão*”\) considerando:

- 
	- 
		- 
			- 
				- Medida Origem: Medida do registro lido da Movimentação CFEM \(TFT\_MOVTO\_CFEM\)
				- Medida Destino: Medida do Cadastro do Produto \(SAFX2013\)

Caso exista, então:

Aplica\-se o Fator de Conversão a Quantidade lida do registro de Movimentação CFEM para a consolidação e gravação da nova tabela TFT\_TOT\_OPER\_CFEM\.

__Totais por Operação CFEM \(TFT\_TOT\_OPER\_CFEM\)__

__Regra de Preenchimento__

IDENT\_MEDIDA\_PROD

IDENT\_MEDIDA do Produto \(SAFX2013\)

QTD\_VENDA\_PROD ou QTD\_TRANSFORMACAO\_PROD ou QTD\_CONSUMO\_PROD ou QTD\_UTILIZACAO\_PROD

QUANTIDADE da Movimentação CFEM \(TFT\_MOVTO\_CFEM\) \* Fator de Conversão

Caso não exista, então:

Gerar mensagem de erro no log da geração\.

*10351 \-* “*Não foi possível fazer a Conversão de Unidade de Medida da Movimentação CFEM para a Medida do Produto, pois não há Cadastro de Conversão de Medida Padrão nem por Produto\.*

*Dados do Movimento CFEM: Estab – Data Fiscal – Movimento Ent\./Saída \- Número – Série – Subsérie \- Produto”*

Aplica\-se o Fator de Conversão = Zero a Quantidade lida do registro de Movimentação CFEM para a consolidação e gravação da nova tabela TFT\_TOT\_OPER\_CFEM\.

__Totais por Operação CFEM \(TFT\_TOT\_OPER\_CFEM\)__

__Regra de Preenchimento__

IDENT\_MEDIDA\_PROD

IDENT\_MEDIDA do Produto \(SAFX2013\)

QTD\_VENDA\_PROD ou QTD\_TRANSFORMACAO\_PROD ou QTD\_CONSUMO\_PROD ou QTD\_UTILIZACAO\_PROD

Gravar Zero\.

\(QUANTIDADE da Movimentação CFEM \(TFT\_MOVTO\_CFEM\) \* 0,00\)

__\(\*\)__ Conversão para a Unidade de Medida da Substância:

Para o Produto que possua Substância parametrizada \(*Módulo Obrigações Tributos Federais,  Menu CFEM 🡪 Parâmetros 🡪 Produto – tabela TFT\_PAR\_PRD\_CFEM*\), considerar a Unidade de Medida da Substância do Cadastro da Substância \(*Módulo Obrigações Tributos Federais, de Menu CFEM 🡪 Parâmetros 🡪 Substância – tabela TFT\_PAR\_SUBST\_CFEM*\) para conversão da quantidade lida da Movimentação\.

Comparar a Unidade de Medida do Cadastro da Substância x Unidade de Medida da Movimentação CFEM\.

Se Unidade de Medida do Cadastro da Substância __é igual a__ Unidade de Medida da Movimentação CFEM, então:

	Não há necessidade de aplicar a conversão\.

A Quantidade e a Unidade de medida lidas do registro de Movimentação CFEM são considerados para a consolidação e gravação da nova tabela TFT\_TOT\_OPER\_CFEM\.

__Totais por Operação CFEM \(TFT\_TOT\_OPER\_CFEM\)__

__Regra de Preenchimento__

IDENT\_MEDIDA\_SUBST

IDENT\_MEDIDA da Movimentação CFEM \(TFT\_MOVTO\_CFEM\)

QTD\_VENDA\_SUBST ou QTD\_TRANSFORMACAO\_SUBST ou QTD\_CONSUMO\_SUBST ou QTD\_UTILIZACAO\_SUBST

QUANTIDADE da Movimentação CFEM \(TFT\_MOVTO\_CFEM\)

Se Unidade de Medida do Cadastro da Substância __é diferente da__ Unidade de Medida da Movimentação CFEM, então:

	Há necessidade de aplicar a conversão\.

Verificar a existência da __*Conversão de Unidade de Medida Padrão \(DW\_CONV\_MEDIDA\)*__, \(*Módulo DW menu* “*Manutenção 🡪 Cadastros 🡪 Conversão de Unidades de Medida 🡪 Padrão*”\)considerando:

- 
	- 
		- 
			- 
				- Medida Origem: Medida do registro lido da Movimentação CFEM \(TFT\_MOVTO\_CFEM\)
				- Medida Destino: Medida do Cadastro da Substância \(TFT\_PAR\_SUBST\_CFEM\)

Caso exista, então:

Aplica\-se o Fator de Conversão a Quantidade lida do registro de Movimentação CFEM para a consolidação e gravação da nova tabela TFT\_TOT\_OPER\_CFEM\.

__Totais por Operação CFEM \(TFT\_TOT\_OPER\_CFEM\)__

__Regra de Preenchimento__

IDENT\_MEDIDA\_SUBST

IDENT\_MEDIDA da Substância \(TFT\_PAR\_SUBST\_CFEM\)

QTD\_VENDA\_SUBST ou QTD\_TRANSFORMACAO\_SUBST ou QTD\_CONSUMO\_SUBST ou QTD\_UTILIZACAO\_SUBST

QUANTIDADE da Movimentação CFEM \(TFT\_MOVTO\_CFEM\) \* Fator de Conversão

Caso não exista, então:

Gerar mensagem de erro no log da geração\.

*10352 \- *“*Não foi possível fazer a Conversão de Unidade de Medida da Movimentação CFEM para a Medida da Substância, pois não há Cadastro de Conversão de Medida Padrão\.*

*Dados do Movimento CFEM: Estab – Data Fiscal – Movimento Ent\./Saída \- Número – Série – Subsérie \- Produto”*

Aplica\-se o Fator de Conversão = Zero a Quantidade lida do registro de Movimentação CFEM para a consolidação e gravação da nova tabela TFT\_TOT\_OPER\_CFEM\.

__Totais por Operação CFEM \(TFT\_TOT\_OPER\_CFEM\)__

__Regra de Preenchimento__

IDENT\_MEDIDA\_SUBST

IDENT\_MEDIDA da Substância \(TFT\_PAR\_SUBST\_CFEM\)

QTD\_VENDA\_SUBST ou QTD\_TRANSFORMACAO\_SUBST ou QTD\_CONSUMO\_SUBST ou QTD\_UTILIZACAO\_SUBST

Gravar Zero\.

\(QUANTIDADE da Movimentação CFEM \(TFT\_MOVTO\_CFEM\) \* 0,00\)

Se “__Aplicar a Conversão de Unidade de Medida__” igual a “__Não__”, então:

Considerar a quantidade e a unidade de medida do registro de Movimentação CFEM\.

Pelo fato do sistema permitir a emissão do Anexo II por Produto ou por Substância, criamos internamente campos: 

- Quantidade convertida na Unidade de Medida do Produto 
- Unidade de Medida do Produto
- Quantidade convertida na Unidade de Medida da Substância
- Unidade de Medida da Substância\.

No caso de não aplicar a conversão de unidade de medida, carregamos esses campos com a mesma informação: a quantidade e a unidade de medida da Movimentação CFEM\.

__Totais por Operação CFEM \(TFT\_TOT\_OPER\_CFEM\)__

__Regra de Preenchimento__

IDENT\_MEDIDA\_PROD

IDENT\_MEDIDA da Movimentação CFEM \(TFT\_MOVTO\_CFEM\)

QTD\_VENDA\_PROD ou QTD\_TRANSFORMACAO\_PROD ou QTD\_CONSUMO\_PROD ou QTD\_UTILIZACAO\_PROD

QUANTIDADE da Movimentação CFEM \(TFT\_MOVTO\_CFEM\)

IDENT\_MEDIDA\_SUBST

IDENT\_MEDIDA da Movimentação CFEM \(TFT\_MOVTO\_CFEM\)

QTD\_VENDA\_SUBST ou QTD\_TRANSFORMACAO\_SUBST ou QTD\_CONSUMO\_SUBST ou QTD\_UTILIZACAO\_SUBST

QUANTIDADE da Movimentação CFEM \(TFT\_MOVTO\_CFEM\)

Gravação do Resultado da Consolidação das Operações CFEM:

O resultado é apresentado no primeiro quadro do Anexo II\. Tabela que armazena o resultado deste processamento é a TFT\_TOT\_OPER\_CFEM\.

__Totais por Operação CFEM \(TFT\_TOT\_OPER\_CFEM\)__

__Regra de Preenchimento__

Empresa \(COD\_EMPRESA\)

Empresa de Login do Manager

Estabelecimento \(COD\_ESTAB\)

Estabelecimento selecionado na Tela de Geração

Data Fiscal \(DATA\_FISCAL\)

Data Fiscal do Movimento CFEM 

Produto \(IDENT\_PRODUTO\)

Identificador do Produto do Movimento CFEM\.

Como o grupo, Indicador e Código do Produto recuperar Identificador do Produto, do registro de máxima validade menor ou igual a Data Fim do Mês/Ano Apuração\.

\(tabela SAFX2013\)

Substância \(COD\_SUBSTANCIA\)

Caso o Produto possua Substância Cadastrada, gravar o código da substância

\(tabela TFT\_PAR\_PRD\_CFEM\)

Medida do Produto \(IDENT\_MEDIDA\_PROD\)

Identificador da Medida do Cadastro do Produto relacionado no Movimento CFEM\.

Como o grupo, Código da Medida, recuperar Identificador do Medida, do registro de máxima validade menor ou igual a Data Fim do Mês/Ano Apuração\.

\(tabela SAFX2013\)

Medida da Substância

\(IDENT\_MEDIDA\_SUBST\)

Identificador da Medida do Cadastro da Substância relacionada ao Produto do Movimento CFEM\.

Como o grupo, Código da Medida, recuperar Identificador do Medida, do registro de máxima validade menor ou igual a Data Fim do Mês/Ano Apuração\.

\(tabela TFT\_PAR\_PRD\_CFEM – TFT\_PAR\_SUBST\_CFEM\)

Quantidade de Venda do Produto \(QTD\_VENDA\_PROD\)

Quantidade do Movimento CFEM, com Operação CFEM = Venda \(COD\_OPER\_CFEM  = '1'\), na Unidade de Medida do Produto

Aplicar as regras da Devolução e da Conversão de Unidades de Medidas já descritas\.

Quantidade de Venda da Substância \(QTD\_VENDA\_SUBST\)

Quantidade do Movimento CFEM, com Operação CFEM = Venda \(COD\_OPER\_CFEM  = '1'\), na Unidade de Medida da Substância

Aplicar as regras da Devolução e da Conversão de Unidades de Medidas já descritas\.

Valor da Venda

VLR\_VENDA

Valor da Operação do Movimento CFEM, com Operação CFEM = Venda \(COD\_OPER\_CFEM = '1'\)

Aplicar a regra da Devolução já descrita\.

Quantidade de Transformação do Produto

QTD\_TRANSFORMACAO\_PROD

Quantidade do Movimento CFEM, com Operação CFEM = Venda \(COD\_OPER\_CFEM  = '2'\), na Unidade de Medida do Produto

Aplicar as regras da Devolução e da Conversão de Unidades de Medidas já descritas\.

Quantidade de Transformação da Substância

QTD\_TRANSFORMACAO\_SUBST

Quantidade do Movimento CFEM, com Operação CFEM = Venda \(COD\_OPER\_CFEM  = '2'\), na Unidade de Medida da Substância

Aplicar as regras da Devolução e da Conversão de Unidades de Medidas já descritas\.

Valor da Transformação

VLR\_TRANSFORMACAO

Valor da Operação do Movimento CFEM, com Operação CFEM = Venda \(COD\_OPER\_CFEM  = '2'\)

Aplicar a regra da Devolução já descrita\.

Quantidade de Consumo do Produto

QTD\_CONSUMO\_PROD

Quantidade do Movimento CFEM, com Operação CFEM = Venda \(COD\_OPER\_CFEM  = '3'\), na Unidade de Medida do Produto

Aplicar as regras da Devolução e da Conversão de Unidades de Medidas já descritas\.

Quantidade de Consumo da Substância

QTD\_CONSUMO\_SUBST

Quantidade do Movimento CFEM, com Operação CFEM = Venda \(COD\_OPER\_CFEM  = '3'\), na Unidade de Medida da Substância

Aplicar as regras da Devolução e da Conversão de Unidades de Medidas já descritas\.

Valor do Consumo

VLR\_CONSUMO

Valor da Operação do Movimento CFEM, com Operação CFEM = Venda \(COD\_OPER\_CFEM  = '3'\)

Aplicar a regra da Devolução já descrita\.

Quantidade de Utilização do Produto

QTD\_UTILIZACAO\_PROD

Quantidade do Movimento CFEM, com Operação CFEM = Venda \(COD\_OPER\_CFEM  = '4'\), na Unidade de Medida do Produto

Aplicar as regras da Devolução e da Conversão de Unidades de Medidas já descritas\.

Quantidade de Utilização da Substância

QTD\_UTILIZACAO\_SUBST

Quantidade do Movimento CFEM, com Operação CFEM = Venda \(COD\_OPER\_CFEM  = '4'\), na Unidade de Medida da Substância

Aplicar as regras da Devolução e da Conversão de Unidades de Medidas já descritas\.

Valor da Utilização

VLR\_UTILIZACAO

Valor da Operação do Movimento CFEM, com Operação CFEM = Venda \(COD\_OPER\_CFEM  = '4'\)

Aplicar a regra da Devolução já descrita\.

Quantidade Total do Produto

QTD\_TOTAL\_PROD

QTD\_VENDA\_PROD \+

QTD\_TRANSFORMACAO\_PROD \+ 

QTD\_CONSUMO\_PROD \+ 

QTD\_UTILIZACAO\_PROD

Quantidade Total da Substâcia

QTD\_TOTAL\_SUBST

QTD\_VENDA\_SUBST \+ 

QTD\_TRANSFORMACAO\_SUBST \+

QTD\_CONSUMO\_SUBST \+ 

QTD\_UTILIZACAO\_SUBST

Valor Total

VLR\_TOTAL

VLR\_VENDA \+ 

VLR\_TRANSFORMACAO \+ 

VLR\_CONSUMO\+ 

VLR\_UTILIZACAO

NUM\_PROCESSO

Parâmetro P\_NRO\_PROCESSO

USUARIO

Parâmetro P\_USUARIO

IND\_DIG\_CALC

‘2’


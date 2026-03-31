# Tela_Incentivos_Fiscais_FINAN_FINOR

> Fonte: Tela_Incentivos_Fiscais_FINAN_FINOR.doc

THOMSON REUTERS

Tela de Incentivos Fiscais 
ECF - Escrituração Contábil Fiscal

DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		13/03/2018	
MFS-12666	Criação do documento	Alessandra Cristina Navatta 		04/06/2018	MFS-18708	Quebra do Item de Menu

Incentivos Fiscais >> FINAN e FINOR	Alessandra Cristina Navatta		


Sumário

 TOC \o "1-3" \h \z \u  HYPERLINK \l "_Toc515870707" 1.	INTRODUÇÂO	 PAGEREF _Toc515870707 \h 3
 HYPERLINK \l "_Toc515870708" 2.	DOCUMENTOS DE REFERÊNCIAS	 PAGEREF _Toc515870708 \h 3
 HYPERLINK \l "_Toc515870709" 3.	TELA/MODAIS	 PAGEREF _Toc515870709 \h 3
 HYPERLINK \l "_Toc515870710" 3.1 Pesquisa de Registros	 PAGEREF _Toc515870710 \h 3
 HYPERLINK \l "_Toc515870711" 3.2 Regras dos Campos Tela Principal	 PAGEREF _Toc515870711 \h 5

INTRODUÇÂO

O objetivo desta especificação é criar uma tela para lançamento dos incentivos fiscais

DOCUMENTOS DE REFERÊNCIAS

Mensagens_Sistema_DWECF.xlsx
Regras_Gerais_DWECF.docx
MTZ_Processamento_em_Lote.docx
Tela_Abertura_de_Apuracao.doc


TELA/MODAIS

3.1 Pesquisa de Registros

Localização da tela: ECF - Escrituração Contábil Fiscal >> Apuração >> Lucro Real>> Incentivos Fiscais >> FINAN e FINOR

Título da tela: FINAN e FINOR


Obs. As opções dos campos de pesquisa e suas opções, podem ter alguma divergência na escrita e tipo, pois serão apresentados como cadastradas no banco.

Campo	Tipo	Regra		Estabelecimento 	LOV
(Tipo - Código – Descrição)	Permite que o usuário busque o registro pelo Código do Estabelecimento.		Exercício	Texto
(AAAA)
	O usuário poderá informar o exercício. 
		Data Inicial	Data
DD/MM/AAAA	O usuário poderá informar a data inicial da Informação ECF.		Versão	Lista
(Código -Descrição)	Aplicar a RNG00004 - Versão de Layout		Forma de Tributação	Lista
(Código -Descrição)	Exibe as opções abaixo:

- Lucro Real
- Lucro Presumido,
-Lucro Arbitrado
-Imune de IRPJ 
-Isento do IRPJ 		Apuração	Lista
(Código -Descrição)	Exibe as opções abaixo:

- Anual
- Trimestral
		Período de Apuração	Lista 
(Código -Descrição)	Exibe as opções abaixo:
 
- Se Apuração= Anual:

Janeiro
Fevereiro
Março
Abril
Maio
Junho
Julho
Agosto
Setembro
Outubro
Novembro
Dezembro

- Se Apuração= Trimestral:

1º Trimestre
2º Trimestre
3º Trimestre
4º Trimestre

		Status	Lista
(Código)	Exibe a lista de Status:

- Importação dos Saldos Realizada- Cálculo Realizado- Reapurar- Alteração Manual Realizada- Aguardando Alteração Manual

		


3.2 Regras dos Campos Tela Principal

Localização da tela: ECF - Escrituração Contábil Fiscal >> Apuração >> Lucro Real>> Incentivos Fiscais >> FINAN e FINOR
Título da tela: FINAN e FINOR 

Considerações: 

As informações deste cabeçalho terão como origem a seleção efetuada pela tela de pesquisa.
Tela de Seleção das Apurações: recuperar apenas as aberturas diferentes de “Apuração em Aberto” e A00.
Desabilitar os botões “Novo”, “Copiar” e “Excluir” na toolbar.
Não permitir edição do registro, se o status da apuração for diferente de ‘Cálculo Realizado’. Caso status diferente de ‘Cálculo Realizado’, aplicar DW00195. 
Se o status for Calculo Realizado e não atender as condições da RNG00054 – Incentivos Fiscais, não permitir a edição dos valores e exibir a mensagem DW00181.


Campo	Tipo	Obrig	Ed	Formato/Default	Regra	MFS		Cabeçalho (*)		Estabelecimento 

	Texto	S	N	Tipo - Código – Descrição	Permite que o usuário visualize o Estabelecimento da apuração que foi recuperada 	MFS-12666		Exercício 	Texto	S	N	AAAA	Exibe o exercício da escrituração.
	MFS-12666		Data Inicial	Texto	S	N	DD/MM/AAAA	Exibe a Data Inicial da escrituração.
	MFS-12666		Versão	Texto	S	N		Permite que o usuário visualize a Versão do Layout utilizada para o processamento do registro.

Valores válidos:

Aplicar RNG00004-Versão de Layout.	MFS-12666		Forma de Tributação	Texto	S	N	Descrição	Exibe a forma de tributação do registro selecionado.

Conteúdos Válidos:
- Lucro Real
- Lucro Presumido,
-Lucro Arbitrado
-Imune de IRPJ 
-Isento do IRPJ 
	MFS-12666		Apuração	Texto	S	N	Descrição	Exibe a apuração do registro selecionado.

Conteúdos Válidos:
- Anual
- Trimestral
	MFS-12666		Período de Apuração	Texto	S	N	Descrição	Exibe o período de apuração do registro selecionado.

Conteúdos Válidos:

- Se Apuração= Anual:

Janeiro
Fevereiro
Março
Abril
Maio
Junho
Julho
Agosto
Setembro
Outubro
Novembro
Dezembro

- Se Apuração= Trimestral:

1º Trimestre
2º Trimestre
3º Trimestre
4º Trimestre

	MFS-12666		PARÂMETROS DOS INCENTIVOS FISCAIS		Base de Cálculo 	Texto	S	S	0,00	Permite que o usuário visualize/ajuste o valor da base de cálculo do incentivo fiscal

Tratamentos:

Recupera o valor calculado para este campo, conforme RNC13, do MTZ_Processamento_em_Lote.docx.

Se não existir valor no campo Base de Cálculo (maior que zero), os campos de Valor Líquido de todos os incentivos devem ser bloqueados para edição.


Tratamento válido a partir da versão 2.0

Se o conteúdo deste campo for zerado, os campos citados abaixo deverão ser zerados e os campos de Valor Líquido (dos incentivos FINOR e FINAM), devem ser bloqueados para edição.

Valor Limite 6%
Valor Líquido (FINOR)*
Percentual (FINOR)* 
Valor Líquido (FINAM)*
Percentual(FINAM)* 
Valor Líquido (Total)*
Percentual (Total)*

Se for ajustado o valor da base, (recalcular o o campo Valor Limite 6%) e apagar os demais valores e percentuais.

	 MFS-12666		Valor Limite 6%	Texto	S	N	Desabilitado
0,00	Exibe o valor limite 6% ser utilizado.

Tratamentos:

Este campo não deve ser habilitado para edição, e o mesmo deve ser calculado pelo sistema. 

Exibe o valor do cálculo: Base de Cálculo x 0,06 

	
MFS-12666		FINOR (ATÉ 6%)		Valor Líquido (FINOR)*	Texto	S	S	Desabilitado

0,00	Permite que o usuário insira o valor liquido referente ao Finor até 6% sobre o incentivo fiscal.


Tratamento:
Se o conteúdo deste campo for zerado, o campo Percentual (FINOR) deve ser zerado.

	MFS-12666		Percentual (FINOR)*	Texto	S	N	Desabilitado
0,0000	Exibe o percentual referente ao Finor até 6% sobre o incentivo fiscal

Tratamento:

Se houver valor nos campos FINOR e Base de Cálculo, exibir o resultado do cálculo abaixo:
(Valor Líquido (FINOR) / Base de Cálculo) x 100

	MFS-12666		FINAM (ATÉ 6%)		Valor Líquido (FINAM)*	Texto	S	S	Desabilitado
0,00	Permite que o usuário insira o Valor Líquido referente ao Finam até 6% sobre o incentivo fiscal.


Tratamento
Se o conteúdo deste campo for zerado, o campo Percentual (FINAM) deve ser zerado.

	MFS-12666		Percentual (FINAM)*	Texto	S	N	Desabilitado

0,0000	Exibe o percentual referente ao Finam até 6% sobre o incentivo fiscal

Tratamento:

Se houver valor nos campos FINAM e Base de Cálculo, exibir o resultado do cálculo abaixo:

(Valor Líquido (FINAM) / Base de Cálculo) x 100

	MFS-12666		TOTAL DE INCENTIVOS		Valor Líquido (Total)*	Texto	S	N	Desabilitado
0,00	Exibe o valor líquido total dos incentivos

Tratamentos: 

Este campo não deve ser habilitado para edição, o mesmo deve ser calculado pelo sistema. 


Tratamento válido a partir da versão 2.0:

Exibir o resultado do cálculo: Valor Liquido (FINOR) + Valor Liquido (FINAM)

	MFS-12666		Percentual (Total)*	Texto	S	N	Desabilitado
0,0000	
Exibe o percentual total utilizado


Tratamentos:

Este campo não deve ser habilitado para edição, o mesmo deve ser calculado pelo sistema. 


Tratamento válido a partir da versão 2.0:

Exibir o resultado do cálculo: Percentual (FINOR) + Percentual (FINAM)

	 MFS-12666		Botões (*)		Confirma	Botão	-	-		Permite que o usuário inclua/altera as informações.

Tratamentos:

 - Aplicar a RNG00010 - Campo Obrigatório
 - Aplicar a RNG00012 - Salvar


Se o valor informado no campo Valor Líquido (FINOR) + Valor Líquido (FINAM)* for maior que o valor informado no campo “Valor Limite 6%, exibir a  mensagem DW00196. 


Tratamento – Cópia e atualização do A00:

Quando se tratar de Forma de Tributação = Lucro Real e Apuração=Anual, ao salvar os valores exibidos na tela, deverá ser copiado para o A00 referente ao registro N615 somente os valores correspondentes aos incentivos fiscais da última apuração existente. 

	MFS-12666		
(*) Não exibir a descrição na tela.
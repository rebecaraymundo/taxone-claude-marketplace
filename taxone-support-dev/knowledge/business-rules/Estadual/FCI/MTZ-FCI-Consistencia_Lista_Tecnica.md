# MTZ-FCI-Consistencia_Lista Tecnica

- **Fonte:** MTZ-FCI-Consistencia_Lista Tecnica.docx
- **Modificado:** 2022-08-29
- **Tamanho:** 85 KB

---

THOMSON REUTERS

Módulo FCI – Relatório de Consistência da Lista Técnica

__Localização__: Menu Estadual, Módulo FCI 🡪 Obrigações 🡪 Relatório de Consistência da Lista Técnica

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS73384

Liliane Videira Assaf

Criação do relatório

08/12/2021

Sumário

[1\.	Introdução	1](#_Toc96611398)

[2\.	Parâmetros da Tela	1](#_Toc96611399)

[3\.	Origem e Recuperação dos Dados	1](#_Toc96611400)

[4\.	Layout e Preenchimento do Relatório	1](#_Toc96611401)

[5\.	Exemplos	1](#_Toc96611402)

# <a id="_Toc96611398"></a>Introdução

A ideia do relatório é verificar se a lista técnica dos produtos \(SAFX16/17/18\) existe a inconsistência de utilizar de um mesmo produto como Acabado e Componente \(insumo ou embalagem\) em sua árvore de produtos\. Isso geraria um loop ao percorrer a árvore de produtos, causando erro na rotina de Cálculo do Conteúdo de Importação do FCI\.

Veja um exemplo de lista técnica com inconsistência:

Esta árvore de produtos possui 3 níveis\. O produto A é um produto Acabado Final e componente do Produto Acabado C:

<a id="_Hlk89794030"></a>			Produto Acabado A \(SAFX16\)

					I                         

                      Insumo 1	| Insumo 2	| Produto Acabado B  \(SAFX17\)

						

						<a id="_Hlk89797190"></a>Produto Acabado B  <a id="_Hlk89795088"></a> <a id="_Hlk89797215"></a>\(SAFX16\)

							|              

				Insumo 1	| Insumo 2	| Produto Acabado C   <a id="_Hlk89793744"></a>\(SAFX17\)

								 Produto Acabado C \(SAFX16\)

									|

							Insumo 1	| Insumo 2	| Produto Acabado A   \(SAFX17\)

Outro exemplo de lista técnica com inconsistência:

Esta árvore de produtos possui 3 níveis\. O produto B é um produto Acabado Intermediário e componente do Produto Acabado C:

			Produto Acabado A \(safx16\)

					I                         

                      Insumo 1	| Insumo 2	| Produto Acabado B      \(SAFX17\)

					

						Produto Acabado B        \(SAFX16\)

							|              

				Insumo 1	| Insumo 2	| Produto Acabado C   \(SAFX17\)

								

								Produto Acabado C   <a id="_Hlk89798508"></a>\(SAFX16\)

										|

							Insumo 1	| Insumo 2	| Produto Acabado B   \(SAFX17\)

Exemplo de lista técnica correta:

			Produto Acabado A \(safx16\)

					I                         

                      Insumo 1	| Insumo 2	| Produto Acabado B      \(SAFX17\)

	

						Produto Acabado B        \(SAFX16\)		

							|   

				Insumo 1	| Insumo 2	| Produto Acabado C   \(SAFX17\)

Produto Acabado C   \(SAFX16\)

									|

							Insumo 1	| Insumo 2	| Insumo 3   \(SAFX17\)

Conceitualmente podemos dizer que o Produto Acabado A é o produto final e os produtos acabados B e C são produtos intermediários utilizados na fabricação do produto final\.

# <a id="_Toc96611399"></a>Parâmetros da Tela 

Período de carga da lista técnica: \[DD/MM/AAAA\] a \[DD/MM/AAAA\]

Estabelecimentos:

<a id="_Hlk89789968"></a>\[ \] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[ \] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[ \] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[ \] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

	

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Período da carga da lista técnica

Data \(DD/MM/AAAA\)

S

S

Neste campo o usuário informará a data inicial e final do período a ser considerado na pesquisa da lista técnica\.

A data inicial deve ser <= à data final\. Caso contrário, será exibida mensagem de erro padrão \(“*A data inicial da lista técnica deve ser igual ou inferior à data final*”\)\.

Estabelecimentos

Alfanumérico

S

S

Neste campo será exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário\. 

__Atenção\!\!__

Todos os registros de estabelecimentos  selecionados na tela, devem ser gerados num único número de processo\. Para isso utilize a opção __MULTISELECT __na package framework ao invés de MULTIPROC\. 

Assim, atenderemos ao requisito de gerarmos um único arquivo excel com todos os estabelecimentos selecionados em tela\.

# <a id="_Toc350763252"></a><a id="_Toc96611400"></a>Origem e Recuperação dos Dados 

__Origem dos Dados__:     SAFX16 \- Tabela da Lista Técnica \(Produto Final\)

                                      SAFX17 \- Tabela da Lista Técnica \(componentes \- insumos\)

                                      SAFX18 \- Tabela da Lista Técnica \(componentes \- embalagens\)

 

__Recuperação dos dados:__

Para cada estabelecimento selecionado em tela será gerado um relatório\.

A partir da tabela mãe \(__SAFX16__\), será realizada a pesquisa dos dados que atendam aos critérios de Empresa, Estabelecimento e Data, considerando o período informado em tela \(campo “Período da carga da lista técnica”\)\. 

Critérios para recuperação das listas técnicas a serem pesquisadas \(SAFX16\):

\- Empresa = Empresa do login

\- Estabelecimento = Estabelecimento em questão

\- Data do Movimento = Deve ser uma data referente ao período informado em tela \(campo “Período da carga da lista técnica”\)

Caso exista mais de um registro na SAFX16 para o mesmo produto, considerar o registro de maior Data de Movimento menor igual a Data Final do período informado em tela\.

Recuperar os dados para a pesquisar a lista técnica do produto:

\- Empresa

\- Estabelecimento

\- Data do Movimento

\- Produto

Para cada lista a ser pesquisada, os componentes serão recuperados nas tabelas “filhas” __SAFX17__ \(Insumos\) e na __SAFX18__ \(Embalagens\)\.

*\(o produto componente corresponde aos campos 06 e 07, tanto na SAFX17 como na SAFX18\)*

O objetivo da pesquisa na lista técnica é verificar se existe algum produto componente \(SAFX17 ou SAFX18\) com o indicador e código iguais ao indicador e código do produto acabado \(final ou intermediário\) \(SAFX16\);

Caso exista, a lista técnica do produto está inconsistente e vamos gravar um registro no relatório em excel, conforme descrito no tópico “Layout e Preenchimento do Relatório”\.

  

__Detalhe importante sobre a pesquisa da lista técnica do produto:__

A pesquisa dos componentes será realizada *nos diversos níveis da árvore do produto*, ou seja, além dos componentes ligados “diretamente” ao produto \(que seria o primeiro nível da árvore\), também serão pesquisados os componentes utilizados na fabricação de subprodutos \(ou produtos intermediários\) que possam ser utilizados na composição do produto\.

Exemplo da árvore de produto em mais de um nível:

Produto XYZ

                                                                          |                                                                                                                                                                                                                                                    

                                                                          |                                                                      

Insumo 1

Insumo 2

Subproduto 1

                                                                                                    |

                                                                                                    |

Insumo 1

Insumo 4

Insumo 5

Insumo 6

Conceito de subproduto \(ou produto intermediário\) para esse relatório 🡪 É um componente do produto final de fabricação própria, e portanto,  também tem a sua composição na SAFX16\. Ele tanto aparece na SAFX16, como um produto fabricado, como na composição de outros produtos, na SAFX17 ou SAFX18\.

__*Apenas*__ as listas identificadas com erro, serão recuperadas e apresentadas no relatório\. 

<a id="_Hlk96610685"></a>

# <a id="_Toc96611401"></a>Layout e Preenchimento do Relatório

Gerar um relatório em formato excel com todos os estabelecimentos selecionados em tela\.

Nomeclatura: Relatorio\_Lista\_Tecnica\_DD\_MM\_AAAA\_DD\_MM\_AAAA\.xlsx

Onde:

DD\_MM\_AAAA: Data Inicial informada na tela

DD\_MM\_AAAA: Data Final informada na tela

Se o número de registros a serem gravados no arquivo ultrapassar o limite do excel \(1milhão de linhas\), quebrar em mais de um arquivo, adicionando ao nome do arquivo um sequencial \(Relatorio\_Lista\_Tecnica\_DD\_MM\_AAAA\_DD\_MM\_AAAA\_1\.xlsx, Relatorio\_Lista\_Tecnica\_DD\_MM\_AAAA\_DD\_MM\_AAAA\_2\.xlsx,\.\.\.\)\. Este tratamento feito no Relatorio de NF p/ CFOP – Formato XLS do Report Fiscal \(ver package REL\_NF\_CFO\_EXCEL\_FPROC \)\.

Preenchimento dos dados:

__Campo__

__Conteúdo__

Empresa

Código da Empresa de login

Estabelecimento

Estabelecimento em questão

Produto Acabado Principal \(ind\./cod\.\)

Indicador e código do produto final \(campos 03 e 04 da SAFX16\)

\(produto acabado nível 1 da árvore de produtos\)

Produto Principal \(descrição\)

Descrição do produto \(campo 04 da SAFX2013\)

Data da Lista Técnica

Data da carga da lista técnica \(campo “05\-Data do Movimento” da SAFX16\)

Rastreio do Produto Acabado Principal

Todos os produtos que compõe a lista técnica do produto principal \(nível 1\), começando pelo principal até o componente inconsistente\.

Componente \(ind\./cod\)

Preencher com o indicador e código do produto componente \(SAFX17 ou SAFX18\) que causou a inconsistência\.

Crítica

Se foi encontrado produto componente \(SAFX17 ou SAFX18\) com o indicador e código iguais ao indicador e código do produto acabado Principal\) \(SAFX16\) \(nivel 1\), então:

    “O componente XXXX possui o mesmo código de um dos produtos fabricados da lista técnica do Produto Principal\. Por favor, verifique todos os níveis da árvore do produto principal, pois o componente XXXX indicado como inconsistente pode estar diretamente ligado ao Produto Principal ou ligado a outro produto, de outro nível, na produção do Produto Principal\.”

Onde o XXXX é o código do componente\.

# <a id="_Toc96611402"></a>Exemplos

Veja dois exemplos de lista técnica com inconsistência:

Exemplo 1:

Esta árvore de produtos possui 3 níveis\. O produto A é um produto Acabado Final e componente do Produto Acabado C:

			Produto Acabado A \(SAFX16\)

					I                         

                      Insumo 1	| Insumo 2	| Produto Acabado B  \(SAFX17\)

						

						Produto Acabado B   \(SAFX16\)

							|              

				Insumo 1	| Insumo 2	| Produto Acabado C   \(SAFX17\)

								 Produto Acabado C \(SAFX16\)

									|

							Insumo 1	| Insumo 2	| Produto Acabado A   \(SAFX17\)

Para o exemplo 1, teríamos o seguinte relatório:

Produto Acabado Principal

Data da Lista Técnica

Rastreio do Produto Acabado Principal

Componente

Crítica

<a id="_Hlk96680376"></a>Produto Acabado A

DD/MM/AAAA

1\-AcabadoA \-\-> 1\-AcabadoB \-\-> 1\-AcabadoC \-\-> 1\-AcabadoA

Produto Acabado A

O componente AcabadoA possui o mesmo código de um dos produtos fabricados da lista técnica do Produto Principal\. Por favor, verifique todos os níveis da árvore do produto principal, pois o componente AcabadoA indicado como inconsistente pode estar diretamente ligado ao Produto Principal ou ligado a outro produto, de outro nível, na produção do Produto Principal

Produto Acabado B

DD/MM/AAAA

1\-AcabadoB \-\-> 1\-AcabadoC \-\-> 1\-AcabadoA \-\-> 1\-AcabadoB

Produto Acabado B

O componente AcabadoB possui o mesmo código de um dos produtos fabricados da lista técnica do Produto Principal\. Por favor, verifique todos os níveis da árvore do produto principal, pois o componente AcabadoB indicado como inconsistente pode estar diretamente ligado ao Produto Principal ou ligado a outro produto, de outro nível, na produção do Produto Principal

Produto Acabado C

DD/MM/AAAA

1\-AcabadoC \-\-> 1\-AcabadoA \-\-> 1\-AcabadoB \-\-> 1\-AcabadoC

Produto Acabado C

O componente AcabadoC possui o mesmo código de um dos produtos fabricados da lista técnica do Produto Principal\. Por favor, verifique todos os níveis da árvore do produto principal, pois o componente AcabadoC indicado como inconsistente pode estar diretamente ligado ao Produto Principal ou ligado a outro produto, de outro nível, na produção do Produto Principal

Exemplo 2:

Esta árvore de produtos possui 3 níveis\. O produto B é um produto Acabado Intermediário e componente do Produto Acabado C:

			Produto Acabado A \(safx16\)

					I                         

                      Insumo 1	| Insumo 2	| Produto Acabado B      \(SAFX17\)

					

						Produto Acabado B        \(SAFX16\)

							|              

				Insumo 1	| Insumo 2	| Produto Acabado C   \(SAFX17\)

								

								Produto Acabado C   \(SAFX16\)

										|

							Insumo 1	| Insumo 2	| Produto Acabado B   \(SAFX17\)

Para o exemplo 2, o seguinte relatório seria apresentado:

Produto Acabado Principal

Data da Lista Técnica

Rastreio do Produto Acabado Principal

Componente

Crítica

Produto Acabado A

DD/MM/AAAA

1\-AcabadoA \-\-> 1\-AcabadoB \-\-> 1\-AcabadoC \-\-> 1\-AcabadoB

Produto Acabado B

O componente AcabadoB possui o mesmo código de um dos produtos fabricados da lista técnica do Produto Principal\. Por favor, verifique todos os níveis da árvore do produto principal, pois o componente AcabadoB indicado como inconsistente pode estar diretamente ligado ao Produto Principal ou ligado a outro produto, de outro nível, na produção do Produto Principal

<a id="_Hlk96682592"></a>Produto Acabado B

DD/MM/AAAA

	1\-AcabadoB \-\-> 1\-AcabadoC \-\-> 1\-AcabadoB

Produto Acabado B

O componente AcabadoB possui o mesmo código de um dos produtos fabricados da lista técnica do Produto Principal\. Por favor, verifique todos os níveis da árvore do produto principal, pois o componente AcabadoB indicado como inconsistente pode estar diretamente ligado ao Produto Principal ou ligado a outro produto, de outro nível, na produção do Produto Principal\.

Produto Acabado C

DD/MM/AAAA

1\-AcabadoC \-\-> 1\-AcabadoB \-\-> 1\-AcabadoC

Produto Acabado C

O componente AcabadoC possui o mesmo código de um dos produtos fabricados da lista técnica do Produto Principal\. Por favor, verifique todos os níveis da árvore do produto principal, pois o componente AcabadoC indicado como inconsistente pode estar diretamente ligado ao Produto Principal ou ligado a outro produto, de outro nível, na produção do Produto Principal\.

= = = = = =

 


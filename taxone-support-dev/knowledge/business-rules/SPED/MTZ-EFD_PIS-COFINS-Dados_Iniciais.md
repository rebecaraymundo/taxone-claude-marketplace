# MTZ-EFD_PIS-COFINS-Dados_Iniciais

> Fonte: MTZ-EFD_PIS-COFINS-Dados_Iniciais.doc

EFD - PIS/PASEP - COFINS – Dados Iniciais 


DOCUMENTO DE REQUISITO

DR	Nome	Descrição	Data Alteração		OS3169-GE	Criação do documento	Tela – Dados Iniciais
	14/03/2012		OS3169-GE25	Alteração do Documento	Adequação da tela para atendimento ao Lucro Presumido	16/03/2012		OS3169-25CDW	Alteração do Documento	Adequação da tela para atendimento ao Lucro Presumido	03/05/2012		OS3169-GE25C	Alteração do Documento	Adequação da tela para atendimento ao Lucro Presumido	03/07/2012		OS3710	Alteração do Documento	Inclusão de um novo parâmetro, para contemplar na EFD-Contribuições as Notas Fiscais (Saídas) de Mercadorias Não Escrituradas.	06/08/2012		OS4097	Alteração do Documento	Inclusão do parâmetro ‘Registro A100, C100, C190, C395, C500, D100 e D500 – Seleção das Operações Geradoras de Créditos’	12/07/2012		OS4165	Alteração do Documento	Inclusão do parâmetro ‘Registro 0145 - Regime de Apuração da Contribuição Previdenciária sobre a Receita Bruta’	30/08/2013		MFS15817	Alteração do Documento	Inclusão de parâmetro na tela de Dados Iniciais para indicar a utilização da parametrização “Cadastro de Conta Contábil (M400/M800)” na geração do arquivo magnético da EFD Contribuições, registros M400 e M800	12/03/2018		MFS29621	Alteração do Documento	Inclusão do registro C600 no parâmetro “Registros A100, C100,C180 e C190– Seleção das Operações Geradoras de Receita”	19/08/2019		
REGRAS DE NEGÓCIO


ATENÇÃO:

NÃO ATUALIZAR ESTE DOCUMENTO!!

O documento matriz da tela de Dados Iniciaisque deve ser mantido está localizado no diretório “Matrizes_de_Tela_EFD_PIS-COFINS”, nomeado por MTZ_Dados_Iniciais.docx.


Cód.		DR		RN01	
Criar uma tela para parametrização de alguns dados gerais que serão necessários para a geração do arquivo. Deverá ser feita inicialmente esta parametrização por estabelecimento, obedecendo à regra de geração centralizada, deve-se parametrizar o Estabelecimento centralizador. 

Localização: Grupo ’! Sped ’! EFD   Escrituração Fiscal Digital - PIS/PASEP-COFINS ’! Parâmetros ( Dados Iniciais
	OS3169-GE		RN02	Configuração adicional dos Parâmetros:

Parâmetro
Conteúdo
Multi-Seleção

Registro 0110
Nome: Incidência Tributária no Período
Conteúdo: Criar lista de valores conforme abaixo

1 – Escrituração de operações com incidência exclusivamente no regime não-cumulativo
2 – Escrituração de operações com incidência exclusivamente no regime cumulativo
3 – Escrituração de operações com incidência nos regimes não-cumulativo e cumulativo
Não

Registro 0110
Nome: Método de Apropriação de Créditos
Conteúdo: Criar lista de valores conforme abaixo

1 – Método de Apropriação Direta
2 – Método de Rateio Proporcional (Receita Bruta)
Não

Registro 0110
Nome: Tipo de Contribuição Apurada no Período
Conteúdo: Criar lista de valores conforme abaixo

1 – Apuração da Contribuição Exclusivamente a Alíquota Básica 
2 – Apuração da Contribuição a Alíquotas Específicas (Diferenciadas e/ou por Unidade de Medida de Produto)
Não

Registro C010
Nome: Indicador da apuração, na escrituração das operações por NF-e e ECF Conteúdo: Criar lista de valores conforme abaixo

1 – Apuração com base nos registros de consolidação das operações por NF-e (C180 e C190) e por ECF (C490)
2 –  Apuração com base no registro individualizado de NF-e (C100 e C170) e de ECF (C400)
Não

Registros  F120 e F130
Nome: Tipo de Apresentação
Conteúdo: Criar lista de valores conforme abaixo

- Geração dos bens de forma individualizada
- Geração por grupos de bens de mesma natureza ou destinação


Não


	OS3169-GE		RN02	Registro 0200
Nome: Utilizar a Descrição Detalhada do Produto
Tipo: CheckBox
Não

Registro 0200
Nome: Substituir o código do Serviço pelo Código da Natureza do Serviço 
Tipo: CheckBox
Não

Registros A100, C100, C180, C190 e C600
Nomes: Data de Emissão e  Data de Lançamento EFD PIS/COFINS
Tipo: Radio Button.

Não

Registros C600,C601 e C605
Nome: Geração com base nas informações da SAFX190 e SAFX191 
Tipo: CheckBox

Não

Registros D600,D601 e D605
Nome: Geração com base nas informações da SAFX161 e SAFX162
Tipo: CheckBox


Não


Registro F100
Nomes: Utilizar a parametrização do Tipo do Documento X CST/Operação/Nat. Base de Crédito e  Utilizar a parametrização da Conta Contábil/Centro de Custo X CST/Operação/Nat. Base de Crédto 
Tipo: Radio Button.

Não

Registro 410 e 810
Nomes: Utilizar a parametrização do Identificador da Natureza da Receita e  Utilizar a parametrização da Natureza da Receita informada no Documento Fiscal/Operação
Tipo: Radio Button.

Não

Registros 0450,A110,C110,C500,D100 e D500
Nomes: Justificar a Direita e  Justificar a Esquerda 
Tipo: Radio Button.

Não 

Registros M200 e M600
Nome: Informar os Descontos/Deuções manualmente, nas telas de Apuração PIS/PASEP e COFINS
Tipo: CheckBox

Não


		RN03	Incluir na tela de ‘Dados Iniciais’, localizada no Módulo: SPED >> EFD – Escrituração Fiscal Digital – PIS/PASEP – COFINS   Menu: Parâmetros,  o parâmetro ‘Manter todos os cadastros centralizados no Estabelecimento Matriz’.
Este parâmetro por default deve estar desmarcado.	OS3543		RN04	Se esta opção for marcada exibir a seguinte mensagem ao usuário: ”Marcando esta opção, se existir na base produtos com o mesmo código, porém em grupos distintos, o mesmo só será gerado uma única vez e embaixo do estabelecimento Matriz.”	OS3543		RN05	Quando o parâmetro estiver marcado, o comportamento do sistema não será alterado.	OS3543		RN06	Se o parâmetro ‘Manter todos os cadastros centralizados no Estabelecimento Matriz’ estiver desmarcado, o sistema deve comparar os cadastros usados pelo estabelecimento matriz e pelas filiais e informar os cadastros embaixo de cada registro 0140, considerando as regras abaixo:
Verificar se o produto que foi movimentado está cadastrado na matriz (usando o critério de comparação: Grupo + Indicador + Código), em caso afirmativo, mostrar abaixo do estabelecimento centralizador (Matriz).
Se o produto que foi movimentado estiver cadastrado apenas pelos estabelecimentos centralizados (ou seja, não está cadastrado no estabelecimento matriz), este produto deve constar abaixo do estabelecimento  em questão e  não na matriz ( usando o critério de comparação: Grupo + Indicador + Código), mas exibindo apenas Indicador + Código no registro 0200. 
Caso exista informações referente aos registros 0150,0190,0205,0206,0208,0400,0450 também deverão ser gerados abaixo do estabelecimento centralizado.
A geração dos registros 0500 e 0600 não devem sofrer alteração. Devem ser gerados SEMPRE abaixo do estabelecimento Centralizador.
IMPORTANTE: Não iremos incluir a exibição do grupo na geração do registro 0200, pois os clientes informam que este campo não faz parte do seu cadastro. Por isso, se o cliente possuir em mais de um estabelecimento, produtos com o mesmo código, porém em grupos distintos o parâmetro ‘Manter todos os cadastros centralizados no Estabelecimento Matriz’, deve estar desmarcado.
	OS3543		RN07	Inclusão do parâmetro ‘Regime de Tributação’, sendo os valores válidos: 1- Lucro Real e 2 -Lucro Presumido	OS3169-GE25		RN08	Inclusão do parâmetro ‘Critério de escrituração e Apuração adotada’, sendo os valores válidos: 
1 – Regime de Caixa – Escrituração consolidada (Registro F500)
2 – Regime de Competência - Escrituração consolidada (Registro F550)
9 – Regime de Competência - Escrituração detalhada, com base nos registros dos Blocos “A”, “C”, “D” e “F”	
	OS3169-GE25		RN09	Caso a opção do parâmetro ‘Regime de Tributação’ seja 2 - Lucro Presumido e o parâmetro ‘Incidência Tributária no Período’, seja igual a ‘2 – Escrituração de operações com incidência exclusivamente no regime cumulativo’, habilitar o parâmetro ‘Critério de escrituração e Apuração adotada’. Caso contrário, o campo ‘Critério de escrituração e Apuração adotada’ deve permanecer desabilitado.
	OS3169-GE25		RN10	O parâmetro ‘Regime de Tributação’ deve ter como default a opção ‘1- Lucro Real’.
	OS3169-GE25		RN11	Na gravação da parametrização da tela de Dados Iniciais, se o usuário marcou a opção de ‘2 -Lucro Presumido’ no parâmetro ‘Regime de Tributação’  e uma das opções  ‘1 – Escrituração de operações com incidência exclusivamente no regime não-cumulativo’ ou ‘3 – Escrituração de operações com incidência nos regimes não-cumulativo e cumulativo’, no parâmetro ‘Incidência Tributária no 
Período’, não gravar o registro e exibir a seguinte mensagem ao usuário: “O Regime de Tributação escolhido está incompatível com a opção informada no parâmetro Incidência Tributária no Período. Favor rever a parametrização”
	OS3169-GE25		RN12	Inclusão do parâmetro ‘Critério do Detalhamento do Registro F525, quando a origem da Receita for Documentos Fiscais’, 	OS3169-25CDW		RN13	O parâmetro ‘Critério do detalhamento do Registro F525, quando a origem da receita for documentos fiscais‘: terá as seguintes opções válidas: 
Clientes
Documento Fiscal
Item Vendido
	OS3169-25CDW		RN14	A opção Documento Fiscal será a default, quando o regime escolhido for Lucro Presumido e Regime Caixa.		OS3169-25CDW		RN15	Se a opção for Lucro Real, o parâmetro ‘‘Critério do detalhamento do Registro F525, quando a origem da receita for documentos fiscais ‘deverá ficar desabilitado e nenhum texto deverá ser exibido.
Se a opção for Lucro Presumido e o Critério de escrituração e Apuração adotada’, for uma das opções: 
2 – Regime de Competência - Escrituração consolidada (Registro F550)
9 – Regime de Competência - Escrituração detalhada, com base nos registros dos Blocos “A”, “C”, “D” e “F”
o parâmetro ‘‘Critério do detalhamento do Registro F525, quando a origem da receita for documentos fiscais ‘deverá ficar desabilitado e nenhum texto deverá ser exibido.
	OS3169-25CDW		RN16	Se a opção for Lucro Presumido é obrigatório o preenchimento do parâmetro ‘Critério de escrituração e Apuração adotada’, caso contrário exibir a seguinte msg ao usuário:  “Favor preencher o Critério de escrituração e Apuração adotada”	OS3169-25CDW		RN17	Retirar do parâmetro”Incidência Tributária no período “ a opção em branco.

Caso este parâmetro não for preenchido, exibir a seguinte msg ao usuário: “Favor preencher a Incidência Tributária no período”.	OS3169-25CDW		RN18	Se o parâmetro ‘Critério do detalhamento do Registro F525, quando a origem da receita for documentos fiscais’ for preenchido com a opção ‘Item Vendido’ deve ser exibido a seguinte msg de alerta ao usuário: “ATENÇÃO: Usando este critério, se existir na base algum documento que foi recebido parcelado, poderá haver diferenças entre o valor da receita informado nos registros F500 e F525.”	OS3169-25CDW		RN19	Renomear o parâmetro ‘Critério do Detalhamento do Registro F525, quando a origem da Receita for Documentos Fiscais’, para ‘Critério do Detalhamento do Registro F525’	OS3169-GE25C		RN20	Incluir o parâmetro ‘Notas Fiscais de Mercadoria Não Escrituradas’ na tela de Dados Iniciais no módulo SPED / EFD – Escrituração Fiscal Digital das Contribuições / Menu: Parâmetros. 

Com a opção : Considerar na EFD-Contribuições, os documentos de saída com classificação ‘7-Notas Fiscais de Mercadoria não escrituradas’, desde que possuam CST´s de PIS e COFINS.	OS3710		RN21	O parâmetro ‘Notas Fiscais de Mercadoria Não Escrituradas’ deve ficar desmarcado por default.	OS3710		RN22	Quando marcado o parâmetro ‘Notas Fiscais de Mercadoria Não Escrituradas’, todas as notas de saída que possuírem na safx07 o campo 12 – cod_class_doc_fis com ‘07’ e que possuírem valores nos campos ‘249 – COD_SIT_PIS’, ‘250 - COD_SIT_COFINS’ (da safx07) ou ‘175- COD_SITUACAO_PIS’ e ‘178 - COD_SITUACAO_COFINS’ (da SAFX08), devem ser consideradas na recuperação dos dados para a geração dos registros (C100,C170,C180,C181,C185,C188,C190,C191,C195,C198,C199,C380,C381,C385,C395,C396,C500,D100,D101,D105,D111,D200,D201,D205,D300,D309,D500,D501,D505,F500,F509,F510,F519,F525,F550,F559,F560,F569), além de gerar os cadastros pertinentes a essas notas (registros 0150,0190,0200,0205,0206,0208,0400,0450,0500 e 0600) da EFD-Contribuições.
	OS3710		RN23	Se desmarcado (parâmetro ‘Notas Fiscais de Mercadoria Não Escrituradas’), nada deve ser alterado, ou seja, as notas de saída com Classificação ‘7 – Notas Fiscais de Mercadoria não Escrituradas’, (campo 12 da safx07), não devem ser consideradas no EFD-Contribuições.
	OS3710		RN24	Incluir o parâmetro ‘Registro A100,C100,C190,C395,C500,D100 e D500 – Seleção das Operações Geradoras de Créditos’ na tela de Dados Iniciais no  Módulo: SPED ( EFD – Escrituração Fiscal Digital – PIS/PASEP/COFINS, Menu: Parâmetros , logo abaixo do parâmetro ‘Registro A100,C100,C180 e C190 – Seleção das Operações Geradoras de Receita’
	OS4097		RN25	O parâmetro ‘Registro A100,C100,C190,C395,C500,D100 e D500 – Seleção das Operações Geradoras de Créditos’ terá o texto:
‘Considerar    EMBED PBrush  mês (es) anterior a data da emissão do documento.’

O list box, terá as opções de 00 à 12 e por default, será gravado 01.

ATENÇÂO: Parâmetro exclusivo para documentos de entrada (Operações Geradoras de Créditos).
	OS4097		RN26	Além do parâmetro acima, iremos manter na recuperação dos documentos, os registros com data de um mês posterior a data da geração do arquivo (com base na data da emissão dos documentos), desde que a data de Lançamento EFD PIS/COFINS esteja preenchida e compreendida no período da geração do meio magnético, ou seja, o range do filtro dos documentos será ‘X meses anterior a data da apuração (conforme novo parâmetro na tela de Dados Iniciais)  + 1 mês posterior (fixo na rotina).

Esta informação será detalhada nos registros impactados pelo parâmetro (A100,C100,C190,C395,C500,D100 e D500).
	OS4097		RN27	Incluir o parâmetro ‘Registro 0145 - Regime de Apuração da Contribuição Previdenciária sobre a Receita Bruta’ na tela de ‘Dados Iniciais’ no Módulo: SPED ( EFD – Escrituração Fiscal Digital – PIS/PASEP/COFINS, Menu: Parâmetros, logo abaixo do parâmetro ‘Registro 0110 – Regime de Apuração da Contrib. Social e de Aprop. de Crédito’	OS4165		RN28	Por default, a opção ‘Gerar o Registro 0145 centralizado no Estabelecimento Matriz’ do parâmetro ‘Registro 0145 - Regime de Apuração da Contribuição Previdenciária sobre a Receita Bruta’ estará marcada.	OS4165		RN29	Se o parâmetro ‘Registro 0145 - Regime de Apuração da Contribuição Previdenciária sobre a Receita Bruta’, estiver desmarcado, será gerado um registro 0145 para cada estabelecimento que possui dados de P100 no período da geração do arquivo da EFD-Contribuições.

Se o parâmetro ‘Registro 0145 - Regime de Apuração da Contribuição Previdenciária sobre a Receita Bruta’, estiver marcado e existir algum registro P100 na base durante o período da geração do arquivo (para o estabelecimento centralizador ou qualquer descentralizado) será gerado um único registro 0145 (embaixo do estabelecimento centralizador) no arquivo da EFD-Contribuições.  

Atenção: Considerar o documento matriz do bloco zero da EFD-Contribuições, para maiores detalhes da geração do registro 0145. 	OS4165		RN30	Registro M400 e M800 – Critério de Identificação da Conta Contábil 
Considerar a parametrização
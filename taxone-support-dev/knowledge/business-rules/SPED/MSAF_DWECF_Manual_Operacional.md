# MSAF_DWECF_Manual_Operacional

> Fonte: MSAF_DWECF_Manual_Operacional.docx





MASTERSAF
ECF - Escrituração Contábil Fiscal (DW)
MANUAL OPERACIONAL



SUMÁRIO

INTRODUÇÃO	2
PUBLICO ALVO	2
LEGISLAÇÃO	3
BLOCOS E REGISTROS DA ECF	3
PARÂMETROS	9
RECUPERAÇÃO DOS VALORES - APURAÇÃO IRPJ/CSLL	10
CRITÉRIOS DE APURAÇÃO	21
INFORMAÇÕES ECF	21
CÓPIA DE ABERTURA EM LOTE	31
ABERTURA DE APURAÇÃO	33
MAPEAMENTO	40
ASSOCIAÇÃO DO PLANO DE CONTAS REFERENCIAL COM O PLANO EMPRESA	40
ASSOCIAÇÃO DA TABELA DINÂMICA COM O PLANO EMPRESA	44
ASSOCIAÇÃO DAS SUBCONTAS CORRELATAS COM O PLANO DA EMPRESA	48
PERFIL DE GERAÇÃO	48
MANUTENÇÃO	50
CONTAS DA PARTE B	50
SALDOS DAS CONTAS DA PARTE B	50
PAT – PERÍODOS ANTERIORES AO DW	51
APURAÇÃO	52
PROCESSAMENTO EM LOTE	52
AJUSTES MANUAIS	56
PERCENTUAIS DE RATEIO DAS ATIVIDADES MISTAS	56
BALANÇO/DRE (BLOCO K)	58
ENTRADA MANUAL DE VALORES	60
LANÇAMENTOS DA PARTE A (M300, M350)	64
LANÇAMENTOS DA PARTE B (M410)	70
LUCRO REAL	74
COMPARATIVO	74
INCENTIVOS FISCAIS	74
FINAN e FINOR	74
PAT	76
DEMONSTRAÇÕES	77
BLOCO V – DECLARAÇÃO DEREX	88
IMPORTAÇÃO	88
MANUTENÇÃO	88
BLOCO W – DECLARAÇÃO PAÍS A PAÍS	90
IMPORTAÇÃO	90
MANUTENÇÃO	90
BLOCO X e Y – INFORMAÇÕES ECONÔMICAS E GERAIS	92
IMPORTAÇÃO	92
MANUTENÇÃO	92
GERAÇÕES	93
ECF	93
RELATÓRIOS	95
CONFERÊNCIA DO LUCRO REAL	95
DEMONSTRAÇÕES	95
LALUR/LACS	95
APURAÇÃO IRPJ/CSLL	95
CONFERÊNCIA DA DECLARAÇÃO PAÍS A PAÍS -BLOCO W	95
CONFERÊNCIA DAS INFORMAÇÕES ECONÔMICAS E GERAIS - BLOCOS X E Y	96
RECUPERAÇÃO DE REGISTROS:	96
INFORMAÇÕES ECF:	96
ABERTURA DE APURAÇÃO:	96
LISTAS DE OPÇÕES:	97
SIGLAS UTILIZADAS NO ECF	98
SUPORTE TÉCNICO	99


## INTRODUÇÃO

O módulo ECF - Escrituração Contábil Fiscal (DW), foi criado com a finalidade de possibilitar a entrega das informações da Escrituração Fiscal Digital do Imposto sobre a Renda e da Contribuição Social sobre o Lucro Líquido da Pessoa Jurídica,que foi instituída pela Instrução Normativa RFB nº. 1.422/2013.
A Escrituração Contábil Fiscal (ECF) substituiu a Declaração de Informações Econômico-Fiscais da Pessoa Jurídica (DIPJ), a partir do ano-calendário 2014, com entrega prevista para o último dia útil do mês de junho do ano posterior ao do período da escrituração no ambiente do Sistema Público de Escrituração Digital (Sped). Portanto, a DIPJ está extinta a partir do ano-calendário 2014.

## PUBLICO ALVO

São obrigadas ao preenchimento da ECF todas as pessoas jurídicas, inclusive imunes e isentas, sejam elas tributadas pelo lucro real, lucro arbitrado ou lucro presumido, exceto:

I - As pessoas jurídicas optantes pelo Regime Especial Unificado de Arrecadação de Tributos e Contribuições devidos pelas Microempresas e Empresas de Pequeno Porte (Simples Nacional), de que trata a Lei Complementar nº 123, de 14 de dezembro de 2006;

II - Os órgãos públicos, às autarquias e às fundações públicas;

III - As pessoas jurídicas que não tenham efetuado qualquer atividade operacional, não operacional, patrimonial ou financeira, inclusive aplicação no mercado financeiro ou de capitais, durante todo o ano-calendário.

Há que se ressaltar que, caso a pessoa jurídica tenha Sociedades em Conta de Participação (SCP), cada SCP deverá preencher e transmitir sua própria ECF, utilizando o CNPJ da pessoa jurídica que é sócia ostensiva e o CNPJ/Código de cada SCP.


## LEGISLAÇÃO

De acordo com Instrução Normativa RFB no 1.422, de 19 de dezembro de 2013, e alterações posteriores – Dispõe sobre a Escrituração Contábil Fiscal (ECF).

- Ato Declaratório Executivo Cofis no 42, de 25 de maio de 2016 – Dispõe sobre o Manual de Orientação do Leiaute da Escrituração Contábil Fiscal (ECF).

## BLOCOS E REGISTROS DA ECF

A estrutura da obrigação consiste em blocos e registros onde o bloco representa o agrupamento das informações e o registros representa o detalhamento das informações agrupadas.
Logo abaixo, segue os blocos e os respectivos registros gerados pela ECF.

Bloco 0 - Abertura e Identificação
- Registro 0000: Abertura do Arquivo Digital e Identificação da Pessoa Jurídica5
- Registro 0001: Abertura do Bloco
- Registro 0010: Abertura do Arquivo Digital e Identificação da Entidade
- Registro 0020: Parâmetros Complementares
- Registro 0021: Parâmetros de Identificação dos Tipos de Programa
- Registro 0030: Dados Cadastrais
- Registro 0035: Identificação das SCP
- Registros 0930: Identificação dos Signatários da ECF
- Registros 0990: Encerramento do Bloco 0
Bloco C - Informações Recuperadas da ECD
- Registro C001: Abertura do Bloco C
- Registro C990: Encerramento do Bloco C
Bloco E- Informações Recuperadas da ECF Anterior e Cálculo Fiscal dos Dados Recuperados da ECD
- Registro E001: Abertura do Bloco E
- Registro E990: Encerramento do Bloco E
Bloco J - Plano de Contas e Mapeamento
- Registro J001: Abertura do Bloco J
- Registro J050: Plano de Contas do Contribuinte
- Registro J051: Plano de Contas Referencial
- Registro J053: Subcontas Correlatas
- Registros J100: Centro de Custos
- Registros J990: Encerramento do Bloco J
Bloco K - Saldos das Contas Contábeis e Referenciais

- Registro K001: Abertura do Bloco K
- Registro K030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário
- Registro K155: Detalhes dos Saldos Contábeis (Depois do Encerramento do Resultado do Período)
- Registro K156: Mapeamento Referencial do Saldo Final
- Registro K355: Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento
- Registro K356: Mapeamento Referencial dos Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento
- Registro K990: Encerramento do Bloco K
Bloco L - Lucro Líquido – Lucro Real
- Registro L001: Abertura do Bloco L
- Registro L030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário
- Registro L100: Balanço Patrimonial
- Registros L200: Método de Avaliação de Estoques
- Registros L210: Informativo de Composição de Custos
- Registros L300: Demonstração do Resultado do Lucro Líquido Fiscal
- Registros L990: Encerramento do Bloco L
Bloco M - e-LALUR e e-LACS – Lucro Real
- Registro M001: Abertura do Bloco M
- Registro M010: IDENTIFICAÇÃO DA CONTA NA PARTE B DO e-LALUR E DO e-LACS
- Registro M030: IDENTIFICAÇÃO DOS PERÍODOs E FORMAS DE APURAÇÃO DO IRPJ E DA CSLL DAS EMPRESAS TRIBUTADAS PELO LUCRO REAL
- Registro M300: Lançamentos da Parte A do e-LALUR
- Registro M305: Conta da Parte B do e-LALUR
- Registro M310: Contas Contábeis Realacionados ao Lançamento da Parte A do e-LALUR
- Registro M312: Números dos Lançamentos Relacionados à Conta Contábil
- Registro M315: Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento
- Registro M350: Lançamentos da Parte A do e-LACS
- Registro M355: Conta da Parte B do e-LACS
- Registro M360: Contas Contábeis Relacionadas ao Lançamento da Parte A do e-Lacs
- Registro M362: Números dos Lançamentos Relacionados à Conta Contábil
- Registro M365: Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento
- Registro M410: Lançamentos na Conta da Parte “B” do E-Lalur E do E-Lacs sem Reflexo na Parte A
- Registro M415: Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento
- Registro M990: Encerramento do Bloco M
Bloco N - Cálculo do IRPJ e da CSLL – Lucro Real
- Registro N001: Abertura do Bloco N
- Registro N030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real
- Registro N500: Base de Cálculo do IRPJ Sobre o Lucro Real Após as Compensações de Prejuízos
- Registro N600: Demonstração do Lucro da Exploração
- Registro N610: Cálculo da Isenção e Redução do Imposto sobre o Lucro Real
- Registro N615: Informações da Base de Cálculo dos Incentivos Fiscais
- Registro N620: Cálculo da IRPJ Mensal por Estimativa
- Registro N630: Cálculo do IRPJ Com Base no Lucro Real
- Registro N650: Base de Cálculo da CSLL Após as Compensações da Base de Cálculo Negativa
- Registro N660: Cálculo da CSLL Mensal por Estimativa
- Registro N670: Cálculo da CSLL Com Base no Lucro Real
- Registro N990: Encerramento do Bloco N
Bloco P - Lucro Presumido
- Registro P001: Abertura do Bloco P
- Registro P030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Presumido
- Registro P100: Balanço Patrimonial
- Registro P130: Demonstração das Receitas Incentivadas do Lucro Presumido
- Registro P150: Demonstrativo do Resultado do Exercício
- Registro P200: Apuração da Base de Cálculo do Lucro Presumido
- Registro P230: Cálculo da Isenção e Redução do Lucro Presumido
- Registro P300: Cálculo do IRPJ com Base no Lucro Presumido
- Registro P400: Apuração da Base de Cálculo da CSLL com Base no Lucro Presumido
- Registro P500: Cálculo da CSLL com Base no Lucro Presumido
- Registro P990: Encerramento do Bloco P
Bloco Q - Livro Caixa
- Registro Q001: Abertura do Bloco Q
- Registro Q100: Demonstrativo do Livro Caixa (FACULTATIVO PARA O ANO-CALENDÁRIO 2015)
- Registros Q990: Encerramento do Bloco Q
Bloco T - Lucro Arbitrado
- Registro T001: Abertura do Bloco T
- Registro T030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Arbitrado
- Registro T120: Apuração da Base de Cálculo do IRPJ com Base no Lucro Arbitrado
- Registro T150: Cálculo do IRPJ com Base no Lucro Arbitrado
- Registro T170: Apuração da Base de Cálculo da CSLL com Base no Lucro Arbitrado
- Registro T181: Cálculo da CSLL com Base no Lucro Arbitrado
- Registro T990: Encerramento do Bloco T
Bloco U - Imunes ou Isentas
- Registro U001: Abertura do Bloco U
- Registro U030: Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Imunes e Isentas
- Registro U100: Balanço Patrimonial
- Registro U150: Demonstração do Resultado
- Registro U180: Cálculo do IRPJ das Empresas Imunes ou Isentas
- Registro U182: Cálculo da CSLL das Empresas Imunes ou Isentas
- Registro U990: Encerramento do Bloco U


Bloco W – Declaração País a País
Registro W001: Abertura do Bloco W
Registro W100: Informações sobre o Grupo Multinacional e a Entidade Declarante – Declaração País-a-País
Registro W200: Declaração País-a-País
Registro W250: Declaração País-a-País – Entidades Integrantes
Registro W300: Observações Adicionais – Declaração País-a-País
Registro W990: Encerramento do Bloco W

Bloco X - Informações Econômicas
- Registro X001: Abertura do Bloco X
- Registro X280: Atividades Incentivadas – PJ em Geral
- Registro X291: Operações com o Exterior – Pessoa Vinculada/Interposta/País com Tributação Favorecida
- Registro X292: Operações com o Exterior – Pessoa Não Vinculada/Não Interposta/País sem Tributação Favorecida
- Registro X300: Operações com o Exterior – Exportações (Entradas de Divisas)
- Registro X310: Operações com o Exterior – Contratantes das Exportações
- Registro X320: Operações com o Exterior – Importações (Saída de Divisas)
- Registro X330: Operações com o Exterior – Contratantes das Importações
- Registro X340: Identificação da Participação no Exterior
- Registro X350: Participações no Exterior – Resultado do Período de Apuração
- Registro X351: Demonstrativo de Rendas Ativas e Passivas
- Registro X352: Demosntrativo de Resultados no Exterior de Coligadas em Regime de Caixa
- Registro X353: Demonstrativo de Consolidação
- Registro X354: Demonstrativo de Prejuízos Acumulados
- Registro X355: Demonstrativo de Rendas Ativas e Passivas
- Registro X356: Demonstrativo de Estrutura Societária
- Registro X390: Origem e Aplicação de Recursos – Imunes e Isentas
- Registros X400: Comércio Eletrônico e Tecnologia da Informação
- Registro X410: Comércio Eletrônico
- Registro X420: Royalties Recebidos ou Pagos a Beneficiários do Brasil e do Exterior
- Registro X430: Rendimentos Relativos a Serviços, Juros e Dividendos Recebidos do Brasil e do Exterior
- Registro X450: Pagamentos/Remessas Relativos a Serviços, Juros e Dividendos Recebidos do Brasil e do Exterior
- Registro X460: Inovação Tecnológica e Desenvolvimento Tecnológico
- Registro X470: Capacitação de Informática e Inclusão Digital
- Registro X480: Repes, Recap, Padis, PATVD, Reidi, Repenec, Reicomp, Retaero, Recine, Resíduos Sólidos, Recopa, Copa do Mundo, Retid, REPNBLRedes, Reif e Olimpíada
Bloco Y - Informações Gerais
- Registro Y001: Abertura do Bloco Y
- Registro Y520: Pagamentos/Recebimentos do Exterior ou de Não Residentes
- Registro Y540: Discriminação da Receita de Vendas dos Estabelecimentos por Atividade Econômica
- Registro Y550: Vendas a Comercial Exportadora com Fim Específico de Exportação
- Registro Y560: Detalhamento das Exportações da Comercial Exportadora
- Registro Y570: Demonstrativo do Imposto de Renda e CSLL Retidos na Fonte
- Registro Y580: Doações a Campanhas Eleitorais
- Registro Y590: Ativos no Exterior
- Registro Y600: Identificação de Sócios ou Titular
- Registro Y611: Rendimentos de Dirigentes, Conselheiros, Sócios  ou Titular
- Registro Y612: Rendimentos de Dirigentes e  Conselheiros, Imunes e Isentas
- Registro Y620: Participações Avaliada pelo Método de Equivalência Patrimonial
- Registro Y630: Fundos/Clubes de Investimento
- Registro Y640: Participações em Consórcios de Empresa
- Registro Y650: Participantes do Consórcio
- Registro Y660: Dados de Sucessoras
- Registro Y665: Demonstrativo das Diferenças na Adoção Inicial
- Registro Y671: Outras Informações
- Registro Y672: Outras Informações (Lucro Presumido ou Lucro Arbitrado)
- Registro Y680: Mês das Informações de Optantes pelo Refis (Lucro Real, Presumido e Arbitrado)
- Registro Y681: Informações de Optantes pelo Refis (Lucro Real, Presumido e Arbitrado)
- Registro Y682: Informações de Optantes pelo Refis - Imunes ou Isentas
- Registro Y690: Informações de Optantes pelo Paes
- Registro Y800: Outras Informações
- Registros Y990: Encerramento do Bloco Y
- Registro Y720: Informações de Períodos Anteriores:
- Registro Y700: Declaração de Informações de Operações Relevantes (DIOR)
- Registro Y710: Tributos vinculados a DIOR
Bloco 9 - Encerramento do Arquivo Digital
- Registro 9001: Abertura do Bloco
- Registro 9900: Registros do Arquivo
- Registro 9990: Encerramento do Bloco
- Registro 9999: Encerramento do Arquivo Digital

## PARÂMETROS

Acesso às telas relacionadas às parametrizações que devem anteceder os cálculos e gerações da obrigação Escrituração Contábil Fiscal (ECF).

Parametrização para a Recomposição dos Saldos Contábeis 

Nessa tela, o usuário irá parametrizar o tipo de apuração e o tipo de encerramento para exportação dos saldos contábeis e dos saldos contábeis por centro de custo via Job Servidor. A partir dessa parametrização, os saldos serão recompostos a partir do mês seguinte ao do definido no encerramento. Serão solicitados os seguintes campos:



Descrição dos campos:

Estabelecimento: Nesse campo serão listados os estabelecimentos que o usuário possui permissão de acesso no módulo Segurança e que estão devidamente licenciados. Os estabelecimentos serão exibidos através do seu Código e Descrição. Por padrão, será exibido o estabelecimento selecionado no Manager. Caso não exista um estabelecimento selecionado, esse campo será exibido em branco. Campo obrigatório de preenchimento.
Apuração: Selecionar o tipo de apuração para a exportação das
tabelas SAFX02 e SAFX80. Serão exibidas as seguintes opções:
    - Anual
    - Trimestral
Encerramento: Selecionar o tipo de encerramento para a exportação das tabelas SAFX02 e SAFX80. Serão exibidas as seguintes opções:
    - Anual
    - Semestral
    - Trimestral
Omitir informação de Centro de Custo em Lançamentos Contábeis e Saldos: Quando selecionada esta opção, na geração do arquivo de Saldos Contábeis (MOV0002) serão desconsiderados os registros da SAFX80 – Saldo por Centro de Custo e o conteúdo do campo de Centro de Custo do arquivo de Lançamentos Contábeis (MOV0001) não será informado.
Replicar para o(s) Estabelecimento(s): Selecionar para qual ou quais estabelecimento(s) a parametrização será replicada.


### RECUPERAÇÃO DOS VALORES - APURAÇÃO IRPJ/CSLL


A funcionalidade Recuperação dos Valores - Apuração IRPJ/CSLL tem como objetivo parametrizar a forma de transporte dos valores das Contas Contábeis para os Registros das Tabelas Dinâmicas, facilitando a automação e servindo de base para a apuração.
Esta parametrização é de uso exclusivo da Forma de Tributação por Lucro Real para os registros do Bloco M, não se aplicando às demais formas.

PRINT da TELA

Descrição dos campos :

Data Inicial: Informar a data inicial da parametrização.
Código: Informar o código da parametrização da recuperação de valores.
Descrição:  Informar a descrição da parametrização da recuperação de valores.
Grupo: :Informar o código qura recuperar as contas contábeis que serão utilizadas na parametrização da recuperação de valores.

A partir da criação de uma parametrização (preenchendo as informações dos campos acima), o usuário poderá Associar uma Conta Contábil, Pesquisar, Adicionar Informação Complementar ou Remover uma Associação.


Associar uma Conta Contábil: Ao selecionar esta opção, serão exibidas todas as contas que estão vigentes no grupo e data inicial  indicados na parametrização,  que possuem as seguintes Naturezas:
- Ativo;
- Passivo;
- Patrimônio Líquido;
- Receita;
- Despesa;
- Custo.

Print da Tela

Na tela acima, pode-se selecionar todas as contas exibidas na grid clicando no botão  “Selecionar Todas” localizado ao lado esquerdo da tela , ou selecionar uma a uma clicando no “check box” ao lado do Código da Conta Contábil. Poderá ser utilizado também a funcionalidade de desmarcar todas as contas através do botão ‘Desmarcar Todas’
Por meio do botão OK, a escolha das Contas Contábeis que deseja parametrizar é confirmada e a mesma é apresentada na Grid de Contas Contábeis da Tela Principal.


Print da Tela

Pesquisar: Permite efetuar uma pesquisa, entre as contas que foram inseridas na Grid de Contas Contábeis da Tela Principal.
Para reexibir todos os dados  após a realização do filtro, deverá ser excluído as informações indicadas na pesquisa.

Adicionar Informação Complementar: Ao selecionar uma ou mais linhas, é possível adicionar informações às contas preenchendo os campos ‘Recuperação de Valores’ e ‘Lançamento de Adição e Exclusão’.

Existem cinco possibilidades para recuperação dos valores: Total de Crédito, Saldo, Movimento, Total de Débito, Lançamentos Contábeis.



Total de Crédito - Ao efetuar o processamento de saldos em lote, o sistema recupera a conta contábil e considera para o cálculo somente o total dos créditos.
Total de Débito - Ao efetuar o processamento em lote - Transcrição dos Valores Empresa para Referenciais Fisco, o sistema recupera a conta contábil e considera para o cálculo somente o total dos Débitos.
Lançamentos Contábeis - Ao efetuar o processamento em lote - Transcrição dos Valores Empresa para Referenciais Fisco o sistema considera apenas o valor dos lançamentos contábeis desprezando o valor de movimento das contas.
Obs.: Para que seja realizada a associação dos lançamentos contábeis durante o processamento, é obrigatória a  seleção da opção  “Associação Automática de Todos os Lançamentos Contábeis (M312 M362)” ou Associação dos Lançamentos Contábeis (M312 M362) informados pela Integração, de acordo com a necessidade. Estas opções estão disponíveis na tela de Processamento em lote. Durante o processamento, caso nenhum lançamento contábil seja identificado tabela para este período, não é gerado valor na linha correspondente à conta  contábil que está associada.

Saldo - O sistema recupera o saldo final para a conta contábil.
Movimento - Ao selecionar a Recuperação por movimento, o sistema efetua o cálculo matemático entre os movimentos de Crédito e Débito recuperando o resultado.
Dependendo da escolha de cada uma das possibilidades da Recuperação de valores, o sistema habilita parâmetros específicos que possibilitam direcionar o resultado do saldo para as contas de Apuração, levando-se em consideração também a natureza da conta.


Exemplo:


- .

Contas com natureza patrimonial e de Resultado não podem ser parametrizadas simultaneamente. Logo, é permitida a seleção simultânea das seguintes naturezas: Ativo, Passivo, Patrimônio Líquido e Outros ou Despesa, Receita e Custo.

Caso nenhuma conta tenha sido parametrizada, por padrão, o sistema assume que todas as contas da Apuração devem ser processadas por saldo, ou seja, utilizará o Saldo Final importado.
Para melhor entendimento, veja abaixo alguns exemplos de utilização dos parâmetros e forma de lançamentos de Adições, exclusão no eLalur (M300A) e eLacs (M350A), a partir das contas patrimoniais e contas de resultado:

CENÁRIO - CONTAS PATRIMONIAIS
- Parâmetro em Contas Patrimoniais

Opção um lançamento (de acordo com o Movimento de todas as Contas).
- Lançamentos de Adições e exclusão no eLalur (M300A) e eLacs (M350A).



Lançamentos de Adições e exclusão no eLalur (M300A) e eLacs (M350A).

- Contas Patrimoniais: Dois lançamentos (Movimento de Contas a Crédito na Adição e Movimento de Contas a Débito na Exclusão).



Lançamentos de Adições e exclusão no eLalur (M300A) e eLacs (M350A)

- Contas Patrimoniais: Dois Lançamentos (Total de Crédito de todas as Contas na Adição e Total de Débito de todas as Contas na Exclusão).


- Contas Patrimoniais: Associar Lançamentos Contábeis (Lançamentos a Crédito na Adição e Lançamentos e Débito na Exclusão).


- Contas Patrimoniais: Associar Lançamentos Contábeis (Um Lançamento Consolidando todos os Lançamentos Contábeis).

Parametrização a partir das Contas de Resultado

- Exemplos práticos do comportamento do produto, para os lançamentos de Adições e exclusão no eLalur (M300A) e eLacs (M350A) utilizando contas patrimoniais e contas de resultado:


Contas de Resultado: Opção Um lançamento (de acordo com o Movimento de todas as Contas).


- Contas de Resultado: Opção Dois lançamentos (Movimento de Contas a Débito na Adição e Movimento de Contas a Crédito na Exclusão).



- Contas de Resultado: Opção Dois Lançamentos (Total de Débito de todas as Contas na Adição e Total de Crédito de todas as Contas na Exclusão).


Associar Lançamentos Automáticos – Contas de Resultados



Associar Lançamentos Automáticos – Contas de Resultados

- Opção Associar Lançamentos Contábeis (Um Lançamento com resultado do Movimento de todos os Lançamentos Contábeis).




Remover Associação: Se o usuário marcar o check-box ao lado da conta contábil , na grid da tela Principal e acionar o botão Remover Associação, os registros marcados serão removidos da parametrização.





### CRITÉRIOS DE APURAÇÃO


INFORMAÇÕES ECF

A tela de ‘Informações ECF’ corresponde ao cadastro responsável por fornecer as informações específicas da Empresa, necessárias à entrega da Obrigação SPED ECF, como por exemplo, Qualificação da Pessoa Jurídica, Forma de Tributação, Signatários, parâmetros para a geração da Obrigação entre outras.
Inserir print

Descrição dos campos

Estabelecimento: Selecionar/Informar o estabelecimento que entregará a obrigação.
Exercício: Selecionar/informar o exercício que se refere os dados que serão entregues pela  obrigação.
Data Inicial: Selecionar/informar data de início do período de apuração independentemente de situação especial.
Versão: Informa a versão do layout que será utilizada. Esta versão é compatível com a data inicial da parametrização. Será disponibilizado as opções, conforme regra Versão, somente após o preenchimento do campo data Inicial.
Este campo é de preenchimento obrigatório.
Associação Tabela Dinâmica com o Plano Empresa: Informar a associação da tabela dinâmica que será utilizada para o processamento das informações desta escrituração.
Associação do Plano Referencial com o Plano Empresa: Informar a associação do plano  referencial que será utilizada para o processamento das informações desta escrituração.
Perfil de Geração do Arquivo - Informar Perfil adotado para a Geração do Arquivo ECF.
Obs.: Este campo é obrigatório para a geração do arquivo ECF




ABA PARÂMETROS GERAIS


Inserir print
Tipo da ECF - Informar se a Empresa participa de Sociedade em conta de participação (SCP).
Natureza Jurídica - Selecionar o Código da Natureza Jurídica (Taces 49).
Descrição da Natureza Jurídica: Exibe a Descrição da Natureza Jurídica selecionada.
- Forma de Tributação - Selecionar/Informar a forma de tributação. A lista para seleção das opções é exibida conforme a seguir:- Lucro Real, Lucro Presumido, Lucro Arbitrado.
- Imune de IRPJ
- - Isento de IRPJ
- Apuração - Selecionar/informar a forma de apuração. A lista para seleção das opções é exibida conforme a seguir:
- - Trimestral
- Anual
Tipo de Entidade - Selecionar/Informar o tipo de entidade quando se tratar de empresas Imunes ou Isentas. A lista para seleção das opções é exibida conforme a seguir:

- Assistência social;
- Educacional;
- Sindicato dos Trabalhadores;
- Associação Civil;
- Cultural;
- Entidade Fechada de Previdência Complementar;
- Filantrópica;
- Sindicato;
- Recreativa;
- Científica;
- Associação de Poupança e Empréstimo;
- Entidade Aberta de Previdência Complementar (Sem Fins Lucrativos);
- FIFA e Entidades Relacionadas;
- CIO e Entidades Relacionadas;
- Partidos Políticos;
- Outras;
Qualificação da Pessoa Jurídica - Selecionar a qualificação da pessoa jurídica.  A lista para seleção das opções é exibida confome a seguir:
- PJ em Geral;
- PJ Componente do Sistema Financeiro;
- Sociedades Seguradoras de Capitalização ou Entidade de Previdência Complementar.
Apuração do IRPJ- Selecionar a forma de apuração do IRPJ. A lista para seleção das opções é exibida conforme a seguir:
- Trimestral;
- - Anual;
- - Desobrigada.
Apuração da CSLL - Selecionar a forma de apuração do IRPJ. A lista para seleção das opções é exibida conforme a seguir:- Trimestral;
- - Anual;
- - Desobrigada.
Escrituração - Selecionar a forma de escrituração. A lista para seleção  das opções é exibida conforme a seguir:
- Livro Caixa (Lucro Presumido) ou Sem Escrituração (Imunes ou Isentas);
- Contábil (Lucro Presumido, Imunes ou Isentas);
- Não se aplica.

SIGNATÁRIOS
Signatário Contador

CPF: Selecionar/informar o CPF do Contador responsável pela escrituração.
Código: Visualização do código atribuído ao contador responsável pela escrituração.
Nome do Responsável: Visualização do nome do contador responsável pela escrituração.
Qualificação do Assinante: Visualização da qualificação do assinante da escrituração.
Inscrição do Contabilista: Informar número da Inscrição do Contador/Contabilista.

Signatário Outros

CPF: Selecionar/informar o CPF do Contador responsável pela escrituração.
Código: Visualização do código atribuído ao contador responsável pela escrituração.
Nome do Responsável: Visualização do nome do contador responsável pela escrituração.
Qualificação do Assinante: Selecionar/Informar a qualificação do assinante para geração do ECF. A lista para seleção  das opções é exibida conforme a seguir:- Diretor;
- Conselheiro de Administração;
- Administrador;
- Administrador do Grupo;
- Administrador de Sociedade Filiada;
- Administrador Judicial – Pessoa Física;
- Administrador Judicial – Pessoa Jurídica - Profissional Responsável;
- Administrador Judicial/Gestor;
- Gestor Judicial;
- Procurador;
- Inventariante;
- Liquidante;
- Interventor;
- Titular Pessoa Física;
- Empresário;
- Outros.
LANÇAMENTO DE ENCERRAMENTO (BLOCO K)

Permite informar a Conta Contábil e o Centro de Custo de encerramento virtual do Bloco K.




Conta Contábil - Selecionar/informar a conta para lançamento automático do sistema no Bloco K.
Obs.: Uma conta de Patrimônio Líquido deve ser informada para fechamento virtual, quando houver divergência entre o Ativo e o Passivo.
Desc. da Conta Contábil - Visualização da Conta de Patrimônio Líquido para lançamento do Bloco K.
Cód. do Centro de Custo - Selecionar/informar o centro de custo para lançamento do Bloco K.
Des. do Centro de Custo - Visualização do centro de custo para lançamento do Bloco K.
ABA LALUR E LACS
Descrição dos campos

INFORMAÇÕES PARA A CRIAÇÃO DO LANÇAMENTO NO EXERCÍCIO  - CONTAS DA PARTE B

Grupo – Selecionar/Informar o grupo que a conta da parte B foi cadastrado. Este grupo será considerado como filtro para o preenchimento dos campos citados abaixo de Conta da Parte B.

LANÇAMENTO DE PREJUÍZO
Atividade Geral
Conta da Parte B - Selecionar/informar uma conta que está cadastrada no grupo selecionado e que está vigente na data inicial da escrituração,para lançamento prejuízo do exercício da atividade geral. Formato: Código  - Descrição da Conta.
Atividade Rural
Conta da Parte B - Selecionar/informar uma conta que está cadastrada no grupo selecionado e que está vigente na data inicial da escrituração, para lançamento de prejuízo do exercício da atividade rural. Formato: Código  - Descrição da Conta.

Lançamento de Base Negativa
Atividade Geral
Conta da Parte B - Selecionar/informar uma conta que está cadastrada no grupo selecionado e que está vigente na data inicial da escrituração, para lançamento da Base de Cálculo Negativa da CSLL da atividade geral. Formato: Código  - Descrição da Conta.
Atividade Rural
Cód. da Conta da Parte B - Selecionar/informar uma conta que está cadastrada no grupo selecionado e que está vigente na data inicial da escrituração, para lançamento da Base de Cálculo Negativa da CSLL da atividade rural. Formato: Código  - Descrição da Conta.

Criar Ajustes Mensalmente de  Compensação de Prejuízos e de Base Negativa de Períodos Anteriores- Ao marcar esta opção,  a compensação será aplicada igualmente  tanto para o Imposto de Renda quanto para a Contribuição Social. Se  desmarcada o sistema, exibe a compensação no último mês do período de apuração, ou seja, Anualmente A12 ou Trimestralmente T1, T2, T3, T4.

Histórico Padrão do Lançamento da Parte A - Informar o histórico padrão do lançamento da Parte A, a ser considerado quando for realizado um novo processamento em lote. A parametrização realizada nos campos Cód. do Registro e/ou Incluir Lançamento Automático com Relacionamento  substitui o histórico padrão informado durante a rotina de Cálculo dos Registros e Fórmulas no Processamento em Lote.



ABA PARÂMETROS COMPLEMENTARES

Os campos desta tela servem à parametrização complementar, abaixo estão disponíveis as informações a serem disponilizadas mediante a seleção:

Inserir print
Descrição dos campos

PJ Sujeita à Alíquota da CSLL: Informa se a PJ é sujeita às alíquotas da CSLL de 9%, 17% ou 20%.
Atividade Rural: Informa se possui atividade rural.
Lucro da Exploração: Informa se possui lucro da exploração.
Administradora de Fundos e Clubes de Investimento: Informa se possui administradora de fundos e clubes de investimento.
Participações em Consórcios de Empresas: Informa se possui participações em consórcios de empresas.
Operações com o Exterior: Informa se possui operações com o exterior.
Rendimentos Relativos a Serviços, Juros e Dividendos Recebidos do Brasil e do Exterior: Ao Informa se possui rendimentos relativos a serviços, juros e dividendos recebidos do Brasil e do exterior.
Pagamentos ao Exterior ou a Não Residentes: Informa se possui pagamentos ao exterior ou a não residentes.
Ativos no Exterior: Informa se possui ativos no exterior.
Royalties Recebidos do Brasil e do Exterior: Informa se possui royalties recebidos do Brasil e do exterior.
Pagamentos ou Remessas a Titulo de Serviços, Juros e Dividendos a Beneficiários do Brasil e do Exterior: Informa se possui pagamentos ou remessas a titulo de serviços, juros e dividendos a beneficiários do Brasil e do exterior.
Rendimentos do Exterior ou de Não Residentes: Informa se possui rendimentos do exterior ou de não residentes.
Royalties Pagos a Beneficiários do Brasil e do Exterior: Informa se possuem royalties pagos os beneficiários do Brasil e do exterior.
Participações no Exterior: Informa se possui participações no exterior.
Operações com Pessoa Vinculada/Interposta Pessoa / País com Tributação Favorecida: Informa se possui operações com pessoa vinculada/interposta pessoa / país com tributação favorecida.
PJ Enquadrada nos artigos 48 ou 49 da IN RFB no 1.312/2012: Informa  se o estabelecimento está enquadrado nos artigos 48 ou 49 da IN RFB no 1.312/2012.
Isenção e Redução do Imposto para Lucro Presumido: Informa se possui isenção e redução do imposto para lucro presumido.
FINOR/FINAM/FUNRES: Quando selecionado, o campo informa se possui FINOR/FINAM/FUNRES.
Doações a Campanhas Eleitorais: Informa se possui doações a campanhas eleitorais.
Participação Permanente em Coligadas ou Controladas: Informa se possui participação permanente em coligadas ou controladas.
PJ Efetuou Vendas a Empresa Comercial Exportadora com Fim Específico de Exportação: Informa se o PJ efetuou vendas a empresa comercial exportadora com fim específico de exportação.
PJ Comercial Exportadora: Informa se é PJ comercial exportadora.
Indicador de optante pelo PAES: Informa se é optante pelo PAES.
Indicador de optante pelo REFIS: Informa se é optante pelo REFIS.
Comércio Eletrônico e Tecnologia da Informação: Informa se possui comércio eletrônico e tecnologia da informação.
Inovação Tecnológica e Desenvolvimento Tecnológico: Informa se possui inovação tecnológica e desenvolvimento tecnológico.
Capacitação de Informática e Inclusão Digital: Informa se possui capacitação de informática e inclusão digital.
PJ Habilitada no Repes, Recap, Padis: Informa se a PJ é habilitada no REPES, RECAP e/ou PADIS. A partir da versão 3.00, quando selecionado, exibe a aba Parâmetros dos Tipos de Programa possibilitando detalhar os tipos de programas utilizados.
Pólo Industrial de Manaus e Amazônia Ocidental: Informa se possui pólo industrial de Manaus e Amazônia Ocidental.
Zonas de Processamento de Exportação: Informa se possui zonas de processamento de exportação.
Áreas de Livre Comércio: Informa se possui áreas de livre comércio.
Optante pela extinção do RTT no Ano-Calendário 2014: Informa se o estabelecimento é Optante pela extinção do RTT no Ano-Calendário 2014.
Existem diferenças entre a Contabilidade Societária e Fcont: Demonstra que no ano base de apuração houve diferenças entre a Contabilidade Societária e o FCONT.
Entidade Integrante de Grupo Multinacional: Informa se faz parte de um grupo multinacional. Este campo está disponível a partir da versão 3.00.
Declaração sobre utilização dos recursos em moeda estrangeira decorrentes do recebimento de exportações (DEREX): Informa se há declaração sobre utilização dos recursos em moeda estrangeira decorrentes do recebimento de exportações (DEREX). Este campo está disponível a partir da versão 4.00.


ABA  PARÂMETROS IDENTIFICADORES DOS TIPOS DE PROGRAMAS

Os campos desta tela servem à parametrização detalhada dos tipos de programas utilizados a partir da versão 3.00, abaixo estão disponíveis as informações a serem disponilizadas mediante a seleção:



PRINT TELA
Descrição dos campos:

Regime Especial de Tributação para a Plataforma de Exportação de Serviços de Tecnologia da Informação (Repes): Informa se o programa  é utilizado no ano calendário.
Regime Especial de  Aquisição  de  Bens   de  Capital  para  Empresas Exportadoras (Recap): Informa se o programa  é utilizado no ano calendário.
Programa de Apoio ao Desenvolvimento Tecnológico da Indústria de Semicondutores (Padis): Informa se o programa  é utilizado no ano calendário.
Programa de Apoio ao Des envolvimento Tecnológico da Indústria de Equipamentos para TV Digital (PATVD): Informa se o programa  é utilizado no ano calendário.
Regime Especial de Incentivos para o Desenvolvimento da Infraestrutura (Reidi): Informa se o programa  é utilizado no ano calendário.
Regime Especial de Incentivos para  o  Desenvolvimento da Infraestrutura  da  Indústria  Petrolífera  das  Regiões  Norte,  Nordeste e Centro-Oeste (Repenec): Informa se o programa  é utilizado no ano calendário.
Regime Especial de Incentivo a Computadores para Uso Educacional (Reicomp): Informa se o programa  é utilizado no ano calendário.
Regime Especial para a Indústria Aeronáutica Brasileira (Retaero): Informa se o programa  é utilizado no ano calendário.
Regime Especial de Tributação para Des envolvimento da Atividade de Exibição Cinematográfica (Recine): Informa se o programa  é utilizado no ano calendário.
Estabelecimentos industriais façam jus a crédito presumido do  IPI na aquisição de resíduos  sólidos, de que trata a Lei nº 12.375, de  30 de dezembro de 2010: Informa se o programa  é utilizado no ano calendário.
Regime Especial de Tributação para construção, ampliação, reforma ou modernização de estádios de futebol (Recopa): Informa se o programa  é utilizado no ano calendário.
Habilitada para fins de fruição dos benefícios fis cais, não abrangidos na alínea   anterior,   relativos   à   realização,   no   Brasil,   da   Copa   das Confederações FIFA 2013 e da Copa do Mundo FIFA 2014, de que trata a Lei nº 12.350, de 2010 regulamentada pelo Decreto nº 7.578, e 11 de outubro de 2011: Informa se o programa  é utilizado no ano calendário.
Regime Especial Tributário para a Indústria de Defesa (Retid): Informa se o programa  é utilizado no ano calendário.
Regime Especial de Tributação  do Programa Nacional de Banda Larga para Implantação de Redes de Telecomunicações (REPNBL-Redes ): Informa se o programa  é utilizado no ano calendário.
Regime Especial de Incentivo ao Des envolvimento da Infraestrutura da Indústria de Fertilizantes (REIF): Informa se o programa  é utilizado no ano calendário.
Habilitada para fins de fruição   dos  benefícios   fiscais,  relativos   à realização,   no  Brasil,  dos  Jogos   Olímpicos   de   2016  e  dos  Jogos Paraolímpicos de 2016, de que trata a Lei nº 12.780, de 2013: Informa se o programa  é utilizado no ano calendário.

CÓPIA DE ABERTURA EM LOTE

O objetivo desta tela é  realizar a cópia de uma abertura da apuração para  períodos posteriores e Estabelecimentos diversos .

A tela possui duas partes para preenchimento:
- Recuperar a Abertura de Origem
- Informar para quais Informações ECF (destino), serão criadas as aberturas

Descrição dos campos:

Apuração :  Selecionar/informar   o tipo de apuração. Opções Válidas: Anual e Trimestral

Forma de Tributação: Selecionar/Informar a forma de tributação da abertura de origem. Opções Válidas: Lucro Real,  ou Arbitrado.

Período de Apuração de Origem: Selecionar qual a abertura de apuração de Origem, que será utilizada como referencia de cópia. (Formato do campo: Estabelecimento – CGC-Exercício-Data Inicial da Informação ECF - Código da Abertura  - Descrição da abertura)
Atenção: Só serão recuperadas abertura de apuração cujo campo “Situação Especial no Período” seja igual a “Não” e o período da apuração seja diferente de A00.
Períodos e Estabelecimentos de Destino:

- Inicial: Informa o período inicial que a cópia será realizada.(Código da Abertura- Descrição)
- Final: Informa o período final que a cópia será realizada.(Código da Abertura- Descrição)

- Sobrepor aberturas existentes com status “Apuração em Aberto”“ – Quando marcado, se uma abertura da apuração for identificada no período em que a cópia está sendo realizada, o conteúdo existente será sobreposto.

- Informações ECF: Permite selecionar para quais informações ECF, serão realizadas as cópias das aberturas.



ABERTURA DE APURAÇÃO

Para que a Apuração do IRPJ e da CSLL possa ser feita, é necessário que para cada escrituração seja criada uma abertura da apuração.
A Abertura da Apuração possibilita o processamento períodico dos períodos além de prover o controle dos períodos que estão sendo processados.
Nesta tela, as escriturações cadastradas na tela Informações ECF são exibidas automaticamente  na tela de Pesquisa ( botão Abre), por isso a tela não possui a ação “Novo” habilitada, sendo possível inciar as parametrizações somente pela ação “Adicionar Apuração”.




Dados Gerais :
Recupera os dados de uma Informação ECF.


Descrição dos campos

Status – Visualização do status da apuração. O status exibido está diretamente relacionado a execução dos processos disponíveis na tela Processamento em Lote, podendo também está relacionado a ajustes manuais realizados no sistema após a execução do processamento em lote.
Neste campo, poderá ser visualizado os seguintes status:
Apuração em Aberto – Quando exibido, indica que existe um período cadastrado que ainda não passou pelo processamento em lote.
Importação de Saldos Realizada - Quando exibido, indica que o período passou pela rotina de Transcrição dos Valores Empresa para Referenciais Fisco. Neste status é possível visualizar valores na tela Lucro Real.
Aguardando Alteração Manual -  Quando exibido, indica que  na funcionalidade relacionada ao Bloco K, foram encontradas divergências e será necessário realizar o rateio dos valores identificados durante o processamento em lote.
Alteração Manual Realizada -  Quando exibido, indica que ajustes manuais foram realizados no sistema. Funcionalidades sujeitas a tal status:
- Entrada Manual de Valores
- Lançamentos da Parte A (M300, M350)
- Ajuste Manual do Balanço/DRE (Bloco K)
Cálculo Realizado - Quando exibido, indica que o processamento do período  passou por todas as etapas do processamento e está concluída. Neste status, a tela Lucro Real referente a Demonstração dos Resultados será atualizada devido a aplicação das fórmulas das linhas das tabelas dinâmicas.
necessárias e passou que ainda não passou pelo processamento em lote.
Reapurar - Quando exibido, indica que a abertura  da apuração finalizada, ou seja, possui o status Calculo Realizado e necessita de ajustes  para realizar algum ajuste no sistema onde será necessário realizar um novo processamento em lote.  Este status é manualmente alterado por meio do botão Ajustar Apuração.

Nota 1:  O status ‘Reapurar’ possibilita que informações sejam alteradas no sistema. Neste status, nenhuma informação existente no sistema é  apagada por isso, qualquer processo disponível na tela Processamento em Lote pode ser realizado.
Nota 2: Quando o status de uma Abertura da Apuração for alterado para ‘Reapurar’, recomendamos realizar a o Processamento em Lote com a rotina de Transcrição dos Valores Empresa para Referenciais Fisco.

Forma de Tributação – Vizualização da Forma de Tributação da Abertura de Apuração.

Período de Apuração – Vizualização do período disponível para apuração. (este campo é preenchido automaticamente pelo sistema, considerando a informação de data inicial da Informação ECF e a partir da segunda abertura, com base, na data inicial da abertura anterior.

Situação Especial no Período – Visualização da ocorrência de situação especial no período. Opções Válidas: Sim/Não

- Tipo da Situação Especial – Visualização do tipo da situação especial.   Opções Válidas:
- Extinção
- Fusão
- Incorporação \ Incorporada
- Incorporação \ Incorporadora
- Cisão Total
- Cisão Parcial
- Transformação
- Desenquadramento de Imune / Isenta
- Inclusão no Simples Nacional
Data do Evento – Visualiza   a data da situação especial.

Patrimônio Remanescente em Caso de Cisão (%) – Visualiza  o  percentual do patrimônio remanescente de cisão.
Data Inicial: Visualização da data inicial da abertura da apuração.




Botões de Ação:

Pesquisar: Permite ao usuário pesquisar um registro de abertura de apuração. A pesquisa por ser feita pelos campos Período de Apuração, Forma de Tributação, Situação Especialno Período, Tipo da Situação Especial, Data do Evendo, Data Inicial ou Status.

Adicionar Apuração: Permite ao usuário adicionar uma abertura de apuração. Apenas será possível adicionar uma apuração se a apuração anterior possuir o status de ‘Cálculo Realizado’
Campos que serão exibidos na tela:
Status: Este campo é exibido desabilitado.
Forma de Tributação: Permite ao usuário informar a forma de tributação utilizada no período da abertura.
Lista de Opções Válidas:
Lucro Real,
Lucro Presumido,
Lucro Arbitrado
Se na tela de Informações ECF, os campos Forma de Tributação = ‘Lucro Real, Lucro Presumido, Lucro Arbitrado’ e Apuração = ‘Anual’:
A partir da primeira apuração:
- Apenas as opções ‘Lucro Real’, ’Lucro Presumido’ e ‘Lucro Arbitrado’, devem ficar disponíveis. 
 A partir da segunda apuração, verificar período anterior:
- A partir do momento que existir uma abertura de apuração com a opção “Lucro Real”, nas demais aberturas do exercício apenas as opções “Lucro Real” e “Lucro Arbitrado” devem ficar disponíveis. Não é permitido fazer abertura de apuração de Lucro Presumido após uma abertura com forma de Lucro Real. 
- Se existir uma abertura com forma de tributação igual a “Lucro Real” ou “Lucro Arbitrado” e a apuração for “Anual”, só pode ser indicado uma troca de forma de tributação, no início de um novo trimestre, ou seja, a mudança de tributação pode ocorrer entre os trimestres, mas não, entre os meses do trimestre.
-Se a primeira abertura do exercício for preenchida com “Lucro Arbitrado” ou “Lucro Presumido”, apenas as opções “Lucro Presumido”, “Lucro Real” e “Lucro Arbitrado” devem ficar disponíveis.

Apuração = Trimestral:
A partir da primeira apuração:
- Se o registro recuperado na tela de Informações ECF, estiver cadastrado com a opção ‘Lucro Real, Lucro Presumido, Lucro Arbitrado’ e a apuração for “Trimestral”, apenas as opções ‘Lucro Real’, ’Lucro Presumido’ e ‘Lucro Arbitrado’, devem ficar disponíveis. 
A partir da segunda apuração:
- Se a primeira abertura do exercício for preenchida com “Lucro Real” e apuração for “Trimestral”, nas demais aberturas do exercício apenas as opções “Lucro Real” e “Lucro Arbitrado” devem ficar disponíveis. Ou seja, não é permitido fazer abertura de apuração de lucro presumido após o lucro real. 

Forma de Tributação = ‘Imune de IRPJ’ ou ‘Isento do IRPJ’:
Para todas as apurações:
-Se o registro recuperado na tela de Informações ECF, estiver cadastrado com uma das opções ‘Imune de IRPJ’ ou ‘Isento do IRPJ’, o campo deve ser preenchido automaticamente, com as mesmas opções e o campo deve ficar desabilitado.


Período de Apuração – Este campo é preenchido automaticamente pelo sistema e não será permitida alteração desta informação pelo usuário.

Situação Especial no Período – Indica se há ocorrência de situação especial no período. Opções Válidas: Sim/Não

- Tipo da Situação Especial – Deve ser informado o tipo da situação especial.  Este campo só é habilitado se o campo ‘Situação Especial no Período’ estiver preenchido com ‘Sim’.
- Opções Válidas:
- Extinção
- Fusão
- Incorporação \ Incorporada
- Incorporação \ Incorporadora
- Cisão Total
- Cisão Parcial
- Transformação
- Desenquadramento de Imune / Isenta
- Inclusão no Simples Nacional
Data do Evento – Deve ser informada  a data da situação especial, quando o campo ‘Situação Especial no Período’ estiver preenchido com ‘Sim’.

Patrimônio Remanescente em Caso de Cisão (%) – Deve ser informado o  percentual do patrimônio remanescente de cisão.  Este campo ficará habilitado se o campo ‘Tipo da Situação Especial’ estiver preenchido com Cisão Parcial

Data Inicial: Visualização da data inicial da abertura da apuração. Este campo é preenchido automaticamente pelo sistema e não será permitida alteração desta informação pelo usuário.
Data Final: Visualização da data final da abertura da apuração. Este campo é preenchido automaticamente pelo sistema e não será permitida alteração desta informação pelo usuário.

Tipo de Receita: Possibilita a seleção da forma de apuração do lucro (somente para apuração do Lucro Real Anual). Exibe as abas de acordo com as opções:
- Receita Bruta
- Balanço Suspensão ou Redução
- Comparativo

Receita Bruta - Processa o Cálculo dos Impostos e atualiza as telas de Demonstração de resultados apenas considerando a receita bruta.

Balanço Suspensão ou Redução - Processa o Calculo dos Impostos e atualiza as telas de demonstração de resultados apenas considerando o Balanço Suspensão ou Redução.

Comparativo - Quando esta opção é selecionada após o processo de Cálculos dos Registros e Fórmulas no processamento em lote,  valor do IRPJ e da CSLL na visão Receita Bruta e na visão Balanço de Suspensão ou Redução são disponibilizados  na tela Comparativo, permitindo a escolha da melhor opção entre os tipos de receita .

Considerar automaticamente o menor valor de imposto no comparativo - Quando esta opção é selecionada após o processo de Cálculos dos Registros e Fórmulas no processamento em lote, o sistema escolhe automaticamente  o tipo de receita que possui o menor valor. Essa parametrização afeta diretamente os valores exibidos nas telas de demonstraçao do resultado.

Tipo de Método de Avaliação do Estoque – Selecionar/informar   o método de avaliação do custo do Estoque Empresa. Este campo é de utilização exclusiva para o registro L210.

Contas da Parte A
Nota: As opções de seleção existentes nesta tela, devem ser utilizadas apenas quando a forma de tributação for Lucro Real.

Fixar  saldo inicial na linha do M300 e Fixar  saldo inicial na linha do M350 – Quando
estiverem marcados, o sistema permite a seleção dos saldos iniciais das contas de natureza patrimonial que possuem associação com as linhas de reversão de saldo dos registros M300 - Lançamentos da Parte A do e-Lalur e M350 - Lançamentos da Parte A do e-Lacs.
Para apuração anual, será fixado o  saldo inicial de Janeiro (ou primeiro período no caso de situações especiais)
Para apuração trimestral, será fixado o saldo inicial do trimestre.
Contas da Parte B

Efetuar Ajuste na Conta da Parte B – Quando estiver marcado, cria automaticamente um ajuste na parte B. Este parâmetro funciona com a Associaçao das Contas da Parte B com as Contas da Parte A. Os ajustes referente as contas contábeis que foram criadas pelo processo decorrente da parametrização do campo ‘Incluir Lançamento Automático com Relacionamento’ na tela Informações ECF aba LALUR e LACS não serão recuperados.

(-) Compras de Insumos – Quando marcado, preenche as linhas 3 e 4 do registro L210 - Informativo da Composição dos Custos com o valor do movimento do mês, e não apenas pelo saldo final.

Ajustar Apuração: Permite ao usuário ajustar uma abertura de apuração. Esta ação somente é possível de ser realizada,se  o registro selecionado possuir o status  igual a Cálculo Realizado. Após a ação neste botão o status da abertura da apuração será alterado para ‘Reapurar’.
Se existir no exercício aberturas de apurações com status “Cálculo Realizado” em períodos posteriores ao da abertura de apuração selecionada e o usuário confirmar, todas as aberturas a partir da selecionada, ficarão com status igual a ‘Reapurar’.

Editar Apuração: Permite ao usuário altera uma abertura de apuração. Só será possível alterar uma abertura se seu status for igual a ‘Apuração em Aberto’ e o  último período de apuração criado para o exercício.
Será apresentado todos os campos do  botão Adicionar Apuração, porém os campos que identificam o registro não ficarão abertos para serem alterados.

Remover Apuração: Permite ao usuário remover uma abertura de apuração. Se existir abertura posteriores a que está sendo excluída, todas serão removidas, caso seja feita a confirmação da exclusão dos registros.

Visualizar Apuração: Permite ao usuário visualizar uma abertura de apuração que foi criada.
Será apresentado todos os campos do Botão Adicionar Apuração, porém todos os campos ficarão desabilitados.



### MAPEAMENTO

Através do menu ‘Mapeamento’ pode-se realizar a  associação da conta referencial ou da linha da tabela dinâmica com o plano empresa (contas contábeis) e com o centro  de custo.
- Associação das Tabelas Dinâmicas com o Plano Empresa
- Associação do Plano de Contas Referencial com o Plano Empresa

#### ASSOCIAÇÃO DO PLANO DE CONTAS REFERENCIAL COM O PLANO EMPRESA


Nesta funcionalidade  é possível informar  qual conta contábil e/ou centro de custo atribuirá  valor para a conta do plano referencial. Esta associação deve ser realizada após a integração das Contas Contábeis e  Centro de Custo (Módulo Básicos/Ferramentas).

Segue tela:





Na inclusão de registro, preencher os  campos abaixo:
Data Inicial :Informa a data inicial da associação do plano referencial com o plano empresa.
Este campo é de preenchimento obrigatório.
Código: Informa o código da associação do plano referencial com o plano empresa que será vinculado a um grupo de estabelecimento. Será possível incluir mais de uma parametrização para o mesmo grupo.
Este campo é de preenchimento obrigatório.
Descrição: Informa a descrição do código da associação do plano referencial com o plano empresa. Este campo é de preenchimento obrigatório.
Grupo: Informa o código do grupo de estabelecimentos. Este cadastro já deve estar criado no módulo Parâmetros (Funcionais/Grupos de Estabelecimento) e após ser selecionado, será apresentado o código e descrição do grupo.
Este campo é de preenchimento obrigatório.
Versão: Informa a versão do plano referencial que será utilizada. Esta versão é compatível com a data inicial da parametrização. Será disponibilizado as opções, conforme regra Versão, somente após o preenchimento do campo data Inicial.
Este campo é de preenchimento obrigatório.

Plano de Contas Referencial
Registro: Informar o registro que o usuário irá parametrizar. Será disponibilizado as opções conforme regra Registros de Tabela Referencial (TFIX91).
Este campo é de preenchimento obrigatório.

Botões de Ação
Pesquisar: Permite pesquisar as contas referenciais (apenas do tipo analítica) da TFIX92, podendo utilizar como filtro os campos: Código, Descrição e  Natureza da conta.
Remover Associação: Permite remover toda associação (contas contábeis e centros de custos) feita na conta referencial.

Associar Conta Empresa: Permite escolher as contas da empresa que serão associadas a conta referencial. Só será permitido associar contas do tipo analíticas e compatíveis com a natureza da conta referencial.
Exemplo:
Natureza do plano referencial igual a ativo, passivo ou patrimônio, apenas as contas contábeis com natureza equivalentes poderão ser associadas.
Atenção: Os botões de ação também podem ser acionados utilizando o botão direito do mouse (dentro do componente):


Apresentação da Grid do Plano de Contas Referencial: Exibe os campos Contas Referenciais (Código com a Descrição da Conta Referencial), a Natureza (código e descrição) e a informação de Associação de Contas Contábeis ( exibindo a quantidade das contas contábeis que estão associados na conta referencial)

Plano de Contas da Empresa
Botões de Ação
Pesquisar: Permite pesquisar as contas contábeis (apenas do tipo analítica) da SAFX2002, podendo utilizar como filtro os campos: Código, Descrição e Natureza.
Remover Associação: Permite remover da conta contábil selecionada, os centros de custo associados.
Mostrar apenas com Associações, se marcar este check-box, só será demonstrado na grid as contas contábeis  que possuem algum centro de custo associado.  Caso o check-box esteja desmarcado, todas as contas contábeis, serão exibidas na grid.

Associar Centro de Custo: Permite adicionar na conta contábil selecionada um ou mais centro de custo.

Atenção: Os botões de ação também podem ser acionados utilizando o botão direito do mouse (dentro do componente):


Apresentação da Grid Plano de Contas da Empresas:
Check-box – Marcar Todos: Permite selecionar todos os registros que estão na grid. Funcionalidades que podem se valer desta opção são: Remover Associação
Check-box: Permite selecionar uma ou mais contas contábeis. Funcionalidades que podem se valer desta opção são: Remover Associação

Exibe os campos Contas da Empresa (Código com a Descrição da Conta Referencial), a Natureza (código e descrição)e a informação de Associação de Centro de Custo (quantidade dos centros de custos que estão associados na conta contábil).

Centro de Custo
Botões de Ação
Pesquisar: Permite pesquisar os centros de custo (SAFX2003), podendo utilizar como filtro os campos: Código e Descrição.
Remover Associação: Permite remover um ou mais centros de custos  vinculados na conta contábil.
Atenção: Os botões de ação também podem ser acionados utilizando o botão direito do mouse (dentro do componente):

Apresentação da Grid Centro de Custo:

Check-box – Marcar Todos: Permite selecionar todos os registros que estão na grid. Funcionalidadeque pode se valer desta opção é a Remover Associação.
Check-box: Permite selecionar um ou mais centro de custo. Funcionalidades que podem se valer desta opção são: Remover Associação.
Exibe os campos Centro de Custo (Código com a Descrição do Centro de Custo).
#### ASSOCIAÇÃO DA TABELA DINÂMICA COM O PLANO EMPRESA

Nesta funcionalidade  é possível informar  qual conta contábil e/ou centro de custo atribuirá  valor para a linha da tabela dinâmica. Esta associação deve ser realizada após a integração das Contas Contábeis e  Centro de Custo (Módulo Básicos/Ferramentas).

Segue tela:

Na inclusão de registro, preencher os  campos abaixo:
Data Inicial :Informa a data inicial da associação da tabela dinâmica com o plano empresa.
Este campo é de preenchimento obrigatório.
Código: Informa o código da associação da tabela dinâmica com o plano empresa que será vinculado a um grupo de estabelecimento. Será possível incluir mais de uma parametrização para o mesmo grupo.
Este campo é de preenchimento obrigatório.
Descrição: Informa a descrição do código da associação da tabela dinâmica com o plano empresa. Este campo é de preenchimento obrigatório.
Grupo: Informa o código do grupo de estabelecimentos. Este cadastro já deve estar criado no módulo Parâmetros (Funcionais/Grupos de Estabelecimento) e após ser selecionado, será apresentado o código e descrição do grupo.
Este campo é de preenchimento obrigatório.
Versão: Informa a versão da tabela dinâmica que será utilizada. Esta versão é compatível com a data inicial da parametrização. Será disponibilizado as opções, conforme regra Versão, somente após o preenchimento do campo data Inicial.
Este campo é de preenchimento obrigatório.
Tabela Dinâmica
Pesquisar: Permite pesquisar as linhas da tabela dinâmica (apenas tipos diferentes de CNA (cálculo não alterável) e R (rótulo) e  de lançamento diferentes de P (prejuízo) e L (Lucro)) da TFIX92, podendo utilizar como filtro os campos: Código, Descrição e  Tipo.
Remover Associação: Permite remover toda associação (contas contábeis e centros de custos) feita na linha da tabela dinâmica.
Associar Conta Empresa: Permite escolher as contas da empresa que serão associadas a linha da tabela dinâmica. Só será permitido associar contas do tipo analíticas.
Exemplo:
Código do Registro: Informar o código do registro que o usuário irá parametrizar. Será disponibilizado as opções conforme regra Registros de Tabela Dinâmica (TFIX88).
Este campo é de preenchimento obrigatório.
Apresentação da Grid Tabela Dinâmica: Exibe o Código, a  Descrição da Linha de Tabela Dinâmica, o tipo e a informação de Associação de Contas Contábeis ( exibindo a quantidade das contas contábeis que estão associados na linha da tabela dinâmica)

Contas da Empresa Selecionadas
Pesquisar: Permite pesquisar as contas contábeis (apenas do tipo analítica) da SAFX2002, podendo utilizar como filtro os campos: Código, Descrição e Natureza.
Remover Associação: Permite remover da conta contábil selecionada, os centros de custo associados.
Associar Centro de Custo: Permite adicionar na conta contábil selecionada um ou mais centro de custo.
Adicionar Informação Complementar: Permite adicionar Percentual de Receita Bruta nas linhas 2 dos registros N500 e N650 os percentuais de receita bruta.
Registro N500:
1,6%
8%
16%
32%
100%

Registro N650:
12%
32%
100%

Esta opção só será habilitada nas linhas 2 dos registros N500 e N650 e se existir pelo menos uma conta contábil associada na linha da tabela dinâmica. Caso na linha exista uma conta com o percentual de receita informado, todas as demais contas desta linha deverá ter um percentual atribuído (este valor pode ser diferente entre as contas).

Apresentação da Grid Contas das Empresas Selecionadas:
Check-box, o código, descrição da conta contábil , naturezae percentual de receita bruta.

Centro de Custo:
Pesquisar: Permite pesquisar os centros de custo (SAFX2003), podendo utilizar como filtro os campos: Código e Descrição.
Remover Associação: Permite remover um ou mais centros de custos  vinculados na conta contábil.

Adicionar Informação Complementar: Permite incluir nas linhas 2 dos registros N500 e N650 os percentuais de receita bruta.
Registro N500:
1,6%
8%
16%
32%
100%

Registro N650:
12%
32%
100%
Apresentação da Grid Centro de Custo:
Check-box, o código, descrição do centro de custo e percentual de receita bruta.

#### ASSOCIAÇÃO DAS SUBCONTAS CORRELATAS COM O PLANO DA EMPRESA


Tem como objetivo indicar a Variação do Ativo Imobilizado (Equipamentos, veículos, imóveis), de acordo com a lei 11638/2007 de padrão internacional, trazendo harmonização contábil e padronizando a contabilidade.
Esta associação possibilita a geração do registro J053 que  é utilizado para demonstrar os grupos de contas que são compostos de uma conta “pai” e uma ou mais subcontas correlatas.
É possível utilizar o mesmo código de identificação do grupo para mais de um conjunto de conta “pai” e subconta(s).
Esta tela é a mesma que está disponível no módulo SPED >> ECD -Escrituração Contábil Digital. Além disso, as informações também podem ser importadas através da SAFX2105 – Subcontas Correlatas.

Descrição dos campos

Conta (Grupo/Cód./Desc.): Informar o código da conta contábil pai, que será relacionada com as contas filhas, ou seja, as subcontas correlatas.
Grupo Conta-Subconta: Informar o Grupo que identifica o relacionamento entre a conta e a subconta.
Natureza da Subconta: Informar o código da Natureza da Subconta Correlata. Esta informação requer a importação da tabela TACES90 – Natureza da Subconta Correlata.
Subconta Correlata: Informar o código da subconta correlata.



### PERFIL DE GERAÇÃO


O Perfil de Geração é uma funcionalidade que permite efetuar a parametrização de Blocos e Registros que serão gerados pelo sistema.  Está funcionalidade está diretamente relacionada com a geração do arquivo. É permitido nesta tela, desmarcar apenas os registros não obrigatórios no leiaute da obrigação ECF .

Nota: O registro M500 não é de caráter não obrigatório, no entanto, como não é gerado pelo sistema não é possível alterá-lo. E, apesar de ser exibido no  Perfil de Geração, não é possível realizar a sua parametrização.
PRINT da TELA

Descrição dos campos
- Leiaute: Selecionar/informar o layout. Exibe a lista de versão
Perfil:  Informar o código do perfil da geração e uma descrição para o perfil.


Descrição dos Blocos - Visualização dos blocos disponíveis para a geração do arquivo pelo sistema.

Descrição dos Registros do bloco selecionado

Código Registro - Visualização dos  códigos dos registros associados aos blocos disponibilizados de acordo com a relação de dependência entre os registros.
Nível - Visualização do nível do registro dentro da sua hierarquia.
Descrição -  Visualização da descrição do registro exibido.
## MANUTENÇÃO


### CONTAS DA PARTE B

Cadastrar as Contas da Parte B do Estabelecimento.
Print da tela
Os campos presentes nesta opção encontram-se abaixo:
Grupo: Neste campo, o usuário deverá informar o código do grupo que a conta será vinculada. Esse Grupo é informado baseando-se nas Tabelas de Grupos, cadastradas pelo usuário no item de Grupo Estabelecimento, no Módulo de Parâmetros.
Conta da Parte B: Nesse campo, o usuário deverá informar o código da conta da parte b.
Descrição da Conta da Parte B: Nesse campo, o usuário deverá informar a descrição da conta da parte B.
Data de Criação: Nesse campo, o usuário deverá informar a data que a conta foi criada. A data de criação precisa ser menor ou igual a data limite da conta, além disso, precisa estar vigente para o grupo selecionado.
Data Limite: Nesse campo, o usuário deverá informar a data máxima que esta conta poderá ser utilizada. A data limite precisa ser maior ou igual a data de criação da conta, além disso, precisa estar vigente para o grupo selecionado. Este campo não é de preenchimento obrigatório.



### SALDOS DAS CONTAS DA PARTE B


Nesta rotina serão informados os valores dos saldos iniciais de cada escrituração para as Contas da Parte B.
Print da tela
Dados Gerais :
Recupera os dados de uma Informação ECF.

- Os campos a seguir referem-se ao registro do saldo inicial da conta da parte B:

- Grupo – Grupo que a conta da parte B está cadastrado.
- Conta da Parte B – Conta da parte B que será indicado seu saldo inicial.
Tributo – Informar se o tributo do saldo é Imposto de Renda Pessoa Jurídica  ou Contribuição Social sobre o Lucro Líquido.
Linha – Informar a linha da tabela dinâmica referente aos registros M300A, M300B ou M300C, se o tributo for igual a Imposto de Renda Pessoa Jurídica e M350A, M350B ou M350C, se o tributo igual a Contribuição Social sobre o Lucro Líquido
CNPJ Origem - CNPJ da outra pessoa jurídica relacionada com evento originário da conta (situação especial).

- Valor do Saldo Inicial da Escrituração – Informar o saldo inicial da escrituração desta conta para este tributo. Se a data de criação da conta estiver no mesmo ano do saldo da escrituração, obrigatoriamente este saldo deve ser zero.
- Ind. Do Saldo:Indicador do saldo inicial desta conta e deste tributo.
- Lançamentos
- Parte A: Permite que o usuário visualize se há lançamentos da parte A, para este saldo.
- Parte B com Cálculo Realizado: Permite que o usuário visualize se há lançamentos da parte B, para este saldo e se foi gerado o cálculo no processamento em lote para algum período de apuração da escrituração.
- Parte B sem Cálculo Realizado: Permite que o usuário visualize se há lançamentos da parte B, para este saldo e se não foi gerado o cálculo no processamento em lote para algum período de apuração da escrituração.


### PAT – PERÍODOS ANTERIORES AO DW


No sistema é possível cadastrar manualmente os valores disponíveis à utilizar (sobras) do PAT cujo controle tenha sido realizado em outros sistemas diferentes do DW.
Será disponibilizada automaticamente a primeira informação ECF existentente no sistema. A partir da data inicial da informação ECF selecionada, os últimos 2 anos são disponibilizados para que o valor disponível à utilizar (sobras) seja cadastrado.
Esta tela está disponível para a realização do cadastro quando a Abertura da Apuração possuir status ‘Em Aberto’ ou ‘Reapurar’, ou, não houver abertura da apuração correspondente.


Dados Gerais :
Recupera os dados de uma Informação ECF.

Descrição dos campos

ANO AAAA - Visualização do ano disponível para inclusão do valor do PAT disponível para utilização (sobras).

Valor –  Informa o valor do PAT disponível para utilização no período correspondente.



## APURAÇÃO


### PROCESSAMENTO EM LOTE


O Processamento em Lote é uma funcionalidade que consiste utilizar todas as parametrizações, permitindo a realização do cálculo do IRPJ e da CSLL, para uma posterior geração do arquivo magnético da ECF..


Descrição dos campos

Exercício: informar o exercício

Transcrição dos Valores Empresa para Referenciais Fisco – Quando selecionado atribui as linhas da tabela dinâmica e do plano referencial os saldos contábeis.

Manter Ajustes Manuais -  Quando selecionado, na realização de um n ovo processamento em lote, mantem os ajustes realizados manualmente no sistema como por exemplo os ajustes manuais realizados na tela Entrada Manual de Valores, Lançamentos da Parte A (M300, M350) entre outras funcionalidades

Cálculo dos Registros e Fórmulas – Quando selecionado, executa as fórmulas existentes nas tabelas dinâmicas.

Períodos de Apuração dos Estabelecimentos

Selecionar o item da lista de seleção que deseja executar o processamento e clicar em “Processar” para iniciar o processamento. A seleção pode ser feita manualmente (selecionando quantos registros houver necessidade)  e utilizando o Check-box – Marcar Todos que permite selecieonar todos os registros que estão na grid.
Selecionar: Permite pesquisar dentre a seleção de registros que estão em condições de executar o processamento.

Obs.  Ao selecionar o processo de Transcrição dos Saldos,   o processo “Manter Ajustes Manuais Realizados” é habilitado.  Se o processo de Transcrição dos Saldos, for desmarcado, o processo “Manter Ajustes Manuais Realizados”  será desabilitado e desmarcado. Se o processo “Manter Ajustes Manuais Realizados” estiver marcado os seguintes dados que foram digitados de forma manual serão preservados:

- Tela Entrada Manual de Valores (todos os ajustes na tela)
Modal Entrada Manual (Valor, Percentual de Receita Bruta e Justificativa).

- Tela Lançamentos da Parte A (M300, M350).
Lançamentos vinculados
Processos vinculados
Ajustes vinculados
Status

- Tela Ajustes da Parte B
- Somente relacionamento com origem da parte A

- Demonstração do Resultado
- Anexos

- Percentual de Rateio de Atividades Mistas
Conteúdo do campo - Perc. Geral Ajustado
Conteúdo do campo - Perc. Rural Ajustado


- Tela Ajustes do Bloco K
- Conteúdo da Aba Rateio
- Conteúdo da Aba Demais Ajustes

Obs.:  Referente ao Bloco K a seguinte regra é aplicada:

Se o saldo da conta contábil for igual e as contas referencias não tiveram novas associações ou retirada de associações, o rateio é mantido, caso contrário, o rateio é excluído.
Se a Transcrição dos Saldos for efetuada com o parâmetro “Manter Ajustes Manuais Realizados” desmarcado, todos os ajustes manuais são apagados.

### AJUSTES MANUAIS


#### PERCENTUAIS DE RATEIO DAS ATIVIDADES MISTAS


Nesta tela é possível realizar o rateio dos saldos quando se tratar de empresa com  Atividade Mista (Atividade Geral + Atividade Rural). O sistema calculará proporcionalmente o percentual de composição do saldo que compõe as contas referenciais de acordo com os Saldos da Atividade Geral e Atividade Rural. Pode-se ratear automaticamente os valores das contas contábeis associadas às contas analíticas do plano referencial L300A iniciadas com 3.01 (Atividade Geral) e 3.11 .
Como pré-requisito, o usuário deve ter realizado a rotina de importação dos saldos do processamento em lotes e possuir a opção “Atividade Rural” da tela de informações ECF selecionada.
Nesta rotina, deve-se visualizar os valores calculados para as contas 3.01.01.01 e 3.11.01.01, somar os dois valores e calcular o percentual conforme exemplo abaixo:


O percentual calculado pelo sistema pode ser alterado.
Após definido o percentual, o sistema deve identificar todas as contas contábeis associadas a ambas atividades (Rural (3.11) e Geral (3.01)) e aplicar o percentual, conforme abaixo:


Caso exista uma conta associada a mais de uma conta de determinada atividade, o rateio deve ser aplicado considerando o percentual da atividade. Assim o valor é duplicado, e o saldo da atividade deve ser rateado manualmente, conforme abaixo:


Caso uma determinada conta esteja associada somente a uma atividade, o percentual não deve ser aplicado.
É necessário manter o histórico de todos os percentuais aplicados mês a mês ou trimestre a trimestre (de acordo com a parametrização realizada).
Para isto, foi incluído na tela de rateio do bloco K as informações do quadro abaixo (somente leitura), previamente informados na rotina de rateio automático, para facilitar a identificação dos valores.


Para que seja realizado o  rateio, será necessário realizar o processamento que pode ser divido em duas etapas:

- 1 – Etapa de ajustar os percentuais calculados
- 2 – Etapa Recuperar as Aberturas de apuração, considerando os percentuais calculados pelo sistema

1 – Etapa Opções de Processamento
Nesta etapa é possível informar o exercício e selecionar as rotinas que serão executadas.

Print da Tela
Descrição dos campos

Exercício – Informa o exercício para a execução dos processos.
Considerar Percentuais Ajustados -  Se desmarcado, os campos de percentuais ajustados ficarão desabilitados.
Percentual Ajustado Geral (%): Este campo só é habilitado, se o campo “Considerar Percentuais Ajustados” estiver marcado. Permite informar o percentual que será utilizado no calculo das atividades gerais.
Percentual Ajustado Rural (%):Este campo só é habilitado, se o campo “Considerar Percentuais Ajustados” estiver marcado. Permite informar o percentual que será utilizado no calculo das atividades rurais.

Atenção: os campos Percentual Ajustado Geral (%) e Percentual Ajustado Rural (%) devem totalizar 100,0000%

Períodos de Apuração dos Estabelecimentos:
Check-box – Marcar Todos: Permite selecionar todos os registros que estão na grid
Apresenta todas as aberturas de apuração do exercício informado na tela, que foram calculados os percentuais de atividades gerais e rurais.
Formato: Código do Estabelecimento – CNPJ – Exercício – Data inicial da InformaçãoECF – Código da Abertura – Descrição da Abertura – Percentual Geral e Rural: XX% e XX%

Selecionar o item da lista de seleção que deseja executar o processamento e clicar em “Executar” para iniciar o processamento.
Ao finalizar este processamento, é necessário 'Validar Rateio na Conta' na tela Ajuste Manual do Balanço/DRE (Bloco K), para cada conta contábil que o saldo foi rateado.

#### BALANÇO/DRE (BLOCO K)


A funcionalidade de Ajuste Manual do Bloco K tem por finalidade efetuar a manutenção nos saldos das contas do Plano da Empresa que foram associadas às contas do Plano Referencial do Governo, podendo efetuar também, quando necessário, o rateio dos saldos quando uma conta do Plano da Empresa estiver associada a mais de uma conta do Plano Referencial.
Tal funcionalidade é iniciada quando na execução da rotina Transcrição dos Valores Empresa para Referenciais Fisco do processamento em lote é identificado que existem contas contábeis associadas a mais de uma conta referencial no painel de controle o status do processamento em lote Aguardando Alteração Manual, sendo preciso efetuar os ajustes necessários na tela de Ajuste Manual do Bloco K. Estas informações podem ser inseridas de forma manual ou via integração de arquivos na tela.
ATENÇÃO: Nesta tela só serão recuperadas aberturas com status diferente de “Apuração em Aberto” e A00. E só serão permitidas alterações nos registros quando o status da abertura de apuração for diferente de  “Cálculo Realizado”.
ABA RATEIO

Nesta tela é possível atribuir valor para as contas referenciais exibidas na coluna do lado direito. Após realizar a manutenção do valor é possível validar e justificar os valores manutenidos.

PRINT DA TELA
Dados Gerais :
Recupera os dados de uma abertura de apuração.

Descrição dos campos

Validar  - Quando o campo está nulo, indica que o registro não foi validado. Se o campo possuir o ícone “”, indica que o registro foi validado e não há diferenças entre o saldo inicial/final informado com o calculado. Quando o registro for validado e existir diferenças entre o saldo inicial/final informado com o calculado, apresenta o ícone de justificativa em vermelho “”, caso a justificativa não tenha sido informada e se for informada, o mesmo ícone é apresentado na cor verde.

Botões de Ação
Validar Rateio em Todas as Contas – Quando selecionado, valida todas as contas que possuem o ícone validar em vermelho.

Deve-se validar o rateio de Saldo inicial para as contas Patrimoniais no primeiro período de apuração anual e para todos os períodos de apuração trimestral.
Se o somatório de todas as Contas Referenciais (segunda grid) for igual ao montante apresentado no Saldo Calculado da Conta Contábil, o sistema grava as informações e exibe o status Validação OK representado pelo símbolo “” na coluna Validar.

Se o somatório de todas as Contas Referenciais (segunda grid) for diferente do montante apresentado no Saldo Calculado da Conta Contábil, o sistema após a validação de conta apresenta um formulário para que se justifique a alteração.

Pode-se confirmar a justificava ou cancelar a justificativa e efetuar a manutenção do valor do saldo novamente.
PRINT DA TELA



Na hipótese de cancelamento da justificativa e saída do formulário, o ECF - Escrituração Contábil Fiscal (DW) entende que existe uma divergência a ser justificada, porque um cálculo já foi feito, e para a manutenção consta o status: “Aguardando Justificativa”, representado pelo lápis em vermelho, o símbolo “”.
PRINT DA TELA


Pode-se efetuar a manutenção dos saldos ou justificar a alteração dos saldos que gerou a divergência entre valores. Para confirmar a justificativa basta clicar no símbolo “” e o formulário de justificativa será novamente exibido.

PRINT DA TELA

Após digitar a justificativa, clicar no botão Justificar e o status será alterado de Aguardando Justificativa  para o status Justificativa OK .
Obs.: A alteração dos saldos não reflete nos saldos inicialmente importados na tela Saldos Contábeis.
ABA  DEMAIS AJUSTES


PRINT DA TELA


Botões de Ação

Validar Ajuste em Todas as Contas – Quando selecionado, valida todas as contas que possuem o ícone validar em vermelho.

ENTRADA MANUAL DE VALORES

A funcionalidade de entrada manual de valores possibilita a alteração dos valores dos registros diretamente nas linhas das tabelas dinâmicas, sobrepondo os valores calculados através do reprocessamento da apuração. As linhas corresponde ao Bloco M não estão disponíveis para a realização da entrada manual.
A funcionalidade de entrada manual só é habilitada após a  execução   da rotina Transcrição dos Valores Empresa para Referenciais Fisco no processamento em lote.
Se o status da apuração estiver como “Cálculo Realizado”,  “Apuração em Aberto” e “Aguardando Alteração Manual” a edição da Entrada Manual de Valores não será permitida, porque  é necessário ter realizada a rotina Transcrição dos Valores Empresa para Referenciais Fisco  e no caso do status “Cálculo Realizado” pelo fato do período está fechado, será necessário reabrí-lo.

Considerações:
Para forma de tributação igual a Lucro Real e apurações anuais:
Apenas será permitido ajustes (entrada manual de valores) na ultima abertura de apuração da escrituração  para os  registros N630 e N670, porém, a cada processamento, o sistema entende que o ultimo período é o período que está sendo processado. Caso seja feito um ajuste nesses registros em uma abertura e depois um novo período for processado, a entrada manual anterior, será descartada.
Na demonstração de resultado desses registros (Tela Lucro Real), apenas é apresentado a aba anual, com a informação do ultimo período processado.

Print da tela

Descrição dos campos

Dados Gerais :
Recupera os dados de uma abertura de apuração.

Registros Processados:
Botões de Ação
Marcar Todos: Se marcado, seleciona todas as linhas da tabela dinâmica desta abertura de apuração.
Pesquisar: Permite pesquisar um registro da tabela dinâmica, pelos campos Registro e Linha.
Descartar as Alterações Manuais - Através desse botão, é possível descartar todos os valores de entrada manual das linhas dos registros selecionados.
Justificar Valor(es) Alterado(s):  Através deste botão, é possível justificar todas as linhas selecionadas que possuem entrada manual informada.
Mostrar Apenas Pendentes de Justificativa:  Se marcado, exibe na grid apenas as linhas que possuem valor de entrada manual e que ainda não foram justificadas.


Inserir/Alterar Entrada Manual

As alterações devem ser realizadas na própia grid (linha da tabela dinâmica), ajustando o campo valor.

Print da Tela

Campos da Grid:

Status: Exibe o status da linha.
Ícones de Status Permitidos:

Em branco: Não foi realizada uma entrada manual.

Ícone Justificar em Vermelho: Realizada entrada manual e o valor não foi justificado.

Ícone Justificar em Verde: Realizada entrada manual e o valor foi justificado.

Ícone Descartar Entrada Manual: Realizada entrada manual (com ou sem justificativa) e o valor foi descartado.

Ícones de Formato de Linhas:
: Exibir este ícone do lado direito do ícone de status, para os campos de valor com formato ‘NS’ com o tooltip:
“Esta linha aceita valores negativos”.
: Exibir este ícone do lado direito do ícone de status,na linha 2 dos regisros N500 e N650 que podem conter informações de percentuais de receita bruta, com o Tooltip:
‘Percentuais de Receita Bruta’.

Caso a linha do registro possua informação de percentual de receita bruta (cifrão exibido no campo Status), o campo pertinente a essas informações é apresentado dentro do modal Percentuais da Receita Bruta – Informa o percentual a ser aplicado sobre a receita bruta.

Ordem de exibição dos ícones no campo: Status + +



Registro: Indica o registro da tabela dinâmica.
Código do Registro: Exibe a linha do registro da tabela dinâmica.
Descrição do Registro: exibe a descrição da linha do registro da tabela dinâmica.
Ordem: Exibe a ordem de cada linha da tabela dinâmica.
Linha ECF: Exibe a linha ECF da Tabela dinâmica.
Valor: Exibe o valor da linha realizado pela rotina ‘Transcrição dos Valores Empresa para Referenciais Fisco’ ou que foi alterado pelo usuário.

Botões de Ação:
Pesquisar: Permite pesquisar um registro de tabela dinâmica, criado pela rotina ‘Transcrição dos Valores Empresa para Referenciais Fisco’
Descartar as Alterações Manuais: Quando uma entrada manual é realizada em alguma linha do registro, o sistema grava e armazena os dados inseridos na linha para que a modificação seja aplicada através do Processamento em Lote.
Caso seja necessário desfazer uma alteração, é possível realizar através da ação de descarte.
Poderá ser selecionados na grid apenas os registros alterados(através do check-box), facilitando a ação de descarte das alterações manuais.

Obs.: Para que a alteração tenha efeito, é necessário refazer o processamento em lote.
Com esta opção, e com a o parâmetro “Manter Ajustes Manuais” da tela de Processamento em Lote, torna-se possível manter os ajustes necessários e descartar os desnecessários.

Justificar Valor(es) Informado(s): Permite Justificar um ou mais registros que foram marcados (selecionando o check-box). Todas as linhas que forem alteradas através desta tela, ficam pendentes de justificativa, sinalizadas com o ícone  Justificar em Vermelho no campo Status.

Percentual de Receita Bruta: Permite inserir valores na linha 2 dos registros N500 e/ou N650 por percentual. Quando acionado este botão (para estas linhas), será aberto uma tela, onde será possível compor o valor da linha pela quebra de percentual de receita bruta.
Atenção: Ao efetuar ajuste na tela de entrada manual, diretamente na linha 2 dos registros N500 e  ou N650 (Campo Valor, na grid principal), os valores existentes por percentual serão descartados. Caso o Ajuste seja realizado pelo botão de Percentual de Receita Bruta, o Somatório do Valor Calculado, será transportado para a Linha 2 (na grid principal).









LANÇAMENTOS DA PARTE A (M300, M350)

O produto ECF - Escrituração Contábil Fiscal (DW) permite a manutenção dos valores de Adição e Exclusão nos Registros M300 e M350 de forma manual nas Partes A e B.
Para as contas contábeis associadas as linhas do registros M300 que foram criadas pelo processo decorrente da parametrização do campo ‘Incluir Lançamento Automático com Relacionamento’ na tela Informações ECF aba LALUR e LACS não será permitida a realização de qualquer ajuste manual.

O valor do ajuste da parte B deve ser preenchido com o saldo disponível para a conta no período.  Se o valor do ajuste da parte B for diferente do saldo disponível para a conta no período uma mensagem de alerta  é  exibida.
Quando selecionada uma conta da Parte B, o produto traz o valor do ajuste preenchido com o saldo disponível da conta para o período, sendo permitida a alteração do valor.
O sistema verifica o valor atualizado da Parte B e também o das demais contas associadas, soma e totaliza o valor na Parte A.
Após consulta do registro a ser alterado, deve-se clicar no botão Editar para iniciar o processo de manutenção diretamente nos valores das Contas. Caso o estabelecimento selecionado para edição esteja com o Processamento em Lote em execução, a edição dos dados da tela não é permitida, sendo necessário acessar a tela Informações ECF e realizar o desbloqueio da escrituração por meio do botão Desbloquear Escrituração para alterar os dados.


Print da tela

Dados Gerais :
Recupera os dados de uma abertura de apuração.


Descrição dos campos

Informações do Lançamento da Parte A (M300, M350)

Registro – Visualização  do registro.
Código do Registro: Visualização do Código do Registro.
Descrição do Registro: Visualização da descrição do Registro.Tipo de Lançamento: Visualização do tipo de lançamento.
Tipo de Lançamento – Visualização do tipo de lançamento.
Tipo de Tributo: Visualização do Tipo de Tributo.

Tipo de Relacionamento – Visualização do tipo de relacionamento

Exibição do conteúdo do campo Valor – Neste campo pode-se selecionar a composição do campo valor quando o  tipo de relacionamento for “Com Conta da parte B e Conta Contábil”. As seguintes opções são exibidas:
- Somatório das Contas Contábeis com o somatório das Contas da Parte B
- Obs.: Quando selecionado o campo Valor será preenchido com das contas da parte B associadas à linha.

- Somatório das Contas Contábeis
- Obs.: Quando selecionado o campo Valor será preenchido com o somatório das contas contábeis associadas à linha. No campo Valor, será possível visualizar o somatório da coluna Saldo e/ou o somatório da coluna Lançamentos/Ajustes. Para cada conta contábil as colunas Saldos e/ou Lançamentos/Ajustes podem estar preenchida. Para as contas contábeis que possuem valores na coluna Lançamentos/Ajustes, este valor, será considerado no somatório. Quando a coluna lançamentos/Ajustes não estiverem preenchidas, será considerado o somatório da coluna Saldo.

- Somatório das Contas da Parte B
- Obs.: Quando selecionado o campo Valor será preenchido com o somatório das contas contábeis com o somatório das contas da parte B associadas à linha.
Somatório das Contas da Parte B – Neste campo será exibido o valor total das contas da parte b associada na aba “Contas da Parte B – Ajustes (M010)” para os tipo de relacionamento igual a ‘Com Conta Contábil’ ou ‘Com conta da Parte B e Conta Contábil’. Este campo é apenas para a visualização dos valores. Será realizada uma validação informando quando o somatório das contas da parte B não são iguais ao somatório das contas contábeis do lançamento da parte A. Esta validação é meramente informativa.

Somatório das Contas Contábeis – Neste campo será exibido o valor total das contas contábeis associadas na aba “Contas Contábeis”para os tipos de relacionamento igual a ‘Com Conta Contábil’ ou ‘Com conta da Parte B e Conta Contábil’. Este campo é apenas para a visualização dos valores. Será realizada uma validação informando quando o somatório das contas da parte B não são iguais ao somatório das contas contábeis do lançamento da parte A. Esta validação é meramente informativa.

Valor – Visualizar/informar o valor da linha.
Histórico – Informar o histórico.

ABA CONTAS DA PARTE B - AJUSTES (M010)

Nesta aba é possível  adicionar através da aba Ajustes da Parte B a serem vinculados à conta da parte A selecionada.

PRINT DA TELA

Descrição dos campos

Esta conta pode receber valores para juntamente com os valores da Parte A, fazer parte do cálculo da apuração. Para isto, clicar em Adicionar. Uma janela para seleção da conta da Parte B e informação do valor a ser inserido é exibida.

PRINT DA TELA

Ao clicar no botão Adicionar, o sistema grava valor na Parte B,  se o  campo Exibição do conteúdo do campo Valor estiver com a opção Somatório das Contas da Parte B e altera o Tipo de Relacionamento de “Conta Contábil” para “Com Conta da Parte B e Conta Contábil”.

Se o campo Exibição do conteúdo do campo Valor estiver com a opção Somatório das Contas Contábeis com o somatório das Contas da Parte B selecionada,  o sistema grava o Valor na Parte B considerando o somatório de todas as contas da parte B e o somatório de todas as contas contábeis.
ABA  CONTAS CONTÁBEIS
Nesta aba as contas contábeis da empresa juntamente com seus saldos que compõem os registros a tabela dinâmica são apresentadas. Caso seja necessário, poderá ser considerado ou desconsiderado o movimento da conta contábil, utilizando os respectivos botões de ação:  Considerar Movimento e  Desconsiderar Movimento.


Print da tela
Descrição dos campos

Botões de Ação

Associar Lançamentos – Quando acionado exibe uma tela  possibilitando a associação dos lançamentos  contábeis decorrentes da execução da rotina ou seleção manual dos lançamentos contábeis corresponde a conta contábil.
Para a contas contábeis criadas pelo processo decorrente da parametrização do campo ‘Incluir Lançamento Automático com Relacionamento’ na tela Informações ECF aba LALUR e LACS a ação neste botão estará indisponível, pois não será permitida a realização de  qualquer ajuste nesse tipo conta contábil.

Alterar Valores – Quando acionado, exibe uma tela “Valores dos Lançamentos Associados ao Mês/Trimestre” permitindo a alteração nos valores e exclusão de lançamentos contábeis.

Considerar Movimento – Quando selecionado indica que o movimento a crédito e/ou débito da conta no período será considerado na composição do campo Valor. Para a contas contábeis criadas pelo processo decorrente da parametrização do campo ‘Incluir Lançamento Automático com Relacionamento’ na tela Informações ECF aba LALUR e LACS a ação neste botão estará indisponível, pois não será permitida a realização de  qualquer ajuste nesse tipo conta contábil.

Desconsiderar Movimento – Quando selecionado indica que o movimento a crédito e/ou débito da conta no período será desconsiderado, sendo utilizado no cálculo o Saldo Final do período anterior na composição do campo Valor. Este botão é exibido quando não há Lançamentos Contábeis na aba Lançamentos Contábeis. Para a contas contábeis criadas pelo processo decorrente da parametrização do campo Incluir Lançamento Automático com Relacionamento na tela Informações ECF aba LALUR e LACS a ação neste botão é indisponível, pois não é permitido realizar  qualquer ajuste nesse tipo conta contábil.

Remover Lançamentos – Quando acionado, remove todos os lançamentos contábeis vinculados a conta contábil selecionada.

Status – Visualização do status correspondente utilização do movimento da conta contábil associada à linha da tabela dinâmica.
- Considerar Movimento
- Obs.: Todas as contas contábeis associadas a linha da tabela dinâmica apresentam-se, inicialmente, com este status.
- Desconsiderar Movimento

Lançamentos/Ajustes – Visualização do  valor do ajustes das contas contábeis somado com o valor do período anterior e o indicador correspondente.

O sistema possibilita que o saldo da Conta Contábil seja utilizado de forma parcial, para isso deve-se informar o(s) lançamento(s), que deseja utilizar da Conta Contábil para compor o Saldo da Conta da tabela dinâmica.

Deve-se selecionar a Conta Contábil e em seguida acionar o botão Adicionar Valores.

ASSOCIAR LANÇAMENTOS
Print da tela


O sistema abre a janela para que os Lançamentos Contábeis seja pesquisados e depois  selecionados ou para visualização dos lançamentos contábeis que foram integrados via processo de integração conforme seleção das rotinas  ‘Associação Automática de Todos os Lançamentos Contábeis (M312 M362)’  e/ou ‘Associação dos Lançamentos Contábeis (M312 M362)’ informados pela Integração  disponíveis na tela de Processamento em lote.
Na seleção manual dos lançamentos, deve-se informar o intervalo de lançamentos para que o sistema efetue a busca dos lançamentos e em seguida clicar em Filtrar.  Apenas os  lançamentos contábeis selecionados  no check-box  e confirmados pelo botão Selecionar  serão considerados na composição do campos Lançamentos/Ajustes.


Print da Tela


VALORES DOS LANÇAMENTOS ASSOCIADOS AO MÊS/TRIMESTRE

Neste passo é possível visualizar as informações do Saldo Acumulado em períodos anteriores, do total dos lançamentos do período atual e movimento de crédito e débito do período.
Pode-se informar o valor do lançamento parcial a ser utilizado pelo saldo, podendo ser utilizado parcialmente ou na sua totalidade, é necessário também para fins de controle, justificar o ajuste realizado.



Print da tela

Descrição dos campos

Vlr. Períodos Anteriores –  Visualização do valor  total calculado para todos os lançamentos/ajustes do período anterior.
Ind. do Vlr. Períodos Anteriores – Visualização do indicador correspondente ao Vlr. Períodos Anteriores
Vlr.Total  - Visualização do valor correspondente ao lançamento contábil. Este campo estará visível quando houver  lançamento na grid da aba ‘Lançamentos Contábeis’.
Ind. do Vlr.Total – Visualização do indicador correspondente ao Vlr. Total.
Vlr. Parcial – Informar o valor parcial dos lançamentos que será utilizado na composição do campo Valor da parte A.
Ind. do Vlr. Parcial – Informar o  indicador correspondente ao Vlr. Parcial.
Vlr. dos Ajustes - Informar o valor  dos ajustes que será utilizado na composição do campo Valor da parte A.
Ind. do Vlr. dos Ajustes – Informar o indicador correspondente ao Vlr. dos Ajustes informado.

Total de Débito – Visualização do total do movimento à  débito da conta contábil. O valor estará disponível para visualização quando o status  da conta contábil for Considerar Movimento. Quando o status  for Desconsiderar Movimento, não será exibido valor no campo.

Total de Crédito – Visualização do total do movimento à  crédito da conta contábil. O valor estará disponível para visualização quando o status  da conta contábil for Considerar Movimento. Quando o status  for Desconsiderar Movimento, não será exibido valor no campo.
Vlr. a Utilizar – Visualização do valor que será utilizado para compor o valor da parte A. Este campo exibe os valores dos campos Vlr. Períodos Anteriores, Vlr.Parcial, Vlr. dos Ajustes e Vlr Total e os respectivos indicadores.
Ind. do Vlr. a Utilizar – Visualização do indicador correspondente ao Vlr. a Utilizar.
Caso exista lançamento contábil selecionado no passo 1 - Associar lançamentos Contábeis, nesta etapa será possível visualizar o grid com os lançamentos contábeis associados .


PRINT DA TELA

Após realização dos ajustes, aciona-se o botão OK e é apresentada a lista de seleção de regsitros já atualizada. Caso queira associar outros lançamentos contábeis, acionar o botão Refazer filtro.

ABA PROCESSOS

Botões de Ação:
Pesquisar: Permite pesquisar os processos, pelos campos Tipo e Número de Processo.
Adicionar: Para cada ajuste informado, se houver algum processo judicial ou administrativo vinculado, na tela abaixo é possível inserir tal infomação clicando no botão Adicionar.
Remover: Permite remover um ou mais processos cadastrados.

- Print da tela

LANÇAMENTOS DA PARTE B (M410)

O sistema efetua os controles dos lançamentos da Parte B da Apuração. Em alguns casos específicos torna-se necessário demonstrar os ajustes.
Nesta funcionalidade, a opção de manutenção dos ajustes da Parte B é disponibilizada por meio da ação Editar.

Print da tela

Descrição dos campos

Dados Gerais:

Recupera os dados de uma abertura de apuração.


Filtro da Conta da Parte B com Saldos na Escrituração
As informações contidas nesse item correspondem ao cadastro da conta que compõe a geração do registro M010  - Identificação da Conta na Parte B do e-Lalur e do e-Lacs no arquivo.
Grupo: Exibe o código e a descrição do grupo, que a conta foi cadastrada.
Tributo: Exibe o tipo de tributo do lançamento.
Opções de Lista:

-Imposto de Renda Pessoa Jurídica
-Contribuição Social sobre o Lucro Líquido

Conta da Parte B – Visualiza o código e a descrição da conta da parte B.

Data de Criação da Conta - Visualiza  a data de criação da conta da parte B.
Data Limite  - Visualiza a data limite de utilização da conta da parte B.
Saldo Inicial da Escrituração: Exibe o saldo inicial da conta da parte B para a  escrituração.

REGISTRO M500 – CONTROLE DE SALDOS DAS CONTAS DO E-LALUR E DO E-LACS (PARTE B)

Exibe valores  correspondente a CONTROLE DE SALDOS DAS CONTAS DO E-LALUR E DO E-LACS As informações desta grid é atualizada pelo sistema, com base nos lançamentos da Parte A (M330/M350) e da Parte B (M410 e Contrapartida)


Print da tela
Saldo Inicial: Visualização do saldo inicial utilizado pelo período.
Lançamentos da Parte A – Visualização da somatória dos lançamentos da parte A (tela Lançamentos Parte A (M300 M350).
Lançamentos da Parte B – Visualização do somatório dos lançamentos da parte B (Lançamentos Parte B (M410).
Lançamentos da Parte B – Contrapartida: Visualização dos lançamentos da Parte B (gerados automaticamente pelo sistema se o campo Contrapartida do Lançamento da parte B (M410) estiver preenchido.
Saldo Final: Saldo Final da Conta da  Parte B

REGISTRO M410 – LANÇAMENTOS NA CONTA DA PARTE B DO E-LALUR E DO E-LACS SEM REFLEXO NA PARTE A

Exibe valores  correspondente a LANÇAMENTOS NA CONTA DA PARTE B DO E-LALUR E DO E-LACS SEM REFLEXO NA PARTE A  para ambos tipos de tributo. Os valores correspondentes a esta aba, são inseridos nessa tela por meio do botão Adicionar.

Print da tela


Grid dos ajustes  (Registros M410)

Data do Lançamento:
Valor  - Visualização do valor com indicador correspondente ao ajuste.
Contrapartida  - Visualização da informação de contrapartida.
Histórico – Visualização do histórico do ajuste.
Ajuste com Origem na Parte B – Visualização da Informação e Ajuste com Origem da Parte B
Tributação Diferida – Visualização da Informação se tem ou não Tributação Diferida no lançamento.

Botoes de Adicionar , Alterar e Remover
Print da tela
Descrição dos campos do Modal Adicionar Laçamentos da Parte B


Valor – Informar o valor do ajuste.
- Ind. do Valor – Selecionar/informar   o indicador correspondente ao valor. Exibe a lista de para selecionar as seguintes opções:
- Crédito
- Débito
- Prejuízo do Exercício
- Base de Cálculo Negativa da CSLL

Atenção:  para calculo as opções Prejuízo do Exercício e Base de Cálculo Negativa da CSLL são consideradas como Débito.

- Tributação Diferida -  Selecionar/informar se há diferimento.  Exibe a lista de para selecionar as seguintes opções:
- Sim
- Não
Histórico – Informar o  histórico para justificar o valor.
- Ajuste com Origem na Parte B  - Selecionar/informar se há diferimento.  Exibe a lista de para selecionar as seguintes opções:
- Obs.: Este campo se apresenta desabilitado quando a apuração para o estabelecimento Matriz/SCP na tela Informações ECF for Trimestral.
- Para a escrituração de apuração Anual se a opção for :
- Incremental
- Esta opção considera o valor do ajuste anterior e o valor do ajuste atual.
- Cumulativo
- Esta opção considera o valor do ajuste de forma acumulada.

Contrapartida – Selecionar/informar a conta da parte B cujo valor do ajuste será transferido automaticamente. Quando este campo for preenchido, o sistema gerará automaticamente um ajuste na contrapartida informada na aba Origem da Contrapartida (da conta em questão).

Descrição da Contrapartida – Visualização da descrição da conta partida.

Dados dos Processos

Para cada ajuste informado no registro M410 na ocorrência de haver algumprocesso judicial ou administrativo vinculado, na tela abaixo, é possível inserir tal infomação clicando no botão Adicionar.

O modal Alterar possui os mesmos campos do Adicionar, porém os campos que identificam o registro não ficam habilitados para serem alterados.

### LUCRO REAL

#### COMPARATIVO


Esta tela permite a visualização  dos  impostos IRPJ e CSLL  na visão Receita bruta e  Balanço de Suspensão/Redução,  para que seja possível escolher o valor a ser utilizado no período.

Funcionamento da Tela:
Para visualizar valores nessa tela, é necessário que na tela Abertura da Apuração, o campo Tipo de Receita esteja preenchido com a opção “Comparativo” e a forma de tributação igual a Lucro Real. Permitiremos escolher uma forma, ou alterá-la,  se a abertura possuir status igual a Cálculo Realizado e se as aberturas posteriores estiverem diferentes de Cálculo Realizado. A escolha pode ser feita para uma ou todas as empresas, utilizando os filtros: Estabelecimentos, exercício e período da apuração.
Após a confirmação do filtro, é  demonstrado o valor apurado pelo sistema para os impostos na visão de receita bruta e Balanço de Suspensão/Redução. É possível escolher o tipo de receita desejado no período selecionando o campo de lista Receita Bruta X Balanço de Suspensão/Redução.  Os valores exibidos na tela tem como origem os registros N620 e N660 das respectivas linhas 26 e 18. Ao escolher uma visão, a tela Lucro Real (demonstração de resultado do bloco N), será atualizada, considerando a visão de cálculo que foi considerada pela empresa.


### INCENTIVOS FISCAIS


#### FINAN e FINOR


Este registro deve ser preenchido pelas pessoas jurídicas ou grupos de empresas coligadas de que possuem Incentivos Fiscais nas áreas da SUDAM e da SUDENE. As informações disponibilizadas aqui serão gerados no Registro N615: Informações da Base de Cálculo dos Incentivos Fiscais.
Nesta tela não será permitida a ação dos botões Novo,Copiar e Excluir.

Dados Gerais :
Recupera os dados de uma abertura de apuração.

Descrição dos campos

Parâmetros dos Incentivos Fiscais

Base de Cálculo: Informar/visualizar o valor da base de cálculo dos incentivos fiscais.
A informação desse campo, pode ser inserida manualmente pelo usuário ou o resultado do cálculo baseado nos registros N610 - Cálculo da Isenção e Redução do Imposto sobre o Lucro Real	e N630 - Cálculo do IRPJ Com Base no Lucro Real é exibido, em conformidade com a 	 definição no manual layout após a execução da rotina Cálculo dos Registros e Fórmulas na tela Processamento em Lote.
Obs.: Os campos definidos abaixo, só apresentam valores se houver valor no campo ‘Base de Cálculo’.

Base de Cálculo – Visualização da Base de Cálculo
Valor Limite 6% - Visualização do valor máximo que pode ser atribuído ao campo Valor Líquido.

Detalhamento dos Incentivos Fiscais

Épossível visualizar os valores correspondentes aos Incentivos Fiscais abaixo:
- FINOR (ATÉ 6%)
- FINAM (ATÉ 6%)
Os campos abaixo são exibidos para todos os incentivos fiscais:
Valor Líquido - Informar o valor líquido a ser concedido para o incentivo fiscal.
Percentual  - Visualização do percentual a ser concedido para o incentivo fiscal.

Total dos Incentivos
Valor Líquido - Visualização do somatório dos valores líquidos lançados.
Percentual - Visualização do somatório dos valores lançados em percentual dos incentivos ficais.


PAT

Nesta tela (Programa de Alimentaçã do Trabalhador – PAT) é possível obter a visualização dos dados do PAT que ocorreram durante o período base de apuração.
Na apuração do imposto trimestral ou anual, bem como no cálculo do imposto mensal sob a forma de estimativa, a pessoa jurídica tributada pelo lucro real, inscrita no PAT, poderá deduzir do imposto devido o valor equivalente à aplicação da alíquota do imposto (15%) sobre a soma das despesas de custeio realizadas no período de apuração.
A parcela do incentivo, a ser deduzida diretamente do imposto, está limitada a 4% do imposto devido em cada período-base de apuração.
O sistema permite a visualização dos cálculos do incentivo fiscal PAT – Programa de alimentação do trabalho apresentando as informações de cálculos do IRPJ mensal por estimativa (N620) ou IRPJ com base no lucro real (N630).

Dados Gerais :
Recupera os dados de uma Informação ECF.

Descrição dos campos
Ambas as abas (Mensal por Estimativa , ou Anual) possuem o mesmo conjunto de informações.


Valor do PAT Disponível de Períodos Anteriores  Permite visualização do valor acumulado do PAT de períodos anteriores disponível para utilização nos períodos posteriores.

Antes da Atualização:
Valor do PAT - Visualiza o valor de PAT de cada período. O valor de PAT corresponde à linha 9 do registro N620 ou linha 8 do N630.
Limite de 15% sobre o PAT - Visualiza o limite de 15% calculado sobre o PAT antes da atualização de cada período. Resultado N620 (9) * 0,15 ou N630 (8) * 0,15

Valor do Imposto Devido - Visualiza o valor do imposto de cada período. O valor do imposto corresponde à linha 3 do registro N620 ou do N630.
Limite de 4% sobre o Imposto Devido - Visualização do limite de 4% calculado sobre o imposto devido de cada período. Resultado N620 (3) * 0,04 ou N630 (3) * 0,04
Valor do PDTI/PDTA -Visualização do valor do incentivo PDTI/PDTA de cada período. O valor do PDTI/PDTA corresponde à linha 10 do registro N620 ou linha 9 do N630.
Limite de 4% com PDTI/PDTA - Visualização do limite de 4% com a dedução do incentivo PDTI/PDTA de cada período do registro N620 ou do anual do N630.
Valor Utilizado do PAT de Períodos Anteriores - Visualização do valor de PAT utilizado de períodos anteriores.
Valor do PAT Atualizado – Visualização do valor do PAT que será atualizado na linha 9 do registro N620 (em cada período) ou da linha 8 do N630 (anual).
Valor do PAT Disponível Neste Período para Uso Posterior - Permite visualização do valor do PAT não utilizado no período .

Os ajustes automáticos provenientes do incentiva PAT deverão ser controlados automaticamente em Conta da Parte B definida na Tela de Informações ECF, aba LALUR e LACS.


#### DEMONSTRAÇÕES


Após a realização  do processamento em lote é possível visualizar todas as informações das linhas da tabela dinâmica e das contas do plano referencial com os valores oriundos das contas contábeis associadas de acordo com os mapeamentos  ou dos valores inseridos por meio da tela Entrada Manual de Valores.

Com base na escrituração recuperada, serão demontrado (TreeViews) em cada período processado (Anual, Mensal e Trimestral) os seus respectivos registros.

Dados Gerais :
Recupera os dados de uma Informação ECF.
Após a seleção de um registro na lista de seleção, será possível verificar  os registros e apurações decorrente do processamento.




Exibição dos Dados

Apenas Registos com Movimento – Se selecionado,  apenas os registros com movimento serão apresentados, caso desmarcado, todas as linhas e informações serão apresentadas.

Descrição da Treview

Registros apresentados quando a forma de tributação for Lucro Real:
-K155
-K355
-L100
-L210
-L300
-M300
-M305
-M350
-M355
-M410
-Visualização do Lançamento da Parte B oriundo de Contrapartida
-M500
-N500
-N600
-N610
-N615
-N620
-N630
-N650
-N660
-N670


Períodos -  As abas são exibidas de acordo com a parametrização realizada. Exibe as abas de acordo com as opções:

Anual:
- Janeiro
- Fevereiro
- Março
- Abril
- Maio
- Junho
- Julho
- Agosto
- Setembro
- Outubro
- Novembro
- Dezembro
Trimestral
- 1º Trimestre
- 2° Trimestre
- 3º Trimestre
- 4º Trimestre

Grid Principal (lado esquerdo, parte superior) Visualização do detalhamento da composição das linhas  e/ou contas referenciais. Ao selecionar um registro na lista de seleção, o botão será habilitado e ao clicar será exibida a  tela Visualizar Detalhamento do Cálculo

Grid Secundária (lado esquerdo, parte inferior) Detalhamento do Cálculo
A tela possui campos diferente, pois o objetivo é exibir a composição dos valores das linhas da tabela dinâmica e das contas do plano referencial e tais linhas podem ser compostas por Contas Contábeis,Contas da Parte B, Entrada Manual de Valores e Fórmula. Logo abaixo consta as possibilidades de campos a serem exibidos na tela.

Contas Contábeis
A tela abaixo será exibida quando à linhas e/ou contas referenciais for composta por conta contábil.

PRINT DA TELA

Fórmula

A tela abaixo será exibida quando à linhas e/ou contas referenciais for composta por uma fórmula.


PRINT DA TELA

Entrada Manual

A tela abaixo é exibida quando a linha da tabela dinâmica for composta por uma entrada manual.



PRINT DA TELA

Conta da Parte B e Contas Contábeis

A tela abaixo será exibida quando a linha da tabela dinâmica for composta por  conta contábil e /ou conta da parte B. Esta tela será exclusivamente exibida para as linhas correspondentes aos registros do Bloco M.



Aba Contas Contábeis



PRINT DA TELA


Registros K155

BALANÇO (K155 E K156)
São apresentados os saldos iniciais, os saldos finais, os totais de débitos e os totais de créditos de todas as contas patrimoniais da escrituração societária da pessoa jurídica (Ativo, Passivo e Patrimônio Liquido), no período de apuração.

Print da tela



DEMONSTRAÇÃO DE RESULTADO (K355 E K356)

Os saldos finais de todas as contas de resultado da escrituração societária da pessoa jurídica antes do encerramento são apresentados.



Inserir print da tela

BALANÇO PATRIMONIAL (L100)

Apresenta o balanço patrimonial com base nas contas referenciais para o período de apuração.

Print da Tela


INFORMATIVO DE COMPOSIÇÃO DE CUSTOS (L210)

Permite informar a composição dos custos dos produtos de fabricação própria, vendidos e custos dos serviços prestados no período para as empresas que utilizam o inventário permanente.

Print da Tela

DEMONSTRATIVO DO RESULTADO DO LUCRO LÍQUIDO (L300)

Esta tela apresenta o demonstrativo do resultado do exercício para o período de apuração.
Print da Tela

LANÇAMENTOS M300, M305, M310 e M312
Permite a visualização do Resultado dos Lançamentos dos Registros M300, M305, M310 e M312.
Exibe valores correspondentes a CONTA DA PARTE B DO E-LALUR quando o tipo de tributo é Imposto de Renda da Pessoa Jurídica.
Os valores correspondentes a este registro, são recuperados automaticamente da tela Lançamentos da Parte A  quando há associação da conta da parte B na aba Contas da Parte B  - Ajustes M010 .
Print da Tela
LANÇAMENTOS M350, M355, M360 e M362

Permite a visualização do Resultado dos Lançamentos dos Registros M350, M355, M360 e M362 relacionados à apuração CSLL.
Exibe valores correspondentes a CONTA DA PARTE B DO E-LACS quando o tipo de tributo é Contribuição Social sobre o Lucro líquido. Os valores correspondentes a este registro, são recuperados automaticamente da tela Lançamentos da Parte A  quando há associação da conta da parte B na aba Contas da Parte B  - Ajustes M010 .

Print da tela
Controle de Saldos das Contas da Parte B do e-Lalur e do e-Lacs  (M500)
Permite a visualização do Controle das Contas da Parte B do e_Lalur e do e-Lacs  (registro M500).
Atenção: Este registro não é gerado pelo produto no meio magnético. Ele é criado pelo PVA.


Print da tela

Grupo da Conta -  Visualização do grupo da Conta da Parte B
Conta da Parte B – Visualização da conta da parte B.
Tributo – Visualização do tributo do registro.
Saldo Inicial -  Visualização do saldo inicial da conta da parte B
Lançamentos da Parte A – Visualização do valor total dos lançamentos da parte A.
Lançamentos da Parte B – Visualização do valor total dos lançamentos da parte B.
Lançamentos da ParteB - Contrapartida – Visualização do valor total dos lançamentos da parte b oriundos de contrapartida.
Saldo Final -  Visualização do saldo final  da conta da parte B



Visualização do Lançamento da Parte B oriundo de Contrapartida
Serão exibidos os valores correspondentes ao ajuste criado automaticamente a partir do preenchimento do campo contrapartida do registro M410. As informações exibidas nesta tela, estão diretamente ligadas com os lançamentos da parte B realizados na tela de Lançamentos Parte B (M410) sendo assim, qualquer alteração nestes lançamentos, será refletida nesta tela.

Print da tela

Grupo da Conta -  Visualização do grupo da Conta da Parte B
Conta da Parte B – Visualização da conta da parte B do registro de contrapartida.
Tributo – Visualização do tributo do registro de contrapartida.
Data Lançamento – Data do Lançamento de origem de contrapartida.
Valor – Visualização do valor e indicador do lançamento realizado para a contrapartida.
Conta Parte B Origem da Contrapartida: Visualização da conta da parte B que deu origem ao lançamento automático
Histórico – Visualização do histórico. Este conteúdo é gerado automaticamente pelo sistema  a fim de justificar os valores exibidos.
Exemplo:
Lançamento realizado automaticamente em 13/02/2017 devido ao preenchimento do campo Contrapartida.




BASE DE CÁLCULO (N500)

Permite a visualização dos Lançamentos da Base de Calculo do IRPJ referente ao Registro N500.
Para a linha 2 do registro N500, se existir a quebra por percentual de receita bruta, essas informações serão demonstradas.

Print da Tela

LUCRO DA EXPLORAÇÃO  (N600)

Permite a visualização do Resultado dos Lançamentos do Lucro da Exploração (Registro N600).

Print da Tela

ISENÇÃO DE REDUÇÃO DE IMPOSTO (N610)

Permite a visualização do Resultado dos Lançamentos do Registro N610.
Este registro lista o imposto de renda trimestral ou anual baseado em benefícios fiscais de redução ou isenção do imposto com base no Lucro da Exploração.

Print da Tela

INFORMAÇÕES DA BASE DE CÁLCULO DOS INCENTIVOS FISCAIS (N615)

Permite a visualização do Resultado dos Lançamentos do Registro N615 referente aos incentivos FINAM e FINOR.

Print da Tela


MENSAL POR ESTIMATIVA (N620)

A tela de resultado dos Registros N620 foi criada para permitir visualizar os dados da Demonstração do Resultado do cálculo do IRPJ mensal por estimativa.
Para este registro, quando na tela Complementares o campo Tipo de Receita estiver  selecionada a opção Comparativo e na tela Comparativo entre Receita Bruta X Balanço de Redução/Suspensão não for identificada confirmação de escolha  do tipo de receita, deverá ser exibido o campo abaixo, para selecionar a forma de visualização:

Visão por Tipo de Receita
- Receita Bruta
- Balanço de Suspensão/Redução
- Obs.: A opção “Balanço de Suspensão/Redução” se apresenta selecionada, por padrão.

Print da Tela

ANUAL (N630)

Nesta tela pode-se obter a visualização do Resultado dos Lançamentos do Registro N630. Apresenta o cálculo do IRPJ com base no Lucro Real.

Print da Tela

BASE DE CÁLCULO APÓS COMPENSAÇÃO DE BASE DE CÁLCULO NEGATIVA (N650)

Este registro é habilitado para a pessoa jurídica que apurou o imposto de renda com base no lucro real anual e que optou por apurar a CSLL por estimativa mensal.
Nesta tela é possível visualizar o Resultado dos Lançamentos do Registro N650. Para a linha 2 do registro N650, se existir a quebra por percentual de receita bruta, essas informações serão demonstradas.

Print da Tela

MENSAL POR ESTIMATIVA (N660)

Nesta tela pode-se obter a visualização do Resultado dos Lançamentos do Registro N660: Cálculo da CSLL Mensal por Estimativa.
Este registro é habilitado para a pessoa jurídica que apurou o imposto de renda com base no lucro real anual que optou por apurar a CSLL por estimativa mensal.
Para este registro, quando na tela Complementares a opção Comparativo do campo Tipo de Receita estiver  selecionada a e na tela Comparativo entre Receita Bruta X Balanço de Redução/Suspensão não for identificada confirmação de escolha  do tipo de receita, o campo abaixo deve ser exibido, para selecionar a forma de visualização:

Visão por Tipo de Receita
- Receita Bruta
- Balanço de Suspensão/Redução
- Obs.: A opção “Balanço de Suspensão/Redução” se apresenta selecionada, por padrão.
Print da Tela

ANUAL (N670)

Nesta tela é possível  obter a visualização dos Resultados dos Lançamentos do Registro N670.

Print da Tela

## BLOCO V – DECLARAÇÃO DEREX

### IMPORTAÇÃO

Esta tela tem por objetivo permitir a importação do bloco V. Registros que estão sendo atendidos na importação: V010, V020, V030 e V100.


A importação será realizada a partir da definição de um exercício e a recuperação de um registro de Informação ECF.

Os registros importados com sucesso, estarão disponíveis para consulta/alteração na tela de manutenção Declaração DEREX .
### MANUTENÇÃO



Esta tela tem por objetivo cadastrar as Declarações DEREX  (Bloco V) a serem  disponibilizadas no arquivo. Estas informações podem ser inseridas de forma manual, ou via importação de arquivos. Registros que estão sendo atendidos no bloco: V010, V020, V030 e V100.

Será necessário ter cadastrada na base uma Informação ECF, que atenda a característica do registro está sendo inserido.

As informações referente a esse bloco não são utilizadas no processamento em lote. Alguns registros possuem a hierarquia de registro pai e registro filho.

Para que um registro filho seja cadastrado, é necessário realizar previamente o cadastro do registro pai.
Para todos os registros selecionados, a tela no layout abaixo é exibida. A descrição dos campos é exibida de forma dinâmica conforme os campos de cada registro definido no manual layout disponibilizado pela RFB.





Registros Filhos
Se o registro selecionado possuir um registro filho, o mesmo será exibido,  abaixo do registro principal.
Para acessá-los é necessário cadastrar/consultar o registro pai.

## BLOCO W – DECLARAÇÃO PAÍS A PAÍS

### IMPORTAÇÃO

Esta tela tem por objetivo permitir a importação do bloco W.
Registros que estão sendo atendidos na importação: W100,W200,W250 e W300.


A importação será realizada a partir da definição de um exercício e a recuperação de um registro de Informação ECF.

Os registros importados com sucesso, estarão disponíveis para consulta/alteração na tela de manutenção Declaração País a País .

### MANUTENÇÃO



Esta tela tem por objetivo cadastrar as Declarações País a País  (Bloco W) a serem  disponibilizadas no arquivo. Estas informações podem ser inseridas de forma manual, ou via importação de arquivos. Registros que estão sendo atendidos do bloco: W100,W200,W250 e W300.
Será necessário ter cadastrada na base uma Informação ECF, que atenda a característica do registro está sendo inserido.

As informações referente a esse bloco não são utilizadas no processamento em lote. Alguns registros possuem a hierarquia de registro pai e registro filho.

Para que um registro filho seja cadastrado, é necessário realizar previamente o cadastro do registro pai.
Para todos os registros selecionados, a tela no layout abaixo é exibida. A descrição dos campos é exibida de forma dinâmica conforme os campos de cada registro definido no manual layout disponibilizado pela RFB.





Registros Filhos
Se o registro selecionado possuir um registro filho, o mesmo será exibido,  abaixo do registro principal.
Para acessá-los é necessário cadastrar/consultar o registro pai.


## BLOCO X e Y – INFORMAÇÕES ECONÔMICAS E GERAIS

### IMPORTAÇÃO

Esta tela tem por objetivo permitir a importação dos blocos X e Y. Registros que estão sendo atendidos na importação: X280,X291,X292,X300,X310.


A importação será realizada a partir da definição de um exercício e a recuperação de um registro de Informação ECF.

Os registros importados com sucesso, estarão disponíveis para consulta/alteração na tela de manutenção Blocos  X e Y -  Informações Econômicas e Gerais


### MANUTENÇÃO

Esta tela tem por objetivo cadastrar as Informações Econômicas e Gerais (Blocos X e Y) que serão disponibilizadas no meio magnético. Estas informações poderão ser inseridas de forma manual (através desta tela) ou via importação de arquivos. Registros que estão sendo atendidos do bloco: X280,X291,X292,X300,X310.
Será necessário ter cadastrada na base uma Informação ECF, que atenda a característica do registro está sendo inserido.

As informações referente a esses blocos não são utilizadas no processamento em lote.
Alguns registros possui a hierarquia de registro pai e registro filho. Para que um registro filho seja cadastrado, será necessário realizar previamente o cadastro do registro pai.
Obs.: Na tela, as linhas  das tabelas dinâmicas que possuem a  fórmula (linhas do Tipo CNA) são totalizadas automaticamente.
Print da Tela

A tela será alterada dinamicamente, de acordo com o preenchimento do campo Registros. Serão exibidos todos os campos de cada registro definido no manual layout disponibilizado pela RFB.

Registros Filhos
Se o registro selecionado possuir um registro filho, o mesmo será exibido,  abaixo do registro principal.
Para acessá-los é necessário cadastrar/consultar o registro pai.


## GERAÇÕES


### ECF


Permite a Geração do Arquivo ECF para que seja validado no PVA.

Descrição dos  campos
Exercício: Informar o exercício para ser utilizado para recuperar as escriturações, que deverão ser gerado o meio magnético. Este campo é de preenchimento obrigatório e deve ser utilizado ano igual ou maior que 2014.

Data Inicial: Informar a data inicial que será considerada para a geração do meio magnético. Este campo não é de preenchimento obrigatório. Caso esteja em branco, será considerada a data inicial da escrituração.

Data Final: : Informar a data inicial que será considerada para a geração do meio magnético. Este campo não é de preenchimento obrigatório e apenas será habilitado se o campo Data Inicial for preenchido. Caso esteja em branco, será considerada a data final da escrituração.

- Indicador de Início de Período – Selecionar/informar   o Indicador de início de Período. Exibe a lista de para selecionar as seguintes opções:
- 0 – Regular (Início no primeiro dia do ano);
- 1 – Abertura (Início de atividades no ano-calendário);
- 2 – Resultante de cisão/fusão ou remanescente de cisão, ou realizou incorporação;
- 3 – Resultante de Transformação;
- 4 – Início de obrigatoriedade da entrega no curso do ano calendário. (Ex. Exclusão do Simples Nacional ou desenquadramento como imune ou isenta do IRPJ);
Atenção: Quando a opção “0 – Regular (Início no primeiro dia do ano)” é selecionada, só estarão disponíveis para o processamento, as escriturações  cuja a Data Inicial na tela Informações ECF esteja preenchida com o primeiro dia do ano ficam disponíveis para seleção.
Quando a opção  “1 – Abertura (Início de atividades no ano-calendário)” é selecionada, só estarão disponíveis para o processamento, as escriturações cuja a Data Inicial na tela Informações ECF esteja preenchida com data inicial após  o primeiro dia do ano são disponibilizados para seleção.

Plano de Contas e Centro de Custos - Selecionar o tipo de movimentação dos registros, só os registros com movimentação no período selecionado ou todos os registros.
Se tratando da geração de um arquivo de retificação, as informações referentes aos campos Retificadora e Número do Recido Anterior devem ser preenchidas.

- Retificadora - Selecionar/informar   o tipo de informação retificadora. Exibe a lista de para selecionar as seguintes opções:
- S – ECF retificadora
- N – ECF original
- F – ECF original com mudança de forma de tributação

- Número do Recibo Anterior -Informa o número do recibo caso seja  um arquivo de retificação. Só será habilitado este campo se o campo Retificadora estiver preenchido com as opções:
Escriturações dos Estabelecimentos

Selecionar o item da lista de seleção que deseja executar o processamento e clicar em “Processar” para iniciar o processamento. A seleção pode ser feita manualmente (selecionando quantos registros houver necessidade)  e utilizando o Check-box – Marcar Todos que permite selecieonar todos os registros que estão na grid.
Selecionar: Permite pesquisar dentre a seleção de registros que estão em condições de executar o processamento.

## RELATÓRIOS


### CONFERÊNCIA DO LUCRO REAL


O objetivo dos relatórios deste item é de exibir as informações dos registros do Lucro Real.

#### DEMONSTRAÇÕES

Será possível gerar o relatório para mais de uma Informação ECF , selecionar mais de um registro e escolher a forma como o arquivo será gravado ( único arquivo ou por quebra de Informações ECF).
Registros que estão sendo atendidos neste relatório: Bloco L ( L100,L210,L300) e Bloco K (K155-K156, K355-K356).

#### LALUR/LACS

Será possível gerar o relatório para mais de uma Informação ECF , selecionar mais de um registro e escolher a forma como o arquivo será gravado ( único arquivo ou por quebra de Informações ECF).
Registros que estão sendo atendidos neste relatório: Bloco M (M300-M310-M312,M350-M360-M362,M410-M415, M500).

#### APURAÇÃO IRPJ/CSLL

Será possível gerar o relatório para mais de uma Informação ECF , selecionar mais de um registro e escolher a forma como o arquivo será gravado ( único arquivo ou por quebra de Informações ECF).
Registros que estão sendo atendidos neste relatório: Bloco N (N500, N600,N610, N615,N620,N630,N650, N660, N670).


### CONFERÊNCIA DA DECLARAÇÃO PAÍS A PAÍS -BLOCO W

O objetivo deste relatório é de exibir as informações dos registros W – Declaração País a País.
Será possível gerar o relatório para mais de uma Informação ECF , selecionar mais de um registro do blocos W e escolher a forma como o arquivo será gravado ( único arquivo ou por quebra de Informações ECF).
Registros que estão sendo atendidos do bloco: W100,W200,W250 e W300.

### CONFERÊNCIA DAS INFORMAÇÕES ECONÔMICAS E GERAIS - BLOCOS X E Y


O objetivo deste relatório é de exibir as informações dos registros X – Informações Econômicas e dos registros Y – Informações Gerais.
Será possível gerar o relatório para mais de uma Informação ECF , selecionar mais de um registro dos blocos x ,y e escolher a forma como o arquivo será gravado ( único arquivo ou por quebra de Informações ECF).

Registros que estão sendo atendidos do bloco: X280, X291, X292,X300 e X310.



## RECUPERAÇÃO DE REGISTROS:

### INFORMAÇÕES ECF:

A pesquisa pela Informação ECF , pode ser feita pelos campos abaixo, usando os possíveis domínios:

Cod Estab – Deve ser informado o código do estabelecimento da Informação ECF
Exercício  - Deve ser informado o exercício da Informação ECF (Formato: AAAA)
Data Inicial -  Deve ser informada a Data Inicial da Informação ECF (Formato: DD/MM/AAAA)
Cod Versão - Deve ser informada a Versão da Informação ECF (Opções Válidas)
Forma Tributação – Deve ser informada a Forma de Tributação da Informação ECF (Opções Válidas: (REAL_PRES_ARBIT, IMUNE, ISENTO)
Onde:REAL_PRES_ARBIT = Lucro Real, Lucro Presumido ou Lucro Arbitrado
IMUNE = Imune de IRPJ
ISENTO= Isento do IRPJ
Apuração  - Deve ser informada a Apuração da Informação ECF (Opções Válidas: 1, 2), onde 1 = Trimestral e 2 = Anual.
### ABERTURA DE APURAÇÃO:

A pesquisa pela abertura , pode ser feita pelos campos abaixo, usando os possíveis domínios:

Cod Estab – Deve ser informado o código do estabelecimento da Informação ECF
Exercício  - Deve ser informado o exercício da Informação ECF (Formato: AAAA)
Data Inicial -  Deve ser informada a Data Inicial da Informação ECF (Formato: DD/MM/AAAA)
Cod Versão - Deve ser informada a Versão da Informação ECF (Opções Válidas:)
Forma Tributação – Deve ser informada a Forma de Tributação da Abertura da Apuração (Opções Válidas: (REAL, PRES, ARBIT, IMUNE, ISENTO)
Onde: REAL - Lucro Real
PRES - Lucro Presumido
ARBIT - Lucro Arbitrado
IMUNE - Imune de IRPJ
ISENTO - Isento do IRPJ)
Apuração -  Deve ser informada a Apuração da Abertura (Opções Válidas: 1, 2), onde: 1 = Trimestral , 2= Anual
Período Apuração – Deve ser informado o período da Apuração da Abertura (Opções Válidas: A01,A02, A03, A04,A05, A06, A07, A08, A09, A10, A11 e A12).
Onde A01 = Janeiro, A02 = Fevereiro , ... A12 = Dezembro.
Status – deve ser informado o status da Abertura da Apuração (opções Válidas: APURACAOABERTA, AGUARDANDOALTERACAOMANUAL, ALTERACAOMANUALREALIZADA, CALCULOREALIZADO, IMPORTACAOSALDOSREALIZADA e REAPURAR.
Onde: APURACAOABERTA=Apuracao em Aberto;
IMPORTACAOSALDOSREALIZADA= Importacao dos Saldos Realizada;
AGUARDANDOALTERACAOMANUAL= Aguardando Ajuste Manual
ALTERACAOMANUALREALIZADA= Alteração Manual Realizada;
CALCULOREALIZADO= Calculo Realizado;
REAPURAR - Reapurar


## LISTAS DE OPÇÕES:


Versão:

- 1.00– Ano Calendário 2014 e Situações Especiais de 2015, para data inicial compreendida no ano de 2014 e 2015. Não está sendo atendida no produto
- 2.00 – Ano Calendário 2015 e Situações Especiais de 2016, para data inicial compreendida no ano de 2015 e 2016. Não está sendo atendida no produto
- 3.00 – Ano Calendário 2016 e Situações Especiais de 2017, para data inicial compreendida no ano de 2016 e 2017.
- 4.00 – Ano Calendário 2017 e Situações Especiais de 2018, para data inicial compreendida no ano de 2017 e anos posteriores.

Registros de Tabela Referencial:
Informações oriundas da TFIX91:



Registros de Tabela Dinâmica:

Informações oriundas da TFIX88

## SIGLAS UTILIZADAS NO ECF

CNAE – Cadastro Nacional de Atividade Econômica
CNPJ – Cadastro Nacional de Pessoa Jurídica
CPF – Cadastro de Pessoa Física
CSLL – Contribuição Social sobre o Lucro Líquido
ECF – Escrituração Contábil Fiscal
eLACS – Livro eletrônico de Escrituração e Apuração da Contribuição Social
eLALUR – Livro  eletrônico de Apuração do Lucro Real
FCONT – Controle Fiscal Contábil de Transição
IRPJ – Imposto de Renda da Pessoa Jurídica
Padis - Programa de Apoio ao Desenvolvimento Tecnológico da Indústria de Semicondutores
PAES – Programa Seletivo de Acesso à Educação Superior
PAT – Programa de Alimentação do Trabalhador
PDTI - Programa de Desenvolvimento Tecnológico Industrial
PDTA - Programa de Desenvolvimento Tecnológico Agropecuário
PATVD  - Programa de Apoio ao Desenvolvimento Tecnológico da Indústria de Equipamentos para TV Digital
PJ – Pessoa Jurídica
Recap – Regime especial de aquisição de bens de capital para empresas exportadoras
REFIS – Programa de Recuperação Fiscal
Repes - Regime Especial de Tributação para a Plataforma de Exportação de Serviços de Tecnologia da Informação
Retid - Regime Especial Tributário para a Indústria de Defesa
Reidi - Regime Especial de Incentivos e Desenvolvimento da Infraestrutura
Repenec - Regime Especial de Incentivos para o Desenvolvimento da Infraestrutura da Indústria Petrolífera das Regiões Norte, Nordeste e Centro-Oeste
Reicomp - Regime Especial de Incentivo a Computadores para Uso Educacional
Retaero - Regime Especial para a Indústria Aeronáutica Brasileira
Recine - Regime Especial de Tributação para Desenvolvimento da Atividade de Exibição Regime Especial para a Indústria Aeronáutica Brasileira Cinematográfica
Recopa - Regime Especial de Tributação para construção, ampliação, reforma ou modernização de estádios de futebol
REPNBL – Redes - Regime Especial de Tributação para construção, ampliação, reforma ou modernização de estádios de futebol
Reif - Regime Especial de Incentivo ao Desenvolvimento da Infraestrutura da Indústria de Fertilizantes
RTT – Regime tributário de Transição
SCP –   Sóciedade em conta de Participação
SELIC - Taxa referencial do Sistema Especial de Liquidação e de Custódia
TJLP – Taxa de Juros a Longo Prazo
UF – Unidade da Federação



## SUPORTE TÉCNICO


Para dúvidas ou problemas, abra um chamado no Contact Center ou entre em contato com nossa equipe de Suporte Técnico pelo Telefone:

 (11) 2159-0600 opção 1 (Atendimento das Soluções Fiscais).
Nosso horário de atendimento é de segunda à sexta-feira de 9h às 18h.


|  | Registro M300 - Janeiro |  |
| --- | --- | --- |
|  |  |  |
| Linha | Descrição | Valor |
|  |  |  |
| Adição |  |  |
| 6 | Provisões Não Dedutíveis | 300,00 |
| Exclusão |  |  |
| 95 | (-) Reversão dos Saldos das Provisões Não Dedutíveis | 250,00 |
|  |  |  |
|  | Registro M300 - Fevereiro |  |
|  |  |  |
| Linha | Descrição | Valor |
|  |  |  |
| Adição |  |  |
| 6 | Provisões Não Dedutíveis | 1300,00 |
| Exclusão |  |  |
| 95 | (-) Reversão dos Saldos das Provisões Não Dedutíveis | 1100,00 |
|  |  |  |


|  | Linhas da ECF - Registro M300/M350 | Linhas da ECF - Registro M300/M350 | Linhas da ECF - Registro M300/M350 | Linhas da ECF - Registro M300/M350 | Linhas da ECF - Registro M300/M350 | Linhas da ECF - Registro M300/M350 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
|  | Jan | Fev | Mar | Abr | Mai | Jun |  |
| Adição | - | - | - | - | - | - |  |
|  |  |  |  |  |  |  |  |
| Exclusão | 100,00 | 100,00 | 100,00 | 400,00 | 200,00 | 500,00 |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


|  |  |  |
| --- | --- | --- |
|  | Registro M300 - Janeiro |  |
|  |  |  |
| Linha | Descrição | Valor |
|  |  |  |
| Adição |  |  |
| 6 | Provisões Não Dedutíveis | - |
| Exclusão |  |  |
| 95 | (-) Reversão dos Saldos das Provisões Não Dedutíveis | 50,00 |
|  |  |  |
|  | Registro M300 - Fevereiro |  |
|  |  |  |
| Linha | Descrição | Valor |
|  |  |  |
| Adição |  |  |
| 6 | Provisões Não Dedutíveis | - |
| Exclusão |  |  |
| 95 | (-) Reversão dos Saldos das Provisões Não Dedutíveis | 200,00 |
|  |  |  |
|  |  |  |


|  | Registro M300 - Janeiro |  |
| --- | --- | --- |
|  |  |  |
| Linha | Descrição | Valor |
|  |  |  |
| Adição |  |  |
| 6 | Provisões Não Dedutíveis | 100,00 |
| Exclusão |  |  |
| 95 | (-) Reversão dos Saldos das Provisões Não Dedutíveis | 50,00 |
|  |  |  |
|  | Registro M300 - Fevereiro |  |
|  |  |  |
| Linha | Descrição | Valor |
|  |  |  |
| Adição |  |  |
| 6 | Provisões Não Dedutíveis | 600,00 |
| Exclusão |  |  |
| 95 | (-) Reversão dos Saldos das Provisões Não Dedutíveis | 400,00 |
|  |  |  |


| Atividade | Conta referencial | Total calculado | Total para percentual | Percentual por atividade |
| --- | --- | --- | --- | --- |
| Atividade Geral | 3.01.01.01 | 5.000,00 | 14.000,00 | 35,71% |
| Atividade Rural | 3.11.01.01 | 9.000,00 |  | 64,29% |


| Conta contábil | Conta  referencial | Total calculado | Percentual | Rateio |
| --- | --- | --- | --- | --- |
| A | 3.01.01.01.01.01 | 2.000,00 | 35,71% | 714,29 |
| A | 3.11.01.01.01.01 | 2.000,00 | 64,29% | 1.285,71 |


| Conta contábil | Conta  referencial | Total calculado | Percentual | Rateio |
| --- | --- | --- | --- | --- |
| A | 3.01.01.01.01.01 | 2.000,00 | 35,71% | 714,29 |
| A | 3.11.01.01.01.01 | 2.000,00 | 64,29% | 1.285,71 |
| A | 3.11.01.01.01.02 | 2.000,00 | 64,29% | 1.285,71 |


| Atividade | Conta referencial | Total calculado | Total para percentual | Percentual por atividade |
| --- | --- | --- | --- | --- |
| Atividade Geral | 3.01.01.01 | 5.000,00 | 14.000,00 | 35,71% |
| Atividade Rural | 3.01.11.01 | 9.000,00 |  | 64,29% |

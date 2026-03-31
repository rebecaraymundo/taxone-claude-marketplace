# ECD_Livros_SPED_Matriz_V2

> Fonte: ECD_Livros_SPED_Matriz_V2.doc

TITLE  "ECD - Livros SPED (Matriz)"  \* MERGEFORMAT ECD - Livros SPED (Matriz)


DOCUMENTO DE REQUISITo

DR	Nome	Descrição		OS2328I	ECD – Livros Auxiliares R e A (Matriz) 	Atualmente a Mastersaf gera somente o Livro G “Diário Geral” para atendimento do SPED, porém, existem os livros R “Diário Resumido” e A “Diário Auxiliar” que deverão ser atendidos pela Mastersaf, tanto para empresas normais como instituições financeiras como é o caso da Yamaha, que gera as informações com base no plano de contas COSIF.
Essa OS deve atender a geração dos os livros R – Diário Resumido e A – Diário Auxiliar para as instituições financeiras e empresas em geral.		
OS2328IB	
ECD – Livros Auxiliares R e A (Matriz) 	Atualmente a Mastersaf gera somente o Livro G “Diário Geral” para atendimento do SPED, porém, existem os livros R “Diário Resumido” e A “Diário Auxiliar” que deverão ser atendidos pela Mastersaf, tanto para empresas normais como instituições financeiras como é o caso da Yamaha, que gera as informações com base no plano de contas COSIF.
Essa OS deve atender a geração dos os livros R – Diário Resumido e A – Diário Auxiliar para as instituições financeiras e empresas em geral.		OS2328-N	Ajustes – Livros SPED “G, R e A”	Conforme especificado acima, o sistema realmente tem uma falha na apresentação dos C.C na forma horizontal, pois desse jeito o mesmo tem um tamanho limitado, onde facilmente o cliente estoura o campo e não consegue fazer o relacionamento correto. O Objetivo dessa OS para esse problema, é alterar o sistema, de forma que a gravação e apresentação dos C.C para as contas contábeis, seja feita de forma vertical assim como é feito no “De/Para”.
Também foi visto outra situação que o sistema não esta atendendo, este não permiti na tela da “DRE” a gravação de duas contas iguais para código de aglutinação diferentes. Sendo assim, essa OS também terá o objetivo de alterar essa esquemática atual permitindo a gravação dos mesmos.
		OS2328-O	Ajustes – Livros SPED	Na geração do SPED Contábil. Surgiram situações, que a Mastersaf no seu módulo “ECD” Escrituração Contábil Digital não esta preparada para atender. A exemplo, temos alguns casos, como a gravação de perfil diferentes por empresa, a geração de DRE/BP diferentes por empresas, a permissão de que a parametrização feita para os códigos de aglutinação possa ser replicada para outras empresas, não sendo necessário a repetição desses parâmetros. Que o termo de abertura/encerramento possa ser feito por empresa Conforme especificado acima, essas situações não são atendidas hoje pelo Mastersaf, por isso, o objetivo desse documento, é de incluir os parâmetros necessários para que a geração das informações acima, possa ser feita por empresa Centralizador/Descentralizado.		OS2328-G1	Melhorias solicitadas pelos clientes Usiminas/Karsten	Foram solicitadas algumas melhorias no SPED Contábil que conforme apontado pelos clientes são de extrema importância para facilitar o dia a dia dos usuários do programa. Sendo assim, o objetivo dessa OS é atender as sugestões dos clientes inserindo novas informações no programa de forma que o mesmo seja uma ferramenta para que facilite o trabalho do usuário.		OS2328-L	Tratamento do Livro Z – Razão Auxiliar	Atualmente a Mastersaf gera o Livro G “Diário Geral” para atendimento do SPED, R “Diário Resumido” e A “Diário Auxiliar”, porém, existe o livro tipo “Z” Razão Auxiliar que ainda não é atendido pela Mastersaf. O objetivo dessa OS é tratar da geração deste livro para atendimento ao SPED Contábil, fazendo o tratamento tanto para empresas normais como para instituições financeiras.		OS2328M	Ajuste das demonstrações consolidadas ou de outros empresários.	As demonstrações financeiras das filiais, sucursais, controladas ou coligadas, no exterior, precisam ser apresentadas no SPED Contábil juntamente com as demonstrações próprias da empresa. Porém, estas precisam estar identificadas no registro J005 com a opção “2” no campo de identificação das demonstrações com (Demonstrações consolidadas ou de outros empresários ou sociedade empresárias) e abaixo nos registros J100 e J150 viriam as demonstrações da coligada, controlada etc..., logo o objetivo dessa OS  fazer com que o sistema aceite mais de um arquivo “RTF” e gere para cada arquivo um registro J800. Consideraremos também a geração de mais de um J005.		CH59678	Alteração de RN conforme Infolegis	Devido emissão de INFOLEGIS_229_09_F_ECD_IN_926.doc os registros I350 e I355 não deverão ser gerados para os livros tipo “A e Z”.		CH59112
	Alterar modo de visualização de signatários
	Alterar a forma de como o sistema recupera as informações dos responsáveis legais para a tabela SPED_DADOS_SIGNATARIO, a fim de recuperar também os indicadores de cada Nome/Razão Social.		OS2328-P	Subtotalizador e Totalizador Para BP
	Atualmente na tela da DRE do SPED Contábil, o sistema possui no cadastro dos códigos de aglutinação, no campo “Classificação”, uma funcionalidade chamada  totalizador/subtotalizador. O objetivo dessa OS é de replicar a parametrização existente na tela da DRE para a tela do BP( Balanço Patrimonial).		CH59742	Relacionamento de contas e C.C.	O cliente solicita que na emissão do relatório das contas de aglutinação (Balanço Patrimonial e Demonstração de Resultado) as contas analíticas e C.C relacionados também sejam apresentadas. Como ocorria na release 31 e que na 32 não esta ocorrendo.		CH57895	Erro na geração do registro I200	Atualmente quando o sistema identifica a existência de lançamentos feitos a crédito ele soma essas partidas e gera o campo 4 do registro I200 com o valor total dessas partidas.
Porém quando não há partidas a crédito ma X101, e somente existem débitos o procedimento que deveria ser o mesmo não ocorre. Então o resultado do campo 4 do registro I200 = zero. O Objetivo desses CH é replicar a regra acima para as partidas a débito.		OS2328-U	Criação Safx2101 (Plano de Contas Referencial X Plano de Contas Safx2002)	Criar uma tabela Safx, para que o usuário possa importar e exportar a parametrização através do Job Servidor, reduzindo a manutenção através do módulo ECD - Escrituração Contábil Digital.
A nova tabela Safx deverá conter informações que atualmente são armazenadas em duas tabelas, SPED_CONTAS_REF_CCUSTO e SPED_CONTAS_REF_EMP.
		OS2328-J1	Livro Tipo “B” Balancetes Diários.	Para geração do SPED Contábil, as empresas que são classificadas como Instituições Financeiras, além de fazer a geração de suas obrigações com base no Plano de contas disponibilizado pelo Banco Central do Brasil denominado COSIF, também devem gerar um livro específico, chamado “Livro tipo B – Balancetes Diários e Balanços.
Atualmente o MSAF não atende a geração desse livro.		CH61131	SPED – Lançamentos Contábeis	Quando o mastersaf encontra lançamentos, cujo “número é o mesmo”, se o arquivamento for igual dentro do mesmo período para mesma conta, o sistema esta fazendo o cálculo entre elas, o que não deveria acontecer, pois, o registro I250 demonstra o detalhe das partidas do lançamento.
Sendo assim, esse cenário deverá ser alterado nesse chamado.		CH64207	SPED – De/Para	Atualmente o mastersaf trata o relacionamento das contas do DE/Para (empresa x Referencial) levando em consideração a data de validade do referencial COSIF. Esse CH tem como objetivo de retirar essa consideração.		CH64346	Registro I012	O sistema não está recuperando a informação correta do campo 03 (NAT_LIVR) para o registro I012 do SPED Contábil, o objetivo do documento é criar regra de negócio direcionando para a informação correta.		CH64454	Aglutinação Balanço/DRE	No Balanço Patrimonial só era possível realizar a parametrização das contas cuja natureza seja ativo, passivo ou patrimônio líquido, conforme regra criada na OS2328-F		CH63450	SPED – De X Para	Inserir estabelecimento na tela de plano referencial x plano empresa		CH65081	Geração registro J150	Alterar regra para gerar validação do registro J150 com opção de “Omitir informação de centro de custo”, estiver marcada.		CH65041	Alteração da busca no NIRE	Na Tabela REGISTRO_ESTADUAL existe o campo referente ao NIRE (Número de Inscrição no Registro de Empresas), esse campo deve ser carregado normalmente com os pontos separadores nessa tabela.
Porém, quando da geração do SPED Contábil o NIRE deve ser levado para o registro I030 no campo 07 sem dos separadores, uma vez que o campo é do tipo “number”.		2328-V	Colocar mensagem no relacionamento entre as contas no De/Para	Colocação de uma mensagem que informe ao usuário a associação de uma Conta Empresa a mais de uma Conta Referencial.		2328-R4	Melhoria na tela de seleão do signatário	Alteração na tela de seleção do signatário nos dados inciais do SPED Contábil.		OS2328-R3	Relatório valorado do B.P e da DRE 	Será criado um relatório que irá apresentar a estrutura de códigos de aglutinação criada para o Balanço Patrimonial e para a Demonstração de Resultado. Além da estrutura o relatório irá demonstrar os valores referentes a cada um dos códigos de aglutinação, de acordo com a parametrização de aglutinação feita nesse mesmo módulo.		2328-N2	Geração registro J005	Alteração na forma de geração da data inicial e final do registro J005		OS2848	Parametrização do Número de Ordem
	Disponibilizar para o usuário uma parametrização prévia do número de ordem a ser utilizado nos arquivos da ECD de cada período, assim, o usuário poderá informar antecipadamente o número de ordem para todos os arquivos da ECD que serão gerados no ano calendário.		CH77588	Alteração na regra de geração do registro J100 e J150	Alteração na forma de geração dos registro J100 e J150
		CH62988-A	Incluir a coluna ‘Num CRC’ na seleção do responsável legal.	Deve ser adicionada a coluna ‘Num CRC’ na janela de seleção do responsável legal existente nos dados iniciais da ECD.		OS3042	Parâmetro Controle da Obrigação	Alteração do processo de exclusão do Histórico dos Livros Gerados.		OS2328-R2	Alteração na regra de ordenação dos Códigos de Aglutinação inseridos manualmente.	Ordenar os Códigos de Aglutinação Automaticamente ao inserir um novo registro.		OS3042	Parâmetro Controle da Obrigação	Alteração do processo de exclusão do Histórico dos Livros Gerados. Ajuste conforme solicitação da Fabrica.		

REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN00	Na tela Parâmetros >Perfil, quando o usuário selecionar o “Perfil” (R – Livro Diário com Escrituração Resumida (com Escrituração Auxiliar)), os registros obrigatórios serão exibidos, porém não habilitados para opção de geração ou não do cliente; Obs: essa mesma regra aplica-se quando o usuário selecionar o “Perfil” (A – Livro Diário Auxiliar ao Diário com Escrituração Resumida)	OS2328I_2		RN01	Se selecionado registro com nível superior aos anteriores que não tenham sido marcados, o sistema deverá marcar automaticamente no momento da seleção. Obs: essa mesma regra aplica-se quando o usuário selecionar o “Perfil” (A – Livro Diário Auxiliar ao Diário com Escrituração Resumida)	OS2328I_2		RN02	Ao definir um tipo de livro no perfil, os demais livros deverão ficar desabilitados para seleção dos registros a serem gerados; Obs: essa mesma regra aplica-se quando o usuário selecionar o “Perfil” (A – Livro Diário Auxiliar ao Diário com Escrituração Resumida).	OS2328I_2		RN03	Os registros que deverão ser exibidos, quando da seleção do livro “[x] R – Livro Diário com Escrituração Resumida (com Escrituração Auxiliar)” são os registros que estão grifados em vermelho no documento de requisitos na composição dos livros. Obs: Essa mesma regra aplica-se quando o usuário selecionar o “Perfil” (A – Livro Diário Auxiliar ao Diário com Escrituração Resumida).	OS2328I_2		RN04	A informação “Entidade responsável pelo plano de contas Referencial”, por regra padrão vem como Secretaria da Receita Federal, porém, Instituições Financeiras deverão selecionar a opção “20 – Banco Central do Brasil (COSIF)”, tal informação deverá ser considerada para realização do DEPARA entre contas referencial  x contas da empresa;	OS2328I_1		RN05	Quando o Usuário Selecionar a entidade responsável pelo Plano de contas como “20 – Banco Central do Brasil (COSIF)”, será apresentado ao lado direito da tela, uma caixa chamado Títulos.	OS2328I_1		RN06	A Caixa acima terá 21 opções de títulos para que o usuário possa marcá-los, conforme segue:
            
             U - Bancos múltiplos;
             B - Bancos Comerciais;
             D - Bancos de Desenvolvimento;
             K - Agências de Fomento ou de Desenvolvimento;
             I  - Bancos de Investimento;
             F - Sociedades de Crédito, Financiamento e Investimento;
             J - Sociedades de Crédito ao Microempreendedor;
             A - Sociedades de Arrendamento Mercantil;
             C - Sociedades Corretoras de Títulos e Valores Mobiliários e Câmbio;
             T - Sociedades Distribuidoras de Títulos e Valores Mobiliários;
             S - Sociedades de Crédito Imobiliário e Associações de Poupança e Empréstimo;
             W - Companhias Hipotecárias;
             E - Caixas Econômicas;
             R - Cooperativas de Crédito;
             O - Fundos de Investimento;
             L - Banco do Brasil S.A.;
             M - Caixa Econômica Federal;
             N - Banco Nacional de Desenvolvimento Econômico e Social;
             H - Administradoras de Consórcio;
             P- Grupos de Consórcio; 	
             Z - Empresas em Liquidação Extrajudicial.
	OS2328I_1		RN07	Os Títulos da regra acima terão ao seu lado esquerdo um “check box” para cada um, que permitirão ao usuário selecioná-los. Podendo ser um ou mais ao mesmo tempo.	OS2328I_1		RN08	Na tela de “Dados Adicionais” essa Caixa “Títulos” só será apresentada para cliente s que utilizem na seleção da entidade responsável o plano de contas “20 – Banco Central do Brasil (COSIF).	OS2328I_1		RN09	Consistir se existir distinta informação de Entidade responsável pelo plano de contas referencial entre os estabelecimentos apresentados em tela de dados iniciais;	OS2328I_1		RN10	“Gerar Plano de Contas (Empresa):completo/contas movimentadas” ficará a critério do usuário a definição das informações a serem consideradas no registro I050, pois existem clientes com volume muito grande de dados (7 milhões), onde os mesmos poderão definir apenas contas movimentadas no período de geração;	OS2328I_1		RN11	“Omitir informação Centro de Custo em lançamentos Contábeis e Saldos” ficará selecionada por definição padrão, pois caso não seja omitida tal informação o validador SPED Contábil fará checagem de saldos por centro de custo versus lançamentos. Obs: Dificilmente as empresas operam com saldos por centro de custo, pois tal controle é para efeito gerencial	OS2328I_1		RN12	A identificação dos signatários deverá permitir a seleção de vários responsáveis, porém o código de classificação correspondente ao signatário será a partir da tabela definida pelo SPED Contábil do registro J930 campo 05.	OS2328I_1		RN13	A Seleção feita pelo usuário no quadro de “Títulos” nessa tela de “Dados Adicionais” impactará nas informações apresentadas nas telas do “Plano de contas Referencial” e “Plano de contas Referencial X Plano de Contas Empresa” conforme regra RN14.	OS2328I_2		RN14	O usuário poderá selecionar um ou mais títulos nessa tela, isso fará com que as informações apresentadas nas telas “Plano de contas Referencial” e “Plano de contas Referencial X Plano de Contas Empresa” sejam alteradas conforme esta parametrização.	OS2328I_2		RN15	Em baixo da caixa “Títulos” terá a seguinte mensagem: (*Títulos – Informar apenas para filtro das contas contábeis que queria visualizar no Plano de Contas Referencial). 	OS2328I_2		RN16	Este cadastro estará disponível apenas para os livros tipo “A” (Livro Diário Auxiliar ao Diário com Escrituração Resumida) e tipo “Z” (Razão Auxiliar). Obs: Essa OS trata apenas da Regra para o Livro “A” e “R”, sendo assim não falaremos do livro “Z” no momento.	OS2328I_2		RN17	No campo “Livro (Cód./Desc.)” o usuário deverá informar uma codificação interna e a descrição para controle do tipo de Livro Auxiliar (Ex.: 001)	OS2328I_2		RN18	No campo “Tipo de Escrituração” o usuário deverá selecionar qual é o tipo de escrituração do livro, podendo ser: 0 - Digital (incluídos no SPED) ou 1 - Outros	OS2328I_2		RN19	No campo “Tipo de Livro” o usuário poderá selecionar o livro tipo “A - Livro Diário Auxiliar ao Diário com Escrituração Resumida" ou tipo “Z - Razão Auxiliar”. Obs: Essa OS trata apenas da Regra para o Livro “A” e “R”, sendo assim não falaremos do livro “Z” no momento.	OS2328I_2		RN20	No campo “Descritivo do Livro para o SPED” o usuário deverá digitar qual será a descrição do livro Auxiliar a ser apresentada no arquivo digital do SPED. Esta descrição pode ser diferente da utilizada no campo "Livro (Cód./Desc)”. 	OS2328I_2		RN21	No campo “Cód. HASH do Arquivo correspondente ao Livro Auxiliar” o usuário deverá Incluir o Código Hash do Livro Auxiliar em questão. Esse código digital é recebido pela Empresa no momento em que o Livro Auxiliar é registrado, tornando-se oficial.	OS2328I_2		RN22	No campo “Informar Conta para a Pesquisa” o usuário irá Informar o código da Conta Analítica para a pesquisa, isso fará com que essa conta seja apresentada no quadro “Contas da empresa a selecionar”. O usuário também poderá clicar diretamente em "Pesquisar" e o sistema apresentará a lista de todas as contas analíticas para seleção. 	OS2328I_2		RN23	No quadro “Contas da Empresa a Selecionar” será apresentado as contas que foram encontradas a partir da pesquisa, efetuada na Regra acima (RN19). O usuário deverá selecionar a Conta Analítica que será associada ao Livro Auxiliar indicado e clicar no botão "Adicionar Contas". 	OS2328I_2		RN24	No Quadro “Contas da Empresa Selecionadas” será apresentado a lista de contas que foram adicionadas após a regra acima (RN20).	OS2328I_2		RN25	Após ter adicionado a conta selecionada conforme regras (RN22, RN23 e RN24) o usuário deverá confirmar a inclusão, acionando o botão “ EMBED PBrush  ” (Confirma).	OS2328I_2		RN26	[ALTERADA – OS2848] Esta telá servirá para definir para cada livro sua periodicidade e número de ordem para geração da obrigação; Obs: Os livros auxiliares seguem a mesma periodicidade e regras de controle dos livros oficiais.	OS2328I_2		RN27	As informações do quadro “Histórico de livros gerados” serão tratadas pelo processo de geração, demonstrando ao cliente ultimo livro gerado.	OS2328I_2		RN28	A informação de periodicidade do livro é meramente informativa, não implicara na periodicidade de geração da obrigação. O usuário poderá gerar qualquer período através de data inicial e final, independentemente da periodicidade informada no controle da obrigação.	OS2328I_2		RN29	No campo “Estabelecimento” no caso de centralização de escrituração contábil, o sistema trará o Estabelecimento definido como sendo o centralizador (Menu Básicos » Parâmetros » Preliminares » HYPERLINK "E:\\MsafDW\\documentacao funcional\\MsafDW\\documentacao funcional\\Documento Matriz\\Tecnologia\\REQ_CONT_MSAFEXE\\V1R31.0\\Executaveis\\Help_on_Line\\basicos\\parametros\\oper_safpr.htm" \l "centr_escrit_contabil"Centralização da Escrituração Contábil - (SPED Contábil)). Caso a escrituração seja descentralizada, o sistema trará todos os Estabelecimentos da Empresa.	OS2328I_2		RN30	No campo “Livro” será disponível para seleção o livro para definição do controle: G - Livro Diário Digital Geral (Completa sem escrituração auxiliar) R - Livro Diário Digital com Escrituração Resumida (com escrituração auxiliar) F - Livro Balancetes Diários e Balanços (filial). Nessa OS estamos tratando do atendimento ao livro tipo “R”, sendo assim, o usuário deverá selecioná-lo.	OS2328I_2		RN31	No campo “Periodicidade” o usuário irá selecionar qual a periodicidade que o livro será gerado, podendo ser Mensal, Diária e Anual. Por padrão o sistema apresentará a periodicidade Mensal.	OS2328I_2		RN32	[EXCLUÍDA – OS2848] No campo “Nº Ordem para geração” esse campo será de preenchimento manual, o usuário deverá imputar o valor aqui manualmente. Obs: Como primeiro Número de Ordem do livro eletrônico, o usuário terá de informar o número de seqüência ao livro original impresso e assim se segue a seqüência nos arquivos digitais. Lembrando que este número de Ordem deverá ser alterado pelo Usuário após cada geração válida. Esse campo fará o atendimento aos registros I030 e J900.	OS2328I_2		RN33	No quadro “Histórico de Livros Gerados (Principais)” deverá ser apresentado um histórico dos livros que foram gerados, com as seguintes informações: Livro, Periodicidade, Data Inicial, Data Final, Nº de Ordem.	OS2328I_2		RN34	A guia “Livros Auxiliares ao Diário” será habilitada para o usuário, quando este selecionar no campo “Livro” da guia “Livros Principais” o Tipo “R - Livro Diário com escrituração Resumida”.	OS2328I_2		RN35	Nesta guia “Livros Auxiliares ao Diário” após a habilitação conforme regra definida acima, existirá também o mesmo controle sobre os livros que auxiliam o Diário. Conforme RN33, RN34, RN35 e RN36.	OS2328I_2		RN36	No campo “Tipo do Livro” o usuário poderá selecionar qual o Livro Auxiliar ao Diário, Hoje existente duas opções, nessa OS trataremos da Opção: A - Livro Diário Auxiliar ao Diário com Escrituração Resumida.	OS2328I_2		RN37	No campo “Livro Auxiliar ao Diário” será exibido os Livros Auxiliares pertinentes ao livro selecionado no campo anterior.	OS2328I_2		RN38	[EXCLUÍDA – OS2848] O campo “Nº Ordem para geração” Seguirá o mesmo critério da regra RN29. Essa tela fará o atendimento ao registro I012.	OS2328I_2		RN39	O campo “Histórico de Livros Gerados (Auxiliares)” seguirá o mesmo critério da RN27 e 33.	OS2328I_2		RN40	Para essa tela somente será permitido apenas o cadastro de um Termo Abertura/Encerramento por livro. Essa Parametrização fará o atendimento aos Registros I030 e J900.	OS2328I_2		RN41	No campo “Tipo do Livro” estará disponível todos os livros gerados pelo SPED, nessa OS trataremos dos livros tipo “R” e tipo “A”, sendo assim nesse campo o usuário poderá selecionar a qual livro se destina à abertura e o encerramento. 	OS2328I_2		RN42	No quadro “Termo de Abertura” na Caixa “Natureza do livro” o usuário poderá descrever Manualmente a finalidade do livro. Contendo no máximo 27 linhas e suportando até 80 posições.	OS2328I_2		RN43	O campo “Arquivamento dos Atos Constitutivos” será de preenchimento opcional do usuário, com formato de data “dd/mm/aaaa”.	OS2328I_2		RN44	No quadro de “Termo de Encerramento” na caixa “Natureza do Livro” o usuário poderá descrever Manualmente a finalidade a que se destinou este livro. Contendo no máximo 27 linhas e suportando até 80 posições.	OS2328I_2		RN45	Os dados referentes ao plano de contas referencial não poderão ser alterados ou excluídos, pois são apenas para consultas.	OS2328I_2		RN46	O campo “Instituição Responsável pelo Plano de Contas Referencial” por definição padrão vem com a opção “Secretaria da Receita Federal”. No caso de instituições financeiras ou equiparadas a Instituições financeiras, o plano de contas que o usuário deverá selecionar para visualização é “20 - Banco Central do Brasil (Cosif)”.	OS2328I_2		RN47	No campo “Entidade Responsável” quando o usuário selecionar o item “20 – Banco Central do Brasil Cosif” será automaticamente apresentado o plano de contas Cosif com os códigos da contas, Descrições, e se a conta é analítica ou sintética.	OS2328I_2		A tela acima é uma tela de somente leitura, os campos não estarão habilitados para o usuário.	OS2328I_2		RN48	Nas contas referentes ao Banco Central existentes na TFIX64, que alimenta essa tela, existe uma coluna referente a classificação dos atributos das instituições financeiras para cada conta contábil, ou seja, para cada linha no plano de contas do BACEN existe esses atributos definidos. Esses atributos são representados por letras, exemplo: “BDIFACTSERLMN   UOHWK JP”. Essa tela será impactada com a parametrização feita na tela de “Dados iniciais” do quadro “Títulos”: Somente as contas que tiverem as letras selecionadas na tela de “Dados iniciais” é que serão apresentadas nessa tela de “Plano de Contas Referencial”. 
Exemplo: Na tela de “Dados Iniciais”, para o plano de contas do BACEN, foram selecionados as letras “P” e “H”. Logo, na tela de “Plano de Contas Referencial” somente serão apresentadas as contas cuja linha na TFIX64 contenham as letras em questão.
Conforme abaixo:
	OS2328I_2		RN48	Código		Descrição		
1.0.0.00.00-7 CIRCULANTE E REALIZAVEL A LONGO PRAZO (na TFIX64, na linha referente a essa conta na coluna dos atributos existem as letras “H” e “P”).                                                                                              1.1.0.00.00-6 DISPONIBILIDADES (na TFIX64, na linha referente a essa conta, coluna atributos, existem as letras “H” e “P”).                                                                                                                                                    1.1.1.00.00-9 CAIXA (na TFIX64, na linha referente a essa conta, coluna atributos existem as letras “H” e “P”).                 1.1.1.10.00-6 CAIXA (na TFIX64, na linha referente a essa conta, coluna atributos existe a letra “H”).   1.1.1.90.00-2 CAIXA (na TFIX64, na linha referente a essa conta, coluna atributos existe a letra “P”).     1.1.2.00.00-2 DEPOSITOS BANCARIOS (na TFIX64, na linha referente a essa conta na coluna dos atributos existem as letras “H” e “P”).
e assim por diante...	OS2328I_2		RN49	Observe essa tela esta sendo impactada pela parametrização efetuada conforme RN13, RN14 e RN15.	OS2328I_2		RN50	Nessa tela o usuário deve selecionar conta padrão versus contas da empresa, realizando o Depara para todas as contas, independentemente da movimentação no período.	OS2328I_3		RN51	Nessa tela serão demonstradas todas as contas sintéticas e analíticas, tanto para plano de contas referencial como plano de contas empresa, porém para definição do De/Para somente será permitida  a seleção de contas analíticas. Lembrando que, caso do Plano de Contas utilizado for o “COSIF”, nessa tela só irão aparecer às contas filtradas conforme parametrização efetuada na tela de “Dados Iniciais” conforme RN04, RN13, RN14 e RN15.
Para o Plano de contas referencial a tela já esta funcionando normalmente.	OS2328I_3		RN52	Essa tela deve permitir a realização de filtros para pesquisa das contas a serem relacionadas, tanto no quadro de “Plano de contas referencial, quando no quadro de Plano de contas da empresa”.	OS2328I_3		RN53	Consistir que não possa ser selecionada mais de uma vez a mesma conta e centro de custo da empresa para o plano de contas Referencial	OS2328I_3		RN54	Se selecionado mais de um centro de custo, a funcionalidade de geração deverá considerar o somatório dos valores dos centros selecionados e informar na conta do plano referencial	OS2328I_3		RN55	Para realização do Depara deverá ser considerada a regra do responsável pelo plano de contas referencial.	OS2328I_3		RN56	OBS: Na TFIX64 foi incluído 3 colunas referente a Data de início de Validade, Data fim de validade, e atributos. Essas informações não serão apresentadas nas telas que são alimentadas por essa TFIX.
Ou seja, para o Plano de contas (COSIF) as únicas informações que deverão ser visualizadas pelo usuário na tela do Mastersaf, são: o Código da Conta Contábil, a Descrição da Conta e a Definição da conta se ela é analítica ou sintética.	OS2328I_4		RN57	Referente à TFIX64 antes das contas 1.0.0.00.00-7 CIRCULANTE E REALIZAVEL A LONGO PRAZO será incluso o dígito "1". O Sistema deverá reconhecer esse dígito como “I” e trazer para a tela de plano de contas Referencial apenas para visualização.	OS2328I_4		RN58	Referente à TFIX64 antes das contas . e para a conta 4.0.0.00.00-8 CIRCULANTE EXIGIVEL A LONGO PRAZO  será incluso o dígito "4". O Sistema deverá reconhecer esse dígito como “II” e trazer para a tela de plano de contas Referencial apenas para visualização	OS2328I_4		RN59	Nessa tela existe um campo chamado “Cód. Hash do Arquivo correspondente ao Arquivo auxiliar”. Esse campo será retirado dessa tela.	OS2328IB		RN60	Na tela de “Controle da Obrigação” será incluso um botão chamado “Informar Hash Code”. Este campo deverá estar posicionado em baixo do campo “Nº Ordem Geração”.	OS2328IB		RN61	O botão “Informar Hash Code” será apresentado somente na primeira guia “Livros Principais”.	OS2328IB		RN62	O botão não estará habilitado ao usuário. O mesmo pode ser visível, mas não será habilitado até que o mesmo selecione no campo “Livro” o tipo “R - Livro Diário com escrituração resumida (Com escrituração auxiliar)”.	OS2328IB		RN63	Quando o usuário acionar o botão referente as regras RN60, 61 E 62. Será aberta uma nova janela para que o usuário informe o Cód. Hash do Arquivo correspondente ao Arquivo auxiliar.	OS2328IB		RN64	A tela apresentada conforme RN63 terá 4 colunas (Data de Geração, Código, Livro Auxiliar e Cód.Hash) e o Campo Período, a que se refere a data do arquivo magnético.	OS2328IB		RN65	O campo referente ao “Período” será uma Dropdown, onde estarão disponíveis para seleção as datas a que se referem os arquivos magnéticos gerados do livro “A”. Sendo apresentadas em ordem “decrescentes” apartir da ultima geração efetuada. Este trará como default sempre a ultima geração.	OS2328IB		RN66	O campo referente a coluna “Data de geração”  constará a data em que o usuário gerou o arquivo, assim como sua hora, minutos e segundos processados. Este não estará disponível alteração. Sendo apresentada sempre a ultima geração efetuada.	OS2328IB		RN67	Nesse campo o Usuário irá selecionar qual a geração que foi validada e informará para essa o “Cód hash” manualmente. Que este obteve após a transmissão do livro “A” para a receita federal.	OS2328IB		RN68	O campo “Cód” e  “Livro” também não estarão disponíveis para alteração. Somente o Campo “Cód. Hash” que será aberto para que o usuário informe o número do hash correspondente ao livro “A” gerado.	OS2328IB		RN69	Nessa tela, somente serão disponibilizadas as linhas para cadastro do Hash code conforme o cadastro dos livros auxiliares. Exemplo: se na tela (Parâmetros > Livros Auxiliares ao Diário) o usuário efetuou dois cadastros para o livro “A”, nessa tela do Hash code aparecerá duas linhas para que o mesmo informe o Hash code correspondente a cada livro.	OS2328IB		RN70	As informações trazidas para os campos “Cód” e “Livro” dessa tela, deverão ser iguais as apresentadas nos campos “Livro(Cód./Desc) da tela de cadastro dos Livros auxiliares (Parâmetros > Livros Auxiliares ao Diário).	OS2328IB		RN71	Obs: No Manual de layout do SPED o Campo Hash code não tem tamanho definido, sendo assim vamos deixar aberto para que o usuário possa informar código conforme o PVA gerar.	OS2328IB		RN72	Também estará disponível um botão “OK” para confirmação do cadastro das informações imputadas nessa tela.	OS2328IB		RN73	Caso o usuário tente confirmar o cadastro feito nessa tela sem preencher o campo referente ao COD_HASH, será apresentada a seguinte mensagem: Favor informar o Código Hash do Arquivo correspondente ao livro Auxiliar.	OS2328IB		RN74	Nessa tela será incluso uma coluna chamada “Código Hash Auxiliar” no quadro “Histórico dos Livros Gerados (Auxiliares)”.	OS2328IB		RN75	Quando o usuário acionar o botão “OK” na tela “informar Hash Code”, conforme definido na “RN72”, o sistema automaticamente colocará na frente dos seus respectivos livros, o hash code informado na “RN67”.	OS2328IB		RN76	Nos botões “  EMBED PBrush  ” apartir dessa OS, os mesmos passarão a funcionar corretamente, de forma que ao invés do registro ser adicionado abaixo um do outro, será aberto um novo cadastro e a numeração ficará sendo registrada. “ EMBED PBrush  ”.	OS2328IB		RN77	Nessa tela, será adicionada uma Dropdown “Selecionar Livro Aux”. Esta somente estará disponível quando o usuário selecionar no campo “Perfil” o livro tipo “A”.	OS2328IB		RN78	No campo “Selecionar Livro Aux” serão disponibilizados os livros auxiliares que foram cadastrados anteriormente (Parâmetros > Livros Auxiliares ao Diário). Default virá a opção “TODOS”.	OS2328IB		RN79	Caso o usuário opte por gerar “Todos”, o sistema deverá gerar “TXTs”  separados para cada livro Tipo “A”.	OS2328IB		RN80	[ALTERADA – OS2848] Se durante a geração do livro perfil “R” o sistema verificar que o campo 2 (NUM_ORD) do registro I012 não estiver preenchido, o mesmo deverá apresentar no Log a seguinte mensagem:

“Tipo I012 – Registro não será gerado. Favor informar o Número de ordem da geração. (Livro Auxiliar) de escrituração. Localização: SPED --> ECD Escrituração Contábil Digital --> Parâmetros --> Controle da Obrigação na opção [Livros Auxiliares]”	OS2328IB		RN81	Se durante a geração do livro perfil “R” o sistema verificar que o campo 3 (NAT_LIVR) do registro I012 não estiver preenchido, o mesmo deverá apresentar no Log a seguinte mensagem:

“Tipo I012 – Registro não será gerado. Favor informar o Descritivo do Livro para o SPED. (Livro Auxiliar) de escrituração. Localização: SPED --> ECD Escrituração Contábil Digital --> Parâmetros --> Livros Auxiliares ao Diário”	OS2328IB		RN81	Se durante a geração do livro perfil “R” o sistema verificar que o campo 4 (TIPO) do registro I012 não estiver preenchido, o mesmo deverá apresentar no Log a seguinte mensagem:

“Tipo I012 – Registro não será gerado. Favor informar Tipo de escrituração do Livro associado para o SPED. (Livro Auxiliar) de escrituração. Localização: SPED --> ECD Escrituração Contábil Digital --> Parâmetros --> Livros Auxiliares ao Diário”	OS2328IB		RN83	Se durante a geração do livro perfil “R” o sistema verificar que o campo 2 (COD_CTA_RES) do registro I015 não estiver preenchido, o mesmo deverá apresentar no Log a seguinte mensagem:

“Tipo I015 – Registro não será gerado. Favor informar o Código da conta analítica do Livro Diário com Escrituração Resumida (Livro “R”) que recebe os lançamentos globais. Localização: Módulo SPED -> ECD Escrituração Contábil Digital -> Parâmetros -> Livros Auxiliares ao Diário”
	OS2328IB		RN84	[ALTERADA – OS2848] Se durante a geração do livro perfil “A” o sistema verificar que o campo 2 (NUM_ORD) do registro I012 não estiver preenchido, o mesmo deverá apresentar no Log a seguinte mensagem:

Tipo I012 – Registro não será gerado. Favor informar o Número de ordem da geração. (Livro Auxiliar) de escrituração. 
Localização: SPED --> ECD Escrituração Contábil Digital --> Parâmetros --> Controle da Obrigação na opção [Livros Auxiliares]
	OS2328IB		RN85	Se durante a geração do livro perfil “A” o sistema verificar que o campo 3 (NAT_LIVR) do registro I012 não estiver preenchido, o mesmo deverá apresentar no Log a seguinte mensagem:

Tipo I012 – Registro não será gerado. Favor informar o Descritivo do Livro para o SPED. (Livro Auxiliar) de escrituração.
Localização: SPED --> ECD Escrituração Contábil Digital --> Parâmetros --> Livros Auxiliares ao Diário	OS2328IB		RN86	Se durante a geração do livro perfil “A” o sistema verificar que o campo 4 (TIPO) do registro I012 não estiver preenchido, o mesmo deverá apresentar no Log a seguinte mensagem:

Tipo I012 – Registro não será gerado. Favor informar Tipo de escrituração do Livro associado para o SPED. (Livro Auxiliar) de escrituração.
Localização: SPED --> ECD Escrituração Contábil Digital --> Parâmetros --> Livros Auxiliares ao Diário	OS2328IB		RN87	Se durante a geração do livro perfil “R” o sistema verificar que o campo 2 (COD_CTA_RES) do registro I015 não estiver preenchido, o mesmo deverá apresentar no Log a seguinte mensagem:

“Tipo I015 – Registro não será gerado. Favor informar o Código da conta analítica do Livro Diário com Escrituração Resumida (Livro “R”) que recebe os lançamentos globais. Localização: Módulo SPED --> ECD Escrituração Contábil Digital --> Parâmetros --> Livros Auxiliares ao Diário	OS2328IB		RN88	O relatório disponível no botão “ EMBED PBrush  ” da tela de “Livros Auxiliares ao diário” deverá ser atualizado com a retirada do campo “Cód. Hash do Arquivo correspondente ao Arquivo auxiliar”, na apresentação do relatório.	OS2328IB		RN89	O relatório disponível no botão “ EMBED PBrush  ” da tela de “Controle da Obrigação” deverá ser atualizado com a inclusão de uma coluna correspondente ao campo “Informar Hash Code”, na apresentação do relatório. Essa coluna receberá o nome de “Código Hash Auxiliar”, será a ultima coluna do relatório, localizada ao lado direito da coluna “nº de ordem”.
Essa coluna somente terá dados apresentados, caso o usuário tenha preenchido o Hash code na guia “Livros Principais” no botão “informar hash code” e o mesmo somente será apresentado na linha do ultimo livro gerado informado.
	OS2328IB		RN90	Será retirada do relatório a coluna “Livro”, pois já existe a identificação deste no relatório, dessa forma se abrirá espaço para a coluna da RN89. 	OS2328IB		RN91	Nessa tela, quando o usuário selecionar um centro de custo para relacionar a conta que foi adicionada nessa parametrização, esta será apresentada na forma vertical, ou seja, um centro de custo em baixo do outro separadamente, com um Check Box para cada Centro de Custo apresentado. Para melhor exemplificar essa situação (pode ser vista a tabela que foi criada para a tela do “De/Para: sped_contas_ref_ccusto, que agrupa os C.C de forma vertical assim como é solicitada essa alteração).	OS2328-N		RN92	No caminho SPED > ECD Menu: Manutenção > Códigos de Aglutinação (B. Patrimonial/D. Resultado), atualmente o sistema não permiti a gravação de relacionamento de uma mesma conta para códigos de aglutinações diferentes. Essa regra trata da retirada dessa exigência. O sistema permitirá que o usuário cadastre códigos de aglutinações diferentes para a mesma conta contábil, contanto que esta esteja relacionada a um centro de custo diferente. 	OS2328-N		RN93	Se o relacionamento dessa tela para a Guia/Aba “Demonstração de Resultado” for feito para códigos de aglutinações diferentes, contas iguais e centros de custo iguais, ou mesmo esteja somente com as contas relacionadas sem diferenciá-las com os centro de custos, o sistema deverá apresentar a mensagem: “Conta da empresa XXXX já cadastrada para outro código de aglutinação de mesmo nível”.

Exemplos: 

Mais de um código de aglutinação criado, com relacionamento para a mesma conta = (Erro–Acusar a mensagem acima)

Mais de um código de aglutinação criado, com relacionamento para a mesma conta, porém, com Centros de Custo iguais = (Erro – Acusar a mensagem acima).

Mais de um código de aglutinação criado, com relacionamento para a mesma conta, porém um possui centro de custo relacionado e o outro não = (Erro – Acusar a mensagem acima).

Mais de um código de aglutinação criado, com relacionamento para a mesma conta, com Centros de Custo diferente  = OK - Permitir o relacionamento.
	OS2328-N		RN94	A Alteração conforme regras acima, não deverão impactar no resultado da geração do meio magnético. Ou seja, se a funcionalidade utilizar os campos de alteração mencionados para gerar o TXT este deverá ser atualizado para atender reconhecer a nova estrutura.	OS2328-N		RN95	A alteração aqui descrita deverá atingir os livros “G” e “R”.	OS2328-N		RN96	Na tela de “Perfil” será incluso um campo chamado “Tipo do Livro”, este será apresentado em forma de “Dropdown”, e terá na sua lista, todos os tipos de livros exigidos pelo SPED Contábil. Este trará a informação em forma de “Dropdown” com a seguinte Descrição:
G – Livro Diário (Completa Sem escrituração Auxiliar).
R – Livro Diário com escrituração Resumida (Com Escrituração Auxiliar).
A – Livro Diário Auxiliar ao com Escrituração Resumida.
B – Livro Balancetes Diários e Balanços (Matriz)
Z – Razão Auxiliar (Livro Contábil Auxiliar conforme leiaute definido nos registros I500 a I555 ).

Observe:
A seleção da letra “G” implicará na apresentação dos Blocos e registros do Livro Diário Geral.
A seleção da letra “R” implicará na apresentação dos Blocos e registros do Livro Diário Resumido.
A seleção da letra “A” implicará na apresentação dos Blocos e registros do Livro Diário Auxiliar ao Diário Resumido.
A seleção da letra “B” implicará na apresentação dos Blocos e registros do Balancete Diário.
A seleção da letra “Z” implicará na apresentação dos Blocos e registros do Livro Razão Auxiliar.	OS2328 - O		RN97	Também serão inclusos nessa tela de “Perfil” os campos “Cód. E Descrição” que são relacionados ao Perfil criado.		RN98	Após a criação dos campos, o sistema deverá permitir a gravação de um ou mais perfis diferentes por empresa. 
EX: O Usuário pode gravar um perfil para o Livro tipo “G” com o registro 0150 flegado para a empresa 076. 
e pode criar outro perfil com um código diferente especifico para outra empresa, onde o registro 0150 do mesmo tipo de livro, não esteja flegado.
A regra é que o usuário poderá gravar diferentes perfis do mesmo livro para diferentes empresas.	OS2328 - O		RN99	Na tela de “Termo de Abertura/Encerramento” será incluso um campo chamado “Estabelecimento”, este será apresentado em forma de “Dropdown”, e terá na sua lista, todos os estabelecimentos da empresa que o usuário logou e que encontra-se em evidência no manager.	OS2328 - O		RN100	A tela de “Termo de Abertura/Encerramento” apresentará os estabelecimentos na forma de “Centralizador /Descentralizados”, este fará a verificação da parametrização feita no módulo (Parâmetros > Preliminares > Centralização da escrituração Contábil (SPED Contábil).	OS2328 - O		RN101	Após a criação do campo, o sistema deverá permitir a gravação de um ou termo de abertura /Encerramento diferentes por empresa.  EX: O Usuário poderá gravar o Termo de Abertura/Encerramento com os campos “Arquivamentos dos Atos Constitutivos” e “Arquivamento Ato de Converção de Sociedade Simples em Sociedade Empresária”, preenchidos com data de “01/01/2000”, após confirmar a gravação, este pode sair e se logar em outra empresa. Nesta ele poderá, gravar outro Termo de Abertura/Encerramento com os campos “Arquivamentos dos Atos Constitutivos” e “Arquivamento Ato de Converção de sociedade simples em sociedade empresária” preenchidos com data de “01/01/2010”.
A regra é que o usuário poderá gravar diferentes Termos de Abertura/Encerramento para diferentes empresas. Sem que um sobreponha ou interfira o outro.	OS2328 - O		RN102	Após a alteração, o usuário também poderá fazer um “Termo de Abertura/Encerramento” para o estabelecimento centralizador, onde este representa todos os estabelecimentos que são centralizados.
E também poderá gravar para estabelecimentos que não esteja como centralizado e seu status seja descentralizado um “Termo de Abertura/Encerramento” diferente.	OS2328 - O		RN103	Será incluso na tela de “Códigos de aglutinação”, o campo “Estabelecimento”.
Esse campo estará localizado, em cima das Guias/Aba “Balanço Patrimonial” e “Demonstração de Resultado”, de forma que a parametrização utilizada pelo usuário afete as duas telas ao mesmo tempo.	OS2328 - O		RN104	Será incluso na barra de ferramentas dessa tela, o botão “Abrir”, este ficará disponível para que o usuário quando entrar nessa tela possa trazer as informações que antes foram cadastradas, para cada qual o estabelecimento utilizado.	OS2328 - O		RN105	O Campo criado “Estabelecimento” será apresentado em forma de “Dropdown”, e terá na sua lista, todos os estabelecimentos da empresa que o usuário logou e que encontra-se em evidência no manager. Serão apresentados os estabelecimentos na forma de “Centralizador /Descentralizados”, este fará a verificação da parametrização feita no módulo (Parâmetros > Preliminares > Centralização da escrituração Contábil (SPED Contábil).	OS2328 - O		RN106	Apartir dessa alteração, o usuário poderá cadastrar uma ou mais “DRE” e “BPs” para empresa diferentes, ou para a mesma empresa, mas estabelecimentos diferentes.
Exemplo: 
1) Para empresa 076 eu utilizo Um “BP e uma DRE”, para a empresa 081, eu utilizo outro “BP e outra DRE diferentes do primeiro”. ou
2) Para a empresa  076, no estabelecimento 01 eu utilizo um “BP e DRE” e para o estabelecimento 001SP eu utilizo outro BP e DRE diferente.	OS2328 - O		RN107	Essa Regra não é só para teste e devida confirmação: “O sistema não permitira cadastrar duas “DRE e BP” para a mesma empresa/Estabelecimento”. Quando acionado o botão novo, dentro dessas telas, o sistema abre outra linha para cadastrar um novo código de aglutinação, o mesmo não abre e nem deve abrir uma nova tela para cadastro de nova “DRE/BP” esse procedimento está correto e deve ser testado para que continue assim.	OS2328 - O		RN108	Na tela de geração será incluso o campo chamados “Tipo do Livro”, este ficará localizado acima do campo “Perfil” e trará a informação em forma de “Dropdown” com a seguinte Descrição: G – Livro Diário (Completa Sem escrituração Auxiliar), 
R – Livro Diário com escrituração Resumida (Com Escrituração Auxiliar), A – Livro Diário Auxiliar ao com Escrituração Resumida, B – Livro Balancetes Diários e Balanços (Matriz), Z – Razão Auxiliar (Livro Contábil Auxiliar conforme leiaute definido nos registros I500 a I555 ).	OS2328 - O		RN109	O Campo Perfil será alterado de forma que traga as informações cadastradas na tela do “PERFIL”. O campo não apresentará mais o tipo do livro, agora será apresentado o descritivo do perfil criado. Obs: Quando selecionado um perfil que esta relacionado ao livro tipo “A”, o campo “Livro Auxiliar” deverá ser habilitado conforme previsto na RN77. (que esta disponível no documento Matriz completo do CVS).	OS2328 - O		RN110	Nesse processo de geração do arquivo magnético, quando o usuário selecionar o perfil cadastrado que foi relacionado com um determinado tipo de livro, este poderá fazer gerações diferentes do mesmo livro para perfis diferentes.	OS2328 - O		RN111	As alterações em todas as telas do SPED, não poderão alterar o que já esta funcionando no cliente. Ou seja, as parametrizações, que hoje já existem paras as telas de Perfil, Termo de Abertura/Encerramento e BP/DRE que são alvo dessa alteração, deverão ser mantidas.
A regra é que, não seja alterado e nem apagado o que já existe na base do cliente. 
Neste momento, quando o cliente aplicar o pacote que trará as alterações dessa OS, deverão ser considerados os mesmos dados existentes na base dele hoje. 
O critério será que as parametrizações efetuadas se manterão iguais para todos, assim como é hoje, (por que o sistema não permite que seja feito diferente). Caso o usuário tenha alguma empresa ou estabelecimento que utilize demonstrações diferenciadas, este deverá logar na empresa e estabelecimento que deseja alterar, e fazer as parametrizações necessárias. (pois apartir dessa alteração o sistema permitirá a agravação desses dados diferentes e não impactará no que esta feito para as outras empresas).
Exemplos:
A Actua possui três empresas.
Hoje o sistema mantém o mesmo perfil, o mesmo termo de abert/Encer, e mesmo Balanço Patrimonial e DRE para as três empresas diferentes.
Classifiquemos essas três empresas como “X”, “Y” e “Z”.
Imagine que para empresa “X, Y e Z” eu tenha o mesmo perfil gravado e não consigo alterar isso.
Após aplicação do pacote o usuário poderá logar na empresa “Z” e gravar um perfil diferente das empresas “X e Y” e o sistema permitira a gravação sem alterar o perfil das outras duas empresas.
Ou seja, ele já tinha um perfil gravado para as três empresas e isso não foi alterado. Mas ele consegue agora mudar o perfil de uma das empresas e gravá-lo. De forma que eu fique com dois perfis iguais e um diferente.
Da mesma forma ocorrerá com as parametrizações do “BP e DRE”. Hoje, os mesmos códigos de aglutinações criados para a empresa “X” estão replicados automaticamente para as empresas “Y e Z”.  (Como ocorre com o perfil, hoje o mastersaf não deixa que o usuário na empresa “Z” ,exclua um código de aglutinação sem que este também seja excluído nas empresas “X e Y”. 
Após a aplicação do pacote, os dados continuarão os mesmos, mas o usuário poderá entrar na empresa “Z” e excluir ou criar outro código de aglutinação, sem que este seja também alterado nas empresas “X e Y”.	OS2328 - O		RN112	Na geração do registro "I051", quando o código da instituição responsável pela manutenção do plano de contas referencial for "20" , que é o código do BACEN (Banco Central do Brasil (Cosif)), o sistema deverá recuperar o número da conta sem os caracteres, ou seja, a conta do BACEN virá somente os números.
 
Ex:
 
A conta 1.1.1.90.00-2 está cadastrada na TFIX64 pelo plano de contas do BACEN (código 20). Note que na conta os números estão separados por caracteres. Na geração do registro, o sistema deverá verificar se o código da instituição responsável for "20" e, gerar o registro da seguinte forma:
 
|I051|20|Centro de Custo|11190002|
 
Resultado: O registro foi gerado com a conta sem os caracteres.
 
Obs.: Na TFIX64 estão cadastradas as contas da Secretaria da Receita Federal e do Banco Central do Brasil - Cosif (BACEN). A geração do registro com a conta sem os caracteres é somente para as contas do BACEN.
	OS2328 - O		RN113	Na tela “Plano Referencial x Plano de Contas Empresa” conhecida como “De/Para”, serão inseridos dois “Red Button”, ao lado direito da tela, dentro do espaço separado para o campo “Informar conta para pesquisa:”.
Os campos criados serão chamados: “Conta e Descrição”.	OS2328-G1		RN114	Com esta alteração o botão “pesquisar” será arrastado para o lado direito dos novos campos.  A funcionalidade de pesquisa para as contas será alterada, de forma que, esta permita ao usuário, selecionar a opção “Conta” este irá  inserir no campo “ informar conta para pesquisa” o código da conta ou parte dele e quando o usuário acionar o botão 
“pesquisar” o sistema apresentará as contas organizadas por código de conta. Exemplo: Pesquisa utilizando o cód: “3.1”

Resultado:
3.1
3.1.1
3.1.1.1
Essa funcionalidade de pesquisa, será feita tanto para o plano referencial, quanto para o da empresa.

Se o usuário optar pelo “red button” “Descrição”, quando acionado o botão “pesquisar” será apresentado as contas que contenham a descrição informada. Exemplo: Pesquisa utilizando a descrição “salários”

Resultado:
2.1.1.1.1 Salários a pagar
4.1.1.1.1 Despesa com salários
OBS: Essa Regra aplica-se tanto para o plano de contas referencial da Receita Federal quanto para o do COSIF.	OS2328-G1		RN115	A tela de seleção de centro de custo será alterada de forma que quando o usuário desejar selecionar “C.C” para uma determinada conta que foi devidamente selecionada e adicionada seguindo a regra que só se pode fazer isso para contas analíticas, o mesmo poderá selecionar, mais de um centro de custo por vez. Ou seja, a tela em si, não será alterada, somente os objetos que regem essa parametrização, de forma que o sistema permitirá que o usuário selecione mais de uma linha antes de clicar no botão “OK”, e recuperando todas as linhas selecionadas para a tela anterior (plano referencial x plano de contas empresa). 	OS2328-G1		RN116	Será criado um menu chamado “Relatórios” ele estará localizado entre os menus “Geração” e “Janela”.
Quando selecionado esse menu, será apresentado um submenu, chamado “Relatório Sintético/Analítico”.	OS2328-G1		RN117	Quando o usuário acionar o submenu “Relatório Sintético/Analítico” será apresentada uma tela chamada “Geração do Relatório Sintético/Analítico”, a tela será composta da seguinte forma:

Campo “Livro” em forma de Dropdown, sendo apresentado os Livros Tipo “G” e Tipo “R” que serão considerados para esse relatório.

Campo “Periodicidade” em forma de Dropdown, apresentando os tipos “Anual”, “Mensal” e “Diária”.

Campo “Período” (sendo este inicial e final).

A tela terá uma divisão de opções, sendo eles de “Demonstrativos Sintéticos” e “Demonstrativos Analíticos”, essa divisão poderá ser melhor visualizada no item 2.2 do documento de requisitos na demonstração da tela. 
Dentro da Opção “Demonstrativos Sintéticos” terá um campo em forma de “check box” chamado “Plano referencial x  Plano de Contas Empresa”.
Dentro da Opção “Demonstrativos Analíticos” terá um campo em forma de “check box” chamado “Plano referencial x  Plano de Contas Empresa”.

Também terá uma caixa, onde estarão organizados em forma de lista, os estabelecimentos, seguindo o conceito centralizador/descentralizado.  Na frente de cada estabelecimento terá um campo “check box”, para que o usuário diga de qual estabelecimento ele quer o demonstrativo.
Esta caixa com os estabelecimentos deverá seguir a padrão mastersaf com o botão (selecionar todos). 

Abaixo da caixa estabelecimentos terá a seguinte observação:
*Objetivo deste relatório é obter visão analítica/sintética na ótica do plano de contas referencial x Contas  Empresa(De/Para), independentemente da geração do arquivo da ECD. A informação apresentada no relatório  poderá ser convergente com a geração conforme a opção “omitir centro de custo”.
Obs: Para obter resultados por centro de custo parametrizado no DEPARA neste relatório, se faz necessário  carregar valores de saldo por centro de custo (SAFX80).	OS2328-G1		RN118	Os Estabelecimentos serão apresentados conforme o cadastro feito na tela de “Controle da Obrigação”. Se o usuário selecionar um livro tipo “G” e a periodicidade “Mensal” só serão apresentados os estabelecimentos que possuírem o cadastro de livros tipo G com esse tipo de periodicidade.	OS2328-G1		RN119	O usuário poderá selecionar as opções sintéticos e analíticos ao mesmo tempo. Se isso acontecer, este terá opção de gerar o relatório sintético e analítico de uma só vez, de forma que as informações serão apresentadas separadas no relatório, a intenção é que somente sejam geradas juntas, mas a apresentação seja em páginas separadas.
OBS: O Usuário poderá gerar os relatórios conforme escolha definida no parâmetros de dados iniciais. Se o usuário utiliza o plano de contas referencial da Receita Federal este é que será apresentado caso contrário o plano referencial apresentado será o do COSIF.	OS2328-G1		RN120	Para apresentação dos valores de forma sintética, o sistema deverá verificar o relacionamento feito entre as contas referenciais e da empresa, inclusive considerar os valores se houver o relacionamento com Centro de Custo.
Os valores serão trazidos para o relatório na frente da conta referencial que foi relacionada no De/Para.

Exemplo:
Imagine que no De/Para, foi relacionado a conta “BANCO” do referencial com as contas “Itau, Bradesco e Banco do Brasil” do plano de contas empresa. Sendo que o valor de cada conta empresa era de R$ 50.000,00.

O relacionamento feito foi esse:

Conta Referencial                                                               Conta empresa
1.01.01.02.00 (Banco)                                                         yy.yyy.yy  1 Banco do Brasil                                                    .                                                                                            yy.yyy.yy 2  Bradesco                                                                                            .                                                                                            yy.yyy.yy 3  Itau                                  

Porém no relatório sintético será apresentado assim:


Conta Referencial                      Valor                 Indicador
             1.01.01.02.00 (Banco)               R$ 150.000,00        D

O valor de 150.000,00 equivale a soma dos saldos das  contas Itau, Bradesco e Brasil no valor de R$ 50.000,00 cada.
Essa será a apresentação do demonstrativo sintético sem relacionamento de C.C.
O demonstrativo sintético, terá 4 colunas,uma que trará os códigos das contas do plano referencial, outra que trará a descrição das contas referenciais, outra que trará o valor dos saldos somados referente ao relacionamento feito no De/para e a ultima trará a indicação do valor apresentado, se este é credor ou devedor de forma (D) ou (C), conforme regra contábil.

Regra contábil: Na sumarização dos saldos, inclusive para as contas sintéticas, seguir os mesmos critérios já vigentes na geração dos saldos do arquivo magnético do Sped contábil, ou seja, verificar o Indicador do Saldo das Contas (Devedor/Credor) e somar valores quando iguais, ou subtrair valores quando diferente. Indicador final é o correspondente a parcela de maior valor, no caso de indicadores diferentes entre as parcelas.
OBS: Essa Regra aplica-se tanto para o plano de contas referencial da Receita Federal quanto para o do COSIF.	OS2328-G1		RN121	Quando houver um relacionamento com Centro de Custo feito no De/Para as informações serão apresentadas da seguinte maneira.

Os valores serão trazidos para o relatório da mesma forma que na RN120.

Exemplo:
Imagine que no De/Para, foi relacionado a conta “SALÁRIOS” do referencial com a conta “Salários e Ordenados” do plano de contas empresa, porém, este tem Centro de custo relacionado, sendo X Vendas, Y Administração e Z Produção. Sendo que o valor de cada “C.C” era de R$ 100.000,00.

O relacionamento feito foi esse:

Conta Referencial                                                               Conta empresa
4.01.01.02.00 (Salários)                                                      X.XX.XXXX Salários e Ordenados
                                                                                                                 X Vendas (C.C)
                                                                                                                 Y Administração (C.C)
                                                                                                                 Z Produção (C.C)

Porém no relatório será apresentado assim:


Conta Referencial                      Valor                 Indicador
             4.01.01.02.00 (Salários)             R$ 300.000,00       D

O valor de 300.000,00 equivale a soma dos centro de custos (SAFX80) vendas, Adminstração e Produção no valor de R$ 100.000,00 cada.

Essa será a apresentação do demonstrativo sintético com relacionamento de C.C.
A apresentação dos dados é a mesma, somente a recuperação dos valores é que serão diferentes quando for identificado o relacionamento de “C.C”.
OBS: Essa Regra aplica-se tanto para o plano de contas referencial da Receita Federal quanto para o do COSIF.	OS2328-G1		RN122	Para geração dos relatórios deverá ser levado em conta que: Se a conta não tiver Centro de custo relacionado o valor cheio da conta é pego da SAFX02 (saldos Mensais), se tiver relacionamento de C.C o valor pego é o da SAFX80 (Saldo por C.C).
OBS: Essa Regra aplica-se tanto para o plano de contas referencial da Receita Federal quanto para o do COSIF.	OS2328-G1		RN123	Para as contas sintéticas imediatamente superior (código da conta referencial), deverão ser sumarizadas os valores.

Exemplo

1          Ativo                     “Sintética”      (vr ativo = soma de estoque + disponibilidade seguindo o nível das contas)
1.1       Disponibilidade    “Sintética”       (vr disponibilidade = soma de caixa + Bancos seguindo o mesmo nível da conta)
1.1.1.1 Caixa                    “Analítica” 
1.1.1.2 Bancos                 “Analítica”       
1.2       Estoques
OBS: Essa Regra aplica-se tanto para o plano de contas referencial da Receita Federal quanto para o do COSIF.	OS2328-G1		RN124	Quando se tratar de contas normais será recuperado o saldo da conta na SAFX02, porém, quando se tratar de contas de resultado que são encerradas normalmente no final do período, estas precisarão ter seus valores recuperados diretamente da SAFX01 (Lançamentos Contábeis). A recuperação dos valores para esse tipo de conta se dará da seguinte forma:

Durante o De/Para foi relacionado uma conta de “Receita” da empresa com uma conta de “Receita” do referencial (RF ou COSIF).
Para sabermos se a conta da empresa é uma conta de resultado, será necessário verificar na SAFX2002 (DW>Manutenção>Códigos>Plano de contas) o campo 07 “Indicador de natureza”. Estando esse como “Receita, Custo ou Despesa” entende-se que essa conta é de “resultado e que será necessário fazer o encerramento da mesma.
Para recuperar seu valor para o relatório Sintético/Analítico do De/Para, após visto que a conta é de resultado ir na SAX01 (DW>Manutenção>Contabilidade>Diário Geral> Lançamentos Contábeis>por estabelecimento) e verificar quais são os lançamentos existentes no período solicitado para geração do relatório, para essa conta que possuiem no campo 17 “Tipo de lançamento (Atend.Portaria 63):” o preenchimento “E” de encerramento e enviar para o relatório sintético/analítico.

Obs: O Livro Diário Auxiliar não reflete sobre o plano de contas referencial, não sendo necessário dados para emissão deste relatório, essa Regra aplica-se tanto para o plano de contas referencial da Receita Federal quanto para o do COSIF.	OS2328-G1		RN125	Se houver mais de uma lançamento de encerramento dentro do mesmo período o sistema deve somar os valores e jogar no relatório o valor total.
Obs.: essa verificação e soma dos dados o sistema já faz para a geração do meio magnético, sendo assinm, isso também deve ser considerado para o relatório.	OS2328-G1		RN126	Deverá ser informado ao usuário que se ele não tiver lançamento de contas de resultado naquele período com o indicador “E” – encerramento, não será recuperado valor para o relatório.
	OS2328-G1		RN127	Para apresentação dos valores de forma analítica, o sistema deverá verificar o relacionamento feito entre as contas referenciais e da empresa, inclusive considerar os valores se houver o relacionamento com Centro de Custo.
Os valores serão trazidos para o relatório na frente da conta referencial que foi relacionada no De/Para.

Exemplo:
Imagine que no De/Para, foi relacionado a conta “BANCO” do referencial com as contas “Itau, Bradesco e Banco do Brasil” do plano de contas empresa. Sendo que o valor de cada conta empresa era de R$ 100.000,00 para o banco do Brasil, R$ 45.000,00 para o Bradesco e R$ 5.000,00 para o Itau.

O relacionamento feito foi esse:

Conta Referencial                                                               Conta empresa
1.01.01.02.00 (Banco)                                                         yy.yyy.yy  1 Banco do Brasil                                                    .                                                                                            yy.yyy.yy 2  Bradesco                                                                                            .                                                                                            yy.yyy.yy 3  Itau                                  

No relatório sintético será apresentado assim:

   Conta Referencial               Valor                        Conta Empresa                                 C.C           Valor                Indicador
    1.01.01.02.00 (Banco)         R$ 150.000,00        yy.yyy.yy  1 Banco do Brasil               -          100.000,00                D
                                                                                yy.yyy.yy 2  Bradesco                         -             45.000,00               D
                                                                                yy.yyy.yy 3  Itau                                  -               5.000,00               D

O valor de 150.000,00 equivale a soma dos saldos das  contas Itau, Bradesco e Brasil no valor de 100 + 45 + 5 = 150.
Essa será a apresentação do demonstrativo analítico sem relacionamento de C.C.

O demonstrativo Analítico, terá 8 colunas, a primeira trará os códigos das contas do plano referencial, a segunda trará a descrição das contas referenciais, a terceira trará o valor dos saldos somados referente ao relacionamento feito no De/para, a quarta trará os códigos das contas contábeis do plano de contas da empresa, a quinta trará a descrição das contas da empresa, a sexta trará os códigos de centro de custos que foram ou não relacionados, a sétima trará o valor dos relacionamentos sendo pego da SAFX80 quando houver o relacionamento de saldo por C.C e da SAFX02 quando houver somente o relacionamento direto da conta, e a ultima trará a indicação do valor apresentado, se este é credor ou devedor de forma (D) ou (C), conforme regra contábil.

Regra contábil: Na sumarização dos saldos, inclusive para as contas sintéticas, seguir os mesmos critérios já vigentes na geração dos saldos do arquivo magnético do Sped contábil, ou seja, verificar o Indicador do Saldo das Contas (Devedor/Credor) e somar valores quando iguais, ou subtrair valores quando diferente. Indicador final é o correspondente a parcela de maior valor, no caso de indicadores diferentes entre as parcelas.
OBS: Essa Regra aplica-se tanto para o plano de contas referencial da Receita Federal quanto para o do COSIF.	OS2328-G1		RN128	Quando houver um relacionamento com Centro de Custo feito no De/Para as informações serão apresentadas da seguinte maneira.

Os valores serão trazidos para o relatório da mesma forma que na RN127.

Exemplo:
Imagine que no De/Para, foi relacionado a conta “SALÁRIOS” do referencial com a conta “Salários e Ordenados” do plano de contas empresa, porém, este tem Centro de custo relacionado, sendo X Vendas, Y Administração e Z Produção. Sendo que o valor de cada “C.C” era de R$ 100.000,00 para cada C.C.

O relacionamento feito foi esse:

Conta Referencial                                                               Conta empresa
3.01.01.07.01 (Salários)                                                      X.XX.XXXX Salários e Ordenados
                                                                                                                 X Vendas (C.C)
                                                                                                                 Y Administração (C.C)
                                                                                                                 Z Produção (C.C)

No relatório será apresentado assim:

   Conta Referencial               Valor                        Conta Empresa                                 C.C           Valor                Indicador
   4.01.01.02.00 (Salários)     R$ 300.000,00          X.XX.XXXX Salários e Ordenados     X          100.000,00              D                                                                                                                                                                                                                                    .                                                                                                                                           Y          100.000,00              D
                                                                                                                                            Z          100.000,00              D

O valor de 300.000,00 equivale a soma dos centro de custos (SAFX80) vendas, Adminstração e Produção no valor de R$ 100.000,00 cada.

Essa será a apresentação do demonstrativo analítico com relacionamento de C.C.
A apresentação dos dados é a mesma, somente a recuperação dos valores é que serão diferentes quando for identificado o relacionamento de “C.C”. Ou seja, se a conta não tiver Centro de custo relacionado o valor cheio da conta é pego da SAFX02 (saldos Mensais), se tiver relacionamento o valor pego é o da SAFX80 (Saldo por C.C).

A diferença do analítico para o sintético, é que no sintético é demonstrada as contas do plano referencial já com os valores totalizados.
No analítico é demonstrada as contas e C.C da empresa que comporam esse valor totalizado demonstrado no sintético.
OBS: Essa Regra aplica-se tanto para o plano de contas referencial da Receita Federal quanto para o do COSIF.	OS2328-G1		RN129	Observação: A informação apresentada neste relatório poderá divergir do resultado de geração da ECD. Isso poderá ocorrer quando selecionada opção “omitir centro de custo” no momento da geração, em que não apresentará o centro de custo nos lançamentos contábeis e valores de saldos por centro de custo (SAFX80) no arquivo digital da ECD. Neste relatório tem por objetivo antecipar a visão das regras parametrizadas no depara desconsiderando o parâmetro de omissão do centro de custo. A omissão é possível na geração da ECD por se tratar de um registro facultativo pela legislação. Essa regra aplica-se tanto para o relatório sintético como para o analítico.

OBS: Essa Regra aplica-se para o plano de contas referencial da Receita Federal e para o do COSIF.	OS2328-G1		RN130	O relatório também deverá buscar normalmente como as regras definidas acima, as informações de relacionamento feito no De/Para, quando esse for o Plano de Contas do COSIF. Ou seja, no relatório sintético e analítico as contas do plano referencial que irão aparecer nos relatórios serão as do Banco Central.	OS2328-G1		RN131	As contas dos planos de contas referenciais (Receita/Banco Central) serão definidas em sintéticas e analíticas conforme seus níveis. Segue posicionamento do Banco Central em relação ao Plano de contas COSIF: 

De: SECRE/CAP [cap.secre@bcb.gov.br]Enviado em: terça-feira, 23 de setembro de 2008 16:13Para: 'elizangela.pereira@mastersaf.com.br'Assunto: Banco Central Responde - Demanda 2008222886

Prezada Sra. Elizangela:
 
O setor responsável pelo assunto respondeu que a própria estrutura do plano de contas define as contas analíticas e as sintéticas. As contas sintéticas são as que agrupam as analíticas, em vários níveis (de 1 a 5).Assim uma conta de grupo 1, é sintética das contas do nível 2, que por sua vez agrupam as de nível 3, e assim por diante. Dessa forma, uma conta de nível 4, é sintética em relação ao nível 5, e analítica em relação ao nível 3.
 
Destacamos que o Cosif está disponível em nosso site pelo endereço  HYPERLINK "http://www5.bcb.gov.br/?PUBMANUAIS" http://www5.bcb.gov.br/?PUBMANUAIS .
Atenciosamente, 
Banco Central do Brasil

OBS: o que o “BCB” entende como nível das contas é:

A conta do COSIF:

1.0.0.00.00-7 é nível “1” (Circulante e realizável a longo prazo)
1.1.0.00.00-6 é nível “2” (Disponibilidades)
1.1.1.00.00-9 é nível “3” (Caixa)
1.1.1.10.00-6 é nível “4” (Caixa)
1.1.1.90.00-2 é nível “4” (Caixa)

Para se definir qual é a mãe de quem deverá ser verificado o código da conta, juntamente com o nível.
As contas 1.1.1.90.....e a 1.1.1.10.... são filhas da 1.1.1..... que é filha da 1.1..... que é filha da 1.....
A mesma coisa se aplica as contas com código com início “2”. A conta 2.... é mãe da 2.2.... que é mãe da 2.2.2	OS2328-G1		RN132	 O relatório deverá trazer as informações organizando por ordem dos códigos das contas e nível exemplo:
O nível não irá aparecer na apresentação do relatório, mas ele juntamente com o código é que fará a ordem do mesmo:

Nível Conta             Descrição Valor....
1          1                   Ativo
2          1.01              Circulante
3          1.01.01         Disponibilidades
4          1.01.01.01    Caixa
1          2                   Passivo
2          2.01              Circulante
3          2.01.01         Realizável a longo prazo
4          2.01.01         Fornecedores
      
A ordem do relatório deverá seguir a mesma esquemática do plano de contas por isso precisará considerar os códigos das contas e os níveis.
	OS2328-G1		RN133	A tela de seleção de centro de custo será alterada de forma que quando o usuário desejar selecionar “C.C” para uma determinada conta que foi devidamente selecionada e adicionada seguindo a regra que só se pode fazer isso para contas analíticas, o mesmo poderá selecionar, mais de um centro de custo por vez. Ou seja, a tela em si, não será alterada, somente os objetos que regem essa parametrização, de forma que o sistema permitirá que o usuário selecione mais de uma linha antes de clicar no botão “OK”, e recuperando todas as linhas selecionadas para a tela anterior (Seleção de Contas da Empresa para apuração).
OBS: Essa Regra aplica-se tanto para o plano de contas referencial da Receita Federal quanto para o do COSIF.	OS2328-G1		RN134	As regras RN113 e RN114 também se aplicam a tela de Balanço patrimonial/DRE nas opções Selecionar conta para apuração. 
OBS: Essa Regra aplica-se tanto para o plano de contas referencial da Receita Federal quanto para o do COSIF.	OS2328-G1		RN135	Da mesma forma que ocorre para o Livro “A” as parametrizações feitas para o Livro “Z” nessa tela deverão ser reconhecidas, de forma que o sistema gere com sucesso os registros I012, I015.	OS2328-L		RN136	Na tela de Controle de obrigação quando gerado o Livro “Z” Razão auxiliar, será apresentado no Historio de livros gerados (Auxiliares) dessa tela, no campo Livro, o nome criado no perfil do livro. Atualmente aparece como o livro “R” que foi gerado, porém nesse histórico deve ser apresentado o nome de perfil do livro auxiliar e não do principal. 
E o numero do Hash Code que foi informado na tela dos livros principais no campo “informar hash code”, após a geração do mesmo deve alimentar o campo “Código Hash Auxiliar” da tela dos Livros Auxiliares ao Diário.	OS2328-L		RN137	A tela “Impressão do livro auxiliar” já existe dentro do mastersaf, porém, será alterada de forma que contenha os seguintes campos. 
Estabelecimento: Nesse campo deverá ser apresentado os estabelecimentos que foram definidos como Descentralizados e aquele que foi definido como centralizador no módulo Parâmetros > Menu Preliminares > centralização da escrituração contábil.

Tamanho da fonte: (Esse campo é numérico com tamanho 2. E será de preenchimento manual do usuário).
Dec.: (Esse campo é numérico com tamanho 2. E será de preenchimento manual do usuário) Obs: embora o tamanho desse campo seja 2, que deverá ser levado em cotna na geração do meio magnético, esse deverá estar travado até 6 casas decimais, caso haja alguma demanda para tratamento de mais casas decimais, estaremos fazendo tratamento posteriormente.

Abaixo dos campos acima estará localizado em forma de colunas os demais campos:

Campo: (Esse campo será alfanumérico, de tamanho 50. E será de preenchimento manual do usuário).
Ordem do Campo no livro Razão: (Esse campo é numérico, deve ser mantido o tamanho já permitido pelo sistema atualmente (18). E será de preenchimento manual do usuário)
Tipo: (Esse campo é alfanumérico com tamanho 1. E será de preenchimento manual do usuário)
Tam: (Esse campo é numérico com tamanho 3. E será de preenchimento manual do usuário).
Largura: (Esse campo é numérico com tamanho 3. E será de preenchimento manual do usuário).

Nessa tela ainda terá um grupo chamado “Totalizadores” que conterá os seguintes campos:

Agrupar por: (Esse campo será criado em forma de Dropdown e servirá para que o usuário defina qual será a quebra do relatório que será utilizada para soma posteriormente).
Totalizar Por: (Esse campo será de preenchimento manual do usuário e servirá para que o usuário defina qual será o campo que deverá ser somado). Neste só estarão disponíveis os campos que foram cadastrados com tipo “N” – numéricos.
Totalizador Geral: (Esse campo será criado em forma de Check Box, e servirá para geração de um totalizador geral no final do relatório.)

A tela conterá uma observação que estará localizada antes do campo “Importar arquivo Externo” e depois dos campos “Campo, Ordem...” com os seguintes dizeres:
**Obs: Para definição de fonte, tamanho e largura considerar espaço de um caractere entre as colunas, para campos numéricos, considerar também os separadores de milhar e a vírgula. Considerar que o livro será impresso/visualizado em papel A-4, com a orientação paisagem, margens de 1,5 cm e com fonte Courier.	OS2328-L		RN138	O Campo  “Tamanho da fonte” servirá para geração do registro “I500”.
Os campos “Dec. ,Campo, Ordem do Campo no livro Razão, Tipo, Tam, Largura” servirão para geração do registro “I510”.	OS2328-L		RN139	Para a geração do registro “I550”. O arquivo importado deverá estar de acordo com o layout definido pelo usuário nos campos “Tamanho da fonte, Dec., Campo, Ordem do Campo no livro Razão, Tipo, Tam, Largura”. 
Para geração do registro “I555” os campos “Agrupar por”, “Totalizar por” e “Totalizador Geral” do grupo “Totalizadores”, da tela de Impressão do Livro Razão Auxiliar, deverão estar parametrizados.
Com os dados informados nesses campos o arquivo será lido e aceito ou lido e rejeitado.	OS2328-L		RN140	Essa tela será composta dos botões padrões do mastersaf: “Novo, Excluir, Confirmar, Imprimir, Relatório, Fechar”.
Todas as vezes que for acionado o botão “Novo”, será apresentada uma linha com os campos (Campo, Ordem do Campo no livro Razão, Tipo, Tam, Largura). Essa linha estará aberta, para que o usuário possa definir um novo campo com suas determinadas características no relatório e existirá uma barra de rolagem caso seja criado vários campos. 
Da mesma forma todas as vezes que for acionado o botão “Excluir” será excluído uma linha por vez, referente os campos (Campo, Ordem do Campo no livro Razão, Tipo, Tam, Largura) que o cursor estiver estacionado.	OS2328-L		RN141	O botão “relatório” disponível na tela de “Impressão do Livro Razão Auxiliar”, quando acionado será apresentado conforme demonstrado no item 2.1.1.4 do documento de requisitos. Apresentando todas as colunas da tela e os dados cadastrados. Inclusive o campo e nome do arquivo a ser importado para o mastersaf.	OS2328-L		RN142	Será inserido no Menu Manutenção o submenu chamado “Livro Razão Auxiliar”: Esse Menu será composto dos seguintes campos:


Estabelecimento: Nesse campo deverá ser apresentado os estabelecimentos que foram definidos como Descentralizados e aquele que foi definido como centralizador no módulo Parâmetros > Menu Preliminares > centralização da escrituração contábil.


Período: Esse campo será de preenchimento manual do usuário e a informação será inserida em forma de mês e/ou ano.
Importar arquivo Externo: (Esse campo será semelhante ao campo existente na tela de “Dados Iniciais” onde o usuário importa um arquivo em formato RTF no mastersaf. Este será idêntico, porém, o mastersaf deverá estar preparado para receber e ler o arquivo informado aqui, em formato “texto separado por tabulações”.


Quando o usuário acionar esse menu e informar os campos acima, será apresentado uma tela com a visualização do relatório que foi importado em formato “texto separado por tabulações”. 


A visualização do relatório não será completa, serão apresentadas somente as 5 primeiras e as 5 últimas páginas do relatório, caso este tenha muitas páginas, se o relatório tiver menos que 10 páginas ele será demonstrado completo. A visualização deste relatório serve apenas para que o usuário possa ter uma noção de como será a apresentação do mesmo no PVA. A fonte que será apresentada neste não terá relação com a fonte pré-definida pelo usuário, pois aquela serve somente para geração do registro I500.	OS2328-L		RN143	O relatório só será possível de visualização se o arquivo informado no menu Menutanção > Livro Razão Auxiliar, estiver exatamente no layout definido pelo usuário no caminho “Parâmetros > Impressão do Livro Razão Auxiliar”.
Exemplo:

Data             Conta            Descrição            Valor

010108        2328.0001     Salários               50,00

A visualização acima só seria possível se no menu “Parâmetros > Impressão do Livro Razão Auxiliar” o layout estivesse assim:
Tamanho da fonte: 10
Dec.: 2
Campo          Ordem...   Tipo Tam  Largura

Data                   1            N      6        10
Conta                 2            C      9        20
Descrição          3            C      20       30
Valor                  4            N      20       30	OS2328-L		RN144	Caso o layout esteja diferente do arquivo informado no campo “Importar Arquivo Externo” do menu Manutenção > Livro Razão Auxiliar, deverá ser apresentada na tela a seguinte mensagem:
“Visualização indisponível” Layout difere da estrutura do arquivo informado no campo “Importar Arquivo Externo” do menu “Manutenção > Livro Razão Auxiliar. Favor verificar os campos cadastrados no menu Parâmetros > Impressão do Livro Razão Auxiliar para que a visualização do arquivo possa ser gerada corretamente”. A visualização de como ficará a tela no caso de uma rejeição do arquivo, esta disponível no item 2.1.1.4 do documento de requisitos.	OS2328-L		RN145	Na tela de Perfil do SPED quando selecionado o tipo do livro “Z” deverão ser apresentados todos os registros do SPED conforme layout definido no item 2.2 do documento de requisitos.
Os registros que na coluna “Z” estiverem com indicador “O” deverão estar marcados e desabilitados para alteração, os que estiverem com “F” deverão estar habilitados para o usuário marcar ou não esta opção e os que estiverem com “N” não deverão aparecer nessa apresentação. 	OS2328-L		RN146	Na tela de geração do arquivo magnético será habilitado o campo “Livro Auxiliar” para que o usuário selecione qual  auxiliar o mesmo deseja gerar o livro tipo “Z”, assim como funciona hoje para o livro “A”.	OS2328-L		RN147	Os registros 0150, 0180, I012, I015,I075, I150, I155, já são tratados no mastersaf para livros como “G” e “R” estes deverão ser replicados para quando da geração do Livro Tipo “Z – Razão Auxiliar”  os registros já citados sejam gerados também. Lembrando que a base para valores do livro “Z” é a X101 e X102.	OS2328-L		RN148	Os Registros I500 e I510 já são gerados atualmente, porém como houve alteração na tela que essas informações são buscadas, esses registros terão de ser verificados conforme segue as demais regras:	OS2328-L		RN149	Registro I500
Campo 01 será fixo contendo “I500” como dado.
Campo 02 terá a fonte informada pelo usuário no campo “Tamanho da fonte” da tela de Impressão do Livro Razão Auxiliar	OS2328-L		RN150	Registro I510:

Campo 01 será fixo contendo “I510” como dado. (Exemplo: |I510| )

Campo 02 será gerado de acordo com a informação que for encontrada no campo “CAMPO” da tela “Impressão do Livro Razão Auxiliar”, o sistema fará a seguinte verificação:
Se o conteúdo do campo for menor que 16 posições, o sistema trará toda essa informação para o campo 2 do registro I510 (Exemplo: |Conta| ).
Se existirem mais de uma palavra excedendo 16 posições exemplo: Conta Contra Partida, o sistema colocará a primeira letra da primeira palavra e trará as outras (Exemplo: |C Contra Partida| ).
Se o conteúdo encontrado ocupar mais que 16 posições mesmo abreviando a primeira palavra, esta será cortada. (Exemplo: Conta Consideravelmente ficará |C Consideravelme| )

Campo 03 terá a descrição informada no campo chamado “CAMPO” da tela de Impressão do Livro Razão Auxiliar não podendo exceder 50 posições.

Campo 04 buscará a informação colocada no campo “Tipo.” da tela de Impressão do Livro Razão Auxiliar não podendo exceder uma posição, variando entre “N” ou “C”.

Campo 05: buscará a informação colocada no campo “Tam.” da tela de Impressão do Livro Razão Auxiliar não podendo exceder 3 posições.

Campo 06: buscará a informação colocada no campo “Dec.” da tela de Impressão do Livro Razão Auxiliar não podendo exceder 2 posições. Observe a informação do campo “Dec” servirá para gerar a quantidade de casas decimais para campos com tipo “N”.

Campo 07: buscará a informação colocada no campo “Largura” da tela de Impressão do Livro Razão Auxiliar não podendo exceder 3 posições.	OS2328-L		RN151	Registro I550:
O campo “Importar arquivo Externo” da tela de Manutenção > Livro Razão Auxiliar servirá para gerar o conteúdo dos campos criados no registro I510.	OS2328-L		RN152	Registro I555:

Os Campos “Agrupar por, Totalizar Por e Totalizador Geral” servirão para geração do registro “I555”.

Se o usuário selecionar uma opção qualquer no campo “Agrupar por”, na geração do arquivo magnético, este deverá fazer a totalização no registro I555, além disso o usuário deverá informar ao sistema qual campo será sumarizado através da parametrização do campo “Totalizar por”. Após isso o sistema somará os valores conforme a quebra dessa opção. Exemplo:

Data             Conta                    Descrição            Credito                   Histórico                                          Valor

02122008     1.1.2.92.10-6-00  Salários              4.9.8.82.10-0-01      VR. ARREC. DO DIA                      281,96
02122008     1.1.2.92.10-6-00  Salários              4.9.8.86.10-6-01      RECEV. TAXA ADM. DO DIA           43,70
02122008     2.1.3.91.10-6-00  Salários              4.9.8.86.10-6-01      RECEV. TAXA ADM. DO DIA           43,70

Selecionei no campo “Agrupar por” a opção “Conta”, e no campo “Totalizar por” optei por sumarizar o campo “Valor” o resultado dessa parametrização será: Todas as vezes que mudar a conta, o sistema deverá somar os valores para cada uma e gerar um I555 em baixo do registro I550 da conta correspondente, exemplo:

|I550|02/12/2008|1.1.2.92.10-6-00|4.9.8.82.10-0-01|VR. ARREC. DO DIA|281,96|
|I550|02/12/2008|1.1.2.92.10-6-00|4.9.8.86.10-6-01|RECEV. TAXA ADM. DO DIA|43,70|
|I555|TOTAL 1.1.2.92.10-6-00||||325,66|
|I550|02/12/2008|2.1.3.91.10-6-00|4.9.8.86.10-6-01|RECEV. TAXA ADM. DO DIA|43,70|
|I555|TOTAL 1.1.2.92.10-6-00||||43,70|

O registro gerado terá como texto Fixo no segundo campo “Total” o restante do texto será variável conforme o usuário fizer a opção do totalizador. Neste exemplo acima ele optou por conta, então no registro totalizador será gerado o fixo “Total + o campo escolhido “1.1.2.92.10-6-00”.
Os outros campos permanecerão vazios enquanto que o ultimo campo referente ao I550 virá com o total.	OS2328-L		RN153	
Se o usuário flegar o campo “Totalizador Geral”, na geração do arquivo magnético, este deverá fazer a totalização no registro I555 e caso tenha registros criados pelo campo “Agrupar por e Totalizar por” este deverá ser a soma destes. Exemplo:

Data             Conta                    Descrição            Credito                   Histórico                                          Valor

02122008     1.1.2.92.10-6-00  Salários              4.9.8.82.10-0-01      VR. ARREC. DO DIA                      281,96
02122008     1.1.2.92.10-6-00  Salários              4.9.8.86.10-6-01      RECEV. TAXA ADM. DO DIA           43,70
02122008     2.1.3.91.10-6-00  Salários              4.9.8.86.10-6-01      RECEV. TAXA ADM. DO DIA           43,70
31122008                                                                                                                                                     369,36

Selecionei no campo “Agrupar por” a opção “Conta”, selecionei no campo “Totalizar por” a opção “Valor” e fleguei o campo “Totalizador Geral”.
Resultado (exemplo):

|I550|02/12/2008|1.1.2.92.10-6-00|4.9.8.82.10-0-01|VR. ARREC. DO DIA|281,96|
|I550|02/12/2008|1.1.2.92.10-6-00|4.9.8.86.10-6-01|RECEV. TAXA ADM. DO DIA|43,70|
|I555|TOTAL 1.1.2.92.10-6-00||||325,66|
|I550|02/12/2008|2.1.3.91.10-6-00|4.9.8.86.10-6-01|RECEV. TAXA ADM. DO DIA|43,70|
|I555|TOTAL 1.1.2.92.10-6-00||||43,70|
|I555|TOTAL GERAL||||369,36|


O registro gerado terá como texto Fixo no segundo campo “Total Geral” Os outros campos permanecerão vazios enquanto que o ultimo campo referente ao I550 virá com o total dos I555 anteriores.	OS2328-L		RN154	Os registros I150 e I155 não são gerados pelo mastersaf quando o livro em destaque é o “Z - Razão Auxiliar”. Estes deverão apartir desta OS, passarem a ser gerados quando houver informações de saldos por centros de custo X80.	OS2328-L		RN155	Na tela de “Dados Iniciais” na Guia/Aba “Dados Iniciais” será retirado o campo “Outras informações das Demonstrações Contábeis (Balanço Patrimonial e Demonstração de Resultado) Localização do arquivo no formato RTF:”  Onde pode ser visualizado no item 2.1.1.1.1 na 1º tela do documento de requisitos.
Nessa mesma tela será criada uma nova Guia/Aba chamada “Demonstrações Contábeis”.	OS2328M		RN156	A nova Guia criada terá a seguinte forma:

Terá 2 grandes campos, um chamará “Identificação da Demonstrações” e o outro chamará “Localização do arquivo RTF”.

Dentro do campo “Identificação das Demonstrações” existirão duas colunas, uma chamada “Tipo” em formado Dropdown com as indicações fixas 1 ou 2, e outra coluna chamada “Cabeçalho das Demonstrações” esta deverá estar habilitada somente quando o usuário informar na coluna anterior a opção “1”.

Dentro do Campo Localização do arquivo RTF terá apenas uma coluna com o nome “Outras Informações das Demonstrações Contábeis (Balanço Patrimonial e Demonstração de Resultado)” 

Ao lado do campo “localização do arquivo RTF”, terá uma pasta “Abrir” no momento que o usuário aciona - la, será apresentada a janela, onde o usuário informará em qual diretório o arquivo se encontra, este servirá para buscar os arquivos em formato “Rich Text”.

Ao lado esquerdo da pasta abrir estará localizado o campo “Adicionar Arquivos”. Quando o usuário escolher o arquivo este deverá clicar no botão “Adicionar Arquivos” que levará o mesmo para a coluna “Outras Informações das Demonstrações Contábeis (Balanço Patrimonial e Demonstração de Resultado)” localizada abaixo deste. O usuário poderá selecionar quantos arquivos desejar.	OS2328M		RN157	Dentro do campo “Identificação das Demonstrações” no campo Tipo Deverá vir Default, a opção “1” que significa: Demonstrações Contábeis do Empresário ou Sociedade empresária a que se refere a escrituração.

O campo “Tipo” será obrigatório e o usuário não poderá sair da tela sem confirmar essa informação.
A tela permitirá a gravação somente com o campo “Tipo” preenchido.

O Campo “Cabeçalho das demonstrações” será obrigatório quando o usuário informar no campo “Tipo” a opção “2” que significa “Demonstrações Consolidadas ou de outros empresários ou sociedades empresárias”. 	OS2328M		RN158	O tela poderá ser gravada com somente o campo “Tipo” que é o único inicialmente obrigatório quando este estiver como “1”. 

Se o usuário colocar nesse campo “Tipo” a opção “2” também deverá preencher o campo “Cabeçalho das demonstrações” e só então a tela será liberada para gravação.

O usuário poderá cadastrar uma tela como “Tipo = 1” confirmar, clicar em novo e será aberto uma nova linha para que ele cadastre novamente as informações.

Se ele tentar cadastrar novamente uma Demonstração com “Tipo = 1” deverá ser apresentada a seguinte mensagem: “Esse Tipo não permiti ser cadastrado novamente, favor informar um diferente”.

O usuário poderá cadastrar quantas vezes quiser essa tela desde que o campo “Tipo seja = a 2”.

Conforme forem sendo adicionados mais cadastros, deverá ser adicionada uma linha na caixa de identificação das demonstrações, onde o usuário poderá ver o que foi parametrizado para cada linha clicando em cima delas. 	OS2328M		RN159	Se na tela de “Dados Iniciais na Aba Demonstrações Contábeis”, somente constar um cadastro com o campo “Tipo” =  “1”, quando o usuário gerar o arquivo magnético, o sistema deverá reconhecer essa parametrização gerando um “J005”  com o campo “4” do registro com a informação “1”.	OS2328M		RN160	Se na tela de “Dados Iniciais na Aba Demonstrações Contábeis”, somente constar um cadastro com o campo “Tipo” = “2”, quando o usuário gerar o arquivo magnético, o sistema deverá reconhecer essa parametrização gerando um “J005”  com o campo “4” do registro com a informação “2”.	OS2328M		RN161	Se a opção “2 – Demonstrações Consolidadas ou de Outros Empresários ou Sociedades empresárias”. For marcada, o campo “5” do registro “J005” deverá ser gerado conforme a descrição colocada no campo “Cabeçalho das Demonstrações” da tela de “Dados Iniciais Aba Demonstrações Contábeis”.
Se a opção estiver desabilitada o campo “5” do registro J005 deverá ser gerado em branco “pipe e pipe” (||).	OS2328M		RN162	Se feito dois cadastros um com o campo “Tipo = 1” e outro com o campo “Tipo = 2” da tela de Dados Iniciais aba demonstrações contábeis, serão gerados dois registros J005, com o campo “4” com a informação “1” e outro registro com a informação “2”, o registro que estiver com a informação “2” deverá também ter o campo “5” preenchido com a descrição colocada no campo “Cabeçalho das Demonstrações”.	OS2328M		RN163	Os registros “J005” deverão ser gerados separados, cada um abrirá um grupo de informações.

Após aberto o grupo do “J001” como é feito hoje, primeiro deverá vir o registro “J005” correspondente ao “Tipo = 1” da tela de Dados Iniciais aba demonstrações contábeis, os campos 2 e 3 desse registro deverão continuar gerando normalmente como é hoje, que são as datas da geração localizadas na tela de geração do arquivo magnético.
Em seguida virão os registros J100 e J150 já gerados hoje pelo mastersaf.
Em seguida a esses será gerado o registro J800 que será conforme cada arquivo adicionado na tela de Dados Iniciais aba demonstrações contábeis,

O Sistema deverá verificar a seguinte ordem para poder começar o grupo do próximo “J005”.

J005 campo 4 = 1
J100  (BP)
J150 (DRE)
J800 pode ou não ter (Notas explicativas)
J005 campo 4 = 2
J800 pode ou não ter (Notas explicativas)
J005 campo 4 = 2	OS2328M		RN164	Os registros totalizadores como, por exemplo,  “J990” , “9999” deverão considerar na sua contagem a quantidade de registros total do arquivo.	OS2328M		RN165	Quando o usuário tiver indicado o campo “Tipo = 2” da tela de Dados Iniciais aba demonstrações contábeis, o único resultado no TXT será no máximo ele gerar o registro “J005” e permitir a geração dos registros “J800” não será tratado geração de “J100 e J150” nessa OS para esse indicador.	OS2328M		RN166	Para alteração deverá ser considerada a parametrização que o usuário tenha feito anterior a essa alteração na tela de dados iniciais. As parametrizações do usuário serão levadas para a nova tela onde o usuário poderá continuar as gerações como é feito hoje, ou alterar conforme sua necessidade.	OS2328M		RN167	O registro “J005” é Pai dos J100, J150 e J800, sendo assim, o sistema deverá fazer a seguinte verificação:
Se o usuário tiver parametrização efetuada na tela de códigos de aglutinação (BP/DRE) no menu manutenção, este deverá exigir a parametrização da tela de Dados iniciais aba Demonstrações Contábeis. Que define as informações do registro Pai.

Na geração do meio magnético feito essa verificação e não encontrado deverá ser acusado no “log” a seguinte mensagem: Registros J100 e J150 não serão gerados pela falta do registro J005, favor verificar a parametrização do mesmo no caminho: Parâmetros > Dados Iniciais > Guia Demonstrações Contábeis.
	OS2328M		RN168	As alterações deverão atingir inicialmente os livros “R, G” que já são tratados pelo mastersaf, e posteriormente o livro “B” que será tratado na OS2328J1.	OS2328M		RN169	Os registros I350 e I355 não deverão aparecer na tela de Perfil quando o usuário selecionar os livros “A” e Z”, devido alteração no layout. Conforme “INFOLEGIS_229_09_F_ECD_IN_926.doc”	CH59678		RN170	Devido essa observação, a RN03 é alterada pela indicação da tela no documento de requisitos a que se refere o livro “A”, pois no layout anterior esses registros eram facultativos. Com a alteração estes não se aplicam aos livros auxiliares, devendo não serem gerados para esses livros.	CH59678		RN171	No drop-down “Responsável” da aba Signatário, o sistema deve exibir o Representante Legal precedido do código. 
Exemplo: 2 – João da Silva. Desta forma, pelo indicador ele será identificado como o contador.
	CH59112		RN172	Caso um Representante Legal esteja cadastrado mais de uma vez no MasterSAF, a gravação na tabela SPED_DADOS_SIGNATARIO deve informar o código do Representante Legal selecionado pelo usuário (ind_categoria + nom_responsável), e não mais o menor valor.	CH59112		RN173	A visualização na tela de signatários se dará por indicador de categoria.	CH59112		RN174	No caso de o responsável estar inativo (ind_ativo = ‘I’) no cadastro dos responsáveis, o mesmo não deverá ser listado na tela de Signatários.	CH59112		RN175	Nessa tela “Código de Aglutinação (Balanço Patrimonial e Demonstração de Resultado)” no campo “Classificação” será incluso mais duas opções de seleção, chamadas “Subtotalizador/Totalizador Ativo” e “Subtotalizador/Totalizador Passivo”.	OS2328-P		RN176	Quando o usuário clicar em novo e optar por um das classificações  de totalizadores exemplo “Subtotalizador/Totalizador - Ativo”, o sistema acusará a seguinte mensagem: “A inclusão de um código Subtotalizador/Totalizador requer o prévio cadastramento dos Códigos de Ativo e Passivo ou Patrimônio Líquido que o compõe, para definição de sua regra”.
O Usuário poderá clicar no botão “OK” que haverá na mensagem, e o sistema libera para seguir com as parametrizações.	OS2328-P		RN177	O tamanho da linha apresentada para os códigos de aglutinação ficará maior para atender as novas opções.
Quando o usuário acionar o “OK” da mensagem escrita na regra acima, será apresentada uma nova linha abaixo da parametrização do código de aglutinação  que o mesmo estará cadastrando.	OS2328-P		RN178	Nesta linha será habilitada uma pasta “Abrir”, onde será disponibilizado ao usuário, todos os códigos aglutinadores criados anteriormente, conforme seu totalizador.
Exemplo:
Para o Subtotalizador/Totalizador Ativo – só poderão ser selecionados os códigos de aglutinação criados com Classificação “Ativo”.
Da mesma forma que, para o Subtotalizador/Totalizador Passivo ou PL – só poderão ser selecionados os códigos de aglutinação criados com Classificação “Passivo ou Patrimônio Liquido”.	OS2328-P		RN179	Conforme cada código de aglutinação for adicionado, o sistema deverá separá-los através de ponto e vírgula “;” assim como ocorre para a tela da DRE.	OS2328-P		RN180	A lógica existente para esse Subtotalizador/Totalizador, deverá ser a mesma existente na geração do Registro “J150 - da DRE – Demonstração de Resultado”.
Que sumariza os valores referentes às contas relacionadas e informa no campo 5 do registro J150, que no caso dessa alteração será no campo “6” do registro J100 – Balanço Patrimonial.	OS2328-P		RN181	Na geração do arquivo magnético também deverá ser levado em conta o indicador informado no registro “J100” Balanço Patrimonial, quando o Subtotalizador/Totalizador for do Ativo o indicador no campo 6 do registro J100 será “1”.
Quando o Subtotalizador/Totalizador for do Passivo ou PL o indicador no campo 6 do registro J100 será “2”.	OS2328-P		RN182	O Relatório de Códigos de Aglutinação - Balanço Patrimonial, não contempla Centros de Custos, portanto não deve ser feito nenhum relacionamento entre as contas empresa e centros de custo neste relatório, para essa tela.	CH59742		RN183	O Relatório de Códigos de Aglutinação – Demonstração de Resultado deve contemplar a possibilidade de haver relacionamento entre as contas empresas associadas a contas aglutinadoras e centros de custo.	CH59742		RN184	A observação: “* C.Custo - Informar apenas se a conta referencial x conta da empresa não for suficiente para o relacionamento, dependendo da seleção dos Centros de Custo” deverá ser visível apenas na aba de “Demonstração de Resultado” desta janela.	CH59742		RN185	Atualmente o mastersaf soma todos os lançamentos a crédito referente o registro I250, e gera um registro I200 com o total no campo 4.
Quando essa soma for “0” (zero), o sistema deverá somar as partidas a débito e gerar um registro I200 com o campo 4 populado o valor total a débito. Dessa forma será corrigido o erro do campo “4” sair zerado quando não existem partidas a crédito.
OBS: não deverão ser somadas as partidas débitos com as de créditos, ou um ou outro.
Essa regra se aplica ao livro auxiliar “A”. 
A crítica que os lançamentos de Débito não batem com os de Crédito, referente ao I250 só deverá acontecer quando o livro for diferente de “A”.	CH57895		RN186	Será criado a Safx2101 que conterá as informações que hoje estão armazenadas em duas tabelas, sendo elas: SPED_CONTAS_REF_EMP 
SPED_CONTAS_REF_CCUSTO	OS2328-U		RN187	Deverão conter os seguintes campos na safx2101 

Código da conta referencial (Contido da TFIX64);
Versão(Contido da TFIX64);
Condigo da Entidade(Contido da TFIX64);
Código conta (Contido da safx2002);
Indicador(Contido da safx2002);
Código do Centro de Custo (Safx2003);
	OS2328-U		RN188	Durante a carga da Safx ou a importação, os únicos campos que serão permitidos carrega-los em branco ou nulo, são:
Código do Centro de Custo (Safx2003);
Caso algum campo diferente esteja em branco ou nulo, o sistema irá impedir a carga desse registro.
	OS2328-U		RN189	Durante a importação, o sistema  irá verificar se o indicador da conta (Contido da safx2002) é igual a “S” (Sintética), caso SIM, não será permitido a importação desse registro.
A importação será permitida apenas quando o campo estiver contido com “A” (Analítica), se estiver diferente disso será impedido a importação do registro.

Mensagem no Log

É permitido apenas importar contas contábeis analíticas.
	OS2328-U		RN190	Caso o Código do Centro de Custo (Safx2003) esteja em branco o sistema irá gravar na tabela o campo ident do centro de custo igual a “0” (zero) na tabela definitiva.
	OS2328-U		RN191	Caso o usuário importe a mesma conta contábil (Safx2002) de uma mesma empresa para contas referenciais de diferentes entidades, o sistema deverá impedir essa importação.

Exemplo:
Conta: 1.0.1
Conta Referencial: 1.0.0 Entidade: 10

Conta: 1.0.1
Conta Referencial: 1.0.3 Entidade: 20

Caso essa situação ocorra dentro de um mesmo arquivo de importação ambos os registros não serão importados.
Caso essa situação ocorra quando já houver dados na tabela, o sistema deverá manter o existente e bloquear a importação do novo registro.

Mensagem no Log.

Plano de contas informado para mais de uma entidade.
	OS2328-U		RN192	ALTERADA – OS3143-A]
Caso durante a importação conter registros de entidades que sejam diferentes da informado no manual layout, acusar erro.

Se
COD_ENTIDADE_RESP for diferente de 00, 10 e 20
Então
Bloquear a importação do arquivo.

Mensagem no Log
Código da Entidade Diferente da informada no Manual Layout.
Campo deve conter: 00 - SUSEP, 10 - SRF ou 20 - COSIF.

	OS2328-U
OS3143-A		RN193	Durante a importação, o sistema deverá verificar se o centro aparece para a mesma conta referencial  duas vezes, caso sim o sistema irá impedir a importação dos dois registros.

Exemplo:

Conta Ref: 1.0.0
Conta Msaf: 1.0.1 Centro de Custo 01
Conta Msaf: 1.0.2 Centro de Custo 01


Com o relacionamento demonstrado acima o sistema irá impedir a importação desse registro.

Mensagem no Log
Centro de Custo informado para mais de uma vez para a mesma conta referencia. 
	OS2328-U		RN194	Caso não encontrado o registro de Plano de contas na Safx2002, o sistema irá demonstrar a seguinte mensagem de erro:

Plano de contas não encontrado.

Realize o Cadastro da Conta Contábil não encontrada.
Modulo Dw no menu Manutenção -> Códigos -> Plano de Contas.
	OS2328-U		RN195	Caso todos os campos necessários para encontrar o centro de custo estejam informados, porém não encontrado o registro da Safx2003, o sistema irá demonstrar a seguinte mensagem de erro:

Centro de Custo não encontrado

Realize o Cadastro do Centro de Custo não encontrado.
Modulo Dw no menu Manutenção -> Codigos -> Centro de Custo
	OS2328-U		RN196	Caso todos os campos necessários para encontrar o plano de contas referencial estejam informados, porém não encontrado o registro da TFIX64, o sistema irá demonstrar a seguinte mensagem de erro:

Plano de contas referencial não encontrado

Realize a importação da TFIX64.
Modulo Ferramentas no menu Tabelas internas -> Importar -> Tabelas Fixas/ Acessórias 
	OS2328-U		RN197	Na tela Parâmetros=>Perfil, quando o usuário selecionar o “Perfil” (B – Livro Balancetes Diários e Balanços (Matriz)), os registros obrigatórios serão exibidos, porém não habilitados para opção de geração ou não do cliente;
	OS2328-J1		RN198	Se selecionado registro com nível superior aos anteriores que não tenham sido marcados, o sistema deverá marcar automaticamente no momento da seleção.	OS2328-J1		RN199	No campo Perfil o usuário poder criar vários cadastros de Perfis diferentes permitindo ao usuário fazer na geração do meio magnético o relacionamento dos perfis criados por estabelecimento. 	OS2328-J1		RN200	Os registros que deverão ser exibidos, quando da seleção do livro “[x] B – Livro Balancetes Diários e Balanços” são os registros que estão grifados em vermelho no documento de requisitos na composição dos livros.	OS2328-J1		RN201	A informação “Entidade responsável pelo plano de contas Referencial”, por regra padrão vem como Secretaria da Receita Federal, porém, Instituições Financeiras deverão selecionar a opção “20 – Banco Central do Brasil (COSIF)”, tal informação deverá ser considerada para realização do DEPARA entre contas referencial  x contas da empresa;	OS2328-J1		RN202	Quando o Usuário Selecionar a entidade responsável pelo Plano de contas como “20 – Banco Central do Brasil (COSIF)”, hoje já é apresentado ao lado direito da tela, uma caixa chamado Títulos.	OS2328-J1		RN203	A Caixa têm 21 opções de títulos para que o usuário possa marcá-los, conforme segue:
            
             U - Bancos múltiplos;
             B - Bancos Comerciais;
             D - Bancos de Desenvolvimento;
             K - Agências de Fomento ou de Desenvolvimento;
             I  - Bancos de Investimento;
             F - Sociedades de Crédito, Financiamento e Investimento;
             J - Sociedades de Crédito ao Microempreendedor;
             A - Sociedades de Arrendamento Mercantil;
             C - Sociedades Corretoras de Títulos e Valores Mobiliários e Câmbio;
             T - Sociedades Distribuidoras de Títulos e Valores Mobiliários;
             S - Sociedades de Crédito Imobiliário e Associações de Poupança e Empréstimo;
             W - Companhias Hipotecárias;
             E - Caixas Econômicas;
             R - Cooperativas de Crédito;
             O - Fundos de Investimento;
             L - Banco do Brasil S.A.;
             M - Caixa Econômica Federal;
             N - Banco Nacional de Desenvolvimento Econômico e Social;
             H - Administradoras de Consórcio;
             P- Grupos de Consórcio; 	
             Z - Empresas em Liquidação Extrajudicial.
Os títulos marcados estão referenciados na  HYPERLINK "http://www.mastersaf.com.br/helpdw/V1R320/TXT/Tfixas_Tacessorias/TFIX64.TXT" \t "_blank" TFIX 64 - Plano de Contas SPED Contábil (SPED Contábil) em frente as contas, esse relacionamento terá impacto na apresentação das contas.	OS2328-J1		RN204	O Contribuinte/Usuário deverá informar nessa tela com quais tipos de títulos que essa instituição financeira mantém operação, marcando – os através do Check box localizado do lado esquerdo de cada título. 	OS2328-J1		RN205	A seleção dos títulos mencionados nas regras acima, fará com que somente as contas que estão referenciadas a eles na TFIX64, sejam apresentadas nas telas onde as contas contábeis são apresentadas. Como por exemplo, (De/Para e BP/DRE)	OS2328-J1		RN206	[ALTERADA – OS2848] Essa tela Possibilitará ao usuário definir por estabelecimento livros a serem gerados, bem como sua periodicidade e Número de ordem do livro. O usuário também poderá através desta funcionalidade visualizar os livros gerados anteriormente para acompanhamento, conforme as regras a seguir.	OS2328-J1		RN207	[ALTERADA – OS2848] Nessa tela o usuário fará a parametrização que define a existência do Livro.
No campo “Livro” da Aba de Livros Principais, entre as opções já existentes, deve constar “B – Livro Balancetes Diários e Balanços (Matriz)”: 
O campo “Periodicidade” estará disponível para esse Livro, inclusive todas as suas Opções (Diária, Mensal e Anual).
O campo “Número de Ordem” também deverá estar habilitado, para que o usuário informe manualmente o número do livro digital. 	OS2328-J1		RN208	Nessa tela também ficará guardado, o histórico dos livros que já foram gerados pelo mastersaf, assim como ocorre atualmente para os outros livros do SPED Contábil atendidos pelo sistema. No Historio deve conter as seguintes informações: 
Qual livro foi gerado, a data contendo as horas, minutos e segundos; a periodicidade definida para este livro, a data inicial e final da geração e o número de ordem do livro.	OS2328-J1		RN209	Essa tela Possibilitará ao usuário definir por estabelecimento Termo de Abertura e Encerramento para o livro Perfil “B” Livro Balancetes Diários e Balanços com todas as funcionalidades já existentes na tela, tamanho e campos disponíveis.	OS2328-J1		RN210	Na tela do Plano de contas referencial o campo “Entidade Responsável”, vem como Default “10 – Secretaria da Receita Federal”, nesta o usuário pode trocar para entidade “20 – Banco Central do Brasil (Cosif)” e quando isso ocorre às contas do COSIF são apresentadas.	OS2328-J1		RN211	Para geração do Registro I300 o mastersaf deverá se comportar da seguinte maneira:
I300:
Campo 01: Fixo I300
Campo 02: “Data lançamento”  informada no campo 03 da X01.	OS2328-J1		RN212	Para geração do Registro I310 o mastersaf deverá se comportar da seguinte maneira:
I310:
Campo 01: Fixo I310
Campo 02: Código da conta analítica debitada/creditada “campo  04 da X01”
Campo 03:  C.C informado no “campo 09” da X01
Campo 04: trará a soma dos valores lançados a Débito, feito naquele determinado período. Campo 07 da X01.
Campo 05: trará a soma dos valores lançados a Crédito, feito naquele determinado período. Campo 07 da X01.	OS2328-J1		RN213	Para que a regra acima, funcione corretamente, o sistema deverá se comportar da seguinte forma:
Se houver mais de um lançamento para a mesma conta, o sistema deverá somar os valores a débito dela, daquele período, e jogar no campo 04 do registro I310.
E se para a mesma conta houver ainda lançamentos a crédito, o sistema deverá somar os créditos dela, e jogar no campo 05 do mesmo registro I310.	OS2328-J1		RN214	Quando houver mais de um lançamento para mesma conta relacionado com C.C diferente o sistema fará a geração dos registros I310 conforme a existência dos C.C.
Exemplo:
Conta XXX Valor Lançamento 100,00 C.C 001
Conta XXX Valor Lançamento   50,00 C.C 002

O arquivo magnético será gerado da seguinte forma:

|I310|XXX|001|100,00|
|I310|XXX|001|50,00|	OS2328-J1		RN215	O Arquivo Magnético somente será gerado conforme definição acima, se o campo “omitir centro de custo” estiver desmarcado. 

OBS: O campo “Omitir centro de custo” também impacta nas informações apresentadas no registro I155, isso deverá continuar, do mesmo jeito.	OS2328-J1		RN216	Se esse campo “Omitir Centro de Custo” estiver marcado o sistema fará a geração do registro I310 para mais de um lançamento para a mesma conta com C.C diferente da seguinte forma:
|I310|XXX||150,00|	OS2328-J1		RN217	Na geração do SPED Contábil para o livro perfil tipo “B” o sistema obrigatoriamente precisará ter gerado os seguintes registros: 0000, 0001, 0007, 0990, I001, I010, I030, I050, I150, I155, I300, I310, I990, J001, J900, J930, J990, 9001, 9900, 9990, 9999.	OS2328-J1		RN218	Para que os totalizadores sejam gerados corretamente e passe no validador, o sistema deverá gerar um registro I052 p/ os códigos de aglutinação que estiverem como totalizadores no registro "J100".
Os registros I052 gerados deverão ser correspondentes a cada conta, cujo código de aglutinação teve ela amarrado. 	OS2328-P
Complemento		RN219	Para essa geração, o sistema deverá observar a conta associada ao código de aglutinação que está sendo totalizado e gerar um registro I052 com o código de aglutinação totalizador.

Exemplo:

As contas 1000 e 1001 estão relacionadas com o código de aglutinação 8.5.8 e as contas 2000 e 2001 com o código de aglutinação 9.6.9.

Os códigos 8.5.8 e 9.6.9 estão sendo totalizadas pelo código de aglutinação 9.9.9.9.

O código de aglutinação 9.9.9.9 é um totalizador e deverá somar todos os valores das contas relacionadas aos códigos 8.5.8 e 9.6.9.

A geração do registro I052 do meio magnético deverá ser da seguinte forma:

|I050|||||1000|||
|I052||8.5.8|
|I052||9.9.9.9|
|I050|||||1001|||
|I052||8.5.8|
|I052||9.9.9.9|
|I050|||||2000|||
|I052||9.6.9|
|I052||9.9.9.9|
|I050|||||2001|||
|I052||9.6.9|
|I052||9.9.9.9|

O código 9.9.9.9 que está como totalizador para os códigos 8.5.8 e 9.6.9 e está sendo gerado no registro I052 para todas as contas associadas a esses mesmos códigos de aglutinação que estão sendo totalizados.”	OS2328-P
Complemento		RN220	Na geração do meio magnético da ECD, o  Sistema identifica o número do lançamento e o valor total dos créditos, a soma deste, ele joga no Registro I200.
 No momento que o sistema for gerar o Registro I250, ele deverá trazer todos os dados das tabelas de lançamentos referentes o livro que esta sendo gerado. Mesmo que o indicador de débito e crédito seja diferente para a mesma conta.
Essa regra se aplica a todos os livros que gerar os registros I200 e I250.	CH61131		RN221	Quando o sistema identificar lançamentos feitos nas tabelas X01 e X101, cujo arquivamento sejam o mesmo, a data seja a mesma, a conta seja a mesma, o número de lançamento seja o mesmo, mas, o indicador do Débito e Crédito seja diferente entre eles, o SPED deverá gerar os registros da forma com que foram carregados nas tabelas de lançamentos.
O arquivo gerado deve ser submetido ao PVA e validado com sucesso.	CH61131		RN222	Esse chamado altera a RN196 da OS 2328-U.
Quando houver contas da empresa, com data de validade inferior a data de validade da conta do referencial COSIF, não deverá ser feita nenhuma crítica a respeito.	CH64207		RN223	Esse chamado altera a RN196 da OS2328-U.
A importação da tabela SAFX2101.COD_ENTIDADE_RESP não terá crítica nenhuma em relação a data de validade da conta empresa x conta do referencia, conforme previsto na RN196.	CH64207		RN224	Geração do livro “R” (Registro I012 campo 03) – Quando o campo 02 do registro I010 for igual a “R” (somente se existirem livros auxiliares), preencher com os dados dos livros auxiliares (“A” ou “Z”) coluna TERMO_ABERTURA da tabela SPED_TERMOS_LIVRO.	CH64346		RN225	Geração do livro “A” (Registro I012 campo 03) – Quando o campo 02 do registro I010 for igual a “A” ou “Z”, preencher com os dados do livro com escrituração resumida (“R”) coluna TERMO_ABERTURA da tabela SPED_TERMOS_LIVRO.
	CH64346		RN226	Parametrização dos Códigos de Aglutinação do Balanço e da DRE – Em ‘Manutenção > Códigos de Aglutinação’, na aba Balanço Patrimonial, ao selecionar a opção ‘Selecionar Contas da Empresa para Apuração, deve ser possível pesquisar as contas da empresa cuja natureza (campo IND_NATUREZA) seja: 1 - Ativo, 2 - Passivo, 5 - Mutações Ativas, 6 - Mutações Passivas, 7 - Patrimônio Líquido ou 9 – Outros
Obs.: Todas as naturezas citadas acima também devem ser consideradas na geração dos registros I052 e J100.
	CH64454		RN227	Parametrização dos Códigos de Aglutinação do Balanço e da DRE – Em ‘Manutenção > Códigos de Aglutinação’, na aba Demonstração de Resultado, ao selecionar a opção ‘Selecionar Contas da Empresa para Apuração, deve ser possível pesquisar as contas da empresa cuja natureza (campo IND_NATUREZA) seja: 3 - Despesa, 4 - Receita, 8 - Custo ou 9 – Outros
Obs.: Todas as naturezas citadas acima também devem ser consideradas na geração dos registros I052 e I355 e J150.
	CH64454		RN228	Deverá ser criado na tabela X2101 que é onde esta o relacionamento das contas da empresa x as contas do referencial e seus possíveis centros de custo, duas colunas, uma “empresa” e outra “Estabelecimento”.
	CH63450		RN229	Será criado na tela de Plano de contas Referencial x Plano empresa um campo chamado “Estabelecimento” este não estará habilitado ao usuário, e trará o estabelecimento que o mesmo estiver logado.

Se o usuário não estiver logado em nenhum estabelecimento esse campo deverá estar habilitado em forma de dropdown para que o mesmo selecione o estabelecimento.	CH63450		RN230	O relatório disponível na barra de ferramentas da tela de Plano de contas Referencial x Plano empresa deverá ser atualizado de forma que saia no relatório o relacionamento das contas conforme a empresa e o estabelecimento.	CH63450		RN231	A geração do relatório existente no menu: Relatórios > Relatório Sintético/Analítico deverá ser alterada para considerar em seu processamento (tanto no relatório analítico quanto sintético) apenas a parametrização existente na tabela x2101 para aquela empresa e estabelecimento selecionado no momento da geração do relatório.	CH63450		RN232	Quando nos dados iniciais estiver parametrizado ‘Gerar Plano de Contas: Completo’, o sistema deve continuar utilizando a regra atual de geração do registro I050, mas, a regra de geração do registro I051 será alterada para considerar apenas as parametrizações do de/para referente à empresa e estabelecimento que foi selecionado na tela de geração do arquivo.
Quando nos dados iniciais estiver parametrizado ‘Gerar Plano de Contas: Somente Contas Movimentadas no período da geração’, o sistema deve continuar utilizando a regra atual de geração do registro I050 e deverá gerar o registro I051 para as contas que foram geradas no I050 se houver parametrização para aquela conta na empresa e estabelecimento selecionado no momento da geração.	CH63450		RN233	O Relacionamento do Plano de contas do referencial x Plano de contas empresa não deverá levar em conta a data de validade constante na TFIX64.
Atualmente o mastersaf importa a TFIX 64 com sucesso com novas contas adicionadas, porém quando o usuário utiliza essas novas contas para parametrização a gravação das mesmas não é feita, por que o sistema leva em conta a data de validade da conta da empresa com a data de validade da conta do referencial na TFIX 64 e isso não pode ocorrer, pois essas datas de validades da TFIX são apenas informativas, para as empresas.	OS2328Z		RN234	A geração do arquivo magnético deverá ocorrer com sucesso, gerando os registros I051 corretamente considerando o De/Para com as novas contas.	OS2328Z		RN235	Os Relatórios sintéticos e analíticos deverão considerar as novas contas no de/para com sucesso, sem críticas.	OS2328Z		RN236	Na geração do registro J150 quando a opção ‘Omitir Informações de Centro de Custo’ estiver marcada nos dados iniciais, o MasterSAF não deve validar se existe parametrização por centro de custo na tabela SPED_CONTAS_AGLUT_EMP_CUSTO e se existe saldo por centro de custo na TMP_SPED_CONTAS_CUSTO, pois, quando essa opção é marcada, ao preencher a tabela TMP_SPED_CONTAS_CUSTO o aplicativo despreza a informação do Centro de Custo, então, nunca existirá saldo por centro de custo nessa tabela e existirá parametrização da DRE por centro de custo, causando o erro “Existe Código de Aglutinação parametrizado com Regra por Centro de Custo, porém não há saldo por centro de custo.”

Quando essa opção estiver marcada o MasterSAF deve buscar na tabela TMP_SPED_CONTAS_CUSTO o valor do saldo para aquela conta (que terá sido gravado na tabela sem informação de centro de custo) e deve utilizar esse valor no somatório para a geração do registro J150.	CH65081		RN237	Quando o sistema buscar os NIRE da tabela REGISTRO_ESTADUAL disponível no módulo > Parâmetros > Preliminares > Inscrição Estadual >, mesmo que lá tenha caracteres especiais separadores, como por exemplo, o (ponto), não deverá ser carregado para o registro I030 no campo 07, ele deverá levar apenas os números no NIRE.	CH65041		RN238	Se durante a importação da SAFX2101 ou na manutenção da X2101_CONTAS_REF_CCUSTO for verificado que uma Conta Empresa está relacionada com mais de uma Conta Referencial, deverá ser apresentada no Log a seguinte mensagem:

“A Conta Empresa XXXX já está associada a(s) seguinte(s) Conta(s) Referencial(ais) : YYYY; ZZZZ.”

A mensagem será meramente informativa, não devendo impactar na importação do arquivo, sendo considerada apenas como um Warning.

Deverá ser verificado o tamanho final da mensagem para que o campo da mensagem do banco não seja ultrapassado.  Se o tamanho for maior, a mensagem deverá ser desmembrada.	OS2328-V		RN239	Se for gerada uma mensagem de log conforme descrito na RN238, deverá ser apresentada na janela de manutenção (Menu SPED,  Módulo: SPED Contábil,  Menu: Manutenção ( Plano de Contas Referencial x Plano de Contas da Empresa) a mensagem abaixo: 
 
“A Conta Empresa XXXX está associada a outra(s) Conta(s) Referencial(ais).  Favor verificar o Log gerado para o Processo: nnnnn.”	OS2328-V		RN240	Ao clicar para selecionar o signatário nos dados inciais, deverá ser apresentada na tela de busca, os campos que estão na tabela do responsável pela informação, dentro do módulo parâmetro, para que o usuário possa identificar e selecionar corretamente o representante.	2328-R4		RN241	Ao selecionar um determinado representante o usuário deverá então indicar a classificação para o mesmo, e somente poderá selecionar um novo representante após confirmar a informação que foi inserida anteriormente. 	2328-R4		RN242	Ao clicar na opção novo, deverá ser apresentada uma nova pasta abaixo de uma já existente, ou um nova pasta caso não existe nenhum representante já cadastrado.	2328-R4		RN243	A tela para geração do relatório será denominada ‘Demonstrações Contábeis’ e deverá conter:

- O campo Estabelecimento que será um combo onde estarão disponíveis para seleção os estabelecimentos centralizadores (parametrização feita no módulo Parâmetros > Centralização da Escrituração Contábil), os estabelecimentos que não são centralizadores e que não foram centralizados em nenhum outro estabelecimento, e ainda a opção ‘Todos’. Só devem ser apresentados para seleção os estabelecimentos que o usuário que está gerando o relatório tem acesso (ver parametrização no powerlock para esse usuário);
- O campo período que deverá conter dois textbox com máscara de data para informação da data inicial e da data final para geração do relatório;
- O quadro ‘Por Código de Aglutinação’ que deverá conter uma pasta ‘Abre’ para seleção de um código de aglutinação previamente criado no menu: ‘Manutenção > Códigos de Aglutinação’, e os campos ‘Código’ e ‘Descrição’ para demonstrar o código e a descrição do código de aglutinação escolhido;
- O quadro ‘Demonstração’ que deverá conter dois checkbox, um para seleção do Balanço Patrimonial e um para seleção da Demonstração de Resultado, por default as duas opções virão desmarcadas;
- O quadro ‘Tipo’ que deverá conter dois radiobuttons onde será possível escolher entre Analítico e Sintético, por default a opção ‘Sintético’ virá marcada.
- Um botão de ‘OK’ e um ‘Cancelar’.

Obs.: Os campos ‘Estabelecimento’, ‘Período’, ‘Balanço Patrimonial ou Demonstração de Resultado’ e ‘Analítico ou Sintético’ são de preenchimento obrigatório, portanto, deve ser emitida mensagem de aviso caso algum deles não esteja preenchido e o usuário pressione o botão ‘OK’.	OS2328-R3		RN244	Ao selecionar o botão ‘Abre’ (Pasta Amarela) no quadro ‘Por Código de Aglutinação’ o sistema deverá exibir para seleção todos os códigos de aglutinação criados para o estabelecimento selecionado, ou, os códigos de aglutinação de todos os estabelecimentos que aquele usuário tem acesso quando o usuário tiver escolhido a opção ‘Todos’ no campo ‘Estabelecimento’.
Caso o usuário ainda não tenha selecionado nenhum estabelecimento, ao clicar no botão ‘Abre’ deve ser emitida a seguinte mensagem na tela:
“Selecione um Estabelecimento”	OS2328-R3		RN245	Caso o usuário selecione um código de aglutinação no quadro ‘Por Código de Aglutinação’, o comportamento da tela será o seguinte:

- Se o código selecionado for um código do Balanço Patrimonial, no quadro ‘Demonstração’ deve ser marcada a opção ‘Balanço Patrimonial’ e desmarcada a opção ‘Demonstração de Resultado’. Quando isso acontecer a opção ‘Demonstração de Resultado’ deve ser desabilitada, para não permitir que o usuário a selecione.

- Se o código selecionado for um código da Demonstração de Resultado, no quadro ‘Demonstração’ deve ser marcada a opção ‘Demonstração de Resultado’ e desmarcada a opção ‘Balanço Patrimonial’. Quando isso acontecer a opção ‘Balanço Patrimonial’ deve ser desabilitada, para não permitir que o usuário a selecione.
	OS2328-R3		RN246	Quando na tela de geração for selecionada a opção ‘Balanço Patrimonial’, deve ser gerado um item de relatório com o título ‘Balanço Patrimonial’, e no cabeçalho as seguintes informações:

- A razão social da empresa a que pertence o estabelecimento selecionado na tela de geração;
- A data e hora de emissão do relatório;
- O código e a razão social do estabelecimento selecionado na tela de geração;
- O CNPJ do estabelecimento selecionado na tela de geração;
- O período (data inicial e data final) selecionado na tela de geração;
- O número da página do relatório.

Obs. Quando for selecionada a opção ‘Todos’ na tela de geração, esse item de relatório será gerado uma vez para cada estabelecimento pertencente a essa empresa e que porventura o usuário que está gerando o relatório tenha acesso liberado no powerlock (caso o usuário tenha alguma restrição de utilização de algum estabelecimento da empresa, esse estabelecimento não será considerado).

O conteúdo desse item do relatório está previsto na RN249 para o tipo sintético e na RN250 para o tipo analítico.	OS2328-R3		RN247	Quando na tela de geração for selecionada a opção ‘Demonstração de Resultado’, deve ser gerado um item de relatório com o título Demonstração de Resultado do Exercício’, e no cabeçalho as seguintes informações:

- A razão social da empresa a que pertence o estabelecimento selecionado na tela de geração;
- A data e hora de emissão do relatório;
- O código e a razão social do estabelecimento selecionado na tela de geração;
- O CNPJ do estabelecimento selecionado na tela de geração;
- O período (data inicial e data final) selecionado na tela de geração;
- O número da página do relatório.

Obs. Quando for selecionada a opção ‘Todos’ na tela de geração, esse item de relatório será gerado uma vez para cada estabelecimento pertencente a essa empresa e que porventura o usuário que está gerando o relatório tenha acesso liberado no powerlock (caso o usuário tenha alguma restrição de utilização de algum estabelecimento da empresa, esse estabelecimento não será considerado).

O conteúdo desse item do relatório está previsto na RN251 para o tipo sintético e na RN252 para o tipo analítico.	OS2328-R3		RN248	Quando na tela de geração forem selecionadas simultaneamente as opções ‘Balanço Patrimonial’ e ‘Demonstração de Resultado’, deverão ser gerados dois itens de relatório, um conforme RN246 e o outro conforme RN247.	OS2328-R3		RN249	Quando for selecionada a opção ‘Sintético’ e não tiver sido selecionado nenhum código de aglutinação específico na tela de geração, o item ‘Balanço Patrimonial’ deverá listar todos os códigos de aglutinação de balanço patrimonial parametrizados no menu: Códigos de Aglutinação (B. Patrimonial/DRE) do módulo SPED Contábil para aquele estabelecimento que possuam valor. Os códigos serão apresentados na coluna ‘Cód. Aglutinação - Descrição’ e essa coluna deverá conter o código de aglutinação seguido de sua descrição.
A ordem em que os códigos aparecem no relatório deverá ser exatamente a mesma ordem parametrizada no menu anteriormente citado.
Os códigos de aglutinação deverão estar corretamente identados de acordo com o nível em que o código foi criado, por exemplo: O código de nível 1 deverá aparecer na margem esquerda do relatório, o código de nível 2 estará um ‘tab’ a frente do código de nível 1, e assim sucessivamente.
Os valores referentes a cada código de aglutinação serão apresentados na coluna ‘Saldo’ e devem ser calculados exatamente como já é feito na geração do registro J100 do SPED Contábil, pois, esse relatório deve refletir os valores gerados no arquivo da ECD. Quando o saldo de um determinado código de aglutinação resultar em um débito, o valor desse código deve aparecer entre parênteses no relatório.
Quando o usuário tiver selecionado um código de aglutinação específico na tela de geração o processamento acima deve ser feito apenas para aquele código de aglutinação.	OS2328-R3		RN250	Quando for selecionada a opção ‘Analítico’ e não tiver sido selecionado nenhum código de aglutinação específico na tela de geração, o item ‘Balanço Patrimonial’ deverá apresentar para cada código gerado conforme a RN249, todas as contas e centros de custo (se for o caso) que fazem parte do valor desse código (o código da conta e do centro de custo devem aparecer entre parênteses para diferenciar as contas/centros de custo dos códigos de aglutinação existentes no relatório), onde cada conta e centro de custo deverá apresentar sua porção do valor total do saldo daquele código de aglutinação. Quando o saldo de uma determinada conta/centro de custo resultar em um débito, o valor dessa conta/centro de custo deve aparecer entre parênteses no relatório.
Na geração do relatório analítico a coluna ‘Cód. Aglutinação – Descrição’ deverá se chamar ‘Cód. Aglutinação – Descrição (Cód. Conta – Cód Centro de Custo)’.
O registro J100 da ECD não demonstra os valores dos saldos das contas/centros de custo aglutinadas em cada código, sendo assim, deverá ser implementada uma rotina para recuperação dessa informação para que ela possa ser apresentada no relatório.
Quando o usuário tiver selecionado um código de aglutinação específico na tela de geração o processamento acima deve ser feito apenas para aquele código de aglutinação.	OS2328-R3		RN251	Quando for selecionada a opção ‘Sintético’ e não tiver sido selecionado nenhum código de aglutinação específico na tela de geração, o item ‘Demonstração de Resultado’ deve listar todos os códigos de aglutinação da Demonstração de Resultado do Exercício parametrizados no menu: Códigos de Aglutinação (B. Patrimonial/DRE) do módulo SPED Contábil para aquele estabelecimento que possuam valor. Os códigos serão apresentados na coluna ‘Cód. Aglutinação - Descrição’ e essa coluna deverá conter o código de aglutinação seguido de sua descrição.
A ordem em que os códigos aparecem no relatório deverá ser exatamente a mesma ordem parametrizada no menu anteriormente citado.
Os códigos de aglutinação deverão estar corretamente identados de acordo com o nível em que o código foi criado, por exemplo: O código de nível 1 deverá aparecer na margem esquerda do relatório, o código de nível 2 estará um ‘tab’ a frente do código de nível 1, e assim sucessivamente.
Os valores referentes a cada código de aglutinação serão apresentados na coluna ‘Saldo’ e devem ser calculados exatamente como já é feito na geração do registro J150 do SPED Contábil, pois, esse relatório deve refletir os valores gerados no arquivo da ECD. Quando o saldo de um determinado código de aglutinação resultar em um débito, o valor desse código deve aparecer entre parênteses no relatório.
Quando o usuário tiver selecionado um código de aglutinação específico na tela de geração o processamento acima deve ser feito apenas para aquele código de aglutinação.	OS2328-R3		RN252	Quando for selecionada a opção ‘Analítico’ na tela de geração, o item ‘Demonstração de Resultado’ deverá apresentar para cada código gerado conforme a RN251, todas as contas e centros de custo (se for o caso) que fazem parte do valor desse código (o código da conta e do centro de custo devem aparecer entre parênteses para diferenciar as contas/centros de custo dos códigos de aglutinação existentes no relatório), onde cada conta e centro de custo deverá apresentar sua porção do valor total do saldo daquele código de aglutinação. Quando o saldo de uma determinada conta/centro de custo resultar em um débito, o valor dessa conta/centro de custo deve aparecer entre parênteses no relatório.
O registro J150 da ECD não demonstra os valores dos saldos das contas/centros de custo aglutinadas em cada código, sendo assim, deverá ser implementada uma rotina para recuperação dessa informação para que ela possa ser apresentada no relatório.
Na geração do relatório analítico a coluna ‘Cód. Aglutinação – Descrição’ deverá se chamar ‘Cód. Aglutinação – Descrição (Cód. Conta – Cód Centro de Custo)’.
Quando o usuário tiver selecionado um código de aglutinação específico na tela de geração o processamento acima deve ser feito apenas para aquele código de aglutinação.	OS2388-R3		RN253	Ao gerar o registro J005 o sistema deverá verificar se a data final de geração for igual a 31/12/XXXX, e a data inicial for 01/12/XXXX, então no registro J005 deverá ser gerado como data inicial e data final  o ano todo, ou seja, a Data inicial do registro J005 será 01/01/XXXX, e a data final será 31/12/XXXX..	2328-N2		RN254	No caso de não cair na situação acima, então o sistema deverá gerar a data incial e final do registro J005 com a mesma data do registro 0000, pois caso o cliente gere o arquivo trimestral, o registro J005 será gerado também desta forma, assim atendendo ao que exige a legislação	2328-N2		RN255	A tela para parametrização do número de ordem será denominada ‘Número de Ordem’ e deverá conter:

- O campo Estabelecimento que será um combo onde estarão disponíveis para seleção os estabelecimentos centralizadores (parametrização feita no módulo Parâmetros > Centralização da Escrituração Contábil), os estabelecimentos que não são centralizadores e que não foram centralizados em nenhum outro estabelecimento, e ainda a opção ‘Todos’. Só devem ser apresentados para seleção os estabelecimentos que o usuário que está usando a aplicação tem acesso (ver parametrização no powerlock para esse usuário);
- O campo ‘Livro’ (ver campo Livro da tela de geração da ECD) que será um combo onde estarão disponíveis para seleção os tipos de livro previstos atualmente para a ECD (G, R, B, A e Z).
- O campo ‘Ano’ que será um textbox para informação do ano a que se refere aquela parametrização.
- O campo período que deverá conter dois textbox com máscara de data (dia e mês) para informação do dia/mês inicial e do dia/mês final para parametrização do número de ordem;
- O campo ‘Nº de Ordem’ que será um textbox para informação do número de ordem referente àquele período.

Obs.: Ao clicar no botão ‘Novo’ na barra de ferramentas devem ser incluídos na tela mais um campo ‘Período’ e um campo ‘Nº de Ordem’ para que o usuário possa parametrizar diversos períodos na mesma tela. Os demais campos da tela serão apresentados apenas uma vez, no topo da tela.	OS2848		RN256	Quando o usuário estiver gerando o arquivo do livro ‘A’ ou ‘Z’, o campo ‘Número de Ordem do Instrumento Associado’ (Campo 02) do registro I012 deve ser recuperado da seguinte forma:

- Da parametrização feita no controle da obrigação, deve-se recuperar o livro principal associado ao livro tipo ‘A’ ou ‘Z’ que está sendo gerado;
- Na parametrização do número de ordem (Parâmetros > Número de Ordem), deve-se selecionar o número de ordem correspondente àquela empresa, estabelecimento, tipo de livro (recuperado no passo acima) e período.
- Esse número de ordem será gerado no campo 02 do registro I012.

Obs.: Quando não existir parametrização de número de ordem para o livro principal recuperado no passo 1, deve ser emitida mensagem no log indicando que o campo ‘Número de Ordem do Instrumento Associado’ não será gerado no registro I012 para aquele livro principal, pois não foi encontrada parametrização de número de ordem em Parâmetros > Número de Ordem. Sugestão de mensagem:

Tipo I012 – Campo ‘NUM_ORD’ não será gerado, pois, não foi encontrada parametrização do Nº de Ordem para essa Empresa/Estabelecimento/Tipo de Livro/Período. Favor informar o Número de Ordem do Instrumento Associado (Livro Principal – (Colocar aqui o código e a descrição do livro principal)).
Localização: SPED --> ECD Escrituração Contábil Digital --> Parâmetros --> Número de Ordem	OS2848		RN257	Quando o usuário estiver gerando o arquivo do livro ‘R’ ou ‘B’, o campo ‘Número de Ordem do Instrumento Associado’ (campo 02) do registro I012 deve ser recuperado da seguinte forma:

- Da parametrização feita no controle da obrigação, deve-se recuperar o(s) livro(s) auxiliar(es) associado(s) ao livro tipo ‘R’ ou ‘B’ que está sendo gerado;
- Na parametrização do número de ordem (Parâmetros > Número de Ordem), deve-se selecionar o número de ordem correspondente àquela empresa, estabelecimento, tipo de livro (recuperado no passo acima) e período. Caso exista mais de um livro auxiliar associado ao livro principal que está sendo gerado, esse passo será executado para cada livro auxiliar recuperado no passo acima.
- Esse número de ordem será gerado no campo 02 do registro I012. Caso exista mais de um livro auxiliar associado ao livro principal que está sendo gerado, cada número de ordem recuperado no passo acima será preenchido no seu respectivo registro I012.

Obs.: Quando não existir parametrização de número de ordem para algum livro auxiliar recuperado no passo 1, deve ser emitida mensagem no log indicando que o campo ‘Número de Ordem do Instrumento Associado’ não será gerado no registro I012 para aquele livro auxiliar, pois não foi encontrada parametrização de número de ordem em Parâmetros > Número de Ordem. Sugestão de mensagem:

Tipo I012 – Campo ‘NUM_ORD’ não será gerado, pois, não foi encontrada parametrização do Nº de Ordem para essa Empresa/Estabelecimento/Tipo de Livro/Período. Favor informar o Número de Ordem do Instrumento Associado (Livro Auxiliar (Colocar aqui o código e a descrição do livro auxiliar)).
Localização: SPED --> ECD Escrituração Contábil Digital --> Parâmetros --> Número de Ordem	OS2848		RN258	O número de ordem a ser gerado no campo 03 do registro I030 e no campo 03 do registro J900 deve ser recuperado da seguinte forma:

- Da parametrização do número de ordem (Parâmetros > Número de Ordem) deve ser recuperado o número de ordem correspondente àquela empresa, estabelecimento, tipo de livro, e período (todos esses parâmetros são os informados na tela de geração);
- Esse número de ordem será gerado no campo 03 do registro I030 e no campo 03 do registro J900.

Quando não existir parametrização de número de ordem para os parâmetros citados acima, deve ser emitida mensagem no log indicando que o campo ‘Número de Ordem do Instrumento de Escrituração’ não será gerado nos registros I030 e J900, pois não foi encontrada parametrização de número de ordem em Parâmetros > Número de Ordem. Sugestão de mensagem:

Tipo I030/J900– Campo ‘NUM_ORD’ não será gerado, pois, não foi encontrada parametrização do Nº de Ordem para essa Empresa/Estabelecimento/Tipo de Livro/Período. Favor informar o Número de Ordem do Instrumento de Escrituração do Livro (Colocar aqui o código e a descrição do que está sendo gerado)).
Localização: SPED --> ECD Escrituração Contábil Digital --> Parâmetros --> Número de Ordem

Obs.: Essa regra vale para todos os tipos de livros (A, B, G, R e Z).	OS2848		RN259	Ao gerar os registros J100 e J150 do SPED Contábil, o sistema deverá considerar as contas que se encontram devidamente parametrizadas para geração do registro J100 e J150 com base nas regras já existentes, para aquelas que tiverem a parametrização, porém, não saldo no período, o sistema deverá apontar no log, porém as demais contas que tiverem valores e parametrização, deverão gerar os registros normalmente, não sendo um impeditivo as contas que não tiverem valores a ser gerado.	CH77588		RN260	Deve ser adicionada a coluna ‘Num CRC’ na janela de seleção do responsável legal existente na aba signatários do menu ‘Dados Iniciais’.
Essa coluna será adicionada após a coluna ‘Num CPF’ e deve apresentar a informação do número do CRC do respectivo cadastro.	CH62988-A		RN261	Apresentar, na tela de Manutenção de Plano de contas Referencial, os dados referentes ao SUSEP (Entidade = 00), conforme dados na TFIX64, que deverá ser importada pelo cliente, via módulo Ferramentas.	CH71180		RN262	Criação do parâmetro “Consistir Saldos x Lançamentos” na tela de geração:

Para geração dos dados do estabelecimento centralizador 01, deverá considerar dados dele e de seus centralizados, ou seja, dados do estabelecimento 01 e 02;

Para geração dos dados do estabelecimento centralizador 03, deverá considerar dados dele e de seus centralizados, ou seja, dados do estabelecimento 03 e 04;

Para geração dos dados do estabelecimento Descentralizado 09, deverá considerar apenas dados do próprio estabelecimento.	2328-D		RN263	No caso dos valores a serem gerados quando se tratar de centralização, deverá ser feito um somatório dos valores dos estabelecimentos centralizados + centralizador, lembrando que débitos somente somam-se com débitos e créditos somente com créditos. A soma de um saldo devedor mais um credor, na verdade deve ser a diferença entre eles, resultando em D ou C conforme o maior valor.	2328-D		RN264	A consistência se dará pelo preenchimento da tela de geração conforme Perfil e por:
Conta contábil;
Conta contábil + centro de custo (caso o mesmo tenha movimentação e saldos por centro de custo);

Consistir valor total de lançamentos versus total de saldos no período, caso contrário exibir a seguinte mensagem “Saldo Final (SAFX02) não confere com o Saldo Final apurado conforme Saldo Inicial (SAFX02) e lançamentos (SAFX01). 
Exemplo:
Mês/Ano – Grupo – Cód. Conta: 01/2006- GRPXX - Contaxyz
Saldo Inicial:
Total de lançamentos a Crédito (SAFX01): 10.000,00
Total de lançamentos a Débito  (SAFX01): 11.000,00
Saldo Final (SAFX02): 0,00 D
Saldo Final Apurado: 1.000,00 D”	2328-D		RN265	Consistir a existência de número de lançamento no cadastro de lançamentos contábeis, caso não esteja preenchido, emitir a seguinte mensagem: 

“Tipo I200/I250/I300/I310/I350/I355 - Lançamento Contábil será desconsiderado na geração dos registros, pois o número do lançamento não está preenchido.
Estab - Data Lancto - Cod. Conta - Arquiv. = XXX - DD/MM/AAAA - YYYY - ZZZZ
Módulo Básicos -> MastersafDW ’! Manutenção ’! Contabilidade ’! Diário Auxiliar ou Diário Geral  ’!  Lançamento Contábil por Estabelecimento 	2328-D		RN266	Ao gerar registro I250 Partidas do Lançamento, consistir se no mesmo N° de lançamento a soma dos valores de débito e total de crédito são iguais, caso contrário exibir a seguinte mensagem: 
“Tipo I250(Partidas do Lançamento) – Divergência entre valores Total de Débito x Total de Crédito para o numero de lançamento. Favor verificar lançamentos No 1957 – data  10/10/2006”. 	2328-D		RN267	Quando o flag “Consistir Saldos x Lançamentos” estiver marcado na tela de geração, o sistema deverá continuar fazendo as consistências de saldo final, conforme as regras RN262 a RN266.

Além disso, deverão ser cruzados os valores intermediários de crédito e débito, conforme regras abaixo:

I355
Campo 04 ’! saldo final
	        Bater com I155 campo 08

I310
Campo 04 ’! total débitos/dia
	        " = campo 06 registro I155

Campo 05 ’! total créditos/dia
	        " = campo 07 registro I155

I250
Campo 04 ’! quando campo 05 = D
	        Bater com I155 campo 06
Campo 04 ’! quando campo 05 = C
	        Bater com I155 campo 07

Resumindo:

I250(04-D) = I155(06) = I310(04)
I250(04-C) = I155(07) = I310(05)


Observações:

Livro G ’! Gera o I155, I250 e I355
Livro R ’! Gera o I155, I250 e I355
Livro A ’! Gera o I155, I250
Livro B ’! Gera o I155, I310 e I355
Livro Z ’! Gera o I155

Portanto, para aplicar as regras acima no log, se atentar para os cálculos de cada livro.
	CH71579-A		RN268	Parâmetro Controle da Obrigação

Nome do Módulo: SPED – ECD – Escrituração Contábil Digital
Caminho no menu: Parâmetros –> Controle da Obrigação

Alterar a regra de exclusão dos registros no Histórico dos Livros Gerados, quando o usuário clicar no botão EXCLUIR, apenas as gerações selecionadas deverão ser eliminadas.

Primeiramente o usuário deverá selecionar o registro a ser excluído, ao clicar no registro do indicador do lado esquerdo da tela, a linha inteira deverá ser destacada na cor “azul”ou simplesmente clicando no botão “Selecionar Todos. Em seguida, ao clicar no Botão Excluir ou Excluir Histórico, surgirá a mensagem de alerta, se o usuário confirmar a exclusão, somente a linha selecionada ou todos, serão apagados do Histórico.

Mensagem de Alerta: Mante
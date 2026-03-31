# Matriz_FCONT

- **Fonte:** Matriz_FCONT.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 167 KB

---

ECD \- II Fase FCONT \(Matriz\)

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS2328\-RTT\-1

ECD – II Fase FCONT \(Matriz\) 

Devido alterações ocorridas através da Lei 11\.638/07 na Lei 6\.404,76 os contribuintes puderam optar por apresentar seus Balanços conforme as normas e padrões internacionais IFRS\. Porém, essas alterações, afetaram o valor de alguns tributos tais como PIS, COFINS, CSLL e IR, pois as alterações alteram o reconhecimento de contas de resultado\. Sendo assim, o Governo Brasileiro, dentro de suas possibilidades, exigiu através da Lei 11\.941/09 que as empresas que optassem por apresentarem seus balanços alterados conforme 11\.638/07 deveriam efetuar ajustes para que os valores dos tributos fossem pagos conforme Lei 6\.404/76, sendo assim, as empresas deveriam fazer essa opção através da DIPJ, efetuar os ajustes conforme RTT \(Regime Tributário de Transição\) instituído pelo Lei 11\.941/09, e manter um controle desses ajustes através do FCONT conforme IN949\. As informações contidas no FCONT seriam somente referente às contas que sofreram ajustes de adição exclusão para atendimento a legislação tributária\.

Conforme exposto acima as empras que optaram pelo RTT e empresas sujeitas cumulativamente ao Lucro Real, deverão entregar o arquivo magnético do FCONT, para isso o objetivo dessa OS é desenvolver um módulo que trate da nova obrigação e atenda as exigências cabíveis\.

OS2328\-RTT\-2

Arquivo Magnético

Atualmente a Mastersaf gera o Livro do FCONT importando dados do arquivo gerado da ECD, essa OS deverá atualizar o sistema fazendo com que o mesmo gere os dados a partir das safxs existentes na base de dados do mastersaf\.

CH85314

Arquivo Magnético

Permitir geração de período diferente de anual, quando há situação especial\.

OS2328\-RTT\-5

Arquivo Magnético

Alterações no escopo do Controle Fiscal Contábil de Transição – FCONT, instituido pela Instrução Normativa nº 941,de 16 de junho de 2009 em atendimento as disposíções da Lei nº 11\.941, de 27 de maio de 2009 que instituiu o Regime Tributário de Transição – RTT, na apuração do lucro real, relativamente aos ajustes tributários decorrentes dos novos métodos e critérios contábeis introduzidos pela Lei nº 11\.638, de 28 de dezembro de 2007, que promoveu alterações na Lei nº 6\.404/76\.

No FCONT atual são demonstrados apenas os valores líquido dos ajustes,  segundo a proposta de alteração, os novos registros demonstrarão o valor integral base dos lançamentos que suportam os ajustes, com  detalhamento\.

OS2328\-RTT\-5B

Arquivo Magnético

Inclusão da geração dos registros I156,I256,I356

OS2328\-RTT\-5A

Arquivo Magnético

Geração automática dos lançamentos do tipo Encerramento Fiscal\.

CH118345\-A

Arquivo Magnético

Deve ser alterado as regras 163, 168, 171 e 176 de geração dos lançamentos automáticos EF, onde não havia sido previsto a situação de reversão e estorno dos lançamentos e casos onde há centro de custo vinculado a conta, sendo assim deve ser alterado as regras acima, para contemplar os casos descritos

CH118257

Arquivo Magnético

Alteração na regra 54 \(geração dos registros I050\) deve ser criado filtro nos casos onde existe a mesma conta contábil na SAFX2002 em diversos grupos para a mesma empresa

CH118158

Arquivo Magnético

Alteração do registro 0000 campo 11 \- IND\_SIT\_ESP

CH119128

Arquivo Magnético

Incluir a regra de negócio que será considerada na geração do Meio Magnético do FCONT, com relação ao parâmetro “Omitir informação Centro de Custo em lançamentos Contábeis e Saldos” em Dados Iniciais\.

OS 2328\-RTT5\-C

Arquivo Magnético

Alteração no processo de geração do Meio Magnético, para as empresas que tiveram  alguma situação especial durante o ano de 2010\.

CH120094

Arquivo Magnético

Alterar a rotina de geração do FCONT para exibir um registro I050 para cada conta contábil \(inclusive para cada alteração de conta, quando existir\)\.

CH11942

Arquivo Magnético

Alterar a rotina de geração do FCONT geração do registro I050 e I051 igualmente ao ECD\-Contábil\.

OS3658

Arquivo Magnético

Alteração no processo de geração dos lançamentos de encerramento automático\.

CH16906\_2012

Arquivo Magnético

Alterar a rotina de geração do FCONT, para considerar nos registros I100 todas as alterações dos centros de custo que estão vigentes no período da geração do arquivo magnético\.

CH119845\_2011

Arquivo Magnético

O objetivo deste chamado é complementar uma situação não prevista no cálculo do EF quando o Lançamento Fiscal \(crédito/debito\) é maior que o lançamento de Expurgo \(crédito/debito\) 

CH15576\_2012

Arquivo Magnético

A rotina da geração do FCONT deve considerar as informações do De\-Para,compatível com o período da geração do arquivo magnético\.

OS3678	

Arquivo Magnético

Alterar a forma de geração dos lançamentos de encerramento quando o período de apuração adotado pelo cliente for Trimestral\.

CH17253\_2012

Arquivo Magnético

Considerar todos os grupos utilizados pelo estabelecimento durante o período de geração do meio magnético do FCONT\.

OS3689

Arquivo Magnético

O objetivo deste chamado é permitir a geração dos registros I050 \(conta contábil\) e I100\(centro de custo\), que tiveram movimentação durante o período da geração do FCONT, no arquivo magnético\.

CH11295/2013

Arquivo Magnético

Ajuste na regra dos registros I350 e I355 para atender ao setor financeiro\.

OS4084

Arquivo Magnético

Alterar a forma de recuperação e geração dos Lançamentos EF, criados pelo processo automático, dentro do Módulo SPED FCONT\- Controle Fiscal Contábil de Transição\. 

Esta alteração só é necessária, para as empresas que tiveram alguma situação especial durante o período\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Será criado um novo módulo no mastersaf dentro do grupo SPED, chamado “FCONT”\. 

__OS2328\-RTT\-1__

__RN01__

Na abertura do novo módulo criado, deverá ser apresentada a tela padrão mastersaf exatamente como se vê na demonstração de visualização do item 2\.1\.1\.1\.1 FCONT do documento de requisitos\.

__OS2328\-RTT\-1__

__RN02__

A nova tela possuirá a seguinte estrutura de menus e submenus\.

__Arquivo:__

\(Submenu Padrão mastersaf\)

__Parâmetros:__

Perfil Layout – FCONT

Dados Iniciais

Critérios de Importação

		Recuperação do Lucro Contábil

__Importação ECD__

__Manutenção: __

Lançamentos Contábeis e/ou Fiscais

Lucro Contábil \(11\.638/07\)

Plano de Contas Referencial X Plano de contas empresa\.

__Geração:__

     Meio Magnético

__Relatórios:__

	Balancete de Resultado FCONT

	Demonstrativo de Apuração

__OS2328\-RTT\-1__

__RN03__

Na abertura do submenu “Perfil FCONT”, será apresentado a tela conforme demonstração no item 2\.1\.1\.1\.2 do documento de requisitos\.

Os registros que nas regras abaixo forem indicados como obrigatórios deverão por default estar marcados e desabilitados para alteração\. Os registros que forem facultativos deverão estar abertos para que os usuários possam marcar conforme desejarem efetuar a entrega ao fisco\.

__OS2328\-RTT\-1__

__RN04__

A tela estará dividida da seguinte forma:

Campo: “Leiaute”: Neste campo constará a seguinte informação “Controle Fiscal Contábil de Transição”, esta informação será fixa, não podendo ser manipulada\.

Campo: Perfil: Neste campo existirá a opção do campo “Código do Perfil” e “Descrição do Perfil” assim o usuário poderá criar quantos perfis desejar\.

Caixa chamada “Definição de Blocos”: neste serão apresentados os blocos conforme leiaute abaixo:

0   \- Abertura, Identificação e Referências\.

I   \- Lançamentos Contábeis \(Lançamentos Contábeis \(Lcts\. a expurgar e a incluir\)

J   \- Identificação dos Signatários da escrituração

M – Informações Fiscais \(Em forma Contábil a serem incluídos\)

9  \- Controle e Encerramento do Arquivo Digital

__OS2328\-RTT\-1__

__RN05__

Caixa chamada “Definição dos Registros”:

Esta será composta de três informações:

Tipo do registro,

Nível e a

Descrição do registro

__OS2328\-RTT\-1__

__RN06__

Quando o usuário clicar em cima do bloco 0 – Abertura, Identificação e Referencias, será apresentada ao lado direito da tela dentro da caixa “Definição dos Registros” a seguinte informação:

Tipo: 0000  Nível: 0  Descrição: Abertura do Arquivo Digital e Identificação da Entidade\.

OBS: Este registro é Obrigatório\.

__OS2328\-RTT\-1__

__RN07__

Quando o usuário clicar em cima do bloco I – Lançamentos Contábeis será apresentada ao lado direito da tela dentro da caixa “Definição dos Registros” a seguinte informação:

Tipo: I001 Nível: 1 Descrição: Abertura do Bloco I

Tipo: I050 Nível: 2 Descrição: Plano de Contas Contábil

Tipo: I051 Nível: 3 Descrição: Plano de Contas Referencial

Tipo: I075 Nível: 2 Descrição: Tabela de Histórico Padronizado

Tipo: I100 Nível: 2 Descrição: Centro de Custos

Tipo: I150 Nível: 2 Descrição: Saldos Contábeis – Identificação do Período

Tipo: I155 Nível: 3 Descrição: Detalhes dos Saldos Contábeis

Tipo: I200 Nível: 2 Descrição: Lançamentos

Tipo: I250 Nível: 3 Descrição: Partidas dos Lançamentos

Tipo: I990 Nível: 1 Descrição: Encerramento do Bloco I

__OS2328\-RTT\-1__

__RN08__

Quando o usuário clicar em cima do bloco J \- Identificação dos Signatários será apresentada ao lado direito da tela dentro da caixa “Definição dos Registros” a seguinte informação:

Tipo: J001 Nível: 1 Descrição: Abertura do Bloco J

Tipo: J930 Nível: 2 Descrição: Identificação dos Signatários do FCONT

Tipo: J990 Nível: 1 Descrição: Encerramento do Bloco J

__OS2328\-RTT\-1__

__RN09__

Quando o usuário clicar em cima do bloco M \- Lançamentos Fiscais será apresentada ao lado direito da tela dentro da caixa “Definição dos Registros” a seguinte informação:

Tipo: M001 Nível: 1 Descrição: Abertura do Bloco M

Tipo: M020 Nível: 2 Descrição: Qualificação da Pessoa Jurídica

Tipo: M030 Nível: 2 Descrição: Identificação do Período de Apuração

Tipo: M990 Nível: 1 Descrição: Encerramento do Bloco M

__OS2328\-RTT\-1__

__RN10__

Quando o usuário clicar em cima do bloco 9 \- Controle e Encerramento do Arquivo Digital será apresentada ao lado direito da tela dentro da caixa “Definição dos Registros” a seguinte informação:

Tipo: 9001 Nível: 1 Descrição: Abertura do Bloco 9

Tipo: 9900 Nível: 2 Descrição: Registros do Arquivo

Tipo: 9990 Nível: 1 Descrição: Encerramento do Bloco 9

Tipo: 9999 Nível: 0 Descrição: Encerramento do Arquivo Digital

__OS2328\-RTT\-1__

__RN11__

Quando o usuário acessar o caminho FCONT> Menu: Parâmetros > Dados Iniciais será apresentado a ele, a mesma tela de Dados iniciais disponível na ECD\. Conforme pode ser visualizado no documento de requisitos item 2\.1\.1\.1\.3 Dados Iniciais\.

Esta tela será como um atalho da ECD, se o usuário alterar um parâmetro no FCONT na ECD a tela de Dados Iniciais será alterada também\.

__OS2328\-RTT\-1__

__RN12__

Nesta tela estão disponíveis na ECD 3 guias, uma referente aos Dados Iniciais, outra referente ao signatários e outra referente as Demonstrações contábeis\.

A única aba atalho da ECD será a de “Dados Iniciais”, a Tela de Signatários deverá ser idêntica, porém os signatários cadastrados na ECD podem não ser os mesmos do FCONT, por esse motivo, o usuário precisará cadastrar os responsáveis legais duas vezes caso seja o mesmo a assinar as duas obrigações, uma vez ele cadastra no SPED ECD e outra vez no SPED FCONT\.

A tela de Demonstrações contábeis não estará disponível para visualização no FCONT pois, neste não será entregue nenhuma demonstração contábil\.

__OS2328\-RTT\-1__

__RN12\. 1__

No campo “Entidade Responsável” da tela de dados iniciais atualmente é apresentada somente duas opções, para seleção que são: Receita Federal e Banco Central, agora deverá ser incluída a seguinte opção: Sociedade Seguradora, de Capitalização ou Entidade aberta de previdência complementar \- SUSEP\.

Logo, na dropdown referente a Entidade Responsável estarão disponíveis as seguinte opções:

Receita Federal: Quando \(na ECD ou FCONT\) o usuário selecionar e confirmar esta, o plano referencial apresentado para o De/Para é o da Receita Federal\.

Banco Central: Quando \(na ECD ou FCONT\) o usuário selecionar e confirmar esta, o plano referencial apresentado para o De/Para é o do COSIF\.

SUSEP: Quando \(na ECD ou FCONT\) o usuário selecionar e confirmar esta, não será apresentado plano referencial na tela de Plano de contas Empresa x Plano de contas referencial, pois para este não se faz o De/Para\.

Obs: \(foi aberto o chamado 71180 para solicitar inclusão do Plano SUSEP na TFIX64, porém isso será tratado através de uma nova OS da ECD\)\.

__OS2328\-RTT\-1__

__RN13__

Existe a OS2328\-R4 que fará uma melhoria na apresentação dos signatários como essa tela é a mesma utilizada para o FCONT essa alteração deverá também atingir o FCONT\.

__OS2328\-RTT\-1__

__RN14__

Na abertura do submenu “Critérios de importação > por Conta” será apresentada a tela conforme demonstração no item 2\.1\.1\.1\.4 do documento de requisitos e terá o objetivo de identificar quais contas que sofreram ajustes conforme prevê a legislação\.

A tela será composta de duas caixas, uma chamará “Contas da empresa a selecionar” e apresentará a \(SAFX2002 – Plano de contas\)\.

A outra caixa será chamada de “Replicar para os Estabelecimentos” virá default vazia, conforme padrão MSAF\.

__OS2328\-RTT\-1__

__RN15__

Nesta tela haverá dois meios disponíveis de pesquisa das contas, por código da conta e pela descrição\.

O campo para pesquisa será chamado de “Informar Conta/Descrição para Pesquisa:”, na frente desse campo deverá possuir um espaço disponibilizado para a menção da conta contábil e em seguida deverá estar disponível as características de pesquisa, um campo em forma de check box por Código da Conta “Cód\. Conta” e outro check box pela descrição da conta “Descrição”\.

__OS2328\-RTT\-1__

__RN16__

Quando o usuário informar o código da conta ou sua descrição, escolhendo um dos métodos de pesquisa e clicar no botão pesquisar, que deverá estar localizado ao lado direito das opções de busca, a tela apresentará somente a conta desejada\. Caso o usuário opte pela descrição, se este colocar uma determinada palavra e clicar no botão pesquisar, o sistema deverá trazer todas as contas cuja aquela palavra é citada, não importando se esta localizada no início ou meio da descrição\.

__OS2328\-RTT\-1__

__RN17__

Para seleção das contas o usuário deverá marcar os check Box existente na frente das respectivas contas, e acionar o botão confirmar\.

Para que o usuário exclua a seleção feita de uma determinada conta, o mesmo deverá retirar o flegue da conta da empresa selecionada e acionar o botão confirmar disponível na barra de ferramentas\. Quando isso acontecer o sistema deverá apresentar a seguinte mensagem “Confirma a exclusão da\(s\) Conta\(s\) da Empresa?”\. Se o usuário acionar o botão “SIM” o sistema exclui a parametrização somente da conta que fora desmarcada, se o usuário acionar o botão “Não” o sistema mantém a parametrização que esta efetuada\.

__OS2328\-RTT\-1__

__RN18__

Na abertura do submenu “Critérios de importação > por número de lançamento” será apresentada a tela conforme demonstração no item 2\.1\.1\.1\.5 do documento de requisitos e terá o objetivo de identificar quais contas que sofreram ajustes conforme prevê a legislação para o FCONT, filtrando – as por número de lançamento\.

A tela será composta de duas caixas, uma será dividida em 3 colunas \(número de lançamento, Arquivamento, e Tipo\), e apresentará o número dos lançamentos do arquivo importado\.

__OS2328\-RTT\-1__

__RN19__

Nesta tela haverá dois meios disponíveis de pesquisa, por Lançamento ou por arquivamento\.

O campo para pesquisa será chamado de “Informar Conta/Descrição para Pesquisa:”, na frente desse campo deverá possuir um espaço disponibilizado para a menção da conta contábil e em seguida deverá estar disponível as características de pesquisa, um campo em forma de check box por Nº Lançamento \(Lançamento\) e outro check box pelo Arquivamento \(Arquivamento\)\.

__OS2328\-RTT\-1__

__RN20__

Quando o usuário informar o Nº Lançamento ou Arquivamento, escolhendo um dos métodos de pesquisa e clicar no botão pesquisar, que deverá estar localizado ao lado direito das opções de busca, a tela apresentará somente a informação desejada\. Se o usuário informar parte do lançamento ou do Arquivamento o sistema deverá trazer para seleção todos os lançamentos ou arquivamentos que contém aquela determinada informação\.

__OS2328\-RTT\-1__

__RN21__

Para seleção do número de lançamento o usuário deverá marcar os check Box existentes na frente dos respectivos, e acionar o botão confirmar\.

Para que o usuário exclua a seleção feita de um determinado nº de lançamento, o mesmo deverá retirar o flegue da destes e acionar o botão confirmar disponível na barra de ferramentas\. Quando isso acontecer o sistema deverá apresentar a seguinte mensagem “Confirma a exclusão do\(s\) Lançamento\(s\) da Empresa?”\. Se o usuário acionar o botão “SIM” o sistema exclui a parametrização somente do Lançamento que fora desmarcado, se o usuário acionar o botão “Não” o sistema mantém a parametrização que esta efetuada\.

__OS2328\-RTT\-1__

__RN22__

Na abertura do submenu “Critérios de importação > Recuperação do Lucro contábil” será apresentada a tela conforme demonstração no item 2\.1\.1\.1\.4 do documento de requisitos e terá o objetivo de levar posteriormente esta informação para a geração do arquivo magnético do FCONT\.

A tela será composta dos seguintes campos:

Estabelecimento: \(Com conceito centralizador/Descentralizado Padrão ECD\)

E uma Caixa chamada “Por Código de Aglutinação/DRE”

__OS2328\-RTT\-1__

__RN23__

Se o usuário marcar a opção “Por Código de Aglutinação/DRE” será aberto uma pasta onde o usuário poderá abrir e lhe será apresentada a DRE montada na ECD através dos códigos de aglutinação\.

Neste o usuário deverá selecionar qual linha da DRE corresponde ao valor do Lucro Contábil, para que posteriormente o sistema leve esse valor para o registro competente\.

Quando o usuário fizer a opção por este meio, a caixa “Por Valor Informado” deverá estar desabilitada ao usuário\.

__OS2328\-RTT\-1__

__RN24__

Se o usuário marcar a opção “Por Valor Informado” será aberto um campo com formato numérico, para que o usuário entre com o valor do lucro contábil manualmente e posteriormente o sistema leve esse valor para o registro competente\.

Quando o usuário fizer a opção por este meio, a caixa “Por Código de Aglutinação/DRE” deverá estar desabilitada ao usuário\.

__OS2328\-RTT\-1__

__RN25__

Na abertura do submenu “Importação ECD”, será apresentada a tela conforme demonstração no item 2\.1\.1\.1\.5 do documento de requisitos\.

Essa tela será semelhante a tela de carga do Job servidor, onde o usuário pode possuir inúmeros arquivos txt na base\. Quando o mesmo informar o diretório para importação do arquivo, o sistema mostrará todos os arquivos txt, e ele fará a seleção de qual deverá ser importado assim como funciona na carga, lembrando que o diretório de importação deve obrigatoriamente ser o do servidor para que o mesmo seja importado com sucesso\.

__OS2328\-RTT\-1__

__Premissas básicas para importação:__

__RN26__

O Caminho indicado para importação deverá ser o do servidor\. Caso contrário o mesmo não será importado com sucesso\.

__OS2328\-RTT\-1__

__RN27__

O Arquivo a ser lido deve corresponder a um arquivo em formato “txt”\. Caso contrário deverá ser criticada a importação, com a seguinte mensagem: \(o arquivo a ser importado não esta no formato esperado \(\*\.txt\)\)\.

__OS2328\-RTT\-1__

__RN28__

O Arquivo lido deverá obrigatoriamente corresponder ao arquivo da ECD entregue ao Fisco em 30/06/09, durante essa importação o sistema deverá verificar se o campo 2 do registro 0000 é igual a “LECD”, se sim, continua as verificações para importação com sucesso, se não, o sistema deverá continuar a leitura porém no final acusar a seguinte mensagem: O arquivo base para geração do FCONT deve ser o arquivo referente a ECD, este arquivo não é uma Escrituração Contábil Digital\.

__OS2328\-RTT\-1__

__RN29__

A data e o Estabelecimento que será levada em conta para importação, deve ser a existente dentro do arquivo da ECD, no campo 03 Data Inicial e campo 04 Data Final das informações contidas no arquivo, no final da importação deverá ser apresentado um relatório contendo as seguintes informações: O Estabelecimento importado, e o Período importado\.

__OS2328\-RTT\-1__

__RN30__

A verificação do estabelecimento deverá ser realizada através do CNPJ que no arquivo encontra\-se no campo 06 do Registro 0000 versus o estab existente nos Dados Iniciais, se diferente mensagem no final da importação\.

__OS2328\-RTT\-1__

__Busca na importação:__

__RN31__

Os registros na ECD são separados por pipe “|”, feito as verificações necessárias acima, deverão ser lidos os seguintes registros:

Registro |0000| de Abertura e Identificação do arquivo

Registro |I001| de Abertura do Bloco I

Registro |I050| do Plano de Contas da Empresa

Registro |I051| do Plano Referencial \(Se houver\)

Registro |I075| de Histórico Padrão \(Se houver\)

Registro |I100| dos Centros de Custo \(Se houver\)

Registro |I150| da Identificação do Período dos Saldos

Registro |I155| dos Detalhes dos Saldos Periódicos

Registro |I200| dos Lançamentos Contábeis \(Se houver\)

Registro |I250| dos Detalhes dos Lançamentos Contábeis \(Se houver\)

Registro |I350| da Identificação da Data dos Saldos antes do Encerramento \(Se houver\)

Registro |I355| Detalhe dos Saldos antes do Encerramento \(Se houver\)

Registro |J001| de Abertura do Bloco J

Registro |J150| da Demonstração de Resultado do Exercício \(Se houver\)\.

__OS2328\-RTT\-1__

__RN32__

Para os registros que não tem o “Se houver” na frente, se durante a leitura do arquivo da ECD não foram encontrados, a importação deverá ser rejeitada e acusada a seguinte mensagem: Para geração do FCONT a premissa é que tenha sido gerado os registros obrigatórios da ECD o registro \(\.\.\.\.\.\.\) não foi encontrado no arquivo e deve ser levado ao FCONT\.

__OS2328\-RTT\-1__

__RN33__

Para essa Verificação o sistema deverá comparar os registros acima exigidos, com o perfil gravado na ECD daquele determinado Estabelecimento\. Os registros obrigatórios que são os que estão fixos no código sem opção de escolha, o sistema procede conforme regra acima, os que estão sujeitos a opção do usuário devem ser importados somente se houver e caso não sejam encontrados deverá deixar passar sem nenhuma crítica\.

__OS2328\-RTT\-1__

__Gravação dos Registros interessantes ao FCONT\.__

Para gravar os registros lidos, o sistema deverá antes verificar as seguintes parametrizações:

__RN34__

O Sistema deverá gravar na tabela os registros identificados na regra acima do jeito que encontra\-los, os únicos que terão regra para gravação são os que seguem abaixo\.

__OS2328\-RTT\-1__

RN34\. 1

Os saldos que são os registros I155 deverão ser lidos e gravados levando em consideração seu registro pai I150, pois é neste que encontra \- se a data dos saldos, sendo que o campo 2 do registro I150 é a data de início do período e o campo 3 do mesmo registro é a data fim do período\.

Deverá ser importado todos os registros I155, mesmo que o usuário importe vários arquivos de períodos diferentes, será gravado na tabela os saldos separando os pelo registro Pai\., dessa forma o sistema terá condições de identificar quais os saldos levar no momento da geração levando em consideração parametrização no momento da geração\.

__OS2328\-RTT\-1__

__RN35__

Se o usuário efetuou a parametrização na tela Parâmetros > Critérios de Importação > Por Conta, o sistema deverá filtrar os registros I250 que tiverem suas contas parametrizadas antes neste caminho e deverá gravar em uma tabela o registro I250 encontrado juntamente com os seus irmãos I250 que estiverem abaixo do mesmo Pai imediatamente superior a eles, juntamente com o registro Pai I200 encontrado\.

__OS2328\-RTT\-1__

__RN36__

Se o usuário efetuou a parametrização na tela Parâmetros > Critérios de Importação > Por Nº de lançamento o sistema deverá filtrar somente os registros I200 que tiverem seus números de lançamentos parametrizados antes neste caminho e deverá gravar na tabela o registro I200 encontrado juntamente com os seus filhos I250 imediatamente inferior a ele\.

__OS2328\-RTT\-1__

__RN37__

Se o usuário efetuou a parametrização na tela Parâmetros > Critérios de Importação > Por Nº de lançamento e Por Conta contábil, o sistema deverá filtrar os registros I200 que tiverem seus números de lançamentos parametrizados antes neste caminho e deverá gravar na tabela o registro I200 encontrado juntamente com os seus filhos I250 imediatamente inferior a ele, ou seja, se encontrar os dois o sistema opta por buscar pelo número de lançamento\.

__OS2328\-RTT\-1__

__RN38__

Se no caminho: Parâmetros > Critérios de Importação > Recuperação Lucro Contábil, o usuário marcar o Check Box referente a \(recuperação automática\) o sistema deverá gravar na tabela a linha correspondente ao código de aglutinação existente na DRE, ou seja, existente no registro J150 do arquivo lido\.

__OS2328\-RTT\-1__

__RN39__

Deveremos recuperar a informação do campo FCONT\_PAR\_IMP\_LUCROC\.cod\_conta\_aglut, filtrando pela empresa/estabelecimento, caso exista registro na tabela, deveremos procurar no arquivo o registro J150 que possua a conta aglutinadora parametrizada, caso o campo esteja nulo, deveremos desconsiderar a importação de qualquer registro J150; Se encontrarmos o J150, deveremos gravar as informações na tabela FCONT\_MAN\_LUCROC as seguintes informações: cod\_empresa, cod\_estab, ano\_calend \(ano do campo 03 do registro J005\), ind\_periodic \(deveremos verificar a seguinte regra: se o mês do campo 03 do registro J005 for \(01,02 ou 03\) gravar T01, se \(04,05 ou 06\) gravar T02, se \(07, 08 ou 09\) gravar T03, se \(10,11\) gravar T04, se \(12\) verificar o período entre os campos ‘02’ e ’03 do registro J005, caso seja maior que 3, gravar A00 senão gravar T04\), vlr\_lucroc com o valor do campo 05 e ind\_lucroc com o valor do campo 06\. 

__OS2328\-RTT\-1__

__RN39\.1__

No arquivo gerado pelo FCONT, o registro I155 não poderá ser gerado com saldo final igual a "0,00", sendo assim, os lançamentos de encerramento deverão ser desconsiderados na importação do arquivo e os seus valores estornados do registro de saldo \(I155\)\. Para isso, o sistema deverá agir da seguinte forma:

Na importação do arquivo gerado pela ECD, o sistema deverá verificar se existe algum registro I200 que possui o valor "E" no campo 05\-IND\_LCTO\. Se existir, deverá se posicionar nos registros I250 associados a esse registro I200\.

No registro I250 associado ao registro I200 com indicador de lançamento de encerramento \(05\-IND\_LCTO = "E"\), o sistema estornará os valores utilizando as seguintes regras:  

Selecionar a conta e o centro de custo \(campo 02\-COD\_CTA \+ campo 03\-COD\_CCUS do registro I250\) e localizar no registro I155 \(campo 02\-COD\_CTA \+ campo 03\-COD\_CCUS do registro I155\)\.

Se o indicador da natureza de lançamento for débito \(campo 05\-IND\_DC = "D" do registro I250\), o sistema deverá selecionar o valor do campo 04\-VL\_DC do mesmo registro \(I255\) e subtrair pelo campo 06\-VL\_DEB do registro I155 e recalcular o saldo final \(campo 08\-VL\_SLD\_FIN do registro I155\)\.

Se o indicador da natureza de lançamento for crédito \(campo 05\-IND\_DC = "C" do registro I250\), o sistema deverá selecionar o valor do campo 04\-VL\_DC do mesmo registro \(I255\) e subtrair pelo campo 07\-VL\_CRED do registro I155 e recalcular o saldo final \(campo 08\-VL\_SLD\_FIN do registro I155\)\.

Exemplo:

Abaixo estão alguns registros do arquivo gerado pela ECD que deverá ser importado pelo FCONT\. Note que o arquivo possui o registro I200 com lançamento de encerramento e deverá estornar o valor do registro I155 referente a conta desse registro\.

|I155|G\.50005\.1|XPTO|250,00|C|250,00|0,00|0,00|D|

|I155|R\.60006\.1||250,00|D|0,00|250,00|0,00|D|

|I200|0004|31012010|250,00|E|

|I250|R\.50005\.1|XPTO|250,00|D|120|R001|Livro R||

|I250|R\.60006\.1||250,00|C|120|R001|Livro R||

Conforme regra especificada acima, na importação desse arquivo o registro I155 deverá ser apresentado da seguinte forma:

|I155|G\.50005\.1|XPTO|250,00|C|0,00|0,00|250,00|C|

|I155|R\.60006\.1||250,00|D|0,00|0,00|250,00|D|

O sistema estornou o valor do campo referente a débito e recalculou o saldo final\.

Importante\!

O registro I200 que possuir o valor "E" no campo 05\-IND\_LCTO não será importado, sendo assim a ação de estorno e composição dos valores do saldo final do registro I155 deverá acontecer no momento da importação\.

__OS2328\-RTT\-1__

__RN39\.2__

Utilizando a regra acima para o livro B:

O livro B não gera os registros I200 e I250, com isso o estorno deverá ser realizado observando o registro I355

 conforme abaixo:

Para cada lançamento de encerramento de contas de resultado, o sistema gera um registro I355\. Se o valor desse lançamento for débito, no registro I355 esse mesmo valor será gerado como crédito e, se o valor do lançamento de encerramento for crédito, o valor do registro I355 será débito\.

Na importação do arquivo gerado pela ECD, o sistema deverá verificar no registro I010 se o campo 02\-IND\_ESC = "B", se sim, verificar se existe registro I355\.

Se existir algum registro I355, o sistema deverá selecionar a conta e o centro de custo \(campo 02\-COD\_CTA \+ campo 03\-COD\_CCUS do registro I355\) e localizar no registro I155 \(campo 02\-COD\_CTA \+ campo 03\-COD\_CCUS do registro I155\)\.

Se o indicador da natureza for crédito \(campo 05\-IND\_DC = "C" do registro I355\), o sistema deverá selecionar o valor do campo 04\-VL\_DC do mesmo registro \(I355\) e subtrair pelo campo 06\-VL\_DEB do registro I155 e recalcular o saldo final \(campo 08\-VL\_SLD\_FIN do registro I155\)\.

Se o indicador da natureza for débito \(campo 05\-IND\_DC = "D" do registro I355\), o sistema deverá selecionar o valor do campo 04\-VL\_DC do mesmo registro \(I355\) e subtrair pelo campo 07\-VL\_CRED do registro I155 e recalcular o saldo final \(campo 08\-VL\_SLD\_FIN do registro I155\)\.

Exemplo:

Abaixo estão alguns registros do arquivo gerado pela ECD que deverá ser importado pelo FCONT\. Note que o arquivo possui o registro I355 e deverá estornar o valor do registro I155 referente a conta desse registro\.

|I010|B|1\.00|

|I155|R\.50005\.1|XPTO|250,00|C|250,00|0,00|0,00|D|

|I155|R\.60006\.1||250,00|D|0,00|250,00|0,00|D|

|I355|R\.50005\.1|XPTO|250,00|C|

|I355|R\.60006\.1||250,00|D|

Conforme regra especificada acima, na importação desse arquivo o registro I155 deverá ser apresentado da seguinte forma:

|I010|B|1\.00|

|I155|R\.50005\.1|XPTO|250,00|C|0,00|0,00|250,00|C|

|I155|R\.60006\.1||250,00|D|0,00|0,00|250,00|D|

O sistema estornou o valor do campo referente a débito e recalculou o saldo final\.

Importante\!

Os registros I355 não serão importados, sendo assim a ação de estorno e composição dos valores do saldo final do registro I155 deverá acontecer no momento da importação\.

__OS2328\-RTT\-1__

__RN39\.3__

Se na leitura das informações quando o sistema fizer a busca pelos Lançamentos de encerramentos, para poder recompor os saldos conforme RN39\.1 e RN39\.2 e não encontrar: 

Conta e o centro de custo \(campo 02\-COD\_CTA \+ campo 03\-COD\_CCUS do registro I355\) e a localização no registro I155 \(campo 02\-COD\_CTA \+ campo 03\-COD\_CCUS do registro I155\)\.

Conta e o centro de custo \(campo 02\-COD\_CTA \+ campo 03\-COD\_CCUS do registro I250\) e a localização no registro I155 \(campo 02\-COD\_CTA \+ campo 03\-COD\_CCUS do registro I155\)\.

Então apresentar a seguinte mensagem:

O arquivo foi importado, porém os saldos referente as contas abaixo não foram recompostos, pois existem lançamentos por centro de custo, sem os saldos por centro de custo correspondentes, ou saldos por centro de custo sem os lançamentos por centro de custo correspondentes\.

Caso este arquivo tenha lançamentos por centro de custo, sem os saldos por centro de custo correspondentes poderá ser importado a SAFX80 com os saldos por centro de custo das contas correspondentes e efetuar novamente a geração da ECD para que o FCONT possa importar e recompor os saldos corretamente

 Caso a situação seja contrária o mastersaf não fará a recomposição dos saldos, sendo assim, favor entrar em contato com o nosso suporte para maiores esclarecimentos\.

__OS2328\-RTT\-1__

__RN40__

Na abertura do submenu “Lançamentos Contábeis e/ou Fiscais”, será apresentado a tela conforme demonstração no item 2\.1\.1\.1\.6 do documento de requisitos\.

Essa tela será criada semelhante a tela apresentada na abertura da SAFX01 no mastersaf, porém ao invés de Lançamentos contábeis a tela deverá apresentar o nome de Lançamentos Contábeis e Fiscais\.

__OS2328\-RTT\-1__

__RN41__

Este tela deverá compor todos os campos existentes hoje na SAFX01, porém esta será criada e alimentada através da nova SAFX129, para que o usuário digite o lançamento manualmente e possa confirmar os dados de forma que estes fiquem gravados no Módulo FCONT\.

__OS2328\-RTT\-1__

__RN42__

A única diferença de tela entre a nova tabela para o FCONT e a SAFX01 é referente ao campo 17 “Tipo de Lançamento” da SAFX01, nesta este campo é apresentado como atendimento a portaria 63, na nova tela/tabela deverá ser apresentado somente como “Tipo de Lançamento” sem a observação de atendimento a portaria 63\.

E na SAFX01, existem as seguintes opções para seleção neste campo: N – Normal e E – Encerramento\.

Na nova tabela estará disponível  as opções N – Normal e F \- Fiscal

__OS2328\-RTT\-1__

__RN42\. 1__

Na abertura do submenu “Lucro/Prejuízo Contábil”, será apresentado a tela conforme demonstração no item 2\.1\.1\.1\.7 do documento de requisitos\.

Essa tela será composta dos seguintes campos:

Estabelecimento: \(conceito de centralizador/descentralizado\)

Exercício: este campo será aberto para digitação do usuário\.

Os campos abaixo serão criados em forma de linha, assim quando o usuário acionar o botão novo da barra de ferramentas uma nova linha será apresentada abaixo da anterior gravada com os campos abertos para manutenção:

Linha: Será apresentado o número no qual corresponde aquela nova linha criada\.

Período de Apuração, este será criado em forma de Drop Down, e deverá vir as seguintes opções de seleção para o usuário: \*Anual, \*Primeiro trimestre, \*Segundo trimestre,  \*Terceiro trimestre e \*Quarto trimestre

Se o usuário parametrizou o lucro de forma automática vindo da DRE, no menu parâmetros esse campo já estará com informação carregada, e ela não poderá ser alterada, se o usuário desejar  modificar a informação aqui carregada, ele deverá excluir a linha inteira, e adicionar uma nova inserindo as informações desejadas\.

Ao lado direito desse campo deverá existir  um com o formato de data que não deverá estar acessível ao usuário\.

O objetivo desses dois campos é trabalharem em conjunto\.

Quando o usuário selecionar a opção “Anual” o campo em formado de data deverá com base no exercício informado preencher o último dia do mês referente a apuração\. Exemplo: Se o usuário parametrizar “Anual”, o campo Data automaticamente apresentará a seguinte informação: 31/12/2008\.

Se o usuário selecionar “Primeiro trimestre” o campo em formato de data ao lado apresentará 31/03/2008 e assim por diante, isso servirá para que o usuário saiba quais serão as datas geradas no arquivo\. 

Lucro Contábil do período: Se o usuário tenha efetuado a parametrização na tela de Recuperação do Lucro Contábil no menu parâmetros>critérios de importação> Recuperação do Lucro contábil” aqui será apresentado o valor do mesmo, recuperado através da importação, se o usuário desejar  modificar a informação aqui carregada, ele deverá excluir a linha inteira, e adicionar uma nova inserindo as informações desejadas\.

Se o usuário desejar cadastrar mais de um registro, é só clicar no botão novo, que estará disponível na barra de ferramentas, assim como se desejar excluir também utilizar o botão “excluir” da barra de ferramentas, efetuado o cadastro somente deve se confirmar os dados que estas informações serão utilizadas para a geração do arquivo magnético\.

__OS2328\-RTT\-1__

__RN43__

Na abertura do submenu “Plano de contas Referencial x Plano de contas Empresa”, será apresentado a mesma tela do De/Para apresentada na ECD, o objetivo dessa é que, quem não fez o \(De/Para\) para a entrega da ECD, deverá fazê\-lo para o FCONT\.

__OS2328\-RTT\-1__

__RN44__

Como esta tela deverá ser um atalho no FCONT, se o usuário efetuar o \(DE/PARA\) para a ECD o mesmo deverá ser replicado para o FCONT\.

__OS2328\-RTT\-1__

__RN45__

Na abertura do submenu “Meio Magnético”, será apresentado a tela conforme demonstração no item 2\.1\.1\.1\.9 do documento de requisitos\.

Essa tela será composta dos seguintes campos:

Data inicial e Data Final: Esse campo servirá para geração da informação que será apresentada no campo 03 e 04 do registro 0000\.

__OS2328\-RTT\-1__

__RN46__

Campo Perfil: Neste o usuário deverá selecionar perfil antes cadastrado e parametrizado para atendimento ao FCONT\. Onde o mesmo poderá ter vários perfis diferentes\.

Campo Tipo de escrituração: Neste campo o usuário deverá informar se a escrituração é Original ou Retificadora, este campo será em forma de dropdown, de forma que o usuário possa selecionar ou um, ou outro\.

Campo Número do Recibo: Neste campo o usuário deverá entrar com o número do recibo da escrituração anterior a ser retificada, por isso ele será um campo aberto para digitação com tamanho 12\. Este campo deverá estar desabilitado quando o campo “Tipo de Escrituração” estiver com a opção “original” e habilitado quando o usuário selecionar a opção “retificadora”\. Este campo deve ser de preenchimento obrigatório quando o campo “tipo de escrituração” estiver com a opção Retificadora selecionada\. 

__OS2328\-RTT\-1__

RN47

Campo em formato check Box chamado “Consistir saldos X Lançamentos”: esse campo servirá para que o usuário possa conferir se a informação que antes foi gerada com sucesso na ECD continua batendo os saldos após a inclusão de novos lançamentos fiscais\.

OS2328\-RTT\-1

__RN48__

Campo em formato check Box chamado “Gerar Plano de contas Referêncial x Plano de contas da empresa com base nos dados importados pelo arquivo da ECD”: esse campo servirá para que o usuário optar por gerar os registros I051 e I050, da parametrização feita em tela do FCONT, ou do arquivo importado da ECD\.

__OS2328\-RTT\-1__

__RN49__

Campo em formato check Box chamado “Gerar somente contas referente a ajustes”: esse campo servirá para que o usuário optar por gerar todas as partidas do lançamento efetuado nos registros I200 e I250 ou somente as que se referirem aos lançamentos ajustes da 11\.638\.

__OS2328\-RTT\-1__

__RN50__

Deverá constar na tela a seguinte mensagem: Obs: Caso a escrituração contábil seja descentralizada, informar no módulo Parâmetros > Preliminares>Centralização Contábil\.

__OS2328\-RTT\-1__

__RN51__

Quando o usuário acionar o botão “Executar” deverá ser gerado os seguintes registros conforme segue:

Registro 0000:

Campo 1: Texto fixo contendo “0000”\.

Campo 2: Texto fixo contendo “LALU”

Campo 3: Campo Data inicial da Tela de geração do meio magnético\.

Campo 4: Campo Data Final da Tela de geração do meio magnético\.

Campo 5: O nome da Empresa deverá ser buscado do campo 09 \(RAZAO\_SOCIAL\) da tabela de Estabelecimento\.

Campo 6: O número do CNPJ deverá ser buscado do campo 05 \(CGC\) da tabela de Estabelecimento\.

Campo 7: A UF da empresa deverá ser buscada do campo 18 \(IDENT\_ESTADO\) da tabela de Estabelecimento\.

Campo 8: A Inscrição Estadual da empresa deverá ser buscado do campo 04 \(INSCRICAO\_ESTADUAL\) da tabela de REGISTRO\_ESTADUAL\.

Campo 9: O código do município da empresa deverá ser buscado do campo 23 \(COD\_MUNICIPIO\) da tabela de Estabelecimento\.

Campo 10: A Inscrição Municipal da Empresa deverá ser buscada do campo 07 \(INSC\_MUNICIPAL\) da tabela de Estabelecimento\.

Campo 11: O Indicador de situação especial deverá ser buscado do campo Campo 45/56/66/67 ou 68 da tabela de Estabelecimento\.

Para esse campo 11 observar o seguinte \(mesma regra da ECD\):

Quando o usuário preencher o campo 45 "Data de Inicio da Atividade" da tabela Estabelecimento, se esta estiver compreendida no mesmo período de geração do meio magnético, o sistema gerará para o arquivo nesse campo a indicação "0" \(0 = Abertura\);

Quando o usuário preencher o campo 66 da tabela de Estabelecimento, se a data de Cisão estiver compreendida no mesmo período de geração do meio magnético, o sistema gerará para o arquivo nesse campo a indicação "1" \(1 = Cisão\);

Quando o usuário preencher o campo 67 da tabela de Estabelecimento, se a data de Fusão estiver compreendida no mesmo período de geração do meio magnético, o sistema gerará para o arquivo nesse campo a indicação "2" \(2 = Fusão\);

Quando o usuário preencher o campo 68 da tabela de Estabelecimento, se a data de Incorporação estiver compreendida no mesmo período de geração do meio 

magnético, o sistema gerará para o arquivo nesse campo a indicação"3"; \(  3  = Incorporação\)

Quando o usuário preencher o campo 56 da tabela de Estabelecimento, se a data de Encerramento estiver compreendida no mesmo período de geração do meio magnético,  o sistema gerará para o arquivo nesse campo a indicação "4" \(4  = Encerramento\);

Caso a data de inicio da atividade não estiver compreendida no período de geração, e os campos referentes a data de cisão, incorporação, fusão ou encerramento

estiver em branco o campo 19 do registro 0000 deverá ficar em branco\.

__OS2328\-RTT\-1__

__RN52__

Registro I001

Campo 1: Texto fixo contendo "I001"\.

Campo 2:  Durante o processo de geração do meio magnético o sistema verificará se existe movimentação no período selecionado, ele preencherá 0 quando existir dados e 1 quando não existir\. \(verificação pode ser feita nos registros I200 e \!250 se eles existirem no FCONT é por que tem movimento\)\.

__OS2328\-RTT\-1__

__RN53__

Registro I050:

Se o usuário marcar o campo “Gerar Plano Referêncial x Plano empresa de arquivo externo” na tela de geração, todos os campos do registro I050 deverão ser levados para o arquivo do FCONT com base nos registros I050 importados do arquivo da ECD em parametrização anterior\.

__OS2328\-RTT\-1__

__RN54__

Registro I050:

Se o usuário não marcar o campo “Gerar Plano Referêncial x Plano empresa de arquivo externo” na tela de geração, todos os campos do registro I050 deverão ser gerados conforme parametrização efetuada na tela de Manutenção > Plano de contas referencial x Plano de Contas empresa conforme segue:

Campo 1: Texto fixo contendo "I050"

Campo 2: Preencher data de inclusão/alteração conforme data de validade do plano de contas  no período\. Observar que cada conta contábil citada nos registros devemos obter o registro no Plano de Contas \(X2002\) que possua a data de validade mais atualizada, limitando\-se à data final do Período informado na geração \(Pois pode ocorrer de existir um registro mais atual, mas posterior ao Período de geração e que, portanto, não diz respeito a esse período\)\.

\(Esse caso só será necessário se o usuário efetuar a parametrização manualmente, pois se o mesmo utilizar a importação da safx2101, esse De/Para já estará pronto\)\.

Campo 3: Esse campo deverá ser buscado da X2002 porém quando levado ao arquivo, considerar para geração do campo do registro em questão o DE\-PARA abaixo especificado: 

 Valor  |Descrição                   |SPED Contábil 

   1      |Ativo                            | 1  

   2      |Compensação             | 5  

   3      |Custo                           | 8  

   4      |Despesa                      | 3  

   5      |Mutações Ativas          | 5  

   6      |Mutações Passivas     | 6   

   7      |Outros                         | 9  

   8      |Passivo                       | 2  

   9      |Patrimônio Líquido      | 7                

  10     |Receita                        | 4 

As descrições apresentadas para os clientes atualmente não são exatamente iguais ao descrito no SPED Contábil porém com a definição do DE\-PARA o resultado será o mesmo\.

Campo 4: informar se é analítica ou sintética, trazer a informação existente no campo 4 \(IND\_CONTA\) da SAFX2002\.

Campo 5: Informa qual o nível da conta, trazer a informação existente no campo 8 da SAFX 2002\.

Campo 6: Informa qual o código da conta, trazer a informação existente no campo 1 \(COD\_CONTA\) da SAFX2002\.

Campo 7: informa qual o código da conta sintética imediatamente superior a conta analítica informada, trazer esta informação do campo 06 \(COD\_CONTA\_SINT\) da SAFX2002\.

Campo 8: Informa o nome da conta analítica informada, trazer a informação do campo 03 \(DESCRICAO\) da SAFX2002\.

__OS2328\-RTT\-1__

__RN54__

__Nos casos onde houver diversos grupos para uma única empresa, pode ocorrer de haver o mesmo plano de contas repetidamente com data da conta igual ou diferente\.__

__Deve ser criado um filtro nesta recuperação devendo verificar se existe os mesmos dados na X2002, gerando apenas um registro I050 respeitando os critérios acima com ênfase na Questão campo 2 \(tratamento do campo data\)__

__OS2328\-RTT\-1__

__CH118257__

__RN55__

Registro I051:

Se o usuário marcar o campo “Gerar Plano Referêncial x Plano empresa de arquivo externo” na tela de geração, todos os campos do registro I051 deverão ser levados para o arquivo do FCONT com base nos registros I051 importados do arquivo da ECD em parametrização anterior\.

__OS2328\-RTT\-1__

__RN56__

Se o usuário não marcar o campo “Gerar Plano Referêncial x Plano empresa de arquivo externo” na tela de geração, todos os campos do registro I051 deverão ser gerados conforme parametrização efetuada na tela de Manutenção > Plano de contas referencial x Plano de Contas empresa conforme segue:

Campo 1: Texto fixo contendo "I051"

Campo 2: Informa qual a Entidade responsável pelo Plano Referencial, esta informação deverá ser trazida do campo 03 \(COD\_ENTIDADE\_RESP\) da tabela SPED\_DADOS\_INI\.

Campo 3: Informa qual o centro de custo, esta deverá ser trazida do campo 06 \(COD\_CUSTO\) da SAFX2101\.

Campo 4: Informa qual a código da conta do plano referencial, esta deverá ser trazida do campo 02 \(COD\_CONTAS\_REF\) da tabela SPED\_CONTAS\_REF\.

__OS2328\-RTT\-1__

__RN57__

Registro I075:

Para geração desse registro o sistema deverá verificar o historio padrão informado na SAFX129, e busca \- lo da SAFX2020, assim como é apresentado no DE/PARA FCONT x MSAF:

Campo 1 é texto fixo I075,

Campo 2 é o código do histórico padrão, cujo campo na tabela SAFX2020 é o 01 \(COD\_HISTPADRAO\)

Campo 3 é a descrição, cujo campo na tabela SAFX2020 é o 03 \(DESCRICAO\)\.

__OS2328\-RTT\-1__

__RN58__

Registro I100:

Para geração desse registro o sistema deverá verificar as informações lançadas na SAFX129, e busca\-las da SAFX2003\.

Campo 1 é texto fixo I100,

Campo 2 é a Data de inclusão do C\.C, cujo campo na tabela SAFX2003 é o 02 \(DATA\_X2003\), lembrando que deve\-se preencher a data de inclusão/alteração conforme data de validade do Centro de Custo  no período\. Observar Centro de Custo citado nos registros, devemos obter o registro no cadastro que possua a data de validade mais atualizada, limitando\-se à data final do Período informado na geração \(Pois pode ocorrer de existir um registro mais atual, mas posterior ao Período de geração e que, portanto, não diz respeito a esse período\)\.

Campo 3 é o Código do centro de custos, cujo campo na tabela SAFX2003 é o 01 \(COD\_CUSTO\)

Campo 4 é o nome do C\.C, cujo campo na tabela SAFX2003 é o 03 \(DESCRICAO\)

__OS2328\-RTT\-1__

__RN59__

Registro I150:

Para geração desse registro o sistema deverá carregar todos os campos do registro I150 importado anteriormente do arquivo da ECD em parametrização anterior\.

__OS2328\-RTT\-1__

__RN60__

Registro I155:

Para geração desses registros o sistema deverá carregar todos os registros desse tipo com seus campos importados anteriormente do arquivo da ECD em parametrização anterior\.

Se o usuário parametrizou o campo “Período de Apuração” da tela de Manutenção > Lucro/Prejuízo contábil, com a informação “Anual” deverá ser gerado nos registros I155 do FCONT os saldos referentes a Dezembro\. Para geração deste o sistema deverá verificar os saldos importados olhando os registro I150 onde o campo 02 e 03 constam às datas iniciais e finais\.

Se o usuário parametrizou, com a informação “Primeiro trimestre” deverá ser gerado nos registros I155 do FCONT os saldos referentes a Março\.

Se o usuário parametrizou com a informação “Segundo trimestre” deverá ser gerado nos registros I155 do FCONT os saldos referentes a junho\.

Se o usuário parametrizou com a informação “Terceiro trimestre” deverá ser gerado nos registros I155 do FCONT os saldos referentes a setembro\.

 

Se o usuário parametrizou com a informação “Quarto trimestre” deverá ser gerado nos registros I155 do FCONT os saldos referentes a dezembro\. 

Se o usuário tiver parametrizado uma ou mais dessas opções \(primeiro trimestre, segundo, terceiro e quarto\) deverão ser trazidos os saldos organizados, pelo seu registro Pai I150, separados pela data, podendo ter dentro do mesmo arquivo 4 registros I150 com os seus I155 correspondestes aquele período\.

Além disso, para gerar estes no FCONT, o sistema deverá trazer os saldos de contas de resultado ou patrimoniais que tenham sido afetadas por lançamentos de encerramentos recompostos no FCONT\. Essa recomposição deve ter sido efetuada já na importação do arquivo conforme RN39\.1 e RN 39\.2, sendo assim, quando verificado o período é só transportar para a geração do FCONT\.

__OS2328\-RTT\-1__

__RN61__

Registro I200 e I250:

Para geração desses registros, o sistema deverá antes fazer as seguintes verificações:

Se o Usuário marcar o check Box chamado “Gerar somente partidas referente a ajustes” antes de gerar os registros para o FCONT, o sistema deverá verificar as contas e lançamentos parametrizados na tela de “critérios de importação” no menu parâmetros\. Se o usuário parametrizou as contas e os números de lançamentos o sistema leva para os registros I250 somente os registros importados que compõe o número de lançamento e a conta parametrizada\.

E para a montagem do registro Pai o I200, o sistema verificará a soma dos débitos ou créditos da partida e jogará no campo 04 do registro I200 do FCONT o novo valor do registro pai somado\.

__OS2328\-RTT\-1__

__RN62__

Se o Usuário não marcar o check Box chamado “Gerar somente partidas referente a ajustes” antes de gerar os registros para o FCONT, o sistema deverá verificar o lançamentos parametrizado na tela de “critérios de importação” no menu parâmetros e carregar daquele lançamento todas as contas importadas, ou seja, da forma que os registros I200 e I250 foram importados, também deverão ser levados para o FCONT, ou seja o Pai e todos os filhos\.

__OS2328\-RTT\-1__

__RN63__

Se houver lançamentos Contábeis e/ou lançamentos Fiscais carregados através da SAFX129, ou inseridos de forma manual na tela Manutenção > Lançamentos Contábeis e Fiscais realizados na tela de manutenção, deverá ser montado o registro I200 e I250 conforme os dados lá informados\. Os mesmos deverão ser montados da seguinte forma:

Registro I200 para os lançamentos fiscais:

Campo1: Texto fixo contendo "I200”

Campo 2: Número ou código de identificação única do lançamento contábil

Campo 3: Data do lançamento

Campo 4: Valor do lançamento \(essa deve ser a soma de todos os lançamentos feitos na nova tabela cujo indicador seja “D” – débitos ou crédito 

Campo 5: Indicador do tipo de lançamento deve ser preenchido com “N ou F”\.

Registro I250 para os lançamentos fiscais:

Campo 1: Texto fixo contendo "I250"

Campo 2: Código da conta analítica debitada/creditada

Campo 3: Código do centro de custos

Campo 4: Valor total debitado/creditado \(Valor da partida\)

Campo 5: Indicador da natureza do lançamento: D\- Débito;  C\- Crédito

Campo 6: Arquivamento

Campo 7: Código do Histórico padrão, conforme tabela I075

Campo 8: Histórico completo da partida ou histórico complementar

Campo 9: Código de identificação do participante

__OS2328\-RTT\-1__

__RN63\.1__

Quando o sistema para gerar o I200 e I250 encontrar diferenças entre a soma dos débitos e a soma dos créditos acusar a seguinte mensagem:

Tipo I250 \(partidas do Lançamento\) – Divergência entre valores Total de Débito X Total de Crédito para o número de lançamento\. Favor Verificar lnaçamento Número – Data do Lançamento \(\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\. \- \.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\)

E apresenta no log o nº do lançamento e a data do mesmo que deu erro\.

Também apresentar a mensagem abaixo:

Geração do meio magnético finalizado com aviso\.

__OS2328\-RTT\-1__

__RN64__

Registro I990:

Para geração desse registro o sistema deverá internamente contar quantos registros existem do bloco I e informar nesse último o total\.

Considerando que Campo 1: Texto fixo contendo "I990", e campo 2: Quantidade total de linhas do Bloco I

__OS2328\-RTT\-1__

__RN65__

Registro J001:

Campo 1: Texto fixo contendo "J001"  

Para geração desse registro o sistema deverá verificar se houve movimentação no período, preencher o campo 2 do registro em questão com 0 quando existir dados e 1 quando não existir\. Essa verificação poderá ser feita se houveram registros I200 e I250 no arquivo\.

__OS2328\-RTT\-1__

__RN66__

Registro J930:

Para geração desse registro o sistema deverá efetuar a mesma geração que hoje já funciona para a ECD:

Ou seja, os dados serão gerados conforme parametrização efetuada na tela de Dados Iniciais guia Signatários do módulo do FCONT\. Sendo:

Campo 1: Texto fixo contendo “J930”

Campo 2: Nome do signatário, cujo campo é o 02 \(NOM\_RESPONSAVEL\) na tabela RESP\_INFORMACAO

Campo 3: CPF, cujo campo é o 20 \(NUN\_CPF\)  na tabela RESP\_INFORMACAO

Campo 4: Qualificação do assinante, cujo campo é o 21 \(DSC\_CARGO\) na tabela RESP\_INFORMACAO

Campo 5: Código de qualificação do assinante,  cujo campo é o 04 \(COD\_QUALIF\_SPED\) na tabela SPED\_DADOS\_SIGNATARIO\.

Campo 6: Número de inscrição do contabilista, cujo campo é o 02 \(NUM\_CRC\) na tabela RESP\_CONTADOR

__OS2328\-RTT\-1__

__RN67__

Registro J990:

Para geração desse registro o sistema deverá internamente contar quantos registros existem do bloco J e informar nesse último o total\.

Considerando que Campo 1: Texto fixo contendo "J990", e campo 2: Quantidade total de linhas do Bloco J

Exemplo:

|J001|0|

|J930|JOSE LUIS MAGALHAES SALAZAR|90251857700|Diretor|203||

|J930|RONALDO FERRARI|49214314934|Contador|900|1MT3755/03T|

__|J990|4|__

__OS2328\-RTT\-1__

__RN68__

Registro M001:

Campo 1: Texto fixo contendo "M001"  

Para geração desse registro o sistema deverá verificar se houve movimentação no período, preencher o campo 2 do registro em questão com 0 quando existir dados e 1 quando não existir\.

Exemplo: |M001|0|

__OS2328\-RTT\-1__

__RN69__

Registro M020:

Campo1: Texto fixo contendo “M020”\.

Campo 2: Qualificação da Pessoa Jurídica, para esse campo deverá ser levado em conta a entidade responsável informada na tela de dados iniciais no menu parâmetros, se lá estiver Receita Federal o campo 2 deverá ser gerado com 10\. Se lá estiver Banco Central COSIF então o campo 2 deverá ser gerado com 20, se lá estiver SUSEP o campo 2 deverá ser gerado com 00\.

Campo 3: Tipo de Escrituração, se o campo “Tipo de Escrituração” da tela de geração estiver Original levar 0, se estiver Retificador levar 1\. 

Campo 4: Número do recibo da escrituração anterior a ser retificada, utilizada quando o campo acima for = 1\.

Neste campo trará o valor do campo “Número do Recibo” da tela de geração do meio magnético\.

Exemplo: |M020|10|0|| ou|M020|20|1|123| ou |M020|00|||

Lembrando que quando o campo 2 do registro M020  = 00, então não deverá existir registro I051 no arquivo\.

__OS2328\-RTT\-1__

__RN70__

Registro M030:

Campo1: Texto fixo contendo “M030”\.

Campo 2: Tabela de períodos Esse campo deverá ser carregado conforme informação do campo Período de Apuração da tela de Manutenção > Lucro/Prejuízo Contábil, se o usuário parametrizou lá Anual neste campo desse registro deverá ser gerado o valor “A00”, se fora parametrizado “Primeiro trimestre” então deve ser gerado o valor = “T01”, se fora parametrizado “Segundo trimestre” então deve ser gerado o valor =  “T02”, se fora parametrizado “Terceiro trimestre” então deve ser gerado o valor = “T03” e se fora parametrizado “Quarto trimestre” então deve ser gerado o valor = “T04”\.

Campo 3: Não preencher

Campo 4: Não preencher

Campo 5: Valor do lucro líquido contábil do período, este deverá ser recuperado da tela Manutenção > Lucro/Prejuízo contábil\.

Campo 6: Indicador da situação do saldo final: D \- Prejuízo; C \- Lucro\.

Observe cada linha existente na tela de manutenção referente o Lucro/Prejuízo será gerado um registro M030 diferente, podendo existir até 4 no máximo dentro do arquivo\.

Exemplo: |M030|A00|||65804622,28|D| ou 

|M030|T01|||9098,28|C|

|M030|T02|||4622,28|D|

|M030|T03|||45704622,28|C|

|M030|T04|||23404622,28|C|

__OS2328\-RTT\-1__

__RN71__

Registro M990:

Para geração desse registro o sistema deverá internamente contar quantos registros existem do bloco M e informar nesse último o total\.

Considerando que Campo 1: Texto fixo contendo "M990", e campo 2: Quantidade total de linhas do Bloco M

Exemplo: 

|M001|0|

|M020|10|

|M030|A00|||65804622,28|D|

__|M990|4|__

__OS2328\-RTT\-1__

__RN72__

Registro 9001:

Campo 1: Texto fixo contendo "9001"  

Para geração desse registro o sistema deverá verificar se houve movimentação no período, preencher o campo 2 do registro em questão com 0 quando existir dados e 1 quando não existir\. Essa verificação poderá ser feita se houveram registros I200 e I250 no arquivo\.

Exemplo: |9001|0|

__OS2328\-RTT\-1__

__RN73__

Registro 9900:

Campo 1: Texto fixo contendo "9900"

Campo 2: Registro que será totalizado no próximo campo, \(para geração desse registro o sistema deverá internamente verificar os registros existentes no arquivo e a cada um, identificar nesse campo do registro 9900\)\.

Campo 3: Total de registros do tipo informado no campo anterior, \(para geração desse registro o sistema deverá internamente contar os registros identificados e informar o total neste campo\)\.

Exemplo:

|9900|0000|1|

|9900|I001|1|

|9900|I050|63|

|9900|I051|20|

__OS2328\-RTT\-1__

__RN74__

Registro 9990:

Para geração desse registro o sistema deverá internamente contar quantos registros existem do bloco 9 e informar nesse último o total\.

Considerando que Campo 1: Texto fixo contendo "9990", e campo 2: Quantidade total de linhas do Bloco 9

Exemplo: |9990|37|

__OS2328\-RTT\-1__

__RN75__

Registro 9999:

Para geração desse registro o sistema deverá internamente contar quantas linhas existem no arquivo e informar nesse último o total\.

Considerando que Campo 1: Texto fixo contendo "9999", e campo 2: Quantidade total de linhas do arquivo digital\.

Exemplo: |9999|384|

__OS2328\-RTT\-1__

__RN76__

Para a emissão do relatório de resultado, o sistema deverá apresentar uma janela para a parametrização dos dados a serem gerados \(item 2\.1\.1\.2\. do documento de requisitos\)\.

__OS2328\-RTT\-1__

__RN77__

A tela de parametrização deverá conter os seguintes campos: Estabelecimento, Período, Conta inicial e Conta Final e Gerar Relatório \(Completo e Somente Contas Ajustadas\)\.

__OS2328\-RTT\-1__

__RN78__

O campo "Estabelecimento" deverá apresentar os estabelecimentos da empresa em questão, demonstrando se é centralizado ou descentralizado\.

Ex\.: Centralizado \- Estabelecimento

        Descentralizado – Estabelecimento

__OS2328\-RTT\-1__

__RN79__

O campo "Período" deverá ter duas caixas de texto para a digitação do período inicial e final e, suas características serão no formato "Data" permitindo a digitação do dia, mês e ano \("dd/mm/aaaa"\)\.

__OS2328\-RTT\-1__

__RN79\.1__

Se o usuário informar a conta somente no campo “conta inicial” então deverá ser apresentada a seguinte mensagem: informar conta final\.

Se o usuário informar a conta somente no campo “conta final” então deverá ser apresentada a seguinte mensagem: informar conta inicial\.

Se o usuário não informar nenhum deverá vir todas as contas geradas para o relatório\.

Se o usuário informar  conta inicial e uma final diferentes deverá vir para o relatório todo aquele intervalo entre elas e as próprias contas informadas

__OS2328\-RTT\-1__

__RN80__

O campo "Gerar Relatório" deverá possuir duas opções: "Completo" e "Somente Contas Ajustadas"\.

__OS2328\-RTT\-1__

__RN81__

Se a opção "Completo" do campo "Gerar Relatório" estiver marcada, o sistema deverá recuperar todas as contas do registro importado filtrando pelo período informado no campo "Período"\.

__OS2328\-RTT\-1__

__RN82__

Se a opção "Somente Contas Ajustadas" do campo "Gerar Relatório" estiver marcada, o sistema deverá recuperar __SOMENTE__ as contas do registro importado que sofreram lançamentos de valores na tela de “Lançamentos Contábeis e/ou Fiscais” \(SAFX129\) dentro do período informado no campo "Período" da geração do relatório\.

Quando a opção “Somente Contas Ajustadas” estiver marcada, o sistema deverá recuperar as contas do arquivo importado para a geração do relatório observando se houve lançamento contábil/fiscal e, se o campo “Data Lançamento” da tabela SAFX129 está dentro do período informado na parametrização para a geração do relatório\.

__OS2328\-RTT\-1__

__RN83__

Se não houver dados a serem recuperados, o sistema deverá apresentar no leiaute do relatório a frase "__SEM MOVIMENTO__" conforme padrão Mastersaf\.

__OS2328\-RTT\-1__

__RN84__

Recuperar o valor do campo 02\-COD\_CTA do registro I155 do arquivo ECD importado\. 

Para a geração, o sistema deverá observar se os campos 02 \(DT\_INI\) e 03 \(DT\_FIN\) do registro I150 associado ao registro I155 estão dentro do período informado no campo “Período” da tela de parametrização para a geração do relatório\.

__OS2328\-RTT\-1__

__RN85__

Recuperar o valor do campo 8\-COD\_CTA do registro I050 associado ao campo 02\-COD\_CTA \(RN84\) do registro I155 do arquivo ECD importado\.

__OS2328\-RTT\-1__

__RN86__

Recuperar o valor do campo 09\-IND\_DC\_FIN do registro I155 associado ao campo 02\-COD\_CTA \(RN84\) do registro I155 do arquivo ECD importado\.

__OS2328\-RTT\-1__

__RN87__

Recuperar o valor do campo 08\-VL\_SLD\_FIN do registro I155 associado ao campo 02\-COD\_CTA \(RN84\) do registro I155 do arquivo ECD importado\.

O formato do campo deverá ser de 17 posições \(15V2\)\.

__OS2328\-RTT\-1__

__RN88__

Recuperar o valor do campo 07\-VLR\_LANCTO da tabela SAFX129 para os lançamentos de exclusão \(campo 17\-TIPO\_LANCTO = “N” da tabela SAFX129\)\. Essa informação deve estar associada a conta contábil \(RN84\)\.

A apresentação do valor deve ser concatenada com o campo 05\-IND\_DEB\_CRE da tabela SAFX129\. 

\(07\-VLR\_LANCTO\+05\-IND\_DEB\_CRE\)

Se houver mais de um lançamento a débito ou a crédito dentro do período informado para a geração do relatório, o sistema deverá somar os valores a débito ou a crédito ou subtrair crédito \- débito\. 

Se não houver valor, preencher com “brancos”\.

O formato do campo deverá ser de 17 posições \(15V2\) \+ o indicador débito/crédito\.

__OS2328\-RTT\-1__

__RN89__

Recuperar o valor do campo 07\-VLR\_LANCTO da tabela SAFX129 para os lançamentos de exclusão \(campo 17\-TIPO\_LANCTO = “F” da tabela SAFX129\)\. Essa informação deve estar associada a conta contábil \(RN84\)\.

A apresentação do valor deve ser concatenada com o campo 05\-IND\_DEB\_CRE da tabela SAFX129\. 

\(07\-VLR\_LANCTO\+05\-IND\_DEB\_CRE\)

Se houver mais de um lançamento a débito ou a crédito dentro do período informado para a geração do relatório, o sistema deverá somar os valores a débito ou a crédito ou subtrair crédito \- débito\. 

Se não houver valor, preencher com “brancos”\.

O formato do campo deverá ser de 17 posições \(15V2\) \+ o indicador débito/crédito\.

__OS2328\-RTT\-1__

__RN90__

Campo referente ao __Saldo Fiscal\.__

O sistema deverá efetuar um cálculo matemático e apresentar o resultado\. Para o cálculo, será necessário realizar as seguintes condições:

1ª Condição:

Se o valor recuperado da RN87 for débito \(RN86 = “D”\), somar com o valor do ajuste de expurgo \(RN88\) a crédito \(indicador deb/cred = “C”\) e, subtrair se o valor do ajuste de expurgo \(RN88\) for a débito \(indicador deb/cred = “D”\)\. Depois, somar com o valor do ajuste de inclusões \(RN89\) a débito \(indicador deb/cred = “D”\) e, subtrair se o valor do ajuste de inclusões \(RN89\) for a crédito \(indicador deb/cred = “C”\)\.

Ex1: 

__RN86__

__RN87__

__RN88__

__RN89__

__RN90__

__RN91__

D

55,00

15,00 C

11,00 D

81,00

D

Ex2

__RN86__

__RN87__

__RN88__

__RN89__

__RN90__

__RN91__

D

55,00

15,00 D

11,00 C

29,00

D

Ex3

__RN86__

__RN87__

__RN88__

__RN89__

__RN90__

__RN91__

D

55,00

12,00 C

89,00 C

22,00

C

2ª Condição:

Se o valor recuperado da RN87 for crédito \(RN86 = “C”\), somar com o valor do ajuste de expurgo \(RN88\) a débito \(indicador deb/cred = “D”\) e, subtrair se o valor do ajuste de expurgo \(RN88\) for a crédito \(indicador deb/cred = “C”\)\. Depois, somar com o valor do ajuste de inclusões \(RN89\) a crédito \(indicador deb/cred = “C”\) e, subtrair se o valor do ajuste de inclusões \(RN89\) for a débito \(indicador deb/cred = “D”\)\.

Ex1: 

__RN86__

__RN87__

__RN88__

__RN89__

__RN90__

__RN91__

C

77,00

27,00 D

22,00 C

126,00

C

Ex2

__RN86__

__RN87__

__RN88__

__RN89__

__RN90__

__RN91__

C

77,00

27,00 C

22,00 D

28,00

C

Ex3

__RN86__

__RN87__

__RN88__

__RN89__

__RN90__

__RN91__

C

77,00

25,00 D

129,00 D

27,00

D

O formato do campo deverá ser de 17 posições \(15V2\)\.

__OS2328\-RTT\-1__

__RN91__

Se o resultado do cálculo efetuado na RN90 for débito, preencher com “D”, se for crédito, preencher com “C”\.

__OS2328\-RTT\-1__

__RN92__

Os valores apresentados no campo “Saldo Fiscal” \(RN90\) não deverá conter sinais matemáticos \(“\+” e “\-“\)

__OS2328\-RTT\-1__

__RN93__

Para a emissão do relatório Lucro/Prejuízo, o sistema deverá apresentar uma janela para a parametrização dos dados a serem gerados \(item 2\.1\.1\.2\.2 do documento de requisitos\)\.

__OS2328\-RTT\-1__

__RN94__

A tela de parametrização deverá conter os seguintes campos: Estabelecimento, Exercício e Período\.

__OS2328\-RTT\-1__

__RN95__

O campo “Exercício” deverá ser numérico \(N\) e possuir o formato AAAA\.

__OS2328\-RTT\-1__

__RN96__

O campo “Período” deverá ter o formato de “Combo Box” e com os valores fixos: 

Anual

1º \- Trimestre

2º \- Trimestre

3º \- Trimestre

4º \- Trimestre

Neste campo não será permitido a digitação\.

__OS2328\-RTT\-1__

__RN97__

Para a apresentação das informações, o campo “Período” deverá estar associado ao campo “Exercício”, ou seja, o relatório deverá demonstrar as informações de acordo com a seleção do campo “Período” e dentro do exercício informado\.

Exemplo:

__Exercício:__ 2008

__Período:__ 2º \- Trimestre 

Resultado: O sistema deverá apresentar as informações do 2º trimestre do ano de 2008\.

__OS2328\-RTT\-1__

__RN98__

Para a seleção da opção “Anual” do campo “Período”, o sistema deverá gerar o relatório com as informações de  todos os trimestres, separando as informações por trimestre\.

Exemplo:

__Exercício:__ 2008

__Período:__ Anual

Resultado:

__Dados da Empresa \(Padrão Mastersaf\)__

__Exercício: 2008__

__Período: Anual__

__Demonstrativo de Apuração__

__1º \- Trimestre__

__Lucro/Prejuízo Contábil__

Cód\. Conta

Descrição

Expurgos

Inclusões

__Lucro Líquido/Prejuízo Contábil \- Fiscal__

 

__2º \- Trimestre__

__Lucro/Prejuízo Contábil__

Cód\. Conta

Descrição

Expurgos

Inclusões

__Lucro Líquido/Prejuízo Contábil \- Fiscal__

__3º \- Trimestre__

__Lucro/Prejuízo Contábil__

Cód\. Conta

Descrição

Expurgos

Inclusões

__Lucro Líquido/Prejuízo Contábil \- Fiscal__

__4º \- Trimestre__

__Lucro/Prejuízo Contábil__

Cód\. Conta

Descrição

Expurgos

Inclusões

__Lucro Líquido/Prejuízo Contábil \- Fiscal__

 

__OS2328\-RTT\-1__

__RN99__

Para a geração do relatório, o sistema deverá recuperar e apresentar SOMENTE as contas de resultado \(campo 07\-IND\_NATUREZA = “4”  e = “3” da tabela safx2002\)\. 

__OS2328\-RTT\-1__

__RN100__

Recuperar o valor do campo 04\-CONTA\_DEB\_CRED da tabela SAFX129\. 

A conta a ser apresentada deve estar de acordo com a RN99\.

__OS2328\-RTT\-1__

__RN101__

Recuperar a descrição da conta contábil da tabela SAFX129 associado a RN100\. 

__OS2328\-RTT\-1__

__RN102__

Recuperar o valor do campo 07\-VLR\_LANCTO da tabela SAFX129 associado a RN100 para os lançamentos de exclusão \(campo 17\-TIPO\_LANCTO = “N” da tabela SAFX129\)\.

A apresentação do valor deve ser concatenada com o campo 05\-IND\_DEB\_CRE da tabela SAFX129\. 

\(07\-VLR\_LANCTO\+05\-IND\_DEB\_CRE\)

Se houver mais de um lançamento a débito ou a crédito dentro do período informado para a geração do relatório, o sistema deverá somar os valores a débito ou a crédito ou subtrair crédito \- débito\. 

Se não houver valor, preencher com “brancos”\.

O formato do campo deverá ser de 17 posições \(15V2\) \+ o indicador débito/crédito\.

__OS2328\-RTT\-1__

__RN103__

Recuperar o valor do campo 07\-VLR\_LANCTO da tabela SAFX129 associado a RN100 para os lançamentos de inclusão \(campo 17\-TIPO\_LANCTO = “F” da tabela SAFX129\)\.

A apresentação do valor deve ser concatenada com o campo 05\-IND\_DEB\_CRE da tabela SAFX129\.

\(07\-VLR\_LANCTO\+05\-IND\_DEB\_CRE\)

Se houver mais de um lançamento a débito ou a crédito dentro do período informado para a geração do relatório, o sistema deverá somar os valores a débito ou a crédito ou subtrair crédito \- débito\. 

Se não houver valor, preencher com “brancos”\.

O formato do campo deverá ser de 17 posições \(15V2\) \+ o indicador débito/crédito\.

__OS2328\-RTT\-1__

__RN104__

Recuperar o valor do campo “Lucro ou Prejuízo Contábil do Período” da tela “Manutenção das Linhas do Lucro ou Prejuízo Contábil do Período para o FCONT” \(Menu: Manutenção 🡪 Lucro/Prejuízo contábil\)

A recuperação deverá ser de acordo com o exercício e período informado\.

Exemplos:

__Exercício:__ 2008

__Período:__ 1º \- Trimestre

Resultado: Recuperar o valor do campo “Lucro ou Prejuízo Contábil do Período” referente ao 1º trimestre do ano de 2008\.

__Exercício:__ 2008

__Período:__ 3º \- Trimestre

Resultado: Recuperar o valor do campo “Lucro ou Prejuízo Contábil do Período” referente ao 3º trimestre do ano de 2008\.

Para a apresentação das informações do período “Anual”, o sistema deverá agir conforme RN98\.

Se não houver valor, preencher com “0,00”\.

O formato do campo deverá ser de 17 posições \(15V2\) \+ o indicador débito/crédito\.

__OS2328\-RTT\-1__

__RN105__

Totalizador dos lançamentos de exclusão \(expurgos/estornos\)\.

O sistema deverá efetuar um cálculo matemático e apresentar o resultado\. O cálculo deverá ser da seguinte forma:

Resultado = Lançamentos a crédito \(C\) – Lançamentos a débito \(D\)

O resultado final deve estar concatenado com o indicador de débito/crédito\. \(Resultado \+ Indicador Débito/Crédito\)\.

Utilizar as condições abaixo para a concatenação com o indicador:

      Se Lançamentos a crédito \(C\) >= Lançamentos a débito \(D\) então,

            Concatenar “Resultado \+ C”

            Ex\.: 100,00 C \- 50,00 D = 50,00 C

       Se Lançamentos a crédito \(C\) <= Lançamentos a débito \(D\) então,

            Concatenar “Resultado \+ D”

            Ex\.: 100,00 C \- 200,00 D = 100,00 D

O resultado final não poderá conter sinais matemáticos \(“\+” ou “\-“\)\.

Se não houver lançamentos, preencher com “0,00”\.

O formato do campo deverá ser de 17 posições \(15V2\) \+ o indicador débito/crédito\.

__OS2328\-RTT\-1__

__RN106__

Totalizador dos lançamentos de inclusão\.

O sistema deverá efetuar um cálculo matemático e apresentar o resultado\. O cálculo deverá ser da seguinte forma:

Resultado = Lançamentos a crédito \(C\) – Lançamentos a débito \(D\)

O resultado final deve estar concatenado com o indicador de débito/crédito\. \(Resultado \+ Indicador Débito/Crédito\)\.

Utilizar as condições abaixo para a concatenação com o indicador:

      Se Lançamentos a crédito \(C\) >= Lançamentos a débito \(D\) então,

            Concatenar “Resultado \+ C”

            Ex\.: 100,00 C \- 50,00 D = 50,00 C

       Se Lançamentos a crédito \(C\) <= Lançamentos a débito \(D\) então,

            Concatenar “Resultado \+ D”

            Ex\.: 100,00 C \- 200,00 D = 100,00 D

O resultado final não poderá conter sinais matemáticos \(“\+” ou “\-“\)\.

Se não houver lançamentos, preencher com “0,00”\.

O formato do campo deverá ser de 17 posições \(15V2\) \+ o indicador débito/crédito\.

__OS2328\-RTT\-1__

__RN107__

Campo referente ao __Lucro Líquido/Prejuízo Contábil – Fiscal\.__

O sistema deverá efetuar um cálculo matemático e apresentar o resultado\. Para o cálculo, será necessário realizar as seguintes condições:

1ª Condição:

Se o valor recuperado da RN100 for débito \(indicador deb/cred = “D”\), somar com o valor do resultado de expurgo \(RN101\) a crédito \(indicador deb/cred = “C”\) e, subtrair se o resultado de expurgo \(RN101\) for a débito \(indicador deb/cred = “D”\)\. Depois, somar com o resultado de inclusões \(RN102\) a débito \(indicador deb/cred = “D”\) e, subtrair se o resultado de inclusões \(RN102\) for a crédito \(indicador deb/cred = “C”\)\.

Ex1: 

__RN100__

__RN101__

__RN102__

__RN103__

55,00 D

15,00 C

11,00 D

81,00 D

Ex2

__RN100__

__RN101__

__RN102__

__RN103__

55,00 D

15,00 D

11,00 C

29,00 D

Ex3

__RN100__

__RN101__

__RN102__

__RN103__

55,00 D

12,00 C

89,00 C

22,00 C

Se o resultado do cálculo efetuado for débito, concatenar com o indicador “D”, se for crédito, concatenar com o indicador “C”\.

2ª Condição:

Se o valor recuperado da RN100 for crédito \(indicador deb/cred = “C”\), somar com o resultado de expurgo \(RN101\) a débito \(indicador deb/cred = “D”\) e, subtrair se o resultado de expurgo \(RN101\) for a crédito \(indicador deb/cred = “C”\)\. Depois, somar com o resultado de inclusões \(RN102\) a crédito \(indicador deb/cred = “C”\) e, subtrair se o resultado de inclusões \(RN102\) for a débito \(indicador deb/cred = “D”\)\.

Ex1: 

__RN100__

__RN101__

__RN102__

__RN103__

77,00 C

27,00 D

22,00 C

126,00 C

Ex2

__RN100__

__RN101__

__RN102__

__RN103__

77,00 C

27,00 C

22,00 D

28,00 C

Ex3

__RN100__

__RN101__

__RN102__

__RN103__

77,00 C

25,00 D

129,00 D

27,00 D

Se o resultado do cálculo efetuado for débito, concatenar com o indicador “D”, se for crédito, concatenar com o indicador “C”\.

O resultado final não poderá conter sinais matemáticos \(“\+” ou “\-“\)\.

O formato do campo deverá ser de 17 posições \(15V2\) \+ o indicador débito/crédito\.

__OS2328\-RTT\-1__

__RN108__

Cada registro de conta deverá ser gerado em uma única linha\.

__OS2328\-RTT\-1__

__RN109__

A tela de perfil deverá ser alterada com a inserção dos registros I350 e I355\. Os mesmos deverão ficar desabilitados, de forma que o usuário não consiga efetuar nenhuma alteração\. O Check Box desses registros deverão estar marcados

__OS2328\-RTT\-2__

__RN110__

A tela de Recuperação do Lucro contábil deverá ser retirada desse módulo, visto que não iremos mais importar a ECD, isso faz com que a operação não seja mais necessária\.  Assim como o submenu Parâmetro > Critérios para importação também será retirado do menu\.

__OS2328\-RTT\-2__

__RN111__

O menu Parâmetro estará organizado da seguinte forma: 

Menu: Parâmetros com os submenus Perfil e Dados Adicionais\.

__OS2328\-RTT\-2__

__RN112__

A tela de importação da ECD deverá ser desativada, este menu deverá ser retirado do módulo FCONT\.

__OS2328\-RTT\-2__

__RN113__

Após a alteração a barra de menu do módulo deverá ser apresentada com as seguintes opções de seleção:

Arquivo, Parâmetros, Manutenção, Geração, Relatórios, Janela e Ajuda\.

__OS2328\-RTT\-2__

__RN114__

No caminho indicado no documento de requisitos, quando acionado a pasta abrir da tela, é apresentado uma tela de pesquisa, para que o usuário selecione ou filtre as informações cadastradas na tela de Lançamentos contábeis e ou fiscais, nesse tela deverá ser adicionada uma coluna referente ao “Tipo do Lançamento” para que o usuário possa Filtra por “N\- Normal” ou “F\- Fiscal”\.

__OS2328\-RTT\-2__

__RN115__

O Arquivo magnético sofrerá as seguintes alterações nos registros:

No momento da geração do arquivo magnético, o sistema deverá considerar os dados carregados nas SAFX01 e SAFX02 para gerar os registros de saldos \(I150 e I155\)

__OS2328\-RTT\-2__

__RN116__

Quando o sistema durante a geração do arquivo encontrar saldo zerado na SAFX02 o mesmo deverá verificar se a conta a que se refere o saldo é de resultado:

Se sim: o mesmo deverá buscar o saldo da SAFX01 dos lançamentos cujo tipo de lançamento é igual a “E”\.

__OS2328\-RTT\-2__

__RN117__

Para os registros do De/Para do Plano referencial X Plano de Contas Empresa, o sistema deverá fazer a verificação dos dados carregados na SAFX2101

__OS2328\-RTT\-2__

__RN118__

Os registros I075 e registros I100 deverão ser gerados somente para os centros de custos e históricos utilizados na movimentação\.

__OS2328\-RTT\-2__

__RN119__

Para geração dos registros referente os lançamentos normais e fiscais \(I200 e I250\) o sistema deverá continuar verificando os dados carregados na SAFX129 e não considerar nenhum lançamento da SAFX01\.

__OS2328\-RTT\-2__

__RN120__

A partir de agora o sistema deverá gerar os registros de encerramento para as contas de resultado olhando os lançamentos de encerramento da SAFX01\. O mesmo deverá verificar o indicador de débito/crédito e deverá inverter o sinal no registro I355 assim como funciona para a ECD\. 

__OS2328\-RTT\-2__

__RN121__

Os registros que deverão contas no arquivo do FCONT serão:

0000: Registro de abertura com dados do estabelecimento o mesmo utiliza a tabela ESTABELECIMENTO e a tabela de REGISTRO\_ESTADUAL\. E deverá ser montado conforme segue o exemplo:

|0000|LALU|01012008|31122008|Empresa testes S/A|53113696000129|SC|250318407|4204301|2289||

__OS2328\-RTT\-2__

__RN122__

I001: Registro de abertura do bloco I, o mesmo deve ser gerado sempre que ocorrer a geração de registros de saldos ou

lançamentos contábeis indicando que existe movimentação nesse registro, gerando no campo 2 desse registro “0” quando existir movimento e “1” quando não existir\. Conforme segue o exemplo:

|I001|0|

__OS2328\-RTT\-2__

__RN123__

I050: Registro referente ao Plano de contas da empresa, o mesmo deve ser gerado com base na tabela safx2101 importada pelo cliente\. Assim como ocorre na geração do arquivo da ECD\. Os campos do registro estarão organizados da seguinte forma:

|I050|01012008|04|A|6|3654800|30011|Ganho nao Realizado c/ Premio Opcoes\-Lei 11638/07|

__OS2328\-RTT\-2__

__RN124__

I051: Registro referente ao Plano Referencial importado na TFIX64, porém, o mesmo deve ser gerado com base na tabela safx2101 importada pelo cliente\. Assim como ocorre na geração do arquivo da ECD\. Os campos do registro estarão organizados da seguinte forma:

|I051|10||1\.01\.05\.05\.00|

__OS2328\-RTT\-2__

__RN125__

I075: Registro referente ao histórico padrão utilizado na movimentação, para a ECD esse registro é gerado se na geração do registro I250 o campo 7 apresentar algum histórico para o FCONT utilizaremos o mesmo processo, porém, o histórico utilizado vem da SAFX129 que gera os registros de lançamentos contábeis\. Se o campo 7 do registro I250 estiver com dados será gerados um registro I075 para cada código de histórico diferente existente no registro I250\.

Os campos do registro estarão organizados da seguinte forma:

|I075|G001|Histórico Padrão do Livro G|

__OS2328\-RTT\-2__

__RN126__

I100: Registro referente aos centros de custos utilizado na movimentação, para a ECD esse registro é gerado se na geração do registro I250 o campo 3 apresentar algum centro de custo, e também se estes forem apresentados no campo 3 do registro I155\.

Para o FCONT utilizaremos o mesmo processo, porém, o centro de custo utilizado vem da SAFX129 quando se referir a lançamentos contábeis e quando se referir a saldo vem da tabela SAFX01 e SAFX02, que gera os registros dos saldos de contas patrimoniais e de resultado encerrados no período\. Se o campo 3 dos registros I250 e I155 estiverem com dados será gerados um registro I100 para cada código de centro de custo diferente existente\.

Os campos do registro estarão organizados da seguinte forma:

|I100|01012008|23456|centro de custo teste|

__OS2328\-RTT\-2__

__RN127__

I150: Registro referente ao abertura dos saldos utilizado na movimentação, para a ECD esse registro é gerado se existir 

movimentação de saldo na safx02 para contas patrimoniais e com base na safx 01 para contas de resultado quando o 

saldo estiver zerado no fim do período\. Para o FCONT utilizaremos o mesmo processo, os saldos utilizados virão exatamente das mesmas tabelas com o mesmo conceito e funcionamento\.

Os campos do registro estarão organizados da seguinte forma:

|I150|01032008|31032008|

__OS2328\-RTT\-2__

__RN128__

I155: Registro referente ao movimentação dos do período, para a ECD esse registro é gerado se existir 

movimentação de saldo na safx02 para contas patrimoniais e com base na safx 01 para contas de resultado quando o 

saldo estiver zerado no fim do período\. Para o FCONT utilizaremos o mesmo processo, os saldos utilizados virão exatamente das mesmas tabelas com o mesmo conceito e funcionamento\.

Os campos do registro estarão organizados da seguinte forma:

|I155|010101||0,00|C|292803323,00|226998700,72|65804622,28|D|

__OS2328\-RTT\-2__

__RN129__

I200: Registro referente a abertura dos lançamentos efetuados no período, para a ECD esse registro é gerado se existir 

movimentação na safx01\. Para o FCONT utilizaremos o mesmo processo, porém os lançamentos gerados nesses registros de lançamentos virão da SAFX129\. De forma que quando o sistema encontre um registro cadastrado na SAFX129 seja uma linha de registro I250 gerado diferente no arquivo magnético\.

Os campos do registro estarão organizados da seguinte forma:

|I200|1|01012008|193981235,00|N|

__OS2328\-RTT\-2__

__RN130__

I250: Registro referente a abertura dos lançamentos efetuados no período, para a ECD esse registro é gerado se existir 

movimentação na safx01\. Para o FCONT utilizaremos o mesmo processo, porém os lançamentos gerados nesses registros de lançamentos virão da SAFX129\. De forma que quando o sistema encontre um registro cadastrado na SAFX129 seja uma linha de registro I250 gerado diferente no arquivo magnético\.

Os campos do registro estarão organizados da seguinte forma:

|I250|1701860||50807697,00|D|01595884142008003||AJUSTE||

__OS2328\-RTT\-2__

__RN131__

Il: Registro referente a abertura dos saldos antes do encerramento efetuados no período, para a ECD esse registro é gerado se existir lançamentos tipo “E” na safx01\. Para o FCONT utilizaremos o mesmo processo, os saldos utilizados virão exatamente das mesmas tabelas com o mesmo conceito e funcionamento\.

Os campos do registro estarão organizados da seguinte forma:

|I350|31012010|

\[__CH11295/2013__\]

Se no Cadastro de Dados Iniciais do Estabelecimento que está gerando o arquivo, no campo Entidade Responsável pelo Plano Referencial, for informada a opção "20 \- Banco Central do Brasil", será gerado um único registro I350 e no campo 02 – DT\_RES será gerada a Data Final parametrizada na tela de geração \(mesmo campo utilizado para gerar o campo 04 – DT\_FIN do registro 0000\.

__OS2328\-RTT\-2__

__CH11295/2013__

__RN132__

I355: Registro referente a abertura dos saldos antes do encerramento efetuados no período, para a ECD esse registro é gerado se existir lançamentos tipo “E” na safx01\. Para o FCONT utilizaremos o mesmo processo, os saldos utilizados virão exatamente das mesmas tabelas com o mesmo conceito e funcionamento\.

Os campos do registro estarão organizados da seguinte forma:

|I355|3350495||2396250,00|C|

\[__CH11295/2013__\]

Se no Cadastro de Dados Iniciais do Estabelecimento que está gerando o arquivo, no campo Entidade Responsável pelo Plano Referencial, for informada a opção "20 \- Banco Central do Brasil", este registro será gerado consolidando, por conta e centro de custo, os valores de lançamentos tipo “E” da SAX01 de todo o período de geração parametrizado na tela de geração\. Por conta desta consolidação, o campo 04 – VL\_CTA será apurado com base na seguinte regra:

\(somatória dos lançamentos tipo “E” a crédito\) __menos__ \(somatória dos lançamentos tipo “E” a débito\)\. Deve ser mostrado sempre o valor absoluto do resultado obtido\.

Apesar de não ser demonstrado o valor apurado com sinal negativo ou positivo, este sinal deve ser considerado para obtenção do indicador de D/C \(campo 05 – IND\_DC\)\. Se o resultado obtido neste cálculo for positivo, será gerado no campo IND\_DC o conteúdo “D”\. Se for negativo, será gerado no campo IND\_DC o conteúdo “C”\.

__OS2328\-RTT\-2__

__CH11295/2013__

__RN133__

I990: Registro referente ao encerramento do bloco I, para a ECD esse registro é gerado considerando a quantidade de linhas geradas no bloco I informando essa quantidade no campo 2 do registro, Para o FCONT utilizaremos o mesmo processo\. Os campos do registro estarão organizados da seguinte forma:

|I990|210|

__OS2328\-RTT\-2__

__RN134__

Os registros abaixo já são gerados pelo sistema conforme criação das regras na OS2328\-RTT\-1 e deverão continuar sendo gerados obedecendo as mesmas regras, segue como exemplo a formatação de como deve estar organizados os registros restantes:

Os campos do registro estarão organizados da seguinte forma:

|J001|0|

|J930|JOSE ANTONIO SILVA|16204647997|Diretor|203||

|J930|JOSE ANTONIO CASTRO|48028429106|Contador|900|1OT3955/01P|

|J990|4|

|M001|0|

|M020|10|||

|M030|T01|||65804622,28|D|

|M030|T02|||75804622,28|D|

|M030|T03|||85804622,28|D|

|M990|6|

|9001|0|

|9900|0000|1|

|9990|23|

|9999|200|

__OS2328\-RTT\-2__

__RN135__

Na tela de geração do arquivo Magnético existe o campo “número do Recibo”, este campo atualmente possui tamanho 12 e deverá ser alterado para tamnho 41\.

Essa informação deverá ser gravada campo 4 do registro M020, assim como já é feita atualmente\.

__OS2328\-RTT\-2__

__RN136__

Com a retirada da Tela de recuperação do lucro contábil, o sistema deverá carregar para o campo 5 do registro M030 as informações cadastradas manualmente na tela de “Lucro/Prejuízo Contábil” localizada no menu manutenção\.

__OS2328\-RTT\-2__

__RN137__

__Registro I155__

Tratar as situações especiais da pessoa física/jurídica, em que precise ser realizada uma geração com um período ≠ ANUAL\.

No registro I155, são gerados os saldos periódicos, de acordo com o período informado no registro I150\.

DT\_INI

Data Saldo Inicial

Data de início do período\.

DT\_FIN

Data Saldo Final

Data de fim do período\.

Este registro deverá ser gerado de acordo com a data informada na tela de geração\.

Exemplo:

Se as datas em tela de geração forem:

Data Inicial: 01/01/2009

Data Final: 05/07/2009

Se a geração for __anual__, deverá ser gerado 1 registro I150 contendo:

Data inicial – 01/01/2009

Data Final – 05/07/2009

Se a geração for __trimestral__, deverão ser gerados 3 registros I150:

Data inicial – 01/01/2009

Data Final – 31/03/2009

Data inicial – 01/04/2009

Data Final – 30/06/2009

Data inicial – 01/07/2009

__Data Final – 05/07/2009__

Os registros I155 deverão ser distribuídos conforme datas no I150\.

__CH85314__

__RN138__

__Registro I250__

Tratar as situações especiais da pessoa física/jurídica, em que precise ser realizada uma geração com um período ≠ ANUAL\.

São gerados os lançamentos contábeis, conforme data informada no registro I200\.

DT\_LCTO

Data do Lançamento

Data do lançamento\.

Os lançamentos deverão ser gerados de acordo com a data x lançamento da safx129, até a data final do período estipulada na tela de geração\.

__CH85314__

__RN139__

__Registro I355__

Tratar as situações especiais da pessoa física/jurídica, em que precise ser realizada uma geração com um período ≠ ANUAL\.

São gerados os detalhes dos saldos das contas de resultado antes do encerramento, de acordo com o período informado no registro I350\.

DT\_RES

Data de apuração

Data da apuração do resultado\.

Este registro deverá ser gerado de acordo com a data informada na tela de geração\.

Exemplo:

Se as datas em tela de geração forem:

Data Inicial: 01/01/2009

Data Final: 05/07/2009

Se a geração for __anual__, deverá ser gerado 1 registro I350 contendo:

Data inicial – 01/01/2009

Data Final – 05/07/2009

Ou seja, gerar o código A00\.

Se a geração for __trimestral__, deverão ser gerados 3 registros I350:

Data inicial – 01/01/2009

Data Final – 31/03/2009

Data inicial – 01/04/2009

Data Final – 30/06/2009

Data inicial – 01/07/2009

__Data Final – 05/07/2009__

Ou seja, gerar os códigos T01, T02 e T03\.

Os registros I355 deverão ser distribuídos conforme datas no I350\.

__CH85314__

__RN140__

__Registro M030__

Tratar as situações especiais da pessoa física/jurídica, em que precise ser realizada uma geração com um período ≠ ANUAL\.

Identifica os períodos de apuração:

IND\_PER

Período Apuração

Tabela de períodos:

A00\- Anual;

T01\- Primeiro trimestre;

T02\- Segundo trimestre;

T03\- Terceiro trimestre;

T04\- Quarto trimestre;

Este registro deverá ser gerado de acordo com a data informada na tela de geração\.

Exemplo:

Se as datas em tela de geração forem:

Data Inicial: 01/01/2009

Data Final: 05/07/2009

Se a geração for __anual__, deverá ser gerado 1 registro M030 contendo:

Data inicial – 01/01/2009

Data Final – __05/07/2009__

Ou seja, no campo 02 deste registro, deverá ser gerada a informação __A00__, e o valor correspondente ao período\.

Se a geração for __trimestral__, deverão ser gerados 3 registros M030:

Data inicial – 01/01/2009

Data Final – 31/03/2009

Data inicial – 01/04/2009

Data Final – 30/06/2009

Data inicial – 01/07/2009

__Data Final – 05/07/2009__

Sendo que:

Para o primeiro trimestre, gerar o total de valores correspondente e no campo 02, gerar a informação T01\.

Para o segundo trimestre, gerar o total de valores correspondente e no campo 02, gerar a informação T02\.

Para o terceiro trimestre, gerar o total de valores correspondente e no campo 02, gerar a informação T03\.

__CH85314__

__RN141__

__Alteração da tela __

Módulo: SPED > FCONT

Menu: Parâmetro > Perfil

Incluir no campo Leiaute a opção FCONT – Controle Fiscal Contábil de Transição – Versão 2011 – Alteração da lei 6404/76

Com todas as opções do leiaute FCONT – Controle Fiscal Contábil de Transição, porém incluindo os registros I156,I256, I356 \(que não são Obrigatórios\) dentro do Bloco I\.

OS2328\-RTT\-5

__RN141\.01__

__Este novo layout será obrigatório a partir do ano\-calendário 2010\.__

__Todos os registros deverão ser mantidos conforme layout anterior, incluindo as alterações e criações dos novos registros que estarão definidos abaixo\.__

OS2328\-RTT\-5

__RN142__

Alteração no Registro 0000:

Incluir o campo 12 – IND\_SIT\_INI\_PER \(Indicador de inicio de período\), com 1 posição \(campo numérico\)\. Os valores válidos são: 0,1,2 ou 3\.

0 \- Normal \(Início no primeiro dia do ano\);

1 \- Abertura;

2 \- Resultante de Cisão/Fusão ou  remanescente de Cisão ou realizou Incorporação;

3 \- Início da obrigatoriedade da entrega da ECD no curso do ano\-calendário

Usar as seguintes regras:

Se estiver preenchido o campo 45 "Data de Inicio da Atividade" da tabela Estabelecimento e a data estiver compreendida no mesmo período de geração do meio magnético, o sistema gerará para o arquivo nesse campo a indicação "1";

Se estiver preenchido um dos campos 66 “DATA\_CISAO”,  67 “DATA\_FUSAO” , 68 “DATA\_INCORPORACAO”  da tabela de Estabelecimento, se a data estiver compreendida no mesmo período de geração do meio magnético considerar a seguinte regra:

Informar 2, para eventos ocorridos posterior a essas datas \(compreendidas no ano da situação especial\) e se o campo 56 “DT\_ENCERRAMENTO”  da tabela de Estabelecimento, e se a data  estiver compreendida no mesmo período de geração do meio magnético;

Caso a data de inicio da atividade e uma das outras datas citadas acima estiverem preenchidas e compreendidas no período considerar sempre a maior data \(que deverá ser a data referente à Cisão, Fusão, Incorporação ou Encerramento\)\.

Ex\. A empresa teve uma cisão em 25/10/11 , no primeiro arquivo até a data da cisão este campo deve sair com ‘0’ e no segundo com o indicador ‘2’\.

Se nenhum dos campos  de data \(da tabela estabelecimento \) citados estiver preenchidos, ou se essas datas não estiverem compreendidas no período da geração do meio magnético, deve ser verificado o Campo Data Inicial da Tela de geração do meio magnético, se a mesma estiver preenchida com o período de 01/01 \(DD/MM\), o sistema gerará para o arquivo nesse campo a indicação "0";

Caso contrário, o campo 12 do registro 0000 deverá ter a indicação “3”\.

OS2328\-RTT\-5 / __OS 2328\-RTT5\-C__

__RN143__

Alteração no registro I200

O campo 5 \(IND\_LCTO\) deve ser alterado para 2 posições e os valores válidos para o Fcont são os mencionados abaixo\.

IND\_LCTO

Tipo lançamento

Indicador do tipo de lançamento:

X – Expurgo

F – Fiscal

TR – Transferência de Saldos Fiscais Remanescentes

TF – Transferência de Saldos Fiscais

TS\- Transferência de Saldos Societários

EF – Encerramento Fiscal

IF – Inicialização de Saldo Fiscal

IS – Inicialização de Saldo Societário	

OS2328\-RTT\-5

__RN144__

Não deverá ser gerados registros I200 com o Tipo de lançamento “N” , a partir do ano\-calendário de 2010\. Esses lançamentos devem ser gerados com o IND\_LCTO =  “X”, caso na SAFX129 o campo 17 \- TIPO\_LANCTO estiver com ‘N’\.

OS2328\-RTT\-5

__RN145__

Inclusão dos campos 05 à 11 no registro M020

OS2328\-RTT\-5

__RN145\.01 a RN145\.04__

Manter a mesma forma de recuperação dos campos

OS2328\-RTT\-5

__RN145\.05__

Campo ID\_ESCR\_PER\_ANT \(CALCULADO PELO SISTEMA\)  \- Deixar o campo nulo \(gerando ‘||’\)\. Registro Calculado pelo sistema\.

OS2328\-RTT\-5

__RN145\.06__

Campo SIT\_SLD\_PER\_ANT  \(PREENCHIDO PELO SISTEMA\) \- Deixar o campo nulo \(gerando ‘||’\)\. Registro preenchido pelo sistema\.

OS2328\-RTT\-5

__RN145\.07__

Campo IND\_LCTO\_INI\_SLD \(PREENCHIDO PELO SISTEMA\) \- Deixar o campo nulo \(gerando ‘||’\)\. Registro preenchido pelo sistema\.

OS2328\-RTT\-5

__RN145\.08__

Campo FORM\_APUR informação contida no campo IND\_PERIODIC da tabela FCONT\_MAN\_LUCROC\. Se a informação for A00 deve ser informado A no campo 8 \(FORM\_APUR\) do registro M020\. Caso a informação seja T01, T02, T03 ou T04 deve ser informado T\.

OS2328\-RTT\-5

__RN145\.09__

Campo FORM\_TRIBUT  \- 

Deverá ser recuperado da tela Manutenção > Lucro/Prejuízo contábil, campo ‘Forma Tributação’, sendo valores válidos:

‘1’\- Real

‘2’ \- Real Arbitrado

’3’\- Real Presumido \(Trimestral\)

’4’ \- Real Presumido Arbitrado \(Trimestral\)

Para o período de apuração trimestral, todos os trimestres deverão ter a mesma forma de tributação, caso, seja diferente considerar na geração do M020 a forma de tributação informada no ultimo trimestre\.

 

OS2328\-RTT\-5

__RN145\.10__

Campo TRIM\_LUC\_ARB

Deverá ser recuperado da tela Manutenção > Lucro/Prejuízo contábil, campo ‘Trimestre do Lucro Arbitrado’, sendo valores válidos:

‘0 ’ \(sem Lucro Arbitrado\)  

 ‘1’ \(com Lucro Arbitrado\)\.

Só será gerado com informação, se a apuração for Trimestral e o tipo da Tributação for Real Arbitrado ou Real Presumido Arbitrado \(Trimestral\), caso contrário o campo 10 do registro M020  será gerado ‘||’\.

Caso a forma seja Trimestral e o tipo da Tributação for Real Arbitrado ou Real Presumido Arbitrado \(Trimestral\),  o campo deverá ser gerado de acordo com o campo ‘Trimestre do Lucro Arbitrado’ da tela Manutenção > Lucro/Prejuízo contábil, sendo:

Campo de 04 posições,  cada uma representa um trimestre do Ano que deverá ser preenchido com ‘0 ’ \(sem Lucro Arbitrado\)  ou ‘1’ \(com Lucro Arbitrado\)\.

Exemplos:

Escrituração sem lucro Arbitrado: ‘0000’

Lucro Arbitrado no segundo trimestre: ’ 0100’

Lucro Arbitrado no terceiro e quarto trimestre:  ‘0011’

OS2328\-RTT\-5

__RN145\.11__

Campo FORM\_TRIB\_TRI

Se a forma de apuração da tela Manutenção > Lucro/Prejuízo contábil, for anual gerar o campo 11 do registro M020  ‘||’\.

Caso a forma seja Trimestral, o campo deverá ser gerado de acordo com o campo ‘Apuração do Trimestre’ da tela Manutenção > Lucro/Prejuízo contábil, sendo:

Campo de 04 posições,  cada uma representa um trimestre do Ano que deverá ser preenchido com: ‘0’  \- Fora do período da escrituração,  ‘1’ – Real, ‘2’ – Arbitrado, ‘3’ – Presumido \(Somente Trimestral\) e ‘4’ Inativo \(Somente Trimestral\)\.

Considere Inativo, quando não há movimentação no ano \(os quatro trimestres sem valor\)\.

Considere fora do período da escrituração quando não houver valor em pelo menos um dos quatro trimestres\.

Exemplos:

Forma de apuração anual com forma de tributação Lucro Real em todos os trimestres: “1111”

Forma de apuração anual com forma de tributação Arbitrada no segundo e terceiro trimestre: “1221”

Forma de apuração Trimestral com forma de tributação Presumida no primeiro e segundo trimestre: “3311”

Período de escrituração com término no terceiro trimestre com forma de apuração anual com forma de tributação Lucro Real: “1110”\.

OS2328\-RTT\-5

__RN146__

Deixar de gerar o campo 03 – IND\_CALC\_ESTIM do registro M030 

OS2328\-RTT\-5

__RN147__

Deixar de gerar o campo 04 – FORM\_TRIB\_TRI do registro M030 

OS2328\-RTT\-5

__RN148__

A partir do ano\-calendário 2010, a geração do FCONT deve considerar a versão 3\.00 da SAFX2101\.

Esta nova versão não deverá impactar os demais módulos \(SPED\-Contábil e Obrigações Municipais\), ou seja, apenas deverá ser considerada a parametrização da versão 1\.00\.

OS2328\-RTT\-5

__RN149__

Alteração no log da geração do FCONT:

\- O sistema deverá verificar se há algum lançamento na X129 sem a informação do tipo de lançamento, caso seja encontrado deverá emitido a seguinte msg:

Tipo I200/I250 \- Lançamento Contábil será desconsiderado na geração dos registros, pois o tipo do lançamento não está preenchido\. Estab \- Data Lancto \- Cod\. Conta \- Arquiv\. = <chave>  Localização: FCONT \-> Manutenção \-> Lançamentos Contábeis e/ou Fiscais\.

\- Deverá ter um tratamento caso o cliente tenha importado um tipo de lançamento não permitido no layout, emitindo a seguinte msg:

Tipo I200/I250 \- Lançamento Contábil será desconsiderado na geração dos registros, pois o tipo de lançamento não é permitido para o layout\.

OS2328\-RTT\-5

__RN150__

Criar a opção “Ajuste de Centro de Custo \(Registros I156,I256 e I356\)” dentro do Menu: Manutenção, a estrutura do Menu ficará da seguinte forma:

__Manutenção: __

__Lançamentos Contábeis e/ou Fiscais__

__Plano de Contas Referencial X Plano de Contas Empresa__

__Lucro /Prejuízo Contábil __

__Ajuste de Centro de Custo \(Registros I156,I256 e I356\)__

OS2328\-RTT\-5B

__RN151__

Criar a tela “ Parametrização da Conta Empresarial X Centro de Custo X Conta Referencial” no Módulo SPED / FCONT – Controle Fiscal Contábil de Transição, Menu: Manutenção / Ajuste de Centro de Custo \(Registros I156, I256 e I356\)\.

Estrutura:

__Manutenção: __

__Lançamentos Contábeis e/ou Fiscais__

__Plano de Contas Referencial X Plano de Contas Empresa__

__Lucro /Prejuízo Contábil __

__Ajuste de Centro de Custo \(Registros I156,I256 e I356\)__

__                  Parametrização da Conta Empresarial X Centro de Custo X Conta Referencial__

__Regras de validações:__

__RT00 __– A pesquisa do grupo deverá seguir o mesmo conceito da pesquisa da tela  “Plano de Contas Referecial X Plano de Contas da Empresa”\.

__RT01__ – Campo Conta: Será recuperado da safx2002

__RT02__ \- Campo Custo: Será recuperado da safx2003

__RT03 __–  Campo Entidade Responsável: Mostra a entidade responsável que está configurada nos Dados Iniciais

__RT04__ – Campo Versão – Será exibido à versão do plano de contas referencial\. Neste caso, apenas a versão 3\.00 deverá ser visualizada\.

__RT05__ – Referencial: Será recuperado da tfix64, filtrando apenas contas analíticas 

__RT06 __– Incluir o botão abrir na barra de ação\. Na janela de seleção, o usuário irá visualizar a Conta/Descrição e Centro de Custo/Descrição\.

OS2328\-RTT5B

__RN152__

Criar a tela “ Rateio dos Saldos \(Origem SAFX80\) – Registro I156” no Módulo SPED / FCONT – Controle Fiscal Contábil de Transição, Menu: Manutenção / Ajuste de Centro de Custo \(Registros I156, I256 e I356\)\.

Estrutura:

__Manutenção: __

__Lançamentos Contábeis e/ou Fiscais__

__Plano de Contas Referencial X Plano de Contas Empresa__

__Lucro /Prejuízo Contábil __

__Ajuste de Centro de Custo \(Registros I156,I256 e I356\)__

__                        Parametrização da Conta Empresarial X Centro de Custo X Conta Referencial__

__                        Rateio dos Saldos \(Origem SAFX02\) – Registro I156__

__                        Rateio dos Saldos \(Origem SAFX80\) – Registro I156__

__Regras de validações:__

#### <a id="_Toc305510363"></a>RT00 – Não será permitido incluir novos saldos nesta tela\. Apenas será permitido consultar os saldos já existentes na SAFX80\.

__RT01 –__ Ficará disponível para consulta, apenas os saldos que estão cadastrados na SAFX80, cuja conta contábil e o centro de custo estejam parametrizados na tela “Parametrização da Conta Empresarial X Centro de Custo X Conta Referencial“\.

__RT02__ – As contas Referenciais serão recuperadas da tela “Parametrização da Conta Empresarial X Centro de Custo X Conta Referencial”  dentro do Módulo: FCONT, Menu:  “Manutenção / Ajuste de Centro de Custo \(Registros I156,I256 e I356\)\. 

Após o usuário consultar o saldo, o sistema exibirá automaticamente  todas as contas referenciais que estão parametrizadas na tela “Parametrização da Conta Empresarial X Centro de Custo X Conta Referencial”\. O usuário deverá informar apenas o valor rateado por referencial\. 

__RT03 \- __A tela deverá fazer a seguinte consistência:

01 – Verificar se a soma dos valores informados nas contas referencias atingiu ou não o valor do saldo final\. Caso não tenha atingido a msg abaixo deve ser mostrada ao usuário: 

O total dos valores informados nas contas referenciais não bate com o valor do Saldo Final\. Deseja gravar o registro?

A MSG é apenas um aviso, o usuário terá a opção de gravar as informações desta maneira\. Se selecionar Sim, as informações serão gravadas e se selecionar Não, o registro não será gravado e as informações digitadas até o momento não serão perdidas\.

__RT04:  __Para a validação da RT03, o sistema deverá fazer o seguinte processo internamente: somar todos os valores do campo de Crédito e Somar todos os campos de Débitos\. Subtrair os resultados \(totais de créditos \- totais de débitos\) e verificar se o valor é igual ao do lançamento\.

Se existir qualquer diferença \(de saldo, ou indicador\), a mensagem de aviso da RT03 deve ser exibida para o usuário\.

OS2328\-RTT5B

__RN153__

Criar a tela “ Rateio dos Lançamentos \(Origem SAFX129\) – Registro I256” no Módulo SPED / FCONT – Controle Fiscal Contábil de Transição, Menu: Manutenção / Ajuste de Centro de Custo \(Registros I156, I256 e I356\)\.

Estrutura:

__Manutenção: __

__Lançamentos Contábeis e/ou Fiscais__

__Plano de Contas Referencial X Plano de Contas Empresa__

__Lucro /Prejuízo Contábil __

__Ajuste de Centro de Custo \(Registros I156,I256 e I356\)__

__                        Parametrização da Conta Empresarial X Centro de Custo X Conta Referencial__

__                        Rateio dos Saldos \(Origem SAFX02\) – Registro I156__

__                        Rateio dos Saldos \(Origem SAFX80\) – Registro I156__

__                        Rateio dos Lançamentos \(Origem SAFX129\) – Registro I256__

__Regras de validações:__

#### <a id="_Toc305510365"></a>RT00 – Não será permitido incluir novos lançamentos nesta tela\. Apenas será permitido consultar os lançamentos já existentes na SAFX129\.

__RT01 –__ Ficará disponível para consulta, apenas os lançamentos que estão cadastrados na SAFX129, cuja conta contábil e o centro de custo estejam parametrizados na tela “Parametrização da Conta Empresarial X Centro de Custo X Conta Referencial“\.

__RT02__ – Referencial será recuperado da tela “Parametrização da Conta Empresarial X Centro de Custo X Conta Referencial”  dentro do Módulo : FCONT , Menu:  “Manutenção / Ajuste de Centro de Custo \(Registros I156,I256 e I356\)\. 

Após o usuário consultar o lançamento, o sistema exibirá automaticamente  todas as contas referenciais que estão parametrizadas na tela “Parametrização da Conta Empresarial X Centro de Custo X Conta Referencial”\. O usuário deverá informar apenas o valor rateado por referencial\. 

__RT03__: A tela deverá fazer a seguinte consistência:

01 – Verificar se a soma dos valores informados nas contas referencias atingiu ou não o valor do lançamento\. Caso não tenha atingido a msg abaixo deve ser mostrada ao usuário: 

O total dos valores informados nas contas referenciais não bate com o valor do Lançamento\. Deseja gravar o registro?

A MSG é apenas um aviso, o usuário terá a opção de gravar as informações desta maneira\. Se selecionar Sim, as informações serão gravadas e se selecionar Não, o registro não será gravado e as informações digitadas até o momento não serão perdidas\.

OS2328\-RTT5B

__RN154__

Criar a tela “ Rateio dos Lançamentos \(Origem SAFX01\) – Registro I356” no Módulo SPED / FCONT – Controle Fiscal Contábil de Transição, Menu: Manutenção / Ajuste de Centro de Custo \(Registros I156, I256 e I356\)\.

Estrutura:

__Manutenção: __

__Lançamentos Contábeis e/ou Fiscais__

__Plano de Contas Referencial X Plano de Contas Empresa__

__Lucro /Prejuízo Contábil __

__Ajuste de Centro de Custo \(Registros I156,I256 e I356\)__

__                        Parametrização da Conta Empresarial X Centro de Custo X Conta Referencial__

__                        Rateio dos Saldos \(Origem SAFX02\) – Registro I156__

__                        Rateio dos Saldos \(Origem SAFX80\) – Registro I156__

__                        Rateio dos Lançamentos \(Origem SAFX129\) – Registro I256__

__                        Rateio dos Lançamentos de Encerramento  \(Origem SAFX01\) – Registro I356__

__Regras de validações:__

#### <a id="_Toc305510367"></a>*RT00 – Não será permitido incluir novos lançamentos nesta tela\. Apenas será permitido consultar os lançamentos já existentes na SAFX01 \(do tipo Encerramento\)*

__RT01 –__ Ficará disponível para consulta, apenas os lançamentos  do tipo Encerramento que estão cadastrados na SAFX01, cuja conta contábil e o centro de custo estejam parametrizados na tela “Parametrização da Conta Empresarial X Centro de Custo X Conta Referencial“\.

__RT02__ – Referencial será recuperado da tela “Parametrização da Conta Empresarial X Centro de Custo X Conta Referencial”  dentro do Módulo : FCONT , Menu:  “Manutenção / Ajuste de Centro de Custo \(Registros I156,I256 e I356\)\. 

Após o usuário consultar o lançamento, o sistema exibirá automaticamente  todas as contas referenciais que estão parametrizadas na tela “Parametrização da Conta Empresarial X Centro de Custo X Conta Referencial”\. O usuário deverá informar apenas o valor rateado por referencial\. 

__RT03 \- __A tela deverá fazer a seguinte consistência:

01 – Verificar se a soma dos valores informados nas contas referencias atingiu ou não o valor do lançamento\. Caso não tenha atingido a msg abaixo deve ser mostrada ao usuário: 

O total dos valores informados nas contas referenciais não bate com o valor do Lançamento\. Deseja gravar o registro?

A MSG é apenas um aviso, o usuário terá a opção de gravar as informações desta maneira\. Se selecionar Sim, as informações serão gravadas e se selecionar Não, o registro não será gravado e as informações digitadas até o momento não serão perdidas\.

OS2328\-RTT5B

__RN155__

Gerar um registro I050, para cada conta contábil que está parametrizada na tela “__Parametrização da Conta Empresarial X Centro de Custo X Conta Referencial__”, desde que haja informações desta conta  \(__para o estabelec*imento e * período da geração do arquivo__\) em um lançamento ou saldo em uma das telas abaixo:__                        __

__\- Rateio dos Saldos \(Origem SAFX80\) – Registro I156__

__\- Rateio dos Lançamentos \(Origem SAFX129\) – Registro I256__

__\- Rateio dos Lançamentos de Encerramento  \(Origem SAFX01\) – Registro I356__

OS2328\-RTT5B

__RN156__

Gerar um registro I051, para cada conta referencial que está parametrizada na tela “__Parametrização da Conta Empresarial X Centro de Custo X Conta Referencial__” \(quando o registro pai – I050 existir\)\.

OS2328\-RTT5B

__RN157__

Gerar um registro I100, para cada centro de custo que está parametrizado na tela “__Parametrização da Conta Empresarial X Centro de Custo X Conta Referencial” __\(quando o registro pai – I050 existir\)\.

OS2328\-RTT5B

__RN158__

<a id="REG_I156"></a>Inclusão do REGISTRO I156 – MAPEAMENTO REFERENCIAL DOS TOTAIS DÉBITOS E CRÉDITOS

ATENÇÃO: Este registro é obrigatório quando existir mais de um registro I051 linha \(2 e 3\) para mesma conta empresa linha \(1\) \(campo 06 do registro I050\) e vinculado ao  mesmo centro de custo \(campo 3 do I051\)\.

Para geração do registro I156, deve ser seguido a seguinte regra:

Será gerado um registro para cada conta referencial que está cadastrada na  tela__ ‘ Rateio dos Saldos \(Origem SAFX80\) – Registro I156’__, desde que, as contas tenham valor diferente de zero \(em pelo menos um dos campos Valor Débito ou Valor Crédito\)\. 

__Importante: __Se existir mais de um saldo \(na safx80\), para o mesmo ano, conta contábil e centro de custo, o sistema deverá agrupar os valores gerando apenas 1 registro para cada referencial\.

Exemplo de RN para geração:

1    |I050|31122007|03|A|5|teste|TESTE1|AJUSTE FCONT|

2    |I051|10|XXX|3\.01\.01\.07\.01\.02\.01|

3    |I051|10|XXX|5\.01\.01\.05\.00|

Exemplo arquivo que deve ser gerado:

|I150|01012010|31122010|

|I155| teste |XXX|56500,00|C|5565,00|0,00|50935,00|C|

|I156|3\.01\.01\.07\.01\.02\.01|5265,00|0,00|

|I156|5\.01\.01\.05\.00|3000,00|0,00|

OS2328\-RTT\-5B

__RN158\.01__

Campo  \-  REG

Gravar no campo 01 – REG o texto fixo  “I156”

OS2328\-RTT\-5B

__RN158\.02__

Campo  \- COD\_CTA\_REF

\- Regra para a recuperação do campo:

 

\- Origem SAFX80:  

Utilizar a conta referencial informada na tela: Rateio dos Saldos \(Origem SAFX80\) – Registro I156, que tiver valor diferente de zero\.

OS2328\-RTT\-5B

__RN158\.03__

Campo \- VL\_DEB

Origem SAFX80:

Gravar no campo 03 – VL\_DEB  a informação contida no campo Valor do Débito,da Conta Referencial da nova tela Rateio dos Saldos \(Origem SAFX80\) – Registro I156  

OS2328\-RTT\-5B

__RN158\.04__

Campo \- VL\_CRED

Origem SAFX80:

Gravar no campo 04 – VL\_CRED a informação contida no campo Valor de Crédito  da Conta Referencial da nova tela Rateio dos Saldos \(Origem SAFX80\) – Registro I156  

OS2328\-RTT\-5B

__RN159__

Inclusão do REGISTRO <a id="REG_I251"></a>I256 – MAPEAMENTO REFERENCIAL DAS PARTIDAS DO LANÇAMENTO

ATENÇÃO: Este registro é obrigatório quando existir mais de um registro I051  para mesma conta empresa \(campo 06 do registro I050\) , vinculado ao  mesmo centro de custo \(campo 3 do I051\)\.

Para geração do registro I256, deve ser seguido a seguinte regra:

Será gerado um registro para cada conta referencial que está cadastrada nas  telas __ ‘ Rateio dos Lançamentos \(Origem SAFX129\) – Registro I256’ desde que, as contas tenham valor diferente de zero\.__

Exemplo de RN para geração:

1    |I050|31122007|03|A|5|teste|TESTE1|AJUSTE FCONT|

2    |I051|10|XXX|3\.01\.01\.07\.01\.02\.01|

3    |I051|10|XXX|5\.01\.01\.05\.00|

Exemplo arquivo que deve ser gerado:

|I200|1515|01012011|20000,00|F|

|I250|teste|XXX|10000,00|C|arq01|01|credito \- 01||

|I256|3\.01\.01\.07\.01\.02\.01|10000,00|C|

|I256|5\.01\.01\.05\.00|10000,00|C|

OS2328\-RTT\-5B

__RN159\.01__

Campo  \-  REG

Gravar no campo 01 – REG o texto fixo  “I256”

OS2328\-RTT\-5B

__RN159\.02__

Campo  \- COD\_CTA\_REF

Gravar no campo 02 \- COD\_CTA\_REF a informação contida  na tela: Rateio dos Lançamentos \(Origem SAFX129\) – Registro I256, que tiver valor diferente de  zero\. 

OS2328\-RTT\-5B

__RN159\.03__

Campo \- VL\_DC

Gravar no campo 04 – VL\_DC a informação contida no campo Valor  da Conta Referencial da nova tela ‘Rateio dos Lançamentos \(Origem SAFX129\) – Registro I256’

OS2328\-RTT\-5B

__RN159\.04__

IND\_DC

Gravar no campo 05 – IND\_DC a informação contida no campo IND\_DEB\_CRE da tabela SAFX129 / indicador de Débito/Crédito do lançamento principal I250\.

OS2328\-RTT\-5B

__RN160__

Inclusão do REGISTRO <a id="Reg_I356"></a>I356 – MAPEAMENTO REFERENCIAL DOS TOTAIS DE DÉBITOS E CRÉDITOS DAS CONTAS DE RESULTADO ANTES DO ENCERRAMENTO

ATENÇÃO: Este registro é obrigatório quando existir mais de um registro I051  para mesma conta empresa \(campo 06 do registro I050\) , vinculado ao  mesmo centro de custo \(campo 3 do I051\)\.

Para geração do registro I356, deve ser seguido a seguinte regra:

Será gerado um registro para cada conta referencial que está cadastrada nas  telas __ ‘ Rateio dos Lançamentos de Encerramento \(Origem SAFX01\) – Registro I356’ desde que, as contas tenham valor rateado\.__

|I350|31122011|

|I355|076\.00401\.04633\.00000\.0000\.0000\.0000|06175096|50935,00|C|

|I356|4\.01\.01\.01\.04\.01\.00|50935,00|C|

OS2328\-RTT\-5B

__RN160\.01__

Campo  \-  REG

Gravar no campo 01 – REG o texto fixo  “I356”

OS2328\-RTT\-5B

__RN160\.02__

Campo \- COD\_CTA\_REF 

Gravar no campo 02 – COD\_CTA\_REF a informação contida no campo COD\_CONTA\_REF  da tabela sped\_contas\_ref 

Regra para a recuperação do campo:  Usar o código da identificação da conta \(campo ident\_conta\) da safx02, na tabela SAFX2101, para saber a identificação da conta referencial \(campo ident\_conta\_ref\)\. Usar o último código na tabela sped\_contas\_ref campo ident\_conta\_ref \. Considerar  a informação do campo COD\_CONTA\_REF da tabela sped\_contas\_ref no campo 02 do registro I356\.

OS2328\-RTT\-5B

__RN160\.03__

Campo \- VL\_CTA

Gravar no campo 03 – VL\_CTA  a informação contida no campo Valor da Conta Referencial da nova tela ‘Ajuste de Centro de Custo \(Registros I156, I256 e I356\)’ , aba I356\.

Deverá ser criado um registro I356 para cada conta referencial\.

OS2328\-RTT\-5B

__RN160\.04__

Gravar no campo 04 – IND\_DC inverso da informação contida no campo IND\_DEB\_CRE da tabela SAFX01 / inverso do indicado da nova tela de Ajuste de Centro de Custo \(Registros I156,I256 e I356\)\.

OS2328\-RTT\-5B

__RN161__

__Incluir no registro 9900 as linhas referente aos registros I156,I256 e I356__

OS2328\-RTT\-5B

__RN163__

Devera ser gerado um lançamento contábil na tabela X129, que atendam aos critérios abaixo:

__ 1 – Empresa__= login

__2 – Estabelecimento__

Deverá apresentar os estabelecimentos da empresa em questão, demonstrando se é centralizado ou descentralizado\.

Ex\.: Centralizado \- Estabelecimento

                    Descentralizado – Estabelecimento

Obs\.: Mesmo conceito do modulo geração do meio magnético do FCONT

__3 – Exercício__

Deve ser gerado somente se o exercício informado for superior a 2010, verificar o campo DATA\_OPERACAO X129 verificar lançamentos que compreenda o ano base de 2010 \(01/01/2010 à 31/12/2010\)

__4 \- Gera lançamentos de encerramento \(tipo EF\) automaticamente:__ 

Esta opção deve estar marcada na tela

__5 \- Deve ser verificado se a conta é uma conta de resultado__

Verificar campo IDENT\_CONTA na X129, com este numero de conta consultar na tabela x2002 campo 

IND\_NATUREZA= 8,3 e 4

__6 \- Verificar o tipo do lançamento__

__6\.1 \- No campo TIPO\_LANCTO X129__

Deve estar “F” e/ou “N”

Obs\.: pode haver casos onde:

1. Na mesma conta existem vários lançamentos do tipo “F” e um único lançamento do tipo “N”
2. Na mesma conta existem vários lançamentos do tipo “N” e um único lançamento do tipo “F”
3. Na mesma conta existe apenas lançamento “F” 
4. Na mesma conta existe apenas lançamento “N” 

__6\.2 \- No campo TIPO\_ LANCTO__ 

For = “EF” devera ser verificado se pertence a conta de resultado filtrada, se a caso sim, não gerar registro para esta conta\. 

__7 \- Calculo dos valores e geração das partidas__

Primeiro deve ser __calculado a diferença dos lançamentos D \(debito\) e C \(Credito\) __para lançamentos tipo F e N, __e na sequência calcular a diferença entre F e N__, \(quando houver esses dois tipos de lançamento na mesma conta filtrada\)

Para o calculo desta diferença deve ser levado em consideração as situações abaixo, tendo __10__ possibilidades que devem ser verificadas para gerar o correto lançamento de encerramento

Se, após o calculo nos casos onde na mesma conta de resultado houver F – N = 0, não gerar lançamento tipo EF

 

__1ª Situação__

 

   

 

 

 

 

Lançamento tipo F

Lançamento tipo N

 

100,00 D

100,00 C

 

100,00 D

100,00 C

 

200,00 C

300,00 D

 

200,00 C

 

 

 

 

__Total__

__200,00 C__

__100,00 D__

__Deve ser lançado__

1º lançamento 300,00 C \(conta Patrimônio liquido\)

2º lançamento 300,00 D \(conta de resultado filtrada\)

Se o valor de F for credor e de N devedor, soma os lançamentos e gera EF da forma acima

200,00C \+ 100,00D = 300,00D \(em conta de resultado\)

 

__2ª Situação__

 

 

 

 

 

 

 

Lançamento tipo F

Lançamento tipo N

 

300,00 D

300,00 C

 

200,00 D

100,00 C

 

100,00 C

200,00 D

 

100,00 C

 

 

 

 

__Total__

__300,00 D__

__200,00 C__

__Deve ser lançado__

1º lançamento 500,00 D \(conta Patrimônio liquido\)

2º lançamento 500,00 C \(conta de resultado\)

Se o valor de F for devedor e de N credor, soma os lançamentos e gera EF da forma acima

300,00D \+ 200,00C = 500,00C \(em conta de resultado\)

OS2328 – RTT5A

__CH118345\-A__

__CH119845\_2011__

 

__3ª Situação__

 

 

 

 

 

 

Lançamento tipo F

Lançamento tipo N

 

100,00 D

400,00 C

 

100,00 D

100,00 C

 

200,00 C

200,00 D

 

200,00 C

 

 

 

 

__Total__

__200,00 C__

__300,00 C__

__Deve ser lançado__

1º lançamento 100,00 D \(conta Patrimônio liquido\)

2º lançamento 100,00 C \(conta de resultado\)

Se o valor de F for credor e de N credor, subtrai os lançamentos e gera EF da forma acima

200,00C – 300,00C = 100,00C \(em conta de resultado\)

 

__4ª Situação__

 

 

 

 

 

 

 

Lançamento tipo F

Lançamento tipo N

 

100,00 D

400,00 D

 

100,00 D

100,00 C

 

200,00 D

200,00 D

 

200,00 C

 

 

 

 

__Total__

__200,00 D__

__500,00 D__

__4ª Situação__

1º lançamento 300,00 C \(conta Patrimônio liquido\)

2º lançamento 300,00 D \(conta de resultado\)

Se o valor de F for devedor e de N devedor, subtrai os lançamentos e gera EF da forma acima

200,00D – 500,00D = 300,00D \(em conta de resultado\)

 

__5ª Situação__

 

 

Lançamento tipo F

 

 

100,00 D

 

 

100,00 D

 

 

200,00 D

 

 

200,00 C

 

 

 

 

__Total__

__200,00 D__

__ __

__5ª Situação__

1º lançamento 200,00 D \(conta Patrimônio liquido\)

2º lançamento 200,00 C \(conta de resultado 12345\)

Se houver somente lançamento do tipo F e seu saldo for Devedor, gera lançamento EF da forma acima

 

__6ª Situação__

 

 

 

 

 

 

 

 

Lançamento tipo N

 

 

400,00 D

 

 

100,00 C

 

 

200,00 D

 

 

 

 

 

 

__Total__

__ __

__500,00 D__

__6ª Situação__

1º lançamento 500,00 C \(conta Patrimônio liquido\)

2º lançamento 500,00 D \(conta de resultado\)

Se houver somente lançamento do tipo N e seu saldo for Devedor, gera lançamento EF da forma acima

 

__7ª Situação__

 

 

Lançamento tipo F

 

 

100,00 D

 

 

100,00 D

 

 

300,00 C

 

 

200,00 C

 

 

 

 

__Total__

__300,00 C__

__ __

__7ª Situação__

1º lançamento 300,00 C \(conta Patrimônio liquido\)

2º lançamento 300,00 D \(conta de resultado\)

Se houver somente lançamento do tipo F e seu saldo for Credor, gera lançamento EF da forma acima

 

__8ª Situação__

 

 

 

 

 

 

 

 

Lançamento tipo N

 

 

500,00 C

 

 

100,00 C

 

 

200,00 D

 

 

 

 

 

 

__Total__

__ __

__400,00 C__

__8ª Situação__

1º lançamento 400,00 D \(conta Patrimônio liquido\)

2º lançamento 400,00 C \(conta de resultado\)

Se houver somente lançamento do tipo N e seu saldo for Credor, gera lançamento EF da forma acima

 

__9ª Situação__

 

 

 

 

 

 

Lançamento tipo F

Lançamento tipo N

 

600,00 C

400,00 C

 

 

 

 

__Total__

__600,00 C__

__400,00 C__

__Deve ser lançado__

1º lançamento 200,00 C \(conta Patrimônio liquido\)

2º lançamento 200,00 D \(conta de resultado\)

Se o valor de F for credor e de N credor, subtrai os lançamentos e gera EF da forma acima

600,00C – 400,00C = 200,00D \(em conta de resultado\)

 

__10ª Situação__

 

 

 

 

 

 

Lançamento tipo F

Lançamento tipo N

 

600,00 D

400,00 D

 

 

 

 

__Total__

__600,00 D__

__400,00 D__

__Deve ser lançado__

1º lançamento 200,00 D \(conta Patrimônio liquido\)

2º lançamento 200,00 C \(conta de resultado\)

Se o valor de F for devedor e de N devedorr, subtrai os lançamentos e gera EF da forma acima

600,00D– 400,00D = 200,00C \(em conta de resultado\)

Após a existência dos dados acima, deve ser criado dois lançamentos \(01 crédito e 01 débito\) na X129, por conta de resultado preenchendo os campos conforme regras abaixo

__RN164__

__Campo COD\_EMPRESA \(X129\)__

1º lançamento: recuperar do lançamento filtrado

2º lançamento: recuperar do lançamento filtrado

OS2328 – RTT5A

__RN165__

__Campo COD\_ESTAB \(X129\)__

1º lançamento: recuperar do lançamento filtrado

2º lançamento: recuperar do lançamento filtrado

OS2328 – RTT5A

__RN166__

__Campo DATA\_LANCTO \(X129\)	__

1º lançamento: recuperar do lançamento filtrado

2º lançamento: recuperar do lançamento filtrado

OS2328 – RTT5A

__RN167__

__Campo IDENT\_CONTA \(X129\)__

1º lançamento: recuperar da tela lançamento automático tipo EF \(campo Conta \(Gr\./Cód\./Val\.\)

2º lançamento: recuperar o numero da conta de resultado existente

OS2328 – RTT5A

__RN168__

__Campo IND\_DEB\_CRE \(X129\)__

__1º lançamento:__ Preencher de acordo com a RN 163, \- 07

__2º lançamento: __Preencher de acordo com a RN 163, \- 07

OS2328 – RTT5A

__CH118345\-A__

__RN169__

__Campo ARQUIVAMENTO \(X129\)__

1º lançamento: recuperar do lançamento filtrado

2º lançamento: recuperar do lançamento filtrado

OS2328 – RTT5A

__RN170__

__Campo IDENT\_CONTRA\_PART \(X129\)__

1º lançamento: recuperar do lançamento filtrado

2º lançamento: recuperar do lançamento filtrado

OS2328 – RTT5A

__RN171__

__Campo IDENT\_CUSTO \(X129\)__

__ __

1º lançamento: Recuperar da SAFX2101 se houver parametrização verificando o campo 06, se não houver valores não preencher

 

2º lançamento: Recuperar da SAFX2101 se houver parametrização verificando o campo 06, se não houver valores não preencher

 

__Obs\.: Esta regra deve ser aplicada somente para versão 3\.0 da SAFX2101 e recuperar valores do centro de custo do 1º lançamento referenciado, pois pode haver casos com mais de um referencial por conta__

Desconsiderar esta regra, por conta das alterações feitas na OS 3658 \(RN190 a RN192\)

 

OS2328 – RTT5A

CH118345\-A

OS3658

__RN172__

__Campo IDENT\_DESPESA  \(X129\)__

1º lançamento: recuperar do lançamento filtrado

2º lançamento: recuperar do lançamento filtrado

OS2328 – RTT5A

__RN173__

__Campo IDENT\_HISTPADRAO \(X129\)__

1º lançamento: recuperar do lançamento filtrado

2º lançamento: recuperar do lançamento filtrado

OS2328 – RTT5A

__RN174__

__Campo IDENT\_OPERACAO  \(X129\)	__

1º lançamento: recuperar do lançamento filtrado

2º lançamento: recuperar do lançamento filtrado

OS2328 – RTT5A

__RN175__

__Campo TXT\_HISTCOMPL \(X129\)	__

1º lançamento: recuperar do lançamento filtrado

2º lançamento: recuperar do lançamento filtrado

OS2328 – RTT5A

__RN176__

__Campo VLR\_LANCTO \(X129\)__

1º lançamento: Preencher com o valor da diferença calculada conforme RN 163 \- 07

2º lançamento: Preencher com o valor da diferença calculada conforme RN 163 \- 07

OS2328 – RTT5A

__CH118345\-A__

__RN177__

__Campo COD\_INDICE\(X129\)__

1º lançamento: recuperar do lançamento filtrado

2º lançamento: recuperar do lançamento filtrado

OS2328 – RTT5A

__RN178__

__Campo VLR\_LANCTO\_CONV \(X129\)	__

1º lançamento: recuperar do lançamento filtrado

2º lançamento: recuperar do lançamento filtrado

OS2328 – RTT5A

__RN179__

__Campo NUM\_PROCESSO \(X129\)__

1º lançamento: gerado seqüencial pelo sistema

2º lançamento: gerado seqüencial pelo sistema

OS2328 – RTT5A

__RN180__

__Campo IND\_GRAVACAO \(X129\)__

1º lançamento: gerado pelo sistema __\(sugestão: poderá utilizar este indicador para deletar os lançamentos automáticos\)__

2º lançamento: gerado pelo sistema __\(sugestão: poderá utilizar este indicador para deletar os lançamentos automáticos\)__

OS2328 – RTT5A

__RN181__

__Campo NUM\_LANCAMENTO \(X129\)__

1º lançamento: recuperar do lançamento filtrado

2º lançamento: recuperar do lançamento filtrado

OS2328 – RTT5A

__RN182__

__Campo TIPO\_LANCTO \(X129\)__

1º lançamento: Preencher fixo com tipo “EF”

2º lançamento: Preencher fixo com tipo “EF”

OS2328 – RTT5A

__RN183__

__Campo IDENT\_PFJ\_EMPRESA \(X129\)	__

1º lançamento: recuperar do lançamento filtrado

2º lançamento: recuperar do lançamento filtrado

OS2328 – RTT5A

__RN184__

__Campo DATA\_PFJ\_EMPRESA \(X129\)__

1º lançamento: recuperar do lançamento filtrado

2º lançamento: recuperar do lançamento filtrado

OS2328 – RTT5A

__RN185__

Registro 0000, Campo 11: IND\_SIT\_ESP

O Indicador de situação especial deverá considerar os campos 56, 66,67 ou 68 da tabela de Estabelecimento\.

Conforme as regras abaixo:

Quando o usuário preencher o campo 66 da tabela de Estabelecimento e se a data de Cisão estiver compreendida no mesmo período de geração do meio magnético, o sistema gerará para o arquivo nesse campo a indicação "1" \(1 = Cisão\);

Quando o usuário preencher o campo 67 da tabela de Estabelecimento e  se a data de Fusão estiver compreendida no mesmo período de geração do meio magnético, o sistema gerará para o arquivo nesse campo a indicação "2" \(2 = Fusão\);

Quando o usuário preencher o campo 68 da tabela de Estabelecimento e se a data de Incorporação estiver compreendida no mesmo período de geração do meio 

magnético, o sistema gerará para o arquivo nesse campo a indicação"3"; \(  3  = Incorporação\)

Quando o usuário preencher o campo 56 da tabela de Estabelecimento e se a data de Encerramento estiver compreendida no mesmo período de geração do meio magnético,  o sistema gerará para o arquivo nesse campo a indicação "4" \(4  = Encerramento\);

Caso as datas citadas acima estiverem preenchidas e compreendidas no período considerar sempre a maior data \(que deverá ser a data referente à Cisão, Fusão, Incorporação ou Encerramento\)\.

Se nenhum dos campos  de data \(da tabela estabelecimento \) citados estiver preenchido, ou se essas datas não estiverem compreendidas no período da geração do meio magnético, o campo 11 do registro 0000 deverá ser gerado ’||’\. 

Esta regra se aplica apenas ao leiaute 2011 do FCONT\.

CH118158

__RN186__

Se a informação “Omitir informação Centro de Custo em lançamentos Contábeis e Saldos” estiver selecionado/marcado em Dados Iniciais, desconsiderar a informação centro de custo nos registros a serem gerados, procedendo da forma descrita abaixo:

\- Nos registros: I155\-Detalhes dos Saldos Contábeis, I250\-Partidas do lançamento, I355\-Detalhes dos Saldos das Contas de Resultado Antes do Encerramento não destacar informação do centro de custo\. 

Importante: As informações das contas e referenciais devem ser geradas normalmente, mesmo quando a opção estiver marcada\. Ou seja, será necessário gerar as informações das contas e referenciais \(I050,I051\), omitindo apenas o centro de custo \(I100\)\.

Caso  a informação “Omitir informação Centro de Custo em lançamentos Contábeis e Saldos” estiver desmarcado em Dados Iniciais, se existir centro de custo cadastrado no de/para e nos lançamentos e saldos, o mesmo deverá ser gerado no arquivo\.

Esta regra se aplica para os leiautes versão 1\.0\.0 e  2011 do FCONT\.

CH119128

__RN187__

__Alteração da tela __

Módulo: SPED > FCONT

Menu: Geração > Meio Magnético

Incluir na tela da Geração do Meio Magnético :

 \- o parâmetro: Situação Especial \(Cisão, Fusão, Incorporação ou Encerramento\) no período\. \*

\- os campos: Valor do Lucro/Prejuízo Antes da data da Situação Especial, Indicador\.

\- o texto: Quando existir Situação Especial para o Ano\-Calendário de 2010, o sistema irá gerar automaticamente, os dois arquivos \(o primeiro com data até a data da Situação Especial , com o leiaute versão 1\.0 e o segundo com data posterior a da situação especial, usando o leiaute 2011 do FCONT\)\.

RT00: Só será incluso o parâmetro: __Situação Especial \(Cisão, Fusão, Incorporação ou Encerramento\) no período\. __\* , os campos__ Valor do Lucro/Prejuízo Antes da data da Situação Especial, Indicador __e o texto__ Quando existir Situação Especial para o Ano\-Calendário de 2010, o sistema irá gerar automaticamente, os dois arquivos \(o primeiro com data até a data da Situação Especial , com o leiaute versão 1\.0 e o segundo com data posterior a da situação especial, usando o leiaute 2011 do FCONT\), __quando for informado pelo usuário o período de 2010 na data inicial e final da tela da geração do Meio Magnético

RT01: Após ter marcado o parâmetro __Situação Especial \(Cisão, Fusão, Incorporação ou Encerramento\) no período\. \*__, os campos__ Valor do Lucro/Prejuízo Antes da data da Situação Especial, Indicador__ serão habilitados\.

RT02: O campo indicador terá as seguintes características:

Valores válidos as opções: Lucro e Prejuízo\.

RT03: O campo Valor do Lucro/Prejuízo Antes da data da Situação Especial terá as seguintes características:

Tipo: Number 

Tamanho: 15 posições

__OS 2328\-RTT5\-C__

__RN188__

Existe uma exceção para as regras RN141, RN144 e RN148 onde:

Na geração do meio magnético, se o cliente possuir uma situação especial \(campo 11 do registro 0000\) igual a 1,2, 3 ou 4 o sistema deve proceder da seguinte maneira:

Verificar se a data da geração do arquivo está compreendida no ano de 2010:

Em caso afirmativo:  Verificar a data da situação especial, campos 56, 66, 67 e 68 da tabela de Estabelecimento e efetuar duas gerações dos arquivos sendo eles:

1º arquivo: com data até a data da situação especial\. Neste caso, o leiaute a ser considerado é a Versão 1\.0\.0 do FCONT

2º arquivo com data após a data da situação especial\. Neste caso, o leiaute a ser considerado é o de 2011 

Caso exista mais de uma das datas preenchidas durante o mesmo ano, considere a maior delas entre as opções cisão, fusão e incorporação\.

Se existir pelo menos duas datas preenchidas e uma delas \(no caso a maior\), for a de encerramento, gere apenas o 1º arquivo, considerando a data de encerramento\.

__OS 2328\-RTT5\-C__

__188\.01__

Para a 1ª geração: Mesmo que existentes na SAFX129 desconsiderar na geração os lançamentos dos tipos EF, IS, IF, TS, TF, TR e  X \(os expurgos, neste caso, deverão ser gerados  como N\) e também os registros I156, I256 e I356\.

Será necessário utilizar a versão 1\.0 do plano de contas referencial  da SAFX2101\.

Os registros 0000,I150,I250 e I350 deverão ser gerados considerando a data inicial \(informada na tela da geração do meio magnético até a data da situação especial, informada na tabela de estabelecimento\.

O registro 0000 deverá ser gerado com o campo 11 preenchido com uma das opções \(1 = Cisão, 2 = Fusão, 3  = Incorporação ou 4  = Encerramento\.

O valor do Lucro/Prejuízo que será informado no registro M030 deve recuperar da tela da geração do Meio Magnético os novos campos inclusos \(“Valor do Lucro/Prejuízo até a data da Situação Especial” e o seu “Indicador”\)\.

A nomenclatura do arquivo deve ficar da seguinte maneira: Estabelecimento\_datainicial\_datafinal\_FCONT\.txt

Onde a data Inicial é a data informada no campo Data Inicial da tela da Geração do Meio Magnético e data Final , será a data da situação especial\.

Exemplificando:

Uma empresa \(001\)  teve uma cisão em 15/10/10\. Será necessário entregar o 1º arquivo  com data de 01/01/2010 à 15/10/10 \(utilizando o leiaute antigo, versão 1\.0\.0 \) com a seguinte nomenclatura: 0001\_01012010\_15102010\_FCONT\.TXT\.

__OS 2328\-RTT5\-C__

__188\.02__

Para a 2ª geração: considerar na geração dos registros EF automáticos apenas os lançamentos com data posterior a data da situação especial\.

Os registros 0000,I150,I250 e I350 deverão ser gerados considerando a data inicial a data posterior informada da situação especial \(tela do estabelecimento\) e a data Final  é a data informada no campo Data Final da tela da Geração do Meio Magnético\.

O registro 0000 deverá ser gerado com o campo 11 nulo, ou seja “||” e o campo 12 será a opção 2 \- Resultante de Cisão/Fusão ou  remanescente de Cisão ou realizou Incorporação\.

O valor do Lucro/Prejuízo que será informado no registro M030 deve recuperar da tela do Lucro/Prejuízo Contábil\.

A nomenclatura do arquivo deve ficar da seguinte maneira: Estabelecimento\_datainicial\_datafinal\_FCONT\.txt

Onde a data Inicial será a data posterior da data informada da situação especial \(tela do estabelecimento \) e a data Final será a data informada no campo Data Final da tela da Geração do Meio Magnético\.

Exemplificando:

Uma empresa \(001\)  teve uma cisão em 15/10/10\. Será necessário entregar o segundo arquivo com data de 16/10/10 à 31/12/2010 \(utilizando o leiaute 2011\) com a nomenclatura 0001\_16102010\_31122010\_FCONT\.TXT\.

__OS 2328\-RTT5\-C__ 

__RN189__

Deve ser apresentado para cada conta contábil \(inclusive para as suas alterações, quando existir\), um registro I050, na geração do FCONT\. As alterações que  ocorrerem antes ou após o ano da geração do arquivo do FCONT, não deve ser informada neste período do arquivo\.

Para as contas que possuírem mais de um registro \(ou seja, que tiveram alteração\), devem ser gerados os registros I051, com base no cadastro da X2101 \(quando configurado\)\.

Alterado CH11942

Deve ser apresentado para cada conta contábil \(inclusive para as suas alterações, quando existir\), um registro I050, na geração do FCONT\. As alterações que  ocorrerem antes ou após o ano da geração do arquivo do FCONT, não deve ser informada neste período do arquivo\.

Para as contas que possuírem mais de um registro \(ou seja, que tiveram alteração\), devem ser gerados os registros I051, com base no cadastro da X2101 \(quando configurado\), considerando somente um I051 para cada I050 gerado\.

Exemplo: 

Considerando a geração do FCONT do exercício de 2010 e que existam lançamentos da conta X durante este exercício\.

A Conta Contábil X teve várias alterações \(descrição\):

Cadastro

Conta\-Contábil

Descrição

Criação/Alteração

01

X

Desc1

01/01/2009

02

X

Desc2

01/11/2009

03

X

Desc3

01/05/2010

04

X

Desc4

01/10/2010

05

X

Desc5

01/07/2011

Deve ser exibido um registro I050 para cada inclusão/alteração \(com exceção dos cadastros 01 e 05\)\. Caso exista a configuração do plano de contas referencial, o mesmo deve ser apresentado embaixo de cada I050 \(referente a esta conta\), que foi apresentado no arquivo\.

O arquivo seja exibido da seguinte forma:

|I050|01112009|02|A|5|X|2132|Desc2|

|I051|10||2\.01\.01\.03\.02|

|I050|01052010|02|A|5|X|2132|Desc3|

|I051|10||2\.01\.01\.03\.02|

|I050|01102010|02|A|5|X|2132|Desc4|

|I051|10||2\.01\.01\.03\.02|

__CH120094__

__CH11942__

__RN190__

Com relação aos lançamentos de encerramento automático \(criados através da OS2328\-RTT5A, no Módulo:\.SPED / FCONT – Controle Fiscal Contábil de Transição, Menu: Geração / Lançamentos \(Tipo EF\)\), devem considerar como quebra a conta \+ centro de custo, para efetuar o calculo informado no item 7 da RN163\. Essa alteração deve ser feita apenas quando os lançamentos possuírem as informações por conta e centro de custo, caso contrário NADA deve ser alterado\.

Exemplos:

|I050|01012009|04|A|1|800800||CONTA RESULTADO IND 8|

|I051|10|123|3\.05\.01\.03\.01\.00\.00|

|I051|10|456|3\.05\.01\.03\.01\.00\.00|

|I100|10012009|123|123|

|I100|10012009|456|456|

|I200|1|05012010|1000,00|F|

|I250|44588||1000,00|C|TESTE 1||TESTE 1||

|I250|800800|123|1000,00|D|TESTE 1||TESTE 1||

|I200|39|23012010|5200,00|F|

|I250|44588||5200,00|C|TESTE FISCAL||TESTE FISCAL||

|I250|800800|123|5200,00|D|TESTE FISCAL||TESTE FISCAL||

|I200|9|31122010|6200,00|EF|

|I250|200200||6200,00|D|EF\-Automatico2||utomático de encerramento utomático||

|I250|800800|123|6200,00|C|EF\-Automatico2||utomático de encerramento utomático||

Obs\. A informação do Centro de Custo deve levar em consideração o Centro de Custo cadastrado na SAFX129 e não na SAFX2101\.

__OS3658__

__RN191__

Se a informação __“Omitir informação Centro de Custo em lançamentos Contábeis e Saldos”__ estiver selecionado/marcado em Dados Iniciais, não deve ser gerado o centro de custo na geração dos registros EF\.

Neste caso, o centro de custo, mesmo que existente nos lançamentos, não serão considerados na geração dos lançamentos de encerramento automático\.

__Exemplo para a geração dos Lançamentos Automático:__

 

Se existir na base 3 lançamentos para uma conta X com centro de custo: 

estab       Lançamento            conta       deb/cred                                cc                     valor            tipo       
1              30/12/2010            40408          C             teste                  13261               150,00             F  
1              31/12/2010            40408          C             teste                  80880               1000 ,00          N  
1              29/12/2010            40408          C             teste                  13261               250,00             F

e o paramentro “Omitir informação Centro de Custo em lançamentos Contábeis e Saldos” estiver Marcado, iremos considerar apenas a conta não importando o centro de custo para fazer o cálculo \(conforme RN163\)

  
1              31/12/2010            40408          C             EF\-Automatico1                           600,00         EF  
1              31/12/2010            40425          D             EF\-Automatico1         1                600 ,00        EF

Se o parâmetro “Omitir informação Centro de Custo em lançamentos Contábeis e Saldos” estiver desmarcado consideramos a quebra conta \+  centro de custo e neste caso teremos:  
1              31/12/2010            40408     D             EF\-Automatico1     13261                  400,00         EF  
1              31/12/2010            40425     C             EF\-Automatico1         1                      400,00         EF  
1              31/12/2010            40408     C             EF\-Automatico2      80880               1000,00         EF  
1              31/12/2010            40425     D             EF\-Automatico2         1                   1000,00         EF

__Na__ __Geração do Meio Magnético teremos uma validação com relação ao Parâmetro __“Omitir informação Centro de Custo em lançamentos Contábeis e Saldos”, para garantirmos que o usuário não fez alteração no utomátic após a geração dos lançamentos automáticos\. Seguindo as regras abaixo:

Ao gerar o arquivo EF automático, o campo txt\_histcompl deve indicar se o registro foi gerado com o parâmetro “Omitir informação Centro de Custo em lançamentos Contábeis e Saldos” marcado ou não\. Neste caso gravamos a seguinte informação no campo:

Parâmetro marcado: “utomático de encerramento utomático por conta”

Parâmetro desmarcado: “utomático de encerramento utomático por conta e centro de custo”

Na geração do meio magnético, o sistema deve comparar se o parâmetro “Omitir informação Centro de Custo em lançamentos Contábeis e Saldos”, está compatível com a informação que foi marcado na tabela quando da geração automática dos lançamentos de encerramento \(de pelo menos 1 registro\)\. Se estiverem compatíveis, nada será informado no log  e a geração será feita com sucesso\. Se existir alguma diferença, deverá ser exibida a seguinte msg no log:

Primeira Situação: 

__Lançamentos EF com a informação: utomático de encerramento utomático por conta e centro de custo  e__

__Parâmetro “Omitir informação Centro de Custo em lançamentos Contábeis e Saldos” marcado:__

“Os lançamentos de encerramento automático foram gerados com o parâmetro \(Omitir informação Centro de Custo em lançamentos Contábeis e Saldos\) desmarcado, e agora, este parâmetro está marcado\. Favor gerar novamente os Lançamentos de Encerramento Automático\.”

Segunda Situação:

__Lançamentos EF com a informação: utomático de encerramento utomático por conta  e__

__Parâmetro “Omitir informação Centro de Custo em lançamentos Contábeis e Saldos” desmarcado:__

“Os lançamentos de encerramento automático foram gerados com o parâmetro \(Omitir informação Centro de Custo em lançamentos Contábeis e Saldos\) marcado, e agora, este parâmetro está desmarcado\. Favor gerar novamente os Lançamentos de Encerramento Automático\.”

__OS3658__

__RN192__

As demais regras existentes sobre a recuperação dos lançamentos e a exibição das informações devem ser mantidas\.

__OS3658__

__RN193__

Se as contas do PL informada na tela Lançamentos \(Tipo EF\) possuir mais de um centro de custo cadastrado na SAFX2101, considerar o primeiro centro de custo cadastrado\.

Obs\.: Esta regra deve ser aplicada somente para versão 3\.0 da SAFX2101 e recuperar valores do centro de custo do 1º lançamento referenciado, pois pode haver casos com mais de um referencial por conta\.

__OS3658__

__RN194__

Ao efetuar a geração automática dos registros EF, o sistema deve verificar se já existem esses lançamentos gerados automáticos na base \(para o período e estabelecimento em questão\), em caso afirmativo, devem ser excluídos automaticamente esses registros, antes de  efetuar a geração novamente \(este processo evita as duplicidades e problemas com o calculo dos registros\)\.

__OS3658__

__RN195__

Deve ser apresentado para cada centro de custo cadastrado na X2003\_centro\_custo \(inclusive para as suas alterações, quando existir\), um registro I100, na geração do FCONT\. As alterações que ocorrerem antes ou após o ano da geração do arquivo do FCONT, não deve ser informado neste período do arquivo\.

Exemplo: 

Considerando a geração do FCONT do exercício de 2011 e que existam lançamentos da conta X  \(que está vinculado ao cc XX\) durante este exercício:

Cadastro

Centro de Custo

Descrição

Criação/Alteração

01

XX

Desc1

01/01/2009

02

XX

Desc2

01/11/2009

03

XX

Desc3

01/05/2010

04

XX

Desc4

01/10/2010

05

XX

Desc5

01/07/2011

06

XX

Desc5

01/01/2012

Deve ser exibido um registro I100 para cada inclusão/alteração \(com exceção dos cadastros 01,02,03 e 06\)\. 

__CH16906\_2012__

__RN196__

A rotina da geração do FCONT deve considerar as informações do De\-Para, \(conta, referencial e centro de custo\) compatível com o período da geração do arquivo magnético\.

Com esta regra, o cenário abaixo deixa de existir:

Tenho uma conta e um centro de custo ambos criados na base em 2009\. Em 2010 no plano de contas referencial essas informações são cadastradas na base\. No ano de 2011 o centro de custo \(por exemplo\), sofre uma alteração da descrição na base, o que faz com que este centro de custo receba uma nova identificação na base \(processo feito automaticamente, pelo sistema\) e se não existir uma atualização no de\-para considerando esta nova numeração, o sistema não encontra esta parametrização no momento da geração do FCONT \(para o ano de 2011\) e por isso não gera as informações do de\-para, na geração do arquivo magnético\.

__CH15576\_2012__

__RN197__

Alterar a tela de Lançamentos \(Tipo EF\), localizada no módulo SPED / FCONT – Controle Fiscal Contábil de Transição, Menu: Geração, incluindo o campo Período de Apuração’ na tela, logo após o campo Exercício\.

Este campo terá os valores válidos: Anual e Trimestral e é de preenchimento obrigatório\. 

Se não for preenchido, exibir a seguinte msg ao usuário: “Favor selecionar o Período de Apuração”\.

Ao ser selecionado o parâmetro ‘Excluir todos os lançamentos de encerramento \(Tipo EF\) gerados automaticamente’, o campo ‘Período de Apuração’, deve ficar desabilitado \(exibindo a opção ‘Branco’\)\.

OS3678

__RN198__

Quando o período de apuração escolhido pelo cliente for TRIMESTRAL, a rotina de geração dos lançamentos de encerramento automático deve considerar o trimestre para gerar os lançamentos\.

Apesar dos lançamentos \(I200\) não serem gerados por quebra de trimestre, internamente, o sistema deve considerar os lançamentos por blocos \(trimestres\) e gerar o Lançamento EF de acordo com esse período \(01/01 à 31/03, 01/04 à 30/06, 01/07 à 30/09 e 01/10 à 31/12\)\. Com relação ao cálculo dos lançamentos, nada será alterado, ou seja, deve continuar seguindo as regras existentes na RN163\.

Para o período de apuração ANUAL, nada será alterado\.

OS3678

__RN199__

Se o estabelecimento utilizar mais de um grupo \(válido no período da geração do FCONT\), todos devem ser considerados na geração do meio magnético\.

Atenção: Esta regra deve considerar os cadastros como Conta Contábil, Centro de Custo e Plano de Contas\.

CH17253\_2012

__RN200__

Alteração na tela de Dados Inicias localizada no Módulo: Sped / FCONT – Controle Fiscal Contábil de Transição, Menu: Parâmetros → Dados Iniciais

No Parâmetro “Gerar Plano de Contas”, acrescentar a seguinte opção: Somente contas \+ centro de custo movimentados no período da geração\.

 

OS3689

__RN201__

Esta opção somente poderá ser selecionada se o parâmetro “Omitir informação Centro de custo em Lançamentos Contábeis e Saldos” NÃO estiver marcado\. Se estiver marcado, ao confirmar as alterações, não permitir a gravação e exibir a seguinte mensagem: “Não é possível Gerar Somente contas \+ centro de custo movimentados no período da geração, pois foi escolhido omitir Centro de Custo”\.

OS3689

__RN202__

Quando este parâmetro estiver marcado, deverão ser gravados somente os dados com movimentação referentes a combinação conta \+ centro de custo\.

Registro I050 → Irá gerar normalmente as contas que foram movimentadas no período, considerando os pontos abaixo:

Se houver para uma mesma conta, dois centros de custos associados, um com movimento e o outro não, a conta deverá ser gravada, pois um dos centro de custo tem movimento\.

Se houver para uma mesma conta, dois centros de custos associados, ambos sem movimento, a conta não será gravada\.

Se houver para uma mesma conta, dois centros de custos associados, ambos com movimento, a conta será gravada normalmente uma vez\.

Registro I051 → Como o registro I050 será gerado somente para as contas que foram movimentadas no período, a mesma regra se aplica a este registro: gerar o referencial, se a conta foi utilizada no período\.

Registro I100 → Somente gerar o centro de custo que tiver movimento, mesmo que não existir registros I051, para a conta\.

OS3689

__RN203__

Alteração no relatório de Dados Inicias localizada no Módulo: Sped / FCONT – Controle Fiscal Contábil de Transição, Menu: Parâmetros → Dados Iniciais

Este novo parâmetro, quando escolhido, deve ser apresentado no relatório de conferência desta tela\.

OS3689

__RN204__

Para os casos de situação especial, o período de recuperação dos registros para a criação automática dos Lançamentos \(Tipo EF\) deve seguir as regras abaixo:

Se pelo menos um dos campos 56, 66, 67 ou 68 da tabela de Estabelecimento estiver preenchido e compreendido no ano informado no campo ‘Exercício’ na tela “Lançamentos \(Tipo EF\)”:

1.  Gerar os lançamentos EF, com a diferença dos lançamentos \(F e N\) do período compreendido entre o início do ano até a data da situação especial \(data dos lançamentos EF = data da situação especial\)\.

Se mais de uma das datas citadas acima estiverem preenchidas \(na tabela Estabelecimento\) e compreendidas no mesmo exercício, considerar sempre a maior data para a data da situação especial\.

1. Se existir movimentação posterior à data da situação especial, na SAFX129, gerar os lançamentos EF com a diferença dos lançamentos \(F e N\) do período compreendido entre a data posterior a situação especial até 31/12 \(data dos lançamentos EF = 31/12/Ano do Exercício\)\. 

 

Caso a empresa não tenha sofrido nenhuma situação especial durante o exercício, nada será alterado\.

As demais regras existentes sobre a recuperação dos lançamentos, cálculos e exibição das informações, devem ser mantidas\.

OS4084


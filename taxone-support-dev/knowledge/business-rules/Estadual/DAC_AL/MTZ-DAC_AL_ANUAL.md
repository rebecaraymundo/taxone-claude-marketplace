# MTZ-DAC_AL_ANUAL

- **Fonte:** MTZ-DAC_AL_ANUAL.docx
- **Modificado:** 2023-03-01
- **Tamanho:** 67 KB

---

# 									DAC\-AL

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data de Alteração__

OS2992

Inclusão de novos registros para a geração ANUAL

Criação de novos registros para atendimento da DAC\-AL com Periodicidade Anual\. A __DAC Anual para Empresa NORMAL__ será composta pelos registros atualmente gerados pelo Mastersaf e apresentando os novos registros 61, 62, 63 e 64, com as informações da apuração do ano anterior\.

10/03/2011

OS3480

Inclusão de novos registros para a geração ANUAL

Inclusão dos Registros 65, 66, 67 e 68\.

10/01/2011

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RG01__

Novo Parâmetro:__ “Tipo de Produto x Lista de Produtos da DAC”__:

Criar parâmetro “__Tipo de Produto x Lista de Produtos da DAC\-AL__” no menu Parâmetros do Módulo \-> Declaração de Atividades do Contribuinte \- AL \(DAC\-AL\)\. Este parâmetro terá como funcionalidade relacionar os produtos X2013 com a tabela de produtos definidos na DAC\-AL\.__ PRT\_PRD\_OBRIG\_MSAF__

A tela deve iniciar com a seleção de Grupo/Validade padrão\. Utilizar o código do estado igual AL e o código de tabela para o grupo igual a 2013\.

Para incluir o cadastro, o usuário deverá informar a data de validade do registro\. Após a digitação de uma data válida, selecionar através do filtro, o produto proveniente da tabela x2013\_PRODUTO, respeitando o grupo e a validade informados anteriormente\. 

O usuário poderá incluir o código do produto manualmente e a descrição deverá ser preenchida pelo sistema\. Caso não possua o produto na tabela x2013\_PRODUTO ou fora da validade, apresentar a mensagem de erro: “Produto não encontrado”\.

Após o preenchido do produto, o usuário deverá incluir o produto referente a Lista de Produtos da DAC\-AL\. Poderá ser selecionado através do filtro ou digitado da mesma forma que o campo anterior\. A tabela origem para esse campo e a PRT\_PRD\_OBRIG \(carregada através da TACES50\.TXT\)\. Deve\-se usar o código do modulo da DAC\-AL \(084\) para a recuperação dos registros do filtro\.

Incluir os botões de inclusão, exclusão, alteração e relatório padrão Mastersaf\. Para o ícone “Relatório”: Deve abrir a tela de relatório padrão com os registros relacionados na tabela PRT\_PRD\_OBRIG\_MSAF\. Utilizar o código do modulo DAC\-AL \(084\) para seleção dos registros\.

*Obs\.:* No caso das Empresas que realizam a apuração de forma centralizada, por Inscrição Estadual Única, as informações deverão ser cadastradas sempre em nome do estabelecimento centralizador\. 

Novo Parâmetro:__ __“__Municípios IBGE x Municípios DAC\-AL__” 

Criar parâmetro “<a id="par_munic"></a>__Municípios IBGE x Municípios DAC\-AL__”, no menu Parâmetros do Módulo \-> Declaração de Atividades do Contribuinte \- AL \(DAC\-AL\)\. Este parâmetro terá como funcionalidade relacionar os municípios da tabela MUNICIPIO com a tabela de municípios definidos na DAC\-AL\. Os dados do relacionamento deverão ser gravados na tabela EST\_DE\_PARA\_MUNIC\.

A tela deverá ser do tipo multi\-registros\. O campo "UF da Obrigação" deverá apresentar o código do Estado de Alagoas que identifica de qual obrigação pertence o registro, neste caso "AL"\. No campo "UF" deverá carregar o código do Estado, que filtrará o grupo de municípios que serão relacionados, também neste caso "AL"\.

No campo "Município" poderá ser digitado ou recuperado através do filtro de seleção de município \(pasta amarela ao lado do campo\), o código do município que se deseja associar\. O filtro de seleção deverá mostrar somente os municípios do Estado de Alagoas\. Quando selecionado, a descrição do município deverá ser preenchida a seguir do código\. Se informado o código que não pertença ao grupo de municípios do Estado de Alagoas, a mensagem de erro será apresentada: "Município não cadastrado\." Deverá ser na cor vermelha para alertar o usuário\. 

OS2992

__RG01__

O campo "Município Destino" poderá ser selecionado através do filtro ou digitado da mesma forma que o campo anterior\. A tabela origem para esse campo é a TACES24\. Deve\-se usar o código do modulo da DAC\-AL \(084\) para a recuperação dos registros do filtro\. Somente os campos "código do município" e "município destino" devem ser habilitados para inclusão\. No caso de alteração do registro somente o campo "município destino" deverá ser habilitado para alteração\.

A tela deverá possuir as seguintes funcionalidades padrões Mastersaf, barra de ferramentas\. Para o ícone “Relatório”: Deve abrir a tela de relatório padrão com os registros relacionados na tabela EST\_DE\_PARA\_MUNIC provenientes da DAC\-AL\.

*Obs\.:* No caso das Empresas que realizam a apuração de forma centralizada, por Inscrição Estadual Única, as informações deverão ser cadastradas sempre em nome do estabelecimento centralizador\. 

Novo Parâmetro:__ Registro 62 \(Por CFOP\) __

Criar parâmetro __Registro 62 \(Por CFOP\) __no menu Parâmetros do Módulo \-> Declaração de Atividades do Contribuinte \- AL \(DAC\-AL\)\. Onde o usuário deverá gravar os CFOP’s que se enquadram às prestações do Registro 62\.

A parametrização será por Estabelecimento \(somente habilitar os localizados na UF = AL\), possibilitando a replicação para os demais Estabelecimentos da mesma UF\. Esta parametrização será opcional, pois somente alguns tipos de contribuintes estão obrigados a informar dados anuais de períodos anteriores\.

O campo Tipo de Operação deve listar os códigos referente a obrigação DAC\-AL \(TFIX31\)\. Poderá ser selecionado através do filtro ou digitado da mesma forma que o campo anterior\. Deve\-se usar o código do modulo da DAC\-AL \(084\) para a recuperação dos registros do filtro\.

*Obs\.:* No caso das Empresas que realizam a apuração de forma centralizada, por Inscrição Estadual Única, as informações deverão ser cadastradas sempre em nome do estabelecimento centralizador\.

Novo Parâmetro:__ Registro 62 \(Por Extensões de CFOP\)__

Criar parâmetro __Registro 62 \(Por Extensões de CFOP\)__ no menu Parâmetros do Módulo \-> Declaração de Atividades do Contribuinte \- AL \(DAC\-AL\)\. Onde o usuário deverá gravar os CFOP’s que se enquadram às prestações do Registro 62\.

A parametrização será por Estabelecimento \(somente habilitar os localizados na UF = AL\), possibilitando a replicação para os demais Estabelecimentos da mesma UF\. Esta parametrização será opcional, pois somente alguns tipos de contribuintes estão obrigados a informar dados anuais de períodos anteriores\.

O campo Tipo de Operação deve listar os códigos referente a obrigação DAC\-AL \(TFIX31\)\. Poderá ser selecionado através do filtro ou digitado da mesma forma que o campo anterior\. Deve\-se usar o código do modulo da DAC\-AL \(084\) para a recuperação dos registros do filtro\.

*Obs\.:* No caso das Empresas que realizam a apuração de forma centralizada, por Inscrição Estadual Única, as informações deverão ser cadastradas sempre em nome do estabelecimento centralizador\. 

__RG01__

__Geração de Dados Acessórios:__

__Módulo: Declaração de Atividades do Contribuinte \- AL  \(DAC\-AL\) Menu: Parâmetros 🡪 Geração de Dados Acessórios__

Os novos registros 63 e 64 utilizarão as tabelas de Resumos para cálculo de valores\. E o processo de consolidação deverá ser feito nesta tela de parâmetro de Dados Acessórios, que normalmente todas as gerações de obrigações utilizam e atendem a todos os estabelecimentos de uma empresa\.

Para a geração de Estabelecimento com Inscrição Estadual Centralizada, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Documentário Fiscal e Inventário\)\.

Mais detalhes da funcionalidade destes Resumos estão no documento da OS1153\.

__\[ALTERADA – OS3480\]__

__Geração dos Registros__

__Módulo: Declaração de Atividades do Contribuinte \- AL \(DAC\-AL\) Menu: Obrigações 🡪 Geração dos Registros__

A funcionalidade desta tela não sofreu alteração\. Os parâmetros de entrada de dados continuam atendendo os novos registros 61, 62,63, 64__, 65, 66, 67 e 68__, somente quando selecionado parâmetro “novo”\.

No programa da DAC\-AL estes registros são habilitados para preenchimento no mês de ABRIL de cada ano vigente da obrigação, porém deve ser preenchido com as informações retroativas aquele ano, como exemplo: no mês de ABRIL de 2011 o programa libera para digitação os quadros III, IV, V, X e XI referente a apuração do ano de 2010\.

Conforme Manual da DAC\-AL \(2\.2\): “Além da declaração Mensal ou Quadrimestral, os contribuintes enquadrados como empresa Normal, EPP e MÉ devem apresentar, a partir do exercício de 2003, juntamente com a declaração da competência de ABRIL do ano seguinte, as informações anuais consolidadas \(até então apresentadas na Declaração Anual do Contribuinte”\.

Embora o período de competência para as operações do ano anterior seja o mês de ABRIL no programa da DAC\-AL, o Mastersaf apresentará os registros anuais quando o parâmetro estiver selecionado\.

__\[ALTERADA – OS3480\] __Deverá ser alterado o nome do parâmetro na TELA e alterada funcionalidade para atender também os novos registros anuais 65, 66, 67e 68\. 

DE:__ __“Gerar informações anuais consolidadas \(Reg\. 61, 62, 63 e 64\)”

PARA:__ “Gerar informações anuais consolidadas__”

__Este parâmetro deverá ser utilizado para os demais registros da DAC\-AL com periodicidade anual\. Seguem destacadas as mudanças na regra a seguir neste documento\.__

Parâmetro: “__Gerar informações anuais consolidadas__”, na tela de Geração dos Registros\. Módulo: Declaração de Atividades do Contribuinte \- AL \(DAC\-AL\) 🡪 Obrigações 🡪 Geração dos Registros

Este parâmetro deverá ficar como default “__inibido__”\. Não deverá aparecer na tela se não for o mês de Abril\. Caso contrário, quando o usuário informar o período “mês igual 04”, o ano a definir, o parâmetro surgirá na tela de Geração dos Registros\. Somente quando o usuário optar por gerar os registros anuais, o mesmo deverá ser selecionado\.

Quando o parâmetro “__Gerar informações anuais consolidadas__”, estiver __marcado__:

          

- Apresentar os registros obrigatórios atualmente já considerados na geração Mensal e incluir no período de competência, quando informado o mês 04 \(Abril\) no campo “MÊS/ANO” da tela de Geração dos Registros, os seguintes registros: 61, 62, 63, 64__,65, 66, 67 e 68__ obedecendo ao critério de consolidação de cada registro, por se tratar de informações anuais do ano anterior;

OS2992/OS3480

__RG01__

Quando o parâmetro “__Gerar informações anuais consolidadas__”, __não__ estiver marcado:

- Apresentar somente os registros obrigatórios atualmente já considerados na geração Mensal obedecendo ao critério de seleção e os parâmetros da tela de Geração dos Registros;

Trazer “desmarcado” como default o parâmetro “__Gerar informações anuais consolidadas__”__\.__

Colocar o novo parâmetro após o parâmetro “__Geração Centralizada por Inscrição Estadual Única”\.__

Novo Parâmetro: “__Considerar Município do Ponto de Consumo \(Utilities\)__” na tela de Geração dos Registros\. Módulo: Declaração de Atividades do Contribuinte \- AL \(DAC\-AL\)  🡪 Obrigações 🡪 Geração dos Registros

Quando o parâmetro “__Considerar o Município do Ponto de Consumo \(Utilities\)__”, estiver __marcado__:

Considerar o Município do Ponto de Consumo \(campo 76/SAFX42\) na geração do Registro 62\. Esta situação somente irá se aplicar às notas de saídas que estiverem na SAFX42 \(modelo 01, 06, 21 ou 22\)\.  Para as notas que estiverem na SAFX07, considerar o município do cadastro da Pessoa Fis\./Jur\. \(SAFX04\)

Quando o parâmetro “__Considerar o Município do Ponto de Consumo \(Utilities\)__”, estiver __desmarcado__:

Considerar o município do cadastro da Pessoa Fis\./Jur\. \(SAFX04\), de acordo com a Pessoa Fis/Jur, da NF\.

Colocar o novo parâmetro após o parâmetro “__Gerar informações anuais consolidadas__”__\.__

Parâmetro *“Geração Centralizada por Inscrição Estadual Única”*: Considerar os novos registros na geração de Estabelecimento com Inscrição Estadual Centralizada\. O somatório deverá atender todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais \(Documentário Fiscal e Inventário\)\.

__\[ALTERADA – OS3480\] __Deverão ser criados os parâmetros que fará a recuperação dos registros do Tipo 65 \(Estoque e Balanço\)\. Incluir na tela de Geração dos Registros o quadro chamado “Informações de Estoque”, logo abaixo dos parâmetros do Reg\. 44 \(GNRE e DAR\)\.

Localização: Estadual → DAC\-AL → Obrigações → Geração dos Registros

__Data Inventário Inicial:__ onde o usuário deverá informar a data inicial para o período de geração\. Esta informação é obrigatória para gerar este registro\.

__Data Inventário Final:__ onde o usuário deverá informar a data inicial para o período de geração\. Esta informação é obrigatória para gerar este registro\.

__Estoque:__ o usuário deverá escolher uma das opções:

- __Por Produto__ → recuperar dados da SAFX52
- __Por NBM__ → recuperar dados da SAFX62

__RG01__

__ALTERADA – OS3480\]  Convenções de Formato e Tamanho dos Campos:__

Campo alfanumérico: preenchido com caracteres maiúsculos \(caixa alta\) com tamanho especificado na Descrição, alinhado à esquerda com brancos à direita\. Se vazio, preencher com brancos\.

Campo numérico com tamanho especificado na Descrição, alinhado à direita, com zeros à esquerda\. Se vazio, preencher com zeros\. 

Campo Data utilizado para datas no formato AAAAMM ou AAAAMMDD, caso possua 6 ou 8 campos respectivamente, onde: AAAA\-Ano; MM\-Mês; DD\-Dia; Serão aceitas apenas datas válidas\. Se vazio, preencher com zeros\.

Campo do tipo N \(Valor\) R$, mas que só aceita valor maior ou igual a zero\. Campo numérico de 17 posições, onde as 14 primeiras posições são a parte inteira com zeros à esquerda; e as 2 últimas posições são a parte decimal com zeros à direita\. No caso de valor negativo, informar o sinal de menos \(\-\) na primeira posição\. Se vazio, preencher com zeros\.

__RN01__

Gerar o __Registro Tipo 61__ __\(Quadro III\)__ \- Municípios \- Operações Internas de Produtos quando o parâmetro “Gerar informações anuais consolidadas“ estiver marcado\.

Selecionar documento Fiscal \(X07\_DOCTO\_FISCAL, X08\_ITENS\_MERC\) onde:

- Movimento Entrada/Saída <> “9” 
- Documento de Entrada emitida pelo Estabelecimento, no ano anterior ao ano informado em tela Geração dos Registros \(campo Mês/Ano\)
- Classificação do Docto Fiscal = 1 – Mercadoria __ou__ 3 – Mercadoria e Serviço
- Município e UF da Pessoa Fis\. Jur da nota pertencente a Alagoas\.
- O código do produto da nota deverá ser parametrizado para um Código de Produto definido pela DAC\-AL \(__Tipo de Produto x Lista de Produtos da DAC__\)\.
- Se Unidade de Medida da Nota for diferente da Unidade de Medida definida pela DAC\-AL para o produto, utilizar o fator de conversão de unidades de medidas, para converter a quantidade da nota na unidade de medida definida pela DAC\-AL\. 
- O município deverá ser parametrizado para um Código de Município definido pela DAC\-AL \(__Municípios IBGE x Municípios DAC\-AL__\)\.

Exceções:

- Não gerar documentos cancelados
- Não considerar no cálculo as notas fiscais da SAFX07 geradas pelo mapa resumo de ICMS\.
- Não considerar os Registros do Tipo 62\.

Demais regras:

O agrupamento do registro será por MUNICIPIO x PRODUTO\. Os campos que serão totalizados serão descritos a seguir no detalhamento dos campos\.

Para a geração de Estabelecimento com Inscrição Estadual Centralizada, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As informações deverão ser cadastradas sempre em nome do estabelecimento centralizador\. 

OS2992

__RN02__

Registro Tipo 61 campo 02 \- Município

__Conteúdo__: Código do Município

__Tamanho__: 06

__Posição__: 03 \- 08

__Tipo__: N

__Regra de Negócio__: Utilizar o critério de seleção da regra RN01 e recuperar o Código do Município Origem \(item 182 \- SAFX07\) nas notas de entrada\. Caso os campos não estejam preenchidos, deve\-se recuperar o Código do Município da Pessoa Física/Jurídica \(item 25 \- SAFX04\)\.  Após encontrar o código do município do documento fiscal, fazer a comparação com o código do município da DAC\-AL parametrizado na tela de “Municípios IBGE x Municípios DAC\-AL”\.

OS2992

__RN03__

Registro Tipo 61 campo 03 \- Produto

__Conteúdo__: Código do produto conforme tabela de Produtos da DAC\-AL

__Tamanho__: 03

__Posição__: 09 \- 11

__Tipo__: N

__Regra de Negócio__: Utilizar o critério de seleção da regra RN01 para obter o filtro dos campos e informar o conteúdo do Parâmetro “__Tipo de Produto x Lista de Produtos da DAC” __com o código da DAC\-AL igual a “084”\.

OS2992

__RN04__

Registro Tipo 61 campo 04 – Quantidade

__Conteúdo__: Quantidade de produtos

__Tamanho__: 010V004

__Posição__: 12 \- 25

__Tipo__: N

__Regra de Negócio: __Utilizar o critério de seleção da regra RN01 para encontrar o campo e totalizar a quantidade \(QUANTIDADE\.X08\_ITENS\_MERC\)\.

OBS: Considerar parte inteira com dez posições e parte decimal com quatro posições

OS2992

__RN05__

Registro Tipo 61 campo 05 – Valor

__Conteúdo__: Valor total dos produtos

__Tamanho__: 14

__Posição__: 26 \- 39

__Tipo__: N

__Regra de Negócio: __Utilizar o critério de seleção da regra RN01 para encontrar o campo e totalizar o valor do produto \(VLR\_ITEM\.X08\_ITENS\_MERC\)\.

OS2992

__RN06__

Gerar o __Registro Tipo 62__ __\(Quadro IV\)__ \- Municípios \- Operações Internas de Serviços quando o parâmetro “Gerar informações anuais consolidadas”, estiver marcado\. 

Selecionar documento Fiscal \(X07\_DOCTO\_FISCAL, X08\_ITENS\_MERC\) onde:

- Movimento Entrada/Saída igual a “9” 
- Nota emitida pelo estabelecimento, no ano anterior
- Data de Emissão entre a Data Inicial e Data Final de geração do arquivo
- Classificação do Docto Fiscal = 1 – Mercadoria __ou__ 3 – Mercadoria e Serviço
- Município e UF da Pessoa Fis\. Jur da nota pertencente a Alagoas\.
- O município deverá ser parametrizado para um Código de Município definido pela DAC\-AL \(__Municípios IBGE x Municípios DAC\-AL__\)\.
- CFOP ou Extensão CFOP da capa \(p/ nota sem item SAFX07\) ou do item \(p/ nota com item SAFX08\) parametrizado para prestação de serviço de energia, comunicação e transporte\.

Nesta parametrização, o campo “tipo de operação”, determinará qual o tipo de serviço prestado de acordo com o código carregado da TFIX31, comparado do código da obrigação DAC\-AL: 

__                       __TFXI 31:__ 386__

\-   DAC\-AL: __701 __\- Energia Elétrica

__                        __TFIX 31:__ 390__

\-   DAC\-AL: __702 __\- Comunicações \(Telefonia, Correios\)

                        TFIX 31:__ 388  __

\-   DAC\-AL: __703__ \- Transportes \(Rodoviário, Ferroviário, Aéreo, Marítimo\)

Exceções:

- Não gerar documentos cancelados
- Não considerar os documentos gerados pelo Mapa Resumo, quando o parâmetro “__*Considerar Município do Ponto de Consumo \(Utilities\)*__” estiver marcado\.
- No cálculo do valor contábil, quando o movimento for gerado a partir das utilities, considerar valor contábil deduzindo o valor dos descontos \(campo 19/safx43 – campo 18/safx42\)\.
- Não considerar os Registros do Tipo 61\.

Demais regras:

\- O agrupamento do registro será por MUNICIPIO x SERVICO\. Os campos que serão totalizados serão descritos a seguir no detalhamento dos campos\.

\- Quando o parâmetro “__*Considerar Município do Ponto de Consumo \(Utilities\)*__” da Geração dos Registros estiver marcado, deverão ser considerados os Documentos Fiscais de Utilities \(SAFX42/43\), com as seguintes características: 

- Modelo de Documento = 06 – Nota Fiscal/Conta de Energia Elétrica, 
- Modelo de Documento = 21 – Nota Fiscal de Serviço de Comunicação ou 22 – Nota Fiscal de Serviço de Telecomunicações
- Campo “Ponto de Consumo / Terminal Faturado” preenchido com “UF” e “Município”\. 

\- Quando o Campo não estiver marcado, permanece o comportamento atual\. Estas condições deverão ser aplicadas tanto na geração normal quanto à Geração por Inscrição Estadual Única\.

\- Quando o serviço é transporte \(703\), o Código do Município que tem que estar preenchido é o código do município origem, da capa do documento\.

\- Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração dos Registros estiver marcado, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\.  As informações deverão ser cadastradas sempre em nome do estabelecimento centralizador\. 

OS2992

__RN07__

Registro Tipo 62 campo 02 \- Município

__Conteúdo__: Código do Município

__Tamanho__: 06

__Posição__: 03 \- 08

__Tipo__: N

__Regra de Negócio:__ Utilizar o critério de seleção da regra RN06 para obter o filtro dos campos e totalizar o movimento de notas fiscais do período, buscando pelo município da pessoa fis/jur da SAFX07 na SAFX04\. De acordo com este município, verificar correspondência na tabela “Municípios IBGE x Municípios DAC\-AL” \(TACES24\), e gravar o município destino\.

Exceto quando parâmetro “Considerar Município do Ponto de Consumo” selecionado:

Totalizar o movimento de utilities \(SAFX42/43\) do período, buscando por município do ponto de consumo \(campo 76/SAFX42\), de acordo com os CFOP’s parametrizados em: DAC\-AL → Parâmetros → Registro 62 🡪 P/ CFOP ou p/ CFOP/Natureza Op\.

 De acordo com este município, verificar correspondência na tabela “tabela “Municípios IBGE x Municípios DAC\-AL” \(TACES24\), e gravar o município destino\. 

   

OS2992

__RN08__

Registro Tipo 62 campo 03 – Serviço

__Conteúdo__: Código do produto conforme tabela de Produtos da DAC\-AL

__Tamanho__: 03

__Posição__: 09 \- 11

__Tipo__: N

__Regra de Negócio__: Utilizar o critério de seleção da regra RN06 para obter o filtro dos campos e recuperar o Código do Serviço da tabela TFIX31 e gravar o conteúdo no campo de acordo com o respectivo código de prestação:

Quando tratar\-se de prestação de serviço Energia: código 386, gravar __701__

Quando tratar\-se de prestação de serviço Transportes \(Rodoviário, Ferroviário, Aéreo, Marítimo\): código 388, gravar __703__

Quando tratar\-se de prestação de serviço Comunicações \(Telefonia, Correios\): código 390, gravar __702__

Neste campo serão válidos os valores da Lista de Serviços da DAC\-AL\.

OS2992

__RN09__

Registro Tipo 62 campo 04 – Valor

__Conteúdo__: Valor do Total do Serviço

__Tamanho__: 14

__Posição__: 12 \- 25

__Tipo__: N

__Regra de Negócio 01:__ Utilizar o critério de seleção da regra RN06 e totalizar o valor do Serviço \(VLR\_ITEM\.X08\_ITENS\_MERC\)\.

Exceto quando parâmetro “Considerar Município do Ponto de Consumo” selecionado totalizar o valor do Serviço \(VLR\_SERVICO\.SAFX43\)\.

OS2992

__RN10__

Registro Tipo 62 campo 05 – Custo Proporcional

__Conteúdo__: Custo proporcional do serviço por município__ __

__Tamanho__: 14

__Posição__: 26 \- 39

__Tipo__: N

__Regra de Negócio: __Informe o valor dos custos do contribuinte no período em relação ao município selecionado

Fora de escopo, preencher com “zeros__”\.__

OS2992

__RN11__

Gerar o __Registro Tipo 63__ __\(Quadro V\)__ \- Operações realizadas por UF – Entradas quando o parâmetro “Gerar informações anuais consolidadas”, estiver marcado\. 

Selecionar os registros processados da tabela de Resumo por UF/CFOP, somente de Entradas \(EST\_RES\_CFO\_UF\_01\) relacionando a tabela ESTADO, com os seguintes filtros:

- cod\_empresa = passado como parâmetro
- cod\_estab       = passado como parâmetro
- dat\_apurac      = compreendida entre a data inicial e final do ano passado como parâmetro
- ind\_e\_s           = ‘__E__’
- Somente operações internas, cujos Municípios participantes do documento fiscal sejam do Estado de Alagoas\. Os CFOPs \(X2012\_COD\_FISCAL\.COD\_CFO\) iniciados com ‘1’, ‘2’ e ‘3’\.

OBS: Críticas para campos obrigatórios \(\*\)

UF \(\*\) \-\-> se IDENT\_ESTADO = 0 critica de UF não preenchida para algumas pessoas fis\. jur\.

Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração dos Registros estiver marcado, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As informações deverão ser cadastradas sempre em nome do estabelecimento centralizador\. As informações deverão ser cadastradas sempre em nome do estabelecimento centralizador\. 

OS2992

__RN12__

Registro Tipo 63 campo 02 \- UF

__Conteúdo__: Sigla da unidade federativa Código do Município

__Tamanho__: 02

__Posição__: 03 \- 04

__Tipo__: C

__Regra de Negócio:__ Utilizar o critério de seleção da regra RN06 e selecionar o COD\_ESTADO \(tabela ESTADO\)

OS2992

__RN13__

Registro Tipo 63 campo 03 – Valor Contábil

__Conteúdo__: Valor Contábil

__Tamanho__: 14

__Posição__: 05 \- 18

__Tipo__: N

__Regra de Negócio:__ Utilizar o critério de seleção da regra RN06 e selecionar VLR\_CONTABIL \(tabela EST\_RES\_CFO\_UF\_01\)

OS2992

__RN14__

Registro Tipo 63 campo 04 – Base de cálculo

__Conteúdo__: Base de cálculo

__Tamanho__: 14

__Posição__: 19 \- 32

__Tipo__: N

__Regra de Negócio:__ Utilizar o critério de seleção da regra RN06 e selecionar VLR\_BASE\_ICMS \(tabela EST\_RES\_CFO\_UF\_01\)

OS2992

__RN15__

Registro Tipo 63 campo 05 – Outras

__Conteúdo__: Outras

__Tamanho__: 14

__Posição__: 33 \- 46

__Tipo__: N

__Regra de Negócio:__ Utilizar o critério de seleção da regra RN06 e selecionar VLR\_BASE\_OUTRAS \(tabela EST\_RES\_CFO\_UF\_01\)

OS2992

__RN16__

Registro Tipo 63 campo 06 – ICMS ST Petróleo e Energia 

__Conteúdo__: ICMS ST Petróleo e Energia__ __

__Tamanho__: 14

__Posição__: 47 \- 60

__Tipo__: N

__Regra de Negócio:__ Utilizar o critério de seleção da regra RN06 e selecionar VLR\_ICMS\_S\_PET \(tabela EST\_RES\_CFO\_UF\_01\)

OS2992

__RN17__

Registro Tipo 63 campo 07 – ICMS ST Outros

__Conteúdo__: ICMS ST Outros

__Tamanho__: 14

__Posição__: 61 \- 74

__Tipo__: N

__Regra de Negócio:__ Somatório do valor de ICMS ST Outros\. Valor encontrado através do critério da regra 11, a subtrair os campos \(VLR\_ICMS\_S\) – \(VLR\_ICMS\_S\_PET\) da tabela EST\_RES\_CFO\_UF\_01\. 

OS2992

__RN18__

Gerar o __Registro Tipo 64__ __\(Quadro V\)__ \- Operações realizadas por UF – Saídas quando o parâmetro “Gerar informações anuais consolidadas”, estiver marcado\. 

Selecionar os registros processados da tabela de Resumo por UF, somente de saídas \(EST\_RES\_CFO\_UF\_01\) relacionando a tabela  ESTADO, com os seguintes filtros:

- cod\_empresa = passado como parâmetro
- cod\_estab       = passado como parâmetro
- dat\_apurac      = compreendida entre a data inicial e final do ano passado como parâmetro
- ind\_e\_s          = ‘__S__’
- Somente operações internas, cujos Municípios participantes do documento fiscal sejam do Estado de Alagoas\. Os CFOPs \(X2012\_COD\_FISCAL\.COD\_CFO\) iniciados com ‘5’, ‘6’ e ‘7’\.

OBS: Críticas para campos obrigatórios \(\*\)

UF \(\*\) \-\-> se IDENT\_ESTADO = 0 critica de UF não preenchida para algumas Pessoas Fis\. Jur\.

Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração dos Registros estiver marcado, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As informações deverão ser cadastradas sempre em nome do estabelecimento centralizador\. 

OS2992

__RN19__

Registro Tipo 64 campo 02 \- UF

__Conteúdo__: Sigla da unidade federativa Código do Município

__Tamanho__: 02

__Posição__: 03 \- 04

__Tipo__: C

__Regra de Negócio:__ Utilizar o critério de seleção da regra RN06 e selecionar o COD\_ESTADO \(tabela ESTADO\)

OS2992

__RN20__

Registro Tipo 64 campo 03 – Valor Contábil Contribuinte

__Conteúdo__: Valor Contábil Contribuinte

__Tamanho__: 14

__Posição__: 05 \- 18

__Tipo__: N

__Regra de Negócio:__ Somatório do valor de Contábil Contribuinte\. Valor encontrado através do critério da regra 18, a subtrair os campos \(VLR\_CONTABIL\) – \(VLR\_CONTABIL\_NC\) da tabela EST\_RES\_CFO\_UF\_01\. 

OS2992

__RN21__

Registro Tipo 64 campo 04 – Valor Contábil Não Contribuinte

__Conteúdo__: Valor Contábil Não Contribuinte

__Tamanho__: 14

__Posição__: 19 \- 32

__Tipo__: N

__Regra de Negócio:__ Utilizar o critério de seleção da regra RN06 e selecionar VLR\_CONTABIL\_NC \(tabela EST\_RES\_CFO\_UF\_01\)

OS2992

__RN22__

Registro Tipo 64 campo 05 – Base de Cálculo Contribuinte 

__Conteúdo: __Base de Cálculo Contribuinte

__Tamanho__: 14

__Posição__: 33 \- 46

__Tipo__: N

__Regra de Negócio:__ Somatório da Base de Cálculo Contribuinte\. Valor encontrado através do critério da regra 18, a subtrair os campos \(VLR\_BASE\_ICMS\) – \(VLR\_BASE\_ICMS\_NC\) da tabela EST\_RES\_CFO\_UF\_01\. 

OS2992

__RN23__

Registro Tipo 64 campo 06 – Base de Cálculo Não Contribuinte 

__Conteúdo__: Base de Cálculo Não Contribuinte

__Tamanho__: 14

__Posição__: 47 \- 60

__Tipo__: N

__Regra de Negócio:__ Utilizar o critério de seleção da regra RN06 e selecionar VLR\_BASE\_ICMS\_NC \(tabela EST\_RES\_CFO\_UF\_01\)

OS2992

__RN24__

Registro Tipo 64 campo 07 – Outras

__Conteúdo__: Outras

__Tamanho__: 14

__Posição__: 61 \- 74

__Tipo__: N

__Regra de Negócio:__ Utilizar o critério de seleção da regra RN06 e selecionar VLR\_BASE\_OUTRAS \(tabela EST\_RES\_CFO\_UF\_01\)

OS2992

__RN25__

Registro Tipo 64 campo 08 – ICMS Retido ST

__Conteúdo__: ICMS retido para outros estados em operações com substituição tributária

__Tamanho__: 14

__Posição__: 75 \- 88

__Tipo__: N

__Regra de Negócio:__ Somatório do valor do ST\. Valor encontrado através do critério da regra 17, a subtrair os campos \(VLR\_ICMS\_S\) – \(VLR\_ICMS\_S\_NAPROPR\) da tabela EST\_RES\_CFO\_UF\_01\.

OS2992

__RG65__

Gerar o __Registro Tipo 65__ __\(Quadro X\)__ – Estoque e Balanço quando o parâmetro “__Gerar informações anuais consolidadas__”, estiver marcado\. 

Este registro é gerado com as totalizações dos campos do registro a seguir, conforme empresa e estabelecimento selecionado, nas datas informadas através dos parâmetros Data de Inventário Inicial e Data de Inventário Final na tela de Geração de Registros\. Deverá ser gravado na tabela apenas um registro por período \(Ano\)\. 

Verificar o parâmetro de __Estoque__ também no menu Obrigações → Geração dos Registros:

Ler os dados conforme o caso: __Estoque__ = __Produto  – Tabela SAFX52__

__                                             = NBM        – Tabela SAFX62__

Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração dos Registros estiver marcado, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As informações deverão ser cadastradas sempre em nome do estabelecimento centralizador\. 

OS3480

__RN26__

Registro Tipo 65 campo 01 \- TIPO

__Conteúdo:__ Tipo de Registro

__Tamanho__: 02

__Posição__: 01\-02

__Tipo__: Numérico

__Regra de Negócio: __Deverá ser preenchido com o conteúdo fixo “__65__”\.

OS3480

__RN27__

Registro Tipo 65 campo 02 \- Data do balanço

__Conteúdo__: Data do Balanço__ __

__Tamanho__: 08

__Posição__: 03\-10

__Tipo__: D – Formato: AAAAMMDD

__Regra de Negócio: __

O usuário deverá preencher o campo “Data de Balanço” no Módulo Estadual → DAC\-AL → Manutenção → Registro Tipo 65 – Estoque e Balanço, para definir o conteúdo deste campo\.

OS3480

__RN28__

Registro Tipo 65 campo 03 \- Mercadorias Tributadas: Inicial

__Conteúdo__: Estoque Inicial de mercadorias tributadas__ __

__Tamanho__: 14

__Posição__: 11\-24

__Tipo__: N \(Valor\)

__Regra de Negócio: Se__ na tela de geração dos registros for escolhido gerar o inventário a partir da __SAFX52 \(Por Produto\)__:

Selecionar os registros processados da tabela de SAFX52 – Produtos, com os seguintes filtros:

- cod\_empresa = passado como parâmetro
- cod\_estab       = passado como parâmetro
- data\_inventario      = compreendida a data inicial de Inventário passado como parâmetro

Recuperar os registros de todo o inventário dos produtos, onde a data do “Inventário Inicial” informado como parâmetro na tela de geração seja no mesmo período do campo 02 – Data do Inventário da SAFX52\.

Gravar neste campo “Mercadorias Tributadas: Inicial” o total do campo 26 \(Base ICMS\) de todos os registros de inventário que se enquadrem na situação acima\.

__Se__ na tela de geração for escolhido gerar o inventário a partir da __SAFX62 \(Por NBM\)__:

Selecionar os registros processados da tabela de SAFX62 – NBMs, com os seguintes filtros:

- cod\_empresa = passado como parâmetro
- cod\_estab       = passado como parâmetro
- data\_inventario  = compreendida a data inicial de Inventário passado como parâmetro\. 

Recuperar os registros de todo o inventário por NBM, onde a data do “Inventário Inicial” informado como parâmetro na tela de geração seja no mesmo período do campo 03 – Data do Inventário da SAFX62\.

Gravar neste campo “Mercadorias Tributadas: Inicial” o total do campo 18 \(Base ICMS\) de todos os registros de inventário que se enquadrem na situação acima\.

OS3480

__RN29__

Registro Tipo 65 campo 04 \- Mercadorias Tributadas: Final

__Conteúdo__: Estoque final de mercadorias tributadas__ __

__Tamanho__: 14

__Posição__: 25\-38

__Tipo__: N \(Valor\)

__Regra de Negócio: Se__ na tela de geração for escolhido gerar o inventário a partir da __SAFX52 \(Por Produto\)__:

Selecionar os registros processados da tabela de SAFX52 – Produtos, com os seguintes filtros:

- cod\_empresa = passado como parâmetro
- cod\_estab       = passado como parâmetro
- data\_inventario      = compreendida a data final de Inventário passado como parâmetro

Recuperar os registros de todo o inventário dos produtos, onde a data do “Inventário Final” informado como parâmetro na tela de geração seja no mesmo período do campo 03 – Data do Inventário da SAFX52\.

Gravar neste campo “Mercadorias Tributadas: Final” o total do campo 26 \(Base ICMS\) de todos os registros de inventário que se enquadrem na situação acima\.

__Se__ na tela de geração for escolhido gerar o inventário a partir da __SAFX62 \(Por NBM\)__:

Selecionar os registros processados da tabela de SAFX62 – NBM’s, com os seguintes filtros:

- cod\_empresa = passado como parâmetro
- cod\_estab       = passado como parâmetro
- data\_inventario      = compreendida a data final de Inventário passado como parâmetro

Recuperar os registros de todo o inventário de NBM, onde a data do “Inventário Final” informado como parâmetro na tela de geração seja no mesmo período do campo 03 – Data do Inventário da SAFX62\.

Gravar neste campo “Mercadorias Tributadas: Final” o total do campo 18 \(Base ICMS\) de todos os registros de inventário que se enquadrem na situação acima\.

OS3480

__RN30__

Registro Tipo 65 campo 05 \- Mercadorias Isentas ou Não Tributadas: Inicial

__Conteúdo__: Estoque Inicial de mercadorias isentas ou não tributadas

__Tamanho__: 14

__Posição__: 39\-52

__Tipo__: N \(Valor\)

__Regra de Negócio: Se__ na tela de geração for escolhido gerar o inventário a partir da __SAFX52 \(Por Produto\)__:

Selecionar os registros processados da tabela de SAFX52 – Produtos, com os seguintes filtros:

- cod\_empresa = passado como parâmetro
- cod\_estab       = passado como parâmetro
- data\_inventario      = compreendida a data inicial de Inventário passado como parâmetro

Recuperar os registros de todo o inventário dos produtos, onde a data do “Inventário Inicial” informado como parâmetro na tela de geração seja no mesmo período do campo 03 – Data do Inventário da SAFX52\.

Gravar neste campo “Mercadorias Isentas ou Não Tributadas: Inicial” o total do __campo 27 \(Base Isenta ICMS\) __de todos os registros de inventário que se enquadrem na situação acima\.

__Se__ na tela de geração for escolhido gerar o inventário a partir da __SAFX62 \(Por NBM\)__:

Selecionar os registros processados da tabela de SAFX62 – NBMs, com os seguintes filtros:

- cod\_empresa = passado como parâmetro
- cod\_estab       = passado como parâmetro
- data\_inventario  = compreendida a data inicial de Inventário passado como parâmetro\. 

Recuperar os registros de todo o inventário por NBM, onde a data do “Inventário Inicial” informado como parâmetro na tela de geração seja no mesmo período do campo 03 – Data do Inventário da SAFX62\.

Gravar neste campo “Mercadorias Isentas ou Não Tributadas: Inicial” o total do __campo 19 \(Base Isenta ICMS\) __de todos os registros de inventário que se enquadrem na situação acima\.

OS3480

__RN31__

Registro Tipo 65 campo 06 \- Mercadorias Isentas ou Não Tributadas: Final

__Conteúdo__: Estoque final de mercadorias isentas ou não tributadas

__Tamanho__: 14

__Posição__: 53\-66

__Tipo__: N \(Valor\)

__Regra de Negócio: Se__ na tela de geração for escolhido gerar o inventário a partir da __SAFX52 \(Por Produto\)__:

Selecionar os registros processados da tabela de SAFX52 – Produtos, com os seguintes filtros:

- cod\_empresa = passado como parâmetro
- cod\_estab       = passado como parâmetro
- data\_inventario      = compreendida a data final de Inventário passado como parâmetro

Recuperar os registros de todo o inventário dos produtos, onde a data do “Inventário Final” informado como parâmetro na tela de geração seja no mesmo período do campo 03 – Data do Inventário da SAFX52\.

Gravar neste campo “Mercadorias Isentas ou Não Tributadas: Final” o total do __campo 27 \(Base Isenta ICMS\) __de todos os registros de inventário que se enquadrem na situação acima\.

__Se__ na tela de geração for escolhido gerar o inventário a partir da __SAFX62__:

Selecionar os registros processados da tabela de SAFX62 – NBM’s, com os seguintes filtros:

- cod\_empresa = passado como parâmetro
- cod\_estab       = passado como parâmetro
- data\_inventario      = compreendida a data final de Inventário passado como parâmetro

Recuperar os registros de todo o inventário de NBM, onde a data do “Inventário Final” informado como parâmetro na tela de geração seja no mesmo período do campo 03 – Data do Inventário da SAFX62\.

Gravar neste campo “Mercadorias Isentas ou Não Tributadas: Final” o total do __campo 19 \(Base Isenta ICMS\) __de todos os registros de inventário que se enquadrem na situação acima\.

OS3480

__RN32__

Registro Tipo 65 campo 07 \- Mercadorias com ICMS Antecipado ou ST: Inicial

__Conteúdo__: Estoque Inicial de mercadorias com ICMS antecipado com encerramento da fase de tributação ou de mercadorias com Substituição Tributária\.

__Tamanho__: 14

__Posição__: 67\-80

__Tipo__: N \(Valor\)

__Regra de Negócio: Se__ na tela de geração for escolhido gerar o inventário a partir da __SAFX52 \(Por Produto\)__:

Selecionar os registros processados da tabela de SAFX52 – Produtos, com os seguintes filtros:

- cod\_empresa = passado como parâmetro
- cod\_estab       = passado como parâmetro
- data\_inventario      = compreendida a data inicial de Inventário passado como parâmetro

Recuperar os registros de todo o inventário dos produtos, onde a data do “Inventário Inicial” informado como parâmetro na tela de geração seja no mesmo período do campo 03 – Data do Inventário da SAFX52\.

Gravar neste campo “Mercadorias com ICMS Antecipado ou ST: Inicial” o total do __campo 29 \(Base de ICMS\-S\)__ de todos os registros de inventário que se enquadrem na situação acima\.

__Se__ na tela de geração for escolhido gerar o inventário a partir da __SAFX62 \(Por NBM\)__:

Selecionar os registros processados da tabela de SAFX62 – NBMs, com os seguintes filtros:

- cod\_empresa = passado como parâmetro
- cod\_estab       = passado como parâmetro
- data\_inventario      = compreendida a data inicial de Inventário passado como parâmetro

Recuperar os registros de todo o inventário por NBMs, onde a data do “Inventário Inicial” informado como parâmetro na tela de geração seja no mesmo período do campo 03 – Data do Inventário da SAFX62\.

Gravar neste campo “Mercadorias com ICMS Antecipado ou ST: Inicial” o total do __campo 21 \(Base de ICMS\-S\)__ de todos os registros de inventário que se enquadrem na situação acima\.

OS3480

__RN33__

Registro Tipo 65 campo 08 \- Mercadorias com ICMS Antecipado ou ST: Final

__Conteúdo__: Estoque Final de mercadorias com ICMS antecipado com encerramento da fase de tributação ou de mercadorias com Substituição Tributária\.

__Tamanho__: 14

__Posição__: 81\-94

__Tipo__: N \(Valor\)

__Regra de Negócio: Se__ na tela de geração for escolhido gerar o inventário a partir da __SAFX52 \(Por Produto\)__:

Selecionar os registros processados da tabela de SAFX52 – Produtos, com os seguintes filtros:

- cod\_empresa = passado como parâmetro
- cod\_estab       = passado como parâmetro
- data\_inventario      = compreendida a data final de Inventário passado como parâmetro

Recuperar os registros de todo o inventário dos produtos, onde a data do “Inventário Final” informado como parâmetro na tela de geração seja no mesmo período do campo 03 – Data do Inventário da SAFX52\.

Gravar neste campo “Mercadorias com ICMS Antecipado ou ST: Final” o total do __campo 29 \(Base de ICMS\-S\)__ de todos os registros de inventário que se enquadrem na situação acima\.

__Se__ na tela de geração for escolhido gerar o inventário a partir da __SAFX62 \(Por NBM\)__:

Selecionar os registros processados da tabela de SAFX62 – NBM’s, com os seguintes filtros:

- cod\_empresa = passado como parâmetro
- cod\_estab       = passado como parâmetro
- data\_inventario      = compreendida a data final de Inventário passado como parâmetro

Recuperar os registros de todo o inventário de NBM, onde a data do “Inventário Final” informado como parâmetro na tela de geração seja no mesmo período do campo 03 – Data do Inventário da SAFX62\.

Gravar neste campo “Mercadorias com ICMS Antecipado ou ST: Final” o total do __campo 21 \(Base de ICMS\-S\)__ de todos os registros de inventário que se enquadrem na situação acima\.

OS3480

__RN34__

Registro Tipo 65 campo 09 \- Outras Mercadorias: Inicial 

__Conteúdo__: Estoque Inicial de outras mercadorias

__Tamanho__: 14

__Posição__: 95\-108

__Tipo__: N \(Valor\)

__Regra de Negócio: Se__ na tela de geração for escolhido gerar o inventário a partir da __SAFX52 \(Por Produto\):__

Selecionar os registros processados da tabela de SAFX52 – Produtos, com os seguintes filtros:

- cod\_empresa = passado como parâmetro
- cod\_estab       = passado como parâmetro
- data\_inventario      = compreendida a data inicial de Inventário passado como parâmetro

Recuperar os registros de todo o inventário dos produtos, onde a data do “Inventário Inicial” informado como parâmetro na tela de geração seja no mesmo período do campo 03 – Data do Inventário da SAFX52\.

Gravar neste campo “Outras Mercadorias: Inicial” o total do __campo 28 \(Base Outras de ICMS\)__ e todos os registros de inventário que se enquadrem na situação acima\.

__Se__ na tela de geração for escolhido gerar o inventário a partir da __SAFX62 \(Por NBM\)__:

Selecionar os registros processados da tabela de SAFX62 – NBMs, com os seguintes filtros:

- cod\_empresa = passado como parâmetro
- cod\_estab       = passado como parâmetro
- data\_inventario  = compreendida a data inicial de Inventário passado como parâmetro\. 

Recuperar os registros de todo o inventário por NBM, onde a data do “Inventário Inicial” informado como parâmetro na tela de geração seja no mesmo período do campo 03 – Data do Inventário da SAFX62\.

Gravar neste campo “Outras Mercadorias: Inicial” o total do __campo 20 \(Base Outras de ICMS\) __de todos os registros de inventário que se enquadrem na situação acima\.

OS3480

__RN35__

Registro Tipo 65 campo 10 \- Outras Mercadorias: Final

__Conteúdo__: Estoque final de outras mercadorias

__Tamanho__: 14

__Posição__: 109\-122

__Tipo__: N \(Valor\)

__Regra de Negócio: Se__ na tela de geração for escolhido gerar o inventário a partir da __SAFX52 \(Por Produto\):__

Selecionar os registros processados da tabela de SAFX52 – Produtos, com os seguintes filtros:

- cod\_empresa = passado como parâmetro
- cod\_estab       = passado como parâmetro
- data\_inventario      = compreendida a data inicial de Inventário passado como parâmetro

Recuperar os registros de todo o inventário dos produtos, onde a data do “Inventário Final” informado como parâmetro na tela de geração seja no mesmo período do campo 03 – Data do Inventário da SAFX52\.

Gravar neste campo “Outras Mercadorias: Final” o total do __campo 28 \(Base Outras de ICMS\)__ e todos os registros de inventário que se enquadrem na situação acima\.

__Se__ na tela de geração for escolhido gerar o inventário a partir da __SAFX62 \(Por NBM\)__:

Selecionar os registros processados da tabela de SAFX62 – NBMs, com os seguintes filtros:

- cod\_empresa = passado como parâmetro
- cod\_estab       = passado como parâmetro
- data\_inventario  = compreendida a data inicial de Inventário passado como parâmetro\. 

Recuperar os registros de todo o inventário por NBM, onde a data do “Inventário Final” informado como parâmetro na tela de geração seja no mesmo período do campo 03 – Data do Inventário da SAFX62\.

Gravar neste campo “Outras Mercadorias: Final” o total do __campo 20 \(Base Outras de ICMS\) __de todos os registros de inventário que se enquadrem na situação acima\.

OS3480

__RN36__

Registro Tipo 65 campo 11 \- Indicador do critério de apuração do Lucro Bruto

__Conteúdo__: Apuração do Lucro Bruto

__Tamanho__: 01

__Posição__: 123\-123

__Tipo__: Alfanumérico

__Regra de Negócio: __

O usuário deverá selecionar este indicador para definir o conteúdo do campo “Lucro Bruto” no Módulo Estadual → DAC\-AL → Manutenção → Registro Tipo 65 – Estoque e Balanço

Quando o usuário escolher a opção “Presumido”, deverá ser informado neste campo o conteúdo “__P__”, caso o contrário, o usuário escolher a opção “Real”, deverá ser informado neste campo o conteúdo “__L__”\.

OS3480

__RN37__

Registro Tipo 65 campo 12 \- Indicador do Sistema de Inventário

__Conteúdo__: Sistema de Inventário

__Tamanho__: 01

__Posição__: 124\-124

__Tipo__: Alfanumérico__ __

__Regra de Negócio: __

O usuário deverá selecionar este indicador para definir o conteúdo do campo “Sistema de Inventário” no Módulo Estadual → DAC\-AL → Manutenção → Registro Tipo 65 – Estoque e Balanço

Quando o usuário escolher a opção “Anual”, deverá ser informado neste campo o conteúdo “__A__”, caso o contrário, o usuário escolher a opção “Periódico”, deverá ser informado neste campo o conteúdo “__P__”

OS3480

__RN38__

Registro Tipo 65 campo 13 \- Indicador do Método de Cálculo do Estoque

__Conteúdo__: Método de Cálculo do Estoque

__Tamanho__: 01

__Posição__: 125\-125

__Tipo__: Alfanumérico

__Regra de Negócio: __

O usuário deverá selecionar este indicador para definir o conteúdo do campo “Cálculo do Estoque” no Módulo Estadual → DAC\-AL → Manutenção → Registro Tipo 65 – Estoque e Balanço

Quando o usuário escolher a opção “Custo Médio”, deverá ser informado neste campo o conteúdo “__M__”, caso o contrário, o usuário escolher a opção “PEPS”, deverá ser informado neste campo o conteúdo “__P__”

OS3480

__RN39__

Registro Tipo 65 campo 14 \- Número de Empregados

__Conteúdo__: Quantidade de Empregados

__Tamanho__: 05

__Posição__: 126\-130

__Tipo__: Numérico

__Regra de Negócio: __

O usuário deverá preencher o campo “Número de Empregados” no Módulo Estadual → DAC\-AL → Manutenção → Registro Tipo 65 – Estoque e Balanço, para definir o conteúdo deste campo\.

OS3480

__RN40__

Registro Tipo 65 campo 15 – Outras Receitas

__Conteúdo__: Valor de Outras Receitas obtidas

__Tamanho__: 14

__Posição__: 131\-144

__Tipo__: N \(Valor\)

__Regra de Negócio: __

O usuário deverá preencher o campo “Outras Receitas” no Módulo Estadual → DAC\-AL → Manutenção → Registro Tipo 65 – Estoque e Balanço, para definir o valor deste campo\.

OS3480

__RG66__

Gerar o __Registro Tipo 66__ __\(Quadro X\)__ – Dados Contábeis quando o parâmetro “__Gerar informações anuais consolidadas__”, estiver marcado\. 

Este registro é gerado conforme empresa e estabelecimento selecionado, na data passada pelo parâmetro na tela de Geração de Registros\.

As informações deste registro serão preenchidas pelo usuário via tela de manutenção\. Deverá ser gravado na tabela apenas um registro por período \(Ano\)\. 

Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração dos Registros estiver marcado, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As informações deverão ser cadastradas sempre em nome do estabelecimento centralizador\. 

OS3480

__RN41__

Registro Tipo 66 campo 01 – TIPO

 

__Conteúdo__: TIPO

__Tamanho__: 02

__Posição__: 01\-02

__Tipo__: Numérico

__Regra de Negócio: __Deverá ser preenchido com o conteúdo fixo “__66__”\.

OS3480

__RN42__

Registro Tipo 66 campo 02 \- Ativo Circulante: Inicial

__Conteúdo__: Ativo Circulante: Inicial

__Tamanho__: 14

__Posição__: 03\-16

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN43__

Registro Tipo 66 campo 03 \- Ativo Circulante: Final

__Conteúdo__: Ativo Circulante: Final

__Tamanho__: 14

__Posição__: 17\-30

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN44__

Registro Tipo 66 campo 04 \- Disponibilidades: Inicial

__Conteúdo__: Disponibilidades: Inicial

__Tamanho__: 14

__Posição__: 31\-44

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN45__

Registro Tipo 66 campo 05 \- Disponibilidades: Final

__Conteúdo__: Disponibilidades: Final

__Tamanho__: 14

__Posição__: 45\-58

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN46__

Registro Tipo 66 campo 06\- Clientes: Inicial

__Conteúdo__: Clientes: Inicial

__Tamanho__: 14

__Posição__: 59\-72

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN47__

Registro Tipo 66 campo 07 \- Clientes: Final

__Conteúdo__: Clientes: Final

__Tamanho__: 14

__Posição__: 73\-86

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN48__

Registro Tipo 66 campo 08 \- Outras Contas a Receber: Inicial

__Conteúdo__: Outras Contas a Receber: Inicial__ __

__Tamanho__: 14

__Posição__: 87\-100

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN49__

Registro Tipo 66 campo 09 \- Outras Contas a Receber: Final

__Conteúdo__: Outras Contas a Receber: Final__ __

__Tamanho__: 14

__Posição__: 101\-114

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN50__

Registro Tipo 66 campo 10 \- Ativo Permanente: Inicial

__Conteúdo__: Ativo Permanente: Inicial

__Tamanho__: 14

__Posição__: 115\-128

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN51__

Registro Tipo 66 campo 11 \- Ativo Permanente: Final

 

__Conteúdo__: Ativo Permanente: Final

__Tamanho__: 14

__Posição__: 129\-142

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN52__

Registro Tipo 66 campo 12 \- Ativo Imobilizado: Inicial

__Conteúdo__: Ativo Imobilizado: Inicial

__Tamanho__: 14

__Posição__: 143\-156

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN53__

Registro Tipo 66 campo 13 \- Ativo Imobilizado: Final

__Conteúdo__: Ativo Imobilizado: Final

__Tamanho__: 14

__Posição__: 157\-170

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN54__

Registro Tipo 66 campo 14 \- Passivo Circulante: Inicial

__Conteúdo__: Passivo Circulante: Inicial

__Tamanho__: 14

__Posição__: 171\-184

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN55__

Registro Tipo 66 campo 15 \- Passivo Circulante: Final

__Conteúdo__: Passivo Circulante: Final

__Tamanho__: 14

__Posição__: 185\-198

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN56__

Registro Tipo 66 campo 16 \- Fornecedores: Inicial

__Conteúdo__: Fornecedores: Inicial

__Tamanho__: 14

__Posição__: 199\-212

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN57__

Registro Tipo 66 campo 17 \- Fornecedores: Final

__Conteúdo__: Fornecedores: Final

__Tamanho__: 14

__Posição__: 213\-226

__Tipo__: N

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN58__

Registro Tipo 66 campo 18 \- Empréstimos e Financiamentos: Inicial

__Conteúdo__: Empréstimos e Financiamentos: Inicial

__Tamanho__: 14

__Posição__: 227\-240

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN59__

Registro Tipo 66 campo 19 \- Empréstimos e Financiamentos: Final

__Conteúdo__: Empréstimos e Financiamentos: Final

__Tamanho__: 14

__Posição__: 241\-254

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN60__

Registro Tipo 66 campo 20 \- Outras Contas a Pagar: Inicial

__Conteúdo__: Outras Contas a Pagar: Inicial__ __

__Tamanho__: 14

__Posição__: 255\-268

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN61__

Registro Tipo 66 campo 21 \- Outras Contas a Pagar: Final

__Conteúdo__: Outras Contas a Pagar: Final__ __

__Tamanho__: 14

__Posição__: 269\-282

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN62__

Registro Tipo 66 campo 22 \- Patrimônio Líquido: Inicial

__Conteúdo__: Patrimônio Líquido: Inicial

__Tamanho__: 14

__Posição__: 283\-296

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN63__

Registro Tipo 66 campo 23 \- Patrimônio Líquido: Final

__Conteúdo__: Patrimônio Líquido: Final

__Tamanho__: 14

__Posição__: 297\-310

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN64__

Registro Tipo 66 campo 24 \- Total Passivo: Inicial

__Conteúdo__: Total Passivo: Inicial

__Tamanho__: 14

__Posição__: 311\-324

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN65__

Registro Tipo 66 campo 25 \- Total Passivo: Final

__Conteúdo__: Total Passivo: Final

__Tamanho__: 14

__Posição__: 325\-338

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN66__

Registro Tipo 66 campo 26 \- Lucro Bruto: Inicial

__Conteúdo__: Lucro Bruto: Inicial

__Tamanho__: 14

__Posição__: 339\-352

__Tipo__: N

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN67__

Registro Tipo 66 campo 27 \- Lucro Bruto: Final

__Conteúdo__: Lucro Bruto: Final

__Tamanho__: 14

__Posição__: 353\-366

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN68__

Registro Tipo 66 campo 28 \- Lucro Líquido: Inicial

__Conteúdo__: Lucro Líquido: Inicial

__Tamanho__: 14

__Posição__: 367\-380

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN69__

Registro Tipo 66 campo 29 \- Lucro Líquido: Final

__Conteúdo__: Lucro Líquido: Final

__Tamanho__: 14

__Posição__: 381\-394

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RG67__

Registro Tipo 67 – Dados do Consumo de Energia

Gerar o __Registro Tipo 67__ \(__Quadro X__\) – Dados do Consumo de Energia__ __quando o parâmetro “__Gerar informações anuais consolidadas__”, estiver marcado\. 

Este registro é gerado conforme empresa e estabelecimento selecionado, na data passada pelo parâmetro na tela de Geração de Registros\.

As informações deste registro serão preenchidas pelo usuário via tela de manutenção\. Deverá ser gravado na tabela um ou mais registros por período \(Ano\)\. 

Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração dos Registros estiver marcado, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As informações deverão ser cadastradas sempre em nome do estabelecimento centralizador\. 

OS3480

__RN70__

Registro Tipo 67 campo 01 \- TIPO

__Conteúdo:__ Tipo de Registro

__Tamanho__: 02

__Posição__: 01\-02

__Tipo__: Numérico

__Regra de Negócio: __Deverá ser preenchido com o conteúdo fixo “__67__”\.

OS3480

__RN71__

Registro Tipo 67 campo 02 – Número do Medidor

__Conteúdo:__ Número do Medidor de Energia

__Tamanho__: 08

__Posição__: 03\-10

__Tipo__: Numérico

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN72__

Registro Tipo 67 campo 03 – Consumo

__Conteúdo:__ Quantidade de Consumo

__Tamanho__: 14

__Posição__: 11\-24

__Tipo__: Numérico

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RG68__

Gerar o __Registro Tipo 68 \(Quadro XI\) – Outras Despesas no Período__ quando o parâmetro “__Gerar informações anuais consolidadas__”, estiver marcado\. 

Este registro é gerado conforme empresa e estabelecimento selecionado, na data passada pelo parâmetro na tela de Geração de Registros\.

As informações deste registro serão preenchidas pelo usuário via tela de manutenção\. Deverá ser gravado na tabela um ou mais registros por período \(Ano\)\. 

Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração dos Registros estiver marcado, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As informações deverão ser cadastradas sempre em nome do estabelecimento centralizador\. 

OS3480

__RN73__

Registro Tipo 68 campo 01 – TIPO

__Conteúdo:__ Tipo de registro

__Tamanho__: 02

__Posição__: 01\-02

__Tipo__: Numérico

__Regra de Negócio: __Deverá ser preenchido com o conteúdo fixo “__68__”\.

OS3480

__RN74__

Registro Tipo 68 campo 02 – Código da Despesa

__Conteúdo:__ Código da despesa conforme tabela

__Tamanho__: 03

__Posição__: 03\-05

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RN75__

Registro Tipo 68 campo 03 – Valor

__Conteúdo:__ Valor Total das despesas que se enquadram neste código

__Tamanho__: 14

__Posição__: 06\-19

__Tipo__: N \(Valor\)

__Regra de Negócio: __Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção

OS3480

__RG90__

Gerar o __Registro Tipo 90– Totalizador da DAC__ 

Deverá ter somatório do Registro Tipo 90 – Totalizador da DAC\. 

Os novos registros 65, 66, 67 e 68 deverão compor também esta totalização da quantidade de registros\.

OS3480

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


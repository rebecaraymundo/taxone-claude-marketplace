# MTZ-eSocial-Geracao-Evento-S1250-Aquisicao-Producao-Rural

- **Fonte:** MTZ-eSocial-Geracao-Evento-S1250-Aquisicao-Producao-Rural.docx
- **Modificado:** 2022-06-07
- **Tamanho:** 99 KB

---

THOMSON REUTERS

Módulo eSocial

Geração do Evento S\-1250

\(Aquisição de Produção Rural\) 

__Localização__: Menu SPED, módulo Informações para o eSocial, menu Geração à Geração do Evento S\-1250

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS16769__

Geração do evento S\-1250

Geração dos dados do evento S\-1250 \(Aquisição de Produção Rural\)

01/10/2018 

\(criação do documento\)

__MFS22083__

Lara Aline

Inclusão da geração do evento S\-1250 a partir da SAFX63

12/11/2018

__MFS22920__

Lara Aline

Inclusão do no campo indOpcCP na tag ideProdutor e inclusão da nova tag infoProcJ de acordo com o novo Layout 2\.5\.

19/12/2018

__MFS23266__

Lara Aline 

Ajuste na geração do campo indOpcCP

27/12/2018

__MFS23741__

Liliane Assaf

CH380/2019 \- DW \- SPED \- E\-SOCIAL \- Sistema não faz a geração do evento S\-1250 quando o campo Indicador do Código da SAFX04 está como 1\-Código\.

Solução: 

Retirar o seguinte critério de seleção na recuperação da SAFX07 e SAFX63:

 \- Campo Indicador do Conteúdo do Código \(IND\_CONTEM\_COD\) da SAFX04 preenchido com o conteúdo igual a “2”\.

16/01/2018

__MFS25893__

Andréa Rocha

Alteração da geração dos registros infoProcJud e infoProcJ

04/04/2019

__MFS25120__

Eduardo Cruz

Alteracão da regra do campo indOpcCP

08/04/2019

__MFS28125__

Liliane Assaf

Tratamento para Dedução de Devolução para geração a partir da SAFX63

17/06/2019

__MFS28766__

Liliane Assaf

Tratamento para Valor Negativo no Cálculo da Dedução de Devolução \(Origem SAFX07 e SAFX63\)

16/07/2019

__MFS\-58457__

Alessandra Cristina Navatta

Inclusão de regra no campo indOpcCP \(do evento S\-1250, Registro ideProdutor\), para considerar a informação do campo 33\-IND\_TRIB\_PRODUTOR\_CP da SAFX63, quando este estiver preenchido\.

13/01/2021

__MFS60476__

Rogério Ohashi

Alteração de regra do Campo “nrInscProd”__, incluir__ a condição do Campo 27 \- Classe de Empresa” __diferente__ de "05 – MEI \(Micro Empreendedor Individual\)\. Tratamento para evitar “impactos” devido inclusão de regra para atender, também, os eventos S\-1200 e S\-1210 para fornecedores autônomos MEI\.

25/03/2021

__MFS66155__

Andréa Rocha

Inclusão da verificação dos códigos 4 e 5 para o campo tipo de aquisição, para as notas de devolução

08/06/2021

__MFS\-87543__

__Elisabete Costa__

__Exclusão do Evento S\-1250 \- Para versão S\-1\.0__

__06/06/2022__

Sumário

[1\.	Parâmetros da Tela	3](#_Toc74046981)

[2\.	Recuperação dos Dados e Processamento	3](#_Toc74046982)

[3\.	Verificação do Status de Eventos já Gerados	7](#_Toc74046983)

[4\.	Gravação dos Dados	9](#_Toc74046984)

__A partir da versão S\-1\.0 não deve ser gerado o evento S\-1250__

__\[MFS\-87543\]__

# <a id="_Toc74046981"></a>Parâmetros da Tela 

Este documento é específico das regras de geração do evento S\-1250\.

Para consultar a tela da geração e o funcionamento dos parâmetros, ver documento “*MTZ\_Tela\_Geracao\_Evento\_S1250*”\.

Nesta geração os dados serão armazenados em tabelas, já com o formato e hierarquia exigidos no layout do eSocial, para posterior conferência do usuário, e geração dos arquivos XML\.

# <a id="_Toc350763252"></a><a id="_Toc74046982"></a>Recuperação dos Dados e Processamento

Origem dos dados: \- Parametrização “Dados Iniciais” do Módulo eSocial;

                               \- Cadastro do Estabelecimento;

                               \- SAFX04 \- Arquivo de Cadastro de Pessoas Físicas/Jurídicas;

                               \- SAFX07 \- Arquivo de Notas Fiscais;

                               \- SAFX263 \- Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte;

                               \- SAFX271 \- Processos Judiciais com decisão/sentença – Produtor Rural;

                               \- SAFX63 \- Funrural

Critérios para a recuperação dos dados da parametrização “Dados Iniciais”:

     Esta parametrização é por estabelecimento centralizador, e para recuperar os dados, considerar:

     \- Estabelecimento – estabelecimento selecionado na tela da geração no caso desse ser o centralizador ou estabelecimento selecionado na tela da geração no caso desse estar centralizado ao estabelecimento centralizador parametrizado nos Dados Iniciais; 

A partir da versão S1\.0 esse evento não será mais gerado\.

Critérios para a recuperação dos registros dependerá da seleção do parâmetro ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais\.

- Se ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ estiver __marcado__, então: 

A recuperação será pela tabela __SAFX63__\. Veja os critérios:

     \- __Empresa__ – Empresa do estabelecimento selecionado na geração;

     \- __Estabelecimento__ – Estabelecimento selecionado na geração;

     \- __Data Movimento__ – O campo DATA\_MOVTO deve compreender o período de geração da tela \(campo “Período”\); 

     \- __Movimento Entrada/Saída__ – O campo TIP\_MOV\_ES seja igual “1” ou "2";

     \- __Tipo de Aquisição/Comercialização da Produção __– O campo IND\_TIPO\_AQUIS – SAFX63 deve ser “1” ou “2” ou “3” ou ”4” ou “5” ou “6”\. 

- Se ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ estiver __desmarcado__, então:

A recuperação será pela tabela __SAFX07 __como padrão\. Os critérios são::

     \- __Empresa__ – Empresa do estabelecimento selecionado na geração;

     \- __Estabelecimento__ – Estabelecimento selecionado na geração;

     \- __Data Fiscal__ – O campo DATA\_FISCAL deve compreender o período de geração da tela \(campo “Período”\); 

     \- __Movimento Entrada/Saída__ – O campo MOVTO\_E\_S seja igual “1” ou "2";

     \- __Situação__ – O campo SITUACAO deve ser diferente de "S";

     \- __Classificaçao Fiscal__ – O campo COD\_CLASS\_DOC\_FIS deve ser igual a "1" ou "3";

     \- __Tipo de Aquisição/Comercialização da Produção __– O campo IND\_TIPO\_AQUIS – SAFX07 deve ser “1” ou “2” ou “3” ou ”4” ou “5” ou “6”\. 

<a id="_Hlk524448874"></a>__Agrupamento dos dados:__

A geração desse evento S\-1250 é diferente dos outros eventos que já geramos nesse módulo, visto que para os outros eventos geramos por estabelecimento Centralizador e esse evento S\-1250 é por estabelecimento, ou seja, um evento para cada estabelecimento seja ele centralizador ou centralizado, de acordo com o estabelecimento escolhido na tela de geração\.

Para cada estabelecimento será gerado um evento S\-1250, com as informações descritas no item “Gravação dos Dados”\. 

- As aquisições recuperadas para cada estabelecimento, serão agrupadas e totalizadas pelas seguintes informações:

     \- Tipo de Aquisição \(campo 276\-Tipo de Aquisição/Comercialização da Produção\-SAFX07/campo 32\-Tipo de Aquisição\-SAFX63\);

     \- Campo a ser totalizado: \(campo 23\-Valor Total do Documento Fiscal\-SAFX07/campo 19\-Valor do Documento Fiscal\-SAFX63\)

O resultado de cada totalização irá gerar um registro __tpAquis__\. Para cada estabelecimento adquirente poderá existir de 1 a 6 tipo de aquisição diferente\. 

Para cada Tipo de Aquisição poderão existir vários Produtores Rurais dos quais foram efetuadas a aquisição da produção, os produtores recuperados para cada estabelecimento, serão agrupados e totalizados pelas seguintes informações:

     \- Tipo de Aquisição \(campo 276\-Tipo de Aquisição/Comercialização da Produção/ campo 32\-Tipo de Aquisição\-SAFX63\);

     \- Tipo Inscrição Produtor: CNPJ ou CPF

     \- Produtor: \(06\- CPF\-CGC/69 \- CPF do Proprietário da Fazenda SP \(São Paulo\)\-SAFX04 ou 289 \- CPF/CNPJ do Consumidor\) 

     \- Campo a ser totalizado: 22\-Valor do Produto\-SAFX07 ou 20\-Valor do Produto\-SAFX63, 243\-Valor Contrib Previd s/ Produção Rural Sub\-rogação\-SAFX07 ou 24\-Valor da Contribuição\-SAFX63, 287\-Valor da GILRAT\-SAFX07 ou 30\-Valor da GILRAT\-SAFX63, 288\-Valor da Contribuição Destinada ao SENAR\-SAFX07 ou 26\-Valor do Senar\-SAFX63\.

O resultado de cada totalização irá gerar um registro __ideProdutor__\. Para cada Tipo de Aquisição poderá existir de 1 a 9999 produtores diferentes\. 

__Sobre o desconto das devoluções \(Parâmetros > Devoluções de Aquisição de Produtor Rural \(S\-1250\):     __

O valor total das aquisições \(registro tpAquis\), assim como os valores de cada produtor rural \(registro ideProdutor\), passaram a ter uma dedução referentes às devoluções que possam existir no período\. As devoluções também são contabilizadas por produtor rural, da mesma forma feita para as aquisições, com objetivo de garantir que a dedução seja feita nos valores do produtor rural correto\. 

Este procedimento sobre as devoluções é realizado __apenas__ para os produtores rurais = __pessoa física__\. 

Para produtor = pessoa jurídica não é possível deduzir as devoluções, pois neste caso teríamos uma inconsistência entre os valores das notas \(registro “nfs”\), e os registros “pai”\. Lembrando que, o detalhamento das notas das aquisições no registro “nfs” é feito apenas quando o produtor rural é pessoa jurídica\.

Para produtor rural pessoa física o registro das notas não é gerado, conforme regra do layout do e\-Social vrs 2\.4\.02

__\[MFS66155__\] Inclusão da verificação dos códigos 4 e 5 para o campo tipo de aquisição, pois também se tratam de códigos relacionados a pessoa física

Critérios da recuperação das notas de devolução:

- Se ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ estiver __desmarcado__: 

A recuperação será pela tabela __SAFX07__\. Veja os critérios:

\- Notas de saída \(MOVTO\_E\_S = 9\);

\- Notas de Devolução \(NORM\_DEV = 2\);

\- Data Fiscal no período da geração;

\- O CFOP da capa \(SAFX07\) deve constar na parametrização das devoluções \(menu <a id="_Hlk524440481"></a>Parâmetros > Devoluções de Aquisição de Produtor

   Rural \(S\-1250\)\);

\- O campo 276\-IND\_TIPO\_AQUIS da SAFX07 deve ser = “1” ou “2” ou “4” ou “5” \(opções usadas para compra de produtor pessoa física\);

\[__MFS28125\]__

- Se ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ estiver __marcado__: 

A recuperação será pela tabela __SAFX63__\. Veja os critérios:

\- Notas de saída \(campo 05 \- Movimento Entrada/Saída TIP\_MOV\_ES = 9 da SAFX63\);

\- Data Movimento no período da geração \(campo 03 \- DATA\_MOVTO da SAFX63\);

\- O CFOP \(campo 13 \- Código Fiscal da SAFX63\) deve constar na parametrização das devoluções \(menu Parâmetros > Devoluções de Aquisição de Produtor Rural \(S\-1250\)\);

\- O Tipo de Aquisição \(campo 32\- IND\_TIPO\_AQUIS\) deve ser = “1” ou “2” ou “4” ou “5” \(opções usadas para compra de produtor pessoa física\);

Tratamento das notas de devolução:

\- Se o total dos valores das Aquisições menos o total dos valores das Devoluções para o produtor rural for menor ou igual a zero, o registro deste Produtor \(registro ideProdutor\) não deverá ser gerado\.  

\[__MFS28766\]__

Neste caso será gravada a seguinte mensagem no log:

*O Produtor Rural não foi gerado, pois o Valor Total das Devoluções excedeu ou foi igual ao das Aquisições do produtor rural no período\. O valor Bruto deve ser maior que zero\.*

*Dados do Registro: Indicativo da Aquisição: XX' \- Inscrição do Produtor: XXXXXXXXXXX*

# <a id="_Toc509582647"></a><a id="_Toc509925718"></a><a id="_Toc509929675"></a><a id="_Toc74046983"></a>Verificação do Status de Eventos já Gerados

O objetivo é verificar se o evento pode ou não ser regerado, o que depende do status que constar na tabela da geração \(ESOCIAL\_PGER\_S1250\_OC, coluna IND\_STATUS\)\.

Para cada estabelecimento a ser gerado, conforme os critérios descritos no item 2, será verificado se já existe um evento gerado para este estabelecimento no mesmo período de referência\.

__Caso não:__ 

      O evento do trabalhador será gerado normalmente, como definido no item “*4\-Gravação dos Dados*”\.  

__Caso sim:__ 

      A geração de um novo evento para o estabelecimento dependerá do status do evento já existente, da seguinte forma:

__Status__

__Permite regeração dos dados__

1\-Aguardando geração XML

Sim

3\-Enviando para mensageria

Não

4\-Erro geração XML

Sim

5\-Evento recebido pela mensageria

Não

6\-Evento rejeitado pela mensageria

Sim 

7\-Em Processamento \(mensageria\)

Não

8\-Recebido pelo Fisco com sucesso

Sim \(Retificação\)

9\-Recebido pelo Fisco com advertência

Sim \(Retificação\)

10\-Rejeitado pelo Fisco

Sim

12\-Evento Excluído

Sim

14\-Evento excluído na mensageria

Sim

15\-Erro técnico na mensageria

Sim__ __

         Se o status do evento já existente __não__ __permitir regeração__:

Nesse caso, o estabelecimento em questão será desconsiderado da geração, e será gravada a seguinte mensagem de aviso no log:

*                  Aviso: Já existe evento anterior gerado para o estabelecimento\. O status do evento não permite uma nova geração\.*

*                  Dados do Registro:  Estabelecimento:  X / XXXXXXXXXXXXXXXXX, *__*Período*__*: XX/XXXX *

         Se o status do evento já existente __permitir regeração__:

             Nesse caso, o movimento em questão será regerado, mas, poderá ser como uma operação __ORIGINAL__ ou uma

             __RETIFICAÇÃO__, dependendo do status do evento original, como descrito a seguir:

              \- Se status do evento original = 8 ou = 9 à Nesse caso, o novo evento será gerado como __RETIFICAÇÃO__;

              \- Se status do evento original <> 8 e <> 9 à Nesse caso, o novo evento será gerado como __ORIGINAL__;

*Sobre a limpeza do evento já existente: Se o status do evento já existente for = *__*1*__* \(Aguardando geração XML\), *__*4*__* \(Erro geração XML\) ou *__*14*__* \(Evento excluído na mensageria\), este evento será apagado ao efetuar a regeração de um novo evento\. Nos demais casos, a limpeza do evento já existente não será feita \(para manter o histórico dos erros ocorridos\), e será feita apenas a regeração de um novo evento\.*

<a id="_Hlk523235760"></a><a id="_Hlk523155984"></a>__Importante:__ Na tela Geração dos Movimentos serão gerados APENAS os eventos Originais, os eventos de Retificação deverão ser gerados diretamente pelo Painel de Controle de Eventos pela opção ‘Reprocessar Evento’\. Caso os eventos encontrados na tela de Geração dos Movimentos sejam identificados nos critérios como Retificação \(Critérios estão no documento de tela do Painel de Controle de Eventos\) esses deverão ser desconsiderados e não gerados, pela tela de Geração dos Movimentos serão gerados apenas os eventos que se enquadrarem como ‘Original’\. 

# <a id="_Toc74046984"></a>Gravação dos Dados

Conforme descrito acima \(“Agrupamento dos dados”\), será gerado um evento S\-1250 __para cada estabelecimento__, com as seguintes informações: 

*\(os registros não citados não serão gerados\)*

__Registro evtAqProd__ – Evento Aquisição de Produção

id

Identificação do evento, conforme REGRA\_VALIDA\_ID\_EVENTO: 

“ID” \+ “1” \+ CNPJ do estabelecimento \+ data da geração \(AAAAMMDD\) \+ hora da geração \(HHMMSS\) \+ sequencial

<a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>CNPJ – 8 primeiras posições do CNPJ, completando com zeros à direita;

Sequencial \(99999\) \- Número sequencial da chave\. Deve ser incrementado apenas quando houver a geração de eventos na mesma data/hora\. 

__Registro ideEvento__ \- Informações de Identificação do evento\.

indRetif

Este campo será gerado de acordo com a verificação de status descrita no item “*3\-Verificação do Status de Eventos já Gerados*”:

__Se__ for a primeira geração do evento do trabalhador no período:

      O campo será gerado com “__1__” \(__Arquivo Original__\);

__Senão__

      Neste caso o preenchimento do campo depende do status do evento gerado anteriormente:

      Se status do evento original = 8 ou = 9 à O campo será gerado com “__2__” \(__Retificação__\);

      Se status do evento original <> 8 e <> 9 à O campo será gerado com “__1__” \(__Arquivo Original__\);

nrRecibo

Este campo será gerado de acordo com o conteúdo do campo anterior \(__indRetif__\), da seguinte forma:

Se indRetif = “1” \(Arquivo Original\)

     Nesse caso este campo *não* será gerado;

Se indRetif = “2” \(Retificação\)

     Nesse caso este campo será gravado com o número do recibo do arquivo a ser retificado\. Ou seja, com o conteúdo

     do campo nrRecibo que consta no *evento original*;

 

indApuracao

Conteúdo fixo = “1” \(= Mensal\)

perApur

Mês e ano do período informado na tela da geração, no formato AAAA\-MM \(conforme orientação do layout\)

tpAmb

Campo “Tipo de ambiente” da parametrização “Dados Iniciais” \(ver acima a regra para a recuperação dos dados desta parametrização\)

procEmi

Conteúdo fixo = “1” \(= Aplicativo do empregador\)

verProc 

Versão do sistema DW\. Esta informação é gerada de forma fixa = “V2R010”\. 

*Obs: A princípio, a definição previa informar neste campo a versão do eSocial informada na tela da geração\. No entanto, este entendimento é equivocado, pois como descreve o manual trata\-se da versão do aplicativo \(do empregador ou governamental\) utilizado para gerar o evento\. No caso, trata\-se da versão do próprio DW\. O REINF já trabalha desta forma\.*

__Registro ideEmpregador__ \- Informações de identificação do empregador\.

tpInsc

Conteúdo fixo = “1”

nrInsc

CNPJ do estabelecimento, considerando apenas as 8 primeiras posições do CNPJ, completando com zeros à direita;

__Registro ideEstabAdquir__\- Informações do estabelecimento adquirente da produção\.

Este registro servirá para identificar a qual estabelecimento se referem as notas que serão demonstradas\. Como vamos gerar um arquivo por estabelecimento, demonstrará o CNPJ do estabelecimento de geração\.

tpInscAdq

Conteúdo fixo = “1”

nrInscAdq

CNPJ do estabelecimento

__Registro __<a id="_Hlk523501001"></a>__tpAquis__ \- Informações da aquisição de produtos rurais\.

Caso o parâmetro ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais esteja selecionado as informações da aquisição serão recuperadas no seu cadastro na __SAFX63, __sempre que:  

__\[MFS23741\]__

\- O campo Movimento Entrada/Saída \(MOVTO\_E\_S\) esteja preenchido com o conteúdo igual a “1”;

\- A pessoa física/ jurídica relacionada esteja com o campo Indicador do Conteúdo do Código \(IND\_CONTEM\_COD\) da SAFX04 preenchido com o conteúdo igual a “2”;

\- O campo Tipo de Aquisição \(IND\_TIPO\_AQUIS\) da SAFX63 esteja preenchido com o conteúdo igual a “1” ou “2” ou “3”;

\- A Data do Movimento compreenda o período parametrizado na geração;

__OU__

\- O campo Movimento Entrada/Saída \(MOVTO\_E\_S\) esteja preenchido com o conteúdo igual a “2”;

\- O campo Tipo de Aquisição \(IND\_TIPO\_AQUIS\) da SAFX63 esteja preenchido com o conteúdo igual a “1” ou “2” ou “3” ou ”4” ou “5” ou “6”;

\- A Data do Movimento compreenda o período parametrizado na geração\. 

Caso o parâmetro ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais NÃO esteja selecionado as informações da aquisição serão recuperadas no seu cadastro na __SAFX07, __sempre que:  

__\[MFS23741\]__

\- O campo Movimento Entrada/Saída \(MOVTO\_E\_S\) esteja preenchido com o conteúdo igual a “1”;

\- A pessoa física/ jurídica relacionada esteja com o campo Indicador do Conteúdo do Código \(IND\_CONTEM\_COD\) da SAFX04 preenchido com o conteúdo igual a “2”;

\- O campo Tipo de Aquisição/Comercialização da Produção \(IND\_TIPO\_AQUIS\) da SAFX07 esteja preenchido com o conteúdo igual a “1” ou “2” ou “3”;

\- A Data Fiscal compreenda o período parametrizado na geração;

__OU__

\- O campo Movimento Entrada/Saída \(MOVTO\_E\_S\) esteja preenchido com o conteúdo igual a “2”;

\- O campo Tipo de Aquisição/Comercialização da Produção \(IND\_TIPO\_AQUIS\) da SAFX07 esteja preenchido com o conteúdo igual a “1” ou “2” ou “3” ou ”4” ou “5” ou “6”;

\- A Data Fiscal compreenda o período parametrizado na geração\. 

Poderão existir até 6 registros de aquisição, e para cada registro recuperado, será gerado um registro __tpAquis, __com as informações descritas abaixo:

indAquis

Campo 276\-Tipo de Aquisição/Comercialização da Produção da SAFX07

Caso o parâmetro ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais esteja selecionado o campo a ser recuperado será:

Campo 32\-Tipo de Aquisição da SAFX63

vlrTotAquis

Campo 23\-Valor Total do Documento Fiscal da SAFX07\.

Caso o parâmetro ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais esteja selecionado o campo a ser recuperado será:

Campo 19\-Valor do Documento Fiscal da SAFX63

Quando se tratar de produtor rural __pessoa física__, será deduzido deste valor o correspondente ao mesmo valor das notas fiscais de devolução\.

\(ver regra geral sobre as devoluções na Recuperação dos Dados e Processamento\)\.

Este campo deve corresponder ao somatório do Valor Bruto do registro de ideProdutor

__Registro ideProdutor__ \- Informações de identificação do produtor\.

As informações do produtor serão recuperadas no seu cadastro na __SAFX04__, através dos campos “06\-Indicador da Pessoa Fis/Jur” e “07\-Código da Pessoa Fis/Jur” da SAFX07 ou dos campos “06\- Indicador Pessoa Física/Jurídica” e “07\- Código/Destinatário/Emitente/Remetente” da SAFX63\.

Havendo mais de um registro da pessoa fis/jur na SAFX04, será considerado o registro de > data de validade cujo mês/ano seja <= ao mês/ano do período informado na tela da geração\. 

Poderão existir vários produtores e para cada um deles será gerado um registro __ideProdutor__, com as seguintes informações:

tpInscProd

Gravar ‘1’ \- CNPJ ou ‘2’ \- CPF\.

nrInscProd

\[__ALTERAÇÃO\- MFS60476\]__ Tratamento para fornecedores MEI não serem considerados na geração do evento S\-1250\.

Se o parâmetro ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais esteja selecionado:

Caso existir informação no campo CPF\_SP da tabela definitiva da SAFX04, gerar o campo com a informação desse campo CPF\_SP, caso contrário:

Caso existir informação no campo CPF\_SP da tabela definitiva da SAFX04 \(X04\_PESSOA\_FIS\_JUR\), __E se__ o Campo IND\_CLASSE\_EMP, \(Campo 27 \- Classe de Empresa\), da tabela X04\_PESSOA\_FIS\_JUR __for__ __diferente__ a "05 – MEI \(Micro Empreendedor Individual\)"\. gerar o campo com a informação do campo CPF\_SP, caso contrário:

Gerar o campo com a informação do campo CPF\-CGC \(CPF\_CGC\) da tabela definitiva da SAFX04\.

Se o parâmetro ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais NÃO esteja selecionado:

Gerar o campo com a informação do campo CPF\-CGC \(CPF\_CGC\) da tabela definitiva da SAFX04, SE o campo Movimento Entrada/Saída \(MOVTO\_E\_S\) da tabela definitiva da SAFX07 estiver preenchido com o conteúdo igual a “1” e o campo Indicador do Conteúdo do Código \(IND\_CONTEM\_COD\) da tabela definitiva da SAFX04 estiver preenchido com o conteúdo igual a “2”\.

Gerar o campo com a informação do campo CPF/CNPJ do Consumidor/ Produtor \(CPF\_CNPJ\) da tabela definitiva da SAFX07, SE o campo Movimento Entrada/Saída \(MOVTO\_E\_S\) estiver preenchido com o conteúdo igual a “2” e SE o campo CPF/CNPJ do Consumidor/ Produtor \(CPF\_CNPJ\) da tabela definitiva da SAFX07 estiver preenchido, SE NÃO gerar o campo com a informação do campo CPF\-CGC \(CPF\_CGC\) da tabela definitiva da SAFX04\.

__Tratamento:__

- Se for CPF \(preenchimento com 11 posições\) não deve ser considerado zeros à esquerda e nem à direita para completar o tamanho do campo;
- Se houver espaços em branco no campo da tabela SAFX04/SAFX07 deve ser desconsiderado, pois esse campo quando for CPF deve vir apenas com os 11 dígitos\.

vlrBruto

Campo 22 \-Valor da Produto da SAFX07 \(total agrupado por Tipo de aquisição e Produtor\)

Caso o parâmetro ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais esteja selecionado o campo a ser recuperado será:

Campo 20\-Valor do Produto da SAFX63 \(total agrupado por Tipo de aquisição e Produtor\)

Quando se tratar de produtor rural __pessoa física__, será deduzido deste valor o correspondente ao mesmo valor das notas fiscais de devolução\.

O valor resultante das aquisições menos as devoluções não pode ser menor ou igual a zero\.

\(ver regra geral sobre as devoluções na Recuperação dos Dados e Processamento\)\.

vlrCPDescPR

Campo 243 \- Valor Contrib Previd s/ Produção Rural Sub\-rogação da SAFX07 \(total agrupado por Tipo de aquisição e Produtor\)

Caso o parâmetro ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais esteja selecionado o campo a ser recuperado será:

Campo 24\-Valor da Contribuição da SAFX63 \(total agrupado por Tipo de aquisição e Produtor\)

Quando se tratar de produtor rural __pessoa física__, será deduzido deste valor o correspondente ao mesmo valor das notas fiscais de devolução\.

\[__MFS28766\]__

O valor resultante das aquisições menos as devoluções não pode ser menor que zero\. Neste caso, gerar o campo com zero e exibir mensagem no log:

*O Valor da Contribuição Previdenciária referente às Devoluções excede ao das aquisições do produtor rural no período\. Nesse caso será gerado o valor 0 \- zero\.*

*Dados do Registro: Indicativo da Aquisição: XX' \- Inscrição do Produtor: XXXXXXXXXXX*

\(ver regra geral sobre as devoluções na Recuperação dos Dados e Processamento\)\.

vlrRatDescPR

Campo 287 \- Valor da GILRAT da SAFX07 \(total agrupado por Tipo de aquisição e Produtor\)

Caso o parâmetro ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais esteja selecionado o campo a ser recuperado será:

Campo 30\-Valor da GILRAT da SAFX63 \(total agrupado por Tipo de aquisição e Produtor\)

Quando se tratar de produtor rural __pessoa física__, será deduzido deste valor o correspondente ao mesmo valor das notas fiscais de devolução\.

\[__MFS28766\]__

O valor resultante das aquisições menos as devoluções não pode ser menor que zero\. Neste caso, gerar o campo com zero e exibir mensagem no log:

*O Valor da Contribuição Destinada ao RAT referente às Devoluções excede ao das aquisições do produtor rural no período\. Nesse caso será gerado o valor 0 \- zero\.*

*Dados do Registro: Indicativo da Aquisição: XX' \- Inscrição do Produtor: XXXXXXXXXXX*

\(ver regra geral sobre as devoluções na Recuperação dos Dados e Processamento\)\.

vlrSenarDesc

Campo 288 \- Valor da Contribuição Destinada ao SENAR da SAFX07 \(total agrupado por Tipo de aquisição e Produtor\)

Caso o parâmetro ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais esteja selecionado o campo a ser recuperado será:

Campo 26\-Valor do Senar da SAFX63 \(total agrupado por Tipo de aquisição e Produtor\)

Quando se tratar de produtor rural __pessoa física__, será deduzido deste valor o correspondente ao mesmo valor das notas fiscais de devolução\.

\[__MFS28766\]__

O valor resultante das aquisições menos as devoluções não pode ser menor que zero\. Neste caso, gerar o campo com zero e exibir mensagem no log:

*O Valor da Contribuição Destinada ao SENAR referente às Devoluções excede ao das aquisições do produtor rural no período\. Nesse caso será gerado o valor 0 \- zero\.*

*Dados do Registro: Indicativo da Aquisição: XX' \- Inscrição do Produtor: XXXXXXXXXXX*

\(ver regra geral sobre as devoluções na Recuperação dos Dados e Processamento\)\.

indOpcCP

Se o parâmetro ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ esteja selecionado nos Dados Iniciais:

__\[MFS58457\] __Se o campo 33\-IND\_TRIB\_PRODUTOR\_CP da SAFX63, estiver preenchido, considerar a informação indicada neste campo, caso o campo esteja sem informação, verificar as regras abaixo:

Se campo 24\-Valor da Contribuição da SAFX63 estiver sem valor informado \(0\-zero\)

E__ __

__\[MFS25120\]__

Não existir vinculação de processo na SAFX271 que zera o campo por liminar \(processo judicial\) OU 

caso exista, os campos 15 \- Valor da Contribuição Previdenciária Não Retida\(VLR\_CONT\_PREV\_N\_RET\) e 16 \- Valor da contribuição para o GILRAT Não Retido\(VLR\_GILRAT\_N\_RET\) da SAFX271 estiverem sem valor informado \(0\-zero\),

então:

       Gravar ‘2’ \- Sobre a folha de pagamento\. 

Senão:

        Gravar ‘1’ \- Sobre a comercialização da sua produção\.

Se geração normal a partir das notas \(SAFX07\):

Deverá ser verificada a parametrização da Pessoa Fisica/Juridica no Módulo Funrural > Movimento > Pessoa Fis/Jur para o Recolhimento FUNRURAL, caso o Produtor gerado nessa tag \(Pessoa Física/Jurídica\) estiver com o campo Forma de tributação do Produtor Rural ‘Sobre a Folha de Pagamento’ marcado, gravar ‘2’ – Sobre a Folha de Pagamento, caso contrário, gravar ‘1’ \- Sobre a comercialização da sua produção\.

__Atenção: Foi visto no atendimento da MFS\-58457 que a regra acima \(referente a origem SAFX07\), não está implementada no sistema\. Atualmente implementado, para documentos fiscais, consideramos sempre fixo ‘1’, neste campo\. Como o cenário do cliente são os dados de origem SAFX63, não foi revisto neste momento se a regra deve ser mantida e implementada ou se o que está implementado é o correto\. __

MFS25120

MFS\-58457

__Registro nfs__ – Detalhamento das notas fiscais de aquisição de produção do produtor

Este registro é gerado a partir das notas fiscais \(SAFX07 ou SAFX63\) vinculadas aos Produtores\. Caso o parâmetro ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais esteja selecionado as notas fiscais vinculadas aos Produtores serão pela SAFX63\.

Conforme descrito na regra geral sobre as devoluções na Recuperação dos Dados e Processamento, este registro __não__ será gerado quando se tratar de produtor rural = pessoa física\.

Para cada nota fiscal, será gerado um registro __nfs__, com as seguintes informações:

serie

Campo 09\-Série do Documento Fiscal da SAFX07 ou SAFX63

nrDocto

Campo 08\-Número do Documento Fiscal da SAFX07 ou SAFX63

dtEmisNF

Campo 11\-Data de Emissão da SAFX07 ou Campo 03\-Data do Movimento da SAFX63

vrBruto

Campo 22\-Valor dos Produtos da SAFX07 ou Campo 20\-Valor do Produto da SAFX63

vrCPDescPR

Campo 243 \- Valor Contrib Previd s/ Produção Rural Sub\-rogação da SAFX07 ou Campo 24\-Valor da Contribuição da SAFX63

vrRatDescPR

Campo 287 \- Valor da GILRAT da SAFX07 ou Campo 30\-Valor da GILRAT da SAFX63

vrSenarDesc

Campo 288 \- Valor da Contribuição Destinada ao SENAR da SAFX07 ou Campo 26\-Valor do Senar da SAFX63

__Registro __<a id="_Hlk524440900"></a><a id="_Hlk524441786"></a>__infoProcJud__ \- Informações referentes à processo judicial

	

Este registro será gerado apenas quando o Produtor Rural possuir processo judicial do produtor \(campo 21 – Indicador Tipo do Processo Judicial for igual a ‘1 \- Processo Judicial do Produtor’\)\. Para isso será verificado o preenchimento dos campos “*21 – Indicador Tipo do Processo Judicial”,* “*13 \- Número do Processo*” e “*14 \- Código do Indicativo da Suspensão de Exigibilidade de Tributos*” da SAFX263, da seguinte forma: 

Esse registro __infoProcJud__ será gerado apenas se o campo *21 – Indicador Tipo do Processo Judicial* for igual a ‘1 \- Processo Judicial do Produtor’ __E__ os campos “*13 \- Número do Processo*” e “*14 \- Código do Indicativo da Suspensão de Exigibilidade de Tributos*” estiverem preenchidos\.

Caso o parâmetro ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais esteja selecionado, será verificado o preenchimento dos campos “*18 – Indicador Tipo do Processo Judicial*”, “*11 \- Número do Processo*” e “*12 \- Código do Indicativo da Suspensão*” da SAFX271, da seguinte forma: 

Esse registro __infoProcJud__ será gerado quando o campo *18 – Indicador Tipo do Processo Judicial* for igual a ‘1 \- Processo Judicial do Produtor’ __E__ os campos “*11 \- Número do Processo*” e “*12 \- Código do Indicativo da Suspensão*” estiverem preenchidos\.

__OU \[MFS25893\]__

Esse registro __infoProcJ__ será gerado quando o campo *18 – Indicador Tipo do Processo Judicial* for igual a ‘3 \- Indicador de Autoria do Processo’ __E__ os campos “*11 \- Número do Processo*” e “*12 \- Código do Indicativo da Suspensão*” estiverem preenchidos\.  Além de verificar o campo 18 da SAFX271, também deve ser verificado o campo 8 \- Indicador de Autoria da SAFX2058, que deve estar igual a “1 \- Próprio contribuinte”;

O registro __infoProcJud__ será gerado com a seguinte informação: 

nrProcJud

Campo <a id="_Hlk524441341"></a>13\-Número do Processo \(SAFX263\) ou 11\-Número do Processo \(SAFX271\)

codSusp

Campo 14 \- Código do Indicativo da Suspensão de Exigibilidade de Tributos \(SAFX263\) ou 12\-* *Código do Indicativo da Suspensão \(SAFX271\)

vrCPNRet

Campo 15\-Valor da Contribuição Previdenciária Não Retida \(SAFX263\) ou 13\-* *Valor da Contribuição Previdenciária Não Retida \(SAFX271\)

vrRatNRet

Campo 16\-Valor da contribuição para GILRAT Não Retida \(SAFX263\) ou 14\-Valor da Contribuição para GILRAT Não Retido \(SAFX271\)

vrSenarNRet

Campo 17\-Valor da contribuição para o SENAR Não Retido \(SAFX263\) ou 15\-Valor da Contribuição para SENAR Não Retido \(SAFX271\)

__Registro infoProcJ__ \- Informações referentes à processo judicial comum a todos os produtores

	

Este registro será gerado apenas quando o Produtor Rural possuir processo judicial comum a todos os produtores \(campo 21 – Indicador Tipo do Processo Judicial for igual a ‘2 \- Processo Judicial Coletivo’\)\. Para isso será verificado o preenchimento dos campos “*21 – Indicador Tipo do Processo Judicial”,* “*13 \- Número do Processo*” e “*14 \- Código do Indicativo da Suspensão de Exigibilidade de Tributos*” da SAFX263, da seguinte forma: 

Esse registro __infoProcJ__ será gerado apenas se o campo *21 – Indicador Tipo do Processo Judicial* for igual a ‘2 \- Processo Judicial Coletivo’ __E__ os campos “*13 \- Número do Processo*” e “*14 \- Código do Indicativo da Suspensão de Exigibilidade de Tributos*” estiverem preenchidos\.

Caso o parâmetro ‘Gerar evento S\-1250 a partir da SAFX63 \- Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais esteja selecionado, será verificado o preenchimento dos campos “*18 – Indicador Tipo do Processo Judicial*”, “*11 \- Número do Processo*” e “*12 \- Código do Indicativo da Suspensão*” da SAFX271, da seguinte forma: 

Esse registro __infoProcJ__ será gerado quando o campo *18 – Indicador Tipo do Processo Judicial* for igual a ‘2 \- Processo Judicial Coletivo’ __E__ os campos “*11 \- Número do Processo*” e “*12 \- Código do Indicativo da Suspensão*” estiverem preenchidos\.

__OU \[MFS25893\]__

Esse registro __infoProcJ__ será gerado quando o campo *18 – Indicador Tipo do Processo Judicial* for igual a ‘3 \- Indicador de Autoria do Processo’ __E__ os campos “*11 \- Número do Processo*” e “*12 \- Código do Indicativo da Suspensão*” estiverem preenchidos\.  Além de verificar o campo 18 da SAFX271, também deve ser verificado o campo 8 \- Indicador de Autoria da SAFX2058, que deve estar igual a “2 \- Outra entidade, empresa ou empregado”;

O registro __infoProcJ__ será gerado com a seguinte informação: 

nrProcJud

Campo 13\-Número do Processo \(SAFX263\) ou 11\-Número do Processo \(SAFX271\)

codSusp

Campo 14 \- Código do Indicativo da Suspensão de Exigibilidade de Tributos \(SAFX263\) ou 12\-* *Código do Indicativo da Suspensão \(SAFX271\)

vrCPNRet

Campo 15\-Valor da Contribuição Previdenciária Não Retida \(SAFX263\) ou 13\-* *Valor da Contribuição Previdenciária Não Retida \(SAFX271\)

vrRatNRet

Campo 16\-Valor da contribuição para GILRAT Não Retida \(SAFX263\) ou 14\-Valor da Contribuição para GILRAT Não Retido \(SAFX271\)

vrSenarNRet

Campo 17\-Valor da contribuição para o SENAR Não Retido \(SAFX263\) ou 15\-Valor da Contribuição para SENAR Não Retido \(SAFX271\)

= = = = = =

 


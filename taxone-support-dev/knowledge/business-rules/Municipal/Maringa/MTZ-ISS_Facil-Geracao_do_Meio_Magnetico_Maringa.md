# MTZ-ISS_Facil-Geracao_do_Meio_Magnetico_Maringa

- **Fonte:** MTZ-ISS_Facil-Geracao_do_Meio_Magnetico_Maringa.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 53 KB

---

# ISS Facil \- Geração do Meio Magnético

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3553

__DW\-MUNICIPAL\-NOVO PRODUTO \- ISSFACIL MARINGA__

Este documento tem como objetivo criar a geração para os municípios que são atendidos pelo ISS Facil\. Dessa forma usaremos o módulo de Parâmetros por Município que servirá para o usuário realizar a parametrização de todos os municípios atendidos pelo ISS Fácil em um único lugar\. Além disso, também realizaremos a geração dos municípios através de uma única geração, ou seja, quando o cliente clicar em um município da ISS Fácil será exibido a mesma tela de geração do Meio Magnético\. 

Essa OS será baseada na geração do ISS Digital BH\.

OS3926\-O

Geração do Meio Magnético Maringa \- Atendimento a constução civil/telecomunicações/utilities

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para os municípios atendidos pelo validador ISS \- FACIL\.

MFS\_2071

DW \- MUNICIPAL – ISS Facil – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

## REGRAS DE NEGÓCIO

	

#### Cód\.

### Descrição

### DR

__RN01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Maringá” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços prestados e tomados no município de Maringá”\.

OS3553

__RN02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “PR” e ao código de município do IBGE igual a “15200” \(Maringá\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Maringá, Paraná\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

OS3553

__RN03__

__Estrutura de menus do módulo ISS Facil:__

Deverão ser criados os seguintes menus e sub\-menus no módulo ISS Facil:

- Arquivo
- Obrigações
	- Geração Meio Magnético
	- Arquivo de Entradas de Serviços \(Consti\. Civil/Utilities/Telecom\)
- Janela
- Ajuda 

OS3553

OS3926\-Q

__RN04__

__Regra de criação do nome do arquivo__

__ISSFACIL\_MUNICIPIO\_DDMMAAAA\.txt__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o  município que está sendo gerado\.

       __ISSFACIL__: representa a obrigação que está sendo gerada\.

       __\.txt__: extensão do arquivo\.

Ex: ISSFACIL\_MARINGA\_01012010\.txt

__OS3553__

__RN05__

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

Gerar Registro Tipo “E” – Notas Emitidas: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Gerar Registro Tipo “R” – Notas Recebidas: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Estabelecimento: o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__OS3553__

__MFS\_2071__

__RN06__

__Regra p/ geração do arquivo magnético__

Cada registro especificado abaixo corresponde a uma linha de arquivo texto\. 

O registro do tipo “H”\. Este registro deverá ser único no arquivo\.

Todos os registros deverão ser finalizados pelos caracteres especiais de carriage return e line feed \(asc 13 \+ asc 10\)\.

Após o último registro, deve existir o caractere de fim de arquivo \(asc 26\)\.

__OS3553__

__RN07__

__Regra p/ preenchimento dos campos do arquivo magnético__

A forma de preenchimento dos campos no arquivo deve ser realizada da seguinte maneira:

Campos do tipo N \(Numéricos\) Ex\. Inscrição Municipal, CNPJ, Valor da Nota Fiscal deverão ser preenchidos com zeros à esquerda até atingir o tamanho exato do campo\.

Campos do tipo A \(Alfanuméricos\) Ex\. Nome do Tomador/Prestador, Código do SIAFI da Prestação do Serviço, deverão ser preenchidos com espaços à direita\.

Campos do tipo D \(Data\) deverão ser preenchidos no formato dd/mm/aaaa\.

Todos os campos deverão obedecer rigorosamente o tamanho e a formatação definido neste layout\.

__OS3553__

__RN08__

__Regra p/ Registro Tipo H__

Primeiro registro do arquivo, contém a Inscrição Municipal da empresa e a versão do sistema\.

Deve existir apenas um registro tipo “H” por arquivo\.

__OS3553__

__RN09__

__Registro H – Tipo de Registro: __

Preencher com o texto fixo “H”\.

__OS3553__

__RN10__

__Registro H –  Inscrição Municipal: __

Preencher com o campo INSCR\_MUNICIPAL da tabela ESTABELECIMENTO\.

__OS3553__

__RN11__

__Registro H –  Versão do sistema: __

Preencher com 100\.

__OS3553__

__RN12__

__Regra p/ Registro Tipo E__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência

__OS3553__

__RN13__

__Registro E – Tipo do Registro: __

Preencher com o texto fixo “E”\.

__OS3553__

__RN14__

__Registro E – Data de Emissão:__ 

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. \(campo 11 da SAFX07\)\. Formato: 99/99/9999\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\) , preencher como campo DAT\_CANCELAMENTO da DWT\_DOCTO\_FISCAL\. \(campo 94 da SAFX07\)

__OS3553__

__RN15__

__Registro E – Série da nota fiscal: __

Preencher com o campo Série ISS Facil da tela Municipal – Parâmetros por Município – Modelo Msaf x Série referente ao modelo cadastrado na nota\.

__OS3553__

__RN16__

__Registro E – Modelo da nota fiscal: __

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. \(campo 09 da SAFX07\)

__OS3553__

__RN17__

__Registro E – Natureza da Operação : __

Preencher com:

D, quando o campo NORM\_DEV da tabela DWT\_DOCTO\_FISCAL = ‘2’ \(campo 04 da SAFX07\)

G, quando o campo IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota\.

I, quando campo IND\_ISS da tabela ESTABELECIMENTO = ‘08’

C, verificar se o campo IND\_ISS da tabela ESTABELECIMENTO =  “04”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros por Município – Classificação de Serviços – Município com o COD\_PARAM =  “433”\.

F, verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “01” se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros por Município – Classificação de Serviços – Município com o COD\_PARAM = “420” \.

H, verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “02”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros por Município – Classificação de Serviços – Município com o COD\_PARAM = “421”\.

E, Verificar se o campo IND\_ISS da tabela ESTABELECIMENTO = “06”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “432”\.

B, o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV > 0\. 

A, o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV = 0 ou quando não estiver preenchido\. 

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\) , preencher com brancos\.

__OS3553__

__RN18__

__Registro E – Número da nota fiscal: __

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. \(campo 08 da SAFX07\)

__OS3553__

__RN19__

__Registro E – Valor bruto da nota fiscal: __

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\. \(campo  da SAFX09\)

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\) , preencher com zeros\.

__OS3553__

__RN20__

__Registro E – Valor do serviço: __

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. \(campo 14 da SAFX09\)

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\) , preencher com zeros\.

__OS3553__

__RN21__

__Registro E – Tipo de recolhimento do ISS: __

Para que esse campo seja preenchido com “A”, é necessário que pelo menos umas das seguintes opções seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “2”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota utilizando o município cadastrado no estabelecimento\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\. E1\-RN0001 

Caso nenhuma das opões seja verdadeira, preencher com “R”\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\) , preencher com brancos\.

__OS3553__

__OS3470\-I1C__

__RN22__

__Registro E – Alíquota de ISS: __

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 32 da SAFX09\)\. Formato: 99\.99

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com zeros\.

__OS3553__

__RN23__

__Registro E – Inscrição Municipal do tomador de serviços: __

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota Se não houver, preencher com zeros\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\) , preencher com zeros\.

__OS3553__

__RN24__

__Registro E – CNPJ do tomador de serviços: __

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota quando o tamanho do campo for igual a 14\. \(campo 06 da SAFX04\)

Se o campo tiver 11 posições ou o tomador for estrangeiro, preencher com zeros\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\) , preencher com zeros\.

__OS3553__

__RN25__

__Registro E – CPF do tomador de serviços: __

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota quando o tamanho do campo for igual a 11\. \(campo 06 da SAFX04\)

Se o campo tiver 14 posições ou o tomador for estrangeiro, preencher com zeros\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com zeros\.

__OS3553__

__RN26__

__Registro E – Nome do tomador de serviços: __

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota \(campo 05 da SAFX04\)

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com brancos\.

__OS3553__

__RN27__

__Registro E – Tipo de Rua do tomador de serviços: __

Preencher com o campo TP\_LOGRADOURO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com brancos\.

__OS3553__

__RN28__

__Registro E – Nome da Rua do tomador de serviços: __

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com brancos\.

__OS3553__

__RN29__

__Registro E – Número da residência: __

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com zeros\.

__OS3553__

__RN30__

__Registro E – Complemento: __

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com brancos\.

__OS3553__

__RN31__

__Registro E – Tipo de Bairro do tomador de serviços: __

Preencher com o “BAIRRO”

__OS3553__

__RN32__

__Registro E – Nome do Bairro do tomador de serviços: __

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com brancos\.

__OS3553__

__RN33__

__Registro E – Cidade do tomador de serviços: __

Preencher com o campo CIDADE da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com brancos\.

__OS3553__

__RN34__

__Registro E – Estado do tomador de serviços: __

Preencher com o campo COD\_ESTADO da tabela ESTADO correspondente a tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Para tomador de serviços estrangeiros usar “EX” e não informar a Inscrição municipal e o CNPJ\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com brancos\.

__OS3553__

__RN35__

__Registro E – CEP do tomador de serviços: __

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\. 

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com zeros\.

__OS3553__

__RN36__

__Regra p/ Registro Tipo R__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência 
- Nota não cancelada \(situacao <> ‘S’\)

__OS3553__

__RN37__

__Registro R – Identificação do Registro: __

Preencher com o texto fixo “R”\.

__OS3553__

__RN38__

__Registro R – Data de retenção do ISS: __

Preencher com o campo DT\_PAGTO\_NF da tabela DWT\_DOCTO\_FISCAL\. \(campo 175 da SAFX07\), quando pelo menos uma das opções abaixo seja verdadeira:

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”\.
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota utilizando o município cadastrado no estabelecimento\.
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV está preenchido\.

*Obs: Se o campo DT\_PAGTO não estiver preenchido, deve\-se preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\.*

Caso nenhuma das opões seja verdadeira, preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. \(campo 11 da SAFX07\) Formato: 99/99/9999\.

__OS3553__

__OS3470\-I1C__

__ RN39__

__Registro R – Data de emissão da nota fiscal: __

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. \(campo 11 da SAFX07\) Formato: 99/99/9999\.

__OS3553__

__RN40__

__Registro R – Série da nota:__

Preencher com o campo Série ISS Digital da tela Municipal – Parâmetros por Município – Modelo Msaf x Série ISS Digital referente ao modelo cadastrado na nota\.

__OS3553__

__RN41__

__Registro R – Modelo da nota fiscal: __

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. \(campo 09 da SAFX07\)

__OS3553__

__RN42__

__Registro R – Natureza da Operação: __

Preencher com:

D, quando o campo NORM\_DEV da tabela DWT\_DOCTO\_FISCAL = ‘2’ \(campo 04 da SAFX07\)

G, quando o campo IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota\.

I, quando campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = ‘06’

C, verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR =  “10”, se não estiver preenchido verificar se o serviço e o município da pessoa fis/jur cadastrados na nota está parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM =  “433”\.

F, verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “07” se não estiver preenchido verificar se o serviço e o município da pessoa fis/jur cadastrados na nota está parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420”\.

H, verificar se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR = “08”, se não estiver preenchido verificar se o serviço e o município da pessoa fis/jur cadastrados na nota está parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “421”\.

E, Verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizado na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “432”\.

B, quando o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV > 0\.

A, quando o somatório do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV = 0 ou quando não estiver preenchido\. \(campo 190 da SAFX07\)

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\) , preencher com brancos\.

__OS3553__

__RN43__

__Registro R – Numero da Nota Fiscal: __

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\. \(campo 08 da SAFX07\)

__OS3553__

__RN44__

__Registro R – Valor bruto da nota fiscal: __

Preencher com o campo VLR\_TOT da tabela DWT\_ITENS\_SERV\. 

__OS3553__

__RN45__

__Registro R – Valor do serviço: __

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\. \(campo 14 da SAFX09\)

__OS3553__

__RN46__

__Registro R – Alíquota de ISSQN: __

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 32 da SAFX09\)

__OS3553__

__RN47__

__Registro R – Numero da parcela de pagamento da NF: __

Preencher com zeros\.

__OS3553__

__RN48__

__Registro R – Quantidade de parcelas de pagamento da NF: __

Preencher com zeros\.

__OS3553__

__RN49__

__Registro R – Descrição do motivo da não retenção: __

Preencher com brancos\.

__OS3553__

__RN50__

__Registro R – Inscrição municipal do prestador do serviço: __

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR\.

Se o tomador for estrangeiro, preencher com zeros\.

__OS3553__

__RN51__

__Registro R – CNPJ do prestador do serviço: __

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR quando o tamanho do campo for igual a 14\. \(campo 06 da SAFX04\)

Se o campo tiver 11 posições ou o tomador for estrangeiro, preencher com zeros\.

__OS3553__

__RN52__

__Registro R – CPF do prestador do serviço:__ 

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR quando o tamanho do campo for igual a 11\. \(campo 06 da SAFX04\)

Se o campo tiver 14 posições ou o tomador for estrangeiro, preencher com zeros\.

__OS3553__

__RN53__

__Registro R – Nome do prestador do serviço: __

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR\. \(campo 05 da SAFX04\)

__OS3553__

__RN54__

__Registro R – Tipo de Rua do tomador de serviços: __

Preencher com o campo TP\_LOGRADOURO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com brancos\.

__OS3553__

__RN55__

__Registro R – Nome da Rua do tomador de serviços: __

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com brancos\.

__OS3553__

__RN56__

__Registro R – Número da residência: __

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com brancos\.

__OS3553__

__RN57__

__Registro R – Complemento: __

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com brancos\.

__OS3553__

__RN58__

__Registro R – Tipo de Bairro do tomador de serviços: __

Preencher com o “BAIRRO”

__OS3553__

__RN59__

__Registro R – Nome do Bairro do tomador de serviços: __

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com brancos\.

__OS3553__

__RN60__

__Registro R – Cidade do tomador de serviços: __

Preencher com o campo CIDADE da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Se for nota fiscal cancelada \(SITUACAO = ‘S’ – campo 30 da SAFX07\), preencher com brancos\.

__OS3553__

__RN61__

__Registro R – Estado do tomador de serviços: __

Preencher com o campo COD\_ESTADO da tabela ESTADO correspondente a tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Para tomador de serviços estrangeiros usar “EX” e não informar a Inscrição municipal e o CNPJ\.

__OS3553__

__RN62__

__Registro R – CEP do tomador de serviços: __

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__OS3553__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


# MTZ-ISS_WEB-Geracao_do_Meio_Magnético-Nova_Granada

> Fonte: MTZ-ISS_WEB-Geracao_do_Meio_Magnético-Nova_Granada.doc

ISS WEB

Geração do Meio Magnético 


DOCUMENTO DE REQUISITO

DR	Nome	Descrição		OS3733	Migração do município Nova Granada do validador E.ISS para ISS WEB.	Este documento tem como objetivo permitir a migração do município Nova Granada do validador E.ISS para ISS WEB.		MFS1418	DW - MUNICIPAL – ISSWEB NOVA GRANADA – Inclusão de novo parâmetro Gerar Arquivos por Data de Emissão	Este documento tem como objetivo disponibilizar o novo parâmetro “Gerar Arquivos por Data de Emissão” na tela de geração dos registros do validador ISS WEB, possibilitando gerar as informações da obrigação acessória por data de emissão.		
Documentos relacionados:

MTZ – Parametros por Municipio.doc
DE-PARA – Municipal.xls


REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN01	Regra p/ inclusão do módulo no Manager - (partir desta OS o módulo "Nova Granada" irá trabalhar com dois validadores "E.ISS" e "ISS WEB").
 
Nova Granada
O novo módulo “Nova Granada” deve ficar localizado no grupo “Municipal”.
A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços prestados e contratados do município de Nova Granada.”.
	OS3733		RN02	Regra p/ abertura do módulo no Manager - (partir desta OS o módulo "Nova Granada" irá trabalhar com dois validadores "E.ISS" e "ISS WEB").

Nova Granada
Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “” e ao código de município do IBGE <> “” (Nova Granada), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:
 “Este estabelecimento não pertence à NOVA GRANADA/SP. Alguns dados não estarão disponíveis. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente. Caso o usuário clique no botão “Não” o módulo não é aberto. O botão “Não” é default.

	OS3733		RN03	Estrutura de menus do módulo - (partir desta OS o módulo "Nova Granada" irá trabalhar com dois validadores "E.ISS" e "ISS WEB").

Deverão ser criados os seguintes menus e sub-menus no módulo ISSWEB:
Arquivo
Obrigações
Geração do Meio Magnético
Janela
Ajuda
	OS3733		RN04	Regra de criação do nome do arquivo:

Serviços Prestados

SP_ISSWEB_MUNICIPIO_DDMMAAAA.txt, onde:

     SP: representa o tipo de serviço informado no arquivo. Nesse caso serviços prestados.
     SPE: representa a obrigação que está sendo gerada. 
     MUNICIPIO: representa o município que está sendo gerado. Deve ser preenchido com o nome do município selecionado no         manager.
     DDMMAAAA: representa a data inicial da geração
     .txt: extensão do arquivo.

Ex: SP_ISSWEB_NOVAGRANADA_01012010.txt

Serviços Tomados

ST_ISSWEB_MUNICIPIO_DDMMAAAA.txt, onde:

     ST: representa o tipo de serviço informado no arquivo. Nesse caso serviços tomados.
     SPE: representa a obrigação que está sendo gerada. 
     MUNICIPIO: representa o município que está sendo gerado. Deve ser preenchido com o nome do município selecionado no         manager.
     DDMMAAAA: representa a data inicial da geração
     .txt: extensão do arquivo.

Ex: ST_ISSWEB_NOVAGRANADA_01012010.txt

Caso o parâmetro Gerar Arquivos por Data de Emissão estiver marcado, não será possível marcar o parâmetro Quebrar Arquivos por Data de Emissão e deverá ser realizada a seguinte verificação: 

Este arquivo deverá conter todas as notas fiscais com data de emissão dentro do período de referência.

Quando o parâmetro Quebrar Arquivos por Data de Emissão estiver marcado, não será possível marcar o parâmetro Gerar Arquivos por Data de Emissão e deve ser realizada a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal. Esse arquivo deve conter todas as notas fiscais que tenham a mesma competência (mesmo mês referente a data de emissão).

Portanto poderão ser gravados N arquivos de acordo com as competências geradas. A nomenclatura desses arquivos deverão ser:

ST_ISSWEB_MUNICÍPIO_DDMMAAAA_MMAAAA.txt, onde:

     ST_ISSWEB: representa a obrigação que está sendo gerada.
     MUNICÍPIO: representa o município que está sendo gerado.     
     DDMMAAAA: data inicial da geração
     MMAAAA: mês da competência referente à nota gerada
    .txt: extensão do arquivo.

Ex: ST_ISSWEB_NOVAGRANADA_01012010_122009.txt

Obs: Neste caso o arquivo normal também deverá ser gerado, além dos arquivos indicando competências distintas. Estas notas com competência distintas não devem estar no arquivo normal.

OBS.:Este novo parâmetro (Quebrar Arquivos por Data de Emissão) será válido, apenas para Notas de Serviços Tomados	OS3733
MFS1418		RN05	Regra p/ tela da Geração do Meio Magnético

Menu:  Obrigações > Geração do Meio Magnético

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA. O sistema deve exibir o primeiro dia do mês corrente. (SYSDATE). 
Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA. O sistema deve exibir o último dia do mês corrente. (SYSDATE).

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial. Favor preencher uma data final válida.” E deve interromper a geração.

Gerar Serviços Prestados: deve ser exibido através de um checkbox. Deve ser exibido marcado como default. (Opções S = Marcado e N = Desmarcado)
Gerar Serviços Tomados: deve ser exibido através de um checkbox. Deve ser exibido marcado como default. (Opções S = Marcado e N = Desmarcado)
Quebrar arquivo por Data de Emissão: deve ser exibido através de um checkbox. Deve ser exibido desmarcado como default. Quando a opção “Gerar Serviços Tomados” não estiver selecionada, deve ser desabilitado. (Opções S = Marcado e N = Desmarcado)
Gerar Arquivos por Data de Emissão: deve ser exibido através de um checkbox. Deve ser exibido desmarcado como default. (Opções S = Marcado e N = Desmarcado)
Tipo Referência: deve ser exibido através de um listbox. Se o município for “Mogi das Cruzes” ou “Sertãozinho”, deve exibir as opções: N – Normal, C – Complementar e I – Informativo (esse último apenas se o campo Gerar Serviços Prestados estiver marcado). Para os demais municípios deve exibir as opções: N – Normal e C – Complementar.  Para o município de Nova Granada, esse campo não deve ser usado.

Estabelecimento: neste campo o sistema deve exibir os estabelecimentos pertencentes ao município logado, que estejam licenciados e que o usuário possua acesso no PowerLock.
	OS3733
MFS1418		RN06	Regra p/ geração do arquivo magnético

- Os arquivos devem ser gerados no formato texto e devem conter os seguintes registros:

Arquivo de Serviços Prestados
Registro Tipo Header 
Registro Tipo Detalhe
Registro Tipo Trailler

Arquivo de Serviços Tomados
Registro Tipo Header 
Registro Tipo Detalhe
Registro Tipo Trailler
	OS3733		RN07	Regra p/ preenchimento dos campos do arquivo magnético

Campos numéricos
- devem ser preenchidos alinhados a direita e sem formatação (sem ponto e sem vírgula).
- quando o campo não for totalmente preenchido, preencher com zeros à esquerda até completar seu tamanho máximo.
- quando o campo não tiver informação, preencher com zeros até completar seu tamanho máximo.

Campos alfanuméricos
- devem ser preenchidos alinhados a esquerda.
- quando o campo não for totalmente preenchido, preencher com espaços em branco à direita até completar seu tamanho máximo.
- quando o campo não tiver informação, preencher com espaços em branco até completar o seu tamanho máximo.

Campos financeiro
- devem ser preenchidos alinhados a direita, com zeros à esquerda até atingir o tamanho exato do campo com duas casas decimais
- quando o campo não tiver informação, preencher com zeros até completar seu tamanho máximo.

Para Notas Fiscais canceladas (DETALHE – campo SituacaoNF = ‘2’):
- campos com o tipo Numerico ou Financeiro devem ser preenchido com zero(0);
- campos com tipo Char devem ser preencidos com espaços (" ");
- com exceção dos campos: "Nf", “SituacaoNF”, “TipodeRegistro” e "DtEmissao" que devem ser sempre informados.
	OS3733		RN08	Regra p/ recuperar notas fiscais de serviços prestados

Esse arquivo deve ser gerado apenas quando o campo “Gerar serviços prestados” estiver marcado e deve conter todas as notas com as seguintes características:

Nota de Saída (movto_e_s = ‘9’)
Classificação do Documento fiscal = 2 ou 3
Empresa e estabelecimentos escolhidos na tela de geração
Data fiscal dentro do período de referência exceto quando o parâmetro “Gerar Arquivos por Data de Emissão” na tela de geração estiver marcado, caso o parâmetro estiver marcado deverá ser considerado a Data de Emissão dentro do período de referência

Quando a nota não tiver itens não deve ser recuperada.
	OS3733
MFS1418		RN09	Regra p/ recuperar notas fiscais de serviços tomados

Esse arquivo deve ser gerado apenas quando o campo “Gerar serviços tomados” estiver marcado e deve conter todas as notas com as seguintes características:

Nota de Saída (movto_e_s <> ‘9’)
Classificação do Documento fiscal = 2 ou 3
Empresa e estabelecimentos escolhidos na tela de geração
Data fiscal dentro do período de referência exceto quando o parâmetro “Gerar Arquivos por Data de Emissão” na tela de geração estiver marcado, caso o parâmetro estiver marcado deverá ser considerado a Data de Emissão dentro do período de referência
Notas não canceladas (situação <> ‘S’)

Devem ser consideradas também notas eletrônicas, quando emitidas fora do município:

Notas com Modelo = 55 apenas quando o município da pessoa fis/jur (COD_MUNICIPIO da SAFX04) <> município do estabelecimento (COD_MUNICIPIO da tabela ESTABELECIMENTO). Quando o município da pessoa fis/jur (COD_MUNICIPIO da SAFX04) for igual ao município do estabelecimento (COD_MUNICIPIO da tabela ESTABELECIMENTO) essa nota não deve ser considerada no arquivo.
Notas cujo campo IND_NF_ELETRONICA da SAFX2005 = ‘S’ referente ao tipo de documento da nota, apenas quando o município da pessoa fis/jur (COD_MUNICIPIO da SAFX04) <> município do estabelecimento (COD_MUNICIPIO da tabela ESTABELECIMENTO). Quando o município da pessoa fis/jur (COD_MUNICIPIO da SAFX04) for igual ao município do estabelecimento (COD_MUNICIPIO da tabela ESTABELECIMENTO) essa nota não deve ser considerada no arquivo.

Quando a nota não tiver itens não deve ser recuperada.	OS3733
MFS1418		RN10	Registro Tipo A - Tipo de Registro
Preencher com o valor “A”.
Tipo Alfanumérico
Campo obrigatório
Obs.: No layout consta como campo tipo numérico. Não considerar essa informação.	OS3733		RN11	Registro Tipo A – Tipo de Declaração
Preencher com:
T, quando o campo MOVTO_E_S da tabela DWT_DOCTO_FISCAL <> ‘9’
P, quando o campo MOVTO_E_S da tabela DWT_DOCTO_FISCAL = ‘9’
Tipo Alfanumérico
Campo obrigatório	OS3733		RN12	Registro Tipo A – TPIdentificação
Preencher com “1”.
Tipo Numérico
Campo obrigatório	OS3733		RN13	Registro Tipo A – CNPJCPF
Preencher com o campo CGC da tabela ESTABELECIMENTO.
Tipo Numérico
Campo obrigatório	OS3733		RN14	Registro Tipo A – Mês Referencia
Preencher com o mês informado no campo Data Inicial da tela de Geração do Meio Magnético.
Formato: mm
Tipo Numérico
Campo obrigatório	OS3733		RN15	Registro Tipo A – Ano Referencia 
Preencher com o ano informado no campo Data Inicial da tela de Geração do Meio Magnético.
Formato: aaaa
Tipo Numérico
Campo obrigatório	OS3733		RN16	Registro Tipo A – Data Lançamento
Preencher com a data da geração do Meio Magnético
Tipo Numérico
Formato: ddmmaaaa
Campo obrigatório	OS3733		RN17	Registro Tipo A – Filler
Preencher com brancos.
Tipo Alfanumérico
Campo obrigatório	OS3733		RN18	Registro Tipo B – Tipo de Registro 
Preencher com o valor “B”.
Tipo Alfanumérico
Campo obrigatório
Obs.: No layout consta como campo tipo numérico. Não considerar essa informação.	OS3733		RN19	Registro Tipo B – Tpdentificação
Preencher com:
1, quando o campo CGC_CPF da tabela X04_PESSOA_FIS_JUR referente a pessoa fis/jur cadastrada na nota fiscal tiver 14 posições.
2, quando o campo CGC_CPF da tabela X04_PESSOA_FIS_JUR referente a pessoa fis/jur cadastrada na nota fiscal tiver 11 posições.
Tipo Numérico
Campo obrigatório.
	OS3733		RN20	Registro Tipo B – CNPJCPF
Preencher com campo CPF_CGC da X04_PESSOA_FIS_JUR.
Tipo Numérico
Campo obrigatório
	OS3733		RN21	Registro Tipo B – Numero NF
Preencher com o campo NUM_DOCFIS da DWT_DOCTO_FISCAL.
Tipo Numérico
Campo obrigatório
	OS3733		RN22	Registro Tipo B – Data Emissão
Preencher com o campo DATA_EMISSAO da DWT_DOCTO_FISCAL.
Tipo Numérico
Formato: ddmmaaaa
Campo obrigatório
	OS3733		RN23	Registro Tipo B – Valor Serviço Prestado
Preencher com o campo VLR_TOT da DWT_ITENS_SERV.
Tipo Numérico
Campo obrigatório	OS3733		RN24	Registro Tipo B – Valor das Deduções
Preencher com VLR_DEDUCOES_ISS da DWT_ITENS_SERV.
Tipo Numérico
Campo obrigatório
	OS3733		RN25	Registro Tipo B – Série da Nota Fiscal
Preencher com o campo SERIE_DOCFIS da DWT_DOCTO_FISCAL. 
Tipo Alfanumérico
Campo obrigatório
	OS3733		RN26	Registro Tipo B – Valor do Imposto
Preencher com o campo VLR_TRIBUTO_ISS da DWT_ITENS_SERV.
Tipo Numérico
Campo obrigatório
	OS3733		RN27	Registro Tipo B – Imposto Retido

Notas Emitidas

Isento
Verificar se o campo IND_ISS da tabela ESTABELECIMENTO = “04”, se não estiver preenchido verificar se o serviço cadastrado na nota está parametrizado na tela Parâmetros por Municípios – Classificação de Serviços com o COD_PARAM = “433”, preencher com ‘I’;

Imposto Retido
Verificar o local da prestação do serviço (campo COD_MUNIC da tabela DWT_DOCTO_FISCAL). Se o mesmo não estiver preenchido,
recuperar o município do estabelecimento (campo cod_municipio da tabela ESTABELECIMENTO).

Recuperado o local da prestação, preencher com ‘S’, quando pelo menos uma das opções abaixo for verdadeira:

- Se o campo IND_TP_RET da tabela DWT_DOCTO_FISCAL (campo 141 da SAFX07) estiver preenchido com “2" e se
o local da prestação do serviço = município do módulo selecionado OU 
- Se na tabela X2098_ALIQ_SERVICO, o campo IND_SUBSTITUIDO_ISS = “N” para o serviço cadastrado na nota e utilizando o campo 
COD_MUNIC_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU
- Se o campo VLR_ISS_RETIDO da tabela DWT_ITENS_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado .

Imposto não Retido
Se nenhuma das opções for verdadeira, preencher com ‘N’.

Notas Recebidas

Isento
Verificar se o campo IND_ IND_CLASSE_PFJ da tabela X04_PESSOA_FIS_JUR  = “10”, se não estiver preenchido verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD_PARAM = “433”, preencher com ‘I’;


Imposto Retido
Verificar o local da prestação do serviço (campo COD_MUNIC da tabela DWT_DOCTO_FISCAL). Se o mesmo não estiver preenchido, recuperar o município do estabelecimento (campo COD_MUNICIPIO da tabela ESTABELECIMENTO).

Recuperado o local da prestação, preencher com ‘S’, quando pelo menos uma das opções abaixo for verdadeira:

- Se o campo IND_TP_RET da tabela DWT_DOCTO_FISCAL (campo 141 da SAFX07) estiver preenchido com “1" e se
o local da prestação do serviço = município do módulo selecionado OU 
- Se na tabela X2098_ALIQ_SERVICO, o campo IND_TOM_TRIBUT_ISS = “S” para o serviço cadastrado na nota e utilizando o campo 
COD_MUNIC_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU
- Se o campo VLR_ISS_RETIDO da tabela DWT_ITENS_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado.

Imposto não Retido
Se nenhuma das opções for verdadeira, preencher com ‘N’.

Tipo Alfanumérico
Campo obrigatório

Obs.: Regra ajustada no documento DE-PARA – Municipal.xls	OS3733		RN28	Registro Tipo B – Situação Nota Fiscal
Preencher com:
Extraviada
3, quando o campo IND_NOTA_SERVICO da tabela DWT_DOCTO_FISCAL = ‘E’
Cancelada
2, quando o campo SITUACAO da tabela DWT_DOCTO_FISCAL = ‘S’
Normal
1, quando o campo SITUACAO da tabela DWT_DOCTO_FISCAL <> ‘S’
Campo obrigatório

Situação 4 (Sem Movimento) não será tratada.
	OS3733		RN29	Registro Tipo B – Código da Atividade

Preencher com o campo “Serviço” da tela de Parâmetros > Serviços Msaf x Serviço, que esteja relacionado com o código do serviço informado no item do documento fiscal (campo 12- COD_SERVICO da SAFX09).

Se não existir parametrização para a o código de serviço informado na nota, log do sistema deve exibir a seguinte mensagem:  “Para o código de serviço “XXX”, não foi localizada a parametrização de Serviço Msaf x Serviço.”.

Tipo Numérico
Campo obrigatório
	OS3733		RN30	Registro Tipo B – Subcontrole
Preencher com o valor fixo ‘L02’.
Campo obrigatório
	OS3733		RN31	Registro Tipo B – Alíquota 
Preencher com o campo ALIQ_TRIBUTO_ISS da DWT_ITENS_SERV.
Formato: “9999”. Ex.: 4,5% deve ser informado como 0450 (2 inteiros e 2 casas decimais).
Se a alíquota informada for > 99,99 sistema deve exibir no log a seguinte mensagem: “Alíquota da nota superou o tamanho máximo permitido (dois inteiro e dois decimal).  Nota Fiscal: XXXXXXXXX - Alíquota: 99,99.”.
Tipo Numérico
Campo obrigatório
	OS3733		RN32	Registro Tipo B – Código Desdobro
Preencher com zeros.
Tipo Numérico
Obs.: Campo não é obrigatório. Informação confirmada com a Prefeitura de Nova Granada.	OS3733		RN33	Registro Tipo B – FILLER
Preencher com brancos.
Tipo Alfanumérico
Campo obrigatório	OS3733		RN35	Registro Tipo C – Tipo de Registro
Preencher com ‘C’.
Tipo Alfanumérico.
Campo obrigatório
Obs.: No layout consta como campo tipo numérico. Não considerar essa informação.	OS3733		RN36	Registro Tipo C – Qtde Registros
Preencher com o total de registros do tipo ‘1’ gerados no arquivo.
Tipo Numérico
Campo obrigatório	OS3733		RN37	Registro Tipo C – Total dos Serviços
Preencher com o somatório do campo “Valor Serviço Prestado” dos registros gerados no arquivo.
Tipo Numérico com duas casas decimais.
Campo obrigatório.	OS3733		RN38	Registro Tipo C – Total das Deduções
Preencher com o somatório do campo “Valor das Deduções” dos registros gerados no arquivo.
Tipo Numérico com duas casas decimais.
Campo obrigatório.	OS3733		RN39	Registro Tipo C – Total dos Impostos
Preencher com o somatório do campo “Valor do Imposto” dos registros gerados no arquivo.
Tipo Numérico com duas casas decimais.
Campo obrigatório.	OS3733		RN40	Registro Tipo C – FILLER
Preencher com brancos.
Tipo Alfanumérico
Campo obrigatório	OS3733
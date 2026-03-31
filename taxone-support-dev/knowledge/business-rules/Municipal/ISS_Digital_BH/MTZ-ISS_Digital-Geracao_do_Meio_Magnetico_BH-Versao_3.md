# MTZ-ISS_Digital-Geracao_do_Meio_Magnetico_BH-Versao_3

- **Fonte:** MTZ-ISS_Digital-Geracao_do_Meio_Magnetico_BH-Versao_3.docx
- **Modificado:** 2025-07-21
- **Tamanho:** 75 KB

---

# ISS DIGITAL \- Geração do Meio Magnético \- BH

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3763

Geração do Meio Magnético ISS DIGITAL \- BH

Este documento tem como objetivo adequar a geração do meio magnético para a versão 3\.00

CH30291

DW \- MUNICIPAL \- DES BH \- Alteração de regra de geração da versão da DES BH

Esse chamado tem por objetivo corrigir o campo Versão do Sistema do Registro H\.

CH1250\-A

DW \- MUNICIPAL \- DES BH \- Erro na geração do campo Série de documentos recebidos\.

Esse chamado tem por objetivo permitir que o campo série do registro R, seja preenchido com a opção 0 – Não se Aplica quando a série cadastrada na nota fiscal seja preenchido com branco\.

CH10227\_2013

DW\-MUNICIPAL\-BELO HORIZONTE\- O Mastersaf DW não está gravando corretamente a Série da nota fiscal

Esse chamado tem por objetivo permitir que o usuário parametrize o Modelo Msaf x Série para o preenchimento do campo Série do Documento do Registro R\.

CH10396\-A\_2013

DW \- Municipal \- Belo Horizonte \- Campo 12 Valor bruto da nf não está considerando o valor total das notas fiscais conjugadas

Esse chamado tem como objetivo ajustar a regra de geração do campo Valor Bruto do registro de serviços Recebidos\.

__OS3926\-P__

Geração do Meio Magnético ISS DIGITAL BH \- Atendimento a constução civil/telecomunicações/utilities

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para os municípios atendidos pelo validador ISS DIGITAL BH\.

OS4054

DW\-MUNICIPAL\-DESBH\- Alteração na parametrização do tipo Série Msaf x Série do Registro R Campo Série

Este requisito tem como objetivo ajustar a regra de geração do campo Série do registro de Serviços Recebidos\. 

OS4080

OS4332

<a id="OLE_LINK12"></a><a id="OLE_LINK13"></a><a id="OLE_LINK14"></a>DW\-MUNICIPAL\-DESBH\- Novo Parâmetro \- Quebra do Arquivo por Data de Emissão

Implementar novo parâmetro na tela de Geração do Arquivo, para que seja possível realizar a quebra do arquivo por data de emissão\.

CH12081\_2014

DW – MUNICIPAL – DESBH – Tratamento Registro R – Valor do Serviço para NF de CC

<a id="OLE_LINK15"></a><a id="OLE_LINK16"></a><a id="OLE_LINK17"></a>Este documento tem como objetivo alterar a regra do campo Valor do Serviço do Registro R para aceitar tratamento para NF de Construção Civil\.

CH13359\_2014

DW – MUNICIPAL – DESBH – Alteração na recuperação de município para Classificação de Serviços\.

Este documento tem como objetivo alterar a regra de recuperação do município para Classificação de Serviços\.

__OS3341\-A2__

Geração do Meio Magnético para nota fiscais com número de documento com mais de 12 posições\.  

Ajuste para considerar o novo campo NUM\_DOCFIS\_SERV

CH19837\-A\_2014

DW – MUNICIPAL – DESBH – Alteração na recuperação de município para Classificação de Serviços\.

Este documento tem como objetivo alterar a regra de recuperação do município para Classificação de Serviços considerando também o Código Município IBGE \(MasterSAF\)\.

CH8546/2015

Alteração no campo Data de pagamento ou reconhecimento do crédito do Registro R\.

Alteração na regra do campo Data de pagamento ou reconhecimento do crédito do Registro R, para verificar qual situação ocorreu primeiro na nota\.

CH7516\_2016

Alteração do preenchimento do campo <a id="OLE_LINK22"></a><a id="OLE_LINK23"></a><a id="OLE_LINK24"></a>Tipo de Recolhimento do ISSQN do Registro Tipo R

<a id="OLE_LINK25"></a><a id="OLE_LINK26"></a><a id="OLE_LINK27"></a><a id="OLE_LINK28"></a><a id="OLE_LINK29"></a>Este documento tem como objetivo alterar o preenchimento do campo “Tipo de Recolhimento do ISSQN” do Registro Tipo R\.

MFS\_2071

DW \- MUNICIPAL – ISS Digital Meio Magnético \- BH – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

MFS6978

DW \- MUNICIPAL – ISS Digital Meio Magnético \- BH – Atualização da Regra Simples Nacional\.

Esta alteração tem como objetivo, atualizar a regra referente ao campo Simples Nacional de serviços Prestados e Tomados, onde o sistema deve verificar a nova opção “05 – MEI Micro Empresa Individual” da tablea safx04\.

MFS7644

DW \- MUNICIPAL – ISS Digital Meio Magnético \- BH – Atualização da Regra Data de Pagamento\.

Esta alteração tem como objetivo, atualizar a regra referente ao Registro R – Data de pagamento ou reconhecimento do crédito, onde o sistema também deverá tratar por campo de Data Fiscal e não por data de emissão\.

CH21781\_2016

DW \- MUNICIPAL – ISS Digital Meio Magnético \- BH – Alteração no preenchimento do campo Pais dos Registros E, D e R

Este documento tem como objetivo alterar o preenchimento do campo “País do tomador” do Registro E, do campo “País do emissor do documento de Dedução/Repasse” do Registro D e do campo “País do prestador” do Registro R, em casos de pessoa física/ jurídica estabelecida no exterior\.

MFS\-15266

DW \- MUNICIPAL – ISS Digital Meio Magnético \- BH – Inclusão de Parâmetro na tela de geração\.

Essa alteração tem como objetivo incluir o parâmetro “Gerar Arquivos Centralizados” na tela de geração do meio magnético\.

MFS\-28749

DW – MUNICIPAL \- ISS Digital Meio Magnético – BH – Inclusão de parâmetro na tela de geração\.

Essa demanda tem como objetivo incluir o parâmetro que permita ao usuário informar se deve ser considerado no Número do Documento, o ano de emissão das NFS\-e\.

MFS\-30450

DW \- MUNICIPAL \- BELO HORIZONTE \- Erro campo 13 Valor do serviço do Registro Tipo "R" \- SERVIÇOS TOMADOS

Essa demamanda tem como objeto ajustar a geração do campo 13 – Valor do Serviço, para que seja preenchido com o valor da Base ISS, quando esta for Base de Redução\.

MFS44517

DW – MUNICIPAL \- ISS Digital Meio Magnético – BH – Campo série

Essa demanda tem como objetivo alterar a regra de preenchimento do campo série do registro R\.

MFS46538

DW – MUNICIPAL \- ISS Digital Meio Magnético – BH – Versão

Essa demanda tem como objetivo alterar a versão do arquivo gerado, conforme informação passada pelo cliente\. 

MFS\-65383

DW – MUNICIPAL \- ISS Digital Meio Magnético – BH – Campo série

Inserido mais detalhes na regra, para facilitar a interpretação e compreensão da mesma\. \(RN94\)

MFS85255

DW – MUNICIPAL \- ISS Digital Meio Magnético – BH – Campo Alíquota\.

Este documento tem como objetivo alterar a geração do campo de Alíquota \(RN103\) para considerar o Campo de Alíquota ISS Retido, caso o ISS for retido pelo Tomador\.

MFS528514

DW – MUNICIPAL \- ISS Digital Meio Magnético – BH – Motivo de Não Retenção\.

Este documento tem como objetivo alterar a geração do campo de Motivo de Não Retenção \(RN97\) para considerar primeiro o parâmetro por Pessoa Física/Jurídica e somente depois verificar o parâmetro por Serviço\.

MFS627760

Rogério Ohashi

Este documento tem como objetivo alterar a regra de geração do campo de Alíquota \(RN103\) para não preencher a alíquota quando o ISS Retido for fora do município\.

MFS\-848124

Rosemeire Santos

Este documento tem como objetivo atualizar a TFIX83, para as __RN15 e RN93__

## 			REGRAS DE NEGÓCIO

Obs: Por já existir na GISS Online o módulo: Parâmetros POR município e existir a intenção de juntar futuramente os municípios da GISS com os demais municípios do Municipal, criou\-se no municipal o módulo Parâmetros PARA município \(a princípio seria Parametros POR município também, mas por inviabilidade técnica o pronome teve que ser trocado\)\. Porém nas documentações o módulo Parametros PARA município está sendo documentado como Parametros POR município para não haver o retrabalho futuro de trocar todas o nome do módulo em todas as documentações de PARA para POR\. 

#### Cód\.

### Descrição

### DR

__RN01__

__Estrutura de menus do módulo ISS DIGITAL:__

Deverão ser criados os seguintes menus e sub\-menus no módulo ISS DIGITAL:

- Arquivo
- Manutenção
	- Deduções
- Obrigações
	- Geração Meio Magnético
	- Arquivo de Entradas de Serviços \(Consti\. Civil/Utilities/Telecom\)
- Janela
- Ajuda  

OS3763 / OS3926\-P

__RN02__

__Regra de criação do nome do arquivo__

Quando o parâmetro Quebrar Arquivos por Data de Emissão estiver desmarcado será gerado apenas um arquivo com a nomenclatura do arquivo normal indicado abaixo\.

__ISSDIGITAL\_MUNICIPIO\_DDMMAAAA\.txt__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o  município que está sendo gerado\.

       __ISSDIGITAL__: representa a obrigação que está sendo gerada\.

       __\.txt__: extensão do arquivo\.

Ex: ISSDIGITAL\_BELOHORIZONTE\_01012010\.txt

Quando o parâmetro Quebrar Arquivos por Data de Emissão estiver marcado, deve ser realizado a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente a data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverão ser:

__ISSDIGITAL\_ MUNICIPIO \_DDMMAAAA\_MMAAAA\.txt__, onde:

- __ISSDIGITAL__: representa a obrigação que está sendo gerada\. 
- __MUNICIPIO__: representa o  município que está sendo gerado\. 
- __DDMMAAAA__: representa a data inicial da geração\.
- __MMAAAA: __mês da competência referente à nota gerada\.
- __\.txt__: extensão do arquivo\.

Ex: ISSDIGITAL\_BELOHORIZONTE \_01012010\_122009\.txt

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__OBS\.: Devido o validador gerar apenas um arquivo, este novo parâmetro \(Quebrar Arquivos por Data de Emissão\) será válido para todos os tipos de Notas\.__

__OS3763__

__OS4332__

__RN03__

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Gerar Registro Documentos Emitidos: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Gerar Registro Dedução de Materiais, Serviços ou Repasses: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Gerar Registro Documentos Recebidos: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Considerar Ano de Emissão, no campo Número do Documento, para as NFS\-e Recebidas: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Quebrar arquivo por Data de Emissão: deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Gerar Arquivos Centralizados: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = desmarcado\), virá desmarcado ao acessar a tela\. Esse parâmetro quando marcado, retornará os Estabelecimentos Centralizados parametrizados para o Estabelecimento Centralizador em \(<a id="_Hlk507054721"></a>Municipal > Parâmetros para Município<a id="_Hlk507054707"></a>> Parâmetros > Estabelecimentos Centralizadores\)\.

Estabelecimento: o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__OS3763__

__OS4332__

__MFS\_2071__

__MFS15266__

__MFS28749__

__RN04__

__Regra p/ geração do arquivo magnético__

A partir da versão 3\.0 da DES o layout do arquivo de importação não possui mais tamanho fixo para os campos\. 

O caractere pipe "|" será usado como separador de campos\. 

Os campos não preenchidos deverão ficar vazios, sem a necessidade de completar com zeros ou espaços em branco entre os pipes\. 

Os campos que não ocuparem o tamanho máximo determinado também não precisam ser completados com zeros ou espaços em branco\. 

Os campos de data devem estar no Formato: DDMMAAAA\.

A informação das NFS\-e devem sempre utilizar o padrão: 4 dígitos do ano \+ número da NFS\-e\.

O campo subitem deve conter o ponto\. 

Os campos que contenham valor devem ser preenchidos com 2 casas decimais separadas por”\."; 

Os campos que contenham alíquota devem ser informados com 2 casas decimais separadas por”\."; 

Nas informações de endereço é obrigatória a informação do número do imóvel e/ou do complemento; 

Exemplo de preenchimento para o Registro "H": H|100001234X||300\. 

__OS3763__

__RN05__

__Regra p/ Registro Tipo H__

Recuperar as informações da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na tela de geração\.

Deve existir apenas um registro tipo “H” por arquivo\.

__OS3763__

__RN06__

__Registro H – Tipo do Registro: __

Preencher com o texto fixo “H”\.

__OS3763__

__RN07__

__Registro H –  Inscrição Municipal: __

Preencher com o campo INSCR\_MUNICIPAL da tabela ESTABELECIMENTO\.

__OS3763__

__RN08__

__Registro H –  CNPJ/CPF: __

Preencher com o campo CGC da tabela ESTABELECIMENTO\.

OS3763

__RN09__

__Registro H –  Versão do sistema: __

Preencher com “VERSÃO300”\.

__\[MFS46538\]__

Preencher com “VERSÃO301”\.

__OS3763__

__CH30291__

__MFS46538__

__RN10__

__Regra p/ Registro Tipo E__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência

__OS3763__

__RN11__

__Registro E – Tipo do Registro: __

Preencher com o texto fixo “E”\.

__OS3763__

__RN12__

__Registro E – Data de Emissão:__ 

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. 

__OS3763__

__RN13__

__Registro E – Código de Tributação no Município: __

Preencher com o campo Código CTISS da tela Parâmetros por Município – Parâmetros – Atividade Econômica x Código CTISS referente a atividade CNAE do serviço cadastrado na nota fiscal\.

Caso a parametrização de Atividade Econômica x Código CTISS não tenha sido realizada para o código de serviço da nota, a geração deve gerar esse campo em branco e exibir mensagem no log informando que a parametrização deve ser realizada\.

Se a Atividade Econômica não estiver preenchida na tela MasterSAF DW – Manutenção – Códigos – Serviços para o serviço cadastrado na nota fiscal, a geração deve exibir uma mensagem informando que a atividade econômica deve ser preenchida\.

__OS3763__

__RN14__

__Registro E – Código Subitem da Lista de Serviço: __

Preencher com o campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na nota fiscal\. Formato: nn\.nn

Caso o código do serviço da lei 116 não tenha sido cadastrado para o código de serviço da nota, a geração deve gerar esse campo em branco e exibir mensagem no log informando que o cadastro do código da lei 116 deve ser realizado\.

__OS3763__

__RN15__

__Registro E – Modelo do Documento: __

Preencher com o campo Modelo da tela Parâmetros por Município – Parâmetros – Modelo Msaf x Modelo referente ao modelo cadastrado na nota fiscal\.

Caso a parametrização de Modelo Msaf x Modelo não tenha sido realizada para o modelo da nota, a geração deve gerar esse campo em branco e exibir mensagem no log informando que a parametrização deve ser realizada\.

Se o modelo não estiver preenchido na nota fiscal, a geração deve exibir uma mensagem informando que o modelo deve ser preenchido na nota fiscal\.

__OS3763__

__MFS\-848124__

__RN16__

__Registro E – Série do Documento: __

Preencher com o campo Série da tela Parâmetros por Município – Parâmetros – Série Msaf x Série referente a série cadastrada na nota fiscal\.

Caso a parametrização de Série Msaf x Série não tenha sido realizada para a série da nota, a geração deve gerar esse campo em branco e exibir mensagem no log informando que a parametrização deve ser realizada\.

Se a série não estiver preenchido na nota fiscal, a geração deve exibir uma mensagem informando que a série deve ser preenchida na nota fiscal\.

__OS3763__

__RN17__

__Registro E – Subsérie do Documento: __

Preencher com o campo SUB\_SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__OS3763__

__RN18__

__Registro E – Tipo de Negócio: __

Se o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = “S”, preencher com 0\.

Senão:

Preencher com o conteúdo parametrizado no campo Parâmetro da tela Parâmetros por Município – Parâmetros – Classificação de Serviços – DES\-BH – Município quando o campo Tabela dessa mesma tela estiver preenchido com “Tipo de Negócio” para o serviço cadastrado na nota fiscal e para o município do estabelecimento\.

Caso o serviço não esteja parametrizado na tela Parâmetros por Município – Parâmetros – Classificação de Serviços – DES\-BH – Município, preencher com o conteúdo parametrizado no campo Parâmetro da tela Parâmetros por Município – Parâmetros – Classificação de Serviços – DES\-BH – Pessoa Fis/Jur quando o campo Tabela dessa mesma tela estiver preenchido com “Tipo de Negócio” para o serviço cadastrado na nota fiscal, para o município do estabelecimento e para a pessoa fis/jur cadastrada na nota fiscal\.

Caso nenhuma das duas parametrizações tenham sido realizadas, a geração deve gerar esse campo em branco e exibir mensagem no log informando que a parametrização deve ser realizada\.

__OS3763__

__RN19__

__Registro E – Exigibilidade do ISSQN: __

Se o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = “S”, preencher com 0\.

Senão:

Preencher com o conteúdo parametrizado no campo Parâmetro da tela Parâmetros por Município – Parâmetros – Classificação de Serviços – DES\-BH – Município quando o campo Tabela dessa mesma tela estiver preenchido com “Exigibilidade do ISSQN” para o serviço cadastrado na nota fiscal e para o município do estabelecimento\.

Caso o serviço não esteja parametrizado na tela Parâmetros por Município – Parâmetros – Classificação de Serviços – DES\-BH – Município, preencher com o conteúdo parametrizado no campo Parâmetro da tela Parâmetros por Município – Parâmetros – Classificação de Serviços – DES\-BH – Pessoa Fis/Jur quando o campo Tabela dessa mesma tela estiver preenchido com “Exigibilidade do ISSQN” para o serviço cadastrado na nota fiscal, para o município do estabelecimento e para a pessoa fis/jur cadastrada na nota fiscal\.

Caso nenhuma das duas parametrizações tenham sido realizadas, a geração deve gerar esse campo em branco e exibir mensagem no log informando que a parametrização deve ser realizada\.

__OS3763__

__RN20__

__Registro E – Local da Incidência: __

Se COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido, preencher com o campo COD\_UF \+ COD\_MUNICIPIO da tabela MUNICIPIO referente ao  campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\.

Senão preencher com o campo COD\_UF \+ COD\_MUNICIPIO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

*Obs: O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS\.*

__OS3763__

__RN21__

__Registro E – Regime Especial de Tributação: __

Se o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = “S”, preencher com 0\.

Senão:

Preencher com o conteúdo parametrizado no campo Parâmetro da tela Parâmetros por Município – Parâmetros – Classificação de Serviços – DES\-BH – Município quando o campo Tabela dessa mesma tela estiver preenchido com “Regime Especial de Tributação” para o serviço cadastrado na nota fiscal e para o município do estabelecimento\.

Caso o serviço não esteja parametrizado na tela Parâmetros por Município – Parâmetros – Classificação de Serviços – DES\-BH – Município, preencher com o conteúdo parametrizado no campo Parâmetro da tela Parâmetros por Município – Parâmetros – Classificação de Serviços – DES\-BH – Pessoa Fis/Jur quando o campo Tabela dessa mesma tela estiver preenchido com “Regime Especial de Tributação” para o serviço cadastrado na nota fiscal, para o município do estabelecimento e para a pessoa fis/jur cadastrada na nota fiscal\.

Caso nenhuma das duas parametrizações tenham sido realizadas, a geração deve gerar esse campo em branco e exibir mensagem no log informando que a parametrização deve ser realizada\.

__OS3763__

__RN22__

__Registro E – Tipo de Recolhimento do ISSQN: __

Para que esse campo seja preenchido com “2”, é necessário que pelo menos umas das opções da regra \[E1\-RN0001\] seja verdadeira\. Verificar o documento DE\-PARA \- Municipal\.xls abas: Detalhamento e ISS DIGITAL BH\.

Caso nenhuma das opões seja verdadeira, preencher com “1”\.

__OS3763__

__RN23__

__Registro E – Número do Documento: __

__Tela\-A__ ç__  Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

  __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ __ __  

  __E__

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __ 

Então, Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL__

Se não,  

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL

__OS3763__

__OS3341\-A2__

__RN24__

__Registro E – Número Final: __

__Tela\-A__ ç__  Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

  __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ __ __  

  __E__

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __ 

Então, Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL __

Se não,

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL

__OS3763__

__OS3341\-A2__

__RN25__

__Registro E – Valor Bruto: __

Preencher com o somatório do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

Se o campo COD\_CLASS\_DOC\_FIS da tabela DWT\_DOCTO\_FISCAL = ‘3’

Preencher com o campo VLR\_TOT\_NOTA da tabela DWT\_DOCTO\_FISCAL

__OS3763__

__CH10396\-A__

__RN26__

__Registro E – Valor do Serviço: __

Preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV

__OS3763__

__RN27__

__Registro E – Alíquota: __

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 32 da SAFX09\)\. 

__OS3763__

__RN28__

__Registro E – Situação do Documento: __

Preencher com:

2, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = ‘S’   \(campo 30 da SAFX07\)

3, quando o campo IND\_NOTA\_SERVICO da tabela DWT\_DOCTO\_FISCAL = ‘E’  \(campo 137 da SAFX07\)

1, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> ‘S’ \(campo 30 da SAFX07\)

4, não será tratado nessa OS\.

__OS3763__

__RN29__

__Registro E – Simples Nacional: __

__\[ALTERADO MFS6978\]__

Preencher com:

__1__,quando o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota for igual a “01 – EPP\(Empresa de Pequeno Porte\)” ou “04 – Microempresa \(ME\)”\.

__3__, quando o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota for igual a “05 \- MEI \( Micro Empreendedor Individual\)"”

__2__,quando nenhuma das opões acima forem verdadeiras\.

__OS3763__

__MFS6978__

__RN30__

__Registro E – Inscrição Municipal do Tomador: __

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota Se a pessoa fis/jur não for de Belo Horizonte, esse campo não deve ser preenchido\.

__OS3763__

__RN31__

__Registro E – CNPJ do tomador: __

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota quando o tamanho do campo for igual a 14\. 

Se o campo tiver 11 posições, não preencher\.

__OS3763__

__RN32__

__Registro E – CPF do tomador: __

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota quando o tamanho do campo for igual a 11\. 

Se o campo tiver 14 posições ou o tomador for estrangeiro, não preencher\.

__OS3763__

__RN33__

__Registro E – Nome do tomador: __

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota 

__OS3763__

__RN34__

__Registro E – Logradouro do tomador: __

Preencher com o campo TP\_LOGRADOURO \+ campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__OS3763__

__RN35__

__Registro E – Número do Imóvel do tomador: __

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__OS3763__

__RN36__

__Registro E – Complemento do tomador: __

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__OS3763__

__RN37__

__Registro E – Bairro do tomador: __

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__OS3763__

__RN38__

__Registro E – Cidade do tomador: __

Preencher com o campo COD\_UF \+ COD\_MUNICIPIO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Se o estado da pessoa fis/jur = “EX”, preencher com 9999999\.

__OS3763__

__RN39__

__Registro E – Pais do tomador: __

Preencher com “1058”

__\[ALTERADA – CH21781\_2016\]__

Se o estado da pessoa fis/jur = “EX”, preencher com o conteúdo do campo COD\_PAIS da tabela X04\_PESSOA\_FIS\_JUR, vinculada à tabela PAIS, concatenando com o conteúdo do campo DIG\_VERIFICADOR\.

__OS3763__

__CH21781\_2016__

__RN40__

__Registro E – CEP do tomador: __

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\. 

Se o estado da pessoa fis/jur = “EX”, não preeencher\.

__OS3763__

__RN41__

__Registro E – Telefone do tomador: __

Preencher com os campos DDD \+ TELEFONE da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\. Somente números\.

__OS3763__

__RN42__

__Registro E – E\-mail do tomador: __

Preencher com o campo E\_MAIL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\. 

__OS3763__

__RN43__

__Registro E – Inscrição Municipal do terceiro vinculado/intermediário: __

Não preencher\.

__OS3763__

__RN44__

__Registro E – CNPJ do terceiro vinculado/intermediário: __

Não preencher\.

__OS3763__

__RN45__

__Registro E – CPF do terceiro vinculado/intermediário: __

Não preencher\.

__OS3763__

__RN45__

__Registro E – Nome do terceiro vinculado/intermediário: __

Não preencher\.

__OS3763__

__RN46__

__Registro E – Logradouro do terceiro vinculado/intermediário: __

Não preencher\.

__OS3763__

__RN47__

__Registro E – Número do imóvel do terceiro vinculado/intermediário: __

Não preencher\.

__OS3763__

__RN48__

__Registro E – Complemento do terceiro vinculado/intermediário: __

Não preencher\.

__OS3763__

__RN49__

__Registro E – Bairro do terceiro vinculado/intermediário: __

Não preencher\.

__OS3763__

__RN50__

__Registro E – Cidade do terceiro vinculado/intermediário: __

Não preencher\.

__OS3763__

__RN51__

__Registro E – País do terceiro vinculado/intermediário: __

Não preencher\.

__OS3763__

__RN52__

__Registro E – CEP do terceiro vinculado/intermediário: __

Não preencher\.

__OS3763__

__RN53__

__Registro E – Telefone do terceiro vinculado/intermediário: __

Não preencher\.

__OS3763__

__RN54__

__Registro E – E\-mail do terceiro vinculado/intermediário: __

Não preencher\.

OS3763

__RN55__

__Registro E – Local da prestação: __

Se COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido, preencher com o campo COD\_UF \+ COD\_MUNICIPIO da tabela MUNICIPIO referente ao  campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\.

Senão preencher com o campo COD\_UF \+ COD\_MUNICIPIO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

*Obs: O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS\.*

OS3763

__RN56__

__Registro E – Pais da prestação dos serviços: __

Preencher com “1058”

OS3763

__RN57__

__Registro E – Descrição do evento: __

Não Preencher

OS3763

__RN58__

__Registro E – Data do evento: __

Não Preencher

OS3763

__RN59__

__Registro E – Data de competência: __

Preencher com o mês e ano do campo Data Inicial da tela de geração do Meio Magnético\. Formato: MMAAAA\.

OS3763

__RN60__

__Registro E – Data de Cancelamento: __

Se o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = “S”, preencher com o campo DAT\_CANCELAMENTO da tabela DWT\_DOCTO\_FISCAL\.

Se o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> “S”, não preeencher\.

OS3763

__RN61__

__Registro E – Motivo de Cancelamento: __

Se o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = ‘S’, preencher com o campo COD\_MOTIVO da tabela DWT\_DOCTO\_FISCAL\. Caso contrário, não preencher\.

OS3763

__RN62__

__Registro E – Outro Motivo de Cancelamento: __

Se o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = ‘S’ e o campo E – Motivo do Cancelamento estiver preenchido com “9 – Outros Motivos”, preencher com o campo OBS\_COMPL\_MOTIVO da tabela DWT\_DOCTO\_FISCAL\.

Senão, não preencher\.

OS3763

__RN63__

__Registro E – Número da Nota Substituidora: __

Não Preencher

OS3763

__RN64__

__Regra p/ Registro Tipo D – Dedução de Materiais e Subempreitadas das NF Emitidas de Const\. Civil__

Para que esse registro seja gerado a nota fiscal emitida deverá ser de construção civil \(IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’ referente ao serviço cadastrado na nota\)\.

Quando a nota for de construção civil, a geração deve verificar se existe dedução para essa nota no menu Manutenção – Deduções\. Se houver a geração deve apresentar um registro para a nota emitida \(tipo E\) e tantos quantos forem os registros de dedução \(tipo D\)\.

- Caso a dedução esteja vinculada a um serviço prestado especifico esta linha deve vir logo abaixo do registro tipo “E” correspondente\. Se a nota de serviço prestado tiver alguma quebra, o registro D deve vir abaixo de todas as quebras referentes a nota de serviço prestao\. Ex:

E001

E001

D001

Este registro deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- IND\_TP\_SERVICO da tabela X2018\_SERVICOS = ‘1’

__OS3763__

RN65

__Registro D – Tipo do registro__

Preencher com texto fixo “D”

__OS3763 __

RN66

__Registro D – Número do Documento que sofrerá Dedução__

__Tela\-A__ ç__  Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

  __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ __ __  

  __E__

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __ 

Então, Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL__

Se não,  

Preencher com o campo Numero Doc\. Fiscal da nota fiscal que será deduzida na tela Manutenção – Deduções\. \(aba Documento Fiscal\)

Se o modelo da nota fiscal selecionada na aba Documento Fiscal estiver parametrizada no menu Parametros por Município – Parâmetros Tipo Docto Msaf x Tipo Docto com a opção “5 \- NFS\-e – Nota Fiscal de Serviços Eletrônica”, esse campo deve ser preenchido da seguinte forma: 4 dígitos do Ano do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(AAAA\) \+ campo \_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__OS3763__

__OS3341\-A2__

RN67

__Registro D – Valor bruto do documento que sofrerá Dedução__

Preencher com o campo Valor Total da Nota da nota fiscal que será deduzida na tela Manutenção – Deduções\. \(aba Documento Fiscal\)

__OS3763__

RN68

__Registro D – Tipo da Dedução__

Preencher com:

1, quando o campo Tipo de Dedução da Tela Manutenção – Deduções estiver preenchido com M – Material\.

2, quando o campo Tipo de Dedução da Tela Manutenção – Deduções estiver preenchido com A – Serviços\.

3, quando o campo Tipo de Dedução da Tela Manutenção – Deduções estiver preenchido com B – Alimentação e Bebidas/Frigobar\.

4, quando o campo Tipo de Dedução da Tela Manutenção – Deduções estiver preenchido com C – Reembolso de despesas\.

5, quando o campo Tipo de Dedução da Tela Manutenção – Deduções estiver preenchido com D – Outras Deduções\.

6, quando o campo Tipo de Dedução da Tela Manutenção – Deduções estiver preenchido com E – Repasse Concorciado\.

__OS3763__

__RN69__

__Registro D – Descrição do Tipo da Dedução__

Preencher com o campo Outras Deduções da tela Manutenção – Deduções quando o campo Tipo de Dedução for igual a D – Outras Deduções\. Caso contrário, não preencher\.

__OS3763__

__RN70__

__Registro D – Data de Emissão do documento utilizado na dedução__

Preencher com o campo Data Emissão da nota fiscal que será deduzida na tela Manutenção – Deduções\. \(aba Dedução\)

__OS3763__

__RN71__

__Registro D – Número de documento utilizado na Dedução__

Preencher com o campo Nº Nota Fiscal da nota fiscal que será deduzida na tela Manutenção – Deduções\. \(aba Dedução\) 

Se o campo NFS\-e – Nota Fiscal de Serviços Eletrônica referente ao tipo de documento informado no campo Tipo Documento da aba Dedução da tela Manutenção – Deduções estiver marcado, esse campo deve ser preenchido da seguinte forma: 4 dígitos do Ano do campo Data de Emissão \+ campo Nº Nota Fiscal\.

__OS3763__

__RN72__

__Registro D – Valor Bruto do documento utilizado na Dedução/Repasse__

Preencher com o campo Valor da Nota da nota fiscal que será deduzida na tela Manutenção – Deduções \(aba Dedução\)

__OS3763__

__RN73__

__Registro D – Valor do Material, serviço ou repasse utilizado nesta na operação__

Preencher com o campo Valor Dedução da nota fiscal que será deduzida na tela Manutenção – Deduções\. \(aba Dedução\)

__OS3763__

__RN74__

__Registro D – Alíquota__

Preencher com o campo Aliquota da nota fiscal que será deduzida na tela Manutenção – Deduções\. \(aba Dedução\)

__OS3763__

__RN75__

__Registro D – Tipo de recolhimento do ISSQN__

Preencher com “2” se o campo ISS Retido da tela Manutenção – Deduções \(aba Dedução\) estiver marcado\. Caso contrário, preencher com “1”\.

__OS3763__

__RN76__

__Registro D – Inscrição Municipal do emissor do documento de Dedução/Repasse__

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR referente ao campo Pessoa Fis/Jur da tela de Manutenção – Deduções\. \(aba Dedução\)

__OS3763__

__RN77__

__Registro D – CNPJ do emissor do documento de Dedução/Repasse__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente ao campo Pessoa Fis/Jur da tela de Manutenção – Deduções\. \(aba Dedução\) quando tiver 14 posições\.

Se o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR tiver 11 posições, não preencher\.

__OS3763__

__RN78__

__Registro D – CPF do emissor do documento de Dedução/Repasse__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente ao campo Pessoa Fis/Jur da tela de Manutenção – Deduções\. \(aba Dedução\) quando tiver 11 posições\.

Se o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR tiver 14 posições, não preencher\.

__OS3763__

__RN79__

__Registro D – Razão Social do emissor do documento de Dedução/Repasse__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente ao campo Pessoa Fis/Jur da tela de Manutenção – Deduções\. \(aba Dedução\)

__OS3763__

__RN80__

__Registro D – Logradouro do emissor do documento de Dedução/Repasse__

Preencher com o campo TP\_LOGRADOURO \+ ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente ao campo Pessoa Fis/Jur da tela de Manutenção – Deduções\. \(aba Dedução\)

__OS3763__

__RN81__

__Registro D – Número do endereço do emissor do documento de Dedução/Repasse __

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente ao campo Pessoa Fis/Jur da tela de Manutenção – Deduções\. \(aba Dedução\)

__OS3763__

__RN82__

__Registro D – Complemento do emissor do documento de Dedução/Repasse__

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente ao campo Pessoa Fis/Jur da tela de Manutenção – Deduções\. \(aba Dedução\)

__OS3763__

__RN83__

__Registro D – Nome do Bairro do emissor do documento de Dedução/Repasse__

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR referente ao campo Pessoa Fis/Jur da tela de Manutenção – Deduções\. \(aba Dedução\)

__OS3763__

__RN84__

__Registro D – Cidade do emissor do documento de Dedução/Repasse__

Preencher com o campo COD\_UF \+ COD\_MUNICIOPIO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR referente ao campo Pessoa Fis/Jur da tela de Manutenção – Deduções\. \(aba Dedução\)

Se o estado da pessoa fis/jur = “EX”, preencher com 9999999\.

__OS3763__

__RN85__

__Registro D – País do emissor do documento de Dedução/Repasse__

Preencher com “1058”

__\[ALTERADA – CH21781\_2016\]__

Se o estado da pessoa fis/jur = “EX”, preencher com o conteúdo do campo COD\_PAIS da tabela X04\_PESSOA\_FIS\_JUR referente ao campo Pessoa Fis/Jur da tela de Manutenção – Deduções \(aba Dedução\), vinculada à tabela PAIS, concatenando com o conteúdo do campo DIG\_VERIFICADOR\.

__OS3763__

__CH21781\_2016__

__RN86__

__Registro D – CEP do emissor do documento de Dedução/Repasse__

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR referente ao campo Pessoa Fis/Jur da tela de Manutenção – Deduções\. \(aba Dedução\)

Se o estado da pessoa fis/jur = “EX, não preeencher\.

__OS3763__

__RN87__

__Registro D – Telefone do emissor do documento de Dedução/Repasse __

Preencher com o campo DDD \+ TELEFONE da tabela X04\_PESSOA\_FIS\_JUR referente ao campo Pessoa Fis/Jur da tela de Manutenção – Deduções\. \(aba Dedução\)

__OS3763__

__RN88__

__Registro D – E\-mail do emissor do documento de Dedução/Repasse__

Preencher com o campo E\_MAIL da tabela X04\_PESSOA\_FIS\_JUR referente ao campo Pessoa Fis/Jur da tela de Manutenção – Deduções\. \(aba Dedução\)

__OS3763__

__RN89__

__Regra p/ Registro Tipo R__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do documento \(cód\_class\_doc\_fis = ‘2’, ‘3’\) ou Classificação do documento \(cód\_class\_doc\_fis = ‘9’\) e codigo do documento \(cód\_docto = ‘RPA’\)
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência 
- Nota não cancelada \(situacao <> ‘S’\)

__OS3763__

__RN90__

__Registro R – Tipo do Registro: __

Preencher com o texto fixo “R”\.

__OS3763__

__RN91__

__Registro R – Data de pagamento ou reconhecimento do crédito: __

__\[ALTERADO MFS7644\]__

Se o campo DT\_PAGTO\_NF da tabela DWT\_DOCTO\_FISCAL\. \(campo 175 da SAFX07\) estiver preenchido verificar se o campo DATA\_FISCAL da tabela DWT\_DOCTO\_FISCAL > campo DT\_PAGTO\_NF

Caso verdadeiro: 

- Para que esse campo seja preenchido com o campo DT\_PAGTO\_NF da tabela DWT\_DOCTO\_FISCAL \(campo 175 da SAFX07\), é necessário que pelo menos umas das opções da regra \[R1\-RN0001\] seja verdadeira\. Verificar o documento DE\-  PARA \- Municipal\.xls abas: Detalhamento e ISS DIGITAL BH\.

Caso contrário:

       \- Se nenhuma das opções for verdadeira, preencher com o campo DATA\_FISCAL da tabela DWT\_DOCTO\_FISCAL\.

__OS3763__

__CH8546/2015__

__MFS7644__

__RN92__

__Registro R – Data de emissão: __

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. 

__OS3763__

__ RN93__

__Registro R – Modelo do Documento: __

Preencher com o campo Modelo da tela Parâmetros por Município – Parâmetros – Modelo Msaf x Modelo referente ao modelo cadastrado na nota fiscal\.

Caso a parametrização de Modelo Msaf x Modelo não tenha sido realizada para o modelo da nota, deve ser verificada se foi  feita a parametrização de Modelo Msaf x Município Prestador Msaf x Modelo\.

Se não existir nenhuma das duas parametrizações cadastradas, deve ser gerado esse campo em branco e exibir no log a mensagem informando que a parametrização deve ser realizada\.

Caso a parametrização de Modelo Msaf x Modelo não tenha sido realizada para o modelo da nota, a geração deve gerar esse campo em branco e exibir mensagem no log informando que a parametrização deve ser realizada\.

Se o modelo não estiver preenchido na nota fiscal, a geração deve exibir uma mensagem informando que o modelo deve ser preenchido na nota fiscal\.

__OS3763__

__/__

__OS4080__

__MFS\-848124__

__RN94__

__Registro R – Série do Documento __

__\[MFS44517\] Alteração do preenchimento da série – série em branco vai utilizar a parametrização Modelo Msaf x Série__

Se a série cadastrada na nota fiscal estiver preenchida com branco

     Preencher com o campo Série da tela de Parâmetros por Município – Parâmetros – Série Msaf x Modelo Msaf x Série   

      referente ao modelo cadastrado na nota e o campo série em branco 

Senão se essa parametrização não estiver cadastrada

     O campo deve ser preenchido com 0 \(zero\), independente da parametrização\.

__Para notas com Série diferente de branco:__

Considerar a parametrização de Série Msaf x Modelo Msaf x Série quando esta existir\. Caso a mesma não seja encontrada nesta parametrização, buscar na tela de Parâmetros \- Série Msaf x Série, conforme detalhamento das regras abaixo:

- Preencher com o campo Série da tela de Parâmetros por Município – Parâmetros – Série Msaf x Modelo Msaf x Série referente ao modelo e série cadastrado na nota\. Se essa parametrização não estiver cadastrada: Preencher com o campo Série da tela Parâmetros por Município – Parâmetros – Série Msaf x Série referente a série cadastrada na nota fiscal e exibir mensagem no log informando que a parametrização de Modelo Msaf x Série não foi realizada e que será considerada a parametrização de Série Msaf x Série\.
- Caso a parametrização de Série Msaf x Série não tenha sido realizada para a série da nota e a série cadastrada na nota fiscal não está preenchida com branco, a geração deve gerar esse campo em branco e exibir mensagem no log informando que a parametrização deve ser realizada\.

###### Se a série não estiver preenchida na nota fiscal, ou seja, se a série for nula, a geração deve exibir uma mensagem informando que a série deve ser preenchida na nota fiscal\.

__OS3763/__

__CH1250\-A/__

__OS4054/__

__MFS44517__

__MFS\-65383__

__RN95__

__Registro R – Subsérie do documento __

Preencher com o campo SUB\_SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__OS3763__

__RN96__

__Registro R – Situação Especial de Responsabilidade: __

__\[ALTERADA – CH19837\-A\_2014\]__

Preencher com o conteúdo parametrizado no campo Parâmetro da tela Parâmetros por Município – Parâmetros – Classificação de Serviços – DES\-BH – Município quando o campo Tabela dessa mesma tela estiver preenchido com “Situação Especial de Responsabilidade” para o serviço cadastrado na nota fiscal e para o município do local de prestação de serviço \(campo 73\-Código do Município do ISS da tabela SAFX07\) considerando para a seleção o campo COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS correspondente\.

Caso o serviço não esteja parametrizado na tela Parâmetros por Município – Parâmetros – Classificação de Serviços – DES\-BH – Município, preencher com o conteúdo parametrizado no campo Parâmetro da tela Parâmetros por Município – Parâmetros – Classificação de Serviços – DES\-BH – Pessoa Fis/Jur quando o campo Tabela dessa mesma tela estiver preenchido com “Situação Especial de Responsabilidade” para o serviço cadastrado na nota fiscal e para o município do local de prestação de serviço \(campo 73\-Código do Município do ISS da tabela SAFX07\) considerando para a seleção o campo COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS correspondente\.

Caso nenhuma das duas parametrizações tenham sido realizadas, a geração deve gerar esse campo em branco e exibir mensagem no log informando que a parametrização deve ser realizada\.

__OS3763__

__CH13359\_2014__

__CH19837\-A\_2014__

__RN97__

__Registro R – Motivo de Não Retenção: __

__\[ALTERADA – CH19837\-A\_2014 / MFS528514\]__

Se o campo R – Tipo de Recolhimento do ISSQN = “1”, então:

Preencher com o conteúdo parametrizado no campo Parâmetro da tela Parâmetros por Município – Parâmetros – Classificação de Serviços – DES\-BH – Pessoa Fis/Jur quando o campo Tabela dessa mesma tela estiver preenchido com “Motivo de Não Retenção” para o serviço cadastrado na nota fiscal e para o município do local de prestação de serviço \(campo 73\-Código do Município do ISS da tabela SAFX07\) considerando para a seleção o campo COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS correspondente\.

Caso o parâmetro de Pessoa Fis/Jur não esteja parametrizado na tela Parâmetros por Município – Parâmetros – Classificação de Serviços – DES\-BH – Pessoa Fis/Jur, preencher com o conteúdo parametrizado no campo Parâmetro da tela Parâmetros por Município – Parâmetros – Classificação de Serviços – DES\-BH – Município quando o campo Tabela dessa mesma tela estiver preenchido com “Motivo de Não Retenção” para o serviço cadastrado na nota fiscal e para o município do local de prestação de serviço \(campo 73\-Código do Município do ISS da tabela SAFX07\) considerando para a seleção o campo COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS correspondente\.

Caso nenhuma das duas parametrizações tenham sido realizadas, a geração deve gerar esse campo em branco e exibir mensagem no log informando que a parametrização deve ser realizada\.

Senão, preencher com “16”\.

Preencher com o conteúdo parametrizado no campo Parâmetro da tela Parâmetros por Município – Parâmetros – Classificação de Serviços – DES\-BH – Município quando o campo Tabela dessa mesma tela estiver preenchido com “Motivo de Não Retenção” para o serviço cadastrado na nota fiscal e para o município do local de prestação de serviço \(campo 73\-Código do Município do ISS da tabela SAFX07\) considerando para a seleção o campo COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS correspondente\.

Caso o serviço não esteja parametrizado na tela Parâmetros por Município – Parâmetros – Classificação de Serviços – DES\-BH – Município, preencher com o conteúdo parametrizado no campo Parâmetro da tela Parâmetros por Município – Parâmetros – Classificação de Serviços – DES\-BH – Pessoa Fis/Jur quando o campo Tabela dessa mesma tela estiver preenchido com “Motivo de Não Retenção” para o serviço cadastrado na nota fiscal e para o município do local de prestação de serviço \(campo 73\-Código do Município do ISS da tabela SAFX07\) considerando para a seleção o campo COD\_MUNIC\_MSAF da tabela X2097\_MUNIC\_ISS correspondente\.

__OS3763__

__CH13359\_2014__

__CH19837\-A\_2014__

__MFS528514__

__RN98__

__Registro R – Local da incidência: __

Se COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido, preencher com o campo COD\_UF \+ COD\_MUNICIPIO da tabela MUNICIPIO referente ao  campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\.

Senão preencher com o campo COD\_UF \+ COD\_MUNICIPIO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

*Obs: O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS\.*

__OS3763__

__RN99__

__Registro R – __<a id="OLE_LINK18"></a><a id="OLE_LINK19"></a><a id="OLE_LINK20"></a><a id="OLE_LINK21"></a>__Tipo de Recolhimento do ISSQN: __

__\[ALTERADA – CH7516\_2016\]__

Para que esse campo seja preenchido com “2 1”, é necessário que pelo menos umas das opções da regra \[R1\-RN0001\] seja verdadeira\. Verificar o documento DE\-PARA \- Municipal\.xls abas: Detalhamento e ISS DIGITAL BH\.

Caso nenhuma das opões seja verdadeira, preencher com “1 2”\.

__OS3763__

__CH7516\_2016__

__RN100__

__Registro R – Número do documento: __

__Tela\-A__ ç__  Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

  __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ __ __  

  __E__

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __ 

Então, Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL__

Se não,  

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL

Se o campo Registro E – Modelo do Documento estiver preenchido com “5 \- NFS\-e – Nota Fiscal de Serviços Eletrônica”,

esse campo deve ser preenchido da seguinte forma: 4 dígitos do Ano do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(AAAA\) \+ campo \_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

 

Se o campo Registro R – Modelo do Documento estiver preenchido com “5 – NFS\-e – Nota Fiscal de Serviços Eletrônica”,

deve ser verificado o parâmetro <a id="_Hlk16081519"></a>“Considerar Ano de Emissão, no campo Número do Documento, para as NFS\-e Recebidas” na tela de geração do meio magnético\.

__SE__ o parâmetro estiver __SELECIONADO__, o campo deve ser preenchido da seguinte forma:

4 dígitos do Ano do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(AAAA\) \+

campo \_DOCFIS da tabela DWT\_DOCTO\_FISCAL

__SENÃO__, o campo deve ser preenchido da seguinte forma:

campo \_DOCFIS da tabela DWT\_DOCTO\_FISCAL

 

__OS3763__

__OS3341\-A2__

__MFS28749__

__RN101__

__Registro R – Valor Bruto do documento: __

Preencher com o somatório do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\.

Se o campo COD\_CLASS\_DOC\_FIS da tabela DWT\_DOCTO\_FISCAL = ‘3’

Preencher com o campo VLR\_TOT\_NOTA da tabela DWT\_DOCTO\_FISCAL

__OS3763__

__CH10396\-A__

__RN102__

<a id="OLE_LINK9"></a><a id="OLE_LINK10"></a><a id="OLE_LINK11"></a>__Registro R – Valor do Serviço: __

Preencher com o somatório do campo <a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>VLR\_SERVICO da tabela DWT\_ITENS\_SERV\.

__SE__ o somatório do campo Base ISS \(campo VLR\_BASE\_ISS\_1 da DWT\_ITENS\_SERV\) for __MENOR__ que o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV __E__ __MAIOR__ que zero

          Preencher com o somatório do campo Base ISS \(campo VLR\_BASE\_ISS\_1 da DWT\_ITENS\_SERV\)

__SENÃO__, preencher com o somatório do campo VLR\_SERVICO da tabela DWT\_ITENS\_SERV\.

__\[ALTERADA – CH12081\_2014\]__

__Tratamento para NF de Construção Civil:__

Preencher com o somatório do campo Base ISS \(campo <a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>VLR\_BASE\_ISS\_1 da DWT\_ITENS\_SERV \- correspondente ao campo BASE\_ISS da SAFX09\) somente quando:

\- O campo Tipo de Serviço da tabela de Serviços \(campo IND\_TP\_SERVICO da SAFX2018\) for igual a “1” __E__ o valor da Base ISS \(VLR\_BASE\_ISS\_1 da DWT\_ITENS\_SERV\) for diferente do valor do Serviço \(VLR\_SERVICO da tabela DWT\_ITENS\_SERV\)\.

__OS3763__

__CH12081\_2014__

__MFS30450__

__RN103__

__Registro R – Alíquota: __

__\[MFS85255\] __Tratamento para considerar também o Campo de Alíquota ISS Retido

__\[MFS627760\] Tratamento para não preencher a alíquota ISS Retido fora do município__

__Tratamento:__

     __Se__ o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1"

        __E __o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL for diferente do município informado no campo COD\_MUNICIPIO da tabela ESTABELECIMENTO

          Preencher com 0

__Senão __

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. \(campo 32 da SAFX09\) __Ou   __

      Preencher com o campo VLR\_ALIQ\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV \(campo 97 da SAFX09\)\.

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\.\(campo 32 da SAFX09\) __Ou__

__   Se__ o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1"

      Preencher com o campo VLR\_ALIQ\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV \(campo 97 da SAFX09\)\.

__OS3763__

__MFS85255__

__MFS627760__

__RN104__

__Registro R – Simples Nacional: __

__\[ALTERADO MFS6978\]__

Preencher com:

__1__,quando o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota for igual a “01 – EPP\(Empresa de Pequeno Porte\)” ou “04 – Microempresa \(ME\)”\.

__3__, quando o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota for igual a “05 \- MEI \( Micro Empreendedor Individual\)"”

__2__,quando nenhuma das opões acima forem verdadeiras\.

__OS3763__

__MFS6978__

__RN105__

__Registro R – Inscrição Municipal:__ 

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota Se a pessoa fis/jur não for de Belo Horizonte, esse campo não deve ser preenchido\.

__OS3763__

__RN106__

__Registro R – CNPJ: __

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota quando o tamanho do campo for igual a 14\. 

Se o campo tiver 11 posições, não preencher\.

__OS3763__

__RN107__

__Registro R – CPF: __

Preencher com o campo CGC\_CPF da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota quando o tamanho do campo for igual a 11\. 

Se o campo tiver 14 posições ou o tomador for estrangeiro, não preencher\.

__OS3763__

__RN108__

__Registro R – Nome do prestador: __

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota

__OS3763__

__RN109__

__Registro R – Logradouro do prestador: __

Preencher com o campo TP\_LOGRADOURO \+ campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__OS3763__

__RN110__

__Registro R – Número do imóvel do prestador: __

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__OS3763__

__RN111__

__Registro R – Complemento do prestador __

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__OS3763__

__RN112__

__Registro R – Bairro do prestador __

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__OS3763__

__RN113__

__Registro R – Cidade do prestador__

Preencher com o campo COD\_UF \+ COD\_MUNICIPIO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

Se o estado da pessoa fis/jur = “EX”, preencher com 9999999\.

__OS3763__

__RN114__

__Registro R – Pais do prestador: __

Preencher com “1058”

__\[ALTERADA – CH21781\_2016\]__

Se o estado da pessoa fis/jur = “EX”, preencher com o conteúdo do campo COD\_PAIS da tabela X04\_PESSOA\_FIS\_JUR, vinculada à tabela PAIS, concatenando com o conteúdo do campo DIG\_VERIFICADOR\.

__OS3763__

__CH21781\_2016__

__RN115__

__Registro R – CEP do prestador __

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\. 

Se o estado da pessoa fis/jur = “EX”, não preencher\.

__OS3763__

__RN116__

__Registro R – Telefone do prestador __

Preencher com os campos DDD \+ TELEFONE da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\. Somente números\.

__OS3763__

__RN117__

__Registro R – E\-mail do prestador __

Preencher com o campo E\_MAIL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota\.

__OS3763__

__RN118__

__Registro R – Inscrição Municipal do tomador: __

Não Preencher\.

__OS3763__

__RN119__

__Registro R – CNPJ do tomador: __

Não Preencher\.

__OS3763__

__RN120__

__Registro R – CPF do tomador: __

Não Preencher\.

__OS3763__

__RN121__

__Registro R – Nome do tomador: __

Não Preencher\.

__OS3763__

__RN122__

__Registro R – Logradouro do tomador __

Não Preencher\.

__OS3763__

__RN123__

__Registro R – Número do imóvel do tomador__

Não Preencher\.

__OS3763__

__RN124__

__Registro R – Complemento do tomador __

Não Preencher\.

__OS3763__

__RN125__

__Registro R – Bairro do tomador__

Não Preencher\.

__OS3763__

__RN126__

__Registro R – Cidade do tomador __

Não Preencher\.

__OS3763__

__RN127__

__Registro R – País do tomador__

Não Preencher\.

__OS3763__

__RN128__

__Registro R – CEP do tomador de serviços: __

Não Preencher\.

__OS3763__

__RN129__

__Registro R – Telefone do tomador: __

Não Preencher\.

__OS3763__

__RN130__

__Registro R – E\-mail do tomador: __

Não Preencher\.

__OS3763 __

__RN131__

__Registro R – Local da prestação dos serviços: __

Se COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL estiver preenchido, preencher com o campo COD\_UF \+ COD\_MUNICIPIO da tabela MUNICIPIO referente ao  campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL\.

Senão preencher com o campo COD\_UF \+ COD\_MUNICIPIO da tabela MUNICIPIO referente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

*Obs: O campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL é correspondente ao campo COD\_MUNIC\_ISS da tabela X2097\_MUNIC\_ISS\.*

__OS3763__

__RN132__

__Registro R – País da prestação dos serviços: __

Preencher com “1058”

__OS3763__

__RN133__

__Registro R – Descrição do Evento __

Não Preencher\.

__OS3763__

__RN134__

__Registro R – Data do Evento: __

Não Preencher\.

__OS3763__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


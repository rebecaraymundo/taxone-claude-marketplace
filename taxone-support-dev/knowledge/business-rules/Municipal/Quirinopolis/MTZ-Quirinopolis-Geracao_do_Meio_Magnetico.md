# MTZ-Quirinopolis-Geracao_do_Meio_Magnetico

- **Fonte:** MTZ-Quirinopolis-Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2025-10-08
- **Tamanho:** 45 KB

---

# Quirinopolis \- Geração do Meio Magnético

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3548

Geração do Meio Magnético Quirinopolis

Este documento tem como objetivo criar o novo módulo que permita a geração do meio magnético de Quirinopolis que irá conter as informações de serviços prestados e tomados\.

OS3926\-U

Geração do Meio Magnético Quirinopolis \- Atendimento a constução civil/telecomunicações/utilities

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para o município atendido pelo validador Quirinopolis\.

MFS\_2071

DW \- MUNICIPAL \- Quirinópolis – Retirada do range da data inicial e final\.

Este documento tem como objetivo retirar o range da data inicial e data final da tela de geração do arquivo magnético para permitir o envio das notas emitidas fora do mês de competência com data de emissão no mês de incidência\.

MFS829438

DW \- MUNICIPAL – Quirinópolis – Ajuste na Nomenclatura do arquivo\.

Este documento tem como objetivo, ajustar a nomenclatura dos arquivos gerados pelo meio magnéticos passando a ser “Código Empresa \+ Código Estabelecimento \+ Município \+ MMAAAA”\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Quirinopolis” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços prestados e tomados no município de Quirinopolis”\.

OS3548

__RN02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “GO” e ao código de município do IBGE igual a “18508” \(Quirinopolis\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Quirinopolis, Goiás\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__OS3548__

__RN03__

__Estrutura de menus do módulo Quirinopolis:__

Deverão ser criados os seguintes menus e sub\-menus no módulo Quirinopolis:

- Arquivo
- Obrigações
	- Geração do Meio Magnético
	- Arquivo de Entradas de Serviços \(Consti\. Civil/Utilities/Telecom\)
- Janela
- Ajuda

__OS3548 OS3926\-U__

__RN04__

__Regra de criação do nome do arquivo__

Serviços Prestados:

__SP\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.XML__, onde:

       __SP__: Apenas registros de serviços prestados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.XML__: extensão do arquivo

Ex: SP\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.XML

__P\_QUIRINOPOLIS\_DDMMAAAA\.XML__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __P\_QUIRINOPOLIS__: representa a obrigação que está sendo gerada, no caso Quirinopolis\.

       __\.XML__: extensão do arquivo\.

Ex: P\_QUIRINOPOLIS\_01012010\.XML

Serviços Tomados:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ DDMMAAAA\.XML__, onde:

       __ST__: Apenas registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.XML__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_01012010\.XML

__T\_QUIRINOPOLIS\_DDMMAAAA\.XML__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __T\_QUIRINOPOLIS__: representa a obrigação que está sendo gerada, no caso Quirinopolis\.

       __\.XML__: extensão do arquivo\.

Ex: T\_QUIRINOPOLIS\_01012010\.XML

__OS3548__

<a id="_Hlk210845091"></a>__MFS829438__

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

Data Inicial: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

Data Final: deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

Gerar Serviços Prestados: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Gerar Serviços Contratados: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Tipo de Arquivo: deve ser exibido através de um ListBox, com as seguintes opções: “0 \- Normal” e “1 \- Retificada”\.

Estabelecimento: o sistema deve exibir os estabelecimentos pertencentes ao município de Quirinopolis, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__OS3548__

__MFS\_2071__

__RN06__

__Regras referentes à estrutura do Arquivo:__

O arquivo deve ter a extensão \.XML e deve conter a seguinte estrutura:

<declaracaoDeServicoDms>

<contribuinte>

   campos\.\.\.

</contribuinte>

<servicoDms>

   campos\.\.\.

</servicoDms>

<itensDeServico>

   <itemDeServico>

      campos\.\.\.

   </ itemDeServico >

   <itemDeServico>

      campos\.\.\.

   </ itemDeServico >

</itensDeServico>

</declaracaoDeServicoDms>

Os campos das tags <contribuinte> e <servicoDms> devem conter apenas um registro\.

Os campos da tag <itemDeServico> podem ter um ou mais registros, de acordo com o número de notas fiscais recuperadas\.

Quando não houver informação para qualquer tag a mesma ficará vazia, exemplo: <aliquota></aliquota>

__OS3548__

__RN07__

__Regra geral p/ recuperar serviços prestados__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Saída \(movto\_e\_s = ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência

Obs: Quando não houver notas fiscais para o período, não gerar arquivo magnético\.

__OS3548__

__RN08__

__Regra geral p/ recuperar serviços tomados__

Este registro deve conter todas as notas com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração
- Data fiscal dentro do período de referência
- Notas não canceladas \(situacao <> ‘S’\)

Obs: Quando não houver notas fiscais para o período, não gerar arquivo magnético\.

__OS3548__

__RN09__

__Regra p/ campo cgc da tag <contribuinte>__

Preencher com o campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento escolhido na tela de geração\. Deve ser preenchido entre as tags <cgc> e </cgc>\.

Somente números\.

__OS3548__

__RN10__

__Regra p/ o campo anoDeReferencia da tag <servicoDms>__

Preencher com o ano do campo Data Inicial da tela de geração do Meio Magnético\. Formato: AAAA\.

Preencher entre as tags <anoDeReferencia> e </anoDeReferencia>

__OS3548__

__RN11__

__Regra p/ o campo mesDeReferencia da tag <servicoDms>__

Preencher com o mês do campo Data Inicial da tela de geração do Meio Magnético\. Formato: MM\.

Preencher entre as tags <mesDeReferencia> e </mesDeReferencia>

__OS3548__

__RN12__

__Regra p/ o campo tipo da tag <servicoDms>__

Preencher com:

1, quando o campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL = ‘9’ 

2, quando o campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> ‘9’

Preencher entre as tags <tipo> e </tipo>

__OS3548__

__RN13__

__Regra p/ o campo tipoDeDeclaracao da tag <servicoDms>__

Preencher com:

0, quando forem recuperados pelo menos uma nota fiscal para o período indicado na tela de geração 

1, não será tratado\. Esse campo não poderá ser preenchido com essa informação, uma vez que quando não há notas fiscais para o período o arquivo magnético não é gerado\. 

Preencher entre as tags < tipoDeDeclaracao > e </ tipoDeDeclaracao >

__OS3548__

__RN14__

__Regra p/ o campo situacao da tag <servicoDms>__

Preencher com:

0, quando o campo Tipo de Arquivo da tela de geração estiver preenchido com “0 – Normal”

1, quando o campo Tipo de Arquivo da tela de geração estiver preenchido com “1 – Retificada”

Preencher entre as tags <situacao> e </situacao>

__OS3548__

__RN15__

__Regra p/ o campo cnpjPrestadorTomador da tag <itemDeServico>__

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\.

Preencher entre as tags < cnpjPrestadorTomador > e </ cnpjPrestadorTomador >

__OS3548__

__RN16__

__Regra p/ o campo razaoSocialDePrestadorTomadorNaoCadastrado da tag <itemDeServico>__

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR referente a pessoa fis/jur cadastrada na nota fiscal\.

Preencher entre as tags <razaoSocialDePrestadorTomadorNaoCadastrado> e    

</ razaoSocialDePrestadorTomadorNaoCadastrado>

__OS3548__

__RN17__

__Regra p/ o campo NumeroDaNotaFiscal da tag <itemDeServico>__

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Preencher entre as tags < NumeroDaNotaFiscal > e </ NumeroDaNotaFiscal >

__OS3548__

__RN18__

__Regra p/ o campo SerieDaNotaFiscal da tag <itemDeServico>__

Preencher com o campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

Preencher entre as tags < SerieDaNotaFiscal > e </ SerieDaNotaFiscal >

__OS3548__

__RN19__

__Regra p/ o campo dataDaNotaFiscal da tag <itemDeServico>__

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\. Formato: DD/MM/AAAA\.

Preencher entre as tags < dataDaNotaFiscal > e </ dataDaNotaFiscal >

__OS3548__

__RN20__

__Regra p/ o campo historicoDaNotaFiscal da tag <itemDeServico>__

Deixar em branco\.

Preencher entre as tags < historicoDaNotaFiscal > e </ historicoDaNotaFiscal >

__OS3548__

__RN21__

__Regra p/ o campo valorDaNotaFiscal da tag <itemDeServico>__

Preencher com o somatório do campo VLR\_TOT da tabela DWT\_ITENS\_SERV\. Preencher com 2 casas decimais separadas por vírgula\.

Preencher entre as tags < valorDaNotaFiscal > e </ valorDaNotaFiscal >

__OS3548__

__RN22__

__Regra p/ o campo baseDeCalculo da tag <itemDeServico>__

Preencher com o somatório do campo VLR\_BASE\_ISS\_1 da tabela DWT\_ITENS\_SERV\. Preencher com 2 casas decimais separadas por vírgula\.

Preencher entre as tags < baseDeCalculo > e </ baseDeCalculo >

__OS3548__

__RN23__

__Regra p/ o campo aliquota da tag <itemDeServico>__

Preencher com o somatório do campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV\. Preencher com 2 casas decimais separadas por vírgula\.

Preencher entre as tags < aliquota > e </ aliquota >

__OS3548__

__RN24__

__Regra p/ o campo recolhidoPeloTomador da tag <itemDeServico>__

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

Para serviços prestados:

Para que esse campo seja preenchido com “0”, é necessário que todas as seguintes opções sejam verdadeiras:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “2" e se o local da prestação do serviço = município do módulo selecionado OU 
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado \.

Caso nenhuma das opões seja verdadeira, preencher com “1”\.

Para serviços tomados:

Para que esse campo seja preenchido com “0”, é necessário que todas as seguintes opções sejam verdadeiras:

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado OU 
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado \.

Caso nenhuma das opões seja verdadeira, preencher com “1”\.

Preencher entre as tags < recolhidoPeloTomador > e </ recolhidoPeloTomador >

__OS3548__

__RN25__

__Regra p/ o campo notaFiscalCancelada da tag <itemDeServico>__

Para serviços prestados:

Preencher com:

0, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> ‘S’

1, quando o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL = ‘S’

Para serviços tomados:

Preencher com 0\.

Preencher entre as tags < notaFiscalCancelada > e </ notaFiscalCancelada >

__OS3548__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


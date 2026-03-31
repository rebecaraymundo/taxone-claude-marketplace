# MTZ_OBARATEC_GIAP_Geracao_Meio_Magnetico_Servicos_Prestados

- **Fonte:** MTZ_OBARATEC_GIAP_Geracao_Meio_Magnetico_Servicos_Prestados.docx
- **Modificado:** 2021-08-13
- **Tamanho:** 105 KB

---

THOMSON REUTERS

Municipal – OBARATEC GIAP

__SERVIÇOS PRESTADOS__

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN01

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Amparo” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Amparo”\.

RN02

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “1905” \(Amparo\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Amparo, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

RN03

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Amparo” deve ficar localizado no grupo “Municipal”\.

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados do município de Amparo”\.

RN04

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “10609” \(Carapicuíba\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Carapicuíba, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

RN05

__Estrutura de menus do módulo NFSE GIAP: \(OBARATEC\)__

Deverão ser criados os seguintes menu e sub\-menus no módulo NFSE GIAP: \(OBARATEC\)

- Arquivo
- Obrigações
	- Geração do Meio Magnético
- Janela
- Ajuda 

RN06

__Regra de criação do nome do arquivo:__

__Serviços Tomados:__

__       ST\_OBARATECGIAP\_MUNICIPIO\_DDMMAAAA\.XML__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __ST\_ OBARATECGIAP__: representa a obrigação que está sendo gerada\. 

       __\.XML__: extensão do arquivo\.

*Exemplo:* ST\_OBARATECGIAP\_AMPARO\_01012021\.xml

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__ST\_ OBARATECGIAP \_MUNICIPIO\_DDMMAAAA\_MMAAAA\.XML__, onde:

__               ST\_ OBARATECGIAP__: representa a obrigação que está sendo gerada\.    

__               MUNICIPIO__: representa o município que está sendo gerado\.   

               __DDMMAAAA__: representa a data inicial da geração\.   

__               MMAAAA:__ mês da competência referente à nota gerada

               __\.XML__: extensão do arquivo\.

Ex: ST\_OBARATECGIAP\_AMPARO\_01012021\_122020\.xml

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

RN07

__Regra p/ tela da Geração do Meio Magnético:__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

RN08

__Regra p/ Geração do Arquivo Magnético__

- Campos alfanuméricos/ numéricos que não houver preenchimento, gravar a tag vazia\.

RN09

__Regra p/ Recuperar Notas Fiscais de serviços tomados:__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)

*Observação: *Quando a nota fiscal não tiver itens não deve ser considerada\.

RN10

__Estrutura do Arquivo:__

__<nfe>__

__<notaFiscal>__

__<dadosPrestador>__

__<dataEmissao>__18/10/2019__</dataEmissao>__

__<im>__00008__</im>__

__<numeroRps>__0009__</numeroRps>__

__</dadosPrestador>__

__<dadosServico>__

__<bairro>__CENTRO__</bairro>__

__<cep>__01378\-056__</cep>__

__<cidade>__SAO BERNARDO__</cidade>__

__<complemento>__TERREO__</complemento>__

__<logradouro>__Rua Continental__</logradouro>__

__<numero>__345__</numero>__

__<pais>__BRASIL__</pais>__

__<uf>__SP__</uf>__

__</dadosServico>__

__<dadosTomador>__

__<bairro>__Vila Vermelha__</bairro>__

__<cep>__04218\-048__</cep>__

__<cidade>__SAO PAULO__</cidade__

__<complemento>__Sala 23A__</complemento>__

__<documento>__18023609807__</documento>__

__<email>__[teste@teste\.com\.br__</email> __](mailto:teste@teste.com.br%3c/email%3e%20%3cie%3eISENTO%3c/ie)

__<ie>__ISENTO__</ie>__

__<logradouro>__Rua Ostenda__</logradouro>__

__<nomeTomador>__SISVETOR__</nomeTomador>__

__<numero>__93__</numero>__

__<pais>__BRASIL__</pais>__

__<tipoDoc>__J__</tipoDoc>__

__<uf>__SP__</uf>__

__</dadosTomador>__

__<detalheServico>__

__<cofins>__0\.00__</cofins>__

__<csll>__0\.00__</csll>__

__<deducaoMaterial>__0\.00__</deducaoMaterial__

__<descontoIncondicional>__0__</descontoIncondicional>__

__<inss>__0\.00__</inss>__

__<ir>__0\.00__</ir>__

__<issRetido>__0\.00__</issRetido>__

__<item>__

__<aliquota>__0\.0__</aliquota>__

__<codigo>__0702__</codigo>__

__<descricao>__Locacao de galpao p funilaria__</descricao>__

__<valor>__100__</valor>__

__</item>__

__<obs>__Servicos realizados inloco\.__</obs>__

__<pisPasep>__0\.00__</pisPasep>__

__</detalheServico>__

__</notaFiscal>__

__<notaFiscal>__

__</detalheServico>__

__</notaFiscal>__

__</nfe>__

__   __

RN11

__Regra para tag <nfe> __Tag relacionada as informações da notas fiscal

TAG obrigatória\.

RN12

__Regra para tag <notaFiscal> __Tag relacionada à abertura da formatação do arquivo e que deve receber as informações das notas tomadas declaradas com o texto fixo __<notaFiscal>__

RN13

__Regra para tag <dadosPrestador> __Tag relacionada à abertura da identificação do prestador do serviço com o texto fixo: __<dadosPrestador>\.__

TAG obrigatória\.

RN14

__dataEmissao__

__Regra para tag <dataEmissao> __Tag relacionada à abertura dos dados do prestador do serviço com o texto fixo: __</dataEmissao>\.__

__Campo obrigatório\.__

Identifica a Data da Emissão da nota\. 

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAX07\)\.

__Obs\.: __Formato DD/MM/AAAA

Tamanho: 10

RN15

__im__

__Regra p/ tag <im> </im> __Tag relacionada a Inscrição Municipal do Prestador do Serviço com texto fixo __<im></im>\.__

TAG Obrigatória

Esse campo identifica o número da inscrição municipal do prestador\. Preencher a informação do campo INSC\_MUNICIPAL __\(campo 09\)__ da tabela __X04\_PESSOA\_FIS\_JUR__\.

__Campo obrigatório__

__Tratamento: __A __tag <im>__ é de preenchimento obrigatório e não está preenchida, favor verificar o campo inscrição municipal para a Pessoa Física/Jurídica\.

Formato: 9999999999999999

Tipo: Numérico

Tamanho: 16

RN16

__numeroRps__

__Regra p/ tag <numeroRps> Tag relacionada ao número da RPS com texto fixo: </numeroRPS>__

Preencher com o conteúdo do campo NUM\_RPS\_NFE da tabela DWT\_DOCTO\_FISCAL\.

__Campo obrigatório__

__Tratamento:__

- Se o campo do RPS não estiver preenchido no documento fiscal, deverá ser gravado com 0 \(zeros\) e emitida a mensagem de log: *“Erro: Favor preencher o número de RPS referente ao documento fiscal <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.*

Formato: 999999999999999

Tipo: Numérico

Tamanho: 16

RN17

__Regra para tag </dadosPrestador> __Tag relacionada ao fechamento da identificação do prestador do serviço com o texto fixo: __</dadosPrestador>\.__

TAG obrigatória\.

RN18

__Regra p/ tag <dadosServico> __Tag relacionada as informações do serviço com texto fixo: __<dadosServico>__

RN19

__bairro__

__Regra p/ tag <bairro> </bairro> __Tag relacionada a identificação do bairro do endereço do prestador\. 

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR \(campo 15 da SAFX04\) referente ao prestador cadastrado na nota fiscal\.

Tamanho: 100

RN20

__cep__

__Regra p/ tag <Cep> </Cep>__

Identifica o CEP do Prestador\. 

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR 

Formato: 99999\-999

Tamanho: 9

RN21

__cidade__

__Regra p/ tag <Cidade> </Cidade> __Tag relacionada a identificação da cidade do Prestador\. 

Preencher com o campo CIDADE da tabela X04\_PESSOA\_FIS\_JUR \(campo 16 da SAFX04\) referente ao prestador cadastrado na nota fiscal\.

OBS:\. Quando o Tomador for de OUTRO PAÍS colocar a cidade como EXTERIOR

__Campo obrigatório__

__Tratamento: __O campo __<cidade> do prestador é de preenchimento obrigatório, se não estiver preenchido__, exibir uma mensagem no log: “O campo __<cidade> do prestador __precisa estar preenchido__,__ favor verificar o campo cidade para a Pessoa Física/Jurídica\.”\.

Tamanho: 255

RN22

__complemento__

__Regra p/ tag <complemento> </complemento> __Tag relacionada a Identificação do complemento do endereço do prestador\. 

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 14 da SAFX04\) referente ao prestador cadastrado na nota fiscal\.

Tamanho: 100

RN23

__logradouro__

__Regra p/ tag <Logradouro> </Logradouro> __Tag relacionada a identificação do endereço do prestador\. 

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 12 da SAFX04\) referente ao prestador cadastrado na nota fiscal\.

Tamanho: 255

RN24

__Numero__

__Regra p/ tag <numero> </numero>__

Identifica o número do endereço do prestador\. 

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 13 da SAFX04\) referente ao prestador cadastrado na nota fiscal\.

Tamanho: 50

RN25

__pais__

__Regra p/ tag <Pais> </Pais> __Tag relacionada a identificação do País do Prestador\. 

Preencher com o campo DESCRICAO da tabela PAIS referente COD\_PAIS \(campo 21 da SAFX04\) do prestador cadastrado na nota fiscal\.

__Campo obrigatório__

__Tratamento: __O campo __<Pais> do Prestador é de preenchimento obrigatório, se não estiver preenchido__, exibir uma mensagem no log: “O campo __<Pais> do Prestador __precisa estar preenchido__,__ favor verificar o campo Pais para a Pessoa Física/Jurídica\.”\.

Tamanho: 200

RN26

__uf__

__Regra p/ tag <Uf> </Uf> __Tag relacionada a identificação da Unidade Federativa do Prestador\. 

Preencher com o campo UF da tabela X04\_PESSOA\_FIS\_JUR \(campo 19 da SAFX04\) referente ao prestador cadastrado na nota fiscal\.

Obs: Quando o local da Prestação for realizado em OUTRO PAÍS colocar a UF como EX\.

__Campo obrigatório__

__Tratamento: __O campo __<Uf> do Prestador é de preenchimento obrigatório, se não estiver preenchido__, exibir uma mensagem no log: “O campo __<Uf> do Prestador __precisa estar preenchido__,__ favor verificar o campo UF para a Pessoa Física/Jurídica\.”\.

Tamanho: 2

RN27

__Regra para tag </dadosServico> __Tag relacionada ao fechamento da identificação do prestador do serviço com o texto fixo:__</ dadosServico>\.__

TAG obrigatória\.

RN28

__Regra para tag <dadosTomador> __Tag relacionada à abertura da identificação do tomador do serviço com o texto fixo: __<dadosTomador>\.__

TAG obrigatória\.

RN29

__Bairro __

__Regra p/ tag <Bairro> </Bairro> __Tag relacionada a identificação do bairro do endereço do Tomador\. 

Preencher com o campo BAIRRO da tabela __ESTABELECIMENTO__ referente ao tomador cadastrado na nota fiscal\.

__Campo obrigatório__

- __Tratamento: __Se o campo __<Bairro> não estiver preenchido__, exibir uma mensagem no log: “O campo __<Bairro> __precisa estar preenchido__,__ favor verificar”\.

Tamanho: 100

RN30

__Cep __

__Regra p/ tag <Cep> </Cep> __Tag relacionada a identificação do CEP do Tomador\. 

Identifica o CEP da localidade do tomador\. Preencher com a informação do campo CEP __\(campo 20\)__ da tabela __ESTABELECIMENTO\.__

Formato: 99999\-999

__Campo obrigatório__

- __Tratamento: __Se o campo __<Cep> não estiver preenchido__, exibir uma mensagem no log: “O campo __<Cep> __precisa estar preenchido__,__ favor verificar”\.

Tipo: Numérico

Tamanho: 9

RN31

__Cidade __

__Regra p/ tag <Cidade> </Cidade> __Tag relacionada a identificação da cidade do Tomador\. 

Preencher com o campo CIDADE da tabela __ESTABELECIMENTO__ referente ao tomador cadastrado na nota fiscal\.

__Campo obrigatório__

__Tratamento: __O campo __<cidade> do Tomador é de preenchimento obrigatório, se não estiver preenchido__, exibir uma mensagem no log: “O campo __<cidade> do Tomador __precisa estar preenchido__,__ favor verificar”\.

Tamanho: 255

RN32

__Complemento __

__Regra p/ tag <Complemento> </Complemento> __Tag relacionada a identificação do complemento do endereço do Tomador\. 

Identifica o complemento do endereço do Tomador\. Preencher com o campo __COMPL\_ENDERECO__ da tabela __ESTABELECIMENTO__

Tamanho: 100

RN33

__Documento CNPJ ou CPF__

__Regra p/ tag <documento> </documento> __Tag relacionada à informação do CPF ou CNPJ do Tomador de serviço fixo:__ </documento>  __TAG obrigatória\.

Recuperar a informação do campo CGC da tabela __ESTABELECIMENTO__ 

Deve conter 11 posições \(para CPF\) ou 14 posições \(para CNPJ\)

Campo obrigatório

Tamanho: 14

RN34

__email  __

__Regra p/ tag <email> </email> __Tag relacionada a identificação do e\-mail do Tomador\. 

Preencher com o campo E\_MAIL da tabela __ESTABELECIMENTO__ referente o tomador cadastrado na nota fiscal\.

Tamanho: 255

RN35

__Ie __

__Regra p/ tag <ie> </ie> __Tag relacionada a identificação da Inscrição Estadual do Tomador

Preencher com o campo __INSCRICAO\_ESTADUAL__ da tabela __REGISTRO\_ESTADUAL__ referente ao campo COD\_ESTAB da tabela __ESTABELECIMENTO__, caso contrário preencher com brancos

Tamanho: 30

RN36

__Logradouro __

__Regra p/ tag <Logradouro> </Logradouro> __Tag relacionada a identificação do endereço do Tomador\. 

Identifica o tipo e nome do logradouro do Tomador\. Preencher com o campo __TP__\___LOGRADOURO__ __\+__ __ENDERECO__ da tabela __ESTABELECIMENTO__

__Campo obrigatório__

- __Tratamento: __Se o campo __<Logradouro> não estiver preenchido__, exibir uma mensagem no log: “O campo __<Logradouro> __precisa estar preenchido__,__ favor verificar”\.

Tamanho: 255

RN37

__nomeTomador __

__Regra p/ tag <nomeTomador> </nomeTomador> __Tag relacionada a identificação da razão social do tomador\. 

Preencher com o campo RAZAO\_SOCIAL da tabela __ESTABELECIMENTO__

TAG obrigatória\.

__Campo obrigatório__

- __Tratamento: __Se o campo __<nomeTomador> não estiver preenchido__, exibir uma mensagem no log: “O campo __<nomeTomador> __precisa estar preenchido__,__ favor verificar”\.

Tamanho: 255

RN38

__Numero __

__Regra p/ tag <Numero> </Numero> __Tag relacionada a identificação do número do endereço do tomador\. 

Identifica o número do endereço do Tomador\. Preencher com o campo __NUM\_ENDERECO__ da tabela __ESTABELECIMENTO__

Campo obrigatório

__Campo obrigatório__

- __Tratamento: __Se o campo __<Numero> não estiver preenchido__, exibir uma mensagem no log: “O campo __<Numero> __precisa estar preenchido__,__ favor verificar”\.

Tamanho: 50

RN39

__País __

__Regra p/ tag <Pais> </Pais> __Tag relacionada a identificação do País do Tomador\. 

Colocar a identificação do país como fixo “BRASIL”

Tamanho: 200

RN40

__tipoDoc  J ou F  __

__Regra p/ tag <tipodoc> </tipoDoc> __Tag relacionada ao Tipo do Documento do Tomador do Serviço

__Tratamento:__

Se o campo CGC da tabela __ESTABELECIMENTO__ for menor ou igual a 11 posições, a TAG deverá ser preenchida com __“F”\.__

Se o campo CGC da tabela __ESTABELECIMENTO__ for maior que 11 posições, a TAG deverá ser preenchida com __“J”\.__

__Campo obrigatório__

Tamanho: 1

RN41

__Uf __

__Regra p/ tag <Uf> </Uf> __Tag relacionada a identificação da Unidade Federativa do Tomador\. 

Preencher com o campo COD\_ESTADO da tabela ESTADO referente ao campo IDENT\_ESTADO da tabela __ESTABELECIMENTO__\.

Campo obrigatório

__Campo obrigatório__

- __Tratamento: __Se o campo __<Uf> do Tomador não estiver preenchido__, exibir uma mensagem no log: “O campo __<Uf> do tomador __precisa estar preenchido__,__ favor verificar”\.

Tamanho: 2

RN42

__Regra para tag </dadosTomador> __Tag relacionada ao fechamento da identificação do tomador do serviço com o texto fixo: __</dadosTomador>\.__

TAG obrigatória\.

RN43

__Regra para tag <detalheServico> __Tag relacionada a abertura aos dados do serviço com o texto fixo: __<detalheServico>\.__

RN44

__Cofins__

__Regra para o campo <cofins> da TAG </cofins> __Tag relacionada a identificação do valor da COFINS

Preencher com o somatório do campo __VLR\_COFINS\_RETIDO__ da tabela DWT\_ITENS\_SERV __\(Campo 51 da SAFX09\)\.__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <Cofins> estiver com o tamanho acima do máximo permitido \(16 posições\), exibir uma mensagem no log: “O campo <Cofins> está com o tamanho acima do permitido, favor verificar”\.
- Se o campo não possuir valor, preencher com zeros, conforme exemplo do XML\.

 

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

__Campo obrigatório__

- __Tratamento: __Se o campo __<cofins> não estiver preenchido__, exibir uma mensagem no log: “O campo __<cofins> __precisa estar preenchido__,__ favor verificar”\.

Tipo: Numérico

Tamanho: 16

RN45

__csll__

__Regra para o campo <csll> da TAG </csll> __Tag relacionada a identificação do valor da CSLL

Preencher com o somatório do campo __VLR\_CSLL__ da tabela DWT\_ITENS\_SERV __\(Campo 45 da SAFX09\)__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <Csll> estiver com o tamanho acima do máximo permitido \(16 posições\), exibir uma mensagem no log: “O campo <Csll> está com o tamanho acima do permitido, favor verificar”\.
- Se o campo não possuir valor, preencher com zeros, conforme exemplo do XML\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

__Campo obrigatório__

- __Tratamento: __Se o campo __<csll> não estiver preenchido__, exibir uma mensagem no log: “O campo __<csll> __precisa estar preenchido__,__ favor verificar”\.

Tipo: Numérico

Tamanho: 16

RN46

__Deducaomaterial  __

__Regra para o campo <deducaoMaterial> da TAG </deducaoMaterial> __Valor das Deduções de Material

Nesse campo será informado o valor das deduções\.

Preencher com o conteúdo do campo __VLR\_DEDUCAO\_ISS__ da tabela DWT\_ITENS\_SERV__ \(campo 59 da SAFX09\)\.__

Se o campo não possuir valor, preencher com zeros, conforme exemplo do XML\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

Tipo: Numérico

Tamanho: 16

RN47

__descontoIncondicional __

__Regra para o campo <descontoIncondicional> da TAG </descontoIncondicional>__

Preencher com o somatório do campo __VLR\_DESCONTO __da tabela DWT\_ITENS\_SERV __\(Campo 21 da SAFX09\)__

__Tratamento:__

- Se o campo <Inss> estiver com o tamanho acima do máximo permitido \(16 posições\), exibir uma mensagem no log: “O campo __<descontoIncondicional> __está com o tamanho acima do permitido, favor verificar”\.
- Se o campo não possuir valor, preencher com zeros, conforme exemplo do XML\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

Tipo: Numérico

Tamanho: 16

RN48

__inss__

__Regra para o campo <inss> da TAG </inss> __Valor do INSS \(Imposto de Renda fornecido ao Instituto Nacional de Seguridade Social\)

Preencher com o somatório do campo __VLR\_INSS\_RETIDO__ da tabela DWT\_ITENS\_SERV __\(Campo 77 da SAFX09\)\.__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <Inss> estiver com o tamanho acima do máximo permitido \(16 posições\), exibir uma mensagem no log: “O campo <inss> está com o tamanho acima do permitido, favor verificar”\.
- Se o campo não possuir valor, preencher com zeros, conforme exemplo do XML\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

Campo obrigatório

- __Tratamento: __Se o campo __<inss> não estiver preenchido__, exibir uma mensagem no log: “O campo __<inss> __precisa estar preenchido__,__ favor verificar”\.

Tipo: Numérico

Tamanho: 16 

RN49

__ir__

__Regra para o campo <Ir> da TAG </Ir> __Tag relacionada a identificação do valor do IR retido

Preencher com o somatório do campo __VLR\_TRIBUTO\_IR__ da tabela DWT\_ITENS\_SERV 

__Tratamento:__

- Se o campo <ir> estiver com o tamanho acima do máximo permitido \(16 posições\), exibir uma mensagem no log: “O campo <ir> está com o tamanho acima do permitido, favor verificar”\.
- Se o campo não possuir valor, preencher com zeros, conforme exemplo do XML\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

Campo obrigatório

- __Tratamento: __Se o campo __<ir> não estiver preenchido__, exibir uma mensagem no log: “O campo __<ir> __precisa estar preenchido__,__ favor verificar”\.

Tipo: Numérico

Tamanho: 16

RN50

__issretido__

__Regra para o campo <issRetido> da TAG </issRetido> __Tag relacionada a identificação do ISS foi retido ou não\.

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\.

Preencher com:

__“1” \- Sim\.__

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado __OU __
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado __OU__
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Senão, preencher com:

__“0” \- Não\.__

Formato: 9 \(1\-Sim ou 0\-Não\)

__Campo obrigatório__

- __Tratamento: __Se o campo __<issRetido> não estiver preenchido__, exibir uma mensagem no log: “O campo __<issRetido> __precisa estar preenchido__,__ favor verificar”\.

Tipo: Numérico

Tamanho: 1

RN51

__Regra para tag <item> __Tag relacionada aos dados do serviço com o texto fixo: __<item>\.__

RN52

__aliquota__

__Regra para o campo <aliquota> da TAG </aliquota>__Tag relacionada a alíquota do serviço\. 

Preencher com o campo __ALIQ\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV\.__

__Tratamento:__ 

Se o campo ALIQ\_TRIBUTO\_ISS for igual a zero\.

Preencher com o campo __VLR\_ALIQ\_SERVICO__ da tabela __x2098\_ALIQ\_SERVICO__, para o serviço cadastrado na nota e utilizando o campo __COD\_MUNIC\_ISS__ da tabela __ESTABELECIMENTO__\.

Formato: 9\.99 – Exemplo: 2,00 = 2\.00

Tipo: Numérico

Tamanho:16

RN53

__codigo __

__Regra para o campo <codigo> da TAG </codigo> __Tag Relacionada ao código de atividade do serviço com o texto fixo:__ </codigo>__

Identifica o Grupo do Código de Atividade do Serviço\. 

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\.

__Tratamento:__

Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, deverá ser gravado com 0000 \(zeros\) e emitida a mensagem de log: O código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal não está preenchido, favor verificar\.

Formato: 9999

Tipo: Numérico

__Campo obrigatório__

- __Tratamento: __Se o campo __<Codigo> não estiver preenchido__, exibir uma mensagem no log: “O campo __<Codigo> __precisa estar preenchido__,__ favor verificar”\.

Tamanho: 16

RN54

__descricao__

__Regra para o campo <descricao> da TAG </descricao >  __Tag relacionada a identificação do campo descrição\.

Preencher com o campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao\(s\) serviço\(s\) cadastrado\(s\) no item da nota fiscal\.

Formato: XXXXXXXXXXXXXXXXXX\(\.\.\.\)

Tipo: Alfanumérico

__Campo obrigatório__

- __Tratamento: __Se o campo __<descricao> não estiver preenchido__, exibir uma mensagem no log: “O campo __<descricao> __precisa estar preenchido__,__ favor verificar”\.

Tamanho: 500  

RN55

__valor__

__Regra para o campo <valor> da TAG </valor> __Tag relacionada ao campo que  identifica o valor do ISSQN\. 

Preencher com o campo __VLR\_TOT__ campo da SAFX09\.

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <Inss> estiver com o tamanho acima do máximo permitido \(16 posições\), exibir uma mensagem no log: “O campo __<valor> __está com o tamanho acima do permitido, favor verificar”\.
- Se o campo não possuir valor, preencher com zeros, conforme exemplo do XML\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

__Campo obrigatório__

- __Tratamento: __Se o campo __<valor> não estiver preenchido__, exibir uma mensagem no log: “O campo __<valor> __precisa estar preenchido__,__ favor verificar”\.

Tipo: Numérico

Tamanho: 16

RN56

__Regra para tag </item> __Tag relacionada aos dados do serviço com o texto fixo: __</item>\.__

RN57

__Obs:__

__Regra para o campo <obs> da TAG </obs> __Tag relacionada a identificação do campo observação

__Observacao __

Formato: XXXXXXXXX\.\.\.

Tipo: Alfanumérico

Esse campo deverá ser gerado em branco, pois não é obrigatório

Tamanho: 500

RN58

__pisPasep __

__Regra para o campo <pisPasep> da TAG </pisPasep> __Valor do PIS/PASEP \(Programa de Integração Social \(PIS\) Programa de Formação do Patrimônio do Servidor Público\(PASEP\)\)

Preencher com o somatório do campo __VLR\_PIS\_RETIDO__ da tabela DWT\_ITENS\_SERV\. __\(Campo 79 da SAFX09\)\.__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <pisPasep> estiver com o tamanho acima do máximo permitido \(16 posições\), exibir uma mensagem no log: “O campo <pisPasep> está com o tamanho acima do permitido, favor verificar”\.
- Se o campo não possuir valor, preencher com zeros, conforme exemplo do layout\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

__Campo obrigatório__

- __Tratamento: __Se o campo __<Cidade> não estiver preenchido__, exibir uma mensagem no log: “O campo __<Cidade> __precisa estar preenchido__,__ favor verificar”\.

Tipo: Numérico

Tamanho: 16

RN59

__Regra para tag </detalheServico> __Tag relacionada ao fechamento dos dados do serviço com o texto fixo: __</detalheServico>\.__

RN60

__Regra para tag </notaFiscal> __Tag relacionada ao fechamento da formatação do arquivo e que deve receber as informações das notas tomadas declaradas com o texto fixo __</notaFiscal>__

RN61

__Regra para tag </nfe> __Tag relacionada ao fechamento das informações da notas fiscal

TAG obrigatória\.

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN


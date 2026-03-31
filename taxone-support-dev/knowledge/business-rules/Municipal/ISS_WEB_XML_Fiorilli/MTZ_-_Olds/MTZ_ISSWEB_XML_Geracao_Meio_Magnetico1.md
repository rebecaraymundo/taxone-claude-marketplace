# MTZ_ISSWEB_XML_Geracao_Meio_Magnetico1

- **Fonte:** MTZ_ISSWEB_XML_Geracao_Meio_Magnetico1.docx
- **Modificado:** 2023-06-30
- **Tamanho:** 186 KB

---

### ISSWeb XML – Geração do Meio Magnético – V01

### Controle das Alterações

__MFS__

__Data__

__Nome__

__Descrição__

MFS\-8205

11/01/2017

Julyana Perrucini

Este documento tem como objetivo a inclusão no validador ISSWeb XML para o município de __Laranjal Paulista/ SP\.__

MFS\-11003

08/06/2017

Julyana Perrucini

Este documento tem como objetivo a inclusão no validador ISSWeb XML para o município de __Cajobi/SP\.__

MFS\-11003

08/06/2017

Julyana Perrucini

Este documento tem como objetivo a inclusão no validador ISSWeb XML para do municípios __Bariri/ SP\.__

MFS\-17564

18/04/2017

João Henrique

Este documento tem como objetivo a inclusão no validador ISSWeb XML para do município __Cedral/SP\.__

MFS\-17564

18/04/2017

João Henrique

Este documento tem como objetivo a inclusão no validador ISSWeb XML para dos municípios __Guaíra/ SP__\.

MFS\-19916

08/08/2018

João Henrique

Este documento tem como objetivo a inclusão no validador ISSWeb XML para dos municípios __Assis/ SP\.__

MFS\-20118

22/08/2018

Andréa Rocha

Este documento tem como objetivo a inclusão no validador ISSWeb XML para dos municípios __Garça/SP\.__

MFS\-20433

05/09/2018

João Henrique

Este documento tem como objetivo a inclusão no validador ISSWeb XML para dos municípios __Avaré/SP\.__

MFS\-21664

31/102018

João Henrique

Este documento tem como objetivo a inclusão no validador ISSWeb XML para do município __Nova Alvorada do Sul/MS\.__

MFS\-22743

26/12/2018

Julyana Perrucini

Este documento tem como objetivo a inclusão no validador ISSWeb XML para do município __Vera Cruz/ BA__\.

MFS\-23335

24/01/2019

João Henrique

Este documento tem como objetivo a inclusão no validador ISSWeb XML para do município Corumbá/MS\.

MFS\-23555

21/02/2019

Andréa Rocha

Este documento tem como objetivo a inclusão no validador ISSWeb XML para do município __Altinópolis/SP\.__

MFS\-24242

20/03/2019

Andréa Rocha

Este documento tem como objetivo a inclusão no validador ISSWeb XML para do município __Ibaté/SP\.__

MFS\-36689

23/06/2020

Andréa Rocha

Este documento tem como objetivo a inclusão do município __Pirajuí/SP__ e da geração para os prestadores, anteriormente só era gerado o arquivo dos tomadores\.

MFS\-42965

15/10/2020

Andréa Rocha

Este documento tem como objetivo alterar a regra do campo Série para o município __Pirajuí/SP\.__

MFS\-53878

26/05/2021

Elisabete Costa

Este documento tem como objetivo a inclusão no validador ISSWeb XML para do __município José Bonifácio/SP\.__

MFS\-62248

14/06/2021

Elisabete Costa

Este documento tem como objetivo a inclusão no validador ISSWeb XML para do município __Santa Rita do Passa Quatro/SP\.__

MFS\-64386

06/07/2021

Alessandra Navatta

Este documento tem como objetivo a inclusão no validador ISSWeb XML para o município __Três Lagoas/MS__\. 

__Obs\.__ Na demanda só foi disponibilizado o layout de serviços tomados, diante disso, considerar o layout de serviços prestados, conforme o __layout de Pirajuí\-SP__

MFS\-67742

23/06/2021

Rogério Ohashi

Este documento tem como objetivo alterar a recuperação das informações de Serviços Tomados do município de __José Bonifácio/SP__, passando a desconsiderar as Notas Fiscais de Prestadores de Serviços do mesmo município\. 

MFS\-77339

18/02/2022

Rogério Ohashi

Este documento tem como objetivo alterar a recuperação das informações de Serviços Tomados do município de __Altinópolis/SP__, passando a desconsiderar as Notas Fiscais de Prestadores de Serviços do mesmo município\.

MFS\-88149

29/06/2022

Elisabete Costa

Este documento tem como objetivo a inclusão de Serviços Tomados e Prestados para o município de __Araçoiaba da Serra/SP__

MFS\-88150

29/06/2022

Elisabete Costa

Este documento tem como objetivo a inclusão de Serviços Tomados para o município de __Paranaíba/MS__

MFS\-88163

29/06/2022

Elisabete Costa

Este documento tem como objetivo a inclusão de Serviços Tomados para o município de __Catanduva/SP__

MFS\-89608

29/06/2022

Elisabete Costa

Este documento tem como objetivo a inclusão de Serviços Tomados para o município de __Fernandópolis/MS__

MFS\-90233

08/09/2022

Elisabete Costa

Este documento tem como objetivo alterar o campo __“Referência”__, para ser utilizado o mês e o ano da Data de emissão, quando o parâmetro de  __“Quebrar Arquivos por Data de Emissão”__ estiver marcado\.

MFS\-511320

16/02/2023

Elisabete Costa

Este documento tem como objetivo a inclusão de Serviços Tomados para o município de __JAÚ/SP__

MFS\-526807

06/04/2023

Elisabete Costa

Este documento tem como objetivo a inclusão de Serviços Tomados para o município de __SANTO ANTÔNIO DE POSSE/SP__

### REGRAS DE NEGÓCIO 

__CÓD__

__DESCRIÇÃO__

__MFS__

__RN01__

__Estrutura de Menus do Módulo ISSWEB XML:__

Deverão ser criados os seguintes menu e sub\-menus no módulo ISS WEB XML:

- Arquivo
- Obrigações
	- Geração do Meio Magnético
	- Arquivo de Entradas de Serviços \(Const\.Civi l/Utilities /Telecom\)
- Janela
- Ajuda 

MFS\-8205

__RN02__

__Regra de Criação do Nome do Arquivo:__

__SERVIÇOS PRESTADOS:__

__       ST\_ISSWEB\_MUNICIPIO\_DDMMAAAA\.XML__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __ST\_ISSWEB__: representa a obrigação que está sendo gerada\. 

       __\.XML__: extensão do arquivo\.

*Exemplo:* ST\_ISSWEB\___Nome do Município__\_01012010\.xml

__SERVIÇOS TOMADOS:__

Quando o parâmetro __“Quebrar Arquivos por Data de Emissão”__ estiver marcado, deve ser realizada a seguinte verificação: 

- Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. 
- Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__ST\_ISSWEB\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.XML__, onde:

__               ST\_ISSWEB__: representa a obrigação que está sendo gerada\.    

__               MUNICIPIO__: representa o município que está sendo gerado\.   

               __DDMMAAAA__: representa a data inicial da geração\.   

__               MMAAAA:__ mês da competência referente à nota gerada

               __\.XML__: extensão do arquivo\.

Ex: ST\_ISSWEB\___Nome do Município__\_01012014\_122013\.xml

__Obs\.:__ Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. 

Estas notas com competência distintas não devem estar no arquivo normal\.__       __

__SP\_ISSWEB\_MUNICIPIO\_DDMMAAAA\.XML__, onde:

       __DDMMAAAA__: representa a data inicial da geração

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __SP\_ISSWEB__: representa a obrigação que está sendo gerada\. 

       __\.XML__: extensão do arquivo\.

*Exemplo:* SP\_ISSWEB\___Nome do Município__\_01012010\.xml

__*Observação:* Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.__

MFS\-8205

MFS\-36689

__RN03__

__Regra p/ Tela da Geração do Meio Magnético:__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Gerar Serviços Tomados:__ deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Gerar Serviços Prestados__: deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\) 

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

MFS\-8205

MFS\-36689

__RN04__

__Regra p/ Geração do Arquivo Magnético:__

- Campos de valor que não houver preenchimento, gravar “0”;
- Campos numéricos que não houver preenchimento, gravar “0”;
- Campos alfanuméricos que não houver preenchimento, gravar branco\.

MFS\-8205

__RN05__

__SERVIÇOS TOMADOS__

__Regra P/ Recuperar Notas Fiscais de Serviços Tomados – REGRA GERAL:__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)

__*Observação:*__* *Quando a nota fiscal não tiver itens não deve ser considerada\.

MFS\-8205

MFS\-67742

MFS\-64386

MFS\-77339

__RN05\.a__

__Regra P/ Recuperar Notas Fiscais de Serviços Tomados – ESPECÍFICA:__

__Desconsiderar as NFS\-e emitidas no próprio município__ __– José Bonifácio/SP, Três Lagoas/MS, Altinópolis/SP, Araçoiaba da Serra/SP, Paranaíba/MS , Catanduva/SP, Fernandópolis, Jaú, Santo Antônio de Posse__

     

__     SE __o campo COD\_MUNICIPIO da tabela ESTABELECIMENTO for igual ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR relacionada ao documento fiscal;

__       E  __o campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S”, referente ao tipo de documento da nota fiscal\)\.__ __

__                      __

__NÃO__ gerar as Notas Fiscais de Serviço no arquivo Meio Magnético\.

MFS\-67742

MFS\-77339

__MFS\-88149__

__MFS\-88150__

__MFS\-88163__

__MFS\-89608__

__MFS\-511320__

__MFS\-526807__

__RN06__

__Estrutura do Arquivo:__

<?xml version="1\.0" encoding="UTF\-8" standalone="yes"?>

<Declaracao>

    <Tomador>

        <CodEmpresa> </CodEmpresa>

        <CpfCnpj>

            <Cnpj> </Cnpj>

        </CpfCnpj>

        <InscricaoMunicipal> </InscricaoMunicipal>

    </Tomador>

    <Referencia> </Referencia>

    <LoteNotaFiscalTomador>

        <NotaFiscalTomador>

            <InfDeclaracaoPrestacaoServicoTomador>

                <DadosNotaFiscal>

                    <IdentificacaoNotaFiscal>

                        <Numero> </Numero>

                        <Especie> </Especie>

                        <Serie> </Serie>

                    </IdentificacaoNotaFiscal>

                    <DataEmissao> </DataEmissao>

                </DadosNotaFiscal>

                <Servico>

                    <Aliquotas>

                        <Aliquota> </Aliquota>

                        <AliquotaCofins> </AliquotaCofins>

                        <AliquotaCsll> </AliquotaCsll>

                        <AliquotaInss> </AliquotaInss>

                        <AliquotaIr> </AliquotaIr>

                        <AliquotaPis> </AliquotaPis>

                    </Aliquotas>

                    <IssRetido> </IssRetido>

                    <CodigoMunicipio> </CodigoMunicipio>

                    <CodigoPais> </CodigoPais>

                    <CodAtividade> </CodAtividade>

                    <CodAtividadeDesdobro> </CodAtividadeDesdobro>

                </Servico>

                <Prestador>

                    <IdentificacaoPrestador>

                        <CodEmpresa> </CodEmpresa>

                        <CpfCnpj>

                            <Cnpj> </Cnpj>

                        </CpfCnpj>

                        <InscricaoMunicipal> </InscricaoMunicipal>

                    </IdentificacaoPrestador>

                    <RazaoSocial> </RazaoSocial>

                    <NomeFantasia> </NomeFantasia>

                    <RgInscre> </RgInscre>

                    <Endereco>

                        <Endereco> </Endereco>

                        <Numero> </Numero>

                        <Complemento> </Complemento>

                        <Bairro> </Bairro>

                        <CodigoMunicipio> </CodigoMunicipio>

                        <Uf> </Uf>

                        <CodigoPais> </CodigoPais>

                        <Cep> </Cep>

                    </Endereco>

                    <Contato>

                        <Telefone> </Telefone>

                        <Email> </Email>

                    </Contato>

                    <ExigibilidadeISS> </ExigibilidadeISS>

                    <NumeroProcesso> </NumeroProcesso>

                    <RegimeEspecialTributacao>1 RegimeEspecialTributacao>

                    <OptanteSimplesNacional> </OptanteSimplesNacional>

                    <IncentivoFiscal> </IncentivoFiscal>

                </Prestador>

                <ItensNotas>

                    <item>

                        <DescriNfi> </DescriNfi>

                        <MedidaNfi> </MedidaNfi>

                        <QuantidadeNfi> </QuantidadeNfi>

                        <VlrUnitarioNfi> </VlrUnitarioNfi>

                        <DesccondicionalNfi> </DesccondicionalNfi>

                        <DescincondicionalNfi> </DescincondicionalNfi>

                        <DeducaobaseNfi> </DeducaobaseNfi>

                    </item>

                </ItensNotas>

            </InfDeclaracaoPrestacaoServicoTomador>

        </NotaFiscalTomador>

    </LoteNotaFiscalTomador>

    <QuantidadeNotas> </QuantidadeNotas>

 </Declaracao>

MFS\-8205

__RN07__

__Regra p/ o Cabeçalho do Arquivo:__

Preencher com o tag <?xml version="1\.0" encoding="UTF\-8" standalone="yes"?>

__TAG obrigatória\.__

MFS\-8205

__RN08__

__Regra para tag <Declaracao> __

Tag relacionada à abertura da formatação do arquivo e que deve receber as informações das notas tomadas declaradas com o texto fixo: __<Declaracao>\.__

__TAG obrigatória\.__

MFS\-8205

__RN09__

__Regra para tag <Tomador> __

Tag relacionada à abertura dos dados do tomador do serviço com o texto fixo: __<Tomador>\.__

__TAG obrigatória\.__

MFS\-8205

__RN10__

__Regra p/ tag <CodEmpresa> </CodEmpresa>__

Identifica o código da Prefeitura\. 

Preencher com o conteúdo fixo: “1”, sem necessidade de espaços ou zeros para complementar o tamanho do campo\.

__Campo obrigatório__

Formato: 99999999999999

Tipo: Numérico

Tamanho: 10

MFS\-8205

__RN11__

__Regra p/ tag <CpfCnpj> __

Tag relacionada à abertura dos dados de cadastro do tomador do serviço com o texto fixo: __<CpfCnpj>\.__

__TAG obrigatória\.__

MFS\-8205

__RN12__

__Regra p/ tag <Cnpj> </Cnpj>__

Identifica o CNPJ do tomador\. 

Preencher com o campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento que está sendo gerado o arquivo magnético\.

__Campo obrigatório__

Formato: 99999999999999

Tipo: Numérico

Tamanho: 14

MFS\-8205

__RN13__

__Regra p/ tag </CpfCnpj> __

Tag relacionada ao encerramento dos dados de cadastro do tomador do serviço com o texto fixo: __</CpfCnpj>\.__

__TAG obrigatória\.__

MFS\-8205

__RN14__

__Regra p/ tag <InscricaoMunicipal> </InscricaoMunicipal>__

Identifica a Inscrição Municipal do tomador\. 

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO referente ao estabelecimento que está sendo gerado o arquivo magnético, sem necessidade de espaços ou zeros para complementar o tamanho do campo, pode permitir pontuação\.

__Tratamento:__

- Se o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO não estiver preenchido, emitir uma mensagem padrão de log\.

__Campo obrigatório__

Formato: XXXXXXXXXXXXXXX

Tipo: Alfanumérico

Tamanho: 15

MFS\-8205

__RN15__

__Regra para tag </Tomador> __

Tag relacionada ao encerramento dos dados do tomador do serviço com o texto fixo: __</Tomador>\.__

__TAG obrigatória\.__

MFS\-8205

__RN16__

__Regra p/ tag <Referencia> </Referencia>__

Identifica o mês/ ano das notas fiscais\. 

Preencher com o mês e o ano do conteúdo do campo “Data Inicial” da tela de geração do meio magnético\.

__Tratamento: __Geração arquivo único \(Serviço Tomado\)

__Se __o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado

      __Preencher__ com o mês e ano do campo Data de Emissão da tabela DWT\_DOCTO\_FISCAL 

__Campo obrigatório__

Formato: MM/AAAA

Tipo: Data

MFS\-8205

MFS\-90233

__RN17__

__Regra para tag <LoteNotaFiscalTomador> __

Tag relacionada à abertura dos dados da nota fiscal do tomador do serviço com o texto fixo: __<LoteNotaFiscalTomador>\.__

__TAG obrigatória\.__

MFS\-8205

__RN18__

__Regra para tag <NotaFiscalTomador> __

Tag relacionada à abertura das informações da nota fiscal do tomador do serviço com o texto fixo: __<NotaFiscalTomador>\.__

__TAG obrigatória\.__

MFS\-8205

__RN19__

__Regra para tag <InfDeclaracaoPrestacaoServicoTomador> __

Tag relacionada à abertura das informações da nota fiscal do tomador do serviço com o texto fixo: __<InfDeclaracaoPrestacaoServicoTomador>\.__

__TAG obrigatória\.__

MFS\-8205

__RN20__

__Regra para tag <DadosNotaFiscal> __

Tag relacionada à abertura das informações da nota fiscal do prestador do serviço com o texto fixo: __<DadosNotaFiscal>\.__

__TAG obrigatória\.__

MFS\-36689

__RN21__

__Regra para tag <IdentificacaoNotaFiscal> __

Tag relacionada à abertura da identificação da nota fiscal do prestador do serviço com o texto fixo:__ <IdentificacaoNotaFiscal>\.__

__TAG obrigatória\.__

MFS\-36689

__RN22__

__Regra p/ tag <Numero> </Numero>__

Identifica o Número da Nota fiscal\. 

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\), sem necessidade de espaços ou zeros para complementar o tamanho do campo\.

__Campo obrigatório__

Formato: 99999999999999999999

Tipo: Numérico

Tamanho: 20

MFS\-36689

__RN23__

__Regra p/ tag <Especie> </Especie>  \(Tipo de Documento\) \-  REGRA GERAL__

Identifica a Espécie da Nota fiscal conforme cadastrado\. 

Preencher com o campo Tipo de Documento da tela de parametrização Parâmetros para Município – Tipo Docto Msaf x Tipo Docto – __TFIX84__, associado ao tipo de documento informado na nota fiscal \(campo COD\_DOCTO da DWT\_ITENS\_SERV\)\.

__Tratamento:__

Senão:

Preencher com o __conteúdo fixo: “1”,__ sem necessidade de espaços, pontos ou zeros para complementar o tamanho do campo\.

__*Obs:*__ Estamos colocando como fixo 1 conforme determina a Prefeitura no que se refere a Prestação de Serviço\.

__Campo obrigatório__

Formato: 99999999999999999999

Tipo: Numérico

Tamanho: 20

MFS\-8205

MFS\-23335

__RN23\.a__

__Regra p/ tag <Especie> </Especie>   \(Tipo de Documento\) \-   ESPECÍFICA __

__Obs:__ Essa regra será aplicada para notas recebidas\.

Para os municípios:__ Cedral/SP, Guaíra/SP, Garça/SP, Altinópolis/SP, Avaré/SP, Ibaté/SP, Araçoiaba da Serra/SP, Paranaíba/MS, Catanduva/SP, Fernandópolis/SP, Jaú/SP, Santo Antônio de Posse__

Identifica a Espécie da Nota fiscal conforme cadastrado\. 

Preencher com o campo Espécie da tela de parametrização __Parâmetros para Município – Tipo Docto Msaf x Espécie__ carregada na __TFIX84__ \(Cadastro dos Tipos de Documento das Obrigações \- PRT\_TP\_DOCTO\_OBRIG\)\.

__Tratamento:__

- Se não existir a parametrização da espécie informada, emitir mensagem padrão de log\.

__Campo obrigatório__

Formato: 99999999999999999999

Tipo: Numérico

Tamanho: 20

MFS\-17564

MFS\-20118

MFS\-20433

MFS\-23555

MFS\-24242

__MFS\-88149__

__MFS\-88150__

__MFS\-88163__

__MFS\-89608__

__MFS\-511320__

__MFS\-526807__

__RN24__

__Regra p/ tag <Serie> </Serie>  \-  REGRA GERAL__

Identifica a Série da Nota fiscal conforme cadastrado\. 

Preencher com o campo Série da tela de parametrização __Parâmetros para Município – Série Msaf x Série__ – __TFIX83__, associado a série informada na nota fiscal \(campo SERIE\_DOCFIS da DWT\_ITENS\_SERV\)\.

__Tratamento:__

- Se não existir a parametrização da série informada, emitir mensagem padrão de log\.

__Campo obrigatório__

Formato: 99999999999999999999

Tipo: Numérico

Tamanho: 20

MFS\-11003

MFS\-17564

MFS\-20433

MFS\-23335

__MFS\-88149__

__MFS\-88150__

__MFS\-88163__

__MFS\-89608__

__MFS\-511320__

__MFS\-526807__

__RN24\.a__

__Regra p/ tag <Serie> </Serie>   \-   ESPECÍFICA__

Para os municípios:__ Laranjal Paulista/SP, Assis/SP, Nova Alvorada do Sul/MS, José Bonifácio/SP, Santa Rita do Passa Quatro/SP, Três Lagoas/MS\.__

Identifica a Série da Nota fiscal conforme parâmetro\. 

Preencher com o campo Série da tela de parametrização Parâmetros para Município – Série Msaf x Série – __TFIX83__, associado a série informada na nota fiscal \(campo SERIE\_DOCFIS da DWT\_ITENS\_SERV\)\.

__SENÃO:__

Preencher com:

__“2” \- Nota Fiscal Eletrônica\.__

- Se o campo código de modelo cadastrado na nota fiscal for igual a “55” __OU__ o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S” referente ao tipo de documento cadastrado na nota fiscal\.

Senão, preencher com:

__“1” \- Nota Avulsa\.__

__Tratamento:__

Se não existir a parametrização da série informada, emitir mensagem padrão de log\.

__Campo obrigatório__

Formato: 99999999999999999999

Tipo: Numérico

Tamanho: 20

MFS\-8205

MFS\-19916

MFS\-21664

MFS\-42965

MFS\-53878

MFS\-62248

MFS\-64386

__RN25__

__Regra para tag </IdentificacaoNotaFiscal> __

Tag relacionada ao encerramento da identificação da nota fiscal do tomador do serviço com o texto fixo: __</IdentificacaoNotaFiscal>\.__

__TAG obrigatória\.__

MFS\-8205

__RN26__

__Regra p/ tag <DataEmissao> </DataEmissao>__

Identifica a Data e Hora da emissão da nota\. 

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\+‘T’\+‘00:00:00’ \(campo 11 da SAX07\)\.

__Campo obrigatório__

Formato: AAAA\-MM\-DDTHH:mm:ss

Tipo: Data\-Hora

Tamanho: \-

MFS\-8205

__RN27__

__Regra para tag </DadosNotaFiscal> __

Tag relacionada ao encerramento das informações da nota fiscal do tomador do serviço com o texto fixo: __</DadosNotaFiscal>\.__

__TAG obrigatória\.__

MFS\-8205

__RN28__

__Regra para tag <Servico> __

Tag relacionada à abertura das informações do serviço da nota fiscal com o texto fixo: __<Servico>\.__

__TAG obrigatória\.__

MFS\-8205

__RN29__

__Regra para tag <Aliquotas> __

Tag relacionada à abertura das informações da alíquota do serviço da nota fiscal com o texto fixo: __<Aliquotas>\.__

__TAG obrigatória\.__

MFS\-8205

__RN30__

__Regra p/ tag <Aliquota> </Aliquota>__

Identifica a Alíquota ISS da Nota Fiscal\. 

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV \(campo 32 da SAFX09\)\.

__Tratamento:__

- Se o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV não estiver preenchido, emitir mensagem padrão de log\.

__Campo obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-8205

__RN31__

__Regra p/ tag <AliquotaCofins> </AliquotaCofins>__

Identifica a Alíquota da COFINS da Nota Fiscal\. 

Preencher com o campo VLR\_ALIQ\_COFINS da tabela DWT\_ITENS\_SERV \(campo 50 da SAFX09\)\.

__Campo não obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-8205

__RN32__

__Regra p/ tag <AliquotaCsll> </AliquotaCsll>__

Identifica a Alíquota da Csll da Nota Fiscal\. 

Preencher com o campo VLR\_ALIQ\_CSLL da tabela DWT\_ITENS\_SERV \(campo 44 da SAFX09\)\.

__Campo não obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-8205

__RN33__

__Regra p/ tag <AliquotaInss> </AliquotaInss>__

Identifica a Alíquota do INSS da Nota Fiscal\. 

Preencher com o campo VLR\_ALIQ\_INSS da tabela DWT\_ITENS\_SERV \(campo 78 da SAFX09\)\.

__Campo não obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-8205

__RN34__

__Regra p/ tag <AliquotaIr> </AliquotaIr>__

Identifica a Alíquota do IR da Nota Fiscal\. 

Preencher com o campo VLR\_ALIQ\_IR da tabela DWT\_ITENS\_SERV \(campo 30 da SAFX09\)\.

__Campo não obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-8205

__RN35__

__Regra p/ tag <AliquotaPis> </AliquotaPis>__

Identifica a Alíquota do PIS da Nota Fiscal\. 

Preencher com o campo VLR\_ALIQ\_PIS da tabela DWT\_ITENS\_SERV \(campo 47 da SAFX09\)\.

__Campo não obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-8205

__RN36__

__Regra para tag </Aliquotas> __

Tag relacionada ao encerramento das informações da alíquota do serviço da nota fiscal com o texto fixo: __</Aliquotas>\.__

__TAG obrigatória\.__

MFS\-8205

__RN37__

__Regra p/ tag <IssRetido> </IssRetido>__

Identifica se o ISS foi retido ou não pelo Tomador\. 

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo cod\_municipio da tabela ESTABELECIMENTO\)\.

Preencher com:

__“1” \- Sim\.__

- Verificar se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) está preenchido\. Se estiver preenchido, verificar se está preenchido com “1”; __OU__
- Verificar se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” \(campo 05 da SAFX2098\) para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO; __OU__
- Verificar se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV \(campo 58 da SAFX09\) está preenchido\. 

Senão, preencher com:

__“2” \- Não\.__

__Campo obrigatório__

Formato: 9 \(1\-Sim ou 2\-Não\)

Tipo: Numérico

Tamanho: 1

MFS\-8205

__RN38__

__Regra p/ tag <CodigoMunicipio> </CodigoMunicipio>__

Identifica o Código do Município \(IBGE\) do Tomador\. 

Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do Município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

__Campo não obrigatório__

Formato: 9999999

Tipo: Numérico

Tamanho: 7

MFS\-8205

__RN39__

__Regra p/ tag <CodigoPais> </CodigoPais>__

Identifica o Código do País \(BACEN\) do Tomador\. 

Preencher com o conteúdo fixo: “1058”\.

__Campo não obrigatório__

Formato: 9999

Tipo: Numérico

Tamanho: 4

MFS\-8205

__RN40__

__Regra p/ tag <CodAtividade> </CodAtividade>__

Identifica o Grupo do Código de Atividade do Serviço\. 

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal, mas considerar apenas as duas primeiras posições e completar com zeros à esquerda\. Exemplo: Lei 116 “0101” deverá ser preenchida como “000001”; Lei 116 “0107” deverá ser preenchida “000001”\.

__Tratamento:__

- Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, deverá ser gravado com 0 \(zero\) e emitida a mensagem de log: *“Erro: Favor preencher o código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”*\.

__Campo obrigatório__

Formato: 999999

Tipo: Numérico

Tamanho: 6

MFS\-8205

__RN41__

__Regra p/ tag <CodAtividadeDesdobro> </CodAtividadeDesdobro>__

Identifica o Desdobro da Atividade do Serviço\. 

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal, mas considerar apenas as duas últimas posições e completar com zeros à esquerda\. 

Exemplo: Lei 116 “0101” deverá ser preenchida como “0000001”; Lei 116 “0107” deverá ser preenchida “0000007”\.

__Tratamento:__

- Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, deverá ser gravado com 0 \(zero\) e emitida a mensagem de log: *“Erro: Favor preencher o código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”*\.

__Campo obrigatório__

Formato: 9999999

Tipo: Numérico

Tamanho: 7

MFS\-8205

__RN42__

__Regra para tag </Servico> __

Tag relacionada ao encerramento das informações do serviço da nota fiscal com o texto fixo: __</Servico>\.__

__TAG obrigatória\.__

MFS\-8205

__RN43__

__Regra para tag <Prestador> __

Tag relacionada à abertura das informações do prestador do serviço com o texto fixo: __<Prestador>\.__

__TAG obrigatória\.__

MFS\-8205

__RN44__

__Regra para tag <IdentificacaoPrestador> __

Tag relacionada à abertura da identificação do prestador do serviço com o texto fixo: __<IdentificacaoPrestador>\.__

__TAG obrigatória\.__

MFS\-8205

__RN45__

__Regra p/ tag <CodEmpresa> </CodEmpresa>__

Identifica o código da Prefeitura\. 

Preencher com o conteúdo fixo: “1”, sem necessidade de espaços ou zeros para complementar o tamanho do campo\.

__Campo obrigatório__

Formato: 9

Tipo: Numérico

Tamanho: 10

MFS\-8205

__RN46__

__Regra p/ tag <CpfCnpj> __

Tag relacionada à abertura dos dados de cadastro do prestador do serviço com o texto fixo: __<CpfCnpj>\.__

__TAG obrigatória\.__

MFS\-8205

__RN47__

__Regra p/ tag <Cnpj> </Cnpj> ou <Cpf> </Cpf>__

Identifica o CNPJ \(se empresa\) ou o CPF \(se pessoa física\) do prestador\. 

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR \(campo 06 da SAFX04\) referente o prestador cadastrado na nota fiscal\.

__Tratamento:__

- Se o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR for menor ou igual a 11 posições a TAG deverá ser gerada como __<Cpf> </Cpf>;__
- Se o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR for maior que 11 posições a TAG deverá ser gerada como __<Cnpj> </Cnpj>\.__

__Campo obrigatório__

Formato: 99999999999 ou 99999999999999

Tipo: Numérico

Tamanho: 11 ou 14

MFS\-8205

__RN48__

__Regra p/ tag </CpfCnpj> __

Tag relacionada ao encerramento dos dados de cadastro do prestador do serviço com o texto fixo: __</CpfCnpj>\.__

__TAG obrigatória\.__

MFS\-8205

__RN49__

__Regra p/ tag <InscricaoMunicipal> </InscricaoMunicipal>__

Identifica a Inscrição Municipal do prestador\. 

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR \(campo 09 da SAFX04\) referente o prestador cadastrado na nota fiscal, sem necessidade de espaços ou zeros para complementar o tamanho do campo\.

__Tratamento:__

- Se o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR não estiver preenchido, emitir uma mensagem padrão de log\.

__Campo obrigatório__

Formato: XXXXXXXXXXXXXXX

Tipo: Alfanumérico

Tamanho: 15

MFS\-8205

__RN50__

__Regra para tag </IdentificacaoPrestador> __

Tag relacionada ao encerramento da identificação do prestador do serviço com o texto fixo: __</IdentificacaoPrestador>\.__

__TAG obrigatória\.__

MFS\-8205

__RN51__

__Regra p/ tag <RazaoSocial> </RazaoSocial>__

Identifica a Razão Social do prestador\. 

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR \(campo 05 da SAFX04\) referente o prestador cadastrado na nota fiscal\.

__Campo obrigatório__

Formato: XXXXXXXXXXXXXXX 

Tipo: Alfanumérico

Tamanho: \(sem limite de tamanho\)

MFS\-8205

__RN52__

__Regra p/ tag <NomeFantasia> </NomeFantasia>__

Identifica a Nome Fantasia do prestador\. 

Preencher com o campo NOME\_FANTASIA da tabela X04\_PESSOA\_FIS\_JUR \(campo 11 da SAFX04\) referente o prestador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: XXXXXXXXXXXXXXX 

Tipo: Alfanumérico

Tamanho: \(sem limite de tamanho\)

MFS\-8205

__RN53__

__Regra p/ tag <RgInscre> </RgInscre>__

Identifica o RG ou a Inscrição Estadual do prestador\. 

Preencher com o campo INSC\_ESTADUAL da tabela X04\_PESSOA\_FIS\_JUR \(campo 08 da SAFX04\) referente o prestador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: XXXXXXXXXXXXXXX 

Tipo: Alfanumérico

Tamanho: \(sem limite de tamanho\)

MFS\-8205

__RN54__

__Regra p/ tag <Endereco> __

Tag relacionada à abertura dos dados de endereço do prestador do serviço com o texto fixo: __<Endereco>\.__

__TAG obrigatória\.__

MFS\-8205

__RN55__

__Regra p/ tag <Endereco> </Endereco>__

Identifica o endereço do prestador\. 

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 12 da SAFX04\) referente o prestador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: XXXXXXXXXXXXXXX *\.\.\.\]*

Tipo: Alfanumérico

Tamanho: 125

MFS\-8205

__RN56__

__Regra p/ tag <Numero> </Numero>__

Identifica o número do endereço do prestador\. 

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 13 da SAFX04\) referente o prestador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: XXXXXXXXXX

Tipo: Alfanumérico

Tamanho: 10

MFS\-8205

__RN57__

__Regra p/ tag <Complemento> </Complemento>__

Identifica o complemento do endereço do prestador\. 

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 14 da SAFX04\) referente o prestador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: XXXXXXXXXX 

Tipo: Alfanumérico

Tamanho: 60

MFS\-8205

__RN58__

__Regra p/ tag <Bairro> </Bairro>__

Identifica o bairro do endereço do prestador\. 

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR \(campo 15 da SAFX04\) referente o prestador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: XXXXXXXXXX 

Tipo: Alfanumérico

Tamanho: 60

MFS\-8205

__RN59__

__Regra p/ tag <CodigoMunicipio> </CodigoMunicipio>__

Identifica o código do município \(IBGE\) do Prestador\. 

Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do Município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\)\.

__Tratamento:__

- Se o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR não estiver preenchido, emitir uma mensagem padrão de log\.

__Campo obrigatório__

Formato: 9999999

Tipo: Numérico

Tamanho: 7

MFS\-8205

__RN60__

__Regra p/ tag <Uf> </Uf>__

Identifica a Unidade Federativa do Prestador\. 

Preencher com o campo UF da tabela X04\_PESSOA\_FIS\_JUR \(campo 19 da SAFX04\) referente o prestador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: XX

Tipo: Alfanumérico

Tamanho: 2

MFS\-8205

__RN61__

__Regra p/ tag <CodigoPais> </CodigoPais>__

Identifica o Código do País \(BACEN\) do Prestador\. 

Preencher com o campo COD\_PAIS \+ DIG\_VERIFICADOR da tabela PAIS relacionado ao IDENT\_ESTADO do município informado no campo <CodigoMunicipio> \(RN60\)\.

__Campo não obrigatório__

Formato: 9999

Tipo: Numérico

Tamanho: 4

MFS\-8205

__RN62__

__Regra p/ tag <Cep> </Cep>__

Identifica o CEP do Prestador\. 

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR \(campo 20 da SAFX04\) referente o prestador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: 99999999

Tipo: Numérico

Tamanho: 8

MFS\-8205

__RN63__

__Regra p/ tag </Endereco> __

Tag relacionada ao encerramento dos dados de endereço do prestador do serviço com o texto fixo: __</Endereco>\.__

__TAG obrigatória\.__

MFS\-8205

__RN64__

__Regra p/ tag <Contato> __

Tag relacionada à abertura dos dados de contato do prestador do serviço com o texto fixo: __<Contato>\.__

__TAG não obrigatória\.__

MFS\-8205

__RN65__

__Regra p/ tag <Telefone> </Telefone>__

Identifica o Telefone do Prestador\. 

Preencher com o campo DDD \+ TELEFONE da tabela X04\_PESSOA\_FIS\_JUR \(campos 22 e 23 da SAFX04\) referente o prestador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: XXXXXXXXXXXXXXXXXXXX

Tipo: Alfanumérico

Tamanho: 20

MFS\-8205

__RN66__

__Regra p/ tag <Email> </Email>__

Identifica o E\-mail do Prestador\. 

Preencher com o campo E\_MAIL da tabela X04\_PESSOA\_FIS\_JUR \(campo 40 da SAFX04\) referente o prestador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: XXXXXXXXXXXXXXXXXXXX *\.\.\.\]*

Tipo: Alfanumérico

Tamanho: 80

MFS\-8205

__RN67__

__Regra p/ tag </Contato> __

Tag relacionada ao encerramento dos dados de contato do prestador do serviço com o texto fixo: __</Contato>\.__

__TAG não obrigatória\.__

MFS\-8205

__RN68__

__Regra p/ tag <ExigibilidadeISS> </ExigibilidadeISS>__

Identifica a exigência da tributação do ISS do Prestador\. 

Preencher com:

__“3” \- Isenção\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “10”; __OU__
- Se não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433” no módulo: Parâmetros para Município\.

__“5” \- Imunidade\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “07”; __OU__
- Se não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420” no módulo: Parâmetros para Município\.

__“6” \- Exigibilidade Suspensa por Decisão Judicial\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “09”; __OU__
- Se não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427” no módulo: Parâmetros para Município\.

__“7” \- Exigibilidade Suspensa por Processo Administrativo\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “11”; __OU__
- Se não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “485” no módulo: Parâmetros para Município\.

__“2” \- Não Incidência\.__

- Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “432” no módulo: Parâmetros para Município\.

__“4” \- Exportação\.__

- Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “520” no módulo: Parâmetros para Município\.

Se nenhuma das opções anteriores for verdadeira, preencher com:

__“1” \- Exigível\.__

__Campo obrigatório__

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-8205

__RN69__

__Regra p/ tag <NumeroProcesso> </NumeroProcesso>__

Identifica o Número do Processo quando a exigibilidade do Prestador é Suspensa por Decisão Judicial ou Suspensa por Processo Administrativo\. 

Preencher com o campo NUM\_PROC\_JUR da tabela DWT\_DOCTO\_FISCAL \(campo 274 da SAFX07\) quando o IND\_TIPO\_PROC da tabela DWT\_DOCTO\_FISCAL \(campo 273 da SAFX07\) estiver preenchido e se a TAG__ <ExigibilidadeISS>__ for igual a 6 ou 7 \(RN69\)\.

__Tratamento:__

- Se a TAG__ <ExigibilidadeISS>__ for igual a 6 ou 7 e o campo NUM\_PROC\_JUR da tabela DWT\_DOCTO\_FISCAL não estiver preenchido, emitir a mensagem de log: “A exigibilidade da nota fiscal *<<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>> *é por Suspensão e necessita do preenchimento do Número do Processo\.”\.

__Campo não obrigatório__

Formato: XXXXXXXXXXXXXXXXXXXX

Tipo: Numérico

Tamanho: 20

MFS\-8205

__RN70__

__Regra p/ tag <RegimeEspecialTributacao> </RegimeEspecialTributacao>__

Identifica se o Prestador possui regime especial de tributação\. 

Preencher com:

__“1” \- Microempresa municipal\.__

- Se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR \(campo 27 da SAFX04\) = “04 – Microempresa \(ME\)” referente o prestador cadastrado na nota fiscal\.

__“2” \- Estimativa\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “08 \- Regime de Estimativa” referente o prestador cadastrado na nota fiscal\.

__“3” \- Sociedade de Profissionais\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “06 \- Sociedade Profissional” referente o prestador cadastrado na nota fiscal\.

__“4” \- Cooperativa\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “02 \- Cooperativa” e “05 \- Cooperativa de Transporte” referente o prestador cadastrado na nota fiscal\.

__“5” \- Microempresário Individual \(MEI\)\.__

- Se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR \(campo 27 da SAFX04\) = “05 – MEI \(Micro Empreendedor Individual\)” referente o prestador cadastrado na nota fiscal\.

__“6” \- Microempresário e Empresa de Pequeno Porte \(ME EPP\)\.__

- Se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR \(campo 27 da SAFX04\) = “01 \- EPP \(Empresa de Pequeno Porte\)” referente o prestador cadastrado na nota fiscal\.

Se nenhuma das opções anteriores for verdadeira, preencher com:

__“0” \- Não Possui\.__

__Campo obrigatório__

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-8205

__RN71__

__Regra p/ tag <OptanteSimplesNacional> </OptanteSimplesNacional>__

Identifica se o Prestador é optante do Simples Nacional\. 

Preencher com:

__“1” \- Sim\.__

- Se o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR \(campo 43 da SAFX04\) for igual “S” referente o prestador cadastrado na nota fiscal\.

Senão, preencher com:

__“2” \- Não\.__

__Campo obrigatório__

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-8205

__RN72__

__Regra p/ tag <IncentivoFiscal> </IncentivoFiscal>__

Identifica se o Prestador possui incentivo fiscal\. 

Preencher com:

__“1” \- Sim\.__

- Se o campo IND\_NF\_ESPECIAL da tabela DWT\_DOCTO\_FISCAL \(campo 71 da SAFX07\) for diferente de “N”\.

Senão, preencher com:

__“2” \- Não\.__

__Campo obrigatório__

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-8205

__RN73__

__Regra para tag </Prestador> __

Tag relacionada ao encerramento das informações do prestador do serviço com o texto fixo: __</Prestador>\.__

__TAG obrigatória\.__

MFS\-8205

__RN74__

__Regra para tag <ItensNotas> __

Tag relacionada à abertura das informações dos itens da nota fiscal com o texto fixo: __<ItensNotas>\.__

__TAG obrigatória\.__

MFS\-8205

__RN75__

__Regra para tag <item> __

Tag relacionada à abertura das informações do item da nota fiscal com o texto fixo: __<item>\.__

__TAG obrigatória\.__

MFS\-8205

__RN76__

__Regra p/ tag <DescriNfi> </DescriNfi>__

Identifica da descrição do serviço\. 

Preencher com o campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\.

__Campo obrigatório__

Formato: XXXXXXXXXXXXXXXXXXXX *\.\.\.\]*

Tipo: Alfanumérico

Tamanho: \-

MFS\-8205

__RN77__

__Regra p/ tag <MedidaNfi> </MedidaNfi>__

Identifica a Unidade de Medida\. 

Preencher com o conteúdo fixo: “UN”\.

__Campo obrigatório__

Formato: XX

Tipo: Alfanumérico

Tamanho: 2

MFS\-8205

__RN78__

__Regra p/ tag <QuantidadeNfi> </QuantidadeNfi>__

Identifica a quantidade do serviço\. 

Preencher com o campo QUANTIDADE da tabela DWT\_ITENS\_SERV \(campo 19 da SAFX09\)\.

__Tratamento:__

- Se o campo QUANTIDADE da tabela DWT\_ITENS\_SERV não estiver preenchido, emitir mensagem padrão de log\.

__Campo obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-8205

__RN79__

__Regra p/ tag <VlrUnitarioNfi> </VlrUnitarioNfi>__

Identifica o valor unitário do item\. 

Preencher com o campo VLR\_UNIT da tabela DWT\_ITENS\_SERV \(campo 20 da SAFX09\)\.

__Tratamento:__

- Se o campo VLR\_UNIT da tabela DWT\_ITENS\_SERV não estiver preenchido, emitir mensagem padrão de log\.

__Campo obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-8205

__RN80__

__Regra p/ tag <DesccondicionalNfi> </DesccondicionalNfi>__

Identifica o desconto condicional do item\. 

Preencher com o campo VLR\_DESC\_CONDIC da tabela DWT\_DOCTO\_FISCAL \(campo 109 da SAFX07\)\.

__Campo não obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-8205

__RN81__

__Regra p/ tag <DescincondicionalNfi> </DescincondicionalNfi>__

Identifica o desconto incondicional do item\. 

Não será tratado, preencher com zero\.

__Campo não obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-8205

__RN82__

__Regra p/ tag <DeducaobaseNfi> </DeducaobaseNfi>__

Preencher com o campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV \(campo 59 da SAFX09\)\.

__Campo não obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-8205

__RN83__

__Regra para tag </item> __

Tag relacionada ao encerramento das informações do item da nota fiscal com o texto fixo: __</item>\.__

__TAG obrigatória\.__

MFS\-8205

__RN84__

__Regra para tag </ItensNotas> __

Tag relacionada ao encerramento das informações dos itens da nota fiscal com o texto fixo: __</ItensNotas>\.__

__TAG obrigatória\.__

MFS\-8205

__RN85__

__Regra para tag </InfDeclaracaoPrestacaoServicoTomador> __

Tag relacionada ao encerramento das informações da nota fiscal do tomador do serviço com o texto fixo: __</InfDeclaracaoPrestacaoServicoTomador>\.__

__TAG obrigatória\.__

MFS\-8205

__RN86__

__Regra para tag </NotaFiscalTomador> __

Tag ao encerramento das informações da nota fiscal do tomador do serviço com o texto fixo: __</NotaFiscalTomador>\.__

__TAG obrigatória\.__

MFS\-8205

__RN87__

__Regra para tag </LoteNotaFiscalTomador> __

Tag relacionada ao encerramento dos dados da nota fiscal do tomador do serviço com o texto fixo: __</LoteNotaFiscalTomador>\.__

__TAG obrigatória\.__

MFS\-8205

__RN88__

__Regra p/ tag <QuantidadeNotas> </QuantidadeNotas>__

Identifica a quantidade de notas fiscais do lote\.

Preencher com a quantidade de notas fiscais informadas na TAG __<LoteNotaFiscalTomador>\.__

__Campo obrigatório__

Formato: 9999999999

Tipo: Numérico

Tamanho: 10

MFS\-8205

__RN89__

__Regra para tag </Declaracao> __

Tag relacionada ao encerramento da formatação do arquivo e que deve receber as informações das notas tomadas declaradas com o texto fixo: __</Declaracao>\.__

__TAG obrigatória\.__

MFS\-8205

__RN90__

__SERVIÇOS PRESTADOS__

__Regra p/ Recuperar Notas Fiscais de SERVIÇOS PRESTADOS – REGRA GERAL:__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de saída \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL = ‘9’\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)

__Observação:__ Quando a nota fiscal não tiver itens não deve ser considerada\.

MFS\-36689

__RN91__

__Estrutura do Arquivo:__

<?xml version="1\.0" encoding="UTF\-8" standalone="yes"?> 

<Declaracao> 

   <Prestador> 

     <CodEmpresa>1</CodEmpresa> 

     <CpfCnpj> 

       <Cnpj>01704233000138</Cnpj> 

     </CpfCnpj> 

     <InscricaoMunicipal>20\.261\.</InscricaoMunicipal> 

   </Prestador> 

   <Referencia>04/2013</Referencia> 

   <LoteNotaFiscal> 

     <NotaFiscal> 

       <InfDeclaracaoPrestacaoServico> 

         <DadosNotaFiscal> 

            <IdentificacaoNotaFiscal> 

               <Numero>1</Numero> 

               <Especie>1</Especie> 

               <Serie>1</Serie> 

            </IdentificacaoNotaFiscal> 

            <DataEmissao>2013\-04\-11T15:14:02</DataEmissao> 

          </DadosNotaFiscal> 

          <Servico> 

             <Aliquotas> 

                <Aliquota>2</Aliquota> 

                <AliquotaCofins>3</AliquotaCofins> 

                <AliquotaCsll>1\.08</AliquotaCsll> 

                <AliquotaInss>2\.5</AliquotaInss> 

                <AliquotaIr>2</AliquotaIr> 

                <AliquotaPis>0\.65</AliquotaPis> 

             </Aliquotas> 

             <IssRetido>1</IssRetido> 

             <ResponsavelRetencao>2</ResponsavelRetencao> 

             <CodigoMunicipio>3504800</CodigoMunicipio> 

             <CodigoPais>1058</CodigoPais> 

             <ExigibilidadeISS>1</ExigibilidadeISS> 

             <NumeroProcesso>45156625</NumeroProcesso> 

             <CodAtividade>000001</CodAtividade> 

             <CodAtividadeDesdobro>0000004</CodAtividadeDesdobro> 

           </Servico> 

           <Tomador> 

              <IdentificacaoTomador> 

                 <CodEmpresa>1</CodEmpresa> 

                 <CpfCnpj> 

                    <Cnpj>32402074000140</Cnpj> 

                 </CpfCnpj> 

                 <InscricaoMunicipal>121213</InscricaoMunicipal> 

              </IdentificacaoTomador> 

              <RazaoSocial>Marisa Martins Concorde Me</RazaoSocial> 

              <NomeFantasia>Marisa</NomeFantasia> 

              <RgInscre>121213</RgInscre> 

              <Endereco> 

                 <Endereco>Rua XV de Novembro</Endereco> 

                 <Numero>454</Numero> 

                 <Complemento>Casa</Complemento> 

                 <Bairro>Jardim Congonhas</Bairro> 

                 <CodigoMunicipio>3549805</CodigoMunicipio> 

                 <Uf>SP</Uf> 

                 <CodigoPais>1058</CodigoPais> 

                 <Cep>15075124</Cep> 

              </Endereco> 

              <Contato> 

                 <Telefone>1732358741</Telefone> 

                 <Email>user@fiorilli\.com\.br</Email> 

              </Contato> 

            </Tomador> 

            <Intermediario> 

               <IdentificacaoTomador> 

                 <CpfCnpj> 

                    <Cnpj>06117145000153</Cnpj> 

                 </CpfCnpj>

                 <InscricaoMunicipal>123\.32</InscricaoMunicipal> 

              </IdentificacaoTomador> 

              <RazaoSocial>Novo Mundo Magazine Ltda</RazaoSocial> 

              <NomeFantasia>Novo Mundo</NomeFantasia> 

              <RgInscre>5645256</RgInscre> 

              <Endereco> 

                 <Endereco>Avenida da Saudade</Endereco> 

                 <Numero>1254</Numero> 

                 <Complemento>Casa</Complemento> 

                 <Bairro>Jardim Eldorado</Bairro> 

                 <CodigoMunicipio>3549805</CodigoMunicipio> 

                 <Uf>SP</Uf> 

                 <CodigoPais>1058</CodigoPais> 

                 <Cep>15075145</Cep> 

              </Endereco> 

              <Contato> 

                 <Telefone>1732358741</Telefone> 

                 <Email>user2@fiorilli\.com\.br</Email> 

              </Contato> 

            </Intermediario> 

            <RegimeEspecialTributacao>1</RegimeEspecialTributacao> 

            <OptanteSimplesNacional>1</OptanteSimplesNacional> 

            <IncentivoFiscal>1</IncentivoFiscal> 

            <ItensNotas> 

              <item> 

                 <DescriNfi>Manutenção Preventiva</DescriNfi> 

                 <MedidaNfi>UN</MedidaNfi> 

                 <QuantidadeNfi>1</QuantidadeNfi> 

                 <VlrUnitarioNfi>550</VlrUnitarioNfi> 

                 <DesccondicionalNfi>0</DesccondicionalNfi> 

                 <DescincondicionalNfi>0</DescincondicionalNfi> 

                 <DeducaobaseNfi>0</DeducaobaseNfi> 

               </item> 

            </ItensNotas> 

         </InfDeclaracaoPrestacaoServico> 

       </NotaFiscal> 

   </LoteNotaFiscal> 

   <QuantidadeNotas>2</QuantidadeNotas> 

</Declaracao>

MFS\-36689

__RN92__

__Regra p/ o cabeçalho do arquivo:__

Preencher com a tag__ __<?xml version="1\.0" encoding="UTF\-8" standalone="yes"?>

MFS\-36689

__RN93__

__Regra para tag <Declaracao> __

Tag relacionada à abertura da formatação do arquivo e que deve receber as informações das notas prestadas declaradas com o texto fixo:__ <Declaracao>\.__

__TAG obrigatória\.__

MFS\-36689

__RN94__

__Regra para tag <Prestador> __

Tag relacionada à abertura dos dados do prestador do serviço com o texto fixo:__ < Prestador >\.__

__TAG obrigatória\.__

MFS\-36689

__RN95__

__Regra p/ tag <CodEmpresa> </CodEmpresa>__

Identifica o código da Prefeitura\. 

Preencher com o conteúdo fixo: “1”, sem necessidade de espaços ou zeros para complementar o tamanho do campo\.

__Campo obrigatório__

Formato: 9

Tipo: Numérico

Tamanho: 10

MFS\-36689

__RN96__

__Regra p/ tag <CpfCnpj> __

Tag relacionada à abertura dos dados de cadastro do tomador do serviço com o texto fixo:__ <CpfCnpj>\.__

__TAG obrigatória\.__

MFS\-36689

__RN97__

__Regra p/ tag <Cnpj> </Cnpj>__

Identifica o CNPJ do prestador\. 

Preencher com o campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento que está sendo gerado o arquivo magnético\.

__Campo obrigatório__

Formato: 99999999999999

Tipo: Numérico

Tamanho: 14

MFS\-36689

__RN98__

__Regra p/ tag </CpfCnpj> __

Tag relacionada ao encerramento dos dados de cadastro do tomador do serviço com o texto fixo:__ </CpfCnpj>\.__

__TAG obrigatória\.__

MFS\-36689

__RN99__

__Regra p/ tag <InscricaoMunicipal> </InscricaoMunicipal>__

Identifica a Inscrição Municipal do prestador\. 

Preencher com o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO referente ao estabelecimento que está sendo gerado o arquivo magnético, sem necessidade de espaços ou zeros para complementar o tamanho do campo, pode permitir pontuação\.

__Tratamento:__

- Se o campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO não estiver preenchido, emitir uma mensagem padrão de log\.

__Campo obrigatório__

Formato: XXXXXXXXXXXXXXX

Tipo: Alfanumérico

Tamanho: 15

MFS\-36689

__RN100__

__Regra para tag </Prestador > __

Tag relacionada ao encerramento dos dados do prestador do serviço com o texto fixo:__ </Prestador >\.__

__TAG obrigatória\.__

MFS\-36689

__RN101__

__Regra p/ tag <Referencia> </Referencia>__

Identifica o mês/ ano das notas fiscais\. 

Preencher com o mês e o ano do conteúdo do campo “Data Inicial” da tela de geração do meio magnético\.

__Campo obrigatório__

Formato: MM/AAAA

Tipo: Data

Tamanho: \-

MFS\-36689

__RN102__

__Regra para tag <LoteNotaFiscal> __

Tag relacionada à abertura dos dados da nota fiscal do prestador do serviço com o texto fixo:__ <LoteNotaFiscal>\.__

__TAG obrigatória\.__

MFS\-36689

__RN103__

__Regra para tag <NotaFiscal> __

Tag relacionada à abertura das informações da nota fiscal do prestador do serviço com o texto fixo:__ <NotaFiscal>\.__

__TAG obrigatória\.__

MFS\-36689

__RN104__

__Regra para tag <InfDeclaracaoPrestacaoServico> __

Tag relacionada à abertura das informações da nota fiscal do prestador do serviço com o texto fixo:__ <InfDeclaracaoPrestacaoServico>\.__

__TAG obrigatória\.__

MFS\-36689

__RN105__

__Regra para tag <DadosNotaFiscal> __

Tag relacionada à abertura das informações da nota fiscal do prestador do serviço com o texto fixo: __<DadosNotaFiscal>\.__

__TAG obrigatória\.__

MFS\-36689

__RN106__

__Regra para tag <IdentificacaoNotaFiscal> __

Tag relacionada à abertura da identificação da nota fiscal do prestador do serviço com o texto fixo:__ <IdentificacaoNotaFiscal>\.__

__TAG obrigatória\.__

MFS\-36689

__RN107__

__Regra p/ tag <Numero> </Numero>__

Identifica o Número da Nota fiscal\. 

Preencher com o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\), sem necessidade de espaços ou zeros para complementar o tamanho do campo\.

__Campo obrigatório__

Formato: 99999999999999999999

Tipo: Numérico

Tamanho: 20

MFS\-36689

__RN108__

__Regra p/ tag <Especie> </Especie>__

Identifica a Espécie da Nota fiscal conforme cadastrado\. 

Preencher com o conteúdo fixo: “1”, sem necessidade de espaços ou zeros para complementar o tamanho do campo\.

__Observação:__ Estamos colocando como fixo 1 conforme determina a Prefeitura no que se refere a Prestação de Serviço\.

__Campo obrigatório__

Formato: 99999999999999999999

Tipo: Numérico

Tamanho: 20

MFS\-36689

__RN109__

__Regra p/ tag <Serie> </Serie> \- REGRA GERAL__

Identifica a Série da Nota fiscal conforme cadastrado\. 

Preencher com o campo Série da tela de parametrização __Parâmetros para Município – Série Msaf x Série__, associado a série informada na nota fiscal \(campo SERIE\_DOCFIS da DWT\_ITENS\_SERV\)\.

__Tratamento:__

- Se não existir a parametrização da série informada, emitir mensagem padrão de log\.

__Campo obrigatório__

Formato: 99999999999999999999

Tipo: Numérico

Tamanho: 20

MFS\-42965

__MFS\-88149__

__RN109\.a__

__Regra p/ tag <Serie> </Serie>  \-  ESPECÍFICA__

__MUNICÍPIOS: Laranjal Paulista/SP, Assis/SP, Nova Alvorada do Sul/MS, José Bonifácio/SP, Santa Rita do Passa Quatro/SP, Três Lagoas/MS\.__

Identifica a Série da Nota fiscal conforme cadastrado\. 

Preencher com:

“2” \- Nota Fiscal Eletrônica\.

- Se o campo código de modelo cadastrado na nota fiscal for igual a “55” OU o indicador de Tipo de Documento para Nota Fiscal Eletrônica for igual a “S” referente ao tipo de documento cadastrado na nota fiscal\.

Senão, preencher com:

“1” \- Nota Avulsa\.

__Campo obrigatório__

Formato: 99999999999999999999

Tipo: Numérico

Tamanho: 20

MFS\-36689

MFS\-42965

MFS\-53878

MFS\-62248

__RN110__

__Regra para tag </IdentificacaoNotaFiscal> __

Tag relacionada ao encerramento da identificação da nota fiscal do tomador do serviço com o texto fixo:__ </IdentificacaoNotaFiscal>\.__

__TAG obrigatória\.__

MFS\-36689

__RN111__

__Regra p/ tag <DataEmissao> </DataEmissao>__

Identifica a Data e Hora da emissão da nota\. 

Preencher com o campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL\+‘T’\+‘00:00:00’ \(campo 11 da SAX07\)\.

__Campo obrigatório__

Formato: AAAA\-MM\-DDTHH:mm:ss

Tipo: Data\-Hora

Tamanho: \-

MFS\-36689

__RN112__

__Regra para tag </DadosNotaFiscal> __

Tag relacionada ao encerramento das informações da nota fiscal do tomador do serviço com o texto fixo:__ </DadosNotaFiscal>\.__

TAG obrigatória\.

MFS\-36689

__RN113__

__Regra para tag <Servico> __

Tag relacionada à abertura das informações do serviço da nota fiscal com o texto fixo: __<Servico>\.__

__TAG obrigatória\.__

MFS\-36689

__RN114__

__Regra para tag <Aliquotas> __

Tag relacionada à abertura das informações da alíquota do serviço da nota fiscal com o texto fixo: <Aliquotas>\.

__TAG obrigatória\.__

MFS\-36689

__RN115__

__Regra p/ tag <Aliquota> </Aliquota>__

Identifica a Alíquota ISS da Nota Fiscal\. 

Preencher com o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV \(campo 32 da SAFX09\)\.

__Tratamento:__

- Se o campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV não estiver preenchido, emitir mensagem padrão de log\.

__Campo obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-36689

__RN116__

__Regra p/ tag <AliquotaCofins> </AliquotaCofins>__

Identifica a Alíquota da COFINS da Nota Fiscal\. 

Preencher com o campo VLR\_ALIQ\_COFINS da tabela DWT\_ITENS\_SERV \(campo 50 da SAFX09\)\.

__Campo não obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-36689

__RN117__

__Regra p/ tag <AliquotaCsll> </AliquotaCsll>__

Identifica a Alíquota da Csll da Nota Fiscal\. 

Preencher com o campo VLR\_ALIQ\_CSLL da tabela DWT\_ITENS\_SERV \(campo 44 da SAFX09\)\.

__Campo não obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-36689

__RN118__

__Regra p/ tag <AliquotaInss> </AliquotaInss>__

Identifica a Alíquota do INSS da Nota Fiscal\. 

Preencher com o campo VLR\_ALIQ\_INSS da tabela DWT\_ITENS\_SERV \(campo 78 da SAFX09\)\.

__Campo não obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-36689

__RN119__

__Regra p/ tag <AliquotaIr> </AliquotaIr>__

Identifica a Alíquota do IR da Nota Fiscal\. 

Preencher com o campo VLR\_ALIQ\_IR da tabela DWT\_ITENS\_SERV \(campo 30 da SAFX09\)\.

__Campo não obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-36689

__RN120__

__Regra p/ tag <AliquotaPis> </AliquotaPis>__

Identifica a Alíquota do PIS da Nota Fiscal\. 

Preencher com o campo VLR\_ALIQ\_PIS da tabela DWT\_ITENS\_SERV \(campo 47 da SAFX09\)\.

__Campo não obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-36689

__RN121__

__Regra para tag </Aliquotas> __Tag relacionada ao encerramento das informações da alíquota do serviço da nota fiscal com o texto fixo:__ </Aliquotas>\.__

__TAG obrigatória\.__

MFS\-36689

__RN122__

__Regra p/ tag <IssRetido> </IssRetido>__

Identifica se o ISS foi retido ou não pelo Prestador\. 

__Preencher com:__

 __“1”__ \- Sim

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “2" e se o local da prestação do serviço = município do módulo selecionado OU 
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_SUBSTITUIDO\_ISS = “N” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado OU
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

__Senão,__ preencher com:

__“2”__ \- Não\.

__Campo obrigatório__

Formato: 9 \(1\-Sim ou 2\-Não\)

Tipo: Numérico

Tamanho: 1

MFS\-36689

__RN123__

__Regra p/ tag <ResponsavelRetencao> </ResponsavelRetencao >__

Identifica o responsável pela retenção\. 

Preencher com:

__“1”__ \- Tomador\.

__Campo não obrigatório__

Formato: 9 \(1 \- Tomador ou 2\- Intermediário\)

Tipo: Numérico

Tamanho: 1

MFS\-36689

__RN124__

__Regra p/ tag <CodigoMunicipio> </CodigoMunicipio>__

Identifica o Código do Município \(IBGE\) do Prestador\. 

Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do Município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

__Campo não obrigatório__

Formato: 9999999

Tipo: Numérico

Tamanho: 7

MFS\-36689

__RN125__

__Regra p/ tag <CodigoPais> </CodigoPais>__

Identifica o Código do País \(BACEN\) do Prestador\. 

Preencher com o conteúdo fixo: “1058”\.

__Campo não obrigatório__

Formato: 9999

Tipo: Numérico

Tamanho: 4

MFS\-36689

__RN126__

__Regra p/ tag <ExigibilidadeISS> </exbilidadeISS>__

Identifica a exigência da tributação do ISS dos Serviços Prestados

__Preencher com:__

__“3”__ \- Isenção\.

- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “04”; OU
- Se não estiver preenchido, verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433” no módulo: Parâmetros para Município\.

__“5”__ \- Imunidade\.

- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “01”; OU
- Se não estiver preenchido, verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420” no módulo: Parâmetros para Município\.

__“6”__ \- Exigibilidade Suspensa por Decisão Judicial\.

- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “03”; OU
- Se não estiver preenchido, verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427” no módulo: Parâmetros para Município\.

__“7”__ \- Exigibilidade Suspensa por Processo Administrativo\.

- Verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “485” no módulo: Parâmetros para Município\.

__“2”__ \- Não Incidência\.

- Se o serviço cadastrado na nota e o município cadastrado no estabelecimento estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “432” no módulo: Parâmetros para Município\.

__“4”__ \- Exportação\.

- Se o serviço cadastrado na nota e o município cadastrado no estabelecimento estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “520” no módulo: Parâmetros para Município\.

Se nenhuma das opções anteriores for verdadeira, preencher com:

__“1” __\- Exigível\.

__Campo obrigatório__

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-36689

__RN127__

__Regra p/ tag <NumeroProcesso> </NumeroProcesso>__

Identifica o Número do Processo quando a exigibilidade do Prestador é Suspensa por Decisão Judicial ou Suspensa por Processo Administrativo\. 

Preencher com o campo NUM\_PROC\_JUR da tabela DWT\_DOCTO\_FISCAL \(campo 274 da SAFX07\) quando o IND\_TIPO\_PROC da tabela DWT\_DOCTO\_FISCAL \(campo 273 da SAFX07\) estiver preenchido e se a TAG <ExigibilidadeISS> for igual a 6 ou 7 \(RN69\)\.

__Tratamento:__

- Se a TAG <ExigibilidadeISS> for igual a 6 ou 7 e o campo NUM\_PROC\_JUR da tabela DWT\_DOCTO\_FISCAL não estiver preenchido, emitir a mensagem de log: “A exigibilidade da nota fiscal <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>> é por Suspensão e necessita do preenchimento do Número do Processo\.”\.

__Campo não obrigatório__

Formato: XXXXXXXXXXXXXXXXXXXX

Tipo: Numérico

Tamanho: 20

MFS\-36689

__RN128__

__Regra p/ tag <CodAtividade> </CodAtividade>__

Identifica o Grupo do Código de Atividade do Serviço\. 

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal, mas considerar apenas as duas primeiras posições e completar com zeros à esquerda\. Exemplo: Lei 116 “0101” deverá ser preenchida como “000001”; Lei 116 “0107” deverá ser preenchida “000001”\.

__Tratamento:__

- Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, deverá ser gravado com 0 \(zero\) e emitida a mensagem de log: “Erro: Favor preencher o código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.

__Campo obrigatório__

Formato: 999999

Tipo: Numérico

Tamanho: 6

MFS\-36689

__RN129__

__Regra p/ tag <CodAtividadeDesdobro> </CodAtividadeDesdobro>__

Identifica o Desdobro da Atividade do Serviço\. 

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal, mas considerar apenas as duas últimas posições e completar com zeros à esquerda\. Exemplo: Lei 116 “0101” deverá ser preenchida como “0000001”; Lei 116 “0107” deverá ser preenchida “0000007”\.

__Tratamento:__

- Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, deverá ser gravado com 0 \(zero\) e emitida a mensagem de log: “Erro: Favor preencher o código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal <<NF>>, <<Série>>, <<Subsérie>>, <<Data Fiscal>>”\.

__Campo obrigatório__

Formato: 9999999

Tipo: Numérico

Tamanho: 7

MFS\-36689

__RN130__

__Regra para tag </Servico> __

Tag relacionada ao encerramento das informações do serviço da nota fiscal com o texto fixo__: </Servico>\.__

__TAG obrigatória\.im26__

MFS\-36689

__RN131__

__Regra para tag <Tomador> __

Tag relacionada à abertura das informações do tomador do serviço com o texto fixo__: <Tomador>\.__

__TAG obrigatória\.__

MFS\-36689

__RN132__

__Regra para tag <IdentificacaoTomador> __

Tag relacionada à abertura da identificação do tomador do serviço com o texto fixo:__ <IdentificacaoTomador>\.__

__TAG obrigatória\.__

MFS\-36689

__RN133__

__Regra p/ tag <CodEmpresa> </CodEmpresa>__

Identifica o código da Prefeitura\. 

Preencher com o conteúdo fixo: “1”, sem necessidade de espaços ou zeros para complementar o tamanho do campo\.

__Campo obrigatório__

Formato: 9

Tipo: Numérico

Tamanho: 10

MFS\-36689

__RN134__

__Regra p/ tag <CpfCnpj> __

Tag relacionada à abertura dos dados de cadastro do tomador do serviço com o texto fixo:__ <CpfCnpj>\.__

__TAG obrigatória\.__

MFS\-36689

__RN135__

__Regra p/ tag <Cnpj> </Cnpj> ou <Cpf> </Cpf>__

Identifica o CNPJ \(se empresa\) ou o CPF \(se pessoa física\) do tomador\. 

Preencher com o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR \(campo 06 da SAFX04\) referente o prestador cadastrado na nota fiscal\.

__Tratamento:__

- Se o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR for menor ou igual a 11 posições a TAG deverá ser gerada como <Cpf> </Cpf>;
- Se o campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR for maior que 11 posições a TAG deverá ser gerada como <Cnpj> </Cnpj>\.

__Campo obrigatório__

Formato: 99999999999 ou 99999999999999

Tipo: Numérico

Tamanho: \-

MFS\-36689

__RN136__

__Regra p/ tag </CpfCnpj> __

Tag relacionada ao encerramento dos dados de cadastro do tomador do serviço com o texto fixo__: </CpfCnpj>\.__

__TAG obrigatória\.__

MFS\-36689

__RN137__

__Regra p/ tag <InscricaoMunicipal> </InscricaoMunicipal>__

Identifica a Inscrição Municipal do tomador\. 

Preencher com o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR \(campo 09 da SAFX04\) referente o prestador cadastrado na nota fiscal, sem necessidade de espaços ou zeros para complementar o tamanho do campo\.

__Tratamento:__

- Se o campo INSC\_MUNICIPAL da tabela X04\_PESSOA\_FIS\_JUR não estiver preenchido, emitir uma mensagem padrão de log\.

__Campo obrigatório__

Formato: XXXXXXXXXXXXXXX

Tipo: Alfanumérico

Tamanho: 15

MFS\-36689

__RN138__

__Regra para tag </IdentificacaoTomador> __

Tag relacionada ao encerramento da identificação do tomador do serviço com o texto fixo:__ </IdentificacaoTomador>\.__

__TAG obrigatória\.__

MFS\-36689

__RN139__

__Regra p/ tag <RazaoSocial> </RazaoSocial>__

Identifica a Razão Social do tomador\. 

Preencher com o campo RAZAO\_SOCIAL da tabela X04\_PESSOA\_FIS\_JUR \(campo 05 da SAFX04\) referente ao tomador cadastrado na nota fiscal\.

__Campo obrigatório__

Formato: XXXXXXXXXXXXXXX \(sem limite de tamanho\)

Tipo: Alfanumérico

Tamanho: \-

MFS\-36689

__RN140__

__Regra p/ tag <NomeFantasia> </NomeFantasia>__

Identifica a Nome Fantasia do tomador\. 

Preencher com o campo NOME\_FANTASIA da tabela X04\_PESSOA\_FIS\_JUR \(campo 11 da SAFX04\) referente ao tomador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: XXXXXXXXXXXXXXX \(sem limite de tamanho\)

Tipo: Alfanumérico

Tamanho: \-

MFS\-36689

__RN141__

__Regra p/ tag <RgInscre> </RgInscre>__

Identifica o RG ou a Inscrição Estadual do tomador\. 

Preencher com o campo INSC\_ESTADUAL da tabela X04\_PESSOA\_FIS\_JUR \(campo 08 da SAFX04\) referente o prestador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: XXXXXXXXXXXXXXX \(sem limite de tamanho\)

Tipo: Alfanumérico

Tamanho: \-

MFS\-36689

__RN142__

__Regra p/ tag <Endereco> __

Tag relacionada à abertura dos dados de endereço do prestador do serviço com o texto fixo:__ <Endereco>\.__

__TAG obrigatória\.__

MFS\-36689

__RN143__

__Regra p/ tag <Endereco> </Endereco>__

Identifica o endereço do tomador\. 

Preencher com o campo ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 12 da SAFX04\) referente ao tomador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: XXXXXXXXXXXXXXX \.\.\.\]

Tipo: Alfanumérico

Tamanho: 125

MFS\-36689

__RN144__

__Regra p/ tag <Numero> </Numero>__

Identifica o número do endereço do tomador\. 

Preencher com o campo NUM\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 13 da SAFX04\) referente ao tomador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: XXXXXXXXXX

Tipo: Alfanumérico

Tamanho: 10

MFS\-36689

__RN145__

__Regra p/ tag <Complemento> </Complemento>__

Identifica o complemento do endereço do tomador\. 

Preencher com o campo COMPL\_ENDERECO da tabela X04\_PESSOA\_FIS\_JUR \(campo 14 da SAFX04\) referente ao tomador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: XXXXXXXXXX \.\.\.\]

Tipo: Alfanumérico

Tamanho: 60

MFS\-36689

__RN146__

__Regra p/ tag <Bairro> </Bairro>__

Identifica o bairro do endereço do tomador\. 

Preencher com o campo BAIRRO da tabela X04\_PESSOA\_FIS\_JUR \(campo 15 da SAFX04\) referente ao tomador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: XXXXXXXXXX \.\.\.\]

Tipo: Alfanumérico

Tamanho: 60

MFS\-36689

__RN147__

__Regra p/ tag <CodigoMunicipio> </CodigoMunicipio>__

Identifica o código do município \(IBGE\) do tomador\. 

Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do Município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\)\.

__Tratamento:__

- Se o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR não estiver preenchido, emitir uma mensagem padrão de log\.

__Campo obrigatório__

Formato: 9999999

Tipo: Numérico

Tamanho: 7

MFS\-36689

__RN148__

__Regra p/ tag <Uf> </Uf>__

Identifica a Unidade Federativa do tomador\. 

Preencher com o campo UF da tabela X04\_PESSOA\_FIS\_JUR \(campo 19 da SAFX04\) referente ao tomador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: XX

Tipo: Alfanumérico

Tamanho: 2

MFS\-36689

__RN149__

__Regra p/ tag <CodigoPais> </CodigoPais>__

Identifica o Código do País \(BACEN\) do tomador\. 

Preencher com o campo COD\_PAIS \+ DIG\_VERIFICADOR da tabela PAIS relacionado ao IDENT\_ESTADO do município informado no campo <CodigoMunicipio> \(RN60\)\.

__Campo não obrigatório__

Formato: 9999

Tipo: Numérico

Tamanho: 4

MFS\-36689

__RN150__

__Regra p/ tag <Cep> </Cep>__

Identifica o CEP do tomador\. 

Preencher com o campo CEP da tabela X04\_PESSOA\_FIS\_JUR \(campo 20 da SAFX04\) referente ao tomador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: 99999999

Tipo: Numérico

Tamanho: 8

MFS\-36689

__RN151__

__Regra p/ tag </Endereco> __

Tag relacionada ao encerramento dos dados de endereço do tomador do serviço com o texto fixo:__ </Endereco>\.__

__TAG obrigatória\.__

MFS\-36689

__RN152__

__Regra p/ tag <Contato> __

Tag relacionada à abertura dos dados de contato do tomador do serviço com o texto fixo:__ <Contato>\.__

__TAG não obrigatória\.__

MFS\-36689

__RN153__

__Regra p/ tag <Telefone> </Telefone>__

Identifica o Telefone do tomador\. 

Preencher com o campo DDD \+ TELEFONE da tabela X04\_PESSOA\_FIS\_JUR \(campos 22 e 23 da SAFX04\) referente ao tomador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: XXXXXXXXXXXXXXXXXXXX

Tipo: Alfanumérico

Tamanho: 20

MFS\-36689

__RN154__

__Regra p/ tag <Email> </Email>__

Identifica o E\-mail do tomador\. 

Preencher com o campo E\_MAIL da tabela X04\_PESSOA\_FIS\_JUR \(campo 40 da SAFX04\) referente ao tomador cadastrado na nota fiscal\.

__Campo não obrigatório__

Formato: XXXXXXXXXXXXXXXXXXXX \.\.\.\]

Tipo: Alfanumérico

Tamanho: 80

MFS\-36689

__RN155__

__Regra p/ tag </Contato> __

Tag relacionada ao encerramento dos dados de contato do tomador do serviço com o texto fixo:__ </Contato>\.__

__TAG não obrigatória\.__

MFS\-36689

__RN156__

__Regra para tag </Tomador> __

Tag relacionada ao encerramento das informações do tomador do serviço com o texto fixo:__ </Tomador >\.__

__TAG obrigatória\.__

MFS\-36689

__RN157__

__Regra para tag </Intermediario__> __> __

Tag relacionada à abertura e encerramento das informações do intermediário do serviço com o texto fixo:__ </Intermediario>\.__

__TAG não obrigatória\.__

__Obs\.: Essa TAG não será gerada\.__

MFS\-36689

__RN158__

__Regra p/ tag <RegimeEspecialTributacao> </RegimeEspecialTributacao>__

Identifica se o Tomador possui regime especial de tributação\. 

__Preencher com:__

__“1” \- Microempresa municipal\.__

- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “11\.

__“2” \- Estimativa\.__

- Se o IND\_ISS da tabela ESTABELECIMENTO = “02; OU
- Se não estiver preenchido, verificar se o serviço cadastrado na nota e o município cadastrado no estabelecimento estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “421”, preencher com ‘02’\.

__“3” \- Sociedade de Profissionais\.__

- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “08”\.

__“4” \- Cooperativa\.__

- Se o campo NAT\_PESSOA\_JUR  da tabela ESTABELECIMENTO = “01”\.

__“5” \- Microempresário Individual \(MEI\)\.__

- Não será tratada\.

__“6” \- Microempresário e Empresa de Pequeno Porte \(ME EPP\)\.__

- Não será tratada\.

Se nenhuma das opções anteriores for verdadeira, preencher com:

__“0” \- Não Possui\.__

__Campo obrigatório__

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-36689

__RN159__

__Regra p/ tag <OptanteSimplesNacional> </OptanteSimplesNacional>__

Identifica se o Tomador é optante do Simples Nacional\. 

__Preencher com:__

__“1” \- Sim__\.

- Se o campo IND\_SIMPLES\_NAC da tabela X04\_PESSOA\_FIS\_JUR \(campo 43 da SAFX04\) for igual “S” referente ao tomador cadastrado na nota fiscal\.

Senão, preencher com:

__“2” \- Não__\.

__Campo obrigatório__

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-36689

__RN160__

__Regra p/ tag <IncentivoFiscal> </IncentivoFiscal>__

Identifica se o Tomador possui incentivo fiscal\. 

__Preencher com:__

__“1” \- Sim\.__

- Se o campo IND\_NF\_ESPECIAL da tabela DWT\_DOCTO\_FISCAL \(campo 71 da SAFX07\) for diferente de “N”\.

Senão, preencher com:

__“2” \- Não\.__

__Campo obrigatório__

Formato: 9

Tipo: Numérico

Tamanho: 1

MFS\-36689

__RN161__

__Regra para tag <ItensNotas> __

Tag relacionada à abertura das informações dos itens da nota fiscal com o texto fixo:__ <ItensNotas>\.__

__TAG obrigatória\.__

MFS\-36689

__RN162__

__Regra para tag <item> __

Tag relacionada à abertura das informações do item da nota fiscal com o texto fixo: __<item>\.__

__TAG obrigatória\.__

MFS\-36689

__RN163__

__Regra p/ tag <DescriNfi> </DescriNfi>__

Identifica a descrição do serviço\. 

Preencher com o campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\.

__Campo obrigatório__

Formato: XXXXXXXXXXXXXXXXXXXX \.\.\.\]

Tipo: Alfanumérico

Tamanho: 2000

MFS\-36689

__RN164__

__Regra p/ tag <MedidaNfi> </MedidaNfi>__

Identifica a Unidade de Medida\. 

Preencher com o conteúdo fixo: “UN”\.

__Campo obrigatório__

Formato: XX

Tipo: Alfanumérico

Tamanho: 30

MFS\-36689

__RN165__

__Regra p/ tag <QuantidadeNfi> </QuantidadeNfi>__

Identifica a quantidade do serviço\. 

Preencher com o campo QUANTIDADE da tabela DWT\_ITENS\_SERV \(campo 19 da SAFX09\)\.

__Tratamento:__

- Se o campo QUANTIDADE da tabela DWT\_ITENS\_SERV não estiver preenchido, emitir mensagem padrão de log\.

__Campo obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-36689

__RN166__

__Regra p/ tag <VlrUnitarioNfi> </VlrUnitarioNfi>__

Identifica o valor unitário do item\. 

Preencher com o campo VLR\_UNIT da tabela DWT\_ITENS\_SERV \(campo 20 da SAFX09\)\.

__Tratamento:__

- Se o campo VLR\_UNIT da tabela DWT\_ITENS\_SERV não estiver preenchido, emitir mensagem padrão de log\.

__Campo obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-36689

__RN167__

__Regra p/ tag <DesccondicionalNfi> </DesccondicionalNfi>__

Identifica o desconto condicional do item\. 

Preencher com o campo VLR\_DESC\_CONDIC da tabela DWT\_DOCTO\_FISCAL \(campo 109 da SAFX07\)\.

__Campo não obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-36689

__RN168__

__Regra p/ tag <DescincondicionalNfi> </DescincondicionalNfi>__

Identifica o desconto incondicional do item\. 

Não será tratado, preencher com zero\.

__Campo não obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-36689

__RN169__

__Regra p/ tag <DeducaobaseNfi> </DeducaobaseNfi>__

Preencher com o campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV \(campo 59 da SAFX09\)\.

__Campo não obrigatório__

Formato: 0\.00

Tipo: Valor

Tamanho: 15,2

MFS\-36689

__RN170__

__Regra para tag </item> __

Tag relacionada ao encerramento das informações do item da nota fiscal com o texto fixo:__ </item>\.__

__TAG obrigatória\.__

MFS\-36689

__RN171__

__Regra para tag </ItensNotas> __

Tag relacionada ao encerramento das informações dos itens da nota fiscal com o texto fixo:__ </ItensNotas>\.__

__TAG obrigatória\.__

MFS\-36689

__RN172__

__Regra para tag </InfDeclaracaoPrestacaoServico> __

Tag relacionada ao encerramento das informações da nota fiscal do prestador do serviço com o texto fixo: __</InfDeclaracaoPrestacaoServico>\.__

__TAG obrigatória\.__

MFS\-36689

__RN173__

__Regra para tag </NotaFiscal> __

Tag ao encerramento das informações da nota fiscal do prestador do serviço com o texto fixo:__ </NotaFiscal>\.__

__TAG obrigatória\.__

MFS\-36689

__RN174__

__Regra para tag </LoteNotaFiscal> __

Tag relacionada ao encerramento dos dados da nota fiscal do prestador do serviço com o texto fixo:__ </LoteNotaFiscal>\.__

__TAG obrigatória\.__

MFS\-36689

__RN175__

__Regra p/ tag <QuantidadeNotas> </QuantidadeNotas>__

Identifica a quantidade de notas fiscais do lote\.

Preencher com a quantidade de notas fiscais informadas na TAG <LoteNotaFiscal>\.

__Campo obrigatório__

Formato: 9999999999

Tipo: Numérico

Tamanho: 10

MFS\-36689

__RN176__

__Regra para tag </Declaracao> __

Tag relacionada ao encerramento da formatação do arquivo e que deve receber as informações das notas tomadas declaradas com o texto fixo:__ </Declaracao>\.__

__TAG obrigatória\.__

MFS\-36689

### INCLUSÃO – MANAGER

__CÓD__

__DESCRIÇÃO__

__MFS__

__IM01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo __“Nome do Município”__ deve ficar localizado no grupo __“Municipal”\.__

MFS\-8205

__IM02__

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF __“XX”__ e ao código de município do IBGE igual a __“XXXX”__ __\(Nome do Município\)__, o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de __XXXXXX / XX__\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

MFS\-8205

__IM03__

Código IBGE:__ 26407 – __Município/UF:__ LARANJAL PAULISTA / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-8205

__IM04__

Código IBGE:__ 5203 – __Município/UF:__ CAJOBI / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-11003

__IM05__

Código IBGE:__ 5203 – __Município/UF:__ BARIRI / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-11003

__IM06__

Código IBGE:__ 11300 – __Município/UF:__ CEDRAL / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-17564

__IM07__

Código IBGE:__ 17406 – __Município/UF:__ GUAÍRA / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-17564

__IM08__

Código IBGE:__ 4008 – __Município/UF:__ ASSIS / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-19916

__IM09__

Código IBGE: __16705 – __Município/UF:__ GARÇA / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-20118

__IM10__

Código IBGE: __4503 – __Município/UF:__ AVARÉ / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-20443

__IM11__

Código IBGE: __6002__ __– __Município/UF:__ NOVA ALVORADA DO SUL / MS__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-21664

__IM12__

Código IBGE: __33208 – __Município/UF:__ VERA CRUZ / BA__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-22743

__IM13__

Código IBGE: __3207 – __Município/UF:__ CORUMBÁ / MS__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-23335

__IM14__

Código IBGE: __1004 – __Município/UF:__ ALTINÓPOLIS / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-23555

__IM15__

Código IBGE: __19303 – __Município/UF:__ IBATÉ / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-24242

__IM16__

Código IBGE: __42909 – __Município/UF:__ RIBEIRÃO BONITO / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-34104

__IM17__

Código IBGE: __38907 – __Município/UF:__ PIRAJUÍ / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-36689

__IM18__

Código IBGE: __25706 – __Município/UF:__ JOSÉ BONIFÁCIO / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-53878

__IM19__

Código IBGE: __47502 – __Município/UF:__ SANTA RITA DO PASSA QUATRO / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-62248

__IM20__

Código IBGE: __8305 – __Município/UF:__ TRÊS LAGOAS / MS__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-64386

__IM21__

Código IBGE: __2903 – __Município/UF:__ ARAÇOIABA DA SERRA / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados e/ou prestados deste município\.”\.

MFS\-88149

__IM22__

Código IBGE: __6309 – __Município/UF:__ PARANAÍBA / MS__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados deste município\.”\.

MFS\-88150

__IM23__

Código IBGE: __11102 – __Município/UF:__ CATANDUVA / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados deste município\.”\.

MFS\-88163

__IM24__

Código IBGE: __15509 – __Município/UF:__ FERNANDÓPOLIS / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados deste município\.”\.

MFS\-89608

__IM25__

Código IBGE: __25300 – __Município/UF:__ JAÚ / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados deste município\.”\.

MFS\-511320

__IM26__

Código IBGE: __48005 – __Município/UF:__ SANTO ANTÔNIO DE POSSE / SP__

A descrição funcional do módulo será: “Consiste na entrega das informações sobre os serviços tomados deste município\.”\.

MFS\-526807

__CONSIDERAÇÕES DESTE MODELO:__

1. __Quando uma Regra de Negócio for EXCLUÍDA, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA –  MFS\-XXXX\] __Descrição da Regra de Negócio 01

MFS\-XXXX

1. __Quando uma Regra de Negócio for ALTERADA, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – MFS\-XXXX\]__ Descrição da Regra de Negócio 01

MFS\-XXXX


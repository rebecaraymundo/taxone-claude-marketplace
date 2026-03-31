# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2118

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2118.docx
- **Modificado:** 2024-04-24
- **Tamanho:** 75 KB

---

__SAFX2118__

__Parametrização da Classificação de Serviços\-DES\-BH __

__por Município e/ou por Pessoa Fis/Jur\.__

 Regras de Carga, Exportação e Importação \(Online e Batch\) 

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

Importação » Programação » Execução     

Importação batch » Programação » Execução

Exportação de Dados » Programação » Execução

##### __DOCUMENTO DE REQUISITO__

__MFS__

__Nome__

__Data__

__Descrição__

MFS\-96595

Elisabete Costa

17/01/2023

Definição das regras de importação, Online e Batch, da SAFX2118 – Parametrização da Classificação de Serviços da DES\-BH por Município e/ou por Pessoa Fis/Jur\.

__Essa melhoria/Nova funcionalidade atenderá somente o TAX ONE\.__

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN00

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX2118, que deve ser criada com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

__UF__

A

002

SIM

SIM

__Código do Município__

A

005

SIM

SIM

__Indicador de Pessoa Física/Jurídica__

A

001

NÃO

SIM

__Código da Pessoa Física/Jurídica__

A

014

NÃO

SIM

__Tabela__

A

002

SIM

SIM

__Parâmetro__

A

002

SIM

SIM

__Código do Serviço__

A

004

SIM

SIM

 

MFS\-96595

RN01

__Regra p/ Atendimento da SAFX__

Esta SAFX irá atender dois parâmetros:

__Parametros » Classificação de Serviços » DES\-BH » Municipio__

__Parametros » Classificação de Serviços » DES\-BH » Pessoa Fis\_Jur__

Para atendimento do parâmetro: __Parametros » Classificação de Serviços » DES\-BH » Municipio__

Senão deverá ser preenchida a tabela __PRT\_SERVIC\_MUNIC\_DESBH__

Para atendimento do parâmetro: __Parametros » Classificação de Serviços » DES\-BH » Pessoa Fis\_Jur__

Deverá ser preenchida a tabela __PRT\_SERVICO\_FIS\_JUR\_DESBH__

Se os campos __IND\_FIS\_JUR__ e __COD\_FIS\_JUR__ estiverem preenchidos deverá informa a tabela __PRT\_SERVICO\_FIS\_JUR\_DESBH__\.       

MFS\-96595

RN02

__Campo: UF \- \(UF\)__

O campo “__UF__” deve ser preenchido e de conter todas as UFs cadastradas na tabela __ESTADO__

Se apenas o campo “__UF__” for preenchido e nenhum dos demais campos de critério \(Indicador de Pessoa Física/Jurídica e Código da Pessoa Física/Jurídica, Código de Receita, Tabela, Parâmetro ou Código de Serviço\), for indicado, exibir a mensagem: “Pelo menos um dos campos de critério Indicador de Pessoa Física/Jurídica e Código da Pessoa Física/Jurídica, Código de Receita, Tabela, Parâmetro ou Código de Serviço\) deve estar preenchido”

Tamanho: 002

MFS\-96595

RN03

__Campo: Código do Município \- \(MUNICIPIO\)__

O campo “__Município__” deve permitir a digitação do código do município, de acordo com a tabela  __MUNICIPIO__

O município deve corresponder a UF previamente selecionada\. 

Tamanho: 005

MFS\-96595

RN04

__Campo: Indicador Pessoa Física/Jurídica \- \(IND\_FIS\_JUR\)__

Deve ser preenchido com o Indicador de Pessoa Física/Jurídica relacionada na Tabela de Pessoa Física/Jurídica \(__SAFX04__\), conforme segue:

__1__ \- Fornecedor;

__2__ \- Cliente;

__3__ \- Estabelecimento;

__4__ \- Transportadora;

__5__ \- Cliente/Fornecedor/Transportadora\.

__Obs: Essa informação será obrigatória quando se tratar da importação por Pessoa Física Jurídica__

Obrigatório

Tamanho: 001

MFS\-96595

RN05

__Campo Código da Pessoa Física/Jurídica \- \(COD\_FIS\_JUR\)__

Deve ser aceito pessoa jurídica cadastrada na __SAFX04__ 

__Validações: __

Caso a pessoa não esteja cadastrada na SAFX04, exibir a mensagem: __“Registro não cadastrado na Tabela de Arquivo de Cadastro de Pessoas Físicas/Jurídicas“__

Apenas pessoas fis/jur que pertençam a __UF__ e __Município__ selecionados anteriormente\.

__Obs: Essa informação será obrigatória quando se tratar da importação por Pessoa Física Jurídica__

Obrigatório

Tamanho: 014

MFS\-96595

RN06

__Campo: Tabela \- \(COD\_TABELA\_DES\)__

Este campo é recuperado da tabela __COD\_TABELA\_DES \(View DES\_BH\_TABELA\_V\)  
__

Quando preenchido, o campo “__Tabela__”  as informações desse campo deve conter uma das seguintes opções: 

__01 \- Tipo de Negócio__

__02 \- Exigibilidade do ISSQN__

__03 \- Regime Especial de Tributação__

__04 \- Situação Especial de Responsabilidade__

__05 \- Motivo de não Retenção__

O campo Tabela deve conter as opções de “__01__ a __05__” senão emitir a mensagem “__Tabela não corresponde à opção informada__”

Tamanho: 002

MFS\-96595

RN07

__Campo: Parâmetro \- \(COD\_PARAM\_DES\)__

Este campo é recuperado da tabela __COD\_PARAM\_DES \(View DES\_BH\_PARAM\_V\)  
__

O parâmetro deve corresponder às opções de cada tabela informada, caso contrário emitir a mensagem “__Código de parâmetro inválido, não corresponde a tabela informada”__

Quando o campo __Tabela__ estiver preenchido com a opção __“01 \- Tipo de Negócio”__, o campo Parametro deve conter as seguintes opções:

__01__ \- Exclusivamente Prestação de Serviços

__02__ \- Prestação de Serviços c/ Dedução

__03__ \- Prestação de Serviços c/ Reembolso/Repasse

__04__ \- Exclusivamente Reembolso/Repasse

__05__ \- Vendas de Mercadorias/Transporte Intermunicipal

__06__ \- Prestação de Serviços c/ Venda de Mercadorias/Transporte Intermunicipal

__07__ \- Devolução/Simples Remessa/Entrada

__08__ \- Não Incidência    

                                                                                                                                                                                                                                                                                                                                                                                                                                              Quando o campo __Tabela__ estiver preenchido com a opção __“02 \- Exigibilidade do ISSQN”__, o campo Parametro deve conter as seguintes opções:

__01 __\- Exigível

__02__ \- Exportação

__03__ \- Imunidade Tributária

__04__ \- Isenta do ISS em BH

__05__ \- Exigibilidade Suspensa por Decisão Judicial

__06 __\- Não Incidência

__07__ \- Vendas/Transporte Intermunicipal  

                                                                                                                                                                                                                                                                                                                                                                                                                             

Quando o campo __Tabela__ estiver preenchido com a opção __“03 \- Regime Especial de Tributacao”__, o campo Parametro conter as seguintes opções:

__01__ \- Regra Geral

__02__ \- Regime de Estimativa

__03__ \- SPL \- Sociedade de Profissionais Liberais

__04__ \- Cooperativa

__05__ \- Não disponível na DES 3\.0

__06__ \- Construção Civil

__07__ \- Propaganda e Publicidade/Intermediação

__08__ \- Agenciamento de Turismo/Administração de Fundos

__09__\- ME ou EPP optante pelo Simples Nacional

__10__ \- MEI – Microempreendedor Individual

__11__ \- Vendas/Transporte Intermunicipal

__12__ \- Não Incidência

                                                                                                                                                                                                                                                                                                                                                                                          Quando o campo __Tabela__ estiver preenchido com a opção __“04 \- Situacao Especial de Responsabilidade”__, o campo Parametro conter as seguintes opções:

__01__ \- Exclusivamente Prestação de Serviços

__02__ \- Prestação de Serviços c/ Dedução

__03__ \- Construção Civil

__04 __\- Agenciamento de Turismo/Administração de Fundos

__05__ \- Propaganda e Publicidade/Intermediação

__06__ \- Propaganda e Publicidade/Intermediação \- Isento

__07__ \- Não Incidência/Reembolso/Repasse

                                                                                                                                                                                                                                                                                                                                                                                                                              Quando o campo __Tabela__ estiver preenchido com a opção __“05 \- Motivo de não Retenção”__, o campo Parametro deve conter as seguintes opções:

__01__ \- Não retido

__02__ \- Imunidade Tributária

__03__ \- Regime de Estimativa em BH

__04__ \- Isenta do ISSQN em BH

__05__ \- Tributacao fora de BH

__06__ \- SPL \- Sociedade de Profissionais Liberais

__07__ \- Incentivador Cultural em BH

__08__ \- Exigibilidade do ISSQN Suspensa por Decisão Judicial

__09__ \- Profissional Autônomo inscrito na PBH

__10__ \- Não Incidência/Reembolso/Repasse

__11__ \- Não disponível na DES 3\.0

__12__ \- Cartórios

__13__ \- PROEMP

__14__ \- MEI – Microempreendedor Individual

__15__ \- Desobrigado legalmente

__16__ \- ISSQN Retido

__17__ \- Exportação   

Tamanho: 002

MFS\-96595

RN08

__Campo: Código do Serviço \- \(COD\_SERVICO\)__

O campo Serviços deve permitir que o usuário marque quantos serviços forem necessários para a classificação desejada\. O campo deve exibir o campo __COD\_SERVICO__ da tabela __X2018\_SERVICOS__\.

Exibir apenas os serviços que ainda não estejam parametrizados para a UF, Município, Pessoa Fis/Jur e Tabela selecionados\.

Tamanho: 004

MFS\-96595

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


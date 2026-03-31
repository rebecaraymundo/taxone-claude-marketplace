# MTZ_GIM_RN_Geracao_Arquivo_Magnetico

- **Fonte:** MTZ_GIM_RN_Geracao_Arquivo_Magnetico.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 74 KB

---

THOMSON REUTERS

GIM\-RN

Geração do Arquivo Magnético

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4229

Julyana Perrucini

Essa OS tem como objetivo alterar a tela de geração da GIM\-RN permitindo o ajuste na descrição dos campos dos registros 15 a 19 e inclusão do campo 34 do registro 15\.

CH28462\_2014

Julyana Perrucini

<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a><a id="OLE_LINK9"></a><a id="OLE_LINK14"></a><a id="OLE_LINK15"></a>Este documento tem como objetivo alterar a geração do campo Valor Contábil das Operações p/ Substituição Tributária do Registro 3\.

CH28710\_2014

Julyana Perrucini

Este documento tem como objetivo documentar o campo 31\-Substituto pelas Saídas – Prest\. de Serviços e alterar a geração do campo 32\-Substituto pelas Saídas Mercadorias do Registro 14\.

CH664\_2015

Julyana Perrucini

Este documento tem como objetivo alterar a geração do campo Valor Contábil das Operações p/ Substituição Tributária do 2 Registro \- Entradas do Estado – \[07\] considerando o valor contábil do item da nota fiscal para operações com ST e valor total da nota fiscal caso não possua itens, além disso, será alterada a geração dos campos \[29\] e \[30\] do 13º Registro – ICMS do Período \(Normal / Substituição\) para que sejam preenchidos com zero, conforme a regra de validação da GIM\.

CH664\-A\_2015

Julyana Perrucini

Este documento tem como objetivo alterar a geração do campo Valor Contábil das Operações p/ Substituição Tributária do Registro 2 \- Entradas do Estado – \[07\] e do Registro 3 \- Entradas de Outros Estados – \[08\] considerando o valor contábil do Resumo das Operações de CFOP/UF mais a parametrização de CFOP da GIM\-RN\.

CH15306\_2015

Julyana Perrucini

Este documento tem como objetivo alterar a geração do 10º Registro, 11º Registro e 12º Registro\.

CH15333\_2015

Julyana Perrucini

Este documento tem como objetivo alterar a geração do campo 34 do 15º Registro\.

CH27989\_2015

Julyana Perrucini

<a id="OLE_LINK35"></a><a id="OLE_LINK36"></a><a id="OLE_LINK37"></a>Este documento tem como objetivo alterar a geração do campo 32 do 14º Registro e o campo 34 do 15º Registro\.

CH27989\-A\_2015

Lara Aline

Este documento tem como objetivo incluir a regra de recuperação dos documentos fiscais por Data Fiscal\. \(RN31\)

CH27989\-B\_2015

Julyana Perrucini

Este documento tem como objetivo alterar a geração do campo Valor Contábil das Operações p/ Substituição Tributária do Registro 6 – Saídas para o Estado – \[11\]\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral:__

As regras serão aplicadas para IEU conforme documento MTZ\-Geracao GIM RN por IEU\.doc

<OS>\.

RN01

__REGISTRO 15 – ICMS do Período \(Substituto pelas Entradas\) – CAMPO 33__

__Origem: __Módulo Estadual >> GIM\-RN >> Obrigações >> Geração dos Registros >> Guia Informativa Mensal do ICMS – Rio Grande do Norte\.

__Tratamento:__

Buscar a informação inserida no campo Substituto não Retido pelo Remetente \[Reg\.33\], devendo gravar no arquivo magnético e no relatório Espelho da GIM\.

OS4229

RN02

__REGISTRO 15 – ICMS do Período \(Substituto pelas Entradas\) – CAMPO 34__

__ \[ALTERADA – CH15333\_2015/ CH27989\_2015\]__

__Origem: __SAFX07/08 \- Nota de Entrada de mercadorias com regime de substituição tributária, Parâmetro de Substituição Tributária\.

Buscar a informação inserida no campo Vlr\. ICMSS do item do documento fiscal de entrada que tenha valor de substituição tributária campo \(VLR\_TRIBUTO\_ICMSS da tabela DWT\_ITENS\_MERC\) quando o campo Indicador do ICMSS for igual a Substituto \(IND\_FORNEC\_ICMSS da tabela DWT\_ITENS\_MERC = 1\) e que o CFOP ou CFOP/Natureza esteja parametrizado no módulo GIM\-RN em Parâmetros >> Subst\. Tributária, devendo gravar no arquivo magnético e no relatório Espelho da GIM\.

__Tratamento:__

- Somar os valores por CFOP ou CFOP/Extensão de acordo com a parametrização feita em Estadual >> GIM\-RN >> Parâmetros >> Substituição Tributária >> Por CFOP ou Por Extensão CFOP\.
- Devem considerar somente os CFOPs da parametrização Tipo 34 – CFOP/Ext\. CFOP de NF Entrada – Mercadorias c/ Regime de Subst\. Tributária para preenchimento deste campo\.

*Observação:* 

- Para restante da seleção, manter tratamento atual, inclusive a mensagem de log quando não houver a parametrização\.
- A responsabilidade é do usuário quanto o CFOP correto a ser levado o valor para o registro\.

OS4229

CH15333\_2015

CH27989\_2015

RN03

__REGISTRO 16 – ICMS do Período \(Ativo Permanente: Crédito Normal/Consumo\) – CAMPO 35__

__Origem: __Módulo Estadual >> GIM\-RN >> Obrigações >> Geração dos Registros >> Guia Informativa Mensal do ICMS – Rio Grande do Norte\.

__Tratamento:__

Buscar a informação inserida no campo Diferença de Alíquotas: Ativo Permanente \[Reg\. 35\], devendo gravar no arquivo magnético e no relatório Espelho da GIM\.

OS4229

RN04

__REGISTRO 16 – ICMS do Período \(Ativo Permanente: Crédito Normal/Consumo\) – CAMPO 36__

__Origem: __Módulo Estadual >> GIM\-RN >> Obrigações >> Geração dos Registros >> Guia Informativa Mensal do ICMS – Rio Grande do Norte\.

__Tratamento:__

Buscar a informação inserida no campo Diferença de Alíquotas: Consumo \[Reg\. 36\], devendo gravar no arquivo magnético e no relatório Espelho da GIM\.

OS4229

RN05

__REGISTRO 17 – ICMS do Período \(Serviço de Transporte / Diferença de Alíquotas\) – CAMPO 37__

__Origem: __Módulo Estadual >> GIM\-RN >> Obrigações >> Geração dos Registros >> Guia Informativa Mensal do ICMS – Rio Grande do Norte\.

__Tratamento:__

Buscar a informação inserida no campo Dif\. de Alíquotas: Serv\. de Transporte – Ativo \[Reg\. 37\], devendo gravar no arquivo magnético e no relatório Espelho da GIM\.

OS4229

RN06

__REGISTRO 17 – ICMS do Período \(Serviço de Transporte / Diferença de Alíquotas\) – CAMPO 38__

__Origem: __Módulo Estadual >> GIM\-RN >> Obrigações >> Geração dos Registros >> Guia Informativa Mensal do ICMS – Rio Grande do Norte\.

__Tratamento:__

Buscar a informação inserida no campo Dif\. de Alíquotas: Serv\. de Transporte – Consumo \[Reg\. 38\], devendo gravar no arquivo magnético e no relatório Espelho da GIM\.

OS4229

RN07

__REGISTRO 18 – ICMS do Período \(Diferimento: Importação / Regime Especial\) – CAMPO 39__

__Origem: __Módulo Estadual >> GIM\-RN >> Obrigações >> Geração dos Registros >> Guia Informativa Mensal do ICMS – Rio Grande do Norte\.

__Tratamento:__

Buscar a informação inserida no campo Estorno AEAC–Anexo VIII do SCANC \[Reg\. 39\], devendo gravar no arquivo magnético e no relatório Espelho da GIM\.

OS4229

RN08

__REGISTRO 18 – ICMS do Período \(Diferimento: Importação / Regime Especial\) – CAMPO 40__

__Origem: __Módulo Estadual >> GIM\-RN >> Obrigações >> Geração dos Registros >> Guia Informativa Mensal do ICMS – Rio Grande do Norte\.

__Tratamento:__

Buscar a informação inserida no campo Estorno B100\-Anexo VIII do SCANC \[Reg\. 40\], devendo gravar no arquivo magnético e no relatório Espelho da GIM\.

OS4229

RN09

__REGISTRO 19 – ICMS do Período \(FECOP – Normal / Substituto\) – CAMPO 41__

__Origem: __Módulo Estadual >> GIM\-RN >> Obrigações >> Geração dos Registros >> Guia Informativa Mensal do ICMS – Rio Grande do Norte\.

__Tratamento:__

Buscar a informação inserida no campo FECOP – Apuração \[Reg\. 41\], devendo gravar no arquivo magnético e no relatório Espelho da GIM\.

OS4229

RN10

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>__REGISTRO 19 – ICMS do Período \(FECOP – Normal / Substituto\) – CAMPO 42__

__Origem: __Módulo Estadual >> GIM\-RN >> Obrigações >> Geração dos Registros >> Guia Informativa Mensal do ICMS – Rio Grande do Norte\.

__Tratamento:__

Buscar a informação inserida no campo FECOP – Substituto \[Reg\. 42\], devendo gravar no arquivo magnético e no relatório Espelho da GIM\.

OS4229

RN11

__REGISTRO 3 – Entradas de Outros Estados – \[08\] – CAMPO __<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a><a id="OLE_LINK5"></a><a id="OLE_LINK6"></a>__Valor Contábil das Operações p/ Substituição Tributária__

__Origem: __Resumo de Operações – Por CFOP/UF, Parâmetro de Substituição Tributária\.

Os valores correspondentes ao preenchimento deste campo devem compreender o Estabelecimento e o período Mês/Ano preenchidos na tela de geração dos registros\.

__\[ALTERADA – CH664\-A\_2015\]__

__Tratamento:__

Buscar a informação do campo “Valor Contábil” do Resumo de Operações por CFOP/UF, localizado em Estadual >> Obrigações Acessórias >> Relatórios >> Resumo das Operações >> CFOP/UF, dos CFOPs ou CFOPs/Naturezas iniciados com “2” que estiverem parametrizados para Tipo 245 – CFOP/Ext\. Considerados para a Entrada de Substituição tributária, parâmetro este localizado em Estadual >> GIM\-RN >> Parâmetros >> Substituição Tributária\.

CH28710\_2014

CH664\-A\_2015

RN12

__REGISTRO 14 – ICMS do Período \(Substituto pelas Saídas – Prestações de Serviço / Mercadorias\) – \[31\] – CAMPO Substituto pelas Saídas – Prest\. de Serviços__

__Origem: __SAFX08, Parâmetro de Substituição Tributária\.

Buscar a informação do campo “Vlr\. ICMSS” do item do documento fiscal de saída de mercadoria \(campo VLR\_TRIBUTO\_ICMSS da tabela DWT\_ITENS\_MERC\)\.

__Tratamento:__

- Somar os valores por CFOP ou CFOP/Extensão de acordo com a parametrização feita em Estadual >> GIM\-RN >> Parâmetros >> Substituição Tributária >> Por CFOP ou Por Extensão CFOP\.
- Devem considerar somente os CFOPs da parametrização Tipo 51 – CFOP/Ext\. CFOP de NF Saída – Prestação de Serviço c/ Regime de Subst\. Tributária para preenchimento deste campo\.

*Observação:* 

- Para restante da seleção, manter tratamento atual, inclusive a mensagem de log quando não houver a parametrização\.
- A responsabilidade é do usuário quanto o CFOP correto a ser levado o valor para o registro\.

CH28710\_2014

RN13

__REGISTRO 14 – ICMS do Período \(Substituto pelas Saídas – Prestações de Serviço / Mercadorias\) – \[32\] – CAMPO Substituto pelas Saídas Mercadorias__

__\[ALTERADA – CH27989\]__

__Origem: __SAFX08, Parâmetro de Substituição Tributária\.

__\[ALTERADA – CH28710\_2014\]__

Buscar a informação do campo “Vlr\. ICMSS” do item do documento fiscal de saída de mercadoria \(campo VLR\_TRIBUTO\_ICMSS da tabela DWT\_ITENS\_MERC\) quando o campo Apropria estiver marcado \(campo IND\_CRED\_ICMSS da tabela DWT\_ITENS\_MERC = S\), deduzindo o valor das notas fiscais de entrada de devolução \(campo NORM\_DEV da tabela DWT\_ITENS\_MERC = 2\) cujo campo Apropria estiver marcado \(campo IND\_CRED\_ICMSS da tabela DWT\_ITENS\_MERC = S\) e o campo Indicador do ICMSS for diferente de Substituto \(IND\_FORNEC\_ICMSS da tabela DWT\_ITENS\_MERC <> 1\)\. Portanto o resultado com a diferença do calculo deverá ser gerado no campo 32 \- Substituto pelas Saídas Mercadorias\.

__Tratamento:__

- Somar os valores por CFOP ou CFOP/Extensão de acordo com a parametrização feita em Estadual >> GIM\-RN >> Parâmetros >> Substituição Tributária >> Por CFOP ou Por Extensão CFOP\.
- Deve considerar somente a parametrização Tipo 35 – CFOP/Ext\. CFOP de NF Saída – Mercadorias c/ Regime de Subst\. Tributária \(Operações Internas\) para preenchimento deste campo\.
- Para as notas de entrada de devolução que serão deduzidas, os CFOP ou CFOP/Extensão deverão ser parametrizados com o Tipo 34 – CFOP/Ext\. CFOP de NF Entrada – Mercadorias c/ Regime de Subst\. Tributária\.

*Observação:* 

- Para restante da seleção, manter tratamento atual, inclusive a mensagem de log quando não houver a parametrização\.
- A responsabilidade é do usuário quanto o CFOP correto a ser levado o valor para o registro\.

CH28710\_2014

CH27989\_2015

RN14

__REGISTRO 2 – Entradas do Estado – \[07\] – CAMPO Valor Contábil das Operações p/ Substituição Tributária__

__Origem: __Resumo de Operações – Por CFOP/UF, Parâmetro de Substituição Tributária\.

Os valores correspondentes ao preenchimento deste campo devem compreender o Estabelecimento e o período Mês/Ano preenchidos na tela de geração dos registros\.

__\[ALTERADA – CH664\-A\_2015\]__

__Tratamento:__

Buscar a informação do campo “Valor Contábil” do Resumo de Operações por CFOP/UF, localizado em Estadual >> Obrigações Acessórias >> Relatórios >> Resumo das Operações >> CFOP/UF, dos CFOPs ou CFOPs/Naturezas iniciados com “1” que estiverem parametrizados para Tipo Tipo 34 – CFOP/Ext\. CFOP de NF Entrada – Mercadorias c/ Regime de Subst\. Tributária, parâmetro este localizado em Estadual >> GIM\-RN >> Parâmetros >> Substituição Tributária\.

CH664\_2015

CH664\-A\_2015

RN15

__REGISTRO 13 – ICMS do Período \(Normal / Substituição\) – CAMPO \[29\]__

Fixar zero para esse campo do registro\.

CH664\_2015

RN16

__REGISTRO 13 – ICMS do Período \(Normal / Substituição\) – CAMPO \[30\]__

Fixar zero para esse campo do registro\.

CH664\_2015

RN17

__REGISTRO 10 – Débito do Imposto – \[15\] – CAMPO Por saídas com débito do imposto__

__Origem: __Lançamentos Complementares do Resumo da Apuração do ICMS\.

Buscar a informação de acordo com o estabelecimento e período de apuração inseridos na tela de geração do arquivo magnético, do campo “Valor” da aba Lançamento de Valores, da tela de Lançamentos Complementares do Resumo da Apuração, localizada em Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

__Tratamento:__

- Agrupar e somar os valores quando o campo Classe Lançamento da aba Lançamento de Valores for igual a “611” \(Vlr das Saidas/Prestacoes com Debito do Imposto\)\.

CH15306\_2015

RN18

__REGISTRO 10 – Débito do Imposto – \[16\] – CAMPO Outros débitos__

__Origem: __Lançamentos Complementares do Resumo da Apuração do ICMS\.

Buscar a informação de acordo com o estabelecimento e período de apuração inseridos na tela de geração do arquivo magnético, do campo “Valor” da aba Lançamento de Valores, da tela de Lançamentos Complementares do Resumo da Apuração, localizada em Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

__Tratamento:__

- Agrupar e somar os valores quando o campo Classe Lançamento da aba Lançamento de Valores for igual a “585” \(Valor Total de Outros Debitos de ICMS\)\.

CH15306\_2015

RN19

__REGISTRO 10 – Débito do Imposto – \[17\] – CAMPO Estornos de créditos__

__Origem: __Lançamentos Complementares do Resumo da Apuração do ICMS\.

Buscar a informação de acordo com o estabelecimento e período de apuração inseridos na tela de geração do arquivo magnético, do campo “Valor” da aba Lançamento de Valores, da tela de Lançamentos Complementares do Resumo da Apuração, localizada em Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

__Tratamento:__

- Agrupar e somar os valores quando o campo Classe Lançamento da aba Lançamento de Valores for igual a “579” \(Valor Total dos Estornos de Creditos de ICMS\)\.

CH15306\_2015

RN20

__REGISTRO 10 – Débito do Imposto – \[18\] – CAMPO Total__

__Origem: __Lançamentos Complementares do Resumo da Apuração do ICMS\.

Buscar a informação de acordo com o estabelecimento e período de apuração inseridos na tela de geração do arquivo magnético, do campo “Valor” da aba Lançamento de Valores, da tela de Lançamentos Complementares do Resumo da Apuração, localizada em Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

__Tratamento:__

- Agrupar e somar os valores quando o campo Classe Lançamento da aba Lançamento de Valores for igual a “578” \(Valor Total dos Debitos\)\.

CH15306\_2015

RN21

__REGISTRO 11 – Crédito do Imposto – \[19\] – CAMPO Por entradas com crédito do imposto__

__Origem: __Lançamentos Complementares do Resumo da Apuração do ICMS\.

Buscar a informação de acordo com o estabelecimento e período de apuração inseridos na tela de geração do arquivo magnético, do campo “Valor” da aba Lançamento de Valores, da tela de Lançamentos Complementares do Resumo da Apuração, localizada em Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

__Tratamento:__

- Agrupar e somar os valores quando o campo Classe Lançamento da aba Lançamento de Valores for igual a “612” \(Vlr Entradas Aquisicoes com Credito do Imposto\)\.

CH15306\_2015

RN22

__REGISTRO 11 – Crédito do Imposto – \[20\] – CAMPO Outros créditos__

__Origem: __Lançamentos Complementares do Resumo da Apuração do ICMS\.

Buscar a informação de acordo com o estabelecimento e período de apuração inseridos na tela de geração do arquivo magnético, do campo “Valor” da aba Lançamento de Valores, da tela de Lançamentos Complementares do Resumo da Apuração, localizada em Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

__Tratamento:__

- Agrupar e somar os valores quando o campo Classe Lançamento da aba Lançamento de Valores for igual a “584” \(Valor Total de Outros Creditos de ICMS\)\.

CH15306\_2015

RN23

__REGISTRO 11 – Crédito do Imposto – \[21\] – CAMPO Estornos de débitos __

__Origem: __Lançamentos Complementares do Resumo da Apuração do ICMS\.

Buscar a informação de acordo com o estabelecimento e período de apuração inseridos na tela de geração do arquivo magnético, do campo “Valor” da aba Lançamento de Valores, da tela de Lançamentos Complementares do Resumo da Apuração, localizada em Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

__Tratamento:__

- Agrupar e somar os valores quando o campo Classe Lançamento da aba Lançamento de Valores for igual a “581” \(Vlr Total Estornos Deb ICMS\)\.

CH15306\_2015

RN24

__REGISTRO 11 – Crédito do Imposto – \[22\] – CAMPO Subtotal__

__Origem: __Lançamentos Complementares do Resumo da Apuração do ICMS\.

Buscar a informação de acordo com o estabelecimento e período de apuração inseridos na tela de geração do arquivo magnético, do campo “Valor” da aba Lançamento de Valores, da tela de Lançamentos Complementares do Resumo da Apuração, localizada em Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

__Tratamento:__

- Agrupar e somar os valores quando o campo Classe Lançamento da aba Lançamento de Valores for igual a “580” \(Sub\-Total\)\.

CH15306\_2015

RN25

__REGISTRO 11 – Crédito do Imposto – \[23\] – CAMPO Saldo credor__

__Origem: __Lançamentos Complementares do Resumo da Apuração do ICMS\.

Buscar a informação de acordo com o estabelecimento e período de apuração inseridos na tela de geração do arquivo magnético, do campo “Valor” da aba Lançamento de Valores, da tela de Lançamentos Complementares do Resumo da Apuração, localizada em Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

__Tratamento:__

- Agrupar e somar os valores quando o campo Classe Lançamento da aba Lançamento de Valores for igual a “613” \(Vlr da Apuracao Saldo Credor do Periodo Anterior\)\.

CH15306\_2015

RN26

__REGISTRO 11 – Crédito do Imposto – \[24\] – CAMPO Total__

__Origem: __Lançamentos Complementares do Resumo da Apuração do ICMS\.

Buscar a informação de acordo com o estabelecimento e período de apuração inseridos na tela de geração do arquivo magnético, do campo “Valor” da aba Lançamento de Valores, da tela de Lançamentos Complementares do Resumo da Apuração, localizada em Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

__Tratamento:__

- Agrupar e somar os valores quando o campo Classe Lançamento da aba Lançamento de Valores for igual a “618” \(Valor Total dos Creditos\)\.

CH15306\_2015

RN27

__REGISTRO 12 – Apuração dos Saldos – \[25\] – CAMPO Saldo devedor__

__Origem: __Lançamentos Complementares do Resumo da Apuração do ICMS\.

Buscar a informação de acordo com o estabelecimento e período de apuração inseridos na tela de geração do arquivo magnético, do campo “Valor” da aba Lançamento de Valores, da tela de Lançamentos Complementares do Resumo da Apuração, localizada em Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

__Tratamento:__

- Agrupar e somar os valores quando o campo Classe Lançamento da aba Lançamento de Valores for igual a “617” \(Saldo Devedor\)\.

CH15306\_2015

RN28

__REGISTRO 12 – Apuração dos Saldos – \[26\] – CAMPO Deduções__

__Origem: __Lançamentos Complementares do Resumo da Apuração do ICMS\.

Buscar a informação de acordo com o estabelecimento e período de apuração inseridos na tela de geração do arquivo magnético, do campo “Valor” da aba Lançamento de Valores, da tela de Lançamentos Complementares do Resumo da Apuração, localizada em Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

__Tratamento:__

- Agrupar e somar os valores quando o campo Classe Lançamento da aba Lançamento de Valores for igual a “616” \(Saldo Devedor\)\.

CH15306\_2015

RN29

__REGISTRO 12 – Apuração dos Saldos – \[27\] – CAMPO Imposto a recolher__

__Origem: __Lançamentos Complementares do Resumo da Apuração do ICMS\.

Buscar a informação de acordo com o estabelecimento e período de apuração inseridos na tela de geração do arquivo magnético, do campo “Valor” da aba Lançamento de Valores, da tela de Lançamentos Complementares do Resumo da Apuração, localizada em Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

__Tratamento:__

- Agrupar e somar os valores quando o campo Classe Lançamento da aba Lançamento de Valores for igual a “614” \(Vlr Apuracao Imposto a Recolher\)\.

CH15306\_2015

RN30

__REGISTRO 12 – Apuração dos Saldos – \[28\] – CAMPO Saldo credor p/ período seguinte__

__Origem: __Lançamentos Complementares do Resumo da Apuração do ICMS\.

Buscar a informação de acordo com o estabelecimento e período de apuração inseridos na tela de geração do arquivo magnético, do campo “Valor” da aba Lançamento de Valores, da tela de Lançamentos Complementares do Resumo da Apuração, localizada em Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única\.

__Tratamento:__

- Agrupar e somar os valores quando o campo Classe Lançamento da aba Lançamento de Valores for igual a “615” \(Vlr Apur\. Sld Credor a Transp\. p/ Periodo Seguinte\)\.

CH15306\_2015

RN31

__REGISTRO 2 a 21 \- Todos os registros da GIM\-RN \(Campos 07 a 71\)__

Considerar os documentos fiscais cuja data fiscal seja dentro do período de geração dos registros da GIM\-RN\.

CH27989\-A\_2015

RN32

__REGISTRO 6 – Saídas para o Estado – \[11\] – CAMPO Valor Contábil das Operações p/ Substituição Tributária__

__Origem: __Resumo de Operações – Por CFOP/UF, Parâmetro de Substituição Tributária\.

Os valores correspondentes ao preenchimento deste campo devem compreender o Estabelecimento e o período Mês/Ano preenchidos na tela de geração dos registros\.

__\[ALTERADA – CH27989\-B\_2015\]__

__Tratamento:__

Buscar a informação do campo “Valor Contábil” do Resumo de Operações por CFOP/UF, localizado em Estadual >> Obrigações Acessórias >> Relatórios >> Resumo das Operações >> CFOP/UF, dos CFOPs ou CFOPs/Naturezas iniciados com “5” que estiverem parametrizados para Tipo 35 – CFOP/Ext\. de NF Saída – Mercadorias c/ Regime de Subst\. Tributária \(Operações Internas\) Tipo 246 – CFOP/Ext\. considerados para Saída de Substituição Tributária, parâmetro este localizado em Estadual >> GIM\-RN >> Parâmetros >> Substituição Tributária\.

CH27989\-B\_2015

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


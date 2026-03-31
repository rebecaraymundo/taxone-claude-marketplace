# MTZ_DIME_SC_Obrigacoes_Informacoes_Iniciais_da_Declaracao

- **Fonte:** MTZ_DIME_SC_Obrigacoes_Informacoes_Iniciais_da_Declaracao.docx
- **Modificado:** 2026-02-23
- **Tamanho:** 79 KB

---

 

THOMSON REUTERS

Informações Iniciais da Declaração

__Localização__: Menu Estadual, Módulo: DIME\-SC, menu Obrigações 🡪 Informações Iniciais da Declaração

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4502

Julyana Perrucini

Documentação da tela de Informações Iniciais da Declaração\.

OS4581

Marcelo Silva

Incluir Item no parâmetro Transferência Crédito, criar campo item 18, 19 e 997 do registro 41 do Quadro 41\. 

CH11707\_2015

Julyana Perrucini

Este documento tem como objetivo incluir a geração para Simples Nacional na DIME\-SC de acordo com a publicação da Portaria n° 147, de 19 de maio de 2015\.

MFS3005

Atendimento à Portaria SEF SC 04/2016

Alterações da DIME para atendimento à Portaria SEF SC 04/2016 com informações da apuração do ICMS Difal UF Orig/Dest \(EC 87/2015\)\.  Ver Quadro 13, campo “100\-Pagamentos Antecipados”

MFS10580

Portaria SEF nº 070/2017

Atualização Legal da Portaria SEF nº 070/2017 \(Quadro 09 e Quadro 14\)

MFS11473

Andréa Rocha

Atualização Legal da versão 15 de 24/05/2017 do Manual de Orientação

MFS13230

Andréa Rocha

Atualização Legal da Portaria SEF nº 230/2017 \(Quadro 14\)

MFS24064

Andréa Rocha

Atualização Legal da Portaria SEF nº 7, de 10 de janeiro de 2019 \(Quadro 11\)

MFS28607

Aline Melo

Criação de parâmetro para tratar cálculo do Item 010, Quadro 41\.

MFS38324

Vânia Mattos

Atualização legal Portaria SEF 148/2020: Exibir mensagem de aviso sobre o campo 021 do Quadro 51

MFS45748

Liliane Assaf

Inclusão do campo* “Remessas para Fins de Exportação \(Exportação Indireta\)*” no Quadro 41

MFS85008

Aline Melo

Ajuste na redação dos campos 065 e 073 do Quadro 11\.

MFS86547

Andréa Rocha

Criação <a id="_Hlk106017341"></a>dos campos para informar a Ident\. Regime Especial e o valor do crédito para o quadro 46, com origem igual a 14\.

MFS91937

Aline Melo

Criação do Quadro 16 em atendimento a Portaria SEF n° 314/2022\.

MFS93956

Liliane Assaf

Portaria 314/2022 \- Inclusão do Quadro 85

MFS520953

Andréa Rocha

Criação do campo 116 do Quadro 11, referentes às alterações da Portaria SEF n° 059/2023

MFS619745

Liliane Assaf

Atendimento à Portaria SEF n° 055/2024 para gerações a partir de maio/2024\.

\- Alteração do item 065

\-  Inclusão do item 074 \- VLR\_OUT\_DEB\_11\_074 

\-  Inclusão do item 899 \- VLR\_DEB\_ESP\_11\_899

Sumário

[1\.	Regras dos Campos	3](#_Toc382488202)

# <a id="_Toc350763252"></a><a id="_Toc382488202"></a>Regras dos Campos 

__Localização da tela:__ Estadual\\ DIME\-SC\\ Obrigações\\ Informações Iniciais da Declaração

__Título da tela: __Código DIME\-SC \-__ __Informações Iniciais da Declaração

__Considerações Gerais: __Parametrização da tela obrigatória para geração do arquivo magnético\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Quadro 00, campo:

Tipo de Declaração

ComboBox

S

S

\-

Neste campo serão exibidas as opções de enquadramento do tipo de declaração do contribuinte\.

__\[ALTERADA – CH11707\_2015\]__

__Conteúdo:__

- Normal;
- Encerramento de Atividades;
- Saída do regime de estimativa fiscal;
- Enquadramento no Simples Nacional\.

CH11707\_2015

Quadro 00, campo:

Transferência de créditos no período

ComboBox

S

S

\- 

Neste campo serão exibidas as opções quando houver ou não transferência de créditos\.

__Conteúdo:__

1 – Não apurou ou reservou nem recebeu créditos;

2 – Apurou ou reservou créditos;

3 – Recebeu créditos;

4 – Apurou ou reservou e recebeu créditos;

5 – Apuração e reserva crédito sistema cooperativo agropecuário\. 

__Tratamento:__

Caso o parâmetro não seja selecionado emitir mensagem na tela: “Transferência de créditos no período deve ser preenchido”\.

OS4443

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>OS4581

Quadro 09, campo:

036\-Segregação do Crédito Presumido Utilizado em Substituição aos Créditos pelas Entradas

Numérico

N

S

Neste campo será informado o valor do crédito presumido utilizado em substituição aos créditos pelas entradas, para o preenchimento do Quadro 09\.

__MFS10580__

__\(novo campo, Portaria SEF 070/2017\)__

Quadro 09, campo:

037\-Segregação do Crédito Decorrente do Pagamento Antecipado do ICMS Devido na Saída Subsequente à Importação, com Utilização de Crédito Presumido

Numérico

N

S

Neste campo será informado o valor do crédito decorrente do pagamento antecipado do ICMS devido na saída subsequente à importação, com utilização de crédito presumido, para o preenchimento do Quadro 09\.

__MFS10580__

__\(novo campo, Portaria SEF 070/2017\)__

Quadro 09, campo:

038\- Segregação de outros créditos permitidos para compensar com o débito pela utilização do crédito presumido

Numérico

N

S

Neste campo será informado o valor do crédito permitido para compensar com o débito pela utilização do crédito presumido, para o preenchimento do Quadro 09\.

__MFS11473__

__\(novo campo\)__

Quadro 09, campo:

076\-Segregação dos Débitos Relativos às Saídas com Crédito Presumido em Substituição aos Créditos pelas Entradas

Numérico

N

S

Neste campo será informado o valor dos débitos relativos às saídas com crédito presumido em substituição aos créditos pelas entradas, para o preenchimento do Quadro 09\.

__MFS10580__

__\(novo campo, Portaria SEF 070/2017\)__

Quadro 11, campo: 065 \- Imposto Retido apurado por mercadoria e recolhido por operação

Numérico

N

S

Neste campo será informado o valor do Imposto Retido apurado por mercadoria e recolhido por operação, para o preenchimento do Quadro 11\.

Campo ficará desabilitado a partir de Maio de 2024\.

__MFS85008 MFS619745__

Quadro 11, campo: 073 \- Imposto retido e recolhido com regime especial de apuração mensal

Numérico

N

S

Neste campo será informado o valor do Imposto retido e recolhido com regime especial de apuração mensal, para o preenchimento do Quadro 11\.

__MFS85008__

Quadro 11, campo: 074 – Outros Débitos

Numérico

N

S

Campo de preenchimento não obrigatório\.

Campo deve ser habilitado a partir de Maio de 2024

Campo VLR\_OUT\_DEB\_11\_074 

__MFS619745__

Quadro 11, campo: 115 \- Ressarcimento do ICMS substituição tributária acobertado por NF\-e

Numérico

N

S

Neste campo será informado o valor do Ressarcimento do ICMS substituição tributária acobertado por NF\-e, para o preenchimento do Quadro 11\.

__MFS24064__

Quadro 11, campo: 116 \- Devolução de mercadorias e desfazimento de venda

Numérico

N

S

Neste campo será informado o valor do crédito do imposto relativo à substituição tributária, correspondente à devolução de mercadorias ou desfazimento de vendas cujo imposto foi retido por substituição tributária, para o preenchimento do Quadro 11\.

__MFS520953__

Quadro 11, campo: 899 \- Débitos Especiais de Substituição Tributária

Numérico

N

S

Campo de preenchimento não obrigatório\.

Campo deve ser habilitado a partir de Maio de 2024

Campo VLR\_DEB\_ESP\_11\_899

__MFS619745__

Quadro 13, campo “100\-Pagamentos Antecipados”

Numérico

N

S

Neste campo será informado o valor dos pagamentos antecipados referente a Apuração do ICMS Diferencial de Alíquota das Operações Interestaduais à Consumidor \(Quadro 13\) \.

MFS3005

<a id="OLE_LINK12"></a><a id="OLE_LINK13"></a><a id="OLE_LINK14"></a><a id="OLE_LINK15"></a>Quadro 14, campo:

010\-Valor da Base da Cálculo das Saídas com Crédito Presumido

Numérico

N

S

Neste campo será informado o valor total da base de cálculo das saídas com crédito presumido<a id="OLE_LINK21"></a><a id="OLE_LINK22"></a><a id="OLE_LINK25"></a>, para o preenchimento do Quadro 14\.

<a id="OLE_LINK18"></a><a id="OLE_LINK19"></a><a id="OLE_LINK20"></a>__MFS10580__

__\(novo campo, Portaria SEF 070/2017\) __

Quadro 14, campo:

045\- Débitos pela Utilização do Crédito Presumido Recebido de Estabelecimento Consolidado

Numérico

N

S

Neste campo será informado o valor dos Débitos pela Utilização do Crédito Presumido Recebido de Estabelecimento Consolidado, para o preenchimento do Quadro 14\.

__MFS13230__

__\(novo campo, Portaria SEF 230/2017\)__

Quadro 14, campo:

050\-Débito Apurado pela Apropriação Extemporânea do Crédito Presumido

Numérico

N

S

Neste campo será informado o valor do débito apurado por apropriação extemporânea do crédito presumido, para o preenchimento do Quadro 14\.

__MFS10580__

__\(novo campo, Portaria SEF 070/2017\)__

Quadro 14, campo:

110\-Saldo Credor das Antecipações para o Mês Seguinte Apurado no Mês Anterior

Numérico

N

S

Neste campo será informado o saldo credor das antecipações de mês anterior, para o preenchimento do Quadro 14\.

__MFS10580__

__\(novo campo, Portaria SEF 070/2017\)__

Quadro 16, campo:

020 \- Saldo Credor do FUMDES Apurado no Mês Anterior

Numérico

N

S

Neste campo será informado o saldo credor do FUMDES apurado do mês anterior, para o preenchimento do Quadro 16\.

__MFS91937 \(novo campo, Portaria SEF n° 314/2022\)__

Quadro 16, campo:

120 \- Saldo Credor do FUNDO SOCIAL Apurado no Mês Anterior

Numérico

N

S

Neste campo será informado o saldo credor do FUNDO SOCIAL apurado do mês anterior, para o preenchimento do Quadro 16\.

__MFS91937 \(novo campo, Portaria SEF n° 314/2022\)__

Quadro 41, campo:

Item 010 – Percentual dos créditos em relação ao total das aquisições \(média dos últimos 3 meses\)

 

Checkbox

N

S

Campo para o usuário informar se deve ser considerado no cálculo,  os ajustes lançados em Lançamentos Complementares > Apuração ICMS > Ajuste SINIEF, com a Classe Tipo “710” e Origem “14\-DCIP”\. Como default, deve vir marcado\.

__MFS28607__

Quadro 41, campo:

018 – Operações de Produtos com saída isenta ou não tributada no Mês

TextField

N

S

\-

Campo para o usuário informar o valor das operações com mercadorias que

tenham sido objeto de saída isenta ou não tributada para a qual haja expressa autorização de manutenção de crédito, no período\.

<a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a>OS4581

Quadro 41, campo:

019 – Operações de Produtos com saída diferida ou suspensa no Mês

Numérico

N

S

\- 

Campo para o usuário informar o valor das operações com mercadorias que

tenham sido objeto de saída diferida ou com suspensão no período\.

OS4581

Quadro 41, campo:

997 \- Outras deduções do Saldo Credor

Numérico

N

S

\-

Campo para o usuário informar o valor de outras hipóteses de dedução do saldo credor, tais como créditos irregulares que tenham sido estornados ou glosados pelo fisco após o último pedido de reserva aprovado, ou em outras situações que sejam previstas, inclusive pelo fiscal no momento da análise do Pedido de Reserva

OS4581

Quadro 41, campo:

*Remessas para Fins de Exportação \(Exportação Indireta\)*

Numérico

N

S

Nesse campo deverá ser informado o valor total das Remessas para fins de exportação que foram averbadas no mês\. 

Na funcionalidade de Geração dos Registros, o item 017 – “Produtos Exportados no mês” do quadro 41, será gerado com a somatória dos seguintes valores: 

\- Remessas para Fins de Exportação \(aqui informado\)

\- Exportações Diretas: registros recuperados da SAFX48, de exportações que tenham sido averbadas no mês, 

MFS45748

Quadro 46 \- <a id="_Hlk106024280"></a>Créditos por Regimes e Autorizações Especiais, campo:

<a id="_Hlk106024749"></a>*Origem 14 \(Crédito DCIP\) – Ident\. Regime Especial*

Numérico

N

S

Nesse campo deverá ser informado a Identificação do Regime ou Autorização Especial\. 

Campo alfanumérico de 15 posições\.

Deve ser informado junto com o campo Valor do Crédito\. Se preencher o campo de* *Ident\. Regime Especial, o campo de Valor de Crédito é obrigatório\.  Caso um destes campos não seja preenchido, dar a seguinte mensagem de erro:

*“Campo Ident\. Regime Especial \(Quadro 46\) tem que ser preenchido quando o Valor do Crédito \(Quadro 46\) estiver preenchido\.”*

MFS86547

Quadro 46 \- Créditos por Regimes e Autorizações Especiais, campo:

<a id="_Hlk106025021"></a>*Origem 14 \(Crédito DCIP\) – Valor do Crédito*

Numérico

N

S

Nesse campo deverá ser informado a Identificação do Regime ou Autorização Especial\. 

Campo numérico de 15 inteiros e 2 decimais\.

Deve ser informado junto com o campo Ident\. Regime Especial\. 

Se preencher o campo de Valor de Crédito, o campo de Ident\. Regime Especial é obrigatório\.  Caso um destes campos não seja preenchido, dar a seguinte mensagem de erro:

*“Campo Valor do Crédito \(Quadro 46\) tem que ser preenchido quando o Ident\. Regime Especial \(Quadro 46\) estiver preenchido\.”*

MFS86547

Quadro 51, campo:

021\-Tributo a recuperar incidente na entrada de mercadoria transferida a preço de custo para estabelecimento da mesma empresa

Numérico

N

S

Neste campo será informado o valor de tributo  a recuperar, referente às entradas de mercadoria transferida a preço de custo para outros estabelecimentos\. 

__MFS38324:__ Conforme atualização da Portaria SEF 148/2020, o campo 21 do Quadro 51 não será mais gerado a partir de Jan/2020\. 

Por isso, será feita uma crítica no momento de salvar os dados incluídos/alterados: 

Quando o período informado \(campo “Mês/Ano”\) for >= Jan/2020 __e__ este campo estiver preenchido, será exibida a seguinte mensagem de aviso em tela:

*“O campo 021 do Quadro 51 não será mais gerado no arquivo a partir de Jan/2020 \(Port\. SEF 148/2020\)” *

Trata\-se apenas de um aviso, mas a operação será salva normalmente\.

__MFS38324__

Quadro 85 – Discriminação das Contribuições ao FIA e FEI Devidas no Exercício Anterior

Campo:

501 \- Valor do IRPJ devido no exercício anterior

Numérico

N

S

Referente ao campo VLR\_IRPJ\_Q85 da tabela Tabela: EST\_SC\_DIME\_DD\_INI

MFS93956

Quadro 85 – Discriminação das Contribuições ao FIA e FEI Devidas no Exercício Anterior

Campo:

511 \- Contribuição para o FIA por meio de DARE destinado ao Fundo Estadual

Numérico

N

S

Referente ao campo VLR\_FIA\_EST\_Q85 da tabela Tabela: EST\_SC\_DIME\_DD\_INI

MFS93956

Quadro 85 – Discriminação das Contribuições ao FIA e FEI Devidas no Exercício Anterior

Campo:

512 \- Transferência ou contribuição para o FIA direcionados a Fundos Municipais;

Numérico

N

S

Referente ao campo VLR\_FIA\_MUN\_Q85da tabela Tabela: EST\_SC\_DIME\_DD\_INI

MFS93956

Quadro 85 – Discriminação das Contribuições ao FIA e FEI Devidas no Exercício Anterior

Campo:

521 \- Contribuição para o FEI por meio de DARE destinado ao Fundo Estadual

Numérico

N

S

Referente ao campo VLR\_FEI\_EST\_Q85 da tabela Tabela: EST\_SC\_DIME\_DD\_INI

MFS93956

Quadro 85 – Discriminação das Contribuições ao FIA e FEI Devidas no Exercício Anterior

Campo:

522 \- Transferência ou contribuição para o FEI direcionados a Fundos Municipais

Numérico

N

S

Referente ao campo VLR\_FEI\_MUN\_Q85 tabela Tabela: EST\_SC\_DIME\_DD\_INI

MFS93956


# MTZ_OTF_DIRF-2020 e anos posteriores

- **Fonte:** MTZ_OTF_DIRF-2020 e anos posteriores.docx
- **Modificado:** 2026-02-12
- **Tamanho:** 609 KB

---

 

Obrigações de Tributos Federais \- DIRF 2020 em diante

##### DOCUMENTO DE REQUISITO

###### OS / CH / MFS

###### Nome

__Descrição__

OS3832

Obrigações de Tributos Federais \- DIRF 2013

<a id="_Toc281404230"></a>Atualização da DIRF – Leiaute 2013 – Ano\-Calendário 2012 e 2013 \(no caso de situação especial\)\.

Módulo: Obrigações de Tributos Federais

- Alteração dos campos “Ano Calendário” e “Ano Referência DIRF” do menu DIRF >> Geração DIRF para permitir a geração do arquivo no formato correto\.
- Quando o parâmetro “Extinção” da tela da Geração da DIRF for selecionado, o default dos campos Ano\-Calendário e Ano Referência\-DIRF serão “2013”,”2013”, caso contrário preencher com “2012”, “2013” respectivamente\.
- Alterado o campo “Valor Anual Mínimo de Rendimentos” para o valor default 24\.556,65\.
- Alterar o nome do parâmetro IN 1\.033/2010 para IN 1\.297/2012
- Incluir no parâmetro IN 1\.297/2012, incluir a opção: Pagamentos relacionados à Copa das Confederações Fifa 2013 e Copa do Mundo Fifa 2014\.

CH28145\_2012

Alteração

Considerar na DIRF todos os registros que possuem o código de Receita 6891\.

OS3734

Obrigações de Tributos Federais \- Gerar Registros RIP65 e RIL96 a partir da SAFX53

O cliente Caixa Seguradora possui o cenário em que além das retenções de Terceiros que são informadas na tabela de Controle de Tributos – SAFX53 – o cliente possui também retenções de Clientes que também fazem parte dessa tabela\. 

Esses clientes possuem contas bancárias nas instituições financeiras e efetuam resgate de aplicações, prêmios, etc\., e nesses casos é devida retenção na fonte para o valor resgatado\. Nesse cenário a Caixa Seguradora é a entidade responsável pelo recolhimento dessa retenção\. Além disso, existe a retenção para clientes com mais de 65 anos e também para lucros e dividendos\.

Quando a obrigação acessória DIRF foi reformulada em 2011, os registros de rendimentos isentos, tais como, RIP65 e RIL96 foram contemplados para serem recuperados apenas da Folha de Pagamento\. Na época esse desenvolvimento não foi estendido para a tabela de Controle de Tributos – SAFX53\.

O cliente Caixa Seguradora tem apenas essa situação para o RIP65 e RIL96\. Conforme alinhado com o Marcos de Paula \(Requisitos\) essa OS irá tratar apenas esses registros para atendimento desse cliente e caso outros rendimentos isentos sejam necessários para serem recuperados da SAFX53, isso será tratado posteriormente\.

OS3832\-A

Alteração

de

CH2967\_2013

OTF – Ajustes na Aposentadoria Isenta para geração do registro RTRT

O objetivo deste requisito é permitir que o valor excedente dos Rendimentos Isentos para Maiores de 65 anos seja considerado como Valor Tributável da DIRF, ao invés de somente o Valor Bruto, conforme é feito atualmente\.

O cliente Caixa Seguradora informou que existe uma beneficiaria que recebeu o benefício de R$ 1\.713,91, por ser maior de 65 anos tem isenção de R$ 1\.637,11\. O sistema no modulo DW representa corretamente o pagamento feito à cliente\. Ao gerar a DIRF o sistema colocar como rendimento tributável o valor total recebido pela cliente e como rendimento isento R$ 1\.637,11\. 

Ao verificar o Manual da DIRF 2013, o mesmo explica o seguinte:

Logo, podemos deduzir que para o Ano Calendário 2012 – Ano Referência 2013, até o valor de R$ 1\.637,11 mensalmente será considerado isento e o valor tributado será o excedente a esse valor\. Fazendo um paralelo com o exemplo do cliente, o valor tributado para o mês de 12/2012 será R$ 76,80\.

Verificamos com a área de Informação e com o Sr\. Marcos Paula, e não será criado parâmetro para essa situação, a regra ficará interna dentro do sistema\.

CH5171\_2013

OTF – Ajustes na geração do registro RTRT para considerar apenas o Valor Bruto

O objetivo deste documento de requisito é permitir duas importantes alterações no que se refere à DIRF e ao Informe de Rendimentos:

Informe de Rendimentos

- Foi observado que ao gerar o Comprovante de Rendimentos através do Validador da DIRF 2013, quando o Código de Receita é 0916 – Prêmios Obtidos em concursos e sorteios, o valor informado na linha 2 – Outros do Quadro 5 – Rendimentos sujeitos à Tributação Exclusiva \(rendimento líquido\) deverá ser o resultado da Linha 01 – Linha 02 do Quadro 3 – Rendimentos Tributáveis\. Ocorre que essa informação – já calculada – já é carregada através do campo 43 da SAFX53 \(Valor Outros de Tributação Exclusiva\)\. Nesse caso quando for gerado o Informe de Rendimentos desse Código de Receita é 0916, o sistema só deve exibir a linha 2 do Quadro 5 e não deve exibir as informações do Quadro 3\.

DIRF

- Ao realizar os testes do Informe de Rendimentos, foi verificado que não existe registro específico para os Rendimentos de Tributação Exclusiva\. Ocorre que existe uma regra no produto MasterSAF DW que ao gerar os registro RTRT – Rendimento Tributável, o sistema realiza uma soma entre os campos de Valor Bruto e Valor Outros de Tributação Exclusiva \(campos 14 e 43 da SAFX53\)\. Ocorre que após entendimento do CAN, essa informação já é composta como Rendimento Tributável, uma vez que a única informação que não deve ser considerada no Rendimento Tributável são as informações de Exigibilidade Suspensa\. Nesse caso o sistema só deve considerar para a geração do registro RTRT a informação do Valor Bruto\.

<a id="_Hlk404538088"></a>OS4293

Obrigações de Tributos Federais – Geração da DIRF 2014

Trata\-se das novas alterações para geração do meio magnético DIRF 2014, ano calendário 2013\.

OS4382

Obrigações de Tributos Federais – Gerar Responsável Legal do Declarante Pessoa Jurídica na DIRF

O cliente ao gerar a DIRF, possui Responsáveis Legais diferentes para os registros RESPO e DECPJ\. Ocorre que a geração desses registros, o sistema recupera a informação de uma mesma origem, fazendo com o que o cliente para gerar esses registros preencha apenas um campo\. Ocorre que o Responsável Legal não necessariamente precisa ser o mesmo Responsável Legal do Declarante Pessoa Jurídica, logo, podem ser CPF’s distintos para os dois registros\.

OS4409

Obrigações de Tributos Federais – Gerar Rendimentos de PLR da SAFX21 com o Código de Receita 3562

O cliente Raízen utiliza a Folha de Pagamento do MasterSAF DW \(tabela: SAFX21\) para a geração das informações da DIRF\. Ocorre que o cliente observou uma situação legal que o sistema hoje não comporta\.

Conforme IN 1\.297 de 2012, os rendimentos tributáveis e de imposto de renda retido na fonte referentes ao PLR – Pagamento de Participação nos Lucros ou Resultados deverão ser gerados sob o código de receita 3562 e não mais sob o código de receita 0561\. Ocorre que ao gerar as informações de um funcionário com suas verbas parametrizadas, todas elas são geradas sob o código 0561 e não sob o código 3562\. Para visualizar essa situação, basta ver a exigência do validador\.

CH2574\_2014

Obrigações de Tributos Federais – Considerar apenas uma pessoa física/jurídica caso exista mais de uma no mesmo ano calendário com datas de validade distintas

O objetivo deste documento de requisito é permitir a correta geração do fornecedor no registro BPFDEC ou BPJDEC quando existem para o mesmo ano calendário\. No caso será gerado apenas o fornecedor mais recente nesses registros, conforme testes realizados\.

CH4180\_2014

Geração do campo 3 – Informações Complementares do registro INF

O objetivo deste documento de requisito é permitir que ao gerar o campo 3 – Informações Complementares do registro INF, o mesmo não ultrapasse 200 caracteres que é o limite do campo\.

Vale salientar que a SAFX22 que é a tabela de onde as informações para esse campo são recuperadas, o cliente cadastra vários registros para um mesmo funcionário\. Como o campo 3 – Informações Complementares do registro INF é formado através de uma concatenação, será necessária uma quebra em 200 caracteres para que essa informação não seja ultrapassada\.

CH22018\-A\_2014

Geração dos campos 4\-DDD e 5\-Telefone do Registro RESPO

O objetivo deste documento de requisitos é permitir a emissão de mensagem ao usuário quando os campos DDD e Telefone do responsável legal não estiverem cadastrados na tela “Responsáveis por Informações” por se tratarem de campos obrigatórios\.

OS4677

Obrigações de Tributos Federais – Geração da DIRF 2015

<a id="OLE_LINK11"></a><a id="OLE_LINK12"></a><a id="OLE_LINK13"></a>Trata\-se das novas alterações para geração do meio magnético DIRF 2015, ano calendário 2014\.

OS4725

Inclusão da Parametrização “Gera Registros sem retenção” na Geração da DIRF

Este documento tem como objetivo incluir nova parametrização “Gera Registros sem retenção” na geração dos registros da DIRF para RTRT \- Rendimentos Tributáveis \- Rendimento Tributável\.

MFS\-2346

<a id="OLE_LINK20"></a><a id="OLE_LINK21"></a><a id="OLE_LINK22"></a>Obrigações de Tributos Federais – Geração da DIRF 2016

Trata\-se das novas alterações para geração do meio magnético DIRF 2016, ano calendário 2015\.

MFS\-3277

Obrigações de Tributos Federais – Geração da DIRF 2016

Alteração na regra de geração DIRF, onde são recuperados os beneficiários dos registros RIL96, RIO, RIPTS, RIIRP somente se o valor total  de rendimentos for superior a 3 \(três\) vezes o valor anual mínimo de rendimentos

MFS\-3988

Obrigações de Tributos Federais – Geração da DIRF 2016

Alteração na regra de geração da DIRF, onde deverá considerar rendimentos isentos para trabalhos sem vínculo empregatício, alugueis e royalties\. 

MFS\-4454

Obrigações de Tributos Federais – Geração da DIRF 2016

Alteração no campo Responsável Legal da tela de Geração do Meio Magnético – DIRF, passará a listar as informações em ordem alfabética\. 

CH15903\_2015

Inclusão de tratamento no campo 03 – Nome Empresarial

Este documento tem como objetivo tratar o preenchimento do campo 03 – Nome Empresarial para considerar o campo RAZAO\_SOCIAL\_COMPL da tabela ESTABELECIMENTO\.

MFS\-8291

Obrigações de Tributos Federais – Geração da DIRF 2017

Registro SCP – BPFSCP – BPJSCP – RISCP \- DIRF \- 2017

MFS\-8380

Obrigações de Tributos Federais – Geração da DIRF 2017

Trata\-se das novas alterações para geração do meio magnético DIRF 2017, ano calendário 2016\.

MFS\-8800

Obrigações de Tributos Federais – Geração da DIRF 2017

Geração dos Registros INFPC\(RTPP, RTFA, RTSP, RTEP\) e INFPA\(ESPP, ESFA, ESSP, ESEP\)

Exclusão dos registros RTPP e RTPA da geração a partir da SAFX53\.

MFS\-8835

Obrigações de Tributos Federais – Geração da DIRF 2017

Criação da SAFX207, 208 e 209 e suas respectivas telas de manutenção para atendimento a obrigação acessória DIRF\.

MFS\-8984

Obrigações de Tributos Federais – Geração da DIRF 2017

Geração dos Registros RTPSE e RDTPSE

MFS\-8989

Obrigações de Tributos Federais – Geração da DIRF 2017

Inclusão de mensagem no log de geração DIRF referente ao campo “Valor Pago a Advogado” e Geração do registro INFPA dentro da estrutura do RRA\.

MFS\-14872

Obrigações de Tributos Federais – Geração da DIRF 2018\.

Trata\-se das novas alterações para geração do meio magnético DIRF 2018, ano calendário 2017\.

CH1608\_2018 \(MFS\-16323\)

Alteração do preenchimento do campo “5\-Indicador de identificação do alimentando” do Registro BPFDEC

Esse documento tem como objetivo alterar o preenchimento do campo “5\-Indicador de identificação do alimentando” do Registro BPFDEC \- Beneficiário pessoa física do declarante\.

MFS\-21816

Obrigações de Tributos Federais – Geração da DIRF 2019\.

Trata\-se das novas alterações para geração do meio magnético DIRF 2019, ano calendário 2018\.

28168/2006

Geração da DIRF \- RTRT

Tratamento de valores “Triplicados”, devido importação dos valores separados na SAFX53 do Código Retenção 5952 – PCC\. \(__Apenas para atualização do documento__\)\.

MFS\-25062

Alteração do preenchimento do campo “6\- Indicador de que o país não

exige Número de Identificação

Fiscal \- NIF” do Registro BRPDE

Esse documento tem como objetivo alterar o preenchimento do campo “6\- Indicador de que o país não exige Número de Identificação Fiscal \- NIF” do Registro BRPDE \- Beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior\.

MFS\-28557 e MFS\-28360

Alteração de forma de preenchimento automático da tela de Geração da DIRF

Esse documento tem como objetivo alterar todo o controle feito por itemChanged da tela de geração da DIRF para atender ao TAX ONE\.

MFS\-33041

Geração da DIRF 2020\.

Alteração nas duas funcionalidades Geração da DIRF e Geração do Meio Magnético, para contemplar a atualização da versão DIRF 2020\. 

Base Legal: ATO DECLARATÓRIO EXECUTIVO Nº 65, DE 29 DE NOVEMBRO DE 2019

MFS\-42862

Geração da DIRF 2021\.

Alteração nas duas funcionalidades Geração da DIRF e Geração do Meio Magnético, para contemplar a atualização da versão DIRF 2021\. 

Regra alterada: RN08\.

Base Legal: ADE COFIS nº34/2020

MFS\-38828

Registros VPEIM, RIMUM, RISEN

Geração dos registros VPEIM, RIMUM, RISEN\. Vide tópico 3\.19

MFS\-59751

Alteração do registro BPFDEC

Alteração da geração para funcionários sem vínculo empregatício e que tenham valor de IR Retido, conforme Instrução Normativa n° 1990/20, artigo 10, inciso III\. 

MFS\-60780

Alteração do registro BPFDEC

Desfazimento da regra relativa à MFS59751, que havia sido feita com base nas definições fornecidas pelo Setor de Informação\.

MFS\-62410

Alteração do registro DECPJ

Alteração da regra de geração do Campo 12, para as Empresas de Natureza Declarante “3”, e que devem informar o registro VPEIM \(imunes e isentos\), porém não se enquadram no campo 12 = S \(Fundação pública de direito privado\), gerando erros no validador\.\( IN RFB 1\.234/2012, Art\. 2º e Art\. 4º\) Cliente Finep\.

__MFS\-68078__

Registros VPEIM, RIMUM, RISEN

Tratamento na geração dos Registros VPEIM, RIMUM, RISEN, para as empresa de Natureza Declarante “3 – Empresas públicas ou sociedade de economia mista Federal”\.\(Cliente Finep\)\. E Retirar a regra implementada na Demanda MFS\-62410\.

[__MFS\-76524__](https://jira.thomsonreuters.com/browse/MFS-76524)

Geração da DIRF 2022 – 09/12/2021

Alteração da DIRF, para contemplar a atualização da versão DIRF 2022\. 

Regra alterada: RN08 e RN246\.

Base Legal:  ADE COFIS n° 94/2021

__MFS\-81694__

Rogério Ohashi – 01/06/2022

Aba \- Resumo das informações DIRF \- Retirar regra para listar os Beneficiários Não\-Informados, somente, quando o campo “VLR\_DED\_INSS\_TERC” estiver preenchido com valor > que ‘0’ \.

__MFS\-90689__

Elisabete Costa – 21/09/2022

\- Alteração da DIRF, para contemplar a atualização do ano\-calendário 2021

Inclusão da geração dos registros __RIRPC, RIJMRE__\.

\- Exclusão da __X530\_RETIFICACAO\_IRRF, __pois não é utilizada\.

__MFS\-97809__

Elisabete Costa – 09/12/2022

Alteração da DIRF, para contemplar a atualização da versão DIRF 2023\. 

Regra alterada: __RN08__ 

Base Legal:  ADE COFIS n° 113/2022

__MFS\-594253__

Alessandra Navatta

Alteração da DIRF, para contemplar a atualização da versão DIRF 2024\. 

Regra alterada: __RN08__ 

Inclusão do registro RTDS \(RN39 a RN52\)

Inclusão do registro ESDS \(RN91 a RN104\)

Base Legal:  ADE COFIS n° 56/2023

__MFS\-713686__

Rosemeire Santos

Alteração da DIRF, para contemplar a atualização da versão DIRF 2025\. 

Regra alterada: __RN08__ 

Base Legal:  ADE COFIS n° 35/2024

# <a id="_Toc49801940"></a><a id="_Toc49802219"></a><a id="_Toc49802422"></a><a id="_Toc49802532"></a><a id="_Toc49803297"></a><a id="_Toc49803540"></a><a id="_Toc49805170"></a><a id="_Toc49805288"></a><a id="_Toc49805400"></a><a id="_Toc50402977"></a><a id="_Toc50403101"></a><a id="_Toc50404640"></a>

# <a id="_Toc155171971"></a>Tópicos:

Contents

[Tópicos:	7](#_Toc155171971)

[1  – Tela de Geração da DIRF	8](#_Toc155171972)

[2  – Tela de Geração do Meio Magnético da DIRF	10](#_Toc155171973)

[3 – Regras de Geração dos Registros	10](#_Toc155171974)

[3\.1 – Dirf – Declaração do imposto sobre a renda retido na fonte	10](#_Toc155171975)

[3\.2 – RESPO – Responsável pelo preenchimento	12](#_Toc155171976)

[3\.3 – DECPJ – Registro de Identificação do Declarante pessoa jurídica	17](#_Toc155171977)

[3\.4 – IDREC – Registro de Identificação do código de receita	24](#_Toc155171978)

[3\.5 – BPFDEC – Registro de Beneficiário pessoa física do declarante	25](#_Toc155171979)

[3\.6 – Registro de valores mensais: RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTDS, RTIRF, ESPP, ESFA, ESSP, ESEP, ESPA	29](#_Toc155171980)

[3\.7 – RTRT – Rendimentos Tributáveis \- Rendimento Tributável	41](#_Toc155171981)

[3\.8 – RTIRF \- Rendimentos Tributáveis \- Imposto sobre a Renda Retido na Fonte	45](#_Toc155171982)

[3\.9 – Registro CJAC,CJAA	48](#_Toc155171983)

[3\.10 – Registros ESRT, ESPO, ESPP, ESDP, ESDS, ESPA, ESIR, ESDJ	59](#_Toc155171984)

[3\.12 – RIVC, RIBMR, RICAP	95](#_Toc155171985)

[3\.13 – RIL96: Rendimentos Isentos anuais – Lucros e dividendos pagos a partir de 1996\.	112](#_Toc155171986)

[3\.13\.a – RIJMRE – Rendimentos Isentos Anuais – Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função	114](#_Toc155171987)

[3\.14 – RIPTS – Rendimentos Isentos Anuais – Valores Pagos a titular ou sócio ou empresa de pequeno porte, exceto pró\-labore e aluguéis	114](#_Toc155171988)

[3\.15 – RIO \- Rendimentos Isentos Anuais – Outros	115](#_Toc155171989)

[3\.16 – INFPC – Informações de Previdência Complementar	116](#_Toc155171990)

[3\.17 – INFPA – Informações do beneficiário da pensão alimentícia	117](#_Toc155171991)

[3\.18 – BPJDEC – Beneficiário pessoa jurídica do declarante	119](#_Toc155171992)

[3\.19 – VPEIM e registros filhos RIMUM e RISEN	120](#_Toc155171993)

[3\.20 – Registros PSE, OPSE, TPSE, RTPSE, DTPSE, RDTPSE	128](#_Toc155171994)

[3\.21 – Registros RPDE, BRPDE,VRPDE	136](#_Toc155171995)

[3\.22 – RRA e filhos \(IDREC, BPFRRA, RTRT, RTPO, RTIRF, RIMOG, RIP65, DAJUD, QTMESES, INFPA, RTPA\)	149](#_Toc155171996)

[3\.23 – INF, FIMDIRF	167](#_Toc155171997)

[4 – Regras Gerais	168](#_Toc155171998)

<a id="_Tela_de_Geração"></a><a id="_Toc49779706"></a><a id="_Toc49801941"></a><a id="_Toc49802220"></a><a id="_Toc49802423"></a><a id="_Toc49802533"></a><a id="_Toc49803298"></a><a id="_Toc49803541"></a><a id="_Toc49805171"></a><a id="_Toc49805289"></a><a id="_Toc49805401"></a><a id="_Toc50402978"></a><a id="_Toc50403102"></a><a id="_Toc50404641"></a>

# <a id="_Toc155171972"></a>1  – Tela de Geração da DIRF

<a id="_Toc49779707"></a>__RN00__

__Tela Geração da DIRF:__

Apresentar os seguintes campos:

__Extinção__: check\-box, habilitado, com default desmarcado\.

__Mês Ini__: campo texto, habilitado, com valor default 01\.

__Mês Fim__: campo texto, habilitado, com valor default 12\. 

__Ano\-Calendário__: campo texto, habilitado, com valor default igual ao ano anterior ao da data corrente\.

__Ano Referência\-DIRF:__ campo texto, habilitado, com valor default igual ao ano da data corrente\.

__Sócio Ostensivo__: lista contendo os valores: “\-“, “sim”, “não”\.

__Código de Retenção p/ Funcionário__:

c/ Vínculo Empregatício: campo texto, habilitado, com valor default 0561

s/ Vínculo Empregatício: campo texto, habilitado, com valor default 0588

Residente no Exterior: campo texto, habilitado, com valor default 0473

PRL: campo texto, habilitado, com valor default 3562

__Tipo de Centralização__: lista contendo os valores: 1 – Não Centralizado; 2 – Centralizado por Empresa

__Tipo de Declaração__: lista contendo os valores: Original, Retificadora

__Excluir tratamento do código de retenção 0588 \(origem Folha\) do Art 15, Parágrafo 2º da IN SRF de 02/01/2001__: check\-box, habilitado, com default desmarcado\.

__Utilizar parâmetros por operação__: check\-box, habilitado, com default desmarcado\.

__Gerar dados de PJ com situação de rendimento especial \(imposto compensado por decisão judicial, tributacao sob exigibilidade suspensa, IR c/deposito judicial\)__: check\-box, habilitado, com default desmarcado\.

OS4293/

OS4677/

OS4409

MFS\-8380

MFS\-14872

MFS\-21816

MFS\-28557

MFS\-33041

MFS\-42862

<a id="_Toc49779708"></a>RN01

__Tela Geração da DIRF \(continuação\):__

Subtítulo: IN 1\.671/2016:

__Declarante depositário de crédito decorrente de decisão judicial__: check\-box, habilitado, com default desmarcado\.

__Declarante de instituição administradora ou intermediadora de fundo ou clube de investimento__: check\-box, habilitado, com default desmarcado\.

__Declarante de rendimentos pagos a residentes ou domiciliados no exterior__: check\-box, habilitado, com default desmarcado\.

__Plano privado de assistência a saúde \- coletivo empresarial__: check\-box, habilitado, com default desmarcado\.

__Pagtos relac\. a Copa das Confederações Fifa 2013 e Copa do Mundo Fifa 2014__: check\-box, com default desmarcado\. Habilitar apenas quando Ano\-Referência\-DIRF for preenchido com anos de 2013 a 2016\.

__Pagtos\. relacionados aos Jogos Olímpicos/Paraolímpicos de 2016__: check\-box, com default desmarcado\. 

\[MFS\-21816\] Habilitar apenas quando Ano\-Referência\-DIRF for preenchido com anos anteriores a 2019\. Para “Ano Referência DIRF” for maior ou igual a “2019”, esse campo fica desabilitado\.

__Observação:__ Na DIRF2018, o __campo 11 do registro DECPJ__ era preenchido de acordo com a marcação do parâmetro da tela de geração “Pagtos relacionados aos Jogos Olímpicos/Paraolímpicos de 2016”\. No novo leiaute da DIRF2019 __o campo 11__ será preenchido com a informação do parâmetro “Indicador de entidade em que a União detém maioria do capital a voto” \(vide RN355\)\.

Subtítulo: IN 1757/2017:

__Indicador de entidade em que a União detém maioria do capital a voto__: check\-box, habilitado, com default desmarcado\.

Subtítulo IN 1836/2017:

__Indicador de fundação pública de direito privado__: check\-box, com default desmarcado\. Habilitar apenas quando Ano\-Referência\-DIRF for maior ou igual a “2019”\.

Campo utilizado no preenchimento do __campo 12 do registro DECPJ__ \(vide RN394\)\. 

__Valor Anual Mínimo de Rendimentos__: campo texto, habilitado, com valor default 28559,70

Para atender ao Tax One será necessário realizar a verificação abaixo para esse campo:

Se campo ind\_environment da tabela prt\_par\_msaf = ‘DW’ então:

    Valor default = '28\.559,70'

Se não

    Valor default = '28559\.70'

__Empresa__: lista da tabela EMPRESA que o usuário de login possui acesso\.

__Estabelecimento__: lista de ESTABELECIMENTOS da empresa selecionada, que o usuário de login tem acesso\. Depende do parâmetro Tipo de Centralização\.

Para facilitar a pesquisa do Estabelecimento, é disponibilizada a tela de seleção do estabelecimento, acionada através do botão “Selecionar”\. Os campos que estarão disponíveis para a pesquisa são Cod\_Estab e Descrição\.

OS3832\-A

OS3528

OS4293/

OS4677/

MFS\-2346

MFS\-8380

MFS\-14872

MFS\-21816

MFS\-28360

# <a id="_Tela_de_Geração_1"></a><a id="_Toc49801942"></a><a id="_Toc49802221"></a><a id="_Toc49802424"></a><a id="_Toc49802534"></a><a id="_Toc49803299"></a><a id="_Toc49803542"></a><a id="_Toc49805172"></a><a id="_Toc49805290"></a><a id="_Toc49805402"></a><a id="_Toc50402979"></a><a id="_Toc50403103"></a><a id="_Toc50404642"></a><a id="_Toc155171973"></a>2 – Tela de Geração do Meio Magnético da DIRF

<a id="_Toc49779715"></a>RN02

__Tela Geração do Meio Magnético \- DIRF:__

Apresentar os seguintes campos:

__Empresa__: lista da tabela EMPRESA que o usuário de login possui acesso\.

__Ano Referência\-DIRF:__ campo texto, habilitado, com valor default igual ao ano da data corrente\.

__Processo\-Ano Base – Dt Geração:__ lista dos processos da Geração Dirf, relacionados a empresa e Ano Referência informados\.

__Natureza do declarante: __lista fixa composta pelos itens:

0 \- Pessoa jurídica de direito privado 

1 \- Órgãos, autarquias e fundações da administração pública federal 

2 \- Órgãos, autarquias e fundações da administração pública estadual, municipal ou do Distrito Federal 

3 \- Empresa pública ou sociedade de economia mista federal 

4 \- Empresa pública ou sociedade de economia mista estadual, municipal ou do Distrito Federal 

8 \- Entidade com alteração de natureza jurídica \(uso restrito\)

__Responsável Legal__: lista dos responsáveis do cadastro de Responsáveis por Informações do módulo Parâmetros\. As informações do campo “Responsável Legal” deverão ser listadas em ordem alfabética\.

__Responsável Legal do Declte PJ__: lista dos responsáveis do cadastro de Responsáveis por Informações \(menu Requisitos Legais >> Responsável por Informações do módulo Parâmetros\)\. Campo obrigatório de preenchimento\. 

__Núm Recibo Última Declaração__: campo texto

__Estabelecimento__: lista de ESTABELECIMENTOS relacionados a empresa e processo da Geração DIRF selecionados\.

Para facilitar a pesquisa do Estabelecimento, é disponibilizada a tela de seleção do estabelecimento, acionada através do botão “Selecionar”\. Os campos que estarão disponíveis para a pesquisa são Cod\_Estab e Descrição\.

MFS\-4454

MFS\-42862

# <a id="_Toc49801943"></a><a id="_Toc49802222"></a><a id="_Toc49802425"></a><a id="_Toc49802535"></a><a id="_Toc49803300"></a><a id="_Toc49803543"></a><a id="_Toc49805173"></a><a id="_Toc49805291"></a><a id="_Toc49805403"></a><a id="_Toc50402980"></a><a id="_Toc50403104"></a><a id="_Toc50404643"></a><a id="_Toc155171974"></a>3 – Regras de Geração dos Registros

## <a id="_Toc49801944"></a><a id="_Toc49802223"></a><a id="_Toc49802426"></a><a id="_Toc49802536"></a><a id="_Toc49803301"></a><a id="_Toc49803544"></a><a id="_Toc49805174"></a><a id="_Toc49805292"></a><a id="_Toc49805404"></a><a id="_Toc50402981"></a><a id="_Toc50403105"></a><a id="_Toc50404644"></a><a id="_Toc155171975"></a>3\.1 – Dirf – Declaração do imposto sobre a renda retido na fonte 

<a id="_Toc49779717"></a>RN03

__Registro DIRF __

Gravar no__ campo 1 – Identificador do Registro__ o valor fixo “__Dirf__”\.

OS4293

<a id="_Toc49779718"></a>RN04

__Registro DIRF __

Gravar no__ campo 2 –__ __Ano referência__ a informação do campo “Ano\-Referência\-DIRF” da tela de geração da DIRF \(módulo: Obrigações de Tributos Federais, menu DIRF >> Geração DIRF\)\. 

OBS: as regras contidas nesse documento devem ser referentes ao ano referência 2020 ou posteriores\. Os outros ano\-referência devem ser gerados através dos outros layouts, com as regras de geração definidas nas matrizes dos respectivos anos\-referências\.

OS4293/

OS4677/ 

MFS\-2346

MFS\-8380

MFS\-14872

MFS\-21816

<a id="_Toc49779719"></a>RN05

__Registro DIRF __

Gravar no__ campo 3 –__ __Ano\-calendário__ a informação do campo “Ano\-Calendário” da tela de geração da DIRF \(módulo: Obrigações de Tributos Federais, menu DIRF >> Geração DIRF\)\. 

Para tanto a informação deve estar preenchida com as opções 2019, 2020 ou posteriores\. 

Campo de preenchimento obrigatório\.

OS4293/

OS4677/

MFS\-2346

MFS\-8380

MFS\-14872

MFS\-21816

<a id="_Toc49779720"></a>RN06

__Registro DIRF __

Gravar no__ campo 4 –__ __Indicador de Retificadora__ se a declaração é retificadora ou não\. Para identificar seguir a seguinte regra:

- Gravar “N” caso o campo “Tipo de Declaração” do menu DIRF >> Geração DIRF estiver selecionado com a opção “Original”\.
- Gravar “S” caso o campo “Tipo de Declaração” do menu DIRF >> Geração DIRF estiver selecionado com a opção “Retificadora”\.

OS3528

<a id="_Toc49779721"></a>RN07

__Registro DIRF __

Gravar no__ campo 5 –__ __Número do Recibo__ a informação de acordo com as regras abaixo:

- Recuperar a informação do campo “Núm\. Recibo Última Declaração” do menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais\.

OS3528

<a id="_Toc49779722"></a>RN08

__Registro DIRF __

Gravar no__ campo 6 –__ __Identificador de Estrutura do leiaute__ o valor fixo, dependendo do Ano referência informado no campo “Ano Referência\-DIRF” da tela de geração da DIRF \(módulo: Obrigações de Tributos Federais, menu DIRF >> Geração DIRF\)\.

Se ano referência for igual a 2020 então: \[MFS\-42862\]

       Preencher com “AT65HD8” 

Se ano referência for __maior ou igual__ a 2021, então: \[MFS\-42862\]

      Preencher com “VR4QLM8”  

Se ano referência for __maior ou igual__ a 2022, então: \[MFS\-76524\]

      Preencher com “__XJFSFHB__”  

Se ano referência for __maior ou igual__ a 2023, então: \[MFS\-97809\]

      Preencher com “__ARNZRXP__”  

Se ano referência for __maior ou igual__ a 2024, então: \[MFS\-594253\]

      Preencher com “__B3VH8RQ__”  

Se ano referência for __maior ou igual__ a 2025, então: \[__MFS\-713686__\]

      Preencher com “__R6GP3ZA__”  

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABL0AAAGaCAYAAADq0DGIAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAAP+lSURBVHhe7P1XkGVHlh0KrqtvaJ2RERmptQAyoTVK66pWfBT9SL4hOTQaH8dsbIZf/Bp7j99j5MeQHzM2Q2P3a0F2d2mogk6IBFJrLUNrfbWctbYfj7gRSKBQzapqAHV3hN9zjmuxfSv34ycUAaqoQx3qUIc61KEOdahDHepQhzrUoQ51qEMdvkAQDq51qEMd6lCHOtShDnWoQx3qUIc61KEOdajDFwZWdnqVqvUNX3WoQx3qUIc61KEOdahDHepQhzrUoQ51+HxDNBSya32nVx3qUIc61KEOdahDHepQhzrUoQ51qEMdvnBQN3rVoQ51qEMd6lCHOtShDnWoQx3qUIc61OELB3WjVx3qUIc61KEOdahDHepQhzrUoQ51qEMdvnBQN3rVoQ51qEMd6lCHOtShDnWoQx3qUIc61OELB3WjVx3qUIc61KEOdahDHepQhzrUoQ51qEMdvnBQN3rVoQ51qEMd6lCHOtShDnWoQx3qUIc61OELB3WjVx3qUIc61KEOdahDHepQhzrUoQ51qEMdvnBQN3rVoQ51qEMd6lCHOtShDnWoQx3qUIc61OELB3WjVx3qUIc61KEOdahDHepQhzrUoQ51qEMdvnBQN3rVoQ51qEMd6lCHOtShDnWoQx3qUIc61OELB6EIUNVNqWqXXwtUg7xCoZBd9SynZ+8nWB/v/vDJ9VIocw5+K3aHapiOd6EKH8p0vK9EFQKE+RxSKsUJWzQHZcbyZdHfnHJ1EGZWlixU4ENWPkzR4sJKLqzCSJWIygOiYM8GeThQXeQUN6hLSHEtU/aF4uvWpQ+pfq41nxp8H/t7wfpnXeUikcia+HX4HMAqMhme6NHhvrNd685w1IPhv8M5xXRBMfsNBfggqHocsV/lw1wtfDVOWZRiDRCHfN4Vj7uBY1h1pVznqb+a7FbBKlyxFC6uy8uyMXDha0DzuyZG7a0vosarDp9RWE9/PI0SmP/qYwDrcMGSGrb6hxVYMw88BFE+NsgClL+PEeRrgUHi+8D98lsPH0ldmyjgA2pHJcD/CHmKIE9+UmZjImRUCY/3QdoqeVk1aKjnFzbPBPetVOC5lkiY8z568jxCLhwOf2oe8ZHxC3JVj4ozyyfio9iVZYhGrdQn4mIFQ1zWLZ3SBRzz1wKuNPV20MkejAc7WiqweAE/FqgeBgG9Kwd1D3FswpUgHWUAyRROEllJYWAjpEwDFLN4Aen04FIpT0Xy9YsxbtielFxxohaHdau6OOWQ4qj/1IurLVwP5mPBLs4aCMY56H6L64dGddWtC6uwmXLyYUAoau3I8Uk+cYbHrP4C5RLgrW7XwX1qsRqtBp9qwft6vKzFVf/8qXBWGflqMqnmUoke8g7zJyrkY23KEZeX/HQnb48VMX/jA9fARzxWQGWsBx9blMDDx/FNjYeLWRuXc1U3tfE/4sF79284JfCz33WFq4Whpfo/VLRnN4ZuHF1sF++TwHDHR3OJCMpzNa2nGbXjVSFu6flTjeFnElYaS/BtCBBlRXZRP6jHNX8DJKzG6djz9K/W6gE2+ZSGLrhVCb6UVdQLfPkgbUagX+GQm8cuheiqwMdQmJ/nlplBEEmPwRiVwm7sPSYIVtIxur/1sBImqMlO4MMcHn88rA32k9WDQn0MZRjgalUyLuvKIFcMaUM1b3eiTqr9+j4UmI4X3K/chDzVFfCq8fG6mhQ/Az2vpHTgk6zzXgu1pa+HT0z4hYWPyhD39/tkUHzq6XYnXNAcYtogm7JHXgPSGvLRsHipQdK6XvghbFMSX3psJY4ycHPBWIRByUbMzTUldk+CsqEL+aXKMh/+ehyqBatgDY5/JA7DLY74lANNV9cc5Rw0TFEIJdKQCp3qFDM/2SOCPBnd1YUQxJeH4ydr55mLp0DdraRauf0Iv/qU4FKtpq29F91bzxvKZY5TII/ej2/8MogGcX/jRi/PwATy92Gq/P0q/lE/Xy9/XQsS7IROISKDhFjhRMgMXEpP1DCiRWQoi9gRIpwMhjgSDSU6Mg97FuILKVfDhOI2zoSoslKQDF6RZYaHUax2W1iMtFb8qxwtoxR1hDduhi3l49vB3KwuRAtfl3CQUMY3I9SBH8EZxtb3wceD+kt9V9vXgvXP/lrb/7Xp6vDZBRuhgB5VI0XDChEx4aIjtsKbVawxfJMAFcS00a6SqBOkVMmwJYNXJRB+LZwQkchkuOF9JPBQqQrudRUBjwYKFyrEXU0Uxwt4W2GoZxCqGZUxhtv8Wc3S4noBzxnJmEEwD1baoLr4Rq+AqJYltv/aLN396qyrw2cT1tOn9XTKQGPMxyCEN8IDuSCOBRATycVWRjyIv2YeCAz5FPxRbLL4CrEoPn85hli9LJRXF9eDyzGIXRuwDtbXxe59EQJbNdGcCaMc4H9MMhsjZshPCpTG4+QRjbIsSGlSFRlWIQ3QQovNfZs7wVWB+vX5r0DQcgsQPVA851bax4vuNA5y3pAgqB0b3X8Sz7C0FiwBje1iXAloMauCz0f0h4JZ0AaZcoxO2BCQm7NoOYXEV8q+X5mr9XLwcfVSPMfhdR8K5Wv6iGlMoXHmtQD16F3ive9jFxAquziliITKCiKVMCK+ojJS8lbGS9+nHoxSs20hs+Zp/JiHy2oF1NsRo83EiWqgxIUShuNF9qGoKpNZf4SqRJKKaDD7OJJkH0eZnpJL0FeufFcH1/LAWbhveHBl3j6+V4pNoFZchmlInLFH8Un7S2U2VY1Ru+PWjjTDFa+BdU+aguDyC1plt75UDwFXWgNKYWDy2HqgT4CTEoKFg7V4KD8t6H0aMOVkpZrkQJEqVSXNQ/YhGxu3sBCKUZVHLqauoFM/FOmULFEM6q8ig3nlQXz542Atbuhp9VmKiiDMP6vj2mytYPMm7qn/fB+Kz1pNVUF5WRzdaFQc0IuemnfCJddPITfh+OfUMhstJjOjqhZ5LTPJyi6+K42YZpkFZQWgW3l7J7DrShzerE1ioDEslUqfeuw+21DbOt8LgaxkNIY9rHExo4n61403Kg10pP8kEtWw/JVashPjy6jODrdxZxZ+xAQRPpitKhhHFSlaIdBohpnI5rHFJ61QVkGYl8tElwRVZWbg0xPKig3kOQ90pxFSeQqzcgV88ClVR1ETn6cB/RRVTukMLQnWLLtz9VgPiutAgUH7DBTCxCsx6B/SZgRCJcknV1dfl0g17cKq7GPSUk0RP018P1J9C/rR9bNBWMYyF25X8Ycyx0jhEW9Io5/GqBZ8Bnbx6e8HHxfmK/C7BV7GqKXrtX6CWjnk/kB6GuBChfqO6JbDcZeuEF3tW1HBMPlopKy5KP9mG0oNn+EIfeSEQ4lywI813sQvha8a0ChL8FeLkyGboAxQBEIhrnLLTCXqynsvZ9Q2w/IRva3B8UpgJ/BgE0S0omr8R09RRleZVkNZc3SnLAiFcJFzndIXw5NBnIoZAXlv/wHfCeJXbVJrNoivBJ4E10TRiqBjPPBWdRCP0Z/yMn71K4DNPUuinGqu7L/acZccut6WJKiVT38ZeKPXp0/xKWE9gkoIEdRWdj3Ser/1bi0ovctjPRgu2BipOZ4ZE4IkzM2Q0wmjIoZBBJYhAVDpjfibv/LQ1cXybvVBP0IuJ2DImb/d6NbnI+dA1VNujhCv+gcZujDemgueDdZ3wSeA76/1fVf7rGstAq0Pq8PnAAxl1o6VPdr4cRIYxRPxlNIkfyKmMWSHl5oLPrWfJ14JCjDRsnJ3mku80pmRjPnLOdFYZNH5KG+7eLC5JEOcM8atgXWP8nD47up4f5B/javF1ZpbB87jI951+MzAx9GaWlrknD06WEGNAAeMDnvcWQuW7KPeK/CxQWsCgof7Zbau+gr9uDzvF7YuuYH8ap1LpBkYprBk6m+QGfvFT2n5rhdEPNyvEIOPDTDwfe/5xOpY3D/d+vA1fN7+XLW9krQKjk65qosvqkHyYxq1MaBxCg5ydC64rHH381zvFdz4OpnXSu6uhI+DNeULapKs0LeVLOSz8vARqIm2cqmNvTZlECoa7Dw+Gq7+Xtmxszb84+4drPfxJdwHbGydW+m/lXJ5pYeGSzl6two1Pkq4DmrjfiTYcGmdYyTJLoKPwzt//6nARw2uapH2y5nBNmieLq6HmX8QzxR/3eg58HOw5uFjwSdzFExtCFrPi39yTr8BT1+jFCnEp3bOQEGKb/FcP62WJmAEfxuAC3Wea4P4VCM/ePB3a+N+FKwq9wGrPcdJ4+jlUIHXFb4Y8DGtr/U2ZLpPLzKOoyIMUxw5m2CBs/AavDT/AC8sO6a0qEpr/07/NqefdTjnwdJ6fxdmQ2Nz3WGIS+0wy7AriKp4utUIWljgby4A+QdYvBpG5/P9dOBj3y+F81f+bimA0qktHmhxImrOlPmqFozLZstTXLcA7CTZj2ZrPUxQ7VVhXleKD0bAE4Va0HiszNVPgvVpVzL/nQTR7jUyREAbfjVgejMqyTglcEYcyRQVOuVuI8e8nf7PJ+LGWmOoxwk5Xwel9G491NDh9dENPI2uSesfa+KsceseHejGyYNOJmQNA+cKZp/x1kgGY0SqslPIQLc2jpvYugSVVZBBEB6A81aGdvOxoHgrWfwK4NOtOvd3vwJr5VHBr8Tna0C2Qcvh17XTy1fKV7BYLCIWc6vXtZWtRWzd+7D7xflEEHUVbdFtYMFdTSXLbIkNDCGvbYsEIXuMCczqa2UpNntBFyNSujKIl1okNRpm0QvMRBv5VWf3eqNPZjtcguWNSDDh3AQSuF9BJLAAuwyd8OIQUuDSyzrrBp/ggz4BvBV0ff9JkJCfVtB8HO8v0DjJCWrT1uGzCBwfjZHhjYPqitJLvNGru0akA4TUSoFWFYSgFqZQieuKH4wx81vd2kugt5m1AkXKQ9TvOghASk/JVjyC3RseZXy27rIC5r3eU8AAzYDVQFeuz87atT6htde71YugNmaNdx0+Q1BLZ3Tvr975MDFtd28XgsKCEV7xY1pza2EFey2APzXxBcEMMZDPahG1IQKGrFZgpXiDdd7r6yBYk3ctKLIvKqzdRBLD/e6LEBLBdCvxUYuGMgu5fcniaK51fueJfuw1Qd1aesL9KmOegVuplPJa7b9qYFCw/qfzBgb/XAt+rAT+3vMSU2aDQdDOE/EzgciRQBxZ9ahYq6JWg3Cwc9TxQjlXN8WTod1gnQKusBUGvAIM94V7CHbPOFxRmH5deStgtHSlggZV253t2ua8+BsclaDXTjVuUi5XeHpg3XOpAr8ATApSVX1TlBWLU+6uhMCYYvSYzvdvOGHKmZLJR7V3u7mk0LnMtMtr/euNq41wFwN5rTzrpiaQNF9PvjdXDZW6MbUheGlEK8xhRP2WMAErlQnaEmdtY1Zjhvsd7LVQk0zga+Cvpoh4XDNP/gSBupQrbjdXLf75+PK7H67eF5Tc5xugi+OdPl/lQRfgrpfl9BREX40qsGhKH/SgV7pskq6LGOTpcLcmV95qFV+gMmyByeODgfPVWHt1zOcs3FFR7rVdxWfckO9/H9PH9vNgFXxoUBM+6MljA8HqFVROdQju/NWDj+GvBrWRGKBxEo3w9EU6gmRS0Q9dNX6f311fNX220sfB+ImYqwNsoBRPhN6HJdgxUr4ZFshrntbY646GR+pVt3PFgziHp4GOZ9IF9EgXOZfKQcW/BuiojauKz2/llT2m8LQ2CNMOMYFKsprwJ+6js5olRnV0z4UlfVhQJeG1SlZYQ9BFHyHn9wEXrFxrr/KtTUh/7XwlZInzkmFjlFnjlQJDQihGGi0sWskwpMy6xJAPJRlSRVM52LEVDl599EUIWD/Hq1RzBWg8pEsGZcurNv5KtfwuMM2/oOPq8Ing6bnmvu79s7+KNnxquh7gVyWQrdYOUcxkJxIf/uiGeZL3aWr6mSHc0Ztf0oPEW80v2CnmaDfryPirLNDN1xWZTGMe0PhiMPFEsR3VlL/CzdvBSj7y9AG/HG9UqlohPI6uyAKuQNtVzqxk6CsG9CTOmM4YrgJXCnW39hgYCIM6OO8gcP1kDW4V34Fi1oR/aqjtCA+r+dTiRaFQML7wqXGhBn6jrzcKVFHP0FTJUslTQAefxNB8Y3xjPxGIiKL3GsOKbUMnMJmQwJ1H4I1eDRYkgVDbDGX0WpGVA6Q29GE+KzhBUFqBXkmwO70SEc6Zf7XaGoRZMjN4mdGLRUdNeKYSowBLqLa49uh1CAdBebpbMTK4ShnC8s9SWPpPhvV9pmc/BrpfjyDyr0Wc2vHyiksdPmvgsdEpW3YnXBIxEjKbwOJFYd2SxK0YvTQPlNJesuFdgA8klHqdphbKUn5W8NFBhEygFoNUimcG2mKrMCOUvLHSayM7b17Xk0S1YzWdS+jLXW3r6n0tyEctXRtSm9dH09ThswK19MnzAk9/HE2iM3xw4HBag6orw4LBFbkzWmzPzlO/bnrYj0LtKnD4EvgEeSgTf7tSTgA+fk1ku1uN4cDzi/tBMFVXgc8W3ScKXqHTK4ClQBFJBtaFIqdYJcwZyzr6F4xLNjep3mha09+EOlko5GuCid2tluPBGJ6LZ78WqHhqtYupX3V/Le9dzzsEfuw8D6nlH348dT6SIEytS0Yv5eirJ46sIwm80UtjEAmMXo5nMiIjO4rB2gVGK2eUqq2PGhmEebB+dXVYBeZN7+pKmPL0Im6Qo/IOjF6+9Wb0CgZQcexWryARShwAZadxqDV6yU8K4CruuF8ZqmwIrFvYH8wseFMyiOvG0x2z4MVZ1UFGLy2MuXoZLtCtirzqM2/0EnUPam9tFfirAxsJi8KfIMilUJ2Uo/M0/OLVaKrayvsVVY6D5IxedLowYlpDxjbFOY4618uV71/RcGW5ctaC+SmqwEUzMLxTO72yIZCfe292BYR3HhflvNHkfni7BlQW66jcq6YFqWzXnyvAcFMSGLIiyzGq7+MANdyTFcf0NsiEFYOf/IJbDyvzVMIjU1sZ8iMNCOKqDMMFM3oFeVqbpD5pV4KruweldrsXnBxgfN4bvfzc579yUDrJAgZBI9wvQ4WDdiefoFyChVv5iuNwZRVWH1bumMDd88Zl7kCewdho3DReMnp5muOvv3T8PrMQjLc1IxhnT6NW5DUGmiKqsfJh3ujF9IGS6o5qYVCt0YtxrAtdNwVhbpxEL93uX1euM8zzhnE9Rayu0L2A3qkqQV7uyBVePT7aVY68SAXyVlHlVKQ3eqnawlvNEdVE+a0YvZSGWZnRi07ZNPomq1L0M1CmKw+rEMxQl9BDTb3cVRQ0MHqRU0qfilVWjV6FqDN6xco1Rq9wkllW0VTRJgZlGRi9VvJleRqq9UYvOyLE9a951VTLdSSd72MzfAdxf4fBz+VaucLD+nmuOD6e6LlohJ4/tV6q7g+IU5n4vNboJbNwzHhbqBIgIf2q5Cmip37BIU7c0YKDzFTlsOYIea6bYgTVw/HjFVXe5rEbflvg8/OHULCJJ2qr3HS7GrYWVEurfPBYG0dpVlvhQS1QdsJjf6yByYdsi0iI6qMjGArBWePe6OXkROW5Ck6nFL1QQ1fLcrH4yzSeF1qPBslX7u0SeP5KsJrXKhgl+wguaBNVNOpoouBX4RG/MaOXF3xVmdoKyULnkTaXyyGbza7E8Y3y8HH+DtY2siwhh4Ms3wiFIxMSSHBstZCIpcF1K4eOsFVAAVKrZMzfCZEaQMNKKu8SlgyNArcK1YqIJuMxn1A4w/sQIiVnSCtSYBLCqOxIUGdvEHBCyNq81h6kp5yU1sdx7ZN11vmwLwzRfjmsJxC6eoFCUCpRuQrC1L+1cQTe//79Xoe/a+DIES8criYCRo2qBCXiM6l4MSKBRWNHx/9YOeYMrMTpqu1OpNJCRm84FuCUDF6xYIXMj3qJAoHHXw/xKvGeMXwcke9imGUTonZIqMoUYnti6pFcKehWCKl3AsaxeqhNrj5Sg9WG9XPG+QX3Bj7+WqidKmvj1+GzAqIvojMC0STRHW8o0b3A0SQ/gKuD6tM5v7W0yjPtVVi9t1S1yPG3BFeqg/Wl/TKoLV1V9YqznfZAHlbmHC4HJ9i35l2YzmZxCyKrqYtRN18TxajtuLGVvECoWRVmVmuqeetq6ubg2m7gAz08D3RnYzpBQ32tcfGKqa7y805+Gi8JIbr6eD5ttGaXguiTDkIuBOPbltdKqs6maKS4SN4qnh2ZtrBChDVg+kQxQacD2qtUWgIroA57DtrlgO2yc4dqgW0xZaMGTAlR+7VDSGFMJwVPyfVj8EnpXDyHYo7uScFT3Zy/qDOzDKTgQpSUzCILXLpkYM1QGnMuhPHobEeAVpjzgfHPcrWxL4SCcxidD8PZ74Gi7HyIScxDMVxZvlwHtb1VC2tjqV6BX5BAhjynDPOH/aDwjJ3ro11eCSq8MY6xMIf15Rhk4jlrV5iarC22qC+D/gwHO+Z8mevLFni8FP5IohMO6d47L5/I1cqZHhTnbwvaUSlIcrhl/ypyGHOsunJvCdArw2fJblrk8QfYa5wFOoPV5DQzkoof8r7sFkUlM37EMFtpctdwmmHCQ/WX8EpX1yZncNUrwEwbGDUUFtYct/LUz9ZTQZDiyxCrBS6P6wHumPyruvr6MpXKZBwZns1P88jwndWzLPlTaXBx6e92kDkQ3lk1g7reDz4yHvZIfCG9KJHui7ZoTHXv6b7SeF7g5dLPHdi8l2Pf+P4xP8LKYfUaU+EJx8mPbZk4ofAVHOJF+GA3QkL1v2R20UDhiQ9jXKVReVZmlHEcjbJ0K2Eufigk/YX1sblJx3xs4YEQCS0HYS6+/MvBhoFwKGVhokmiWZonjcHckGKvOWPnhTGpwpqDMNFJ+SuOrqIpPsyfL/argu/WVWB9Atqb5wSVoh8njUiUZfwNoaizmhQo3U1zSm2rxqxXmqlICzLRCOe3ZlPJzQVBhfPHFo/VP4ztx8aPp3K1/uXVdE0tPKhRjp7bXPTjK/hoxX8nwNPp+9FoH7aepntaUCuDyK+W5n8c+G4Wrum2RPpSDGhMtFIyA5ZouAxUkktyxE2hjzcIN5hsRRknXCJvcLgQKctI6miucpVB2eQuP768RllPp8uLW3Oe0JVDwfyhnuUWsz4diJc6WG2v8yGeyUBOqGgDTrggqoB4cPZeLpKwsuNkal4+LNih5GXGcZsXJG9o4cTl7fNXHOXhnQeGr8iVrg8dKA7b7uv5a8RtjXHteHveL7/29vYgFsfyVzCA/caMXh6pfQU84yqRsc3Pz2NsbAzj4+PIZDIWx8dbn+7jYW24DF5yaoYIrdu14pDAGbxEhCSsO6W/TCHAFAyWY0Yv3osACjQZhKZrBlLAwfyI0Yt+ER08SShwZomwKa03enkh1q3aroJCnUCxCk5grimP4OrGG3obEf0lIKIgxFB/qw91rz6VfzKZXDE66ln+MoTJaqq4evZI5cehDp89ECbpXAJBouIP7RTxo2BCguY+oiAW7yBaihIfhdskZnYgpyOIDrEk9EqA1qsoAYMPQKtgzui1iqhxlrf6pLqsGr0ikEGMYPkSV/1VsEJE/bySZ4BjRkgV311NJaohuqvlufirzw5qY3gIcjb4aGgdPgsgGiV6419p8X6iPWsVodoRXD+ael71c+o03ZpowjmCea+N/7eGmiIM136VLGvSutq4+knp1GuNzujlhK5WN11NIJOC4VMI1hu99BXBUnAAsRPICCtCip8lKlxx1FNBRawBLp44kKCqXSUBDxA/8PzY8wWNjZyeFaZx8v6ef/jxjZTFe1X/kmsb21LUqimhVdvUGbeIJlKnwOgVdUavvAklMnrFkSxpzxDj2cn+BDvcNWijAdsUHPq8AqJ561+rCxQVfSXZfdFJ9V9NZ620dF6Icu01I4D6Legy81oxejE/60f2nvqDt2aQIBQ4Ho7P+/6nIB0YvbR+rHQqQcYqxfCLDPFKXpjgwugv2aQQ0Fn5uIU1Gb3ceCu98YVgHC2OpV4LQVVWISjfg937OumeIJTSIblmQAlee0rHXJ2iHJe1Rq8isvEs68Nasw/CMnjaGLh2Se30YH12H3Bl85f/YbbL45NXhjzuCec87fC4JuFXcWvDPi2oXL8QmWBTvNErz6qLHa03eqlf4nRKpwVPA8mZbLcZhgJei3Kbu2rBSUaOWjB5kmBGL6YR7hlua364ylRNYVbfqv2uD9STIc55GUNMtjVFP6i8xSfuBGnsi+A6uFtB9sXxoK4CDkLYwrUArDI1KNp9GXwgh31vfibjSgKlwqb8+eTiKjc/kP76yWCsnVE1rhXNmWA8vUyqe8mkFjcY/88ncKzUWEP0YGx833uDlZRfo0nCi2BsZQg12rKKQyv03IxX4pF8XplXPizIx4qQn+aC4qizlU74pbqoXD7K6KXHYPzdIoCbp+FQikHBQLEs6TErSnto2cJEfaQ3kaSjKZjWotl6jUvzQ0UpbI3RKwg3o1dNOiOJcr8iBL1ZA8Jnl1GeE1Q7n2PlVaNXKeSNXmnWT/3IyrBt0r2aS25uZiLkpSZzUPZYMXqx7Wao1O46hbHifn4bKFf62XhzXlq+dDVGLzd/PfwtGvs7BqIDRiNIF0THJRPqWfeeTnwSaEQCVDBabaPG9EWOryBK/qmPFuhDJTKKScbKRyWnkNcEfK6h4AxGMnqVJW8xXriS5FA6mUa5iv+b3CVaa6mYL+ssDLA6MI6MxqWVo5Vkl6jFhU+GVaOXy2sVxANEJ1hnb/TS5oUg66y9phth+7zRq+KMXqxfouy+MqmFVmfodm0xEK4GNTd89mCdud4JgrjmPPiw/zHwfEHgeYFsGCXy9wcffBDbtm1Dc3OzhdfCJ/GM38rrjaqgKuEttceOHcOrr76Ke/fuoaenxwQVX0nFXwvyl98v60QRHFFQIrQQgYNlQpquWuUS0RLRCWuVgmDIwrhkFPp6k4OgDnYlMecg+91VHvEckaSfGL+VF0K86ASXXIyMgJRcRjNti1RYPiJCGSaSMUfLQgPIB2aRjTiC6FZvOEmImHH/noMYHkFfmJBhTvVwX2f4ZPCIoX72RMMTicbGRiwtLSGVSplQoWf1v3bbKbw2rZzGqw6fQSAeSfzUr4QHA+EqA0T0RMwVSehmjJ4KptslInDG15i+UlKDTlKopSbVgnzW7hYQLrpyPbg4wmnOtmCXiWf6TlBbLVdxTCgz5u8ZBB9XBAQvwDEsILxq1Sro3rVqFdbWzzmXUqD61eGzCaJLJfIG0SLt+m1tbUUikTB/0S5jeIZbAV4RN2xcPU3mvY24hti83Fh7zLc7RTffADtsnrj0DidrwWIEKX0cB+6pxpeRamMEVQrAl1gLqxHsriaKX4gpVVtZI/ILCeMUYqj6IRkI4kUKZNrNHKIQHapISKdnxPEyt7vEmTgk2Jifn3c2B1WiL5BXi6Nn3Qe3Ft9ms13tLqiy58leyNR45fN5c+IXWnFTmF888fE8Dwnr637MTzTGXpnmXHciIZCoutdMSpRA/BkUZoS3Gqhslkv+GKGgqLpV7KtbiuXqVAvrx+x+PqsDxfyN5unW45fPU/3MNvAxiMGr4gThAcKZ4sm4RjctL7bT6FbIdtcKihSW3fmeq3WRkVIgwVrjZfgYyBXi9QI7S4T5OUOWo9/aeSvQAoV9WVd5BmOjvlMJLrWvcwB89O1wYQoJYvLia+ZjuPZpFimEo8Xqm+yyEjeEDKuidsuoFaXMIiE/rp3CHCutiJviAMpYVN59/ppvbvHPzctVcHnWgtVAbaN3WG3jfTV4vTFMpcVkE+Y1MzNj9EKyjJz8a5Uij7ufDFaa3RVM2aVMVyEOst22+y6oWmPJxVPbS2yf+kQbvNRdPo5XIMzoZfOa9+VgRdoMTk6uW4HanV4y2ooHalcJ00WDndea9yWbO6qLm1sad73GEmG/25XOho0ghV0qjXY1qP7CIObAK4soO1nV8XvmQxk2Bu3qkTmS5bJ8GW6F1fr1uyJEM5RC4ycnMIMYM3FjGXSAQe29A0X14G75y/9UKo3lZZUPoyNamLWxVntqE30uQfRAHaR79aPaY73Oi8MTF0c4oT61iLyVbqJwPhttkl6hML1aRd7I/teckpHS77ZSXsIF/6aIw1tHbwWSCWUk15h6w3oolGYq4Y3one6kmKtsspbAsOUoirBBS6JOuYxjnr6qg2iOx0fFC1pgtw6/3N0qeD/zXHlwUJNDzdWDQldzUs38nUHto/UtL6RDZppj3eQMqwMjlDvjiZSV/aU3g5RBtCK+RJodUd/JRzTW0fMVfdEXpDEL+HbIG65trNzccP0ht9qeoItqwPXd+pYKPhL1dwi0WLGwsGAbYkTPm5qazE/0XM+SKz4NXVeMYtjhQrK8ejaXXvuTPq/x1/TUApV2ZrvzEd2YRIJdkCt4pjiGV5Jj5CEerN1SetZOL3oKxyqaI8Il5sG8xd/1aqXhRlBlJffzanWkFShXI2cEMd3i3Kqvk9+Ev8TTis4TZ3lIsz55i+N5hJex3BE14mdhJGwrM/uPvMbqZtXWD+OI9itBQHNWnQeXj+sTX2/n4+I53Hdhq+GfCLXZG7h0rn90ozHgzOXYy4knLC4u2oap5557Dl/5ylewe/duNDQ4g7yHT+Idv1Gjl2deEkKErL4i/+2//Tf82Z/9mSH2N7/5zZXXImrBx71vdT5KPSgYZelEhGQZbDLEFDIqapXP1SqdBiXiGGyoEnfITuQOUeCQEOFzLZEpyLilcL9V1l1WK6MJo3foRdwSgdErExi9JLAmyk5gyUQlSETQWBRToocQKlhFS8Ucg/Hb3mPlCJJFWWfl5wxx2WjEhBcRbU2kXwar/eYQRc+yjAokFEpIPHPmjCHO9u3b8fDDD5uyIkKiuBonP2brx6QOnw0QobaFZeJnOhYIMMRtMekYxzHBsXPgfHMBDrl54/CjuagdW5ofbo5IOCqGAnwMwB3i6PNy4F6LXMULMRL3WqTeF/fzg3PHv9rCuKqvI9QyZgn/HVHVn8BtGRcF4lVpFNevsAX1tavlo3tfjq7+3oOvm9rLixW+Pk4dPgsgo8ns7CxGR0eNF+zbtw9btmyxMC/UVKVkGeHUKEpo1fgScz0uM5rRbnv0Y+2deADvDGcUTFYq5x55DQiqogaeVkZwXQviD6s8wgv5LrGDFa8av1Vwgfa7Ehz4SeElFCudrFGSbdEiEQU+CjE6j0RQ0OozubTxLSrFUsjD4QULc1+j0lxTxkGb7Jn5r1bKgfWR4uhaW0/Xr85IptugTwmej4tPiy/Mzc2Z0KEd21JSNW5SWEslCmKMJ77heYj4yeoZXRIqNdc1z105EVO8SgwT76QH/cPk1/78L0FVC1Vm4GObym2u1qYo1tZfo+No4So4mlgL/vUUa72aa55S4AQ+P+GIcMXFdFffr/ZgMR02iG4JZxhT+QQrxPGAj5eiMmy5Olip/I+XXFhZSploHdO7evE26HP1mcoUHqrfJGL73b06V9GMXuxjD94gZvVVITXg22GFr0CA5xxkn0Jlr8ZzTnVYNagwlPVUGr3yp6vOGhKtF9/R7jTtZlIfSPYqVxuZgz4Vrz+2k23VDnw10bJbA2vnm5UetC8clkyiZ42Bk1HkSsU8XnnlFcO3vXv3YtOmTaYcSZ7xxvNPB6qT+pqykpQX1kXnlDn8CwaEkCypDYHRK+z6RH3jFjNdXKdosC2U8bwxO1TqtKszeklRqgFTktg24bd4nvDAjF7Ek6rbxS3Frcix1+KVNwyL7zpDY5HXMnR4sTd4+LiFsHbnELc4v6QUqZ6uLs5QItoYFo0Ju52V2m2pnSnudVbhB/MIdkU4edThgmvvKqw8WsMcPq1CbeS1CZPJBly5chVnz5412vHYY49h586dK+P2+Zc/nZzjOkZt8f3C+xXcYrjRB+G265+Qf/XRPfBHR1a48HhZ4+4kJ7f7V7tQXF56TUvRLIUWSejtXxtMCEeYTpheCgwBelNFNETjKVwXbS4Gu7kioSXG9PNe5vc4McW9pttYnWGY5ovqKMOXcNSCVvLyfFbN9GECF+5cbZieFd/VVk7grwrxTlCLY6vx3a/8A1oo3Y5jIBrqjIjqDFeg0w1l8NIrbgGdsLd/gj5jmNJ6A69/lV11NtCGhxWjdvD6MvvEZFfCij5pGyOYjk/Ox2cgcHXxrayF2lge3FjU1OELAKLxXmf1INp+5coVDA4OmsyxY8eOFdquuJ4v/DJQf9umE0JjKUfa5Y2+pG0ssuTPywv0Dr/4LjoaI73UeEqnEa6EK6SLZUeXy3ZIVoE0V2+2iNdp57rawLlQ7rBrjMKMcFrG1VKEtFMLd4EcpHCHh/5KMLxhghUDuEB5SpYKcM9+eVXcQD8qV9vNP1FNWX1ED7yhT+ULNMfUZtkXWnNubugtAdu9xkhqn5NBZBNhYCCvqB7CWge68/iqejl8tjuNB+skmlAb/kmgUCvKZ29Qky7wd2119+IHcpI93333XTz66KP4/d//fTz++OPo6FC/r8J6nKqF37jRy189sur6X/7Lf8Ff/MVf2La0f/Nv/o0JKPdjcC5NcG8/azvEgx6jJMkRMuYKBy8voZmKfhU6aJ5/Wh2mE8kvRd2upiifIzbQEgaWEdFuGK0CGLNwTCWkbYHlKJkD/TQfVH97H7dqK33GbJhHotDAZCFko8yfgxSn+NCAAkpkUPmIvgwSo6ArS6sypTCrFT3GzzCWDU4kwxw5icoxMicKiiynQiRWWDEqwUXKjpDY9V8t+D4WuP5yz7qqT3X1K/BSUKRg/uVf/qW9Xvr0008b0iis1ujl09fhMwqi2EaoScziVDQ1drzXDLJV2hIVIuKzXIlhZc4FEWZTGoRIhATx0RErElnhMoliaZ3RK0qFW8qVQPgg/NCXbpjA/AQSjXX+jCqjsxqMIVfCnFtiHiyXxUVUtgkfKl8MQ+UyWiBQOKYTKH5iPIbsVAgNB1lP1k0Z68l+1Firgh68C7wCwuyYiXwU14XX4bcP6+mIcMiDVvLu3r1rRnjRo6997Ws4cuTIymtJLi0F08DaLyHbGC/Hlthofja8FOZFig1NJNhIAaSH4iilBFlF90YvqYGWkPECrDKwO9JaXRWiRLrXneXP+E7xJigfFUh/1dPqqogE10SfL/MI+kDKOx+CZ4fXrq7kU5woRXSw3CTrR16g10soJNlr+szQ7fh1gkmkRH5Z5rwLL1j6POdthQpumHiuQ1nV9gobbX1tfUVgmeJjjgbIxzvVxP+6vhXYXA3Cff3FG8RLhoeHcfnyZbt2dnbaatvGjRstnucjAo2h7kWHBFIgXB+y71hflZknU3Tc1r025VZdm9gOtVVNZ1vIHyuRNPuIYXpVzPLUqqby8m3QYlfCtVEr96yCMx4WGceiWAtD2vVtfaJdVKKTbC//9ZqV6xvfG/xjPsIAUww11qqp4vFPCOGyJZ0VXrK/9fqmdn+L70ZLSRvTSlR+oqEurdoUDY5DqEgYVvuFoJQzIhFhZnBmmnKnt1aetaNDq9AO92VWkTLm6LJqq3y1e8PopI2bB1dv+xKn+p4+ap7appa5EVb+ysMF2qvEmkOGR/SydIql+vs+jlCuUb8qF+Kd/lhGrJxHOML2EpPVR5VqI8ug3MVGVyWkM2vjT1auynQ9aDii9vHZ/FRJ3SuQV48/FY0rISyjF+uZz2Xx7//9v7dV3q9//ev2uoNkSeGo/Eolr2SsBY+fAtcG9bL4E+XfeBzamOg+WCQ+psVGV652VJX5l9c5bTpvTn9sd5R114H+ql+VdVVuUnbD5GHq/3KhmVfF1/m17NegfOGcXm8UDlY53zmTWSGOY3B2Uqzqjv7QImyREq4OUq7y3mrD8YlxnPQ1ZSlTohMaI9Xa4rJOpTDbIpphRi+WLXy2nQEylKjFrCbLTITmrZxCVa9hatce5yEda4pijHyceQknNRZKJUxUSk8LrT+tSfrRuOveg4vrrsFv4NXU2IzXXnsNP/rRj+xtg3/4D/+h8QC/SOt1gtrx+nyBm/eu/WwLccnd17ZH4aQTHE/RLv2ZAq74QVzRqiLnlbohRrpvurrmlHYkcUz0aqDmfqSixUbFZ45MLsqqRXiXTgZLlcYRJA7ZyOl1W/rI6GNh9M9LV1I9Qk7p18yTOKbXG3Mh95puY2XG8MAtMgjftShjQcRHUUMWrnOFhN8cQ21s1a1aI9FPO6tEB2U016uOmke2x0SRLCLDGXlFPgz6wTu1tcw8hJNR0gKjLxaXaRkeDsX5rLmpI2iUn9IJyL8kl/JZO98kK4i2R5if0om+lZlPRXjHf304QjxY5VWoAIr/lRnfcuM8Fk1TmN/p5epApziMpDYqnu51a2XwV010wLQM9I8r3gRLq6uvOp9rblcfPmfgaf4vgzfffBOnTp1CnPRYeqrkQtF2pfcyxv1sBrWgkgoR4WgVCfImGexNvyCN1UjJ4KOD66tuQtGf40E6LgocCc68KkR1DilnTYX8uRy3cvOmM+kjLW73mIzLMnrZnK02k+9IiiO+0EfHzbgzlhlfuCXmYnRcceW0g43xSixPc1W7wgLK7BzjUl5QW5zjr3BKsoOeSLOFdtLBoixDel5wyAziMriyzUWWpQ8j6ZibloLT8YrxNNsV7PSy+MJxyi3itcR5x6MkXwmfVWXiPqslXqW+s65kOpdS+K4nJ2M4icEyXsFfP+7umen4KPoUBDsI6KPzc7+2kKg/pvd8YGhoCH/yJ39im3a++93v4qmnnrI31mr5RO39eviNv97oQQKIN6jI6PXiiy/aqs6//bf/1rYv1oLvICG1MVuCGuEbonAfx4N9HptEqsiOW6KwJQNPpTzDNCJcFLArVKTYxEyck4aIF0cjHRG5uEwmsoxoLIGCLPZk8lUzQpHYkSJHi0TfKImlEW69L7tIIlfiZIogF9HBhjEkcsxJzyyrTIRJUNBtiBYolOXJkBoooJEokgtVxQgorIdjei2EiJhvsTaGo0sk4lkWkEA80mkMMF+atf4Kh7Xdm3US8rFW6wezth8UVoscPsz3l6zmeqX0P//n/2wKi3bZ/fN//s8tvvpZdanNrw6fTdCKnN4Pl3LXFJ9BtShlUcycOE5CmifRjcSoPMcTyGVziMWI58TNCoUAUz6UR0UrvjIj5OhELJ2Q7Ibf4UBUwrQIMB8Nr+hXED5aqIDMgdQrZl/GqSIfc2K3krBEE2SK+aIZMSrMSzhslnuSAQl4Rs4kAInNiOCZoitBgCWQUeiT9CYAUhhjAqubmwdWNP117+aFwLFA/QYMxYBhXoKow28d1tOTWvqlVxqvX7+Ot99+2+jS3//7f99WbyToeLpvBhwqZkplQrY4FRHIVGdDCMYjXY0ygthLmcKK6GdUOMeyJD4YKzbaKGZLbCOdsy+hSdEw3BFzJy5KgA1LIKKaaNV2oSYkMwsTcEoUdCWkULmIRmLuvizcdu107dP9Kh1WWxQcizlhXMqxwqRMlijsxGIl44/FUAvRNsF5R0W0suTSkr9I0MjHmI5KjlYjI4UYIqxgI+bNsLQUaUQ51sB2cd6xfsavCtplJYGPPFRto4sygspxNgRXR/27Wuo3mDsEz2/cPXu7hjfIUHn8+HFcu3YNGzZssHHr7u62Nq3tB5e2GGtiHUJoqqSQKC1bf8TiFOSoSEzE20l9wkhUl5C01Uq2r9zI+OJ5TrAtxQoUHHOoULtLlFqYN3lmPMU4boeyICzDQKHZ2l4x6Yx9RV4bipCvsr8FqpGtykvorZJmUcA0mYT9VCIulJWX0jGiLQjw2QyqvI9GtftCfFI8nn4spywZgfULc4yqlB7LMv6zzGiU8ka5ibhCPLTzFR1+qBaid+GwzpVhIayb5BMJmxUKGEnifQRpGyPt6nKvL0mplBwgfGf9jCYzJ9WPIH8zELMPJZiaISUYN8WJsm1VyivqExtd4qv6T9GE/fZ6FP3VRcoronIqpL3FAmL2FexgBhkNZR8XW0yOKFdZT+J9hLzFBGGdEcK5FyOOmkGOfVchhsroJeG6GqZMxSZrF4gZEJmdDEaqh6uTxtvhqQfhkMZX9WUhTOLmjkBzssLy/uW//JdoaWkxHNROIZP7mEbjWptXLXjcFCiOFHjtnlPfhRqbkSX/lBwpY5s+OtCQc/O1QtkxW8k7JYjtlnkvz3bHOd6teSrwHO8K5UejNwyNRDj+7P9sWucWcjzJf8NMqwVWgcatQkXKaBUyxEEpMlKuOTdY9QhSNiYV4muJrkr+LmOx6lkh3YhyTELQ+TBUvpiDxkn9UqaCJhlBtEQcXjgT0+ssrJ++WKZURY6hJIFQuYAmZK2cbLWbYWEqZ0uIcK5q5IsJ0hrWp5xnXizCXjU2QwppZGBUFF0RyE9jqnmk/Hz/y9/C+OxHRM9aBHjxhRfxp3/6p3bkxr/6V/8Kf/iHf7jy2rTy+HyD6BBbLMRnv/KB927sNVYujLfsF80l6RBubjpDicxHUorL5G/FGOU09oed3Sadm+ljerOEOCRDjeiR9IcKx956mXhWYT4RM7yy/5mH230l3IiZnqdziCRDJco50l/SEOJWRkZto22kW2HtDuNc4pwTDcpBCw7kO5VZ5iPsIJ0jXkpxducval8n5T6WU+EcMlpHvM9L/eK9Ws5qkb7TX6SM816LOaZXkd7ZYgVL0hzRn3i5xxOhkvFv5qLnEnFZxtGGRreTtEIa52iV48sVllFmHRQ3xHZUtKjCubjE/okR99uKxDHSOHurJ0b9jP0uHUz9GaYcLHpEwZrVET3nXClwnieSVq7RI9ZddEY0l8UzDWcgn6tMLzCc143F0dhrfqqmTqYwvsV8JAMIPVz7XDoDPujOP1puikAwdPocw33pwjq/H//4xzh69KjR8+985zt45plnVmi6nI/3SaAczbBFvHA0njhIehspJTnOHAOOS4W4XkhQ1pJRWfha4HzQWVjZuI1pIUa+wCHW7tcIeYHqsCC+z6IbqWNoZyW5K3Un1onxNUez2QwaiYMyrohHyCAsbtjCjIoF5hfnHGfZWsTTuaDCx2wmzfnMCms3sBmr1BfEG8kWlHlUILGLc5pzlnM6Es8aH4hUKDOKzPBPfEWG5LR0Lf41RxZZBmVLxElfEgiXYmgoNlrdy01znH+8ltSnkhM5F0nPE5RBOHkCw5CMdMyc5cSI+3nqchFWUrTD+DCjaAzEmYXhzIlx1VL2q9ExzQsGyFvMg+DGTc/BOCoTD4bYa3w4Z9lupvVjrvkp28V//I//0Qxdzz//PB555BGTPzVPBYpbyzt8Wg+/MaOXb5RAFSixQ32l/ut//a946aWX7F3Mf/fv/t19DyLzFXdCz9qJ4aG2IWLeIQprVQogJdtdxQEtL1mnR7Q7hcSuQMaSjumkiTiFtxB/KUQTgaJ06mxUmyjsMCoRjzSNE4RCRkkCMvuFVXd5uS2zEj3zUsY5wE2yiDG+thFq1VTnj2hlTcqYjF46mFQrk6quWwXNsS1MSoQlntI/YwKzGFYEMoQpW21tZwLWUqv2im/W1Jo2C3yfeP/14R6MQDNjKZf/6T/9J2jr6Le//W0zeslf+fh+FtTe1+GzBRqVlbNfKBhzcHknRCKuSoEi3kWoYEsYkVyqVXvJRFFS6HLVCbhOQWSqMAm4kWTOUSN+Gns6XsMknqbAOOSzgksy9Fqoq4fKjla0ik8GIQKlUAZQNCGTIdHPU+COi5qLySuN1solhIh4k+nzzwl3DGSFrThmENUJwQQZfCX0GXlkHSRjCORnq3hWC+EunVXIJo/Lz4MLqMNvET6ODtWCdnpdvXp1xej1j/7RPzIGJkFnlQ5pdEWfneBteG74R1zRL39sJZoCsu2UkYcYrIgoEwtvnGomeqbMiFukxcISi8dczRhLIm/5aWu4hAcFB04/ttuHN2EVpnwlMTA/pbL0ypf8TddCIc/iHb7qWUZfle8VdufP5zKVawre8biUE73MGGeWnDchLeBQAbb4UmTKyFAQ0m7jGBXfBBUTOz6vPG/tLEYbKdzpnC8qD5xAEvSLReWptqgsVlX15/wsGR9W65V3UB+bK7VOdbTLR0D53L59Gx9++KEZvXp7e/EP/sE/MAFEdOV+IE6mpsSqOfcKnOiVzrMshDCf1E6gsO2MTkoxMUmM/FoCn4aHUIxoK752nWpHjYQvBseWjX4ZnjFv241SpXLOfpGOYW0W3miRiXGMZtGzWmJ5evU6wv6IujEvsXJmLArGTKCR1ZhHVQ/b+uPxLrgQz/Ilp5xH9Wqh6s1x05cgXVkJVYDhEkA1WLoP0lfdbiKOKh9keoqZjMLiGcbesrroa5VSYJ16KS/lR+rOfqEPx1r5mdHO8mUI/bS7XGNkXrwKryIcd8uA4S4jgtpF/CAZ5T29ebEQH4+yknBd88mUcAn1WlRh/6nIEnmDyWbMP2QCPJXmEnGZZTkDmfKSgUXtYP9S8VRv2yuDDFbdVUf1lfq+RHwV/qg9K/1UA0GOK9WXTz6XM6OXzgIUDuo1B+3wUvutXxRrNcEK+PxXwtgWoxL0l/lIK+OcPVa3OL3jjvxoKqKo142Jd1XWVSMrp9xa/BluzNOmk0atKgMR8yomOedUnpR4i8Z+dAftVynzaQwiEa30qxCNI+cvletEVIguTFQ/Sg4lLgRVFo7zn7RP1I31lxVBlVSbmKcZvVZwlv2h3QlCOhkq2L48vSUfRImzcaM1FeT01UCWJwNZhPRG4+XO9KIipJ2IjK/dpIK1Y8R42qnAOz9+Smt4qL+auPJTDubH9vzsZz+zVXsZvf71v/7X+KM/+iOjUcKFtWV8DkH0wLWWFxsta7OBnyME9ZFAc0g8QnRa6SQLyagk0OtINj+IG7aby+a/DFPMl9FNMeS4myxFr5ViRFNVByEO6+AXEEtEBS1VRlmWzJ9hHcci5SWmD4ooofgt8Yp8Vbs4hUvFsN5M0atU2oHIOJzfHHHV1PBEWpEOBtfGbDMasRymJP0vshwtbGr+M4XqYbUihSbeRhi3qoVa8WU6GbBKLJcVMp7qjfTimbajlm2Jx2WAF/0J2q45zMxVToEyZzxOJT9IV7ZFWS0GJZAm/qvqDcWc4bNooOZWkXmWKlkq/doJo3SsC+lfWGPITJy8SR7D8dFVY8GsGeTw3PCVz3IrwAiSS2wesD9tJ58qbJ2nMZTxQPV3c0J+nm6pTOMHAXgckb8f288jGG1gG/y9wPehwPvJ6CW5ULu7vve97+HZZ59dsR948Gk+CfRGlmEaabEWLcOk06Ey6ZmmI106R/xo0K4nyRchJMnjyI2BPPGA4WXJCMzDjlvQ/GCRafqpnomSjE7ibdKLNJaUv4JzurVQRiRWySjFNA8qSOr8BqYrEac0L2w+cs5KN5OeFmEeVWKok3cJDI/IllGhPOyKJq5oVjCyPsQgn2Ij6bX4iCtfRq9SXNqX2NUC/XR2l+SpRtZfm3yUCV0yS38tUHDuiW5orjCt5mDVKY2Wh4bDGXnpNP8YXihqrqlumicql7ybVRFPkgAmE6PmlckdBBnARU8cTecz6ylnvOIjyBw01AOzqjV6lVg32S7+w3/4DytGr8OHD9vxGr+q0Uv1/d908//43+zyawEV5J0a6Suid/hv3LhhFX3iiSessjZgrJx3ehbIsufSszMpiDmLoXpFhKjEQXN+WhnVV+QKFJ7i2srIkY1K6GevyaKqHTAayGR+EQ2kyiGtJikXIilFNWRKQhStlhKlxHyYvwRw++ods9H58nlOnGgujXAmzThU8uPNYhfGQLSqEOOkEMpLFNJKSYTIGC5wkhUqSLMNOSJBgYim7ZEVEs6EDiQWEpLh6HWVMhlciv46FC9HjpdlH0T19QizpilXtdX1jXe1/SUnpNCz+k333s+f26Uzvd5//307S0fbA7VtVKD4Ap/P+nLq7rPjhG9U5YwghHPT2jJD4hcnLmmFingbK1CYyFN459whYdGZKyZomBJDIYZErBCKU3GREC/8dfgVpUIaplAf1gobryWm0TG32hKueJpjUsbDJKQhKXx0UsB0hoi+9Fik8FImEdMUFcMWzZNqIIG8QhwvFnLG4FkLFy8QzEvEvSoFcokRJmSw1Gzeba8XoTVCL2GHj3bVM512gmkHmTnRB84ZEyB8PLuybPkHfVd3vx0neuJpkL9f79LpNEZGRowXTE1N2dlQfX19Ru8VrnxEh7QrS0xdu6s0ru4qHCCCSZEjD7AzkExAdc9S2sUlFJeyhzF0RjCmLSNHIU9hQAK94RyDNJdMIA0jR6ZeoEBtWRue0pt1YKk2P0qFPPOjsspwe82CZaq+WqkXHmr3loR3E+BVH2EyK1xkvspLTngqPSSRpACWZx0i5F0MKTF+iHMsWlli/SiYlNpZFwpjUfIicpUy+Zt2RlX5HK2k2D9FFCpxFEqsj1ahtTrtamz9aMY15qny1H4Fldg/Nnf8WGlO2rwRzVffOt6qsVO4rhoH8RDdT05OmuFLr8pLcdd5St7YoHA/vpY3r/ZanFZJq1k61pnzW2ddpWQUoDAWZXgsT16nt21KEhCLyLNb5iiVpEhEdExWskDezDApdcyWCowUY7WPuamubGMknEQuH8gL1m4mJL2TwsDWWf/oQGKNs8wblRL7VzKE8ENIQPlEfVHmGJdZN+ZgK/dVxqmQWJYKbBeJr+EE4xfJx7WKT9RQpxrN1MsF5WIeS+UEm6IxIr3UgpwKYZ8zMdtE2ktU03iaIG54F0OOsm4sN8F6sAcky0gdZVsLLJvVoryQMcOSXqELRUnreVV9tYM8RFzRq62UJE2mkZFOddNYq/5qiyufTjjJ/IR/ElB1FU8p8kc7GTQCcUriVm9GlLImIVaGlLxWq1WX8gKftPuEfay+ZZ+UY+x/yjxRU6DZdxxze01Q4yG5irjBSrEs3nPyaO4wK8M3zTsvHyqenMc9h0PCSTe3tCtG93ol7oc//KGlEw729/c7QxLjOplxlR55p7D1fiA/C1eJfJTctYNSiotmOytFfNU4sYWU/3QcisZN3SG8UL1lsJW8GM+zPPZdhfgmYVoYpq5WanFR25XMfznbbardgDZ+UvBJi8hjxQ9LDBM/DMfYz6Qxec5HDVeYZYV1TAXbHGWfSEFTHYT3GqU851COcU0ukMFBibQDnC5iY066IIZsOEB5VP2n6jFtTDjFdpaJUwWWHymnmca97VCgliQjRJj4rN2MGrsin7UroMCxEE1RfWXAV587A0XQx/TT1T1r/OTkx36jU9ilS5dw8uRJWwDR+bIHDx5cGW8/Pp9btyJ3qC3W7XScXbqSvkgR124m8QXhQy5DvqJxZp+HRbeIjzI0izyI+hc1Lyjf2aH2pD02rszLcIpjI41GxkztcBaP08JHTDigeDJ6RjRXOR6kpTLGpojIOabVLscodSbjmcxaZDJLJCZ1Jq5qF5bqFGWdiKOWlaM1kh/zHE/Vy8xtxB3bhaWxY52F2wXSwiTTxUQnGU+GPbVHaCrDVon4LMwvisYJdwwlVR5pJx2phPEdUQrpZww0uhElfWLvsL6sEF2YE9WMBswzTvzUa4naSZwhzV7m3FiOJpFhuq7iPcRDKZbfzJy1K5TtZ7tVciaRYN+p4uxE4na1JIsIZwnpukhqWfcMMiNdmbOawRQFEErMs63UCcnfKjpXifzbdFMNTylu/Wbzn3WSv9ojHGd1DNRu1ylqG/HFzxs59r9d5TQveDV+zevn0dXO6/vNcflpB9/58+dx8+ZN6yd9oU+0XaA41ndB3E925K2FJUQ5XzLUjQpI2DhEq0scipTpRvEEcZP6f5y4ELfXYkGcySND+UNvbsVypLeUFUV/tRNSfDIX5RwkvkRJbw0nSVc1hmXq6cXqHGJh4rh4IPGHraI+L1mxirj0JeKnjqJQXpKLKGbafGMCw197xZF5aUe/ZDExnmLRGXhF0iXLaOeidCQt5sXZVyHOsYLmXZy0QsyHbSDK8n6J/COLcIZ6W0b0O8J5zZRCtcgE27DMeJRT8g1u/tnRBE4Ps+MNeBWpUT+WZT9g2TJ4SfaR0Uu8IM/yJfPKeE4Fz5XPumi2Cr9LpPnij2yUcqUfe0SdTKd0/tld3b3xBrVB9+rBGtyQPCDbxTvvvGMGUZ31poVXvS1Ya+gSL6qF2ud//7//73ZVVX+tRi/HAJ0TqNICVVxnuOi1Fp0HIkudVvZl9ZNTxb1T2tp7WRbXx5HA6MIdEbR4HM6F+XnML81jdm4Oi4sp5EX8OVgNjSJAjEOhMkxGIwFSAo7+TMBhGSbUKDeOlX3VgXXOMhaL4QQhIV9cxMxSCrPkIY0NjeC8MaKvV2AkXMq6WiYjEeHW9kVNrrJe/bJwMTLVNEziLGuaCmXfUInRF6xkYBACqQ5qV4wTQ8jNRrG+92n/OufDfX/6Z7VZxkUdYH/ixAn7iuOePXtsZ4Xi1PZ13X22nb0aqPEiWsQiJMjkyKGwzgEhPpGoV6MkRmTaS6k0ZmYWsDibxvJ8Dvl8DrE4hSXipb7SI4VYE187X3QV3RIxsxUpXu0cGRFgmy+BY0oxXoG2doc4h0IsXwRRfNviBnWzM+hIyOSnbapWfylTEqBkkKa/5pZeN9OOBLcjQ3VgHhT6LZ1WDJRO81L1Uh3ptIrgDQtuhVDhxHdzyt/F16qp77e6++25WvpT62rDJLyIgekdfX3BSwZ4HWQvZrYan+Mnemn5alwDeqZxF47ZVXgixBDyOB5TIjNeJP5ncnmkqFDpmqFSkaMAo0gJ0lK9csSsHAOmoCmBk9QYEeK08I2ZruCksjcvFWM/Wh0TLjv8UySj05wJEsitjnzW1fK09rA8Xi1HeqqeEnDUDptvzEf8TK8M2w5MptfXgCRIhKNSFlg/K8PNCZ1haeki7C/SdjbHXi+z+rEMlevB5pI5tcPVy+aVOdYtcO45CGe5bgzc1d+Lh+gMNo2ddmnXrrT5eLVOhTJrznPSKipfbizF0OJsQxK5HBkpxyicJp/OpJGiECdxsRgljWJ/kFMjwavSWV5sZzgisdPRIbVJP+LpRtPIiG1I2F+2Wm8jyGf+hatx/TKMfa94HKtIRK8yqJ5uzJSf0uusF9E6KaSisR73jK8zuhQyxdfCmPJWnmEtqDFdOZyk8KtdFFLAqvbKlj7WsLi4hHBjJ+vKsZIiSoVNAqKMXoJoOIcS+2I2VUI6z7yYRzLBsVVeqjPLl8yi1khG0RxS66QemnDIiqnFArVBuO3mkGuX0kse0YDYzgn1hdorL8VjuJRNpa3K6KXy+KeZ4ZRS4T3rKdxT/uoI5cX5YF/FItIlrN+Zr8XVYDEv1l34bgpg0IfCN2UhMLmLhXrjiYxXtTjkcVDzx9+r7dopJPlR53lt3brVaIeNEZ3y8fef5KQgl3JpLM1rfNJI5wpYJp1YzuSQ4XN+nniZzWMunyIuuP7RmHI0rC/Vt5yBHHs2VPNPnaey2QdWZ3tUXPaHyuO9QPPT+iFok9I4X81RjaPrC61MCxdF/5RHWCvaik9Q+TZGSsqCLL76VX3NrKx9IjAyrFFhmOOcTS0to0ycjrLf4gyKsf0C7eJWRu58XOIl66bzjTSGMbaQpVleom8y8Buds3rp3tEkgcZ5lZa4cH9fOyZqtxTbc+fOmTKjBfBDhw5ZHN8nn2/n26q2+PbIT+OusVE7tdODMhT/1Gb1Y5hKbZEKcj5LXUMLAdQBItQfxAcMd/ivntYYF3M5Dq0UYM4Hplfmjr4rP+GCGzNGNiNTNp3Fwlwao8OzCLe0Gq7qYwgxKTuas6RDESrPBY0Tk8WJRNJrVGhJO2R5FxVvUl1EE+lUb018GzOmc3xNbXT9INzVs9cBlYlmj9IIj/SKtPF2xlOI6moFmaHI8Uh79VO0ik6vsGvuKar4r0wQTqeSrarIPqReR3waGZnE0Og4ltlH4aQWO6poDS0js5zC+JTkYy1OkbfEo8hlsxienUeGdDrOuiQ4DiyGdeDcYMY2xyjLalFgcTGHmek80hmgo1NzMm/t1hjIIOaMXGwL+YI98zbEOqrCDv/dHLa+sjYLOE7BuPk+Mx5PZ/yGz0Y7FK5+lv8X0Pl5L/uAdvToqAsthuoopLVy4f3Tr3XsU+3K4r2slrqKrknjZ4citZDCwvwSZuaWMbdAuYPyR7GctdfNY7FG8tIq6SPzIZ6ll7OYnloSRUakKW60OeJOiBeKMq6yJN8i/zeaWHHlVjm/ZeASDsUok2YW5snbs7aYIR4X4+RiMgYzE9ZLi5jCM/k5msH5pfozhuEGcTIke4E2L+iP+CVPfchGBlv+27yQwTsazbK9rG9IBqGkmLZQ0uTEaCiDsfER3Lo5jfk5aoPJBsS0IYzJV/BOTzb/REPEy8Nm4F5McQ5xvmiea3ySpBcqx47+UFs4PiyQORnGsx7Mi3XXk9II9Ern6jitH083B2z8gns/5gLJn3rTQLKnPnIgg6gWXX24wOhkDdQ+/8aMXgLfQBWoe1VK97Li3rp1y97DfPbZ5yjUJa2BPq6voC5CAOssdR+fvRNhtEOLA/9wKU0kXEC1uExEnsJ773+ID4+fw5lz13Dz3him5lIUItnZDRsQbRDSukkgpVyHdsZJyKP2WmOeYXHm6ohSREYECtgZCuylEIX2iTncOH4W756+jBtzOXT19KGhWUyeSFYmM9DKKttS1RkgIQrTZRJAIpt98UECuOpPzCuXiAxVEmPmrTMYWDM2gi1VPixXVlkOOwVq9RmDNZ7Wdj24q7/3sD6sNo4YjvpfX9zSeSwSwPV6qVbXPLL4uILa+zp8tkAM1FbZK3nS3EbiTII+WjkQY9XqVAq52UmceP9dnCBxOHHhOi7fHcYUBXgkW9HY1onGSI54JgOAFBkhHueRrZppzhJv+KtXOJzRS17mwzK1m0FzjvEMRWwGcs5Q0WMcpRaxlKBEH97ZVkbDX4XKgm/lkdBpd4BWM5zRS+ESMKQUO2VPVbHqcA64woTP/JWTl0CCkQSeoD4mHCh/i69LcK3DbxVq6Y9360EretPT03ZGlOjRAw88gM2bN5sw4MGlE4bpKiQxRFlxhotU2kyoJO2VESGfJUMfHsbp0+dw/eZtXLtGd+MO7ty7h+m5eROKO9paESfjVXzLX3WUREFcFC6L9qtoOUeziWfM3x8WX6GQofUK8TWrHSPqznZ5ienLn0601c5FCGisrXIpP2bq0kgA4RzhvPKHlYvnaceI200Wd0JDaYFyDpVVzpdMtcmEJn2gQl9o05fmYiqL+Ur5laFG+oWKUmHic1IOrI0Kt1IVFLRbnrqqYubs0fkHUHsvHqJzFbRrWMKGDA56xczz91pw+WtninqV91W9zpVAVucEhRJIZAaxOHwJt65dxdlLN3Hh+g3cGx7D8hKVvkQnQsSFBgquSSnhNlYyv7j22Uoo+8gOxZfhyfpUbRNNoBOIdlBZo4hDXk6eL/ogKdZokzMYaZeNrTbqwepLOken/nRjL6cxdXRFF/WzXlMQrTHFxkJIG7VjiOOXiZAuMy99DCTM8R+6ewdvvPoahczbiPdtpYDZgGSEUoataorySYFkuekJjNy+gXO3pzC2mKeCF0dzk15NIM0vpFhGyV5l1U5x5a/yRT911pKosMJ0iLnqp8o7GUa3ajOd8NgQg7EVibhqU0rttHi8KpwKckhCLD10llSVsox2+pYYScnimGL4siYxZS7tZUogxby0SSKm3U7sf5uTRv+1aytuq+T2pSjVW+OgK//07Ixk9rSCRx6X/L09s27+XvTjpz/9qQneMpbIYK57D5p/lmYd1PopTiazgKHhmzh7+hRuXrmBwduDGLo9xOs93Lx9B5dv38Lle7exVMxQfoyjgTgZZ/+bGs42SUbTGWBiepIDDa/YTI5MUOcs28/+ZP8xBsM072XgY5yoeB7pSVl8mO3SWFifCzf06hfLsGHTmKnuiiAMZ2xThvUofNU4M73GTpNDvja+jGMr+LNYnh/BsaOXcPbUDSwWooi3tKOxIcS2LDA/zjedNcey7TByzlOqNKZM6XXJmFWiaCNqu2Gsjg6/VAwDrUz9a4ykyDg/gTwtkoIM/Bjq9Xa9+SGjsM5k0ziaITcI/1yDb7a1w1GIFZCcozkShJW1I8+MopqXWdLYSQySXw0NTpBPJRFqbuJYcmw4TtEKFc5S3gxYN4mjM4s5kr84+WYVCY61aK3w2nZ8ETfdB1AyqOYXMTk6iqNvHMdPfvgyWrftQXNHE5qp82i3n9WTTos5y5yDwiLOfJapsWctmZfGOyyk57PenhG/Mv1BaS2NBljxhc1CE5ZPRBdP80Yw+dtiqFKzvU52c/RMgdYn/Ncri2ZAoFN7lK3wX8+WiT3zwvxF+/xuKp3dlJmawJvvfYATl65ikbjc0r+ZvAromDmLC2+/gl9cmMXdhTLxP47OZAXD9+7grbM3MTk9j5aGGJrprx2fOq/RvaY9R96ewfjEIM5dOEHZ4hImRirYunUAyUbK4eotvYZG3ubOYFYj2VekiXavxQ+203ROtllhmtMWxHub19Yo59wf74Km1oYo/ucVauf0/ea4njXW+nqj5EIZgbU5Q28l6X59/E8G5i/eXnQGFuFxpDJP33HOi2Wcu3kDbx87gQsnbuDy2Ru4c+MeluaX0dTQjmJXG+WsEBpLs9Sl7uHciSt44/U7yHF8W7eT9nNcJJPIAFzVDkPir+kwrJ7OVw6ViDdlN3v00RB722zmHCZGr+PSrWlML5C2k7c3NGqhUPoO5QSjB5QlJKdUyW/1yjzzckYg8gmdO6Yrca0stiE7hewLZtDT8fUpll0i/aZ/vmznMerjZGHGM/7K+qJCvY80pEreffrkCRx9/xrG5qrYuKkfPd1JkhjiaMB3dLVjCzge2qhQKpUwNDqCU2fO4O7gPVUAXV2dJkdrNzAxXV6kC9rNTVnAkQnDd+NpDtmDZ9EO8yC4qxtZP77BlReV73FFvEHyp95Wa2xstIUuvR3ytzF6rcb+NYERqXXgKy7nBRs3GGsrKFjvtfqofFed4pmjcJVLTWPw5gWcOvE+Tp0+iQsXr+Dq9bu4dOUmjp86ywE+ifOXB7GUiTK2CDQTsp46sDtaLdAnS2TVJ9SlsEhZ4VXvgyuMTN/80zlM3B3BhbOXcJFC+nK6gAJJXom/iiuia+2h8Fni4LOBVnkJPVUzGKizOXk1MXQwi1aG1RdEGfWFFguNdXDC6c+D77ePg08K82Ohq0cg3/8+3f3Gqw6fTRB+6Nw4ORloyyKQ9K3KuFrOY2F8GFfPENc/fB/XL57D1ZvXcPHWTZy5egOnL97F8CSFpvwyhYMsU0mM9SBccEzHGDJRQuhhzkVwD4bTdIogwqjSgwjy8kKw/kxiNwVUOO2EH4sT4LcJzQo14iqCzivj69mVHYRbGuXqnMn1BkHBBHenUMKqdx0+w+BpUq3zsHIvhFpHD1eBcUyRJx7btYJcNoOhe3fx1ltv4cSHJ3Dp4mUqV9dw9doN3L03iPnFJWfkkBNnJpgCKcZMRHMHmjMrZh3omgG660FliIYadju8tAiKI4XFJailrStpdaN752t0391KGCmYIiAfh/NSAqKm6NjXqcg7SqkFLE1NYnRiBrPagRKKo0inDHXuioQU2+3DskTftVq3ImSzPPn7sh346/1gtf7roXaMBPcbs1o/pxpJoGPrKIRRNTMjiQz1leUJTN85g3On38e7J47j5LkLuHz5Kk5/eAYnTpzHtZsjmKMgqnNZdHC9aInoiOOXVEokIJpqJiGL/SiFTIKbOSlIMnTJuMn+lPHLuoJ1M8MXnfJiO9VU9Y+9XsKr/zOFS7QpGGil8mMuxxC2zOGL9ZbqYH5Sc3invCihzk3P4PKFi7h04QJml5aQ1atwwmnjwxprRtbg5zNYnp/F2MQExqdmsJjSAecMUgWDtilvyS5m9GJ6wzkzqrDNhkByjm46XHK4rj9XSYHDEWUrP6G8Cam+YfKWFK+rRpCKY0mv9DCOtYsKYDHF+k2NY2psHLMzcygwnVov04heEdWqtTN6sY/ZQDOEsCxlr/r4VxpUBfWT/Fx/rFRyDdTilMDHc+O36n5V0Gt6cwuzuHXnFm5eu4Yr587j+NH38OE771G5PY2z1y7j1JWLuDM0iJmFeeSD3aKaX2650pn35Ay3Aj7H2ji8kTLj8c3iBHW1ealUblwNhAgME07JgKW3DxRLztofNM+NZ+CnsjiAMjPJMdDlz/ETruitg2o1hUxmGjeu38Sp4xdx9844nzWflCevYS2gMU8riOOu8zwqVBY5T7X7x7WB42j8nFEsX4eLApYYtE5tc3hjEVecwLX7l4HNGbXrCwXr2632qffogvZam4Uv9FtcnKXifwnH3n8P98iz0px4ep1Qs0+7ZbULc2lhASdPncHlG3ewkKJMR9qjnfjax+/yZmwOqHw0UnpdfnFuCueptL704stUYKeDV1QZ0RwLEB+lYqm6KAcVaZjGZ42qYyVBW1Rf/nNUbd7aTmn6afw9DqydkwpzeTjjmdIR11WecE+FKS+l4d9K2Yy/kg8f9TqtcvTOGc4Uh7qcLPzFHErZNOYX5rCYTiFLwlaKygDAyIsTGL16GifOnMMZ6oYTswuw19Hn5zA0MoGh4QmkMmniNvtBRj19sa8i/GcvhktYJs27N3iZuuVpXL96x15vdPUULXN0Urqj5oMp4SzTRpmNs76x2HwWwSWoTeoLV3/nVhpmD18cWMWDtbAytgGob/x8kPsfAung5Ps6j0tGmWoxjdTcPdy7dQbvnyZ9v3AWN67dwp3r93D1/HWcOnYWp4+fx82xKSxrKlRzyKQmcff2LZw+eZ1zcRZ5+knf1wFZoagWhswCZc5e1bcHyRxO7rBzq+gyS6NYnB/C5NQUpqcXkUqR5jK+vu5sBim7cu6Qo/jz8mTccht/xCdIx1mycChiCyjMn1fhm+Z8mPpcIbOI2YlpjJBmLKSLyNsH/ISPSk/6wKqEqgUUKCOntPN8OU1ZhHgZ03EJ63iv7uWnCcs6qB46kmRsbBQjI8OUy+bYP3pDQh+V4EQI4loWgdO9ukQ7JHX1Y61Xv5mp/QkUfQVq0gvW1KkGPG78bXHEc6nfGNQisL+Xc50g37WI76IGHUJvT9jk5xRnKgj0s/HgfV7bU2/fxRuvvokfvX4Cs/kINvYP4MDOrdjSlUBl8R5unX8Hb1EJukbETeW1+kgE0vvphWVUSCSXslEyjxCJXhklO9FeZ6hkkaWykc5SUM2lUcznUcqXkcuUkDahQcgpoxcRUu/wZklkl5ewsJjCcjprZ3NJ7BPS6LPSIUmWeg+cFDjPv7nMHJZyOaQKFRRYps5TKlHwTc9nUUyXkMsLcVmPoC9qwffnpwXX16t97O9r/WrBx6+7z5aTaqxTFCp6RTegh2EsE/+mMD8zggvnbuCVN05gaqGC9u6t2L1rM7ZvaUEymsfU8DgmR2aQzpWQIR7rLI3MMgkwcXaJ+JrhvCiRQdhqruYohaIKhQKtLJbzWYuzQEK5nCX2lp1gVCkViPPzWF7K2pzQ++dG+xkqBbXEcHNFhhUKjMM8FpaQyeprViThmmpidEF8fTlMr2Iup1L2Gq4IbYHzwA60Z9wVpyJqgKHBHXFXjj/uev9+rLvfnPs4qA3zPMDDx90Hoxi4tSABwPkyvoR2XnXAtRizFNa5uTnEYgm0tbWba2pqRky7QYjfKkPG1QLxMkOc1Ktn81RqhW86e8ad16W6uOx1+LRem9RuLsXJ5rLG8JWPzjZQGp3XoVc1hbs54rAOeNZqb5Z1WlpatgObtTVcZbpsVUCOaTPIpXNILxPvlymEp1iGXvujzKazRMrpecwP38L1s6dx/MQFXL45iMklxi9L4eYspCBT0Ssx5E+ZNAUalqPt+jnWUfNOdfR9ujJPXAVWoHZsPmEIV0D5fdJYC6yPNUrqb0U1wU6rghTAONcrpD1TQ/dMcbsyvohMOIn2ZIR+N/D+Ky/g2Gtv4RqVkxnSFb1yI+U7T/6oM6Gy2SLpFmlWhrSpJNpBnk4FP5cnfUotYmlxkX2ZsYON3S4tVUicVLyf+Yme2SuHi/YlUX/upaszY1E+0PgVCs7pS7iplF6DyBiNo/RhfS/Djcm14vXs7yzHX68ALOvsT52BQbwRHdW5GMqjSKVtmfiWJh3N8VpiuJDY08yGpFaAGxFvaESUwqg2DrpuluJKus0085QvlpheeGRGWl5LbE+a9RN91dkbjqaKvrqxl1N84YV2VjocpgBflJGK4cxGypnqI6d7yVVpKtTpVAGZHNvHOormVyVcj97FtYvncOr4CfKcK5iaYd45VkXjqgUMw0nKQBn2xVKK5eU4ZhwrKbn8U/7OeOPq6Pv+/uD9dfXOwf1ojp5rF/ZqnQffJ9qBEk8m0NTciPaWFsQjUUyMjGDs7iAVnjRirU1ItrUg1qAveZPvMo3OBMylyDsXl5Fl27LkWQX2oc4vUZ4qxeJl1Y/OCJgWPyONSZPnCi/0GlqOuJxKiccRj6mk5PLqA9WN80TjQBwSPi3RLbAu8xnSB529xnZI9bddnVQ4yrkMQqQ3VV4dP2d/kyblGK5DuonyrFCE48rxyC8gVyRtKDhctl2VlEmFhoaDZqzUe3USVPPEEc6lBc6pReFBjrSO84SVVDtl+BLyWr+a08WrE+oFhclP9wI9a1zWKVgE/6zr+vvPo6sFPcqn1hmw+3QvvNK9vd7LG9Ht0dFhXLhw3nbDzZHO5RgmfkUmhBLDZ6ancfrceQxPTdtoaQdylXpMbmmBCu288YD5HOUtDqrNOOkWVHaznP9LxI8C8aigMQ+ZqRRV4nSBYanFBYZnSaOKyDKC0ReLoB0mjEN8KwjfGT9rvIZ0iPkXhBOMJh6ZEx3i3Fgmbc0USGPIm81IqrnPdujg+hLrtkQ6Oc/yUpxLeZ2ZKFamovinPjSFmjRL5575BQnJgQL1qXhxUfjPq8680n1hdgaZhTlEko3oHthCPXAjmhu1z4fpiORh5pkjrcyyr3QepM5HjCUa0Uaa25RI2oeX9DqXULvENqZZx1Sa85xzS/KrvsCXJy3Mc64qS51R6XgP5VbOqeX0EnmKo6+sljNcuInl5gw9JXcvUrbVGDneI3odtCto2xoUqvFcj2efF/dxoD4R+Dh6Fi9YDz6eh/X5r3fqNBnydZ6kfU6HNC81PYMbZ27j/ZeP48yFCUQSG7FlZx/27e9B38Yocf8ePnjvJbxx9ALGJslHZdRkcp3FVigKRx3OLOXSWKRskU6RvhakK7l42qVZKGiRLsVxJu0m75PcJxlMX85NRBrQ1NCGZLKVvJ36m0094iPzXUrNM26K9JhynTbTUG7JkidIVjHckl2Acs0y57eLJ/tCGIaGFR2LMI3p4Zs488GHOPrW+7h7d5rzmPIC8T1LOl4IzmMukT/MjE4QuWOcG1uwaccWNLQ3mizDTmbfsauE55zjOj9TMuUi6Ynko3jCydL6YrLbVS2cdnRJV+FyWjREc4ZOz16W1ui5cVE/aUxWwYXWgp4dDaiFteOr6q5P9+lBa3q/9tcbPaiCEnTM8k3wB9l3dnTi2eeeQ5yCnU3qGrBOkPVfyC9lxsJXO9g6hfnqvkilfHbwLk6/8QZ+8rNX8f5iJ5785h/i6089gmcObcPOzhIacrexMHkH7040IR9KYMvWHrTEioimJ1CdH0F6aREX5jtwb4rKyXweDdEIGhNElswM7ty7jqszdzAxN47I0Dymbk5jeIl12bgVDz38CFrb9NpBHpE5Eu+RYdy+O4wrY2Q6FMYrZGbheBSNUX1Zi0J0qsyJV6GwlMVE9Qau3LrMyQUKyWJ6+oLVPBZmp3D9zCyyiwXMaZIlQKIcQ/Q+46tBvx9i1ILiyKn/JezqfVhdd+3aZa83Kr6ITG063f+PIFQdfnMgYVf7vKp6PUivyXKKRHAbS7NnbTfBq28N4oNzQzj45LfwyBNfxmOP9WPvngb0SHgvd6OrpRUtfa2YoxIyNjiKkTt3MTw8guHJORNyGppFkGOkTCT0ZODppXkUMinMzUziOnH73sioGb/CFBaisQhSc/S/cgE3RykUZ8q23bUpGYW+AFXKLWF+bobKHhkAFb7ZuUXcGxy3OZJK5zl32qjUsQ0kDVpJKxapiC7OY2ZujjTiNu7cuUcBYpm4GCGRpUDC8tx5Xo5wkpyyRwIaIdDFFNwAlwO6UYffLqynQQL51frr9SQdYK8vN8rwoNcbBwYGbBu7B6YQAbN7t9YcDHEwrnqd3F5vNOsvQ8hnFij0nj11Br949U08eORRHH7ocezcvQebt25B/+bNdvBlW6u+ehOmYJHB7PQUBgeHcOfuXQxR2c3kimhodAdj2mILc5YxY5H5phemkaKwenNwzFbJHE+rsh2TFA5ymGZe9+7dtTOvUhR6ZfCSkW1waAjXrt+wQ+BlaNDXVXWOggT5cGGEwhbrcCdFQWUOd0cnMTQzi3Qxh872FpSLk8jdPo2bH7yBN985gzcupTHKuVtpbUe4rRGd4Sway1S8OUfHZxYweG/YXg0Ym2BZnHM6o8zOOiKXV3skyFAUtH7000SgltorUQHUDqEfO/EEGRL96406QFTjJiGodmx9fDl7DUZKLqmWXrOxV571TGEuOnyeQuhxvHojhVvxHXjw0Sfwe/vbsTx2Fx8cfQ/TbEO4rQPNm7ehuY2CVmEe45Pk18shDA2NsZ+nSFs4Xg2NSDZQScuxDwdvkWff5DiMYmpCAmeV9WRaHWYRzlAYJZ2iUqJXYK9fv8ZxHzWjhYiKPtkdJ43RzjoZJOY5DqbYLeUxzrKGSPtm5xcQpXLU2Jwk9dFxBGwwBbvMwgym7un1uNs4P6WFsgw6iB5NdDOT03Z+kYx1HQePYI74nh4bQoY4VSQJC1EQ1tgkilMIUdKeD3ch1rEJPT1daG2MIJ9aQmlmBFkKrLfH53FzaByTU7PsX6ClMck0C5geGcL1wUmMz6ZNyIzFSTMpxwjPtQtCq7tTE+N2tMStW3cwNc22UdEMhXWGSdRouT7uoBXg+ZlpVCnYT46OEHfnMTlHxYwYk2xLQGdaRSY+xPmTR/He0ZM4eeIWbo/msNywE/GGJnS1Sn6ippenwD8zhuF7g7h2Ywmjk7NYTM+znCj7Ocl8tFKt3XjkX7xK1nO7HgI8IoIKJ90N57phrGGtgXZc6Stfwm29FudfjV4vy9wPvEwkZ0fBR1jnxgbs6NqMtqZ23LxyE5VMCQP792Dnl5/Epp3bsXPXDgz0bLDX/xanpjF6i3Ps5l1Mj1HZCFPoJ92Kh6kYUJEJh6Lsb9KFiQU+zBoPvHVzBEP3xsnf0hS4I5z/CQyP38Ct27cwOiolWKtXISSbdE5SBRHy3rmhe8TnIY73KO6MT2NkMYUC824iL9dOMxm58guzyM3PopqlojE9gWvEv+HJKczmStRrkmhIxpAsURalon7rFuUEKleJ7jZUGhKsF3ktaZ4OYS7Feg0HEqEM+XEGpVAOCzkqiTcuYfjGHEaHpjC9sMjeqiApo6y9hq7x0q91qn6CIaqVH1fHYsVLdIZjKoOOzvgVL7jf641yq/l8vkA71l1nsK1qrzkLYrtEAzXx1TcRTgPOBc5ZM3pFJCeN2668a9fuopgPoW3ffiqmLWguLyO6PIMl4t/VO6N4+f0T6DtwGNsY3pyfR2aEuET+c5s4M0J9ZFDGzHgMLdEMGhm+PDGN69cmMDyVxqPf/UNs6O9CR5Q0TAr3xAQmyLfuDA7i0gxpEBXuCHWSJlYtSQVdZ8Kl5ucwqx1U5IFzswuYJO5LVov2kBeRz1TE00dIlym3yWg8Pj6Oidwiki3kt8QX7UiGFvIXljA1NoqLd0kvx4bJ/0vkT3Ekk3HyRo25aIEOuC+aAWme9FILnzqvNcZyRCvVl4usy9zsNHGGc5jx56bGsHT1Mq6eP4vzyrNrEwbI93u7WxGvltExdxkzlDeu5LuQ6NmE/Tu3YXt/L1KcK4VMBe3kMX2bemx+iaYvk8fduHEFQ6NnOCbTmJufJ4+XUbEJrcmDeOSRnWjsmCUNp9yaSmOc9PXu3VuUce9hYXGJ9GAD2xEmrSvZ4oWMdsvLKdJU0sRrlAemp5EjvdcuWOufwNhmPwGuCIQl3qPG+3MJ6+fzCh0WbgTPoguSC9Uner1Rr7H51xs/LV1QaDFcRTlCbalE+rg4gTtnL+Gtn3+IE+8PYmnD83jy+e/i+ad78NADrdi0gfQ0P4bLl47hpast6NqwB/tbcmgspTA8soA7w0to29iO1h1xjHKcp++Rh8+xLtTakw1ux305NImZqWFUSIszi5STRsdJuyc49jH0xYrQmaLL1X7EmwfQ3d2O9nZyn8oiRsao69y9ifGRRcoKGTt3L0X9X4ugLR0y+GaJd2MYGqZsQ33t3p0pjI8uIp9sRYhzJl4ewvLISVz88Bje/MUpvHf8NkLtWxBv6gSayQeS+iBDFvHZKcxwflw8cxmj4ykU2wbQsnUbOnsa0ZrQoU/quAr5P2mMDOecd5LB9OEiyUdCYh1gn0gm0dnVie6ubtIGpuLckkF9mHh9i3Tp9iBpCfmVFgubW5qNV0hvs3GzkdGvv1qh9ns/qB3nj3u9UffeviRQObVQ+/wbP8je36viOoxM97Vnej3/3PPWgV7YWeOUlhWzK38sN13pTCHhQ6FUsFWR4RvXcfHEh7g3PoX+x7+Nf/Ev/gke2NaHDWTuG7sbsa2/E61dfXjtWhYTHMSHH9iOBuSRHrqFqWuXcPXyNfwfb57HK6/8AmOcbE0JCtHRKu7cuoD//td/hT974Ye4cPECKrenMX6bA0oZObZlK/bt24O2Lq2mZzF/+Tre/cVr+IufvIAfvf4Obt+57Q56Y/u0eq3DUofujuPi+TsUdG7iwuD7eOGFF3D0zYsYGZom68tRoFrCxQsX8f/9f//YvmozPDtKISiBDUSwJgp36he1/SN9FTjrIl7XEwQ9K503emkHjb54VHuml7+uz7PuPntOr7bo6zjxorYBkBjkhnD7xlkc++ACFYxFdPduwr/5v/7fcODAAIlCA/o2dGDb1l3Yu/MINvZ1keiGcI7z8IUf/wQ//dFP8Orrb+DY8ZN2OHV3V5cpiflsCmMy4lIov3v3jn0A4cc/exFHj75jwozoVKmQw4Wzp/Anf/qn+OkvjlEoWEB7ayPxtZWCcxXTVFA13+/evUdFeRQnT53Fy6+8jtffeMsUyJ6eXjRTaWtIyEhWpkIwgytkeEff+wD//S//Ci++8IoZvrS619DYwrnUZAKiDqtmFwROCpG6QX567Ulbf4OwOj7/nThPf3RfC7V0yRu9dGCpP9PLG70Uz/IymqSBdPm6AbXkvOgVIwUpTy2n8krFYZGK3OVLl/HBidP4wR/8Eb7ytW9i/8H92Lx1E3p6e9DY1IAE8UdfzhsevEt8ftuU55/85Cd46+2jGJuYQpw0O9nAeImkrVyPjw7j3JlTOHvyOC5evIiXXjtKwXbIVruXlhZx5uxp3COOnzsn/H4J73CO6OuGUsglzL388iv4k//6JzhBmi5jWEdHJzYQ99Wk+bEruHrlCn76k3fx1z96ES/+4iV8cOoYhexJ7KZQHiqnMXjmGE69exTvnLqO926Rj8xMokRFu4tCx5bGMFqLGYwODuOVo8eMh+mA77Nnz9mKvgxTHR0dVhcpE647XX/aayZmeAh4ivrV+teNk8ZB9fe8QSCjlz4+oPPYlLcUVRm9auMIbLwIFXehjqvX+zlOhHIoZsMVnryOW+S/ZyfLqG48iG9+7Uv43rMH0N/WhovXh2wnWwPb2LZR5zY0Y2HwMk6SDl26eBtvvfWOLaCJl3V0tVNRCVu9fvSjH+HnP/853nj1KC6cuwp95W/Dhl7StTaUyhkqHYu4cP4ifv7Tn+Kv//pv8OIrb5jyEYpGKKCRxjTEqMTkMDU5iQ/eO4Yh9uvF81dJs96kewNXb94wA8nArj4kIuTJUo4oiF0mDrzwk7/CX/3V3+BH757EFPPcRIG0i320uLxkhqaFpWWMV6N47bXXcOzlF3CNypl2UHX0bkNbexOS6VEqblO4uywjRCtaZUwslXH76gXcvHDc2vfK0RP46cuvWT9o10bfhi5kpkfw4osv4L//jP7nLyOfz6J3Qycakgk7aLaYy+Au5RHh+k9/8lPKHS/hxKkzSGXzlMuizihIXNeOrCsXz9l5H/duX8fpU6dJ81/Fux+ctq9atfdtRGtHC5ZuHMX777yF9947jys3JqlgF3BxbJn0fAv2bIugKVbB7PgoTh37AD/96Uv44c/exTsfHKMScIfzO0Jhv81wR4Yuib12LhkVWfd6Rw0ISTS/6SmM9PRDFF+vTOhML3+unD/TS3GEix7HP855iEQrHPcY+jf2Y6BvBzpbOolXFxSCg089hie++3Xs3LGDciQVZSabHBnBh0ffw4s/+Rle+tkLePfddzGYWrBV7e7WBrQ2JVEuhij0p3D+3DmMT16zfvzpT36BV3/xFpW5QdKgJkTjCbzx9s/xZ3/+5zj69inKpXPEvQRpVBuvlBfHxvHuO+/gxy++gh+9+DJeefMtnLlwie0uYfPAZlM2JoepZFy7jEEZzkaGjDb9zU9fwFvE23uUcyOUYzd0daA9VkKG8+TKlduYmJrDdK6A66S7H77/Lk6/9ybGx8bQ0f8kxySJpmgBMSnx83M4ffkC8fmv8PJP3mI738M1yq05ytyiJ50dXRyFgE6zt+4rw69zGmOLZ3Q7RMX/ms1h7SLwRi/B+nSfR+ewVKirZ4fX8rYgGbyE0WYI03YPhjvURiii3UtUfBeWiEMLpgA3crwHNvehk4pzeWYMI3cHcfneOG4MjeGpL38Tm8g3Ry6fxLFXX8RLv3gVP3zxF3jzg+O4Mjxp8tKWZmBDvILF2SWcPXcXd0cXcOQb38HW7VRcqxlM3biKt99+y2jcn//3v8Evzl7FMPEvUcljQ0sj2ptbUMjm3Hhd5Jwnv/rwA5b3/ge4NzyEnq0DaO9sw+zoBI6+/jpeJn15nTTufSrh10fvYWPvRmzs2YCGaAz5xRRuX7mKl3/xC/zp3/w3vPraqxgZmaHi2kT60clrwnZw6YuPecqXOtT89MlT5DezRqdaW9ugr+kWCyVcvkzd7colpDMpzvsy9bgLOEadSrz8TfKPhSKQaO5AU1sPmhrC6Jmh7nnpEk7MNdmiwv7tm7G5rRnjExMYnZy3Q/Xb2htJ35NILSzi7Acn8Od/8X+QJ/+F6XPzHBMt3GZSDeho3YvHn9iBaNsc59Q45/pVvPrqm0ZfX2Xb79y+S7m2F4l4E9ukQ85l8FrCVfbhCy++hL/4878wHp1OZ9DUTB7d3sF4DUIY021trhhNNISxfyHPejz7vDsPuvcyhIxekgtlM/BGL28/8FCbx/0cf6BX7bWzWx9e0QLTiXeP4TXSYGoT+O7/+u/wla/swJ4B0siOZmza1If+/j7MTM3ir94cQydljsc3VdEayeHu4BwuXZ/GcimH8dwdvPTSSzj687fIl+9Q5Iyhu2cALc0xjIxfwckPT2D07hCuX72Jt9/9EK+9c8xk3Z0dYdv9N7akLzu3oL2jgXynjKmZUbz26kv4GXnZ22+cwIkPz1E+uYTblBf0CmF3b8I2Apw+cxK/+MUreOHnLzP+Ozh2jDy5Gkbvxs1oKo7h9vl3iH/vUL+nrnaOaTlHCpKfWmTMjaKR/DJ9+SpeYR6vvvk23j95DjemUlguJzg3GrGzvxlh6lnL5BMXqLPpKAY5nQH+GvXDpVQKXRs22M5MveVg87W7214ploHs7q3beOWll/HXP/45Xnj5dVvMkMF648Zek5e0yOVpv2ifxtrxDH/196u8uxb0LN6uBfIPPvjA5Ad92fMzY/TywolABdYKzn6nV0dnF5567kuIUTCU4d4OCzahWAqMVkF4S6ZQohKrEwvsnBOt9oeYV7VAaTqNaDWF4swIlZwLOH13GJn2bdj1tf8V+460o41VCIcWEWrMI9QWQyEWx8wZIu2Zc3j2sZ1obM5gbuI0bpyVkvEerqf2I9nYhR07S9i2iWVx8G8ev44P3z6PpYZeDPQfQnhsBndvXMaNYgW53Q/h0KMH8WTkAkaPv4UP3p/BnckwiWw7tvZK6QdGx0nswm1oH4gjG8li+O41XH+XCHHsbQr0G1HOtqJt8h5iIxcwPjWCM5kyhpcpdMxfxfTUZUxl2fZ4L9q6etDeo9U9HVMplHHd4xmlAfvYBtecdZ27Mo5WGNT/spLKeCHE0U4vfb1R/n511Ls6fHZBY67P5cYpLJXinC0crsjMHYydPYkPzk3hRPkItj/2VTz11e2IxkREGhmpjWkiaExOIEECqVXh2+dJlEbH0NWQxJbeTuaXQbmwiMFkLzp2bUN39hbSF1/CyWMn8fNzDRicCKOz/QbCJSrcS0XMjizizt0R3KFineEc3UBFPDw5jGxjJwobd0D8u3/kBIZPvoMXj43gxug8ZrKLyIZSyFJwnhwLsbwIBaJtaG2kULU0jBsX3qbw9TaOXppFOdaEHRSCyrkU7szkMZSlMNLejYN9ZBqZNML2RVR9WlvH+sfJ3sJIii4YDZEgGeBxHZ1/6/Bp6Mj6nV5SeGT08gfZW3q6PJ1e54nocO2yhBjY4aACHeIuyJCBZCN6NWgBxVkqgBSEz1/owMEnv4PuA2TMHQnbxZBkPk0UhRLVK5iZuIhjVA5PnzmPueVltHR1obtjM+IjHZi5toD5lg6ENnRQcJ1HeuRNvP7qX+GFY1nM5RKINUaweVsn+trLyI2ex/tvUNG8vhGl6BZsTF9D+/JNzM8VcH68FaMzReLrm1hYvIXULEtPtyIUp2K7oRst3c3Ij53C7ZuXKGQX0d7UjM0bG9DVrPNXRlFs/x7ysZ1oWrqKwvQFTC1msBzdiPYuCinb+nB4305sS+axPHwD7508jxfOjGFyqYCBtnnOimWklluwmGnHUqQVaQr/sdYomsJ5xMhrI6QHEZ3dQyiHS+QrnEE694od7MfPO62wSejUVYZx7fSS0UvChr7e6I1e4vs+jQepd+JZ4UqMtIPlcRzLsQyFn3nkpidxe3AEF2d6EOp+Fl966gj2dZIfhtN468R5zFOZ6SFt2rNzM/pbk8hePY9f/OiHGJ6OYyxdRdPARux6bB/6t/Si92oKF195G2eXbyPcm8Suvk72DXFjeQ7Xmx5CoWMDNi5dxuKl93Hy0j1cWm5Hx8BeHOyNIVLM4sZiG8otO9DbHkdn6SamB6/hpb8+iysXb2G5soh8RK+uzNhuArWu4/C3UaIi1Tr9AabO/ATHTr+JDydmkIluQk/ySTRFKAgPtAO9TZinsnPv9AVcpOxToQKmw9C7M0uIa1drqRk32g4j39aOAw0nOR/O4L3bISxU+rC5ow1bKpO4QVr916/8AiOLy1jMF1Di+JUpQC+T/uYWMnh7dtF2l0Uos8RnJ4lLBaQSB5Ds2IqBxjsoDl3B+yeu4cKtOYTjCWzZ0Y6WtjhmxylQz+fR2hVCxwYKyQtzuP3qWbzxV0dxCjHMEE9jxSVE5u9iaXkeqY37qeT1YWD6LsauDXEcOB8iDSh0dyKydRP2PrwHzzffQ9PwBZw7dQ+vnprAtdEZNPeGEI2T7i+Oo5iaBWL9iLftREMT0Mqx1i7APGm5djFXSL/LnKPCx0iB+EIGl6NgXdScJ37pmAgiGPRKkAycMub6j2D4XaLCVY+Lq+CFJV1XnTsbTl+yI5+MjaFcmsb5oyfRUmlG35GHEX5ov8U8lJshnx3HzN1BWwzKRpbQvDWERCeQPkd+NF1FecseFHv7kQzPIDn2Es6+9Sd44WQCM/NxtEC8d9BeHxudDmF4fgG3Fq5ikbjXkCoiOp9BngpUadMOtPd2ITVyBpdvnkexXEFPRzs2tpJ/58eQzE1iccPziHW3oWf4fZSO/wgfnLmAP53pxnCkBx25W8gtTWB2USbmdnR1dmAjeWaB3Xbq7CmcvXDGviCmV7p6EhH0p8cxff0yxrt/gFB7K7obphDLXMPNy9eoxAzj1vASEn0tqDazTydnkBhfsMPVh7ZtQaYpiY1FIM68JW/qdSJUS1SeMuwxjqP8eKdzbfTnZFE+S4ynv4wn0gfECx5//HEcPHhwRRb1sHYMP09AeujMF2o5GyK8dU66TAWUY4h7RXaGHTofZkciQ92miGSliGbOu/DCTQxfeQOTnV/CnkM7sLFxCdnZm7h17S5uXs2TjvTg6a9+A42UlYZu3MbIxDDKDRl0bM2hszODrpvb0DUbQ0sf52h/I0aXKzh7kvTk5nV84wdPYs/WLixTUf/gvRfx9ocXcHfpAHnSg9jUfAbZ0WO4vRzHdMdBdGzqQP/8CUwdfwk/fEsLk7OUx8rIatFl53Z8f1sCyaVJXH1vHNcuDGIxNIWGbcS+nlbEh9rQVqR8t7kLuZYYpkav4cqJ13Du6mUs9zyL1v4HsLGrE1s3a9dGL3mJjOHEtQrbR5l09u23cO+t13ErH8YYda4Q+eO26geoDL+Ll85UcOpmCTHO9w0tFYwOj+Ha1Cy69x7ATvKE1vIylpfLoOqNNvLzncVLtgv6xNxOxDoO4+D2DmzvGMLs8GW8cB6YSVXx8EAEXUwhnvz28fdx6doVtLdtR0O8D1MTS1TuhzFRrKL6wB7seHYPts+/hltv/ASvnJrFuUFKo+UI9rU0orywyHFKc6xjaOom34+VSG8HMUl8v3v+LJIHv0r63I/mjgFs2LgTXRt7EaGuKl04no1A35nKhDKkMxniB9uoaWBTwck+X0TQXBfdFl24c0cLJFH74JoOsve7eH28TwM6qVtnh8ZS2gl1De9cmcPPRrupn+zCv/jjQ+jrbKHs04I0OlEqtaKBNLNhaBnn3j2GPb1RbHmgB9nWGK4N3cTF029jeW4KI40DqEQ3oH/sMtrHzyNXTWOevKdnWz+6rx7Hhddfw6njC7g6VMV0KEl87cXGvXvwCPnwzOQNnJzNYjoWR1c7ZUji58iJc/jhG7PI5brR35xBc+UeZbgZXC33omFgO769mTLZEvHx9iym54C25gbsGMggGZvEPexFIUE5pmkZ4dwUZgZnsHgvhY5yMypPPIXevXvxWH8Je+NTWBqdxpvvLuHd00MIdW5CZ/8mdBC3EvM3KJNOYXnLAZQ4nzePvo+b7/4Eb7wxiONXk5iPJFHqu4ttj2xBS7iJOM35MlFgPfqxc6AfDdmbuPDOy/jJq5dwc1DHieTJrwpoZK9O37mF9lAHslv3I683jSIFNJeylAUpE0e0y1og+igqyXEVg6BvhXiv14bdeawWycZ8/U6vz5TRqxZU4Hqjl7b6d1LJeOa5L1Fo0ScvGc9a5x3BKsq04pCa7dYhWj2R0YuKLTtO5w8sz8/ZQcWD41No79+F9t3PY+vWBmxkfyUi+rTmMvu1gCoF/BPvTNqrJ0995QgamisYu3UOlz88hjtDWWx7+n/Bt7/zbTxypBeJUBG3LlzDtfNX0djchqf/pz/EM08/g+b5RcyNjWO8Gkd053586ZkD6J09jf/+l39JZf0WOro24ytf/zKeeOoRex3gtbdO2/vb3ZxAcQrg82NTuEbl5Pz5yzj8/Nfxpee/hF0djcxzGOc4yUdKFTxI5e8HTzyEZipAU5kIZpfzaGqK48CerXbehOsVR/p0XQMWuM6X3SZC4o1estxKyRQx8Uav+ykrdfgMgyRHEoBKlASDiFCZuYUb5z7AyesTmGs6hIc5rocPdiNBDmq2ZEqe+nxDlPNBcmmJeKZzcLYNbMNDFOwlbGo+3h68i0tTGezZdwibIykKw2fw5vvn8QEFi3379+P739mOBw/up1JVwbnTV+1rHgcefwjf+e53cJhEVFthR/PEpfYN2Nrbje7UbZw/ewavnRlBQ3sn9h7ahceeZHkHDlMZjeLShYvYuXMbNlBpmpu8jRMfvI7jp86hmOzDH//xH+Pbzz9tuxWuDU7hOp1eHdnRnUDnhh4nZLNpMoiQIhD1q0iILvBZB4qu4HIdpT+T8GmNXhpjgb5mpqGUodM+pc97HfQsJpmzs6Kos1YLyMxT8D53GW++N4O2vg0oJ9OYmp3A+NgMle4KWpNNVBamcIJ08CiV2zyFy8eefAp/8Ed/D088+gwiS0m8/vrrmIzm0djVhq7GElJjl/DyL16jstiD/fsP4PkvPY5HH3sAnc1xKhtX8NIrr2FwuQ9f/erX8P3H+ihMb8AE2c5b50bZzjy+/qU+KnWPoX/DESwvVTA1P4M4027dtgnR1B3ieAN27XgUDz/8NA49uA/t3Q0YHh/DlZE4GfsOHOxcRHt0EcvFBszHt2L/kQfwze98E7t3bEFycRzn3nsTR4+fQ76pH08++ST+6R88Y69jzc1HcPPeFKaoaDf3dGDTQCdayTPtPGodsiouQoJQtddD+WS7DuzWuQA8/xAf9683+p1e2mVTu9NrPR/R4edi3SpTu+sgA1tERrY8CmOjuHX9Gk4OVjGDLdixqReHmu7aSuNr75xHnvN4+7592HtgPxrjUQyfOY4f/eiH6Bw4jEcpOzzzlWew7+BuNEdiuPkKlaCXfobGg3148ivP4fmHHsNAayf7cRqvXl2wswq3lgZx/tibOHlthIr8Pvzg+9/D733lYUwTDz+4NkUFNIFNnWF0xxcxNjqBv/5vR6GDkw89dhCPPfUYtgxsQTGbZ9vnEOqhQkmaiZHT+OD1n+P8zTvo3fcQ/t4f/Z/w5We+id7ezejb2kKZoAHZeQqtZy7YawIDjz6N3//938dz+/egkX1/bXIJZ+fD6N2wBc90XLcdWe9eKyJVacf2TV3obylTiP4QL73xOnr7+/E8ldynnn6OgmUHxm8P4q2338YcZZ2nnn4aXz58GG2cP0PjcxhJRdHXP4D9TRO4fPoU3vjwMlLFKB599Ai+8pXHbKf3sXevY3RkDKFYFi3tCfvq08WjZ/Hyq68jsWcbnnn+eTxHfOxujGFsbgFDxbjtUjxCoTaUz2Axz/FNtqGHstBDX/0unn12P3akbuL6yQ9w9MR1TGXDeOixR/D93/8ODhzcxzGM49aNm1hMNaOpfSc625NojeqVV85iKgg2iU3Gk+P8DoyyspWK3gt/qA5bPBm9tENTO+m90Uu0Q7hXi4u/DHSWjpzO2AqHFrA8M4fjb55GjgpwMxX65MEdFNYj2KIvXxH/s7ky+6oD+9kvjz59xHaYnXmDbZ2YRZzzuYvKdk+ygNLwBbz84os4NZjAkSMP4etP7cGDB7ahVE3g5Ll7uHTrOp788iF8+ctfxqFNe5GezWBwini1YQM2DmxFa24Yba2t2LvvQTz0CMdrz040JMK4QxwaKvVxfm9B79JdjJ0/hncu3sYlKvaPPPY4/vGXD6C/byPmMlHSGdKwhjAeOTRg5xOd+PA4zpw+h46+rXju69/EtzlPDm/qwJWrV3CtuBvtXZuwvS2N/NQlvPvuSdZzCo8//yy+8b2v44knH8fGhlakJmZwd3ICMx1t2LR5K/oLITt6Q6cKyK3I5+x7/0Vap9a4sWDUFaOX/3qj3+m13uil66cZw88yqParLffgMdw5hejLae6rsTqUmvRRZ/jMT9mO4VuhPZTpDmJzPIWZO5dw6sRF3LqdwsGHH8W+xx6m0hdHA1X8gY0dOPLoXjzx/IP2Kf/xczFMjE2iZUsMbZsakU0VMXxlBsMjw3j8a09Tt4nizqWTuHrmBFLZEHYd+i7+4T/8AWW8BDhVcWs6hOlsI/rbW7E/NI6LJ0/iL16/Sf5LfYR05NlvfhVPPHIYW9uqOHfiJF579RxKbM/uI1tInx/A/j2HKJsmcf7cBRR6k2jsSGB+6BaufvghpuaW8Y1//H/HV776JB4/tJ+0dROam3WsgNNxkjGOfTWL6SvXcPPKFVzPlLFIZX0Lldzd5dsYvXUTb54rYIk0ZktfM3ZvbkVPTw/6Nw/g0cefwO5du+wogSuDMxicK2Mb/Q83D+LGxYukt/2ItA5gH+nz5vY0brCMX5x2Zzse2dGCQmoWH548hcs3bpGfPoMf/OD3sHPHTuj8vZGRISySIPXsOYKnntyH8Lkf4/WXX8bp0RD6dz+EP/j2N/CdZx6zLxr/zY/eI/+roK1Hr8JnMHbvDu6wL8Q7v/5P/i+kl0/g4D7N1w1o4VjoC5xqeyzn6V4J1YiTbmM2uUTX5L6Y4Od67dcbpafKuLHmDYBPSRNkRlbMeH4S04O3cfLKOC5PhrBhQze+/60jaGtqg742qFhxLewtLWOJss3xG+No7G5H/442NFBOmxhmulOXGK0Bh777A3z1a1/Fwy1hJLNLGE7lMRJuomy1FX3zd/Aiaf65q3MIN3fjwacfx5e//00cPrwXbdNnOJdH8MHdDArJLuzd0o/24hJ+9sMfYjTbhO997/v46tN7sbW/lXw1jFsLMXzrW9/Ck9sb7dXBaFMntu0+gMcffQAPH5GBeCN+fmKOOF7AgYEQ9mxsQGO4kbibQCETw8E//sd48tkD2NmRR26G/ObCTRz/4B7RJ4zv/N73OO++hI29HZiZGsdVHSPT1I6tW7eje+oK3n7tFbx9fAQpdOORZw7jm39wgLLpQ8hNF3GW/TA1uYju7l7s2j6A7NQ1/Pmf/RneOnELBw8dpkz1dXz9q89QNt2JEnnl5Yt3MN/YhQ0bO9HXQjoVvNZdlnXXMHuVO/hRrZIG6knnoEl2FGjMxRv0VsixY8f+h41ef4ezyE3y+0NtN0i1oXDCHhATNX/byhRBsaSDHwsIU7puTySAFiBPPKZcjVgxYmcwRHV4LoWWxjA1nNwCCuUpFKo6t6CN1HU/OnofxZEnD+HAw/3Y2xNBcvYW5kfHkU5sQ//z30Pfw49gw4GdeOqh3Xj+0DYc6KWgx7ok0xVMTGUwMZ3BtRSZRKUBiyROsdw8KrOjyOZztnV2emoM+cVZhLJpxMol9LZ3YufTX0X/QwdxaCCBw60p9LU2IrTpKbTuoyByqBlP7E2gt7sNuWKYSqE+e60e+GT4ZeF1+PyDxrjEKaBF8EiBeJ3NoVQII5MjsSuWqQTM0y0YsdDxd/FynoQmiygV22o1SaEkSYEmhm0kWJtJmBJtXfY1sVA1xTmzjNRCHLnlKPLFFJXAaU6iEpo69mLvA8/jkSP78OSju7F9YBtaGjZRAaICfvAw9h/YjkceoCDeF0E5QuZeSGOOuI+lFBKpHKpte7Fp/9ex55EnsffhvcxnD/7ekX40TF6iQHIDNxaHcfnuFMZHImjrPIJNj30HA48/gl27OvHE7g481FlAV/oWpoeu4cR4GVNUcvOkAaIH7qt3zmmVWYZwfRpfxhL/alUdPr+wlgvcHyLa2Ud8t8+Xc9B1Pog+nnD16mUcffstvPLKy3jztTdx6ewlZGaWgeVFjF2+iNF8C6LbqMwdfgoDxOGde5vw1INZ7OobRml5DHNUGDLTVMLSvaimutG37yE8+Ow3sPeRvWS4G9CdbCQPAJqLcXTtPICtR7Zj6wObsHtnJ3b0daKrZzM6uwcwcPgA9hCfH390ALs3sqIFlr+UoxgcRfuGfmzdthP92qaeaEZVB0WTf0QpEF0aHsUM53Sooxntm3vQtWkL2tr3Y6DrCPbsTKO9QZ/ZnsadW1kspNqx64kvYc9Tz9qugMeffAAP7upCS3YOM9duUlifxBLrGi7F2EdR6FP2ZC28OrFDJjA9y/06500sVEGcgo6+gCwluFTVoamtLK0NjaAQpK/EFccwMfoKXn31/4f/1395Hf/P/88rGJptRXf/k2znVmztWSRbH0Yhv4xEuAebHn4Wu556GHt3NmB7YhDNqau4ODaF128Pk+60YDnfjIWlErLLbHA+j/StU7j7/iu4cPMOrkwvYShVxkwhblv7EznSuOVRLE+PYWZ0GMvk1ciw/ykvLDX2YcOhZ7H78POkcRz7XZvxYF8cbeVJ3Bmbw1y2QgGwA7dvtGJucTeVnt/DriMP4eEDG/HckSQOb49ja0cFzTEKB8kiNu/agX2PPIOBfXuw54FeHNjPcW0qYOjeGMZnGIdEvUzls1AuoBQroEoXouiJ6jIaWx7Cjm3fxL59Azh0KI6D+1up7PUglIsj3HGQ+PsIDh3ejZ2bm9AUyaLMtleW2YbsCG5PXcLwuA6W7uCA97CcIpZmZigTpZBZmsTU9CRmF1PIVShLxVjf3i48SKXuyJ79eGj/FjxI4X9DYxgjcxHc0auoDWm0bIqiu7cdmzr6sKd/KxXl7WhvSSKcS2H09nXcncwi1PMgHnr+m3jw0ACePrwDP3jsUWyJtGNyag4X56YxRK1knnysRIFVx4DFClVEy17CIxJKH+GDFkWlBkp21e4hE/1+XcCyq3QFHZAd5KvzR2Lir9quT2VLyhNKaUSolPYNbMb2nXvR3dWLMutbzpM+FClLptOcgyksFwsolosIkwc2lnNIbnkM/Ueewo6H+nHwwSbs29mD7ta9VAg6sH3/Q9hz4EE8/sAu7OoOI5yZxtIclRSibWdnF7Zu2YrWnl4qvwnkyOujuSxyszO4NTGN6VwJlVIOkTx5LMMHdj2CHcxr74F+PPHwDgz096LA+ulcunBpgR23gMZkN3p7HkD/vqfR98Aj6N+zA7u29WNnMsw5M4qp5XHMTacxfS+HsZE8Uk09OPLcN/DYod14bOdGPH5kM7bsbMLSMsfuWgSpaXaYdupFUyS/BcqoIsP087ua/AD6jlUoefOvc/g+P8BWS3iT432toiejq1FhW8GkXzSGhvYO9PRvRs+mzajMjyKt8wvnC1icLeLORBpXSHuad+3DxqYl9FLm29LXhS0D+9DVvAOJdDNC83Hkk8uYiUxiPrOIfIp4SpoXyico0jWhLZFGevYu7lLhzRaT2H74abQ+9wQiR3rx4PYWfHt7G/a2JZGdX8bwLSrA6RCqTRuwlKuid2AHDh85iMMHt2JLT4I4eA2F4bdxeniCczqJVKQZGdL1VL5MHSuLsckZ3B7NYGQ2gWKmitjSDHLDw4iMjGOgrRPdmzaihTqVjHdJ4o0Wr9QXlG7RubELXeSl1XwWc7fuITc+R/qcJM+bx8TCBNo2NmLT9j70bCRf2LIF23Y8gmism72ap1w8g+X5BcyNV5BfipOeZpGlC7O/4wXyPCFspEAFPE9drYRUVgd4ZzE/N4GxuRTSTeTnj38DWx/djsNP7MU3Dx/El7dxzrS329mPGsx711OYHCWWdzyOjn1fQd/+3di9uxHPktc/tHMJTdnTGB4axcRiC8vvRLkyjrHxc6jMLaK3pQOb+7vQ2dWAUFzfY48hqzmjXX/2ZUC30GcMmXybwrWe6vApIUaaHqfTWaL58jz1nxBaogNojQ84w3I1h6jwjd0bDmdQiU6g2LCIBuJ5udoAfUuoRDyMxDvQ2rmP9PsZPHnkCA5SJnn0AbpDfehsi3E+zmM6XSKd5fjkgVzfJoQeOIxNdA/t6Mee5iqSVcpABY5ugaNMma5aLGGBsslt8uFoaxgDezZh55bd2NG9GwMtveiOVNHflECG+Ye39WLzwX1mlGoirUc6i0SJ9Z4hfkzo4wqNKLb2I9y3DU2behHpaiMtoEy5oR0dBcoz19/GzOVjGI9vwtZn/x66KaO0HdiKB1j/J3c0Y0OkiHvXSrh7rYxKlrhYbEasuQkbdvTi8EP78fg+1qu5AW3kNXHKm9XsAiphzhv+jU+QxswVsNSwBa37HseWQw9h9949ePDB/Tjy8G7Mp29g8M4IMil3rli1vMiRoWxA2U9fqtTi68qKiZzxiyQd2+mw/zcCKuUzBGpobWODezN4STDx4XQ6+I9IaQcBkliEiUwVCm36oIIMiuESCRs7UhuN7eBcii8xraRE80RqMulQA5JNW7Bh0370b92I5vYwWkI5lGeHkVlYRKi5H117D6NpYx9iLc3YvKUPO6h8bO5sQTuFocpyAZPTi8TBCnINbZgkob83MYWxu9eQm5uyd+039PYimYyybBHzMhooTQ1s3IheCsDxzlZ0JArY0lTEFhLtzh0Poal/G1pbS9jcHUJHWzMbQealdolA3w+MidbhdwVk+iySUFciFJI0Hcq8LxO7KmTqnBOh0DKvS7ZNWkYvfSUtRgUuQkXKto3Lel4pYXZ6AhevXMHJsxdw7eYNzEyNophbRqWQQLVE5YtpwrE8WjqaKFDsRu+mHejqpLDUEkNrUyt6ujZjgIS1l3OjuTlJ5a2KnjYqL4kq0mQoGR0yToaTKJXR3rcHfduPULjZjMbORrR2JPDgphZ0VJeQIhGczMxibGYR2XSC82UfNh14HOHODiRiRWztbsCBviYMNFGAovA2nNK3Kqmgs+0y7Gmd1Bm9NBHYYLZXd5ITdK3DFwlE9z8K5svJYOoUeUGYtFn6Q1NTA1qam23HRFtbK5obGsVmtc0M86OjyEfb0bLlIFpIc0HFL5bMYktvDod2RZGMEIcXl5Ff5vwpd6A51oferbuwZc9utPW0oqEhQrZN1kxBpzPZin4qIF2b25Bsi6AhQZxvSaKvfys2b92JVtL2ZEcbujoYt4mifKiIVFFHaEdQJm2fIM/QuZIXzl7EtUuXMDp8C6Ws5gaFdSrklRjnOoXisH3MoRsN0W60NC4w9aStPqc4J2KJXvTv3oduKrFoqKKjqwmbe1vQFQ+hsqSvOWZBOYt8UHRDr9eEzICgV2v8n+aMGRXUn78miJBWuR0MMnqxLVXSHxNokqRJ5M3sh1B5gQrKPSwt3sXUkl7p34iHn/oennnuu9i/j3SnJY9EdY50q4jeri1U1vehY6AXzezL5soEotkxzFBhmShVsZAJY2h0AbduDVIZGUechHBXTzN69HrJchrzJBxpYsF8torbI1O4cf44SqkZ5tuG7naOK/s6StlAxrpQ20Zs2ncEfVv2oK2jG52tjdjcEed4U2BN5ZCiAri41ICFhWai3Xb0bn4MMdLGFiLGpg1UDtuBtrhkDtLSRAWbtg5g254DSFCgTLaE0NUdJi0NIZvJ2wcU7DPnotHsq0qYPJ8YIkExEi6ho2MvBdmHiUPNaGrOoL2taud59XZtQvfAQdJVKo7EubYm4n2cwj4pYpTK3XJuFjPLEyajpJZjGB+jEntvECNDQ2hqjGIjBWOdsRWLN9gOSiQiVGolgO9Cf3cnlegoeljHrqY4suUGzCyR3yCDuAT5JJXzSAItMdJ/KshCHH0dan5qArlyDM0bd2LDlq1oZNye1gR2bejFpqZOO9B/kgL0AuOnKdxrESdMP31oK0zFREZYoqGb2HRS9UzdE26uyH+/HrBVYM0xPQjxDfn1RMewKumJyZ1aUClk7Mt0IyOjuHjhEs6fOY9bN27bF46jxO0iGW5Bi5PakUZcbUvE0LX9AbRv3oKmDsqWLTmOn87Y3IXurm3o7ttCPGhGV3sjelrCnNdUI4gGeokhn8tjaHAI5y9dxqkLF3H91i0sTU8jUiohy3HNkNXpAG/x9eaGZmzdeQAbBzagKVllGQk7lDtKBUlfna2W0qxTFrFII3o37OaY7EPjhj5Ekgk0kK700EUTRZDiYXkxjcWZPPIFju2GTTZ+LcSTjmQIA/1t6CeNi0SrmBouY2FKfadP99OZgu7Hxnck72Wh9N5yroN/x8AavgKO2tZ0h+k2HHf+6Et/opPxxmZ0927Elm07yHsqGLx+A0My6s+mOQ9JI9t70KYdgck8QvlpzM9MkOYN4+KZm7hKN3JzHHO5KeRiWeJkkXKdZEFyP+2epHwXraaRT82S5i6S71FJ3nsQTXv7kKHK0cL5vqerAVupn0Qow02PT2E5XUS4oZ1jncSGPsl+/ehsbyBtojJLxTqSHsJ0voQ55j+VyuPeyDjuDA5zFhXJi7oRbewGYq3Y2L0BD+zcjC1dLbh9+jTeeOkXeP/DUxianLMvSmqft2zNmkPVcBSdm6mo79lJHE9ibngUU3eHUUxVce/eNNuVR9/WDejb3It8qYg79+7izNlrOHf+BvviOqanh1HI6qt1TagWSZSp3FfiMnJQX5ReqI+6kL6ykcRp8aWwLZZlMsvIsC6h1n50bN6LOOdse3cj9m8ZwCPbtmMr2yPQ90+mJrKUszlWm4+gc9s+JLoaOXYltjOGw3ua0JWcI+/NoFBtQU/vZuxhH3f3JHDhwxN47613cOPqNczOzSFH5uw0VBFD0h7WyQR8gmGLjh74da5GfcFBPWW4xC60D0dw7O3MqHIjwqUGIph7mZ4XfbOLY19ENZ5BKZZBKkMPcVDyNS3UEfHR1r4Fu/c+iL2Ur9oaSNfbE9i2qYN6UCtShTKW8yLI4l9hNJLed+w/iK4tm0k3I2gtpqR1mbyoOkU4x7XzXdspQw0NmJqfxNnLp3H6+ClcI/4uTc5jQ0sTOhvIc9mAyUIKt4IzGy+fv4Chm7cwNz6BsGTTDFtBXluMtyDUQp2JMkxI5yQnm8jKI0hk54CJ68hMDKLQRHnm0GNI9Haj3By3Xeg6y2tjq86wo2wwxPbnokzXQr2vk7S/12weXTrrkbytkXOjmXywgTw7QjKir6tOsK5qWUv/XjRt2o54a7ttqmhupqy0dSPlUspJlLt0Bh8JD12enaSrlrHE1TlS4hG2kqUr8d/C5OT3mwGV8ncEblKvwvpGuq2/BjXGLik3TsHRV4fIuJNJPlGRmabivqRt6LLQikbwRmfBkPBV2PHjlOjLXb1ob2jiIDIHErZqNI5IUzMFBPeapcrRdmt9slOKtIxUjUTyGP3DCaItn+2AZQrT+vqWdpnlKbDGk0QWOgmsVZ1x1LcJTz7zNJ567insGhhAu75MwklXjnLCNREhKWAkRNTCyrMZ+mJYB4ULHQJLzkLvBiTiUcQlfHNWamun+mJ9j62A9U8dvvhAvCXuRqm8aotolQJrhCiUbKTQTHyppImT8xRwSYFDIi6yfgmTZQGjkEBtGnPTc3jn6Ad49fU3cYlMN0MBOxoh/nM+6YuoWo219XbiZjRBPGykkhpoHTpEVFd9faqR80YIGWZgqJSjUE1c1bwLVs2rRPU8havGZCMSnKf64pSb0cw/ql0fLIPlyoBVonAu7hOnxNNERiBmJNDhxI1NFCS0i5OgQw8lHDpDF8uzogIxUgyKc8eeXBXq8DkHjeGacbzPoBplJNO0r2CRG+vz6NRVceTwA/jqV76K73/3e/j2t76BI49QsG/XKlIIuUyWgkeVwnQDFcUkMZiKXyhOOt5mSkCZUkmhSj6gOUNm3dySRJK0W1MhKYmFymZZ0lI4RjbUYnPPDsjXvBNuEr+jOhCfc0RfY+PMYj5l8qSy8QhVWV8WvHvuLN555SW8/u6HOH93HIvkJ/FqDskQ+U+iyea4zjnSrg59Mr6q8jiXEOIMFz+hMBEulxGPUFGKRewsPdbalAZ9OTImnqU+I68Sf1NfyXBuf6qHgetl60dzvz7Q6qqM05azymeZFe3GpPBTYd9WqI1FQ0l0t23BAwcex7e++y38s//zP8P//E//EM99+TA2D/RSCNO5hDLEkxezPxupgOtDGfpwBTvJlKNCeYnCaAQt8ZCd3Qalad2EjdsfwA++9iy+9vTDJojlSd9EdhIxUi3y1qV0ARsHtuH5Z5/G4488aK+aRPVuDytciTUg2iCDkL7MV5E9yGSNJMP1KW69GitZoUJcoPhgX3QsiW7J4M96ybBXqehjBsRLjlWMAnCiIQH7+hjrrvOkopGEGSdMYGE79FVcI9lU4ip09ql/Cq+xaNTKjvM+SuKoMyliyRbiWJMdvKz8JRPp3M8YaaoopBYD9cn/vFaXWf8kZQvtnyhT+W1o6sDe/YfxzHNfwUMPPYCNPcTTkL7sGSMvabVXBWPsS/lFwmXKIpwhGkctwIkGsx7CZX112l5nY0opGJU8+U9az2E7ukLzUIpcSO1ivfRxiBD7vVjK2zjItFfSmAhBAjx0QLzhrZx7orM4v14w3GQh+rqp1hUdrroZoq9gii2xmoqJ9MQYzpw4jtd+oQ8JnML83AKHicoAx0WKuuNJqqTwsoHzVB9GYL/pwyuWC/kkESVKeVJjltD4M36IuBwmcsWJZzHWpZIv4frVK3jjjddw7MPTGBye4ThStSBaNlNG1McHrEaMKz4dZeGJpPqbnoZ/ITvnSPKj+GWZacPVqBkbI8mY8VL7eqYB5xLHJEnenORgldjgDGVf6dc6WFtvm8sQo4WEOHm+ZIEIaVteXycn/rMwm88qmCj4kXF0v/IU/dPV+fxuQtAv1kcfBXvVVuHsyEg8YWf57tyzDwNUSm+dPQl9YGFoJo1waw8Gdu5ES08752YGs6PX8N7b7+GFF9/B8RMXMDc3rdxMhopyTIUn6v0QcSJEXIkSL0pFzkEq6hXqRBHioWhaO0mmcUfqI5HGDtIX4jDnfqGYM1mNqG7nuTXEG6kXETeYt76iXSWtyxG/4owng3+cdKkYbUeR+N+7eTOeePoRPL5nC/b0JLFtxxYc/to38Pz3v4VkhXLoj/8UL//0Rzh96gLGphaRIeKViF9VLdSKZm3ox4bdB9Hb2YrE9C1MXTqBa5NVXKGLNzZioL+dda/i1s3r+PnPf4a//uHPcXdwDIWcZGBSM+proqlsrqGgHahN1JcTHdIEt/mtM2JFq/hcLnPSc4zULzIe6FpmveLMp4m6Y4KTQsYxNh35YkYiAOdfjLyJc7CB+bB/9RaCPtIWCieZFWlyPIzeTRvwyFPP4dvf+T2kUiN47fUf4aWXX8e583cwu5BhH7sFWyOaohXmNE/ZH5pbv8tT528BVelHkgWoxySSzaZvh3Su5MIYsgVnhiJJ5Lwrsp85F9jty4Us7s0totjYho7mZjTT33ZniS9Sj2ltpExFRihZM07cSHKO6IMsJfIzLVBmWVxDYzPaWtrQ0OB4HSjPaUT1JWVSYHJgMYuQ6fobOLdnhgbxwdGjePW9D/DB9TtY5EDvPbATvT3UexYXcJc856c/fgU/fY24PzTFGmlDQsl0tip1LX3oS7qbXvUX3de8MfIuUkOkLpUkB3CehnKUUSgfidcwfoT4HIonjbZrU1CZbchSlqzwOSG5mLieZDglFf5JXiF9kEypzDkfJAMtZ7MmUzUk2R+kLe41QznpiA32gZwK55O+TCuZJ2T0iMEB+Nvaq9Bc7jcJNuf/LsAax1a6Bvpm+iaLofPKcNcR/AsEOydaaFQTiDdoJV+S/ixuXj6G5dtTaNMWQxLfYpRcOb+MytgoFq/fxDEKzsv7HsKGeDMGClR4KkRSKhDzRBR9DUhCXYjCT5SKgj7NXeUEKC4vUrFYIhFL26Ha+VwGS5kU0lSaNKjtLd1sQ4zpSiRqbdj34AE8+NhzeO7r38PXv/sNfOkbz+OBrQPoYUOrRLyFaCsmOPDhpWm0EMF0kN5SqA35UhUN+Rkk8hQgVE86KVaNkTwao8YKCdYj7l6dIvcpwKWtwxcBRICSFDCiFGS1wVS7QBKtVfT0J7CxsxlRyjtTlyftTIhqOEvaJKWJ0jAJWaW0hNzMEG7cHMT7J65gajFrK7mHHn4UB/dR4esZMMIsnb5SiREn48hwnmRJtLWyjCqVrhCFAHIHnQuW55wpMlyg/RPREAUyKXysnylusTksh6aRXkwjPZ+DPpsuuVwH8S8W8phjpqUIFQYqWTqQOErlqZBZwvLCnC12ifln84y3sGBfD5Fioi+ByO4WY9w42YeMCY7Ekl5QwECIQjmZhhQwtaMOn29YoXcSXgJCtuqnHzcnbFGAOFMmTafOyJlRwPYdm/HAgYN46OCDOHRgFwZ2dCDaLvpKYVjGUQoz5Uya1zLnVAOF8DZUYz24N5ZFShodBQQkSKOry8RPZp6j6loIoZFKXriYItOn4kcFoVjuQmFpnuFCWq2CEfEiIWSIhynOk3JpmWnyFFRYXowCFoXkOIWJdLqMc6+9jAuvv4KhxQrie57EoWe/guceHMCOTiATJW+gtKs14EgoQ1di/RqpILdSQG9CMdJAPNfr9HmUyaey6bTsLVR09BU72NeNtcqviSBuSf2F9IACiDkJ2PxjE3UGngRz0wrM/fomjjN6aXwkVnJcpCRVdND1EudzgUKRzlnrxZbOp/DYoe/i2W88h69//xvYe6QDXQMUDBupkJfbESs2M007OFQoZpY5ZuzHCuvNfgCVrHxpBF2xHA5tbMcz+/bhkce/hV1f/Wd44Bv/FP/020/h95/ci43dHUirvbEQtm/qxKNH9uPBp7+BZ7/5R/gDlvmlJw9iUz/5OZWaKmnbUqgFk3kqiOzHZDVDl6M/x14KDemVcE7nsITDRZa/iIXsNMVR9l2Uv2XlQXwqd1N2aOMIcjxJf5dJ30y11asqxRhpaQMSkVaEdSYDxyFEethIWq3zvqLMP0/hNCfhlgqxdv9Eyzk02JeeKxRQ45hZLiGbXaQwWWa9OcpSmFiFCmmsBF7tYJCg2ZIsY8/mJjz+6EE8+PBXceSxb+DbP/hj/ODv/c949pmHsK2PQivxvFRO0CWRojBrxqiQVsizpKlZREshNEcTKMZjSFF2oYiMWDSLFuK75KVmEuJEsoctbUMuW6CMtEylkMoyVeky6XKVrsL5UOLcqmh3EOeBJBstYmgWu62HuudV48T8pIjwNqDxdL8+1DTQ+owOeTfMZ59F2L6Idj7RSbFhFzgopDFy4wreevMtnD5zjvWJ4rGHnsDjDz+JrQN9iEfI26LkR8Z0ZIjtoRjXw/bPEGfJp8NUjjRnmecS8ShFPAgvV9BCHJahvBSiYsXha2d4dSGHE6eO4fzFM0zbgO27n8RDjzyDPbs3oJW8Xkd6qM+qlDsjMq5Sscrk5o3uQTyQuKdDgUUvdA5aJcf2EGvUlIVKFpmiDOgaW/aqaexUrrJFNIsuEveKlCmy5K+SdVWQaKN2MOQoDy/nllEkTelq7ASnGtEtR3yhfKzFAdWJfWhjaU73AvWuzX5G0MCa5+8WWJsNg3WzgsviWdolaHOWvlUZrPVV2DgVxs4N2Lb/QexvzmP+3Ps4dfIirsyRH/QdQO/BfSi3M13xJmZuvIqjrx7Fh8fHyf868MDh/Xjo4YPYvW0nmqiYk0BRz6AjTyoQJ5JtHO9QAyKkH2HKeNll0rop8rh8hVjCehUbkSq2IJXTK3ZZdHQ1I049Z4m8L0l9JUr6ECf9aiJONArfGjdgjnjalprHzq4E9j7wKHY/9T9h/7N/iCPPP4Nv/eFz+IODvXiihZShawOST3wDj/3xP8E/+cY2PBwfRW7iPK6f/xDX7w1hokieyc6JhJZYvwzKTaQnm/Zjd08TnkqfR+j0C/iz8zG8t7gbTd2d6O4qIJ8dxmXOlaNvv4kbd6awbffDeOqhh3Fkz050tbWTToZA9GbvRszIV+T8q5AXhxOcxbEkGqiM56lj5YLdVRoPnW9ZZnsLWRm+I8R55pHOY3luGalF0nDOo2Z2VpzdWyDdnJodwwL9SyIo5Nji2dPzS0ilOan1RlFjDC2drejf/Qh+/4/+Gb73gz2kMSN2pt3p03cxNpU2OVuzRJsmWEHWQQaHRo5BQlPajHJ1+HSgUcjR6Y3DarwFjS0b0UUe2TZNHBo+i/HZJuJFAmGOe0NsmfLgAtK5RdycHsXVchSZ/r3Y1NaGzZT1WtIZFJeKmJ/PIpepkBeKJ8aQy5NOZiSH5EmHq1ikrDKfiJNmk6cJb/LaxcwRTeTsVcuodrWTv+Q5nvrCcjQ1ig4sYgPpaW9SxxvtRPTRL2PPd3+Ab33/WWwZCKP1zg3Mv/EqTrx7A9fmu9G883EcfmIHdh/qpTzTi5h0OyKGcEa4l01TNqqmbRNEhfO9EuGki/SQjCeQK48jV5pmeIXyA8PIL9LZEpbJq+ORIno6GpCJUedKkv5wXkSJfSHqmQnymbAW7krkb0ynjXNVMs0I502sowXzxSxmqFcWyC80b4wnUQbV68Ilxo+TTMm2IoZepXwu67mnf4LgskIi5f/r5vPrgbX4DIPjEUQyKhx06gtzkuoJWv3UAcjd3RsxMjyLy5cvY5qKf44IoLMa9CrL0sSEfW53bm4eBw4cQKN2kgTpLU/d85rjpUJhurmpCU1NzUTMgn16XJ8a1QuKywuLdujt8vKyKmDOVmCZn6C9vR0D27ejf88ebNm9E9u2NdOPCnhLI5EvurKCoN0rHR3tZil1r+KEiLAkk0QqrfZoeU1CtR0ezDh6tVH11J8Bozissac6/C6Bxl4uGkIiFrd5oSXgrt5emwdaUb546RLuDd6l0JqznQglzoFSKo2FkWEMDg1hbHTM0Le3dyO279huZ4ds3Eim0NVlOJelrFvSq8FREjUpgCSSmkoGEp6Ij8Jl4WSysQHpEhMYfrJaxGelieiZgnVnZyfSqRTmZmftk80SmqfT05idnbODsLVS0tbaxnnSYWVPTkxyHg9r2priuTg/b36acw0NjWjjHGtgXRRX5cvVJ8LvNgjnTYEQnhIf4pwXHm/tYGTGkaGBqicZMqUg0tsNGzZQEKhibHwck6Tpor2aL5ofExPjRo+bm5vtkHblVSwVDbcZzRTOsFbUAtpdJJ5qV1WygXOGuKmvzKhcfUVOcWRcyuTTVp54jVbHlUc+R2VjadHy3bFjBx44NIC9ezrsUG7huSapdm+EQ2VbsVc8fQBA/ChHAZm5o7lR9aPiwrovLCxjclKLN2Gkl1O8n0KGcTXPxG9aWm36aqqa+22AW/ljn8mwIN2Xo6HVdv3JMK7+0Geqmxob0d7RwREK/ugfZ9oonQxl2q2kbfNF8mejG9pFJAODFBR2kuiM+LYOMxY927OnH/v3t2Hn3naEN/QgyrBOhonWqG/7+3uwbUcz+vbtw0by7I2bOplHAxqaiDfsa42haKt4u1ZQrR4cfNFT1Vk8vLlZK/gRjnuDjff8/JzrV/6USPO020AfstEnvoWBwj2Noc5RqzB/fZZfy3eZhQWjtYJ8Ps8ySsSdMPO2l3GtzSYDML1wSffCIetL5qdd6g0x3jOyyQvMO2oLeSXbJatP4rPKduDr9m3b7GtYOsh+67YO4kUULQ1JJGNOJspmcjaHJH+Uimyz7BQsS/2hFe0Yy1I9XNnsK96lKGhr0VCmzCrLbWlttXFPpXJse5VKZsk+gDB44zoWyAdUj87ODltgYY8bPlgFhSC6/hbBjZd2bOhJRswY+yCDjJgglRsOgbVR9cpksmxTivKj+nE7du/eY3REbRWu2KtpGhfG1dl8kh8Vxi5BiPSkxLEV39ROK42txkgr6KqA8F31EF5pJ+D4+IT1034ZcB/ejwP7NxuPFj4aDWExYfab0kmOtN3QcWUVtjyEIxp/LRSrTcIT4bH2Wmv87AuXahdBY6sFJeXbxHwkxyqOePTsXBFlvXqVzWJuZgazM7PWIRo/VVntjcU5P4IdimprHT4lsL+IHsYzhD+m47DfTdJn32oObuzrI471su/ncOnSZczMztiHCvbv34s26rMybgonhccDA5vw0EMP20dhhCs65Fm8UPRVeZtuwX8dpC5+pXkq2lUoFizfedIh2U313t4MeeLU9JTRme7ubvLBVsMhfdjDomgHaT5neCZE6OrqNvlR/LKltQV9GzpxYFsf67kd23ZtR5L0196QYQVYVdtJsvWRh/HUU09Z+/QxGzkFmuGI9MSQnPVubWvDAHliZ1cnxsfG8O677xre9fX3GS/I5fJGN5tbSM/Z5r3Uv/o3bTI8VrsVLn7NicCmFZBjXNHkgnbTsi46wF5tsLcKOLfFs/Wmj+RW0W/VWzR5amraPuIyvzDPcXKLa+o/zQPx2cUF5psi72f+oh9Tk5O2EKX+a29rN5rADEFmx3E6gr379toY63DueeqmqptkFJuYzFTzUX91+NuB+GFJNJl4JNmgi/y/mfiZoS6kr0MuZ8rEhaL1e4pjMEa/YepGHDBs4PyRbiLaKRxMMY3GfWZGxxllkF9awhRxcXpm2ui5ZEW/A1c4J/4tNqlzr5SekYxWC1dKnDvCrRTxXXgonH300Ufx2KOP4emnn8LTnBPi06Lf4puaZzqiY9euXZxP+7Fpy2b0bewzWi46LrlI+Kj5rbdpNGeL2tqo6cP6x4lvSfJ44fTk5AT5dQ75ShHLaeplxLt8IY9efWVyY4/tTtNcyrFM4Z/mTbFcQJV+kgs07ySrJFhmPBa2dksmnSOv0DEN5ZL4UdnJ0oP3rC96qZs2NzcYjwlxjoUS2v24FrN/21gumvt38PXGTjz33LMUXhPGLI0SmtOPrtoKyHs9s0fMm1cNhIRHbVuU5T4UjqEciyJTpQKxuIDi1auYOf0Bblw/geOnT+Dnr3+Av379LN6/m8KmB7+O3//BD/BAZxal+UlcGpzH+QktAYTwxMEd2LWBWgEFjXJrHxapZA+eeRPn3/w5bt+9h4mb9/DeSy/jvdPncKdEQXfvATz0+IM40JnA9OwS5sauozBxEzODd3HtxghOXriLM6dvYPTuJBoaMxR085gYncPIlRHk57I49P1vIcKyMndO4ta107i7zGr0PoID23djd/s9DI6P4uyVeRLOZfT1duKxxw4jQWKsblBP6irnfgiaTbxXf68B32fszwVOWn21bIGTrf71xs8p6JWSSIFIQIG2SCJUJJGJbQA69qKhrQut5ZuYH3wfb5+4htvX7+Lqh8dw4u038Ob7p/D+YBbVjh3YFJrD/NgtDE3MYGohRUF2Clcun8fbxz7EYrUdzz3zBPrb8hgZvI6zVyewVOnDA3u24sGtMvGHcOXqJK7dHEY5UsLhhw5iG4UwzacTF27g9mQJbY29OLypBb3Ry7h27zp+cTSN6fkZ3Bq+gNPnWY/3zuONd66hcdN2PPvlr2Lvlm3obwSyc/dw/OTbuHLuOHIj93Dp+Gm8+eFFnJ2mgrXlETz57Jfw/J5Oxg1eRbaZwO4gpdBdBXFWzykRK6hcR+nPJHzarzfavVxAo8yPTuNtmyqoHYiByygUZ9AClbLTZy7i+Nk7OHB4P7bvHqDA2UhlXQaxHJMWEG1swzKSuHPpOEbPv4PZG9cwfnUMR1+/gp+9OYop4vvOp4/gkWcOYPOGOKYHr+CVN16mcL4bTz/8IFpbpEjGsTS/jEvnT+Po8dfRsv15PPnwAWyMLyC3NI9L96ikDC9g04ZGHH5gCxoj7SgsFXDtylXcG5/8/7P3n1GWXdl5IPg9b+OFNxmR3ltkJpAJU4UCCuVYhqQ0pEjRaKjWaKhZkji9ZrSWNJofM6t7fkg/2EtLUrdWs5tOEtmLkooUiyKLZYBCwQOZSO9tRGRkeB/P+zfft++7kQ+BSCCASot6O2K/6849Z5+z99nm3HPPRbxjPZ56Yi+GT72DW9PsH/kiA8xpTAzexLXzl3D24jhuLrTguT37sH97FLWwD4Ojk7j+3l9j6PiPMF46glj8CfRG8gyeRzA2ewNvvf4Wrh97FYMXL+AHP3wHb12aQbl9PQ49/yyeeXI/1nUy8PDT0HgZzLPtQjUNuvhQpAGW8x+qsl52Tm3ME3Uw58ecqk/x9UYiNRXbnkGFp4QAdZcGOxTaTY1P4TR11LHBNHLUYU+z/Q5sJJ8rWXirHoRos6DXIL0VOq/AxfdP48zpi9j+uS9j3UAXyyelftJGlRiezSFJffbG2DCuTk1g7soQZt46g7NvncJfzPoxE92EPdFJ+KavYOzGIG5cH8L8rdu4deEy3nzjOF65Oo/xAp3XEFVpdQ6zEzP4q5fP4YnNXdi8sYOOYxCF9BIWR4bpD7C9Y9uxe8cu7IndQiV1mjy9gPNXz+PGyct4+80LePmdc5gk7ZX2FiymSrhx6jZSS17se4oy1dEBTdKYmpjDO+8P4cL5JXzhyJN4aX8BgzeH8d5wHuVID3ZvXo9NsSounzyFU4MjeOqZ3di4ZT2Dz04sTBVw6/JFDF07Dw/p0OsQA5UcFig/F2+MYzLrx7at623x8Uo5hqnJIYyPnsaNm2dx/OJlXL02iR+/Rv1+dhiV4jh1dh75NHDy2CJ9jwlsf3IHtu/qQ0dtCemRIVwamsf76R60d7Rh60Et9O6Hf5aB8pXjOPXeCbx1ZjM2te1F2/qbKPf5sZDNsM7v471Xv4cbtCEvv3oKf/Xaq5ijDBx46lm8cOhp7GyPYkOQ+luLwatHB6nJ6UhrspBCY/kscmsqvCT59FD+tE6ZhFOD1Kt9vVHQKIsfByav+mNBAW8Ri/MZvPKDN7CULqFn5x5s3LcfHYEaegsppJI5XKMPN7WwiGw+RR9xARcvXMIbL7+NbKmCHn1pdNcObEp4kJ28itfeexuLLYdxcM9ebG4r2WvImkV65vJt5Ipz+NyL7DvtEfhY1tWz13Ht1iQind3Ysa0f81OXMEF5Hpkp4OboHNvwMm6ceQ+Xr95CsnMXnnnqEPqzY5S3kzg2nEVt23PYt2M7toeGUSatJ85PYmh4AR2trXjq6DNYzBRx4vQ7mBq7jL7+jdi5ZRs2JHzwZcibN1/HmblN6OndhkObgfXtiwyIlnDm/ATpOoHTp17De8dO4Qffewc3bsxj886D+MLfeBrbtyXQHXBmo5TKelVIg/7kpKakeAJyFcQ0tq64aQdkrAZgnN2frq838lei+8EzZsecS2olbuvJKmzVCmMbveaYvnbTZkJdTwXhH3gC++m3H9i7Dv1xL9rTWcyOpXH10jQmGdAu5Wdwe2keJy7ewjuvvoyl2XFs3EndsGU7Sgzwr106jjfe/RE+99Vfx7bdzyBapA949Q28/96PbCZZdnQCb/3wdXzvrYu4WY6j//DT+PzRQ9hWY/9/9y38+PgINFiz/3A31q3XK7Fe+GvdKNW6cHFpGINjFzB89i1Mn30fM6T79Xeu4sK1W6zTHPwoYuzqTbz5336I7//p93Hl5gzeOD+IxVwe3X1t5P9ubN20CRG9Vq1BWB9ly+c82A3lF5CfuMG46iJ+OBHBwM6d+NJLB7BnUy9ChRymGaNdvXyd5ReoE0KYGqGveeokLgwtoRpdh6dogw933sLZC1dxcSqBWMc67N/RhYGOMm5eG8KbF7M0Vnkc3T+Ajd3d8C3mMc/7b735Cl59/V2cPnMdr1+jjzx+HSN0PtfpS3pPH8Z+zy0G99cwemUQC2dPYer8OZy/eBP/7Qcn8ZfDYWx64edw8Olt6IwuYfLGSbz94x/RPrxJPbKDvvA8Ftn3tfbRE/s2YUNvDC2aeVSW1aSPrzd82L60cKb/NBHWGVb5bIL4LF/jXny9USn8ClcKTB/qQjXWj3Awh07PaRSyZ/DexWGcJX8vU2beO3kFP/jBWfz4R8NI5nrw/N/6Mr7xM0exuzOFUnIM589fxutvHqPuPYHk4jCGL17Cd//yGL771iCmvBEc/uphfOn5g6gyzx9+90dYCAbRv30ABymbOwMheLIlTC2N4MrkNE5Q/wfaOnFwZw82Rhdx7p3X8N0rbZR14q13kTr3XVy5cBJvTuSQDXeiNRHG6bFZXB++jez0EMqp2/bg4ezFKXznrbcRbi9iz67t2NK9AbFiAenpS6zHt3FhjH5X1odYSxihjRtQaBvAJP2Ft//bf8L0+TO48d4pvPEmbdeleSRjXfjczx7Grn2d6CgO49Uf/xXOjrAfrTuMJ+mvbO5J2muQI6MjeJf6+mbKg/DGPdh7YAs2BmYwO3oD87fpT908jaGLp3DmzAW8+Rbr8NoV+t60VV96nr7SADqDcQSKDPSqzptxHk+ZjKK20yugshPLWOCxht/vvAopnss23KuvNz6kQa9OPP+FLzgzmpZpqtdQwPvMENj2znnt2/pavMcCIb8HwaAXLfEoOju6EKi20nGZw2R6CgvJOWQzKXuitn7LThz6yq/j4BPt6PcsIFTMIocYqi19GBgYwK4dW9HRxsbzMSBgBwvr9ZdcGdOz85igElKH6yFDutta0bvnEDY98wJ27tiEbRG9W+tDKB5HjkZldmaBuGQDYZMz8/YkcOOGEFqiPniLfvjKEXR19mHbS5+zd2s7UmPw5ZaAjk1I7H2RjOzGxvgoK1pDqtBJodXnqTdj+3Y6dT5n0Eug7R1W1kFt0sBgAzadBS10IDVSfaw56PVYg/MkWa8QSlnQIWBH0Cu5Aa0BQQXXkwhB71DfmNUCggwmF2aQWWA/oFMe6hrAfgYITw7EUcjlMDqfwyIVss1zZX+Qge3f+5J9Hrs3loS/vMAiOhHp+xwOP7kLW/oy8LHs1JIGm1uxbsMAdhzYgURbAJHcHPJ6VaxtC/q2HcS2gVa050/j2vVruDy+GYFEJ2rBNJKZCSzNp9DC+7/+jW/hiWcOI9HaglYa+BZflQGPD6la0J62Z+bG7SnNxl0HcfSFr+HQwSewobuFxkv9QG6AA6YdTHblUDsDIibJTXF+ZGGtg16u5tcrZQKzB0Tjtp3ijx6p8cBTLaKSy1AOCwwaunHomaPYumuzrcflrrmjYZhAtYJWBoN+rx9aj3FpIY25mSQdmiIi0R7sZvB16MtHsIWOS2eIDnchbU+ft+x6iYHeJjoiHt5bYVk5VDM52qAANj/7t7FnTw+6Y4sIlVPIVeIoxhlsDKzD7r0tiNERAukq0MEPtTBg2E4nY+cG2qIU7VcI86UgFtJ5FFKz8Bfm0ZJoRXjXN/Hkk3uwnf2uLVy0RYjTizWMDs8i167ZTDuxpbOCjljVAoSZHPtOKolKfs6e/rd2b8Xhp7+AZ549ag9O4hEvfHQoNCzsY2CqoScNEmuNJoHeyjTQYUPfMftB3fBpBr3U4grkzHXXIjN6tY3tL5aFSlnyKotSZCO6tx6h87YVW/uqqDCd18uAh/zxai59NY9yjvelyDt/HJue/iK617UhFM4x3wwiDA474z20rV5czSYxk0ohQ0cxOzqNJNt8tq0HrW3t2NuVRVfUi7I3jpmMD9OTk3QSJzBLJ3K8GES8swebukPoC6fJ2xLGS/pS4j5s27YOiZYAglqQVrbaH0Jt15exicHKlgTzjFCeGeQPM1BamNUC0SWb+dS7pRdd67oQZKDvz9F/6KUTfPRJe2obr+jriovIVBLw9x3F/n378dSWGeQzGSyG1qN7817s3tCNPm+KejwFxNbbLPWedVGEgjVUCxU69DXqwha0P/08/Zd1GPAX4c0soVAmrV27sGvXTuzYWLOnshpsSC5lMDI2hcmFFOYWMpgcT5FXPqxjm/f18h5/G2nvslkYW5/YgfUb2W6eNPzZBZS8CSz0fp513oQnduTQQRraNCMjncP4fBHXknS8t+7CE7tm6PO0MK9uJEn2ONu4UCpjYWERsbCH8nwIh5/7HDbRp0lEPYjoFTzKiL64Krlx1kQ10eF5Z9DLPZbNU59X/79Xg15aakQDqnq1EJUU27WE9Hwa6/s3YyNlO7Ztg80s7qa3iHwennA7A3wPfct5+obj9lS7P9GPrdt2YfORI+infuiMaKkK2t10Bt6tX6deWI+BRJpykKGPGEShxnZtb8PnXjiIWDSAaKGM/GISYFDQv+sQfb1taIuQ77x/lnKaZgzgK2fQiiWTndiTP0u53IatlWkkqCsCPRsQPPQz2L6jExtD01RxBSxk4vCFerB54wD27doATUJIJhcZhCQwsOMwetdvQnuMdBYXkJ6lPul+Ebv27MaeDTUMdFYRjnZgLt9ms65L+Wlkk0l23Qo2b9qCz7/4InYe2Y9I2Ef50MMEdXBpFfKLbakPV7Dx7/CtjgY/tYNejcAzDSc1jqtZIFrbTRZPa6qqTTWAqHPRLO0a5T3YvxfbnnwOB586gPUbEowH9MJ3EgwjaU8TlMso8tUsFjPTzuw/6sU9u2k/Du1H94b1CLKP5eaT6O3tx5PPvYSNGzvRG6VOpb1ayBSw6GmljkiiNDdGnRHEugNPYz/76v6t3ehlvkuMqyrhHTh0+Ag27+pEop12kDZEyxDrIzGVSAiLyTQW5xhILy7RViQxNrFEPR1Gf0+INjBgXxO9eX0QQ4O3sMS0uXwBrb1dOPLsM7S7B8zuac0kfUxEa8N6GIdpACzKQsKePLtgBamtX2Xs+DyOHtqAvrYwWgNeXtNHRehfFlvZbrRsVbZBKYN4L9vs0Newd/c6HOgcRpZ2MRM9iP7N+7F7WzvWtWRRzOQx693OALofz+1fRz+3E/FgjOeruHVrBEvUUX7a6HgijI7eTvRv3YmNuw9iL+3VptAc/NQBRW8/itUw228Gk1PDxtPdn/9ZfP7zX8D+vZvhJ+1zY0OYujVk8e+t6Tjy5OnO3Ttx5OknsXMX478E25J8Dynel9wrMtcED/UrnSI2B70+mU6wh+N+RguMW6LhCtb3xtDX1YVLcz7Kix5cpKgXKYcp+RFBPHHoMJ7/pW+hm3FGj28BYfoe1XKIPl43YoxTPLRZi/MLyM0m0RKJY9eRg3jq619EX2c32uaWbGZgx4Ej2LTvCWymXPcF1Ydpl4tT9oZMNrYRHet3YGtPHN2FcVy7chlXljagt68fXcElFJPjuDo6hVNTGZtV+eR6rQsZYYyXQJH+TSG3gFpp1myDr2ULnjh4EIee2Iv1kll/hTFbyt5UGK0OsC+1Y2t/CFs2tKG9oxsl+jh6U63G+DDFfp6nD9FFmT/03LPY99xT6GhpRWtmjP13BtHeQ9h24Hns3NaJdW2L9D0ryCWz1O8+xHp3Yf2uJ7B9SyfafUlENEOybYP1ZU2skT+vGeMR2rOvfPkbOPD5J1g+60GDEGDH8LB/14TGITGIbbS8J5TXaIwz+y8Qz+/loJfmRljWZbeEnxAknC6owDI7t4RW8Ad/8Af47ne/a8L8//rn/28z4rawq5FQR20004tbe+pnx0QBDyTI1jByoplYCwrn8vrqDJXtzXE6c3RkayUU6clUNEWRznl7u77ycRADHX60F8fgySzQOfZjKh+jUvXQ8QuRlggqCgJYcGFhCrPDV3Fj8DZGSz02dXbAp45RQamtF9iw076eRFYjTSGZmhnFBIVtYYmBS1lrWKjcNjpj67FpfZUOXwX5JSrmmSq0gPG6/ezIDN59c7eRmh7DQtmPUucmdHUk0BmmQDJ4m5yuIZOpoaWVZa/vtdkMagaxV37FSjAxYnu74iTQlHt73YH3akrnv/2f/y2Gb93CN77xDfzmb/6mTY+06e0Umk+iTJrwsIDBTq1AOWC/shUYzNXkEfsCjXyBRnd0bAxn2Q80JVszJnx0fvwxBt7r1mPLls3YAgY+Y6O4PDqLJa1RFKVColdcpDL09mxkYDNAJz+LKvOaSRYx7+k2+etrLbL4Euan9LpimjrJb19kTCT8CKbGMDs9iek8FVB8HXojRcQG/xO+/e0/xV9PvoANh55F19YIfNEUQuyv28sJ7GEQ17K5Dz72g2AhhwKdqtvsuzcn5pBlgOGj864pxon+rTQU29DdEUdvkDSyvxZNA7Bu/NUXKh3J1S/Pa7EYyrL6yR1V2ISHDa5d0Favq164cAGvvfYaHctb+JVf+RU8++yzy6/vSBcJZf4EXho8abiqZn/U9ZStE0C5L1MZ6uVFXzmHSnoRs1PzGBr3o3NgHToGEnQaKF9M6WceNfYamzlUplyPXsfoyC3MzDAYzQVob2gnOjagvbsLnXSI420hRNgnqnRyxiamANqQHl5rZVDr91Cf07DPTS1inNcinQxE1seQCNOpyM1iZsGLsXQX6xPA1o0ZaNHfdNaDGTpGmWwF0VgXDXY7avM3aK8mMTZZRpZxtd9fZMCpNRkYwLTsw0DfOvS3sB/UcnRG5hgs3GTQMIpi/xE88cQ+bG0tI1BYwPjUHK7cnqPDsUjHosg+H0Soewt6N29FvxwiRkh+v+qftQdGWpNFA19qz7I+m8d+E9Rn0QUNHUe8kH2Q/ZYdl8Mup0OOqV4l/PVf/3VzPOx1qQa+uaBn1rJH6qM+9vsatzUL7gh0ouSEDac9yEY6MNDbgR0tWm9Md1C30RaXPSlyLIlyroz0aAWLCxm0bOlHS0cYIX0ggDxltVAu5jA9OonTQ+NYIl8CxSIi1Yp9TbGy4TDtezt2t0zBm53FbQZiN8cYICXzyJJuLSTvb+mnrd6I7eu86AnNIreUxvnbcXR1ieeUIQpQtTCP7OIo5ugkz8YPobMzgfW1JXgXJzAyPoJLtP+LpBPYhhB9joGdHehZl0CwWEBhcsbap33zNkTC1MWlPIp04MbmixijD9LR0YqDPQtIzk/hZp5SHWtFb0sC7VTrczOzLBPo6elGazflPlBCIVOkL5Gzr7lVe+n89bagw5NGiX7L9Eyaer3NHrj1rSszIM5hZmKSsj5KP2XOlp7T2mF+avm29g5s2hhhIKxXDqKUZTr1ySQ6+1vQ3dOKMOWllJzBwnwe09kuROMRrN+UovwXUdK5kWkM3prBRLILB544gH279fpeDTMKbodu4fbtGfi0rhllKNzpwcCGfgys22profq9VQSZj2Sh5NMaadwh7+1pL3f9WrON5zTTSwMominlI78ls3rF5Dd+4zds8PrXfu3X8LnPfc50h6BRFu+A6xPd0UECreNVZeZakwXVJAPdHCYGpxhYsH/09aC2vgthdpjeSobtsMR+naGNop2bn0SpmoOWwWit9SAYjCK2YQCJng60BOlPpScwMT6KTGgTetd1IBEhI6mfFihzU+R5vlTE/u0b7ZUqb76MOeqQOfaHSGsfenp7kE3doJ82iNlZ6rSKPpIUhD9Mf5F+WoxBW18/eZfLoUjZmC8wmOrZjL6+BFoDC6gU2a8m/VhakG33YvOWFpSrBfoFKeqYPKIMhto62hALsX3yKUwM38JkqRvtnQxwWktIBPPUzwVcH1ww3Zyn3yt/M+6No7+jn0E/6d6UII88aC+Tfm6XF41mOtlk6Q97VYug6/pTk0uNaxBD8Gd/9mcWD+h17X/0j/4RfvmXf9l0zN0G0B8nYFWXwWrQeKIBrE201QH7A7Ut0wt1VvENt+NzGL09ivECfav2Ptq1buq/kLVza2UWnsUkJgeJE4tYIO9TVON6nSnsT6ON/aO1ayMD9m7KdBGTI0MMnIsY2LgPHZ0tqJXneB9lbeQ2FlI1G4D01dqtLyU20I/bvI5BbxQt2SQmbo/g1hx1VVcvuvt9iLfK9/KxX5K39AvHZmYwMjRCvTSOMuOxsjeMZHDAXrU8sK4FrbEg5Wqe/ecWJmijy9UO1s/DPhPH+s0b0dvZizj7kYLisr9kgwT2wTG1QimN1Ow4+8Rt3Kj12auNW2g/2yM+BKhL0/MzjG9uYWgsi0A4iihtvsWHEeruTtaDvuP20Az15SyGMjH6wx3o64ygLVTE4uwibs5pcM2HrX0x++hYnsH72NBNDA4NI+WJId7exn7j1XdTUAu2Idy+mXqzBwOlQSyMk66JMvt1AUvpNPLlAvRhsq6t+2kbe9GjlQryi1icHsf8BONT9vUFz24EyaO+/lasJz8V9+nZhD5QFWJ8SMFHJUC/RmPJBGfYS31LnsxnB6SHXV2svq6BjW9/+9t49dVX7YHGN7/5TXzxi1+0fXdAfG06gXlqxhzzLvkZK1EWvOU8PLkkFqkzjw9O0v6nqCu1hELQZi7HWcbA+n70HdhiYxJR6nxQjudn0xgbTSKZWqTMZhibF5AuJhAItaBvYzu27KZdjifgUz8dnUA21kmZI09b6D9ozU8PdXj+JtIsb3QpjCL9zHgtjcKt9/Gf/uRPcHn9L+H5F17AEd9VRKfP4+RwFn96u51xVSv+H//dl9DSQh9tchaZiVmk2c8K3a3mjwVKjL865UcOoD3RAr/iv8nbOH/+FAbzIbTSjmzdth599Ks81KsLwyO4cf0GcukYbQqbKBJCvLsdvZTjrs3tCDIGDC6lMEZdkCzEEWnro18QQHsLdQz7YZq2Tw+HM6Uwom296O9ln6CsL8wuYHFiBFP0f2ZSOeRq9D1DCcTC7di5aw+imzrYJ/2IlOnVqVzpOfq59kEc19FkLxdXdaRVbB2tqdf0udER00o3aTD0t3/7t+2V4RdffBGHDx+216rd8SXJUuMA2Eo/wF/ff2iDXv/8n/9zMtZZ/8EB3UfU/fVBLzk7d3JzQGSrucww8KLaUbRLqUfSege2gCwbPktHKhfSE4gIDUAArUwX5y0+z7zNCihXYyhV9GJ8lQK8SKWnCbgxZilFvghPaYp5VbCU32yGOu5LQ1+oKwUjyIeoOEl3nOX7WG6lTCVOg6OFWwuVMNkWgJfOrb7IEw2kmVafxyUTy1GrX1ALuVLJlioM14yzCuYZrJCGsifBuvMcA64apVPp9JVK1dsRCsLKRiHYYBfb27Z1aA56fdZA0l60PUq7be0ZqxZXrBR4WV9Eo4LKpNnvKKtVGgtfhMaazimVXDDgR6I4ZSP32WIFBb2KoC+daaFhyng1RKeHMhFjABwoyf1iGl+BgRblWWkohR4674wAKca8l46wvk7lKycpriX2QxplzdJg4F84/Wf44z/6Y7wb+Aae+vrPYefhzUh0edHiKWNHQWuPBFCKa6Flj/Qgu0CFdqrMPlRCkVvNrvEFwvTg6AgxONAX1FprjAhJZ06LIpMWfaVSi9rbzDf1GUKJ5SswUrt8lp+MPW7g2gVt1zro5WoyvdokUGDlzkxyBr2oP22QhOaTMumlEa7RCS+U2+uLmGptLS8CDG4DtKWyJ1kNYFD/B6nfq6UsipTFAg25FvHWl6cCYco+A0I9DJFDr8Xr9SQ+F86YngyzXK1ZV675kWdAqi+4aRFof4g6NKBBmgKK5RD1ahv7TA2xwJTp5YynDQUtUMu+F6UT5vdrEI/lF4uopcOo0QGTs1+KFm3WSsgXZJDPYJd9yhbWrdJRKo/T6cohFdxk62AlSKOv6nxtWJ9tL2tWckFBfJj5xIBoEGG2g77KpQGnimZOkaZgRa+lsL9zv+xTkMX2KdGjl5VRx6mbZPHiJxn0kvsi7ohGm+mlSwqQ9TSrGKBtAlIsPxeoQjF4hxx+XpfDI11TpM0tetPkvx/erNYcZN1CS9yS37UI9ZgGa6rUUSkrv7jE/k+9Vq3mGYgXyA/WKTIAfcQyjhnSUeB1pqcayRf9mNLC5f4gWrhtYZtHAjna+CWzm6VCuw0e2loU/NMSBSVvBiWWU66JFiBGlesvadH3ReSr+vpYFZnaNuorfaWPfgWFLlwrIEy5VN1r3hbTo36N5LBxyC3SrnapIkF+aFZbxpe1gUif1ruqtFLf0pEjPZr1UQtSvn1a+1N2WzJGvlHXBSSrrK9m0tFtoJ9BuSHPqmxU8b1aKtjAYLGY5z0l8y986LSvewZDAVunQ/0qTxrUjiHqaPWbMiupb5V4qZNbM9T73gpqMco+y8tTxtWGFTZmkMGEnrgG4q3WXqXqLPJaxJ23eDL9En/kWgssL4C4h0Gp7ATLYediAi/y9HvUt+XTOXMbKIZa7J9JrB/zfvUbtYPS3atBL8vYZh/xmPyt0gbVCrQaDD6LAeqRCPsJqYooaOK9+oJqsZBj3fJkn+PXhmtdVpaXttXWxiLxksmq+F7Jmv9W9MWZWl+B07o9DKYICekC+qhsaWhx+hp9QTnl/oAWzs5RJ/HeHAM12vFiIIJkuNN4sr56m3nqAwHtzI+2UXR4s1bvDPnCkhEoUHeUfEzH3CMMusjvfKmdNOm1YfKLfKx6qb/A8llnfznD+6XzKO+2kDbbgQGf1maZpyzK1sfpG0fpK1B8kYuwT/IvXoqzXVhh8UhMYzNqI3mW7yAOMFeiI1cKXEWnoDnoxdP18/Zwv27Hlge7DIFAVnEAZUC8In+qlEsEpJO4QRYB6jsv02iWoga0lwJRyqWPtmwO+sCEH7RDNc0Ho30opcgJyhhjDMlq0V9mkEr5YOwSyDqzS7LYDC/jpWhYs2MoS+KH9CHtVEEfNeCxj0Grz15REq/0wIi0U0dIF9TyS6iwnCLt42J0A/Slb1oIlqkek6bNTNkHkorlHpPjgL7Gy74TpYyFNQjNiiUpY5LjVto1iiX1EFg224C6q0wfV/0uwj6lD9J4LU5iPEc5zhfYv0hTkfXThyh8fuqcAOvGdKFyjPTS/tdSkIjLRurjTBVN9azknXr5tI6i6pthm9CHzcletMFng84sh31BExpq3gRjONp2pExnlOgDFGhXcoz/8mwPyXg4GqaPKy2uNyQ0w5n0k0f68uk8OmzAW5MhwkHxg1qG9ZfO00fXxdwyfZcabQOtNFvPkQUas/r2swHSCa4uVl+/t4NeND7Mu8D4RDPa1RN81OsaPMmVFmycAAXyinKq+MYXooyEfEQtVM90NdpXyaPsJeXQo7Wt2E+0buacvxvlQIw+QwldlC+tb1nOky7mZQM5lCXzVdin9RpfzTNDGaPsFIMkiz7C3CRuXHgPv//7v48LO38WX/nq1/BlXELbxBm8P1zCfx3fjr6+dfjNf/h19PWE0JNbQiSboq8UwkRLv/XvnsoS7T51qU/r5clXpP3I0jZl5mnHl1ClH4tYH12pVnsQGi/Oo0h9nk92mh0oyzGMUk+EtJ6dbBJ9HPob+tiD7KyPguhl/6nS53GalHZVs7t1je0Z8Kn/xNnXqSMyw+z/OaTpD+c8MeodjX3o641BFDRQzKIo6s4sRgV7jCn1oMSxqg7Inoiz9GycE/dx0OtOikcGXCLl9rronL1DfuMVVoIbHxVnNUYGd/WitbcPXT3d6GmNoovKI0GHMOSn8mDbSEDoCZijF6SAB4Ny8OTw0wmhkFOvMQ0ZHIlSXlrR0RlFe0cYkdaEzZjRVFc56AE2qBw0D/PxhyMIaZFcMqCnp8tGV1tatDAilToNlJwVoZ/7cmo8RgjLYofUOdHu8VOIJLwahCNX9Nqk1o5xPy/9wfo34acTJPOSOilxqVc6p3Ql5CAoGJCiUFAVbu9CvKsHHd1d9hRJrz7qyW6QsqUvwNXCcURb2myBzZYWOrNxfY48wACZW/YDDUTRU6DS87LfBHlGQYk6BsvUZ6/ri4VL15hiJz1ymGXINdCr/pNHFJVAKyJxGveoF23xMLpa2J9ibQizH3kZkHqpfD1Clmf9iEqypa3dnjp3dHUyqEmgJUKHyF+xQS8tMq2QSKrS+h7/9EqkHB1mYqhWcFI14fEHmUTXLN6BRj0oGbBhCT2+0dev6IAE6EgGqFu1WLgGqEwWdBNRg2VBOpn+YAtCcerpjm7aih709nXarMVohE4AEyk0s3y542W2QebttwPaGW0pa/Y6AvW0L0iJZF/Q+Rqv2yvvTCI9XvE4X69T8BzmcVj9hzR6tWaLh30uFEUkwZCyoxUt7a1IxFsQCenz03rFz1nMXIGQgupQC/tEZz+6mC6mxdxZP3Y8OmyyT21IdLC/dztrLyWirAsdF30VVXpC/VRaQ0/nrUVIu1SG9IjcDyvIKeyegWOh5bkoY/VaIfdVMKMZDzHIfq9XFGnp7Jx0jH0iyCvnU5SGuKVdJE/FB63p6WU7i++qhoy/n9cDtJ3RNuq6nk509dH20/53sp3ET/uipmv3I2zf9g608fqG7k70t7ego0UfxdGCx9Sk5Je+BKtF220AhcVUNOCkoIh8DPJaiMFIwMs2o06qasZ2tAXx1l50dwygryuEroQXrSwuwrro1Vof9aWP9t1vPGeraKCLDrM+PU62UseKH46g6VU/DbbpQVVA5dBvMTkmLZI50392jS1D1ICXxEBtItk0/cyyPbxPbaTzwUAYcfpGHZL17l62TR9a2+OIS+9TjuQ8+8UL0qSBOvkqcvx1vw3EsC2qGpBm8MFUrDb5xfaIUaBbWyL0kbpNp9eop8vkneoQC7GNE902o6SjM45EhHYmELGybHzPkPUhShwcf490Cxu6vHtOpyRJ4se9g+VcnXZlH/fRBvnUJuy8dLvZXyo2Y7HM9vBqYDQWtcE2fXylhTY0HGNwG6EtY70kr9bPKBtiqaaG1CibThkK4GvUAfQVpRPYpiW1MWVEAbSW6VAflzxriY0ofcoY84+1dSCeaAFdWbap5IaBr77cSr+Qomc2WIVVZUNlh2uyy5QPfZ2OeaottbyF0go1CKcBL/kLCtHYrcz/9PIeC/yZj+ripf8bpk/bxb7SS3ucSMQQJL/9+mgCW4YlWGDHrAluOypgcdrT+qehHTpo14RNaAS3pZw2M8ExlParUnfUqN/9NCjBAPlF2yR1JjumhyEa3KnpFR+9Ek9916FX/hKU03Ar08cpGtRP1F/q3xH6UiHKhTJQ/5O8hGlnYpEEYu3daO3q4/0BtMWYluXZRytIkod6LiC+U55MD1NOjEYNGLND6uMpQfpzkWgCUebT0r0ebb0D6KZuTbBMrxHM2lEPBWLtSLR3opt6srsjgDiD8zBlT3rxjpzU/TcTLqFiJsVDqhf1rwYpRJiCcLUD66gvIttSGcSWhI8+rerL+pEuzWKR7ZCJEZ0B9kuzIayXXAYt+B+k0pTe89Jv8NKPDcVlT2lLaSMS7W3s9wzkQ+x39VnTkv2qvmwnexCKIUHftrOjHT2d3FK3xuRHmA2jHmZ7aeJClDq4vZO+RlcUna0+6k+WS1+ErUx62C+oNyqyQRpodpWgFJ6jLJ3jJqwR1KryeGQHpcEZK0k/U3b0gKaV/pJ8hG7G6/rQjxa7lwzQa2Sby8egHmcnC5DfYerCSFyynUCc/O1qo42nfMXZl2TrFInZjHHuawDXR32sriP/QAPZtZrSMO8g7QptbsRkVB9+6MTE+VO49MaPcOyd9/HKsXM4fukaapUMDh7Yjr7uNkQp175QHN7WbvottKfREFqoyKM8F/JrENrxUcwu8nyEtqKd9rijtcuW1dBjFYo0/YEYbVWHzaxs642hrSOERMzP/kHa9XCVGGT7BNlP/aRfH3TwajwCmhVOG4cIrxHpxwTYTvbRDdZPvkYt3goP6WvpWWeL4nd20R9KsCXDWm+X7UhRNj/Qo1Ev2QjKsj0lEdHa1v1Coc4vX7s/oNwfEXAawKm8jrinkTsh912UYdCvjX9LcUmQeUZcL3hbUdD7rxRAOarhagadxXm0FxfJNj1VZLpqnGnJJCotXyBFZaiF5qMo16jQCnQi83Rwyl4kyeqkOZIkhpsSBVqfG5UhaqlUEatU6J8rP4o1FVeNAmIDD2SsPgtK2WE5ulwmm7XOTBn2UIHnLEIiLR4tSO4rUsmxW3piNntHz9/8tZzjCFJZawBBu4Z2L/FjYGUS9/4mPN4g5Vqm+hH6pcwk05QtffJcoS00c5G46Itj0R+nAdXYVQGhmoNaK6HiaWHfSFhw5zEFU6Vcl1Cy2WJUeOYNVS1PDaj5y3RISuxbvDevWSw8S5eev3o6RYPCvmCzGCtEzTLgT4X9JJfYg7ZdL2HL7l70dQLtgQraKIUJPWaTB8Ky9IVGm4GikijcJfbZMmnSwIGeNsoJkdKOVXPsy6wj8y0rwKVOCLFsbtRbbE0d18gZZXW90YTHGxxNTz6aXpUidsICA+6YNSCfTS+K/x7qZx+R4uAMyEpbO7fbZR6EqIP9eoJXa6GstVGeqPt5vuor0PlN0SFO0khT/5adJ+zS187DV8dgM3RlLwhQ5ukO8FSUdqfMTEvU4wUWUGLfrFG/B+lnBYqaPdNG+WyjTGrKfAkh2Q3Rq8df9U+T1+hYVcJ2yHJ0kbJdpmNeYR/TNH29uklfIefpRN5P54d0BEiPBrtLtFEFeu4p0pVm36gxgFCF1V/ipRyi5azZEz1pD5TZd+yVJNKvwQYF59aDaPTUUE4T3zPQGoB+myXDjEUbGSM9VSZ9VQVerK8WrG+hzonIa5NTpBlLWnDft1S37e10QKmv6Fw57UN7qLZTeokGt/4qHTPa7xzrlGFRBbaLR7PLqIsUTEhP1cjvWq2DPI8jRx1T9FRs5neC7RrBEltkjhTrY/PtbNMOlk0BYv4FtlHOx/Ok01OjY1yNIkqdGqE+1czYYpj8p0OJajvJZ6DJ/KLMN07fI6HPh5NXJda9pNV3ytRO1HtlTw4F1rFM9HoypJ16XPWRHqXsaCFrPaWUHHqRk4om3Ro2kXz5mcYZkAnpy55qNlKuz5br1W41jTeYpxykqZPZxiyvSkNQq/CadDQDNXulL1igI8y8ySPNuNNaH/J6fJ4k6dA9ose6DR1clh+mjIbIw1IUvoLaAQyY84j4xTMN7PhJaQZZTwoV1sNX6SFf2I4+yq+nhBaWGyNqgXqb6MaMy9TvZRuscfqpBoY1A1EPQxxwHGbRoCfDmmHmzvS8NyDdwcprZhPbXQNUNTaoJqJpJku0lkWYmGPbpklFiWnV59QgXrY1XX72PfJFokKyaL6g13j9bIcA5UMyV7G3BzTTb5E55KkzwoiUIkhRV6XVFuS9j3JCC0sdQnkzZlJ2mZfW6qsGGPAwsoiS++FanvaVcqwZgNId8j8pJwXKeIF9x6v2JVoLKYiWAJMw9T8NbgXZyBXqiiztqOQoVHHk2Ev9wwozPe+hjqqxPQr0Owu0wUHmH2S9feRzLcR2Ig8C7DFCRy87ZZl+VP8VstYmiPJz5WMYkBYNZrNk2/8MgzVJHQ0aT3wA1SaOjbNd+5O/r57A/kosBhi5MPDVytwBr9aGy5kN0/ineF0jL2uUj1qQ9iLoYyCcIZ+zvDfOeKPF9ImmTHjIV9gswzTlNY8iA1ZKLPsp7UEtSh2XILYgQp5qXpge/mt9Rc1chuSTOks6W33XQ9kPKF6qhng/KaZyqvKCZj9Tq6Lq7WAGej1afVozUHPMrEBb6KOGof5lCX4P7RKyiHqLejxKP5UNIFHhVrM95MepHEqtHbFHWN/XYIT1PIqZr8Q0LFd2hQrNiPZqqhTzkRtLlcH24mnpf71m5tFXj6mbqpRdJqjawxXZKPqbPNbcxDLvsXjOE2e7tiAfoo/p0yxplmN9i38m46xSMYJqnnlJCYge9hVNiNAUiqAsco26VLO8WH6V+ddoO0B/Q28NRcnLEHWuX19Kp572yd8WX0L0I+g8VGh3NBRv/UezsG0mdhPWBupcbC/GOPLWPJS6CvsNJZG2mD/UbXqoZTN8zX9kvE5d6tH7pGXysxLhOdlDzRZjPMPzZfK+QFtWoOBF6Re202RHaMSKNepSGYwi76U4uf6iXqlUmWXyv1htpfZu5/0+5NhxK9EQOjq34OjTX8U3WgPYtTSGxXwAg9EdqGzcjScP9uHI4XWIBcqsBeli36wFumgH4hb3CH20I94i7QNtu2lV1qXqp1IIsb8HWli3EPsfYyf2sRDtSbVEu1FN0Ff1oBSmPg+UEKbMhelYBstxYszRK+xbPg28svOwJLYBfVe0sq/H6TvG4Ffb0L7XKJf0PvlHuxVsZbN1k8YWKQf2HcZqNks/xbTsq+ra6jMaXNEXBqg3PGoz9mRpCKHiSaHj6BGXfYB7D1Izjzyo+k4TuL93GsRRQkQxSYpaPgwbWef1WWfQGCAoJknxKECnKpFNls7XDUS9EqbdevtbXnIU9Etdx62DGt23hTt1s1sYO41AG5uqyXNyIHXWzlE0THkRdavyczIkvUxgU4P1xySi2/J0K+H8N6EJdwG5Sw0SYkJK8eFGirDKwB1Fame988Jk7tRPk3UJowW+dHz4pyeCerfdZiXSKOjpvmYo2CML9S+i9QgKsPLR2lrat2t68haiA6Sn5FTsWgx5/dat+Na3voWvf/0b2LNnLxItVMRWeh3q5bgzCix/BvC0JwZOWnWAel/jvrpEWYNsOi10UhjaCUtfR+dsEz7j4LBbP/UD7tTVK7fSqw5SDTuoa04KSy6bUGGQV6FjYJnwpAZSpOdN31PE7QGGk5ulkRyarhbWC3O0vFOAZFn90Ghwulz9gCUzT7suNHByrbBcw3pOdln3sp+ICEvjohwqsz28xAI03Vx1MpLcepr9EOokc7Q+9OiA6qf2XQbRKRqtAry+/Kd9Bw1Up+W6CevnCNRU1mTLaVmI6Ta2j+kqgnSXZsno+ANNYjyRLvpgWR/4Wy5W+/QbuDX7LRTpvGayoXzdHf7Ll1B5IsGK4WXVzD1vetlO8qzRUKfCpckRAe5LwpQ583ZBZdvGfolOq6nezitrDmpWndBm8kieRD/pk+8jneveqfscP4dligyCJLJE578se1IvRuXpowRaNNuE0upppZJs3ih6JKO6RwPILE8yqAE2axZedurigMp+4GDt65RreoARi6oj2px6WkXNLVTzO3x3UG3iBLO8QLBc9ONWo77vZFXP0L1OQVV+yyC+q821S7Qy9OcUz3Icvuu8gbWvEmrX6f963GMyprwsFwecsuvA07piZdgJgtXfKW/5LM85Nt6haFlW2Djit9pJ9W7I2eCh8PAzAtb6dYa7MqY/yaK1c/2ag/VzdbA+TL5YfEPbYAPZPGdpTLbIR+MlgXImv8te3+cp9XGVpZcP1cftnvqPIyv8tfs1a6YutypfWN9XKpf7OrS+bdfVd/zmHyKoWaya1eToWIc6u7m+re+LPqZxUhGXL8nGUvb4p95gcmsVqOtLt20kp25eLtTbQDKt/mHJ+GPLyLggeRZaNmpPrf2pVnH+9Iqw+kPAZnxLIzBkl3us2J1taVAnQaSpRwa8TMv0NmOONLqhnYYSS1XnNXMDV9EaNO434ScHtWfdN+KPmSTZMq0xqrhIBkkXmUZ21hFwnqr3KV3Ua8KyiY6EE7SR6JHvmpEt/Wugc7xWF0tHp3NHr9/52QeUNugJIBppQd+WLfiVX/1VW+bp13791/BzP/9ztlzEb/3Wb+E3fuPvYO/uTTYrOsD0mnnlFEEKTN/XiSRoz0UDCR9prpQoX0a/Q65+dFim3Fn9qSeW5U8bqyp/2EjWVvbn9DhHrziCrVeSnX7k9CWBrikv2XdbUkn79bytPYj1pARr7A/B8uUHAHda75ECBR5SunqCJEZIMDUO77zj7ICaiaiXwEs8W/IgRwVUlH5lkjANsypXIYPsCUGpDF85a9NHC0yTpcCmGejniHquIt3lYTHKXs5bEGHYy14ePUNPmZAUWFbZHlEyAz3yEF026s99PR3QTBR/lJf1ZT2eZVJ/rRWBShdTxKgl2dH8FZFLtaenCzzFLHx6sspq2OCmZutUW3hV42+aV6AneDz4GHAE1UGDNdzThMcLxFKtAyOJQ4kSUgoiUIohWImb7KXCVaTDNXTzch9lK+QJoernNXvvO2JSLt9HU641fVoypz4UqPnZZ2jQy5Q3vbvOe8v2dIMlBnLsUFr9w/mTMRclphrrGr6qtZSoTKntqFi9yHqCSHZ0w7dzL/b2x7A5kkWvJ4MuptEsiFwIyIeZf0BPr5gn+1GwliV1LIe0OS4FS5GmVCfS4LUcJiuOfdmehBeI0gcCDwp60sdy1bM014MdSRea8DiDBF4oOdC/+M9DoV0yeaARlkdA/asZhlU6mppBqydLevKqWX96apoLFJEnwkfZ8WmFHQ9CtQAxhHA1glA1Tm3bhoKng7IUQ9EfQFWvegXTdDqyCFUitClRm5EUoYz5mL+6YNmvmRAF5qEnWnLXndfxTIi5CTNdSLJIGiv0kPVqkeoiY1P2sS9TuespY6hCeqq0OrUE08dYZga1QBrZkBepCEtkX0nkK2gh2owtK4dS7ikxd9kJzX1mXevtYo1k78DohFOkJu9oVpuzDpr+dFZP29R3uBHeU1DebEcSWqax0xpiHra5Xo9zZr9kyCctnuyQWWIdy74W1qSd1zt4PmhPKUNV6R8Hc94wMuIPjxyjqZvp4HmLtNhajp0lsq31iqLN3GE5mn2qAKZYogPHRtDrWR7NSvBmyMkUannSmYvSh9C8hApLYVo/FRV5G6n4ES+yvcmjoi+DvC9Lkx+Et6JnsAzAPLzDl0MlJD1ZYKDjsN5TaWWFqIllz1kjLymWT+DIsPRohBhlEVF4qqyL1CoxRLq05pUCqyJlpagpiyRPE3FUN60jqtdqS/XrNf888521/P1sW1CeU5Ug0poJVCrQ58mzrjnSSRqZpsTzZa31CLazN86AlHIbSiFIeaNEsWWqpkGFLMr4ItkKasYwW8dmt/O/Qj1dZL/Sk+9cmNtQFZFqDDE9NWb5JkxsjGqUvIipT2pQxsctbY+e9rIfOnM62F7MM0iUHDhCSOSB1tDRQB//DY2gew0yKjSK+lqo7FmV/VF1k+epKV96Yu5YKSVlm/LY74mwnaLs2xHywuG3z1ekXsnb4tMlTxt9vDYe19gEJabXayJa/4oyI6ePjdrKTatmyVAPVKivtHyAeouetns9MaaPMS/qGMqcLH6A+idS43k/uSQjHmAb0i5DT/dJiz7+oNd4pJcsJpJOpCx5tJ6T1l9jOUXWSmC9komqWlKDdjNYpv7RumIsVbO7ShQ2ccEGHyhPXspnzdKzVXwV8lkzSUUny9bbCuIRU6slZL2dmiyHiA7wwGaWm0R9xsGV1QZ5Vcs3omnfumArxjFfRjEPT2mZFU+FPGCsoVkT4lytptlJ7UwbhtefpBwk2fSKa7zkrQdLDHrSWmeL/Vtf+tX6WJIIDXJr9mKVMiMfsUq9SEvDdOQDCRGPpMlaGQi3saRSoEbfjCeDRcquZkbpMYzmf9DPpGGxmVPUx56K1j5M0q7mGHdpDqozOByQ/yb7S3Qop67XLKUC5YgyFqAO0VqsmnXiJTqjzLIFZZvJWxIyN2GtQvmu5KjXHN2upTcCpMNDSqvUizVTtpJBpvOw77F/qn4x3iutKy1bY38VanaJV2tAUo7ZLUijl3IcoN6h3LLOFQZiei1Zlkl9Rx/XKKmvMRflFNCanyQuKDvNWslX1QSvAu8thUrsYgX6AtyyQbU0JQqaAUakPoTqKd0RSnOTpmprJ9nUD6I7ME++kHb6FpWq+rG4wbQs2fSKGKQdYRPWCGSAn74eMe9pJad6Ke+yTQXEidEC/QrG8DnydzEUQFbqinpacYPsObS+NuUo6CHfqFuzzI4Sj1AhjjB5WqKeTwcXUWDM4udFIQUUNKtOWEae0coxlqJPpsFTmxXFPl3wkiQWxrzzLRFU+rqx/uB+7D58EFuf+hw2PfF5bNu6C9s7Qmij3xMt+209Wg/9FgjpY9p4iNBR76RTdpk+qmaLawYj6S16wgwNGfdRZ3iKEcp91EIovYro2AZH9ygOtLzqkNfYCPW7r1JGpEi/lWV6SuxD7CMl0lGm7OsjLzYlmQ6CfIQq4zP5tPYRQO7rNWR7WEL/xBn4dewN73D0oYqTTGtfWN+xX/ecnb9/oCZ4PEDe4mpALtpi7xpNZW2kJJTU2pWtaE/w5KgJ662pX4fdGstkg8vY6IJ+xC/+aeDLQR3xj9cs6Bb36sG+3cB87YmnHGtuy1TsWkRco536u8NIjYA69PDfsGbRibBOr+1wT5Jp9XXK/rTw6e9swuMFjqxInKpSZPw3f0p9w7QcfQcqYD290qwWSZrkymYZUM4cceYZ7ZjcucC+YY/mnXscUZYcS4Yp29avdK/KcW4VqmtY2dYv6/nzPltwnnSUpDCdXXvyoicS9mRA/UM08tjpI+ovKvUO2ExLUVLvWO5VO3JO3cEm/HRAXfC0kQxIKlzJ0NOoZR3OPwPKlIkbUXGbXtGF5qXXZUYbJwdZBybQww05H6av3eJ4XM9OYE+9dE5lMJ1uUUaSeeUjeXbkXWVzhyjKrCynQKfP8l79qVzZD/VnG6QisaLTaCUtTGn3Ko2e0BcrBedJvU4KtKNyVEkBaavvOWU6ux+GhjrdM2jMkwU7ZbtUNFLi1otYb2uXUXoFQbW1U0rnJP0ASFU49Xf0nvGIf9JtmoGq9Tm0rybUzXZeussUFg279CH/5KzJJ1BWVsxycTwjJgnsnEOAUlbs6XHJXvF2vEFeU5DP5K4vYGy3Y0mEaJUsSMfpQp12os2sURrbSs8qP6c8kzMnWR3qN9XPSKb0RSqtHyb9a8pYoHxUniVTG6iNdSA55Fb7ooON487+MvGx1GrRejvpqJ5cYL2L7WatVabQ243c1031hjObJKhnZpfs907+DtzZWw2c++4hqD1EK6kQqWanJDNGd70k9WVtlFbonCXwfL0NHRtVR/tnX5P8qpEMlVrHalNHDrTvpOU5/YnXUjN2TWmd8lWiU6px37nBzdcO9OuUp1kwJi/L1wX1cu3PzcsB924XnKtOStM+VGL2ijf5ajJKEFXLzSO9VP9zr62E1c414Q7caR9r0Pqxs+/sNZyry8Qyz7Qhqv0da8EDySJ5vyy+RPHOZjPzyGTgTjInAVGvIQmltgyVznJ1ZEoxlETA7jEBMCdvOZXJNeWkUi7TxpVMZpz4SSBipCmcM/ane1WQ5eUkccmRpJm06WD5rCYxKA8NyDp90upg/YU7vF8t4MZYd2adqL68rsRE/QmsyHrRyuROn1F6xz+VZlSZxgEjSifVSdUfynavdIWWUTCkAnF8X15QoKgBAb02WWH/VNspE9kPI1zF8ccyZpl2k1GzAlY714Q1AdtXPNQjJ+lIPbBxeKZW1QvZWsZF8k2/qa58TW4kVGIN71NiE3XdJ2nQse3zbzkz2YG6znS4bCx2jah4rzhH684q5tLdylSPK9UPtM5YJByxD8toak9VHyTiTZqNKbI0UEvh4n2qkh5uct/kR2dUYn32oxXn9EldcmSKaUUQ87GtitaPQBkIdahdu8sBxxetHwi0rzSqGOslu+D+6ZKytnitHmM6f7xav88puI4fAB2vPHd/wWnJRxLUwsst5uzXjz/QRBImDdKW9YQySUzxXA4oscErQWitrIo36jxF9utJm9SYBs4ZkFcDRD8zoNB4qawDZJSfYkfG6BPuwTKVlinEKgJkpMbgtYaGRli1toGewhZ9QRNKZwCBeZvio+CZQyApJIEm/KJcTx7keHOP1+2ddU+I+z7mXUJY7/+SIxpIVZkeedC838Si3gzLsPJ4FVhDkiY8RiDVrTU2ApQNaPqfPQ13ZNfLc2Ea13DZS6dFawJQpTON3s0W+KDZIHoiR/mknFYo4yXuK9b3se9oXQZbBExPGOVcSc6ZTmtoCd1ZMz5e0xeepMClVG3JAdJR8Gl9IdLCAEcLp+r5mNbecqbDUM5rSk/D4HNoK3NfPo80kOYXeCoxYph58xSFXU8Y1Ue0eH2R5WsNEvV/DSKU2W9KXpbAOofKGfbTHPsn+ynvrTDYK2tGjYLYJjzGIO3loLvXCMvHdlGGXs6N9K72ZYhlhk2MzcjpCS4lUCskIWu6+YM6VbvFep8QyLXWou80Cryop3M8KVml0GodEVsBxJsj5imGzpNkf5U2hRnpCVrJT2S/YJbOrSxMel/2QQt4Sz69zNtHFOU1b5GyqyeTtooKQespaBFRH2l3MtFsGiGJMNoVAPh5Vc/uY7UCMcczJIU/OX8QSX8UWa8eQapj0D6S3pI9FS/wXg2QyfEKG1oaNVlDm/ykQHVkeka8Mb3DvqvvW3n1FVa2aa3GdrOKZK3+Zba3relnwR3vksdkNIla9mvNEjNNwDx4RrSKXDmu+vNSmVEd8qTWZtEcafJKHidtqDgu2dDQgF9PaNVWmhVBGrL+CNJaO0ezSeu2XmuwmXyQH/BIb1ape8VfP9tXPOQ+/YtgOcT0msXE9FJeWveG4qLZ5LkAdRXTBjRzS7R75eQKJV+SIelatozqq3+i8q1Q3ymFfA0/iZAYamKG1ClZ79STbSMTkEacHk/cnsRq3RytYxZgYh+FoOItkOcFFLxVypVpVJEns2ETJPQVSa3HKP6XNVtIXybzhKGPhoSoo4OalaGZFszTq3U2KJNav64c5jEzcVaHc1Yg8td9H26o41VvyZt6oZ82hhzjNc2MkJOsdd781s5sGwmJ2pl5aCN222wJHtk6JdwXaIJUfeLXPQM1uyujbvurXwvtOmtnfGDf0hpdkmExw9bnkd9JeiQnWo2EV0irQ69IVN42o99kjmnIZ3tgY8rAudfqwvMqQz3ELimjOjrn6oES29KSqoGI1q6a2cJDrVvj9VAPSTZ53jIm/5y3EFSQfEnmQ6IkM1Yu5Ud/VUsjjSPkGRXC+plciqfkmUeC6GXeyl/XWZZ0iKNjlRnP8bz6rVrCWsMqqEYSqgxuHceZ+6rgZxzULHXQ7kp0Wu7OmXqrEcV18ZRIeXHSCOpp1X61CO9nn9VbI5rxR6ZqLqH0jL5IqOtav6rqoX1ytCDP+ak/o7wvRh1JeSQBXl6Hd4msy7CP0s+jPvNRN2t1Ps2+12xYra9TYoxSoc/n9ZZ4T4FyQbr09TbalgD1p1DxkEIpBeda746p6Y/mbZauR7No2HkVF+m9Guk+WjKUtOYRj/WhF+fjMAroy4hQv0dJh70WSF/Oq7sok4b0T22ypJQh02pA3bWnmmFo6zxTe3hsbo78Ysmzj32RloM06sv93irbxWIrR2b1ZV7N8KHGYTs5bxEENbuY8RhVuM1u04xkybxxrqK3dLS2ruZgqs+Qdwr4ubWexOYusR00u06zhryaHcz+WCPPauSPvi4uPV/2xulztFJH8DwrpTI0azxIGvT2j75arMFsrb/mrMHWhLWBWXm2q5/2uYpIiT4DbWaZsUGJNl6zuIuUR81K1OzpkMkMdT3lVl8s1kwtzYotSUYqjPvpOwXpEzj6T3FHmP2D/plmWuu1smCFfKSt5V2ya3LRJP/wM619wIb+J9Hr5/2kySwM5Vr628YHWF6IfSMs/Uy+l0Qn6ah4MrxJ6/AxjRkqzcLKklLKKv0lzZZWX5QVtpiMeppZmFzrIxdS3prl6RhOpqdsmX4ndTaDkXJXJR159lv5KvJ3A7ITykOOlPojjQVJ4S30UQPsa4bsEMw+UPIhxPhO65g6deYtakv6L7YyoGaxsx/Ck3bqWVHbqZ3Vl+poll59Q/Gb6CSarKt/3x9QdR5hcCuu7Z1GEE+EBjrN9tTnNKVIhTUqDZ2X01I1hU30MRC2V6A0Ii8GSVS0ILgCeCYm6qsZFfOaeZ3KVQNiTllS1jxHpUa96bQaJaPik2Op+x3HxJDnbeaL3cl8zXFXEEaQ82LpKDNEWyxXAmu0mFvPTsfqEM2hYAey2TErwT21yqVlUPFN+EyBxFQyKDQZJI9lLGsKpCgvQSpMoZSHg7xujjYVl9KYYZUzK2fKwnbeRUlldkI5roY6p0Om05Rxc3gox/osrq6wB5nMK5HK0KtL9kqIblJx3DjhgpwByrgUnRKqEEVcRjO7hdIrsVJrbjAdCR1q8Wn7CpblJ+UvQyHDZNmb4RCqFn46MUINyqkK5vzwmj0dacJnCsTfD4MkgtBw0XSnSbYD0rd0bw31IYYij805cBPYVi6y3GhJlRMcymE2x1/a3+kWdqMzG4up6Hh4ZLgl40TpccmhBr0qGvyQrNdvc6aTc0ti9OBFjq9XDrwWq2d6BalVb4WOGp0tu0vyreCBdoh7Eme9SsnkBPUroYUDdF98iLJ/R3inyle/KtC5y/tCdJbVE3kzz1cYfFTk/DAIFf06X6ENtJc6dOjiPQKHCwJHazg8cF5eMa9J/V46QUGRBQXSYkqlO1xC1PAasNHQgtpYmsCG653LPKvARzxXSvFNPJJGtIdRTCk9xI3xXG3tI88UXGnxYvFNznDRJ19BQwxy/qR7LDGRNWB7adDSGYAkHeKhpfUzKOIZyogCORvUYLUkMuJTmSheO9flmIpGUaZaqT2cX6GB0UgKpNu4VQsJLW6rJ7GqEO0a0xcYSOXJeT280KK7WphdYqeHE6K7xro6AzuOzrSyeV1ipK+uaU8yoAcb9hoQUV9cClpQoJBUrwnLD9EdrDsdXjm+Uv+SS9FheXLfBv1Y3xoJ0IeEnNdonVpUeE2DWSJeXFY764MSQp12Kqb6s65EcVf9UTmoaipD9VLd7xWwB7E8SZrTuA4d0ht13cH2Eu2+qgZaJQM8q44oIuu0OLWznHQHfx16BXqtVzK1zGkeO22ki7xfaAdCXeevFWyH9ftk93hdhemaMmf5akEb4LKrpM36BKkx+VFatqAVoH1xwYbP+EcaXAIFy2nlDaglPvjnrgXnzBh3yjPO2ECW+h1B7WHnXRToinq/OKmtjl1p+ekD1b4RBY6kuEdu69X/ePChlrKmZf+q6SVkxTNOvCK5CbBtpWMYgTNL6nQ9RKkP0jiyJ/2plwTDFlhbHGzBc5rsYzrJOlFy7reHo5Rp6/MaWHUGk7RkgOTMxF8BO1FlSicaEQyw7fUm5iNZM9+MsZheabbOq3pR59hXu5lrjfbO9dfUTxw51cuUJUObWeqVrym7SpqZhZfKTNndeYgkWkStWsuRL49kmbSazTUbTq3LvKSDJI9e6UmWo7ROz+WxPZBQv5d9cT4XpXhMuZrU8zoLVxX471hl5SB0Oah9x4dgKSzLHrLYcgoF873FG8Wk5puyXvqYVAVRG3BUX1X7Ou0vnavmcOjTR56ETVgbqKUk9dKRGp8J0VfS2I8+8lOlfDoPrUxc2Rso4bKDkn/xlHyTvZTuFv+cvsUrylSDsJR5fUbGHvfICLIjaeJB2WTZWVJDZZqlle/l06xr7jIfE1bLQ7x37LwZY17kFStHr52j7ovIE/RpoFkP7iR+rIe8NU1e0ESHO/JYj8cc8eexo7tVnsV/dl5p9fBP8q4T9b5tA4HO3ARpEP25foyEUHQb7dzXcgM1NoQG0tQ39dBM4yT28IrVkKVyZtjrUZhaVktwaGCuPlgsfSKU7VD/dHqKc81Fs1lCHt4nUFvfU1BAvVb4yLS6JgGw2mvr7t+5x450mkzQp7rD/NMKDB4TNjKP3BJrHRbX3QfeJNRrDbYInZdXKDDGLPsT0yyBkwedQT25EJPNYdE/UVuTC25tIMFhuU4b6kiK31HcTp6NtbCeqYxMogTOVctPh6qYBNkquAJ0i4t1aDxlVCh/58fgzl4THmuwfiEuO2DyKokxWeIJoikuO88/S86T6hNUsnbMZJJPp0/oBuGd+0307NCRWaUX6se2zm4dHEfZ1CVvtIHf+lVHeSrveqb1lPZUkmnUNy1/JXfR4M4J5WX9jKj8hCLV6Xc8a32dyD5mfVvp6nc34fEEZ9q/w/9GTjby9INXuM8D95yj6SUxOumcdfSz5E4oeVxOvJysMYhfBulvk9062H3qV5LM+jwXXbZ8lJHTa5weKJCToZucWxu3BpYf76Es6y7Hnb6TQntO9o6rrT8TdEvCdrKmYgqvHGe5Tab9zUkLcav1n9w18RSc2EMeokO007+dvU8GK233arZcZz5wVmWaoyc95Ogmp3S1o/SH26+VVju8VkcNQln/Zzprc92nW5mYltzQOa7faimYmmU5yBJ0Tfnp4RfP1ROy9Hpb6R7SqIdWzjWXBra50S4+KVf+8ZJOiR02w0kZGTq/kiOnVkpINNC2ERt3yTButav7HS7W8xSPXT6bztOW/0TRztoY3S6dlkyHvCptK85L5k2ueN6yFoFKVz8lpIfMn4a6qI2kXy1fXiOq/fVn7W3Iaw7p/HEydP6Ug5OTeFfvKTxWGodOuyh0il0G915ru/oFa4KGNCthNfn7MLj5OWi2xCi6c68oNFR+blIeq57Ge5635ndO1elXWodi5abTTss49TX7qzpbYoFqQ6jn7bSMrhPsnAMOJ3T9TptaFspORdbTOMvwC5kAAP/0SURBVOVSxkVb/VydMP5za34ur/HwDjKVUOVKd2hGDWm0PqhbdCtzsEav81dBovIxubAaijYRo4TOxkXBB+gQuhcawNH1d8DRC6skfNxgRRXqLbCMArWPYxvUhkLu1w9ddKwC29n0Fi/WkzmXdW1Zo9vl5ex4xdHzak/nHj9/JGXat3R2pwJTagdlb8l1H/u89LT2SZflreQahDF5sJstCzdvR16cv+ULpjt4t+nQOh3kt9L4mH/QF3Lk0M3L/pz+4JSvGxoK0UF9ox+zwUav0JF9oaNfRLU1hKHOO7dJ3kWTtjwkihZbr4/ntfagoXxKy6MOSm9+pra60em1Qpu8wLqq/zCFIVPVQXvKRzQ6NDj9r471vuXUnWmtTGK97rrm1vCzDit1QSN8Ep2glELx3BFsth55Jrb52ejmBbGd1X+WG7mOy32KvPTzPi2LIEbZAu5iM9F8CQqOJFU3qU9YnvwTF+unifX8BfWqOUsqGKcNrdNRpoz7TKqPb5ueZe6y2z7NmlI++ufFgF/z+h3aXW1vWdfliFkvo46XweS20UYQ6+kcieN5XnBI1g5pEl1MUBdFov5Urk4wTV0fLWfYADqly6ZLhCp/OZ17k1MH59fJ3QrT9lPCR8mQCyr5nsPdBHSlQXP3P0woyVLnlxNvqP061kl2hUY6TF6fN+BFAi2GPn+E5yS0zkiuUHe69widRpaw3TkrobVn65JsWyBMZTXm0Ei742yaw8m79IqWxFSpxGZnCUSKrr5coq/a+fVE3nGuVbZloOwMVb6esmrQrp6nHBGbQsy868nvpP8wWtty1xEg57Tb0fRkWs/kPl4cmvBIgwmC+oaQMiPFRImT/OnpmomxRNf9Y3pTPKbJXOnjMbGe1K6bwAh1gqhi3OsKljRI5ShnqkbmpaR3bpOcBw3Zcz50DfoceoD3+qm8vSGm0VKkWtbX+TS2yboKs87E9H63v9cNgXuJqHyFoktofcQfJ23MqS7/Lt0qvwmPNkjvN+r+lceurLt8bwTnHH/rF7UR7x2p0fRqyoYE2UDS4LiosTpa8GaCxC1l1EOUTLbwlHqJ0y94n3k6zFnHQl2wTiWdr+nblD2nYJ5TOvZHbh0K7pRbD12Wk6poE2oZCwUHLNX5fIqf6NglV/6dq1oGW8vX806bL89rpEOkWFiiRVeFTKzLcZ5v5X0xtaEN8oQRIa36Uwkq3KHTIcMIEorkj4HVbPhq4GZpTcM/2/PQNhPv2CmVrnaMWLtb29t5phft5njJNrv5qQV4vwIQ/mtKv+ojdAJD3kLeSm9JHznt6LSlKFBq8H54yTez8TzihRjPyp00LhkfLTFRhZAqe+VQ94pyJy+rgFVC+Ye5K3TqpXqolW3QUbJmN/B+C44c6kwvq7LK1mGk2Gr3KoUFpERdkpg6wZV4SZrqeYrHwqDaQwuTa7Va5qNiPayVl1Id5J/kR3nrmpVZR+Wr8iSvzixgI4aorerNPFV/K89tTf3qLvHNeSVdWdsOeaDlGpwHG5J6Jze1nu5wOOmUuExLPW/loUPHm3L8J5UkR0YP4/UKle6RjjB/R5Wsw0fJoUPdHXSCZYdTLr9ccGqoPsutkos22Rf7EIxSWyKHdqFlqR2XYg0wOq3noOrl7t3RA24T+Mwm0iJaG/NcQ95qR8eSO+1gZdczNpngGaWQ3OnDCCpX6OgDtS/z1JZ5u3ww5L2GlqeuU+sRndfSlouwtKZ/qQP1+qpTLxJWlwmHS6JC55R2mXSi7nZzqreIRz7oh73QD+j8zwLU28KwvvlA+xuq7fXLI8mPIVM23kt0NFvdXrk3c1dtLMkQxxzb4OgOVwgC7PdC45rSE+tccHYkHj5d7+LlVqdoofXpul0jj+VXKm+hh3z3eKlTTIe56R2UTFudnAPSyR/zy6TvRQP7Gm/SoIMCb2cYXNSbJrR7nd4oCrUgt3S08mCGKsz2iaLd2kAF6S4nB6Erbc4sE5WtSrIspuee1cGrPsG+7OhQZSNaHPuz3CmXa0yflsWIBPs4jeTe9K9zUqUIHSsaYdlBsyNCI1P3Wb76crn6qHtO+TlpQtyGeOD08HrZpguYmvSpzRz+8uCnBFxdvpp+X6uuWJYFG+li21J+1ILigdNrhJIbNTLzrt+gKEZY12oOqGyhTtST35FX6nPKd4j8FTqv5Nbvqd+gX1eMZcs0M1gvGkekC33iNUskfQp/JAEOqnfIflOOQyRMYqRYymTVsbuSFy2MZHP92U+VvdBkllunTP6oA5jcyr90PnCh6gpEm7JmKQ7JhrpbVKjfcmN7smyyNrJfLEtp9M6miFZyp6qWXhvJtlA+CCDflPV0idI+0aFdrS2b6eRvZVv5TsErY4LGfeu7RJ1z9xth5bELoq8JTWhCE5rQhPsOqxmnJjw+0ORdE5rQhCY0oQlNaEITHjdoDno1oQlNaEIT7iusZbCkOSDWhCY0QbDWJ/pNePSgybsmNKEJTWjCowj3ZdCrafSa0IQmNKEJTfhsQ9PWN+F+wUrZasra4wNNXjWhCU1oQhMeNbjng16fxNgprZu+aSQfHDTbuglNaMKDhJU6Z7UZXc1ZXo82uPxZzX40bUoTHgQ05ezxA/GsybcmNKEJTZAPtRKb8CDhgbze6Bq8uxm/pkF8MHC39m9CE5rQhAcBjfpHgyjusTugom1z8OvRgLvZika+NaEJDwKa8taEJjShCU14fKFxoKvp4z4saK7p1YQmNKEJTbjv0AxcH30Qj1z8OPioNE1eN6EJTWhCE5rQhCY04VGBR3LQq+kwN6EJTWjCZwMaB1HcbXM212cHmva6CU1oQhOa8NEgO1FdgU1oQhOa8ODgkZ3p5QZKTVwb3ktYLf8mNrGJTfw4XAmN51a7/lHQmG8THwzeS1gt/yY28W54L2G1/Jt4//Fewmr5N/ExRvsjXxtxtXRN/MzhvYTV8m/iZwvvJ9zXQS8R7/f7UalUPlARd92WarX6gYrq2D1XLpeXjx8UNtLSSM/jgGpjYalUMtQ5F3TePVa7e71e2xYKBaunQNeLxaKdc/O8H7iyjYWfJs29xJXluO21GjamddOvFVfe+0nvXwt+FO2fFVytHVfD1e5t4oNBVx9pX7xwdb7A3XevhUIhSyud7+LD4N9HlenWp7FeK1H33w1XS/+ootrftSGyFaLfrbNbH5/PZ+ieE7j3ausef1bQrXcj/iTpmvhhdPu+C64cSvbcdtS+5M7dSj51XumURuddGfys4eMiU6LP5Z22jTRL77v74l8wGKxz27ELjXrGza+JjyfWauRlI9p5bRtxtfvuyLmLq6Vr4uODrk5u7N8u6lzjVjpdusHVFS4oj0Z94mJjOQ8LV9K0Gq5232qodnBxteufFhvz+zR0PUh0aW0Ed9yicd9FQeO+C6rfSrgvg15uQdqKeNcxEcjIRSKRVYkVupVZWakHgSthtTSPKqq9hFIWrjPotqGONfiotleAGQgE7Ly7dfmlNO65B4WC1c5/FvFe1NXlayN/V15fee6nEe9FWzfx02Fj27vy2AjSQ7FYDPF4HNFo1NK4esvVXdJJbh4PElX2an3IPd9I493SroZrTfcooOonW6Bto22Q7RDfWlpajG9uGoHseyPPBI15Pu74WavPo4wuaL+xv7lyKTmUDylfxe1Xbl8Uuvd+lrGxvh91fbVr9xPdtnf5JnTPSz+4+kQ8dH1RbQXSIQ+L7iY+CGzq0J9WdPu0uxU0boXSBS5KJ8jHkK+owXOh7nX1yaOGjfVYDT/ueiO6OtBtq3uF9zq/+4mN9XfbTrZD9l/nXX/z48C9vxE8dFntzvIaMlgLNBKiAS+XUMG///f/Ht/97nexYcMG/ON//I/NgXbTu5V193XvagTfT1itER80DavBJ2Gu0rr7Egy1oxTHyMiItf/o6CheeOEF/Oqv/qrxxc1bWxclVPcC3Lw/rg2V7mHxerVy7zU9H1fWSliZrvH+xmur3duEO7CW9rkffP4ouJflParQ2A6uzOqci3JgBgcH8dZbb2F4eBh/82/+TRw8eND01FrasBHuZXu6eX0UDR+Vxj13L2l6GODS79oPOaGqm2zIqVOncP36dfT09ODrX/86uru7zRHVdfc+3SO4V3bkYcBq/F3JVydNYzrJen33E8PjLTP3GtS2QleGXH6IB9If/+Sf/BPzH7/1rW/hySeftABJoPSr8e6zCK48Pkr1beSZQDTqnHSC9IkbtL788sv4z//5PyOdTuPv/b2/h2984xvG10aftAkPHtbS9iv14OqgfNiHl/dd+GD+Hjix4b2Ae0d7E+4HuLqgEdzBC/V76Yjvfe97eO+99xAOh/GVr3wFzzzzjKVrvO9R5KHo+yi6jP57SPdPmlMjrSt58iiAS5PbrtreunULf/AHf2C+5/PPP4/Dhw/bvuzNWmTCX09zzwe9BCJQKIEWMTJ0Ag26/Mmf/ImdU6AjR8UVep1zCddW0xjd43sBa8lLdAjultY976b7KFhLmrXCJ6HdbUuBG7TIOZyYmMCPfvQjzMzMYN++ffjyl7+8nMZ1FF1eNDotDxPWUu9GuJdtfjdoLOOT0teEJjwIGX2Y8FF9wq27XqMeHx/HlStXMD09jWeffRY7duxY1kPKw91+HNzL9vy48ly6XHD33fsaj1fm9ZPQeS/ruBZorI9sgjsYOTk5iWvXrmFsbAytra14+umn0dHR8SF7If4+ysHrSt6sBitpX/2eD06/Z6r6tgE+vigHamtNeG/gUeSN229Em0ufZKvRLxHm83n8/u//vgVGCoq2bdu2PDCr6/I33XseR1iLfK4VHkYbuIPgjeDyQ3pB9Tt58iRef/115HI5C24/97nPGV/de4VraYeHUb/PMtw72WvUjS6PGnjlFlNTbPjhMhv5+rj3hyY4IN28sv11LJT+VswvvSC/UMdPPPEEdu7cuawzpEMEK+VhNZ4+aD6vSVfp55OK8l2qce96xKPZVoKVPFes8OMf/xh79uwxm6GHXV1dXct+wcfBfR/0ErEitLGCf/RHf2QjdQp4JNCaoq50K4VZW/dp8b2ARho+Du6WtvH8WoTErdNPCmul3WV6I22iQccKUCQwUibJZBLr16/HoUOHkM1mbQ0vKRjX2XDv+Tj4JG3qwv3K916AS9tq5a+F7o+Cj5KdldfuVv+flIaVsNZ2vtfl3gtYK+1rgQddv0exPe8lrKaHBOKZyzfpnKWlJczOzpo+2rJlC3p7e+0eN90n0f/3qk0/Tq50fbWyPu6+u8Fa6b5X9VsLSP+rPuKjW193EEG80kMT8U7ndu3atTxbu5Ff2teAhGZuPEja1wJr5dXa0qlu96Z+teagl7W5K3NCVwZdX0oyJ19FAyVvvPGGDcZqsFyOr9K7sts4cPI4wt0c+E9SH1d+3bZ7EOCWKfpX0qpjXddrS9oODQ3ZALoGyKVHFMikUim75t7r5vdR8Ljy+FGFtbT5WtJo0MvhzB3+2F2eFfxqGPRaTWYEKu9eykJTZh4ONOoFl6eufpJeF2g2jyZoKO3AwAA6OzvtvK4rve5fC/8epN4TNOrslfS5sluvuf3egQ/X5c6Zu9dzZTf6tPCg+8Ja+rFANlxtKl9SvNSxZgXrLQO9qfbzP//zOHLkCNrb2y2dK1sflf99H/QSuEIq51dEa5bXH//xH9tgy8/+7M/aTC+3Um56gVvZBw1u+as1nHtO9VmLoKwlzVphNXpWgtpM6dSWbnq3XROJhA166dVSbTUtUDO91MbihSs0Si/U/sfBWmi6WxusPP9Rea2lHBc+SZu7+eqexvt0vrHMj6vDWuhrLGsl3O3aR93zIKGx/LXU9UHAvaTjQbfvw+bn/QbpDreO7lb8Ero6SoMnt2/fNgdncXERR48exfbt2y2t7nH1j578fRzcy/b8tHL1ae9bC+33sn5rAbW9bLXqJFvg2mEFpxqk1Ovx8/PzNtglO9LW1mbpZOMF7n0KbtfCv0cV1mIDFditBdbGw7WUd+/gQcvVp4FGOdRWg1xC+Sy/93u/Z9c1S1SDJhpklay6/qTwcajjauDK3lrpd9OtpocedBuIBtHf2P46p32dl14QD9955x28/fbbpje+8IUv4MUXX7RBL+mMj6pPE+4v3LM2t6jclb07Mmi524/Ocac+6LWanDbKwVroWi2PlbCWNE24P+DqhUZ+uvzQoJauaabXpUuXTLdryQsNhmvf1emC1WRhJV8fNJ8/Smcv11VybnuNoDMrz7r1u3PtTgpnz1v7yfyFh9kP1tKXZcfFd6Fm+mmrsQs97Dpw4AC++tWv2kwv900DoVunu+V/3wa9Ggt2BVVEa/sf/+N/xF/+5V/aCO4/+2f/bPkpsdAlVFtVwHW2m7A2UPu6jHfb0m1/zahTsPJv/s2/sWDzm9/8Jv7O3/k7JkhyIAW6V/e5+HHg8vmjYC1pGmEt5X4crLVMtyw3vbvVebXFWmEt5SnPleUIXBoar98LcPP9KPhJy2ssY61tcK/gcWurnyZYKcvuvvqUq2Okcy5evIhXX33V1vT6lV/5FXz+8583x0eDK64uu5cysxZYSfta4G7pP472T1PWgwDXZog2bQWy09rXUzYFqnJKtZbXL/7iL2Lr1q1WF9lrbWVTFLgKZfcfV2jk3915/MHzzlH93Cdm7YMd9HqUwe0bLg9cOZR+EOqJ79/9u3/XHuZpbVK94ii50wwwDX5pYMWV4c8SNNanUT5Xwlpk936Cy7/GffdYOkEfMPkv/+W/2Cuq4tk//If/0JY70QMQ6X35q9o2Y4DHGcjz5YcCCvcJq4iss6bX6rL8MGS3CfcHpAeEri53dZSrp90xAo0P6LVnHX/ta1+zAXHpdqXR1r1P8CjJh0vXajQt15WXPnxVZ+6cVdrlvNzfD+SpfrW2QS+XFjc/dyt4mG3XSMfdQGmk/12+C/Sm2u/8zu+gr68PL7300vKgl9LKXrhwt/zv+6CXQI6viHGJ1quNmm2kKeka9JLTIgJXMsCtwINmzN3KW3l+rUx7kCAaVaZbro5dVPtr4eh/9a/+lc2u0Cy73/zN37R2bqzbary4G6wl3VrS3Mt2WivtgtXaSaA2WdkuLnxaWt28GssRKL+75dlI31rgk9K21nxXg0/bDvcK1kL7Wuvn6pqfFO4Xnx43cNtB9VzZJm5bK7jRoJe7kP0v/MIv2FRl2QPXwXkU2nMlDXejaeV50bQaXY8b71Uv2XANNGj/5s2bNuh1/vx5ex31137t17Bu3Trja+Ogl0AO7ONW37vB3fi+PJthlcuU4Poek90lqGsEjzyxJiyD2+aSIdf51b5kTQMlv/7rv26vNvztv/23bbaXBlJ0TWkks5LDx13+Vspd4/Hd6vaw6+zyqZF/AukDofgifv7FX/wF/vAP/9AGMH/rt34Lv/RLv7SsM8Q/bV1d0oRHCz4olh+UUfdY+q9WIz/rR40q0Hbd49qHB71WyvDKfvCTwMq8m/DgQG2/kpfq8zqnvq79P/3TP8Urr7xis0H1kRINbuhBhmC1+11Yef5h8NmloZEWlw5tKzy9fGmZPJ1oSC/0uDGJ9SLbLkM9Ay8+XjeKDqHKbsSVbfUogkunS79sgl6H/5/+p//JHrjqTbWnnnrq0Rr0UsGNRkxCrYXs9XUGLU73T//pP7W1pnTdrZhbycYKPEhwaW+ExnMuncKPg7WkuZfg0rayDjpWe+op/b/7d//OBr301S0NejXWZeV99wI+Ls973UafpA6N9XZRoLYSSnZXgnvPp2mzxjIaQXmt1g6rleHur5b+fkBj2Wul8VGBtdL0oNrShQdd3oOGlTK6kg86r0BHAyf6sIbWdtGsDT210Ywige5Zazvdr/Z06W6k/6Po+jg6Vru+sm3uBverjquBaHJR5UoPuvpQvHIHvfS0TTP05IBoUExpV9L5IOm+n3B3Pn3YRrDl6nuE+u7a2uHB+jyPIm/cdhZtru/oQqNc6jW4v//3/745vBosee6552zQS9fcQVrd+yjW8ZOA2x4urDxeCY31fVh1F40q26XVpUPHGuxSHKD9//pf/yv+w3/4D8hkMvgH/+Af4Jd/+ZeX7xVo+7Dq0ISPhzp7CavJpM7VZwo3zIY1btZZ6u7XqgreP8jn+8n3pkw9HGjs242g85ITVy98+9vfNr9Qs3U1OUOvPWtfYPJEuNv4gO534WHw2S3/bnRoCHj50vJpnWhIX9+6YP5EQ36uf+Hz+Jj2o+uo9hItokFttrJNXDofRlt9HLj2Xyg69QaIJu789m//tvmcGgzV8hqNrze6cLf6uINe99XTEiEiuLHBdewKr8Bt+LsxQOfvJTLHD6D91SQcEskSyy+RiKoJqKYjemoVHpaZVAqc54hlYsVFZWMk1/PkOYqZTqwJVqPx0+BqjHav3QG1u56aVvnLuvCoVtUUcq29UiTdBda5hDJP1Sy/MlMR2RCeCutFLPB8nljyFNkWRUmnXWOG3Gd5vKb2KdDYsVWde9WGbNca0+takfJQFvI6S2M+LF9YZvuXyqgwT5VTJCpr1c1TrSPzgqfAO4tse5ZFRK1IOgvcsgzrLGoP0lbJ8h7RJzqUJsN78ygxnwIrn6sUeJfqwcCO2XhZDlMa36tMoy9q1ZhXxVMh3WwHEuMp8Xw5ywTMi3e7T7OcNqpafQpMy1ooJ+ZRYX6qI7fsbRVijfte0sGWRK3Mu5msanSoXlrTgvVmNcukQzKmKkoi9VcjrWXm51G5ypvllJlfiXslJiySbmcAm9cpt54q24RpS8xHWKnqdVaWI3pYN9XX6sV7S/xjbrxTNIj3KkPtR96wW4j/FeZdJg0VMZztLeRZNgDpZf7imaTJ7rX7uc+8nb6VZZk5ZNk+aeYhKnWtShmskk5LX+ezWs/6Vz0ny0NiUhLNBZaVQ4FlF0Q3y65QvpblUQwkqCZF1kMyqTa16fYsVwVXWReJfsXkuMTWp1zwV3UTJQXxs0T5oWypdXmF7erQx5vIH4e2EnlWYr3KzMPVC8uyqhQ8b9t6O6wVGvv244SCRl3UuL8ynba6rq1rtNxrq+mz1cDN716jC6Z7GpFy4KUg1ozf6kc8rtG+mVyoI5PX6ncV6RvqWt4j+ZVI6nKJ8lmiTKrnOnrqDrI2TqEfALWP6nn/6tqIVmK9rgKdc/cVtLrOiAuubXfPNV5bmfejgPwxHWEMcf7JC+kKbZmGfHH8gfpF6SXyskqeFsgLWhnqoRT7snSDq4fZRvWMsh4vckRaUuoVcZ5/UvyUj5oEgMcVXi8RnTIlS1XeJ5sn0piXZrpUWK7smnQTM5eOq2sSZcF/lUmU6uVF6XkPbYrs+FpgZbs8CuiC9iVH7rZRptzj1a7rWPLoyqSOHxiyfHF3uRaUC9l+B7Uv5FXDehqB9nVO8mgyqXTioew285VeEcMtmTwA6RTmKV+pSJvHPpllXYUq30kr6XCzXkHnfca7QeO1xnhA4PLQTeMerwUay27iT44rYbXzPEMmUdqE8mnkmxnPJHnSW/Rta9KWlE/KbI26rsYgvUY9KNGmqqJO89HjcvxF+a3yty1LKVHqVnrn1G3s35J/+fWeNK9k6JepB4gI5l9KsxvkkWca9RhLyvxcrBPkoAuqy8dgY3s08d7gR/Vnt++76J4TuMcrz68Gjgw62JjfT4Qr/kjJspw4uLyhrLNcCpuDooe/8gVp49UX5BV4KfXeag4+rXNOQc5Ta6sPSHh9jCm8tAHyL4U5ntNdoH/p5b7FsvQHnDhR9oEZaACCMWSN2xJ9BrMN8gXK9FlYbsXL/kI6zI4Ync5f1ermwKr1vk+4Vmjkv9A91uCou+9CY9q1gBNp3AdwCZCT7BLqEueOQLrg7q+szFor8clAed4NKTRVuqsUVDkQ0ucWslC4JGAK06VwGXczmHacZcfR4AFpFb12n517+GD0yMEnqG2tXuoYcp7UQdXeuk7nnRaEaWg6FNDZHdzVeVkopdFuWcMNGjLRITsULVhNozNMos5XLWmwpIZMqYAcyynrGu9VYCBrp4GqEjtgQe3HW5yBGmegRYM9HqUnatBG3Vp3WBurfO0I1dF5tcKr6u9Cs6Q0gqqHBvGqDBoK+SSVBA2jgghTDAWUi4tIpWYwOjGFmYUlLGSTyJZzDERVDwUwzIttYrGJ2ofHUg4a9BL3jblGEIOLSpqYt7Y0OZWwEFWbAn81+EViHNnhOQ2eSapKPC7yvnIpRTrTNuglhWQKiiqwzLqouvJ/VZQGvso8UVU+9AqcP15RO7CNdV5BtMpTECXUwKxJonjHelkanhc6HGTbsc75IrEgL8RJqhw0OGf3Kn8pbNVBgbxlbP9KRQpUP94kGeGRnBvxTWXojPhgA6pqU0NdyVn5eabXXoV8UdMpV2ewT3nyUEU7G4fH/KlqxyI/pqzkkGf7F9hWkqMi26dkEiN6RKTDE9oQ2gPVhmZHVVIbii6lEX+5EbfKzMVB8o1p1LfVxx250qCXrlAGxBSSqLYQ3Za/cZsyZPc7NBvxQjtTbyPda+d+usHVSUI3QNVgSiOstAOPFJiMUl9QX6pXWT8wQSUa3ylfGiQp5lAh5guUJ4qAxNcuS264J4lnRg1oqmd5/2GBa6eF4o17TtBot1274tp297zATf9Igug0dOgX1WKdeqrOUCPZr1s/6UAy09GhrJZsEmo53pQhn+kr6CFNHcvFCpbKFWTNDojnzE35UJl4pFSo56VDChSGIk+byJAO/Ul7STNbudKbZnc1qJFnmbreSGMDSAkpIwWGDDYdy/p4git37v5qoPPurIBGeRTommZ5CRrPPwhQaS7e2RO3VuIqsHwzf4xuSY98UdlI8l2iYPu0MpI50zn01xg4Vems6CFkjqhgS/9uVo8K3I0XLg8b+e7Cg+ZfE9YOTvwgP7HOI24kq86OZJOhPP3qCrclCnCBp0rUU9Wql7648wBAQ2JFhp8aDijQyS3L4TJnj4mpX5VCgbyZW+k2ZHhbznRgkbJRzCWRnBvH9NQEJuYWkMwV2DcUOzi2VdRoqx6n/SY8eqA+3tjPXX3gnm/U79qupiceBIiCOhUipOGMix8+49DNesh/kIGmDNtAsAaEy7TTOco4O0aaNj5LmZXoOw9OeQ91fJn9x2Ib9gQNFns1ICafhX6nRca2la9Zz56XKib7zkNXdRxddwa97tidOlX2Z/CA29Pl58eBy2c3vXu88rygUSYa9+9W1n0b9LoXoArcK3Tz+0io6TUOx8HgAcVNQsZ9Ck1FgyaFDLKZNJaSWaSzDHJ52Z4qMPVy1mxo56n92mAlnZ8WPy2Yo2TogLLy+pw6OQaMQX+5iFw2i1Qy7QySELw1PblRB2VKNRrTytBVi2ncvnUbY2PTmFU7MU2BwZM6pQYabCSbjpqNWqt0pyDnX84sUeToiY8GQby8p8qGlok1315/yky9XfRRaWjGlwbxdLVKhTI/O4nrN4Yws5BEtkQ+aXAks4jFkWFcPX0SP3j7fZy6NozJ26NYHB/H1NgkxiYXkcyyFPLayvCaSrGgRANXfikUDQiZPPhZrurEGrDYsgJdL/cVxPOEJeG9+le1K+xmrDUTplFOTSI1OYLxW7cwNj6NFNsip0SGDIeJqqde2fapbCl+zRohDaqhWs3rZfm85gwque1Qho+0+6nk/EwjPWf1cGpBNHKcabGU0UJqCdMjQxgZGsR8voI0HWvRrSBN6VSaBtuMGhUstjCB0cHyjD8so6oFFY0Ena8ymVPjCp0XobqSUPrH2ouXfTwIMgdzaiQPosnrcwaVLKFKNwp4yDZhOg18aVqDHP75xXnMzs0hncqhxOixRKdJ523QTAJsbakW98DPw1pVTljG0hUlS2pXH5E81iwMNSPDJf6QevJPJAS01ERAwZWG+NSnyVs9seQ1NZDa2csbfeI3TwmM72oTkWAn64lFA390tFZYrY8/LnivYLW8HzS64BpQiaj6szqE1+ME2DYgK5nSYFgpjczSLMbHJzA0NIzrQ7cwPTePdKZAPSo5Yr7L6zEoT1cq3O0HQRQs4wra7gd+FHzc9ZWwMu9HAfkjyupbB+pnPgDyAZY5Ur9PaWgauU99lMsgtZDC1KTD6/HJMdyeoN3jfiqVoRzQKS3mKAtLmJ2ax+Iidb/fhwL1dJn2tEa7JX3qoy6XzvHb01yWKX3H87IlpkmpVx39TX3DX6osEndHHmV/9AE0pZeOkXyuVu/HAe8lrJb//UQr034bwYTF2W3YF+fMzNX3mcEdT5wXzI5RTmrFLLILi5idXsRMqowk9YceVpnBlS2izaQzQG1COeJ9dyyMm3Nd3zxAXA0az98tzaeFxrKb+JPjWkC6x9U/dgd3K5RZYZm+ajabxPz0FEYZA0xPzWFybAJzM3NIZQvIUWZL9oGTIgK0mZLx5Pws5mbnsJTKIl+UvmNnkHwzlUILzQKr1qQnvQh687xnEVO3J3Dm9CW8fewEzl64iInpORSKefM5jT79uXTy/079PgYb2qKJ9w4fNKxGw6fBRtn4cC1WPy+Zs5lUku+6/AmqjEWLuTSSiwuYpJ9we3gEo6MzmJlLoUhfoVbNoZhPYX5mFpNTM7T9JZtIYL6I8hFNNPj0FJhnna564XpLyc+gxZlZyZN12+DQp5m1okuug3wJ1w/VSWXLvQeIDxt8bJb/QTv/3//BNvcUVEGN1rpPjM+cOWNrS+k9zOeff355gTpBY4Pcj4a5k2ddApfhzrECXy9CpJduhAJsBsten0YDiigvzSA1cxvXb47i/M155IoetLS2msMZpJNqo7DmjGhqovJ0A5uHB67S15NRfWb+2LH3sLi0iB07duGpp44a8zVgpA5jAxpsiyorVKppAEDCkQTKOTr3aQwNj+P6yAiyTNPV2Q4vA72Qz8806jWaUZWCtzyL8vwo/vB3f4Tz1yYwH2tFoacbnqAPHRo0YPsGSmUEGRAEvBWNKXArp00DMSowgAqJqnoLVACaSVVApBJlvl7kgh4UaCv1fChQKzmOXiWNUllTnhOoeJkOOaRnr+Pksbfxf3z/BMbnM4i2hRCMFlC8cQq3/+LbeO0vv4t/PdeF2WAHuodOInX+FE6eG8OpcdYl2oW+PskrnUsbxFJ4WkCwwrpVmYeP7cmox+uJsnVjKHuCKCotSddCxBpgDxLDbL+AN8h6+FD0+JHU0y3uhxfPwHvlVdx65zW8+vYFnBtOIrtpL/xtAbRUMwgzGAID6UIgbK+6RHIF+P1F+Nm+Xmhaq6aChymbbEk9DfNV2f5V7peJzsCcr6zgKABPxce2pNIMENnGVZAeimioWqE4Z7Fw+QzOfu87eO/4GYz3HIG/L4J1fjotBbZh1Y+CL2R1LSGNIBnlIW+KRQZy1STrloWf9anUWpDP+xFgHTVV10+eer1Mwz5QZltVKHclBnVltqNHNDBNoUD+k5o4+ezzkk7JHOtV4b4GnXzWd/K8J8t2zcFPhR9ie1LU2LgZZDKzePv9E7hyZQTppRDCvm60hL1oCeWYf55yGGVZWnibip7tEfBlSNdttuEUZtPtbD/yTmMVbBsFCgHKVyAfpGwFSCvpofwHSVOIdfF40iiynUvkd4281vhe1c82lhyWC/Cxrfw88JPXAbZZoOy0QyFI0RXLyTfNz3Cm9zv36zXan1ZwdbDez9fnh7WI/dLSEvbv34/169cvz9JotAWPGlD7UB4kIVo3iApMfd9khYxPXkRm9DTOnTyN77x8Cj94/xjeu3gCqVIG3lIL7USMjkmAekGyL30om+GCU1+n7s7rPx9qgwfcJCpf9lv2Q1vZEH39d3Z21tZf06ejW1palulcSfOH6H8kQDTVUf9EaRydsUElO5Ilr/NAg++8WCGvZXVMk2bHkZ4axfsnRvHuqes4cfkczg2ewrmr5zBGuxeiy9DlT1MfLODG1dt45dWbmMqUkdjZjQr1eYuHdom6jeqAuUXZtj7ESh7eR+tG21f2s0wpGeqVGvUSJYZEUvJKXviL1MW0vdL90s9l2UuKofNKj5/6RY8TlPPjDWp7+S6uDJnTT9Bxif7Dd77zHfMfpTs2bNhgCx8LXF/zQYPMlih1qHWk6c5WekI2QDwSku9EqxG35nvpYRvRoxkB3gXUqDMyQ0MYPPY+jl8YxolaD2r0u7bGF2gjNfs4QlsUoVvhRZg2JqwHMLKzypPywp7LPLX/4Nujsd837gtc/ly+fNniAdmCo0ePYt++faZjlN69Z+W9TXh48EFecF82irJlyzjQ9JX88tcY0C+M4ib14LvHjuHY8QkMXh/F+LUzSE7RbpQCmA+2oxasUj/OUWZzmB26hsun3sXVkUnMFCP08eLoiEtO/OwP7NMBSjL9shL9ugr1YxSnEVi8hu//YAR/9Odv4/Wzl5CsltDR24n+9oTjj9FeKaYxkN7g7vLxR8EakjTh/oDkSzpeX4bW2qH6eqM+eLd582bzC11b8DB1Aims77kgWoj81xWHRm3l10kH8yzjMk0ikUeR01tGQ1fx/qlT+O4bJ/GXb57C2fNzyKWDWJfIoDUwjamJYbx37CIu3xhHsKMT4VgEUb+P3YA+gZboqWhSgx/ZEvNnTCbfzKsn+1SrejBWKpftQbyIKjGWrBAt8lY3oH3RkhyizWuzxxQj8fDBm4hPDGpb+Z/vvfeefd1XcqGPKLlf+nVhpXw0Hv///sf/0bYPpboPV3gdgXCQ0CDHklU9tXdGVjUmWkWxVMT1q1fwJ//pT/Av/sW/wL/8l/8Sf/THf4x3330X2RzTm1xX6oIu5eq6zY8mNNT8rlCvioEckcnJSRsw+/73v4/Tp0/XrzCcp8OiNSWsEcVPCqDa7uTJE/b0O5/Po8TMChRYpeVFJ6kcVA2IlEsoFNgJdZ2OrPuVJnVSP42eDBijTOirxlr6ykriVq8vLjFo1tff/vN/+c948823MD83RztMBzAWpxO8EU888YQtttzW1mr5Xrt6DW+/9TbGxsbta09f+5kX8NWvfQVPP/00du3axaB7AO3tLaZQ8sU88gUNolCxqEORVslr0Bd0aKp7rDKkPi8VEo3y8mCGnmLREa3w3lKRCo/n/VRKzswfsE1yFvDfGr6F0bExW8jVhIj5sPdS4lhP/jAXeDTdSG2mE9oSlVSvSy2f13RwEuMhjSrX6OVp+dlOYE3a+cdD0skiRB/bo5jLY3T0Nq5cvYrFpSUbkBI/AuRNNOinY60BL9VZIRf/mGcoFCSG2RwarFL9jeWOPKl869PqO6KfTgv/iiSPzQBNhvEzgItHYwgHwyyPF2zxOPsnbzUDi7+UGeWlGWmi3nK3bJmKMqKAJ53RjEPKFuktlipw3tCsmKEUT1QXkeLzaxBXUlPCufPn8Ud/9B06YkNYSjrZqX1QdOTPBXZfskFP1CvIl/PGc/VptaELtq9bWEjDnfVtE1bCw9P19xZMN1E+2M1YKeosyoj0lmqXmprCy3/xF/id/+V/sS8QTUxOINGSsMD8BPXhn//5f6WeOo7pmSVTESY3kjtDHTya8Fnh3YegoVofqiFP+I3Jd0A2kWaHKovMov4ZpmP+7nvv4q2338bZs2dtkVXZPDlmmXTa9JQbxEunisUaoJBe1KxW6eBqQfpMZTllSEkHqCPlxJX5p5kT0qF6dd30oZST0hKVX7k+k1bgPL99hAXpU8BnQvbuwhK3ZtIp7oyAZf55/Ji4fRs/oL/1e7/7u/jffud3qD/+EiMjRWj9wCKDH9lKJ20dDeo7ajdru+ULDww+s/qiCcsgHhufZbvka3IjD0lrzY5PjdPOvYnv/Pl3MHhzkP72GC5fuowf/vBl/O7//r/j3/2738XLrxw3v7dCxy1oD7o85i+78i8JKtAPtBiMYl6i3tVMf7mYDBjot45icGgQAfrHTx89im984+vmw0s/+uQDWw76deh0ZVJ9rAmPFzxa+uTutJgbJ6wfi27Zcdl8u0Dn4dyZs/izP/szfOc7f2EDe9Fo1OR+ZmbGZn+VFIsQNGOrwH3Zd8WBGlGwZXuUj4Iu5hkJRy1GVhiVzzPGLlTMJoQCIfiCAearSTvqU+yi+hGqL9TjwWXQ+Z8y+KBn95DgURBsU7gkw0uh8no0g4YCx30tTn1tdARDZ97F5LljmB4axth0FqPzWaSZPi+Ztif9ZaIsAEVK078eSVA7CzUdXq8O0piwfnSp2TF4vj4yoyfHGmuqVRd4MMMOOIO5pWlMsHOmljQNk84577cp9cyjWCwjlc0gXVrEvC+PDbFWbGL/bWXHtYXUiT7vNAubAJaywHwFS2k/ZhBFJhin3QzCG4yi5suw3DkGk6KtBYFyCKXFUSA5i6ViBWmWVfYwTfEWpsdP4eS7P8Zbrx7DsbM3cX08y2Q+BJKt6IxtxYYD+7D54BPoaS0hMD+MyaksblZ3Itj/En55Vxc+FweibX0I9O9C3+5N2LI3jHhXlq2TQpR1SPhK8OezKMwxoJ3twEKqC4MI4zbbqlCcgCd9g3UZRnl+lgorjakcsED6lkwmuOPNI1ibhj8zikC2iNpihq3egfngRkyHuoGQH+0hqaAuVPhbq8yyxSfhr04hkpqEL5XHQtaHRcSw5G/Dgr8dOZYfK6TRkmZb+soo+gqYLvoxWWzBfLWFlEeQ9QTpKGhUTGsiFOAtEctZKlTyLjmG/EIS1XwAhXILyv5eeOM9QMyHvMbXPHOkZAHhyiJasksIJwtYysWxWIwhQ/nIqW6eKOloRQYhliV+JanT5+mZUE6qSZ4vIk8tm80FWZYP8UIViWIeoTLrX1hALjmP6cUQbi1EsUAvJunX+jYF+Is5ZxZaIIz8UgGpOb0aVEa25EWKArlU8KFSjCMR7cL+vs042NuHjt4Qcr1l5FsrrOcSPNlZZFMFLGZKWMxVkCr5mXeI8jOCG8d/iNf//Pt4780zGBxfxGw1gGn1Vz8ZF55G1DuJWH4IlQxlvehFshZCyLsOnlIbIuU8IvkZMncamdlFLLGMZCWEfDjOdBGkq2GUxPPAIhBcYl3JXqK3plkXYfI9YIO2wiY83qBhaWGNvbYinvt98BWOYeb6n+K/vTKBPz/ehZv5fVi351k8+/xX8I2jR7CzvY29Yok9axoFT8pmZfoqtjqUoYEdSEBWCIl76iHLzqPlfP6E4FbFHnM6/NRr2c7jKif0YveFPVvQGQ16084H6BMEzWguobAwgsXFMRT9FYQ3bkXn4a9i4Nlv4MWdO7CzK4wwHdpyKI5AWxTd6/3obq+gK5lGfClDg0ld5k/AR10XoW725bJaBscG70vUS8VqkE5rlvbjOi3jDSTn/UgmA8QKHVxn5mjFR91G1DpjcpWpOfkrd+4zxKfHDRzxaUDygv1GuxqiEkqu3H0nzNfAJiXNU6Lfya3eLCBcHR7C2dNnMTo4gmIqg3J6Hrn5SUzQLqW9Cd4TMP9LyykoNCprINUkQaslOdLQhCbcD3Dki3LKuKccoDoj+qpziOYX4advVJyjz7bQgvTATsSPvICde6kDO2dRmzqO2Tf/Ald//COcHPdjNtyPKAP8/tYg+tZ1INrXDW8iDp8nzrghrK7DjsL8yiX6gB5ktJ7MAv2vm4PI5NJIrB/Ahn308TduRyAetRlBNuvDhF+9zgENgwmcQYA755dBl5sd5pEG+R8Pywe5Ix78/QAJlCXzIbQn2SJSJzsypgdelFei1rbTq7fXzk5h8FQOldomDLz0ZRz6m1/DV3cHsTcxQzvvQb7WDV90Izq6tmLduo1o6fDC66efWKTPQH/RqzeNvDnGcePIzKWRnU8jw7yz4Tz9kCSCOcaFi7cwnvVgzhOh4BcYYc/A72HcpZie7eeX3aB/oZleRr82P2WgcciH+nqjK8iNAv2ghdtVhI4gaGJ4CWUG4uVKico1a0/tA0szaI9QWFrXoxDbgLbOLjxx+BDiMSBGZ0VOs+7VK1ra1hp6x8PqrM5TxA++3riUXMKO7Tvw1FNHSJfzBSk59HSjreZVHmhaJG9DCFOolfKYnk7h2s1xTM6l0L9pCw4ePMDOVMbczDROnzqFN994A++fOIbrwxcwPHILI6cXsK6rDx17t6BlQzcS/ipiSyO4cPIEXv3r9/DWa8dw7OoVDJEmjVS3+CLwB7zIlOYwNHITN2+MYegGFcS1mzj95qt447UfYyZAgxhJIOFNoTx3gw7hafzwh2/i0tUxzGR9WEjmMDM0iJEL53HxyjWcn59FR2cnustTGL5wGm+/dgrnzo4imatiKVTDxO0RjFw8z7JuYDKVRCUaQFtbHB2hKsqFLG5cvYF33zqGN187jlMnr2BwlOUEaogmEghPD2Hq6gWcOHESP3rzOF579wQu3mRbUaHoqX446GXAkkclNYuJW8P47ivH8fprr+HaufcwNHgNk7MLKNHrjbV2oX3vl9HVCcQLY1gcv4mzp87hRy+/jdfeOI6zlyeQytGx0GyjUBDBcgGB6Ukkp8ZxfWwQZy9dwLsnr7K+w5idW2Bn9qOzPYEA5U2vXMm1lugl0ymcuXAOr7zyQ5x++wRuXGLbXx/E+Ng4igzMuo48j9a2BAa8M1iancLlM5fw5qtv4uVX3sDbZy5ianoOQX+IdYvAwyC/7svTSdegHQNGKvTFuVkMTY6xHa7jFOvwzpuncfXCFfSGAoix3TLsP5cvnsGPX38br759HRevDSJfXWIkWUUk4EOEOqJWKmNhdhGvvfpjvH3sHZyivjh97irOnr/BdruFYLWE7rYWjI8MI6vZFAwsPZ10luh05YbOkF9v4q13buCNd9/H8OhtGhfKM4PKxaHX8b2/+m9451gR2UoYLAxlfwGFQhLhpXlMTQxhYnQQl86dwXsnL+D0lXGk0zls6umnTqhgdPgKTh5/l3L+Nt557yTOX7qKwVujCMcpC7GIPXH0eRh66OtpapsK20kd0Iye9It6l6MD9eTmpxmkCzW783F8vVE0aeaguTckT0/Q6IcgMHsCp4+9hTdP5OCLb8YR2rbnX3oe23dswKbOOHq7u9G3eSs279iBgb4exG2tONpF1dPJ2UH7r+8/AmD1rdtv2ZG5ubnH//XGRpIa9u/sOr6AHgRpz6sHMLyo19L0YEhvKvgzgxi+dhVXRzMM0rqx5YmD2Pf0UWzZthlPJlqpz1sQbo3Z64fzCynK+iJaW+NoDflw8fw53KBNyBWL9rQ2SH8hy/YcHJrHxOw8HVPKFHWmBvEXb53Ce6+/iv/yl9RJZ85inDonk0xS9qrUPRH4/P7l4Q0N2DmehxFr5x7J9l8jNMqUwJ2loeNH8fXGu4FYUWeHeYjSGY1sUWCk5TDcAVfZ7JFbN2xG/dilQVTTVYS61yO0Yx+2bt2CLVtCCNM/C1X98OvhKjPT8goKuPQKjAMqQO0gbCjsIUCjDIqHLn+arzc+XvABPjoW0MRVX2WUTPtr8/DSP52bmsf1yyMYn8lj/zd/AU8+vReHe/PYtK4D8WgnfesgFlJ5ZOi77dq3H4ncDOanxjBfDqCS6EUiFkUb46/BwSHiTfp9N/H+uUt4m37Z4LUrqNx4DaeOH8Nbl9IYTxdt4D8Ua0FnRxe6QwpoPyjzNu+rgXaTL/e6NncuNeEhgvgi/bDa643ad9M8aGgs0dmXAq8fLF9U5KzOwD2jkTtE+QrOmsQllOjzvvfjk5gYmUPX5i3Y9ZXnsXfPdhxsjaC/twsd9BH9wbCtFT4zk0Qqm2W6DgTDQZQWkpgdHcXQ8A3cuHkZF+hDvMG8bt0aQaqWxVI5xfhlCNffP45XX/4hTgwq3mCsHKsgFtEXoH08jhq9asn6sz7tiWDHTDziINm4V683PnKDXiuJfmAgmdWrCxIEDRgwiNVrXTk9hPP4sSnqw4aOVlTCPZj2dCLAYHf/k08gHvMg7inazClHxdL50uI9q1TjQddNgiK8M+h1zILMHTu248iTh42eooc0q8rsnF6mJbdQYH3lqIUxTu8/i2l2wmuDk5iez2D95h10NPchtnQVQ6ffwnffPYu3B2fpxOfRmRnG2JWLePNaCN6BHdiwuwebu72IpJZw+zQduWMXcD2Xw0y1gAI7dXFqFpm5RUR61yPSHoN37hzOvfV9vPbuLZy4WcPsfBre2WO4fOE4htOtCNNotif03vI0Bm8O4+q7p5FbWEKmZQtqkVZ26CVkl67j6pXLuHmxiC2tWxDrruDmzASun7uBhau3UNLI+OZelLwMZkavYn74CkYWS1gIbURPXy82eS/i9tXjePfNYZw6dxu3ppcwly9gMZdBJLSA9VRS+bE5DN2YwODEGKZz01RUScwPZZCanmXblRFhwBMJsJPevo5XXnkVP74wh9l0AaHkNSzdvoirt+dxLdeFUM9WHDmyB+3eFMYvnMGF98/g9IVhXJpIYalQRnZ0BPPjtzCa8aEcbUV7qIjo9FlM3DiDP3vjIk7dGMPthQJyrHk4GkMX5bO3o82kUA99PfkhlFLXGFAN4XtvsD6nr6OQmUS5lMXIzUGMjoyjGm9H13PPoK+vA5sWbuHye+/jxLlJ3JysIl8sIVQaw9LEDUwUw/CG45T7MIMy59VFP+UlVKJSTU1h4up5vE/63zt1HZdvLeB2yYtsIIRn26bhz97C6ZszePPyEkYmFxGuTKGQHMWVCT8WMmF0BMvo8C9gfmYcZ87ewDt0auaSM5hbmMat66T/4jkszo2jY1Mf+jZtxLlT5zAzm0Q5QHqiCVRSOQy9+QZOv38O0wUfFnJZ+Nj+7a0htEY9SE4N4Z1jZ3F5JgwkWtDd3YaBtg506NXN+Ss4cewNHD85gfPXZnF7voCiBg+7ItjbG8DC6BW8+dZxnD53BaOTU1jKpBj0z2Dwxi14KnTUOntQpi7w+4qI1TLsdHpvvsUGRWRctFC+DXqxk6n3/7QPegkepzW9XDpcmiT3FqTWivBXMvCVMkjeoFP+5kmcyg6g7eAX8PSLT+LwvnZ0twbRFm5Be0c3ent62Tc7EafNcwNhvULMTIlWgFNOw+/DBtX3szboZe5onSzrkR4G2rbvPKYSKo0eY4l82UVtdU7DnV5PBf7kdYzeuIqb47Qh8XXYvHMfdu7chZ62ONrohAWiFQSCSwzwJu3hzemzebZXHzYlJhmw/RinL09iMRNAC/VGLJzGreHL+M5rV1EJBNHeThpK1ENXruLUG5dw+fwYbtEJWcxMY2nkMpKj15CmXs51bUegLYxEJUU9rFdsnWEvtbk7s8GFR5EPHwcuze5W8ifQ8SM76CVSVyLB+ru2dVSVTN7kc1GqnG/Y0X/U7M9SAd97/QSGR2fhpy0LByhP8SjaexLYsqkTvVvXUwaDiFQqCNLnlJ0p0r/T1j5gY0OfFuqrpDo+HFgpd+Jhc9Dr8YQP8EI6kbInftq6QRRqv3eSqjSNuSn6jlduYmY+h6e/9evYvbULfR1h9Pb2ozvBwL5QwtjEbVxJV/Ds519AV2Ecg5fP4OpCFan4RrS1xzFQuo3T77yCd96gz3ZjFNem5zCezVHuq9iWvInha4N4byGGOU8Y4Xgcfd3d2No/gO5oQ98nvXceKjlgsqUzOtkUrUcKxBvJkwa95Bc+KoNejeCU7tihleBMeZHuUgqloV5XAKAPktjD9yKunTyFqeHr1PRVhDrXo6u3Fz393fC2tSPmyyCYn8LC7ALODBUwODaL9du64A+VUB67hpFTb+H4+6fwznAJEws1JMeuYnJ8CMOMoW+Nz2FqYgpzk0O4duMmrl6dhJ/mJNbNmFgOhTeECA2ET4tOex1PR2to2+CXnug9RJO5VpBsPNZrej2qYMJqT940GuhhZwvAH4xjXf9WbN+zDzu2bEZfVycCoTBKZELZq5dcxBANeAkl5GxSeSCrgOu4PTxwXXtnTx1TvzboK+CBSLQr+vFoSqU6irqp1ttSH5FrxdpOXMDkqZdxfXgIi3T8N+w/ikO9nQjPz+BisoKL5QgK1RLa8tOojN/G8Tcv4/qlGXQd3ocD3/oiDh7YhfjCAi6/8RYu3h5DsupDKDOOmQvs3O+dxtuXkpgtxvHEnh5sXBfC8NVrGLo8jIm5JDJ0cONdPdjCIHJbWwhd6wbQt3UXNu/fjnU7Wsm8LPKX8shdzCHtb0WlfyNaenuwLhZAT8yDnm3rsHHfVmxbl0BbLUVDvYhrY8AcA5HqwnlcevfbuHDyMorlODbuOYAdRw4h3s2AtTCNRHYKubwPeU8XOtZvwZHnD+DFlw6ix+fHzeMncOHcOYxMz2A2laLyHsLrb72JjDeBHYe/gIN7tqDDn8PY2CTeH63gNuvXG0uhOjuKM++epZE/j9GJDDq27cGzX/0KdvQEMXXpXbzy6tt459w4ZpM51Mq3sTh+Gi+/+j4uDy0h1N6PTbv3YWD7NiTaW413ZfGw5Ec1fRtLt9/EtbNv4PQ5KsLwBuw7shebd20kb3KYYvCapDNRRB70rVEancKl198h3UuI9z+BL3z5Z/DNz+9EJHMLb586jZNXb2J0YQlpOqf63LRmPnj11cbcPFIjV3HlveM4d+wy5jM+rHv6GQw8/yxag2OYvvEy3jt5BmdG/Yj27MU3XtiCJ7cEcO78Al758TiuX76F1PRV3LpxEu8dP45UIYede7Zj1+6tSIQqyM/cQG5uCFrndMnnxejMIm5PLGJ+Jo3sTAbTt2Zx4cRNTLI9+jaux9NfeAZPHN6L3p4WtLcwkOzagY6enQj0xhAfiDFI6sKunn6sD3ahmJ3E6eNv4pVXLuDKYBXh1i3YtW83BjZ1wJcbwtDF13DsneOYW8hj45YdeOroIazn/bnFJZx65ySOXbmNa8k8lugIaip+TTNE2UG0kH1N7wlX9Oqqo2bFmyY83iBHWs5MoFZAqJKErzCH2ckCpidyKK/bhOD+A4hs7kMknkXEl4ffF0EklEBXjLIY1ORy2QwPTcRqw5+r240m3FtQP7xjou2ovnWxwSbKaTLHiWcs0NPrZ0UE9DoandlSoUJdkEdmOoOliSRuZbmt5VDxzFKhUlfPjOPa9Sx1fg1RnvMzyBsfnaHum8DFSzcxPnkRV4ZP4a0LF5Bi0cFAjvlcxLHX38QPv38dqcVOfP5Ln8MTT+9CxLuA8ctv4fSJd/De4AKmSFKoliWmKTn6zu6dGaWN8PD9jp9SoNi4A6x3JMsB+ZoaOPAStTXbUcygTPl5/9wtpMsxrN/+BO36DsQZzHcVp5CoTdHLjCCLoHFbn7+XLDpzujV0Ju0SYOaaSbos4E1owj0FZ8BW+lDvxDiRj5bzqEEP/dLweXII+WtoCcSgT5VVogMItG3ChvUbsHdLF/oSwMjENBYzRZSKWUxP3sbQ6Dhu0cdKliqmI+cHT+LM28dx6dIQsvSjendsoQ+9H1sHtmF9Wx9CvesQ7u1FZ28f1nV2IhEkCY3BryF/G4JeC4Cb3eKxgJWDF48FiGQTMWp6I9/Zen0+extkfR/jj2AKt6+cwjvffQ2nTlzC9aIXk6EYil5q9eIYKslJDNKXvHBtBtlsEYViEsXFIUxdeQtnjr2FE4Ml5KK7sG/PZvjY104dP4XXf3QSw4MzCLW1Ysf+fSjOXcf4pWMYvD2DkXwIS+yFgWoZ/nKRMRstB/1Xx795DNv4HsCHPaT7DI0OWKNgPwqOmV4XEEVaNE70aGFELbQYi8Xha2lBldfL5bItoF1lGmfRxDo0yI+qovtXq9OjUM+PAlXDqmJk8sdL07FsTPSkzqloZnqKzvtttlkQe/bswzPPPo2d+3Zhy47NNgsgogFDvT5ZqWBuaREXbw7i9vQMtm7chiP7nsS2jZtRKedx5coFXL12Gdk8HUA6bPlsiZ29gEAogI1b1uO5zz+Ho0cPIxIOYWFhHjOzc8zTY7OytmzciJ7ODvQPDOCJg/vx9NNHcPDAQWzasAHRuBfpwjyCzKeXxrGXxrG9oxM9NJbbd+3C4cNP4uChQ9hIOiIhH8qFBVrvHDIzBZw/dR3zyTQ2b9uKL3/5BXz1K5/HoYN7sWFgMzrae9DV04at29exrD04cvApPLn/SURbWrGUyiCTXER6cY6GfBpDI9OYmsti+46deP4Ln8PRZ49yfzO628KIe/JURFmbAjs3M49rN0cwOrOEaGsnnnn6WfzMz3wVR5/cj5CnjOFrVzB0ZQSL8yWUqbTShRymFjKIt3TgwP79eOboQezftQV9He32nLemJ6ZhOsNUctNj0xi8McR7Cjh49Ci+/PWv44lDh7Fx/Wa0xlrZ4noCQAeaODI2isvXr2Ehk0HHum7sPrATO3btQMBbw62RMdwYvGWfoC7qq5Isxy+50CrMtSLydNjnFlPIFmoY6F+Pr774DJ4/spW5e3Hj+jCGBodQzGfRTQdl95792LxpK+s9hRtXL+P22G1Mzs3aK4m3Rm7a10GffeZZPPfs57Bl23bE9SSktQ3tiQ4GmWVk0zkkNcMvk0KunEWmmGJek5ifnUJ3Vy+OHnkGTxHXs4yWtk5s3jyArVs2IBJhIDGwCQcP7sbevevQ3q436QO8L4WJ+UUEWhLYt28vnjt8ABt7OpGamWGdBzE8NY/Wvo147oUX8OWXvkC+PIHt2zZgbnYcN69SVmYWUC1rpoW1itN3iDUaFzMv3DrDzY9237+f8Kjp+k8CH3bAyFdzoInUb3n2rSKxrb0diUSMDo7UZn22heSAUUFN74CoX7LuNnCma8twZ/9RapnHjU/3Axzeu1gH7sqJ1UcMZmkHr125ipPHT+P4Oxdx9tRFzExpIXsmqvnsoyvFzAJSC9PwJLrQtXU7Oql3UrPXce70cXs9/fy1cUTiMdq0bkT9HixOjuMq9cqliQWE+jbj6196EV95/jns37MT0WgIM9R1w0PD0Ldhal5Fe/qSqFem2uTrcfQ7Pg08enUSPSvxDpgUuWIk2qkP7N0wYpWylE+lME87ODOziLa2LuzauY22tJt+Zg0lpvXqQzq81fHG9CuULnGGO1WaghlZHfvXiSY04X5BXZZdmZbfabP1NGGA+lGLaSuNn16pPvalfS3e3dbWZtey2ZwtWJ9kfJBcSnGfcVWF0su4IJNN0r/L0WeLYxt9wKNHn8SRpw6ib/s2bNq0Cev6++n3b7DZQDt3bkVbQjqQFle2tb4VuPqwacseP/iw3/XoguTL5E8Hy1unDj59fTEYxMad2zFAnQ5/FeNXz+DCm6/gxPuXcHt8DpkSw09fCAUq8FRqgXZgijpdE3A89gGdVLpILCEcbmGMsgcvfOE5bGNMk2esvDSfRUu8HXv278NLX/ky+jrbUMosYXZ+HnOZPPRoxDEIegnTiUQc+OnsE+5oxgOBlYrHVUaN51emud/gCGpdSVJhKzgRBTrUnoKXgNcPD50SrZWkV1KkwDUQVC7bm7yO6CjIIQqc+6l8mcbyX4H3A1ZrN7csGSIDO1TFrHK2v/I2HQqdcS6mYx4VM2aqs8deQcpm9UXHMTrdGazv34ad2/egu78F7fu68bVf+RIO9a3HTm8Yreyt86k5XJkbxyBN36AniMVbWQydG8Ot65dRyN1GS0se47PXkC5Mo5aNIlztxebN+/H0F5/B0Rd3wd/hx049HertRDq1iMmJDJKFGHw0nOviEfTGQmhpT6BjXQRdXTF0t3Sguy3K64NIJi4jV1qi4YwinmiDP9iCYLgLbesGGGBsQt+6zWjvWIdEMInWyglEMteRvjaApcv9CPXQ4TywF32bWHZPBS88vQlH9n4RbbFN2LwrgF2HquhrL6M8mMHEiQVcn8sgxfwDhQX4Z4cwPzqNm7MJoPtF7D14BO29EcQ3tmLfk9vw1ec24aU9FRxooWJbnMfs1BLO3q5gPrYHfQe/iq3b90mccHRnHC9sC6Mrx3RjN4GFcaSRwRR/2w98HXuf+iZ27diOjW1h9JFp7ZkaQtSaQaapeG4jPzWDxYszyEwX0HFgH7oPHkCxqwO923biS898A1/Y/Tz6SXNbJQ1vOsk6jGGmmsWtYgHnFou4cHsOs6deR3X6JhZzAQwzn/mpDIKpPBL6sojkylsA2H7FSAqeHir1vT+LI4dewM5IFZvBYG+mgpHrS0hOLaKaXsDixBgun7yJ4euka2II1aVRTKdncDW9iFEGh6XKrM3O8pf9iPlaEYh3otLeDU97LwLlCIvzIpT2IpZnQOktIxlLIh2ZQbAyh5mR87h2dgS3b+WQKkZRDPcgE25n4DmJjrYy4qFetMd3oCWSgN87A31coZht57lDiB18Bj3Pv4htOzdil28efdlJGwC8PT+Nhf6jqBz4JiKbd5DnJTy1ux1fe3EzelrTWLg2jfzNLPy5CCr+HlR83XrWblihcSuF6Oz5ywiDBou4Ut/9tIBb58e97s5gFlEKUqMMtAvmmNAmSN8HAl74/Y4t0JpyUqE0H6Y7pUt1wvlrBLaJmkVto/9HoI1W2qlGmrT/cfy8X3bu3sJqtH+QN8Zv1kXV0QMfq1eFfTkUQK2Uxsytazj/7it4+3t/hmM//B6352jbYsgn46iWIgiUqHsL1xFKXcT1/mdR/fLP4csv1HAg8Fe48Naf4t9+exo/utaDfc8dweYD/WhZHEfwygXkcsCNJ34Jc1/+v6G/Oof9kRKO7h3AoacY4LUFcOvaTbB4gLYQpVZ4q9SZrI6f9Ll+hwsO/Y8DP9YOrty5dVspnw8cPOrrH0TnebqQfiRRq8S5tiHo0SMSvVqrwYAqcuk0bl25jBNvvI6Afx327nkBGwfaEQnOoVCiDSoXUfAkEK146CORz94o4Gsx3RPVx2ewaMNe+gARQyXmK3y0eX43Pj0U/jXhE4PYRPNXjxW49TmvV2tAq1QqEgt2TaonEAgSQ/b2jK0lzNhJX3q3Dy94NHqvh4VRyjN96uI4ytVpbNiwB0ePfBlHn/k8tmzeiKBsaEsMPT2diMfaEIvpIVMrErEw9R7LYW72xXKz0QI3lnN04seB0rrYhIcH6v8uurDy+FEDs0MmdY49cuXN/ETRzW3syT04/I9/DX//n/0a/p+Hgoj/9f+M//X/8y/xgz/8CwzeXMIs9f5SrIP9aAEhxlQ16n1foYh8KQ5PbAvWb3sOTz75TRw4sB2b1kewbUMEA+2bsGfjS/jckZ/H+h07EVnXjs9tbMcGzwRjtixuFIOYYuwOxnWoFRiBaEawF1V2mGpAbxw8um3q8lvtqX216fJYBuHTysPHa4KfIjAV6dNnRv1UnD46KU7z6FOgGifK5fPIF/LW8FqMeVmwxRQqcH1+1MYBNN3mMQV122WhsM7ivO5pDr9O8VjrMKRSKXvS3dnVSSOkd49paOIxtHZ02MyqeJwdlW2pdkou6alNxtbdOHnyNE6dPIlrV6/Zk6EDB57Anr17loPCaCSK9vYOdHUl0NrOc+Ew25MKg3lrbbKqAklSEtCsPBo30aJ7K1Viyb6DiGgsau+B+/0+hMIhcww1E6NIekWD+Kbuovx0HAjKDXX4m8lmuM2R/ha0tYYRDXvg9wVIRoRGlo4m4cKFC/jr730Pf/THf4Q//uM/xrvvvGMfOyiRFnXEHCMWa59yGS3Mp6+vj8LFVqWMdHZ2Ytu2bdgwsJ45ebC4tIRMOmN5t7e3s94tbE+nHM2iSrS2ojWRsHzTdIzzpNEfCKC1rQ3tbOso6ycGlaxGdfnldTkgqsvC4gLbqEDnoIVld5is6j1oravX3taOUChkn8Yt5AuYn9OHBSq2r5lZb7/1No4dP2ZtdPjJw/ZZ6Pb2Nraf49z46p/e5wl7kiE6O5ineGiDw/zLke+Li4vWJtlsFqO3R+0DAENDg9i6bSuePPwktm7diu6eHvT3D2BgfT++/73v4zvf+XP83u//Hl7+4ctWb83ma2VbiF6VbTMuyc8o5ezw4cP4pV/6JfzM138GV69dw+/8b7+LP/z3/wnnzt8kBaSNbVUgb1S+KU2KVU3yzLyUn54+qu17erqRaNOXsaooz83ZO+QLC4s2S7Czq5XskHwBCcpnb18vwqxzle2VXKqS38axJnzGQeszWD8j36l0QEVhsiWQXsnlgXRG4afSERx1ZbpN/cSdNevMy2jCIwNyoIjSs4rFxDJBiXqmQv1oThftjT74rXTpTJrs9NjaEl/84kv4xV/8RfzCL/4Cvva1r2HLlk0IU58H6vpFdkb3K8/+1n7s3rEH6zf0IL80iavvvWtB4gsvvICEvvhY1EznjD1oau9qZzreRD0j7O1fZ+tYBBlAZnN0YPVukay1dC3z1z1lySRBx0149EB80QC5nrpLHwirtLcTgzfx3b/6Lv71v/7XGB8fx/nz5/E2/Yrz587h9sgIbty4gdNnzmDk9gJtH+93BbQJTXgA8AF9IvklypaFqJokjgZae4m6jqnNjyzTH9eHqvLVPArlHOVWD/2YjP6pHp5rTT7zwbmv2TAG1GXO9aD5yvKzFEuodOlfOmt2j8pWHppxq75Q0GzqD9jUegdp9pMmPACQbEr+7ENHjJtliyvcVtVXFHNQdDvjXdi9dTc+/9KX8Av/l7+P//7//t8z7unG+++/jzfffANnzp7B1OQU4zO9FMz4hDKuGNd524yxNWOv9o52xn68Wo8NFdP10yfo7+9HJBq2tIp9tdaqukM+XzQ31fU/dVJLFdkDWe67b279NIFaoQl10FcO9ISsUqmhSGe3XGUwU1mio7sITywMLwPjCAWtPR5FZzSCVj8VNGVGz+883gi8/iBq/hpKWt/nUQR2Ak33VYdyX8WSqRGqT0CfY9eW/cGGgbzsOJ4W3hOGp+q8+ul82TLPzh1hG4WQ9gSwEPBhSZnTeYO+qpevopBlsFBLohacgt+3gLaaHwOROJ7etw0vHt2Hz331G3j2l34TL/7i38FLR3ejJ857PJ1YqnSioC8TeUoI+LSwaYr0pWksPWxXL4q1EIqeOPej8BbzCLGtY1EfO7xmoVGc9aUKps1Q4RTYsSu5MPyVdoSDLfCFVEYalVgCGQUK1TEEPcMIeaoI1DbCX+2jwsgYlsj7IpWVPiFfrupblX4qiGGU5o/jrb++iG//H5dx/EoK/t0bseVLu/G1/ir2Vm/DG2rBUqgfSU+UARMDo9o8MukqlRGbM+bDDLK4OZ/B5EQY1XI34i1VVL3TQDYN/1IR5XQJM6Q9qWe23gGEiJryWvCxbUOkIlhEkFt4WokJDeno0wkIqicHyYNKEYUSFXCtjwGXF5Gw5DeHajqKUDVkbyNqwmuSvNFfwVOk4xJgWuZT6SJ2Y1t7B76wow8vPrUfh176eTz3s7+Cv/WzL+FbX3oKh/dtQndHC1vDj5o+G+XtplxFWW6I7eMlfRXSXEGENMf5Vw0wEAvQQerwoHVXCzY/swu7P/83cOCLfwu/8X/9efzq//klfPHgAWwj79sWygjOzKGn5MHZKQ8GK33o3PFlvPjF/w5fePYb6B+YRxjnybNbSATLiHv74c9vpaz0oudLT+L/9E/+Ab71tfVoK13CpXd/gDdfP46RoRSKpRgQXodoIGRfzvP54shQtgu+HHoqJ7HOewx59t05fwQZtoWHchqItFFeSVPOj+pSGr5iAQE2XtUfIN/YDwps4yJlUU5fgnIa0WuizJvIS4bSJgGyxCd94GITHm+g3tAAe579OxPqQyG0Dm09BWIRnjPvoOXMMbTPJVEtdTJNAhVvBlVPDouVEuYpCzlp3moJIXdQrAkPFFwzp69u0rDpiBzRoxL2be3r6RZPS50K/Uzjqz8N1VqJekoK6vhyIIZ8x2bEth/A9ieP4PBzT+PJZ3fjqed7sWHLHMKhRaCUog2qYD5EWUgMoG0xgETGi/HZKIYzPQjEW/BE3wI2Z4YwODSNJdrMtL+IZChLGzaL3uQQuhfSWPLmUQlGkStEkU7FUS4mEKQe0qvx8DlrjOnrsUEv7Vg9dmzCgwX1Zs3bclAi5L5IIqnS64e8QlkQ+jQTTCJlSCZSn9CTtK8jRyIt6A97UZ4Zxdj1k5gcOYfpZBLnMwlcmi5ibi6PWq5qpkQfR6kK66XK5moWmImAZKMJTbiH4A581Xz0/fzy9/zmewYU1JdjqOYj1E3cejsQjHfC3xkEXWe0eSYR8c1hYm4W71yew7lbZezaNIAuxlRB+kuBqh4mUKDl4zJvD/25YrkN+XAAxTg9Tfr3WqPeL6EvLFB/Z60/uTpaetD8Xz2tMBodOtWrbL6jBTcfDe5dzp1NaMInAecBv/qHuoKkUpLnPCKjYFIuFSt5ylHE0IdE63YE9h3C5m/9Lfzzrx7C84E8ZicXcGa8gpF0mD6DD2VvED7GIr4qY9/SNDyVGfa3JRTpG6SZpcasanRI9KEszU0pF+WZVFBmDB7whXiN/Yr+QJSxV1AdRH2Afgx7Lfss/RzuFz1Mz3700wZSFU2og/sQn5JKGaHIenwIMdAtlfIMfBdRTKeRyWaRTWdsVk8qmUO5pKcaesoqsed9bFHNTHrUwXnuvLoxWLYRJfYmCwIUDKhD85h3hsMhdHRqrYkgxianMDg6iVSK3WdhAZNDw5iZnEY+RwPGDhWNBdDV3Yb2Fn1CNY6deid/wwC2bt+BXfsPYeeefdjQ14dIgJ2X7V1QB7YZc8QyGVLIw76W5lVwItdOCsbHNnac/lqljGRyEVr0r1w28szuFXneujNp92iWFeuhGXv5Qg7ZQtG5xkChUsmSh0XyPoBgMIZ4PIJoJIhF8nt2LoVUmoFIpoTxiXEkx25gZmoYtwbHMD2VRjTRgT1PPoHNu7ZiQ2cCoSrzZr1r/jBa2T6J1hYszE/bl+qSySpyqQzznMXt8QlMjM0ikymyLf1ob49TMfmQ1/WZOUzNz0ETUQuj05ganWKeWUToILS2t9IxpktLp7lUqtoDN9l5Q6uPfugcaKYiFV8kzHtaYzaoNTu9gPHbSzaLTbO/JqcnMT07jVQmxbprUC6Anq51CDGYi4UjGOhJYPu2AWzatx87Dx7G3j392NDfgpYWqkw2vPMkg6WqzUmApqrbkw3JiDqS/tnekVgUHV0dCMdC8IW8aO9ux/bd+7GbvD94aDd27qLz0xZHjfybm2DgNzOLfTt2YsvOfTj6/JfwM9/8Obzw4ovYuGEDYhGqdQaSqDEIZJ+sFFVxzdyjLLREkGA5R48cwDNP7kUr+TgzPUs+ZigbBXgoq3r6qNdIsrkicrw3nUtTxpN0plJyuVBk8MHuTJGhwQpSxlvb0RZPYGFOX0dJYmmxbJ8SnpiYwI3rN0y2Onu6WSfyL0yjJjmTfEouxQg7ctmiM+7ZJjxO0PiUW460dL0G1mseyhQd/971vdi4aR1mR4Zw/dRJ3Lo6hKnpPJKZKpKpJczMTGGUfX56boH9r2B9RFqsCQ8H6mqyAcQNp9OK18Zv/lvf5Y8FTc5lqjX90lZRV5T1MQJ/EMFQlHaOepM6qK0tilC4YguU1yolm9VTYFowSKwVqxgdvIVzF65hbimH7Tt34ltf+wJ6E1G8/PKPMDGZhT8ctdf1fXRYFyZvE6eQrxRpN+YxMjKOqakFUuBHV1enM6nCBuREvWgmUic3ymsTHhQ4PfrDLe+ecTwubTXz3ARLfKKv4/HTB+jpxdGjT+Nv/I2/iSOHD9pHk3q7O2hvwwjRHwm0cL+jGy0J+gCa6WLy6Jbp/Gow17FATWjC/QFHtzjya7tEP/1Bj60r6GCVgXiBQbj8q+l5+txz9DPHR3D10kWcOX8ZC6k8Dh44gNYWr63zWqI/bjOoma1cykqFfl7Zi3y5RF89j2LRmSHGS7xIv576ULNvNQu3VJ9NpgkrdXIMPk0f0D2f5r4mNMG1ufIVhNLxGkPgj72Rks1ksTi/hPnZJJKLWcbHjGspbV0RPxJ+vTXjhycQgY9Ypn9ZZkdQDKyoV4NZtariW/YFyr7CYs2qlG9RKpUZv6pPVJiH1/ZFiq5V2TH0wQlnoguRW0fG9aczmvXl9pifHnj0R2ceAtiMLypvPfUtFwuYGB7GyRNn8PbJ8zh7+TKGblzEzcvnceKttzA9OotMWq/OSVCpk3m/LXL8iIPrMJmjZJ2BOyTbQyfa3o/XxUqQCSPsfOxghQoNVI71zCESC6GjrxfBlhhmb17ArTdfwciJSzh9Po2Xj83g5uIgZj3TSFK8vIH16G3dgnUhdsqlSdyYZmA4N4oJBoLzE5OYGZ1EejFHGtQRizRwSWRzS8hpoFHiWQuzXUlHdhbF3AwNaRbZMo/97eYQatTl5rVLuHDmLAZHJjCXB40lDW+6BH9awWUApYqHxrPMILTI+/OoFJYQlDKgoS4Ua0hlS0gWgJI3hGhPGD3bulFJDePm2Xdw4t338d57l/HaGxdx4loSU/korW8O/vwMkEkizzLmZpIYS85hOpfCor6QEQmjvSOGdS0sPz2Gc2ffwml9/fDkKM6eT+LarSzGltJMW0PB14ZEVz8GOrwIZgcxeukYzr53CpdOXcUrZy7j5PQiQl3d6N+4AYnWDnjKYRQyrHVugvuz8FcL8FHupAeLtPxlvw81H4NyTx6++Dq0DRxFR/dmFGbO4/Rrf4aL717AxdM3cIJ5Xx0Zw1K5giwVaCEYwo4u0hyi0sySNzPDmJkex/hMASMMxhZG02RBmTJQs1cpy17WTWsxeNKosr1LpSDSpSKS5RRyNTYm5SdIqmK9fejZsQM90VaEp5LIDI9idv42ZtITuD0xhZHxGSylkuwzzItBXNkTRikcRDywhBbfHPNYQj4zj8nJCaRSUV7vQaoYwmJRi+cvopiawsztMdy+cBnXzp1DKu0jH3tIX4Kla3BUi/9WEAn64C+w3MH3cZ3ycmMqh7E05bfQgYVSNwLZDGLEgCZ3esM22yva24LOzT0I5ycxfe4dXHrnXZw+cQ3vvHcR33vnIhZpoLZv6cWW7hjzJy/ZJhVPxWZ3CfU00hpCHcvWrHBeo23C4wsadNdsUropprPkaIR7n0LfthfQ01FAfurHuHr8z3Hm3bdw/twZvHPuPF49fpxycxGTg9RhGcoE77d8mvDgwXUArW8KHDvozJgRT9RXaYt40jikKMyehsmJ9TOtD5WqD7mKnzalQHuSQaqUQc6TQ9lHPVPzwVfSuhlBZH3/f/b+O8iu6z4TRb+TQ5/ODTRyJBJBgpmSGERKsmVLsi2HGY+u/J7f3HmemilXvVe3au5U+a/7Zua/d31fje+dcF13PPaMk2TLsiRLshWYCYIEAwiCyDkDjc7p5PC+77fO6t44PABBCmg0iP11/87ee+21117ht35h7bXXTmOa1xaKY7xtHrXxC9j78svYvecspqOrcf9Dz+IXn3gY21dlqb/exrFDxzBV7kXH0gfIS33IjryKS2/+N7z/3kW8sfccnn+HdsjZSVRTWWxf34u+NPU27RTxkyuTrA9frhALD8c/zqVwprXb9xAPyRHSOYZreQDJkngKnQOD2LzjITzzxS/hkYc2Y8e967Bxy1b0LFuLRDaHrkwSy5b0ob8vg1ScdhX5OKoHTBp8BW0kkrV/Qy9ON4fBgrcOEeJmgfxrM2PJYFGKmzi39Qhts6QoinxtCpeHj+H0mztxZOcuvPfWKex86SB2vXcOp4sxdK1eh4fuGcSSZJ72ZI02G2VkqUg7XctPkHP1pkKhgfHSDKarsyjrtUjaytaj2F8KpQryxSJtdxntZSQrFfdmyhwc44fsH+LWw3GZzArJensFl5zqh5ckhMsV+lgzeVw8eBhHX96Ffa+8ib3vH8drh07i745dwrFEDr2DS7G+L4c+veE0NYVMPo+IHtZTvhfo141Rtk9UZtAoXkFat0hkUaBfXioyjH6Q1sKrNzTLMo4i+1GxOoNagdfn6QVpMrg6qpx9lytZr/SL9Hv39RKTIyGaEI/ahqxAA7dGTi7SqD134jhe3r0HL7z1Hg6dOIHJsYu4fPYE3nr1JVw8cR4zk3k6/Q1TAnVes/jNThn46piuH+jlDg12ydLXeJ1e/bD+Ec0ZJeKd6OzoQndnJ5KpGOKJCHLLl2Jw3VqkS+MY37sTB15+DS+9NY7dx1j6JTTKlgHlTAei8dVY2bcJ96/oQVdlEs+//RJ+/Nar2PnGTux+6VW8+/qbGLo4gkitgUQK6MjFkcklkEjTGEwwjzHmIdaJ3nQV3R0NxNMp1KJdiKf6sHz5EgwMdGPk8jns2/M22+YkxioRJDJ9GOxagn5eF6fjoa9bxdMd9iW/ru5+dPA+SZZTs3+SqRzSHX2IdfSinkojtbwD2z+9Dcu6Sjh/eDdefu6n+Olzb+KVXUew53yDZVqFdWsooAYSqE6N8b6H8fab+3BucgTRng6k+nqQ0CuwvR3YtDSNjUtTOHrkTex89QW8+PIRHDxWRb4+gOzSFUj0LEEx1kOBtwqP3rscm5ZQmV86jDdffB07n9uN7713CMPM29bHHsfWHVuR68ohVu+g0OvBQFcd3ZkysvZqJsuiJwo0hkvxGMqNKo3gAiLdq9FHZ3zdpgdZF0PmjL/54zew5439OH7mMkosf25wOarZDl6XxKrBHB5Y00/HbRrHD+/BTjpoO18/gOdffhd7d53A5eNTyE83P1OtQa9omcK3QLmeZtv1IkX+iHcn3at+lCxp9oeOlSuxZscObFq+Fr3jJVzYsw+v7voJXtr9HF545XW8tecghq4MI8ZCZHvIax0DODMxgrGh/Th35GW8s+vHeO7HP8Tzz7+AI7x/NbYc8c4VrOc+dHTyPtUpDJ+9wLK9TX56Ga/tOoQDJydRauQwsGQZurs7kc0ksKSvC6u6i8gPHcCB/SzPyWGcm8mhEFuLSNc2LM9msJxM36HPvUeziGQ7kV7RjbX3rcfmpQmUz+zBOy/8GC8+/xZef+sw3j83hdSaDbhv60qsG8jYq0U26MVtkoZbguQGkq0jkTTopVeKQ9xJCM6a0b5scukGPZlzrUoZ1XUvlm18Fs8+uQHbVoxi+vxOvPnyj/Dqy8/hRztfw/NvvoUjB09i6tIM6kVeRXnkXs4IcVtgg1i+Xd1gl6jRNFhFevCjPb2OpvcHbPBCA0x0ryTv4lpIuasLyWwKDb3inKiiFqNeYfRYlbYD9U4p3WlrvnVTJnbmyCeTF3Dx0EGMz6TQu+5J3PvQ53Df+uV4bHMfOjNxDF04S0evE10rH8MD996LR5cOY3r/N/Gjf6Dt8dpxvHl8HBfKWXQuX4NHti7DEi39SF6yQS/T3SyFyRuHcMbXQoL8YVyirXu9xUadSNYk2tfZ5oCX5EiDMoSKj0IkibgGtgZXYNXGLdi0eQU2rBvA2o2bsWw9ZcuqDVi3agVW0+bqos7TK6wx8nC0zvbW7GRkSGm2twY9RQ13uxAhbgFk2Zj/YANe5EWyXBUplGTAZ5NIden8OE7uegn7fvpDvPT8Xjz/oh401tCx8QHc99TT2LqqCz203RKxDNK017WuairD9OhbxBoZ9DIs0U27qitF21LrK0vXkqkTeu0rTdsvhxxtu1wqSZutZoNeQZa/FvtLJnry8HvWTd1uiBBt0OQOzyhNmS64MQPJdx7zXINy2ViM8l7WhtZhHD5yAoeffxVv/OglPPfau/i7t/fh+6dGcGXpGqzZeA+2rxjA6mwCy2JxbOjsQpZcn9AD0kwaNflGPRl0pUvooNqI0AaJZXrQ092B/s4YUnRoq/QNY+ksMp3sE90p9o00co0EUlI2GvSK1Zll9V6noTTkJbrbIN/032jnf/k3trmpEAPYFL2oq9h3330Xx44dswUKn3rqKVvI0GOOYZr7twP2WXnCbi+bhexaLs3i0rnzuHD2HIrFEjLdSzGw8h461AO2uPrG9evpUGfRlctCXydhYZWSCemFLke7+0m4q/7Hx8exe/duTE5O4J5Nm/Dww4/6rHIrg1nGUp3GWBRVdpQ4z0UjResgNRrx0WgaPf0DWLVlo30uuCs2izQ752Q9g8ky27lSRjYaoYHfi+UPPoYdD9yPzTTcVvd3YlmuF/2ZHPLlCg5OjWN6Zhbl0WkUJ2boR0SwZss6DA72o5N308J7qRVbsGLrvdiwIoGB2iTilQbK6ZUYWKMvWGzEiuXLsJQKclVpGFFqyiONXkSSGaxe2of1ywbQne1Eb7YXm5jX/k2rkc6y81frWJ7pwOrN92DJ04+iL9WFvuKoW4+gdz0619+PTeuZ354CBnoGUGC5RiaLGJ0uoVzXgp0xrF89gB2bN2BpLsNydqGR7sB4uY5quYxVvd3Ysu1eLN3+EI3VTdgw0I0VWYoWGrYnp7Rk1xRS5XH7nOz6TTtwz72PY/OmDdi0YSkG+7tZHqbZ0YFZOlZnJstoVKuITI/jic98Bvd95inGX49lXVV0VSZoI2dRXfK4fdJ81ZIuCjcKL41S0unRq1egCawvjcbZuzPZDsTTOUyUIpiYGDMxpwXol/UtwfYtW7HloQfQt3UjluS6sDxeQTfzMRnvsJloo1eG6KQXMDo+SWNmGfoGtNh7FjmWS3MZYo2KveoYrVRswLfSsQz9q+/Blg1rsLI3iURD64VV0UmDPhodwGw5ibHpMdJFjE1NYnQ2hiz70D1Lk8jVpnHy2FmcPT+LCOVCdmmX9cHLZ4dweN9RnD17FmkaOdvv3YZUpY5lg4NYTl7oIS9EaiXMXtiPc+cuYGiiZg7nqvUb8MBD92Pb5qXoSWjOYQyzhRiFPhkn04lktwYOc9iYox2VySK99gGs27SRPJRDb7qOGPtDPNNAB/m2hj57FXVichT50gz9lBQG12zGs5/7PO6/T5/LzmpIC0nWvxbwjzXU+9UftfaaVJ4UoDobe1Ozi94uGbcYoI9P6JXf06dPUx5N4r777sOqVatsYVpBdbPY6scbyW7QS/JSolNhdfu6r9aLG+zX621dKDXSuDxRQb6imUAFJJMp9odVWLt6LQaX0cDPudeT3GMHD19ebRdP+b3+kB7Xhx3OnTuH4eFhW1h1x44dtmCq1++Lsd0+gMCgkDUC61o9VKE6ciXhvi8T5Zyi1Wh8ViJyu+pI18bY7HVEOtdjcNVGrF23EssH+5Dm1VkNPLDfR+JVxx21DHLp5dhEWT/QHcPoxDj1GPXv45+m/F1LI7aMbsre0Y51WNrfi82rl1IG9WKQ+qO/N4fp6TwOD1HHUH8N9A1QZ2zCjgd34L4Ht6MjHUWaDKk8yZi1t/iZB5mznl/viDZpA59nvw2WR6+LfOc73zH78f7778fq1avnZEeQFxcSnqt0V09Xhza3lq8G9NEjmxUQ4Ee9EqNFvLOdPfbxmFSygWQ8ho4lq7Dyvk/j3i2bqO9TyMYa1K1saV6qN2crGvPkn5b0dPdQuvZv4bcLrW3gZYlw6NAh8wfUlo899hi2b99uMibY7gvdhiFuHGpL+UtaAkZsXolqtcoaorUq/WvpxzjyxQQq1TJt3wm7ZvWm+/DIE8/i0Qfvw5plGSSqJejj1npVPLmK8nHLNqxZ0oGVjSIaWlplxT3YQHtvxYqlyKRjSDL9jvKIrV03MXA/lq3egC2rlmFVX4428Tzf2KtldvThaMdjCgk5b2GhdhBPHTx4EKdOnbLF2DdR1+lDMdrXudstE9pySjM/siFcBA2oaleyjlv9NLQIMH2ZUxdw6fxlXJmawJXyNGbI/+neATz+yAN45oGt9HcHkU7RX4t1YGDpALY8sBodnSkb7E0l6X8vpZ+84VGsWNaD3sqUvdqYSCzByjX3YPWGlch0US/Q7sjMlNBDW6Fr0yPoX8truuniRvQKsfRFhqm5PuLxwXItDgR1vnSDPoi2a9cuGyAXX+ijPtr3OkVo5Y/g8b/7t//Wtk2RBVSbN/hZ4TMq6IZVOu9iWuGP//iP8cMf/tCY+fd+7/egr7EJQYb2+7cOwXK6/fnKLfO3jlojzkrW++l6klHSJxAwUyohQuelEUuwrmhWxuJ0hPPoyOVoYjom0pPiKrd6vzxrjtGtLMfV8PUWrH/t68tQ+trJyZMn8R//j/8dZ86cxhe/9BX8s9/5l7YmSKxacwa6HHSWvc4u1mhkrAwoTdo0ekSzaNQ0g6iOqaxONNBf0SuJNUxOT2NsYhLlYpTG+z3o6k6h3jWCWrSCdCNHpZa2tbTy8bq911y4VEJJX56S4cYO3dOdRU+sDH2RCske5GncN6JUnDHmi8owNUumZj7Hk+dZ9zUk6z1Ms5v3rrBsV6wFz1waQakeQyrbZzO5ujpiyFYvyQJGuZpELMo2aiSpSOm8sAxlalrdr1FzT6vKkQJqsSKSEQmYrB5boVo4jytD521B/HhPP9LxLnRVl6Crk+2frKBIh3ZqbBr5iSIy2QyS/Vn7UlcimkCK940zkUZ5FmXWz4UJ1gfL1ZHsYN562FHpKMZTrHwWjF2jSAUfSRRQqk1jdrqC0lgUU6NjWLZ0CdNmPnvTKNOijdNQ7qppADKFSTZQnPdJzxbZhiwYy9TI1GgWaNHcPrajuUKsHfarcgm1sRETGtV6P+8dR3dvkkIySaGsta4SKLFZK+kSr2G9TkyhyDadnq1gupS1waa+dXFml23M444K+wHbqJKdJa+wCLVO25YoxGVvp1N6/WIWlXyefb+DYWmbVTY6W2CdXkR95rI5zTPLliOZzWHF2CQu/vR5/MWffAN7zyXwP/9//x3uebobKbbj0OHLePOne7Bz937EVm3G//q//k/oakyjzvoH6yEWz9i6bo3RYYxPDOFKhH2yR+vHrUQ2tQTpJJ2Lwgx5KIaR/LQ5nfVaA11dfejtXYICnQrlWQMYGoRIU5Fkim6NiXxXjvVFQ6tQRHF0FMPFaUywvRJsu2yiB/3ZLuR4HLMRYvYbJkSWMhITJcD7cks3mZTTTeSO6uSCyobFAC+XtNWXTfUF1Jdeeony6Ay+9rWv4dOf/rR9VdTLscVSP8F8C5F6kcQ2Zf+rxkk0aLKUSWxg4//Z4hSN/EmU8rPkM8qa+AB6enptjbl0KkY+FKdp7TtK2oCyJvM0d7RdHOVXmaU/pL+lx/XASkaHDNMlS5bgt37rt8zwmPs64SJqt2uDzpTNiCH0FJU90mk+9U2S2tmXRW3R0Ke+q5SPSRQox2gZIFc7R6FNJ6++GtVaBwUgbZxMibJCs3jL9iXblJ66auqX9AD1S4VyZCSlFKPoqUaQplNYj1LaNihr6CRmIpTBtDOQ6GJcymXGz0Yotycn8P7QCHVbD2VWP7fUh0onWUMZBQyWuU8+qlC+ljWTVGnZNG2HO6NNrobnJb8V1F/8sb4E/du//dtmP37961/HE088YbJDCPLiQoK3nMPcnS3MnVD3tp7PQ2svXqAHJLKNlFcNVeo6hpAPK+QJavBGlHpOHMQzaekQIIMxGTEMTDNB2iKUQwWaTuLeBFMxHmZMN79AcLb3QqO1DXSsNlT7CN/+9rfNH1Bb/u7v/i5+8zd/02TMHTWAfhdA7RbcGujbiG/Vnim9SaFTmkkiSdqgrKOdVKTtl8zpQy4dKBT1kEcPhuK2kLY+FFY0P4Lijmac7LEoZWiUB9KZKU2dJe9PM/2aPk5FnnG9g7KNfK3h7TptNH1QCHH6abLlmYdonDzXjOk5J5hv8dNV5SAsjNtgaPD6ELcOagvfHmoH8dO3vvUtvPDCC/ZA48tf/jKeffZZ29e52yUTPG/IozLMMQvz0syPRLKKIhlv/MMf+2CJrqmRV7XWVjlGs6GCkdkxXCwP006oYWBJAj0dnciVV5kfVSdzV+grT8/MoFv+GVOI1hhIW0IPOLQrOZmmDSFZWZKNQF+Mbgz7DfslfcFKtZdxWVfsOvKdNRWTFgx3gGwlw+6rzDGvPK/6X6xfcFSbC2pzPRzRYOjv//7vY2BgAM8884x9tV8TqPz4kivLvE2t4yC/xJv78zFCmIGvilalqPJsNFSczErNdfcg25GzDigDK51K2edDpcSTCUea9aJL7oB17K8NFpf2tiGaYg9rGiky1KJaIJ1/KaqdCAupxfO6urqwdt163LNpPZYuTemLwlYH+rpfpFK3OPZFFv715HqwZu0KbN68Hpu1+Pvqleih4ZrK5RBJJbWmq81Cisih1PBNpKZxDSZIm4/KNa3XSrwRxx6dzGqR9iQ2rF+PTRvvwaoVg+jKpRi9KYF4Xw1Oar+uQchkDLEkU2B7Kj9qJ51OcEdPrCSw9IBJ+U8zT5pyumHTZixdshR9vX3o6WO5dQ3jaoBr6eAANm1ehxXLB9HT2YV0MsU0VS+sQ31Zg/up3h6sX78B99xzD5avWYMcj6N6Kt3sgFXWkV4ZlTMcTybQy/Nr1q3E/Y/cj6UrlqGzuwsRreHBGyfo2ERZP/Uq64V1ZEmoffS+A++lRQs1EVxlK5UpaOkA2R/jptlOgxs3YuW6FVi+eik6ejqZP5aZmVUSLI5dK3R25rBy5UqbnbBjx0bmfylysQ5LV1VrYJoysW0BUkIDYtl0BgnWbbmitb4iSHRowIvXkAc06KfFnjdtWI/77ttOnlmL5blBdMZyrE8aRGzLpUsHeVnEDOJv/c3f4M/+7M+5/RbefXePPcnftHmT8QiLhRTvFafBoz6rRkkvXYJlrON7t96HVctXsQxZUwTVGvMph4g8IF5bv24d7mG7LqXTbgKR/+Io1ZqGfOvqu+Qp3sDKq0FM8XqOgnYF+XwD23L96vVYuWyprSkX09cUQtw9YD9zTwTEOvbNNfK3+rHYhjqht9c+H72eMkkzajdtWkW+zpGd2G/JuPoAhT0hN2skxGLBXC+mTJDulx1gHziRHlEwSaLB4iksk6XOiml9eptlIFmqz+xnUx1IRhI0VBXPXSA9YANhSJPo9snapNySnyj5EqegqpOB9CDGxY0glaD+0APDnl7Ky/uxceMaGng5m2WbSNZRBuPzz4R3UyhKn0kVhFicENtIHwv+Sbs3yhUu16Rcr6BUdfpTzKMHVOId8aGcHYNkUPO6ECEWGuJV8W+C9pegmdvizzptQZ1L0JjMUW7FKNfkH+U65DMlaWNpaJegfCvSHpTlKDWYTknm0kakTDR7XfwtEUt9mtQHq+w6Xakv4+utAvpo7BOJdMrZ8jwlMag4Ya8IcTsgHjRTgSQelImopY6qpTJ9nyp9CPmeCfpd3Vixdg22b7kX29ZvQyf9zKR8DF0g/UDRrw9BdHbpvSd6stTrGiSWilf6Sls8H9MHzdhN1L/0QN/ATMRoQ/A0bQnaAqQojQwNULvJELxAUMfz+WzasncTmrVwN0GN7EnFp0Cl0yyKRjPcaqEMPTNzI7b1aBL1WBpVfUaUNkddTote56KgjzIgwXhKRV9I0H4mwm1zhFKKIEi3GyqRcqty6RPB8tfl5CvnEWjaY5ZnNXAjI5pKqZ7i+TTLH0UtVmfH1FPuOlKqCL0mluxGI9rBfa2bxXqKs2tReSVqOSSqeu0lY5835g2QrLFzVjX4xDgxdsBIHUnWSbyuEf40OzYNu7ocgap9xjjbyNJFyFh6lWgFsWoH4tVuOpka+GH+mO9aLct2oXBoZFiCBFKNCK+t2yeQ69GlPM/8aeYWhYoGfvRkXYu8RzVkznh6mqptvBFHup7ltVSyzJfy1tCigPVOxOpdyNbpyDBPEhx15kfXxZiGlLEG08A0Y0rH0uL1uo8cJ9VdJAW9UldnHdkzXAqmSpTKm+lUo6xHvWetUbIqFXhVM9LSvJb1xDRU51XKsxTzl6vTaeLWPlNOYZa2euL19HvqaZYvwevQxbruFOMhRUEY5zbK9tLwVDWhtoyjofnkdJpqelrH/DQYr877RJnvjIQt2yJuz9PSbG+6VcxLhul01OPoZX3rdYt6inlurr2QjGjwTE2sOlPd0Slju9dZb0YxPb3I2rvp6WpNkyLomPUgFe9BH/O2XPfNdSJ9/w5s/8e/jC/8Pz6D7uUlTF6cxMylKtPMYWDDBjz27GP4/BNb7H12Wjso01qq6cleUrPkqlZPdQ3M8Z6xWg/bguVgHYr0ym6d5aeZxnKK2HJstgR/xCEZtluWBldOVaM2ZRkbJPFSXLweJ29rQDOWIl/SbWV6WlNF5VVc9Q8bLGN6+tKoXj1JME6EeW80uo0/beFh3ktOTvDpQ4jFDy+/NRDSoByg5GJoinKE3EJSX7U+xfbVIuc1nqtFsyT2IV4X4XXkEPIi+YJ8IrmhS9jR54lhjhxvLBad8ckD69gWf5fD5sxAyUn1WZvlxbaae8IoGc62poRi/6VUpIxIUmbVMEhDcgnbN065wvhMpM7z9SY/iNjY9t0Kk6+U/TrXUY0iW2H/Z1xZDjVFoM6JUvfUYyLuU37EGjSSlaaecNOCVS5imhFUK1JPFEyO9lEed1GO2Uw15kOaPaEHGAwJ8o7fD3np1sKtp+aIDWXUkK3Ajt7QMblG5/T0P8L2jdUrbPcyt1XqKi0V4D6AkqSejNMGbUiuUBPXyQhqO9kWaen+eo4ypoP6KcXICTo5ceok2Ut6vdHxsHP95Qg1naEQIT4ignLDy0NBtoukpqxfMqcNQMWTGnhiaESDs+LPLlTJp/Ua7THa/RENZslWpb1rNi/7Aq1CpBneYD+oajojeVh2Z5T2lda6k12lh7gJyts0yWw03i8p2UodK2uqTvks1SmZKflnX6lrks97EDr29lfQDtOv9ICn0DoLEYT4wfFEk0OknI3mOUW8pyVm9ODJxpHEepTJWje6QX+IlgN9Pvp+0gt1+mf09xLsHx21NdyuYJwkavLN6FslpCfI7xHyufkrvC4ad36l1nHUOfW7uumSCOJ6+6eaRLVJ8uwa6m/yp5mPlPRDnb6aZlBKJch81fYuZXS1Yog5tlZ1iBw3OMFI7rCn8k5I6ilwjAyvGT0ivaJiVysut/NXLz5YP3S71l/n8+lzTkVjysuV1RZdVflt6zYyr1Ub+rKlFI+d51YOgs4rXowOhSgqY5zhCnSKsnnT5kZn3L2UhsgdO5Xq/mwEXLfhnfXSoJ1t3seuiWgUxKWta/XKgLYahNPgpaZV6wJTcLpGp7hvfwqyYF3HuxkpXBGVH3dPqWM5qrrWNnPXi3jMMGXJiMcil2/lb540G8Dqo1kmpad4Lj3VEO/D/Fqa+mkmKH5zc+zshF2jAUtLQtcrPbuHyqotz/M+vi5dWgpv1p0kocKMVDfadXUX5/VRn1fbd/fS/e2ZmyJbUtwqT5bfZhlIGvTSbDT3BdQmMS+aEWXTS6kcnA0lgU6DiQfxRBLdy5Zh+2OP4iu/9ot44qnHsHXzNmzfeh8+9ekn8fkvfhGf/dxnsXnjChs0UN6Ub1WHqtPyYqT7uTazfFgwf0R2TmGOF1xeXZ6YmpHxts4zURF/SYTuxetVL/ydC1eylgHLhALmNiT9ulQZYS48xJ0L8Ywa3fG1+ED8xDZW81sf9K2sAPEo49mfCzU20qlmgNKYJ8eTrRTiZmOuNZrUeuRg9S850GxHyQ3TLYpF506Wo5MTPGzKQidfxBu6RvEsoeY5aRGmwUBrby8jLYRkMk1hOu+cM5u+YHngJkhMMdHMj9KyOPZnGrmZBiOGWGAELSy/L13rjn376OGHiQvbn9+KpH8cDzl+8m3p9LBiSp+IVxibidg5puDTcTS/FyLEzwovS+ZlijjM8Z7xn5Sa8Zr4VbwpHpVdqIfp4mfxr64nGc/yLH8Y04XpPNMwf0F8rbRN7jm+Fs1Jyma/sDg8/1EpRIhbBXGXUZPPTH5Lz5tu1z75VvzOP3I7/2QTaCXQFONK1/Mie3BuPcliuTS4r0tJFsUS57942qel65tndXsjF83iyLe1NF3i7sRdCqu/EA7BJwNBAal9J5Qd2fRCGqTGdE3y8T5p8OXzZff7rU9RgnGCcYPntG3d9/DhnoIIhrdLw+97+H1/vpWCaBcmKCx4j1a63rl25ONr20rB8OA1bcmMBuZXwlDHJr10bLmeJ4vPOEqXW0/unK69+n5B+LAbDf8gPnjeXscU8c/zjowh//Qtm8licHAQm+7ZjEceeQQPP/wwHnzwQTz80IN4YMd2rFu3Gh1az0bZb/6xBPbrj1zelE+lfXV+r0VCuzCP1nPXoxCfPLS279yxY7D5YyMLMl53rx+7MPG57fOPMSydEIsHahsPv+/a7voUROux0BrmZXxQ1nv4NE0um3y++l6iaEwPD2i88togGwXjt8KHtTsXYiGh+iexrfy+tZltnQ7jznz4daiVd0KEuNm4Hn95PrwWPI/eCHl51i5Nn067e/mwdudChLhdaOVLbYP83o4U5+NS8PrrpRtiHuGgVwDtmMMzzUdhpnbh14q7GBEs37WotS5u5LrgNa31eK2w1vDWONe6ZjGT8nytfH9oPdrgTptrndnc3OrPxTGHW/eaux+3+vPXXYNutF7b51dhV5OPp7W/fDw3cOxEkI7jsbjdd3Bwma29tWb1avuqZ1dXhuc0lZ7xGFdXsAZVwjnSnxtc8Pd09/gw8ve+Ht1MHgtx58G3necD/hj5cDvHoOY4mCO7zpNv+wDZcYjFAtc+Dr69Pgq1u65dmHjo48oTrQNna17q2P8FzjtcHXb1uRC3Dqrja1Bjft/+vP6W5mru88cd2/kPpxAhbjXa8VyQ94LhHj7My7lW8udb6Vrngmm2oxAhFiva8euN9IVbSSHCQa+bjnbM9UliNl++dtQO7eKJWnGtc8Hwa51rh+A1rXGuFd4OwbhB+jj4sHRawz4Yr3nc/NPx1SQEZ+C58KvjO3ww7Q/CnwvGu17860GTu3StX9xUsOPmwJfWx9Jn3PX1Hg1+pVNpUpL7PG+xm4MK3M6Xxp8J7pH8wUdAsIwe7cJC3J2Y4wUjC7HwVijUqBltnjNbcPVE2RCLAL6Nr9fng3Fa6VpoF/cDNPd3bQTjewTDLFz/weMQtwms/+ae7RjNt4fOWnOJmn8fF8F2Dts8xM1EUJbcKG99lGs+LE4wnSCFCHEnoR0PX4s+Ktql4SnEBxEOegXwUZlFr2Z5asVHTetuxbXqT7hW+J2GDyuHzl+LTz4YruP2ZOusBZ4qX58+On42XlYdzNeDfXWxmQ+lq/Uc9OUefZFRA1/VatW++KjPWeuyOCWVSF8ysWvsV1v9ue2tQNh/Q3wQ89z3Ybgqhg5CdrrtWJx6xTPHjZGK4IpxdfitkoMhPgyqdzcHeZ70wCZIHzzvqDX8o0N6KtRVIT7pkOz2FCLEYkEof+8cfDwNe5chKGiDwtYzesjsHx2tdRlEu3MLVcfXyte1wm8U17r2RtO8kfsvbl5Uvubzpum9goqkUolc3lkGnkskEogn3BRgLXxfa35AyF5hdLvt4RMLEeJWIOStOx43S0Z6mRykW4dg2s39m1OMECFChFgw3Cx5eetlbogQHx9BPg/5dPEgHPS6AfjBBE8hfja0CoDWOv2wum4nQG6WULnefT8urpfmjdzvkyMw54W/K7ObsVCvM9wGtSiOGqwPfYe6OWNNY2Oa4aXn4RHGlcDSGa1+4sj9WujHqKZPTt2GWAjMc8sH+2wwxHFvOzBU69g117ILcefCy+4gfXx4jrkWecnn9t3ajMGwIIW4kyGdFOqlEHc6rsXDP4u8bL3mZ5O5IULcenxcXg9xaxBa3h8D3ihpJ9SvFf5Jwc0onxcCrcLgWum2hl9LgNzKem/N60Lidt33ZkJFCNah5yMd+6+PafCLsVxki2RHdqitmtfvO8zvhQixEHD8e22+u/7ZECFuPm6l3gsRIkSIjwNv610PH0d2KV1PIUIsVnxUHr0Vetz7WaGNMI8FHfS6FhMEwz4Kk4T4aFjsdfuz5E/XfpJ555NavmC55n7bzYJRsDYukmEu/hzNb0IsHnwUhftJ7sN3Eq7XZu1kUdhutw+f9LpvZ7S3hqkOrsezdxo+CW16I+3RGieUI3cXwvYOIbTKc0G84fkjuB/i7kOw7dvxikcw/Fr8suAzvXxGbiTTvnA3g24E7a5rJcF3wHaVeq3wa6HdPT4OBXGtfLVudZ3f+jRa02qF4vs0bgQ+7Z+FbjSdW42Fvl87tOahHd0o2l27UOQRPHZ8RbJXGwUX7mNH9H6jxfXh5F2R4luQztspQ/B+16IbjRfSxyeP4L5HMM5HkSse/vqbQYsV7fJ6qyiIa7WH1wE+/rXitaa9GGixol1e7zbyCPJWK1rj+n3PgzoO7i8c6X43h67Vn66F1rwE0XpuISgIf9zunBAsq9//KOX36Ya0cHSno12ZQrp19GHwcVr7v7Yinf8oMkEI3n8h6Gbgo5SxXR7aURDtzi9WuhaC51r540brb8EHvXym6/X6VST4Ai92ullol/bHJd/g7bYfFtZ6fLPQLp+LgT4ugnV1M+vpRtGuLO3oRtDuusVA/Jmj+XAf5I/rgX2S/rjlD0mFC8YNaSGptY+0o3bQta1oTftW02JEu3wuBLWiXbtdrz2FdukuBlqMaJfPu5E8WnnLH7fStdAu7TuFPiquVSft0l5o8vnwW78vtOZ5MeY/pPZ0p6JdWUK6teT9+1YE+7/v98H+L+j6IFrTvpPoZqJd+p8kEtrxRmvYx8FtWdNLGY7H44jFYnPkC6KvugX3bxb5NK9H7a5rJcVr10itdCO40XveCHm05iF4fC26VbiZ5bsR8u34YXS7cL26v1a4EAxrV+5WakUwXU+qh3bX3jxS+u2oXVxH+mojorEmueOIXaPDBqmZRoTxI7GryF1Lan4F3l33wXuEdGvpWhDPBbftEORPUWu/bUft8vBxqfX+bUn5bNIHwPNzdO1Y82n4NK9DN7uMH0atUB6CWyGYv2C4EAxvl/7tJtXnzUKwrNejG0G7vN5tFGybdnX3YXUaPL/Q/eZqHfez0c3CwteBo+B9te+PvZ1/LQTbT/DXXo/8fUJaOFK93ywE2/x6dLMQ8sztIaG1LYPte73wIAnB/n8tapeHW0nt8tBK7crTjm4E7fLwSSKhtU5ajz8uru2lLCCChdKo8M0o2K1EO4ZupcUAX4++LoPHPizEwuF6fHKtcOFa4TeK4PU/SzohQtwMtOPHdrTQaJeHVroudNrTDaBd+q200Gi9pz/+sLz4/Hq6G9Ba5mtRiJsHX5+tW8HXdzAsxMLC25Xejhe09W90tNqdOg7GE4Xtd/cg2GevRyHuTnySeKFdWdpRiA+iVW/8LLgtg15BRRdE2Pg/O1rrLlif16IQdxLUb24GLQQ+wj2vGVUHmh4dpBB3GrycCcqbm6nIbgfa594zcJDuLHwUnXA9XR4ixM+CVh4KHms/eOx5MOS7xYHWtvLw+61t1ypHwnYMEeLugPq67+/tZEAoC0IEeSFIHwcLMujlGTmo3IJPfjy1InjuZ6UbQbvr2pHP+/Wo3XW3knTP1jK0OxaCYa3UWo521O66xUA3inbXttLNLHNrWjdKrWnYWlY38Neazhzxek/BtG8JXevvqnhqiyapXYLk48z9Kbzlj4EfJIWHtNhI/Oe3QQqea6UbQbvrPi615q0dubhteK0u4nnbBqglTl3EfZHC2t3D01XXLiD5e7fmx5POCcGwWq121Xm//SSTL++HUbtrQ7ox8mh3TtRaz5+E+g6W6aNSu/QWktohGN4a35+7VviHod11IS0OasefH5fapR/SnUnXas9rtbUP9+duBK1p3Gq6EShesCw3Sq33utvJI7j/UXDbXm+UkRykdo29WKm1EdpRu+tuJbXeO3j8Uak17db0Wo+vRa1p3En0YWX5KOW7VhrXO9caNn+svvIh1BAx7twAV5OUTpNcXJf2wlG7e6pcnigXmuSOfZxmuYLHjHT19f6YDnhgP6TbQ6187fd9uIc/bkf+2oWidnloJbIaSdvmsb+WPBnsX/zhebc/d4+5664u99z5AF0rfCHJ5+968Pm81vaTTCrjjVC7a0NqT631FjwOUhCt1wePP8nUWie+7K3Ht5ta8xHMnxA8DlLwmpDuPGrXph+X2qUf0p1F7drVkz/v5YHftlJrmncatSvTh1G7dD7pFCx7sC6C9HFx29f08pnXtl2hbxYF074WtbuuHd0stEv7ZlAQrdMBg9QOrddfCx8l3kJRuzZtR3cyPjCTpA01Y7bQ1WB1faD+biqxntvl7QNfXpyLx/zYeUd+UMEPIlxN8/GC8ecHFQLXh7SgdCPQQpX+Qybab13g2KfVru+2UvDePyvdEKzffLDvBGdPWqQ24Nnm3o3B10nwPgtBQfg8aBtcaNR/gEb7wTiehHZpLwZajGiXz7uNWuH5SAjyWKvcCJJHu/TvFLpZaJf2QtH15LSgtvKyw8uUYDu2S6MdBdMNaeHoTkW7soR060l9+noI9n0vD4JywUNptZMDrdR6/1tN7fLQSjcT7fLwSSKPYNtfa/+jIhJj/WmnGrjRz4JghgXN4pJxIvzJn/wJfvCDH2D9+vX41//6X6Orq8vCg7hWgRcWwfuywzb3HIKNErXKsyNGCsZb6JyrU0lABKF8qv4TiQROnz6N//yf/jPOnD2LL37xi/gf/9n/2IxTswK4a2VsMC1XIkR54JrAldNg5XRGiTvU1p/1928e28W+JnyYj8vwhjsXmVunycdVqm6/EXHn7GjuUu7wWv05+BNC8zqFcdelI9KerrNdg8VpwqfEWnT7qhc7zyML8FvCLnMHLg8KCAo13olld/dusB4V5u41f0+lR7J6VFwfPl+LaH7JKdKsJ5eGT6d5PzuldLTTjKcRJJ8ig1xo8x5zx7zLXP17uL1gXuYxH8vBt5D22iFYHx66ojUdwifAU8G0XExXlqvheDWI1hht7hJiAdAq/z2C4cViEUePHsVLL71kcukf/aN/hMceewzpdHrOQGg1dhYC18p7EHX1a0aL8Mf1U8pY8qh6V7TelEiMo7xbapRVjUgz5lw/dtv5D7UxDtOzdF0Cze3tgfLi6z6ov48fP47du3db2y1duhS/8Ru/YVu1la+74P5ihc9es4Xm8IFcswpUCxaun9Y2mZO5rv1tz8fROd+I/n46tJv7SIrmTtK8t21Q9s7HcntXy2W/766bRzDOnYsgD7q+0awn8pfkx7/4F/8CnZ2dJjsef/xxZDIZkxueV28HrHndbhPzLTiPD28fFVVFt5jNcs8l1fDtTb3YPOdPGe/xQtkLrur08+H3u5lobbfWNvRy/Xvf+x7+7M/+DPl8Hv/8n/9z/Nqv/ZrJGp3z14RYrCBPia3YTE7qcbfJiwr0e1fJK+66MyLuNdvYt7XEoG918z/8gXCVnertSh9BaTV3Zfdqfy6AvDQXT1C6wbTdztX2tf8NcbPhZXiwf/vBIB/2ne98By+//LLZgl/+8pfx9NNPm8y4fZjPq8ONckfrdbqS1871kyZ8XTBYezqriQE6UH/RcZCH3b6dbB7Pw/dF6yPaNb62nfmIzdv7Q6EZtKggfhBveJ1RqVTMV/iDP/gDDA4O4nOf+xweeugh9PX12XlRO/4KIt4Mv+mDXkEmlhIT9FRf4VJyf/EXf4FSqYRf+qVfssGYarVqcX1GFc8X4FqZ/ziYrxBtfbrzZRZ7yfCM0EGhmY9KnR2NzJeMVBCvM6TO88pPtIJatMT6Uhr9qESSKDJcQjwaodEVrdH5qSLRLPtCwTOHL6ffqg2y2Symp6fx4x/8FBNjE7j/wQfwwKcfpoHIUldGFJk10sMayKASbSCfZHlY9hX5aRv4KjWyqEbSaDA+4lVLu1FLsa0aSGIMicg0q5QOa2PA+lkjUmBaUl1xUozEP9aN1X2McdUpa13c5FjjZaQwbHmtN3iPRga1eifbII1KvIJS6goTBNK1BNuAiUfKzGuZ+zFEq102oBSJlHi1yhs30r3L8SJKPCyhl0dx5nMWmfq0u67SY3U1Gx1nW5Z5pwjSNCbL1QbG60uQTqXRXbmIWK1IGzOKejzGNm6gmNIT5iTqBZaqnrRUY/U488CyJS6oCLw324BnitEsZuIdpmP7C2XyTZl1kEckynphGrWIjHTGrpBfokw/Tr4jDyXqFWR0X/6V4ioTkKrkEG8kGcI6YoJWt/GLdlyJpHhdmicyiNTT4mBkaxH2qwoqKdZ1ssI0WXd59rVaFbOdRecYsD6jtRh5mzXGfDhhqrpjUtGqkTI/Z8zUOvmjODqWcVolvxd1hkcp/upciBAOrXIoCDmtly9ftkEUbeW03n///UgmkygUCiiX2b/Jo0F5thCQvvmw+5VSVVRQRboURXcpZT7oUPcUe0UDA5M59l3JyRh4mrKU/TSR51VegVP8sY/FGwmGUZHLuJlD8L7cl+Dw+63nPhCmvndzDEPlU3Uvna120LH0tOrl4sWLOHXqFEZGRpDL5czoGBgYsDiKq/pLpaQX6qbXb+cAxLUh+ezyFWtQxqkeqZtcjbKdWAYHymZGi9hDoZrjC7WJ9AHjVdl0jTp1GNsy1ZhBrjFC2R7FVCYOilleQt1AGd9AAmUqRc1Q7cvUUCF/o5JlLhLUK1VUU9RdTDuTz9pdS4kCqrGK6bW49B0ZLEJ9KNRiJcpl6T/K3ibvNGr9NthRjdWoB2g7yWa5iq/uHKiOReIj9X3xkD8WxE9eRvzpn/6phX3mM5/Bli1b5vjV25o303a8EUTJS85JIX/QqhYv1cy6Zj6aWZEuFT/pIZ+4cH6gwMEdsR/TdlD5ayjSFioxnGnHqKHFe6WlYhca8JPkoAJ1O60NkjCclY3AOqomGCbmJV/TXlpIBGVosA18mMrV0dGBXbt24Y033jBnRg88nnzySdv3bbjQsj/EjSMif0iyMEYOjNP+5HG2RrnEftegrSmZJ/YrJ2nzKppsd9qkyUae2i9v/WMi4SY8xMnX7LDoKEbRWYqxz9AGp0ys0/aN0N+wGdT0NWK0bxMm387T2qSnVs2hXotTXtLWTrK/sf/F6hPGNzSO2bdok9ZoE1MOS5YmE+RL+iWziQlU6cNRSZOSzHMSncWM5aUWn3a2r/ks8iVC3Ey0ygUdi3Qs2S65vWfPHpw4ccLsiK1bt5psl1zwcYLyZUFAPomQnxzkE9EeEJFLBIl3tyP7S3zIAAt05IrqIlFD8xQ1hHzhuvQFw9O0l2oMK8oXo+1Am7EQLSCdod6vzFhZozHeX+lXGYeyXXVQkC/OyxPUJzH2kTrPyxdUzTTik3Zf+YPib/nesikE+dAa5I0xfpRbxdc9Fxs8P/h91cOFCxfwzjvvmK/wcz/3c3j44YexZMkS0xeC1ZX6fxOetzxu2aCXoJuJlGllSINcyvi3vvUt/OEf/qFlXKN1YuwqDRvBZ1bX3WxcnaYqorkbgMwVrRMUjVDZRhIUvnJMGkhTCMYo1KNVGitKh8caKKlYGfu5n6SDI0NHLKw4NDKqJWTFqLcBrfWnYxkZU1NTmBydZtZq6OjKoW/lUuTzkxTtE6wPlpkGfJ0dpEwNUUrHKGiqWDFLw4rtVot1WYeqNOTuFV0XbmTYpnGkIxNUcUyXCqhc7dFwDJmKhryUouowEreObscSFNEpt98c9NIAVhpXeE7CTANnWVInazKDSqyMclrnNHYjQ049Wc5VGVFq1Vhz0EtDW24wk8qORBGAcqKEMpm7COaJeUg2ZpFuTCNei/K6PuPNUlJKToNCdOyqGkqKYTa+0nixt3qZTV1g3tmq8RjNSyDP4kSj/ClHkaTqjbO+IjU658xtNHFJGVHpLR0b9EqwfKz//jwFjgbmKMxkwFYpSCvNgaKknBrF16BXNEIhpkEvxeNtmoNeyUqH3ct41OqS92kOepUjSd6PSpvt4Qa9KEerzAM9r3JiknkvMc0EMkxDfXAyPYNyhfVHo4DmMdOlidIc9HLOIMvLOmlo0Ishc11lbtBLgogUqdDw0WCjhHk46BViHl7RBGWRD9NWjo0GvkSzs7OmuDSIonMapPdOq79moeDz2ypDgygkKjToKVOrcXQVk6jQeLncPWl9a8l0F1LlJNj9qBMalGw1Gtgzdo6F4dUsk+SPBsopc+sxr6D9/YL31X6T5qohGM/vC4owr+x/Fvg6l16WsalBBuVf4RpsEEmf6/zy5cvtnJWPULspXCTdfr16vF1oNI1T1R81m20l+QUbY5Iu1J8NHJEPNTDWHESyqmGbKY4GvvSgqM62TNamkGuM8ipgJCYbgu2LLC+XbKYTSD2puumKU3dWeWVN52hj0BAtx/Pk+Sq6Kt12j2KCxzEaxEwsTkcxwpT8oFc1VmwOejlDV2jUqMsYUomx39B4vZMHvTx835csCNqF2vf2pAZgTU/39s7xmo97OzA/6MV8s/3VJ92gl86SccQ7yqNsBbaPczcUPN9HnLaNokT7wvqcHJUI+U9OCYsmHqqXNbMyTiuHMoc2TZxpJZrNPZzWgAP5kbLJD3rR2HEnFwhqN+XTw8sTtY9vV5VND2HHx8dNVvT399vguWSL4nn5fzvbM8S1oUGvCPmOJjP1oR4ZA53ka4XrMbioSt7LR2Z5ju1YT5FHI0g18khECpRT9DoSXdbWeqCgtLrKCcrABK3jOm3UCi162vTy9dVnaNvGGx1MX3brebOZ440uXpek8x/FjAbHahXkUm6At2ETFlKUsxlEa7RNjR+ZMu9f7pih7awHGewfst+ZRmfRPXCoxaZp+1abOkD+X4ibCWvvAPyx7+uisbExzMw4m0mTNTTjS/uyQ0z+NWXDgkH+mT2kVF5lLzQHvcjflnufFbMryDcNBti+TriTPr91XUOyhx7sKyqLpjdEqSfS9N3kp9WiNZTiZYZqsk3e6sT0Avk1pgdsjCfMMp5gg15MjymaT2l5ijkf2wa9yN+6r2wNwVQJ8xhlH5HnadbPIhSzfsxIJIhXZA/IZ9AMQL1l8Mgjj5j+XxSDXoLPpDKkrfCNb3zDntANDw/btEX/OovgM6tj7fvwm49gOef31fgxOvuUd6hRwJbrEqoNdJE5gTyF6xR5WQZLgsyUZJk0KktHjXlN1CfJuBSqbKBKlCxYmzdEFgpqXNW5KAjVo+p5dHQUb76zF+OT01i/YQ0eeGirmf6piuugDT3WpjISXzSYf6ViA1gMEEtpxhfdPdYDjRbFrWrQg8YZw3gTUzTqYGJSe8KjcJMP6lg0yu1dngZSNPCdoeeJ8SIVKkmNVHdSKMRtFFozkPQkPkLlF2f62lceZuMpe7qkS+UQyIhMUeFp8EsDVCZSuK1JcfGW8UaJcVQSV86IhEc0ZYN69USSN4khUZuhoTjN/QRKiV6UaIjF2Z4N5lX3liiR6ZhnW2uAMFWtUXlroDPJ3KXM2WjEJyxPSZZZQkUGrwZO7b6sFwmhJEVclCnVWA49nFVaHTQGxC+zcfGOBr3YXryvaiafUJ0xjLxmRizzLuEmNBLDFsfMZ+vFcbYBFT3rLsb768oKHahqrIxENYpcMcG+mMQ4ZWZZbad4TCvGvIisdUxYc0uh7l8rnYOenLlYJN2VfcFqhc1sA8QhQrSHVzzaivRKi2YLXbp0yRyfzZs3Y+XKlSanhCr7n9cDCwmfz+uhJqHJbMXYPRIV6jj218kM80o5smSGxlmJjgDP59NMi/05WnezITX7izcwoyMub4GozBnW7tjB7ze3NpjfDq3hH573G4FvI+kRtYH0t7Y6lkGqwQa1mV4nu/fee63N1E6+7hRX7afz0vut+uj2Y76e5vWQgx1ZOUiqA8k5tq9OKHh+lrg/z/JSduvJaSKaYHNTWzXGTAdGqKOqNWonezKrhzmUsY0i4mScuB46sJ5q1LflmGY2U59E6bAxQcl6PdDRjIcqnbkaFVujabCmqryW9yP3MWqGOpO6NupmACdAR4HaSJL8TnXYgv3P86DnR/GVYPZFuYzvf//7xnviQT/4Kj7UNbfWfmwPN/PO8Uedel3Qwy/jlTnIGnDx5kN1jYfajtfqgZ6lISe+YjNGizJ5WLZMsYu2h2wk2qq0iYJOix6aWXI+ccZf6P4XbKtge/p8KEwzRzXLd9++fdaWDz74oM3okEOjtgs6OiEWHxL0g/Rwv1KjfIrnyK8JJPX2Am3qKnm1FtPgVwmJGOWd+LnWgShlYZSyS/1E/DqRUU+Qm16ywbJ4tYeyrYf6lLIuPYNqXec06sXkjQ0cb8dkU0sGakBNMpIytEK7Xd2lwWvEcXYv9SH6auavqY9o0Ctepbwt2iCAnAPFidKmTlecvKzRVtZsWdc7m50qxE2D+nOrTPBhXnZr6YRz586Z3bFu3TqT7ZLzOtdOrtx6iLHkAZP55mZ4iVplk/hFPKq8tebPxY2Q3+SfkTFpH6gflFCqT9MmiFNjZxGhrRCt0h8l32tiwmiOfm08imy5QpuBfY76JKY3e9iBys1JNUnq/bhmBOsaPWhr8rt5gNFZ+vW0PzXA2+iwvJmOIBJ1+rbUH+bJyX9cZFBbiwc8X8imnJycxIEDB/Doo4/iS1/6kg166fXGRTXopYxr65WY1vTSu/zLli3DP/tn/8wMY50XfOZ8Rn34zUcw3avvEYkWeG+Kx3oWZc1CYh465KBEKigmJ9ygVz1Focp81+kMiPGY7WRtkiyvGWBxVGnsarRXgzYLiXZ1pmM5Hqp/vUb0Z3/1LVy6Mownn/wUvvKVZ5GioZ6oOEfT9VXWvYorQz5KE5odTgpHs49iDb0+EUVBxiXvFauXqDBUg2xbUx5u5DjKTlVMqDPxDOtA0ynVBSvWvg0bFLKW1rR7PcW0UPIf0y7Z6yB68YPxeGMNxkQ19ZNKkalazEI8zTy4PCuzGgfPkM9sFh4TNpHEtHRGSNRnuEcBYwNQSVdQ5qVKB6Ie12AU71ebJU1TSLD9kl0osIOp/CqDZoGlxcdMSwOaujZhg2wyNhMMSzDv2pdwoWNC0sxTy4zlLgZN6lZQhkpe89DMUKXyV10l6TjXeb9SkkYD61ZlTrC8il/U1G9en+CBBtLsCYI1FDfxaYtjN+W9rB00uMb9iKYsEJV4ieVm29UiyJQ0uySOmXTcHHXlUb1StaSyODTTtgEvH9bE3BRfQX2UccgTdmRPtkOEaI9WI0WOjt7Pf+utt3D+/Hmbqrx9+/a5dXm8cRNUYIsFbjYQy8Q86pV3DZLMSk5SBvQUKPcp0myGKZ3UGPOv15Ulg+sqC0l9zg1c0Mi+1uDEVdXV0g/n0Bp+dR1/XHgdEqx73x4apHz//fft9QPNztDakN3d3Ve1r/a9weKvW6yQ1AxCekpwrzg6fao4shPdGWfT6MjKrAdd9lBMxlnGxWmMU3eQH6RLaJzKTtC8YMn8qj0EpHyvzlLmapmEFJ22nJ2LRGh78PJEJWnOmPisxrhabqBOu0RI0xYxu4KyuN6grmTG9BBKF2oWhQZCJNHrNIzvdLTKDLWFSHypNtCasHrK+wu/8AsmOzTby/Oszi+07LDBUbajGsOv4SeHIggdeZ7zZ1p7scWoUk5YEuQttmmFdqd7AAY6QBnyAO0s403xqgZHucP6chPDxS+0MRhuaxU17YWFgtrNy5BrQW2j9Rw1cKkHIL/+67+OL3zhC9Zuut633YelE+L2IKrZprT/67LtY52o1+SMx1CjfKrS6K9RCWpQLEW5pXcvoJmq5Gk9I5XZqAdHUxnxbwVpWsc220txat2Ua5SRqRIqtLHTNmilQWTZzCTq2yg6eF/yRXyKvMJ70fbUwJfuX22+Mhan3NX6mvJJzPlndMlYGdIV+h1Kzda9Y2r28Jf2seD7jeudC9tv7laYjmWf93Ljueeew9tvv20DXc888wweeOAB81+r8sma8UQLB/FP837GGyIv64OQEBYCefNR7DpuauwDUuwSb81Br1pjiv1JnEh9XiG/V7RoDn3Bag1XOnkdz3VWK0jZxCHlxU2kqDTfEtDDLnrODGM/YN+QbWC+ouJGNVFH/SvBLGgpBvq9TE+5iZtPL/9b9sLi999kQ+uB6ze/+U17QP75z3/eltdYNDO9dDN/Q70ioUxp/4/+6I/w4x//GPfddx/+1b/6V/banYfO65rgfjDDNw++nPPlNYEoREpkFT29T5BSxr5JeyrfQDHhXtnTSG3UBgAYk7WnOPGKnlZUbFxA6z8xFhlqYQ3PYN15KMzPspNz+Qf/+T/j3MVL+NKXfh5f//qv26BXvJRWUdhnmwKfCiVS4zamJygRyD/TGLK9CkJjrsq9BtPkpZZ+Q6PIjKGaELvJ9ivHFFdiQGGuk9WbgkNGu2NL1ac6ncI1rVkDY05wRCNuyqYprho7uT0dYv3yTwpOg4sC1aEN3iSZplJR/jVgo7WxqsyTkKrIwahR0fK6mAa99MSJgpPX1DQqxzRjNb3C6p6aFlJ0UBjHvdPvZl4lVbe8QcUGb+tIaLaa8iRFz4qQEo02nGOiITurCd5A+RMvlBruaTxFmZVLwsfIos0ySeZPzk+E17LskYjKyigaxFJ+LS3Vta5ztWevkKpNLD39a3aA4zkZxGqbitYn4LUykm3mN68t0DkQVJKmvxSABg+bu4ZghOaJ5sbYzAx9bprtFiLEteDlk6Cpy0eOHDED58yZM/ja175m7+f7J3oiybFbI/8/OoJ514wd3ye00WxNdS0NaGhwXDKvTsOiSlmh/Mcp5ySD3czTKI8pU2S0c58SztIJgqWeS//6mM+Tw82pq6Dj6cvtdcjZs2dtIXs9bdMC9mo3vZbk4dvMp7E40VpvV0Py2sVw+Vcx3B7PsD7M4RJ/so315Nf4le2ohyqKF0WR7cry17UOBaU9m9hUH6lRjiMhtVLXABfrlHpMs4WVtlurkqhK5lOeShDrlUUGUqNZAnqApAdNFl1/POceJsneEDfpJPOvhzN3MFSnQf4TxFOCwsWPX//61433/vE//sf25FeyQ3amrtF5OUoLyoNNXaj6t4Yh5nM/j2CO5s97nnOIlEssp3vI5vxxpi1+sH89dNXgp2wJDXA5WaN76sm92FI8PH+n4B0XBr7dfP0H21FQuF/IXq+3/87v/I69riIE4y5eGXL3Qu0j2eVe+yb/0d+RTIzVU/QLKPtjmlFV4Tnyp2xZ2at1vc6t/sxg8Tp5WesTyn7VmxriXVqojCPbW64HbddambpS/Kxz0pNM28SgHA+GxbTMSTMF3kN6WA+fxT1a5MNMe8nqJuTfRhO6m5PZ9oCep/WoXjdVzKZpbdBdQ9x6BGWFZPzf/u3f2oC4Xm38lV/5FTzxxBMmyzWOINkfHNRYKDh56veMU9xhAPIZgxyjeI6rBG3lW3FrvCYvULqf/B2bsbMR9h+ts6x+oreRhNkUNT/90hT7kZ55KDyigTE6bnqwKmiNPLNAG9J9eoDGXc3E5FaDyrCBLUVm/2Sgsxd4nfqn6Sz1R+crL0aIJ8Qj2spX+Pf//t+jp6fHBkQ/7qDXLeEgn0ndUJnwBouYV+f8miAyTnTOk7/ulpIGK4za3IuM66aka6CBFWiGpwwOispGmiykBd01u6duAwqSwWIyVFnpNbozTCNKJoxg9oNp32JS3fn61L6vS23VDjpXLmsdnRnWf542GoWMuob6BAuihXZtoEaaQOVmZ+Mlrrsy3K3xVLEBnyTbTtH8a4Q2yMSkZKBrK9aSMpGI0FCS5i0xG4wg3tC9dDEPmJaNqukVkLoWeJaTqKvsRUqmWzJbUgKlGk2gHNc7z+IhpqVyMWXNQDPlpoE65rneKPOeWhPAhtXoaDCBItuvWqE7UmYYyyLngVfHqFg1E0Ov+Wk9sWo5ionSJArVPEoV5loNTCFUl/NC0lCUclZv1hFTMh4QEtWSkdKu0uGpMU/1RpHpaoq3hvWUZfIN665SZt2WWUsV3jc+i0aSTpCEkKqY9VKlA1TTDC098bUw1aBmz1EI+qKyvhjIetNTMtay2kvX8lhOkmZ4KX9qY3PUzUiRcOQ/q4QnjNQMGtcV1ZgHPWlTPq3e7byUkdJonnPMwn8S20sU5MOQ7m7ysicogzxJBokk/+Xs6HUWrwt8fEE6o/XahaBWBPPkoQFlDbTLyJbcU/9Ksn8kKfgiWg8kXqTOcE+ctUCpXquI6gLKDBn71hdN/qlvtckH+1bb8A+Q6idI7eJ8dPJGgvZVdh1rqzZSe/k1vUQyRIPX+vryFDy3aEj125Rl83U9X4+mB7mVnBRYDDu0WQ3UQ5TItAtkmEoFyE4gr5rD5XRfVa8fIIlINYm4XlWkfKxQFuuvyQbSWqbPZPxKfku+OyeyQp6ijrB0VJ96hU3XaUaCHv4kKKepA6WvNFOa+kz6K0Edqo+SyGhuaJZYsLx3IHm0Oye+Eu9Jjoj/NGtU+55PtX9b5Ifnk8B9TUe2UPAa2Qhm/pBsy+tF0UaeAXkbPp2JxskPCaRph6TIKgXyRpEekAYX9JBWdkFV9pfqK6plJaTj2Y9VjaTg/RaagnLAy/7gebWfyMOfb40X0uKihs1YSZPXtGZhnnw3azwnZ1IPeRKNGcorPQSWLawZr/IPKAfjEZSS5PG4lvDIk2ihm1zrYL/R2kM8ZCJumEsPDJT2NMNoR4uhdVs69Pqgll7h1jU2k5YyjxFMLpaZgPqSfAy3LiPj03+rsL9o4Et2vHIZYX9iUq7jMR7PWP+tyZ5VP25T7pBuDgXlQpBkYwRlgGS7SPDyvfWaW07GM5503BJmMlYk28HxHU9wq0DynibD1CmX6/IFZ1iQGfIjvVDyWUMfE5OtoIkSde1rQIt8TxaVe5dh+ok6dR1lejki/uW9m7MSzQ/klncheMB/zSGhWUMbQjpBfpz4XGs960Ea61TEiCImbRcrz23LfZtJbe0R1CHihyCffBzc9EEvZVAMqgEuwT99E/mnb0FGloEi0r6ndmE3jYJ/PObP3LHqWQMHWmOjRmEoRmaJGO4q3MLmRh0UlwwkRlPlK67KafFdHSwktdaZr3N/zsJZGi1wXmdZ1Ba8guVnIMtQ1fv4PMe+6KjpiIpB5CBourGuY0JqVEbgGUZU0WW0yVjTvk77ezGC/fqNO+d3dO8maeMucLD4zQB6F3p33y6xP0bXfvPYw13CkIgrl56Ciiwyy6/7sBaMhCqLos7jXk9hW9L4mpmYwNkLl3Dm0nlM5/O8us560n1Yl2zf+bsRuhfT9nmhtGrexx3rCZW1Cbda90U8UsjPYnR0BMNXRjE5mWc/cAJIjrNL0/4JpnNVmPZVNv7O1UfzfPOcq0tdqTypnGp/tZ1yT9JsLOZRX92Zy3MTzRRcmiT709b258+5Y8VpHvs/fy6ku55aETznZZSH9iVj5Pi4vuiUnfalI4LXLgQ5GT9PXgEHw9SpVErJDeXbhdVBe55dUAPkSod9msEVqjld718zcjM1eTHTkHxtl4fbTcqv6n+ubIR0uNfdguKofVrbTST4dm5Ne1HQVX9X82eQ7KGFdDyrwHQFSe1qjpRZijIqxSOOnN2gdqd8lW7kv808ll1gNgN5xGZHWxWZnHb38rKUWwvjuTkZrb5iktyu01a/7prmOR7YOmQuAaNgOe5EaoXnKw/xnga+9GqceFDXiD897y5a3iMFYUfNNrN282Gex0iaUS4ekm9elf1pjGDM4Db8mR+0FQ8yPpm1TpLN0S4PC0G+DQQf5qFzki2+HdVmrhwsJGG26SJuw7uNgvDH1ie525CiE19KBlIeasaz5KROSlaav8Fwva2gKQURHbO9TZ7SJtUyIkrS+i59EFtPmPuy1vWgQXyvrSxafeVc97XXwXSR9REmZA6+8iDZIPuB/YX5aFQrRjxp1ykfzhq27KkwTfK7Hyx7SDePrNpbjj10rDZSu3n7wz/cULg/7/cXjJQ3T3YcDONfIK5gWxfZts1ggn2CDGr9hV6fe6NHfYXlqstYUBzJP/YRPSDlnxa4j0Xj3MpacLBolr7fNA8IOyc0d7QRtzv7YD6Piu/TcaeuLsdiINNlbHtt1eaWXYZrP6hbPg70Zui/0c7/8m9s8zMjmEExrxSYSOHvvvuurQeiNb2eeuopW8MlqNw8bq3Cm29kHdhdm2EaFNDggFuFo46Yni7E8pgpjWF0ZAwjl0cxfnkSs6NF1Ipkpy69uhmhMZtAhKSF0DVqG9VU3Yh7pfN6dLPLaUUJ7ItptK/61yLE+95+HcWJYWxcuwEPPvy0My4UMc6iJ2lA87jMDpaPxVFIxJBjm8XZMcvRKkp6usLqSE7Rk7sygrGpJGZZzkqCyiROQ5PJZNl5bRaEZjzoCTUNsQQdADkBWndCT3KiPBfR0xq9ohhJM3+aA8VdXqfX/hVHT7YTNT1RZxniBQaUoc8Vu2fjmovH/QZrmonqKU85EUUlrtlgrv2oRpFpFJk7dppEBlVSjJyehhbvo7NK76PM29o6KPUSypPDGDpxCO+9txf/cL6Ak8MlpHJL0d2RQUdcrwcWeR9SXM+SWK7moJNmufHIBEvCXmdVedimqoOInFp96ZL3LE8jNjWEMweP4/13D+Pw6QsYpfJP9nQi2aEvXuZY9+zQesWUPKGcRhta24XpqHIUxvMyGqKRCklfhdMTf71amWKdaY2zpJVbL4pGqxcwe+kkjk9UcKGSQjWeQSqZQoo8Gatp5hnrkG1LTrH76lsGrE7eTEYyb2dCVqRyOGroM892XmVXa5O05UkN/nm+C+nupqD8byUfLmdHHzPRdGXJJa3bsGbNGmiBY8lEySXt+/iiW6sTHOke7cjrMJGMdPG9nFFKHCTi7I9TF1EePYeheDemkp3sUwmk2XlTWsiXfaaQn8HIVBUFdrR4LIl0MomIpaW+5Mvoyqf7BfO00BQsr9rSG50Kn5iYsDbT2l5amkCvlXV1dc1NL/dQXK/7293jthPzqK3TQc16t3M8lDSnjJO+MPEmUcdwFoltp+soB6szQH4c+elhjExcxIXxcZyfrGJ4rIL6RS3KnEQtW0MhVsD0+AiKpy+hMVVAdaAfBeq+KArki7LpOWiNUHP+LFP8J19RR9qsMMruaC2OEm+sWYVaczQapc5i/vRFM82SKLDua8wcc8swJcF4lOlzZb0DSfBb8ZLIQ+EyhH/wgx/YenJ6xWH16tXGawqX3FAcXePTWwjiz9y+8ZLl1ffvICkObS2VaU5vXh0nGr0MJGhblqZRmpjB8FQdl2kj1HIJDDYKSFOH1ylHKrRr9CXZWHQCCfJGItJNGyDFNGh7ajBBdXCbdPP16l/tdPjwYezfv9/ki15t15InkiO6TucVb6HbMKR58n2t7bFkI+1tVIvAxVMoDg3h3OhZnJsawaV8EjONfqSyHUhTVMbFl/E85Rxt4JFLwMlTGD97Hu+W+zBDftWsrVSsSn2ZJ+dOIVKdwtTIBM5fGsWRoTFcnGxQb2bJxzmzgeUfJPTBsdIM8kxvYvQKrkyO48LIJCYKXZiYrCCTriGdpu9C3ySiN3UoGOtRLePi+EnaSh97clPLSFqTk7zmHx7YQ2Nf1pBuKl2vT0t2Hzx40NZ71dcat27divXr18/xnrdLWq+7lcQf4wkvy/Uj+W06u8lP+lMkHrljdg0XX3KsOcBFnQ7ainnaDhPjwxi7dBFD52gDX1qOSjmJRIq8Hx/FVD6PC0PA0PA0emhHpuiHx6L0PelLusdftB0lI81ecL6yPtagmY9V9kuF6+vNsh/0VlRZYYwYp3MtP7wQq9BvpI3CfY10MIVFaS+IT4K8on0tZP/yyy/bl97FF/rIgR9D8lDcIILH/+7f/lvbskpu7qCXv4kMZTGoH61Txvbs2WNMrXcyP/vZz9rio8H4Hq0Zv/lw6fu7sFpta0KveSQDsl6vYnJ6xJTzzl1v4ZWXd2HnK7vw3p73MDI6Cn24JNeVQypK41TZr4vBNVKhhvrwQa+bDdVha9pqA9W9nMvdu15lhxvFZgqThx//NDsKzxdrZnyxR7H8mnlEXUZSx8jqCQvLpKmV6kyJIs+cuYg9r7+O598+gLFiAbFcFOmOJFIRdlAz4pkOHT4NnJgQYJjqVQNaAjmiWdt2trnvoFnT0kG2gL1yx/wYMZZSs0zaFSJeL6VF6M0OG7SZAzs9246h0Osgmn2h1wdFzB7Lk2SYhEMZmJnGqcNH8NKLL+L5l17BG5cnUCqVsXLpMgx2d6Irqa9pqFAUOHG5RHI4lAMp4BjrijcntK6Ysiw2Vo5trqm9bsA2KVZw+dw5vPzqG/jpCy9j78EjyLNfaE2S3r4OU+Z639iVrlk2/SpNQkLUnVTKIt3bOZq+2HM1QwGLmSt4f997eOPIOVwYm0UmEcdSCoqMentFC+4zDZPMMr41eNe8luV0twq0TDNhTREX3Jm5u1mY34QIEZRvQfLnBD/oJeNGX3HcsWMHVq1aNTfQJTnmZZngt7caQR10LWjWpmBZoqwvl/M4tXcPdr76KvZdmsZ4MYJkNE65EbUHBrMzUzh06CDeP3wS45MzyKaS6GNfnOs+TEhpBevpdqJVD3vDQ5AO0ZeVtNVgl76cJwMkGEfwZQmGLS40y0j553N4dU4pCU1GSt672DovNWmv0E+NY2JiDK+/+QZ27n4du/fux7sHTuDQgWO4dPgMI9FQzZE36gWcOX4S+15/CwXqyu571lpdaY0OSW+9flDXK5BSITKMufGQ3vRre5QZ2fSIHmiYjNY59hXmb06vMpNmg1hGLeiORTteCvKlXrP9u7/7Oxsk0SL2GvSSLeltndvNd3Z3+5nPs8MH+4X2WinamADo/Jw4ehKvvbEXu/Ycx9nhCLq7l2FlTq+86hVYPd7S4z/aGZHmeqKNjOMbOyJ8gguM1vr3x16mq420LqD8gWq1iscffxz333+/6QXF0XlRiNuHa7WhoK5YKBRx5fJFHH7nNezatQt//8rLeO2tPdh/5CxGxopIxDJY3i1nvEynvoDLly7h8J592P3Sq3jh1dfw3JHzts5wrTSJdLyBLGVctFrCGO2C1157Gz967iU8/8YuHDx0GJcvXEFptoJsJkd/K0k5XMXJ/Qewkw7wzjfeoOylfj10DG/uOYoLFy4gl6qhpyPFdOmD6Uk9eUnL0gjiKslxK42Xl/IfdNyEguZLG+JmopWvPBSuvi+5oAdrsgU1sCHSAJjkgcYRfNzbBXdnyvA2HDKXLduSozQWYB6n2x8eu0x+PoDdr+/Gqy++hpdfIu/uH6GtkUB3V5k6rIyhK5N4651jVgc97BSdXWlEkrQ5NImCnqgWvJdtoskKwpyvzLP+q8HysQUdawkiuY32ARxeYuttE27Qi/GVaZ/vRQSvKzykJ0ZHR/H666+b7amH5IODg7b2W1BXtPJG8NgPet0yzaKb+RsGR2e9YeKNGG39vhDM5K3F/H1kUDb/CRmUPNeoolaZweWLJ3Ho4B5MjkxjoGcp7lnWgY6ZvXjte/8Bf/X3+3ByOIXLlRqmyNSlSAwVre9F5myFL2ewrDcTSre17nQsQTEvLGQQsslZPtMFii6GUduw9N7Er5G05DJq7CC1EpINfWWFyqs4icNHj+Cv/uaH+G//9c/xo+//GMdPXsR0RYu1Mx3rT+yc9VnWYd4pHE3fZP1UbTWtCio11hGNfX1cuMQ6K0aK7J2TvGwcCX0QoNLADNO6QsdxHClECxlEixmGpTDJblpiepEyqVpHI04jKV5CgmmkGgUkqxXEtbZOPYZCJM20kzaTK1nXFywaPNa3YjQLD0ynzHrRIvJs40uncezkKWS6V+IXf/n/hmd//qvYunENejINxPRVx+oMnZMCpsoyNDMsa4Zl0MwuzT6bNGImyega9GQ9shprjSTv1YnpWgemLuzD5JVDGOyN4enPPIRnP/95LNu4HRcnqOTH2Bfk1dRZT5oWXq5rYhsNADWFjNkC811hWvoINLOiwSc5TcxPXLO26jVbm0CvmM6wQcflDLHuUvEUcokO5Gh8UGUgHuXVqmsbSWPiGvBj2zYqWgPNQozketlrWM1XcsQSYtkGy2r9RNB5pmndRLshQnxMBGcJefmlbZAWCq33DZKHMzHE++xLkWF2o4u4eGIv/v4738Af/+E38Z1vvYp9h89hhHJlLDKL+vQIzh7aizee34sDb1/G2GgNRYrKguREcxB7/s/3sWY/uw1oLbPXK626y4f7eIL2vQESDF9UsOpl3qhjfE17cr9OEmqASZpQLSJ9Ued+jTJX8jhSG8OZY3uw+90T2PP+CK5cnEaqMoVsdBKziQqmY5SrCTlzo+iIV5FNLqGR2UfZnqK81nIPeoxCT0szuhLUTRHpJ93EfUCnTKpITEs/NWaRqkunMifUKfpCU8XmoVdMlkvlKqrUr0a9tPZNa1sFcb1ziwE+b8E8+n3PbyJv0wTjtQtbKOiOngyWh6tJf/Yaog/RDyG7Sw/kGrRJNHdcg7EnTp3Giy++iO996xv4wd/8NV7d9TYuXM6b8a815HjFfDomk1gvZALrdp5uI67VBr79JCe8H6Bjf05h/jjEwiPYbr4dfNhcu9AeLRRHcfLMCbyy5zTOXalh/fLl6I+WMXP8Pez5yd/ih3/319hfLOJsPIeRo2fw5nd+iH/4yRvYO07bdO19WJehc/+D/4rvfuOb2PPOYVwancDlySs4cvI4ju2/jL5EPzYPVBCdeQdvvvBTfPvP38Lu1y/QZzhNW/gCho+fxcGX9uHI+6cwpi+xJ5LI0N7XGyKRBH2xeAVlGcbKM7OvnLvcMy6lpuuFrgfNl1jHXqKGuNn4sH7t+UzbVrmg49sjG5SneQ65FixbV0XjgcqjcPprlXIF7+85hBf+/nW8/vpxDFVyWHbvQ1jaXUZ+/ARGCyOY1DqNqTr6E0X00ZeUD6fZ3OU6ve9GllypVx1pf5QnES/OQl/5r1AXzERioDVK22KG4eMo87igr+o1SjZ7Mk47VG9aifTZnDQzpfeTbJ08s0EXH9TO0ueeDzyJB+bHM1xYMI72PXTcDs5CvYkI3tTD39xnrDUz/pprZXLhoHfIKRI1WEOm0KyteCyCwaX92LplGx575HE8+fhDeHDLChq4BezecwRnLmpabZFMRwPZyiaj1ilzD+17upVl9GkH6zOYDwawhGZiucNmWBBSATL0Fc+PjNmC/nUqtNlJnD1/FoePnMDE+CSGLw/j7NkLuDQyiqJmVule3BYYb2JsCKOXh3Dh1Fns37cPr+16FW/veQuXhsYxm6+hXKNbweh6x7k2O4FLp49i7+438MpLL+PlN3bj7cNHceriMCLTzEkpzrgxLdFq4zARW/GVHZ5G4sTMGC6ePYWzJ47i8P792Pv2ezh65BQmZ0so0cAcunge7729274I8uJOjawfwuXhYcRYrki5iMsXz+Lo0cM4c/YcCqUaOjr70DewAl25DjotEVSmxzF09CD2vbYTz7+0E6+9vg8nT49gfKqGUrmKSnUGhfw4RkeHcJH3OnrkGN7buw/v7TuIk+eGUaxSwNQLqFdmUC3NWP3IqM2XaxidnKUwbI64s0izM7MYHhrBZV537uQF7Nr1CgXkq3j/0H5cGB7CTLlALpPRSx4tzOLiKTpdu9/Ezpdexc5d72DvgbMYnmDrxeLk2zhymQ7ksjmkaBDU1H4zkzjFa95+azfr+QW88dqrOHTwMIaGWQa9tcNM2EL4JGtL4wH7b0IH4pereSZEiI+La8nD268L2sO+2ifQSdWgdLUyjfHRy7h47jTOnLqIwwdO4f39h3H8wmkUIiVE6xWMDl3CmePncPnCBGZnKfvk+HrZTHK6gYLN+pwk8HyPu53w+qNVr7j8Xp3H1uM7Aa625+Hq3ZEbkHRHZg2wfbQmjA2KVfOYGr+CK6OTlJdprBhcjQfv24bHH74P9z28AyvWrkQul0QyTsM1EUU2243OXJ99vOTs6SGcPXcZ4xNTqFXdArfl4jSGL13GlUtXMDVVoE7h/cgjxZlx6rS9ePWlF/HqK6/irT3v49ipS9Q9RWsTW4zf55H5s/wH+o1vp2Db6LrF2rdulIeC+V9MZflg7hXiqQnm14fI1pQBr7VSa1pPlW2ooazC9DROnjqNQ4cPUa6cw+z0FG0v8tx03p7y0/I3OWRFdz8khvG33S0XE3x7tWu3YNidKE8+CWhtg/btUIc+zpLJZrBkxTps3vYgnvjUp/DUY49g48oldOL1psEeHL8yhOFSFacO0bbftZtybwi5Zevw2NOfw9OP30/nu4ALZ87i4MEj9lX5EnVlKpPB+jWb8eRjT+HZzzyArRsHUC3mKQfP4fChs8hXRlDCNIrTsyhOFJBOdmDDlq145PFP4fFHH8f2rfeit68LcX0ml/1E/UPrhOn5vYMrT1DWX13CduUNsZDwfNdOHrSTG4sByp7lUD/KvwZs6EdpK9leKZdx9PAxHDt8glGSuPfBx/HpZz+PTz12PzasG6TfmUGd/maE1JNNoDMVRybNsHoM+ULV3hIYGr7C/nISx48cxDtvvo739ryD8xcvYmK2gNHxMZymn/jmqy/ijbeO4+IQ/V/6pxH2Fj3A00tRshVUe5o/7rSQnGlXr3cCfNv/rLxw019vDEKZklLX6JygNb2OHTuG/v5+W9NLn5n2UFxfiI9bmJ8ZeoJGY1NfUopFyzzW89gkhegyrFi+AatWrsKyHqCjfhmTk+N47kIfdjz0Kaxe1oGuTALJaAzkWdcDroFbWbZ2aYtBVP/j4+N4483dGJuawsbNm/HQIw9BMyQjej9CzaMZQBr5Vd65SUZYFjliWsikPks7fxQjF4ewb/8FHD59Huu23IPepT2o6b3jTDdWLl2OzmQUldoUps6exMXjx3Hk5EXsO3keB9hJD+3bhTPHjiBfXY5YshepNLt+fIZJT2H4xHm89fpbeG3vXrx35ABOnjyOoXNnUJiYRi67AbGuBDRwrVf39EKhfd1RXziavYJLJw7hzXcO4MTx8zh85CxOn7lMR6SBpcu7MEOn4dDbe/DeO+/SET2A46eO4/LIEMqRHJYvX41EfghHD76PXa+/g0NUqBpRrzA8xnrc0lFCrjyBy6dO4d2392HP+wdYFpbrwkWWoRP1WBeiCfHHKGZHx3Dq4GEc278fbx04h/ePncfFkSuIxkusl35ExiZwng7vwTMjOHV5HJfp8MwWZpGIVLFyHR2knhQSs+cwdnofheJR7D8+SiNgCPvf/BEO7mWfGSqgGO1Cd1cXejvYJtUKTh05ibffepu0B/sPHMXJ8yO4km+gu2cJ1vWWcZ71f3kmjki6D/1dWbZNAcOXL+Kdt97Be/v24eD+93Ga5Rken8FkvRPJTCcdNcZn42u9tJjEoxx81oVNjNDrmmITndFrN+I1/gvNTYgQNwT/euMp9i29p6/1XIKvNwq3TQd8CCTZndItkO8nUCvO4sjbR3HkyDmkBlYj091BWVVjv0th9dr1GChcxt53d+PI0Sp6+jdi8333YOmqTpO5WnvhKvguxbK70t/+OvD6Q3pcrzXqlRS1ndb00mupnZ2dc/pdbbZY2+2DkFy7Oq+amSz51zyy81qBS4+AaBgg2ihT+pWAqcs4c5IG7NlZZLqWYesDO3Dfww9i1do1WL28B4P9GeRSJTTKJQxdyePkpSqyfQNYlsjj4Bu7cPTSMGYaSWQyaeTowE2OXKYcP4fpmRJi6aTplfz0FerLA9i58yW8s+ddHD1yHGfOD2FiqkCVnEBPT69bF8psFEIzhZRThl2rBe6Utgnm0+8HDV3Jj+9+97tmP+q1OL3eqFdgPK/6eAsJb/Hprs0cN8mDobQvRRq4Uv40yGUPFO3LnVXui9tqOHbgIPa/fxinz16gPUWd3r8MS1esw8a1K7BmQx+qMa06q1nmsoXqdGikrWl/ml5mej4TqgOXmduC1jYIts+hQ4fMH9CC1Y899pi9pioZo2v8dQvdhiGujWC71MmnWgollUpjcGAF1q9bjzVrU1gykEO9WMPw+SvU67PY8tknkYgncPDV13CAzn5y2TbseOYX8dCj92BN1yRmzx3FdCENffG2b8VyLGM6ua4BrBlYg3Vr+zGwvEJbNI+Lp4u0n4E++lmPfW4J7YQ0Rt87jwtHzyM5uBybn/4stm7ZjjU9y+mndSPbQ98llaR9Hbc1he2L6o2EuTLqkyYnadS618F5vvkgSwMB2pP21V+IhYN4S/JByx/JLtQbAJs2bcK6detsX+eCPLiwcFzh9zyHXAUdNkWv+dGUy/rQjewGDXqVK2W89fKruHTyDPoG12LTk7+ENfdswMolPVg22IGe3irSmEFpIo9zV+oYmZrF8nWrUEtWkR87g5EzB3Hi8DHsPzJGv/oyDu19DWdOn8BUKYKpImz5nFN7duLtN9/Aeyen6V/n0NmdRjqbpK2p1a211qUGvLREgnIpcvposfJ6UOdLN2hNWb1KrVcaxRda00v7rXxxLR655a833onQuE+cBkRMO1E6NfEGejpXY83KHRSmy9DX14HuHDDQVcLy3gbq6VWYRT85qQNxfYKcbVQmk+tPDeYbzW9vN/Ree4kdoKJFTjULwT5vzROWPa0VUjNHrJM2WLbesAVyGyxXtJxHffQ8Ji+fx9l6Akto4D/7pc9gw9o+jJ8fwfn9IyhP0h1gfc1GpzF97BiOPv8SfvCjH+M7b76J98+dRfXSaZx+61V870fvYNe7VzA8Pkan4BKmhk7jrV37sPPFt3Hw3HGMzl7G+NkDOP3qj/HWT/4e3z86ilPMH+UGEmT8RrSKYrKIcmwMydFjVH4v47kfvYDnX9yD9/efwvDoJPQFrUhjGu/v3Y2333gbQ+eHgVIe1enLOH1yP15+8zBODM1ioljGNIXRVKmG6dkGJsdnMTp0DkMXKXQvHUb+2DvYv/dd7DxyHudmdX9eM3oSu/edwMvvXsDx82Mo56eQH7qEvS/+GC//3Tfx09ffwdtnRnFpehbl0hiQn8DxUzW8t5/KeyaN2TgdXtZzfOo88hcO4fTIUQyVp1EZ3ovpA9/DOy//Nb79k+fw1uGjKI9exqn39+C55/fipdcv4uxFSrdKAYWZcbz8yit47bXdOH7ypK0vNzwyzvNXcJFbqe6JsXFcOncZI5fGUZxi2WfHcOnSKRw/cxrDE+PIF2YwOnwB77/PtHe+zfydRrFKniX/u8EuCW73eMwGvZqC0n2BzgLmWSdEiI+IxSITPzKacl0f6tDiogm9QhHtpm64B088sBL3bYihUBjHnoPjuDzeScN6HJlEHlka6ql4N6LxrH2SWi97ex1hZEm7ff7oyG4X4lahWefuYB7Uf0Z06jTnma1Easams0cBzFNFxGp5dFCPdma7kOlehljPakS7lmCgexw9mRGk64xXqGNovIC3hsZxaKaA/iuHUXnvRex8fS/+fu8lHDw/jvLUBQydeg8vvngAJ05PYzZfxNjYeezd/xp+/PL3sffAG5gZp568cA4H330fr+3cjTffft90z2yNTl21glRDT3L1wRka2Ca352H8dAei1ZC9s+HcaZFax9ZkIWm2uT5KoLX/EuQrDajWizN4+62juDRUQE//KqzZtBErV3RhVXoK2fIQrsTSGIq4mdup2jSd+grTzTHdDt5Gr0bqtVcaS/YQM5QhIW4+xMexVBI9Swawads2rN6wAZmeGvoHolg7kMQGOtqrYknKxk7M0g4+NFHDRPcq5LZ+BrlND6LSybjpy/jq/TnsWL4EjVIDI4UMZjMbEF+2CavvoTPbOUXfC9jUm8aGvgQ6O8uox6fpa+k1rwxiGlCg7CsUgNGpKEYmyogXp7Gkg2czHajy/mXaqY2GltPRR5xcl1CPsD6oPZMv6pcOOpJD/EmROiF+drjhrda/FjBArGTs5BZ89gfcisSDMSwlX/bRtpgansSes2WcmKwiRdnevyqOgXQeffR9G6OXcGh4BnvOX8bFygxGasP0L/djaPePsPsffojvvXgabx4u4tKZEzi69w289NKr+OFPX8crr72Dk8cOYmToPN5840W8vWcnTl+4gvFiCoWGBpbJ+yT3XQdxvB7muY+w3W0IB70CsE+S1x3Tii0kHNGcfaBF7TVyq+mKszNFXLh4BStWLEMHBXytVkelSoOT5+yLidd52ng7jVB3Z5+n9vkwY1P5t7KozKwTXjI9PW2LRE7PzGDb9u3YumUzHb0eTIyPu9lPhaLF05csx0bHsHfvu3jrrbcxPDKG9Rs34hd+4YtYu2aNzU7a+94+i6PXO4aGhvDKztcxMTOL+3c8gK985ct45umnsXzpEoyOXMFbb7/FNOh8yLdkvoyYR1NgpRIunL+AQ4ePYWRsHEuXLcOjjz6Ce7dtpX9Sw+uvvYLjJ09jzYaN+OpXfw2/8Wu/im2bNjH+YRw8dAylUgXLl6/E2tVrsKS/DytXrsCDDz1oaejrXadOncSp06eRSmfxcz//RfzW17+Gxx97xO6pBfWOHzvOfNVQyOftafy+AwcRjcWx48EH8NlnnmYd3YPC7AxeePElvPjyy+gb6Mcvf/VX8LWvfQ0PP/QwyzeCPXvfw/jYlH2ueWxsFEeOHMXhI8fsns8yjR077iXP1XDu3BmcPXsG4+OjrLsRvL57N6Zm8th+3/3M28/jiSc/gzWrVzI/NHorZUxOjOPM2bM4c+YcxthG/kueeir+1FNPWx5+/os/j45czp6uKP/TbAOtOcJGV2dwI40BBDmmPfeECPHJhj6XHqdskMMq2VitVm0audaqlHxbu3YN+1kDZ06dxuWLw6hSNyQSSSSSWsfJxZcM1mLk10PYv24tWuv3A/XNtpWmnNPgtsMfGbHUQbG4HhwBs/kZDF25gnPnh2kTzFKfjaBS1CzxiH3Cf3JywvTFMPVcpCOLrt5uTE+N49jhAzh2iEbqpSs4eZJy+tw5pDJpdJCGLl3Ay3od/6WdyHX24ld/9VfxlV/6Mu2NQYxcuYj39u7Be/v2m3hWvrVOZ5xGtWYo2+AcYXpbZVAmQywOsGnUGt6GUUupvfyrMPVKBcXJSRw8fAQxyox7791mbxc4GeM+iqPZ+bJIbb1U6WqS1LVDs63njkOE+Hjw8kOkWRbBY2kuvySHzERzlGj8F6emMTI8Sls+T/mYZHgVlVLBbGTN+JJNba+Jm2MVQSqVobzL0A4vYEYPict6k0OnyMfqH7TPh/Wl+PFJxHl9X18f0rxGerRYLmGCNu7x48fw2s6d+OlPXsCu197AqWPnaI/rYT6v14N7ZZD31dKhJi9b+0qIEB8L1xOy9KHJv3oFXbI+QeZLJJNYOriM/SKBAwcP4B++/3fY8+YpjE+XkC9WyacNW/dremoKV4au4Az9zlKpyD6jmc0VnKfvfeToUYxPTGDlqpV46umnMDi41L6Cu3Pna7gyPIxNmzfjCz/3c8ikkjh7+iTO0qYYn5xGsVKzfjufZ/Uvt7kbcX3L+y5DIiEmlaDUIJbEepb7cRRnJTRPkAH34PTQBXx/Vwe+t3MJHrg/g/u3A+u7qxiIV9BJwZrR+kmUs15BXAvXO3froNloaRpMVEB6UgJ2tjjzKU2jDkBFIZaIsJNWaUhrRLhRnQKmRjHLTnTpxAlMdA7g0V/9J3j04XuwfdMSrMxmEJuuYGRsAqdRxqVYEn31DgxUskgN3IPkQ1/A2me+gs898Sh+6YGtKOYjuDzEjn7uDEpHXseJg3vxo9ENyH72f8ZnvvJP8fnPfw5f//yD+N1nt+KLGzpxdN9O7H97L5WnPtmaZzZHSUPM5zgiFAaNYhH53MNY9uhv4/Gv/lN8+oufwfrBIroO/QNSe76L9yursK/n80DnGuyojmDr1GXsuzKKH7+3H0cvRNDbuR3bVt+Lrav68Mi2fjz6mXuxbdsSlMfHcOiNPdh35BzOJJZgtmcVtnRewj2pM7h0dJ/l6cS+Ixg9y7qpRTGeGEBszRex6ul/gs1ffAbbH85hc3wvSu//V7y29z28cvEEzrN+yr0dSHcl0F0YwuSx9/D621EcOdOP8kQMmekCso1+dG/8NWz/7P8TT306iV/+bCeeeCCLXOwixo6+hOm3f4rZ91/GkfI6ZLZ/Cfd++et46jd/A7/wa8/gl5/ehGfXs56KF5GpXEGhlMBwqR+T9R6kuntw/30P4ks//zk8+6lHcc/a5ejKRSloZ3H8zCiOnbyCqTw5Qgvqa7ZAVE+NxSOOLWTq6MmAiQyTn+QN6Ckz44UIcRPwYTJzMUAPAjTLoqFXi2jAxyuUl7X1iMdWYum25XjomTV48oFVWFNo4MQPnrNXkycbnRhNNDARL6AS0SsbFEeUYhG9lqTp5aLmn4x9A+P4OUYhbiZUpxp4tGf9cyRcVdOmC6nQJe90aK/J8Lj5rfBsNI5LpSN44/CP8fd/9zf4mz/6a3zjD7+B/+tPjmDnG7OYmHR6Kl4eRmL4MkpnT2Nq8yr0/dKj+Mq9BTx46Rs48Nf/J37/vxzFN3d3I/HIp5B5eAd6ogcRP/KXGHrvfZya/Dks2/Fv8ciXv4pnf3Ur/ocvJfALW48hM/s+9UYMI1TNFWSgFxvjKCCpRWsbs3N9yAzvAC123Cn5bAfl2tM8XIjpTvZ1rePnNKrjtXq1xAakTVOdBfJjKF08jjMH38K5ejeWPfh5PHPfDnymO42+RgkjXUnke9P6DI8tRqzXGeu2F7cvc9GMY1o8W0uhRl7Vh+kpqRgYIsTHh5clXjeLNJEwWYnY67QzkTxmM1U0Rmfx7nM78ZevDOGnsafR9fn/O355yQTWX96J+ESJflUPYskikrFLyMQSdEXWoJxai1xyll7WKBAropSIIV8r07Q/yuMkzhxu4HvPjeDt8xH0bNiOLdufRBr9jN+LwfXrsfWJe7FpWw+6o5cwc/Et7HvpL/AX/+Hf4Yc7X8XRsRnkYxl2jDTFPcugRb2ZVz3KqLLP6JVgPbzQzJwo5FuQGE0fwdIHIUKE8JiX7UEJbxK8Sa5/VOuyDevNZxFO7iOSQCSaRDzega2f/So+8/X/CU9/ejs+c/EPcPk/PYP/9//nT/CffjKJEyM5VGMDtC87kRyeReHKBGbiRzEdH0JBa9JVc0h3LMeaHY/h2a/+Cn79V57FE49tRnekA/2NQTx039PY/qtfwtZf/jk8PdjA+smjOD1ewiu1bhyP1tFVuIJ0eRxFMnmBtotmQNqsL5f9uwph726BjK5ojAxBEvRUIkW5GaWDc/HkCby7ezdOnjqF9es34FOfehy9nTQ6WIuVagVlkukI9ougkvAIGnWL3bhTB9fsBOWzPjuL0fPnceTIEXvfWiPIJ04ct1FmfVr13NmzOHX6FGZLMzSzaja6vWTJEnsne8uWDVi2rJdKLGbv33Z396Czq4uduIqhy5cxPHwFy1csx9atW7Fs+SDS6RSSXd1YzmsffPBBW6tjeHgExWIBVdavnp5r+V79uXwC3Yy/ceNKrFjRS6FRwuVLl23tGT8z7Ny5s9i9axd2vfwyjh8/jqVLl9r6QXp6qvVB1HZaCFjlVbhcnUq5hOnpKfs08/T0DF577TX86Ec/wqGDBy1NpdHd3UX+qLFocaxYuRL379jBMq9CT3eGhmwVldkZjIwM0yGOW31cuTJkM8ReZj60tp3qo7e310byVR9x1tGSJQPYtm0DtmxlJjIZ5Do7WX+DzXhlq++TJ0/y3t22DlJHR9ae/mqGwIqVy7B89WqbnVhheuQ+W9DTf85dOHf+HF548QX88O//Hnve2YPJiUkrs9bm0ZO3mF59NYFOeB6dZ+EQIW46WuXkYoa6hJfjynKN/V9PkwvFoh33sZ9u3bKFsmg5vvOd79gnuNPsx0n2wQT7YoKGPU0O+2BEMK05cndp/uvIhYRYePjWEGeqbY1HmzNsFKbZB5LtajdBfCA9JXlurwDpCS9lq7aVStn4YPOWzXjiySdMph86fBDf+d53ceHiRZutu2FVB4r5cUxNTVEe53DvvffinnvuIY9VTYZv3LjRwnp7+zA2OgGqF95b2SE/aVY28+Xz/EmEr+c7EcZDTaIPY7xipZFejkVtlvdrr+3EN77xl9aomoE9MTmJoaErGB0bw8WLF8ymmZouI1rTjC+2NO0QzRlVQkp3HsG7hQhx47ghPazlL2RbkwfTyZTx8iHaki8//zxOnz5N2bYMjz3+OKK0890MRUHr8jRsUMCOm7OwJLP0cEdrHhVLjKu0adPWL13Cqy+8QH/DpffEk4/h/vtXMRUN9yaw6d7t+JVf/Sr+yT/5Tfw8Zafup3jv7X3PPvpxiL7K5NS03VO2vaFpA4cIcbPh7berYCK4yf08NbCkD888+1n8y3/5L43WrFmDN37yE3zn29/G7ld3YpSy3sYe4jG6fhnaF/HmmwHOx127Zi396Y1Yu5asnOtAP31KvbmjNXEfevghmwmpGZWDg4PmZ2uGZrFYUldTDuzfw4Jc1u46hINeAVTKcmBoONaTNCxytEwSKCVnMJOcxMSJAk6/NoF3907geLQD63/uKdy/Zin6YxT80SqS0QpFcdVmUCUkuJvwnWExGGzxGvNapdKo0lhiGfU51EqsjArz7tRCHFqqd5hZHTH9UEK0mkdpZhYTY9O4fGkUhw8dx9995wf4/je/hdd+8hxOnt6Ps6OHcfLSIZQLZdZBJyajSUwnM6hGe5liF5IalYlXUYjQ8K8WkK3MIlWYQTKfR6JSQjnNzpmqoBbXSz+se6YRjy1BNtmPQXb6aGkKBRqG+VgXypE+1NCLRqQH1WQvyolu5NIF9GWK6I8Po6d+mrcaxmgkg+F6F+KlKOLTFUxNlnGpTCHS0Y+ty5bjvlVrsKm/E71pOqHMLyI5Cgcq8MgEy11DtTCKRnGYtVE0JT9TLOP4VBeG6itwz4YH8ODmHdi6YhCr0jOIz5zFeLwLMxQ0Wjiwg+VNUuBoJlqsWMFkbD2V/TpU6BDlp85RGY8hz7z1L9+K7VuAVYOTiGY7MRVbhplomoJv0unnWIbGbQo91RqWVPLIMg/5fBSzhShSyTQ6O7rQlYgibeuBsJ6SDRQp9JDpxWSE6VDZdzbK6ChNIj50FGffeR5//eM9+Ie3TuPE+csoFKbMoSpXIqjUoihX66joSQXDVAduTRByRkSGikQF21FBRjJWNMdAT5PvUukZ4mfGnTLY5aEZGzU9KW5IhrqHIdHItD0lnomsQqHjXqwY7MeTA2fQNfImDhwu4cTUKgxT1k5Q1pYjJfbXEhJ1DZJp4Oxqsj5mv27b7Gw3QCFuDKoryTTJrjY1qDYQaSYA22D+PPfrlK2a7UU9CsrMbLQbqyjDH3j0STz9xS/gC1/5En7h5x/HvVt66LdRMlLX1anfFF9rY86Wc6jEu7GUsnsV05Q8n8oXMJ6cRXSwjkIKKE7GURvJoFHqRiXXi1JHgvylteOAnBawj6VAlYXZ+BTyVFup2izilSIi1TTz1s1cfnBh108C7rjyWHb1M89DHrK1bDF74yoeVUuYHhnCoX3v4u3X38TF4REcPnkKe9/fh5Mnj2Fi+Aomz1zGuVOXcXEkj4lKHWVNt6E8idJ2S1EFJ3moGft1G5DQB2kSJDPiQoS4Yfh+5mVIkDwq5N0SGbraqCBZPoPqqdfxwp5pvDe9CekVW3Hf9iVYv5bCqTpO63+Kjng3ivUOxk8znRQtVfWAPMVi0V597IjRliWvZiplZPRRh8oZvP/O9/Hc8QYudTyBnvufwooHlyO9PIl4o5M+RBKpziT61y/F5nvW4PF1a/Hklk343Ge2Y3lv3D72cXm0hMkC7VnKcst5Pc8OUmCPm5/ha6CNG7GP0hQYhx3JOqc7FSKEwTPMHOO0BohhyEdX9Rc9jHBrZmmWuOzFZCqG7q4EBlf04Z6H7sPP/dIX8Y/uj2HF5Hs4dvoK3rzUhZOFVZiO6QNx/ejMp9A/Rf+U/no1mUAjl0C1u4YpmiEN+oRx+mtRLbPQkaarSDuhXkaW/SnZkUWV/l9Fdofs0xjzmHD6IlmLk+xRiekLMznvMoSDXgEYs+qP3BChcasHBFUyyrmxczj07hGc3n8RERq62z7zFB7/4mcxqK8jsAZjNQ061BCj52MmTt11AM0I8um24nY4e3LMNKUxZopAeYuiFq2hboMayqNMsKi+T4USDxtajDc/TaNrGBPj00jG2Qn7lyCm6cnVKvq6urBu7Upku5O4PHweo6OjvJpGezzB6zWIws5aZofXuAiNMc0aTshlrJWR4p2yrJ8k7zNdmkG5qQr1pRWtulcpNjA7U0a8XEI2RSczxhqOJnm1vkTBbYP30TGdgGSswrIVEK/PIINppBNMKZNDnk5KZ7oTm1cvw333bcP2Rz+Nx556Fl985rP41EObsGKFvgRDwWTtlWTb0lBkWlUNIkWqSLGYWQqTgf4BWztr28NPY9sjz+DLv/gF/OLP64tDq+yLh7HqDGrJrA041diu5ghbbbK8rIdCI8f27sLqVStpENyDBx98AA8/9jSe+fyX8NQT92L1yg7EUmkUaRSU6nqNUC2gBCTdokgwvUyN+SEfJdM5pFmmQr6ISqVqXwuN8Xyd5/VEq6AnAxHWV5y8maaDxEav56cwcfEUDrzzGl575wCK0QzWrN+IezZuQH9fnznbNthrwlr8Lx5Wozlh7khQiYIIngsR4i4A+7MGgOuSU3Jc9eS6odcjKO8aHXRGe9DZ2YHtqxP41LYunDo9ireoN4ZnaOQn2LcSlJA07G2FL17fTg+0URct8P0u7H8fDzdSb2pf/jejSV/qdVRKW4pF6jLKy1Qsi2WDq7Fl2zbc98Am3PfgOjywYwuWLdeDHumBGtWek6upbAYl6sOZYhWzY+OIFvJY0t2N1XTYItkEzg6fwni1QH3UgXSkE+ViBGOzRcxWwLTIXZTrlXwBJfJRtVICbVrEs5L9VTtnX9WlXtQrmF6OC57Hboe9EaKJZn/2XKemiWmWlsLN0dZXQ7WgfR3duTSyuZytUXrx0kVuRzA7NYXZ8UlMTs5gtlBFSe2pB1KML4tNPo2ITNC06JXw3EGIEB8bczZhk5qBEoGUUXmMHtuL93c9h8vjdWx86Iv43Jd+GY8/thn9PWTIWhH9nWmkkh2YminZ12nJ6k6oNioYHbuCsfFRxKNx9JLnuzKUX+UiLh99F3vf3Yl47zrsePpLeOSzn8KqjX1IZDSMqzcxKOOS/O3OItfbhYHuHqxcMoCN61dh1bI+G2AolOr25VN1Bcu3XpukZa9Hteoqc7AHu7SZRZYvCw0R4iPgaqZx/cT1Fc2y0gMOzTjUmuAxCupURxIdy5Zg+xOfxi89tR3L0xUbqD05XMGlScZPULHTR9PklBz1ufqHnrOVqevLkQoqXsZrpiTlf408XGXaWks2rkkL0g968EF7RVmxOTj2HiPtEfqXUT8QrB/bubsQasW5lqdAZW3EzJBwM1jq1QpiM8M49uYr+P6LL+HNU6ftk/SPb1uLVT0pTEyWaYREaMzGUKlrnheJTpFebrjegNdtg55uRyX4VT4Z8HLg9LKN9plPdlDNGMo0SsjUi4xeR3GmiENnr+B0PoIV2x7Cr//iF/BLX3gKn/nCL+JLv/ob+PVf/UU8dM9SzF46g9PHrmBmJoJKrIRSJI9KhT24OIuIPh0RpUKLJlCLTqFUH0UlHkesV5/4X4bsxBCKpw5jYug4rkxcwvnRIRy5cBaHafTVunrQvWw1Otn5s2XmtKbvns0yl7pHmVSh8qWgKFMwNDKoJHoQzS3BCqbdmehEf6KE9UtjuGfzSqx9YAc2PPQAHti6CRtWLEGUSjNPR3SqRkekVKXgoEpVPtmCye5O5JYOINvRhR46Ils3bsHGHVux4f6teOi+jXhk0yqsXtoDpBM2mCdFW2X+UGHbU75EYklEs/3IDqxEfyzP/E9geV8XNqxdi+33bMKjW7fjkW07sGrdZmS7+5hGA+UanZpKEXU6OpocpwYpcysHu0LbuBJPI7ZkFeKDqxAdO4P82f0YGTlPQTmGoStjmDg/gZnLeae7yX91MnSV6c6WSxgemcSZc5cwMXoFy1mujVvvw7L1W5HOdSNemaCAnUC6UUeKfBDRoBnroa5tU4CLm+2ptNb5imhgjUJWg8N6XBAixMfEopKPN4pm31RH4y+KNOBnSRqERrVuA9OD92zBU1/8LIqTQzj5zm6MD19hn9TU9TjjqO8ojatx41Xh+uQ8hbhxsL5kDFLTNYcvHVH2qSbd2kvSgvPrL2ltSw1gKVSRpMfyNB7zjSSdryw6cmn0dUfR31VHd1ca8WSCF+lBjWY1JCjPI0hF0vTzxnHm+FHsPnAZ5/J9WL3lQfz8Zzdhc08V+17YhYmzQ0BHN6JLl7lRjIsHUDi5D5WxWYwMzeLg2Rnsv1zHRL0TK5Z0IZeSTmA+qSy0FqnJZwl/4pM4yNVapuDx7S+v6l958BQAD3XOiHwWZ+fXhzD0RS/Nrm/EMsj0r8Smh57EZ7/8q3jigW3YsKTbljCIpDpoMyXsgWNXKoWeVA0dNDBiDcqRRpotnjQniP4RU5djX7Z7SL60kzEhQnwUeP2s/uX7mAbaG4UJDJ85jld+8jJ+9JPXMFypY+199+FB2sZrOulhTI1irNKPxpL7sby7hlz+JEoXDmH6/FkURqZw6Uod7xwZwdErZcS6l2P5YAd6o7RPzx/Acz8+gLffn8Ay2tc7ti7H2mUZJGtTqDBNzE6jWiqimK9iarKEkak8rhRmMVTI49xsA1NxykXq2CW06zspFzXhRssw1iK06yMpey1YHo9kv+sgKl/akSLr0BU5RIgmZOc5W8/RnDQPkItlv3qQQXuBnMdt3WZ7V4p5TAwPYWzoEsbGpzBcjGM20Yd471o0Mn3IkF+z9WnEKmOI1AuolKZ4NX3ahMYUqihWZ1Eq5ZEoNpCUmKd9UKYPVqW/SVedDE6Opm9fjrNvlkqI6qMQtDMTtEdjGjGjL+fWI5Vlo6EyG+ads3HuRHxcna9auMvgpZpIxdeop9vaaIMWF9VCxRTstXIe9dP7cPRH38F3dr6G58+dxwU6MflTe7H/xR/hxZeP4+TZWYwXEijWszQ3UihHo6jENMKq9F3DBBvHH98WZy9SYccoWOfQYJcMLhlNel1HUzD5w75URicVTBdJztnYTAW7z03iCPqx7jNfxD/9lS/i1599DJ/6ha/i2a/+I/zKV57Ck5s6kBw7h1OHJ3HxfBUTtTEUU7y+MYZUeRppm72UtPqpJ0dQaJzGTJL3Xno/lqy5H/fWJnHlue/irVe+jdfefRE/fXcX/n7PG3jj3Clk76XS3LINS6pJ9FKppSozzPMEBUER09E8CokyKmX3Omo9thTFzGrUu9dhw+AO3DO4Cd15Ktlz7+LMxePYPz6KA2PDGD51DMWRGUyzrFOZKCbYFOP5GgrVGBL1BLmhgo7lS9G/aSM6st3Inx/HEB2SwyNncWz8AoZOnkP++BXUmUaDvFKJ1FEo6ZVIvcUZQ5J1GUt0mEDr3fggHhqoYmV0CFOXz+DcyZMYOnUGM6cvYPzYBZwdnsUMLVa9YlrBDCrVImpkQbWOpnGVqLjlbpXImvlkJ2qrtyOy4T6sqZ7D9Hs/xptv/hTPvb0LO9/YQ558H2OHJ9jOUTN/ZyhsCxRtNfJjpa5Bx6y9GhOpFDE2W8XZSX3uOY9M8Ty6a1eQKhRoXFAcxtMUtqzPKI1qpqWFPdWCms0YibJvxIv0G/Uqb9LI+k6IEB8TkoWLdfCrVX6bKaOsmsqg8cBtiX1hOkVDnydjGrBO5ZBZtw33ffaLWJGjhL10BsWpSeuTGvhiJ2dCejI3X263dTT/muNHoYVBsC7uSGi2Fh0gzaKN0zAV2WwpEkUc25ZGZjSJkoa4WK3yi2L1BhINzeaWdVmnPM1ihjTR6MBkOWoPKmKNWXREKbgb+opxjXouQ77IUKfQcC3plQIeT57Anp0v4kd7JnA29ji2PvkV/OaX1+Dzq0o48ZM3MPb2KUxFsmis34KBFf1YPfkuxl/5M7z38m7sev0kfvjWFbx0oQPTnZvx4LbVdO6AYoKyPhUjH7qBOQ3eeZ71bbWY+1c7+HwH8x+Ejv05j9bjhYbrhfPuj6BurD2FqV1s6QvyT6J5LF5sxLPUtT20N7Zh++d/E1/4H/5f+JWnHsSXHtmCB3Y8gCXrNiM3sAIrlq3G5hXLsaEvgr6Y+DaJer2T2j2LIlmaPhR5Vx/6mTVedp+mt2zccbjdbRnig22gYx8Wrc6gNHwCx995DX/7dy/gldeO0LaewcGRYZw8+CbO7vw+jrz+BvZe6cNQ35N4cC3waO48kufexLFXX8DBnXvx4q7LeHHfLE7Xl6Fr4yNYtTSJ9NjLOP/uD/DNH1zA3mNdmBg+g4vH9uDAGy9j364XcPrAHsyeP4P88BWcO3YR7+46gFdfexvP73kLP377bXxr9zHsn05iXU8PHuzvxEq98sU+WKVPVo51oRbN0a6O0gvRrEqWx3qnFHknC0iKshOxL1lnDhHCQC4Rr8yRLAD3RpSIGrdJhMl76n7aCprJGKUdoAdltVIe5elJnDjwHt585QXsfPUNvPL2Gfx09ym8cGACk5E+rF3ajx0r4ljdRRleGUe9NEL7I4NZ8m6edkepMU1fs4gcbYks/cwI/cVyvI5KJYJoKYU4/dYKfftCqoRUvYJEsYJ0WURdoZkTsnkamv2lvNVsYo6sGR7d0ZBM8vaA3/fw8qoV6vEhmmgUS66iyGjaanHiI0eO4uzZs7YgbT6fx9vvvIO//Mu/xH/4j/8B/9d/+S94442DGBubtAUavbQ0ucnKb2estQtfTNCrfloEPZlIWj5nZmdRpYOWy+Vs8fb+/j6GKyLrKc4O2NGB5ctXYNWq1baIrxa1r1Zr6Ovvx+DSQXR35ZCgLpHzkEqlbfH1PqaRTqfR2dmFDRs24uGHH8KpUyfx13/11/jv//1P8Td/823s3v0m67uATZu0eG8WyaxYVXUs6NWAKLSAfDbbgbXr1trCr2JxLS6c69LT8iV46KGHrN127nwVf/kXf4G/+Iu/xJ//+Z/ju9/9Lk6cOGGfhJUQ0yLuWgSzq6sLWmNA06cHli/H1u33Yxm3ytuf/vc/wX//b/8Nf/XNb+Cv/vqv8YMf/AMOHzpq5VJdDbC8PT3d3JdgYXnJQ/F0FgMDS2zh4lWrV2Pfvn12729+85v4sz/7c/zZn/4p9u55F7PTZV4TQ2d3t9Vxb3cvqhRmrFykSJ25TlvIXovhq/60cOHDDz+Mixcv4m+//bf4o//yR/gLluunP/kJRoaHWT0R+1hALtdhn4TWtavXrMG6detsYfu33noTP/zhD21xfi2Sq3SXDg5Ci9gr83N/i5hPQ4S4HdAUchnSkj82hTwWtcXr11MG9fX2UK4lEEvGkOrMYe369Xj88U/hnk33YOnyZciyP8YkDLXunoRViEULqXNpG1t7ie2tmduSiW6wMkaZ2kO9txwDSwZs0Vmd1SuG0gVR8oZeZxCPpNMZ0wv6vPiFCxfsAyb6+Mm92+/F0898Fg8++ige2LHDFqHVh05mZmawZu0aPP3Zp7F5yybse38f/uAP/sD01q7Xd2F2lucpy+/bvg3dHeRD/tni0Gbgyfj7oLF3LeMvxMJCbSXeoHnONqvZIsVazFu8JR7qpw2xcuVK+0jS5m3bsI08smXLFmykjbSesmTDhvXo7x1werrZpNLQoZYOcatxlS1IeTMzNYXTZ87g8uXLdLwrOH/hPL7//e/jP/2n/0h59b/jzyivdu/ebfa3Ftl+4sknkUwm8NJLL+KP//iP8bd/+7eYpT+1efNm8vhms+OHabsep11+ZfgKSuWSXf/Hf/xf8f/73/43/OH/+Yf40Y9/ZDbv8MgIXn/jDfzVX/0V/uiP/oulJ/v3e9/7ntnwD9Lu37RpA23grJOHzLLJZA0021EoD0PcXJgcZh8Rn9lHRtRfxHx63dD0cx0H9u/Hd7/3Xfq4/43+5H83f/T1198w3pec30Q7UR+4GRjoMz0gRGlj+g+e9fT0sj/F2Y90s6jZGlqeRh9U0/3kD4u0wL38b53LdWiNT8YX78uo8R2iubkboeeeVvbqTTKMggaWGkKKXV8hECSc5Gzrq36/93u/Z9O3BV2juCK/v1C4Kr9NNqjX3Du4etWxOPQujdWLKGU3YaZMg6UyjVSsZJ+FvlxbY4Mlq3rK6M7GyJB6NS5iSiBjnPlB3Kqy+XoLlkf7Mqr05T598e8//h9/gDNnTuMXv/Rl/M7v/AsLn2F2lKMU+0NcHSNaQSOiKZDEbJHlreLixCSKkTi6+5bQOOsE+xUa+TGkNDDGS6YnpjHMOHk6ez09/chWoygWipioFhHLZbF8YABdtQhmNdp94TSyHSks7e1DF53AWq2MyaEL7kuQ02lU6hFkYwkMdHZh6crlSG9Yjp6MFnMfpUtRRzXGayJZ68CJfNm+zDjOfPcNDpqSi8drSLAK0vkKMDGOIxemcXJoCGPFEVSieUTjKSzpu5cG5AYsWRJDhh1g5tIM8iMFdFPYlFd3o4wC+mmUxosVjF0axtnTZ6lor7CuJhHLppCIPoIl/RuwamWEzsooKpoRN6aK7ES2qxuZjgQyiQqSEdZfrY7xC7PmzJy9cAYTUxMosU000yCTzWHTtvvM4YnEmYf8OIp5LUE7gP7uHuR6riA/NY3Zybq9whlJp5Hs7bZ2S46PmoFw4MpllBNpLOsaxLJUv325o38Fr6FzNDwziFq0B725EpamL2F6fBwHLyWZ13EmVkSuM4lspof12mMG97JlneQZ9UM5dnTuaVzLUDdeiFS4ZXhg4BF1TQt3uyFCXA9eLmk7PT2N/TQAXnrpJcqjM/ja176GT3/60+b4eTm2kDrgegjKUyFC6aAPPTRkQCif/Bs9fxnj45Po3rAaCRoomivaEaVslMwbm8TQ5SsYSTWQ7uvB8q4eLI1p0XH+J31fUlLz5V1MZZf+8F8R0oDNrl27cPDgQRso/63f+i0b+JE8Wmztdi2oNX2L6lmtGYNzMk3SjWWhQemn/Wviq141j1MmRuslBlAQV/OYpk45VepCLd1NWd2Jga4MkpSD8Qptg3qBNmmJdVbE9FQUU1PUCzQ+a6kjuHTpElKN1RjsXY2+niiisTFUymWcnojZOl5LewZoS2S5P4KhK+/bF/suXiwjm1uKXO8geinfB5bToB3oYF7rSDaYX6q6ZIy6NkbdreNGUy434dvEb31bLVb4/AXz6RwHdzw7O4vf/u3fNvvx61//Op544gmTHUKQFxcWQc5ycEf8DQQrb0YW6PqLvoJ3dX51Dak4g9nRYYxNlzCbXYqOjg62e9r6ZIrcmyCv1ngdzVKmRB4A7RtuI5p9rdcfFbjQ1dBEaxvoWG2o9hG+/e1vmz+gtvzd3/1d/OZv/qbJmOCyIAvfhiFaoXYLboVIrYJ6YRozY8M4f/kkqrQVx3IrqRnpA5FXOyoRpHOdqHTksGrVSgzUziBensHJy8M4fO4KpsYriFZz2LxpKxJLaJ+SOikH4+ULKFHEXjolv6CG0UQZ0ZTeQnEDBzn28dX0MbRW7dTUpMnGS9NTmGDeGvUolveutPutWbOC8iDFa2r05erUXzHEY3oswXJQZno/T7pbjyrmMF/E29Zv7iaYHGzylfq62vhb3/oWXnjhBZsU8eUvfxnPPvus7evc7ZEJyp/LIyWakdu/GuIreyzG8uj1cosh55j7VTJ1pVTElSuHybPHMTJWQxXrUax3I5Xpx/r1q7Fx7QQ6s6OYnq1geDyGQj6BdWs3s36Y5uwYavkJSvcIZnr67CHa0sYEivRvL17ifRL031Z2Ip6dtHxFDk/QTInhykAPigNd6EtHsLLBjiXIZ2Md6o1HvbGg0rjRmcUHtbmgNteYyqlTp/D7v//7GBgYwDPPPGOTWuS3+vEl8ZLXH4KOg/wSb+7f9YNegs+zMSt37TO3JFsno3YOVRql1eQqGsIpHhcRFQPFExhDDgkq8RwNYhm8erJrMwBUhkA9BOHLdrPL6OvNl0XQ/kcd9GpEyixnyRbPw1ReGUVZC7THU/QStIB8FEmeitOw11onDGBdaZpkDCUZNGS6tOZM8lyJ9VeJR43ZskUaNAka9nQctH5VTINKjBahR1FnWJl1PDSdRqFURVcygd4OOsBUcGNUesloBP3VUcZ3g16a9imnM1OLolKt8D5MSF+xsDbQqyo1pIvMVK2KciOFmVINE4VRFGpTSGdz6OpcwWwmkEyUbHH4KBNoaOV+5v1Kp14/iKKXYileqaJerlJg8R55rR1wEdFMErn0BqSSXUgmi0jEJ3kZjc8ar2DdaElh1VmCTk8ykoc+GlAr00FhfRTzU3T4J1EoVxBPZtBFAZakIrfF9COzrDNWXC1BYvmqrMfOEdTZfxrVNMtLJR5jDTCuVHWCRkelWMRFCtNKPInuZCd6aOwqL3Fdx/vNVrpRqmeQokPUFWcYhe9UYyUmJmfobJVpGMRYjixbLm1Pj6MyDMQPNGK0FXQvJ0nDQa8QHx9eLml7Jw16CUGZ6qeHW5dQ31CvKFRQo76o0dCuUYZoOaaUXgkmaeZorey+uFNJRJGhxu2mTFACDVt9+oNYLGX3+uOuGvRi+1Dzzw16VanfbNCLITHpfb17Th1Zp76ajvezvdPmUKWoo+TOx/XlW+pGRItMh85ajTxR6aI8ZlB6iCqJKVd7qB/0gKYMxKYsP9OU1TXK/CzrOkH+aDTyzMuIzbLWUjblWpr6gPZGljKXOhUJOnRMNBtLuY/T6AtkzJcGvYCssj4H3yZ+69tqscLnL5hPGcD++E4Z9BJcSDOcG+VNM05kJ2qwSyJEs+sVLijfUfJSg/0tUtX6niXaFLSb0j20Eaj31fZMKMFrzLZgmAa9hHDQK8TNhudLYY5HqyWjOvVgtU75xWYaSwySF/UFRsokCU/KxDz1XZQ2a1f1Ijm4giLDpwsNFGjqJhvd6O3rQIE2fozxUhinSBsxE7haXGe6cZosrNe2jZeYZJppdlTKiLAP6N4F2hHjhQKmeDJGOdzf0U+bPG76KpHQYLJy6/KsATD38QiXlnS3nQ4ar/NFvW395m6C2nWOp9jX7+xBL1kN2qEyVl6p+xVbgVZG+qLV+hh9yQnyfwxThUH2B/ps/fS+MnFk4udpE8ywIjLU9T10q7M2k4vqH3H2tai+sk/+nUqm7C2iJfSHdddqJUPLJE3/vEo/eBSJWALZiSx1QAJjTHc2FeHZOga18JdkK302laHGfqVBLw3UyQ9fjLhVg16BHn/3wldMRZXLStOXAiMaRNE22U9Dc5BCO4V0nAyVzdorZ/FUCl2JODopXFPU4zHNjKEgjpC5o+LURQgpJ/vqjxn53PJYh2ICqwL+2JNiLYqnyCkakqk0Yiy3FEaM1r9sLvvSHx06DZk22MnqeqWD9dXBIL2F2NAIYCqOdCKGLt4go8E0KiPVbZJ1mqLBZ1+AjOmLiVpcsoNG6wAGezuxerAXfUs6Ee+M00mIoJuaq1NZi3VQAWZZx3IK9BVIGXx0GnigAZu40lQhyOhVdRYtJkxhGWMeOjszGFyyFCsG12KwbwU66ZxKgaYoGKIVKmbmK5FlGdOMy3LnWCONWoLCJ8nyUSjlgK6lHVi1YhtWLtmErp5OJFnYqGa6xbp5yw4kowk6PnJ+6uSHGgWYXnPsYH3ry4xikDqynV0YWLYSy1etwZLly9DRTScmQqeSdSSljShLyutisTwSGTlNXbxOs8CSTIN1z74dpbGb4H1qPEjS6F+xZBCrejU7gPfJJJHoYJtEKOZo+KbZWD20f7NsG63nVYtnkUunsGygB0v7etGZzbGa4kixrmKsD8lrGQpiBdWjeKPJFm5rv2zbOQoR4pMPb2yZnpD4ZD9gj6W+SKAkeUn5k0glaLTT/NBgPqNV2ZFq7PYRGfU0ProY2MfwLDsVxSuvtaQ/gKCSDnHzoebzpHa8mvgruaezttX4kpuJ456oaCCBegXSd7QD2KZpBunBSaxKUa2VYW3QiXqz3s20eihXs7QVqmgk8oyQIZ90mZ6pJ+gwMs26ZDzjaWZgJ+VwMlEkz9CRTNRRjy+lfluB3GAPBpbTQKYwpyqztbw6qnHkanE0aPxGIpPUjRGmRxlP2R/koZCfFhKq6yD5veYf28KTd/bMKGvCnYvaQKc+INOIpRBN5sg/HUjRjklRn9uQkQZONYqqa0gKE9ES5a9IgoebECF+Rnh+vWo/TkMxRaeeciyaWM7j5eiibOtNpJDL0ubO0a7OVJFLztIfmKTY7EG5vpQ27iB6u5Zj2eAyyrMMoqkyMkl9RIR2fJ3OfGSZpZfMJel2JJGjrOukWdydSaCLtnxKH4eKs0/QZo2zP3TQDl+6bJA+w0qsXLoUPV0ZdDBukn6K9Qlm1axU+gNx+S88VklYivbdo21giBAOjneuRf7XbeuU6yLJd/uKInk3Hu9DJrsGPf1rsHxZN9asTKGzh/4X/dxIrItWRz+v7KUPmaNvSl5vVMjLVdD9M7MjFm2wP0XdIy36ivVGxnzCVLJiYxDpaC/94i76zexb9AU7eE03/UsNi9EBN6qy/+qjJ/alR3uQtzjHKm4lQs+1CRPmMkK5NYNDRq6qR8xCQ1KDPhorok9D5nSMndQl4hmNFmjAq2koGzGN69HtgTf3Sc0s+Pw6KG9UZNG49ASLzzLToWOgO83yxRik/Osps7kHMRrejKP+rYE/zcbSfCA5dlHGiMsJVP3QYGvQMFdSeu/ZvlxE0lcPNYQlRyIVjyFLL0KTzKqs2Eakbt9VYQvwOsYhSZ3pCWdceVVeKAgE5VApMWX+MT8WSGHDMsSp7VLJNNOmMKHS1GCOBu/iPB9THLtS96C7wuOk0lYeWTbNREOMJYo3kEl18/pOhivvvEDlZuyG8m/lcoJJg1jmKDG83mD9aJqrqpHlSzIf6UwWiTSNU8bTV5zEVDVWmOK6+1IYxasoV5IM0ww73Y+1TdLAXkODqsoD85ekRExry3zaBzp0Ww0JRihkmZYmk0iu1Xgioq8/8rwcuQSvsSdfzXK7vFsxHDVZJEjtQkKEuKsgwSJxL6NGckbyQw9H2JckDWKUkSZN2Kk0hbwq51T9TZKCclDn9SV1ycsgbq9euLugJhSZDLM6n6937Zlo557tN6NY20gOU26agiJJxkueuviMI52pRtezUzMyU+QT8UiVl+mOMjMpv/0FTMMGKur6IAh1Gi9toMQkCtSrTIx2B/TFsWSC+sLphUidaVH+J6gv9GpjLFJmGmVeR35rOH0jtPLTtfZD3Eqonq8m6Xfb2jH3uDGdL13cbDOLY7YX29IGWsl34ljKD1019zqktjpukowM5+67tEOEuFmY503xHXkxSqOSTBeJpo3ikl8M1uk6BWEtonc/ykhIPlGGRaN0xBkvSrvUeJ32bYTGqZYskd/g7HstUpijb9FM25ZZEblXx0wWq1+IvUl60J5MpZBN0abWg3ed5ymLwh0NLNvsDx6IbOaHuzREiI+F6/GOnaPsFo96MkbWGYWzH0SiHbQFMkinoujQ5GTyvmzBiB5W8ZzmZUXrtC2o/qPqZ5r6SP6PkLk1A9i0O7tHIyr7Qn6zrq1Z3BjT0JxJ6wBUA7In9NEG+bOmR9TbuGv3Y7j8cw1+3W1Qi4RoQsM4+iVPGOlQgzJybvTqlwSvBoPIcxYzTs7UWV03fyWrlMZxUEkEabHA5diVc668ghVEHbRpPLGHmFGm/Dev0eCIOrERw9R5bPDGrlE96ct+VFbqUBZPw0pVdsIqT8fZ8RjPSFcqQe5zR53a3UN1ap4ltCaWkjFzby5P3PCcOrdmeWmWkuWfRqH2NMuqxnzXmL6mQjezYDnzT/K1XpucFBuF531tYIrhGkOL6NUBHmmwTANcEjB66VHtLpIijtv3vcqsF96TN1C4BkutTNwqeyrCXJ2Zs6QBVVfzlg/eJxLX95wIBprDrOtjKYbFWRyXV/GTnGvVtM67IA0v8qzuwWMroztFUGhGNfDFaxhgxNzGom6grWGj+0zb2lTnXdndgKauJ3SB73UHAAD/9ElEQVRu7kCpar+VQoS4u+CkHTsKoZm9Mtr1anVVsinGPse+qrP2RUBKBZNjko0KtdEO9TlqFFk1TSwmvXD3IVj32peskxzWxklT/ep1cY1f6uMFNhhB+Sp9In0hjpDsVRMbXBKO1P4kzTSwoc8G+YPtLbvUHtio7XUv8QN1iVuTy74vxjDKZG5i+ty+hfNOjObWk6MMp+MZj8hyplw33nJo5aeQvxYCN1bHYilZQ6Z7rV3c1g+GmaOuveY5p9i1b48SFeJ4yeIT1OeSJ0ZzPNeEIocIcdOhh9V6IEt5poGrOG3gaJFyrUAe1CCVJKMeUMvdTtJaJjSmpRlifk1Myqs47dEIZV6ccs4NSonXxcJkYqYrGSy+ltMl3jYfwwlOkvwHrffFJOvO6TcwQGxvrK8gHTcP5mZXhgjxM8Dzl7FVAJ673EMMjQGIRyWnHckHM9KokyKT9/XAKkJf0pg0okej8jwZW4c8km9mHE2bI0LSJAbP6m7yBQ2Epl0gF1Z5UjfS64tKkp4gSfnQGW2cHlG/sNEv0V0GtUaIJrTWgrEYuUpPcMUoWrOjFtHTWAlyCmIK3TqFrdZA0+dIk9GKE8YaYBBjLXpGUq+Z22sa7U0o6zyuVqVwqKX0CqI6MEmzgqSYdJVdbnMu1eF0LOdPukkdOoZ0pEhVV2S4EneOoNZDiWtNFKZVYzytDWZpW6eVwlMCLi03kKQAds4q97mrwUfdhTmzeDL8vSOi2VUafNSrfxo4kttZYd4rGixSGlK7UpwUCiqrBt8ijQoaZbY2y6onU/U4FXGcd1Aauqde4SQ1GnG2f5Z8kLHPu5INeH0BicY0yzPbdG4pupiPCkkiRaJMude9dE5C0BZHZsVpaqleMeWttCyLvVJbiyeQ4Dape/IGlYbulUGaVaynYBp0rdpTfD3JZZgG4lj3zgRm+roZ8228y4ao1XmuLgEasRkGiaRmrOUYn3zMWAmttcB8NK9GrVal3cBcM8DCmJ4rQZAEnXWlchQixN2FOuVVXa9lsz8nGmXE6yWTC2XKp7pkpox9dhcNiMd5JhpzOsUGMTSTkzHiUckMPRRwDm+I2wMn1UziNakJ2gHS9dIx5ig19YwepFg7yh7Qxwh4HG3GdbqueX0ASjUaFQdoADRB3eHW22rI+aMOUroWKUZloBlhkQ7yRDd5JkN9Id2k+1L2U55rVlgsqpkSik9dGi1TT3WhUdOXizXzTPdS6kyqyVshfy0kVNcfRvxlm9hMd2MYF95kM6NKvco212mel7Oj+JQl+piCLJq5V3DdlbIOjMwOUBraMFkXI0SIm4tGJENu6yafZlHWADx9oERskjbsBPmwSJs4RkmX4b5mruQo6YASmbPGeNF4CcmULFrKwQZlGVPSA+RIXYvOqx+Q17V4faTMNBpIkvcl+ZrPBNCQY6bBgYj8D+pbhqHGvkH5akvMkPTw1mShHSvDziL3bzaECPGR0JSrQYiPghQ873YZShvRTdRwJN/YfGQ5kRL0dX3srEDeneU1DfPxapqpLV63FGo28UKDXW4Wt95CAjoYRdDSO9IPNljMvhMVMbzK85XmQ9UEr9HAlxKUTuAZEnuk7q/XsZSXuwx3X4mvA73qZmKR/GA8QTvU7A7Vkj7jJFCKyuGxhd6JWkVfTBKXunBtnSX7QdhTvADdLnzgzoEADeqlUjLoGWgKTSa9y7vAUrJPyhmwvunCSdpUq6746uz2xRXWma82XalBKkFrg7lZXdYLDao6aSulp0UqJQT0+mGKClBpSnnNxda17PAajKtQ4SmDbsaXC9P0aDczjXlkppSm2lD3MOeF523h9gRbm3nRgnk1n1FdJGGiRHVPptOqKjW8pATtDmISIs5LTAYxyAZPNZuqWV5B5bkKKhQvsPXHXIBLk5nU3ey1qCZ0H5XLTe3WWXcPF+aOlbzqVNDMN5v9pvtbHjzxV1PHGeY/cx+PxW3BRHt91yLo9A3w54ecDhHikwh1C9c1XAdQ3zS9IZnE7idV0LB3jElam8ekJNHsXhJA7tPpIRY7JAPVktIl9tDHy3xCusz0jQYvuK9ZuQanDqz5rc2t3aUxtPC8G/5U+2tr9gLhVUCtVDL5bDPBSM6E1SAIZT35yx46iXRPbaWzJOs1m5nHSlUUYvFC7SQSxF/GE06gGH+JtGSBtXWzKcUm4jxrX/KZ4xuXRogQCw2pL3FfPB6h7ShbmZAsMn51elD7XiZqZqKTZy6Kgr3M82AUI5mnul4fqFK3MCnY1K1ays73laoe1DIRyeBEQg+bdN183/L9SsfqU+46d22IEDcbTbZzHMYfsZt4Lsh3nseNR43ZJdHdny63PqIdRefpINQHZIPM+9MevIZ9IJaI26xwb4Y4P9InNg+FmV1hSsUy0zxz96Clau9u6GlZwp6aufk6emIgHjM+S4hJ9LzAzpDIYXq9hUK/HklqTJZhYiIl1J6RvFD2tNBw3U/3nb93nB1v/l18ntcp6ydUZprNRQPbXtlhJxGzaEaVqTnF1SaS4Dm9NhdHNNVAVY9jqklE6lm7Tqv7muNXTyHa6HA127xW0O2aCbt7R5NIRrKa58S20OyuImqRImu3YflkE7j4zLDefU7HsqxufVmwCJtazcQ1Hq70RXrvX2XTAJCmhmqoMqGpYxrx1lbpsaFrbLOy8umhxlc72kh90tJM8WKt46anVBF0QIvD1+NpbiNucX0R001HqhbPCxXxhf50b70oqTW/XBmAjkYUKSrzaLTMzBW5rdhxhyqJ5W6QXAouq1ZHJD0js2ViuN/Qy9skxTFS8joXq6ERYzkjWlctZqTXdHWNBm3jrGsnBKsMb3prPGev8qrtDAr39aKbMdzWjXHpGIUIcZdA/U8zNm3tpGqGKkBPvV14laRgk3s1PTjQq2d6fZlmjeRinNJPIpEyU1IqxGKBhJgnjzqS1B1aQ3H+jCQx25ltp9ne0oSaY6wHrdCXGKNFtwClHVNuamV7u76DXNBFveC+zJhi+ycZonl/UjEyViWjYxk6b1psUpeTNC/XnuzKsWNcWy5Agt0+10jSSV6vvEn3pJW2KYgQdwJkA9pAqniE5OH37IMXEiXWxprl5SwJM2wUySLqQBJI5I48hQhxSyAWbLKh3liM1Sipov086qN4StDO1npesq9r5NqK2alJkmaq6uNM+sBTTPKR8tLNWOQveVlpau3cOnk5ntAHOSQB5VvIbqWM09gW+4tkcCxG4Ud56gYVNHuF/M9913f0kEBR1a8sgFsG2NlmgCG430RrlBB3OTxDkNroVh8SiGU856gp143IlSLrO9ohQ+sLjdTssgbIrcbXdoumewX60KhlbfaXOLymmeCxae5N8zR9RfYuvUFU1Vs/7CO6VB9Gs+WFeM76FhNUDzGblTaokpYvPedHi+4y3IVFDhEiRIgQIUKECBEiRIgQIUKECPFJRzjoFYAGP91cLo2N2rhrM6wJ7vhjF6an9SJ3hUZp52ZLLUqoufVusV5ZdHmO2tMRTcNUaR15aI6PGy92hXJ/LXXQ3NFgtp57qzaaj1lslFt3dKPdCnPzGyyMNHe/5k4DFSM9tXGv5uneSjWBhoaqmSG9NlmL6LUhHujJtyXg1tKZHyIPtozu5MmS5CXNMgnNzdxOc1R+Lpxblz1dobyR7DEX79dQ3vRXd21uEXWBS8DvuqNm7dm1CrHAAJh3palcuwuIFDciTVV1QS4v8zuqJrWTuHXu5Nw5PQuIwn06txnGY5GrJ1dX7mpPrfAJCnMZIxjGdjAKEeIugXqMkyvNA5LvSZIGJrdsRg5j2OO0Zn/x3Yjk5I+uCLHQUGv49mq2DHd8KLcm/3UsmtcUonZwTao/99ECL/MbNvNG+oIy1WbHMv05HtC+wsRJDtKzIt1J7OPI8ZP2HVxuNN/HxzdV4s/PxQtxJ0NNKm5Uc87rdvGMQh10bt7WdHwzD531FCLEzYXnT3ubQGSsJ7tV8kx8SrlktqdW5bI5qhbXm+smUb0MNG3qrvOi10k5RW7GsXtQltobHTrfJIUHcZXsvlEKEeJDMM+YbeE5ydP1YOeviux4/aogbwA0oT1H6g/yO0XqgW7muUgWiNYE1VGM57Suns7bDC+7mj61tEmdfmaN/ZJ9VG9gzS2/cRdBNReiCc98YiHBBK+HO2FwzKlfVZ8GERy0dUbIIoUyZxn01PxtFiBQWoOVR+Sv4YG/Mkj+On/shYSXE/NhgeMmgvVlToM6phzHZqpukKap+Ejzg0zzcVw7OMXpU2+9T1t8IAID/IVN8ndxd5IJqvzphBs8cucCgmOujolmGn7XhQcCgzAh1izDXBQda9qq4zYPy0szU81NW7hzzcTm4nuTwt9EdL1UPHzcIG7kuhAhPjmY6zXNnaCMM1vF9wcL8GcEhrv/JvnwEAsJ3yJX134wtP3Z4PaDcFrJ/uaSkE7wQxYM8DrBGt/ZDcEU52Qyzzub14eQdI3F8fH8fgBXHYS4k2HsQ7q6nX2ow/w5H948N7frrgoR4lYgwHEOQV1nrCc55R6DO73YCh/fycI2Fi7h5aSOvSxt4rrs7dMOphnE9c6FCHFr4DnOtnMs6PV8AHPnHMTqxu62w/7QYj+48/pV/1Ba7E9NQ0Qb5yu7c+79SvZL7rpr7j6o5kLMwTNTk6FMkIsxmszRDHJnxTXGUQq+ihYvlLu53Dfh9lwH+GA3uPp4vpTzZXXXGTXrww1esZNZsMIUT51uXmm5ax2alzVTbda9dW6F6MsrUngueB5KtBkQGCSzIFJzMx9A+KzMixkfw82l0p2bqXCHeyT9+Zy71cxELqFIQ3lzX4axdC05/TTL4EJJDv5oPoRpUiCJDHaSadFhsjWAroocvIowS8KFuVIEMHdOJdNZUiDM0c2A0hOFCHH3wPUg9SfKJfbTVmni+oSTge6cPzsfK+w3iwxzTRNsI+FqGefPXk1Og7gjDz+jNhhG+IsMPu2moerjt1zyQSiuHoZIFzVh14Q89YlAgOVs1wwX8oY5Ow4+ioum8Plz82gmEiLETYREzZyIMpuyaf8a8cxVD3vm4XShjyn4eF6DXgN2qhk3eLlB4c2HxSFCLGrIi3SDt3NsbDMZnU/p2Fz+n+zKps97FZp9YI7crzhfV7s+RGr2j2A3cTYKzzWjGN2lCCVFEMaAbqk3m6prwlvMJyYkCzV5xj2/IJoMG6VRouO5yly0DMUcznUybuxHgytuSMcNVs13FYXOHc3tzHWfZjF1onmdGWfsfDZoo9c9dFr3owNgx6zHBrsmT+ha11nnLiOahrzaoK4nRHID9IJehU3RvIg0pyLdRdpxpDhM1N6kZIhL3+012Jb+Pv4JlK5SQvpqhhbN16ddLWUla/XCPDO/bplYLffenFpq7xUopobB3IsmJs4UbFO8xUNyTJqDYs3s6d52KQ/th1SL6lPOqj1F0D+PWVciHTtqnicpayJXiTwW+TAPDZjJGWe5zDkSH/sw/+cqwtH8joM/5H3nD1rvojCVWqT9ECE++ZiTK+pP0Qqp3JQmgvpUs49oqjnJyQD9zUsk15vVb0LcDjRF5xy068jLOE8eOuOGsFwLNokX6bWdKPWbtEfE7AbHAi72PGfMYe5iT04uO+2jLxUrsHmOVxsFghwvSU+6V9/nTli8ZvwQdzakd6XztdGhGtjbbQrQIUmWqaTL3Dnxgah5VYgQtwJOFpK8ICVJm7nXrSn3zHeS/au4TVg8catiSeYp0NvhjM+AueQYYlqScZws9SGBOAw3suvda5QMbgPdqJVChFh42AfDUOZedY630aAOJ0VoQzjulO/sXuVtD/UVkbNEnJXhjkxPiNQRmp3B9wmlrr9mpyGace9CqK5ChAgRIkSIECFChAgRIkSIECFChPhEIRz0aoEfJNWMnJoeKTTn+ei9WB3peYM+LmofGG1GjjbcbCSN4kZRYhyN5i5GBMeFm01vs3n8LC/3vMZm7zBYRyLFMDTL6+AONGMo0pzNVWWSokg9gWg9yWtjqCgswjgME9W535wo5ZOYu49GuW2JXptFwQCG6BPIIs3sF2kx+RgKPF1ycTRYrfeUa7ySCavmNUY+N47dfPKkVvNPRt2TJZHFsDJE6zEjhbgi6rye3ut+E9ybQlKZVCIG5Vafkk0xKGnX6fPNyrqViWnqw7EiO0lyL7zwJHlJWRbxrvZXj1ZQixW5FS9p3pnKXDByT8jmxur//+z9d5wlyXUeCn7X3/Kuve9pN95bYOA9KJJ6JAgaUHg0IilKWumnlZbL/Wn1ltTT/rHik0gKBCVSJACSIAhoAAwGg4EZb3t6uqfNtPe+q6vLu+vdft+JG1XZd6rN9LSpns6v6tzMjAwfJ845ERkZSdJTMD0RcHxopVOm6+m4GiA/VnmP+Y1W5V88rA8EWPJTdX+xCAaZJvcXIsSNArdhOfuSBBjlmcitD3X9Uas2bfUF5V+EFGfvlCRRXy/zpGof83B/Ia4FJK8kxEl10eVkmSOJb9GUMLUb/LHV0E6DsCmNJIfdimD5Y3uTnLuIvGErsST/JYRF9G92hNtA1nGS0xHSG6J6EoxPKwUn68Rroe4nyjSdvVFyb0GQFFM1UmRWzvWEOMR1A7U/aVq/ir/IR6I65MVYxXivfo+nkkNuTYwxrryGCHGZISubcol2uFZ2lUnOEuUIiPZ9nkKwGJVdmqf+y9Oedzzs5KLjyzIvRHVWnx4PGJyrk5Q6U9xxkvicDuZPdnGG6Rfp7rl+Or4gnRX1eeF9XpzvEO99iBMuzEdBX+cj9QCO1thfOFw18m9auRXjiknj1CQ1e9IZGWZQkNcxRsoyGjqQbPxnip8hGIXGsOojWkvm3kDQRx/MEuU9hdHbUxyvRstG6lu2Ql33bjDceCUOcZmhbnU23ubydi+XABeJVmfOCryLfMyWIoQIESJEiBAhQoQIESJEiOsH5x1LhgPNGXFFJ73K5TK0R0W1qllOTVi4VvDX9rQ8AF03+rm68E/IKojURHoamzDSbKxW/egJrWZTtVsLIkUjrVyy9Tbai8rTVYavS9VfkKLR6NS59p+KR7RySSt+tKJIT1u0ykj7PmlvMh5tOZXKBiQYpcitTtJ0csUR41Hr2Dv8SpQ/St7d4bmakKT4YwpP8k92fDSCfVWCJH+OEfUkU/uiKA9yVACdqww8yM2eoDeTpvczUZZdtrWGS+Wq8w6j91Rj29U0U44cYhXWCzOj9tRTq3KkjDzjKSgN5c+C+xJqLZbSa3JliFVRi/n9epheNWakZLQysBIlj0SLvFe2VVYiqxRGp6ey7ul+hX8lI2sH8T15JlJLkNQGjJ5uNdaF2/NAedHsvMK5XPlC6ymYri3LagSjOg+qwuhNR7cPDFteZSDZajsRXbUfgqtXcwhA1y4uxcAr1wb1E5c/8bocQoQ4P4Ly3sukSqUuDIigDJu9UIeSnNLKCgkd1wfVj9QjdGUrVY3cOg2Reui0bDqrk81KNOpmQW4i6ZRYTDqDJW7w569nCj87IN5SG6rtzMHaZprqNoCy7xWZ92+ka7WhSVx6oW+RzkVTJ3UyBMOKT7Rq163xFSfpjsli0ZRX3aHeqYl4Krjg9Z86D1K51kRTe0nqeH3D93/Pb548ZBvKj/hQ516GeH4M+r0eQXPCKE4lnaayjlcrtDuyRmYA6EE+2S8mfqU9V43k2f553qA9yrL71fdmy11lNLZT8Nq3q7ftg+0sN2+rhpjtkIxJUixpZQnbkyQJKC0oCWQkHizzjCTOzFEXls1mdXzp1rdyJEX20J7I1u6Mtkabv8q4q7Zyln2ckUfZDzxNG+hKRft4Odtb5Oxm5eVscnfrK2POS4pXFOJKYSbZ7N0a+77cg7L9WiDIR54uFc4CJN+yD3AYybHxNLOKtW1PaF46UrkLRvFKDMlyM8eSSVRieiNI41bZEOxPqhf3r+5D0gXPSLI05KZhtHkg+bcMtI+1ValolkNtLxI/zMQ/7xRXRCv6jOnoM3w++PsX8nd14IxebwCLUW1ZraQpz1jtZEd3d2oSSA1iIl/VaWymiK4ZPHM0kgR7pEZFQ6URU/bpUqWhIaNdHUjKqGaGkrvpOpHzp3rxdSBytaO03C0hcGpQuHpsbmLQTurRWEAHOYuc7+n0neP0XQflyE/S1FH34jZ1dzQFn6mahIiMQk000a+KYW5lZqmGEsOLpvzXy6mII/b6ol7NVBnqgdnu1upSzCTBXoGlu14jVNipdCwtH7X+3MstIvs0PW9oAOQmpqZ5x/GUz5SLxMUhyD1QWkWiM9WrGRcz1+NUdnhp2bY+d3ZLT0PXgTapw50Fw4UIcekIDnZmhw44H5Q/kuXTkZc6wlSPNBnh+mvQ3e7NYkhP+MFqsC107kmY1ikO3j0YZvZCeQyUzWi6fc5uI+83GEb3SXbp3WaGtMfZYQW5+j8nXe3kLJJrg56bgg9F8v7tR7LYYrtu0chXQXh3yQt/HuRLuWmQdH3w4LnhdbMeGGrLBL3OWrXJLQ526grc2QziVdoR9a0L3MCdN6aVO+naoLEN/LVvNx0b5cxMcifEbIRkjLP9zJaUE1GXSEYm2eqzt+JMDdNlMU/f1ZX6qq5k+7L/8tyI8Yp0YTa0kc4VXqnJwedhWlrrbiNNox7ugiT4Y4jLjWDf1rnIy4TGfq9ryXp/Lni/VxNv56VLg7MsnNR2k710rEfu+D5I6lnqORyvV6OIVbTND/uFjS/VdwK5qp+6g35dL9R5/daUH7lO35m9UDvP1Nbncn8ncBx1heAHM40M6xm5EY0F8tdXi/hDUsL1U5IXuvpstJvUYnl4Q26OU0W6loML42jmNK4U+TptdPeGhD+vaH8nnnvDUU1jOXfZZ+nODj9F8jJVNnch9wZHRw3uLrz7m76vQ/3eZaN61HauclNwmAOTdSm7U38yRfTPg6F+HaSzLu22/QYc6qfGI1NO3jHowU4d1Cck8OXs8m8X06GnTv0tZ+9KHLr7ikH7dYncJJ4520GXbkpPk7QujNLQPl/yrwh9uiGFdKUpCF0HBzhB2SX3oMyafWRdx52zV9n0v60KZi+ju1ZzThF9+Hs85X3197P7/PVCQlCPa3LBu/ujEPTvz2cfKW8Xkz/v79z+6XpeminMhag6g9uFiD/1c52efe96IsEfzwXxofhPcsLLD4Vp5Mnrl6w5GyCHgKO/rHv0pww9fW4UjPfqUlBeeLkuCrrpqPYT+TYVFNbHE9JsIzWgGzjobRiRdJ3sTNncEbNH5UlwA2z9WQAFNgrowvqfLtzYinEwRjk56K5SEL/4cErLkd7Ccfb+tNvbyaK/CPJ+G8OHdKXIWpjHRhkRlO1eVgg+3Owizz8XoPrfTDf9qXqKk5zqY+7MgTfrNHMe3jskBPWHqPH6UnFFJr2UuSDDCjp6Zg4qOF8Az+zncrsa5CdKmDRJeY9SALM8uq5SDGupj1074Tw16UUBX5OQrx9FM8V/pcnXmygI3x4aiJWZt1KFftih1AZWIIZlIFv9xaaZKkNNcdbjlRc6oVwnN6FUJ7vp665OPmzDPR9G51WrJ1dX3m9jmS6GpsMyLlOISlIGMMunTJNMUZoqdfcNzIq75y7tKDflkeG1mbCLt55t3nekeMt1R+fmklEdO76xuHRfEfLC2mSKHN/oyZVz0n2mI7L0HLk6c/FWjLRWrWpU0f0KS8PGiJZYMt8wpAoDFcm0+UgVefotMJNluql+4mzzeJl5YmS61iTodDuQlBcefZ1OEdM6K28BCrqHdGOTlz/nu+fJ6wA/WPVu5XJ56t7sI/UZdR/1KeaxVkS0UjCSe6kaQ4n9n13S7kcqeSMTGZUYSa9k8fxt8c4Okp7Qq4tedwfbQef+2usUwbeZ9ydS2OD17CHlS/Xf2AZ1+efJ5HGD24wUjOPSqcL0PJ11TzqAx5nI+WG/OYsCYa8zEs8E4XnM85kgP6VSaYq/vKzQtXjW862/fz0Ss852VDlcuWW5aBMDURDBh6/yy+ZnOJHK744zxX+lKVj3wbYIyg/Bt1cQkj2CDx/S7KNahfymr7JQl+nV25hevyVvOrtUOq9Me1QKT0KW7c/2FBlTym62OGJGsmtlm9rDeI1LZNNWikZiZuNnHZmCNpaRfW09QWHkLh1LO10PlkxeG69Nk5OJFhXJjeHOT8qe49eQLi+dSy74cy/LG+97ueHh45g95HjtgsTyiG9VLmNIhlX/EOmSDE538TuvdaIBn+7z39x50MSyaOZ8vHdIkG6Q7rf6InT0+qLRLngn0NufFqMEz+WGMilm9Yrsq1/9Kn70ox9h3bp1+Hf/7t+ho6PjbRlXmEstzLuHq2wH5UE7Mzlowa1cVEvujI2iLywJtp9GPc++Gq9yEWQIeoNP9efPff0fOXIEf/bfvoRjR4/i05/5NH77n/0zuy+7Sh3Olg/z3FYNN7LCVNHqndFQZz4Ly3v0oy81CtoHLFh8hdA+UkKcskun1F1neQr6v1QoHZc7GYnuzL52wVN92apie21RUVfq+6TwWm1eisRRJCkPzZKtOrGvYFH4agk37wXjpm96YcFtvyv3+om+Wung9vrSVzEiWt7toWwwXl+Hvh7jviJmqACKtvqZA9W7dgGz8zRpanWXi2oqjhqTFWeqKLqlunC7gxEWhi71/Ag6nJW8j68RZ3mSN+eRnGPHECEuBplMBrt27cJzzz2HQ4cO4Qtf+AIefvhhNDU11X3MXgS7mzqTvaJhFgv7W0R7jEwJAt6rIlaTjBGSpPq966C7eD0ivZJIsFy8PnDgANavX489e/Zg7ty5+JVf+RXMnz/f/HkKhp218A04lcWz5ay7Ub8ZlIVv8x/w9y5x3hiDeQgi4HHGbF5nMHukTkHjVpAdI3fZMoVCAb/+67+O1tZW/MIv/AIeeeQRtLW1mT+hzMGT/M1qHjwPpniBJzapRVukFs04t1KnHaXjoQ2PTMu7AaFsG3vlK2hczZIqUNtpMOPb9fHHH8fXvvY1TE5O4nd+53fwi7/4iyZr4vG4tbXazo8bQswyiCe9wDEe1M5Dsnplz9LW9PdlexM5mslV8mGS96QhHdy9qhmxYlP+mUGq+/VxlexrMbA6Qd2fGN/Zrbr2cTm4HYzeDYLxzZKOcwMgKBe+/e1v44UXXkAqlcJP/dRP4YMf/KDZH/IjmXC9ynRBUlpcq9ca9eq68ZuNM2U7aoTm6sD5KrMf1Xm+wjGm8X0VlbjzH/d7Wr9H4dvbQzpdcxj/5b/8F3R2duJDH/oQ7r33XvT09JjOEIJ2g6DrYBzx+vlln/RSQv6oDAQNkL/5m7/BU089hRUrVuD3fu/3zFCRHx9G8OGCblcdgYpqzIXuTN91MMOkAZouuZpQnTXWmxhHBoSExrFjx/Anf/rfcPjwEXz6U5/Cb/3WP6UPZ0QqTJX+VDLb4M5CM3z9xG3U65SazoVoTRuwu86ro/wWXU9GwtlgdTAc7/lJoSTvqb70uVYf/0z1d2nQ9I4iFbPn7SxaaWL8Udv8r0xS6eLlpOXbTWnWUIzGUYi5Sa+mkgaydK9PiFUpXCq1dL3s/IlQGCFHPyqkeo8mvuIoccBroGDSPW1ObxsVMoZK3TCIakN4WasuInMrakdDhpFfV8NBOL9Vq3+VTv6cQaCJOAfLGf/kR5XMeC0unfHIcyXnY3b5VnhfVw7mP5D89J1zozG3IULMBC+TvNEyPj5uk16vvPIKjh8/jp/7uZ/DAw88gJaWFvPnEVRYswXaMNz6je2hU6S8LCNJmSHkom028eU+0S6lXUZzUZ+bpvyLtNCFMsKK5Pq8HWchfHtJN0h/yKjQgFSTXhs2bMD+/fvN2Pjc5z6HxYsXT+kekVAssl54Phvbz7SbTQqoLeuKytpLpHvmwENdlhoJdT+BdmOJ7Xg23l7mi7FlvC4UplINBHt7rGfjwinMfniekd3i7RJdm31CN+9nZGQEv/u7v2vy4vOf/7xNeulcvKr7PuzF1PusRC3p+IEkzR5FgZJj3G6Vq/Ps6D6lRCuTvOv+6Nf6myfPQ1e/Dnyb+fYTfPvJFlUbfec737FJLz0A+e3f/m388i//MvL5vMmaxjYPMbsQq8SMNKeVk9kbpY6LTRo/Jkppkh4q1+1hIp/K0y/bkm762JdsY9nZkqMFDha0T26U96JV6k66RSMTFq7GfmBjD30cSnvaketrFTfpq4/F6CMO6gdOHpPPzBYPymTfFyj16zb32b3Beo3z4s8bfIS4fFC/n0ku6FpyoVwu47vf/S5efPFFJJNJfIrj1I985CP2MNSv7lU4H3b24Fz5OZuXKlHyH71qvOz2aqSj2ZHiYH0YQpO2vGF2SZljPfE1Y6mmeC/OPlRBOa7N7RleH4l4j8PPG6ndxRsHDx7El7/8ZVss9eijj+Kee+6xh6+zZtIryNSe2TXppZlcZVpPd/SkTvBhBJ/xoNvVwlSazPp06mYmu2ueOPv47LxNVbN3Vvir3DGVd9V50FDQuai5uRmnTp3C33397+346KMfwC987ucZxvm1nDLvOioOvTpnTvUiMGY7t6NzYpnZrrzwJCOtZL2Yhs10FgwK5ye9NCGmaP2kl86tTi8LlD/FqLqYnvSSIqxEy1OTXomyNgVUWSVcasx3DIVofdKrXJ/0qq/0qiBNanbl1oCH7nFk6Udh1XvcLHwx4mbeXZwVE1gxLU1l4aYmvapeKYuUGutMk15Wl0xXfEXnqeqo+3WTjjrTpFf9yQBzYbBodFd+XLxyUp262vAGMX/kbvlW3Ss25zjt/2xcqF18nCFCeHg55BGU43IX6em+FNiWLVtw5swZfPKTn8Qtt9xiT/e8f/kLKrDZAvUxkzEyViJa8VkxmSFko50oR7Siy8mJKKm1PulVjHTQ1d+ToSNBeIEOdg0QNEx17icSdNSDk+3bt9uxq6vL2k0rvQSv59Vu8usnHmYfyIN1waUnpw7+KOjetCx1JEiOqjxqP+fff8DkbMzkdmHoy03CVIpMKhjTjSKLg7zn+SfoJgN3bGwMf/iHf2j246c//WncddddNkgSD/pJFZ378NcdOMiRbTT9det8w6QXZaNe6SIvGlfSj9pfD8ccIzhmcGfXpg5U/4LkgaC20Llvp6effhpPPPEEcrmcrdb77Gc/a5NeXob4cCFmH+K0n+OVBO3aGrJ6ih3N0hTWRFUVqVITkqUWtjftYr2iy2bMpzLOBp6a9AJaS7JDXXib9KrWJ71oB0ejjtc1+Svbt1r/IroN/Mtu0jcSlX1fZN9w/cC4XZNeZ632kpv4KCjz3dFBfSNAFxKyIS4ZXn57maz+rXNPktt6WPbss89i8+bNZgu+//3vx/3332/3ZFPMXrlwrjydzU/S8ZLr4n8/6aUHo4J9sdTGdHqQoTEeR3hTk15NjClhk16lOPsakdTqr/cwxBONPCK787HHHsOyZcvw0Y9+dPat9PKJScH5zGvS6+tf/7rN2mrpomZw5e4zFwzrz68mNAmgVO1pA8mdOSGqb5Dorq7dhIOW8TqGlVmigZCeYDgBzLgClX810FiHgjc82tvb0dfXhx8//QwGBodx91134iMf/jAq5RIqJQ3c6uF5tDh4oljcUaV2pPrw0GBPndY6Lq/ZijaRJdQXfE1BYb1Rb3M8hOKWkWYxN/ifgoWZTtOh7nnGMMqAiIno6ZOuys381SuKZVRjbC+WM05lrFj90x/NwJf1XVfeS2qiSuHrk15VpFHVZ+OZoBmh5INoJMt6UtszLVu5Je6QH8VGP3oKZSvh6CdSQaVeaFthpokv5se+lMmzbJLpMK6EBopMXz4r4h3mzVaFKUa1iUIxzlTVvS6Vi+nJAGEDMBm/4ljFHbHXS02wWh5YhkjUJvYMHKgL4nD59fBnwbaYvuvQeO29BoKEuMHh5VAQ3k0kpaTXk06ePIm9e/dieHgY73vf+0yRybjxg9WZ4pgdcH3RuJ59W/I+bjJDk/6UFXXDRUaLemSyUjdqIhzI8p7TD87gt9Ucswwm/yWH2A7eSPWGRH9/v72O2tvbaxMOeiVVk1/yI52usJrsUlh/nG2QxjHlQ0xNek1Nfsndt6+TvdPCTe2tC/l1/t+ut87VoOdyn0b9TSCXTP3UjoE0GmMJXgez8rZsXSfwvCd43vMkyLhNp9PIZrP4i7/4C3uYJx5cuXLlFI/OVr57R7BBjniCujtaJicWkKq5wU4Reo0zanaU7E1xgU0MkBlsosxCuvoSZAdcC6gN1J5ejnt5osGs2ujNN9+0lb6a6NKrKmpHnfu2C4YNMdtApmLTSP7FK05O6qH2tD7TSIo6oFIyUVvkCL9GGzRZjpHiPHdvVjg4G1lx2B51srujk/Vb3UyJg/toniY2STZz1a0Gj8i+p90cqSUovvXAWXnSKhhlok51+162tsl90tndQTa9juI53Tn7bojLB8lwL9MFL+v9tWw/QXJBdqGu77jjDqxevdr8Si5Ibvhw1x7GOHUEz4MI5pPjY3oTv6nfmPymq22NQTdnN8pFYzlnH7oRoupOLwVrZaXGkm78lqi4RRqXA7OhNs8FtbXaXG2vB+Qvv/wy7r77bnzmM5/BfffdZ/bnrJr00rm/FjThpSXNGuhopk4KUDO4gs+cz2hjhq8GNEwRJ2miIGqMx3qxJ/d6H11PFbSVovZ/StGbJkjyds/t+RSth9MgR5M805V/NaD6CgoVwRsQegfWGOa11zEyNo6b163Dg/fdSwVSQZkDUM33WGfzYengXqmbJquYqXMNCaRweMUgclHIWt3CajS0FMYpRCkgc3L+rX2Z76k8u7g9nEI6282FpOtZafhIpYBFLHesvgdGpdXc7VOvUU1kufQUa6QqQau8cZBnmaZocVVGZwoXutdqKZtpF2yQpAmtCOOuK2qjWhzVWvDVLMXvduDS5Fkl5ngpWabBV0kyCjc5JUyklU4Zab0GzHxVWCdldVzmeWrSy3xqEquMJm3wSUwk3CuXCqt8if/s9Sn618M3lSNRKzHOqvFiIeqUSi1Kw8DK5eL28Gdn16vD1D39zHB/Ng7eQ1wbeLkdlOfeTfJJpEkvyaPDhw9jdHTUntgsWrRoatJLOkFhGhXY7IPypJ7noAciJlmsE/GMh6kl6iaXVCfy4criHwTMNqiu1Q4yJnzbCUNDQzhx4gQGBgZswuHOO+88a9JLRxkns7Ot6qBScQMgnaptXFu5a7nX76m9nAIyWJtN+a/bLHW/02i8JqaqYoZ7ATj9Q9QP3ve0PA7mpX6cujcNOQWyfd3C2zKexINaJaQHpZr0+sY3vmETYDKAlyxZYmE8/0l+BGXHdYeqe4BWpt2gVS6xWgHpqnutpRDVAD+GeCVKd7lI7zv7ypFsFNYZ/5z8uTbM4GWAlx2SJ2oT2fyS8zt27LAVHdIFGrzoVRWdl2kHKYwPF2L2QVuF2GRsNYq2PPmxmkIx2sSxEm3XeIH3tf1HngNzjo/YjCWzPWNoLsXQUozbmGq4vn+nHgq5NysoU/UgWRNXWjlG1EqL+JOkzZqjm+x5SmFbzcUz80Ne1yRYVW8Mkd+jY3ZP/tQvnCAkL9mkl+TBtC0t/+6XRxOkTk+HuDKQPPAyPQh/LZmgPq9tL2QXSo5rwksPQ71N4eVCYxxXFsG0gjLJ8dbFQXG4h5w6Uyipe7HdtA53/Gk+zM4Q3NHsSo7hZK+o3wkJm2y+PJjKwiyCl/+eb2SLyu7U2yF6QKKVwRo3zIpJLz/RosR17hPWtSa9/u7v/s6Mlp/5mZ8xA8YPcIIMraNXklcTVdVGVCu2yohWNGERRVlP7zlwSVfzZL0qBXgK+UiTTRi1ULALJSSMKbXPlV4/U9WWFddVxEz15etfe6edPn0azzz/IoZGRnDH7bfjA+97H/NZQ6VQpFBR3WugIwOTYTQLpvYjS4gr2CL8dSTlIUWhSUF7Ha9+x34Zh7Vf3S3IUX5AUQ/CU6eAzLU+MHSQSz0sTy02Xii4Cyv+UBidy03XvLBr1TlJ11SS8h+hQrQNLjXpJaVqaclM5J9NejlhUpMwUTBNkCkgr1kjdEuSZGgyvyaMGFZPnmxyU87MjD2ml+L15VOetBxX+xAUUdUMFG8kK000VpMuDZspqmGiScu2S2iuuBUjWnFWsqdgzLPiVVbMK+ucfJmsOqMwE0/ba6hxlimqJ8L0XxYfKmRFC8EjjE8Gc4WD6xgK2muIf7GI8i4BzDzw2hLgv4qh/Pt6DcJuCfJXPw0inPQKEYT4MwjrT4Tkk+5J/us1a+0RpQcgDz74oBk3/vVGrxOCymzWYCovKmO9nOygZjyzP6roU+VXt9eR1ybtKHtcKHdfE9yzFapzb2yKpEtkdMgg1aph6RTtw9bd3W3tqsGq/HndrfOrrb8vChwIufpnuUzYedIv3ettokkvqYqoCV851GW/LqVLKKsjdR3vy+3K7uKa4gGB99Xq54MeGNkfk7EkfHhLx1zcdR3K+owxKg/18lyPUF0K4h3xURCa9JKM0J6Af/VXf2X2o1/pJV4N2kBn1f91hlolTRtDK9D16leJer+EpOxKlqnE8mnFiya9omZ3yH5Rmzs9rEkvs1PIIFrJfi0nvZRfkc7VNjpXG0qub9y40T6KoVeaPvCBD5gO0MS55Ijuy29j+4eYHZCtXCNvRshwiXyCfY+2KG1aPSgv2t65BbNG02WNoWrIxzVycpNezaU478Qx2ZSiaKvQJtbDYcpT+yMYvhbJOb4p9zAx2q3RHN0yPJfMSzsZQTvWJge03261me7kr5hsfsVCnmcf0VF9wMl793YHuZK/gpMzlmqDHnC4Nv3mvQq1i2Szax+H4Ln6vOy+rVu32p6hkue33norVq1aZQ83hKD/q4fz8YSuz8cnwbDkNHqVi0LYpBf/nB3heNR9rVc3XDitm1GZJQU1v0AW5rkmiSnXz/HE1NeR4rwYON+zD8H861y8I7tTK730gET7veko+zM4TrC6rIf11x5XbdJLSszP4n7lK1+xr7bMmzcPX/ziF21vL2vUukIUGjN6uXAx8WqiKsoKjOkT9MUMmS6OQqKdirmAttokEhTOhXgbJqPtKJcKmGNLbmvIauPRaAJxGibxSs7KXqmvrLla8OXTUQieq/6PHj2Kv/vmN3Gqtw8fpJHxhV/6RVSKVFDaPDShZaNiBP4xjFRQPJlAme3CWB2HkKQ2YvV2FawTKw0GjtmkX9VtiB9z9Sx/CqrN8XlXZ6xjlycGsgiYS7q6J+fujlxceF279Pk7lS6HI4qPZPHzXpRxurKqHDSYbACRq/tvYXsk6Ic8VtMnj/XpY01IUQDTuFSYWESr+PTkSGm3oFRVGRSnwkfpQ0aYBLYrUySuAZ4mxRSP3FjHEU16xVl+V+aIHsNGWb96Qhun8Ur3dK0NiVoK0TLT4bUw0aanm3l0UIgl6FZgOXNJGb1xKn3GQbcUy6PXJaUUrPxUCHqyVigU0UYjQfftJYiIOJRBmFEJgng1x2Lo9cYEcpUkw0XRxvyojco81+uoqjeR+MWI4a1VmLSrU16rkDrqR051dw+bJA0RgvC84uF5SPDnfk8vLWXX5JdedddSdhk3nh8F8fmFEIz/3cIbZY1xnlUm9h3dp8Qj6WEH+2LSDbgT5TEkOBiIsu9q9WeFfToj2cN4k6A+oV6RzItFkoyD/a+hrhrr7lrC14X0t+kzlltt9dZbb1nb6QnbT//0T09Neinvwbrz4WcdlCXpHVZ1cNKr7swf6SnBtWmcAzY5VyuS+foojMpaRYm6MxrTSnVnv6i84lcN3C10gHd93ciPYDqEbsE6M0OMsrpCeS93hZd7tezilv7x8PXqhnEOOrP4SHpIdz3D15V4LlhPvl40af77v//7toLdyw7ZOPKj+8H6na3wbRiEz2+l7J5s68FbRfZKfYI1Sp2NSE4KHtEq+bK+VYI4QQysfZNs0otH8bYG/O7r0FcPvq08/LV307UmLp955hnbtFp7eukrsB//+Mft9Ubd931npjoKcWURbKdzwd5o4W1NV40Vq2htaUGsMG5mf443CqQE+bJd6o7xjTVzHMgw6XISySL1Iu3rWFOUsjKHpJKhn3IlQbs8hQjHIsVawcYkVepP/cVjtM8jWbOHE3Ariyva5oMJajKgWpfn0UTZ9JWf6NKfiqOxh8JozHAWeGmllR6wf/7YuUJe3X4TwulF7eklu1DyXJuVazWP5IXXB9aOdT16dSAOEQmef6YYp0511PlLizBcP/LhBJ4rmHSzTsm3olKJfYHl0Zi2xvIrmGS96iKRTqJIu6NSKyIW18RPDGX2tziPSsml4aD+qjBe913dOroy8DJIR/VrTXppDkkPuT7xiU9Mvd6osop8fZxLdl211xtlBEqBK1N6tfHJJ5/ETTfdhH//7/+97TUlPyKf0eD51UZRj8oksCNlxClU2b2Qq6WNkZqiWZnBKHDAUog20U8NqULGjNRaukVWLg2Rsr3HHolRsF9lY0NQHSuvvg593UqA6HOff/LlP8eRY8fw6U9+Er/167+BBI2oWolKIq68st3oV+FLVGdqsyKFjDGU5xLe1+SWICaMyjCvN5V0hZShoNcFK7yvOGKsC3VmTfpI/VSZllNGTIvGGxNkp68b6SYIGKHSULyMvCp/Stcbs2oVtpFi0bXALFr+dCnS5E60/u5ziYqWxZBvCgumxaJU+Gd1VaahzDbXhpgxvx9ArNUOZRqbyktUeaEfZsHiVvaiMRmVmhqs2ADDBiRlvQbJuHSf5DaXZcK2Cqs+ECqnES3JWOWF6pP+ci16qZaDqSLrk04lRpBjfLFo0hmtdIzTSNA9VbLqUk9Hq8lWK0tcE7TkOz1J0xckYzIW6FULDmJlGpHVEo3gBMoxPREDmpU446AoVbFYD+Rb1oVvEy94LTnmJdgX7ax+LwiGqJ+FCHFuiL8EfbFr3759tqeLNqfUVwC1YalWbqhPT/dr4/qrBs/rPp8ecvdu9nVb+eNljUa5xFoxyb5Gp4Red9c+JnSL2MrKGPJJ9/CD5gv7qeSAehrdKBqq6sAXQGNerjSUXrDfy9CU7JW8lw6RQaq2mzNnjn11Uw+wdN/n04dX213tvF8sJFeFsya9zEnaxd1jixofxuq6xuSi9IZWRUt2Sibbq2ZnG1siXTeW3ddH46SY3HSvrFW59Xr0QcVrsfpejA3RmT85Kjf+2gYFPI8n3GupjfB5m+1QHlUnKo+OyndQJmgj+3/1r/6VrTYUD2qVUPDLr/Irf7MRKouHyhm89pDNUSiwvFHaBBzsxKLaPoEmhl4Fi+TNFohRokQlR2Rn1ptUD/816aW9wKYmvaTkrzI8j6lsnueCbmqb733ve/bWh3TBP/2n/xQ///M/b/fUdn6yc7a24Q0Pyj6TlPEEbU7XRvFyzviySHlVVJ9lc7fIBKdMy8TKKJMvU9UY0hXJJvKqbH7ax3oo6zhUY4k47W69OcMrzfny6Lo9bVy9VUOdGau2W5+wN1LMxuY586AxQrmSNZ6RzIxxzCL+d2+vODlJr9ZXfI8wmW+OzoKlTzkT9FvXESGuPIKyQYti9PVGTXTpgcYHP/hBG0fKj+SC93f14DjDwRjGnQaPvK2VuSqGK4vTVcqmz6sO4q8KZbjZFTGO1TR55W4wSD0NGzy607IeqJHHozHpCTcO1qAtXh9TKy3F5etP9oO3K8q014RgXenc+71e4POvMa/szz/+4z+2LzaKL/xKL/V5kS9bsMxB+Emvy65VlGAwUWVG175xxMD+qVwjfNhrQUJcs6l2yh8yTyQWRVOihpaUMzw0RShDVBMRDMVBSxPizW3kwxgKJRq0FZaVzOwnb64leaieJSyMykUjrVLS6ihBxnutTCO+XGUn0/5PrIOEvpqi8jMuljVGhWWLkmmYRyscvGlFG9tQdVRjxy3TkxSVBoEaIqiukilt6kxmLTFNdXL6sQ7J+GWcSVnpOkEDXUa6yL1KInUqReX8qA30tF1NYuVS3QbZViNMepZQiFE4xNleel1QY4uyvgbDoHG2H4tERap7LCPzo0ki/bNgPNKz9gCLZlkGKl2mrX3a9FpgiX7LWqHBOOOMX1ks09AslnlPmwnSH0vGDsVBS6TIsjslLmVb0mSZao7Ci1zDNHhHW8TVqcb8lKvj1OU51FhPKKosjDOeolHAsMyf1RWVPrSRrSbiGDCZaIEe8paVFw6ytXLNykHGzBULln5CfY3VFNcEoKqLjlYuXivuGPthUpOSPNfrpVrJIFJqanO1vapZNeU4RXXHX+WnTh6NvBdSSI3k+cRDSlkrNjTo8RMBHvLn9cbVJp9+o5tgOov9ulpkXylqDysa7RSDtsuOum4kzY7Xyr7dggoHBOUE5RvvRSRj9Uqz9oeMSD9Id9TjuwAa83Klyde7oPx5N0E6RKsx1G4iPzgNIhjHrCQJwgY3E+o6ejeVg9KO5oDJRukYrRSOc5Am/Rep6iEJJSObT5Jdq5AlNPUMx1pUcdFd+s8/tPHuOpdOc2GYitLgue0zSdIT3zjz43ShjNoKdU0J+UKBurTkdBf9CTpWlD/5N12aNNtqqlwB+Gt/73qimSC5IZIxLIjnxK+eZ4XGeGYD+TyKhMZrg+yIuL7YWEGCTKYV92MMm6VMScbYxpQh+lBSkTKEZgj9O9Kp5A0tN6pu/c2ch6tJQvDcQ7JDe3iJdO6hdnQPS92AMKTZR1HarXqoXC1nUMjRvi+Sf2O09+NJ2pM1WqgF6kPZ0rRZNWincWp742o/LrJBJFqhXTpBytPWpfVK3pfsFCRz0xSNNZq8kr1x+eV4Ihptpd9WRLU0TP+Ut7K7tZ1MvDKGRGWctn8z85WmfZ5AnixVZLxVyVHKW62U0Vse9sRZE251ctuQKD4Ry2e9Zhbrr+uUhAu5a45A8lyrP2VnyEaUbJB9qKNkg7dFLoRgGleO6nxCHuOBJN3jSbxFHtPCB44Na3o9nbo8wTFlyvpJhHq9jDz7jsZlZd4vV1hmjZc188v4tEeePkLG3sE/feSDtgdN5VphesWb9L1eGfdzKqozN6nmJsCC+b169XJ5SPB60buJDzxfqJyXgovjoHcBNYwyq8wrk37yS5C7v+/JM3aj+5UmpccTY2AxHDOKqhhQAzLluUgprIkJzb6Sj8ukeikUjAymSRxXTjHuTGlcabLc8BisPw+rc9eXpIemwJD8oV91EhpVtnqLyoalrM8my8h2R9WDFd4YTnXglJXS0RLNaNw9qS6w/CKd+5VE/LHUFLPcRZYXUpWVqbSUXb+KSzB+qbjJOAdXTg0UVIQpfqofp57qsDw2wWZ+mE8KEVuRx3zbwMLuSciqE9XbUe1O4m2D2ldhLa/8m+IP3hPZajI6TQ1oVP6Y24vClYN5ICmEzehbqDrqkTCbSFChs+Z5zjxp0rHAAU6pCv5bvEUOrt0+MWwRKoT8xCSymRKGhvMYn2CZ9TqnTQoqwogJPwVUvm0ZiuqHp2WeyotQZqErmujkfb3q6AZSqn9Xv/Km8KpTXQv1Uk7B++XP1HlIIZ2LvDzyR+PPOh9Z3yKsr5GC/q42Kd0geXefP+bYZGSE/UyvG+mWnCVf1Esc6EfGSr2Mclb/MlnBc3MNxBuET+9aUmO5heC5b6eZ6sofBR/HbCO/Wm+amH9/rj/pQ+bf3OzPl1/E1rNzdyXZ7F5xlN4voyRdpnvUJc4377Ht/cSuHhbZ6i0XhdWjve7Dgb7Pg6Bfnz/pKxm2U0as4q676yjeEzk9MR3OU2PbzHaaKb9B+HLrviZIdPQ86d2DYWcLnQ/B+3pQaGEoX1goZ4fR3XhCHupl1X4wRq7Z6x5Y7qmB+7Wpg2D9B9vBuyvvlt26m29PP7j190KaXeSh/Yw1HhB/yt6MJ5wMKtA+1QS92tdsXq1yZnsWXZNC+xjp+WyV9ng2q/23OIBlmytue3VXt+WX/pSaJvw1qU8ON9lW0sMmqlltFabns3pAbYMB2e3koTzvlyiLlVUbj5D/BdtyhXC8OM1bTt7W+dSI53XZGtLlpaAcOBeJb+TPeIpyXdea4NAx6E9+LkRB/++axBOeptzFR9MkkSZ3G7/Wx7y6FjNLRk+NEzXWop2gMZj8qO+QxRm3xt+a7CfPMhyLzXMFUJeRTaE+RVmZYNxxlpG8GpwQFCRHfZ3JTefCdJ4dXfb6uYLkoXPftlZv9QcjlwInFS4jVNFBCmZc8BMVQQQLGfTf6H6p5HEu9ylQyGrvJDuFXhNjBaOA6sQgjhw/hbd2H8Zbb+3AoZ1vYfRMLwpk0DHNvJK3kqxJs1EieqKvZTfnRmM+LgedC/6ejlIytaqECOtfJPdonCRhz8yzw6qblNlJrZtZULYha8JmraOsm0oBpfFh9PcPY2h0AplCCUUG0oJny4vFRYVn8WmWuj7JoskbdtDylCJzcU9B/CLhQN6wSRgqUddpyeyKV2f1YupA31PnBvqtVvUkvMA7UrxsB1tpRTArlv+aXj3Sa6sqIxU1T1QLmoWvFEYwMXgSe/fuw+Ytu3GydwTZAuvKZu1VGxQk5TyFDMtfFg8rbabByFUmxa1p+KpW01H526QS49fkme3hY3lhTTIvpsbNcNCqLE1q5W1SdeJ0P47uOYh9R04gx+i07krLwGvQKrBJZIYHcGDnAfz4qedw6NgZ5LU6i22mJbAsAUps36Lal0LPPjKgTOYLyAyN4tCR0yzTEEbYXrYZLitu6uubdlR/VW2orlyde+GoSnbLyO2mIznyaG0eUkgXIM9XItevJR6cAhOCbsFwV5NmQqN7RTJKbtpvJzJJI3sItdHjKA0exsh4DoO5CMbLEWTpJUuZEy0OIzLZh4mRPMYm6F6SRtH3qmav4SE0HoNo9Ouha99+vj2DfmcD8YekjE3nzcO0hX8iJJlo9+UmuSi7QHKeRBlbzmcxNDiEY8dOYP/+Q9i37wB1x34c2H8QfZTjuVwBuXwRg4PDOHr0GE6cPGkrtQRNgtmTSh5d+pS9utaEmWS2siB5TF5TPWqrAFuRrbD8nTKglT/1Hx7lz/2djWD5BF/m2UpBNMoCDysrKQh/7WVKMNzVpnNhJr8zUS2SZ7vSTsmOI3umHwOnhnBivIxBDfT12mM1ZvZWibyp18b0OqM4g5VAspSm/2aI/2rSTPDuajP/YG2mMI3uIV09akSwvxXJd9JvpUoRiYGDmNy7CTu2bsL2bQdweN8ohs9ofUAKk7EkMrEaUtFhNKMf5bEDOHPwNezb9jK27cngxJkURrIp5PX1cy1hwTgqpQGM9B3CwZ0bsfPNN3Bg1z70nhzD2HgUxUqMtmsVJW1dEtfbDxmK5CxQyKMyOopB6tjB0TxyHJBUaKxOfYGe4xE7KvPMt73WflYRZYNQZuiP4eyvoT5CuvwkzHTur8VzOtfkhmS6R9DfVaHgH7M27R5kI9c/3H3lWzwmbU17gUdb+cXxWnEyg4HTp7Fn1y5sfHMj3tq+E8dP9bqVbZUSRsdHaSucwoGDRzDJQaC2nbJ9HWta0az5CSZAPUBrge6Un0xB9oAdlQeOBx25sbe8SzvoKFIGLac6uszyf3ZSEN7Nzx+Z/SRb6RIwzUmXCY2Z9cLSZ7rx/tXAxaap5bR+IkDviWtvrmglT6PjKLa+tRMvrt+I5597Aa889wy2b3kT/WNZ5DSzIehJq0gdQy+kzwL4ck8djabEv0Gz1+ZKJ+s8VnbnS7PJ7mlIvRPT8M6Pj+H4wf3YvoOd9WQvJrM5dWvrgJWyOjfrTUanJr54bh1N8HzAP96wc4+pK6VNf9NkTv6WkQ+qg+cnK5/F74SLJm80yaSVXNYevK3N7d0G95pU0xJJiQiVS3FxEFOYwEDvMWzatAnPPf8KDhw6jvFJfemQ97UpvZuC4gXPGUb1ZBtoauLLOp9qQVYpj8zLWXVc09NN5YVhlFWSlUavy5grw+Wy6KOg2/jaG1i/8U2MUDgWNCunutS+XIUMxs70Ydub2/D4d76Pk300IpgWh952VGoiCUNNqOmpWoSZrORyGOo9jW1v7cauPQdxZngUBdWtssB8m7pXHSrHdHcrUlSH9OH98XeqTXTpKm2aQoR4F/DKa6ovE8Z/sxFT/M6eFsnRUJnAxJmjOLrrTezZdwTHz0xiLG8vJGvqHZHcCMb6juLQgWM4foLnE2VbxWkTZw3wZb+W8P1cCOansT2C7TSTf2E2lKcRytK5OMvcrSx1ol+VwMlyNhrloh3LRUyMDuPQwUPYsmUb3ti4EW+84Wjz5q04evQ4JiYyyOcK6Os7gx3UlYcPH7FXueqp1OEmCZWIPmwyNeGlH1PEJN2zOjbvBjP6SNLXqmM9XXY6V/3H+fdobLfZjovlGdWB5z1fRj/ZdanG8NXAucoXLEs0pgdiRUwODeDk/oPYs3Mf9h0fwLCxD/nFbImIbX1gH6ORTWKMQ+K/Xc5iqA5EwbYT5ObbMMTshbZAyZEDxyZHMbhvGw688SJeeu5ZPPvMS3jt5bewb+cZjAzXkIvEkCUvR6pDwGQvho7twI6Nz+Clp7+H517egze3ncLx3hzGMjV7cFyt6i2Gfhze9xY2vvICXn72Gbz64ivYumUfTp6aQLEShz6EVYoXqD8L5J0cZXEehYkJnD50CDt37ceevYcxODSOfFFvMKhvkJc4DrFxAPNOjqv/BjuJ7pDMnnf+Qlx5NPZzLxOCExqSB34laFBWXDu8nTuMe/gzXRzJNeknlYF5tkkvsWoBQ2f6sX/PXry+fj2efvppPPfCS9i9dy9GOa7OFXLk3SHsO3CA47XtGBodNz0vyAZxCxl4wSGmVj661WdujC1/5pcJ6U0EZUrujdzurh0J/jgb4dtbbR/klUa98U5x2Se9BJ/BYOZ8xkXBWVuhsUBXCj4/wXwJ/lq5sL2umB+t4BHPFkcGcfTQPhw4dAQHj57AQQnXt7ZQGD+PLdsPI0vhaiuUKloJpBlZF94jmJ7oSuFi4tZ7xPZa3nT2FNAdRCyvjlqeKdGvDezl1XW2Kkr5LAZPncD6V1/BM888i7e2b8fA0KBbgkp/6nTmleeGentbfdQnw7TBpC0jtjque2OGlH8JOm/MKmFfjbL/PaZP67zE8vi47FqFU1yae6r/aSpSn0fWSjflTmmU1Fa6dFnjdRHDw4PYv28ftm17CydP9iKbrU96WZQqVQ2xeMzqUZeUzQZLn+2vVXTa6Dhmy09dPlQErXRTRIrLVpcpTa3MlBdNUNFvpFTCQO9p7Ni+g/W6A6Nj4yiUNahh5uinTIE4MTaG0/396KNgtC/EKV3e0+SWPk2uubkE205Wb0Urvkjaw22CRsGp3l6c7utDdjLL6M4eMHjij5HO/eSXcu3v2wqDOgn69echQlwMPP9M8RCPMw1SrwVfNeYtCPXxKXnD/i+ZovWVVeTRf+Iw1r/4NJ5//jXqhCPoHcwixy4vQ7uWG8dJ6o/Nm7bSID+OkdG89SN1/sb0Gq+vNXyZPRrzd768BsPNRijXlv+pq7Phsu/dzXedKMNLRfSf6eMga5fpil07d2M/DdVDhw7j+PHjGBwcRC6XN+PdZO/JU7b5uvjcXjtgHJLrbt8ugg5vr6963daTtfs6r8MeUFHuu/oXX7KtLD4XT2O7NLbj9YBz5VP2o+4FSeXzZZyyIa4BzpVuMK+N140kG3RicgSHDh7Apg0b8Oqrr2Lrjl0cBHGgL71voxmVVXa02r1+6pllCtemDi4ElTHYXr7cXg8E74W4+lBbBOGvfTtpnWGtMEYZeAKb9pzG5v0DOH7kAA7u3oStm17GxtfXUybux2ShYA9+CgMj6NuxFzveOoQ39g9ix5EBnNy3Hm+8+B28uWUzjpzow9hkHvl8EUNnBnF47yGcOHIMx47sx/a3xP8vYcOmbejtH4V2tS0wO2Xyv3JSLmQx3HsAW5ju0888j1dfe5227gDyBaUsOal8y+4mbxlPTfOVK1XIZ7MJXg7oKDkflPXXHufOg5NXuq+8yjZ0f7yw+ywVBmgz7DWbYZt9DEgfcTp0iLx+/ASGR0bIs3lk8zkMcXx3+vRpTE66V4Btmxwffz0LXlaqfmxxCd1tfFavu+mxmnlz5zra3+xHsL1dORypHjxfXCouPeQF4BVXMPPezZ8Hjx6N15cLPu3zkTandStv9DJbFLlSBaPH92H05EHbsH7xmjuw7uZbMb81jkO7tuLxn7yMw2fyKJRKSES04WKE6iBq+5ErvnOleyXQGG/wejptnkv4k9xRjOT9kBnMcGYHYhnq00P8o4KrlIASldL4KA7t3YWnn/o+vvfEk3j+xZexe99BDI9NmA2WTOpVSU1+6cmNJl60MWEJGXbeidER5CYmUay4vb6YkqrZOq8NH1mHk5lJGyT4DWo1mSg7Ps58TYFhfAcQrJy6rur95gJy2QmMT45RYLhBh1RjpVZCqZhFMTuOPKlAhZjJFJDJlVAsaYa8zChyKJfd5ri6lyvQXWkxd9rIPpufxOjYECbGR5hHKWh9HllhmT7zUClmUNHXPPWKJesrm81xgJvBOP0W6VcTiMqNXgXVklV9P7FQzjKvQ/Q7ahvma6+DSrFiK7zsS6JxvTqpVWgZZEepyPMZzFm2Ap/6+c9h7dpb7AsnqVgCCfqtaUNYCs0oebbAehifHGU5J23jz+aeDvQsWIiuefPQ2d6FdCQObb+vOizkchgfHcWYhC7P1R6ahLM9GeqCRTXtaltHd+bdzPYOEeIC8PJoWhadfR3ETG5XAz7dc+VHJH6XXCjXiijV2McqfRg5tBlv/Oh/4dvfexrffXozXt91CqcyFWRosESzZzB4YDM2v7ETu/cMYWSC4WNxDgbOjcb0ryZ8OT38uTOuzq4fk+MNbh6N17MJypoj5ZF5ly6yM++ucvFCOkYk1M+1qqZUyOHM6VPYv2+/PRwpFstoa+1ET89cdHfPQTrdxPrSwwftsZhEW3s7urq6eR6njsvYqwz2uiJ1sF5p0Ff55Ff7h+rhmZ67KTeSxdrUd5S6U+GkHxVWWfEfd9F+lzYBRjc/wAu2yUztMJPbbML58qd7fh8vnQcN4LNsgmsEpd1Ije7+WvC2zNlUwMGDu/Hai8/ime//AE//8Fm88MYW7D81gJp2PdbWGwzvbDTGoV9jmjoD8KjYmRp/rz2C5RZUxpncynp4OlUHri1DXH34tjkXpTCO1ORBjB0/iJd65+NY8kHce9sy3Ls6inThCLa9+hSeePxvcHhAbyM0obj1JLZ+42k8/fIp7E4/innv/1V8ePUIjr36x/jBT/4WL21Zj6NnTlPOZTB4chiloQJuWbwSd62Zj6ZkP7a89Sz+1/cex/MbtmJCH5GKtLELtCESa0dm6BSObP0eNr7yTfzgqefwyqtvordvmLxEa5vsJZmovYd1rXGN8u96hv4kN+pD4JDdrglce5x91Mqu4F6NfuWX7nl/1wYNaTtWmnKWPvd6XQylhxd6u0hjwhLHz9u3bcULzz6Lfbt2ob2tDffd/yBuWr0GcY7jsnmOT0tFpJvS6OrpQWd3DxKpNO0NfZlU8Wq8qW1zyhyKF80WyNI2cFsmkHmZB42hxycnzVYoa289ZWoqj1MnJMfus5nlPR943S4ekH4QH7xb/aBtqP5AJ//HH9jhXcNnyjOozn3GNcO5f/9+GoBdePTRR23QLjT699D1lYZPz/LAbIpZSlqYE4kjqffRs/1W+Qtvez9uv+ch3L56GbqSNRw8cgyvHRzGTStvwoouGrZNCdZmguZHFLJH9TUmH28jrlS5fLxK05NNYrD+R0dH8caG1zE2Noq1a9fg/vseYIAYbSXmz4fTTz1rMqTcjlVSC6wbduaJ4WFsf/NNfP3r30I20YHmzk7MnU9Df04P2ltb0RKNMz1gaHzEvu41Nj6K3t5TOMDBwf7de+0JeCUZs46d0kbQTFub/2Ynx3Hk6FFs377DXps8cPAg+vr7USgUkUim0NycdgY9f/w+Jzabbrzmnp6XikWcOHEUm7duwptbtmLX9sMolqtItTSxXasYH+nHsUP77an8+k3kwwNHWSfaTytFxVpCMjKMydFJHDxWRK4Sw6q1t2DFikVobgLGFPboMWzdvBU7tu/GsZN6TUlfWEqgvb3JJksnR/utjgvZEvrPDGLfgUPYvmcv83QCXR3t7pPq7G2qY/1qT5ijRw9hw6ZXsHfvXsT6J9F38BSOjY4junQx7r7rLszpbsGZvuMY3vcWtr/+KtZvfAu9wxXMXboc85Ys5QArgXQ5i/zYsL1OU6hGcOLkCbxF4XqK6caqRbSyriuxNAZy+oJlAisWL2R5qVAoiEeHBq0/vsk23cIwWgkmISqFo42T4yyfYwhVvk7dCjbrq3VGmT4LEYJswr7ZKN/kFjxqQruf/VtPurQC5o477sDixYtNznp4g+dCuBo6IoiK3ilimtFYAZXaOHLZUZymPHnxxZ3Y1d+EsVICTW1JzFvcis45UcwfOEa5uwHPbxtFsn0Rbr39Jixa0mLdKU2yvhQow9Uuz7mgupfu8PpDx2HK/1OnTpkcb25utnZro/HmXz8Q+TabLeW4GFCb1M907n6Ue5Ns9dXBVDbuSEM2R722Y/t27Np7HMlUC+66+2584AMfwF133YnVq1dj4aKFlM2dJiu14ks6as6cOTZRdfToEZvI0opBZxe5DWrPnDxp9av6S1D2qv70AGj37t145ZVXsIe6ZGh4yAw/TZ41NVHvRKmhmVfF46tbZfE139gWs71NfH51DPKSECyL5Me3v/1tq4O7qCeXLl1qPCg7IDghdq0RzL/HxbTFePYUXnrpZWx6/jX0Hj6NUnMXUjffgXVr1+HhrjTLF0GBtqn2N5ItQavLVnnbEnK2fk1PCuvxO8v76iLYVoKuPXnI5tmyZYu15UMPPYTbbrvN3IM6YDa04Y2OYLv5Y6Q8Sttygn2tHdGWu3DzzTfjMx9YgsUL59Duj9GWH8DpUY6NHrobrV2dOPbk9/Dqs0+jN9aBVR/8OH7qkw/ggQVuPLh3OIJ4UxuWzOvCgs5mNHFM0tPShQcffADr7liBSDqGvYeHsWv/IGKpJB754PsoO4EmieJMFod3rMcbrzxJm/w0TlZWmuy7/bZbsXDhArRw3EBTFwk9zNfgTo+d1TWsFDrq7Bw9JGS9K45GvtJR+k52oWS4dOny5cttLDI7ZLrSnzkP3lbSG0XyYnxGku4vFLRIIo8ffe8H2LltBxZy7Pazv/A5fOhjH0NHZw/mz5uHRew7LRyrlkt60EUdz3HvwiVLkEqnUK5OYnJiGGMDoxg7NW5vI23auQUjHG+qzkQae0qmaiw3MjKCNMOlUum6PBX/u3w6np+Grs52mR3w5RLU7jrXWGEDbWmNpcUXCxcuNDtU94O8cS4++Y9/+Id2vOyTXoJPVEdvNOt869atNsju6ekxIzGdltnvoPvBcP78SuPsNDWrqosqInGt9aogkWpH58JVWLBwEbpbk0gW+5Ad3oWhwV70RR/EI498Ap1LmxFrTtqX+NIsb0RfekzQHNHTN0ZvSRgFyngFWO3sskwbjap/dYQN2itqNIM1q9bifhrqykImVkGF9/Xuu8R/FCXSOKrlSXJHGzscjfPJU4id3kUD7BieONmOfNdK/PRDi7BmfjN6+2LIFObippuWoLl1CIncSWS2b8Cu576PF97cg+f3nHab9W16Cls2PI9tmTWYTCxGV2ICPTiO4kgv9r2+C0998zt4ZscmbNq9DUf27Ubv3t04eqwXwz33oXlJK5qiJcQjehKobEftNT42E+IUMtnxndi66Ud4/vmX8Nwru/HylkPY2tePvnwBK1vjaC/lcGLHbmx4/mXs2rwRR3a+gmM7X8WmMxH0FuLoaKpgSTqP0ZEcNm8dwng+g2W3LcPc5d2ITA7g5Bsv4eUf/Rib3srj6KEhHNv9Iwyfeh1DtSIGe5ZTabPtX38ez33zG3juyBm8dvgkdmxdj8OvPIH9W9bjrdL9GCj1INk5gdbkMFJDJzC+eROef+xb+NNX9uLoUAkTe3bhGOvtwMgYxhbeibseeBR3Yy+OvbUez795BG8czWBw+AyiZ15B7tQbODgyF20tC5BuHsfQ6AHseWsTtr34It58bj2e2JnE4cE0+fUkuttOYHh8Elu3RzA2lMcdKyocbOdw6sgRvPbyy/jR00/hJaax89Au7KeBffTkKFu/B9HOeUi3xWhMZ8kUVeMP1XuU/BDjwN8mS9kmetGLjGJ8FiKEl0FBBOWS4Ce9jh7VxPMobr/9diyRgq8/BPHy62LoasGnVdW+gNofsDaOVHkQyXwE2zcM4siJQTx070KsWpZFrtCPoUwKt6y9Gx2REWzcw/55phndS27j4G4lli9IoiVghGsiRX+aWJHM9mmZrLuKZQxiOg/uoZWf9NLrewMDA2Zs3HnnnTbpFcyjzq9Vni8WTiuynqtaVVVFxVbhao2304D2W5pgYcooRJMoRBIokSrRFENF0TT6JvIH3sSR/jhi3SuwlPy77PZbaSd0YUmE+qaphGRsGKXyaRw+eQxv7upFNNmE+bUJbHjhWby47Th6Mwl0tANzE9Sru5/HXz43hsFiGl0dMaTLExjW5vjPvYpXvvs9PLdvE/Ye3InDB/fjTG8/sgX2k/aVSLRH0QLq6UoWZZahrEkw5j1WbzO1neenYHvO1vYJ5jN4FCnf/lry44knnjD7UbJDk1764pfu+XL78FcLyt0UX2kNVk0vYmltt0gQf2n3UMq/MsvEgbj2HY3SX6xaoF7N8jyDaHYIP1n/FvbsP2F2WfP8DvTMb8Padva3+T1oumklKukYShrIM61krYQmfcreVgtKftJqJQO7FdjOprva8HXfeFS7+AlyDW41HlBbPvDAAzbpFWw3Hf15iKsHyXnjYdNJWh2l2SVyrj5iFdEDAPEzxzvxRUh1LkXHsi7MX9KE9o7DaI4MAqMcD5xkyMkJ3Pexm1HLDOKF7duxt1BC520fwD3v/xBuuSmBBTiJ5tIkxxf0P1lCW88qLF73ENqWLMbiVTchTTmYai+jmh3ByJFh5PuLWLZ4Lu7/5AfI4hF0Zvai/8gb2LRxE23WAm697SO4Z/V81LLDSN/5KTSt5BijvYquWg7RivYAo91K+aj+pj4pWV+WTGeJxGVu3aQnwvRziCuNoFzXueTC4cOH7eHFmjVrsGLFCjsP+ru6YHomTElTabu8CJL2gvaJ1l5a9gV/c1MfIpfx1L5CSh48umUjsn3HEOmai7E1H0S5axFuWtiNlZ1z0J3qQzq3F+ODJ/Fa7yR2HD6A5TfPRQF9aD74FiZefQHrX1mPv9vfjy29p9D70mM4umMDjvWVcagX2L9/Lw5u+zbWv/QkNr45iGw1jXj3XERpZEjXtGgeRvnUHAePUdo97vMOxCyUs54f/LnkksYKr732mtme4osFCxa4h3/1ByVef3ge8dceftIr7NkBuM/Os5LJqVYxFPyRZBoxVpxezxs43YsD+/dhy5ubjMlWrVqN+fNTaEm7J7Oa5dUxGk9YhZ9NrhGMAp3mSiLY4OeC+vNUbure1VGTLIPbGC9KXVfC2EAfjh06hNFsAQ+9/4P41Cc/hkUL5mKgnwO+I2cwMaHArK9EDKOD/djwykv43uOPY+eu3Vhz8zr80i9+HosWzsfTP3oGL764Ab0ne1HKjOPk4YN47JvfxFD/AO5/4H78yq9+AZ/81CfQ09WFY8eO4ifPvkADMENDv2jLPF2RNAirl490+NB+GsHfx/btO3HzulvwO//sn+OLv/4btnS0kM+jkM2hrbkFN69Zh4995KP4l7/7O/jZf/QZtHd2YNfefbY3y+TEJMuteGvIZTOMt2ZLTnfv2YUN7Gj5TIbG2cP41V/9Ij720Q+xfiLYtXsXNu3YhVNU2sVsFm++8Qae/MFTOHjkCFbSOP0sy7FyxTK88PJ6PPXjZ3H42BEMDPfj4IG92PDqKziwZw8eefSD+ORnfgpz5s5BNjPJjj2CiUyW7ULjvVzQ3CmWrViJD3/sk/gnX/zf8Zu/9qu4/+7bsX7969ixfZdtfDg8MoR9+/bgpeefxybm4Y67H8AHPvx+3HbHzWjraKaffqubkeEx5JjGQP8ZbNjwuq1AET/+7D/+Wfyb//u/wX00PvftP4AXXnwF23cdxhjHU7qvKnf7sJE8kxiC5yFCXDouRlZdS3jZLf63r9FSV9jHOig8i6UaeubMxd133oo7b12DRBzYw7599Ogp5IslJNNNiCdTFl7yJaa+LQHmBa8dr45OeCc4V5uoHI2Yye16gXLuyYHllhL0LnU9Y37YfhFNVGj6gm2oFc39A4M4fqoPR08MYPTYMS0NRqSo19oz6OvrpQ7Zi+MnT6G7qxOd7W3oO0P5+8YmbKas7j96EHt3b8emzduQSDWTUjh48CC++9hj+ObX/x4p6uHf/Ke/gc/9wucwZ04PdcdBvPzKq9iwcbM+zGv5krGthxKyXqbL8N6CePFCMmK2yxCDWIvywUxNsZXc1HdI2kaikstSt2+AXo+9+ZZbsfymFUilE0hyAEWr0rYrKNMmUHCPOme6CxfjdcMH10Wb3UBwCxR0Rn6UirIHMe5hjOMqERkwEudgM4GW5hjSKcqgap625ZjZsGLu1qZmdHe2Izs5gXHydDSVRltnJ1paW41FqQExp6cb3R1tvNQ2KGX+Mp6Ee2NGirXKuEqUr5VyCelkgmOCDkuLQwyMDA1gz64dGB4ewuIly3HTqrWY093OtIsWRy0ed+OFasWyqzGXJh98XxPOkpdTfBjy47XC+WTBbLcvXL9h/uvZFL8Zq/FcK7xTqSRWLF9ufLxx4xv4ytf+Fs+9+BomJtkTKrQjta1BIYvM6BAOHT2CvQf2YzI7iQQHgJnxMezcsgUvPPsc9h46iAVLluBTn/g45rH/vEJb4LFvf4c2wyGsW7sKn/3sJ1EslGy8d+jwEYxx3Fo0W1P9Wbny8HU9u+v1neJi9InN7YRwiNS0yqlsbJBHnJSkZGzG6EAOe7e/hI3rHyOTPYtXN57A/iM1LFnWifauCNoSVaS0ZWOtgmKNRokGNYrPYvWYDcylPHhS7qKI1tjh7EzPuvUcEihVmqkwWlAtFZCo6QlkGWPjGZzsH2TnruHhRx7EulvWYuGSBWiOV1EZH0FmYhJjrK9BdtLyxDiKQ0MYLSSR7VyH7rX34a77luHO1R0Y6Z3A4PEMMoNjyAydxImTx7HpdAL5+fdg5W0fwZ33vw8fvGMxPrq8hNXpQew8cAgHTwyjPHkSE0O70XvqOI6enMCp0xPIDpxAbrgPfacKOHSixPS7MPfm23HfI/fiE3ctxUdWzcUCKtm2pm70LLkFy+75CFY/8FGsvW0B1t2+EPMpiEq9ZzB0moOVahSlpF6FpIBi27djAomJ0+g/fBwH94+xgpahcutqRO5cg8ULmtBZGcTIsUPYv6uXQimClso4qiOMK59GufNmLLn9ftzz/nW4eW0PRkf6OFjZieLgGZRZL/rM/bajx5FNtOOh930Id91zP267dSUWL2xGmgZxNE8jl00RTTRj/sLluPX2dbjjzlVYu24Zlq9kvhd04kj/KE4M08CgQdGUn0BhdBRnhgvINy3AbQ+swS33LMDchUm0JPKoZkdxfIACtdqESimLwcFe7Do2gOO5ZrQuvRt3PfAp3HfvB/CZde1YEzmGTP8xHDk5htMjVUzQuCmxPrR6IEY+0FM/VpUjco4oRIj3MmRweXIOegolKVqkjMygNJmgzOhGy/JV6F53C+bO70JT9jj6tr+MwVF6jC2kXIlSpmZpeBSsx7iPRCgud5g6hrh60IyliJWvNpmWZHLXkYM9uyZ4bfaUhYlAX2guF7PUHcexf8cWvPnqC3jppefxxK6D2DwCjJeLiFUmEZmg0dlXQJmytNreio6VXbilYwTdvS/i4Ks/wvdf6cXLRzlYa25D1+IetMf6kT/zKnYf2YGXRxdhct3P4ZGH78GH7lmLB1d0Y3FsFBO9+7H98GmMaDuPMjMlo7lcRbxSgV5ID3GtYYwSIMHzGvW6OVFzaqm6Vs9oBXslTzkyioHB0+gbmsC8xTfhrpvXYmV3G2LFIiaLcRTieqrNmBg+QVs1TUowfq3drkbSjIc3mIZL9ezHUyFCXDycfhPPaqCsBzXuoxnunvjMvkZeqiCZy6NVX22fLODEkZN443gfdsRaEFt7K5Y0ldGUOYPKBLm0Oh+pWBtogdrkLeJlpNqTaE2lEC1VkS+VQO2IUpTjkCgFKPtFhjb+ka1HcJi269ji5UivWoc51QH0lGhn9/Hecdq/8Tasvm0dFixn/NrKhLZqUypGOzri3j9Qno340zAgdv3EkcH6j47uMkSIc8M6wxTOmvDi0ZGzGbVYQCuRF65eihV3rMbi9hg69ryGoR98B48/swGvHB7EYDGCUjyFTCnGcW0ZmQEq93wekSLty+IkMtkxTJRqyHfehva1D+HBh+7GymXzkc2UMDxaRXPnIiy67Q7c9fD7sLolh47hfTjDMfZ+jiXPaHq3SlukPOZWFcv2ZHb1FVbRjYZw0isAm/jhwF4Mq4F+WSZkNYnJ0QJOHtuBg/texdFjBzFCIV6NLiIrZe2rIBEauPGqXofUgmAzZ1yERPDs2psh6pX1wZY1vfKjSS/9yVhS7uUrSUpB+8fHObBDQa/+jaH3DA3ybBZN6RRKFbrHaoiy7LnRQQz092GiHMUEB3cJGt9zW1uwaOUt6Fl3H1oWLUZLexXL5qXQTCUVrzSjnMljbKjXVioVWlehc+37qbjWoK2nB4vmpnDfihTuX9aMiXwRvQODyI6cwImDm7Fl8ya88eZu7Nx9CH1H96P/xBEMDxURSc5Dx+K16Fy6Ai2dTVjaCty+uBNL5s9He2sPEs1zUWyai8F8DIeP78TQ2AlUxscQn2AbFsv2eeVCNG61kOIxWZpAbfwMJgaHWXZ93bEbhygw3hjoxXD/UaTyg4gX88iNs85KVLXFCXSlalh0051YePMD6Fm+DN3z01iyhIo+HUWhMIFojgOgkVH7jP1pDoZ6lq7BQipzbVy4+paVuPm2FVi6cB7aEp0cMLGF4mm0tnUhkYxiMjuCk71HcezEIYyMDdgrN5PlGmKlIloqBTTFomhqn4eF6+7B4tXtaJsTRTyeR6I6wdYs05hoRiXOSqmWMETDejhfRWLOTVi45j50zFmOWKoZt86N4YElcbSngJHxIvpH85is6YVXxx/qG+IfbR3iVgi61QUhQtwI8JNeWvVIMUcHfbQix77ajFpRr5x1oXPFSqxavQILm8vY/fozOHJihFK10y19j5ah/QVNCuvpW4hrDLWEa1MPyTk/EaalDvYVJHP3P7zSU924Jr1ymBgZRP/JYzh+cC8O7NuFjacHsT8TQbYiC4Jymd6bSmnUOD4rJRNYsHYRHl7bgVXRXpzY8Qa+8+xubO9rwi333IfOBZT7pV6UR3cjX6NuWfZ+RNZ9CK3tNJi7m3HXinm4c0k72hMlnBzKYCTP3Ghjc21BwEFpTKQshriGEJN48mAb1Se8POxxkSa9ZHNRjuQmR3Hs0D68uXkjKtEkOucsRDdtqBZNiNH+GsuWqe+rKNDsYjOTtyqm12W9VSJJ6mQ/3eknvUKEuEyo671pcKSjVf90TlWqtH2LGDrRh907dmPLkZM409qNhfc+gDm0h5vLtKMLHE9UqQM5lkpwnJQSc8bJ+0nbBQb6+niFaRR5XmKfiETGUBwfxvG9x3Bw+2GMlqJo44B+wR23oK06Dgwdw6H9HA+cmmAEzZizcC5iTTFk8rTlSxUU8znoA1ruI1NMa0pvh70ixJWF7ynGdiLjvQhNhhgW3LQED3z4EfzMJz+An1m7EB0cuz725I/x+MubsP/4aWTKFdt/OV5poh2Q4tia14UM+1kZLa1pzF28DHPXPYwe2pdzF87B3Dnt6OmZhyXLb8aqm+/m2HcZuuYvwJqeOBZFJ5EtlHGyEMOo5YHGQjVrCxf0WqMb7d+YixbCSa8A7EsJqhLySJKCOKmBSbRCuRpHa/dCdC1YjVVrbsYD996Ku25djgO79+PUiVEMTmSQkyVCdooxTMwMmoib/a0fTd7apSYQrhWjuUwop5q8sKeCvJh25TUd9BVHXaVslTENsolJnOkbwuFjvTh0cB/Wv/Yy1q9/Ddvf2kbFcxynTp/E0WOHkc+Ns/zsTIkmtHQvwkJ20iWLutHZSVOchlyE7p3pJNr11e1SAWPjE5jIZtDS04mFK5Zj3rw0WhI03Fua0Lp4IZYuX4amWAKTw6MYG8vgxInT2L17H3bu2IXDh45gsK8PA6SJyUl0dHZi0aJF6OJRu7JE4zQYO7vRPreNJVXYw9i4aQuee+EVvL5pK3bvO4zhgSFbih2PsMXKepoFlCkURPoSRi6TQzaXR6FSRr6UwyDLuvett3C0bxDldAfmL1qKlfO60cF6Gi/QCG3jYGblMqxeNhfdHKhog+LWzi60plpYjhTTKGNiYsxeRywUcli8ZLF9gjzG+uhcMA/LVi7HkiXz0dyurzOVUSlm0ac9YTbtwEsvbcWGjTuwc98BHD5xCq00GCIlfaWjinIkhUS6DXPmLMDK5UvR1U6bQqMftkW1qi9qxtGRjqI5pgmrKAZGxlDmvbnzFjIPS5l+BKVakXzeguVLl6K9rRU5DehYr2XVC6OScV5jvUytdjFoAB+8DhHivQn/1E5PvPXkTn3b5GUtgnRzK4o0tvWQpIuD1TWr12DJvA7s3PYG9u/Zj8kMR6oME9cHJOJ6NOLiCjE74LXxtFaut40OngTjAUlDN+ir6OFISyt65s/HkqXLbXPVFQs70dMaQ0IftamlKYiTiPOQLY6TbxKU76ux9qY1mNvRgaH+fmzbth0jo8O4+5470dKSQm4yg+x4jsGaMJeyvGdBM4pad96UxIL5C7F8yXJ0tHdhIpclMSuyOzQJJ6LudvkLcW1xLvvOMZPfpsG1lWRKBUNDg7RPNuLJp36IUpn2xEQWJ44eRf/JE/Z15T7aKqdPn8HgcB5F6mSF04eAZKkpFjd4CTJriBCXDhu7iKds7OJe3XJujsN0HqfdmIhnUBg6ije3HsSW/cMYLSewaOUS3Hr3OiRSUXsDJlWjrqxEaWNGUGC4kgYd4tsCB+LFMpJ0i8oGjepr6LRRMxxv7NiG9dsP4WQujoUr1+KRB+7E7avnAYVxnDm4C1u278SxPqY3mcfA0JB9COvIkSO2uffRw0fRe3qUtrt6hiuD6VvLOMn92K87CxHineDtMjbIXppctQejPE6P9SNon7MYt973KD7xs/8b/tEv/SzufOBmVAYOYN/6H2L7lh04eiqPTLkJyVQT4okUw3O8pS8WxpJItM/DnHlLsHZhN26ayzTS9Ee7c+6cHqxavoS0FB2trRz3xdA2dy7H0B2IsC/FCwUktJYlytyxG2r8py//KremP5TxGwzhpFcA5VjalpBr0qStlEdLKQMkMpi/tgcPfPrX8FNf/D/xa7/9b/Evf+3j+OkPzMOmp1/H9k27cGB4Ar0VPd2tIUlBHqfV4tjKYbawlTOR2OTMXM2WEpWtL+jLP9rQFzS+tNeMPsmf4zitVulDNTuI/tEMDvRXsPf4GLZsfglf/7v/gb/+yl/g8ce/jb37d+L04AkcObYHY0OHUGa9DUS6MJRYilw1hVglZ18LrDX1YCzaijn5EczPDiBVzCLPgeJYoYjhpjhyrW55fmeljGZN2DSz0zel0FGm4pwosvOn0dQ0Dx0d89Da1ol0uhlt8ThSlYoZkdFkygkKK1wU2UIHqEU56Biiwbgezz33bXztq/qs8Qs4k09gvNKCZC2B5ioVN/3VylrlldRsJyqxEqLarJ3u+txxTpNFzTUsiOSxMMq8LFyL2i2P4tZ7H8HP3r4SaxIRDMW6MZGejyh5pr2SRav2FEilkU2m0VJ0VCsWODimkVCaRJ71Ek/FkY/JLJBS1sqAImKRMbqdQiE2huyZI3jt6e/i6197Gj/84VEc7Y2h1NqNTLIVXdUzaC+d5kA7ifHIHGSjcxBNdCEdraCZxW5jFSaS3YxrLvLlGNoLp9FTHUAx0YSRUg2TKhuaECG/R2hw2Cf2K1W0aXBO46OglQbaALTaRINaM2wsN8teZfziZw3c2WPqpPMQId770F5e7quxvKARH6UMqaXaMVGKYIwGSzExB4vmL8C9K5qRyp/APg4GDhwcxIT2JkGBPYUylyIqmZC8Cf6FvejqQTXtJhx8rUtfu2PdTZOabChNJJmb9GPN6UcqT+SrMUR65mD5nXfjI5/5GfzK//6b+Ge/9Vv4F59/GJ+8vRNdHQtRiC6hXG5CPim5O0xF245EZBm6Yq3oZippymF98yaTm0B7Zxwx7deUo0TNSO/EUGgSKVN0jFSQilJfoRUxUK/ECqBKpH6LW1HqNi3z5soT4urD85Atg7bWEPG8PsgQaZBRrRTpVGUb59l0JcqFMobGhvDWrh146dXX0Tswgc079uP1557DntdewpE9e7H5wHFsemsPTp46Y6+C2auslRKjrKBEnZ0nv9a02Th1NxPRv+OHECHeAdzDGPGrm+Ryq5o1gJ+e+LLXHektEs2jln0TE2/9PX70yiD2VD+E7od/Hrd/6gHMXUvhVB1CT6kf8zgOiOZjGK3G0ZdIYkBplItITowhMZZFh+RXqoLxZBFZDvLjJ09i50+ewA+OxzFw6y/g7s/8Kj51/y1Ykc4Dvdswsu1p7D4+gsPZFuw+NYZnX3oJT/7oh9i+azdO9p7Gzq2bcGTvcUyMsn8w35BtyyRpxbNcvFZZ7M/BH63fGtWvQ4R4G4LMoXN37Sa6XP8w/lK/iWh1f9zcNSadrHRjMr0GidV3Yd2n78Kv/JvP4v/3jxfh4eoGHNzbjx/vaMNbp7pRTbSgGtdWN2NoKlcxXmvFqchC5GpdWJnvx016hppoRqSpg/ZEjX4mOI7NkbSAMoqx1lYMN/doKIsFuRy6irrBcVqigmI0yVEm+wD1hm1cYx+nuLFww+vF4BP3UrVMFqbBYAYvBaU2UKBxofPW5ma0NzchRUq0t6OrqwuFQgE5Dmb0xK5Ew0Xvo8M2YnRfm/DEn7Ou9TdboZxJoanosXjClgkPD4+wGipYvmI5Hnz4IXzwQx+0T4W/733vw4c/8mEsXbLUvuiVyWTQnepGW2sbBwc1dngJgTjyWXa6Qp7xxexz7Pragt5x1qdoda7NgMuVMibZmUt6ism0CrksxsZGqWCr6OzsQFt7K9auXYNHHnkE73/0Udx999246aab0NPdbXHoyw6TGW1GH7HXMrWZtKmzsTEMnDqJQ4cPY2x8DGvWrLZ86+uh+vJTR0eHebMn5aQk8xUn6XOvqWSK8STQSiFy8823MMwH8dGPfhQf//gn8OlPfxqf+ORHcP/9NzNvTJM8oq9Jlcsl8kWZR9Yj866vE+kT85qBV3mbWzhsaWu1L5Jo0/qOTg6aWU+qd32i3n+Gtqkpjb4zfRwwH7SyLVq4CI88/IiVX187amJaSi9OXjNjhHmPM696HSfPutSRN1y5+FflYN2+cMV0mpspVHl/cnKCdZ+xupIfvTsxOjKKEutf+WxjPsXOTkgoLgl2O51C4DREiPcsbABg8oGyK+5WekVoQMTSKesDui95qb3uki1prFq1iv31IZw+fRq7du50/YydSTJRsq6g2Q51+vPADKgQ1wa2CkfyzbWBmkrkm0QyOk0d0U5boIPUTHmdos6UGwU/irQN1M7yHotF0dLaYrL6zMAwjp84iQnK3nnz5+Oue+61T3C/+eZmRKgjW1v0pDdpK43HxsaR4zgvyb+I4svnTccW8gX6a6aMZuQ0rkt0r1Fmez0QYvZDD1Y9NKHQSh5YunQJ7Zqb0TOnxybXxQN6oCf7oZl2Z5lGhWyoSkUTDyZ16hQixOWBH6MIXp4YmeBzJB0mlMYnkd+xA1u3bTVb9NOf+hQ+97lP4M67l9peQRHyrdxFsmFHNI4gTyfI7zSw0dfXh1OnTln8nR2dSDc1IU9ZdmbrVpw8edK+3vfZz34Q73v/WnTPiaIYKYHCEu202VevXo0VK1eYLS07W/Z0Pq+lrzWUaHPb9gHKs883/9XPzokpXXwBpRwixAzwY3r1HftaI/lP42gxnmR4kXyv/bA5BKQdwBscpMbmziMfr6F9EEcum0MulzMZrwdrTo+7cWHVdLvCxRh3jTYAHTlW0weR1C9tUppUpE2p8JWy/LtxX70rm03ibRpBzu6W+seNhdBCqkPMmozESTHEyGQ1GpmlTA69J09j8/o3sW3zBuzetQUH9x3A3j0n8ebe41i4qBU97RF0JKLoiiTRHE2RmaNkUq1+mYWo6b1C7dfFPEbVczKIsxPZSq8Ke2O5mUopgVypgEhcM8BlDA+dxsYtx3DwTALrHvgQ/s3/7Z/gD37vX+Bf/3/+BL//H/87fv9f/xp+6oEWlPt34YU3J/DmiQjy46cQKx9DvjQO2/KKdRKpJNBWimE0dwqDuWMoRCronHsTblqyDMsGXsPwG3+HPTs34I3jZ7BhbxYvbpjE89uzaJ07B0uo/OYvWo4ly1bh5pXLcO9Nc3D7mm6k1y1Hzy2rsGBBO5ryAxjfvwHHtj6LA7t3YcfxCfxk+6ANJgZ7jyGV7kLPoocwZ/6dWNMMdJVHMFA8g1O1QYxE8yioTsoUHCNl5AbyGK+1odgxj/47sbIli1LfNhzpz2G0lEbrSA1zztDfcAE7inmcSFRRyJ5BbrIPuXgLxhLNmKyWEa8U0EVBFxmKoNJPI7acRryrFfNWtmHRogL2H3oc2197EUf37sXmN07j1c0F7DtF/6UcqoUMJgZPIxUto6ezDfPnz0EXDYNoNc5BTgW9pRQGaq1U9KOIZnsRKY7Z6q3BAo3kaJxGBw3mUhmpSgypeBrjHEidpuBFPoNVC+bg5s4Ckv0bcXTjD3HwrV04cbAfTx/O4PHjRQyXm7By3jysW9SBntgY0uSTIlgftU7yRBwJlKCvl8VYZ/FQhIR4j8OM/zpJtpeKNE5kX2c6Ucl14EzkBE635ClLk2jJppBCC+asuAkf/dRn0d6Ux+k963Hq+GFb7UXrBPGom/Q3eOtj2goJcYUhY5CmIk8c1YdFRu43RiORFEk441H60UiT/nSPtyMXoeydjGJipIIRPawo9WGScrJWaaK/FqRqk+io9NGWyFBOt2Mc7agN7cW+17+P/7llGE8mPoAFH/wl/N6n1+Hz8yex/ts/wdEt/RiPzUF52c1oa4ljzf4fIP7MV7F/TwEbj2TwxI7DeObYCYxSVd+2aB7aaGbUqHtibQlU0zEUqMi1bijE1cc0j+jCXPivE73OrMELz8k/sjPjMT18ipLLxF9JxBItWLBoFT7+mZ/DP/uX/w/80s//b/j0xz+Chx55P5asXIvWzk7q/y6svmkxli7sRgfbWlsyOHtOPKz0lBQZIkodbytaQnES4p3D6znHVOJZHkjGwzoafw9hcnwTNmx4Av/hL17GXz05ghOUhYlqHu19J9C6ezeqBwawZeQRHF7xz9F1SwWLureg48RjiL36LWQ278LLGxP46rY2PF++Ffm1n8CtC5K4/8xjwBv/A3/03W14ur8HTekcYhwvjB89iMHdhzBwZAx9HR9D4ZF/gc/+9Mfxa//obnzuEw/gI+9/FPfddTfWrl2HjvkLcNetK3HnqjmY18GxDvucyuH/3CpMdy7Llb3IQWU2Un+SnxAhLgZOytqHHvyf+olEsN2K0F6sIjOZRe/uzTj08o9w5OXXcfrNUfRunsD/2t+Dfc0fQ8fCOVg1dwjz0mcQz40DE0MoZro5dutEIsnxYOQgJmuHcZpju0wXo+a4Mp+bQG4ii3wRKMZakUssRrYthaXZPswd2IpMcRInUi0YTJKftWFeHrRLstQ6+lIq7YX6SO5Gg/p9iDrs6YC4VYKPgxPNmurz4f/wD/+AP/uzP8OXv/xl/Lnov/8lHn/iJ1i6dDFuu/1WzO+Zh3QiZbOpWhGlTW6DAyUJ0eC1/q4NlK5PWz3SdViDlAFJT0PiCW2TqtmqIjIT4zh16jQ7VgWrVq9leW9BqjVunx9u79A+WguwhB1WG1IeOnISBw4dQz7PwZ32xuIAsVxlPNqwtViyDStZQyiVizYL3tHZTUW1FresXo7vffub+NM//WP8Kev5z//H/8Q/fPM72LnnAO697z7cc28HmltSSKSa0NSctI3h42wfVW2yvQ3Lli3F8iWL0XviGP72q1/B//VHf4Q/+r/+K7752HfRP9BvT4Oam1vR23sGP/zBj/DEd7+DHzzxBNZvWI/BkaGp9tFRn3tVPegVz55583Hrbbdh3txuPPfMj/ClP/tz/N3Xv4Fv/f0/4G+/8lU8/t3vYue+vdrq357GZrMTLG+VwRmXVm/xqCdbMRqo+axm8Svo7O5inLfg1ltvtn3JvvQnf4K/+drf4NuPPY6NG7dicFArvbTnRwTzF8y3lWz9fX147ZVX8eSTT+Kpp36IHz71IwwMjTCNmK1y41CcrFdhfbOuWS8JJq96tqd2lSrKzENeK/ZGx6DP5666aRVuXrMK+YlRPPm97+DP/tuX8Bf/4y/xt//wLdsvbN78hVi9agk6O2iYmxWvpxZ6YiED3pilzkUB/gkR4j2MKdnNfq0+pM+1U9DTTfvvaV899REOaOknlYihvbPLVvHccvNae7JdyOedbuB9GUYzI+xP1wIz6mPKUdkBWtRgrycY6u0j/UAFUS7ReCzLXtAqP63dkc1AGawnrZSZ9IWKPvRCnZJqasah/Xvwkx/+ADv3H0bPktV4/8c+iQcfuBe3r15pXz9e/8rrlNHjWLXuZlvN25GM4unvP44vfem/48/+/C/w1b/7Jrbt2ovuuXPxvkceQFezcsQ8Mf0q5bRy54ZyIWYfyEPGS+Ip6VHqUDnxXHzW1NaOFRy03/vwI7j33rtx3z23466778RN1NVz2d7z5s3l+Up0daaR1ENEY0n92Ekd4gDxAw9B5xAhLgF+ksvsyCCVChgdOI0d27fhhZc3YOuefXj19Q342le/iv/vH/wB/sPv/T/xX//zH+HpFzYg0TYHd9x1K+3dlQxzCt/71t/jv3/pz/A//vJvKMsO8n43Vq5bjR4O1keO78f2TeuxfuNmbNj6Fr73ve/iv/3pf8W//3/9Pv6Pf///xje+8Q+0t4+guXs+br55He6/9y48+OADuPu++7GO44gVy1faStvFixZj4bx27ZDixnTsDOov7lwFsuIZAqd1hJ0nxKXDy3etvPKrtUq0E7SK69WXXsJf/+Vf4Mtf+hK+8ldfxX/9oz/GX//V3yJfjmLdurW49RbK+p522gxu2yFaFZpSsPFyWVvNyJ4gI8vkMM7VWJNn4mvZHdq7uaAVZZUSOEQ22CMQY2k6WJzuEYyxuFMiNxyoPvEHOvk/KKwuN2Tgq0HEAMLWrVtx4MAB9PT04NFHH7Vlrx5+UOHPrzYs/RrzKqHO8xLzXCSb5cayGBuZ4P0sUtES4tEE4mkaIStuxkMf/SjuuedWLKQh0qpP5JKXtMFtjYMi7QVi8dZp+vfs4+XETPUmJaX6HxkZwYY33sTo2DhWr1mJ++67nZ3Tfa3QnmarZ1j+gYqt8sojVc6jmC2gVO3A/GU3Y92dt2Dx8m7GR4O+mkbMVsZp++YKmlo7MG/xaqxauADz22JIdnSjY9k6rFm9Crcv6sKCWAS5POuotRu33rEaa25ZijmL5qOZ1+loGpFyAR3pFDpSSaTo1rxkHZbd+SA+8Mh9uGtNN+tdeUtaXmP6ChrTjcZ4HWuC7caVZDgqvGQ0hXS8FZXWdixesQS33bIM8xcsRnu6FT3xAuY0sx2XLgLaVqOrYx1uW3M7Dcx1WHnTPDQ1Ka4kFi1ejBV33YV5S5eguzWC1tgY6yCH5th8LGJ6mtTMpduRmr8AS1YsxIo5XWihdCmlOrD0jttw29qFWNmTQkssTgHVggK6cdPabtx9zwIsXTwP3W09SMdaUSgmWKZuLOich/mdCzB3+SrcdOe9uO/eB3HP6jWY01ZjWNZNUye6u5sxtzuBzvYW1tkcLF99Dx667w6sXNlNw6EZkWQH5nQuxJqblmDdzTchwX7XxAF5rdaEXKUZ8VQr1q6Yx7wtRVfPXPIyB+fk0ZZUxJbc6p3vRMdKrLztYdz30EO4de0iLGiNQzvcxetPk6Mc2Md47gZWMrzFbzq/8Z4WhLh06JXf/v5+HD16FGNjY/aa8ZIlS6ZWP5ksnkGWzQ5onSyJcjWiSeBIAqO8bp/TjdtvuQtL5najLcU+E08g1dSGlmoU7eyfK+66D/c+qH61DF3t6nDsRYxD/Uq6QMX15XZF18+1rwOvP6THh4eHceLECXuVXa/k3XnnnWhra5vS77O73RrBfJqKVhu6up7+VVn0o+8cSba5NlEptSdTrJixdk9QDi9dsYwyeCmN1R40x5NoqsUoJ2mYRmmo0roqVeLkh1bcR4O2oyWBiXwZc5etxV0P3Ic7bluL+d2t5BPqgniKg7ZFthl+99yV6G7vxqJUhjpnBJkWPe3tQPecFbj59gdx78OP4s7bb8a8Zn1jWftD6WGS8qr9Q7SCaLodznWc7WjMr/hQ0LVe+3v88cfNfrzjjjuwdOnSKdkR5MWrCiUnm88na/YfL5gPpy91dO3i/uQiHarW4iApRn5KNpvMED+0NiXRyjhi5Knm+Yux7LY7cPuta7BkAfU9o0vRUNPDtFqUxDjFpYlIgb+0X80icjrZ1ca1QWMbeFki7Nmzx8YDaktN8N52220mY3wYq6eG8CGuPFTnvq85TJ9ba/CnxrFQrjCK8YxeVaT8ow29es1qLJ7bg462NNo7WjF33gKsXr3WNtie21W0j3RoQiohuRmnPdqxGCupL+996BHcffdaLOmMI1HII5ONI9/cjSVrVmH10sVY2N6BluZ2tM1dhGUrV2HpTfPtrYfuljb2kVba7Iw3HXe2P+3vjjmLcPM992P50rnoatJbCZoYYA+L6gGVK4P1Po15RL5c9d+3H0NcDXi+2717t32QQK+r6vXWFStW2LnuXXOZcFbSvl84R5Nt5CdBLi6vutLrjlUeqhgY7MNkbgJR6qpEuhm1BGX8ggV43yP34n13rcZNC+YhlWzi+DuNRSvmY93tq9Da0YV4pRXpyHx0zmMfW7sKKxe1YQ7Tyxc47k134KbVy7BuDce4LRwDs39V8jm0LOT4es29WLpoCZY0RzBHe3hzvFyKtaDCcbse0GkHIKeZZie8HFJdqg71ivT69evR3Ex7mnyxcOFCO/c6RWjkj+D1f/zDP7Qj1aZrvXI9gXeLoMBUguVy2ZhW+MpXvoKnnnrKmPn3f//33X5KRJCh/fnVxFTl1mwjJtsYtEhjQjOutaFx9Pf1Y3zyAPLFMRRKrahG56O5qx2di+ahu6cb3bS3tKFchSyk7ciV+0RET3s9gmfu3B8vF3y9Betf51pdoNVAhw8fxp/8t/+Oo8dO4DOf/Th++7d/mXlkGdkfo5pYKZNx2C8qsSrySc0PT6K5nENhYhyDIy0oVNtZ5hTae2y+GZFKO+LRCJKFYZTGBzA6WbQN1VtbW9jxRpHPZTFea0aECqyHg745Vd4fHsLYZA6xFAcHVI7p5iQHfhXk+kcx0H8GQ2RqvTU02dKFahsVW2sz1nXEMKdnDt315DyGZI2KtpanDGFZI+1W5nKmHxNjwxgcGOHALItMMYa+thYsmD8PK7pT6IrmERkZQOZMPwYnsjg1ZxWaku3oLiY4UGlCWw/Q2lNm09eQGaigkKdhPXce0u0ptJWPIza0DX2nBjExsBrVchp97VSlzQnybwIL5zZTMdMQHctjcHAQldYIWrpa0UKDPGr7cpRx6rRNzaO7o4KOdqeIM6PDOHWqF6eHEoim2pFqaTcDV3uKdXEgOa+7jddnLM6BoQlMZvIUqkALlXuM/akcm4Pmzna0dpJlkUdxnIOf8SiFIMu7ZAEqrNdEhAq/XMTkZAajIxM2MOjp6aJxEEVhdAATQwO2h1j/xChGyfeV9jvR0z0Hi7qTmNsWRyuFckKzoEyhTKEpno1WE4jo1R/JGW2aa5gWOiFCzAQvl3TU3nU7d+7Eiy++iGPHjuGXfumX8PDDD9uks5djV1sHXAxcGTTh7/SEhKf2aziWGUI2U0BPCw2P5hbEk3pwQhnKwQFOn7LVpgPxRUh3L8Kcrja0NWmYy6Gp4iFMF6jM/spO9HNt68DrD+lv6XE9sJLRIcNUq0++8IUvmOEh/TKb2+2csPZkU86QZ+klNYSkXoUy0FqDP9FKGdHcGdtHa3iSMjPWinhbBxLUVUmaOS1q0kgZxcgIytU88uMF5IaL1IsdtLGqGJqcRC6WRnNHN+a2ptBRyaKczeAYZXykqQtNLd0mw1OFXsT7Xkff6dPYgXWs4xY0N7VT53RRH1J3ddJPnBZHhHJfeYQ+OEJdwuTj9ba4XuF5yR8FGb3+WvuaffGLXzT78Vd+5Vdsj07JDiHIi1cX4qVp22sa07ox6MP4yV8wv+6O06eyPzV1Fc3QHqJdM54vI9/cgWbaBdovlVIHTbR/Egwi9SzTTeETtNkE3jVeUBpu6uvqo7ENdK02VPsI3/nOd2w8oLb85//8n+Pzn/+8yZjrcwL9vQe11/SxTnWGrUWo73K9GB7IYvLUPHubIxIrUx1S7lESlWQeplLonrsAXZ1daEsdR3FiGKOnRzByOoOJbAJZ6cp53WjvbkdbRyu6IxNITfZheGQERwrakyuB1iJlQCmKcaSQb2phf29Fz5woOtpa0cExS6IaZZa0p/IYKsUyxieAMQ0gOuagpa2J9msNqar2xaOujadMV9vDKmMr8RkzGrLYNYN4y/OZ+rrkw2OPPYbnn3/eHmh89rOfxYc//GE7171rJhNcFuu8IhntHfxZ1Pbw0r7OBt9n2F+04lv7PJdKefT3H8fQ4GlkJjl+Lcc5fm5CkWPdeXPnYGlHGm2JCCbLNfSSh8tMq72jBWn2o8RoGeXRHLIoId8TZ39JYz7tjInxcYyPZhBPpNHexUFsPEE+j2JkYB/tNvbH1EJEm3rQkqyiM+621shGmpk3jtv562ZlZi/U5oLaXA9HNBn6R3/0R5gzZw4+9KEP4Z577rEFVH5+SbwUnADTdZBf9BaGEE56ET7PfjBTZsWVycCqvmSFHVPrCaOjJG0Q3kwGb6WxyzrTii75qWk5op4o6KmxVnmpG2iSxiN45s798XLB11uw/nUenPT60y99GUc06fWZT+C3f+tXkdDEHhWWPiwcKbNANKSq0RqKSW3on0G6RoOa9ZEvtNPwb0aUnSeaKLLraT8nbYbOzlMaR6KSY7gkyrFOK2osmrM6yNUSKNY0yVNDK/lAdatXgmra9ywq061kG/AmNYnCvFb1JSLeyzKuQjRhE4ntEX2dkeWwScSoTRjF6U/FrFSStoQ0Ws26tmN+9AVGfdFwKBWHNrRvod9UNYMohY42CKyyzOPJDpuwayqSLyVd4ixnssA4mUIhaZNKw2x8LX5rrg2jqXJGH89CtbiG+Y1hNMX8JyOs1xIHHWU0sZypomUIxRTzGmNbMD8xkng/X9GXKYEUByhRKmH5s7pg3iu1LlTJR2WWVeXUSgINWlT2ajxv9aKvhQm2p4xWXbGO8mV9hYP3YgXWAQemrMMmutED20HtKgHA9mK6xtMlDV7d65DVml41Vduy/vVapNqY97KJHtZwBCnycpKkenaCgoM7M3iUfsLlR871SS+1S4gQ54OXSzpez5NekjAUAtan2EPJ/BFkY+xDNFaaImnE2Dd0R19SqyGHVIGWOAexuWQXdYo2vXeSX+tykoqHOEsXqOxT19e2Drz+eK9PemmljDsLQHqR7hW2nV51lwfpE7UbKrQFynr0w4FUlAZ5LM42d+Vu0t4eMclLGpnUDdpzSfsw2tFW5lB2U15Km8UofxOSw8xHVF+Opq4U10iuJmoTSBR7GUUVE03rGFYrmVTH9Mt8aVU5agWqAukg2is15qP+wM3Wb19P7dAAz0v+KLynJ70E6lt/t6Sb4gmzv2SL0T7gwEaTpvY6NW8naZzE5Z1+ZUsJcdpsQjjpFeJyQG1mR+M4d26sqbXNkXEyGm3lwhLnKHfKPtm+lQT7qux7BnE8OEyRxrat0FKkza6xRDbWArIo43H2fbKcpZ2eo+yMoURelyxLsiPEKBPz5HntV2j2rMYMkrwljg/01oG+pq6vSFo6LRyrRFBIMWIavgnq1wRlrOUhliT/aawj3uKPndXt2BDXBOIvz2Pq69fzpJd42K/0sjKR7MvPGseR7ypl7ZMtHVa2j4rFaTtEI0lMcqybIK/GOSaL2rY/EZP19lqi5iAYVZpjywRNRQ3Rs0nt21lEN+W/6qKmD78xfa341TRFIkn9UByxcXGB9miZ422NJdOMX8hp33EWRNaErAXldbbK2Ss16TXtIwQFbgK1RIrGbRTpCg1STeYgi2o8R+bpptGxkDWmZbQTaIpP0rTQl5XYOGSsEo1SGb6a6IiRyWclG0WoACJ55o35q1DpVNM8Z66pNGDLH+mFvSym+/oke62V5e1AsimJNL0nE+yc7C6Jql5otIUOVHTqPnoJLoUkHWJkzlyVgzwO/rQEv4t10SrmjTPyFGsryQEU67dA0udTazT2TY6w7ksUbpVkAq2MbUGphi4qyQJTzLFuJQbSHETaK6RUbohygJxgu8QmeGS7pVpYnBTKaSrbVIHpAl3KGcsRq7SjEp+HQvMC3utCd6kP7bUhSggKICZfSWiirI3KuIUpq+VK6I4U0VXL0UsbO99tTONW5NvJDV15tFH5dheBjnKUoVgnGtxoj58UhQzzVUIzi0SDwAa1es1lEKXoAOOh4ClR6BQ6eZzHhOewPVTb9EW/FQ1gYjkko6Os+1FMVNuQjbSzvHHyFNumQuFaZvga24PJxfV0jR25qBaT7KvmUS3l7Ou0qTIFGstu9ygIkgwWUyQqHw2JGuu+miAHJ1uRSLWjLd6GDqbUptplm4n/JYgRzZE4uKJEjZk1znjZlPpKnUwIZ0aECHGDwAQfB9YafMbVF2RcJ9AST9N40cQG+wm9xOgWZf9l52IfS6GJ7pRQpi8EqmNTyKaUrVvVr93tEFcSkpUiq3vWOc9tDw3vTqpSyGmrAmuaupvmJdRuiLJdk5TLKbWtHlJU0EQx2ZSRnzJ1CQ3XSCtlbxeKkSYO2ArUdVlardS1lM1NFerEkh6AAOP66EmyDSXyix6hxSj/o1HqNA7+KunVqLXdgWYaxwnqwhR1d1NkEmkODhOUxYkK9W59M3Pa0yb3tZd5iGsB6VZPYhhxTn0QVCdBfDbFa0HYgMkkBy0sDtY1AGK7FxNtZp9weES7a4z3tOEB4yPfFjhY0l6C8SqtpBptuHp4pW18SwoRYhpBTrww/IBRDzUdOa6SJZ6vddKu7JDpr9Gzsb22SIlEOLiPjJLHB9FcPkP7exBl2rm56hKUaIPXmloRaYqhmWFayfLtlQw6S2PUm3FMpOYjm5hD7m8lpWj3kyiHtaKxi2OIDsq9FmSYZMb0qB4ilKPNHMh3ktops+McAEeQZjYpma33SU/r1WHBlUekO65swSrRwffeECHOjwDj8Gh7M54Fz2e0CWUXxjjGjLShGOtBNdnDcW4KJY6nY7QNNC6vRCnZOQYrc1yWLo2irTrBXkZbskZrgraC9teOcUzWwjFZm+wI6wEcP1ORVKkTapT/GglaqrEujgc5budFK8dvTImM3cSxo+wFbV1P28M43feJGwuNLXVDQ5+J1ga1ZtjGKOTjcURJ+hS9hGmMgjpCI0Nf8NITcC1e0qSuKjFG5tFn7PUkKzjbOCVcieuFvaTg4lEZ0yxctQK99lfWxr2qHxr4uicDPUH7Kqp3OvT0Tn45KoglE0hSybhZ77pgoHuVnbaQy6JQKNsMrBtO1FBhfaqumQgVHdOimzZy1yxOjaSuKZ2qWlY410ZupZeUMMWJXdvnvXlP13LXfe0prDioDS2sZUWdXDNADFMpaxbessFQTIdGZIT5tydWLKeWQ9tsPe+xGihaJFTYzlrlZVq1ynFM2fKs/3KxiiLTU5Im6LTPiMpCqGw1LbsiL9l7MLJNKYuKlGfKkj5rr4QkxBiY/rT81bKOmgrC/NqKAMahvNg8otqBSt3KawUg79kGXTonKTz9lUrMV5G5LxWsrrygszpRxgUmxFayP6ujqBpXkTq/IUKEqEP9g6Q/9f1SsYQS+6h7ssQ+wz6qXqUuLVT0JeBc3l7BkGBSj5KMME8BqouoELMAdRFpMHFIUttIF5oAlv6AJrgk/ylk5Z8yN0KZL9kv3vANKy2VoFFrsp/hzHAgopSxbj05Qa8SuXHyj1x17fSa9F3dC4W5nhoblCEloesyFQkZSk71hTQhrmdIaatt+aOn3fogkHhMskV/slD1FyLElcbUoFjiRjqPpC+HJiIUdlqVwgF4meN27QxjPMv74k3Z4jZgkh0slUhSVNKRU+MJqUPqRfF7jMJLoktvKBS1cICRJRhcZK+a036t0cYv1vQCpXQt4w+C3UFjACd7HbR4QV9KNvtYeVK/ChHiCsDznIN1BHdqoAVA5jeLQeNK/mm0JftBMN6UL/aRWJzh6iuXbPWY+FdjOo5LIzQoNf5LJnitDmX3aS/YHEXctq+x8TEjs9scWyvNCvuK3JQljcudbVLHDahGWDUhpmBWI48mnXlSiZJZ9OoAKULmidD40Gbq0S4yVQdSsTISkvZk5JoEs4SqlhvaiEaMNc1cATa7hlC+xP3TnK51XVpJpBUL9bcwEGMZ4rU4SjE9pW5ieaNIsvPoCaQtCGOd6OmL9qySktKm/xWbEaRjicMANwND4lEFj9LwV7x0SrDjaplhnB0+RgWmV+0K7MS5ZBxpdk6tMtJkWjWlJZsRtBZqtkl8pNbMn3Z2/Ca6x5huFdFqHvGqljczkbhWjfEetBl9kz3pSbGokfgk4xrjMcd0mX/+VSNzmN8FzE/C5Yn+ElTcsSIVcTSDckJLolP038L0UqhQxlRY4KjWjzKP2q+nXNPsuvbRaGadpI1v4omovY7ZwTJp8/cC2pGP9CBSmY90dRG96H1qVmBNGyFngCYOhFm4SrRss/qt1QjS2qBDy6hoVDQzuWZ6j8TSTL8FtWTavlKuFqxEJlm7OaRY5U1V7b3FfLI8NTM0VGFlW4GQEqn9Em2Upa3MJwWsCUO1ZhPjYcoakDFck8VVYf1pQ9wc65LiudZKauN9xsk6rDFecY9I8McQIW4ISDeoZ5Dx9cxMC9WbE81Ix5JUH3pqN8F+mVc3Y7+PUIZ2o5aeh1iacikuY15P2ShvGI0m1SVDjOp/MmTCXnWFoSYUedSv1bTWvCS92k7Ray1hZgEbTYuVo6Ynk6Q0dWITdVYT3WIoNVMnNEluTlI/TlL2lpHkoDBF2ZyqtFFXtmCcYcdT1HxxaifaETEyUVOFMrySRTROXSi5W4nRbxMTbkaecj8Xp5Gq+TKK9XikiXxFWaynvHHJY5LkvVYyKJMhriFU/+rZItlUmhB3utrDWkg/DU0lHjN+Y1ARtHpeetlWsnDATr7R0F1frJb9IvsrSt46e7WYIpXVQ3vNfIcIcXlgk11TvK0PfOmdC61kTdP+pl2dyJBd82S/EuVignxLnRdfgGKUx1o3naOgeKRc01seTajSpo7Rxo5TfmnPXyS7OT7gmCMyjHRkHJ0ciDRzWJWuZqldqU9leybJ17RhU7TJ42hBiQP8vCYIaIs36yNTWu2YStFW1krJqu3lFaUtqzUxmlrQhJf2XLKHUuw71uk0cSaqw5zqFCLE2zETZ7zdTbLX7AhBY2Fjqih1fRxt1O/NpTiSRdoOhRbKcvJ1JYVEJY9kdZySu4CyNpynjZEuyTYoclxXQzYdRSZZYb+bID9nUK3UUCFj22O3qCaCeWS/KeapI0oTjFd73Wm7hDYmnUaU/S3K/hann3iF+kUT1ryrbYNuNEiKhahDq2wcC9c5VsI+aAmT3CwpDVHNmNJdtqZmcW0GVQJVU6w6BqAQsw0z5skcWQcaeLFT2ORKfVDmqsGVvlzWCxwaCNC8Ynn1ZRQZ/lZ23nHDN/qweBiLwtJ4j+mxDePQk2tNlmkVlQw5GXyqs4jceNMGgXTTk28NMpS2RSJ2VR7Mv9wC+SJJsWnFhZ4+acTi7k2TcqU9zCqazDTr0pVHzeVJviy/YgTGU2V+NDOvCBIcXGhlld1n2aee6HslyoOew2p/N4XXujO97CRlqy9dukToTweWy+RhRDubub21tJLL4pM/lw0bbCktrb7SQFtVqrKI5ywqHjWJqJWGulcqMy5NwDJltYTI5bLOnxaHV/QKo3g1iKd/1b9zVsRKWCd1EhjYKESIGxTsFpJP2n/QPbFTf1T/Ul9yT/DU+a0f8aYemlSdYKEz79nTZvVJO1hcBh3qpyGuPdikBjWPJzk5Z/6aB9fu1vZs86oMyCot0QplsB58KYwRfUjOMoQ2zbeVtCQ9tZX+096adSeKXOpJ6lO99m5fgmYEkuYm0hUnSSuR9WeRM22nV5QfQk4hrgHq9T91PBszu9bReFPtKVFh8oR/ZD7JFW1ObHw4Y2RyDJL/DRHi3WFKR9UheTdlFzoB54j8KltSW16Y7UsDN0K7V/ar41nJQNr/9KrHrhJWeo28UhWJxzWuUEj5JPFHMtLCcZBQU3y8K7KbFicPTFPk3r6RfV+mf8U/DT9GCBHiiiPIZuRL33/EyjYWkz1Afo7YFjTyzHPeNFZnL9DKLPPJMbWcqrIB9IYZL8wL/VjfsMGh9SLeY8/iuRaFRZIao8oG1V+9N9X7qB2sL1lEhIvxRoJqJEQdZleaIJZUFjeJqTSNIVEs1pJgJvRjFiyNEBq4NpEigW/3xESzlJFMaagjqRPQOGdHsaVDJKkalV9GudMNVaqguhpSmTh40yf6bSNdbShZtd2irEMWoyT1JrqovhS/rlR94jCrLrtIMA52QyYbY30pvDbd1bltqqc9vqIpxqnVWAxXJ6tX5OgjY+m68MqnSy9WZegy09UTUJMsTDGa4b0MCkwzX2ti+yTor156epFdaS3KtO1La7E8wxR4N8ks27uLLnHzpdcLWDsMpLxoBYc25ZQwK9n72KpLpqmbFeapvmROJeYV9BXFqFYE8r5KWo4lUIrrYwlMjcFS9YrS3nBaSYgK0y+xTJVJhsta6spZUXVBrzYZiDyTzCJaLtvqOxVZ+3tVNFiK6p1JUYH1oVcyNRBjlkhqZ7WH3GK1EsNpsk3lUp1rRWMMBeYhH0mjqPYyYaonAmlSkwLyn/HaihWtnFNsIULcIFA/t5WrkiWUJuo7muxQf2N/MMknQ0d9TuKJ/UUTy2C/F0k8xdl3ItqDwWSt7hHqV3aqn7pbiCsAyatGMsFdP4rkFvg1I7SuK0hTPikbtfpbq1+15k+yvhKlnIxqtQ11hIWjwcpGFzWRD1LUG/aYg7pG4aMc9Gmj+ygHfrY/F2PRR030Mn1TeZw0YfnQAmBtgq/3F7XBbZZyOiu/it/SoP0hsrAhrg2m+22wFXTurvUrnpC8kM0gmuY7SQ3nj/HIvqEcEV9JZshu0FR5lQaABkomhuhTer9+ZmEcBXMSIsQ7gPipThoGiYTgxJc+oJAmyyblZq9+iMiXMkzN/hf/6W0OQjKTfi0ucrEbVdBuFA9XnD0tW1/LWSNoIdH+174ftE2nbkoxisVNQWqVilY60v6saWUtY6W9amMHerKhPjuHyDqJ5UThGJU9cBLctcKGCPHOcX6+EXd5s07QxJOz88R/lPnU01L1WnAV4TjVSIMzjh0j+qojb8SKHLeSp/NRN2bWh0tSDJSotCBa0kpwcrWJfWkIjhttDEc7RK8YaCW4keBG8W52gve8urH+XHe7waBqC1GHZwOtqHH8IEYVMwUnvTRbSnfjFXJQjQxVN4SNj/QzJVxnF2zWV69tqlvaQE351LU6jsroimUKw1YysLTqrJqU0WyLFJUMdQ36NFmiyT760bdTCgqpelFPZBirRwvPM4uP6ZB0qhQ1zaZJL5FUlRlv7OD6CqSUp3Sd6tQjwlRAM1/KMMob8m+TXhIomuwS6Y9umviSIAEyVJ8aYupzxXHEWA5NesmKND8Wr34UIUuhySJtQE2B4QQVfbM8KoNT1rwt/xy4yF6t6fVOTQhF3T3nQfWksjI8r31ZbV8CutUiccq2GAc9EftKU5LMlpbfKH1ZuSkNq5r4knLP8TzHlCsosk5LJCZtmdbEk+pES7hVH6pwDbn1ukstWmI6HFiLNMBmDLqv/Ghiy+wIhrOPLpB3VStgWStMX5NeJRoWhZo299dUpGtJN+llW+jSvya82A4qlyt5iBA3BigL9HU++2qs+o36u/WRMvsXj+wOti+f5J5EoW4LsnL01FtdlH1H2wFPwfpz/STEVYBkVpCcjHMaR9f+l1DbsD3dYxznz/vWmdP8mvSSLqObJr1iaWtnG9IxrCa89IAjJcOVpEkyeyVBSkReqLsieq2R+lF6WJoXHNTpq8Mi5cGepejJLmW05HSBqeVIlg/et5VmVIqiENcC1giOZoTaxfOQeCZI3roUOcjuIssYD4n3NLCR/DAbgp4kYswGUroSNFNkObH758pJiBAXgufDmaCPZqTItjbppSfQ+lIx+VX2q+xlSjPjTWcbTsfkpKX7+iKlnQQamZRcqgPt/iiaeZliXIzTDGwGqge34QO9aisW2eZ64CobVC76PIx9IoZpuzcwmLbi0ISbDcrUF9xD6unceLzdJUSIc+Mi+cW8eQlMhjRDUHxNipEPpc81L6UP3ET0KiLd2R8i1QRiFfaFUhwFyvuixrNkfG3Vk+T9uF6HLHEcpvitP7jtidSJ1BMMtuhCk8hK3+kYx/mk+sGf+t8bCU5LhjDEWR0ivTI2xa9EXYwbEzlGqkOTIvEk4rEEtLmjfBjqgnbWYip702XRmae6djHF5FSMu3bEc7PoZYS5EouJ7EwXukV/xlhSMurnvNJSTAWbCmBCgD2fDtOv3fFK4eveDLo2b/pR59bEka71o47u4pUfc1IkVv+KRfmnsKAFGLMw9XvKl0IygHtNUOpZcUkxSnDIj/wrTreiQ+UTH4g/bNaeylVHuQmmXJVFkTkxBbopWUUUYQbtVU3eU1wuVcuU86H0PGTtagMZ2/vFUrRyKGrBCTCtwnJ7GNSzYHl2pxJ6PLMBuYjx6Z9Uv3K/9G/VoUv7cfeUjrZLsDojXG59OMXgC1n3ECLEDQdN/KvTqI+rH7A/mEyTfCDJ8q77cRMm9Q5miNrrzpIfnqxz1g+zDcGn/MJUnt9TUHneXia1rbWnL7OO5l6/pzObiPCuHv7c+Vfzqxalp+Jse+mUKbZQvFO8JI1Gf5rgkPwnSTu5V3h4g1B8JqN1pF60FYfm6iMMMbuhtgqSMMVN5iRzx9jN7gm6x5Ymc8g8cPd8W8uXuOZsNPbb6wHvPblyfeGiJIh50I/aykkiF6Yuv0xWOdvf5CUFVYQDfXtLhD6shRVAvEzyfC7S/Zj2KZQuNaJdLg/0L3YWSR5Lf0pGmu1ed7ceYH4dif+1DYFz9ilMH9zJ1IXh7KsQIRrheSZIZ0O8eBY8g0v5m11Yh/jWuJZ8bIYB+d7Gc86/Fm2pd7kU6kyuW3RU1/DQGFSLPbQtgqUVgBtlOrIeUj/YK8eKzOj6QFCfvRvdFqi6qwtvRAbpWiBYeQmSJl/11TzbaZgjfzGU1v6kyZgifV2pFqVAp58afYviFLB66hGjULcnEtp8lm6evBB2xLhJ18QgYZpuEMZ8OJPZnAVdWdlVvliKlLbXMZqZTS2ZrCVJrBO9fqgya1WWVi2lWDvttSS0vWQtTiUTrbIuqmiq8qgly9E0/dMv07U/+qklSIwH2pS31sJcUImxPjXJoqpXrpQXfXLVOreyi3YeutjhtaElL7WcutZqcei1D7WJXruMk7TXWC3WZZQiX2mT+LhWaGg2jmWJ8VzPyN1KJT1JVYrNPDZbPjQjX1OZmVetCEvWWE6WMU3SMRKnIk4y1/EE78ktZULE+MKHY5TKf0zltsknhmHyqn/xS7qWYDjWi1a2sR61J5eK5XhPpMpop0MHmlhgbV/cQhKfubm7OY4U3tLTFv5sGd6P1hgOHbxqJ7mNDK3emT8ekNBqNrVjXBvw61zt7pLVi51pxtFM0ib5NTK0KG75ZtzWMtqQ33+r2iosRIj3PKSj1AMkL8yMoBxJ6Ek3z03GRVsdsRe5fZuc3NHrzTL6TU7p9WXdt36kvkMyZUL/JE2esJvViT/XGNq3UPnw+nmmPM2GfF48VI56vU+R5Jgj37YmgknSDE5fyp8ml2LWcnaP7RazlcGSmpS+NVoIrIuE6st0klY+RMxNloKeBmlFlrZaTtSayBuSy5Sv4o2k9BP1kvhFqWjFQ5QynKR1DGm6x8RrJPFTB91ElMxM302iuTPmvt5W72WojNYfWbdB/hSuWfmVbD3pRg6b5iHxmbjHLBw71yOt6fZjfxKfSFfzWjaHPpYQJ2/FIs3GP+IjrbaX3tZDO9kPbiTEwAG6Xvnges337IdnjvNBsryRHHxfq8UpqxKykXW3xUhvRUTJm3qrIUn5lCR/anJKb83o9f9qrEJ5F+G4QB+s0lsNvKc3LDhWkI3s5KZkqvq0ZKfe+NBWJ+ojLm43F0Cml90sO5x2t3pNXH2FZHY945MurlK2RhlW0jmq/cL08J35EfGHHUedp071KuHZFIUIMYWpbqMfcYesAkeyBxxPknk9kQP1Z0cGsSudmIx2slq8rCFeGj20Hrp4zdGdJq04ELOxWpPrWRqHufEs+4T2gTZbgUR+158+OJdgX9BRK8LMVeNrjQnJ63KP836UVGO/sUTZpWTX8Q5zr3LMTng94PW7Xk/29ui7wTXr3+8249cSaoDLQSEcppTpeejiwHq9TH+XEzO1fSPNVOaZaKawl0IhQoR452DvuXx/M/TLRgoxezFTe81EFwP6vOBfiBDngmyDECHeLWaSX28j+bsImtGxgRjdeeHTbLSDZ6IQIa4Vzuof5yCPIM9qIqeRgvfPRTPF30jvZbybMoaT2iEuGTMx3aUw40ydupFmwqUyfYhLQ1jfIUKECBEixLXFTHbR+WylECEuH2QHXpi0AuZC5PxeHvixx/koRIhrjZn40MvuUH5feVzTSa/Z0MihIHx3OFf9vZN6ld8L0blwtr+642WA4jo77kuni8FM4Waiy42Z4gy6Xcm0Q4QIEeK9jqAMPReFCOExE3+ci4KYye1aIhzA3dgQK16IGnEuHvbu75ZChJgNmIk33wldCi413GyBz/+7LcesWel1LRXku2Gk9yJ8fZyPgpjJzSMY5t3QxUN+Lxe9d3Ghen3n9R4ixI2CoIx4N3T9I5QTlwuNvDEThQjh4PtdkEKEuHpolE2XStMI8nAjPwf5/FwUIsT1Bs+72qvKU5Cnz0UXg0sJcyNgVuzpFT4Rem+gsWNd/Y4WduwQIUKECBEiRIjZjkbbPxwLXA+QnX25yOF8Y4VwwB4ixI0J9f3L3f+vyaRXqNjeu/BMGiqqECFChHhv4kLyPdTxVwKhTg0xu3Ep/T6UFTcuzjdWCMcRIUKEuNyYNa83hghxeSAleTkoRIgQIRoxk6y4VLo+EQ5ErgQaeeNcJJPtfCQ/IULMLmhi62Int8JJsBAhQoQIcSUgK+maIVRuIUKECBEiRIgQIUK89xC080ObP0SIECFCXCtc0UmvarWKWCxmR6/sdC5qPBf8tfz685AujnydCTqvVCp2rafy/jzor1gsmt9G96DfkEIKKaR3S5ItXr4Ej1426bxUKk256Vgul+3ehSiYTkjvnlTvagsdPeReKBTMTW2jehe06apvA7nrqGudCz7OkEJ6JyT+8fzkzz0JOnoelB8vKxptnZCuPqltdFQ7+LYItp+/L/hztZuOsknlpmtBbu9VCtaHr4eZ6Fz3Ljb8xVKwvS6GvP/zhWvM40w0k/+Zwgf9nYvOl5cgnc/PuynLuWim+G408vUgWe3ldbB+BN9+cvMIXsuf9yPycYd0fVGwDc9FQb+eZ2Rvyk2QjvB64p3iik56eSPEM62O8Xgczc3NdnwnXysI6eJI0FGTjapbHUWq76amJqTTaSQSCSPB+xMULmyPkEIK6d2QlyUzXQupVMpkkZdDyWTS5JMgpSY94XXDhSiYTkjvnlSnQZ0g/a1ztZH0tkjnQf/BdvDnakPvFlJI74SExnMPnUt+iMSHXnZ4fvVHHz6ka0ONcqGR1GZqO7WjzuXm5Yof9AT9v9coyKPB80uhdxtedKH2aiTv/3zhLgYz+Z8pfNDfueh8eQnS+fy8m7KcCzPFd6OSbyNfz8H6lhwQBceskgmCtycaw4d0/VGwDc9F8ifo3Nuj4gFPgj++U0RiDKuT8iVGMBOCmfFGs/C1r30NP/zhD7F69Wr823/7b82AboTC+gIKvvAhzg/VlyhYX74OVZ/Hjx/HX/zFX+DYsWP42Mc+hl/7tV8zdz/IFDxD+usQIUKEeLdolCdaNbRv3z688MILJpd+7ud+Dvfff78NgPRER9Bk2MXIoVA/XF74J2leD2jVl28L6Y6NGzdiz549mD9/Pv7xP/7HmDdv3pRftYVI58HrECHeCTzviBfFWzr3D09lAGtF0O/8zu+gpaUFP//zP4+HHnrIJtHlR34VRgh57+pC7SOo3v25h7czNZAVnnzySfz93/89MpkMfvM3fxM//dM/bfd8G4Zt5zBTXV4KLhTHuer7XOlfTJ4utg2D/i4U70z3ffhzhX0n8XvMlPfGsBdTvneT3nsJqgeV0deHL6+uJRsk19X3n3jiCbzyyiu2OONTn/oUPvCBD0zdExTuYurqvV6f1zMupk94fvHtqHHBgQMH8OUvf9lszg996EO455570NPTM6VTFMbrfsHH4RGvn1+xSS9PPlGdf/3rX8djjz1ms7e//uu/boZKoz9B597gCXHxUD0G4Q0N1ffp06fxne98B2fOnDEj8ad+6qemDEgP1bsfwIQIESLEpSAoy718F/kBbD6fx9GjR7Ft2zb09/fj0Ucfxe23325yKjjp5Q2d8yGYVoh3D+kM1al0g9pM7eEHo6dOnbIJr5MnT2LOnDl43/veZ0aHIL9efyiMwocI8U7g+7LnJfGclxniS0HXuVwOf/zHf2zyQsavZIef9BI874a4+pjJbldb+PaTLFF7amD7k5/8xHSBbFHpAD+4lez37X+jI9gn3i3OFYdPoxHnclc8F5Ofc4UPYiY/ijvoHkyrMd1z+fM4V/zng8JcKN53gotJ770O1YHK6evC17Hkgkh9X3bDa6+9hh07dphs14PQO++882224MXU141Qp9crLqY/yU9Qj4hHTpw4gR/84AdYs2YNPvrRj+Luu++ePZNegjIpJhbzeob91re+hb/8y7+0GbsHHnhgylDxmRP5jCt8yLgXD9WV6sxD574OW1tbMTAwYKsrZGQsXboUq1atMkGjJ21iGl/nokajJUSIECEuBl4GedkteS4SJFfkLr0wMjJiE17ZbBZLlizBwoUL7b70gY6SScEJ+XMh1BGXF6rPxrbz7TIxMYGhoSGMjY2Zm1ZsS4d7vz6c2lfuOoYIcbFolBXiuWD/9nJBMmPz5s1mvyxbtswMXw2MdC0oDi+HQlxdeHnhzz18e2g8IHdNoB88eNBk/Lp166wd/Z5eCh+UQ+9FqJzB+rmUsvrwF1tXwfSEmcI0+rkamKke/DFYRmGm/M10b6ayeVyojI1hL+T/fDhfPjwU/8Xk/WLimo3w5VO/9uX0ZZFckJufuNBqctmFupZN2N3dbXJdpDDev3C91seNDt9+54PnlyB/SO/rYfkHP/hBWxmslV5dXV1TvOPDeOg6yCNXbNIrWCC9GuEnvZT4N7/5Tfz5n/85du3aZTO4WsKoe4Lui4KFDfHO4BvZ16PqUHXZ0dFhgxVNNuop6YIFC2ziS37ESHqtSEajoPYItmGIECFCXCwkc7wMEiRLvDzxhosmQzRxMjw8bK86zp0718jfk3/vN8TVhepebej1gDc45SZdMTk5aUfd14MT6XDdE/l2lt4PJ71CvFOIf0Tq9+I5zz9eDsi4la0iG0arROVHA6P29nazc3St8Aonv6H8uDZQWwTbMniu9pPM15sHmviS3JAcWbFihT0I8YMW+X2vt5/qRDhXOf39IIJ+LxS+ERfjT+0hnM9vJHJ2vqau3pbdt+e/EbXa2eVRuo1lnMlNOF8ez4eZ6tVDcer+u03D42LCB9NrxLtNf7ZA5fN1K/hy+Wu/ulOryAcHB00O6GGGxq66p2vPm15GCOeqn3PVZ4jrA2pjkexMtbv0uRbsaLXXRz7yEfzsz/6sLZyaFSu9goypRGUAyxjRtfb00movGcr/5J/8EzOMG4Wsz7jcgwUIcX6ovlSHqjMdde3rVnun6bVGvVoqY0OvpWg/FrWNGEn+xFwKq7YKESJEiEtFoyHilY8nTZocPnx46vVG/36+9IGe9ksuyZ/CXQiNaYV4dwjWuepW+iBocOiBlY4yNrTEXJOV0h+aaJB/r7t9+BAh3ik834mngrLDT3qJF//Df/gPZkd+8pOftAeofj9Az78h710b+PZqlAHeXQNYPZ3/8Y9/bPt6aQLzZ37mZ+wVR9moXt7Ib1AWvVfh66exvP7c15uHzs/l993AxxFMS2i8FpxfT/Vfd0pMnVzU+C0S0TiRofgj8uUTvJsQzMdMbheCDxNEY/iZ/AjnSudi0j9XnOfDueK9lLhmC5R3let8ckFH7fPqV/E++OCDuO+++2z8qvGp7ELv/0K4GD8hrg0uho/FJ2pDPych0oTod7/7XXu9UXp/1qz08kztE9cgRpnS9V/91V/ZO5l6LeJf/+t/bRuRCsGM+YxfLHOHcPCM5OtM157EMBqoaBO4I0eO4OMf/zh+4zd+w+pZ/kXerxDWe4gQIS4FXoYIwXMvU3QcHx+3yZNXX33VFNnnP/95M278qiGFk87wuuR8CGXV5Uew3dQGagtNKBw6dAgbNmywfb002fWLv/iLWLRokflTGLWF190K522AECEuBuKbIB/51Ya61lFusmX0mu1v/dZv2asvn/vc56Y+giF/Xm7oXBTi6sK3l5fdvg182/qxwPe+9z184xvfsO01vvjFL+KXfumX7GGIf/1ReC+3n8ro+TQIX3ZfX4L8BGkmnMt9Jvh4heC50HgdjHf6XH68P+bTHQJwF2c5nQMRjkBr1emyCl5vyM3rEe8meL8XW+bGMgnnCiu/M/mfCReT/uXM48XGNRuh8qkNG+vXywlNekneP/7443j55ZdNDnziE5/A+9//fpPtPrzqQOcXqovrua7e6wi2/7ng29m3u3hD9ueXvvQlW92tOQxNenV2dppOEbxfj0Y+ueKvNwYzrXPRX//1X+Opp56yd/h///d/3/aa8n6D/oMZD3Hx8HXvj6pTD62s+NM//VP7WtqnP/1p+2LOuQzE4HmIECFCXCy87DkfNGjVpNeLL75oculXf/VXp57oeVysDApl1eVHsA39oENGh9pq/fr1ttGsvqDzhS98YWovtiDUJoojbJsQ7xRB2yU4KeAHR+I1TY6I97Ta8Jd/+Zfx8MMPv012hLx3bdFog+paMkSTloImvb7yla/Y69K/+7u/aw8+tJJDg9/GsO9FqIxB/vaQuycPz8+evNs7rSfvPxh38LwRjfFOXyt//oEUz90hgPrFReQrgumVXh7q4758M41Pgn4b8zgTGssbjM8fvR9/bIw3GIfHxaR9qZgp7iuZ3pWGr/cg5Kb21VH9Xud6E0yrvbTq/zOf+Yx9vVEPQ4XG8NdzfdzImKkvNUJtG/Snh65asPOf//N/to8offjDH8a9995rD77e6aTXZZ9dUiKNGfYI3vMZ8gLOU+N1SJdOHo3nMjxUz55BgmFCCimkkC6VvFyZiWbyLxIu1m8jCTO5h3TpFKx/nQv+KPj7F2onYSb3kEI6F4mngvwVJLkFecrbmN6vdw+eh3TtqLEddC34ox8HyB71foRgmOuS6n/izlKkYjTtqkmcCqKkmI61Es9VJ6yfapGUZ7gCMshhtJhBtlxFqUoPVfqpMTzjr7H6ygzLQBzAsY7lLj+sy0qkhBrv1eiPNUl3pldl+qKK8sFgjCwK5aHA6wxq5QneK6KSLyFfijK9GMq1mHxYGp7KTKeq1xFVhprCc5AJjiXo1/uJRHmNOOONM59yjzFMnvkmsVyVch6FQhHZUoz1EqMfukczqBTGkBsZQmZoGENnziCXLaBYrCFLmigDE4w7yzqqocxkWE5WgkrBBNwf86aKqSl/9FslVei/TC86j1aUV+bWKpvhGVOJ/iu8jERGmYdh1lEJKERQzEUxqXqweMij0aqqnx4ZA/OseNhadu3TKrMu2NJ0zbt6pRtHuKwnpis5xXSqTFt+I1EWqFZkeiwLb7nYSIzPruhH0deUthpM9xQuyGPXEVkJZnAPUlCWe+hcsiE4Xr2e6yGki+OF85HXFReDc/lTL7us8IpMUKLBpxk6irwf79547eHdQ7o4mqme9XQt6K72aHRrpMZ4Qwrp+iPJD08z3Q/pSlEjZvIjOeR1gz+KPILnF8JM8Yd0aeQxU/173eGhaw8ftjFcY/whhXQu8giezwTxnZ840XkwDu8edAvp6pGv+yD8vaCM93507eWIzoNhfbjrjaAikDRVUkTZyGZNRFohVSsZRUSVgrmx5ADPy9kR9A+cwI4ju7Bl3w7sOngIvX0DyGXyDFJBlfK3xPhKtQoqikpxSiST9Jqgu1tERXmxNPlTVfq0+cskuttEGMPXKhlkJ/swcOYI+k4cxfGDR3Dk+ABOnRnD6GQBhTLjY5uI9EmJMqMqMY2q4qJLRAlUoixDzBVPbVvjdY0DU02aRWL0JcryXga5/Aj6+k5g/76DOHB8EOP5CMvBPOTO4OTRPdi24TW89tzz2PTG6zh54hQOH+nF7v3Hsf/UGZzOFTDOVFXQiCatqswX01K1RZjPiOaRanJTnDUUmbcCy5gnaUIqysqKMu+aqGMFWHmK9FtmBCWcYbgzKGXHMXhiCAf39eHAyRGbbCu62maqsldUdtYr67rKNNVqJRa8yPQKvFK9R2o5Rs/yKqfiA9W1tQHTYfZLTK8a0VdKCzbpZW3CSCLyLP86WL4UX5npTuvbmXjteiDB921/7eFlgtwb7Ymg35nCereQrh96N2ictwii8fp8uOyTXpcTvkOEdGG6nJgp/pBCur6IfCxeDvn5qtPlwkxxh3Rl6XJipvhDCulcdDkxU/whXXm6nJgp/uuBDBrfkehifwEnUtRWTJWjJN6rVvKolfOolgoYPN2PrW9swvef/AF++OMf49kf/Rjb3tyMoaERFCtVlCplm9CKaVVQTVM2WrNU5UiupoVHPLgNa6o2V8KBZixK0ooq3tSRrlrdVI1UUcxMou/wEWxavx4/efZZPP/ii1j/2qt4c9MWHDx8DMPjkyiUNNnjJnkScc32aMJOaSmuKColDWYZJxOs1kocmIoKKFdyyEzkkS9oakjbqEQwMjKKvbt346WXXsTGTZswPl5EpVxCf+8JvL7+DXzjW9/H//za3+PV11/H0RPHsInlfumlV7B163YM9A9beSKaBGK5YyovXTRRokm4qiYOYyp0hekXUWZ9Flmfqi9NEKrsvMF60cRKhOGBeFR7BlZQoJ8yyzc2MsS0NrIunsaGN97CZIZByvTDNOIxTUvSH+OuMozSU2WWWP6SJq1qijPuVprZ5JjSqU/Ia6KM/hW+UisyXJXZiTK/zJP8lujOwtSiWsnCo8IwDbWrvpSpVYDCTLx2vdD5cKH7jWiMO6T3Hl1JzOpJrxAXjyvNKCFCXHdQlwi7xaxBKKNChAgRIsR7Gpp7KQOxahRNSCBNqnCk5SiBciSFyUgaJ6PNGEi1I4ZDiAxswJnNr2PHU69g07ObsffUEEY0yXX4BM5s24H9/aM4iDiGkmnq0SRjjCARG0A03g8kxlCLF5go3UppJIvNSOkVuljFXvErRBLIk6qJBIqVGEaiJYzGciidOoahZ57D61//Jh5/dj0ODg5g956X8cIL38RXv/0Y/vaZzdh8PIuxCUaV10uLvWhKnEQiWkStkka1HEetFtUbjDYpFIlmeX4SleIOnDy8Hk98eyMO7hpDcbKL/hegOd6NuS3NmN+VRMfcKBKteaTyvH9gNw7sGcHWoZuQ63k/bv3Q+7Hy7pvR1DMfNdZRgnXVlkizHiuIlU4jUulDKlJCPFJBIV7DaFMMY01RZCMjiEaH0BKfQEcii5ZkVTuko6gMxuKkJEqs+wqSDFtGc2wUzZExNNUWsVzLUKgN48TIq3jr0PPYcfgwJqsRtFda0VSpIVIbRS02BCQnEU3XEEuzBVjFbYkoOhNxtLF+4zWmpZVtzGsyxvyRCWrROEoxpqk5RzBsdBzxSo78MQmUNFuYQimaZnvwrsyjapF5yzIsjwwfrTERzZ+Jp0KEuMHhV4tdzKqxc/m5JpNeV2M2L8TMCOs+RIgQVxOhvAkRIkSIEDcWpPc8nQ0NvOIclE3odfFCHpnRUTz/zLP44Q9/hEKhgF/5whfsAy8/+zM/gxUrV8Jt8F+1qMocy+nVSTcbInIri+zVc02OWJIuTT/s05XGgFWS9o6KaQpmYhIHDx3Gjh177OMyd911J+6+5x7bHHr//v148skf4PnnX8b4eA3JNOMo632/AsZHhnHs6DEc3H8IJ070o/fkOLKlPAq1IvOexdFDB/HYY4/hP/2n/4Snn34GBw/249SpQYyPTaC9vcO+unbXXXdZmQonTuDk/gO8N44lS5bg/Y8+itVr1iCXz2H58hX4xCc+iYceehidHR31WuRvJoPB4ydwmOEOHj6IE/0nMZodsXLJ1pgcGsIJ5n/v7u3Ye3APThw/aavOtEeW5r9UTVrZVWS99/cPWFlFg4NDtmG2Nk5vaW2G7Y+thmLd5nJZDA0P4cjRI9i2/S0cOHAQIyPjqJSrDKP4GG+5Ym03PjqGIeaht7cXJ0+OMd4SsjmmVylgcGQAx48fw/59+3Bo/wDO9JbAqH1zoVzS6r0bb4wW2oghZoJb9Tjz5NWl4ppMejUiZPgQIUKECBEiRIgQId47kH1/I9n45ThQTPIY0ytqBQ6ySHolzyiPOLSSJ49UpIoevXZYSWN8IIOxoTIq5W60dtyKuYvuxdzFqzHvwdux/P1346YVPVjaFMGcKtBciiBWTTClTg4I21GstSg2lKNMWBM1mgcrjiBaGEa5UkCRVa99rYpaHRXPoB2TaK3kGSaOwVg7RlJLkVvwMaRv+Qg+dUcEn78/gk/d1IMFhShO7t+Lk5ljGIxrl6kWjPXlsHPbVjzz3BP4zvf+Ad/6zhPYsGMXzozHMVnqQWFoEJm9L+DMzpfQO1zEC3tOYMtzf4etP/wKnn/mOTy96Th2HctivH8cpYkB9B3ZhaN7t+LA8f3YPXAK248fxM71r2DTC89g0/ad2HfiNIYzE6iwDmta9VRoReFkDm9tWY8f/Phb+F/f+z6efmkXjpxiOSciyA1O4sCOvXj5mRfw9Le/i+cf+xae+9EP8cPtAzharCHDqonHJpEo9TOeIzj48nP4zjd+jO98+1ls3HwEZ0ajyLBOxhJxTCQ1SzgI5McwcawPxzftweYfP4dnv/sP+OH3/xYvHxrB/kwVmcgER9IDKGWGMXZ0Eke3n8LmrXvx9Gtv4KmXX8WW/UcwlsuiWuhH767NeP7J7+Opb/0I33ryBXz7lS3YuPcUsmNlJMQtyTLyUe3mFWN5Uxz1k5HcvOZ1jwvJgXAeIMS7wcXyzzWf9PIZDRn+8kD12FiXl3umNESIECEuBaGcDxEiRIgQ71XUpOJINW2aDu1pJdL6HZHO9V3EGhL8jclvLIloJI6mZAsSiRZMTJRx6Eg/RsfoozWN+UuXoLuzA+movvBYsXkt7SFV1TtzjEUzXZFIDBHt/aT4lKxuaX8oXmvxl/aMEiKRMuMoIVYu2/5T1XgK0eYONHUvQcucTvTMY3pdMcxnuh3JJkSqNeTKWeQjJWSGRrBv5x68tXUrjh07hEx2Aqf7zmDbjp3Y+OYOnD6TRSFTQDU3CmhPraZWjGaLGBk4hdH+Ezh+7Bje2nUAG7fswJ6du5GdHEO5mEcpn0Uml8HA2AiOHD+GE0cP49jhQ9i48U1s3LwFh44ewXhmzNI78dZuvPT0i9jy5kYcOXoIp0734fipAaY9jJGhUZw+0YveEycxPDiEydExDPf1Yc/uXXhxwxYcPJHH4NgkJjL0d+wgtrzyEt54+SWcPN6Lvr4B7D9wBLv3HkLvwCCqtukXK7KUw5GD+/Hq8y/i5edexN4duzDY14tDB/bgh8++jNfe3IcTZ3oxmR3B0EA/tr35Fn7wvafw6quvY8eu3TjJ9MczOeQKeYyNDKL3+FH0nz6N7EQOx3vPYMPWt/Dy+jds1VyukLM21O5fmueaakQhHMKFuMHh5zH86i9//U7HFOpVswrhoChEiBAhQoQIESJEiOsPN7Idr0GVJrU0XRGxWShSla6kKuLQnlKRWhzpagQJvauYnIum+euw+Na16FiUQm/vNrzy7b/G5mefRO+ZMWRLiimOKP3bPFqUP5EKKqUC8pkJZDLjNiE0yeNIZhTj2VGUckUUJwvITOrVuiqK5Qiq9jXFFEr6i5V4VkE7o2ovF9GeP4XIwEmc7K9hz8kiDk4A+c55WHTTTVjaMo6WzHEc27kT2zZswpG+MSQXrcFd73sfHr2tDeXeN/D8cxtx+NgoyvEetLEscxevRUtXGkuXdGPp3fdg1b134dZlnVhe7kXp2Ha81VfCaKob7QvnoGtRFzrm9qC9ex565i3AXasX4uZlPchPZnD88HH0nTqBbGYYo2NDePW11/GTlzfgdDaKxWsfwP3/f/b+A8iS60wTxb7Mm9dW3fLetvcejUbDdgOgA0jODLnzZrict7PxJmIUq4lQSIrQk0ZSvKfdlUIR2tkXoZjdt/uk2R3FzuxYDsmhAQkQhG+49r67vOvy9tb1N53+7+TN7tuFagAkQaAand+tvzLzePOf/5zz58lzjjyGPZ3tSJgl5FZNZHJSpjWt2LL/II4/egSP7e7C1piJ/sFRXLg0ivmFcSwtT+DStWG8cmoM06tJ7HzkIex55AAa4xGUpqZQmJ1HWDe8UxdTY+g/+wpeuTKCi6sJxLp24MnHDuCRgzswduUyTr/2Fi5fGcTkUk59ojl/TfL28k9xM1WA1tKD7Xt7sW1zNZIGYGfiiBuStn3HcPTkU9jXW4eq1BBGr53G2wOjGMvz1Mao8IkmVUzFqClkSYVzoq8unytQRgTz/QC/Cn4Z/tlwSq8AnyyCVV4BHlyQ9yspQIAAAQIECPDrwoM+kfXX5/Cqqf9UeImJkO1GPMUGwog6LuJqk61mxDr2Y/sjR7DjkV5UJ1cwfeYFvP/Cf8bPfv4O3r5wHdMzi7CL3NicgbpwnRLSqSUMD/bj8uWLOH/xHM5dOofTF87g/NWzuHnxGq6cuYjLF26gf+AW5hfSKJpUo8RghhyYBpVeFpIlSc3qEorD72HgjdfxwouX8ZO3RnFp3gS6NmHXkQPYWZ9BaOoyrp09h4FrN7FqRRHfchi9Bw7hyZ0h1OWu4NKFQUzcysKKtKGu+zA6Nx1AfZ2BXTs7sfvkMzj09Ak8fXgzTraY6DBnMeE0I1ffjZqeNrRuaUFrTwc6Nu3A/kMP4fmnDuHkQ9vR0dQMt+SimEujVFjB/OwMTl28golUHjWbD+Hhk9/Ac1/+Gr5w9BB2NDYiEa5BsrYHndsOYtfDj+Dho/vw1PZmHG0KYSWTw/X+QaSWx7C4NIYrA5O4OKKjcfPTeOqbv4Env/YMHtmzEzuqk2iQ+jK0MKyCA2u+DxOXX8OknYS76wvY+fTX8PWvPo5vfv0k2qIGJm5ewdWrwxiZSyOfLyK+NIvQ3BRiO6TcnnoWj5w4iH27atBaHUZNqBtbe45h9yNPY8+jj+BAdzU2YRbm0gguzq9g1Iyrz1RhhxBybOGhovBPUbGPSzYKECDAr4xPvSlVKmEqO8dAOfPrRVC+AR4sBPy+kRC80QsQIMAniWBME+B+A3tB1ROSdYX0UEhtLh+ORtC7ZRO+8KUv4He/9bs48dSTsEpF/OV//jP87V/8Bc6cvYS55TSK4th2HbErYWZ6Eu+/9zZe+NGP8A/f+Qeh7+L73/s+fvCPP8Df/8N38dd/87f43ve/hzfeeAsD/WPc/52NBtzEntEzXssG0rk8BkZH8fJrr+E7f/PXOPvOu3Ak7i2bWrF9RwtCiQQGhwbVpve5XEFt3j43vYjz527iWt8g8qYjwVoo5G2YJmCEI6iqSqIqnkC1+I3F4ghH4kgka1FdU49QJCpl4CAalvwbhtgnEI9XIV5VhZraWrkmERWzmmQ1EvEYDF1DPpvB1OQtzM0vSJp2Yu++fejoqENDXQztbU3Ysrlbrg3oam9ANB7G3MIC+q/dwMCVa5iam4cp+TGLBZTyeaws8lPEeUmzjV17dqG1vRX1dQ3YuXMHDh0+iN7eblU5paKL1YUVzM0torunBwcP7UNXTye0cBSxunocOrgX0YihNsCfmZnDajoLPRpF9+bNePSRR7B/dzdqkzHoUubhcAj1DbVoqq+X8BZw9fpNDAwNYGVlEY5twi6Z4JZlprglOfwu1f9OVtKih1hjAQIE+FXxqSq91g5S+OyTj400kFmbto0MP52VaeZEk8TnYNIZ4EGAz/9eE+C/SuJOCZWkHAX4FODLJP+6Hvy6C7BxwFPBdF2/XS9+f+I/36u+gv4mwK8Tlfzo86SPe/FkgE8P69UBzT6OXLjf64+fIGqO5NMNget1uCk5/9RFjL1duMQNxx+WBTNiwYo40GoNNG9twfGnjuC/+71v4v/0B7+P3z3Ui9zps3j1dB9+PlvAddvAEk9fTABtCRe9dRFsaevA9q5d2N2zB3t796KnbRMae7agbftudG3ajM72VjTX16BWd1AdshCT2MNuGJZdBUtrhFHfi8Sh/Tj0O7+N/+3zX8dvbt2BVieD0tI03EwJMLMwrSzmFwvIFyKw0w4yY/MY7pvAm8smbtV144lHN2N3r45kXPqMUBKWJLDKcVEt5WDYcbjhZqSjbViItiIbb0atkUFEgtZsHZophaLHYMdqUTSqxa+kqaoLcd1CtZ5DUs8j7qTg5BaQsyNo6tiFRHMjrKjkQQrbkDzFYynEozdRGPsx/uFHf4n/8Fd/i7/42Sm8NDSDC0sFxLU8YkKJ5Szi81lUmUXU1DuItAIpdwUL7iJqmsNo66hCMmlL/S1JPZqYmY3AMjtQ1dyMqvY4jNqYVF4DdCeOnsY8tjREUEibWFkKI4MGpJoaUerqxKa6BtTrIVShKPlfBXKzUmZX8dJf/SX+/X/6K/zgxVMYHbmJXHoEoeIi2lwDdQUHORSwFImKr6TwRq0UphSoZgkvFclanyuwnQeyOsC94POG37+H+IJAxqN+n0/4POTTx0GwaDLAhsFaBv64TPzrwGcZd4AAAQIECBAgQIDPIbhflGnJDMybglmOJWNOb0IXq65G15YtOPbMM3jyyacQj8UxPT2N+YVFte4nGvLGp/UNjXjk0eP44he/hC8JPfvss3jm6WfU9Utf+jKee/45PCNhPPTQQ+jp6UIkAuQKOWSKGQaASDisKB6LYfv2bfjGN76Ir377n+LEs8/AkAnmwMAgpqem1N5WjU1N0CVtoZCOZLIaHR0d2LVzBw7s34+TJ0/gxIkT2LatG1U1cbjizrZsFIslhCV8+tM1XcL0VH35XA6WacKg9k/smBfLssR9UREntiEjpPy5cm/ZNmy5Oo7nLrWyArNUUv5CIQ1hXcpSwkQmg9dffx3vvPuuWn3V3NyCffv2Srq2qXTYEk4sGkM8HldxrK6mUcjnUaVXIa7FkUtnkVpNoVAoSLJ0KZsIYlI2tsMVbKaQLf6kBqRsXMNAUdKQTqcRjUYRTyRgSJrVBF3CpnumT5efK/4WpP7ef+cdvPDCj+FIPff29Eqd9KBR6pBpY1ilkuRdfmo6783ppZ5Ikj9JT4AAAX51BC0pwGcOdg6k9fBhdr8s/DA/jD5ZqJ7rY5C/AuleRDcBPh7WlmdlOftY+xwgQIAAHw/r9RsfRQECBPicozyscKS923JDKumOItcpQrNy0FACoprMwByE7RuI5C+juDSLlXkXS6kklq02pN1mROsaEGuKoMooIl7MIcx9vSR4x41Bi/ciUb8H3Z1bsWNzD7Zu6UXvTtJWbN62A1u378KOLV3obatGXUJH2NARNaoQCsVh2TpKbhFmaAVuqAij2A0zZcDoyKJ5fwhbN9Ujlsrh5vt9GF/chFxoF7q7q9DR5qCjox7btm/H/v178cihQzhx/Dj2HdmB+laGLbnld3pURrkGCtmSUhTlLAOZUkHiXIERsxANR2BJEQCWxG8homlIuhEkNB2FxBxWjVtI2ybyEoaFZujGDtTWdGFTbB7W5GvQB8aRWCigWADG7DBGtARGB+bQN7SIeE03Dhx9FidPPIHHD7VjT1cUCaMRhlONmXAUi/X1iFTXojVXRGR4ErcwgwUUMLNQxMykg+XVBAqhepQiLpL1y0gkJc7RadhXU3CmllC0hlAwx3BzvBuL7j4kuqpR1ZWGnkhDK4ZgZ2KIaabEByFhhKKJDDe5X55H0cnjoS8+hkeeewqP7NqDg7WtaI0lUaiKwaqJokoLoYZHHdji2WYfo8HSw7A1aggDBAjwqyJQegX4zOEvVbwXPsr+F8EvMvH4dCcpn2ZcDwZYoj7dXb5BWQcIEODTR6D8ChDgwYE//lBfO6phrCM3tnelmWNDt1YxN9WPt998A//4/Rfwve+/iB/99E384Eev4icvvoSCmUdXZyt62huQjHtjYY1KEKMKeoT7X1UhEeMKJqGqOBLVVYjF44gnqlDN56gBg59X0h8MhELiVwvBtErI5FJIra4gl3Fg8Qu6hIOmTY3YuWsb9JKJN15+FYMjS2jt3I5jxw4hWR3G6OgQzl+4hJs3+9HfdxPnzp7BlavXMLeYQkmmlIakJSpkiv+f//wVvPfeZfQNjGJ6dgbpzDJKkh+upuICJpYBV28VcnkUs3lY4sfWCzCRQ65YwFJqFal0UfJbhfb2HuzZ2oHF6QG89eLP8NPvv4Tvfu8n+N5Pf4YL/UNIp/KwHR2mrWNe0jIyOIThGxcxPnQTC3PLksciSiED8cYmtLZ3oBohnH/rFP76e3+NH73yE7xx6l1cvTKA6WlxW7LhhjTUdDegq7cZtwaH8dZPX8NP//GH+Mcf/C1+8MO/x6WrU4jXdmHTjs1o665HKOwik8piZSkNXTIX1ly1wo2fZYWNMHRdk7wXML0wi2sDN9B//RpmR8eRXlpBWvJaELYwXB1hKRRx6vEHV45JmbKoAny+EYwLPh0ESq8ADwx+GaGysQRRIBQ/PlhWPt39P0CAAAECBAgQ4BMHhxnUabkaQq6OkJpmUXkhpBlw9Qgc3UBJ0xVRubGwvIzLVy7i9ddexMs//S5+/tPv4Mc//Ae8euYqnOpm7Nrci10tdWiIcD8wbzWVpWtwDAkz5KrVUq5uShwmNO4BRS2JDYlfQ1ijqotw4Ti2pCsuKUrADsdgJ+IwqsOojaSR0C04oVaEa7ejo7sX9dXA/PQIZubmUdvUjh179qOqvhFTE4M48+ZP8NYrP8WLr72HH770Jt5/5yxmJhdhWmEY8QbUJGvRnsxh8PxP8DZPkRyYxlyqIGk2EIknJC6eIynJ5P5fsSZEYxrqjDkk9UUxjCGkVSGeMBCOurCZHyOMptZOHDrwMKLhKty8chqv/+wF/OTHP8Err72N/sFJFCNNaO7ciSrTxszli3jnzXfx8/NjuHQrDc2ZRSJaQEyvR01iEzp6elDX5eLa0Cm8/Rcv4fT338WZK2MYyzvQIjG0SJ3Umjqi7TvQtueYlOU8Jm7+DO+8/iK+98I5/MNPzmOpuIiezW042NON7dU1qOXL+bCGWFLKVwqcSk5Lyto16hCvqUd9Uw3i1SHcPC9p+/mreOtyH66liigYEbSGTCTNjKpbdcyAsIUbEtag4kzqVIeUQYDPLfx5ZqD4+vUjUHoF2BDgaq61K7oqzSgMKukXxa8iTH4Vvx7o/8Pp4/02Fn7Zuvj0sLaM7/z3iPCvAQIECBAgQIAAvwKocBLSHX7iF0JYqTHKSi89DDcUhaVHUNRCKHJjK8NAJFGF2vok6msjqI4WEbap/FlBw9YD2Hn8CziwbSs2J8KocSxE+EmgyxVRLmzu72U4ntJLK4pNQaIuQmMauGWYXA0Z4hgyTtMlBbrGVWZVQklEG1rRdWgfjj39CI7tbURj1IajdcCKbEVzSzuOHujBY8f2oaq2Tm1MX93aji179mH71nY0J3IwM9NYymkohGoQ1qOISDw6ojCiDWhvb8cXj7bgyCYddjiMjJuAkWxBx5bt2LV/P/ZvbkctZ5+RJtR2H8Defdvw+J4YdrU7MLRaJGLN2LWjF4eO7MIm7hVWm0R1TSP27DuGY0eexK7eBtTHLcTCOuKJekRiTdAatmHX4ZM4umkLtkZDkuc4Vqt3ItJ7FMePtuPQvlY013SjOrYJ3Vt6se+pFrRt1bE5U4/OTCuSbfvQJWX90GNP4ZHOdrQ6UmLJHjTtexLHHurA0e0uWusjMPVtyEe2Y/ex7dh/pBu7m+uwSQujM57A5j3b8PBTj6A6GVGrtEwnIXVUj3h9M3p39OChR/agzogiZjkItfYgeehxbD/2GJ7Y1obNsRIiGj9ftcWvjFQ59ZH60lESDjLlIcDnEWvnUP686sMowC8PEbverM/6hAqyskKosODSVUOEOvHnf/7neOGFF7B9+3b88R//MWpra5U5/fgKDv9+I8DPy0ZJz4fBL7fK8uc9N2/k8trh4WH86Z/+KcbGxvDcc8/hD//wD5U57Xk610Yrc6IyTZXmPj5umtfz+1Hw/fhx/GrlwxHIh+PjpZFt5LPXU69N60bhHeJO2riTRnlTUEKl8U46pSTVfw+B7v/XDb9eeOXmr1evXlWbzlIefetb38Lx48fVBrO0Jz9tJJ56UMG6YP/A/pv9+MDAAN555x1cv34dzc3N+L3f+z01uWE/EtTbveHzPhGUz0fD5yX/SnDjaf85m83i93//99X48dvf/jYee+wxJTuISl4M8NlhbR3wWW1QLvVDfPe731XzAdblH/3RH+F3fud3lIzhWJSg3/u1Dl3qJ6TJc5UOmF3JUqE81uBMiDnkup1CWSwktUsw83mkFlwsL1lIZwrImybyiMBo2IG6unpsSkZQR61SSMaSMbUWCLYbkTgYHsc5lox4LJiuyGsxCTsJcaAslfLEdThZlrmAoXsrxFypi2IWhaV5LK8WYNZvQWNjQoJegiHptnJhZFYsZAsmwvW10r4iSOqzsFYWMLVkYnK5iHQ2A606gnhVFWriPWhpqUN9tYGonUdpdR7zE+NYWV7CrfpHEE42YltiGZ2hWeTsEGYTu9FYq6HGGoeVWcayWY802hCLAN018ypfY3NRZM0wIokYqqujSGgWaufHYc7MYHKpiFnHwEp1PdymNrQ0NqC9ZKLWsJGen0dK0pnVirBrDERicSmfRiTi9UhU8zNQDTF7Fu7iNUyM3sJMehvCdRJ3shZGJIqwEUGiKoymJhcxbRK51TQWZ7ISZgEZiSMt5W0aUdTVP4W2dqAjMY8EsjAzUqfLEZimgeKOFlXjVC/GHRMhaxVOdhYrk7dwqVivNshvsQwkHA02N8tvaUBTY43UEVd76VLNUegON8YXTgnlEeJMXWL5PIEygUSwrVM+fOc738Grr76qyuf555/HyZMn1T3t7meZcC/4+f9F8Xkrh/XAOieYVx4MMTIygj/5kz+RdtmkDs44fPiwyKzG2/ollqXffxB8riwno3x/x0WAAJ8hKgWgj/XMflX8ouF90vHfE2yPH4c+Y3xq5fGJQPhH/XjL/3fS7t35z3fMAwQIEOCThD9YfxAGqgECPOgwwy6KEVuupsywCjK8KCAmtySuwOJaK+quauSZlLUPohQ5jmTXUfQcPIq9xx7DYw8/gy8++QU8vbsFh7uiqK4PIRfXkQsbcNwobDsKVyvBQUnC4ws+A4adQDxfg3CpWiIowI1kYBt5WKEiHMNCiBNCia/k6ihqOqxYFPGONrTv2oLW1ggXnMG1GuA6jXDjESTaI2jbnERblY1acwVuuBV2/U50btuPx449jGdOPImjxx/FHq7cao+hI2whKhNVy6iCU9+DhkMPYdvTX8JXNhn4Qv0KOuuqYbYcQLh9N3pqi4gjhwy6YNccQnNzL7Y1RdFeFUHJ7IJld6G3qRp728PYVGejxijA0F04TVsRPvg42p59BjuePoonjrXjK9stHGlYRHtbGEZDGI2727D50T3Yc2Qf9vdsx77Ordi/qR1b63XUV1kwQiVYEcljx7PofPSf4+EvP44jj2zFwT1h7N+Sx66OFHqSK4ibRRStdkRr9qBzx1HsfljcPfo0njj+RXzp+FN4YouDbVUmEprkF41wks3QNzcjuqMJ7VLObRbU6re8FhJKIhTrQeP2J/DYgYM4sG0nuvbtRPPhXWjd3YPWxjjCUo/JbBzxUhy6+HHCMvFX83m+viXXBPi84/6aX92fCJReAT5zVDZ03vvk45MWBJVx3Is+SUiIH/nj38eiDYj1ym8tBQgQIMDnCevJufUoQIAAAdaF46pN5qmPovJKrcAyDOjRKAWMGvO5ltjYFrXnMNRmUfJX/njAUeoQ8Sc/9VK0Ykbnix6t/FMGtrf6nauJ4PA0SS8ghmCLPdNC3TydMkyXEfEhHoNpWeWVeuW9wSSdKl7CiKiLJ/PowvNfdEtwmJd4Ao64kax4pD7XcxHiju3yZ9kubIu+uMITKJXElqvT5MYx6ZbbZXEzeHErj0x2xIjCcHQ4RXUMpGRNyk4ciC+V7lCYn41ylZcGq1CQALiBv65WTXGnNWYtJHHzgEVTipfxqoSzAHTm07slSpIGm4cOiDHLyKYOiumiJ0k7nSmlItPOYylZD2JoSyS0M2hXLthIOIJIJKJWpZimi0KJKSbEXpWvpsLnAY5MOzfDD/D5RuVYwb//MArwyyNoTRWgaOUBJhaloUOBZsMSQUVzlwLOLIpwLiAvv4JbhFukZFJyTAlOCjhHxDlJTD+CPn24mnRtugVbYwenU1ZDd01oaj22Jali92lLfr0fOxZ10Az7FCkY13LENC+3ORHK7DAZqDRC8WuJKe14VQWiSPUMyr4k93xSHbQrcTFwFrE4t6WMLZeHOIsdl4RL2DpPTzFtlOS5KGQyLVynrRKTgebkvMoSKkp43M2A772YE3beMKWTK4obKy9uJY/smEzpUC0dK9LZZNjhMG2aCUt3UJDnoqRDlzjUvgdaUcoqpwga39ZJyHJLKklli60Qr94zbLFwCiodOTEXH5D+zOu4ZLDgkXRhEr8jhkVVViX1rBWkGUraJDLxyXrRpTw84hf97AE16ek1KQ+VfWEvNUgR4sBAbsQv/+UVsYYYus0EiJFTZDpZr/Isf/QP4WO4WVqqelAZEUv+pLK4Hl8GISxpBynxwFOoGY8t9ViSn5Sa2Ei9OZo4zSGvZSSvTKN02EIpKcuMkGtL+VtZKb7S7UOLVPy8SqRMGbmnJHXG9JXk3uMUVrgQ26GkkUd9M05yKb2rIJgXOiXRrUTgOh4fs91yz4yCDG50JyxpCAufsGwyUq7c80Lcsy6kjB2pc4Zqi7ntSAEzs8y8YnApY0kV0+nKAM4bjQgxLqaU6RZnahDERKn0sO14HEniZwdeexC7j0DQoW10kEsLUqfkRq/p5OQfm5riTLYnjsppKWQK3xTFvVqqrdhJHAqPeo0hwKcONi+vWZfbI6Uoew62b6kX1X5pLheRqcpM9S8OVsQsTQvWnZDGQHjPCSDlrwgByh2S4gWRF5qyl1syCuMj8Zg0kYsMm+wgXYPEJfJc/Ct5zrRxZlikbCb/+GK/IJQWXstBukeRY2KobCifKDfVNJWGAT5tsNgr6YMGHwLaq0pX5PWEwjCqT5M/4SGXHTk5QTGSVL4ijgG8sQbJ6yvpj2GQEz4q3gC/DvD0vYiM2wy5A6IyABTiih0h6j54S12P2oA+7MKQth8W+RF2QkLiW64cB5NctedXRCl8YjKWUSf7SRhhCSQsv4iETwoxVJE78kALFa+uJSQVtAvLvdhTWxMzxImLiIwzDEmXJm40N4q4a4AfCKtPMmknv7ATE7sIbF1IwghJ+LrYKSWMwS1RXFTL2KmK46ewjFWjjEMTd3TNPEma3ZjYxWBHJD0hHTHxE5NkRt04wmIXlbSEhc9DYq7JOFwXMgzxGxZZxg3/w1XiLyFuJOcSN/cx4yZlKny51UPVUkYt8lQn6ZHxNc0kLyFJty5+xLHYU4loSHj0x9VXmoo3KvMgxh0T3zGJV5MScPUaqZcaOBIn91/jQQCajNcNKsukNLlCj/ujRSQiJ8x6kvGjpNPVWFZhyZeOau7bJnGRopKmuLgJU1sWYVl4ysyQIolf3MSkOCMy9g+J7HeYb4nEEN6ISDkxTqaLBw8E+PRBGer9KE+9MT/pjgwuy1heKkiq924zAWenFmdmtshxduoi7vlZMjUMwkVylRCFF/LCE1mZp3Neyvk6dNrLWELcCZsI0XU5DgWmiSMUzjxlHsqJ/e2k8V9FevlYJv/2QYMUYQAfZADFTIojPOKz4h81aSFzecoGTr/V5wrijFYeA3q2ni8arEefIdiquL5aBDbfTTA1Wnli76ev8qeUCj4xj9KYvPxxwO8Fd8eB8iE/Drj4TPjm3vNtUxYWA+efEN+ysJ0SatDOAuWgXzobL3VMq5Byw7tyAy5fHLFQdcIr00mHasBI3/Tkkwd643aflkw+bTXx8MQY4+EbLOVWOm5PveLZKDNvTCpuPPcqPgarCkLcyICTSiGvhORRzMkingMhBiOGTB/L0aQSxfLsbn/+Ip0slTDKo5A6svi2okUiU2HII+PhYJhmCrwyVm86zjT4VUsntFXqJI6JlZc77tWtQpkr+Cz+mE8Ov+lKwa8z3sp/xR+STFsTYSyuHJmF+ZM7Rs1bNQpR/MbwxIrEcqQDlRBvcM4s84n/Wet84+n5EirXpTep86qBaVLevSDKN16xsQ7VJFICNYUh7AL9c4qqSl3994L2eMorH9+/b1CO0yZ/lBXZvmNmhD7EnmyqikVIpYNXVXUMkb6k1IUvVB3SLsB9DlayV9F37vyr3Cl+p4E8CXOU+KZbeEDZ0eFtHuJDgM8Eqh68W+9GSTOpFrmvtPPrSto57criXz178liuJPYZUteayAr2Bz4vKFnCwMqGyqm6lh9IAk/Ul+V/JWhf7gO9kCQexUtMr4pSoqaCnTLKC4u40yfcDZrfyy7AJw2vxjxaAzFSbHWXle/Wq20qutiPOcJnrGPL9hSbHL+55DdV314A5AqSz1NK1pTtAnz6YCumqoI/b4olxFu287K9aurKSvNdKAUHVSvK322H9CvmJM/GI+WEZt7vth8/MAmHpCny7BVXiBvfiefPs/dcipmSQ55dSFO7S8mDUDkNlWnjhSdDUhHneWJaeeuqFVQh+VF5RnNXwqD/kDgxJM8qbI0uyvEySIYhqaR/XSb+DMwVN5pameWlS/G22DE3dKJ860p1RhfiR8wkk36p0qUqQ0mDZ8q4PTKYxjIZdCJp0rSIuA8LeflW5SEhhSrKnwpLksqMCpvlUy5HeaaCzJfnKi6mSa5u2S29Mv1euF55qLAlP9zAXh68OJQb5apMAT4LkOfIjXfkqk+Efy1DHinXWWuVUH2vyHbOPW7PP9h/c1UgZT75Q7nzegDKc7p2pB9QL9b4IoNXmpc7Dl4UKZ/0RdkvV++WFhXgg3J8+/KgQppXAB9cV8MjY71C4X+yLhnNhisCzglRKFLIU/MvbKPWxnJALAypycBTzLhKx9moAkoxvKSZdBtMq+T1rlbgiWSeEKPy7/UuZXMuaRYRzQGWDL448WfD49sprqjR1bsUr3GrIB0R22yAUjY0o7rMFuHvqLBzIvG52kfcc3UVnQnxjYxlSFmGJCZbOielPbJhalQqMV1RcSXEKhJiJyM1o96ccOUa05yXTq5ghGFTKy7elRyQBFEshNTb8aJ4dVQ+Qo6JiF2Ua0m9MTUlPHIC33Lx7Y3XgUqo0h/akj3VYUqm6cpbBSRxOmJpSRcvE5Cwy/VFSuWj4jblyZbOzg5Rey9xS/74vk29naPKXy+iECogp+VhCi+JM9BZiDwlA11TesCS8J4pPOjyVRPfiEmsTJWwm4rD5Y0liRNiuOyi+cc9AfhGkSoftTKBxPLQDVjSwVvSWTshSashRI0YFUbiviRB8a0D34rFeUSQlL1auSDxqo5Y8s8VgrpTkDxHJM98sygFHCrKOKCEsAzWXctUq+cKzLskhtbkFUuC48I2CmuWv846UOES3p3LTVjJEh5zCcsyzypLvt5WckKeKEkeqDwUA3HPNkjlnlfqJSkJb3WYsKeXTh6HLXzK0lMDDMkXTz3iZIEDD8ZA/iSpdsLClZDY6jmwUUpINeLxpsDlbka8SVh8K0PeknrjwI3lxCGPxrOnVbujwwD3MzxOZbslt5CLHISlvegyINGoCKGSVe6LIq8sYaGQNEDFb2JGhataZevzV4ANgQ80SzZvXqSt+2Bds6fkVbV99jOq32ffJXzBfkZIWEHqW6yks6Gui2KMso68AK28VFgccTJni1zgKi/GR3nHfsZW/ZzINF34xWCfQV4j3zEwkeqU7+xnJTwvefQs/0W++BRgo4E8Q/Kg7u48lnHHjRpZSH/uvWglr9FUzKSuZZSiRi5qtCR9Fkl6cEWKF4TY83gvCgNsZNwlX+S+kj4r+Erxj0xLmbk4zvQUZWvc+Wbla/lWcehd+GgDD/S8Lmh+L7t18HGcihs/P5VXnyqfPy5+mZcNv0j4AX6dYD2QVCdepkpU1K1Y3ak2mlMuc55IOS4yWcaDHElwXsY5CccIXOulpjmKvHkd57O6DBx0mSxpMv9yxLF6iS/hFWSO4b9IVTFz7ueKDwlUk6vFORDHJewlynN0zm7UDEpNnvzewacHCyzfAGXIEFSmtjJZ5mBCTWz4hoFHyAqryQCU36Tz9LyIMFJMDUiEqH3VxV4pZPgulioxDo83HkRMS6NQ7xRUw/QaJyfkPhsw30oVoUidHEJlB82lbfDzQpniyS2VK5zgCamBF71JWbkRGEJUJlCJpfYDkBmB+jZfypHLO002XCpaZOjmuik47qo44aeEqukrt6buohCxUTJsGErpxWBKYs5PxiTRTlwo6iVdqkmmlUqFxOXKEREImltC1jCEpDbVZITpITEnzFle6jSvaios8RlmEeHCKsJWDjkplLwEykXPcBNCUUmnhCF+S2JkStRUgUREWhmc+FBRxYmMSY1YXHjDQszNSthcvyrFJGXjK73MkOTfyMm9cIkbR5Th61kJI4uslsYK0sjZObX3aUhI4+d2Ek4xbCAXjkp5SDrCUuZSIErRx4kz88RlsLwpSZmYUYmbS9qlcAypL0mWyzOrFR8LZ4pflrPlhlFyY0otZIdKwgJUHAk5kkaZteWp9AppqHJ0xEvkGypzSBI/wcG4lRH2yEpZxCTfcRiSNttIIVdcQGZpEfl0CilpK6vivCj84vKTValLU8LmF51KZEsbCkkbCskE0uNCqvMMT9iT9cSDK/mTBKgWyUldWe8ndWKiFJLyZ4Gpgna9z2hDEo/wlO5kxY/wlpQfJ59UeMXsKvEfk2CFB1UvU5BrXspEphRMjtS1RaWEmmzyTR+XuEfFzmvXdkj88c2eXRB+l/JQS5CZFsoBPudVOVEZKqaSG+FOjXLD20PiowY/wUBnY4Nc6KpvSNjCpB0KRYQHqDhXn8Ra3sq+vPQJWZFHRiGCsLRJvkCwhE+pzDApC6i1CPDZ4a5m5vV3yqxszmaq614/SfDCGlO1pl6sUPZzCEqlu/zXRdJwz5mi8IL0DWzrXAnME9py4pufLGh6SuTJsgQifaG4d8pKLzWMkCvHqJT3JvsU4Z+S9GElfsekrBigyEUzJiJYra1QCw24WkKRyC1dOikl0u4hQ37RiVqAXxWU9evIezGi6e2qILNVOLM4/mCfIffqhZA4NEJR1YOzR8sL76heWOyobKcMIvkc6qniSUFdb3T4bdJvl5XPvtmnhfXGJuulxVu14rkVm/KPFhUkqPRbdnEbKiohZXPbHf3Q9m63ZUNlqtxXPpWdli+erWd1B8rojoGX+nv/+EcwTZXX9eCn3YdfhqqMKmgtfH+V/tczC/DZQmqi4leeO5dtPLBuhfh4F9FMZDLnBWoiQ+IL8Kj095yVWMg7JRRlLFjivFrmoZqQrkj8WCYiMkkyStLX89AKGXOaMl5Q/jhnkQGDxhftAs5PXdsQd1ykEVELRkyZO6uFJfzKRAYY/nY5fEl3R/HlK78eLAQjb4EvmLhskHuvKBlV5gUqSbxbueMqGNOEWSigmM2jVDTV4ON2YxBmV4tANiwjqcR9ZPJozTc4hoyqmScqoqySjVKeEzoOp8psQ+HMJ2m4IXGrliSzLMXKi0I8q0IR97SSnykTAioH+bMKOaUcmV9NqX2R2ADzuTRW0itYzeVQsiQuNVmQeikP4UgqfPlHvYsiCZNCQ9Wjipbra26nUiCplDBCIQdhg+nnag0JwyxCMoVSJqXSUUilUChZkHmL8IJMNORqyT9+BslPDby9NcSQvpUGg6lSqjwVixchC0xIpUfCEAYxRAjxx7QTTCf3f1NKQULC1iWv+bzkfWUFuVURVDLXsW7vK+WBvHjnsz9GwTho5tHtAhJYUk90SX5UdajSzSuD9PwxmYpvRZiyxNSeD3QhdsyKEoiMn6u2+CT1zPhtruDK57E0v4CSlJdpioBlfGKeWppH343reO/ceQyNjWN5eRHp9DKWlpaxvJRBqeCl3+YrDpUAiZMJrEijipbxMq+sCHHn16Yl5eR9NkQ36uL5VzxGA04PTanHPFZSK5iTNObyYiL1oJxLgTAvjInePFOWBdPANswSkVuWj1yVXldubMuWuKm0Y9mJ7xI7E+nGGLVKD80ZDsuQEw4qFtnxeHliGORV757uA9xvYL2RL1jX6pltgvVKblKDHDETNqR8K+SLmJubw/z0MkrZIkzLW/lDbiBnldkiwAYF+5O1oIkyZeWJYDCLJaRXM1haTmNpReThchbLC6si40wld8kX+XwJqysm8tmyDBVBRFlCxqG4jUZF1krfxK17vHcY3o93lIeKt9STkCewlF8mT0Su9+8u+mC6A2wwSDV+UOdNmcAKJWvZMieRsZYpfavwmCV9jeou6VGu9Op1OepfmQLcr/Db9VpFx3qKj/XMPkmoMYziq/Wh7PkTJ4poJuSNQWXUo+zvhnJDt7fJi+P2+Pc2/HLw8nmblI0yVHbqyXv0UDbzQbfqp9x79z7uxP0hVM4B79fCN6u8VrrjvTeHvNt8PdyVR6EAnyew7j3y5zVq1iE8XyoVsCjzpMnpSZnvrcqctyBzBa7Lkjm2zEmzWRlPLC7CMvlSzeMpNhVyCOV+iAtM1DzDG39yjuJ1HR4PMUbGyf/8U3QbAZ/xZeG/5M3/+C/V5RMFGzIFAE+pIC5cuICBgQE0NjbiiSeeQCwWU+ZEZcP/NAWAL5jUlenkho9MizKV9Ov8ZI+frU0jVLiFzNwEhq6P4PSFcQxWbYPeFEECFj+2U9+3h4Rx+W62ks/80Dz49598HtcrN+aL5b+8vIz33z+NlDSyHdu346GHDknli3s7JINt5lsGWlydJeniejem2cC0hLCC9EoBY6OzGL41gZzksK6uVp0woz7Zk1me98mh1LNZglMqohSSemU5ij0ngdQ26zJw4+ae/GM5GUs3MH3uB3jlZz/DP062I9S0Fb12P2auncL71+ZweS4JU0uiPpGThp6R8pUy1qjOMJCRsPmJXExIN7iyh5+oWbA0U70h56qsEGLlXHifI2nIiLCYEX7MIK21IKLFYRgT0J05TPVfxplXX8O50zdw2diDqvYqJEJUlEn5SR40nevIQogWFxDmxuzMhPrUkOUtT5IeVxcOkEfHlqsVl3C5zaiNsG4hL8St5aNSF1EqmLjKyiZpiOgp8ZfCxPB5vPfGj/HGqbMYXo5h075eVIWltKVOHH5TKfFrkn9Lk/JlWcjkhqsOdQpAFrKUqVpxJMXO/FPoGTLR5uaYnrCVAbTUA/nZlNlWSeqea9FsSUM4y7cEQhFJi5QlS0vmYgg7JbjFFSmzLJZitZKPCMLWCqz5Qdy8cB5//8JpzCxm0NjSCC1sYf7aaVz+0Xfxwks/x38aL+LGShHNI2cwf+UM3h+4hYurNoqJsLR/IEklJFctFPlmWvhHnqn8C4tUNyQvFjdGDUue+SlPMSJCX5N0r0ALFWDw81bbU4LqOldSSU2rdkvl6y1Jo3Qo1wbx2vffxQv/cB63jG2o7Uii1rCkHZvqE9ZsSPgiJPVhFxCScjJdbthqqLcsYYufcdpIG1Le3PhBxSTlrBeFpVckPpmE6I3IFWPCR1IXXMUjbjJ6XL2h5yeh7JTYHtmmOH1VqzEoGBgUL+u01QcFpVJJKYRGR0eRSqWwb98+dHV1IczTlQReuW2s8vH7Ca7u020uLwcKwnMFlc688G1BmvEkCtNDuHzpOr730nm88fo7uHbpXWQLWcyH2pGL18OIaKiSNhzh2zZpu2uxEfPN/oP9+NLSEiYmJjA/P4+qqiocOHAAyWRS2RMbsd4+FEyqEOuSMoh9hZLtYlbealH+RM5I30Z7aqW4KjWcm0Rp/paMAabxztlhnL96Ddf6L+DKjUsY6LshskDcJ7MiZxYx1jeKK6/ehCl9aLKnS2RancQQV/0JV1K7Wg5FKy3difQWInss9sESDz+ndqWfMG0d1bal+EXnG2Pp3zRDZKfwnup+RB6qzW7Z2/FNCctfssB683n2vqqTMvw0+9fKvJgyGfj+97+vxo/79+9Hd3f3bdlRyYufKZRWinxVRvmG6bo7ad4ERTKontjvhK1lkSMjuDyWx5U5FzOFEIrhamgxA03iJiZ9mPfajtwpduQdqXSuMmd43FybL3EYjVcanw3W1oEvS4gbN26o+QDr8uGHH8bevXuVjPH9eOX0GdfhBoBfDp9Gefjhr43nA+Zy5SeN3h5fBGUNL14afTtCTJQbmqurMvWuykTMffhmyu0HiLwsV7pSfxU//1kFoP59kFQYvOfTR/+Uq7KftVSJtWbrPa/FWjeE/7z2+qCA+aV8uH79OkZGRmRuZmC7zFM3bdqk7mlHN59FuZTfZ0rc6qlMZYFeBmU4x/kcTfCrJq7s4tcenLHKiFe8yDw1n8bc+DAunD2NV15/DW+99i5uXJpFJiX9eYOFQl0GkwtjuPnGeYxcH4Xb3AW9Oir5D6mveiIyV4sVbCQsGRsYYfV+S5dxgaFTx8Lmp6MkAxfbWJVegat/Ze7EwyrkTqnIJNnqKxbVK4gsFjcePste4t6o7PPZN3BByDvvvINEIqH4or29Xd37fQqxlj8qn//1v/pX6roxc/spg4VL4l4slss3bMKshYI6LpcHKJWEb91CESsy2D93+jT+6q/+Cv/xP/xHnD1zBpm8pVa7fEC7z8sHb+8bWNKiuDyyVCpiZmYG52WA8vrrr+PylStq1YxpOWqFFbPrkTCXCCc9FlWaVL7MLppSNmZRvbn0wQmvyY1ZJdzVxUUMDg7ixs2bSK9mZfAeUkcDZ7NZ5HM52JZ3RDIHtIp3hcjfDP82L3OiIJMC1huHjyIWVVnzzShJkqnSwrSqhLLRl5NDdzxJMZ1OY3x8HDdlwjI5eQuLi4767IQ6QRK9qZVJZAYSAxBDbjLIHaO4ConpYTxUwOsysVVLT8sqeGrwb3fYkl6uGKT7CL+SEuQkr2zQI8PDuHL5MoaGhpRX+mOe6I3poOBiOIyTZcM3w2olFM3pptyac0WZgPPHSLzlajBCBiIGz+1RISoiWJY8UMZTyHDwbcOROipkMliYnUVfXz/efe893BiQcknzE1MDMZnw1tc3KOV1fX29ygsPORgdGVODWZ7s+cjxR/D444/j4MED6O7qQk2yBlHJcFiENSeWauWWpF+VI8tIMsxJX0kaW1HaWj4nXYb0FUosS8aZXrZPrtJjZtWx3up4Z2aRq7DkhukQH5aEtSp1St566623MHHrllhJCHQk/MWJq1rURrByGY4UHtNFRaLKkLjnCj6WFpOpjKVObZlYWNIu6CQq9UeVHcGiZx1wlQ+Px7aET7jBNNedcdUdF+2VnQa4z3BbphO8F7rd7oS4WW9+NY133zqF//qXf4m//853ZPB2Tcm6XDaH9959Dz998UWcOzeIpSXyPFnR6zMq+w3SWrMAnw34aaMChXpZ3tNE6TKyGTUwf1sGYJQv586dU3JveHBIKXIXFxdEhhWUTOOknv0ZlbtcCaE2NpawuWK1yHGDmMXCMSXLvMGtN8AviuxgPytijlGLfKUAYQJ4LzxC/hEzuVMySq1AFSci2m7zjs9L6/FYgF8/brfeezRjribkRvWcvbD+eG+KzLjy9jv4s//lf8G//5//Z/zjD36Aq9euYXFp+XYwFvmG/Tr5Qv3KuEc8ATYmKtvkpwGOB9fSWnACuZ47mpM4Hg/JOP32pvZl8txQ2eXdE7S/6+eHRb+MR9zfCeHum/V+PtS971bd+nbenYq+gvjMW/7n+O6jie5+MfLLxy+/yvu1dC/4dh/mJsDGBJuwasuVPz5LX6sO1ZI5yqVLl/CjH/4IL730EgaHBtUYcHp6GsMy75tPzSNbzKAg4wbTlHGjzAkNNfclL3k8rAYfHHfKPft9mvGTSFfC4apgHhqu3MqPc0S68RLGBKpkfhD3Mv8cg2P2AGUYrgEejcujdZ2YMEzEQTTsyEBUuCmVR2Z0FiOXbuDy+dPon7iJG/NpTBZ5vChXePBNqw2Nx5Hy2HofG4ippPnIj2+z5V4ryrXIlzPlJHotg8oB2rNFaVpaGlEKheIiZuemMDI+ifnFtMc17qJ0fstSVnlpWqYM4PPIZ7Io5aXBStGVxI0jjdblscMSp26Jv+KyTCC87441GeupYxu5gifcgLwegxutQai6CY1VdeiKJVAXiaEYSSCnhyU+E1ouBWQW4BYkTdLCZyXJy7pMOfUionYGEYk7smogtBJBWoIuSkakChGV6tPsOGw0SnqTaNBSqM7OiluJM90gyWhGPt6KVLIexdpa5JNcgTWDmDWCSHEMkdw8Qjmu2GpBMdqMYjgu95I34ZW4mUC0FBbeyYiQWkVeJivLEveiFNJKOIysEUFU8psQ3gpx4mIVERLiCiOjkMOyW0A+EkfYqUdtqU3cdaEQbUVGd2HQrcxkYvYqYrlFRDNpyaNMmnI6SkZcyph7llE5w5Vkttonq6A5qApFELGkrm0pc2cBlrOKlEyyVou6TKY4qdIQk/qrKo3AyE+qE/SpYJo06zCPBpQcqffVq8gPvYW+d17Ae6+8iHcHlzCYsZCxw3ClDGP1ndiy6xg6evejoU4G7MVZTKeWMePEkWzbiRO7j+CxbT3o7NyC1o4t2Lx1FzZv2YL6hmrhhozw2KrUqfCDK/xjaShZUamvGPJGFGZEyixakAHWKmwtjyJXy1EBK3m3JF9FKUZ1ICM30bdTUsdS9lJOWrEANysDjSL37KqCpSfhxhOIxPOQYIURpDyiK9KelxEvCO9mMlImhoRdhYIZRtH0JqPyT2m6zRLbinQ8tgZ7tYTVrI0lPYEUouI3hXB2WTqpPFYtF2k7JP7ZbDipTUi9VUmNxKRmuBcY2x43aeM+XwHuV6hBjAyK1epPuUrXIO1I+of8DSwOvoUfvT2Avz+TxsBqAr3bt+D4kw/h4cO7kYgKf8xPYVVkqCmDGYea8fIG5esNcINB768TXj/naa8IlrVHykZuvZWyHnngMJJvRi3wYAyYKWTmxzA9P45MMYtkdR16u3Zh+9aD6NyxFdWttYiF6xC3a1Ersqy1pYSmJpH53JfJ1KWPcFE0HLjcm5GKfCHueVjg3okiX6MiQ6ttU2gQcWtI5J7IGREdaTOCjCt9jxFDQfrWvPCQY1VJVqqlr3VRihRghe+WMZWTavKVTwF+jbireO9w0Vrc+byLdST1L/3XamoFV975GS689TLOnL2AczfHcGMmhSnpu2X0I7y3gJAmfafwr6Vxtb2hhmOKe0UmkVi9TEJQy/cHKttlJX0a+GXi9Hjr7h8VWUqZRRKOvGPju/X9VZL8KuO//VvP7Vr6oLvKp8pfpfnHp18eH7cc18O9/PoyPMBnCFUF/Eeq5BWPz5R+Sc1LhDiQKEtmdQq+zHVHrk2j7/Q0FmaiiHc/jK2PPYcju5rQ3eCgzoqgLl+PJr0ZDfVNqKlNwEhY0q87yGs5oRQcY0XmLwuAMSuDgQx0LrhxdTXHLIo7w56BUZpCTua6RTcJfoEF7gstc/2MDDll+qTmk5wrMQsczdgciz5g4EKPB/rzRuL2wNDxBDc3e3Nlos03F3wpWizmUbg1jOFrV3Hl8lWMzcwh1NCM6J4vYNuuTeitCqOamxlz4i1TXcmA0F3fMnmXiv93rp8c1is35ovlz88bz7x/Rn3euH37Vhx5aL96K+M43ioqfobFlT5SW6ox0CyMW3DtPGans7jZN42p2WU09/Tg6EN7UUzfkrAWMDO7gJGxCdy8cQNXz1+Sax+WbAuxRDWiMZ7oJ2XK1TWpKfRfvYzXzwzi+s1BzPWfwdLoZcxkXEw1PYU9+3Zgb20eqbkZac8hhKNNqG+SiUMtpxliPngdN86dwZlz53GpfxC3FlaRtqKIJmqlNU9idoyf3N3Apfeu4eL5GzgzNoaS6aIhFEc8zFVB3mLOYkHyM3gNZ0+9iZuX+zE2OInRiRlMLi1jNRRBbM+T6N6cRC9mUJgdwdD167j0/iWcf1/CHs5gNS/8EbFhREOIuCG4qznM3ZrCwsIEpmYmcP7aBG4MT2Epk0MoHpP0xRAX1uL2/0ohKmVjF4pYnprDpbNn8POLb2Biahr5mRXMjc5hIRtFrPsgHnq4Fw3OMnIrMuAdHUGf8N3Fc5fUp1PjEp+rwo5LA+ZAw1NV2nLl6XAxEYQLE1NIzwwjszCOickpvHtzGH0Do1LHMqmKxGBmJzExfBEXz17G+dMT6B8Yw3jJQaSqFkl7Hvnxq7hx/jTOnD6Ni1f7cVPvwVK2JEU9hBkpv5HxWZm81aKxqQXJ+CKG+6/jnbffxU0Jp+AmoNd1I5tKITd8BXMzM1hxY9CTzairiaM+loEjbWrkRj+uXrqG8xf7cfnGKEYnpe4LJqpqahDWspidncC16304K/k+d/4cBvr6sLC4JHzVjJBMII0QV21lkV9dxdjQFM5wRdqN85i8JXmbWMDY+DIWVovYeuQg9u3fLBNQmaymZjE8MIjL5y/j0oUrOHulD4vLBWSzyxw3oQAA//RJREFUIn90KXvpA8KWtHcp96tTs5iRtj49OIbrl65geP4WclWcFLtYPXcNV8+dxbuXLuHCzT5MzMyjZLmIx+KoDUelKWnSEbkyKWHXJ+XKnpDSlivVyvi05dxGwf34eaMPtZ8c08eXB9LOuPeOu3Ae16WtfP/UJJbMJHbt24/HnzyGvfu2YWtjPWprkqhq7kFnTy862mtRHdfUcnX+vDC9/K5HnzX8/oP9+Ofn80bWIa/yT9Kr3ojySaXdywvXT9Fal/zTXCnDxIxtWU+PY3xoEJfGUyLj67Bz524cPHAE27ZtR1NHA1o7mlFbVS1tXhfZJDJH+smGeirg29DXP4S5pXkJz0Iiyk8WTBS4cuzWAhYXM+qFUESPQDNTyM5fxeDVi3jtzYu42jeKidlFpPNFpXSNiPxnn2ZY3iTT0W1FzI8hMt6HXyd+HRH3Qx35afSv/qSPzxv+80YVtZdeDzTwqSJtZd4SUaBWbmeFD1ZWljB75V3kM6tYifbCrOlAVVMT2nu70dGWQEthXq0md7WY9EMRIQlL/bkIqyj5IAEyXHm6U+ufPtbWgS9LiODzxo/O42edf7/N+bg7PbQr19WaH1Hpd718KBOf/8vPlfRR8Nzdie8OKkNZS58MKmXRp4nPmh9+nWDeWK4b8fPGu3CP6KnsZRq9vUBFzok7zq/FBJZVUqu63n/lHMZuzKC6uQu7nzmJA0f2YHedgZbGOjQ2NiMRq5a5oYWUzNW52qths/RrkTByuVWZa89iaW4CM7cGMTQosvN0n8yrlrAi7tKWjZXFWUxIv3HujMzB5sIwnRhqIiEkpFNgH1EIcQbKl7T8Wqb88pYkGdqoaq/Kdsa+4ZP6vDFQegn8BgWZtFKI8k0vj/3kKYS6u4KVmRFcuTSOm0PLWE6nEY9YqG1oQLj3MPZs7UVXMoyYzgExp7TCQhyVcODhtxA/XxX/71w/OaxXbswby59Kr9PvnZFJ5iq2b9uCh47uE/cyWHbDklTxp/YekmG9mFHpRYQxDtfKY3a2gMGhBcyncujcsg37D+yCPnsaw9LITl8cxoVr0xgdHsHs6AUZzFzA6FIEVclO1Ncaal8qM7WMW1eH8frLb+ON/gmlNFy+dQOLEwOYzmpYankIRw6JAKhewvTIdYxOFZF1GlHbWItkXQ6zt4Zw5ZW3cPncVVwemkT/zAoWUgWZICRQn6iFtjqB4evXpI5u4kb/CEYnxnHr1iiKK8vQwl2I1CYRC68glB3C6kQ/fvjGCN589wpuTd1Ub+uHJ+YxPlOAE02ie/c+7OiRSerUAAZOn8V7Z/pwum8ZN4dnsDh+DUtTI1iJN8CsaoQMOxGav4W+y+fxztmzuDk6hfN9k5heSkOPGKhvqJEyiHv7VLlFmciwLGRQOzaDC5dG8cap93Fh8CKWF1NI3VrErZFpLJpAcucOHHpoG1rmRzB56QpOXRzC2f4pjIyOY27sJpYWpjFr1qCqpgWxqggMLoFlFYoIC0l7C5fy6Dv7Hm5cPC2TrAFclXDPjcwL7xbRXS0cahdxa3wCly/14dqVAcxMjGFmZgwTGZmIVSWRcLNYnptE381BDN4Yxvj4DOYjW1FMm3CX+rEwcQF9QxOYWk6isaULMam3/r4+XD17CZPDE8gUgYVECxZTWVhX3sDsUD9G0wYysTYR8LXoisxguu8KfnrqKt65cAN9g1O4NTGH6dl5ZGUS2N7dhmprBeMDN3H+4nVcvDqEsdFRrEz2Y2J0EMXardBq61AVMxHOTGOmbwA/fr0Pb713HtMzNzC/MIWxiZRMJPPIIYJNRw5jx+4e1GcnMHrpLN569ybeujSPwfE5LI2dwsx4H4YXpaMI16MuaSGJUcxP9OEnr14RmUXF6AyGh6eRt1Koqc8DxQxunB3Ches3MD5xFdPCyzNzC1jOS9mGY+hobFKClSs5WCfcI41tTcmFimnIpy3nNgrub6UXGxoHCyIrpU3DzsAevoz33nwH7y/UI7n1YTz2xCN4/MhWtDc3oLmmGs2trWju3IS2tkbUVxtqb0LyhL/vmx/uRsy33398rpRet5PIuqQyq6z0Uj8vL1Rwef2/NyaQJ2XGQyuo9JocGcbAtI1ITTu27d6LXfv3oaOrBS01CdRVhxEPcXuEFCanFnFjWKRQVSvqIiVceO9NkZ1jyBZt1FZFURM2MTU6jJffG0O+oKMhqUtfkcLsxCCun7uEs+9ewpmhcYxM3sL06BhSs3OwHB2hhnYY8TCq1dmQ3KuR45aQpD4kvOUNYysHjZXX+wFr01yZlw2p9PKjux2tl17vQsM7Du6kjfe8ulCHwxQL6qVcrW5JP1MPO9EGJ5xAvLYWHVu3oKMtjjaemMwxmh6XMSrzbEtt8zRqvnCViY0EqPbzknC9WP24Pn2srQNflhCB0uv+w931ca+6+aD5h9Xj/VzHn3baP8/tgXmjfNjYSi8R5h+IngaeoeN60pb/1V25z+Kn6HypceP9d9T8LVwTR8ueg9jc247u1nok6huQCJcQKS4htbKCSzNZ3Fpalbl2N+IyLzdnRzB97RwuX7iMt4dSuD62hLGLFzA7NYmJZXG7mJM5iMzfrr+JS1cu4NK1tPQJUdTVJxGvqZJ5iMznZWwQcmS8wnJkmuRZvTARPGhKrzuuH2D4jSlEhiCDujpKWlRt9M3VTqnxd/Hzc9O4me1G/aajOLCzB20yqG10l9Hg8BBRG/kQj6GPSbOIS21xI3cpbJZ3RR14Vcj/3t2nD0mMitpPg+RV/ttrjW9fTGiuqT6/kBulIg2FI2qvkdrVq5h5/+9w6mcv4czlSZTcKDZviqIqtoz3T0/ivdMzmJuZhm6OY3V2EK+/0Ycz52YRbW5Gy46tQE0LRhddXB2aRyEzI/5YZGksLQxjcHQEAxNLWEoVYJYmcfX9N/DmqfNYXo2gsesA2rYeRCRah5xMwnITM3BXijL3tBGvrkX3nu3Yc2Q79tcbmDv/Bl47N4GrMwWkMxPA5M+wcu6H+O6pOcyGdiG5qQ2RVh3TmTSuDWWxumKg3VxCqwwspy/34/TLb+Nq/wqKbcfQdvRxHGiZwuKV/4qXz43gp31FDMznYKcmsTBwCT/6x5/hfTFfLBZR1VaPuo5GmZQIX0nZqc2JOUEuprE6Nogr753Fy6f6VP6727aivqpFHRTQ1zeO+ZV5FOMLapWQOzCKsZd+jndOD2HUrEfrjv04tq8bXUkbr707jjNXljCVysuQlx84WtCtIhJSOXppCQsjl6TMX8M/vPQm3rgyjqLRjJ7dh9FTbWNp8BzOv3sdA4MOqqs7cfyRZuzZoWF+chxXzp7HjckUFiMtUldb0VjTgeZ4AlviSaEadDbFZUBuI51fwOkrMxiaLGGJyyCSNUgmalBvxFDNvbsaGhBtakId33JMjKP/2jCujKxgJWMhujqO6698Hz+XMu4vALGWNnS1d4jgj2Aps4K8k4WbWoSxuowqI4qO3h3Yf/AwdrbXYGHwMl66chPnU2ksl3IoTA5h5N238NO3b2K+WI2aZin3mI6phRQGpzLIhasASVdOuDkrE9WhN17FlQujmHK2oXbTcTy+U0Nh4if4yVtv4qfnhzC8MAHTuoTZ2bfw/guv4OXvyiR1cBV61SZ0tXSiQ9q8MzOAcS0CffMOHDnUgePb+fnqEs5f7cOp0xexnHdhhTTpdjTEpWyoCHdCEWlr9xbOAe4PsA5tl6eYcr897/NhczaDpYEpRNp2o+7wM2jauR8tjXFUSRvWpe1UyQS2szWJtpowkuQL6V9CjscDPgX4lKCKuqKjE3CAyp+yLFcF64RqLmUgTmnPN7feplklGJBBKg8YsSMyTtCRkbFD2sojZpZQbeel3c9DM8cwMz+H9wZ03JipRrM9idjyDfRfuYx3370qE/9hGeROo7//Il55awBL2TDCoSWsLpzG2Xd+jhd/fBlDA3n0HNiN1i0tyC3ewuC7b+DC2+/gwsgy5iUpIT0ltCLppEqOR5vf+WxW5UHSxQEjrz4F+DWhzDs++KjatmIh/srPZahbGVfxM0eaU4lXX1+H3Y88gR2HH8GWtmq0RrJI6KZMXKLSzwvCMr6U/oQHLZiqOzERcVZkMpPyFJ+cAKgovMlNgAC/LHwZ4tMdKMa9B3lY39/d+DC7jYyPytevA/drWX1+4I8ZKvtP1olHnrTlVzf8SopKOhkjqpPFQjD0uPTrUbQ3mEiGBzAz+gbef+sd3Lg8hqVIEsWGJoT1VSRW+5CX+e+ZxRJeGV3Eci4PLZ9CZKoPy+++hHdlLvj9aw5u2DvQXF+N7NI43j51Gi/89DTOXexHTvqBpo4kZq9exdCZMxgcm8GtgoaMzFUkRTLu5NhFkilzEg4DOLrhVtUPGgKlVwWoEVXHRqtNY2XCQq4oFDA2MoKZuVlE4zH09PITlXZhaBtGOIx4Ii4DDSqPZGBJxZDw/u2tGu6JjS3AVDtQ/3hiHc8J4jfJJbXJnmWZahULNwufn13C1PQ8wtE4jh57GF/4wrN49umn1VLOiYlxLCwsqCX7s7MzuHL1uvos45lnn8HXvvZVPP7YcTTUN2NxIa82b+Wm4JqESU334sIispmMMl9ZXlGb58/LdeuOnXj++efx29/8psRzErU11WqFU7K6Gr1SL49KmL/5m7+Bb4r9o489qsIaGR7CSmoVdtFEenEJff196B8cwtOSjt/6zW/gqSeeQndXpzQEB8ViTvIL5LN5DI9OYHBkApFYAs88/QS+/e3nJe7n0NLSqD6zu35lGAvzOVUOqfQqJqZn1BvWXbt24tHjj+DwwQPoaG1FTAuzFKFR214qYm5qEleuXMWApKG3dwt+6xu/gcceP466ujqJvygkEyotpPYLSo2O4sb165iamUFzSytOnDyJLz/3FRw+fBi3JiaU3cLigto4ntKrJH5F4srAOKTKfWJiEiNjt6T2NCmPY/jylx5BT3cXpqemcE38coP1Y8eP4/mv/QaelnqLCD9fvnhJHVzQ0NCAnbt3YceO7ZLnZrnfgyeefAInT5zEo488gq2bNws/5JDJpBGWvFHz3tHRieamFmzfvgMnTjyJxx9/DA8/fFTM2xXH8y22K+Vlr2Zx9sw5MNl79u7Ds1IXX/7yl3D80ePo7uxAbbJG2peLhsZGHD16FN/4ra/jd3/nm2pj/ESiCrOSvuXFLErpIpbl/qrkJS9l9/gTT0hYX8DBQ4fQ1NSoFltyQhEOG2qbLm5s398/AFPSsO/AXvzmN74k/PKb2L51G1aWFmSC2adWIJmOhtV0FgMDQ1iYW0Bba5vE/ajQcfT29Cp+65ZyfP6rz+Fr3/gmvvjcc9iyeQvmxe+Na9dRLNnednWSPxkeqSphOtiGAtzf8DYl9Saphm6AR7XnZHDCdhuLx6Udx+XqrWbzNpu+o2hQG/2GhB+8ZZkBNjjU56cii+9atV0eJLJd56U/nJufVXKF2x6cPd+PS5euYnF+UfoFR735zUg/Nif9X1rkZELkWktbG2JhHQvTIr8vX8I18Tc8Mi59lAxYRc5GpSNcEPdXpY+43j+Erp4t+O1/8tv4+le/ij27d0r8tjrwhCtl1DiDHRbTJEQlHTfGX6vY4ptQ8mswcfpscKc2PAUkoa7leuOm3uFIBFWJhBoHhGtrEZI+S21sb5oeyb3ySdnBsQTr/UPg1fTdfBAgQIAAAX49oMxl18t++c6Yz5PtcRkbdssctamlBUvLS3j/7bfwxqsvY3g4hUJWxoqRGNxIVMaNJpaXFmUeMoN8PivjRZk3ybxxXubE8zKfjoQjOHjwoMzZnkdXdyemJmWONzwic7AIdstc6ktf+bLMUTqxtDAnc/NpmZvmINMRtWKd40/VL6ikldP3AA4JPrznfMBQkLFELhGGFjFQaxVRtTSN0sVxFPrmoG3rQM0XDmLzsT3Y2dCM6oKJYj6vJjZhJ4yYyxNNNJSESW1urkCe8vjqNjz++uy4jAty7kTvPVjC9XxrqDbeczmA9hqG0gA7Mli2eDR6VBquUDQkcwAZiEkjslZd1IRrULPpOJIPPYfmw0ewuasWzx3cjLaamJRJAcXZKSyPDmNmcRFjehNWd+xD27btaOlsxOGdTfjNx1rx/PE6tFRHgWxRvboMIYZaSUBtcRXW/DRuDd7CfKGImU3fQP74b6J5xyY81OjiCztq8VuP7cCRvQ1o7WzFnj270dZShVSqH6NjZzEyPYCF3BJK4UmYRg6Z/Com58dxM5uCvvdZhA/uRFfNFjzVeBC/vX87vnZcx7amcdjzFzBxaRgXZnZisuafIrn769i6qxP19UBHj42vPNyM5vQUMhfew+zgTUyLMJmQsskc/gq2f+Of49gzj+LA5iS2hFfRmZ9Htbil8o77XFl2HlOLIzg/fgtD6XpsOvRV7D8cFSGm4fnnH8aJE09hd8cW9FpR1OZc/GR4ADccC+m6RkzaIVyankL/fB+GVqRMr/dheXhUytiEm49AtyOIFGW27USkHEeB0DQiW55EzxP/Oxw9+Xs4uKcdSSODaG4aiwOncXNuDpeFWa8sm7h0QSZgfYuIjC0hdaEfM2PTmHdNFBrDqGnXkWzTYTQfRLK3De1tNXiotQFPd9SjNZGDZswhLWxjtTWjrrYDvaEe9Fb3oHl7NVq2xrFpEz9zrUFzoogGdxL27KjEL5O+MekEtn4R+499HXse2oMDR+vwhcd78DuH92G3HkeivgtN2w+hvaMJCXMWS2NSryN5aE4XQukVhFYW4GYzWJY2OFwsIr5zJzafPIm9Dx3B8ceO46mTB3HwQA3isXmE44tYySzj9LkbsFCNLY88jrZnj6K4WUe8thlf2rkf33ioAT3aVcwNX0PfdA0W9b1wCvtwZOuzePSxp7DvoTa0dcbRVNslZfkQHnt8JyKRtPDarExOF7EwmUNiyYG1VEA2YWBJWNoyRRgUpB3JpMXVSghF1giEAPcdeP5pmKs2HRMl6T5zWlhkjoZCPobqqrgMbgyRYGHUuVWIhnTkpd7zIU5aHe4pCo2KaWtF5GymHGKATx1e1yd1ICQDVG9XLF5lYCjynO9tpZeDKTJQKZYcfgDAFVRhcSQU0hAKhzAXzuPyzADefvMneP2v/wNe/P/9Kf7xx1dx4XoU6eUIQgXpzcwCYtYoVpYvYbxpL2q//DT+2VEHX1j+Hvr+/s/wP/zH6/h+Xz0e/o0TaD3cIP3gEFb7TuHW3DL6Wv4J3Cf/L+hu7cXBrjp84/HN+OLBWtQ60xi+3o88F3hZdZKPRkTdKKotIG7dUawQvrKrUuEVrPb6dMBS9kpa/t8pfgXWBzevV3asD/KduNHDwmdh4S+NMyd+suiqk4rVCdb0aOaAUkb40lTbcHh7elExGxKeVews7kzh5YK6BggQIECAXxaU4JSqlOG8JxGUxpTOnokS4eKMpiEZHxi6dxIz932ld+7xu/nRL+PZf/HH+IM/+H38UXcB4Z/8Kf43/+L/iv/p3/4Al0dkjpvchJlEE4z8AmIlmeOErqLgjCIjsxbUtqBj8348vO9xHNu3G7sOdWDX7gZsad2EQ72P48nj38Sm419HzZ6DONaygIdiA0iZFt4vVWPULSFWmEMoNy9TeuknuBWAzrm29C2S3gcNHOsFKIOrtzQ1IHRlEpPH9Pg4XnzxRbz99tvqCNHZ2Xm1YolvWefm5tWeNNevXcPM9ALyBRmEiE9b/FcOOm+3kfsETC734jPULEAGYNy/Rlozy4b5snnKVFHKSRpNoiqBzs4OdHU3I0lNVSSi3kIakbDSbIdCBvL5AjLptNr7pbOzE/GYNDUZ0EViUbS2tmFT7yYxi6m3ma4RAo9uJ/FoZL615motHufN1XU1NQmEdFetqAqJH64EqqqugpPN4szbp/DDH/wjXnjhBbzx5psYHhlRdUYVHgeYJQk/L3VKtPFte1SylohDr0mivq1VreCpr6tTx8vPzMzCEvedXZ3YvKkdiSRQ5OBS8sQVZdEIT+GyhEcK6vQ+robjnkRbt25Fc1OzFINMjSn9+EZW3PKbdG+Q66g00E88HkV3VwuK8quprcEW8bt1yxb1ppcrt7i6bpXH3PM7bAljaWkZ58+dw6lTpzA0NIRt27dh586dqK2tlYxIHqW8olEeUUjp6zFdbU0Ntm7bhh3ijt8+yzSOTK7qkPI7m8miv79fyusNnD1zVibt1di1axc6OzqUex6hz2P3vf1SZLLP+V5E+EHqnrzAPHFFFjdvpztGzbzy7QZXTKoPMWQwzmcqhNXEq+yH4be2tEh5UZlqqfwmqqtR39oqg34Z4Et+xkbH8fLPXsZf/dVf4fvf+x4uXriITDajVkxZFo/otW6vjmsVf42NMtEU/mA5dEgeSDmpI5Yny3xyclJ9QtLVXY9GmV+qz5Ukvc2Sjs2bN6Na4ueqnWwuq9LHvQc3b94kdZsUO8mX1F9R4h/rH8Crr7yKv/vbv8PPXvoZLl++jOnpKanbnCQ9IleZrLAO1GsU1gVzx9WgnJYEuK8h8lDtISANyNZsj9elrjkxJW9z4CNNVq2i5MrYvM3TbWVCK16Ut3Iwd24CbETwk2TKLrUqT7Vjry2rleCUPaUSwtK/UUZw75Fjx47hySefwKFDh9Dc3IywyBnyBPsKwwjDsaTPk36ho6Ude/YfQEd3B1LLMp44f07tlfboo4+itjousiOrVodRhm3btlnkmphZOSWLGRf7maamJiXTeES5Wk0oaXIkTWrcUebHD1NsKTkc4DPFnTpgXbFPNmHxCwPWm4xB7JI8Sz9tktdYt2IutjLAFOEifaMSJuvA620CBAgQIMCnBXa9d3W5lO++jKeFEOcXe/bswXPPP4//5nd/F1/+ylfU+PHs2bN4//3TGB0ZVV8IRKMxbx4V8saa/FKFe6g2NjWivaNViKMRW+YyUZn/1ch8tlXGBVyYUa9WB/PrMzV/5upgDkZVpyD/2HeUe4fKpD5oWL/nfEDB/RBKUiKWVUComIZuuZhercN8thEhcw6ZmffQd+UtnL98A1NzyxiZXcXArUWsTK3CTskIVAYp0GRCLrQR2YpTb+9HsOqlYUi7lPYqZvLs6jKXo3KinHo7KhSXyT5PCQxLQ5TJXZhKEAf5cCOyRhPy0WbkwklkHMm/PS+eFtWeNVGXx2lHsKpHseroMigvISaDN6plopoM4mUg72ZzKKZzSIdqJJwY3IKDWJ4KGQdFicPh/jdmNbQVDRFtBrFwHqYWQ8aukQYdgh6ZhJ27hqs3ruBHr7yDt29OYjneiupNu3F0awN6kkWlYS+VNFhFERPFkLrmSgVmXRJSFMrLgNNBaSUMPZeQYuFplllo5jTCxRmZ5GSQl6Lhu1PozbALVUg5IaxyIqPbSNopNITySISLwi9cwVFSSjnXjUjBcqOyqOKHIg8cl3iMooRTclFwLCkfmVRZmvCWBjOdhp3PiJAqIiexUT1XiLjIC1VFqtBb14ltPQfQs+Mktu75In7vW4/i2RNbsLk9ofYJUmqpiPeOF1otTL1OiCdfSjxaGlp4TMp+Ba4dlnKIISZ56EpWY/tmmVgd3I+W/fuw/+ln8fRv/BM8fHAXNkc11K/KxC4bRr38VttDmKwHMiKMXTeKkCMTvlIeNUWZoFkipEsGnHAIxWoXZtRElamjWtJkhhbhxJeBsPCH8BYVmLYM7kslruxzwcVP3NhbkzIypZRMzUXWLGL60nlcf/mneP/yBC6Zvcg17cOj7RZ2RqYQCUfFbRwFyWtR455pErzVgJh0BaGQ1J2WgmtmoOVcJEpJmZy2wiwmpXm6KErdZ2RCkZV4qRBFMY6Ek0QhnRc/JiJGRCarEra41ZPCOzGpi5CLDEoo5OeRHTmPiz/7Lv7ihxcwMB9HW30H9nb3YFNLD6rj7ZKQehRldmJK2K4hckDIFT5he+LnTgHub7AmvYM+hOfdKkRQg5pm4feGPLKj/TAHR2BnskhHDZQiMSTcMF0iInJIWibckMjFUJW0yYS0I054PWkc4NOCtEupCdXflcFWySeaatIbqhOY5V71lGrASkfiSq2ooXKTq2o01EVrsa17Gw4+8hQeev438bAMYp99dDe2d1ky8Mwhb2Sl77AQc6uFD5LSJ1rSPRSQKsSQ0ppgVCfQVsd9C1cxt5BBoSRxC3+wP86LbM1ZGeEVDVX6IsKat7KwEEpIn10r/UhSxigiU7SwyBl+vigSR5N+Ta4fhkDh9esH2cVv1f5o64PwVnYRiv9k7MmTmNWD1Hl1PIJEsh6R6mbE4knUCNuxP1Xfuwj/GdKXsO/URLYUtTpF7M9kiKZeznijOlKAABsRla0kQICNCgpkn+6MEjy6w8UU3ST1REWTI2N/mctRH+CRJfPFKoSqOpHo2o6ax/biyD//Av73X0viYPx9zF67jisXc5ibqULClrmMWY9EIY5wKYaizL8zMmbMh+IyP9LkmdG4iIW4OETSoZJlI+QWUGMbCEu/wbEnX8xGZaQSYcJCMvMORSTVatZzO/W8f9CgqilAGcJQXHPCNRk8Ea+6vh6btx/BgYdOYEtvG9oawkgmZMAhDKUZMtjUI4gkkoiHEzL0CEHjEinxa8uUl3e3cdfDZwkZgklDUA1WtRS5CtffSZ7fuD39ndImOCHllm+RuZ8Xl9UbYR22HpNBeBR5OySDcw0lDrSk0UEXeylHp2TB4kQvXoVosgZmqYiVhQXksznYVg6lQhqphUXMzc5jtSANNm5As12ELEmfxFXigC2ko7GmCWE3gvnZUeSyaZiSnoIVRi7jIL88hulb19E30I+puSWEEnXo3n0Auw4fxZ4tXaiLM/2SO/mjoiQeq5bcGVhJpZDNi1U+C7OwipXlZcxNLSOXKiASjaOxsRYRw0J6aQbzc/NI5W0RNBJIuiTuFkV4hRGvq0dNXQ2qo7pkOSfVXhAZY8p4lZNbns0mo1RXBqhSdmpFEadJMmFiGuISR75YUif+Ucm4uiyTnukZzE5PYjW1Ii5l8hOWQW5jnQx644hFY+hsacGBPftw4PCT2HfocZx48hB2bGtHQ21CfUbFlVv8JJUKN4SrhAO9jdO5Ws5xiwjJBMygKsaIIhKpRnUsgXbh7x3btmLfsWM49PijOHR8Lw4f24PNPa2oDYdE4FoSigjLkoa0UcK81E3OVkNrte+YIRM4HoFLxV1UhCrjzkk5FEXYR8UNFXG2lhdeKUjaTMVDXBUXiYQVL60sLWN5qYQiN343C1hZXcaS5D8vvDJ64zrGb16XPETRtucotj/0EA7t6UF7UnhEwjAd6XzkakRFkBsG5mdSmJ92hb8yyGaXsDA3jaW5RYTssLhPSBkm0NrWCls6pIXlNJYyNrKSH2RKWJlPSdnPwBGmr6utQ7Xwa8m0kSlQ1WVKHlzhb+GBnPDNzDimhm9iYGwJzZ07sWv/IezZtRudrR0wjITUq9SdpEtClqZEJTgnHmxx5AtqWgPcz/B0INLGpC0LJ0t7j6Cuqx4tHbVYGO7H4LlzGB8ewVKuIAMUcSs8lllOYWFmCanlHIol4XVpOzw9x0eg+Pq0QXlMWg+sC/aR8hPZqerbJ1Xv0m9SxsqVHJCMJ9HQ0oa6zh7UdHSgvVX6hRqRkBEZRchA1BR541q6DFDjcjWVnL92cxizy3l0dHfh8eN70NQQw+nT57GwJP1PJIGq6mqRlw5mZqewuLwig9YizFwac/MLmJ5flL7LRiJcLeaSVPKRpE3TJXVqE1L2MyJtVJ8TYEPhXvVCc/bhcuWKPb6Rt7iCuSR9jsiPkiljKbUfJh1LpdvSj8q4RlW/8KEtMshWva08kxd4E8iUAAECBPgEQIm6lu4GxbpPqkNW82GPXFtkeSGHtMw1VjMyR5L5rF0fR7K3CXu7dXRWr8KQuUepyC9mqgDTUNvVGFZIrjJW5MxN+vmSzBU5nlBbD6lovAUEPFSJ8Tp2Sc2fTTE3xY3jWDI3owJO3PKrLSE/eZz4q/sHEOw3A5QRdkxEnZL3aV88gTA35X7kKI4//xU8tPcwHtq8B7u37ERzTyciyQSaEgY2tdSisTGBSNyQSTi3Q/eY9APYSGMQjozKjVfxP4naLz7LA5dqKrgcSBnSsFz1CVmxmIdlUXstDYmf7RTTKOXmYZdSMvmTQjPiSilli5tMYRU5JwK9qhPJ+mbUOXPIjZ3H8OAgRsdm0D++iqu3ChicLSKVXWE0KlyehZmVgV9WWi2VGm2NETRVS3ST17F6/TRuDQzixugSLgwu4nzfEgZnilhdLYigkIlAyEBNTCYNMiFYKSQxn0mgVLAQEqGQqE6iuqlTrnWITp5H+to1TPTP4+bQKq6PSzgyoZiRiaoWrUFjew+aamUwmRnF7PBlTPb1YXFiCv3i/vTQIkLVcXRuakNzW4Mk20FhaQH6igw71YZumgglnv4ZQlH4oURtPKKI2AkZ2Mokqb4KnU1RNDu3MHX5VYxJeH0Di7g2vITrE4uYWFxVg9toWEOvTKAaEhJmbhVORsrYKsk0WxfSJPwEClK+fNPPz29sTQSrtgI3lJFylLgl31YhK3WRVp9aWW4jTNQCwrMtbTVoSRqImKsw05J2y0E0EhHBakOm6kJRSXtCEhFCooqCehwL/cOY75tHer4kdWOo1W7LUv/8ZFITwWw4UaXYzOSXkS9JuKE8SlKXmhmCm9dRyEnYIpD1aBSJ1gSMBgPLY+cweuEMBq8N42bfHM5fmcS5vltYKhpYLS4gb80jLpPHVqm7+kQVcrFaLDphNQnQJU+RcAzV1fWolTrPjF3A8IULGLgxhoGBGQwMz2F8ZgU5fgqZWUVjVQjbt22CsAgWxgaxcOMyZoeGMT2zgLf7hjA0QeVWL2oaelBVIzzv5LCytAK7KHFJowhJ58Vjh/NFU9Il+cibaIhWIVqVgB0OiVkB2cKy8FtKJqOsJ1fqxtsvz6Hik29g3HXkQoD7CrrISRLlJOuWp3TGO7ahY+sBVNmLSA+8jeGLb+Ha9ZsYGpvC8NA0rl4bwcUbwxieXEQqL4MU+a0dcASKr08Ht/s79VSG/6Dq4A5V1hHfnYiYVERr2hYL3qfV/FycfaSIBZREXlkGT+s1YbiWeCiKzMiI3HFRWlnGwMWbePvKGG7ZSWw6eBRfOXEY2xs1XDp9GuODM9JnViPRtA31yVpEFq9g8Qo3u53Djf5ZnL88if5hka0i89u2VkPEofAiZazILullTF0G01yJFuAzAznnXlAjLDUrKruSe/W5rPAd2z8/b8ylM5ickPoenMD42AiWbg1jYbQf4/3XMT8p/a8jYyzE6FmNa7xVXcQdbvU416cAAQIECPBJo1LW8yWZJvNqknrRrYgvvWVsUMohl1nB1PgEBq71of+qyPOhSYwMzOHyaBRLzg4kGhvR0OwiHs3CKaSBYlYdhlWScKnUcswiTDGzzQzPKZMIY/Ksy5xL3LvL0PScNy6VKLMFW8YcfIEi7rhVjtKSmTJYkHDklsSeQb00uSsXDwYCpVcFYk4BSaEYGc2IwamuRXzHFnQ++hAObt6HY627sbNjK2q62xBrrMGW+jA21YZRW6tT36M+j1Qf8GmJcogbDWRwf5DEluOtSPHYXpqBmsxJYxEDg9a6ZEoalyaTdSMUQjgi17CEIGVk2KuS06yU1aJQCtGQATdcIw01AkN3ZGCeR8FogJXYiWRDOw7WLSM5dxqn334dr79yHj9/fxqnJ2OY1zuBqDRSKqRDMjGQyUGOShstBj0WR2tdAXu6YthSHEHq1N/h1I9/iO++ehnffbcPL94oYs7tQl1NOyIy41gcn8TwpRu4caEfb17OYWy5RWQPt8Z3EUnUo7pjF9q7t2B36n2svPwPePOVm/jpqVmcGctiRjeQrkoC8UZUN/dgZ1cEHVUzyIy9i2s//zGuvHEKP3p3Am9NAMnONuw40IXW9iQ0EWjh1RSas3HE81G1qrUgRZzVQ1iNhJELixnXS8kkJ2ToaGitxZEdtXiiaQrLZ/4GL/7jabxzeh5XxiyMZCNSkgnoWpRfOGB3TwO668Jwl2YxfvESLr3xDs69+TYunHoPr77fj+vjK0hlvb1c7FAGhfAk7PA8K0hI6sHOy8RrBa7uomj3IIc2Mjl27mrD9uYIStM3JLyf4P1X38R7p97Bq+9ewTtXhjE4W0Jaq0G4sQqNLQWUzCGMv3EW469ewVTfAubSBua1KuSiFkohE2EnCr0o6eQ340YRCOdRNFYg/xE2E4iXqqDLYN0mPyUSiPRG0XawDfbU2xh49W/w5gsv4ccvXsEPf96Hn50bxWSxGo09MdS0mcinJ3Hr0nVcP9OHt/un0JfTJR4NVeEwErEkaus6sLm1Ew2rVzH05l/gjZffx7vvD2NA6jRVisCJRYDUMiS72LF9E5J1CayOX8GtV/4eAy+9iDcuCA/0j2M204uq2idR27Qd4XgRupFDRCaQUhMISacRkQmKEZG2XV2HeF0T6h0pg5vD6gS2i9evYHByCAVzEXVVLmJuTvxxzyd+jsTj5Q3o0i6o+Apwf4MDi5DwH/ely8FGifs91W1B196ncGJfI/ZEh7Fy4w28/PNX8NJr7+KVn5/Fm29cxukrgxicW0bKtNXq2jty+A4Cxdeng9t93u0b/yr/1NtZT21we08v+WPVcPsstQJaDLiakyteKYv8rZj4Lx8twZQBqOvkEXVLiPOzQ0NGBRGRwTMzGHr/Jq4uSF/T+yg2P/oMnjzQguMdRZRWUrjVP4L5XByR9oewe9sutRlt+r3/hB/+6D288Hof3nx/HhOz1ahp34wdjzUh1OAKP0qHY5ooST9XlJ5OpDETeE8EPPbrw8cpWW9/VLb9smupD9aJ69jqYKTFxSWckn74lfevYeDmdaTGrmPx5jlce+c19J2+hKl8NXIyruJbe76kNcQfedV/b++FqrhXHoLhfYAAAQJ8UlDdfJkqoVaFKyUXNU0kKpnkqvEU7xwKhRRGRZ6/+/NX8cqPfoo3X3oPr//sIv7xdBLj9kkke3vR1ltAbdUiEm4eVVpBRohRFESEM1xDxpoGZN6NVcg0XAYj1XCtakRkDhaJLkDHEiK69+UBjITMpWsRNuLeJ5DqxUhepUW9hBfiuxc1xf9ATj7/CEmZ/kve/I//Ul0+Uajl2tLBq41/BRe4EmNgQG3I+sQTT6hNpX3QrfcWzLv/TGAWJG7qbAXyLxSOwojGUVWVQENNEjVCVTLvjXDvDBl0dB9+Fnv37EFjbTXi4ZAaY8gQVA05YuVJjTcY8fOl/qv7O9dPDuuVGwdULP/l5WW1WV4qlcL27dvw0EOHlTn3RaKvsLgLcUAsYThqqZvks7Sk3iIXS4ZaeWVUxbF9725s2tyLhtUhKa4C8u0Po27HEWztCKMb0wibFgZnWtHU1YPe7dKQOxvRnDTQaRUwcWsCpyaXMTQ2juLCHFqrE9hx6Ahqj53A1i2d2BnPICfmeb0FdV37sWd7D3a25tGYrMH01AxGRsZwYXgVN6YKyOVW0dkRw94tPeiurkE2tYpby4u4tbKCUr4EeyWjTpzceuQx7D2wHV0tOupiRSRjSSyuhHHhSj9u3ZrG/NIiIokoNm3djE3btmLb7p3YvKUXHYYJM5vGyMwSroxOSfxTmB8aQrK6Gru+9A0cfHgXttVbqMvOwc0VoXWckLzsQ20LP0fkJsgsQSkzihUp1qg8a0YWybiBltpGhKO1uHpjEG/fuCyuIkgkmtDc0oFNUjfb9+3C9m1d6K3OwC2VML6SxK25AuZnxrA0M6g2sr8xk0FjQwPaG+tRm4wKO5oi0HISXxhhkbU5yb8TkzA3bcOmnVvQ2FKnpkN1uVtoFT7OW3GMzi5jcGwEi8tLGJoYw+gtTtYctLbUoLOlCs0JBzX2ivr07ydjLVhezaE7WcSWtgRqJA95J45tO3egR/iBGy2bK7OoCjlolzzUHDkoE74EelbmYOeyyNZvRmLTfmzpbcH2pqzaqHFiPIXx8QVMzCxgfGYOM0spxGpqceShIzjcuopCZglXxy1cHsljef4WIpl+day70X0UO/buFZ6rQlPMlK7BwHIqhGv9NzEx3Sfdg4VYvAUNTdtU+nbt3yPl2YjeeB6lbAoDc6u4MrGI2albmLt2Vh332733G3j8qUPYt9eQ+ltBPmOisNyLXbt2YtuBTWhqiqMmUkQixDLSMbTShoWFBVjpfqyuzCCTN1BVtxUHpF3tO7gD8XgYunSAhtR7WLoXfg6qmqfXtNZtqw8KuFnn3NycOgiE8mjfvn1qg27vwASvbDZq+ahxjVytkAtT47peDVEnj/p4NRrrGhAORTG+lMbF8SkszM9jZmBEbVSuRWLo6hGZ2N2G2jhfLtgiIz6ooNho+fb7D/bjzMfExATmJV/cWPXAgQPqgBK/f9/I9VYJf5in+zdq5bNPHqzyOCDEVZpSx1RU8mv1sCEy3ZrD6sIiCtFNqG3fjM7NnejobEBcGnu15N8QORwyZJBpF5HNRFCwO9Db24PmWheXLl1CVWs3Hn7sSRw7vBOtDTbqEtUYyvWqstzdm0RvW60MfqVcZXQ6MjYm/c+EOizHybno7ujG/uNHsf3xw4jKmKNZBrT8vNs2wkrJzkQb8s+vE9bfevWy0evJT59/9ZV1fOahN9///vfV+HH//v3o7u6+LTsqefGzxR1e8lBOjxjfHhPTSE1IxMy2kJd+cl7GPz/94Y8xJmMkrhiPxpOwpH9alDENXzzu2r4dDdLfyxBDTVi4pYCt8ix1LGGrO+6RqcafjINTm88Ga+vAlyUED4PifIB1+fDDD2Ov9Ocsl8p6/+zrMMCvH0EdB/DaO+XD9evXZZ43ouYHPCBm06ZN6v5e/dinig+NmunjxVEvMDi+U6u+dEmzY6FQLODS+QGcO3cFg0N9mJ0fx7iMpeZSTTggfdgXnt2BPbs7EDFkbiZjhlgsLvORnYgnZPZQLHlf49S3o2bXo+joqEMbv6bJZJB2Imjo6MW2rT1oaODXJBqycymZp9YisWU/anq6Zb7nolXjF1rSK4SqVRkqKSxl6pWrJ5M3Gir7fPYNKzK3f+edd9QhY+SL9vZ2de/3KcRa/qh8/tf/6l+pK7tEFbJVjuBXhZ9QghFalkz8hGmJP//zP1en65GZ//iP/9g7eU5QydD+/aeByrQSLNi1ZmtBN8wTT6tjOnkiE09K8NNcmY+PwieZT7/cKuPlPdPJ9A0PD+NP//RPZTA1hueeew5/+Id/qMxpT6bx0+L74TPN/fxycMJ7Di452OTEleY0ozuGxSv90pzh0C2J9zy1kJMlTnIJMisH+T7TMkyGURkXzemf/DM7O4vV1VV1IiPBkzCoPGUYPMGP5jx5kelinfD0K/rlPcPmlXli+JxwUwlIfzxlsqamRk3iGA+Jfhk/T9FiQ2Oa/XAbGhoU39I907e2bOjfrwcSQbPKMmVYDNNPA+NjOTB8P80kuqV9Op1WaVlNZ5HO5pGQuJsk70x3IhGXiZinUFHx8ZtviUud2iFporkR8uqH+4aII6XYyuaLSK1KmFKmDJ9+GR5Pj2TemCbGT3PWG8l3w/yz3AjG5ZcX7+mG/phnXn1+YD6Yf9Yb88aT7VgPLAfaM98Mk+XAOOifPEN71ivDpT3r2y8juiEYFifkLE+a+emnO15Z/zRnPOQTliWJ/giG6dcpwyVYp0wz/VRX05wHHMgEw+apfEUVV44bw4kZ/XDfNZWmsMc/VALq7PD8Ji4doDzJzcbsYH7dYP35V/Lb1atX8frrryt59K1vfQvHjx9X9Ut7ljNpI8BPtw9OMmnGAxlUWsuTW+7FY1klxTfMH/mDq8F4Em0snlC8laiqRrTMi0oWlP1WYm2+P8tyYP7Yfv22wxdWHHRwYMoTCn/v935PDTwoWzZavf2qUHVcpkr4cs6Xa8wv2z1ljV8OdEPQzpcjlIU0p+wn6IdEPzQv5PLKry/beJ/OpDG/sKBkFf1TdlJW8cq2Qt7iHoWVSSQ/Us749VBZJ/51o4N5Z1r9K8Ey8p/ZH/z+7/++ktnf/va38dhjj93ujyp5cSOCaasEn5k3n/jsyQ6Pz3wz5ov9CuueVz9/lVefNgLW1oGfT+aD+O53v6vmA6zLP/qjP8Lv/M7vqPZEPic2Ul4+U3iiRArE2wxbSlVI5IPDFeieVSkkY3G1kbXwiEyCiULIG9uEXe4k6o85yrxneQpiVwJwdOEzCdPfkkUHTzxnLN5IhSp/tc2JI/Y+6ypFbTlhXAkrVertROsiIe54SJJITpgGQ9ZgmDL2FL+WxGeFvE/7+XJWcQKDYbhcIcNDOFjnahsI6XN4K3c6THFLuSnjSXUmeCVknsAcuOLY8vKQkwv3YQ3zuxt+/i28pzZCYsROTPIsMjckZckyVWBOZewuZaXCkfC89DD+qHKhFvBIEI7uqhdejJe5JHiwDXPFz40j/KaMQajPzCWHvA+wLigTSATbOuXDd77zHbz66qtqzP7888/j5MmT6p52G1kmMH0+/DxVgmbp1Kqaz3B8mMvnVP+t5pMy51InLso4i+GUiiWVT467jLI85BYK/JLGn1tpMr/guILjC7rluIHmhD8fVf7ptlxu9LtRy289+GXKNDNPVIb+yZ/8iTq9+sSJEzh8+LDSAfj5Zhn7/QfB58r8cq9xIlB6/RKgPw5ICHbifnr98CoL/tOCX26VefLTyTR+XKUX4Yflg25INKdbNjDekyl9t5V59s0rw+UzeYFEM8bt+6FdJeP6cVW68dPgNwTa+fZ06/ujPc0ZB80IPx18pj3veWVaaFcZj3+tDM+P03fr58m/+u5YLjTz4/JR6d+3ox9/AsS8+/H6oDua+W5V2UnHzbe/PMo2EmZauEm+hFn2Q0joyg8VW1xyy7cN3EhfY/h0yHQJcZ8pWyblDJtEMB1+Wfh5I2hPocNwK9PKZ9776WQ+K8180L9fBgyfRHeVcfvl5uebV98N/fp2hG9PrHVHVMZN+8rw6MaPl88E7f18+X5p55MyKheHpELC8PN0h/e9sD2eNdRKSabXC0f+l4np8Qb9Dxq8cvCu97/SizeeOcf8HuRZKZxFXoid+nE/BbqTQbZqV+W2pRhDoAbja7BR8k0w7eRztg3KnwdJ6bUefF6gDPGJ+fVlmo9KnuE93flyheVIKH6okDXiyCtDMfPfvPLFRaksd30Zw6svq8TH7TSwH/CxXg3cT/WiykHS618J5tN/vp+VXuuB6a2kSn7hsw+aMV/3yttGyjPTXZkeP19+OwmUXh8T3pBGCuTeSq+iUnpx79oQYpanpMmH86oPiogZlTkeyrxkeYox1+AJ4r7Sy1OEhT5RpRdlnUzIqfRyZC5oUOlVnjdBJuRUMt3OH5VFlUovbgvBlDANH1R60dzjjo9SepkSh7gmEW48UHptEPjyjmBbp3y4X5VelaiU2T5UXoUHmQ/26yo/IusoD1WfXyHv1YIF8hPHCMpUzMm/YqdyT7dywzA4PmOZqHDKZeOF4TUsv8x8up9QmYdPUul1x0WAu5jjo0gxJJl1Hbv7HX4eyDQE80nGIvmDlvXyzGulH977CgYyMM04OKUQ8xVEPqP6YRB8rixfgnH7q3ZIPqP7YRP04791p31lOD7xmXHSnuHQPc3XA80Zlh+n/2aeafLJD5Ph+WbEWjck3jNuP88Mk+XBOBhGJfluCT+tXNVVXS3XOPMo+aPCS6K7m8rxlcPhaYmewovpqnAooDvmiaurSJV1wjJdGz/T6peBnx//ejveimcSQTOG4ZcRw/b5geGR/DLw/fjxV7qhf9/MD5/PvNI/+aMyff7VB93RjG6YF5+YNz9uP8/05xMnoSo++XHPO5p58ZXTFZK8CdGMCi/l1svGbXhmawwD3HdgDbIaudeTUibfJql34aGQtEvyQUQoFosiGr9bbqhxspAXTqV/jwJsXPh1xPbP+mQ9k/j8Yaj058vBtX4op+/IICpOvUG+L3d92cb4fHdemHdksUcBX21k+P1LJVg/rEMS69bnjbX15/ebJKLS3ncT4HMGViuJiiAnKvwT5m5B6tAhuHLHE8P5ItSNqkMsciFLyFaKpigPEXI0FMV/SfiD9txwQzwIyfhK8ybRHNEbYqRITES6SHgyFnRjEn5Y4hd+00244k8dSE6H4t82HGSEVzMyjeR2LtVC3CZF9W8MSybqhsgxS/yUqFOTMMLIixtvFRr3FqKOSZFSIXGFq1y1VaFlcZEWs6Jy4NqSFieiwmWaqeiiMoy7KIutmJA8eOYl9fm6JmUGKRu1kY8iKgkcVWYhMSeVJNclCUXpxYRYKiwr7qKk4mNzKyvlZEaj7JleHh5C4tFlEddSeVV73EgebFXeVP0FeNCwVi77RHChAvvyynmHMD0czmPJP+JMzdnoxwtM+Stf1E1lmH6/4T/7qOxL1to96Lh75PWAwWcGnzgg+ThE+NdK+OF8HlCZVz9ffgOqRGWeK/0Qvl0lfZS5f10vrrXw/VYSUZmOe6XHf67Ees9rqdK8EpVmfvxr414L5pGoHMz6ftaPQ/7RWojO+FjpQllXxHsnDCGaKVI2tLxt78dT+eybEQyPaatUMNK+so58P2vrzTdfa+df/fSSKt1WUqUbhsGrD9oTvr0P35yovCd8t777tf4q3Xt2QmUnlUHR6k44kj9leXd6Pdwdf4D7G14te/9u13XFmziP5D95SfjV53tlRpQvAe4P3GnHd8D6vF2vQrf5YI3bSntfdhKV7jx2kGe6vf2743dt+IqUP0/meK6lH1HKsg+mNcDGwgfqskw+1vahvl0lPwR4QKAEAW88ZQqVQpQiDjUxnCSrNUb8UWmkweJKJKGQLZNem2a6OkWa5KqXdxIOV2dRIySgTzEV3zIhF+I9if89DRfHqOJW4vMVVEoTJP55T2UaFUaMKSzEqw/6ZDSO3JDoLwRLovfSTJd3XPPZywOo6BJy1eourshnxGKn0kO3dM0wSHeH4qFsp6zKOWObUcRxJmORHIqdJkT1GdfWqGYmRFuPWAaemVfWXAEm+RY7poD2JC/ljlekTKtzJ2UBHlysle1KdiveKbPUGrnutTvvnqTsy27IbzRTuG12x69vtzbMSrsAHiiKAvwSeBCYqTJ/6+XVLwOffDMO2vyBG6/UOPtvp30hQKKdv/rHR6XfD8PasH0/lf7WPvvw37T79qSPitNP872w1u9Hub1XXL5dJd2GBMknnyrhP38wnZU+yiRhMr9+nn33vK80r4y7MlzfrtKe+DBz4sP8+8+VcVfaE3z2V3uRKu3Xhu3Df15r7odRibVufCi36o52H7SvLNr1sE6QAe4TfIAfFN+U7++CGPrmt/0IP/G3lq/W4b0A9y/8urxXna6t/w88i8wTA3WvJpUyKfXNKsP0/Size/HPPYwDbAxU1rsP1ufaevb7YZI/xvFpLf8E+PyCIw/v54GKHLVQS0xsrrbSPUU6zQwRHtzIOix9ji0G/AyPXOKtapJxldwzHEf+K19lFuKFKhqSciBheAqj8qP8PD8+UalDhZCGiNyRPLWXkAqMnw5aKGq6IletvCoqX2otmSskt0pvJyY0ZRxaWYnHjxlJmhOGTsWdBGpKuFxnpfFzRSGmVn1gWF5ZpXLBAKU8mFPJsddGmBGljSorv+hOxXoHnASTaEP3Xpq81KoH1TbliavrlM0auFx1Z3lXZatKUvm/O6YADwrWGwuouY2Qb0M35NG75LqY80WW/xUBocwVW8k/RcpYmfvzJR+e2zt+A3wQbOsByqhkmI8if0DCe8IfuPh0v8PPZyXWmq33vF6Z+Fhr/nHLif58t7z3aW0YfvgE79fWUSXW+vWf15oTa+0qifDTU4n1zAjfnOT7XzugJdaGTeLG6LdXaYszuvTJh+/WexCH61G52a/Nh4+15gyPyqaP8ynPvVAZpk9enu7UEc18t5Ur3/w8VbohKt0TtCf85/Xqns80Z1n7ys/KNBCV4dGd96ZRGSkzn1gf3mb1JNr5dMcN6Q4q7wPcL6isyzIbKH5gbd6uY5LwkNfGys90Ju7u8Kzwvfy49xspwP0BVb8VuF3ngjt1e8f8w8iXM5VU9nybtxjmWvJlFul2GJ7j231ASHgvRB4MsKGxtu4rn0msb9/c75v8Oq/kiQCff9jgnluOaucUEDoVTQ4VWzZKhq02i6d6JSxOYnIbd0KIi5uiGJDIMxFHhyF+qP+xheX4aSRPHqYCi4FS2eST0lqR6N4LWqXAUuQo8lZG8bNHA1ViQmKKHETFq4QZKsDWS1gVe5KDrPjgR5CWZCMiiYgiZIozU/pBcW+rVWOUY4zQRgERfgQJzaqCUYrClvTnQkBB3GluXtKVhyNp9PbSKu83JvmGLv4l0SFN7RimFAf8DNNTenEfs4jEw/5ZbpnOclb5SSdJnbYnRDNTnpkriUClyf+8UZPw6Z3wSo//SuKuIFcqviQdEgddkZR9gAcCHymbfcYR0I0v7/1ntVK78kuaCnu5EbbyiPeekWd/241g7XOADyIYIQX4WFjboCuffapUVBB+46t8XjuII3z/PvxnPyzSeg15rRnd+5/gVaajEvTj2/vPlempTB+pEveyX5sOPlea+feV6alMqw8/r376SL4f346PHJuoSTOt7gSp4MddGb8P8a3+q/tyuHTHfKxNox9GZfoqQXdr07mWKs39eNaWXSXohm79e98d733w/q6JX4W7e8FPS2V61qLSDYl140MdGFCRjkr/vF9bjx8E/d3JW4D7F8Jxwgfq5i5U8qjXxO48V/IplRLkJ9KHgbwS8Mv9A7+OK+HX4Xp16Zv58oao5JNKmbbW71rcK+yP8hfgs4df55W8U9nXfBiCeg5wG+QBssFtfpCr+qlbBRpT0vg2Mhq6/VODStJalP1+FNZzxtA8Ykzef+VSXeQf5d5tj2U7IZWeNVhr4rnxyYfXZlSb4I9x+ESUm5Tvg1f/3oP3dLfZvXHb/8f1EOBzjUpZvh75fML7tTKed9yjubLP98cGip/LBM77yi9Mace5B0nZleH7rTQLcAcfPvJ+wOAz1kfRWkYkVTJ3JTPf7/DzV4n18kvyB+q8J3wzXtcLx8cHBIDcV/r17ei/UhAQlXa85+qdSqXIeqAd3VTa++lj2ITF0xKF/OfK8Gh2L4XVWvhma+0Ynp9WotLeT996eeATjby3AGUDAf0zPZVp8sGQaSol5L2BEgPerwXDYHyV5KeP4VaWh2/HNPrpXEuV5gzbLzPe+8/rCexKv76Z74/gSR6VafHt/Wc/TT788CrTQ1SGW+mG+fLz7cEv6A8qrujPMFgOd5Spfph3g/EG4vZ+B1nH54ZKsL5Z5VRGq5oXh2xjPo/dxRu8Ct8H2Ljw2/BaqsTaZx9r3fsyx5c7hP/syyme5EtaKw99mUXQzpd7a8P2Uem30jzAxoDPF5X1dC/47tbWt88zPoJ6/vxCWrf6qZmakBNyUQpxxZWBuB1FTEjTs7DD82KXEgciLyyudNIR5ud/whumDGUcjac7riJiryq/JiIyFhR7CdYbC3oRuDKOIfnxkZzyWigZMSuiscdxDjQnp8j/aMvSwihqVXKNod7OC6XFLbevjyGDBFa1BDIy7qVfUtjmKjXhb5RQ1HPiz0KNW4Uau17iDsGMQH3ZUCXdZUzaQMkoKjLcIiKWA92W8awkxlaJ8tLADeVDDtemOciJXYHjLi86aUc89dY7GZKfTHKz+ZiTUcQ82eKW+5/xnkFy831vVRhXifHkSJYq17nZiCKNuJuWuKSA7SoJOw5bbktCjIXEUUCAAIRIc7Way5frlbJdyfUyKd7jfXk+QjufxMIjuhE7f65S2QeosCrGDQHuhmrXATz4jPVRtJYRSZ9H+AMt4l75rWzAlVhrXulvrR3B+8rBXSV8t/RfKQgqURn+Wvj+14Jmdwmdctg084VJZVx+ODTz7T4KfrwflT7iw9ysa8f0cJJd1vz76V8P4lv9JDeeYC2Hxbgry8CHb04i/DzfK310v5YqzenPTx/vSX4Z895356fff/bh+yEqFZsEzf2wfX+VfivNKonw0/Nh8MuH8NNRqcDzzf003CtM322A+xs+//hE+HxRWfdreaKSyL8fBj+8AJ8NWEd+HVRSJT7KnGEQle2e95Vyg6DbtSdBruUtwuebtfFVwo/7w9wE+Ozwi9SP787nxUr4dmvNAzx4IAes5QLhjA+YCbMo8t179mWXZbtPEuuFRjNlfju+tWMiPleYrXm8G+u59ftl3sq1/PPslKsAAT5xVPbX90KlLPdprWz/OOEQ67n5OP4CyDiqfA0Q4AOobJz3wr3c3MucWM9uPTMf9zL/uPgw/x8W31p/a58rcS+7e7lfi4/rzuu5y8KNcXqXe/qvFIO+T9/MT7NPlVjPfD13PirdV7pbz2w9rLVb66/Sfu1zJXzz9dyvRx8H67mt7Lw+Ln4RtwE2Lvx6/0XrP8CDh/V4ZK2Z/7weVeLD7AIECPD5g7R09ZMGr/aa8syE+KA2cecaKxfc/t2xs3DTM8hNT2MxqyPreCuaAAu6kwFys0BqAtm8g4IFlBwHluvAFjc+WQihJKFZ8t/VCzLQEb/g1vhhb0N8hy8oxQ/jc23x78r9HdIsE+FCDkYmDWtmDreu9mHw7DXcuCDXsXnM5CykJZ7lsA4z7K000xxXhW24EYkrAlNzYepFoDiHwsIgJifHMTidwXxag2HXQDe5dX4BdigtaS5KvBzTajB5EqMmZOaQT81h9tYcxobSWJx3UAxJcAzT5d5iaSmPktpXjFuiFblaDNwfzIMu5WLYllrNZbslWE4BJSnvohOWMtPVah1N4teyM1ieuokbl4cwNJzCSg7I6y6KmtrxTIUjhRUoIx4AfFJ98scNYz13wZjg4yFQegXYMPi0Gy3j86kSn2Q6Pk5Yv1J8yu/6/j9uV3uv+Gn+SZbFR+GTiuuTTvN64X3aZRMgQID7H4HcCBAgwMcFlTkeyb3aZF3ulBKFV2UIx7VgOkWk00sYunEJ773+Bs5c7MPETBa5ovhxxD6/itziFG4NXkdf/zhm5zIolByl6PFC8+LxNmBnsPJfbd5OF7qY6moTfRJd8qfsKMs0Kt48maaXSjAXFjA/MIDL776HUz9/DW+9/CpOvf423nrnDN67dA0Dk3PIOI767NLlFJRfKthy50gc6uNBF7aEXcwtY2qsD1euXMblG8OYXcpK/FFxE5VoWRZFpZyzxT+D4KecahN5q4i52Vu4cfUGLl/ox/jYHAqWJWEyT6YkuwjdNtW+98ys+ghR8z4FVXkgSRlrjqfKY9ZYLurESglfubJLcM0MLp9/Fy/88EW89dY5TM4swhJLlifLSH3yWVZ4BYqvAB8Xwfjg14tA6RUgQIAAAQIECBAgQIAAGwRKueST/Ck9k7q6sOTGKp/C6FgmVuZmcfbdU/jO3/0NvvOjV3D6ygQWU3nYYmfl01iZnsCNKxdw9vw1jE0sI5+3ZYJ9ZwqoFibJlWotNe+mkkipwMooa8i4L1ZZNYSQzn2+XIScAkJWHsWVBYzfvI6333gTL75/FTcml7G6soTc4jRGLr2Pd176Ed56/XWMTq8i5Uq6daaepzo6sJUCT5e8GQjZBkzTQiq9ioX5OSwvzKGQTSvlHk9jVOctutxrjOllGJJSebDkCklRPlvE4twS5mYWkE7nxJ+Uk8TnKQ15yiLPZpR75lk34GghuTXFb0nMPRWXKhCBpg6d8RURYuvosCStkLT0X7+Et069h/MX+zAzvyJ58NLi2kpFFigwAgTYYLgj8QIECHAfwOvmPw7WuvSf15oH+FWghjhrKMDnF/eu50qb9V34+HDbAAECBAgQgP0EfxyvqfVWrgbD8ahguIqouDIKNvKzcxi8egEv//SH+M4Lb+KVs/0Yn1mBbZeg2Vmk58cx0X8JfQNjmJlfRaHINU4SA5VPXPHkeEojz5QKn5JYil/pqkjKSK5cw8TPAXlV68LsIkLmErTsNOYn+vD+u2/ixy+9jAupKJoOfxlf+eLT+PLR3egNpTFz9mW8+qO/w8tnhjHl6DDdggReVMq7gqsjV5RYMw6sNFdY6aiurUFbWzPam+oQD2vI2xnYVgFW0YWZdWHlSzBLWeSLeaQKBSwLaXocddXNaK3vRFtDNxrq2hGKRlDSLCmLIhwrrz6BtEp5FNIFrBZ1pIoStpWD7WagOXnAzMMs5lAsFpDKrSKTyyOXN4WknE0NlsShS1qQX5JylHRbSRScKEqOiSKVZ0phFoyyA9yBP+oj/bL4Vf0HCJReAQIECBAgQIAAAQIECLDxUaFP4UquYiGvTn/V1aokwJyYxGj/AKanp1HI5eBYFgqFIlZXV1EqFtUpsFxd5U+iqaPhoiTu1uWp2cSUf1wdpa4qWGXGTwkVqWe5kTjpbmlpCSOjoxgaGsLy8jI2b96MY8eOYffhw9h36BAOHDiIzs5OrKykcPbsWWSzgJUvoJhOIyeUTq9ifm4e/f2DuHz5GmZmZ1SUVVXVqE4m5VqF6niVMpu9NYFrFy/g7Pvv48zZc7hw+TImJyXPEn9uZQU8JiYejysyImGV1qL88qllpOfnkZqdxczIKC6evoSz56YkzTkpmyJs24FVKmJlbg5D16/hosTx1qm3JT03xc0tzM4tSTkXvRVctq3SVN/QgJqaGkTCYVUehvx0w4DLE5pZUAECBNgwCJReAQLcT+BgZz36EPyCzgP8wuDAZi0F+Pzi49fzB118fL8BHhxUckUlfSz8Up4CBAiw8cHPC7maShq2RUWTi5LhohhyEXZ0RFwhcwVRcwZarITMlm1ofOIZHOioR8vMKMZv9OHczBKmjRhqqpMy4dPhxnSYBjewd5RyKOqQSojKbDDKVWRuCLoTh2YnoTnVkGgUubo41G2ENRdRGUTqroGCWS8DSg3aUj8WT/8Q56+cw/XqdrT95u/jn/zBt9G9I45UbRVCHXV49vEd+D98aR/+aXcVBi8v4tYAkAllMbh4Da+9/gb+5v/7A/zpv/0z/Kv//J/xH3/2Ewy+eQOFi3OYmZjE+ZWbuLbaD31lGMWhs3j1Z+fwX/7Lq/hP/+G/4r/86b/Fn/2b/wf+b//3f4dXXr+AmZk5rCwtYGRyElfE7+xyCoY5Dnd6Gu+8cgl//9dv4i/+9sf4zz/4S/z7v/63+P/8n/9X+P7/+1/jvXM3MbgawnTWxkj/DfzkB9/DX/7Ff8Wf/4c/w5/+v/4H/Kd/9//ET376E1waX8FciSXHlWZ5rOZLyBYdOLaGiJhyO36oPcLu7BMWIEAlPtBNV/bfPgX4tSBQegUIECBAgAABAgQIECDABgL32KqE/+LS06fIv3AEbigEx3aUkqWquhqPP/6EWlV1+fIlvPfee8gX8ojFYjDEnVq5xaVdcvVD5solp1RSK7ZM7gEm945pwrUtlEokG7bcm2JWKNry7PuVQBhWJoOZiXHcmryl5us9Pd2oSWrQxVEkFIUuadRqkqhqa0NrS4s4zyKbMVGUgCZuTeDVV1/Fd7/zXVy6eBn79x/A17/+dWzu3YRCoYCBgQH0DfSjVCzASa3gpy+8gGtXr2Hb9u34xje+gePHjyOTTuPq1atqVVhNQz0y2Ryu3biG8xfOY25+XuUrlUphoH9AxcWVZolEAs995SvYvn0H+vtu4r1338PQ0DCKxZLYxdHa2irl+Dj+xb/4X6v01NbW4Oq1a3hb3OXyqtBuF6Cm65JXtXU9TLukVtLpUtbBnl4BAmwsBEqvAAE+92BXvJYC/OoIyjKAB58LfI4IOCPAp4KAyQIE+NyCzZuru6io4oPmaAiRoCGr6choGkw3jbA1h3CxgHxhC1yjG4cfa8OBR+qRyS/g8sVhDPUvIZXOw9UjcEI2HMPmUi3v8zvblKAtFFYWcOn0Gbz72ts49cp7eOfVszj1+mm8+sbP8eqbL+PVU6/hlbdexfnLlzE1t4QCv94zdBQRhVuMo5iPwSraiIdMtCXDqJfZZUKSTb1PRnOQRxhGtB7Vda2oNVOIZxdRMrPI2XlkC0CpWIea2k04+Nh+7Nrdjtpq7ts1i9mZGczMlVAsxaCtFjFxcxi5lRw2d23GscOHsG97N2rjBnKrUSQTvQgnbOTtW5hamsLwfB4pM4yEtSrxzSCzWEI6n0CkcQt6jzyBfU88hi9sz2F31QAWUiYGF2NYtRJobW3Bww8fxdFDR7Gtdyvam2oRMwpYXp7H0OQKMtz8TPLPDfX5KajjcGN8B1Gpk4hmwNF12JJxVluAAD7W5Yd7Mckacz76FOCXR6D0ChDggUIgOgME+HXgo1tU0OYCBAgQIMDHw10jNbnh6Y06lS2uhiI0ddag4xYR0nJqVVWxVActVI/Wzjh27W9HV3crMmkTV68MYWx8ErajQTMkjLA4ltmfY9tqvy/XtbG6tIALZ8/i3bfexqnX38GpN97HqTffw+tvvi70Kt58+028ceoNnL98CbemZ5Er2nAlUkeLSEARWKYB2+aeVhbiEnZY0ml4C8pgSjptiVgzEjAicUTMLOION7G3xdxGvLoW3d27sXPnIXRu7kB1jYFqCUSXvHHVlOmEYdlhlf+QRX2dDtt0UMhmUMymEAkByepWJOJNUhZSKnpW0mWj6EaljMKIWDlE7byUnYG6hi707jyI3j0HUd/egX2dOvZ3UWUVwVIhioIr7iNhGGEDqaUUhgcGMDM1gVx6EcViDtkS88P60BAKGdClDFyqJh1+LqrB0EMSty4mFXUXIEAZAU98tgiUXgECPFDgcutgyfUnB788KynA5xvr13MlB9zbhX/9oG2AAAECBAjgg+qU2z2F6jYcOJoFBybC8mgI6W5I/iWAcBw2SmJjworUoa5zC47s24nuKgfj186jv38Uts2VXtUw9SpY4tt2XUWQMBxHR6mQ9VZfWVmsCmWKWbXZvJUvokQq8tNHKqK46bul9gQzNElJqARXz0NzqRGyYZkuLBuKQo6LmO2q9HJfsJJjISVTz2KsCjFdR9x2UB1LoqljE9p6tyKRiEhWbcSiYYSNEMKhCIxQDC7zWSXumxJI51Zw7tI5/PS1N/DG+atYzNvo7mpCXXWY++pD10OIhmNIGAmELDGQtHLFWSikoa62Gu0tjWiqr4Khm6iubURtQwsSUrbxUh5ONoOJ6Vt457138NLr7+Pdc9cxMT6ObGoZrlVSeeYiOYSoPQxJnnQ41DhqLnTHFjKpAlO7sQUIUAnVhL3bXwq/qv8A0mTL1wABAnxu4YvKtRTgV8N6ZepTgM8n1q/ntaaVdDfubRPgwUUlV1TSR+KX8hQgQID7AVRq8QM6XWmX+DmhA9sowNYLqHJdJF0xduJw3BrYmlyNIpZKS1gyepCt6sGhTc14JJmCO3Ye12/cQj5fjVW0IOU2I4c4bO47FaKSKYaGhi48fHgPnjp5BMe/dAwHv/gwjjx9FF954gS+8vhJPPXYCTzz1LM4evQQunsakYh74ibkGtASGUQbCqiOOwiXbKRXCihx430HSuFVXTIRKWZQyC9jMb+C+WQjUo2NqBa7FtuRlESRC9UjH6lDLMQ1UgW4dhG6a0HjLvpmDJobgV1Xgt1oY2xmEK+9+3P8w2uv4+UbM1iJt+AAV7Y1A+FYGCUqpSwDVXaVxMvt5dVHonI15bYg4WYRkZIw3EU44SQKbhRNdhat2XnkJ0fw3tl38b0ffR+nLk9hVWtBMlGFuogr6bRg2DZCtgY3HJV4dOQl3CLrRyjmFBE2c3A0rsJTX0AGCKBwz256rUUlVeAexgF+QQRKrwABAgQIECBAgAABAgS4H8AFWryGvBVblmkiEo4iEokgtbKCsGGgt7cHW7ZuEbMobvb14eLFi8jl8mrFk/q8kauTQrracD1WVYXjjz6Kp546gRMnT+Ik6emn8bTQyZNPK7MTJ07g4IEDaGttQzgcUYdKKojftq5utLe3q83uBweHkV51y4uhQtAkTblMFmM3b+LmjZvokXS1tOow+F2iwOGKM9uCJWTbtiSNU1NO7yUMXdxJXhzHwcLiotqQvquzCydPnMTXvvY1fOtb38J//3/87/Htb38bO3Y0Q7OLsCUNIcmXYYRVOhkWV3rxs0UGyzgs20S2mEFJ3EZjMeV+aXkZIyMjGB0dwbLc79u7D88/9xyefeZZ7Nq1CzXJpArHsiS9uZz6tJHlHZZwmVpu/l8JmgUIEGDjIFB6BQgQIECAAAECBAgQIMAGgYuIR2ozrwI03ZRJm6GIRhqXEtn8lE6HGQIcewVuPgVki6hyXNQ2NWLroYPYe/QwCpqLty/fwPLECOJmEUlNQ0SdOOjAtUtAXMJNJBAXSsarUBuvFkoilkwizpMXq6qQIMXDiBmOpMBE3JVkmQ6s6ofQcuh3sf/IU9gcz2H6/PfwNy9+H6+cG8bN99/CpdffxosvX8aPTqcwUWjDN5/swuZqIFxagp2ZxUxhBTdtC1MWEE3XolNS5YYWkMEkFvO3MLcyjZX0Mox5A/FUAmEni9bmKPZu68berk7UhuPQjCqML0qZREPQ9SIWpycwNjSCrC7T3FBaUruK1HIWS4sFrJZcmPGERFYDqwCsLGSwkkshY2eRtQso2Dbiku8d3VtQE6nCXGYRQ4sTWFpdRqKgI1HSEGqMY9FOY3l2FqW5FWhFKcOYFEjU00ZS1RZMsAME2FgI2mSAAAECBAgQIECAAAECbFhU7vHlrV7SuIlVKKRWSxUK3BweCIcNWDY3udfQ2NyI3bt2q9VR/N7Q5L5clq3c061OpRDvuS+VXF2e6MhnFUeZqIRS1zvQxYLxU8GjhQw0NLVgy5at2LplM8KSpr//+7/HX/7lf8V3v/sP+Ju/+Wv84Ac/QF//ABqbmrF/317UVUkYtgnH5lGIDNCLzJH4eec4kkYh13UkeyEkEnHU1tUjmUxianoSb7z5Bn4oYf61hP1v/s2/wb/7d/8O585fRjadgVrIFo/DSSRUeH5CbdtR+30xe8VigblSK9MKhSI0KYeEuK+vr0MinsDY6Bj+/jvfwfe++128+tpruHzlGmZmFmBbFqIRFyWzBFPuuUqOAXKlmipTgRjLvSqaAAECbCAESq8AAQIECBAgQIAAAQIE2HDgVC0MzSVpCAnpmiPkAqE6hOK9aGzZjmOH9+OrX3wKOze1oj5mwAhXI1HfjW37j+Crv/1P8Du//0187eTj2NtZi7qo2oZKncDoRkJw5Edtk8afBMvN2jUqweiGOqPylX7CLjdst2DLs2PIPyMOI9GAps5t2PfQkzjxzJfwyK4W1GIZeUmzHRO77t04fPwZfOELX8bhre2oDXF1WScaNh3HsWN78BtPVuOJvSE0hyPQnAZYTQdRc+BLOP74cXztYB121Swjt7ykPitMdB5B3ZYn0NW5GVtrHTQ6c1iduoK+6+fQPxuD3fgkjp14Ct/6WgP2d89LOncjUnccO544goe/dBj7dvWgzY2gWatBaPshdD35ZTx8/CEc3tuLXdu34MChRyUPX0FPZwTRSBp1jZtx4Ohv4EtfeR4nHu9AfVUBTmg7du37DXz1uSdw8vFOdLXHoek1sN0EoiEHhtQPDyIIECDAxkGg9AoQIECAAAECBAgQIECADQdO1ahuCimlFFdZcWGUWumFKELhBjR3bMaTjx3Bb331GezY3I5kzEDIiCEUr0VL1yY889zz+Gd/8M/w9S8ewc7earGn3/IG72Ff6eUFquJw76wqU6obtVqKCjGeUujIVfmAHdLghniCYxTxumZs2nMIT3/5efx33/oNfO3ZR/H4iWfx7HO/ha9+83fw3Nd/A48cP4q22gQi/Cgz1oj2LYfwxGMP4Wsnt+GRfU2oDRuwS1UINW5F96ETePqZZ/HV4zvQXlXA+NAQxoSqmjdj//GncOLE43j66F48tKMDTUkNM1OjmF01kGjdhxPPPolv/dY+7N8WBYxOJJv24Yi4P/HcEziwZzsaJL01RhXqduzDnpNfxqOPH8eB3VuwfUsvjj78GP7bf/YH+G9++8t4+uRRPHXyK/jq1/9bfOOb38STj+5EMuFKdjtw6OiX8M3f+gqeObEXXZ310PQ4bCeKsM7y4Qq2QOkVIMBGQqD0ChAgQIAAAQIECBAgQICNiNv6E00tudJgQ+OmXmKuh2JI1tZjS0879uzcgub6KsQMuqFzA9GqWvRs3Yojxx7Bnq31aEqGEAm5cF21o5cK0vu8kFNC9eGiMvL83/6nQD9eWnT1OR9JKXh40mI0ikRzK3p37sHJJx/Hl545iZPPPouTX/winjrxOA4e3I7W5hqEJa6Q+A+FoqhraMGmnk3YsakXHc2N0Lg3mYQZi8fR2taOHdt3Y/vmnaiKJLH4/2fvP6PsOtLzYPQ5Z5/YudHIOQMkSJBgGg7JGU6QNKPRjCzZsizJlnWl66Vl66e9HH9oyf51v+V7P18HLfn+kCxbWRqKM6OZ4cwwB0SSYEIgcmjEbnTuPvnsc5/nrVPdGwcNMAGNBrmf7vfs2pXDW2+9Vbt27cIUzg0NoVIcQ1tQRFuOcWTaGSaPIJVGPpdDNpPGApZ/08ZVuHvbFixavABBOoVcWxvWrVuHzRs3YfGixUgmU6y/FNNfgpVrN2L12lVYTL+9C3qxavUaPPb4E/gp5v2xxx7Fgw/uwH077sPdd9+NVStX2OujqVSAVatWYts9W7F+3Sp0dbZZtah6rIIaWhKMESPGfEK86BUjRowYMWLEiBEjRowY8wS2fiJoDcVWVBJAyGmbFpoSJSRQAlJtaGT66NSBRo329TqyjTJyqCKVTKKRpHuqE8hk0cjl0BYm0K4D43nVBFBnZtWZgEXbXOpyrzdqt5e7p1fb1aUFskRDy1UZpp9mmgnU6TkZFmhfYDxAKdGGMrLI1EpYkNPh+O2oZHKop7TIFSJIhMgz3nwji0TQgTrzp6815sIK813VW5xI5RNopJOoKf9hgGytDX2ZJVh4z91Y8cD9CIsX8N5rz+GZ7/0Iz7zwOvYfPIOpYgWPPPQAVixbhGyakTTqVj915ksFrbBetJimatRZZw0VONRx8228z6sGWFR3vhhziToLnWIemAtAC4RJ1keQQCaVYBkaqNG7ymuLfajQQH+sp1SKF9ap6l71GyNGjPmDuE/GiBEjRowYMWLEiBEjxrxB80wtdxMxEDTLNawDOgteCzlBMolMKmWbjHRAe61acwfTm/8678uoVHToOm/pX4ewi1wazl80CYNzZPzuVUhbB9MKXK0O/dnSTirgbJIO/GcWkA7kXrWMaZJZqzdQ1eH5dbf7yRaf6KXOjGjnmA7TTwUp5j/QWftGOnTedpUx0iTL1N7VjW333It//x/+A/7Fv/jneOjhh7Fu/Xo88cQX7P7f/Jt/gyeffBLLFneiPavJrQ7CD5HJ5Kw+lIYW9eqsD10VpzKhg+6djSAT06WdDqxP0Y/CuX1vrtgNVnidZVPOmtYGVbPaQX4qdK/rEP6mW4wYMeYH4kWvGDFixIgRI0aMGDFi3FbY1/BiGHRovXZdJRJVJJIlztjqJK3otCGBDiQbHXaeVpimVaqBXKqGFEQ5ZIIOBCn6zSQQpoB6IodkpgP5VIIE6Px5nRGWTGjnVsNOC9MvEmmmlbKvGTJh/ifNT2D+kuaGdBbJdBptjSpyDe04yyJMdNJvFmnGq1cHw+wigJRn+AVBHe2ZOhJZ5p95DBivDspPMU9p5lW7x2y/WaJu62c6vSyXyCDbyNFvBmEmg2pnG8q9y5FetQWP330fvnX/g3jskUex9onHsebRR7H53u3o684xrRC9rINcModqajFKYL6CK8hkhy2/HazTVDKBEqkcpFilKWaJZU5oixbLR9JiVzbXxjzprLIc88n4ghIyrOMw2c4q6kQ2KLOeyy4c09KCXSZVot8Ssuk23rNcrDO/sBgjRozbj3jRK0aMGDFixIgRI0aMGDHmK7QC5gwzFFlPmTG2unmD27Nkd9PO3u0jYjq8IJOnJmyhZya9aZeIFwfn57rQopF2WyW0CEfSrrCOdnQtXoxFy5ejb9EitLV1IhkEdE7YhjNNbK9OWfXmX950ZLjBYlRrrmbCzZgMZuSPXV061/iJESPGvEC86BUjRowYMWLEiBEjRowY8wRakzFqcKrWSJECe73QvWIYIQ/vKHe38tP80V6ulJFfjwn5o1Ov7FU/hhFpp1dDfi1RH94b5dO9CqgXHe2tyVCnzgc0M5ziQJWknV9lVBmoQmrU+UOyXWvNP/2LGknGRNJNEKZt11VCt6QKDeVEHTXlVK9Asg4ajRypDY1cGkFXFrmOPNrSOdu5lW6ECPS6InOgly6VRLpRN3ug00jncoHp6cuUaVqnSI2AeSepuqz0VqfKnP6tpIxL8bHu6KOZPf7wnmQ1kqiZPyZAkj+lHiNGjPmGeNErRowYMWLEiBEjRowYMeYJtHTilk+ml2RIth5zLbyDaCZg8+IXtPTioLNxS1giF7ubDOpepmbgJlx03rdb9NGdW+RRnlyYBF2SqPBagw55r8lLJF8unibkltCCUQi9/pcMA6Nm5DoWHlW6h7YKptS08KSD50lavMrQJqVXLxWjX66TyeVHtilGJnsg58gW87SIRf+MVqSdYyLFo5BWxpZFL2VWr2C6spoT8+kW/HSnMrhdeMqBKEaMGPMRce+MESNGjBgxYsSIESNGjHkDLbiICFtpidq45Rct7ogc3F3Y/DM//He2fpeVLFxkbuFK5Lx6O3/btDK4OK4mvxXNR6ndXn4BzC09+Rh8CBer+3Xw15lIo1B8Lj9CkEiSlA6pWS0zweTLLWhN36pszVy4VF3tqYY8ZO/+hJnYhGaNEXS1hS2FbfqIGFRad+PTiBEjxnxEvOgVI0aMGDFixIgRI0aMGPMGVUf2ScMEGiTtgNLLdH4BR0s62m+kg+j9zqtaokY/9NVoNBektDAjH/Rph+HXFR3qvBfp9UORi01XvfrolnDsR/HwItKkUTHZDquAdyS9EmivBdIlRIZBUkgz/YxisvWg5lRTX4BkXJY2yS1RkSxiZVR+HLklM/c6YT1RR4IF0YuD6aY3VYkWvlT2tGzoB0l9LdLt7rKFKL1qGLq9Xg2rOe1CK/Mqs4PbyyUf8s/YrA55S0oyJu0Zc7XuwiltkTe4ek2RGE55sFcdXRQxYsSYX2hKohgxYsSIESNGjBgxYsSIEWN+QAtltbCGer1uu7xsvUkLTrZjrbm8NL0SdT3Ey1AxYnzWES96xYgRI0aMGDFixIgRI8a8QZqUcjM1250V2p4j229U1w6tAInGFJ2HaTOhALa2oz1WVdtnFQIJ7W6qzuzG0sHxjEvnaWk3lx1Ir8O37AAutzSk3VUiuZuFkRxJsmQmGvUQFRSMGs1dWjqTK6inETRStgNLsYR0U1btEPlEEjq/y16FpGuFOVfuGBXj5U+jzCKzHCLtmiKSjTTSjTbWQh5BUGcUDEFKBtrVlUCylqFXpVYx0q4thVRWfd5dljO8VuleopUK4PxUaBCF9pqnKprXJmyXHN0UjbKoex1+L3JtQhJ83dC3dq8phplYYsSIMV8QL3rFiBEjRowYMWLEiBEjxnzFdVdStAqjRZfZMLv99Xx/NCiW1pi0eNQ0fgjY643O0AQNtoOrCRr1Wud04f17jbbI1IS9H2mG5nUGth7VNDuTpxgxYnzWcNMXvbQN1d4j197T5r3bkursBe8m2Kp/y73g/c4prpGH7nhD99eEd9cY48kc5UfvcleN5hrROowiWu8aGOz9c/p1zzZIzXMCnB9Pzct0+fSj50t6XiJzxGk6mN6L11OWCs30F7Ldaa+aiJ4/MB1u2k7X+QcrkjNeH97TbDRtUBlVb67uHC+50jvSn+qFfSRC03Uz49HRLcBsOXJ/M3mfSV6/re2me2834/OD4f1Gw8f4NMLLJ109ednk3Tym5dW8RIRXm+yr7LosS0Y2z2AxszspZDaaz1D9h5xYtLZNtF28W5SimK9tGG2DGYreRRC1vsp5NodPSjE8PC9FeUr85HlK16S+uNY0C96v+Pb2wLWjHzWjNN26yqtN2DmmTpPuHQe6kdY8NsnB383YCLxTfBbepeTT9vG4uG4fPqwMUNv5Nm1tzxiqh+aWokSSvwlkeSeyrVSihO46eM1Ne21+4xBJnaWVSJGk9/Ni1apAOnMrad80zMhOG8pIOiTeR+vJsmCBXR58GvqCYsBURBavyLuZhc66cmdiyco5uJ1rclbcPp8ps6B7Unl1X1rM0r9MKTopWR8nEozDSGbayc0ScOFUS3YOl7zTXt6UliiJNrp00o1+FZyUoa3IzihTmGY4I5nNoFPDmFNL09tHQQvLpPzZCWOze/uMQv3a02yIuqnviyQPdPW6yO0B0/UyVlnQrSd3a+QgiSu9z5PunWyWJy+bbRbc0DxZOxNdeNnpr6F0poV3ySikPlk3V+LqBD+1UHv7MSBqjvKDt/uoUC+9JVCmlDllLJo5b6/rjfBB7rcEszCUFAn3pzw5O3cTIYMMUjy0xGMcO6dQfXkSWhnC3Uu54NW8uE6ZMEHtoA5nnc5juny+u4pc/NNOTYOFtbIz3qaA0Lbp6f5rcchPsy6bv47mL66bO+8QLUbUs5n148rtyq6r8+S9u/rQX1PomR9PTV8znm8hoom4HDlzNC/OZcbew9t5+ij4JGFjzDdEZdD14P34seHDhJk/UD7J+005Gc21k/szCo/6stxb6U5A65jt28vDt5vG8turlH50tLaHZJr+Zmw+CB/Fb4xbgSi/zQ/+c/ygPz9iejIX/2O6kYiyQmSu/OXF+3d2nq4Dc4r6c6RfxTET8+2F2sWTh9qrFbKLLmTe/vacL3B6OwWukRZmmutTkYUZ3dnylfNOOzvw3Yzy4JZ7ZqD7gH8uLi0qWYDmW5TONRKqmYVpg/JCB40BAWMQOfsZL+aHnrTcNWM9E7tz9fl05dIiGpJyd0thOhpeMWshzjzrqvC28CSyTDg3hTXfFpvz7sORXKoyZumepyP9Nt2Ujsii10+UDCqD8ixfSpdW027E9L0idAt9rV5iXAvxj9cpWq9eprfazz28RL1aZsk2Sg7er6SvJ907H97V5tiNqqOmvSS36YuSez6oNpDY5hQtedHVeXT0GcRs48bHgXrpTYVfnVXjKZOplFb1ZxjW23tzFLpvtZtTXNWvZsnHjfqdeZcHJ+jnGr5OW4WD7n17JDgwqGvVQ7/YxZzyoiAKpaoPrf49ebhyNX2RoszH++k209dWvD/F6+JxqbqQ7u5OxEwJjKLbr2eDVYH3oxtPs+FqN5dCS/wfkNzHx0zELt2rMWMnsStJzDv9G0lItwqi65Xxw8ClFOPOh5fl1yPByyav4AjR8WOuEc3fdUn+jJRHd+PtxPtOvkkOCjPhzMJIcUiBcT7mGyyvTbS2g+7VPp7kprbzO7kFXUXyOy/BbCqrnqI3Lu8zvDg7Ztws+E36i6EmYE00yd9Hrx5eZkTh/YgvhdYwtxpKLdqO7r5J3mDwY72nGVxrMxPsqihugNnimEtE26y1DaJugtrRywnZqU3nrdyIESPGx4bv67P179nsvDwQrhduTjCL0DWrD8yOPETJwZn0q3HKjVXOh/dH8kZbphVNW3ymEB0nBD9P+KRzBFfrtwBRRvWKsTKbTqcRBMFV7t4ctfNK9VwSEuxkOuRRV7K2/hyYr6bJoJsoGdgQDW0Y1pOEzKzx30pqrUPZRaF76YNJO8mS10Sa7ZJArQa2jRa79LQlQGBKIy3s07s0iuwzvvbMxblBh0FSKMnJ/GnFWjZue7Ftp05q6S9ECjWGojITpoyUuoWzHWcimWcv0+0ky2iTzM7+/OuHKiv/tPDlZZcnX2fT0I17jGZPgOxzyI6fnDcX0D1Favqxe9kTSsOnwwCt+fy45FrB8bl9zpr50ueqZUMPSMoP7UOQT+zpmQ4NdU8mQvJJIyHBIyVVIWZK4xA1O1h00+TzQbPcojTtFtOdSK1yaDaSbPfyvVWx0b2nD4PW9D8JRfN4PdLH0Ovsp1rYmu6a0/0gTfscSVe38JWgfEzSUzIkSXTSm+3pNP8fjNnyeSspWv8as307qOyCd9O9HmhpLNdV7endaxpUiNniv90kKWMbCqZJ92r7KDXbRkW+ilx4a0SSs745f7Pl9bNGvo+1wtt7Er/Jv+dD8Z6uuvf2QjTuW01qQzduu/x7lnGjuzObSTtUpA8ktdOEcoL3oZWLtmQtkQ+lWD18fNdAAUV0jabt05wtr7eS1A6Cb6tWEiQz/BzA36sNy+XydBze7YPQmn5MMcU0/yjaVz38veS1l92C+r7kgeSC7KVPiKJhPwg+7k9MFptkkR5mMl67J5o3UglMLTCdQJBfL/VFmv1yXkVrTb0l3/XCr5f/TMSWGzT/sl2E0qM0XdQw0eBcWkR90sU7g1nz+iki8YCunjd8mcUHuvc88nHw8ULdAMqYoEyJaavVqmXSZ9C7+wK1wrsLimMuyTEyf0judb3m4oauZj/jxRmapGI0zfInmi3+W00evm5FPj+iWq3eFB6OabTAlWLnog5pfc33K7+Dh0EcmZ03+z9nH8W0S9Nz9M98u38jd+MsWssxL4g5nCa7j/55N5ZM5WT7T5PuW8i1hXdnQBW7aTYyK//rTA5NxwiuyefHJJe28sdImxmJ/jUdZDKaNsxCfnfErNQst6tHT5G8tP5F3WK64+h68PJICymexB8K4yc9gld2RNfw0izUmv4nodnibyXH9M2L5//pvxl452nXGQtvc03cs9Fs+byV5OveUyaj81pc3ajNBN1rgqqxpHVhzIfz9/ORPgym26Apv4zYftP2N5lmy+dnjVqhevHXKIn3ogutCiuzruJF8V803rmg66HZ5R10o3dUSK1lEpm7Lte4ya5Jxof+xsfnGNTprPpzTqLZ8noryfKmtJvX60HzgmKxaCSz2q918Xym/Nen2fIQU0wxzS8SomYh6u5JfdrrFbqX/qGNMlHZ0CoDZqPWeD8J8cfILsp3K+mHac6Ql8e6VX6c9bRQ5o//M/lNR0luk97utunXx9P0K2peZsvnp4m8/Be8XTabNX7wfPBxoaMDf0+G3/09u3xiKHNRVCqV6Yy+8cYbOHz4MPr6+vD4448bMwueUT0pDl0/7MB3s8gdGOeOjCO7OZ5TvdtVfjxrOj/T9w3lV0R/9aZZO4Ka8c4FeSHhJyFRN9X9yMgI9u7dhdGxYWzatAkP7HiYyobCWQ+ivwRq1TqqtQoSgQ7j144m7cYgqUyc7zT400gWaE+hZDsaqGw2SqQizaq9rNsxJqWOPvQ+sj6VnFAeqhmrx0pQQ5ioI6A5aXUl65m8zhuyw/1ZZsub2lL1oWuz3XkfivRHjyqD8YRXaC2ciNWrzylrqZ9mkcUrszFZk79YXdJd5U9uIeNROzo+qzFenZcW2scBLD2S4vfX6xF/XJ5ayMWs8jB/zbzVkrJTu7C9rL21py/JNCgo2M4JK3OSeXALEu59c4YJxSfO/9XpqyzeTDeVc9qPyhVxmzV8THcazSazjY8jVCqVMDAwgLNnz2JsbAxbtmzB4sWLTU5JfnkZ5seB+URVyViSOkWgzsg+VJVM41+D/dx/FET9QvIiTMitRvnHiXhNT/woJ+lf7gmTf9emcTspWv+iWvPJmsbxoaEhnDt3DsPDw+jo6MC9996LfD5v7gqr9vJtpnBCNO75RU2ZLlJbmZn2ko+8mlw1s9zUls2rkfxKmKmsoqj8+rjk0v0sU5RfBM9XIvGkNxcKBXzve99DLpfD3XffjaVLlxrfRXnOX+eKJA8adfYZmqUdaWyVfoCwzrGUfV0Da5NfqKmhnNTeaZHCy53+alX6r6HGsmjMVbSOImk0edDrAPJnZPHIs3PXVXqXDzuXJKjtPLy97LyOevToURw6dMjsH374Ydx11122+CX32cLGFFNMdyZ5zHavvu77u+SC1gdOnTpluuC6deuwatUqM8uvHwMEH9dckJexdt+cn1HcyoL/lLfMv9cfVBLnX/MmyjqbLzm7ZIOzqbBKs2mEvAYIatIl9W8jhpF0xDopVUvRIaCZfl2hGZ5jHMPrPprHO4lcUWZ38ySeULv78UJzhitXrmDfvn027q9duxbLli0z/VP+POQ/iuj9f/qP/9Gun2zJ7AZQxgWfId0rA1qx1YqdL9BskP313G4lXLoz6c9Oco8S7ajAXGXXjG8uoXz4q+rWk4fVN/OZjtR/Oq3z1gLoEEm96pFKebtIWa5DM1A7O/Jujas9XFUfMrO2nMn8RV3nIRwbN2EibZos9yzDVWS8MBu54l6f5Mf1iWm6Ki4mdh1clcUWXM9N8fl4p9PQn7NwZG3kLh5Xxee9tOZ7FnJxMLTkwo0yHOOOxmxtL5K80Q4MyX8NVO3t7dM7gvTwwz/Rk52XXbPF00q3A1exb/TG9wddlL8Zq2ugYK1lmY1uB1T3aiffFjJL0RDJLPi28m0nf1JUpKDo6sf/+QhVq6tfb77e/Ww040aTizDGTYer3xn4OhfPdXd3T8sHz4Mi6TW6ym2uoez6PHoyvcrGcOaHZlHzwh9H5ld+pIBF7VpIcc3c31g2Rv3ONaL58PBmb6/2ic4PZPb3unq54/3fiGLEiDG/oT7tdQJv9uTtRNItRF6n8PLc9/P5IRdm12uuTt/lkT/6jxDDKmt2MzMmeLKwNg5EKRJ/JMidjGibX4/8GO75RG0v3vB1LHfv56NCJwxYK9aY0M2CMi0oc3p6owzL7v/8n/+DH/7wh1i9ejX+1b/6Vzbxifr1iJrnEmFCO5yYH71fKzKO8xWrfJLsDCtbd23WnK5sDPrX2VdsDmcVuPOP5gqqR9WbvwqagIgkQPr7+/H7v/9fcf7COXz9a9/AP/pHv077NGpVPX0To7l6TyTraCQmLTwaGVKaEbW5a7LM2c6gOdXCTv5S6WyUSdq9FaCcbKc/IFuvMS5OfrTLgXWVZL2kq/aRZZQzil+7JAIEIbmPWW0EviLnDxI6x8zAurH2VruTBOVZV/7oya3xiNp/GrKTD7YFf5PaSdW0MTd3S8jANps2N8H6MVtL15PCU0G0M0Ec3LvkDpHQ05i2a/qL+tEzBSsX82+8y7jrTQ9691ykZT09ZRACFO2qM410npeVjf1FQXSW3bU5iN67nnSNF5+xGJ8p6PWkI0eO4MUXX8Tp06fxy7/8y3jwwQdNyfFP87xyM5fQ4PpBqJH11Z3T7CwZPaUjD09lxcdU2uigfpNQf7W+20DVBuYEspU0ZV4StaCGSsZ9qjod6itVN8btGgv9WKL2kLKhutETWD1pU9tpd80v/MIvYMmSJTa+15o7whTu4yojcwXtgBHsuawJ0agcUn1rIq5rtO6b/qZlsm6lPd2c9knM8zqbK4jnfP8X73le8n1TvChe++3f/m3bbfiLv/iLeOSRR9DWRh3lNiJp4yi1BP7UtI3dRk83jgYhFXTbDa0n9gm6J1BqDuMsJUdU6mgsa7a5U62QztvVs2UrJzqHVr5rep7mU+eHGprZzhW8/unbS2Z/LzfJCt1rp95f/uVf2q693/iN37B29GEE+YkRI8anB162+74ts4e3k1x49dVXTRf8+te/bm+Eyc37lXkuZYOGd59LiVRJVHcV5OJIuoSZzL9mb5T3JNMlmr6DRpHSuEoPmsdxztRIkTifolstKNNa8j/J8UL2lNwmDqkzcgyUzplscJzgfFsIkx+sO85XRNv9etA44dcvfJufPHkSv//7v49FixbhySefxI4dO+ytQekEguKN6p5RXhNSTfNNX/SKFsgPdMqIrn/+53+Ov/7rv7aM/Oqv/qo9OY4OjoLPqL9GM32rUSNDin3FcFqo8YsBDsqnFgrqtGoufriqo1OafsWoKYZTA9A+7SY2cwXVl8hD9eaZRsrhpUuX8PR3/hpXrgzg4YcexZee/FloV1fdtktq9V1hONFkx2skxpuxsCxhlsXu4ZWKWLIAZM6ZS2iLXlTmtGWT9SLVrZLUoXtArqbFENolQxLbnwpfruZeZS2nVIcMyY6tOja401vnF7QgZ8JKFSNyi17Kqc+tqttVOXlk1kUvc2FwH6KJaZ42V/oUEfppOkUnzpa2ErKlflePrVAwH+s0msleY0+EemXSeJquapBmXgy8d6YZgW0fK6BRIRya+SJcOzb9eVicM5i9LyuOpjHGpwJeBkVlkYdvf70qp0X49957DxcvXsRXvvIVbNy4cfrhyEfB7Hz10dEqP6+Hqj0UaCBdCzhJTZl5wtbzGzZxDfRqkfi6iVJKyk0SbZUk0tRc9GpjuTk2pDhufBBuVvk+CnxdiHz6Gqc1hhw7dsxecezt7cUXvvAFdHV12fheay56ySwlROOOMNd5/0CoTNY8Gulp4I1dp6H8ig+b5mkn+Y3IY7OS9hSV+x8XHCPJ+591RPlOfOT5yfOfIN7Sqw7/7b/9N9sxqkmRXo3zuqT4UA/5FMdcwtQDJil9pxaIPxyv6Hleqi49STylV1U47UkmUHR6OkfYGtWfGvWjGtqai15jmeYCHssgbvR0NZzeoDQ8nBahdN2Cm2wSOix5juDbLtpeaj9B93JT+8l979699tBDbfnTP/3TJkvkx5PwYWSHjz9GjBjzE60yQdC9l9Ey+76+c+dOHDhwwGS4XnveunXrtHvU/wfhZskFk6bN5NwDTXe118enZa9b8pJfyWS96cQRjHeO9LBDSCYmNUu2+XDCdL80aomshaulJ6lKyC1Auk6F0sIofo4QHDMUnz4klmlM0U7OnI9/iHqYb/Bt+EFQG0uHjI4Z0jt/8IMf4J577sGXvvQlW/TSAti8WfTSVQqIJjJecfmzP/sz/OEf/iHOnDmDbdu2maLSqhz7jEY7yFyhbpoLDWS4pMiektFCZTLlWAtC8iMWd+W0XNtOLy2SuSstEJKB5xKqM9Wdrz9fhyK9DqD3YQ8eegeFwgRWrVqHzRu3W92HYc3aR0W00iSq7ORa9KIFy9PQgl7Yy55PRUyLXukL8ki3dv4wHaXHbqtzKqr6GhFt2xivzn+qUjpQ37MV6xwniUKFWmBD2/lVV+zgJi78JGI+QYuXtnDDzF9n0UvlZ0XTwgk3VSJL5pwMujcXOrldEGaryjazwpIk1FTdith54UV+1Aea6TO8BB/VaOehBc3YrkYzo9fYC+Jni9dumB3GrSI2d3ZZKObNZVlt5qNz+XFl4C0poUa+CrOkaIH1E3Fzs88YnyI4WeLa1V89PP9rXBgfH7dzvUZHR7F58+bpV5Y0Xng/0QHsemhN45PA5+9GqCfd7tVUPYVMTfIugYmMk7m5kEqLFpOZJ8kB9ddiUgfBJ5GvapFL8rCOSsotICcZx3yDyqH8a9yQ2S9E6n5yctLO89I5bFJKpZD6MHKXP9+GWtj0bTmfoHahNkKTRnDyjmSZc2pCbuJhk8Dm30F3kn26arQT/BjhYrO6Yxvr6mFp8F/1orM8ZuK7GubvMw5fb56PrB/RzuqVZsHz1muvvWY8qHNftNvQL7Rq55Ae8nmFea4QaKwk6UGf3+mlVpUxpZ1ekUUv7RYtpVW+EIFkiZ7gVyv2sDBIBhhNuZ1e4kCnXzmuFKZLpPGaN7pXtVndsQ9KR5E+Zud53UBfuFXw7SV5IHgZ7uWD2k92ethx/Phx2/Ur+b9mzRp7K0Tw7ebD3ghz2cYxYsT4eLDxrykTTFY1of7rZYZkg3b+6+Ga5PnKlStNLxT8gwzv/4Nws+SCchxd9JJEkgpg2gHlt0Huknm2RkAXm0NpzHJXhbIoElM0US/ieJCqu0WvUjLn0kiPc45VtkWvTFUPPfSWjXQwbSnRF/Q1hlSQxZSVrYbcNfXg71XPH6aObhc+TN6i44dIZZb+Kf742te+hp/92Z/F/fffj4ULF07rmZ43fPytvHLLFr18ZgUNYtqm6BnwT//0T/HHf/zHxtR6OqcnddFFL5HPqOy93a2ATysKPWeTjZQXLXmlA+1Gag7gVCbqzUWvhg78FsMza5Y/GcnIAf/c7jDGo3dzm2hNx5ep1f6TwAsVkcxKQ3UokhJ4+fJlHD12EMXiJFauWIvNm+7jxJIlqhfdORgJvcKi8lfJFAXLm+LR4fZJLGC5tMhVQjIzanUkNpOfsNGGWphhqAoS6YrVS7cObq8n2KG1s0GvQIZoq5cVuXXgRJBBmEyT53hPRS/t9nFehdb2id77+hOidjKLZPZ+vJ1H1L41Hu/P6q+h3XuMU3+22OV4gKF4NW+EDGxvBpNwCsWzspHQkwDUKpLuWR21WoWC3E0g+UOdVXHTm1b9WSdukiWz+KeZF8Zhr54qXdahZa8pUB0UlzPJxpc7Wha5R90cnFudcRofM0oNKrWJMtuCV7U7vepju2kKWiVcTfWwnXkflBhPiXzFCII8s8PAFfeE2qfh8yBEr6Kr83F1vuQelR9RfzHuDETbzLe9ELXXF7u02KWD0bWAog9raMeQFB3/1KZWq02bb4RoGjcDH8RziWSJvYfjAGVeMmyjOcAUg6RSabQnR5jxAuWApESG1IaRMGc7ajP1AruZFrua+bV03GAt3OxyfFyo/MqLyNeFv5fSoYVKfRRFRxNs2LDBZKXGD8GP2VJC1H5+HJpPcGO7jV72p0Wvq0YfuksgaudVleNjYPmXbJYv3cuTXt+XnR7azCz4iV+l86g+vJ0nyVe5yY+XcYpDZouLfnxd+TC693Wo+yha/X4aobIL0TFBUD1qp5DqWRMjKb7SM+Vfi1561bE1zK2G3wWgiY8WvgRxiP4De+1ZC1DUEUgaW+sZ92XzXCZFLuL4XqRuVSlb3seQsri0cOVCicsc1NQh2147uGohJVE9REC9QnXRoI4R1t3O+6T0BYWcw51eN0KUR8W7emqvXaNawNTiuQ4mlr3khvfjeTzG/MMHtc2nVSbF+HgQv3ie8H07OnZ5ftKGGK0PSIfwsl1uuo+Om3MFpRg2xyHbxc/s6iqZPM3hzE6Dk7yq8qeyacymHqGPkbGA9OvyW09RPidqSFPEdenDRpxzD2U6Jf05dx6m6jGJoJZBR7lXwVBMFxFwfAjDPOfJWlsoI08/1UqVY0jedE6NeaoXkdfDJFO97nyn9kONAyqD2lp6pcqn8VJHa+jVxm9961t46KGHsGDBAvOjemjlpVbc8p1eSlgZVWZUAJn/4i/+As8884w91fnd3/1dW/Rqzajuo2FvFny814PcG6o4+tG8xIg8HNaajJ4h6wZSfWuo62m+TV5EUqLF5FqJdVfBrw7PJawMJNWbr0MxihRCKRn/n//7/4X+c6fxs1//Fn71l38T7R1ZZZ9MRQVJipl2YNnrjUUrlbq1rgmdPaNdX1p8SZQZb90YSPGH+opjIsO6o2+6m41tZCCzUlDVlRcKiXS9xEqRCGEnFmkliDMINUmSeY5CZfBQOaK84eHtlAfB3/urEPUfhfx4t9n8m52i1a2cPdFSVj5WM/PHFrkI88J7F49vC2dJVZj3LlLF78OwEtCou/biT9NOcTRvm5G6SZduZu8TMyFvAGXLri5y8bC+MFUnpZIpKt20Z7uE5APxrzhAO1fUbrUU25iWgXYChmVU9UWqgII3oOBttkEU0br0FIXcfdt9GLSGj3HnQhNTfaXnhRdeMCVHr7prAPOLBZJf0cWBeQXKRi1+QzKx7l7nLlPXELdn62PsC9rhK4UmS5nYhikqPxSDyJDfA40Z4nv1OZYtaJ7L4PuKx+3kdeVF6XslwisfukbP9JIyKsVDX1eSe2t/9wtg8w1SRkUOGrNEvg1k78nBijDdPJSH5tft4tYXmjRC+rKLf1VPUQXdj8WCdrXITf519XUsd38VZPZxRu08ZOfDCFG3TwNUHl9Gfx8to5T63/zN37SFcp0H+Oijj04/QFW9+nBzCdMXSeInveJIE0mTI5aD46bphRzz9TBUX/PSbi+NoSnepxkmUH+plDnG1lHN65VhloE81Khz/JX+lNYkJoFapYYk+YxBmRbjpT9VjVLTFyDTplOJ91Rn/LU3D+YO16v7KK+qjZ566il7CK4HIL/1W7+FX/qlX7L+4OWGKNrmMe483Mz2ux19OsbNhfjB921/73lEdur7Tz/9NF5++WV7C0z6hV5j01gale1zKRf0gEEkaLHLyXmN+lfrplo7cFJXLsqfZL7NnvknB40LVdR1DjJleLZEP6kcSnnqkPRQwwgvZaTDPDJ1t7utkipYnCF1zQTnzEGyjgzn3w5aO7m6X6heVFey87rFXNbVzUQ0/75c0j//63/9r3a0xhNPPGGvN/pFUe9fiNZJFH7Ra/YZ9CeAT9BXvlcCvUIoaOeRMih3uYmUaZ95kWdwf/9JyadxPfLpKfe8aD3GdujoSBbO96lckJWtAVRlYkIyHfSkX9e0KSC26JMosQNUZk3jVpOvSytHs+78hESKYjabR3tbJ7KZLLK5mYPwgoBhUwxj3KBFmBzLpzKy3Ox2dSr5VMUYJ+Nmp0zpwHqlqfToQ+dWSBDoU91atbZD+pJMl27utT5OEnXORYrMq8WTFCcFrGBtFvLHXfk8e3gGvhFu5Ef859193D5+147X0jWYyU4T6lgqkyM2NL1ohxedKJ2cQJSiq91x+ihtldKsjGqoBUMtDLLO9eRVyq/Va42/el2qortmPpQ/RywCDUrXpcVIXJainprky6ByR8seBX3Yzi4J5TozHWrhinEGjRTzyvitIal0hlUk6xW7SuFWuAT9hjUKbeYpGeSQSevreymW4dq0XF5MXDM+VzFaKK1Tgfckdyn2Ub69EUX5PKY7m7TrRTsaNA7oqvZV35Ss0jihqzBb2NtJJj/URdQPNSmlPNNb0DnaZWrqWxwHgjbac1xgGTRmaKO6nuypD0sqmALFuFLsO14mRdO43bzuZaSHZImgNtHCgv+Co9pQrx74tpM/KaZeFui+tWzzgazdNM6JtEAge8rjJAd7e0JLd1WBisFbW+SaDmJVU7OW1MKCxk3VhUj1IMjs61B1UKPOI5LZ+/N15uTkTH1F7+U+G1kZeI36aS3jnUzR8vjyRe1Ud54HJSvEhzJ7N1+33v9ckelOZAHxj/ZukSuoZOvVZo737OsN6lcN6kDUxNCoFZAlH7XzPksdQMOu/NRy7ahTP3ODvPqPeIw8pUW0ul7905gt/lM6jjkpihDSaA+p5FkZkSX5SP5my+utpGibXY8kJ9RuIrWXHsrKXv1Ecfh+0Bp3THcW+f54M2i2+GO6MykqC6L2kuOSCZIHku2ClwnRcTUa5paT8qg0SYH0BGbBZD3dHFHmSnbriBptIbI8smyU36kkZXuCc6mwgGSjaA87wgbn1ukOoI1zaO3ypR1D8cr+QmVSadhDVVKa5gzj04MMdgHmgbFWmVZZMnJGZxB01b3vK14Xu6Y8dwh5+PKp7cUDulfZvN3HwUzstwjRDKpR9LRTT3e0A0luspuNVDjfkHNBlhdLT8zkJumhFun0pE11q8quaeLORjCuF1vTjpN3+rRrLXTKLT3bda4pWme+bqN2xULBztIpFAtqEgqUmbDyrx1fIt6quK5sDdWLSqp41GmltLBTsS4Ur9UNoTqr0u+0P2lhcuSNFjmYGKnKPNRQKGkyQE9CM7zPp8VJeIaO2rdSK2TnyxP15+9b7a9nJ2Ixpkm3jidm/NJo9oK7p73xDv3IkQFdEehJ1cAfnfciHtOfLT6xzmlrZZ2OQ+k14xZZOmbvSPFHSXYe3o/359rUkQaPqH8fXpnz6Vs4+tVVdtYGzasEkSZ58l9XOSyWZjgzz8AFa4YnVB8WIuHqZMbNufu8eJ69EX0YPzHNP4ryog4vnpiYMNKuL40FrX6j93NF10vX51tm95qxI9eH5cf1Fy2c6OGHuF1yVH1OEJerjzA4ahw/FI/8R9PwdLvK7snLAU/Kp/KkcVvtpVccNX6rDf04LhIkI+Rf4byCMlsat5dYLpOpJKomkmUmz6Ikucu8q9E03otsDNTCPdtU8liI1pMvq5ezgpOZTgmVe7R+5MfzlUiIxjUb+TCuHJ9umq2cshOviQ91Ff9NTU3ZAz1fR77PtYadS7JxPkpeVjB/YirbxcWyJFRGknjK+Ez81hyPa5KJdDMmJHy5dEQCnf3Qyfj1uqfK7uzkT/GF1M+MWvJ2q8nz8/XI+1P7qe0kT5TnKJ8LukbjjSmmmO58isqAqJ1IOob0QZFkuuwkGyQr5M/Lh9bwt5yUpuQ3zTa3i5DuJeOVV5Pulkc3BphfzX1F1B3MTfK9Kbztnl5EtrRGwc6QckHI8usDaFrokpWzZUjqmEFKx+E43Ux5srSb9y79O192+jFB0L34Qfwhs+DdPg5u+qKXz4wawJMyKnuv9EULFIXcotebDZ8fT1G4e7crKZGQgqFdLkVetZ2wTAVZZxuJuaSvJOwYoyqvYkRXjWJa0Qc3xmzp3wq0toXLu5iKuWZW1Tm1IKUFPt7RD9uI/tROtouJxO7De3bAhLZaTtlEwWqqkeG9VuNZZ6wftirNOnAvhQqVuoqqJFFFKlFG0KBSyjQL40WcHhzBuZEJTJWqjF+nosxgNt4RPKML8nM9f0LUzcrRNEevgg83G1kctkOpSSyV6icaTlErNjW3zNJj5dfqwc7BYplZL2G9RKENKuoNVGua/HBizFJbyfV0wGJR3EpTcfC/haYTavqWINSfv3q4fLk+JnIRuNidOULKsNUP/ZKPEzW2Ga0qehqt9q6zvauc3DKfBTvUfxhBYhiVagWTpSSKLGIYsozaEcZwM3D5dLu4XFLiIf1OJ510vCZy/vl7gzaN4nr2MeY3WttNfVrKjAaz2fr37WjnD8VzCck9EtlVci9JuZiojSPZmLBdXGXKxVJIGci+XdJYQpmZ1AGmVEzUDVTSGvle3wlWvLPRfIAfs/2ijfKle6+gekVU9nL3fmQn9/kK1a5VcZOi5hlqLkzIbO0kYstZe9Y4dqoVWQ8cP6uqD9WVbHjVOWA6Z8kiVn3InvVWU50070Xy73aWOSEZldueBNW5b4soWv0JUfNsmC3MfEM0j1GKQnUhHTIqNzzkt7Wu5gTKosYzXRvMc5NkIa1APSIk/6jnJ5Pkoxp1pkoRSepeyrNkR4lEaaIItAnRhmhXdE1+GHfoFrTUv9zDM7k48jWhRXcFsjoTb80xfHvdiMTrXpZE28rLFkH+YsTwaOWh2SjG/MYHtZl0DUGy3euFs/mbSyhpI5lN0gruzoiOXuaaLObV8qw5jkllzYs1WdKri5TroXTEBEaSAcYoBwOOB0GthHQthVS9jWNGCtVkGZUUw3ASHU6GKE8VUSzq4U4V5SrnXiW3huLhZajS9TLU62TXw+2u1w8Ln89W/fKTjPG3dFRUxvwAJxJT+63orYW53v2tpGvSMrYlw1A5SSal3DqGLUwM4dLFflw4fw7n+s/j9OlzONN/EVeujKNUllLqFjDsVQnTVK4/oblVJOiqMs1Wh85eTwklWGTHPDYXJUR0NjvlXV1Rn2M3v1oYaxRRKA5iaOgCxkaL8sIAWSpqeppfQ6M8iWphAoVSlf5C2FHPjC9saLW6hIB+KqUSTp04g/2Hj+D4uUsYmyygwcmBVrOVv0+CaAfwcbVeBe9PdrO5e7PxqxNh/NOExk9VHBja/dG7QrC2+esmRkbNha+wOoWJ8Ss4cqQfBw+extBIwRZKQ9ZtqIUvNoB7GqxJjeJ3aSo6i1vRGiRAm3bO2SnE5ka4Yhl82TwpkHulx5lF8u4nXKqShDZqVCkwKairgYRmEWXme+DCORw/ewmXR6ZQLQ+iMN6Pc+wDJ88MYfAK27xaJHtUp/NhtcVyiCJqOP+V4gx5eTDTHuK/2Xm21S6mO59cm8+0r/jfT2Cj9vORphe9yPVJdpyA09TaxGVMXTmH0bEiJstJVBppyr8U9MHaRH0C1alBjA9RPk5owsqewWiqimGW+G83+boXovLSL34Jvu/qProo1gof53wi03jUjMpuZPxrJenfZqa8cmOlk+9asNfDjWqlaB9huHx5AP3nz1Mf6MepM2dw/sIFjIyOolguo0TFfWRkFOfOnae8vIKqFmqsTl0ipi8wIVv4+hBQ/q/XN7z9B7nPZ1Ieb5TPqJvkhe69PinoKn4Ub0bDzQUZXxk/Ne2af7yxiZDWv3SWX6gP/iQpBBocdHWMAMtRK1eoD01hpFhGkeyhh5ABy6JiNSgwquUS9YgxnDlxAu8fPoSTJ09SFxum7kkpQv9Jvaar+K0OyE/iqUi/nEtSmh9E8ufbSPdezsjsEY0zps82eZ6J6c6lD9uGUfngFzdkd9t4gH8m2u3eyaWmgSSBb0LfxnAnxWhP6M4elOkBWa2E8uQIpobHMTlaoo5YxyT9T1FGB3qIVi6gPFZCYaSG4hTnyokyqukqLp66hHd2v4W9u3bj7bffxJGjR0lnaX4fg4OD9uDRw8tQr0tfU44IRevyttXrB5DGcV0Ff6+8ts4VPg5mRpmbBJ8RNYIomlndyz1amLnCh09Lixx6Kqu8NlCrlnHm1HHs2bMLr7zyCl59dSdee3U379/EUTLg6FgVFTvPRfGTmA5L7qKaBbeqzL6+BV/HIm/vyV7HiQgT3z5arFO+9US6Jp3MotKrbHVMTI3j1NkTeOvtt3Ho4BkqYBXaOyVLXwwqjV7BQP9pnD57HucujmCyxHgYXl9mbNTLjK+KkcEr2L//bbx74BDOX76MQqloi15a9PF5E7w5SsJs9RZ191cP7xYlj6id70RRO+enuRBl9xEyP01rQtmyeLTyLktlUwtMVHCrxSlcungBzzzzMp750XM4ffoSikXtDJBwEs9QHqot+BfNh4dMjtyf4pfzNOlPYTw1w/pyOJI/ZUsZ83b06+7s3t6rUH5op9dZG+UiJq4M4Nj77+OVnW/gzLnLqBbGMHD+FN5iG+59/V2cPH0eZSrjimU63xFykzs5+zRJSoN+jax+5WdGJogPvV8P7xalGPMb12szf219GuV5QtC9/IkHouGvRzcTs8Uv8m6Ceo4WrXQriandkKPnz+DY/n048N4ZnLswhamm/KMzUJrEcP9JHKXcPHNmDFNTDKNw1tvmJ1RW3w56oqi28H1cV7Wdrr5OvL2g8cS/2jgfwRbVj5G1oWvI6XtvphSiQb+utVxjNu04ro0NDeIYldA33nwDO3futMN3pR/o/vSZ07Ygple3zvb3m93x4ydQLJVMLtofo/J1ZLE269DX87RbxHw9+Ha4Hj7I/U6DlP1onfh6E2Qv3p17OMaxXDV5yIiQneMgmpRPeyjEclTKmBgexinyxoFDR3D63AAmi+4MOIXVgldxahJXBi7j+NEjePGFF/Djn/wYzz77LN555z2c47g8Pqm3Eeid/qVPeHZ2TCXD/IPayssQkdpTPCq5IRI+iOdj3D6oreaSYny64dvZy/WoXig5cTt5QEkrdZeDGZOHl1K6Sv5qV7fKYG9PGYWojY/h8plTOPzW+zhy4DQuXR5DkZNAW7Kq11CdmsD5k/04dugEzl+4TLciqmEVB/a/g+889V089Tff5hzyh3iJOsZLL+3kXPJZziXP2GugHn7883V3Pdwp/SmaT29WGWWWjin6uLhl2oFreKfAqRGUSd1rQNdVdq0NoPvWwt4suh6ibtrhlbBtL2UWoEiencLI8AXs378Lzz/3DF588Xm88cZ+HDp8HIcOnaJCewXj4zXb7aVXHt0h92S6D1mtrXn8JNRan96s+hc5yJ8WubSKqnZxjOTbKUiSoeimV5D9eo8WSK4M9WP/O6/gh898B3/3vRfw1psXMDBChazGNq1NYnzgCN5/exf27D6IA0fOYmiqjgmGD20nxBSqxWFc7L+Ac/1DKKazSPQsQCafbx7Q5/LtO6tI8PnWfSuD+zK3hhP5cvtyzebHk/fr44r6tcP3mX/t9ksmxa8SKE6oKJiRBW7a2xYshWHlBZwokoeqlQmMDl8m37xFRXUfzpxm+QsS5HoOoENcc4xfT6r1IQTZcaJv+XE0nabMZsc8Kn1PDCP/Hr48vmyqP7/zyr42Kv8W1m1j0ORdgtpOwiX/lpl+JSH/5P/iKEYHLuKdExcxWEwgnRxGYfR9HDp4GPv2n8XJ08OolSeRTol31G9cW+nMESmuelLNVlQyzo1XPZG2jyaI6K6FVpdny4Tl98PA6iGmeUuzIWqvQ0pFvo/6e/GP7jVG2MTvQ6A17U9C14N301Wfp6jbLk1ahFMcJgZw6djrePF7/wd//e0f4UcvncShMyWM1BooasfnxEmcPvAidj+/E+++fg6XBysoMYaZZ3SzI5qvuaSo3JTc1cGyahevaIh0L/j+Gg3vodcThKjbfCAnYJtkElfK4gyxBoxCfbVWZu3clUz3r6w3qqiWxjmWnbQHYS++9BJefe01vP7GG9j/1ls4cPCg7fYqFIv2uuPE5IQtfF0ZHrJ7oSntSM1UWY8+f6rbVrJ8EybPGYeuH0VWzgaf3nwij9b7KFQf/uMXkhF+8Vz3qhM/cYrGOxc0w0tsFzWNa2TmRRMh93qjeC6lk4tDjrSTY7hy9H3se+EFfOfbf4unv/cD7HrnAE5eGnJh+VOplG3B69iRI3j33Xfw/uGD1CFOYdfOnfjJT35ik6BDh49hStvDLIQPyl8R05str7eSPgz84pbI87faTDIj+jCkNe6Y5gfNV8yW15jmB0Xbx6P13uuAHpIP+miJxjzJdckGwYebE+IfJZGRS9wywB/ms7nLSzLXj+XOTfJXC17azVvG8OV+vLd/L37y3R/hJ995DrvfPIh3J4s4L5+VSVQ4R3zv1bex68dv4+DBU7hcGkQhKKE6zDjGEsgktHZSwsDgAE6cGsDFgSnem6S3PHq9TOboWNiqI8h9NkyXdR6RH8P9WCCID3xZxQueHz4qZjjsJsErZcqYmFbM6pVo3wiy943SSh5R881AazqeokqkFge0s8ntnKmjUqbScWXQPpU5MjJiXxu7666tePiRR3i9C6tWrsKCBXnksmJ+peHSsqe5H4JuJlS/gsoTLZPgGckWGcRA9OrO8WqGi/QFLVCkmmtM1ar7csbk1BSOHj2K5557Fn/2p3+Kbz/1bRx5/wTtCywrMDI2Zoshb1DxP3XqJIolTuoYvVKvF0soXBnC1OSUfWL0V37lV/Clz9+LxQvabXdUveIOpJXCI/KHGeqQU111YLKUW/mJkuzFW3KLXmWvJ+w6sN8fuuwFpq6KX9doegqjq1eidXWHrE5hqqC0yqg043B1q/pr0J9ec1E9sm4psK3O5H90DMWJCYtT/LRw0UILp7q0+id8tRdLRXsdpsC6FL/pve1qlRN/RlvnxNk6N+Oo1ZU3HVCr3XM1NJRXXw6GKyuPNCvvIleP7qBYlaPAfOk8LlsA4592dFl52cbQK7pTVUxSAFc5qWtkM8h0dmLZsmV4+OFH0Nu7gPKbYZkp9Wv3dZWUhR9l3sfHdSA5J3nKl+qGaWgHm+qsoPYvFjDG9jC/E+NWZoXVgqrvczXGrbJ6vo3ysOfjGPMf12uvaFuq/4m8XPI8Kzfxl18Emw+I5lskqaZf8WxVu1zJ25cuXcKzz+7FX/7xn+Ev/uRP8Oorr+HK0AhqDfYv9sMTJ05i3959OHDgPQwODYKltVi8rI6SS8OlezvglQqlb/KBfVJQ3nz/dGOJW6D0kL2Xj4KUVRtb5jl8i7b++ZybzFY51B4a7Dg+Finr+vv7cejwIVy+fBk9PT148MEH8eSTT+Lee+/F0qVL0Un5KR7W57W3bt2K5cuXU0/IoUZ5K1J8emVCV9Wb+oPvB54kwzUO6eB2jWc2ntDvjcjz0I1ovuN6+ZSdyqfxWogulKvsgl+kva1wTDVNLA0nRPpTG1FP4Zh8+fhxfPfpp/EHf/AH+F9/9EemWx07dsz4SrKFhbJxXfx1+vRp47nHHnsM//jX/jHWrluHvXv34C/+4s/xwgvP48yZM6DKQD5V4q6vTr9GO08QlQWzta3azMseyz8pxp0N34/nimLMb7S2U7TtvL2XE5LnGhNlL5mgNQNd56tOoVzZg31dabAv6cqW+Zd+uH//ftuh++2nnsJTpFd37sRQmXoAyzMyMozXXnsNL774IseAozbe6wvAW7dswW/91m/hP/z7f4/f+I3fwMMPPWxz6H/2z/6Z6RnSMfy4r3rR/G94eNjCe12htY5bab5C5VH+pQf5scDff9J863tsvyfD7/6eXW4KPGP6q1cc3377bRvYpQg+8cQTphh7yF2kAnnzzYSPczYSlG6V5qrO7qiXkS4XkeCEJjV8BecOH8Th7H1Y8NDfw4OPPolHtqzDho3L0LYsg/buNDoZNsdo7HOjZFad2aTdQVpAUvRaC7Yrne1qdHMVM19vQrRMgupfnWHX3jcwMjaBTRs34pEdd9NfHQU7myuJZIMUahdDEsUUJ6LsszmcR1AcweClAZw/O4qhi1TARwdt5TlYvhGdC5egt20YkyMHcPjMOZyc2oC+RWvwpc1ZVAfP4PihIzh3fhyN3FIEq7eia/VaLKmew/iJd9B/9iImwgA9nRlkz+7HhXf34K3LDex97ySe/8l38cKP/gLvvfs2KrWFSKY68dbe7+NH3/9LfOeZl7Dn0HkUEhn0rFyOSipEW6OIoDCK80cPYuezz+C7f/UXeO7Zl/DmgSMYov7Y6OxGW7YNmUIFY2fO4v23n8PI+ePY9e4QnnnxHbx14CSmanW0d6TQc/YIDj3/I3zv757G0z96Fs/tfQ9HLpWRaFuJMNeORjaJTPIK63SEFcvOmGyzjpiaPIhq/2G8tfuw7YZ79vnn8P7x99DPen/uZA8KuW489PnN2LyuDQuCYdQuHsTp1+nv20/j+3/9fTz79lHsO3EJF8bZAt0Lke4KkE1eZAedQqOaRSLkJLI8jMrwGxi+8B5OvHcEb+55Dz/YeQQvv30W/YNFpDKd6Otsw9jZF/ES6+8vv/0svv/jPXj37SMYGRjH4oXLUO9MopSYQGbyLPP7Lg7ufRl/+vQP8Gfffwl7376A8dEcFoYVtFUnMDBaxpErAfp6F2JDx3mUrgzi7Hnyw9AlTAweR/+h9/DKsy/gxdf34/xEEejuBWeAbLMKOoZOIxg8j90vn8J3n3oOz3zvR3jt5ddw4OgpDIbt6Fi8Gu3kO/WZKuuxnOSEjX0vzf4jRHnZm2PMf9yovby9lBmdSaDJnF4D0wC+atUqm8R6zJc2j5ZH12SjhnRzB2ujPol6McTJfSM48PYZtPU2sGBpEemeKsLubixatRbZkUG8ffgU9p5LILVkA7Zt24i7l/Ui00jYYdWKupWkK7k0RbcHvswaQ/zCgh78aFJ+5coV222zfft2exDkFxmsfprm+QvKbJ1Dyat9Zpx1rD+OfjN/HDaTGjtJdfqpNlKoNbQbN0fXFDJD72Di0Bs4dDGF3MKtuHfH49jx8BNYv2kLNq9egDXUC7ry1B0awxgaHsXR83Vk8r1Ykr6C3S89g1OU87VKGu0ZyvjGEOpDF/DKu6MmW5NBHfl0CampSxg/vh+v/eCv8f9+6gX85LVdOHT6LC6NjaOscbN9AVLU3sKgiEayygz7A/YJylSyl9uNaKBB/00Gm7aex1Beo7pgVJfRePv000/bwxcvO7TY5d2jutBcQYfWczSTie1B/pL+x3bS5u9SskTdsoKgHiBTpr5QTePdc/2odWSxdd0iLO+k1phuR3rx41i3djv6VnQjlU4h3yijN9PAomWr0HffE1ix9X5s7jyOrvp5DAyVcP5KAmF2Ce7a8QQWL8ujhgnmQPtQmRPyK2uD/7entVvbQPeSIWof2R8+TF3prbdsLHjkkUcoF7dd1d6eYty5UPNNz4F4JRewjTURZ6egnd6O0MN3tbPnDwktNzeK8kE0LsZj5BKY/pOHGPMavj1b4e3FAwcPHrRNJtIFt2zZgjVr1kxvkrle+FsLjanal6+HKo4v7drMhz7Gpp3hHJVopfOsOb/SXSJN/uZspl5B6Y0f4NLh/XZecimfxpVxYPJsFvctfQDbNhRxYfACdr9+FOOTNazYuAorH9qIfHsHBg/sxb63nuO86Xnsfm4vZeZFDKc70b10GRas7kE9XUWG87Spc8dxaPerePnHz+Kpv/lbfG/vqzhy5jJKlR6Oi33IpFlvOkeSik2dfadqH+rTOKGykXR29zyFb3MteOnB365du0z3FF9oU0Y+n7fFUKGVR/y9x3/6j//RrnOioUYTno9Q5Qg1MgBFMuUu86tdUVQq2d1QKxYxODqFExeu4HT/RQxdoaJapULS1YVMoDVZ8RPjCPXUluWdtVpdGnOJ2epdXVRQRxXDK1fOjsQBR2Z1DH1hLBHqK34VpJMBOtq7sHTJMmzZvA69vV1498BBvH9UhzdT0WJnTmdTjCLNTtZmi4bnzpzEnl27sWfvm7g8OILOvj509HZj5PIFvPv6Xrzx+j47A6xQqGD4Qj9+9L2/xd98+2+xc/c+28ZZKk7i7JlT+PGPn8Of/9lf4vDB9zA5MYbxiQkcPnocL726E4ePHUeReazS/hjd39i7G2dOnUBPZwc2bthgO9H2vvkmDrz/PkaujCAs1DA+OoqXnv8Jnv72X+GVV3bh8sAIFc48ix7g5OmTePVHP8Rrz/0EVy5dEmNgbGIKb759AN/9/o/x2u7DGB6ro1rX4e0Ucs02TUrYXTiLl3/yQ7zy4guc1JxGYarEuhnFewcO4NTJ0wiTVMqp8JUrRQwPXMDxd9/Ej3/wHVw4c5oTpHba13BI5dq5m3l+F0MTEkt6os0Jtr0SQVOxjPGRAZw8dhA/+P738MpLL+PUmXMo1chxKSq99QTOn7+EnzzzPfo5hPb2dk4I1nLQyNgZIK+89KoduFyulDB+5RLe3bcTL7/wE1y8eB5BJkulI4V+CstLFy5jZHgIFy5exKEDh3D54oCdx5UmrxcmR3H61Ps4duQARodHkEmlMcj+8PJrO/Hq3ndw9tII9FpG8exp7Hn2x9i3cy8m2HeymTzrK4F+tvkPfvQs3mR+RkernABosNPrHyEqOtw3gvkuN2LcPEQHqvkKlzeOD6GeQGrXI8eHdJY8nLQF5c89tB1bN63g4DyIvZRvwyPjyLZ1kLeT7P+cinJinqZ/LaykZlU05he/R/tf1Hy9Nroz+qtrw6tNyrenCFhO50eSnm1IamhJgXIqQ/mfouzL5jrQ1tGDdlIbFdX29jbkMgF9UZbVKeuHBnH02EmMjU+hwHHqxNHD2Ld7D/bt2WcHk1fHRnDq2Pt4kbL50qUhyvAQY6MjeOvNffjhd5/C4Xf3I0c5nmBa73JC8JPnX8SuPftx6vS47Qa2s0ctd8quJpVSYiVp9Sd3/tp/S9nuYLTKivnBd8pDMx82KW/mzS6Oi7QYmQgySJEWLl2OBz73OTz55S9ix313Y3HfAsqTLCcobUimqSdwvG1wstdOvWnx6pVYunwpuql35bqzWNCTo47TTl7rRJrjqr6YrTMEJVecBsd8WJ3Mh3qJEUMgVxpbugcjvst6s+x1tIo78sK5abeiO/PX3bfCvDX9xrjzEZXjrTL+9qEpu42EaxnObDT28k8z6pA2nrQmkKyVkaLOuGLZQqxZsxJt+TYMXRjBycOnUCuVOCbQH3VJ7Q6TTqGjbiYqk5zrUh8IS+hoy2FJ3yJ0dfbg8tAQXnrtNZw8exYFzuMGL/bjjddewY9+8Hd4d/+baMtlkcqmOUc+hhdf3ondew7i3Hm9kcVxQdmxXPpS3O66/WiYjT9acT37KOZk0Ws+w3cqXVMNTkbqGSoqVCQSbWgkMyinqiglKyiNnMTlIztx7M3ncfTNV3HqvbcxNJpGoZa0LzEUWZP1hD5HXUQy4bbfG0/Nylcf3DC3BkpXTa5rM3P8d7mRsqynLuqq7s+6SKjthFKl0lS+e7B+891YuXYFagMnMXTkTYxcojJfXYpKYiF9lxCk68iigMJQPy70H0X/hRMYmRpEJsVJYqKM8ug4hs9dxLkLgzg/VsBYpYbC5ADefH0XXnr9BPqn2rF23Rp8accyrO1L4p39x/Cdv3seI9Uslt+1HQ9sXY1NiRFMvP86Xj8zgXOVNKojgzi5fzfeOnAGlxIbsOahb+ArX92ILeuBC5cGOFk4hXOXT6EanMFk7QwOvn8Qb755BifLKaQ2b8aGe1didX4QV957DX+z5zjeHkuhe+N27PjCE3jknrVYVjqHky9/Gy+9+iaGxvXKTxqJMAOd0VIOC6g3Krh8bAh7XzmAdwYqqK/Zjk0PP4q71y5EujiEyYuXkaiyXoIxhKUBXDl/AccPncGRwxcxuu4RrPzGz+OL2xdjW+MYikf2WN7OnwcKjRTKml7ZvtkaJ1sTCIqnUDj3Bl7ZdRGHhmtIr1yO1Q9sxLqt7ViWegfV49/B37wygsu4D/c9cD++/uQGbF+/GJXBBN7bdRzHzl7C4EQFx8+OYd/b5/D+hRK67nsUO775M3jwkQVY2n2FKY6jVCjgir5Mdvo8JkYm0QiqCDN1FKZCjFwJMVXPo2fLZmz7qUfxwJo+oP8Q+8RhnOkfw9R4CWNnjuPNl5/DK1cGUNt2Nx78yg586ZFlWN0b4uJ7F/Du3iPov1LEqD5mQJ7LNDiJJK/FiDHfEFW8Qu38IenA0mRY5lhRxlgxDXQtw6b7KEvuWop0oobB4xcwfm6YSou+9JjlRLZOovKhs/7qCcoOJ3VnwPtWqxi3AKrkqyu61cZa2yxcu5u7/WgCpgFTCmoK2cY4ylOXcXlwAGeoxJ6+MIlzl+oYn+xgu1dQqV3ByMglXDgziKFL48jlimhvr2ByuB8nDr6Bw++9hZP9l/HO6XPY+/5pTKU6kEmOYuzCPuza/Qq+/coFDCY24me+9CCefGgzVgVl1I++i+P79+HlU2dxhnmy/UXkpWSYQtLGpaZK18y0Xew3xtzB1bpULR3zquVttowetBMhgmwGi1csxVKO3UsWabd8F3Kc8Deof9V1vACDmvKuiVCaelc6i17yXBf1De2CGR8hj1RzaHStQueipUjm65RJDeTpniLZ0QtM6xoREyPGHMINm1czofjaiGbb2UWDdvvp6A0d4aFjMao6G8UQM3CM2w33SMkeK0kmz8qSdOUcRm8BNH3aLio9HEO9QrWhxrlvA4m+5ZxX3oW1G5djZecIBo49j/NDRZSDbusT6bCENHXDTKUb6eoCVHoWY/FdW7Hj8Ufw+Jcfwra7ViAYHsGhXTsx0H8WtVIFl/oHcOCdYzh48jLOta/A2i/9Pfw855Krq0dw/OA+vLT/EN49O4jhOvVO5kq7j9OcV2o7D3j9LC4BffZKfAOk9eoCJyhBI09lpQ1I0dyRxoKVfVizOI2FmQmEo6dx/vB+vPXKS3jhtWO4MEgll4pmiTUZBmT6RJHMNNWMcb4JbeXH50kjEjuidHi7184vvWOs59lNUFtrUFOrUYkqVbRGnMaK1etx171bsbItxNTZg7hIhX5wtB3lsIdzASlsWtVm+cujqJZGUaxMoFSbZLT6WmMRyQrrqFJHsVzHaLWBgs50qk6gMDmMkbAL+VX34O4d9+CLD6/Bjk2LMDVWx5XhEhasuhtbHvw8Pn/fFjyyOEBXYQCHh2o4W8gwqSGcfW8/TpwZxnB6IxKLt6F3QRHLFxZQKJZx9MQlnBs8hXLqDEqNcyhUCshklqB9431Y9OB9WLWxB331sxg6vBtvXKoAa3ZgzUNfoLB5HE/s2IoHFlLwnXsbr7/1Lq6MVZjflC16aTGwxvKWakWcOzGM8ydGMNW5HH0PPI57GPaBe9djK3mno60TiXoD2QQnSeMXcO7kKZw+cQHZdC/yn/sGFn3hi3jiwVX4ypoQKxJjON8/hdOnxlGggCo10qbQNoKQk+kp5CrnkJ48heHJXqSWbcXqB7Zh3Y71WLoCWFjZh8rxv8Mbp9sxlNyOBX29WL2wgoVUioNCG4ZOT+FE/yWcujiE4/3juDjElu9ag1WPfxXbvvwwHv7cIjy4rQ3LF+XIEw1Mjk9QwZ5kO2prbBV1LVwGeXRRuC5dezfWPfIINj22A4/ftRZr06yHK2yHfub//Biu9J8yutjThXbm8e7Ht+LzDy/HA5v6sDi1iJO+szh9eQRjemcbdQriOpRqjBjzGXXyaF0fntBNtYBGZQqFWh7FoAt9Gic2LcaKZX1IFxM4+sYhXB4YQzJoQypD+ZmYpCx15yCGrTPSmPXnGDMVfk3VS7kVmoudpus2rTQK6iaR4hhQGcLgxeN498B72Ln3Xby6+yD27DuNs+eqHBPK5JVxVMQfY1VcuTSK7t4Etm6lwrukA1MjF7D/jb14Yec+vH2yH8nuJehevQyZxADGzu3D8WOHcWykG51rv4InPncPHt+xEV/cvAp3tQUoXzmP3edO4SyzYvt6tLu8HriFrwYVW5fVGLcbbAitQepBvha99NaA/hLpAG2dnQgyGeoRdKQu1KhwfOW0JKQOpo8p27kw1pIJTVXQVmsgTx2sMjKKE9q5Xkqha8VdWL5xEzr7UgxL/SKsU/fS62N6AJuIF71izBsY5zflqSCjFrh0ZuHFS5dw5vQZO+7gXP85DA0NoUq90KSbZK0XvjFizDE0vk4vepk8ng3eV0hZrb3glPlkcL/opUPtA70NlO9B++oNuO+BrXj4rg6Mn9+Ld/W2VEkSnrPrRgVBlfPvUjs6EovQvX4LVmy7Bys3r8OyNX3o60kjNTaOwWPHMDk8xLnxOC70D2D4yhQyXcvRce8TnMt9EU/euxiPLC0jURvF0YtXcPj8RVyaGufoogcvSaR0/BLJTfB1/WwhXvQivDDW++J2FpdtNyQjZnJYsHAFHnjgMfzMV76Gn/rSV3HvXVuQTVVw7Mjb+NM/fwqH3x/G2EQVFc5kpKxQ28D83rDiFCl11Ok7M/LHDKbWO2dtN9Y5O4kkB6G6Tdb6Fi7Egw8/hK1b1qA4dYUK2CFcOH0OoT7WlW9DkTGG1RqCGuuRWpftEmPAUCveWlBLME6qf9olVaNQ0Fs+OoR18fKFWLFxDbbctRqL16xA57JVWLlqLRZ0deD+e7Zh2z13Yd3atVi+ZAUW9y1BV3snB8wRUg2TEwX091/GwOAVjBfGcKr/LN56931cujwKHTZfnCqgMFlEWA7tgxqZnsXY+uAOPPTAFmxY2YaOTIXuUzh3aQCZdCfuv/9zWLd+Ixb1LcKypcuwZs0q2zZ6Xh80GOIkptxAhWXQ66/ZRA21yhguDY6SB1JYvGQpVq1ejKWcAC9dvQrbt9+DVXetJzvV7IMeo0MTOHr0BE6f7ceGjRuxacsGdOdT6F6xDBso4DZtWMN6KuDs2fdRLqneKEpZ71Jg1SQJVpa++Lh09Xrce+8DuGsd66MziUy5hOpQEefPj7DOSxgZuYjTp47j8OFDOHHmJMZqBVSzCYxduoiLJ09iZHgM2Y5urF63HuuYdl+ObbB4Oe5iHvQUOpFJoFovs87IzHpsbBMroK27Gys3bcBd27ezPdahJ9+J5csXYcWKRdCelqGzAzh99BL6h0aR7OjBpvXrsWFZF7r72tG+ZCHWb1iLe+/fgMGB8xga1Bcgq8Yf4hO99hEjxnyEHyPcr3tSbYK+RkmgBS3Kt1SuG8tX34Vt6kNUUJ5/5rs4dvSMnbUXBJQXDE1RCnZfilbGZMK3SRG03MaYQ7j2dbA2N7I7I8cHmohxTOSYNzzI8ebUCRw8+jbePbgP7x18E5cvn7XdCvo6bzaZQYZhSlRQw7aFWHv3g9ix/W4syDRwaP/reOo7P8T7x/vx5S9/AVs2dwGVCQxfHkKJrLWACvLqu+9GT3sXlizsw4M7tnE82YLOtgxGL1xCOOl29OhF+5ATQ+0QarKpz+60McatR2s92z3bxM6Io1GvciVTnBZxvLOPGMhxWj/SQ0d9nUq8JbMtj9ELhQX1DD1MLBdHcOyds3j70EVk29pw370bsOOe9VjR14aslAQxgHiTiYkUPEaM+QDJTfUHdyW/N/QRqKod8n3o4CHs2bPHDvN+/fXXcZJ6drFQQt36hNDas2LEmDu4Ja0PEKYS1SL61BKZe7lRfOt4WB8w01d8F/Qtxv0P7MAjn78fpeoY3nnzdVw8ex7lKud5qU6O5QHVygnk0hX0dfdy7Ejh7LlzOHxcb02dx+TYBIpjU6iUihi4fBnnL1xEkM5g27334b77t3POyjnp8hVYv/UurFm+nLPUGgavDGBgeFIHLrAwnMSRpvvjZ3CMiBe9ItBigY6hQ7KCKicl5XQbkL0LGzb/HL7x6M/jlx7/Fv7ekw/ip5/sxI5tdbx94DW8TUX32NkrGKACWgrbydx9ZMKFjC3KTTLffu5y3bGpDVmWGgjYJ6WU2WfZqVgl2DV0Hq7szQ87ayORZdfNo04lHvkcVm1eh8cebseyrgs4/85OnH71ICqDaVzuXYQLXQuQKSfRV2igA51Iqi4SGXbkUU4AisggTWpnB6+jkiuimk1iPNmG9uXrsW5NF5YuTCGfzjJN1mN+CVa0Z/G5LevRsyBjO40S1QCdlR70JnsRVi+gXh5EtVjXpgtMVsZxoXgch86/hz3vDOPAqRq6O/pw18ZNWLtgFbqL7eisdaO/7x4En9+ObevGsaHtPDqCKZQzOUxm29GzcAeWLPsccp2LUE1VkW4P3bvYpJ5yAY3JYZwv53Gh0YMS+SVfPoiOqSMYqvWgnrsH7QtXINuVQyPdQL4thU3rV2DlEpY72Y9kKYfKeBuGr5QwOlXE2q3r0b0sgykquvpS5sL2NqaTRGfPQQyPvIrieB/rrZcN18b6t28/sV462Cas1/UPYMniB7A8m8Hy+gX0FMdQHV+Dscl1WNA7gpGh13H86Bs4fOhdHB08ifMrQuSeWIvteWDVxCTjrmMsvxjtK9ZhTXsKTIXitg/Z9oVotNdQbh9F0FHDklQvFqKL9Z5DMJlAob0dxXXLkV+7Bl2czHcXq8jlJ9C3JMRyFLHo/CXUz17C2/VOXFm6BXetXI0luRzLHyLF+uhd3YHtD5MLw3Ool5JI1Mhfet2rrufg2m4bI8b8RUML+carNKdKlGNTyHZcRlCdxJX6OtR6v4itG+7Gw30XcPqVv8KhQwWMlJexf6co+RpIp/ThBh0mKqVoZkwwceyMMW4pbFCz60yda7DTwx79NRVcPQAi2Z3aSgsRJO181sOgCilorMCSvq3Ydt9GPPJTi/H5ry/Cw0/0Yc2aJHLZToSVXmRLeSyvhFgZBjiS3YHBFV/GA+sW4MsdF9F++Tj2HJnEmWIfHrp/NXpyaUwOTKIwWEaYW4Hi9q/iysYNqExNoCMxybGxgpUrqliWn8SSS4NYMVRFLcyjlGpHOZVCmWN1JaEvb6pMrjQz5hi3GsYyxlGOh+pkMw5tdmxGNtSjPtrTUz2sosLJCFsPesNLr5tk6C+sT6FUGkGWckWvTSNBfavO8b5Gv40jOHviGfznPy/gYPUbWHvXNjz+YBr3raliTVjBsvIUeTTDQVx6WoryRYuhMWLMN5AxOdPWq40ifWDrbP9ZvH/kfRw4cBDHjh+3j9zoVUebmBs1g8aIMceQHNe7TyKxoUgbEGwTAsmEvtlybhrWbLdWhtI9TekeSAJrpwDHZVGZY3WibTGWrF+OzQ/nsWpDBcMn3sGpfYfRP9KNS/ltKLYvRl/uPHqSF3Fy30H8+G9ewN98/xk8s38nDp87heqVSSwIs+jMBShPTmJkimMF56rLN9yLJSuoM3A8aSCL3r4VWL+gA4tSE5jgmNJf6sQlZbc+wTnXOHNboQ7DMUJl+IxB2t9nHn77bECFUWYtMNTIFnoaIWbN9fRi6YoeLFmax4KVC7Hm/vvx1a9+1b4e4N9LTycTSKkjhFRqqramekdCNcF5mfVTaWQqS51Kl5+gFYtFTuCAe1gHWrEenxjH66/vw7GjRzE6Osb6SyKRz7MyZ7ZN6qlmmkq5BrIJ+i9MTTk5QS+lujv/bHJyinGXMDVVRZU90V4fkaAoa9fSKArFguYlyKQyyOXyyGayyGTSSKdT1gbpVANdXW1Yv349vvLlL+MLX/gCvvXNb+JXf/VX8Yu/+IvYevddtuW/VCrap131ZLVcKXMCW7cDNBNsv3KpZJ97HRsbRcXvQJK/QpH5m0Q2l0O+rY1pBSyTZZsVxooiKQ+lcpl1o7Z3YrLKtAYHBlgvo+4T/iyPvkSir05pGjI8NILxMVYF6yKRy7IuWD9MR1+q0FfRVDb39EB8Ra5kXpRfbQkvl8pWX+V6BQHjbMu3I2AayofqTF+1euRzn7OvpH7z576JX//1X8cv/dIv4etf/zpWr17FMIG1pdpCT9womqmU60Bc7b5LsP1V9xW6F9wn4nmvgxalhPhP6RcYXl9ZUV5lp/hUPrtn/s5fuGD+lCeVoVqrYnRsDBcvXrat7dbX2KapIGt1orLGiDFfId4P1N1llpwj70t2qM+HOo+E/K2n0729C/DAg5yUPr4ab7zxOl55+WWTAeJ3xaFNGbWqm5JKrnrZGmMeQTKZ7eV1g2nonm5hrY7Ori7cc889pgv87M9+A1/76tfxta99DRs3bTA5GFLG6etkGm90X2W4IsooDA+hPjWJXG83ejduQD6fw7n+fhQ55nR19Zgs1JeKLl/m5I9sosPxTR5TphYKBVRsjKG+wTg1Vmv8IPsZAo6D7s/Dm2ZsYtw6zFrLYiHyjcZB6VNqS2ourt/TLks50t3Zje7uLo6d7ahQjgT6+pe2hBJV6iQDx47hpZdeMj3k537uG/jmN38O9959L7o7esyPdAuN0RYl7zWe6xojxnyAjXImT+3G+kCKfL982XLct307vkA99UtfehKff/RRbN60yT7ClE5Tz6aifY0MjhFjvkETGQn/qwYAMbpbUxAk/zWnTCVSWNy7GD/9Mz9jfL5z104cO3HM3DVP1LxKeuNf/dVf2RduNZ/awfn2fdvvszUH+VE6Pt4C56fDwyMoFcvIc06d4NxOcUiH0BwunXZz5hgOHCVjCGKgUOuzYY5KZBL6OpO+i4PqJOoTA1Q2KhibbKA4lcTkKHDo1BUEpRF0BWX0pJPIMUytRndxY5rKilsGblITs2pEcwnfK5knfdKapKUpkSlgZnInSZjWVM9xgtZOxywa7Lw1UphizdBbI70Za9c+js1rFqEzOI7Bi29icGgJpkrrEabPAR39rM1xJEYLmBwaRrUyzrobwqFL49h/dhhjY1X0hHl0Mm60J1BiPYa1PqRY6zrwGZkBTipHLA8B2hA0ljDnbagnx1DFcRQqZxCWF9N+AZL5BDI9SSztbMc9nQtw35JF2Hr/Zux45H7cu2UV1i7LobOngXqek9NGBduHl2LZlW5MlpdiqLEcxWon2spJrE7lkKwfwKXLz2Nq8gLKxTouDRdx6OIA+gtVVFfsQL1rIXozRSxMTKAt2cGy3o1afjNW586ht74XpYvvY/L8CKojDVQKCVy6UkR/vxaKFrJqB9HdNYR1K7JYubADl0+fxfjFKWTJN8mxEi72D+PUBS22bsWa9V9AtncSiQzrIllCiu2RpjKcTJxHR34Ipa4QhQ49SehAtr6Igq0bSSbRtjqP7nInNi/YiOVrvoBFW7+FLXd9GV9ZvQz3d2SRX9GGzJocuttH0Dl2FI2LxzExReHIedToWIBTR+uYuJBBdqoT2bANEwvqGO2qIAzyqCbYNgMTSB48heqB91EfPIVKsYQz5wOcvZTDMCeBlfsWo/vePnyx+wruKh/G2JlhTF2poTYZojhaxIVzkzhxrA1LVz2IvmVUfNrZLkm3i63WaM7cYsSYp1A/zJBNU/UG+0SIUhu7YL2IdFIH1XcjTObt6zkb163Er/69n0Vx7D28++arGLrcQK2ygppPF4LkBFKUIbMjMl7EuDXQgiVJyo8pQDYs8ofkR0j7pU7gnvHqdQAqrGoaPeRIZlBoBLiYmMRgWES1lEHbZC96ql3oSnRyohZSsR1BOriCSq6AS905DPbkse3yBbTvehN/+14DTyW/gPxDX8Q//+kSHlm4B3/zo1fx1vEJFPM9CBYvQkc4hi2Hf4iV77yKyeIkLlB+HjxdxfunU7icWI7R7VtxamUS2eoldBT7eZ1CiupKwEy6P8dJzjRzjXGLwOrVLi7HPartGf7SArl22CepPwUp7WyuoV4t2TleWsAcr9aoN00gM34J9VoZY7UOXKL/YvE0KhdexrE9T+Ev/vrbePGt43j4mz+F7Z/fipWdAdrHhuyMr4FaFhOZNsbLTHDilKGOk0fJdhzEiHG74CbllKnWJWakkvUO9gk9CF+0eDHu3rYNn3/sMXtQ/dDDD3Fesdbc3NEojMEJ5Bgxbisc987ApL143PhcV6dXGMPaP82JDCaSbRgJMygnulCq5TFcacNodjXW3bUJ32wbxZZLbwETo7iU7sRAjuND5QDnSS+gHK7Gxnu+hYce/Tlsv+8xbNzAeebybuqb47iic6V7l2DlohS6q+/jyolXcPr0Fc7lmO5wHYOXijhdSGOyfQVWLVqDR7IFbGAua5kOlDJdVBT0zpU2Onz2oDH5Mw0JZr9iqnduQ2m2IioPhcIkzpw4jn17d2PXrt3Ys/d17Ny5Gy++8DL27nsTfQu6sXzZEvR0aueRziQS47sdLfMfKrMn/bqrIN1NnzgVeyQSAc1AqVTGVEFfKtT2fDoF7Vi6bDXu3XYXli5eiLGRKRQLoX3ZUDPDvsVdWLZkEerlKva/8SaeffYnrMOdeO/Q+3j/+EkMD40irNZtx0OhVMAk63p8vMB7zirrrL+wZK8BFAolTKons3tqFwWnjswTlcWK0qvSa4CuvgVYt2k9Ojvace7kGbyx5w2cOHkcB99/D4cOHcHF80MoTZbRqOkLMQw7XACKWlzSAbAZhAntVurCpjVrEQQVvPXWbrz26st45ZVX2d57cPjYMaRzeWy8+z50Lcggn9WuPk6EmB+Fz2S7KIz60N2exIX+00z/dex6dRde3/cG3tz/DoYvDGJsdIqysIqenjasWrkUi5jnk8dPYDfjf2XXEex6cTfefmM/Ll4eQr6tF6tWr0MqlbBDcKdH/rDG/wLCegnjhQkUKkXXFvoKR5BG0M02WbEU7dk2nDp2CkeOnMKxk+dx9OgZHDtwGGePncTFsYsI2tJYtqwP+aBhZ7I9//zzeOGFV/Darj3YvXs/+k/2ozLO+q+FmChPYarKCTrbRTxSZFtose7Iu+/inf2v4+UXX8Irr+5Bf/8A0u3t6Fu1FD2Le7C8l+a2FI4fOYY9Ow9h5ytvYs/uPdj/5js4ceICVq9ZT4VnAXJZnRlHnmq+Zx4jxnyCe71ihi8lG7WjN2DfcTuCQ1SrZVTKZdRqCcoXDqlBCh0LFmDL5k1Y2KezB8cxOjppZ/TRkaTXlLVgbVHGmFN8yEpXm5tCqzbz7e9HSbYzB8USx5KpUhHlYgXJeoCMHgyValRadUwAOaNRRrFSwEixgGJYx+Sli3jj5Zex5533MZbowNYdD+KrX9iO9Ss68N7Bwzh64gzjK3OMWYCli/qQLY3j0J6deOnll7Bzzz7K59dx+Mhp1KhIr9i0Ufo0FWCmzbRSSXsp0x44Ox1ceRfpXxYxbiuabSJO0s6/M6dPUa/cSx3jFezZtw/vvPM23ti3G8/+5Fm8tvswTl8g74xPYvDMMezftwuvvbYTb717EOcuX8S+/Qfx7I+fxfM/eoa61Vu4NEg9QJMtlwj/7OVKmkUxYtw+uKHTyaYoZG27vYIA7W3t6OrsQiepo70DuVy2ucPLusw1YWPEuJ24lh+bjGo7bXklc5veqIkz/yt1fQiujnKlhmIpJJG3gzwWLVqMu9csw9qFNeQbRYyOTWBoYhzpoMb+kEaBc9SLl4dxeWDI3o45zXnXGZ3PPDaMEudmnT29WLxoAZJhEcfeP4BdO/fhxZeOYM9LOznPeptxTaFzwSLbTbmoI29nizZ0/IHm9MoblYXPYt/6zC96XTXRtsWFGvTZ70Qthzrn+gMDp/Hm2zvxwq7v48Xdz+D5117HK3su4tJQOx6+fzu2blyHxd1Z5JN1TmdqCNwBWc0Io5AQv90s5t5QdnDrvFKO3MGpmoxleO/s0NBrh21IBp3IZNrQ29tjC3wdnR32sFvlaWeHWrfjUWx+7Ems2rwa9yycxOaOIdTbNqJjzWPYdM99WL20DSPnT+HF5/fgwIHzmGC4rlXLsGL5MizPt6OH+cjll2Dpsi1YujiJ3q4GsqkONOpLOLFkh13bh96l7WjP1Ww3RSLViWT3WvQs24i+njLaspPI9fThnkeexKYNq1G8cAivP/93ePaF3Xjh1dexe9cbOHrkDMZG9QWNRWjrWIHetRxcF6SwghPXlWz/rkwWuWUrsPbBh/DAxtVIDF3B+/v2YtfzL2HvW4dwqZJjOb+Ibz2xFWu6A+YvhTAh0qH8gR3AvuTujdjwuR3ozoS4fHg/Xn9lJ/a9ew4T1XZsXMsJMMvR2bYM7V3rsXLLdmx68D4ku5KYeOO7OPHDv8VP9hzD7pEOhIs24P7Ny7BpaR6seaTDhDtfjXVeS/ehkn8Etc7Ps64zWJlj+QNOoKkgVClEEx1LsXTrPdh+bwbjo3vw5uvP4aUXX8GLL+/G87v24c2DRzAyVEcu2YV1a9ZjHcuaShRwaOdP8PL3voPXWGcnT13EgNYE8wvRuXg5tixLY2VXFeXGItQya7FkxUKsWFFHrXwe7+3aj13P7sVrh/tR71uNNes3YNOSHqxY1I2eex/A0vs/h6W1SVza/Rpee3YPntt9BgfPjCPXm8G2ezZgzdIe1lcSyYadVmaKULzwFWM+w5SFBOVoQl9v7eJ9FzILl2DB+pXozdWxoFFGO2Vm0LGBMmo7Ht5xHx6+ewU2rVuChX1dyGb0bE27aSVvY8wPmORp/jrSGG6yiOQWEdxrqWZi27d19aFv6UIsWNqBji4gmyhDL60ngik2r7543E2Zthzt7cuwbmknVvTlMDQ1hbOXB5AkD2zcuhH3c+zctOGL2Lb5y7iruw2ZkQFUKhwTVz2Aex95BHfdlcHgpV344U9ewyu738e75ycx2rYEK9bfhS+t4BjB/CRSGQ7lWYRkqzrHx5C8afmP4FqbGLcMpuM5PU/rpVKV9MS/LlIzkIn0iuPguQt4Z++beHHPXhy8cA6TYQ2VsRGcevctvLd7HyYHRlAt1zBcKOHSeBW1Wi91oMU4fXI3dr/2HVsce/H5N/DW/uO4OHjFXp3l9IqJud3StssgljExbiNmdDlJzxk4s+ZD5FH1F/3zOkPmodmLiGnDdfBB7jFifEyItUQ25bW5s8hxsH6lD7jzviRrHcms84kbySyqyRyCrqXoWr4Byxb1YHG+gZ5EFd0M0xYsRmbbk1jyxM9g+d2LOG8awYK2Cudx92HJmiexdQnnRZffwlGOCfvfPIr3T5zHaFDD0m0b0dPdhV4qHmvXbcDKdRuRSSUwcXwfDrzwQ/xg1xEcHgqwdOkSfP6upbh79QJ7jVLrGwnOtTQa6aN9n9V+oyNKfk+G3/09u9xUSIDpPVWt6At6P/XYsWPo6+uzs4bs3dQmvMDz5psNCeDrxTvjJjZmfhtJBCGVyWqIQvEMRqiMUgVBLdBUpQOduXVYvX4HHvnS53D3lvVk1KQd1B3YZMilEdg1Su7CUjrz9PXmYbbyqWyq/5GREezd9zpGx0axeeNGTsYeZE9WJ2UnsGA0a8cQByLtQnDfJ0zTTS96JpBta8fi5SuwYvUarFi+CHnVWTpAqrMTmZ4eTvAWYfPd67Fj0wKsXrqG/hegs6MNnVmKAHa2YqYbK1ffi1VMe+M9W+2LjNvXb8CqBb1Ise7aOjmJ2LwZG7eswoquDDpC7TDrRCrTh7VbV2HdlqVozzO9ql4b6EC6bxkymzihWNWHlekEenoXIp/NIl2ZRKI2hXHlLduBXGoxlixaTIHSiwUUEol0JxLdvVi3aSXWLe7B0vYcOtnUyTzbsLMbC3M96ErqrDCmE6SQ716IZZvuxY7PfRmfv28jlvVm6KYVc/FCAim9TkI5mOqoI9PbhVyeAkZPrzIBuvuWYv3m+7Bm2/14cMcW3LtpExYtWITOnk7kF+QpFEP0hZPorZZQ6lmH9LoHsWn7g3js/k3YuKIHOU6eUlSSxUt68tVIsi0SC1HLrMSypeuxeU0fy9aJbE6P/JkX+sn1tiHfNoZsdpyKcgqVWhsnQm1I6pB+1sHaNavR19WFboZpzwachLNvVsvQJ++7etayjdZi3ca16FmyBPmuHqxa1I4Ht+lDAuvQCHrQ0ZPG8hVZLGW6HY02BPU8qktWYetDj+H+++/DxpWLsLArhWx3CsnOXiwG261SQo15q3UuRA/zfe8O1sdD27CGk8E8Wc7tmSGfahFR33gnxMvX668x7mxop8PAwIB9onxsbMzORVq5ciX7lRbi51fbX5MP9XflL6ndWjqzKUve7kH34uXYvJmysa+L40MbUkEH5Uc7uiizli/qxrp7P4et997N/teNrk6pSQmk9Yr5bOOA4jf7218HfvzQOK5Dh/v7++2gYSlR27dvRyflvx/f51O73RgzdatfqaxOClFfae6Y0ViuM7l01qNstM+1Jr1A97VxSSs0Fi7H8vVrsH7VEiztzKM9lUKQGbUzEethjvFpbOOYQjm6ZcMqdC1ot6e9yzdvxfYHd9gDs758Nzral6I3y3FuySIsW74KvUtWoG9RB5Z0TyGXnsTl+iKOp8vQs3wj1t/3EHY88AAeWrUMq7KUsamqjeO1ZAp1toPyO6PPOi5q3vg7fzuv4fnIX/0EWvc6Q+/pp582/VFnV65atWpadkR5cS5h+bM0fc/lX+jMNSoINTUKuUYPsPR64+ToCKbGJjimJrBg+TKs33I3Nm64GyuWLsXCJb3YtnENlnZUUW8UqHd2YdGS+7H5ru3oWAR0dSXIN9JnlmMBx97FG5ejbyH5qF5gFsi3rINGQmeGkT8sB7cHrW3gZYlw+PBhmw+oLR9++GFs27bNZEy03ee6DWPcCrANZ2lGa9tI+8p0lZ2MzWsrZOWk8iyOMe5IqO0lHw4dOoRTp07ZeZWbOF/Sq64yy+12yQTHbyR9+VC6wvSuWrsjSc5Ldmk5SR85otTlXEZf2Tc9oV7i3HIBFq/bijVrVmB1XxaLOS9O1rModyxGuGANEksXYOPWxXjgno1Yvmo7ens4TysMoL0xDk4Yke5cgt5e6gerluPeR3Zgy457sGLJYiyifqm5ZqZND9+60I4Swmwvlm7kHOvBB/Hgveuxbjl1zras5VE6K1UEGxfUh25HfX5YRMd8jQ06F3fXrl1oa2szvtD5ZjL7MUVoLU/0/j/9x/9oVzaNtRsVOpfAJ4XPqKAEa7WaMa3wR3/0R/jBD35gzPzv/t2/Q3d3t9lHGdqbbzauF6/Pr3MnU8uLXlGpiSq8PYtyqYizJWBoMkS+3k6GpRKazyO5VAcZAymVkRWvyq+zcSrVCtrSGUbUkh5vxWruf6ahbgZ8+Xx5BJl1KHoQBDh58iT+v//993HqzFn83Ne/ht/5rf+nvacTNmpNphEn6IlMiHqiQmOItD001ETAvumIcsOd65Wm9w6WE6G+MFS11wbLrLrhtj52+gYW2deKJtipS6hPTFDBG8OFVBv77jLWmw5opzv9ZUJ2fNVxOMp4ErhExb/MfHRXR9DVmEQj2YZwYqF9xKiWZb6CMlLFKtKlOiqs+P4uTiyZw5XlMWTYBmG5hspkGaNTkziXLNhnvTtyG9HGtupIldBGgdBIpFAotyGTZQvoPSX+JzHJSQ6Fi9p9Mo/aVAUXJ0dpyzrN5ZHv6OJEtRt5Heij+tWEl38BzVqUUpsmMKjZPEYm2zFZoHBh3eRzDXbKdhQ6lrIdgB5Gn6V9IjHFfEyhNj6JyakqxkfqmOpZjkYbhVY2jQVtKTuQsGpnBSXZTMykEFaRqBVYGVSaE8sQZqRE0p7uQaOKfMgyJKfYfgVMUKkeHMliqsQ6SumA3F5OUFNgdpBJVhCUJ4DiFKYmC7g8WkCl0Yn2JRuR0gJiHsgFnNAr01SidRCisZXdM322UqMcojxcw8jQFIZ6GHdvL7rbM8ikpdiz7usX6Z/1MLDcXn0dZG3q/KP2Lgpgau55mnOqXy0ciOcYv+YFKfKYlwW3Qg7EuD2Iyll9LOLAgQN2MPOZM2fwK7/yK3j00UeRZz/1cmw+tb3y5ElnkZBd+T9JkTlM2SHFZiGKE+T7PCfe9iCBsjNBuaq+XpliP2hgLOhFNZWjLKYkDYoM10BHo8Ml0AJXdk+3Dyqvxg+N3xrH9cBKSocU00WLFuEf/+N/bIqHxpf52G4fBD2zFbTTVHf2DFQaEZHhiBfW9FEPt2xQ5ZhWbqRs7MvWzwPj4xjqWIVauhN5lrlNw4LGgiTlnj0O0XhK3tC5mLUcJ/chcu2UmzqMnnxQT6eRDivIVieQyKRRL3VzXGK6lIvpDNOtj6JRvISQusfBiQUMn0E3ld6u7jbkyGZK087wSo5Yfit6OMWxTXpFhjLUeMf9T0OjlLvOb3he8ldBSq+/18dR/uk//aemP/7ar/0aHnvsMZMdQpQX5xpNCdf8lW5DZuFtiX2+xnEuRbPOfmVhKBPIC9S92MM4TNZQq2vnOPXhLMfsoEb5wTYOr7CNJ6kfUbEPl9iZl0PJCftwTVeDdsU09MZ0pdvpIt3UuTQhqyfTjEsLXvo0ze1p7dY20L3aUO0jPPXUUzYfUFv+zu/8Dn75l3/ZZEx00fJ2tGGMWwH1CdcvWqGzEh3U1mp71+b2e1Xz+zh8PDN+Y9yZkEwQCerrkg9/8zd/gxdeeMEeaHzjG9/Al770JTP7BfG5lglXcZzfRUsZS+k+rT8Ige2y5dSMclduyqVm09ItksULdOAcL7cYlXQ70pyrtXOOlFD5Td9IYqgeoEpzNsXxi6yt88TzA5c5F53EBU6AK+096GnvAKdwls54Ru8YcR5eHka2OIpyNYErHD+GhzkHZMYWL16GfHuW8znOqbR5opkfXx5Vu/QBfWRuvspZtbmg/OnhiBZD//N//s9YuHAhnnzySezYscM2UPn1JfFSdAGsdQzy8+gZH59yXK9ho/aJ+ghpgLU1Rb5JUHnQqwOrkO29G6tWbMNdm7dj4+aNWLSyB50LM6zgElXjSdS1cMMJfhAmqCyn0JGm5jotlCPUmLn6zj6noOKV4GRMzK9uqt7lOrKUL60Cy1RDpTZFP1rgoCLZyFPp0p4vKmzU2rQxyM6RYtlriTLK9SyqwUKk2xZw6ldGL5W0WrVBt06EjUUIsuvRueI+rF6zhgq7PvOuHQ56uVKvkU5xUlVCg8IAuUVYmmhgRVhiOp0oZlejlOoD5xSgHECOk4P2OsNQuS30cgLZ2YEVGMEqvTCZ7UIp14tQiymLV2Pp2s24b/U6bFy+HIsWppHj3LLKjE+mOZXhBCPZVkIixYkF07O3UbW7SGeRSTS055Fauggr16/Hlg0bsWnVKqzs60ZXhpOW+jhypSEE5SkEVND0ciNSGdQ5MaoHVFjblqJz8WIsXrMCS9esR9/iDWjrWooORtudZZmVFusL9R4KvCVId29CdtV29N2zAxtXBbhr0SjWdk2hg+XV7jGbMCFrCmy11mDHZ0TJRawMTjTbQnvKn2WdtFcoIKvMf7kPmFyNkepWBD2fx9L1d2Pt1gVYu6GB1csn0dc5yvKOk9jaQRsanUvRvmwzVq+/D1u3bGbeC8j00p1Kt3Y6ptN5TsD08QCmH4yjnJlAJakdD+0I093ILl2IZds2YN3aJVjYk0V7ivxfp8Cvd6AcbEIttwWJZZ3o3bIUa+lPXzVbsWQR+tqp2zMPDS2uks+0yyxZSaNR/syIoxh3IDRW2IHm9giA8j9cinqlB0UqK40uysh6A7kye2yd/pJUYpI5itkF1GCWoDvIoZuiNl3j5BbtlK+UFxoOrkFzjIhxy6DRT6RadhLH2/hfgTKJyq1vCapPHM+S9nAHIWV4Wx/6Eln0sa31LESnTk4GCVQSfVTWutGoUshVcwwV2NlbQY4xhQMcqziGhGPo4HiWovJboFZaDlJI5YroaptALlHk+BIirPWi2H4f6osf5Ti0GfduXYMViyhj01WOoXWO0bAFDw4GLEieeXW7eizH0ml8xg26ucoixk2G9CcO7GbSZCKhmUuTrbSv00hmPTiSQQuUKY6t1F1qnNAkOrqQz2T0TR8sDofQW76EQqMLA+mNmEgtRYL6Rppx5vILESR70KAuk+oK0dlZRl+tiG5OfELTQ5Icn9PkQekzcZvHmA8QH0rSzkJ6iGTyyvGqfmOujTFfEOVcTsiMtFhltyRJfFGNP5WavrBPW8l52lU5152kvsfJGNCxlBpjDm0VPTTTRhLaU4aXwjLnylX0ce60mPPm/FQVGcp5ez1y4QoEa7ZgwbIVWNCZRTZTQBCMcX42gjbO+7TRI9nQg5J1yPSsxpJFGWzZ0odtG1diUWeAzkwFOc7T0SigSKpq/s+5bsD5VtDQ7FXawmevt1lbxpDMZeNrxZAKqF5P4EXrGc6OzBVysqONQWm5Baw4msX0ZEXkc3mkFEA7W+hXy6hacRQpXk+t9/MRASdwuXTOOoRBF2ZVB9vrqb/KrIUvPRdXmTNacWbRNRWso4ZsMkM7p9fJr8LqYY7WmNnVrDq1gCu7JG8CW8WX2KCQsK8T6hUSW07SdMFFIkGSoRJHhU6weInpPBIWRgMokaA5k29DJshwkqInCGy3JPMapK3es6mseyJsvpttrxXiSJsk6J5sPuWXnkoZ48D8prM5ZkeLnsoh+YF1JtJh7DroX7DomEK1oloJKQBZd3LT8rztMKNgo6RU3CqWkrZddppUq25ol80ybosnYa9vaMeVLX6L6FvPcfUKpnYjWFWwbsmOFI70YkVJsK3IoZxwq/51cparAx0gyroXPypYimVNJVHS1lhFrris4IpD7WVLotZ+aYZPZ7LsGyy/pe12ZvlsKd96uqAsVXTQSPObDvKjPFTDKtu5TndNB53Yld9Mhu2Sc3FZe8SIMY8Q5cmE+k2T77XrQnytPsqL9Z1QXyOlTJNMMoGnTs6+rzew7IMn9KSHCxZG0U5T8z7GbcDVFW9S3A/yhMkoNmVa8luQoKNSq1DyJpEuJ5Np4g0JwTR5g/4k9sUG1r6Su2QEG/voR2Ot5Diqek2RcZosF7mElLwOxFVKKdpJ/mYYVmOsvdGnOJmAxmf9eShfoqt/Y8wVTFywGUWBdBotSlJHMDmip3jkEbV5LdSDH/mRvkE3jbnGMGxn8oLWSu0JtRqb/KQmzzJojWGr0jWbPKOHgYrDcWSMGHcGxK3TJD6P2TfGHQibC+tBhGRxk42lF+g7XSa7OXFLBQ03jZWclyORz3D8N12S9lnG0ca5qZzpVioB5YrEfgrtOc7jOG/V8QUZXqUDZBlvwDGBioFtWNE7M5pRSbdQhHXOs0JOXGWXSep1d3oyhcL3N+XgswfV7Wce0xOaeieZs5c8kYcOha2RDKkM0lRaUnp6F9ZQTxTJoVUqIJz489ee6qkqydQJvROYnPlUtOL2dLuhpYkku4Z2cen1RdcH2EEa2n3AiRjv68xnKNVK53vVqEZX6U+rwwmWNpFhiRmsoe7Vxlja6EblvdJgkbUwkqOdPoVaQDY5hWRmCo1cAY2MXmFkZ0YW7aybdr2myMQbtSwa2mGl99qUk0QOyUaGCjyVQcaBButRKymaUehluFqGEwB1XS1AJpFtdCPd6LQddqbuUZkMs0mEnJk0whybow09lCDdbMeMiQQt/Gg3m6KlcNI2L05Qdf4FGl107UGVAqOYqKGi1+6aO+P0qlLa6quD/toZWEJM57bUUKLSqn1yevqfDDtQZU7KzK7SkIDSq5ztTKtdiq/mMYqXf1XmtU6J2B5MIJsYZx46GGYxhVQXkmVmiwIvUGZJlbCKihakggLrdIL1wTDkOU2wqskapoIiikEJDQVgs7Uz8Q7Gka6rtZhfxpkq9SBVXIAi24yhUWQ910kSlo0024jtlUMv205HLKrSJ+w1ySkWrSpByz5BMWvtW6RJu1u0A0xKd57e20nayaaFPS1iJhtl5FM1lHMNlLS5jfWcZj21MZx6jbpIhbxTaaStZfQ0ItEoTfeT+dBfYsQQojypvTTsiNCXZKso2zih3b3G0xl2cHUJes9oEsswJd4UMnrliDdkc70Cl6aBXcKgGGf+dB/jVsKNNI5cXUvWeZuoOxuMbWg3etijB1o0Gi+kOA6kKFfTHEU4lmU5PkgGikKOjWX+lZIFlEl17QqkWE5QHtfCTsbRTTndyaE1b68shhVyjnb/0g5JxqlFsgzHHT2lDSrkFb3ypdGE42M9gWyVY11FT5SrJmf1WmM1KUVZoyuzRH8znBTz1FxBj3Skl+g6DfV5knQdagdI+0VwW9Qk6QzSoI3uOY594jUyUBCill6Imna500+7xlHqQ7IXr6ar5AOyQ47egxRlEHWnEtu/kKR+RD5KNnLkR/ICG53qaIwYdwBiKRVjHsMpBDdE6De70KN0PG3U0AYFcXVI+Ywga2/vJKra6NDAFGX0BH1PcT42xTlarcS52hTnpGXNk0p0KZqM53SWY7vPgEaXPCpUJoN6GclakdacfTIRfcxMn9LTIxQdN6Q5nBbXtHFDCqlGJ9NplKNmd9OzFXtr6zMG1UIMwk1syGWatahaxBuyEmyyo/dfvb6iXVvyLf80iOvMn4icZEw6/+By6TuQz6Nl2nUcmqZtEyooS82OY5M9OhjRh94DDm3ixy6uRSiGtYP7WB/qQ+p+OgXMrloIZBx62qk61JcidY6T64ZaFedkkaRdZAmrR/nSgo7M7MBa+JFRAkNpWDousw1OApSmvYbCTLj8u7LYjiga/BN4udguJovMk7OzT8syLtfuLj+uPqzAitHIu9uVUN5FcpGd8iKfmqLYji9mQvnS15rsNUpXgVavOghfez2SVhfaQScxRd6zMlqEVt/Gc00L5VaLZiKrK7orjw3zSGtlS0lIR1Z4/jlBxzjrVL11bgjvlUd5dld51A41CUrPz4yEeVIGlLR50R/TdDWhOF0Z9N61JnXSyc2WdsqvyzfzRktVrbKrGjI/ulFR+OcKq/RowUmc8ZrZxYgxf+D50kh/YtEmhWTwWs31DTG+HSbOP70KWbc+T65XgGktw5bcFW2M+Y7phnZSSmTCjOOenUej8UwSkQ5O/qll9Se/WiijuwIxnmRKO271mhtdqUDoqbB7MqyQlL3Nj3hYYMleH95bOWuTrzM7mx3JzUl0y2GM2w3fDGwYGwvNyD/jJzraGCs7NyoaD7hBk5Ma6VEpcgRHZPoTHzg38guvKXm1CB2HufGYJN2BA64bXxm/KUExYsSIEeNWwt7i4lUkUW0fvOFV96YXiiTy7bUhzffc/K9q8pujtgWiLyoSbgyvm4yXtUNzvKCMtw9+0UFpmK5JP0Y2lmgOR79NOzdGaH6nNHWvnxnMxP/ZgUbLGE2E5ABjRCoMOpDelA1N/nXulVdSjJkcU2qHkQ6TTaDM+wL1jBpqjRRdtHA2D2EKlBmYaZWN1+YuNe3QcSqUIOWJnWdakydRkdK7zNopJpUsYE0FOh/Mlq9NnUOGE780J4BVll97ueraEVXTk2wqa40Sw1QYUgsvJMbdCMrstIzD75RjXNrlpUzYDjrVo/qwJc/ckfT0MqN6V3sk6vRfAbPhyFbImAZvasyT3qxrlJh5UrLqzxJz0wiVXl9XStJgAohtr8UZFVlJqpzaF2YCg+k6AeVIiz2uzPLLCEImXnXCTPliqRle9VJpEuPWa4uMBSovy6l0GqzTmu2e0tkvqiM6qyCpAiOeUjVYGlJ/3YsNeu6vPWvuq6eWV06U0iLzzDwovApA0hOClBRfTb4ZXBu/MrUGcnXmkdYqO6hg27kwpAwrIMc60QJlI3A8nGGZ5Ffnurln1k64W4vptVRN/CynhPGCaqrOrNCuRsFNK7WZ/Ks+dR6SbWVLkdSPfHAp6hTmMWLMazRZXZKwod2wJqdclzOQjzXf1BM3yR+5mg96CK0jOBlm8ivGvIRaRq90O5lEkvZpC0yCWpvtLhlJ+eXGTAoxBSIFIWV1mGH7uv1/UlIlYnW0h76wWCEjaLxRbPZVXsXItKo0VEg6zJYSl3GRayhz9TVbaRRJhkxo57M+HEOhqq9Male2NvfahnSOoRpX9RJ6jNsB35/FN+5OzWJNo2GxSX4ZUx8HUvvJo8ZxTXSkE9XpSfLBNnZJLyI/6NJIUq8JSraOJdGhowqknWisTVHSpKl7Sp+REmNDL42iGDHuWJCPY8SY75CY1eKTE8yc+3A+qAPsteHCxnfPyPKjxTEtWnGctuNiKLv10ZwgxXFdpJkm9UqdGVtPVqkXlBiw5j5aQ10gqbO4dB6k5k4cLzQnlpzXnDTNkSDgYOH0UukZjjSP1gxS52lLpalrnLFFMOZVg89nDGqTGE1ICdGUvUaznfwvZZaMQVVUNsbcThLrhTYd9s1JDSmhdxcSBfrWSS16XUtM93Gh+FvpJkIds6msmxZm2+rVLWWjjsBy0q5hCpfSVh0onHqWGEYKeBUpdkhRUnEQ8qo3O7VwolfWygnWAxV/1Ki81/TEUt9lLDMKLXrptTqG0ztu2pbEtHTmRSOprZqqa0Edmx3W6/BS/JiIFt7SbJK0Fqyo8TcaFBTU8rTeI0GTsMPRK6gF+tIkBUCF+S5x4sBrlklKDMwsekmQ0D1Jv3rdkEJJMkB+pEyqjbUTTIth+qqX9kJp0cs+ay+FlRFoqmFf/9JJhjqrivnTS4X2OiTrR4te7twfQZzldsCp40kG1qBXQvO8d19a0mIiAn0Zboph+W91rj8temVRa+QsjOVddU5BqIMPla7xqhbVNGdiAqq6NO2146rGTFVJuboO5NerMrSndx1smGB8yUQeWUrPvBa9ODlr6NVFllOLZhK4moQ1SMoNs2XtYF8mUU2ahdhDHlVGRqxJIwcALXppMU95NZVfi4BU3pGSMCe30V6LfzapbJ5jEyPGfIV1M4N41Xq6jtSB3mw0/YGknTxVsrTGkwzvbUFaCoq6T+AW34N4F8ZtQ7OZHGYa9CrYQ6Bpj5JPEnJNJNmQOs/QrNiOPg4akzoktk6eoKzUwpcUVFvwIumlBS1qaWxNatwRCxg1UCX/VCgoq/TvF72SDBTUpbDqXA49WCNpvGMgjZKStFr0stfgNWZzBPGLXpHcxpgzzPCShrTphSdaSz/R1S14JU030YM2OUuP1DgfclAXZclYftFLX/fSWB4my6SSbRTVIpoeoklfkyaTblSoE3FcVRokXXQkQajF2hgxbjrE5630SXCDOD5p1DFifELMcKektaeoifAbAHTVGyvUCSR9HTWZWPJYr7dTd9Cil+Z8ms2lQ2oGmiuK6DfJsT9B3SEMOI+l3LdtJNQRUnXpDVr40vqCBgg3Y9f8VIteWvASae7coD6grSkypxhfhspnQI8MTv9a7tLc2QYZ0mcLqqEYTYiB3QQmgA6maz6HFUdNM7e7auKvFVtvQX9UVu3weu9xHsAOTr8KzQxLI/OQtqWLkfuTjStb07+gIpqS1ly3tp+mu/7Vv1RdJNWBlmlsK7/1O4YK3GkjypLLVtOzLSDpnvbs2Doc3h9kb9bql7rhnX91ZAbs6Gon/w4jL4pa6ciX+dRE0yabJDrKRSLDYBmxXE37V5aVb8ui+dZCFIUJC6VyyY+bECmM2puTEpsE+XK4OF1EtGvWtR1qbR4c6Zfz32kbgwU1F5a5OamKOMroXmnR0qSDHarNuO31CAvrApg7I9Chyjq0fzoaXwiRomJSM7HNQPEltfClg8imAzv44FcHm86RI6VDAW/BaVSdqh4l7F3Cakv+0qitulZXMWLMc1ifbPKs69Pke/fPH2eQH3G3cbjZse/K3v5cELO/Q2GveFpF3LmYyb03uat+TSzqtcNZ3K6Gk2Nu5y+NnoRm85rca3G28cMxgSNLy/NMMwo56cGBrt5WMrJZ79P+XBYMTVaLcdugFnHtI0w3jayaDTbDU97s7v0YbON703o6POHUoJSdiawx1Q7H531SkxwFFa9IyCg4w/pY7zTc6XIlxsdFs91nY9k7j41jfCohHnV86qXUtI14VLJLb8iIZn3gQE+U0V7EO1B/oOzWuK2P3yT1hRo56p5u9gEUN0kj6ce5mX+5MB1NPZ1dw3RSTdvcCz6ydEF01e51DRHaYW4fPTFZO5OTTwOuXfO4FrO1zC3DfFeWtRii9RFd3bILGTCZ542+jCOVQxWml1X0yfl2eXKkA87RQ7c2e/Yv+vjwjBilD4av19nqWPfGDKYgqRQpKuq8kvH1pbFGsoE0zfqOlA5ctXPjjehfPUoWVilS0zIsMuskQWII253j60EFp7821lEHKa2wVqGqyzbG3IEM85JhdDrO3OrQ4uCFlAxyzKsOvNfmTgZVHnQ6L+O2RRj+6XwwF6d3JPn8JZW3Dtq08Q/KpTWfS4YeUnqNUB+ObbrpU1xpLVolLSZrN0XLdNL0kWYsWouXcqno8/Qu0rkaCdaf4tIRtcozcqR8xhZMadMMwYQTOsZeMdJIPkKgw4r12ovLsvw2q82t+wSMJ9nHmwUukAXUvxaNnF+FUfOpXpoRkxSOJdOV/iVzPRvIi8Kp3EjzzoiOrEcFVbzyo6SNLXzZtGVMbah0lISC0UhvDM6bFE1GjIvtYguAdE0qD2xLkZ0/I2dLQ31HLdNplGEcduCuJarErQVifIrRKpuig9RssmveodnnlE0Z1VMk3izbzT6lBXLt3dQ3cN2qrvqG6786jwEBPanfWK+bjRTZ7a0HtcuHbYsPo2jMF6hEzSZ0kByTnCP5w+Alhczd2o53pBRllMYMkWsatbxamfLd5J1ZOZKQtNV++XF6g+LtpKcOUoYMYw9qRJLF9Kp4JRklo5W+gtun+0wkauzspKzm2JHWl6LTNqRJ6/BpKqs+SuWdl+lrK8W4FZhueKtk1b3uRGobs9ZCufGD9Bu9/KoHpfRMNz0wlc6gV170T6OFc/5zjEf6ZafZidIJ2bWTZ6VPkDIixkV+EUuJn6Qn3A5cTx5M66HXgZc3834M+MxD7dNKHxfNzuHjaI3Wk/14vxH/MWLcYkgcmUjS5gYRdQbdeokvQiA9Qe4S3KSmH8el5FfpfSbQOQbworFe43dAU5DqpjNtLDzDMZB0SmkcGekXOghfX2nMKHwzuoSb4Wq8UD70hd+kwstR3hgkpU0H1Gv0xpQ8BQzv52K2OKZ8ztN+NNs40WqnccKPKd4cxfXGEVZPjBgxYsSIcetxo0lPjBgxYsSIESNGjBgxYtxsxIteMWLEiBEjRowYMWLEiBEjRowYMW4rrrdb65MgXvSKESNGjBi3BbdiUIsRI0aMGDFixIgRI8adhei8IGq+GW+KxIteMWLEiBHjtiN+9TFGjBgxYsSIESNGjM8ubtUD8XjRK0aMGDFi3HJ8mEWteOErRowYMWLEiBEjRowYNxPxoleMGDFixIgRI0aMGDFixIgRI0aMeQk9HP+4D8jjRa8YMWLEiHHLMNvgpK3L8XleMWLEiBEjRowYMWLEuNWIF71ixIgRI0aMGDFixIgRI0aMGDFizDt80iNQbvqiV3TbWRiG9jRfV28W1ev1aX+6TyZdNqKFiZpjfDB8fUXrrbXuPbx9NEyU7mR8GsowF4i2940oRoyPgtl4Jyp7vL334+WTR2vYGHMLX/++zXxb6F7jtLfXtVKpTJvlz48p0faMEeOjwvOYlw2eJz2iZg8fRoiaY8wt1Daq/2gb+PbzblE7zQVqtdq0+YPgw3mKESPG/Ifvq639VmbJeMkFvw7gzbp6XULm2cJej2Lc+VA7eh3A84JI9lF++ai46YteyoxI8JkTopmOLnJ5it5HzTF9dJLy4JljtrqUm2+P6ETGo9V/TDHFFNOHoShmcxd52SQSdO9JdpJf0QcjMc09qS18G8hcrVZtkUsTVG+vsSPqz8O3Y0wxfRyajX9k5+2jOqXgeVAks3h1tjhimjuK1r9H1F5tJ5IMSaVS0/dR+PAxxRTTp4Oi/drD30tui7wc9/ber5cPUbvrIRo2pjuP1P5CtM2FIAiuGSc+Km75olcUnpE1yLUufAnRsJ+0YDEconUdXeCSWfXu61xm3z6fBni+mg/lieblejTX8O3+QRTj9mA2HonSnYRofj1f+clOVD7FfHf70Vr/UjIEb697tZmQyWTs6ts32o4xYnwczCYrWs3iM09R+xi3H9G28G3Z2j6y9+2mNvTyRPdy8zQbfDhPMWLEmP+I9tVWc/Re+oUnL+OFG8mEGJ8+qK2jvOHbXmNFq91HRYIqrYWs3WSGUoa0YiumlVnXP/zDP8QPf/hDbNmyBf/yX/5LtLe3N31f3RFifHR4JvFmD884J06cwP/8n/8Tp0+fxk//9E/jt3/7t+2pvZjIt5WgdrpT2yJa7lbczjLdKF9R3Kn1HuPm4tPGL63yaHJyEu+//z5ee+01k0f/4B/8Azz88MPI5XJNXzFuF3xbqZ1k1lWk8eHkyZPYu3evtV1fXx/+yT/5J+ju7p5WTn0YkZTWaLvHiPFhIb4RP+khnHjK2wmyLxaL+M3f/E309PTgl3/5l/G5z30O+Xw+5rt5BN920faTndpHdt/97nfxx3/8xygUCvid3/kd/MIv/ILJGN920bAxYsT4dEL93ctt4W//9m/x8ssvmy749a9/HU888QTS6fT0/DSWC58NiCfUzn488Prn//gf/wMLFizAk08+iQceeAALFy6c1j+jY8dsSDXtb/qiVzThaIbF1P/7f/9vG+yWLl1qiy5tbW3XDI6CzApzvczHuBZeoRB8vftrNpu1yeX/+l//C/39/fjyl7+MX//1X7dFL6G1nr2AudPgy+sR88/10VpX10NchzE+KcRr4iNPWvQ6evSoLaBIHn3rW9+yAUxySnJM8JPeGHMLtZXqXu0ks9rAK52nTp3CG2+8YW2nMVwT1d7eXvPv4ccOPUyJ2y/Gx4Xv/+JDwfOleFHyQw9NOzs78fM///N48MEHbdHL85786DWZDzvGxbi5UJtF5bi/V3tIR5Wc/8EPfoC/+qu/sgVM6aI/93M/Z37UhgrjZU+MGDHufHj57WWyZEJULvjNF9///vexc+dOkxFf/epX8eijj9qOcskFPxZ8GLng/ca4M+F1TrW1f1CiRa8/+qM/wqpVq2wNY14uegmeQXX/Z3/2Z/jzP/9zK4ye0HlFRW7ev8LLrHDeLsYHwysLgq83zzRdXV24fPkyvve972FgYMCYRbu95F4qlYypogtmd3K9e/4TYv65PqL1dCPEdRjjk8LLFMknXfV0/+zZs7ZjSHLpi1/8IjZs2HDNQknMe3OPVvnplQ5d1VZHjhzB+fPnbafXI488YkqHoAco8qM21tUrsTFifFiIX7ysEM9JP/H2ghRh7QAYHx/Hf//v/90emj722GPYtGnTtOxQGE2YYtlx+6C6j7al4M2awKqtNLF98cUXUS6XbQKjMUBmr8fKb9yGMWJ8OuD7v7/6vu3lhJffu3btwsGDB01O3H///bjrrrtMnnvIr/x9EGLZcWdD7afxQO3tx4xz587hJz/5ia1f/MzP/Azuu+8+2+2t8UIkvz7sbLhli15ReAb1Cyp/+qd/ait1Wnh5/PHHTYHxDBztBILsVZAYHw2qP1+XUiBEmqAMDQ1hz549GBsbw+bNm+3pqNz01NQvenn/vr0+Lj6I+W4lfNoetyMPdwpa66oVcd3F+DiI8o14zPOZn8xoMLty5Yrt8pJc2rFjB5YvX25yR34l+yWHYv67PfBtoPbyY4HaY3R0FJcuXbI2kyKqYwq01Vz+tbNG7SXlRAtgcdvF+DjwskJ853VDb6dFLz0oFa/p4amOx9i+fbvJDs9vCiMeFL/6cDHmDqpzr7fL7NvA20tuiA4cOIC33nrLxgLJf9HU1NRVbRY1e8RyJUaMOw/qy77verNI8lr3ktmS74cPH7a3kiT/161bh2XLlpmb/Hp5EMuAOxuzyfVWqP39HEDjhcYOrRvt37/fXm3Uq69a/Fq0aJG5iT6IP+Zk0UsM7ZUQZehP/uRPbOFLA903v/lNU2Dkrkx6phZ58/UyH+Na+LryDS94geJ3ev34xz+2yea9995rT9YUJrrTy7fXJ613n4fb0X7R8nvEfDQ7ZqurKOJ6i/FxEOUb8VhUHmhw0istFy5cwLFjx2wg024NKTgaJ7wMUhj5jTG38MqDHwdEutdCw+DgIM6cOWNjSUdHh53Dptcb5UcKinAzx5EYny14XhOJj3QVvJ3kg576anFE55Pq9UbtNvSyw4eP5cbtg69/33aCbz+1j9pP7pq86ExHjQWaxHz+85+ffgDrw7bKj1iexIhxZ8L3/2jfFnldT/JbkFzQbnLd33333di4caMthvnwMT478G2uMUHQA1ed96YNO1/72tdsJ6A29Gg8iY451+OTOXm90Su/YmDZ60wvHVSnjOpML3/4qPz6jEaV5etlPsa18PXor95O9amVUu2q0Oulmmxql93f//t/35jJP5X/pHWttGbDXLbh9fLwcXAz8/1h8jWX9SR82Lqa63zFmL98/GHg8x5NVzJI0MAke73eePz4cTsfSluWv/GNb9iODSk3Ub8xbh/UTmpLtYfaQotaGkPeffddO1tBi11qN43lfqFL/hVO/jWueGUlRoyPAvGS+MiT50OZJSMmJibwu7/7u7bwKuVXssPrkoIPF2Pu4WVAq9nLB80FJB+ee+45fOc737GxQEed/OzP/qyZtSjm27EVcZvGiHFnQn1a/V5yQIjKCNn5NYJnn30W+/btMzmvQ+x1ppfc9NBN4aNxtCKWD58etI4ButeRKFrDWLt2Lb7yla/YTi+9aeD5woe5Hh/c8kUvDynLnqH1tRYdYLl+/Xr863/9r01pkb0yKZLZ3wtzz8TKu8+/T9tdZ6uduc7djSBBoIaPQnXpBYomKv/z//cH6Cfj/PRP/Qz+H7/xm27RC2VXjpBtADIOb2oJtgHNKZMtM6V0bs6cVo3wv857qqNIMK1UgwHUhsaAik9/sqKPoEJTAmGDSo21q2pUuwNCBM3abUCfwFdculHiNCSdG1nWbpUHb8NUeCNiuc2SilWiuWiqewlI/YXaJplkOnqaIAfzzLwoH0zPwig98mDoekSC6TYkXBlXwuJR7O7g/yT9cPpuNqwR818PWC5zVb4UkyO1QU3x8y9gZSVYZCtDmvEzvH4d5EO1zl+2hVBN1swuaASsE9r5SC1U8yMEIctE/6qCWlLxhaxFF1658/HShzLDe9/j+cOKVs5YO0gq+lDtTmowbtWHpANb2kNZUAoK61JQPnTvntJwqmuxybVmJUkpNdeegl1Zi1Yu2tPVShxp1JDlqDPpZLJoYVlRJMbvEjSoeuQ9qfySVOGOBTiwyqPFZRZW5AojUnDauKv4seF2pljBp+tEZmdUuCTz6SzkzpphnYRsQKWTYC3LX8AfXz5djLVJrm3Vt+RXbSRlnm5WqJkwzuBulHsH5c1iY5gAdQYUPwoB86H60t20L6YnSqLCEOJHJhJmFRx14wkH4wOGpZULGFTN3rWzT/uTQfwuRGV3VK6LNLnRNnY9tdFW9n/4D/+h7djQ4rxXaCSbfFzzC615cuWcLaczNRBB1OOsHm4vou0nc3T89l9vPHTokJ3l9Y/+0T/C4sWLp9vKh/WKaet4dGfhgxuqtc3nYXPekRDveP7zPORfdRCvaUfQv/gX/8J2eunLr/p6o1519PwnyG+MuYfawLed4NtBberbU6TzZfUQXLv29ABc7ag3QDTZ9Yjb89ZipnadFheFq+3o70dDa3wfhA+Txux5nEHUfcbtRjm5OobZw8e4WYjKBQ/de7kgaCH8pZdeMjmghXCd92fz1MjmjNY4PO5sGfHh+fSzAs8bgsaPEydO2Fme0j2/9KUvzZ9FLw9lQIlLWRHTCvp6oBa9dPDov/23/9Y+d+4L5jMqs+8Acw83GReYI/6KbGmlyZLe1cHfsRuah5mwxNVebzmidRiFr3/3uc//ijNnTuPrX/sG/tlv/nMk2SyV5ASCBJkmDJAIk7aoVeIEO5lIIV9WMdgWipZUCzhhbTZNZ93VVYltVWG6AZmynXYqfSOlHRvNxQybw1aRzIzJgHJ9gS2KJRI1+tRCWAVZheFfGPbwPmlxJZhv0A8ytLdFijY0GKctsikPiQZSnPYn6/KbYrJ0kP+AxPLYPctdZ9qVsIoAaWSQcwtZjaotZNUanMwp78kay6vFggTCmjs0MaHFAisP42F5LLfJKeYuiVQ1i1RDC1/Mf6NIlwSK2U5bQNIiiLKXVHuYC8vcXDzJllIIqrSlp3pbaHnTr8quBSCLm4UL6sp/AxOZMm0SyNVzrBNOLBlZQ4sfWnhJlCzOZCnHYqdQS4Uo5KqMqY5u5YDhKwzQ0GIfy2j5qZMazUMhtfpGb3W6lZUmzclaiFSSk4uwSA/Mc5IKaKKDPMTwipLpV7Xwo3q3hTwt7TAetQ0d0yiwTUqMM4liQulkkW0wbtWJ+IB1H7LOipkiw2opKM/ypujGyLVwRy8VJlljlKngMoUU+bDaQbcOty7TRIkRKi+paoi0PNOtnpEMqyPN9PSHuiw5+aa/MWWF5dfSXIqJpNn+qYbajvlP0R/5wPLANhU/KExIt3RQoB0DaQGJ7vUkeSlVZhm0UNvJ4ElkWE1aiFJ+tP4m1mPRGEeFdqPG58mwjdXdY+u4YVOn11qXvKod5Ed5qSW06KvgFbqR/9gHa40MalrcC9xiUJptocVT1X5Va2mKhxGp9gKMk0qujWvqS2BdVxQTTerJ5C/WS7qiDNIqM87Ayjv9J2YmGzcbkk1RaNFLCyc6yFiLXnrSr4lr626N+QnXDh7Ww/nfzLX9Gmihu2kbMoiZp6uCPGwMMD+hdpCiIZICqnFESofOhVTbaYfXr/3ar9lXHP2ilzB/260Jy+YseZxehdZ1upGauKolCWe2fuWtI0Yhar4KLf4ES+26AT5b8HwkHdAvdImiiyZa9Pqt3/ot0x9/5Vd+xV6N06H23l1+fbi5g8v3DG6Udotba9DZmOQOgOpfJHmgNhB8G3g3r9s//fTT9hBci16/8zu/Y4tefjeHDzO37fcpR4SljN14I/klvYW/Zt8KjVj2kMzfz+LNxxWF7GazvyEYwFTb5q2Hj8fijDo2/SpPuspdKpzBu7lQZp6GrJogNzqP0z49zCXGTYb6v+Bls5cJUTz11FOmF+oBqL7oqlef9dBN8DLFy5A7Diyq+tTVaPY+bTIwXF0fjns9XY1rbeY/Wtv7w0K6gN4O+S//5b+Y7qlFL50DqTcOPH9ExxdB99ExxC963TbuUYa8ItNKsr8d1OAM0pmZjxY32c1G3p92M3m/14adG/J1JwZpdRPVanVbMa+Zu9qAgkT5to7nmNE6JZlDE2RNrWE7YugmTuEII7ZR92xUNVFvMhAjq9er5EwtlFCYsV4S9Ks0tGvH7BjS1YvqzKWt8BpUEw23k0n+HXlHpaXdBqpT2kTcrUyyULzyK7Myl3ArviFzZn5pDpKBLfyE9QqqpTKKxSoVrAZqoZaySPLPKORXcWtXjWy1+WkAALgeSURBVPpHMkghESg+1V2IakOLSs5NUHnk1qCfOv8srHzwWqnWUam4w51Vl7VQB+syQ1pM0yqQJagaVhmUddYk60D1wn8rn5JRSZSm7OTGaCwd8yM7xVPjPfMnG+2tMn8k8YFI5VP8Vq9qEFUMI7e4lS+amV3yRc3FyXJbScgvSqfOcDWlwXiML1jHVlfkDfELWcqa3vJQV+KKXmUjv/He/ylTVpeqrWaeXEYsFbdbi8Y0ZZjSUf1WGafq3mIgT9Vlx8TqTFv5bmjCrZUmhrP2EDGShvIhopNEYoXlrlp9uPa2VbSkXBJsqyrCGvnXwrs8aBHQGlp15irT1RVL5fqMm1i5Mik+/pNvqqynSkW1qNK5etQDBUZti8xJ+pF/tQWjtHw2FLcWbxmNep3qz9Uvr/xJMS9SCJV+nf2ubu0ivmZd0UFZrYrfWAalpfpQXYWKm+HcT7MO7c+yNw2XH5boFlFr/DUyjCY4njyfRv3f6jx9fLo6X06mXWtvPBJxm+FNNa41cMR9/tFsbeDbKUpRe+9v/rYdyfLWbAIj3re01dVt2Xo/Q2rL6fuIeYYnrqXZ3G7k/7NEs/Fc9N67R/kvyndRao1nfpLnrRa6ih/vHFKd+/HEX71Z8Pfef7QNvX3rNaabQ6an6qr7Jn9Ze5hdk+ciJDujpl/z3yR/7+2i995uNvsbkaXTTMuHN4rYXeXfk+XVCfNWt6j/a8mVfeZ+ZkxglBH7mOaCxIvSBSuVyjTNph/eyXLB8VWUmmUxHvflipav2S+n72fog/l7fpLa78Mg2s4mp5r3rfYfB5ov3RbYYkDzqY4333biRNgR88UJcdJIu2C8H+VzNlLYVj/+fm7I12OUrgWZx0153SRdhAyZIEOzVhpoobh47zxM8jrKCf8kaqUiSkUKI03UGUUiyNE+ZTttOlFFV4r+tWuGwmrgzACGr0xgqFHDIL0NBQlUaymGZTqpGhDUkaoEyE21IVvsRljoQqXUa3UY2FoE2ZLmKgXDMPNRTLVBG48CCoEsE8/b1b1CN1GvoZgeRD03yLyOI5wqoThaxeVLRQyMVDFSBP1UUC6eQXJwN2rn9+Llt1PYeziDk1cO4XLpXVycGsK5oRxGSlmESZZV5a00mKckKrUC6sF5ZDKD6K31or3azvsApUwDU7kkJrNZVFNZdFZT6KprV1YRuWQB+WwNqUwShXKFeU8hW88jmR5DvXEa1dFTqJwfQeMiBV+1C/VaJ1KNHKslhXI9iWG2xVg6i45GFR21MuqJEBOskgm2XTkZosx6qVXzSNXbkcyzQbomkc4X0VUL0d4IMFZIoML4skE72pJMt5FBMUyhmmZj5CZYt1fYTiMoX7qAsbP9mFKbsvkbuQwKAcuUzGEy3YupdAcq5XFkkkWkgxLzV0TI+q7ZLqosctUMsmEOHbztSAPpTDvj0cHWnWhDmnxB3mQrVVT/jQJq6SKCbArdWIh0pZN1y7Zle1a18Ai9midi1GzrFNsiVe9GhnkK2hme6Y8kyqz3JMuYZL2wj9F3gf11gnWfmCI/oR0h819MllFOVVBnnrQwpo1e3akGelJFdKSmmDMmoC1lZe1wyqORbEclk0Ulm7QNYhqctBFOi0safO1V0kCLT2m01drRrt11dBcm0zWMZaqYYnpKM8ip3cuMo4pGrRuJ6jKkQvE2Y9EAXhlivkfJ42Uk0lT22W/qyQwpi0Cdi32sUWP/C9uZBstYm0CSbdUYu4DKwBlMkR8mWYfFtBZWK0iS37WJsqNEWYU+1kcfxljoqfQIavlxtFXTaK+wDlkw9f06+14lT+WijX056EKNbQWmP5tMuRXk5VLrgNUqu2YLOz+I48P02CCaGTNaqXXcSDSJjkbXxn376XptIEQVDo+o/1aKhp8/pHzZMNck1zZXu98g79dpa6PZ/Mf0oemDeMbz1WyI8px2GrWGnV/U5DHl1/LcSrOFuTMo2kbe7O+jkCxpHQN8HPO//e480psN9pSMNG1PmRVQnolS1DmjJLtWuXZN+BuQxr4Uw4r0Jsn1aDoNEcPoIbPyGiWz1zXi14+tV/mzPEd5R+ZIOUTTbgwzXZYE8+KKx1u7j/qL6eZTVDZ4ms2fZIF28oi041zX2fzdCeT0P8rFaeL9Vf3J826Tb2m2fqJrC82EufNotrafjWbzL/jrxwWrfu7hC+Svolb720GUil7q8d7lx5M5tVDUj7NkIZqO0bBzQRIO3hytQ1+/3mwKhQ0sqnBmlXY3BCc4hckJnOs/h6NHj+PypStWxIaOA6LOoifn2rlRK5cRTk1hZGAA33n6u/j2t7+NN97dj4HCMAoombDKpDmZ1+S/zsm/bQ/ScjfzoAUTkiZT5UoZtYp79SzBMCwFqvxrcIJvqxFSlLQqUirbU4BcOod0Im27lKqMd3h4GK++/DL+y3/5v+3ciIHBQXotY+DkSbz69NP4H//X/4U/+IM/wFNPfQ/P/OjH+N53v4e//Itv43t/9yJOnBhh/aRsFZ0yh3WmnUV1VMMK6jrnSlkoKfkG7WpucYSNXqiWaK/y8J9lUhhBdauDWUOz42SxWMSl/n7s2r0b3/nud/DDHz6DU6dGLYzKovIHrFyt+VUqLGdRiWk3lV61A7LpBK9UJFgvUhirtTrCChvC6pJp0i7ktb2NaYbMu3ZnqYrrDZRKdUxNuZ1qeoJ39sgRPPfDH7COvo9Dh45jfKrBchTtFUEGYXmZX8an/LNSbIeRFm0UodY2aeV4XenqwjJrZ5u+BqovMhULWiCTXypQpHQqbbynJxdl+tM5a6qfFEn8KPVXfCR21E4vVr4rF9PUeXGmnLFRjBfKrJdCwdyUj1yOWZGB9+Ua3RiZ/CoKPQm0svBP/BGy3Zoe0EgnFcT6gurFnqqo9Awnu4B5TufzHJiYIfp3IxU5ksyq/hRaGKe8q84EpmbpunLTQD/aKafyBSyYG7SdIqZw9pSbf6obdYIk3cNQX1UFyLaWTsA22LN7j23t/ZM/+Uu89dZhTExUWE9MI6OVPUbOtlY7s2cjnVQFMnxo7ye7PCtTduOgfqW6lrXMcr+VpLaelj9Ns7/3dt6frpbHSPj5Tpq83uiePzN0m8aID0PRthGpbWZza23HKHm/Pty8IuP1ZlNMd+mIOy0cRe0ifnyYZrjphQvv/gHk2543V9Fsfj+rJN4RorznSfC8Jejq+c7b++u8pygvRWk2v3cQCdE2EqJtFJX3gg/n7WKaWzLZ1frn7Wch/lxFs/n5sDSb7OTPNXG3+pt245/MohnRGnFXhyJfTTtGyMdlZP3OOel6lVtMN4V8/2+9j9pH3YXowrjMIu9+55HnLdKssr71XvTZlIlRnhAJs/HJxwGrfe5hk0RO8L05itb7OYW9X6WKFH1w1cxe5cr/3JfhevUme08eWkSxQ5ZYgIYOGdJh4Qb58a/VkYIx+hnB2PhFHD9xBG+//R5Onz4vj2hkJ4AMifEkkllO1tNIpMpINibx/v5zOHVgBJcHgZFqDkWmkSjTX6nOIA3kKwFq6QAj7QmMZ/UK3BQHmyrKnPcX0wlUNfKwLXTOUr5eQ1CroJpPoaydOOkpIDXIZhpAdeACLp06g7MDAcaqC1BLdqFui1BlDE8UMD5WRLZSQxfNFea7/93D6D9+Aqe7JzG5Povl2UVYOJZHdaiCgakpjNfrqCSYXkZlGkciGEKa5cs0lrLEizCRAwp5LcoMoz0xiDZMMn8BOhJ5lPLa/cVsp/PMQQYJ5jmojiNVH2U9FhGktS9tCBg9ivGj+3Dsjd04eOQQ3qNQO01Wq6YmqAxepp8RO3eqTfWQXYBiKocE6zRbH0S6OopERedRNZCynUJltxjD9HT+U50BE9pFRx7O1nWennZ8sQmDBjpzrIe8di2xDGEVk+MjOHfsMN595x0cGSjgSkj/CpuoI9+ooq1eRboWohRmUU2kUc+kEOZSTC6BTJ1NUCMX6eyxpF7h00JZgXmfRIZlzabZCsx3uZZC1V7hVB7ZuDLXmO9UCemszlFzO6LqzG89lWU+EwjGz6B+/j30D1dxsZTDaEO1nCYPNZCtNdDBa5Ltw0yyTpkPxlxLNnCZ8Y0yjxm0s+xtrDPySqrKZJlWqPorsDxMu1FHcaqEC/2DeP/IOQxNMvdi+ETIOqwxi6GOArOz7Wp12SUZf4AySa9lQmdmBTWkGwGCSoKpVdGRLCEXMu4a3WuMim3RkHhjekFYQpisYSKVwBTLV290kLJao2JaWiBTe9WYfNnKUWWZgjTjS0+QzwpopPTKaQOTZ0fw3guH8PbBfvRPVmxHXiVRQJn9odw5TBpinVeQJj+ma1m2USerqMcVhPWeZlXkyAy6spYZo07Eq9C5bPm41ZhNDnlE7W7kb77D2KhJ12BWyzsHXsG4UbtE223ett8NG0nw+Y56nN1zqw9PHwofK9BnAx/EQ9dTdm8vz8UNKrS2zQdNTNRmUYpx66DajZIQ5dgoSWPz5tZwPuw0ZvMgaiIa741oGrNaXm097XSNxTW3RNRT1DWSyRi3Db7vS1ZEZYEnrRXoesejlf2uQtQxSoK/frbQ2uZRXvgkPCHZdlugDPtMf9zM3xqQwWzhK4IPlT15IjUv8xGWLctiM5Mqphb6pjvYTMZDGRNVtk0JExMjOHPmlH1x7dy5C2Q4ze1LqDaKKJWLmJwokCZRL00irJcxNV5BWNH7cllOrHUQdxIJveZXLKIxUUR1ZBzjxXGMoohiwAm/zjkKa5yAh6jSrN0zOmSqUSyjzHir5RKmGLyshZyQE/XyCIYHzmL/3p340Q9+iNf2vI0zF6cwWWKWk0n7otgDDzyEzZu3oKezE42pIq70n8fl/nPIBAG2Pf4ANj96N7Zt3Ip71pK23INN/3/2/gPMkuQ6DwX/e29eb8rbrvbeu3EYBwzhQSPKEAIBiZREkVqB4tOupLfLt/t9+ki+3e9RhCQKoJVEgF7EAASGMIMBMN702Pa+u7rLe19163q3/x95s+p2TfVMDzAz3TOd/61TmRkZGfbEiXMiIyN2bkNdU8Ss26V1lzStK5edY76SSC9WmHQ/FotAlsVULi2iUphHnnlIzy8iNZ/HbLqAnHja42O+PWZ2kgY0POUCMrkU5pPTKC5MwZuZhVVIwVvSAuNAOhjAAoV9yZuH15NGqZhDJl1CKqkwmX95YjgaFPTyqOmurBSmM4ssw0lrVhXLKatv4Ita60qzozSgxOfotcSsqDx9dM+m5jAzO0O/ORQLWt8sY8+s8/pRoP+SBn2Y/1KBdZROIbOYwtwC6zjvQZkBisQi2jXRCA6WtRawLytOj9wYr2aLpZNYSKawwErL5jTTiZ2Z8qFnfeQFb5lpX8T8/AySCwvIZAtMshYuZjCpGZw48gwee+JpvHjsLPpGp1j3mg2lFbK88JGPPJopmGe+yRupxTRyRQ25lZBhorQ8vjZlUB1oMKeogZ1cGj6Wt+aTpRbmceHsWXzv0e/jm9/8Ni529zCdZYahvNuzrkpMq8qNFWhkkwbFcixTlXGZcfMuvJIRJtt8Lp9mWaZIrBMzw03rehXIH2nkUwtYXFzAtAZVtQ6eBsTMoJPCVxGSV3Ql/mf8SoFHg2XFNMqs3ySfn0tqsJN+cl5oYl+GCSowfg02aqAujXnM5iZY5lmw6FlvXqZF5aBR2Gq5k7QWvmFtO0aShtOqFfMOolbOvxG9H/Bez8XKulhZL7VG7JsZtO89KK+1tEr+am+7eNdQy5fX47uVvOvi3cf1yt+pm9Xuu3X2zkMlXEtCbSvSeS2txMpnbxaul743hXislm56TlxcTx448l1HhxxcT/a/Z+Cw3nVZcKWH93h+f0zU8sjK448KzRP5DZ38x98wh7cVYlAlUFPRhJMnT6K7u9usvn/fffchpO+SCIeRVx5vGlaLfhW3N0zlTcjDauXmlP/c3BxeefVlzM/PYcvWLTh86JAxuMsaoOFjHhrQvKIRrX3jbKPc7xmjLZ7G6Mg0zpzrQ8/ABOpa2nHw4B4EKinkFpMYGZzC1cuDGOi9ioWpXswvzOL7x3sR6WxBx45OdHQm0Gx5UbeYwfjAEM5dvIgzly6gb2wU6WwewUAQMX2O5ykhXclgYWEa6alFpCbTmB4bx9Xu4+jrvoyUrwOecBh+/zzSC724ePYUfvDt7+O1F8+if96HbCmMwtwkFkcvY4F5LYfXoGvtRtQlFjExdAHHn38J545dQcFKIHLvfWiI+hBbGEUxn4In0obGlq3obAkhHpqGv1LEzMQ4rly8ijOXh3F+ZB6js2kWkoW6MHl2oR/zEwPovdqPc+d60X11AKMTi0xbyHwS57FUpizLYg7J2VmcOnsG3czz7OAgxhnW0FQFE7korKYOrDuwG20JoLkwA8/cBMtoHBfODuPihW6MTIzAEwjDF4igYmkHwSKsxWmUUtMYn5vBAOult3+BxxRmUhmU/CWEIlFokfiKpVlEWXiRRTG3iMmxIZw+fgrdFwawMM3rwREMDw4h5Q2h7Y4H0bGmEa2WRkySmBocQ/e5bpw/zXrqG0Q2W0Q5oiluflj6zJAMo10k9fmnBk1KnrzJb3Ehiem+AT57AWcvXET/8CCSRdYZn7UsPUeuYh4WZ0Zw9vRxnD7Zj/7BSTMrL1su8dYCSkNH8dh3voZHTyxgaJJpL3nhDwQQsjRDcBZTI33Ip9MYIi+dudqHK5NTZrCxlMwgM5uCFr0v+xiXZsKVZ5BJzWGc4aSzBTaGEkb6B3Hk6Rfww+/9EGfPnUE60YFo4xr4i5Pw5BeZfc0QTCNfLMIfCzN3bBm5LGbGx9h2kgw7BC/r2UIGszMTmJ2eIK/MYnBwBlf7JzHLZwPhDGamxjB0+RJ6LlzCxau9uDoxhWLZg0S80WxkYNa6UNtjkWhAkGcoecmLbAPpuQWMDo3hck83LvVewtT0JCYuTDKOKQQ3bcKanduxrq0RLZpBWMxjZEBlfhlXLo+yPCcwOTuPXMmHaDxqD35q4wQv+ZF1VvGp7ryMjU6wd4lkSnjtk7h4V6Ct6ScmJszOjZJLe/bsQVdXF9nLmXFqy7Kb3g/8CKhN8etSv9LhFs6eU/ZO/6E3a7OUZYOUYVNTU4hGo9i7dy/i8fhSXTnPrDy+N6G0v0n638vZu8WxkoccRVfXWgpAW9trhy/x4Lp168xn+A6vvrf57r2PleVfW4c6F+kF6okTJ8yamXfddRd27969VH8O3Hp856CSvaZ07eZ1La5T/KqWG6qZG/L09kM61epxy7FKS7y17PH1Li7eLaitS8fQztC9vb1mGZCtW7diw4YN5tyRBe87mfC67MhhJd1+cPp7B7rW0kWvvPKK2alZfNHR0WF2fH+jPqP2+rd+8zfN8aYNet1///0mwSuZeWWi31Uo6tWip5tzq5ZeD7ou3VzdxzuJ65Wdyl/G5atkGA16bd26GYcOHzQGcVk7J9KPmZWkgRqel/TRGE/83n6Ui4sYH1vAZRrUIxNJtHZt5LN7ESkuYJzC6firF/DaS2dw6fxZTEyex9j4MH4wNovQuhas39KIzS1RtNKgzg7P4NUjr+DxYy/h1bPH0d8zgsx03l4cvDUCb6iCdHYSVy+cwqUz/ei7PI3hq324fPQHeO2ppzAZ2w5/UwNC8Tkkk+dx+ujLeOE7P8Do5QUMFtsxm7KQGr2Ame7naPxfxuXJKNo71iMYuoje7ldx9PkLuHgqiWQhhPmGApJjgxjtOY2e4auYm/cjbq3HmqYI6hNDWJwdx+ljJ/DKC8fx7MleHOmbQv/EJOLBCDY1NKIwfg7950/i2NGTeOnYKZy+eAVDvXMsMj/zEYI/GmbZlZCdGmOcp/D4E4/h7Ilj6OtfYHwVXJ30YiQXQrC5BXfsXoOOBEt89DKmzp/C2VeO48XnXsPJU+fRPTiMdCWCnDeBcrAOgcIiQqNHMT/IMr84iKNnh3D8/CK6h/KYzxcRavCgubUFeV8JZW+aZbsAT3EaU2P9OPbqa3jye8/i0qlRTA0vYJjG69jkBIqROjQduBsdXU1YUxrHdN8VnH/tLF59/hiOvnQcfVd7MDOXxGK8Cb5oHNFgAEHTnJ2pWyUUkEU2l8Zkdy8uvHiU9fwizpw9hnN9ZzCabUCwvh7hUNgMreSSU+g79wKefOzbePmVCVzpn8RUahEFf5FlNgdPzxN4/slv4YnedozOWygiiFA4hHi4jEjyIl59+WlMjM/g+KmLeI48d2F2gszLTpF1NHSxF9NKUjyGWDgNX67XDPYdvUAeGZtBzO/DSO8g8/YCTrz8AmZnptEb3oy6zo1oyvcDi+MYGx5jPY0gmcsi1rmGgVkoTY/j8smjuDowjlywBTHmJ1oZxblTzOdRdtIXx3DuwijrYgjpdAl1LTPou3IOZ194GWdePYlTFy7h3KjuVRBr7IInFEDM50OwzI6+xJLkUYOlXs8gculJdF8ewZGXT+KFl4/g3KWTbLvTGDo9h7nZAsJbN6Jj5xZsaI6hOTvFJE/gJOvq2AsnceL0CZy5cpY8NobFgg+J5mbEYkE25LL57NWe6qXWbq+V50eKdaLBbg022euAvROQXKqV7zJ0Jicn0d/fT3k0bwzXtWvX2uvHVVHbkd3qMPJzFVoV5iaZ1Hi4rq+bhtq6cqC6kEI6PU0+HBoydbdy0MtBbT3fulAvdz0o3Q6tgje57eLHxxvxkNyKxSIeeeQRIy/cQa9bDyp/1YVI5059SIY45ysHvfTiw/HvoPbcxY8PR+qpVK/pXXVjpUh0ip5HndZ60bWpmlpawsqAhKqHa/xVUeu9en8VJxvXuXFNupyTlVCCa2nZ9zV4vYuLdwor23rtoJfW/du2bdvSoFct3qtywfBple2WWPAaOI61dHvCqWMdHd7QS9e3Y9DrHbEs1Hm9GZxO0cGNPOPi+rheWTrlfI1b7X/HWUdd6I9Ua3NqtwjLb8Ef8POoRbyB3Ow0zhw/ildffQ39wyPQAtyhgIWr3ZcxOmrPioEW8KZVPzY2gldfegnHT51EXWMD9h08gK41azA+OoJnn34K585dRJaKbGphAcdeeRnf+fZ38MQzz2BwZNSeIcS0vPDCczj62mUMjy7oqzLEEnE0NTSgqbEe9Q11qCM1NTexQYQxPDyE5555GkMDA2bmj49pjkSiiNFQkxwJsKEEQmFYXo+Z0XWJCtj5i1cxPVdGZnERR9mwnn/+RfQPjSIYCqGZcZRLeYzQ4JuemmHjW8D0zJxpUBs3bsC2rVuQSaUY5zN45dVXMDw+jIX5OfRevITvPfZ9TM7Mwx+OIhTyIzk/jZ6r3ejt60GhmEcoGEIyncKpV4/hmcefxvGTp5EtFLBpy2Z4KyU8++TjVPB/iKPH+rCwCJZTjh3DGXz7u4/hpZdfNaPf8VgUbW0tSMRjLJuCEZWqzhLDn5oYw9nTp+j3qElzY0sjwpEgy2gY/X39SKXSFChFljMwPjKIZ558AidOnoIvEMShOw5h375dZjbTCy8cwemzVzE1swAtyq9ZgoIETj6fQU9vN15+9VWcvXgZXj57+PABbN60AWMjI3jlxTO40j2CyYlpXL58mcruSRPvxs2bsX3XTqxZ04ko6y3Ieqqva6RBHWddRVCnOm5iHTcrzWHMTk3j6Sefwte+8Xc4fe4CPF4f2ttaEQkF0dtzBUfIIxcuXjSDdMViCblMGiPM57Fjx/EqyyrFOpKxXl9fj0RdAolEwvBFImHXTT6XwSB55tTps1TKL2NxMUUWLmMxuYAzp07hyJEXcflKD3IFoFjIkR9fNRsB/PCJp9DXP4gI01xPXvFbAczNahC0gnXr12Hb9q0mb6dPHsfzL7xAv9PIZorL7ZJFWWF55rOLGCRfPPvs83juhVcwNDKOeDxqePrS5UsYn5wwGwVohp0+m10YH8MLbD9PPvM8Utk8WlqaEWYbHOi7iueffQbPPfcKeStnPs0skZdsrlCc1dN3sWOtlT+C05k55w4cfyv9u7g5qK2PWpISIqp1e2/A5av3Omr5beXRxc1FrUyvlfFC7fVqdeji3cNSib8dRX+jYdygP3l7m4N0cQugts0LzrVDsiU02OWQrp2XGLV0W+OtNI73MBw+cY4OnOsfhxfe9kGv6yVS0LlDToKdawe157cKpNybXdZWpO3adNtEr8Q7Mpb4hqhlgOsxg9ZfYsk7VyQm1smCR99Ylcx6S3pcG+SZOV/6VI/ZKemzsVIZwaDf5DPb/S0MHvkjDBQziP/0L+Cn/vd/h1/5+E48tMlCZaEN+cUNiCfDqJ+Zx2RfL/708cfw7Oggtv38P8CDv/qv8fd/+iewpzKNM9/6Or5/ehZXU+3YONWP+jPPoK9nHMd8O+A5/En82uf/Pv7Zz9wJa2EUAxeP43LvNCb9G9F2x0P4+J47cce6Cvbc2YyPffpOfPoXP4a/9zP3467967AuWMTYwGnkop1IHPwI1uw7hI0dLdi1fTf2/IOfx0d/7d/jP/zEPfjlNQk0VRZxNDOLQV8B5dMn8dpf/xmevxJE6M5/hl/8v/0b/Ndf+TD+nz+9Fw9ubkRTvAKrdT+67vocPvFz/xq/9iu/iH//S/8QhxqbkDx2AkcvPI9T0924OD6Jo0fHcOSlSeTv/Nd46P/9Zfxv//LD+Ln9E2j3HcV0sh/51Cha/BFMnZ7Ht745ie8+6Ucq9iB+4n//P/Dzv/Fv8R8/uhH7xp/G09/4Br71+Fn0Ts6gZJ3FZPIFfO1pL7L+Q7j/kz+Fn/7ch/DQBzfhzvY42nMpFFhvRYRhXexGheU+8NQxvDi+Ges+9u/xz3/70/j4vziIDZvb4c/HUcp4UQwtmvWwfEx/98MP49KEF8GH/jE++r/9Iv7ZP9qCPZ5j+P4PL+H7Tw3gpf4JXCmmMEfeKZbz8BQyqB/tQea5x/HDVy7hSWxGw6c+g5/7N3fjl//V3YjOZXD8m0/g5A+ewmh3Nwau9uO7330FjQ3bcM8v/zN8+Nf+CT71cx/HJw7twuGOTjRt/CC2bP8Y7tq5Bg/duxEf/tgmHLy3if4LaJhMYeG1c3hifh1mD/4iPvpPfhX/j3/0UfzkugjC0ydRHnoOQ4sFDJUsLJQzKBfHkF0cQWaigumBNIqeOjRt3YnNhw5j4/YdaF3bhU988lP4iQc7sH9HCF3BUaTnZ3F2sgGDyWZkC1kEMI/GiWGELpzFXM8IrmbCGMwXWXYXMH7pUZy9XMRgcTfa7v4wPvFLn8CDn74DW8Jb8cCeB/Gpz/xj/IN/80/wK7/0j/Gr99yLpr4xfOv5Ezg9MIOFhbQZFC77WedsU/Msz9DkUcw+9RU8cTyHU56/hy0P/hv821/6R/hHn7gH4TURjJcmsFiYYrvMIDczhf6nj+DVhx/BD1MHsPOX/k/86r/9HH7jn+7Gv7jTh6bZ1/DcD/4cfzd6GefYyFNah61UNPO5NJ/KzzZcKtSjUmpge7ZnSbwbcOLRsfa89vjjdGjvJpRe9QvqHxw4fYUzIORA18tuytutn79arFYnzvV7oa6uheqglgSnTmxaWX9vBPlz6l1wzuUuctxr4dy73v2VkL/bBU5e3yzP4jvnLa/8Ojx6q5eV0leiLNbOwrwyR5ucFxPXlyPCW+HNmwWnPlbCqaOVJOgZh1y8zWCZlst6IarjMp+prKXX2xf2YXXIctBiD6of8mCVDByxKZij7Aryrln/VJ4cHl+u2+phCSYd4mue67+943b1aeNYfcA4iOxrhmiW83B64JW8U3tdK5Mdd6ct1R6d81p/Ln581Lb1WtS615a/c+64vxfr4ho+qqGV+XFkvQPnntyuuVdta7XPvh8hfqjNo87V1zvlpmNteb0VvPujM7cwnIKsJcEZcXYKu7YyHEFa25g1/f69CmWNWYLPLPHjM3lz8ueztHufhVSqgunpGTMa39raQmpAuD4Aa906HDh4EGs3bkJDQyOCgQAymTTGxseQ5lHlMjE+gYnJCQwND5tPmwLBAMbHx5HLshzZmsORCNZ0rcHu3duwbcc6IJEwn8N2tHcgn8thYWHBhKMF67WmRywWQyQaRTweQCgWgJ/niXjcxG3qjJ2lPn3Q2mF+MxstaGb7NHh9CCTqYGnWl9/PvPiRTpcxPTPD9I6bWUCbNrWjs7PexNHZ2Wm+MU/U1WH9+g3YxDzW8TyTWsTk0DCSyaSJJ8Dwc9kcZmfnkMqkUFdfh82btyAUsuCpT2Dt9u04eOAg3TabvIqfVA5aYF6zj7Zu24bWllZYPgvtGzZg3fr1iHi8KGWyyGezKPLo473tO3Zg187dWLeuDowCAW35KGVGdcRmTe41s8+mJyaRWkxhDdO/adMmRIJRnq+pflKw23yepLLSDKL5uQXWs9csDj88nMRwXxoLvb2mzMkZZlaZ6l11WfFU4Nf2iUwPH8bI0CDLL234ZGZm1szoGhkZMQvV67Oo+fkF8kLGfM6g6co9PT0YGZ1AKZtHwOc1bmZ0lXWhejV1G40hFokhaGlBdtsQVXvbsX0bdu7ainbyXsgfMuWuOlI+8/kc+ZXKmWaisf7VQZRYLrr2WT4zW1H+tU6Y+FnrChpWlz+GnWP6RMViobrGFPNJv4q7UNDaZRWmTQ8wqXTvZFnu3bMHu3ftQkdbO0KeEKKsvzXkkeaWFpNnrV2ltZCy5AtHNog3tdlBuVg2i9OrzbFhYWJsDHXky82bNpvPdsT7ba1t2LtvL7r0GQ/bS5Zh6nNllas2Wti4cSPa28jjITYX8qR4aDfrVvVlNi6QgcWy1ZbfpoFX5VqNyHJxg6hVQIxMrL6RdKBzueme01847qbOq4Ve24e4uPWwsq7eiASn3p1zkXPfcde5+KGWfxweEhz/DtXCSYuL9y6c+nfq3KlThw/U9zpw+Mnhw1qecNxcuLhhkF+ku5tT/qQXG36q5bsVLEUfS/JKzyx54EHs57Cgw9caTKtoAE1sKn2DeqqNqiwzz9gP6aDoK1J8mBbD/+Rrc08/XkuP01cFNt/zAQ188drouUtB2n4dOG3EQe09tadrBhAIEy/JaVM6OucOuXDxo6KWf2p5yuGxpfZVdXf4V+eC/Dn9gKD7Iue+i7eO5V7WxRLj1ZItXcVkYkC50Z/xvexffCpyrr1VJfaWhMmOcqCqZzqdzOhdiYediUefrvHSuGsGCKnsZ2dRocGeo68ccvk0klrYvWChoXkN6jva4YmwETeE0bpzI7bXJbCWz0fyYyhnLqJQGEYy1IK0VY+ZU6cxfuQILl/uxVigDi0792BjQwn13hFkPfXIBbsQaepC57pGtHUxfaESfNEKIg1aoJ3GezaHaNaHhlwCBW8DqR5WgAn2suO1SGEapkEPQgginvPCKhTNrJZcMIyRaALjQR/acxm0Iw1/sBG5UBsC9NCGPsQyV5HOB5EvR9BQ1476aBwefwj5UB1i+oyyhcnxzmKxZxzDr/bipWdP4G+efR7fP3saIzPdyGMBbbkKmmfyKMwsYoKdNta0YW1LFI1hD/wMJ9K8ARs3bsKh9XHUhxYwl+rGbKEXs756pBN7UGzZinxDjCH54Iv5sbY1gY5EBfH8KDCnz9vC7PsTsDa1wr9B60t50OjPIqGOPBcE8mHUlcL0H0ZwMYnK1CDrYAaBjnr42+sw6SmgEAqiva0TrfUNiBSzaEston52CmfSHgxFWpGqlDA70oMLzNfRbqbNG8DaDTF0dQXRqk/4KhGEK36ykc8sil4pp7GYmka+tIB0cQYDg4M483wal14pIuifw8ZtTE9nPTzNa7Fh7z341EfvglWZwyuP/BEe/+qf4sXnj+PyWBEzrEsES6yXEhZZl/mAVgGzEMyFkMhHUAxk4ItXmJYutHcmEIx4GGfFzEKMBkKsGwthf5Elp+8Pi1puDAFvEIFKE9PZBG0oWgiwnILkCx/bKusnZgV5JLNqTbFAHiG/RX5o4P0E23GW/F9E3h9A0utnuRfQUEmhgQpdHh1Mz3rEO1qxZkMb1rXUo9VTQayYwUxmEq+dO4knnjqBJ39wFkdfOYfBgbPIZPsRxhoESq3IWl4kA1lkvVl4WXdmNauMF+W5PCKJBBpVtx1xVMI+BCIBrFu7Di0NzYiGY2zCXkzlk7iIMSyutbCxcxfzEWI7IX+2+dHclUBXSzOasiw7lms8VUGAbRhsy0ZxrOTZvvMosdmIJBJc3BgcZaUqSI2blBAp0yXyXJlHR3GpVU7kYnR2upknq+4ubgZU9itpdcjwsmtPdSmSguqQ7ttKqEjKq/hAcHQBwVFsHX6ovec8uxy+SM+buz8iubi1YNfLyno1P/JXLWkHYYdfasnhmWV+ceHixkHOWSKzMgXljIH4yej+1AUcvjL3+VflOUPmWfJoiX1cWbtMG4vBkPoy40f20ZLtID7V4JQtP51wFIP6Qe2ObcwQ27OB+LpowlaaTAKWnjPezFHESHQkmCLzTKE6q0wxmPzwv6AwJZP1stFeloM6ZdXAUXbLSkwVamcVkrnhwsXbhCUelozXwLAGbcWfhv9s2b6sV4ovbf4Tb+pUV9IbzQCw8WLz/hvB7SOuD7V+F4SYRGzisIrDqLYyssxAYjcJRhk3S8pIlVGNt+pzty7shoXKUu9kw3SCdqeh5Ju8kDyaN+TROl4ayOM97QDHzqyYr6CQL8HSTJtQ2Aw6aZ0hfyRIw76CEMvHKqXpvMAWm0a67EMw1oiEz0KCITU2NmPL/sO4/yMfxX137kF9hGXqDaHki8Ef0uytIIIhhkkDXS+oPH69OaJgYMJ8RSBQ8rOjs5Av+Ri/Zu7wPv1ULOaASQ1YfgR5omETujJcC5lAEFmfBxo2CCDHQH2MMwyL/iNIwiosMEwPyQu/FSLxaT5X9gVQZhq83ixK+QWcOPIqvvPVb+GJHz6NvokJ5AMW4nUhaIPFKPvMYJYdd7aADDvfQsiPkJ+lyDL1eANMX9iM3IeQZdoydMsiW5xHzhNAKdiEcrgOBb8P+kgRzA//EPAUEShn4Tcde5B1EYYnwTKPBuinBJYEAqowlgcKXpaPZVOB/rOLKBXSqGigJx5kiiyWj2VmpJkBHpZFlHUVIy9P5cuYZzrCiRjq4swPy9IbjmLH/oP4yEcewH33H8Tm9V1IhKLwkX/MSz0K61wuQ8WiwHqqIBz1I5GoQ8TfgaCnBYcP7cLHPvEADt29Hx0butC1ZQMe+vADeOC+O+DJzODky0fw2Pd+iBdfO4+5rAZhS+S3MorkR2/Az3plPbKk/OSfEsshyPAD4QD5zuYHL5lD68kZ9mUn4eXzqk/7zQgLnWksF3if9Ux1DXkZFfyZWU/iUzOLS17F14XqoAX9k+ct5kez5krkE/GPdK1AOU++9lBp026WdeT3CIJMT5AV7C/mgXwGV3u78bd/901861s/wOVLQ7DI102N5OkI01UKMT0B1hh5Um2Gz2kAzlJyWf4l7ZTJtHnJN76Q6orP8KZmKZq3oko185lhXHPkn6QvT16PsO0pAN73sh58ZQRZtxE+HCqwfTC9XgWkNm/yaqus6kB1qaJzcWMQ2xj5qJ8RkjZML0AGMbKf7s6b9Fo/9lOSsC5uHtTuHei89tqGU29O3dl1rnOn5lSPzr3l540uUHPtwHGvpZVx2Fg9PW8OO21OqmrDvjZ8FzcbrHrCqZflurHdVfvLPLISbn26+LFAY1sv+q5hLZ6Tq8xR7rZRbd9y+E02EDs046wBM4c3xYlmp3DdNzy7/Iwdnv4Zr0tH3ZPO4VybGfnV8BSiebYKRzehqx68hmwbzLbNFI/XjLbpXAfGYew2E5Odjmo8KwfanPOleJfS4sLF2wyxYPVUPKqL5cEu8rt42jZGzPXrWNFc35j+6ITp4vWQpHCxBInX5Z+ubVTPJWxF+pE5HYErZpSyIj4WGb69paFqF1UbhjlU82iIMG76rCzAPAbYZ1hsoGqkZdD+RzgUZAge5BYWUJhbgC/LfKfKmJ5KYSw7h+lyCil/EMVQMyx/HepzOWwIhbFu40Zs2LED+w7sx71334V777kL+/dsQyysQQW9RcrSdNfPi6LewhS1q6QHViEFP431YiWIdCWBgj+GiDcJf3kGpbyFUsGiVx4rEfqPsNMrGCoELGQ1ClLMI5FZRLyQR84fQgZ+dpoZWJVFFDxFzPoDSIcjiFh+5toDX2YcpfQsMtkCFnI+TKZ8SKcXMTM1hZOnX8Yrrz2D8ckxtHVswJate83C/MGAH2l2vlmFEfKjzl8EFsaxsFhGmuVTylZQmEljfGwRl6Y9mCk1wBONwQqFEK1MIJq9DF+yD8XkPHzlIvIZL6b4bLISRyHcBm+oHiGWQZj58hbKzDs7+6KmbFvMgw/FAMvMyiPvyaDsSyEfDSPX2IpiMIzyzAQwO4lQJghPCkhNzyC7MKOhD8wFo8jGE2hjvTaWsmhIxNG6vgvrtq7H1l3bcdd99+Che+/GXXu3Y117PSJBme7Mm2GVAEpeC0E+HyNPtMaC2LJuDbbu24dNu/bg7nsewgP3fgj7dm9CR5sPdQlg7YY9uPeBT+IDd25HVwswNjyAM+eGMauvKKmclIMBRJmOYF7rchXNemMpulcKrJliCL5CDn7yhZcaTNnyoqR8e5gTP89Ti6y7DDxZPjdfxMzEIgbIn1kP61sDZEx3oJJFiPVuFZLkGeZELyQRRt5bx+hLiBYG4UkOoECeypVDmGblJekpwzbA0JGmb18lg2BJA4oaJBXf5VEqT7FMRzF64QquHr2EwbFJ+BrrsXYn87lxEyKJOnjyBVTy4nOmnXUm3tagpsX6hj+OSqwFnsIkSjPnkZ0bxmLWi8UceWUqg2Qyh0KuyDxUEGUjbPAG4V/MITN3hbyVQSVrIT1HnpkoYorHUjiGWEMUXpaPFsrXDDHFWWY+bBVWn1pW3zq5uEFI+tuy3y43W9HWLGANpOrnyFXn3OkXjIt9i/XvlvmtCMf4cY5OfdmQm002D7Cjpz950SCn4HyGYGYNVMMQHF3BPM3z2qOtoC77vR7ku/qk7VAD46L4auJ0UJsOFzcT19aDkRaqe/7ZVWTfd+pL92zeWOanWjcXLm4YhqdsebVE5DcjT8hOxmQRHxpXh669IhOS93i67LJEgnPUmR1u9fMtxiXedWY5SwoucbAcJDtNeuhqInAiqYaje7otOMaVcXbahP1Jogbm7Ef5VFmTEmzdRjO7dN9e3kHR2ekQ2G0blErSiJz2WHV04eLthtiLBzN+QP60+ZZ/4knDlDpWudPwon2qc+czZNuvw8Eu3irsUrzN4TCQLeskpCkwSbZQvZYMhxp/toA0j9r/zPM6deSyA4dJbw1GVeLV0CySZtbYrkq/DGCm0pzZZRGlcxSlov15oxbCLGnGUaCCpuZms8PeTM9V9L16CuOXJjHSP4/XXuvGxblBDFVmMRWKIpfYhLr6jdjnD2KtdsPzB1COxxGO0yDXDC1PGb5KCiFfhpGmkc7N0NDnkfZ4vlpcYtIg3VFIIVMMYx4dyEWb0RFfQKQ0hIGeGVztnsXoaBbprGYz1WExNYtcfhGLfi/mAjTys4uonxxBQ3Iec94wFj1x5jMFqziFhdIi+pi+hcYmtNc3YW1DC3zTFzB04SjOnO3G0YsTePHMHPr7BzE6PIKF1CDKvjnE6+NoaduCcLTVFF8hn8UkO8/FUAx1zQ3YUO9lOD04fW4El65OYPTCAMZPXUH35Skcm63DcGkDsuEIGts6sCE2gbrZp7Fw7nsYPHkSi0PjuHRqAFfHC8jGtsDXvhe+RDOCxUWEs/OoJHPw5yrwF0KosEw0U6wQ8SEbyaNgzaMcnEG+oxnl7fvhbe1E7up59L3wFCbPjWHk7DAuHzuBsasXkMlnMBBMYDJRj8NNUezwFc2AW0obGNQFEW2KwxuxECPvhwpaHj+LoDfNOstBq4dpgDHQ2IrmtRtRHwkimJ6DL5+Cp6EBwZZ2+KwWWOUE/BWN+g1hMTmEwaEMcqVG7Nlah/sP16OjtQHJTAwLaT8QYX7q4ogtTmK++xJ6r/bj6twiJsSQmQhSZINQPo0YedHHNGU8RWTIj8GGKGKt9UiODGHs/FkMnulG7+lBnD/Vj2PDY5gtWyhaAQT9ZSSsFOKlGZTnRnC1dwTjE2kszPuR969BLB5AS/4MkpeexpXLEzjfN4tXL/XgyvQMpsoezHj8SDG+QGkWocVRpDWgmSfPebTe1zBKyT5gZBbtzF+8vROBDZ1AUz1LzYsU21AgVzQDdiW2PbkVKWesUoZuOVQaNiCy4QCswgBmLzzCOvohTl8ew9lL47h4YQILC0UUMkWE2FF21tVhZ10r1vnjmOp7CkMXL2K4ew7d5+dx7MQUzl3JIdC5Hs3rmmBFLTPJSzPWyuSTsjdoziuegiHJPBdvjGUZzrIimZk/Znag+gmnr+BRwp/+1DfYb5/VKZhH5FwNi3VRMxPMIRfvFtS5LXV8q8IeXKhesH1okMtuJzq369weiFDd8q5mfjszMWvq09YR7E9sBJ0rBIPqPRlhdlgKX/dWJ0cHscOuJR3emJdWc3PxbmK5/FlDhi+Wrlj3MtAdHhCv6LwWtfXqnNeSCxdvBpvjqnJMcoQ8Z/iHLlo4viCZxivN3nI+dRSbmoEh3tdMMTKneUbSzAwpyQNJzxs+5KWZQS5eJhWrn0M6fGrH5jHjXEvrdUk2OvzOsNgajC/j07QTDZPpijAHymbqQMYPn5d/xa+vDUze1C/LVflRuk3ces4Oz0Sp/td2Mtdl6mY6mhnaSpwLF28BS/z9RiS+MudqG2wT4nuxWvWe3ZS0WLuuyZPiS0O8rnKrWobT1uz+QuEtk4s3hzvoVYVhIjJTsUjDUt9/m2PBLESdy+VshVZ+eCzS+F9SYsmc+UIJhYIUFxYoS1Rrcjt4zzGikusk2XQ4miRll4MWKheFwyF0bNyIhpYWXDx1Cn/1P/8SX/riX+DP/uwv8Jd/+deYHhzkQzSo2WKDgRDWrVuPHTt3oH+gHw8//DX8xZ//Bf7iL/4Sf/lXf4VvfOObOH36tCl7lVWK8aQWFxlnDj7NTvH6WA8q36KJWwuuq+lrYfimlmbkCnk89dRT+NrD38Pzzx3D+MSU8b8wP2cW0S/k80a45JmHxVQKqdQictkMvKoXVlae9ZxOZ5DRIuw+HxJr1+HOe+7B1Mw0vv71r+G//bffwxd/9w/xX77wn/G9x77PdHrQ1tFhPq3ruXoVTzPur3/963ju2ecwPjmJNNOvBdJbmluwprOD/FLEV/7kf+L3vvQw/upL/xOPffObOHv+PDLZNMunyHiz2LhhIw4dOsQwPczLk/jvf/xH+PM//VP8zn/5XVy6chVbtmzGoYPr0N5CwZZjXWRzyDGeIvNuDCXynKrKa34+WF4NR/lQ19iMzdu3Y+3atRgaHMCf/umf4Pd/7w9YT3+O7373UVy4dBGZXNbmZxbHho2b0M40D7P+vv+9J/H1hx/Ft771bXzlK3+Kv/3bI3jppWFMTGTNGlrify+VC01P9ze3YtP2HYjGojh/7iwe/urD+OrDD+Ob33wEf/bn38B3v/cyTp+7gp6+Hrx45Aj+6A//CH/J+v/Wt7+DF198GbOzs4hGgvAHmIlgGHV19WbB/Md/+AN87WuP4IUXTmJ6pkgFqoQk63CR/KH2KT5VJxEJR7Fr927SLly50o0vf+XL+KM//mN857vfw9GjRzE6Moy88slnfJYfoXCE6Q5gZCSJh//mf+HR717AsVfOIM9ybWpqNrz43HPP4stf/grr4r+bfFy63G02KGC1I6D17TXzK5MlP+rTTqaFSVe9NzQ2ms0LVK6XL18iTz6HJx5/gvl8Cd3dV2Dpk0zTuTnKGjs/9WzkRU9TI7aynWgx/iMvvIC/+su/wpf/5Mustz9jGbyAJPOte8p4E/3u3LkLu/fswYljR8lfX8TvffGL+JP/+Sfkx7/F6bNncODAQaxdswYRv2a4mSQy3/y3BLm4eDPUynDnzJQcL6S4S8aIHGPV9BGUf+o/jJv6DbpL0VYfobbqN9+zXgtXabm5cIpf9eDUBc+W6s+ZnUeTy3jWzAEze6DaT6odOzPArwd7cKyqtJIk00TiIzuOKlEGOedL4fFg4uC1Idt16dqcm//Xurm4tWD4h1ANOnUsmNmi7AdEte72AKx9T3War8qaWrh17eINIXlAPU9E4WKuHWNavOX0Xdr0RwNVGkCSvuSsU2mekXQRn0nnrPKbOFnP5KmLyv9SX8dnxJMK29m0QXFpRlWRpL4wndEawQra5nXD5/wpPNM2qu6KZGmWi0kL3ZRevTzkUf7V1+aoczkvnfSQ1u/ysc0IJkyTHgVSTaPZREhhKBVyZ9DSbRmu7ov0jEMuXFwPDr+8EZXIo/pyRS1BstwM3Iq3zH3xnM23PtqB0gnswWa2GXOPvGhiIuju8KRxr54LzlGove9iGbLhfkMn//E3zOFthYSYCt1M4SNOnDhBw6/b7Eh2//33m53THBiBZySSff52QxW/Wri1DGFmd/FnUUhrNzkNuojBtOOfFqeXwanBH9HiYsoooCF95kfhqsEQuy9RnqnAaCbAKngn8ubgevlT+Wtg4ZVXXjG76G3dsg2HD91hGpVUJ9sIzzGrmvmh2SAhYxz7tVtd0Yt0ipQtwx8JYd32Ddi7Ywv8wQBG8xaGx9IoTE0iUEwi5Y0j42vD/q4GfHjPGuzcuBONbTsQqWtgQ57FxYGzuDI0iInhaYwMLmBodBHpnJfpOYyNa3cjy9/owiKa6ptw96a1OLyuC2F/BGPpMBYyMSQSTehauwZru9rRkPCjGBxGTz6Jif4iApkk1mhx9vUHzLpYHoxj6951OLRpO9r0yeM8O0TLj8bN67H7vh3Y1FiHUCWDiXwR81YTWpo2Y+/aLmxus2A1NaInOYne/itIjk4imC4jRGHV0LkJmw4fhuUvouhNI1XMYXpiEanpOfJHCOu37UHn4TuxbvcebGoJYl1pEOXFcUyNzSM/fBazFeawcyPqduzC5i3t2Le1DQ907sRafxze0DwWrRnMJEcwO9CLudlFnArQ790fxQfu342HdjZhS9SPUtbCYqkZQasR27e3oHk9+S9OQVnxIp4LwF8Mw0+hqTWpiqE65BKtyLOVF8fOYfzKq5hcCCFbCsBb34CmXUzH3Xdh/96dWB9PoDWQQrpSwNTMIqav9mDyyiUMTSZxoWcGHl8EzQ0hdLW3oS7cQr7wwB+YZKNJkokibC8NyKaymJ0YwvjIACamZtAzNopLY1dRihawfm0CneEgFvomcerFixgfGsfpvjn0TvvQtm4jPvCBHdi1vQ31sSCSi8DYyBBmhvsQoFrU1dqE9a2NKMe9GMoXsHPP3di/ZTM6G+oR9IbYDr2wvFnkyMgjo93muWI2jEBsLxItO7B1vQ+H9tdj966tiJIXy3kqO+kUksUsFidT6IgUEK7vQuOGPahrTqBYGMbg2EUszvhRmNVumY3k4+3YfvAADty1FVvXtqA+lUfvaBKejnXYuHs980f+jPoQ8NchjSIG5kaRm5tGZXoa6bkUUojCk1iD3XeS9jRgbUc96kMxRD1BBNne2NqAyAIylgdZlp2XZC2yPeailDuN8DV0Ytudd2DfwQ3Yt7MZG9YkEInVI++PYnHwNDDbj6FkGr35KDKJdejcsx8PfuwjuI/80WixfUBr82n9AEZlxIQXgRJ5vSyFlI3dyABz4x2HjLaJiQmzq6V2Lt2zZw+6urqqu2Xa6Xi30vKWwT5CSROpr5DC4mP7sgJ+U766LlJpzlOuqI/QALVR5U0Z22+n1VcIRqlZgVst307/oX5cu4FqF9LJyUmzA+6+ffvM7q9O/35L11sNVtMFltSA6lF+qDJWlUZ7Zp8e0bFIgzBHXaCQswe+9cJEL8ZEmXTG5gfqDzICU+ZFC3UFhqcdaQs0KGWg6VptTkfxvTHmlCQnWbxt0iB/gvxWf8I194Tqs+I1OTv5q83ne6FuHKxMv5NXXRcKBTzyyCNGf9y7d695qePIjlpevDWwXEem9pgPpc3hLckMZ1BA/LKYWqQfz9ILPsNTehFIHpJ/5Vm8ZcKoKRMHt06+X58WpdepnwsXLhh7QHV55513Yvfu3SZ/zjM63kp5eT/AyDDymjoe8VpyMWleIuZYB2nymWwcr0Wq8qPhXco+2UFae1TbTKf5zOxiGvOZHPSyT+3OYp1q8Mnis8Yvn1VdaiAsSWVOL+tShp9zpjUEgiHjT7s7+sn/Gd7XjuC56osiyciAX8uqSJoxXhlWko9Mc5rpLSm9lLvpbIaaVgU+rf3KNhEO+MzAQnKBujTDzOXyDK9oXkBKTqu5aGduRz4rbL18MnnlvSzzJD8qA3uR2GWYtJgycfFOQGUr+XD+/Hn09vaa+tFu+Rs2bDDnjty8VevAkcVvBPGdZnjlxLuptOHRNHVEDX5ZtE01+Gom2WTzmJmbRTgSNfJSYUtl1ICy2UGebmyh1VBt1JaLkxbzXE263mv866Rd6ZY80Y71L774IiKRiOGLjo4Oc+70KcLKPNZe/9Zv/qY5erS8sU6KNYXz42BlIUu4immFr3zlK3j00UcNM//6r/866urqjLuekV+Rc/5243rhyn0pzRR0zsCX1qsSnDcHUvR7e/vQffkKBgYGjRDt6lqL+x/8ICtgIws/bKdfwfDRd3vQy8nfUl4InaszklLV09ODL33pS+jvH8AnP/Ep/PK//BW6258Qsi0yvQvMMTuRchDpUr2ZzRLMT8DDTiSfCWF6voDpbBLepjC62poQLwxjfmwUA4M+jE36kC+lEYrlUN/AZxlwIp5AsLENgUTCLP5dmRzCyOgoumfnzPpWVjmKiNb6aqhD27pWNLeG4SsOYGZqHKlCC0LxdWht9CJSmkKBhsTYXBgLJR/K0TAC9REkAhk0Z49gamQEJy5sQBZxtK7tQPuaFlgeKosjlxAOh9GyttO8WSqOz8EzuYii38Lsvi5E/VE0Z/pQmBnDSLEeM9GNaEr4saUygiI71ssT4xgYXcDCHI3ZShMS9Qk0tIewYVMzMD2AxZlJjMzmMJUJIkbh1OAJUCFlGltbEGyKo8O/gJaFy1joH8bz413IsuONWQtoSARh1TcjF21EhArsllAc0ZiFQop+54YxNjGLwck0ZssJpBv2oq29DRuaI+gKW6grzcGbvIo8FYje9C74OupYFhVQXiJStNCYYzvTDJKg3qAVzS9fZIc/P4P5gQEM9PdjFltoqCZQF/Kx/Ck66+LA+i7UBf1Ys3AO+alJXJkOon+mjNTiLBWTebPofX3H3WhqbkBLfRiJoM8snu8LzJkZTyj7Uc4WMDU9iaGJCdbVAmZTVEeCMYQTrWhsbMLapgpaQlQqFkoYvZLC+Pg45sNUnGJ+1LVuRFsnqTGIRt8UMjNzGO6dwGDfFIrRJtSv28J7CTRWJjHBdlip34EErwNMhxa9D3ozCGSGWC4ZXOgfxNhYEj7ycFNCnyvGkEQOgYaQmcVmhVhEC2Moj/ZjjDxxbrKdYTVgzfpWtLSFEcIUFscuoqd3CKPzneTjZiSidbC0kF1DGP41CTRpV83cEGbYOV/1boXV2Iz2+jwaLZYV21N+Pk05MYC5hTyyBS/8oQgiLPNcxYdwUyeammKIMww/G578hzTyXORJ+AqK7PSmRlKYGF7E1ByNnYof8cYuVKw2hOMBROtLSDRU0BAqI5ZPIb+QRP+VPszOLmCi5EE2EGc7bEdD03qsW9uIdTF2knqfWrEH1tR5KiqJN79ecFJGOHtavFOySXDkko7JZBJnz57FM888Q3nUj8985jO45557THt15Ng7mZa3ilqZytJjQTGNKlWVHW/pbbI+j0iyLuYo365cvWpmr87MzMMfCGD79h3Yun071nR1IVGXoKEgo4Iy95pwbdxq+baNGXsARy+spHRIMW1pacHnPvc5o3iof7kV6+16cNJaC6cq7Lq2jXMNTOgzRl0L6tOlH6TTKTM4cf7MFQwPjdKgoyFGOahnLfYvmnW6efNmM8ilgV0Z+OvWrcPBgwepyGrNyaquoxioX/gpwDXrV3DcnRldmu0gXqt9RrDTqWa7fE8kl6UZaeb69cdbHU79OEdB5eRcawDoF37hF4z++NnPfhb33nuvkR1CLS/eGrDrwjkup81uW5oprbwlFxYwNDxM3bIfgwOj5sWA2p34UP4EtbXDhw+jtbWVfbI9KODAOb9V8r2yDnStfKp+hG984xvGHlBdfv7zn8enP/1pI2McA0bP3ip5eV+AcgSlvBoSpqenMDg8gsu0CSZnZszXFBoMa25uwR7KrsbGRuonUYQ0kEwjvZjLYWZyApfPncfl7svon5xFORjG5k2bcPjQQWzdvNH0gRr8KtNeWEyKl4dw+tRp85Jkfj4Ji/za1t5B228btu/YheaWVmSyGcwODeHKpcsYm5pAljLQCgWMPqZB0Db6SUTj1O98KNJoGBsZxakTJ40tM5daQJCydOP2Ldi9fz91nS74SzkzYKJ+amJqmvxUNnqb1gaWDRCNxNHZ2Ylt27ahra0dQTOwVsEow52anCLZL3PWrluLjjXtptgcPnT58e2HZIJIUNlKPuirGX25o8H9T33qU/jQhz5kznXvVq4DJx8OVl4L6eQ8hijfL1++TL1ggPbSNHWEsPnKZ/fevbSFG2nfTBndOMs2d/iOw7RZ2m1Zz35CXYh2KdWAsNeZnfgmUDqccruVy281qM4FpVkvR9S2v/CFL1BONeODH/yg0ac0gcoZX1JeawfAnLw7sKrnt82g1/Wg+Jw0e2gRlgssaC8NRX+ON4vwpLIYpWH2yPNXcHVwkhWRRSTsQSToR30giAcefBAtFORBdRIUoBGFpTDFpFXU5uedyptTbk5eBJ3XDnp98fe+hD42uk9+/FP4V7/0r8ygV7mskWM+p10Z+SuXvSgW9PaGCmQlSxVayrg9xTJf9qDkD7Oz8MGfy7CscsgXfcjSS4G/sq9gFP1gWW9y1JH6GbaUHH0+t2je/BTy2iFPZa0ZckEaCX54A1TuzIvaLOOh3zKv+WzAp10g2VEzS+lyEAVa5xW6eUkBlBAqzLEfL2E6n0DJQ/8MJ6QZF8xLMZ/h0cM6CbCzZwDKJ+tTaxBkoxHNe4G/Ms+k5ZBDCHkrbjrtWClD/2VkGG+2wA4/rzL1mzdaPgYVDFrwFLPs3PPIFSrIl9jZV99YacZfnkaPh4UX8LAsiinzOeJUIcxypfHIMrL0ZskfRJmGjo9pCTEdcquU6Zdx5gtFZPJaX8GHUqDOCDzt/hgk21gUeJ5SmvmoUEGoQyWoMla9s0zIu/4SPemPbua7cdUnjTR9YlnOMb3ZLPLQrCym1+fRCz9ZCSiHWA88DxYXWJEFpAsW01BBgXn0eAusS4vKSL15m2Z2GqRf+9PGgqkbhmQGhyWY8hokZbnlJZT1maUVNJ/9Ba0ygj52XKz7QobpZ1oKvBaj+QIR5lO7ZfJSfESeLZCpshnxFMuJHYPeyAWYet0r+aLkgWpemQXLW2b+2V6ZhjTzmSdPVMrkUVaYMdhpvHqYaA1AaMDCy3L2Fhg/07mQI69aPgTDqmOmpcI4Cil2OnlkCkHGS/JqIwfKBqYBASl3QJhto8yOKeWJMgHi1SJ5gPWj5k8DOJPRdH+2G16bafYybFVSbB/Ki2Szyl/+WV3GyIVvkSd8hsVa0Gw0yiINUFkBGnQecgqbknZm9LEsWWvwqVNgeeizS33+m5P8qpa5pXbKtIZUxqokPmGXln0lKG77hH/vkFxy4MglHd9Lg15Kj5N2wchDXpfY3gskzeqK+xZQnp7Di8++jEsXetA3l8QYZVBDfQNCWbZD1m19Qyf27DmIvfu3obVdL0j0KfJyuPap8mzn+1bIv/L9fhv0qvZyPFM6KYtZ7nY7qN4xF1KwdaQfymGdiQVEXi/7kNnT6DlzBn/76kVcGkrBqtSjMdqKEBtohI368J17sPNgB/yhCvquDODK2X6W1xrs+8SHEWEfFaEMtBSo+lzGo4G1IuVZWetbaqVEtmMv5SjYz5g1cygbtVEJpQtJj5UQZq9lsT+WzqKEFXxBhsH+gOEGeX0Nz1br5VavGwcOLzlHQQqwc31LDnotFbdOSCZ6+5yp0QXTZTsZxZwX6pdNMtlXL8zNoq+3h23sMq509xh9K8g+pZTPYmI6icGxNMKNHfjn/+7/hQ0bm9AWgtnUxsh16ifig4xEPBGQzqfI1MEY/evdx8o60LU76HVzoLI3M5TL1G3LOcz3XMAPvv99/PDKHKaDzdjYFMfmzADGxscx3nE/tu85gPvu3IxdXRHEklPInbuAJ598At/Lt5oNgRoCRTRFvGhpXYc9+38Sa7tiaK0fptmUxNTIOM6cuohXj13C4ELM9BOx4hCjz1HXqoc3vB67dm/Chz7SjNxiGudfPYmjrxzHRLqAUFMH4uFGZEZnqAP5seOnfwr779qBLXVJeEdP4dSJ8/jmaelHJaxNziAzNYmZWBMa7rgfH/3oQ1jflcLA5Svofe4UZkYmKSGTKIeZZ9oN/ZdnMTNRQfy+j+Luj34Id+1ahw2Rolkft/eHz+LYsWP4Xs8kGrbtwIMf+yAO3LEbEfJquxQwtqeyRflCPZ9SmvJXui1tIVnPhDjWcGq1fRuSLmegl422/eviWogvDW8Sauu37KCXnUQbjL720oFmPWryiO6SQ+ViSPzC3tnYLZfI68ePvIZzg9OYCFJfCIWRmJ/Dtu3rsP++3ejY0IHFuRQuHL+M2ekZPPDAA0a/CrJvc77GKGvHd0XDvt+kQ30A9QbxpEcTEGinzrGN6l6IykKQJx7aC0XZaqbstF8/bTj6N32EcJP6iDfDOzXotezDhVEc7MWHy/xpKm6OjJTB1XMn8TyZ9XLvKIKxRuw5eBh33HUXtm/dinBAu8LRFGJ52uoNmc+w3DKchi3Unr/bMPpx9ehACrTSLMFcQZDnNP5ZBKYZeCmwvXTjhRWoIBzy0YgO8Bk6VCLw+esQjkZR1xhGfbN2iovDHwmwkUYQ8IcQYGPyM0INMJUDAVjRCBrrEmhpTKC5KYaGhjCiMT8CQU3xV6QKUzN4NFihz4jUufjpHoQv4EOQ/sIMMMKGrsaMSiP9tzP+BBoaI4hHLTOwokEJXzgKTzBCeUAjokyl0AqgzLSxwhBmJ6gZNspbJRAzgyFRb9mEydBp58QQCtahLt7ARlXPRsY8JgJm4X01HJ8/TIOmDrE4jZ2GBBKJCMLxEIJRPxIBL+KMP0jBA389EGumnyjzG0d9YyOiiXpEKMTi5ButteRzdtbzMb2BBobRwry0o7WpBe3xABqDoCFVYbwqSNYRy7wcqGcZe2lkVdilephuL2uNlcpqMdPQTbOmASQDyhOExXINROoRZ7hNLKs6pTcaRJDlEQpaiLL+g+rIme9KsB4h1ml9fRQtzQ1MdyvrqZHKiF32fpaTqRfDS8yjh0JUuwF6LXhpnIUicRojDWilYGptZPnEQswr08ry9zEdnkAYAcafaG1k2Tajqa4R9eEQFQwWl8q/Qn7z0g/DSTRpfaw447YQIlN6yVNWKIZggDlTmTDdPmOckr88YaYhwvgbUNfQQp6oRzhBHozQyIyyzoN+M1gntcVHfvKE65iOJjS3RJk/xk/eEt9ooNbHMogmWpl38kAd78V8LC8fokEPooxPRiVLjJWcQJR8Kd7R54MeM5uKxHyGouSPunqmn+WeiCMSCSHGMo8wk0H5ZzhqcSb9zIsZ+WJNwBNjOUYpZ5jvhjqmrY58HUA8Umb8ZbAoWOoaMGHZs5zgZ3nEmxBrbGN5tqKFddUYjyIR8jIeBql0kRfVaTpKg7MWkQa7DfHcxQ1Cg5OqKvIRVQ22XRVyHmMDV/DC44/huccew0BPD/m7Fdv37zPrrmnQd2JiFpMT88hkNGwhZU9KkQJySKg9d/HOQL2086uWtjmpXlG2aSDKdpTCKmh40ouSpkSy87TyM0hP9GBotBdTiwuUaVE0taxHe8cWdLVvQkO8GQHKBctfpqz3ozFRh0QkgRIVUu0Cm81pnRx7MNSs8cHmp91n9XlPvlw0SVGL9FBR9uZppM7NIpXJYz4LpItMh2mzTBXTKV1DfqkDo8C0qTcXnLbutu2bBZt/7KPNa0JtfYjNbKogQP0nzj6iuaEeazpa0d7ahM4W9qMNEdNfzE7PYnBoEqlyABnKdG2Aopd4Rt9U5TMqSRS9otQMVA2k2Tzt4nbGsr3BI/moUkijmJzCZP8lDIyOIkk9pqljLTa11CE3OYzHHz+CHzx7DBd6BylzkigsTmH0zDFcOvI0BmZSiK7ZjP133oO77zyMDevXI0g9uFCmhl9eQGp+AH1XTuDEK0/j5KsvU14GsXHzbjxwzx249/A+rGlbg2zawtjoHFKpMZ5PYHz0KoYGLmMxNUd9ibZBSzsqqSKefvQZPH3kFHrZZ2YLKZSzI8gtDiFNfbNx/SYc3L4L66k7TrBNPP/qeVwemESWNoM2XWqh/tlFXaiDuntrc9jQ4swU+i72oncqjSnK8gx1yHwlj3x6FvO9l3Hppedw9OgxnL58Fb2Tk5jKpZGlTPZoYJpy2MhqpznrH8tVp07pLl0sOaqft/t6F7cDHI1CTKKvxTTIlKe811c3KRRLSVy5cArnjr2GqYlp1HVuws477seWjTsQCkTYVvRdTpa2pQcNiQR1/iiiIdo7GmhlkBrbqlBnKObzZjkFfSqcSmWQ0yQSynpNbigVcsglF7BIvxn1DOxr7DVHmSIGoFEN9RFG8zR8yn+3YR9hzCIXNgxjUHDCR9J0i1wO+ZlZDF/tMZ9rRanY7th9AHfu24e9u3ZjB42aIJUU84aXjKnClKDMrVKqN3Owy4FsayVNirLeaGvwq2zeVmgQy7QNo0h7NbBBMp5p1FVoNMus13to06g1qizP/Kdw9IZaufOYN46asqUGL6IK5mVZ0o/WDrLKlq2YKV49wTKR0id7XzOV9Emp89O53PgwSXDOmXo9ZE41ymMXthE46pXYQZk3M3QzRH9lk2ldqRPSYpt0I2l2kkdk0sEjw1D6RLy9jGsuqnCSUwOleyVMXlhOtYMOb2iIvNG9GoifRM4b8LcMPaIyqIZTC5NGZ0Ck5udgZfpXjb8a/kqYcK6bxRvLu7DksyYec1Baqum5NjT7atlt5XWNS63jjwinjJz6tq9tN7vMzalBzekSnGzonn1u15Mpa9ENYmVduXhruLb+BA2ASFLoXpnikTJlbgz9l07iVO8YhothNKzdjjv3341De/dj/x17sffQLuzYuQXt7c0Ih7T2l2kFLm4SVi97u07tIaRVfPCm7YMo2Isme7MVNIfrsWHTemw+tB3b7tqJfYc2Y01X3AyQ66WEPl0sBKPwxuMIJGlMXTmHKzSyhmenkDEzhtPIZxbQOzKOwbEpLCQzDD6PYm4RyZkBXD77Mp58+hU889TLOP3aSQx3X8HC1CySZT9SHvan1D30eZK6OD/lgt7gXsuv4tNrr128k3D4R9ziUBWqg6V6YJ1owNy4eWEFgmhobML6DRuxb/8h7Nt7EDspM9av1wucOnijrYjUtSJGo97Pftlbou5TtKBZ8zkaVnkaWBYNJz+NH1sj0n/7zIULI9v0j/qi1pnUZk9+GtvtHV3YtWcHdu7bjG1bO1FeTGO0px9TA1eRnh3G5OwcXro6jxE0YdOG9bhj3y4clv2zYw+2btyAeAOgiehYzGDg/FWcONaNq8MZhFs3YO+dh7Dz4C72f/fgwJ334+Ddh7D70EZ0bWhEmLzvTaVQShdoavkQb+5EF/vLjft24AM7G9DhG8VIXz+GBrRURhiF6HrUrduPQwd24s6DO7Hnrs3YcaAT8ZgPs2NzmBufRyXrQUO0CVtom+05yDa0Zy92rtuAtng90j7K3/Y2dLYm0BG3UGelYeXHkE6O4epcCD2kUDCAUHkR6bFxLAwlEWD70tcKsChn2Ub1IYUhyvWSsSfs3mK5gVM/o21S4b0yZDPZs/tdvP9h7DujG5KM3SrZa9vWZTJNiabw5OgsFiaziEdasHX3Xuy/cw923LcTXTs60VifQLTig5/+ypYmbMRR8QdpKxeRJY8mJy5jfOgizl+9iFMXz+ClI8/j1PHXzJI14xPTGBgcwbkL5/DCkedw5rXTmBiaQDqfR55JKMhepu3rpe1rUqZL8W91ltjtBrdXrEHBVyKT5FCmEqFPyTCfxPTFy0iPjCHevh1tux9AU8cmhDX6ny8g2NoMq6UZcQrGeIGcVCpj3ltGUgNGq8AZHHCO7za0how+idJUSCOYJcCrM3U0d8QMPqnZsqF5SHqxrUGxEkIU4GY+kHGn+LdbDhW2EvOqhqk8efVZY0kf7GWpx6XZ3jMkjXZXECgESfpMw0sFTW+k1R0oLUwThYSfibHFhodiQnOUqAiSmDjTqUiYLLOrOha6azaVlH7bxQxcWcyf8mgPxlEvpBfaB0yHZgUx7SS7A2N+6UHjm1ZJxoKdd/a/hkwN2gFfA5mr1/yYjiWjgn+rodbP68j8qo/y2obt8rrgap4TavnprfKUgrgmrGpGHbeVg3RvRpoh6dDr7lHB0dHJEF2rCTARLvkzTlW36k3z3zmXu/Hj/KrXurUSuu8843hY/m+fCdWQTFjOlbm/9JzjJifb342Sk+9aYkWZsJZLfCXoT78Vz/2o5OLHh1OO5qjZlpQb9jo7BZ4vIH/1GIYvvIj56Bo03v8PceDjn8E9++/Dxo616NrajnsfuhMf/8SDOHxoO5obY5RTtpxz8e5Dpb40HPG6BlhVWk0/Y/sUzBk928MXJPb/WjC5sRDG2mgL1m5Yg5b9a9FyaC0276qnIVlCzJ9DsJAxizhfnF7EUC6P0MgFDL/wXTzz3A9w5NwpjM5NoFKcxfjgRXz/6Vdx/HwfJqeTWJibx9jAJZw7/hi+88h/x9999yX89V99Bz/4+t/g1UcfwemjJ3A1WcK4h/2pV8aVPaM6UmFPTflSy68OuXgXwfJ2+MjMBl2iJc4zZD4rqb6406BXvL4BnWvXYcfO/diz+zA2b+5ELFZATp/c121B17bD6GgKIuqn3lIMALkwikUfFn0pLFopamdZ1n/e6E+gTqdwXbgwoHyQMe4JBs1LXa/lR119G7rWbsKmrWuxdnsD7r5rAzpaOii3qH/PjyE/3YO+iUk8MRzGzIaHcHDPHmxsrYc/lwNSBdSHI4g2AcEYReJYEueePY5XX+xF0rcZd/+9f477PvUT6Nq5BqG6TiRatmDHoZ148FO78IGHtqErUY9oMoko7YVEuA0tm/ej7c570Lp7I/7+3RH8wj0eBItljPQXMDTbiFTTByhffxaf+Im7cNe+DWjcUEbLpjzWdETQ5G9BqBCBJx1Aa7QL6zQgd/Awdm3diQ2RBPITs5gJdGLnJz+B++7Yhu1NUTSX5xBKX8Dc1EWcWliHZPOHcOcd+7G92YPCwBDGT0wilAoCfrYzK0CbwEO7hT0+7Z6ip0Q7Ri/Q9aLcLlvbYCC8JZRpaxRpM4lo3VRvuHjPQpXs0HXgWZo8IqLBWSUtjVMukWiEWuTRSKUFEX8nvFG2o4SFpjuaseHQGnS2NqKRstwzl8XwTB6DpLlcGcnMPOZGT6LvxLfw8jNfxXee+QEeffaH+ObX/gqPffvrePaZZ3HkyFHqFC/isScfw1e/+VV888v/CyeeOYqRiRnMkQMzphfKMXV5Y28b093Y8NWJKbcZ3F6xBuYzvHIZJX16wmMxk7YXTZybM5/czc7NksGO4G+++jf45je/gfPd3eZ7Uq3ZI/+aNaTBI4u/1VCrjN5sXM/kNs4yzGtvVxu8rUAzh15zYUi/6k04zsbpOnBuX+NlhYMdatXRxFO9bf4J1ZPXXfMo0lskuplhMl6ahfo1a0lvVnXPPiz7d+KwD0t0Dcx9hrGSan62J/uwKlZ5Xm4OLT26dGLDPtV9eyClll4X3ipY6Uf0+nBYICbe6n1DdFe5Vd3s2V81cZoHlsO/Nrxr3UzZy381iSYq86uBeYb+zXM8d+Lj0WznXnPfDt+OZ+laofEoqh5M+DatcHgdlu85YZmjifvaPIlWXpsQVrnnPOsQHe1IqjDNjO1tubnZRuvyIKLCWA7HLg87fBfvLszAsvqH6ucOrBH4yl6Mjo7i6tUriMYi2LhpI9au7UA8bpmq9tP4bEw0or2tHnV12gXYXierxHBc3EzUdnCvxzX9I+vRaW1s1dU+hHXPvl/yQTqDWWuwxGOZvOHTDAEfcoU8xsfHzEL2gwMDyOcLmKQReerkCbzw/HM4e+Y05mfncPbcOfzwhz80uzkpnqHBAfzghz/A3/7tNzEwOAyt7XHo0EHMUw955pmn8cTjj+MydQ+tpWnP9BUvMb1iOFLty5Dao4ubD9WUZpkbfqrWl0gy3dJ6qNGooXAdjfViEX19/dC6h3V19Th46BDqEkFoS3sTgPO40XTk4MLFdUBG0a6MhmEoD2z9BAhouZAozKfX2r3wam+vPJslGbQbo9ZcS2VSZg3Wqz1X8cyzz+E7332UxvYzGBoaol9btsxQjvX09Jp1wbSj7969u9GgT3N5X7stqr8LhyJoqG80GylJhpq1eJgGrdnU1NSIlvp6JPwWKvKTsNd7NrtDWlqn14tohM9HE+Z6cXAQY0yrdmfs7OxAe3s746s3u7mZLFIeaw3bYfbNJ06eNDNuP/rxj+Huew6ipaXBtBZ9Itbb24OpqSmzycxdd91l1lCamprGlSu9zLvebxTNC3ZGzzZqkmSwuv3kytnbFeI58ZTRD3Sif2QH9b1qa9roobm5CcViAUdfewWPfPNbOHF8AjHE0RBpRKDiRT6TxuzsLPoo78+cOUv+S6NYKLLfn8fRo0fxyCN/h5deehmL6Qw2bdpAvzN47LHH8NWHH8axY8fN+s/aQOfKlcv09yK6r/RjIZlDoVRNksufBjXN2IWGqwKeCKxyE5DvQDnXhKlKH7qnj2No4mUMDD2H6cljyM5dwMVTT+FP/scP8cyTPbg4OocJD40hrQ2FAMIMye5UriXBOd4M6HNBzW5ypjfqC98Ck6M3GFLE7H/UpD1ZetYi9gUKfE3lhfFXMq/GpbbRj6UtGDPm0wqw6UJrHPEZy6dn2YvKrRQisSwYTzmQQzGoKfgR+MsxlgM7Nx/D8eYZHAPnqdbc1owrX8XHNAZgPpVUnLxtRqcVPS/0fkUTNZ3pxh6NYJtPKtkVmREuqYFyY3xFCh2GzV6dSY+w2YfNR46iEpUALShf9mlxvwBlggehcp6kJYMF/VcEEmU15zXkwCRNMDPTqn6rMDZHlZw7dojX/lbecc5tdxsSoo4Rs1o6HKzmdi2ccGv92bFde6+GTL7srNiw3U3W+G+JzD37aNJrX1ZRE55DSqvyUXWp/b/sJjjps7HyvJb0f+lnyugal6Vfbdpq3Z1yFffWwnF3zt8Iq91fer7mnkkD/zllZ5ejXc/2uU32boHL5OLdQW2Zaz0lX9iCFcijUhxlHzEM32IC3mQC/q37kNu9B9n2RgTDlIV+ys9SBIV8GNlyCUVvGh7KR61XaGmKqantN+YhF283NMdGA5Z2EzTNsEpGdPOOXl3ZQ5Jq//Jf7fMqeZ6zv/J5EAz4MVTw4uVLfXj624/iuT/4Q3z/v34RX3j4GTx6Po/J5AI8uXHk5mYwMVLA+GgB5a69OPjAg/hUZwVdZ7+Jl/7sj/E7f3UCXzuVRbBlHbp2H0KnZxC+i4/g+NHj+MrYPSh85A/wuZ//IP7dz+3AL32wHfe2pJAe6ca3j03iao4GY5n8RCqRN/O0ypg6w6fOZ+8iwTm6eGcg3tHMckO8tml5tpd0FpFqQX7V+rXXi+EzWdNau1Szs1RPnssopE+g+2IPXn4xie6+ZkS3P4D19+xCS3kIrZUh8t8EKmGtJ1dGiIZTCPXUc6RzaW1LanbUzyp6k+/CBaH2n9cMVX8FDZUSYtk0MldfwplHv4K//v0v4zf+4Bn87pMjaP/Ur2LHP/n/YOueA+jIDMMzdAb92QVcHR/BUO8AxvtHcPH8aTz+9HfxtUf+Bs+8dgKD2mV6NI7iRAtV/k3A2p2INq1Bm28BUye/haf+5rfwyB/83/GlP/gi/q+/fg6PvHAVoFwsB2g7+KaRmT2DS08+ipf+/BG8+tir+PL3u/E/LhZR6FiLxNY4GtoLaKyMw+p9EX2P/D5Ofvn/wh98+Zv4z988gdeGptG23o+1m2M07v3IgPYHLiMz/ThePPIKvvIocHT+AA7efT/u2LcW6+N+rKnMoSGdR2Yggv5XZ4Gdrdj/mY/gYw/twk/sbUZzUwgXU15cSAFnyyH0aTatJ49oJYlIKYVgoYwwbRurSDtFZocK2HQoas223eGv0JYkrdQfXbxXIcntSPZV+tKqk3R7e4Vl2sMVEfnEW4eAP4E9D23Avf+wGYc29mLri1/CyP/3X+A/fukJ/MVLKQwkk7CCs8j753ApOY6Tk33IZcbhT83BkyGvLuQwW2jA3PZfRsfP/DZ++Z9+AD9xJ3k+HcXc3D50bv4U7vjp+/Dxf/5JfLI1jW3jr+LK6BS+nw3hHPWVQMEHH3k1UE7T0qWW4NH++3zeE7ETfhtBTdVFFdqBQcqikVNVo1Rv5YvFolnMe9euXfjIRz6Kn/3Zn8UddxzGxYsXzcwvvQHRGxE9WipXUNTJKngzI/nWANNYtQb0MzCaGv9E1V8tnCvbf00ea08VpHOscV8V1fhqsfR8lQyuuXDwOgcbq4Rpu/EfyTYQlt2knjppXcqX/bcC9r2qj9U8mLDtwB2s4qmKWh5Z6UvhmFkiJMeocXCjvCV/Ij2rWQlmlgJ51uweSLfaVOrKLpcacvzVkK7lewmrOJnzJbdrLpagK3tgZ9lgU3zLcTGtS+dMf60/kX4MRGRgKk/l4tD14KTFIRtOrSpsB7Xx1RqWzrVDq90XOeVvh21j6ZyHWncHfNL8qhdLtDLs1cjFj4eVZWkvGkpTloaqpU0PvD7zFlxv8CxtP0qov1BNaseZHHVwvWD3+7Tzqa0E6y00AzR+XdyaqG2hqntbRkpemoZn3DULYGFhwcz06+/vM7PC+/sHqITOoqglENjOnRmr4gm9id22cwcO3XEHGhsbcebMaXz1q19Fz9Ue/PRP/zTa2xuQnp/FxOiI8b9+/Xrs2LGD0ZUQqK/Dzr37zPbm9Tzv7e1nP6BUMJWUM+I/zTRzZPtKyN3BavddvDtQLYhUA6YvE1+ZG/pv85jWEVpcTGF0bNzsdBuNxdC1pg3trfIi3bLaf0sWmV+VJd1qdXEdqPlrtglNXzNrSvJlZnoaJ0+exN898nf4m7/5G7x29KjZeGX3bg00BVCyfMhrXeNCHvUN9bR57sTP/MzP4Cd/6qewceNG9FLePfa9x4wdJKZWuNqdvVjMmxnN0teuXL2KEydO4LnnnsN3vvY1PPynX8H3v/+YmbWqWVyarT8zM2t2c9Zs169/7et4+KsPm1m0hynrtm3SOnZ6PV9iOgoYGBgwfoeHhqo2F93zeczPL/CoNlUyu2cP9vWZ2S5K2+7de/DhD3+YafQjT/8VptXD/KenpswsXLUx7aSnHbAz6QzDmsfoyBgGByZBsWrallqZnrMHqHXiwsUyrhG94i8dzFGzvNjqqBuu2bQRn/jpn8Gv/Mqv4Kd+8qeoO8zj737/9/HIww+j79Il5BYXDQ8Gg0HEKPP9mvXINqS+W7ug7iEfH9i/G7t2AJFYBK1tbWhrbcW2bVvNeERHR7t5rmttF6LRiJm5ubgo3bSaGDGy6Shub7iDXjXwVbzwFn0UpHPIBCkMI1fRkQpgQ34dog0fQGjNXWigIrpucx2272hGU2UY+bEeDC3kMFDyYNGjXQXzCGqBuFVws5VN87ZRQpvQkvLMqWmcSzAt1UvhrknJWpReW19rATzbn4aCCnTPI0DdiwZe2YcSewK1KXUKFjL0mzGzsPLsAEtS0LQblZRyxqYY1fjUZ2hWnUbCtVufHa/c9KSmE7OT47WZWaZPTZUOKodmgzv6slNO85HXIquaKi2eX/Sxe2TcCt/EIfdKlvnmPW+Fz3rM+ieiojpBTwBa6K/syTBptFCZJ0N8eilhJAke2wy6loy7Idu/+UnAVO8vu8nc1c85Vn8sP0P8KdXO+dKv5r4DO/y3jtc/51zb6TTEuJZko5OWFfmxF2pcSUy7KYeVJPfaslTYK8LQefXa3lSAZw7JtfZ6OXHX3l/6OTV3gz/Gez1ST8YzhqYoFecyVrt26I3ghCdcc14tL/5bOn8j4r/qky7eaSyVOaEdccwsU8ogC0FSAKlQDrlYCeUsZX+GcqpomV32Ar4gtGGsduoslnIoGIVbu2lS5mlmqan/N+YXF+8AVOS1xa5qqDYn25n1baSIoL5PvQZ7OfMmn0TZoAGncMCL9tYWbN6xHzvu+DAO3PsJfGLvdhzqYL3H4lgM1dNwDKOZRlgjNc+cN4RcXR2aG5vQHonCR36ZHZ1ALp1De2ML4kE/Kr4cUpVFM2srEduMeFS7Pg6RXTIIR8NUahsRZph6AxzTRB7yUsnjrB2jHppOVX51eNbFO4/l/ql6vQpdq1HwWvWjE9Nv2C9ITJ0V8pgaHkTfcAFZ8kDn3h1Y31VBjOqMp5jg/Qg50o+CFCk+FyJvBYvUbXhf69srEc7cMhcubJD7qO+msmXMkUdT2j28qQs799yHj3/0k/jHH96BPW0lZCcGgYUsfGSmohVC2R9EZ8DCxjUdaOnoxJr1bdixIYwdbWnErQVcGK3D5fEGlEJZWHVpBMp5+BfId3kvkp4IPBu3YvfBPbjr7gPYum4tEnny6eQMZiircuYri0ZyaRti4Tasb++gAb8FOx76AB763D/ER+5qw64mH5poa0RLMcSia9G06UFs2P+TuO+hT+KjH3oQm9Y2Y3quB+f6jmNgYRxzlIPp6VkMXO3DhalFjDWuR3T7IazbmEXCN4NYKQM/TYJMMo/xyXEMDQ/jymsncPKp5/Di91/EsWdPYfBiN2YnL+HkxaMYmS9THrOZ8TlPOc1ylE3D/lsNTW2dJNvHbIImmUudwKMdyKv3DLl4H0CC2iHh2sp1utolFzKAEe/mEekP1CBCXSituRN1++/GwYc24GM/uwUfai4icekozlwYxPNjPvTkEmyp9E17t4h5yvQS8hXaqOUE/GxPrZUUuqg6ev1hBAIxhIIV1CWKaKzzk/Pi8OT98Dc0oxThOUPQuqJBdQP2bnE277I9af1rrfNlvpC6zeBodi4IT0VvQshy3hyZbQbF4DyavBG0eFsQiq1DqLEdoboIwjEvWlqiaIlWEKAxkypVsEBFOE9Gt6gYe82248tGcK0hXHv+roMN0I6djUptoFYi1zRaKdD2ByCOwu8oTx7jbgavzKAA78gA4B2qbLxjf/6haw2GmbzK0GMD055Cdph2DCasiuJhWEYw6M+OjyXGcPmo8cq4SVUv1acVjkSD7WZ/QMB0UrhooEyfGNiDSyKlhvXBowbSqjGb9u/kxaTfLExJw0ZbPZIPJKScARvbeHhzqh3gsY0O+9qsjcWfc6z9OVh5bl9f62bWePLa6Vlp0KzGVyv9XAuFYadvObzX+1/pZ5lWe845V90qTTaZQteBF7XJrD034HVtHLWodTekX83RrH1VJdtdqbiBH/06aXbITqedOB1NeMbfMla6OddvRMLKPPOOHrb92FerQK61VD2rCft65OLHg1OGS2XKn9lEg/LNQ0GjFyWRphiCdSFMjIzSWB1DNpVFscyexGOxP6B8ov8S+4QiZaEkaYXPUAsx4bq4taDmKaIkMdfq2USqcpsHbCfN5g6HA1i7dg32HjiEux94APd96AP40F2Hsbm9HlYggJwviJLXQqhQRFjrfXkDSPK5Qj5Po7KMaCCIRKIeQSuIxfkkO0360QsfbwEFnmcz2p3Pgs9KMz05M5srky2iVCgjQUPUz46rrP7KFzALU2tGWa28qiUX7zxUyg4JtUfnXMylPsC8+DMkbYS/6qxg45hJ02i/goGhWURaNmDfPXdg/bq4zZGVEP8FqaL46Zd9MK+0JIRIrGDUlyWL24ULG+IGexjUh6JloRIMoqltDQ7fcQ9+9md/Ep/9+x/BA4e3oefEUVw8cRmz43PweXwIRqII86nW5ibUNzYiHA2ipcGPda0BNMZ8mM/GMJeNwke2jNHdT8U6ObGA0eFpZOBH5+bdOPzA/XjwYx/GBz7wAWxbtwFRzWRkX6idZ4ulAOKJDmzdsgv33XMPPvXJj+MffO6zuP+TH8O2DfVoDnkRZn/pRwjheCs277kb++/6CD744Y/hEx//GLZu7MLkxCBOnz+GoalRzGaz6L/ag9GhEdS1d+GOT3wSmw5sQCySQ9iXZSjsg9N5zIxPY3RszJgxxWQKg91X0XPxKqZGZlHRbLX8Ak6fO4Fe7YJXsm0gvfK37REzsrzUxGhxVEnQPdlH5oaL2wimuk29OxVPHhGbkGck2/OeCHKBJqCxBc3b2nDPJ+/Ez334bqzxlijrJ3BqeB5jyTJ1RjP9gTI+b+sDslE1OaRsIVBgqyIbevTJLZnXpw3avDnqotQpKn54qXfm2V700szLthhkX+BXJ6GEmX5Bk03USdi2tm0f314w/ejtCsewdVCu5A2j+TwU3uUmqhbN8LW1otgYQCHVC196AL5cBrlUEJlUAFlfAp5YAmF2IlrFSu/upXBoXtOtCNPpsTGYNxLKO//MUJQpBipeTLtO7aaghqFBIK1dk6WinUa+oNkKuq/A7OfNc9UfKmxQbHRLxcqTCo29crGIina3lP1Af/ZnaUwNndQe1fGIdFuPKiz7nD+TTlF18E1hmgh4pYMB01kpmNFxL7U+OasGlM6KDAGTLxoD5jkbCl+bbNpriFHEMO0aBKtQAFV0wwiK10Nxr+SbG8FKw+NHDUeDXm9l4Ot6cJ5fSdfDG/lz4v1R8vN2443ycLOxWtreUokZzze/jG83OPXm8L5RSaQ4lDRrK4yGzvVUsNdisr8bA6dexlRfN9LJJDKZLBbTKczNz2J+dh7pRcnQoi2XTIgu3n2oLle2w2pt0HnlXfVT/Gefs+4r7D81yMRqhL8SQH20AW0dzejY2IjOjXG0r21COEblE1lYpRT71gIyfKZg+REszCI5PIBTA1PozoWRWLeRhuY6bK4v4fix05iZZj/rC6MSjqPEfjc/fhGFyWEUMh7MpwoYnUpiZJJ8la+goZG6h7po7UjsK8FiPye+XIlbWR6+n6GhLJukdTnnVYidSEvu4i+SPmPV51q5mTS6L/RhbH4BDWvbsWffNqxv9iGMNIoaKPBZfM4PX4l8pheHVOCktzhx2AO2Mr5fzw8ubm/IoKawQJnywhetR11nF9ZtW4+du3firn27kR+5gJ6TR9DTO4y5cgK++k4EKzS00zOgEURZlEK+6EPBG0PRE0IsAoSDJUTqI5R9bWhptMi/Pbh0/BgmZkoIBTrRuGYNWjd0ob2zA03xBoR8QbYKP41zH3K0D4LxCDo3bcK2Awew6+BefGDfPdjUvA514QgCTKenROOfxn6ZstRfH0espZlhNWJtVxOisTjY1WJ2PAVrfgLZ4R6cPnEVwyN5bOzaiE9+cA+2dYWQW/AgnSqjwHDmF8ZxZaAPV8YX0LJ1D+798J3YcXAz1jD/O+5/AHd94B7saIph+sxrGDhPGbwga0LWXcDYRUUWociMHch4Wk3E2g3RxfseVWFeJWcA1FiYZmY4r8oF5PMZ5BeTKC0kUcxWkA52IrT2INZtPYhIosl8QpxJLaCYp97A9qUls71aMM6rr5TI+54U+/qs6eNLGnulwWx3G+TpYt5smuPxagqYjyZ7hm2Vz7Ftlcifsvc1YGbIGN1Kq6aKVAdobzO4vWIVMtgNc3lTvKKwLW5GrLINnp1bsLg+iMneRzF+7NsYPHEBF08sULDOoz+bgNWxHl0NdVhjWYjoMz5PAWWzSPEyahXPm6mE6rO/AklqmPkCs6QBLw31EBoYIpWYPm16nYOFSjmDSmER2YUxTI32YWh4CJPJLO+xvEoaELMbuAb5zABUWQvXh+hsCwANmuUzi1iYnsb8RJLtsMQo2RCpqNuDXmqA7EDUJtn2SmZUW3OyeG3Sw2PJHiVnr0f/vKvZEoxXDzL5Rq54ykwR0+nJs0vSVt7sjZTGHFNmj8NJGGlATE1cA3qajlyBn9fsrxGgMPBWQgzPQsnP+rOYHz2reGug6xuh1bCav1qqRa2bY2g7WM1/LZz7q/lbeW81+lFwo+lz8lJLb4RaPyvTuDIMx73W343SStSG+2aoTcdqz70uLt5WjA45qHV73TMOrXhipb/VyMXbA6de9ck2S5YyhwJL8s7fgGDnZrTtOoxYfgaZ889h4JWncOHYCVy+dBkXr5zDq0dfxemTZzHUN0rFWy9WfEbOsoKqpAhMJKvykIu3G6awTbGbFiIlUKRT81+XrAce1d+oj1NfpLOivPljNNj88KTY11BdyJVyWPAlsajNwb0zrN8kwuU5xIoz8JYySPppdIWj8E+TB155Ht86PYpXA1uw/v6fwOd/chM+uGYRTzz+Ai5fnEQ+QKNwzQbE4hZiEy9j9vgPcOH8MI5eGsKLp3txsX+eBlecBl8rQmQ/y6KyW0mTH4uwmEg/jdpa/llNBrj89c5Ceo092EV9hDqLIfKOSBsvms0X6UezuzQT3kMlxkP+82j2C42ekauz6CcvZGj0xzZ3om1NCJ3+YTSDbtplj8aNh3qWvxCiTkM9zUt9xcoZjlYcHmPIyEin8uPCBaEWb1Ev9hXKyJDP0pQXs+y/JsoRzPGmFfBgV0czDq8pIDT3Gi4MjOJMbg3K7Xuwvg5InjuCS8efw4VTJ3DibB+OX1nAZNqH7VvqsaatglhnHNsPbMHd+5vQ5RtAz4tP4JkX+nDifBq9A33o7ruE/t5eJMfnqHcHYIXqsUjezVE3z+rTwEQdKi2tSFsehDIBxJMBRKngB2gveLK0QSaHMHzlPJ4/dwav9V3GlavHcPHc8xgeGoXfWo9Nrfux3buI0ulXcfKlEXRfCSIzm4WPMne++wrOHxvE2VMDGBi4hJ6hUzh69SLOTANd9/0k/vm/+zQ++/mfwcd+9VfwyX/77/GZf/Lz+NmtbWi4chyTZ84jN5RBKasBrzAKHrY/NqtcdQyhbLEds/wkZZdI19VBMVPwLt7bcCrWVKZTodfUuPmRG0hGSyDZXw7pmC+mkUrNYZJ8OHT8FK6c6sPJbgsn+0I41ZNEuhJGfWMTWlsSqAtZsJJAeF76xzw8gUXy2AxylVGGM0l9wl6aRxM8NBOzSLs4y/C1SUW5EmEKLERo+YZKaRRLWaTYzrW1gjY4QTFokqu0lvlsmX2EBp9vN9zWg161yp/OA9oeV2/RNJMmEECwrh7r1q5DV9das534k08+hT/8wz/C7/7u7+Jv//brZmveAwcOYPOW9UjURTTb3A7LPhi8VxVMW1dm800mceXCebPI5He+8yhOnbxgN31ltmQPQtkNnlTSqJIPfp+tehWLJbPI74svvYjnn2MHNTyOggbLqjD2Hhtv0V6RV4XFIHhOw9JXLTeVn8fSVH4pcjIIFTf/KTp5VXCMp5TJoJDJo1CgmKGbdrMqVAq2Yslzs4gn61ZxZnMZE7YyouhEikcLDuoDV5Mf/gkrjQaTnhq6Eax8ZjV6t7FaGlajG8Fqz62kG8Vqz63m9m5iZfzXoxuBfL0ZMbAbIHvG35uRi7cZRmjxKBmkv3wB8UQCDz7wAH7qJ38STU1NeO65Z/Gf//N/xhe/+EV86Ytfwh//8R/j29/+Ns6fv4DF5KKpPvNeQDB1WT13ccvAfrHC7syy2I40o0+fTrM9qf7ZYUSjUbMwvdoYW7+5F6ACafmDdt9o/JXNYvf6LDHgD5iF7h9//HEMDg5g0+bN+OhHP2q2yd9pFquv4LXXXsP0zDQ2bdqEe+65x2zj/+1vfwv/9b/+V/zhH/wBvva1r6O/vx/r1q3lc3egMa6E0mBkHBpkcZv7ewum2Vfbvg5OP/LCCy9QtylizZo16GhvQjTspWHvZw1XjM6zBPshm6qXLlysCsoXyQnxinThUCiEQJCyyhjOlGG8bmxtpVy5G5FIhLr6EKamp9HR0WE2z+jr68Of/umf4vd+7/fwx//9j/HMM88Y+ffQhz6IQ4c7EGiIY+/BA/jExz9hbKKhoWH8n7/1W/hvX/wfxmb6/d//fcqy72BsbAwNDXUIhoImDeoGw+GQ0c2LhZLpVs3OL7wvgVaiDC1Qfg4NDeHhhx/Gr//6/4Hf+cIX8F/Yv/7O7/wOnnrqSbMpyIc+9JBZ7PvqlSs4d+6cWaD/29/5Dn77P/0n/If/8L/jN3/zN9knfwH/62/+Fx5/4nGcPn3aLCTe3t6B5uZGREO093yU4D6/sevU9trb2zE7N4uR4QmkaV+o7Dx6YcUkLlsxLlzYsOX38ksnTezQzF1taCR69tnn8Ed/+If4T7/924Z3/9N/+m1845FvUqaXsH37duzevRttbW2wyGMNDQ2mPUgvkG5hGT3EazZtMKYwz809XvipW4h0X/5MOngeCIbMovhq+9JFTLuibW7GN6qdhV7o3W6gyLPN+6IK5m1A7SCBCr9IQauKEL7yla/g0UcfxdatWym8fh11dXXGXc/YDKMpe/b5u4Vr0punKGN6M5YHmWDAvCcLYBqTA73oPnIFE4MzmCjkMR2oIBAO4uBdW3Dw4CGE/FEWoh/BsoVoQQoveSxgM9PKvLxTeXPKrTY/OleD8pHZpXD/l9//Y/QMDOGnPvZh/Nov/rxpBCUzyEcu8Gjwyl5wPsucFynZG3PdwMwUXjx2Ao8eeQ19M2Uc/omfxz/97CdQv9AHf0DPxhhR1CwKvxgAlXwg4lmAv5xHMZXE1cuXcexMN9Kx7XjwwQextZ4N1Fs0C/bCp05Yg0wBJNNFlMJh6PORCFMQ1tbDmrpfibOhl9kZpdTOq6CKz84pXQmaTjI0ewIzfRdxccSPaWszurZvxNoN9WZEN1rOIVDMwVcd/CoxY/PxZtNxxfP8x7C9rGgrqJljNCC8JVNmfn0fXRVgDrlw4eJHgyOXdNRuSdqBSYqzjPjPfOYzxsgPq/3z/q3a3pQ2bbJRLFNu8dzr1WYfPmi2aSFXwdzoCYwOXUZv/zCGRubMGg6pYCOampqxpaUVm7rWoHlNC6z6KGWgF8El1dnJK/Ntzm+NvDv9h/pv9ePd3d148cUXcf78eWNgfO5znzNGkfqXW7neXodqF6k1HgWzHqTp/ezVIZkV8zZVG6PYU6L1AsWLXEVrtHkQSg1gor8Pl2bDKAfraRy1oL2jAT6riGBlAlaZ5VAqI5/NYWJ8DqNji4jXU5lNtOAMyy4Y9mHdhnasa4kikVtAJZXC0305ZNlHbdq2DQ2NDSjPjWDh8gs4+tpRnM62IhwKozESIw91Ydf2Tdi4qc0or3lPmIahx6wlqne3Jj8evdxZ1gPea32Xw0vOUXB2wtW1dm37hV/4BaM/fvazn8W9995rZIdQy4vvKpaKWyci1YVzrrTUEqH6EUl4GL/MH+WKPknpfvUY85hGvmsvEmvXoT1eQqK8AIt5y5TDrOsgecwLfVml9UuLUt8YguFZomLWJxXfUn8xM77efaysA12rDlU/wje+8Q1jD6guP//5z+PTn/60kTHOixo9+67X4fsQKnfn6NVs1lIO5YUe9PZcRW++CeHOrdi5vg0NRcqrzDzG58fROzSAdDGI9s6N2NJRD1w9gVdeeQUX59PU09OoRJpR174Rm7dsxl13HYJfsic3iqDlo0rvxdzwBC6dO4fjYz1YWEghmKRVoU2r6tYhsX4XtlF+rd+sNYqA6f5RTI3NINbYia5NG1EXoc6u9eIDRcwGPCh4C4gkJ+EZ6kNfdx9ePZNEWp/yUtZm2X8G2ruwfv8d2Ld7I9b7BhnvWZzumcVUEsgVAihrRi7z3uLRzngFtLC/StQ1IJdl+yj7cOjQQTS0RJDOpI0x7PEVYOVSyI0O49zZc8g0bsbaNVvR3tyESFgbjbCvJ4uKM/U9jM2hmi3D9sgMaXanAeM1cFn4uhBPOvypti758PWvfx1PPfWUGRD91Kc+hQ996EPmXPdumkyoylWnLpcmeRjYRy3Zo/UZ7bv2UjwizfrK5SjLs1lcOXMOPZe6MT03jwLlcroUQia4C3v37sU9O4GOuhxmkyWcH8pjNr2IbXs6kUgkYE1ksTg0h8lsHpm2Rmzf1oW2wiSmxsdwqXcawWgTdmzdiqjFNsUknDj3OHWVPPyxrUg0rkdTXQD1bC+SrSXpBkyl1rX3VcveGNG3IJwXj6pztd3e3l584QtfQHNzMz74wQ/i4MGD5iWzM75kZNzyIIG5ruUX6W7CbT/o5cDEq5EeFnTe50XGpJkKPyYpBPMojBRQWChhqlTAhK+EUDSCjjUxBEIB8gyJJkyo7EeoasdUHA2kBu9kvpxyqy1/nf8og14Z5lqznxry3fDMz+HYmbP44cvH0TtVwv4Pfhp//2c/hLbckNmGtZCh4p3WEvYB5BJR1rUPdZZCyIMtHcMD/Th/eQCp2Hbs27sH69kXWN4c7y4iU0qbBXsD/hiVNyqtkQiPHviLSbOOgMVGXCrodTaVem+K6bTzVGaeCrRY0t46+Bmer+9JHH3+Cbx4icIhuhsH7r0TOw9sQaI+hIZyAWEqkj7yoXZFKrCOh6ONJsxWdkxBNnjTCKgQFDWVWtKAf1objHeW+PJm8KQLF+8XOHJJx/fyoFfJDFQxjZT4UnQ1/qX1vcyM0/II5dU8FhfSmJvNUamhYhNsRn19PVqpMEeDVMCDFop+KchajrraWTA0kZ1j+/xWgMnv7TzopU8UTL+oHZS0z1HArJ0VKoyhSCV2AY3sx8Lws3xCIT7nKSKCGXgrdsAVllkxp/do1A8CcbOA9EIqa1ThYNhDJZV9U34BSGUwE1pLRZV9WUA7J7MPLC0gWhhGZnISr83EEYsn0BKvQz3bSDTkQzCozxnKKAXqpbLAR8PTYh9mq3x2fTh4r/VdDi85R+F9Oei15K9KWr6BlJ9LopwvYCbRgnwkhpingIbKAnlPWpVWj/XZg158RINeZsdGwh30crESKvfqGXmBBnkhw/5qCvl8DlOeRmQDDUhQLjVJ+HizyHsyyBYLyJaD8FhRRHyUaXMDSM/PY6ZiIanB2AD17ro2tr846mJhciMQqkzDpzfe2p0xV0I6m8FYZhbz80mEUqx3bcBQ3wl/azufYz/op05OhT5QqCCXJt9bfliRgFl0O5JlgF4NetGu8OYRoYyMpuZpZxSQWWjEwPQYW0sW/ngEvpZmeBubEAn6sLbSj/RiEvPlBNtJDKVKwLwQ0LTq+kLatDYrFITXp93nyWe8pwEVLezrpd7vMetz5eEtpOBNJZEtFNn+ulheQQTItwGLJUizMC9/TEGA/bfNocyPaWvuoNdbgXjT4U+19ff0oBd/4gA7P9VBr+oLjYr54qiI7OwCFmepH6YzyBR9yFYisJo3o74hhBbfFNtaFjlPBHOFOpQp3AMhRkheiyxS4rNNpH1ezEZ9CFGPbM2NM9wyMoWgsZ0DPj/lP+1k2t+L+QGU+HzJRzvXFwebEbUUyla2twLLTynUUgi+qp5SVRpuObxTg14sRvyGTv7jb5jD2wqHkZ2EnDhxwijOSuj9999vC5wqahm6NqFvF1YWwEroXpFqrZYZ1rfYPiq3GgkNsCP2e0NUUusRqqtHpLEedc0NZvphIEQFxBOg4uqnIqyRkwzy1gwZNkeBbithtXgn8lWL1cJ3GGF2dhYvv3IMc+yEtm/ZiLsO7jLMXvBqdFifZ9gqv7pG7RahdScC5Sl4simMjs+gZ2QayYIX67fswqaN65EoTWNiqA8nj53BSy+fwIlTp3Gl+zKNvRlY0Qi8ITbochrZ6X6Ma4vi0HY0dzaguTiD+dFenDx7As+9/BJefullXDh1BtnFFCbQhmIggIiVRJThq6M9ejaJucUCogkaDuyAK6kFpMdHMDQ4ggvpBiTLAXh6n8ax576Pp8704OR0AdOL7NCnUmiLdqAlwA4sPYurPVfw/NFjOPLyazjO41hPP+bTVJADSiszq5UDmf8ADVVKDJWcKU9RbUNy4cLFjwdN0Z6YmDCfTMyzje/ZswddXV3wawSbcNrdrQit9WQ+c2P6tLNO2UPFlwqGdtGxKEEtb4T9WiNijW2ob2pBXVMIiYQP4UCI9/zsW6h0mPWjSkbBVy6ZW/OzYbvcKnD6D/XjMzMzGBwcxOTkpPm8b9++feZTEEc+3sr1thpkD0nO22/oVSd0YOev6jF2TYUGjC7orDUwih4pVx7qBCV4/RGUg0H2H/ZgU6RAo63I/OtTfI8+26GiTlXTa7EfDFIXYBlVaDFFwuzfqIWGWGR+hun1RXgSgxX2k0csBMlbNDfNQBrCdI+3IF7XhHbqHU11EUQjVG75vPlEgcaWr8S+mmdlJrgofmQKxYe1eC/ViQMnzc5RfCjoWgrwI488YvRHvSVfu3btkuyo5cWbg2q810SvC6VLpHOSOdhHY3sYmaBz1ir5xQqLb0LkEx95gsYMfx7yn5fGkrcouaPBLps3Vf8KuawBWoZj1qPTDFQNR9y0clDU18btyBLhwoULxh5QXd55553m0x7HsBV0vHl1+P6BU4bS6/VCWXKs4gvBE4wj6A8jSnkjSWVp0IfsIoMwQB4K+8l3FEE+ypVSIA7EmhCOhFFX34DGhjo0xoOIBWUjyb6zaDlZlD+0Jfi81tP2RWgXxetRX9+O5qYONDS1m90f62Ihyjmp2CUa45RdVgCBIInGup/8oXkoXot2iKegd/KUcOwn2W96rRgq/jj71QhiDRE0tLQYisXiCFFWRpnwIJ+GV5+dNyESSlDWSt5WEA37UE+5HKHfINuVXtb7Az6EeN9jKU4f8y95Kt7U54t+5NhfVyJR2iK0CSTjmUdb5tqtmKVo2p2e0Usvu83Zbdg0ShmRDlw2flOITyUf9EJNgxsayNDkmA0bNphz3btpMkFRLkWrOnZIcG7a/COOMNdGqPOa7csm8Rx1w3gdwg3NCDa2I9HcjHijj/xJfmI7KEsXIEXYPiPsz4LkoYCI4Vhsj1bIz7bCcBgytUmGGYSPfAryMqh/alkh6TF+H9uTwrJC7CO0ZE8FwTL1VJVdtfzslNrnzuFWQ22fr75hbm7OvHTV59fiC71w1Xmtfb6SP2qvf+s3f9Mca1qmC1Ma0hMo6MUoEsBWJUBhRmHqp0CPhBCIRRCnMAzyulAm45El/QUyYoFsVNY2vBlDK3FTGusKKAVGhxcvVU+Mul9Nm7nPPKsYlmY8slMrUskqFNgRldl4/DQRaAvMTY7j3LGjOEPFRUJqeHgQF0+dxisvHsGZS5cxuZCmcZtFdmEK46NDGBifx5w2lUjNYGqkH71Xu9Hb14vRkVFcvXQRrx15Hk88fwKXBxeQzhZRzs5hcqgHTz37Co4ev4D5VNbscJFOzmK8rwdnjx/HK2d7cXVsEYs0nFNzk5hNzmAsOY/+sQmmaRzFNA2V+TkMXj6H48cYzqlT6O7vx8wQ03r8BF54+TiOn+vB0NQ0MuU0M09jpqQ3qBJStoC9FerNhQsXtwbMHC1anOWS3vdRhsoooILuodIBjwY82AlTOQ+GqNywn4hFtFakZjBI3po/W76a0FzcfKgzdMiuHyPxl53owNoyxHrXtVYwpuqpT121iLhcfQXqmHlpDVQ0y0FDOq/QAqzImuTj6lPFBhY7UEtKPPWKUiVCxTTOoEu8LsBfKiGkRWr500f+GX8CDQkae6EAfBrUKOeoAGojGKrY+rw2X6S+y0D5p3mD9KEUuripcLjoeiRUz6Vf1JDWWNKGQ3ne00yuIOtWb/DL4pUyDRjVO5+0Nx2S/kZ9jVUusq9ECps8V2t4u7htIR1W9mOBenvFSz7yhlGo6BNZDyKURZRWxmg2XzpoEKtUpnwq0rLJwcdj3oqhFErAH6JBHpMsshD15mmUa9mQguHHfFm+Qyj4GL5FLqSIDAQj7AMTsKINCCbqEQ4HESLPWsWSealu+Fjp44nFa0tdqFkXmDxM2aoBL02L8OnME0XFH6XYLSFWF0K0jv1rNGoGvMIMJESer0ALeUfon7JSvG+mX2cZNtPoY8+tNkLjWesslShrS2xlXsalAQBN+zUvtPh02RdEzh9G1lIbysFiXuVPaWUEmhhmZsos/5huc1NnLm5HOANeZoCLPKRBLltSi4fIm7QppQd4LfJmKApfrA6heAyWP0e/7NN9ARR95HFvUJoF/Lki/PmSvvJlP0++kgrBNqF5uz6zg1vIfLqrL/T04lW7iGp2mGYKewrk9SJDYZzSV8rSNaQjVHsGZya6geHb2wuqldsCNzJ4UdH3rlQkKdIo+MmyFJwVSme9RXWmNErB1S6CegusDkIDYyZo8SWZOkBF1WI3UotbaeBEFW6nRj2MnSs1DDOoSpLwtpsK8yjQc5nlUCyyLHjPz8ZXKuQwfOk8Lhx7FXOpHFo278DO/Xuxob6C9NBZvHK2B72zaWTYy2aSSYwNDWJ0uB+pxQIy2RxypSKisRh2btmK++66C9s3bUL/lSt45oXXcLl31vgrpecxPzaMs+cu42rvENLZAgrssHKZNGbGRnC1+xIu9g9hJlNAkJ1pU0OC1IamxnVob1uPdWv1hsmH9OwYzpw8ijOXB5C02tC14w48cHgDWqxZDPT24NTpbvQNTiHD/OnTTnWEWi/g7awyjVg7o9Yu3hhuWbm4tUH+NIMMmsJuD3iUSpKYlKw0KCo0WLXzrHbx1U61GtiwtGsOlSFt+CjNW4MXelNsS+Jbp2+4nbCqhJHcWbrBE1ljqp+qs0g9o9FAWd/a+djMTlCnqR1/vdRQeVoif0gvNWMOVFT1maTFevfTEKTKwHtUTo2Sqq+B9Fm9YtHbbMWlPrnEAw2tSpr2X4pR2R9gyh5kF0h+03IUPLKTsrck14sqDaSJr+wUurj5kLZo07UwbCYy92we07kzuKq1RUvlIklGjB4QG5EvVOkyoKhnGh4hX2nNGMdT1av9b+nCxe2E6+tPdKPcse0X8pOEieQQ+yLNWC6SD4tl9mjkr7L6MQ+NZvZdFbpVKjn4PXlYNNg9msbFexqSktHtpR+977HIj172d4qB5rp9z/Bv3ujtBUYqWaV0aEaUPgiUHeUrU86RNGSv+xrItflWslBtwzL2h2ScT58XyiYj/ysmDVtJIltsG5r9aOedz2mQQH+M11sswqIwLvr1MSJlJv15dELhW1De6LGkXfu1hrApBcbD+L2859Ugs9qnZC7v6qPhAsOVhGVs/K80iuQim1BHO8wi0ysyWXHxPoFTmytrlTxAOM1uabKE0R9kN2vgS0cS+Uqy3CoX2AbYUkw78cHH9ujTbCy2If2oVRoeK5OXTR/v1Sxeu+1W9MJVUTIOw4tqJ+oXGKbpD5Q+3tMaY3o9pwFm86BJt0IVNysg2+V2g2rltofTUeSoMlK8k6loqBTIiAUyKSWgppGrYxDDaPtpi51AmD4TvhLMd91aTIF2jc/SYvYxBCoxO2DiVhrwkjBXByXBbp9QuWLyTDMR99PJHsgrMJ85udIPWcQbIcXg03fD7PwyySmMnD2OqUtnUYo0ovHwQ9h19x348PoCtuQu4Ej3Ak7PWJhl+ZWyaWTnpvnMBCr5NAoBP6JtbdixYycevOtuPHTvB3Dnnj1IT0/i7JVJDEzlzHoAvsIs/NkFLKR9SOeD0JphJUvvvwvwpedMmOOFAHLRBjS0NmLDunasW7MNnR13YueuD+Cuu7ajrSWNmaledF86gYEFL7JrP46Wwz+Jj+3x4d7mEbPjY0//FIZHmad8I7IevalKomxp1hcFzC1Udy5cuLgFQEEpkeij7PQhRVlKZbkcpqFKRV+fL/J+oZJF3sqgYGURKEdg5SJ08yFL3adonstRzkrJltB18W5DpW5sleq5c2Z0wyqZ/zqRbmB+pnukHkBHvz5DCFFhLSNERdXvpbIZyqIUyPAR+pSiyrqWkaRPznyeLOs7ZWwi8Y4+qTEbpoj8VG796pu1nk0Y3mAAlSD7YF8Kico8EliA5o3nffoUKIyAxX6Y8ZesIHJMSynMfpFKsY89pDZ/CZrZDS7ebRgOImsskbQs1o99rJ4v3dd59ZocowFz1WD1FarRzfwhL/x+r1lmQzNy/NRJ/eQReyBAlKffFI/2sgwiDTiIHF2OHly4MNBniyFLr3Xz8FNEhEp+s8ZNmW55yqG8eI9yJU8bphBgf+aN0jSO0/4JI+ib43PzNK41M5UWD+8V/XVmhqqvFDb7UcU8GUR8aXKfRXuikccEbagsQtq0KuRBhjZSXjNRjPyzzMwsXznLtCzCyicZLvtMv9YoZGI1WKWBt3KAp5SHbANlq8R4ed+K8DrEvrSAjGbIlGgZ5PO0CTR45jWDciX5p/wNsN3EsxUEMtTv6Z4JBplnrb2sDyFDbEZmpSOGOQuvf57PUk4zbl/Rw/KxEGHezKyYYomtrIKsxVZH2Z2XTWjaMTNjBhw04JU3Rw1wlDw+pq1syAziuXgfwEh4kgTrSlRlLsmMe5pzMYgGuzTjS9weMksZeANRsz5crJwy/XW8EkO0FEOoUCJlqQfkyWdZFCJe5CMBtkWLPKfZlpT37Bc0bhxkY9YLs4reomkQWl+jkY/9bA9e07ipUPj9CJA/tQKkWWhJ04Y1wE2tpEIbXjPCBKbytgOLzoUD8aqBOEFUddB4v7b59egjczMItFxsBX1qIMEmHi9R8Sho8Vv+sUN5zw+aKP3Kl1oySUctbKz1wcbHJzA1PcXzOYyMTOHK1RHMTE+zkypjoH8AExNpZNnhaLHdAjulIjsOTf3Uos4bN27Emq41DK+CwYEBjI2OIpPJoMSGr+LTSyhBYWn9H0kUTUl2Bic1XVNvQT3s3FQlHhoKwXDYfN+r8NetXYvNm9cbv2PjYxgaGjTr0aRSGYyNzGDy/Dlk0mnGlWc+xjE8PImFRcZtssx6s6NfgsL5cfC+4IV3CW5ZubilId40Rqzel0lx0JoflFnSe0lm+jodNExir7BEN96XnFJ/IlEi7vZp8xAXty5UoVWoR3B6BfNf/9ivaZ0Xy2cZ3UB9RIkdl2SXDEyxiXqNspTfqjzTLsRSHbQLn6D+1EfzK1/t8LQOdLlcMWGorzTMwgd0Wz6WeiHxEQ9FGYc86o2ukZmGjA8XtzKWKnJ1aGVZe5iV9U42FF8YUSPQ2bDTUj3LH8n+c+FiVYifzAxCyTXDP5IVValGxpEzxYksHbrpyw6b73z0IxmltY41g9V45kM6lX/eNG/Nc9SlNQNa/gWKOiO7BJnaZt6KopSb5KW5LWFY7Rx5T2k0unZV9jp9pWZbKexcMWsmcZlnTUppmXn0rMLkDT4X8Ft8zmN2ny+rjw0GbSKMDNXDyhfva8mBAp9ROIpHG4+Yz8P4mJJG0W5D6ZH9Y35Kk2bR2Hlz4UKosr3hL7ULsgv/VUngfdnCsmlNuxODVf2afeTEv6Y9irfoQJQYmBOM3VI9xr+ai2mKhDbWsXx8Rs8zoIoMaD7n6CMlTTl3YBJlh2WHd3vitm+5tQMaMYrmOClAiVgJkkJ6bxY2ZC9ArCmG9OjxUzDq21sforRovBaZzKJgDFhmgcgKaPRUGe+N6F2HJ8MaT/KEUr/YRKpHmg1Nb5KLZY02ZWm4aacqfeUfoeMs7yRZFiFU/HVmCrGVHUBgvge9Ux7MljoxPpfF2XPH8fyrJ/DKWAjjwe24b2sLDjR70KhvIX0J+GMJxINzCHmn4En2Y/zk0/j6I9/A/++v/w5f+d6zOHPiMrKLJTSE5lgH4+xisyj7tUBfGG28kglZLoewUPTCU1xAu3cMneEUUhUf8vpkJO5HMRFAxO9BczEHb34BhXAaI6E0Mhl2gOkgfBqAm57A5dNn8XunC/hhbiOijQHs2xbD7i4/unwZNBUpVEoJ5jlOogC5WfXkwoWLWw4aWNBnaRWvBvD1triJUqKexxJClP/eAPsHfxk+r0XpGeOPskQzaukW8pSRIEWMsqx3b1qtxEw+NyRF3SZeunhHIQVVtaCFDPw8s3e40yeo7L91w8M6DtDQkhKpjV54L8C+po6VkyDZGxiwr9DMm1KEfaZ2HQ3BH+R5uWg+89EMsAiPAdZpuaJdiWMIhskLWn+DYfnIAwH+tINnnDwi3cJH/tGmCOYNsSdBnaKD7q1o4r16GmN+3aNfbZqg1WsSTKs+NLIH2cRP6rfsHVBdvLsQTxnVsIbEWRqQ1PEad9aXsVGMH7V+GfBmOW2eBRFFIzmjDgHqmVqj2AqQ56iLljTbxbI/f/GVwwiWGuCvkE9kNdES0uLGkko+MYS9SoeL2wz2gLm4bAUq5ELKKK8nDC3XUvZLjpFJzJcpEUQp03gHwQqtmjI5UbNHtXFU2QNfpYH32swMFQ1X+SiLAsZOKpqZYqVQAX5/nOwWMQtvR41MY19m1dN3nDLTiwbKQfV6Zh1EmfIV8XqU55RktBEsD9NAtzAZt+LXxh8B+KjPy8AXG2vRmIQvwjxUKF8riFH2xkl+HyVgJGCoEtCMF/ql/I4x/VoAv8Swy744IrRrYiRvkLI7QbuOsjjEcOL0Y1VamJ4Wiv86RsYegc8GSIq34m9EJdyKKO29eoaeIGmjEXsRe0LdtwbuLKbZfP5ppzfOGyLN83HxfoDq0ZbWdu07JOlOqM8l32k9cLMLKEkvRpeIAt/rDE5Rz4AvxiP5mTLdfGLsJx9bIbZdLZAkfcPLllExM7dD5HOLbVcbJvg8Beob+jRS642TT0lhUpA6g9oa/A1s35aaO7QknXZuNIPGXrY1T5T8GDGkmZRMvk23GVSLtzVqOwh7/PNt+lU7nzeim4NahdhOg+2i/2ycPOjFhtqm6XHoViqxY6OjZlhpIUilPRKREh/BunXrcODAAdxx5534wL334aMf+zj+3s/8DHZt7UCUeng+l0MqlWa4Wgw/hyunT+HZJ5/AyROnoLfaO3buMjv3tLa0Mi75KZgRaqMskjQDTG+EtPVwgEJBMyQ0S2t+fo4drT4n4mP5vEmjEKBbJBwyi94rf4pDaY/FYti8aRMOHjyEe++/H/fd/6DZEvcTn/g49u3dg7oEhQGFUsDvM2/Qa0vJhQsXLgSJRUrv6s+YtUtXzs/F+xem/qv9t5lhxY7Sub6Grud+HVodDrfZcDnrdsFyTRvWqF5eyy8uN7h4ZyCJ83peW8lvyxqy8b/CDy0F/l++Xvn0Muw7djzXx3JaroXjXntvNX8rUfvc8g5714ZjQ9d0Nz8XLlbHtfy0OqlFqF3U/uw/+2hwHSZjCM6JfeCxNuxlLLtd6+7CwW0/6HV7QStG2MQWYRqQPXatS/43b7q98JvRYTn6USpbZkqlnjGfclhhRBMJBCNBhKNBtLbWY9vmLuzbtw27DhzAvg98AIf3bEJjXZhhWSh5NH05YHZZySwuoq9vBEMjM/D6Qti+dQc+cPdd2LK9jeHlUckE4S/WwbLqUArHkQuHUClMoTQzACxOAakFTC8s4tLsInqmU/DnwgjkmTZvGWab43IGpew8yvkUilmtAuZHIBxDrL4JjQ0JdDaFsXV9Mw7sO4R9ew/ijkO7sI9pbe9sRMXyIFewd6LRQL0DV3C4cOFiGW8uD6humP8u3u9QTbOeq9XtnNv1vwzb1xv/XLhYDStn7dUaNK5u4uLdgMNnSzy3Qj+upSVcy7bXhR655jnija6deBx6I6z045zfyHO1eDP/LlzcMNQuaul6qLIcOfiac/Mz/Ojy5I8Kd9DrtgNbWk17MYM8JNO4dMYGZW6rQWqXlorPrMeltbXy+YJZX6SuoRGt7W0IR0OYnZnE6Eg/FuZnMDs/j8npaUxPTSKXLZjv6gv0XyxVUCoUUcwpDH1H70GxUDF+UqkU5hfGMTM3gnyqAm9B0zg11TMAj9nyH5gc6MalM8dw+tgrOHHmLM4PjGBiMYtSmsnUOq5+H0JMi3avGBnqw6kTr+H82XNIpVNI1Degua2DHksYHbqKsWGmdWER0zOzmBifxPzsHHL5nPlcxWSbSqZ5g6/su52dCxcuXLh4CzBvbt8C3M8RXayGWr64ni7i6igu3m6Ip2ppVRgz4vX3VnN7Y1zr/434ebV7b+T/engjeat7rjx28Y7gOmxl2swSG+vkWp6+9r6NWh51+fWtwR30uq2gWV720V6brHbQSwNe1Su1oTLJF4THCpmtigMBPwL+ALxeP+J19dixa6cZ+Orv78HzzzyFIy88j+dfOILnnnoax4+fxsLcIhujD14+HwhGELB8iIXDaO3oQkNzO3L5Ii5fvIwjR17GiXPdSGbLaE54UR/O258Ze+NI1Ldj0+Y1WEhO4sWXnsHTTz+F46cuYHqhgli8DfXBFILlLDz+esQaNyAcrcPM5AhefP5pHHnuBUxNTaG5rR0bt2xj/so4e+IVHHn2cTz/3IukI3j22Zdw4sQFjI/NmpLxaRHMUtF82vmjdKYuXLhw4eK9D8n/G+4D1F+SjPJZPbevHbINqeuRQbU/fkP6EeD2Y+89XMMXNXB4spZcuLgRrMY7q5GDlde1eN09nZtr24137dMboRvE9dIirJbW2uvV7tfK31paiZXPuXDx44M8Jb4yvGXzl91mzP8q6drcMnDu16KWZ2t5uNa9Fi4v29Aoh4sliCneLrr1YH/aqMX52SiqydSCeFrz1KvFULUovxZPpbs+8fMgAl+kCW1r1mHvnt3Yv38/OtdsRChWj+379uDAXYfRUB/BzHgvrlw6jbPdV9E7MoZCahZBFBCKxNCydgv2HLgTB3Zsx5a1a/jc3dh9+AFs2LgDfq+FiYlZTOfC2HHnR/GzP7EZd22toDERBULb0dC2B/c+sAubtjViITWC+fkZeAKt6Nz6Mdz9wM/hgzsK2JqYQyC0HonO+7Fp+yFsXluPUCWFxclZ5OfzaFu7GQc/8CB27dyMaGUaE72ncfF8N4b6RzE1NoaFuRlkclnkyxUt749KSbtFmjOSDVdYuHDhYhlV4fmGtBI34sfFrQbHYHLoGpjLqrtDtXVbPSy7XZ9u5HdjoM9qWl+XXhfvKdTW40qqxcprFy5+VLwZL117v8qPzs/c0r8atzf76fkaejtRG+bK8Fder8Sb3Xfh4q3C4SlDq/C/vjDiSdU3T/mzr20yv6rflXgz99Xu3a7QSk7Gui+uMjL4o6B2hFEFXSwWYVnazwL4yle+gkcffRRbt27Fr//6r6Ours646xmnYpzzdxt2vNWLtwXvbh6ccqstf51rEXefz4eenh783u/9Fwz09+CTn/gp/Mtf+jWzVeqitwItxRyslOGj/4rHa4bFtGVx0DNkhkULxQaks34ec4gnLPgtPpNPAdkMri7kMJIpwV8qoIlu0WgUpZaNCEUiiHsLCOQWzWeMmXAjoqGAufbk8xjic2OpAvyeCjrCXgSDAczlIojGSFHA7y/DWyal85icmMBUaQ7BcBD1PoWbAML1GI5qpyKgHcPwFzNIzscxORvFTG4B+UgGnWsa0OllnMUyZlNlTKRLyOcyKKdHEGH6ApEuhKJxBCM+bdqiEkOMeYTXy3KwWJ7umLALF28HHLmkYzKZxNmzZ/HMM8+gv78fn/nMZ3DPPfcgHLZ3nnP6glsTN9ZPUpKu6AFWy8+yW63cvlXy7vQf6r/Vj3d3d+PFF1/E+fPn0dLSgs997nPo6Ogw/cutX283DicvbwTbT/XCQPV37TPiAYGlYo5vjBvjqzeH4rqR+G5dOOVfWw/a6t251pIIv/ALv2D0x89+9rO49957jewQannRxc3DyjrQtepQ9SN84xvfMPaA6vLzn/88Pv3pTxsZo02LBD3r1uGtCVuusX7tS8I5W5Zhr5eG18Pbp2Ov1u7l5sDlp1sLqhunflQ3kg9f//rX8dRTTyEUCpmNxj70oQ+Zc91778uEZV68cVzbpgx4cjvYpqpzQXWuDe56e3vxhS98Ac3NzfjgBz+IgwcPoqmpaWl8Sbzk9B/CSnlgVc9vG6u+VvitBrtw3k669eCkSiVR5kWZtR+o5BCAVoPXtbY9pWApleFHjhpkHTkkYXZJjEcDqK+LweMLIVukQqoF6sMJdHV04sDmjdizdSs27NiPjvU70BaPIk7dxtLnjYEEQnXNqAtZjIehF8mg/jha21qxa0sXtm1ei3hnF6JNrVjbEkVTjHFbBWQrGSRLKbPvanPXRmzZfABr1+xConkNvHUReMNFtHvzaEMRpXwLStiIWH0rNqyNYu/GVmxlmE2BBvi8UeYjhPpEEFvXhLFrUwN279yDdeu2o7O1DvVRppHlkGWhGA6RTuZRY3tjfnHhwsXtCEe+vxERZiqtuleHVvoRuXiv4vX6wuvr2Nndc6X76lTLKz8OKSwXLly4eGcgyWbLtVqZc60Mu/b+G9E7C8forTV+Xbi4OXDayVuh5bbi6BPuZIwfD27p3fZYHtxxzrxeNi2NBLGjKJf1hq76zprX6jz8Pr/didBdzdDy+gzJzePzolQu2k3WNE4PKvRXKhQUgl7FLoWjNcTKJgSN5Oq//faozJ9OFA8sC55Sib7ssPS818/4mT7513+fT7OyGD8NTa3H5bd8CAcCvMOfxq8Yj7aQ92o2G9OikWGR0qBsWiS/IhZ4nxk2z7pw4cLFW4crO2431L61FpzrN3vZ5sKFCxfvZdzqcs7YGi5c3GTciE5wK7ej9ws0knBbwBV8AsvAzEDQcJENrd3lrV7pP5sk/2vQSat/Beg9aH/qR9cl0kexCPHBEM81HKWhK8LnN2cWPVkMR0WuzyU1suRjRB6tlaVBL15rcMrnKdFvEX6QfEVU6Fj0+qAhLjP8ZQbNSvRPFwoDn5JG5yLDKtGv0lWpMGxGpNTyDv0W+VgJfrpp0iNv22nw8GFPgaT1usxwmElzLTFo+5/LKy5cuPgx8Fb7G/l3yMXNxY9SByvrzrn+UcJy4cKFi/cKbhU558paF7cynHbyRnzq8vA7D9n6Lm4XVAe8DFXblj27anm4S7T838dHAmyIXhKZpfqM/bCfB82m8pGJ7AEurRCn0PTtbHXYygw4qSHbSzloAIuuZjBLzFeGz2OT5SubQS8NmpXpfylFlbLhUo1ZOcxaYhAiKH2MxUStKV01JL8mSiXMJE4hMn7dl7NIt6rnr8Oqji5cuHDhwoULFy5cuHDhwoWL9wrcQa/bCPZQljOaYw9KmevqYJj57/yzT2w/ziUhhlliGjoarzX+DJaeX3a6Bua2Pk1UGuxU2Y72wavZW7BI+hSS981AVonJLBmfmltmPms05wSfqThxVsOoHmyYEzkqPD2xdGfJ31K+atLuwoULFy5cuHDhwoULFy5cuHjvYmn8wsXtAA0z2UNF9h6NgKei4SPR8gDQ8sCPPRRkhrSqTtcMDvHMHnzSABadquNX9iCY8zOP2nAu6FkzszzQ2l8a0NKDTJGZBaZPI/0IVsKkAODjfV8RZV8WFU/exGNVLEPacFGfUmrAq6JZZub5CsNmehikPoe0g9Q/DXhZVZIfudukzyAZkyH7hlxduHDhwoULFy5cuHDhwoULF+9lmPELFy6W4QwFvcnAzypelseLnJsrPNwoFI59qMGNhKUHbTLpcB6pPXfhwoULFy5cuHDhwoULFy5c3BZwB71uI5g1uip+s/i7vfB72b6GZRjBZ2Zelcx/keaEiZbHi/hMpWTT0kCSPWPLq+XnNbOKJBeR5m/ZkEfNyxLxnDc0ucueQ6Yngyh59DFjjj5I5SJ8+pKxwtgrcZQ9cRQQRh4Bnus5xlcpAIW8oVylgiy95xhakXkpm1TXJJHQovxFxBhXhFdKAJ+tplBp9jM+xcmYDTkff7pw4cKFCxcuXLhw4cKFCxcu3ptwB71cED/GAM/bPjZkD0QZmNPaoasa6J5DNada/N45vh7XCasK+2NMFy5cuHDhwoULFy5cuHDhwsX7Ae6g120FL7Sbohne0a6IlUrNTonVWVw8OgNIum92T3RcnGuScfHIVfcdkqv93z4jqh7NroyK33EzA0ya6+WFl4+KyiiZeWYlTwUVO5kmWE9R63iVzRwuPVzkfflxdmr0aZaZuSfvmjmmPPF+Na0ipZjBGFqZXnOQNx6dWWouXLhw4cKFCxcuXLhw4cKFi/c23EGv2wj2Xoka+HIGdTQ0VP0MUYND0OeOzkwp47gK2YNIFQ1M8WrJzdCyi6HqiX1QPKTqtRkxE/vxaMavjLsGpxS2SJ4IBquxLX1wKJIvDc2VzH372nxaaeKXd3twzbnnkPLlpHI5vVXUeF1Kp7nhwoULFy5cuHDhwoULFy5cuHivwh30eh/CszSotRIazinzoCEd+fFUdzfUqVjBXmXLvuNg+UxPG5bRQvFL7npO+x9WV/9i0EtP6ESjWdUnjXv1ptlxkRdmAK56U6uI2VRly6q7IfPPWQXMzA+jk5MWc3UNLT9ok8pk+V71zIRL1HitOXXhwsXbjOvLJhtvdt/FzYXqx6FauPXm4mbC5b9bD3rR+Faxmmxx4cLF+x9vJC9cmeDiR+lPVoM9BvAOQszqJNbt0N45OOX6RuXr9ejDvwLPSih7NG/KC4scYA98WfwX5PP+pSXn7UGl6gARycNn4OUdb8AMCsnVgyD/R0lhXtCVjhr+0jCYwtU/D2kpFP5TMB6GqzjNcvnVmxbD8DMsH//bz5KW1r/306/f3PPTp+VhDBbjtkLwmTRbTInXpCZA8ulhJ/0kxRSiO3PI/zoj6Z7iUIIZh4IM0EHEVNPRhQsXbwcc2e/Qangj2eXi5sArgV3FyjqsVUIcNxcufly8GR/pvsOXtbqlA5cPbx5uxDB5Mz+qP7cOXbi4vVArF3ReKwec443IFxfvD9TWuc7L5bI5Ojzg3H+rWNZo3yYoIQ4JSqgSWUu1WOnfObr48VBbrg6tLH+dq34cKpVKKBbtVa9cuHDh4q1iNXlfK2ckY3RcCcknFzcfq9WX4PQNTv3V1m2t/1o3Fy7eCmp5qfa6lgSHDx03h/dqedDFzYEjxx2dczU491a779SnW4cuXLy/sVIG1LZ9h1yZfnvievUtftELL9Fq/ceN4G0f9HLgJNphbIdWJtZhbsf/9TLr4o1xI+XmlP/1yOfzwbI0R8uFCxcu3jokR2rlvUO1MkbXtVh57eLmYWV9iQSn7pw+wqFafyLnebdOXbxV1PKesJKfREIt/4nEk///9s7ldcdujePrbW9nQnIohAFlgJRzIjGRQxmIqSQj/8LubU+NTRgYKpEkIxMmJgbKRMgxRSQ5n97B3p+1fd+uvdzP+fDz3L/vp749616Hx/2s67qva93ruX+P0gfN2BLX9KBjiRvZcgPdGDN+KK/7uLaoiukxB5h6U9pZvoJ6zRl93/TSSYnSUXWyUaKqzepd0Um02JA4VrtQX8uyrF6lGBNjjVTGm0ist8ZOpS2wYZk/qmxrWd2qyudK/+JYPljWx2NruCptV0rE+wLdJyBucqFqrGVZo61I2RZjeiOVY6z6CWJOiFJ+oNwNfd/0gngy+gBAWY4bP4T6l3VW+9L8xdeS2L9RH2xU9rMsy+pUIpahqk8VsZ81HJVU1bVCY+L7WlYrNaNRn3KRHNEYa7gq5748jvVCdkTcH0DVGMuyRlNVVLXHmC5iexxj1VPaJ0KlL4hG9a3o+6ZXPHE5rxTby7ao+GGtzlXOXSOwQySOsSzL6kVCZcX+iPrGmKX43440xuqfhGylurJdxPqqsmW1I6GyXmPMoFw1BhRfYrs1XFXFZCjLIHsJ1QPlMtZXSe9rWdboSsQyEB/inzdCOdaqn2Tn+Apln24YyJNeEZ2cnFeKJ98oeTmpdadG8wZ6LSn7WpZl9aqqWFSF2ujfSdx3juivoi2q6kS8WRVlX8vqVfKnSNUxUiyIddbw1G4sFvGeQDe1ElSNtSxrtNVsjQcxBlRRNc6ql7B/zAv9ZCCbXjpx0ImD6nhVsovSBy3rrNaK8xd/BFA/CjhhwoRffiSQ/rKHiO9pWZbViUTMARDbFI/QxIkTs6p+uDQeN1P8963eFJENEW3MNXaKtqoaF1G7ZbUSxJhBOW5kAWX8TrFDvkh97Ff1/tZgFeNBeUwZW1EubQUc81s+8X/mZEwr6f0ty/q9VXXtxjIiRug+FVEXN8lAfa36ClvL7lFCPtMNf/zjv/mGwl9FEuoWOaaSFgkMR+b49OnT6fLly2np0qXpxIkTadasWblefTXOdI7mUPMph6DMAvHJkyfpzJkz6dmzZ2nXrl3pyJEjvyww5GzGGNNPFI94/fz5c7p79266fv16evr0aTp8+HDasGFDmjRpUo5JSm7dJjXTO8oF2IL8gV0ePXqUbt26le7du5dmz56dDh06lObPn/9/eSeONaYTdL3jO5RZm+Bb8i9gLfnly5d07NixNHPmzHTw4MG0bt26HDvwVdrN2CHb6TXaFPtwIztlypR8H3D27Nn08ePHdPz48XTgwIFsV2xtjKkXigkRjhUndP956dKldOPGjTR58uS0e/futHnz5r9juuJJ+T6mfkQ7q/z48eN06tSpNG/evLRz5860fv36NGfOnJxTgD4xf8i3xD9/lvu+6QX8YyQ4OSliAUOSO3fuXP6G7ujRo3kxLYeOHxDKEzbN0fwB88YxNyrMNQHkxYsX6cKFC/l148aNad++fbkdxXn2vBtjuiXGIYixRGVubkhgt2/fTm/evElbt25Na9euzTdD379/z6JvO3HIsWpwaPOR/IFN+MKEzcrnz5+nGTNmpG3btqVFixblfki2p0xu13hj2qFcw7CA1ZdyHLOWYYH76dOndPLkyexjO3bsSKtWrcqbXvgor8QXPSVghotsqLnnWHWs9bEhcf7atWvp6tWr6du3b2nv3r35i1jsit1iLGmG7WvMaMC1qmu6vLa14YX4IpR1IbGd+1TF9hgTfN3XH3IFNkeU8RHuGc6fP59WrFiR9uzZkzZt2pTmzp37c8T/aOYbA930Ap0wkMhw2CtXrqSLFy+mV69epTVr1uQPg2grHZpjO3dnlHPIhhbzyyLj7du3+Yblw4cPafHixWnlypW5nUUHDqUdUs+7MaZbFIMiMZ5Q/vHjR45HL1++TF+/fs0bJwsWLMh5Ij55qvzRDMeqwYANNP/awHr//n16/fp1evfuXbbV8uXL8+YXeSTmDY4ZU+ULxjQDn9H1jz9pHUkZn2M9w6YWTxzSZ8mSJfmbX+qJHbzKbx0bho+uec297ImwDTZk4+vBgwfp/v37uZ616LJly/JTX/SJY1thGxszOigWgK5d3Xty7T98+DA/mEGc4D6VJ3loVz5oJyaY0QdbK4/jCxzjF3fu3Mlftu7fvz+tXr06TZs2LfcRzfLBwDa9olNy0hwrkXHCN2/ezDt2JD45c7wQTHdEJ1GA4OYD2Clnc4vFIn2Y+6lTp+Y26rFPtEMzxzHGmG5QXCHGEJsQ8YikhohBQL8Yz8zwiflYdsMebFhqY3L69Om5nmP6yH7afIjvYUwr8CF8Rn4T1yRI6xr8i81y6ljLsMGqeuBYZTP2yH7YSGtN1qLYEFiLYjNiC8jOxph6QRyI6DpXbOBpT57Ypcx9q9o5hnK8qSfYnfUmr9wbAF+28sXr9u3b05YtW/KmqPxCyF+qGPimF/+4kh1JjA/ASbNbh9hsoU/sZ7qnnG+OmXMWf7qhlLjZZP71Zyuqpz/jGWuMMf2ijCnEGyUsbnaU4NTP+WDs0NxjC+ykvMIxNuOVY2ymL1ZK22mcMe0i/9E6JN7oRF+iXk8fxs0tytSpzQwfxQaVobSf1pv6Bp81KDkAu2JD2jTWGFN/uN6RYgOU6wvFdMeG+oMPyN5aB7BnQR1PBi9cuDB/WVL6QjPfGNqml04C51UdCS62AcdxrOkNzSGLCMosMDTnOA4OxJ89qh00/8YY00+axfQy7isXNBtjhgOLD2wRF5xalGpBqmOQ3ZDsakw7yGfkN/K1WAesZVi3UEefCHX4avRJMxxki2g/oTpeZVPdzOhLD57s0H2CMaa+lLFCEBtoo56YQBlRjsem3sgHVAbsT37gLwyUQ6IvtPKLgf+mFyfEwkSPpnHCOsmqBYk+ILQ6efMr0QE0lzpWsBCxrHHlGGOMGRTEG8UexRzFIHAcGnuqckK0G3lFN66gNm84mEEjHwT8EOR3flro90V2U6ygbDsZY2JMV3zQ5oZjxfhCexYI2wNlngrmSW7VdbLWHNqTXnFhzC4ddXrqSIuV6MjUlx/WtIa50kKPeUUcM/f6rQTa4mKQevWhv97D826MGTSK86D4ozrUThxyrBoM0S6lTWQnvUKsJ4fEJ4iNaYfSX+RTgnZEXVyzqI0ydawveTVjS7SNbEud7Kd24gXw1wfc0ABtGtMMvYcxZjSIsSCiuEA78VtrCPVvNM7UD+yPL4D8gLzOHpJ8pFMGtumlxYYSGRsrnCwnKWetct6yrpsPNZ4pAwHHzCGSTdQH21Af5zqO99wbY3qhjEeiWdyBst0MF+UK5l62aGQnoL/6SKA6Y3qhkd+B/hROa036UseP25vhI1vFGCCi3RQbYuxQPbZUXRxjjKkfMUYIrnvqyzigvo4L9Ue2V47QBhjluEZV7m+HgT7pJefkhPSoeYR2JTeITqzx1Nm5OyPOdbs2wIHKefa8G2N6QfEnUsYVxXkRx1Bf9R4ljlX9RXMu22h+OY51Kqs/xL6gY2PaJfoTlD5UtovSH8v1jhkOsoOQPWJsiHbqldI/jDGjQRkbINaprJgBvt7HB2V+wO7sVZDXY1sn/jDQ3/QqHbd8VVsVrdpNY7SBVc6z5j7Srj2MMcaML8q8oGNolSuq8o0xg6LKV+1/vzeNbFTa0hgzfqi6/h0Txh+N/KAXHxj4D9kbY4wxxhhjjDHGGDNsftn0+teff+YKY4wxxhhjjDHGGGNGlX//3OP6e9PLGGOMMcYYY4wxxph6kNJ/AJKV+k2xE0IAAAAAAElFTkSuQmCC)

__Campo de preenchimento obrigatório\.__

OS4293/

OS4677/

MFS\-2346

MFS\-8380

MFS\-14872

MFS\-21816

MFS\-33041

MFS\-42862

MFS\-76524

MFS\-97809

MFS\-594253

__MFS\-713686__

## <a id="_Toc49801945"></a><a id="_Toc49802224"></a><a id="_Toc49802427"></a><a id="_Toc49802537"></a><a id="_Toc49803302"></a><a id="_Toc49803545"></a><a id="_Toc49805175"></a><a id="_Toc49805293"></a><a id="_Toc49805405"></a><a id="_Toc50402982"></a><a id="_Toc50403106"></a><a id="_Toc50404645"></a><a id="_Toc155171976"></a>3\.2 – RESPO – Responsável pelo preenchimento

<a id="_Toc49779723"></a>RN09

__Registro RESPO__

Gravar no__ campo 1 – Identificador do Registro__ o valor fixo “__RESPO__”\.

OS3528

<a id="_Toc49779724"></a>RN10

__Registro RESPO__

Gravar no__ campo 2 – CPF__ a informação que estiver contida no campo NUM\_CPF da tabela RESP\_INFORMACAO de acordo com o Representante Legal da Empresa informado no campo “Responsável Legal” dos seguintes menus:

- Caso o Ano\-Referência seja igual ou inferior a 2010
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência até 2010 >> Formatação Mídias do módulo Obrigações de Tributos Federais\.
- __Caso o Ano\-Referência seja 2011 em diante__
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais

A regra é variável de acordo com o Ano\-Referência, visto que os layout’s são diferentes\.

OS3528

<a id="_Toc49779725"></a>RN11

__Registro RESPO__

Gravar no__ campo 3 – Nome__ a informação que estiver contida no campo “Responsável Legal” dos seguintes menus:

- Caso o Ano\-Referência seja igual ou inferior a 2010 
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência até 2010 >> Formatação Mídias do módulo Obrigações de Tributos Federais\.
- __Caso o Ano\-Referência seja 2011 em diante__
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais

A regra é variável de acordo com o Ano\-Referência, visto que os layout’s são diferentes\.

OS3528

<a id="_Toc49779726"></a>RN12

__Registro RESPO__

Gravar no__ campo 4 – DDD__ a informação que estiver contida no campo NUM\_DDD da tabela RESP\_INFORMACAO de acordo com o Responsável Legal informado no campo “Responsável Legal” dos seguintes menus:

- Caso o Ano\-Referência seja igual ou inferior a 2010 
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência até 2010 >> Formatação Mídias do módulo Obrigações de Tributos Federais\.
- __Caso o Ano\-Referência seja 2011 em diante__
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais

A regra é variável de acordo com o Ano\-Referência, visto que os layout’s são diferentes\.

Caso o primeiro algarismo da informação recuperada do campo NUM\_DDD seja “0”, utilizar o algarismo seguinte\.

__\[ALTERADA – CH22018\-A\_2014\]__

Esse campo é obrigatório e quando não estiver preenchido ou ainda estiver preenchido com zeros na tela “Responsável por Informações” \(localizada em Básicos >> Parâmetros >> Requisitos Legais >> Responsável por Informações\) deve emitir a mensagem informando a obrigatoriedade do mesmo e gerar o campo com zeros \(numérico – fixo \- tamanho 2\)\.

OS3528

CH22018\-A\_2014

<a id="_Toc49779727"></a>RN13

__Registro RESPO__

Gravar no__ campo 5 – Telefone__ a informação que estiver contida NUM\_TELEFONE da tabela RESP\_INFORMACAO de acordo com o Responsável Legal informado no campo “Responsável Legal” dos seguintes menus:

- Caso o Ano\-Referência seja igual ou inferior a 2010 
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência até 2010 >> Formatação Mídias do módulo Obrigações de Tributos Federais\.
- __Caso o Ano\-Referência seja 2011 em diante__
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais

A regra é variável de acordo com o Ano\-Referência, visto que os layout’s são diferentes\.

A partir do ano de referência 2013, o campo passa a ter 9 posições \(variável\)\. 

Caso o campo tenha 8 \(oito\) posições, utilizar essa informação, caso tenha 9 \(nove\) posições utilizar essa mesma informação\. Caso a informação recuperada do campo possua menos que 8 \(oito\) posições, completar com zeros à esquerda\. 

__\[ALTERADA – CH22018\-A\_2014\]__

Esse campo é obrigatório e quando não estiver preenchido ou ainda estiver preenchido com zeros na tela “Responsável por Informações” \(localizada em Básicos >> Parâmetros >> Requisitos Legais >> Responsável por Informações\) deve emitir a mensagem informando a obrigatoriedade do mesmo e gerar o campo com zeros \(numérico – tamanho 9\)\.

OS4293

CH22018\-A\_2014

<a id="_Toc49779728"></a>RN14

__Registro RESPO__

Gravar no__ campo 6 – Ramal__ a informação que estiver contida NUM\_RAMAL da tabela RESP\_INFORMACAO de acordo com o Responsável Legal informado no campo “Responsável Legal” dos seguintes menus:

- Caso o Ano\-Referência seja igual ou inferior a 2010 
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência até 2010 >> Formatação Mídias do módulo Obrigações de Tributos Federais\.
- __Caso o Ano\-Referência seja 2011 em diante__
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais\.

A regra é variável de acordo com o Ano\-Referência, visto que os layout’s são diferentes\.

Campo: Não obrigatório\.

OS3528

<a id="_Toc49779729"></a>RN15

__Registro RESPO__

Gravar no__ campo 7 – Fax__ a informação que estiver contida NUM\_FAX da tabela RESP\_INFORMACAO de acordo com o Responsável Legal informado no campo “Responsável Legal” dos seguintes menus:

- Caso o Ano\-Referência seja igual ou inferior a 2010 
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência até 2010 >> Formatação Mídias do módulo Obrigações de Tributos Federais\.
- __Caso o Ano\-Referência seja 2011 em diante__
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais

A regra é variável de acordo com o Ano\-Referência, visto que os layout’s são diferentes\.

A partir do ano de referência 2013, o campo passa a ter 9 posições \(fixo\)\. 

Caso o campo tenha 8 \(oito\) posições, utilizar essa informação, caso tenha 9 \(nove\) posições utilizar essa mesma informação\. Caso a informação recuperada do campo possua menos que 8 \(oito\) posições, completar com zeros à esquerda\.

Campo: Não obrigatório\.

OS4293

<a id="_Toc49779730"></a>RN16

__Registro RESPO__

Gravar no__ campo 8 – Correio Eletrônico__ a informação que estiver contida E\_MAIL da tabela RESP\_INFORMACAO de acordo com o Responsável Legal informado no campo “Responsável Legal” dos seguintes menus:

- Caso o Ano\-Referência seja igual ou inferior a 2010 
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência até 2010 >> Formatação Mídias do módulo Obrigações de Tributos Federais\.
- __Caso o Ano\-Referência seja 2011 em diante__
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais

A regra é variável de acordo com o Ano\-Referência, visto que os layout’s são diferentes\.

Campo: Não obrigatório\.

OS3528

## <a id="_Toc49801946"></a><a id="_Toc49802225"></a><a id="_Toc49802428"></a><a id="_Toc49802538"></a><a id="_Toc49803303"></a><a id="_Toc49803546"></a><a id="_Toc49805176"></a><a id="_Toc49805294"></a><a id="_Toc49805406"></a><a id="_Toc50402983"></a><a id="_Toc50403107"></a><a id="_Toc50404646"></a><a id="_Toc155171977"></a>3\.3 – DECPJ – Registro de Identificação do Declarante pessoa jurídica

<a id="_Toc49779731"></a>RN17

__Registro DECPJ__

Gravar no__ campo 1 – Identificador do Registro__ o valor fixo “__DECPJ__”\.

OS3528

<a id="_Toc49779732"></a>RN18

__Registro DECPJ__

Gravar no__ campo 2 – CNPJ__ a informação que estiver contida no campo CGC da tabela ESTABELECIMENTO de acordo com o\(s\) estabelecimento\(s\) selecionado\(s\) para a geração\.

OS3528

<a id="_Toc49779733"></a>RN19

__Registro DECPJ__

__\[ALTERADA – CH15903\_2015\]__

Gravar no__ campo 3 – Nome empresarial__ a informação que estiver contida no campo RAZAO\_SOCIAL ou no campo RAZAO\_SOCIAL\_COMPL da tabela ESTABELECIMENTO de acordo com o\(s\) estabelecimento\(s\) selecionado\(s\) para a geração\.

__Tratamento:__

- Se o campo RAZAO\_SOCIAL\_COMPL da tabela ESTABELECIMENTO estiver preenchido, considerar o conteúdo dele na geração do campo desconsiderando o conteúdo do campo RAZAO\_SOCIAL, caso não esteja preenchido, buscar o conteúdo do campo RAZAO\_SOCIAL normalmente;
- Truncar à direita caso o campo ultrapasse 150 posições exigidas pelo layout da DIRF\.

__Observação:__ No campo RAZAO\_SOCIAL\_COMPL o usuário pode informar a razão social dos estabelecimentos que tenham mais do que 100 posições \(tamanho do campo “Razão Social” original do Mastersaf\)\. Esta informação será utilizada apenas quando preenchida, nas obrigações fiscais que permitam mais que 100 caracteres no preenchimento desta informação\.

OS3528

CH15903\_2015

<a id="_Toc49779734"></a>RN20

__Registro DECPJ__

Gravar no__ campo 4 – Natureza do Declarante__ a informação que estiver contida no campo “Natureza do Declarante” da tela de Formatação das Mídias da DIRF no menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídias\. As informações contidas devem ser gravadas da seguinte forma:

- Caso a opção selecionada seja “__0__ \- Pessoa jurídica de direito privado”, gravar “__0__”\.
- Caso a opção selecionada seja “__1__ \- Órgãos, autarquias e fundações da administração pública federal”, gravar “__1__”\.
- Caso a opção selecionada seja “__2__ \- Órgãos, autarquias e fundações da administração pública estadual, municipal ou do Distrito Federal”, gravar “__2__”\.
- Caso a opção selecionada seja “__3__ – Empresa pública ou sociedade de economia mista federal”, gravar “__3__”\.
- Caso a opção selecionada seja “__4__ \- Empresa pública ou sociedade de economia mista estadual, municipal ou do Distrito Federal”, gravar “__4__”\.
- Caso a opção selecionada seja “__8__ – Entidade com alteração de natureza jurídica \(uso restrito\)”, gravar “__8__”\.

As regras para a geração da DIRF cujo Ano\-Referência seja igual ou inferior a 2010, continuam iguais, ou seja, recuperam a informação do campo “Natureza da Informação” de acordo com o menu DIRF >> Geração do Meio Magnético >> Ano\-Referência até 2010 >> Formatação Mídias\.

OS3528

<a id="_Toc49779735"></a>RN21

__Registro DECPJ__

Gravar no__ campo 5 – CPF Responsável perante o CNPJ__ a informação que estiver contida no campo NUM\_CPF da tabela RESP\_INFORMACAO de acordo com o Responsável Legal informado no campo “__Responsável Legal__” dos seguintes menus:

- Caso o Ano\-Referência seja igual ou inferior a 2010 
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência até 2010 >> Formatação Mídias do módulo Obrigações de Tributos Federais\.

Gravar no __campo 5 – CPF Responsável perante o CNPJ__ a informação que estiver contida no campo NUM\_CPF da tabela RESP\_INFORMACAO de acordo com o Responsável Legal informado no campo “__Responsável Legal do Declte PJ__” dos seguintes menus:

- __Caso o Ano\-Referência seja 2011 em diante__
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais

A regra é variável de acordo com o Ano\-Referência, visto que os layout’s são diferentes\.

OS3528

OS4382

<a id="_Toc49779736"></a>RN22

__Registro DECPJ__

Gravar no__ campo 6 – Indicador de Sócio Ostensivo responsável por sociedade em conta de participação – SCP__ a informação do campo “Sócio Ostensivo” da tela de geração da DIRF – menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

- Caso a opção selecionada seja “Não”, gravar “__N__”\.
- Caso a opção selecionada seja “Sim”, gravar “__S__”\.

OS3528

<a id="_Toc49779737"></a>RN23

__Registro DECPJ__

Gravar no__ campo 7 – Indicador de declarante depositário de crédito decorrente de decisão judicial__ a informação do campo “Declarante depositário de crédito decorrente de decisão judicial” da tela de geração da DIRF – menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

- Caso a opção selecionada seja “Não”, gravar “__N__”\.
- Caso a opção selecionada seja “Sim”, gravar “__S__”\.

OS3528

<a id="_Toc49779738"></a>RN24

__Registro DECPJ__

Gravar no__ campo 8 – Indicador de declarante de instituição administradora ou intermediadora de fundo ou clube de investimento__ a informação do campo “Declarante de instituição administradora ou intermediadora de fundo ou clube de investimento” da tela de geração da DIRF – menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

- Caso a opção selecionada seja “Não”, gravar “__N__”\.
- Caso a opção selecionada seja “Sim”, gravar “__S__”\.

OS3528

<a id="_Toc49779739"></a>RN25

__Registro DECPJ__

Gravar no__ campo 9 – Indicador de declarante de rendimentos pagos a residentes ou domiciliados no exterior__ a informação do campo “Declarante de rendimentos pagos a residentes ou domiciliados no exterior” da tela de geração da DIRF – menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

- Caso a opção selecionada seja “Não”, gravar “__N__”\.
- Caso a opção selecionada seja “Sim”, gravar “__S__”\.

OS3528

<a id="_Toc49779740"></a>RN26

__Registro DECPJ__

Gravar no__ campo 10 – Indicador de plano privado de assistência à saúde – coletivo__ empresarial a informação do campo “Plano privado de assistência à saúde – coletivo empresarial” da tela de geração da DIRF – menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

- Caso a opção selecionada seja “Não”, gravar “__N__”\.
- Caso a opção selecionada seja “Sim”, gravar “__S__”\.

OS3528

<a id="_Toc49779741"></a>RN355

__Registro DECPJ__

     

- Gravar no campo 11 – Indicador de Pagamentos Relacionados aos Jogos Olímpicos de 2016 e aos Jogos Paraolímpicos de 2016

Se selecionado o campo ““Pagamentos relacionados aos Jogos Olímpicos de 2016 e aos Jogos Paraolímpicos de 2016” \(Menu: DIRF >> Geração DIRF Módulo: OTF\)

Gravar “S”

Se não

Gravar “N”

\[MFS\-21816\]

Na DIRF2019: Gravar no__ campo 11 – O “indicador de entidade em que a União detém maioria do capital a voto”\.__ Vide parâmetro criado na tela \(RN01\)\.

\(\.\.\.\)recebe recursos do Tesouro Nacional e está obrigada a registrar a execução orçamentária no Siafi \(IN 1\.234/2012\), art\. 4º, incisos ||| e |V\.

Esse campo é de preenchimento obrigatório na geração do arquivo magnético, será um Checkbox:

Caso o campo esteja marcado, gravar “__S__” \- significa que existe pagamento de valores a entidades imunes/isentas\.

Caso o campo esteja desmarcado, gravar “__N__” \- significa que não é uma declaração de situação especial\.

__Tratamento: __

A opção “__S__” só será permitida se no campo 4 – Natureza do declarante \(Da tela de Formatação das Mídias da DIRF no menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídias\) estiver parametrizado com as opções “__0__”,“__1__”,”__3__” OU “__8__”\. 

Se o usuário informar um valor diferente das opções mencionadas no campo “Natureza do Declarante” e tentar marcar o campo 11 \- Indicador de entidade em que a União detém maioria do capital a voto, o sistema deverá exibir a mensagem de aviso na tela: 

__“*Indicador de entidade em que a União detém maioria do capital a voto' será marcado se o campo Natureza do Declarante estiver preenchido com uma das seguintes opções '0','1','3' ou '8”\.*__

Tamanho: 1 posição

Tipo: Caractere

__*Observação*__: o campo foi incluído na tela de geração da DIRF2018 \(Menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\)\. Porém, no ano passado este indicador era gerado no campo 12 do registro INFPA vide \(RN394\)\.

MFS\-2346

MFS\-21816

<a id="_Toc49779742"></a>RN394

__Registro DECPJ__

Gravar no campo 12 – Indicador de entidade em que a União detém maioria do capital a voto, recebe recursos do Tesouro  Nacional e está obrigada a registrar a execução orçamentária no Siafi \(IN 1\.234/2012\), art\. 4º, incisos ||| e |V\.

Incluir o campo na tela de geração da DIRF em: \(da tela de geração da DIRF – menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

Esse campo é de preenchimento obrigatório na geração do arquivo magnético, será um CheckBox:

Caso o campo esteja marcado, gravar “S” 

Caso o campo esteja desmarcado, gravar “N”\.

__Tratamento: __

A opção “S” só será permitida se no campo 4 – Natureza do declarante \(Da tela de Formatação das Mídias da DIRF no menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídias\) estiver parametrizado com as opções “0”,“1”,”3” OU “8”\. 

Se o usuário informar um valor diferente das opções mencionadas no campo “Natureza do Declarante” e tentar marcar o campo 12 \- Indicador de entidade em que a União detém maioria do capital a voto, o sistema deverá exibir a mensagem de aviso na tela: “*Indicador de entidade em que a União detém maioria do capital a voto' será marcado se o campo Natureza do Declarante estiver preenchido com uma das seguintes opções '0','1','3' ou '8”\.*

Tamanho: 1 posição

Tipo: Caractere

Observação: Esse campo será considerado na geração a partir do ano calendário 2017\.

\[MFS\-21816\]

Na DIRF 2019: Gravar no__ campo 12: “Indicador de fundação pública de direito privado”\. __

\(\.\.\.\) instituída pela União, Estados, Municípios ou Distrito Federal\. Vide parâmetro novo criado na tela \(RN01\)\.

Incluir o campo na tela de geração da DIRF em: \(Menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\)\.

Esse campo é de preenchimento obrigatório na geração do arquivo magnético, será um Checkbox:

Caso o campo esteja marcado, gravar “__S__” – Fundação pública de direito privado\.

Caso o campo esteja desmarcado, gravar “__N__”\- Não é fundação pública de direito privado\.

Default: desmarcado\.

\[MFS\-62410\] Tratamento para as empresa de Natureza Declarante “3 – Empresas públicas ou sociedade de economia mista Federal”\.\(Cliente Finep\)

__Tratamento: __

Se o campo “Indicador de fundação pública de direito privado” \(Da tela de geração da DIRF\) estiver marcado __e__ se o campo 4 – Natureza do declarante \(Da tela de Formatação das Mídias da DIRF no menu DIRF >> Geração do Meio >> Ano\-Referência a partir de 2011 >> Formatação Mídias\) estiver parametrizado com a opção ”3”, Gravar __“N”__ no campo 12\.

MFS\-14872

MFS\-21816

<a id="_Toc49779743"></a>RN28

__Registro DECPJ__

Gravar no__ campo 13 – Indicador de situação especial da declaração__ a informação do campo “Extinção” da tela de geração da DIRF – menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

- Caso o campo esteja marcado, gravar “__S__”\.
- Caso o campo esteja desmarcado, gravar “__N__”\.

OS3528/

MFS\-2346

<a id="_Toc49779744"></a>RN29

__Registro DECPJ__

Gravar no__ campo 14 – Data do evento__ a informação do campo “Data do evento” da tela de geração da DIRF – menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\. A informação deve ser gravada no formato AAAAMMDD\.

Obs: Obrigatório se o campo de ordem 13 igual a “__S__”

OS3528/ 

MFS\-2346

MFS14872

## <a id="_Toc49801947"></a><a id="_Toc49802226"></a><a id="_Toc49802429"></a><a id="_Toc49802539"></a><a id="_Toc49803304"></a><a id="_Toc49803547"></a><a id="_Toc49805177"></a><a id="_Toc49805295"></a><a id="_Toc49805407"></a><a id="_Toc50402984"></a><a id="_Toc50403108"></a><a id="_Toc50404647"></a><a id="_Toc155171978"></a>3\.4 – IDREC – Registro de Identificação do código de receita

<a id="_Toc49779745"></a>RN30

__Registro IDREC__

Gravar no __campo 1 – Identificador do Registro__ o valor fixo “__IDREC__”\.

OS3528

<a id="_Toc49779746"></a>RN31

__Registro IDREC__

Gravar no __campo 2 – Código de Receita__ os códigos de receita de acordo com a regra abaixo:

- Caso a informação componha o registro __BPFDEC__ – ou seja, seja originária da tabela X21\_FICHA\_FINANC, gravar a informação contida no campo “c/ Vínculo Empregatício” da tela de geração do meio magnético \(menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.
- Caso a informação componha os registros __BPFDEC__ ou __BPJDEC__ – ou seja, seja originária da tabela X53\_RETENCAO\_IRRF e o Participante seja uma Pessoa Física ou Jurídica \(o que caracteriza uma retenção referente à uma prestação de serviço\), gravar o conteúdo do campo 11 \(COD\_DARF\) da mesma tabela X53\_RETENCAO\_IRRF ou __X530\_RETIFICACAO\_IRRF__ caso exista um registro nessa tabela, sendo o mais recente \(vide __RNG\-01__\)\.

Ver __RN337__ com tratamento para PLR\.

OS3528

OS3267\-B

MFS\-90689

## <a id="_Toc49802430"></a><a id="_Toc49802540"></a><a id="_Toc49803305"></a><a id="_Toc49803548"></a><a id="_Toc49805178"></a><a id="_Toc49805296"></a><a id="_Toc49805408"></a><a id="_Toc50402985"></a><a id="_Toc50403109"></a><a id="_Toc50404648"></a>

## <a id="_Toc155171979"></a>3\.5 – BPFDEC – Registro de Beneficiário pessoa física do declarante

<a id="_Toc49779747"></a>RN32

__Registro BPFDEC__

Gravar no __campo 1 – Identificador de Registro__ o valor fixo “__BPFDEC__”\.

As informações desse registro serão recuperadas das tabelas SAFX21 \(Ficha Financeira do Funcionário\) e SAFX53 \(Controle de Tributos – Retenções\)\. Para que as informações sejam recuperadas da SAFX53, serão recuperadas somente as retenções que pertençam a uma Pessoa Física\. Caso o registro da SAFX53 possua uma ou mais retificações na tabela __X530\_RETIFICACAO\_IRRF__, deverá ser recuperado o registro mais recente dessa tabela \(vide __RNG\-01__\)\. Caso no mesmo ano calendário, a pessoa física possua retenções ou retificações distintas para a mesma pessoa física, porém com datas de validade distintas, deverá ser gerado na DIRF a pessoa física com data de validade mais recente no ano calendário\.

Serão recuperados os Beneficiários a partir da SAFX21 cujo valor total de rendimentos anuais seja igual ou superior ao valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

\[CH9048/2015\]

__\[MFS\-59751\]__ Tratamento dos funcionários sem vínculo empregatício e que tenham valor de IR Retido

__\[MFS\-60780\]__ Desfazimento da regra criada pela MFS\-59751

Caso os beneficiários recuperados sejam da SAFX53 \(o que caracteriza trabalho sem vínculo empregatício, de aluguéis ou royalties – ver o código de Retenção a partir do campo “s/ Vínculo Empregatício” – e também os Códigos de Retenção da SAFX53 \(campo 11 \(COD\_DARF\) da SAFX53 = 3208\), considerar os valores de rendimentos pagos \(VLR\_BRUTO\) e isentos \(VLR\_OUTROS\_DIRF\) acima de R$ 6\.000,00\. Mesmo que o valor do tributo \(VLR\_IR\_RETIDO\) seja maior que zero, somente serão considerados os valores que tenham rendimentos pagos \(VLR\_BRUTO\) e isentos \(VLR\_OUTROS\_DIRF\) acima que R$ 6\.000,00\.

\(OBS: essa regra já existe na DIRF 2010\)\.

OS3528

OS3267\-D

CH2574\_2014

MFS\-3988

MFS\-59751

MFS\-60780

MFS\-90689

<a id="_Toc49779748"></a>RN33

__Registro BPFDEC__

Gravar no __campo 2 – CPF__ o CPF do Beneficiário\.

- SAFX21
	- Recuperar o CPF do Funcionário a partir do campo 03 \(COD\_FUNC\) da SAFX21\. Com essa informação, recuperar o campo 12 \(CPF\) da tabela SAFX15 e gravar a informação\.
- SAFX53
	- Recuperar o CPF da Pessoa Física a partir dos campos 04 \(IND\_FIS\_JUR\) e 05 \(COD\_FIS\_JUR\) da SAFX53 ou IND\_FIS\_JUR/COD\_FIS\_JUR da __X530\_RETIFICACAO\_IRRF__\. Com essa informação, recuperar o campo 06 \(CPF\_CGC\) da tabela SAFX04 e gravar a informação\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779749"></a>RN34

__Registro BPFDEC__

Gravar no __campo 3 – Nome__ o nome do beneficiário pessoa física\.

Caso a informação seja da SAFX53, 

- SAFX21
	- Recuperar o Nome do Funcionário a partir do campo 03 \(COD\_FUNC\) da SAFX21\. Com essa informação, recuperar o campo 05 \(NOME\) da tabela SAFX15 e gravar a informação\.
- SAFX53
	- Recuperar o Nome da Pessoa Física a partir dos campos 04 \(IND\_FIS\_JUR\) e 05 \(COD\_FIS\_JUR\) da SAFX53 ou IND\_FIS\_JUR/COD\_FIS\_JUR da __X530\_RETIFICACAO\_IRRF__\. Com essa informação, recuperar o campo 05 \(RAZAO\_SOCIAL\) da tabela SAFX04 e gravar a informação\. Caso no mesmo ano calendário, a pessoa física possua retenções ou retificações distintas para a mesma pessoa física, porém com datas de validade distintas, deverá ser gerado na DIRF a pessoa física cuja descrição esteja com a data de validade mais recente no ano calendário\.

OS3528

OS3267\-D

CH2574\_2014

MFS\-90689

<a id="_Toc49779750"></a>RN35

__Registro BPFDEC__

Gravar no __campo 4 – Data atribuída pelo laudo da moléstia grave__ a informação da Data de afastamento do funcionário\.

- SAFX21
	- Recuperar a Data atribuída pelo laudo da moléstia grave a partir do campo 03 \(COD\_FUNC\) da SAFX21\. Com essa informação, recuperar o campo “Data atribuída pelo laudo da moléstia grave” da tabela SAFX15 – Campo 70 \(DATA\_MOLESTIA\) e gravar a informação\.
- SAFX53
	- Recuperar o Data atribuída pelo laudo da moléstia grave a partir dos campos 04 \(IND\_FIS\_JUR\) e 05 \(COD\_FIS\_JUR\) da SAFX53 ou IND\_FIS\_JUR/COD\_FIS\_JUR da __X530\_RETIFICACAO\_IRRF__\. Com essa informação, recuperar o campo “Data atribuída pelo laudo da moléstia grave” da tabela SAFX04 – Campo 52 \(DATA\_MOLESTIA\) e gravar a informação\.

__OBS:__ Ao preencher esse campo é habilitado o flegue beneficiário é portador de moléstia grave atestada por laudo médico \(Validador\)\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779751"></a>RN395

__Registro BPFDEC__

Gravar no __campo 5 – Indicador de Identificação do alimentando__\.

__\[ALTERADA \- CH1608\_2018 \(MFS\-16323\)\]__

Esse campo é de preenchimento obrigatório na geração do arquivo magnético e deverá ser igual a “__S__” quando houver registro INFPA e RTPA, caso contrário gerar “__N__” e apresentar apenas os registros de valores RTPA e/ou ESPA\.

Verificar se para o beneficiário em \(Federal >> OTF >> DIRF >> Rendimentos Recebidos Acumuladamente \(Pensão Alimentícia\) tabela: IRT\_DIRF\_MM\_RRA\_DEP possui valor cadastrado para o COD\_FUNC  em algum mês das colunas de ”Pensão Alimentícia” do respectivo ano calendário da geração da DIRF\.

Caso possua valor em alguma coluna/mês, marcar esse campo como “S” , deverá constar o registro INFPA seguido do registro de valor \(RTPA e/ou ESPA\) para cada alimentado no arquivo magnético\.

Senão, gerar como “N”, não apresentar o registro INFPA, deverão constar apenas os registros de valores \(RTPA e/ou ESPA\)

 

Tamanho: 1 posição

Tipo: Caractere

Observação: Esse campo será considerado na geração a partir do ano calendário 2017\.

MFS14872

CH1608\_2018 \(MFS\-16323\)

<a id="_Toc49779752"></a>RN396

__Registro BPFDEC__

Gravar no __campo 6 – Indicador de Identificação da previdência complementar__

Esse campo é de preenchimento obrigatório na geração do arquivo magnético\. 

Verificar se para o beneficiário em \(Básicos >> Mastersaf DW >> Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Plano Previdência\) SAFX207 possui valor da verba cadastrado para o COD\_FUNC \- Campo 03  para o respectivo ano calendário da geração da DIRF\.

Caso possua valor da verba, marcar esse campo como “__S__”, deverá constar o registro INFPC seguido do registro de valor \(RTPP, RTFA, RTSP e/ou ESPP, ESFA, ESSP\) para cada entidade de previdência complementar do beneficiário\.

Senão, gerar como “__N__”, não apresentar o registro INFPC, deverão constar apenas os registros de valores mensais \(RTPP, RTFA, RTSP e/ou ESPP, ESPA, ESSP\) com o total dos valores de previdência complementar pagos pelo beneficiário\.

As informações detalhadas a que se refere o campo são: CNPJ e Nome empresarial da entidade de previdência complementar \(Registro INFPC\)\.

 

Tamanho: 1 posição

Tipo: Caractere

Observação: Esse campo será considerado na geração a partir do ano calendário 2017\.

MFS\-14872

## <a id="_Toc49803306"></a><a id="_Toc49803549"></a><a id="_Toc49805179"></a><a id="_Toc49805297"></a><a id="_Toc49805409"></a><a id="_Toc50402986"></a><a id="_Toc50403110"></a><a id="_Toc50404649"></a><a id="_Toc155171980"></a>3\.6 – Registro de valores mensais: RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTDS, RTIRF, ESPP, ESFA, ESSP, ESEP, ESPA

RTRT \- Rendimentos Tributáveis \- Rendimento Tributável 

RTPO \- Rendimentos Tributáveis \- Dedução \- Previdência Oficial 

RTPP \- Rendimentos Tributáveis \- Dedução \- Previdência Privada 

RTFA \- Rendimentos Tributáveis \- Dedução \- FAPI 

RTSP \- Rendimentos Tributáveis \- Dedução \- Fundo de Previdência do Servidor Público

RTDP \- Rendimentos Tributáveis \- Dedução \- Dependentes 

RTPA \- Rendimentos Tributáveis \- Dedução \- Pensão Alimentícia

RTDS \- Rendimentos Tributáveis \- Dedução – Desconto Simplificado Mensal

RTIRF\- Rendimentos Tributáveis \- Imposto sobre a Renda Retido na Fonte

ESPP \- Tributação com Exigibilidade Suspensa \- Dedução \- Previdência Privada 

ESFA \- Tributação com Exigibilidade Suspensa \- Dedução \- FAPI 

ESSP \- Tributação com Exigibilidade Suspensa \- Dedução \- Fundo de Previdência do Servidor Público

ESEP \- Tributação com Exigibilidade Suspensa \- Dedução \- Contribuição do ente público patrocinador

ESPA \- Tributação com Exigibilidade Suspensa \- Dedução \- Pensão Alimentícia

<a id="_Toc49779764"></a>RN39

__Registro RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTDS, RTIRF, ESPP, ESFA, ESSP, ESEP, ESPA:__

Devem ser recuperados as fichas financeiras \(tabela X21\_FICHA\_FINANC\) e as retenções \(X53\_RETENCAO\_IRRF ou __X530\_RETIFICACAO\_IRRF__\) dos funcionários e dos prestadores que estejam no período informado para a geração\. 

O campo “Tipo Lançamento” \(campo 11 da SAFX21 e 40 da SAFX53 ou __X530\_RETIFICACAO\_IRRF__\) deve estar selecionado com a opção “Informações dos Beneficiários”\.

No caso da SAFX53/__X530\_RETIFICACAO\_IRRF__ deverão ser recuperados somente os beneficiários que forem PESSOA FÍSICA\.

As retenções da tabela X53\_RETENCAO\_IRRF, cujos campos “Estorno” e “Data do Estorno” estiverem preenchidos, não deverão ser consideradas para a geração da DIRF\. Vale salientar que essas retenções não possuem registros de retificação\.

Caso um funcionário ou prestador de serviços não possua valores para retenção de Imposto de Renda no período para nenhum mês ou Décimo Terceiro Salário, o mesmo não deverá ser informado\.

Gravar no campo 1 – Identificador do Registro a informação de acordo com as regras abaixo:

- Gravar o valor fixo __“RTRT”__ caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Rendimentos Tributáveis”\.
	- No caso da SAFX53, recuperar a informação a partir da somatória dos campos VLR\_BRUTO __e__ __VLR\_OUTROS\_TRIB\_EXCL__ da SAFX53 ou __X530\_RETIFICACAO\_IRRF__ mais recente \(vide __RNG\-01__\)\.
		- Ao gerar a consolidação por Beneficiário e Mês para geração desse registro, caso o campo VLR\_APOSENT\_ISENTA esteja preenchido para pelo menos um dos registros da SAFX53 ou __X530\_RETIFICACAO\_IRRF__ mais recente no Ano Calendário de 2012, o sistema irá recuperar o campo VLR\_BRUTO e irá subtrair o somatório do campo VLR\_APOSENTADORA\_ISENTA\. Caso o campo seja menor ou igual que R$ 1\.637,11 esse valor irá compor o registro RTRT do mês em processamento\. Caso seja maior também, porém será exibida a seguinte mensagem no log de geração da DIRF: “O valor da parcela isenta referente a rendimentos de aposentadoria, reserva, reforma e pensão para maiores de 65 anos, permitida pela legislação para o ano calendário é de R$ 1\.637,11 por mês\.”\. A informação será gerada da mesma forma\.
		- Caso o campo VLR\_APOSENT\_ISENTA não esteja preenchido para pelo menos um dos registros da SAFX53 ou __X530\_RETIFICACAO\_IRRF__ mais recente com o valor de R$ 1\.637,11, o sistema irá considerar o campo VLR\_BRUTO como informação do registro RTRT\.
		- Caso o campo VLR\_BRUTO seja inferior ao valor de R$ 1\.637,11 informado em pelo menos um dos registros do beneficiário, o sistema irá considerar o campo VLR\_BRUTO como valor do registro RTRT e o registro RIP65 não será gerado\.
- Gravar o valor fixo __“RTPO”__ caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Previdência Oficial\)”\. No caso da SAFX53, recuperar a informação do campo VLR\_DED\_INSS\_TERC da SAFX53 ou __X530\_RETIFICACAO\_IRRF__ mais recente\.
- Gravar o valor fixo __“RTPP”__ caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Previdência Complementar\)” e no \(campo 11 da SAFX207\) no módulo Básicos >> MastersafDW >> Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Previdência com a opção \(Previdência Privada\)\. 
- Gravar o valor fixo __“RTFA”__ caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Previdência Complementar\)” e no \(campo 11 da SAFX207\) no módulo Básicos >> MastersafDW >> Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Previdência com a opção \(FAPI\)\.
- Gravar o valor fixo __“RTSP”__ caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Previdência Complementar\)” e no \(campo 11 da SAFX207\) no módulo Básicos >> MastersafDW >> Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Previdência com a opção \(Fundo de Previdência do Servidor Público\)\.
- Gravar o valor fixo __“RTEP”__ caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Previdência Complementar\)” e no \(campo 11 da SAFX207\) no módulo Básicos >> MastersafDW >> Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Previdência com a opção \(Contribuição do Ente Público Patrocinador\)\.
- Gravar o valor fixo __“RTEP”__ caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Previdência Complementar\)” e no \(campo 11 da SAFX207\) no módulo Básicos >> MastersafDW >> Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Previdência com a opção \(Contribuição do Ente Público Patrocinador\)\.
- Gravar o valor fixo __“ESPP”__ caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Previdência Complementar\)”\. No \(campo 11 da SAFX207\) módulo Básicos >> MastersafDW >> Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Previdência com a opção \(Previdência Privada\) e no \(campo 11 da SAFX21\) módulo Básicos >> MastersafDW >> Manutenção >> Folha de Pagamento >> Ficha Financeira com a opção \(Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa\)\.
- Gravar o valor fixo __“ESFA”__ caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Previdência Complementar\)”\. No \(campo 11 da SAFX207\) módulo Básicos >> MastersafDW >> Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Previdência com a opção \(FAPI\) e no \(campo 11 da SAFX21\) módulo Básicos >> MastersafDW >> Manutenção >> Folha de Pagamento >> Ficha Financeira com a opção \(Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa\)\.
- Gravar o valor fixo __“ESSP”__ caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Previdência Complementar\)”\. No \(campo 11 da SAFX207\) módulo Básicos >> MastersafDW >> Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Previdência com a opção \(Fundo de Previdência do Servidor Público\) e no \(campo 11 da SAFX21\) módulo Básicos >> MastersafDW >> Manutenção >> Folha de Pagamento >> Ficha Financeira com a opção \(Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa\)\.
- Gravar o valor fixo __“ESEP”__ caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Previdência Complementar\)”\. No \(campo 11 da SAFX207\) módulo Básicos >> MastersafDW >> Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Previdência com a opção \(Contribuição do Ente Público Patrocinador\) e no \(campo 11 da SAFX21\) módulo Básicos >> MastersafDW >> Manutenção >> Folha de Pagamento >> Ficha Financeira com a opção \(Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa\)\.
- Gravar o valor fixo __“RTDP”__ caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Dependentes\)”\. No caso da SAFX53, recuperar a informação do campo VLR\_DED\_DEP\_TERC da SAFX53 ou __X530\_RETIFICACAO\_IRRF__ mais recente\.
- Gravar o valor fixo __“RTPA” __caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Pensão Alimentícia\)”\. 
- Gravar o valor fixo __“ESPA”__ caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Pensão Alimentícia\)” e no \(campo 11 da SAFX21\) módulo Básicos >> MastersafDW >> Manutenção >> Folha de Pagamento >> Ficha Financeira com a opção \(Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa\)\.
- Gravar o valor fixo __“RTIRF”__ caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Imposto de Renda Retido”\. No caso da SAFX53, recuperar a informação do campo VLR\_IR\_RETIDO da SAFX53 ou __X530\_RETIFICACAO\_IRRF__ mais recente\.
- __\[ALTERAÇÃO MFS\-594253\]__ Gravar o valor fixo __“RTDS”__ caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Desconto Simplificado Mensal\)” e com o campo 11 da SAXF21 sem preenchimento, ou com informação diferente de ‘2’\. No caso da SAFX53, recuperar a informação do campo VLR\_DESC\_SIMPL\_MENSAL da SAFX53 

OS3528

OS3267\-D

CH2967\_2012

CH5171\_2013

MFS\-8800

MFS\-90689

MFS\-594253

<a id="_Toc49779767"></a>RN40

__Registro RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTDS, RTIRF, ESPP, ESFA, ESSP, ESEP, ESPA:__

Gravar no __campo 2 – janeiro__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de janeiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\.

- Para os registros __RTPP, RTFA, RTSP, RTEP, ESPP, ESFA, ESSP, ESEP__ gravar no campo 2 – janeiro o valor contido no campo 12 da SAFX207 para a competência de janeiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX207\)\. 
- Para os registros __RTPA, ESPA__ gravar no campo 2 – janeiro o valor contido no campo 10 \(VLR\_VERBA\) da SAFX212 para a competência de janeiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX212\)\. 

No caso da SAFX53/__X530\_RETIFICACAO\_IRRF__ a informação deve ser recuperada da seguinte maneira:

- Para o registro __RTRT__: ver campo 14 \- VLR\_BRUTO e campo 43 \- VLR\_OUTROS\_TRIB\_EXCL da SAFX53 ou __X530\_RETIFICACAO\_IRRF__, observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.
- Para os registros __RTPO, RTDP__ e ver os seguintes campos da SAFX53 ou __X530\_RETIFICACAO\_IRRF__\.
	- RTPO: campo 41 \- VLR\_DED\_INSS\_TERC
	- RTPP: campo 29 \- VLR\_PREV\_PRIVADA
	- RTDP: campo 42 \- VLR\_DED\_DEP\_TERC
	- RTPA: campo 30 \- VLR\_PENS\_ALIMENT
- __\[ALTERAÇÃO MFS\-594253\] Para o RTDS:__ campo 105\- VLR\_DESC\_SIMPL\_MENSAL da SAFX53 
- Para o registro __RTIRF__: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou __X530\_RETIFICACAO\_IRRF\.__

OS3528

OS3267\-D

CH2967\_2012

CH5171\_2013

MFS\-8800

MFS\-90689

MFS\-594253

<a id="_Toc49779768"></a>RN41

__Registro RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTDS, RTIRF, ESPP, ESFA, ESSP, ESEP, ESPA:__

Gravar no __campo 3 – fevereiro__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de fevereiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\. 

- Para os registros __RTPP, RTFA, RTSP, RTEP, ESPP, ESFA, ESSP, ESEP__ gravar no campo 3 – fevereiro o valor contido no campo 12 da SAFX207 para a competência de fevereiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX207\)\. 
- Para os registros __RTPA, ESPA__ gravar no campo 3 – fevereiro o valor contido no campo 10 \(VLR\_VERBA\) da SAFX212 para a competência de fevereiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX212\)\. 

No caso da SAFX53/__X530\_RETIFICACAO\_IRRF__ a informação deve ser recuperada da seguinte maneira:

- Para o registro __RTRT__: ver campo 14 \- VLR\_BRUTO e campo 43 \- VLR\_OUTROS\_TRIB\_EXCL da SAFX53 ou __X530\_RETIFICACAO\_IRRF__, observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.
- Para os registros __RTPO, RTDP__ e ver os seguintes campos da SAFX53 ou __X530\_RETIFICACAO\_IRRF__\.
	- RTPO: campo 41 \- VLR\_DED\_INSS\_TERC
	- RTPP: campo 29 \- VLR\_PREV\_PRIVADA
	- RTDP: campo 42 \- VLR\_DED\_DEP\_TERC
	- RTPA: campo 30 \- VLR\_PENS\_ALIMENT
- __\[ALTERAÇÃO MFS\-594253\] __RTDS: campo 105\- VLR\_DESC\_SIMPL\_MENSAL da SAFX53 
- Para o registro __RTIRF__: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou __X530\_RETIFICACAO\_IRRF\.__

OS3528

OS3267\-D

CH2967\_2012

CH5171\_2013

MFS\-8800

MFS\-90689

MFS\-594253

<a id="_Toc49779769"></a>RN42

__Registro RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTDS, RTIRF, ESPP, ESFA, ESSP, ESEP, ESPA:__

Gravar no __campo 4 – março__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de março \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\. 

- Para os registros __RTPP, RTFA, RTSP, RTEP, ESPP, ESFA, ESSP, ESEP__ gravar no campo 4 – março o valor contido no campo 12 da SAFX207 para a competência de março \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX207\)\. 
- Para os registros __RTPA, ESPA__ gravar no campo 4 – março o valor contido no campo 10 \(VLR\_VERBA\) da SAFX212 para a competência de Março \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX212\)\. 

No caso da SAFX53/__X530\_RETIFICACAO\_IRRF__ a informação deve ser recuperada da seguinte maneira:

- Para o registro __RTRT__: ver campo 14 \- VLR\_BRUTO e campo 43 \- VLR\_OUTROS\_TRIB\_EXCL da SAFX53 ou __X530\_RETIFICACAO\_IRRF__, observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.
- Para os registros __RTPO, RTDP__ e ver os seguintes campos da SAFX53 ou __X530\_RETIFICACAO\_IRRF__\.
	- RTPO: campo 41 \- VLR\_DED\_INSS\_TERC
	- RTPP: campo 29 \- VLR\_PREV\_PRIVADA
	- RTDP: campo 42 \- VLR\_DED\_DEP\_TERC
	- RTPA: campo 30 \- VLR\_PENS\_ALIMENT
- __\[ALTERAÇÃO MFS\-594253\] __RTDS: campo 105\- VLR\_DESC\_SIMPL\_MENSAL da SAFX53 
- Para o registro __RTIRF__: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou __X530\_RETIFICACAO\_IRRF\.__

OS3528

OS3267\-D

CH2967\_2012

CH5171\_2013

MFS\-8800

MFS\-90689

MFS\-594253

<a id="_Toc49779770"></a>RN43

__Registro RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTDS, RTIRF, ESPP, ESFA, ESSP, ESEP, ESPA:__

Gravar no __campo 5 – abril__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Abril \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\. 

- Para os registros __RTPP, RTFA, RTSP, RTEP, ESPP, ESFA, ESSP, ESEP__ gravar no campo 5 – abril o valor contido no campo 12 da SAFX207 para a competência de abril \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX207\)\. 
- Para os registros __RTPA, ESPA__ gravar no campo 5 – abril o valor contido no campo 10 \(VLR\_VERBA\) da SAFX212 para a competência de abril \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX212\)\. 

No caso da SAFX53/__X530\_RETIFICACAO\_IRRF__ a informação deve ser recuperada da seguinte maneira:

- Para o registro __RTRT__: ver campo 14 \- VLR\_BRUTO e campo 43 \- VLR\_OUTROS\_TRIB\_EXCL da SAFX53 ou __X530\_RETIFICACAO\_IRRF__, observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.
- Para os registros __RTPO, RTDP__ e ver os seguintes campos da SAFX53 ou __X530\_RETIFICACAO\_IRRF__\.
	- RTPO: campo 41 \- VLR\_DED\_INSS\_TERC
	- RTPP: campo 29 \- VLR\_PREV\_PRIVADA
	- RTDP: campo 42 \- VLR\_DED\_DEP\_TERC
	- RTPA: campo 30 \- VLR\_PENS\_ALIMENT
- __\[ALTERAÇÃO MFS\-594253\] __RTDS: campo 105\- VLR\_DESC\_SIMPL\_MENSAL da SAFX53 
- Para o registro __RTIRF__: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou __X530\_RETIFICACAO\_IRRF\.__

OS3528

OS3267\-D

CH2967\_2012

CH5171\_2013

MFS\-8800

MFS\-90689

MFS\-594253

<a id="_Toc49779771"></a>RN44

__Registro RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTDS, RTIRF, ESPP, ESFA, ESSP, ESEP, ESPA:__

Gravar no __campo 6 – maio__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de maio \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\. 

- Para os registros __RTPP, RTFA, RTSP, RTEP, ESPP, ESFA, ESSP, ESEP__ gravar no campo 6 – maio o valor contido no campo 12 da SAFX207 para a competência de maio \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX207\)\. 
- Para os registros __RTPA, ESPA__ gravar no campo 6 – maio o valor contido no campo 10 \(VLR\_VERBA\) da SAFX212 para a competência de maio \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX212\)\. 

No caso da SAFX53/__X530\_RETIFICACAO\_IRRF__ a informação deve ser recuperada da seguinte maneira:

- Para o registro __RTRT__: ver campo 14 \- VLR\_BRUTO e campo 43 \- VLR\_OUTROS\_TRIB\_EXCL da SAFX53 ou __X530\_RETIFICACAO\_IRRF__, observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.
- Para os registros __RTPO, RTDP__ e ver os seguintes campos da SAFX53 ou __X530\_RETIFICACAO\_IRRF__\.
	- RTPO: campo 41 \- VLR\_DED\_INSS\_TERC
	- RTPP: campo 29 \- VLR\_PREV\_PRIVADA
	- RTDP: campo 42 \- VLR\_DED\_DEP\_TERC
	- RTPA: campo 30 \- VLR\_PENS\_ALIMENT
- __\[ALTERAÇÃO MFS\-594253\] __RTDS: campo 105\- VLR\_DESC\_SIMPL\_MENSAL da SAFX53 
- Para o registro __RTIRF__: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou __X530\_RETIFICACAO\_IRRF\.__

OS3528

OS3267\-D

CH2967\_2012

CH5171\_2013

MFS\-8800

MFS\-90689

MFS\-594253

<a id="_Toc49779772"></a>RN45

__Registro RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTDS, RTIRF, ESPP, ESFA, ESSP, ESEP, ESPA:__

Gravar no __campo 7 – junho__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de junho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\. 

- Para os registros __RTPP, RTFA, RTSP, RTEP, ESPP, ESFA, ESSP, ESEP__ gravar no campo 7 – junho o valor contido no campo 12 da SAFX207 para a competência de junho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX207\)\. 
- Para os registros __RTPA, ESPA__ gravar no campo 7 – junho o valor contido no campo 10 \(VLR\_VERBA\) da SAFX212 para a competência de Junho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX212\)\. 

No caso da SAFX53/__X530\_RETIFICACAO\_IRRF__ a informação deve ser recuperada da seguinte maneira:

- Para o registro __RTRT__: ver campo 14 \- VLR\_BRUTO e campo 43 \- VLR\_OUTROS\_TRIB\_EXCL da SAFX53 ou __X530\_RETIFICACAO\_IRRF__, observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.
- Para os registros __RTPO, RTDP__ e ver os seguintes campos da SAFX53 ou __X530\_RETIFICACAO\_IRRF__\.
	- RTPO: campo 41 \- VLR\_DED\_INSS\_TERC
	- RTPP: campo 29 \- VLR\_PREV\_PRIVADA
	- RTDP: campo 42 \- VLR\_DED\_DEP\_TERC
	- RTPA: campo 30 \- VLR\_PENS\_ALIMENT
- __\[ALTERAÇÃO MFS\-594253\] __RTDS: campo 105\- VLR\_DESC\_SIMPL\_MENSAL da SAFX53 
- Para o registro __RTIRF__: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou __X530\_RETIFICACAO\_IRRF\.__ 

OS3528

OS3267\-D

CH2967\_2012

CH5171\_2013

MFS\-8800

MFS\-90689

MFS\-594253

<a id="_Toc49779773"></a>RN46

__Registro RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTDS, RTIRF, ESPP, ESFA, ESSP, ESEP, ESPA:__

Gravar no __campo 8 – julho __o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de julho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\. 

- Para os registros __RTPP, RTFA, RTSP, RTEP, ESPP, ESFA, ESSP, ESEP__ gravar no campo 8 – julho o valor contido no campo 12 da SAFX207 para a competência de julho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX207\)\. 
- Para os registros __RTPA, ESPA__ gravar no campo 8 – julho o valor contido no campo 10 \(VLR\_VERBA\) da SAFX212 para a competência de julho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX212\)\. 

No caso da SAFX53/__X530\_RETIFICACAO\_IRRF__ a informação deve ser recuperada da seguinte maneira:

- Para o registro RTRT: ver campo 14 \- VLR\_BRUTO e campo 43 \- VLR\_OUTROS\_TRIB\_EXCL da SAFX53 ou __X530\_RETIFICACAO\_IRRF__, observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.
- Para os registros __RTPO, RTDP__ e ver os seguintes campos da SAFX53 ou __X530\_RETIFICACAO\_IRRF__\.
	- RTPO: campo 41 \- VLR\_DED\_INSS\_TERC
	- RTPP: campo 29 \- VLR\_PREV\_PRIVADA
	- RTDP: campo 42 \- VLR\_DED\_DEP\_TERC
	- RTPA: campo 30 \- VLR\_PENS\_ALIMENT
- __\[ALTERAÇÃO MFS\-594253\] __RTDS: campo 105\- VLR\_DESC\_SIMPL\_MENSAL da SAFX53 
- Para o registro __RTIRF__: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou __X530\_RETIFICACAO\_IRRF__\.

OS3528

OS3267\-D CH2967\_2012

CH5171\_2013

MFS\-8800

MFS\-90689

MFS\-594253

<a id="_Toc49779774"></a>RN47

__Registro RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTDS, RTIRF, ESPP, ESFA, ESSP, ESEP, ESPA:__

Gravar no __campo 9 – agosto__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Agosto \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\. 

- Para os registros __RTPP, RTFA, RTSP, RTEP, ESPP, ESFA, ESSP, ESEP__ gravar no campo 9 – agosto o valor contido no campo 12 da SAFX207 para a competência de agosto \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX207\)\. 
- Para os registros __RTPA, ESPA__ gravar no campo 9 – agosto o valor contido no campo 10 \(VLR\_VERBA\) da SAFX212 para a competência de Agosto \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX212\)\. 

No caso da SAFX53/__X530\_RETIFICACAO\_IRRF__ a informação deve ser recuperada da seguinte maneira:

- Para o registro __RTRT__: ver campo 14 \- VLR\_BRUTO e campo 43 \- VLR\_OUTROS\_TRIB\_EXCL da SAFX53 ou __X530\_RETIFICACAO\_IRRF__, observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.
- Para os registros __RTPO, RTDP__ e ver os seguintes campos da SAFX53 ou __X530\_RETIFICACAO\_IRRF__\.
	- RTPO: campo 41 \- VLR\_DED\_INSS\_TERC
	- RTPP: campo 29 \- VLR\_PREV\_PRIVADA
	- RTDP: campo 42 \- VLR\_DED\_DEP\_TERC
	- RTPA: campo 30 \- VLR\_PENS\_ALIMENT
- __\[ALTERAÇÃO MFS\-594253\] __RTDS: campo 105\- VLR\_DESC\_SIMPL\_MENSAL da SAFX53 
- Para o registro __RTIRF__: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou __X530\_RETIFICACAO\_IRRF\.__

OS3528

OS3267\-D CH2967\_2012

CH5171\_2013

MFS\-8800

MFS\-90689

MFS\-594253

<a id="_Toc49779775"></a>RN48

__Registro RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTDS, RTIRF, ESPP, ESFA, ESSP, ESEP, ESPA:__

Gravar no __campo 10 – setembro__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de setembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\. 

- Para os registros __RTPP, RTFA, RTSP, RTEP, ESPP, ESFA, ESSP, ESEP__ gravar no campo 10 – setembro o valor contido no campo 12 da SAFX207 para a competência de setembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX207\)\. 
- Para os registros __RTPA, ESPA__ gravar no campo 10 – setembro o valor contido no campo 10 \(VLR\_VERBA\) da SAFX212 para a competência de Setembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX212\)\. 

No caso da SAFX53/__X530\_RETIFICACAO\_IRRF__ a informação deve ser recuperada da seguinte maneira:

- Para o registro __RTRT__: ver campo 14 \- VLR\_BRUTO e campo 43 \- VLR\_OUTROS\_TRIB\_EXCL da SAFX53 ou __X530\_RETIFICACAO\_IRRF__, observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.
- Para os registros __RTPO, RTDP__ e ver os seguintes campos da SAFX53 ou __X530\_RETIFICACAO\_IRRF__\.
	- RTPO: campo 41 \- VLR\_DED\_INSS\_TERC
	- RTPP: campo 29 \- VLR\_PREV\_PRIVADA
	- RTDP: campo 42 \- VLR\_DED\_DEP\_TERC
	- RTPA: campo 30 \- VLR\_PENS\_ALIMENT
- __\[ALTERAÇÃO MFS\-594253\] __RTDS: campo 105\- VLR\_DESC\_SIMPL\_MENSAL da SAFX53 
- Para o registro __RTIRF__: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou __X530\_RETIFICACAO\_IRRF\.__

OS3528

OS3267\-D CH2967\_2012

CH5171\_2013

MFS\-8800

MFS\-90689

MFS\-594253

<a id="_Toc49779776"></a>RN49

__Registro RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTDS, RTIRF, ESPP, ESFA, ESSP, ESEP, ESPA:__

Gravar no __campo 11 – outubro__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Outubro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\. 

- Para os registros __RTPP, RTFA, RTSP, RTEP, ESPP, ESFA, ESSP, ESEP__ gravar no campo 11 – outubro o valor contido no campo 12 da SAFX207 para a competência de Outubro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX207\)\. 
- Para os registros __RTPA, ESPA__ gravar no campo 11 – outubro o valor contido no campo 10 \(VLR\_VERBA\) da SAFX212 para a competência de outubro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX212\)\. 

No caso da SAFX53/__X530\_RETIFICACAO\_IRRF__ a informação deve ser recuperada da seguinte maneira:

- Para o __registro RTRT__: ver campo 14 \- VLR\_BRUTO e campo 43 \- VLR\_OUTROS\_TRIB\_EXCL da SAFX53 ou __X530\_RETIFICACAO\_IRRF__, observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.
- Para os registros __RTPO, RTDP__ e ver os seguintes campos da SAFX53 ou __X530\_RETIFICACAO\_IRRF__\.
	- RTPO: campo 41 \- VLR\_DED\_INSS\_TERC
	- RTPP: campo 29 \- VLR\_PREV\_PRIVADA
	- RTDP: campo 42 \- VLR\_DED\_DEP\_TERC
	- RTPA: campo 30 \- VLR\_PENS\_ALIMENT
- __\[ALTERAÇÃO MFS\-594253\] __RTDS: campo 105\- VLR\_DESC\_SIMPL\_MENSAL da SAFX53 
- Para o registro __RTIRF__: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou __X530\_RETIFICACAO\_IRRF__\.

OS3528

OS3267\-D CH2967\_2012

CH5171\_2013

MFS\-8800

MFS\-90689

MFS\-594253

<a id="_Toc49779777"></a>RN50

__Registro RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTDS,RTIRF, ESPP, ESFA, ESSP, ESEP, ESPA:__

Gravar no __campo 12 – Novembro__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  para a competência de Novembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\. 

- Para os registros __RTPP, RTFA, RTSP, RTEP, ESPP, ESFA, ESSP, ESEP__ gravar no campo 12 – Novembro o valor contido no campo 12 da SAFX207 para a competência de Novembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX207\)\. 
- Para os registros __RTPA, ESPA__ gravar no campo 12 – Novembro o valor contido no campo 10 \(VLR\_VERBA\) da SAFX212 para a competência de Novembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX212\)\. 

No caso da SAFX53/__X530\_RETIFICACAO\_IRRF__ a informação deve ser recuperada da seguinte maneira:

- Para o registro __RTRT__: ver campo 14 \- VLR\_BRUTO e campo 43 \- VLR\_OUTROS\_TRIB\_EXCL da SAFX53 ou __X530\_RETIFICACAO\_IRRF__, observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.
- Para os registros __RTPO, RTDP__ e ver os seguintes campos da SAFX53 ou __X530\_RETIFICACAO\_IRRF__\.
	- RTPO: campo 41 \- VLR\_DED\_INSS\_TERC
	- RTPP: campo 29 \- VLR\_PREV\_PRIVADA
	- RTDP: campo 42 \- VLR\_DED\_DEP\_TERC
	- RTPA: campo 30 \- VLR\_PENS\_ALIMENT
- __\[ALTERAÇÃO MFS\-594253\] __RTDS: campo 105\- VLR\_DESC\_SIMPL\_MENSAL da SAFX53 
- Para o registro __RTIRF__: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou __X530\_RETIFICACAO\_IRRF__\.

OS3528

OS3267\-D CH2967\_2012

CH5171\_2013

MFS\-8800

MFS\-90689

MFS\-594253

<a id="_Toc49779778"></a>RN51

__Registro RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTDS,RTIRF, ESPP, ESFA, ESSP, ESEP, ESPA:__

Gravar no __campo 13 – Dezembro__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  para a competência de Dezembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\. 

- Para os registros __RTPP, RTFA, RTSP, RTEP, ESPP, ESFA, ESSP, ESEP__ gravar no campo 13 – Dezembro o valor contido no campo 12 da SAFX207 para a competência de Dezembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX207\)\. 
- Para os registros __RTPA, ESPA__ gravar no campo 13 – Dezembro o valor contido no campo 10 \(VLR\_VERBA\) da SAFX212 para a competência de Dezembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX212\)\. 

No caso da SAFX53/__X530\_RETIFICACAO\_IRRF__ a informação deve ser recuperada da seguinte maneira:

- Para o registro __RTRT__: ver campo 14 \- VLR\_BRUTO e campo 43 \- VLR\_OUTROS\_TRIB\_EXCL da SAFX53 ou __X530\_RETIFICACAO\_IRRF__, observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.
- Para os registros __RTPO, RTDP__ e ver os seguintes campos da SAFX53 ou __X530\_RETIFICACAO\_IRRF__\.
	- RTPO: campo 41 \- VLR\_DED\_INSS\_TERC
	- RTPP: campo 29 \- VLR\_PREV\_PRIVADA
	- RTDP: campo 42 \- VLR\_DED\_DEP\_TERC
	- RTPA: campo 30 \- VLR\_PENS\_ALIMENT
- __\[ALTERAÇÃO MFS\-594253\] __RTDS: campo 105\- VLR\_DESC\_SIMPL\_MENSAL da SAFX53 
- Para o registro __RTIRF__: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou __X530\_RETIFICACAO\_IRRF\.__

OS3528

OS3267\-D CH2967\_2012

CH5171\_2013

MFS\-8800

MFS\-90689

MFS\-594253

<a id="_Toc49779779"></a>RN52

__Registro RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTDS,RTIRF, ESPP, ESFA, ESSP, ESEP, ESPA:__

Gravar no __campo 14 – Décimo Terceiro__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 \. Para identificar o Décimo Terceiro Salário, o campo 06 \(IND\_FOLHA\) da SAFX21 deve estar preenchido com a opção “Pagamento de 13º\. Salário”\. 

- Para os registros __RTPP, RTFA, RTSP, RTEP, ESPP, ESFA, ESSP, ESEP__ gravar no campo 14 – Décimo Terceiro o valor contido no campo 12 da SAFX207\. 
- Para os registros __RTPA, ESPA__ gravar no campo 14 – Décimo Terceiro o valor contido no campo 10 \(VLR\_VERBA\) da SAFX212\. Para identificar o Décimo Terceiro Salário, o campo 06 \(IND\_FOLHA\) da SAFX21 deve estar preenchido com a opção “Pagamento de 13º\. Salário”\. 

No caso da SAFX53/__X530\_RETIFICACAO\_IRRF__ a informação deve ser recuperada da seguinte maneira:

- Para o registro __RTRT__: ver campo 46 \(VLR\_SALARIO\_13 \) da SAFX53 ou __X530\_RETIFICACAO\_IRRF\.__
- Para os registros __RTPO, RTDP__ e ver os seguintes campos da SAFX53 ou __X530\_RETIFICACAO\_IRRF__\.
	- RTPO: campo 41 \- VLR\_DED\_INSS\_TERC
	- RTPP: campo 29 \- VLR\_PREV\_PRIVADA
	- RTDP: campo 42 \- VLR\_DED\_DEP\_TERC
	- RTPA: campo 30 \- VLR\_PENS\_ALIMENT
- __\[ALTERAÇÃO MFS\-594253\] __RTDS: campo 105\- VLR\_DESC\_SIMPL\_MENSAL da SAFX53 
- Para o registro __RTIRF__: ver campo 47 \(VLR\_TRIBUTO\_13\) da SAFX53 ou __X530\_RETIFICACAO\_IRRF\.__

OS3528

OS3267\-D

MFS\-8800

MFS\-90689

MFS\-594253

## <a id="_Toc49805180"></a><a id="_Toc49805298"></a><a id="_Toc49805410"></a><a id="_Toc50402987"></a><a id="_Toc50403111"></a><a id="_Toc50404650"></a><a id="_Toc155171981"></a><a id="_Toc49803550"></a>3\.7 – RTRT – Rendimentos Tributáveis \- Rendimento Tributável

<a id="_Toc49779785"></a>RN58

__Registro RTRT:__

Gravar no __campo 1 – Identificador do Registro__ o valor fixo “__RTRT__”\.

OS3528

<a id="_Toc49779786"></a>RN59

__Registro RTRT:__

Gravar no __campo 2 – Janeiro__ o valor contido no campo VLR\_BRUTO e VLR\_OUTROS\_TRIB\_EXCL da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Janeiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\), observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\. 

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

CH2967\_2013

CH5171\_2013

MFS\-90689

RN59\.a

__\[ALTERAÇÃO\-28168/2006\-MFS81146\] __Tratamento de valores “Triplicados”, devido importação dos valores separados na SAFX53 do Código Retenção 5952 \- PCC__ __

__Tratamento:__

Caso o sistema identificar um segundo registros com as chaves abaixo:

    \- Campo Empresa da tabela SAFX53;

    \- Campo Estabelecimento da tabela SAFX53;  

    \- Campo CPF\_CGC da tabela SAFX04;

    \- Campo Código da Receita da tabela SAFX53;

    \- Campo Data movimento da tabela SAFX53;

    \- Campo Num\_docfis da tabela SAFX53;

    \- Campo Serie\_docfis da tabela SAFX53;

    \- Campo Sub\_serie\_docfis da tabela SAFX53\.

 

__ Se__ as chaves acima for verdadeiro, considerar somente o valor bruto e valor de dedução do primeiro registro \(lido\) e desconsiderar os valores de Valor Bruto e Valor de Retenção dos demais registros e continuar somando o valor de imposto retido\.

“Tratamento implementado em a*tendimento ao chamado 28168/2006 para o cliente Alcoa, para contornar o problema de valores ‘Triplicado’, devido alguns ERP’s calcular e informar as retenções separadamente, desta forma um documento onde haja incidência dos 3 impostos \(PIS/COFNIS/CSLL\), passa a gerar automaticamente os três registros de retenção na SAFX53 para uma mesma Nota Fiscal*”, nesse cenário o sistema __não irá somar__ o Campo de Valor Bruto e Valor de Dedução e continuará somando o Valor do Imposto Retido\.

<a id="_Toc49779787"></a>RN60

__Registro RTRT:__

Gravar no __campo 3 – Fevereiro__ o valor contido no campo VLR\_BRUTO e VLR\_OUTROS\_TRIB\_EXCL da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Fevereiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\), observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D CH2967\_2013

CH5171\_2013

MFS\-90689

<a id="_Toc49779788"></a>RN61

__Registro RTRT:__

Gravar no __campo 4 – Março__ o valor contido no campo VLR\_BRUTO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Março \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\), observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D CH2967\_2013

CH5171\_2013

MFS\-90689

<a id="_Toc49779789"></a>RN62

__Registro RTRT:__

Gravar no __campo 5 – Abril __o valor contido no campo VLR\_BRUTO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Abril \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\), observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D CH2967\_2013

CH5171\_2013

MFS\-90689

<a id="_Toc49779790"></a>RN63

__Registro RTRT:__

Gravar no __campo 6 – Maio__ o valor contido no campo VLR\_BRUTO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Maio \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\), observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D CH2967\_2013

CH5171\_2013

MFS\-90689

<a id="_Toc49779791"></a>RN64

__Registro RTRT:__

Gravar no __campo 7 – Junho__ o valor contido no campo VLR\_BRUTO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Junho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\), observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D CH2967\_2013

CH5171\_2013

MFS\-90689

<a id="_Toc49779792"></a>RN65

__Registro RTRT:__

Gravar no __campo 8 – Julho__ o valor contido no campo VLR\_BRUTO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Julho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\), observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D CH2967\_2013

CH5171\_2013

MFS\-90689

<a id="_Toc49779793"></a>RN66

__Registro RTRT:__

Gravar no __campo 9 – Agosto__ o valor contido no campo VLR\_BRUTO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Agosto \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\), observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\. 

OS3528

OS3267\-D CH2967\_2013

CH5171\_2013

MFS\-90689

<a id="_Toc49779794"></a>RN67

__Registro RTRT:__

Gravar no __campo 10 – Setembro__ o valor contido no campo VLR\_BRUTO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Setembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\), observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\. 

OS3528

OS3267\-D CH2967\_2013

CH5171\_2013

MFS\-90689

<a id="_Toc49779795"></a>RN68

__Registro RTRT:__

Gravar no __campo 11 – Outubro__ o valor contido no campo VLR\_BRUTO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Outubro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\), observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D CH2967\_2013

CH5171\_2013

MFS\-90689

<a id="_Toc49779796"></a>RN69

__Registro RTRT:__

Gravar no __campo 12 – Novembro__ o valor contido no campo VLR\_BRUTO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Novembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\), observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D CH2967\_2013

CH5171\_2013

MFS\-90689

<a id="_Toc49779797"></a>RN70

__Registro RTRT:__

Gravar no __campo 13 – Dezembro__ o valor contido no campo VLR\_BRUTO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Dezembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\), observando a regra geral referente ao campo da Aposentadoria Isenta da RN39\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D CH2967\_2013

CH5171\_2013

MFS\-90689

<a id="_Toc49779798"></a>RN71

__Registro RTRT:__

Gravar no __campo 14 – Décimo Terceiro __o valor contido no campo “Valor 13º\. Salário” da SAFX53/__X530\_RETIFICACAO\_IRRF__\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

MFS\-90689

## <a id="_Toc49805181"></a><a id="_Toc49805299"></a><a id="_Toc49805411"></a><a id="_Toc50402988"></a><a id="_Toc50403112"></a><a id="_Toc50404651"></a><a id="_Toc155171982"></a>3\.8 – RTIRF \- Rendimentos Tributáveis \- Imposto sobre a Renda Retido na Fonte

<a id="_Toc49779799"></a>RN72

__Registro RTIRF:__

Gravar no __campo 1 – Identificador do Registro__ o valor fixo “__RTIRF__”\.

OS3528 OS3267\-D

<a id="_Toc49779800"></a>RN73

__Registro RTIRF:__

Gravar no __campo 2 – Janeiro__ o valor contido no campo VLR\_IR\_RETIDO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Janeiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779801"></a>RN74

__Registro RTIRF: __

Gravar no __campo 3 – Fevereiro__ o valor contido no campo VLR\_IR\_RETIDO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Fevereiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779802"></a>RN75

__Registro RTIRF:__

Gravar no __campo 4 – Março__ o valor contido no campo VLR\_IR\_RETIDO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Março \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779803"></a>RN76

__Registro RTIRF:__

Gravar no __campo 5 – Abril__ o valor contido no campo VLR\_IR\_RETIDO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Abril \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779804"></a>RN77

__Registro RTIRF:__

Gravar no __campo 6 – Maio__ o valor contido no campo VLR\_IR\_RETIDO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Maio \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779805"></a>RN78

__Registro RTIRF:__

Gravar no __campo 7 – Junho__ o valor contido no campo VLR\_IR\_RETIDO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Junho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779806"></a>RN79

__Registro RTIRF:__

Gravar no __campo 8 – Julho__ o valor contido no campo VLR\_IR\_RETIDO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Julho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779807"></a>RN80

__Registro RTIRF:__

Gravar no __campo 9 – Agosto__ o valor contido no campo VLR\_IR\_RETIDO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Agosto \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779808"></a>RN81

__Registro RTIRF:__

Gravar no __campo 10 – Setembro__ o valor contido no campo VLR\_IR\_RETIDO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Setembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779809"></a>RN82

__Registro RTIRF:__

Gravar no __campo 11 – Outubro__ o valor contido no campo VLR\_IR\_RETIDO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Outubro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779810"></a>RN83

__Registro RTIRF:__

Gravar no __campo 12 – Novembro__ o valor contido no campo VLR\_IR\_RETIDO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Novembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779811"></a>RN84

__Registro RTIRF:__

Gravar no __campo 13 – Dezembro__ o valor contido no campo VLR\_IR\_RETIDO da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Novembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779812"></a>RN85

__Registro RTIRF:__

Gravar no __campo 14 – Décimo Terceiro__ o valor contido no campo 47 \(VLR\_TRIBUTO\_13\) da SAFX53 /__X530\_RETIFICACAO\_IRRF__\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/__X530\_RETIFICACAO\_IRRF__\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc50402989"></a><a id="_Toc50403113"></a><a id="_Toc50404652"></a>

## <a id="_Toc155171983"></a>3\.9 – Registro CJAC,CJAA

__CJAC__ \- Compensação de Imposto por Decisão Judicial \- Ano\-calendário 

__CJAA __\- Compensação de Imposto por Decisão Judicial \- Anos Anteriores

<a id="_Toc49779917"></a>RN178

<a id="_Hlk113979625"></a>__Registro CJAC__

Gravar no __campo 1 – Identificador__ do Registro o valor fixo “__CJAC__”\.

O registro CJAC corresponde a um registro BPFDEC correspondente, logo deverão ser recuperadas as Fichas Financeiras \(SAFX21\) e as Retenções do período \(SAFX53/__X530\_RETIFICACAO\_IRRF__\) dos Beneficiários – pessoas físicas – cujo campo Tipo Lançamento = Beneficiários com valores de imposto compensados em virtude de decisão judicial – ano calendário\. Nos casos em que a informação for oriunda da SAFX21, verificar o código da verba \(campo 07\) e verificar se na Parametrização por Verba \(menu: Parâmetros >> Parâmetros p/ Verba \(Folha de Pagamento\) o campo “Classe DIRF” = “Imposto de Renda Retido”\.

Caso o registro da SAFX53 possua uma ou mais retificações na tabela __X530\_RETIFICACAO\_IRRF__, deverá ser recuperado o registro mais recente dessa tabela\.

O valor compensado em virtude da decisão judicial já vai ser informado nesse registro além do campo respectivo ao mesmo Beneficiário no registro RTIRF também já vir com a informação correta\.

*Exemplo*: caso se tenha um valor a ser compensado de R$ 1\.000,00 e o valor retido no mês foi de R$ 1\.000,00, o registro RTIRF será informado com o valor R$ 0,00 e o registro CJAC com valor R$ 1\.000,00\. Caso o valor da compensação seja maior, o valor do imposto retido RTIRF será zerado e a sobra do crédito \(a ser utilizado no CJAC\) deverá ser utilizada em outro mês\. Caso o valor da compensação seja menor, o valor do RTIRF será diminuído até o valor máximo da compensação, e o CJAC será informado com o valor creditado\.

OBS: vale salientar que as verbas informadas no campo 07 da SAFX21 deverão seguir a regra previamente existente de que as verbas classificadas como “Desconto” deverão ser subtraídas, enquanto as verbas classificadas como “Proventos” deverão ser somadas\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779918"></a>RN179

__Registro CJAC__

Gravar no __campo 2 – Janeiro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Janeiro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 para a competência de Janeiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779919"></a>RN180

__Registro CJAC__

Gravar no __campo 3 – Fevereiro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  para a competência de Fevereiro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 para a competência de Fevereiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

<a id="_Toc49779920"></a>RN181

__Registro CJAC__

Gravar no __campo 4 – Março:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  para a competência de Março \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 para a competência de Março \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779921"></a>RN182

__Registro CJAC__

Gravar no __campo 5 – Abril:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  para a competência de Abril \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 para a competência de Abril \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779922"></a>RN183

__Registro CJAC__

Gravar no __campo 6 – Maio:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  para a competência de Maio \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 para a competência de Maio \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779923"></a>RN184

__Registro CJAC__

Gravar no __campo 7 – Junho:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  para a competência de Junho \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 para a competência de Junho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779924"></a>RN185

__Registro CJAC__

Gravar no __campo 8 – Julho:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  para a competência de Julho \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 para a competência de Julho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779925"></a>RN186

__Registro CJAC__

Gravar no __campo 9 – Agosto:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  para a competência de Agosto \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 para a competência de Agosto \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779926"></a>RN187

__Registro CJAC__

Gravar no __campo 10 – Setembro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  para a competência de Setembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 para a competência de Setembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779927"></a>RN188

__Registro CJAC__

Gravar no __campo 11 – Outubro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  para a competência de Outubro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 para a competência de Outubro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779928"></a>RN189

__Registro CJAC__

Gravar no __campo 12 – Novembro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  para a competência de Novembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 para a competência de Novembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779929"></a>RN190

__Registro CJAC__

Gravar no __campo 13 – Dezembro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  para a competência de Dezembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 para a competência de Dezembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779930"></a>RN191

__Registro CJAC__

Gravar no __campo 14 – Décimo Terceiro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  desde que o campo “Indicador da Folha” \(campo 06 da SAFX21\) seja “Pagamento de 13º\. Salário”\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 47 \(VLR\_TRIBUTO\_13\) da SAFX53\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779931"></a>RN192

__Registro CJAA__

Gravar no __campo 1 – Identificador__ do Registro o valor fixo “__CJAA__”\.

O registro CJAA corresponde a um registro BPFDEC correspondente, logo deverão ser recuperadas as Fichas Financeiras \(SAFX21\) e as Retenções do período \(SAFX53/__X530\_RETIFICACAO\_IRRF__\) dos Beneficiários – pessoas físicas – cujo campo Tipo Lançamento = Beneficiários com valores de imposto compensados em virtude de decisão judicial – anos anteriores\. Nos casos em que a informação for oriunda da SAFX21, verificar o código da verba \(campo 07\) e verificar se na Parametrização por Verba \(menu: Parâmetros >> Parâmetros p/ Verba \(Folha de Pagamento\) o campo “Classe DIRF” = “Imposto de Renda Retido”\.

Caso o registro da SAFX53 possua uma ou mais retificações na tabela __X530\_RETIFICACAO\_IRRF__, deverá ser recuperado o registro mais recente dessa tabela\.

O valor compensado em virtude da decisão judicial já vai ser informado nesse registro além do campo respectivo ao mesmo Beneficiário no registro RTIRF também já vir com a informação correta\.

*Exemplo*: caso se tenha um valor a ser compensado de R$ 1\.000,00 e o valor retido no mês foi de R$ 1\.000,00, o registro RTIRF será informado com o valor R$ 0,00 e o registro CJAC com valor R$ 1\.000,00\. Caso o valor da compensação seja maior, o valor do imposto retido RTIRF será zerado e a sobra do crédito \(a ser utilizado no CJAC\) deverá ser utilizada em outro mês\. Caso o valor da compensação seja menor, o valor do RTIRF será diminuído até o valor máximo da compensação, e o CJAC será informado com o valor creditado\.

OBS: vale salientar que as verbas informadas no campo 07 da SAFX21 deverão seguir a regra previamente existente de que as verbas classificadas como “Desconto” deverão ser subtraídas, enquanto as verbas classificadas como “Proventos” deverão ser somadas\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779932"></a>RN193

__Registro CJAA__

Gravar no __campo 2 – Janeiro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  para a competência de Janeiro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53para a competência de Janeiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779933"></a>RN194

__Registro CJAA__

Gravar no __campo 3 – Fevereiro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  para a competência de Fevereiro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53para a competência de Fevereiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779934"></a>RN195

__Registro CJAA__

Gravar no __campo 4 – Março:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Março \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53para a competência de Março \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779935"></a>RN196

__Registro CJAA__

Gravar no __campo 5 – Abril:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  para a competência de Abril \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53para a competência de Abril \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779936"></a>RN197

__Registro CJAA__

Gravar no __campo 6 – Maio:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  para a competência de Maio \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53para a competência de Maio \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779937"></a>RN198

__Registro CJAA__

Gravar no __campo 7 – Junho:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Junho \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53para a competência de Junho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779938"></a>RN199

__Registro CJAA__

Gravar no __campo 8 – Julho:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Julho \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53para a competência de Julho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779939"></a>RN200

__Registro CJAA__

Gravar no __campo 9 – Agosto:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Agosto \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53para a competência de Agosto \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779940"></a>RN201

__Registro CJAA__

Gravar no __campo 10 – Setembro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Setembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53para a competência de Setembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779941"></a>RN202

__Registro CJAA__

Gravar no __campo 11 – Outubro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Outubro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53; /__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53para a competência de Outubro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779942"></a>RN203

__Registro CJAA__

Gravar no __campo 12 – Novembro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Novembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53para a competência de Novembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779943"></a>RN204

__Registro CJAA__

Gravar no __campo 13 – Dezembro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Dezembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 15 \(VLR\_IR\_RETIDO\) da SAFX53para a competência de Dezembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779944"></a>RN205

__Registro CJAA__

Gravar no __campo 14 – Décimo Terceiro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21  desde que o campo 06 \(IND\_FOLHA\) da SAFX21 seja “Pagamento de 13º\. Salário”\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo 47 \(VLR\_TRIBUTO\_13\) da SAFX53\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

## <a id="_Toc49805182"></a><a id="_Toc49805300"></a><a id="_Toc49805412"></a><a id="_Toc50402990"></a><a id="_Toc50403114"></a><a id="_Toc50404653"></a><a id="_Toc155171984"></a>3\.10 – Registros ESRT, ESPO, ESPP, ESDP, ESDS, ESPA, ESIR, ESDJ

ESRT \- Tributação com Exigibilidade Suspensa \- Rendimento Tributável 

ESPO \- Tributação com Exigibilidade Suspensa \- Dedução \- Previdência Oficial 

ESPP \- Tributação com Exigibilidade Suspensa \- Dedução \- Previdência Privada

ESDP \- Tributação com Exigibilidade Suspensa \- Dedução \- Dependentes 

ESPA \- Tributação com Exigibilidade Suspensa \- Dedução \- Pensão Alimentícia

ESDS \- Tributação com Exigibilidade Suspensa \- Dedução – Desconto Simplificado Mensal

ESIR  \- Tributação com Exigibilidade Suspensa \- Imposto sobre a Renda na Fonte 

ESDJ \- Tributação com Exigibilidade Suspensa \- Depósito Judicial

<a id="_Toc49779817"></a>RN90

__Registro ESRT, ESPO, ESPP, ESDP, ESPA, ESIR__

Devem ser recuperados as fichas financeiras \(tabela X21\_FICHA\_FINANC\) e as retenções \(X53\_RETENCAO\_IRRF ou __X530\_RETIFICACAO\_IRRF__\) dos funcionários e dos prestadores que estejam no período informado para a geração\. 

Caso um funcionário não possua valores para retenção de Imposto de Renda no período para nenhum mês ou Décimo Terceiro Salário, o mesmo não deverá ser informado\.

No caso da SAFX53 ou __X530\_RETIFICACAO\_IRRF__ deverão ser recuperados somente os beneficiários que forem PESSOA FÍSICA\.

As retenções da tabela X53\_RETENCAO\_IRRF, cujos campos “Estorno” e “Data do Estorno” estiverem preenchidos, não deverão ser consideradas para a geração da DIRF\. Vale salientar que essas retenções não possuem registros de retificação\.

Gravar no campo 1 – Identificador do Registro a informação de acordo com as regras abaixo:

- Gravar o valor fixo “__ESRT__” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha no campo 11 \(IND\_TP\_LANCTO\_DIRF\) a opção selecionada “Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa e quando a verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Rendimentos Tributáveis”\. No caso da SAFX53, recuperar a informação a partir da somatória dos campos VLR\_BRUTO e VLR\_OUTROS\_TRIB\_EXCL da SAFX53 ou __X530\_RETIFICACAO\_IRRF__ mais recente \(vide __RNG\-01__\)\.
- Gravar o valor fixo “__ESPO__” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha no campo 11 \(IND\_TP\_LANCTO\_DIRF\) a opção selecionada “Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa e quando a verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Previdência Oficial\)”\. No caso da SAFX53, recuperar a informação do campo VLR\_DED\_INSS\_TERC da SAFX53 ou __X530\_RETIFICACAO\_IRRF__ mais recente\.
- <a id="OLE_LINK8"></a><a id="OLE_LINK9"></a><a id="OLE_LINK10"></a>Gravar o valor fixo “__ESPP__” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha no campo 11 \(IND\_TP\_LANCTO\_DIRF\) a opção selecionada “Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e quando o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Previdência Privada/FAPI\)”\. No caso da SAFX53, recuperar a informação do campo VLR\_PREV\_PRIVADA da SAFX53 ou __X530\_RETIFICACAO\_IRRF__ mais recente\.
- Gravar o valor fixo “__ESDP__” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha no campo 11 \(IND\_TP\_LANCTO\_DIRF\) a opção selecionada “Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e caso a verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Dependentes\)”\. No caso da SAFX53, recuperar a informação do campo VLR\_DED\_DEP\_TERC da SAFX53 ou __X530\_RETIFICACAO\_IRRF__ mais recente\.
- Gravar o valor fixo “__ESPA__” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha no campo 11 \(IND\_TP\_LANCTO\_DIRF\) a opção selecionada “Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e caso a verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Pensão Alimentícia\)”\. No caso da SAFX53, recuperar a informação do campo VLR\_PENS\_ALIMENT da SAFX53 ou __X530\_RETIFICACAO\_IRRF__ mais recente\.
- <a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a>Gravar o valor fixo “__ESIR__” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha no campo 11 \(IND\_TP\_LANCTO\_DIRF\) a opção selecionada “Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e caso a verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Imposto de Renda Retido”\. No caso da SAFX53, recuperar a informação do campo VLR\_IR\_RETIDO da SAFX53 ou __X530\_RETIFICACAO\_IRRF__ mais recente\.

OS3528

OS3267\-D

CH5171\_2013

MFS\-90689

RN91

__Registro ESDS__

Gravar no __campo 1 – Identificador__ do Registro o valor fixo “__ESDS__”\.

Gravar o valor fixo “__ESDS__” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração possuir o campo 11 \(IND\_TP\_LANCTO\_DIRF\) preenchido com a opção “2 \- Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e a verba informada \(campo 07 da SAFX21\) estiver com o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais  preenchido com a opção “Deduções \(Desconto Simplificado Mensal\)”\. No caso da SAFX534, recuperar a informação do campo VLR\_DED\_EXIG\_SUSP da, quando o IND\_TP\_DEDUCAO for igual a “8 \- Desconto Simplificado Mensal”\.

MFS\-594253

RN92 

__Registro ESDS__

Gravar no __campo 2 – janeiro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Janeiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21, quando o campo 11 \(IND\_TP\_LANCTO\_DIRF\) estiver preenchido com a opção “2 \- Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e a verba \(campo 07 da SAFX21\) com o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais, preenchido com a opção “Deduções \(Desconto Simplificado Mensal\)”\.
- SAFX534 
	- Considerando a competência de janeiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\), da SAFX53, gravar a informação do campo VLR\_DED\_EXIG\_SUSP da SAFX534, quando o IND\_TP\_DEDUCAO for igual a “8 \- Desconto Simplificado Mensal”\. 

MFS\-594253

RN93 

__Registro ESDS__

Gravar no __campo 3 – fevereiro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Fevereiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21, quando o campo 11 \(IND\_TP\_LANCTO\_DIRF\) estiver preenchido com a opção “2 \- Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e a verba \(campo 07 da SAFX21\) com o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais, preenchido com a opção “Deduções \(Desconto Simplificado Mensal\)”\.
- SAFX534 
	- Considerando a competência de fevereiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\), da SAFX53, gravar a informação do campo VLR\_DED\_EXIG\_SUSP da SAFX534, quando o IND\_TP\_DEDUCAO for igual a “8 \- Desconto Simplificado Mensal”\.

MFS\-594253

RN94

__Registro ESDS__

Gravar no __campo 4 – março__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de março \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21, quando o campo 11 \(IND\_TP\_LANCTO\_DIRF\) estiver preenchido com a opção “2 \- Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e a verba \(campo 07 da SAFX21\) com o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais, preenchido com a opção “Deduções \(Desconto Simplificado Mensal\)”\.
- SAFX534 
	- Considerando a competência de março \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\), da SAFX53, gravar a informação do campo VLR\_DED\_EXIG\_SUSP da SAFX534, quando o IND\_TP\_DEDUCAO for igual a “8 \- Desconto Simplificado Mensal”\.

MFS\-594253

RN95

__Registro ESDS__

Gravar no __campo 5 – abril__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de abril \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21, quando o campo 11 \(IND\_TP\_LANCTO\_DIRF\) estiver  preenchido com a opção “2 \- Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e a verba \(campo 07 da SAFX21\) com o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais, preenchido com a opção “Deduções \(Desconto Simplificado Mensal\)”\.
- SAFX534 
	- Considerando a competência de abril \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\), da SAFX53, gravar a informação do campo VLR\_DED\_EXIG\_SUSP da SAFX534, quando o IND\_TP\_DEDUCAO for igual a “8 \- Desconto Simplificado Mensal”\.

MFS\-594253

RN96

__Registro ESDS__

Gravar no __campo 6 – maio__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de maio \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21, quando o campo 11 \(IND\_TP\_LANCTO\_DIRF\) estiver preenchido com a opção “2 \- Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e a verba \(campo 07 da SAFX21\) com o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais, preenchido com a opção “Deduções \(Desconto Simplificado Mensal\)”\.
- SAFX534 
	- Considerando a competência de maio \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\), da SAFX53, gravar a informação do campo VLR\_DED\_EXIG\_SUSP da SAFX534, quando o IND\_TP\_DEDUCAO for igual a “8 \- Desconto Simplificado Mensal”\.

MFS\-594253

RN97

__Registro ESDS__

Gravar no __campo 7– junho__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de junho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21, quando o campo 11 \(IND\_TP\_LANCTO\_DIRF\) estiver preenchido com a opção “2 \- Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e a verba \(campo 07 da SAFX21\) com o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais, preenchido com a opção “Deduções \(Desconto Simplificado Mensal\)”\.
- SAFX534 
	- Considerando a competência de junho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\), da SAFX53, gravar a informação do campo VLR\_DED\_EXIG\_SUSP da SAFX534, quando o IND\_TP\_DEDUCAO for igual a “8 \- Desconto Simplificado Mensal”\.

MFS\-594253

RN98 

__Registro ESDS__

Gravar no __campo 8 – julho__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de julho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21, quando  o campo 11 \(IND\_TP\_LANCTO\_DIRF\) estiver preenchido com a opção “2 \- Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e a verba \(campo 07 da SAFX21\) com o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais, preenchido com a opção “Deduções \(Desconto Simplificado Mensal\)”\.
- SAFX534 
	- Considerando a competência de julho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\), da SAFX53, gravar a informação do campo VLR\_DED\_EXIG\_SUSP da SAFX534, quando o IND\_TP\_DEDUCAO for igual a “8 \- Desconto Simplificado Mensal”\.

MFS\-594253

RN99

__Registro ESDS__

Gravar no __campo 9 – agosto__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de agosto \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21, quando o campo 11 \(IND\_TP\_LANCTO\_DIRF\) estiver preenchido com a opção “2 \- Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e a verba \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais, preenchido com a opção “Deduções \(Desconto Simplificado Mensal\)”\.
- SAFX534 
	- Considerando a competência de agosto \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\), da SAFX53, gravar a informação do campo VLR\_DED\_EXIG\_SUSP da SAFX534, quando o IND\_TP\_DEDUCAO for igual a “8 \- Desconto Simplificado Mensal”\.

MFS\-594253

RN100

__Registro ESDS__

Gravar no __campo 10 – setembro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de setembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21, quando o campo 11 \(IND\_TP\_LANCTO\_DIRF\) estiver preenchido com a opção “2 \- Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e a verba \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais, preenchido com a opção “Deduções \(Desconto Simplificado Mensal\)”\.
- SAFX534 
	- Considerando a competência de setembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\), da SAFX53, gravar a informação do campo VLR\_DED\_EXIG\_SUSP da SAFX534, quando o IND\_TP\_DEDUCAO for igual a “8 \- Desconto Simplificado Mensal”\.

MFS\-594253

RN101

__Registro ESDS__

Gravar no __campo 11– outubro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de outubro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21, quando o campo 11 \(IND\_TP\_LANCTO\_DIRF\) estiver preenchido com a opção  “2 \- Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e a verba \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais, preenchido com a opção “Deduções \(Desconto Simplificado Mensal\)”\.
- SAFX534 
	- Considerando a competência de outubro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\), da SAFX53, gravar a informação do campo VLR\_DED\_EXIG\_SUSP da SAFX534, quando o IND\_TP\_DEDUCAO for igual a “8 \- Desconto Simplificado Mensal”\.

MFS\-594253

RN102

__Registro ESDS__

Gravar no __campo 12 – novembro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de novembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21, quando  o campo 11 \(IND\_TP\_LANCTO\_DIRF\) estiver preenchido com a opção  “2 \- Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e a verba \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais, preenchido com a opção “Deduções \(Desconto Simplificado Mensal\)”\.
- SAFX534 
	- Considerando a competência de novembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\), da SAFX53, gravar a informação do campo VLR\_DED\_EXIG\_SUSP da SAFX534, quando o IND\_TP\_DEDUCAO for igual a “8 \- Desconto Simplificado Mensal”\.

MFS\-594253

RN103

__Registro ESDS__

Gravar no __campo 13 – dezembro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de dezembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21, quando o campo 11 \(IND\_TP\_LANCTO\_DIRF\) estiver preenchido com a opção “2 \- Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e a verba \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais, preenchido com a opção “Deduções \(Desconto Simplificado Mensal\)”\.
- SAFX534 
	- Considerando a competência de dezembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\), da SAFX53, gravar a informação do campo VLR\_DED\_EXIG\_SUSP da SAFX534, quando o IND\_TP\_DEDUCAO for igual a “8 \- Desconto Simplificado Mensal”\.

MFS\-594253

RN104

__Registro ESDS__

Gravar no __campo 14 – décimo terceiro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21, quando o campo 06 \(IND\_FOLHA\) da SAFX21 estiver preenchido com a opção “Pagamento de 13º\. Salário”, o campo 11 \(IND\_TP\_LANCTO\_DIRF\) preenchido com a opção “2 \- Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e a verba \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais, preenchido com a opção “Deduções \(Desconto Simplificado Mensal\)”\.
- SAFX534 

Considerando o campo 47 \(VLR\_TRIBUTO\_13\)\., da SAFX53 preenchido, gravar a informação do campo VLR\_DED\_EXIG\_SUSP da SAFX534, quando o IND\_TP\_DEDUCAO for igual a “8 \- Desconto Simplificado Mensal”\.

MFS\-594253

<a id="_Toc49779970"></a><a id="_Toc49801972"></a>RN231

__Registro ESDJ__

Gravar no __campo 1 – Identificador__ do Registro o valor fixo “__ESDJ__”\.

- Deverão ser recuperadas as Fichas Financeiras \(SAFX21\) e as Retenções do período \(SAFX53\) – somente para pessoas físicas – cujo campo Tipo Lançamento = Beneficiários do Imposto de Renda retido na fonte com depósito judicial\.
- Quando as informações forem recuperadas das Fichas Financeiras \(SAFX21\), o código da verba \(campo 07 da SAFX21\) deverá estar parametrizado no módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros p/ Verba\) com o campo “Classe DIRF” = “Imposto de Renda Retido”\.

OBS: as verbas oriundas da tabela SAFX21 que estiverem classificadas como “Proventos” devem ser subtraídas, enquanto as verbas classificadas como “Descontos” devem ser somadas\.

OS3528

<a id="_Toc49779971"></a><a id="_Toc49801973"></a>RN232

__Registro ESDJ__

Gravar no __campo 2 – Janeiro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Janeiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Janeiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779972"></a><a id="_Toc49801974"></a>RN233

__Registro ESDJ__

Gravar no __campo 3 – Fevereiro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Fevereiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Fevereiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779973"></a><a id="_Toc49801975"></a>RN234

__Registro ESDJ__

Gravar no __campo 4 – Março__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Março \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Março \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779974"></a><a id="_Toc49801976"></a>RN235

__Registro ESDJ__

Gravar no __campo 5 – Abril__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Abril \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Abril \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779975"></a><a id="_Toc49801977"></a>RN236

__Registro ESDJ__

Gravar no __campo 6 – Maio__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Maio \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Maio \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779976"></a><a id="_Toc49801978"></a>RN237

__Registro ESDJ__

Gravar no __campo 7 – Junho__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Junho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Junho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779977"></a><a id="_Toc49801979"></a>RN238

__Registro ESDJ__

Gravar no __campo 8 – Julho__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Julho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Julho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779978"></a><a id="_Toc49801980"></a>RN239

__Registro ESDJ__

Gravar no __campo 9 – Agosto__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Agosto \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Agosto \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779979"></a><a id="_Toc49801981"></a>RN240

__Registro ESDJ__

Gravar no __campo 10 – Setembro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Setembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Setembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779980"></a><a id="_Toc49801982"></a>RN241

__Registro ESDJ__

Gravar no __campo 11 – Outubro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Outubro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Outubro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779981"></a><a id="_Toc49801983"></a>RN242

__Registro ESDJ__

Gravar no __campo 12 – Novembro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Novembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Novembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779982"></a><a id="_Toc49801984"></a>RN243

__Registro ESDJ__

Gravar no __campo 13 – Dezembro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Dezembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Dezembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779983"></a><a id="_Toc49801985"></a>RN244

__Registro ESDJ__

Gravar no __campo 14 – Décimo Terceiro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21, desde que o campo 06 \(IND\_FOLHA\) da SAFX21 esteja com a opção “Pagamento de 13º\. Salário”\.
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo 47 \(VLR\_TRIBUTO\_13\)\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

RIDAC \- Rendimentos Isentos \- Diária e Ajuda de Custo 

RIIRP \- Rendimentos Isentos \- Indenizações por Rescisão de Contrato de Trabalho, inclusive a título de PDV 

RIAP \- Rendimentos Isentos \- Abono Pecuniário 

RIMOG \- Rendimentos Isentos \- Pensão, Aposentadoria ou Reforma por Moléstia Grave 

RIRPC \- Rendimentos Isentos \- Resgate de previdência complementar por portador de moléstia grave 

RIP65 \- Rendimentos Isentos \- Parcela Isenta de Aposentadoria \(65 anos ou mais\)

<a id="_Toc49779845"></a>RN108

__Registro RIDAC__

Gravar no __campo 1 – Identificador__ do Registro o valor fixo “__RIDAC__”\. Essa informação poderá ser recuperada a partir da Ficha Financeira \(SAFX21\) ou das Retenções \(SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

- SAFX21
	- Deverão ser recuperadas as Fichas Financeiras \(SAFX21\) do período cuja verba \(campo 07 \(COD\_VERBA\) da SAFX21\) esteja parametrizado na Parametrização de Verbas do módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\) = “Isentos \(Diária e Ajuda de Custo\)”\.
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Deverão ser recuperadas as Retenções \(SAFX53\) do período que pertençam à Pessoas Físicas \(campos 04 \(IND\_FIS\_JUR\) e 05 \(COD\_FIS\_JUR\) da SAFX53, desde que o campo 05 pela SAFX04 tenha 11 posições\) e que possuam o Valor de Ajuda de Custo preenchido \(campo VLR\_AJUDA\_CUSTO da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779846"></a>RN109

__Registro RIDAC__

Gravar no __campo 2 – Janeiro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Janeiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Janeiro \(ver campos 12 \(ANO\_COMPETENCIA\) e 13 \(MES\_COMPETENCIA\) da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779847"></a>RN110

__Registro RIDAC__

Gravar no __campo 3 – Fevereiro:__

- SAFX21

O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Fevereiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Janeiro \(ver campos 12 \(ANO\_COMPETENCIA\) e 13 \(MES\_COMPETENCIA\) da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779848"></a>RN111

__Registro RIDAC__

Gravar no __campo 4 – Março:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Março \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Janeiro \(ver campos 12 \(ANO\_COMPETENCIA\) e 13 \(MES\_COMPETENCIA\) da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779849"></a>RN112

__Registro RIDAC__

Gravar no __campo 5 – Abril:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Abril \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Janeiro \(ver campos 12 \(ANO\_COMPETENCIA\) e 13 \(MES\_COMPETENCIA\) da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779850"></a>RN113

__Registro RIDAC__

Gravar no __campo 6 – Maio__:

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Maio \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\.

 

- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Janeiro \(ver campos 12 \(ANO\_COMPETENCIA\) e 13 \(MES\_COMPETENCIA\) da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779851"></a>RN114

__Registro RIDAC__

Gravar no __campo 7 – Junho:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Junho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\.

 

- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Janeiro \(ver campos 12 \(ANO\_COMPETENCIA\) e 13 \(MES\_COMPETENCIA\) da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779852"></a>RN115

__Registro RIDAC__

Gravar no __campo 8 – Julho:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Julho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\.

 

- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Janeiro \(ver campos 12 \(ANO\_COMPETENCIA\) e 13 \(MES\_COMPETENCIA\) da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779853"></a>RN116

__Registro RIDAC__

Gravar no __campo 9 – Agosto:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Agosto \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Janeiro \(ver campos 12 \(ANO\_COMPETENCIA\) e 13 \(MES\_COMPETENCIA\) da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779854"></a>RN117

__Registro RIDAC__

Gravar no __campo 10 – Setembro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Setembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\.
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Janeiro \(ver campos 12 \(ANO\_COMPETENCIA\) e 13 \(MES\_COMPETENCIA\) da SAFX53\) Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779855"></a>RN118

__Registro RIDAC__

Gravar no __campo 11 – Outubro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Outubro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Janeiro \(ver campos 12 \(ANO\_COMPETENCIA\) e 13 \(MES\_COMPETENCIA\) da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779856"></a>RN119

__Registro RIDAC__

Gravar no __campo 12 – Novembro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Novembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Janeiro \(ver campos 12 \(ANO\_COMPETENCIA\) e 13 \(MES\_COMPETENCIA\) da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779857"></a>RN120

__Registro RIDAC__

Gravar no __campo 13 – Dezembro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Dezembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\.

 

- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Janeiro \(ver campos 12 \(ANO\_COMPETENCIA\) e 13 \(MES\_COMPETENCIA\) da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528 OS3267\-D

MFS\-90689

<a id="_Toc49779858"></a>RN121

__Registro RIDAC__

Gravar no __campo 14 – Décimo Terceiro:__

- SAFX21
	- O valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 desde que o campo 06 da SAFX21 = 02 \(Pagamento de 13º\. Salário\)\. 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- O valor contido no campo “Valor 13º\. Salário”\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela __X530\_RETIFICACAO\_IRRF__ mais recente\. Os campos são os mesmos da SAFX53\.

OS3528 OS3267\-D

OS3832\-A

MFS\-90689

<a id="_Toc49779859"></a>RN122

__Registro RIIRP__

Gravar no __campo 1 – Identificador __do Registro o valor fixo “__RIIRP__”\.

Essa informação deverá ser recuperada a partir da Ficha Financeira \(SAFX21\) do período cuja verba \(campo 07 da SAFX21\) esteja parametrizado na Parametrização de Verbas do módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\) = “Isentos \(Indenizações por Contrato de Trabalho\)”\.

Serão recuperados os Beneficiários cujo valor total de rendimentos anuais seja igual ou superior ao valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

OS3528

MFS\-3277

<a id="_Toc49779860"></a>RN123

__Registro RIIRP__

Gravar no __campo 2 – Janeiro__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Janeiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779861"></a>RN124

__Registro RIIRP__

Gravar no __campo 3 – Fevereiro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Fevereiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779862"></a>RN125

__Registro RIIRP__

Gravar no __campo 4 – Março__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Março \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779863"></a>RN126

__Registro RIIRP__

Gravar no __campo 5 – Abril__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Abril \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779864"></a>RN127

__Registro RIIRP__

Gravar no __campo 6 – Maio__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Maio \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779865"></a>RN128

__Registro RIIRP__

Gravar no __campo 7 – Junho__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Junho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779866"></a>RN129

__Registro RIIRP__

Gravar no __campo 8 – Julho__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Julho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779867"></a>RN130

__Registro RIIRP__

Gravar no __campo 9 – Agosto__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Agosto \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779868"></a>RN131

__Registro RIIRP__

Gravar no __campo 10 – Setembro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Setembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779869"></a>RN132

__Registro RIIRP__

Gravar no __campo 11 – Outubro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Outubro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779870"></a>RN133

__Registro RIIRP__

Gravar no __campo 12 – Novembro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Novembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779871"></a>RN134

__Registro RIIRP__

Gravar no __campo 13 – Dezembro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Dezembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779872"></a>RN135

__Registro RIIRP__

Gravar no __campo 14 – Décimo Terceiro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 desde que o campo 06 da SAFX21 = 02 \(Pagamento de 13º\. Salário\)\.

OS3528

<a id="_Toc49779873"></a>RN136

__Registro RIAP__

Gravar no __campo 1 – Identificador__ do Registro o valor fixo “__RIAP__”\.

Essa informação deverá ser recuperada a partir da Ficha Financeira \(SAFX21\) do período cuja verba \(campo 07 da SAFX21\) esteja parametrizado na Parametrização de Verbas do módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\) = “Isentos \(Abono Pecuniário\)”\.

OS3528

<a id="_Toc49779874"></a>RN137

__Registro RIAP __

Gravar no __campo 2 – Janeiro__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Janeiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779875"></a>RN138

__Registro RIAP__

Gravar no __campo 3 – Fevereiro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Fevereiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779876"></a>RN139

__Registro RIAP__

Gravar no __campo 4 – Março__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Março \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779877"></a>RN140

__Registro RIAP__

Gravar no __campo 5 – Abril__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Abril \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779878"></a>RN141

__Registro RIAP__

Gravar no __campo 6 – Maio__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Maio \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779879"></a>RN142

__Registro RIAP__

Gravar no __campo 7 – Junho__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Junho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779880"></a>RN143

__Registro RIAP__

Gravar no __campo 8 – Julho__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Julho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779881"></a>RN144

__Registro RIAP__

Gravar no __campo 9 – Agosto__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Agosto \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779882"></a>RN145

__Registro RIAP__

Gravar no __campo 10 – Setembro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Setembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779883"></a>RN146

__Registro RIAP__

Gravar no __campo 11 – Outubro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Outubro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779884"></a>RN147

__Registro RIAP__

Gravar no __campo 12 – Novembro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Novembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779885"></a>RN148

__Registro RIAP__

Gravar no __campo 13 – Dezembro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Dezembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779886"></a>RN149

__Registro RIAP__

Gravar no __campo 14 – Décimo Terceiro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 desde que o campo 06 da SAFX21 = 02 \(Pagamento de 13º\. Salário\)\.

OS3528

<a id="_Toc49779887"></a>RN150

__Registro RIMOG__

Gravar no __campo 1 – Identificador__ do Registro o valor fixo “__RIMOG__”\.

Essa informação deverá ser recuperada a partir da Ficha Financeira \(SAFX21\) do período cuja verba \(campo 07 da SAFX21\) esteja parametrizado na Parametrização de Verbas do módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\) = “Isentos \(Pensão, Aposentadoria ou Reforma por Moléstia Grave\)”\.

Serão recuperados os Beneficiários cujo valor total de rendimentos anuais seja igual ou superior ao valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

OS3528

MFS\-3277

<a id="_Toc49779888"></a>RN151

__Registro RIMOG__

Gravar no __campo 2 – Janeiro__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Janeiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779889"></a>RN152

__Registro RIMOG__

Gravar no __campo 3 – Fevereiro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Fevereiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779890"></a>RN153

__Registro RIMOG__

Gravar no __campo 4 – Março__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Março \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779891"></a>RN154

__Registro RIMOG__

Gravar no __campo 5 – Abril__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Abril \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779892"></a>RN155

__Registro RIMOG__

Gravar no __campo 6 – Maio__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Maio \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779893"></a>RN156

__Registro RIMOG__

Gravar no __campo 7 – Junho__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Junho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779894"></a>RN157

__Registro RIMOG__

Gravar no __campo 8 – Julho__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Julho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779895"></a>RN158

__Registro RIMOG__

Gravar no __campo 9 – Agosto__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Agosto \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779896"></a>RN159

__Registro RIMOG__

Gravar no __campo 10 – Setembro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Setembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779897"></a>RN160

__Registro RIMOG__

Gravar no __campo 11 – Outubro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Outubro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779898"></a>RN161

__Registro RIMOG__

Gravar no __campo 12 – Novembro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Novembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779899"></a>RN162

__Registro RIMOG__

Gravar no __campo 13 – Dezembro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Dezembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)

OS3528

<a id="_Toc49779900"></a>RN163

__Registro RIMOG__

Gravar no __campo 14 – Décimo Terceiro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 desde que o campo 06 da SAFX21 = 02 \(Pagamento de 13º\. Salário\)\.

OS3528

<a id="_Toc49779901"></a>RN164

__Registro RIP65__

Gravar no __campo 1 – Identificador__ do Registro o valor fixo “__RIP65__”\.

Essa informação deverá ser recuperada a partir da Ficha Financeira \(SAFX21\) do período cuja verba \(campo 07 da SAFX21\) esteja parametrizado na Parametrização de Verbas do módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\) = “Isentos \(Parcela Isenta de Aposentadoria para Maiores de 65 anos\)”\.

Essa informação também será recuperada a partir do Controle de Tributos \(SAFX53\) do período nos casos em que o campo VLR\_APOSENT\_ISENTA estiver preenchido\. Caso exista uma __X530\_RETIFICACAO\_IRRF__, a informação deverá ser recuperada do registro mais recente dessa tabela\.

Caso exista um mesmo beneficiário – mesmo CPF ou CNPJ – existente na SAFX21 e SAFX53 com o mesmo Código de Receita e ao ser gerado o registro RIP65, as informações das tabelas SAFX21 e SAFX53/__X530\_RETIFICACAO\_IRRF__ deverão ser consolidadas no mesmo registro RIP65 no arquivo \(obviamente consolidada por mês\)\. Isso é importante para que não exista duplicidades de um mesmo CPF ou CNPJ para um mesmo Código de Receita, sendo que esse caso gera erro na validação do arquivo ao importar o arquivo no validador da DIRF\.

Nos casos de existir um mesmo beneficiário – mesmo CPF ou CNPJ – existente na SAFX21 e SAFX53/__X530\_RETIFICACAO\_IRRF__ com Código de Receita diferentes, a geração permanece inalterada, ou seja, a informação continua sendo gerada separadamente para cada Código de Receita \(vide registro: IDREC\)\.

OS3528

OS3734

MFS\-90689

<a id="_Toc49779902"></a>RN165

__Registro RIP65__

Gravar no __campo 2 – Janeiro__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Janeiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53__ X530\_RETIFICACAO\_IRRF__ para a competência de Janeiro\. 

OS3528

OS3734

MFS\-90689

<a id="_Toc49779903"></a>RN166

__Registro RIP65__

Gravar no __campo 3 – Fevereiro__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Fevereiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53__ X530\_RETIFICACAO\_IRRF__ para a competência de Fevereiro\. 

OS3528

OS3734

MFS\-90689

<a id="_Toc49779904"></a>RN167

__Registro RIP65__

Gravar no __campo 4 – Março__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Março \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53__ X530\_RETIFICACAO\_IRRF__ para a competência de Março\. 

OS3528

OS3734

MFS\-90689

<a id="_Toc49779905"></a>RN168

__Registro RIP65__

Gravar no __campo 5 – Abril__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Abril \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53__ X530\_RETIFICACAO\_IRRF__ para a competência de Abril\. 

OS3528

OS3734

MFS\-90689

<a id="_Toc49779906"></a>RN169

__Registro RIP65__

Gravar no __campo 6 – Maio__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Maio \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53__ X530\_RETIFICACAO\_IRRF__ para a competência de Maio\. 

OS3528

OS3734

MFS\-90689

<a id="_Toc49779907"></a>RN170

__Registro RIP65__

Gravar no __campo 7 – Junho__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Junho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53__ X530\_RETIFICACAO\_IRRF__ para a competência de Junho\. 

OS3528

OS3734

MFS\-90689

<a id="_Toc49779908"></a>RN171

__Registro RIP65__

Gravar no __campo 8 – Julho__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Julho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53__ X530\_RETIFICACAO\_IRRF__ para a competência de Julho\. 

OS3528

OS3734

MFS\-90689

<a id="_Toc49779909"></a>RN172

__Registro RIP65__

Gravar no __campo 9 – Agosto__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Agosto \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53__ X530\_RETIFICACAO\_IRRF__ para a competência de Agosto\. 

OS3528

OS3734

MFS\-90689

<a id="_Toc49779910"></a>RN173

__Registro RIP65__

Gravar no __campo 10 – Setembro__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Setembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53__ X530\_RETIFICACAO\_IRRF__ para a competência de Setembro\. 

OS3528

OS3734

MFS\-90689

<a id="_Toc49779911"></a>RN174

__Registro RIP65__

Gravar no __campo 11 – Outubro__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Outubro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53__ X530\_RETIFICACAO\_IRRF__ para a competência de Outubro\. 

OS3528

OS3734

MFS\-90689

<a id="_Toc49779912"></a>RN175

__Registro RIP65__

Gravar no __campo 12 – Novembro__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Novembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53__ X530\_RETIFICACAO\_IRRF__ para a competência de Novembro\. 

OS3528

OS3734

MFS\-90689

<a id="_Toc49779913"></a>RN176

__Registro RIP65__

Gravar no __campo 13 – Dezembro__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Dezembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53__ X530\_RETIFICACAO\_IRRF__ para a competência de Dezembro\. 

OS3528 OS3734

MFS\-90689

<a id="_Toc49779914"></a>RN177

__Registro RIP65__

Gravar no __campo 14 – Décimo Terceiro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 desde que o campo 06 da SAFX21 = 02 \(Pagamento de 13º\. Salário\)\.

__OBS:__ Não haverá informação a ser recuperada para a geração do campo 14 – Décimo Terceiro nos casos do Controle de Tributos – SAFX53\. Conforme alinhamento com o Sr\. Marcos de Paula e o cliente Caixa Seguradora não existe essa informação na origem do cliente e caso haja demanda isso será desenvolvido no futuro\.

OS3528

OS3734

RN404

__Registro RIRPC__

Gravar no __campo 1 – Identificador__ do Registro o valor fixo “__RIRPC__”\.

Essa informação deverá ser recuperada a partir da Ficha Financeira \(SAFX21\) do período cuja verba \(campo 07 da SAFX21\) esteja parametrizado na Parametrização de Verbas do módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\) = N \- “Isentos \(Valor de Resgate da previdência complementar\)”\. 

__OU__

Gravar no __campo 2 – Valor pago__ no ano o total de valores contido do ano calendário a partir do __campo 101 \(VLR\_RESG\_PREV\_COMPL\)__ da SAFX53, desde que esse campo esteja preenchido para geração 

Observação: Esse campo será considerado na geração a partir do ano calendário 2021\.

MFS\-90689

RN405

__Registro RIRPC__

Gravar no __campo 2 – Janeiro__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Janeiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 101 \(VLR\_RESG\_PREV\_COMPL\) da SAFX53 para a competência de Janeiro\. 

Observação: Esse campo será considerado na geração a partir do ano calendário 2021\.

MFS\-90689

RN406

__Registro RIRPC__

Gravar no __campo 3 – Fevereiro__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Fevereiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 101 \(VLR\_RESG\_PREV\_COMPL\) da SAFX53 para a competência de Fevereiro\. 

Observação: Esse campo será considerado na geração a partir do ano calendário 2021\.

MFS\-90689

RN407

__Registro RIRPC__

Gravar no __campo 4 – Março__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Março \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 101 \(VLR\_VLR\_RESG\_PREV\_COMPL\) da SAFX53 para a competência de Março\. 

Observação: Esse campo será considerado na geração a partir do ano calendário 2021\.

MFS\-90689

RN408

__Registro RIRPC__

Gravar no __campo 5 – Abril__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Abril \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 101 \(VLR\_RESG\_PREV\_COMPL\) da SAFX53 para a competência de Abril

Observação: Esse campo será considerado na geração a partir do ano calendário 2021\.

MFS\-90689

RN409

__Registro RIRPC__

Gravar no __campo 6 – Maio__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Maio \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 101 \(VLR\_RESG\_PREV\_COMPL\) da SAFX53 para a competência de Maio

Observação: Esse campo será considerado na geração a partir do ano calendário 2021\.

MFS\-90689

RN410

__Registro RIRPC__

Gravar no __campo 7 – Junho__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Junho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 101 \(VLR\_RESG\_PREV\_COMPL\) da SAFX53 para a competência de Junho\. 

Observação: Esse campo será considerado na geração a partir do ano calendário 2021\.

MFS\-90689

RN411

__Registro RIRPC__

Gravar no __campo 8 – Julho__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Julho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 101 \(VLR\_RESG\_PREV\_COMPL\) da SAFX53 para a competência de Julho

MFS\-90689

RN412

__Registro RIRPC__

Gravar no __campo 9 – Agosto__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Agosto \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 101 \(VLR\_RESG\_PREV\_COMPL\) da SAFX53 para a competência de Agosto

Observação: Esse campo será considerado na geração a partir do ano calendário 2021\.

MFS\-90689

RN413

__Registro RIRPC__

Gravar no __campo 10 – Setembro__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Setembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 101 \(VLR\_RESG\_PREV\_COMPL\) da SAFX53 para a competência de Setembro

Observação: Esse campo será considerado na geração a partir do ano calendário 2021\.

MFS\-90689

RN414

__Registro RIRPC__

Gravar no __campo 11 – Outubro__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Outubro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 101 \(VLR\_RESG\_PREV\_COMPL\) da SAFX53 para a competência de Outubro

Observação: Esse campo será considerado na geração a partir do ano calendário 2021\.

MFS\-90689

RN415

__Registro RIRPC__

Gravar no __campo 12 – Novembro__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Novembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 101 \(VLR\_RESG\_PREV\_COMPL\) da SAFX53 para a competência de Novembro

Observação: Esse campo será considerado na geração a partir do ano calendário 2021\.

MFS\-90689

RN416

__Registro RIRPC__

Gravar no __campo 13 – Dezembro__ 

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Dezembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53
	- Gravar o campo 101 \(VLR\_RESG\_PREV\_COMPL\) da SAFX53 para a competência de Dezembro\.

Observação: Esse campo será considerado na geração a partir do ano calendário 2021\.

MFS\-90689

RN417

__Registro RIRPC__

Gravar no __campo 14 – Décimo Terceiro__

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 desde que o campo 06 da SAFX21 = 02 \(Pagamento de 13º\. Salário\)\.

Observação: Esse campo será considerado na geração a partir do ano calendário 2021\.

MFS\-90689

## <a id="_Toc50404655"></a><a id="_Toc155171985"></a>3\.12 – RIVC, RIBMR, RICAP

__RIVC__ \- EXCLUIDA

__RIBMR__ \- Rendimentos Isentos \- Bolsa de Estudo Recebida por Médico\-residente 

__RICAP__ \- Rendimentos Isentos \- Complementação de aposentadoria de previdência complementar correspondente às contribuições efetuadas no período de 1º de janeiro de 1989 a 31 de dezembro de 1995

<a id="_Toc49780064"></a><a id="_Toc49802066"></a><a id="_Toc49802308"></a><a id="_Toc49802410"></a><a id="_Toc49802513"></a><a id="_Toc49802623"></a><a id="_Toc49803391"></a><a id="_Toc49803636"></a><a id="_Toc49804471"></a><a id="_Toc49805270"></a><a id="_Toc49805388"></a><a id="_Toc49805500"></a><a id="_Toc49805716"></a><a id="_Toc50403082"></a><a id="_Toc50403206"></a><a id="_Toc50404538"></a><a id="_Toc50404658"></a><a id="_Toc50413237"></a>RN303

Este layout é valido, apenas quando o cliente informar na tela da Geração da DIRF, no campo Ano Referencia\-DIRF um ano a partir de 2016, caso contrário manter o layout compatível com os anos anteriores\.

<a id="_Toc49780065"></a><a id="_Toc49802067"></a><a id="_Toc49802309"></a><a id="_Toc49802411"></a><a id="_Toc49802514"></a><a id="_Toc49802624"></a><a id="_Toc49803392"></a><a id="_Toc49803637"></a><a id="_Toc49804472"></a><a id="_Toc49805271"></a><a id="_Toc49805389"></a><a id="_Toc49805501"></a><a id="_Toc49805717"></a><a id="_Toc50403083"></a><a id="_Toc50403207"></a><a id="_Toc50404539"></a><a id="_Toc50404659"></a><a id="_Toc50413238"></a>RN304

Não deverão ser recuperados os registros da tabela de Controle de Tributos \(X53\_RETENCAO\_IRRF\) cujo campo 52 – DATA\_CANCELAMENTO esteja preenchido e cujo campo 53 – IND\_CANCELAMENTO = “S”\.

Essas retenções não deverão ser recuperadas para a DIRF, pois as mesmas foram retidas indevidamente e a partir do seu cancelamento o valor das mesmas será considerado como crédito para futura recuperação\.

OS3267\-D

<a id="_Toc49780066"></a><a id="_Toc49802068"></a><a id="_Toc49802310"></a><a id="_Toc49802412"></a><a id="_Toc49802515"></a><a id="_Toc49802625"></a><a id="_Toc49803393"></a><a id="_Toc49803638"></a><a id="_Toc49804473"></a><a id="_Toc49805272"></a><a id="_Toc49805390"></a><a id="_Toc49805502"></a><a id="_Toc49805718"></a><a id="_Toc50403084"></a><a id="_Toc50403208"></a><a id="_Toc50404540"></a><a id="_Toc50404660"></a><a id="_Toc50413239"></a>RN305

__Registro RIVC – Rendimentos Isentos – Benefícios Indiretos e Reembolso de Despesa – Voluntário da Copa:__

Regras de validação do registro:

\- Deve ocorrer apenas se houver pelo menos um dos valores referentes aos meses ou ao 13º salário;

\- Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário;

\- Deve estar associado ao registro tipo BPFDEC\.

__Se Ano\-Referência\-DIRF for anterior a 2017,__ então

    O registro RIVC deve ser gerado\.

Senão,

   O registro RIVC NÃO deve ser gerado\.

#### Deverão ser recuperadas as informações da SAFX21, SAFX53 ou X530\_RETIFICACAO\_IRRF seguindo as seguintes regras:

- Quando as informações forem recuperadas das Fichas Financeiras \(SAFX21\), o código da verba \(campo 07 da SAFX21\) deverá estar parametrizado no módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros p/ Verba\) com o campo “Classe DIRF” = “Isentos \(Benefícios Indiretos e Reembolso de despesa – Voluntário da Copa\)”\.
- Quando as informações forem recuperadas das informações de terceiros \(SAFX53/__X530\_RETIFICACAO\_IRRF__\), considerar os campos: Valor – Voluntário da Copa e Valor 13º– Voluntário da Copa\.

Atenção: Recuperar apenas os registros de PF \(que possuírem CPF preenchidos\) , desde que exista valores em pelo menos um dos campos : Valor – Voluntário da Copa e Valor 13º– Voluntário da Copa\.

OS3832\-A

MFS\-90689

<a id="_Toc49780067"></a><a id="_Toc49802069"></a><a id="_Toc49802311"></a><a id="_Toc49802413"></a><a id="_Toc49802516"></a><a id="_Toc49802626"></a><a id="_Toc49803394"></a><a id="_Toc49803639"></a><a id="_Toc49804474"></a><a id="_Toc49805273"></a><a id="_Toc49805391"></a><a id="_Toc49805503"></a><a id="_Toc49805719"></a><a id="_Toc50403085"></a><a id="_Toc50403209"></a><a id="_Toc50404541"></a><a id="_Toc50404661"></a><a id="_Toc50413240"></a>RN306

__Registro RIVC__

Gravar no __campo 1 – Identificador__ do Registro o valor fixo ‘__RIVC__’

OS3832\-A

<a id="_Toc49780068"></a><a id="_Toc49802070"></a><a id="_Toc49802312"></a><a id="_Toc49802414"></a><a id="_Toc49802517"></a><a id="_Toc49802627"></a><a id="_Toc49803395"></a><a id="_Toc49803640"></a><a id="_Toc49804475"></a><a id="_Toc49805274"></a><a id="_Toc49805392"></a><a id="_Toc49805504"></a><a id="_Toc49805720"></a><a id="_Toc50403086"></a><a id="_Toc50403210"></a><a id="_Toc50404542"></a><a id="_Toc50404662"></a><a id="_Toc50413241"></a>RN307

__Registro RIVC__

Gravar no __campo 2 – Janeiro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Janeiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Voluntário da Copa da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Janeiro 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

<a id="_Toc49780069"></a><a id="_Toc49802071"></a><a id="_Toc49802313"></a><a id="_Toc49802415"></a><a id="_Toc49802518"></a><a id="_Toc49802628"></a><a id="_Toc49803396"></a><a id="_Toc49803641"></a><a id="_Toc49804476"></a><a id="_Toc49805275"></a><a id="_Toc49805393"></a><a id="_Toc49805505"></a><a id="_Toc49805721"></a><a id="_Toc50403087"></a><a id="_Toc50403211"></a><a id="_Toc50404543"></a><a id="_Toc50404663"></a><a id="_Toc50413242"></a>RN308

__Registro RIVC__

Gravar no __campo 3 – Fevereiro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Fevereiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Voluntário da Copa da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Fevereiro 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

<a id="_Toc49780070"></a><a id="_Toc49802072"></a><a id="_Toc49802314"></a><a id="_Toc49802416"></a><a id="_Toc49802519"></a><a id="_Toc49802629"></a><a id="_Toc49803397"></a><a id="_Toc49803642"></a><a id="_Toc49804477"></a><a id="_Toc49805276"></a><a id="_Toc49805394"></a><a id="_Toc49805506"></a><a id="_Toc49805722"></a><a id="_Toc50403088"></a><a id="_Toc50403212"></a><a id="_Toc50404544"></a><a id="_Toc50404664"></a><a id="_Toc50413243"></a>RN309

__Registro RIVC__

Gravar no __campo 4 – Março __de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Março \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Voluntário da Copa da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Março 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

<a id="_Toc49780071"></a><a id="_Toc49802073"></a><a id="_Toc49802315"></a><a id="_Toc49802417"></a><a id="_Toc49802520"></a><a id="_Toc49802630"></a><a id="_Toc49803398"></a><a id="_Toc49803643"></a><a id="_Toc49804478"></a><a id="_Toc49805277"></a><a id="_Toc49805395"></a><a id="_Toc49805507"></a><a id="_Toc49805723"></a><a id="_Toc50403089"></a><a id="_Toc50403213"></a><a id="_Toc50404545"></a><a id="_Toc50404665"></a><a id="_Toc50413244"></a>RN310

__Registro RIVC__

Gravar no __campo 5 – Abril__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Abril \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Voluntário da Copa da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Abril 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

<a id="_Toc49780072"></a><a id="_Toc49802074"></a><a id="_Toc49802316"></a><a id="_Toc49802521"></a><a id="_Toc49802631"></a><a id="_Toc49803399"></a><a id="_Toc49803644"></a><a id="_Toc49804479"></a><a id="_Toc49805278"></a><a id="_Toc49805396"></a><a id="_Toc49805508"></a><a id="_Toc49805724"></a><a id="_Toc50403090"></a><a id="_Toc50403214"></a><a id="_Toc50404546"></a><a id="_Toc50404666"></a><a id="_Toc50413245"></a>RN311

__Registro RIVC__

Gravar no __campo 6 – Maio__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Maio \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Voluntário da Copa da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Maio 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

<a id="_Toc49780073"></a><a id="_Toc49802075"></a><a id="_Toc49802317"></a><a id="_Toc49802522"></a><a id="_Toc49802632"></a><a id="_Toc49803400"></a><a id="_Toc49803645"></a><a id="_Toc49804480"></a><a id="_Toc49805279"></a><a id="_Toc49805397"></a><a id="_Toc49805509"></a><a id="_Toc49805725"></a><a id="_Toc50403091"></a><a id="_Toc50403215"></a><a id="_Toc50404547"></a><a id="_Toc50404667"></a><a id="_Toc50413246"></a>RN312

__Registro RIVC__

Gravar no __campo 7 – Junho__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Junho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Voluntário da Copa da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Junho 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

<a id="_Toc49780074"></a><a id="_Toc49802076"></a><a id="_Toc49802318"></a><a id="_Toc49802523"></a><a id="_Toc49802633"></a><a id="_Toc49803401"></a><a id="_Toc49803646"></a><a id="_Toc49804481"></a><a id="_Toc49805280"></a><a id="_Toc49805398"></a><a id="_Toc49805510"></a><a id="_Toc49805726"></a><a id="_Toc50403092"></a><a id="_Toc50403216"></a><a id="_Toc50404548"></a><a id="_Toc50404668"></a><a id="_Toc50413247"></a>RN313

__Registro RIVC__

Gravar no __campo 8 – Julho__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Julho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Voluntário da Copa da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Julho 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN314

__Registro RIVC__

Gravar no __campo 9 – Agosto__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Agoato \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Voluntário da Copa da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Agosto 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN315

__Registro RIVC__

Gravar no __campo 10 – Setembro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Setembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Voluntário da Copa da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Setembro 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN316

__Registro RIVC__

Gravar no __campo 11 – Outubro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Outubro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Voluntário da Copa da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Outubro 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN317

__Registro RIVC__

Gravar no __campo 12 – Novembro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Novembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Voluntário da Copa da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Novembro\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN318

__Registro RIVC__

Gravar no __campo 13 – Dezembro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Dezembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Voluntário da Copa da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Dezembro 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN319

__Registro RIVC__

Gravar no __campo 14 – Décimo Terceiro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 desde que o campo 06 \(IND\_FOLHA\) da SAFX21 deve estar preenchido com a opção “Pagamento de 13º\. Salário”\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN320

__RIBMR – Rendimentos Isentos – Bolsa de Estudo Recebida por Médico\-Residente __

Regras de validação do registro:

\- Deve ocorrer apenas se houver pelo menos um dos valores referentes aos meses ou ao 13º salário;

\- Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário;

\- Deve estar associado aos registros dos tipos BPFDEC\.

Deverão ser recuperadas as informações da SAFX21, SAFX53 __ou X530\_RETIFICACAO\_IRRF__ seguindo as seguintes regras:

Quando as informações forem recuperadas das Fichas Financeiras \(SAFX21\), o código da verba \(campo 07 da SAFX21\) deverá estar parametrizado no módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros p/ Verba\) com o campo “Classe DIRF” = “Isentos \(Bolsa de Estudo Recebida por Médico Residente\)”\.

Quando as informações forem recuperadas das informações de terceiros \(SAFX53/__X530\_RETIFICACAO\_IRRF__\), considerar os campos: Valor – Bolsa de Estudo Recebida por Médico Residente e Valor 13º – Bolsa de Estudo Recebida por Médico Residente\.

Atenção: Recuperar apenas os registros de PF \(que possuírem CPF preenchidos\), desde que exista valores em pelo menos um dos campos : Valor – Bolsa de Estudo Recebida por Médico Residente  e Valor 13º – Bolsa de Estudo Recebida por Médico Residente\.

OS3832\-A

MFS\-90689

RN321

__Registro RIBMR__

Gravar no __campo 1 – Identificador__ do Registro o valor fixo ‘__RIBMR__’

OS3832\-A

RN322

__Registro RIBMR__

Gravar no __campo 2 – Janeiro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Janeiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Bolsa de Estudo Recebida por Médico Residente da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Janeiro 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN323

__Registro RIBMR__

Gravar no __campo 3 – Fevereiro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Fevereiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Bolsa de Estudo Recebida por Médico Residente da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Fevereiro 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN324

__Registro RIBMR__

Gravar no __campo 4 – Março__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Março \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Bolsa de Estudo Recebida por Médico Residente da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Março 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN325

__Registro RIBMR__

Gravar no __campo 5 – Abril__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Abril \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Bolsa de Estudo Recebida por Médico Residente da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Abril\. 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN326

__Registro RIBMR__

Gravar no __campo 6 – Maio__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Maio \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Bolsa de Estudo Recebida por Médico Residente da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Maio 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN327

__Registro RIBMR__

Gravar no __campo 7 – Junho__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Junho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Bolsa de Estudo Recebida por Médico Residente da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Junho 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN328

__Registro RIBMR__

Gravar no __campo 8 – Julho__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Julho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Bolsa de Estudo Recebida por Médico Residente da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Julho 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN329

__Registro RIBMR__

Gravar no __campo 9 – Agosto__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Agosto \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Bolsa de Estudo Recebida por Médico Residente da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Agosto 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN330

__Registro RIBMR__

Gravar no __campo 10 – Setembro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Setembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Bolsa de Estudo Recebida por Médico Residente da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Setembro 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN331

__Registro RIBMR__

Gravar no __campo 11 – Outubro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Outubro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Bolsa de Estudo Recebida por Médico Residente da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Outubro 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN332

__Registro RIBMR__

Gravar no __campo 12 – Novembro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Novembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Bolsa de Estudo Recebida por Médico Residente da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Novembro 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN333

__Registro RIBMR__

Gravar no __campo 13 – Dezembro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Dezembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Gravar o campo Valor – Bolsa de Estudo Recebida por Médico Residente da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Dezembro 

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN334

__Registro RIBMR__

Gravar no __campo 14 – Décimo Terceiro__ de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 \(VLR\_VERBA\) da SAFX21 desde que o campo 06 \(IND\_FOLHA\) da SAFX21 deve estar preenchido com a opção “Pagamento de 13º\. Salário”\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3832\-A

MFS\-90689

RN339

__Registro RICAP__

Regras de validação do registro:

\- Deve ocorrer apenas se houver pelo menos um dos valores referentes aos meses ou 13º salário;

\- Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário;

\- Deve estar associado ao registro do tipo BPFDEC

Gravar no __campo 1 – Identificador__ do Registro o valor fixo “__RICAP__”\.

#### Deverão ser recuperadas as informações da SAFX21, SAFX53 ou X530\_RETIFICACAO\_IRRF seguindo as seguintes regras:

- Essa informação deverá ser recuperada a partir da Ficha Financeira \(SAFX21\) do período cuja verba \(campo 07 da SAFX21\) esteja parametrizado na Parametrização de Verbas do módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\) = “Isentos \(Complementação de aposentadoria de providência complementar correspondente às contribuições efetuadas no período de 1° de janeiro de 1989 a 31 de dezembro de 1995\)”\.
- SAFX53 \(Controle de Tributos – Retenções\)\. Para que as informações sejam recuperadas da SAFX53 o campo 65 \(Tipo de Isenção\) deverá estar populado com o código \(11 \- Complementação de aposentadoria, correspondente às contribuições efetuadas no período de 01/01/1989 a 31/12/1995\)\. Serão consideradas somente as retenções que pertençam a uma PESSOA FÍSICA \(Vinculada a um CPF\) e o Código de DARF \(tabela SAFX2019\) preenchido na SAFX53 \(ou porventura SAFX530\) esteja com o campo DIRF marcado\. 
- Se o registro da SAFX53 possua uma ou mais retificações na tabela __X530\_RETIFICACAO\_IRRF__, deverá ser recuperado o registro mais recente\.
- Caso no mesmo ano calendário, a pessoa física possua retenções ou retificações distintas para a mesma pessoa física, porém com datas de validade distintas, deverá ser gerado na DIRF a pessoa física com data de validade mais recente no ano calendário\.

OS4677

MFS\-90689

RN341

__Registro RICAP__

Gravar no __campo 2 – Janeiro__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Janeiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\. 

Gravar no campo 2 – Janeiro o valor contido no campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Janeiro \(ver campos 12 e 13 da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

OS4677

MFS\-90689

RN342

__Registro RICAP__

Gravar no __campo 3 – Fevereiro__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Fevereiro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\.

Gravar no campo 3 – Fevereiro o valor contido no campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Fevereiro \(ver campos 12 e 13 da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

OS4677

MFS\-90689

RN343

__Registro RICAP__

Gravar no __campo 4 – Março__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Março \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\.

Gravar no campo 4 – Março o valor contido no campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Março \(ver campos 12 e 13 da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

OS4677

MFS\-90689

RN344

__Registro RICAP__

Gravar no __campo 5 – Abril__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Abril \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\.

Gravar no campo 5 – Abril o valor contido no campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Abril \(ver campos 12 e 13 da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

OS4677

MFS\-90689

RN345

__Registro RICAP__

Gravar no __campo 6 – Maio__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Maio \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\.

Gravar no campo 6 – Maio o valor contido no campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Maio \(ver campos 12 e 13 da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

OS4677

MFS\-90689

RN346

__Registro RICAP__

Gravar no __campo 7 – Junho__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Junho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\.

Gravar no campo 7 – Junho o valor contido no campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Junho \(ver campos 12 e 13 da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

OS4677

MFS\-90689

RN347

__Registro RICAP__

Gravar no __campo 8 – Julho__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Julho \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\.

Gravar no campo 8 – Julho o valor contido no campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Julho \(ver campos 12 e 13 da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

OS4677

MFS\-90689

RN348

__Registro RICAP__

Gravar no __campo 9 – Agosto__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Agosto \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\.

Gravar no campo 9 – Agosto o valor contido no campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Agosto \(ver campos 12 e 13 da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

OS4677

MFS\-90689

RN349

__Registro RICAP__

Gravar no __campo 10 – Setembro__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Setembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\.

Gravar no campo 10 – Setembro o valor contido no campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Setembro \(ver campos 12 e 13 da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

OS4677

MFS\-90689

RN350

__Registro RICAP__

Gravar no __campo 11 – Outubro__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Outubro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\.

Gravar no campo 11 – Outubro o valor contido no campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53 /__X530\_RETIFICACAO\_IRRF__ para a competência de Outubro \(ver campos 12 e 13 da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

OS4677

MFS\-90689

RN351

__Registro RICAP__

Gravar no __campo 12 – Novembro__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Novembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\.

Gravar no campo 12 – Novembro o valor contido no campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Novembro \(ver campos 12 e 13 da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

OS4677

MFS\-90689

RN352

__Registro RICAP__

Gravar no __campo 13 – Dezembro__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 para a competência de Dezembro \(ver campos 04 \(ANO\_COMPETENCIA\) e 05 \(MES\_COMPETENCIA\) da SAFX21\)\.

Gravar no campo 13 – Dezembro o valor contido no campo 33 \(VLR\_APOSENT\_ISENTA\) da SAFX53/__X530\_RETIFICACAO\_IRRF__ para a competência de Dezembro \(ver campos 12 e 13 da SAFX53/__X530\_RETIFICACAO\_IRRF__\)\.

OS4677

MFS\-90689

RN353

__Registro RICAP__

Gravar no __campo 14 – Décimo Terceiro__ o valor contido no campo 09 \(VLR\_VERBA\) da SAFX21 desde que o campo 06 da SAFX21 = 02 \(Pagamento de 13º\. Salário\)\.

Gravar no campo 14 – Décimo Terceiro o valor contido no campo 46 \(VLR\_SALARIO\_13\) da SAFX53/__X530\_RETIFICACAO\_IRRF__\.

OS4677

MFS\-90689

RN354

__Regra Parâmetro “Gera registros sem retenção”:__

Regra para tela de Geração da DIRF

Criar na tela Geração da DIRF, localizada em Federal >> Obrigações de Tributos Federais >> DIRF >> Geração DIRF, o Parâmetro “Gera registros sem retenção” em formato checkbox que deverá vir marcador por default e indicar: marcado = SIM e desmarcado = NÃO\.

*Observação: *Essa funcionalidade já é aplicada para Comprovante/Etiqueta Anual de Retenção – PIS/COFINS/CSLL do item de menu Relatórios\.

Regra para execução de Geração da DIRF

Aplicar ao Registro RTRT, caso ele não seja apresentado desconsiderar aos que nele são associados:

- Quando o usuário marcar a opção “Gera registros sem retenção”, gerar todos os registros da SAFX53 ou __SAFX530__ \(X53\_RETENCAO\_IRRF ou __X530\_RETIFICACAO\_IRRF__ mais recente\) independente dos campos Valor Bruto e Valor Retido estarem preenchidos ou não;
- Quando o usuário desmarcar a opção “Gera registros sem retenção”, gerar os registros da SAFX53 ou __SAFX530 __\(X53\_RETENCAO\_IRRF ou X530\_RETIFICACAO\_IRRF mais recente\) se o campo Valor Retido estiver preenchido, caso contrário não será considerado registros de rendimentos sem retenção\.

OS4725

MFS\-90689

RN355

## <a id="_Toc49805184"></a><a id="_Toc49805302"></a><a id="_Toc49805414"></a><a id="_Toc50402992"></a><a id="_Toc50403116"></a><a id="_Toc50404669"></a><a id="_Toc155171986"></a>3\.13 – RIL96: Rendimentos Isentos anuais – Lucros e dividendos pagos a partir de 1996\.

<a id="_Toc49779780"></a>RN53

__Registro RIL96:__

Gravar no __campo 1 – Identificador__ do Registro o valor fixo “__RIL96__”\.

OS3528

<a id="_Toc49779781"></a>RN54

__Registro RIL96:__

Gravar no campo 2 – Valor pago no ano o total de valores contido do ano calendário a partir do campo 09 \(VLR\_VERBA\) da SAFX21, desde que a verba informada no campo 07 da SAFX21 possua na parametrização de Verba por Folha de Pagamento \(módulo: Obrigações de Tributos Federais, menu: Parâmetros >> Parâmetros p/ Verba \(Folha de Pagamento\)\) o campo “Classe para DIRF” preenchido com a opção “Isentos Anuais \(Lucros e Dividendos\)”\.

__OU__

Gravar no campo 2 – Valor pago no ano o total de valores contido do ano calendário a partir do campo 36 \(VLR\_LUCRO\_PJ\) da SAFX53, desde que esse campo esteja preenchido para geração\. Caso exista uma __X530\_RETIFICACAO\_IRRF__ mais recente \(vide __RNG\-01__\), recuperar do registro mais recente dessa tabela\.

Serão recuperados os Beneficiários cujo valor total de rendimentos anuais seja igual ou superior ao valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais, independente se a informação será gerada a partir da SAFX21 ou SAFX53/__X530\_RETIFICACAO\_IRRF__\.

Caso exista um mesmo beneficiário – mesmo CPF ou CNPJ – existente na SAFX21 e SAFX53 com o mesmo Código de Receita e ao ser gerado o registro RIL96, as informações das tabelas SAFX21 e SAFX53/__X530\_RETIFICACAO\_IRRF__ deverão ser consolidadas no mesmo registro RIL96 no arquivo\. Isso é importante para que não exista duplicidades de um mesmo CPF ou CNPJ para um mesmo Código de Receita, sendo que esse caso gera erro na validação do arquivo ao importar o arquivo no validador da DIRF\.

Nos casos de existir um mesmo beneficiário – mesmo CPF ou CNPJ – existente na SAFX21 e SAFX53/__X530\_RETIFICACAO\_IRRF__ com Código de Receita diferentes, a geração permanece inalterada, ou seja, a informação continua sendo gerada separadamente para cada Código de Receita \(vide registro: IDREC\)\.

OS3528

OS3734

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a><a id="OLE_LINK17"></a><a id="OLE_LINK18"></a><a id="OLE_LINK19"></a>MFS\-3277

MFS\-90689

## <a id="_Toc50402993"></a><a id="_Toc50403117"></a><a id="_Toc50404670"></a><a id="_Toc155171987"></a><a id="_Toc49803551"></a><a id="_Toc49805185"></a><a id="_Toc49805303"></a><a id="_Toc49805415"></a>3\.13\.a – RIJMRE – Rendimentos Isentos Anuais – Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função

<a id="_Toc49779818"></a>RN418

__Registro RIJMRE__

Gravar no __campo 1 – Identificador__ do Registro o valor fixo “__RIJMRE__”\.

MFS\-90689

<a id="_Toc49779819"></a>RN419

__Registro RIJMRE__

Gravar no __campo 2 – Valor pago__ no ano o total de valores contido do ano calendário a partir do campo 09 \(VLR\_VERBA\) da SAFX21, desde que a verba informada no campo 07 da SAFX21 possua na parametrização de Verba por Folha de Pagamento \(módulo: Obrigações de Tributos Federais, menu: Parâmetros >> Parâmetros p/ Verba \(Folha de Pagamento\)\) o campo “Classe para DIRF” preenchido com a opção “M – Isentos Anuais \(Juros de mora recebidos\)\.

__OU__

Gravar no __campo 2 – Valor pago__ no ano o total de valores contido do ano calendário a partir do __campo 100 \(VLR\_JUROS\_MORA\)__ da SAFX53, desde que esse campo esteja preenchido para geração

- __Caso o Ano\-Referência seja 2021 em diante__
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2021 >> Formatação Mídia do módulo Obrigações de Tributos Federais

A regra é variável de acordo com o Ano\-Referência, visto que os layout’s são diferentes\.

MFS\-90689

## <a id="_Toc155171988"></a>3\.14 – RIPTS – Rendimentos Isentos Anuais – Valores Pagos a titular ou sócio ou empresa de pequeno porte, exceto pró\-labore e aluguéis

RN91

__Registro RIPTS__

Gravar no __campo 1 – Identificador__ do Registro o valor fixo “__RIPTS__”\.

OS3528

RN92

__Registro RIPTS__

Gravar no __campo 2 – Valor pago__ no ano o total de valores contido do ano calendário a partir do campo 09 \(VLR\_VERBA\) da SAFX21, desde que a verba informada no campo 07 da SAFX21 possua na parametrização de Verba por Folha de Pagamento \(módulo: Obrigações de Tributos Federais, menu: Parâmetros >> Parâmetros p/ Verba \(Folha de Pagamento\)\) o campo “Classe para DIRF” preenchido com a opção “Isentos Anuais \(Valores pagos a titular ou sócio de empresa\)”\.

Serão recuperados os Beneficiários cujo valor total de rendimentos anuais seja igual ou superior ao valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

OS3528

MFS\-3277

## <a id="_Toc50402994"></a><a id="_Toc50403118"></a><a id="_Toc50404671"></a><a id="_Toc155171989"></a>3\.15 – RIO \- Rendimentos Isentos Anuais – Outros

<a id="_Toc49779782"></a>RN55

__Registro RIO:__

Gravar no __campo 1 – Identificador__ do Registro o valor fixo “__RIO__”\.

  
Este registro tem como origem de informação da tabela SAFX21 e SAFX53, podendo ser recuperados o conteúdo dos campos das duas tabelas\.

OS3528

<a id="_Toc49779783"></a>RN56

__Registro RIO:__

Gravar no campo 2 – Valor pago no ano o total de valores contido do ano calendário a partir do campo 09 \(VLR\_VERBA\) da SAFX21, desde que a verba informada no campo 07 da SAFX21 possua na parametrização de Verba por Folha de Pagamento \(módulo: Obrigações de Tributos Federais, menu: Parâmetros >> Parâmetros p/ Verba \(Folha de Pagamento\)\) o campo “Classe para DIRF” preenchido com a opção “Isentos Anuais \(Outros\)”\.

Serão recuperados os Beneficiários cujo valor total de rendimentos anuais seja igual ou superior ao valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

Se a origem da informação for da tabela SAFX53/__X530\_RETIFICACAO\_IRRF__, o sistema deverá recuperar as informações da SAFX53 e somente nos casos em que o registro da SAFX53 possua uma ou mais retificações na __X530\_RETIFICACAO\_IRRF__, deverá ser recuperado o registro mais recente \(vide __RNG\-01__\)\. Após essa verificação, deverá ser recuperado do Valor de Outros Dirf \(campo 38 \- VLR\_OUTROS\_DIRF\), quando o Beneficiário for Pessoa Física e o valor total de rendimentos anuais seja igual ou superior ao valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

Porém, se o Beneficiário Pessoa Física não atinja o “Valor do Anual Mínimo de Rendimentos” e os demais registros possuam critério de geração, ou seja, são gerados no arquivo da DIRF, o registro RIO deverá ser apresentado com o valor que possui de rendimentos\.

OS3528

OS3267\-D

MFS\-3277

MFS\-90689

<a id="_Toc49779784"></a>RN57

__Registro RIO:__

Gravar no campo 3 – Descrição dos rendimentos isentos – outros a informação que estiver contida no campo “Descrição” do menu Parâmetros >> Parâmetros p/ Verba \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais\.

Se a origem da informação for da tabela SAFX53/__X530\_RETIFICACAO\_IRRF__, deverá ser recuperado a descrição dos rendimentos isentos – outros do campo 39 \- DSC\_OUTROS\_DIRF\.

Para recuperar as informações da SAFX53/__X530\_RETIFICACAO\_IRRF__, o sistema deverá recuperar as informações da SAFX53 e somente nos casos em que o registro da SAFX53 possua uma ou mais retificações na __X530\_RETIFICACAO\_IRRF__, deverá ser recuperado o registro mais recente \(vide __RNG\-01__\)\.

OS3528

OS3267\-D

MFS\-90689

## <a id="_Toc49802431"></a><a id="_Toc49802541"></a><a id="_Toc49803307"></a><a id="_Toc49803552"></a><a id="_Toc49805186"></a><a id="_Toc49805304"></a><a id="_Toc49805416"></a><a id="_Toc50402995"></a><a id="_Toc50403119"></a><a id="_Toc50404672"></a><a id="_Toc155171990"></a>3\.16 – INFPC – Informações de Previdência Complementar

<a id="_Toc49779753"></a>RN357

__Registro INFPC__

Gravar no __campo 1 – Identificador__ do Registro o valor fixo “__INFPC__”\.

As informações desse registro serão recuperadas da tabela SAFX207 \(Ficha Financeira Segregada por Plano Previdência\)\.

Validação do Registro:

Serão Apresentados todos os CNPJ em ordem crescente\.

MFS8800

<a id="_Toc49779754"></a>RN358

__Registro INFPC__

Campo CNPJ 

A informação deverá ser recuperada da \(SAFX207 campo 09\) – Módulo Básicos >> MastersafDW >> Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Previdência\. 

MFS\-8800

<a id="_Toc49779755"></a>RN359

__Registro INFPC__

Campo Nome Empresarial  

A informação deverá ser recuperada da \(SAFX207 campo 10\) – Módulo Básicos >> MastersafDW >> Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Previdência\.

MFS\-8800

## <a id="_Toc49803308"></a><a id="_Toc49803553"></a><a id="_Toc49805187"></a><a id="_Toc49805305"></a><a id="_Toc49805417"></a><a id="_Toc50402996"></a><a id="_Toc50403120"></a><a id="_Toc50404673"></a><a id="_Toc155171991"></a>3\.17 – INFPA – Informações do beneficiário da pensão alimentícia

<a id="_Toc49779756"></a>RN360

__Registro INFPA__

Gravar no __campo 1 – Identificador__ do Registro o valor fixo “__INFPA__”\.

As informações desse registro serão recuperadas da tabela SAFX55 \(Arquivo de Dependente\)\.

Validação do Registro:

Deve estar classificado em ordem crescente de CPF e data de nascimento\.

Deve estar associado ao registro do tipo BPFDEC\. 

O Registro  INFPA somente será permitido quando o campo 08 \- IND\_RRA da tabela SAFX181 estiver com a opção = ‘1’ – pago pelo declarante \(campo 2 do registro RRA\)\.     

__*Observação:* __Essa validação era necessária no leiaute 2018 da DIRF\. Para o ano de 2019 foi retirada a consistência\.

MFS\-8800

MFS\-8984

MFS\-14872

MFS\-21816

<a id="_Toc49779757"></a>RN361

__Registro INFPA__

Campo CPF do Alimentado

A informação deverá ser recuperada da \(SAFX55 campo 11\) – Módulo Básicos >> MastersafDW >> Manutenção >> Cadastro >> Controle de Funcionário >> Dependentes\.

\[MFS\-8984\]

Log de Geração Dirf: 

Caso o dependente maior de 18 anos exibir a seguinte mensagem se o CPF não for preenchido:

Para dependentes maiores de 18 anos completos até 31 de Dezembro do ano\-calendário da declaração, o campo CPF tem seu preenchimento obrigatório\.

Beneficiário \(Código: xxxx / Nome: xxxx / CPF: xxxx\)

Dependente \(Código: xxxx / Nome: xxxx / CPF: xxxx\)

Empresa – Estab: xxxx\- xxxx

MFS\-8800

MFS\-8984

<a id="_Toc49779758"></a>RN362

__Registro INFPA__

Campo Data de Nascimento

A informação deverá ser recuperada da \(SAFX55 campo 08\) – Módulo Básicos >> MastersafDW >> Manutenção >> Cadastro >> Controle de Funcionário >> Dependentes\.

MFS\-8800

<a id="_Toc49779759"></a>RN363

__Registro INFPA__

Campo Nome 

A informação deverá ser recuperada da \(SAFX55 campo 07\) – Módulo Básicos >> MastersafDW >> Manutenção >> Cadastro >> Controle de Funcionário >> Dependentes\.

MFS\-8800

<a id="_Toc49779760"></a>RN364

__Registro INFPA__

Campo Relação de Dependência

A informação deverá ser recuperada da \(SAFX55 campo 06\) – Módulo Básicos >> MastersafDW >> Manutenção >> Cadastro >> Controle de Funcionário >> Dependentes\.

MFS\-8800

## <a id="_Toc49803309"></a><a id="_Toc49803554"></a><a id="_Toc49805188"></a><a id="_Toc49805306"></a><a id="_Toc49805418"></a><a id="_Toc50402997"></a><a id="_Toc50403121"></a><a id="_Toc50404674"></a><a id="_Toc155171992"></a>3\.18 – BPJDEC – Beneficiário pessoa jurídica do declarante

<a id="_Toc49779761"></a>RN36

__Registro BPJDEC__

Gravar no __campo 1 – Identificador do Registro__ o valor fixo “__BPJDEC__”\.

Devem ser recuperados os controles de tributos existentes na tabela X53\_RETENCAO\_IRRF desde que os mesmos sejam de Pessoas Jurídicas \(ver campos 04 e 05 da SAFX53 e verificar na tabela SAFX04 o campo CPF\_CGC que tenha 14 posições\)\. O campo “Tipo Lançamento” dessa tabela deve estar preenchido com a opção “Informações dos Beneficiários”\.

Caso o registro da SAFX53 possua uma ou mais retificações na tabela __X530\_RETIFICACAO\_IRRF__, deverá ser recuperado o registro mais recente dessa tabela \(vide __RNG\-01__\)\.

Deverão ser recuperados somente os beneficiários que forem PESSOA JURÍDICA\.

Caso no mesmo ano calendário, a pessoa jurídica possua retenções ou retificações distintas para a mesma pessoa jurídica, porém com datas de validade distintas, deverá ser gerado na DIRF a pessoa jurídica com data de validade mais recente no ano calendário\.

OS3528

OS3267\-D

CH2574\_2014

MFS\-90689

<a id="_Toc49779762"></a>RN37

__Registro BPJDEC__

Gravar no __campo 2 – CNPJ__ o CNPJ da Pessoa Jurídica \(ver campo 06 da tabela SAFX04\) de acordo com o campo de Pessoa Física/Jurídica do Controle de Tributos \(ver campos 04 e 05 da tabela SAFX53\)\.

Caso o registro da SAFX53 possua uma ou mais retificações na tabela __X530\_RETIFICACAO\_IRRF__, deverá ser recuperado o CNPJ da Pessoa Jurídica referente ao registro mais recente dessa tabela\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779763"></a>RN38

__Registro BPJDEC__

Gravar no __campo 3 – Nome Empresarial__ a Razão Social da Pessoa Jurídica \(ver campo 05 da SAFX04\) de acordo com o campo de Pessoa Física/Jurídica do Controle de Tributos \(ver campos 04 e 05 da tabela SAFX53\)\.

Caso o registro da SAFX53 possua uma ou mais retificações na tabela __X530\_RETIFICACAO\_IRRF__, deverá ser recuperada a Razão Social referente ao registro mais recente dessa tabela\. Caso no mesmo ano calendário, a pessoa jurídica possua retenções ou retificações distintas para a mesma pessoa jurídica, porém com datas de validade distintas, deverá ser gerado na DIRF a pessoa jurídica cuja descrição esteja com a data de validade mais recente no ano calendário\.

OS3528

OS3267\-D

CH2574\_2014

MFS\-90689

## <a id="_Toc50404675"></a><a id="_Toc155171993"></a>3\.19 – VPEIM e registros filhos RIMUM e RISEN

__VPEIM__ \- Valores pagos às entidades imunes ou isentas \- IN RFB 1\.234/2012 

__RIMUN__ \- Rendimentos Imunes \- art\. 4º, inciso III 

__RISEN __\- Rendimentos Isentos \- art\. 4º, inciso IV

RN398

__Regra Geral – registros VPEIM, RIMUM, RISEN__

Os registros VPEIM, RIMUM e RISEN são gerados com base na __SAFX533__ \- Rendimentos Imunes ou Isentos de pagamentos às entidades do art\. 4º, incisos III e IV – IN RFB 1\.234/2012 – tabela X533\_RIMUN\_RISEN\.

Esses registros devem ser apresentados na DIRF de Ano Referência a partir de __2018__, em declarações onde o campo 12 \(__Indicador de fundação pública de direito__ __privado\)__ do registro DIRF estiver __marcado__\.

Se o __Ano Referência\-DIRF __for maior ou igual a__ 2019__ e o __Indicador de fundação pública de direito__ __privado__ estiver __marcado__ na tela de geração, então, executar a regra abaixo para geração dos registros VPEIM, RIMUM, RISEN\.

__OU__

__Se__ o __Ano Referência\-DIRF __for maior ou igual a__ 2019,__ __E __na “Geração da DIRF” o “__Indicador de entidade em que a União detém maioria do capital a voto” __estiver __marcado\.__

__Obs\.:__ Regra divergente em relação ao Manual e Validador da DIRF, porém a regra foi alterada conforme cenário especifico, evidenciado pelo cliente FINEP, teste realizado e não criticado pelo Validador\.

Abaixo está a hierarquia desses registros\.

__Dirf__ – Declaração do imposto sobre a renda retido na fonte 

  __RESPO__ – Responsável pelo preenchimento 

 	__DECPJ __– Declarante pessoa jurídica 

                __  VPEIM __– Valores pagos às entidades imunes ou isentas – IN RFB 1\.234/2012 

 	            __RIMUM__ – Rendimentos Imunes – art\. 4º, inciso III 

 	 	__RISEN__ – Rendimentos Isentos – art\. 4º, inciso IV

MFS\-38828

RN399

__Geração DIRF– registros VPEIM, RIMUM, RISEN:__

Menu: DIRFà Geração DIRF

\[__ALTERAÇÃO\- MFS\-68078__\] Tratamento para as empresa de Natureza Declarante “3 – Empresas públicas ou sociedade de economia mista Federal”\.\(Cliente Finep\)\.

Se o __Ano Referência\-DIRF __for igual a__ 2018__, então executar a regra abaixo para geração dos registros VPEIM, RIMUM, RISEN\. 

Se o __Ano Referência\-DIRF __for maior ou igual a__ 2019__ e o __Indicador de fundação pública de direito__ __privado__ estiver __marcado__ na tela de geração, então, executar a regra abaixo para geração dos registros VPEIM, RIMUM, RISEN\.

__OU__

__Se__ o __Ano Referência\-DIRF __for maior ou igual a__ 2019,__ __E o__ “__Indicador de entidade em que a União detém maioria do capital a voto” __estiver __marcado, __então, executar a regra abaixo para geração dos registros VPEIM, RIMUM, RISEN\.

__Obs\.:__ Regra divergente em relação ao Manual e Validador da DIRF, porém a regra foi alterada conforme cenário específico, evidenciado pelo cliente FINEP, teste realizado e não criticado pelo Validador\.

   Processar os Rendimentos Imunes ou Isentos da SAFX533 para geração dos registros VPEIM, RIMUM e RISEN\.

   Para isso executa os procedimentos abaixo\.

1\) Fazer uma consulta na tabela X533\_RIMUN\_RISEN, com os seguintes critérios:

\- Empresa informada na tela;

\- Estabelecimento:

   Se o Tipo de Centralização informado na Tela = 1 – Não Centralizado, então:

         Considerar os rendimentos do estabelecimento selecionado na tela\.

   Se o Tipo de Centralização informado na Tela = 2 – Centralizado por Empresa, então:

         Considerar os rendimentos de todos os estabelecimentos da empresa informada na tela;

\- Se o Regime de Caixa estiver marcado para Pessoa Física/Jurídica \(menu Parâmetros >> Regime de Caixa\), então:

         Data Movimento do rendimento compreendida entre o Mes Ini e Mês Fim do Ano Calendário, informados na tela;

  Senão

         Mês e Ano Competência do rendimento compreendidos entre o Mes Ini e Mês Fim do Ano Calendário;

\- Considerar os rendimentos apenas de Pessoa Jurídica \(Campo CPF\-CGC da SAFX04 com 14 posições\)

Recuperar os campos:

\- Campo CPF\-CGC da Pessoa Jurídica;

\- Indicador de Imunidade ou Isenção \(IND\_IMUNE\_ISENTO\);

\- Mês da Data do Movimento, se o Regime de Caixa estar marcado para Pessoa Física/Jurídica;

\- Mes de Competência, se o Regime de Caixa estar desmarcado para Pessoa Física/Jurídica;

\- Valor do Rendimento \(VLR\_RENDIMENTO\)

Somar os Valores do Rendimentos para cada Mês, consolidando por Pessoa Jurídica \(Campo CPF\-CGC da SAFX04\) e Indicador de Imunidade ou Isenção\. Esse resultado será gravado numa tabela \(IRT\_DIRF\_MM\_VPEIM\), que será usada na geração do meio magnético para gravar os registros VPEIM, RIMUM, RISEN\.

Exemplo:

X533\_RIMUN\_RISEN

Estab

Data do Movimento

Pessoa Física/Jurídica \(CNPJ\)

Número do Documento

Indicador de Imunidade ou Isenção

Valor do Rendimento

001

01/01/2020

12345678901234

10001

1 – Pagamento à Entidade Imune

1000,00

002

01/01/2020

12345678901234

10002

1 – Pagamento à Entidade Imune

1000,00

001

01/02/2020

12345678901234

10003

1 – Pagamento à Entidade Imune

3000,00

002

01/02/2020

12345678901234

10004

1 – Pagamento à Entidade Imune

3000,00

001

01/01/2020

10000000000004

20001

2 – Pagamento à Entidade Isenta

4000,00

002

01/01/2020

10000000000004

20002

2 – Pagamento à Entidade Isenta

4000,00

001

01/02/2020

10000000000004

20003

2 – Pagamento à Entidade Isenta

2000,00

002

01/02/2020

10000000000004

20004

2 – Pagamento à Entidade Isenta

2000,00

Geração Centralizada no estab 001\.

Consolidação dos Rendimentos por Pessoa Jurídica e Indicador de Imunidade ou Isenção:

IRT\_DIRF\_MM\_VPEIM

Estab

Ano

Pessoa Física/Jurídica \(CNPJ\)

Indicador de Imunidade ou Isenção

Valor Rendimentos \(Janeiro\)

Valor Rendimentos \(Fevereiro\)

Valor  Rendimento \(Março\)

Valor  Rendimento \(Abril\)

001

2020

12345678901234

1 – Pagamento à Entidade Imune

2000,00

6000,00

0,00

0,00

001

2020

10000000000004

2 – Pagamento à Entidade Isenta

8000,00

4000,00

0,00

0,00

MFS\-38828

RN400

__Geração do Meio Magnético – registros VPEIM, RIMUM, RISEN:__

Menu: DIRFà Geração do Meio Magnético à Ano\-Referência a partir de 2011 à Formatação da Mídia

\[__ALTERAÇÃO\- MFS\-68078__\] Tratamento para as empresa de Natureza Declarante “3 – Empresas públicas ou sociedade de economia mista Federal”\.\(Cliente Finep\)\.

Se o __Ano Referência\-DIRF __for igual a__ 2018__, então executar a regra abaixo para geração dos registros VPEIM, RIMUM, RISEN\. 

Se o __Ano Referência\-DIRF __for maior ou igual a__ 2019__ e o __Indicador de fundação pública de direito__ __privado__ estiver __marcado__ na tela de geração, então, executar a regra abaixo para geração dos registros VPEIM, RIMUM, RISEN\.

__OU__

__Se__ o __Ano Referência\-DIRF __for maior ou igual a__ 2019,__ __E o__ “__Indicador de entidade em que a União detém maioria do capital a voto” __estiver __marcado, E__ se o campo 4 – Natureza do declarante \(Da tela de Formatação das Mídias da DIRF no menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídias\) estiver parametrizado com a __opção ”3”, __ então, executar a regra abaixo para geração dos registros VPEIM, RIMUM, RISEN no arquivo Meio Magnético, __caso contrário__ os registros gravados na tabela “IRT\_DIRF\_MM\_VPEIM” deverão ser desconsiderados\.

__Obs\.:__ Regra divergente em relação ao Manual e Validador da DIRF, porém a regra foi alterada conforme cenário específico, evidenciado pelo cliente FINEP, teste realizado e não criticado pelo Validador\.

 Para gerar os registros VPEIM, RIMUM e RISEN, executar os procedimentos abaixo\.

1\) Os Rendimentos Imunes/Isentos que foram consolidados por Pessoa Jurídica e Indicador de Imunidade ou Isenção e gravados na tabela \(IRT\_DIRF\_MM\_VPEIM\), devem ser recuperados com base nas informações preenchidas na tela de Geração do Meio Magnético:

\- Empresa 

\- Ano\-Referência DIRF

\- Processo – Ano Base – Dt Geração

2\) Para cada registro recuperado da IRT\_DIRF\_MM\_VPEIM, verificar os valores mensais\.  

Se pelo menos um valor mensal for maior que 0, deve gravar um dos registros RIMUM ou  RISEN\.

    Se Indicador de Imunidade ou Isenção\. = ‘1’ \- Pagamento à Entidade Imune, então:

         Gravar o registro __RIMUM__\.

    Se Indicador de Imunidade ou Isenção\. = ‘2’ \- Pagamento à Entidade Isenta  então:

          Gravar o registro __RISEN__\.

3\) Deve ser gravado um registro __VPEIM__ para cada CNPJ de Pessoa Jurídica presente nos rendimentos recuperados\.

MFS\-38828

RN401

__Geração do Meio Magnético – Registro VPEIM:__

Menu: DIRFà Geração do Meio Magnético à Ano\-Referência a partir de 2011 à Formatação da Mídia

Gravar registros de forma ordenada, pelo campo CNPJ em ordem crescente\.

O registro __VPEIM__ é composto pelos campos:

Campo 

Regra de Preenchimento

Identificador de registro 

VPEIM

CNPJ 

Campo 06 \- CPF\_CGC da SAFX04, da Pessoa Física/Jurídica dos rendimentos recuperados da SAFX533, conforme regras RN399, RN400 acima\.

Nome empresarial 

Campo 05 \- Razão Social da SAFX04, da Pessoa Física/Jurídica dos rendimentos recuperados da SAFX533, conforme regras RN399, RN400 acima\.

__ __

MFS\-38828

RN402

__Geração do Meio Magnético – Registro RIMUM:__

Menu: DIRFà Geração do Meio Magnético à Ano\-Referência a partir de 2011 à Formatação da Mídia

O registro __RIMUM __é composto pelos campos:

Campo 

Regra de Preenchimento

Identificador de registro 

__RIMUM__

Janeiro

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Janeiro, conforme regras RN399, RN400 acima\.

Fevereiro

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Fevereiro, conforme regras RN399, RN400 acima\.

Março

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Março, conforme regras RN399, RN400 acima\.

Abril

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Abril, conforme regras RN399, RN400 acima\.

Maio

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Maio, conforme regras RN399, RN400 acima\.

Junho

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Junho, conforme regras RN399, RN400 acima\.

Julho

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Julho, conforme regras RN399, RN400 acima\.

Agosto

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Agosto, conforme regras RN399, RN400 acima\.

Setembro

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Setembro, conforme regras RN399, RN400 acima\.

Outubro

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Outubro, conforme regras RN399, RN400 acima\.

Novembro

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Novembro, conforme regras RN399, RN400 acima\.

Dezembro

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Dezembro, conforme regras RN399, RN400 acima\.

Décimo Terceiro

Gravar zero\.

MFS\-38828

RN403

__Geração do Meio Magnético – Registro RISEN:__

Menu: DIRFà Geração do Meio Magnético à Ano\-Referência a partir de 2011 à Formatação da Mídia

O registro RISEN é composto pelos campos:

Campo 

Regra de Preenchimento

Identificador de registro 

__RISEN__

Janeiro

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Janeiro, conforme regras RN399, RN400 acima\.

Fevereiro

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Fevereiro, conforme regras RN399, RN400 acima\.

Março

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Março, conforme regras RN399, RN400 acima\.

Abril

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Abril, conforme regras RN399, RN400 acima\.

Maio

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Maio, conforme regras RN399, RN400 acima\.

Junho

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Junho, conforme regras RN399, RN400 acima\.

Julho

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Julho, conforme regras RN399, RN400 acima\.

Agosto

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Agosto, conforme regras RN399, RN400 acima\.

Setembro

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Setembro, conforme regras RN399, RN400 acima\.

Outubro

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Outubro, conforme regras RN399, RN400 acima\.

Novembro

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Novembro, conforme regras RN399, RN400 acima\.

Dezembro

Campo 014 – VLR\_RENDIMENTO da SAFX533, dos rendimentos recuperados da SAFX533, com Mês = Dezembro, conforme regras RN399, RN400 acima\.

Décimo Terceiro

Gravar zero\.

MFS\-38828

## <a id="_Toc50402998"></a><a id="_Toc50403122"></a><a id="_Toc50404676"></a><a id="_Toc155171994"></a>3\.20 – Registros PSE, OPSE, TPSE, RTPSE, DTPSE, RDTPSE

__PSE__ \- Plano privado de assistência à saúde \- coletivo empresarial 

__OPSE__ \- Operadora de plano privado de assistência à saúde \- coletivo empresarial 

__TPSE__ \- Titular de plano privado de assistência à saúde \- coletivo empresarial 

__RTPSE__ \- Reembolso do titular do plano de assistência à saúde \- coletivo empresarial 

__DTPSE__ \- Dependente do titular de plano privado de assistência à saúde \- coletivo empresarial 

__RDTPSE__ \- Reembolso do dependente do titular do plano de assistência à saúde \- coletivo empresarial

<a id="_Toc49779820"></a>RN93

__Registro PSE__

Gravar no __campo 1 – Identificador do registro__ o valor fixo “__PSE__”\. Esse registro só será gerado caso o campo “Plano privado de assistência à saúde – coletivo empresarial” da tela de geração do meio magnético \(menu: DIRF >> Geração DIRF\) do módulo Obrigações de Tributos Federais esteja selecionado com a opção “Sim” e se existe informações na Ficha Financeira \(SAFX21\) desde que a verba esteja classificada como “Pagamento ao Plano Privado de Assistência à Saúde”

Vale salientar que os registros de plano de saúde – PSE, OPSE, TPSE e DTPSE – quando um funcionário possuir mais de um plano de saúde – independente se o mesmo for de assistência médica ou odontológica – só serão gerados caso o campo “Operadora de Plano Privado de Assist\. à Saúde” não esteja preenchido na SAFX15\. As regras para planos múltiplos só serão atendidas caso esse campo não esteja preenchido\. Caso o campo esteja preenchido, as regras de geração atuais serão mantidas\.

OS3528

<a id="_Toc49779821"></a>RN94

__Registro OPSE__

Gravar no __campo 1 – Identificador do Registro__ o valor fixo “__OPSE__”\. Esse registro só será gerado caso existam registros TPSE existentes\. Só deve ser recuperado dos planos de saúde do movimento\.

Vale salientar que os registros de plano de saúde – PSE, OPSE, TPSE e DTPSE – quando um funcionário possuir mais de um plano de saúde – independente se o mesmo for de assistência médica ou odontológica – só serão gerados caso o campo “Operadora de Plano Privado de Assist\. à Saúde” não esteja preenchido na SAFX15\. As regras para planos múltiplos só serão atendidas caso esse campo não esteja preenchido\. Caso o campo esteja preenchido, as regras de geração atuais serão mantidas\.

OS3528

<a id="_Toc49779822"></a>RN95

__Registro OPSE__

Gravar no __campo 2 – CNPJ__ da operadora de plano privado de assistência à saúde \- coletivo empresarial, o conteúdo do campo “CNPJ” da tela pertencente ao menu Manutenção >> Cadastros >> Assistência à Saúde >> Operadora de Plano Privado de Assistência à Saúde do módulo DW\.

Essa informação será recuperada de acordo com o Plano de Saúde informado no campo “Operadora de Plano Privado de Assist\. à Saúde” da tela Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\) para a verba informada na SAFX21, desde que o campo “Operadora de Plano Privado de Assist\. a Saúde” da SAFX15 não esteja preenchido\.

Caso o campo “Operadora de Plano Privado de Assist\. à Saúde” da SAFX15 esteja preenchido a regra acima será ignorada\.

OS3528

<a id="_Toc49779823"></a>RN96

__Registro OPSE__

Gravar no __campo 3 – Nome Empresarial__, o conteúdo do campo “Nome Empresarial” da tela pertencente ao menu Manutenção >> Cadastros >> Assistência à Saúde >> Operadora de Plano Privado de Assistência à Saúde do módulo DW\.

Essa informação será recuperada de acordo com o Plano de Saúde informado no campo “Operadora de Plano Privado de Assist\. à Saúde” da tela Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\) para a verba informada na SAFX21, desde que o campo “Operadora de Plano Privado de Assist\. a Saúde” da SAFX15 não esteja preenchido\.

Caso o campo “Operadora de Plano Privado de Assist\. à Saúde” da SAFX15 esteja preenchido a regra acima será ignorada\.

OS3528

<a id="_Toc49779824"></a>RN97

__Registro OPSE__

Gravar no __campo 4 – Registro ANS__, o conteúdo do campo “Registro ANS” da tela pertencente ao menu Manutenção >> Cadastros >> Assistência à Saúde >> Operadora de Plano Privado de Assistência à Saúde do módulo DW\. O campo possui 10 posições na tela de manutenção, porém no registro serão gravadas somente as 6 primeiras posições

Essa informação será recuperada de acordo com o Plano de Saúde informado no campo “Operadora de Plano Privado de Assist\. à Saúde” da tela Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\) para a verba informada na SAFX21, desde que o campo “Operadora de Plano Privado de Assist\. a Saúde” da SAFX15 não esteja preenchido\.

Caso o campo “Operadora de Plano Privado de Assist\. à Saúde” da SAFX15 esteja preenchido a regra acima será ignorada\.

OS3528

<a id="_Toc49779825"></a>RN98

__Registro TPSE__

Gravar no __campo 1 – Identificador do Registro__ o valor fixo “__TPSE__”\.

Essa informação será recuperada a partir das fichas financeiras cadastradas na SAFX21 desde que a verba parametrizada na SAFX21 \(campo 07 – COD\_VERBA\) possua na Parametrização de Verbas do módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros para Verba \(Folha de Pagamento\) esteja com o campo “Classe DIRF” com a opção “Pagamento ao Plano Privado de Assistência à Saúde” e com o campo “Operadora de Plano Privado de Assist\. à Saúde” da mesma tela parametrizado para o Plano de Saúde\.

Caso o campo “Operadora de Plano Privado de Assist\. à Saúde” da SAFX15 esteja preenchido a regra acima de recuperar a partir da vinculação da Verba com o Plano de Saúde será ignorada\.

Vale salientar que os registros de plano de saúde – PSE, OPSE, TPSE e DTPSE – quando um funcionário possuir mais de um plano de saúde – independente se o mesmo for de assistência médica ou odontológica – só serão gerados caso o campo “Operadora de Plano Privado de Assist\. à Saúde” não esteja preenchido na SAFX15\. As regras para planos múltiplos só serão atendidas caso esse campo não esteja preenchido\. Caso o campo esteja preenchido, as regras de geração atuais serão mantidas\.

OS3528

<a id="_Toc49779826"></a>RN99

__Registro TPSE__

Gravar no __campo 2 – CPF do Titular__ o CPF do Funcionário de acordo com o campo 03 \(COD\_FUNC\) da tabela SAFX21 preenchido\. Com o Funcionário identificado, gravar o CPF a partir do campo 12 \(CPF\) da tabela SAFX15\.

OS3528

<a id="_Toc49779827"></a>RN100

__Registro TPSE__

Gravar no __campo 3 – Nome__ o Nome do Funcionário de acordo com o campo 03 \(COD\_FUNC\) da tabela SAFX21 preenchido\. Com o Funcionário identificado, gravar o Nome a partir do campo 05 \(NOME\) da tabela SAFX15\.

OS3528

<a id="_Toc49779828"></a>RN101

__Registro TPSE__

Gravar no __campo 4 – Valor pago no ano__ o conteúdo do campo Valor Pago no Ano do Funcionário de acordo com o campo 09 \(VLR\_VERBA\) da tabela SAFX21\.

Caso o Funcionário possua Dependentes na SAFX212, será considerado o Valor Pago no Ano para o Titular o conteúdo do campo 09 \(VLR\_VERBA\) da tabela SAFX21 subtraindo o somatório do Valor da Verba da SAFX212 de cada um dos Dependentes\. 

__Valor Pago pelo Titular quando o mesmo tem Dependentes__ = SAFX21\.VLR\_VERBA – SAFX212\.VLR\_VERBA \(somatório de todos os dependentes\)\.

__OBS:__ para que essa solução funcione corretamente, o cliente deverá carregar para o Valor da Verba do titular o somatório do Titular e dos Dependentes\.

Caso o Funcionário não possua Dependentes na SAFX212, gravar o valor nesse campo\.

MFS\-21816

Na DIRF2019: O “campo 4 – Valor pago no Ano” passa a ter 9 posições\. Nossa tabela permite gravar o valor de 015V002 \(13 posições inteiras e 2 decimais\), então para atender o layout neste ano, desconsiderar as 4 primeiras posições para atender o layout exigido\. 

OS3528

MFS\-21816

<a id="_Toc49779829"></a>RN365

__Registro RTPSE__

Gravar no __campo 1 – Identificador do registro__ o valor fixo “__RTPSE__”\.

As informações desse registro serão recuperadas da tabela SAFX208 \(Reembolso do Plano Privado de Saúde do Funcionário\)\.

Regras de Validação:

Deve estar Classificado em ordem crescente de CPF/CNPJ do prestador de serviço \(primeiro os CPF´s e depois os CNPJ\);

Deve estar associado ao registro do tipo TPSE;

Só deverá constar o registro se houver valor de reembolso do ano\-calendário ou de anos\-calendário anteriores;

Log:

Caso não houver Ficha Financeira para o beneficiário titular exibir a seguinte mensagem:

Não foi identificada a ficha financeira com a respectiva verba de \(Plano Privado de Assistência à Saúde\) para o beneficiário \(Cód: xxx / Nome: xxxx / CPF: xxxxx\)\. Registros de Reembolso do Titular \(RTPSE\) não serão gerados, pois, não existem os registros \(PSE, OPSE e TPSE\) para serem associados\.

Empresa – Estab: xxxx – xxxx

MFS\-8984

<a id="_Toc49779830"></a>RN366

__Registro RTPSE__

Gravar no __campo 2 – O CPF/CNPJ do Prestador de Serviço__ da tela \(Módulo Básicos >> MastersafDW Menu Manutenção >> Folha de Pagamento >> Reembolso do Plano Privado de Saúde do Funcionário – SAFX208\)\. 

MFS\-8984

<a id="_Toc49779831"></a>RN367

__Registro RTPSE__

Gravar no __campo 3 – O Nome Empresarial do Prestador de Serviço__ da tela \(Módulo Básicos >> MastersafDW Menu Manutenção >> Folha de Pagamento >> Reembolso do Plano Privado de Saúde do Funcionário – SAFX208\)\.

MFS\-8984

<a id="_Toc49779832"></a>RN368

__Registro RTPSE__

Gravar no __campo 4 – O Valor do reembolso do ano\-calendário__ da tela \(Módulo Básicos >> MastersafDW Menu Manutenção >> Folha de Pagamento >> Reembolso do Plano Privado de Saúde do Funcionário – SAFX208\)\.

MFS\-8984

<a id="_Toc49779833"></a>RN369

__Registro RTPSE__

Gravar no __campo 5 – O Valor do reembolso de anos anteriores__ da tela \(Módulo Básicos >> MastersafDW Menu Manutenção >> Folha de Pagamento >> Reembolso do Plano Privado de Saúde do Funcionário – SAFX208\)\.

MFS\-8984

<a id="_Toc49779834"></a>RN102

__Registro DTPSE__

Gravar no __campo 1 – Identificador do registro__ o valor fixo “__DTPSE__”\.

Vale salientar que os registros de plano de saúde – PSE, OPSE, TPSE e DTPSE – quando um funcionário possuir mais de um plano de saúde – independente se o mesmo for de assistência médica ou odontológica – só serão gerados caso o campo “Operadora de Plano Privado de Assist\. à Saúde” não esteja preenchido na SAFX15\. As regras para planos múltiplos só serão atendidas caso esse campo não esteja preenchido\. Caso o campo esteja preenchido, as regras de geração atuais serão mantidas\.

OS3528

<a id="_Toc49779835"></a>RN103

__Registro DTPSE__

Gravar no __campo 2 – CPF do Dependente__ a informação do CPF do Dependente de acordo com o campo “Dependente” da tela Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Dependente \(SAFX212\)\. Com o Dependente identificado, gravar o CPF a partir do campo CPF do Dependente da SAFX55\.

Log de Geração Dirf: 

Caso o dependente maior de 18 anos exibir a seguinte mensagem se o CPF não for preenchido:

Para dependentes maiores de 18 anos completos até 31 de Dezembro do ano\-calendário da declaração, o campo CPF tem seu preenchimento obrigatório\.

Beneficiário \(Código: xxxx / Nome: xxxx / CPF: xxxx \)

Dependente \(Código: xxxx / Nome: xxxx / CPF: xxxx \)

Empresa – Estab: xxxx\- xxxx

OS3528

MFS\-8489

<a id="_Toc49779836"></a>RN104

__Registro DTPSE__

Gravar no __campo 3 – Data de Nascimento__ a informação da Data de Nascimento do Dependente de acordo com o campo “Dependente” da tela Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Dependente \(SAFX212\) do módulo DW\. Com o Dependente identificado, gravar a Data de Nascimento a partir do campo 08 \(DATA\_NASC\) da SAFX55\.

OS3528

<a id="_Toc49779837"></a>RN105

__Registro DTPSE__

Gravar no __campo 4 – Nome__ o Nome do Dependente de acordo com o campo “Dependente” da tela Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Dependente \(SAFX212\) do módulo DW\. Com o Dependente identificado, gravar o Nome a partir do campo 07 \(NOME\) da tabela SAFX55\.

OS3528

<a id="_Toc49779838"></a>RN106

__Registro DTPSE__

Gravar no __campo 5 – Relação de dependência__ a Relação de Dependência do Dependente em relação ao Funcionário, de acordo com o campo “Código Dependente” da tela Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Dependente \(SAFX212\) do módulo DW\. Com o Dependente identificado, gravar o código do Dependente – conforme relação abaixo – de acordo com o campo 06 \(COD\_TIPO\_DEPEND\) da tabela SAFX55\.

- Caso a opção selecionada seja “03 – Cônjuge/Companheiro\(a\)”, gravar “03”\.
- Caso a opção selecionada seja “04 – Filho\(a\)”, gravar “04”\.
- Caso a opção selecionada seja “06 – Enteado\(a\)”, gravar “06”\.
- Caso a opção selecionada seja “08 – Pai/Mãe”, gravar “08”\.
- Caso a opção selecionada seja “10 – Agregado/Outros”, gravar “10”\.

Caso o campo 06 \(COD\_TIPO\_DEPEND\) da tabela SAFX55 esteja com outra opção selecionada, a opção será gravada, porém isso poderá causar crítica no PGD da DIRF 2011\.

OS3528

MFS\-

<a id="_Toc49779839"></a>RN107

__Registro DTPSE__

Gravar no __campo 6 – Valor pago no ano__ o conteúdo do campo “Valor pago no ano” do dependente da tela Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Dependente \(SAFX212\) do módulo DW\.

Cada Dependente deve ser gerado em um registro do tipo DTPSE separado\.

MFS\-21816

Na DIRF2019: O “campo 4 – Valor pago no Ano” passa a ter 9 posições\. Nossa tabela permite gravar o valor de 015V002 \(13 posições inteiras e 2 decimais\), então para atender o layout neste ano, desconsiderar as 4 primeiras posições para atender o layout exigido\. 

OS3528

MFS\-21816

<a id="_Toc49779840"></a>RN370

__Registro RDTPSE__

Gravar no __campo 1 – Identificador do registro__ o valor fixo “__RDTPSE__”\.

As informações desse registro serão recuperadas da tabela SAFX209 \(Reembolso do Plano Privado de Saúde do Dependente\)\.

Regras de Validação:

Deve estar Classificado em ordem crescente de CPF/CNPJ do prestador de serviço \(primeiro os CPF´s e depois os CNPJ\);

Deve estar associado ao registro do tipo DTPSE;

Só deverá constar o registro se houver valor de reembolso do ano\-calendário ou de anos\-calendário anteriores;

Log de Geração Dirf:

Caso não houver Ficha Financeira para o beneficiário titular exibir a seguinte mensagem:

Não foi identificada a ficha financeira segregada por dependente com a respectiva verba de \(Plano Privado de Assistência à Saúde\) para o Dependente \(Cód: xxx / Nome: xxxx / CPF: xxxxx\)\. Registros de Reembolso do dependente \(RDTPSE\) não serão gerados, pois, não existem os registros \(PSE, OPSE, TPSE e DTPSE\) para serem associados\.

Beneficiário Titular \(Cód: xxx / Nome: xxxx / CPF: xxxxx\)

Empresa – Estab: xxxx – xxxx

MFS\-8984

<a id="_Toc49779841"></a>RN371

__Registro RDTPSE__

Gravar no__ campo 2 – O CPF/CNPJ do Prestador de Serviço__ da tela \(Módulo Básicos >> MastersafDW Menu Manutenção >> Folha de Pagamento >> Reembolso do Plano Privado de Saúde do Dependente – SAFX209\)\.

MFS\-8984

<a id="_Toc49779842"></a>RN372

__Registro RDTPSE__

Gravar no__ campo 3 – O Nome Empresarial do Prestador de Serviço__ da tela \(Módulo Básicos >> MastersafDW Menu Manutenção >> Folha de Pagamento >> Reembolso do Plano Privado de Saúde do Dependente – SAFX209\)\.

MFS\-8984

<a id="_Toc49779843"></a>RN373

__Registro RDTPSE__

Gravar no __campo 4 – O Valor do reembolso do ano\-calendário__ da tela \(Módulo Básicos >> MastersafDW Menu Manutenção >> Folha de Pagamento >> Reembolso do Plano Privado de Saúde do Dependente – SAFX209\)\.

MFS\-8984

<a id="_Toc49779844"></a>RN374

__Registro RDTPSE__

Gravar no __campo 5 – O Valor do reembolso de anos anteriores__ da tela \(Módulo Básicos >> MastersafDW Menu Manutenção >> Folha de Pagamento >> Reembolso do Plano Privado de Saúde do Dependente – SAFX209\)\.

MFS\-8984

## <a id="_Toc50402999"></a><a id="_Toc50403123"></a><a id="_Toc50404677"></a><a id="_Toc155171995"></a>3\.21 – Registros RPDE, BRPDE, VRPDE

__RPDE __\- Rendimentos pagos a residentes ou domiciliados no exterior 

__BRPDE__ \- Beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior 

__VRPDE__ \- Valores de rendimentos pagos a residentes ou domiciliados no exterior

<a id="_Toc49779945"></a>RN206

__Registro RPDE, BRPDE, VRPDE__

Gravar no campo 1 – Identificador do Registro o texto fixo “__RPDE__”\.

As informações a serem gravadas serão recuperadas das tabelas SAFX21 e SAFX53/__X530\_RETIFICACAO\_IRRF__\. Caso não existam registros nessas tabelas, os registros __RPDE, BRPDE__ e __VRPDE__ não deverão ser gerados\. O critério para recuperar as informações dos beneficiários domiciliados no exterior é o seguinte:

- SAFX21
	- Campo “Declarante de rendimentos pagos a residentes ou domiciliados no exterior” = Sim no menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais;
	- Total de Rendimentos anuais igual ou superior a 1x o valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\. Deverão ser considerados como Total de Rendimentos anuais os valores do período informado nos campos “Mês/Ano da Saída do País” e “Mês/Ano do Retorno ao País” \(campos 68 e 69 da SAFX21\) __OU__ com valores de IR retido na fonte – ver campo 07 da SAFX21 cuja campo “Classe DIRF” = Imposto de Renda Retido na tela de Parâmetros por Verba \(módulo: Obrigações de Tributos Federais, menu: Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\)\) – e com o campo 09 \(VLR\_VERBA\) da SAFX21 preenchido para o período\. 
- SAFX53
	- Campo “Declarante de rendimentos pagos a residentes ou domiciliados no exterior” = Sim no menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais;
	- Total de Rendimentos anuais igual ou superior a 1x o valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\. Deverão ser considerados como Total de Rendimentos anuais os valores durante o período quando a Pessoa Física/Jurídica possuir a UF = EX __OU__ com valores de IR retido na fonte – ver campo VLR\_IR\_RETIDO da SAFX53 para o período informado\. Caso a retenção da SAFX53 possua um ou mais registros na __X530\_RETIFICACAO\_IRRF__, o sistema deverá recuperar o registro mais recente dessa tabela\.

O total de rendimentos do ano calendário que estiverem fora do período informado nos campos 68 e 69 da SAFX21 serão considerados nos registros\-filhos da família BPFDEC \(porque os mesmos serão pagos para o funcionário residente no Brasil\)\. Só serão considerados nos registros\-filhos da família RPDE os que estiverem dentro do período informado nos campos 68 e 69 da SAFX21\.

Nos casos em que o prestador de serviço \(pessoa física ou jurídica\) estiver parte do ano prestando serviço no Brasil e na outra parte do ano fora do país, o cliente deverá criar dois cadastros desse prestador \(SAFX04\) com data de validade distinta\. Só será considerada nos registros da família RPDE os que estiverem com UF = EX\. O cadastro do prestador que estiver no Brasil \(UF <> EX\) será considerado nos registros da família BPJDEC\.

Caso um mesmo funcionário \(SAFX21\) ou prestador \(SAFX53/__X530\_RETIFICACAO\_IRRF__\) possuam informações para os respectivos registros dentro do país \(BPFDEC ou BPJDEC e filhos\) ou fora do país \(RPDE, BRPDE e VRPDE\) o sistema não deverá considerar o somatório de dentro e fora do país para definir se o funcionário ou prestador é elegível para ser considerado na DIRF\. As informações devem ser consideradas de forma separada\. Caso em ambas as situações os valores não sejam iguais ou superiores a 1x o valor informado no campo “Valor Anual Mínimo de Rendimentos” da tela de Geração da DIRF, o funcionário ou prestador __NÃO SERÁ INFORMADO__ no meio magnético\. Porém se em um dos casos o mesmo for elegível, __TODAS__ as informações pertinentes ao funcionário ou prestador serão geradas no arquivo\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779946"></a>RN207

__Registro BRPDE__

Gravar no __campo 1 – Identificador__ de Registro o valor fixo “__BRPDE__”\.

OS3528

<a id="_Toc49779947"></a>RN208

__Registro BRPDE__

Gravar no __campo 2 – Beneficiário__ a informação de acordo com as regras abaixo:

- SAFX21
	- Gravar o valor “1”
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Caso o Beneficiário seja uma Pessoa Física \(campo 04 \(IND\_FIS\_JUR\) da SAFX53\), gravar “1”\.
	- Caso o Beneficiário seja uma Pessoa Jurídica \(campo 04 \(IND\_FIS\_JUR\) da SAFX53\), gravar “2”\.

No caso da SAFX53, para identificar uma Pessoa Física de uma Jurídica, verificar o identificador do campo 04 \(IND\_FIS\_JUR\) da SAFX53 e procurar o campo 06 da SAFX04\. Caso o campo 06 da SAFX04 possua 11 posições é uma Pessoa Física\. Caso possua 14 posições é uma Pessoa Jurídica\.

Caso o campo 06 da SAFX04 não esteja preenchido – o que caracteriza que o beneficiário não possui CPF ou CNPJ – verificar o campo 26 da SAFX04\. Caso o mesmo esteja preenchido com “1”, gravar “1”\. Caso esteja preenchido com qualquer outra informação, gravar “2”\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779948"></a><a id="_Toc49801950"></a>RN209

__Registro BRPDE__

Gravar no __campo 3 – Código do País__ a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 \(COD\_FUNC\) da SAFX21\)\. Com essa informação, gravar o valor de acordo com o campo “País”\.
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação de acordo com o campo 04 \(IND\_FIS\_JUR\) da SAFX53\. Com essa informação, gravar o valor contido no campo 21 da SAFX04\.

No caso em que o Código do País não for preenchido na SAFX21, deverá ser exibida a seguinte mensagem no log de geração da DIRF: “__*Retenção de Funcionário residente no exterior sem preenchimento do campo Código do País\. Por gentileza, verificar o cadastro do Funcionário\.*__”\.

No caso em que o Código do País não for preenchido na SAFX53, deverá ser exibida a seguinte mensagem no log de geração da DIRF: “__*Retenção de Terceiro residente no exterior sem preenchimento do campo Código do País\. Por gentileza, verificar o cadastro da Pessoa Física/Jurídica*__”\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779949"></a><a id="_Toc49801951"></a>RN210

__Registro BRPDE__

Gravar no __campo 4 \- Número de identificação fiscal__ – NIF a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 \(COD\_FUNC\) da SAFX21\)\. Com essa informação, gravar o valor contido no campo “Número de Identificação Fiscal” da SAFX15\.
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação de acordo com o campo 04 \(IND\_FIS\_JUR\) da SAFX53\. Com essa informação, gravar o valor contido no campo “Número de Identificação Fiscal” da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779950"></a><a id="_Toc49801952"></a>RN211

__Registro BRPDE__

Gravar no __campo 5 – Indicador de beneficiário dispensado do Número de Identificação Fiscal – NIF__, seguindo as regras abaixo:

- SAFX21
- Recuperar a informação de acordo com o Funcionário \(campo 03 \(COD\_FUNC\) da SAFX21\)\. Com essa informação, verificar se existe informação no campo 73\- “NUM\_ID\_FISCAL” da SAFX15, em caso afirmativo o campo deve ser preenchido com ‘N’, caso contrário ‘S’
- SAFX53/__X530\_RETIFICACAO\_IRRF__
- Recuperar a informação de acordo com o campo 04 \(IND\_FIS\_JUR\) da SAFX53\. Com essa informação, verificar se existe informação no campo 53\- “NUM\_ID\_FISCAL” da SAFX04, em caso afirmativo o campo deve ser preenchido com ‘N’, caso contrário ‘S’

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779951"></a><a id="_Toc49801953"></a>RN212

__Registro BRPDE__

Gravar no __campo 6 – Identificador de que o país não exige Número de Identificação Fiscal – NIF__

- SAFX21
- Recuperar a informação de acordo com o Funcionário \(campo 03 \(COD\_FUNC\) da SAFX21\)\. Com essa informação, verificar se existe informação no campo 76\- “DSC\_PROVINCIA\_EX” da SAFX15, em caso afirmativo o campo deve ser preenchido com ‘N’, caso contrário ‘S’
- SAFX53/__X530\_RETIFICACAO\_IRRF__
- Recuperar a informação de acordo com o campo 04 \(IND\_FIS\_JUR\) da SAFX53\. Com essa informação, verificar se existe informação no campo 55\- “DSC\_PROVINCIA\_EX” da SAFX04, em caso afirmativo o campo deve ser preenchido com ‘N’\.  

Se o campo 55 “DSC\_PROVINCIA\_EX” não estiver preenchido, verificar o campo 59 – “Indicador do Nº de Identificação Fiscal” da SAFX04\. Se o conteúdo for igual a “1”, o campo deve ser preenchido com “N”, senão se o conteúdo for igual a “2” ou “3”, o campo deve ser preenchido com “S”\.  Caso o campo 59 – “Indicador do Nº de Identificação Fiscal” não estiver preenchido, o campo deve ser preenchido “S”\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-25062

MFS\-90689

<a id="_Toc49779952"></a><a id="_Toc49801954"></a>RN213

__Registro BRPDE__

Gravar no __campo 7 – CPF/CNPJ__ a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 \(COD\_FUNC\) da SAFX21\)\. Com essa informação, gravar o valor contido no campo 12 da SAFX15\.
- SAFX53__/X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação de acordo com o campo 04 \(IND\_FIS\_JUR\) da SAFX53\. Com essa informação, gravar o valor contido no campo 06 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779953"></a><a id="_Toc49801955"></a>RN214

__Registro BRPDE__

Gravar no __campo 8 – Nome/Nome Empresarial__ a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 \(COD\_FUNC\) da SAFX21\)\. Com essa informação, gravar o valor contido no campo 05 da SAFX15\.
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação de acordo com o campo 04 \(IND\_FIS\_JUR\) da SAFX53\. Com essa informação, gravar o valor contido no campo 05 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779954"></a><a id="_Toc49801956"></a>RN215

__Registro BRPDE__

Gravar no __campo 9 – Relação fonte pagadora pessoa jurídica e beneficiário pessoa jurídica__ a informação de acordo com as regras abaixo:

- SAFX21
	- Não será gravada nessa situação, visto que essa informação é pertinente somente para Pessoas Jurídicas\.
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação de acordo com o campo 098 \-  “Relação Fonte Pagadora/Beneficiário” da SAFX53\. Essa informação só será gravada caso a Pessoa Física/Jurídica da SAFX04 seja uma __Pessoa Jurídica__, neste caso o preenchimento do campo é obrigatório\.
	- Se ano referência for __maior ou igual__ a 2020, e o campo 098 da SAFX53 for igual a “900”,então: \[MFS\-33041\]

Gerar a seguinte mensagem e gravar o campo normalmente:

Aviso: Relação da Fonte Pagadora do Registro BRPDE gerado com código inválido\(900\) \- Cgc Benef \- xxxxxx

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-33041

MFS\-90689

<a id="_Toc49779955"></a><a id="_Toc49801957"></a>RN216

__Registro BRPDE__

Gravar no __campo 10 – Logradouro__ a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 \(COD\_FUNC\) da SAFX21\)\. Com essa informação, gravar o valor contido no campo 35 da SAFX15\.
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação de acordo com o campo 04 \(IND\_FIS\_JUR\) da SAFX53\. Com essa informação, gravar o valor contido no campo 12 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779956"></a><a id="_Toc49801958"></a>RN217

__Registro BRPDE__

Gravar no __campo 11 – Número__ a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 \(COD\_FUNC\) da SAFX21\)\. Com essa informação, gravar o valor contido no campo 36 da SAFX15\.
- SAFX53__/X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação de acordo com o campo 04 \(IND\_FIS\_JUR\) da SAFX53\. Com essa informação, gravar o valor contido no campo 13 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779957"></a><a id="_Toc49801959"></a>RN218

__Registro BRPDE__

Gravar no __campo 12 – Complemento __a__ __informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 \(COD\_FUNC\) da SAFX21\)\. Com essa informação, gravar o valor contido no campo 37 da SAFX15\.
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação de acordo com o campo 04 \(IND\_FIS\_JUR\) da SAFX53\. Com essa informação, gravar o valor contido no campo 14 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779958"></a><a id="_Toc49801960"></a>RN219

__Registro BRPDE__

Gravar no __campo 13 – Bairro/Distrito__ a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 \(COD\_FUNC\) da SAFX21\)\. Com essa informação, gravar o valor contido no campo 38 da SAFX15\.
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação de acordo com o campo 04 \(IND\_FIS\_JUR\) da SAFX53\. Com essa informação, gravar o valor contido no campo 15 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779959"></a><a id="_Toc49801961"></a>RN220

__Registro BRPDE__

Gravar no __campo 14 – Código Postal__ a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 \(COD\_FUNC\) da SAFX21\)\. Com essa informação, gravar o valor contido no campo 40 da SAFX15\.
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação de acordo com o campo 04 \(IND\_FIS\_JUR\) da SAFX53\. Com essa informação, gravar o valor contido no campo 20 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779960"></a><a id="_Toc49801962"></a>RN221

__Registro BRPDE__

Gravar no __campo 15 – Cidade__ a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 \(COD\_FUNC\) da SAFX21\)\. Com essa informação, gravar o valor contido no campo 39 da SAFX15\.
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação de acordo com o campo 04 \(IND\_FIS\_JUR\) da SAFX53\. Com essa informação, gravar o valor contido no campo 16 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779961"></a><a id="_Toc49801963"></a>RN222

__Registro BRPDE__

Gravar no __campo 16 – Estado/Província__ a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 \(COD\_FUNC\) da SAFX21\)\. Com essa informação, gravar o valor contido no campo 76 da SAFX15\.
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação de acordo com o campo 04 \(IND\_FIS\_JUR\) da SAFX53\. Com essa informação, gravar o valor contido no campo 55 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779962"></a><a id="_Toc49801964"></a>RN223

__Registro BRPDE__

Gravar no __campo 17 – Telefone__ a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 \(COD\_FUNC\) da SAFX21\)\. Com essa informação, gravar o valor contido nos campos “DDD” e “Telefone” da SAFX15\.
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação de acordo com o campo 04 \(IND\_FIS\_JUR\) da SAFX53\. Com essa informação, gravar o valor contido nos campos 22 e 23 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779984"></a><a id="_Toc49801986"></a>RN245

Caso durante a geração do arquivo o campo “Relação Fonte Pagadora/Beneficiário” do registro BRPDE seja informado para uma Pessoa Física, deve ser exibida a seguinte mensagem de erro no log de geração\.

“Não pode ser informado para uma Pessoa Física a Relação de Fonte Pagadora com o Beneficiário, pois a mesma é pertinente apenas para Pessoa Jurídica”\.

Embora seja exibida a mensagem de erro, a geração do arquivo não será impedida\.

OS3528

<a id="_Toc49779963"></a><a id="_Toc49801965"></a>RN224

__Registro VRPDE__

Gravar no campo 1 – Identificador do Registro o valor fixo “__VRPDE__”\.

OS3528

<a id="_Toc49779964"></a><a id="_Toc49801966"></a>RN225

__Registro VRPDE__

Gravar no __campo 2 – Data do Pagamento__ a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação do campo 08 da SAFX21\.
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação do campo “Data Pagamento” \- DATA\_PAGTO da SAFX53\. Caso o campo “Data Pagamento” não esteja preenchido, gravar a informação contida no campo 03 \(DATA\_MOVTO\) da SAFX53\.

Nesse caso em que a Data do Pagamento não esteja preenchida para a SAFX53/__X530\_RETIFICACAO\_IRRF__ e seja gerada no arquivo a Data do Movimento deverá ser exibido no log de geração da DIRF a seguinte mensagem: __*“Retenção de Terceiro residente no exterior sem preenchimento de algum dos campos: Data Pagamento, Tipo Rendimento e/ou Forma Tributação\. Por gentileza, verificar a manutenção do Controle de Tributos”*__

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779965"></a><a id="_Toc49801967"></a>RN226

__Registro VRPDE__

Gravar no __campo 3 – Código de Receita__ a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação a partir do campo “Residente no Exterior” da tela de geração da DIRF – módulo: Obrigações de Tributos Federais, menu: DIRF >> Geração DIRF\.
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação do campo 11 \(COD\_DARF\) da SAFX53\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779966"></a><a id="_Toc49801968"></a>RN227

__Registro VRPDE__

Gravar no __campo 4 – Tipo de Rendimento__ a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação do campo “Tipo Rendimento” Campo 13 \(TP\_RENDIMENTO\) 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação do campo “Tipo Rendimento” Campo 49 \(TP\_RENDIMENTO\)

No caso em que o Tipo Rendimento não esteja preenchido na SAFX21, deverá ser exibido no log de geração da DIRF a seguinte mensagem: “__*Retenção de Funcionário residente no exterior sem preenchimento de algum dos campos: Tipo Rendimento e/ou Forma Tributação\. Por gentileza, verificar a manutenção da Ficha Financeira\.*__”

No caso em que o Tipo Rendimento não esteja preenchido na SAFX53, deverá ser exibido no log de geração da DIRF a seguinte mensagem: “__*Retenção de Terceiro residente no exterior sem preenchimento de algum dos campos: Data Pagamento, Tipo Rendimento e/ou Forma Tributação\. Por gentileza, verificar a manutenção do Controle de Tributos\.*__”

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779967"></a><a id="_Toc49801969"></a>RN228

__Registro VRPDE__

Gravar no __campo 5 – Rendimento Pago__ a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação a partir do campo 09 \(VLR\_VERBA\) da SAFX21, desde que a verba informada \(campo 07 da SAFX21\) esteja parametrizada no menu Parâmetros >> Parâmetros p/ Verba do módulo Obrigações de Tributos Federais com a opção “Rendimentos Tributáveis”\.
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação a partir do campo 14 da SAFX53

OBS: as verbas oriundas da tabela SAFX21 que estiverem classificadas como “Proventos” devem ser somadas, enquanto as verbas classificadas como “Descontos” devem ser subtraídas\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779968"></a><a id="_Toc49801970"></a>RN229

__Registro VRPDE__

Gravar no __campo 6 – Imposto Retido__ a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação a partir do campo 09 \(VLR\_VERBA\) da SAFX21, desde que a verba informada \(campo 07 da SAFX21\) esteja parametrizada no menu Parâmetros >> Parâmetros p/ Verba do módulo Obrigações de Tributos Federais com a opção “Imposto de Renda Retido”\.
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação a partir do campo 15 \(VLR\_IR\_RETIDO\) da SAFX53

OBS: as verbas oriundas da tabela SAFX21 que estiverem classificadas como “Proventos” devem ser subtraídas, enquanto as verbas classificadas como “Descontos” devem ser somadas\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

<a id="_Toc49779969"></a><a id="_Toc49801971"></a>RN230

__Registro VRPDE__

Gravar no __campo 7 – Forma de Tributação__ a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação do campo “Forma Tributação” 
- SAFX53/__X530\_RETIFICACAO\_IRRF__
	- Recuperar a informação do campo “Forma Tributação” 

No caso em que a Forma de Tributação não esteja preenchido na SAFX21, deverá ser exibido no log de geração da DIRF a seguinte mensagem: “__*Retenção de Funcionário residente no exterior sem preenchimento de algum dos campos: Tipo Rendimento e/ou Forma Tributação\. Por gentileza, verificar a manutenção da Ficha Financeira\.*__”

No caso em que a Forma de Tributação não esteja preenchido na SAFX53, deverá ser exibido no log de geração da DIRF a seguinte mensagem: “__*Retenção de Terceiro residente no exterior sem preenchimento de algum dos campos: Data Pagamento, Tipo Rendimento e/ou Forma Tributação\. Por gentileza, verificar a manutenção do Controle de Tributos\.*__”

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na __X530\_RETIFICACAO\_IRRF__\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

MFS\-90689

## <a id="_Toc50404678"></a><a id="_Toc155171996"></a>3\.22 – RRA e filhos \(IDREC, BPFRRA, RTRT, RTPO, RTIRF, RIMOG, RIP65, DAJUD, QTMESES, INFPA, RTPA\)

__RRA __\- Rendimentos recebidos acumuladamente 

__IDREC__ \- Identificação do código de receita 

__BPFRRA__ \- Beneficiário pessoa física do rendimento recebido acumuladamente 

__RTRT __\- Rendimentos Tributáveis \- Rendimento Tributável 

__RTPO__ \- Rendimentos Tributáveis \- Dedução \- Previdência Oficial 

__INFPA__ \- Informações do beneficiário da pensão alimentícia 

__RTPA__ \- Rendimentos Tributáveis \- Dedução \- Pensão Alimentícia 

__RTIRF__ \- Rendimentos Tributáveis \- Imposto sobre a Renda Retido na Fonte 

__RIMOG__ \- Rendimentos Isentos \- Pensão, Aposentadoria ou Reforma por Moléstia Grave 

__RIP65__ \- Rendimentos Isentos \- Parcela Isenta de Aposentadoria \(65 anos ou mais\)

__RIJMRE \-__ Rendimentos Isentos Anuais \- Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função

__DAJUD \-__ Despesa com ação judicial 

__QTMESES__ \- Quantidade de meses

<a id="_Toc49779985"></a><a id="_Toc49801987"></a><a id="_Toc49802229"></a><a id="_Toc49802331"></a><a id="_Toc49802434"></a><a id="_Toc49802544"></a><a id="_Toc49803312"></a><a id="_Toc49803557"></a><a id="_Toc49804392"></a><a id="_Toc49805191"></a><a id="_Toc49805309"></a><a id="_Toc49805421"></a><a id="_Toc49805637"></a><a id="_Toc50403003"></a><a id="_Toc50403127"></a><a id="_Toc50404559"></a><a id="_Toc50404679"></a><a id="_Toc50413258"></a>RN246

__Tela Rendimentos Recebidos Acumuladamente__

Localização: DIRF >> Rendimentos Recebidos Acumuladamente

Alterar o valor default do campo “Ano Calendário” e “Ano Referência\-DIRF” para 2016 – 2017 2019 – 2020 2021 – 2022 respectivamente\. Esse campo poderá ser alterado\. \[MFS\-33041\] /\[MFS\-76524\]

Inclusão do campo Valor pago para Advogado

Obrigatório: Não

Tipo: Text Box

Caso houver beneficiários diferentes com mesmo número de processo com valores distintos pagos a advogados deverá ser exibida a seguinte mensagem no log de geração da DIRF: “Existem valores diferentes pagos a advogado para o mesmo processo \(n° xxxxxx\)”\.

OS3528/ 

MFS\-8380

MFS\-8989

MFS\-33041

MFS\-76524

<a id="_Toc49779986"></a><a id="_Toc49801988"></a><a id="_Toc49802230"></a><a id="_Toc49802332"></a><a id="_Toc49802435"></a><a id="_Toc49802545"></a><a id="_Toc49803313"></a><a id="_Toc49803558"></a><a id="_Toc49804393"></a><a id="_Toc49805192"></a><a id="_Toc49805310"></a><a id="_Toc49805422"></a><a id="_Toc49805638"></a><a id="_Toc50403004"></a><a id="_Toc50403128"></a><a id="_Toc50404560"></a><a id="_Toc50404680"></a><a id="_Toc50413259"></a>RN247

__Registro RRA \- Rendimentos Recebidos Acumuladamente__

#### Deverão ser recuperado as informações da tela “Rendimentos Recebidos Acumuladamente” localizada no Menu: DIRF do módulo Federal / Obrigações de Tributos Federais, com base nos campos Ano Referência\-DIRF e Processo \- Ano Base \- Dt Geração, da tela de Formatação das Mídias \(Menu: DIRF / Geração do Meio Magnético / Ano Referência a partir de 2011\) seguindo as seguintes regras:

\- Serão considerados no txt da DIRF\-2012, os registros de RRA que estiverem cadastrados com Ano\-Calendário 2011, Ano Referência\-DIRF2012, uma vez que na tela de Formatação das Mídias, o usuário informe o Ano Referência\-DIRF2012 e escolha um processo que tenha sido gerado com o Ano\-Calendário 2011\.

\- Serão considerados no txt da DIRF\-2012, os registros de RRA que estiverem cadastrados com Ano\-Calendário 2012, Ano Referência\-DIRF2012, uma vez que na tela de Formatação das Mídias, o usuário informe o Ano Referência\-DIRF2012 e escolha um processo que tenha sido gerado com o Ano\-Calendário 2012\.

Estrutura completa:

__RRA __\- Rendimentos recebidos acumuladamente

__IDREC__ \- Identificação do código de receita

__BPFRRA__ \- Beneficiário pessoa física do rendimento recebido acumuladamente

__RTRT__ \- Rendimentos Tributáveis \- Rendimento Tributável

__RTPO__ \- Rendimentos Tributáveis \- Dedução \- Previdência Oficial

__RTPA__ – Rendimentos Tributáveis \- Dedução – Pensão Alimentícia 

__RTIRF__ \- Rendimentos Tributáveis \- Imposto de Renda Retido na Fonte

__RIMOG__ – Rendimentos Isentos – Pensão, Aposentadoria ou Reforma por Moléstia Grave

__DAJUD__ \- Despesa com ação judicial

__QTMESES__ \- Quantidade de meses

cmsamasmxdmas

asd

asd

__\[MFS\-8989\]__

Estrutura para ano\-calendário 2016, referência 2017

Estrutura completa:

__RRA __\- Rendimentos recebidos acumuladamente

__IDREC__ \- Identificação do código de receita

__BPFRRA__ \- Beneficiário pessoa física do rendimento recebido acumuladamente

__RTRT__ \- Rendimentos Tributáveis \- Rendimento Tributável

__RTPO__ \- Rendimentos Tributáveis \- Dedução \- Previdência Oficial

__RTIRF__ \- Rendimentos Tributáveis \- Imposto de Renda Retido na Fonte

__RIMOG__ – Rendimentos Isentos – Pensão, Aposentadoria ou Reforma por Moléstia Grave

__DAJUD__ \- Despesa com ação judicial

__QTMESES__ \- Quantidade de meses

__INFPA__ – Informações do Beneficiário da Pensão Alimentícia

            __RTPA __– Rendimentos Tributáveis – Dedução – Pensão Alimentícia

cmsamasmxdmas

asd

__\[MF\-21816\] __

Estrutura para ano\-calendário 2018, referência 2019

Estrutura completa:

__RRA __\- Rendimentos recebidos acumuladamente

__IDREC__ \- Identificação do código de receita

__BPFRRA__ \- Beneficiário pessoa física do rendimento recebido acumuladamente

__RTRT__ \- Rendimentos Tributáveis \- Rendimento Tributável

__RTPO__ \- Rendimentos Tributáveis \- Dedução \- Previdência Oficial

__INFPA__ – Informações do Beneficiário da Pensão Alimentícia

__RTPA__ – Rendimentos Tributáveis \- Dedução – Pensão Alimentícia 

__RTIRF__ \- Rendimentos Tributáveis \- Imposto de Renda Retido na Fonte

__RIMOG__ – Rendimentos Isentos – Pensão, Aposentadoria ou Reforma por Moléstia Grave

__DAJUD__ \- Despesa com ação judicial

__QTMESES__ \- Quantidade de meses

cmsamasmxdmas

asd

__\[MF\-90689\] __

__Estrutura para ano\-calendário 2022, referência 2021__

Estrutura completa:

__RRA __\- Rendimentos recebidos acumuladamente

__IDREC__ \- Identificação do código de receita

__BPFRRA__ \- Beneficiário pessoa física do rendimento recebido acumuladamente

__RTRT__ \- Rendimentos Tributáveis \- Rendimento Tributável

__RTPO__ \- Rendimentos Tributáveis \- Dedução \- Previdência Oficial

__INFPA__ \- Informações do beneficiário da pensão alimentícia

__RTPA__ – Rendimentos Tributáveis \- Dedução – Pensão Alimentícia 

__RTIRF__ \- Rendimentos Tributáveis \- Imposto de Renda Retido na Fonte

__RIMOG__ – Rendimentos Isentos – Pensão, Aposentadoria ou Reforma por Moléstia Grave

__RIP65__ \- Rendimentos Isentos \- Parcela Isenta de Aposentadoria \(65 anos ou mais\) 

__RIJMRE__ \- Rendimentos Isentos Anuais \- Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função

__DAJUD__ \- Despesa com ação judicial

__QTMESES__ \- Quantidade de meses

OS3528

MFS\-8989

MFS\-21816

<a id="_Toc49779987"></a><a id="_Toc49801989"></a><a id="_Toc49802231"></a><a id="_Toc49802333"></a><a id="_Toc49802436"></a><a id="_Toc49802546"></a><a id="_Toc49803314"></a><a id="_Toc49803559"></a><a id="_Toc49804394"></a><a id="_Toc49805193"></a><a id="_Toc49805311"></a><a id="_Toc49805423"></a><a id="_Toc49805639"></a><a id="_Toc50403005"></a><a id="_Toc50403129"></a><a id="_Toc50404561"></a><a id="_Toc50404681"></a><a id="_Toc50413260"></a>RN248

__Registro RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 1 – Identificador do Registro__ o valor fixo “__RRA__”\.

- Este registro deve ser classificado em ordem crescente por:

                 \- Indicador de rendimento recebido acumuladamente e 

                 \-  Número do processo

OS3528

<a id="_Toc49779988"></a><a id="_Toc49801990"></a><a id="_Toc49802232"></a><a id="_Toc49802334"></a><a id="_Toc49802437"></a><a id="_Toc49802547"></a><a id="_Toc49803315"></a><a id="_Toc49803560"></a><a id="_Toc49804395"></a><a id="_Toc49805194"></a><a id="_Toc49805312"></a><a id="_Toc49805424"></a><a id="_Toc49805640"></a><a id="_Toc50403006"></a><a id="_Toc50403130"></a><a id="_Toc50404562"></a><a id="_Toc50404682"></a><a id="_Toc50413261"></a>RN249

__Registro RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 2 – Identificador de rendimento recebido acumuladamente__, a informação do campo “Identificador de rendimento recebido acumuladamente”, da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49779989"></a><a id="_Toc49801991"></a><a id="_Toc49802233"></a><a id="_Toc49802335"></a><a id="_Toc49802438"></a><a id="_Toc49802548"></a><a id="_Toc49803316"></a><a id="_Toc49803561"></a><a id="_Toc49804396"></a><a id="_Toc49805195"></a><a id="_Toc49805313"></a><a id="_Toc49805425"></a><a id="_Toc49805641"></a><a id="_Toc50403007"></a><a id="_Toc50403131"></a><a id="_Toc50404563"></a><a id="_Toc50404683"></a><a id="_Toc50413262"></a>RN250

__Registro RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 3 – Número do Processo/Requerimento__, a informação do campo “Número do Processo / Requerimento”, da tela “Rendimentos Recebidos Acumuladamente”\.

Obs\. Este campo será obrigatório se o campo 2– Identificador de rendimento recebido acumuladamente, for igual a “2”

OS3528

<a id="_Toc49779990"></a><a id="_Toc49801992"></a><a id="_Toc49802234"></a><a id="_Toc49802336"></a><a id="_Toc49802439"></a><a id="_Toc49802549"></a><a id="_Toc49803317"></a><a id="_Toc49803562"></a><a id="_Toc49804397"></a><a id="_Toc49805196"></a><a id="_Toc49805314"></a><a id="_Toc49805426"></a><a id="_Toc49805642"></a><a id="_Toc50403008"></a><a id="_Toc50403132"></a><a id="_Toc50404564"></a><a id="_Toc50404684"></a><a id="_Toc50413263"></a>RN251

__Registro RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 4 – Indicador de tipo de advogado/escritório de advocacia__, de acordo com as regras abaixo:

- Se o campo “CPF/CNPJ” da tela “Rendimentos Recebidos Acumuladamente” estiver preenchido com 11 posições gravar “1”, caso seja 14 posições gravar “2”

OS3528

<a id="_Toc49779991"></a><a id="_Toc49801993"></a><a id="_Toc49802235"></a><a id="_Toc49802337"></a><a id="_Toc49802440"></a><a id="_Toc49802550"></a><a id="_Toc49803318"></a><a id="_Toc49803563"></a><a id="_Toc49804398"></a><a id="_Toc49805197"></a><a id="_Toc49805315"></a><a id="_Toc49805427"></a><a id="_Toc49805643"></a><a id="_Toc50403009"></a><a id="_Toc50403133"></a><a id="_Toc50404565"></a><a id="_Toc50404685"></a><a id="_Toc50413264"></a>RN252

__Registro RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 5 – CPF Advogado/CNPJ escritório de advocacia__, a informação do campo “CPF/CNPJ”, da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49779992"></a><a id="_Toc49801994"></a><a id="_Toc49802236"></a><a id="_Toc49802338"></a><a id="_Toc49802441"></a><a id="_Toc49802551"></a><a id="_Toc49803319"></a><a id="_Toc49803564"></a><a id="_Toc49804399"></a><a id="_Toc49805198"></a><a id="_Toc49805316"></a><a id="_Toc49805428"></a><a id="_Toc49805644"></a><a id="_Toc50403010"></a><a id="_Toc50403134"></a><a id="_Toc50404566"></a><a id="_Toc50404686"></a><a id="_Toc50413265"></a>RN253

__Registro RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 6 – Nome do advogado/escritório de advocacia__, a informação do campo “Nome do Advogado / Escritório de Advocacia”, da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49779993"></a><a id="_Toc49801995"></a><a id="_Toc49802237"></a><a id="_Toc49802339"></a><a id="_Toc49802442"></a><a id="_Toc49802552"></a><a id="_Toc49803320"></a><a id="_Toc49803565"></a><a id="_Toc49804400"></a><a id="_Toc49805199"></a><a id="_Toc49805317"></a><a id="_Toc49805429"></a><a id="_Toc49805645"></a><a id="_Toc50403011"></a><a id="_Toc50403135"></a><a id="_Toc50404567"></a><a id="_Toc50404687"></a><a id="_Toc50413266"></a>RN356

__Registro RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 7 – Valor Pago para o Advogado__, a informação do campo “Valor Pago para Advogado”, da tela “Rendimentos Recebidos Acumuladamente”\.

MFS\-8380

<a id="_Toc49779994"></a><a id="_Toc49801996"></a><a id="_Toc49802238"></a><a id="_Toc49802340"></a><a id="_Toc49802443"></a><a id="_Toc49802553"></a><a id="_Toc49803321"></a><a id="_Toc49803566"></a><a id="_Toc49804401"></a><a id="_Toc49805200"></a><a id="_Toc49805318"></a><a id="_Toc49805430"></a><a id="_Toc49805646"></a><a id="_Toc50403012"></a><a id="_Toc50403136"></a><a id="_Toc50404568"></a><a id="_Toc50404688"></a><a id="_Toc50413267"></a>RN254

__Registro IDREC da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

- Deve ser apresentado com os códigos de receita em ordem crescente
- Deve estar associado ao registro do tipo RRA

Gravar no __campo 1 – Identificador__ do Registro o valor fixo “__IDREC__”\.

OS3528

<a id="_Toc49779995"></a><a id="_Toc49801997"></a><a id="_Toc49802239"></a><a id="_Toc49802341"></a><a id="_Toc49802444"></a><a id="_Toc49802554"></a><a id="_Toc49803322"></a><a id="_Toc49803567"></a><a id="_Toc49804402"></a><a id="_Toc49805201"></a><a id="_Toc49805319"></a><a id="_Toc49805431"></a><a id="_Toc49805647"></a><a id="_Toc50403013"></a><a id="_Toc50403137"></a><a id="_Toc50404569"></a><a id="_Toc50404689"></a><a id="_Toc50413268"></a>RN255

__Registro IDREC da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 2 – Código de Receita__ de acordo com a regra abaixo:

- Preencher com a informação do campo “Código de Receita” da tela “Rendimentos Recebidos Acumuladamente”, Atualmente no layout de 2012 este campo é fixo “1889”\.

OS3528

<a id="_Toc49779996"></a><a id="_Toc49801998"></a><a id="_Toc49802240"></a><a id="_Toc49802342"></a><a id="_Toc49802445"></a><a id="_Toc49802555"></a><a id="_Toc49803323"></a><a id="_Toc49803568"></a><a id="_Toc49804403"></a><a id="_Toc49805202"></a><a id="_Toc49805320"></a><a id="_Toc49805432"></a><a id="_Toc49805648"></a><a id="_Toc50403014"></a><a id="_Toc50403138"></a><a id="_Toc50404570"></a><a id="_Toc50404690"></a><a id="_Toc50413269"></a>RN256

__Registro BPFRRA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Registro de beneficiário pessoa física dos rendimentos recebidos acumuladamente 

- Este registro deve ser classificado em ordem crescente por:

                \- CPF

                \- Natureza do RRA

- Deve ser associado ao registro do tipo IDREC

Gravar no __campo 1 – Identificador do Registro__ o valor fixo “__BPFRRA__”\.

OS3528

<a id="_Toc49779997"></a><a id="_Toc49801999"></a><a id="_Toc49802241"></a><a id="_Toc49802343"></a><a id="_Toc49802446"></a><a id="_Toc49802556"></a><a id="_Toc49803324"></a><a id="_Toc49803569"></a><a id="_Toc49804404"></a><a id="_Toc49805203"></a><a id="_Toc49805321"></a><a id="_Toc49805433"></a><a id="_Toc49805649"></a><a id="_Toc50403015"></a><a id="_Toc50403139"></a><a id="_Toc50404571"></a><a id="_Toc50404691"></a><a id="_Toc50413270"></a>RN257

__Registro BPFRRA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 2 – CPF,__ a informação do campo “CPF”, da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49779998"></a><a id="_Toc49802000"></a><a id="_Toc49802242"></a><a id="_Toc49802344"></a><a id="_Toc49802447"></a><a id="_Toc49802557"></a><a id="_Toc49803325"></a><a id="_Toc49803570"></a><a id="_Toc49804405"></a><a id="_Toc49805204"></a><a id="_Toc49805322"></a><a id="_Toc49805434"></a><a id="_Toc49805650"></a><a id="_Toc50403016"></a><a id="_Toc50403140"></a><a id="_Toc50404572"></a><a id="_Toc50404692"></a><a id="_Toc50413271"></a>RN258

__Registro rip da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 3 – Nome__, a informação do campo “Beneficiário”, da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49779999"></a><a id="_Toc49802001"></a><a id="_Toc49802243"></a><a id="_Toc49802345"></a><a id="_Toc49802448"></a><a id="_Toc49802558"></a><a id="_Toc49803326"></a><a id="_Toc49803571"></a><a id="_Toc49804406"></a><a id="_Toc49805205"></a><a id="_Toc49805323"></a><a id="_Toc49805435"></a><a id="_Toc49805651"></a><a id="_Toc50403017"></a><a id="_Toc50403141"></a><a id="_Toc50404573"></a><a id="_Toc50404693"></a><a id="_Toc50413272"></a>RN259

__Registro BPFRRA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 4 – Natureza do RRA__, a informação do campo “Natureza do rendimento recebido acumuladamente”, da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780000"></a><a id="_Toc49802002"></a><a id="_Toc49802244"></a><a id="_Toc49802346"></a><a id="_Toc49802449"></a><a id="_Toc49802559"></a><a id="_Toc49803327"></a><a id="_Toc49803572"></a><a id="_Toc49804407"></a><a id="_Toc49805206"></a><a id="_Toc49805324"></a><a id="_Toc49805436"></a><a id="_Toc49805652"></a><a id="_Toc50403018"></a><a id="_Toc50403142"></a><a id="_Toc50404574"></a><a id="_Toc50404694"></a><a id="_Toc50413273"></a>RN260

__Registro BPFRRA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 5 – Data__ __atribuída pelo laudo da moléstia grave,__ a informação do campo “Data atribuída pelo laudo”, da tela “Rendimentos Recebidos Acumuladamente”

Formato do campo: AAAAMMDD

OS3528

<a id="_Toc49780001"></a><a id="_Toc49802003"></a><a id="_Toc49802245"></a><a id="_Toc49802347"></a><a id="_Toc49802450"></a><a id="_Toc49802560"></a><a id="_Toc49803328"></a><a id="_Toc49803573"></a><a id="_Toc49804408"></a><a id="_Toc49805207"></a><a id="_Toc49805325"></a><a id="_Toc49805437"></a><a id="_Toc49805653"></a><a id="_Toc50403019"></a><a id="_Toc50403143"></a><a id="_Toc50404575"></a><a id="_Toc50404695"></a><a id="_Toc50413274"></a>RN397

__Registro BPFRRA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 6 – Indicador de Identificação do alimentando\.__

Esse campo é de preenchimento obrigatório na geração do arquivo magnético\. 

Verificar se para o beneficiário em \(Federal >> OTF >> DIRF >> Rendimentos Recebidos Acumuladamente \(Pensão Alimentícia\) tabela: IRT\_DIRF\_MM\_RRA\_DEP possui valor cadastrado para o COD\_FUNC em algum mês das colunas de” Pensão Alimentícia” do respectivo ano calendário da geração da DIRF\.

Caso possua valor em alguma coluna/mês, marcar esse campo como “__S__”, deverá constar o registro INFPA seguido do registro de valor \(RTPA e/ou ESPA\) para cada alimentado no arquivo magnético\.

Senão, gerar como “__N__”, não apresentar o registro INFPA, deverão constar apenas os registros de valores \(RTPA e/ou ESPA\)

 

Tamanho: 1 posição

Tipo: Caractere

Observação: Esse campo será considerado na geração a partir do ano calendário 2021\.

MFS\-14872

<a id="_Toc49780002"></a><a id="_Toc49802004"></a><a id="_Toc49802246"></a><a id="_Toc49802348"></a><a id="_Toc49802451"></a><a id="_Toc49802561"></a><a id="_Toc49803329"></a><a id="_Toc49803574"></a><a id="_Toc49804409"></a><a id="_Toc49805208"></a><a id="_Toc49805326"></a><a id="_Toc49805438"></a><a id="_Toc49805654"></a><a id="_Toc50403020"></a><a id="_Toc50403144"></a><a id="_Toc50404576"></a><a id="_Toc50404696"></a><a id="_Toc50413275"></a>RN261

__Registros RTRT, RTPO, RTPA, RTIRF, RIMOG da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 1 – Identificador do Registro__ a informação de acordo com as regras abaixo:

- Gravar o valor fixo “__RTRT__” – Rendimento Tributável
- Gravar o valor fixo “__RTPO__” – Previdência Oficial 
- Gravar o valor fixo “__RTPA__” – Pensão Alimentícia
- Gravar o valor fixo “__RTIRF__” – Imposto Retido
- Gravar o valor fixo “__RIMOG__” – campo Rend Isento Moléstia Grave
- Gravar o valor fixo “__RIP65__” – Parcela Isenta 65 anos

OS3528

<a id="_Toc49780003"></a><a id="_Toc49802005"></a><a id="_Toc49802247"></a><a id="_Toc49802349"></a><a id="_Toc49802452"></a><a id="_Toc49802562"></a><a id="_Toc49803330"></a><a id="_Toc49803575"></a><a id="_Toc49804410"></a><a id="_Toc49805209"></a><a id="_Toc49805327"></a><a id="_Toc49805439"></a><a id="_Toc49805655"></a><a id="_Toc50403021"></a><a id="_Toc50403145"></a><a id="_Toc50404577"></a><a id="_Toc50404697"></a><a id="_Toc50413276"></a>RN262

__Registros RTRT, RTPO, RTPA, RTIRF, RIMOG da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 2 – Janeiro__ o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Janeiro, conforme regras abaixo:

- Para o registro __RTRT__: campo Rendimento Tributável
- Para o registro __RTPO__: campo Previdência Oficial
- Para o registro __RTPA__: campo Pensão Alimentícia
- Para o registro __RTIRF__: campo Imposto Retido
- Para o registro __RIMOG__: campo Rend Isento Moléstia Grave
- Para o registro __RIP65: __campo Parcela Isenta 65 anos

OS3528

<a id="_Toc49780004"></a><a id="_Toc49802006"></a><a id="_Toc49802248"></a><a id="_Toc49802350"></a><a id="_Toc49802453"></a><a id="_Toc49802563"></a><a id="_Toc49803331"></a><a id="_Toc49803576"></a><a id="_Toc49804411"></a><a id="_Toc49805210"></a><a id="_Toc49805328"></a><a id="_Toc49805440"></a><a id="_Toc49805656"></a><a id="_Toc50403022"></a><a id="_Toc50403146"></a><a id="_Toc50404578"></a><a id="_Toc50404698"></a><a id="_Toc50413277"></a>RN263

__Registros RTRT, RTPO, RTPA, RTIRF, RIMOG da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 3 – Fevereiro__ o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Fevereiro, conforme regras abaixo:

- Para o registro __RTRT__: campo Rendimento Tributável
- Para o registro __RTPO__: campo Previdência Oficial
- Para o registro __RTPA__: campo Pensão Alimentícia
- Para o registro __RTIRF__: campo Imposto Retido
- Para o registro __RIMOG__: campo Rend Isento Moléstia Grave
- Para o registro __RIP65: __campo Parcela Isenta 65 anos

OS3528

<a id="_Toc49780005"></a><a id="_Toc49802007"></a><a id="_Toc49802249"></a><a id="_Toc49802351"></a><a id="_Toc49802454"></a><a id="_Toc49802564"></a><a id="_Toc49803332"></a><a id="_Toc49803577"></a><a id="_Toc49804412"></a><a id="_Toc49805211"></a><a id="_Toc49805329"></a><a id="_Toc49805441"></a><a id="_Toc49805657"></a><a id="_Toc50403023"></a><a id="_Toc50403147"></a><a id="_Toc50404579"></a><a id="_Toc50404699"></a><a id="_Toc50413278"></a>RN264

__Registros RTRT, RTPO, RTPA, RTIRF, RIMOG da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 4 – Março__ o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Março, conforme regras abaixo:

- Para o registro __RTRT__: campo Rendimento Tributável
- Para o registro __RTPO__: campo Previdência Oficial
- Para o registro __RTPA__: campo Pensão Alimentícia
- Para o registro __RTIRF__: campo Imposto Retido
- Para o registro __RIMOG__: campo Rend Isento Moléstia Grave
- Para o registro __RIP65: __campo Parcela Isenta 65 anos

OS3528

<a id="_Toc49780006"></a><a id="_Toc49802008"></a><a id="_Toc49802250"></a><a id="_Toc49802352"></a><a id="_Toc49802455"></a><a id="_Toc49802565"></a><a id="_Toc49803333"></a><a id="_Toc49803578"></a><a id="_Toc49804413"></a><a id="_Toc49805212"></a><a id="_Toc49805330"></a><a id="_Toc49805442"></a><a id="_Toc49805658"></a><a id="_Toc50403024"></a><a id="_Toc50403148"></a><a id="_Toc50404580"></a><a id="_Toc50404700"></a><a id="_Toc50413279"></a>RN265

__Registros RTRT, RTPO, RTPA, RTIRF, RIMOG da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 5 – Abril__ o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Abril, conforme regras abaixo:

- Para o registro __RTRT__: campo Rendimento Tributável
- Para o registro __RTPO__: campo Previdência Oficial
- Para o registro __RTPA__: campo Pensão Alimentícia
- Para o registro __RTIRF__: campo Imposto Retido
- Para o registro __RIMOG__: campo Rend Isento Moléstia Grave
- Para o registro __RIP65: __campo Rend Isento Aposentadoria

OS3528

<a id="_Toc49780007"></a><a id="_Toc49802009"></a><a id="_Toc49802251"></a><a id="_Toc49802353"></a><a id="_Toc49802456"></a><a id="_Toc49802566"></a><a id="_Toc49803334"></a><a id="_Toc49803579"></a><a id="_Toc49804414"></a><a id="_Toc49805213"></a><a id="_Toc49805331"></a><a id="_Toc49805443"></a><a id="_Toc49805659"></a><a id="_Toc50403025"></a><a id="_Toc50403149"></a><a id="_Toc50404581"></a><a id="_Toc50404701"></a><a id="_Toc50413280"></a>RN266

__Registros RTRT, RTPO, RTPA, RTIRF, RIMOG da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 6 – Maio__ o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Maio, conforme regras abaixo:

- Para o registro __RTRT__: campo Rendimento Tributável
- Para o registro __RTPO__: campo Previdência Oficial
- Para o registro __RTPA__: campo Pensão Alimentícia
- Para o registro __RTIRF__: campo Imposto Retido
- Para o registro __RIMOG__: campo Rend Isento Moléstia Grave
- Para o registro __RIP65: __campo Rend Isento Aposentadoria

OS3528

<a id="_Toc49780008"></a><a id="_Toc49802010"></a><a id="_Toc49802252"></a><a id="_Toc49802354"></a><a id="_Toc49802457"></a><a id="_Toc49802567"></a><a id="_Toc49803335"></a><a id="_Toc49803580"></a><a id="_Toc49804415"></a><a id="_Toc49805214"></a><a id="_Toc49805332"></a><a id="_Toc49805444"></a><a id="_Toc49805660"></a><a id="_Toc50403026"></a><a id="_Toc50403150"></a><a id="_Toc50404582"></a><a id="_Toc50404702"></a><a id="_Toc50413281"></a>RN267

__Registros RTRT, RTPO, RTPA, RTIRF, RIMOG da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 7 – Junho__ o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Junho, conforme regras abaixo:

- Para o registro __RTRT__: campo Rendimento Tributável
- Para o registro __RTPO__: campo Previdência Oficial
- Para o registro __RTPA__: campo Pensão Alimentícia
- Para o registro __RTIRF__: campo Imposto Retido
- Para o registro __RIMOG__: campo Rend Isento Moléstia Grave
- Para o registro __RIP65: __campo Rend Isento Aposentadoria

OS3528

<a id="_Toc49780009"></a><a id="_Toc49802011"></a><a id="_Toc49802253"></a><a id="_Toc49802355"></a><a id="_Toc49802458"></a><a id="_Toc49802568"></a><a id="_Toc49803336"></a><a id="_Toc49803581"></a><a id="_Toc49804416"></a><a id="_Toc49805215"></a><a id="_Toc49805333"></a><a id="_Toc49805445"></a><a id="_Toc49805661"></a><a id="_Toc50403027"></a><a id="_Toc50403151"></a><a id="_Toc50404583"></a><a id="_Toc50404703"></a><a id="_Toc50413282"></a>RN268

__Registros RTRT, RTPO, RTPA, RTIRF, RIMOG da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 8 – Julho__ o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Julho, conforme regras abaixo:

- Para o registro __RTRT__: campo Rendimento Tributável
- Para o registro __RTPO__: campo Previdência Oficial
- Para o registro __RTPA__: campo Pensão Alimentícia
- Para o registro __RTIRF__: campo Imposto Retido
- Para o registro __RIMOG__: campo Rend Isento Moléstia Grave
- Para o registro __RIP65: __campo Rend Isento Aposentadoria

OS3528

<a id="_Toc49780010"></a><a id="_Toc49802012"></a><a id="_Toc49802254"></a><a id="_Toc49802356"></a><a id="_Toc49802459"></a><a id="_Toc49802569"></a><a id="_Toc49803337"></a><a id="_Toc49803582"></a><a id="_Toc49804417"></a><a id="_Toc49805216"></a><a id="_Toc49805334"></a><a id="_Toc49805446"></a><a id="_Toc49805662"></a><a id="_Toc50403028"></a><a id="_Toc50403152"></a><a id="_Toc50404584"></a><a id="_Toc50404704"></a><a id="_Toc50413283"></a>RN269

__Registros RTRT, RTPO, RTPA, RTIRF, RIMOG da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 9 – Agosto__ o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Agosto, conforme regras abaixo:

- Para o registro __RTRT__: campo Rendimento Tributável
- Para o registro __RTPO__: campo Previdência Oficial
- Para o registro __RTPA__: campo Pensão Alimentícia
- Para o registro __RTIRF__: campo Imposto Retido
- Para o registro __RIMOG__: campo Rend Isento Moléstia Grave
- Para o registro __RIP65: __campo Rend Isento Aposentadoria

OS3528

<a id="_Toc49780011"></a><a id="_Toc49802013"></a><a id="_Toc49802255"></a><a id="_Toc49802357"></a><a id="_Toc49802460"></a><a id="_Toc49802570"></a><a id="_Toc49803338"></a><a id="_Toc49803583"></a><a id="_Toc49804418"></a><a id="_Toc49805217"></a><a id="_Toc49805335"></a><a id="_Toc49805447"></a><a id="_Toc49805663"></a><a id="_Toc50403029"></a><a id="_Toc50403153"></a><a id="_Toc50404585"></a><a id="_Toc50404705"></a><a id="_Toc50413284"></a>RN270

__Registros RTRT, RTPO, RTPA, RTIRF, RIMOG da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 10 – Setembro__ o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Setembro, conforme regras abaixo:

- Para o registro __RTRT__: campo Rendimento Tributável
- Para o registro __RTPO__: campo Previdência Oficial
- Para o registro __RTPA__: campo Pensão Alimentícia
- Para o registro __RTIRF__: campo Imposto Retido
- Para o registro __RIMOG__: campo Rend Isento Moléstia Grave
- Para o registro __RIP65: __campo Rend Isento Aposentadoria

OS3528

<a id="_Toc49780012"></a><a id="_Toc49802014"></a><a id="_Toc49802256"></a><a id="_Toc49802358"></a><a id="_Toc49802461"></a><a id="_Toc49802571"></a><a id="_Toc49803339"></a><a id="_Toc49803584"></a><a id="_Toc49804419"></a><a id="_Toc49805218"></a><a id="_Toc49805336"></a><a id="_Toc49805448"></a><a id="_Toc49805664"></a><a id="_Toc50403030"></a><a id="_Toc50403154"></a><a id="_Toc50404586"></a><a id="_Toc50404706"></a><a id="_Toc50413285"></a>RN271

__Registros RTRT, RTPO, RTPA, RTIRF, RIMOG da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 11 – Outubro__ o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Outubro, conforme regras abaixo:

- Para o registro __RTRT__: campo Rendimento Tributável
- Para o registro __RTPO__: campo Previdência Oficial
- Para o registro __RTPA__: campo Pensão Alimentícia
- Para o registro __RTIRF__: campo Imposto Retido
- Para o registro __RIMOG__: campo Rend Isento Moléstia Grave
- Para o registro __RIP65: __campo Rend Isento Aposentadoria

OS3528

<a id="_Toc49780013"></a><a id="_Toc49802015"></a><a id="_Toc49802257"></a><a id="_Toc49802359"></a><a id="_Toc49802462"></a><a id="_Toc49802572"></a><a id="_Toc49803340"></a><a id="_Toc49803585"></a><a id="_Toc49804420"></a><a id="_Toc49805219"></a><a id="_Toc49805337"></a><a id="_Toc49805449"></a><a id="_Toc49805665"></a><a id="_Toc50403031"></a><a id="_Toc50403155"></a><a id="_Toc50404587"></a><a id="_Toc50404707"></a><a id="_Toc50413286"></a>RN272

__Registros RTRT, RTPO,RTPA, RTIRF, RIMOG da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 12 – Novembro__ o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Novembro, conforme regras abaixo:

- Para o registro __RTRT__: campo Rendimento Tributável
- Para o registro __RTPO__: campo Previdência Oficial
- Para o registro __RTPA__: campo Pensão Alimentícia
- Para o registro __RTIRF__: campo Imposto Retido
- Para o registro __RIMOG__: campo Rend Isento Moléstia Grave
- Para o registro __RIP65: __campo Rend Isento Aposentadoria

OS3528

<a id="_Toc49780014"></a><a id="_Toc49802016"></a><a id="_Toc49802258"></a><a id="_Toc49802360"></a><a id="_Toc49802463"></a><a id="_Toc49802573"></a><a id="_Toc49803341"></a><a id="_Toc49803586"></a><a id="_Toc49804421"></a><a id="_Toc49805220"></a><a id="_Toc49805338"></a><a id="_Toc49805450"></a><a id="_Toc49805666"></a><a id="_Toc50403032"></a><a id="_Toc50403156"></a><a id="_Toc50404588"></a><a id="_Toc50404708"></a><a id="_Toc50413287"></a>RN273

__Registros RTRT,RTPO,RTPA, RTIRF, RIMOG da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 13 – Dezembro__ o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Dezembro, conforme regras abaixo:

- Para o registro __RTRT__: campo Rendimento Tributável
- Para o registro __RTPO__: campo Previdência Oficial
- Para o registro __RTPA__: campo Pensão Alimentícia
- Para o registro __RTIRF__: campo Imposto Retido
- Para o registro __RIMOG__: campo Rend Isento Moléstia Grave
- Para o registro __RIP65: __campo Rend Isento Aposentadoria

OS3528

<a id="_Toc49780015"></a><a id="_Toc49802017"></a><a id="_Toc49802259"></a><a id="_Toc49802361"></a><a id="_Toc49802464"></a><a id="_Toc49802574"></a><a id="_Toc49803342"></a><a id="_Toc49803587"></a><a id="_Toc49804422"></a><a id="_Toc49805221"></a><a id="_Toc49805339"></a><a id="_Toc49805451"></a><a id="_Toc49805667"></a><a id="_Toc50403033"></a><a id="_Toc50403157"></a><a id="_Toc50404589"></a><a id="_Toc50404709"></a><a id="_Toc50413288"></a>RN274

__Registros RTRT,RTPO,RTPA, RTIRF, RIMOG da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 14 – Décimo Terceiro__ o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Décimo Terceiro, conforme regras abaixo:

- Para o registro __RTRT__: campo Rendimento Tributável
- Para o registro __RTPO__: campo Previdência Oficial
- Para o registro __RTPA__: campo Pensão Alimentícia
- Para o registro __RTIRF__: campo Imposto Retido
- Para o registro __RIMOG__: campo Rend Isento Moléstia Grave
- Para o registro __RIP65: __campo Rend Isento Aposentadoria

ATENÇÃO: Até recebermos definição da Receita sobre a existência ou não do campo de 13º, o campo deve ser gerado com ‘||’, mesmo possuindo valor correspondente na tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780016"></a><a id="_Toc49802018"></a><a id="_Toc49802260"></a><a id="_Toc49802362"></a><a id="_Toc49802465"></a><a id="_Toc49802575"></a><a id="_Toc49803343"></a><a id="_Toc49803588"></a><a id="_Toc49804423"></a><a id="_Toc49805222"></a><a id="_Toc49805340"></a><a id="_Toc49805452"></a><a id="_Toc49805668"></a><a id="_Toc50403034"></a><a id="_Toc50403158"></a><a id="_Toc50404590"></a><a id="_Toc50404710"></a><a id="_Toc50413289"></a>RN275

__Registro DAJUD \- Despesas de Ação Judicial da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no campo 1 – Identificador do Registro o valor fixo “__DAJUD__”\.

#### Deverão ser recuperado as informações da tela <a id="_Toc313347822"></a>“Rendimentos Recebidos Acumuladamente” localizada no Menu: DIRF do módulo Federal / Obrigações de Tributos Federais, com base no campo Ano Referência\-DIRF \(neste caso 2012\)\.

OS3528

<a id="_Toc49780017"></a><a id="_Toc49802019"></a><a id="_Toc49802261"></a><a id="_Toc49802363"></a><a id="_Toc49802466"></a><a id="_Toc49802576"></a><a id="_Toc49803344"></a><a id="_Toc49803589"></a><a id="_Toc49804424"></a><a id="_Toc49805223"></a><a id="_Toc49805341"></a><a id="_Toc49805453"></a><a id="_Toc49805669"></a><a id="_Toc50403035"></a><a id="_Toc50403159"></a><a id="_Toc50404591"></a><a id="_Toc50404711"></a><a id="_Toc50413290"></a>RN276

__Registro DAJUD \- Despesas de Ação Judicial da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 2 – Janeiro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Janeiro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780018"></a><a id="_Toc49802020"></a><a id="_Toc49802262"></a><a id="_Toc49802364"></a><a id="_Toc49802467"></a><a id="_Toc49802577"></a><a id="_Toc49803345"></a><a id="_Toc49803590"></a><a id="_Toc49804425"></a><a id="_Toc49805224"></a><a id="_Toc49805342"></a><a id="_Toc49805454"></a><a id="_Toc49805670"></a><a id="_Toc50403036"></a><a id="_Toc50403160"></a><a id="_Toc50404592"></a><a id="_Toc50404712"></a><a id="_Toc50413291"></a>RN277

__Registro DAJUD \- Despesas de Ação Judicial da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 3 – Fevereiro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Fevereiro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780019"></a><a id="_Toc49802021"></a><a id="_Toc49802263"></a><a id="_Toc49802365"></a><a id="_Toc49802468"></a><a id="_Toc49802578"></a><a id="_Toc49803346"></a><a id="_Toc49803591"></a><a id="_Toc49804426"></a><a id="_Toc49805225"></a><a id="_Toc49805343"></a><a id="_Toc49805455"></a><a id="_Toc49805671"></a><a id="_Toc50403037"></a><a id="_Toc50403161"></a><a id="_Toc50404593"></a><a id="_Toc50404713"></a><a id="_Toc50413292"></a>RN278

__Registro DAJUD \- Despesas de Ação Judicial da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 4 – Março__ de acordo com a regra abaixo:

- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Março da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780020"></a><a id="_Toc49802022"></a><a id="_Toc49802264"></a><a id="_Toc49802366"></a><a id="_Toc49802469"></a><a id="_Toc49802579"></a><a id="_Toc49803347"></a><a id="_Toc49803592"></a><a id="_Toc49804427"></a><a id="_Toc49805226"></a><a id="_Toc49805344"></a><a id="_Toc49805456"></a><a id="_Toc49805672"></a><a id="_Toc50403038"></a><a id="_Toc50403162"></a><a id="_Toc50404594"></a><a id="_Toc50404714"></a><a id="_Toc50413293"></a>RN279

__Registro DAJUD \- Despesas de Ação Judicial da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 5 – Abril __de acordo com a regra abaixo:

- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Abril da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780021"></a><a id="_Toc49802023"></a><a id="_Toc49802265"></a><a id="_Toc49802367"></a><a id="_Toc49802470"></a><a id="_Toc49802580"></a><a id="_Toc49803348"></a><a id="_Toc49803593"></a><a id="_Toc49804428"></a><a id="_Toc49805227"></a><a id="_Toc49805345"></a><a id="_Toc49805457"></a><a id="_Toc49805673"></a><a id="_Toc50403039"></a><a id="_Toc50403163"></a><a id="_Toc50404595"></a><a id="_Toc50404715"></a><a id="_Toc50413294"></a>RN280

__Registro DAJUD \- Despesas de Ação Judicial da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 6 – Maio__ de acordo com a regra abaixo:

- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Maio da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780022"></a><a id="_Toc49802024"></a><a id="_Toc49802266"></a><a id="_Toc49802368"></a><a id="_Toc49802471"></a><a id="_Toc49802581"></a><a id="_Toc49803349"></a><a id="_Toc49803594"></a><a id="_Toc49804429"></a><a id="_Toc49805228"></a><a id="_Toc49805346"></a><a id="_Toc49805458"></a><a id="_Toc49805674"></a><a id="_Toc50403040"></a><a id="_Toc50403164"></a><a id="_Toc50404596"></a><a id="_Toc50404716"></a><a id="_Toc50413295"></a>RN281

__Registro DAJUD \- Despesas de Ação Judicial da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 7 – Junho__ de acordo com a regra abaixo:

- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Junho da tela “Rendimentos Recebidos Acumuladamente”

 

OS3528

<a id="_Toc49780023"></a><a id="_Toc49802025"></a><a id="_Toc49802267"></a><a id="_Toc49802369"></a><a id="_Toc49802472"></a><a id="_Toc49802582"></a><a id="_Toc49803350"></a><a id="_Toc49803595"></a><a id="_Toc49804430"></a><a id="_Toc49805229"></a><a id="_Toc49805347"></a><a id="_Toc49805459"></a><a id="_Toc49805675"></a><a id="_Toc50403041"></a><a id="_Toc50403165"></a><a id="_Toc50404597"></a><a id="_Toc50404717"></a><a id="_Toc50413296"></a>RN282

__Registro DAJUD \- Despesas de Ação Judicial da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 8 – Julho__ de acordo com a regra abaixo:

- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Julho da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780024"></a><a id="_Toc49802026"></a><a id="_Toc49802268"></a><a id="_Toc49802370"></a><a id="_Toc49802473"></a><a id="_Toc49802583"></a><a id="_Toc49803351"></a><a id="_Toc49803596"></a><a id="_Toc49804431"></a><a id="_Toc49805230"></a><a id="_Toc49805348"></a><a id="_Toc49805460"></a><a id="_Toc49805676"></a><a id="_Toc50403042"></a><a id="_Toc50403166"></a><a id="_Toc50404598"></a><a id="_Toc50404718"></a><a id="_Toc50413297"></a>RN283

__Registro DAJUD \- Despesas de Ação Judicial da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 9 – Agosto__ de acordo com a regra abaixo:

- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Agosto da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780025"></a><a id="_Toc49802027"></a><a id="_Toc49802269"></a><a id="_Toc49802371"></a><a id="_Toc49802474"></a><a id="_Toc49802584"></a><a id="_Toc49803352"></a><a id="_Toc49803597"></a><a id="_Toc49804432"></a><a id="_Toc49805231"></a><a id="_Toc49805349"></a><a id="_Toc49805461"></a><a id="_Toc49805677"></a><a id="_Toc50403043"></a><a id="_Toc50403167"></a><a id="_Toc50404599"></a><a id="_Toc50404719"></a><a id="_Toc50413298"></a>RN284

__Registro DAJUD \- Despesas de Ação Judicial da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 10 – Setembro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Setembro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780026"></a><a id="_Toc49802028"></a><a id="_Toc49802270"></a><a id="_Toc49802372"></a><a id="_Toc49802475"></a><a id="_Toc49802585"></a><a id="_Toc49803353"></a><a id="_Toc49803598"></a><a id="_Toc49804433"></a><a id="_Toc49805232"></a><a id="_Toc49805350"></a><a id="_Toc49805462"></a><a id="_Toc49805678"></a><a id="_Toc50403044"></a><a id="_Toc50403168"></a><a id="_Toc50404600"></a><a id="_Toc50404720"></a><a id="_Toc50413299"></a>RN285

__Registro DAJUD \- Despesas de Ação Judicial da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 11 – Outubro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Outubro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780027"></a><a id="_Toc49802029"></a><a id="_Toc49802271"></a><a id="_Toc49802373"></a><a id="_Toc49802476"></a><a id="_Toc49802586"></a><a id="_Toc49803354"></a><a id="_Toc49803599"></a><a id="_Toc49804434"></a><a id="_Toc49805233"></a><a id="_Toc49805351"></a><a id="_Toc49805463"></a><a id="_Toc49805679"></a><a id="_Toc50403045"></a><a id="_Toc50403169"></a><a id="_Toc50404601"></a><a id="_Toc50404721"></a><a id="_Toc50413300"></a>RN286

__Registro DAJUD \- Despesas de Ação Judicial da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 12 – Novembro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Novembro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780028"></a><a id="_Toc49802030"></a><a id="_Toc49802272"></a><a id="_Toc49802374"></a><a id="_Toc49802477"></a><a id="_Toc49802587"></a><a id="_Toc49803355"></a><a id="_Toc49803600"></a><a id="_Toc49804435"></a><a id="_Toc49805234"></a><a id="_Toc49805352"></a><a id="_Toc49805464"></a><a id="_Toc49805680"></a><a id="_Toc50403046"></a><a id="_Toc50403170"></a><a id="_Toc50404602"></a><a id="_Toc50404722"></a><a id="_Toc50413301"></a>RN287

__Registro DAJUD \- Despesas de Ação Judicial da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 13 – Dezembro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha Dezembro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780029"></a><a id="_Toc49802031"></a><a id="_Toc49802273"></a><a id="_Toc49802375"></a><a id="_Toc49802478"></a><a id="_Toc49802588"></a><a id="_Toc49803356"></a><a id="_Toc49803601"></a><a id="_Toc49804436"></a><a id="_Toc49805235"></a><a id="_Toc49805353"></a><a id="_Toc49805465"></a><a id="_Toc49805681"></a><a id="_Toc50403047"></a><a id="_Toc50403171"></a><a id="_Toc50404603"></a><a id="_Toc50404723"></a><a id="_Toc50413302"></a>RN288

__Registro DAJUD \- Despesas de Ação Judicial da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 14 – Décimo Terceiro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de 13º da tela “Rendimentos Recebidos Acumuladamente”

ATENÇÃO: Até recebermos definição da Receita sobre a existência ou não do campo de 13º, o campo deve ser gerado com ‘||’, mesmo possuindo valor correspondente na tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780030"></a><a id="_Toc49802032"></a><a id="_Toc49802274"></a><a id="_Toc49802376"></a><a id="_Toc49802479"></a><a id="_Toc49802589"></a><a id="_Toc49803357"></a><a id="_Toc49803602"></a><a id="_Toc49804437"></a><a id="_Toc49805236"></a><a id="_Toc49805354"></a><a id="_Toc49805466"></a><a id="_Toc49805682"></a><a id="_Toc50403048"></a><a id="_Toc50403172"></a><a id="_Toc50404604"></a><a id="_Toc50404724"></a><a id="_Toc50413303"></a>RN289

__Registro QTMESES – Quantidade de Meses da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

- Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário
- Deve ser associado ao registro do tipo BPFRRA

Gravar no campo 1 – Identificador do Registro o valor fixo “QTMESES”\.

OS3528

<a id="_Toc49780031"></a><a id="_Toc49802033"></a><a id="_Toc49802275"></a><a id="_Toc49802377"></a><a id="_Toc49802480"></a><a id="_Toc49802590"></a><a id="_Toc49803358"></a><a id="_Toc49803603"></a><a id="_Toc49804438"></a><a id="_Toc49805237"></a><a id="_Toc49805355"></a><a id="_Toc49805467"></a><a id="_Toc49805683"></a><a id="_Toc50403049"></a><a id="_Toc50403173"></a><a id="_Toc50404605"></a><a id="_Toc50404725"></a><a id="_Toc50413304"></a>RN290

__Registro QTMESES – Quantidade de Meses da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 2 – Quantidade meses \- Janeiro__ com a informação do campo “Quantidade de Meses” referente à linha de Janeiro da  tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780032"></a><a id="_Toc49802034"></a><a id="_Toc49802276"></a><a id="_Toc49802378"></a><a id="_Toc49802481"></a><a id="_Toc49802591"></a><a id="_Toc49803359"></a><a id="_Toc49803604"></a><a id="_Toc49804439"></a><a id="_Toc49805238"></a><a id="_Toc49805356"></a><a id="_Toc49805468"></a><a id="_Toc49805684"></a><a id="_Toc50403050"></a><a id="_Toc50403174"></a><a id="_Toc50404606"></a><a id="_Toc50404726"></a><a id="_Toc50413305"></a>RN291

__Registro QTMESES – Quantidade de Meses da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 3 – Quantidade meses \- Fevereiro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Fevereiro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780033"></a><a id="_Toc49802035"></a><a id="_Toc49802277"></a><a id="_Toc49802379"></a><a id="_Toc49802482"></a><a id="_Toc49802592"></a><a id="_Toc49803360"></a><a id="_Toc49803605"></a><a id="_Toc49804440"></a><a id="_Toc49805239"></a><a id="_Toc49805357"></a><a id="_Toc49805469"></a><a id="_Toc49805685"></a><a id="_Toc50403051"></a><a id="_Toc50403175"></a><a id="_Toc50404607"></a><a id="_Toc50404727"></a><a id="_Toc50413306"></a>RN292

__Registro QTMESES – Quantidade de Meses da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 4 – Quantidade meses \-  Março__ de acordo com a regra abaixo:

- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Março da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780034"></a><a id="_Toc49802036"></a><a id="_Toc49802278"></a><a id="_Toc49802380"></a><a id="_Toc49802483"></a><a id="_Toc49802593"></a><a id="_Toc49803361"></a><a id="_Toc49803606"></a><a id="_Toc49804441"></a><a id="_Toc49805240"></a><a id="_Toc49805358"></a><a id="_Toc49805470"></a><a id="_Toc49805686"></a><a id="_Toc50403052"></a><a id="_Toc50403176"></a><a id="_Toc50404608"></a><a id="_Toc50404728"></a><a id="_Toc50413307"></a>RN293

__Registro QTMESES – Quantidade de Meses da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 5 – Quantidade meses \- Abril__ de acordo com as regras abaixo:

- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Abril da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780035"></a><a id="_Toc49802037"></a><a id="_Toc49802279"></a><a id="_Toc49802381"></a><a id="_Toc49802484"></a><a id="_Toc49802594"></a><a id="_Toc49803362"></a><a id="_Toc49803607"></a><a id="_Toc49804442"></a><a id="_Toc49805241"></a><a id="_Toc49805359"></a><a id="_Toc49805471"></a><a id="_Toc49805687"></a><a id="_Toc50403053"></a><a id="_Toc50403177"></a><a id="_Toc50404609"></a><a id="_Toc50404729"></a><a id="_Toc50413308"></a>RN294

__Registro QTMESES – Quantidade de Meses da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 6 – Quantidade meses \- Maio__ de acordo com a regra abaixo:

- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Maio da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780036"></a><a id="_Toc49802038"></a><a id="_Toc49802280"></a><a id="_Toc49802382"></a><a id="_Toc49802485"></a><a id="_Toc49802595"></a><a id="_Toc49803363"></a><a id="_Toc49803608"></a><a id="_Toc49804443"></a><a id="_Toc49805242"></a><a id="_Toc49805360"></a><a id="_Toc49805472"></a><a id="_Toc49805688"></a><a id="_Toc50403054"></a><a id="_Toc50403178"></a><a id="_Toc50404610"></a><a id="_Toc50404730"></a><a id="_Toc50413309"></a>RN295

__Registro QTMESES – Quantidade de Meses da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 7 – Quantidade meses \- Junho__ de acordo com a regra abaixo:

- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Junho da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780037"></a><a id="_Toc49802039"></a><a id="_Toc49802281"></a><a id="_Toc49802383"></a><a id="_Toc49802486"></a><a id="_Toc49802596"></a><a id="_Toc49803364"></a><a id="_Toc49803609"></a><a id="_Toc49804444"></a><a id="_Toc49805243"></a><a id="_Toc49805361"></a><a id="_Toc49805473"></a><a id="_Toc49805689"></a><a id="_Toc50403055"></a><a id="_Toc50403179"></a><a id="_Toc50404611"></a><a id="_Toc50404731"></a><a id="_Toc50413310"></a>RN296

__Registro QTMESES – Quantidade de Meses da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 8 – Quantidade meses \- Julho__ de acordo com a regra abaixo:

- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Julho da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780038"></a><a id="_Toc49802040"></a><a id="_Toc49802282"></a><a id="_Toc49802384"></a><a id="_Toc49802487"></a><a id="_Toc49802597"></a><a id="_Toc49803365"></a><a id="_Toc49803610"></a><a id="_Toc49804445"></a><a id="_Toc49805244"></a><a id="_Toc49805362"></a><a id="_Toc49805474"></a><a id="_Toc49805690"></a><a id="_Toc50403056"></a><a id="_Toc50403180"></a><a id="_Toc50404612"></a><a id="_Toc50404732"></a><a id="_Toc50413311"></a>RN297

__Registro QTMESES – Quantidade de Meses da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 9 – Quantidade meses \- Agosto__ de acordo com a regra abaixo:

- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Agosto da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780039"></a><a id="_Toc49802041"></a><a id="_Toc49802283"></a><a id="_Toc49802385"></a><a id="_Toc49802488"></a><a id="_Toc49802598"></a><a id="_Toc49803366"></a><a id="_Toc49803611"></a><a id="_Toc49804446"></a><a id="_Toc49805245"></a><a id="_Toc49805363"></a><a id="_Toc49805475"></a><a id="_Toc49805691"></a><a id="_Toc50403057"></a><a id="_Toc50403181"></a><a id="_Toc50404613"></a><a id="_Toc50404733"></a><a id="_Toc50413312"></a>RN298

__Registro QTMESES – Quantidade de Meses da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 10 – Quantidade meses \- Setembro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Setembro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780040"></a><a id="_Toc49802042"></a><a id="_Toc49802284"></a><a id="_Toc49802386"></a><a id="_Toc49802489"></a><a id="_Toc49802599"></a><a id="_Toc49803367"></a><a id="_Toc49803612"></a><a id="_Toc49804447"></a><a id="_Toc49805246"></a><a id="_Toc49805364"></a><a id="_Toc49805476"></a><a id="_Toc49805692"></a><a id="_Toc50403058"></a><a id="_Toc50403182"></a><a id="_Toc50404614"></a><a id="_Toc50404734"></a><a id="_Toc50413313"></a>RN299

__Registro QTMESES – Quantidade de Meses da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 11 – Quantidade meses \-  Outubro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Outubro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780041"></a><a id="_Toc49802043"></a><a id="_Toc49802285"></a><a id="_Toc49802387"></a><a id="_Toc49802490"></a><a id="_Toc49802600"></a><a id="_Toc49803368"></a><a id="_Toc49803613"></a><a id="_Toc49804448"></a><a id="_Toc49805247"></a><a id="_Toc49805365"></a><a id="_Toc49805477"></a><a id="_Toc49805693"></a><a id="_Toc50403059"></a><a id="_Toc50403183"></a><a id="_Toc50404615"></a><a id="_Toc50404735"></a><a id="_Toc50413314"></a>RN300

__Registro QTMESES – Quantidade de Meses da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 12 – Quantidade meses \- Novembro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Novembro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780042"></a><a id="_Toc49802044"></a><a id="_Toc49802286"></a><a id="_Toc49802388"></a><a id="_Toc49802491"></a><a id="_Toc49802601"></a><a id="_Toc49803369"></a><a id="_Toc49803614"></a><a id="_Toc49804449"></a><a id="_Toc49805248"></a><a id="_Toc49805366"></a><a id="_Toc49805478"></a><a id="_Toc49805694"></a><a id="_Toc50403060"></a><a id="_Toc50403184"></a><a id="_Toc50404616"></a><a id="_Toc50404736"></a><a id="_Toc50413315"></a>RN301

__Registro QTMESES – Quantidade de Meses da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 13 – Quantidade meses \- Dezembro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Quantidade de Meses”, referente à linha Dezembro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

<a id="_Toc49780043"></a><a id="_Toc49802045"></a><a id="_Toc49802287"></a><a id="_Toc49802389"></a><a id="_Toc49802492"></a><a id="_Toc49802602"></a><a id="_Toc49803370"></a><a id="_Toc49803615"></a><a id="_Toc49804450"></a><a id="_Toc49805249"></a><a id="_Toc49805367"></a><a id="_Toc49805479"></a><a id="_Toc49805695"></a><a id="_Toc50403061"></a><a id="_Toc50403185"></a><a id="_Toc50404617"></a><a id="_Toc50404737"></a><a id="_Toc50413316"></a>RN375

__Registro INFPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 1 – Identificador do Registro__ o valor fixo “__INFPA__”\.

As informações desse registro serão recuperadas da tabela SAFX55 \(Arquivo de Dependente\)\.

Validação do Registro:

Deve estar classificado em ordem crescente de CPF e data de nascimento\.

Deve estar associado ao registro do tipo BPFRRA

MFS\-8989

<a id="_Toc49780044"></a><a id="_Toc49802046"></a><a id="_Toc49802288"></a><a id="_Toc49802390"></a><a id="_Toc49802493"></a><a id="_Toc49802603"></a><a id="_Toc49803371"></a><a id="_Toc49803616"></a><a id="_Toc49804451"></a><a id="_Toc49805250"></a><a id="_Toc49805368"></a><a id="_Toc49805480"></a><a id="_Toc49805696"></a><a id="_Toc50403062"></a><a id="_Toc50403186"></a><a id="_Toc50404618"></a><a id="_Toc50404738"></a><a id="_Toc50413317"></a>RN376

__Registro INFPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 2 – Campo CPF do Alimentado__

A informação deverá ser recuperada da \(SAFX55 campo 11\- NUM\_CPF\) – Módulo Básicos >> MastersafDW >> Manutenção >> Cadastro >> Controle de Funcionário >> Dependentes\.

MFS\-8989

<a id="_Toc49780045"></a><a id="_Toc49802047"></a><a id="_Toc49802289"></a><a id="_Toc49802391"></a><a id="_Toc49802494"></a><a id="_Toc49802604"></a><a id="_Toc49803372"></a><a id="_Toc49803617"></a><a id="_Toc49804452"></a><a id="_Toc49805251"></a><a id="_Toc49805369"></a><a id="_Toc49805481"></a><a id="_Toc49805697"></a><a id="_Toc50403063"></a><a id="_Toc50403187"></a><a id="_Toc50404619"></a><a id="_Toc50404739"></a><a id="_Toc50413318"></a>RN377

__Registro INFPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 3 – Campo Data de Nascimento__

A informação deverá ser recuperada da \(SAFX55 campo 08 \- DATA\_NASC\) – Módulo Básicos >> MastersafDW >> Manutenção >> Cadastro >> Controle de Funcionário >> Dependentes\.

MFS\-8989

<a id="_Toc49780046"></a><a id="_Toc49802048"></a><a id="_Toc49802290"></a><a id="_Toc49802392"></a><a id="_Toc49802495"></a><a id="_Toc49802605"></a><a id="_Toc49803373"></a><a id="_Toc49803618"></a><a id="_Toc49804453"></a><a id="_Toc49805252"></a><a id="_Toc49805370"></a><a id="_Toc49805482"></a><a id="_Toc49805698"></a><a id="_Toc50403064"></a><a id="_Toc50403188"></a><a id="_Toc50404620"></a><a id="_Toc50404740"></a><a id="_Toc50413319"></a>RN378

__Registro INFPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 4 – Campo Nome __

A informação deverá ser recuperada da \(SAFX55 campo 07\- NOME\) – Módulo Básicos >> MastersafDW >> Manutenção >> Cadastro >> Controle de Funcionário >> Dependentes\.

MFS\-8989

<a id="_Toc49780047"></a><a id="_Toc49802049"></a><a id="_Toc49802291"></a><a id="_Toc49802393"></a><a id="_Toc49802496"></a><a id="_Toc49802606"></a><a id="_Toc49803374"></a><a id="_Toc49803619"></a><a id="_Toc49804454"></a><a id="_Toc49805253"></a><a id="_Toc49805371"></a><a id="_Toc49805483"></a><a id="_Toc49805699"></a><a id="_Toc50403065"></a><a id="_Toc50403189"></a><a id="_Toc50404621"></a><a id="_Toc50404741"></a><a id="_Toc50413320"></a>RN379

__Registro INFPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 5 – Campo Relação de Dependência__

A informação deverá ser recuperada da \(SAFX55 campo 06 \- COD\_TIPO\_DEPEND\) – Módulo Básicos >> MastersafDW >> Manutenção >> Cadastro >> Controle de Funcionário >> Dependentes\.

MFS\-8989

<a id="_Toc49780048"></a><a id="_Toc49802050"></a><a id="_Toc49802292"></a><a id="_Toc49802394"></a><a id="_Toc49802497"></a><a id="_Toc49802607"></a><a id="_Toc49803375"></a><a id="_Toc49803620"></a><a id="_Toc49804455"></a><a id="_Toc49805254"></a><a id="_Toc49805372"></a><a id="_Toc49805484"></a><a id="_Toc49805700"></a><a id="_Toc50403066"></a><a id="_Toc50403190"></a><a id="_Toc50404622"></a><a id="_Toc50404742"></a><a id="_Toc50413321"></a>RN380

__Registro RTPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

RTPA \- Registro de Rendimentos Tributáveis \- Dedução \- Pensão Alimentícia

Gravar no __campo 1 – Identificador do Registro__ o valor fixo “__RTPA__”\.

#### Deverão ser recuperado as informações da tela “Rendimentos Recebidos Acumuladamente de Pensão Alimentícia por Dependente” localizada no Menu: DIRF do módulo Federal / Obrigações de Tributos Federais, com base no campo Ano Referência\-DIRF \(neste caso 2017\)\.

MFS\-8989

<a id="_Toc49780049"></a><a id="_Toc49802051"></a><a id="_Toc49802293"></a><a id="_Toc49802395"></a><a id="_Toc49802498"></a><a id="_Toc49802608"></a><a id="_Toc49803376"></a><a id="_Toc49803621"></a><a id="_Toc49804456"></a><a id="_Toc49805255"></a><a id="_Toc49805373"></a><a id="_Toc49805485"></a><a id="_Toc49805701"></a><a id="_Toc50403067"></a><a id="_Toc50403191"></a><a id="_Toc50404623"></a><a id="_Toc50404743"></a><a id="_Toc50413322"></a>RN381

__Registro RTPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 2 – Janeiro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Pensão Alimentícia”, referente à linha de Janeiro da tela “Rendimentos Recebidos Acumuladamente”

MFS\-8989

<a id="_Toc49780050"></a><a id="_Toc49802052"></a><a id="_Toc49802294"></a><a id="_Toc49802396"></a><a id="_Toc49802499"></a><a id="_Toc49802609"></a><a id="_Toc49803377"></a><a id="_Toc49803622"></a><a id="_Toc49804457"></a><a id="_Toc49805256"></a><a id="_Toc49805374"></a><a id="_Toc49805486"></a><a id="_Toc49805702"></a><a id="_Toc50403068"></a><a id="_Toc50403192"></a><a id="_Toc50404624"></a><a id="_Toc50404744"></a><a id="_Toc50413323"></a>RN382

__Registro RTPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 3 – Fevereiro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Pensão Alimentícia”, referente à linha de Fevereiro da tela “Rendimentos Recebidos Acumuladamente”

MFS\-8989

<a id="_Toc49780051"></a><a id="_Toc49802053"></a><a id="_Toc49802295"></a><a id="_Toc49802397"></a><a id="_Toc49802500"></a><a id="_Toc49802610"></a><a id="_Toc49803378"></a><a id="_Toc49803623"></a><a id="_Toc49804458"></a><a id="_Toc49805257"></a><a id="_Toc49805375"></a><a id="_Toc49805487"></a><a id="_Toc49805703"></a><a id="_Toc50403069"></a><a id="_Toc50403193"></a><a id="_Toc50404625"></a><a id="_Toc50404745"></a><a id="_Toc50413324"></a>RN383

__Registro RTPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 4 – Março__ de acordo com a regra abaixo:

- Gravar o valor do campo “Pensão Alimentícia”, referente à linha de Março da tela “Rendimentos Recebidos Acumuladamente”

MFS\-8989

<a id="_Toc49780052"></a><a id="_Toc49802054"></a><a id="_Toc49802296"></a><a id="_Toc49802398"></a><a id="_Toc49802501"></a><a id="_Toc49802611"></a><a id="_Toc49803379"></a><a id="_Toc49803624"></a><a id="_Toc49804459"></a><a id="_Toc49805258"></a><a id="_Toc49805376"></a><a id="_Toc49805488"></a><a id="_Toc49805704"></a><a id="_Toc50403070"></a><a id="_Toc50403194"></a><a id="_Toc50404626"></a><a id="_Toc50404746"></a><a id="_Toc50413325"></a>RN384

__Registro RTPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 5 – Abril__ de acordo com a regra abaixo:

- Gravar o valor do campo “Pensão Alimentícia”, referente à linha de Abril da tela “Rendimentos Recebidos Acumuladamente”

MFS\-8989

<a id="_Toc49780053"></a><a id="_Toc49802055"></a><a id="_Toc49802297"></a><a id="_Toc49802399"></a><a id="_Toc49802502"></a><a id="_Toc49802612"></a><a id="_Toc49803380"></a><a id="_Toc49803625"></a><a id="_Toc49804460"></a><a id="_Toc49805259"></a><a id="_Toc49805377"></a><a id="_Toc49805489"></a><a id="_Toc49805705"></a><a id="_Toc50403071"></a><a id="_Toc50403195"></a><a id="_Toc50404627"></a><a id="_Toc50404747"></a><a id="_Toc50413326"></a>RN385

__Registro RTPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 6 – Maio__ de acordo com a regra abaixo:

- Gravar o valor do campo “Pensão Alimentícia”, referente à linha de Maio da tela “Rendimentos Recebidos Acumuladamente”

MFS\-8989

<a id="_Toc49780054"></a><a id="_Toc49802056"></a><a id="_Toc49802298"></a><a id="_Toc49802400"></a><a id="_Toc49802503"></a><a id="_Toc49802613"></a><a id="_Toc49803381"></a><a id="_Toc49803626"></a><a id="_Toc49804461"></a><a id="_Toc49805260"></a><a id="_Toc49805378"></a><a id="_Toc49805490"></a><a id="_Toc49805706"></a><a id="_Toc50403072"></a><a id="_Toc50403196"></a><a id="_Toc50404628"></a><a id="_Toc50404748"></a><a id="_Toc50413327"></a>RN386

__Registro RTPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 7 – Junho__ de acordo com a regra abaixo:

- Gravar o valor do campo “Pensão Alimentícia”, referente à linha de Junho da tela “Rendimentos Recebidos Acumuladamente”

MFS\-8989

<a id="_Toc49780055"></a><a id="_Toc49802057"></a><a id="_Toc49802299"></a><a id="_Toc49802401"></a><a id="_Toc49802504"></a><a id="_Toc49802614"></a><a id="_Toc49803382"></a><a id="_Toc49803627"></a><a id="_Toc49804462"></a><a id="_Toc49805261"></a><a id="_Toc49805379"></a><a id="_Toc49805491"></a><a id="_Toc49805707"></a><a id="_Toc50403073"></a><a id="_Toc50403197"></a><a id="_Toc50404629"></a><a id="_Toc50404749"></a><a id="_Toc50413328"></a>RN387

__Registro RTPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 8 – Julho__ de acordo com a regra abaixo:

- Gravar o valor do campo “Pensão Alimentícia”, referente à linha de Julho da tela “Rendimentos Recebidos Acumuladamente”

MFS\-8989

<a id="_Toc49780056"></a><a id="_Toc49802058"></a><a id="_Toc49802300"></a><a id="_Toc49802402"></a><a id="_Toc49802505"></a><a id="_Toc49802615"></a><a id="_Toc49803383"></a><a id="_Toc49803628"></a><a id="_Toc49804463"></a><a id="_Toc49805262"></a><a id="_Toc49805380"></a><a id="_Toc49805492"></a><a id="_Toc49805708"></a><a id="_Toc50403074"></a><a id="_Toc50403198"></a><a id="_Toc50404630"></a><a id="_Toc50404750"></a><a id="_Toc50413329"></a>RN388

__Registro RTPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 9 – Agosto__ de acordo com a regra abaixo:

- Gravar o valor do campo “Pensão Alimentícia”, referente à linha de Agosto da tela “Rendimentos Recebidos Acumuladamente”

MFS\-8989

<a id="_Toc49780057"></a><a id="_Toc49802059"></a><a id="_Toc49802301"></a><a id="_Toc49802403"></a><a id="_Toc49802506"></a><a id="_Toc49802616"></a><a id="_Toc49803384"></a><a id="_Toc49803629"></a><a id="_Toc49804464"></a><a id="_Toc49805263"></a><a id="_Toc49805381"></a><a id="_Toc49805493"></a><a id="_Toc49805709"></a><a id="_Toc50403075"></a><a id="_Toc50403199"></a><a id="_Toc50404631"></a><a id="_Toc50404751"></a><a id="_Toc50413330"></a>RN389

__Registro RTPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 10 – Setembro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Pensão Alimentícia”, referente à linha de Setembro da tela “Rendimentos Recebidos Acumuladamente”

MFS\-8989

<a id="_Toc49780058"></a><a id="_Toc49802060"></a><a id="_Toc49802302"></a><a id="_Toc49802404"></a><a id="_Toc49802507"></a><a id="_Toc49802617"></a><a id="_Toc49803385"></a><a id="_Toc49803630"></a><a id="_Toc49804465"></a><a id="_Toc49805264"></a><a id="_Toc49805382"></a><a id="_Toc49805494"></a><a id="_Toc49805710"></a><a id="_Toc50403076"></a><a id="_Toc50403200"></a><a id="_Toc50404632"></a><a id="_Toc50404752"></a><a id="_Toc50413331"></a>RN390

__Registro RTPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 11 – Outubro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Pensão Alimentícia”, referente à linha de Outubro da tela “Rendimentos Recebidos Acumuladamente”

MFS\-8989

<a id="_Toc49780059"></a><a id="_Toc49802061"></a><a id="_Toc49802303"></a><a id="_Toc49802405"></a><a id="_Toc49802508"></a><a id="_Toc49802618"></a><a id="_Toc49803386"></a><a id="_Toc49803631"></a><a id="_Toc49804466"></a><a id="_Toc49805265"></a><a id="_Toc49805383"></a><a id="_Toc49805495"></a><a id="_Toc49805711"></a><a id="_Toc50403077"></a><a id="_Toc50403201"></a><a id="_Toc50404633"></a><a id="_Toc50404753"></a><a id="_Toc50413332"></a>RN391

__Registro RTPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 12 – Novembro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Pensão Alimentícia”, referente à linha de Novembro da tela “Rendimentos Recebidos Acumuladamente”

MFS\-8989

<a id="_Toc49780060"></a><a id="_Toc49802062"></a><a id="_Toc49802304"></a><a id="_Toc49802406"></a><a id="_Toc49802509"></a><a id="_Toc49802619"></a><a id="_Toc49803387"></a><a id="_Toc49803632"></a><a id="_Toc49804467"></a><a id="_Toc49805266"></a><a id="_Toc49805384"></a><a id="_Toc49805496"></a><a id="_Toc49805712"></a><a id="_Toc50403078"></a><a id="_Toc50403202"></a><a id="_Toc50404634"></a><a id="_Toc50404754"></a><a id="_Toc50413333"></a>RN392

__Registro RTPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 13 – Dezembro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Pensão Alimentícia”, referente à linha Dezembro da tela “Rendimentos Recebidos Acumuladamente”

MFS\-8989

<a id="_Toc49780061"></a><a id="_Toc49802063"></a><a id="_Toc49802305"></a><a id="_Toc49802407"></a><a id="_Toc49802510"></a><a id="_Toc49802620"></a><a id="_Toc49803388"></a><a id="_Toc49803633"></a><a id="_Toc49804468"></a><a id="_Toc49805267"></a><a id="_Toc49805385"></a><a id="_Toc49805497"></a><a id="_Toc49805713"></a><a id="_Toc50403079"></a><a id="_Toc50403203"></a><a id="_Toc50404635"></a><a id="_Toc50404755"></a><a id="_Toc50413334"></a>RN393

__Registro RTPA da hierarquia do RRA \- Rendimentos Recebidos Acumuladamente__

Gravar no __campo 14 – Décimo Terceiro__ de acordo com a regra abaixo:

- Gravar o valor do campo “Pensão Alimentícia”, referente à linha de 13º da tela “Rendimentos Recebidos Acumuladamente”

MFS\-8989

<a id="_Toc49780062"></a><a id="_Toc49802064"></a><a id="_Toc49802306"></a><a id="_Toc49802408"></a><a id="_Toc49802511"></a><a id="_Toc49802621"></a><a id="_Toc49803389"></a><a id="_Toc49803634"></a><a id="_Toc49804469"></a><a id="_Toc49805268"></a><a id="_Toc49805386"></a><a id="_Toc49805498"></a><a id="_Toc49805714"></a><a id="_Toc50403080"></a><a id="_Toc50403204"></a><a id="_Toc50404636"></a><a id="_Toc50404756"></a><a id="_Toc50413335"></a>RN301

Se o Beneficiário Pessoa Física não atingiu o “Valor do Anual Mínimo de Rendimentos”, porém existem informações no período de RRA,  todos os registros da DIRF deverão ser apresentados, independente do valor que possui de rendimentos por registros\.

OS3528

## <a id="_Toc50403000"></a><a id="_Toc50403124"></a><a id="_Toc50404757"></a><a id="_Toc155171997"></a>3\.23 – INF, FIMDIRF

<a id="_Toc49779813"></a>RN86

__Registro INF:__

Gravar no __campo 1 – Identificador de Registro__ o valor fixo “__INF__”\.

OS3528

<a id="_Toc49779814"></a>RN87

__Registro INF:__

Gravar no __campo 2 – CPF__ o CPF do Beneficiário Pessoa Física presente no registro BPFDEC\. Deverá ser gravado apenas um registro para cada CPF informado no registro BPFDEC\.

OS3528

<a id="_Toc49779815"></a>RN88

__Registro INF:__

Gravar no __campo 3 – Informações Complementares__ a informação de forma concatenada separando cada campo com “\-“ a partir dos campos preenchidos na tabela X22\_INF\_COMPL\.

- Caso o campo IND\_TIPO = “2” da X22\_INF\_COMPL
	- NUM\_PROC\_JUD
	- DAT\_DECISAO
	- TRIB\_JUST
	- VARA\_JUDICIAL
- Caso o campo IND\_TIPO = “1” da X22\_INF\_COMPL
	- CPF
	- NOME
	- VLR\_PENSAO
	- VLR\_PENSAO\_13

Caso ao gravar esse campo, a concatenação de campos ultrapasse 200 \(duzentos\) caracteres, o sistema deverá limitar a gravação desse campo em 200 caracteres, ignorando o restante\.

OS3528

CH4180\_2014

<a id="_Toc49779816"></a>RN89

__Registro FIMDIRF:__

Gravar no campo 1 – Identificador do Registro o valor fixo “FIMDirf”\.

OS3528

# <a id="_Toc50404758"></a><a id="_Toc155171998"></a>4 – Regras Gerais

<a id="_Toc49779711"></a>RNG\-01

__Tratamento das Retificações das Retenções \(X530\_RETIFICACAO\_IRRF\)__

Ao gerar os registros de retificações contidos na OS3267\-D, ou seja, quando as retenções a serem recuperadas serão da tabela __X530\_RETIFICACAO\_IRRF__ mais recente e não da X53\_RETENCAO\_IRRF, vale salientar que independente da Data de Retificação da Retenção informada na tabela __X530\_RETIFICACAO\_IRRF__, os valores serão informados nos respectivos registros da DIRF __do mês da retenção da X53\_RETENCAO\_IRRF e não do mês da retificação__\. Nesse caso em que a retificação for recuperada, serão considerados somente os valores da retificação mais recente, sendo que as outras informações, serão consideradas da retenção original \(SAFX53\)\.

Caso a retificação mais recente possua uma Data de Retificação cujo ano seja subsequente ao Ano\-Calendário da Retenção original, a mesma será recuperada e gerada na DIRF do ano\-calendário da retenção\.

Essa regra é existente devido à competência ser referente ao Pagamento Original que ocorreu para o Prestador\.

OS3267\-D

MFS\-90689

<a id="_Toc49779712"></a>RNG\-02

__Tratamento para Receita 6891__

Todos os registros da tabela X53\_RETENCAO\_IRRF, que possuírem o código de Receita 6891\(IRRF \- VIDA GERADOR DE BENEFÍCIO LIVRE \- VGBL\), devem ser apresentados no arquivo txt da DIRF \(nos seus respectivos registros, de acordo com as regras especificadas neste documento\), mesmo que durante o ano calendário não possuírem valor de retenção \(campos 15 \- VLR\_IR\_RETIDO e 47 \- VLR\_TRIBUTO\_13, com valor igual a zero, para o ano\-calendário\)\. 

CH28145\_2012

<a id="_Toc49779765"></a>RN39A

__Tratamento para PLR – registro IDREC:__

Ao gerar a DIRF através do processo de Geração da DIRF \(menu: DIRF >> Geração DIRF\) do módulo Obrigações de Tributos Federais, caso o funcionário recuperado da SAFX21 \(conforme premissas da RN39\) possua alguma verba com o parâmetro “Incide PLR” selecionado na tela “Parâmetros p/ Verba” \(menu: Parâmetros >> Parâmetros p/ Verba \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais, o código de receita desse funcionário que será gravado no registro IDREC \(ver RN30\-RN31\) será recuperado do campo “PLR” da tela “Geração da DIRF”\.

Essa regra só é válida para os registros recuperados da SAFX21\.

__OBS: __Vale salientar que os valores de Rendimentos Tributáveis, Imposto de Renda Retido na Fonte ou Pensão Alimentícia NÃO DEVERÃO SER SOMADOS aos valores sob outros códigos de receita, como por exemplo, o 0561 – conforme regra atual do sistema\.

OS4409

<a id="_Toc49779766"></a>RN39B

__Tratamento para PLR – registros RTRT, RTIRF, RTPA__

As verbas serão gravadas nos seus respectivos registros e meses de acordo com a regra abaixo:

- Caso a verba com o parâmetro “Incide PLR” esteja selecionado e o campo “Classe p/ DIRF” = “Rendimentos Tributáveis”, o valor contido no campo “Valor da Verba” do menu: Manutenção >> Folha de Pagamento >> Ficha Financeira será gravado no registro RTRT \(ver RN39 em diante para a SAFX21\)\.
- Caso a verba com o parâmetro “Incide PLR” esteja selecionado e o campo “Classe p/ DIRF” = “Deduções \(Pensão Alimentícia\)”, o valor contido no campo “Valor da Verba” do menu: Manutenção >> Folha de Pagamento >> Ficha Financeira será gravado no registro RTPA \(ver RN39 em diante para a SAFX21\)\.
- Caso a verba com o parâmetro “Incide PLR” esteja selecionado e o campo “Classe p/ DIRF” = “Imposto de Renda Retido”, o valor contido no campo “Valor da Verba” do menu: Manutenção >> Folha de Pagamento >> Ficha Financeira será gravado no registro RTIRF \(ver RN39 em diante para a SAFX21\)\.

Vale salientar que essa regra será válida para as DIRF’s geradas cujo ano\-calendário seja a partir de 2012 \(ano referência: 2013\) ou ano calendário 2013 \(ano referência: 2014 ou 2013\)\.

Essa regra só é válida para os registros recuperados da SAFX21\.

OS4409

<a id="_Toc49780063"></a><a id="_Toc49802065"></a><a id="_Toc49802307"></a><a id="_Toc49802409"></a><a id="_Toc49802512"></a><a id="_Toc49802622"></a><a id="_Toc49803390"></a><a id="_Toc49803635"></a><a id="_Toc49804470"></a><a id="_Toc49805269"></a><a id="_Toc49805387"></a><a id="_Toc49805499"></a><a id="_Toc49805715"></a><a id="_Toc50403081"></a><a id="_Toc50403205"></a><a id="_Toc50404639"></a><a id="_Toc50404759"></a><a id="_Toc50413338"></a>RN302

__Aba Resumo das Informações Dirf__

Módulo: Federal à Obrigações de Tributos Federais

Menu: DIRFà Geração DIRF

__Deduções:__ deverá ser informado o valor do campo \(VLR\_VERBA\) da SAFX21, conforme parametrização referente a deduções na tela Parâmetros/Verba \(Módulo >> Federal >> Obrigações de Tributos Federais –Menu >> Parâmetros\)\. 

__OS3960__

RN303

__Aba Resumo das Informações Dirf__

Na aba “Resumo das informações da DIRF“na tela de “Geração DIRF” Caminho: Módulo Federal à Obrigações de Tributos Federais Menu: DIRF à Geração Dirf

Inclusão das Informações referente a Quantidade e valores de “Rendimentos”, “Deduções” e “Retido” para Beneficiários Residentes no Exterior PF/PJ\.

o sistema deverá gerar as colunas “Rendimentos”, “Deduções” e “Imposto Retido” considerando a seguinte regra:

- __Rendimentos:__ deverá ser informado o somatório de todo o valor do campo Valor Bruto da tela de Controle de Tributos \(campo 14 – VLR\_BRUTO da SAFX53 ou __X530\_RETIFICACAO\_IRRF__ mais recente\) para o mês em questão\.
- __Deduções:__ deverá ser informado o somatório de todo o valor dos campos Valor INSS Retido – Terceiros, Valor Dependentes – Terceiros, Valor Previdência Privada e Valor Pensão Alimentícia da tela de Controle de Tributos \(campos 29 – VLR\_PREV\_PRIVADA, 30 – VLR\_PENS\_ALIMENT, 41 – VLR\_DED\_INSS\_TERC e 42 – VLR\_DED\_DEP\_TERC da SAFX53 ou __X530\_RETIFICACAO\_IRRF__ mais recente\) para o mês em questão\. Só será gerado está informação para beneficiário PF residente no Brasil\.
- __Imposto Retido:__ deverá ser informado o somatório de todo o valor do campo Valor Tributo da tela de Controle de Tributos \(campo 15 – VLR\_IR\_RETIDO da SAFX53 ou __X530\_RETIFICACAO\_IRRF__ mais recente\) para o mês em questão\.

Residentes no exterior pessoa Física e Jurídica \(UF=EX\)

O campo CPF/CNPJ\(SAFX04\) não deverá ser preenchido, para estes casos utiliza\-se a informação do ID Fiscal que quando preenchido considera\-se o beneficiário como pessoa física, quando não preenchida pessoa jurídica\.

OS3961

MFS\-90689

RN304

__Aba Resumo das Informações Dirf__

Na aba “Resumo das informações da DIRF“ na tela de “Geração DIRF” Caminho: Módulo Federal à Obrigações de Tributos Federais Menu: DIRF à Geração Dirf

__\[MFS\-81694\] __Retirar regra para listar os Beneficiários Não\-Informados, somente, quando o campo “VLR\_DED\_INSS\_TERC” estiver preenchido com valor > que ‘0’ \.

__Lista do Beneficiários Não Informados: __Apresentar a lista de “Beneficiários Não\-Informados”, sempre que o Campo ‘VLR\_IR\_RETIDO’ for igual à ‘0’, __E__ o Campo “VLR\_DED\_INSS\_TERC” estiver preenchido com valor > que ‘0’\.

__CPF/CNPJ:  __Recuperar informação do Campo “CPF\_CGC” da tabela X04\_PESSOA\_FIS\_JUR;

__Nome/Razão Social: __Recuperar informação do Campo “RAZAO\_SOCIAL” da tabela X04\_PESSOA\_FIS\_JUR;

__Cod\. Retenção: __Recuperar informação do Campo “COD\_DARF” da tabela X53\_RETENCAO\_IRRF;

__Rendimentos: __Recuperar informação do Campo “VLR\_BRUTO” da tabela X53\_RETENCAO\_IRRF;

__MFS\-81694__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


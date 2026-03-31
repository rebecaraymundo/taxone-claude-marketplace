# MTZ_Geracao_Anexos VI e VI-M

- **Fonte:** MTZ_Geracao_Anexos VI e VI-M.docx
- **Modificado:** 2026-01-26
- **Tamanho:** 512 KB

---

Combustíveis e Derivados de Petróleo

Geração dos Anexos VI e VI\-M para Refinarias

__Localização: Movimento de Refinaria > Geração Anexos VI, VI\-M__

Quadro de Revisões

__                         __

__Data__

__OS / Chamado__

__Descrição__

__Responsável__

29/05/2023

MFS535202

Geração do Anexo VI\-M para produtos com tributação monofásica\.

Liliane Assaf

03/07/2023

MFS547704

Leitura do Anexo V\-M com EAC para geração do Anexo VI\-M \(quadros 6\.1\.1, 6\.1\.2, 9\.1\.1 e 9\.1\.2\)

Ato Cotepe 44/23

Liliane Assaf

17/07/2023

MFS548195

Alterar o tratamento da leitura do arquivo das distribuidoras para considerar os anexos \(III, III\-M, V, V\-M, \.\.\.\) onde o CNPJ do Destinatário ou CNPJ do Fornecedor for igual ao CNPJ do estabelecimento, retirando a condição do valor da provisão ser maior que zero\.

Antes da MFS\-97574, apenas eram considerados os anexos \(III, III\-M, V, V\-M, \.\.\.\) cujo CNPJ do Fornecedor fosse igual ao CNPJ do estabelecimento\. 

A MFS\-97574 ampliou esse tratamento para considerar o caso em que o estabelecimento da geração não é o Fornecedor, mas é Destinatário do anexo, caso em que ocorre valor de provisão e não repasse\. Ao implementar esse tratamento, o valor provisionado maior que zero foi colocado como condição\.

Em reunião com a Acelen em 17/07/2023 sobre a MFS\-548195 voltamos a avaliar essa regra, e ficou claro que, independente do valor ser de repasse ou provisão, a refinaria é responsável pelo recolhimento do tributo quando ela é Fornecedora ou Destinatário do anexo da distribuidora\. 

Vide RN00\.

Liliane Assaf

MFS576550: Novo Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras

08/01/2024

MFS576550

Novo Relatório “Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras” – vide RN16\.

Liliane Assaf

19/01/2024

MFS604154

Alteração do preenchimento do campo UF Destinatária para a Geração do Anexo VI\-M \- Quadro 3 \(RN03\)\. Essa alteração está sendo feita para seguir a Base Legal:   
\- Convênio 15/23 \(Cláusula segunda: "IV \- nas operações com gasolina A o imposto caberá à UF onde ocorrer o consumo"\),   
\- Convênio 199/22 \(Cláusula segunda: "IV \- nas operações com óleo diesel A ou GLP, o imposto caberá à UFs onde ocorrer o consumo"\)\.

Andréa Rocha

07/03/2024

MFS616801

Alteração do preenchimento do campo UF Destinatária para a Geração do Anexo VI \- Quadro 3 \(RN03\)\. Essa alteração está sendo feita para seguir a definição dos CFOP 5667 e 6667, que devem informar a UF de efetivo consumo do combustível, para a geração dos produtos que não são monofásicos\.\.

Andréa Rocha

05/07/2024

MFS658449

Alteração do preenchimento do campo UF Destinatária para a Geração dos Anexos VI e VI\-M \- Quadros 10, 11, 12 e 13, para utilizar a UF de consumo quando estiver preenchida\. 

Andréa Rocha

18/03/2025

MFS783073

Geração dos Quadros 6\.1 e 9\.1 a partir da leitura do Anexo XI\-M\-AJ do arquivo das distribuidoras\. E alteração no tamanho do campo ID de 3 para 4 nos registros A3HD, A5HD, A11AHD, A3MHD, A5MHD, A5MAHD, A11MHD, e A11MAJHD\(novo registro\) do arquivo das distribuidoras\.

Liliane Assaf

13/10/2025

MFS917434

A geração Anexo VI\-M deve ser alterada para tratar os seguintes pontos:

1. Gerar os novos Quadros 3\.1 e 3\.2 do Anexo VI\-M \(ver [RN03\.1](#_RN03.1_-_Geração)\)
2. Atualizar Quadro 1 do Anexo VI\-M \(ver [RN01](#_RN01_-_Geração)\):

Inclusão da linha __1\.1\.1\.2__: Somatório dos registros do quadro 3\.1\.

Inclusão da linha __1\.2\.0\.1__: Somatório dos registros do quadro 3\.2\.

Atualização da linha __1\.1\.7__: adicionar o valor da linha 1\.1\.1\.2 no somatório das linhas 1\.1\.1, 1\.1\.2, 1\.1\.3, 1\.1\.4, 1\.1\.5, 1\.1\.6\.

Atualização da linha __1\.2\.8__: adicionar o valor da linha 1\.2\.0\.1 no somatório das linhas 1\.2\.1, 1\.2\.2, 1\.2\.3, 1\.2\.4, 1\.2\.5, 1\.2\.6, 1\.2\.7\.

Liliane Assaf

[1\.	Introdução	1](#_Toc211245058)

[2\.	Parâmetros de Tela	1](#_Toc211245059)

[3\.	Regras de Negócio	1](#_Toc211245060)

[RN00 – Regra Geral	1](#_Toc211245061)

[RN01 \- Geração do Anexo VI\-M \- Quadro 1	1](#_Toc211245062)

[RN02 \- Geração do Anexo VI\-M \- Quadro 2	1](#_Toc211245063)

[RN03 \- Geração do Anexo VI\-M \- Quadro 3	1](#_Toc211245064)

[RN03\.1 \- Geração do Anexo VI\-M \- Quadros 3\.1 e 3\.2	1](#_Toc211245065)

[RN04 \- Geração do Anexo VI\-M \- Quadro 4	1](#_Toc211245066)

[RN05 \- Geração do Anexo VI\-M \- Quadro 5	1](#_Toc211245067)

[RN06 \- Geração do Anexo VI\-M \- Quadro 6	1](#_Toc211245068)

[RN07 \- Geração do Anexo VI\-M \- Quadro 7	1](#_Toc211245069)

[RN08 \- Geração do Anexo VI\-M \- Quadro 8	1](#_Toc211245070)

[RN09 \- Geração do Anexo VI\-M \- Quadro 9	1](#_Toc211245071)

[RN10 \- Geração do Anexo VI\-M \- Quadro 10	1](#_Toc211245072)

[RN11 \- Geração do Anexo VI\-M \- Quadro 11	1](#_Toc211245073)

[RN12 \- Geração do Anexo VI\-M \- Quadro 12	1](#_Toc211245074)

[RN13 \- Geração do Anexo VI\-M \- Quadro 13	1](#_Toc211245075)

[RN14 \- Geração do Anexo VI\-M \- Quadro 14	1](#_Toc211245076)

[RN15 \- Geração do Anexo VI\-M \- Quadro 15	1](#_Toc211245077)

[RN16 \- Geração do Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras	1](#_Toc211245078)

[RN17 \- Geração do Anexo VI \- Quadro 3	1](#_Toc211245079)

[RN10 \- Geração do Anexo VI \- Quadro 10	1](#_Toc211245080)

[RN11 \- Geração do Anexo VI \- Quadro 11	1](#_Toc211245081)

[RN12 \- Geração do Anexo VI \- Quadro 12	1](#_Toc211245082)

[RN13 \- Geração do Anexo VI \- Quadro 13	1](#_Toc211245083)

# <a id="_Toc211245058"></a>Introdução 

O Anexo VI\-M vem para substituir o Anexo VI para os combustíveis no regime de tributação monofásica do ICMS\. Segundo a legislação que regulamenta o regime monofásico sobre combustíveis, o Diesel, Biodiesel e GLP/GLGN entram para o monofásico em Maio/2023, portanto, a partir desse mês devem ser apresentados no Anexo VI\-M e não mais no Anexo VI\. A Gasolina e EAC aderem ao monofásico do ICMS a partir de Junho/2023\. Uma vez que o combustível é apresentado no Anexo VI\-M ele deixa de compor o Anexo VI\.

Anexo VI\-M é gerado a partir de duas origens:

\- Arquivo txt que a refinaria exporta do “Sistema de Captação e Auditoria dos Anexos de Combustíveis – Módulo Refinaria \(SCANC REF\)” 

\- Notas fiscais das operações da refinaria e de ressarcimentos\.

O arquivo txt contém os seguintes anexos: III, III\-M, V, V\-M, V\-M\-AJ, XI\-A, XI\-M, XI\-M\-AJ \[MFS783073\]\. Um arquivo pode conter todos esses anexos, que devem ser lidos e as informações direcionada para o Anexo VI ou VI\-M\.

Os anexos III, V e XI\-A são utilizados para a geração do Anexo VI\. E os III\-M, V\-M, V\-M\-AJ e XI\-M e XI\-M\-AJ \[MFS783073\] para a geração do VI\-M\.

Anexo VI\-M \- Relação dos registros x origem da informação:

Quadro do Anexo VI\-M

Origem

A6MHD 

Registro de Header\. 

A6MQ1 

Registro totalizador de quadros

A6MQ2 

Registro totalizador de quadros

A6MQ3

Leitura de Notas Fiscais Saídas e devoluções de vendas\.

A6MQ41 1

Arquivo txt

A6MQ41 21

Arquivo txt

A6MQ41 22

Arquivo txt

A6MQ42  

Arquivo txt

A6MQ43

Essa rotina não gera, pois é extemporâneo

A6MQ5

Arquivo txt

A6MQ61

Arquivo txt

A6MQ62

Erra rotina não gera, pois é extemporâneo

A6MQ71 1

Arquivo txt

A6MQ71 21

Arquivo txt

A6MQ71 22

Arquivo txt

A6MQ72  

Arquivo txt

A6MQ73

Essa rotina não gera, pois é extemporâneo

A6MQ8

Arquivo txt

A6MQ91

Arquivo txt

A6MQ92

Essa rotina não gera, pois é extemporâneo

A6MQ10

Leitura de Notas de ressarcimento efetuado à Distribuidora

A6MQ11

Leitura de Notas de ressarcimento efetuado à TRR

A6MQ12

Leitura de Notas de ressarcimento efetuado à Importadores

A6MQ13

Leitura de Notas de ressarcimento efetuado à Outros Contribuintes

A6MQ14

Não gera dedução transferida de outro estabelecimento

A6MQ15

Não gera dedução transferida para outro estabelecimento

Relação dos quadros do Anexo VI\-M com os lidos do arquivo txt \(anexos III\-M, V\-M, V\-M\-AJ, XI\-M ou XI\-M\-AJ \[MFS783073\]\)

AnexoVI\-M – Quadro

\(gravação\)

Anexo de Origem \(III\-M,V\-M, V\-M\-AJ ou XI\-M\)

\(leitura do arquivo txt\)

OBS

A6MQ41 – 1

A6MQ71 – 1

A3MQ4 com VLR42

Mesmo valor do anexo III\-M vai para dois quadros do Anexo VI\-M\.

A6MQ41 \- 2\.1

A6MQ71 – 2\.1

A11MQ1com VLRQ31

Mesmo valor do anexo XI\-M vai para dois quadros do Anexo VI\-M\.

A6MQ41 \- 2\.2

A6MQ71 – 2\.2

A11MQ1com VLRQ32

Mesmo valor do anexo XI\-M vai para dois quadros do Anexo VI\-M\.

A6MQ42   

A6MQ72    

A3MQ4 com VLR43 não importadores

Mesmo valor do anexo III\-M vai para dois quadros do Anexo VI\-M\.

A6MQ5

A6MQ8

A3MQ4 com VLR43 importadores

Mesmo valor do anexo III\-M vai para dois quadros do Anexo VI\-M\.

A6MQ61

A6MQ91

A5MAQ1 com VLRQ3

Mesmo valor do anexo V\-M\-AJ vai para dois quadros do Anexo VI\-M\.

A6MQ61

A6MQ91

A5MQ4 com VLR42, VLR43

Mesmo valor do anexo V\-M vai para dois quadros do Anexo VI\-M\.

A6MQ61

A6MQ91

<a id="_Hlk193214070"></a>A11MAJQ2 com VLRQ2

\[MFS783073\]

Mesmo valor do anexo XI\-M\-AJ vai para dois quadros do Anexo VI\-M\.

Existe muita semelhança entre os anexos lidos do arquivo txt\. Segue as informações que são extraídas para gerar os anexos VI e VI\-M:

\[MFS783073\]: Alteração no tamanho do campo ID de 3 para 4 posições e reposicionamento dos campos posteriores\.

__ANEXO III__

__ANEXO III\-M__

__Registro__

__Pos ini\-fim \(tam\)__

__Registro__

__Pos ini\-fim \(tam\)__

A3HD

A3MHD 

MESANO

9\-14 \(6\)

MESANO

10 – 15 \(6\)

UFDESTPR

15\-16 \(2\)

UFDESTPR 

20\- 21 \(2\)

UFORIGEM

188\-189 \(2\)

ID

17\-20\(4\)

ID

16\- 19 \(4\)

__Emitente__

A3Q1

A3MHD 

CATEGORIA

9\-11 \(3\)

CATEGORIA 

24\-26 \(3\)

CNPJ

12\-25 \(14\)

CNPJ 

27\-40 \(14\)

UF

238\-239 \(2\)

UF

253\-254 \(2\)

RAZSOCIAL

55\-114 \(60\)

IE

41\-54 \(14\)

__Destinatário__

A3Q2

A3MQ1 

CNPJDEST

9\-22 \(14\)

CNPJDEST 

10\-23 \(14\)

__DADOS DO SUJEITO PASSIVO \(FORNECEDOR\)__

A3Q3

A3MQ2 

CNPJFOR

9\-22 \(14\)

CNPJFOR

10\-23 \(14\)

__APURAÇÃO DO IMPOSTO DAS OPERAÇÕES REALIZADAS NO PERÍODO __

A3Q4

Não utilizar

A3MQ3

não utilizar

__Resultado da Apuração__

A3Q5

A3MQ4 

VLR58

121\-135 \(15\)

VLR42

25\-38 \(14\)

SINALPN

136\-136 \(1\)

SINALPN

39\-39 \(1\)

VLR59

137\-151 \(15\)

VLR43

40\-53\(14\)

SINALPN

152\-152 \(1\)

SINALPN

54\-54 \(1\)

\[MFS783073\]: Alteração no tamanho do campo ID de 3 para 4 posições e reposicionamento dos campos posteriores\.

__ANEXO V__

__ANEXO V\-M\-AJ__

__ANEXO V\-M__

__Registro__

__Pos ini\-fim \(tam\)__

__Registro__

__Pos ini\-fim \(tam\)__

__Registro__

__Pos ini\-fim \(tam\)__

A5HD

A5MAHD 

A5MHD 

MESANO

9\-14 \(6\)

MESANO

11 – 16 \(6\)

MESANO

10 – 15 \(6\)

UFDESTPR

15\-16 \(2\)

UFDESTPR 

21\- 22 \(2\)

UFDESTPR 

20\- 21 \(2\)

ID

17\-20 \(4\)

ID

17\-20 \(4\)

ID

16\-19 \(4\)

UFORIGEM

188\-189 \(2\)

UFORIGEM 

23\-24 \(2\)

UFORIGEM 

22\-23 \(2\)

Emitente

A5Q1

A5MAHD 

A5MHD 

CNPJ

12\-25 \(14\)

CNPJ 

31\-44 \(14\)

CNPJ 

30\-43 \(14\)

UF

238\-239 \(2\)

UF

257\-258 \(2\)

UF

256\-257 \(2\)

RAZSOCIAL

40\-99

RAZSOCIAL

59\-118 \(60\)

RAZSOCIAL

58\-117 \(60\)

IE

45\-58 \(14\)

IE

44\- 57 \(14\)

CATEGORIA

9\-11 \(3\)

CATEGORIA

28\-30 \(3\)

CATEGORIA

27\-29 \(3\)

__Destinatário__

A5Q2

A5MAQ1 

A5MQ1 

CNPJDEST

9\-22 \(14\)

CNPJDEST 

11\-24 \(14\)

CNPJDEST 

10\-23 \(14\)

__DADOS DO SUJEITO PASSIVO \(FORNECEDOR\)__

A5Q3

Não Anexo V\-M\-AJ

A5MQ2

CNPJFOR

9\-22 \(14\)

CNPJFOR

10\-23 \(14\)

__APURAÇÃO DO IMPOSTO NO PERÍODO __

A5Q4

Não utilizar

Não Anexo V\-M\-AJ

__Resultado da Apuração__

A5Q5

A5MAQ1

A5MQ4 

VLR51

9\-23 \(15\)

VLRQ2

239\-252 \(14\)

VLR42

26\-40 \(15\)

SINALPN

24\-24 \(1\)

SINALPN

253\-253 \(1\)

SINALPN

41\-41 \(1\)

VLR52

25\-39 \(15\)

VLRQ3

254\-267\(14\)

VLR43

42\-56\(15\)

SINALPN

40\-40 \(1\)

SINALPN

268\-268 \(1\)

SINALPN

57\-57 \(1\)

\[MFS783073\]: Alteração no tamanho do campo ID de 3 para 4 posições e reposicionamento dos campos posteriores\.

__ANEXO XI__

__ANEXO XI\-M__

__Registro__

__Pos ini\-fim \(tam\)__

__Registro__

__Pos ini\-fim \(tam\)__

A11AHD

A11MHD 

MESANO

11 – 16 \(6\)

MESANO

11 – 16 \(6\)

UFDESTPR

17\-18 \(2\)

UFDESTPR 

21\-22 \(2\)

ID

19\-22 \(4\)

ID

17\-20 \(4\)

UFORIGEM

23\-24 \(2\)

CATEGORIA 

192\-194 \(3\)

CATEGORIA 

25\-27 \(3\)

__Emitente__

A11AQ1

A11MHD 

CNPJ

11\-24 \(14\)

CNPJ 

28\-41 \(14\)

UF

229\-230 \(2\)

UF

254\-255 \(2\)

RAZSOCIAL

56\-115 \(60\)

IE

42\-55 \(14\)

__Destinatário__

A11AQ1

A11MQ1 

CNPJREF

239\-252 \(14\)

CNPJDEST 

11\-24 \(14\)

__APURAÇÃO DO IMPOSTO NO PERÍODO __

A11AQ2

Não utilizar

__Resultado da Apuração__

A11AQ3

A11MQ1 

VLR35

110\-124 \(15\)

VLRQ31

271\-285 \(15\)

SINALPN

125\-125 \(1\)

SINALPN

286\-286 \(1\)

VLRQ32

287\-301 \(15\)

SINALPN

302

\[MFS783073\]: Geração dos Quadros 6\.1 e 9\.1 a partir da leitura do Anexo XI\-M\-AJ do arquivo das distribuidoras\.

__ANEXO XI\-M\-AJ__

__Registro__

__Pos ini\-fim \(tam\)__

A11MAJHD 

 05\-12 \(8\)

IDGRUPO

1\-4 \(4\)

MESANO

13\-18 \(6\)

ID

19\-22 \(4\)

UFDESTPR 

 23 \- 24\(2\)

UFORIGEM 

 25\-26\(2\)

__Emitente \(Distribuidora\)__

A11MAJHD 

 05\-12 \(8\)

CATEGORIA

 27\-29\(3\)

CNPJ 

 30\-43\(14\)

RAZSOCIAL

 58\-117 \(60\)

UF

 256\-257\(2\)

__Quadro 1 e 2 \- Destinatário \(Refinaria\) e Apuração do Imposto__

 A11MAJQ2

05\-12 \(8\)

CNPJDEST \*

 13\-26\(14\)

VLRQ2

241\-255 \(15\)

SINALPN

 256\-256\(1\)

\* CNPJDEST = CNPJ do Estabelecimento da Geração

# <a id="_Toc211245059"></a>Parâmetros de Tela

Parâmetros demonstrados na tela:

- Mês/Ano Referência
- Excluir Registros Inseridos pela Manutenção

# <a id="_Toc211245060"></a>Regras de Negócio

## <a id="_Toc211245061"></a>RN00 – Regra Geral

O anexo da distribuidora lido do arquivo TXT será considerado para a geração do Anexo VI, VI\-M da refinaria caso essa seja identificada como Destinatária ou Fornecedora no anexo da distribuidora\.

Para isso o CNPJ do estabelecimento da refinaria selecionado para geração deve ser igual ao CNPJ do Destinatário ou do Fornecedor, presente nos seguintes quadros dos anexos da distribuidora:

![Uma imagem contendo Diagrama

Descrição gerada automaticamente](data:image/png;base64,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)

\[MFS783073\]: Geração dos Quadros 6\.1 e 9\.1 a partir da leitura do Anexo XI\-M\-AJ do arquivo das distribuidoras\.

Anexo

A11MAJ

CNPJ Destintatário

CNPJDEST

A11MAJQ2

 \(13\-26\)

CNPJ Fornecedor

Não tem

Todo anexo da distribuidora lido do arquivo txt será gravado na tabela CBT\_CARGA\_ARQUIVO para permitir a emissão do relatório de conferência disponível na opção de menu Relatórios >> Conferência dos Anexos VI, VI\-M, VII, VII\-M \(Refinaria\)\.

Os anexos VI e VI\-M gerados nessa opção estão disponíveis no menu Relatórios >> Conferência dos Anexos VI, VI\-M, VII, VII\-M \(Refinaria\)\.

## <a id="_RN01_-_Geração"></a><a id="_Toc211245062"></a>RN01 \- Geração do Anexo VI\-M \- Quadro 1

O Quadro 1 é uma totalização de quadros 3 ao 15\. 

Para cada UF que o estabelecimento tenha Inscrição Estadual, devem ser gerados os quadros 1 e 2, mesmo que zerados, ou seja para um período/UF SEM MOVIMENTO\. Esse procedimento já era adotado para o Anexo VI, e vale também para o VI\-M, com base em esclarecimento recebido por email do Sr Lino Silva Neto \([lino\.neto@fazenda\.mg\.gov\.br](mailto:lino.neto@fazenda.mg.gov.br)\) \.

Gravar os campos do Quadro 1 conforme regras abaixo\. O registro gerado está disponível para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 1 e 2\.

Tabela: CBT\_ANEXO6M\_QUADR1

__Nome do Campo__

__Nome físico do campo__

__Regra de Preenchimento __

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano informado na tela de geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF Destinatária do Anexo VI\-M recuperada dos quadros selecionados nos campos abaixo\.

Vlr 1\.1\.1 

ICMS SOBRE OPERAÇÕES POR TRIBUTAÇÃO MONOFÁSICA PRÓPRIAS E RETIDAS \(QUADRO 3\)

vlr\_icms\_st\_111      

Consultar o __Quadro 3__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração\.

Recuperar Vlr ICMS Total \(ICMS Cobrado \+ Retido\) totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS Total \(ICMS Cobrado \+ Retido\)\.

__\[MFS917434\]__

Vlr 1\.1\.1\.2 

ICMS SOBRE OPERAÇÕES COM GLGN DEVIDO A UF DE ORIGEM \(QUADRO 3\.1\)

vlr\_icms\_st\_1112      

Consultar o __Quadro 3\.1__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ31\.

Recuperar Vlr ICMS Total \(ICMS Cobrado \+ Retido\) totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS Total \(ICMS Cobrado \+ Retido\)\.

Vlr 1\.1\.2

REPASSE DE ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs \(QUADRO 4\.1\.1\)

vlr\_icms\_st\_112    

Consultar o __Quadro 4\.1\.1__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ41 e COD\_QUADRO = 1\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.1\.3

REPASSE DE ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS DE GÁS \(QUADRO 4\.1\.2\.\)

vlr\_icms\_st\_113

Consultar os __Quadros 4\.1\.2\.1__ e __4\.1\.2\.2 __com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ41 e COD\_QUADRO = 21 e 22\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.1\.4

REPASSE DE ICMS DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS \(QUADRO 4\.3\)

vlr\_icms\_st\_114    

Consultar o __Quadro 4\.3__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ43\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.1\.5

REPASSE DE ICMS SOBRE BIOCOMBUSTÍVEIS DECORRENTE DE AJUSTES DE REPARTIÇÃO DE RECEITA \(QUADRO 6\.1\)

vlr\_icms\_st\_115

Consultar o __Quadro 6\.1__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ61\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.1\.6

REPASSE DE ICMS SOBRE BIOCOMBUSTÍVEIS DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS \(QUADRO 6\.2\)

vlr\_icms\_st\_116

Consultar o __Quadro 6\.2__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ62\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

__\[MFS917434\]__

Vlr 1\.1\.7

SUB\-TOTAL \(1\.1\.1\+1\.1\.1\.2 \+ 1\.1\.2 \+ 1\.1\.3 \+ 1\.1\.4 \+ 1\.1\.5 \+ 1\.1\.6\)

vlr\_icms\_st\_117

Somatório dos campos Vlr 1\.1\.1, Vlr 1\.1\.1\.2, Vlr 1\.1\.2, Vlr 1\.1\.3, Vlr 1\.1\.4, Vlr 1\.1\.5 e Vlr 1\.1\.6\.

__\[MFS917434\]__

Vlr 1\.2\.0\.1 

DEDUÇÃO DE ICMS SOBRE OPERAÇÕES COM GLGN DEVIDO A UF DE ORIGEM \(QUADRO 3\.2\)

vlr\_icms\_st\_1201      

Consultar o __Quadro 3\.2__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ32\.

Recuperar Vlr ICMS Total \(ICMS Cobrado \+ Retido\) totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS Total \(ICMS Cobrado \+ Retido\)\.

Vlr 1\.2\.1

DEDUÇÃO DE ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs A SER REPASSADO A OUTRAS UFs \(QUADRO 7\.1\.1\)

vlr\_icms\_st\_121

Consultar o __Quadro 7\.1\.1__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ71 e COD\_QUADRO = 1\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.2

DEDUÇÃO DE ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS DE GÁS \(QUADRO 7\.1\.2\)

vlr\_icms\_st\_122

Consultar os __Quadros 7\.1\.2\.1__ e 7__\.1\.2\.2 __com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ71 e COD\_QUADRO = 21 e 22\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.3

DEDUÇÃO DE ICMS DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS \(QUADRO 7\.3\)

vlr\_icms\_st\_123

Consultar o __Quadro 7\.3__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ73\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.4

DEDUÇÃO DE ICMS SOBRE BIOCOMBUSTÍVEIS DECORRENTE DE AJUSTES DE REPARTIÇÃO DE RECEITA \(QUADRO 9\.1\)

vlr\_icms\_st\_124

Consultar o __Quadro 9\.1__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ91\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.5

DEDUÇÃO DE ICMS SOBRE BIOCOMBUSTÍVEIS DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS \(QUADRO 9\.2\)

vlr\_icms\_st\_125

Consultar o __Quadro 9\.2__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ92\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.6

PROVISÃO PARA REPASSE POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs \(QUADRO 7\.2\)

vlr\_icms\_st\_126

Consultar o __Quadro 7\.2__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ72\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.7

PROVISÃO PARA REPASSE POR OPERAÇÕES REALIZADAS POR IMPORTADORES \(QUADRO 8\)

vlr\_icms\_st\_127

Consultar o __Quadro 8__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ8\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

__\[MFS917434\]__

Vlr 1\.2\.8

SUB\-TOTAL DAS DEDUÇÕES \(1\.2\.0\.1\+1\.2\.1 \+ 1\.2\.2 \+ 1\.2\.3 \+ 1\.2\.4 \+ 1\.2\.5 \+ 1\.2\.6 \+ 1\.2\.7\)

vlr\_icms\_st\_128

Somatório dos campos Vlr1\.2\.0\.1, Vlr 1\.2\.1, Vlr 1\.2\.2, Vlr 1\.2\.3, Vlr 1\.2\.4, Vlr 1\.2\.5, Vlr 1\.2\.6 e Vlr 1\.2\.7\.

Vlr 1\.2\.9

ICMS RESSARCIDO A DISTRIBUIDORAS \(QUADRO 10\)

vlr\_icms\_st\_129

Consultar o __Quadro 10__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ10\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.10

ICMS RESSARCIDO A TRRs \(QUADRO 11\)

vlr\_icms\_st\_1210

Consultar o __Quadro 11__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ11\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.11

ICMS RESSARCIDO A IMPORTADORES \(QUADRO 12\)

vlr\_icms\_st\_1211

Consultar o __Quadro 12__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ12\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.12

ICMS RESSARCIDO A OUTROS CONTRIBUINTES \(QUADRO 13\)

vlr\_icms\_st\_1212

Consultar o __Quadro 13__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ13\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.13

__SUB\-TOTAL DOS RESSARCIMENTOS \(1\.2\.9 \+ 1\.2\.10 \+ 1\.2\.11 \+ 1\.2\.12\)__

vlr\_icms\_st\_1213

Somatório dos campos Vlr 1\.2\.9, Vlr 1\.2\.10, Vlr 1\.2\.11, Vlr 1\.2\.12

Vlr 1\.3

__ICMS DEVIDO \[1\.1\.7 \- \(1\.2\.8 \+ 1\.2\.13\)\]__

vlr\_icms\_st\_13

Preencher com Vlr 1\.1\.7 \- Vlr 1\.2\.8 \- Vlr 1\.2\.13

Vlr 1\.3\.1

DEDUÇÃO TRANSFERIDA DE OUTRO ESTABELECIMENTO DO SUJEITO PASSIVO POR TRIBUTAÇÃO MONOFÁSICA \(QUADRO 14\)

vlr\_icms\_st\_131

Consultar o __Quadro 14__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ14\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.3\.2

DEDUÇÃO TRANSFERIDA PARA OUTRO ESTABELECIMENTO DO SUJEITO PASSIVO POR TRIBUTAÇÃO MONOFÁSICA \(QUADRO 15\)

vlr\_icms\_st\_132

Consultar o __Quadro 15__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ15\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.3\.3

__ICMS A RECOLHER \(1\.3 \+ 1\.3\.1\) ou \(1\.3 \- 1\.3\.2\)__

vlr\_icms\_st\_133

Preencher com: Vlr 1\.3 \+ Vlr 1\.3\.1 ou 

                          Vlr 1\.3 \- Vlr 1\.3\.2

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

## <a id="_Toc211245063"></a>RN02 \- Geração do Anexo VI\-M \- Quadro 2

O Quadro 2 é uma totalização de quadros 4\.2 e 5\.

Para cada UF que o estabelecimento tenha Inscrição Estadual, devem ser gerados os quadro 1 e 2, mesmo que zerados, ou seja para um período/UF SEM MOVIMENTO\. Esse procedimento já era adotado para o Anexo VI, e vale também para o VI\-M, com base em esclarecimento recebido por email do Sr Lino Silva Neto \([lino\.neto@fazenda\.mg\.gov\.br](mailto:lino.neto@fazenda.mg.gov.br)\) \.

Gravar os campos do Quadro 2 conforme regras abaixo\. O registro gerado está disponível para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 1 e 2\.

Tabela: CBT\_ANEXO6M\_QUADR2

__Nome do Campo__

__Nome físico do campo__

__Regra de Preenchimento __

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF Destinatária do Anexo VI\-M recuperada dos quadros selecionados nos campos abaixo\.

Vlr 2\.1

ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs \(QUADRO 4\.2\)

vlr\_icms\_st\_21

Consultar o __Quadro 4\.2__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ42\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 2\.2

ICMS SOBRE OPERAÇÕES REALIZADAS POR IMPORTADORES \(QUADRO 5\)

vlr\_icms\_st\_22

Consultar o __Quadro 5__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ5\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 2\.3

ICMS PROVISIONADO \(2\.1 \+ 2\.2\)

vlr\_icms\_st\_23

Preencher com Vlr 2\.1 \+ Vlr 2\.2

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

## <a id="_Toc211245064"></a>RN03 \- Geração do Anexo VI\-M \- Quadro 3

Quadro gerado a partir das Notas de Saídas e devoluções de vendas de Produtos sujeitos a tributação monofásica\.

Segundo a legislação que regulamenta o regime monofásico sobre combustíveis, o Diesel, Biodiesel e GLP/GLGN entram nesse regime em Maio/2023, portando, a partir desse mês devem ser apresentados no Anexo VI\-M e não mais no Anexo VI\. A Gasolina e EAC entram aderem ao monofásico do ICMS a partir de Junho/2023\. Uma vez que o combustível é apresentado no Anexo VI\-M ele deixa de compor o Anexo VI\.

Os principais critérios para identificação da nota nesse novo regime são: os CSTs e o produto enquadrado na lista de produtos\.

__Critérios de Seleção:__

Para geração desse quadro recuperar os documentos fiscais a partir das tabelas SAFX07, SAFX08, SAFX325, considerando os seguintes critérios:

\- Código da empresa = código da empresa da geração; 

\- Código do estabelecimento: depende do parâmetro “Inscrição Estadual Única” informado na tela de geração\.

   Se parâmetro desmarcado, então considerar apenas notas do estabelecimento selecionado na geração;

   Se parâmetro marcado, considerar as notas do estabelecimento centralizador selecionado na geração e dos estabelecimentos centralizados\. 

\- Data Fiscal compreendida no mês/ano Referência informado na geração;

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Somente notas com item de mercadoria \(SAFX08\);

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu: Parâmetros > Anexos I, II, III, IV, V, VI e VIII para os tipos:

  88 \- Saída,

  90 \- devolução de venda,

  92 – saída a consumidor final, 

  93 \- devolução de venda para consumidor final

\- Somente notas com Informações de Tributação do ICMS Monofásico \(__SAFX325__\);

\- Código da Sit\. Estadual “B” \(campo 1 da SAFX08\) = __‘02’, ‘15’, ‘53’__;

\- Considerar a Parametrização da Regras p/ Geração dos Anexos feita para o estabelecimento no item de menu: Parâmetros > Regras p/ Geração dos Anexos\. 

   Se o Campo “Considerar somente as Notas Fiscais com movimentação física de mercadoria” estiver marcado, então recuperar 

   apenas itens de mercadoria com Ind\. Movim\. Física da Merc\. \(campo 115\-IND\_MOV\_FIS da SAFX08\) = ‘S’;

   Se desmarcado, recuperar independente do Ind\. Movim\. Física da Merc\. \(campo 115\-IND\_MOV\_FIS da SAFX08\) ser S ou N\.

\- Produto do item da nota deve ser parametrizado no item de menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados, com o seu respectivo grupo de combustíveis \(SAFX96\)

\- O Grupo de Combustível parametrizado para o produto, deve estar com o flag Anexo VI\-M selecionado, no menu Parâmetros 🡪 Grupos de Combustíveis e Derivados\.

Ao recuperar a nota fiscal com os critérios acima, fazer a seguinte consistência:

Se a UF Pessoa Fis/Jur da não estiver preenchida exibir mensagem no log de erros e ignorar registro:

Existe pessoa juridica com a informacao de estado nula, estes registros serao ignorados na geracao, favor verificar

__\[MFS604154\] __Alteração do tratamento do campo UF Destinatária para verificar a UF de consumo da nota\.  Se a UF Ponto de Consumo não estiver preenchida, utilizar a UF da Pessoa Fis/Jur da nota, que era o campo utilizado anteriormente\.

Gravar os campos do Quadro 3 conforme regras abaixo\. O registro gerado está disponível para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadro 3\.

Tabela: CBT\_ANEXO6M\_QUADR3

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF do Ponto de Consumo da nota \(campo 207 \- UF\_CONSUMO da SAFX07\), se não estiver preenchida utilizar a UF da Pessoa Fis/Jur da nota

Grupo Combustível

Ident\_grupo\_comb

Identificador do Grupo de Combustivel da parametrização do produto\.

Quantidade \(Base de Cálculo\)

Qtd\_comb

Quantidade do Item de Mercadoria \(item 24 da SAFX08\)

Se medida do item for diferente da parametrizada para o produto \(Parâmetros > Produtos x Grupos de Combustíveis e Derivados SAFX96\) aplicar a conversão de unidades de medida\.

Vlr ICMS Cobrado

Vlr\_ICMS

Valor do ICMS Próprio Devido \(campo 23\-VLR\_ICMS\_MONO da SAFX325\)

Gravar o valor com sinal positivo ou negativo dependendo da parametrização do CFOP ou CFOP/NAT:

\+ se  parametrizado para saída \(88, 92\)

\- se  parametrizado para devolução \(90, 93\)

Vlr ICMS Retido

Vlr\_ICMS\_Ret

Valor do ICMS com retenção \(campo 26\- VLR\_ICMS\_MONO\_RETEN da SAFX325\)

Gravar o valor com sinal positivo ou negativo dependendo da parametrização do CFOP ou CFOP/NAT:

\+ se  parametrizado para saída \(88, 92\)

\- se  parametrizado para devolução \(90, 93\)

Vlr ICMS Total

Vlr\_ICMS\_Tot

Soma dos dois campos anteriores \(ICMS Cobrado \+ Retido\)

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

__\[MFS917434\]: inclusão da RN03\.1__

## <a id="_RN03.1_-_Geração"></a><a id="_Toc211245065"></a>RN03\.1 \- Geração do Anexo VI\-M \- Quadros 3\.1 e 3\.2

Quadros gerados a partir das Notas de Saídas e devoluções de vendas de Produto GLP/GLGN que tenha em sua composição GLGNn e GLGNi, quando a UF origem do GLGNn e GLGNi for diferente da UF destino da operação\.

Os principais critérios para identificação da nota nesse novo regime são: os CSTs e o produto enquadrado na lista de produtos\.

__Critérios de Seleção:__

Para geração desse quadro recuperar os documentos fiscais a partir das tabelas SAFX07, SAFX08, SAFX325, SAFX326 considerando os seguintes critérios:

\- Código da empresa = código da empresa da geração; 

\- Código do estabelecimento: depende do parâmetro “Inscrição Estadual Única” informado na tela de geração\.

   Se parâmetro desmarcado, então considerar apenas notas do estabelecimento selecionado na geração;

   Se parâmetro marcado, considerar as notas do estabelecimento centralizador selecionado na geração e dos estabelecimentos centralizados\. 

\- Data Fiscal compreendida no mês/ano Referência informado na geração;

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Somente notas com item de mercadoria \(SAFX08\);

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu: Parâmetros > Anexos I, II, III, IV, V, VI e VIII para os tipos:

  88 \- Saída,

  90 \- devolução de venda,

  92 – saída a consumidor final, 

  93 \- devolução de venda para consumidor final

\- Somente notas com Informações de Tributação do ICMS Monofásico \(__SAFX325__\);

\- Código da Sit\. Estadual “B” \(campo 1 da SAFX08\) = __‘02’, ‘15’, ‘53’, ‘61’__

\- Considerar a Parametrização da Regras p/ Geração dos Anexos feita para o estabelecimento no item de menu: Parâmetros > Regras p/ Geração dos Anexos\. 

   Se o Campo “Considerar somente as Notas Fiscais com movimentação física de mercadoria” estiver marcado, então recuperar 

   apenas itens de mercadoria com Ind\. Movim\. Física da Merc\. \(campo 115\-IND\_MOV\_FIS da SAFX08\) = ‘S’;

   Se desmarcado, recuperar independente do Ind\. Movim\. Física da Merc\. \(campo 115\-IND\_MOV\_FIS da SAFX08\) ser S ou N\.

\- Produto do item da nota deve ser parametrizado no item de menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados, com o seu respectivo grupo de combustíveis \(SAFX96\)

\- O Grupo de Combustível parametrizado para o produto, no menu Parâmetros 🡪 Grupos de Combustíveis e Derivados deve atender aos dois critérios abaixo:

- Indicador Anexo VI\-M selecionado;__ __
- Código Produto SEF igual a__ GPN__ 

\-  Pelo menos um dos percentuais diferentes de zero:

   Percentual do GLGNn na composição do GLP/GLGN \(campo 18\- PERC\_GLGN\_N da SAFX325\) diferente de zero;

   ou

   Percentual do GLGNi na composição do GLP/GLGN  \(campo 19\- PERC\_GLGN\_I da SAFX325\) diferente de zero;

\- UF destino Diferente da UF Origem\. Sendo que:

- <a id="uf_destino_31"></a>UF Destino: \(\*\)

Se UF do Ponto de Consumo da nota \(campo 207 \- UF\_CONSUMO da SAFX07\) estiver preenchida, então:

UF Destino = UF do Ponto de Consumo da nota \(campo 207 \- UF\_CONSUMO da SAFX07\)\.  

Se UF do Ponto de Consumo da nota \(campo 207 \- UF\_CONSUMO da SAFX07\) NÃO estiver preenchida, então:

UF Destino = UF da Pessoa Fis/Jur da nota\.

- <a id="uf_origem_31"></a>UF Origem: \(\*\*\)

Considerar UF de Origem \(campo 17 \- COD\_UF\_ORIG\) da Tabela de Origem dos Combustíveis Sujeitos à Tributação Monofásica do ICMS \(SAFX326\)\. 

Podem existir vários registros na SAFX326 para um item de mercadoria da SAFX08\.

Para o GLGNn \(Percentual do GLGNn na composição do GLP/GLGN \(campo 18\- PERC\_GLGN\_N da SAFX325\) diferente de zero\): 

Recuperar os registros da SAFX326 com Indicador da Origem \(campo 16 \- IND\_ORIG da SAFX326\) = 0 – Nacional\.

Para o GLGNi \(Percentual do GLGNi na composição do GLP/GLGN  \(campo 19\- PERC\_GLGN\_I da SAFX325\) diferente de zero\):

Recuperar os registros da SAFX326 com Indicador da Origem \(campo 16 \- IND\_ORIG da SAFX326\) = 1 – Importado\.

Ao recuperar a nota fiscal com os critérios acima, fazer a seguinte consistência:

Se UF Destino estiver nula:

*Para gerar os quadros 3\.1 e 3\.2, a UF Destino é obrigatória e não foi informada no documento fiscal\. Preencher UF do Ponto de Consumo \(207 \- UF\_CONSUMO da SAFX07\) ou a UF da Pessoa Fis\.Jur\(SAFX04\)\.*

Se UF Origem estiver nula:

*Para gerar os quadros 3\.1 e 3\.2, a UF Origem é obrigatória e não foi informada no documento fiscal\. Preencher as UFs de Origens na SAFX326\.*

Gravar o registro no quadro 3\.1 consolidandos as notas recuperadas da seguinte forma:

Para GLGNn \(Percentual do GLGNn na composição do GLP/GLGN \(campo 18\- PERC\_GLGN\_N da SAFX325\) diferente de zero\):

	Gravar um registro para cada UF Origem e UF Destino

Descrição do Produto = GNGNn

UF Destinatária do Anexo VI\-M  = [UF Origem](#uf_origem_31)  \(\*\*\)

UF do Quadro = [UF Destino](#uf_destino_31) \(\*\)

Para o GLGNi \(Percentual do GLGNi na composição do GLP/GLGN  \(campo 19\- PERC\_GLGN\_I da SAFX325\) diferente de zero\):

	Gravar um registro para cada UF Origem e UF Destino

Descrição do Produto = GNGNi

UF Destinatária do Anexo VI\-M  = [UF Origem](#uf_origem_31)  \(\*\*\)  

UF do Quadro = [UF Destino](#uf_destino_31) \(\*\)

Os mesmos registros que gravam o quadro 3\.1, gravam o quadro 3\.2 só invertendo UF Destinatário do Anexo VI\-M e UF do Quadro:

Para GLGNn \(Percentual do GLGNn na composição do GLP/GLGN \(campo 18\- PERC\_GLGN\_N da SAFX325\) diferente de zero\):

	Gravar um registro para cada UF Origem e UF Destino

Descrição do Produto = GNGNn

UF Destinatária do Anexo VI\-M  =[UF Destino](#uf_destino_31) \(\*\)

UF do Quadro =  [UF Origem](#uf_origem_31)  \(\*\*\)

Para o GLGNi \(Percentual do GLGNi na composição do GLP/GLGN  \(campo 19\- PERC\_GLGN\_I da SAFX325\) diferente de zero\):

	Gravar um registro para cada UF Origem e UF Destino

Descrição do Produto = GNGNi

UF Destinatária do Anexo VI\-M  = [UF Destino](#uf_destino_31) \(\*\)    

UF do Quadro = [UF Origem](#uf_origem_31)  \(\*\*\)

Exemplo: Nota fiscal com um item de mercadoria do produto GLP/GLGN:

SAFX07

Nota Fiscal

UF do Ponto de Consumo

22002

SP

SAFX08

Produto

Quantidade

CST

1\-001 

100,00

002

SAFX325

Produto

17 \- PERC\_GLP

18 \- PERC\_GLGN\_N

19 \- PERC\_GLGN\_I

22\- ALIQ\_AD\_REM\_ICMS

1\-001 

50

20

30

1\.3441

Produto

16 \- IND\_ORIG

17 \- COD\_UF\_ORIG

18 \- PERC\_UF\_ORIG

1\-001 

0 \- Nacional

RJ

35

0 – Nacional

BA

65

1\- Importado

ES

40

1\- Importado

MA

60

Gravar os seguintes registros no quadro 3\.1:

UF Destinatária do Anexo VI\-M

Quadro

UF do Quadro

Descrição do Produto

Quantidade \(Base de Cálculo\)

Vlr ICMS Cobrado

RJ

A6MQ31

SP

GLGNn

100 \* 20/100 \* 35/100

100 \* 20/100 \* 35/100 \* 1\.3441 \*0,6667

BA

A6MQ31

SP

GLGNn

100 \* 20/100 \* 65/100

100 \* 20/100 \* 65/100  \* 1\.3441 \*0,6667

ES

A6MQ31

SP

GLGNi

100 \* 30/100 \* 40/100

100 \* 30/100 \* 40/100  \* 1\.3441 \*0,2222

MA

A6MQ31

SP

GLGNi

100 \* 30/100 \* 60/100

100 \* 30/100 \* 60/100  \* 1\.3441 \*0,2222

Gravar os seguintes registros no quadro 3\.2:

UF Destinatária do Anexo VI\-M

Quadro

UF do Quadro

Descrição do Produto

Quantidade \(Base de Cálculo\)

Vlr ICMS Cobrado

SP

A6MQ32

RJ

GLGNn

100 \* 20/100 \* 35/100

100 \* 20/100 \* 35/100 \* 1\.3441 \*0,6667

SP

A6MQ32

BA

GLGNn

100 \* 20/100 \* 65/100

100 \* 20/100 \* 65/100  \* 1\.3441 \*0,6667

SP

A6MQ32

ES

GLGNi

100 \* 30/100 \* 40/100

100 \* 30/100 \* 40/100  \* 1\.3441 \*0,2222

SP

A6MQ32

MA

GLGNi

100 \* 30/100 \* 60/100

100 \* 30/100 \* 60/100  \* 1\.3441 \*0,2222

Gravar os campos do Quadro 3\.1 conforme regras abaixo\. O registro gerado está disponível para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 31 e 3\.2\.

Tabela: CBT\_ANEXO6M\_QUADR31\_32

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

[UF Origem](#uf_origem_31)  \(\*\*\)

Quadro

cod\_tag

A6MQ31

 

UF do Quadro

ident\_estado\_quad    

[UF Destino](#uf_destino_31) \(\*\)

Código do Produto

Cod\_produto

Preencher com 

01 para GLGNn

02 para GLGNi

Quantidade \(Base de Cálculo\)

Qtd\_comb

Para GLGNn: 

      __\[Quantidade \* PERC\_GLGN\_N/100 \* PERC\_UF\_ORIG/100\]__

Para GLGNi: 

      __\[Quantidade \* PERC\_GLGN\_I/100 \* PERC\_UF\_ORIG/100\]__

Onde:

- Quantidade: Quantidade do Item de Mercadoria \(item 24 da SAFX08\)\.  

Se medida do item for diferente da parametrizada para o produto \(Parâmetros > Produtos x Grupos de Combustíveis e Derivados SAFX96\) aplicar a conversão de unidades de medida\.

- PERC\_GLGN\_N:  campo 18 da SAFX325
- PERC\_GLGN\_I:   campo 19 da SAFX325
- PERC\_UF\_ORIG: campo 18 da SAFX326\. 

Somar ou subtrair o valor dependendo da parametrização do CFOP ou CFOP/NAT:

\+ se  parametrizado para saída \(88, 92\)

\- se  parametrizado para devolução \(90, 93\)

Vlr ICMS Cobrado

Vlr\_ICMS\_COB

Para GLGNn: 

      __\[Quantidade \* PERC\_GLGN\_N/100 \* PERC\_UF\_ORIG/100 \* ALIQ\_AD\_REM \* 0,6667\]__

Para GLGNi: 

      __\[Quantidade \* PERC\_GLGN\_I/100 \* PERC\_UF\_ORIG/100 \* ALIQ\_AD\_REM \* 0,2222\]__

Onde:

- Quantidade: Quantidade do Item de Mercadoria \(item 24 da SAFX08\)\.  

Se medida do item for diferente da parametrizada para o produto \(Parâmetros > Produtos x Grupos de Combustíveis e Derivados SAFX96\) aplicar a conversão de unidades de medida\.

- PERC\_GLGN\_N:  campo 18 da SAFX325
- PERC\_GLGN\_I:   campo 19 da SAFX325
- PERC\_UF\_ORIG: campo 18 da SAFX326\. 
- ALIQ\_AD\_REM: 

Se o Código da Situação Estadual “B” \(campo 31 da SAFX08\) estiver preenchido com ‘02’, ‘15’ ou ‘53’, então:

   Preencher com o campo 22\- ALIQ\_AD\_REM\_ICMS da SAFX325\. 

Se o Código da Situação Estadual “B” \(campo 31 da SAFX08\) estiver preenchido com ‘61’, então:

   Preencher com o campo 33\- ALIQ\_AD\_REM\_ICMS\_RET da SAFX325\.

- 0,6667 e 0,2222 são os percentuais definidos pelo Convênio 199/22, cláusula décima, inciso II alínea “c” com referência as alíneas “a” e "c" do inciso VI da cláusula segunda, onde estão definidos esses percentuais\.

Somar ou subtrair o valor dependendo da parametrização do CFOP ou CFOP/NAT:

\+ se  parametrizado para saída \(88, 92\)

\- se  parametrizado para devolução \(90, 93\)

Vlr ICMS Retido

Vlr\_ICMS\_RET

Preencher com zero

Vlr ICMS Total

Vlr\_ICMS\_TOT

Soma dos dois campos anteriores \(ICMS Cobrado \+ Retido\)

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

Gravar os campos do Quadro 3\.2 conforme regras abaixo\. O registro gerado está disponível para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 31 e 3\.2\.

Tabela: CBT\_ANEXO6M\_QUADR31\_32

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

[UF Destino](#uf_destino_31) \(\*\)

Quadro

cod\_tag

A6MQ32

 

UF do Quadro

ident\_estado\_quad    

[UF Origem](#uf_origem_31)  \(\*\*\) 

Código do Produto

Cod\_produto

Preencher com 

01 para GLGNn

02 para GLGNi

Quantidade \(Base de Cálculo\)

Qtd\_comb

Para GLGNn: 

      __\[Quantidade \* PERC\_GLGN\_N/100 \* PERC\_UF\_ORIG/100\]__

Para GLGNi: 

      __\[Quantidade \* PERC\_GLGN\_I/100 \* PERC\_UF\_ORIG/100\]__

Onde:

- Quantidade: Quantidade do Item de Mercadoria \(item 24 da SAFX08\)\.  

Se medida do item for diferente da parametrizada para o produto \(Parâmetros > Produtos x Grupos de Combustíveis e Derivados SAFX96\) aplicar a conversão de unidades de medida\.

- PERC\_GLGN\_N:  campo 18 da SAFX325
- PERC\_GLGN\_I:   campo 19 da SAFX325
- PERC\_UF\_ORIG: campo 18 da SAFX326\. 

Somar ou subtrair o valor dependendo da parametrização do CFOP ou CFOP/NAT:

\+ se  parametrizado para saída \(88, 92\)

\- se  parametrizado para devolução \(90, 93\)

Vlr ICMS Cobrado

Vlr\_ICMS\_COB

Para GLGNn: 

      __\[Quantidade \* PERC\_GLGN\_N/100 \* PERC\_UF\_ORIG/100 \* ALIQ\_AD\_REM \* 0,6667\]__

Para GLGNi: 

      __\[Quantidade \* PERC\_GLGN\_I/100 \* PERC\_UF\_ORIG/100 \* ALIQ\_AD\_REM \* 0,2222\]__

Onde:

- Quantidade: Quantidade do Item de Mercadoria \(item 24 da SAFX08\)\.  

Se medida do item for diferente da parametrizada para o produto \(Parâmetros > Produtos x Grupos de Combustíveis e Derivados SAFX96\) aplicar a conversão de unidades de medida\.

- PERC\_GLGN\_N:  campo 18 da SAFX325
- PERC\_GLGN\_I:   campo 19 da SAFX325
- PERC\_UF\_ORIG: campo 18 da SAFX326\. 
- ALIQ\_AD\_REM: 

Se o Código da Situação Estadual “B” \(campo 31 da SAFX08\) estiver preenchido com ‘02’, ‘15’ ou ‘53’, então:

   Preencher com o campo 22\- ALIQ\_AD\_REM\_ICMS da SAFX325\. 

Se o Código da Situação Estadual “B” \(campo 31 da SAFX08\) estiver preenchido com ‘61’, então:

   Preencher com o campo 33\- ALIQ\_AD\_REM\_ICMS\_RET da SAFX325\.

- 0,6667 e 0,2222 são os percentuais definidos pelo Convênio 199/22, cláusula décima, inciso II alínea “c” com referência as alíneas “a” e "c" do inciso VI da cláusula segunda, onde estão definidos esses percentuais\.

Somar ou subtrair o valor dependendo da parametrização do CFOP ou CFOP/NAT:

\+ se  parametrizado para saída \(88, 92\)

\- se  parametrizado para devolução \(90, 93\)

Vlr ICMS Retido

Vlr\_ICMS\_RET

Preencher com zero

Vlr ICMS Total

Vlr\_ICMS\_TOT

Soma dos dois campos anteriores \(ICMS Cobrado \+ Retido\)

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

## <a id="_Toc211245066"></a>RN04 \- Geração do Anexo VI\-M \- Quadro 4

__Quadro 4\.1\.1 \- REPASSE POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS DE COMBUSTÍVEIS/TRRs \(ICMS COBRADO PELO EMITENTE\)__

Quadro gerado a partir da leitura do Anexo III\-M \- quadro A3MQ4 \- valor __VLR42__, contido no arquivo txt informado na geração\.

Esse registro é gerado apenas quando o Emitente do Anexo III\-M __não__ for Importador \(campo CATEGORIA posição ini\-fim 23\-25 do registro A3MHD <> ‘IMP’\)\.

Para cada registro lido do quadro A3MQ4 com valor VLR42, será gravado um registro no quadro 4\.1\.1 e outro no quadro 7\.1\.1\.

Os registros gerados estão disponíveis para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 4 a 15\.

Além do valor __VLR42__ do quadro A3MQ4 do Anexo III\-M, o valor __VLR43__ também pode ser considerado para o quadro 4\.1\.1 quando os dois critérios abaixo forem verdadeiros:

- O parâmetro seguinte parâmetro “Definir Destinatário do Relatório como responsável pelo Repasse” da tela “Regras para Geração dos Anexos” estiver marcado\. 
- Raiz do CNPJ \(Considerar os 8 primeiros dígitos do código do CNPJ\) dos dados do Destinatário do Relatório apresentado no Quadro 1 \(A3MQ1\) corresponde a raiz do CNPJ dos dados do Sujeito Passivo por Substituição que tiver originalmente retido o imposto apresentado no Quadro 2 \(A3MQ2\)\.

A regra acima foi criada para o Anexo VI pela MFS\-99207 e adotamos a mesma para o Anexo VI\-M por similaridade dos anexos\.

Tabela: CBT\_ANEXO6M\_QUADR4A15

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF recuperada do registro A3MHD – campo UFDESTPR posição ini\-fim 20\-21

Quadro

cod\_tag

A6MQ41

 

cod\_quadro

1

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A3MHD – campo CNPJ posição ini\-fim 27\-40

UF do Quadro

ident\_estado\_quad    

UF emitente recuperada do registro A3MHD – campo UF posição ini\-fim 253\-254

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor recuperado do registro A3MQ4 \- campo VLR42 posição ini\-fim 25\-38 e SINALPN posição 39

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

Ver [RN16](#_RN16_-_Geração) para gravação da tabela CBT\_ANEXO6M\_RELAT para composição do Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras\.

__Quadro 4\.1\.2\.1 \- REPASSE POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORES DE GÁS EM FAVOR DA UF DE ORIGEM DO GLGN__

Quadro gerado a partir da leitura do Anexo XI\-M \- quadro A11MQ1 \- valor VLR31, contido no arquivo txt informado na geração\.

Para cada registro lido do quadro A11MQ1 com valor VLR31,  será gravado um registro no quadro 4\.1\.2\.1 e outro no quadro 7\.1\.2\.1\.

Os registros gerados estão disponíveis para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 4 a 15\.

Tabela: CBT\_ANEXO6M\_QUADR4A15

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF recuperada do registro A11MHD – campo 7\-UFORIGEM posição ini\-fim 23\-24  

\(UF DE ORIGEM DO PRODUTO\)

Quadro

cod\_tag

A6MQ41

 

cod\_quadro

21

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A11MHD – campo CNPJ posição ini\-fim 28\-41

UF do Quadro

ident\_estado\_quad    

UF emitente recuperada do registro A11MHD – campo UF posição ini\-fim 254\-255

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor recuperado do registro A11MQ1 \- campo VLR31 posição ini\-fim 271\-285 e SINALPN posição 286

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

Ver [RN16](#_RN16_-_Geração) para gravação da tabela CBT\_ANEXO6M\_RELAT para composição do Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras\.

__Quadro 4\.1\.2\.2 \- REPASSE POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORES DE GÁS EM FAVOR DA UF DE DESTINO DO GLP/GLGN__

Quadro gerado a partir da leitura do Anexo XI\-M \- quadro A11MQ1 \- valor VLR32, contido no arquivo txt informado na geração\.

Para cada registro lido do quadro A11MQ1 com valor VLR32, será gravado um registro no quadro 4\.1\.2\.2 e outro no quadro 7\.1\.2\.2

Os registros gerados estão disponíveis para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 4 a 15\.

Tabela: CBT\_ANEXO6M\_QUADR4A15

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF recuperada do registro A11MHD – campo 5\- UFDESTPR posição ini\-fim 21\-22  

\(UF DE DESTINO DO PRODUTO\)

Quadro

cod\_tag

A6MQ41

 

cod\_quadro

22

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A11MHD – campo CNPJ posição ini\-fim 28\-41

UF do Quadro

ident\_estado\_quad    

UF emitente recuperada do registro A11MHD – campo UF posição ini\-fim 254\-255

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor recuperado do registro A11MQ1 \- campo VLR32 posição ini\-fim 287\-301 e SINALPN posição 302

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

Ver [RN16](#_RN16_-_Geração) para gravação da tabela CBT\_ANEXO6M\_RELAT para composição do Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras\.

__Quadro 4\.2 \- REPASSE POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS DE COMBUSTÍVEIS/TRRs \(ICMS COBRADO POR OUTROS CONTRIBUINTES\)__

Quadro gerado a partir da leitura do Anexo III\-M \- quadro A3MQ4 \- valor __VLR43__, contido no arquivo txt informado na geração\.

Esse registro é gerado apenas quando o Emitente do Anexo III\-M __não__ for Importador  \(campo CATEGORIA posição ini\-fim 23\-25 do registro A3MHD <> ‘IMP’\)\.

Para cada registro lido do quadro A3MQ4 com valor VLR43, será gravado um registro no quadro 4\.2 e outro no quadro 7\.2\.

Os registros gerados estão disponíveis para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 4 a 15\.

Tabela: CBT\_ANEXO6M\_QUADR4A15

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF recuperada do registro A3MHD – campo UFDESTPR posição ini\-fim 20\-21

Quadro

cod\_tag

A6MQ42

 

cod\_quadro

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A3MHD – campo CNPJ posição ini\-fim 27\-40

UF do Quadro

ident\_estado\_quad    

UF emitente recuperada do registro A3MHD – campo UF posição ini\-fim 253\-254

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor recuperado do registro A3MQ4 \- campo VLR43 posição ini\-fim 40\-53 e SINALPN posição 54

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

Ver [RN16](#_RN16_-_Geração) para gravação da tabela CBT\_ANEXO6M\_RELAT para composição do Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras\.

__Quadro 4\.3 – REPASSES EXTEPORÂNEOS: __

Esse quadro não é gerado\.

## <a id="_Toc211245067"></a>RN05 \- Geração do Anexo VI\-M \- Quadro 5

Quadro gerado a partir da leitura do Anexo III\-M \- quadro A3MQ4 \- valor __VLR43__, contido no arquivo txt informado na geração\.

Esse registro é gerado apenas quando o Emitente do Anexo III\-M for __Importador__  \(campo CATEGORIA posição ini\-fim 23\-25 do registro A3MHD = ‘IMP’\)\.

Para cada registro lido do quadro A3MQ4 com valor VLR43,  será gravado um registro no quadro 5 e outro no quadro 8\.

Os registros gerados estão disponíveis para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 4 a 15\.

Tabela: CBT\_ANEXO6M\_QUADR4A15

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF recuperada do registro A3MHD – campo UFDESTPR posição ini\-fim 20\-21

Quadro

cod\_tag

A6MQ5

 

cod\_quadro

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A3MHD – campo CNPJ posição ini\-fim 27\-40

UF do Quadro

ident\_estado\_quad    

UF emitente recuperada do registro A3MHD – campo UF posição ini\-fim 253\-254

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor recuperado do registro A3MQ4 \- campo VLR43 posição ini\-fim 40\-53 e SINALPN posição 54

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

Ver [RN16](#_RN16_-_Geração) para gravação da tabela CBT\_ANEXO6M\_RELAT para composição do Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras\.

## <a id="_Toc211245068"></a>RN06 \- Geração do Anexo VI\-M \- Quadro 6

__Quadro 6\.1 \- REPASSE DE ICMS SOBRE BIOCOMBUSTÍVEIS DECORRENTE DE AJUSTES DE REPARTIÇÃO DE RECEITA__

Quadro gerado a partir da leitura dos Anexos V\-M, V\-M\-AJ e XI\-M\-AJ \[MFS783073\], contido no arquivo txt informado na geração\. 

Anexo V\-M\-AJ \- quadro A5MAQ1 \- valor __VLRQ3__\.

Anexo V\-M \- quadro A5MQ4 \- valores __VLRQ42  e VLRQ43__\.

Anexo XI\-M\-AJ \- quadro A11MAJQ2 \- valor __VLRQ2__\. \[MFS783073\]

Para cada registro lido dos quadros A5MAQ1 com valor __VLRQ3__, A5MQ4 com valor VLRQ42, A5MQ4 com valor VLRQ43 e A11MAJQ2 \- valor __VLRQ2 __será gravado um registro no quadro 6\.1 e outro no quadro 9\.1\.

Os registros gerados estão disponíveis para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 4 a 15\.

Tabela: CBT\_ANEXO6M\_QUADR4A15

Anexo V\-M\-AJ

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF recuperada do registro A5MAHD – campo 5\- UFDESTPR posição ini\-fim 21\-22

Quadro

cod\_tag

A6MQ61

 

cod\_quadro

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A5MAHD – campo CNPJ posição ini\-fim 31\-44

UF do Quadro

ident\_estado\_quad    

UF recuperada do registro A5MAHD – campo 7\-UFORIGEM posição ini\-fim 23\-24  

\(UF DE ORIGEM DO PRODUTO\)

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor recuperado do registro A5MAQ1 \- campo VLRQ3 posição ini\-fim 254\-267 e SINALPN posição 268

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

Ver [RN16](#_RN16_-_Geração) para gravação da tabela CBT\_ANEXO6M\_RELAT para composição do Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras\.

\[MFS783073\] Geração dos Quadros 6\.1 e 9\.1 a partir da leitura do Anexo XI\-M\-AJ do arquivo das distribuidoras\.

Anexo XI\-M\-AJ

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF recuperada do registro A11MAJHD – campo 5\- UFDESTPR posição ini\-fim 23\-24

Quadro

cod\_tag

A6MQ61

 

cod\_quadro

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A11MAJHD – campo 8\- CNPJ posição ini\-fim  30\-43

UF do Quadro

ident\_estado\_quad    

UF recuperada do registro A11MAJHD – campo 6\-UFORIGEM posição ini\-fim 25\-26

\(UF DE ORIGEM DO PRODUTO\)

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor recuperado do registro A11MAJQ2 \- campo VLRQ2 posição ini\-fim  241\-255 e SINALPN posição  256

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

Ver [RN16](#_RN16_-_Geração) para gravação da tabela CBT\_ANEXO6M\_RELAT para composição do Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras\.

__MFS547704__: Leitura do Anexo V\-M \(Etanol Anidro\) e gravação do quadro 6\.1:

Conforme orientações passadas por email pelo Lino da Sefaz\-MG os valores 4\.2 e 4\.3 do quadro 4 do anexo V\-M devem ser gravados sumarizados no quadro 6\.1, o campo COD\_QUADRO sem preenchimento e gravando o COD\_TAG com A6MQ61\.

Se acontecer de termos para o mesmo CNPJ e UF Repasse/Dedução os valores VLRQ3 do V\-M\-AJ e VLRQ42 e VLRQ43 do V\-M, a orientação foi de gravar dois registros no quadro 6\.1, um para o VLRQ3 do V\-M\-AJ e outro com a soma de VLRQ42 e VLRQ43 do V\-M\. Mas a nossa geração irá somar os valores e gerar um único registro por CNPJ e UF Repasse/Dedução\. Essa forma também foi aceita pelo Sr Lino \(SEFAZ\-MG\) com resposta por email em 06/07/2023\.

![](data:image/x-emf;base64,AQAAAGwAAAAAAAAAAQAAAH0AAABLAAAAAAAAAAAAAAC4BwAA1gYAACBFTUYAAAEAyCMAABYAAAACAAAAAAAAAAAAAAAAAAAAgAcAADgEAAAsAQAA5gAAAAAAAAAAAAAAAAAAAOCTBABwggMAGAAAAAwAAAAAAAAAGQAAAAwAAAD///8ATQAAAOwBAAArAAAAAQAAAFIAAAAoAAAAKwAAAAEAAAAoAAAAKAAAAMYAiAAAAAAAAAAAAAAAgD8AAAAAAAAAAAAAgD8AAAAAAAAAAP///wAAAAAAbAAAADAAAACcAAAAUAEAACgAAAAoAAAAKAAAACgAAAAqAAAAAQABAAAAAABQAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8AAAAAAAAAAAAAAAAAAAAAAP//////AAAA/gAAAAcAAAD+AAAABwAAAPwAAAAHAAAA/AAAAAcAAAD8AAAABwAAAPwAAAAHAAAA/AAAAAcAAAD8AAAABwAAAPwAAAAHAAAA/AAAAAcAAAD8AAAABwAAAPwAAAAHAAAA/AAAAAcAAAD8AAAABwAAAPwAAAAHAAAA/AAAAAcAAAD8AAAABwAAAPwAAAAHAAAA/AAAAAcAAAD8AAAABwAAAPwAAAAHAAAA/AAAAAcAAAD8AAAABwAAAPwAAAAHAAAA/AAAAAcAAAD8AAAABwAAAPwAAAAHAAAA/AAAAAcAAAD8AAAABwAAAPwAAAAPAAAA/AAAAB8AAAD8AAAAHwAAAPwAAAA/AAAA/AAAAP8AAAD8AAAB/wAAAPwAAAP/AAAA/AAAA/8AAAD8AAAH/wAAAPwAAB//AAAATQAAAKAZAAArAAAAAQAAAFIAAAAoAAAAKwAAAAEAAAAoAAAAKAAAAEYAZgAAAAAAAAAAAAAAgD8AAAAAAAAAAAAAgD8AAAAAAAAAAP///wAAAAAAbAAAADQAAACgAAAAABkAACgAAAAoAAAAKAAAACgAAAAoAAAAAQAgAAMAAAAAGQAAAAAAAAAAAAAAAAAAAAAAAAAA/wAA/wAA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAAD///8A////AP///wD///8A////AICAgACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAA////AP///wD///8A////AP///wCAgIAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAP///wD///8A////AP///wCAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAAD///8A////AP///wCAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAA////AP///wCAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAICAgACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAADAAAAAAAAAISAAAADAAAAAEAAABSAAAAcAEAAAEAAAAUAAAAAAAAAAAAAAAAAAAAvAIAAAAAAAABAgIiUwB5AHMAdABlAG0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI4uDp/n8AAAEAAACUAAAAAAAAAAAAAAA39sTp/n8AAAAAAAAAAAAA8Ku1DpQAAAA+IAFQAAAAAAFQAAAAAAAAAgAAAAAAAACljF3q/n8AAElPBS4ADQAAkKu1DpQAAAAYQMAc/n8AAAAAAAAAAAAAsSwAAAAAAAD31MUaAAAAAPg/wBz+fwAAAAAAAAAAAAABAAAAAAAAAJiWhyF7AgAAsKy1DpQAAADFMsJx/n8AAAAAAAAAAAAAPiABUAAAAAAAAAAAAAAAABGMXer+fwAAWOg+C3sCAADLMB7q/n8AAGCutQ6UAAAASa21DpQAAAAAr7UOlAAAAAEAAABkdgAIAAAAACUAAAAMAAAAAQAAACUAAAAMAAAADQAAgCgAAAAMAAAAAQAAAFIAAABwAQAAAQAAAPP///8AAAAAAAAAAAAAAACQAQAAAAAAAABAACJTAGUAZwBvAGUAIABVAEkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB/AAAAAAAAN/bE6f5/AADA/I4LewIAADUaOy7+fwAAAAAAAAAAAABwgZQLewIAAAAAAAAAAAAA+LG1DpQAAAAAABByewIAAOCxtQ6UAAAAYLK1DpQAAABosrUOlAAAAAH8jgt7AgAAoVud7P5/AAA6AQAAAAAAAKFbnewAAAAAgCkVGv5/AAAAAAAAAAAAAICSlAt7AgAAsUed7P5/AACAKRUa/n8AAAAAF3J7AgAAwPyOC3sCAACkAAAAAAAAAAAAAAAAAAAAcIGUC3sCAABY6D4LewIAAMswHur+fwAA8LS1DpQAAACps7UOlAAAAACZIXJ7AgAAAAAAAGR2AAgAAAAAJQAAAAwAAAABAAAAVAAAAHwAAAAnAAAAKgAAAFoAAAA6AAAAAQAAAAAAekHRXqpBJwAAACoAAAAIAAAATAAAAAQAAAAAAAAAAAAAAH4AAABSAAAAXAAAAEUAWABUACAAUgBFAFMAIAAHAAAACAAAAAcAAAAEAAAACAAAAAcAAAAHAAAABAAAAFQAAACAAgAAAAAAADsAAAB9AAAASwAAAAEAAAAAAHpB0V6qQQAAAAA7AAAAXgAAAEwAAAAEAAAAAAAAAAAAAAB+AAAAUgAAAAgBAABSAEUAVABJAEYASQBDAEEAxwDDAE8AIABDAG8AbQBwAGwAZQBtAGUAbgB0AG8AIABhAG8AIABNAGEAbgB1AGEAbAAgAE4ATwBUAEEAIABUAMkAQwBOAEkAQwBBACAAUwBDAEEATgBDACAAUgBFAEYAIAAtACAAIABNAGEAbgB1AGEAbAAgAE4ATwBUAEEAIABUAMkAQwBOAEkAQwBBACAAUwBDAEEATgBDACAAUgBFAEYAIAAuAG0AcwBnAAgAAAAHAAAABwAAAAMAAAAGAAAAAwAAAAgAAAAIAAAACAAAAAgAAAAKAAAABAAAAAgAAAAIAAAACwAAAAgAAAADAAAABwAAAAsAAAAHAAAABwAAAAQAAAAIAAAABAAAAAcAAAAIAAAABAAAAAwAAAAHAAAABwAAAAcAAAAHAAAAAwAAAAQAAAAKAAAACgAAAAcAAAAIAAAABAAAAAcAAAAHAAAACAAAAAoAAAADAAAACAAAAAgAAAAEAAAABwAAAAgAAAAIAAAACgAAAAgAAAAEAAAACAAAAAcAAAAGAAAABAAAAAUAAAAEAAAABAAAAAwAAAAHAAAABwAAAAcAAAAHAAAAAwAAAAQAAAAKAAAACgAAAAcAAAAIAAAABAAAAAcAAAAHAAAACAAAAAoAAAADAAAACAAAAAgAAAAEAAAABwAAAAgAAAAIAAAACgAAAAgAAAAEAAAACAAAAAcAAAAGAAAABAAAAAMAAAALAAAABgAAAAgAAAAlAAAADAAAAA0AAIBGAAAAIAAAABIAAABJAGMAbwBuAE8AbgBsAHkAAAAAAEYAAADcAAAAzgAAAEUAWABUACAAUgBFAFMAIABSAEUAVABJAEYASQBDAEEAxwDDAE8AIABDAG8AbQBwAGwAZQBtAGUAbgB0AG8AIABhAG8AIABNAGEAbgB1AGEAbAAgAE4ATwBUAEEAIABUAMkAQwBOAEkAQwBBACAAUwBDAEEATgBDACAAUgBFAEYAIAAtACAAIABNAGEAbgB1AGEAbAAgAE4ATwBUAEEAIABUAMkAQwBOAEkAQwBBACAAUwBDAEEATgBDACAAUgBFAEYAIAAuAG0AcwBnAAAAAABGAAAASAAAADwAAABDADoAXABXAEkATgBEAE8AVwBTAFwAUwB5AHMAdABlAG0AMwAyAFwAbwBsAGUAMwAyAC4AZABsAGwAAABGAAAAEAAAAAQAAAAAAAAARgAAACAAAAASAAAASQBjAG8AbgBPAG4AbAB5AAAAAAAOAAAAFAAAAAAAAAAQAAAAFAAAAA==)

Anexo V\-M

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF do Remetente

Registro A5MHD – campo 7 – UFORIGEM posição ini\-fim 22\-23

Quadro

cod\_tag

A6MQ61

 

cod\_quadro

Não preencher

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A5MHD – campo 10 \- CNPJ posição ini\-fim 30\-43

UF do Quadro

ident\_estado\_quad    

UF de Destino do biocombustível, informada no cabeçalho do Anexo V\-M\.

Registro A5MHD – campo 5 – UFDESTPR posição ini\-fim 20\-21

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor 4\.2 do Quadro 4 dos Anexos V\-M \+ Valor 4\.3 do Quadro 4 dos Anexos V\-M

Registro A5MQ4 – campo 5 – VLR42 posição ini\-fim 26\-40 e SINALPN posição 41\-41

Registro A5MQ4 – campo 7 – VLR43 posição ini\-fim 42\-56 e SINALPN posição 57\-57

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

Ver [RN16](#_RN16_-_Geração) para gravação da tabela CBT\_ANEXO6M\_RELAT para composição do Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras\.

__MFS547704__: Leitura do Anexo V\-M \(Etanol Anidro\) e gravação do quadro 6\.1\.1:

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF do Remetente

Registro A5MHD – campo 7 – UFORIGEM posição ini\-fim 21\-22

Quadro

cod\_tag

A6MQ61

 

cod\_quadro

1 ???

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A5MHD – campo 10 \- CNPJ posição ini\-fim 29\-42

UF do Quadro

ident\_estado\_quad    

UF de Destino do biocombustível, informada no cabeçalho do Anexo V\-M\.

Registro A5MHD – campo 5 – UFDESTPR posição ini\-fim 19\-20

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor 4\.2 do Quadro 4 dos Anexos V\-M

Registro A5MQ4 – campo 5 – VLR42 posição ini\-fim 26\-40 e SINALPN posição 41\-41

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

__MFS547704__: Leitura do Anexo V\-M \(Etanol Anidro\) e gravação do quadro 6\.1\.2:

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF do Remetente

Registro A5MHD – campo 7 – UFORIGEM posição ini\-fim 21\-22

Quadro

cod\_tag

A6MQ61

 

cod\_quadro

2 ???

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A5MHD – campo 10 \- CNPJ posição ini\-fim 29\-42

UF do Quadro

ident\_estado\_quad    

UF de Destino do  biocombustível, informada no cabeçalho do Anexo V\-M\.

Registro A5MHD – campo 5 – UFDESTPR posição ini\-fim 19\-20

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor 4\.3 do Quadro 4 dos Anexos V\-M

Registro A5MQ4 – campo 7 – VLR43 posição ini\-fim 42\-56 e SINALPN posição 57\-57

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

__Quadro 6\.2 – REPASSE EXTEMPOÂNEO__

Esse quadro não é gerado\.

Dúvida: hoje a rotina faz a geração desse quadro a partir do A5\.  Como Anexo 5\-M continuaremos a gera\-lo?

## <a id="_Toc211245069"></a>RN07 \- Geração do Anexo VI\-M \- Quadro 7

__Quadro 7\.1\.1 \- DEDUÇÃO POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS DE COMBUSTÍVEIS/TRRs__

Quadro gerado a partir da leitura do Anexo III\-M \- quadro A3MQ4 \- valor __VLR42__, contido no arquivo txt informado na geração\.

Esse registro é gerado apenas quando o Emitente do Anexo III\-M __não__ for Importador  \(campo CATEGORIA posição ini\-fim 23\-25 do registro A3MHD <> ‘IMP’\)\.

Para cada registro lido do quadro A3MQ4 com valor VLR42,  será gravado um registro no quadro 7\.1\.1 e outro no quadro 4\.1\.1\.

Os registros gerados estão disponíveis para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 4 a 15\.

Tabela: CBT\_ANEXO6M\_QUADR4A15

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF emitente recuperada do registro A3MHD – campo UF posição ini\-fim 253\-254

Quadro

cod\_tag

A6MQ71

 

cod\_quadro

1

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A3MHD – campo CNPJ posição ini\-fim 27\-40

UF do Quadro

ident\_estado\_quad    

UF recuperada do registro A3MHD – campo UFDESTPR posição ini\-fim 20\-21

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor recuperado do registro A3MQ4 \- campo VLR42 posição ini\-fim 25\-38 e SINALPN posição 39

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

Ver [RN16](#_RN16_-_Geração) para gravação da tabela CBT\_ANEXO6M\_RELAT para composição do Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras\.

__Quadro 7\.1\.2\.1 \- DEDUÇÕES POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORES DE GÁS EM FAVOR DA UF DE ORIGEM DO GLGN__

Quadro gerado a partir da leitura do Anexo XI\-M \- quadro A11MQ1 \- valor VLR31, contido no arquivo txt informado na geração\.

Para cada registro lido do quadro A11MQ1 com valor VLR31, será gravado um registro no quadro 7\.1\.2\.1 e outro no quadro 4\.1\.2\.1\.

Os registros gerados estão disponíveis para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 4 a 15\.

Tabela: CBT\_ANEXO6M\_QUADR4A15

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF emitente recuperada do registro A11MHD – campo UF posição ini\-fim 254\-255

Quadro

cod\_tag

A6MQ71

 

cod\_quadro

21

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A11MHD – campo CNPJ posição ini\-fim 28\-41

UF do Quadro

ident\_estado\_quad    

UF recuperada do registro A11MHD – campo 7\-UFORIGEM posição ini\-fim 23\-24  

\(UF DE ORIGEM DO PRODUTO\)

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor recuperado do registro A11MQ1 \- campo VLR31 posição ini\-fim 271\-285 e SINALPN posição 286

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

Ver [RN16](#_RN16_-_Geração) para gravação da tabela CBT\_ANEXO6M\_RELAT para composição do Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras\.

__Quadro 7\.1\.2\.2 \- DEDUÇÃO POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORES DE GÁS EM FAVOR DA UF DE DESTINO DO GLP/GLGN__

Quadro gerado a partir da leitura do Anexo XI\-M \- quadro A11MQ1 \- valor VLR32, contido no arquivo txt informado na geração\.

Para cada registro lido do quadro A11MQ1 com valor VLR32, será gravado um registro no quadro 7\.1\.2\.2 e outro no quadro 4\.1\.2\.2\.

Os registros gerados estão disponíveis para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 4 a 15\.

Tabela: CBT\_ANEXO6M\_QUADR4A15

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF emitente recuperada do registro A11MHD – campo UF posição ini\-fim 254\-255

Quadro

cod\_tag

A6MQ71

 

cod\_quadro

22

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A11MHD – campo CNPJ posição ini\-fim 28\-41

UF do Quadro

ident\_estado\_quad    

UF recuperada do registro A11MHD – campo 5\- UFDESTPR posição ini\-fim 21\-22  

\(UF DE DESTINO DO PRODUTO\)

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor recuperado do registro A11MQ1 \- campo VLR32 posição ini\-fim 287\-301 e SINALPN posição 302

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

Ver [RN16](#_RN16_-_Geração) para gravação da tabela CBT\_ANEXO6M\_RELAT para composição do Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras\.

__Quadro 7\.2 \- DEDUÇÃO POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS DE COMBUSTÍVEIS/TRRs \(ICMS COBRADO POR OUTROS CONTRIBUINTES\)__

Quadro gerado a partir da leitura do Anexo III\-M \- quadro A3MQ4 \- valor __VLR43__, contido no arquivo txt informado na geração\.

Esse registro é gerado apenas quando o Emitente do Anexo III\-M __não__ for Importador  \(campo CATEGORIA posição ini\-fim 23\-25 do registro A3MHD <> ‘IMP’\)\.

Para cada registro lido do quadro A3MQ4 com valor VLR43,  será gravado um registro no quadro 7\.2 e outro no quadro 4\.2\.

Os registros gerados estão disponíveis para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 4 a 15\.

Tabela: CBT\_ANEXO6M\_QUADR4A15

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF emitente recuperada do registro A3MHD – campo UF posição ini\-fim 253\-254

Quadro

cod\_tag

A6MQ72

 

cod\_quadro

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A3MHD – campo CNPJ posição ini\-fim 27\-40

UF do Quadro

ident\_estado\_quad    

UF recuperada do registro A3MHD – campo UFDESTPR posição ini\-fim 20\-21

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor recuperado do registro A3MQ4 \- campo VLR43 posição ini\-fim 40\-53 e SINALPN posição 54

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

Ver [RN16](#_RN16_-_Geração) para gravação da tabela CBT\_ANEXO6M\_RELAT para composição do Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras\.

__Quadro 7\.3 – DEDUÇÕES EXTEPORÂNEOS: __

Esse quadro não é gerado\.

## <a id="_Toc211245070"></a>RN08 \- Geração do Anexo VI\-M \- Quadro 8

Quadro gerado a partir da leitura do Anexo III\-M \- quadro A3MQ4 \- valor __VLR43__, contido no arquivo txt informado na geração\.

Esse registro é gerado apenas quando o Emitente do Anexo III\-M for __Importador__  \(campo CATEGORIA posição ini\-fim 23\-25 do registro A3MHD = ‘IMP’\)\.

Para cada registro lido do quadro A3MQ4 com valor VLR43,  será gravado um registro no quadro 5 e outro no quadro 8\.

Os registros gerados estão disponíveis para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 4 a 15\.

Tabela: CBT\_ANEXO6M\_QUADR4A15

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF emitente recuperada do registro A3MHD – campo UF posição ini\-fim 253\-254

Quadro

cod\_tag

A6MQ8

 

cod\_quadro

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A3MHD – campo CNPJ posição ini\-fim 27\-40

UF do Quadro

ident\_estado\_quad    

UF recuperada do registro A3MHD – campo UFDESTPR posição ini\-fim 20\-21

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor recuperado do registro A3MQ4 \- campo VLR43 posição ini\-fim 40\-53 e SINALPN posição 54

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

Ver [RN16](#_RN16_-_Geração) para gravação da tabela CBT\_ANEXO6M\_RELAT para composição do Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras\.

## <a id="_Toc211245071"></a>RN09 \- Geração do Anexo VI\-M \- Quadro 9

__Quadro 9\.1 \- DEDUÇÃO DE ICMS SOBRE BIOCOMBUSTÍVEIS DECORRENTE DE AJUSTES DE REPARTIÇÃO DE RECEITA__

Quadro gerado a partir da leitura dos Anexos V\-M, V\-M\-AJ e XI\-M\-AJ \[MFS783073\], contido no arquivo txt informado na geração\. 

Anexo V\-M\-AJ \- quadro A5MAQ1 \- valor __VLRQ3__\.

Anexo V\-M \- quadro A5MQ4 \- valores __VLRQ42 e VLRQ43__\.

Anexo XI\-M\-AJ \- quadro A11MAJQ2 \- valor __VLRQ2__\. \[MFS783073\]

Para cada registro lido dos quadros A5MAQ1 com valor __VLRQ3__, A5MQ4 com valor VLRQ42, A5MQ4 com valor VLRQ43 e A11MAJQ2 \- valor __VLRQ2 __será gravado um registro no quadro 6\.1 e outro no quadro 9\.1\.

Os registros gerados estão disponíveis para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 4 a 15\.

Tabela: CBT\_ANEXO6M\_QUADR4A15

Anexo V\-M\-AJ

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF recuperada do registro A5MAHD – campo 7\-UFORIGEM posição ini\-fim 23\-24  

\(UF DE ORIGEM DO PRODUTO\)

Quadro

cod\_tag

A6MQ91

 

cod\_quadro

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A5MAHD – campo CNPJ posição ini\-fim 31\-44

UF do Quadro

ident\_estado\_quad    

UF recuperada do registro A5MAHD – campo 5\- UFDESTPR posição ini\-fim 21\-22

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor recuperado do registro A5MAQ1 \- campo VLRQ3 posição ini\-fim 254\-267 e SINALPN posição 268

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

Ver [RN16](#_RN16_-_Geração) para gravação da tabela CBT\_ANEXO6M\_RELAT para composição do Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras\.

\[MFS783073\] Geração dos Quadros 6\.1 e 9\.1 a partir da leitura do Anexo XI\-M\-AJ do arquivo das distribuidoras\.

Anexo XI\-M\-AJ

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF recuperada do registro A11MAJHD – campo 6\-UFORIGEM posição ini\-fim   25\-26

\(UF DE ORIGEM DO PRODUTO\)

Quadro

cod\_tag

A6MQ91

 

cod\_quadro

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A11MAJHD – campo 8 \- CNPJ posição ini\-fim  30\-43

UF do Quadro

ident\_estado\_quad    

UF recuperada do registro A11MAJHD – campo 5\- UFDESTPR posição ini\-fim  23\-24

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor recuperado do registro A11MAJQ2 \- campo VLRQ2 posição ini\-fim 241\-255 e SINALPN posição  256

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

Ver [RN16](#_RN16_-_Geração) para gravação da tabela CBT\_ANEXO6M\_RELAT para composição do Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras\.

__MFS547704: __Leitura do Anexo V\-M \(Etanol Anidro\) e gravação do quadro 9\.1:

Conforme orientações passadas por email pelo Lino da Sefaz\-MG os valores 4\.2 e 4\.3 do quadro 4 do anexo V\-M devem ser gravados sumarizados no quadro 9\.1, o campo COD\_QUADRO sem preenchimento e gravando o COD\_TAG com A6MQ91\.

Se acontecer de termos para o mesmo CNPJ e UF Repasse/Dedução os valores VLRQ3 do V\-M\-AJ  e VLRQ42  e VLRQ43 do V\-M, a orientação foi de gravar dois registros no quadro 9\.1, um para o VLRQ3 do V\-M\-AJ e outro com a soma de VLRQ42  e VLRQ43 do V\-M\. Mas a nossa geração irá somar os valores e gerar um único registro por CNPJ e UF Repasse/Dedução\. Essa forma também foi aceita pelo Sr Lino \(SEFAZ\-MG\) com resposta por email em 06/07/2023\.

![](data:image/x-emf;base64,AQAAAGwAAAAAAAAAAQAAAH0AAABLAAAAAAAAAAAAAAC4BwAA1gYAACBFTUYAAAEAyCMAABYAAAACAAAAAAAAAAAAAAAAAAAAgAcAADgEAAAsAQAA5gAAAAAAAAAAAAAAAAAAAOCTBABwggMAGAAAAAwAAAAAAAAAGQAAAAwAAAD///8ATQAAAOwBAAArAAAAAQAAAFIAAAAoAAAAKwAAAAEAAAAoAAAAKAAAAMYAiAAAAAAAAAAAAAAAgD8AAAAAAAAAAAAAgD8AAAAAAAAAAP///wAAAAAAbAAAADAAAACcAAAAUAEAACgAAAAoAAAAKAAAACgAAAAqAAAAAQABAAAAAABQAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8AAAAAAAAAAAAAAAAAAAAAAP//////AAAA/gAAAAcAAAD+AAAABwAAAPwAAAAHAAAA/AAAAAcAAAD8AAAABwAAAPwAAAAHAAAA/AAAAAcAAAD8AAAABwAAAPwAAAAHAAAA/AAAAAcAAAD8AAAABwAAAPwAAAAHAAAA/AAAAAcAAAD8AAAABwAAAPwAAAAHAAAA/AAAAAcAAAD8AAAABwAAAPwAAAAHAAAA/AAAAAcAAAD8AAAABwAAAPwAAAAHAAAA/AAAAAcAAAD8AAAABwAAAPwAAAAHAAAA/AAAAAcAAAD8AAAABwAAAPwAAAAHAAAA/AAAAAcAAAD8AAAABwAAAPwAAAAPAAAA/AAAAB8AAAD8AAAAHwAAAPwAAAA/AAAA/AAAAP8AAAD8AAAB/wAAAPwAAAP/AAAA/AAAA/8AAAD8AAAH/wAAAPwAAB//AAAATQAAAKAZAAArAAAAAQAAAFIAAAAoAAAAKwAAAAEAAAAoAAAAKAAAAEYAZgAAAAAAAAAAAAAAgD8AAAAAAAAAAAAAgD8AAAAAAAAAAP///wAAAAAAbAAAADQAAACgAAAAABkAACgAAAAoAAAAKAAAACgAAAAoAAAAAQAgAAMAAAAAGQAAAAAAAAAAAAAAAAAAAAAAAAAA/wAA/wAA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAICAgACAgIAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAAD///8A////AP///wD///8A////AICAgACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAA////AP///wD///8A////AP///wCAgIAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAP///wD///8A////AP///wCAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAAD///8A////AP///wCAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAA////AP///wCAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAICAgACAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAACAgIAAgICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAADAAAAAAAAAISAAAA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)

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF de Destino do biocombustível, informada no cabeçalho do Anexo V\-M\.

Registro A5MHD – campo 5 – UFDESTPR posição ini\-fim 20\-21

Quadro

cod\_tag

A6MQ91

 

cod\_quadro

Não preencher

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A5MHD – campo 10 \- CNPJ posição ini\-fim 30\-43

UF do Quadro

ident\_estado\_quad    

UF do Remetente

Registro A5MHD – campo 7 – UFORIGEM posição ini\-fim 22\-23

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor 4\.2 do Quadro 4 dos Anexos V\-M\+ Valor 4\.3 do Quadro 4 dos Anexos V\-M

Registro A5MQ4 – campo 5 – VLR42 posição ini\-fim 26\-40 e SINALPN posição 41\-41

Registro A5MQ4 – campo 7 – VLR43 posição ini\-fim 42\-56 e SINALPN posição 57\-57

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

Ver [RN16](#_RN16_-_Geração) para gravação da tabela CBT\_ANEXO6M\_RELAT para composição do Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras\.

__MFS547704: __Leitura do Anexo V\-M \(Etanol Anidro\) e gravação do quadro 9\.1\.1:

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF de Destino do biocombustível, informada no cabeçalho do Anexo V\-M\.

Registro A5MHD – campo 5 – UFDESTPR posição ini\-fim 19\-20

Quadro

cod\_tag

A6MQ91

 

cod\_quadro

1  ????

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A5MHD – campo 10 \- CNPJ posição ini\-fim 29\-42

UF do Quadro

ident\_estado\_quad    

UF do Remetente

Registro A5MHD – campo 7 – UFORIGEM posição ini\-fim 21\-22

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor 4\.2 do Quadro 4 dos Anexos V\-M

Registro A5MQ4 – campo 5 – VLR42 posição ini\-fim 26\-40 e SINALPN posição 41\-41

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

__MFS547704: __Leitura do Anexo V\-M \(Etanol Anidro\) e gravação do quadro 9\.1\.2:

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF de Destino do biocombustível, informada no cabeçalho do Anexo V\-M\.

Registro A5MHD – campo 5 – UFDESTPR posição ini\-fim 19\-20

Quadro

cod\_tag

A6MQ91

 

cod\_quadro

2  ????

Pessoa Fis/Jur

ident\_fis\_jur        

Pessoa Fis/Jur emitente recuperada do registro A5MHD – campo 10 \- CNPJ posição ini\-fim 29\-42

UF do Quadro

ident\_estado\_quad    

UF do Remetente

Registro A5MHD – campo 7 – UFORIGEM posição ini\-fim 21\-22

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Valor 4\.3 do Quadro 4 dos Anexos V\-M

Registro A5MQ4 – campo 7 – VLR43 posição ini\-fim 42\-56 e SINALPN posição 57\-57

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

__Quadro 9\.2 – REPASSE EXTEMPOÂNEO__

Esse quadro não é gerado\.

Dúvida: hoje a rotina faz a geração desse quadro a partir do A5\.  Como Anexo 5\-M continuaremos a gera\-lo?

## <a id="_Toc211245072"></a>RN10 \- Geração do Anexo VI\-M \- Quadro 10

Quadro gerado a partir das Notas Fiscais de ressarcimento dos Produtos sujeitos a tributação monofásica\.

__Critérios de Seleção:__

Para geração desse quadro recuperar os documentos fiscais a partir das tabelas SAFX07, SAFX08, considerando os seguintes critérios:

\- Código da empresa = código da empresa da geração; 

\- Código do estabelecimento: depende do parâmetro “Inscrição Estadual Única” informado na tela de geração\.

   Se parâmetro desmarcado, então considerar apenas notas do estabelecimento selecionado na geração;

   Se parâmetro marcado, considerar as notas do estabelecimento centralizador selecionado na geração e dos estabelecimentos centralizados\. 

\- Data Fiscal compreendida no mês/ano Referência informado na geração;

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Somente notas com item de mercadoria \(SAFX08\);

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu: Parâmetros > Anexos I, II, III, IV, V, VI e VIII para os tipos:

  108 – Ressarcimentos Autorizados de ICMS\-ST

\- Produto do item da nota deve ser parametrizado no item de menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados, com o seu respectivo grupo de combustíveis \(SAFX96\)

\- O Grupo de Combustível parametrizado para o produto, deve estar com o flag Anexo VI\-M selecionado, no menu Parâmetros 🡪 Grupos de Combustíveis e Derivados\.

\- Ramo de Atividade da Pessoa Fis/Jur da nota fiscal deve ser 104 – Distribuidora \(no módulo Data Warehouse, menu Manutenção >> Cadastros Parâmetros >> Pessoa Física Jurídica por Ramo de Atividade\)

Fazer as seguintes consistências:

1 \- Se a UF Pessoa Fis/Jur da nota não estiver preenchida exibir mensagem no log de erros e ignorar registro:

Existe pessoa juridica com a informacao de estado nula, estes registros serao ignorados na geracao, favor verificar

2\- A Pessoa Fis/Jur da nota deve ter Ramo de Atividade cadastrado no módulo Data Warehouse, menu Manutenção >> Cadastros Parâmetros >> Pessoa Física Jurídica por Ramo de Atividade\. Caso não exista cadastro exibir mensagem no log de erros e ignorar registro:

Pessoa Fisica/Juridica nao esta parametrizada para um ramo de atividade \(Cadastro de Pessoa Fisica/Juridica por Ramo de Atividade, no modulo DataWarehouse\)\.

Gravar os campos do Quadro 10 conforme regras abaixo\. O registro gerado está disponível para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 4 a 15\.

Tabela: CBT\_ANEXO6M\_QUADR4A15

__\[MFS658449\] __Alteração do tratamento do campo UF Destinatária para verificar a UF de consumo da nota\.  Se a UF Ponto de Consumo não estiver preenchida, utilizar a UF da Pessoa Fis/Jur da nota, que era o campo utilizado anteriormente\.

Quadro 10 \- DEDUÇÃO POR RESSARCIMENTO EFETUADO A DISTRIBUIDORAS

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF do Ponto de Consumo da nota \(campo 207 \- UF\_CONSUMO da SAFX07\), se não estiver preenchida utilizar a UF da Pessoa Fis/Jur da nota

Quadro

cod\_tag

A6MQ10  

cod\_quadro

Não preencher

Pessoa Fis/Jur

ident\_fis\_jur        

Idenrificador da Pessoa Fis/Jur da nota

UF do Quadro

ident\_estado\_quad    

Não preencher

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Se Valor ICMS Substituição Tributária \(item 52 VLR\_SUBST\_ICMS da SAFX08\) = 0 Então

  Preencher com Valor Contábil do Item \(item 64 VLR\_CONTAB\_ITEM da SAFX08\);

Senão

  Preencher com Valor ICMS Substituição Tributária \(item 52 VLR\_SUBST\_ICMS da SAFX08\);

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

## <a id="_Toc211245073"></a>RN11 \- Geração do Anexo VI\-M \- Quadro 11

Mesma regra da geração do quadro 10, apenas considerando o Ramo de Atividade da Pessoa Fis/Jur da nota fiscal deve ser 106 – TRR \(no módulo Data Warehouse, menu Manutenção >> Cadastros Parâmetros >> Pessoa Física Jurídica por Ramo de Atividade\)\.

Gravar os campos do Quadro 11 com as mesmas regras de preenchimento dos campos do quadro 10, diferenciando apenas o preenchimento do campo cod\_tag\.

O registro gerado está disponível para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 4 a 15\.

Tabela: CBT\_ANEXO6M\_QUADR4A15

__\[MFS658449\] __Alteração do tratamento do campo UF Destinatária para verificar a UF de consumo da nota\.  Se a UF Ponto de Consumo não estiver preenchida, utilizar a UF da Pessoa Fis/Jur da nota, que era o campo utilizado anteriormente\.

Quadro 11 \- DEDUÇÃO POR RESSARCIMENTO EFETUADO A TRR

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF do Ponto de Consumo da nota \(campo 207 \- UF\_CONSUMO da SAFX07\), se não estiver preenchida utilizar a UF da Pessoa Fis/Jur da nota

Quadro

cod\_tag

__A6MQ11 __

cod\_quadro

Não preencher

Pessoa Fis/Jur

ident\_fis\_jur        

Idenrificador da Pessoa Fis/Jur da nota

UF do Quadro

ident\_estado\_quad    

Não preencher

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Se Valor ICMS Substituição Tributária \(item 52 VLR\_SUBST\_ICMS da SAFX08\) = 0 Então

  Preencher com Valor Contábil do Item \(item 64 VLR\_CONTAB\_ITEM da  SAFX08\);

Senão

  Preencher com Valor ICMS Substituição Tributária \(item 52 VLR\_SUBST\_ICMS da SAFX08\);

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

## <a id="_Toc211245074"></a>RN12 \- Geração do Anexo VI\-M \- Quadro 12

Mesma regra da geração do quadro 10, apenas considerando o Ramo de Atividade da Pessoa Fis/Jur da nota fiscal deve ser 97 – Importador \(no módulo Data Warehouse, menu Manutenção >> Cadastros Parâmetros >> Pessoa Física Jurídica por Ramo de Atividade\)\.

Gravar os campos do Quadro 12 com as mesmas regras de preenchimento dos campos do quadro 10, diferenciando apenas o preenchimento do campo cod\_tag\.

O registro gerado está disponível para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 4 a 15\.

Tabela: CBT\_ANEXO6M\_QUADR4A15

__\[MFS658449\] __Alteração do tratamento do campo UF Destinatária para verificar a UF de consumo da nota\.  Se a UF Ponto de Consumo não estiver preenchida, utilizar a UF da Pessoa Fis/Jur da nota, que era o campo utilizado anteriormente\.

Quadro 12 \- DEDUÇÃO POR RESSARCIMENTO EFETUADO A IMPORTADORES

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF do Ponto de Consumo da nota \(campo 207 \- UF\_CONSUMO da SAFX07\), se não estiver preenchida utilizar a UF da Pessoa Fis/Jur da nota

Quadro

cod\_tag

__A6MQ12 __

cod\_quadro

Não preencher

Pessoa Fis/Jur

ident\_fis\_jur        

Idenrificador da Pessoa Fis/Jur da nota

UF do Quadro

ident\_estado\_quad    

Não preencher

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Se Valor ICMS Substituição Tributária \(item 52 VLR\_SUBST\_ICMS da SAFX08\) = 0 Então

  Preencher com Valor Contábil do Item \(item 64 VLR\_CONTAB\_ITEM da SAFX08\);

Senão

  Preencher com Valor ICMS Substituição Tributária \(item 52 VLR\_SUBST\_ICMS da SAFX08\);

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

## <a id="_Toc211245075"></a>RN13 \- Geração do Anexo VI\-M \- Quadro 13

Mesma regra da geração do quadro 10, apenas considerando o Ramo de Atividade da Pessoa Fis/Jur da nota fiscal deve ser diferente de 97 – Importador, 104 – Distribuidora e 106 – TRR \(no módulo Data Warehouse, menu Manutenção >> Cadastros Parâmetros >> Pessoa Física Jurídica por Ramo de Atividade\)\.

Gravar os campos do Quadro 13 com as mesmas regras de preenchimento dos campos do quadro 10, diferenciando apenas o preenchimento do campo cod\_tag\.

O registro gerado está disponível para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 4 a 15\.

Tabela: CBT\_ANEXO6M\_QUADR4A15

__\[MFS658449\] __Alteração do tratamento do campo UF Destinatária para verificar a UF de consumo da nota\.  Se a UF Ponto de Consumo não estiver preenchida, utilizar a UF da Pessoa Fis/Jur da nota, que era o campo utilizado anteriormente\.

Quadro 13 \- DEDUÇÃO POR RESSARCIMENTO EFETUADO A OUTROS CONTRIBUINTES

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF do Ponto de Consumo da nota \(campo 207 \- UF\_CONSUMO da SAFX07\), se não estiver preenchida utilizar a UF da Pessoa Fis/Jur da nota

Quadro

cod\_tag

__A6MQ13__

cod\_quadro

Não preencher

Pessoa Fis/Jur

ident\_fis\_jur        

Idenrificador da Pessoa Fis/Jur da nota

UF do Quadro

ident\_estado\_quad    

Não preencher

Mês/Ano Referência do Quadro

dat\_ref

Último dia do mês/ano da geração

Vlr ICMS

vlr\_icms

Se Valor ICMS Substituição Tributária \(item 52 VLR\_SUBST\_ICMS da SAFX08\) = 0 Então

  Preencher com Valor Contábil do Item \(item 64 VLR\_CONTAB\_ITEM da SAFX08\);

Senão

  Preencher com Valor ICMS Substituição Tributária \(item 52 VLR\_SUBST\_ICMS da SAFX08\);

Comunicado

comunic\_ref

Não preencher

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

## <a id="_Toc211245076"></a>RN14 \- Geração do Anexo VI\-M \- Quadro 14

Esse quadro não é gerado\.

## <a id="_Toc211245077"></a>RN15 \- Geração do Anexo VI\-M \- Quadro 15

Esse quadro não é gerado\.

## <a id="_RN16_-_Geração"></a><a id="RN16"></a><a id="_Toc211245078"></a>RN16 \- Geração do Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras 

__MFS576550: Novo Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras__

Os Quadros gerados a partir dos anexos lidos dos arquivos das Distribuidoras serão detalhados através do Relatório “Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras” São eles:

Quadro do Anexo VI\-M

Anexo de Origem \(arquivo da Distribuidora\)

A6MQ41 1

III\-M

A6MQ41 21

XI\-M

A6MQ41 22

XI\-M

A6MQ42  

III\-M

A6MQ5

III\-M

A6MQ61

V\-M\-AJ, V\-M e XI\-M\-AJ \[MFS783073\]

A6MQ71 1

III\-M

A6MQ71 21

XI\-M

A6MQ71 22

XI\-M

A6MQ72  

III\-M

A6MQ8

III\-M

A6MQ91

V\-M\-AJ, V\-M e XI\-M\-AJ \[MFS783073\]

Cada anexo lido do arquivo de Origem da Distribuidora irá gravar dois registros na tabela do Anexo VI\-M \(CBT\_ANEXO6M\_QUADR4A15\) e dois na tabela do relatório CBT\_ANEXO6M\_RELAT\. Os registros são: um de repasse e outro de Dedução\.

Cada registro do Anexo VI\-M pode ter 1 ou N registros na tabela do relatório, ou seja, mais de um anexo do Arquivo de Origem da Distribuidora compõe o registro do Anexo VI\-M\.

O registro será gravado na tabela CBT\_ANEXO6M\_RELAT com os seguintes campos preenchidos:

  cod\_empresa          = Idem a informação gravada na CBT\_ANEXO6M\_QUADR4A15

  cod\_estab            = Idem a informação gravada na CBT\_ANEXO6M\_QUADR4A15

  dat\_apuracao         = Idem a informação gravada na CBT\_ANEXO6M\_QUADR4A15

  ident\_estado\_destino = Idem a informação gravada na CBT\_ANEXO6M\_QUADR4A15

  cod\_tag              = Idem a informação gravada na CBT\_ANEXO6M\_QUADR4A15

  cod\_quadro           = Idem a informação gravada na CBT\_ANEXO6M\_QUADR4A15

  ident\_fis\_jur        = Idem a informação gravada na CBT\_ANEXO6M\_QUADR4A15

  ident\_estado\_quad    = Idem a informação gravada na CBT\_ANEXO6M\_QUADR4A15

  dat\_ref              = Idem a informação gravada na CBT\_ANEXO6M\_QUADR4A15

  ind\_repasse\_deducao  = ‘R’ para os quadros de Repasse \(4,5,6\) ‘D’ para os quadros de Dedução \(7, 8, 9\)

  vlr\_icms\_anx6M       = Valor do ICMS do Anexo lido do Arquivo da Distribuidora

  ID\_GRUPO             = ID\_GRUPO do Anexo lido do Arquivo da Distribuidora

    ANEXO\_ORIGEM         = preencher c/ a identificação do anexo lido do arquivo da Distribuidora \(ex: ‘A3M’, ‘A11M’,’A5M’,’A5MAJ’, ’A11MAJ’\)

  UF\_DESTINO           = UFDestino do Anexo lido do Arquivo da Distribuidora

  UF\_ORIGEM            = UFOrigem do Anexo lido do Arquivo da Distribuidora

  UF\_EMITENTE          = UFEmitente do Anexo lido do Arquivo da Distribuidora

  CATEGORIA\_EMITENTE   = Categoria Emitente do Anexo lido do Arquivo da Distribuidora

  CNPJ\_EMITENTE        = CNPJ Emitente do Anexo lido do Arquivo da Distribuidora

  RAZAO\_SOCIAL\_EMITENTE=Razão Social do Emitente do Anexo lido do Arquivo da Distribuidora

  CNPJ\_DESTINATARIO    =CNPJ do Destinatário do Anexo lido do Arquivo da Distribuidora

  CNPJ\_FORNECEDOR      =CNPJ do Fornecedor do Anexo lido do Arquivo da Distribuidora

  UF\_REPASSE           = Pode ser a UFDestino, UFOrigem ou UFEmitente, dependendo do Anexo lido do Arquivo da Distribuidora

  UF\_DEDUCAO           = Pode ser a UFDestino, UFOrigem ou UFEmitente, dependendo do Anexo lido do Arquivo da Distribuidora

  VLR\_ICMS\_ANX\_DISTRIB = Valor do ICMS do Anexo lido do Arquivo da Distribuidora 

  DSC\_DIG\_CALC         = não preencher

  usuario              = usuário de login do sistema

  num\_processo         = número do processo da geração do anexo

  ind\_dig\_calc         = 2 – inserido via geração do Anexo VI\-M

Ver documento matriz <a id="_Toc155549588"></a>MTZ\_Relatorio\_Conferencia\_Anexos\_VI\_VI\-M\_VII\_VII\-M\.docx tópico 11 – “Relatório Anexo VI\-M \- Quadros 4 ao 9 x Anexos lidos do Arquivo das Distribuidoras” para mais informações quanto ao preenchimento dos campos na tabela\.

## <a id="_Toc211245079"></a>RN17 \- Geração do Anexo VI \- Quadro 3

Quadro gerado a partir das Notas de Saídas e devoluções de vendas de Produtos sujeitos a tributação monofásica\.

Segundo a legislação que regulamenta o regime monofásico sobre combustíveis, o Diesel, Biodiesel e GLP/GLGN entram nesse regime em Maio/2023, portando, a partir desse mês devem ser apresentados no Anexo VI\-M e não mais no Anexo VI\. A Gasolina e EAC entram aderem ao monofásico do ICMS a partir de Junho/2023\. Uma vez que o combustível é apresentado no Anexo VI\-M ele deixa de compor o Anexo VI\.

Os principais critérios para identificação da nota nesse novo regime são: os CSTs e o produto enquadrado na lista de produtos\.

__Critérios de Seleção:__

Para geração desse quadro recuperar os documentos fiscais a partir das tabelas SAFX07 e SAFX08, considerando os seguintes critérios:

\- Código da empresa = código da empresa da geração; 

\- Código do estabelecimento: depende do parâmetro “Inscrição Estadual Única” informado na tela de geração\.

   Se parâmetro desmarcado, então considerar apenas notas do estabelecimento selecionado na geração;

   Se parâmetro marcado, considerar as notas do estabelecimento centralizador selecionado na geração e dos estabelecimentos centralizados\. 

\- Data Fiscal compreendida no mês/ano Referência informado na geração;

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Somente notas com item de mercadoria \(SAFX08\);

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu: Parâmetros > Anexos I, II, III, IV, V, VI e VIII para os tipos:

  88 \- Saída,

  90 \- devolução de venda,

  92 – saída a consumidor final, 

  93 \- devolução de venda para consumidor final

\- Considerar a Parametrização da Regras p/ Geração dos Anexos feita para o estabelecimento no item de menu: Parâmetros > Regras p/ Geração dos Anexos\. 

   Se o Campo “Considerar somente as Notas Fiscais com movimentação física de mercadoria” estiver marcado, então recuperar 

   apenas itens de mercadoria com Ind\. Movim\. Física da Merc\. \(campo 115\-IND\_MOV\_FIS da SAFX08\) = ‘S’;

   Se desmarcado, recuperar independente do Ind\. Movim\. Física da Merc\. \(campo 115\-IND\_MOV\_FIS da SAFX08\) ser S ou N\.

\- Produto do item da nota deve ser parametrizado no item de menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados, com o seu respectivo grupo de combustíveis \(SAFX96\)

\- O Grupo de Combustível parametrizado para o produto, deve estar com o flag Anexo VI selecionado, no menu Parâmetros 🡪 Grupos de Combustíveis e Derivados\.

Ao recuperar a nota fiscal com os critérios acima, fazer a seguinte consistência:

Se a UF Pessoa Fis/Jur da não estiver preenchida exibir mensagem no log de erros e ignorar registro:

Existe pessoa juridica com a informacao de estado nula, estes registros serao ignorados na geracao, favor verificar\.

__\[MFS616801\] __Alteração do tratamento do campo UF Destinatária para verificar a UF de consumo da nota, se o CFOP for igual a “5667” ou “6667”\.  Se a UF Ponto de Consumo não estiver preenchida, utilizar a UF da Pessoa Fis/Jur da nota, que era o campo utilizado anteriormente\.

Gravar os campos do Quadro 3 conforme regras abaixo\. O registro gerado está disponível para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI 🡪 Quadro 3\.

Tabela: CBT\_ANEXO6\_QUADR3

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI

Ident\_estado\_destino

Se CFOP = ‘5667’ ou ‘6667’ \(campo 22\- COD\_CFO da SAFX08\)

     UF do Ponto de Consumo da nota \(campo 207 \- UF\_CONSUMO da SAFX07\)

Senão se  UF do Ponto de Consumo não estiver preenchida ou CFOP <> ‘5667’ e ‘6667’

                UF da Pessoa Fis/Jur da nota           

Grupo Combustível

Ident\_grupo\_comb

Identificador do Grupo de Combustivel da parametrização do produto\.

Quantidade \(Base de Cálculo\)

Qtd\_comb

Quantidade do Item de Mercadoria \(campo 24\- QUANTIDADE da SAFX08\)

Se medida do item for diferente da parametrizada para o produto \(Parâmetros > Produtos x Grupos de Combustíveis e Derivados SAFX96\), aplicar a conversão de unidades de medida\.

Vlr Operação

Vlr\_Operacao

Valor Contábil do item \(campo 64\- VLR\_CONTAB\_ITEM da SAFX08\)

Gravar o valor com sinal positivo ou negativo dependendo da parametrização do CFOP ou CFOP/NAT:

\+ se  parametrizado para saída \(88, 92\)

\- se  parametrizado para devolução \(90, 93\)

Vlr ICMS 

Vlr\_ICMS

Valor do ICMS \(campo 43\-VLR\_ICMS da SAFX08\)

Gravar o valor com sinal positivo ou negativo dependendo da parametrização do CFOP ou CFOP/NAT:

\+ se  parametrizado para saída \(88, 92\)

\- se  parametrizado para devolução \(90, 93\)

Vlr ICMS ST

Vlr\_ICMS\_ST

Valor ICMS Substituição Tributária \(campo 52\- VLR\_SUBST\_ICMS da SAFX08\)

Gravar o valor com sinal positivo ou negativo dependendo da parametrização do CFOP ou CFOP/NAT:

\+ se  parametrizado para saída \(88, 92\)

\- se  parametrizado para devolução \(90, 93\)

Vlr ICMS Total

Vlr\_ICMS\_Tot

Soma dos dois campos anteriores \(Vlr ICMS \+ Vlr ICMS ST\)

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

## <a id="_Toc211245080"></a>RN10 \- Geração do Anexo VI \- Quadro 10

Quadro gerado a partir das Notas Fiscais de ressarcimento dos Produtos cadastrados no Grupo de Combustíveis e Derivados\.

__Critérios de Seleção:__

Para geração desse quadro recuperar os documentos fiscais a partir das tabelas SAFX07, SAFX08, considerando os seguintes critérios:

\- Código da empresa = código da empresa da geração; 

\- Código do estabelecimento: depende do parâmetro “Inscrição Estadual Única” informado na tela de geração\.

   Se parâmetro desmarcado, então considerar apenas notas do estabelecimento selecionado na geração;

   Se parâmetro marcado, considerar as notas do estabelecimento centralizador selecionado na geração e dos estabelecimentos centralizados\. 

\- Data Fiscal compreendida no mês/ano Referência informado na geração;

\- Somente notas não canceladas \(campo 30\-SITUACAO da SAFX07 <> S\);

\- Somente notas com item de mercadoria \(SAFX08\);

\- Somente itens com CFOP ou CFOP/NAT parametrizados no menu: Parâmetros > Anexos I, II, III, IV, V, VI e VIII para os tipos:

  108 – Ressarcimentos Autorizados de ICMS\-ST

\- Produto do item da nota deve ser parametrizado no item de menu: Parâmetros > Produtos x Grupos de Combustíveis e Derivados, com o seu respectivo grupo de combustíveis \(SAFX96\)

\- O Grupo de Combustível parametrizado para o produto, deve estar com o flag Anexo VI selecionado, no menu Parâmetros 🡪 Grupos de Combustíveis e Derivados\.

\- Ramo de Atividade da Pessoa Fis/Jur da nota fiscal deve ser 104 – Distribuidora \(no módulo Data Warehouse, menu Manutenção >> Cadastros Parâmetros >> Pessoa Física Jurídica por Ramo de Atividade\)

Fazer as seguintes consistências:

1 \- Se a UF Pessoa Fis/Jur da nota não estiver preenchida exibir mensagem no log de erros e ignorar registro:

Existe pessoa juridica com a informacao de estado nula, estes registros serao ignorados na geracao, favor verificar

2\- A Pessoa Fis/Jur da nota deve ter Ramo de Atividade cadastrado no módulo Data Warehouse, menu Manutenção >> Cadastros Parâmetros >> Pessoa Física Jurídica por Ramo de Atividade\. Caso não exista cadastro exibir mensagem no log de erros e ignorar registro:

Pessoa Fisica/Juridica nao esta parametrizada para um ramo de atividade \(Cadastro de Pessoa Fisica/Juridica por Ramo de Atividade, no modulo DataWarehouse\)\.

Gravar os campos do Quadro 10 conforme regras abaixo\. O registro gerado está disponível para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI 🡪 Quadros 10, 11, 12 e 13\.

Tabela: CBT\_ANEXO6\_QUADR10

__\[MFS658449\] __Alteração do tratamento do campo UF Destinatária para verificar a UF de consumo da nota\.  Se a UF Ponto de Consumo não estiver preenchida, utilizar a UF da Pessoa Fis/Jur da nota, que era o campo utilizado anteriormente\.

Quadro 10 \- DEDUÇÃO POR RESSARCIMENTO EFETUADO A DISTRIBUIDORAS

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI

Ident\_estado\_destino

UF do Ponto de Consumo da nota \(campo 207 \- UF\_CONSUMO da SAFX07\), se não estiver preenchida utilizar a UF da Pessoa Fis/Jur da nota

Indicador de Quadro

Ind\_quadro

10  

Pessoa Fis/Jur

ident\_fis\_jur        

Idenrificador da Pessoa Fis/Jur da nota

Vlr ICMS

vlr\_icms\_st

Se Valor ICMS Substituição Tributária \(item 52 VLR\_SUBST\_ICMS da SAFX08\) = 0 Então

  Preencher com Valor Contábil do Item \(item 64 VLR\_CONTAB\_ITEM da SAFX08\);

Senão

  Preencher com Valor ICMS Substituição Tributária \(item 52 VLR\_SUBST\_ICMS da SAFX08\);

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

## <a id="_Toc211245081"></a>RN11 \- Geração do Anexo VI \- Quadro 11

Mesma regra da geração do quadro 10, apenas considerando o Ramo de Atividade da Pessoa Fis/Jur da nota fiscal deve ser 106 – TRR \(no módulo Data Warehouse, menu Manutenção >> Cadastros Parâmetros >> Pessoa Física Jurídica por Ramo de Atividade\)\.

Gravar os campos do Quadro 11 com as mesmas regras de preenchimento dos campos do quadro 10, diferenciando apenas o preenchimento do campo Indicador de Quadro\.

O registro gerado está disponível para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI 🡪 Quadros 10, 11, 12 e 13\.

Tabela: CBT\_ANEXO6\_QUADR10

__\[MFS658449\] __Alteração do tratamento do campo UF Destinatária para verificar a UF de consumo da nota\.  Se a UF Ponto de Consumo não estiver preenchida, utilizar a UF da Pessoa Fis/Jur da nota, que era o campo utilizado anteriormente\.

Quadro 11 \- DEDUÇÃO POR RESSARCIMENTO EFETUADO A TRR

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF do Ponto de Consumo da nota \(campo 207 \- UF\_CONSUMO da SAFX07\), se não estiver preenchida utilizar a UF da Pessoa Fis/Jur da nota

Indicador de Quadro

Ind\_quadro

__11 __

Pessoa Fis/Jur

ident\_fis\_jur        

Idenrificador da Pessoa Fis/Jur da nota

Vlr ICMS

vlr\_icms\_st

Se Valor ICMS Substituição Tributária \(item 52 VLR\_SUBST\_ICMS da SAFX08\) = 0 Então

  Preencher com Valor Contábil do Item \(item 64 VLR\_CONTAB\_ITEM da  SAFX08\);

Senão

  Preencher com Valor ICMS Substituição Tributária \(item 52 VLR\_SUBST\_ICMS da SAFX08\);

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

## <a id="_Toc211245082"></a>RN12 \- Geração do Anexo VI \- Quadro 12

Mesma regra da geração do quadro 10, apenas considerando o Ramo de Atividade da Pessoa Fis/Jur da nota fiscal deve ser 97 – Importador \(no módulo Data Warehouse, menu Manutenção >> Cadastros Parâmetros >> Pessoa Física Jurídica por Ramo de Atividade\)\.

Gravar os campos do Quadro 12 com as mesmas regras de preenchimento dos campos do quadro 10, diferenciando apenas o preenchimento do campo Indicador de Quadro\.

O registro gerado está disponível para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadros 10, 11, 12 e 13\.

Tabela: CBT\_ANEXO6\_QUADR10

__\[MFS658449\] __Alteração do tratamento do campo UF Destinatária para verificar a UF de consumo da nota\.  Se a UF Ponto de Consumo não estiver preenchida, utilizar a UF da Pessoa Fis/Jur da nota, que era o campo utilizado anteriormente\.

Quadro 12 \- DEDUÇÃO POR RESSARCIMENTO EFETUADO A IMPORTADORES

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF do Ponto de Consumo da nota \(campo 207 \- UF\_CONSUMO da SAFX07\), se não estiver preenchida utilizar a UF da Pessoa Fis/Jur da nota

Indicador de Quadro

Ind\_quadro

__12 __

Pessoa Fis/Jur

ident\_fis\_jur        

Idenrificador da Pessoa Fis/Jur da nota

Vlr ICMS

vlr\_icms\_st

Se Valor ICMS Substituição Tributária \(item 52 VLR\_SUBST\_ICMS da SAFX08\) = 0 Então

  Preencher com Valor Contábil do Item \(item 64 VLR\_CONTAB\_ITEM da SAFX08\);

Senão

  Preencher com Valor ICMS Substituição Tributária \(item 52 VLR\_SUBST\_ICMS da SAFX08\);

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

## <a id="_Toc211245083"></a>RN13 \- Geração do Anexo VI \- Quadro 13

Mesma regra da geração do quadro 10, apenas considerando o Ramo de Atividade da Pessoa Fis/Jur da nota fiscal deve ser diferente de 97 – Importador, 104 – Distribuidora e 106 – TRR \(no módulo Data Warehouse, menu Manutenção >> Cadastros Parâmetros >> Pessoa Física Jurídica por Ramo de Atividade\)\.

Gravar os campos do Quadro 13 com as mesmas regras de preenchimento dos campos do quadro 10, diferenciando apenas o preenchimento do campo Indicador de Quadro\.

O registro gerado está disponível para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VI 🡪 Quadros 10, 11, 12 e 13\.

Tabela: CBT\_ANEXO6\_QUADR10

__\[MFS658449\] __Alteração do tratamento do campo UF Destinatária para verificar a UF de consumo da nota\.  Se a UF Ponto de Consumo não estiver preenchida, utilizar a UF da Pessoa Fis/Jur da nota, que era o campo utilizado anteriormente\.

Quadro 13 \- DEDUÇÃO POR RESSARCIMENTO EFETUADO A OUTROS CONTRIBUINTES

Nome do Campo

Nome físico do campo

Regra de Preenchimento 

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF do Ponto de Consumo da nota \(campo 207 \- UF\_CONSUMO da SAFX07\), se não estiver preenchida utilizar a UF da Pessoa Fis/Jur da nota

Indicador de Quadro

Ind\_quadro

__13__

cod\_quadro

Não preencher

Pessoa Fis/Jur

ident\_fis\_jur        

Idenrificador da Pessoa Fis/Jur da nota

Vlr ICMS

vlr\_icms\_st

Se Valor ICMS Substituição Tributária \(item 52 VLR\_SUBST\_ICMS da SAFX08\) = 0 Então

  Preencher com Valor Contábil do Item \(item 64 VLR\_CONTAB\_ITEM da SAFX08\);

Senão

  Preencher com Valor ICMS Substituição Tributária \(item 52 VLR\_SUBST\_ICMS da SAFX08\);

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação


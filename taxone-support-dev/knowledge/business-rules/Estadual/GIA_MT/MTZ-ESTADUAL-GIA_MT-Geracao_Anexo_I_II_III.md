# MTZ-ESTADUAL-GIA_MT-Geracao_Anexo_I_II_III

- **Fonte:** MTZ-ESTADUAL-GIA_MT-Geracao_Anexo_I_II_III.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 40 KB

---

# GIA MT

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3111\-G

GIA MT

Alteração na forma de geração dos Anexos I e II 

OS 3148

GIA\-MT \- Ajustes na geração por IE Única

Correção na geração das informações do anexo I\.

OS3342

GIA\-MT \- Parametrizar geração do Anexo I

Parametrizar geração do Anexo I por CFOP ou CFOP/Natureza de Operação

CH91858

GIA MT – Ajuste na geração do Anexo I

GIA MT – Ajuste na geração do Anexo I

CH12576

GIAMT \- Correção  Código de Município

GIA MT – Ajuste na geração do Anexo I

## REGRAS DE NEGÓCIO

#### Cód\.

### Alteração nas regras de geração para composição dos seguintes campos dos Anexo I e II

### DR

__RN00__

__Obrigações → GIA ICMS 3\.07i __

__Geração das Informações do Anexo I__

Na geração deste anexo consideraremos os códigos de operação 03 e 05, representando as características a seguir:

__Código de Operação 03:__

Este código será gerado quando “*Geração para Empresas c/ Insc\. Estadual Única*” estiver marcado, onde iremos apresentar os valores das saídas por Município\. Os documentos de saída deverão ser consolidados seguindo os critérios abaixo:

Parâmetro “Considerar Município do Ponto de Consumo \(Utilities\)” = “NÃO”

Nesta situação devemos listar os totais de todas as notas de saída existentes no período na SAFX07, totalizando seus valores por Município de origem da prestação ou pelo Município da pessoa física/jurídica, o que estiver preenchido\.

Parâmetro “Considerar Município do Ponto de Consumo \(Utilities\)” = “SIM”

Nesta situação devemos listar os totais das notas de saída existentes no período na SAFX07, excluindo\-se os mapas\-resumo gerados a partir dos documentos fiscais utilities \(SAFX42\), totalizando seus valores por Município do Ponto de Consumo \(campo 208 da SAFX07\) ou pelo Município da pessoa física/jurídica \(campo 25 da SAFX04\), o que estiver preenchido respectivamente nesta ordem\.

Além destas notas, devemos recuperar também o total das notas fiscais utilities existentes no período na SAFX42, totalizando seus valores por Município do Ponto de Consumo \(campo 76 da SAFX42\)\. O resultado final deverá ser a soma por Município, destas notas\.

__Obs\.:__ em ambos os casos acima os Municípios devem pertencer ao Estado do Mato Grosso\.

Somente serão considerados os CFOP’s ou CFOP/Natureza de Operação parametrizados em:

GIA\-MT → Anexo I → CFOP ou

GIA\-MT → Anexo I → CFOP/Natureza de Operação

Somente considerar uma das parametrizações\. Se tiver parametrização por CFOP/Natureza, não considerar a parametrização por CFOP e vice\-versa\.

Este código é gerado apenas por estabelecimentos com inscrição centralizada\. Desta forma, considerar parâmetros do estabelecimento centralizador\.

__Código de Operação 05:__

Este código representa as operações de entrada provenientes do Estado do Mato Grosso, adquiridas de pessoa não obrigada a possuir inscrição estadual, portanto, devemos considerar as notas de entrada emitidas pela pessoa física/jurídica \(movto\. de E/S iguais 2, 3, 4 ou 5\) no período, totalizando\-as por Município de origem da mercadoria, neste consideraremos o Município informado no cadastro da pessoa física/jurídica \(campo 25 da SAFX04\)\.

O parâmetro “Considerar Município do Ponto de Consumo \(Utilities\)” não terá qualquer efeito sobre este código de operação\.

Somente serão considerados os CFOP’s ou CFOP/Natureza de Operação parametrizados em:

GIA\-MT → Anexo I → CFOP ou

GIA\-MT → Anexo I → CFOP/Natureza de Operação

Somente considerar uma das parametrizações\. Se tiver parametrização por CFOP/Natureza, não considerar a parametrização por CFOP e vice\-versa\.

No caso de geração centralizada, considerar parâmetros do estabelecimento centralizador\.

REGRA ANTERIOR \- ALTERADA PELA OS 3148

Criar na tela o parâmetro: 

Considerar Município do Ponto de Consumo \(Utilities\): \[  \]

Quando o flag estiver marcado:

\- Considerar o Município do Ponto de Consumo \(campo 76/safx42\) na geração do campo 02/Anexos I e II

\- Esta situação irá se aplicar às notas de entradas e saídas que estiverem na safx42 \(modelo 01, 06, 21 ou 22\) para o Anexo I  e devolução de entradas e saídas para Anexo II

\- Para as notas que estiverem na x07, considerar o município do cadastro da pessoa fis/jur \(safx04\)

Quando o flag estiver desmarcado:

\- Considerar o município do cadastro de pessoa fis/jur, \(campos\), de acordo com a pessoa fis/jur da NF\.

OS3111\-G

OS3148 

OS3342

__RN01__

__Anexos I e II Campo Código do Município__

Caso o parâmetro ¨Considerar Município do Ponto de Consumo \(Utilities\)¨ estiver marcado:

Considerar o município do ponto de consumo \(campo 76/safx42\)\.

Esta regra se aplica tanto para a geração normal, quanto para a geração por inscrição estadual única\.

Com base neste código, fazer a correspondência com os códigos específicos do Mato Grosso  \(Município IBGE x Município das UF’s – TACES24\)\.

Para gerações efetuadas a partir da safx07 o sistema atualmente efetua as conversões \(Município IBGE x Tabela dos Códigos dos Municípios GIA\-MT\) para os seguintes códigos: 

 

__Municípios IBGE__

__Municípios GIA MT__

102

00500\-2

201

01000\-6

250

01500\-8

300

02000\-1

359

02300\-0

409

02500\-3

508

03000\-7

607

03200\-0

805

03300\-6

1001

03400\-2

1209

03500\-9

1258

04000\-2

1308

04500\-4

1407

05000\-8

1605

05500\-0

1704

06000\-3

1803

06500\-5

1852

06700\-8

1902

06800\-4

2504

07000\-9

2603

07300\-8

2637

07400\-4

2678

07200\-1

2686

08600\-2

2694

07600\-7

2702

07500\-0

2793

07700\-3

2850

08100\-0

3007

08000\-4

3056

08400\-0

3106

08300\-3

3205

08500\-6

3254

08200\-7

3304

08800\-5

3353

08900\-1

3361

08700\-9

3379

09100\-6

3403

09000\-0

3437

09200\-2

3452

09300\-9

3502

09500\-1

3601

10000\-5

3700

10200\-8

3809

10300\-4

3858

10400\-0

3908

10500\-7

3957

10700\-0

4104

10800\-6

4203

11000\-0

4500

11200\-3

4526

11100\-7

4542

11400\-6

4559

11300\-0

4609

11500\-2

4807

12000\-6

4906

12200\-9

5002

12500\-8

5101

13000\-1

5150

13300\-0

5176

13400\-7

5200

13500\-3

5234

3600\-0 

5259

13900\-9

5309

14000\-7

5580

14300\-6

5606

14400\-2

5622

14500\-9

5903

15000\-2

6000

15500\-4

6109

16000\-8

6158

16100\-4

6208

16500\-0

6216

16600\-6

8808

16200\-0

6182

15900\-0

8857

16300\-7

8907

16400\-3

8956

16700\-2

6224

17100\-0

6174

15700\-7

6232

16800\-9

6190

15800\-3

6240

16900\-5

6257

17000\-3

6273

17200\-6

6265

17600\-1

6315

15600\-0

6281

17300\-2

6299

17400\-9

6307

17500\-5

6372

18000\-9

6422

18300\-8

6455

18400\-4

6505

18500\-0

6653

18700\-3

6703

19000\-4

6752

19500\-6

6778

19700\-9

6802

20000\-0

6828

20300\-9

6851

20400\-5

7008

20500\-1

7040

20700\-4

7065

20800\-0

7156

21200\-8

7180

21300\-4

7198

21400\-0

7578

21900\-2

7602

22000\-0

7701

22500\-2

7750

23000\-6

7248

23300\-5

7743

23200\-9

7768

23400\-1

7776

23500\-8

7263

23700\-0

7800

24000\-1

7792

23900\-3

7859

24500\-3

7297

24700\-6

7305

2500\-7 

7354

21100\-1

7107

21000\-5

7404

20900\-7

7875

25200\-0

7909

25500\-9

7925

25700\-1

7941

25800\-8

7958

26000\-2

8006

26200\-5

8055

26300\-1

8105

26500\-4

8204

27000\-8

8303

27200\-3

27200\-0

8352

27400\-3

8402

27500\-0

8501

27700\-2

8600

28500\-5

CH12576 \- Corrigir o código 8303 para 27200\-0 conforme destaque\.

OS3111\-G

CH12576\_2012

__RN02__

__Anexo I Campo Valor Contábil__

Caso o parâmetro ¨Considerar Município do Ponto de Consumo \(Utilities\)¨ estiver marcado:

Considerar Notas de Entrada e Saída, campo Valor total da Nota safx42\.

OS3111\-G

__RN03__

__Anexo II Campo Valor Contábil__

Caso o parâmetro ¨Considerar Município do Ponto de Consumo \(Utilities\)¨ estiver marcado:

Considerar Notas de Devolução de Entrada e Saída, campo Valor total da Nota safx42\.

OS3111\-G

__RN04__

__Regra para geração do Anexo 1:__

__Módulo:__ Estadual → GIA MT

__Menu:__ Obrigações → GIA – ICMS 3\.07i

No momento da geração da GIA MT \(também para Inscrição Estadual Única\), o sistema também deve considerar o campo 12 – COD\_CLASS\_DOC\_FIS = ‘4’ \(SAFX07\), quando:

\- Campo 03 – MOVTO\_E\_S = ‘9’ \(SAFX07\)

Para a correta geração do Anexo 1, a parametrização deve ser feita no módulo GIA MT\.

Esta regra deve ter sua funcionalidade para a parametrização Por CFOP e Por CFOP/ Natureza da Operação\.

__CH91858__

__RN05__

__Regra de Consolidação do Anexo II:__

O Anexo II será gerado consolidando as informações por Código do Município \(codgMunicipio\) e Código COP \(codgCop\), sumarizando o valor contábil\. Esta consolidação deve ocorrer tanto na geração por estabelecimento quanto por IEU\.

__CH12576\-A/2012__

__RN06__

__Regra de Geração do Campo COP do Anexo II:__

O campo COP \(codgCop\) para o Anexo II será gerado com base no CFOP do item selecionado, considerando a seguinte regra:

\-> COP = 01, quando cfop for igual a 5207;

\-> COP = 03, quando cfop for entre 1205, 1206, 1207, 2205, 2206, 2207, 3205, 3206, 3207;

\-> COP = 04, quando cfop for entre 1201, 1202;

\-> COP = 05, quando cfop for entre 5201, 5202, 5210;

\-> COP = 06, quando cfop for igual a 5206;

Para outros Códigos de CFOP o campo COP não será preenchido;

A parametrização existente no menu Parâmetros > Anexo I > Por CFOP ou Por CFOP/Natureza da Operação não é utilizada para geração do Anexo II porque para o Anexo II a legislação define CFOPs específicos na geração do COP, cenário não encontrado para o Anexo I e que permite a parametrização\.

Esta regra se aplica tanto na geração por estabelecimento quanto por IEU\.

__CH12576\-A/2012__

__RN07__

__Regra de Geração das Informações de Contribuintes e Não Contribuintes para Utilities, Anexo III:__

Na geração das informações de Contribuintes e não contribuintes do Anexo III, os valores gerados na SAFX07 através do processo de mapa resumo devem ser desconsiderados e o sistema deve buscar estes valores da SAFX42/43, considerando a seguinte regra:

__Campo no Arquivo__

__Campo nas tabelas de Utilities__

codgUfExtendida

Campo UF da pessoa Fis/Jur \(SAFX04\)

valrContabilNaoContribuinte

Campo 19 – Valor do Serviço \(SAFX43\) __menos__ Campo 18 – Valor do Desconto \(SAFX43\), quando não contribuinte

valrContabilContribuinte

Campo 19 – Valor do Serviço \(SAFX43\) __menos__ Campo 18 – Valor do Desconto \(SAFX43\), quando contribuinte

valrBaseCalculoNaoContribuinte

Campo 23 – Base Tributada \(SAFX43\), quando não contribuinte

valrBaseCalculoContribuinte

Campo 23 – Base Tributada \(SAFX43\), quando contribuinte

valrOutras

Campo 25 – Base Outras \(SAFX43\)

valrDemaisValores

Campo 28 – Valor ICMS UF Destino \(SAFX43\)

valrIcmsCobradoPorSubstituicao

Campo 39 – Valor Substituição Tributária \(SAFX43\)

A identificação de Contribuinte e Não Contribuinte deve ser com base no parâmetro 3 – Resumo por UF da tela de Parâmetros por UF\.

Se neste parâmetro for selecionada a opção “Layout Resumido c/ Contr p/ CFOP”, o sistema deve identificar se o CFOP vinculado à NF é de contribuinte ou não contribuinte\.

Se neste parâmetro for selecionada a opção “Layout Resumido c/ Contr p/ Indicador” ou “Layout Completo \(Convênio ICMS\)”, verificar na SAFX42 o campo 85 – Indicador de Consumidor Fiscal\.

__CH12576\-A/2012__

Para o restante do arquivo permanecem as mesmas regras\.

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


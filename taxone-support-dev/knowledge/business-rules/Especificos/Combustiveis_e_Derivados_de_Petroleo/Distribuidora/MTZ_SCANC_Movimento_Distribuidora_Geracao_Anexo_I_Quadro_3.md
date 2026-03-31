# MTZ_SCANC_Movimento_Distribuidora_Geracao_Anexo_I_Quadro_3

- **Fonte:** MTZ_SCANC_Movimento_Distribuidora_Geracao_Anexo_I_Quadro_3.docx
- **Modificado:** 2026-02-05
- **Tamanho:** 86 KB

---

THOMSON REUTERS

Movimento de Distribuidora – Geração Anexo I Quadro 3 \(Relação dos Recebimentos no Período – Entradas\)

Combustível e Derivados de Petróleo \(SCANC\)

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-11111

Julyana Perrucini

Este documento tem como objetivo definir o processo de cálculo do Anexo I – Quadro 3 \(Relação dos Recebimentos no Período – Entradas\) para geração do arquivo magnético do SCANC\.

CH22610\_2017 \(MFS\-14934\)

Julyana Perrucini

Este documento tem como objetivo alterar a geração do campo 22 dos produtos oficiais: 99600, 99610, 64432 e 64433\.

MFS\-16400

Julyana Perrucini

Este documento tem como objetivo alterar a geração da __Regra do Convênio 54: Com base no Convênio 110 __para que o cálculo passe a verificar a data de validade da alíquota interna\.

CH10314\_2018 \(MFS\-18719\)

Julyana Perrucini

Este documento tem como objetivo alterar a geração da __Regra do Convênio 54: Com base no Convênio 110 __para que o cálculo de BXD, Gasolina C, Gasolina C Aditivada, Gasolina C Premium passe a considerar o ramo de atividade em Usina\.

CH18317\_2020 \(MFS\- 46986\)

Rogério Ohashi

Este documento tem como objetivo alterar a regra de geração do Registro Tipo 40, Campo 21, para o Tipo 97, “Importador”\. Inclusão de regra para verificar se houve destaque ou não do imposto, com destaque preencher o campo 21 com “1’” \(Nota Fiscal COM RETENÇÃO do imposto\) ou sem o destaque preencher com “0” \(Nota Fiscal SEM RETENÇÃO do imposto\)\. RN03 \- Inclusão de Regra no Item 7 e criação de nova regra Item 13\.

MFS\-74142

Rogério Ohashi

Este documento tem como objetivo alterar a regra de geração do Registro Tipo 40 para os Campos 22 e 23 p/ parâmetro 89 \(Aquisições e Transferências\) para os produtos derivados de Petróleo\.

MFS\-75599

Rogério Ohashi

Este documento tem como objetivo alterar a regra de geração do Registro Tipo 40 para o Campo 23 p/ Notas Fiscais de Saídas, conforme definição junto à área de Informação, seguiremos as orientações do Manual de Orientação \- SCANC CTB \- Versão do Manual 3\.0\.9\.0 \(16/07/2021\), o “*Campo 23 \- Valor de Imposto do Registro Tipo 40, devem ser informados somente para as Notas Fiscais de Entradas*”\.

MFS\-76521

Rogério Ohashi

Este documento tem como objetivo alterar a regra de geração do Registro Tipo 40 para os Campos 22 e 23 para o parâmetro “*Regra do Convênio 54: Base\-ST da Nota Fiscal*”\.

MFS\-83880

Rogério Ohashi

Este documento tem como objetivo alterar a regra de geração do Registro Tipo 40 para o Campos 23 para o parâmetro “*Regra do Convênio 54: Base\-ST da Nota Fiscal*” para considerar o Campo 80 \- ICMS Não Escriturado\.

MFS\-85500

Rogério Ohashi

Este documento tem como objetivo alterar a regra de geração do Registro Tipo 40 para o Campos 23 para o parâmetro “*Regra do Convênio 54: Base\-ST da Nota Fiscal*” para verificar se o Campo 80 \- ICMS Não Escriturado é maior que zero\. \(Regra para preencher com a soma de ICMS\-ST \+ ICMS \+ ICMS Não destacado\)\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN00

__Regra Geral__

O Quadro 3 do Anexo I do SCANC está relacionado aos recebimentos no período, mas conforme o layout de importação das informações que é representado pelo Registro 40 \- Nota Fiscal \(exceto GLN\), há margem para declaração de notas de entrada, saída e devolução\.

No módulo de Combustível e Derivados de Petróleo, no item de menu Parâmetros, existe um cadastro de Regras p/ Geração dos Anexos, nela existe um item específico para informar a opção de geração para o Anexo I \- Quadro 3\. Como não atendíamos distribuidores só existiam as opções: Regra do Convênio 54: Base ICMS\-ST da Nota Fiscal e Regra Alternativa \(que foi implementada para Texaco no intuito do sistema efetuar o cálculo devido o ICMS\-ST vir destacado apenas nas observações da NF\)\. Basicamente, em atendimento as distribuidoras, o sistema terá que realizar o cálculo porque o ICMS\-ST também vem destacado nas observações da NF, porém a tratativa do cálculo para esse ramo de atividade é diferente, pois se baseia no Convênio ICMS 110, então foi criado o parâmetro: Regra do Convênio 54: Com base no Convênio 110\.

*Observação:* Todo o material utilizado como base para o desenvolvimento do cálculo visando o ramo de atividade de distribuidores está no diretório de documentação do módulo e tivemos apoio da consultoria Adejo Aliz na elaboração das regras focando nos cenários do cliente Total e também nos testes\. Responsável pelo Projeto: Sr\. Vitor Cardoso \([vitor\.cardoso@adejoaliz\.com\.br](mailto:vitor.cardoso@adejoaliz.com.br)\)\. 

No cálculo dos valores do ICMS\-ST a ser declarada através do validador SCANC no Registro 40 \- Nota Fiscal \(exceto GLN\) deverão seguir as seguintes regras para geração dos campos “21\-Valores da BC\-ST e ICMS\-ST obtidos da NF”, “22\-Valor Base de Cálculo” e “23\- Valor total do ICMS”\.

__\[ALTERADA \- CH22610\_2017/MFS\-14934/__ __MFS\-75599\]__

*Considerações:*

- Independente das parametrizações os campos 21, 22 e 23 serão gerados com 0 quando o Código do Produto Oficial for igual a “99600” que se refere a AEAC\. O campo 22 passa a gerar com a informação gerada no campo 19 porque o validador SCANC não aceita esse campo sem valor mesmo que diferido, então ao invés da Base de Cálculo ST é exigido o valor total dos produtos;
- NF de entrada que não seja AEAC, preencher os campos 21, 22, 23;
- NF de saída de óleo combustível e querosene não usa PMPF, preencher os campos 21, 22, 23;
- NF de saída para as UF que não adotam PMPF \(SP, BA, CE, PR, RN e RS\), preencher os campos 21, 22, 23;
- Para todas as saídas de combustível, independente se usam ou não o PMPF, preencher os campos 21, 22, 23;
	- Conforme reavaliação junto à área de informação, seguindo a orientação do Manual de Orientação \- SCANC CTB \- Versão do Manual 3\.0\.9\.0 \(16/07/2021\), o Campo 23 \- Valor de Imposto do Registro Tipo 40, devem ser informados __somente__ para as Notas Fiscais de Entradas\.
- O Registro 40 é apresentado e agrupado por NF e deve ser demonstrado mesmo com os valores zerados nos campos 21, 22 e 23 porque alguns produtos não possuem tributação, mas possui movimentação de estoque, exceto o produto Hidratado, nesse caso os mesmos precisam constar no arquivo, menos o produto Hidratado que não será parametrizado\. A fim de apresentar cada cenário colocaremos a verificação de cada produto na documentação de regra\.

*Observação:* 

- Existe uma condição para Consumidor Final que considerará sempre o ICMS de Destino conforme Convênio ICMS 72 com imposto destacado na NF, exceto para a regra baseada no Convênio ICMS 110\.

MFS\-11111

CH22610\_2017 \(MFS\-14934\)

RN01

Se a opção __Regra do Convênio 54: Base ICMS\-ST da Nota Fiscal __estiver selecionada:

__CAMPO 21__

SE o campo VLR\_TRIBUTO\_ICMSS da tabela DWT\_ITENS\_MERC > 0 OU o campo VLR\_TRIB\_ICMS\_ORIG da tabela DWT\_ITENS\_MERC > 0 E o campo COD\_PROD\_OFICIAL = “64432”, então \(Referente Código de Produto B100\)

                     CAMPO\_21 := 2;

                  SE o parâmetro “Anexos I, II, III, IV, V, VI e VIII” Por CFOP ou Por Extensão CFOP estiver com o campo Tipo igual a “94”, “95” e “96” e __“97”__, então 

                     CAMPO\_21 := 1;

                  SENÃO

                     CAMPO\_21 := 0;

  \[__MFS\-76521__\]  Tratamento na recuperação de valores dos Campos 22 e 23\.                             

__CAMPO 22__

SE o campo VLR\_BASE\_ICMSS da tabela DWT\_ITENS\_MERC <> 0, então

      Preencher o Campo 22 conforme regra abaixo:

                              CAMPO\_22 = VLR\_BASE\_ICMSS da tabela DWT\_ITENS\_MERC  __OU__

                              CAMPO\_22 = VLR\_BASE\_ICMS\_ORIG da tabela DWT\_ITENS\_MERC __OU__

                              CAMPO\_22 = VLR\_BASE\_ICMS\_DEST da tabela DWT\_ITENS\_MERC

  \[__MFS\-83880__\]  Inclusão de tratamento para considerar o campo de ICMS Não Escriturado

__CAMPO 23__

SE o campo VLR\_BASE\_ICMSS da tabela DWT\_ITENS\_MERC <> 0, então

   SE for Nota Fiscal de Entrada preencher o Campo conforme regra abaixo:

       __SE__ o campo VLR\_TRIBUTO\_ICMSS > ‘0’ __OU__ campo VLR\_TRIBUTO\_ICMS > ‘0’ __OU__  campo  VLR\_ICMS\_NDESTAC > ‘0’;

           CAMPO\_23 := VLR\_TRIBUTO\_ICMSS \+ VLR\_TRIBUTO\_ICMS \+ VLR\_ICMS\_NDESTAC da tabela DWT\_ITENS\_MERC 

               __SENÃO  __CAMPO\_23 := VLR\_TRIB\_ICMS\_DEST da tabela DWT\_ITENS\_MERC 

Se for Nota Fiscal de Saída, 

Campo 23 = 0

MFS\-11111

RN02

Se a opção __Regra Alternativa: NF Complementar à Base ICMS\-ST / NF não complementar à Base ICMS\-ST = Vlr Unitário \(PMPF, MVA, ANP\) \* Qtd Combustível__ estiver selecionada:

__CAMPO 21__

SE o campo VLR\_TRIBUTO\_ICMSS da tabela DWT\_ITENS\_MERC > 0 OU o campo VLR\_TRIB\_ICMS\_ORIG da tabela DWT\_ITENS\_MERC > 0 E o campo COD\_PROD\_OFICIAL = “64432”, então \(Referente Código de Produto B100\)

                     CAMPO\_21 := 2;

                  SE o parâmetro “Anexos I, II, III, IV, V, VI e VIII” Por CFOP ou Por Extensão CFOP estiver com o campo Tipo igual a “94”, “95” e “96” e __“97”__, então 

                     CAMPO\_21 := 1;

                  SENÃO

                     CAMPO\_21 := 0;

__CAMPO 22__

SE o campo VLR\_BASE\_ICMSS da tabela DWT\_ITENS\_MERC <> 0, então

                              CAMPO\_22 := VLR\_BASE\_ICMSS da tabela DWT\_ITENS\_MERC

                        SENÃO

                              CAMPO\_22 := VLR\_BASE\_ICMS\_ORIG da tabela DWT\_ITENS\_MERC

__CAMPO 23__

Receberá o resultado do cálculo do valor da Base do ICMS\-ST gerado no CAMPO\_22 \* a Alíquota Interna parametrizada para a UF em Alíquota Interna p/ UF/Grupo Combustível e Derivados /100,2 \+ VLR\_TRIBUTO\_ICMS da tabela DWT\_ITENS\_MERC

MFS\-11111

RN03

Se a opção __Regra do Convênio 54: Com base no Convênio 110__ estiver selecionada, será necessário dividir o processamento em duas etapas, lembrando que essa opção servirá apenas para Distribuidoras porque possui cenários específicos:

__\[ALTERADA \- CH22610\_2017 \(MFS\-14934\)\]__

__1ª Etapa: __Não haverá cálculo das informações\.

1. *Álcool Anidro*

- Recupera os produtos parametrizados na tabela x96\_grp\_comb\_prod com código oficial campo cod\_prod\_oficial = 64432, 64433, 99600 e 99610;
- CFOP parametrizados na tabela prt\_cfo\_msaf ou prt\_extcfo\_msaf com o tipo de movimento campo cod\_param = 88 e 89;
- Ramo de atividade parametrizado na tabela prt\_pfj\_msaf com o campo cod\_param <> 97\.

__Sem Cálculo:__

Campo\_21 := 0;

Campo\_22 := 0 Campo\_19;

Campo\_23 := 0;

1. *Álcool Anidro Importado*

- Recupera os produtos parametrizados na tabela x96\_grp\_comb\_prod com código oficial campo cod\_prod\_oficial = 99610;
- CFOP parametrizados na tabela prt\_cfo\_msaf ou prt\_extcfo\_msaf com o tipo de movimento campo cod\_param = 89;
- Ramo de atividade parametrizado na tabela prt\_pfj\_msaf com o campo cod\_param = 97\.

__Sem Cálculo:__

Campo\_21 := 0;

Campo\_22 := 0;

Campo\_23 := 0;

1. *Gasolina A, Gasolina A Premium 62Y, DSL – Óleo Diesel A \(Sem Adição de B100\), DSL – Óleo Diesel A S10*

- Recupera os produtos parametrizados na tabela x96\_grp\_comb\_prod com código oficial campo cod\_prod\_oficial = 62006, 62448, 64300 e 64301;
- CFOP parametrizados na tabela prt\_cfo\_msaf ou prt\_extcfo\_msaf com o tipo de movimento campo cod\_param = 89;
- Ramo de atividade parametrizado na tabela prt\_pfj\_msaf com o campo cod\_param = 94\.

__Sem Cálculo:__

Campo\_21 := 1

Campo\_22 := vlr\_base\_icmss\_3 da tabela dwt\_itens\_merc \(campo 61 SAFX08 quando campo 94 = 3\);

Campo\_23 := vlr\_tributo\_icmss da tabela dwt\_itens\_merc \(campo 52 SAFX08\)\.

1. *Biodiesel B100, Biodiesel B100 Importado, Álcool Anidro, Álcool Anidro Importado*

- Recupera os produtos parametrizados na tabela x96\_grp\_comb\_prod com código oficial campo cod\_prod\_oficial = 64432, 64433, 99600 e 99610;
- CFOP parametrizados na tabela prt\_cfo\_msaf ou prt\_extcfo\_msaf com o tipo de movimento campo cod\_param = 688;
- Ramo de atividade parametrizado na tabela prt\_pfj\_msaf com o campo cod\_param = 104 e 107\.

__Sem Cálculo:__

Campo\_21 := 0;

Campo\_22 := 0 Campo\_19;

Campo\_23 := 0;

1. *Regra específica para os CFOP: 1949 – Ganhos e 5927 – Perdas*

- Recupera todos os produtos parametrizados na tabela x96\_grp\_comb\_prod e com esses CFOP parametrizados na tabela prt\_cfo\_msaf ou prt\_extcfo\_msaf com qualquer tipo de movimento informado no campo cod\_param;
- Ramo de atividade parametrizado na tabela prt\_pfj\_msaf com o campo cod\_param = 104\.

__Sem Cálculo:__

Campo\_21 := 0;

Campo\_22 := 0;

Campo\_23 := 0;

__2ª Etapa: __Haverá cálculo das informações\.

1. *Produtos diferentes de Biodiesel B100, Biodiesel B100 Importado, Álcool Anidro, Álcool Anidro Importado*

- Recupera os produtos parametrizados na tabela x96\_grp\_comb\_prod com código oficial campo cod\_prod\_oficial <> 64432, 64433, 99600 e 99610;
- CFOP parametrizados na tabela prt\_cfo\_msaf ou prt\_extcfo\_msaf com o tipo de movimento campo cod\_param = 88 e 89;
- Ramo de atividade parametrizado na tabela prt\_pfj\_msaf com o campo cod\_param = 104\.

__Cálculo:__

Campo\_21 := 0

Campo\_22 :=  Se os produtos parametrizados na tabela x96\_grp\_comb\_prod com código oficial campo cod\_prod\_oficial = 64300, 64301, 62006, 62448, 66575, 65583, 66591, 66605, 66621, 66630, 66648, efetuar o seguinte cálculo:

\(\(\(\(campo vlr\_regra\_base\_st \(PMPF, MVA, ANP\) da tabela cbt\_base\_st\_grp\_uf \(SAFX111\) / campo fator\_div\_gas\_a da tabela x96\_grp\_comb\_prod \(SAFX96\)\) \* campo quantidade da tabela dwt\_itens\_merc \(SAFX08\)\) \* 100,000000 \- campo vlr\_regr\_reducao\_base da tabela cbt\_base\_st\_grp\_uf \(SAFX111\)\) / 100\);

Senão

\(\(\(\(campo vlr\_regra\_base\_st \(PMPF, MVA, ANP\) da tabela cbt\_base\_st\_grp\_uf \(SAFX111\)\) \* campo quantidade da tabela dwt\_itens\_merc \(SAFX08\)\) \* 100,000000 \- campo vlr\_regr\_reducao\_base da tabela cbt\_base\_st\_grp\_uf \(SAFX111\)\) / 100\);

__\[MFS\-75599\]__

Cod\_param = 89 \(NF Entradas\):

Campo\_23 := \(\(\(Campo\_22 \* campo aliq\_interna da tabela cbt\_aliq\_grp\_uf\) / 100,2\) \+ campo vlr\_tributo\_icms da tabela dwt\_itens\_merc \(SAFX08\)\);

Cod\_param = 88 \(NF Sáidas\):

Campo\_23 := 0;

__*Obs\.:*__* Conforme orientação do Manual de Orientação \- SCANC CTB \- Versão do Manual 3\.0\.9\.0 \(16/07/2021\), o Campo 23 \- Valor do ICMS\-ST Valores referente ao ICMS\-ST\. Informar somente para as Notas Fiscais de Entrada de combustíveis derivados de petróleo*

__\[INCLUSÃO DE REGRA \- CH 18317\_2020 \(MFS\-46986\)\]__

1. *Gasolina A, Gasolina A Premium 62Y, DSL – Óleo Diesel A \(Sem Adição de B100\), DSL – Óleo Diesel A S10*

- Recupera os produtos parametrizados na tabela x96\_grp\_comb\_prod com código oficial campo cod\_prod\_oficial = 62006, 62448, 64300 e 64301;
- CFOP parametrizados na tabela prt\_cfo\_msaf ou prt\_extcfo\_msaf com o tipo de movimento campo cod\_param = 89;
- Deverá ser considerada a data da importação da nota fiscal para recuperar os registros, campo dat\_di da tabela dwt\_docto\_fiscal;
- Ramo de atividade parametrizado na tabela prt\_pfj\_msaf com o campo cod\_param = 97;
- Nota Fiscal com destaque do ICMS do imposto \(Nota Fiscal COM RETENÇÃO do imposto\) = Campo IND\_CRED\_ICMSS da tabela DWT\_ITENS\_MERC = ‘S’ \(Campo 78 da SAFX08\)  
 

__Cálculo:__

Campo\_21 := 1

Campo\_22 := \(\(\(\(\(campo vlr\_regra\_base\_st \(PMPF, MVA, ANP\) da tabela cbt\_base\_st\_grp\_uf \(SAFX111\) / campo fator\_div\_gas\_a da tabela x96\_grp\_comb\_prod \(SAFX96\)\) / campo fator\_conv\_volume da tabela x96\_grp\_comb\_prod \(SAFX96\)\) \* campo quantidade da tabela dwt\_itens\_merc \(SAFX08\)\) \* 100,000000 \- campo vlr\_regr\_reducao\_base da tabela cbt\_base\_st\_grp\_uf \(SAFX111\)\) / 100\);

*Observação: Nessa regra de cálculo o fator de divisão do valor unitário também é considerado, assim como, o FCV, este só deve ser calculado para as importadoras\.*

Campo\_23 := \(\(\(Campo\_22 \* campo aliq\_interna da tabela cbt\_aliq\_grp\_uf\) / 100,2\) \+ campo vlr\_tributo\_icms da tabela dwt\_itens\_merc \(SAFX08\)\);

1. *BXD, Gasolina C, Gasolina C Aditivada, Gasolina C Premium*

- Recupera os produtos parametrizados na tabela x96\_grp\_comb\_prod com código oficial campo cod\_prod\_oficial = 64491, 64483, 64475, 64440, 62154, 62155, 62456;
- CFOP parametrizados na tabela prt\_cfo\_msaf ou prt\_extcfo\_msaf com o tipo de movimento campo cod\_param = 90;
- Ramo de atividade parametrizado na tabela prt\_pfj\_msaf com o campo cod\_param = 103, 105 e 106\.

__Cálculo:__

Campo\_21 := 0

Campo\_22 := \(\(\(\(campo vlr\_regra\_base\_st \(PMPF, MVA, ANP\) da tabela cbt\_base\_st\_grp\_uf \(SAFX111\)\) \* campo quantidade da tabela dwt\_itens\_merc \(SAFX08\)\) \* 100,000000 \- campo vlr\_regr\_reducao\_base da tabela cbt\_base\_st\_grp\_uf \(SAFX111\)\) / 100\);

Campo\_23 := \(\(\(Campo\_22 \* campo aliq\_interna da tabela cbt\_aliq\_grp\_uf\) / 100,2\) \+ campo vlr\_tributo\_icms da tabela dwt\_itens\_merc \(SAFX08\)\);

__\[ALTERADA – CH10314\_2018 \(MFS\-18719\)\]__

1. *BXD, Gasolina C, Gasolina C Aditivada, Gasolina C Premium*

- Recupera os produtos parametrizados na tabela x96\_grp\_comb\_prod com código oficial campo cod\_prod\_oficial = 64491, 64483, 64475, 64440, 62154, 62155 e 62456;
- CFOP parametrizados na tabela prt\_cfo\_msaf ou prt\_extcfo\_msaf com o tipo de movimento campo cod\_param = 88 e campo ind\_destinacao <> 2;
- Ramo de atividade parametrizado na tabela prt\_pfj\_msaf com o campo cod\_param = 103, 105, 106 e 107\.

__Cálculo:__

Campo\_21 := 0

Campo\_22 := \(\(\(\(campo vlr\_regra\_base\_st \(PMPF, MVA, ANP\) da tabela cbt\_base\_st\_grp\_uf \(SAFX111\)\) \* campo quantidade da tabela dwt\_itens\_merc \(SAFX08\)\) \* 100,000000 \- campo vlr\_regr\_reducao\_base da tabela cbt\_base\_st\_grp\_uf \(SAFX111\)\) / 100\);\]

__\[MFS\-75599\]__

Cod\_param = 88 \(NF Sáidas\):

Campo\_23 := 0;

__*Obs\.:*__* Conforme orientação do Manual de Orientação \- SCANC CTB \- Versão do Manual 3\.0\.9\.0 \(16/07/2021\), o Campo 23 \- Valor do ICMS\-ST Valores referente ao ICMS\-ST\. Informar somente para as Notas Fiscais de Entrada de combustíveis derivados de petróleo*

Campo\_23 := \(\(\(Campo\_22 \* campo aliq\_interna da tabela cbt\_aliq\_grp\_uf\) / 100,2\) \+ campo vlr\_tributo\_icms da tabela dwt\_itens\_merc \(SAFX08\)\);

1. *Gasolina A, Gasolina A Premium 62Y, DSL – Óleo Diesel A \(Sem Adição de B100\), DSL – Óleo Diesel A S10*

- Recupera os produtos parametrizados na tabela x96\_grp\_comb\_prod com código oficial campo cod\_prod\_oficial = 62006, 62448, 64300 e 64301;
- CFOP parametrizados na tabela prt\_cfo\_msaf ou prt\_extcfo\_msaf com o tipo de movimento campo cod\_param = 88 e campo ind\_destinacao = nulo/branco;
- Ramo de atividade parametrizado na tabela prt\_pfj\_msaf com o campo cod\_param = 104\.

__Cálculo:__

Campo\_21 := 0

Campo\_22 := \(\(\(\(campo vlr\_regra\_base\_st \(PMPF, MVA, ANP\) da tabela cbt\_base\_st\_grp\_uf \(SAFX111\) / campo fator\_div\_gas\_a da tabela x96\_grp\_comb\_prod \(SAFX96\)\) \* campo quantidade da tabela dwt\_itens\_merc \(SAFX08\)\) \* 100,000000 \- campo vlr\_regr\_reducao\_base da tabela cbt\_base\_st\_grp\_uf \(SAFX111\)\) / 100\);

__\[MFS\-75599\]__

Cod\_param = 88 \(NF Sáidas\):

Campo\_23 := 0;

Campo\_23 := \(\(\(Campo\_22 \* campo aliq\_interna da tabela cbt\_aliq\_grp\_uf\) / 100,2\) \+ campo vlr\_tributo\_icms da tabela dwt\_itens\_merc \(SAFX08\)\);

__*Obs\.:*__* Conforme orientação do Manual de Orientação \- SCANC CTB \- Versão do Manual 3\.0\.9\.0 \(16/07/2021\), o Campo 23 \- Valor do ICMS\-ST Valores referente ao ICMS\-ST\. Informar somente para as Notas Fiscais de Entrada de combustíveis derivados de petróleo*

1. *BXD, Gasolina C, Gasolina C Aditivada, Gasolina C Premium*

Recupera os produtos parametrizados na tabela x96\_grp\_comb\_prod com código oficial campo cod\_prod\_oficial = 64491, 64483, 64475, 64440, 62154, 62155 e 62456;

- CFOP parametrizados na tabela prt\_cfo\_msaf ou prt\_extcfo\_msaf com o tipo de movimento campo cod\_param = 687;
- Ramo de atividade parametrizado na tabela prt\_pfj\_msaf com o campo cod\_param = 104 e 105\.

__Cálculo:__

Campo\_21 := 0

Campo\_22 := \(\(\(\(campo vlr\_regra\_base\_st \(PMPF, MVA, ANP\) da tabela cbt\_base\_st\_grp\_uf \(SAFX111\)\) \* campo quantidade da tabela dwt\_itens\_merc \(SAFX08\)\) \* 100,000000 \- campo vlr\_regr\_reducao\_base da tabela cbt\_base\_st\_grp\_uf \(SAFX111\)\) / 100\);

Campo\_23 := \(\(\(Campo\_22 \* campo aliq\_interna da tabela cbt\_aliq\_grp\_uf\) / 100,2\) \+ campo vlr\_tributo\_icms da tabela dwt\_itens\_merc \(SAFX08\)\);

1. *Produtos diferentes de Biodiesel B100, Biodiesel B100 Importado, Álcool Anidro, Álcool Anidro Importado*

- Recupera os produtos parametrizados na tabela x96\_grp\_comb\_prod com código oficial campo cod\_prod\_oficial <> 64432, 64433, 99600 e 99610;
- CFOP parametrizados na tabela prt\_cfo\_msaf ou prt\_extcfo\_msaf com o tipo de movimento campo cod\_param = 688;
- Ramo de atividade parametrizado na tabela prt\_pfj\_msaf com o campo cod\_param = 104\.

__Cálculo:__

Campo\_21 := 0

Campo\_22 :=  Se os produtos parametrizados na tabela x96\_grp\_comb\_prod com código oficial campo cod\_prod\_oficial = 64300, 64301, 62006, 62448, 66575, 65583, 66591, 66605, 66621, 66630, 66648, efetuar o seguinte cálculo:

\(\(\(\(campo vlr\_regra\_base\_st \(PMPF, MVA, ANP\) da tabela cbt\_base\_st\_grp\_uf \(SAFX111\) / campo fator\_div\_gas\_a da tabela x96\_grp\_comb\_prod \(SAFX96\)\) \* campo quantidade da tabela dwt\_itens\_merc \(SAFX08\)\) \* 100,000000 \- campo vlr\_regr\_reducao\_base da tabela cbt\_base\_st\_grp\_uf \(SAFX111\)\) / 100\);

Senão

\(\(\(\(campo vlr\_regra\_base\_st \(PMPF, MVA, ANP\) da tabela cbt\_base\_st\_grp\_uf \(SAFX111\)\) \* campo quantidade da tabela dwt\_itens\_merc \(SAFX08\)\) \* 100,000000 \- campo vlr\_regr\_reducao\_base da tabela cbt\_base\_st\_grp\_uf \(SAFX111\)\) / 100\);

Campo\_23 := \(\(\(Campo\_22 \* campo aliq\_interna da tabela cbt\_aliq\_grp\_uf\) / 100,2\) \+ campo vlr\_tributo\_icms da tabela dwt\_itens\_merc \(SAFX08\)\);

__\[NOVA REGRA \- CH 18317\_2020 \(MFS\-46986\)\]__

1. *Regra específica para o Registro 40 – Campo 21 – Para Tipo de Ramo de Atividade 97 \- Importador*

- CFOP parametrizados na tabela prt\_cfo\_msaf ou prt\_extcfo\_msaf com o tipo de movimento campo cod\_param = 89;
- Ramo de atividade parametrizado na tabela prt\_pfj\_msaf com o campo cod\_param = 97\.
- Verificar a NF se não houve destaque do imposto, conforme: Campo IND\_CRED\_ICMSS da tabela DWT\_ITENS\_MERC = ‘N’ \(Campo 78 da SAFX08\)\.

__Sem Cálculo:__

Campo\_21 := 0;

Campo\_22 := vlr\_base\_icmss\_1 da tabela dwt\_itens\_merc \(campo 61 SAFX08 quando campo 94 = “1”\);

Campo\_23 := vlr\_tributo\_icmss da tabela dwt\_itens\_merc \(campo 52 SAFX08\)\.

\[__ALTERAÇÃO\- MFS\-74142__\] Tratamento p/ parâmetro 89 \(Aquisições e Transferências\), produtos derivados de Petróleo\.

1. *BXD, Gasolina A, B e C, Gasolina C Aditivada, Gasolina A e C Premium e Óleo Diesel\.*

- Recupera os produtos parametrizados na tabela x96\_grp\_comb\_prod com código oficial campo cod\_prod\_oficial = 62006, 62103, 62154, 62155, 62448, 62456, 64300 e 64301, 64440, 64475, 64483, 64491, 64483, 64475, 64440;
- CFOP parametrizados na tabela prt\_cfo\_msaf ou prt\_extcfo\_msaf com o tipo de movimento campo cod\_param = 89;
- Ramo de atividade parametrizado na tabela prt\_pfj\_msaf com o campo cod\_param = 105, 106 e 107\.

__Cálculo:__

Campo\_21 := 0

Campo\_22 := \(\(\(\(campo vlr\_regra\_base\_st \(PMPF, MVA, ANP\) da tabela cbt\_base\_st\_grp\_uf \(SAFX111\)\) \* campo quantidade da tabela dwt\_itens\_merc \(SAFX08\)\) \* 100,000000 \- campo vlr\_regr\_reducao\_base da tabela cbt\_base\_st\_grp\_uf \(SAFX111\)\) / 100\);

Campo\_23 := \(\(\(Campo\_22 \* campo aliq\_interna da tabela cbt\_aliq\_grp\_uf\) / 100,2\) \+ campo vlr\_tributo\_icms da tabela dwt\_itens\_merc \(SAFX08\)\);

__\[ALTERADA – MFS\-16400\]__

__*Tratamentos importantes no cálculo:*__* *

- *Usar regra de arredondamento para o vlr\_regra\_base\_st dividido pelo fator\_div\_gas\_a da tabela x96\_grp\_comb\_prod \(SAFX96\), o resultado deve considerar até 4 casas decimais a mesma coisa serve para o fator\_conv\_volume “FCV” \(SAFX96\);*
- *As notas de transferência deverão considerar o cálculo com a pauta levando em consideração a data de emissão;*
- *Na regra de cálculo o fator de divisão do valor unitário é considerado apenas no cálculo para produtos A\. O cálculo da redução da base deve ser feito de forma que corresponda à redução do percentual parametrizado, então vai ser calculado com a diferença de 100,000000 ou da forma que seja melhor ser implementado;*

*\-     A alíquota interna deve ter sua data de validade compreendida no período de geração\.*

__*Tratamentos importantes na recuperação das notas fiscais considerando a parametrização do tipo de operação:*__* *

- *As notas fiscais de devolução emitida em período de vigência de Pauta diferente da vigência da Pauta da nota fiscal de venda original deve respeitar a Pauta da Vigência da nota fiscal de venda e não da nota fiscal de devolução\. Então deverá conter na nota fiscal de devolução o número da nota fiscal de venda no campo 16\-NUM\_DOCFIS\_REF da SAFX07 e o campo 75\-DAT\_DI da SAFX07;*
- *As notas fiscais de empréstimo deverão ser contempladas no SCANC se a devolução total \(Item/Quantidade\) não ocorrer dentro do mês, ou seja, caso haja saldo em aberto na operação, deverá ser contemplada no arquivo\.*
- *Considerar as notas fiscais para importadora quando o campo 75\-DAT\_DI estiver preenchido\.*

MFS\-11111

CH22610\_2017 \(MFS\-14934\)

MFS\-16400

CH10314\_2018 \(MFS\-18719\)

MFS\-46986

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN


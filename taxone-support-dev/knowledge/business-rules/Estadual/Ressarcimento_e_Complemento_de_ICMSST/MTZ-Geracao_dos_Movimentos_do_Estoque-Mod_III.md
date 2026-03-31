# MTZ-Geracao_dos_Movimentos_do_Estoque-Mod_III

- **Fonte:** MTZ-Geracao_dos_Movimentos_do_Estoque-Mod_III.docx
- **Modificado:** 2023-10-11
- **Tamanho:** 40 KB

---

Ressarcimento e Complemento do ICMS\-ST 

 Geração dos Movimentos do Estoque do Modelo III

Localização: Menu Estadual, Módulo: Ressarcimento e Complemento de ICMS\-ST,  item Obrigações 🡪 CAT 17/1999 🡪 Geração Movimentos do Estoque

*\(este item de menu foi alterado devido à reorganização dos menus do módulo Ressarc/Compl\. feito na OS2925\-E\)*

Localização: Menu Estadual, Módulo: Ressarcimento e Complemento de ICMS\-ST,  item Obrigações 🡪 CAT 17/1999 🡪 Modelo III \(Mercadorias\) 🡪 Geração Movimentos do Estoque

Revisões e Documentos de Requisito

__Data__

__DR__

__Descrição __

__Resp__

19/01/2011

__\-\-\-__

Criação do documento para registrar as regras bascas da geração dos movimentos do estoque da CAT 17 a partir das notas fiscais\.

Vânia Dias Mattos

16/05/2011

__OS3157\-D__

Alteração no preenchimento do campo “37\-BC Operação Própria” da SAFX27

Vânia Dias Mattos

06/06/2011

__OS2732__

Alteração da regra RN00 para recuperar o Produto\.

Juliana Garcia

19/06/2012

__OS2925\-E__

Reorganização dos menus da CAT17/1999

Vânia Dias Mattos

29/12/2014

__OS4699__

Alteração no preenchimento das colunas 24 e 25 da SAFX27 quando se tratar de saída com isenção ou não incidência \(col 12 do Modelo III\)

\(ver RN24 e RN25\)

Vânia Dias Mattos

08/10/2015

__CH17035\_2015__

Alteração da regra RN00 para recuperar o Produto\.

Julyana Perrucini

03/12/2015

__CH26159\_2015__

Automação do lançamento do Valor de ICMS Retido\.

Julyana Perrucini

####  

\(as regras da geração da SAFX27 a partir dos cupons fiscais ainda não consta deste docto\)

   

Regras da Geração a partir das NF’s \(SAFX07/SAFX08\)

__Parâmetros de Tela__

__UF__ – Este campo é uma lista das UF’s da tabela Estados\. No campo “Estabelecimentos” serão exibidos apenas os estabelecimentos da UF informada;

__Período__ – Neste campo o usuário informará a data inicial e final que serão utilizadas na recuperação das notas fiscais;

 

__Origem dos Dados__ – Processa as Notas __ou__ Notas \+ Cupons Fiscais 

__Utiliza Base Retenção na Origem__ – Parâmetro \(S/N\) utilizado no preenchimento do campo “16*\-Valor Total da Base de Cálculo da Retenção*”, conforme descrito na __RN16__\. Na abertura da tela, default = desmarcado;

__\[ALTERADA – CH26159\_2015\]__

__Utiliza Retenção na Origem__ – Parâmetro \(S/N\) utilizado no preenchimento do campo “30 *\-* *Valor ICMS Retido*”, conforme descrito na __RN38__\. Na abertura da tela, default = desmarcado;

Gerar Dados de Veículos e Motos – Se marcado, serão considerados também os movimentos dos produtos parametrizados p/a apuração específica de Veículos e Motos \(Modelo II e Modelo IV\); 

__Alteração da OS2925\-E__: Este parâmetro foi retirado da tela porque os menus do módulo foram reorganizados, e passaram a existir menus separados da geração dos movimentos, um p/o Mod\. III e outro p/o Mod IV\.  

* *

__Considerar Desconto na BC na Saída a Consumidor__ – Parâmetro utilizado no preenchimento do campo “24*\-Base de Cálculo Efetiva na Saída a Consumidor ou Usuário Fina – Valor de Confronto”,* conforme descrito na __RN24__\. 

__RN00 – Regras Gerais __

Esta rotina é responsável pela geração dos dados da SAFX27, a partir das notas fiscais do período \(SAFX07 e SAFX08\) e também dos documentos de ECF \(ainda utiliza a modelagem “antiga”\)\.

Critérios para recuperação das notas na SAFX07/SAFX08:

- Notas do período solicitado em tela
- Notas não canceladas
- Somente notas com itens
- O produto deve constar da parametrização dos Produtos por UF \(opção “Parâmetros 🡪 CAT 17/1999 🡪 Produto por UF”, seja como “produto principal” ou “produto associado”\), considerando a UF do seu estabelecimento e data de vigência estiver no período da geração, ou seja, o campo data início de vigência ser <= data final de vigência e data final de vigência is null ou >= data final de vigência\. 
	- __\[ALTERADA – CH17035\_2015\] Tratamento: __Se existir o mesmo produto cadastrado e não estiver com o campo data final de vigência preenchido, buscar o produto de maior validade inicial, ou seja, de maior data inicial de vigência e emitir a mensagem no log de processo da geração dos movimentos de estoque modelo III como Atenção e descrevendo\-a na coluna Mensagem de Erro: “O produto <<XXXXX>> está duplicado na parametrização Produto por UF e será considerado na geração o produto de maior validade inicial”\.
- O CFOP e/ou Natureza deve constar da parametrização de  CFOP/Natureza p/o Modelo III \(opção “Parâmetros 🡪 CAT 17/1999 🡪 CFOP/Natureza p/o Modelo III”\) para algum dos seguintes códigos de parâmetros:

__Param__

__Descrição__

342

Valor Total BC da Retenção – Entradas

343

Valor Total BC da Retenção – Entradas \(Devolução\)

344

Saída a Consumidor ou Usuário Final

345

Saída a Consumidor ou Usuário Final \(Devolução\)

346

Fato Gerador Não Realizado

347

Fato Gerador Não Realizado \(Devolução\)

348

Saída com Isenção ou Não Incidência

349

Saída com Isenção ou Não Incidência \(Devolução\)

350

Saída para Outro Estado

351

Saída para Outro Estado \(Devolução\)

352

Saída para Comercialização Subseqüente

353

Saída para Comercialização Subseqüente \(Devolução\)

Para cada item da SAFX08 é gravado um registro na SAFX27\. As regras de gravação de cada campo estão descritas nas “RN” abaixo\.

Obs 1: Sobre as Operações de Devolução:

As operações de devolução devem ser parametrizadas corretamente, para que os valores sejam lançados nas mesmas colunas das operações originais, mas negativas, para que haja a dedução dos valores\.

Obs 2: Geração de Movimentos de Estoque:

Alterar a Geração de Movimentos do Estoque, tratando a vigência das parametrizações existentes nas tabelas dos parâmetros de produto por UF\. Esta rotina de geração possui uma verificação nas tabelas ESP\_SP\_PROD\_ST e ESP\_SP\_PROD\_ST\_ASS, onde o produto da nota fiscal recuperada nas tabelas SAFX07 e SAFX08 é confrontado com os produtos parametrizados\. Esta verificação deve ser ajustada para que sejam consideradas as datas de início e fim de vigência dos produtos parametrizados\.

__RN13 \- Campo Número do Equipamento  __

Este campo não é preenchido no caso das notas da SAFX08\.

\(só é utilizado quando a origem da informação for ECF\)

__RN14 – Código do CFOP  __

__RN15 \- Código Complementar da Operação  __

Este campo é gerado a partir da parametrização de Natureza de Operação do módulo CAT17 \(menu Parâmetros 🡪 CAT 17/1999 🡪 Cód\. Complementar p/ CFOP/Nat\), da seguinte forma:

Se  Natureza <> nulo                                                                                                                                                                              

       Verifica se o CFOP/NAT consta na parametrização

      Se  sim

             Grava o código complementar parametrizado 

      Senão

             Grava  “00”

Senão

       Grava  “00”

\(tabela da parametrização: ESP\_SP\_COMPL\_ST\)

__RN16 \- Valor Total da Base de Cálculo da Retenção __

Preenchido originalmente apenas nas operações de entrada

Conteúdo 🡪 BC do ICMS\-ST  \(campo 61\) da SAFX08

__Alteração da OS1165 \(Set/2003\)__:

A geração passou a trabalhar com o seguinte parâmetro de tela: “Utiliza Base Retenção na Origem” \(default = não\):

Se  “Utiliza Base Retenção na Origem” = N

      Preenche com a BC do ICMS\-ST \(campo 61\)

Senão 

      Preenche com a BC do ICMS\-ST \(campo 61\) e 

       BC Carga Tributária Origem \(campo 106\),

       quando estiverem preenchidos;

=  fim alteração OS1165 =

__Alteração OS3157\-B \(Jan/2011\) \(tratamento das devoluções\)__:

O preenchimento deste campo passou a ter um tratamento diferenciado no caso das notas de devolução:

*\(ver orientações de preenchimento do campo no Manual de Layout\)*

 

Notas de entrada de devolução de vendas 🡪 São as notas de entrada parametrizadas como devolução para os seguintes parâmetros:

\-Saída a Consumidor ou Usuário Final        \(Dev\. de Vendas\) 

\-Fato Gerador Não Realizado                      \(Dev\. de Vendas\)

\-Saída com Isenção ou Não Incidência        \(Dev\. de Vendas\)

\-Saída p/ Outros Estados                              \(Dev\. de Vendas\)

\-Saída para Comercialização Subseqüente \(Dev\. de Vendas\)

Neste tipo de nota o campo *não* será ser preenchido\.

Notas de saída de devolução de compras 🡪 São as notas de saída parametrizadas como devolução para o seguinte parâmetro:

\-Valor Total BC da Retenção \- Entrada \(Dev\. de Compras\)  

Neste tipo de nota o campo passou a ser preenchido, apesar de tratar\-se de uma saída\. O valor é carregado *com sinal negativo*, por se tratar de uma devolução\. 

*\(este mesmo procedimento é feito nas notas de  entrada de devolução para o preenchimento dos campos 19 a 23\)*

=  fim alteração OS3157\-B

__RN17 – Quantidade Entrada / Saída \(QTD\_E\_S\) __

__Conteúdo original 🡪 __ campo “24\-Quantidade” da SAFX08;

__Alteração feita p/ Carrefour:  \(OS1585\-D, Dez/2004\)__

Se campo “137\-Quantidade Convertida” > zero 

      Usa o campo “137\-Quantidade Convertida”  \(\*\*\*\);

Senão

      Usa o campo “24\-Quantidade”;

\(\*\*\*\) A orientação do Manual de Layout é que este campo seja utilizado somente nas notas de entrada, para informar a quantidade já convertida, nos casos em que a unidade de medida da nota for diferente da unidade de medida padrão em que o produto é comercializado\.

__Alteração feita p/ Chevron:  \(OS1585\-G, Dez/2004\)__

 

Se o produto da nota constar na parametrização do menu “*Percentual de Composição de Produtos Sujeitos a ST”, * a quantidade a ser gravada será proporcional ao percentual informado, ou seja:

                                                             Quantidade = Quantidade \* Perc / 100

__RN18 – Valor Unitário \- Saídas __

Este campo não é preenchido na geração dos movimentos, e será atualizado somente na rotina do “Cálculo dos Saldos do Estoque”\.

__RN19 – Saídas para Consumidor ou Usuário Final __

Este campo não é preenchido na geração dos movimentos, e será atualizado somente na rotina do “Cálculo dos Saldos do Estoque”\.

__RN20 – Fato Gerador Não Realizado __

Este campo não é preenchido na geração dos movimentos, e será atualizado somente na rotina do “Cálculo dos Saldos do Estoque”\.

__RN21 – Saída com Isenção ou Não Incidência __

Este campo não é preenchido na geração dos movimentos, e será atualizado somente na rotina do “Cálculo dos Saldos do Estoque”\.

__RN22 – Saída para Outro Estado __

Este campo não é preenchido na geração dos movimentos, e será atualizado somente na rotina do “Cálculo dos Saldos do Estoque”\.

__RN23 – Saída para Comercialização Subsequente __

Este campo não é preenchido na geração dos movimentos, e será atualizado somente na rotina do “Cálculo dos Saldos do Estoque”\.

__ RN24 – Base de Cálculo Efetiva na Saída a Consumidor ou Usuário Final – VC__

Preenchida nas seguintes operações de saída:

\- Saídas a  consumidor ou usuário final 

\- Saídas a  consumidor ou usuário final \- Devoluções

\- Saídas com Isenção ou Não Incidência                          \(após alteração do CH74230/74554\)

\- Saídas com Isenção ou Não Incidência \- Devoluções

\(não necessita parametrizar CFOP para que o campo 24 da SAFX27 seja gerado, basta que a saída tenha o CFOP ou CFOP/NAT parametrizado para os tipos de saída descritos acima\)

Conteúdo original  🡪  BC do ICMS próprio

__Alteração da OS1585\-C \(Out/2004\):__

Conteúdo atual 🡪 Passou a preencher o campo com o preço do item \(campo 28\-Preço do Item da SAFX08\), ao invés da BC\.

__Alteração da ??? \(chamado não identificado\)__:

No caso das saídas a consumidor ou usuário final, o campo passou a ser preenchido apenas quando o campo “Contribuinte Final” da SAFX07 estiver = “S” \(na definição original da OS36 não existia esta condição\)\.

__Alteração da OS2871 \(Set/2009\):__

__\(criado parâmetro “Considerar Desconto”\)__

Se parâmetro “__Considerar desconto na Base de Cálculo na Saída a Consumidor”__ = “N”

      Preenche com o Valor do Item \(campo 28\-Preço do Item\);

Se parâmetro “__Considerar desconto na Base de Cálculo na Saída a Consumidor”__  = “S” 

      Preenche com o Valor do Item \- Desconto do Item; 

__Alteração do CH74230__:

O campo passou a ser preenchido também para as saídas do tipo “Saídas com Isenção ou não Incidência”\.

__Alteração da OS4699 __

__Tratamento das saídas do tipo “Saídas com isenção ou não incidência”__:

Quando se tratar das saídas do tipo “__Saídas com Isenção ou não Incidência__”, este campo será preenchido *apenas* quando o CFOP ou CFOP/Natureza parametrizado tiver o parâmetro “Valor de Confronto” = “VC na coluna 15”, ou seja:

    __Se__ CFOP ou CFOP/NAT parametrizado tiver o parâmetro “Valor de Confronto” = “VC na coluna 15” __ou__ = nulo:

          Nesse caso a coluna 24 da SAFX27 será gerada normalmente com o preço do item 

          \(conforme o funcionamento anterior à alteração da OS4699\)

    __Senão__

         Nesse caso a coluna 24 da SAFX27 *não* será preenchida;

__ RN25 – Valor Total da Base de Cálculo Efetiva da Entrada nas Demais Hipóteses – Valor de Confronto__

Campo originalmente preenchido apenas nas entradas \(com a BC ICMS próprio\), mas posteriormente foi alterado para ser preenchido *apenas* nas operações do tipo:

\-Saídas para Outros Estados                        \(__OS2738__\)

\-Saídas para Outros Estados \- Devoluções

\-Fato Gerador não Realizado                        \(__CH74554__\)

\-Fato Gerador não Realizado \- Devoluções 

\-Saídas p/Comercial\. Subseqüente                 \(__CH74554__\)

\-Saídas p/Comercial\. Subseqüente – Devoluções

\- Saídas com Isenção ou não Incidência                          \(__OS4699__\)     __\(\*\)__ 

\- Saídas com Isenção ou não Incidência – Devoluções     \(__OS4699__\)     __\(\*\)__

__\(\*\)__ As saídas com isenção ou não incidência terão a coluna 25 da SAFX27 preenchida apenas quando o CFOP ou CFOP/NAT tiver o parâmetro “Valor de Confronto” = “VC na coluna 16”\.

\(não necessita parametrizar CFOP para que o campo 25 da SAFX27 seja gerado, basta que a saída tenha o CFOP ou CFOP/NAT parametrizado para os tipos de saída descritos acima\)

Conteúdo 🡪 campo “106\-BC da Carga Tributária na Origem” da SAFX08

__Alteração da OS1585\-G \(Dez/2004\)__:

Nos movimentos parametrizados para a coluna “Saídas a Consumidor ou Usuário Final”, com CFOP 6656 ou 6659, o valor lançado na coluna  “Saídas \- Consumidor / Usuário Final” *deverá ser lançado também* nesta coluna da BC Efetiva da Entrada nas Demais Hipóteses\. \(alteração feita p/a Chevron\)

Obs: esta alteração foi feita na procedure do cálculo \(SAF\_SP\_CALC\_SALD\), mas esta comentada e sem  registro de chamado \(???\) para desfazer a alteração da OS1585\-G\.

__Alteração do OS3157\-B \(Jan/2011\):__

A partir desta OS este campo *deixou de ser preenchido* para as operações do tipo “Saídas para Comercialização Subseqüente”\.

Esclarecimentos da Informação 🡪 Este tipo de movimento não consta no Modelo I, ou seja, não interfere na apuração do Ressarcimento / Complemento do ICMS\-ST\. Sendo assim, estas operações não geram valor de confronto, e por isso, não podemos preencher o campo do valor de confronto ao trazer a nota da X07/X08 p/a X27\. Estas operações são demonstradas no Modelo III apenas para registrar a baixa do estoque\.  

__Alteração da OS4699 __

__Tratamento das saídas do tipo “Saídas com isenção ou não incidência”__:

Quando se tratar das saídas do tipo “__Saídas com Isenção ou não Incidência__”, este campo será preenchido *apenas* quando o CFOP ou CFOP/Natureza parametrizado tiver o parâmetro “Valor de Confronto” = “VC na coluna 16”, ou seja:

    __Se__ CFOP ou CFOP/NAT parametrizado tiver o parâmetro “Valor de Confronto” = “VC na coluna 16”:

          Nesse caso a coluna 25 da SAFX27 será gerada c/o conteúdo do campo “106\-BC da Carga Tribut\. Origem” da SAFX08

    __Senão__ \(se parâmetro “Valor de Confronto” = “VC na coluna 15” __ou__ = nulo\)

          Nesse caso a coluna 25 da SAFX27 *não* será preenchida;

__ RN26 – Quantidade__

Este campo não é preenchido na geração dos movimentos, e será atualizado somente na rotina do “Cálculo dos Saldos do Estoque”\.

__ RN27 – Valor Unitário__

Este campo não é preenchido na geração dos movimentos, e será atualizado somente na rotina do “Cálculo dos Saldos do Estoque”\.

__ RN28 – Valor Total__

Este campo não é preenchido na geração dos movimentos, e será atualizado somente na rotina do “Cálculo dos Saldos do Estoque”\.

__ RN35 – Modelo Livro__

Este campo será preenchido sempre com “3”, indicando tratar\-se de movimento referente ao Livro Modelo III\.

__ RN37 – Base de Cálculo Operação Própria__

Originalmente este campo era preenchido sempre com o valor da Base de Cálculo Tributada do item da nota fiscal\. 

A partir da OS3157\-D, o preenchimento do campo foi alterado da seguinte forma:

__Se__ Base de Cálculo Tributada \(Base 1\) estiver preenchida

      O campo é preenchido com o conteúdo da BC Tributada \(Base 1\)

__Senão__

      O campo é preenchido com o conteúdo da BC Outras \(Base 3\)

Obs: A geração identifica o tipo de movimento \(Modelo III ou IV\) a partir do CFOP e/ou Natureza do item da nota fiscal \(SAFX08\), que deve atender a parametrização do módulo\. 

__RN38 – Valor de ICMS Retido__

Preenchido para operações de entradas e saídas com o Conteúdo 🡪 Valor do ICMS\-ST \(campo 52\) da SAFX08

__Alteração do CH26159/2015 \(Dez/2015\)__:

A geração passou a trabalhar com o seguinte parâmetro de tela: “Utiliza Retenção na Origem” \(default = não\):

Se  “Utiliza Retenção na Origem” = N

      Preenche com o Valor do ICMS\-ST \(campo 52\)

Senão 

      Preenche com o Valor do ICMS\-ST \(campo 52\) e

       Valor Carga Tributária Origem ICMS \(campo 107\),

      quando estiverem preenchidos;

= = = = =


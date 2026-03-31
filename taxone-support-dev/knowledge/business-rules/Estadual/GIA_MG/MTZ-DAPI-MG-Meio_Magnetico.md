# MTZ-DAPI-MG-Meio_Magnetico

- **Fonte:** MTZ-DAPI-MG-Meio_Magnetico.docx
- **Modificado:** 2022-03-21
- **Tamanho:** 72 KB

---

# GIA MG – DAPI – MEIO MAGNETICO

__Módulo:__ Estadual > GIA MG

__Menu:__ Obrigações > DAPI > Meio Magnético

##### DOCUMENTO DE REQUISITO

__DR__

###### Nome

__Descrição__

__OS3706__

Atualização do Layout da DAPI – versão 7\.03\.00

Inclusão de itens no detalhamento Tipo 90 do campo “Estorno de Débitos” relativos à atividade de Comunicação e criação de campos do FEM

__CH5973\-A\_2014__

Linha Tipo 22, Detalhamento 3, Campo 90

Reversa da regra de recuperação automática do Detalhamento de Estorno de Débito – campo 90 da DAPI 1 a partir de documentos fiscais

__OS4576__

Alterações da versão 8\.00

Alterações da versão 8\.00 \(novos campos na linha 23 e inclusão da linha 36\) \(ver __RN04, RN05 e RN06__\)

__OS4662__

Linha 29, Detalhamento 10, Campo 95

Este documento tem como objetivo alterar a geração da linha 29/ Campo 95\.

__CH27262\_2014__

Linha 27, Detalhamento 08, Campo 70

Linha 22, Detalhamento 03, campo 90

Este documento tem como objetivo alterar o campo de Motivo do Campo 70 e do Campo 90 do Detalhamento\.

__CH2492\_2015__

Linha Tipo 00 – Identificação da DAPI

Este documento tem como objetivo alterar a geração do campo “DAPI com movimento \[S/N\]” quando houver apenas valores de Saldo Credor \(do período anterior e seguinte\), considerando como sem movimento no arquivo magnético\.

__CH26067\_2015__

Linha Tipo 00 – Identificação da DAPI

Este documento tem como objetivo alterar a geração do campo “DAPI com movimento \[S/N\]”\.

__MFS7299__

Atualização da DAPI\-MG para a versão 8\.02

Atualizações da nova versão 8\.02 \(ver __RN01, RN03, RN04 e RN10__\)\.

__MFS\-18544__

Atualização da DAPI\-MG para a versão 9\.00\.00

Atualizações da nova versão 9\.00\.00 \(ver __RN09__\)\. 

__CH11240\_2018 \(MFS\-18927\)__

Linha Tipo 00 – Identificação da DAPI

Ajuste no campo Termo de Aceite das Informações da Declaração e do Contribuinte \(Geração da Linha Tipo 00 \- Identificação da DAPI\) \(ver __RN09__\)\.

__CH11086\_2018 \(MFS\-19044\)__

Linha Tipo 10

Ajuste na Linha Tipo 10 para inclusão da geração da identificação das linhas 130 a 133\.

__MFS27892__

Atualização da DAPI\-MG para a versão 9\.01\.00

Atualizações da nova versão 9\.01\.00\.

__MFS33913__

Atualização da DAPI\-MG para a versão 9\.02\.00

Atualizações da nova versão 9\.02\.00\.

__MFS38330__

Atualização Legal – versão 9\.03\.00

Na vrs 9\.03\.00, os campos 115 e 116 \(Anexo XI\) foram retirados do layout \(ver __RN18__\)

__MFS39540__

Campo IE Remetente, linha tipo 24

Alterou o preenchimento do campo “Inscrição Estadual do Remetente” para completar com brancos à esquerda, quando necessário, ao invés de zeros, conforme regra anterior\. Ver __RN13__\.

MFS48473

Linha 29 gerando erro no validador

Alteração na regra de preenchimento da linha 29\. Ver __RN07__

MFS80115

Campo 98 – Linha 34 e 35 \- Detalhamento

Alteração na regra de preenchimento do Campo 98 – Linha 34 e Linha 35 do Campo Valor da Operação\. Ver __RN16__ e __RN17\.__

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Descrição da Regra de Negócio 00

__OSNNNN__

__RN01__

###### Geração do Anexo VII – ICMS – Substituto Tributário 

__\- Campo 77\.1 – Outros Débitos de ST:       __\(__MFS7299__: campo criado p/a versão “802”\)

Este campo será preenchido com zeros para períodos anteriores à 09/2016\. 

A partir de 09/2016 \(vrs 8\.02\), será preenchido com a informação do campo \[77\.1\], gerado previamente na rotina da Geração dos Registros e/ou Manutenção dos Anexos\.

Linha Tipo 10, identificação da linha = __126__, identificação da coluna será preenchida com “zeros”\.

__\- Campo 081 – Saldo Credor ST p/o Período Seguinte:    __\(__MFS7299__: alterada a totalização deste campo para inclusão do campo 77\.1\)

Este campo é preenchido com o resultado da totalização dos débitos e créditos deste Anexo, conforme definido no documento de regras da rotina “Geração dos Totalizadores” \(ver “MTZ\-DAPI\-MG\-Geracao\-dos\-Totalizadores”, regra RN03\)\.

__\- Campo 082 – ICMS Subst\. Tributária a Recolher:            __\(__MFS7299__: alterada a totalização deste campo para inclusão do campo 77\.1\)

Este campo é preenchido com o resultado da totalização dos débitos e créditos deste Anexo, conforme definido no documento de regras da rotina “Geração dos Totalizadores” \(ver “MTZ\-DAPI\-MG\-Geracao\-dos\-Totalizadores”, regra RN03\)\.

__\- Campo 82\.1 – Estorno Devido ao FEM:       __\(__MFS7299__: campo criado p/a versão “802”\)

Este campo será preenchido com zeros para períodos anteriores à 09/2016\. 

A partir de 09/2016 \(vrs 8\.02\), será preenchido com a informação do campo \[82\.1\], informado na Manutenção dos Anexos \(este campo *não* tem geração automática\)\.

Linha Tipo 10, identificação da linha = __119__, identificação da coluna será preenchida com “zeros”\.

__\- Campo 082\.1 082\.2  – Fundo de Errad\. da Miséria – FEM:      __\(campo criado na OS3706\)

__                                                                                                          __\(__MFS7299__: este campo foi renumerado de 82\.1 para 82\.2\)

Este campo será preenchido com a informação do campo \[82\.1\] \[82\.2\], informado na Manutenção dos Anexos \(este campo *não* tem geração automática\)\.

Linha Tipo 10, identificação da linha = __119__ __128__, identificação da coluna será preenchida com “zeros”\.

 *\(*__*MFS7299*__* \- a identificação da linha foi alterada devido ao campo ter sido renumerado de 82\.1 para 82\.2\)\.*

No campo de valor, deverá ter tamanhos 15 \(quinze\), utilizando o caracter “0” \(zero\), alinhado à esquerda, para preenchimento\. Deverá conter apenas caracteres numéricos, suprimindo pontos e vírgulas\. Ex: R$1\.000,50; formatando: 000000000100050\.

Em caso de não possuir valor, preencher com zeros\.

__OS3706__

__MFS7299__

__RN02__

###### Geração do Anexo VIII – Apuração do ICMS no Período

Atualização do __Campo 090 – Estorno de débitos__

Acrescentar na recuperação do Motivo do Campo 90 do Detalhamento as novas as opções abaixo, quando selecionadas na Manutenção:

Gravar __3__ quando for “3\- Estorno debito serviço comunicação \- Art\. 44\-E do Anexo IX do RICMS/02” 

Gravar __4__ quando for “4\- Estorno debito serviço comunicação – Regime Especial”

__\[ALTERADA – CH5973\-A\_2014\]__

__REVERSA:__

Recuperar os dados para geração do arquivo magnético de acordo com o preenchido na tela Detalhamento, localizada em Estadual >> GIA\-MG >> Obrigações >> DAPI >> Manutenção:

__\[ALTERADA – CH27262\_2014\]__

__Consistência__

__Posição – Tamanho__

__Gravar fixo “22”__

\[01, 02\] 

__Inscrição Estadual do Contribuinte: __Campo__ __Inscrição Estadual do Estabelecimento \(Básicos >> Parâmetros >> Preliminares >> Inscrições Estaduais\)\.

\[03, 13\] 

__Ano de Referência: __Ano preenchido na tela de geração do arquivo magnético\.

\[16, 04\] 

__Mês de Referência: __Mês preenchido na tela de geração do arquivo magnético\.

\[20, 02\] 

__Dia Final da Referência: __Dia preenchido na tela de geração do arquivo magnético\.

\[22, 02\] 

__Dia Inicial da Referência: __Dia preenchido na tela de geração do arquivo magnético\.

\[24, 02\] 

__Número da nota fiscal: __Campo Nota Fiscal Aba Campo 90 do Detalhamento\.

__Tratamento:__

Informar, em ordem cronológica, os números das Notas Fiscais que originaram o estorno de débito\.

\[26, 09\] 

__Série da nota fiscal: __Campo Série da Nota Fiscal Aba Campo 90 do Detalhamento\.

\[35, 03\] 

__Data da nota fiscal: __Campo Data Emissão Aba Campo 90 do Detalhamento\.

__Tratamento:__

Data da nota fiscal <= Data final do período de referência da declaração

\[38, 08\] 

__Valor: __Campo Valor Aba Campo 90 do Detalhamento\.

\[46, 15\] 

__Justificativa: __Campo Justificativa Aba Campo 90 do Detalhamento\. 

                      __\[MFS33913\]__ A partir do período de referencia 01/2020, informar vazio\.

\[61, 60\] 

__Motivo:__ Campo Motivo Aba Campo 90 do Detalhamento\.

__Tratamento:__

Os campos anteriores só vão gerar de acordo com o Motivo do estorno, conforme segue:

__Código 1 = “Outros”:__ O Sistema permitirá a informação de todos os campos do detalhamento \(Número da NF, série da NF, data da NF, justificativa e valor\)\.  __\[MFS33913\]__ A partir do período de referencia 01/2020, informar vazio\.

__Código 2 = “Estorno débito serv transp recolhido ST”:__ O Sistema permitirá a informação apenas do campo "valor"\.

__Código 3 = “Estorno de Débito Serv\. Com Art\. 44\-E, da Parte 1 do Anexo IX do RICMS”:__ Na utilização desse código o usuário deverá informar o nº da NF emitida, série da NF, data da NF, Justificativa e valor\.

__Código 4 = “Estorno de Débito Serv\. Comunição – Regime Especial”:__ Na utilização o usuário deverá informar o valor a ser estornado e na justificativa o nº do Regime Especial\.__ \[MFS33913\]__ A partir do período de referencia 01/2020, informar vazio\.

__Código 5 = “Estorno Débito TTD”: __O Sistema permitirá a informação apenas do campo "valor"\. __\[MFS33913\]__ A partir do período de referencia 01/2020, informar vazio\.

__Código 6 = “Estorno de Débito Sub\-apuração\- Recolhimento Efetivo”: __O Sistema permitirá a informação apenas do campo "valor"\.

\[121, 01\]

__OS3706__

__CH5973\-A\_2014__

__CH27262\_2014__

__RN03__

###### Geração do Anexo VIII – Apuração do ICMS no Período

__\- Campo 090\.1 – Estorno FEM:          __\(campo criado na OS3706\)

Deverá ser informado o número __120__ na identificação da linha correspondente ao quadro VIII\.

E a identificação da coluna será preenchida com “zeros”\.

No campo de valor, deverá ter tamanhos 15 \(quinze\), utilizando o caracter “0” \(zero\), alinhado à esquerda, para preenchimento\. Deverá conter apenas caracteres numéricos, suprimindo pontos e vírgulas\. Ex: R$1\.000,50; formatando: 000000000100050\.

Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção\. Em caso de não possuir valor, preencher com zeros\.

__\- Campo 98\.1 – Fundo de Errad\. da Miséria a Recolher :       __\(__MFS7299__: campo criado p/a versão “802”\)

Este campo será preenchido com zeros para períodos anteriores à 09/2016\. 

A partir de 09/2016 \(vrs 8\.02\), será preenchido com a informação do campo \[98\.1\], informado na Manutenção dos Anexos \(este campo *não* tem geração automática\)\.

Linha Tipo 10, identificação da linha = __127__, identificação da coluna será preenchida com “zeros”\.

__OS3706__

__MFS7299__

__RN04__

###### Geração do Anexo IX – Obrigações 

As informações deste anexo são geradas na linha Tipo 10\. Será gerada uma linha 10 para cada informação do anexo, diferenciadas por uma coluna de identificação, utilizando uma numeração definida pela própria obrigação DAPI\.

__\- Campo 104\.1 – Recolhimento Efetivo:         __\(campo incluído na __OS4576__\)

A informação deste campo é gerada a partir do campo “104\.1\-Recolhimento Efetivo” da manutenção dos anexos \(menu Obrigação 🡪 DAPI 🡪 Manutenção 🡪 Anexos, aba “Obrigações”\)\. 

No campo de identificação da linha será gerado o número “123”, conforme as orientações de preenchimento da DAPI\.

O campo de identificação da coluna será preenchido com zero\.

O tamanho do campo no layout é de 15 posições, incluindo as 2 casas decimais, e sem vírgulas ou pontos\.

__\- Campo 105\.1 – Total do FEM Subst\. Tributário:__

\(__MFS7299__: a partir da versão 8\.02 este campo foi renomeado para “Total do FEM Subst\. Tributário”\)

__  __

Este campo será preenchido com o somatório do campo “082\.1\- Fundo de Errad\. da Miséria\- FEM” \+ campo “090\.1\-Estorno FEM”\. 

Alteração da __MFS7299:__

\- Quando o período de referência for anterior à 09/2016 🡪 o campo será preenchido com a soma do campo__ 082\.1  __082\.2 \(Anexo VII\) \+ campo 090\.1

  \(Anexo VIII\);

\- Para períodos a partir de 09/2016 🡪 o campo será preenchido com a informação do campo “82\.2\-Fundo de Erradicação da Miséria” da aba “ICMS

   Subst\. Tributario” \(Anexo VII\)\.

Em caso de não possuir valor, preencher com zeros\.

Deverá ser informado o número __121__ na identificação da linha correspondente ao quadro IX\.

E a identificação da coluna será preenchida com “zeros”\.

__\- Campo 105\.2 – Total do FEM Op\. Própria:        __\(__MFS7299__: campo criado p/a versão “802”\)

Este campo será preenchido com zeros para períodos anteriores à 09/2016\. 

A partir de 09/2016 \(vrs 8\.02\), será preenchido com a informação do campo \[105\.2\], gerado na Manutenção dos Anexos\.

\(o campo 105\.2 é originado do campo 98\.1 do Anexo VIII, campo este que não tem geração automática\)\.

Linha Tipo 10, identificação da linha = __129__, identificação da coluna será preenchida com “zeros”\.

__Campo 110\.1 – Total do FEM Antecipado:__

Incluir na geração do meio magnético do Tipo de Linha “10” o__ Campo 110\.1 – Total do FEM Antecipado__

Deverá ser informado o número __122__ na identificação da linha correspondente ao quadro IX\.

E a identificação da coluna será preenchida com “zeros”\.

No campo de valor, deverá ter tamanhos 15 \(quinze\), utilizando o caracter “0” \(zero\), alinhado à esquerda, para preenchimento\. Deverá conter apenas caracteres numéricos, suprimindo pontos e vírgulas\. Ex: R$1\.000,50; formatando: 000000000100050\.

Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção\. Em caso de não possuir valor, preencher com zeros\.

__\- Campo 99\.1 – Desconto ICMS – Decreto 47\.226/17 \(ICMS Normal\):        __\(__CH11086\_2018 \(MFS\-19044\)__: campo criado p/a versão “900”\)

Este campo será preenchido com zeros para todos os períodos independentemente da versão\.

Linha Tipo 10, identificação da linha = __130__, identificação da coluna será preenchida com “zeros”\.

__\- Campo 99\.2 – ICMS a Recolher:        __\(__CH11086\_2018 \(MFS\-19044\)__: campo criado p/a versão “900”\)

Este campo será preenchido com o resultado da linha 99 para todos os períodos independentemente da versão\.

Linha Tipo 10, identificação da linha = __131__, identificação da coluna será preenchida com “zeros”\. \(Resultado da linha 99 \- o resultado da linha 130 🡪 neste caso sempre “zeros”\)\.

__\- Campo 104\.2 – Desconto ICMS – Decreto 47\.226/17 \(TTS\):        __\(__CH11086\_2018 \(MFS\-19044\)__: campo criado p/a versão “900”\)

Este campo será preenchido com zeros para todos os períodos independentemente da versão\.

Linha Tipo 10, identificação da linha = __132__, identificação da coluna será preenchida com “zeros”\.

__\- Campo 104\.3 – Recolhimento Efetivo Líquido:        __\(__CH11086\_2018 \(MFS\-19044\)__: campo criado p/a versão “900”\)

Este campo será preenchido com o resultado da linha 123 para todos os períodos independentemente da versão\.

Linha Tipo 10, identificação da linha = __133__, identificação da coluna será preenchida com “zeros”\. \(Resultado da linha 123 \- o resultado da linha 132 🡪 neste caso sempre “zeros”\)\.

__OS3706__

__OS4576__

__MFS7299__

__CH11086\_2018 \(MFS\-19044\)__

__RN05__

###### Geração da Linha Tipo 23 

Alteração da __OS4576__:

Nesta linha foram incluídos os seguintes campos, que serão recuperados da tabela EST\_MG\_GIA\_LIN23:

\- Saldo Período Anterior \- Incentivo ao Esporte

\- Incentivo ao Esporte

\- Total Dedução Incentivo ao Esporte

\- Vlr Limite para Dedução \- Incentivo ao Esporte

\- Saldo Credor Período Seguinte \- Incentivo ao Esporte

\- Alíquota de Dedução \- Incentivo ao Esporte

\- Estorno de Saldo de Incentivo ao Esporte

Todos estes campos tem o tamanho no layout de 15 posições, já considerando duas casas decimais, inclusive o campo da alíquota\.

\(conforme orientações de preenchimento da DAPI\-MG no documento “InstrucoesGeraDapi\.pdf”\)

__OS4576__

__RN06__

###### Geração da Linha Tipo 36 

\(a geração desta linha foi implementada na __OS4576\)__

Esta linha será gerada a partir do detalhamento dos valores de incentivo do esporte cadastrados na aba “__Incentivo ao Esporte__” da tela de manutenção do campo 98 da DAPI \(menu Obrigação 🡪 DAPI 🡪 Manutenção 🡪 Detalhamento, aba “Campo 98”\)\.

 

*\(estes dados ficam armazenados na tabela EST\_MG\_GIA\_DET, com o identificador COD\_LINHA = 36\) *

Poderão existir várias linhas 36 no arquivo, uma para cada linha de detalhamento inserida na manutenção da aba “__Incentivo ao Esporte__” para a Empresa, Estabelecimento, e Mês/Ano de referência em questão\.

Layout da linha 36:

__Campo__

__Posição__

__Conteúdo__

Identificador da linha

\[01,02\]

“36” 

Inscrição Estadual do Contribuinte

\[03,13\]

     Informações do registro de identificação da DAPI

                            \(Linha Tipo 00\)

Ano de Referência

\[16,04\]

Mês de Referência

\[20,02\]

Dia Final da Referência

\[22,02\]

Dia Inicial da Referência

\[24,02\]

Número do Termo

\[26,10\]

Campo “Número do Termo”\. 

Preencher com zeros à esquerda se necessário\. 

Data da autorização do termo

\[33,08\]

Campo “Data da Autorização”

Valor

\[41,15\]

Campo “Valor”

__OS4576__

__MFS27892__

__RN07__

###### Geração do Anexo VIII – Apuração do ICMS no Período \(linha 29 – Detalhamento 10 – Campo 95\)

Atualização do __Campo 095 – Estorno de Créditos__

Recuperar os dados para geração do arquivo magnético de acordo com o preenchido na tela Detalhamento, localizada em Estadual >> GIA\-MG >> Obrigações >> DAPI >> Manutenção >> Detalhamento – aba Campo 95:

__Consistência__

__Posição – Tamanho__

__Gravar fixo “29”__

\[01,02\]

__Inscrição Estadual do Contribuinte: __Campo__ __Inscrição Estadual do Estabelecimento \(Básicos >> Parâmetros >> Preliminares >> Inscrições Estaduais\)\.

\[03, 13\] 

__Ano de Referência: __Ano preenchido na tela de geração do arquivo magnético\.

\[16, 04\] 

__Mês de Referência: __Mês preenchido na tela de geração do arquivo magnético\.

\[20, 02\]

__Dia Final da Referência: __Dia preenchido na tela de geração do arquivo magnético\.

\[22, 02\]

__Dia Inicial da Referência: __Dia preenchido na tela de geração do arquivo magnético\.

\[24, 02\]

__Código do motivo do estorno: __Campo Cód\. Motivo Estorno Aba Campo 95 do Detalhamento\.

__\[MFS33913\]__ Se motivo = Estorno de crédito decorrente de Recomposição Fiscal – campo = 01

                          A partir do período de referencia 01/2020, informar vazio

\[26, 02\]

__Auto de Infração: __Campo Auto Infração Aba Campo 95 do Detalhamento\.

\[28, 13\]

<a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a><a id="OLE_LINK9"></a><a id="OLE_LINK10"></a><a id="OLE_LINK11"></a><a id="OLE_LINK12"></a>__Valor: __Campo Valor Aba Campo 95 do Detalhamento\.

\[41, 15\]

__Nota Fiscal: __Campo Nota Fiscal Aba Campo 95 do Detalhamento\.

\[MFS48473\] Preencher com o Número da Nota Fiscal apenas para Código do Motivo = 05\.  Para os demais códigos, preencher com espaços em branco\.

\[56, 09\]

__Série Nota Fiscal: __Campo Série da NF Aba Campo 95 do Detalhamento\.

\[MFS48473\] Preencher com a Série da Nota Fiscal apenas para Código do Motivo = 05\.  Para os demais códigos, preencher com espaços em branco\.

\[65, 03\]

__Data Nota Fiscal: __Campo Data da NF Aba Campo 95 do Detalhamento\.

\[MFS48473\] Preencher com a Data da Nota Fiscal apenas para Código do Motivo = 05\.  Para os demais códigos, preencher com espaços em branco\.

\[68, 08\]

__OS4662__

MFS48473

__RN08__

###### Geração do Anexo VI – Outros Créditos/Débitos \(linha 27 – Detalhamento 08 – Campo 70\)

Atualização do __Campo 070 – Ressarcimento – Sub\. Tributária__

Recuperar os dados para geração do arquivo magnético de acordo com o preenchido na tela Detalhamento, localizada em Estadual >> GIA\-MG >> Obrigações >> DAPI >> Manutenção >> Detalhamento – aba Campo 95:

__\[ALTERADA – CH27262\_2014\]__

__Consistência__

__Posição – Tamanho__

__Gravar fixo “27”__

\[01,02\]

__Inscrição Estadual do Contribuinte: __Campo__ __Inscrição Estadual do Estabelecimento \(Básicos >> Parâmetros >> Preliminares >> Inscrições Estaduais\)\.

\[03, 13\] 

__Ano de Referência: __Ano preenchido na tela de geração do arquivo magnético\.

\[16, 04\] 

__Mês de Referência: __Mês preenchido na tela de geração do arquivo magnético\.

\[20, 02\]

__Dia Final da Referência: __Dia preenchido na tela de geração do arquivo magnético\.

\[22, 02\]

__Dia Inicial da Referência: __Dia preenchido na tela de geração do arquivo magnético\.

\[24, 02\]

__Motivo do Ressarcimento tributário: __Campo Motivo Aba Campo 70 do Detalhamento\.

__\[MFS33913\]__ A partir do período de referencia 01/2020, informar “00”

\[26, 02\]

__Número da NF de ressarcimento ST: __Campo Nota Fiscal Campo 70 do Detalhamento\.

\[28, 09\] 

__Série da Nota Fiscal: __Campo Série da Nota Fiscal Aba Campo 70 do Detalhamento\.

\[37, 03\] 

__Data da Nota Fiscal: __Campo Data Emissão Aba Campo 70 do Detalhamento\.

\[40, 08\] 

__Data do Visto: __Campo Data do Visto Aba Campo 70 do Detalhamento\.

__\[MFS33913\]__ A partir do período de referencia 01/2020, preencher com 0 \(zeros\)\.

\[48, 08\] 

__Valor: __Campo Valor Aba Campo 95 do Detalhamento\.

\[56, 15\] 

__CH27262\_2014__

__RN09__

###### Geração do Anexo I  e II – Informações da Declaração  e do Contribuinte \(Geração da Linha Tipo 00 \- Identificação da DAPI\)

__\[ALTERADA – MFS\-18544\]__

__Consistência__

__Posição – Tamanho__

__Gravar fixo “00”__

\[01,02\]

__Inscrição Estadual do Contribuinte: __Campo__ __Inscrição Estadual do Estabelecimento \(Básicos >> Parâmetros >> Preliminares >> Inscrições Estaduais\)\.

\[03, 13\] 

__Ano de Referência: __Ano preenchido na tela de geração do arquivo magnético\.

\[16, 04\] 

__Mês de Referência: __Mês preenchido na tela de geração do arquivo magnético\.

\[20, 02\]

__Dia Final da Referência: __Dia preenchido na tela de geração do arquivo magnético\.

\[22, 02\]

__Dia Inicial da Referência: __Dia preenchido na tela de geração do arquivo magnético\.

\[24, 02\]

__Modelo da DAPI: __Gravar fixo “D1”\.

\[26, 02\]

__DAPI para substituição?: __Campo Substitui DAPI já entregue da tela de Geração dos Registros \(GIA\-MG >> Obrigações >> DAPI >> Manutenção >> Geração dos Registros\), preencher de acordo com a RN10 do documento matriz MTZ \- DAPI\-MG \- Geracao dos Registros\.doc\.

\[28, 01\]

__CAE: __Campo CAE da tela de Anexos \(GIA\-MG >> Obrigações >> DAPI >> Manutenção >> Anexos >> aba Identificação\) que tem como origem a Atividade Econômica da tabela Estabelecimento na geração dos registros\.

__Tratamento: __

Se a atividade for menor que 7 posições preencher com zeros a esquerda\. *Exemplo:* Atividade Econômica 111301 – Cultivo de Arroz, no arquivo magnético considerar 0111301\.

\[29, 07\]

__Desmembramento do CAE: __Campo Desmembramento CNAE\-F da tela de Desmembramento do CNAE\-F \(GIA\-MG >> Parâmetros >> Desmembramento do CNAE\-F\), preencher com as duas últimas posições de acordo com o parametrizado para o código de atividade cadastrado\.

\[36, 02\]

__Regime de Recolhimento: __Campo Regime Recolhimento da tela de Anexos \(GIA\-MG >> Obrigações >> DAPI >> Manutenção >> Anexos >> aba Identificação\) que tem como origem ao Regime de Recolhimento preenchido na tela de geração dos registros\.

__Tratamento:__

Na geração dos registros, se a Data limite para pagamento = “00/00/0000” então considerar N\. 

Na geração dos registros, se a Data limite para pagamento > Dia final de referência, então considerar S\. 

\[38, 02\]

__Regime especial de fiscalização? \[S/N\]: __Campo Sob regime especial de fiscalização ou memorando de entendimento da tela de Anexos \(GIA\-MG >> Obrigações >> DAPI >> Manutenção >> Anexos >> aba Identificação\)\.

\[40, 01\]

__Data limite para pagamento: __Campo Data limite de pagamento__ __da tela de Anexos \(GIA\-MG >> Obrigações >> DAPI >> Manutenção >> Anexos >> aba Identificação\) que tem como origem a Data Limite de Pagamento preenchido na tela de geração dos registros\.

\[41, 08\]

__Optante pelo FUNDESE? \[S/N\]: __Gravar fixo “N”\.

\[49, 01\]

__DAPI com movimento \[S/N\]: __

__\[ALTERADA – CH26067\_2015\]__

Na geração dos registros, se não houver nenhuma movimentação gravada na DAPI, ou seja, seus registros gerarem com zeros nos Anexos, Detalhamento, Movimento de Café e Demonstrativo das Operações/Prestações \(tabelas: est\_mg\_gia\_lin10, est\_mg\_gia\_lin23, est\_mg\_gia\_det, est\_mg\_gia\_cafe, est\_mg\_rel\_demonst\) e ainda, se apenas os campos Saldo Credor do Período Anterior, Saldo Credor para Per\. Seguinte e de Total dos Créditos estiverem preenchidos em Anexos \(tabela est\_mg\_gia\_lin10\), preencher com “N”, caso contrário preencher com S\.

Na geração dos registros, se não houver nenhuma movimentação da apuração gravada na DAPI, ou seja, seus registros gerarem com zeros, preencher com “N”, caso contrário preencher com S\.

__\[ALTERADA – CH2492\_2015\]__

__Tratamento:__

Existe uma exceção para a DAPI quando são gerados apenas os valores de Saldo Credor \(Anterior e Seguinte\), então gerar como sem movimento, ou seja, igual “N”, mesmo quando houver apenas os registros 87, 91 e 92 do Anexo VIII preenchido com valor maior que zero\.

No Mastersaf DW, para preenchimento desse campo na DAPI, são verificadas as informações cadastradas diretamente na aba “Apuração”, localizada em Obrigações >> DAPI >> Manutenção >> Anexos, então focando na apuração, quando:

- Possui Movimento de Notas e Apuração, gerar S;
- Possui Movimento de Notas e Não Possui de Apuração, gerar N;
- Não Possui Movimento de Notas e Possui de Apuração, gerar S\. Com EXCEÇÃO se houver apenas valores nos Registros 87, 91 e 92 do Anexo VIII, pois assim, deverá gerar N;
- Não Possui Movimento de Notas E Apuração, gerar N\.

\[50, 01\]

__Movimento de Café \[S/N\]: __Campo Movimento de Café__ __da tela de Geração dos Registros \(GIA\-MG >> Obrigações >> DAPI >> Manutenção >> Geração dos Registros\)\.

\[51, 01\]

__CNAE\-F: __Campo CAE da tela de Anexos \(GIA\-MG >> Obrigações >> DAPI >> Manutenção >> Anexos >> aba Identificação\) que tem como origem a Atividade Econômica da tabela Estabelecimento na geração dos registros\.

__Tratamento: __

Se a atividade for menor que 7 posições preencher com zeros a esquerda\. *Exemplo:* Atividade Econômica 111301 – Cultivo de Arroz, no arquivo magnético considerar 0111301\.

\[52, 07\]

__Desmembramento do CNAE\-F: __Campo Desmembramento CNAE\-F da tela de Desmembramento do CNAE\-F \(GIA\-MG >> Parâmetros >> Desmembramento do CNAE\-F\), preencher com as duas últimas posições de acordo com o parametrizado para o código de atividade cadastrado\.

\[59, 02\]

__Termo de Aceite: \[ALTERADA \- CH11240\_2018 \(MFS\-18927\)\]__Gravar fixo “N”\. a partir da apuração de 05/2018\.

\[60, 01\]

__CH2492\_2015__

__MFS\-18544__

__RN10__

###### Geração do Anexo VI \- Outros Créditos / Débitos

__Campo 71\.1 – Crédito Difal Origem \(EC 87/15\):    __

\(__MFS7299__: campo criado p/a versão “802”\)

\(__MFS27892__: campo excluído p/a versão “901”\)

Este campo será preenchido com zeros para períodos anteriores à 09/2016 e para períodos posteriores à 04/2019\. 

A partir de 09/2016 \(vrs 8\.02\), será preenchido com a informação do campo \[71\.1\], gerado previamente na rotina da Geração dos Registros e/ou Manutenção dos Anexos\.

Linha Tipo 10, identificação da linha = __124__, identificação da coluna será preenchida com “zeros”\.

__Campo 72 – Total:       __\(__MFS7299__: alterada a totalização deste campo para inclusão do campo 71\.1\)

Este campo é preenchido com a totalização dos campos 66 a 71\.1, conforme definido no documento de regras da rotina “Geração dos Totalizadores” \(ver “MTZ\-DAPI\-MG\-Geracao\-dos\-Totalizadores”, regra RN02\)\.

__Campo 74\.1 – Débito Difal Origem \(EC 87/15\):     __

__  __\(__MFS7299__: campo criado p/a versão “802”\)

\(__MFS27892__: campo excluído p/a versão “901”\)

Este campo será preenchido com zeros para períodos anteriores à 09/2016 e para períodos posteriores à 04/2019\. 

A partir de 09/2016 \(vrs 8\.02\), será preenchido com a informação do campo \[74\.1\], gerado previamente na rotina da Geração dos Registros e/ou Manutenção dos Anexos\.

Linha Tipo 10, identificação da linha = __125__, identificação da coluna será preenchida com “zeros”\.

__Campo 75 – Total:       __\(__MFS7299__: alterada a totalização deste campo para inclusão do campo 74\.1\)

Este campo é preenchido com a totalização dos campos 73 a 74\.1 conforme definido no documento de regras da rotina “Geração dos Totalizadores” \(ver “MTZ\-DAPI\-MG\-Geracao\-dos\-Totalizadores”, regra RN02\)\. 

__MFS7299__

__MFS27892__

__RN11__

###### Geração da Linha Tipo 20

Esta linha será gerada a partir do detalhamento de Créditos Recebidos da tela de manutenção do campo 66 da DAPI \(menu Obrigação 🡪 DAPI 🡪 Manutenção 🡪 Detalhamento, aba “Campo 66”\)\.

 

*\(Estes dados ficam armazenados na tabela EST\_MG\_GIA\_DET, com o identificador COD\_LINHA = 20 e COD\_LINHA = 66\) *

Layout da linha 20:

__Campo__

__Posição__

__Conteúdo__

Identificador da linha

\[01,02\]

“20” 

Inscrição Estadual do Contribuinte

\[03,13\]

     Informações do registro de identificação da DAPI

                            \(Linha Tipo 00\)

Ano de Referência

\[16,04\]

Mês de Referência

\[20,02\]

Dia Final da Referência

\[22,02\]

Dia Inicial da Referência

\[24,02\]

Produtor Rural? \[S/N\]

\[26,01\]

Campo Produtor Rural\.  Preencher com

“S” ou “N”\. A partir da Versão 8\.02\.00, informar sempre “N”__ __

UF

\[27,02\]

Campo “UF”

Inscrição Estadual do Remetente 

	\[29,15\]

Campo “Inscrição Estadual do Remetente”\.  

SE Rural = “N” ENTÃO 

Inscrição Estadual válida para a UF Informada\. 

FIM 

Preencher com zeros à esquerda se necessário\. 

__\[MFS33913\]__ A partir do período de referencia 01/2020, informar fixo “MG”

Número da nota fiscal 

\[44,09\]

Campo “Número da nota fiscal”

Série da nota fiscal 

\[52,03\]

Campo “Série da nota fiscal”

Data da nota fiscal 

\[56,08\]

Campo “Data da nota fiscal”

Data do visto 

\[64,08\]

Campo “Data do visto”

__\[MFS33913\]__ A partir do período de referencia 01/2020, preencher com 0 \(zeros\)\.

Valor 

\[72,15\]

Campo “Valor”

Código do Motivo

\[87, 02\] 

Campo “Código do Motivo”

__\[MFS33913\]__ A partir do período de referencia 01/2020, informar “00”__ __

__MFS27892__

__RN12__

###### Geração da Linha Tipo 73

Esta linha será gerada a partir do detalhamento __de Créditos Transferidos__ da tela de manutenção do campo 73 da DAPI \(menu Obrigação 🡪 DAPI 🡪 Manutenção 🡪 Detalhamento, aba “Campo 73”\)\.

 

*\(Estes dados ficam armazenados na tabela EST\_MG\_GIA\_DET, com o identificador COD\_LINHA = 21 e COD\_LINHA = 73\) *

Layout da linha 21:

__Campo__

__Posição__

__Conteúdo__

Identificador da linha

\[01,02\]

“21” 

Inscrição Estadual do Contribuinte

\[03,13\]

     Informações do registro de identificação da DAPI

                            \(Linha Tipo 00\)

Ano de Referência

\[16,04\]

Mês de Referência

\[20,02\]

Dia Final da Referência

\[22,02\]

Dia Inicial da Referência

\[24,02\]

Produtor Rural? \[S/N\]

\[26,01\]

Campo Produtor Rural\.  Preencher com

“S” ou “N”\. A partir da Versão 8\.02\.00, informar sempre “N”__ __

UF

\[27,02\]

Campo “UF”

__\[MFS33913\]__ A partir do período de referencia 01/2020, informar fixo “MG”\.

Inscrição Estadual do Destinatário 

\[29,15\]

Campo “Inscrição Estadual do Destinatário”\.  

SE Rural = “N” ENTÃO 

Inscrição Estadual válida para a UF Informada\. 

FIM 

Preencher com zeros à esquerda se necessário\. 

Número da nota fiscal 

\[44,09\]

Campo “Número da nota fiscal”

Série da nota fiscal 

\[52,03\]

Campo “Série da nota fiscal”

Data da nota fiscal 

\[56,08\]

Campo “Data da nota fiscal”

Data do visto 

\[64,08\]

Campo “Data do visto”

__\[MFS33913\]__ A partir do período de referencia 01/2020, preencher com 0 \(zeros\)\.

Valor 

\[72,15\]

Campo “Valor”

Código do Motivo

\[87, 02\] 

Campo “Código do Motivo”

__\[MFS33913\]__ A partir do período de referencia 01/2020, informar “00”\.

__MFS27892__

__RN13__

###### Geração da Linha Tipo 24

###### Esta linha será gerada a partir do detalhamento da Compensação de Crédito entre Estabelecimentos da tela de manutenção da DAPI \(menu Obrigação 🡪 DAPI 🡪 Manutenção 🡪 Detalhamento, aba “Compensação de Créd\. entre Estabelecimentos”\)\.

######  

###### \(Estes dados ficam armazenados na tabela EST\_MG\_GIA\_DET, com o identificador COD\_LINHA = 24\) 

###### Layout da linha 24:

__Campo__

__Posição__

__Conteúdo__

Identificador da linha

\[01,02\]

“24” 

Inscrição Estadual do Contribuinte

\[03,13\]

     Informações do registro de identificação da DAPI

                            \(Linha Tipo 00\)

Ano de Referência

\[16,04\]

Mês de Referência

\[20,02\]

Dia Final da Referência

\[22,02\]

Dia Inicial da Referência

\[24,02\]

Inscrição Estadual do Remetente 

\[26,15\]

Campo “Inscrição Estadual do Remetente”\.  

__MFS39540__\-Alterou preenchimento do campo p/incluir brancos à esquerda\. 

Preencher com zeros brancos à esquerda se necessário\. 

Número da nota fiscal 

\[41,09\]

Campo “Número da nota fiscal”

Série da nota fiscal 

\[50,03\]

Campo “Série da nota fiscal”

Data da nota fiscal 

\[53,08\]

Campo “Data da nota fiscal”

Data do visto 

\[61,08\]

Campo “Data do visto”

__\[MFS33913\]__ A partir do período de referencia 01/2020, preencher com 0 \(zeros\)\.

Valor 

\[69,15\]

Campo “Valor”

__MFS27892__

__RN14__

###### Geração da Linha Tipo 25

###### Esta linha será gerada a partir do detalhamento dos valores de incentivo à cultura cadastrados na aba “Incentivo à Cultura” da tela de manutenção do campo 98 da DAPI \(menu Obrigação 🡪 DAPI 🡪 Manutenção 🡪 Detalhamento, aba “Campo 98”\)\.

######  

###### \(Estes dados ficam armazenados na tabela EST\_MG\_GIA\_DET, com o identificador COD\_LINHA = 25\) 

###### Poderão existir várias linhas 25 no arquivo, uma para cada linha de detalhamento inserida na manutenção da aba “Incentivo à Cultura” para a Empresa, Estabelecimento, e Mês/Ano de referência em questão\.

###### Layout da linha 25:

__Campo__

__Posição__

__Conteúdo__

Identificador da linha

\[01,02\]

“25” 

Inscrição Estadual do Contribuinte

\[03,13\]

     Informações do registro de identificação da DAPI

                            \(Linha Tipo 00\)

Ano de Referência

\[16,04\]

Mês de Referência

\[20,02\]

Dia Final da Referência

\[22,02\]

Dia Inicial da Referência

\[24,02\]

Número do Certificado de aprovação 

\[26,13\]

Campo Número do Certificado de aprovação\. Preencher com zeros à esquerda se necessário 

Data da autorização da Declaração de Intenção 

\[39,08\]

Campo “Data da autorização da Declaração de Intenção”

Valor deduzido no mês de referência 

\[47,15\]

Campo “Valor deduzido no mês de referência”

__MFS27892__

__RN15__

###### Geração da Linha Tipo 28

###### Esta linha será gerada a partir do detalhamento do Ressarcimento ICMS  da tela de manutenção do campo 79 da DAPI \(menu Obrigação 🡪 DAPI 🡪 Manutenção 🡪 Detalhamento, aba “Campo 79”\)\.

######  

###### \(Estes dados ficam armazenados na tabela EST\_MG\_GIA\_DET, com o identificador COD\_LINHA = 28\) 

###### Layout da linha 28:

__Campo__

__Posição__

__Conteúdo__

Identificador da linha

\[01,02\]

“28” 

Inscrição Estadual do Contribuinte

\[03,13\]

     Informações do registro de identificação da DAPI

                            \(Linha Tipo 00\)

Ano de Referência

\[16,04\]

Mês de Referência

\[20,02\]

Dia Final da Referência

\[22,02\]

Dia Inicial da Referência

\[24,02\]

Inscrição Estadual do Remetente 

\[26,15\]

Campo “Inscrição Estadual do Remetente”\.  

Preencher com zeros à esquerda se necessário\. 

Número da nota fiscal 

\[41,09\]

Campo “Número da nota fiscal”

Série da nota fiscal 

\[50,03\]

Campo “Série da nota fiscal”

Data da nota fiscal 

\[53,08\]

Campo “Data da nota fiscal”

Data do visto 

\[61,08\]

Campo “Data do visto”

__\[MFS33913\]__ A partir do período de referencia 01/2020, preencher com 0 \(zeros\)\.

Valor 

\[69,15\]

Campo “Valor”

Código do Motivo

\[84, 01\] 

Campo “Código do Motivo”

__MFS27892__

__RN16__

###### Geração da Linha Tipo 35

###### Esta linha será gerada a partir do detalhamento do Remetente de Crédito da tela de manutenção do campo 98 da DAPI \(menu Obrigação 🡪 DAPI 🡪 Manutenção 🡪 Detalhamento, aba “Campo 98”\)\.

######  

###### \(Estes dados ficam armazenados na tabela EST\_MG\_GIA\_DET, com o identificador COD\_LINHA = 35\) 

###### Layout da linha 35:

__Campo__

__Posição__

__Conteúdo__

Identificador da linha

\[01,02\]

“35” 

Inscrição Estadual do Contribuinte

\[03,13\]

     Informações do registro de identificação da DAPI

                            \(Linha Tipo 00\)

Ano de Referência

\[16,04\]

Mês de Referência

\[20,02\]

Dia Final da Referência

\[22,02\]

Dia Inicial da Referência

\[24,02\]

Identificador Utilização Crédito 

\[26,10\]

Campo “Identificador Utilização Crédito”

Inscrição Estadual do Remetente 

\[36,15\]

Campo “Inscrição Estadual do Remetente”\.  

Preencher com zeros à esquerda se necessário\. 

Número da nota fiscal 

\[51,09\]

Campo “Número da nota fiscal”

Série da nota fiscal 

\[60,03\]

Campo “Série da nota fiscal”

Data da nota fiscal 

\[63,08\]

Campo “Data da nota fiscal”

Data do visto 

\[71,08\]

Campo “Data do visto”

__\[MFS33913\]__ A partir do período de referencia 01/2020, preencher com 0 \(zeros\)\.

Valor da Operação

\[79,15\]

Campo “Valor”

__\[MFS80115\] Preencher __com o valor do campo 64 \- VLR\_CONTAB\_ITEM \(SAFX08\)\.

__MFS27892__

__RN17__

###### Geração da Linha Tipo 34

###### Esta linha será gerada a partir do detalhamento de Utilização de Crédito da tela de manutenção do campo 98 da DAPI \(menu Obrigação 🡪 DAPI 🡪 Manutenção 🡪 Detalhamento, aba “Campo 98”\)\.

######  

###### \(Estes dados ficam armazenados na tabela EST\_MG\_GIA\_DET, com o identificador COD\_LINHA = 34\) 

###### Layout da linha 34:

__Campo__

__Posição__

__Conteúdo__

Identificador da linha

\[01,02\]

“34” 

Inscrição Estadual do Contribuinte

\[03,13\]

     Informações do registro de identificação da DAPI

                            \(Linha Tipo 00\)

Ano de Referência

\[16,04\]

Mês de Referência

\[20,02\]

Dia Final da Referência

\[22,02\]

Dia Inicial da Referência

\[24,02\]

Identificador Utilização Crédito 

\[26,10\]

Campo “Identificador Utilização Crédito”

Código do Motivo

\[36,02\]

Campo “Código do Motivo”

__\[MFS33913\]__ A partir do período de referencia 01/2020, informar “00”\.

Número da nota fiscal 

\[38,09\]

Campo “Número da nota fiscal”

Série da nota fiscal 

\[47,03\]

Campo “Série da nota fiscal”

Data da nota fiscal 

\[50,08\]

Campo “Data da nota fiscal”

Data do visto 

\[58,08\]

Campo “Data do visto”

__\[MFS33913\]__ A partir do período de referencia 01/2020, preencher com 0 \(zeros\)\.

Valor da Operação

\[66,15\]

Campo “Valor”

__\[MFS80115\] Preencher__ com o valor do campo 64 \- VLR\_CONTAB\_ITEM \(SAFX08\)\.

__MFS27892__

__RN18__

###### Geração do Anexo XI – Informações Econômicas

__Campo 115 – Número de Empregados no Úlitmo Dia do Período    __

Para períodos a partir de __05/2020, __a linha do registro Tipo 10 referente ao campo 115 não será mais gravada no arquivo \(__MFS38330__: Versão 9\.03\)\.

__Campo 116\-Valor da Folha de Pagamento__

Para períodos a partir de __05/2020, __a linha do registro Tipo 10 referente ao campo 116 não será mais gravada no arquivo \(__MFS38330__: Versão 9\.03\)\.

__MFS38330__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


# MTZ-Report_Fiscal-Diferencial_de_Aliquotas_por_CFOP

- **Fonte:** MTZ-Report_Fiscal-Diferencial_de_Aliquotas_por_CFOP.docx
- **Modificado:** 2026-03-23
- **Tamanho:** 80 KB

---

__Report Fiscal – Relatório de Diferencial de Alíquota por CFOP__

                                         

__BÁSICOS → REPORT FISCAL → Obrigações Acessórias → ICMS → Diferencial de Alíquota p/ DataMart → CFOP__

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

CH75629

Alteração Relatório Report Fiscal

Incluir opção por UF e “Todos” os estabelecimentos no critério de seleção

OS3196

Permitir a geração por Inscrição Estadual Única dos relatórios de Diferencial de Alíquota de ICMS 

Permitir a geração a partir dos estabelecimentos centralizadores\. 

OS2853

Considerar Base Isenta ICMS para Diferencial de Aliquota

Considerar Base Isenta ICMS para Diferencial de Aliquota

OS3819

Alteração da apuração do Dif\. Alíquota

Alteração da apuração do diferencial de alíquota para considerar o parâmetro 67 \(Parametrização por UF do Módulo ICMS\)\. \(ver __RN09__\)

__MFS76479__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para as UF’s RS, GO, MG e PR \(Readequação a alteração dos Lançamentos Automáticos da Apuração\. \(MTZ\_Calculo\_Diferencial\_Aliquota\_Lancamento\_Automatico\)\.

__MFS88013__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para a UF de SP\.

__MFS94495__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para as UF´s de ES, BA e SC\.

__MFS435431__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para a UF de PA

__MFS519100__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para a UF de MA

__MFS564128__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para a UF de RO

__MFS569514__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para a UF de AC

__MFS571687__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para a UF de RJ

__MFS571692__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para a UF de SE

__MFS572622__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para a UF de RR\.

__MFS572711__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para a UF de TO\.

__MFS573401__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para a UF de AM\.

__MFS573416__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para a UF de AP\.

__MFS573406__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para a UF de PE\.

__MFS573412__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para a UF de MS\.

__MFS576319__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para a UF de PI\.

__MFS576330__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para a UF de AL\.

__MFS593861__

Andréa Rocha

Alteração da regra de validação do parâmetro “Somente documentos com diferencial” para tratar as regras específicas criadas para cada UF\.

__MFS593347__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para a UF de PB\.

__MFS844874__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para a UF de RN\.

<a id="_Hlk204202502"></a>__MFS859953__

Alteração para calcular o DIFAL

Ajuste do Cálculo do DIFAL com Base Dupla p/ São Paulo em atendimento às operações de contribuintes do Simples Nacional – Base Dupla – RN10\.d

__MFS938348__

Alteração para calcular o DIFAL

Ajuste do Cálculo do DIFAL com Base Dupla p/ São Paulo em atendimento às operações de contribuintes do Simples Nacional – Base Dupla – RN10\.d

__MFS1049811__

Alteração para calcular o DIFAL

Inclusão de Regra para considerar o Parâmetro 92 \(Parâmetros p/ UF\) Específico para a UF de DF\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Criar o listbox “UF”, onde serão exibidas todas as UF’s para seleção do usuário, com os critérios abaixo:

1 \- A primeira opção de seleção deve ser NULO, caso o usuário não queira utilizar esse filtro;

2 \- Caso o usuário selecione determinada UF, somente devem ser gerados os dados referentes a UF selecionada\.

CH75629

__RN01__

O listbox “ESTABELECIMENTO” deve ficar abaixo do listbox “UF” e possuir o seguinte comportamento;

1 – Caso o usuário selecione determinada UF, deverão aparecer somente os Estabelecimentos situados naquela determinada UF;

2 – Para o caso 1 \(acima\) deverá aparecer no listbox a opção “TODOS” e caso o usuário a selecione, deverão ser gerados os dados de todos os Estabelecimentos daquela determinada UF\.

CH75629

__RN02__

Na tela de argumentos deste relatório, acrescentar um flag antes do campo UF:

__\[  \] Geração Centralizada por Inscrição Estadual Única__

Este campo deve vir por default desmarcado\.  
  
__\[  \] Somente documentos com diferencial__

Este campo deve vir por default __marcado__ \(vide RN11\)\.

OS3196

MFS593861

__RN03__

Quando não for selecionado nenhuma opção no campo UF e o campo ¨Geração Centralizada por Inscrição Estadual Única¨ estiver marcado, apresentar somente a lista dos estabelecimentos centralizadores\.

OS3196

__RN04__

Quando for selecionada uma UF no campo UF e o campo ¨Geração Centralizada por Inscrição Estadual Única¨ estiver marcado, apresentar somente a lista dos estabelecimentos centralizadores daquela UF\.

OS3196

__RN05__

Quando não for selecionado nenhuma opção no campo UF e o campo ¨Geração Centralizada por Inscrição Estadual Única¨ não estiver marcado, apresentar a lista de todos os estabelecimentos\.

OS3196

__RN06__

Quando for selecionada uma UF no campo UF e o campo ¨Geração Centralizada por Inscrição Estadual Única¨ não estiver marcado, apresentar a lista de todos os estabelecimentos daquela UF\.

OS3196

__RN07__

Regra para incluir fleg “Considerar Base Isenta ICMS para cálculo do Diferencial de Aliquota”:

No módulo Básicos → Report Fiscal → Obrigações Acessórias → ICMS → Diferencial de Alíquota p/ Datamart → Código Fiscal de Operação – CFOP, incluir o fleg “Considerar Base Isenta ICMS para cálculo do Diferencial de Aliquota”\.

OS2853

__RN08__

Regra para o fleg “Considerar Base Isenta ICMS para cálculo do Diferencial de Aliquota”:

Se campo flag “Considerar Base Isenta ICMS para cálculo do Diferencial de Aliquota”  estiver marcado:

Considerar para o cálculo do Diferencial de Aliquota o campo “Base Isenta ICMS”

Se campo flag “Considerar Base Isenta ICMS para cálculo do Diferencial de Aliquota” estiver desmarcado:

Considerar para o cálculo do Diferencial de Aliquota o campo “Base ICMS”

Este campo deve vir por default desmarcado\.

OS2853

__RN09__

__Recuperação das NFs utilizando o parâmetro 67 \(Parâmetros por UF do Módulo ICMS\)__

__Alteração da OS3819:__

A recuperação das notas para emissão do relatório foi alterada para utilizar o parâmetro 67 da parametrização por UF do Módulo ICMS \(menu Manutenção  Parâmetros por UF\)\. Originalmente, este parâmetro não era utilizado no filtro dos documentos\. A partir desta OS, tanto a apuração do DIFAL feita no livro P9, como os 4 relatórios do DIFAL do Report Fiscal foram atualizados para usar o parâmetro 67\.

A partir de então, serão recuperadas apenas as notas em que e UF da pessoa fis/jur \(ou a UF Origem da nota, dependendo do conteúdo do parâmetro 67\) for diferente da UF do Estabelecimento\.

A comparação das UF’s a serem utilizadas será feita da seguinte forma:

__Se__ parâmetro 67 marcado

      Neste caso, a comparação entre as UFs é feita utilizando a UF Origem informada no documento fiscal \(campo 117 

      da SAFX07\), mas apenas nos casos em que ela estiver preenchida, ou seja:

        __Se__ UF Origem da SAFX07 preenchida:

             \[UF Origem da SAFX07  <>  UF do cadastro do Estabelecimento\] 

        __Senão__

             \[UF do cadastro da SAFX04  <>  UF do cadastro do Estabelecimento\] 

__Senão__

       Neste caso, a comparação das UFs é feita sempre a partir da UF da pessoa fis/jur:

                \[UF do cadastro da SAFX04  <>  UF do cadastro do Estabelecimento\]

OS3819

__RN10__

__ \[MFS76479\] Tratamento Regra Cálculo Diferencial de Alíquota – Débito \(Considerando Parâmetro 92\) __

A regra para o cálculo do Valor de Diferencial de Alíquota dependerá do parâmetro 92 da parametrização por UF do Módulo ICMS \(menu “*Manutenção > Parâmetros por UF*”\), considerando a UF do estabelecimento, da seguinte forma:

__Se__ \(parâmetro 92 Desmarcado\)

O sistema deverá calcular o Diferencial de Alíquota conforme regras originais, aplicando a fórmula abaixo:

     Valor do DIFAL = Valor da Base de Cálculo \(considerando a parametrização definida no RN01\) __multiplicado__ 

                              pelo Valor da Diferença Alíquota ICMS \(valor deve ser dividido por 100\) <a id="OLE_LINK64"></a><a id="OLE_LINK65"></a>\(campo 44 da SAFX08\);

Sendo:

   Se parâmetro = 1  o DIFAL será = \[ Base Tributada \* DIF\_ALIQ\_TRIB\_ICMS / 100 \]

   Se parâmetro = 2  o DIFAL será = \[ \(Base Tributada \+ Base Outras\) \* DIF\_ALIQ\_TRIB\_ICMS / 100 \]

   Se parâmetro = 3  o DIFAL será = \[ \(Valor Contábil do Item – \(Base Isenta \+ Base Redução\) – Valor do ICMS\-ST\) 

                                                                                                                                          \* DIF\_ALIQ\_TRIB\_ICMS / 100 \]

   Se parâmetro = 4  o DIFAL será = valor carregado para o campo VLR\_OUTROS1 __\(\*Informado somente para linha de Débito\)__

Para os parâmetros 1, 2 e 3 o que muda é o valor que será utilizado como base para aplicação da alíquota, e no caso do parâmetro 4, o valor não é calculado, pois já vem carregado no campo “Valor Outros 1” do item do documento fiscal\.

__*\(\*\) *__*Módulo ferramentas, menu “Parâmetros do Sistema  Parâmetros por Estabelecimento”\.*

__Senão__

__  Se__ \(parâmetro 92 Marcado\):

     Neste caso, a regra de cálculo a ser utilizada depende da UF:

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a><a id="OLE_LINK17"></a>     Se UF do Estabelecimento = “__RS__”  <a id="OLE_LINK42"></a><a id="OLE_LINK43"></a><a id="OLE_LINK44"></a><a id="OLE_LINK45"></a>Neste caso será utilizada a regra de cálculo descrita na __RN10\.a__;

     Se UF do Estabelecimento = “__GO__”  Neste caso será utilizada a regra de cálculo descrita na __RN10\.b__;

     Se UF do Estabelecimento = “__PR__” ou “__MG__” <a id="OLE_LINK39"></a><a id="OLE_LINK40"></a><a id="OLE_LINK41"></a> Neste caso será utilizada a regra de cálculo descrita na __RN10\.c__;

     Se UF do Estabelecimento = “__SP__”  Neste caso será utilizada a regra de cálculo descrita na __RN10\.d__;

     Se UF do Estabelecimento = “__ES”, “BA” ou “SC”__  Neste caso será utilizada a regra de cálculo descrita na __RN10\.e__;    

     Se UF do Estabelecimento = “__PA__”  Neste caso será utilizada a regra de cálculo descrita na __RN10\.f__;

     Se UF do Estabelecimento = “__MA__”  Neste caso será utilizada a regra de cálculo descrita na __RN10\.g__;

     Se UF do Estabelecimento = “__RO__”  Neste caso será utilizada a regra de cálculo descrita na __RN10\.h__;

     Se UF do Estabelecimento = “__AC__”  Neste caso será utilizada a regra de cálculo descrita na __RN10\.i__;

     Se UF do Estabelecimento = “__RJ__”  Neste caso será utilizada a regra de cálculo descrita na __RN10\.j__; 

     Se UF do Estabelecimento = “__SE__”  Neste caso será utilizada a regra de cálculo descrita na __RN10\.k__;

     Se UF do Estabelecimento = “__RR__”  Neste caso será utilizada a regra de cálculo descrita na __RN10\.l__;

     Se UF do Estabelecimento = “__TO__”  Neste caso será utilizada a regra de cálculo descrita na __RN10\.m__;

     Se UF do Estabelecimento = “__AM__”  Neste caso será utilizada a regra de cálculo descrita na __RN10\.n;__ 

     Se UF do Estabelecimento = “__AP”__  Neste caso será utilizada a regra de cálculo descrita na __RN10\.o__;

     Se UF do Estabelecimento = “__PE”__  Neste caso será utilizada a regra de cálculo descrita na __RN10\.p__;

     Se UF do Estabelecimento = “__MS”__  Neste caso será utilizada a regra de cálculo descrita na __RN10\.q__;

     Se UF do Estabelecimento = “__PI”__  Neste caso será utilizada a regra de cálculo descrita na __RN10\.r__;

     Se UF do Estabelecimento = “__AL”__  Neste caso será utilizada a regra de cálculo descrita na __RN10\.s__;

     Se UF do Estabelecimento = “__PB”__  Neste caso será utilizada a regra de cálculo descrita na __RN10\.t__;

     Se UF do Estabelecimento = “__RN”__  Neste caso será utilizada a regra de cálculo descrita na __RN10\.u__;

     Se UF do Estabelecimento = “__DF”__  Neste caso será utilizada a regra de cálculo descrita na __RN10\.v__;

Se nenhuma das alternativas acima  Neste caso o cálculo será feito pela mesma regra usada p/o parâmetro

                                                           desmarcado, conforme descrito acima; 

__MFS76479__

__RN10\.a__

__Regra do cálculo para Diferencial de Alíquota– Débito e Débito \(extras\) \(UF = RS\)__: __p/ Material de Consumo e Ativo Imobilizado__

Regra para obtenção do valor a débito:

__S__e o parâmetro 92 estiver marcado \(menu “*Manutenção > Parâmetros por UF*”\);

  __E__ a UF do Estabelecimento for igual à __RS__

Aplicar a fórmula abaixo:

\[\(\(Base de Cálculo – ICMS Origem \* VLR\_ALIQ\_DESTINO\) / \(1 \- VLR\_ALIQ\_DESTINO\)\] – ICMS Origem\)

\[Valor da Base de Cálculo – Valor do ICMS x Valor da Alíquota de Destino\] \- Valor do ICMS

       1 \- Valor da Alíquota de Destino

Sendo:

\- Base de Cálculo: <a id="OLE_LINK52"></a><a id="OLE_LINK53"></a><a id="OLE_LINK54"></a>o valor a ser utilizado depende da opção de valor escolhida pelo usuário no parâmetro 92

  \(Parâmetros por UF\), da seguinte forma:

   Se opção = 1 \(“Valor Contábil do Item”\), será utilizado o valor contábil do item \(campo 64 da SAFX08\);

   Se opção = 2 \(“Valor parametrizado no Ferramentas”\), será utilizado o valor parametrizado no módulo

                        Ferramentas, \(*Módulo ferramentas, menu “Parâmetros do Sistema  Parâmetros por Estabelecimento”\)\.*

\- Valor do ICMS: Campo VLR\_ICMS SAFX08 ou Campo VLR\_ICMS\_NDESTAC SAFX08\.

\- Alíquota de Destino: Campo VLR\_ALIQ\_DESTINO SAFX08 \(valor deve ser dividido por 100\)\.

__Exemplo:__

\- Base de Cálculo: R$ 1\.000,00

\- ICMS Origem: 120,00

\- Alíquota interna: 18

\- Diferença de Alíquota: 6

Valor do DIFAL __=__ \[ \(\(1\.000,00 – 120,00\) x 0,18 \) /  \(1 \- 0,18\)\] – 120,00

                          \[ \(880,00 x 0,18\) / 0,82\] – 120,00

                          \[ 158,40 / 0,82\] – 120,00

                          193,17 – 120,00 = __73,17__

__Obs¹\.:__ Para maiores informações consultar documento: MTZ\_Calculo\_Diferencial\_Aliquota\_Lancamento\_Automatico\.doc

__Obs²\.:__ O cálculo do DIFAL para o tipo “Material de Consumo – Débito \(extras\)” é exatamente igual ao do tipo “Material de Consumo – Débito”\. A diferença é apenas na recuperação das notas, já que a parametrização de CFOP e Natureza de Operação é feita separadamente\.

__MFS76479__

__RN10\.b__

<a id="OLE_LINK86"></a><a id="OLE_LINK87"></a><a id="OLE_LINK88"></a>__Regra do cálculo para Diferencial de Alíquota– Débito e Débito \(extras\) \(UF = GO\)__: __p/ Material de Consumo e Ativo Imobilizado__

Regra para obtenção do valor a débito:

__S__e o parâmetro 92 estiver marcado \(menu “*Manutenção > Parâmetros por UF*”\);

  __E__ a UF do Estabelecimento for igual à __GO;__

Aplicar a fórmula abaixo:

\[Base de Cálculo / \(1 – VLR\_ALIQ\_DESTINO/100\) \* \(DIF\_ALIQ\_ICMS/100\)\]

<a id="OLE_LINK58"></a><a id="OLE_LINK59"></a><a id="OLE_LINK60"></a><a id="OLE_LINK94"></a><a id="OLE_LINK95"></a><a id="OLE_LINK96"></a>Valor do DIFAL =       Base de Cálculo 

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-      x    <a id="OLE_LINK68"></a><a id="OLE_LINK69"></a><a id="OLE_LINK70"></a>Diferença de Alíquota ICMS/100

                          1 – Alíquota Interna/100

 

Sendo:

\- Base de Cálculo: o valor a ser utilizado depende da opção de valor escolhida pelo usuário no parâmetro 92

                            \(Parâmetros por UF\), da seguinte forma:

      Se opção = 1 \(“Valor Contábil do Item”\), será utilizado o valor contábil do item \(campo 64 da SAFX08\);

      Se opção = 2 \(“Valor parametrizado no Ferramentas”\), será utilizado o valor parametrizado no módulo

                          Ferramentas, \(*Módulo ferramentas, menu “Parâmetros do Sistema  Parâmetros por Estabelecimento”\)\.*

\- Alíquota Interna: alíquota informada no campo “Valor da Alíquota de Destino” \(campo 63 da SAFX08\);

\- Diferença de Alíquota ICMS: valor da diferença entre as alíquotas interna e interestadual \(campo 44 da SAFX08\);

__Exemplo:__

\- Base de Cálculo: R$ 1\.000,00

\- Alíquota interna: 18

\- Diferença de Alíquota: 6

<a id="OLE_LINK100"></a><a id="OLE_LINK101"></a><a id="OLE_LINK102"></a>Valor do DIFAL __=__ \[ 1\.000,00 / \(1 – 0,18\) \] x 0,06 __=__ \[ 1\.000,00 / 0,82 \] x 0,06 __=__ 1\.219,51 x 0,06 __=__ __73,17__

__Obs¹\.:__ Para maiores informações consultar documento: MTZ\_Calculo\_Diferencial\_Aliquota\_Lancamento\_Automatico\.doc

__Obs²\.:__ O cálculo do DIFAL para o tipo “Material de Consumo – Débito \(extras\)” é exatamente igual ao do tipo “Material de Consumo – Débito”\. A diferença é apenas na recuperação das notas, já que a parametrização de CFOP e Natureza de Operação é feita separadamente\.

__MFS76479__

__RN10\.c__

__Regra do cálculo para Diferencial de Alíquota– Débito e Débito \(extras\) \(UF = MG e PR\)__: __p/ Material de Consumo e Ativo Imobilizado__

<a id="OLE_LINK92"></a><a id="OLE_LINK93"></a>

Regra para obtenção do valor a débito:

__S__e o parâmetro 92 estiver marcado \(menu “*Manutenção > Parâmetros por UF*”\);

  __E__ a UF do Estabelecimento for igual à __MG ou PR;__

Aplicar a fórmula abaixo:

\[\(\(Base de Cálculo – ICMS Origem\) / \(1 – VLR\_ALIQ\_DESTINO/100\) \* \(VLR\_ALIQ\_DESTINO/100\)\] \- ICMS Origem

Valor do DIFAL =           Base de Cálculo \- ICMS Origem

                         __ \[ \(__  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-  __\)__  x  Alíquota Interna/100 __\] __– ICMS Origem

                                       1 – Alíquota Interna/100

Sendo:

\- Base de Cálculo: o valor a ser utilizado depende da opção de valor escolhida pelo usuário no parâmetro 92

                            \(Parâmetros por UF\), da seguinte forma:

      Se opção = 1 \(“Valor Contábil do Item”\), será utilizado o valor contábil do item \(campo 64 da SAFX08\);

      Se opção = 2 \(“Valor parametrizado no Ferramentas”\), será utilizado o valor parametrizado no módulo

                          Ferramentas, \(*Módulo ferramentas, menu “Parâmetros do Sistema  Parâmetros por Estabelecimento”\)\.*

\- Alíquota Interna: alíquota informada no campo “Valor da Alíquota de Destino” \(campo 63 da SAFX08\);

\- ICMS Origem: valor do ICMS do documento fiscal \(campo 43 da SAFX08\)\. Quando este valor não estiver preenchido, 

  será utilizado o valor do campo “80\-ICMS Não oi” \(caso das aquisições em que o ICMS não será creditado,

  como por exemplo as aquisições de Bens cujo crédito será apropriado no controle do CIAP\);

__Exemplo:__

\- Base de Cálculo: R$ 1\.000,00

\- Alíquota interna: 18

\- ICMS Origem: 120,00

Valor do DIFAL __=__ \[ \[\(1\.000,00 – 120,00\) / \(1 – 0,18\)\] x 0,18 \] – 120,00

                         \[ \[ 880,00 / 0,82 \] x 0,18 \] – 120,00

                         \[ 1\.073,17 x 0,18 \] – 120

                          193,17 – 120 = __73,17__

__Obs¹\.:__ Para maiores informações consultar documento: MTZ\_Calculo\_Diferencial\_Aliquota\_Lancamento\_Automatico\.doc

__Obs²\.:__ O cálculo do DIFAL para o tipo “Material de Consumo – Débito \(extras\)” é exatamente igual ao do tipo “Material de Consumo – Débito”\. A diferença é apenas na recuperação das notas, já que a parametrização de CFOP e Natureza de Operação é feita separadamente\.

__RN10\.d__

__Regra do cálculo para Diferencial de Alíquota– \(UF = SP\)__\.

Regra para obtenção do valor a débito:

__S__e o parâmetro 92 estiver marcado \(menu “*Manutenção > Parâmetros por UF*”\);

  __E__ a UF do Estabelecimento for igual à __SP;__

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para SP\.

![](data:image/png;base64,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)

__Alteração \[MFS859953\]: Ajuste da Regra para SP nas Operações de contribuintes optantes pelo simples nacional:__

__Cálculo do Valor Diferencial Alíquota para estabelecimentos de SP para Contribuintes do Simples Nacional:__

__  __

__Cálculo dos Valores__

- __Base de Cálculo Crédito \(Considerada para o cálculo do Valor de Crédito\)__  
Valor Contábil do Item / \(1 – Alíquota Interestadual\)
- __Valor do Crédito:__  
Base de Cálculo Crédito \* Alíquota Interestadual

\[__MFS938348\]__

- __Base de Cálculo Débito \(Considerada para o cálculo do Valor de Débito\)__  
Valor Contábil do Item / \(1 – Alíquota Interna\)
- __Valor do Débito:__  
Base de Cálculo Débito__ __\* Alíquota Interna
- __Valor Cálculado = __Valor do Débito – Valor do Crédito
- __Valor Diferencial Alíquota = Valor Calculado__

__   Observação:__ A mesma base de cálculo deve ser utilizada tanto para o débito quanto para o crédito\.

__A seguir os valores a serem recuperados para os cálculos do Valor de Crédito e do Valor de Débito:__

__ __

__ Definição das Alíquotas__

- __Alíquota Interestadual:__  
Buscar no Campo 42 da tabela SAFX08 \(alíquota do ICMS do item de mercadoria\)\.
- __Alíquota Interna:__  
Buscar no Campo 63 da tabela SAFX08 \(alíquota de destino do item de mercadoria\)\.

__      Regra de Recuperação da Alíquota Interestadual para a fórmula da Base de Cálculo de Crédito:__

	Primeiro verificar se a __Alíquota ICMS__ está preenchida no item de Mercadoria\. Se não estiver preenchido, utilizar a __Parametrização da Alíquota por CFOP e Produto__\. Caso a parametrização não seja encontrada, verificar a __Parametrização da Alíquota Padrão__\.

	Critérios para recuperação da Parametrização da Alíquota por CFOP e Produto :

	\- Tributo = ICMS

	\- UF Origem = 

Se CST for iniciado por 1, 2, 6 ou 7 \(estrangeira\), então considerar UF Origem = “EX”\.

Se CST for iniciado por 0, 3, 4, ,5 8 \(nacional\), então considerar UF Origem = UF do fornecedor\.

	\- UF Destino = UF do Estabelecimento = SP

	\- CFOP do Item de Mercadoria

	\- Produto do Item de Mercadoria

	Critérios para recuperação da Parametrização Padrão:

	\- Tributo = ICMS

	\- UF Origem = 

Se CST for iniciado por 1, 2, 6 ou 7 \(estrangeira\), então considerar UF Origem = “EX”\.

Se CST for iniciado por 0, 3, 4, ,5 8 \(nacional\), então considerar UF Origem = UF do fornecedor\.

	\- UF Destino = UF do Estabelecimento = SP

__      Regra de Recuperação da Alíquota Interna para a fórmula da Base de Cálculo de Débito__:

	Primeiro verificar se a __Alíquota Destino__ está preenchida no item de Mercadoria\. Se não estiver preenchido, utilizar a __Parametrização da Alíquota por CFOP e Produto__\. Caso a parametrização não seja encontrada, verificar a __Parametrização da Alíquota Padrão__\. 

     Critérios para recuperação da Parametrização da Alíquota por CFOP e Produto :

	\- Tributo = ICMS

	\- UF Origem  = UF do Estabelecimento = SP 

	\- UF Destino = UF do Estabelecimento = SP

	\- CFOP do Item de Mercadoria

	\- Produto do Item de Mercadoria

	Critérios para recuperação da Parametrização Padrão:

	\- Tributo = ICMS

\- UF Origem  = UF do Estabelecimento = SP

	\- UF Destino = UF do Estabelecimento = SP

	

__OBS:__ Em caso de não encontrar as alíquotas parametrizadas \(Necessárias para o cálculo dos valores a débito e a crédito\) informar os valores zerados e emitir __mensagem de Log__\.

__Mensagem de Log__: Caso não sejam encontrados os parâmetros da __Alíquota por CFOP e Produto__ ou __Alíquota Padrão __emitir a seguinte mensagem de Erro:

“Para clientes optantes pelo Simples Nacional os parâmetros de Alíquota por CFOP e Produto ou Alíquota Padrão devem estar preenchidos para cálculo do DIFAL SP\.”

__MFS88013__

__MFS859953__

__MFS938348__

__RN10\.e__

__Regra do cálculo para Diferencial de Alíquota– \(UF = ES, BA e SC\)__\.

Regra para obtenção do valor a débito:

__S__e o parâmetro 92 estiver marcado \(menu “*Manutenção > Parâmetros por UF*”\);

  __E__ a UF do Estabelecimento for igual à ES ou BA ou SC__;__

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para ES:

![](data:image/png;base64,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)

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para BA:

![](data:image/png;base64,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)

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para SC:

![](data:image/png;base64,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)

__MFS94495__

__RN10\.f__

__Regra do cálculo para Diferencial de Alíquota– \(UF = PA\)\.__

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado \(menu “Manutenção > Parâmetros por UF”\);

  E a UF do Estabelecimento for igual à PA;

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para PA\.

Valor do DIFAL =    \[Valor da Base de Cálculo – Valor do ICMS x Valor da Alíquota de Destino\] \- Valor do ICMS

                                  1 \- Valor da Alíquota de Destino

__MFS435431__

__RN10\.g__

__Regra do cálculo para Diferencial de Alíquota– \(UF = MA\)\.__

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado \(menu “Manutenção > Parâmetros por UF”\);

  E a UF do Estabelecimento for igual à MA;

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para MA\.

Valor do DIFAL =         Base de Cálculo – Valor do ICMS  
                                   \( \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\)  x  Dif\. de Alíquota ICMS/100  
                                           1 – Alíquota Interna/100

Quando estiver sujeito ao adicional relativo ao FUMACOP:

	

	Será identificado através do campo 263 \(VLR\_FECP\_ALIQ\_ICMS\) descrição: Alíquota FECEP ICMS da tabela SAFX08

Neste caso o Valor da alíquota do FUMACOP será incorporado ao cálculo da fórmula:

Valor do DIFAL =         Base de Cálculo – Valor do ICMS  
                               \( \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \)  x  Dif\. ALiq\.\(FUMACOP\) /100  
                                   1 – Alíquota Interna \+ FUMACOP/100

__MFS519100__

__RN10\.h__

Regra do cálculo para Diferencial de Alíquota– \(UF = RO\)\.

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado \(menu “Manutenção > Parâmetros por UF”\);

  E a UF do Estabelecimento for igual à RO;

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para RO\.

Valor do DIFAL =      Base de Cálculo \- Valor do ICMS

                             \[ \( \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\) x Alíquota Interna/100 \] – Valor do ICMS

                                         1 – Alíquota Interna/100

Vigência a partir de: 01/04/2022

__MFS564128__

__RN10\.i__

__Regra do cálculo para Diferencial de Alíquota– \(UF = AC\)\.__

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado \(menu “Manutenção > Parâmetros por UF”\);

  E a UF do Estabelecimento for igual à AC;

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para AC\.

Valor do DIFAL =      Base de Cálculo \- Valor do ICMS

                             \[ \( \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\) x Alíquota de Destino\] – Valor do ICMS

                                         1 – Alíquota de Destino

Vigência a partir de: 17/03/2023

__MFS569514__

__RN10\.J__

__Regra do cálculo para Diferencial de Alíquota– \(UF = RJ\)\.__

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado \(menu “Manutenção > Parâmetros por UF”\);

  E a UF do Estabelecimento for igual à RJ;

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para RJ\.

Valor do DIFAL =      Base de Cálculo \- Valor do ICMS

                             \[ \( \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\) x Alíquota de Destino\] – Valor do ICMS

                                         1 – Alíquota de Destino

__MFS571687__

__RN10\.k__

__Regra do cálculo para Diferencial de Alíquota– \(UF = SE\)\.__

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado \(menu “Manutenção > Parâmetros por UF”\);

  E a UF do Estabelecimento for igual à SE;

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para SE\.

Valor do DIFAL =      Base de Cálculo \- Valor do ICMS

                             \[ \( \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\) x Alíquota de Destino\] – Valor do ICMS

                                         1 – Alíquota de Destino

Vigência a partir de: 01/04/2022

__MFS571692__

__RN10\.l__

__Regra do cálculo para Diferencial de Alíquota– \(UF = RR\)\.__

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado \(menu “Manutenção > Parâmetros por UF”\);

  E a UF do Estabelecimento for igual à RR;

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para RR\.

Valor do DIFAL =      Base de Cálculo \- Valor do ICMS

                             \[ \( \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\) x Alíquota de Destino\] – Valor do ICMS

                                         1 – Alíquota de Destino

Vigência a partir de: 01/04/2022

__MFS572622__

__RN10\.m__

__Regra do cálculo para Diferencial de Alíquota– \(UF = TO\)\.__

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado \(menu “Manutenção > Parâmetros por UF”\);

  E a UF do Estabelecimento for igual à TO;

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para TO\.

Valor do DIFAL =      Base de Cálculo \- Valor do ICMS

                             \[ \( \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\) x Alíquota de Destino\] – Valor do ICMS

                                         1 – Alíquota de Destino

Vigência a partir de: 29/08/2022

__MFS572711__

__RN10\.n__

__Regra do cálculo para Diferencial de Alíquota– \(UF = AM\)\.__

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado \(menu “Manutenção > Parâmetros por UF”\);

  E a UF do Estabelecimento for igual à AM;

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para AM\.

Valor do DIFAL =      Base de Cálculo \- Valor do ICMS

                             \[ \( \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\) x Alíquota de Destino\] – Valor do ICMS

                                         1 – Alíquota de Destino

Vigência a partir de: 01/04/2023

__MFS573401__

__RN10\.o__

__Regra do cálculo para Diferencial de Alíquota– \(UF = AP\)\.__

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado \(menu “Manutenção > Parâmetros por UF”\);

  E a UF do Estabelecimento for igual à AP;

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para AP\.

Valor do DIFAL =      Base de Cálculo \- Valor do ICMS

                             \[ \( \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\) x Alíquota de Destino\] – Valor do ICMS

                                         1 – Alíquota de Destino

Vigência a partir de: 30/08/2022

__MFS573416__

__RN10\.p__

__Regra do cálculo para Diferencial de Alíquota– \(UF = PE\)\.__

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado \(menu “Manutenção > Parâmetros por UF”\);

  E a UF do Estabelecimento for igual à PE;

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para PE\.

Valor do DIFAL =      Base de Cálculo \- Valor do ICMS

                              \( \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\) x Dif\. de Alíquota ICMS

                                         1 – Alíquota de Destino

Vigência a partir de: 01/04/2017

__MFS573406__

__RN10\.q__

__Regra do cálculo para Diferencial de Alíquota– \(UF = MS\)\.__

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado \(menu “Manutenção > Parâmetros por UF”\);

  E a UF do Estabelecimento for igual à MS;

Aplicar a fórmula abaixo:

Valor Calculado =      Base de Cálculo \- Valor do ICMS

                             \[ \( \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\) x Alíquota de Destino\] – Valor do ICMS

                                         1 – Alíquota de Destino

       Valor Diferencial Alíquota = Valor Calculado 

     Em caso de FECOMP de MS:

       Valor com FECOMP = \[Base de Cálculo – Valor do ICMS  \_\]  \*  Alíquota FECEP ICMS 

                                             1 \- Valor da Alíquota de Destino

       Valor Diferencial Alíquota  = Valor Calculado \- Valor com FECOMP

Vigência a partir de: 01/04/2023

__MFS573412__

__RN10\.r__

__Regra do cálculo para Diferencial de Alíquota– \(UF = PI\)\.__

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado \(menu “Manutenção > Parâmetros por UF”\);

  E a UF do Estabelecimento for igual à PI;

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para PI\.

Valor do DIFAL =      Base de Cálculo \- Valor do ICMS

                             \[ \( \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\) x Alíquota de Destino\] – Valor do ICMS

                                         1 – Alíquota de Destino

Vigência a partir de: 08/03/2023

__MFS576319__

__RN10\.s__

__Regra do cálculo para Diferencial de Alíquota– \(UF = AL\)\.__

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado \(menu “Manutenção > Parâmetros por UF”\);

  E a UF do Estabelecimento for igual à AL;

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para AL\.

Valor do DIFAL =      Base de Cálculo \- Valor do ICMS

                             \[ \( \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\) x Alíquota de Destino\] – Valor do ICMS

                                         1 – Alíquota de Destino

Vigência a partir de: 01/01/2016

__MFS576330__

__RN10\.t__

__Regra do cálculo para Diferencial de Alíquota– \(UF = PB\)\.__

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado \(menu “Manutenção > Parâmetros por UF”\);

  E a UF do Estabelecimento for igual à PB;

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para PB\.

Valor do DIFAL =      Base de Cálculo \- Valor do ICMS

                              \( \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\) x Dif\. de Alíquota ICMS

                                         1 – Alíquota de Destino

Vigência a partir de: 01/04/2020

__MFS593347__

__RN10\.u__

__Regra do cálculo para Diferencial de Alíquota– \(UF = RN\)\.__

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado \(menu “Manutenção > Parâmetros por UF”\);

  E a UF do Estabelecimento for igual à RN;

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para AL\.

Valor do DIFAL =      Base de Cálculo \- Valor do ICMS

                             \[ \( \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\) x Alíquota de Destino\] – Valor do ICMS

                                         1 – Alíquota de Destino

Vigência a partir de: 22/03/2024

__MFS844874__

__RN10\.v__

__Regra do cálculo para Diferencial de Alíquota– \(UF = DF\)\.__

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado \(menu “Manutenção > Parâmetros por UF”\);

  E a UF do Estabelecimento for igual à DF;

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para DF\.

                            Base de Cálculo                                        Base de Cálculo

Valor do Difal: \[ \(\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-  \*  Alíq\. Destin0\) \-  \(\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-  \* Alíq\. Interestadual\) \]

                           1 \- Alíq\. Destino                                    1 \-  Alíq\. Interestadual         

Vigência a partir de: 05/01/2022

__MFS1049811__

__RN11__

__Tratamento do parâmetro “Somente documentos com diferencial”:__

Se o parâmetro “Somente documentos com diferencial” estiver desmarcado

     Todas as notas fiscais devem ser consideradas para o relatório, de acordo com os parâmetros de tela

Senão

      Serão consideradas somente as notas fiscais em que a coluna Valor Diferença da Alíquota do relatório for maior  

      que zero\.

As notas fiscais que devem ser consideradas para calcular a coluna do Valor Diferença da Alíquota, devem ter o campo Valor da Alíquota de Destino \(campo 63 da SAFX08\) ou o campo Diferença Alíquota ICMS \(campo 44 da SAFX08\)  preenchido no item de mercadoria, se o parâmetro Base de Cálculo p/ Dif\. Aliquota\*\* for igual a 1, 2 ou 3\.

Se o parâmetro Base de Cálculo p/ Dif\. Aliquota for igual a 4, o campo Valor Diferença Alíquotas ICMS – Ativo / Material Consumo \(campo 69 da SAFX08\) deve estar preenchido no item de mercadoria\.

__Alteração \[MFS859953\]__

Regra para Pessoa Física e Jurídia optante do Simples Nacional para UF SP:

Considerar na seleção das Notas os clientes optantes pelo Simples Nacional para UF de São Paulo:

No cadastro da tabela SAFX04 o campo 43 \(IND\_SIMPLES\_NAC\) de Enquadramento do Simples Nacional deve estar marcado\.

\*\* A parametrização da Base de Cálculo do Diferencial de Alíquota deve ser realizada no seguinte caminho: Módulo Ferramentas, item de menu Parâmetros do Sistema > Parâmetros por Estabelecimento\.

__MFS593861  
MFS859953__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


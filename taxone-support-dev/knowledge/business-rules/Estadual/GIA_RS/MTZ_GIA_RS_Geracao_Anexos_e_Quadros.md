# MTZ_GIA_RS_Geracao_Anexos_e_Quadros

- **Fonte:** MTZ_GIA_RS_Geracao_Anexos_e_Quadros.docx
- **Modificado:** 2025-05-27
- **Tamanho:** 100 KB

---

 

THOMSON REUTERS

GIA\-RS

Geração – Anexos e Quadros E e A/C \(parcial\)

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4486\-A

Julyana Perrucini

<a id="OLE_LINK65"></a><a id="OLE_LINK66"></a><a id="OLE_LINK67"></a>Rotina para geração automática dos Anexos I\.c e V\.c\.

OS4486\-B

Julyana Perrucini

Inclusão dos itens de serviço na rotina para geração automática dos Anexos I\.c e V\.c\.

CH13432\_2014

Julyana Perrucini

Rotina para geração automática da Ref\. 12 – Débitos por Compensação do Quadro A\.

CH28430\_2014

Julyana Perrucini

Inclusão da Base de Redução do ICMS para Motivo de Ajuste 005\.

OS4803

Julyana Perrucini

Inclusão da recuperação de crédito/débito por transferências através de códigos de ajuste\.

CH13025\_2015

Julyana Perrucini

Alteração da recuperação do código de amparo do Anexo V\.A\.

CH12646\_2015

Julyana Perrucini

Alteração da recuperação do código de amparo do Anexo V\.B\.

OS4803

Julyana Perrucini

Este documento tem como objetivo alterar a geração do Anexo II \- Discriminação dos Créditos Recebidos por Transferências e do Anexo VI \- Discriminação dos Créditos Transferidos da obrigação acessória GIA\-RS, em atendimento a cartilha EFD ICMS IPI \- Simula GIA \- Correspondência entre Quadro A, B e Anexo VII da GIA e a EFD, para que o Quadro A – Resumo das Operações e Prestações represente o valor da EFD por ajuste\(s\) via registro\(s\) C197, conforme alínea “a”, subitem 4\.4\.2, e subitem 4\.4\.2\.1, ambos do Capítulo LI, Título I, da IN DRP N° 045/98\.

OS4818

Julyana Perrucini

Inclusão da recuperação de outros créditos e débitos, inclusive estorno, dos lançamentos de Substituição Tributária a partir do Resumo da Apuração para composição de outros créditos e débitos do Anexo VII\.

CH2412\_2016

Lara Aline

Alteração na geração do Anexo I, ajustando para a recuperação dos valores para importações\.

CH17451\_2016

Lara Aline

Inclusão de regra de geração do Anexo XV, ajustando para a recuperação dos valores para incluir os Lançamentos Créditos/Débitos Especiais – RS\.

CH16323\_2016

Lara Aline

Alteração na geração do Anexo I, ajustando para a recuperação para itens que são bens patrimoniais\.

CH17457\_2016

Julyana Perrucini

Este documento tem como objetivo alterar o preenchimento do Anexo XIV – Outros Créditos – Detalhamento que tem reflexo na Ref\. 06 – Outros Créditos do Quadro A\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00\.a

__Regra Geral – Anexo I, Anexo V e Detalhamentos:__

__Anexo I__

Origem: tabela <a id="OLE_LINK105"></a><a id="OLE_LINK106"></a><a id="OLE_LINK107"></a>est\_res\_extcfo\_uf<a id="OLE_LINK80"></a><a id="OLE_LINK81"></a><a id="OLE_LINK82"></a><a id="OLE_LINK83"></a> <a id="OLE_LINK74"></a><a id="OLE_LINK75"></a><a id="OLE_LINK76"></a>\(Resumo por UF/Extensão CFOP do Módulo Estadual >> Obrigações Acessórias >> Relatórios >> Resumo das Operações\), SAFX07/SAFX08 e TACES51\.

Novo critério de seleção dos Registros de Entrada:

Leitura da tabela de Resumo por UF/Extensão CFOP\. Os CFOP’s gerados no resumo devem obrigatoriamente estar no Cadastro de Situação CFOP por UF \(TACES51\.TXT\)\. 

__\[ALTERADO CH16323\_2016\]__

Seleção das notas fiscais com itens de Bem Patrimonial \(SAFX07/SAFX08\):

   \- somente notas fiscais de entrada;

   \- data fiscal referente ao período da apuração;

   \- classificação do documento = ‘1’ ou ‘3’ \(campo COD\_CLASS\_DOC\_FIS da SAFX07\);

   \- situação da nota <> S \(campo SITUACAO da SAFX07\);

   \- somente notas fiscais que não sejam de transferência = ‘0’ ou nulo \(campo IND\_TRANSF\_CRED da SAFX07\)

   \- somente notas fiscais cuja situação especial seja <> ‘1’, ‘2’, ‘8’ ou que situação especial = ‘nulo’ \(campo IND\_SITUACAO\_ESP da SAFX07\)\.

   \- somente notas fiscais com item\.

   \- somente itens que possuam apenas o Bem Patrimonial preenchido \(campo COD\_BEM da SAFX08\) e que não exista o código do produto preenchido no item \(campo COD\_PRODUTO da SAFX08\)\.

Os CFOP’s recuperados desses itens \(bem patrimonial\) devem obrigatoriamente estar no Cadastro de Situação CFOP por UF \(TACES51\.TXT\)\.<a id="OLE_LINK71"></a><a id="OLE_LINK72"></a><a id="OLE_LINK73"></a>

Recuperar os valores \(contábil, base tributada de ICMS, isenta, outras, valor do IPI, e ICMS\-ST\) totalizados por CFOP,

__\[ALTERADO \- CH16471\-A\_2013\] __com exceção aos CFOPs iniciados com “__3XXX__”, considerar o apenas o valor contábil na geração e preencher o restante dos valores pertinentes ao anexo, com “Zeros”\.

__\[ALTERADO – CH2412\_2016\] __com exceção aos CFOPs iniciados com “__3XXX__”, considerar apenas o valor contábil, base de cálculo, isentas ou não\-tributadas e outras na geração e preencher o restante dos valores pertinentes ao anexo, com “Zeros”\.

Processar os CFOP’s lidos considerando as regras abaixo:

Se os indicadores de Valor Contábil, Base de Cálculo, Isenta, Outras, Excluída do Cadastro de Situação CFOP por UF \(TACES51\) estiverem iguais a ‘N’ então:

	Dar mensagem de erro e não considerar o CFOP no registro\.

__\[ALTERADA – CH24428\_2013\]__

__\[ALTERADA – CH2746\_2014\]__

__\[ALTERADA – OS4486\-A\]__

Se __indicador de Cálculo do Valor Excluído__ = ‘__1’__ __\(valor contabil\),__ então:

          Campo VLR\_CONTABIL        = vlr\_contabil;

          Campo VLR\_BASE\_CALC      = <a id="OLE_LINK4"></a><a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a>vlr\_base\_calc;

          Campo VLR\_ISENTA              = <a id="OLE_LINK8"></a><a id="OLE_LINK9"></a><a id="OLE_LINK10"></a><a id="OLE_LINK11"></a>vlr\_isenta;

          Campo VLR\_OUTRAS            = <a id="OLE_LINK12"></a><a id="OLE_LINK13"></a><a id="OLE_LINK14"></a><a id="OLE_LINK15"></a>vlr\_outras;

          Campo VLR\_IMPORT\_EXCL =  <a id="OLE_LINK22"></a><a id="OLE_LINK23"></a><a id="OLE_LINK24"></a> Soma do campo Valor do detalhamento do Anexo I\.C\.

          Campo VALOR DO CRÉDITO / DEBITO = manter a regra atual\.

	Gera mensagem se o indicador de Valor Contábil for N ou indicador de Excluída for N\.

Se __indicador de Cálculo do Valor Excluído__ = ‘__2’ \(sem importâncias excluídas\)__, então:

          Campo VLR\_CONTABIL         = vlr\_contabil;

          Campo VLR\_BASE\_CALC       = vlr\_base\_calc;

          Campo VLR\_ISENTA               = vlr\_isenta;

          Campo VLR\_OUTRAS             = vlr\_outras;

          Campo VLR\_IMPORT\_EXCL  = 0;

          VALOR DO CRÉDITO / DEBITO = manter a regra atual\.

Gera mensagem se o Valor Contábil for diferente de \(Base de Cálculo \+ Isenta \+ Outras\) e Valor Contábil for menor que \(Base de Cálculo \+ Isenta \+ Outras\) dividido por 2\.

Se __indicador de Cálculo do Valor Excluído__ = ‘__3’__ __\(regime de substituição tributária\)__, então:

          VLR\_IMPORT\_EXCL =  Soma do campo Valor do detalhamento do Anexo I\.C\.

          VLR\_CONTABIL         = vlr\_contabil – VLR\_IMPORT\_EXCL

          VLR\_BASE\_CALC      = vlr\_base\_calc;

          VLR\_ISENTA              = vlr\_isenta;

          VLR\_OUTRAS            = vlr\_outras;

         Se o Indicador de ICMS/OUTRAS \(flag ICMS Retido/Outras\) = 'S' então:

             VLR\_OUTRAS = VLR\_OUTRAS \- vlr\_icms\_retido;

             VALOR DO CRÉDITO / DEBITO = manter a regra atual\.

Gera mensagem se o Valor Contábil for diferente de \(Base de Cálculo \+ Isenta \+ Outras \+ ImportExcluídas\) e 

                                    Valor Contábil menor que \(Base de Cálculo\+ Isenta\+ Outras\+ ImportExcluídas\) dividido por 2\.

Se __indicador de Cálculo do Valor Excluído__ = __‘4’__ __\(natureza de operação\)__, então:

          VLR\_CONTABIL   = vlr\_contabil;

          VLR\_BASE\_CALC = vlr\_base\_calc;

          VLR\_ISENTA         = vlr\_isenta;

  VLR\_OUTRAS       = vlr\_outras \- vlr\_icms\_retido;

  VALOR DO CRÉDITO / DEBITO = manter a regra atual\.

Verifica se o CFOP que está sendo processado possui Natureza de Operação parametrizada na opção \(Importâncias Excluídas → Por Extensão CFOP\)\. 

Se não existir parametrização, os valores se mantêm inalterados e o valor das Importâncias Excluídas fica zero:

    VLR\_CONTABIL    = vlr\_contabil;

VLR\_BASE\_CALC  = vlr\_base\_calc;

VLR\_ISENTA          = vlr\_isenta;

    VLR\_OUTRAS        = vlr\_outras;

    VLR\_IMPORT\_EXCL = 0;

	    VALOR DO CRÉDITO / DEBITO = manter a regra atual\.

Se existir parametrização, faz a recuperação dos valores a serem excluídos da seguinte forma:

Leitura da tabela de Resumo por UF/Extensão CFOP para o CFOP que está sendo processado\. Recupera os valores \(contábil, base tributada de ICMS, isenta, outras\) referentes às Naturezas de Operações parametrizadas na opção de Importâncias Excluídas\.

Subtrai os valores de base tributada de ICMS, isenta e outras do total calculado para o CFOP:

 VLR\_BASE\_CALC = VLR\_BASE\_CALC \- BASE\_EXCL1;

 VLR\_ISENTA        = VLR\_ISENTA   \- BASE\_EXCL2;

 VLR\_OUTRAS      = VLR\_OUTRAS  \- BASE\_EXCL3;

 VALOR DO CRÉDITO / DEBITO = manter a regra atual\.

Calcula o valor das Importâncias Excluídas para o CFOP, considerando o valor contábil parametrização:

            VLR\_IMPORT\_EXCL := Soma do campo Valor do detalhamento do Anexo I\.C\.

  Se P\_Ind\_icmss\_outras = 'N' então  VLR\_IMPORT\_EXCL :=  Soma do campo Valor do detalhamento do Anexo I\.C\.

Gera mensagem se o Valor Contábil for diferente de \(Base de Cálculo \+ Isenta \+ Outras \+ ImportExcluídas\) e                                     Valor Contábil menor que \(Base de Cálculo\+ Isenta\+ Outras\+ ImportExcluídas\) dividido por 2\.

Se o indicador de Valor Contábil do Cadastro de Situação CFOP por UF for igual a ‘N’ e o valor contábil gerado segundo as regras acima, for diferente de zero, então:

	Dar mensagem de erro\.

               Zera valor contábil  \(VLR\_CONTABIL = 0;\)

Se o indicador de Base de Cálculo do Cadastro de Situação CFOP por UF \(EST\_UF\_CFO\_SIT\) for igual a ‘N’ e o valor da base de cálculo, gerado segundo as regras acima, for diferente de zero, então:

	Dar mensagem de erro\.

               Zera valor da base de cálculo  \(VLR\_BASE\_CALC = 0;\)

Se o indicador de Isenta do Cadastro de Situação CFOP por UF \(EST\_UF\_CFO\_SIT\) for igual a ‘N’ e o valor de isentas, gerado segundo as regras acima, for diferente de zero, então:

	Dar mensagem de erro\.

               Zera valor de isentas  \(VLR\_ISENTA = 0;\)

Se o indicador de Outras do Cadastro de Situação CFOP por UF \(EST\_UF\_CFO\_SIT\) for igual a ‘N’ e o valor de outras, gerado segundo as regras acima, for diferente de zero, então:

	Dar mensagem de erro\.

               Zera valor de Outras \(VLR\_OUTRAS = 0;\)

Se o indicador de Excluídas do Cadastro de Situação CFOP por UF \(EST\_UF\_CFO\_SIT\) for igual a ‘N’ e o valor de importâncias excluídas, gerado segundo as regras acima, for diferente de zero, então:

	Dar mensagem de erro\.

               Zera valor de importâncias excluídas \(VLR\_IMPORT\_EXCL = 0;\)

__\[ALTERADO – CH22403\_2012\]__

Na geração deste anexo devem ser considerados os CFOP = ‘1601’, ’1602’, ’1603’, ’1604’, ’1605’, mesmo se os indicadores de Valor Contábil, Base de Cálculo, Isenta, Outras, Excluída do Cadastro de Situação CFOP por UF \(TACES51\) estiverem iguais a ‘N’\. 

__Anexo V__

Origem: tabela est\_res\_extcfo\_uf \(Resumo por UF/Extensão CFOP do Módulo Estadual >> Obrigações Acessórias >> Relatórios >> Resumo das Operações\) e TACES51\.

Novo critério de seleção dos Registros de Saída:

Leitura da tabela de Resumo por UF/Extensão CFOP\. Os CFOP’s gerados no resumo devem obrigatoriamente estar no Cadastro de Situação CFOP por UF \(TACES51\.TXT\)\.

Recuperar os valores \(contábil, base tributada de ICMS, isenta, outras, valor do IPI, e ICMS\-ST\) totalizados por CFOP\.

Processar os CFOP’s lidos considerando as regras abaixo:

Se os indicadores de Valor Contábil, Base de Cálculo, Isenta, Outras, Excluída do Cadastro de Situação CFOP por UF \(TACES51\) estiverem iguais a ‘N’ então:

	Dar mensagem de erro e não considerar o CFOP no registro\.

__\[ALTERADA – CH24428\_2013\]__

__\[ALTERADA – CH2746\_2014\]__

__\[ALTERADA – OS4486\-A\]__

Se __indicador de Cálculo do Valor Excluído__ = ‘__1’__ __\(valor contabil\),__ então:

          Campo VLR\_CONTABIL        = vlr\_contabil;

          Campo VLR\_BASE\_CALC      = vlr\_base\_calc;

          Campo VLR\_ISENTA              = vlr\_isenta;

          Campo VLR\_OUTRAS            = vlr\_outras;

          Campo VLR\_IMPORT\_EXCL =   Soma do campo Valor do detalhamento do Anexo V\.C\.

          Campo VALOR DO CRÉDITO / DEBITO = manter a regra atual\.

	Gera mensagem se o indicador de Valor Contábil for N ou indicador de Excluída for N\.

Se __indicador de Cálculo do Valor Excluído__ = ‘__2’ \(sem importâncias excluídas\)__, então:

          Campo VLR\_CONTABIL         = vlr\_contabil;

          Campo VLR\_BASE\_CALC       = vlr\_base\_calc;

          Campo VLR\_ISENTA               = vlr\_isenta;

          Campo VLR\_OUTRAS             = vlr\_outras;

          Campo VLR\_IMPORT\_EXCL  = 0;

          VALOR DO CRÉDITO / DEBITO = manter a regra atual\.

Gera mensagem se o Valor Contábil for diferente de \(Base de Cálculo \+ Isenta \+ Outras\) e Valor Contábil for menor que \(Base de Cálculo \+ Isenta \+ Outras\) dividido por 2\.

Se __indicador de Cálculo do Valor Excluído__ = ‘__3’__ __\(regime de substituição tributária\)__, então:

          VLR\_IMPORT\_EXCL = Soma do campo Valor do detalhamento do Anexo V\.C\.          VLR\_CONTABIL         = vlr\_contabil – VLR\_IMPORT\_EXCL

          VLR\_BASE\_CALC      = vlr\_base\_calc;

          VLR\_ISENTA              = vlr\_isenta;

          VLR\_OUTRAS            = vlr\_outras;

         Se o Indicador de ICMS/OUTRAS \(flag ICMS Retido/Outras\) = 'S' então:

             VLR\_OUTRAS = VLR\_OUTRAS \- vlr\_icms\_retido;

             VALOR DO CRÉDITO / DEBITO = manter a regra atual\.

Gera mensagem se o Valor Contábil for diferente de \(Base de Cálculo \+ Isenta \+ Outras \+ ImportExcluídas\) e 

                                    Valor Contábil menor que \(Base de Cálculo\+ Isenta\+ Outras\+ ImportExcluídas\) dividido por 2\.

Se __indicador de Cálculo do Valor Excluído__ = __‘4’__ __\(natureza de operação\)__, então:

          VLR\_CONTABIL   = vlr\_contabil;

          VLR\_BASE\_CALC = vlr\_base\_calc;

          VLR\_ISENTA         = vlr\_isenta;

  VLR\_OUTRAS       = vlr\_outras;

  VALOR DO CRÉDITO / DEBITO = manter a regra atual\.

Verifica se o CFOP que está sendo processado possui Natureza de Operação parametrizada na opção \(Importâncias Excluídas → Por Extensão CFOP\)\. 

Se não existir parametrização, os valores se mantêm inalterados e o valor das Importâncias Excluídas fica zero:

    VLR\_CONTABIL    = vlr\_contabil;

VLR\_BASE\_CALC  = vlr\_base\_calc;

VLR\_ISENTA          = vlr\_isenta;

    VLR\_OUTRAS        = vlr\_outras;

    VLR\_IMPORT\_EXCL = 0;

	    VALOR DO CRÉDITO / DEBITO = manter a regra atual\.

Se existir parametrização, faz a recuperação dos valores a serem excluídos da seguinte forma:

Leitura da tabela de Resumo por UF/Extensão CFOP para o CFOP que está sendo processado\. Recupera os valores \(contábil, base tributada de ICMS, isenta, outras\) referentes às Naturezas de Operações parametrizadas na opção de Importâncias Excluídas\.

Subtrai os valores de base tributada de ICMS, isenta e outras do total calculado para o CFOP:

 VLR\_BASE\_CALC = VLR\_BASE\_CALC \- BASE\_EXCL1;

 VLR\_ISENTA        = VLR\_ISENTA   \- BASE\_EXCL2;

 VLR\_OUTRAS      = VLR\_OUTRAS  \- BASE\_EXCL3;

 VALOR DO CRÉDITO / DEBITO = manter a regra atual\.

Calcula o valor das Importâncias Excluídas para o CFOP, considerando o valor contábil parametrização:

            VLR\_IMPORT\_EXCL := 

  Se P\_Ind\_icmss\_outras = 'N' então  VLR\_IMPORT\_EXCL :=  Soma do campo Valor do detalhamento do Anexo V\.C\.

Gera mensagem se o Valor Contábil for diferente de \(Base de Cálculo \+ Isenta \+ Outras \+ ImportExcluídas\) e                                     Valor Contábil menor que \(Base de Cálculo\+ Isenta\+ Outras\+ ImportExcluídas\) dividido por 2\.

Se o indicador de Valor Contábil do Cadastro de Situação CFOP por UF for igual a ‘N’ e o valor contábil gerado segundo as regras acima, for diferente de zero, então:

	Dar mensagem de erro\.

               Zera valor contábil  \(VLR\_CONTABIL = 0;\)

Se o indicador de Base de Cálculo do Cadastro de Situação CFOP por UF \(EST\_UF\_CFO\_SIT\) for igual a ‘N’ e o valor da base de cálculo, gerado segundo as regras acima, for diferente de zero, então:

	Dar mensagem de erro\.

               Zera valor da base de cálculo  \(VLR\_BASE\_CALC = 0;\)

Se o indicador de Isenta do Cadastro de Situação CFOP por UF \(EST\_UF\_CFO\_SIT\) for igual a ‘N’ e o valor de isentas, gerado segundo as regras acima, for diferente de zero, então:

	Dar mensagem de erro\.

               Zera valor de isentas  \(VLR\_ISENTA = 0;\)

Se o indicador de Outras do Cadastro de Situação CFOP por UF \(EST\_UF\_CFO\_SIT\) for igual a ‘N’ e o valor de outras, gerado segundo as regras acima, for diferente de zero, então:

	Dar mensagem de erro\.

               Zera valor de Outras \(VLR\_OUTRAS = 0;\)

Se o indicador de Excluídas do Cadastro de Situação CFOP por UF \(EST\_UF\_CFO\_SIT\) for igual a ‘N’ e o valor de importâncias excluídas, gerado segundo as regras acima, for diferente de zero, então:

	Dar mensagem de erro\.

               Zera valor de importâncias excluídas \(VLR\_IMPORT\_EXCL = 0;\)

__Anexo I\.C__

<a id="OLE_LINK77"></a><a id="OLE_LINK78"></a><a id="OLE_LINK79"></a>

Origem: SAFX07/08/09, SAFX2013, TACES51, TACES86 e TACES87\.

<a id="OLE_LINK116"></a><a id="OLE_LINK117"></a><a id="OLE_LINK118"></a>Seleção das notas fiscais \(SAFX07/SAFX08/SAFX09\):

   \- somente notas fiscais de entrada;

   \- data fiscal referente ao período da apuração;

   \- classificação do documento = ‘1’ ou ‘3’ \(campo COD\_CLASS\_DOC\_FIS da SAFX07\);

<a id="OLE_LINK113"></a><a id="OLE_LINK114"></a><a id="OLE_LINK115"></a>   \- situação da nota <> S \(campo SITUACAO da SAFX07\);

   \- somente notas fiscais com item\.

__\[ALTERADA – OS4486\-B\]/\[ALETARADA – CH28430\_2014\]__

<a id="OLE_LINK206"></a><a id="OLE_LINK207"></a><a id="OLE_LINK208"></a>Recuperação dos registros:

   <a id="OLE_LINK127"></a><a id="OLE_LINK128"></a><a id="OLE_LINK129"></a><a id="OLE_LINK130"></a>\- parametrização da TACES51 – verifica se há indicação de importância excluída para o CFOP destacado no item da nota fiscal, ou seja, <a id="OLE_LINK138"></a><a id="OLE_LINK139"></a><a id="OLE_LINK140"></a>só irá gerar os registros para a tabela do Anexo I\.C quando os CFOPs estiverem com campo Cálculo Valor Excluído igual a 1, 3 ou 4 na TACES, quando for igual a 0 indica que os campos estão bloqueados para a digitação e este CFOP não será considerado na geração do meio magnético, quando for igual a 2 não haverá cálculo de importâncias a excluir do valor adicionado, então será gerado apenas no registro principal\.

   \- parametrização da TACES86 – verifica se há indicação do Código de Ajuste para os CFOPs recuperados, caso não houver parametrização ou a data de apuração não estiver dentro data de validade os registros serão desconsiderados\.

- <a id="OLE_LINK135"></a><a id="OLE_LINK136"></a><a id="OLE_LINK137"></a>__Atenção:__ o campo Código de Ajuste não deverá ser gravado quando o campo “Data Fim” da TACES86 estiver preenchida e for menor que a data de apuração parametrizada, somente gerar se houver nova parametrização para o CFOP ou se o período de apuração parametrizado estiver dentro da faixa Data Início e Data Fim\.

   \- parametrização da TACES87 – verifica para os CFOPs com Código de Ajuste se há campo Recuperar Motivo, então:

- <a id="OLE_LINK141"></a><a id="OLE_LINK142"></a>Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 1, <a id="OLE_LINK154"></a><a id="OLE_LINK155"></a><a id="OLE_LINK156"></a>verificar se o campo Vlr ICMSS <a id="OLE_LINK143"></a><a id="OLE_LINK144"></a><a id="OLE_LINK145"></a><a id="OLE_LINK146"></a>do item da nota fiscal \(campo VLR\_SUBST\_ICMS da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- <a id="OLE_LINK151"></a><a id="OLE_LINK152"></a><a id="OLE_LINK153"></a>Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 2, verificar se o campo Vlr ICMSS do item da nota fiscal \(campo VLR\_SUBST\_ICMS da SAFX08\), <a id="OLE_LINK157"></a><a id="OLE_LINK158"></a><a id="OLE_LINK159"></a>B\. Isenta ICMSS do item da nota fiscal \(campo <a id="OLE_LINK147"></a><a id="OLE_LINK148"></a><a id="OLE_LINK149"></a><a id="OLE_LINK150"></a>BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 2 da SAFX08\) ou B<a id="OLE_LINK166"></a><a id="OLE_LINK167"></a><a id="OLE_LINK168"></a><a id="OLE_LINK169"></a>\. Outras ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 3 da SAFX08\) <a id="OLE_LINK160"></a><a id="OLE_LINK161"></a><a id="OLE_LINK162"></a>são maiores que zero, caso contrário desconsiderar registros\.
- <a id="OLE_LINK163"></a><a id="OLE_LINK164"></a><a id="OLE_LINK165"></a>Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 3, verificar se o campo B\. Isenta ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 2 da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- <a id="OLE_LINK170"></a><a id="OLE_LINK171"></a>Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 4, verificar se o campo B\. Outras ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 3 da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- <a id="OLE_LINK172"></a><a id="OLE_LINK173"></a><a id="OLE_LINK178"></a><a id="OLE_LINK179"></a><a id="OLE_LINK180"></a><a id="OLE_LINK181"></a>Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 1, verificar se o campo Vlr IPI do item da nota fiscal \(campo VLR\_IPI da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- <a id="OLE_LINK176"></a><a id="OLE_LINK177"></a>Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 2, verificar se o campo Vlr IPI do item da nota fiscal \(campo VLR\_IPI\), B\. Isenta IPI <a id="OLE_LINK174"></a><a id="OLE_LINK175"></a>\(campo BASE\_IPI e TRIB\_IPI = 2 da SAFX08\) ou B\. Outras IPI \(campo BASE\_IPI e TRIB\_IPI = 3 da SAFX08\) são maiores que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 3, verificar se o campo B\. Isenta IPI \(campo BASE\_IPI e TRIB\_IPI = 2 da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 4, verificar se o campo B\. Outras IPI \(campo BASE\_IPI e TRIB\_IPI = 3 da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 003 e campo Recuperar Motivo da TACES87 igual a 1, verificar se o campo <a id="OLE_LINK182"></a><a id="OLE_LINK183"></a><a id="OLE_LINK184"></a><a id="OLE_LINK185"></a><a id="OLE_LINK186"></a>Vlr Frete do item da nota fiscal \(campo VLR\_FRETE da SAFX08\) é maior que zero e o produto cadastrado no item da nota fiscal é classificado como Material \(Uso ou Consumo\) ou Ativo Imobilizado \(campo CLAS\_ITEM igual a 07 ou 08 da SAFX2013\), caso contrário desconsiderar registros\.
- <a id="OLE_LINK189"></a><a id="OLE_LINK190"></a><a id="OLE_LINK191"></a><a id="OLE_LINK187"></a><a id="OLE_LINK188"></a>Se o CFOP com Código de Ajuste igual a 003 e campo Recuperar Motivo da TACES87 igual a 2, verificar se o campo Vlr Frete do item da nota fiscal \(campo VLR\_FRETE da SAFX08\) <a id="OLE_LINK201"></a><a id="OLE_LINK202"></a>é maior que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 004 e campo Recuperar Motivo da TACES87 igual a 1, verificar se o campo Vlr Cont\. Item \(campo VLR\_CONTAB\_ITEM da SAFX08\) é menor que a <a id="OLE_LINK192"></a><a id="OLE_LINK193"></a><a id="OLE_LINK194"></a>Base ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 1 da SAFX08\), e ainda o Valor Total \(campo VLR\_TOT da SAFX09\) é menor que a Base ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 1 da SAFX09\), caso contrário desconsiderar registros\.
- <a id="OLE_LINK203"></a><a id="OLE_LINK204"></a><a id="OLE_LINK205"></a>Se o CFOP com Código de Ajuste igual a 005 e campo Recuperar Motivo da TACES87 igual a 1, verificar se o campo Base ICMS <a id="OLE_LINK195"></a><a id="OLE_LINK196"></a><a id="OLE_LINK197"></a>do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 1 da SAFX08 e SAFX09\), <a id="OLE_LINK198"></a><a id="OLE_LINK199"></a><a id="OLE_LINK200"></a>B\. Isenta ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 2 da SAFX08 e SAFX09\), B\. Outras ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 3 da SAFX08 e SAFX09\) ou B\. Redução ICMS \(campo BASE\_ICMS e TRIB\_ICMS = 4 da SAFX08 e SAFX09\) são maiores que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 006 e campo Recuperar Motivo da TACES87 igual a 1, não iremos tratar no momento, indicaremos de que será feito de forma manual tanto na TACES quanto no manual operacional\.
- __Atenção:__ o campo Valor \(de acordo com o Recuperar Motivo parametrizado\) não deverá ser gravado quando o campo “Data Fim” da TACES87 estiver preenchida e for menor que a data de apuração parametrizada, somente gerar se houver nova parametrização para o Código de Ajuste/Recuperar Motivo ou se o período de apuração parametrizado estiver dentro da faixa Data Início e Data Fim\.

__\[ALTERADA – CH13025\_2015\]__

__Anexo V\.A__

Recuperação dos registros:

   \- parametrização da TACES21 – verifica código de amparo/ texto/ ocorrência de validade inicial e final correspondente ao período de apuração\.

__\[ALTERADA – CH12646\_2015\]__

__Anexo V\.B__

Recuperação dos registros:

   \- parametrização da TACES21 – verifica código de amparo/ texto/ ocorrência de validade inicial e final correspondente ao período de apuração\.

__Anexo V\.C__

Origem: SAFX07/08/09, SAFX2013, TACES51, TACES86 e TACES87\.

Seleção das notas fiscais \(SAFX07/SAFX08/SAFX09\):

   \- somente notas fiscais de saídas;

   \- data fiscal referente ao período da apuração;

   \- classificação do documento = ‘1’ ou ‘3’ \(campo COD\_CLASS\_DOC\_FIS da SAFX07\);

   \- situação da nota <> S \(campo SITUACAO da SAFX07\);

   \- somente notas fiscais com item\.

__\[ALTERADA – OS4486\-B\]__

Recuperação dos registros:

   \- parametrização da TACES51 – verifica se há indicação de importância excluída para o CFOP destacado no item da nota fiscal, ou seja, só irá gerar os registros para a tabela do Anexo I\.C quando os CFOPs estiverem com campo Cálculo Valor Excluído igual a 1, 3 ou 4 na TACES, quando for igual a 0 indica que os campos estão bloqueados para a digitação e este CFOP não será considerado na geração do meio magnético, quando for igual a 2 não haverá cálculo de importâncias a excluir do valor adicionado, então será gerado apenas no registro principal\.

   \- parametrização da TACES86 – verifica se há indicação do Código de Ajuste para os CFOPs recuperados, caso não houver parametrização ou a data de apuração não estiver dentro data de validade os registros serão desconsiderados\.

- __Atenção:__ o campo Código de Ajuste não deverá ser gravado quando o campo “Data Fim” da TACES86 estiver preenchida e for menor que a data de apuração parametrizada, somente gerar se houver nova parametrização para o CFOP ou se o período de apuração parametrizado estiver dentro da faixa Data Início e Data Fim\.

   \- parametrização da TACES87 – verifica para os CFOPs com Código de Ajuste se há campo Recuperar Motivo, então:

- Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 1, verificar se o campo Vlr ICMSS do item da nota fiscal \(campo VLR\_SUBST\_ICMS da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 2, verificar se o campo Vlr ICMSS do item da nota fiscal \(campo VLR\_SUBST\_ICMS da SAFX08\), B\. Isenta ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 2 da SAFX08\) ou B\. Outras ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 3 da SAFX08\) são maiores que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 3, verificar se o campo B\. Isenta ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 2 da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 4, verificar se o campo B\. Outras ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 3 da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 1, verificar se o campo Vlr IPI do item da nota fiscal \(campo VLR\_IPI da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 2, verificar se o campo Vlr IPI do item da nota fiscal \(campo VLR\_IPI\), B\. Isenta IPI \(campo BASE\_IPI e TRIB\_IPI = 2 da SAFX08\) ou B\. Outras IPI \(campo BASE\_IPI e TRIB\_IPI = 3 da SAFX08\) são maiores que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 3, verificar se o campo B\. Isenta IPI \(campo BASE\_IPI e TRIB\_IPI = 2 da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 4, verificar se o campo B\. Outras IPI \(campo BASE\_IPI e TRIB\_IPI = 3 da SAFX08\) é maior que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 004 e campo Recuperar Motivo da TACES87 igual a 1, verificar se o campo Vlr Cont\. Item \(campo VLR\_CONTAB\_ITEM da SAFX08\) é menor que a Base ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 1 da SAFX08\), e ainda o Valor Total \(campo VLR\_TOT da SAFX09\) é menor que a Base ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 1 da SAFX09\), caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 005 e campo Recuperar Motivo da TACES87 igual a 1, verificar se o campo Base ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 1 da SAFX08 e SAFX09\), B\. Isenta ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 2 da SAFX08 e SAFX09\) ou B\. Outras ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 3 da SAFX08 e SAFX09\) são maiores que zero, caso contrário desconsiderar registros\.
- Se o CFOP com Código de Ajuste igual a 006 e campo Recuperar Motivo da TACES87 igual a 1, não iremos tratar no momento, indicaremos de que será feito de forma manual tanto na TACES quanto no manual operacional\.
- __Atenção:__ o campo Valor \(de acordo com o Recuperar Motivo parametrizado\) não deverá ser gravado quando o campo “Data Fim” da TACES87 estiver preenchida e for menor que a data de apuração parametrizada, somente gerar se houver nova parametrização para o Código de Ajuste/Recuperar Motivo ou se o período de apuração parametrizado estiver dentro da faixa Data Início e Data Fim\.

OS3402

CH16471\_2013

CH16471\-A\_2013

CH24428\_2013

CH2746\_2014

OS4486\-A

OS4486\-B

CH28430\_2014

CH2412\_2016

CH16323\_2016

RN00\.b

__Regra Geral – Anexo II e Anexo VI:__

Anexo II

__\[ALTERADA – OS4803\]__

__*Se Tratamento por Código de Ajuste:*__

Origem: SAFX07/08, SAFX113\.

Seleção das notas fiscais com códigos de ajuste:

   \- serão recuperadas as SAFX113 – Ajustes/ Outros Valores do Lançamento Fiscal vinculadas a uma SAFX07/08 – Documento Fiscal de Mercadoria desde que o campo 13 – Código de Ajuste da SAFX113 esteja parametrizado na tela de Transferências / Recebimentos – Por Código de Ajuste e com o campo Anexo = Anexo II \- Discriminação dos Créditos Recebidos por Transferências;

   \- somente notas fiscais de entrada;

   \- situação da nota <> S \(campo SITUACAO da SAFX07\);

   \- data fiscal referente ao período da apuração;

__Senão,__

__*Se Tratamento por Documento Fiscal:*__

Origem: SAFX07/08, SAFX2012, SAFX04, TACES21\.

Seleção das notas fiscais \(SAFX07/SAFX08/SAFX04/TACES21\):

   \- somente notas fiscais de entrada;

   \- data fiscal referente ao período da apuração;

   \- classificação do documento <> ‘2’ \(campo COD\_CLASS\_DOC\_FIS da SAFX07\);

   \- situação da nota <> S \(campo SITUACAO da SAFX07\);

   \- somente notas fiscais com item;

   \- somente nota fiscal transferência de crédito/ débito = ‘1’ \(campo IND\_TRANSF\_CRED da SAFX07\);

   \- com CFOPs iniciados com ‘1’ \(campo COD\_CFO da SAFX08\);

   \- com remetente vinculado a NF com IE preenchida no cadastro \(campo INSC\_ESTADUAL da SAFX04\);

   \- com código de amparo iniciados com ‘2’ \(campo COD\_AMPARO da SAFX07\)\.

   \- o código de amparo escriturado na nota fiscal deve ter incidência de ICMS = S \(campo IND\_INCIDE\_ICMS da DWT\_AMPARO\_LEGAL\)\.

As seleções devem ser agrupadas por estabelecimento, mês/ ano da apuração, inscrição estadual do remetente e pelo código de amparo\.

Ou seja, se o usuário optar pela geração a partir dos códigos de ajuste, será considerado apenas os valores a partir da SAFX113\.

Anexo VI

__\[ALTERADA – OS4803\]__

__*Se Tratamento por Código de Ajuste:*__

Origem: SAFX07/08, SAFX113\.

Seleção das notas fiscais com códigos de ajuste:

   \- serão recuperadas as SAFX113 – Ajustes/ Outros Valores do Lançamento Fiscal vinculadas a uma SAFX07/08 – Documento Fiscal de Mercadoria desde que o campo 13 – Código de Ajuste da SAFX113 esteja parametrizado na tela de Transferências / Recebimentos – Por Código de Ajuste e com o campo Anexo = Anexo VI \- Discriminação dos Créditos Transferidos;

   \- somente notas fiscais de saída;

   \- situação da nota <> S \(campo SITUACAO da SAFX07\);

   \- data fiscal referente ao período da apuração;

__Senão,__

__*Se Tratamento por Documento Fiscal:*__

Origem: SAFX07/08, SAFX2012, SAFX04, TACES21\.

Seleção das notas fiscais \(SAFX07/SAFX08/TACES21\):

   \- somente notas fiscais de saída;

   \- data fiscal referente ao período da apuração;

   \- classificação do documento <> ‘2’ \(campo COD\_CLASS\_DOC\_FIS da SAFX07\);

   \- situação da nota <> S \(campo SITUACAO da SAFX07\);

   \- somente notas fiscais com item;

   \- somente nota fiscal transferência de crédito/ débito = ‘1’ \(campo IND\_TRANSF\_CRED da SAFX07\);

   \- com CFOPs iniciados com ‘5’ \(campo COD\_CFO da SAFX08\);

   \- com destinatário vinculado a NF com IE preenchida no cadastro \(campo INSC\_ESTADUAL da SAFX04\);

   \- com código de amparo iniciados com ‘2’ \(campo COD\_AMPARO da SAFX07\)\.

   \- o código de amparo escriturado na nota fiscal deve ter incidência de ICMS = S \(campo IND\_INCIDE\_ICMS da DWT\_AMPARO\_LEGAL\)\.

As seleções devem ser agrupadas por estabelecimento, mês/ ano da apuração, inscrição estadual do destinatário e pelo código de amparo\.

Ou seja, se o usuário optar pela geração a partir dos códigos de ajuste, será considerado apenas os valores a partir da SAFX113\.

__*Observações: *__

- *Essa regra será aplicada para empresas com IEU, em que serão considerados os dados do estabelecimento centralizador consolidando os centralizados\.*
- *Os campos em tela são obrigatórios para estabelecimento, mês/ ano da apuração, inscrição estadual do remetente ou destinatário e código de amparo, então caso não haja o preenchimento na origem não será considerado o registro a ser preenchido na manutenção\.*

__*ATENÇÃO: *__

*A regra criada para Transferências por Código de Ajuste é específica para contribuintes que possuem grupo de fornecedores para os quais existe a extensão de incentivo fiscal do ICMS nas vendas de determinados insumos aos contribuintes a cada mês, esta venda tem o ICMS Diferido, ou seja, não é pago pelo fornecedor, então por esse motivo será feito a recuperação por código de ajuste ou se não houver parametrização para este, pelas notas fiscais\.*

*Nesse conceito, o crédito não é proveniente de lançamento de notas fiscais, mas de lançamento na apuração do ICMS:*

*1 Cada fornecedor emite uma Nota Fiscal de Transferência de Crédito do ICMS para o contribuinte sob o fundamento conceitual de "Sistemistas";   
2 Esta Nota Fiscal é declarada na EFD\-Fiscal como lançamento de "Ajustes na apuração do ICMS" e tem o valor sumarizado por mês \(valor total do crédito transferido\);  
3 NA GIA, ANEXO II e VI, o contribuinte deve declarar em tela específica de forma individualizada as I/E dos fornecedores e as respectivas notas fiscais de transferência de crédito do ICMS\.*

OS4803

RN00\.c

__Regra Geral – Anexo VII__

__\[ALTERADA – OS4818\]__

__*Seleção para composição de “Outros Créditos” do Anexo VII*__

Origem: Lançamentos Complementares – Apuração ICMS Subst\. Tributária – Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única \(tabela item\_apurac\_subst\)\.

   \- recuperar e somar os valores totalizados \(campo VAL\_ITEM\_DISCRIM\) dos lançamentos complementares de todas as UFs, e que sejam de item 006\-Outros Créditos e de item 007\-Estorno de Débitos do resumo da apuração de ST obrigação fiscal 108 e 165 \(campo COD\_TIPO\_LIVRO\), de acordo com o estabelecimento e período preenchido na tela Geração – Anexos e Quadros E e A/C \(parcial\)\.

__*Seleção para composição de “Outros Débitos” do Anexo VII*__

Origem: Resumo da Apuração de Substituição Tributária/ Interno, Resumo da Apuração de Substituição Tributária/ Interestadual, Lançamentos Complementares – Apuração ICMS Subst\. Tributária – Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única \(tabela item\_apurac\_subst\)\.

   \- recuperar e somar os valores totalizados \(campo VAL\_ITEM\_DISCRIM\) dos lançamentos complementares de todas as UFs, e que sejam de item 002\-Outros Débitos e de item 003\-Estorno de Créditos do resumo da apuração de ST obrigação fiscal 108 \(campo COD\_TIPO\_LIVRO\), de acordo com o estabelecimento e período preenchido na tela Geração – Anexos e Quadros E e A/C \(parcial\)\.

OS4818

RN00\.d

__Regra Geral – Anexo XV__

Origem: Lançamento Créditos/Débitos Especiais – RS: Apuração – Apuração do ICMS \- Lançamento Créditos/Débitos Especiais – RS, Lançamentos Complementares: Apuração \- Apuração ICMS – Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única \(tabela item\_apurac\_subst\)\.

   \- Recuperar os valores totalizando os lançamentos complementares de todas as UFs que sejam de item 002\-Outros Débitos e de item 003\-Estorno de Créditos do resumo da apuração obrigação fiscal 108 ou 165 \(campo COD\_TIPO\_LIVRO\) e/ou os Lançamento Créditos/Débitos Especiais – RS para os itens igual a ‘Débito’ caso houver, de acordo com o estabelecimento e período preenchido na tela Geração – Anexos e Quadros E e A/C \(parcial\)\. Verificar as regras dos campos do Anexo XV no documento ‘Matriz \- Estadual \- GIA\-RS \- Geracao Versao 8’

CH17451\_2016

RN00\.e

__Regra Geral – Anexo XIV__

__*Seleção para composição de “Valor Outros Créditos” do Anexo XIV*__

Origem: 	Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única

	Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS Subst\. Tributária >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única

__\[ALTERADA \- CH17457\_2016\]__

   \- recuperar e somar os valores totalizados \(campo VAL\_ITEM\_DISCRIM\) dos lançamentos complementares de todas as UFs, e que sejam de item 006\-Outros Créditos e de item 007\-Estorno de Débitos do resumo da apuração própria e de ST obrigação fiscal 108 e 165 \(campo COD\_TIPO\_LIVRO\), de acordo com o estabelecimento e período preenchido na tela Geração – Anexos e Quadros E e A/C \(parcial\), desde que o código de amparo esteja preenchido e que sua inicial seja igual a “7”\.

CH17457\_2016

RN01

__Regra Geral – Quadro A:__

__\[ALTERADA – OS4803\]__

__Ref\. 03 – Créditos por Transferências__

__Origem:__

- Estadual >> GIA\-RS >> IN DRP 45/98 – GIA >> Manutenção >> Anexo II – Créditos Recebidos p/ Transferência

__Tratamento:__

Preencher o campo __Valor Transferência__ do item Entradas do Quadro A \(localizado em Estadual >> GIA\-RS >> Obrigações >> IN DRP 45/98 – GIA >> Manutenção >> Quadro A – Resumo Operações e Prestações\) com a soma dos valores do campo Créditos Recebidos p/ Transferência\.

__Ref\. 06 – Outros Créditos__

__Origem:__

- Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única
- Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS Subst\. Tributária >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única

__\[ALTERADA – CH17457\_2016\]__

__Tratamento:__

Preencher o campo __Valor Outros__ do item Saídas do Quadro A \(localizado em Estadual >> GIA\-RS >> Obrigações >> IN DRP 45/98 – GIA >> Manutenção >> Quadro A – Resumo Operações e Prestações\) com a soma dos valores do campo Valor, quando houver lançamento complementar com o período de apuração dentro do período preenchido na Geração \- Anexos e Quadros E e A/C \(parcial\) e o campo Amparo/ Texto/ Ocorrência for diferente de branco ou nulo e for iniciado com “7”\.

__Ref\. 11 – Débitos por Transferências__

__Origem:__

- Estadual >> GIA\-RS >> IN DRP 45/98 – GIA >> Manutenção >> Anexo VI – Saldos Credores Transferidos

__Tratamento:__

Preencher o campo __Valor Transferência__ do item Saídas do Quadro A \(localizado em Estadual >> GIA\-RS >> Obrigações >> IN DRP 45/98 – GIA >> Manutenção >> Quadro A – Resumo Operações e Prestações\) com a soma dos valores do campo Saldos Credor Transferido\.

__Ref\. 12 – Débitos por Compensação__

__Origem:__

- Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única
- Estadual >> ICMS >> Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS Subst\. Tributária >> Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única

__Tratamento:__

Preencher o campo __Valor Compensação__ do item Saídas do Quadro A \(localizado em Estadual >> GIA\-RS >> Obrigações >> IN DRP 45/98 – GIA >> Manutenção >> Quadro A – Resumo Operações e Prestações\) com a soma dos valores do campo Valor, quando houver lançamento complementar com o período de apuração dentro do período preenchido na Geração \- Anexos e Quadros E e A/C \(parcial\) e o campo Amparo/ Texto/ Ocorrência for igual a 8999\.

CH13432\_2014

OS4803

CH17457\_2016

RN01\-ANEXO\_IC

__Geração campo Estabelecimento do Anexo I\.C:__

__Origem:__

Estadual >> GIA\-RS >> Obrigações >> IN DRP 45/98 – GIA >> Geração >> Anexos e Quadros E e A/C \(parcial\)\.

<a id="OLE_LINK84"></a><a id="OLE_LINK85"></a><a id="OLE_LINK86"></a>Será gerado de acordo com o estabelecimento selecionado na tela de geração dos anexos\. 

OS4486\-A

RN02\-ANEXO\_IC

__Geração campo Mês/Ano Apuração do Anexo I\.C:__

__Origem:__

Estadual >> GIA\-RS >> Obrigações >> IN DRP 45/98 – GIA >> Geração >> Anexos e Quadros E e A/C \(parcial\)\.

Será gerado de acordo com o mês e ano de apuração preenchido na tela de geração dos anexos\. 

OS4486\-A

RN03\-ANEXO\_IC

__Geração campo CFOP do Anexo I\.C:__

Será informado o CFOP processado na geração dos Anexos havendo registros a serem informados na discriminação das entradas e de acordo com o estabelecimento e período de apuração informado\.

OS4486\-A

RN04\-ANEXO\_IC

<a id="OLE_LINK102"></a><a id="OLE_LINK103"></a><a id="OLE_LINK104"></a>__Geração campo Código de Ajuste do Anexo I\.C:__

<a id="OLE_LINK131"></a><a id="OLE_LINK132"></a><a id="OLE_LINK133"></a><a id="OLE_LINK134"></a><a id="OLE_LINK209"></a><a id="OLE_LINK210"></a><a id="OLE_LINK211"></a>Será gerado o código de ajuste de acordo com a regra geral, considerando a seleção e recuperação mais o parâmetro efetuado na TACES86\.

__Exemplo:__

__SAFX08__

__SAFX08__

__SAFX08__

__SAFX08__

<a id="OLE_LINK212"></a><a id="OLE_LINK213"></a>NF 001

CFOP 1101

Vlr Cont\. Item = 28\.000,00

Base ICMS = 20\.000,00

Vlr ICMSS = 28\.000,00

NF 002

CFOP 1101

Vlr Cont\. Item = 20\.000,00

Base Isenta ICMS = 20\.000,00

Vlr ICMSS = 0,00

<a id="OLE_LINK228"></a><a id="OLE_LINK229"></a>NF 003

CFOP 1101

Vlr Cont\. Item = 22\.000,00

Base ICMS = 20\.000,00

Vlr IPI = 2\.000,00

NF 004

CFOP 1102

Vlr Cont\. Item = 200,00

Base ICMS = 100,00

Vlr IPI = 100,00

__TACES51__

<a id="OLE_LINK214"></a><a id="OLE_LINK215"></a>UF

CFOP

Vlr Cont\.

BC ICMS

BC Isenta

BC Outras

Excluída

Cálculo

Obs

RS

1101

S

S

S

S

N

1

N

RS

1102

S

S

S

S

S

0

S

__TACES86__

<a id="OLE_LINK224"></a><a id="OLE_LINK225"></a>CFOP

Cód\. Ajuste

Data Início

Data Fim

<a id="_Hlk398660361"></a><a id="_Hlk398660930"></a>1101

001

<a id="OLE_LINK218"></a><a id="OLE_LINK219"></a><a id="OLE_LINK220"></a>20140701

1101

002

<a id="OLE_LINK221"></a><a id="OLE_LINK222"></a><a id="OLE_LINK223"></a>20140701

1101

004

20140701

1102

001

20140701

1102

002

20140701

1102

004

20140701

__TACES87__

Cód\. Ajuste

Descrição

Recuperar Motivo

Data Início

Data Fim

001

ST XXXXXXXXXX

1

20140701

002

IPI XXXXXXXXXX

1

20140701

003

Frete XXXXXXXX

1

<a id="OLE_LINK226"></a><a id="OLE_LINK227"></a>20140701

004

Diferença XXXXXX 

1

20140701

005

Soma XXXXXXXX

1

20140701

006

Exclusões XXXXX

1

20140701

__Manutenção:__

Anexo I

CFOP 1101

Importâncias Excluídas = 30\.000,00

Anexo I\.C

CFOP 1101

Código de Ajuste: 001

Valor = 28\.000,00

CFOP 1101

Código de Ajuste: 002

Valor = 2\.000,00

Nesse caso para recuperação do CFOP 1101 ele identifica que existe ST e IPI destacado, por mais que tenha valor de Base Isenta, ele não considera na geração, pois não existe o parâmetro para o CFOP com código de movito igual a 005\.

O campo Importâncias Excluídas do Anexo I deverá buscar a soma do campo valor do detalhamento para cada CFOP\.

O CFOP 1102 está com indicador do cálculo igual a 0, então será desconsiderado da recuperação dos registros\.

OS4486\-A

RN05\-ANEXO\_IC

__Geração campo Valor do Anexo I\.C:__

Será gerado o valor do motivo de ajuste de acordo com a regra geral, considerando a seleção e recuperação mais o parâmetro efetuado na TACES87\.

__\[ALTERADA – OS4486\-B\]/\[ALTERADA – CH28430\_2014\]__

- Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 1, gravar soma do campo Vlr ICMSS do item da nota fiscal \(campo VLR\_SUBST\_ICMS da SAFX08\)\.
- Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 2, gravar soma dos campos Vlr ICMSS do item da nota fiscal \(campo VLR\_SUBST\_ICMS da SAFX08\), B\. Isenta ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 2 da SAFX08\) e B\. Outras ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 3 da SAFX08\)\.
- Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 3, gravar soma do campo B\. Isenta ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 2 da SAFX08\)\.
- Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 4, gravar soma do campo B\. Outras ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 3 da SAFX08\)\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 1, gravar soma do campo Vlr IPI do item da nota fiscal \(campo VLR\_IPI da SAFX08\)\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 2, gravar soma dos campos Vlr IPI do item da nota fiscal \(campo VLR\_IPI\), B\. Isenta IPI \(campo BASE\_IPI e TRIB\_IPI = 2 da SAFX08\) e B\. Outras IPI \(campo BASE\_IPI e TRIB\_IPI = 3 da SAFX08\)\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 3, gravar soma do campo B\. Isenta IPI \(campo BASE\_IPI e TRIB\_IPI = 2 da SAFX08\)\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 4, gravar soma do campo B\. Outras IPI \(campo BASE\_IPI e TRIB\_IPI = 3 da SAFX08\)\.
- Se o CFOP com Código de Ajuste igual a 003 e campo Recuperar Motivo da TACES87 igual a 1, gravar soma do campo Vlr Frete do item da nota fiscal \(campo VLR\_FRETE da SAFX08\)\.
- Se o CFOP com Código de Ajuste igual a 003 e campo Recuperar Motivo da TACES87 igual a 2, gravar soma do campo Vlr Frete do item da nota fiscal \(campo VLR\_FRETE da SAFX08\)\.
- Se o CFOP com Código de Ajuste igual a 004 e campo Recuperar Motivo da TACES87 igual a 1, gravar a diferença da soma do campo Vlr Cont\. Item \(campo VLR\_CONTAB\_ITEM da SAFX08\) e da Base ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 1 da SAFX08\) mais a diferença da soma do campo Valor Total \(campo VLR\_TOT da SAFX09\) e da Base ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 1 da SAFX09\)\.
- Se o CFOP com Código de Ajuste igual a 005 e campo Recuperar Motivo da TACES87 igual a 1, gravar soma dos campos Base ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 1 da SAFX08 e SAFX09\), B\. Isenta ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 2 da SAFX08 e SAFX09\), B\. Outras ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 3 da SAFX08 e SAFX09\) e B\. Redução ICMS \(campo BASE\_ICMS e TRIB\_ICMS = 4 da SAFX08 e SAFX09\)\.
- Se o CFOP com Código de Ajuste igual a 006 e campo Recuperar Motivo da TACES87 igual a 1, não iremos tratar no momento, indicaremos de que será feito de forma manual tanto na TACES quanto no manual operacional\.

Utilizar como exemplo o mesmo caso especificado na RN04\-ANEXO\_IC\.

OS4486\-A

OS4486\-B

CH28430\_2014

RN01\-ANEXO\_ VC

__Geração campo Estabelecimento do Anexo V\.C:__

__Origem:__

Estadual >> GIA\-RS >> Obrigações >> IN DRP 45/98 – GIA >> Geração >> Anexos e Quadros E e A/C \(parcial\)\.

Será gerado de acordo com o estabelecimento selecionado na tela de geração dos anexos\. 

OS4486\-A

RN02\-ANEXO\_ VC

__Geração campo Mês/Ano Apuração do Anexo V\.C:__

__Origem:__

Estadual >> GIA\-RS >> Obrigações >> IN DRP 45/98 – GIA >> Geração >> Anexos e Quadros E e A/C \(parcial\)\.

Será gerado de acordo com o mês e ano de apuração preenchido na tela de geração dos anexos\. 

OS4486\-A

RN03\-ANEXO\_ VC

__Geração campo CFOP do Anexo V\.C:__

Será informado o CFOP processado na geração dos Anexos havendo registros a serem informados na discriminação das saídas e de acordo com o estabelecimento e período de apuração informado\.

OS4486\-A

RN04\-ANEXO\_ VC

__Geração campo Código de Ajuste do Anexo V\.C:__

Será gerado o código de ajuste de acordo com a regra geral, considerando a seleção e recuperação mais o parâmetro efetuado na TACES86\.

__Exemplo:__

__SAFX08__

__SAFX08__

__SAFX08__

__SAFX08__

NF 001

CFOP 1101

Vlr Cont\. Item = 28\.000,00

Base ICMS = 20\.000,00

Vlr ICMSS = 28\.000,00

NF 002

CFOP 1101

Vlr Cont\. Item = 20\.000,00

Base Isenta ICMS = 20\.000,00

Vlr ICMSS = 0,00

NF 003

CFOP 1101

Vlr Cont\. Item = 22\.000,00

Base ICMS = 20\.000,00

Vlr IPI = 2\.000,00

NF 004

CFOP 1102

Vlr Cont\. Item = 200,00

Base ICMS = 100,00

Vlr IPI = 100,00

__TACES51__

UF

CFOP

Vlr Cont\.

BC ICMS

BC Isenta

BC Outras

Excluída

Cálculo

Obs

RS

1101

S

S

S

S

N

1

N

RS

1102

S

S

S

S

S

0

S

__TACES86__

CFOP

Cód\. Ajuste

Data Início

Data Fim

1101

001

20140701

1101

002

20140701

1101

004

20140701

1102

001

20140701

1102

002

20140701

1102

004

20140701

__TACES87__

Cód\. Ajuste

Descrição

Recuperar Motivo

Data Início

Data Fim

001

ST XXXXXXXXXX

1

20140701

002

IPI XXXXXXXXXX

1

20140701

003

Frete XXXXXXXX

1

20140701

004

Diferença XXXXXX 

1

20140701

005

Soma XXXXXXXX

1

20140701

006

Exclusões XXXXX

1

20140701

__Manutenção:__

Anexo I

CFOP 1101

Importâncias Excluídas = 30\.000,00

Anexo I\.C

CFOP 1101

Código de Ajuste: 001

Valor = 28\.000,00

CFOP 1101

Código de Ajuste: 002

Valor = 2\.000,00

Nesse caso para recuperação do CFOP 1101 ele identifica que existe ST e IPI destacado, por mais que tenha valor de Base Isenta, ele não considera na geração, pois não existe o parâmetro para o CFOP com código de movito igual a 005\.

O campo Importâncias Excluídas do Anexo I deverá buscar a soma do campo valor do detalhamento para cada CFOP\.

O CFOP 1102 está com indicador do cálculo igual a 0, então será desconsiderado da recuperação dos registros\.

OS4486\-A

RN05\-ANEXO\_VC

__Geração campo Valor do Anexo V\.C:__

Será gerado o valor do motivo de ajuste de acordo com a regra geral, considerando a seleção e recuperação mais o parâmetro efetuado na TACES87\.

__\[ALTERADA – OS4486\-B\]__

- Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 1, gravar soma do campo Vlr ICMSS do item da nota fiscal \(campo VLR\_SUBST\_ICMS da SAFX08\)\.
- Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 2, gravar soma dos campos Vlr ICMSS do item da nota fiscal \(campo VLR\_SUBST\_ICMS da SAFX08\), B\. Isenta ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 2 da SAFX08\) e B\. Outras ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 3 da SAFX08\)\.
- Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 3, gravar soma do campo B\. Isenta ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 2 da SAFX08\)\.
- Se o CFOP com Código de Ajuste igual a 001 e campo Recuperar Motivo da TACES87 igual a 4, gravar soma do campo B\. Outras ICMSS do item da nota fiscal \(campo BASE\_SUB\_TRIB\_ICMS e TRIB\_ICMSS = 3 da SAFX08\)\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 1, gravar soma do campo Vlr IPI do item da nota fiscal \(campo VLR\_IPI da SAFX08\)\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 2, gravar soma dos campos Vlr IPI do item da nota fiscal \(campo VLR\_IPI\), B\. Isenta IPI \(campo BASE\_IPI e TRIB\_IPI = 2 da SAFX08\) e B\. Outras IPI \(campo BASE\_IPI e TRIB\_IPI = 3 da SAFX08\)\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 3, gravar soma do campo B\. Isenta IPI \(campo BASE\_IPI e TRIB\_IPI = 2 da SAFX08\)\.
- Se o CFOP com Código de Ajuste igual a 002 e campo Recuperar Motivo da TACES87 igual a 4, gravar soma do campo B\. Outras IPI \(campo BASE\_IPI e TRIB\_IPI = 3 da SAFX08\)\.
- Se o CFOP com Código de Ajuste igual a 004 e campo Recuperar Motivo da TACES87 igual a 1, gravar a diferença da soma do campo Vlr Cont\. Item \(campo VLR\_CONTAB\_ITEM da SAFX08\) e da Base ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 1 da SAFX08\) mais a diferença da soma do campo Valor Total \(campo VLR\_TOT da SAFX09\) e da Base ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 1 da SAFX09\)\.
- Se o CFOP com Código de Ajuste igual a 005 e campo Recuperar Motivo da TACES87 igual a 1, gravar soma dos campos Base ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 1 da SAFX08 e SAFX09\), B\. Isenta ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 2 da SAFX08 e SAFX09\) e B\. Outras ICMS do item da nota fiscal \(campo BASE\_ICMS e TRIB\_ICMS = 3 da SAFX08 e SAFX09\)\.
- Se o CFOP com Código de Ajuste igual a 006 e campo Recuperar Motivo da TACES87 igual a 1, não iremos tratar no momento, indicaremos de que será feito de forma manual tanto na TACES quanto no manual operacional\.

Utilizar como exemplo o mesmo caso especificado na RN04\-ANEXO\_VC\.

OS4486\-A

OS4486\-B

RN01\-ANEXO\_II

__Geração campo Estabelecimento do Anexo II:__

__Origem:__

Estadual >> GIA\-RS >> Obrigações >> IN DRP 45/98 – GIA >> Geração >> Anexos e Quadros E e A/C \(parcial\)\.

Será gerado de acordo com o estabelecimento selecionado na tela de geração dos anexos\. 

OS4803

RN02\-ANEXO\_II

__Geração campo Mês/Ano Apuração do Anexo II:__

__Origem:__

Estadual >> GIA\-RS >> Obrigações >> IN DRP 45/98 – GIA >> Geração >> Anexos e Quadros E e A/C \(parcial\)\.

Será gerado de acordo com o mês e ano de apuração preenchido na tela de geração dos anexos\. 

OS4803

RN03\-ANEXO\_II

__Geração campo Inscrição Estadual do Remetente do Anexo II:__

__Origem:__

Básicos >> Mastersaf DW >> Manutenção >> Cadastros >> Pessoas Físicas/Jurídicas \(SAFX04\)\.

__\[ALTERADA – OS4803\]__

Será gerada a Inscrição estadual da Pessoa Física/ Jurídica cadastrada na nota fiscal de entrada processada na geração dos Anexos de acordo com o estabelecimento e período de apuração informado e também se houver vinculação de SAFX113 mais parametrização por código de ajuste\.

OS4803

RN04\-ANEXO\_II

__Geração campo Amparo/ Texto/ Ocorrência do Anexo II:__

__\[ALTERADA – OS4803\]__

__Origem:__

Básicos >> Mastersaf DW >> Manutenção >> Documento Fiscal >> Novo Documento Fiscal >> Doc\. Fiscal de Mercadoria \(SAFX07\) 

Básicos >> Mastersaf DW >> Manutenção >> Cadastros >> Código Amparo/ Texto/ Ocorrência \(TACES21\)

Estadual >> GIA\-RS >> Parâmetros >> IN DRP 45/98 – GIA >> Transferências / Recebimentos >> Por Código de Ajuste \(campo Anexo = Anexo II \- Discriminação dos Créditos Recebidos por Transferências\)

Será gerado o código de amparo de acordo com a regra geral, considerando a seleção e recuperação mais o parâmetro efetuado na TACES21 ou de acordo com a parametrização feita em Transferências / Recebimentos – Por Código de Ajuste\.

OS4803

RN05\-ANEXO\_II

__Geração campo Créditos Recebidos p/ Transferência do Anexo II:__

__\[ALTERADA – OS4803\]__

__Origem:__

Básicos >> Mastersaf DW >> Manutenção >> Documento Fiscal >> Novo Documento Fiscal >> Doc\. Fiscal de Mercadoria – Aba Item Mercadoria \(SAFX08\)

Básicos >> Mastersaf DW >> Manutenção >> Documento Fiscal >> Novo Documento Fiscal >> Doc\. Fiscal de Mercadoria – Aba Observação do Lançamento Fiscal – Quadro Ajuste/Outros Valores do Lançamento Fiscal \(SAFX113\)

Será gerado o valor de crédito recebido por transferência de acordo com a regra geral, considerando:

- Se a seleção for a partir da parametrização por código de ajuste, preencher com a soma do valor tributado do ICMS \(campo VLR\_ICMS da SAFX113\);

__Senão,__

- Se a seleção for a partir dos documentos fiscais, preencher com a soma do valor do imposto \(campo VLR\_ICMS da SAFX08\);

OS4803

RN06\-ANEXO\_II

__Geração campo Nº Processo do Anexo II:__

Neste campo é informado o número do processo pelo qual o registro foi inserido no MasterSAF, em que recebe 1 se processado manualmente e 2 se processado automaticamente\.

OS4803

RN01\-ANEXO\_VI

__Geração campo Estabelecimento do Anexo VI:__

__Origem:__

Estadual >> GIA\-RS >> Obrigações >> IN DRP 45/98 – GIA >> Geração >> Anexos e Quadros E e A/C \(parcial\)\.

Será gerado de acordo com o estabelecimento selecionado na tela de geração dos anexos\. 

OS4803

RN02\-ANEXO\_VI

__Geração campo Mês/Ano Apuração do Anexo VI:__

__Origem:__

Estadual >> GIA\-RS >> Obrigações >> IN DRP 45/98 – GIA >> Geração >> Anexos e Quadros E e A/C \(parcial\)\.

Será gerado de acordo com o mês e ano de apuração preenchido na tela de geração dos anexos\. 

OS4803

RN03\-ANEXO\_VI

__Geração campo Inscrição Estadual do Destinatário do Anexo VI:__

__Origem:__

Básicos >> Mastersaf DW >> Manutenção >> Cadastros >> Pessoas Físicas/Jurídicas \(SAFX04\)\.

__\[ALTERADA – OS4803\]__

Será gerada a Inscrição estadual da Pessoa Física/ Jurídica cadastrada na nota fiscal de entrada processada na geração dos Anexos de acordo com o estabelecimento e período de apuração informado e também se houver vinculação de SAFX113 mais parametrização por código de ajuste\.

OS4803

RN04\-ANEXO\_VI

__Geração campo Amparo/ Texto/ Ocorrência do Anexo VI:__

__\[ALTERADA – OS4803\]__

__Origem:__

Básicos >> Mastersaf DW >> Manutenção >> Documento Fiscal >> Novo Documento Fiscal >> Doc\. Fiscal de Mercadoria \(SAFX07\) 

Básicos >> Mastersaf DW >> Manutenção >> Cadastros >> Código Amparo/ Texto/ Ocorrência \(TACES21\)

Estadual >> GIA\-RS >> Parâmetros >> IN DRP 45/98 – GIA >> Transferências / Recebimentos >> Por Código de Ajuste \(campo Anexo = Anexo VI \- Discriminação dos Créditos Transferidos\)

Será gerado o código de amparo de acordo com a regra geral, considerando a seleção e recuperação mais o parâmetro efetuado na TACES21 ou de acordo com a parametrização feita em Transferências / Recebimentos – Por Código de Ajuste\.

OS4803

RN05\-ANEXO\_VI

__Geração campo Créditos Recebidos p/ Transferência do Anexo VI:__

__\[ALTERADA – OS4803\]__

__Origem:__

Básicos >> Mastersaf DW >> Manutenção >> Documento Fiscal >> Novo Documento Fiscal >> Doc\. Fiscal de Mercadoria – Aba Item Mercadoria \(SAFX08\)

Básicos >> Mastersaf DW >> Manutenção >> Documento Fiscal >> Novo Documento Fiscal >> Doc\. Fiscal de Mercadoria – Aba Observação do Lançamento Fiscal – Quadro Ajuste/Outros Valores do Lançamento Fiscal \(SAFX113\)

Será gerado o valor de crédito recebido por transferência de acordo com a regra geral, considerando:

- Se a seleção for a partir da parametrização por código de ajuste, preencher com a soma do valor tributado do ICMS \(campo VLR\_ICMS da SAFX113\);

__Senão,__

- Se a seleção for a partir dos documentos fiscais, preencher com a soma do valor do imposto \(campo VLR\_ICMS da SAFX07\);

OS4803

RN06\-ANEXO\_VI

__Geração campo Nº Processo do Anexo VI:__

Neste campo é informado o número do processo pelo qual o registro foi inserido no MasterSAF, em que recebe 1 se processado manualmente e 2 se processado automaticamente\.

OS4803

RN04\-ANEXO\_VII

__Geração campo Outros Créditos do Anexo VII:__

__Origem:__

Lançamentos Complementares – Apuração ICMS Subst\. Tributária – Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única \(tabela item\_apurac\_subst\)\.

Será gerado com a soma do campo Valor dos itens 006 e 007 da obrigação da apuração de acordo com a regra geral, considerando a regra de recuperação\.

OS4818

RN05\-ANEXO\_VII

__Geração campo Total dos Créditos do Anexo VII:__

__\[ALTERADA – OS4818\]__

Será gerado com a soma dos campos Total de Créditos ICMS\-ST e Outros Créditos no momento da inserção na tabela do Anexo VII que depende do Anexo VII\.A\.

OS4818

RN08\-ANEXO\_VII

__Geração campo Outros Débitos do Anexo VII:__

__Origem:__

Lançamentos Complementares – Apuração ICMS Subst\. Tributária – Ajuste SINIEF ou Empresas c/ Insc\. Estadual Única \(tabela item\_apurac\_subst\)\.

Será gerado com a soma do campo Valor dos itens 002 e 003 da obrigação da apuração de acordo com a regra geral, considerando a regra de recuperação\.

OS4818

RN09\-ANEXO\_VII

__Geração campo Total dos Débitos do Anexo VII:__

__\[ALTERADA – OS4818\]__

Será gerado com a soma dos campos Total de Débitos ICMS\-ST e Outros Créditos no momento da inserção na tabela do Anexo VII que depende do Anexo VII\.B\.

OS4818

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


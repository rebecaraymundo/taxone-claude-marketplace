# MTZ-ICMS-GIA-ST_Manutencao

- **Fonte:** MTZ-ICMS-GIA-ST_Manutencao.docx
- **Modificado:** 2025-11-03
- **Tamanho:** 191 KB

---

THOMSON REUTERS

Guia de Informação de Substituição Tributária

Manutenção GIA\-ST

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

OS3298

Vânia Mattos

A geração da GIA\-ST e da GNRE foi alterada para possibilitar que o valor dos lançamentos complementar seja utilizado a partir de um novo parâmetro definido pelo usuário\.

OS4798

Julyana Perrucini

Este documento tem como objetivo atualizar a GIA\-ST de acordo com Versão 3 do layout disponibilizado pela SEFAZ do RS\.

MFS2283

Julyana Perrucini

Este documento tem como objetivo atualizar a GIA\-ST de acordo com Versão 3\.1 do layout disponibilizado pela SEFAZ do RS\.

CH24358\_2016

Lara Aline

Este documento tem como objetivo incluir regra para o campo Credito ICMS\-ST Periodo Anterior\.

CH4823\_2017

João Henrique

Este documento tem como objetivo incluir regra para o campo Valor do ICMS Devido à UF de Destino e Devoluções ou Anulações\.

MFS28188

Alteração na geração do Valor ICMS ST FCP

Automatização do campo Valor do ICMS\-ST FCP da GIA ST

MFS545769

Andréa Rocha

Inclusão de um parâmetro para definir se os campos de ICMS\-ST devido, Crédito p/o Período Seguinte e ICMS\-ST a Recolher, devem ficar habilitados para a alteração dos valores calculados\.  

Sumário

[1\.	Regras dos Campos	3](#_Toc480792187)

[2\.	Sugestão de Layouts	20](#_Toc480792188)

# <a id="_Toc350763252"></a><a id="_Toc480792187"></a>Regras dos Campos 

__Localização da tela:__ Estadual\\ ICMS\\ Apuração\\ Guias de Recolhimento\\ Guia de Informação de Substituição Tributária\\ Manutenção

__Título da tela: __Guia de Informação de Substituição Tributária

__Regra Geral Botões:__

__NOVO – __Permite inserir novo registro\.

__ABRE – __Permite abrir seleção de registros inseridos\.

__EXCLUI – __Permite excluir registro inserido\.

__CONFIRMA – __Permite salvar registro\.

__RELATÓRIO – __Permite emitir relatório listando todos os registros existentes na base de dados ou de acordo com a Empresa e Estabelecimento selecionados na tela de login \(mostrar campos chaves como critério de busca\)\.

__FECHA – __Permite sair da tela\.

__Regras Gerais: __

- __Alteração da OS3298:__
- A partir da OS3298 a manutenção da GIA\-ST foi alterada para a criação de campos para os lançamentos complementares da apuração do ICMS\-ST, que passaram a ser gerados durante a rotina de geração da GIA\-ST \(ver documento de regras específico da geração: “MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc”\)\. Com a criação destes campos, foi alterada a totalização dos valores nos campos “ICMS\-ST Devido”, “Crédito p/o Período Seguinte” e “ICMS\-ST a Recolher”\.
- __Regra Geral Vencimentos:__

Para recuperar os Vencimentos e Valores do ICMS\-ST e do FCP, existem dois processos na rotina de geração da GIA\-ST no Mastersaf DW:

- Através das GNRE’s, preenchendo automaticamente os campos de Vencimento e Valor \(exceto valor do FCP, que deverá ser preenchido manualmente \[MFS28188\]\) associados aos vencimentos das GNRE’s do período;

Nesse caso é verificado se existe conteúdo na tabela ICT\_GUIA\_GNRE\_CON, que contém as guias recolhidas no período, então se houver, a rotina de geração realiza o tratamento abaixo:

1. Verifica a inscrição estadual do estabelecimento para a UF em questão \(módulo Básicos \- Parâmetros, menu Preliminares >> Inscrições Estaduais\);
2. Caso a inscrição não esteja cadastrada, ou esteja suspensa, soma todas as guias da UF em questão, o valor recuperado será gravado na GIA\-ST no campo do 1º vencimento \(módulo Estadual \- ICMS, menu Apuração >> Guias de Recolhimento >> Guia de Informação de Substituição Tributária >> Manutenção\), e a data do vencimento será a maior data das GNRE’s existentes no período;
3. Caso a inscrição exista e seja válida, totaliza as GNRE’s por data de vencimento, e grava um registro para cada vencimento, com o valor totalizado do vencimento\. \(__Ver OS2289__\)

- Ou; Através da parametrização por UF Favorecida, caso não localize guias no período\. Nesse caso o usuário precisa colocar os dias de Vencimento e quando efetuar a geração dos dados, esses dias serão preenchidos na Manutenção no item Vencimentos da Aba Principal, mas seu valor deverá ser preenchido manualmente\. 

*Observações:*

- A GIA\-ST é sempre gerada por UF, portanto, ao ler as GNRE’s na tabela ICT\_GUIA\_GNRE\_CON, sempre considera a UF da GIA\-ST, tratando cada caso separadamente\.
- Ao fazer o cálculo das GNRE’s considera as GNRE’s com Data de Apuração dentro do período informado na GIA\-ST\.
- Os Vencimentos estão acoplados para o preenchimento do valor do ICMS\-ST e do ICMS\-ST FCP, então será uma única data, até porque no layout exige desta forma, porém os valores a recolher deverão ser separados\.

__ABA PRINCIPAL__

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Crédito ICMS\-ST Período Anterior:

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Habilitado

Neste campo será exibido o valor do Crédito p/ o Período Seguinte constante da GIA\-ST do período anterior\.

O campo poderá ser alterado pelo usuário, ou mesmo inserido manualmente, conforme os demais campos da GIA\-ST\.

CH24358\_2016

Lançamentos Complementares \- Outros Débitos

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Habilitado

Neste campo será exibido o valor dos lançamentos complementares de outros débitos da Apuração do ICMS\-ST \(P9\) totalizados durante a geração da GIA\-ST \(menu “Geração”\)\.

O campo poderá ser alterado pelo usuário, ou mesmo inserido manualmente, conforme os demais campos da GIA\-ST\.

OS3298

Lançamentos Complementares \- Estorno de Crédito

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Habilitado

Neste campo será exibido o valor dos lançamentos complementares de estorno de crédito da Apuração do ICMS\-ST \(P9\) totalizados durante a geração da GIA\-ST \(menu “Geração”\)\.

O campo poderá ser alterado pelo usuário, ou mesmo inserido manualmente, conforme os demais campos da GIA\-ST\.

OS3298

Lançamentos Complementares \- Outros Créditos

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Habilitado

Neste campo será exibido o valor dos lançamentos complementares de outros créditos da Apuração do ICMS\-ST \(P9\) totalizados durante a geração da GIA\-ST \(menu “Geração”\)\.

O campo poderá ser alterado pelo usuário, ou mesmo inserido manualmente, conforme os demais campos da GIA\-ST\.

*Observação:* Este campo já existia, mas não continha valores trazidos da apuração do ICMS\-ST, pois até o desenvolvimento desta OS a GIA\-ST não recuperava valores da apuração, ou seja, o campo só recebia valores inseridos manualmente pelo usuário\.

OS3298

Lançamentos Complementares \- Estorno de Débito

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Habilitado

Neste campo será exibido o valor dos lançamentos complementares de estorno de débito da Apuração do ICMS\-ST \(P9\) totalizados durante a geração da GIA\-ST \(menu “Geração”\)\.

O campo poderá ser alterado pelo usuário, ou mesmo inserido manualmente, conforme os demais campos da GIA\-ST\.

OS3298

Lançamentos Complementares \- Deduções:            

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Habilitado

Neste campo será exibido o valor dos lançamentos complementares de dedução da Apuração do ICMS\-ST \(P9\) totalizados durante a geração da GIA\-ST \(menu “Geração”\)\.

O campo poderá ser alterado pelo usuário, ou mesmo inserido manualmente, conforme os demais campos da GIA\-ST\.

OS3298

Alterar Valores de ICMS\-ST Devido, Crédito p/ Per\. Seguinte e ICMS\-ST a Recolher

Texto

N

S

Formato: 

Check Box

Default: 

Habilitado

Este campo indicará se será permitido alterar os valores de ICMS\-ST Devido, Crédito p/ Período Seguinte e ICMS\-ST a Recolher\.

A opção virá desmarcada quando via processamento \(geração dos registros\), esse campo não será preenchido na geração\.

A opção marcada indicará “S”, que vai permitir alterar os campos de valores indicados e a opção desmarcada indicará “N”,  que não vai permitir alterar os campos de valores indicados\.

MFS545769

ICMS\-ST Devido

Numérico

N

S

Formato: 

Text Input 0,00 

Default:

desabilitado

A habilitação desse campo para manutenção vai depender do campo “Alterar Valores de ICMS\-ST Devido, Crédito p/ Per\. Seguinte e ICMS\-ST a Recolher”\. 

 Quando o campo  for desmarcado, o campo ICMS\-ST Devido vai ficar desabilitado para a alteração, mas o cálculo abaixo deve ser feito\.

Quando o campo  for marcado, o campo ICMS\-ST Devido vai ficar habilitado para a alteração, e se o usuário alterar ou zerar o valor, o cálculo abaixo não deve ser feito\.

Neste campo será gravado o resultado abaixo, caso positivo:     \(caso negativo, gravar zero\)

\(ICMS\-ST Retido \+ Outros Débitos \+ Estorno de Créditos\) – \(Devoluções \+ Ressarcimento \+ Crédito do Per\. Anterior \+ Pagamentos Antecipados \+ Outros Créditos \+ Estorno de Débitos \+ Deduções\)

__Obs__\.:  Se o campo “Alterar Valores de ICMS\-ST Devido, Crédito p/ Per\. Seguinte e ICMS\-ST a Recolher” estiver marcado e depois for desmarcado, o cálculo acima deve ser refeito\.

OS3298

MFS545769

Crédito p/o Período Seguinte

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

desabilitado

A habilitação desse campo para manutenção vai depender do campo “Alterar Valores de ICMS\-ST Devido, Crédito p/ Per\. Seguinte e ICMS\-ST a Recolher”\. 

Quando o campo  for desmarcado, o campo Crédito p/o Período Seguinte vai ficar desabilitado para a alteração, mas o cálculo abaixo deve ser feito\.

Quando o campo  for marcado, o campo Crédito p/o Período Seguinte vai ficar habilitado para a alteração, e se o usuário alterar ou zerar o valor, o cálculo abaixo não deve ser feito\.

Neste campo será exibido o valor do crédito do ICMS\-ST a ser apropriado no período seguinte\.

Se o resultado abaixo for positivo, gravar o resultado no campo “__Crédito p/o Período Seguinte__”, caso contrário,__ __o resultado deverá ser gravado no campo “__ICMS\-ST a Recolher__”: 

\(Devoluções \+ Ressarcimento \+ Crédito do Per\. Anterior \+ Pagamentos Antecipados \+ Outros Créditos \+ Estorno de Débitos \+ Deduções\) – 

\(ICMS\-ST Retido \+ Outros Débitos \+ Estorno de Créditos \+ Repasse ICMS\-ST Combustível\) 

Obs: Este valor é o resultado do total dos créditos – total dos débitos \(incluindo o repasse do ICMS\-ST de combustível\)\.

Se o campo “Alterar Valores de ICMS\-ST Devido, Crédito p/ Per\. Seguinte e ICMS\-ST a Recolher” estiver marcado e depois for desmarcado, o cálculo acima deve ser refeito\.

OS3298

MFS545769

ICMS\-ST a Recolher

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

desabilitado

A habilitação desse campo para manutenção vai depender do campo “Alterar Valores de ICMS\-ST Devido, Crédito p/ Per\. Seguinte e ICMS\-ST a Recolher”\. 

Quando o campo  for desmarcado, o campo ICMS\-ST a Recolher vai ficar desabilitado para a alteração, mas o cálculo abaixo deve ser feito\.

Quando o campo  for marcado, o campo ICMS\-ST a Recolher vai ficar habilitado para a alteração, e se o usuário alterar ou zerar o valor, o cálculo abaixo não deve ser feito\.

Ver regra do campo “Crédito p/o Período Seguinte”\.

__Obs__\.:  Se o campo “Alterar Valores de ICMS\-ST Devido, Crédito p/ Per\. Seguinte e ICMS\-ST a Recolher” estiver marcado e depois for desmarcado, o cálculo desse campo deve ser refeito\.

OS3298

MFS545769

Observação

Texto

N

S

Formato: 

Text Input

Default: 

Habilitado

Nesse campo o usuário poderá fazer qualquer observação sobre a GIA\-ST\.

__\[ALTERADA – OS4798\]__

Aumentar campo em tela para receber até 185 posições\.

OS4798

Vencimentos – Data do 1º Vencimento

Data

N

S

Formato: 

Text Input

Default: 

Desabilitado

Neste campo será exibida a data de vencimento do ICMS\-ST no formato DD/MM/AAAA, conforme prazos constantes de Convênios e Protocolos ICMS\.

Essa informação deve ser processada de acordo com a RN00 \(Vencimentos\) do documento matriz: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

*Observação:*

Só é editável quando habilitado\.

MFS2283

Vencimentos – Data do 2º Vencimento

Data

N

S

Formato: 

Text Input

Default: 

Desabilitado

Neste campo será exibida a data de vencimento do ICMS\-ST no formato DD/MM/AAAA, conforme prazos constantes de Convênios e Protocolos ICMS\.

Essa informação deve ser processada de acordo com a RN00 \(Vencimentos\) do documento matriz: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

*Observação:*

Só é editável quando habilitado\.

MFS2283

Vencimentos – Data do 3º Vencimento

Data

N

S

Formato: 

Text Input

Default: 

Desabilitado

Neste campo será exibida a data de vencimento do ICMS\-ST no formato DD/MM/AAAA, conforme prazos constantes de Convênios e Protocolos ICMS\.

Essa informação deve ser processada de acordo com a RN00 \(Vencimentos\) do documento matriz: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

*Observação:*

Só é editável quando habilitado\.

MFS2283

Vencimentos – Data do 4º Vencimento

Data

N

S

Formato: 

Text Input

Default: 

Desabilitado

Neste campo será exibida a data de vencimento do ICMS\-ST no formato DD/MM/AAAA, conforme prazos constantes de Convênios e Protocolos ICMS\.

Essa informação deve ser processada de acordo com a RN00 \(Vencimentos\) do documento matriz: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

*Observação:*

Só é editável quando habilitado\.

MFS2283

Vencimentos – Data do 5º Vencimento

Data

N

S

Formato: 

Text Input

Default: 

Desabilitado

Neste campo será exibida a data de vencimento do ICMS\-ST no formato DD/MM/AAAA, conforme prazos constantes de Convênios e Protocolos ICMS\.

Essa informação deve ser processada de acordo com a RN00 \(Vencimentos\) do documento matriz: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

*Observação:*

Só é editável quando habilitado\.

MFS2283

Vencimentos – Data do 6º Vencimento

Data

N

S

Formato: 

Text Input

Default: 

Desabilitado

Neste campo será exibida a data de vencimento do ICMS\-ST no formato DD/MM/AAAA, conforme prazos constantes de Convênios e Protocolos ICMS\.

Essa informação deve ser processada de acordo com a RN00 \(Vencimentos\) do documento matriz: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

*Observação:*

Só é editável quando habilitado\.

MFS2283

Vencimentos – Valor do ICMS\-ST \(1º Vencto\)

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Desabilitado

Neste campo será exibido o valor do ICMS\-ST referente o 1º Vencimento, conforme prazos constantes de Convênios e Protocolos ICMS\.

Essa informação deve ser processada de acordo com a RN00 \(Vencimentos\) do documento matriz: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

*Observação:*

Só é editável quando habilitado\.

MFS2283

Vencimentos – Valor do ICMS\-ST \(2º Vencto\)

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Desabilitado

Neste campo será exibido o valor do ICMS\-ST referente o 2º Vencimento, conforme prazos constantes de Convênios e Protocolos ICMS\.

Essa informação deve ser processada de acordo com a RN00 \(Vencimentos\) do documento matriz: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

*Observação:*

Só é editável quando habilitado\.

MFS2283

Vencimentos – Valor do ICMS\-ST \(3º Vencto\)

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Desabilitado

Neste campo será exibido o valor do ICMS\-ST referente o 3º Vencimento, conforme prazos constantes de Convênios e Protocolos ICMS\.

Essa informação deve ser processada de acordo com a RN00 \(Vencimentos\) do documento matriz: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

*Observação:*

Só é editável quando habilitado\.

MFS2283

Vencimentos – Valor do ICMS\-ST \(4º Vencto\)

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Desabilitado

Neste campo será exibido o valor do ICMS\-ST referente o 4º Vencimento, conforme prazos constantes de Convênios e Protocolos ICMS\.

Essa informação deve ser processada de acordo com a RN00 \(Vencimentos\) do documento matriz: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

*Observação:*

Só é editável quando habilitado\.

MFS2283

Vencimentos – Valor do ICMS\-ST \(5º Vencto\)

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Desabilitado

Neste campo será exibido o valor do ICMS\-ST referente o 5º Vencimento, conforme prazos constantes de Convênios e Protocolos ICMS\.

Essa informação deve ser processada de acordo com a RN00 \(Vencimentos\) do documento matriz: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

*Observação:*

Só é editável quando habilitado\.

MFS2283

Vencimentos – Valor do ICMS\-ST \(6º Vencto\)

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Desabilitado

Neste campo será exibido o valor do ICMS\-ST referente o 6º Vencimento, conforme prazos constantes de Convênios e Protocolos ICMS\.

Essa informação deve ser processada de acordo com a RN00 \(Vencimentos\) do documento matriz: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

*Observação:*

Só é editável quando habilitado\.

MFS2283

Vencimentos – Valor do ICMS\-ST FCP \(1º Vencto\)

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Desabilitado

Neste campo será exibido o valor do ICMS\-ST do Fundo de Combate à Pobreza referente o 1º Vencimento, conforme prazos constantes de Convênios e Protocolos ICMS\.

Essa informação deve ser processada de acordo com a RN00 \(Vencimentos\) do documento matriz: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

*Observação:*

Só é editável quando habilitado\.

MFS2283

Vencimentos – Valor do ICMS\-ST FCP \(2º Vencto\)

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Desabilitado

Neste campo será exibido o valor do ICMS\-ST do Fundo de Combate à Pobreza referente o 2º Vencimento, conforme prazos constantes de Convênios e Protocolos ICMS\.

Essa informação deve ser processada de acordo com a RN00 \(Vencimentos\) do documento matriz: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

*Observação:*

Só é editável quando habilitado\.

MFS2283

Vencimentos – Valor do ICMS\-ST FCP \(3º Vencto\)

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Desabilitado

Neste campo será exibido o valor do ICMS\-ST do Fundo de Combate à Pobreza referente o 3º Vencimento, conforme prazos constantes de Convênios e Protocolos ICMS\.

Essa informação deve ser processada de acordo com a RN00 \(Vencimentos\) do documento matriz: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

*Observação:*

Só é editável quando habilitado\.

MFS2283

Vencimentos – Valor do ICMS\-ST FCP \(4º Vencto\)

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Desabilitado

Neste campo será exibido o valor do ICMS\-ST do Fundo de Combate à Pobreza referente o 4º Vencimento, conforme prazos constantes de Convênios e Protocolos ICMS\.

Essa informação deve ser processada de acordo com a RN00 \(Vencimentos\) do documento matriz: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

*Observação:*

Só é editável quando habilitado\.

MFS2283

Vencimentos – Valor do ICMS\-ST FCP \(5º Vencto\)

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Desabilitado

Neste campo será exibido o valor do ICMS\-ST do Fundo de Combate à Pobreza referente o 5º Vencimento, conforme prazos constantes de Convênios e Protocolos ICMS\.

Essa informação deve ser processada de acordo com a RN00 \(Vencimentos\) do documento matriz: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

*Observação:*

Só é editável quando habilitado\.

MFS2283

Vencimentos – Valor do ICMS\-ST FCP \(6º Vencto\)

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Desabilitado

Neste campo será exibido o valor do ICMS\-ST do Fundo de Combate à Pobreza referente o 6º Vencimento, conforme prazos constantes de Convênios e Protocolos ICMS\.

Essa informação deve ser processada de acordo com a RN00 \(Vencimentos\) do documento matriz: MTZ \- ICMS \- GIA\-ST Geracao \(Registros\)\.doc\.

*Observação:*

Só é editável quando habilitado\.

MFS2283

EC N° 87/15 com Movimento

Texto

N

S

Formato: 

Check Box

Default: 

Habilitado

Este campo indicará quando houver movimentação referente à Emenda Constitucional nº 87/2015\.

A opção virá marcada quando via processamento \(geração dos registros\) gerar valores para diferencial de alíquota à UF de Destino e FCP, mas também será possível o usuário efetuar a parametrização manualmente\.

A opção marcada indicará “S” por existir a movimentação e a opção desmarcada indicará “N” por não possuir a movimentação no período para aquela UF favorecida\.

__Tratamento:__

- Se houver movimentação para a EC e o usuário desmarcar a opção, emitir a seguinte mensagem de aviso: “Existem valores referentes à EC 87, deseja excluir as informações?” \(incluir OK e Cancelar, em que ao clicar OK serão excluídos todos os registros da EC da aba Anexo 4 e os valores da EC da aba Principal serão zerados e o Cancelar não irá desmarcar e nem excluir e zerar os registros\);
- Se o usuário marcar a opção da EC 87, mas não houver movimentação, emitir a mensagem de aviso: “Favor inserir as informações referente à EC 87\.”;
- Se o usuário não marcar ou desmarcar a opção, todos os campos e a aba referente à EC 87/2015 devem ser bloqueados para digitação\.

MFS2283

Valor ICMS Devido à UF de Destino

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Habilitado

Nesse campo será exibido o valor do ICMS a recolher de Diferencial de Alíquota, ICMS este devido à UF de Destino de acordo com o exigido pela Emenda Constitucional nº 87/2015\.

Para o Estado do RJ:

Esse campo deverá ser preenchido com a somatória do VLR\_ICMS\_UF\_DEST \(Campo 284\) \+ VLR\_FCP\_UF\_DEST \(Campo 283\) da SAFX07\.

O campo poderá ser alterado pelo usuário, ou mesmo inserido manualmente, conforme os demais campos da GIA\-ST\.

MFS2283

CH4823\_2017

Devoluções ou Anulações

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Habilitado

Nesse campo serão exibidas as operações de retorno da mercadoria devolvida pelo cliente \(comprador da mercadoria\), em que se referirá aos valores de ICMS da UF de Destino da origem da venda \(saída\) de acordo com o exigido pela Emenda Constitucional nº 87/2015\.

Para o Estado do RJ:

Esse campo deverá ser preenchido com a somatória do VLR\_ICMS\_UF\_ORIG \(Campo 285\) \+ VLR\_FCP\_UF\_DEST \(Campo 283\) da SAFX07\.

O campo poderá ser alterado pelo usuário, ou mesmo inserido manualmente, conforme os demais campos da GIA\-ST\.

MFS2283

CH4823\_2017

Pagamentos Antecipados

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Habilitado

Nesse campo será exibida a totalização dos valores de ICMS de UF de Destino recolhidos antecipadamente, nota a nota, por intermédio de GNRE, em decorrência de inadimplência de pagamento ou de entrega de meio magnético ou de entrega de GIA\-ST de acordo com o exigido pela Emenda Constitucional nº 87/2015\.

O campo será preenchido manualmente, conforme os demais campos da GIA\-ST\.

MFS2283

Total do ICMS Devido à UF de Destino

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Habilitado

Nesse campo será exibida a totalização do ICMS devido à UF de Destino, que será correspondente aos valores lançados nos campos Valor ICMS Devido à UF de Destino deduzidos os valores de Devoluções ou Anulações e Pagamentos Antecipados\.

O campo poderá ser alterado pelo usuário, ou mesmo inserido manualmente, conforme os demais campos da GIA\-ST\.

__Tratamento:__

- Realizar o seguinte cálculo automaticamente quando preenchidos os campos Valor ICMS Devido à UF de Destino, Devoluções ou Anulações e Pagamentos Antecipados: \(Valor ICMS Devido à UF de Destino \- Devoluções ou Anulações \- Pagamentos Antecipados\)\. Se valor for negativo, zerar o preenchimento\.

MFS2283

Total ICMS FCP

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Habilitado

Nesse campo será exibida a totalização do valor do Fundo de Combate à Pobreza \(FCP\) da UF de destino de acordo com o exigido pela Emenda Constitucional nº 87/2015\.

O campo poderá ser alterado pelo usuário, ou mesmo inserido manualmente, conforme os demais campos da GIA\-ST\.

MFS2283

__ABA ANEXO IV – EC 87/15__

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Data de Vencto do ICMS Devido à UF de Destino

Data

N

S

Formato: 

Text Input DD/MM/AAAA

Default: 

Habilitado

Neste campo será exibida a data de vencimento referente o valor declarado para o recolhimento do ICMS devido à UF de destino

O campo poderá ser alterado pelo usuário, ou mesmo inserido manualmente, conforme os demais campos da GIA\-ST\.

MFS2283

Valor do ICMS Devido

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Habilitado

Nesse campo será exibido o valor do ICMS devido à UF de destino por data de vencimento\.

O campo poderá ser alterado pelo usuário, ou mesmo inserido manualmente, conforme os demais campos da GIA\-ST\.

MFS2283

Data de Vencimento FCP

Data

N

S

Formato: 

Text Input DD/MM/AAAA

Default: 

Habilitado

Neste campo será exibida a data de vencimento referente o valor declarado para o recolhimento do ICMS do Fundo de Combate à Pobreza \(FCP\) da UF de destino\.

O campo poderá ser alterado pelo usuário, ou mesmo inserido manualmente, conforme os demais campos da GIA\-ST\.

MFS2283

Valor do ICMS FCP

Numérico

N

S

Formato: 

Text Input 0,00 

Default: 

Habilitado

Nesse campo será exibido o valor do ICMS do Fundo de Combate à Pobreza \(FCP\) da UF de destino por data de vencimento\.

O campo poderá ser alterado pelo usuário, ou mesmo inserido manualmente, conforme os demais campos da GIA\-ST\.

MFS2283

# <a id="_Toc480792188"></a>Sugestão de Layouts

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA0UAAAGLCAIAAACHmK4PAAAAAXNSR0IArs4c6QAAgtBJREFUeF7tnWXcJMXZrw+Lu2uQAEEXd1/cghPc3d0tOMFlcQvuDiE4hOC+uAd3WLK4n3Ox955+++2xnpmeeeaZ5+oP85vpKb2quuvf911VPdxPP/30f/73wZmRRhopczLPzx9++IFgo4wySp7ApWHMNyc3OecEFcHsVzlx2a9ygrJf1QXKflUXLu9XOXHZr0pB9cvJzmASkIAEJCABCUhAAp1JYLiwz2299dYXXnhhZxbRUtUkMNNMM9UM08cD9OtX2KNLwxboPt4EVj9NYNFFFy0EyPfff19IOiTy66+/FpLUGGOMUUg63333XSHpmEg7CYw22mhFZTf//PMXklRj/sbSrIcbbrhCykMik08+eSFJjT/++CQVFfz5559/90ZxzD333IWkbiISkIAEJCABCUhAAu0hMOmkkx5//PEIuWH2uQUXXPCpp55qT949lQtKtpCsJ5pookLSMZE8BJZaaqk8wWqGKZ0nWjNKpQCffPJJw3HTESeeeOJC0imqPIUUpthE3njjjUISLNDS89ZbbxVSJBOpSWDssceuGSZngKI6wO8mkCKOAi09c845ZxElKsw6++yzzxZSHhOpi8Bf//rXAw88cJieGzBgwCOPPEL8//t//29dqRhYAhKQgAQkIAEJSKDNBOaaa65nnnmGTE877TRmzQ2bVPTHP/6xzeUwOwlIQAISkIAEJCCBxgicfPLJEfG1117jc5ieK3BSbWPFMpYEJCABCUhAAhKQQGMEhum56kv2cMLqh22Mr7EkIAEJSEACEpBA6wgMHjz4f+xzE0wwQdmc3n333SOOOGKGGWZg0uV5550XcSodzMDbf//96y0xSnGnnXZ65ZVX8kQ84IADmEW+3HLLffXVV1XC//3vf1966aWrlzZPdvWGIce//e1vFPL1119/6aWXrrjiinpTuOCCC2666aacsf71r39ttNFGU0899WqrrXbRRRdVZ3LCCSfccccdOVNOBzv77LNvuOGGPBE//vjjdddd95tvvqkUmFbee++9TznlFED94x//eOKJJ2om++KLL84xxxzjjTfemGOOySRivnDMN998n376aRL3t99+22abbQBOd91www1jn8nGDpK98cYbSbA0emPdu7FiGEsCEpCABLqJACKKISx9jDvuuGWHe8b01Vdf/Z133slUn6GTvxjrS7F88cUXnBxmn/v6669LQzD6LrLIItdee+0ee+yx/vrrH3bYYZtssklEK3uwD8qqq65abwOw8oipfC+//HKeiMsuuywjLqWqssURSW2xxRajjz768MMPnyfNAsMce+yxL7zwAjViluLyyy8/8sgj15v4v//974cffjhPLIItscQSk002GYJ71llnPfLII1F1VSTsfffd9/TTT+dJmTCXXXbZLbfcEoHnnXdeFBVfPvvss1122WXIkCGVEkFy0UMq7T/E7lYrrbQS+8AhQ9kfhzYifM3yUEHkPouxt99+ewKzhIfve+655zjjjJPE5QpZc801//CHP7z99tuU/PPPP6+ZbKaOEf7bb7/daqutjjrqqF9++aU0hca6d56SGEYCEpCABLqYAOJs0KBBmQr+97//3XXXXUtrzUCGWYFh9/7770/+3WyzzQjMXxylUVAOv5+M/ecYhiNEuFY5mFG30EIL/fnPf0YixBlSmWWWWdZee+0kTPNfyJpBlHxRjXlSCzFx8803Vwl89dVXTzHFFKQcYZARmFvyJN58GBTPjz/+SHbPP/884imdL8Wonj4r4Qmz5ZZbop7zlOSYY45hL48ki9hGAbFfKS6KB0WeJ2XCIN+xMmYCP/bYY2TBFhI5EykN9uGHH1JgmgYxSoHTAWryCeMiWq1K7iGFuXLylLC0jhQJFf7qq6/miW4YCUhAAhKQQB4C6DPGpsUXXzwdONahYuDIpLDpppsmiu2QQw5BemGsSc7wMwmP4Es2YmNgrbhpPnkwOmJwwiQYCU011VSoLnydfD/99NNxw8V5Qm633XZ8efDBB3fcccc4ibLBYrTwwgtj0SkrJxk7sYWwrzGOUcLH1uQM9ni1kB3YnB5//HEKndSh9Av73DAkX3nllUsuuSSbrYc+RUWhh95777211loLKwtVQJVS4W233RZnHAGee+45JCl+4emnn/7MM8+85pprMPzstttu88wzz0knnYQHkEW/uPMGDhyY7JZeti7I3DPOOGOBBRbA4/nRRx9F8XBbU34sTzvvvDOriMPMQ77kiLEQ69Sjjz5aWhFEKjYhzEuY2WieJF+ctieeeCJFvf3225GJmYiYuO655x4MsLH9GK1z7rnn9u/fv1LrYCy87rrrMHACBNtb4lLEoLj55pvzhomDDjroP//5D9EvH3qQMhD4STUvueSSL7/8Ekr8pGMhy3Ct0hP45AzVxM1KfeGQ2Agr8SFlmgbn75tvvhk1qskngsUGciOMMEL8pDB0dJDSWO+//z4XAE0fFlm6HEbpfffd94MPPuAn3ZI2ir5EXkShLpk68hd6+qGHHqJD7rPPPoAt7Srp7k1z4NNfccUV11lnHWKVtqlnJCABCUhAAkEgjHPh6UqOSvuKsGo1CckwR7CQgxy8x4uxPp1IemPdinoOXYKjbcYZZyQmwuL8888/66yzsJFMN910nEEnoZkiUcZI/kIfsGI2PLuM5WussQa2IsZRnLb4yzKNipmRQR2dxJw8RAz/hp0JRYXaQHJhCuJdH+ecc05G0sU2jMnYzAQ1RCFmKorKxCnGdWrOAI/WQZYhOxi84XLcccdhs0EBMLOKL2g4ZBOyD78txUPVEXKDDTbYfffdiYs8wiqJJojZXWXrgiBYb731QIwWZLoYcjaKRJUR4GyDidZB1d19990M/JSQmjIxDocdsUJWJgcVxxKGTZFmQxyAOvQc7lEUJwkiSlZYYQUKn9kSE2crtNG+k0wyCYRRFWiaaaedtlLrgA4FDFVMUKussgrT1wiJcRSL4FhjjbXXXnuxoTR/IdGAOfPMM5MpdSEMHJjERqXAwk8kOzPYaP0777wzioTSuuqqq9CCYKTAeOTL8qGmlJZmAjteVHQ8KGrySUAF4WQfTrTpoYceisEYEzQeXlCQWvxL70KToS/RqVQQ/ztSLNKhbLfeeisu+0wdk7LxYIBxN8qW6SpJ96aBSJ8egjgGC9Bo30wP96cEJCABCUggCIRVKyPgQrRhEctQYljhZEb8EYbBLnGllgcb/lbsK/F3Ysdj6GXMCy8YgyUvlJh99tkpDTKCM4xhmFgi8KWXXkpEzBuIM96dwJnDDz+cgZYBnu+Y9PiXYTVtUUS+cJIhk5NheSIR5rPzJaQhBxOh+InRJR0x5vkhpDiJ15XvYcaLeWMM1XzHLohe4QvT8hZbbLHIOtyRzOuPWInT8Oijj0b8RRgC46JG85E7spJ5WpXqQtlQuogDAqD/UDZ8QSVQ/YMPPhh7FT9JFvtWGG9QaZxB/cANu1G6RjFxEAtcnNxhhx0wJeLsRlGhtKIwSHtSRpinI8Z3lASmppi2iCSlMJVaZ+ONN0b2RSwWJdCakCc69lek5JNPPklcZBnylABIrqR9UWD77bcfJ5Gn5BJZhF8f8cf3WH9A3FDAsC3L54EHHogmIEqIWs7U5JNUOebzodXiDF0Ry2U8BsRCEHpFFABnNydxm0Z2PCQss8wyESv2LkeeZupYtmyZrpJ079tuu41E7rrrLhKJdTyZXlraTJ6RgAQkIIE+SyCMIxnXatmTgYiRLu11HarO/g+zxhEDaYYMxNh9+AsvZTV/KyM6o2MMV0gBTC8khGLAGsQZdF7y5pPEZsbgiqUE7yFTu8LnRchw12Ym0TPko2wwhPBXeNBIMLY5Rs0wZZ6DvPgZJzMH9eFMONfCXhi5hJkEx2LIPjx6KNyYns/wj2kKq1LEwsIUafIT61SEYeUsZSY6NaKayK9KdUHTUPjIFB9rvP0WJx2SDltdZAFl5E64/EKVjzrqqJh/Mis/Qtkk72whd1DE8lgEBPvIgIJakDIWuzQHXLc4WMkdmx+qBUmBAenUU0+t1DqozOT9OX/5y19QNtifiI6hjkLibiYXChNrOChDYgmjWeNl9ulVn/E9HMoRMlR4/CzLB7MoNj+kNmFgzicqvCafbNv//9+QoQnS9loKGR0jWhP+KFEoUaqYo8kRFYlg6TqWLVumq0T3JiLeZ1KOeQKBFHtkpXJ6XgISkIAE+jiBWMBXuiSiLBaEB1IPC07mX0Qe5zNqKpYVxkg0zN8aAzOCI4nPAI+NDYWYzHNC2zFnKOblYb5CvkSsMH0xUjJAMuAhErHxJIIpmWKVLhnWJlILs0pYdxhiWZHKF2aMYb3D5oSNh08cppX6QYzl4Z0McTniiCNGLcJcxzYrzK4LkYd8wYeLUSoRH5EsY3YyXy1JjS9YyEitUl143S3mmVBmGOGQxpQf/Ye7MxhCgDEeA1ho1niXGo2BtRIDZ7pGAQpPcUBAiVKeSARNTHh8yqDgwKiWjghYHMSxlpNKMQFuyimnDKRlW4fChBkySsIna4RRgbgO8dZDCe82XtfocLjkkzWesA3NHaUKXKFQw6QaE/ggGXqOnlCWD70Qj3Pwj1XSpFyTT1LltBTjJEVKShhFogBxJnoUJxGL4MWSyvSAEI7xGUItXceyZct0lejeRKRlMVdHwaJ3FfVWx3T7+l0CEpCABDqWAH5LHHoM6BzpXUjiDFOk0qtTw3maTIOLSsVom3HChphLlB/f8dXiQwtFyNidvBMiEmGiFJ9haPtdeXAwr5/vWInSpjxSRKBw4MEkCUQYE7zCH4dLi/BsG8FbYPmCMuAkE+fxEvKFmfUMoggdfIuRZbhWk4OJ8wzkGJYwQcWsLJQiWoSZcJhw8L3i/wIWIiZjng1AKBuKEW6vWPAYAiXWvYajliEW+xPjLmkiU7CloU0Z6dOxCMzUuvAgc2ARTBZ1IltjNWjZupA4SxwwNeHLIy8kESExYZIdtkxWijCzivNM0SNHJClGRFyW4EVQEixdKZJiKiG2Q4xt2CaJRTkRRqRJLOb2YaHF/IbMzfisYUh2FAPBB2pcitQRgVWpdTCIkjj7tOHRpplw7BIyFkCwCcjFF1/M4hISjMWheMzRZKhJFBILY+lMnOQvGpqKIPH5ifeWGmERjJSvv/76WF5K5yvLJ+yLEKa0Mc+P9GvySVjhTCdKsto63Nnxb+Jtj4kIcGO9TizNoaMikcEOKDzIVJyTGDIzdSxbtkxXSbp3eH7pHiQYwi5xl2e6qz8lIAEJSKArCYS2qX4kFU9WhSLLkGiM8slOJRk4iZJD56UnWZECUULqJVESyYjY+H3n15g/x4BHsTJ6jjiYXlByTCxjjES7YJlIEmIMY4IdxeI8KoHzzK+KvTYQmEw+IzWkDIqE8T4dMVJgWWXM+mK5ADoGARcRCc9aCnQDsZiSlakqM9yJglhEUqBdUEIIAsJgTkN2YDDjOy5aUo79SjDLoRoZxdFtUYZ0LH4ilZjxFrmwohMRGd8pBlqzSl0oAHou9A3O0IhF1njiyA7uCJdYz4HwQtfSNix6jTmFmQPIWNpICi1LLLQIAZBEKCTgIKMhyUJj6piJiHWNOXZICrQX8iKdeGnrUAZahxahJDjEUTmRGhoILUj7Is1DqHGgjwmPykQugy5pCGYKoo8R34RBRfEIQlvAClFO3elwkKcR+beUDyIVwY3SpdtQHdQzZss8fKJITHqDbbINDdjRW/EXpkdamWU0hIEhUpg6UqSYW8lBx6BTUXJEM9dD9IR0HcuWLdNVku6NxsWETDrYQbk6kP50s9Jm9YwEJCABCXQrgVpa7vf/03VHnKW3TY3oDB+lfFBsmXlylRgmeo6JXgyOw8U2EPieGOAZ1OOtrqUHySUTqur9t0q1yZ0dIvInGLUK22Yemi0Nw6QroKPSmHjXfEagwMNbWq/q5KPHVKeRCVAzfFKXsiHznyyWT12Eq9SxYRp1FcDAEpCABCTQxQSqD7s4WNFqWIsyBHBzYfgIVxJGgQEDBjSDiG3aIgUcg1ighum5EFXYY8pukNZMft0aF1mAUQ0LEBCZu9at1Wy4XvJpGJ0RJSABCUigwwmkp8eli4qSS5YetroKiZ7j/WC40dRzjQNHshC5EyyFjdehlTHl00q6pi0BCUhAAn2aAHqOmUusp2RCOfOXKu4n3Kch5at8h7h98xW2B0LJpwegm6UEJCABCfQZAskbvKjxMD0XL2nQ1NRn+oAVlYAEJCABCUigdxOIXbRi5cMwfyurFFkdybz+2DKjo47SJSGNFS92HvaoQoB3yBbFh83wikrKdCTQOQSYztw5hSm2JLENu0ffJPD7bhcevY0AnlZ2F4lS/8/61rKLTHtb1SyvBCoSiE20CznY3qWQdIbtAFlIWgUlwvtCCkqpmGRiu+yOOtiWvJDyFCWeKu1IUEghTaRFBJL99luUvsn2KQLsHcYuYL+/PDP2n+M9VPEWMA8JSEACEpCABCQggQ4nMOH/P9j65H/sc2yly0sUKHqsSWz+iBc2FHLkfOVZIXnlSSR2jumoo9LC6R4sZFGtVmBH6kEaZi2BvkOgqBky8YqkjjqKmrTTv3//jqpXdxcmXvPY/FHgYBRvN23+4JX01113HemsvPLKfBk2f65wPdd8QU1BAhKQgAQkIAEJSKAsAZY9xMszeb8lLwV1vxL7iQQkIAEJSEACEujdBNRzvbv9LL0EJCABCUhAAhJQz9kHJCABCUhAAhKQQO8moJ7r3e1n6SUgAQlIQAISkIB6zj4gAQlIQAISkIAEejeB7PpWlogXtdo8DSaz0LeozSx6N/tapWdHmXSQTTfddJNNNkmf2WyzzS688MIWNVmSUekibZuvVtPl/T/TxETrqVaOEtvWeVuuoHAd1QHKbsfgxV5QU2eT6aimL3vtc9LWb1Hrp5Mt7QllB4KyJcmsbx22n/Bxxx3XhnKbRZMEaHg2CEyOJlMzemcSsJU7s13aVio7QNtQd1pGNn2ntUgPlifTGdJDf/L9zTffjBKyX8nv+wl/9dVX/Dj77LNjP2G+tKICY4wxRjrZGWaYoRW59PY0M68AuuWWW9I1Ouecc3jF3q677nrSSSfF+eGGG651TZZknWk7ztt8jfW00lc8ZZqYZHuqlaNGtnVjLZszVod3gNLW92LP2bI1gzXT9O3Zwb6sX2722WevWTUD1EVgyJAhmfA42UpTOOSQQ7CXp4f7srmk7XNHHXVUVs89+eSTdRXOwG0jwFW95557kt3bb7891VRTJXrOJmtbE7QhI1u5DZA7OQs7QCe3TkvLVqnpi3ppU0sLb+LFErjppptWW2219HCfR8/1G2XoUWxRTK0VBLC+zj333KR84403tiJ90+wEArZyJ7RCD5bBDtCD8Hs2a5u+Z/l3VO6rrrpqzKvLP9wj5P7X+tbpp5++o6pkYTIEDj74YM5giU3O22Td10ls5e5r07pqZAeoC1erA+Mq/eGHH1qdS6Rf2vQd+BLb9qAwl/DDpof7mkz+l54bc8wxa0ZoW4DBgwfjD2ZW33rrrYef8R//+EfpFAQK89xzz51++ul1laqBKKR/xhlnPPHEE3VlVHjgySabjDkuuNWfffbZSLz5JsOYf+yxx5ZO5Cq88EmC33///Q477LDiiiueeuqpOXOJKBtuuOEyyyxDfzj//PPfeOONnHGrB7v//vsvvfTSepPC5T1w4MArrriCyRAPPPDAiy++WG8KVcI30Mqvvvrqdttt9+WXXxZYjJrcoi2YkAuNv/zlL7wQ+t57781ZAIp6+OGH06DE2mabbeiBXFy//vprzuitCPbFF1/sv//+3333XSsSryvN3t4BuFXSN3baaadvv/02Z8VPO+00omCQmGeeefiM7zfccEPO6DmDceffaqutXnnllZzhCfbhhx9yZe2yyy68+Dx/rCTk9ddff9999+WPWNr0rdhuIn95DNmDBJhVReunh/uahflfeq6sYKqZRIsCcP1wMUw99dQbbLABfsbLLrvsb3/7Gys4MtlNPPHEAwYMqKsMDUQh/UcfffStt96qK6NWBN56661JNtHszTfZu+++e/XVVzMNP//Nt8l6jTzyyIssssinn34655xz5kyK4f+xxx7jXo+qW2mllZCz6667bl03ykoZoQvrXZP/22+/7bbbbv369Xv66adRJIcddtjoo4+esyI5g9XbynfccQd6CGWZM/3mg0033XR/+MMf/vjHP0400UQTTjghVyg2jPzWYsZUJoig6RFzSy65JHEZNU8++WTYNl+2xlIYbbTR6FqFTz55+eWXL7jggnqL1Ks7wPzzz88Fy1T6UUcdNWfFF1hgAS7t3XffnZeLL7jggizW43ux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fAJ12OcGDBiwySabHHzwwXlq9fLLL7PIbqaZZmJNHBHPOeec9957L0/EBsIwYDONJucEGvbluvnmm9O5/OMf/zj00EMbyLeoKBdccMFNN91UM7Vvv/126aWXnmyyyfbZZ58k8AsvvMDPOeaYY8UVV7z44ot//PFH/mJtID/vuOOOTJq0wn777cfJn3766dJLL2UB49RTT73VVlv985///OWXXzKBC2lBJNQ222wTix/TR84qJ1GY7U4TQ6CUEgu211133e+//z75C0v1Ouus89133z377LNTTjklO5+xPxkuSD4BVakf1tWLYM6ebbTFn/70Jzb+YSNvkNZsweoBzj777PzLOasn9fnnnzdTGOqy8847P/bYY3UlQu+66KKLemoFxu23315XaQ0sAQlIoMsI1KHn2E/4wgsvzLmZMGMqO2BtueWWRx555HLLLXfqqafOP//8r776ahV8PNzfcsstDfBl5D7ttNPQH3niMlYdd9xxWGsi8M8//3zUUUcVYrlpuPz//ve/a+7vQFFHHXVUFNhHH3202GKLReHBxb4PgwYN2nzzzWeffXbU9r777kuNEDe33Xbbeuuth9pLmNx9991IK/LizHnnnbfHHnuwChJ1TrJ//vOfESgZCA20YCl/1umsueaape6/nFVOEpxxxhmvu+46dr0uzeKNN95A7aWl3scff3z11Vd/+umn77//PurtzDPPRLzSOujdvffee8IJJyzbT+rqRTwSTDPNNDwG7LrrrtDmRXt8b6AXcY3Q/aI87JqL3MzTh1sdhh71zDPPLLPMMvkz4hHirLPOogcmK7Pyx20yZPSur7/+usl0jC4BCUigdxNA34TEiWrweF3IgZ4gtS+++CJS++abbzbccEOGPW67ldJff/31DzjggHpzp/Axll977bV54oagef755yPwI488ws+nn346T9zqYUrLj2qsHgXtRRhUL+oqCYmprFKsMJm8+eabBEAcszk+5sYffvghwodB7sknnxw8eHC05oILLois4S+2+Jpiiik4s9RSS/FzkUUWOfbYY5Ncbr31Vv5CGKXzbaAF8zCst8pJmo8++ugTTzxRmkXYtNL9CjnCGfjcddddfMETV7Ng9faiOeeck0eIJNl77703fw9MFwabHO1Ss3h5+kY6kTPOOKOZyxmVv8QSS1Tph6UFji6EgM5fl0JCci0kL7co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gRl++OFbVFSTlYAEWkEg2XCqph5L5s9xQ37wwQfr0HMsiGMdGYf7z7WiCU1TAkURmGeeeZ566qmiUjOdXk1g4YUXPuyww5ZccsleXQsLL4G+Q6BxPRcPmmi1mva5/Hn0He7WVAIdSKAxPZe8HyJqlPnZTDVXXnnldPSRRhop/fOTTz5J/5x44omr/Fu9GC+99FI6QMaK9vDDDzdTi3TczEtjhwwZkv733XffTf8ce+yx0z/XWGON9M/MvjA33HBDUYVM0rnxxhtXXXXVwpM1QQlIoBUE8muttH3u7rvvHk4914r2ME0J9CABjDHxLuea5voeLKRZt5rAbrvtdvLJJ5PLVVddtfbaa7c6O9OXgAQKIdCwnuvHhAwXQxTSBiYigQ4hUHNv3g4pp8VoKYGddtop0n/llVdampGJS0ACPU4AIed+JT3eChZAAgUTGGGEEQpO0eQkIAEJSKCzCbRKz+HWxcKfnr/yzTff8I7FN998sxTIgQceeM899zQJ6sknn2RZX55EDjjgAOboLLfccknxfvjhhwsvvJACTz/99HvuuWfyOLvrrrsef/zxmfV3jzzyCJNRqA55Me9wo402mnrqqVdbbbWLLrqodNXbt99+u+yyy84111wsNOMdR6w6fO655xrwgp199tmlE2vyVzkPFsN0DYECp751DZO+XJHPPvusL1ffukugdxFAIbz11lsxZ6auo1V6DgfwNddcg/RJSsNmKkzjKLt4nt1SXn755brKXRr4+eefj8kiNQ8E1qeffrrIIovEHgSIMIQmvolppplml112efrpp5l+xCd/sUhwr732oiJJmuzysskmm9x8883MgGZ6NS8+n2yyyVBpzI8+8sgjUXWDBw9OF4A76V133UWCxx133MYbb0yU2Wef/aabbqpZyEwAti1Iv/Iy/s1f5XqzM3yvJjDVVFP16vJb+GIJZFacFJu4qUlAAoUTaGo/4VaUhgWzt956a6SM3rzkkku23HJLSlmaF+6htA2s3v2oCP/rr7+yXxQ2syQuZypVas455+Qv5FFsMXXUUUexLO7xxx8/+uijd9hhB9aCLbXUUqeeeip/xVI7ih27P/z444+7777766+/zneEKdu9EJJYG2ywweGHH37nnXciqDmZzjf0KyvatthiC+Lecsstp5xyyuabb17vjBYsfFgBk5TrrXLh7WuCnUzg888/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Yz0Em85vttlmhx56aG+HZfkl0N0ECtzAtsNB7bTTTlHCV155pcOLavEkIAEJFE4gPC3x9sI69Fzh5TBBCUigFQRGGGGEViRrmhKQgAQk0LEE1HMd2zSNFAz/GksRf/3118YWJDaSpXE6j0DNuXGdV+RmS/TZZ581m4TxJSABCfRmAq3Scy+//DKTsmeaaSbmUA8YMOCcc8557733WgQKEYPbJafDhX0cbr755nRJ/vGPfzTvRH7kkUf233//FlUwT7LPPvvslFNOya4Q7N2AeYZPXjEZzH/44YcLL7yQ2UXTTz/9nnvumYC6/PLLN910U9YGLrDAApzvUysi8yDtvWFY695k4R8cetSVCDNrL7vssrqiFBi4dIlGgYmblAQkIIHOJ9AqPffWW2+hD7bccssjjzxyueWWO/XUU+eff/5XX321ChEGg1tuuaUBZN99991pp52GgswT96effjruuOOwYEXgn3/++aijjmremjX55JMXvryOUh1wwAE56/X++++j3s4888xLL70UkhdffPHee+894YQTsuRw3XXXRe9OM800u+yyy9NPP81keT6p+zXXXPPhhx9uuOGG2223Hd539HfN3W7yEDZMjxP4/PPPmykD18jOO+/82GOP1ZUIz2wXXXRRT63AuP322+sqrYElIAEJdCYB7qIoqFjTVt/BvZvjjDPOiGgkVOlI0q0SJvnrtttuI/wXX3wRZ7755ht0w+KLL45uqBR9/fXXR77kSTwdhsJ/++235HXttdfmifvvf/+bwM8//3wExq7GT/RNnrhtDhO7OWBNTPINR2rZYtx1110ExkqR+XefffaZbrrp2E4izpMmDYFZju+LLLII0jbOk+y+++47++yz//LLL22uptkVTiDP5Vwl01ByWHzzF+zLL79ka1+eJfJHKSTkm2++mTiXC0nQRCQgAQn0FgLpGyBaqFX2udgUHutXqMDRRx8ddyTmHwaJOIPC2HXXXfH0HXPMMdiQ8P1xnHLKKQMHDowATIjBtoc3EKsSrpxSlYqA3Wqrrdgfa+mll+bfMLmhS5BobC6KX/Xxxx+nVTIR55prrimmmCIxROFsRWXONttsOCVvuukmBCWmRPboIxbShy24MGJtsMEGLBjE/JCk9tprr2HTwqF5+umnYx0kMM6pHXfckYqsttpqGPxWWGGFddZZ59FHH2VkxR6GhSzx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08zPZqq/8sorp6OPNNJI6Z+ffPJJ+ufEE09c5d/qxXjppZfSATJWtIcffriZWqTjzjrrrOmfQ4YMSf9899130z/HHnvs9M811lgj/TOzb/MNN9xQVCGTdG688cZVV1218GRNUAISaAWBdui5/Hm0ooamKQEJ5CSAMea+++4jsNMnchLrymC77bbbySefTNWuuuqqtddeuyvraKUk0H0E8mutxvcT7j5q1kgCXUmg5ruzurLWVipDYKeddoozr7zyinAkIIGuJ+D61q5vYivY5wiMMMIIfa7OVlgCEpBA3yagnmtH++P2YhHfr7/+yqcusHYQ79t5FDj1rW+D7JLaf/bZZ11SE6shAQlUJtAqPYdblxkb6fnILKZdd91133zzzdLCHHjggffcc0+TzfTkk0+yTUOeRA444ADmXC+33HJJ8X744YcLL7yQAk8//fR77rln4p7Yddddjz/++Mx+Co888giTi2OfF9aIbLTRRlNPPfVqq6120UUXle5iwERptkVg7wN2DcBqwuf4449///33E5dk77zzzm222eZPf/oTiSQEPv30U06uvvrqzLkmWbaSycy2zlNHw/RlAlNNNVVfrr51zxDIrDiRjwQk0MkEMPq89dZbMQe6rqNVeo4Jfddccw3SJykNIoZpuWU3Q7r99ttffvnluspdGvj555+Pyb81j2WXXRbNtMgii8SeUogwhCZzTaaZZppddtnl6aefZjo5n/zFpg977bUXFUnSfOeddzbZZJObb74ZjcVyuSWWWGKyySZjry+015FHHon8Gjx4cLoA/HzwwQcRrJdeeulll112ySWXnHTSSahGxBybCKApWWO8xx57IPiWXnpppBtxX3/99XPOOYcpUChL0j/xxBORdz/++GPNehlAAkHg888/F4UEEgLcYKUhAQn0IgKN7Sf8f9ATHGeccUZUFWFY6UhYVAmT/IVeWWWVVRBJcYaf66yzzpZbblk27vzzz3/KKackf+GXzJNFOvwvv/yCgY0SJnE5UymRMHehySLAPvvsM91007HTQfzk3w033HDTTTfl+5prrklIZB/GP35ixkv2Gvjoo4+OOeaYpZZaKlyoIagJfNNNN6Xz/eCDDziJ0M4UJnYlYB+BiE5pjzvuOM5g9rv77rv5QvoR5bXXXuPnLbfcUhcTA/dlAnku577Mp4/UHWdI4nnvI1W2mhLo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)![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA0gAAAGOCAIAAAAiq7QMAAAAAXNSR0IArs4c6QAAkTRJREFUeF7tnQf41MT6tv+goFIsyBGxIB4PiiKKiij2BioeFQt2BT2KFXtvYG8oxd7Bhl0s2BWwo6BwwAIWQMGCiCKIoqjfLS/fnJjN7maT7G5298l1wZVfdmYyc8/MO8+8M0nq/Prrr/+38OCkfv36dl7Q8csvvxB+ySWXLCiWC6z7huQmziFBqT0XBErtqiBcslchcaldhQQle1UQKLWrMLjqhgmkMCIgAiIgAiIgAiIgAuknIGGX/jpSDkVABERABERABEQgFIE6thTbs2fPQYMGhYqhQOkjsPbaa6cvU+nKUd26ycxhIm85SBcO5abcBLbccstEsvDzzz8nkg6J/P7774kk1ahRo0TSmTdvXiLpKJFSEmjQoEFSt9tkk00SSSraHrPMW9epUyeR/KyyyiqJpEMiyy+/PKlZAX/77bf/JYuw49hoo42SupPSEQEREAEREAEREAERKAGB5s2b9+3b17ScHYs8dh07dhwzZkwJclDGW6BtE7n7CiuskEg6SiQMge233z5MsLxh3ENCeUPmDvDNN9/ETMFFb9asWSJJJZilRPKTYCKffPJJIqkl6PuZPHlyIllSInkJLLPMMnnDhAyQVAP4m1Mk5L2DgiXl+yHtDTbYIEZG/hc1KX/tuHHjEsmPEimIwPnnn3/uuee6KIuE3dZbb/3mm29y9c8//ywoOQUWAREQAREQAREQAREoMYENN9zwvffe46bXXXcdG+rc3RdtPGrZsmWJM6TbiYAIiIAIiIAIiIAIRCPQv39/izhp0iRvCouEXYI7cKPlT7FEQAREQAREQAREQARiElgk7HI/68f6rJZoY4JWdBEQAREQAREQARFInMCsWbMCPHZNmzYNvNPnn39+8cUXr7XWWuzQvO2223yRfVHYpXf22WcXmmMkY69evT766KMwEc855xy2nO+4444//vhjjvB33HHHDjvskDu3YW5XaBjueNlll5HJjz/++IMPPhgyZEihKdx5552PP/54yFgjRow4+OCDV1999a5duw4ePDg3k6uvvvq5554LmbI32M033/zYY4+Fifj111/vt99+c+fOzRaYWj799NMHDBgAqKeeeuqdd97Jm+z777/frl27Jk2aNG7cmB3HnHB06NBh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MCIgAiIgAiIgAiIgAkUlYKque/fuvXv3ZkGV47333rPd//YnHzHnJ15nS7AffvjBm5lFHrvTTz+9f//+/KCl2KJWlRIXAREQAREQAREQgdwE7EPGPkmG2uMdZxwINluN5bV2fGps22239e5u1Hvs1LpEQAREQAREQAREIO0EunbtyuOSfCaekxx5lbBLe0UqfyIgAiIgAiIgAjVOoEePHuPGjTMII0eO5NEKTniQgv8nT57shSNhV+NNRcUXAREQAREQARFINQFeaIKjzpvFQYMG8actyPoOCbtU16UyJwIiIAIiIAIiUOMEMj8Ry5tQsjGRsKvx1qLii4AIiIAIiIAIpJoAnrmt/35wxfcwrCuAhF2q61KZEwEREAEREAERqE0CtpGOA/9c5hG4Dktgve6kNluLSi0CIiACIiACIpBSAva6k/XXX9+n3njjCQ/G+jJNmBkzZriLEnYprVRlSwREQAREQAREoDYJ8Gq6HLvoMpn8+uuv7qKWYmuzzajUIiACIiACIiACqSbQr18/+86EO9z3J+wrFIEflZCwS3WlKnMiIAIiIAIiIAK1SYDX1NmnJtxhL67LfUjY5SOk30VABERABERABESgQghI2FVIRSmbIiACIiACIiACIpCPQN1fFh75gul3ERABERABERABERCBNBIwLWeHPHZprCHlSQREQAREQAREQAQiEKi75MIjQkxFEQEREAEREAEREAERKDsB03J2LPLYrbzyymXPljIgAiIgAiIgAiIgAiIQh4CWYuPQU1wREAEREAEREAERSBEBCbsUVYayIgIiIAIiIAIiIAJxCEjYxaGnuCIgAiIgAiIgAiKQIgISdimqDGVFBERABERABERABOIQkLCLQ09xRUAEREAEREAERCBFBCTsUlQZyooIiIAIiIAIiIAIxCEgYReHnuKKgAiIgAiIgAiIQIoISNilqDKUFREQAREQAREQARGIQ0DCLg49xRUBERABERABERCBFBGo8+uvv5KdAQMGnHbaaZz8+eefKcqdsiICIlAzBEaOHDlixIjcxe3Ro8dqq61WM0gquKCqzQquPGU9BQS23XZb7OHw4cO32Wab3NmpU6cOAUzL2SFhl4IKVBZSRsCmN9ZbdJSMwAUXXNC/f/927dpluyNmjmPrrbcuWZYCb6TmEYZ/OmtTdRem7hQmDdOSOMJOS7FqwyLwPwKff/75xRdfvNZaa22wwQa33XbbrFmz7LdzzjmnWbNmO+64448//uhCjx07drvttvv2228DCTJ/uueee3bdddfVV1/9iCOOePrppxcsWJAI6x9++KFLly7PPfecL7VbbrnlrLPOCn+LP/7448gjj/zggw/CRyl2SFQdM9RsR9euXadMmVLsPORIv1zNg7bUvXv3zz77rNCyx6nim2+++bHHHiv0jt7wqapN6u7888//5z//uc466/Ts2fPZZ58FTpzS+eLSu9Gym2+++UorrbTpppviWr7vvvt++umnBG9RjKRQur169froo4/CJz5hwoQzzjiDysUK3XXXXfPnzw8f1xfy6quvzrRj0VKjNq9aeISPTqkPOuggr6PLxWUCySTTZpKBR58+fcpri3IXU8IufDNQyConQD/fYostHn744VNOOeWAAw648MILGU2/++47it25c+cZM2bwa6NGjRyFe++9Fwny1FNPBXJBF5IOyq93795LLbXULrvsgjVMZCz5+eefn3nmmf333x8L62794osvotJeeeWV8JWES3KvvfZaeeWVw0cJE3LMmDGXXnppmJCFhkHRFholwfBlbB6zZ89mBP3kk09CFoeW+eSTTxLYW8Vh6sVFJO7GG2+cw3saMic5gpWyNr/88ss999wTNwwzn/POO2+55Zbbeeedb7jhhvilcCl89dVXDPabbbbZZZddduihhzIPPO644zp16kTdJXiXxJOaN2/edddd9+GHH4ZMmXbVtm1b5rSHHXbY+uuvj4U888wzf/vtt5DRfcGwn++++260uMTCnDLltswzcz799NNbt24dPjWUGQ1+zpw5gVFSNS0JX6hFIZGrHE7not91iEANEkAtYZSRX3jprPh0+3XXXXefffbh3KzzE0884cgg+BB5HB07dqQHZRJDBV555ZXu+rBhw0iBsTk+W+dH5NbITRLEG7HqqquS/vbbb+/Sx4UQ/14RUsDTQ2a8EUPmhHGR3SQ57sivzJ4jZCl+lPI2D6txhq6QBWFawoDnC5xZL5mpBUYMeVNfsFTVJuKDxuO6NoJg8ODBdN4vvvgiWukyY9EHqaNXX33V/TRx4kSu0PGTukXi6WC4zKfIbDZM4pQITcyaxi+//GLhzd82evRoF/33338Pk5SFYWLJ/Dl8eF9Ir1meNGkSDuaCkrLMs+SSGStM6x00aFBBtys0sG2tQ/vmjWhizrScHfLYFSyFFaEqCaAY3njjDaQYlssKyCZ97B3Lr4HlZfY/d+7cW2+99c0338SuZYbZbbfdcAlgawjGr+wM69u37worrGATTWJh0TCRb7/9Nv2Wiw899NAxxxxz0kkntW/fvl+/fu+88w4LRh06dBg4cCC20pt+vXr1+BOv2Pfff8+IhebADLEAdPzxx9et+1ePxlgzri+++OIkxZSU9M8++2xz4XBglJlnk2eSZcGIGTOeP7OwSNsTTzxx3Lhx5557Lrc+9dRTnYj8+OOPr7nmGtJhDcsWXwiGDrj//vvxSm655ZbmLOQimWG8RBCTvo2gLEZzXHTRRbgHKrTxlKx5QOzAAw+kKRoo1oPw1S222GKc0yrwIuy3337vvfeew4huwPlExV1//fXmA2MFkIPn4azlWBX76uW11147+OCDreGhSP7973/TlrwRuU7rvfvuu2nAuJzd7WgDjGf8yQo+TYU1xyuuuMK7PyGF9csc7PLLL8d97ro2jkz2SJBVlMqnn376n//854477mCh38c2s83/97//pWHTC9Zcc80bb7zRW1jreobUDmvtyy67LP8Hdnm6Ep0Fs4BxOOGEE7755hsXNxMvs6Nrr712ww033H333R955BHb1xF4keuZOffVy+TJk9kfUr9+/R122IGfzMIEZtIbERuCSwyzsMQSS9h1ljLYIbDeeutZQwIObZXm9NZbb3Elr2EhHcpCIjRgErcFDVoykxBLn3539NFHZysp1o+fsGYYH0wriySUC8862XB+uJdeeumoo44iGM2AWmbZhHZu6zDWrSKvorRs2dJHNT1/Stilpy6Uk3ISQGmx9mSefMzi7bffftNNNzGla9WqFVfsQQpntbEF2AiWPrt164aTDNuUmXVUGuMEC0Ds6UGETZ06laGlcePGJMIIjSFjkBg1atQmm2zC3jguYo8YKlgzYlw/+eST0VUYejyIWHxEnjd9G0IYWjBkZIM88D9prrLKKmakOOcn8s8YwCYSVmkbNGjACpGtmGDp0AqMNyg8VBfmeNq0aY8++ijDDIM9v6IeON9jjz1Y8H3wwQeJwqyR2z3++OPTp09HRqA+GbSIOGTIEIYHCICOG5EOapg9v2BkpQa7+fzzzyMsUKgMBtwLqVHOOo5x75I1D6YBbuAhv++//z7txDLOMIkEWXrppXfa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1B0h4Y+xdUaYWSizaOZFLv+IP3oTwJlOc1Nojx8/ni5ARF8Z+TPvDtES2KI4e+wWfVKMEciUO0WKqBAVTQSqiAAdweuRsp7PlQjfGfMl5YWU46d0sgyf4fAhXUnRlL6vIrKfj51/GH0OxATuljR8UszsZAmaR8w2EFgFYS5GqLvMrKazNm3joDe3aAgUAEIW92cg8Dg0MuN6r/ACIFbS8cDFrOhs0fPmHLdO4EasvBEzu0DMIsQ0kmEybDk0hZPXjDO1RhTZ7pHMAwWMXSq2LYrzSTEJu5gNUtFFQASSIYC5zLY8h6qzze9MzXlzRzL3UyrFJFAptYmLjsfV8cDZKnYpD7ZIsoeM93GU8qa6VxgCaZiWSNiFqSmFEQEREAEREAEREIE8BNIwLZGwUzMVAREQAREQAREQgSohEEfY6anYKmkEKoYIiIAIiIAIiIAISNipDYiACIiACIiACIhAlRCQsKuSilQxREAEREAEREAEREDCTm1ABERABERABERABKqEgIRdlVSkiiECIiACIiACIiACEnZqAyIgAiIgAiIgAiJQJQQk7KqkIlUMERABERABERABEZCwUxsQAREQAREQAREQgSohsEjYlf5rKlXCT8UQAREQAREQAREQgdQQkMcuNVWhjIiACIiACIiACIhAPAISdvH4KbYIiIAIiIAIiIAIpIZA3V8WHqnJjzIiAiIgAiIgAiIgAiJQAAHTcnbIY1cAOAUVAREQAREQAREQgTQTqMtjE3pyIs01pLyJgAiIgAiIgAiIQA4CpuXskMdOTUUEREAEREAEREAEqoSAhF2VVKSKIQIiIAIiIAIiIAISdmoDIiACIiACIiACIlAlBCTsqqQiVQwREAEREAEREAERkLBTGxABERABERABERCBKiEgYVclFaliiIAIiIAIiIAIiICEndqACIiACIiACIiACFQJAQm7KqlIFUMEREAEREAEREAEJOzUBkRABERABERABESgSggUXdh99tln++yzz48//uiAzZ07d7/99vv000/jIPz6669JhKTiJKK4IiACIiACIiACIlBNBIou7OrUqfPQQw+9+eabjtrIkSMfeOCBxRZbLA7Hxo0bd+/evUGDBnESyYw7ZsyYSy+9NNk0lZoIiIAIiIAIiIAIlIZA0YVdy5Ytd9ttt2HDhll5/vzzz7vvvvvwww/nepwSNmzYcOedd65bN+H8I+xuuukmb8Z+//33OPlUXBEQAREQAREQAREoGYFFwmjatGlFuiUeu27dut15553fffcdt2BlFncdVzj/+OOPr7nmmrPPPvvZZ5+dP38+V+6///4LLriAi+3atdt7772nTp1qufr1119JYcsttzzwwAPHjRvHla+++qpr166zZs3CHXjMMcecdNJJ7du379ev3zvvvNOzZ88OHToMHDjQabKQNyLlPn36fPHFF6wdE/enn34655xzFl98cVK+9957kaTcd8GCBddee+2GG264++67P/LII/xZJG5KVgREQAREQAREQAQKJZCwxyvw9ttuuy2b4V577TV+femll5o3b96xY8fhw4evueaajz/++PTp0/G9oczmzZs3YcIEpNXtt99+xBFHIK2OPfZYU06otMMOO6xz58646EgNwffll18SF7H40Ucf3XjjjfyJ5jv55JORdN98880uu+xywgknIPKIG/5Gq622Gom3bt2ae7FSjEy87bbbcOCh4Q466KAXX3yR1LjpDTfccNxxx2200UY9evTg1oUSV3gREAEREAEREAERKBYBnGEciBW7AX6pYhx40fbff39utMkmm1x44YU///zzOuusw4LsL7/88scff4wdO3aFFVYYNGgQHjI0H9448vDGG2+QnylTppg3EbXHRcI/88wzRDfR9sknn1x++eVoLLxr/LrVVlsdeuihluZmm23Wt2/fgm5ECldccUWnTp04Mf/iY489ZjSQm2T4t99+Q2JyO1aWP//887fffnvUqFHFwKU0RUAEREAEREAEapbANttsY56pvARMvJmWs6MO/7iEa4oFTRN2eSXkeeedd/HFF+cO5ksHdxeC6Y477sAZNnr06Pr166+33nq+FHgYgo13H3zwwYMPPshPkyZNWmuttd599110Hh64mTNnLr/88lz/4Ycf2GD33nvvoRF5tPbRRx99+umnX375ZX5iCbVt27Zkj/O99tqL9VyWa8PfaIMNNkAm8mwH2vHDDz9EyeFBbNOmDak9//zzO+64I3nAZchSMm481m1xNF511VUWwA7WnfPSK2UA/JelvF1F3CtMCw9TECYPYYIpjAiwhyQ+hHr16sVPJJFNyY0aNYqfE+97EuKnphQSJ5DIg4kbb7xx/IwtueSS8RNZYokl4idCCnig4qez3HLLNWnSJO/zo6wfjhgxAmFnCi/HYcLDtNyiI4LHDpdV3rL5NCZLsauuuiqxcKTh92LTG+eslj788MNDhgxhBxvH+++/zwY71j0t7vjx4wnD/6+++ionEydOtOsotltuucUes508eTIb8nDU2U9s3evdu7edo7ouu+yygm5ELBxylhq797Bf/Mk5GT7++OMRl4zlCFOkJDsC0Z2cs0TrLWleLAogAiIgAiIgAiJQ4wQ233xzdqbl8MaV2mPHwwQ8PZq7VjL9ImxZYw8cz0CwNY1fzzrrLBQSV9Zee+3vv/8eiXbkkUei0ljcfPLJJ0mck0033ZSHLVZeeeUuXbrgqCMAApEor7zyCs80oBFZqOXhCeexQ2bh8zNv4h577MEjDueee274G62++uo8xoE6vPLKKw844IDrr78each6MQu+Tz311Ouvv84dcQfiHSQnM2bMwG+HtuPhD4dilVVW4ZwM13iTLVLxd9111/gp4y2OnwgpsJUzfjrNmjWLn0giOYmfjaRSwGcfP6mkHEK2IURH4gRYWomf5uzZs+MnQgrsq4mfzjLLLBM/kT333DN+IoyV8RNhG1L8RJRCbgJDhw7Fk5UtTCyPHVKJo6A9dtzPspJ36dcbgOcbKAODkF3EDYaw4yEJfJusgaKl2A9HY7rkkkssAHKKhVTyxjlroMi1Vq1aId1YJ+UKko7U6NhEcV66AQMGDB482KLzWAPry4XeiCc2iLj++uuzh499e0g3boqPEFVnybL3jpzw/AcOvCeeeIL9fAVBUGAREAEREAEREIGaJXDiiSeagmJbVw4IhXrsTMvZEWWPXa9eva677joTdvElOYmUZmta+BuFDxm/+EpBBERABERABESgRgiwDrnGGmtQWPaenX/++cXw2EV53QnLoAlWQGlUHRkOf6PwIRPkoKREQAREQAREQAREICaBKMIu5i0VXQREQAREQAREQAREoBgEJOyKQVVpioAIiIAIiIAIiEAZCEjYlQG6bikCIiACIiACIiACxSAgYVcMqkpTBERABERABERABMpAQMKuDNB1SxEQAREQAREQAREoBgEJu2JQVZoiIAIiIAIiIAIiUAYCEnZlgK5bioAIiIAIiIAIiEAxCEQRdvpkVjFqQmmKgAiIgAiIgAjUCIFvv/22SCWNIuyKlBUlKwIiIAIiIAIiIAIiEIeAhF0ceoorAiIgAiIgAiIgAikiIGGXospQVkRABERABERABEQgDgEJuzj0FFcERCB5An/++ecff/zx+++/8z/nyd9AKYqACIhAIQQqyyhVobD78MMP27dvv/baazdr1mzrrbe+5ZZbvvjii0JqsFLDfvbZZ/vss8+PP/7oCjB37tz99tvv008/zSzSueee+9JLL8Us6ujRo88777wwiZxzzjlUx4477uiy98svvwwaNIgMr7nmmqeeeupHH31k6Zx44ol9+/ZlRPcm++abb+6+++4Uh4sjRow4+OCDV1999a5duw4ePNhbXm+U77777qqrrtp8883btm171llnjRkzxn599NFHW7Ro0bhx4zp16vA/uWrSpAkJxhEQIp8g+eOPP75u3bqLLbbY4osvzv+cDxgwwNKfMGHCGWec0a5duy5dutx1113z58/n4owZM4488sg99tiDiqZJcH327Nlh2mQpw8goyShBQEbJmkHFDQeVZ5R+XXjccMMNRpzhLe/BeBk+cN7UEg8wbNgwsoc4uPXWWy+55JJ11123efPm6IYcN7rnnnueeOKJxHNS4gSRFxT82Wefdfd96qmnuDJ58uTMnGy00UbXXnttzBzecccdjRo1CpMIaoycXHjhhbhhCM/Qi1AjLuP0ddddt+2221JHaC9+2mKLLQh5//33u2SnTJnSqlUrLk6bNu3111/n5PTTT6fK0KZcJy7m0peHBQsWHHDAAZtsssntt99O20Y+EmvIkCEEmzhxIlqf6/vuu2/r1q1vu+02zl988cUwpcgWRuQdmfjkqdNDDjmE+r333nv5H+0+duxY0qeHUomdO3dG55155pmcMwfAdr322ms2VDBP6N+///rrr0/NMm2IU6GJx5VRklGK3zUKapYySqk1Ss7Vctxxx+Wo02222QbLNnz48Lz1bnrMtJwdi/6oJmH3zDPP2NzIcODmOeigg2A0Z86cbIAQAQwMefGlPABert12261Xr16WT/5khDv88MMDs43oYYB0P5neCn8QHjvFUApqF5cr2VIwJ4pTz+g5xu8PPvjAwvMrddSjRw/O99prL0Ki+XAH8icj9J577mkN96uvvrriiiu23357W6HjQLNy/fHHH/fdd/r06Vx3co0coimRcd5iIvrBFb7IOUKKvIMTnzzK/uqrr/bRRo4vt9xyF198sVNszz33HFVMI6GWrW1YlEmTJvHnk08+mUjNJpWIjJKM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0c61Kt845xvhfGObb0grdDCLP3RlG5+KwSrMEJjJk1iSDj50TK2+/PLLQltLGP4Kk5cA70U3R91+++03cODAvOFzByhSR7N+JKMUs3Y0n/EBzDGfkVGK39gip5BplIok7LwzhLR47NTyvO0m9/gkVpH7WPyI0aSDvU6IY+zYsYF5CHzVZOCLxb0puGTjlyt+Ct5VZr7QlZmg1+me+VHBMBmYPn26C+bKbl8Ps4OL8GHrCZ8Oy/xEWJhbeMOoo8koFdpmyhJeRikb9nQapQjCLnCSiZnl262UPb1Lsb6KyTYQ+sY/38jnxrwSDHiuxfjGMDd6hRm63EDlG6UijE+SDjShipMOZRkGdNNoBGSUChXNMkoyStH6WnXHSkrYQckWKCpG2FV3vap0IiACIiACIiACNUigBMIuyutO9ILcGmyLKrIIiIAIiIAIiEBSBBJ8BMeXpSjCLqlSKR0REAEREAEREAEREIEECUjYJQhTSYmACIiACIiACIhAOQlI2JWTvu4tAiIgAiIgAiIgAgkSkLBLEKaSEgEREAEREAEREIFyEpCwKyd93VsEREAEREAEREAEchDo0aNHQXwk7ArCpcAiIAIiIAIiIAIiUDoCfDh+6NChXbt2tRfo8j/ngwYNypaDRcJuwoQJhOjYsWPpcqo7iYAIiIAIiIAIiIAI5COw++67P/bYY99//z0vJeZ/zrt3755H2OVLU7+LgAiIgAiIgAiIgAjEJdChQweSmD17dtyEssTXUmyRwCpZERABERABERABESg1AQm7UhPX/URABERABERABESgSAQk7IoEVsmKgAiIgAiIgAiIQKkJSNiVmrjuJwIiIAIiIAIiIAJFIiBhVySwSlYEREAEREAEREAESk1Awq7UxHU/ERABERABERABESgSgbq/LDyKlLqSFQEREAEREAEREAERKCoB03J2yGNXVNRKXAREQAREQAREQAT+R6Bu3b+kVxHfY7fkwkPIRUAEREAEREAEREAEKpGAaTk75LGrxBpUnkVABERABERABEQggICEnZqFCIiACIiACIiACFQJAQm7KqlIFUMEREAEREAEREAEJOzUBkRABERABERABESgSghI2FVJRaoYIiACIiACIiACIiBhpzYgAiIgAiIgAiIgAlVCYJGwK977VKqEk4ohAiIgAiIgAiIgArEJtG3bNnYauRKQx66oeJW4CIiACIiACIiACJSOgIRd6VjrTiIgAiIgAiIgAiJQVAISdkXFq8RFQAREQAREQAREoHQEJOxKx1p3EgEREAEREAEREIGiEpCwKypeJS4CIiACIiACIiACpSMgYVc61rqTCIiACIiACIiACBSVgIRdUfEqcREQAREQAREQAREoHYEowq5Dhw5kcM6cOaXLpu4kAiIgAiIgAiIgApVPYMGCBRRi0qRJRSpKnV9//ZWkN9tss9GjR3fu3Pm5557Le6fWrVtPnDixefPmPXv2zBu4NAGWXXbZ+Ddq1apV/ESqL4WVV145fqFatGgRPxGlIAIlJjB16tQS37Got9NsvKh4U5L43LlzU5ITZSOQwLx587p162Y//fnnn9kobbvttiNGjBg+fPg222yTm2SdOnUIYFrOjijCzlLRIQKVSKBx48aJZLtTp07x01lxxRXjJ5JICk2bNk0knfiJzJw5M34iSaUwatSo+EklIqeKN7mPX0ClAIEmTZqIgwiEJzBr1qwuXboMGzasGMLuL5XH0b59e1LHY4d+zHugH9dcc83wBVBIERABERABERABERCBFVZY4R8Lj169euWQW+aow2OXV5IZUtNydtQxty1JhF+KTbZifvjhh/gJjh07Nn4iSaWA+zSppGKmM3LkyJgpJBU9kQpKpKkkVSKlIwK1SSCRfS/t2rVLD71ENuG0adMmPSWqppxMnz49fnGSGjsaNmyYSGYYEKdMmTJkyJCddtopW4KFLsV6l+CjLMXGL5hSEAEREAEREAEREAERCCRQqLDz7rGL8lSsqkEEREAEREAEREAERCCFBCTsUlgpypIIiIAIiIAIiIAIRCEgYReFmuKIgAiIgAiIgAiIQAoJLBJ2vJeOzC222GIpzKKyJAIiIAIiIAIiIAIiEIaAPHZhKCmMCIiACIiACIiACFQAAQm7CqgkZVEEREAEREAEREAEwhCQsAtDSWFEQAREQAREQAREoAIISNhVQCUpiyIgAiIgAiIgAiIQhoCEXRhKCiMCIiACIiACIiACFUBAwq4CKklZFAEREAEREAEREIEwBCTswlBSGBEQAREQAREQARGoAAISdhVQScqiCIiACIiACIiACIQhIGEXhpLCiIAIiIAIiIAIiEAFEJCwq4BKUhZFQAREQAREQAREIAwBCbswlBRGBERABERABERABCqAgIRdBVSSsigCIiACIiACIiACYQhI2IWhpDAiIAIiIAIiIAIiUAEE6v6y8KiAnCqLIiACIiACIiACIiACGQRMy9khj50aiAiIgAiIgAiIgAhUCYG6Sy48qqQ0KoYIiIAIiIAIiIAI1BgB03J2LPLYzZkzBwjt27evMRQqrgiIgAiIgAiIgAhUDwEtxVZPXaokIiACIiACIiACNU5Awq7GG4CKLwIiIAIiIAIiUD0EJOyqpy5VEhEQAREQAREQgRonIGFX4w1AxRcBERABERABEageAhJ21VOXKokIiIAIiIAIiECNE5Cwq/EGoOKLgAiIgAiIgAhUDwEJu+qpS5VEBERABERABESgxglI2NV4A1DxRUAEREAEREAEqoeAhF311KVKIgIiIAIiIAIiUOMEJOxqvAGo+CIgAiIgAiIgAtVDQMKueupSJREBERABERABEahxAhJ2Nd4AVHwREAEREAEREIHqISBhVz11qZKIgAiIgAiIgAjUOAEJuxpvACq+CIiACIiACIhA9RCQsKueulRJREAEREAEREAEapyAhF2NNwAVXwREQAREQAREoHoISNhVT12qJCIgAiIgAiIgAjVOoO6vC48ap6Dii4AIiIAIiIAIiECFEjAtZ0fd+guPCi2Jsi0CIiACIiACIiACNU7AtJwdWoqt8cag4ouACIiACIiACFQPAQm76qlLlUQEREAEREAERKDGCUjY1XgDUPFFQAREQAREQASqh4CEXfXUpUoiAiIgAiIgAiJQ4wQk7Gq8Aaj4IiACIiACIiAC1UNAwq566lIlEQEREAEREAERqHECEnY13gBUfBEQAREQAREQgeohIGFXPXWpkoiACIiACIiACNQ4AQm7Gm8AKr4IiIAIiIAIiED1EJCwq566VElEQAREQAREQARqnICEXY03ABVfBERABERABESgeghI2FVPXaokIiACIiACIiACNU5Awq7GG4CKLwIiIAIiIAIiUD0EJOyqpy5VEhEQAREQAREQgRonIGFX4w1AxRcBERABERABEageAhJ21VOXKokIiIAIiIAIiECNE5Cwq/EGoOKLgAiIgAiIgAhUD4G6vyw8qqdAKokIiIAIiIAIiIAI1BIB03J2yGNXSzWvsoqACIiACIiACFQ1gbpLLjyquowqnAiIgAiIgAiIgAhULQHTcnbIY1e11ayCiYAIiIAIiIAI1BoBCbtaq3GVVwREQAREQAREoGoJSNhVbdWqYCIgAiIgAiIgArVGQMKu1mpc5RUBERABERABEahaAhJ2VVu1KpgIiIAIiIAIiECtEZCwq7UaV3lFQAREQAREQASqloCEXdVWrQomAiIgAiIgAiJQawQk7GqtxlVeERABERABERCBqiUgYVe1VauCiYAIiIAIiIAI1BoBCbtaq3GVVwREQAREQAREoGoJSNhVbdWqYCIgAiIgAiIgArVGQMKu1mpc5RUBERABERABEahaAhJ2VVu1KpgIiIAIiIAIiECtEZCwq7UaV3lFQAREQAREQASqloCEXdVWrQomAiIgAiIgAiJQawQk7GqtxlVeERABERABERCBqiUgYVe1VauCiYAIiIAIiIAI1BoBCbtaq3GVVwREQAREQAREoGoJ1P114VG15VPBREAEREAEREAERKCqCZiWs6Nu/YVHVZdXhRMBERABERABERCBqiVgWs4OLcVWbTWrYCIgAiIgAiIgArVGoI6tw5rT7rzzzrvwwgtrDYHKKwIiIAIiIAIiIALpIbDtttuOGDGie/fuLVu2zJGrH374YcCAAUi4uXPnumASdumpR+VEBERABERABERABP7PhF1IEI0aNZo1a5aEXUhcCiYCIiACIiACIiACJSUQ0mM3ZcqUwYMHS9iVtG50MxEQAREQAREQAREoiIAJu+HDh2+zzTY5IhKGkBJ2BbFVYBEQAREQAREQAREoKQGfsOvTp0/m7Xv06IHHTsKupBWjm4mACIiACIiACIhAoQR8wq5du3bjxo3zJfLnn38Geuz0upNCaSu8CIiACIiACIiACJSOAM453814YDbb7SXsSlcxupMIiIAIiIAIiIAIFEqga9eu3iirrbZa//79ucLrTjKTWiTsOnTowG9z5swp9GYKLwIiIAIiIAIiIAIiUDwCvM1u6623tvSXWWaZoUOHLrvsspyPHTuW/30fhl30Hru2bdtOnDixefPmPXv2LF7OoqVsuY9/tGrVKn4i1Z3CyiuvnFQBW7RokVRSSkcE0kNg6tSp6clMsjnRxD5ZnpWVmvf1tpWV82rN7Zlnnjl+/HjvU7E45/DbjRw5sl+/fieeeKIVnIcqLrjgAp+2+9sLiqsVkMolAo0bN04EQqdOnRJJh0RWXHHFpJJKJJ2mTZsmkk6CicycOTPB1BJJatSoUYmkk5SKmjRpUiL5USKlJNCkSZNS3k73qkQCP/7444IFC0444QTEHO4tHp6wUvAYrPdbFCbs8Fu9//77/ysmHjwOXpSy5pprVmLhlWcREAEREAEREAERqFkC7KYzLWfHIo9dvXr1kiUSuKEv2i1sCTk9R/ivfJQsz/hmS3avkDdKqtYSbEghc65gIiACcQgktXnGuSjiZCbZuEnt52nTpk2yGVNqOQhMnz49ET5JDUYNGzYMk59p06Z9+umn8+fPx3X37bffcpIj1hVXXHHSSSe5AIuEHX+j8viObJj7+cL88ssvXFlyySUjxNV9w0MT5/Cs1K7Cs1K7Cs9K7So8K7Wr8KzUrsKzUrsKw0qvOwlDSWFEQAREQAREQAREoAIISNhVQCUpiyIgAiIgAiIgAiIQhkAdlm/DhFMYERABERABERABERCBlBP4fxCpa2cjRp0jAAAAAElFTkSuQmCC)![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA0cAAAGMCAIAAACeaE6KAAAAAXNSR0IArs4c6QAAo6pJREFUeF7tnQn4FWP7x99SoUSWKFJ5KZEohWRJkkJUKEIqKmuyJktUJFurXZYisrXY96UslbVkK3kVKpESIYT/53W/nuY/Z5tzzpxz5pzfd66rrvnNedbP88zMd+77Wcr99ttv/4o5uFipUqXY6ymvrFmzhjAbbLBBypBxAyjfgNzEOSAoC6Z+FRCX+lVAUOpXaYFSv0oLl55XAXGpX8UFVT4gPgUTAREQAREQAREQARGIMoFyzlbXp0+fcePGRbmsKlsSAjvttJP4JCdQvnxo3zAZW6PVRiLgCOy3336h0Pjll19CSYdE/vjjj1CS2mijjUJJ5+effw4lHSWSTwKVK1cOK7u99torlKQy8z3GZl2uXLlQykMitWrVCiWpzTffnKSsgr///vt/0/zhn6Np06ah5KFEREAEREAEREAEREAE8kOgZs2a119/vam5cvyzXFu1avXOO+/kpwSFygVVG0rWW265ZSjpKJEgBFq3bh0kWMowcYeQpowVN8CyZcsyi+iLtdVWW4WSTljlCaUw4SayYMGCUBIM0erz+eefh1IkJZKSwCabbJIyTMAAYXWA/5lDAuaaOFiIVp8mTZpkXZz/JhCWpXbOnDmhlEeJpEXgsssuO//884myzgPbsmXLGTNmcOmvv/5KKy0FFgEREAEREAEREAERyDOB3Xff/b333iPTG2+8kXF0nKwbaVS3bt08l0bZiYAIiIAIiIAIiIAIZEZg1KhRFnH+/Pl2sk7VhTjkNrPCKZYIiIAIiIAIiIAIiEDGBNapuuTT+nDLyjObMWVFFAEREAEREAEREIEcEVixYoXfVrfFFlvEzeyLL7648sord9xxR4Zk3nHHHS5m3MCMzLv44ovTLTR6sW/fvp988kmQiJdccgljzNu2bevmecSNdddddx100EHJSxsku3TDkOOwYcMo5KeffvrRRx9NnDgx3RTuvvvuRx99NGCsV155pVu3btttt13Hjh3Hjx+fnMnw4cOfffbZgCl7g912221TpkwJEvHrr78+9thjV69enSgwrdy/f//Ro0cD6oknnnjrrbdSJvvhhx82btx4s802q1q1KkOMOeHYc889v/nmGxf3zz//POWUUwBOdz3hhBNsdcrMDpKdOnUq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t0U1gdmf3RJZp+rYGktkRUAEREAEREAEREAECk5g3LhxLGLCMhccjRs3Ruqx8zsXOWdPKX7i/9hCamWTgjecCiACIiACIiACIiACyQh07NiRMfRsE8pJknDl3RxY4RQBERABERABERABEYgaAcxyc+bMsVJNmzZt9uzZnGC085bT5Fz5Sv8cUauDyiMCIiACIiACIiACZZwA81sx0Xkh4Iflz2rVqnkvmpqTB7aM9xZVXwREQAREQAREILoEYrcIe+WVVxIVV6ouug2pkomACIiACIiACJRxAtjkWv7/gyvff/99XCxSdWW8t6j6IiACIiACIiACkSNgg+c4sMzFHj73qyu9VF3kGlIFEgEREAEREAERKOMEmCFhy5q4g5VNynmOVq1axSKSqivj3UbVFwEREAEREAERiBABZBylYdIr0129ByubpCylVF1KRAogAiIgAiIgAiIgAnklMHLkSNtJwh1uhwnbZyLu/q5SdXltJGUmAiIgAiIgAiIgAikJsBydzwPrW6AubgpSdSnBKoAIiIAIiIAIiIAIFAEBqboiaCQVUQREQAREQAREQARSEpCqS4lIAURABERABERABESgCAhI1RVBI6mIIiACIiACIiACIpCSgFRdSkQKIAIiIAIiIAIiIAJFQECqrggaSUUUAREQAREQAREQgZQE1qm6bbbZJmVoBRABERABERABERABEYgUgW+//dbKI1tdpNpFhREBERABERABERCBDAlI1WUITtFEQAREQAREQAREIFIEpOoi1RwqjAiIgAiIgAiIgAhkSKD8mn+ODBNQNBEQAREQAREQAREQgYISMDUnW11BG0GZi4AIiIAIiIAIiEBIBMpv8M8RUoJKRgREQAREQAREQAREIK8ETM3JVpdX6MpMBERABERABERABHJEQKouR2CVrAiIgAiIgAiIgAjklYBUXV5xKzMREAEREAEREAERyBEBqbocgVWyIiACIiACIiACIpBXAlJ1ecWtzERABERABERABEQgRwSk6nIEVsmKgAiIgAiIgAiIQF4JSNXlFbcyEwEREAEREAEREIEcEZCqyxFYJSsCIiACIiACIiACeSUgVZdX3MpMBERABERABERABHJEQKouR2CVrAiIgAiIgAiIgAjklcA6VVenTp285qzMREAEREAEREAEREAEsiawbNkyS0O2uqxZKgEREAEREAEREAERiAABqboINIKKIAIiIAIiIAIiIAJZE5CqyxqhEhABERABERABERCBCBCQqotAI6gIIiACIiACIiACIpA1Aam6rBEqAREQAREQAREQARGIAAGpugg0googAiIgAiIgAiIgAlkTkKrLGqESEAEREAEREAEREIEIECj/2z9HBAqjIoiACIiACIiACIiACKRNwNRc+Ur/HGknoAgiIAIiIAIiIAIiIAIRIGBqTh7YCDSFiiACIiACIiACIiACWROQqssaoRIQAREQAREQAREQgQgQkKqLQCOoCCIgAiIgAiIgAiKQNQGpuqwRKgEREAEREAEREAERiAABqboINIKKIAIiIAIiIAIiIAJZE5CqyxqhEhABERABERABERCBCBCQqotAI6gIIiACIiACIiACIpA1Aam6rBEWKIE//vijQDkrWxEQAREQAREQgSgSWKfqNthgg4IU8JNPPqlfv37t2rUnTZqUpACLFy/u0KHDvffem+dCvvHGG23btj311FO//fbb++677/HHH8+4ACtXruzUqVOjRo122GGHrbfeequtttpss82eeeYZS/DPP/987rnnTjnlFH7t1q3biy++GDejL774om/fvtttt12FChVuuOGG33///ZdffiFZEqxatSppNmzY8JZbbnFx//rrrwkTJixatMhdWbFixUEHHfT2229nXBFFFAEREAEREAERiA4B95YvvK0OOXLggQf++uuvjRs3TgJo+PDhM2fORLjkEyKSqEePHm3atEFC7bbbbhdccMHOO++ccQE++OCDqVOnnnjiiaQzePDgq666ikohwkzSDRkyBPnIdh/nnXde+fLlEV733HOPL69vvvnmsMMOW7p06fnnn9+/f/+zzjrrpZdeQo6jdy+88EISHDBgALIPUC7if/7zHzTi559/7q68/PLLSMabb74544ooogiIgAiIgAiIQBQJuH1gH3vsMSsfUibPx2233Va3bt0kmaL5tt1224cfftiFWbt2bX4KiYlu7ty548aNu+yyyz7++ONsMjXzG5osNpEpU6bwE5oPecev1O66667jyurVq72Bx48f36pVq59++skuIhAvueQSbwAUG7FIzV00ti4d0j/qqKM22mgjgiH4sqmO4oqACIiACIiACIRO4IADDuAdzQs9ZcpOVu65557/2wc2CkqzXLlybpTY2Weffdddd2HN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gAiIgAiUIAH2ms91rXKi6nJdaKUvAiIgAiIgAiIgAiLgIyBVpy4hAiIgAiIgAiIgAqVAQKquFFpRdRABERABERABERABqTr1AREQAREQAREQAREoBQJSdaXQiqqDCIiACIiACIiACJT77bffjMIdd9xx+umnc/LXX39lyeX666+/4IILQkkqy5IEjP7nn3+W+/sIGF7Bckrglb+P5Fn06NGjbt26OS2GEhcBERABERCB7An85z//2X777UnnzDPPvOGGG1Im2KpVK16CL7/88gEHHJA8sNMtVatW/e677whceFvdypUrO3Xq1KhRox122GHrrbfeaqutNttss2eeecZqgt567rnnTjnlFH7t1q3biy++GFvD6dOnn3DCCT/88IP7adasWbBDnv7888933333wQcf/Pzzz8dGJPGJEyeCb5NNNmnXrt0nn3xCmAULFjRr1oxiwIjy7Lnnnq+++qqL+9NPP918880ka1dmzpzZoUMHsobm4YcfXrt2bSt/48aNv/zyy5Qtl32As88+Gw1NRbxJzZgxg1KtXr06ePq33XbblClTgofPaUh686hRo0zbxT0GDx68cOHCnJZBiYuACIiACIhA0REoj63OjkIV/YMPPpg6deqJJ56IeY+39VVXXTV8+PCGDRuapBsyZEjbtm0p3nnnnVe+fPmDDjronnvu8RX1rbfeuu+++0aOHOmsjJ999tlNN930xx9/3H777ddeey3r5yHs3njjDV9Efu3Tpw/pX3755SSOEPz999+rV69OYS655BJK0r17dxL/9NNPXcQXXnjhjDPOMAWJbqPAjz32GDIcLfjEE09g7Bw2bBgya8CAAaSTB6TvvPMO3B5++GGX16JFiyg2pVq1alXwAuyxxx4o0eDhg4Sk+cDothwOEsWFoTBJVB2aVaouLZ4KLAIiIAIiUNoE/qflnKrDBGUVRhtleVx33XXBkzLz29KlS2MzNesRmg99wK9r1661lLFCeQNfc801lh3mSruOyONPwrdo0QLFhiFto402wmjnjfXjjz9uu+22jz76qF1EvREFOegNM2LECC7Onz/fXTzuuONOPfVU/kQ2uf7x5ptvovb4E0WVGToEaGYRjzrqKPKldm+//TYprFmz5sgjj7SCOaRwyCzxLGOZrASUS4dqWlMmP2iyli1bJgnDr77WTJWkfhcBERABERCBwhBA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VXjwwQe7dOlS1HVR4UVABIqOQD5VXeFnS3z88ceYQ3baaSfsDS1btrz99tu//PLLUNrs0ksvffHFF4MnxUCle++9lwFPI0aMYDvwc889d8GCBcGjhxgSc2nfvn3HjRuXQZqffPLJCSec8Ntvv6UVF/NM27ZtTz311G+//fa+++57/PHH04pewoGz3/+ghOEUS9W4m6yo3B3FUmaVUwREQAQyIFB4Vff5558zbqlXr15Dhw5FWNxwww177bXXvHnzMqiMLwrWSCRj8HQWLVp04YUXnnHGGc8+++wOO+xA3K233jp49BBDfvrppzfeeONll12WwahztkVClnl3ZE9ZMERkjx492C2+QoUKu+22G474nXfeOWWsMhIAJmWkpqqmCIiACIhAsRMov+afo1A1sZl0PXv2RNhdfPHFM2fObN26NUaj1atXp1ukP/74wxuF93Fa8wTr1KkzZ86cunXrdurU6ayzzpowYYJv8l265SG8r0gBU3jhhReYUYjNcvr06QGjuGDGM63BkeXKlcNWx/6YzC7s3bv3Sy+9tP3226ebb6mGz3JgXKliKdJ6YYou0pKr2CIgAiKQnICpucLb6mythN9//92Ky57caDv2REdg8SdFfPTRRy+55BJseHimucLQ6csvv9zVDW8pnsqffvqJMMg4nLlYqkzTkDKiCmF3/PHHuwHgDK+55557LPprr73Wp08fdiJnz2+ioIc4OeCAA0477bSLLrpo0qRJLheMZ2REwbD//frrr3b9gw8+OOmkk/Ads/iFlc17kO/48eO3+/u44oorcOlajt26dbPiMWy8ffv2K1eu9EUk/TvuuAOr4YknnohH2Omzs88++6677sKQhh3xvPPOI8Gvv/4a6yb/k8LatWuPPfbY9957z5ZvMDlL3Oeee44cGRx2//33O4npqzghGTi/9957Y7FjkuBNN930yy+/WKkCVhzH1lFHHeUa0Vejov4TrV/U5VfhvQQCziMRNBEQAREoUgLlWfDJjkJVwFSd16aFDOLKkiVL0BYnn3wyo8QQLmg1ZAfibMMNN0R54LclDP+jb6pVqzZy5EiU0K233soEN8Jj6+JXs9Vh80PQfPfdd1bBDz/88P333+fk4YcfZiGumjVrYiM87rjjXn/99aVLlyINkX24L3GAnnLKKaYsGSxfv359xOXixYsPOeQQRl6jqNCRRNx4442RWXiQMXSZunIHcgqRhGo8//zzkXdjxozhJ7y6KCoLQ5GefPLJb775xkd+1qxZiDMmP1KRhx56aP78+RZg8uTJ0KD8JEjiaC+MeZyYXmQgHSPBEZcY3vjTVB0VR/ZhbUKqOmkbW3ECg/SII46AFQmikgmTVsVxVSOFvYuZFao7hZ7v8uXLQ09TCRaKgM0R0yECIiACpUfgf1oONWDHddddZ5XEwJPlcfPNNwdPyiYYouFcpiaP8AMiUziZMWMGsgMLFvoJ9ygh69Wrx+IphGfeboMGDb766iuCYcOzFAYNGsSwMOxGDBSjUvZ1Ti72K+KjX79+yBecjGPHjrWL/IpimzZtGiHJnSsISlJGLHJCagg4rIYUY/bs2axuiu7BlcPSpuT19ttvkwVFJU0vt44dO2LbIwoXUW+kjN2LBCmVBTPJiErz0UY14n5FBWLhI8Dw4cMtAHVn0DcajnMkXZMmTbBougJTPM4phvFEoTJMkHQggGLGkmfFjltxU5YOEUZBxGvGFc+y80QtelqdOWqFV3mMwGeffeY86WIiAiIgAnkmwCPIrTwfJGsMMd6XcpIoTpvikTMtV3gPrFnpvMu+I3S4gp/RVAsmOnyjLByPQGEqAKoOZYZZDlsXFrUzzzzTphQg9ax6hMefyCpZZrUCB/8ja+xXkkJpYWmDMlnYxd13332LLbYw16rFQvMyvA/TF1KM1DAEcoW4uGvRQAggwj/xxBNoQXy+XMSd6l3ankqxMtauu+5qqXFi8suydiVxxXMNg0MWrcmfOHyRaChLVIVFoQDoS0yVnNeoUQN7nvlJrWrOROdqzZwPxgUyTo5ig5e4KNG4FbcJs26rAEbXPf3005gVM6i4q4hORCBSBDQ+MlLNocKIgAjkiEBUVJ2TFGg1ViRhsgJPYVyr2MMY64a+wZmIE5axbrvssguWJAxdAwYMQHIdeuihSByMUtj2TOJgGDvssMPYIAhzHckiv5o2bYpFzX5lBBie2erVq7Nsla1uijJj1i1OW9ys/GkTFDB9IZswj5mKwrz3yCOPUBLKwNG/f/93332XoW+4a5FKrMaCHREznmskVBTp4z81T6jZz3bccUdUGk5kcrR8+d+3ixHuV8xpjNjDuTx37lzqgvo0py3FdtrUBKjNabC1ZM0kSWqWIycIuG233da0JhoXCUisuBVnTRmkMC5mQiKCUdUYFKtWrZpBxXPUTZWsCIiACIiACIhASgJRUXUIpttuu41pEPvuuy9CBM8mgozpAhiosNhxBZGH4GMYHOfII8acYT9D/DEID+XH5Abcnfgumb6K75JzTFYoM5QQ+oaxdyybcv3112PkYwU7hn/xK0Y+QjIJA+8qUg9TH+PiEWeUAfMY0yAwVh1zzDEoJ9TbU089hXojd6xf6CfUHpkitoYNG4ZZi8Lzk3ffSbgzBo6RcN27d8daRkUwK6Ko9t9/f5YOYSU8THH8H6vqsP8xNLB27drWctSOMpA+51Tc7I4cmCcpGGXGJ0vxSJwBfF7lBz3SYYEY9ChgGTOHXiRA3IpDibF6FOnqq69GK1911VXI1rQqjoJkxJIrXspuV0QBnG21iMqsoiYioO3C1DdEQARKm0DhVR3mK0QS+gxJgQphUBdWMTQT3M2yhcEJQYb5DXubLR6GNEGscIXA1jycEAbLFtKHeQ8tWrTgIvYnUuCkc+fOJI7TFqse8gVrHxeRj1whX0x6RDQHLpKORVUYtYbye/XVV5GS5MXm7tdccw3GOcxvzCrAYIZmQm8hN5FKjH7Dk4vCc1LMioS5i2Tx4WJLe+CBB5h7wUVsipyTAjIRDYrvHKnn7WGYBlkwz7yoVlP+tI2VDj74YOdlJi9mvHJx8ODBJEKB0XAAoVToSzZfYhoH5xgg2XkJzde8eXMqbh7nuBVHDaNBUahvvvkmEyZ4+aVVcZzLiGw3O7iU7pkMVtgppeqXTF1s6cpatWqVTI1UEREQARGIQ6DgsyUw8OA0tFkFSY6UAYKMQPSFYYQcFrvHHnssYNzQyxBugsFTK3jFAwKPQjC+H7ht8EdHoTAqQ2YEGMZgzz6s9ZmloFgiIAIikDGBop8tka7TCrOQs04lkt4pA2Sg2RE3DH1jPFxA12HoZQg3weCpFbziGTRWoaIwxpGssfsWqgDKN0QC2a8rHmJhlJQIiEBZI5CHQSCF98AWsFHZ4pMVQFhDOLgeKmBpQ8y6zFY8A4ZMNMkglqJEk4At7qhDBERABEqVQJlWdTSqm3tbqg2cqF5ltuLpNrRtSeybqpxuIgofEQLpuhEiUmwVQwREQAQCEijrqi4gJgUrswTYaIS6syphmSVQShW31tQhAiIgAqVKQKquVFtW9RIBEVhHgGng/MFq4YIiAiIgAiVMQKquhBtXVRMBEfgfgUaNGomFCIiACJQqAVsBjUOqrlSbWPUKh4Bt3ifPXTg0C5eK7csyf/78whVBOYuACIhAzgmUsz1AOUaPHs3OCpwEXOYjSdFYEDispHIOQBmIQFICLGTNhAnWdrbdO+IebG3nrruVotPi6t2l1LecdVrphBJ40aJFQdLJqdINd/Fnpr6yFLlVKvvnWxA4CiMCIiACjgD7EXTt2pVF/lnZhA2uUpJp1aoV2xyw1yi7DCQP7FbwYCsB9lYlsFRdSrwKUKYJRGrVG9uc1w42L3HnbJqSqJHYBznRT8uXL4/7k20u5w6vegvX1sVmzfnsWytWrGDbaHZ8yWemyksEREAEpOrUB0QgKgT4ZlqyZEm4aiYqdSsz5WCPZjPRsc8euz+XmXqroiIgApEgIFUXiWZQIUQgEQF21/X+xPYkiUJiRY/707Rp0xJF8abmyyjKLeJ1Qzdu3DhRUb0ealbDzrJGixcvdin4WFWpUsX7E1QXLlw4ceLEdu3aZZmpoouACIhAWgSk6tLCpcAiIAIiIAIiIAIiEFECqLouXbq88847jH6bPHlyylJmM66uPLMl7EiZjQKIgAiIgAiIgAiIgAhEkIBpufKV/jkiWEQVSQREQAREQAREQAREICUBU3Nary4lKAUQAREQAREQAREQgSIgoJVNiqCRVMQCEhg4cOCVV14ZegFsceN0D+9aa3/++We60TMLv99++7mIFStWdOfly/+/b8KNNtrI/fTDDz9kllfcWJUrV/Ze32OPPdyfG2ywgTtff/31vcGY9+r+3HTTTVlFZb311guxVEpKBERABAISyOe4un+5cXXXXXedlY83R5ZHiEllWRJFF4EsCTRt2jTgfatgESewzz77sP5nlv1B0UVABEQgXQKfffaZvUqYLREkri0+zCrEKQO7py4pm5yTrS7ibyIVr8AEmjVrxsSl4IXw7hJBLN+fwdOxkIcffrg3CmMm3J/Lli1z51tttZU3mPenJDl+9NFH7levde2NN95It5y+8N5NV1etWuX99YsvvnB/uo0LuXLkkUd6g3mXKZkyZUqW5XHRp06d2qFDh7BSUzoiIAIiEISAbHUp5akCiECeCDDD3G7aPOWnbHJA4Oyzz7ZGZEedHCSvJEVABEQgGYF82uo0WyKIzlaYsksg+5Vyyy67yNS8b9++VpZPPvkkMoVSQURABEQgfAJSdeEzVYqlRKBChQqlVB3VRQREQAREoIQJ5ETVrV69uoSRqWplikCWA+PKFKvoV/bbb7+NfiFVQhEQgdIjYJuJV61aNddVW6fqCiXFvvnmm1NOOYXpG4yw7tix4z333OMbXp1rBPlMn80oDzzwwNy9Wr7++mv2L8+mKRkagLtKjirXK+rUqZPPHqK8ckog4DySnJZBiYuACIhA6AScXsyJrS6t4n766ae33347o5fOP/98RqaPGDECkffrr7+mlUhOA7Mw2CWXXPLxxx9nn8t9993HXOUnnngiZVKEfPzxx1MG8wWgXbt37+5b3yutRH7++ecbb7wxlMqmlW9kAy9fvjyyZVPB0iXwzDPPpBtF4UVABESgiAgUXtWtWbMGXmeeeSZypF+/fg8//DDz1J5//vkkEP/44w+U1tq1a72LsuYOOqavq666asGCBd4sMlgDdsWKFbfeeiuLtY4dO/b3339PXuCnnnpq1qxZ6VaqSpUqhxxyiG952OCJUKpy5coR3lu7DGoaPEeFFIH8EDBP+o8//pif7JSLCIiACBSEQOFVnekbt+x79erV0T0rV65EsT333HPdunXDZXn//fej5Ai2ePFi1vonDLa91q1bP/LII0aNlbdYvKB58+bXXHONrbx1wQUXXHbZZSeccAL2v8f+Po466ijO3cc6avLRRx/FCHfDDTewloylQyJ33XUXcXfYYYfzzjsPwxUXBwwYwP+IzunTp3PCgltdunShwO3bt585c6ZF/OCDD0466aSddtqJ4rnUfC06bdo0BCKSbsaMGW+//bb9+sADDwwePBgLZePGjY8++uhFixZxkfpyjB49esyYMRYMiyZhLr74YsrvDJmsN3j33Xez9P/xxx8/Z84cgi1duhQvNvKRYIMGDbr++utbtmyJVvY6nvD/Dh06lBVZub5w4UJL//PPP+/duzfLoR100EH8abQD1hR3LWxT6lQfDf0pAvkkoPGR+aStvERABApFoPCqzvQc6mTcuHHoGNYIZXuf/fffH1nTtm1bnsUssoxqYWVUFiZF5LF9Ezpviy22QGPZ8C8Ezb777sv4PDQcmol0uIi174orrqhRo8Zee+1FmhzsILTLLrugvRA9v/zyy8knn0x4BqLh69x7771t5dXJkydz/cMPP8QdjKa86aabuGgrwSJ66tevj6LiBGFEgWvVqtW1a1ekz08//dSr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V7EPJvty8KZnCPn111/vdSe5HM866ywGkjM0u0KFCvzP+f/GMP7rXx988MGFF15IfdmP8p577vn111+Jhfi75JJLjj/+eJx9Bx100HXXXRc32QxoKEr2BGjE7BNRCiIgAiIgAiKQBwKFV3Vbb701X9IopNNPP50KX3rppZyff/753g2IHAhGOF111VVJuLAp0H333eeTZbvtthtbee6888425glJx4C/tm3bIv6QaKgutBQai5+IPm7cuMGDB6O0LBfWgMF9w47g7E3EcCUG5XBy8cUXH3HEEY8//jjT8ebOnesrzzPPPHPiiSdOmDCBkvD/+PHjbeQj4VGW7Fx00kknUaTu3bsPGDDg999/Z+ARlWI2H37xY445hr2kKM9XX32Vh+ZXFikJ+MbJpQyvAFEm8O2330a5eCqbCIiACGRLIDpzYJ999lkqs3z5cuc4dx5Md+W2227bdtttk3jWLRGe3b4wxx13HHrRLtrga8ZNm3t07dq1mMe4snr16ptvvtmA3nXXXRb42muvtSsvvfTSCy+8wAmmO/vpp59+Yk9JFJ4vr3333Xf48OG+i/PmzWN5BdbIWLNmjf1kRWU1GRK09O06xUAFagZxRMZPYL61DhCR8qgYGRBwg1o6d+6cQXRFEQEREIFsCJTRcXXmNnUOLybisYTe5ptvfuqpp5pHcs6cOYMGDfryyy+7dOlitjQ8mMgvvJmYuF5//XWu2JJUcZfyoknsJ6QhHk+sbjZXlyjnnHPOggUL2A6cJa9YdgtNhjlt5syZb731Vv/+/S+77DKCERhrH78OHToUiUZqLKN1wQUXYFfzKWtm9plrlbyQjFYYDHUNGjTABulW1WIRGebF7LrrroRxJedkww03xD6EXRDV2LFjR8yHvvT1Zz4J8JmRz+yUV04JYEfPafpKXAREQAQKS6DwHlhXf1NdprSQcQxlY/wZVrRFixahujBx1alThwmJaCMkF1IMYccYtX79+iGPEFKYzTDRWfRYVcd1Sx+1xJO9TZs2Xu6ktv3225umxFSGLxj36Mknn4zvFV8qJ/xE9Jo1az7//PN4SCkDCzEwXI/xf26OpEuQRDDgkSPJsmor2pRlIx577DHEqG+h1O22244AtporFsS777771ltvZZwfrtujjjoK1Yii9S6mWti+otxFoHgJmCfdNzajeKujkouACIhAXAIRUnUm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ZiIgAiIgAiIgAiIgAiERMDUnW11IOJWMCIiACIiACIiACBSUgFRdQfErcxEQAREQAREQAREIiYBUXUgglYwIiIAIiIAIiIAIFJSAVF1B8StzERABERABERABEQiJgFRdSCCVjAiIgAiIgAiIgAgUlEBOVN2ee+5Jpdz+FQWtoDIXAREQAREQAREQgUISWLt2LdnPnz8/14Uo99tvv1kelSpV4v+BAwcOGTIky1wbNGgwb968mjVr9unTJ8ukwoperVq1LJOqV69elimUWPRtttkm+xrVrl07+0SUggjkmsCiRYtynUXe0tf3dt5Q5z+j1atX5z9T5ZiSwM8//9y5c2cL9tdff6UM36pVq1deeeXll18+4IADkgcuV66cBejUqdODDz7ISU5UncsmZdEVQASiQKBq1arZF6NNmzbZJ1KjRo3sE8k+hS222CL7RLJPYfny5dknEkoKs2bNyj6d7OVUHj70s69m2Uxhs802K5sVV62DE1ixYsWhhx765JNPpoySjar7F7Y6OywbbHUIySwP1GX9+vVTllsBREAEREAEREAERKC0CWy55ZbV/z769u0bRF+ZiQ5bXcrAjhu2OtNyObHVhds833//ffYJzp49O/tEsk8Bm2r2iWSfwrRp07JPJJQUsm+XULpHKHVRIiJQdghkP6alcePGEcEVyuiahg0bRqQ6JVOMxYsXZ1+X7F8QVapUCaUYvOwWLlw4ceLEdu3apUwwG1tdEai6lPVXABEQAREQAREQAREoDQLZqLqczIEtDayqhQiIgAiIgAiIgAhEn8CqVauskFJ10W8slVAEREAEREAEREAEUhOQqkvNSCFEQAREQAREQAREIPoEpOqi30YqoQiIgAiIgAiIgAikJiBVl5qRQoiACIiACIiACIhA9AlI1UW/jVRCERABERABERABEUhNQKouNSOFEAEREAEREAEREIHoEyjv21si+iVWCUVABERABERABERABLwETM6Vr/TPIToiIAIiIAIiIAIiIALFSMDUnDywxdh2KrMIiIAIiIAIiIAI+AlI1alPiIAIiIAIiIAIiEApEJCqK4VWVB1EQAREQAREQAREQKpOfUAEREAEREAEREAESoGAVF0ptKLqIAIiIAIiIAIiIAJSdeoDIiACIiACIiACIlAKBKTqSqEVVQcREAEREAEREAERkKpTHxABERABERABERCBUiAgVVcKrag6iIAIiIAIiIAIlFkCq1atsrpL1ZXZPqCKi4AIiIAIiIAIlBQBqbqSak5VRgREQAREQAREoMwSkKors02viouACIiACIiACESaQKdOncr9fWy33Xacjx8/Pnlxpeoi3ZwqnAiIgAiIgAiIQJklMHXqVKv7woULOe/Rowfybtq0aYmASNWV2a6iiouACIiACIiACBQZAeTdK6+8IlVXZM2m4oqACIiACIiACJRxAnXr1k2LgGx1aeFSYBEQAREQAREQARHIEwGpujyBVjYiIAIiIAIiIAIiECkC5df8c0SqWCqMCIiACIiACIiACIhALAGG1sVeNDUnD6w6jAiIgAiIgAiIgAgUDYG4qs5KX36Df46iqY0KKgIiIAIiIAIiIAIi4CFgak62OnUKERABERABERABESgFAlJ1pdCKqoMIiIAIiIAIiIAISNWpD4iACIiACIiACIhAFAnEXXD4+++/T1RWqbootqLKJAIiIAIiIAIiIAJxCcyePVuqTn1DBERABERABERABEqZgGx1pdy6qpsIiIAIiIAIiEDZISBVV3baWjUVAREQAREQAREoZQJSdaXcuqqbCIiACIiACIhA2SEgVVd22lo1FQEREAEREAERKGUCUnWl3LqqmwiIgAiIgAiIQNkhIFVXdtpaNRUBERABERABESgmAj169EiruFJ1aeFSYBEQAREQAREQARHIE4G777576tSpHTt2rFatGlnyP+fjxo1LlL1UXZ4aRtmIgAiIgAiIgAiIQLoEOnToMGXKlJUrV/7111/8z3n37t0TJVLut99+s98qVarE/wMHDhwyZEi6WSq8CIiACIiACIiACIhA9gRatWrFRmFIt7p16yZJjX3DRo8eXbVq1R9//LFp06YzZswgsFRd9vyVggiIgAiIgAiIgAiEQ8BUXcC0atasuXTpUqm6gLgUTAREQAREQAREQATyRyCgrW7hwoXjx4+XqstfwygnERABERABERABEUiLgKm6l19++YADDkgSkTCE9Kk6zZZIC7UCi4AIiIAIiIAIiED+CAyKd2Coi1uC8syWsCN/BVROIiACIiACIiACIiACAQiwssngmCN2IoVpufJMfbUjQMoKIgIiIAIiIAIiIAIikD8CsQsRx13ZxLScPLD5axjlJAIiIAIiIAIiIAJpEWDZYW/4OnXqjBo1iiusbBKbjlRdWmwVWAREQAREQAREQATyRwBna8uWLS2/TTbZBIes7TMxe/Zs/me2hLco61TdnnvuyQ+sZZe/kionERABERABERABERCBpARQcibsmDjRuHFjb9g///yTP+fPn28X161C3KhRo3nz5iH6+vTpEzW8JkuzP+rVq5d9IqWdwjbbbBNWBWvXrh1WUkpHBKJDYNGiRdEpTLgl0Vd9uDyLK7XVq1cXV4FLuLQDBgyYO3duv379bPtXJ+OY9+qdJIHCYxKF42DTXv17S5QwJlWtjBNgW5WwCLRp0yaUpGrUqBFKOiEmssUWW4SYWvZJLV++PPtEwk1h1qxZoSQYloRy3+ihlEqJ5IfAZpttlp+MlEsxEvjhhx/Wrl0bsOQbbrjhL7/8cuihh2LP+28Ut7IJi93Vr18/YCoKJgIiIAIiIAIiIAIiUFgCjLSrXr163759Tc6ts9VVrFgx3JLFnZ2RWRY2JDA6R/AN2vJW5mnTpuUtr4AZhdVqIXakgCVXMBEQgWwIhDVmxjd+KJsihRU3rGE8DRs2DKtISiclgcWLF6cMEyRAiC+jKlWqBMkxZRiKxKsWz+zEiRNbt25N+HWqzhsZuZfZCnZr1qwhnQ022CBlUeIGUL4BuYlzQFAWTP0qIC71q4Cg1K/SAqV+lRYuPa8C4lK/igtKK5sE7D8KJgIiIAIiIAIiIAKRJiBVF+nmUeFEQAREQAREQAREICCB/wNLej7u0zhITQAAAABJRU5ErkJggg==)
# MTZ-PIM-Lancamentos_Complementares_Apuracao_ICMS-ST

- **Fonte:** MTZ-PIM-Lancamentos_Complementares_Apuracao_ICMS-ST.docx
- **Modificado:** 2021-01-21
- **Tamanho:** 79 KB

---

THOMSON REUTERS

PIM \- Gestão do Controle de Incentivos Fiscais do Polo Industrial de Manaus

Tela Lançamentos Complementares – Apuração ICMS\-ST

__Localização da tela:__ Específicos, Módulo PIM \- Gestão de Controle de Incentivos Fiscais do Polo Industrial de Manaus, menu Apuração 🡪 Apuração dos Saldos de Impostos e Taxas 🡪 Lançamentos Complementares 🡪 Apuração __ICMS\-ST__

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

__MFS27264__

Vânia Mattos

Inclusão da opção “Copiar Lançamentos” na barra de menu \(ver item “3\-Aba Lançamento de Valores” e item “7\-Cópia dos Lançamentos”\)

MFS32612

Andréa Rocha

Alteração na tela dos Documentos Fiscais Vinculados \(lançamentos do tipo “2”\) para mudar o filtro de recuperação das notas fiscais para seleção do usuário \(vide aba “Lançamento de Valores”\), incluindo o mesmo tratamento existente para o módulo ICMS\.

Sumário

[1\.	Introdução	3](#_Toc62116399)

[2\.	Regras dos Campos	3](#_Toc62116400)

[3\.	Aba APURAÇÃO	4](#_Toc62116401)

[4\.	Aba LANÇAMENTO DE VALORES	4](#_Toc62116402)

[5\.	Aba GUIA	5](#_Toc62116403)

[6\.	Aba DÉBITOS ESPECIAIS	5](#_Toc62116404)

[7\.	CÓPIA DE LANÇAMENTOS	6](#_Toc62116405)

[8\.	Tela de Documentos Fiscais Vinculados	9](#_Toc62116406)

# <a id="_Toc350763252"></a><a id="_Toc62116399"></a>Introdução 

Características da Apuração do ICMS\-ST do Módulo PIM:

- A apuração do ICMS\-ST foi implementada no PIM para atendimento à geração do Sped Fiscal \(OS2388\-AM4, Maio/2009\);
- A apuração segue as mesmas regras da apuração feita no módulo ICMS, com a diferença que na recuperação dos documentos fiscais é feito filtro por inscrição estadual \(campo 126 da SAFX07\)\.
- A apuração *não* utiliza nenhuma regra referente aos incentivos do PIM\. A apuração é basicamente a mesma feita no módulo ICMS, só que separada por inscrição estadual;
- Na emissão do livro \(menu “Obrigações 🡪 Livro de Apuração”\), os dados da Apuração do ICMS\-ST são demonstrados apenas no livro consolidado;

# <a id="_Toc62116400"></a>Regras dos Campos 

As regras desta manutenção estão definidas separadamente para cada uma das abas desta tela: 

     \- Aba __Apuração__

  
     \- Aba __Lançamentos de Valores__

     \- Aba __Guia__

     \- Aba __Débitos Especiais__

__OS4593\-A__: Esta manutenção foi alterada para inclusão do campo “SubaApuração do Sped Fiscal” em cada uma das três abas: “Lançamento de Valores”, “Guia” e “Débitos Especiais” \(ver detalhes nas regras específicas de cada aba\)\.

# <a id="_Toc62116401"></a>Aba APURAÇÃO

# <a id="_Toc62116402"></a>Aba LANÇAMENTO DE VALORES 

__MFS27264__: Incluída a opção __<*Copiar Lançamentos*>__ na barra de menu da aba Lançamento de Valores\. Consultar o funcionamento desta opção no item “__7\-Cópia de Lançamentos__”\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Tipo de Lançamento

Texto

N

S

Formato: 

Combo Box

Default: 

Habilitado e Branco

Este campo é uma lista dos tipos de lançamento do Sped Fiscal \+ opção “branco”, conforme o exemplo abaixo:

 1\-Lançamento referente aos ajustes demonstrados no registro  C197 \(SAFX113\)

 2\-Lançamento associado a outros documentos fiscais

 3\-Outros lançamentos

Default    <branco> 

O campo é de preenchimento não obrigatório, e internamente, poderá ter os valores: nulo, 1, 2 ou 3\.

MFS32612

# <a id="_Toc62116403"></a>Aba GUIA 

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

# <a id="_Toc62116404"></a>Aba DÉBITOS ESPECIAIS 

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

# <a id="_Toc62116405"></a>CÓPIA DE LANÇAMENTOS 

A opção__ __<*Copiar Lançamentos*> foi incluída na barra de menu da aba “__LANÇAMENTO DE VALORES__” na __MFS27264__\. Trata\-se da mesma opção existente no Módulo ICMS, cujo objetivo é permitir a cópia de lançamentos já existentes para o período em questão \(apuração selecionada na aba “Apuração”\)\.

A opção <*Copiar Lançamentos*> ficará habilitada somente após o usuário selecionar uma apuração na aba “APURAÇÃO”\.

Funcionamento:

- Ao clicar nesta opção será aberta uma janela de pesquisa dos lançamentos complementares __\(ICT\_IT\_AP\_SUBS\_IES\)__;
- A princípio a janela aparecerá vazia, com as opções __<PESQUISAR>__ e __<CANCELAR>__, e o usuário poderá:

\- Informar um critério para filtro, e clicar na opção <PESQUISAR>;

\- Não informar critério nenhum, e clicar na opção <PESQUISAR>;

\- Clicar na opção <CANCELAR>, e nesse caso a janela será fechada;

__Selecionar Lançamentos__

DAT\_APURACAO

UF

IND\_UF

COD\_OPER\_APUR 

NUM\_DISCRIMINACAO

VAL\_ITEM\_DISCRIM

__        \.\.\.\.\.\.__

                                                                                   <<<  =  >>>

      __<PESQUISAR>    <CANCELAR>__

- Ao clicar na opção <Pesquisar>, será efetuada a pesquisa de todos os lançamentos que atendam aos critérios informados pelo usuário;
- Serão exibidos apenas os lançamentos que atendam à condição abaixo, e mais o filtro informado pelo usuário \(quando for o caso\);

\- Lançamentos da Empresa e Estabelecimento em questão \(apuração selecionada na aba “Apuração”\); 

- Os lançamentos recuperados na pesquisa serão exibidos na janela de seleção, com as opções __<CRITÉRIO>__, __<CANCELAR>__ e __<OK>__;

__Selecionar Lançamentos__

DAT\_APURACAO

UF

IND\_UF

COD\_OPER\_APUR 

NUM\_DISCRIMINACAO

VAL\_ITEM\_DISCRIM

__        \.\.\.\.\.\.__

                                                                                   <<<  =  >>>

      __<CRITÉRIO>    <CANCELAR>   <OK>__

- Nesse momento, o usuário poderá selecionar os lançamentos desejados;
- Para selecionar mais de um lançamento, será utilizada a tecla <CTRL>;
- Após a seleção dos lançamentos o usuário poderá clicar em uma das seguintes opções da janela:

__Critério__

Nesse caso a janela será limpa, e o usuário poderá informar um outro critério desejado\. 

__Cancelar__

Nesse caso a janela de seleção dos lançamentos será fechada

__OK__

Nesse caso, todos os lançamentos selecionados serão “copiados” conforme descrito abaixo, no item “*Gravação dos Lançamentos Selecionados para cópia*”\.

Ao finalizar o procedimento da cópia, a janela de pesquisa será fechada

 

__Gravação dos lançamentos selecionados para cópia: __

Todos os lançamentos selecionados pelo usuário serão “copiados” para a apuração em questão, considerando os campos descritos no quadro abaixo\.

__Campos da ICT\_IT\_AP\_SUBS\_IES__

__Conteúdo a ser gravado no primeiro lançamento__

COD\_EMPRESA

Dados da apuração para a qual o lançamento será copiado

 

\(apuração selecionada na aba “Apuração”\)

COD\_ESTAB

INSC\_ESTADUAL

COD\_TIPO\_LIVRO

DAT\_APURACAO

IDENT\_ESTADO

Conteúdo do IDENT\_ESTADO do lançamento a ser copiado 

IND\_UF

Conteúdo do IND\_UF do lançamento a ser copiado

COD\_OPER\_APUR

Conteúdo do COD\_OPER\_APUR do lançamento a ser copiado

NUM\_DISCRIMINACAO

Esta coluna é um sequencial calculado pelo sistema\. 

Para cada código da operação do lançamento \(COD\_OPER\_APUR\), é gerada uma sequência de numeração a partir do 1\.

Assim, para cada novo lançamento a ser gravado, será verificado o maior sequencial já existente \(NUM\_DISCRIMINACAO\) para:

\-Empresa \(COD\_EMPRESA\)

\-Estabelecimento \(COD\_ESTAB\)

\-Inscrição Estadual \(INSC\_ESTADUAL\)

\-Código do Tipo do Livro \(COD\_TIPO\_LIVRO\)

\-Data da Apuração \(DAT\_APURACAO\)

\-Código de Operação da Apuração \(COD\_OPER\_APUR\)

O sequencial a ser gravado será = número recuperado \+ 1 

VLR\_ITEM\_DISCRIM

*O valor do lançamento será gravado sempre com zero*

DSC\_ITEM\_APURACAO

Conteúdo do DSC\_ITEM\_APURACAO do lançamento a ser copiado

VLR\_BASE\_ST

Conteúdo do VLR\_BASE\_ST do lançamento a ser copiado

COD\_CLASSE

Conteúdo do COD\_CLASSE do lançamento a ser copiado

IND\_DIG\_CALCULADO

Conteúdo do IND\_DIG\_CALC do lançamento a ser copiado

COD\_AJUSTE\_ICMS

Conteúdo do COD\_AJUSTE\_ICMS do lançamento a ser copiado

IND\_TIPO\_LANC

Conteúdo do IND\_TIPO\_LANC do lançamento a ser copiado

# <a id="_Toc61962688"></a><a id="_Toc62116406"></a>Tela de Documentos Fiscais Vinculados

__\[MFS32612\] Alteração da regra de recuperação dos documentos fiscais, para passar a considerar notas fiscais com ajustes na SAFX113\. Tratamento já   adotado no módulo do ICMS\.__

Esta opção é específica para os tipos de lançamentos igual a “2”\. Clicando nesta opção será possível selecionar documentos fiscais \(SAFX07\) a serem associados ao lançamento, considerando somente os documentos do estabelecimento e inscrição estadual em questão\.

O filtro das notas fiscais a serem disponibilizadas para seleção do usuário foi alterado em relação à condição da nota ter ou não ajustes na SAFX113 \(tabela “filha” da SAFX07\), da seguinte forma:

Na janela de seleção dos documentos fiscais serão consideradas:

 \- Notas fiscais __SEM__ ajustes na SAFX113 __ou__

 \- Notas fiscais __COM__ ajustes na SAFX113, mas que sejam de períodos anteriores \(data fiscal < data inicial do período \(\*\)\) __ou__ 

 \- Notas fiscais __COM__ ajustes na SAFX113, desde que o terceiro caractere do Código de Ajuste informado na SAFX113 seja igual a ‘9’ \(campo 13

 da SAFX113\), e compreendendo o período da apuração em questão __ou__

 \- Notas fiscais __COM__ ajustes na SAFX113, desde que o campo Sub\-Apuração do Sped Fiscal \(campo 24 da SAFX216\) da aba de Lançamentos de Valores esteja preenchido, e compreendendo o período da apuração em questão\.

\(\*\) A data inicial do período será obtida a partir da data da apuração em questão \(data exibida na aba “Apuração”, campo “Data Apuração”\), considerando a periodicidade da apuração\.  

Obs\.: Originalmente só eram disponibilizadas para seleção do usuário as notas fiscais *sem* ajustes\.

Funcionamento da tela:

- Ao selecionar um documento, deverão ser exibidos os dados das seguintes colunas: Data Fiscal,  E/S, Número/Série/Subsérie e Pessoa fis/Jur;
- O campo “N\. Item da NF” deve ser um listbox que exibirá a lista dos itens existentes para a nota selecionada\. Importante: na lista deve existir uma linha em branco, pois a informação do item da nota não é obrigatória;

 

- O valor do ajuste deverá ser informado pelo usuário, pois é uma informação que não consta no documento fiscal, já que nem sempre se trata do próprio valor do ICMS\.
- Ao confirmar a operação, deve\-se verificar:

1\)Verificar se em algum dos documentos informados, o usuário não digitou o valor do ajuste\. Neste caso, exibir a mensagem abaixo:

*         “Informar o conteúdo do campo “Valor do Ajuste” para todos os documentos fiscais selecionados\.”*

2\)Verificar se o total dos valores informados confere com o valor do lançamento complementar\. Caso não, exibir a mensagem abaixo:

*        “O total geral dos ajustes informados não confere com o valor informado no lançamento\. Favor verificar\.”*

3\)Verificar se foram informados documentos fiscais repetidos\. Para isso, pode ser utilizado como critério de comparação as cinco primeiras colunas do quadro “Documentos Fiscais” \(Data Fiscal, E/S,  NF/Série/Subsérie, Pessoa Fis/Jur e N\.Item\)\. Se existirem documentos ou itens de documentos repetidos, exibir a mensagem abaixo:

*      “Existem documentos fiscais ou itens de documentos fiscais repetidos\. Favor verificar\.”*


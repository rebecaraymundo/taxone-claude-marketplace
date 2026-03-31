# MTZ-PIM-Apuracao-DIFAL-UF-Origem-Destino

- **Fonte:** MTZ-PIM-Apuracao-DIFAL-UF-Origem-Destino.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 92 KB

---

THOMSON REUTERS

Módulo PIM – Apuração do ICMS de Diferencial de Alíquota UF Origem / Destino \(EC 87/15\)

__Localização__: Menu Específicos, Módulo: PIM, menu Apuração 🡪 Apuração dos Saldos de Impostos e Taxas 🡪 Geração da Apuração

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS2404

Atendimento ao Ato Cotepe ICMS 44/2015

Criação da nova apuração do ICMS Diferencial de Alíquota UF Origem/Destino, para atendimento ao Ato Cotepe ICMS 44/2015

02/12/2015 \(criação do documento\)

MFS2405

Atendimento ao Ato Cotepe ICMS 44/2015

Atualização da geração para considerar o saldo credor do período anterior e os lançamentos complementares na apuração do saldo final\. 

07/12/2015

MFS3041

\(CH1544\)

Correção na atualização do saldo final

Correção na atualização do saldo final quando resultado = zeros\.

28/01/2016

CH15773\_2016

Correção na apuração do saldo final

Correção na apuração do saldo final para ajustar valores negativos\.

07/07/2016

__MFS6078__

Atendimento ao Ato Cotepe ICMS 7/2016

Alteração da apuração do ICMS Diferencial de Alíquota UF Origem/Destino, para atendimento ao Ato Cotepe ICMS 7/2016 com a separação da declaração dos valores para FCP\.

10/11/2016

Sumário

[1\.	Parâmetros da Tela	3](#_Toc466560830)

[2\.	Origem e Recuperação dos Dados	3](#_Toc466560831)

[3\.	Processamento	4](#_Toc466560832)

# <a id="_Toc466560830"></a>Parâmetros da Tela 

Esta geração é chamada pela Apuração do ICMS \(livro 108\) do Módulo PIM\.

Trata\-se de um dos processos executados de forma separada da apuração principal, assim como é feito também para a Apuração do ICMS\-ST\.

A sua execução depende do parâmetro “__31 \-__ __Apuração ICMS Dif\.Alíquota UF Orig/Dest \- EC 87/15__” da parametrização por Inscrição Estadual do Módulo PIM \(menu “Parâmetros 🡪 Parâmetros por Inscrição Estadual 🡪 Parâmetros de Obrigação Fiscal”\)\.

     \- Quando o parâmetro estiver ativado p/o Estabelecimento e Inscrição Estadual da geração, esta rotina será executada;

     \- Quando o parâmetro *não* estiver ativado p/o Estabelecimento e Inscrição Estadual da geração, esta rotina *não* será executada;

Esta geração é feita a partir dos documentos fiscais da SAFX07/SAFX08, e os resultados obtidos são gravados numa tabela auxiliar e posteriormente são utilizados na geração do Sped Fiscal, registro E310 e “filhos”\.

As informações destes resultados *não* são demonstradas no Livro de Apuração \(P9\), por isso, a emissão do livro não utiliza esses dados\.

# <a id="_Toc350763252"></a><a id="_Toc466560831"></a>Origem e Recuperação dos Dados

__Origem dos Dados__: SAFX07 \- Documentos Fiscais \(Capa\)

                               SAFX08 \- Documentos Fiscais \(Itens\)

Para a apuração do ICMS Diferencial de Aliquota Orig/Dest serão utilizados os seguintes campos dos documentos fiscais:

__Nas notas sem itens__

__\(SAFX07\)__

__Nas notas com itens__

__\(SAFX08\)__

   283\-Valor FCP UF Destino

   221\-Valor FCP UF Destino

   284\-Valor ICMS UF Destino

   222\-Valor ICMS UF Destino

   285\-Valor ICMS UF Origem

   223\-Valor ICMS UF Origem

Serão recuperadas as notas fiscais de operações interestaduais, tanto entradas como saídas, que tenham ao menos algum destes campos preenchidos\.

Como padrão da apuração do Módulo PIM, serão consideradas apenas as notas fiscais da Inscrição Estadual da geração\.

Critérios da recuperação das notas:

\- Empresa – empresa da apuração;

\- Estabelecimento – estabelecimento da apuração;

\- Data da nota – notas com data fiscal enquadrada no período de geração, ou, notas com data extemporânea enquadrada no período de geração;

\- Classificação – notas de classificação 1, 3 ou 4 \(nota de mercadoria, nota mista, ou transporte\);

__\- Inscrição Estadual \(campo 126 da SAFX07\) – inscrição estadual da apuração;__

\- CFOP – apenas as operações interestaduais \(CFOP’s iniciados por “2” ou “6” \);

\- Somente notas não canceladas;

\- Serão consideradas apenas as notas / itens que tenham ao menos algum destes campos preenchidos;

Obs: Teoricamente, estas notas são as notas que serão gravadas no C100 e D100, e que terão os registros C101 e D101 gravados com os valores descritos acima\. O modelo não foi incluído no filtro das notas para evitar a necessidade de manutenção em caso da criação de novos modelos, ou mesmo alterações no Sped Fiscal criando estes valores para outros modelos de documento \(de outros registros além do C100 e D100\)\. De qualquer forma, o usuário só poderá utilizar estes campos seguindo as orientações da Emenda Constitucional 87/2015\. 

 

# <a id="_Toc466560832"></a>Processamento

Com base nos dados recuperados, será feita a totalização dos valores de ICMS e FCP, considerando as entradas como crédito, e as saídas como débitos\. 

A totalização destes valores será feita por UF de Origem e UF de Destino, separadamente\. Ou seja, cada nota pode gerar um valor para a UF Origem e outro para UF Destino\.  

     Exemplo:

     Supondo uma nota de saída com os seguintes valores:

     \- Valor FCP __UF Destino__ = 7,00

     \- Valor ICMS __UF Destino__ = 100,00

     \- Valor ICMS __UF Origem__ = 25,00

     Esta nota irá gerar

     \- Um débito de ICMS de 100,00 para a __UF de Destino__;

     \- Um débito de FCP de 7,00 para a __UF de Destino__;

     \- Um débito de ICMS de 25,00 para a __UF de Origem__;

__A identificação da UF Origem e UF Destino de cada nota é feita de acordo com o tipo de operação, da seguinte forma:__

__🡪__ Para as notas de __saída__:

     \- __UF Origem__ – será sempre a UF do estabelecimento da geração \(que é o contribuinte emitente da nota da venda\);

 

     \- __UF Destino__ – será a UF de destino informada na nota fiscal \(campo “122\-UF Destino” da SAFX07\);

__🡪__ Para as notas de __entrada__:     *\(seriam as devoluções da mercadoria vendida\)*

 

     \- __UF Origem__ – será a UF de origem informada na nota fiscal \(campo “117\-UF Origem” da SAFX07\);

     \- __UF Destino__ – será sempre a UF do estabelecimento da geração \(que recebeu a mercadoria na devolvida\);

Desta forma, para cada __Estabelecimento / Inscrição Estadual__ apurado, teremos:

     \- Uma única apuração para a __UF própria __\(UF do estabelecimento\);

     \- Uma apuração para cada __UF __com as quais__ __existam operações de venda ou retorno no período \(UF de destino, no caso das operações de

      venda, ou UF de origem, no caso das operações de retorno\);

\(“retorno” seria uma operação de devolução, só que, como o destinatário seria no caso um *não contribuinte*, ele não emite nota, e assim, a nota para a devolução da mercadoria seria emitida pelo próprio vendedor\)

Observações sobre o tratamento das notas de entrada:

Conceitualmente, a Emenda Constitucional 87/15 descreve a partilha do ICMS de Diferencial de Alíquota entra as UF’s de origem e destino no caso das operações interestaduais de venda a consumidor final não contribuinte\.

Assim, o foco são as notas de saída\. No entanto, o layout dos novos registros divulgados no Ato Cotepe/ICMS 44/2015 prevê uma apuração destes valores no formato da Apuração do ICMS, prevendo débitos e créditos\.

 

Nas reuniões de estudo sobre o assunto, foi adotado o seguinte conceito para o tratamento das notas de entrada:

   \- A única entrada a ser tratada nesse caso, seriam as operações de retorno da mercadoria devolvida pelo cliente;

   \- Nesse contexto, o cliente \(comprador\) seria um “não contribuinte”, e portanto, não emite nota, sendo assim, quem emitiria a nota da entrada

     seria o próprio contribuinte;

Conforme Guia Prático da versão 2\.0\.18 liberado em 05/01/2016, o tratamento das notas fiscais de entrada segue as orientações descritas nos campos 07 e 08 do registro E310\.

Conforme padrão, para as notas com itens os valores serão totalizados dos itens, e para as notas sem itens, serão totalizados os valores da capa\.

__Gravação dos resultados obtidos por UF:__

Os valores totalizados para cada UF serão gravados numa tabela\. Esta tabela será utilizada posteriormente na geração do Sped Fiscal para geração dos registros E300 e “filhos”, e também na emissão do relatório de conferência desta apuração \(módulo: PIM, menu Relatórios 🡪 Apuração ICMS Dif\.Alíquota UF Orig/Dest \- EC 87/15\)\.

Estrutura da tabela que armazenará os resultados por UF:

__Tipo__

__Tamanho__

__Código da Empresa__

A

003

__Código do Estabelecimento__

A

006

__Inscrição Estadual__

A

014

__Código do Tipo do Livro__

A

003

__Data da Apuração__

Data

008

__UF__

N

012

*\(IDENT\_ESTADO, conforme padrão das tabelas da apuração que têm a identificação do estado\)*

Total Débitos

N

015V002

Total Débitos – FCP

N

015V002

Total Créditos

N

015V002

Total Créditos – FCP

N

015V002

Resultado Devedor

N

015V002

Resultado Credor

N

015V002

Campos que compõe a chave da tabela 🡪   __Empresa__ \+ __Estabelecimento__ \+ __Inscrição 	Estadual__ \+ __Código do Livro__ \+ __Data da Apuração__ \+ __UF__ 

*\(os 5 primeiros campos, Empresa, Estabelecimento, Inscrição Estadual, Código do Livro e Data da Apuração, identificam a apuração em questão na tabela ICT\_APUR\_INSC\_EST\)*

Os resultados obtidos serão gravados na tabela da seguinte forma:

\(assim como todos os processos gerados no Livro de Apuração \(P9\) deve\-se prever a limpeza dos dados da tabela em caso de regeração\)

Empresa

Código da empresa da apuração

Estabelecimento

Código do estabelecimento da apuração

__Inscrição Estadual __

__Inscrição estadual da apuração__

Código do Livro

= 108”

Data da Apuração

Data da apuração

UF

UF apurada

Total Débitos

Valor total dos débitos das __notas de saída__\.

O campo a ser totalizado depende da UF da apuração, da seguinte forma:

Na apuração da __UF de origem __\(UF do Estab\) 🡪 campo VL\_ICMS\_UF\_REM

Na apuração da __UF de destino__ 🡪 campo VL\_ICMS\_UF\_DEST

Total Débitos – FCP

Valor total dos débitos \(FCP\) das __notas de saída__\.

O campo a ser totalizado depende da UF da apuração, da seguinte forma:

Na apuração da __UF de origem __\(UF do Estab\) 🡪 gravar zeros \(ver OBS\)

Na apuração da __UF de destino__ 🡪 campo VL\_FCP\_UF\_DEST

OBS: Não existe valor de FCP para a UF de origem \(remetente\), conforme os valores dos novos registros C101 e D101\. Por isso este campo será gerado com zeros p/a apuração da UF de Origem \(UF do Remetente\)\.

Total Créditos

Valor total dos créditos das __notas de entrada__\.

O campo a ser totalizado depende da UF da apuração, da seguinte forma:

Na apuração da __UF de origem__ 🡪 total do campo VL\_ICMS\_UF\_REM

Na apuração da __UF de destino __\(UF do Estab\) 🡪 campo VL\_ICMS\_UF\_DEST

Total Créditos – FCP

Valor total dos créditos \(FCP\) das __notas de entrada__\.

O campo a ser totalizado depende da UF da apuração, da seguinte forma:

Na apuração da __UF de origem__ 🡪 campo VL\_FCP\_UF\_DEST

Na apuração da __UF de destino __\(UF do Estab\) 🡪 gravar zeros \(ver OBS\)

OBS: Não existe valor de FCP para a UF de origem \(remetente\), conforme os valores dos novos registros C101 e D101\. Na operação de retorno \(devolução\) é utilizado o mesmo campo do FCP para o destinatário \(conforme orientação do Guia Prático vrs 2\.0\.18, registro E311, campo 08\)\.

Resultado Devedor

Este campo será gravado com o resultado da apuração, em caso de __saldo devedor__\.

Caso contrário, o campo será gravado com zeros\.

O cálculo do resultado da apuração da UF é feito conforme a regra abaixo: “__Cálculo do Resultado da Apuração__”\.

Resultado Credor

Este campo será gravado com o resultado da apuração, em caso de __saldo credor__\.

Caso contrário, o campo será gravado com zeros\.

O cálculo do resultado da apuração da UF é feito conforme a regra abaixo: “__Cálculo do Resultado da Apuração__”\.

__Cálculo do Resultado da Apuração__

Este procedimento é necessário porque esta apuração *não* tem a opção de recálculo dos saldos, como existe no livro P9 no menu referente à emissão do livro\. Desta forma, o saldo da apuração é sempre calculado na própria geração, e também na manutenção dos lançamentos\. 

 

Para o cálculo do saldo da UF serão utilizados os seguintes valores:

     __\( A \)__ \- Valor dos débitos e créditos apurados \(campos “Total Débitos”, “Total Débitos\-FCP”, “Total Créditos” e “Total Créditos\-FCP”\);

     __\(__ __B \)__ \- Valor do saldo credor do período anterior, caso exista;

     __\( C \)__ \- Valor dos lançamentos complementares cadastrados para o período e a UF em questão;

__\( A \) \- __São os débitos e créditos apurados para a UF a partir dos documentos fiscais, que serão gravados nos campos:

                             “Total Débitos”, “Total Débitos\-FCP”, “Total Créditos” e “Total Créditos\-FCP”

__\( B \) \- __Recuperação do valor de saldo credor do período anterior da UF \(tabela da “Apuração ICMS Difal UF Orig/Dest”\):

Empresa

Código da empresa da apuração

Estabelecimento

Código do estabelecimento da apuração

Inscrição Estadual

Inscrição Estadual da apuração

Código do Livro

= 108”

Data da Apuração

Data da apuração do período anterior \(anterior ao período da apuração em questão\)

UF

UF para a qual será calculado o resultado

Com base nestes critérios, existe apenas uma linha na tabela para cada UF\. 

O campo que contém o saldo credor é o “Resultado Credor”\.

Caso o registro __*não*__ exista na tabela, será considerado o valor zeros para o saldo credor anterior\. 

__\( C \) __\- Recuperação dos lançamentos complementares da UF:

Tabela: Tabela dos Lançamentos Complementares da Apuração do ICMS de Diferencial de Alíquota UF Origem/Destino \(EC 87/15\)

\(menu: “Apuração 🡪 Apuração dos Saldos de Impostos e Taxas 🡪 Lançamentos Complementares 🡪 Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\)”\) 

   

São todos os lançamentos cadastrados para a UF e período em questão: lançamentos a débito, lançamentos a crédito e as deduções\.

Empresa

Código da empresa da apuração

Estabelecimento

Código do estabelecimento da apuração

Inscrição Estadual

Inscrição Estadual da apuração

Código do Livro

= 108”

Data da Apuração

Data da apuração

UF

UF para a qual será calculado o resultado

Código de Ajuste

Serão considerados apenas os lançamentos em que o quarto caracter do código seja igual a um dos seguintes valores: = 0,1, 2, 3 ou 4\.

*\(os débitos especiais, que têm o quarto caracter = “5”, não entram no cálculo\)*

Alteração da __MFS6078__: O Ato COTEPE ICMS 7/2016 alterou a composição do Registro E310 da obrigação acessória SPED Fiscal, com isso, será necessário considerar o cálculo abaixo até o período de 31/12/2016 \(data que corresponde à versão EFD109\), pois a partir de 01/01/2017 serão consideradas as informações de FCP separadamente ao resultado credor e devedor\.

Saldo final: 

Com base nos valores descritos acima para os itens __A__, __B__ e __C__, a saldo da apuração é calculado da seguinte forma:

 \[ campo “Total Débitos”  \+ campo “Total Débitos\-FCP” \+ total dos lançamentos c/o quarto caracter do cód ajuste = 0 ou 1 \] 

\- 

\[ saldo credor do período anterior \+ campo “Total Créditos” \+ “campo “Total Créditos\-FCP” \+ total dos lançamentos c/o quarto caracter do cód ajuste = 2, 3 ou 4 \]

Alteração do chamado __1544/ 15773\_2016__ __\(MFS3041/ MFS5423\)__: Incluído tratamento quando o resultado for = zeros;

__      Se __o resultado obtido >= zero

  

           O resultado será gravado no campo “__Resultado Devedor__”

           O campo “__Resultado Credor__”será gravado com zeros

__      Senão__

            O resultado “inverso” será gravado no campo “__Resultado Credor__”, ou seja, créditos – débitos, mas *sem considerar os lançamentos *

*            de dedução* \(quarto caracter do cód ajuste = 4\), caso existam\. O cálculo nesse caso será o seguinte:

\[ saldo credor do período anterior \+ campo “Total Créditos” \+ “campo “Total Créditos\-FCP” \+ total dos lançamentos c/o quarto caracter do cód ajuste = 2 ou 3 \]

\-

\[ campo “Total Débitos”  \+ campo “Total Débitos\-FCP” \+ total dos lançamentos c/o quarto caracter do cód ajuste = 0 ou 1 \] 

__      Se __o resultado obtido >= zero

           O resultado será gravado no campo “__Resultado Credor__”

           O campo “__Resultado Devedor__”será gravado com zeros

  

__      Senão __

           O campo “__Resultado Credor__”será gravado com zeros

           O campo “__Resultado Devedor__”será gravado com zeros;

= = = = = =

Alteração da __MFS6078__: O Ato COTEPE ICMS 7/2016 alterou a composição do Registro E310 da obrigação acessória SPED Fiscal, com isso, será necessário considerar o cálculo abaixo a partir de 01/01/2017 \(versão EFD110\), em serão consideradas as informações de FCP separadamente ao resultado credor e devedor\. 

__Cálculo do Resultado da Apuração__

Este procedimento é necessário porque esta apuração *não* tem a opção de recálculo dos saldos, como existe no livro P9 no menu referente à emissão do livro\. Desta forma, o saldo da apuração é sempre calculado na própria geração, e também na manutenção dos lançamentos\. 

 

Para o cálculo do saldo da UF serão utilizados os seguintes valores:

__\( A \)__ \- Valor dos débitos e créditos apurados para o diferencial de alíquota \(campos “Total Débitos” e “Total Créditos”\);

__\(__ __B \)__ \- Valor do saldo credor do período anterior para o diferencial de alíquota, caso exista;

__\( C \)__ \- Valor dos lançamentos complementares cadastrados para o período e a UF em questão para o diferencial de alíquota;

__\( D \)__ \- Valor dos débitos e créditos apurados para o fundo de combate à pobreza \(campos “Total Débitos\-FCP” e “Total Créditos\-FCP”\);

__\(__ __E \)__ \- Valor do saldo credor do período anterior para o fundo de combate à pobreza, caso exista;

__\( F \)__ \- Valor dos lançamentos complementares cadastrados para o período e a UF em questão para o fundo de combate à pobreza;

__\( A \) \- __São os débitos e créditos do diferencial de alíquota apurados para a UF a partir dos documentos fiscais, que serão gravados nos campos:

                             “Total Débitos” e “Total Créditos”

__\( B \) \- __Recuperação do valor de saldo credor do período anterior do diferencial de alíquota da UF \(tabela da “Apuração ICMS Difal UF Orig/Dest”\):

Empresa

Código da empresa da apuração

Estabelecimento

Código do estabelecimento da apuração

No caso da Apuração do ICMS por Inscrição Estadual Única, será o código do estabelecimento centralizador\.

Código do Livro

= “108” \(no caso da Apuração do ICMS normal\)

= “165” \(no caso da Apuração do ICMS por Inscrição Estadual Única\)

Data da Apuração

Data da apuração do período anterior \(anterior ao período da apuração em questão\)

UF

UF para a qual será calculado o resultado

Com base nestes critérios, existe apenas uma linha na tabela para cada UF\. 

O campo que contém o saldo credor é o “Resultado Credor”\.

Caso o registro __*não*__ exista na tabela, será considerado o valor zeros para o saldo credor anterior\. 

__\( C \) __\- Recuperação dos lançamentos complementares da UF:

Tabela: Tabela dos Lançamentos Complementares da Apuração do ICMS de Diferencial de Alíquota UF Origem/Destino \(EC 87/15\)

\(menu: “Apuração 🡪 Apuração do ICMS 🡪 Lançamentos Complementares 🡪 Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\)”\) 

   

São todos os lançamentos do diferencial de alíquota cadastrados para a UF e período em questão: lançamentos a débito, lançamentos a crédito e as deduções\.

Empresa

Código da empresa da apuração

Estabelecimento

Código do estabelecimento da apuração

No caso da Apuração do ICMS por Inscrição Estadual Única, será o código do estabelecimento centralizador\.

Código do Livro

= “108” \(no caso da Apuração do ICMS normal\)

= “165” \(no caso da Apuração do ICMS por Inscrição Estadual Única\)

Data da Apuração

Data da apuração

UF

UF para a qual será calculado o resultado

Código de Ajuste

Serão considerados apenas os lançamentos em que tenha o terceiro caractere igual a 2 e o quarto caractere do código igual a um dos seguintes valores: = 0,1, 2, 3 ou 4\.

*\(os débitos especiais, que têm o quarto caracter = “5”, não entram no cálculo\)*

__\( D \) \- __São os débitos e créditos do fundo de combate à pobreza apurados para a UF a partir dos documentos fiscais, que serão gravados nos campos:

                             “Total Débitos\-FCP” e “Total Créditos\-FCP”

__\( E \) \- __Recuperação do valor de saldo credor do período anterior do fundo de combate à pobreza da UF \(tabela da “Apuração ICMS Difal UF Orig/Dest”\):

Empresa

Código da empresa da apuração

Estabelecimento

Código do estabelecimento da apuração

No caso da Apuração do ICMS por Inscrição Estadual Única, será o código do estabelecimento centralizador\.

Código do Livro

= “108” \(no caso da Apuração do ICMS normal\)

= “165” \(no caso da Apuração do ICMS por Inscrição Estadual Única\)

Data da Apuração

Data da apuração do período anterior \(anterior ao período da apuração em questão\)

UF

UF para a qual será calculado o resultado

Com base nestes critérios, existe apenas uma linha na tabela para cada UF\. 

O campo que contém o saldo credor é o “Resultado Credor”\.

Caso o registro __*não*__ exista na tabela, será considerado o valor zeros para o saldo credor anterior\. 

__\( F \) __\- Recuperação dos lançamentos complementares da UF:

Tabela: Tabela dos Lançamentos Complementares da Apuração do ICMS de Diferencial de Alíquota UF Origem/Destino \(EC 87/15\)

\(menu: “Apuração 🡪 Apuração do ICMS 🡪 Lançamentos Complementares 🡪 Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\)”\) 

   

São todos os lançamentos do fundo de combate à pobreza para a UF e período em questão: lançamentos a débito, lançamentos a crédito e as deduções\.

Empresa

Código da empresa da apuração

Estabelecimento

Código do estabelecimento da apuração

No caso da Apuração do ICMS por Inscrição Estadual Única, será o código do estabelecimento centralizador\.

Código do Livro

= “108” \(no caso da Apuração do ICMS normal\)

= “165” \(no caso da Apuração do ICMS por Inscrição Estadual Única\)

Data da Apuração

Data da apuração

UF

UF para a qual será calculado o resultado

Código de Ajuste

Serão considerados apenas os lançamentos em que tenha o terceiro caractere igual a 3 e o quarto caractere do código seja igual a um dos seguintes valores: = 0,1, 2, 3 ou 4\.

*\(os débitos especiais, que têm o quarto caracter = “5”, não entram no cálculo\)*

__Saldo final__ para coluna de __Diferencial de Alíquota__ da Apuração da EC 87/2015: 

Com base nos valores descritos acima para os itens __A__, __B__ e __C__, a saldo da apuração é calculado da seguinte forma:

 \[ campo “Total Débitos”  \+ total dos lançamentos c/o terceiro caractere do cód ajuste = 2 e c/o quarto caractere do cód ajuste = 0 ou 1 \] 

\- 

\[ saldo credor do período anterior do diferencial de alíquota \+ campo “Total Créditos” \+ “total dos lançamentos c/o terceiro caractere do cód ajuste = 2 e c/o quarto caractere do cód ajuste = 2, 3 ou 4 \]

__      Se __o resultado obtido >= zero

  

           O resultado será gravado no campo “__Resultado Devedor__”

           O campo “__Resultado Credor__”será gravado com zeros

__      Senão__

            O resultado “inverso” será gravado no campo “__Resultado Credor__”, ou seja, créditos – débitos, mas *sem considerar os lançamentos *

*            de dedução* \(quarto caractere do cód ajuste = 4\), caso existam\. O cálculo nesse caso será o seguinte:

\[ saldo credor do período anterior do diferencial de alíquota \+ campo “Total Créditos” \+ total dos lançamentos /o terceiro caractere do cód ajuste = 2 e c/o quarto caractere do cód ajuste = 2 ou 3 \]

\-

\[ campo “Total Débitos”  \+ total dos lançamentos c/o terceiro caractere do cód ajuste = 2 c/o quarto caractere do cód ajuste = 0 ou 1 \] 

__      Se __o resultado obtido >= zero

           O resultado será gravado no campo “__Resultado Credor__”

           O campo “__Resultado Devedor__”será gravado com zeros

  

__      Senão __

           O campo “__Resultado Credor__”será gravado com zeros

           O campo “__Resultado Devedor__”será gravado com zeros;

__Saldo final__ para coluna de __Fundo de Combate à Pobreza \- FCP__ da Apuração da EC 87/2015: 

Com base nos valores descritos acima para os itens __D__, __E__ e __F__, a saldo da apuração é calculado da seguinte forma:

 \[ campo “Total Débitos\-FCP”  \+ total dos lançamentos c/o terceiro caractere do cód ajuste = 3 e c/o quarto caractere do cód ajuste = 0 ou 1 \] 

\- 

\[ saldo credor do período anterior do FCP \+ campo “Total Créditos\-FCP” \+ “total dos lançamentos c/o terceiro caractere do cód ajuste = 3 e c/o quarto caractere do cód ajuste = 2, 3 ou 4 \]

__      Se __o resultado obtido >= zero

  

           O resultado será gravado no campo “__Resultado Devedor__”

           O campo “__Resultado Credor__”será gravado com zeros

__      Senão__

            O resultado “inverso” será gravado no campo “__Resultado Credor__”, ou seja, créditos – débitos, mas *sem considerar os lançamentos *

*            de dedução* \(quarto caractere do cód ajuste = 4\), caso existam\. O cálculo nesse caso será o seguinte:

\[ saldo credor do período anterior do FCP \+ campo “Total Créditos\-FCP” \+ total dos lançamentos c/o terceiro caractere do cód ajuste = 3 e c/o quarto caractere do cód ajuste = 2 ou 3 \]

\-

\[ campo “Total Débitos\-FCP”  \+ total dos lançamentos c/o terceiro caractere do cód ajuste = 3 c/o quarto caractere do cód ajuste = 0 ou 1 \] 

__      Se __o resultado obtido >= zero

           O resultado será gravado no campo “__Resultado Credor__”

           O campo “__Resultado Devedor__”será gravado com zeros

  

__      Senão __

           O campo “__Resultado Credor__”será gravado com zeros

           O campo “__Resultado Devedor__”será gravado com zeros;

= = = = = =

 

 


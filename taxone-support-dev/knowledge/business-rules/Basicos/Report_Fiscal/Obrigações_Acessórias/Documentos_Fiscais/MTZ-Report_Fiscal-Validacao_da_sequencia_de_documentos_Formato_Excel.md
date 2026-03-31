# MTZ-Report_Fiscal-Validacao_da_sequencia_de_documentos_Formato_Excel

- **Fonte:** MTZ-Report_Fiscal-Validacao_da_sequencia_de_documentos_Formato_Excel.docx
- **Modificado:** 2025-09-09
- **Tamanho:** 153 KB

---

THOMSON REUTERS

Módulo Report Fiscal – Relatório de Validação da Sequencia de Documentos – Formato Excel

__Localização__ 🡪 Menu: Básicos, Módulo: Report Fiscal, menu Obrigações Acessórias 🡪 Documentos Fiscais 🡪 Validação na Sequência de Documentos – Formato Excel

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS78918

Liliane Videira Assaf

Criação do Documento

23/02/2022

MFS443502

Andréa Rocha

Inclusão de um parâmetro para definir se serão mostrados os documentos inexistentes no arquivo gerado

09/01/2023

MFS520224

Andréa Rocha

Inclusão de um parâmetro para definir se será mostrada uma linha de resumo com a coluna de total de documentos inexistentes zerada

14/03/2023

Sumário

[1\.	Parâmetros da Tela	1](#_Toc96526543)

[2\.	Origem e Recuperação dos Dados	1](#_Toc96526544)

[3\.	Processamento	1](#_Toc96526545)

[4\.	Layout e Preenchimento dos Dados no Relatório em Excel	1](#_Toc96526546)

[5\.	Layout e Prenchimento dos Dados no Relatório em Tela	1](#_Toc96526547)

[6\.	Exemplos	1](#_Toc96526548)

# <a id="_Toc96526543"></a>Parâmetros da Tela 

__Tela deve ser desenvolvida em Framework\.__

__Aba Parâmetros__:

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

Tipo de Execução: \( \) Imediata     \( \) Programada   Data/Hora de Execução \[ dd/mm/aaaa hh:mm \]                 \[Executar\]

Data Inicial: \[DD/MM/AAAA\] 

Data Final:  \[DD/MM/AAAA\]

Classificação de Documento: \[                                \\/\]

Série de Documento:              \[                                \\/\] 

Informar Série :    \[           \]

Modelo de Documento:          \[                                \\/\]

Informar Modelo: \[          \]

Sequência de Numeração dos Documentos:

\( \) Única para documentos de entrada e saída

\( \) Numeração de entrada distinta da saída

\[  \] Validar NF de entrada \(emitidas pelo Estabelecimento\)

\[  \] Validar NF de saída

\[  \] Exibir Numeração dos Documentos Inexistentes

\[  \] Exibir Resumo com a coluna Total Documentos Inexistentes zerada

\[ \] Inscrição Estadual \(PIM\)

UF: \[     \\/\]

Estabelecimento:

\[ \] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[ \] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[ \] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[ \] xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

	

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Data Inicial

Data

__S__

S

DD/MM/AAAA

Este campo deve ser preenchido com a Data Inicial do período da geração\.

Valor Default:

Data Incial: primeiro dia do mês corrente\.

Consistências:

Deve ser uma data válida\.

Caso o campo não seja preenchido, exibir mensagem na tela:

        “Informe Data Inicial”

__Obs\.: Relatório foi limitado a geração de 31 dias, essa limitação se faz necessária devido ao estouro de capacidade de memória PGA na utilização de algumas funções presentes no referido relatório, esse estouro de memória PGA é decorrente da própria arquitetura do banco de dados Oracle\.__

Data Final

Data

__S__

S

DD/MM/AAAA

Este campo deve ser preenchido com a Data Final do período da geração\.

Valor Default:

Data Final: último dia do mês corrente\.

Consistências:

Deve ser uma data válida\.

Caso o campo não seja preenchido, exibir mensagem na tela:

        “Informe Data Final”

Caso a Data Final informada seja menor que a Data Inicial, gravar no log a seguinte mensagem:

“A Data Inicial deve ser menor ou igual a Data Final informada\.”

__Obs\.: Relatório foi limitado a geração de 31 dias, essa limitação se faz necessária devido ao estouro de capacidade de memória PGA na utilização de algumas funções presentes no referido relatório, esse estouro de memória PGA é decorrente da própria arquitetura do banco de dados Oracle\.__

Classificação de Documento

Alfanumérico

__S__

S

Listbox

Lista composta pelas seguintes opções:

 \- “Todos”

 \- “1 – Documento de Mercadoria”

 \- “2 – Documento de Serviço”

 \- “3 – Documento Misto”

Opção Default: “Todos”

Consistências:

Caso o campo não seja preenchido, exibir mensagem na tela:

        “Informe Classificação de Documento”

Série de Documento

Alfanumério

__S__

S

Listbox

Lista composta pelas seguintes opções:

\- Todas

\- Série Específica

\- Documentos sem Série

Opção Default: “Todas”

Consistências:

Caso o campo não seja preenchido, exibir mensagem na tela:

        “Informe Série de Documento”

Informar Série

Alfanumérico 

__N__

S

Texto

Caixa de texto com 3 posições para digitação da série do documento\.

Se no campo “Série de Documento” for selecionada a opção “Série Específica”, então: 

   Habilitar o campo para digitação\.

Senão:

    Desabilitar o campo\.

Consistências:

Caso este campo não seja preenchido, quando a opção “Série Específica” estiver selecionada, gravar mensagem no log:

        “O campo Informar Série deve ser preenchido, uma vez que a opção Série Específica foi selecionada\.”

Modelo de Documento

Alfanumério

__S__

S

Listbox

Lista composta pelas seguintes opções:

\- Todos

\- Modelo Específico

Opção Default: “Todos”

Consistências:

Caso o campo não seja preenchido, exibir mensagem na tela:

        “Informe Modelo de Documento”

Informar Modelo

Alfanumérico 

__N__

S

Texto

Caixa de texto com 2 posições para digitação do modelo do documento\.

Se no campo “Modelo de Documento” for selecionada a opção “Modelo Específico”, então: 

   Habilitar o campo para digitação\.

Senão:

    Desabilitar o campo\.

Consistências:

Caso este campo não seja preenchido, quando a opção “Modelo Específico” estiver selecionada, gravar mensagem no log:

        “O campo Informar Modelo deve ser preenchido, uma vez que a opção Modelo Específico foi selecionada\.”

Sequência de Numeração dos Documentos

Alfanumério

__S__

S

Radiobutton

Campo do tipo Radiobutton, composto pelas seguintes opções:

\-  Única para documentos de entrada e saída

\-  Numeração de entrada distinta da saída 

Opção Default: Única para documentos de entrada e saída

Validar NF de entrada \(emitidas pelo Estabelecimento\)

Alfanumérico

__N__

S

Checkbox

Campo será habilitado quando a opção “Numeração de entrada distinta da saída” for selecionada no campo “Sequência de Numeração dos Documentos”\. Caso contrário, campo permanece desabilitado\.

Validar NF de saída

Alfanumérico

__N__

S

Checkbox

Campo será habilitado quando a opção “Numeração de entrada distinta da saída” for selecionada no campo “Sequência de Numeração dos Documentos”\. Caso contrário, campo permanece desabilitado\.

Consistências:

Caso a opção “Numeração de entrada distinta da saída” for selecionada no campo “Sequência de Numeração dos Documentos”, pelo menos uma das opções abaixo deve ser selecionada:

\[  \] Validar NF de entrada \(emitidas pelo Estabelecimento\)

\[  \] Validar NF de saída

Caso ambas estejam desmarcadas, então gravar mensagem no log:

“Pelo menos uma das opções de Validar NF \(entrada e/ou saída\) deve ser escolhida, uma vez que a opção Numeração de entrada distinta da saída foi selecionada\.”

Exibir Numeração dos Documentos Inexistentes

Alfanumérico

__N__

S

Checkbox

__\[MFS443502\]__ Inclusão do parâmetro para definir se serão mostrados os documentos inexistentes no arquivo gerado

Esta opção deve ser marcada para os usuários que quiserem demonstrar os documentos fiscais inexistentes\.

Exibir Resumo com a coluna Total Documentos Inexistentes zerada

Alfanumérico

__N__

S

Checkbox

__\[MFS520224\]__ Inclusão do parâmetro para definir se será mostrada uma linha de resumo com a coluna de total de documentos inexistentes zerada

Esta opção deve ser marcada para os usuários que quiserem ver o resumo dos documentos fiscais que foram processados e não têm problema de sequência, ou seja, o total de documentos inexistentes está zerado\.

Inscrição Estadual \(PIM\)

Alfanumérico

__N__

S

Checkbox

Esta opção deve ser marcada para os contribuintes que trabalham com inscrição estadual do módulo PIM\.

Para os contribuintes do PIM, documentos fiscais são carregados com a informação da inscrição estadual PIM \(campo 126 da SAFX07 e campo 11 da SAFX130\) e a sequência de documentos fiscais é validada por inscrição estadual PIM\.

UF

Listbox

Lista montada com todas as Unidades Federativas, adicionando a opção \* Todas as UFs\*\.

Tabela: ESTADO

Montar a lista começando pela opção \* Todas as UFs\* e as demais opções em ordem crescente pela descrição da UF\. Veja

\- \* Todas as Ufs \*

\- Acre

\- Alagoas

\- Amazonas

Etc\.\.

Estabelecimentos

Alfanumérico 

__S__

S

Neste campo é exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário\.

__Se__ parâmetro “Inscrição Estadual \(PIM\)” = marcado

     Serão disponibilizados para seleção os estabelecimentos com suas Inscrições Estaduais cadastradas em Parâmetros > Funcionais > Inscrições Estaduais do Estabelecimento \(AM\) do módulo PIM, atendendo a “UF” informada em tela\.

    Para montagem dessa listagem, fazer uma consulta envolvendo as tabelas:

    \- ESTABELECIMENTO, 

    \- ICT\_ESTAB\_IESTAD \(tabela de Inscrições Estaduais do PIM\)

    Considerar os critérios:

    Se campo “UF” for preenchido com opção \* Todas as Ufs\*:

       \- Considerar os estabelecimentos de todas as Unidades Federativas\.

    Senão:

       \- Considera apenas os estabelecimentos da UF selecionada\. 

    \- Associar as tabelas ESTABELECIMENTO e ICT\_ESTAB\_IESTAD através dos campos COD\_EMPRESA, COD\_ESTAB\.

    Demonstrar os seguintes campos de forma concatenada, na listagem de estabelecimentos:

    \- COD\_ESTAB \+ RAZAO\_SOCIAL \+ INSC\_ESTADUAL

__Senão __

     Serão disponibilizados para seleção os estabelecimentos que atendam a “UF” informada em tela\.

    Para montagem dessa listagem, fazer uma consulta envolvendo a tabelas:

    \- ESTABELECIMENTO

    Considerar os critérios:

    Se campo “UF” for preenchido com opção \* Todas as Ufs\*:

       \- Considerar os estabelecimentos de todas as Unidades Federativas\.

    Senão:

       \- Considera apenas os estabelecimentos da UF selecionada\. 

    Demonstrar os seguintes campos de forma concatenada, na listagem de estabelecimentos:

    \- COD\_ESTAB \+ RAZAO\_SOCIAL 

    

 

A lista de estabelecimentos depende da escolha dos parâmetros “Inscrição Estadual \(PIM\)” e “UF”\. Por isso ao abrir a janela, o campo Estabelecimento não virá carregado\. Apenas será carregado após a escolha dos referidos parâmetros\.

__Atenção\!\!__

Todos os registros de estabelecimento \(ou estabelecimento/inscrição estadual PIM\) selecionados na tela, devem ser gerados num único número de processo\. Para isso utilize a opção __MULTISELECT __na package framework ao invés de MULTIPROC\. 

Assim, atenderemos ao requisito de gerarmos um único arquivo excel com todos os estabelecimentos \(ou estabelecimento/inscrição estadual PIM\)  selecionados em tela\.

Selecionar

N

N

Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos\.

O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimento”:

Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimentos” já marcados\. 

   

Marcar todos

N

N

Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos”\.

# <a id="_Toc350763252"></a><a id="_Toc96526544"></a>Origem e Recuperação dos Dados 

Origem dos Dados: Tabela de Capa de Documentos Fiscals \(X07\_DOCTO\_FISCAL\);

                                Tabela de Notas Fiscais Denegadas/Inutilizadas \(x130\_NFE\_DENEGADA\_INUTILIZADA\);

  

A partir dos parâmetros informados em tela, montar uma consulta que recupere os registros da X07 \+ X130\. A ordenação dos documentos depende do parâmetro “Inscrição Estadual \(PIM\)” disponível na tela\. 

Se o parâmetro “__Inscrição Estadual \(PIM\)__” estiver marcado na tela, a ordenação será através dos campos:

    Código do Estabelecimento, __Inscrição Estadual __\(campos INSC\_ESTADUAL – item 126 da SAFX07 e item 11 da SAFX130\), Serie do Documento, SubSerie, Modelo Documento, Número do Documento Fiscal e Data fiscal\.

Se o parâmetro “__Inscrição Estadual \(PIM\)__” estiver desmarcado na tela, a ordenação será:

    Código do Estabelecimento, Serie do Documento, SubSerie, Modelo Documento, Número do Documento Fiscal e Data fiscal\.

SELECT X07\_DOCTO\_FISCAL

__UNION ALL__

SELECT X130\_NFE\_DENEGADA\_INUTILIZADA

Order by

cod\_estab,

insc\_estadual \(considerar apenas quando parâmetro “Inscrição Estadual \(PIM\)” estiver marcado\)

serie\_docfis,

sub\_serie\_docfis,

cod\_modelo,

num\_docfis, \(\*\)

data\_fiscal

\(\*\) Quanto ao campo NUM\_DOCFIS:

\- Preencher com zeros a esquerda para realizar a ordenação de forma correta\.

\- Quando a tabela for X130\_NFE\_DENEGADA\_INUTILIZADA, considera o NUM\_DOC\_FIS\_INI na ordenação\.

Critérios de recuperação das notas na X07\_DOCTO\_FISCAL:

\- Código da Empresa – Empresa do login;

\- Código do Estabelecimento – Estabelecimento selecionado em tela;

\-  Se o parâmetro “__Inscrição Estadual \(PIM\)__” estiver marcado na tela:

       __Inscrição Estadual __\(campo INSC\_ESTADUAL – item 126 da SAFX07\) = Inscrição Estadual selecionada em tela \(informada no campo Estabelecimento\)\.

  Se o parâmetro “__Inscrição Estadual \(PIM\)__” estiver desmarcado na tela, a ordenação será:

      Não utilizar o campo __Inscrição Estadual __\(campo INSC\_ESTADUAL – item 126 da SAFX07\) como filtro\. 

\- Data Fiscal – compreendida entre a Data Inicial e Final do período informado em tela;

Se a opção de seqüencia escolhida seja “Única para documentos de entrada e saída”, então:

   \- Considerar Movimento E/S \(movto\_e\_s\) = ‘2’, ‘3’, ‘4’, ‘5’, ‘9’

Se a opção de seqüencia escolhida seja “Numeração de entrada distinta da saída”, então:

    Se “Validar NF de entrada \(emitidas pelo Estabelecimento\)” estiver marcado, e “Validar NF de saída” estiver desmarcado, então:

    \- Considerar Movimento E/S \(movto\_e\_s\) = ‘2’, ‘3’, ‘4’, ‘5’

    Se “Validar NF de saída” estiver marcado, e “Validar NF de entrada \(emitidas pelo Estabelecimento\)” estiver desmarcado então:

    \- Considerar Movimento E/S \(movto\_e\_s\) = ‘9’’

    Se “Validar NF de entrada \(emitidas pelo Estabelecimento\)” estiver marcado, e “Validar NF de saída” estiver marcado, então:

    \- Considerar Movimento E/S \(movto\_e\_s\) = ‘2’, ‘3’, ‘4’, ‘5’, ‘9’

Se para “Série de Documento” for selecionada a opção “Todas”:

    \- Considerar todas as Séries, ou seja, não utilizar o campo Serie \(serie\_docfis\) como filtro\.

Se para “Série de Documento” for selecionada a opção “Série Específica”:

    \- Considerar Série \(serie\_docfis\) = série informada no campo “Informar Série” da tela\.

Se para “Série de Documento” for selecionada a opção “Documentos sem Série”:

    \- Considerar Série \(serie\_docfis\) = ‘ ‘ \(um espaço em branco\)\.

Se para “Modelo de Documento” for selecionada a opção “Todos”:

    \- Considerar todos os Modelos de Documento Fiscal, ou seja, não utilizar o campo Modelo \(cod\_modelo\) como filtro\.

Se para “Modelo de Documento” for selecionada a opção “Modelo Específico”:

    \- Considerar Modelo \(cod\_modelo\) = modelo informado no campo “Informar Modelo” da tela\.

Se para “Classificação de Documento” for escolhida a opção “Todos”

    \- Considerar todas os Códigos de Classificação de Documento Fiscal, ou seja, não utilizar o campo COD\_CLASS\_DOC\_FIS como filtro\.

Se para “Classificação de Documento” for escolhida a opção “1 – Documento de Mercadoria”

    \- Considerar Código de Classificação de Documento Fiscal \(COD\_CLASS\_DOC\_FIS\) = ‘1’\.

Se para “Classificação de Documento” for escolhida a opção “2 – Documento de Serviço”

    \- Considerar Código de Classificação de Documento Fiscal \(COD\_CLASS\_DOC\_FIS\) = ‘2’\.

Se para “Classificação de Documento” for escolhida a opção “3 – Documento Misto”

    \- Considerar Código de Classificação de Documento Fiscal \(COD\_CLASS\_DOC\_FIS\) = ‘3’\.

Campos a recuperar  das notas na X07\_DOCTO\_FISCAL:

cod\_estab,

insc\_estadual \(recuperar apenas quando parâmetro Inscrição Estadual \(PIM\) estiver marcado\)

serie\_docfis,

sub\_serie\_docfis,

cod\_modelo,

num\_docfis,

data\_fiscal,

razao\_social do estabelecimento,

movto\_e\_s

Critérios de recuperação das notas na X130\_NFE\_DENEGADA\_INUTILIZADA:

\- Código da Empresa – Empresa do login;

\- Código do Estabelecimento – Estabelecimento selecionado em tela;

\-  Se o parâmetro “__Inscrição Estadual \(PIM\)__” estiver marcado na tela:

       __Inscrição Estadual __\(campo INSC\_ESTADUAL – item 11 da SAFX130\) = Inscrição Estadual selecionada em tela \(informada no campo Estabelecimento\)\.

  Se o parâmetro “__Inscrição Estadual \(PIM\)__” estiver desmarcado na tela, a ordenação será:

      Não utilizar o campo __Inscrição Estadual __\(campo INSC\_ESTADUAL – item 11 da SAFX130\) como filtro\. 

\- Data Referência – compreendida entre a Data Inicial e Final do período informado em tela;

Se a opção de seqüencia escolhida seja “Única para documentos de entrada e saída”, então:

   \- Considerar Movimento E/S \(movto\_e\_s\) = ‘2’, ‘3’, ‘4’, ‘5’, ‘9’

Se a opção de seqüencia escolhida seja “Numeração de entrada distinta da saída”, então:

    Se “Validar NF de entrada \(emitidas pelo Estabelecimento\)” estiver marcado, e “Validar NF de saída” estiver desmarcado, então:

    \- Considerar Movimento E/S \(movto\_e\_s\) = ‘2’, ‘3’, ‘4’, ‘5’

    Se “Validar NF de saída” estiver marcado, e “Validar NF de entrada \(emitidas pelo Estabelecimento\)” estiver desmarcado então:

    \- Considerar Movimento E/S \(movto\_e\_s\) = ‘9’’

    Se “Validar NF de entrada \(emitidas pelo Estabelecimento\)” estiver marcado, e “Validar NF de saída” estiver marcado, então:

    \- Considerar Movimento E/S \(movto\_e\_s\) = ‘2’, ‘3’, ‘4’, ‘5’, ‘9’

Se para “Série de Documento” for selecionada a opção “Todas”:

    \- Considerar todas as Séries, ou seja, não utilizar o campo Serie \(serie\_docfis\) como filtro\.

Se para “Série de Documento” for selecionada a opção “Série Específica”:

    \- Considerar Série \(serie\_docfis\) = série informada no campo “Informar Série” da tela\.

Se para “Série de Documento” for selecionada a opção “Documentos sem Série”:

    \- Considerar Série \(serie\_docfis\) = ‘ ‘ \(um espaço em branco\)\.

Se para “Modelo de Documento” for selecionada a opção “Todos”:

    \- Considerar todos os Modelos de Documento Fiscal, ou seja, não utilizar o campo Modelo \(cod\_modelo\) como filtro\.

Se para “Modelo de Documento” for selecionada a opção “Modelo Específico”:

    \- Considerar Modelo \(cod\_modelo\) = modelo informado no campo “Informar Modelo” da tela\.

Campos a recuperar  das notas na X130\_NFE\_DENEGADA\_INUTILIZADA:

cod\_estab,

insc\_estadual \(recuperar apenas quando parâmetro Inscrição Estadual \(PIM\) estiver marcado\)

serie\_docfis,

sub\_serie\_docfis,

cod\_modelo,

num\_docfis\_ini,

num\_docfis\_fim,

data\_ref,

razao\_social,

movto\_e\_s

# <a id="_Toc96526545"></a>Processamento

__Passo 1: Montagem das Sequencias de Documentos a serem validadas:__

Nesse passo vamos separar os documentos em sequências de documentos para serem validadas no passo 2\.

Se o parâmetro “__Inscrição Estadual \(PIM\)__” estiver marcado na tela:

   A sequência de documentos é formada pelos documentos fiscais de mesmo estabelecimento, __Inscrição Estadual__, série, subsérie e modelo\.

Se o parâmetro “__Inscrição Estadual \(PIM\)__” estiver desmarcado na tela, a ordenação será:

   A sequência de documentos é formada pelos documentos fiscais de mesmo estabelecimento, série, subsérie e modelo\.

Esta sequência pode conter documentos de entrada e saída, ou apenas entradas ou apenas saída, vai depender da opção escolhida em tela, conforme descrito abaixo:

__Se__ a opção de seqüencia escolhida for “__Única para documentos de entrada e saída__”, então:

   \- A Sequencia de Documentos será formada por todos os documentos recuperados da X07 e X130 \(Movimento E/S \(movto\_e\_s\) = ‘2’, ‘3’, ‘4’, ‘5’, ‘9’\) de mesmo estabelecimento, série, subsérie e modelo \(se parâmetro “__Inscrição Estadual \(PIM\)__” estiver desmarcado\), ou de mesmo estabelecimento,  inscrição estadual, série, subsérie e modelo \(se parâmetro “__Inscrição Estadual \(PIM\)__” estiver marcado\)\.

__Se__ a opção de seqüencia escolhida for “__Numeração de entrada distinta da saída__”, então:

    Separar em sequencias distintas os documentos de entrada e saída recuperados da X07 e X130:

    \- Sequencia de Documentos de Entrada: formada pelas notas com Movimento E/S \(movto\_e\_s\) = ‘2’, ‘3’, ‘4’, ‘5’ de mesmo estabelecimento, série, subsérie e modelo \(se parâmetro “__Inscrição Estadual \(PIM\)__” estiver      desmarcado\), ou de mesmo estabelecimento,  inscrição estadual, série, subsérie e modelo \(se parâmetro “__Inscrição Estadual \(PIM\)__” estiver marcado\)\.

    \- Sequencia de Documentos de Saída: formada pelas notas com Movimento E/S \(movto\_e\_s\) = ‘9’’ de mesmo estabelecimento, série, subsérie e modelo \(se parâmetro “__Inscrição Estadual \(PIM\)__” estiver desmarcado\), ou      de mesmo estabelecimento,  inscrição estadual, série, subsérie e modelo \(se parâmetro “__Inscrição Estadual \(PIM\)__” estiver marcado\)\.

    Se “Validar NF de entrada \(emitidas pelo Estabelecimento\)” estiver marcado, e “Validar NF de saída” estiver desmarcado, então:

    \- Processar as Sequencias de Documentos de Entrada no passo 2\.

    Se “Validar NF de saída” estiver marcado, e “Validar NF de entrada \(emitidas pelo Estabelecimento\)” estiver desmarcado então:

    \- Processar as Sequencias de Documentos de Saída no passo 2\.

    Se “Validar NF de entrada \(emitidas pelo Estabelecimento\)” estiver marcado, e “Validar NF de saída” estiver marcado, então:

    \- Processar as Sequencias de Documentos de Entrada no passo 2\.

    \- Processar as Sequencias de Documentos de Saída no passo 2\.

Exemplo:

Supondo que tenhamos os seguintes documentos fiscais de um determinado estabelecimento e estejamos trabalhando com o parâmetro “__Inscrição Estadual \(PIM\)__” estiver desmarcado:

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

01

A

55

2

000001

X07

01

A

55

2

000002

X07

01

A

55

9

000003

X07

01

A

55

2

000004 – 000005

X130

01

A

55

9

000006

X07

01

A

55

2

000007

X07

01

A

55

9

000008

X07

02

55

2

000001

X07

02

55

2

000002

X07

02

55

9

000003 – 000004

X130

Se opção de seqüencia escolhida seja “__Única para documentos de entrada e saída__”, teremos duas sequencias de documentos para validação:

Sequencia 01, formada pelos documentos de série __01__:

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

01

A

55

2

000001

X07

01

A

55

2

000002

X07

01

A

55

9

000003

X07

01

A

55

2

000004 – 000005

X130

01

A

55

9

000006

X07

01

A

55

2

000007

X07

01

A

55

9

000008

X07

Sequencia 02, formada pelos documentos de série __02__:

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

02

55

2

000001

X07

02

55

2

000002

X07

02

55

9

000003 – 000004

X130

__Se__ a opção de seqüencia escolhida for “__Numeração de entrada distinta da saída__”, então teremos as sequencias de documentos de entrada separadas das saídas:

Sequencia 01, formada pelos documentos de série 01 de entrada:

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

01

A

55

2

000001

X07

01

A

55

2

000002

X07

01

A

55

2

000004 – 000005

X130

01

A

55

2

000007

X07

Sequencia 02, formada pelos documentos de série 01 de saída:

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

01

A

55

9

000003

X07

01

A

55

9

000006

X07

01

A

55

9

000008

X07

Sequencia 03, formada pelos documentos de série 02 de entrada:

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

02

55

2

000001

X07

02

55

2

000002

X07

Sequencia 04, formada pelos documentos de série 02 de saída:

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

02

55

9

000003 – 000004

X130

__Passo 2: Processamento das Sequencias de Documentos:__

Para cada sequencia de documentos fiscais montada no passo 1 efetuar a varredura da sequencia verificando documentos inexistentes:

1. Recupera o primeiro documento da sequencia\. 
2. Verifica se o proximo documento da sequência é igual ao número do documento anteiror \+ 1\.
3. Caso não seja, este é um documento inexistente que será demonstrado no relatório\.

Lembrando que Uma nota só será considerada “faltante” quando ela não existir na X07 e nem na X130 \(lembrando que na X130 deve\-se utilizar o range de ‘número de documento inicial’ e ‘número de documento final’, já que não é necessário cadastrar um registro na X130 para cada nota denegada/inutilizada\)\.

1. Continue a varredura, recuperando a numeração de documento fiscal inexistentes na sequencia, até chegar ao último documento da sequência\.

Exemplo:

Vamos seguir com o exemplo dos documentos fiscais apresentados no passo 1:

Se opção de seqüencia escolhida seja “__Única para documentos de entrada e saída__”, teremos duas sequencias de documentos para validação:

Sequencia 01, formada pelos documentos de série __01__:

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

01

A

55

2

000001

X07

01

A

55

2

000002

X07

01

A

55

9

000003

X07

01

A

55

2

000004 – 000005

X130

01

A

55

9

000006

X07

01

A

55

2

000007

X07

01

A

55

9

000008

X07

Sequencia 02, formada pelos documentos de série __02__:

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

02

55

2

000001

X07

02

55

2

000002

X07

02

55

9

000003 – 000004

X130

As duas sequências de documento são processadas e o resultado do processamento é:

\- Sequência 01: sem documentos fiscais inexistentes\.

\- Sequência 02: sem documentos fiscais inexistentes\.

__Se__ a opção de seqüencia escolhida for “__Numeração de entrada distinta da saída__”, então teremos as sequencias de documentos de entrada separadas das saídas:

Sequencia 01, formada pelos documentos de série 01 de entrada:

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

01

A

55

2

000001

X07

01

A

55

2

000002

X07

01

A

55

2

000004 – 000005

X130

01

A

55

2

000007

X07

Sequencia 02, formada pelos documentos de série 01 de saída:

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

01

A

55

9

000003

X07

01

A

55

9

000006

X07

01

A

55

9

000008

X07

Sequencia 03, formada pelos documentos de série 02 de entrada:

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

02

55

2

000001

X07

02

55

2

000002

X07

Sequencia 04, formada pelos documentos de série 02 de saída:

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

02

55

9

000003 – 000004

X130

Se “Validar NF de entrada \(emitidas pelo Estabelecimento\)” estiver marcado, então:

    As Sequencias 01 e 03 são processadas e o resultado do processamento é: 

    \- Sequência 01: Documentos fiscais inexistentes = 000003, 000006\.

    \- Sequência 03: sem documentos fiscais inexistentes\.

Se “Validar NF de saída” estiver marcado, então:

    As Sequencias 02 e 04 são processadas e o resultado do processamento é: 

    \- Sequência 02: Documentos fiscais inexistentes = 000004, 000005, 000007\.

    \- Sequência 04: sem documentos fiscais inexistentes\.

# <a id="_Toc96526546"></a>Layout e Preenchimento dos Dados no Relatório em Excel

Gerar um único arquivo formato Excel \(extensão xlsx\) com todos os estabelecimentos \(e estabelecimentos/inscrição estadual \(PIM\) se parâmetro “__Inscrição Estadual \(PIM\)__” estiver marcado\) que foram selecionados na tela de geração\.

Nomeclatura: “Relacao\_Documentos\_Inexistentes\_DD\_MM\_AAAA\_DD\_MM\_AAAA\.xlsx

Onde:

DD\_MM\_AAAA: Data Inicial informada na tela

DD\_MM\_AAAA: Data Final informada na tela

´

Se o número de registros a serem gravados no arquivo ultrapassar o limite do excel \(1milhão de linhas\), quebrar em mais de um arquivo, adicionando ao nome do arquivo um sequencial \(Relacao\_Documentos\_Inexistentes\_DD\_MM\_AAAA\_DD\_MM\_AAAA\_1\.xlsx, Relacao\_Documentos\_Inexistentes\_DD\_MM\_AAAA\_DD\_MM\_AAAA\_2\.xls,\.\.\.\)\. Este tratamento feito no Relatorio de NF p/ CFOP – Formato XLS do Report Fiscal \(ver package REL\_NF\_CFO\_EXCEL\_FPROC \)\.

O arquivo será composto pelas seguintes colunas:

Cod\. Estabelecimento

Código do Estabelecimento da Sequencia onde foi identificado o documento fiscal inexistente\.

Utilizar o caracter especial chr\(2\) concatenado com o COD\_ESTAB, para que no Excel o código do estabelecimento se mantenha com zeros à esquerda\.

Obs: esse tratamento é feito na package PKG\_DW\_CONF\_CHAVE\.

Razão Social

Razão Social do Estabelecimento\.

*Inscrição Estadual \(PIM\)*

Caso o parâmetro “__Inscrição Estadual \(PIM\)__” esteja marcado na tela de geração, então:

    A coluna Inscrição Estadual \(PIM\) deve compor o arquivo\.

    Neste caso, prencher com a Inscrição Estadual \(PIM\) da sequencia onde foi identificado o documento fiscal

    inexistente\.

Caso o parâmetro “__Inscrição Estadual \(PIM\)__” esteja desmarcado na tela de geração, então:

    A coluna Inscrição Estadual \(PIM\) __NÃO__ deve compor o arquivo\.

Utilizar o caracter especial chr\(2\) concatenado com o INSC\_ESTADUAL, para que no Excel a inscrição se mantenha com zeros à esquerda\.

Faixa de Datas

Informar o primeiro e último dia da faixa de documentos fiscais que foram lidos \(existentes na base\)\.

Modelo

Código do Modelo da sequencia onde foi identificado o documento fiscal inexistente\.

Utilizar o caracter especial chr\(2\) concatenado com o COD\_MODELO, para que no Excel o código do modelo se mantenha com zeros à esquerda\.

E/S

Quando a opção escolhida for “Única para documentos de entrada e saída”, então:

   Preencher com “E/S”\.

Quando a opção escolhida for “Numeração de entrada distinta da saída”, então:

  Se o documento inexistente foi identificado na sequência de documentos de entrada, preencher com “E”\. 

  Se o documento inexistente foi identificado na sequência de documentos de saída, preencher com “S”\.

Série

Série da sequencia onde foi identificado o documento fiscal inexistente\.

Utilizar o caracter especial chr\(2\) concatenado com a SERIE\_DOCFIS, para que no Excel a série se mantenha com zeros à esquerda\.

Subsérie

Subsérie da sequencia onde foi identificado o documento fiscal inexistente\.

Utilizar o caracter especial chr\(2\) concatenado com a SUB\_SERIE\_DOCFIS, para que no Excel a subsérie se mantenha com zeros à esquerda\.

Faixa de Notas

Informar o primeiro e último da faixa de documentos fiscais que foram lidos \(existentes na base\)\.

Documento Inexistente

__\[MFS443502\]__ Inclusão do parâmetro para definir se serão mostrados os documentos inexistentes no arquivo gerado

Se o parâmetro “Exibir Numeração dos Documentos Inexistentes” estiver marcado

      Mostrar a coluna “Número do Documento Fiscal inexistente”

Senão

      Não mostrar a coluna “Número do Documento Fiscal inexistente”\.

Utilizar o caracter especial chr\(2\) concatenado com a NUM\_DOCFIS, para que no Excel o numero do documento se mantenha com zeros à esquerda\.

# <a id="_Toc96526547"></a>Layout e Prenchimento dos Dados no Relatório em Tela 

Além do relatório em Excel, ao final da execução, demonstrar um resumo na tela Framework com o segunte layout:

__Título da Aba__: Resumo da Validação de Documentos

__Layout__::

		Resumo da Validação da Sequência de Documentos

Período: DD/MM/AAAA a DD/MM/AAAA

Num\. Processo: 999999999

Estabelecimento  | Inscrição Estadual \(PIM\)  | Faixa de Datas | Total Documentos Lidos | Total Documentos Inexistentes

XXXXXX              | YYYYYYYYYYYYYY        |                          | 999999999 |                              9999999999 |

Obs: A coluna “Inscrição Estadual \(PIM\)” só deve ser apresentada caso o parâmetro “__Inscrição Estadual \(PIM\)__” esteja marcado na tela de geração\.

__Preenchimento dos campos__:

Campos de Cabeçalho:

Período

Data Inicial e Final do período informado na tela de geração

Num\. Processo

Número do processo da execução da rotina framework\.

Campos do Detalhe do Relatório:

Cod\. Estabelecimento

Código do Estabelecimento informado na tela de geração\.

*Inscrição Estadual \(PIM\)*

Caso o parâmetro “__Inscrição Estadual \(PIM\)__” esteja marcado na tela de geração, então:

    A coluna Inscrição Estadual \(PIM\) deve compor o relatório\.

    Neste caso, preencher com a Inscrição Estadual \(PIM\) informada na tela de geração\.

Caso o parâmetro “__Inscrição Estadual \(PIM\)__” esteja desmarcado na tela de geração, então:

    A coluna Inscrição Estadual \(PIM\) __NÃO__ deve compor o relatório\.

Faixa de Datas

Informar o primeiro e último dia da faixa de documentos fiscais que foram lidos \(existentes na base\)\.

Série/Sub

Série e Subsérie da sequencia onde foi identificado o documento fiscal inexistente

Modelo

Código do Modelo da sequencia onde foi identificado o documento fiscal inexistente\.

Faixa de Notas

Informar o primeiro e último da faixa de documentos fiscais que foram lidos \(existentes na base\)\.

Total Documentos Lidos

Total de registros recuperados das tabelas X07\_DOCTO\_FISCAL e x130\_NFE\_DENEGADA\_INUTILIZADA, considerando o parâmetro “Inscrição Estadual \(PIM\)”\.

Caso o parâmetro “Inscrição Estadual \(PIM\)” esteja marcado na tela de geração, então:

    Total de registros recuperados por o estabelecimento e Inscrição Estadual \(campo 126 da SAFX07, campo 11 da SAFX130\)\.

Caso o parâmetro “Inscrição Estadual \(PIM\)” esteja desmarcado na tela de geração, então:

    Total de registros recuperados por o estabelecimento\.

Total Documentos Inexistentes

Total de documentos inexistentes contabilizados\.

Caso o parâmetro “Inscrição Estadual \(PIM\)” esteja marcado na tela de geração, então:

    Total de documentos inexistentes contabilizados por estabelecimento e Inscrição Estadual \(PIM\)\.

Caso o parâmetro “Inscrição Estadual \(PIM\)” esteja desmarcado na tela de geração, então:

    Total de documentos inexistentes contabilizados por estabelecimento\.

__\[MFS520224\] __Inclusão do parâmetro para definir se será mostrada uma linha de resumo com a coluna de total de documentos inexistentes zerada

__Obs\.: __ Se o parâmetro “Exibir Resumo com a coluna Total Documentos Inexistentes zerada” estiver marcado

	    Deve ser exibida uma linha com o resumo dos documentos fiscais que foram processados e não têm problema de sequência, ou seja, a coluna de total de documentos inexistentes está zerado

           Senão

                 Não exibir essa linha\.

# <a id="_Toc96526548"></a>Exemplos 

¨__6\.1 – Validação com Inscrição Estadual \(PIM\):__

Supondo que tenhamos os seguintes documentos fiscais de um determinado estabelecimento \(001AM\) e estejamos trabalhando com o parâmetro “__Inscrição Estadual \(PIM\)__” estiver MARCADO:

Este estabelecimento possui duas inscrições estaduas PIM cadastradas em Parâmetros > Funcionais > Inscrições Estaduais do Estabelecimento \(AM\) do módulo PIM:

Estab

Inscrição Estadual

001AM

041504330

001AM

062001558

As notas fiscais estão com a informação de Inscrição Estadual preenchidas nas SAFX07 e na SAFX130 \(campo 126 da SAFX07 e campo 11 da SAFX130\)\.

Estab

Inscrição Estadual

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

041504330

01

A

01

2

000001

X07

001AM

041504330

01

A

01

9

000003

X07

001AM

041504330

01

A

55

2

000007

X07

001AM

041504330

01

A

55

2

000008

X07

001AM

041504330

01

A

55

2

000011

X07

001AM

041504330

02

55

2

000002

X07

001AM

041504330

02

55

9

000005

X07

001AM

041504330

02

55

2

000006 \- 000006 

X130

001AM

041504330

02

55

2

000009

X07

001AM

062001558

02

55

9

000003 – 000004

X130

001AM

062001558

02

55

9

000006

X07

001AM

062001558

02

55

9

000008 – 000009

X130

001AM

062001558

02

55

9

000011

X07

Se opção de seqüencia escolhida seja “__Única para documentos de entrada e saída__”, teremos as seguintes sequencias de documentos para validação:

Sequencia 01, formada pelos documentos de Inscrição estadual 041504330, série __01__, subserie A e modelo 01:

Estab

Inscrição Estadual

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

041504330

01

A

01

2

000001

X07

001AM

041504330

01

A

01

9

000003

X07

Sequencia 02, formada pelos documentos de Inscrição estadual 041504330, série __01__, subserie A e modelo 55:

Estab

Inscrição Estadual

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

041504330

01

A

55

2

000007

X07

001AM

041504330

01

A

55

2

000008

X07

001AM

041504330

01

A

55

2

000011

X07

Sequencia 03, formada pelos documentos de Inscrição estadual 041504330,série __02__, sem subserie e modelo 55:

Estab

Inscrição Estadual

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

041504330

02

55

2

000002

X07

001AM

041504330

02

55

9

000005

X07

001AM

041504330

02

55

2

000006 \- 000006 

X130

001AM

041504330

02

55

2

000009

X07

Sequencia 04, formada pelos documentos de Inscrição estadual 062001558,série __02__, sem subserie e modelo 55:

Estab

Inscrição Estadual

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

062001558

02

55

9

000003 – 000004

X130

001AM

062001558

02

55

9

000006

X07

001AM

062001558

02

55

9

000008 – 000009

X130

001AM

062001558

02

55

9

000011

X07

__Resultado gravado no arquivo  __Relacao\_Documentos\_Inexistentes\_DD\_MM\_AAAA\_DD\_MM\_AAAA\.xlsx__ __

Cod\. Estabelecimento

Razão Social

Inscrição Estadudal \(PIM\)

Modelo

E/S

Série

Subserie

Documento Inexistente

Faixa de Datas

Faixa de Notas

001AM

xxxxxx

041504330

01

E/S

01

A

000002

000001 a 000003

001AM

xxxxxx

041504330

55

E/S

01

A

000009

000007 a 000011

001AM

xxxxxx

041504330

55

E/S

01

A

000010

000007 a 000011

001AM

xxxxxx

041504330

55

E/S

02

000003

000002 a 000009

001AM

xxxxxx

041504330

55

E/S

02

000004

000002 a 000009

001AM

xxxxxx

041504330

55

E/S

02

000007

000002 a 000009

001AM

xxxxxx

041504330

55

E/S

02

000008

000002 a 000009

001AM

xxxxxx

062001558

55

E/S

02

000005

000003 a 000011

001AM

xxxxxx

062001558

55

E/S

02

000007

000003 a 000011

001AM

xxxxxx

062001558

55

E/S

02

000010

000003 a 000011

__Resultado no relatório da tela__: Resumo da Validação de Documentos

		Resumo da Validação da Sequência de Documentos

Período: DD/MM/AAAA a DD/MM/AAAA

Num\. Processo: 999999999

Estabelecimento  | Inscrição Estadual \(PIM\)  | Faixa de Datas | Serie/Sub | Modelo | Faixa de Notas     |  Total Documentos Lidos | Total Documentos Inexistentes

001AM                 |    041504330                    |                          |  01/A        |      01    |000001 a 000003  |                                       2 | 1

001AM                 |    041504330                    |                          |  01/A        |      55    |000007 a 000011  |                                       3 | 2

001AM                 |    041504330                    |                          |  02/          |      55    |000002 a 000009  |                                       4 | 4

001AM                 |    062001558                    |                          |  02/          |      55    |000003 a 000011  |                                       4 | 3

__Se__ a opção de seqüencia escolhida for “__Numeração de entrada distinta da saída__”, então teremos as sequencias de documentos de entrada separadas das saídas:

Sequencia 01E, formada pelos documentos de Inscrição estadual 041504330, série __01__, subserie A e modelo 01 de entrada:

Estab

Inscrição Estadual

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

041504330

01

A

01

2

000001

X07

Sequencia 01S, formada pelos documentos de Inscrição estadual 041504330, série __01__, subserie A e modelo 01 de saída:

Estab

Inscrição Estadual

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

041504330

01

A

01

9

000003

X07

Sequencia 02, formada pelos documentos de Inscrição estadual 041504330, série __01__, subserie A e modelo 55 de entrada:

Estab

Inscrição Estadual

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

041504330

01

A

55

2

000007

X07

001AM

041504330

01

A

55

2

000008

X07

001AM

041504330

01

A

55

2

000011

X07

Sequencia 03E, formada pelos documentos de Inscrição estadual 041504330,série __02__, sem subserie e modelo 55 de entrada:

Estab

Inscrição Estadual

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

041504330

02

55

2

000002

X07

001AM

041504330

02

55

2

000006 \- 000006 

X130

001AM

041504330

02

55

2

000009

X07

Sequencia 03S, formada pelos documentos de Inscrição estadual 041504330,série __02__, sem subserie e modelo 55 de saída:

Estab

Inscrição Estadual

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

041504330

02

55

9

000005

X07

Sequencia 04, formada pelos documentos de Inscrição estadual 062001558,série __02__, sem subserie e modelo 55 de saída:

Estab

Inscrição Estadual

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

062001558

02

55

9

000003 – 000004

X130

001AM

062001558

02

55

9

000006

X07

001AM

062001558

02

55

9

000008 – 000009

X130

001AM

062001558

02

55

9

000011

X07

__Resultado gravado no arquivo  __Relacao\_Documentos\_Inexistentes\_DD\_MM\_AAAA\_DD\_MM\_AAAA\.xlsx__ __

Cod\. Estabelecimento

Razão Social

Inscrição Estadudal \(PIM\)

Modelo

E/S

Série

Subserie

Documento Inexistente

Faixa de Datas

Faixa de Notas

001AM

xxxxxx

041504330

55

E

01

A

000009

000007 a 000011

001AM

xxxxxx

041504330

55

E

01

A

000010

000007 a 000011

001AM

xxxxxx

041504330

55

E

02

000003

000002 a 000009

001AM

xxxxxx

041504330

55

E

02

000004

000002 a 000009

001AM

xxxxxx

041504330

55

E

02

000005

000002 a 000009

001AM

xxxxxx

041504330

55

E

02

000007

000002 a 000009

001AM

xxxxxx

041504330

55

E

02

000008

000002 a 000009

001AM

xxxxxx

062001558

55

S

02

000005

000003 a 000011

001AM

xxxxxx

062001558

55

S

02

000007

000003 a 000011

001AM

xxxxxx

062001558

55

S

02

000010

000003 a 000011

__Resultado no relatório da tela__: Resumo da Validação de Documentos

		Resumo da Validação da Sequência de Documentos

Período: DD/MM/AAAA a DD/MM/AAAA

Num\. Processo: 999999999

Estabelecimento  | Inscrição Estadual \(PIM\)  | Faixa de Datas    | Serie/Sub | Modelo | Faixa de Notas     |  Total Documentos Lidos | Total Documentos Inexistentes

001AM                 |    041504330                    |                             | 01/A          |   01      |000001 a 000001   |                                     1  |                                               0 |

001AM                 |    041504330                    |                             | 01/A          |   01      |000003 a 000003   |                                     1  |                                               0 |

001AM                 |    041504330                    |                             | 01/A          |   55      |000007 a 000011   |                                     3  |                                               2 |

001AM                 |    041504330                    |                             | 02             |   55      |000002 a 000009   |                                     3  |                                               5 |

001AM                 |    041504330                    |                             | 02             |   55      |000005 a 000005   |                                     1  |                                               0 |

001AM                 |    062001558                    |                             | 02             |   55      |000003 a 000011   |                                      4 |                                               3 |

¨__6\.2 – Validação sem Inscrição Estadual \(PIM\):__

Supondo que tenhamos os seguintes documentos fiscais de dois estabelecimentos \(001AM, 001SP\) que não trabalham com Inscrição Estadual do PIM, ou seja, o parâmetro “__Inscrição Estadual \(PIM\)__” está DESMARCADO:

As notas fiscais NÃO estão com a informação de Inscrição Estadual preenchidas nas SAFX07 e na SAFX130 \(campo 126 da SAFX07 e campo 11 da SAFX130\)\.

Estab

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

01

A

01

2

000001

X07

001AM

01

A

01

9

000002

X07

001AM

01

A

01

2

000003

X07

001AM

01

A

01

9

000005 \- 000006

X130

001AM

01

A

01

2

000011

X07

001AM

01

A

55

2

000004

X07

001AM

01

A

55

2

000007

X07

001AM

02

A

55

2

000001 \- 000009 

X130

001AM

02

A

55

2

000011

X07

001AM

02

55

9

000013 – 000015

X130

001AM

02

55

2

000016

X07

001AM

02

55

9

000018 – 000019

X130

001AM

02

55

2

000021

X07

001SP

01

A

01

2

000001

X07

001SP

01

A

01

2

000003

X07

Se opção de seqüencia escolhida seja “__Única para documentos de entrada e saída__”, teremos as seguintes sequencias de documentos para validação:

Sequencia 01, formada pelos documentos de série __01__, subserie A e modelo 01, do estabelecimento 001AM:

Estab

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

01

A

01

2

000001

X07

001AM

01

A

01

9

000002

X07

001AM

01

A

01

2

000003

X07

001AM

01

A

01

9

000005 – 000006

X130

001AM

01

A

01

2

000011

X07

Sequencia 02, formada pelos documentos de série __01__, subserie A e modelo 55, do estabelecimento 001AM:

Estab

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

01

A

55

2

000004

X07

001AM

01

A

55

2

000007

X07

Sequencia 03, formada pelos documentos de série __02__, subserie A e modelo 55, do estabelecimento 001AM:

Estab

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

02

A

55

2

000001 \- 000009 

X130

001AM

02

A

55

2

000011

X07

Sequencia 04, formada pelos documentos de série __02__, sem subserie e modelo 55, do estabelecimento 001AM:

Estab

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

02

55

9

000013 – 000015

X130

001AM

02

55

2

000016

X07

001AM

02

55

9

000018 – 000019

X130

001AM

02

55

2

000021

X07

Sequencia 05, formada pelos documentos de série __01__, subserie A e modelo 01, do estabelecimento 001SP:

Estab

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001SP

01

A

01

2

000001

X07

001SP

01

A

01

2

000003

X07

__Resultado gravado no arquivo  __Relacao\_Documentos\_Inexistentes\_DD\_MM\_AAAA\_DD\_MM\_AAAA\.xlsx__ __

Cod\. Estabelecimento

Razão Social

Modelo

E/S

Série

Subserie

Documento Inexistente

Faixa de Datas

Faixa de Notas

001AM

xxxxxx

01

E/S

01

A

000004

000001 a 000011

001AM

xxxxxx

01

E/S

01

A

000007

000001 a 000011

001AM

xxxxxx

01

E/S

01

A

000008

000001 a 000011

001AM

xxxxxx

01

E/S

01

A

000009

000001 a 000011

001AM

xxxxxx

01

E/S

01

A

000010

000001 a 000011

001AM

xxxxxx

55

E/S

01

A

000005

000004 a 000007

001AM

xxxxxx

55

E/S

01

A

000006

000004 a 000007

001AM

xxxxxx

55

E/S

02

A

000010

000001 a 000011

001AM

xxxxxx

55

E/S

02

000017

000013 a 000021

001AM

xxxxxx

55

E/S

02

000020

000013 a 000021

001SP

yyyyyy

01

E/S

01

A

000002

000001 a 000003

__Resultado no relatório da tela__: Resumo da Validação de Documentos

		Resumo da Validação da Sequência de Documentos

Período: DD/MM/AAAA a DD/MM/AAAA

Num\. Processo: 999999999

Estabelecimento  | Faixa de Datas    | Serie/Sub | Modelo | Faixa de Notas     |  Total Documentos Lidos | Total Documentos Inexistentes

001AM                 |                             | 01/A         | 01         | 000001 a 000011 |                                        5|                                                5

001AM                 |                             | 01/A         | 55         | 000004 a 000007 |                                        2|                                                2

001AM                 |                             | 02/A         | 55         | 000001 a 000011 |                                        2|                                                1

001AM                 |                             | 02            | 55         | 000013 a 000021 |                                        4|                                                2

001SP                 |                              | 01/A         | 01        | 000001 a 000003 |                                        2|                                                1

__Se__ a opção de seqüencia escolhida for “__Numeração de entrada distinta da saída__”, então teremos as sequencias de documentos de entrada separadas das saídas:

Sequencia 01E, formada pelos documentos de série __01__, subserie A e modelo 01, do estabelecimento 001AM de entrada:

Estab

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

01

A

01

2

000001

X07

001AM

01

A

01

2

000003

X07

001AM

01

A

01

2

000011

X07

Sequencia 01S, formada pelos documentos de série __01__, subserie A e modelo 01, do estabelecimento 001AM de Saída:

Estab

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

01

A

01

9

000002

X07

001AM

01

A

01

9

000005 \- 000006

X130

Sequencia 02, formada pelos documentos de série __01__, subserie A e modelo 55, do estabelecimento 001AM de Entrada:

Estab

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

01

A

55

2

000004

X07

001AM

01

A

55

2

000007

X07

Sequencia 03, formada pelos documentos de série __02__, subserie A e modelo 55, do estabelecimento 001AM de entrada:

Estab

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

02

A

55

2

000001 \- 000009 

X130

001AM

02

A

55

2

000011

X07

Sequencia 04E, formada pelos documentos de série __02__, sem subserie e modelo 55, do estabelecimento 001AM, de Entrada:

Estab

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

02

55

2

000016

X07

001AM

02

55

2

000021

X07

Sequencia 04S, formada pelos documentos de série __02__, sem subserie e modelo 55, do estabelecimento 001AM, de Saída:

Estab

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001AM

02

55

9

000013 – 000015

X130

001AM

02

55

9

000018 – 000019

X130

Sequencia 05, formada pelos documentos de série __01__, subserie A e modelo 01, do estabelecimento 001SP, de Entrada:

Estab

Série

SubSérie

Modelo

Movto E/S

Nota Fiscal

Tabela

001SP

01

A

01

2

000001

X07

001SP

01

A

01

2

000003

X07

__Resultado gravado no arquivo  __Relacao\_Documentos\_Inexistentes\_DD\_MM\_AAAA\_DD\_MM\_AAAA\.xlsx__ __

Cod\. Estabelecimento

Razão Social

Modelo

E/S

Série

Subserie

Documento Inexistente

Faixa de Datas 

Faixa de Notas

001AM

xxxxxx

01

E

01

A

000002

000001 a 000011

001AM

xxxxxx

01

E

01

A

000004

000001 a 000011

001AM

xxxxxx

01

E

01

A

000005

000001 a 000011

001AM

xxxxxx

01

E

01

A

000006

000001 a 000011

001AM

xxxxxx

01

E

01

A

000007

000001 a 000011

001AM

xxxxxx

01

E

01

A

000008

000001 a 000011

001AM

xxxxxx

01

E

01

A

000009

000001 a 000011

001AM

xxxxxx

01

E

01

A

000010

000001 a 000011

001AM

xxxxxx

01

S

01

A

000003

000002 a 000006

001AM

xxxxxx

01

S

01

A

000004

000002 a 000006

001AM

xxxxxx

55

E

01

A

000005

000004 a 000007

001AM

xxxxxx

55

E

01

A

000006

000004 a 000007

001AM

xxxxxx

55

E

02

A

000010

000001 a 000011

001AM

xxxxxx

55

E

02

000017

000016 a 000021

001AM

xxxxxx

55

E

02

000018

000016 a 000021

001AM

xxxxxx

55

E

02

000019

000016 a 000021

001AM

xxxxxx

55

E

02

000020

000016 a 000021

001AM

xxxxxx

55

S

02

000016

000013 a 000019

001AM

xxxxxx

55

S

02

000017

000013 a 000019

001SP

yyyyyy

01

E

01

A

000002

000001 a 000003

__Resultado no relatório da tela__: Resumo da Validação de Documentos

		Resumo da Validação da Sequência de Documentos

Período: DD/MM/AAAA a DD/MM/AAAA

Num\. Processo: 999999999

Estabelecimento  | Faixa de Datas    | Serie/Sub | Modelo | Faixa de Notas     |  Total Documentos Lidos | Total Documentos Inexistentes

001AM                 |                             | 01/A         | 01         | 000001 a 000011 |                                        3|                                                8

001AM                 |                             | 01/A         | 01         | 000002 a 000006 |                                        2|                                                2

001AM                 |                             | 01/A         | 55         | 000004 a 000007 |                                        2|                                                2

001AM                 |                             | 02/A         | 55         | 000001 a 000011 |                                        2|                                                1

001AM                 |                             | 02            | 55         | 000016 a 000021 |                                        2|                                                4

001AM                 |                             | 02            | 55         | 000013 a 000019 |                                        2|                                                2

001SP                 |                              | 01/A         | 01        | 000001 a 000003 |                                        2|                                                1

= = = = = =

 


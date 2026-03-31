# MTZ-DES_IF-Tela_de_Manutencao_Registro_0440

- **Fonte:** MTZ-DES_IF-Tela_de_Manutencao_Registro_0440.docx
- **Modificado:** 2021-09-17
- **Tamanho:** 86 KB

---

THOMSON REUTERS

Validador DES\-IF 

Manutenção do Registro 0440 – Módulo 2 

__Localização__: Menu Municipal, módulo São Paulo \- Financeiras, menu Manutenção 🡪 Módulo 2 🡪 Registro 0440 \- Demonstrativo do ISSQN mensal a recolher \(DAIR\)

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS35905__

Liliane Assaf

Criação da tela de manutenção do registro 0440 específico do validador DESIF

14/04/2020

Sumário

[1\.	Regras Gerais	1](#_Toc37236796)

[2\.	Layout da Tela	1](#_Toc37236797)

[3\.	Regras de Funcionamento dos Campos	1](#_Toc37236798)

# <a id="_Toc37236796"></a>Regras Gerais

Esta funcionalidade tem como objetivo possibilitar a imputação de deduções e ajustes na receita declarada, incentivos autorizados em lei e depósitos judiciais que não são identificados por registros de saldos ou lançamentos contábeis da empresa, mas que fazem parte da apuração do ISSQN de instituições financeiras\. Tais informações serão apresentadas no registro 0440 do arquivo Módulo 2 do validador da DES\-IF\.

Informações de Deduções, incentivos fiscais, compensações e processos de suspensão de exibigilidade devem ser inseridas nesta tela, antes da realização da geração do meio magnético – bancos, e devem estar de acordo com o Tipo de Consolidação a se considerado na geração do arquivo módulo 2\.

A geração do arquivo módulo 2 no meio magnético \- bancos, apura o ISSQN a partir das contas contábeis que tiveram tributação de ISSQN com registros de saldos contábeis \(SAFX02\) no mês\. O registro 0440 é gerado consolidando os registros de saldos, de acordo com o tipo de consolidação escolhido na geração, podendo ser: por Alíquota ou por Alíquota e Código de Tributação Desif\.  As informações imputadas manualmente nessa tela, são recuperadas de acordo com o tipo de consolidação e completam a apuração do ISSQN a recolher a ser apresentado no registro 0440\.

O Tipo de Consolidação é determinado pela legislação de cada município\. 

1 \- Instituição e alíquota

2 – Instituição, alíquota e código de tributação DES\-IF

3 – Dependência e alíquota

4 – Dependência, alíquota e código de tributação DES\-IF\.

Para os municipios que trabalham com o tipo de consolidação 1 ou 3, as informações registradas nesta tela, devem ser por alíquota, deixando o campo Código de Tributação DES\-IF sem preenchimento\.  Para os tipos de consolidação 2 ou 4, as informações inseridas nesta tela devem ser discriminadas por alíquota e Código de Tributação DES\-IF\.

# <a id="_Toc37236797"></a>Layout da Tela

Tabela: mun\_manut\_desif\_0440 \(principal\)

             mun\_manut\_desif\_0440\_comp \(detalhamento do valor da compensação\) 

Dados que definem a chave de tabela principal:

     \- Código da Empresa

     \- Código do Estabelecimento

     \- Período da Apuração

     \- Alíquota

     \- Código de Tributação Desif

Dados que definem a chave de tabela de detalhamento do valor da compensação:

     \- Código da Empresa

     \- Código do Estabelecimento

     \- Período da Apuração

     \- Alíquota

     \- Código de Tributação Desif

     \- Data da Compesanção

Um registro 0440 pode ter 0 ou N registros de detalhamento do valor da compensação\.

Caso o valor de compensação seja preenchido no registro principal 0440, deve ser incluído um ou mais registros que detalhe aquele valor\.

Registro Principal 0440

Estabelecimento:                   \[  cod – razão social                                  \\/\]

Período da Apuração:            \[ MM/AAAA\]

Alíquota:                                \[             0,00\]

Cód\. Tributação DES\-IF        \[ pastinha\] \[ cod\] \[descrição\]

Vlr\. Dedução:                         \[              0,00\]

Dsc\. Dedução:                       \[                                                                                \]

Vlr\. Incentivo Fiscal:               \[             0,00\]

Dsc\. Incentivo Fiscal:             \[                                                                                \]

Vlr\. Compensação:                \[             0,00\]

Vlr ISSQN Recolhido:            \[             0,00\]

Motivo da não exigibilidade:  \[  cod \- descrição                                   \\/\]

Número do Processo da Suspensão da Exigibilidade: \[                                                   \]

Registros de Detalhamentos da Compensação:

Data da Compensação            Vlr\. Compensação

\[ DD/MM/AAAA\]                        \[                    0,00\]

\[ DD/MM/AAAA\]                        \[                    0,00\]

__Botões da barra de menu__:

Os botões do menu funcionam tanto para realizar ações de inclusão e exclusão do registro principal do 0440 quanto para os registros de detalhamento da compensação\. Caso o foco esteja nos campos da tela principal, as ações de inclusão e exclusão serão relacionadas ao registro principal\. Caso o foco esteja na parte de detalhamento, as ações de inclusão e exclusão corresponderão aos registros de detalhamento da compensação\.

NOVO

Cria um registro principal 0440 ou de detalhamento, dependedo de onde esteja o foco na tela\.

ABRE

Exibe janela de pesquisa dos registros 0440 já gravados, para que o usuário selecione <a id="OLE_LINK4"></a>o que desejar exibir em tela\.

EXCLUI

Exclui o registro principal 0440 ou de detalhamento, dependedo de onde esteja o foco na tela\.

Ao excluir o registro principal 0440, os registros de detalhamento correspondentes são automaticamente excluídos

CONFIRMA

Salva as informações tanto do registro principal 0440 quanto dos registros de detalhamento\.

RELATÓRIO

Esta opção permite imprimir os dados do registro principal 0440 e seus detalhamentos\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Toc37236798"></a>Regras de Funcionamento dos Campos

Começo neste tópico descrevendo de forma geral, como os módulos municipais funcionam\.

No Manager, o usuário seleciona no grupo dos Municipais, o módulo do município que deseja acessar\. Exemplo SÃO PAULO – FINANCEIRAS\.

A partir do módulo selecionado no manager, o sistema verifica os validadores que são relacionados ao município do módulo\. Há municípios com apenas um validador, como há também os com mais de um validador, pois ao longo do tempo um validador foi substituído por outro\.

Caso o município tenha mais de um validador, o sistema abre o módulo do município e disponibilza uma tela com os validadores, para que o usuário escolha qual irá trabalhar\.  Caso o município só tenha um validador, essa tela não é aberta\.

Os itens de menu disponível no módulo são determiandos pelo validador\. Cada validador tem seu grupo de funcionalidades e esta informação é carregada pela TFIX105 \(tabela PRT\_VALIDADOR\_MUNIC\)\. 

 

No caso da tela de Manutenção do Registro 0440 \- Demonstrativo do ISSQN mensal a recolher \(DAIR\), ela está disponível para o validador DESIF\.

Ao acessar essa tela através do menu “Manutenção 🡪 Módulo 2 🡪 Registro 0440 \- Demonstrativo do ISSQN mensal a recolher \(DAIR\)”, o sistema deve verificar se o estabelecimento foi informado no login do Manager\.

Caso o estabelecimento tenha sido informado no login e seja de um município diferente do selecionado no módulo, o sistema exibir a mensagem a seguir e não abrir a janela:

*“Este estabelecimento não pertence ao município XXXXX\-UF”*

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

<a id="_Hlk517437550"></a>Estabelecimento

Alfanumérico 

__S__

S

Listbox

Este campo é uma lista dos estabelecimentos da empresa para seleção do usuário\.

Caso o estabelecimento seja informado no login do Manager, este campo deve ser apresentado bloqueado\. 

Caso contrário, apresentar uma lista contendo todos os estabelecimentos da empresa de login, cuja UF e Município são do Município selecionado no Manager\. Exemplo, se o módulo selecionado no manager for SÃO PAULO – FINANCEIRAS, o estabelecimento apresentado na lista possui UF = SP e COD\_MUNICIPO = 30508\.

Período da Apuração

Data 

__S__

S

MM/AAAA

Apresentar o mês/ano\.

Gravar na tabela o campo DAT\_APUR com o último dia do mes/ano informado\.

Alíquota

Numérico 

__S__

S

0,00

Campo obrigatório\.

__Ao salvar o registro, executar a seguinte consistência__:

Caso o Cód\. Tributação DESIF seja preenchido, verificar se a alíquota informada nestes campo, pertence a Tabela de Códigos de Tributação do Municipio \-  DESIF \- Anexo 7 \(TACES103 \- CAD\_TRIB\_DESIF\_MUNIC\)\. 

Para isso fazer uma consulta com os critérios:

\- COD\_MUNICIPIO\_IBGE = código de 7 posições, formado pela concatenação dos campos COD\_UF \+ COD\_MUNICIPIO da tabela de Municipio\. Observação: O COD\_MUNICIPIO deve ser completado com zeros à esqueda para formar 5 posições\.  Considerar o municipio do estabelecimento selecionado na tela\.

\- COD\_TRIB\_DESIF = Código da tributação DESIF informado na tela\.

\- VALID\_INI <= último dia do mes/ano informado no Período da Apuração

\- VALID\_FIM nula 

  ou

\- VALID\_FIM >= último dia do mes/ano informado no Período da Apuração

Recuperar a ALÍQUOTA\.

Caso a alíquota informada na tela seja diferente da ALÍQUOTA recuperada na consulta, exibir a seguinte mensagem:

“Alíquota informada não corresponde a cadastrada para o Código Tributação DES\-IF, na Tabela de Códigos de Tributação do Município DESIF – Anexo 7\. Alíquota correta é xxx,xx\.”   Onde xxx,xx é a aliquota recuperada\.

Ex:

select t\.aliq

from CAD\_TRIB\_DESIF\_MUNIC t

where  t\.cod\_municipio\_ibge = '3550308'

and    t\.cod\_trib\_desif     = C

and    t\.valid\_ini         <= fdata\_ini

 and  \(\(t\.valid\_fim    is not null and t\.valid\_fim >= fdata\_ini\)OR     t\.valid\_fim    is null\) \) ; 

Cód\. Tributação DES\-IF

Alfanumérico 

__N__

S

Pastinha \+  Código \+ descrição

Origem da informação: Tabela de Códigos de Tributação DESIF \- Anexo 6 \(TACES102 \- CAD\_TRIB\_DESIF\)\. 

Ao digitar o código da tributação, e o mesmo não exitir na tabela de origem, exibir a mensagem no campo descrição:

“Código Tributação DES\-IF não cadastrado\.”

 

Vlr\. Dedução

Numérico 

N

S

0,00

Campo não obrigatório\.

Caso seja informado, habilitar o campo Descrição da Dedução\.

Caso o usuário limpe o valor digitado, desabilitar o campo Descrição da Dedução\.

Desc\. Dedução

Alfanumérico

N

S

Texto

Campo não obrigatório\.

Caso seja informado o Valor da Dedução, esse campo deve ser preenchido\.

__Ao salvar o registro, executar a seguinte consistência:__

Caso o campo Valor da Dedução esteja preenchido e o campo Descrição da Dedução não esteja preenchido, dar mensagem e não salvar o registro\.

“Descrição da Dedução é obrigatória e deve ser informada\.”

Vlr\. Incentivo Fiscal

Numérico 

N

S

0,00

Campo não obrigatório\.

Caso seja informado, habilitar o campo Descrição do Incentivo Fiscal\.

Caso o usuário limpe o valor digitado, desabilitar o campo Descrição do Incentivo Fiscal\.

Desc\. Incentivo Fiscal

Alfanumérico

N

S

Texto

Campo não obrigatório\.

Caso seja informado o Valor do Incentivo Fiscal, esse campo deve ser preenchido\.

__Ao salvar o registro, executar a seguinte consistência:__

Caso o campo Valor do Incentivo Fiscal esteja preenchido e o campo Descrição do Incentivo Fiscal não esteja preenchido, dar mensagem e não salvar o registro\.

“Descrição do Incentivo Fiscal é obrigatória e deve ser informada\.”

Vlr\. Compensação

Numérico 

N

S

0,00

Campo não obrigatório\.

__Ao salvar o registro, executar a seguinte consistência:__

Caso o campo Vlr\. Compensação esteja preenchido e NÃO exista registro de Detalhamento, dar mensagem e não salvar o registro\.

“Detalhamento da Compensação deve ser informado, pois o Valor da Compensação foi  preenchido\. Favor incluir os registros de detalhamento\.””

Caso o campo Vlr\. Compensação NÃO esteja preenchido e existam registros de Detalhamentos, dar mensagem e não salvar o registro\.

“Detalhamento da Compensação não deve ser inforamdo, pois Valor da Compensação está zerado\. Favor excluir os registros de detalhamento\.”

Caso o campo Vlr\. Compensação esteja preenchido e exista registros de Detalhamentos, mas o total do valor da compensação dos detalhamentos seja diferente do Vlr Compensação principal, dar mensagem e não salvar o registro\.

“Somatório dos Valores da Compensação dos Detalhamentos não corresponde ao Valor da Compensação informado para o registro 0440\.”

Vlr ISSQN Recolhido

Numérico 

N

S

0,00

Campo não obrigatório\.

Motivo da não exigilibilidade

Alfanumérico

N

S

Lista

Campo não obrigatório\.

Lista composta pelos valores:

1 \- Exigibilidade suspensa por decisão Judicial;  

2 \- Exigibilidade suspensa por procedimento administrativo\.

Caso escolhido um item da lista, habilitar o campo Número do Processo da Suspensção da Exigilibilidade\.

Caso o usuário o campo fique em branco, desabilitar o campo Número do Processo da Suspensção da Exigilibilidade

Número do Processo da Suspensção da Exigilibilidade

Alfanumérico

N

S

Texto

Campo não obrigatório\.

Caso seja informado o “Motivo da não exigilibilidade”, esse campo deve ser preenchido\.

__Ao salvar o registro, executar a seguinte consistência:__

Caso o campo “Motivo da não exigilibilidade” esteja preenchido e o campo “Número do Processo da Suspensção da Exigilibilidade” não esteja preenchido, dar mensagem e não salvar o registro\.

“Número do Processo da Suspensção da Exigilibilidade é obrigatório e deve ser informado\.”

= = = = = =


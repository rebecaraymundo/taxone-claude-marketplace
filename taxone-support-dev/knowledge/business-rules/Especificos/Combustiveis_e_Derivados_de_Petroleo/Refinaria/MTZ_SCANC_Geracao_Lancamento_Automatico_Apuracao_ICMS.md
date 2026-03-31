# MTZ_SCANC_Geracao_Lancamento_Automatico_Apuracao_ICMS

- **Fonte:** MTZ_SCANC_Geracao_Lancamento_Automatico_Apuracao_ICMS.docx
- **Modificado:** 2025-01-16
- **Tamanho:** 114 KB

---

THOMSON REUTERS

Módulo Combustíveis e Derivados de Petróleo

Geração dos Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST

__Localização__: Módulo Específicos, módulo Combustíveis e Derivados de Petróleo, menu Movimento de Refinaria à Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MF569804__

Liliane Videira Assaf

Criação da Geração 

11/01/2024

MFS623048

Andréa Rocha

Alteração da geração para tratar a inclusão do campo de Item da Apuração na PK da tabela\.  Inclusão do tratamento do valor negativo do lançamento e do lançamento sem valor\.

17/05/2024

MFS672382

Liliane Assaf

Tratamento do valor negativo dos quadros 1 e 2 dos Anexos VI e VI\-M na geração dos lançamentos automáticos na Apuração, considerando os Parâmetros para Lançamento de Valor Negativo \(“Item da Apuração”, “Descrição do Lançamento” e “Código do Ajuste Sped Fiscal \(E220\)”\), criados na tela de Parâmetros 🡪 Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST

15/01/2025

Sumário

[1\.	Introdução	1](#_Toc156337132)

[2\.	Parâmetros da Tela	1](#_Toc156337133)

[3\.	Críticas	1](#_Toc156337134)

[4\.	Processamento	1](#_Toc156337135)

[4\.1 – Etapa 1: Limpeza dos lançamentos gerados por esse processo nas Apurações do ICMS e do ICMS\-ST	1](#_Toc156337136)

[4\.2 \- Etapa 2: Recuperar Parametrização dos Lançamentos Automáticos e Valores dos Anexos VI e VI\-M	1](#_Toc156337137)

[4\.3 – Etapa 3: Gerar lançamento complementar	1](#_Toc156337138)

[4\.4 – Etapa 4: Recálculo dos Saldos da Apuração do ICMS e ICMS\-ST	1](#_Toc156337139)

[5\.	Relatório	1](#_Toc156337140)

# <a id="_Toc156337132"></a>Introdução

Este processo consiste em gerar os lançamentos complementares nas Apurações do ICMS\-ST e ICMS a partir dos valores gerados nos quadros 1 e 2 dos Anexos VI e VI\-M das Refinarias\.

A execução dessa geração pode ser realizada antes ou depois da Apuração do ICMS \(Localização: módulo Estadual >> ICMS, item de menu DATA MART >> Apuração do ICMS\)\.

Caso a Apuração do ICMS não tenha sido realizada antes dessa geração, é imprescindível executá\-la após esta geração, para que o Status da Obrigação seja atualizado para Situação = Apuração Realizada e Validade = Não Analisada\.

Caso a Apuração do ICMS tenha sido realizada antes dessa geração, pode apenas emitir o livro de apuração com a opção de "Recalculo dos Saldos" marcada\. Localização: módulo Estadual >> ICMS, item de menu DATA MART >> Emissão Livro Apuração\.

Obs: Apesar dessa rotina já estar fazendo o recálculo dos saldos na etapa 6, manteremos a orientação para emissão do livro de apuração após esta geração, para garantirmos que os totais fiquem corretos nos resumos da apuração do ICMS e ICMS\-ST\.

Pré\-requisito:

- Criar Calendário para a Apuração do ICMS – P9, no módulo Estadual >> Controle das Obrigações Estaduais, item de menu Obrigações>> Calendário das Obrigações >> Por Estabelecimento\.
- Parametrizar as informações para os lançamentos, disponível neste módulo, menu Parâmetros à Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST\.
- Realizar a Geração dos Anexos da Refinaria, disponível neste módulo, menu Movimento de Refinaria à Geração do Anexo VI e VI\-M

# <a id="_Toc156337133"></a>Parâmetros da Tela 

Mês/Ano Referência :                 \[ dd/aaaa \]

\[  \] Inscrição Estadual Única

Pesquisa UF \(Estabelecimento\): \[ \*Todas \*                              \\/\]

Estabelecimentos:

 \[ x \] xx \- xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx      

 \[ y \] xx \- xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx      

 \[    \] xx \- xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Funcionamento dos campos:

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

<a id="_Hlk517437550"></a>Mês/Ano Referência

Data

\(mês e ano\)

S

S

\(MM/AAAA\)

Neste campo será informado o período \(mês e ano\) para a geração dos lançamentos

Deve ser um mês válido\.

Inscrição Estadual Única

Check\-box

N

S

Default Desmarcado

O usuário escolherá essa opção caso trabalhe com inscrição estadual única\. Caso seja marcada, apenas estabelecimentos centralizadores e descentralizados são apresentados para seleção\.

Pesquisa UF \(Estabelecimento\)

Lista

S

S

Default “Todos”

Este campo é composto pelos códigos de Unidades Federativas oriundas da tabela Estado\. Adicionar à lista o item “__Todos__”\.

Servirá para filtro dos estabelecimentos apresentados para seleção\.

Estabelecimentos

Alfanumérico 

S

S

Neste campo é exibida a lista dos estabelecimentos da Empresa do login\.

Apresentar os estabelecimentos de acordo com os campos “Inscrição Estadual Única” e “Pesquisa UF \(Estabelecimento\)”\.

Se o campo Inscrição Estadual Única estiver desmarcado, apresentar todos os estabelecimentos da empresa, com UF igual a selecionada em “Pesquisa UF \(Estabelecimento\)”\.

Se o campo Inscrição Estadual Única estiver marcado, apresentar apenas os estabelecimentos Centralizadores da Parametrização da Inscrição Estadual Única e os Descentralizados, ou seja, os que não estão como centralizador nem centralizados\. Sempre obedecendo a UF selecionada em “Pesquisa UF \(Estabelecimento\)”\.

 Parametrização da Inscrição Estadual Única está disponível no módulo Controle de Obrigações Estaduais\.

Selecionar

N

N

Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos\.

O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimento”\.

Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimentos” já marcados\. 

   

Marcar todos

N

N

Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos”\.

# <a id="_Toc156337134"></a>Críticas 

Os Pré\-requisitos para a Geração dos Lançamentos nas Apurações do ICMS / ICMS\-ST são:

- Possuir um calendário para a Apuração do ICMS – P9, no módulo Estadual >> Controle das Obrigações Estaduais, item de menu Obrigações>> Calendário das Obrigações >> Por Estabelecimento, para o estabelecimento, período e código da obrigação 108 ou 165 \(de acordo com as parametrizações dos lançamentos automáticos\)\.
- Parametrizar as informações para os lançamentos, disponível neste módulo, menu Parâmetros à Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST\.
- Ter realizado a Geração dos Anexos da Refinaria, disponível neste módulo, menu Movimento de Refinaria à Geração do Anexo VI e VI\-M

Antes de iniciamos, vamos checar se esses passos foram feitos\. Caso encontre alguma falha nestas verificações, o processo será abortado\.

Parametrização dos Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST:

Verificar se existe parametrização dos Lançamentos para a Empresa e Estabelecimento foco da geração\.

Se não for encontrada parametrização, exibir a seguinte mensagem no Log da Geração:

*“Faltou realizar parametrização dos Lançamentos Automáticos para o estabelecimento\. Vide menu Parâmetros à Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST”\.*

Verificar se a Geração do Anexo VI e VI\-M foi realizada:

Verificar se a etapa de geração do Anexo VI e VI\-M foi realizada, para os anexos selecionados na tela\. Para consultar as tabelas dos quadros 1 e 2 \(CBT\_ANEXO6\_QUADR1, CBT\_ANEXO6\_QUADR2, CBT\_ANEXO6M\_QUADR1, CBT\_ANEXO6M\_QUADR2\) com os critérios abaixo:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado em tela;
- Mês/Ano Referência = Período informado em tela;

Caso nenhum registro seja encontrado, exibir mensagem de erro no Log da Geração:

*“Não foi possível realizar a geração dos lançamentos, pois não há informação nos quadros 1 e 2 dos Anexos VI e VI\-M\. *

*Certifique que a Geração dos Anexos VI e VI\-M foi executada para o período e estabelecimento”\.*

Verificar se o Calendário para Apuração do ICMS foi criado, no Módulo Controle das Obrigações Estaduais:

Verificar se existe calendário para a Apuração do ICMS – P9, para todos os Tipos de Livros \(‘108’,’165’\) que foram referenciados nas parametrizações dos Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST, para a empresa e estabelecimento em questão\.

O cadastro do Calendário das Obrigações está localizado no módulo Estadual >> Controle das Obrigações Estaduais, item de menu Obrigações>> Calendário das Obrigações >> Por Estabelecimento\.

Verificar se existe Calendário da Obrigação Fiscal por Estabelecimento \(tabela CALEND\_OBRIGACAO\), considerando os critérios: 

- Empresa de login;
- Estabelecimento informado na tela de geração;
- Data da Apuração =Último dia do período informado na tela de geração;
- Obrigação Fiscal = Tipos de Livros existentes nas parametrizações Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST, para a empresa e estabelecimento foco da geração\. Todos os tipos de livros que estiverem parametrizados, devem possuir calendário\.

Caso não encontre registro, exibir mensagem de erro no Log da Geração:

*“Não é possível realizar a geração dos lançamentos, pois não existe Calendário para a Apuração do ICMS – P9 para o estabelecimento e período informados para geração e Tipo de Livro XXX\. Favor verifique que a parametrização dos lançamentos com referência para o Livro XXX está correta \(Parâmetros >> Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST\) e crie seu calendário no módulo Estadual >> Controle das Obrigações Estaduais, menu Obrigações>> Calendário das Obrigações >> Por Estabelecimento\.”*

*Onde XXX é o Tipo de Livro existente na parametrização que não possui calendário\.*

Verificar o Status da Apuração do ICMS

Para realizar a geração dos lançamentos, caso exista Apuração do ICMS realizada para o estabelecimento, período e livro \(108 ou 165\), esta não pode estar encerrada\.

Para isso vamos consultar o Status da Obrigação Fiscal \(tabela APURACAO\), no módulo Estadual >> ICMS, item de menu Manuteção >> Status das Obrigações\. Considerar os seguintes critérios:

- Empresa de login;
- Estabelecimento informado na tela de geração;
- Data da Apuração =Último dia do período informado na tela de geração;
- Obrigação Fiscal = Tipos de Livros existentes nas parametrizações Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST, para a empresa e estabelecimento foco da geração\. 

Caso a apuração esteja com Situação = “Apuração Realizada” \(campo IND\_SITUACAO\_APUR = ‘2’\) e Validade = “Válido” \(campo IND\_VALID\_APUR = ‘2’\), então exibir mensagem de erro no Log da Geração:

*“Não é possível realizar a geração dos lançamentos, pois a Apuração do ICMS – P9 encontra\-se encerrada para o estabelecimento e período informados para geração e Tipo de Livro XXX\. Favor verifique que a parametrização dos lançamentos com referência para o Livro XXX está correta \(Parâmetros >> Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST\) e reabra a apuração, no módulo Estadual >> ICMS, menu Manutenção>> Status das Obrigações\.”*

*Onde XXX é o Tipo de Livro existente na parametrização que não possui calendário\.*

TABELA: Apuracao 

ind\_situacao\_apur 

ind\_valid\_apur

1 \- Não Apurado

2 \- Apuracao realizada

5 \- Apuracao reaberta

1 \- Não analisado

2 \- Válida

3 \- Não válida

Acontecendo qualquer erro, finalizar a geração com status = “\-1” – Erro\.

# <a id="_Toc156337135"></a>Processamento

## <a id="_Toc156337136"></a>4\.1 – Etapa 1: Limpeza dos lançamentos gerados por esse processo nas Apurações do ICMS e do ICMS\-ST 

Nesta etapa vamos eliminar os lançamentos complementares, gerados em processamentos anteriores\.

__Eliminação do Lançamento na Tabela de Lançamentos da Apuração do ICMS \(ITEM\_APURAC\_DISCR\)__

Identificar o lançamento com os critérios abaixo:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Códigos dos estabelecimentos selecionados em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = Tipos de Livros existentes nas parametrizações Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST, para a empresa e estabelecimento foco da geração\. \("108", “165”\)
- Indicador de Lançamento Digitado/calculado \(ind\_dig\_calculado\) = __‘8’__ \- lançamento gerado por esse processo

__Eliminação do Lançamento na Tabela de Lançamentos da Apuração do ICMS\-ST \(ITEM\_APURAC\_SUBST\)__

Identificar o lançamento com os critérios abaixo:

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Códigos dos estabelecimentos selecionados em tela;
- Data da Apuração = Período informado em tela;
- Código do Livro = Tipos de Livros existentes nas parametrizações Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST, para a empresa e estabelecimento foco da geração\. \("108", “165”\)
- Indicador de Lançamento Digitado/calculado \(ind\_dig\_calculado\) = __‘8’__ \- lançamento gerado por esse processo

## <a id="_5.2_-_"></a><a id="_4.2_-_"></a><a id="_Toc156337137"></a>4\.2 \- Etapa 2: Recuperar Parametrização dos Lançamentos Automáticos e Valores dos Anexos VI e VI\-M

Nessa etapa vamos recuperar as parametrizações Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST e, a partir delas, os valores dos quadros 1 e 2 dos Anexos VI e VI\-M, base para geração dos lançamentos\. Cada valor recuperado, pode gerar um ou mais lançamentos na apuração do ICMS ou ICMS\-ST\.

__\[MFS623048\] __Alteração da geração para tratar a inclusão do campo de Item da Apuração na PK da tabela, permitindo gerar mais de um lançamento para um valor do anexo\.

__Obs__\.:  Verificar que a chave da tabela de parametrização \(CBT\_PAR\_LANCTO\_P9\) foi alterada, o campo Item da Apuração foi incluído na PK\.  Então para a mesma empresa, estabelecimento, UF, anexo, quadro e item do quadro, pode existir mais de um item de apuração na tabela\. Isso permite que um valor recuperado do Anexo VI ou VI\-M possa gera um ou mais lançamentos\.

__Recuperação da Parametrização dos Lançamentos Automáticos__

__Origem dos dados__: \- Tabela de Parametrização dos Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST Consolidado da Restituição/Complemento \- CBT\_PAR\_LANCTO\_P9

__Critérios da recuperação: __

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado na tela de geração;

__Recuperação dos Valores dos Quadros 1 e 2 dos Anexos VI e VI\-M__

Para cada parametrização recuperada acima, buscar o valor nos quadros 1 ou 2 dos Anexo VI ou VI\-M:

\- Se parametrização for referente ao quadro 1 do Anexo VI, a consulta deve ser feita na tabela CBT\_ANEXO6\_QUADR1\.

  \(campos COD\_ANEXO = ‘6’ e COD\_QUADRO = ‘1’ da CBT\_PAR\_LANCTO\_P9\)

\- Se parametrização for referente ao quadro 2 do Anexo VI, a consulta deve ser feita na tabela CBT\_ANEXO6\_QUADR2\.

   \(campos COD\_ANEXO = ‘6’ e COD\_QUADRO = ‘2’ da CBT\_PAR\_LANCTO\_P9\)

\- Se parametrização for referente ao quadro 1 do Anexo VI\-M, a consulta deve ser feita na tabela CBT\_ANEXO6M\_QUADR1\.

  \(campos COD\_ANEXO = ‘6M’ e COD\_QUADRO = ‘1’ da CBT\_PAR\_LANCTO\_P9\)

\- Se parametrização for referente ao quadro 2 do Anexo VI\-M, a consulta deve ser feita na tabela CBT\_ANEXO6M\_QUADR2\.

  \(campos COD\_ANEXO = ‘6M’ e COD\_QUADRO = ‘2’ da CBT\_PAR\_LANCTO\_P9\)

__Critérios da recuperação: __

- Código Empresa = Código da empresa do login;
- Código Estabelecimento = Código do estabelecimento selecionado na tela de geração;
- Mês/Ano Referência = Período informado na tela de geração;
- UF Destinatária do Anexo igual a informada na Parametrização;
- O valor a ser recuperado do quadro, depende do campo “Item do Quadro” indicado na parametrização\. Os itens são:

__\- Anexo VI\-M Quadro 1__

1\.1\.1 \- ICMS SOBRE OPERAÇÕES POR TRIBUTAÇÃO MONOFÁSICA PRÓPRIAS E RETIDAS \(QUADRO 3\)

1\.1\.2 \- REPASSE DE ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs \(QUADRO 4\.1\.1\)

1\.1\.3 \- REPASSE DE ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS DE GÁS \(QUADRO 4\.1\.2\.\)

1\.1\.4 \- REPASSE DE ICMS DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS \(QUADRO 4\.3\)

1\.1\.5 \- REPASSE DE ICMS SOBRE BIOCOMBUSTÍVEIS DECORRENTE DE AJUSTES DE REPARTIÇÃO DE RECEITA 

\(QUADRO 6\.1\)

1\.1\.6 \- REPASSE DE ICMS SOBRE BIOCOMBUSTÍVEIS DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS \(QUADRO 6\.2\)

1\.1\.7 \- SUB\-TOTAL \(1\.1\.1 \+ 1\.1\.2\. \+ 1\.1\.3 \+ 1\.1\.4 \+ 1\.1\.5 \+ 1\.1\.6\)

1\.2\.1 \- DEDUÇÃO DE ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs A SER REPASSADO A OUTRAS UFs \(QUADRO 7\.1\.1\)

1\.2\.2 \- DEDUÇÃO DE ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS DE GÁS \(QUADRO 7\.1\.2\)

1\.2\.3 \- DEDUÇÃO DE ICMS DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS \(QUADRO 7\.3\)

1\.2\.4 \- DEDUÇÃO DE ICMS SOBRE BIOCOMBUSTÍVEIS DECORRENTE DE AJUSTES DE REPARTIÇÃO DE RECEITA \(QUADRO 9\.1\)

1\.2\.5 \- DEDUÇÃO DE ICMS SOBRE BIOCOMBUSTÍVEIS DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS \(QUADRO 9\.2\)

1\.2\.6 \- PROVISÃO PARA REPASSE POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs \(QUADRO 7\.2\)

1\.2\.7 \- PROVISÃO PARA REPASSE POR OPERAÇÕES REALIZADAS POR IMPORTADORES \(QUADRO 8\)

1\.2\.8 \- SUB\-TOTAL DAS DEDUÇÕES \(1\.2\.1 \+ 1\.2\.2 \+ 1\.2\.3 \+ 1\.2\.4 \+ 1\.2\.5 \+ 1\.2\.6 \+ 1\.2\.7\)

1\.2\.9 \- ICMS RESSARCIDO A DISTRIBUIDORAS \(QUADRO 10\)

1\.2\.10 \- ICMS RESSARCIDO A TRRs \(QUADRO 11\)

1\.2\.11 \- ICMS RESSARCIDO A IMPORTADORES \(QUADRO 12\)

1\.2\.12 \- ICMS RESSARCIDO A OUTROS CONTRIBUINTES \(QUADRO 13\)

1\.2\.13 \- SUB\-TOTAL DOS RESSARCIMENTOS \(1\.2\.9 \+ 1\.2\.10 \+ 1\.2\.11 \+ 1\.2\.12\)

1\.3 \- ICMS DEVIDO \[1\.1\.7 \- \(1\.2\.8 \+ 1\.2\.13\)

1\.3\.1 \- DEDUÇÃO TRANSFERIDA DE OUTRO ESTABELECIMENTO DO SUJEITO PASSIVO POR TRIBUTAÇÃO MONOFÁSICA \(QUADRO 14\)

1\.3\.2 \- DEDUÇÃO TRANSFERIDA PARA OUTRO ESTABELECIMENTO DO SUJEITO PASSIVO POR TRIBUTAÇÃO MONOFÁSICA \(QUADRO 15\)

1\.3\.3 \- ICMS A RECOLHER \(1\.3 \+ 1\.3\.1\) ou \(1\.3 \- 1\.3\.2\)

__\- Anexo VI\-M Quadro 2__

2\.1 \- ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs \(QUADRO 4\.2\)

2\.2 \- ICMS SOBRE OPERAÇÕES REALIZADAS POR IMPORTADORES \(QUADRO 5\)

2\.3 \- ICMS PROVISIONADO \(2\.1 \+ 2\.2\)

__\- Anexo VI Quadro 1__

1\.1\.1 \- ICMS OPERAÇÕES PRÓPRIAS E RETIDO POR SUBSTITUIÇÃO TRIBUTÁRIA \(QUADRO 3\)

1\.1\.2 \- REPASSE DE ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs \(QUADRO 4\.1\)

1\.1\.3 \- REPASSE DE ICMS DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS \(QUADRO 4\.3\)

1\.1\.4 \- REPASSE DE ICMS SOBRE AEAC OU BIODIESEL \- B100 REMETIDO A OUTRAS UFs\. \(QUADRO 6\.1\)

1\.1\.5 \- REPASSE DE ICMS SOBRE AEAC OU BIODIESEL \- B100 DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS \(QUADRO 6\.3\)

1\.1\.6 \- SUB\-TOTAL \(1\.1\.1 \+ 1\.1\.2 \+ 1\.1\.3 \+ 1\.1\.4 \+ 1\.1\.5\)

1\.2\.1 \- DEDUÇÃO DE ICMS S/OP\. REALIZADAS POR DISTRIBUIDORAS/TRRs A SER REPASSADO A OUTRAS UFs \(QUADRO 7\.1\)

1\.2\.2 \- DEDUÇÃO DE ICMS DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS \(QUADRO 7\.3\)

1\.2\.3 \- DEDUÇÃO DE ICMS SOBRE AEAC OU BIODIESEL \- B100 RECEBIDO DE OUTRAS UFs \(QUADRO 9\.1\)

1\.2\.4 \- DEDUÇÃO DE ICMS SOBRE AEAC OU BIODIESEL \- B100 DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS \(QUADRO 9\.3\)

1\.2\.5 \- PROVISÃO PARA REPASSE POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs \(QUADRO 7\.2\)

1\.2\.6 \- PROVISÃO PARA REPASSE POR OPERAÇÕES REALIZADAS POR IMPORTADORES \(QUADRO 8\)

1\.2\.7 \- PROVISÃO PARA REPASSE SOBRE AEAC OU BIODIESEL \- B100 RECEBIDO DE OUTRAS UFs \(QUADRO 9\.2\)

1\.2\.8 \- SUBTOTAL DAS DEDUÇÕES \(1\.2\.1 \+ \.\.\. \+ 1\.2\.7\)

1\.2\.9 \- ICMS RESSARCIDO A DISTRIBUIDORAS \(QUADRO 10\)

1\.2\.10 \- ICMS RESSARCIDO A TRRs \(QUADRO 11\)

1\.2\.11 \- ICMS RESSARCIDO A IMPORTADORES \(QUADRO 12\)

1\.2\.12 \- ICMS RESSARCIDO A OUTROS CONTRIBUINTES \(QUADRO 13\)

1\.2\.13 \- SUBTOTAL DOS RESSARCIMENTOS \(1\.2\.9 \+ \.\.\. \+ 1\.2\.12\)

1\.3 \- ICMS DEVIDO \[1\.1\.6 \- \(1\.2\.8 \+ 1\.2\.13\)\]

1\.3\.1 \- DEDUÇÃO TRANSFERIDA DE OUTRO ESTABELECIMENTO DO SUJEITO PASSIVO \(QUADRO 14\)

1\.3\.2 \- DEDUÇÃO TRANSFERIDA PARA OUTRO ESTABELECIMENTO DO SUJEITO PASSIVO \(QUADRO 15\)

1\.3\.3 \- ICMS A RECOLHER \(1\.3 \- 1\.3\.1\) OU \(1\.3 \+ 1\.3\.2\)

__\- Anexo VI Quadro 2__

2\.1 \- ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs \(QUADRO 4\.2\)

2\.2 \- ICMS SOBRE OPERAÇÕES REALIZADAS POR IMPORTADORES \(QUADRO 5\)

2\.3 \- ICMS SOBRE REMESSAS DE AEAC OU BIODIESEL \- B100 PARA OUTRAS UFs \(QUADRO 6\.2\)

2\.4 \- ICMS PROVISIONADO \(2\.1 \+ 2\.2 \+ 2\.3\)

<a id="Tratamento_Valor"></a>__Tratamento do Valor Negativo, Positivo e Zero:__

Aplicar o seguinte tratamento de acordo com o valor \(negativo, positivo ou zero\) recuperado do Anexo/Quadro:

- __Valor = zero__: não deve gerar o lançamento\. __\[MFS623048\]__
- Valor __positivo__: gerar o lançamento com os “Parâmetros para Lançamento de Valor Positivo” \(“Item da Apuração”, “Descrição do Lançamento” e “Código do Ajuste Sped Fiscal \(E220\)”\)\.
- Valor __negativo__:
	- Considerar o valor absoluto, ou seja, o valor recuperado será lançado sem o sinal negativo\. __\[MFS623048\]__
	- Gerar o lançamento com os “Parâmetros para Lançamento de Valor Negativo” \(“Item da Apuração”, “Descrição do Lançamento” e “Código do Ajuste Sped Fiscal \(E220\)”\)\. __\[MFS672382\]__

__\[MFS672382\]__

Se o valor for negativo e o “Item da Apuração” dos “Parâmetros para Lançamento de Valor Negativo” não estiver preenchido, então exibir a seguinte mensagem no log de erro, e não gerar o lançamento para esse valor:

*“Não foi possível realizar o lançamento na apuração para o valor XXXX do Anexo YY e Quadro Z, pois o valor é negativo e falta informação de Parâmetros para Lançamento de Valor Negativo, na parametrização dos Lançamentos Automáticos para o estabelecimento\. Vide menu Parâmetros à Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST”\.*

Onde:

XXXX : substituir pelo campo “Item do Quadro” da parametrização dos lançamentos\. Exemplo 1\.1\.1, 2\.1\.

YY: substituir pelo campo “Anexo” da parametrização dos lançamentos\. Exemplo Anexo VI, Anexo VI\-M

Z: substituir pelo campo “Quadro” da parametrização dos lançamentos\. Exemplo Quadro 1, Quadro2\.

*Exemplo de mensagem: “Não foi possível realizar o lançamento na apuração para o valor *__*1\.2\.10*__* do Anexo *__*VI *__*e Quadro *__*1*__*, pois o valor é negativo e falta informação de Parâmetros para Lançamento de Valor Negativo, na parametrização dos Lançamentos Automáticos para o estabelecimento\. Vide menu Parâmetros à Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST”*

As parametrizações para lançamento de valores positivos e negativos estão disponíveis neste módulo, menu Parâmetros à Lançamentos Automáticos na Apuração do ICMS/ICMS\-ST\.

## <a id="_5.3_–_Etapa"></a><a id="_4.3_–_Etapa"></a><a id="_Toc156337138"></a>4\.3 – Etapa 3: Gerar lançamento complementar

__Gravação da Tabela de Status da Obrigação \(APURACAO\)__

Antes de gravar o primeiro lançamento complementar de um determinado tipo de livro \(‘108’ ou ‘165’\), verificar se existe registro de Status da Obrigação Fiscal \(tabela APURACAO\), no módulo Estadual >> ICMS, item de menu Manutenção >> Status das Obrigações\. Considerar os seguintes critérios:

- Empresa de login;
- Estabelecimento informado na tela de geração;
- Data da Apuração =Último dia do período informado na tela de geração;
- Obrigação Fiscal = Tipo de Livro da parametrização do Lançamento Automático na Apuração do ICMS/ICMS\-ST \(‘108’ ou ‘165’\)\.

Caso não exista registro, criar um registro na tabela APURAÇÃO para aquela Obrigação Fiscal\.

Veja a seguir o preenchimento dos campos na tabela APURAÇÃO\. Os campos sinalizados com asterisco compõem a chave da tabela\.

__PK__

__Campo__

__Nome na tabela__

__Regra de preenchimento__

__\*\*\*__

__Código da empresa__

COD\_EMPRESA

Código da empresa do login\.

__\*\*\*__

__Código do estabelecimento__

COD\_ESTAB

Código do estabelecimento selecionado em tela\.

__\*\*\*__

__Data da Apuração__

DAT\_APURACAO

Úlitmo dia do mes e ano do Período da informado na tela de geração\.

__\*\*\*__

__Código do Livro __

COD\_TIPO\_LIVRO

Gravar o Tipo de Livro da parametrização do Lançamento Automático na Apuração do ICMS/ICMS\-ST\.

Situação

IND\_SITUACAO\_APUR

Preencher com ‘1’ – Não Apurado

Validade

IND\_VALID\_APUR

Preencher com ‘1’ – Não Analisado

Data da Realização

DAT\_REALIZACAO

Data da execução da geração\.

Este passo é necessário quando a geração da Apuração do ICMS não foi realizada antes desta geração\. O registro deve ser criado na tabela de Apuração para que os lançamentos possam ser realizados\.

__Gravação do Lançamento na Tabela de Lançamentos da Apuração do ICMS \(ITEM\_APURAC\_DISCR\)__

Se o Indicador da Apuração da parametrização do Lançamento Automático na Apuração do ICMS/ICMS\-ST for igual a ‘0’ – Apuração Própria \(ICMS\) gravar o lançamento no Resumo da Apuração do ICMS – Tabela ITEM\_APURAC\_DISCR, conforme preenchimento abaixo\. Os campos sinalizados com asterisco compõem a chave da tabela\.

__PK__

__Campo__

__Nome na tabela__

__Regra de preenchimento__

__\*\*\*__

__Código da empresa__

COD\_EMPRESA

Código da empresa do login\.

__\*\*\*__

__Código do estabelecimento__

COD\_ESTAB

Código do estabelecimento selecionado em tela\.

__\*\*\*__

__Data da Apuração__

DAT\_APURACAO

Úlitmo dia do mês e ano do Período da informado na tela de geração\.

__\*\*\*__

__Código do Livro __

COD\_TIPO\_LIVRO

Tipo de Livro da parametrização do Lançamento Automático na Apuração do ICMS/ICMS\-ST

__\*\*\*__

__Operação da Apuração__

COD\_OPER\_APUR

“Item da Apuração” da parametrização do Lançamento Automático na Apuração do ICMS/ICMS\-ST\.

__\[MFS672382\]__

Ver “[__Tratamento do Valor Negativo, Positivo e Zero__](#Tratamento_Valor)” do tópico 4\.2, para definição do uso da parametrização de acordo com o valor sendo positivo ou negativo\.

__\*\*\*__

__Número do Lançamento__

NUM\_DISCRIMINACAO

Sequencial único por Operação da Apuração \(COD\_OPER\_APUR\)\. 

Ou seja, recuperar o próximo número da seguência de lançamentos da Operação da Apuração que está sendo gravada, considerando a empresa, estabelecimento, data da apuração, código do livro e a operação da apuração\.

__Valor do Lançamento__

VAL\_ITEM\_DISCRIM

Valor recuperado do quadro 1 ou 2 do Anexo VI ou VI\-M, especificado no campo “Item do Quadro” da parametrização do Lançamento Automático na Apuração do ICMS/ICMS\-ST\.

__Obs__\.: Quando o valor recuperado for negativo, deve\-se considerar o valor absoluto, ou seja, o valor recuperado será gravado sem o sinal negativo\.  

Quando o valor do lançamento for igual a zero, o registro não deve ser gerado\.

__Descrição do Lançamento__

DSC\_ITEM\_APURACAO

“Descrição do Lançamento” da parametrização do Lançamento Automático na Apuração do ICMS/ICMS\-ST\.

__\[MFS672382\]__

Ver “[__Tratamento do Valor Negativo, Positivo e Zero__](#Tratamento_Valor)” do tópico 4\.2, para definição do uso da parametrização de acordo com o valor sendo positivo ou negativo\.

__Código do Ajuste ICMS__

COD\_AJUSTE\_ICMS

“Código de Ajuste Sped Fiscal \(E220\)” da parametrização do Lançamento Automático na Apuração do ICMS/ICMS\-ST\.

__\[MFS672382\]__

Ver “[__Tratamento do Valor Negativo, Positivo e Zero__](#Tratamento_Valor)” do tópico 4\.2, para definição do uso da parametrização de acordo com o valor sendo positivo ou negativo\.

__Indicador do Tipo do Lançamento__

IND\_TIPO\_LANC

Gravar com __“3”\.__

Este valor signfica que o lançamento não possui documentos associados\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “8”\.

__8 __– identifica os lançamentos gerados por esse processo\.

Demais campos não mencionados não precisam ser preenchidos

__Gravação do Lançamento na Tabela de Lançamentos da Apuração do ICMS\-ST \(ITEM\_APURAC\_SUBST\)__

Se o Indicador da Apuração da parametrização do Lançamento Automático na Apuração do ICMS/ICMS\-ST for igual a ‘1’ – Apuração do ICMS\-ST gravar o lançamento no Resumo Principal do ICMS\-ST \(p/ UF = UF estab\) ou os Resumo das Entradas e Saídas do ICMS\-ST \(p/ UF <> UF estab\)  – Tabela ITEM\_APURAC\_SUBST, conforme preenchimento abaixo\. Os campos sinalizados com asterisco compõem a chave da tabela\.

__PK__

__Campo__

__Nome na tabela__

__Regra de preenchimento__

__\*\*\*__

__Código da empresa__

COD\_EMPRESA

Código da empresa do login\.

__\*\*\*__

__Código do estabelecimento__

COD\_ESTAB

Código do estabelecimento selecionado em tela\.

__\*\*\*__

__Data da Apuração__

DAT\_APURACAO

Úlitmo dia do mes e ano do Período da informado na tela de geração\.

__\*\*\*__

__Código do Livro __

COD\_TIPO\_LIVRO

Tipo de Livro da parametrização do Lançamento Automático na Apuração do ICMS/ICMS\-ST

__\*\*\*__

__Identificador do Estado__

IDENT\_ESTADO

UF Destinatária do Anexo presente na parametrização do Lançamento Automático na Apuração do ICMS/ICMS\-ST;

__\*\*\*__

__Indicador da UF__

IND\_UF

Se UF Destinatária do Anexo for igual a UF do Estabelecimento então:

    Preencher com ‘1’;

Se UF Destinatária do Anexo for diferente da UF do Estabelecimento então:

    Preencher com ‘2’;

__\*\*\*__

__Operação da Apuração__

COD\_OPER\_APUR

“Item da Apuração” da parametrização do Lançamento Automático na Apuração do ICMS/ICMS\-ST\.

__\[MFS672382\]__

Ver “[__Tratamento do Valor Negativo, Positivo e Zero__](#Tratamento_Valor)” do tópico 4\.2, para definição do uso da parametrização de acordo com o valor sendo positivo ou negativo\.

__\*\*\*__

__Número do Lançamento__

NUM\_DISCRIMINACAO

Sequencial único por Operação da Apuração \(COD\_OPER\_APUR\)\. 

Ou seja, recuperar o próximo número da seguencia de lançamentos da Operação da Apuração que está sendo gravada, considerando a empresa, estabelecimento, data da apuração, código do livro, identificador do Estado \(ident\_estado\), Indicador da UF \(ind\_uf\) e a operação da apuração\.

__Valor do Lançamento__

VAL\_ITEM\_DISCRIM

Valor recuperado do quadro 1 ou 2 do Anexo VI ou VI\-M, especificado no campo “Item do Quadro” da parametrização do Lançamento Automático na Apuração do ICMS/ICMS\-ST\.

__Obs__\.: Quando o valor recuperado for negativo, deve\-se considerar o valor absoluto, ou seja, o valor recuperado será gravado sem o sinal negativo\.

Quando o valor do lançamento for igual a zero, o registro não deve ser gerado\.

__Descrição do Lançamento__

DSC\_ITEM\_APURACAO

“Descrição do Lançamento” da parametrização do Lançamento Automático na Apuração do ICMS/ICMS\-ST\.

__\[MFS672382\]__

Ver “[__Tratamento do Valor Negativo, Positivo e Zero__](#Tratamento_Valor)” do tópico 4\.2, para definição do uso da parametrização de acordo com o valor sendo positivo ou negativo\.

__Código do Ajuste ICMS__

COD\_AJUSTE\_ICMS

“Código de Ajuste Sped Fiscal \(E220\)” da parametrização do Lançamento Automático na Apuração do ICMS/ICMS\-ST\.

__\[MFS672382\]__

Ver “[__Tratamento do Valor Negativo, Positivo e Zero__](#Tratamento_Valor)” do tópico 4\.2, para definição do uso da parametrização de acordo com o valor sendo positivo ou negativo\.

__Indicador do Tipo do Lançamento__

IND\_TIPO\_LANC

Gravar com __“3”\.__

Este valor signfica que o lançamento não possui documentos associados\.

__Indicador de Lançamento Digitado/calculado__

IND\_DIG\_CALCULADO

Gravar com “8”\.

__8 __– identifica os lançamentos gerados por esse processo

Demais campos não mencionados não precisam ser preenchidos

## <a id="_4.5_–_Etapa"></a><a id="_Toc156337139"></a>4\.4 – Etapa 4: Recálculo dos Saldos da Apuração do ICMS e ICMS\-ST

Nesse passo os subtotais e totais das Apurações do ICMS e ICMS\-ST são recalculados para considerar os valores dos lançamentos complementares realizados nas etapas anteriores\.

Sendo assim não é necessário após a execução dessa geração, realizar a Apuração do ICMS novamente ou a Emissão do Livro de Apuração com opção de “Recálculo dos Saldos” marcada\. Os totais da apuração já estarão atualizados ao final desta geração\.

Chamar a procedure SAF\_ICMS\_CALC\_SLD para os Tipo de Livros da parametrização do Lançamento Automático na Apuração do ICMS/ICMS\-ST \(‘108’, ‘165’\) que tiveram lançamentos gerados\.

# <a id="_Toc156337140"></a>Relatório

Gerar um arquivo excel a partir da leitura das tabelas onde foram gerados os lançamentos complementares __ITEM\_APURAC\_DISCR e ITEM\_APURAC\_SUBST__

Nome do arquivo: Relatório\_Conferencia\_Lancamentos\_mm\_aaaa\_cod\_estab\.xlsx

O relatório deve demonstrar os lançamentos que foram gerados nas Apurações do ICMS e ICMS\-ST por esse processo:

Layout do Relatório:

__Campos__

__Regra de Preenchimento__

Código da empresa

Código da empresa do login\.

Código do estabelecimento

Código do estabelecimento selecionado em tela\.

Data da Apuração

Úlitmo dia do mês e ano do Período da informado na tela de geração\.

Código do Livro

Código do Livro da Apuração do ICMS \(__ITEM\_APURAC\_DISCR\- COD\_TIPO\_LIVRO\) __ou da Apuração do ICMS\-ST \(__ITEM\_APURAC\_SUBST – COD\_TIPO\_LIVRO\)\.__

Apuração

Para o lançamento realizado na Apuração do ICMS \(__ITEM\_APURAC\_DISCR\):__

   Preencher com “ICMS”

Para o lançamento realizado na Apuração do ICMS\-ST \(__ITEM\_APURAC\_SUBST\):__

   Preencher com “ICMS\-ST”

UF da Apuração 

Para o lançamento realizado na Apuração do ICMS \(__ITEM\_APURAC\_DISCR\):__

   Preencher com a UF do Estabelecimento

Para o lançamento realizado na Apuração do ICMS\-ST \(__ITEM\_APURAC\_SUBST\):__

   Preencher com a UF do Lançamento \(__COD\_ESTADO referente ao IDENT\_ESTADO \-__ __ITEM\_APURAC\_SUBST\)__

Item da Apuração \(cod\-desc\)

Código \+ Descrição da Operação da Apuração da Apuração do ICMS \(__ITEM\_APURAC\_DISCR\- COD\_OPER\_APUR\) __ou da Apuração do ICMS\-ST \(__ITEM\_APURAC\_SUBST \- COD\_OPER\_APUR\)\.__

Para recuperar a descrição, consultar a tabela OPERACAO\_APURACAO considerando o código do livro \(108, 165\) e o código da operação\.

Exemplo: 002 \- OUTROS DEBITOS \(DISCRIMINAR ABAIXO\)

Descrição do Lançamento

Descrição do Lançamento da Apuração do ICMS \(__ITEM\_APURAC\_DISCR\- DSC\_ITEM\_APURACAO\) __ou da Apuração do ICMS\-ST \(__ITEM\_APURAC\_SUBST \- DSC\_ITEM\_APURACAO\)\.__

Código do Ajuste Sped Fiscal

Código do Ajuste ICMS da Apuração do ICMS \(__ITEM\_APURAC\_DISCR\- COD\_AJUSTE\_ICMS\) __ou da Apuração do ICMS\-ST \(__ITEM\_APURAC\_SUBST \- COD\_AJUSTE\_ICMS\)\.__

Valor do Lançamento

Valor do Lançamento da Apuração do ICMS \(__ITEM\_APURAC\_DISCR\- VAL\_ITEM\_DISCRIM\) __ou da Apuração do ICMS\-ST \(__ITEM\_APURAC\_SUBST \- VAL\_ITEM\_DISCRIM\)\.__

= = = = = =


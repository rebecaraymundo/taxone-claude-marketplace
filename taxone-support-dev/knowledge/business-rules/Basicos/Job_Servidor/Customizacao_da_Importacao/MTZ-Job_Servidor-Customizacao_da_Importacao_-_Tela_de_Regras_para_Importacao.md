# MTZ-Job Servidor-Customizacao da Importacao - Tela de Regras para Importacao

- **Fonte:** MTZ-Job Servidor-Customizacao da Importacao - Tela de Regras para Importacao.docx
- **Modificado:** 2022-03-07
- **Tamanho:** 91 KB

---

THOMSON REUTERS

Módulo Básicos \- Job Servidor

Tela de Regras para Importação

__Localização__: Menu Básicos, módulo Job Servidor, menu Importação <a id="OLE_LINK28"></a><a id="OLE_LINK32"></a>🡪 Customização da Importação 🡪 Regras para Importação

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS30481

Liliane Assaf

Criação da tela de cadastro das regras de preenchimento de campos SAFX\.

Esta MFS compõe a solução do atendimento a demanda que cria regras para preenchimento de campos da SAFX, que não vem preenchidos pela interface\. Os campos que possuem regras definidas, serão preenchidos no momento da importação através da execução das regras\.

08/10/2019

Sumário

[1\.	Introdução	2](#_Toc23871234)

[2\.	Regras Gerais	3](#_Toc23871235)

[3\.	Layout da Tela	4](#_Toc23871236)

[4\.	Fluxo de Operação da Tela Principal	5](#_Toc23871237)

[5\.	Fluxo de Operação da Tela Modal de Regras para Importação	7](#_Toc23871238)

[6\.	Regras dos Campos da Tela Principal	7](#_Toc23871239)

[7\.	Regras dos Campos da Tela Modal de Preenchimento de Regras	9](#_Toc23871240)

[8\.	Consistências:	9](#_Toc23871241)

[7\.1 – Validação ao Salvar registro de Regra da Importação:	9](#_Toc23871242)

[7\.2 – Validação da Regra da Importação:	10](#_Toc23871243)

[9\.	Exemplos de Regras de Preenchimento:	13](#_Toc23871244)

# <a id="_Toc23871234"></a>Introdução

Muitos clientes DW criam processos customizados para completarem o preenchimento de campos da SAFX, visto que a informação não é extraída do sistema de origem\.

Com o advindo do TAX ONE os processos customizados não podem mais ser utilizados, visto que a base de dados é mantida pela Thomson Reuters\. 

Desta forma, para continuar permitindo o preenchimento dos campos que não são carregados via interface, estamos propondo uma solução onde é possível criar regras de preenchimentos de campos da SAFX a serem executadas no momento da importação\.

__Processo de Customizado da Importação__

Disponibilizado novo __Processo de Customizado da Importação__, onde é possível definir regras de preenchimentos de campos de tabelas SAFX’s, para execução em momento da importação\.  

Com esse processo é possível preencher campos nas tabelas SAFX’s cujas informações não são extraídas via interface\.

O Processo Customizado da Importação é composto pelas seguintes funcionalidades:

- Tela de Cadastro das Listas Pré\-definidas de Valores \(ainda não disponível\);
- Tela de Cadastro de Regras para Importação;
- Importação Online;
- Importação Batch, via tabela SAFX\.

Através da tela de Cadastro de Regras para Importação, é possível definir as regras de preenchimento de campos das tabelas SAFX’s\.

As regras são executadas e os campos da tabela SAFX são preenchidos durante a execução das Importações Online e Batch, sendo que a última apenas para opção via Tabela SAFX\. 

O Processo Customizado da Importação não se aplica à Importação Batch pela opção de leitura do Arquivo TXT\.

__Procedimentos__:

Na Tela de Cadastro de Regras para Importação, criar a regra de preenchido de um campo de uma SAFX\.

Depois executar a carga da tabela SAFX, via processo de Carga do Job Servidor\.

Programar e executar a Importação \(Online ou Batch via tabela SAFX\)\.

Conferir se campo foi carregado na tabela definitiva de acordo com a regra definida\.

# <a id="_Toc23871235"></a>Regras Gerais

Este documento matriz tem como objetivo definir o funcionamento da Tela de Cadastro das Regras de Preenchimento\.  

Nesta tela será possível acessar a tabela SAFX, visualizar os campos que a compõe e criar regras de preenchimentos para os campos\. 

A regra escrita numa uma pseudolinguagem baseada em PL\-SQL, não permitindo algumas palavras chaves como “DELETE”, “UPDATE”, “COMMIT”, “DROP”\. 

A regra é validada no momento da sua criação, evitando erro em sua execução durante o processo de importação da SAFX\.

As regras são executadas de acordo com a ordem de execução definida em tela\.  Logo é importante dar atenção a esta definição, principalmente quando existe dependência entre regras, ou seja, uma regra faz referência à campos que possuem regras\.  

Exemplo:

Regra de Preenchimento do Campo A:  IF Campo B is null THEN  Return 1 END IF;

Regra de Preenchimento do Campo B:  IF Campo C is null THEN  Return 2 END IF;

A regra do campo B deve ser executa antes da regra do campo A\.

 

# <a id="_Toc23871236"></a>Layout da Tela

__Tela Principal__

Tabela:   \[ SAFX01        \[\\/\]\]

 Nome:   \[ Lançamentos Contabeis\]  

 Exibir apenas campos com regra \[ x \]

Campos da Tabela: 

__|Item| Obrigatório| Descrição 		     | Nome do Campo    | Tamanho	| Tipo|Ordem|Sobrepõe|Regra       |   Ações__

| 1     |  Sim	      | Código da Empresa	     | COD\_EMPRESA     | 003	| A      |2         |Sim	     |                 |  \[Editar\] \[Limpar\]

| 2     |  Sim	      | Código do Estabelecimento| COD\_ESTAB	    | 006	| A      |1         |Não	     |                 |  \[Editar\] \[Limpar\]

| 3     |  Sim	      | Data da Operação	     | DATA\_OPERACAO| 008		| N      |3         |Não	     |                 |  \[Editar\] \[Limpar\]

__Tela Modal de Regra para Importação__:

Nome do Campo: COD\_EMPRESA

Descrição:            Código da Empresa

Descrição da Regra:

  IF CAMPO\(COD\_ESTAB\) = ‘0001’ THEN RETURN ‘076’ END IF; 

  IF CAMPO\(COD\_ESTAB\) = ‘0002’ THEN RETURN ‘077’ END IF;

Deseja que o resultado da execução da regra sobreponha o conteúdo do campo gravado via carga da SAFX? \[Não \[\\/\]\]

                                                                           \[Ok\]                          \[Cancela\]

__Tabelas Envolvidas:__

Leitura:     CAT\_PRIOR\_IMP; CAT\_LAYOUT\_IMP

Gravação: CAD\_IMP\_REGRA

__Botões da barra de menu__:

CONFIRMA

Opção para salvar as regras na tabela CAD\_IMP\_REGRA\.

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Fluxo_de_Operação"></a><a id="_Toc23871237"></a>Fluxo de Operação da Tela Principal

__Fluxo Principal:__

__Passo__

__Acionador__

__Descrição__

1

Usuário

Usuário seleciona o item de menu Importação >> Customização da Importação >> Regras para Importação

2

Sistema

Abre a janela com todos os campos em branco\.

3

Usuário

Seleciona uma tabela SAFX na lista disponível no campo “Tabela”

4

Sistema

Preenche automaticamente o campo “Nome” e os campos Item, Obrigatório, Descrição, Nome do Campo, Tamanho e Tipo da grid “Campos da Tabela” – todos desabilitados\.

Caso o item já tenha regra gravada, apresenta também os campos Ordem \(habilitado\), Sobrepõe \(desabilitado\) e Regra \(desabilitado\) preenchidos\.

Habilita os botões “Editar”, “Limpar”\.

__Fluxo Para Editar Regra:__

__Passo__

__Acionador__

__Descrição__

4

Partir do passo 4 do fluxo Principal\.

5

Usuário

Seleciona o botão “Editar”

6

Sistema

Abre a tela Modal de Regra para Importação\. 

Ir para o tópico 4 – Fluxo de Operação da Tela Modal de Regra para Importação\.

7

Usuário

Retorna para a Tela Principal

8

Sistema 

Atualiza os campos “Sobrepõe” e “Regra” da grid “Campos da Tabela”, com os dados orinudos da Tela Modal de Regra para Importação\.

9

Usuário

Preenche o campo “Ordem” da grid “Campos da Tabela”\.

10

Usuário

Clica no botao Confirma do menu da janela

11

Sistema

Sistema valida os dados antes de salvar na tabela de destino\.

Vide tópico [7\.1 \- Validação ao Salvar registro de Regra da Importação](#_7.1_–_Validação)\.

12

Sistema

Salva as informações de Ordem, Sobrepõe e Regra de todos os itens da grid “Campos da Tabela” na tabela destino \(CAD\_IMP\_REGRA\)\.

Exibe mensagem padrão que os dados forma gravados com sucesso\.

__Fluxo Para Limpar Regra:__

__Passo__

__Acionador__

__Descrição__

4

Partir do passo 4 do fluxo Principal\.

5

Usuário

Seleciona o botão “Limpar”

6

Sistema 

Apresenta mensagem padrão de confirmação\.

7

Usuário

Confirma exclusão\.

8

Sistema

Limpa os campos “Ordem”, “Sobrepõe” e “Regra” da grid “Campos da Tabela”\.

9

Sistema

Deleta item registrado na tabela destino \(CAD\_IMP\_REGRA\)\.

__Fluxos alternativos__:

__Passo__

__Acionador__

__Descrição__

1

Usuário

Seleciona uma outra tabela SAFX na lista diponível no campo “Tabela”

2

Sistema

Caso as regras da grid “Campos da Tabela” não tenham sido salvas, exibir mensagem padrão que indica que os dados não foram salvos e pergunta se deseja salvar as informações\.

__Passo__

__Acionador__

__Descrição__

1

Usuário

Seleciona o botão do menu __Fecha__\.

2

Sistema

Caso as regras da grid “Campos da Tabela” não tenham sido salvas, exibir mensagem padrão que indica que os dados não foram salvos e pergunta se  deseja salvar as informações\.

__Passo__

__Acionador__

__Descrição__

1

Usuário

Seleciona o botão Limpar\.

2

Sistema

Caso o item da grid “Campos da Tabela” ainda NÃO tenha o campo “Regra” preenchido, exibir a seguinte mensagem:

                                        “Não existe regra a ser excluída\.”

# <a id="_Fluxo_de_Operação_1"></a><a id="_Toc23871238"></a>Fluxo de Operação da Tela Modal de Regras para Importação

__Passo__

__Acionador__

__Descrição__

1

Usuário

Na tela principal, o usuário seleciona o botão “Editar”

2

Sistema 

Abre a tela Modal de Regra para Importação\. 

Preenche automaticamente os campos Nome do Campo e Descrição, mantendo\-os desabilitados\.

3

Usuário

Preenche o campo “Descrição da Regra”\.

4

Usuário

Seleciona o botão Ok 

5

Sistema

Aplicar a lógica de validação da regra\.

Vide tópico [7\.2 – Validação da Regra da Importação](#_7.2_–_Validação)\.

6

Sistema

Caso a regra esteja válida, então:

   Tela modal é fechada e volta para a tela principal\.

Caso a regra esteja inválida, então:

   Exibir pop\-up com mensagem de erro retornada pela rotina de Validação da Regra\.

   Manter a tela modal aberta\.

# <a id="_Toc524527073"></a><a id="_Hlk21544161"></a><a id="_Toc23871239"></a>Regras dos Campos da Tela Principal

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

Tabela

Alfanumérico

__S__

S

Lista com os nomes das tabelas SAFX do Catálogo Prioridade de Importação \(TFIX11\)\.

Este campo serve como filtro para recuperação dos registros a serem apresentados na grid “Campos da Tabela”\.

Tabela Origem: CAT\_PRIOR\_IMP

Campo: NOM\_TAB\_WORK

<a id="_Hlk517192821"></a>Nome

Alfanumérico

__S__

N

Após a seleção da tabela, este campo deve apresentar o nome descritivo da SAFX\. 

Tabela Origem: CAT\_PRIOR\_IMP

Campo: DESCRICAO\_ARQUIVO\.

Exibir apenas campos com regra

Alfanumérico

__N__

S

Check\-box

Caso o campo seja selecionado, são exibidos apenas os campos que possuam regra preenchida, na grid Campos da Tabela\.

Caso contrário, todos os campos da tabela são exibidos\.

__Campos da Tabela__

__Grid__

__Após seleção da tabela, a grid apresenta o conjunto de campos da SAFX, oriundos do Cadastro de Layout SAFX \(TFIX96\)__

__Tabela Origem: CAT\_LAYOUT\_IMP__

__Atenção: __

__Pedro orientou utilizar DATAWINDOW TABULAR para possibilitar conversão do TAX ONE\.__

Item

Alfanumérico

__S__

N

Tabela Origem: CAT\_LAYOUT\_IMP

Campo: NUM\_CAMPO

Obrigatório

Alfanumérico

__S__

N

Tabela Origem: CAT\_LAYOUT\_IMP

Campo: IND\_OBRIG

Se “S”, apresentar “Sim”

Se “N”, apresentar “Não”

Descrição

Alfanumérico

__S__

N

Tabela Origem: CAT\_LAYOUT\_IMP

Campo: DESCRICAO

Nome do Campo

Alfanumérico

__S__

N

Tabela Origem: CAT\_LAYOUT\_IMP

Campo: NOME\_CAMPO

Tamanho

Alfanumérico

__S__

N

Tabela Origem: CAT\_LAYOUT\_IMP

Campo: TAMANHO

Tipo

Alfanumérico

__S__

N

Tabela Origem: CAT\_LAYOUT\_IMP

Campo: TIPO

Ordem

Numérico

__S__

S

Campo habilitado para preenchimento da ordem de execução das regras\.

Tabela destino: CAD\_IMP\_REGRA

Campo destino: NUM\_ORDEM

Sobrepõe

Alfanumérico

__S__

N

Este fica desabilitado, pois o usuário informa seu valor na “Tela Modal de Regra para Importação”

Tabela destino: CAD\_IMP\_REGRA

Campo destino: IND\_SOBREPOE

Regra

Alfanumérico

__S__

N

Este fica desabilitado, pois o usuário informa seu conteúdo na “Tela Modal de Regra para Importação”

Tabela destino: CAD\_IMP\_REGRA

Campo destino: DSC\_REGRA

OBS: como esse campo é grande podemos apresentar apenas uma parte do conteúdo gravado no campo DSC\_REGRA\.

# <a id="_Toc23871240"></a>Regras dos Campos da Tela Modal de Preenchimento de Regras

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

Nome do Campo

Alfanumérico

__S__

N

Tabela Origem: CAT\_LAYOUT\_IMP

Campo: NOME\_CAMPO

Descrição

Alfanumérico

__S__

N

Tabela Origem: CAT\_LAYOUT\_IMP

Campo: DESCRICAO

Descrição da Regra

Alfanumérico

__S__

S

Campo texto de 4000 posições\.

Campo utilizado para o preenchimento da regra\.

Ver tópico [7\.2 – Validação da Regra da Importação](#_7.2_–_Validação)

Tabela destino: CAD\_IMP\_REGRA

Campo destino: DSC\_REGRA

Deseja que o resultado da execução da regra sobreponha o conteúdo do campo gravado via carga da SAFX?

Alfanumérico

__S__

S

__Não__

Lista com os valores:

S – Sim

N – Não

Tabela destino: CAD\_IMP\_REGRA

Campo destino: IND\_SOBREPOE

# <a id="_Toc23871241"></a>Consistências: 

## <a id="_7.1_–_Validação"></a><a id="_Toc23871242"></a>7\.1 – Validação ao Salvar registro de Regra da Importação:

A tela não permite que o número de Ordem se repita em mais de um item da grid “Campos da Tabela”\. 

Caso existam repetições, exibir a seguinte mensagem:

“Existem itens com mesmo número do ordem\.  Favor ajustar as ordens para que não se repitam\.”

Se um dos três campos for preenchido, Ordem, Sobrepõe ou Regra, todos os três devem ser preenchidos\.

Caso um item da grid “Campos da Tabela” possua o campo Ordem preenchido e o campos Sobrepõe e Regra não preenchidos, exibir a mensagem:

	“Exitem itens com campo Ordem preenchidos mas sem Regra especificada\. Favor adicionar Regra\.”

Caso um item da grid “Campos da Tabela” possua os campos Sobrepõe e Regra preenchidos e o campo Ordem não preenchido, exibir a mensagem:

	“Existem itens com campo Regra preenchidos mas sem Ordem especificada\. Favor adicionar Ordem\.”

Qualquer erro acima impede que todos os registros sejam salvos\.

__   __

Voltar para:

[Fluxo de Operação da Tela Principal](#_Fluxo_de_Operação)

## <a id="_7.2_–_Validação"></a><a id="_Toc23871243"></a>7\.2 – Validação da Regra da Importação:

Para validar a regra, chamar a execução da função __validar\_instrucao__ da package __pkg\_imp\_custom__:

pkg\_imp\_custom\.validar\_instrucao \(p\_tabela       in varchar2,

                         p\_coluna      in varchar2,

                         p\_instrucao  in varchar2,

                         p\_mens\_erro  out varchar2,

                         p\_cod\_erro   out PLS\_INTEGER\);

Passar como parâmetros:

- p\_tabela    = nome da tabela \(Tabela Origem: CAT\_PRIOR\_IMP \- Campo: NOM\_TAB\_WORK\)
- p\_coluna    = nome do campo \(Tabela Origem: CAT\_LAYOUT\_IMP \- Campo: NOME\_CAMPO\)
- p\_instrucao  = conteúdo da regra a ser validada

A execução da rotina retorna os seguintes parâmetros:

- p\_cod\_erro   

= \-1 \- regra inválida, 

=  0  \- regra válida

- p\_mens\_erro   

Caso a rotina de validação retorne que a regra está inválida \(P\_COD\_ERRO = \-1\), então este parâmetro retorna a mensagem de erro\.

A mensagem pode ser a do próprio Oracle, caso a o problema seja na execução da regra\. 

Caso o erro seja porque a regra contém palavras reservadas, a mensagem será: 

 “Instrução não validada, pois, contém palavra\(s\) reservada\(s\)\.’

Voltar para: 

[Fluxo de Operação da Tela Modal de Regras para Importação](#_Fluxo_de_Operação_1)

__Orientações para Montagem da Regra __

As regras só poderão referenciar à campos da própria tabela SAFX, não havendo a possibilidade de referenciar campos em outras tabelas\.

O tamanho máximo da regra é 4000 caracteres\.

Como as regras são aplicadas aos campos das tabelas SAFX’s, atentar\-se aos formatos dos valores manipulados nas regras:

- O conteúdo do campo lido está no formato definido no Manual de Layout Mastersaf DW;
- O conteúdo do campo retornado pela regra deve estar no formato definido no Manual de Layout Mastersaf DW;

       Segundo o Manual de Layout:

- Campos do tipo data no formato AAAAMMDD;
- Campos do tipo numérico com decimais: para identificar a parte inteira e a decimal não são usados pontos nem vírgulas, mas sim o número de casas decimais é preenchido de forma a completar seu tamanho\.

__Linguagem:__

A regra deve ser escrita em linguagem PL\-SQL, com algumas restrições como uso de LOOP, comandos como DELETE, INSERT, SELECT\. Expressões condicionais, operadores lógicos, aritméticos, funções de conversão podem ser aplicadas\. Veja:

__Expressões Condicionais:__

IF \(condição\) THEN \(ação\) END IF;

IF \(condição\) THEN \(ação1\) ELSE \(ação1\) END IF;

IF \(condição1\) THEN \(ação1\) ELSIF \(condição2\) THEN \(ação2\) ELSE \(ação3\) END IF;

Considerar a possibilidade Ifs dentro de Ifs\. Exemplo:

IF \(condição1\) THEN 

      IF \(condição2\) THEN 

      IF \(condição3\) THEN 

\(ação1\)  

      ELSE 

\(ação2\)

                                END IF; 

      ELSE 

\(ação4\) 

      END IF;

ELSE 

      IF \(condição4\) THEN 

\(ação5\)  

      ELSE 

\(ação6\) 

      END IF;

END IF;

As expressões condicionais com DECODE e CASE não são permitidas, pois se aplicam apenas em consultas\.

__Operadores Lógicos da Linguagem PL\-SQL:__

- E: AND 
- Ou: OR
- Negação: Not

__Operadores aritméticos da Linguagem PL\-SQL:__

- Soma: \+
- Subtração: \-
- Divisão: /
- Multiplicação: \*
- Exponenciação: \*\* \(esse operador só é reconhecido pelo pl/sql\)

__Operadores de comparação da Linguagem PL\-SQL__

- Diferente:  \!= e <>
- Igual que:  =
- Maior que: >
- Menor que: <
- Maior ou igual que: >= 
- Menor ou igual que:<= 
- Entre: BETWEEN

             Campara se o valores esta entre dois valores\. 

- Concatenar: || 
- Parecido: LIKE
- IS
- IS NOT

__     Funções PL\-SQL:__

__	__De modo geral todas as funções podem ser usadas, exceto as que estejam no conjunto das restrições\.	

- ABS
- LPAD
- LTRIM
- SUBSTR
- ADD\_MONTH
- INSTR
- UPPER
- NVL
- TO\_CHAR
- TO\_DATE
- TO\_NUMBER

__Operadores de atribuição  
__

- Atribuir o resultado utilizando a palavra RETURN, da seguinte forma: “RETURN” \+ valor ou campo \+ “;”

Exemplo: Return ‘12’; 

                Return 12;

                Return COD\_EMPRESA;

                Return TO\_CHAR\(sysdate, ‘DD’\);

__Algumas restrições:__

A regra não pode conter as seguintes palavras:

DBMS; DROP; TRUNCATE; DELETE; INSERT; UPDATE; FORMAT; CREATE; REPLACE; COMMIT;

ROLLBACK; EXECUTE; ALTER; ADD; ADMIN; ANALYZE; ALLOCATE; ARCHIVE; AUDIT; AUTOEXTEND;

 BACKUP; RESTORE; CACHE;CANCEL;CASCADE;CHANGE;CLEAR;CLONE;CLOSE;CLUSTER;

 COMPILE;COMPRESS;COMPUTE;CONSTRAINT;CONNECT;CONTROLFILE;CPU\_PER;CURSOR;DATAFILE;

 DBA;DEBUG;DEALL;DEFERRED;DIRECTORY;DISABLE;ENABLE;DISCONNECT;DISMOUNT;DML;DDL;ENABLE;

 ENFORCE;EXCEPT;EXPLAIN;EXTENT;FAILED;FALSE;FILE;FORCE;FUNCTION;PROCEDURE;GRANT;

 IMMEDIATE;IDENTIFIED;PARTITION;INSTANCE;LOCK;LOGFILE;LONG;NOFORCE;LOGGING;

 NETWORK;OFFLINE;OVERFLOW;PACKAGE;PROCEDURE;PRIVILEGE;PROFILE;PUBLIC;PURGE;

 READ;RESET;RENAME;REFERENCE;REFRESH;REPLACE;RESIZE;ROLE;RULE;SAVEPOINT;

 SCHEMA;SCOPE;SEQUENCE;SESSION;SIZE;SKIP;SNAP;STATISTICS;STANDBY;TRACE;START;

 STOP;STORAGE;STORE;STRUCTURE;SUCCESSFUL;SYS\_OP;SYNONYM;SYSDBA;SYSOPER;

 SYSTEM;TABLE;TEMPORARY;TIMESTAMP;TRACE;TRACING;TRANSACTION;TRIGGER;TYPE;UNDO;

 UNLIMITED;USAGE;USER;VIEW;&; GO TO\.

Ou seja, a regra não pode ter consulta em tabelas \(exemplo SELECT \* FROM SAFX02\), comandos de insert e delete\.

Caso a regra contenha palavras reservadas, a seguinte mensagem será exibida durante a validação:

“Instrução não validada, pois, contém palavra\(s\) reservada\(s\)\.’

# <a id="_Toc23871244"></a>Exemplos de Regras de Preenchimento:

Regras definidas para a SAFX02, campo VLR\_SALDO\_FIM:

IF TO\_NUMBER\(nvl\(VLR\_SALDO\_INI,0\)\)/100 = 0\.1  THEN 

RETURN LPAD\(\(\(TO\_NUMBER\(VLR\_SALDO\_INI\)/100 \+ 1\)\*100\),17,'0'\); 

END IF;

Regra contendo erro, pois está referenciando nome de campo que não existe na tabela SAFX02:

IF TO\_NUMBER\(nvl\(VLR\_SALDO\_INII,0\)\)/100 = 0\.1  THEN 

RETURN LPAD\(\(\(TO\_NUMBER\(VLR\_SALDO\_INI\)/100 \+ 1\)\*100\),17,'0'\); 

 END IF;

Erro retornado:

ORA\-06550: linha 1, coluna 44:

PLS\-00103: Encountered the symbol "I" when expecting one of the following:

   \) , \* & = \- \+ < / > at in é mod lembrete not rem =>

   <um expoente \(\*\*\)> <> ou \!= ou ~= >= <= <> e ou como like2

   like4 likec como entre de usando || multiset membro

   submultiset

The symbol "," was substituted for "I" to continue\.

Regras definidas para a SAFX02, campo COD\_CONTA:

IF COD\_CONTA IS NULL THEN RETURN SUBSTR\(COD\_ESTAB||COD\_EMPRESA, 1, 7\); END IF;

       = = = = = =


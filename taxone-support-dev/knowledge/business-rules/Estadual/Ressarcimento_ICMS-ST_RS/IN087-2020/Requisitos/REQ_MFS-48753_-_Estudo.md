# REQ_MFS-48753 - Estudo

- **Fonte:** REQ_MFS-48753 - Estudo.docx
- **Modificado:** 2024-03-27
- **Tamanho:** 366 KB

---

THOMSON REUTERS

<a id="_Hlk22664599"></a>__MFS\-48753__

__Módulo Estadual – Ressarcimento RS__

<a id="_Hlk53754126"></a>

Revisões

__Data__

__OS/Chamado__

__Descrição__

__Autor__

16/12/2020

MFS\-48753

IN087/2020

Liliane Assaf

Sumário

[1\.	INTRODUÇÃO	1](#_Toc60125991)

[1\.1	Documentos e Base Legal para a Solução	1](#_Toc60125992)

[2\.	Levantamentos junto a Área da Informação	1](#_Toc60125993)

[3\.	SOLUÇÃO FUNCIONAL / ESCOPO	1](#_Toc60125994)

[3\.1	Procedimentos para Fábrica	1](#_Toc60125995)

[3\.1\.1	– Alteração no Menu	1](#_Toc60125996)

[3\.1\.2	– Parametrização por CFOP	1](#_Toc60125997)

[3\.1\.3	– Parametrização por Natureza de Operação	1](#_Toc60125998)

[3\.1\.4	– Geração dos Movimentos	1](#_Toc60125999)

[3\.1\.5	– Limpeza das tabelas Específicas do Processo \(estudar\)	1](#_Toc60126000)

[3\.1\.6	– Cálculo da Média Ponderada Móvel Diária	1](#_Toc60126001)

[3\.1\.7	– Geração do 1250/1255 Pendente	1](#_Toc60126002)

[3\.1\.8	– Geração do Inventário  \(H030\) Pendente	1](#_Toc60126003)

[3\.1\.9	– Geração da Devolução da Saída \(saída é uma NF\)	1](#_Toc60126004)

[3\.1\.10	– Geração da Devolução da Saída \(saída é Um Cupom Fiscal\) Pendente	1](#_Toc60126005)

[3\.1\.11	– Geração da Devolução da Saída \(saída é Um Cupom Fiscal SAT\) Pendente	1](#_Toc60126006)

[3\.1\.12	– Geração da Saída \(Cupom – C480\) Pendente	1](#_Toc60126007)

[3\.1\.13	– Geração da Saída \(NF\)	1](#_Toc60126008)

[3\.1\.14	– Geração da Entrada	1](#_Toc60126009)

[3\.1\.15	– Geração da Devolução da Entrada	1](#_Toc60126010)

[3\.2	Procedimentos para Interface	1](#_Toc60126011)

[4\.	PROCEDIMENTOS PARA CONTEÚDO	1](#_Toc60126012)

[4\.1	Criação / Alteração – Tabelas \(Manual de Layout\)	1](#_Toc60126013)

[4\.2	Criação / Alteração em telas e relatórios \(manual operacional, roteiro e help\)	1](#_Toc60126014)

[4\.3	Criação / Alteração de Tabelas \(Fixas, Acessórias, Básicas\)	1](#_Toc60126015)

[4\.4	Criação / Alteração de Roteiro Operacional	1](#_Toc60126016)

[4\.5	Outras informações que necessitarão ser atualizadas \(help, manual operacional etc\)	1](#_Toc60126017)

[4\.6	Informações p/ Carta do Patch	1](#_Toc60126018)

[5\.	TESTES	1](#_Toc60126019)

# <a id="_Toc200962059"></a><a id="_Toc200996459"></a><a id="_Toc200996577"></a><a id="_Toc200998055"></a><a id="_Toc354574223"></a><a id="_Ref354574309"></a><a id="_Ref354574320"></a><a id="_Toc354574398"></a><a id="_Toc354574442"></a><a id="_Toc354574527"></a><a id="_Toc354578073"></a><a id="_Toc354578300"></a><a id="_Toc354578991"></a><a id="_Toc354579132"></a><a id="_Toc60125991"></a>INTRODUÇÃO

<a id="_Hlk53754794"></a>

## <a id="_Toc60125992"></a>Documentos e Base Legal para a Solução

__INSTRUÇÃO NORMATIVA RE Nº 087/20__

__INSTRUÇÃO NORMATIVA RE Nº 096/20__

# <a id="_Toc60125993"></a>Levantamentos junto a Área da Informação

<a id="_MON_1675838620"></a>![](data:image/x-emf;base64,AQAAAGwAAAABAAAAAQAAAGMAAAA7AAAAAAAAAAAAAAAtBwAApQQAACBFTUYAAAEAfBYAABUAAAACAAAAAAAAAAAAAAAAAAAAgAcAADgEAABYAQAAwgAAAAAAAAAAAAAAAAAAAMA/BQDQ9QIAGAAAAAwAAAAAAAAAGQAAAAwAAAD///8AcgAAAKAQAAAjAAAAAQAAAEIAAAAgAAAAIwAAAAEAAAAgAAAAIAAAAACA/wEAAAAAAAAAAAAAgD8AAAAAAAAAAAAAgD8AAAAAAAAAAP///wAAAAAAbAAAADQAAACgAAAAABAAACAAAAAgAAAAKAAAACAAAAAgAAAAAQAgAAMAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAA/wAA/wAA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABaW12ydHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/WltdsgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAARiEIYL1aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/476l//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAvVoY/71aGP+9Whj/vVoY//v18f//////0o5g/71aGP+9Whj/0o5g///////79fH/vVoY/71aGP+9Whj/vVoY//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/71aGP/FbzX////////////it5r/vVoY/71aGP/it5r////////////FbzX/vVoY/71aGP+9Whj/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/vVoY/9KOYP////////////fr4/+9Whj/vVoY//fr4////////////9KOYP+9Whj/vVoY/71aGP/6+vr/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAvVoY/71aGP+9Whj/3q2M/////////////////8l5Q//FbzX///////v18f//////3q2M/71aGP+9Whj/vVoY//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/71aGP/rzLf//////+K3mv//////3q2M/9qiff//////68y3///////rzLf/vVoY/71aGP+9Whj/+vr6/9N8K//TfCv/03wr/9N8K//TfCv/03wr/9N8K//6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/vVoY//fr4///////wWQm///////z4dT/68y3///////FbzX///////fr4/+9Whj/vVoY/71aGP/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAvVoY/71aGP/BZCb///////v18f+9Whj/68y3////////////9+vj/71aGP/z4dT//////8FkJv+9Whj/vVoY//r6+v/upUH/7qVB/+6lQf/upUH/7qVB/+6lQf/upUH/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/86DUv//////79bG/71aGP/aon3////////////it5r/vVoY/+bCqf//////zoNS/71aGP+9Whj/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/3q2M///////erYz/vVoY/8VvNf///////////9KOYP+9Whj/2qJ9///////erYz/vVoY/71aGP/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAvVoY/71aGP/mwqn//////9KOYP+9Whj/vVoY//fr4///////wWQm/71aGP/Og1L//////+bCqf+9Whj/vVoY//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAARiEIYL1aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/476l//r6+v/6+vr/+vr6/6aoqf90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5//r6+v/6+vr/+vr6//r6+v/Iycn/dHd5/yssLWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/+vr6//r6+v/6+vr/yMnJ/3R3ef8rLC1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef/6+vr/+vr6/8jJyf90d3n/KywtYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5//r6+v/Iycn/dHd5/yssLWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/yMnJ/3R3ef8rLC1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef90d3n/KywtYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWltdsnR3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/yssLWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAADAAAAAAAAAISAAAADAAAAAEAAABSAAAAcAEAAAEAAAAQAAAAAAAAAAAAAAAAAAAAvAIAAAAAAAABAgIiUwB5AHMAdABlAG0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAApwIAAM7IVNf7fwAAAAAAAAAAAACdHAEPAAAAACAAAAAAAAAACyRa1/t/AABDG93//////+gvAAAB3QEAAABqMZ8CAABDG93//////+gvAAAB3QEAAABqMZ8CAABDG93//////+gvAAAB3QEAAABqMZ8CAACL6I/XAAAAAACA/wEAAAAAQxsB3f////8AAAAAAAAAAAAAAAAAAAAAnRwBDwAAAADNLG7Y+38AAKAAAAD/////QxsB3QAA//8AWc/LpQAAAO1k8mz7fwAAAAAAAAAAAACL6I/X+38AANBZz8ulAAAA+VjPy6UAAAABAAAAAAAAANBZz8tkdgAIAAAAACUAAAAMAAAAAQAAACUAAAAMAAAADQAAgCgAAAAMAAAAAQAAAFIAAABwAQAAAQAAAPX///8AAAAAAAAAAAAAAACQAQAAAAAAAABAACJTAGUAZwBvAGUAIABVAEkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABi2z8ulAAAAYZfW2ft/AAAAAAAAAAAAAECWNyGfAgAACKo1IZ8CAAAAAAAAAAAAAAAAuSSfAgAAUA3Pbft/AACQPjshnwIAAK8AAAAAAAAAAAC5JJ8CAACgKrkknwIAAAAAAAAAAAAABwAAAAAAAAAAAIcUnwIAAJAauSQAAAAAOJk9IZ8CAAAAJX4UnwIAAAAAAAAAAAAACAAAAAAAAAA4mT0hnwIAAEAAAAAAAAAAAAAAAAAAAADA805pAAAAAOBLuSSfAgAAkV7W2ft/AABAAAAAAAAAAIvoj9f7fwAAALbPy6UAAABptM/LpQAAACAAAAAAAAAAALbPy2R2AAgAAAAAJQAAAAwAAAABAAAAVAAAAKwAAAAGAAAAIgAAAGEAAAAuAAAAAQAAAFVVj0EmtI9BBgAAACIAAAAQAAAATAAAAAQAAAAAAAAAAAAAAGYAAABCAAAAbAAAAFIARQBRAF8ATQBGAFMALQA0ADgANwA1ADMAIAAtACAABwAAAAYAAAAIAAAABQAAAAoAAAAGAAAABgAAAAQAAAAGAAAABgAAAAYAAAAGAAAABgAAAAMAAAAEAAAAAwAAAFQAAAC0AAAAAQAAAC8AAABjAAAAOwAAAAEAAABVVY9BJrSPQQEAAAAvAAAAEQAAAEwAAAAEAAAAAAAAAAAAAABmAAAAQgAAAHAAAABMAGUAdgBhAG4AdABhAG0AZQBuAHQAbwAuAGQAbwBjAHgAZD4FAAAABgAAAAUAAAAGAAAABwAAAAQAAAAGAAAACQAAAAYAAAAHAAAABAAAAAcAAAADAAAABwAAAAcAAAAFAAAABQAAACUAAAAMAAAADQAAgEYAAAAgAAAAEgAAAEkAYwBvAG4ATwBuAGwAeQAAAAAARgAAAFAAAABEAAAAUgBFAFEAXwBNAEYAUwAtADQAOAA3ADUAMwAgAC0AIABMAGUAdgBhAG4AdABhAG0AZQBuAHQAbwAuAGQAbwBjAHgAAABGAAAAEAAAAAIAAAAAAAAARgAAABAAAAAEAAAAMQAAAEYAAAAgAAAAEgAAAEkAYwBvAG4ATwBuAGwAeQAAAAAADgAAABQAAAAAAAAAEAAAABQAAAA=)

\- \[DUV\-TEC\] NF de devolução de saída com a saída no mesmo dia da devolução\. Não vou conseguir obter o valor unitário da saída pela tabela de controle\.

\- \[DUV\-TEC\] No caso da Devolução da Saída que referencia uma nota de Saída de um período anterior a vigência da IN\-087, ou seja o valor médio ponderado do dia da nota de saída não está calculado no sistema, podemos pensar em seguir como feito no Ressarcimento SP \-CAT 42: a nota de saída deve ser carregada com esse valor no campo 107\. IN RE 096/20 orientou\.

5\) Qual a diferença entre 19\.3\-A\.4 para 19\.3\-A\.3? 19\.3\-A\.4 é relacionado ao inventário de qualquer período e 19\.3\-A\.3 especificamente de 31/12/2020?

6\) Consegui acompanhar bem os itens 19\.3\-A\.1, 19\.3\-A\.2 e 19\.3\-A\.3\.  Os demais precisa estudar para tentar extrair quais tratamentos precisamos fazer\.

7\) Quais tratamentos que tenho que fazer para gerar 1250, 1255? To perdida\. 

\- \[DUV\-TEC\] Como é gerado esse registro por Inscrição Estadual Única? Achamos que não há necessidade\.

8\) Qual a definição do cod\_motivo do C185, \.\.\.? Cada operação usa um conjunto de códigos?

 

# <a id="Premissas"></a><a id="_Toc200962060"></a><a id="_Toc200996460"></a><a id="_Toc200996578"></a><a id="_Toc200998056"></a><a id="_Toc354574225"></a><a id="_Toc354574400"></a><a id="_Toc354574444"></a><a id="_Toc354574529"></a><a id="_Toc354578075"></a><a id="_Toc354578302"></a><a id="_Toc354578993"></a><a id="_Toc354579134"></a><a id="_Toc60125994"></a>SOLUÇÃO FUNCIONAL / ESCOPO

1. Devolução de Saída: Utilizar a SAFX08 utilizando os campos de referência\. Utilizar a SAFX192\.
2. Devolução de Entrada: Utilizar a SAFX08 utilizando os campos de referência\.
3. Utilizar para cupom safx993/994 e safx201/2020
4. Utilizar SAFX117 – Devolução de Saída por Cupom referenciado

 

__Documentos__

__Tabelas \(Capa/Itens\)__

Notas Fiscais \(modelos 01, 1B, 04, 55, 65\) 

SAFX07 / SAFX08

Cupons Fiscais \(modelos 02, 2D, 2E e 60\)

SAFX993 / SAFX994

Cupons Fiscais \(modelo 59\-CFe SAT\)

SAFX201 / SAFX202

2\) Parametrizações de CFOP e Natureza Op\. com revisão do menu\.

3\) Geração do Movimento:

\- Cálculo da Média Ponderada Móvel \+ Relatório com detalhameto de cada valor que compõe a média

\- Geração das Notas Fiscais de Saídas p/ Consumidor Final \+ Relatório \(referente ao C185, C380\);

\- Geração das Notas Fiscais de Devolução de Saídas p/ Consumidor Final \+ Relatório \(referente ao C181\);

\- Geração das Notas Fiscais de Entradas \+ Relatório \(referente ao C180\);

\- Geração das Notas Fiscais de Devolução de Entradas \+ Relatório \(referente ao C186\);

\- Geração dos Cupons Fiscais \(SAFX994\) \+ Relatório \(referente ao C480\);

\- Geração das Notas Fiscais de Devolução de Saídas p/ Consumidor Final \(referencia cupom\) SAFX117 \+ Relatório \(referente ao C181\);

\- Geração dos 1250/1255: baseado nos registros anteriores;

\- Geração dos resultados nas tabelas do SPED FISCAL:

  C180 ou C185 ou C380, a rotina irá alimentar a tabela x296\_info\_compl\_st\_itens\_merc;

  C181 ou C186, a rotina irá alimentar a tabela SAFX308;

  C480 a tabela será a X297\_INF\_COMP\_ST\_CUPOM\_ECF;

  1250/1255 a tabela será a x304\_saldo\_cons\_res\_comp\_icms;

  H030 a rotina irá gravar a tabela X52 registro do último dia do mês anterior, a partir da Tabela de Controle das Médias Ponderadas Móveis\.

OBS: O Ressarcimento MG gera C330 e C430, Mas RS não menciona esses registros pois são do perfil B\. RS está trabalhando com Perfil A que usa C380 e C480\.

__4\) Pontos para Discussão e avaliação__:

\- Geração Por Inscrição Estadual Única

 \- FECEP embutido ok Carrefour \(04/01\)

\- Utilizar DATA MART p/ períodos anteriores ok

\- %Redução de Base de Cálculo ok

\- Quantidade Convertida ok

\- Produtos Associados ??? Carrefour \( em 04/01 disse que não tem\)

\- 43, 80, 225 : ICMS\-ST ok

\- Relatório de conferencia da media ponderada com detalhamento\.

\- Relatório de conferencia do 1250/1255, pois no tópico 19\.4, cita que o cliente deverá fazer um lançamento com base no resultado apurado nesses registros\. O relatório deve servir de apoio para o cliente fazer manualmente esse lançamento:

"19\.4\-A \- Apuração a partir de 1º de janeiro de 2021 \(RICMS, Livro III, art\. 25\-C\)

19\.4\-A\.1 \- Ao final de cada período de apuração o contribuinte deverá informar os registros 1250 e 1255 com as

informações resultantes do preenchimento do subitem 19\.3\-A, e apurar, por meio de subtração, a diferença entre:

a\) a soma dos valores informados no campo VL\_ICMS\_ST\_COMPL\_MOT dos registros 1255, que citarem, no campo

COD\_MOT\_REST\_COMPL, código da tabela 5\.7 que tenha, para a classificação para ressarcimento/restituição/complemento o caractere "3" ou

o caractere "6";

b\) a soma dos valores informados no campo VL\_ICMS\_ST\_REST\_MOT dos registros 1255, que citarem, no campo

COD\_MOT\_REST\_COMPL, código da tabela 5\.7 que tenha, para a classificação para ressarcimento/restituição/complemento o caractere "1" ou

o caractere "8"\.

19\.4\-A\.2 \- Apurados os valores previstos no subitem 19\.4\-A\.1:

a\) a diferença positiva constituirá valor líquido a complementar, que deverá ser informado na EFD por meio de ajuste em

registro E220, que deverá citar o código RS101255 no campo COD\_AJ\_APUR;

b\) a diferença negativa constituirá o valor líquido a restituir, que deverá ser informado na EFD por meio de ajuste,

distribuído por escolha do contribuinte, para compensar saldo devedor do imposto:

1 \- de responsabilidade por substituição tributária, por meio de informação no registro E220, que deverá citar o código

RS121255 no campo COD\_AJ\_APUR;

2 \- próprio, por meio de informação no registro E111, que deverá citar o código RS021255 no campo COD\_AJ\_APUR\.”

\[DUV\-CARREFOUR\]

\- O cenário de devolução parcial só dá pra ser atendido com uso da SAFX192\. No primeiro momento que estamos usando os campos de referência da SAFX08 da nota de devolução, só estamos considerando devolução total\.

\- Um item devolvido se composto por mais de uma nota de saída tb só pode ser atendido pela SAFX192\. 

\- Produtos Associados no Sped Fiscal, como são escriturados? O produto associado grava inventário \(H010\)?

\- Registros C380 e C480 tem necessidade de gerá\-los? Priorização\!

## <a id="_Toc200962061"></a><a id="_Toc200996461"></a><a id="_Toc200996579"></a><a id="_Toc200998057"></a><a id="_Toc354574226"></a><a id="_Toc354574401"></a><a id="_Toc354574445"></a><a id="_Toc354574530"></a><a id="_Toc354578076"></a><a id="_Toc354578303"></a><a id="_Toc354578994"></a><a id="_Toc354579135"></a><a id="_Toc60125995"></a>Procedimentos para Fábrica

### <a id="_Toc60125996"></a>– Alteração no Menu

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Descrição__: 

Alterar o menu para distribuir os itens já existentes e incluir novos\.  Os itens já existentes que apenas foram reposicionados, estão marcados em amarelo, e os novos em verde\.

Parâmetros		         Geração			       Relatórios		

IN\-RE 048/18		         IN\-RE 048/18		                       IN\-RE 048/18

     Dados Iniciais		              Geração dos Movimentos	            Conferência dos Movimentos

     Operações		              Transferências entre Apurações            Conferência da Transferência entre Apurações

          CFOP		         IN\-RE 087/20

          Natureza de Operação	              Geração dos Movimentos

IN\-RE 087/20		     

      Operações

   	CFOP

   	Natureza de Operação

Produtos

      Por Código

      Por NCM

      Por Cest

### <a id="_Toc60125997"></a>– Parametrização por CFOP

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> \(IN\-RE 087/20\) >> Operações >> CFOP

__Descrição:__

Criar tela de parametrização do CFOP para demonstrar as operações:

\- Entrada \(e Devoluções\)

\- Saída Interna à Consumidor Final \(e Devoluções\)

Can vai confirmar as demais operações:

\- Venda interna a consumidor final: RICMS, Livro III, art\. __25\-A e art  25\-B__;

\- Saída com CFOP 5\.927 \(baixa de estoque decorrente a perda, roubo, ou deteriorioração\)

\- Fato gerador presumido não realizado: RICMS, Livro III, __art\. 22\.__

\- Operações definidas no RICMS, Livro III, __art\. 23__ \(saídas para outras ufs?\)\.

\- Operações definidas no RICMS, Livro III, __art\. 24 __\(saídas para outras uf?\) e __24\-A__ \(saídas isentas?\)\.

### <a id="_Toc60125998"></a>– Parametrização por Natureza de Operação

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> <a id="_Hlk59893211"></a>\(IN\-RE 087/20\) >> Operações >> CFOP

__Descrição:__

Criar tela de parametrização do CFOP para demonstrar as operações:

\- Entrada \(e Devoluções\)

\- Saída Interna à Consumidor Final \(e Devoluções\)

### <a id="_Toc60126000"></a>– Limpeza das tabelas Específicas do Processo \(estudar\)

__Localização__: 

__Menu__: 

__Descrição:__

EST\_ST\_RS\_NF\_SAI, …

### <a id="_Toc60125999"></a>– Geração dos Movimentos

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Geração >> \(IN\-RE 087/20\) >> Geração dos Movimentos

 

__Descrição:__

Realizar a geração dos documentos fiscais de entradas \(e devoluções\), saídas internas para consumidor final \(e Devoluções\)\.

Ver documentos:

MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\.docx

MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Entradas\.docx

MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Devolução de Entradas\.docx

MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Saidas\.docx

MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Devolução de Saidas\.docx

__Pendências__:

 \- Cálculo do médio ponderado movel

__Próxima MFS__:

\- geração do 1250, 1255 \(pendente\)

\- geração do h030 \(pendente\)

__Futura MFS:__

\- geração do C181 devolução com saída por cupom fiscal \(modelos 02\) 

\- geração do C181 devolução com saída por cupom fiscal saf \(modelos 59\)

\- geração da C480 saída por cupom fiscal \(modelos 02\) \- SAFX993, SAFX994

ESBOÇO DA PACKAGE:

CHAMADORA:

  1o\) GERAÇÃO DO C180; \(TODOS NOTAS DO PERIODO grava NF\_ENT\)

  2o\) GERAÇÃO DO C186; \(TODAS AS NOTAS DO PERIODO grava DEV\_ENT\)

3o\) LOOP POR DIA, executar:

       3\.1\) GERAÇÃO DA C181 \(DIA\) \(LE E GRAVA DEV\_SAI\);

	         loop devolução \-\-> saidas

			 gravar a dev\_sai

       3\.2\) CALCULAR DA MEDIA PONDERADA \(DIA\)

            A\) SALDO INICIAL = SALDO FINAL DO DIA ANTERIOR

			B\) NF ENTRADA \(C180\) \(leitura  NF\_ENT\)

            C\) NF DEVOLUÇÃO DE ENTRADA \(C186\) \(leitura DEV\_ENT\)

            D\) NF DEVOLUÇÃO DA SAÍDA \(C181\)  \(leitura DEV\_SAI\)

            E\) CALCULO O SALDO FINAL E INSERT NA TABELA DE MEDIAS PODERADAS 

    END LOOP DIA;

4o\) GERAÇÃO DA C185; \(TODOS NOTAS DO PERIODO grava NF\_SAI\) 

\-\-\-\-\-\-\-\-\-

5o\) Expurgo dos relatórios:

    Le as tabelas NF\_ENT, NF\_SAI\.\.\. e gravar em arquivo;

6o\) Geração das tabelas do sped fiscal;

    Le as tabelas NF\_ENT, NF\_SAI\.\.\. e gravar tabelas X296, X308;

### <a id="_Toc60126004"></a>– Geração da Devolução da Saída \(saída é uma NF\) 

Recuperação da nota de devolução de saída \(que é uma nota de entrada\) e das notas de saídas objetos da devolução\.

__Origem dos Dados:__ __SAFX07, SAFX08__ __ou SAFX192__

   \- __*Nota de entrada*__ \(MOVTO\_E\_S <> “9”\);

   \- Nota fiscal de devolução \(NORM\_DEV = “2”\);

   \- produto parametrizado;

   \- cfop / Natureza de Operação parametrizado;

   \-  modelos para geração do C181: \(01, 1B, 04, 55,65\)

   \- Recuperar as notas de saídas pelos campos de referência da SAFX08\. O documento de referência deve ser recuperado na base de dados a partir dos critérios descritos abaixo: 

\- nota fiscal de saída \(MOVTO\_E\_S  = ‘9’\);

\- Nota fiscal normal \(NORM\_DEV = “1”\);

\- número da nota = conteúdo do campo 117 da SAFX08;

\- série da nota      = conteúdo do campo 118 da SAFX08;

\- subsérie da nota = conteúdo do campo 119 da SAFX08;

\- data de emissão da nota = conteúdo do campo 102 da SAFX08;

\- produto = produto do item da nota de devolução; 

Obs: a recuperação dos documentos ficais do período pode ser feito pelas tabelas do Data Mart\. Mas a recuperação da nota referenciada, deve ser feita pela tabela definitiva X07/X08, pois essas notas podem estar em períodos anteriores, onde pode não existir informação do Data Mart\.

OBS: CUIDADO SE FOR USAR A SAFX192, Pois o campo __32 \- Quantidade Convertida __será gravado com a__ quantidade devolvida da SAFX192, MAS __todos os outros campos que utilizam a quantidade para fazer calculo do valor unitário, precisarão ser alterados para usar a quantidade convertida da nota de saída referenciada\!\!\! 

__Gravação da SAFX308__

__EST\_ST\_RS\_NF\_DEV\_SAI__

__Regra de geração do C181 no SPED FISCAL__

RNC181

Gravar a SAFX308:

Campos 01 a 15 – Campos chave da nota de devolução de saída 

Campo 16 – preencher com 1\-Nota Fiscal \(SAFX07/08\)

Campos 17 ao 23 – campos chave da nota de saída referenciada; Campo 21 deve ser preenchido com a data de emssão\.

Campo 30  \- preencher com o numero do item da nota de saída referenciada;

Este registro foi criado na versão 1\.14, com vigência a partir de Jan/2021 \(__MFS45380__\)\.

Trata\-se de um registro “filho” do C170, e seu objetivo é demonstrar informações complementares de ICMS\-ST, das operações de devolução de saída \(__*notas de entrada*__\)\.  São informações referentes às notas de saída que originaram a devolução\.

__Origem dos Dados:__ __SAFX308__ \(Tabela das Informações Complementares das Operações de Devolução Sujeitas ao ST \- Sped Fiscal\) 

Este registro será gerado apenas quando a nota fiscal em questão \(nota fiscal do item gravado no registro “pai” C170\) tiver as seguintes características:

   \- __*Nota de entrada*__ \(MOVTO\_E\_S <> “9”\);

   \- Nota fiscal de devolução \(NORM\_DEV = “2”\);

Se atendidas estas condições, será verificada a existência de dados na SAFX308 para o item do registro “pai” \(C170\)\.

Critérios para recuperação dos dados na SAFX308:

Campos 01 a 15 – Considerar os campos chave do item do registro “pai” C170;

Poderão existir ‘n’ registros na SAFX308 para o item, e para cada um deles, será gerado um registro C181\.

RNC181\-02

__Campo 31 \- Código Motivo __

??????

Se basearmos na regra de MG, para saber se houve ressarcimento ou complemento na operação de saída, comparar:

Se \(BC\-Ent\) > \(BC\-Sai\) então:

   A saída referenciada na devolução obteve Restituição;

   RS600 

Se \(BC\-Ent\) < \(BC\-Sai\) então:

   A saída referenciada na devolução obteve Complemento;

   RS800  

Se \(BC\-Ent\) = \(BC\-Sai\) então:

   A saída referenciada na devolução não teve nem Restituição nem Complemento\.

  RS500 

Onde:

- \(BC\-Ent\) Valor unitário médio móvel calculado da BC ICMS\-ST recuperado da Tabela de Controle considerando o Produto e a Data de Emissão da nota de saída referenciada\. 

*\(ver OBS sobre os produtos associados, pois os valores medios estariam no produto principal\)*

Caso não exista registro na Tabela de Controle, segundo o tópico __19\.3\-A\.1\.5\.1 da IN __é necessário recuperar a informação da última nota fiscal de recebimento da mercadoria anterior à nota de saída referenciada\. Recuperar da tabela definitiva X07/08 não da DWT\. 

- \(BC\-Sai\) Valor Unitário da BC do ICMS na Operação Conv, calculado conforme regra:

Se o campo “__%Redução BC__” da parametrização de Produto ou NCM está preenchido com valor > 0, então:

     Este campo será gerado da seguinte forma:

     \[\(Vlr Contábil – \(Vlr Contábil \* “%Redução BC” / 100\)\)\]/ QTD\_CONV

Senão:

      Este campo será gerado da seguinte forma:

      \[\(Vlr Contábil\)\] / QTD\_CONV 

Onde:

- %Redução BC da parametrização de Produto ou NCM sujeito ao ICMS\-ST, vigente na Data de Emissão da Saída referenciada;
- 64\-Vlr Contabil do Item da nota de Saída referenciada;
- QTD\_CONV que foi gravada no campo __32 \- Quantidade Convertida __

\*\* 28/12: alterei pra quantidade do item da nota de SAÍDA \*\*

Campo __02\-COD\_MOT\_REST\_COMPL__

Conteúdo do campo “31\-Código Motivo” da SAFX308\.

RNC181\-03

__Campo 32 \- Quantidade Convertida \(QTD\_CONV\)__

\*\* 28/12: alterei pra quantidado do item da nota de devolução \*\*

Campo 24\-Quantidade do Item da nota de Saída referenciada, aplicando a conversão, quando necessário\. Veja:

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\)  __*\(ver OBS abaixo sobre os produtos associados\)*

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria quantidade do item da nota;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\)

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade Convertida”;

     Senão         

         Nesse caso a quantidade do item \(SAFX08\) será convertida para a unidade de medida do cadastro do produto;

         \[ Quantidade do item da nota \(SAFX08\) \* Fator de Conversão \]

__Sobre os produtos associados:__ Quando se tratar de uma nota fiscal de produto “associado”, a comparação será feita da unidade de medida da nota, com a __unidade do produto principal__\.

Exemplo:

__Produto principal__: COCA\-COLA PET                 \(unidade de medida do estoque – SAFX2013 = UN\) 

__Produtos associados__: COCA\-COLA PET–1      \(unidade de medida do estoque – SAFX2013 = PAC \(6 unidades\)\)

Nota de venda do produto associado: __COCA\-COLA PET\-1__, unidade da nota = PAC, Quantidade = __5__

Compara a unidade de medida da nota do produto associado com a unidade de estoque do produto principal: PAC x UN

Como é diferente, deve\-se converter a quantidade da nota de PAC para UN\. 

Para acessar a tabela de conversão por produto, será utilizado o código do produto principal:

__DWT\_CONV\_MEDIDA\-2: __Produto = __COCA\-COLA PET__

                                          Unidade Origem = PAC

                                          Unidade Destino = UN

                                          Fator de conversão = 6,0000

Conversão da quantidade da nota do associado:  QTD da nota x Fator de Conversão   =  5 x 6,0000 = 30,0000 

Lembrando que, quando não existe fator na tabela de conversão por produto \(DWT\_CONV\_MEDIDA\_2\), será utilizada a tabela padrão \(DWT\_CONV\_MEDIDA\)\.  

__= = = = =__

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o item da nota será gerado com o campo Quantidade da Saída sem informação, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. O item do documento será gerado sem a informação da quantidade e do valor unitário”*

* *\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item do documento, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

Campo __03\-QUANT\_CONV__

Conteúdo do campo “32\-Quantidade Convertida” da SAFX308\.

RNC181\-04

__Campo: 33\-Unidade de Medida \(COD\_MEDIDA\)__

Unidade de Medida do Produto\. Campo “14\-Código de Medida” da SAFX2013 \(unidade da SAFX2007\);

*\(ver OBS sobre os produtos associados\)*

Campo: __04\-UNID__

Conteúdo do campo “33\-Unidade de Medida” da SAFX308\.

A unidade informada deve ter seus dados de cadastro informados em um registro 0190 \(Identificação das Unidade de Medida\)\. 

Se a unidade de medida informada neste campo for diferente da unidade de medida que será gravada no registro 0200 do Produto \(unidade de medida padrão da SAFX2013, campo “*20 – Unidade de Medida Padrão*”, conforme a RN0200\-06\), o fator de conversão entre as duas unidades será gravado no registro 0220\. 

RNC181\-05

Campo: __05\-COD\_MOD\_SAIDA__

O preenchimento deste campo depende da espécie do documento de referência informado \(campo 16\- Espécie do Documento de Referência da Devolução\), da seguinte forma:

Se campo 16 = 1 \(Nota Fiscal SAFX07/SAFX08\)

    A partir dos campos da SAFX308 que compõem a chave da nota fiscal \(campos 17 ao

    23\), e considerando nessa busca apenas as notas de *saída* e NORM\_DEV = “1”, 

    recuperar o modelo da capa do documento fiscal \(campo 13\-Modelo de Documento,   

    da SAFX07\); 

Se campo 16 = 2 \(Cupom Fiscal SAFX993/994\)

     Preencher com o conteúdo do campo “24\-Modelo do Cupom Fiscal de Referência” da 

     SAFX308;

Se campo 16 = 3 \(Cupom Fiscal SAFX201/202\)

    A partir dos campos da SAFX308 que compõem a chave do cupom fiscal \(campos 27, 28

    e 29\), recuperar o modelo da capa do cupom fiscal \(campo 06\-Modelo Documento da 

    SAFX201\); 

RNC181\-06

 

Campo __06\-SERIE\_SAIDA__:

Este campo será preenchido apenas se as seguintes condições forem verdadeiras:

- Campo “16\- Espécie do Documento de Referência da Devolução” = “__1__” \(Nota Fiscal\);
- Modelo da nota fiscal informado no campo 05\-COD\_MOD\_SAIDA = 01, 1B ou 04;

Nesse caso, será informado o conteúdo do campo “18\-Série do Documento Fiscal de Referência” da SAFX308\.   

RNC181\-07

Campo __07\-ECF\_FAB\_SAIDA__:

Este campo será preenchido apenas se as seguintes condições forem verdadeiras:

- Campo “16\- Espécie do Documento de Referência da Devolução” = “__2__” \(Cupom Fiscal\); 
- Modelo do cupom fiscal informado no campo 05\-COD\_MOD\_SAIDA = 02 ou 2D; \(ou seja, apenas cupom fiscal da SAFX993/SAFX994\) 

Nesse caso, será informado o conteúdo do campo “07 – Número do Fabricação \(COD\_FABRICACAO\_ECF\) da Tabela de Cadastro do Equipamento ECF \(SAFX2087\), relacionado ao “25\-Número do Caixa do Cupom Fiscal de Referência” da SAFX308\.

RNC181\-08

;   

Campo __08\-NUM\_DOC\_SAIDA__:

Este campo será preenchido apenas se as seguintes condições forem verdadeiras:

- Campo “16\- Espécie do Documento de Referência da Devolução” = “__1__” ou “__2__” \(Nota Fiscal ou Cupom Fiscal\);
- Modelo do documento informado no campo 05\-COD\_MOD\_SAIDA = 01, 1B, 02, 2D ou 04\.

 

Quando se tratar de nota fiscal \(campo 16 = “__1__”\), será informado o conteúdo do campo “17\- Número do Documento Fiscal de Referência” da SAFX308;

Quando se tratar de cupom fiscal \(campo 16 = “__2__”\), será informado  o conteúdo do campo “26\-COO \(Contador de Ordem de Operação\) do Cupom Fiscal de Referência” da SAFX308;   

RNC181\-09

Campo __09\-CHV\_DFE\_SAIDA__:

Este campo será preenchido apenas na seguinte condição:

- Se o Modelo do documento informado no campo 05\-COD\_MOD\_SAIDA = 55, 59, 60 ou 65;

O conteúdo a ser informado depende da espécie do documento, da seguinte forma:

 

Se campo 16 = 1 \(Nota Fiscal SAFX07/SAFX08\)

    A partir dos campos da SAFX308 que compõem a chave da nota fiscal \(campos 17 ao

    23\), e considerando nessa busca apenas as notas de *saída* e NORM\_DEV = “1”, 

    recuperar a chave eletrônica da NFe \(campo 226\-Chave de Acesso da NF\-Eletrônica

    da SAFX07\)\. Utilizar as primeiras 44 posições, seguindo o formato da NF\-e nacional; 

Se campo 16 = 2 \(Cupom Fiscal SAFX993/994\)

    A partir dos campos da SAFX308 que compõem a chave do cupom fiscal \(campos 24,

    25, 26, 27\), recuperar a chave eletrônica do cupom \(campo 28\-Chave do CFe da 

    SAFX993\)\. Utilizar as primeiras 44 posições, seguindo o formato da NF\-e nacional;

Se campo 16 = 3 \(Cupom Fiscal SAFX201/202\)

    A partir dos campos da SAFX308 que compõem a chave do cupom fiscal SAT \(campos

    27, 28 e 29\), recuperar a chave eletrônica do cupom \(campo 10\-Chave de Acesso do CF\-

    e da SAFX201\)\. Utilizar as primeiras 44 posições, seguindo o formato da NF\-e nacional; 

Crítica sobre o preenchimento do campo:

No caso destes modelos de documento \(55, 59, 60 ou 65\), se a informação da chave eletrônica não estiver preenchida no documento, para qualquer um dos casos \(seja documento da SAFX07, SAFX993 ou SAFX201\), o campo será gravado sem informação, e no log será gravada uma mensagem de erro, conforme padrão do Sped Fiscal: “*O campo CHV\_DFE\_SAIDA  é de preenchimento obrigatório, e não foi informado”*\.

O log deve exibir os dados de identificação da nota de devolução, e também do documento de referência \(seja Nota, Cupom ou Cupom SAT\), para que o usuário possa identificar o problema\.

RNC181\-10

Campo __10\-DT\_DOC\_SAIDA__:

O conteúdo a ser informado depende da espécie do documento, da seguinte forma:

 

Se campo 16 = 1 \(Nota Fiscal SAFX07/SAFX08\)

    A partir dos campos da SAFX308 que compõem a chave da nota fiscal \(campos 17 ao

    23\), e considerando nessa busca apenas as notas de *saída* e NORM\_DEV = “1”,

    recuperar a data de emissão da nota \(campo 11\-Data de Emissão da SAFX07\);

Se campo 16 = 2 \(Cupom Fiscal SAFX993/994\)

    A partir dos campos da SAFX308 que compõem a chave do cupom fiscal \(campos 24,

    25, 26, 27\), recuperar a data de emissão do cupom \(campo 06\-Data da Emissão da 

    SAFX993\);

Se campo 16 = 3 \(Cupom Fiscal SAFX201/202\)

    A partir dos campos da SAFX308 que compõem a chave do cupom fiscal SAT \(campos

    27, 28 e 29\), recuperar a data de emissão do cupom \(campo 05\-Data da Emissão da

    SAFX201\); 

RNC181\-11

Campo __11\-NUM\_ITEM\_SAIDA__

Conteúdo do campo “30\- Número do Item do Documento de Referência” da SAFX308\.

RNC181\-12

__Campo 34\-Valor Unitário Conv \(VLR\_UNIT\_CONV\)__

  VLR\_UNIT\_CONV = VLR\_CONTAB\_ITEM da SAFX08 / QTD\_CONV

Onde:

- VLR\_CONTAB\_ITEM é o campo 64\-valor Contabil do Item da nota de saída referenciada;
- QTD\_CONV que foi gravada no campo __32 \- Quantidade Convertida__

\*\* 28/12: alterei pra quantidade do item da nota de SAÍDA \*\*

__Pode ser alterado pelo Carrefour – MFS57863 __

Campo __12\-VL\_UNIT\_CONV\_SAIDA__

Conteúdo do campo “34\-Valor Unitário Conv” da SAFX308\.

RNC181\-13

__Campo 39\- Valor Unitário ICMS OP Estoque Conv \(VLR\_UNIT\_ICMS\_ESTQ\_SAI\)__

Valor Unitário Médio Móvel Calculado para o __ICMS__ recuperado da Tabela de Controle considerando:

\- Produto e a Data de Emissão da nota de saída referenciada\.

*\(ver OBS sobre os produtos associados, pois os valores medios estariam no produto principal\)*

Caso não exista registro na Tabela de Controle, segundo o tópico __19\.3\-A\.1\.5\.1 da IN __é necessário recuperar a informação da última nota fiscal de recebimento da mercadoria anterior à nota de saída referenciada\. Recuperar da tabela definitiva X07/08 não da DWT\. 

Preencher com: Valor do ICMS / Qtde Convertida da NF de Entrada

Valor do ICMS é oriundo de um dos três campos SAFX08, dependendo de qual esteja preenchido:

Campo “43\-Valor ICMS”, se preenchido, ou

   Campo “80\-ICMS não Escriturado”, se preenchido, ou

       Campo “225\-Valor ICMS Não Destacado”  

Campo __13\-VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV\_SAIDA__

Conteúdo do campo “39\- Valor Unitário ICMS OP Estoque Conv” da SAFX308

RNC181\-14

__Campo 40\-Valor Unitário ICMS ST Estoque Conv \(VLR\_UNIT\_ICMSS\_ESTQ\_SAI\)__

Valor unitário médio móvel calculado para os __ICMS\-ST__ \+ __FECP\_ICMS\_ST__ \(\*\) recuperado da Tabela de Controle considerando:

\- Produto e a Data de Emissão da nota de saída referenciada\.

*\(ver OBS sobre os produtos associados, pois os valores medios estariam no produto principal\)*

\(\*\) Pelo guia prático esse campo corresponde ao VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV preenchido na ocasião da saída \(C185\), que é preenchido com ICMS ST incluindo FCP ST\.

__\(\*\) Faz sentido a gente inserir o parametro FECP embutido\.__

Caso não exista registro na Tabela de Controle, segundo o tópico __19\.3\-A\.1\.5\.1 da IN __é necessário recuperar a informação da última nota fiscal de recebimento da mercadoria anterior à nota de saída referenciada\. Recuperar da tabela definitiva X07/08 não da DWT\. 

Preencher com: \(Valor do ICMS\-ST \+ FECEP\-ST\) / Qtde Convertida da NF de Entrada

Onde:

Valor do ICMS\-ST é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Campo “52\-Valor ICMS Substituição Tributária”,                 se preenchido, ou

   Campo “145\-Valor de ICMS\-ST não Escriturado”,            se preenchido, ou

       Campo “133\-ICMS\-ST Não Escriturado”,                      se preenchido, ou 

           Campo “107\-Valor Carga Tributária Origem”,             se preenchido\.

Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.

 

Na IN087/20 tópico 19\.3\-A\.2\.2\.1:

2 \- ao valor unitário médio móvel calculado ao fim do dia em que ocorreu a saída objeto de devolução ou retorno deverão corresponder às registradas no campo VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\_SAIDA dos registros C181 do dia\.

Redação dada pela IN096/20:

2 \- ao valor unitário médio móvel calculado ao fim do dia em que ocorreu a saída objeto de devolução ou retorno deverá corresponder à soma dos valores informados nos campos VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV\_SAIDA e VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\_SAIDA dos registros C181 do dia, dividida pela alíquota informada no campo ALIQ\_ICMS do registro 0200, expressa em notação decimal

Campo __14\-VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\_SAIDA__

Conteúdo do campo “40\-Valor Unitário ICMS ST Estoque Conv” da SAFX308

RNC181\-15

__Campo 41\-Valor Unitário FCP ICMS ST Estoque Conv \(VLR\_UNIT\_FCP\_ESTQ\_SAI\)__

Valor Unitário Médio Móvel Calculado para o FECP\_ICMS\_ST recuperado da Tabela de Controle considerando:

\- Produto e a Data de Emissão da nota de saída referenciada\.

*\(ver OBS sobre os produtos associados, pois os valores medios estariam no produto principal\)*

Caso não exista registro na Tabela de Controle, segundo o tópico __19\.3\-A\.1\.5\.1 da IN __é necessário recuperar a informação da última nota fiscal de recebimento da mercadoria anterior à nota de saída referenciada\. Recuperar da tabela definitiva X07/08 não da DWT\. 

Preencher com: \(FECEP\-ST\) / Qtde Convertida da NF de Entrada

Onde:

Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.

Campo __15\-VL\_UNIT\_FCP\_ICMS\_ST\_ESTOQUE\_CONV\_SAIDA__

Conteúdo do campo “41\-Valor Unitário FCP ICMS ST Estoque Conv” da SAFX308

RNC181\-16

__Campo 42\-Valor Unitário ICMS na Operação Conv \(VLR\_UNIT\_ICMS\_OPER\_SAI\)__

Se o campo “__%Redução BC__” da parametrização de Produto ou NCM está preenchido com valor > 0, então:

     Este campo será gerado da seguinte forma:

     \[\(Vlr Contábil – \(Vlr Contábil \* “%Redução BC” / 100\)\) \* Aliquota interna / 100\]/ QTD\_CONV

Senão:

      Este campo será gerado da seguinte forma:

      \[\(Vlr Contábil\) \* Aliquota interna / 100\] / QTD\_CONV 

Onde:

- Alíquota Interna da parametrização de Produto ou NCM sujeito ao ICMS\-ST, vigente na Data de Emissão da Saída referenciada;
- %Redução BC da parametrização de Produto ou NCM sujeito ao ICMS\-ST, vigente na Data de Emissão da Saída referenciada;
- 64\-Vlr Contabil do Item da nota de Saída referenciada;
- QTD\_CONV que foi gravada no campo __32 \- Quantidade Convertida__

\*\* 28/12: alterei pra quantidade do item da nota de SAÍDA \*\*

Campo __16\-VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV\_SAIDA__

Conteúdo do campo “42\-Valor Unitário ICMS na Operação Conv” da SAFX308

Conforme regra do Guia Prático \(campo Motivo do Ressarcimento/Complemento:

Se o terceiro caracter do Código do Motivo \(campo 31 da SAFX308\) = “__5__”, este campo não será preenchido \(“||”\)\.

RNC181\-17

__Campo 35\-Valor Unitário ICMS OP Conv \(VLR\_ICMS\_CONV\)__

Em MG preenchemos com nulo\.

Como vamos preencher para RS???

Campo __17\-VL\_UNIT\_ICMS\_OP\_CONV\_SAIDA__

Conteúdo do campo “35\-Valor Unitário ICMS OP Conv” da SAFX308

Conforme regra do Guia Prático \(campo Motivo do Ressarcimento/Complemento:

Se o terceiro caracter do Código do Motivo \(campo 31 da SAFX308\) = “__5__” ou “__6__” ou “__8__”, este campo não será preenchido \(“||”\)\.

RNC181\-18

__Campo 43\-Valor Unitário ICMS ST Conv Rest \(VLR\_UNIT\_ICMSS\_REST\_SAI\)__

Campo referente ao estorno de Complemento, logo deve ser preenchido no caso da saída referenciada ter sido objeto de Complemento\.

Se \(BC\-Ent\) > \(BC\-Sai\) então:

   Não preencher;

Se \(BC\-Ent\) < \(BC\-Sai\) então:

   Preencher com o resultado da formula:

    VLR\_UNIT\_ICMS\_OPER\_SAI \- 

    VLR\_UNIT\_ICMS\_ESTQ\_SAI \- 

    VLR\_UNIT\_ICMSS\_ESTQ\_SAI

    Onde:

- VLR\_UNIT\_ICMS\_OPER\_SAI: valor gravado no campo 42\-Valor Unitário ICMS na Operação Conv;
- VLR\_UNIT\_ICMS\_ESTQ\_SAI : valor gravado no campo 39\- Valor Unitário ICMS OP Estoque Conv;
- VLR\_UNIT\_ICMSS\_ESTQ\_SAI: valor gravado no campo 40\-Valor Unitário ICMS ST Estoque Conv;

Se \(BC\-Ent\) = \(BC\-Sai\) então:

   Não preencher

Campo __18\-VL\_UNIT\_ICMS\_ST\_CONV\_REST__

Conteúdo do campo “43\-Valor Unitário ICMS ST Conv Rest” da SAFX308

Conforme regra do Guia Prático \(campo Motivo do Ressarcimento/Complemento:

- Se o terceiro caracter do Código do Motivo \(campo 31 da SAFX308\) = “__5__” ou “__6__” ou “__7__”, este campo não será preenchido \(“||”\)\.
- Se o terceiro caracter do Código do Motivo \(campo 31 da SAFX308\) = “__8__”, este campo deve ser > zero\. Caso contrário, o campo será gerado com zero, e será gerada uma mensagem de aviso no log: “*Quando o terceiro caracter do Código do Motivo = 8, deve ser informado o valor do campo VL\_UNIT\_ICMS\_ST\_CONV\_REST”*\.

*              \(O log deve exibir os dados de identificação da nota de devolução, e também do*

*               documento de referência \(seja Nota, Cupom ou Cupom SAT\), para que o usuário*

*               possa identificar o problema\)*

RNC181\-19

__Campo 44\-Valor Unitário FCP ST Conv Rest \(VLR\_UNIT\_FCP\_REST\_SAI\)__

Campo referente ao estorno de Complemento, logo deve ser preenchido no caso da saída referenciada ter sido objeto de Complemento\.

Se \(BC\-Ent\) > \(BC\-Sai\) então:

   Não preencher;

Se \(BC\-Ent\) < \(BC\-Sai\) então:

   Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMSS\_REST\_SAI \* Alíquota FCP / 100

    Onde:

- VLR\_UNIT\_ICMSS\_REST\_SAI: valor gravado no campo 43\-Valor Unitário ICMS ST Conv Rest;
- Alíquota FCP da parametrização de Produto ou NCM sujeito ao ICMS\-ST, vigente na Data de Emissão da Saída referenciada;

Se \(BC\-Ent\) = \(BC\-Sai\) então:

   Não preencher

Campo __19\-VL\_UNIT\_FCP\_ST\_CONV\_REST__

Conteúdo do campo “44\-Valor Unitário FCP ST Conv Rest” da SAFX308

Conforme regra do Guia Prático \(campo Motivo do Ressarcimento/Complemento:

- Se o terceiro caracter do Código do Motivo \(campo 31 da SAFX308\) = “__5__” ou “__6__” ou “__7__”, este campo não será preenchido \(“||”\)\.
- Se o terceiro caracter do Código do Motivo \(campo 31 da SAFX308\) = “__8__”, e o campo na SAFX308 estiver nulo \(campo 44\), este campo será preenchido com zero\.

RNC181\-20

__Campo 45\-Valor Unitário ICMS ST Conv Compl \(VLR\_UNIT\_ICMSS\_COMPL\_SAI\)__

Campo referente ao estorno de Restituição, logo deve ser preenchido no caso da saída referenciada ter sido objeto de Restituição\.

Se \(BC\-Ent\) > \(BC\-Sai\) então:

    Preencher com o resultado da formula:

    VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ 

    VLR\_UNIT\_ICMSS\_ESTQ\_SAI – 

    VLR\_UNIT\_ICMS\_OPER\_SAI  

    Onde:

- VLR\_UNIT\_ICMS\_OPER\_SAI: valor gravado no campo 42\-Valor Unitário ICMS na Operação Conv;
- VLR\_UNIT\_ICMS\_ESTQ\_SAI : valor gravado no campo 39\- Valor Unitário ICMS OP Estoque Conv;
- VLR\_UNIT\_ICMSS\_ESTQ\_SAI: valor gravado no campo 40\-Valor Unitário ICMS ST Estoque Conv;

Se \(BC\-Ent\) < \(BC\-Sai\) então:

    Não preencher;

Se \(BC\-Ent\) = \(BC\-Sai\) então:

   Não preencher

Campo __20\-VL\_UNIT\_ICMS\_ST\_CONV\_COMPL__

Conteúdo do campo “45\-Valor Unitário ICMS ST Conv Compl” da SAFX308

Conforme regra do Guia Prático \(campo Motivo do Ressarcimento/Complemento:

- Se o terceiro caracter do Código do Motivo \(campo 31 da SAFX308\) = “__5__” ou “__8__”, este campo não será preenchido \(“||”\)\.
- Se o terceiro caracter do Código do Motivo \(campo 31 da SAFX308\) = “__6__” ou “__7__”, este campo deve ser > zero\. Caso contrário, o campo será gerado com zero, e será gerada uma mensagem de aviso no log: “*Quando o terceiro caracter do Código do Motivo = 6 ou 7, deve ser informado o valor do campo VL\_UNIT\_ICMS\_ST\_CONV\_COMPL”*\.

              *\(O log deve exibir os dados de identificação da nota de devolução, e também do*

*              documento de referência \(seja Nota, Cupom ou Cupom SAT\), para que o usuário*

*              possa identificar o problema\)*

RNC181\-21

__Campo 46\-Valor Unitário FCP ST Conv Compl \(VLR\_UNIT\_FCP\_COMPL\_SAI\)__

Campo referente ao estorno de Restituição, logo deve ser preenchido no caso da saída referenciada ter sido objeto de Restituição\.

Se \(BC\-Ent\) > \(BC\-Sai\) então:

    Preencher com o resultado da formula:

    VLR\_UNIT\_ICMSS\_COMPL\_SAI \* Alíquota FCP / 100

    Onde:

- VLR\_UNIT\_ICMSS\_COMPL\_SAI: valor gravado no campo 45\-Valor Unitário ICMS ST Conv Compl;
- Alíquota FCP da parametrização de Produto ou NCM sujeito ao ICMS\-ST, vigente na Data de Emissão da Saída referenciada;

Se \(BC\-Ent\) < \(BC\-Sai\) então:

    Não preencher;

Se \(BC\-Ent\) = \(BC\-Sai\) então:

   Não preencher

Campo __21\-VL\_UNIT\_FCP\_ST\_CONV\_COMPL__

Conteúdo do campo “46\-Valor Unitário FCP ST Conv Compl” da SAFX308

Conforme regra do Guia Prático \(campo Motivo do Ressarcimento/Complemento:

- Se o terceiro caracter do Código do Motivo \(campo 31 da SAFX308\) = “__5__” ou “__8__”, este campo não será preenchido \(“||”\)\.
- Se o terceiro caracter do Código do Motivo \(campo 31 da SAFX308\) = “__6__” ou “__7__”, e o campo na SAFX308 estiver nulo \(campo 46\), este campo será preenchido com zero\.

__Campos que não pertencem a SAFX308 mas que devem ser apresentados em relatorio de conferência, por isso a necessidade de criarmos a tabela EST\_ST\_RS\_NF\_DEV\_SAI:__

- \(BC\-Ent\) 
- \(BC\-Sai\) 
- QTD da nota de saída \(campos 24 e 137\)
- QTD devolvida da nota de saída \(safx192\)
- Unidade da nota
- Fator de conversão
- Dados da nota de entrada anterior a saída referenciada, caso quem que não existe Caso não exista registro na Tabela de Controle\.
- Aliq FCP, Interna, %Redução BC

### <a id="_Toc60126005"></a>– Geração da Devolução da Saída \(saída é Um Cupom Fiscal\) Pendente

Recuperação da nota de devolução de saída \(que é uma nota de entrada\) e das notas de saídas objetos da devolução\.

__Origem dos Dados:__ __SAFX07, SAFX117__

   \- __*Nota de entrada*__ \(MOVTO\_E\_S <> “9”\);

   \- Nota fiscal de devolução \(NORM\_DEV = “2”\);

   \- produto parametrizado;

   \- cfop / Natureza de Operação parametrizado;

   \-  modelos para geração do C181: \(01, 1B, 04, 55,65\)

   \- Recuperar as notas de saídas pelos campos de referência da SAFX08\. O documento de referência deve ser recuperado na base de dados a partir dos critérios descritos abaixo: 

\- nota fiscal de saída \(MOVTO\_E\_S  = ‘9’\);

\- Nota fiscal normal \(NORM\_DEV = “1”\);

\- número da nota = conteúdo do campo 117 da SAFX08;

\- série da nota      = conteúdo do campo 118 da SAFX08;

\- subsérie da nota = conteúdo do campo 119 da SAFX08;

\- data de emissão da nota = conteúdo do campo 102 da SAFX08;

\- produto = produto do item da nota de devolução; 

Obs: a recuperação dos documentos ficais do período pode ser feito pelas tabelas do Data Mart\. Mas a recuperação da nota referenciada, deve ser feita pela tabela definitiva X07/X08, pois essas notas podem estar em períodos anteriores, onde pode não existir informação do Data Mart\.

__Gravação da SAFX308__

__EST\_ST\_RS\_NF\_DEV\_SAI__

__Regra de geração do C181 no SPED FISCAL__

Gravar a SAFX308:

Campos 01 a 15 – Campos chave da nota de devolução de saída 

Campo 16 – preencher com 2

Campos 17 ao 23 – campos chave da nota de saída referenciada; Campo 21 deve ser preenchido com a data de emssão\.

Campo 30  \- preencher com o numero do item da nota de saída referenciada;

### <a id="_Toc60126006"></a>– Geração da Devolução da Saída \(saída é Um Cupom Fiscal SAT\) Pendente

Recuperação da nota de devolução de saída \(que é uma nota de entrada\) e das notas de saídas objetos da devolução\.

__Origem dos Dados:__ __SAFX07, SAFX117???__

   \- __*Nota de entrada*__ \(MOVTO\_E\_S <> “9”\);

   \- Nota fiscal de devolução \(NORM\_DEV = “2”\);

   \- produto parametrizado;

   \- cfop / Natureza de Operação parametrizado;

   \-  modelos para geração do C181: \(01, 1B, 04, 55,65\)

   \- Recuperar as notas de saídas pelos campos de referência da SAFX08\. O documento de referência deve ser recuperado na base de dados a partir dos critérios descritos abaixo: 

\- nota fiscal de saída \(MOVTO\_E\_S  = ‘9’\);

\- Nota fiscal normal \(NORM\_DEV = “1”\);

\- número da nota = conteúdo do campo 117 da SAFX08;

\- série da nota      = conteúdo do campo 118 da SAFX08;

\- subsérie da nota = conteúdo do campo 119 da SAFX08;

\- data de emissão da nota = conteúdo do campo 102 da SAFX08;

\- produto = produto do item da nota de devolução; 

Obs: a recuperação dos documentos ficais do período pode ser feito pelas tabelas do Data Mart\. Mas a recuperação da nota referenciada, deve ser feita pela tabela definitiva X07/X08, pois essas notas podem estar em períodos anteriores, onde pode não existir informação do Data Mart\.

__Gravação da SAFX308__

__EST\_ST\_RS\_NF\_DEV\_SAI__

__Regra de geração do C181 no SPED FISCAL__

Gravar a SAFX308:

Campos 01 a 15 – Campos chave da nota de devolução de saída 

Campo 16 – preencher com 3

Campos 17 ao 23 – campos chave da nota de saída referenciada; Campo 21 deve ser preenchido com a data de emssão\.

Campo 30  \- preencher com o numero do item da nota de saída referenciada;

### <a id="_Toc60126007"></a>– Geração da Saída \(Cupom – C480\) Pendente

Recuperação da nota de saída\.

__Origem dos Dados:__ __SAFX993, SAFX994__ 

   \- __*Nota de saída*__ \(MOVTO\_E\_S = “9”\);

   \- Nota fiscal de devolução \(NORM\_DEV = “1”\);

   \- produto parametrizado;

   \- cfop / Natureza de Operação parametrizado;

   \-  modelos para geração do C480: \(01, 1B, 04, 55,65\)

### <a id="_Toc60126008"></a>– Geração da Saída \(NF\)

Recuperação da nota de saída\.

__Origem dos Dados:__ __SAFX07, SAFX08__ 

   \- __*Nota de saída*__ \(MOVTO\_E\_S = “9”\);

   \- Nota fiscal de devolução \(NORM\_DEV = “1”\);

   \- produto parametrizado;

   \- cfop / Natureza de Operação parametrizado;

   \-  modelos para geração do C185: \(01, 1B, 04, 55,65\)

__Gravação da SAFX296__

__EST\_ST\_RS\_NF\_SAI__

__Regra de geração do C185 no SPED FISCAL__

RNC185

Gravar a SAFX296 \- Informações Complementares das Operações Sujeitas ao ST \(C180, C185 e C380\)

Campos 01 a 15 – Campos chave da nota de saída 

__Novo registro da versão 1\.13, Jan/2020 \(MFS33219\)\.__

__\[MFS35492\] Alterada__

Este registro é “filho” do C100, e seu objetivo é demonstrar as informações complementares das operações de saída referentes à substituição tributária\.  

Origem dos Dados: SAFX296 \(Informações Complementares das Operações Sujeitas ao ST \(C180, C185 e C380\)\)

Critérios para recuperação dos documentos:

Recuperar os registros da SAFX296 a partir das informações da SAFX07 do registro pai, C100\.

RNC185\-02

__Campo: 02 \- NUM\_ITEM__

RNC185\-03

Campo: COD\_ITEM

????

Se trabalharmos com produto associado, e a nota fiscal ser referenciar a um produto associado, apresento qual código?  O código do produto principal?

__Campo: 03 \- COD\_ITEM__

Este campo deve ser preenchido com o código do item dos cupons fiscais agrupados pela combinação de código do Item, Unidade de Medida, CST e CFOP\.

Deve ser gravado um registro 0200 para o código do item informado neste campo\. 

OBS1: Observar regra de gravação do código do item no registro 0200 \(concatenar indicador \+ código do item conforme regra de gravação do COD\_ITEM\)\.

Se parâmetro ‘Considerar o Indicador no Código do Item’, não concatenar o código, utilizando a mesma regra descrita no campo 02 do registro 0200\.

RNC185\-04

__Campo: 04\-CST\_ICMS__

Preencher com os campos 30\-Cód Situação Tribut A \+31\-Cód Situação Tribut B da SAFX08

RNC185\-05

__Campo 05\-CFOP__

Preencher com o campo 22\-Código Fiscal da SAFX08

RNC185\-06

__Campo 24 \- Código Motivo \(Saídas\) \(COD\_MOTIVO\_SAI\)__

??????

Se basearmos na regra de MG, para saber se houve ressarcimento ou complemento na operação de saída, comparar:

Se \(BC\-Ent\) > \(BC\-Sai\) então:

   A saída obteve Restituição;

   RS100

Se \(BC\-Ent\) < \(BC\-Sai\) então:

   A saída obteve Complemento;

   RS300

Se \(BC\-Ent\) = \(BC\-Sai\) então:

   A saída não teve nem Restituição nem Complemento\.

  RS000

Onde:

- \(BC\-Ent\) Valor unitário médio móvel calculado da BC ICMS\-ST recuperado da Tabela de Controle considerando o Produto e a Data de Emissão da nota de saída\.

*\(ver OBS sobre os produtos associados, pois os valores medios estariam no produto principal\)*

- \(BC\-Sai\) Valor Unitário da BC do ICMS na Operação Conv, calculada conforme regra:

Se o campo “__%Redução BC__” da parametrização de Produto ou NCM está preenchido com valor > 0, então:

     Este campo será gerado da seguinte forma:

     \[\(Vlr Contábil – \(Vlr Contábil \* “%Redução BC” / 100\)\)\]/ QTD\_CONV

Senão:

      Este campo será gerado da seguinte forma:

      \[\(Vlr Contábil\)\] / QTD\_CONV 

Onde:

- %Redução BC da parametrização de Produto ou NCM sujeito ao ICMS\-ST, vigente na Data de Emissão da Saída;
- 64\-Vlr Contabil do Item da nota de saída;
- QTD\_CONV que foi gravada no campo __16 \- Quantidade Convertida__

__Campo 06\-COD\_MOT\_REST\_COMPL:__

Preencher com o campo 24\-Código Motivo \(Saídas\) da SAFX296

RNC185\-07

__Campo 16 \- Quantidade Convertida \(QTD\_CONV\)__

Campo 24\-Quantidade do Item da nota de Saída, aplicando a conversão, quando necessário\. Veja:

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\)  __*\(ver OBS abaixo sobre os produtos associados\)*

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria quantidade do item da nota;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\)

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade Convertida”;

     Senão         

         Nesse caso a quantidade do item \(SAFX08\) será convertida para a unidade de medida do cadastro do produto;

         \[ Quantidade do item da nota \(SAFX08\) \* Fator de Conversão \]

__Sobre os produtos associados:__ Quando se tratar de uma nota fiscal de produto “associado”, a comparação será feita da unidade de medida da nota, com a __unidade do produto principal__\.

Exemplo:

__Produto principal__: COCA\-COLA PET                 \(unidade de medida do estoque – SAFX2013 = UN\) 

__Produtos associados__: COCA\-COLA PET–1      \(unidade de medida do estoque – SAFX2013 = PAC \(6 unidades\)\)

Nota de venda do produto associado: __COCA\-COLA PET\-1__, unidade da nota = PAC, Quantidade = __5__

Compara a unidade de medida da nota do produto associado com a unidade de estoque do produto principal: PAC x UN

Como é diferente, deve\-se converter a quantidade da nota de PAC para UN\. 

Para acessar a tabela de conversão por produto, será utilizado o código do produto principal:

__DWT\_CONV\_MEDIDA\-2: __Produto = __COCA\-COLA PET__

                                          Unidade Origem = PAC

                                          Unidade Destino = UN

                                          Fator de conversão = 6,0000

Conversão da quantidade da nota do associado:  QTD da nota x Fator de Conversão   =  5 x 6,0000 = 30,0000 

Lembrando que, quando não existe fator na tabela de conversão por produto \(DWT\_CONV\_MEDIDA\_2\), será utilizada a tabela padrão \(DWT\_CONV\_MEDIDA\)\.  

__= = = = =__

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o item da nota será gerado com o campo Quantidade da Saída sem informação, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. O item do documento será gerado sem a informação da quantidade e do valor unitário”*

* *\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item do documento, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

__Campo 07\-QUANT\_CONV__

RNC185\-08

__Campo 17 \- Unidade de Medida __

Unidade de Medida do Produto\. Campo “14\-Código de Medida” da SAFX2013 \(unidade da SAFX2007\);

*\(ver OBS sobre os produtos associados\)*

__Campo: 08\-UNID__

Deve ser gravado um registro 0190 para a Unidade de Medida informada neste campo\. 

Caso a unidade de medida informada seja diferente da unidade de medida informada no Registro 0200, deverá ser gerado um registro 0220 com o fator de conversão entre as unidades de medidas\. 

RNC185\-09

__Campo 18\-Valor Unitário Conv \(VLR\_UNIT\_CONV\)__

  VLR\_UNIT\_CONV = VLR\_CONTAB\_ITEM da SAFX08 / QTD\_CONV

Onde:

- VLR\_CONTAB\_ITEM é o campo 64\-Valor Contabil do Item da nota de saída;
- QTD\_CONV que foi gravada no campo __16 \- Quantidade Convertida__

__Pode ser alterado pelo Carrefour – MFS57863__

__Campo: 09\-VL\_UNIT\_CONV__

Campo 18\-Valor Unitário Conv\. da SAFX296

RNC185\-10

__Campo 19 \- Valor Unitário ICMS Conv \(VLR\_ICMS\_CONV\)__

Se o campo “__%Redução BC__” da parametrização de Produto ou NCM está preenchido com valor > 0, então:

     Este campo será gerado da seguinte forma:

     \(Vlr Contábil – \(Vlr Contábil \* “%Redução BC” / 100\)\) \* Aliquota interna / 100\]/ QTD\_CONV

Senão:

      Este campo será gerado da seguinte forma:

      \(Vlr Contábil\) \* Aliquota interna / 100\] / QTD\_CONV 

Onde:

- Alíquota Interna da parametrização de Produto ou NCM sujeito ao ICMS\-ST, vigente na Data de Emissão da Saída;
- %Redução BC da parametrização de Produto ou NCM sujeito ao ICMS\-ST, vigente na Data de Emissão da Saída;
- 64\-Vlr Contabil do Item da nota de saída;
- QTD\_CONV que foi gravada no campo __16 \- Quantidade Convertida__

__Campo: 10\-VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV __

\[MFS47079\]

Se UF do Estabelecimento = “__MG__” e campo 06 – COD\_MOT\_REST\_COMP = ‘__MG200’__, então:

   Gerar este campo vazio ‘||’

Senão

  Considerar a informação do Campo 19 \- VLR\_ICMS\_CONV da SAFX296

RNC185\-11

__Campo 25\-Valor Unitário ICMS na Oper Conv \(Saídas\) \(VLR\_UNIT\_ICMS\_OPER\_SAI\)__

Em MG preenchemos com nulo\.

Como vamos preencher para RS???

Na IN RE096/20 operações referentes aos art\. 22, 23, diz para gravar esse campo\.

__Campo: 11\-VL\_UNIT\_ICMS\_OP\_CONV__

\[MFS39301\] 

Se UF do Estabelecimento = “__MG__” então:

  Gerar este campo vazio ‘||’

Senão:

  Considerar a informação do Campo 25\-Valor Unitário ICMS na Oper\. Conv\. \(Saídas\) 

  da SAFX296\.

RNC185\-12

__Campo 26\-Valor Unitário ICMS Estoque Conv \(Saídas\) \(VLR\_UNIT\_ICMS\_ESTQ\_SAI\)__

Valor Unitário Médio Móvel Calculado para o __ICMS__ recuperado da Tabela de Controle considerando:

\- Produto e a Data de Emissão da nota de saída referenciada\.

*\(ver OBS sobre os produtos associados, pois os valores medios estariam no produto principal\)*

__Campo: 12\-__ __VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV__

26\-Valor Unitário ICMS Estoque Conv\. \(Saídas\)

RNC185\-13

__Campo 27\-Valor Unitário ICMS\-ST Estoque Conv \(Saídas\) \(VLR\_UNIT\_ICMSS\_ESTQ\_SAI\)__

Valor unitário médio móvel calculado para os __ICMS\-ST__ \+ __FECP\_ICMS\_ST__ \(\*\) recuperado da Tabela de Controle considerando:

\- Produto e a Data de Emissão da nota de saída referenciada\.

*\(ver OBS sobre os produtos associados, pois os valores medios estariam no produto principal\)*

\(\*\) Pelo guia prático esse campo corresponde ao VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV preenchido na ocasião da saída \(c185\), que é preenchido com ICMS ST incluindo FCP ST\.

__\(\*\) Faz sentido a gente inserir o parametro FECP embutido\.__

Na IN087/20 tópico 19\.3\-A\.2\.2\.1:

2 \- ao valor unitário médio móvel calculado ao fim do dia em que ocorreu a saída objeto de devolução ou retorno deverão corresponder às registradas no campo VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\_SAIDA dos registros C181 do dia\.

__Campo 13 \- VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV__

27\-Valor Unitário ICMS\-ST Estoque Conv\. \(Saídas\)

RNC185\-14

__Campo 28\-Valor Unitário FCP\-ST Estoque Conv\. \(Saídas\) \(VLR\_UNIT\_FCP\_ESTQ\_SAI\)__

Valor Unitário Médio Móvel Calculado para o FECP\_ICMS\_ST recuperado da Tabela de Controle considerando:

\- Produto e a Data de Emissão da nota de saída referenciada\.

*\(ver OBS sobre os produtos associados, pois os valores medios estariam no produto principal\)*

__Campo 14 \- VL\_UNIT\_FCP\_ICMS\_ST\_ESTOQUE\_CONV__

28\-Valor Unitário FCP\-ST Estoque Conv\. \(Saídas\)

RNC185\-15

__Campo 29\-Valor Unitário ICMS\-ST Conv\. Rest\. \(Saídas\) \(VLR\_UNIT\_ICMSS\_REST\_SAI\)__

Campo deve ser preenchido no caso da saída seja objeto de Restituição\.

Se \(BC\-Ent\) > \(BC\-Sai\) então:

    Preencher com o resultado da formula:

    VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ 

    VLR\_UNIT\_ICMSS\_ESTQ\_SAI \- 

    VLR\_ICMS\_CONV

    Onde:

- VLR\_ICMS\_CONV: valor gravado no campo 19 \- Valor Unitário ICMS Conv;
- VLR\_UNIT\_ICMS\_ESTQ\_SAI: valor gravado no campo 26\-Valor Unitário ICMS Estoque Conv \(Saídas\);
- VLR\_UNIT\_ICMSS\_ESTQ\_SAI: valor gravado no campo 27\-Valor Unitário ICMS\-ST Estoque Conv \(Saídas\);

Se \(BC\-Ent\) < \(BC\-Sai\) então:

    Não preencher;

Se \(BC\-Ent\) = \(BC\-Sai\) então:

   Não preencher

No ressarcimento MG essa regra foi questionada pelo Claudio \(MFS\-48892\), mas mantivemos nossa regra \(passei email para Can, mas como o problema do cliente se resolveu pois tratamos o valor do ICMS com o campo 225, eles não voltaram a questionar a regra\.

__Campo: 15\-VL\_UNIT\_ICMS\_ST\_CONV\_REST__

\[MFS39301\] 

__Se UF do Estabelecimento = “MG”, então:__

Se o campo 06 \- COD\_MOT\_REST\_COMPL  estiver preenchido com ‘__MG100’ __gerar com o campo 29\-Valor Unitário ICMS\-ST Conv\. Rest\. \(Saídas\) da SAFX296\. Caso o campo esteja sem informação, gerar zero\.

\[MFS47079\]

Se o campo 06 \- COD\_MOT\_REST\_COMPL  estiver preenchido com __MG200__ gerar com o campo 29\-Valor Unitário ICMS\-ST Conv\. Rest\. \(Saídas\) da SAFX296\. Caso o campo esteja sem informação, gerar zero\.

Se o campo 06 \- COD\_MOT\_REST\_COMPL  estiver preenchido com ‘__MG300’__, gerar este campo vazio ‘||’\.

Senão:

  Considerar a informação do Campo 29\-Valor Unitário ICMS\-ST Conv\. Rest\. \(Saídas\) 

  da SAFX296\.

RNC185\-16

__Campo 30\-Valor Unitário FCP\-ST Conv\. Rest\. \(Saídas\) \(VLR\_UNIT\_FCP\_REST\_SAI\)__

Campo deve ser preenchido no caso da saída seja objeto de Restituição\.

Se \(BC\-Ent\) > \(BC\-Sai\) então:

    Preencher com o resultado da formula:

    VLR\_UNIT\_ICMSS\_REST\_SAI \* Alíquota FCP / 100

    Onde:

- VLR\_UNIT\_ICMSS\_REST\_SAI: valor gravado no campo 29\-Valor Unitário ICMS ST Conv Rest;
- Alíquota FCP da parametrização de Produto ou NCM sujeito ao ICMS\-ST, vigente na Data de Emissão da Saída;

Se \(BC\-Ent\) < \(BC\-Sai\) então:

    Não preencher;

Se \(BC\-Ent\) = \(BC\-Sai\) então:

   Não preencher

__Campo: 16\-__ __VL\_UNIT\_FCP\_ST\_CONV\_REST__

\[MFS39301\]  

__Se UF do Estabelecimento = “MG”, então:__

Se o campo 06 \- COD\_MOT\_REST\_COMPL  estiver preenchido com ‘__MG100’__ gerar com o campo 30\-Valor Unitário FCP\-ST Conv\. Rest\. \(Saídas\) da SAFX296\. Caso o campo esteja sem informação, gerar zero\.

\[MFS47079\]

Se o campo 06 \- COD\_MOT\_REST\_COMPL  estiver preenchido com __MG200__, gerar com o campo 30\-Valor Unitário FCP\-ST Conv\. Rest\. \(Saídas\) da SAFX296\. Caso o campo esteja sem informação, gerar zero\.

Se o campo 06 \- COD\_MOT\_REST\_COMPL  estiver preenchido com ‘__MG300’__, gerar este campo vazio ‘||’\.

Senão:

  Considerar a informação do Campo 30\-Valor Unitário FCP\-ST Conv\. Rest\. \(Saídas\) 

  da SAFX296\.

RNC185\-17

__Campo 31\-Valor Unitário ICMS\-ST Conv Compl\. \(Saídas\) \(VLR\_UNIT\_ICMSS\_COMPL\_SAI\)__

Campo deve ser preenchido no caso da saída seja objeto de Complementação\.

Se \(BC\-Ent\) > \(BC\-Sai\) então:

    Não preencher;

Se \(BC\-Ent\) < \(BC\-Sai\) então:

    Preencher com o resultado da formula:

    VLR\_ICMS\_CONV \-

    VLR\_UNIT\_ICMS\_ESTQ\_SAI \- 

    VLR\_UNIT\_ICMSS\_ESTQ\_SAI  

    

    Onde:

- VLR\_ICMS\_CONV: valor gravado no campo 19 \- Valor Unitário ICMS Conv;
- VLR\_UNIT\_ICMS\_ESTQ\_SAI: valor gravado no campo 26\-Valor Unitário ICMS Estoque Conv \(Saídas\);
- VLR\_UNIT\_ICMSS\_ESTQ\_SAI: valor gravado no campo 27\-Valor Unitário ICMS\-ST Estoque Conv \(Saídas\);

Se \(BC\-Ent\) = \(BC\-Sai\) então:

   Não preencher

__Campo: 17\-VL\_UNIT\_ICMS\_ST\_CON V\_COMPL__

\[MFS39301\] 

__Se UF do Estabelecimento = “MG”, então:__

Se o campo 06 \- COD\_MOT\_REST\_COMPL  estiver preenchido com ‘__MG100’__ gerar este campo vazio ‘||’\.

\[MFS47079\]

Se o campo 06 \- COD\_MOT\_REST\_COMPL  estiver preenchido com ‘__MG200’__ gerar este campo vazio ‘||’\.

Se o campo 06 \- COD\_MOT\_REST\_COMPL  estiver preenchido com ‘__MG300’__, gerar com o campo 31\-Valor Unitário ICMS\-ST Conv\. Compl\. \(Saídas\) da SAFX296\. Caso o campo esteja sem informação, gerar zero\.

Senão:

  Considerar a informação do Campo 31\-Valor Unitário ICMS\-ST Conv\. Compl\. \(Saídas\) 

  da SAFX296\.

RNC185\-18

__Campo 32\-Valor Unitário FCP\-ST Conv Compl \(Saídas\) \(VLR\_UNIT\_FCP\_COMPL\_SAI\)__

Campo deve ser preenchido no caso da saída seja objeto de Complementação\.

Se \(BC\-Ent\) > \(BC\-Sai\) então:

    Não preencher;

Se \(BC\-Ent\) < \(BC\-Sai\) então:

    Preencher com o resultado da formula:

    VLR\_UNIT\_ICMSS\_COMPL\_SAI \* Alíquota FCP / 100

    Onde:

- VLR\_UNIT\_ICMSS\_C0MPL\_SAI: valor gravado no campo 31\-Valor Unitário ICMS ST Conv Rest;
- Alíquota FCP da parametrização de Produto ou NCM sujeito ao ICMS\-ST, vigente na Data de Emissão da Saída;

   

Se \(BC\-Ent\) = \(BC\-Sai\) então:

   Não preencher

__Campo: 18\-VL\_UNIT\_FCP\_ST\_CONV \_COMPL__

MFS39301\] 

__Se UF do Estabelecimento = “MG”, então:__

Se o campo 06 \- COD\_MOT\_REST\_COMPL  estiver preenchido com ‘__MG100’__ gerar este campo vazio ‘||’\.

\[MFS47079\]

Se o campo 06 \- COD\_MOT\_REST\_COMPL  estiver preenchido com ‘__MG200’__ gerar este campo vazio ‘||’\.

Se o campo 06 \- COD\_MOT\_REST\_COMPL  estiver preenchido com ‘__MG300’__, gerar com o campo 32\-Valor Unitário FCP\-ST Conv\. Compl\. \(Saídas\) da SAFX296\. Caso o campo esteja sem informação, gerar zero\.

Senão:

  Considerar a informação do Campo 32\-Valor Unitário FCP\-ST Conv\. Compl\. \(Saídas\) 

  da SAFX296\.

__Campos que não pertencem a SAFX296 mas que devem ser apresentados em relatorio de conferência:__

- \(BC\-Ent\) 
- \(BC\-Sai\) 
- Aliq FCP

__DEVOLUÇÃO DE SAÍDA:__

__19\.3\-A\.1\.5__ \-No registro C181, são de preenchimento obrigatório os campos VL\_UNIT\_CONV\_SAIDA, VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV\_SAIDA, VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\_SAIDA, VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV\_SAIDA, que devem ser informados com os valores que constaram nos campos VL\_UNIT\_CONV, VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV, VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV, VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV, respectivamente, do registro C185 por ocasião da venda objeto de devolução\. \(Acrescentado pela [IN RE 087/20](http://www.legislacao.sefaz.rs.gov.br/Site/Document.aspx?inpKey=275375), de 03/11/20\. \(DOE 04/11/20\) \- Efeitos a partir de 04/11/20\.\)\.

__19\.3\-A\.1\.5\.1__ \-Se a venda objeto de devolução ou retorno ocorreu antes de 1º de janeiro de 2021, para o preenchimento dos campos: \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)\.

a\)VL\_UNIT\_CONV\_SAIDA, deverá ser utilizado o valor unitário da mercadoria constante no documento fiscal da saída objeto da devolução ou retorno; \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)

b\)VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV\_SAIDA, deverá ser utilizado o valor unitário do ICMS que o contribuinte teria se creditado referente ao último recebimento da mercadoria pelo estabelecimento, antes da saída objeto da devolução ou retorno, caso a mercadoria estivesse submetida ao regime normal de tributação; \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)

c\)VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\_SAIDA, deverá ser utilizado o valor unitário do ICMS\-ST constante no documento fiscal do último recebimento da mercadoria pelo estabelecimento antes da saída objeto da devolução ou retorno; \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)

d\)VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV\_SAIDA, deverá ser utilizado o montante do imposto efetivo informado no campo VL\_AJ\_APUR, conforme subitem 19\.2\.2, "a", ou 19\.3\.1, "a", conforme o caso\. \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)

VLR\_AJUSTE = VLR\_ICMS \+ VLR\_FECP\_ICMS\_ST \(unitário, então tem que dividir pela quantidade\) considerar parametro FECEP embutido

__19\.3\-A\.1\.5\.1\.1__ \-Para efeitos do disposto no subitem 19\.3\-A\.2\.2, "b", a multiplicação da quantidade de mercadorias de cada devolução ou retorno, informada no campo QUANT\_CONV do registro C181, deverá ser realizada, em substituição ao valor unitário médio móvel calculado ao fim do dia em que ocorreu a saída objeto de devolução ou retorno, pelo resultado da soma dos valores informados nas alíneas "b" e "c" do subitem 19\.3\-A\.1\.5\.1, dividida pela alíquota informada no campo ALIQ\_ICMS do registro 0200, expressa em notação decimal\. \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)

__DEVOLUÇÃO DE ENTRADA:__

__19\.3\-A\.1\.4__ \-No registro C186, são de preenchimento obrigatório os campos VL\_UNIT\_CONV\_ENTRADA, VL\_UNIT\_ICMS\_OP\_CONV\_ENTRADA, VL\_UNIT\_BC\_ICMS\_ST\_CONV\_ENTRADA e VL\_UNIT\_ICMS\_ST\_CONV\_ENTRADA, que devem ser informados com os valores que constaram nos campos VL\_UNIT\_CONV, VL\_UNIT\_ICMS\_OP\_CONV, VL\_UNIT\_BC\_ICMS\_ST\_CONV e VL\_UNIT\_ICMS\_ST\_CONV, respectivamente, do registro C180 por ocasião da entrada objeto de devolução\. \(Acrescentado pela [IN RE 087/20](http://www.legislacao.sefaz.rs.gov.br/Site/Document.aspx?inpKey=275375), de 03/11/20\. \(DOE 04/11/20\) \- Efeitos a partir de 04/11/20\.\)

__19\.3\-A\.1\.4\.1__ \-Se a entrada objeto de devolução ocorreu antes de 1º de janeiro de 2021, para o preenchimento dos campos: \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)

a\)VL\_UNIT\_CONV\_ENTRADA, deverá ser utilizado o resultado da multiplicação do valor informado no campo VL\_BC\_ICMS\_ST pelo resultado da divisão do valor informado no campo VL\_ICMS\_OP pelo total da soma dos valores informados nos campos VL\_ICMS\_OP e VL\_ICMS\_ST, todos os campos do registro __H030,__ informado conforme o subitem 19\.3\-A\.3; \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)

b\)VL\_UNIT\_ICMS\_OP\_CONV\_ENTRADA, deverá ser utilizado o valor informado no campo VL\_ICMS\_OP do registro H030, informado conforme o subitem 19\.3\-A\.3; \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)

c\)VL\_UNIT\_BC\_ICMS\_ST\_CONV\_ENTRADA, deverá ser utilizado o valor informado no campo VL\_BC\_ICMS\_ST do registro H030, informado conforme o subitem 19\.3\-A\.3; \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)

d\)VL\_UNIT\_ICMS\_ST\_CONV\_ENTRADA, deverá ser utilizado o valor informado no campo VL\_ICMS\_ST do registro H030, informado conforme o subitem 19\.3\-A\.3\. \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)

19\.3\-A\.3 estoque no fim do dia 31 de dezembro de 2020 ou do dia anterior àquele em que passar a apurar o ajuste, se posterior a 1º de janeiro de 2021\.

### <a id="_Toc60126009"></a>– Geração da Entrada

Recuperação da nota de entrada\.

__Origem dos Dados:__ __SAFX07, SAFX08__ 

   \- __*Nota de saída*__ \(MOVTO\_E\_S <> “9”\);

   \- Nota fiscal de devolução \(NORM\_DEV = “1”\);

   \- produto parametrizado;

   \- cfop / Natureza de Operação parametrizado;

   \-  modelos para geração do C180: \(01, 1B, 04, 55,65\)

__Gravação da SAFX296__

__EST\_ST\_RS\_NF\_ENT__

__Regra de geração do C180 no SPED FISCAL__

RNC180

Gravar a SAFX296 \- Informações Complementares das Operações Sujeitas ao ST \(C180, C185 e C380\)

Campos 01 a 15 – Campos chave da nota de entrada 

__Novo registro da versão 1\.13, Jan/2020 \(MFS33218\)\.__

Este registro é “filho” do C170, e seu objetivo é demonstrar as informações complementares das operações de entrada referentes à substituição tributária\.  

Origem dos Dados: SAFX296 \(Informações Complementares das Operações Sujeitas ao ST \(C180, C185 e C380\)\)

Critérios para recuperação dos documentos:

Recuperar os registros da SAFX296 a partir das informações da SAFX08 do registro pai, C170\.

RNC180\-02

Campo 20\-Responsável Retenção \(Entradas\) \(IND\_RESP\_RET\_ENT\) 

Este campo será preenchido de acordo com os campos 131\- Indicador de ICMS\-ST e 132 – Situação Especial – Substituição Tributária que estiver preenchido na SAFX08 \(referente ao item de entrada recuperado\)\. De acordo com as regras abaixo:

Se campo “132 – Situação Especial – Substituição Tributária” igual a ‘1’, então:

   O campo será preenchido com o valor igual a “3” – Próprio Declarante

Senão

     Se campo “131\- Indicador de ICMS\-ST” igual a ‘1’, então:

         O campo será preenchido com o valor igual a “1” – Remetente Direto

     Se campo “131\- Indicador de ICMS\-ST” igual a ‘2’, então:

         O campo será preenchido com o valor igual a “2” – Remetente Indireto

Campo 02 \- COD\_RESP\_RET

Preencher com o conteúdo do campo 20\-Responsável Retenção \(Entradas\) da SAFX296

RNC180\-03

Campo 16\-Quantidade Convertida \(QTD\_CONV\)

Campo 24\-Quantidade do Item da nota de Entrada, aplicando a conversão, quando necessário\. Veja:

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\)  __*\(ver OBS abaixo sobre os produtos associados\)*

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria quantidade do item da nota;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\)

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade Convertida”;

     Senão         

         Nesse caso a quantidade do item \(SAFX08\) será convertida para a unidade de medida do cadastro do produto;

         \[ Quantidade do item da nota \(SAFX08\) \* Fator de Conversão \]

__Sobre os produtos associados:__ Quando se tratar de uma nota fiscal de produto “associado”, a comparação será feita da unidade de medida da nota, com a __unidade do produto principal__\.

Exemplo:

__Produto principal__: COCA\-COLA PET                 \(unidade de medida do estoque – SAFX2013 = UN\) 

__Produtos associados__: COCA\-COLA PET–1      \(unidade de medida do estoque – SAFX2013 = PAC \(6 unidades\)\)

Nota de venda do produto associado: __COCA\-COLA PET\-1__, unidade da nota = PAC, Quantidade = __5__

Compara a unidade de medida da nota do produto associado com a unidade de estoque do produto principal: PAC x UN

Como é diferente, deve\-se converter a quantidade da nota de PAC para UN\. 

Para acessar a tabela de conversão por produto, será utilizado o código do produto principal:

__DWT\_CONV\_MEDIDA\-2: __Produto = __COCA\-COLA PET__

                                          Unidade Origem = PAC

                                          Unidade Destino = UN

                                          Fator de conversão = 6,0000

Conversão da quantidade da nota do associado:  QTD da nota x Fator de Conversão   =  5 x 6,0000 = 30,0000 

Lembrando que, quando não existe fator na tabela de conversão por produto \(DWT\_CONV\_MEDIDA\_2\), será utilizada a tabela padrão \(DWT\_CONV\_MEDIDA\)\.  

__= = = = =__

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o item da nota será gerado com o campo Quantidade da Saída sem informação, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. O item do documento será gerado sem a informação da quantidade e do valor unitário”*

* *\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item do documento, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

Campo 03 \- QUANT\_CONV

Preencher com o conteúdo do campo 16\-Quantidade Convertida da SAFX296

RNC180\-04

Campo 17\- Unidade de Medida \(COD\_MEDIDA\)

Unidade de Medida do Produto\. Campo “14\-Código de Medida” da SAFX2013 \(unidade da SAFX2007\);

*\(ver OBS sobre os produtos associados\)*

Campo 04 – UNID

Preencher com o conteúdo do campo 17\- Unidade de Medida \(COD\_MEDIDA\) da SAFX296

Deve ser gravado um registro 0190 para a Unidade de Medida informada neste campo\. 

Caso a unidade de medida informada seja diferente da unidade de medida informada no Registro 0200, deverá ser gerado um registro 0220 com o fator de conversão entre as unidades de medidas\.

RNC180\-05

Campo 18\-Valor Unitário Conv\. \(VLR\_UNIT\_CONV\)

  VLR\_UNIT\_CONV = VLR\_CONTAB\_ITEM da SAFX08 / QTD\_CONV

Onde:

- VLR\_CONTAB\_ITEM é o campo 64\-valor Contabil do Item da nota de entrada;
- QTD\_CONV que foi gravada no campo __16 \- Quantidade Convertida__

Sendo revisado pelo CARREFOUR – MFS\-57863

Campo 05 \- Valor Unitário Conv\.

Preencher com o conteúdo do campo 18\-Valor Unitário Conv\. \(VLR\_UNIT\_CONV\) da SAFX296

RNC180\-06

Campo 19 \- VLR\_ICMS\_CONV \(VLR\_ICMS\_CONV\)

Preencher com: Valor do ICMS / QTD\_CONV

Onde:

- Valor do ICMS é oriundo de um dos três campos SAFX08, dependendo de qual esteja preenchido:

Campo “43\-Valor ICMS”, se preenchido, ou

   Campo “80\-ICMS não Escriturado”, se preenchido, ou

       Campo “225\-Valor ICMS Não Destacado”  

- QTD\_CONV que foi gravada no campo __16 \- Quantidade Convertida__

Campo: 06\-__VL\_UNIT\_ICMS\_OP\_CONV__

Preencher com o conteúdo do campo 19 \- VLR\_ICMS\_CONV \(VLR\_ICMS\_CONV\) da SAFX296

RNC180\-07

Campo 21\-Valor Unitário BC ICMS\-ST Conv\. \(Entradas\) \(VLR\_UNIT\_BC\_ICMSS\_ENT\)

Preencher com: Valor da BC\-ST / QTD\_CONV

Onde:

- Valor da BC\-ST é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor da BC\-ST = 61\-BASE\_SUB\_TRIB\_ICMS\.

Senão: 

Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

   Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

Senão:

Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então:

   Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

Senão:

Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, então:

   Valor da BC\-ST = 106 \- VLR\_BASE\_ICMS\_ORIG

- QTD\_CONV que foi gravada no campo __16 \- Quantidade Convertida__

Validação

Considerando os campos 61\-BASE\_SUB\_TRIB\_ICMS , 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT, 106 \- VLR\_BASE\_ICMS\_ORIG, se no mesmo item de nota, dois ou mais desses campos estiverem preenchidos, gravar  zero neste campo e exibir a mensagem no log :” O campo Valor Unitário BC ICMS\-ST Conv\. \(Entradas\) foi gerado com zero, pois existe mais de um campo de Base de ICMS – ST com valor preenchido na nota”\. 

No log deve constar esses campos com os respectivos valores e os campos identificadores da nota\.

Campo: 07 \- VL\_UNIT\_BC\_ICMS\_ST\_CONV

Preencher com o conteúdo do campo 21\-Valor Unitário BC ICMS\-ST Conv\. \(Entradas\)\) da SAFX296

RNC180\-08

Campo 22\-Valor Unitário ICMS\-ST Conv\.  \(Entradas\) \(VLR\_UNIT\_ICMSS\_CONV\_ENT\)

__\(\*\) Faz sentido a gente inserir o parametro FECP embutido\.__

Preencher com: \(Valor do ICMS\-ST \+ FECEP\-ST\)/ QTD\_CONV

Onde:

- Valor do ICMS\-ST é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

   Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

Senão:

Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então:

   Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

Senão:

Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, então:

   Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.
- QTD\_CONV que foi gravada no campo __16 \- Quantidade Convertida__

Validação

Considerando os campos 52\-VLR\_SUBST\_ICMS , 145 \- VLR\_ICMSS\_N\_ESCRIT, 133\- VLR\_ICMSS\_NDESTAC , 107\- VLR\_TRIB\_ICMS\_ORIG, se no mesmo item de nota, dois ou mais desses campos estiverem preenchidos, gravar  zero neste campo e exibir a mensagem no log :” O campo Valor Unitário ICMS\-ST Conv\.  \(Entradas\) foi gerado com zero, pois existe mais de um campo de Valor ICMS – ST com valor preenchido na nota”\. 

No log deve constar esses campos com os respectivos valores e os campos identificadores da nota\.

Campo: 08\-VL\_UNIT\_ICMS\_ST\_CONV

Preencher com o conteúdo do campo 22\-Valor Unitário ICMS\-ST Conv\.  \(Entradas\)da SAFX296

RNC180\-09

Campo 23\-Valor Unitário FCP\-ST Conv\.  \(Entradas\) \(VLR\_UNIT\_FCP\_CONV\_ENT\)

Preencher com: FECEP\-ST/ QTD\_CONV

Onde:

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.
- QTD\_CONV que foi gravada no campo __16 \- Quantidade Convertida__

Campo: 09\-VL\_UNIT\_FCP\_ST\_CONV

Preencher com o conteúdo do campo 23\-Valor Unitário FCP\-ST Conv\.  \(Entradas\) da SAFX296

RNC180\-10

Campo: 10\-COD\_DA

Preencher com o conteúdo do campo 235\-Código do Modelo do Documento de Arrecadação da SAFX08

RNC180\-11

Campo: 10\-COD\_DA

Preencher com o conteúdo do campo 236\-Número do Documento de Arrecadação da SAFX08

__Campos que não pertencem a SAFX296 mas que devem ser apresentados em relatorio de conferência:__

- \(BC\-Ent\) 
- \(BC\-Sai\) 
- Aliq FCP

### <a id="_Toc60126010"></a>– Geração da Devolução da Entrada

Recuperação da nota de devolução de entrada \(que é uma nota de saída\) e das notas de entradas objetos da devolução\.

__Origem dos Dados:__ __SAFX07, SAFX08__ 

   \- __*Nota de entrada*__ \(MOVTO\_E\_S = “9”\);

   \- Nota fiscal de devolução \(NORM\_DEV = “2”\);

   \- produto parametrizado;

   \- cfop / Natureza de Operação parametrizado;

   \-  modelos para geração do C186: \(01, 1B, 04, 55, 65\)

   \- Recuperar as notas de saídas pelos campos de referência da SAFX08\. O documento de referência deve ser recuperado na base de dados a partir dos critérios descritos abaixo: 

\- nota fiscal de entradas \(MOVTO\_E\_S  <> ‘9’\);

\- Nota fiscal normal \(NORM\_DEV = “1”\);

\- número da nota = conteúdo do campo 117 da SAFX08;

\- série da nota      = conteúdo do campo 118 da SAFX08;

\- subsérie da nota = conteúdo do campo 119 da SAFX08;

\- data de emissão da nota = conteúdo do campo 102 da SAFX08;

\- produto = produto do item da nota de devolução; 

Obs: a recuperação dos documentos ficais do período pode ser feito pelas tabelas do Data Mart\. Mas a recuperação da nota referenciada, deve ser feita pela tabela definitiva X07/X08, pois essas notas podem estar em períodos anteriores, onde pode não existir informação do Data Mart\.

__Gravação da SAFX308__

__EST\_ST\_RS\_NF\_DEV\_ENT__

__Regra de geração do C186 no SPED FISCAL__

RNC186

Gravar a SAFX308:

Campos 01 a 15 – Campos chave da nota de devolução de Entrada  

Campo 16 – preencher com 1\-Nota Fiscal \(SAFX07/08\)

Campos 17 ao 23 – campos chave da nota de entrada referenciada; Campo 21 deve ser preenchido com a Data de saída/recebimento \(campo 20 da SAFX07\);

Campo 30  \- preencher com o numero do item da nota de entrada referenciada;

Este registro foi criado na versão 1\.14, com vigência a partir de Jan/2021 \(__MFS45380__\)\.

Trata\-se de um registro “filho” do C100, e seu objetivo é demonstrar informações complementares de ICMS\-ST, das operações de devolução de entradas \(__*notas de saída*__\)\.  São informações referentes às notas de entrada que originaram a devolução\.

\(Observar que, diferente do C181, este registro C186 é “filho” do C100, e não do C170\. Por isso, ele tem no seu layout o número do item da devolução, no campo 02\-NUM\_ITEM\)\.

 

__Origem dos Dados:__ __SAFX308__ \(Tabela das Informações Complementares das Operações de Devolução Sujeitas ao ST \- Sped Fiscal\) 

Este registro será gerado apenas quando a nota fiscal em questão \(nota fiscal gravada no registro “pai” C100\) tiver as seguintes características:

   \- __*Nota de saída*__ \(MOVTO\_E\_S = “9”\);

   \- Nota fiscal de devolução \(NORM\_DEV = “2”\);

Se atendidas estas condições, será verificada a existência de dados na SAFX308 para a nota em questão\.

Critérios para recuperação dos dados na SAFX308:

Campos 01 a 12 – Considerar os campos chave da nota do registro “pai” C100;

Poderão existir ‘n’ registros na SAFX308 para a nota em questão, e para cada um deles, será gerado um registro C186\.

RNC186\-02

Campo __02\-NUM\_ITEM__

Conteúdo do campo “15\-Item da Nota Fiscal” da SAFX308\.

RNC186\-03

????

Se trabalharmos com produto associado, e a nota fiscal ser referenciar a um produto associado, apresento qual código?  O código do produto principal?

Campo __03\-COD\_ITEM__

Neste campo será gravada a identificação do Produto, a partir dos campos “12\-Indicador do Produto” e “13\-Código do Produto” da SAFX308, considerando o parâmetro “*Considerar o Indicador no Código do Item*” da tela dos Dados Iniciais do Sped, da seguinte forma: 

Se parâmetro estiver marcado:

      Neste caso, será gravado o código do produto concatenado com o indicador:

      \(Indicador de Produto  \+  “\-“  \+  Código do produto\)

Senão

      Neste caso, será gravado apenas o código do produto;

O Produto informado deve ter seus dados de cadastro informados em um registro 0200\.

RNC186\-04

Campo __04\-CST\_ICMS__

Neste campo é informado o código da situação tributária do item da nota de devolução\. 

Esta informação é recuperada do item da nota \(SAFX08\), através dos campos da SAFX308 que identificam a chave do item \(campos 01 ao 15\)\.

Conteúdo: concatenação dos códigos das tabelas de situação estadual  “A” e “B” \(código A \+ código B\), que são os campos 30 e 31 da SAFX08;

RNC186\-05

 

Campo __05\-CFOP__

Neste campo é informado o código do CFOP do item da nota de devolução\. 

Esta informação é recuperada do item da nota \(SAFX08\), através dos campos da SAFX308 que identificam a chave do item \(campos 01 ao 15\)\.

Conteúdo: código do CFOP \(campo 22\-Código Fiscal da SAFX08\)\. 

RNC186\-06

Campo 31\-Código Motivo \(COD\_MOTIVO\)

Qual código deve ser utilizado?????

Preencher com: RS400??

Campo __06\-COD\_MOT\_REST\_COMPL__

Conteúdo do campo “31\-Código Motivo” da SAFX308\.

RNC186\-07

__Campo 32 \- Quantidade Convertida \(QTD\_CONV\)__

\*\* 28/12: mudei para Qtde Convertida da NF de Devolução \*\*

Campo 24\-Quantidade do Item da nota de Entrada referenciada, aplicando a conversão, quando necessário\. Veja:

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\)  __*\(ver OBS abaixo sobre os produtos associados\)*

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria quantidade do item da nota;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\)

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade Convertida”;

     Senão         

         Nesse caso a quantidade do item \(SAFX08\) será convertida para a unidade de medida do cadastro do produto;

         \[ Quantidade do item da nota \(SAFX08\) \* Fator de Conversão \]

__Sobre os produtos associados:__ Quando se tratar de uma nota fiscal de produto “associado”, a comparação será feita da unidade de medida da nota, com a __unidade do produto principal__\.

Exemplo:

__Produto principal__: COCA\-COLA PET                 \(unidade de medida do estoque – SAFX2013 = UN\) 

__Produtos associados__: COCA\-COLA PET–1      \(unidade de medida do estoque – SAFX2013 = PAC \(6 unidades\)\)

Nota de venda do produto associado: __COCA\-COLA PET\-1__, unidade da nota = PAC, Quantidade = __5__

Compara a unidade de medida da nota do produto associado com a unidade de estoque do produto principal: PAC x UN

Como é diferente, deve\-se converter a quantidade da nota de PAC para UN\. 

Para acessar a tabela de conversão por produto, será utilizado o código do produto principal:

__DWT\_CONV\_MEDIDA\-2: __Produto = __COCA\-COLA PET__

                                          Unidade Origem = PAC

                                          Unidade Destino = UN

                                          Fator de conversão = 6,0000

Conversão da quantidade da nota do associado:  QTD da nota x Fator de Conversão   =  5 x 6,0000 = 30,0000 

Lembrando que, quando não existe fator na tabela de conversão por produto \(DWT\_CONV\_MEDIDA\_2\), será utilizada a tabela padrão \(DWT\_CONV\_MEDIDA\)\.  

__= = = = =__

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o item da nota será gerado com o campo Quantidade da Saída sem informação, e será gravada a seguinte mensagem de erro no log:

“*Fator de conversão de medida de XXX para XXX não encontrado\. O item do documento será gerado sem a informação da quantidade e do valor unitário”*

* *\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item do documento, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

Campo __07\-QUANT\_CONV__

Conteúdo do campo “32\-Quantidade Convertida” da SAFX308\.

RNC186\-08

__Campo: 33\-Unidade de Medida \(COD\_MEDIDA\)__

Unidade de Medida do Produto\. Campo “14\-Código de Medida” da SAFX2013 \(unidade da SAFX2007\);

*\(ver OBS sobre os produtos associados\)*

Campo: __08\-UNID__

Conteúdo do campo “33\-Unidade de Medida” da SAFX308\.

A unidade informada deve ter seus dados de cadastro informados em um registro 0190 \(Identificação das Unidade de Medida\)\. 

Se a unidade de medida informada neste campo for diferente da unidade de medida que será gravada no registro 0200 do Produto \(unidade de medida padrão da SAFX2013, campo “*20 – Unidade de Medida Padrão*”, conforme a RN0200\-06\), o fator de conversão entre as duas unidades será gravado no registro 0220\. 

RNC186\-09

Campo: __09\-COD\_MOD\_ENTRADA__

Neste campo é informado o modelo da nota fiscal *de referência*\.

Esta informação é recuperada da capa da nota de referência \(SAFX07\), através dos campos da SAFX308 que identificam a chave da capa \(campos 17 ao 23\), e considerando nessa busca apenas as notas de *entrada* e NORM\_DEV = “1”\.

Conteúdo: campo 13\-Modelo de Documento da SAFX07\. 

RNC186\-10

  

Campo __10\-SERIE\_ENTRADA__:

Este campo será preenchido apenas na seguinte condição:

- Modelo da nota fiscal informado no campo 09\-COD\_MOD\_ENTRADA <> 55;

Nesse caso, será informado o conteúdo do campo “18\-Série do Documento Fiscal de Referência” da SAFX308\.   

RNC186\-11

Campo __11\-NUM\_DOC\_ENTRADA__:

Este campo será preenchido apenas na seguinte condição:

- Modelo do documento informado no campo 09\-COD\_MOD\_ENTRADA <> “55;

 

Nesse caso, será informado o conteúdo do campo “17\- Número do Documento Fiscal de Referência” da SAFX308;

RNC186\-12

Campo __12\-CHV\_DFE\_ENTRADA__:

Este campo será preenchido apenas na seguinte condição:

- Modelo do documento informado no campo 09\-COD\_MOD\_ENTRADA = “55”;

A informação da chave eletrônica é recuperada da capa da nota *de referência* \(SAFX07\), através dos campos da SAFX308 que identificam a chave da capa \(campos 17 ao 23\), e considerando nessa busca apenas as notas de *entrada* e NORM\_DEV = “1”\.

Conteúdo: campo “226\-Chave de Acesso da NF\-Eletrônica” da SAFX07 \(utilizar as primeiras 44 posições, seguindo o formato da NF\-e nacional\)\.

Crítica sobre o preenchimento do campo:

No caso deste modelo de documento \(55\), se a informação da chave eletrônica não estiver preenchida no documento, o campo será gravado sem informação, e no log será gravada uma mensagem de erro, conforme padrão do Sped Fiscal: “*O campo CHV\_DFE\_ENTRADA  é de preenchimento obrigatório, e não foi informado”*\.

O log deve exibir os dados de identificação da nota de devolução, e também do documento de referência, para que o usuário possa identificar o problema\.

RNC186\-13

Campo __13\-DT\_DOC\_ENTRADA__:

A data de emissão é recuperada da capa da nota *de referência* \(SAFX07\), através dos campos da SAFX308 que identificam a chave da capa \(campos 17 ao 23\), e considerando nessa busca apenas as notas de *entrada* e NORM\_DEV = “1”\.

Conteúdo: campo 11\-Data de Emissão da SAFX07\.

RNC186\-14

Campo __14\-NUM\_ITEM\_ENTRADA__

Conteúdo do campo “30\- Número do Item do Documento de Referência” da SAFX308\.

RNC186\-15

__Campo 34\-Valor Unitário Conv \(VLR\_UNIT\_CONV\)__

  VLR\_UNIT\_CONV = VLR\_CONTAB\_ITEM da SAFX08 / QTD\_CONV

Onde:

- VLR\_CONTAB\_ITEM é o campo 64\-valor Contabil do Item da nota de Entrada referenciada;
- QTD\_CONV que foi gravada no campo __32 \- Quantidade Convertida__

\*\* 28/12: qtde da nota de entrada

__19\.3\-A\.1\.4\.1__ \-Se a entrada objeto de devolução ocorreu antes de 1º de janeiro de 2021, para o preenchimento dos campos: \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)

a\)VL\_UNIT\_CONV\_ENTRADA, deverá ser utilizado o resultado da multiplicação do valor informado no campo VL\_BC\_ICMS\_ST pelo resultado da divisão do valor informado no campo VL\_ICMS\_OP pelo total da soma dos valores informados nos campos VL\_ICMS\_OP e VL\_ICMS\_ST, todos os campos do registro __H030,__ informado conforme o subitem 19\.3\-A\.3; \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)

43\-VLR\_BASE\_ICMSS\_MEDIO x

\(21\-VLR\_ICMS\_MEDIO / \(21\-VLR\_ICMS\_MEDIO \+ 22\-VLR\_ICMSS\_MEDIO\)\)

Sendo revisado pelo CARREFOUR – MFS\-57863

Campo __15\-VL\_UNIT\_CONV\_ENTRADA__

Conteúdo do campo “34\-Valor Unitário Conv” da SAFX308\.

RNC186\-16

Campo 35\-Valor Unitário ICMS OP Conv__ \(VLR\_ICMS\_CONV\)__

Preencher com: Valor do ICMS / QTD\_CONV

Onde os valores são oriundos da nota de entrada referenciada:

- Valor do ICMS é oriundo de um dos três campos SAFX08, dependendo de qual esteja preenchido:

Campo “43\-Valor ICMS”, se preenchido, ou

   Campo “80\-ICMS não Escriturado”, se preenchido, ou

       Campo “225\-Valor ICMS Não Destacado”  

- QTD\_CONV que foi gravada no campo __32 \- Quantidade Convertida__

\*\* 28/12: qtde da nota de entrada

__19\.3\-A\.1\.4\.1__ \-Se a entrada objeto de devolução ocorreu antes de 1º de janeiro de 2021, para o preenchimento dos campos: \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)

b\)VL\_UNIT\_ICMS\_OP\_CONV\_ENTRADA, deverá ser utilizado o valor informado no campo VL\_ICMS\_OP do registro H030, informado conforme o subitem 19\.3\-A\.3; \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)

Campo __16\-VL\_UNIT\_ICMS\_OP\_CONV\_ENTRADA__

Conteúdo do campo “35\-Valor Unitário ICMS OP Conv” da SAFX308

RNC186\-17

Campo 36\-Valor Unitário Base ICMS ST Conv da Entrada \(VLR\_UNIT\_BC\_ICMSS\_ENT\)

Preencher com: Valor da BC\-ST / QTD\_CONV

Onde os valores são oriundos da nota de entrada referenciada:

- Valor da BC\-ST é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor da BC\-ST = 61\-BASE\_SUB\_TRIB\_ICMS\.

Senão: 

Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

   Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

Senão:

Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então:

   Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

Senão:

Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, então:

   Valor da BC\-ST = 106 \- VLR\_BASE\_ICMS\_ORIG

- QTD\_CONV que foi gravada no campo __32 \- Quantidade Convertida__

\*\* 28/12: qtde da nota de entrada

Validação

Considerando os campos 61\-BASE\_SUB\_TRIB\_ICMS , 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT, 106 \- VLR\_BASE\_ICMS\_ORIG, se no mesmo item de nota, dois ou mais desses campos estiverem preenchidos, gravar  zero neste campo e exibir a mensagem no log :” O campo Valor Unitário BC ICMS\-ST Conv\. \(Entradas\) foi gerado com zero, pois existe mais de um campo de Base de ICMS – ST com valor preenchido na nota”\. 

No log deve constar esses campos com os respectivos valores e os campos identificadores da nota\.

__19\.3\-A\.1\.4\.1__ \-Se a entrada objeto de devolução ocorreu antes de 1º de janeiro de 2021, para o preenchimento dos campos: \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)

c\)VL\_UNIT\_BC\_ICMS\_ST\_CONV\_ENTRADA, deverá ser utilizado o valor informado no campo VL\_BC\_ICMS\_ST do registro H030, informado conforme o subitem 19\.3\-A\.3; \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)

Campo __17\-VL\_UNIT\_BC\_ICMS\_ST\_CONV\_ENTRADA__

Conteúdo do campo “36\-Valor Unitário Base ICMS ST Conv da Entrada” da SAFX308

RNC186\-18

Campo 37\-Valor Unitário ICMS ST Conv da Entrada \(VLR\_UNIT\_ICMSS\_CONV\_ENT\)

__\(\*\) Faz sentido a gente inserir o parametro FECP embutido\.__

Preencher com: \(Valor do ICMS\-ST \+ FECEP\-ST\)/ QTD\_CONV

Onde os valores são oriundos da nota de entrada referenciada:

- Valor do ICMS\-ST é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

   Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

Senão:

Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então:

   Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

Senão:

Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, então:

   Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.
- QTD\_CONV que foi gravada no campo __32 \- Quantidade Convertida__

\*\* 28/12: qtde da nota de entrada

Validação

Considerando os campos 52\-VLR\_SUBST\_ICMS , 145 \- VLR\_ICMSS\_N\_ESCRIT, 133\- VLR\_ICMSS\_NDESTAC , 107\- VLR\_TRIB\_ICMS\_ORIG, se no mesmo item de nota, dois ou mais desses campos estiverem preenchidos, gravar  zero neste campo e exibir a mensagem no log :” O campo Valor Unitário ICMS\-ST Conv\.  \(Entradas\) foi gerado com zero, pois existe mais de um campo de Valor ICMS – ST com valor preenchido na nota”\. 

No log deve constar esses campos com os respectivos valores e os campos identificadores da nota\.

__19\.3\-A\.1\.4\.1__ \-Se a entrada objeto de devolução ocorreu antes de 1º de janeiro de 2021, para o preenchimento dos campos: \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)

d\)VL\_UNIT\_ICMS\_ST\_CONV\_ENTRADA, deverá ser utilizado o valor informado no campo VL\_ICMS\_ST do registro H030, informado conforme o subitem 19\.3\-A\.3\. \(Acrescentado pela [IN RE 096/20](javascript:goDocument('276538')), de 04/12/20\. \(DOE 08/12/20\) \- Efeitos a partir de 08/12/20\.\)

Campo __18\-VL\_UNIT\_ICMS\_ST\_CONV\_ENTRADA__

Conteúdo do campo “37\-Valor Unitário ICMS ST Conv da Entrada” da SAFX308

RNC186\-19

Campo 38\-Valor Unitário FCP ST Conv da Entrada \(VLR\_UNIT\_FCP\_CONV\_ENT\)

Preencher com: FECEP\-ST/ QTD\_CONV

Onde os valores são oriundos da nota de entrada referenciada:

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.
- QTD\_CONV que foi gravada no campo __32 \- Quantidade Convertida__

\*\* 28/12: qtde da nota de entrada

Campo __19\-VL\_UNIT\_FCP\_ST\_CONV\_ENTRADA__

Conteúdo do campo “38\-Valor Unitário FCP ST Conv da Entrada” da SAFX308

## <a id="_Toc354574228"></a><a id="_Toc354574403"></a><a id="_Toc354574447"></a><a id="_Toc354574532"></a><a id="_Toc354578078"></a><a id="_Toc354578305"></a><a id="_Toc354578996"></a><a id="_Toc354579137"></a><a id="_Toc60126011"></a>Procedimentos para Interface

<a id="_Toc200962071"></a><a id="_Toc200996470"></a><a id="_Toc200996588"></a><a id="_Toc200998068"></a>

# <a id="_Toc354574229"></a><a id="_Toc354574404"></a><a id="_Toc354574448"></a><a id="_Toc354574533"></a><a id="_Toc354578079"></a><a id="_Toc354578306"></a><a id="_Toc354578997"></a><a id="_Toc354579138"></a><a id="_Toc60126012"></a>PROCEDIMENTOS PARA CONTEÚDO

<a id="_Toc199304378"></a><a id="_Toc200962072"></a><a id="_Toc200996471"></a><a id="_Toc200996589"></a><a id="_Toc200998069"></a>

## <a id="_Toc354574230"></a><a id="_Toc354574405"></a><a id="_Toc354574449"></a><a id="_Toc354574534"></a><a id="_Toc354578080"></a><a id="_Toc354578307"></a><a id="_Toc354578998"></a><a id="_Toc354579139"></a><a id="_Toc60126013"></a>Criação / Alteração – Tabelas \(Manual de Layout\)

## <a id="_Toc200996472"></a><a id="_Toc200996590"></a><a id="_Toc200998070"></a><a id="_Toc354574231"></a><a id="_Toc354574406"></a><a id="_Toc354574450"></a><a id="_Toc354574535"></a><a id="_Toc354578081"></a><a id="_Toc354578308"></a><a id="_Toc354578999"></a><a id="_Toc354579140"></a><a id="_Toc60126014"></a>Criação / Alteração em telas e relatórios \(manual operacional, roteiro e help\)

<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a><a id="OLE_LINK7"></a>

## <a id="_Toc23774813"></a><a id="_Toc60126015"></a>Criação / Alteração de Tabelas \(Fixas, Acessórias, Básicas\)

## <a id="_Toc354574233"></a><a id="_Toc354574408"></a><a id="_Toc354574452"></a><a id="_Toc354574537"></a><a id="_Toc354578083"></a><a id="_Toc354578310"></a><a id="_Toc354579001"></a><a id="_Toc354579142"></a><a id="_Toc23774814"></a><a id="_Toc60126016"></a>Criação / Alteração de Roteiro Operacional

## <a id="_Toc354574234"></a><a id="_Toc354574409"></a><a id="_Toc354574453"></a><a id="_Toc354574538"></a><a id="_Toc354578084"></a><a id="_Toc354578311"></a><a id="_Toc354579002"></a><a id="_Toc354579143"></a><a id="_Toc23774815"></a><a id="_Toc60126017"></a>Outras informações que necessitarão ser atualizadas \(help, manual operacional etc\)

## <a id="_Toc426992014"></a><a id="_Toc428981618"></a><a id="_Toc23774816"></a><a id="_Toc60126018"></a>Informações p/ Carta do Patch

Direto no Jira

# <a id="_Toc200962062"></a><a id="_Toc200996464"></a><a id="_Toc200996582"></a><a id="_Toc200998062"></a><a id="_Toc354574235"></a><a id="_Toc354574410"></a><a id="_Toc354574454"></a><a id="_Toc354574539"></a><a id="_Toc354578085"></a><a id="_Toc354578312"></a><a id="_Toc354579003"></a><a id="_Toc354579144"></a><a id="_Toc60126019"></a>TESTES

= = = = =


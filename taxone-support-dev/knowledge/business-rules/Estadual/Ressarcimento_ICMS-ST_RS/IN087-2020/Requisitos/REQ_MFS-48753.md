# REQ_MFS-48753

- **Fonte:** REQ_MFS-48753.docx
- **Modificado:** 2021-02-21
- **Tamanho:** 401 KB

---

THOMSON REUTERS

<a id="_Hlk22664599"></a>__MFS\-48753__

__Módulo Estadual – Ressarcimento RS – 1ª Entrega__

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

[1\.	INTRODUÇÃO	1](#_Toc64492355)

[1\.1	Documentos e Base Legal para a Solução	1](#_Toc64492356)

[2\.	Levantamentos junto a Área da Informação	1](#_Toc64492357)

[3\.	SOLUÇÃO FUNCIONAL / ESCOPO	1](#_Toc64492358)

[3\.1	Procedimentos para Fábrica	1](#_Toc64492359)

[3\.1\.1	– Alteração no Menu	1](#_Toc64492360)

[3\.1\.2	– Parametrização por CFOP	1](#_Toc64492361)

[3\.1\.3	– Parametrização por Natureza de Operação	1](#_Toc64492362)

[3\.1\.4	– Geração dos Movimentos	1](#_Toc64492363)

[3\.1\.5	– Transferência dos Movimentos para EFD FISCAL	1](#_Toc64492364)

[3\.1\.6	– Geração do Meio Magnético – Sped Fiscal	1](#_Toc64492365)

[4\.	PROCEDIMENTOS PARA CONTEÚDO	1](#_Toc64492366)

[4\.1	Criação / Alteração – Tabelas \(Manual de Layout\)	1](#_Toc64492367)

[4\.2	Criação / Alteração do Manual Operacional	1](#_Toc64492368)

[4\.2\.1	– Alteração no Menu	1](#_Toc64492369)

[4\.2\.2	– Introdução	1](#_Toc64492370)

[4\.2\.3	– Parâmetros – Operações da IN\-RE 048/18	1](#_Toc64492371)

[4\.2\.4	– Parâmetros – Operações por CFOP da IN\-RE 048/18	1](#_Toc64492372)

[4\.2\.5	– Parâmetros – Operações por Natureza de Operação da IN\-RE 048/18	1](#_Toc64492373)

[4\.2\.6	– Parâmetros – Operações da IN\-RE 087/20	1](#_Toc64492374)

[4\.2\.7	– Parâmetros – Operações por CFOP da IN\-RE 087/20	1](#_Toc64492375)

[4\.2\.8	– Parâmetros – Operações por Natureza de Operação da IN\-RE 087/20	1](#_Toc64492376)

[4\.2\.9	– Parametrização por Produtos	1](#_Toc64492377)

[4\.2\.10	– Parametrização por Produtos – Por Código	1](#_Toc64492378)

[4\.2\.11	– Parametrização por Produtos – Por NCM	1](#_Toc64492379)

[4\.2\.12	– Parametrização por Produtos – Por CEST	1](#_Toc64492380)

[4\.2\.13	– Menu Geração	1](#_Toc64492381)

[4\.2\.14	– Geração dos Movimentos – IN\-RE 048/19	1](#_Toc64492382)

[4\.2\.15	– Confêrência dos Movimentos \- IN\-RE 048/18	1](#_Toc64492383)

[4\.2\.16	– Geração dos Movimentos \- IN\-RE 087/20	1](#_Toc64492384)

[4\.2\.17	– Transferência dos Movimentos para EFD FISCAL	1](#_Toc64492385)

[4\.3	Criação / Alteração de Tabelas \(Fixas, Acessórias, Básicas\)	1](#_Toc64492386)

[4\.4	Criação / Alteração de Roteiro Operacional	1](#_Toc64492387)

[4\.5	Objetivo	1](#_Toc64492388)

[4\.6	Procedimentos para utilização do módulo	1](#_Toc64492389)

[4\.7	Procedimentos a serem executados a cada período	1](#_Toc64492390)

[4\.8	Menu Janela	1](#_Toc64492391)

[4\.9	Menu Ajuda	1](#_Toc64492392)

[4\.10	Atendimento Técnico MasterSAF	1](#_Toc64492393)

[4\.11	Outras informações que necessitarão ser atualizadas \(help, manual operacional etc\)	1](#_Toc64492394)

[4\.12	Informações p/ Carta do Patch	1](#_Toc64492395)

[5\.	TESTES	1](#_Toc64492396)

# <a id="_Toc200962059"></a><a id="_Toc200996459"></a><a id="_Toc200996577"></a><a id="_Toc200998055"></a><a id="_Toc354574223"></a><a id="_Ref354574309"></a><a id="_Ref354574320"></a><a id="_Toc354574398"></a><a id="_Toc354574442"></a><a id="_Toc354574527"></a><a id="_Toc354578073"></a><a id="_Toc354578300"></a><a id="_Toc354578991"></a><a id="_Toc354579132"></a><a id="_Toc64492355"></a>INTRODUÇÃO

<a id="_Hlk53754794"></a>

## <a id="_Toc64492356"></a>Documentos e Base Legal para a Solução

__INSTRUÇÃO NORMATIVA RE Nº 087/20__

__INSTRUÇÃO NORMATIVA RE Nº 096/20__

# <a id="_Toc64492357"></a>Levantamentos junto a Área da Informação

<a id="_MON_1675079978"></a>![](data:image/x-emf;base64,AQAAAGwAAAABAAAAAQAAAGMAAAA7AAAAAAAAAAAAAAAtBwAApQQAACBFTUYAAAEAfBYAABUAAAACAAAAAAAAAAAAAAAAAAAAgAcAADgEAABYAQAAwgAAAAAAAAAAAAAAAAAAAMA/BQDQ9QIAGAAAAAwAAAAAAAAAGQAAAAwAAAD///8AcgAAAKAQAAAjAAAAAQAAAEIAAAAgAAAAIwAAAAEAAAAgAAAAIAAAAACA/wEAAAAAAAAAAAAAgD8AAAAAAAAAAAAAgD8AAAAAAAAAAP///wAAAAAAbAAAADQAAACgAAAAABAAACAAAAAgAAAAKAAAACAAAAAgAAAAAQAgAAMAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAA/wAA/wAA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABaW12ydHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/WltdsgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAARiEIYL1aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/476l//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAvVoY/71aGP+9Whj/vVoY//v18f//////0o5g/71aGP+9Whj/0o5g///////79fH/vVoY/71aGP+9Whj/vVoY//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/71aGP/FbzX////////////it5r/vVoY/71aGP/it5r////////////FbzX/vVoY/71aGP+9Whj/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/vVoY/9KOYP////////////fr4/+9Whj/vVoY//fr4////////////9KOYP+9Whj/vVoY/71aGP/6+vr/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAvVoY/71aGP+9Whj/3q2M/////////////////8l5Q//FbzX///////v18f//////3q2M/71aGP+9Whj/vVoY//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/71aGP/rzLf//////+K3mv//////3q2M/9qiff//////68y3///////rzLf/vVoY/71aGP+9Whj/+vr6/9N8K//TfCv/03wr/9N8K//TfCv/03wr/9N8K//6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/vVoY//fr4///////wWQm///////z4dT/68y3///////FbzX///////fr4/+9Whj/vVoY/71aGP/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAvVoY/71aGP/BZCb///////v18f+9Whj/68y3////////////9+vj/71aGP/z4dT//////8FkJv+9Whj/vVoY//r6+v/upUH/7qVB/+6lQf/upUH/7qVB/+6lQf/upUH/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/86DUv//////79bG/71aGP/aon3////////////it5r/vVoY/+bCqf//////zoNS/71aGP+9Whj/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/3q2M///////erYz/vVoY/8VvNf///////////9KOYP+9Whj/2qJ9///////erYz/vVoY/71aGP/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAvVoY/71aGP/mwqn//////9KOYP+9Whj/vVoY//fr4///////wWQm/71aGP/Og1L//////+bCqf+9Whj/vVoY//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAARiEIYL1aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/476l//r6+v/6+vr/+vr6/6aoqf90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5//r6+v/6+vr/+vr6//r6+v/Iycn/dHd5/yssLWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/+vr6//r6+v/6+vr/yMnJ/3R3ef8rLC1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef/6+vr/+vr6/8jJyf90d3n/KywtYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5//r6+v/Iycn/dHd5/yssLWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/yMnJ/3R3ef8rLC1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef90d3n/KywtYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWltdsnR3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/yssLWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAADAAAAAAAAAISAAAADAAAAAEAAABSAAAAcAEAAAEAAAAQAAAAAAAAAAAAAAAAAAAAvAIAAAAAAAABAgIiUwB5AHMAdABlAG0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAApQEAAM7IEwv5fwAAAAAAAAAAAADXGgG8/////yAAAAAAAAAACyQZC/l/AAB5Fdz//////xwSAAAB3AEAAADn96UBAAB5Fdz//////xwSAAAB3AEAAADn96UBAAB5Fdz//////xwSAAAB3AEAAADn96UBAACL6KoKAAAAAACA/wEAAAAAeRUB3P////8AAAAAAAAAAAAAAAAAAAAA1xoBvP/////NLJoM+X8AAKAAAAD/////eRUB3AAA//9QVjE7jQAAAO1ke6P4fwAAAAAAAAAAAACL6KoK+X8AACBXMTuNAAAASVYxO40AAAABAAAAAAAAACBXMTtkdgAIAAAAACUAAAAMAAAAAQAAACUAAAAMAAAADQAAgCgAAAAMAAAAAQAAAFIAAABwAQAAAQAAAPX///8AAAAAAAAAAAAAAACQAQAAAAAAAABAACJTAGUAZwBvAGUAIABVAEkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGizMTuNAAAA8ZUsDfl/AAAAAAAAAAAAADCatvelAQAA2Dqu96UBAAAAAAAAAAAAAAAABvulAQAAUA1YpPh/AACQSAL7pQEAAGYAAAAAAAAAAAAG+6UBAADAmQb7pQEAAAAAAAAAAAAABwAAAAAAAAAAAADrpQEAAHCRA/sAAAAAqNaf96UBAAAAH+zqpQEAAAAAAAAAAAAACAAAAAAAAACo1p/3pQEAAEAAAAAAAAAAAAAAAAAAAADA8+icAAAAAICtBvulAQAAIV0sDfl/AABAAAAAAAAAAIvoqgr5fwAAULMxO40AAAC5sTE7jQAAACAAAAAAAAAAULMxO2R2AAgAAAAAJQAAAAwAAAABAAAAVAAAAKwAAAAGAAAAIgAAAGEAAAAuAAAAAQAAAFVVj0EmtI9BBgAAACIAAAAQAAAATAAAAAQAAAAAAAAAAAAAAGYAAABCAAAAbAAAAFIARQBRAF8ATQBGAFMALQA0ADgANwA1ADMAIAAtACAABwAAAAYAAAAIAAAABQAAAAoAAAAGAAAABgAAAAQAAAAGAAAABgAAAAYAAAAGAAAABgAAAAMAAAAEAAAAAwAAAFQAAAC0AAAAAQAAAC8AAABjAAAAOwAAAAEAAABVVY9BJrSPQQEAAAAvAAAAEQAAAEwAAAAEAAAAAAAAAAAAAABmAAAAQgAAAHAAAABMAGUAdgBhAG4AdABhAG0AZQBuAHQAbwAuAGQAbwBjAHgAAAAFAAAABgAAAAUAAAAGAAAABwAAAAQAAAAGAAAACQAAAAYAAAAHAAAABAAAAAcAAAADAAAABwAAAAcAAAAFAAAABQAAACUAAAAMAAAADQAAgEYAAAAgAAAAEgAAAEkAYwBvAG4ATwBuAGwAeQAAAAAARgAAAFAAAABEAAAAUgBFAFEAXwBNAEYAUwAtADQAOAA3ADUAMwAgAC0AIABMAGUAdgBhAG4AdABhAG0AZQBuAHQAbwAuAGQAbwBjAHgAAABGAAAAEAAAAAIAAAAAAAAARgAAABAAAAAEAAAA+gAAAEYAAAAgAAAAEgAAAEkAYwBvAG4ATwBuAGwAeQAAAAAADgAAABQAAAAAAAAAEAAAABQAAAA=)

 

# <a id="Premissas"></a><a id="_Toc200962060"></a><a id="_Toc200996460"></a><a id="_Toc200996578"></a><a id="_Toc200998056"></a><a id="_Toc354574225"></a><a id="_Toc354574400"></a><a id="_Toc354574444"></a><a id="_Toc354574529"></a><a id="_Toc354578075"></a><a id="_Toc354578302"></a><a id="_Toc354578993"></a><a id="_Toc354579134"></a><a id="_Toc64492358"></a>SOLUÇÃO FUNCIONAL / ESCOPO

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

## <a id="_Toc200962061"></a><a id="_Toc200996461"></a><a id="_Toc200996579"></a><a id="_Toc200998057"></a><a id="_Toc354574226"></a><a id="_Toc354574401"></a><a id="_Toc354574445"></a><a id="_Toc354574530"></a><a id="_Toc354578076"></a><a id="_Toc354578303"></a><a id="_Toc354578994"></a><a id="_Toc354579135"></a><a id="_Toc64492359"></a>Procedimentos para Fábrica

### <a id="_Toc64492360"></a>– Alteração no Menu

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Descrição__: 

Alterar o menu para distribuir os itens já existentes e incluir novos\.  Os itens já existentes que apenas foram reposicionados, estão marcados em amarelo, e os novos em verde\.

Parâmetros		         Geração			       Relatórios		

IN\-RE 048/18		         IN\-RE 048/18		                       IN\-RE 048/18

     Dados Iniciais		              Geração dos Movimentos	            Conferência dos Movimentos

     Operações		              Transferências entre Apurações            Conferência da Transferência entre Apurações

          CFOP		         IN\-RE 087/20

          Natureza de Operação	              Geração dos Movimentos

IN\-RE 087/20		              Transferência dos Movimentos para EFD Fiscal

      Operações

   	CFOP

   	Natureza de Operação

Produtos

      Por Código

      Por NCM

      Por Cest

### <a id="_Toc64492361"></a>– Parametrização por CFOP

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> \(IN\-RE 087/20\) >> Operações >> CFOP

__Descrição:__

Criar tela de parametrização do CFOP para demonstrar as operações:

771 \- Entrada \(e Devoluções\)

770 \- Saída Interna à Consumidor Final \(e Devoluções\)

Ver documentos:

MTZ\-Ressarc\-RS\-IN087\_2020\_Parametrizacao\_CFOPs\.docx

### <a id="_Toc64492362"></a>– Parametrização por Natureza de Operação

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> <a id="_Hlk59893211"></a>\(IN\-RE 087/20\) >> Operações >> Natureza de Operação

__Descrição:__

Criar tela de parametrização do CFOP para demonstrar as operações:

771 \- Entrada \(e Devoluções\)

770 \- Saída Interna à Consumidor Final \(e Devoluções\)

Ver documentos:

MTZ\-Ressarc\-RS\-IN087\_2020\_Parametrizacao\_Natureza\.docx

### <a id="_Toc64492363"></a>– Geração dos Movimentos

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

<a id="_Toc200962071"></a><a id="_Toc200996470"></a><a id="_Toc200996588"></a><a id="_Toc200998068"></a>

### <a id="_Toc62224290"></a><a id="_Toc64492364"></a>– Transferência dos Movimentos para EFD FISCAL

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Geração >> \(IN\-RE 087/20\) >> Transferência dos Movimentos para EFD Fiscal

 

__Descrição:__

Criação da funcionalidade\.

Ver documentos:

MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_EFD Fiscal\.docx 

MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_Inventário\_H030\.docx

MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_Saldo Ressarcimento Complemento\_1255\.docx

MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_Tabelas SAFX\_C180\_C181\_C185\_C186\_C380\_C480

### <a id="_Toc62224287"></a><a id="_Toc64492365"></a>– Geração do Meio Magnético – Sped Fiscal

__Localização__: Módulo Sped  >> EFD \- Escrituração Fiscal Digital

__Menu__: Geração >> Meio Magnético 

__Descrição:__

Alteração na regra de geração do registro 0200 – campo Alíquota Interna\.

Ver documento:

Sped\_Fiscal\_Regras\_Bloco\_0\.docx

# <a id="_Toc354574229"></a><a id="_Toc354574404"></a><a id="_Toc354574448"></a><a id="_Toc354574533"></a><a id="_Toc354578079"></a><a id="_Toc354578306"></a><a id="_Toc354578997"></a><a id="_Toc354579138"></a><a id="_Toc64492366"></a>PROCEDIMENTOS PARA CONTEÚDO

<a id="_Toc199304378"></a><a id="_Toc200962072"></a><a id="_Toc200996471"></a><a id="_Toc200996589"></a><a id="_Toc200998069"></a>

## <a id="_Toc354574230"></a><a id="_Toc354574405"></a><a id="_Toc354574449"></a><a id="_Toc354574534"></a><a id="_Toc354578080"></a><a id="_Toc354578307"></a><a id="_Toc354578998"></a><a id="_Toc354579139"></a><a id="_Toc64492367"></a>Criação / Alteração – Tabelas \(Manual de Layout\)

## <a id="_Toc200996472"></a><a id="_Toc200996590"></a><a id="_Toc200998070"></a><a id="_Toc354574231"></a><a id="_Toc354574406"></a><a id="_Toc354574450"></a><a id="_Toc354574535"></a><a id="_Toc354578081"></a><a id="_Toc354578308"></a><a id="_Toc354578999"></a><a id="_Toc354579140"></a><a id="_Toc64492368"></a>Criação / Alteração do Manual Operacional

<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a><a id="OLE_LINK7"></a>Reformular o manual operacional do Módulo Ressarcimento ICMS\-ST – RS para atendimento a nova legislação: IN\-RE 087/20\.

Hoje esse módulo atende a IN\-RE 048/18\. 

E a partir dessa MFS, o módulo passará a atender as duas IN\-RE’s:

\- IN\-RE 048/18; 

\- IN\-RE 087/20\.

Sendo assim o título do manual deve ser alterado:

MANUAL OPERACIONAL  
RESSARCIMENTO DE ICMS \- ST \- RS \(IN\-RE 048/2018 e IN\-RE087/20\)

### <a id="_Toc64492369"></a>– Alteração no Menu

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Descrição__: 

O menu do módulo foi reorganizado distribuindo os itens de menu pelas IN\-RE’s:

\- IN\-RE 048/18 

\- IN\-RE 087/20

Sendo assim, os itens de menu que já existiam, utilizados no atendimento a IN\-RE 048/18, foram remanejados para abaixo do novo menu IN\-RE 048/18 \(ver os itens marcados em amarelo\)\.  

E novos itens de menu foram incluídos para atendimento a IN\-RE 087/20\. Ver o itens estão marcados em verde\.

Parâmetros		         Geração			       Relatórios		

IN\-RE 048/18		         IN\-RE 048/18		                       IN\-RE 048/18

     Dados Iniciais		              Geração dos Movimentos	            Conferência dos Movimentos

     Operações		              Transferências entre Apurações            Conferência da Transferência entre Apurações

          CFOP		         IN\-RE 087/20

          Natureza de Operação	              Geração dos Movimentos

IN\-RE 087/20		              Transferência dos Movimentos para EFD Fiscal

      Operações

   	CFOP

   	Natureza de Operação

Produtos

      Por Código

      Por NCM

      Por Cest

Com isso, os tópicos do manual ficarão organizados da seguinte maneira:

Introdução

Bla bla bla\.\.\.

Menu Parâmetros

 > IN\-RE 048/18

>> Dados Iniciais

       Bla bla bla\.\.\.

>> Operações

       Bla bla bla\.\.\.

>>> CFOP

          Bla bla bla\.\.\.

>>> Natureza de Operação

         Bla bla bla\.\.\.

> IN\-RE 087/20

>> Operações

      Bla bla bla\.\.\.

>>> CFOP

         Bla bla bla\.\.\.

>>> Natureza de Operação

        Bla bla bla\.\.\.

> Produtos

Bla bla bla\.\.\.

>> Por Código

       Bla bla bla\.\.\.

>> Por NCM

       Bla bla bla\.\.\.

>> Por CEST

       Bla bla bla\.\.\.

Menu Geração

 > IN\-RE 048/18

>> Geração dos Movimentos

       Bla bla bla\.\.\.

>> Transferência entre Apurações

       Bla bla bla\.\.\.

> IN\-RE 087/20

>> Geração dos Movimentos

       Bla bla bla\.\.\.

>> Transferência dos Movimentos para a EFD Fiscal

       Bla bla bla\.\.\.

Menu Relatórios

 > IN\-RE 048/18

>> Conferência dos Movimentos

       Bla bla bla\.\.\.

>> Conferência da Transferência entre Apurações

       Bla bla bla\.\.\.

### <a id="_Toc64492370"></a>– Introdução

__Descrição:__

Refazer o texto da Introdução conforme ABAIXO:

O módulo Ressarcimento de ICMS\-ST – RS amparado pelas Instruções Normativas RE 048/2018 e RE 087/2020 tem como objetivo calcular os valores de ressarcimento e complemento de ICMS\-ST a serem apresentados nos arquivos do Sped – EFD Fiscal\.

A IN\-RE 048/2018, com vigência a partir de 1º de janeiro de 2019, estabelece a geração de uma subapuração apresentando os créditos ICMS\-ST provenientes das entradas de mercadoria e dos débitos originários das saídas para consumidor final e para outros Estados\. O ICMS\-ST a ser ressarcido ou complementado é lançado na Apuração do ICMS\-ST e demonstrado no bloco E, registros E210 e E220 do Sped – EFD Fiscal\.  A subapuração e seus detalhamentos são apresentados no bloco 1, registros 1920, 1921 e 1923 do SPED EFD\.

A IN\- RE 087/2020, com vigência a partir de 1º de janeiro de 2021, estabelece a escrituração dos movimentos de Entradas, Saídas, Devoluções de Entradas e Devoluções de Saídas dos produtos sujeitos a ICMS\-ST, nos registros C180, C181, C185, C380 e C185 do Sped – EFD Fiscal, o saldo do Ressarcimento e Complemento do ICMS\-ST nos registros 1250/1255 e os valores unitários médios do ICMS, ICMS\-ST do Inventário, no registro H030\.  Nesta sistemática é realizado o cálculo do Valor Médio Ponderado Móvel do dia, aplicado nas operações de saídas e devoluções de saídas, a fim de determinar o valor ser Ressarcido/Restituído ou Complementado do ICMS\-ST\.

__Observação:__

A Subapuração gerada no módulo Ressarcimento do RS é diferente da Subapuração do ICMS gerada no módulo ICMS\. A Subapuração gerada no módulo ICMS tem como objetivo escriturar o ICMS de operações especificadas em legislação estadual como obrigadas a realizar apurações em separado e a Subapuração gerada no módulo Ressarcimento do RS, tem como objetivo realizar a apuração da diferença entre o preço praticado na operação a consumidor final e a base de cálculo utilizada para o cálculo do débito de responsabilidade por substituição tributária \(ressarcimento/restituição/complemento\), embaseada na IN\-RE 048/2018\.

A subapuração em cada módulo é distinta, ou seja, a Subapuração do RS não é visualizada pelo módulo ICMS, e vice\-versa\. A Subapuração do ICMS e a Subapuração do RS são apresentadas no mesmo conjunto de registros do SPED Fiscal, porém, as regras dos cálculos das duas apurações são completamente diferentes\.

Como consequência, os lançamentos a crédito e a débito gerados na Subapuração RS não podem ser alterados manualmente via tela de manutenção do módulo ICMS\.

Não está disponível o atendimento ao Ressarcimento ICMS\-ST RS para empresas cuja entrega de obrigações se dá por Inscrição Estadual Única\.

### <a id="_Toc64492371"></a>– Parâmetros – Operações da IN\-RE 048/18

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> IN\-RE 048/18>> Operações

__Descrição:__

Esse tópico é refere à Operações que ficará abaixo do item IN\-RE 048/18\. Não há modificação no texto\.

<a id="menu_param_oper"></a>Operações

Nesse menu são realizadas as parametrizações dos CFOP´s, CFOP’s/Naturezas por UF e Operação que são considerados na rotina de geração dos movimentos a partir das notas fiscais para a apuração do Ressarcimento de ICMS\-ST do Rio Grande do Sul, de acordo com a Instrução Normativa 048/2018\.

Bla bla bla\.\.\.

### <a id="_Toc64492372"></a>– Parâmetros – Operações por CFOP da IN\-RE 048/18 

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> IN\-RE 048/18>> Operações >> CFOP

__Descrição:__

Alteração no texto, incluindo o trecho marcado em verde/amarelo:

CFOP

O objetivo desta parametrização é identificar os CFOP´s por UF e Operação que são considerados na geração dos movimentos de entrada e saída para o Rio Grande do Sul, de acordo com a Instrução Normativa 048/2018\.

Orientação de preenchimento dos campos:

__UF:__ Apresenta a sigla da UF do Rio Grande do Sul\.

__Operação:__ Selecione a operação, conforme cadastro importado através da tabela TFIX31, para a qual os CFOP’s são associados:

\- Entrada com Substituição Tributária

\- Saída para Consumidor Final

\- Saída para outro Estado, Saída Isenta ou Não Tributada

__<<<<SÓ NO MANUAL DO MASTERSAF>>__

Obs\.: As Tabelas Fixas \(TFIX\) e Acessórias \(TACES\) são importadas no processo de atualização do patch, mas podem ser importadas, caso necessário, acessar o módulo Básicos \[menu: Ferramentas > Importar\]\.

__CFOP’s:__ Selecione os CFOP’s para a operação informada, considerados de acordo com a lista importada através da tabela SAFX2012\. Os CFOP’s de devolução não devem ser parametrizados para o Rio Grande do Sul\.

Obs\.: Para consultar o cadastro de CFOP \(SAFX2012\) acessar o módulo Básicos \[menu: Data Warehouse > Manutenção > Códigos > Código Fiscal\]\.

Para selecionar todos os CFOP’s exibidos na lista, utilize a opção “Marcar todos”\.

Retirando CFOP’s da parametrização de uma determinada Operação

\- Para retirar um CFOP da relação parametrizada, desmarque o CFOP desejado e clique no botão \[Confirmar\] na barra de menu\.

\- Para retirar todos os CFOP’s da relação parametrizada, utilize a opção “Marcar Todos” e clique no botão \[Confirmar\]\. Observe que nesse caso, essa opção funcionará como um “desabilitar todos os marcados”\.

Nos casos em que diferentes operações utilizem o mesmo CFOP, a solução é utilizar naturezas de operação distintas\. Neste caso, a parametrização deve ser feita na opção “[Parâmetros > IN\-RE 048/18 > Operações > Natureza de Operação](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/Estadual/Ressarcimento_de_ICMS_ST_RS/oper_safufrcrs.htm#menu_param_oper_nat)”\.

### <a id="_Toc64492373"></a>– Parâmetros – Operações por Natureza de Operação da IN\-RE 048/18 

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> IN\-RE 048/18>> Operações >> Natureza de Operação

__Descrição:__

Alteração no texto, incluindo o trecho marcado em verde/amarelo:

Natureza de Operação

O objetivo desta parametrização é identificar os CFOP´s/Natureza de Operação por UF e Operação que são considerados na geração dos movimentos de entrada e saída para o Rio Grande do Sul, de acordo com a Instrução Normativa 048/2018\.

Orientação de preenchimento dos campos:

__UF:__ Apresenta a sigla da UF do Rio Grande do Sul\.

__Grupo:__ Selecione o grupo de relacionamento \(Estabelecimento/Grupo/Validade\)\. Se informado um estabelecimento na tela principal do DW, são disponibilizados apenas os grupos relacionados ao estabelecimento em questão, caso contrário, são exibidos os grupos de todos os estabelecimentos da empresa\.

__Operação:__ Selecione a operação, conforme cadastro importado através da tabela TFIX31, para a qual os CFOP’s/Naturezas das Operações são associados:

\- Entrada com Substituição Tributária

\- Saída para Consumidor Final

\- Saída para outro Estado, Saída Isenta ou Não Tributada

__<<<<SÓ NO MANUAL DO MASTERSAF>>__

Obs\.: As Tabelas Fixas \(TFIX\) e Acessórias \(TACES\) são importadas no processo de atualização do patch, mas podem ser importadas, caso necessário, acessar o módulo Básicos \[menu: Ferramentas > Importar\]\.

__CFOP/Naturezas de Operação:__ Selecione os CFOP’s/Naturezas de operação para a operação informada, considerados de acordo com a lista importada através da tabela SAFX2081\.

<a id="_Hlk49851603"></a>Obs\.: Para consultar o cadastro de CFOP/Natureza de Operação \(SAFX2081\) acessar o módulo Básicos \[menu: Data Warehouse > Manutenção > Códigos > CFOP/Natureza de Operação\]\.

Para selecionar todos os CFOP’s/Naturezas de operação exibidos na lista, utilize a opção “Marcar todos”\.

Retirando CFOP’s/Naturezas de operação da parametrização de uma determinada Operação

\- Para retirar um CFOP/Naturezas de operação da relação parametrizada, desmarque o CFOP/Naturezas de operação desejado e clique no botão \[Confirmar\] na barra de menu\.

\- Para retirar todos os CFOP’s/Naturezas de operação da relação parametrizada, utilize a opção “Marcar Todos” e clique no botão \[Confirmar\]\. Observe que nesse caso, essa opção funcionará como um “desabilitar todos os marcados”\.

### <a id="_Toc64492374"></a>– Parâmetros – Operações da IN\-RE 087/20

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> IN\-RE 087/20>> Operações

__Descrição:__

Incluir o tópico para Operações referente a IN\-RE 087/20, com o texto abaixo\.

Operações

Nesse menu são realizadas as parametrizações dos CFOP´s, CFOP’s/Naturezas por UF e Operação que são considerados na rotina de geração dos movimentos a partir das notas fiscais para a apuração do Ressarcimento de ICMS\-ST do Rio Grande do Sul, de acordo com a Instrução Normativa 087/2020\.

É importante se atentar para os Códigos de Motivos de Restitiução/Complementação oriundos da tabela 5\.7 da EFD Fiscal, relacionados às operações parametrizadas\.  

Por exemplo: Na operação com Saída Interna à Consumidor Final \(e Devoluções\) é necessário o cadastro dos Códigos de Motivos RS100, RS300, RS600, RS800\. Esse cadastramento deve ser feito no módulo Básicos 🡪 Data Warehouse, menu Manutenção 🡪 Cadastros 🡪 Códigos de Motivo de Restituição/Complementação de ICMS \(SPED FISCAL\)\.

### <a id="_Toc64492375"></a>– Parâmetros – Operações por CFOP da IN\-RE 087/20 

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> \(IN\-RE 087/20\) >> Operações >> CFOP

__Descrição:__

Incluir o tópico com o texto abaixo\.

CFOP

O objetivo desta parametrização é informar os CFOP´s a serem considerados para cada uma das Operações de Entradas e Saídas, citadas na Instrução Normativa 087/20, para geração dos movimentos \(vide Geração >> \(IN\-RE 087/20\) >> Geração dos Movimentos\)\.

Esta parametrização é utilizada apenas para atendimento à IN\-RE 087/20\. Para a IN\-RE 048/18, devem ser utilizadas as parametrizações do menu “Parâmetros >> IN\-RE 048/18>> Operações”\.

O usuário deve informar os CFOP’s da operação original, e também os CFOP’s das suas devoluções\. Por isso, estarão disponíveis para seleção tanto os CFOP’s de entrada como os de saída\.

Orientação de preenchimento dos campos:

__UF__: Apresenta a sigla da UF do Rio Grande do Sul\.

__Operação__: Selecione a operação, conforme cadastro importado através da tabela TFIX31, para a qual os CFOP’s são associados:

\- Saída Interna para Consumidor Final \(e Devoluções\)

\- Entrada \(e Devoluções\)

__<<<<SÓ NO MANUAL DO MASTERSAF>>__

Obs\.: As Tabelas Fixas \(TFIX\) e Acessórias \(TACES\) são importadas no processo de atualização do patch, mas podem ser importadas, caso necessário, acessar o módulo Básicos \[menu: Ferramentas > Importar\]\.

__CFOP’s:__ Selecione os CFOP’s para a operação informada, considerados de acordo com a lista importada através da tabela SAFX2012\. Além dos CFOP’s da operação em questão, devem ser informados também os CFOP’s referentes às suas devoluções\.

Obs\.: Para consultar o cadastro de CFOP \(SAFX2012\) acessar o módulo Básicos \[menu: Data Warehouse > Manutenção > Códigos > Código Fiscal\]\.

Para selecionar todos os CFOP’s exibidos na lista, utilize a opção “Marcar todos”\.

Retirando CFOP’s da parametrização de uma determinada Operação

\- Para retirar um CFOP da relação parametrizada, desmarque o CFOP desejado e clique no botão \[Confirmar\] na barra de menu\.

\- Para retirar todos os CFOP’s da relação parametrizada, utilize a opção “Marcar Todos” e clique no botão \[Confirmar\]\. Observe que nesse caso, essa opção funcionará como um “desabilitar todos os marcados”\.

Nos casos em que diferentes operações utilizem o mesmo CFOP, a solução é utilizar naturezas de operação distintas\. Neste caso, a parametrização deve ser feita na opção “[Parâmetros > IN\-RE 087/20 > Operações > Natureza de Operação](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/Estadual/Ressarcimento_de_ICMS_ST_RS/oper_safufrcrs.htm#menu_param_oper_nat)”\.

Não esqueça de cadastrar Códigos de Motivos de Restituição/Complementação relacionados às operações que foram parametrizadas, no módulo Básicos 🡪 Data Warehouse, menu Manutenção 🡪 Cadastros 🡪 Códigos de Motivo de Restituição/Complementação de ICMS \(SPED FISCAL\)\.

Operação

Códigos de Motivos de Restituição/Complementação

Saída Interna para Consumidor Final \(e Devoluções\)

- RS100 \- saída com RESSARCIMENTO\-ST \- calculado com base no valor de saída inferior ao valor da BC ICMS ST \- RICMS, Livro III, art\. 25\-B
- RS300 \- saída com COMPLEMENTO\-ST \- calculado com base no valor de saída da mercadoria superior ao valor da BC ICMS ST\- RICMS, Livro III, art\. 25\-B
- RS600 \- entrada com estorno do RESSARCIMENTO\-ST \- entrada em devolução ou retorno de mercadoria não entregue que na saída teve registro no código RS100
- RS800 entrada com estorno do COMPLEMENTO\-ST \- entrada em devolução ou retorno de mercadoria não entregue que na saída teve registro no código RS300

Entrada \(e Devoluções\)

- RS400 \- saída sem RESSARCIMENTO\-ST ou COMPLEMENTO\-ST \- saída em devolução

### <a id="_Toc64492376"></a>– Parâmetros – Operações por Natureza de Operação da IN\-RE 087/20

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> \(IN\-RE 087/20\) >> Operações >> Natureza de Operação

__Descrição:__

Incluir o tópico com o texto abaixo:

<a id="menu_param_oper_nat"></a>Natureza de Operação

O objetivo desta parametrização é identificar os CFOP´s/Natureza de Operação relacionados às Operações de Entradas e Saídas que ensejarem ao contribuinte o direito à restituição, conforme  previsto na Instrução Normativa 087/20\.  Para geração dos movimentos \(vide Geração >> \(IN\-RE 087/20\) >> Geração dos Movimentos\) obrigatoriamente as operações devem ser parametrizadas, nas opções CFOP e/ou Natureza de Operação\.

O objetivo desta parametrização é informar as naturezas de operação a serem consideradas para cada uma das Operações de Entradas e Saídas, citadas na Instrução Normativa 087/20, para geração dos movimentos \(vide Geração >> \(IN\-RE 087/20\) >> Geração dos Movimentos\)\.

Esta parametrização é utilizada apenas para atendimento à IN\-RE 087/20\. Para a IN\-RE 048/18, devem ser utilizadas as parametrizações do menu “Parâmetros >> IN\-RE 048/18>> Operações”\.

O usuário deve informar as naturezas de operação da operação original, e também as naturezas das suas devoluções\. Por isso, estarão disponíveis para seleção tanto os CFOP’s/Naturezas de entrada como os de saída\.

Orientação de preenchimento dos campos:

__UF:__ Apresenta a sigla da UF do Rio Grande do Sul\.

__Grupo:__ Selecione o grupo de relacionamento \(Estabelecimento/Grupo/Validade\)\. Se informado um estabelecimento na tela principal do DW, são disponibilizados apenas os grupos relacionados ao estabelecimento em questão, caso contrário, são exibidos os grupos de todos os estabelecimentos da empresa\.

__Operação:__ Selecione a operação, conforme cadastro importado através da tabela TFIX31, para a qual os CFOP’s/Naturezas das Operações são associados:

\- Saída Interna para Consumidor Final \(e Devoluções\)

\- Entrada \(e Devoluções\)

__<<<<SÓ NO MANUAL DO MASTERSAF>>__

Obs\.: As Tabelas Fixas \(TFIX\) e Acessórias \(TACES\) são importadas no processo de atualização do patch, mas podem ser importadas, caso necessário, acessar o módulo Básicos \[menu: Ferramentas > Importar\]

__CFOP/Naturezas de Operação:__ Selecione os CFOP’s/Naturezas de operação para a operação informada, considerados de acordo com a lista importada através da tabela SAFX2081\.  Além dos CFOP’s/Naturezas da operação em questão, devem ser informados também os CFOP’s/Naturezas referentes às suas devoluções\.

Obs\.: Para consultar o cadastro de CFOP/Natureza de Operação \(SAFX2081\) acessar o módulo Básicos \[menu: Data Warehouse > Manutenção > Códigos > CFOP/Natureza de Operação\]\.

Para selecionar todos os CFOP’s/Naturezas de operação exibidos na lista, utilize a opção “Marcar todos”\.

Retirando CFOP’s/Naturezas de operação da parametrização de uma determinada Operação

\- Para retirar um CFOP/Naturezas de operação da relação parametrizada, desmarque o CFOP/Naturezas de operação desejado e clique no botão \[Confirmar\] na barra de menu\.

\- Para retirar todos os CFOP’s/Naturezas de operação da relação parametrizada, utilize a opção “Marcar Todos” e clique no botão \[Confirmar\]\. Observe que nesse caso, essa opção funcionará como um “desabilitar todos os marcados”\.

Não esqueça de cadastrar Códigos de Motivos de Restitiução/Complementação relacionados às operações que foram parametrizadas, no módulo Básicos 🡪 Data Warehouse, menu Manutenção 🡪 Cadastros 🡪 Códigos de Motivo de Restituição/Complementação de ICMS \(SPED FISCAL\)\.

Operação

Códigos de Motivos de Restitiução/Complementação

Saída Interna para Consumidor Final \(e Devoluções\)

- RS100 \- saída com RESSARCIMENTO\-ST \- calculado com base no valor de saída inferior ao valor da BC ICMS ST \- RICMS, Livro III, art\. 25\-B
- RS300 \- saída com COMPLEMENTO\-ST \- calculado com base no valor de saída da mercadoria superior ao valor da BC ICMS ST\- RICMS, Livro III, art\. 25\-B
- RS600 \- entrada com estorno do RESSARCIMENTO\-ST \- entrada em devolução ou retorno de mercadoria não entregue que na saída teve registro no código RS100
- RS800 entrada com estorno do COMPLEMENTO\-ST \- entrada em devolução ou retorno de mercadoria não entregue que na saída teve registro no código RS300

Entrada \(e Devoluções\)

- RS400 \- saída sem RESSARCIMENTO\-ST ou COMPLEMENTO\-ST \- saída em devolução

### <a id="_Toc64492377"></a>– Parametrização por Produtos

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> Produtos

__Descrição:__

Alteração no texto, incluindo o trecho marcado em verde:

<a id="menu_param_prod"></a>Produtos

O objetivo desta parametrização é identificar os produtos sujeitos a substituição tributária, que são considerados para a apuração do Ressarcimento de ICMS\-ST do Rio Grande do Sul, e que serve tanto para à Instrução Normativa RE 048/2018, como a RE 087/2020\.  

Além da parametrização dos produtos por código, também pode ser realizada por NCM \- Nomenclatura Comum do Mercosul ou por CEST \- Código Especificador da Substituição Tributária, opções disponíveis no menu Parâmetros > Produtos > [Por NCM](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/Estadual/Ressarcimento_de_ICMS_ST_RS/oper_safufrcrs.htm#menu_param_prod_NCM) e [Por CEST](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/Estadual/Ressarcimento_de_ICMS_ST_RS/oper_safufrcrs.htm#menu_param_prod_CEST)\.

As três modalidades de parametrização de produtos \(por Código, por NCM e por CEST\) são utilizadas simultaneamente, no processo de geração, com a seguinte prioridade de pesquisa:

\- Verifica\-se se o produto consta na parametrização por Código;

\- Caso sim, a parametrização por NCM e por CEST não são verificadas;

\- Caso não, o produto é pesquisado na parametrização por NCM, e por último, na parametrização por CEST\.

Desta forma, é possível analisar qual das três parametrizações é mais interessante para cada caso, lembrando que não é necessário utilizar as três parametrizações para os mesmos produtos\.

__ATENÇÃO__: 

1\) Para o processo de geração dos movimentos é obrigatória a parametrização de pelo menos uma das opções de produtos a seguir, com vigência abrangido o período da geração\. 

2\) Para geração dos movimentos da RE 087/2020 que envolvam devoluções de saídas, a vigência da parametrização deve cobrir a data da emissão de notas de saídas que estão sendo devolvidas no período da geração\. Exemplo: Dado um período de Janeiro/2021, onde as notas de devolução de saídas desse período referenciam notas de saída emitidas em Outubro de 2020\. A parametrização do produto devolvido deve ter uma vigência que acoberte outubro de 2020 a janeiro/2021\.

### <a id="_Toc64492378"></a>– Parametrização por Produtos – Por Código

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> Produtos >> Por Código

__Descrição:__

Alteração no texto, incluindo o trecho marcado em verde:

<a id="menu_param_prod_cod"></a>Por Código

A informação dos produtos parametrizados é utilizada nas rotinas de geração dos cálculos dos movimentos\.

Tratar\-se de uma parametrização por Empresa e UF que também pode ser realizada através da importação da tabela SAFX104 \- Parâmetros de Produto por UF \(Ressarcimento e Complemento de ICMS\-ST\)\.

Obs\.: Para maiores detalhes consultar o Manual Layout no módulo Básicos \[menu: Job Servidor > Carga > Manual de Layout SAFX > Selecionar tabela na aba Tabela SAFX > Consultar na aba Layout SAFX / ou baixar o Manual Layout na Base de Conhecimento do Contact Center\]\.

Nessa opção, é aberta automaticamente a janela de seleção do GRUPO, obrigando a seleção do grupo desejado\. Esse grupo é utilizado para filtro dos produtos na tabela SAFX2013 – Tabela de Produtos, só permitindo parametrização dos produtos para o grupo escolhido\.

Orientação de preenchimento dos campos:

__Estado:__ O sistema traz a sigla da UF do Rio Grande do Sul \- RS\. Esse campo não é editável por utilizarmos produtos associados somente para esse estado\.

__Produto:__ Esse campo utiliza duas funcionalidades:

\- Clique na pasta para selecionar o produto de acordo com a Tabela de Produtos \(SAFX2013\)\. São considerados apenas os produtos do Grupo escolhido na abertura da tela;

\- Selecione um dos indicadores do produto descritos abaixo e digite o código do produto:

1 – Produto Acabado;

2 \- Matéria Prima/Insumo;

3 \- Embalagem;

4 \- Material Uso/Consumo;

5 \- Outros;

6 \- Em Elaboração;

7 \- Intermediário;

8 \- Miscelâneas\.

Obs: Para consultar o cadastro de Produto \(SAFX2013\) acessar o módulo Básicos \[menu: Data Warehouse > Manutenção > Códigos > Produto\]\.

__Alíquota Interna:__ Informar obrigatoriamente a alíquota interna para o produto parametrizado\.

Blá, blá, blá

### <a id="_Toc64492379"></a>– Parametrização por Produtos – Por NCM

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> Produtos >> Por NCM

__Descrição:__

Alteração no texto, incluindo o trecho marcado em verde:

<a id="menu_param_prod_NCM"></a>Por NCM

A informação de parametrização dos produtos por NCM \- Nomenclatura Comum do Mercosul para o estado do RS é utilizada nas rotinas de geração dos movimentos a partir das notas fiscais\.

Essa tela apresenta na parte inferior “Informe os NCMs a serem incluídos na parametrização” todos os códigos NCM’s\. A partir de uma seleção, todos os NCM’s podem ser adicionados a “Relação dos NCM’s parametrizados” à lista superior\.

Descreveremos a seguir as funcionalidades para incluir, excluir ou alterar NCM’s na parametrização:

Orientação de preenchimento dos campos:

Blá, blá, blá Blá, blá, blá

Blá, blá, blá Blá, blá, blá

Blá, blá, blá Blá, blá, blá

Alteração de NCM’s da parametrização

\- Os únicos campos habilitados para alteração são: Validade Final, Alíquota Interna, % de Redução de BC e Alíquota FCP\.

Ao final clique no botão \(Confirmar\) na barra de menu\.

__Atualizar a Validade Final dos itens selecionados para:__ Utilize esse campo para informar simultaneamente a validade final para vários itens da parametrização\. Para isso, marque os tens desejados no campo “Relação dos NCM’s Parametrizados”, informe uma data para a validade final e clique no botão “Atualizar”\. Se desejar atualizar a Validade Final de todos os NCM’s da relação parametrizada, utilize a opção “Marcar Todos” na tela superior\.

__Atualizar:__ Através desse botão, todos os itens marcados são alterados para a data de validade final informada no campo “Atualizar a Validade Final dos itens selecionados para”, exceto aqueles cuja validade inicial seja superior à data de validade final informada\. Para confirmar a atualização, clique no botão “Confirmar” na barra de menu\.

__Código/Descrição para pesquisa:__ Para pesquisa, informe os caracteres iniciais do código ou da descrição dos NCM’s pesquisados na Tabela de NCM’s \(SAFX2043\), selecione o tipo de pesquisa e clique no botão “Pesquisar”\. Essa funcionalidade é um facilitador para visualizar no campo “Informe os NCM’s a serem incluídos na parametrização” apenas os NCM’s do código ou descrição informados\.

Quando esta opção não for utilizada, todos os NCM’s da Tabela de NCM’s \(SAFX2043\) são visualizados na lista do campo “Informe os NCM’s a serem incluídos na parametrização”\.

<a id="_Hlk49789520"></a>Obs\.: Para consultar o cadastro de NBM \(SAFX2043\) acessar o módulo Básicos \[menu: Data Warehouse > Manutenção > Códigos > Código NBM\]\.

Quando essa opção for utilizada para uma determinada pesquisa, e for necessário visualizar novamente todos os NCM’s parametrizados, limpe o campo, e clique novamente na opção “Pesquisar”\.

__\- Código:__ Ao marcar essa opção, a pesquisa é realizada pelos códigos dos NCM’s demonstrados no campo “Informe os NCM’s a serem incluídos na parametrização”\.

__\- Descrição:__ Ao marcar essa opção, a pesquisa é realizada pelas descrições dos NCM’s demonstrados no campo “Informe os NCM’s a serem incluídos na parametrização”\.

__\- Pesquisar:__ Ao clicar nessa opção, são listados no campo “Informe os NCM’s a serem incluídos na parametrização” os NCM’s para o critério de pesquisa informado\.

__Informe os NCM’s a serem incluídos na parametrização:__ Apresenta a relação de NCM’s da Tabela de NCM’s \(SAFX2043\)\. O objetivo deste quadro é permitir a seleção dos NCM’s que são inseridos na parametrização\. Para isso, selecione os NCM’s desejados, informe a data de Validade Inicial e a Alíquota Interna \(campos obrigatórios\), se for o caso, informe os campos % de Redução de BC e Alíquota FCP\. Clique no botão “Adicionar à lista” para adicionar os NCM’s selecionados na “Relação dos NCM’s Parametrizados”\.

Obs\.: Para consultar o cadastro de NBM \(SAFX2043\) acessar o módulo Básicos \[menu: Data Warehouse > Manutenção > Códigos > Código NBM\]\.

Para selecionar todos os NCM’s exibidos na lista, utilize a opção “Marcar todos”\.

Blá, blá, blá Blá, blá, blá

Blá, blá, blá Blá, blá, blá

Blá, blá, blá Blá, blá, blá

### <a id="_Toc64492380"></a>– Parametrização por Produtos – Por CEST

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> Produtos >> Por CEST

__Descrição:__

Alteração no texto, incluindo o trecho marcado em verde/amarelo:

<a id="menu_param_prod_CEST"></a>Por CEST

A informação de parametrização dos produtos por CEST \- Código Especificador da Substituição Tributária para o estado do RS é utilizada nas rotinas de geração dos movimentos a partir das notas fiscais\.

Essa tela apresenta na parte inferior “Informe os CESTs a serem incluídos na parametrização” todos os códigos CEST’s\. A partir de uma seleção, todos os CEST’s podem ser adicionados a “Relação dos CEST’s parametrizados” à lista superior\.

Descreveremos a seguir as funcionalidades para incluir, excluir ou alterar CEST’s na parametrização:

Orientação de preenchimento dos campos:

Blá, blá, blá Blá, blá, blá

Blá, blá, blá Blá, blá, blá

Blá, blá, blá Blá, blá, blá

Alteração de CEST’s da parametrização

\- Os únicos campos habilitados para alteração são: Validade Final, Alíquota Interna, % de Redução de BC e Alíquota FCP\.

Ao final clique no botão \(Confirmar\) na barra de menu\.

__Atualizar a Validade Final dos itens selecionados para:__ Utilize esse campo para informar simultaneamente a validade final para vários itens da parametrização\. Para isso, marque os tens desejados no campo “Relação dos CEST’s Parametrizados”, informe uma data para a validade final e clique no botão “Atualizar”\.

Se desejar atualizar a Validade Final de todos os CEST’s da relação parametrizada, utilize a opção “Marcar Todos” na tela superior\.

__Atualizar:__ Através desse botão, todos os itens marcados são alterados para a data de validade final informada no campo “Atualizar a Validade Final dos itens selecionados para”, exceto aqueles cuja validade inicial seja superior à data de validade final informada\.

Para confirmar a atualização, clique no botão “Confirmar” na barra de menu\.

__Código/Descrição para pesquisa: __Para pesquisa, informe os caracteres iniciais do código ou da descrição dos CEST’s pesquisados na Tabela de CEST’s \(TACES94\) selecione o tipo de pesquisa e clique no botão “Pesquisar”\. Essa funcionalidade é um facilitador para visualizar no campo “Informe os CEST’s a serem incluídos na parametrização” apenas os CEST’s do código ou descrição informados\.

Quando esta opção não for utilizada, todos os CEST’s da Tabela de CEST’s \(TACES94\) são visualizados na lista do campo “Informe os CEST’s a serem incluídos na parametrização”\.

Quando essa opção for utilizada para uma determinada pesquisa, e for necessário visualizar novamente todos os CEST’s parametrizados, limpe o campo, e clique novamente na opção “Pesquisar”\.

__\- Código:__ Ao marcar essa opção, a pesquisa é realizada pelos códigos dos CEST’s demonstrados no campo “Informe os CEST’s a serem incluídos na parametrização”\.

__\- Descrição:__ Ao marcar essa opção, a pesquisa é realizada pelas descrições dos CEST’s demonstrados no campo “Informe os CEST’s a serem incluídos na parametrização”\.

__\- Pesquisar:__ Ao clicar nessa opção, são listados no campo “Informe os CEST’s a serem incluídos na parametrização” os CEST’s para o critério de pesquisa informado\.

__Informe os CEST’s a serem incluídos na parametrização:__ Apresenta a relação de CEST’s da Tabela de CEST’s \(TACES94\)\. O objetivo deste quadro é permitir a seleção dos CEST’s que são inseridos na parametrização\. Para isso, selecione os CEST’s desejados, informe a data de Validade Inicial e a Alíquota Interna \(campos obrigatórios\), se for o caso, informe os campos % de Redução de BC e Alíquota FCP\. Clique no botão “Adicionar à lista” para adicionar os CEST’s selecionados na “Relação dos CEST’s Parametrizados”\.

__<<<<SÓ NO MANUAL DO MASTERSAF>>__

<a id="_Hlk50497359"></a>Obs\.: As Tabelas Fixas \(TFIX\) e Acessórias \(TACES\) são importadas no processo de atualização do patch, mas podem ser importadas, caso necessário, acessar o módulo Básicos \[menu: Ferramentas > Importar\]\.

Para selecionar todos os CEST’s exibidos na lista, utilize a opção “Marcar todos”\.

Blá, blá, blá Blá, blá, blá

Blá, blá, blá Blá, blá, blá

Blá, blá, blá Blá, blá, blá 

### <a id="_Toc64492381"></a>– Menu Geração

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Geração

__Descrição:__

Refazer o texto:

<a id="menu_gerar"></a>Menu Geração

Nesse menu é possível realizar o processamento das gerações para atendimento as Instruções Normativas RE 048/2018 e RE 087/2020\.   através dos documentos fiscais \(SAFX07 e SAFX08\), finalizando com a gravação de um conjunto de tabelas que compõe a subapuração RS, base para a geração dos registros 1920, 1921 e 1923 do SPED FISCAL

Nesse menu é possível realizar o processamento das gerações que resultará na gravação de um conjunto de tabelas base para geração dos registros do SPED FISCAL\. Na geração para atendimento a IN RE 048/2018 o resultado é atribuído às tabelas que geram a Subapuração do SPED FISCAL \(registros 1920, 1921 e 1923\)\. Veja:

\- Tabela de Subapuração do RS \(Registro 1920\);

\- Tabela dos Ajustes da Subapuração do RS \(Registro 1921\);

\- Tabela de Identificação dos Documentos Fiscais dos Ajustes da Subapuração do RS \(Registro 1923\)\.

Na geração para atendimento a IN RE 087/2020 o resultado é atribuído às tabelas que geram os registros C180, C181, C185 e C186 do SPED FISCAL\. Veja:

\- Tabela de Informações Complementares das Operações Sujeitas ao ST \(C180, C185 e C380\)

\- Tabela de Informações Complementares das Operações de Devolução Sujeitas ao ST \(C181 e C186\)

### <a id="_Toc64492382"></a>– Geração dos Movimentos – IN\-RE 048/19

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Geração >> \(IN\-RE 048/18\) >> Geração dos Movimentos

 

__Descrição:__

Alteração no texto, incluindo o trecho marcado em verde

<a id="menu_gerar_mov"></a>Geração dos Movimentos

O processamento da geração dos movimentos atende à contribuintes Varejistas e Não Varejistas e, de acordo o estabelecido na IN\-RE 048/2018, os contribuintes Varejistas devem prestar informações relacionadas à:

\- Movimentos de Entradas,

\- Movimentos de Saídas para Consumidor Final,

\- Movimentos de Saídas para outras UF’s, Isentas ou Não Tributadas\.

Os Não Varejistas precisam demonstrar:

\- Movimentos de Entradas;

\- Movimentos de Saídas para Consumidor Final\.

Para gerar essas movimentações, opções são disponibilizados na tela de Geração do Movimento: “Gerar saídas para Consumidor Final”, “Gerar Entradas” e “Gerar saídas para Outras UF’s, Isentas ou Não Tributadas”\. O uso dos parâmetros deve estar alinhado com a definição do contribuinte ser varejista ou não \(vide parametrização dos Dados Iniciais\)\.

Todas as opções de Geração dos Movimentos baseiam\-se nos documentos fiscais \(SAFX07\) cujos itens de mercadoria \(SAFX08\) tenham produtos parametrizados em uma das opções disponíveis no menu Parâmetros > Produto, e CFOP ou CFOP/Natureza parametrizados para uma das operação abordadas na IN\-RE 048/2018 \(ver detalhes no help das [Parametrizações](http://www.mastersaf.com.br/HELPDW/V2R010/Estadual/Ressarcimento_de_ICMS_ST_RS/oper_safufrcrs.htm#menu_param)\)\.

O resultado desse processamento pode ser conferido nos Relatórios de Conferência dos Movimentos disponíveis no módulo \(menu [Relatórios > Conferência dos Movimentos](http://www.mastersaf.com.br/HELPDW/V2R010/Estadual/Ressarcimento_de_ICMS_ST_RS/oper_safufrcrs.htm#menu_relat_conf_mov)\), onde poderão ser analisados os seguintes dados:

__\- Sub\-Apuração RS \(registro 1920\):__ Sub\-Apuração calculada a partir dos lançamentos, demonstrando um saldo a recolher ou a creditar de ICMS\-ST\.

__\- Ajustes da Sub\-Apuração \(registro 1921\) :__ Lançamentos realizados com os totais das movimentações e código de ajuste especificado na IN 048/2018, parametrizado na tela de Dados Iniciais \(ver detalhes no help das [Parametrizações](http://www.mastersaf.com.br/HELPDW/V2R010/Estadual/Ressarcimento_de_ICMS_ST_RS/oper_safufrcrs.htm#menu_param)\)\.

__\- Identificação dos Documentos fiscais \(registro 1923\) : __Item a item dos documentos fiscais que compuseram o lançamento\.

__Limpeza dos lançamentos gerados pela Transferência entre Apurações__

Nos casos em que houver reprocessamento da geração do movimento após a execução do processo de transferência entre apurações, a geração dos movimentos apagará os lançamentos de transferência realizados na Sub\-Apuração e na Apuração do ICMS\-ST \(P9\-ST\)\.

Dependência com a tela de parametrização de Dados Iniciais:

Definir se o contribuinte é Varejista ou Não Varejista;

Realizar a parametrização das informações que são obrigatórias para a geração:

\- Sub\-Apuração

\- Código de Ajuste de SPED Fiscal\.

<a id="_Hlk49863629"></a>Obs\.: Para consultar o cadastro do Código de Ajuste SPED FISCAL, acessar o módulo Estadual \[menu: ICMS > Apuração > Apuração do ICMS > Lançamentos Complementares > Código de Ajuste \(SPED FISCAL\)\]\.

__Dependência com as telas de parametrizações de Produtos e Operações:__

__Parametrização de Produtos:__ por Código, por NCM ou por CEST;

__Parametrização de Operações:__ CFOP e CFOP/Natureza de Operação\.

__Dependência das Entradas para Saídas a Consumidor Final – para contribuintes Não Varejistas:__

A geração da entrada \(Não Varejista\) tem como pré\-requisito a execução da geração da saída para consumidor final\. Logo, para contribuintes Não Varejistas, duas situações são proibidas:

\- Gerar a entrada sem a existência de movimento de saída para consumidor final para o estabelecimento/período/livro informados\.

\- Gerar novamente a saída para consumidor final sem realizar novamente a geração da entrada, no caso que existam movimentos de saída e entrada gerados para o estabelecimento/período/livro\.

__Sobre as Notas Fiscais de Saídas para Consumidor Final__

Mapeamos aqui campos da SAFX08 utilizado na geração do movimento:

\- Produto \(campos 13 e 14 da SAFX08\)

\- CFOP \(campo 22 da SAFX08\)

\- Natureza de Operação \(campo 23 da SAFX08\) \- opcional\.

\- Quantidade \(campo 24 da SAFX08\)\.

\- Medida \(campo 25 da SAFX08\)\.

\- Valor Contábil do Item \(campo 64 da SAFX08\)\.

\- Para identificar a última nota fiscal de entrada do produto vendido, os campos relacionados a Documento Fiscal de Referência podem ser preenchidos \(campos <a id="_Hlk49935761"></a>102\-Data DI / Data Doc Refer”, “117\-Número do Documento Fiscal de Referência”, “118\-Série do Documento Fiscal de Referência” e “119\-Subsérie do Documento Fiscal de Referência” da SAFX08\) – opcionalmente e somente para não varejistas\.

__Sobre as Notas Fiscais de Saídas para Outras UF’s, Isentas ou Não Tributadas__

Mapeamos aqui campos da SAFX08 utilizados na geração do movimento:

\- Produto \(campos 13 e 14 da SAFX08\)

\- CFOP \(campo 22 da SAFX08\)

\- Natureza de Operação \(campo 23 da SAFX08\) \- opcional\.

\- Quantidade \(campo 24 da SAFX08\)\.

\- Medida \(campo 25 da SAFX08\)\.

\- Para identificar a última nota fiscal de entrada do produto vendido, os campos relacionados a Documento Fiscal de Referência podem ser preenchidos \(campos 102\-Data DI / Data Doc Refer”, “117\-Número do Documento Fiscal de Referência”, “118\-Série do Documento Fiscal de Referência” e “119\-Subsérie do Documento Fiscal de Referência” da SAFX08\) – opcionalmente e somente para varejistas\.

__Sobre as Notas Fiscais de Entradas sujeitas a Substituição Tributária__

Mapeamos aqui campos da SAFX08 utilizado na geração do movimento:

\- Produto \(campos 13 e 14 da SAFX08\)

\- CFOP \(campo 22 da SAFX08\)

\- Natureza de Operação \(campo 23 da SAFX08\) \- opcional\.

\- Quantidade \(campo 24 da SAFX08\)\.

\- Medida \(campo 25 da SAFX08\)\.

\- Valor Contábil do Item \(campo 64 da SAFX08\)\.

__\- Valor do ICMS:__ um dos campos abaixo relacionados ao ICMS são considerados:

\- Campo 43 \- Valor ICMS, se preenchido, ou

\- Campo 80 \- ICMS não Escriturado, se preenchido, ou

\- Campo 225 \- Valor ICMS Não Destacado\.

__\- Valor do ICMS\-ST:__ um dos campos abaixo relacionados ao ICMS\-ST são considerados:

\- Campo 52 \- Valor ICMS Substituição Tributária, se preenchido, ou

\- Campo 145 \- Valor de ICMS\-ST não Escriturado, se preenchido, ou

\- Campo 133 \- ICMS\-ST Não Escriturado, se preenchido, ou

\- Campo 107 \- Valor Carga Tributária Origem, se preenchido\.

\- Valor do FECEP ICMS\-ST \(campo 140 da SAFX08\)\.

Obs\.: Para maiores detalhes consultar o Manual Layout no módulo Básicos \[menu: Job Servidor > Carga > Manual de Layout SAFX > Selecionar tabela na aba Tabela SAFX > Consultar na aba Layout SAFX / ou baixar o Manual Layout na Base de Conhecimento do Contact Center\]\.

__Sobre Conversão de Medida:__

Caso existam operações onde o produto é comercializado numa unidade de medida diferente da unidade padrão do cadastro, é pré\-requisito que os fatores de conversão estejam cadastrados nas tabelas de conversão de medida\.  Para isso acesse o módulo Básicos 🡪 Data Warehouse, menu Manutenção > Cadastros > Conversão de Unidades de Medida, opções Padrão ou Por Produto\.

Durante a geração dos movimentos é verificado se a unidade de medida do documento fiscal é a mesma unidade do cadastro\. Caso contrário, recupera a informação do fator de conversão e converte a quantidade para a unidade do Cadastro do Produto\.

A comparação das unidades \(movimento x cadastro\) é feita a partir dos campos "Unidade de Medida", referentes ao Código de Unidade da SAFX2007\. O motivo é que as tabelas de conversão de medida do módulo DW trabalham com este campo\. Já na geração do Registro 0200 do SPED FISCAL, a medida utilizada é a do campo "Unidade Padrão", referente ao código da SAFX2017 \(cujo código é maior\)\.

Assim, também é pré\-requisito que os dois campos de unidade \("Unidade de Medida" da SAFX2007, e "Unidade Padrão" da SAFX2017\) estejam sempre preenchidos no Cadastro do Produto, e que nos documentos, esteja preenchido o campo "Unidade de Medida" da SAFX2007\.

<a id="_Hlk49789015"></a><a id="_Hlk49935842"></a>Obs\.: Para consultar o cadastro de medidas \(SAFX2007\) acessar o módulo Básicos \[menu: Data Warehouse > Manutenção > Códigos > Medida\]\.

<a id="_Hlk49188506"></a>Obs\.: Para consultar o cadastro de unidade padrão \(SAFX2017\) acessar o módulo Básicos \[menu: Data Warehouse > Manutenção > Códigos > Unidade Padrão\]\.

__Obs\.:__ Em outros módulos de Ressarcimento de ICMS\-ST, o usuário pode, opcionalmente, informar a quantidade já convertida no campo “137 \- Quantidade Convertida" da SAFX08, e nesse caso, ao invés de efetuar a conversão, é utilizada a informação deste campo\. No entanto, neste módulo este campo não é utilizado\.

Nessa tela, as opções de geração foram relacionadas da forma abaixo e pelo menos uma das opções deve ser selecionada:

\- Gerar Entradas

\- Gerar saídas para Consumidor Final

\- Gerar saídas para Outras UF's, Isentas e Não Tributadas \(Varejista\)

Descrição dos campos

__Tipo de Execução:__ Informar o tipo de execução\. Podendo ser: Imediata ou Programada\.

__Data/Hora de Execução:__ Informar a data e hora que deseja fazer a geração dos movimentos\.

__Gerar por Inscrição Estadual Única:__ Este parâmetro se encontra desabilitado, pois não está disponível a geração do Ressarcimento RS para empresas cuja entrega de obrigações se dá por Inscrição Estadual Única\.

__Período:__ Informar o período \(mês e ano\) para a recuperação dos dados dos documentos fiscais\.

__Gerar Saídas para Consumidor Final:__ Se essa opção for selecionada, é executada a geração que recupera toda movimentação das saídas para Consumidor Final desse estado pertencente ao período da geração, dos produtos sujeitos ao ICMS\-ST, gerando um lançamento em Outros Débitos na Sub\-Apuração\.

__Obs\.:__ Esta geração atende a contribuintes Varejistas e Não Varejistas\.

__Gerar Entradas:__ Essa geração considera a parametrização informada no campo “Contribuinte Varejista” na tela de Dados Iniciais\. Ao marcarmos esse campo teremos as seguintes condições:

Se o contribuinte for Varejista: É executada a geração dos movimentos de entradas com Substituição Tributária, pertencente ao período informado, gerando um lançamento em Outros Créditos na Sub\-Apuração\.

Se o contribuinte for Não Varejista: É executada a geração dos movimentos de entradas com Substituição Tributária de produtos existentes no movimento de Saída para Consumidor Final gerado no período\. A partir do produto presente no item da nota de saída para Consumidor Final, é recuperada a última nota de entrada desse produto, cuja identificação se faz de duas formas:

\- Se a última nota de entrada for referenciada pelo item da nota de saída para Consumidor Final, através do preenchimento dos campos Número do Docto\. Fiscal de Referência, Série do Docto\. Fiscal de Referência, Subsérie do Docto\. Fiscal de Referência e Data DI \(campos <a id="_Hlk49863754"></a>102\-Data DI / Data Doc Refer”, “117\-Número do Documento Fiscal de Referência”, “118\-Série do Documento Fiscal de Referência” e “119\-Subsérie do Documento Fiscal de Referência”* *da SAFX08\), a geração buscará a nota fiscal de entrada considerando os dados de referência;

\- Se a última nota de entrada não for referenciada pelo item da nota de saída para Consumidor Final, é recuperada a nota de entrada cuja data fiscal seja a mais próxima da data fiscal da nota de saída\. Neste caso, a nota de entrada pode ser encontrada em períodos anteriores ao da geração, até a data informada em “Pesquisar Últimas entradas até”\.

__Observação:__ Existe uma dependência da Geração das Entradas para a Geração da Saída para Consumidor Final, no caso do contribuinte ser Não Varejista\. Portanto:

\- A Geração da Entrada deve executada em conjunto com a Geração das Saídas para Consumidor;

\- A Geração da Entrada deve executada após a Geração das Saídas para Consumidor\.

__Gerar Saídas para Outras UF’s, Isentas e Não Tributadas \(Varejista\):__ Se essa opção for selecionada, é executada a geração que recupera toda a movimentação das saídas para outras UF’s, Isentas ou Não tributadas, pertencente ao período da geração, e gera um lançamento em Estorno de Crédito na Sub\-Apuração\.

Nessa geração, consideraremos as notas fiscais de entrada acompanhadas das notas de saídas que são demonstradas no Relatório de Conferência da Saídas para Outras UFs, Isentas ou Não tributadas, a fim de esclarecer o cálculo do valor do ajuste das saídas a partir dos valores das entradas\.

A partir do produto presente no item da nota de saída para outras UF’s, Isentas ou Não Tributadas, é recuperada a última nota de entrada desse produto, cuja identificação se faz de duas formas:

\- Se a última nota de entrada for referenciada pelo item da nota de saída, através do preenchimento dos campos Número do Docto\. Fiscal de Referência, Série do Docto\. Fiscal de Referência, Subsérie do Docto\. Fiscal de Referência e Data DI \(campos 102\-Data DI / Data Doc Refer”, “117\-Número do Documento Fiscal de Referência”, “118\-Série do Documento Fiscal de Referência” e “119\-Subsérie do Documento Fiscal de Referência”* *da SAFX08\), geração buscará a nota fiscal de entrada considerando os dados de referência;

\- Se a última nota de entrada não for referenciada pelo item da nota de saída, é recuperada a nota de entrada cuja data fiscal seja a mais próxima da data fiscal da nota de saída\. Neste caso, a nota de entrada pode ser encontrada em períodos anteriores ao da geração, até a data informada em “Pesquisar Últimas entradas até”\.

__Obs\.:__ As notas fiscais estão sendo gravadas na tabela de Identificação dos Documentos fiscais objetivando a conferência através do relatório disponível neste módulo, pois o SPED Fiscal não exige a geração do registro 1923 para tais notas\.

__Pesquisar Últimas Entradas até:__ Neste campo deve ser informada a data limite para a pesquisa das últimas notas de entrada do produto\. Esse campo é habilitado/desabilitado a partir da seleção do campo “Gerar Entradas” e “Gerar saídas para Outras UF's, Isentas ou Não Tributadas \(Varejista\)”\.

__Utilizar DATA MART nos Movimentos de Entrada: __Este parâmetro permite que os movimentos de entrada sejam lidos das tabelas do DATA MART\. Pela necessidade de busca dos documentos fiscais de entrada em períodos anteriores, por padrão a recuperação desses documentos é feita pelas tabelas de documentos fiscais definitivas \(X07, X08\)\. Mas caso seja de interesse melhorar a performance da geração, pode\-se utilizar essa opção para que os movimentos de entrada sejam lidos das tabelas do DATA MART\. Atentar\-se para que o DATA MART esteja equalizado tanto para o período da geração quanto para os períodos anteriores até a data definida no campo “Pesquisar Últimas Entradas até”\.

__Estabelecimento:__ Lista os estabelecimentos da empresa informada\. São disponibilizados, para seleção, apenas os estabelecimentos do Rio Grande do Sul \- RS\.

__Selecionar:__ Utilize como facilitador para selecionar um ou mais estabelecimentos da empresa através de uma janela de seleção da tabela de estabelecimentos da UF do RS\. Ao selecionar os estabelecimentos nessa opção, ao clicar no botão \[OK\] da tela, os estabelecimentos são demonstrados marcados no campo “Estabelecimentos”\.

__Marcar Todos:__ Possibilita marcar/desmarcar a seleção de todos os estabelecimentos para geração dos dados\.

__Botão Executar:__ Realiza o processo de geração dos dados para os critérios informados\.

### <a id="_Toc64492383"></a>– Confêrência dos Movimentos \- IN\-RE 048/18

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Relatórios >> \(IN\-RE 087/20\) >> Conferência dos Movimentos

 

__Descrição:__

Corrigir os erros de português:

__Saídas para Outras UF’s, Isentas ou Não Tributadas \(Varejistas\):__ Ao marcar essa opção é gerado o relatório de conferência dos Movimentos de Saídas para Outras UF’s, Isentas ou Não Tributadas para os contribuintes Varejistas parametrizados na tela de dados Iniciais\. O relatório apresenta exatamente as informações que são geradas na opção Geração dos Movimentos, onde cada documento fiscal de saída é <a id="_Hlk49936053"></a>demosntrado demonstrando com sua respectiva nota de entrada, assim como, os documentos fiscais de saída, cuja nota de entrada não foi encontrada\.

Os valores dos ajustes das notas de saídas são totalizados gerando o valor do lançamento de estorno de crédito na Sub\-Apuração\.

Os valores dos <a id="_Hlk49936061"></a>ajutes ajustes das notas de entradas NÃO são totalizados para gerar o valor do lançamento à crédito na Sub\-Apuração\.

Apenas o valor total dos ajustes das notas de Saída é demonstrado ao final do relatório por estabelecimento, pois é um lançamento apresentado no registro 1921 no SPED FISCAL\.

### <a id="_Toc64492384"></a>– Geração dos Movimentos \- IN\-RE 087/20

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Geração >> \(IN\-RE 087/20\) >> Geração dos Movimentos

 

__Descrição:__

Geração dos Movimentos baseia\-se no processamento dos documentos fiscais \(SAFX07\) cujos itens de mercadoria \(SAFX08\) tenham produtos sujeitos ao ICMS\-ST, parametrizados em uma das opções disponíveis no menu Parâmetros > Produto, e CFOP ou CFOP/Natureza parametrizados para uma das operação abordadas na IN\-RE 087/2020 \(ver detalhes no help das [Parametrizações](http://www.mastersaf.com.br/HELPDW/V2R010/Estadual/Ressarcimento_de_ICMS_ST_RS/oper_safufrcrs.htm#menu_param)\)\. O resultado do processamento são os movimentos contendo os valores exigidos pelos registros C180, C181, C185, C186 do Sped Fiscal, cuja conferência pode ser realizada através de relatórios em arquivos com extensão “csv”, disponibilizados na aba “Arquivo”\.  Os relatórios são disponibilizados apenas em Excel, e não é demonstrado em tela\. 

__Configurações Iniciais__:

Para iniciar a utilização dessa rotina, primeiramente é necessário realizar os seguintes cadastros e parametrizações:

\- Parametrização de Produtos sujeitos ao ICMS\-ST\.  Acesse o menu Parâmetros > Produto, opções por Código, por NCM ou por CEST;

\- Parametrização de CFOP ou CFOP/Natureza\.  Acesse o menu Parâmetros > IN\-RE 087/20 > Operações, opções CFOP ou Natureza de Operações;

\- Cadastro de Motivo de Restitiução/Complementação\.  Acesse o módulo Básicos \[menu: Data Warehouse > Manutenção > Cadastros > Códigos de Motivo de Restituição/Complementação de ICMS \(SPED FISCAL\)\]\.

Cada Operação relacionada ao CFOP ou CFOP/Natureza na parametrização disponível no menu Parâmetros > IN\-RE 087/20 >> Operações, exige o cadastro de uma faixa de Códigos de Motivo estabelecidos na tabela 5\.7 do Sped Fiscal\. Ex: Para Saída Interna para Consumidor Final \(e Devoluções\) é necessário o cadastro dos códigos de motivo RS100, RS300, RS600 e RS800\. Para Entrada \(e Devoluções\), o código RS400\. 

\- <a id="Conv_Medidas"></a>Cadastro de Conversão de Unidades de Medidas:

Caso existam operações onde o produto é comercializado numa unidade de medida diferente da unidade padrão do cadastro, é pré\-requisito que os fatores de conversão estejam cadastrados nas tabelas de conversão de medida\. Para isso acesse o módulo Básicos \[menu: Data Warehouse > Manutenção > Cadastros > Conversão de Unidades de Medida, opções Padrão ou Por Produto\]\.

Durante a geração dos movimentos é verificado se a unidade de medida do documento fiscal é a mesma unidade do cadastro\. Caso contrário, recupera a informação do fator de conversão cadastrado para a Medida Origem = Medida do documento fiscal e Medida Destino = Medida do produto e converte a quantidade para a unidade do Cadastro do Produto\.

A comparação das unidades \(movimento x cadastro\) é feita a partir dos campos "Unidade de Medida", referentes ao Código de Unidade da SAFX2007\. O motivo é que as tabelas de conversão de medida do módulo DW trabalham com este campo\. Já na geração do Registro 0200 do SPED FISCAL, a medida utilizada é a do campo "Unidade Padrão", referente ao código da SAFX2017 \(cujo código é maior\)\.

Assim, também é pré\-requisito que os dois campos de unidade \("Unidade de Medida" da SAFX2007, e "Unidade Padrão" da SAFX2017\) estejam sempre preenchidos no Cadastro do Produto, e que nos documentos, esteja preenchido o campo "Unidade de Medida" da SAFX2007\.

Obs1\.: Para consultar o cadastro de medidas \(SAFX2007\) acessar o módulo Básicos \[menu: Data Warehouse > Manutenção > Códigos > Medida\]\.

Obs2\.: Para consultar o cadastro de unidade padrão \(SAFX2017\) acessar o módulo Básicos \[menu: Data Warehouse > Manutenção > Códigos > Unidade Padrão\]\.

Obs3\.: É possível informar a quantidade já convertida no campo “137 \- Quantidade Convertida da SAFX08, e nesse caso, não há necessidade de realizar o Cadastro da Conversão de Unidades de Medidas\.

__Sobre a Carga Mensal__:

A cada período da geração é necessário que as seguintes informações estejam carregadas via importação SAFX:

1. Inventário dos Produtos \(SAFX52\)

Os produtos sujeitos a ICMS\-ST devem apresentar o inventário referente ao último dia do mês anterior com Motivo do Inventário = 06 e Grupo de Contagem 1, 2, 3 ou 5\.

Para o primeiro período da geração do movimento pela opção IN\-RE087/20, se faz necessário carregar no Inventário \(SAFX52\), os Valores Unitários Médios de ICMS, ICMS\-ST, Base ICMS\-ST e FECEP\-ST \(campos 21, 22, 43, 44\), além da quantidade \(campo 13\)\.  Para os demais períodos, torna\-se necessário apenas carregar a quantidade\. Os Valores Unitários Médios não devem ser carregados, uma vez que a rotina considera os valores unitários calculados pela geração do movimento do período anterior\.

Por exemplo: Supondo que a primeira geração do movimento para atendimento a IN\-RE 087/20 é realizada para o período de janeiro de 2021\. Para essa geração, o Inventário dos Produtos \(SAFX52\) deve conter: Data do Inventário = 31/12/2020, Quantidade e Valores Unitários Médios de ICMS, ICMS\-ST, Base ICMS\-ST e FECEP\-ST preenchidos\.  

Para a geração do segundo mês \(fevereiro/2021\) o Inventário dos Produtos \(SAFX52\) deve conter: Data do Inventário = 31/01/2021, Quantidade preenchida e Valores Unitários Médios de ICMS, ICMS\-ST, Base ICMS\-ST e FECEP\-ST não preenchidos\.  Os meses subsequentes devem seguir como o segundo mês de geração: sem valores unitários médios\.

Obs\.: Para consultar o Inventario do Produto \(SAFX52\) acessar o módulo Básicos \[menu: Data Warehouse > Manutenção > Estoque > Inventário por Produto\]\.

Atenção:

Para todo período de geração, os produtos sujeitos a ICMS\-ST devem possuir Inventário \(SAFX52\) referente ao último dia do mês anterior, com Motivo do Inventário = 06 e Grupo de Contagem 1, 2, 3 ou 5\. 

Esse pré\-requisito atende a exigência do SPED FISCAL em apresentar registro H030 acompanhando os registros C180, C181, C185, C186\.

1. Documentos Fiscais de Operação de Entrada Normal \(SAFX07, SAFX08\):

Mapeamos aqui campos da SAFX08 necessários:

\- Produto \(campos 13 e 14 da SAFX08\)

\- CFOP \(campo 22 da SAFX08\)

\- Natureza de Operação \(campo 23 da SAFX08\) \- opcional\.

\- Quantidade \(campo 24 da SAFX08\)\.

\- Quantidade Convertida \(campo 137 da SAFX08\)\.

\- Indicador de ICMS\-ST \(campo 131 da SAFX08\)

\- Situação Especial – Substituição Tributária \(campo 132 da SAFX08\)

\- Medida \(campo 25 da SAFX08\)\.

\- Valor Contábil do Item \(campo 64 da SAFX08\)\.

\- Valor do ICMS: um dos campos abaixo relacionados ao ICMS são considerados:

\- Campo 43 \- Valor ICMS, se preenchido, ou

\- Campo 80 \- ICMS não Escriturado, se preenchido, ou

\- Campo 225 \- Valor ICMS Não Destacado\.

\- Base do ICMS\-ST: um dos campos abaixo relacionados a Base do ICMS\-ST são considerados:

\- Campo 61 \- Base ICMS Substituição Tributária, se preenchido, ou

\- Campo 144 \- Valor de Base ICMS– ST não escriturado, se preenchido, ou

\- Campo 106 \- Base Cálculo Carga Tributária Origem ICMS, se preenchido\.

\- Valor do ICMS\-ST: um dos campos abaixo relacionados ao ICMS\-ST são considerados:

\- Campo 52 \- Valor ICMS Substituição Tributária, se preenchido, ou 

\- Campo 145 \- Valor de ICMS\-ST não Escriturado, se preenchido, ou

\- Campo 133 \- ICMS\-ST Não Escriturado, se preenchido, ou

\- Campo 107 \- Valor Carga Tributária Origem, se preenchido\.

\- Valor do FECEP ICMS\-ST \(campo 140 da SAFX08\)\.

1. Documentos Fiscais de Operação de Saída Normal \(SAFX07, SAFX08\):

Mapeamos aqui campos da SAFX08 necessários:

\- Produto \(campos 13 e 14 da SAFX08\)

\- CFOP \(campo 22 da SAFX08\)

\- Natureza de Operação \(campo 23 da SAFX08\) \- opcional\.

\- Quantidade \(campo 24 da SAFX08\)\.

\- Quantidade Convertida \(campo 137 da SAFX08\)\.

\- Medida \(campo 25 da SAFX08\)\.

\- Valor Contábil do Item \(campo 64 da SAFX08\)\.

1. Documentos Fiscais de Operação de Devolução de Entrada \(SAFX07, SAFX08\):

A nota de devolução deve referenciar a nota de entrada que originou a devolução\.

Para atender esta condição, a nota de devolução de entrada conter a identificação a nota de entrada no próprio item da devolução, através dos seguintes campos da SAFX08:

117\-Número do Documento Fiscal de Referência

118\-Série do Documento Fiscal de Referência

119\-Subsérie do Documento Fiscal de Referência

102\-Data DI / Data Doc Refer

Além desses campos, o item da Nota de Devolução \(SAFX08\) deve conter:

\- Produto \(campos 13 e 14 da SAFX08\)

\- CFOP \(campo 22 da SAFX08\)

\- Natureza de Operação \(campo 23 da SAFX08\) \- opcional\.

\- Quantidade \(campo 24 da SAFX08\)\.

\- Quantidade Convertida \(campo 137 da SAFX08\)\.

\- Medida \(campo 25 da SAFX08\)\.

Quanto a nota de entrada referenciada pela devolução, esta pode estar no próprio período de geração ou em períodos anteriores\.  Ver mapeamento dos campos no tópico “Documentos Fiscais de Operação de Entrada Normal \(SAFX07, SAFX08\)” já mencionado\.

1. Documentos Fiscais de Operação de Devolução de Saída \(SAFX07, SAFX08, SAFX192\):

A nota de devolução deve referenciar a nota de saída que originou a devolução\.

Para atender estas condições, é indispensável informar a nota fiscal de referência da operação original, que pode ser de duas formas:

1. Informar a identificação da nota de saída da operação original no próprio item da devolução, através dos seguintes campos:

117\-Número do Documento Fiscal de Referência

118\-Série do Documento Fiscal de Referência

119\-Subsérie do Documento Fiscal de Referência

102\-Data DI / Data Doc Refer

1. Informar as notas de saídas objetos da devolução através da SAFX192 \(Tabela de Referências de Documentos Fiscais\), através dos campos:

\- Campos 1 ao 15 da SAFX192: identificam o item da nota de devolução;

\- Campo “16\-Tipo de Referência” da SAFX192 = “1” \- Devolução \(Entrada\) x Documentos de Origem \(Saídas\);

\- Campos 17 ao 23: identificam o item da nota de saída operação original da devolução;

O item da Nota de Devolução \(SAFX08\) deve conter:

\- Produto \(campos 13 e 14 da SAFX08\)

\- CFOP \(campo 22 da SAFX08\)

\- Natureza de Operação \(campo 23 da SAFX08\) \- opcional\.

\- Quantidade \(campo 24 da SAFX08\)\.

\- Quantidade Convertida \(campo 137 da SAFX08\)\.

\- Medida \(campo 25 da SAFX08\)\.

Quanto a nota de saída referenciada pela devolução, esta pode estar no próprio período de geração ou em períodos anteriores\.  Ver mapeamento dos campos no tópico “Documentos Fiscais de Operação de Saída Normal” já mencionado\.

__Obs\.:__ A manutenção da SAFX192 é feita na tela de manutenção dos itens de documento fiscal \(SAFX08\), opção “Documentos Referenciados”\.

Obs\.: Para maiores detalhes consultar o Manual Layout no módulo Básicos \[menu: Job Servidor > Carga > Manual de Layout SAFX > Selecionar tabela na aba Tabela SAFX > Consultar na aba Layout SAFX / ou baixar o Manual Layout na Base de Conhecimento do Contact Center\]\.

<a id="fecep"></a>Sobre Procedimento para Equalização DATA MART versus FECEP embutido no ICMS, ICMS\-ST:

Na escrituração dos documentos fiscais, os valores de FECEP podem ou não compor os valores de ICMS e ICMS\-ST\. Isso é uma determinação oriunda de cada Unidade Federativa\. Sendo assim, o sistema contempla os seguintes cenários para os itens de mercadoria \(SAFX08\):

\- Valores de FECEP embutidos nos valores de ICMS e ICMS\-ST \(campos 43 e 52 da SAFX08\);

\- Valores de FECEP separados dos valores de ICMS e ICMS\-ST \(campos 43 e 52 da SAFX08\);

Caso os valores de FECEP __não__ estejam embutidos nos valores de ICMS/ICMS\-ST \(campos 43 e 52 da SAFX08\) dos itens de mercadoria \(vide interface SAFX08\), proceder da seguinte forma:

- Na Equalização DATA MART, marcar a opção “Realizar a soma dos valores FECP ao ICMS/ICMS\-ST”\.
- Na Geração do Movimento da IN\-RE087/20, não marcar a opção “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)“\.

Caso os valores de FECEP já venham embutidos nos valores de ICMS e ICMS\-ST via interface SAFX08, proceder da seguinte forma:

- Na Equalização DATA MART, não marcar a opção “Realizar a soma dos valores FECP ao ICMS/ICMS\-ST”\.
- Na Geração do Movimento da IN\-RE087/20, marcar a opção “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)“\.

Para maiores esclarecimentos consulte o help do módulo Data Warehouse\.

__Sobre Geração do Movimento de Entrada \(C180\)__:

Para geração do C180 são consideradas as notas de entradas, normais, não canceladas, cujo código de modelo é 01, 1B, 04, 55 ou 65, cujo produto esteja parametrizado \(menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\) e cujo CFOP ou CFOP/Natureza da Operação esteja parametrizado para Operação de “Entrada \(e Devoluções\)” \(menu Parâmetros > IN\-RE 087/20 > Operações, opções CFOP ou Natureza de Operações;\)\.

A movimentação gerada pode ser conferida no Relatório de Conferência do C180\.

Segue explicações sobre a geração de alguns campos:

Responsável pela Retenção \(campo 02 COD\_RESP\_RET do C180\):

Para determinar o responsável pela retenção do ICMS\-ST, faz\-se necessário o preenchimento dos seguintes campos da SAFX08:

131 – Indicador de ICMS\-ST

132 – Situação Especial – Substituição Tributária

Quando o responsável pela retenção do ICMS\-ST for:

\- Remetente Direto: preencher o campo 131 com 1\.

\- Remetente Indireto: preencher o campo 131 com 2\.

\- Próprio adquirente: preencher o campo 132 com 1\.

Valores do ICMS\-ST \(campos 07 e 08 do C180\):

O valor e a base de cálculo do ICMS\-ST considerados nesta geração, são oriundos dos campos da SAFX08:

Quando o ICMS\-ST está destacado na nota, são considerados:

52 \- Valor ICMS Substituição Tributária e 61 \- Base ICMS Substituição Tributária

Quando o ICMS\-ST não está destacado/escriturado na nota, são considerados:

133 \- ICMS ST Não Escriturado e 144 \- Base ICMS\-ST não Escriturada, ou

145 \- Valor de ICMS – ST Não escriturado e 144 \- Base ICMS\-ST não Escriturada, ou

107 \- Valor Carga Tributária Origem ICMS e 106 \- Base Cálculo Carga Tributária Origem ICMS

Atenção:

Quanto ao Valor do ICMS\-ST destacado na nota, o campo 52 \- Valor ICMS Substituição Tributária pode ser carregado via SAFX08 com o FECEP\-ST embutido ou não\. 

Por isso, quando o FECEP __não__ estiver embutido no valor do ICMS\-ST, marcar a opção “Realizar a soma dos valores FECP ao ICMS/ICMS\-ST” na equalização DATA MART e __não__ marcar a opção “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” na Geração do Movimento\.  Caso contrário, o FECEP\-ST será considerado dobrado\.  Para maiores esclarecimentos veja o tópico [Sobre Procedimento para Equalização DATA MART versus FECEP embuitido no ICMS, ICMS\-ST](#fecep)\.

__Sobre Geração do Movimento de Saída \(C185 e C380\)__:

Para geração do C185 e C380, são consideradas as notas de saídas, normais, não canceladas,  cujo produto esteja parametrizado \(menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\) e cujo CFOP ou CFOP/Natureza da Operação esteja parametrizado para Operação de “Saída Interna para Consumidor Final \(e Devoluções\)” \(menu Parâmetros > IN\-RE 087/20 > Operações, opções CFOP ou Natureza de Operações;\)\. As notas com código de modelo 01, 1B, 04, 55 ou 65 geram o registro C185 e as de modelo 02, o registro C380\.

Nesta geração são utilizada as informações de %Redução BC, Alíquota Interna e Alíquota FCP parametrizadas para o produto \(menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\)\.

A movimentação gerada pode ser conferida através dos Relatório de Conferência do C185 e C380\.

Segue explicações sobre a geração de alguns campos:

Valores Unitários de ICMS, ICMS\-ST e FCP\-ST Estoque \(campos 12, 13 e 14 do C185, campos 08, 09, 10 do C380\):

Esses valores são oriundos do Cálculo da Média Ponderada Móvel, considerando a data da emissão e o produto da nota de saída\. Consulte o Relatório de Conferência do Cálculo da Média Ponderada\.

- Valor Unitário de ICMS Estoque = Valor Médio Unitário ICMS
- Valor Unitário de ICMS\-ST Estoque = Valor Médio Unitário ICMS\-ST \+ Valor Médio Unitário FECEP\-ST
- Valor Unitário de FCP\-ST Estoque Valor Médio Unitário FECEP\-ST

 Valor Unitário do ICMS na Operação \(C185\-10 \- C380\-06\):

Valor calculado a partir da Base de Cálculo aplicando a alíquota interna parametrizada para o produto \(vide menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\)\. 

Considera\-se como Base de Cálculo, o valor da operação \(valor contábil do item\) quando não existir percentual de redução na parametrização do produto\. Já se existir percentual de redução, a base é calculada a partir do percentual de redução informado, aplicando esta redução sobre o valor da operação \(valor contábil do item\)\.

<a id="sobre_c186"></a>__Sobre Geração do Movimento de Devolução de Entrada \(C186\):__

Para geração do C186, são consideradas as notas de devolução de entradas, não canceladas, cujo código de modelo é 01, 1B, 04, 55 ou 65, cujo produto esteja parametrizado \(menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\) e cujo CFOP ou CFOP/Natureza da Operação esteja parametrizado para Operação de “Entrada \(e Devoluções\)” \(menu Parâmetros > IN\-RE 087/20 > Operações, opções CFOP ou Natureza de Operações;\)\.

A nota de devolução deve conter referência para a nota de entrada \(através dos campos da SAFX08 117\-Número do Documento Fiscal de Referência, 118\-Série do Documento Fiscal de Referência, 119\-Subsérie do Documento Fiscal de Referência, 102\-Data DI / Data Doc Refer\)\. Não são consideradas as notas de devolução sem referência para nota de entrada\.

Segundo o tópico 19\.3\-A\.1\.4\.1 da IN\-RE 045/98, para as entradas objeto de devolução ocorridas antes de 1º de janeiro de 2021, os valores unitários de ICMS, ICMS\-ST, Base ICMS\-ST devem ser oriundos do inventário do Produto de 31/12/2020 \(ou dia anterior ao primeiro mês que adotar a nova sistemática da IN\-087/20\)\.

Como solução aplicada às notas de entradas anteriores a 01/01/2021 \(ou data inicial da adoção da nova sistemática da IN\-087/20\), damos a possibilidade de escolha entre usar valores unitários do inventário \(conforme Tópico 19\.3\-A\.1\.4\.1\), ou calcular os valores unitários a partir dos valores de ICMS, BC ICMS\-ST e ICMS\-ST presentes na nota de entrada objeto da devolução\. Essa escolha é feita através das opções na tela da geração:

“Tratamento p/ Entrada objeto da Devolução de períodos anteríores à adoção da sistemática da IN\-RE 087/20:

Valores Unitários Médios recuperados:

\( \) do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)

\( \) da própria Nota de Entrada referenciada pela Devolução”

Dt anterior à adoção IN\-RE087/20: \[31/12/2020\]

O campo Dt anterior à adoção IN\-RE087/20, por padrão é preenchido com 31/12/2020, pois a nova sistemática da IN\-RE 087/20 inicia\-se em janeiro/2021\. Mas se o primeiro período da geração do movimento pela IN\-RE087/20 não for janeiro/2021, esta data deve ser alterada para o dia imediatamente anterior ao primeiro mês da geração\. Exemplo: se a adoção da sistemática da IN\-RE 087/20 foi abril/2021, o campo “Dt anterior à adoção IN\-RE087/20” deve ser preenchido com 31/03/2021, para todos os meses em que for realizada a geração \(abril/2021, maio/2021, junho/2021\.\.\.\)\.

Escolhida a opção do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\), deve existir Inventário \(SAFX52\) para os produtos sujeitos a ICMS\-ST, com Data Inventário =” Dt anterior à adoção IN\-RE087/20”, com Motivo do Inventário = 06 e Grupo Contagem 1, 2, 3 ou 5\.

A movimentação gerada pode ser conferida através do Relatório de Conferência do C186\.

__Sobre Geração do Movimento de Devolução de Saída \(C181\):__

Para geração do C181, são consideradas as notas de devolução de saídas, não canceladas, cujo código de modelo é 01, 1B, 04, 55 ou 65, cujo produto esteja parametrizado \(menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\) e cujo CFOP ou CFOP/Natureza da Operação esteja parametrizado para Operação de “Saída Interna para Consumidor Final \(e Devoluções\)” \(menu Parâmetros > IN\-RE 087/20 > Operações, opções CFOP ou Natureza de Operações;\)\.

A nota de devolução deve conter referência para a nota de saída \(através dos campos da SAFX08 117\-Número do Documento Fiscal de Referência, 118\-Série do Documento Fiscal de Referência, 119\-Subsérie do Documento Fiscal de Referência, 102\-Data DI / Data Doc Refer ou através da SAFX192\)\. Não são consideradas as notas de devolução sem referência para nota de saída\.

Segundo o tópico 19\.3\-A\.1\.5\.1 da IN\-RE 045/98, para as notas de saída objeto de devolução ocorridas antes de 1º de janeiro de 2021 \(ou data inicial da adoção da nova sistemática da IN\-087/20\), os valores unitários de ICMS, ICMS\-ST devem ser oriundos do documento fiscal do último recebimento da mercadoria pelo estabelecimento antes da saída objeto da devolução\.

Adotamos essa regra verificando se na data da emissão da nota de saída objeto da devolução, já existe Média Ponderada calculada para o produto movimentado\. Caso exista, os valores unitários são gerados considerando o Cálculo da Média Ponderada\. Caso contrário, buscamos a última nota de entrada do produto anterior à emissão da saída\.

A movimentação gerada pode ser conferida através do Relatório de Conferência do C181\.

__Sobre o Cálculo da Média Ponderada Móvel__

Base na IN\-RE 087/20 tópico 19\.3\-A\.2\.2, o cálculo é realizado para todos os produtos sujeitos ao ICMS\-ST vigentes no período da geração\.

O cálculo é feito com quatro valores conforme estabelece o tópico 19\.3\-A\.2\.2:

\(alínea “a”\) no saldo inicial do primeiro dia do período, que corresponde ao saldo final do dia anterior;

\(alínea “b”\): movimento de devolução de saídas do período;

\(alínea “c”\): movimento de entradas do período;

\(alínea “d”\): movimento de devolução de entradas do período;

Por dia e produto, os valores unitários do ICMS, ICMS\-ST e FECEP\-ST são calculados da seguinte forma:

\[Saldo Inicial do Dia \+ Devolução de Saídas do Dia \+ Entradas do Dia – Devolução de Entradas\] dividido pela \[Quantidade Inicial \+ Quantidade de Devolução de Saídas \+ Quantidade de Entradas – Quantidade de Devolução de Entradas\]\.

O cálculo pode ser conferido através do Relatório de Conferência do Cálculo da Média Ponderada\.

__Sobre os Relatórios de Conferência__:

Ao final da execução da geração os seguintes relatórios são disponibilizados:

1. Relatório de Log de Erros: composto por mensagens que apontam para falta de informações em documentos, parametrizações e cadastros\. Com base nesse relatório é possível realizar as correções na base para obter uma finalização do processo com sucesso\.
2. Relatórios de Conferência: os movimentos gerados são gravados em arquivo formato cvs\. 

É gerado um arquivo para tipo de movimento:

- Entradas – Relatorio\_Conferência\_C180, 
- Saídas – Relatorio\_Conferência\_C185
- Saídas de Modelo de Documento 02 – Relatório Conferência\_C380
- Devolução de Entradas – Relatorio\_Conferência\_C186
- Devolução de Saídas – Relatorio\_Conferência\_C181

Ainda é disponibilizado um relatório para conferência para os valores médios diários calculados para os produtos: “Relatório\_Conferência\_Cálculo\_Média\_Ponderada”\.

Com objetivo de facilitar a conferência das informações que serão apresentadas nos registros C180, C181, C185 e C186, além dos campos pertencentes ao layout do SPED FISCAL, foram adicionados campos auxiliarem que demonstram informações oriundas de cadastro, das notas fiscais, parametrizações, que foram utilizadas na geração dos registros\.  

Através do título do campo é possível identificar se este faz parte do layout do SPED FISCAL ou se é um campo auxiliar\. Título contém o número de referência do campo no layout do SPED FISCAL, ou se for auxiliar, a origem da informação internamente no sistema\. Por exemplo: “Medida \(C180\-04\)”, “Qtde Conv \(C180\-03\)” e  “Vlr Unit Conv \(C180\-05\)” são campos pertencentes ao layout do C180\.  “Medida Produto \(SAFX2013\-14\)”, “Medida Item \(SAFX08\-25\)”, Qtde Item \(SAFX08\-24\) e Vlr Contabil Item \(SAFX08\-64\) são campos auxiliares\.

__Relatório de Conferência do C180:__

- Campos de Identificação da Nota Fiscal:

\- Do 1º ao 11º campo: \(Cod Empresa, Cod Estab, Dt Fiscal, E/S, Norm/Dev, Cod Docto, Ind Fis/Jur Cod Fis/Jur, Num Docfis	, Serie, SubSerie, Num Item\);

- Campos do Layout do C180:

\- Qtde Conv \(C180\-03\): Quantidade \(campo 24 da SAFX08\) do item documento fiscal, quando a unidade de medida do item é igual a do Cadastro do Produto \(SAFX2013 – campo 14\)\.

                                            Caso a medida do item do documento fiscal seja diferente da medida no cadastro do produto, esse campo demonstra o resultado da multiplicação do campo Quantidade \(campo 24 da SAFX08\) pelo

                                            Fator de Conversão \(veja tópico [Cadastro de Conversão de Unidades de Medidas](#Conv_Medidas)\), ou apresenta a quantidade já convertida carregada no campo 137 da SAFX08\.

\- Medida \(C180\-04\): Unidade de Medida do Cadastro do Produto \(SAFX2013 – campo 14\)\.

\- Vlr Unit Conv \(C180\-05\): Valor unitário da mercadoria calculado considerando: \[Valor Contábil do Item \(campo 64 da SAFX08\) subtraído o Valor do ICMS\-ST\(campo 52, ou 145 ou 133 ou 107 da SAFX08\)\] dividido pela Quantidade Convertida;

\- Vlr Unit ICMS Conv \(C180\-06\): Valor unitário do ICMS calculado considerando: \[Valor do ICMS \(campo 43, ou 80 ou 225 da SAFX08\)\] dividido pela Quantidade Convertida;

\- Cod Resp \(C180\-02\): \- 1\-Remetente Direto \(quando Campo 131 da SAFX08 for igual a 1\)\. 2\- Remetente Indireto \(Campo 131 igual a 2\)\. 3\- Próprio adquirente \(quando Campo 132 da SAFX08 for igual a 1\)\.

\- Vlr Unit BC ICMS\-ST Conv \(C180\-07\): Valor unitário da Base do ICMS\-ST calculado considerando: \[Valor BC ICMS\-ST \(campo 61, ou 144 ou 106 da SAFX08\)\] dividido pela Quantidade Convertida;

\- Vlr Unit ICMS\-ST Conv \(C180\-08\): Valor unitário do ICMS\-ST calculado considerando: \[Valor do ICMS\-ST \(campo 52, ou 145 ou 133 ou 107 da SAFX08\) somado FECEP\-ST \(campo 140 da SAFX08\)\] dividido pela Quantidade Convertida;

Atenção:

Quanto ao Valor do ICMS\-ST destacado na nota, o campo 52 \- Valor ICMS Substituição Tributária pode ser carregado via SAFX08 com o FECEP\-ST embutido ou não\. 

Por isso, quando o FECEP __não__ estiver embutido no valor do ICMS\-ST, marcar a opção “Realizar a soma dos valores FECP ao ICMS/ICMS\-ST” na equalização DATA MART e __não__ marcar a opção “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” na Geração do Movimento\.  Caso contrário, o FECEP\-ST será considerado dobrado\.  Para maiores esclarecimentos veja o tópico [Sobre Procedimento para Equalização DATA MART versus FECEP embuitido no ICMS, ICMS\-ST](#fecep)\.

\- Vlr Unit FCP\-ST Conv \(C180\-09\): Valor unitário do FECEP\-ST calculado considerando: \[FECEP\-ST \(campo 140 da SAFX08\)\] dividido pela Quantidade Convertida;

- Campos Auxiliares origem Cadastro do Produto \(SAFX2013\):

\- Ind Produto \(SAFX2013\-01\) Cod Produto \(SAFX2013\-02\),

 \- Medida Produto \(SAFX2013\-14\), 

\- NCM Produto \(SAFX2013\-05\), 

\- CEST Produto \(SAFX2013\-54\)

Para consultar o cadastro do produto \(SAFX2013\) acessar o módulo Básicos \[menu: Data Warehouse > Manutenção > Códigos > Produto\]\.

- Campos Auxiliares origem Documento Fiscal \(SAFX08\):

\- Qtde Item \(SAFX08\-24\)

\- Qtde Conv Item \(SAFX08\-137\)

\- Medida Item \(SAFX08\-25\)

\- Fator Conv \(Cadastro Conversão Medida\): Fator de Conversão cadastrado no módulo Básicos \[menu: Data Warehouse > Manutenção > Cadastros > Conversão de Unidades de Medida, opções Padrão ou Por Produto\];

\- Vlr Contabil Item \(SAFX08\-64\)	

\- Vlr ICMS Item \(SAFX08\-43,80,225\):  Considerado o Campo “43\-Valor ICMS”, se preenchido, ou Campo “80\-ICMS não Escriturado”, se preenchido, ou Campo “225\-Valor ICMS Não Destacado”  

\- Vlr BC ICMS\-ST Item \(SAFX08\-61,144,106\): Considerado o Campo “61\- Base ICMS Substituição Tributária”, se preenchido, ou Campo “144\- Base ICMS\-ST não Escriturada”, se preenchido, ou Campo “106\- Base Cálculo Carga Tributária Origem ICMS”  

\- Vlr ICMS\-ST Item \(SAFX08\-52,145,133,107\): Considerado o Campo “52\- Valor ICMS Substituição Tributária”, se preenchido, ou  Campo “133\- ICMS ST Não Escriturado”, se preenchido, ou Campo “145\-Valor de ICMS – ST Não escriturado”, se preenchido, ou Campo “107\- Valor Carga Tributária Origem ICMS”  	

\- Vlr FECEP\-ST Item \(SAFX08\-144\)	

- Campos Auxiliares para o Cálculo da Média Ponderada:

<a id="_Hlk64475918"></a>\- Vlr Unit ICMS \(Cálculo da Média Ponderada\): igual ao Vlr Unit ICMS Conv \(C180\-06\);

\- Vlr Unit ICMS\-ST\(s/ FCP\-ST\) \(Cálculo da Média Ponderada\): Valor unitário do ICMS\-ST \(sem o FECEP\-ST\) calculado considerando: \[Valor do ICMS\-ST \(campo 52, ou 145 ou 133 ou 107 da SAFX08\) subtraído o FECEP\-ST \(campo 140 da SAFX08\)\] dividido pela Quantidade Convertida;

Atenção:

Quanto ao Valor do ICMS\-ST destacado na nota, o campo 52 \- Valor ICMS Substituição Tributária pode ser carregado via SAFX08 com o FECEP\-ST embutido ou não\. 

Por isso, quando o FECEP __não__ estiver embutido no valor do ICMS\-ST, marcar a opção “Realizar a soma dos valores FECP ao ICMS/ICMS\-ST” na equalização DATA MART e __não__ marcar a opção “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” na Geração do Movimento\.  Para maiores esclarecimentos veja o tópico [Sobre Procedimento para Equalização DATA MART versus FECEP embuitido no ICMS, ICMS\-ST](#fecep)\.

\- Vlr Unit BC ICMS\-ST \(Cálculo da Média Ponderada\): igual ao Vlr Unit BC ICMS\-ST Conv \(C180\-07\);

\- Vlr Unit FCP\-ST \(Cálculo da Média Ponderada\): igual ao Vlr Unit FCP\-ST Conv \(C180\-09\);

\- Vlr ICMS \(Cálculo da Média Ponderada\): Valor calculado considerando: \[Qtde Conv \(C180\-03\) x Vlr Unit ICMS \(Cálculo da Média Ponderada\)\]\.  O total desse valor por dia e produto é apresentado no campo “Valor ICMS \(Entrada\)” do Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr ICMS\-ST \(s/ FCP\-ST\) \(Cálculo da Média Ponderada\):  Valor calculado considerando: \[Qtde Conv \(C180\-03\) x Vlr Unit ICMS\-ST \(s/ FCP\-ST\) \(Cálculo da Média Ponderada\)\]\. O total desse valor por dia e produto é apresentado no campo “Valor ICMS\-ST \(Entrada\)” do Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr BC ICMS\-ST \(Cálculo da Média Ponderada\): Valor calculado considerando: \[Qtde Conv \(C180\-03\) x Vlr Unit BC ICMS\-ST \(Cálculo da Média Ponderada\)\]\. O total desse valor por dia e produto é apresentado no campo “Valor Base de Cálculo do ICMS\-ST \(Entrada\)” do Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr FCP\-ST \(Cálculo da Média Ponderada\): Valor calculado considerando: \[Qtde Conv \(C180\-03\) x Vlr Unit FCP\-ST \(Cálculo da Média Ponderada\)\]\.  O total desse valor por dia e produto é apresentado no campo “Valor FECEP\-ST \(Entrada\)” do Relatório de Conferência do Cálculo da Média Ponderada\.

__Relatório de Conferência do C185:__

- Campos de Identificação da Nota Fiscal:

\- Do 1º ao 11º campo: \(Cod Empresa, Cod Estab, Dt Fiscal, E/S, Norm/Dev, Cod Docto, Ind Fis/Jur Cod Fis/Jur, Num Docfis	, Serie, SubSerie, Num Item\);

- Campos do Layout do C185:

\- Qtde Conv \(C185\-07\): Quantidade \(campo 24 da SAFX08\) do item documento fiscal, quando a unidade de medida do item é igual a do Cadastro do Produto \(SAFX2013 – campo 14\)\.

                                            Caso a medida do item do documento fiscal seja diferente da medida no cadastro do produto, esse campo demonstra o resultado da multiplicação do campo Quantidade \(campo 24 da SAFX08\) pelo

                                            Fator de Conversão \(veja tópico [Cadastro de Conversão de Unidades de Medidas](#Conv_Medidas)\), ou apresenta a Quantidade já Convertida carregada no campo 137 da SAFX08\.

\- Medida \(C185\-08\): Unidade de Medida do Cadastro do Produto \(SAFX2013 – campo 14\)\.

\- Vlr Unit Conv \(C185\-09\): Valor unitário da mercadoria calculado considerando: \[Valor Contábil do Item \(campo 64 da SAFX08\)\] dividido pela Quantidade Convertida;

\- Vlr Unit ICMS Operação Conv \(C185\-10\): Valor unitário do ICMS calculado considerando: \[Vlr Unit BC ICMS Operação Conv\] multiplicado pela Alíquota Interna dividido por 100;

  Onde:  	Vlr Unit BC ICMS Operação Conv é calculado considerando o %Redução BC parametrizado para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\):

                 Para produto sem %Redução BC: Vlr Unit BC ICMS Operação Conv = \[Valor Contábil do Item \(campo 64 da SAFX08\)\] dividido pela Quantidade Convertida;  

                 Para produto com %Redução BC: Vlr Unit BC ICMS Operação Conv = \[\(Valor Contábil do Item – \(Valor Contábil do Item \* “%Redução BC” / 100\)\)\] dividido pela Quantidade Convertida;

                  O Vlr Unit BC ICMS Operação Conv é demonstrado nesse relatório no campo “Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\)”\.

Alíquota Interna: Aíquota parametrizada para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\)\.

\- Cod Motivo \(C185\-06\): Para saídas internas a consumidor final com ressarcimento, esse campo é preenchido com “RS100”\. Quando houver complementação, esse campo é preenchido com “RS300”\.

 Para saber se houve ressarcimento ou complemento, é realizada a comparação entre os valores unitários da Entrada e da Saída, através dos campos:  

- Valor Médio Unitário Base de Cálculo do ICMS\-ST: Valor unitário da entrada, obtido pelo Cálculo da Média Ponderada Móvel\.  Ver campo “Valor Médio Unitário Base de Cálculo do ICMS\-ST” do Relatório de Conferência do Cálculo da Média Ponderada\. Esse valor é demonstrado nesse relatório no campo “Vlr Unit BC ICMS\-ST \(Recuperado da Média Ponderada\)”\.
- Vlr Unit BC ICMS Operação Conv: Valor unitário da saída, que é demonstrado nesse relatório no campo “Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\)”\.

\- Vlr Unit ICMS Op Conv \(C185\-11\): Para saídas internas a consumidor final, esse campo não é preenchido;

\- Vlr Unit ICMS Estoque Conv \(C185\-12\):  Valor Médio Unitário ICMS obtido do Cálculo da Média Ponderada Móvel, para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit ICMS\-ST Estoque Conv \(C185\-13\):  Valor Médio Unitário ICMS\-ST \+ Valor Médio Unitário FECEP\-ST obtidos do Cálculo da Média Ponderada Móvel, para o dia e produto da saída\. Esses campos são demonstrados no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit FCP\-ST Estoque Conv \(C185\-14\): Valor Médio Unitário FECEP\-ST obtido do Cálculo da Média Ponderada Móvel, para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit ICMS\-ST Conv Rest \(C185\-15\): valor do ressarcimento calculado com base nos campos Vlr Unit ICMS Operação Conv \(C185\-10\), Vlr Unit ICMS Op Conv \(C185\-11\), Vlr Unit ICMS Estoque Conv \(C185\-12\), Vlr Unit ICMS\-ST Estoque Conv \(C185\-13\);

\- Vlr Unit FCP\-ST Conv Rest \(C185\-16\): valor do ressarcimento calculado com base no campo Vlr Unit ICMS\-ST Conv Rest \(C185\-15\) aplicando a Aliquota FECEP parametrizada para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\);

\- Vlr Unit ICMS\-ST Conv Compl \(C185\-17\): valor do complemento calculado com base nos campos Vlr Unit ICMS Operação Conv \(C185\-10\), Vlr Unit ICMS Op Conv \(C185\-11\), Vlr Unit ICMS Estoque Conv \(C185\-12\), Vlr Unit ICMS\-ST Estoque Conv \(C185\-13\);

\- Vlr Unit FCP\-ST Conv Compl \(C185\-18\): valor do complemento calculado com base no campo Vlr Unit ICMS\-ST Conv Compl \(C185\-17\) aplicando a Aliquota FECEP parametrizada para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\);

- Campos Auxiliares origem Cadastro do Produto \(SAFX2013\):

\- Ind Produto \(SAFX2013\-01\) Cod Produto \(SAFX2013\-02\),

 \- Medida Produto \(SAFX2013\-14\), 

\- NCM Produto \(SAFX2013\-05\), 

\- CEST Produto \(SAFX2013\-54\)

Para consultar o cadastro do produto \(SAFX2013\) acessar o módulo Básicos \[menu: Data Warehouse > Manutenção > Códigos > Produto\]\.

- Campos Auxiliares origem Parametrização do Produto:

\- %Redução BC \(Parametrização Produto\)	

\- Alíq\. Interna \(Parametrização Produto\)	

\- Alíq\. FCP \(Parametrização Produto\)

Para consulta acesse o menu Parâmetros > Produto, opções por Código, por NCM ou por CEST;

- Campos Auxiliares origem Documento Fiscal \(SAFX08\):

\- Qtde Item \(SAFX08\-24\)

\- Qtde Conv Item \(SAFX08\-137\)

\- Medida Item \(SAFX08\-25\)

\- Fator Conv \(Cadastro Conversão Medida\): Fator de Conversão cadastrado no módulo Básicos \[menu: Data Warehouse > Manutenção > Cadastros > Conversão de Unidades de Medida, opções Padrão ou Por Produto\];

\- Vlr Contabil Item \(SAFX08\-64\)	

\- Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\):  calculado considerando o %Redução BC parametrizado para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\):

                 Para produto sem %Redução BC: Vlr Unit BC ICMS Operação Conv = \[Valor Contábil do Item \(campo 64 da SAFX08\)\] dividido pela Quantidade Convertida;  

                 Para produto com %Redução BC: Vlr Unit BC ICMS Operação Conv = \[\(Valor Contábil do Item – \(Valor Contábil do Item \* “%Redução BC” / 100\)\)\] dividido pela Quantidade Convertida

- Campos Auxiliares Recuperados da Média Ponderada:

\- Vlr Unit ICMS \(Recuperado da Média Ponderada\): Valor Médio Unitário ICMS obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit ICMS\-ST\(s/ FECEP\-ST\) \(Recuperado da Média Ponderada\): Valor Médio Unitário ICMS\-ST obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit BC ICMS\-ST \(Recuperado da Média Ponderada\): Valor Médio Unitário Base de Cálculo do ICMS\-ST obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;	

\- Vlr Unit FECEP\-ST \(Recuperado da Média Ponderada\): Valor Médio Unitário FECEP\-ST obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

__Relatório de Conferência do C380:__

- Campos de Identificação da Nota Fiscal:

\- Do 1º ao 11º campo: \(Cod Empresa, Cod Estab, Dt Fiscal, E/S, Norm/Dev, Cod Docto, Ind Fis/Jur Cod Fis/Jur, Num Docfis	, Serie, SubSerie, Num Item\);

- Campos do Layout do C380:

\- Qtde Conv \(C380\-03\): Quantidade \(campo 24 da SAFX08\) do item documento fiscal, quando a unidade de medida do item é igual a do Cadastro do Produto \(SAFX2013 – campo 14\)\.

                                            Caso a medida do item do documento fiscal seja diferente da medida no cadastro do produto, esse campo demonstra o resultado da multiplicação do campo Quantidade \(campo 24 da SAFX08\) pelo

                                            Fator de Conversão \(veja tópico [Cadastro de Conversão de Unidades de Medidas](#Conv_Medidas)\), ou apresenta a quantidade já convertida carregada no campo 137 da SAFX08\.

\- Medida \(C380\-04\): Unidade de Medida do Cadastro do Produto \(SAFX2013 – campo 14\)\.

\- Vlr Unit Conv \(C380\-05\): Valor unitário da mercadoria calculado considerando: \[Valor Contábil do Item \(campo 64 da SAFX08\)\] dividido pela Quantidade Convertida;

\- Vlr Unit ICMS Operação Conv \(C380\-06\): Valor unitário do ICMS calculado considerando: \[Vlr Unit BC ICMS Operação Conv\] multiplicado pela Alíquota Interna dividido por 100;

  Onde:  	Vlr Unit BC ICMS Operação Conv é calculado considerando o %Redução BC parametrizado para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\):

                 Para produto sem %Redução BC: Vlr Unit BC ICMS Operação Conv = \[Valor Contábil do Item \(campo 64 da SAFX08\)\] dividido pela Quantidade Convertida;  

                 Para produto com %Redução BC: Vlr Unit BC ICMS Operação Conv = \[\(Valor Contábil do Item – \(Valor Contábil do Item \* “%Redução BC” / 100\)\)\] dividido pela Quantidade Convertida;

                  O Vlr Unit BC ICMS Operação Conv é demonstrado nesse relatório no campo “Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\)”\.

                 Alíquota Interna: Aíquota parametrizada para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\)\.

\- Cod Motivo \(C380\-02\): Para saídas internas a consumidor final com ressarcimento, esse campo é preenchido com “RS100”\. Quando houver complementação, esse campo é preenchido com “RS300”\.

 Para saber se houve ressarcimento ou complemento, é realizada a comparação entre os valores unitários da Entrada e da Saída, através dos campos:  

- Valor Médio Unitário Base de Cálculo do ICMS\-ST: Valor unitário da entrada, obtido pelo Cálculo da Média Ponderada Móvel\.  Ver campo “Valor Médio Unitário Base de Cálculo do ICMS\-ST” do Relatório de Conferência do Cálculo da Média Ponderada\. Esse valor é demonstrado nesse relatório no campo “Vlr Unit BC ICMS\-ST \(Recuperado da Média Ponderada\)”
- Vlr Unit BC ICMS Operação Conv: Valor unitário da saída, que é demonstrado nesse relatório no campo “Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\)”\.

\- Vlr Unit ICMS Op Conv \(C380\-07\): Para saídas internas a consumidor final, esse campo não é preenchido;

\- Vlr Unit ICMS Estoque Conv \(C380\-08\):  Valor Médio Unitário ICMS obtido do Cálculo da Média Ponderada Móvel, para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit ICMS\-ST Estoque Conv \(C380\-09\):  Valor Médio Unitário ICMS\-ST \+ Valor Médio Unitário FECEP\-ST obtidos do Cálculo da Média Ponderada Móvel, para o dia e produto da saída\. Esses campos são demonstrados no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit FCP\-ST Estoque Conv \(C380\-10\): Valor Médio Unitário FECEP\-ST obtido do Cálculo da Média Ponderada Móvel, para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit ICMS\-ST Conv Rest \(C380\-11\): valor do ressarcimento calculado com base nos campos Vlr Unit ICMS Operação Conv \(C380\-06\), Vlr Unit ICMS Op Conv \(C380\-07\), Vlr Unit ICMS Estoque Conv \(C380\-08\), Vlr Unit ICMS\-ST Estoque Conv \(C380\-09\);

\- Vlr Unit FCP\-ST Conv Rest \(C380\-12\): valor do ressarcimento calculado com base no campo Vlr Unit ICMS\-ST Conv Rest \(C380\-11\) aplicando a Aliquota FECEP parametrizada para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\);

\- Vlr Unit ICMS\-ST Conv Compl \(C380\-13\): valor do complemento calculado com base nos campos Vlr Unit ICMS Operação Conv \(C380\-06\), Vlr Unit ICMS Op Conv \(C380\-07\), Vlr Unit ICMS Estoque Conv \(C380\-08\), Vlr Unit ICMS\-ST Estoque Conv \(C380\-09\);

\- Vlr Unit FCP\-ST Conv Compl \(C380\-14\): valor do complemento calculado com base no campo Vlr Unit ICMS\-ST Conv Compl \(C380\-13\) aplicando a Aliquota FECEP parametrizada para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\);

- Campos Auxiliares origem Cadastro do Produto \(SAFX2013\):

\- Ind Produto \(SAFX2013\-01\) Cod Produto \(SAFX2013\-02\),

 \- Medida Produto \(SAFX2013\-14\), 

\- NCM Produto \(SAFX2013\-05\), 

\- CEST Produto \(SAFX2013\-54\)

Para consultar o cadastro do produto \(SAFX2013\) acessar o módulo Básicos \[menu: Data Warehouse > Manutenção > Códigos > Produto\]\.

- Campos Auxiliares origem Parametrização do Produto:

\- %Redução BC \(Parametrização Produto\)	

\- Alíq\. Interna \(Parametrização Produto\)	

\- Alíq\. FCP \(Parametrização Produto\)

Para consulta acesse o menu Parâmetros > Produto, opções por Código, por NCM ou por CEST;

- Campos Auxiliares origem Documento Fiscal \(SAFX08\):

\- Qtde Item \(SAFX08\-24\)

\- Qtde Conv Item \(SAFX08\-137\)

\- Medida Item \(SAFX08\-25\)

\- Fator Conv \(Cadastro Conversão Medida\): Fator de Conversão cadastrado no módulo Básicos \[menu: Data Warehouse > Manutenção > Cadastros > Conversão de Unidades de Medida, opções Padrão ou Por Produto\];

\- Vlr Contabil Item \(SAFX08\-64\)	

\- Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\):  calculado considerando o %Redução BC parametrizado para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\):

                 Para produto sem %Redução BC: Vlr Unit BC ICMS Operação Conv =   \[Valor Contábil do Item \(campo 64 da SAFX08\)\] dividido pela Quantidade Convertida;  

                 Para produto com %Redução BC: Vlr Unit BC ICMS Operação Conv =   \[\(Valor Contábil do Item – \(Valor Contábil do Item \* “%Redução BC” / 100\)\)\] dividido pela Quantidade Convertida

- Campos Auxiliares Recuperados da Média Ponderada:

\- Vlr Unit ICMS \(Recuperado da Média Ponderada\): Valor Médio Unitário ICMS obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit ICMS\-ST\(s/ FECEP\-ST\) \(Recuperado da Média Ponderada\): Valor Médio Unitário ICMS\-ST obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit BC ICMS\-ST \(Recuperado da Média Ponderada\): Valor Médio Unitário Base de Cálculo do ICMS\-ST obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;	

\- Vlr Unit FECEP\-ST \(Recuperado da Média Ponderada\): Valor Médio Unitário  FECEP\-ST obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

__Relatório de Conferência do C181:__

- Campos de Identificação da Nota Fiscal de Devolução:

\- Do 1º ao 11º campo: identificação da nota fiscal de devolução com o número do item de mercadoria \(Cod Empresa, Cod Estab, Dt Fiscal NF Devolução, E/S NF Devolução, Norm/Dev NF Devolução, Cod Docto NF Devolução, Ind Fis/Jur NF Devolução Cod Fis/Jur NF Devolução, Num Docfis NF Devolução, Serie NF Devolução, SubSerie NF Devolução, Num Item NF Devolução\);

- Campos do Layout do C181:

\- Num Docfis NF Saída \(C181\-08\), Serie NF Saída \(C181\-06\), Dt Fiscal NF Saída \(C181\-10\), Num Item NF Saída \(C181\-11\): campos de identificação da nota de Saída;

\- Cod Motivo \(C181\-02\): Para saídas objeto de devolução com ressarcimento \(“RS100”\), esse campo é preenchido com “RS600” – Estorno do Ressarcimento\-ST\.

                                             Para saídas objeto de devolução com complemento \(“RS300”\), esse campo é preenchido com “RS600” – Estorno do Complemento\-ST\.

 Para saber se houve ressarcimento ou complemento, é realizada a comparação entre os valores unitários da Entrada e da Saída, através dos campos:  

- Valor Médio Unitário Base de Cálculo do ICMS\-ST : Valor unitário da entrada, obtido pelo Cálculo da Média Ponderada Móvel, para o dia e produto da saída objeto da devolução\.  Ver campo “Valor Médio Unitário Base de Cálculo do ICMS\-ST” do Relatório de Conferência do Cálculo da Média Ponderada\.  Para saídas de períodos anteriores à nova sistemática da IN087/20, o valor é calculado a partir da última nota de recebimento do produto anterior a data da saída;

Esse valor é demonstrado nesse relatório no campo “Vlr Unit BC ICMS\-ST \(p/ Cálculo da Média Ponderada\)”

- Vlr Unit BC ICMS Operação Conv: Valor unitário da saída, calculado considerando o %Redução BC parametrizado para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\):

Para produto sem %Redução BC: Vlr Unit BC ICMS Operação Conv = \[Valor Contábil do Item da Saída \(campo 64 da SAFX08\)\] dividido pela Quantidade Convertida da Saída;

Para produto com %Redução BC: Vlr Unit BC ICMS Operação Conv = \[\(Valor Contábil do Item da Saída  – \(Valor Contábil do Item da Saída \* “%Redução BC” / 100\)\)\] dividido pela Quantidade Convertida da Saída;

O Vlr Unit BC ICMS Operação Conv é demonstrado nesse relatório no campo “Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\)”\.

\- Qtde Conv \(C181\-03\): Quantidade \(campo 24 da SAFX08\) do item documento fiscal de devolução, quando a unidade de medida do item é igual a do Cadastro do Produto \(SAFX2013 – campo 14\)\.

                                            Caso a medida do item do documento fiscal de devolução seja diferente da medida no cadastro do produto, esse campo demonstra o resultado da multiplicação do campo Quantidade \(campo 24 da 

                                            SAFX08\) pelo Fator de Conversão \(veja tópico [Cadastro de Conversão de Unidades de Medidas](#Conv_Medidas)\), ou apresenta a Quantidade já Convertida carregada no campo 137 da SAFX08\.

\- Medida \(C181\-04\): Unidade de Medida do Cadastro do Produto \(SAFX2013 – campo 14\)\.	

\- Vlr Unit Conv \(C181\-12\): Valor unitário da mercadoria calculado com base na saída objeto da devolução, considerando: \[Valor Contábil do Item da Saída \(campo 64 da SAFX08\)\] dividido pela Quantidade Convertida da Saída;

\- Vlr Unit ICMS Op Conv \(C181\-17\): Para saídas internas a consumidor final, esse campo não é preenchido;

\- Vlr Unit ICMS Estoque Conv \(C181\-13\): Valor Médio Unitário ICMS obtido do Cálculo da Média Ponderada Móvel, para o dia e produto da saída objeto da devolução\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada; para saídas de períodos anteriores à nova sistemática da IN087/20, o valor é calculado a partir da última nota de recebimento do produto anterior à data da saída;

\- Vlr Unit ICMS\-ST Estoque Conv \(C181\-14\): Valor Médio Unitário ICMS\-ST \+ Valor Médio Unitário FECEP\-ST obtidos do Cálculo da Média Ponderada Móvel, para o dia e produto da saída objeto da devolução\. Esses campos são demonstrados no Relatório de Conferência do Cálculo da Média Ponderada;  

Para saídas de períodos anteriores à nova sistemática da IN087/20, o valor é calculado a partir da última nota de recebimento do produto anterior a data da saída, considerando: \[Valor do ICMS\-ST \(campo 52, ou 145 ou 133 ou 107 da SAFX08\) somado FECEP\-ST \(campo 140 da SAFX08\)\] dividido pela Quantidade Convertida;

Atenção:

Quanto ao Valor do ICMS\-ST destacado na nota, o campo 52 \- Valor ICMS Substituição Tributária pode ser carregado via SAFX08 com o FECEP\-ST embutido ou não\. 

Por isso, quando o FECEP __não__ estiver embutido no valor do ICMS\-ST, marcar a opção “Realizar a soma dos valores FECP ao ICMS/ICMS\-ST” na equalização DATA MART e __não__ marcar a opção “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” na Geração do Movimento\.  Caso contrário, o FECEP\-ST será considerado dobrado\.  Para maiores esclarecimentos veja o tópico [Sobre Procedimento para Equalização DATA MART versus FECEP embuitido no ICMS, ICMS\-ST](#fecep)\.

\- Vlr Unit FCP\-ST Estoque Conv \(C181\-15\): Valor Médio Unitário FECEP\-ST obtido do Cálculo da Média Ponderada Móvel, para o dia e produto da saída objeto da devolução\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada; para saídas de períodos anteriores à nova sistemática da IN087/20, o valor é calculado a partir da última nota de recebimento do produto anterior a data da saída;

\- Vlr Unit ICMS Operação Conv \(C181\-16\): Valor unitário do ICMS calculado com base na saída objeto da devolução, considerando: \[Vlr Unit BC ICMS Operação Conv\] multiplicado pela Alíquota Interna dividido por 100;

  Onde:  	Vlr Unit BC ICMS Operação Conv é calculado considerando o %Redução BC parametrizado para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\):

                 Para produto sem %Redução BC: Vlr Unit BC ICMS Operação Conv = \[Valor Contábil do Item da Saída \(campo 64 da SAFX08\)\] dividido pela Quantidade Convertida da Saída;  

                 Para produto com %Redução BC: Vlr Unit BC ICMS Operação Conv = \[\(Valor Contábil do Item da Saída – \(Valor Contábil do Item da Saída \* “%Redução BC” / 100\)\)\] dividido pela Quantidade Convertida da Saída;

                  O Vlr Unit BC ICMS Operação Conv é demonstrado nesse relatório no campo “Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\)”\.  

Alíquota Interna: Aíquota parametrizada para o produto vigente em relação da data da emissão da nota de saída \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\)\.	

Vlr Unit ICMS\-ST Conv Rest \(C181\-18\): valor referente ao estorno de complemento calculado com base nos campos Vlr Unit ICMS Operação Conv \(C181\-16\), Vlr Unit ICMS Estoque Conv \(C181\-13\), Vlr Unit ICMS\-ST Estoque Conv \(C181\-14\);	

Vlr Unit FCP\-ST Conv Rest \(C181\-19\): valor referente ao estorno de complemento calculado com base no campo Vlr Unit ICMS\-ST Conv Rest \(C181\-18\) aplicando a Aliquota FECEP parametrizada para o produto vigente em relação da data da emissão da nota de saída \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\);

Vlr Unit ICMS\-ST Conv Compl \(C181\-20\): valor referente ao estorno de ressarcimento calculado com base nos campos Vlr Unit ICMS Operação Conv \(C181\-16\), Vlr Unit ICMS Estoque Conv \(C181\-13\), Vlr Unit ICMS\-ST Estoque Conv \(C181\-14\);

Vlr Unit FCP\-ST Conv Compl \(C181\-21\): valor referente ao estorno de ressarcimento calculado com base no campo Vlr Unit ICMS\-ST Conv Compl \(C181\-20\) aplicando a Aliquota FECEP parametrizada para o produto vigente em relação da data da emissão da nota de saída \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\);

- Campos Auxiliares origem Cadastro do Produto \(SAFX2013\):

\- Ind Produto \(SAFX2013\-01\) Cod Produto \(SAFX2013\-02\),

 \- Medida Produto \(SAFX2013\-14\), 

\- NCM Produto \(SAFX2013\-05\), 

\- CEST Produto \(SAFX2013\-54\)

Para consultar o cadastro do produto \(SAFX2013\) acessar o módulo Básicos \[menu: Data Warehouse > Manutenção > Códigos > Produto\]\.

- Campos Auxiliares origem Parametrização do Produto:

\- %Redução BC \(Parametrização Produto\)	

\- Alíq\. Interna \(Parametrização Produto\)	

\- Alíq\. FCP \(Parametrização Produto\)

Para consulta acesse o menu Parâmetros > Produto, opções por Código, por NCM ou por CEST;

Observe que a parametrização do produto considerada é a vigente em relação a data da emissão da saída objeto da devolução\.

- Campos Auxiliares origem Documento Fiscal de Devolução \(SAFX08\):

\- Qtde Item NF Devolução \(SAFX08\-24\)

\- Qtde Conv Item NF Devolução \(SAFX08\-137\)

\- Medida Item NF Devolução \(SAFX08\-25\)

\- Fator Conv NF Devolução \(Cadastro Conversão Medida\): Fator de Conversão da Unidade de Origem sendo a Medida do Item NF Devolução e Unidade de Destino à Medida do Produto, cadastrado no módulo Básicos \[menu: Data Warehouse > Manutenção > Cadastros > Conversão de Unidades de Medida, opções Padrão ou Por Produto\];

\- Qtde Conv Calculada p/ NF Devolução: quantidade convertida calculada a partir da aplicaçao do Fator de Conversão à Qtde Item NF Devolução \(SAFX08\-24\)\.  Ou a Qtde Conv Item NF Devolução \(SAFX08\-137\), caso a quantidade convertida já venha carregada no item da NF de devolução\.

\- Qtde Devolvida \(SAFX192\-24\): caso a nota de devolução referencie à nota de saída através da SAFX192, quantidade devolvida informada no campo 24 da SAFX192\.

\- Qtde Devolvida Conv Calculada \(SAFX192\-24 aplicado Fator Conv\): quantidade convertida calculada a partir da aplicaçao do Fator de Conversão à Qtde Devolvida \(SAFX192\-24\)\.

- Campos Auxiliares origem Documento Fiscal de Saída objeto da Devolução \(SAFX08\):

\- Qtde Item NF Saída \(SAFX08\-24\)	

\- Qtde Conv Item NF Saída \(SAFX08\-137\)	

\- Medida Item NF Saída \(SAFX08\-25\)	

\- Fator Conv NF Saída \(Cadastro Conversão Medida\): Fator de Conversão da Unidade de Origem sendo a Medida do Item NF Saída e Unidade de Destino a Medida do Produto, cadastrado no módulo Básicos \[menu: Data Warehouse > Manutenção > Cadastros > Conversão de Unidades de Medida, opções Padrão ou Por Produto\];	

\- Qtde Conv Calculada p/ NF Saída: quantidade convertida calculada a partir da aplicação do Fator de Conversão à Qtde Item NF Saída \(SAFX08\-24\)\.  Ou a Qtde Conv Item NF Saída \(SAFX08\-137\), caso a quantidade convertida já venha carregada no item da NF de saída\.	

\- Vlr Contabil Item NF Saída \(SAFX08\-64\)	

\- Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\):  calculado considerando o %Redução BC parametrizado para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\):

                 Para produto sem %Redução BC: Vlr Unit BC ICMS Operação Conv = \[Valor Contábil do Item \(campo 64 da SAFX08\)\] dividido pela Quantidade Convertida;  

                 Para produto com %Redução BC: Vlr Unit BC ICMS Operação Conv = \[\(Valor Contábil do Item – \(Valor Contábil do Item \* “%Redução BC” / 100\)\)\] dividido pela Quantidade Convertida\.

- Campos Auxiliares Recuperados da Média Ponderada:

\- Vlr Unit ICMS \(Recuperado da Média Ponderada na ocasião da Emissão da Saída\): Valor Médio Unitário ICMS obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit ICMS\-ST\(s/ FECEP\-ST\) \(Recuperado da Média Ponderada na ocasião da Emissão da Saída\): Valor Médio Unitário ICMS\-ST obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit BC ICMS\-ST \(Recuperado da Média Ponderada na ocasião da Emissão da Saída\): Valor Médio Unitário Base de Cálculo do ICMS\-ST obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit FECEP\-ST \(Recuperado da Média Ponderada na ocasião da Emissão da Saída\): Valor Médio Unitário FECEP\-ST obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

- Campos Auxiliares origem Documento Fiscal – Último Recebimento \(SAFX08\):

Para saídas de períodos anteriores à nova sistemática da IN087/20, os valores unitários não serão recuperados da Média Ponderada para preenchimento dos campos Vlr Unit ICMS Estoque Conv, Vlr Unit ICMS\-ST Estoque Conv e Vlr Unit FCP\-ST Estoque Conv\. Tais valores são calculados a partir da última nota de recebimento do produto anterior a data da saída\. Abaixo as informações dessa nota de entrada para apoio na conferência do C181:

\- Num Docfis NF Última Entrada	

\- Serie NF Última Entrada	

\- SubSerie NF Última Entrada	

\- Dt Fiscal NF Última Entrada	

\- Num Item NF Última Entrada	

\- Qtde Item NF Última Entrada \(SAFX08\-24\)	

\- Qtde Conv Item NF Última Entrada \(SAFX08\-137\)	

\- Medida Item NF Última Entrada \(SAFX08\-25\)	

\- Fator Conv NF Última Entrada \(Cadastro Conversão Medida\)

\- Qtde Conv Calculada p/ NF Última Entrada	

\- Vlr ICMS Item NF Última Entrada \(SAFX08\-43,80,225\)	

\- Vlr ICMS\-ST Item NF Última Entrada \(SAFX08\-52,145,133,107\)	

\- Vlr BC ICMS\-ST Item NF Última Entrada \(SAFX08\-61,144,106\)	

\- Vlr FECEP\-ST Item NF Última Entrada \(SAFX08\-144\)	

- Campos Auxiliares para o Cálculo da Média Ponderada:

\- Vlr Unit ICMS \(p/ Cálculo da Média Ponderada\): igual ao campo Vlr Unit ICMS Estoque Conv \(C181\-13\);

\- Vlr Unit ICMS\-ST \(s/ FECEP\-ST\) \(p/ Cálculo da Média Ponderada\): Valor Médio Unitário ICMS\-ST obtido do Cálculo da Média Ponderada Móvel, para o dia e produto da saída objeto da devolução\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada\.

Para saídas de períodos anteriores à nova sistemática da IN087/20, o valor é calculado a partir da última nota de recebimento do produto anterior à data da saída, considerando: \[Valor do ICMS\-ST \(campo 52, ou 145 ou 133 ou 107 da SAFX08\) subtraído FECEP\-ST \(campo 140 da SAFX08\)\] dividido pela Quantidade Convertida;

Atenção:

Quanto ao Valor do ICMS\-ST destacado na nota, o campo 52 \- Valor ICMS Substituição Tributária pode ser carregado via SAFX08 com o FECEP\-ST embutido ou não\. 

Por isso, quando o FECEP __não__ estiver embutido no valor do ICMS\-ST, marcar a opção “Realizar a soma dos valores FECP ao ICMS/ICMS\-ST” na equalização DATA MART e __não__ marcar a opção “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” na Geração do Movimento\.  Caso contrário, o FECEP\-ST será considerado dobrado\.  Para maiores esclarecimentos veja o tópico [Sobre Procedimento para Equalização DATA MART versus FECEP embuitido no ICMS, ICMS\-ST](#fecep)\.

\- Vlr Unit BC ICMS\-ST \(p/ Cálculo da Média Ponderada\): Valor Médio Unitário Base de Cálculo do ICMS\-ST obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada\.

Para saídas de períodos anteriores à nova sistemática da IN087/20, o valor é calculado a partir da última nota de recebimento do produto anterior à data da saída, considerando: \[Valor da BC ICMS\-ST \(campo 61, ou 144 ou 106 da SAFX08\)\] dividido pela Quantidade Convertida;

\- Vlr Unit FECEP\-ST \(p/ Cálculo da Média Ponderada\): igual ao campo Vlr Unit FCP\-ST Estoque Conv \(C181\-15\);

\- Vlr ICMS \(p/ Cálculo da Média Ponderada\): Valor calculado considerando: \[Qtde Conv \(C181\-03\) x Vlr Unit ICMS \(p/ Cálculo da Média Ponderada\)\]\.  O total desse valor por dia e produto é apresentado no campo “Valor ICMS \(Devolução Saída\)” do Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr ICMS\-ST \(s/ FCP\-ST\) \(p/ Cálculo da Média Ponderada\):  Valor calculado considerando: \[Qtde Conv \(C181\-03\) x Vlr Unit ICMS\-ST \(s/ FECEP\-ST\) \(p/ Cálculo da Média Ponderada\)\]\. O total desse valor por dia e produto é apresentado no campo “Valor ICMS\-ST \(Devolução Saída\)” do Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr BC ICMS\-ST \(p/ Cálculo da Média Ponderada\): Valor calculado considerando: \[Qtde Conv \(C181\-03\) x Vlr Unit BC ICMS\-ST \(p/ Cálculo da Média Ponderada\)\]\. O total desse valor por dia e produto é apresentado no campo “Valor Base de Cálculo do ICMS\-ST \(Devolução Saída\)” do Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr FECEP\-ST \(p/ Cálculo da Média Ponderada\): Valor calculado considerando: \[Qtde Conv \(C181\-03\) x Vlr Unit FECEP\-ST \(p/ Cálculo da Média Ponderada\)\]\.  O total desse valor por dia e produto é apresentado no campo “Valor FECEP\-ST \(Devolução Saída\)” do Relatório de Conferência do Cálculo da Média Ponderada\.

__Relatório de Conferência do C186:__

- Campos de Identificação da Nota Fiscal de Devolução:

\- Do 1º ao 11º campo : identificação da nota fiscal de devolução com o número do item de mercadoria \(Cod Empresa, Cod Estab, Dt Fiscal NF Devolução, E/S NF Devolução, Norm/Dev NF Devolução, Cod Docto NF Devolução, Ind Fis/Jur NF Devolução Cod Fis/Jur NF Devolução, Num Docfis NF Devolução, Serie NF Devolução, SubSerie NF Devolução, Num Item NF Devolução\);

- Campos do Layout do C186:

\- Num Docfis NF Entrada\(C186\-11\), Serie NF Entrada \(C186\-10\), Dt Fiscal NF Entrada \(C186\-13\), Num Item NF Entrada\(C186\-14\): campos de identificação da nota de Entrada;

\- Cod Motivo \(C186\-06\): 

\- Qtde Conv \(C186\-07\): Quantidade \(campo 24 da SAFX08\) do item documento fiscal de devolução, quando a unidade de medida do item é igual a do Cadastro do Produto \(SAFX2013 – campo 14\)\.

                                            Caso a medida do item do documento fiscal de devolução seja diferente da medida no cadastro do produto, esse campo demonstra o resultado da multiplicação do campo Quantidade \(campo 24 da 

                                            SAFX08\) pelo Fator de Conversão \(veja tópico [Cadastro de Conversão de Unidades de Medidas](#Conv_Medidas)\), ou apresenta a quantidade já convertida carregada no campo 137 da SAFX08\.

\- Medida \(C186\-08\): Unidade de Medida do Cadastro do Produto \(SAFX2013 – campo 14\);

\- Vlr Unit Conv \(C186\-15\): Valor unitário da mercadoria calculado com base na entrada objeto da devolução, considerando: \[Valor Contábil do Item da Entrada\(campo 64 da SAFX08\) subtraído o Valor do ICMS\-ST da Entrada \(campo 52, ou 145 ou 133 ou 107 da SAFX08\)\] dividido pela Quantidade Convertida da Entrada\.  Para entradas de períodos anteriores à nova sistemática da IN087/20, o valor será oriundo do inventário \(SAFX52\), caso a opção “do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)” tenha sido escolhida na tela da geração\.

\- Vlr Unit ICMS Conv \(C186\-16\): Valor unitário do ICMS calculado com base na entrada objeto da devolução, considerando: \[Valor do ICMS da Entrada \(campo 43, ou 80 ou 225 da SAFX08\)\] dividido pela Quantidade Convertida da Entrada\.  Para entradas de períodos anteriores à nova sistemática da IN087/20, o valor será oriundo do inventário \(SAFX52\), caso a opção “do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)” tenha sido escolhida na tela da geração\.

\- Vlr Unit BC ICMS\-ST Conv \(C186\-17\): Valor unitário da Base do ICMS\-ST calculado com base na entrada objeto da devolução, considerando: \[Valor BC ICMS\-ST da Entrada \(campo 61, ou 144 ou 106 da SAFX08\)\] dividido pela Quantidade Convertida da Entrada\.  Para entradas de períodos anteriores à nova sistemática da IN087/20, o valor será oriundo do inventário \(SAFX52\), caso a opção “do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)” tenha sido escolhida na tela da geração\.

\- Vlr Unit ICMS\-ST Conv \(C186\-18\): Valor unitário do ICMS\-ST calculado com base na entrada objeto da devolução, considerando: \[Valor do ICMS\-ST da Entrada \(campo 52, ou 145 ou 133 ou 107 da SAFX08\) somado FECEP\-ST \(campo 140 da SAFX08\)\] dividido pela Quantidade Convertida da Entrada\.  Para entradas de períodos anteriores à nova sistemática da IN087/20, o valor será oriundo do inventário \(SAFX52\), caso a opção “do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)” tenha sido escolhida na tela da geração\.

Atenção:

Quanto ao Valor do ICMS\-ST destacado na nota, o campo 52 \- Valor ICMS Substituição Tributária pode ser carregado via SAFX08 com o FECEP\-ST embutido ou não\. 

Por isso, quando o FECEP __não__ estiver embutido no valor do ICMS\-ST, marcar a opção “Realizar a soma dos valores FECP ao ICMS/ICMS\-ST” na equalização DATA MART e __não__ marcar a opção “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” na Geração do Movimento\.  Caso contrário, o FECEP\-ST será considerado dobrado\.  Para maiores esclarecimentos veja o tópico [Sobre Procedimento para Equalização DATA MART versus FECEP embuitido no ICMS, ICMS\-ST](#fecep)\.

\- Vlr Unit FCP\-ST Conv \(C186\-19\): Valor unitário do FECEP\-ST calculado com base na entrada objeto da devolução, considerando: \[FECEP\-ST da Entrada \(campo 140 da SAFX08\)\] dividido pela Quantidade Convertida da Entrada\. Para entradas de períodos anteriores à nova sistemática da IN087/20, o valor será oriundo do inventário \(SAFX52\), caso a opção “do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)” tenha sido escolhida na tela da geração\.

- Campos Auxiliares origem Cadastro do Produto \(SAFX2013\):

\- Ind Produto \(SAFX2013\-01\) Cod Produto \(SAFX2013\-02\),

 \- Medida Produto \(SAFX2013\-14\), 

\- NCM Produto \(SAFX2013\-05\), 

\- CEST Produto \(SAFX2013\-54\)

Para consultar o cadastro do produto \(SAFX2013\) acessar o módulo Básicos \[menu: Data Warehouse > Manutenção > Códigos > Produto\]\.

- Campos Auxiliares origem Documento Fiscal de Devolução \(SAFX08\):

\- Qtde Item NF Devolução \(SAFX08\-24\)	

\- Qtde Conv Item NF Devolução \(SAFX08\-137\)	

\- Medida Item NF Devolução \(SAFX08\-25\)	

\- Fator Conv NF Devolução \(Cadastro Conversão Medida\): Fator de Conversão da Unidade de Origem sendo a Medida do Item NF Devolução e Unidade de Destino à Medida do Produto, cadastrado no módulo Básicos \[menu: Data Warehouse > Manutenção > Cadastros > Conversão de Unidades de Medida, opções Padrão ou Por Produto\];

- Campos Auxiliares origem Documento Fiscal de Entrada objeto da Devolução \(SAFX08\):

\- Qtde Item NF Entrada \(SAFX08\-24\)	

\- Qtde Conv Item NF Entrada \(SAFX08\-137\)	

\- Medida Item NF Entrada \(SAFX08\-25\)	

\- Fator Conv NF Entrada \(Cadastro Conversão Medida\): Fator de Conversão da Unidade de Origem sendo a Medida do Item NF Entrada e Unidade de Destino à Medida do Produto, cadastrado no módulo Básicos \[menu: Data Warehouse > Manutenção > Cadastros > Conversão de Unidades de Medida, opções Padrão ou Por Produto\];	

\- Qtde Conv Calculada p/ NF Entrada: quantidade convertida calculada a partir da aplicaçao do Fator de Conversão à Qtde Item NF Entrada \(SAFX08\-24\)\.  Ou a Qtde Conv Item NF Entrada \(SAFX08\-137\), caso a quantidade convertida já venha carregada no item da NF de s Entrada;	

\- Vlr Contabil Item NF Entrada \(SAFX08\-64\)	

\- Vlr ICMS Item NF Entrada \(SAFX08\-43,80,225\): Considerado o Campo “43\-Valor ICMS”, se preenchido, ou Campo “80\-ICMS não Escriturado”, se preenchido, ou Campo “225\-Valor ICMS Não Destacado”;

\- Vlr BC ICMS\-ST Item NF Entrada \(SAFX08\-61,144,106\): Considerado o Campo “61\- Base ICMS Substituição Tributária”, se preenchido, ou Campo “144\- Base ICMS\-ST não Escriturada”, se preenchido, ou  Campo “106\- Base Cálculo Carga Tributária Origem ICMS” ;

\- Vlr ICMS\-ST Item NF Entrada \(SAFX08\-52,145,133,107\): Considerado o Campo “52\- Valor ICMS Substituição Tributária”, se preenchido, ou  Campo “133\- ICMS ST Não Escriturado”, se preenchido, ou Campo “145\-Valor de ICMS – ST Não escriturado”, se preenchido, ou Campo “107\- Valor Carga Tributária Origem ICMS”

\- Vlr FECEP\-ST Item NF Entrada \(SAFX08\-144\)	

- Campos Auxiliares Recuperados do Inventário \(SAFX52\):

Registro do inventário do produto cuja Data Inventário é igual a “Dt anterior à adoção IN\-RE087/20” informada na tela de geração\.

\- Vlr Unit ICMS Inventário: campo 21 \- Valor de ICMS Médio da SAFX52 

\- Vlr Unit ICMS\-ST Inventário: campo 22 \- Valor de ICMS\-ST Médio SAFX52

\- Vlr Unit BC ICMS\-ST Inventário : campo 43 \- Valor Base ICMS\-ST Médio SAFX52

\- Vlr Unit FECEP\-ST Inventário: campo 44 \- Valor FECEP Médio SAFX52

- Campos Auxiliares para o Cálculo da Média Ponderada:

\- Vlr Unit ICMS \(p/ Cálculo da Média Ponderada\): igual ao campo Vlr Unit ICMS Conv \(C186\-16\);	

\- Vlr Unit ICMS\-ST \(s/ FECEP\-ST\) \(p/ Cálculo da Média Ponderada\): Valor unitário do ICMS\-ST calculado com base na entrada objeto da devolução, considerando: \[Valor do ICMS\-ST da Entrada \(campo 52, ou 145 ou 133 ou 107 da SAFX08\) subtraído FECEP\-ST \(campo 140 da SAFX08\)\] dividido pela Quantidade Convertida da Entrada\.  Para entradas de períodos anteriores à nova sistemática da IN087/20, o valor será oriundo do inventário \(SAFX52\), caso a opção “do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)” tenha sido escolhida na tela da geração\.

Atenção:

Quanto ao Valor do ICMS\-ST destacado na nota, o campo 52 \- Valor ICMS Substituição Tributária pode ser carregado via SAFX08 com o FECEP\-ST embutido ou não\. 

Por isso, quando o FECEP __não__ estiver embutido no valor do ICMS\-ST, marcar a opção “Realizar a soma dos valores FECP ao ICMS/ICMS\-ST” na equalização DATA MART e __não__ marcar a opção “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” na Geração do Movimento\.  Caso contrário, o FECEP\-ST será considerado dobrado\.  Para maiores esclarecimentos veja o tópico [Sobre Procedimento para Equalização DATA MART versus FECEP embuitido no ICMS, ICMS\-ST](#fecep)\.

\- Vlr Unit BC ICMS\-ST \(p/ Cálculo da Média Ponderada\): igual ao campo Vlr Unit BC ICMS\-ST Conv \(C186\-17\);

\- Vlr Unit FECEP\-ST \(p/ Cálculo da Média Ponderada\): igual ao campo Vlr Unit FCP\-ST Conv \(C186\-19\);

\- Vlr ICMS \(p/ Cálculo da Média Ponderada\): Valor calculado considerando: \[Qtde Conv \(C186\-07\) x Vlr Unit ICMS \(p/ Cálculo da Média Ponderada\)\]\.  O total desse valor por dia e produto é apresentado no campo “Valor ICMS \(Devolução Entrada\)” do Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr ICMS\-ST \(s/ FECEP\-ST\) \(p/ Cálculo da Média Ponderada\): Valor calculado considerando: \[Qtde Conv \(C186\-07\) x Vlr Unit ICMS\-ST \(s/ FECEP\-ST\) \(p/ Cálculo da Média Ponderada\)\]\. O total desse valor por dia e produto é apresentado no campo “Valor ICMS\-ST \(Devolução Entrada\)” do Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr BC ICMS\-ST \(p/ Cálculo da Média Ponderada\): Valor calculado considerando: \[Qtde Conv \(C186\-07\) x Vlr Unit BC ICMS\-ST \(p/ Cálculo da Média Ponderada\)\]\. O total desse valor por dia e produto é apresentado no campo “Valor Base de Cálculo do ICMS\-ST \(Devolução Entrada\)” do Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr FECEP\-ST \(p/ Cálculo da Média Ponderada\): Valor calculado considerando: \[Qtde Conv \(C186\-07\) x Vlr Unit FECEP\-ST \(p/ Cálculo da Média Ponderada\)\]\.  O total desse valor por dia e produto é apresentado no campo “Valor FECEP\-ST \(Devolução Entrada\)” do Relatório de Conferência do Cálculo da Média Ponderada;

__Relatório de Conferência do Cálculo da Média Ponderada:__

Para cada produto e dia do mês da geração é gravada uma linha do relatório, contendo as seguintes informações:

\- Qtde Inicial: Para o primeiro dia do Mês, considera\-se a Qtde Final do último dia do Mês anterior, obtido da Média Ponderada calculada na geração do movimento do período anterior\. Caso a Geração do Movimento não tenha sido realizada para o mês anterior, este valor é oriundo do Inventário do produto \(SAFX52\) – campo 13 – Quantidade\.  Para os demais dias do mês, considera\-se a Qtde Final do dia anterior demonstrada no Relatório do Cálculo da Média Ponderada do período\.

\- Valor ICMS Inicial: Para o primeiro dia do Mês, considera\-se o “Valor ICMS Final” do último dia do Mês anterior, obtido da Média Ponderada calculada na geração do movimento do período anterior\. Caso a Geração do Movimento não tenha sido realizada para o mês anterior, este valor é oriundo do Inventário do produto \(SAFX52\), campo 13 – Quantidade multiplicado pelo campo 21 \- Valor de ICMS Médio\.  Para os demais dias do mês, considera\-se o “Valor ICMS Final” do dia anterior demonstrado no Relatório do Cálculo da Média Ponderada do período\.

 \- Valor ICMS\-ST Inicial: Para o primeiro dia do Mês, considera\-se o “Valor ICMS\-ST Final” do último dia do Mês anterior, obtido da Média Ponderada calculada na geração do movimento do período anterior\. Caso a Geração do Movimento não tenha sido realizada para o mês anterior, este valor é oriundo do Inventário do produto \(SAFX52\), campo 13 – Quantidade multiplicado pelo campo 22 \- Valor de ICMS\-ST Médio\.  Para os demais dias do mês, considera\-se a “Valor ICMS\-ST Final” do dia anterior demonstrado no Relatório do Cálculo da Média Ponderada do período\.

 \- Valor Base de Cálculo do ICMS\-ST Inicial: Para o primeiro dia do Mês, considera\-se o “Valor Base de Cálculo do ICMS\-ST Final” do último dia do Mês anterior, obtido da Média Ponderada calculada na geração do movimento do período anterior\. Caso a Geração do Movimento não tenha sido realizada para o mês anterior, este valor é oriundo do Inventário do produto \(SAFX52\), campo 13 – Quantidade multiplicado pelo campo 43 \- Valor Base ICMS\-ST Médio\.  Para os demais dias do mês, considera\-se o “Valor Base de Cálculo do ICMS\-ST Final” do dia anterior demonstrado no Relatório do Cálculo da Média Ponderada do período\.

 \- Valor \-ST Inicial: Para o primeiro dia do Mês, considera\-se o “Valor FECEP\-ST Final” do último dia do Mês anterior, obtido da Média Ponderada calculada na geração do movimento do período anterior\. Caso a Geração do Movimento não tenha sido realizada para o mês anterior, este valor é oriundo do Inventário do produto \(SAFX52\), campo 13 – Quantidade multiplicado pelo campo 44 \- Valor Base FECEP Médio\.  Para os demais dias do mês, considera\-se o “FECEP Valor FECEP\-ST Final” do dia anterior demonstrado no Relatório do Cálculo da Média Ponderada do período\.

\- Qtde \(Devolução Saída\): Totalização do campo “Qtde Conv \(C181\-03\)” dos movimentos demonstrados no Relatório de Conferência do C181 por dia e produto\.

\- Valor ICMS \(Devolução Saída\): Totalização do campo “Vlr ICMS \(p/ Cálculo da Média Ponderada\)” dos movimentos demonstrados no Relatório de Conferência do C181 por dia e produto\.

\- Valor ICMS\-ST \(Devolução Saída\): Totalização do campo “Vlr ICMS\-ST\(s/ FECEP\-ST\) \(p/ Cálculo da Média Ponderada\)” dos movimentos demonstrados no Relatório de Conferência do C181 por dia e produto\.

\- Valor Base de Cálculo do ICMS\-ST \(Devolução Saída\): Totalização do campo “Vlr BC ICMS\-ST \(p/ Cálculo da Média Ponderada\)” dos movimentos demonstrados no Relatório de Conferência do C181 por dia e produto\.

\- Valor FECEP\-ST \(Devolução Saída\): Totalização do campo “Vlr FECEP\-ST \(p/ Cálculo da Média Ponderada\)” dos movimentos demonstrados no Relatório de Conferência do C181 por dia e produto\.

\- Qtde \(Entrada\): Totalização do campo “Qtde Conv \(C180\-03\)” dos movimentos demonstrados no Relatório de Conferência do C180 por dia e produto\.

\- Valor ICMS \(Entrada\): Totalização do campo “Vlr ICMS \(p/ Cálculo da Média Ponderada\)” dos movimentos demonstrados no Relatório de Conferência do C180 por dia e produto\.

\- Valor ICMS\-ST \(Entrada\): Totalização do campo “Vlr ICMS\-ST\(s/ FECEP\-ST\) \(p/ Cálculo da Média Ponderada\)” dos movimentos demonstrados no Relatório de Conferência do C180 por dia e produto\.

\- Valor Base de Cálculo do ICMS\-ST \(Entrada\): Totalização do campo “Vlr BC ICMS\-ST \(p/ Cálculo da Média Ponderada\)” dos movimentos demonstrados no Relatório de Conferência do C180 por dia e produto\.

\- Valor FECEP\-ST \(Entrada\): Totalização do campo “Vlr FECEP\-ST \(p/ Cálculo da Média Ponderada\)” dos movimentos demonstrados no Relatório de Conferência do C180 por dia e produto\.

\- Qtde \(Devolução Entrada\): Totalização do campo “Qtde Conv \(C186\-07\)” dos movimentos demonstrados no Relatório de Conferência do C180 por dia e produto\.

\- Valor ICMS \(Devolução Entrada\): Totalização do campo “Vlr ICMS \(p/ Cálculo da Média Ponderada\)” dos movimentos demonstrados no Relatório de Conferência do C186 por dia e produto\.

\- Valor ICMS\-ST \(Devolução Entrada\): Totalização do campo “Vlr ICMS\-ST\(s/ FECEP\-ST\) \(p/ Cálculo da Média Ponderada\)” dos movimentos demonstrados no Relatório de Conferência do C186 por dia e produto\.

\- Valor Base de Cálculo do ICMS\-ST \(Devolução Entrada\): Totalização do campo “Vlr BC ICMS\-ST \(p/ Cálculo da Média Ponderada\)” dos movimentos demonstrados no Relatório de Conferência do C186 por dia e produto\.

\- Valor FECEP\-ST \(Devolução Entrada\): Totalização do campo “Vlr FECEP\-ST \(p/ Cálculo da Média Ponderada\)” dos movimentos demonstrados no Relatório de Conferência do C186 por dia e produto\.

\- Qtde Final: Qtde Inicial \+  Qtde \(Devolução Saída\) \+ Qtde \(Entrada\) \- Qtde \(Devolução Entrada\)\.

\- Valor ICMS Final: Valor ICMS Inicial \+ Valor ICMS \(Devolução Saída\) \+ Valor ICMS \(Entrada\) \- Valor ICMS \(Devolução Entrada\)\.

\- Valor ICMS\-ST Final: Valor ICMS\-ST Inicial \+ Valor ICMS\-ST \(Devolução Saída\) \+ Valor ICMS\-ST \(Entrada\) \- Valor ICMS\-ST \(Devolução Entrada\)\.

\- Valor Base de Cálculo do ICMS\-ST Final: Valor Base de Cálculo do ICMS\-ST Inicial \+ Valor Base de Cálculo do ICMS\-ST \(Devolução Saída\) \+ Valor Base de Cálculo do ICMS\-ST \(Entrada\) \- Valor Base de Cálculo do ICMS\-ST \(Devolução Entrada\)\.

\- Valor FECEP\-ST Final: Valor FECEP\-ST Inicial \+ Valor FECEP\-ST \(Devolução Saída\) \+ Valor FECEP\-ST \(Entrada\) \- Valor FECEP\-ST \(Devolução Entrada\)\.

\- Valor Médio Unitário ICMS: Valor ICMS Final dividido por Qtde Final\.

\- Valor Médio Unitário ICMS\-ST: Valor ICMS\-ST Final dividido por Qtde Final\.

\- Valor Médio Unitário Base de Cálculo Base de Cálculo do ICMS\-ST: Valor ICMS\-ST Final dividido por Qtde Final\.

\- Valor Médio Unitário  FECEP\-ST: Valor FECEP\-ST Final dividido por Qtde Final\.

__Sobre reprocessamento de períodos já apurados__:

Caso haja necessidade de processar um período anterior, todos os períodos subsequentes devem ser reprocessados\.

__Orientação de preenchimento dos campos:__

__Período:__ Informar o período \(Mês e Ano\) para a geração dos movimentos; Segundo IN\-RE087/20, a adoção da nova sistemática é válida a partir de Janeiro/2021\.

__Utilizar somente DATA MART p/períodos anteriores:__ Através deste campo o usuário pode optar como será feita a recuperação dos dados de notas de períodos anteriores\.  O parâmetro é utilizado da seguinte forma:

\- Marcado: A recuperação das notas de períodos anteriores é feita com base no DATA MART;

\- Desmarcado: A recuperação destas notas de períodos anteriores é feita com base nas tabelas “normais” \(tabelas X07/X08\)\.

Importante observar que a recuperação das notas do período, é feita sempre através do DATA MART, independentemente do parâmetro\. O parâmetro se aplica apenas à recuperação das notas de períodos anteriores\.

Quando o parâmetro for marcado, é importante que o usuário tenha a certeza de que o DATA MART esteja equalizado para os períodos anteriores, o tempo suficiente que permita a identificação das entradas\.

__Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\): __Caso os valores de FECEP já venham embutidos nos valores de ICMS/ICMS\-ST \(campos 43 e 52 da SAFX08\) dos itens de mercadoria, esse parâmetro deve ser marcado na geração do movimento de entrada\.

Na escrituração dos documentos fiscais, os valores de FECEP podem ou não compor os valores de ICMS e ICMS\-ST\. Isso é uma determinação oriunda de cada Unidade Federativa\. Sendo assim, o sistema contempla os seguintes cenários para os itens de mercadoria \(SAFX08\):

\- Valores de FECEP embutidos nos valores de ICMS e ICMS\-ST \(campos 43 e 52 da SAFX08\);

\- Valores de FECEP separados dos valores de ICMS e ICMS\-ST \(campos 43 e 52 da SAFX08\);

Independente dos valores estarem embutidos, os itens de mercadoria \(SAFX08\) possuem campos específicos para FECEP \(138 a 141\)\.

A geração do Valor ICMS\-ST dos movimentos de entradas – C180 e Devoluções de Entradas – C186 deve conter o FECEP\-ST\. É necessário saber se o FECEP já vem embutido no campo 52\-ICMS\-ST da SAFX08, para que a rotina some ou não o valor do FECE\-ST\( campo 140\) ao ICMS\-ST \(campo 52\)\.   

Caso os valores de FECEP já estejam embutidos nos valores de ICMS/ICMS\-ST \(campos 43 e 52 da SAFX08\), esse parâmetro deve ser marcado evitando duplicidade do FECP no cálculo\.

Para mais informações consulte o tópico: [Sobre Procedimento para Equalização DATA MART versus FECEP embuitido no ICMS, ICMS\-ST](#fecep)

__Valores Unitários Médios recuperados__: escolha a opção “do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)” caso deseje que os valores unitários do ICMS, ICMS\-ST sejam recuperados do inventário\.

Escolha a opção “da própria Nota de Entrada referenciada pela Devolução” caso deseje que os valores unitários sejam calculados a partir dos valores presentes na nota de entrada\. Para maiores informações consulte o tópico “[__Sobre Geração do Movimento de Devolução de Entrada \(C186\)__](#sobre_c186)__”__\.

Dt anterior à adoção IN\-RE087/20: preencher com o dia imediatamente anterior ao primeiro mês de geração do movimento pela IN\-RE087/20\.  Por exemplo: se a primeira geração ocorrer em abril de 2021, esta data deve ser preenchida com 31/03/2021, em todos os períodos de geração, não apenas em abril de 2021\.  Para maiores informações consulte o tópico “[__Sobre Geração do Movimento de Devolução de Entrada \(C186\)__](#sobre_c186)__”__\.

__Estabelecimentos:__ Apresenta a lista dos estabelecimentos da Empresa para seleção do usuário\. São disponibilizados para seleção apenas os estabelecimentos do estado do Paraná\.

Como facilitador, podem ser utilizadas as opções “Selecionar” e “Marcar todos”, para selecionar um os mais estabelecimentos específicos, e marcar todos os estabelecimentos exibidos simultaneamente\.

### <a id="_Toc64492385"></a>– Transferência dos Movimentos para EFD FISCAL

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Geração >> \(IN\-RE 087/20\) >> Transferência dos Movimentos para EFD Fiscal

 

__Descrição:__

A Transferência dos Movimentos para a EFD Fiscal deve ser executada quando os resultados da Geração do Movimento estiverem validados\.  Esta é a última etapa anterior à geração do Meio Magnético no módulo Sped >> EFD – Escrituração Fiscal Digital\.

Essa rotina é responsável por:

- Transferir os movimentos de entrada e saída, demonstrados nos Relatórios de Conferência do registro C180, C185 e C380, para a tabela SAFX296, base para geração dos C180, C185 e C380 do Sped Fiscal\. 
- Transferir os movimentos de devolução de entrada e devolução de saída, demonstrados nos Relatórios de Conferência do registro C181 e C186, para a tabela SAFX308, base para geração dos C181 e C186 do Sped Fiscal\.
- Atualizar o Inventário \(SAFX52\) do último dia do mês anterior e com Motivo do Inventário = 06, gravando os Valores Unitários do ICMS, ICMS\-ST, Base de Cálculo do ICMS\-ST e FECEP\-ST calculados pela Média Ponderada Móvel do mês anterior\. Processo realizado a partir do segundo período da adoção da sistemática da IN\-RE 087/20\.
- Gerar os registros de Saldo Consolidado da Restituição/Complemento de ICMS e gravá\-los na tabela SAFX304, base para geração do registro 1255 do Sped Fiscal\.

__Obs:__

__1\)__ A manutenção da SAFX296 é feita na tela de manutenção dos itens de documento fiscal \(SAFX08\), opção “Informações Complementare Oper\. ST \(Sped Fiscal\)”\.

__2\)__ A manutenção da SAFX308 é feita na tela de manutenção dos itens de documento fiscal \(SAFX08\), opção “Informações Complementare Oper\. ST \(Sped Fiscal\) \- Devolução”\.

3\) A manutenção da SAFX304 é feita no módulo SPED \[menu: EFD – Escrituração Fiscal Digital >> Geração >>Manutenção >>Registro 1255\]

Ao final da execução da geração os seguintes relatórios são disponibilizados:

1. Relatório de Log de Erros: composto por mensagens que apontam para falta de informações em documentos, parametrizações e cadastros\. Com base nesse relatório é possível realizar as correções na base para obter uma finalização do processo com sucesso\.
2. Relatórios de Conferência do 1255: relatório em arquivo formato cvs, demonstrando por código de motivo, os valores de restituição e complementação\. 
3. Relatório de Quantidade Total de Registros Gravados: apresenta o total de registros C180, C181, C185, C186, C380 que foram lidos da Geração do Movimento e gravados nas tabelas SAFX296, SAFX308 para geração do Sped Fiscal\.  Apresenta o total de registros 1255 gravados na tabela SAFX304 e o total de registros de Inventário atualizados na SAFX52\.

__Orientação de preenchimento dos campos:__

__Período:__ Informar o período \(Mês e Ano\) para a geração dos movimentos; Segundo IN\-RE087/20, a adoção da nova sistemática é válida a partir de Janeiro/2021\.

__Estabelecimentos:__ Apresenta a lista dos estabelecimentos da Empresa para seleção do usuário\. São disponibilizados para seleção apenas os estabelecimentos do estado do Paraná\.

Como facilitador, podem ser utilizadas as opções “Selecionar” e “Marcar todos”, para selecionar um os mais estabelecimentos específicos, e marcar todos os estabelecimentos exibidos simultaneamente\.

## <a id="_Toc23774813"></a><a id="_Toc64492386"></a>Criação / Alteração de Tabelas \(Fixas, Acessórias, Básicas\)

## <a id="_Toc354574233"></a><a id="_Toc354574408"></a><a id="_Toc354574452"></a><a id="_Toc354574537"></a><a id="_Toc354578083"></a><a id="_Toc354578310"></a><a id="_Toc354579001"></a><a id="_Toc354579142"></a><a id="_Toc23774814"></a><a id="_Toc64492387"></a>Criação / Alteração de Roteiro Operacional

ROTEIRO OPERACIONAL  
RESSARCIMENTO E COMPLEMENTO DE ICMS\-ST – RS \(IN\-RE 048/2018 e in\-re087/20\)

[__Objetivo__](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/Estadual/Ressarcimento_de_ICMS_ST_RS/rot_safufrcrs.htm#objetivo)

[__Procedimentos para utilização do módulo__](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/Estadual/Ressarcimento_de_ICMS_ST_RS/rot_safufrcrs.htm#proc_uti)__ para atendimento a IN\-RE 048/18__

[__Procedimentos a serem executados a cada período__](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/Estadual/Ressarcimento_de_ICMS_ST_RS/rot_safufrcrs.htm#proc_exec)__ para atendimento a IN\-RE 048/18__

[__Procedimentos para utilização do módulo__](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/Estadual/Ressarcimento_de_ICMS_ST_RS/rot_safufrcrs.htm#proc_uti)__ para atendimento a IN\-RE 087/20__

[__Procedimentos a serem executados a cada período__](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/Estadual/Ressarcimento_de_ICMS_ST_RS/rot_safufrcrs.htm#proc_exec)__ para atendimento a IN\-RE 087/20__

[__Menu Janela__](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/Estadual/Ressarcimento_de_ICMS_ST_RS/rot_safufrcrs.htm#menu_janela)

[__Menu Ajuda__](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/Estadual/Ressarcimento_de_ICMS_ST_RS/rot_safufrcrs.htm#menu_ajuda)

[__Atendimento Técnico MasterSAF__](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/Estadual/Ressarcimento_de_ICMS_ST_RS/rot_safufrcrs.htm#atendimento)

<a id="objetivo"></a><a id="_Toc64492388"></a>__Objetivo__

Refazer o texto da Introdução conforme ABAIXO:

O módulo Ressarcimento de ICMS\-ST – RS amparado pelas Instruções Normativas RE 048/2018 e RE 087/2020 tem como objetivo calcular os valores de ressarcimento e complemento de ICMS\-ST a serem apresentados nos arquivos do Sped – EFD Fiscal\.

A IN\-RE 048/2018, com vigência a partir de 1º de janeiro de 2019, estabelece a geração de uma subapuração apresentando os créditos ICMS\-ST provenientes das entradas de mercadoria e dos débitos originários das saídas para consumidor final e para outros Estados\. O ICMS\-ST a ser ressarcido ou complementado é lançado na Apuração do ICMS\-ST e demonstrado no bloco E, registros E210 e E220 do Sped – EFD Fiscal\.  A subapuração e seus detalhamentos são apresentados no bloco 1, registros 1920, 1921 e 1923 do SPED EFD\.

A IN\- RE 087/2020, com vigência a partir de 1º de janeiro de 2021, estabelece a escrituração dos movimentos de Entradas, Saídas, Devoluções de Entradas e Devoluções de Saídas dos produtos sujeitos a ICMS\-ST, nos registros C180, C181, C185, C380 e C185 do Sped – EFD Fiscal, o saldo do Ressarcimento e Complemento do ICMS\-ST nos registros 1250/1255 e os valores unitários médios do ICMS, ICMS\-ST do Inventário, no registro H030\.  Nesta sistemática é realizado o cálculo do Valor Médio Ponderado Móvel do dia, aplicado nas operações de saídas e devoluções de saídas, a fim de determinar o valor ser Ressarcido/Restituído ou Complementado do ICMS\-ST\. 

Não está disponível o atendimento ao Ressarcimento ICMS\-ST RS para empresas cuja entrega de obrigações se dá por Inscrição Estadual Única\.

Recomendamos a leitura do manual operacional \([Help](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/Estadual/Ressarcimento_de_ICMS_ST_RS/oper_safufrcrs.htm)\) desse módulo como forma de obter orientações sobre a funcionalidade desse módulo\.

<a id="proc_uti"></a><a id="_Toc64492389"></a>__Procedimentos para utilização do módulo para ATENDIMENTO A IN\-RE 048/2018__

__Pré\-requisitos__

__1\.__ O módulo de Ressarcimento de ICMS\-ST do Rio Grande do Sul utiliza as informações de tabelas fixas, acessórias e SAFX\. Para utilização de todas as suas funcionalidades, certifique\-se de tê\-las importado:

__<<<<SÓ NO MANUAL DO MASTERSAF devem ser mencionadas tabelas fixas e acessórias>>__

Módulo Ferramentas:

Menu: Tabelas Internas > Importar > Tabelas Fixas

Menu: Tabelas Internas > Importar > Tabelas Acessórias

• TACES94 \- Tabela com os Código Especificadores da Substituição Tributária

• TFIX18 \- Tabela de códigos de Operação da Apuração

• TFIX30 \- Parâmetros MasterSAF Módulos

• TFIX31 \- Parâmetros MasterSAF Nomenclatura

Módulo Job Servidor:

Menu: Carga > Programação e Execução e Importação > Programação e Execução\) ou

Importação Batch: menu Importação Batch > Programação e Execução

• SAFX07 \- Tabela de Documentos Fiscais

• SAFX08 \- Tabela de Itens de Documentos Fiscais de Mercadorias e Produtos

• SAFX104 \- Parâmetros de Produto por UF \(Ressarcimento e Complemento de ICMS\-ST\)

• SAFX128 \- Fator de Conversão de Unidade de Medida por Produto

• SAFX2007 \- Tabela de Unidade de Medida

• SAFX2012 \- Tabela de Códigos Fiscais

• SAFX2013 \- Tabela de Produtos

• SAFX2043 \- Tabela de Classificação Fiscal

• SAFX2081 \- Tabela de Extensão de CFOP

__2\.__ Cadastrar os fatores de conversão de medida no módulo DW, menu Manutenção > Cadastros > Conversão de Unidades de Medida\. Estes fatores serão utilizados, quando necessário, para converter a quantidade dos movimentos para a unidade de medida de estoque do produto;

__3\.__ Cadastrar os Código de Ajuste de SPED FISCAL no módulo Estadual > ICMS, menu Apuração > Apuração do ICMS > Lançamentos Complementares > Código de Ajuste de SPED FISCAL especificados pela Instrução Normativa RE 048/2018, para geração dos lançamentos nas Subapurações e Apuração do ICMS\-ST;

__4\.__ Cadastrar os parâmetros da Subapuração do RS para estabelecimentos, no Módulo Estadual > Ressarcimento ICMS\-ST RS \(IN\-RE 048/2018\), menu Parâmetros > IN\-RE 048/18 > Dados Iniciais; Atenção à escolha do número da Subapuração para o Ressarcimento RS, para não repetir o mesmo número de Subapurações já usadas no módulo Estadual > ICMS para escriturar o ICMS de operações especificadas em legislação estadual como obrigadas a serem apuradas em separado\.

__5\.__ Cadastrar a parametrização dos produtos a serem considerados na apuração do Ressarcimento de ICMS\-ST do Rio Grande do Sul de acordo com a Instrução Normativa 048/2018\. Esta parametrização pode ser feita por código de produto, por NCM ou por CEST, conforme as opções disponíveis no Módulo Estadual > Ressarcimento ICMS\-ST RS \(IN\-RE 048/2018\), menu Parâmetros > Produtos;

__6\.__ Cadastrar a parametrização das operações a serem consideradas na apuração do Ressarcimento de ICMS\-ST do Rio Grande do Sul de acordo com a Instrução Normativa 048/2018\. Trata\-se da movimentação de entradas, saídas para consumidor final e saídas para outras UF’s, Isentas ou Não Tributadas\. Esta parametrização está disponível por CFOP e Natureza de Operação, conforme as opções disponíveis no Módulo Estadual > Ressarcimento ICMS\-ST RS \(IN\-RE 048/2018\), menu Parâmetros > IN\-RE 048/18 > Operações;

__7\.__ Cadastrar a descrição da Subapuração criada para o Ressarcimento do RS, no módulo SPED > EFD – Escrituração Fiscal Digital, menu Parâmetros > Dados Iniciais \(Descrição das Subapurações para geração do Registro 1900\)\.

__8\.__ Criar perfil para geração dos registros 1900 e “filhos” e do bloco E, no módulo SPED > EFD – Escrituração Fiscal Digital, menu Parâmetros > Perfil\.

<a id="proc_exec"></a><a id="_Toc64492390"></a>__Procedimentos a serem executados a cada período para ATENDIMENTO A IN\-RE 048/2018__

__1\.__ Importar os Documentos Fiscais \(SAFX07/SAFX08\) no módulo Job Servidor, via carga e importação de jobs \(menus Carga > Programação e Execução e Importação > Programação e Execução\) ou via importação Batch \(menu Importação Batch > Programação e Execução\);

__2\.__ Realizar a equalização do Datamart no módulo Ferramentas > Rotinas Acessórias > DATAMART > Equalização/Limpeza;

__3\.__ Realizar a Geração do Movimento, no Módulo Estadual > Ressarcimento ICMS\-ST RS \(IN\-RE 048/2018\), menu Geração > IN\-RE 048/18 > Geração dos Movimentos;

__4\.__ Conferir o resultado da Geração do Movimento nos relatórios disponíveis no Módulo Estadual > Ressarcimento ICMS\-ST RS \(IN\-RE 048/2018\), menu Relatórios > IN\-RE 048/18 > Conferência dos Movimentos;

__5\.__ Realizar a Geração do Transferência entre Apurações, no Módulo Estadual > Ressarcimento ICMS\-ST RS \(IN\-RE 048/2018\), menu Geração > IN\-RE 048/18 > Transferência Entre Apurações;

__6\.__ Conferir os lançamentos realizados na Subapuração RS e na Apuração do ICMS\-ST, resultantes da geração da transferência, nos relatórios disponíveis no Módulo Estadual > Ressarcimento ICMS\-ST RS \(IN\-RE 048/2018\), menu Relatórios > IN\-RE 048/18 > Conferência dos Movimentos \(opção subapuração\) e Conferência da Transferência entre Apurações;

__7\.__ Realizar a Apuração do ICMS para o estabelecimento e período, disponível no módulo Estadual > ICMS, menu DATA MART > Apuração do ICMS > Ajuste SINIEF\. Nesta etapa, selecionar o parâmetro de tela “Substituição Tributária”\. Este procedimento é necessário para que os totais do Resumo da Substituição Tributária sejam recalculados considerando o lançamento criado pela Transferência entre Apurações;

__8\.__ Realizar a geração do SPED FISCAL, no módulo SPED > EFD – Escrituração Fiscal Digital, menu Geração > Meio Magnético\.

<a id="menu_janela"></a><a id="_Toc64492391"></a>

__Procedimentos para utilização do módulo para ATENDIMENTO A IN\-RE 087/2020__

__Pré\-requisitos__

__1\.__ O módulo de Ressarcimento de ICMS\-ST do Rio Grande do Sul utiliza as informações de tabelas fixas, acessórias e SAFX\. Para utilização de todas as suas funcionalidades, certifique\-se de tê\-las importado:

__<<<<SÓ NO MANUAL DO MASTERSAF devem ser mencionadas tabelas fixas e acessórias>>__

Módulo Ferramentas:

Menu: Tabelas Internas > Importar > Tabelas Fixas

Menu: Tabelas Internas > Importar > Tabelas Acessórias

• TFIX30 \- Parâmetros MasterSAF Módulos

• TFIX31 \- Parâmetros MasterSAF Nomenclatura

Módulo Job Servidor:

Menu: Carga > Programação e Execução e Importação > Programação e Execução\) ou

Importação Batch: menu Importação Batch > Programação e Execução

• SAFX07 \- Tabela de Documentos Fiscais

• SAFX08 \- Tabela de Itens de Documentos Fiscais de Mercadorias e Produtos

•SAFX192 – Tabela de Referências de Documentos Fiscais

•SAFX52 – Tabela de Inventário do Produto

• SAFX104 \- Parâmetros de Produto por UF \(Ressarcimento e Complemento de ICMS\-ST\)

• SAFX128 \- Fator de Conversão de Unidade de Medida por Produto

• SAFX2007 \- Tabela de Unidade de Medida

• SAFX2012 \- Tabela de Códigos Fiscais

• SAFX2013 \- Tabela de Produtos

• SAFX2043 \- Tabela de Classificação Fiscal

• SAFX2081 \- Tabela de Extensão de CFOP

__2\.__ Cadastrar os fatores de conversão de medida no módulo DW, menu Manutenção > Cadastros > Conversão de Unidades de Medida\. Estes fatores serão utilizados, quando necessário, para converter a quantidade dos movimentos para a unidade de medida de estoque do produto;

__3\.__ Cadastrar os Código de Motivo de Restituição/Complementação, no módulo Básicos > Data Warehouse, menu Manutenção > Cadastros > Códigos de Motivo de Restituição/Complementação de ICMS \(SPED FISCAL\) especificadas na tabela 5\.7 do Sped Fiscal;

__4\.__ Cadastrar a parametrização dos produtos a serem considerados na apuração do Ressarcimento de ICMS\-ST do Rio Grande do Sul de acordo com a Instrução Normativa 087/2020\. Esta parametrização pode ser feita por código de produto, por NCM ou por CEST, conforme as opções disponíveis no Módulo Estadual > Ressarcimento ICMS\-ST RS \(IN\-RE 048/2018\), menu Parâmetros > Produtos;

__5\.__ Cadastrar a parametrização das operações a serem consideradas na apuração do Ressarcimento de ICMS\-ST do Rio Grande do Sul de acordo com a Instrução Normativa 087/2020\. Trata\-se da movimentação de entradas, saídas internas para consumidor final e outros tipos de saídas\. Esta parametrização está disponível por CFOP e Natureza de Operação, conforme as opções disponíveis no Módulo Estadual > Ressarcimento ICMS\-ST RS \(IN\-RE 048/2018\), menu Parâmetros > IN\-RE 087/2020> Operações;

__6\.__ Criar perfil para geração dos registros C180, C181, C185, C186, 1250 e 1255, no módulo SPED > EFD – Escrituração Fiscal Digital, menu Parâmetros > Perfil\.

__Procedimentos a serem executados a cada período para ATENDIMENTO A IN\-RE 087/2020__

__1\.__ Importar os Documentos Fiscais \(SAFX07/SAFX08\) no módulo Job Servidor, via carga e importação de jobs \(menus Carga > Programação e Execução e Importação > Programação e Execução\) ou via importação Batch \(menu Importação Batch > Programação e Execução\);

__2\.__ Realizar a equalização do Datamart no módulo Ferramentas > Rotinas Acessórias > DATAMART > Equalização/Limpeza;

__3\.__ Realizar a Geração do Movimento, no Módulo Estadual > Ressarcimento ICMS\-ST RS \(IN\-RE 048/2018\), menu Geração > IN\-RE 087/2020> Geração dos Movimentos\.  Conferir o resultado da Geração do Movimento nos relatórios disponíveis na aba “Arquivo”;

__4\.__ Realizar a Geração do Transferência do Movimentos, no Módulo Estadual > Ressarcimento ICMS\-ST RS \(IN\-RE 048/2018\), menu Geração > IN\-RE 087/2020> Transferência dos Movimentos para a EFD Fiscal;

__5\.__ Realizar a geração do SPED FISCAL, no módulo SPED > EFD – Escrituração Fiscal Digital, menu Geração > Meio Magnético\.

__Menu Janela__

Vide manual de [Conceitos Iniciais](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/@Geral/Conceitos_Iniciais.htm#menu janela)\.

<a id="menu_ajuda"></a><a id="_Toc64492392"></a>__Menu Ajuda__

Vide manual de [Conceitos Iniciais](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/@Geral/Conceitos_Iniciais.htm#menu_ajuda)\.

<a id="atendimento"></a><a id="_Toc64492393"></a>__Atendimento Técnico MasterSAF__

Para dúvidas ou problemas, abra um chamado no Contact Center ou entre em contato com nossa equipe de Suporte Técnico MASTERSAF pelo Telefone:

\(11\) 2159\-0600 opção 1 \(Atendimento das Soluções Fiscais\)\.

Nosso horário de atendimento é de segunda à sexta\-feira de 9h às 18h\.

## <a id="_Toc354574234"></a><a id="_Toc354574409"></a><a id="_Toc354574453"></a><a id="_Toc354574538"></a><a id="_Toc354578084"></a><a id="_Toc354578311"></a><a id="_Toc354579002"></a><a id="_Toc354579143"></a><a id="_Toc23774815"></a><a id="_Toc64492394"></a>Outras informações que necessitarão ser atualizadas \(help, manual operacional etc\)

## <a id="_Toc426992014"></a><a id="_Toc428981618"></a><a id="_Toc23774816"></a><a id="_Toc64492395"></a>Informações p/ Carta do Patch

Direto no Jira

# <a id="_Toc200962062"></a><a id="_Toc200996464"></a><a id="_Toc200996582"></a><a id="_Toc200998062"></a><a id="_Toc354574235"></a><a id="_Toc354574410"></a><a id="_Toc354574454"></a><a id="_Toc354574539"></a><a id="_Toc354578085"></a><a id="_Toc354578312"></a><a id="_Toc354579003"></a><a id="_Toc354579144"></a><a id="_Toc64492396"></a>TESTES

= = = = =


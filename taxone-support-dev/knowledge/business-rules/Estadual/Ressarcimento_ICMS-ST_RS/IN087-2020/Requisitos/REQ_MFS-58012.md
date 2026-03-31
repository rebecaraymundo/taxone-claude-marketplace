# REQ_MFS-58012

- **Fonte:** REQ_MFS-58012.docx
- **Modificado:** 2021-02-10
- **Tamanho:** 281 KB

---

THOMSON REUTERS

<a id="_Hlk22664599"></a>__MFS\-58012__

__Módulo Estadual – Ressarcimento RS__

<a id="_Hlk53754126"></a>

Revisões

__Data__

__OS/Chamado__

__Descrição__

__Autor__

30/12/2020

MFS\-58012

IN087/2020

Liliane Assaf

Sumário

[1\.	INTRODUÇÃO	1](#_Toc60252972)

[1\.1	Documentos e Base Legal para a Solução	1](#_Toc60252973)

[2\.	Levantamentos junto a Área da Informação	1](#_Toc60252974)

[3\.	SOLUÇÃO FUNCIONAL / ESCOPO	1](#_Toc60252975)

[3\.1	Procedimentos para Fábrica	1](#_Toc60252976)

[3\.1\.1	– Alteração no Menu	1](#_Toc60252977)

[3\.1\.2	– Parametrização por CFOP	1](#_Toc60252978)

[3\.1\.3	– Parametrização por Natureza de Operação	1](#_Toc60252979)

[3\.1\.4	– Geração dos Movimentos	1](#_Toc60252980)

[3\.1\.5	– Limpeza das tabelas Específicas do Processo \(para estudo futuro\)	1](#_Toc60252981)

[3\.2	Procedimentos para Interface	1](#_Toc60252982)

[4\.	PROCEDIMENTOS PARA CONTEÚDO	1](#_Toc60252983)

[4\.1	Criação / Alteração – Tabelas \(Manual de Layout\)	1](#_Toc60252984)

[4\.2	Criação / Alteração em telas e relatórios \(manual operacional, roteiro e help\)	1](#_Toc60252985)

[4\.3	Criação / Alteração de Tabelas \(Fixas, Acessórias, Básicas\)	1](#_Toc60252986)

[4\.4	Criação / Alteração de Roteiro Operacional	1](#_Toc60252987)

[4\.5	Outras informações que necessitarão ser atualizadas \(help, manual operacional etc\)	1](#_Toc60252988)

[4\.6	Informações p/ Carta do Patch	1](#_Toc60252989)

[5\.	TESTES	1](#_Toc60252990)

# <a id="_Toc200962059"></a><a id="_Toc200996459"></a><a id="_Toc200996577"></a><a id="_Toc200998055"></a><a id="_Toc354574223"></a><a id="_Ref354574309"></a><a id="_Ref354574320"></a><a id="_Toc354574398"></a><a id="_Toc354574442"></a><a id="_Toc354574527"></a><a id="_Toc354578073"></a><a id="_Toc354578300"></a><a id="_Toc354578991"></a><a id="_Toc354579132"></a><a id="_Toc60252972"></a>INTRODUÇÃO

<a id="_Hlk53754794"></a>

## <a id="_Toc60252973"></a>Documentos e Base Legal para a Solução

__INSTRUÇÃO NORMATIVA RE Nº 087/20__

__INSTRUÇÃO NORMATIVA RE Nº 096/20__

# <a id="_Toc60252974"></a>Levantamentos junto a Área da Informação

<a id="_MON_1674464806"></a>![](data:image/x-emf;base64,AQAAAGwAAAABAAAAAQAAAGMAAAA7AAAAAAAAAAAAAAAtBwAApQQAACBFTUYAAAEAfBYAABUAAAACAAAAAAAAAAAAAAAAAAAAgAcAADgEAABYAQAAwgAAAAAAAAAAAAAAAAAAAMA/BQDQ9QIAGAAAAAwAAAAAAAAAGQAAAAwAAAD///8AcgAAAKAQAAAjAAAAAQAAAEIAAAAgAAAAIwAAAAEAAAAgAAAAIAAAAACA/wEAAAAAAAAAAAAAgD8AAAAAAAAAAAAAgD8AAAAAAAAAAP///wAAAAAAbAAAADQAAACgAAAAABAAACAAAAAgAAAAKAAAACAAAAAgAAAAAQAgAAMAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAA/wAA/wAA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABaW12ydHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/WltdsgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAARiEIYL1aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/476l//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAvVoY/71aGP+9Whj/vVoY//v18f//////0o5g/71aGP+9Whj/0o5g///////79fH/vVoY/71aGP+9Whj/vVoY//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/71aGP/FbzX////////////it5r/vVoY/71aGP/it5r////////////FbzX/vVoY/71aGP+9Whj/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/vVoY/9KOYP////////////fr4/+9Whj/vVoY//fr4////////////9KOYP+9Whj/vVoY/71aGP/6+vr/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAvVoY/71aGP+9Whj/3q2M/////////////////8l5Q//FbzX///////v18f//////3q2M/71aGP+9Whj/vVoY//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/71aGP/rzLf//////+K3mv//////3q2M/9qiff//////68y3///////rzLf/vVoY/71aGP+9Whj/+vr6/9N8K//TfCv/03wr/9N8K//TfCv/03wr/9N8K//6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/vVoY//fr4///////wWQm///////z4dT/68y3///////FbzX///////fr4/+9Whj/vVoY/71aGP/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAvVoY/71aGP/BZCb///////v18f+9Whj/68y3////////////9+vj/71aGP/z4dT//////8FkJv+9Whj/vVoY//r6+v/upUH/7qVB/+6lQf/upUH/7qVB/+6lQf/upUH/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/86DUv//////79bG/71aGP/aon3////////////it5r/vVoY/+bCqf//////zoNS/71aGP+9Whj/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/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)

 

# <a id="Premissas"></a><a id="_Toc200962060"></a><a id="_Toc200996460"></a><a id="_Toc200996578"></a><a id="_Toc200998056"></a><a id="_Toc354574225"></a><a id="_Toc354574400"></a><a id="_Toc354574444"></a><a id="_Toc354574529"></a><a id="_Toc354578075"></a><a id="_Toc354578302"></a><a id="_Toc354578993"></a><a id="_Toc354579134"></a><a id="_Toc60252975"></a>SOLUÇÃO FUNCIONAL / ESCOPO

As SAFX requeridas para a geração dos registros são:

1. Devolução de Saída: 

Utilizar a SAFX08 utilizando os campos de referência\. 

Utilizar a SAFX192\.

1. Devolução de Entrada: 

Utilizar a SAFX08 utilizando os campos de referência\.

1. Cupom Fiscal:

SAFX993/994 

SAFX201/2020

1. Devolução de Saída por Cupom referenciado

SAFX117\.

 

__Documentos__

__Tabelas \(Capa/Itens\)__

Notas Fiscais \(modelos 01, 1B, 04, 55, 65\) 

SAFX07 / SAFX08

Cupons Fiscais \(modelos 02, 2D, 2E e 60\)

SAFX993 / SAFX994

Cupons Fiscais \(modelo 59\-CFe SAT\)

SAFX201 / SAFX202

O Módulo Ressarcimento terá duas novas funicionalidades:

1\) Parametrizações de CFOP e Natureza Op\. com revisão do menu\.

2\) Geração do Movimento:

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

__ __

## <a id="_Toc200962061"></a><a id="_Toc200996461"></a><a id="_Toc200996579"></a><a id="_Toc200998057"></a><a id="_Toc354574226"></a><a id="_Toc354574401"></a><a id="_Toc354574445"></a><a id="_Toc354574530"></a><a id="_Toc354578076"></a><a id="_Toc354578303"></a><a id="_Toc354578994"></a><a id="_Toc354579135"></a><a id="_Toc60252976"></a>Procedimentos para Fábrica

### <a id="_Toc60252977"></a>– Alteração no Menu

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

### <a id="_Toc60252978"></a>– Parametrização por CFOP

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> \(IN\-RE 087/20\) >> Operações >> CFOP

__Descrição:__

Criar tela de parametrização do CFOP para demonstrar as operações:

771 \- Entrada \(e Devoluções\)

770 \- Saída Interna à Consumidor Final \(e Devoluções\)

Can vai confirmar as demais operações, que não serão consideradas nesse momento:

\- Venda interna a consumidor final: RICMS, Livro III, art\. __25\-A e art  25\-B__;

\- Saída com CFOP 5\.927 \(baixa de estoque decorrente a perda, roubo, ou deteriorioração\)

\- Fato gerador presumido não realizado: RICMS, Livro III, __art\. 22\.__

\- Operações definidas no RICMS, Livro III, __art\. 23__ \(saídas para outras ufs?\)\.

\- Operações definidas no RICMS, Livro III, __art\. 24 __\(saídas para outras uf?\) e __24\-A__ \(saídas isentas?\)\.

### <a id="_Toc60252979"></a>– Parametrização por Natureza de Operação

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> <a id="_Hlk59893211"></a>\(IN\-RE 087/20\) >> Operações >> CFOP

__Descrição:__

Criar tela de parametrização do CFOP para demonstrar as operações:

771 \- Entrada \(e Devoluções\)

770 \- Saída Interna à Consumidor Final \(e Devoluções\)

### <a id="_Toc60252980"></a>– Geração dos Movimentos

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

MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Cálculo Média Ponderada\.docx

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

### <a id="_Toc60252981"></a>– Limpeza das tabelas Específicas do Processo \(para estudo futuro\)

__Localização__: 

__Menu__: 

__Descrição:__

EST\_ST\_RS\_NF\_SAI, EST\_ST\_RS\_NF\_ENT, EST\_ST\_RS\_NF\_DEV\_SAI, EST\_ST\_RS\_NF\_DEV\_ENT

## <a id="_Toc354574228"></a><a id="_Toc354574403"></a><a id="_Toc354574447"></a><a id="_Toc354574532"></a><a id="_Toc354578078"></a><a id="_Toc354578305"></a><a id="_Toc354578996"></a><a id="_Toc354579137"></a><a id="_Toc60252982"></a>Procedimentos para Interface

<a id="_Toc200962071"></a><a id="_Toc200996470"></a><a id="_Toc200996588"></a><a id="_Toc200998068"></a>

# <a id="_Toc354574229"></a><a id="_Toc354574404"></a><a id="_Toc354574448"></a><a id="_Toc354574533"></a><a id="_Toc354578079"></a><a id="_Toc354578306"></a><a id="_Toc354578997"></a><a id="_Toc354579138"></a><a id="_Toc60252983"></a>PROCEDIMENTOS PARA CONTEÚDO

<a id="_Toc199304378"></a><a id="_Toc200962072"></a><a id="_Toc200996471"></a><a id="_Toc200996589"></a><a id="_Toc200998069"></a>

## <a id="_Toc354574230"></a><a id="_Toc354574405"></a><a id="_Toc354574449"></a><a id="_Toc354574534"></a><a id="_Toc354578080"></a><a id="_Toc354578307"></a><a id="_Toc354578998"></a><a id="_Toc354579139"></a><a id="_Toc60252984"></a>Criação / Alteração – Tabelas \(Manual de Layout\)

## <a id="_Toc200996472"></a><a id="_Toc200996590"></a><a id="_Toc200998070"></a><a id="_Toc354574231"></a><a id="_Toc354574406"></a><a id="_Toc354574450"></a><a id="_Toc354574535"></a><a id="_Toc354578081"></a><a id="_Toc354578308"></a><a id="_Toc354578999"></a><a id="_Toc354579140"></a><a id="_Toc60252985"></a>Criação / Alteração em telas e relatórios \(manual operacional, roteiro e help\)

<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a><a id="OLE_LINK7"></a>

## <a id="_Toc23774813"></a><a id="_Toc60252986"></a>Criação / Alteração de Tabelas \(Fixas, Acessórias, Básicas\)

## <a id="_Toc354574233"></a><a id="_Toc354574408"></a><a id="_Toc354574452"></a><a id="_Toc354574537"></a><a id="_Toc354578083"></a><a id="_Toc354578310"></a><a id="_Toc354579001"></a><a id="_Toc354579142"></a><a id="_Toc23774814"></a><a id="_Toc60252987"></a>Criação / Alteração de Roteiro Operacional

## <a id="_Toc354574234"></a><a id="_Toc354574409"></a><a id="_Toc354574453"></a><a id="_Toc354574538"></a><a id="_Toc354578084"></a><a id="_Toc354578311"></a><a id="_Toc354579002"></a><a id="_Toc354579143"></a><a id="_Toc23774815"></a><a id="_Toc60252988"></a>Outras informações que necessitarão ser atualizadas \(help, manual operacional etc\)

## <a id="_Toc426992014"></a><a id="_Toc428981618"></a><a id="_Toc23774816"></a><a id="_Toc60252989"></a>Informações p/ Carta do Patch

Direto no Jira

# <a id="_Toc200962062"></a><a id="_Toc200996464"></a><a id="_Toc200996582"></a><a id="_Toc200998062"></a><a id="_Toc354574235"></a><a id="_Toc354574410"></a><a id="_Toc354574454"></a><a id="_Toc354574539"></a><a id="_Toc354578085"></a><a id="_Toc354578312"></a><a id="_Toc354579003"></a><a id="_Toc354579144"></a><a id="_Toc60252990"></a>TESTES

= = = = =


# REQ_MFS-58013

- **Fonte:** REQ_MFS-58013.docx
- **Modificado:** 2021-02-10
- **Tamanho:** 278 KB

---

THOMSON REUTERS

<a id="_Hlk22664599"></a>__MFS\-58013__

__Módulo Estadual – Ressarcimento RS__

<a id="_Hlk53754126"></a>

Revisões

__Data__

__OS/Chamado__

__Descrição__

__Autor__

20/01/2021

MFS\-58013

IN087/2020

Liliane Assaf

Sumário

[1\.	INTRODUÇÃO	1](#_Toc62224282)

[1\.1	Documentos e Base Legal para a Solução	1](#_Toc62224283)

[2\.	Levantamentos junto a Área da Informação	1](#_Toc62224284)

[3\.	SOLUÇÃO FUNCIONAL / ESCOPO	1](#_Toc62224285)

[3\.1	Procedimentos para Fábrica	1](#_Toc62224286)

[3\.1\.1	– Geração do Meio Magnético – Sped Fiscal	1](#_Toc62224287)

[3\.1\.2	– Alteração no Menu	1](#_Toc62224288)

[3\.1\.3	– Geração dos Movimentos	1](#_Toc62224289)

[3\.1\.4	– Transferência dos Movimentos para EFD FISCAL	1](#_Toc62224290)

[3\.2	Procedimentos para Interface	1](#_Toc62224291)

[4\.	PROCEDIMENTOS PARA CONTEÚDO	1](#_Toc62224292)

[4\.1	Criação / Alteração – Tabelas \(Manual de Layout\)	1](#_Toc62224293)

[4\.2	Criação / Alteração em telas e relatórios \(manual operacional, roteiro e help\)	1](#_Toc62224294)

[4\.3	Criação / Alteração de Tabelas \(Fixas, Acessórias, Básicas\)	1](#_Toc62224295)

[4\.4	Criação / Alteração de Roteiro Operacional	1](#_Toc62224296)

[4\.5	Outras informações que necessitarão ser atualizadas \(help, manual operacional etc\)	1](#_Toc62224297)

[4\.6	Informações p/ Carta do Patch	1](#_Toc62224298)

[5\.	TESTES	1](#_Toc62224299)

# <a id="_Toc200962059"></a><a id="_Toc200996459"></a><a id="_Toc200996577"></a><a id="_Toc200998055"></a><a id="_Toc354574223"></a><a id="_Ref354574309"></a><a id="_Ref354574320"></a><a id="_Toc354574398"></a><a id="_Toc354574442"></a><a id="_Toc354574527"></a><a id="_Toc354578073"></a><a id="_Toc354578300"></a><a id="_Toc354578991"></a><a id="_Toc354579132"></a><a id="_Toc62224282"></a>INTRODUÇÃO

<a id="_Hlk53754794"></a>

## <a id="_Toc62224283"></a>Documentos e Base Legal para a Solução

__INSTRUÇÃO NORMATIVA RE Nº 087/20__

__INSTRUÇÃO NORMATIVA RE Nº 096/20__

# <a id="_Toc62224284"></a>Levantamentos junto a Área da Informação

<a id="_MON_1674464939"></a>![](data:image/x-emf;base64,AQAAAGwAAAABAAAAAQAAAGMAAAA7AAAAAAAAAAAAAAAtBwAApQQAACBFTUYAAAEAfBYAABUAAAACAAAAAAAAAAAAAAAAAAAAgAcAADgEAABYAQAAwgAAAAAAAAAAAAAAAAAAAMA/BQDQ9QIAGAAAAAwAAAAAAAAAGQAAAAwAAAD///8AcgAAAKAQAAAjAAAAAQAAAEIAAAAgAAAAIwAAAAEAAAAgAAAAIAAAAACA/wEAAAAAAAAAAAAAgD8AAAAAAAAAAAAAgD8AAAAAAAAAAP///wAAAAAAbAAAADQAAACgAAAAABAAACAAAAAgAAAAKAAAACAAAAAgAAAAAQAgAAMAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAA/wAA/wAA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABaW12ydHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/WltdsgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAARiEIYL1aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/476l//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAvVoY/71aGP+9Whj/vVoY//v18f//////0o5g/71aGP+9Whj/0o5g///////79fH/vVoY/71aGP+9Whj/vVoY//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/71aGP/FbzX////////////it5r/vVoY/71aGP/it5r////////////FbzX/vVoY/71aGP+9Whj/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/vVoY/9KOYP////////////fr4/+9Whj/vVoY//fr4////////////9KOYP+9Whj/vVoY/71aGP/6+vr/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAvVoY/71aGP+9Whj/3q2M/////////////////8l5Q//FbzX///////v18f//////3q2M/71aGP+9Whj/vVoY//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/71aGP/rzLf//////+K3mv//////3q2M/9qiff//////68y3///////rzLf/vVoY/71aGP+9Whj/+vr6/9N8K//TfCv/03wr/9N8K//TfCv/03wr/9N8K//6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/vVoY//fr4///////wWQm///////z4dT/68y3///////FbzX///////fr4/+9Whj/vVoY/71aGP/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAvVoY/71aGP/BZCb///////v18f+9Whj/68y3////////////9+vj/71aGP/z4dT//////8FkJv+9Whj/vVoY//r6+v/upUH/7qVB/+6lQf/upUH/7qVB/+6lQf/upUH/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/86DUv//////79bG/71aGP/aon3////////////it5r/vVoY/+bCqf//////zoNS/71aGP+9Whj/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/3q2M///////erYz/vVoY/8VvNf///////////9KOYP+9Whj/2qJ9///////erYz/vVoY/71aGP/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAvVoY/71aGP/mwqn//////9KOYP+9Whj/vVoY//fr4///////wWQm/71aGP/Og1L//////+bCqf+9Whj/vVoY//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAARiEIYL1aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/476l//r6+v/6+vr/+vr6/6aoqf90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5//r6+v/6+vr/+vr6//r6+v/Iycn/dHd5/yssLWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/+vr6//r6+v/6+vr/yMnJ/3R3ef8rLC1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef/6+vr/+vr6/8jJyf90d3n/KywtYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5//r6+v/Iycn/dHd5/yssLWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/yMnJ/3R3ef8rLC1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef90d3n/KywtYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWltdsnR3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/yssLWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAADAAAAAAAAAISAAAADAAAAAEAAABSAAAAcAEAAAEAAAAQAAAAAAAAAAAAAAAAAAAAvAIAAAAAAAABAgIiUwB5AHMAdABlAG0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAJQIAAM7IX536fwAAAAAAAAAAAACqHgEeAAAAACAAAAAAAAAACyRlnfp/AACPIwT//////3ALAAABBAEAwA3J2yUCAACPIwT//////3ALAAABBAEAwA3J2yUCAACPIwT//////3ALAAABBAEAwA3J2yUCAACL6AGdAAAAAACA/wEAAAAAjyMBBAAAAAAAAAAAAAAAAAAAAAAAAAAAqh4BHgAAAADNLBmf+n8AAKAAAAAAAAAAjyMBBAAAAADQUlxkiwAAAO1kszT6fwAAAAAAAAAAAACL6AGd+n8AAKBTXGSLAAAAyVJcZIsAAAABAAAAAAAAAKBTXGRkdgAIAAAAACUAAAAMAAAAAQAAACUAAAAMAAAADQAAgCgAAAAMAAAAAQAAAFIAAABwAQAAAQAAAPX///8AAAAAAAAAAAAAAACQAQAAAAAAAABAACJTAGUAZwBvAGUAIABVAEkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOivXGSLAAAA8ZV0n/p/AAAAAAAAAAAAAHDfUMwlAgAA2AtQzCUCAAAAAAAAAAAAAAAA3c8lAgAAUA2QNfp/AAAwAtfPJQIAAB8BAAAAAAAAAADdzyUCAACQnN3PJQIAAAAAAAAAAAAABwAAAAAAAAAAAK6/JQIAAFDL3M8AAAAAuFJFzCUCAAAABqa/JQIAAAAAAAAAAAAACAAAAAAAAAC4UkXMJQIAAEAAAAAAAAAAAAAAAAAAAADA8/IgAAAAAADT3c8lAgAAIV10n/p/AABAAAAAAAAAAIvoAZ36fwAA0K9cZIsAAAA5rlxkiwAAACAAAAAAAAAA0K9cZGR2AAgAAAAAJQAAAAwAAAABAAAAVAAAAKwAAAAGAAAAIgAAAGEAAAAuAAAAAQAAAFVVj0EmtI9BBgAAACIAAAAQAAAATAAAAAQAAAAAAAAAAAAAAGYAAABCAAAAbAAAAFIARQBRAF8ATQBGAFMALQA0ADgANwA1ADMAIAAtACAABwAAAAYAAAAIAAAABQAAAAoAAAAGAAAABgAAAAQAAAAGAAAABgAAAAYAAAAGAAAABgAAAAMAAAAEAAAAAwAAAFQAAAC0AAAAAQAAAC8AAABjAAAAOwAAAAEAAABVVY9BJrSPQQEAAAAvAAAAEQAAAEwAAAAEAAAAAAAAAAAAAABmAAAAQgAAAHAAAABMAGUAdgBhAG4AdABhAG0AZQBuAHQAbwAuAGQAbwBjAHgAAAAFAAAABgAAAAUAAAAGAAAABwAAAAQAAAAGAAAACQAAAAYAAAAHAAAABAAAAAcAAAADAAAABwAAAAcAAAAFAAAABQAAACUAAAAMAAAADQAAgEYAAAAgAAAAEgAAAEkAYwBvAG4ATwBuAGwAeQAAAAAARgAAAFAAAABEAAAAUgBFAFEAXwBNAEYAUwAtADQAOAA3ADUAMwAgAC0AIABMAGUAdgBhAG4AdABhAG0AZQBuAHQAbwAuAGQAbwBjAHgAAABGAAAAEAAAAAIAAAAAAAAARgAAABAAAAAEAAAAZQAAAEYAAAAgAAAAEgAAAEkAYwBvAG4ATwBuAGwAeQAAAAAADgAAABQAAAAAAAAAEAAAABQAAAA=)

 

# <a id="Premissas"></a><a id="_Toc200962060"></a><a id="_Toc200996460"></a><a id="_Toc200996578"></a><a id="_Toc200998056"></a><a id="_Toc354574225"></a><a id="_Toc354574400"></a><a id="_Toc354574444"></a><a id="_Toc354574529"></a><a id="_Toc354578075"></a><a id="_Toc354578302"></a><a id="_Toc354578993"></a><a id="_Toc354579134"></a><a id="_Toc62224285"></a>SOLUÇÃO FUNCIONAL / ESCOPO

1\) No Módulo Sped Fiscal – alteração na funcionalidade de Geração do Meio Magnético:

   \- Geração do registro 0200: Aliquota interna parametrizada no módulo Ressarcimento RS deve ser gerada no registro 0200 \- campo 12\.

2\) No módulo Ressarcimento ICMS\-ST – RS \-  criação da funcionalidade Transferência dos Movimentos para EFD Fiscal:

   \- Incluir críticas sobre registros importados pela SAFX296, SAFX308, SAFX304;

   \- Atualizar o Inventário do Último dia do Mês Anterior p/ H030 do Sped Fiscal;

   \- Atualizar Tabelas SAFX p/ gerar os registros C180, C181, C185, C186, C380, C480 do Sped Fiscal

   \- Gerar os Registro de Saldo Ressarcimento e Complemento \(1255\)

   \- Gerar Relatório de Conferência do Registro de Saldo Ressarcimento e Complemento \(1255\)

   \- Gerar Relatório de Resumo Registros Gerados

 3\) No módulo Ressarcimento ICMS\-ST – RS \-  alteração na funicionalidade de Geração dos Movimentos:

   \- Retirar criticas sobre registros importados importados pela SAFX296, SAFX308\. Essas críticas foram migradas para a funcionalidade Transferência dos Movimentos para EFD Fiscal\.

## <a id="_Toc200962061"></a><a id="_Toc200996461"></a><a id="_Toc200996579"></a><a id="_Toc200998057"></a><a id="_Toc354574226"></a><a id="_Toc354574401"></a><a id="_Toc354574445"></a><a id="_Toc354574530"></a><a id="_Toc354578076"></a><a id="_Toc354578303"></a><a id="_Toc354578994"></a><a id="_Toc354579135"></a><a id="_Toc62224286"></a>Procedimentos para Fábrica

### <a id="_Toc62224287"></a>– Geração do Meio Magnético – Sped Fiscal

__Localização__: Módulo Sped  >> EFD \- Escrituração Fiscal Digital

__Menu__: Geração >> Meio Magnético 

__Descrição:__

Alteração na regra de geração do registro 0200 – campo Alíquota Interna\.

Ver documento:

Sped\_Fiscal\_Regras\_Bloco\_0\.docx

### <a id="_Toc62224288"></a>– Alteração no Menu

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Descrição__: 

Alterar o menu para incluir o item “Transferência dos Movimentos para EFD Fiscal”\.

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

### <a id="_Toc62224289"></a>– Geração dos Movimentos

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Geração >> \(IN\-RE 087/20\) >> Geração dos Movimentos

 

__Descrição:__

Retirar as críticas abaixo, pois foram migradas para a funcionalidade de Transferência dos Movimentos para EFD Fiscal:

__Existência de Movimento de Entradas e Saídas importados pela SAFX296__

Caso exista Movimento de Entradas e Saídas importados pela SAFX296, para o estabelecimento e período informados na tela de geração, exibir a seguinte mensagem no log:

“*Existem dados importados através da SAFX296 – Informações Complementares das Operações Sujeitas ao ST \(C180, C185 e C380\) para o estabelecimento e período informados\. Nesta rotina os movimentos de entradas e saídas a serem apresentados nos registros C180, C185 e C380 são gerados na tabela definitiva da SAFX296\. Como pré\-requisito não pode existir movimentos oriundos da Importação da SAFX296\. Favor realize a limpeza dessa tabela no módulo Ferramentas, opção Exclusão de Tabelas Definitivas\.”	*

__Existência de Movimento de Devoluções de Entradas e Saídas importados pela SAFX308__

Caso exista Movimento de Devoluções de Entradas e Saídas importados pela SAFX308, para o estabelecimento e período informados na tela de geração, exibir a seguinte mensagem no log:

“*Existem dados importados através da SAFX308 – Informações Complementares das Operações de Devolução Sujeitas ao ST \(C181 e C186\) para o estabelecimento e período informados\. Nesta rotina os movimentos de devoluções a serem apresentados nos registros C181 e C186 são gerados na tabela definitiva da SAFX308\. Como pré\-requisito não pode existir movimentos oriundos da Importação da SAFX308\. Favor realize a limpeza dessa tabela no módulo Ferramentas, opção Exclusão de Tabelas Definitivas\.”*

Ver documento:

MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\.docx

### <a id="_Toc62224290"></a>– Transferência dos Movimentos para EFD FISCAL

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Geração >> \(IN\-RE 087/20\) >> Transferência dos Movimentos para EFD Fiscal

 

__Descrição:__

Criação da funcionalidade\.

Ver documentos:

MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_EFD Fiscal\.docx 

MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_Inventário\_H030\.docx

MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_Saldo Ressarcimento Complemento\_1255\.docx

MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_Tabelas SAFX\_C180\_C181\_C185\_C186\_C380\_C480

## <a id="_Toc354574228"></a><a id="_Toc354574403"></a><a id="_Toc354574447"></a><a id="_Toc354574532"></a><a id="_Toc354578078"></a><a id="_Toc354578305"></a><a id="_Toc354578996"></a><a id="_Toc354579137"></a><a id="_Toc62224291"></a>Procedimentos para Interface

<a id="_Toc200962071"></a><a id="_Toc200996470"></a><a id="_Toc200996588"></a><a id="_Toc200998068"></a>

# <a id="_Toc354574229"></a><a id="_Toc354574404"></a><a id="_Toc354574448"></a><a id="_Toc354574533"></a><a id="_Toc354578079"></a><a id="_Toc354578306"></a><a id="_Toc354578997"></a><a id="_Toc354579138"></a><a id="_Toc62224292"></a>PROCEDIMENTOS PARA CONTEÚDO

<a id="_Toc199304378"></a><a id="_Toc200962072"></a><a id="_Toc200996471"></a><a id="_Toc200996589"></a><a id="_Toc200998069"></a>

## <a id="_Toc354574230"></a><a id="_Toc354574405"></a><a id="_Toc354574449"></a><a id="_Toc354574534"></a><a id="_Toc354578080"></a><a id="_Toc354578307"></a><a id="_Toc354578998"></a><a id="_Toc354579139"></a><a id="_Toc62224293"></a>Criação / Alteração – Tabelas \(Manual de Layout\)

## <a id="_Toc200996472"></a><a id="_Toc200996590"></a><a id="_Toc200998070"></a><a id="_Toc354574231"></a><a id="_Toc354574406"></a><a id="_Toc354574450"></a><a id="_Toc354574535"></a><a id="_Toc354578081"></a><a id="_Toc354578308"></a><a id="_Toc354578999"></a><a id="_Toc354579140"></a><a id="_Toc62224294"></a>Criação / Alteração em telas e relatórios \(manual operacional, roteiro e help\)

<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a><a id="OLE_LINK7"></a>

## <a id="_Toc23774813"></a><a id="_Toc62224295"></a>Criação / Alteração de Tabelas \(Fixas, Acessórias, Básicas\)

## <a id="_Toc354574233"></a><a id="_Toc354574408"></a><a id="_Toc354574452"></a><a id="_Toc354574537"></a><a id="_Toc354578083"></a><a id="_Toc354578310"></a><a id="_Toc354579001"></a><a id="_Toc354579142"></a><a id="_Toc23774814"></a><a id="_Toc62224296"></a>Criação / Alteração de Roteiro Operacional

## <a id="_Toc354574234"></a><a id="_Toc354574409"></a><a id="_Toc354574453"></a><a id="_Toc354574538"></a><a id="_Toc354578084"></a><a id="_Toc354578311"></a><a id="_Toc354579002"></a><a id="_Toc354579143"></a><a id="_Toc23774815"></a><a id="_Toc62224297"></a>Outras informações que necessitarão ser atualizadas \(help, manual operacional etc\)

## <a id="_Toc426992014"></a><a id="_Toc428981618"></a><a id="_Toc23774816"></a><a id="_Toc62224298"></a>Informações p/ Carta do Patch

Direto no Jira

# <a id="_Toc200962062"></a><a id="_Toc200996464"></a><a id="_Toc200996582"></a><a id="_Toc200998062"></a><a id="_Toc354574235"></a><a id="_Toc354574410"></a><a id="_Toc354574454"></a><a id="_Toc354574539"></a><a id="_Toc354578085"></a><a id="_Toc354578312"></a><a id="_Toc354579003"></a><a id="_Toc354579144"></a><a id="_Toc62224299"></a>TESTES

= = = = =


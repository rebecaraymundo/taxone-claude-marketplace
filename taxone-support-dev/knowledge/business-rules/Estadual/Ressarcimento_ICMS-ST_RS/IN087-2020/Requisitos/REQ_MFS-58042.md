# REQ_MFS-58042

- **Fonte:** REQ_MFS-58042.docx
- **Modificado:** 2021-03-09
- **Tamanho:** 318 KB

---

THOMSON REUTERS

<a id="_Hlk22664599"></a>__MFS\-58042__

__Módulo Estadual – Ressarcimento RS – 2ª Entrega__

<a id="_Hlk53754126"></a>

Revisões

__Data__

__OS/Chamado__

__Descrição__

__Autor__

22/01/2021

MFS\-58042

IN087/2020

Liliane Assaf

Sumário

[1\.	INTRODUÇÃO	1](#_Toc65088954)

[1\.1	Documentos e Base Legal para a Solução	1](#_Toc65088955)

[2\.	Levantamentos junto a Área da Informação	1](#_Toc65088956)

[3\.	SOLUÇÃO FUNCIONAL / ESCOPO	1](#_Toc65088957)

[3\.1	Procedimentos para Fábrica	1](#_Toc65088958)

[3\.1\.1	– Parametrização por CFOP	1](#_Toc65088959)

[3\.1\.2	– Parametrização por Natureza de Operação	1](#_Toc65088960)

[3\.1\.3	– Geração dos Movimentos	1](#_Toc65088961)

[3\.1\.4	– Geração do Meio Magnético – Sped Fiscal	1](#_Toc65088962)

[3\.2	Procedimentos para Interface	1](#_Toc65088963)

[4\.	PROCEDIMENTOS PARA CONTEÚDO	1](#_Toc65088964)

[4\.1	Criação / Alteração – Tabelas \(Manual de Layout\)	1](#_Toc65088965)

[4\.2	Criação / Alteração em telas e relatórios \(manual operacional, roteiro e help\)	1](#_Toc65088966)

[4\.3	Criação / Alteração de Tabelas \(Fixas, Acessórias, Básicas\)	1](#_Toc65088967)

[4\.4	Criação / Alteração de Roteiro Operacional	1](#_Toc65088968)

[4\.5	Outras informações que necessitarão ser atualizadas \(help, manual operacional etc\)	1](#_Toc65088969)

[4\.6	Informações p/ Carta do Patch	1](#_Toc65088970)

[5\.	TESTES	1](#_Toc65088971)

# <a id="_Toc200962059"></a><a id="_Toc200996459"></a><a id="_Toc200996577"></a><a id="_Toc200998055"></a><a id="_Toc354574223"></a><a id="_Ref354574309"></a><a id="_Ref354574320"></a><a id="_Toc354574398"></a><a id="_Toc354574442"></a><a id="_Toc354574527"></a><a id="_Toc354578073"></a><a id="_Toc354578300"></a><a id="_Toc354578991"></a><a id="_Toc354579132"></a><a id="_Toc65088954"></a>INTRODUÇÃO

<a id="_Hlk53754794"></a>

## <a id="_Toc65088955"></a>Documentos e Base Legal para a Solução

__INSTRUÇÃO NORMATIVA RE Nº 087/20__

__INSTRUÇÃO NORMATIVA RE Nº 096/20__

# <a id="_Toc65088956"></a>Levantamentos junto a Área da Informação

<a id="_MON_1676136110"></a>![](data:image/x-emf;base64,AQAAAGwAAAABAAAAAQAAAGMAAAA7AAAAAAAAAAAAAAAtBwAApQQAACBFTUYAAAEAfBYAABUAAAACAAAAAAAAAAAAAAAAAAAAgAcAADgEAABYAQAAwgAAAAAAAAAAAAAAAAAAAMA/BQDQ9QIAGAAAAAwAAAAAAAAAGQAAAAwAAAD///8AcgAAAKAQAAAjAAAAAQAAAEIAAAAgAAAAIwAAAAEAAAAgAAAAIAAAAACA/wEAAAAAAAAAAAAAgD8AAAAAAAAAAAAAgD8AAAAAAAAAAP///wAAAAAAbAAAADQAAACgAAAAABAAACAAAAAgAAAAKAAAACAAAAAgAAAAAQAgAAMAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAA/wAA/wAA/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABaW12ydHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/dHd5/3R3ef90d3n/WltdsgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHR3ef/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdHd5//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0d3n/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAARiEIYL1aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/476l//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY/71aGP/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAvVoY/71aGP+9Whj/vVoY//v18f//////0o5g/71aGP+9Whj/0o5g///////79fH/vVoY/71aGP+9Whj/vVoY//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/71aGP/FbzX////////////it5r/vVoY/71aGP/it5r////////////FbzX/vVoY/71aGP+9Whj/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/vVoY/9KOYP////////////fr4/+9Whj/vVoY//fr4////////////9KOYP+9Whj/vVoY/71aGP/6+vr/vVoY/71aGP+9Whj/vVoY/71aGP+9Whj/vVoY//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAvVoY/71aGP+9Whj/3q2M/////////////////8l5Q//FbzX///////v18f//////3q2M/71aGP+9Whj/vVoY//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/71aGP/rzLf//////+K3mv//////3q2M/9qiff//////68y3///////rzLf/vVoY/71aGP+9Whj/+vr6/9N8K//TfCv/03wr/9N8K//TfCv/03wr/9N8K//6+vr/+vr6/3R3ef8AAAAAAAAAAAAAAAAAAAAAAAAAAL1aGP+9Whj/vVoY//fr4///////wWQm///////z4dT/68y3///////FbzX///////fr4/+9Whj/vVoY/71aGP/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/dHd5/wAAAAAAAAAAAAAAAAAAAAAAAAAAvVoY/71aGP/BZCb///////v18f+9Whj/68y3////////////9+vj/71aGP/z4dT//////8FkJv+9Whj/vVoY//r6+v/upUH/7qVB/+6lQf/upUH/7qVB/+6lQf/upUH/+vr6//r6+v90d3n/AAAAAAAAAAAAAAAAAAAAAAAAAAC9Whj/vVoY/86DUv//////79bG/71aGP/aon3////////////it5r/vVoY/+bCqf//////zoNS/71aGP+9Whj/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/+vr6//r6+v/6+vr/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)

 

# <a id="Premissas"></a><a id="_Toc200962060"></a><a id="_Toc200996460"></a><a id="_Toc200996578"></a><a id="_Toc200998056"></a><a id="_Toc354574225"></a><a id="_Toc354574400"></a><a id="_Toc354574444"></a><a id="_Toc354574529"></a><a id="_Toc354578075"></a><a id="_Toc354578302"></a><a id="_Toc354578993"></a><a id="_Toc354579134"></a><a id="_Toc65088957"></a>SOLUÇÃO FUNCIONAL / ESCOPO

__Escopo da 2a Entrega  \(sprint 270\)__

- Item 19\.3\-A\.1\.9, da IN 096/20

Operações do escopo da 2a  entrega:

- 778 \- Saída para Outra UF \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)
- 780 \- Devolução para fornecedor de outra UF, quando a retenção inicial foi realizada pelo próprio remetente da devolução, nos moldes do RICMS, Livro III, art\. 53\-A \(RICMS, Livro III, art\. 25\)
- 781\- Saída para Exportação \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)
- 782 \- Saída Interna com nova ST \(RICMS, Livro III, art\.23, III\) \(e Devoluções\)
- 783 \- Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.23, V\) \(e Devoluções\)

MFS da entrega: [MFS\-58042](https://jira.thomsonreuters.com/browse/MFS-58042)

 

__Escopo da 3a Entrega \(sprint 271\)__

- Fato Gerador Não Realizado item \(item 19\.3\-A\.1\.7, da IN 096/20\)
- Situação de emissão de Nota Fiscal para estabelecimento que realizou retenção \(item 19\.3\-A\.1\.10, da IN 096/20\)
- Situação de operação de saída de mercadoria a destinatário do RS que não seja consumidor final \(item 19\.3\-A\.1\.13, da IN 096/20\)

Operações do escopo da 3a entrega:

- 772\- Furto ou Roubo \- baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)
- 773 \- Perda, extravio ou Deterioração – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)
- 774 \- Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)
- 775 \- Furto ou Roubo \- baixa sem Ressarcimento
- 776 \- Perda, extravio ou Deterioração – baixa sem Ressarcimento
- 777 \- Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa sem Ressarcimento
- 779 \- Saída para Outra UF \(RICMS, Livro III, art\.24\) \(e Devoluções\)
- 784 \- Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.24\-A\) \(e Devoluções\)
- 785 \- Saída com ST não destinada a consumidor final deste Estado, ao abrigo de exclusão de responsabilidade \(RICMS, Livro III, art\. 11\) \(e Devoluções\)

MFS da entrega: [MFS\-59698](https://jira.thomsonreuters.com/browse/MFS-59698)

## <a id="_Toc200962061"></a><a id="_Toc200996461"></a><a id="_Toc200996579"></a><a id="_Toc200998057"></a><a id="_Toc354574226"></a><a id="_Toc354574401"></a><a id="_Toc354574445"></a><a id="_Toc354574530"></a><a id="_Toc354578076"></a><a id="_Toc354578303"></a><a id="_Toc354578994"></a><a id="_Toc354579135"></a><a id="_Toc65088958"></a>Procedimentos para Fábrica

### <a id="_Toc60252978"></a><a id="_Toc65088959"></a>– Parametrização por CFOP

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> \(IN\-RE 087/20\) >> Operações >> CFOP

__Descrição:__

Incluir as operações marcadas em verde:

Cód

Descrição

770

Saída Interna à Consumidor Final \(e Devoluções\)

771

Entrada \(e Devoluções\)

772

Furto ou Roubo \- baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

773

Perda, extravio ou Deterioração – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

774

Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

775

Furto ou Roubo \- baixa sem Ressarcimento 

776

Perda, extravio ou Deterioração – baixa sem Ressarcimento 

777

Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa sem Ressarcimento 

778

Saída para Outra UF \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)

779

Saída para Outra UF \(RICMS, Livro III, art\.24\) \(e Devoluções\)

780

Devolução para fornecedor de outra UF, quando a retenção inicial foi realizada pelo próprio remetente da devolução, nos moldes do RICMS, Livro III, art\. 53\-A \(RICMS, Livro III, art\. 25\)

781

Saída para Exportação \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)

782

Saída Interna com nova ST \(RICMS, Livro III, art\.23, III\) \(e Devoluções\)

783

Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.23, V\) \(e Devoluções\)

784

Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.24\-A\) \(e Devoluções\)

785

Saída com ST não destinada a consumidor final deste Estado, ao abrigo de exclusão de responsabilidade \(RICMS, Livro III, art\. 11\) \(e Devoluções\)

Obs: Os códigos de operação do 772 ao 777 só devem considerar CFOP’s de Saída \(iniciados por 5, 6 e 7\)\. Os demais códigos devem compreender CFOP’s de Entrada \(iniciados por 1, 2 e 3\) e Saída \(iniciados por 5, 6 e 7\)\.

Ver documento matriz: __MTZ\-Ressarc\-RS\-IN087\_2020\_Parametrizacao\_CFOPs\.docx__

### <a id="_Toc60252979"></a><a id="_Toc65088960"></a>– Parametrização por Natureza de Operação

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> <a id="_Hlk59893211"></a>\(IN\-RE 087/20\) >> Operações >> Natureza de Operação

__Descrição:__

Incluir as operações marcadas em verde:

Cód

Descrição

770

Saída Interna à Consumidor Final \(e Devoluções\)

771

Entrada \(e Devoluções\)

772

Furto ou Roubo \- baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

773

Perda, extravio ou Deterioração – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

774

Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

775

Furto ou Roubo \- baixa sem Ressarcimento 

776

Perda, extravio ou Deterioração – baixa sem Ressarcimento 

777

Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa sem Ressarcimento 

778

Saída para Outra UF \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)

779

Saída para Outra UF \(RICMS, Livro III, art\.24\) \(e Devoluções\)

780

Devolução para fornecedor de outra UF, quando a retenção inicial foi realizada pelo próprio remetente da devolução, nos moldes do RICMS, Livro III, art\. 53\-A \(RICMS, Livro III, art\. 25\)

781

Saída para Exportação \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)

782

Saída Interna com nova ST \(RICMS, Livro III, art\.23, III\) \(e Devoluções\)

783

Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.23, V\) \(e Devoluções\)

784

Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.24\-A\) \(e Devoluções\)

785

Saída com ST não destinada a consumidor final deste Estado, ao abrigo de exclusão de responsabilidade \(RICMS, Livro III, art\. 11\) \(e Devoluções\)

Obs: Os códigos de operação do 772 ao 777 só devem considerar CFOP’s de Saída \(iniciados por 5, 6 e 7\)\. Os demais códigos devem compreender CFOP’s de Entrada \(iniciados por 1, 2 e 3\) e Saída \(iniciados por 5, 6 e 7\)\.

Ver documento matriz: __MTZ\-Ressarc\-RS\-IN087\_2020\_Parametrizacao\_Natureza\.docx__

### <a id="_Toc60252980"></a><a id="_Toc65088961"></a>– Geração dos Movimentos

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Geração >> \(IN\-RE 087/20\) >> Geração dos Movimentos

 

__Descrição:__

Alterar a geração dos movimentos de Saída e Devolução de Saídas para contemplar as novas operações, aplicando os tratamentos definidos pela IN\-RE 096/20\. As novas operações estão marcadas em verde\.

Acrescentar críticas contemplanado os novos códigos de motivo\.  Quando existir parametrização por CFOP e/ou Natureza de Operação, o código de motivo correspondente a operação parametrizada, deve ser cadastrado\. Caso o cadastro não tenha sido realizado, apresentar mensagem de log e abortar o processo de geração do movimento\. Ver “__MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\.docx__”\.

Cód Operação

Descrição da Operação \(*menu Parâmetros 🡪 \(IN\-RE 087/20\) 🡪 Operações\)*

Cód Motivo

Base Legal 

 IN 096/20

770

Saída Interna para Consumidor Final \(e Devoluções\)

RS100, RS300, RS600, RS800

19\.3\-A\.1\.12 

771

Entrada \(e Devoluções\)

RS400

19\.3\-A\.1\.11 

772

Furto ou Roubo \- baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

RS211

19\.3\-A\.1\.7 

773

Perda, extravio ou Deterioração – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

RS212

19\.3\-A\.1\.7

774

Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

RS215

19\.3\-A\.1\.7

775

Furto ou Roubo \- baixa sem Ressarcimento 

RS011

19\.3\-A\.1\.7

776

Perda, extravio ou Deterioração – baixa sem Ressarcimento 

RS012

19\.3\-A\.1\.7

777

Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa sem Ressarcimento 

RS015

19\.3\-A\.1\.7

778

Saída para Outra UF \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)

RS213, RS713

19\.3\-A\.1\.9 

779

Saída para Outra UF \(RICMS, Livro III, art\.24\) \(e Devoluções\)

RS001, RS501

19\.3\-A\.1\.10 

780

Devolução para fornecedor de outra UF, quando a retenção inicial foi realizada pelo próprio remetente da devolução, nos moldes do RICMS, Livro III, art\. 53\-A \(RICMS, Livro III, art\. 25\)

RS213, RS713

19\.3\-A\.1\.9 

781

Saída para Exportação \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)

RS214, RS714

19\.3\-A\.1\.9 

782

Saída Interna com nova ST \(RICMS, Livro III, art\.23, III\) \(e Devoluções\)

RS217, RS717

19\.3\-A\.1\.9 

783

Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.23, V\) \(e Devoluções\)

RS219, RS719

19\.3\-A\.1\.9 

784

Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.24\-A\) \(e Devoluções\)

RS001, RS501

19\.3\-A\.1\.10 

785

Saída com ST não destinada a consumidor final deste Estado, ao abrigo de exclusão de responsabilidade \(RICMS, Livro III, art\. 11\) \(e Devoluções\)

RS000, RS500

19\.3\-A\.1\.13 

Esboço dos tratamentos realizados nos registros C185, C181 para as novas operações da 2ª e 3ª entregas:

3ª ENTREGA

3ª ENTREGA

1ª ENTREGA

2ª ENTREGA

3ª ENTREGA

3ª ENTREGA

__\(Layout C185\)__

__19\.3\-A\.1\.7__

__\(com ressarcimento\)  
RS211, RS212, RS215__

__772, 773, 774__

__19\.3\-A\.1\.7__

__\(sem ressarcimento\) __

__RS011, RS012, RS015__

__775, 776, 777__

Ressarc MG – Fato gerador presumido não realizado \(MG200\)

__19\.3\-A\.1\.12__

__Consumidor Final__

__770__

__19\.3\-A\.1\.9 – __

__Livro III, art\. 23, I, III e V __

__RS213, RS214, RS217, RS219__

__778, 780, 781, 782, 783__

__19\.3\-A\.1\.10__

__RS001__

779, 784

__19\.3\-A\.1\.13__

__RS000__

785

__10\-VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV __

0

0

0

Valor saidas

0

0

0

__11\-VL\_UNIT\_ICMS\_OP\_CONV __

__12\-VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV__

0

0

0

0

__0__

__0__

__12\-VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV __

12

0

12

12

0

0

__13\-VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV__

13

0

13

13

0

0

__15\-VL\_UNIT\_ICMS\_ST\_CONV\_REST__

12 \+ 13 \- 11

0

12 \+ 13 \- 10

12 \+ 13 \- 10

12 \+ 13

0

0

__16 \-VL\_UNIT\_FCP\_ST\_CONV\_REST__

\(12 \+ 13 \- 11\) \* Aliq FCP

0

\(12 \+ 13 \- 10\) \* Aliq FCP

\(12 \+ 13 \- 10\) \* Aliq FCP

\(12 \+ 13\)\* Aliq FCP

0

0

__17\-VL\_UNIT\_ICMS\_ST\_CONV\_COMPL__

0

0

0

10 \- 12 \- 13

0

0

0

__18\-VL\_UNIT\_FCP\_ST\_CONV\_COMPL__

0

0

0

\(10 \- 12 \- 13\) \* Aliq FCP

0

0

0

2ª ENTREGA

3ª ENTREGA

3ª ENTREGA

__\(Layout C181\)__

__19\.3\-A\.1\.9 – __

__Livro III, art\. 23, I, III e V RS713, RS714, RS717, RS719__

__778, 780, 781, 782, 783__

__19\.3\-A\.1\.10__

__RS501__

779, 784

__19\.3\-A\.1\.13__

__RS500__

785

__16\-VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV\_SAÍDA__

0

0

0

__17\-VL\_UNIT\_ICMS\_OP\_CONV\_SAIDA__

0

__0__

__0__

__13\-VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV\_SAIDA__

13

0

0

__14\-VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV\_SAÍDA__

14

0

0

__18\-VL\_UNIT\_ICMS\_ST\_CONV\_REST__

0

0

0

__19 \- VL\_UNIT\_FCP\_ST\_CONV\_REST__

0

0

0

__20 \- VL\_UNIT\_ICMS\_ST\_CONV\_COMPL__

13 \+ 14

0

0

__21 \- VL\_UNIT\_FCP\_ST\_CONV\_COMPL__

\(13 \+ 14\) \* Aliq FCP

0

0

Ver documentos matrizes:

__MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\.docx__

__MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Saidas\.docx__

__MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Devolução de Saidas\.docx__

### <a id="_Toc62224287"></a><a id="_Toc64492365"></a><a id="_Toc65088962"></a>– Geração do Meio Magnético – Sped Fiscal

__Localização__: Módulo Sped  >> EFD \- Escrituração Fiscal Digital

__Menu__: Geração >> Meio Magnético 

__Descrição:__

Alteração na regra de geração dos registros C181, C185\.

Ver documento matriz:

__Sped\_Fiscal\_Regras\_Bloco\_C\.docx__

## <a id="_Toc354574228"></a><a id="_Toc354574403"></a><a id="_Toc354574447"></a><a id="_Toc354574532"></a><a id="_Toc354578078"></a><a id="_Toc354578305"></a><a id="_Toc354578996"></a><a id="_Toc354579137"></a><a id="_Toc65088963"></a>Procedimentos para Interface

<a id="_Toc200962071"></a><a id="_Toc200996470"></a><a id="_Toc200996588"></a><a id="_Toc200998068"></a>

# <a id="_Toc354574229"></a><a id="_Toc354574404"></a><a id="_Toc354574448"></a><a id="_Toc354574533"></a><a id="_Toc354578079"></a><a id="_Toc354578306"></a><a id="_Toc354578997"></a><a id="_Toc354579138"></a><a id="_Toc65088964"></a>PROCEDIMENTOS PARA CONTEÚDO

<a id="_Toc199304378"></a><a id="_Toc200962072"></a><a id="_Toc200996471"></a><a id="_Toc200996589"></a><a id="_Toc200998069"></a>

## <a id="_Toc354574230"></a><a id="_Toc354574405"></a><a id="_Toc354574449"></a><a id="_Toc354574534"></a><a id="_Toc354578080"></a><a id="_Toc354578307"></a><a id="_Toc354578998"></a><a id="_Toc354579139"></a><a id="_Toc65088965"></a>Criação / Alteração – Tabelas \(Manual de Layout\)

## <a id="_Toc200996472"></a><a id="_Toc200996590"></a><a id="_Toc200998070"></a><a id="_Toc354574231"></a><a id="_Toc354574406"></a><a id="_Toc354574450"></a><a id="_Toc354574535"></a><a id="_Toc354578081"></a><a id="_Toc354578308"></a><a id="_Toc354578999"></a><a id="_Toc354579140"></a><a id="_Toc65088966"></a>Criação / Alteração em telas e relatórios \(manual operacional, roteiro e help\)

<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a><a id="OLE_LINK7"></a>

### – Parametrização por CFOP

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> \(IN\-RE 087/20\) >> Operações >> CFOP

__Descrição:__

Incluir as operações marcadas em verde:

Blá blá blá blá

__Operação:__ Selecione a operação, conforme cadastro importado através da tabela TFIX31, para a qual os CFOP’s são associados:

\- Saída Interna para Consumidor Final \(e Devoluções\)

\- Entrada \(e Devoluções\)

\- Furto ou Roubo \- baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

\- Perda, extravio ou Deterioração – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

\- Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

Entre outras\.

Blá blá blá blá

### – Parametrização por Natureza de Operação

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Parâmetros >> \(IN\-RE 087/20\) >> Operações >> Natureza de Operação

__Descrição:__

Incluir as operações marcadas em verde:

Blá blá blá blá

__Operação:__ Selecione a operação, conforme cadastro importado através da tabela TFIX31, para a qual os CFOP’s são associados:

\- Saída Interna para Consumidor Final \(e Devoluções\)

\- Entrada \(e Devoluções\)

\- Furto ou Roubo \- baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

\- Perda, extravio ou Deterioração – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

\- Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

Entre outras\.

Blá blá blá blá

### – Geração dos Movimentos

__Localização__: Módulo Estadual >> Ressarcimento ICMS\-ST – RS \(IN\-RE 048/18\)

__Menu__: Geração >> \(IN\-RE 087/20\) >> Geração dos Movimentos

 

__Descrição:__

Incluir os trechos marcados em verde:

 

__Blá blá blá __

__Blá blá blá __

__Blá blá blá __

__Relatório de Conferência do C185__

• Campos de Identificação da Nota Fiscal:

\- Do 1º ao 11º campo: \(Cod Empresa, Cod Estab, Dt Fiscal, E/S, Norm/Dev, Cod Docto, Ind Fis/Jur Cod Fis/Jur, Num Docfis , Serie, SubSerie, Num Item\);

• Campos do Layout do C185:

\- Qtde Conv \(C185\-07\): Quantidade \(campo 24 da SAFX08\) do item documento Fiscal, quando a unidade de medida do item é igual a do Cadastro do Produto \(SAFX2013 – campo 14\)\.

Caso a medida do item do documento Fiscal seja diferente da medida no cadastro do produto, esse campo demonstra o resultado da multiplicação do campo Quantidade \(campo 24 da SAFX08\) pelo Fator de Conversão \(veja tópico [Cadastro de Conversão de Unidades de Medidas](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/Estadual/Ressarcimento_de_ICMS_ST_RS/oper_safufrcrs.htm#cadastro_unidade_medidas)\), ou apresenta a Quantidade já Convertida carregada no campo 137 da SAFX08\.

\- Medida \(C185\-08\): Unidade de Medida do Cadastro do Produto \(SAFX2013 – campo 14\)\.

\- Vlr Unit Conv \(C185\-09\): Valor unitário da mercadoria calculado considerando: \[Valor Contábil do Item \(campo 64 da SAFX08\)\] dividido pela Quantidade Convertida;

\- Vlr Unit ICMS Operação Conv \(C185\-10\): Para saídas internas a consumidor final, o Valor unitário do ICMS é calculado considerando: \[Vlr Unit BC ICMS Operação Conv\] multiplicado pela Alíquota Interna dividido por 100;

Onde:

Vlr Unit BC ICMS Operação Conv é calculado considerando o %Redução BC parametrizado para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\):

Para produto sem %Redução BC: Vlr Unit BC ICMS Operação Conv = \[Valor Contábil do Item \(campo 64 da SAFX08\)\] dividido pela Quantidade Convertida;

Para produto com %Redução BC: Vlr Unit BC ICMS Operação Conv = \[\(Valor Contábil do Item – \(Valor Contábil do Item \* “%Redução BC” / 100\)\)\] dividido pela Quantidade Convertida;

O Vlr Unit BC ICMS Operação Conv é demonstrado nesse relatório no campo “Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\)”\.

Alíquota Interna: Alíquota parametrizada para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\)\.

Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico [Regra de Preenchimento C185 por Operação](#c185);

\- Cod Motivo \(C185\-06\): Para saídas internas a consumidor final com ressarcimento, esse campo é preenchido com “RS100”\. Quando houver complementação, esse campo é preenchido com “RS300”\. 

Para saber se houve ressarcimento ou complemento, é realizada a comparação entre os valores unitários da Entrada e da Saída, através dos campos:

- Valor Médio Unitário Base de Cálculo do ICMS\-ST: Valor unitário da entrada, obtido pelo Cálculo da Média Ponderada Móvel\. Ver campo “Valor Médio Unitário Base de Cálculo do ICMS\-ST” do Relatório de Conferência do Cálculo da Média Ponderada\. Esse valor é demonstrado nesse relatório no campo “Vlr Unit BC ICMS\-ST \(Recuperado da Média Ponderada\)”\.
- Vlr Unit BC ICMS Operação Conv: Valor unitário da saída, que é demonstrado nesse relatório no campo “Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\)”\.

Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico [Regra de Preenchimento C185 por Operação](#c185);

\- Vlr Unit ICMS Op Conv \(C185\-11\): Para saídas internas a consumidor final, esse campo não é preenchido\.  Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico [Regra de Preenchimento C185 por Operação](#c185);

\- Vlr Unit ICMS Estoque Conv \(C185\-12\): Para saídas internas a consumidor final, o Valor Médio Unitário ICMS é obtido do Cálculo da Média Ponderada Móvel, para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada\. Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico [Regra de Preenchimento C185 por Operação](#c185);

\- Vlr Unit ICMS\-ST Estoque Conv \(C185\-13\): Para saídas internas a consumidor final, soma\-se os campos Valor Médio Unitário ICMS\-ST e Valor Médio Unitário FECEP\-ST obtidos do Cálculo da Média Ponderada Móvel, para o dia e produto da saída\. Esses campos são demonstrados no Relatório de Conferência do Cálculo da Média Ponderada\.  Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico [Regra de Preenchimento C185 por Operação](#c185);

\- Vlr Unit FCP\-ST Estoque Conv \(C185\-14\): Para saídas internas a consumidor final, o Valor Médio Unitário FECEP\-ST é obtido do Cálculo da Média Ponderada Móvel, para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada\.  Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico [Regra de Preenchimento C185 por Operação](#c185);

\- Vlr Unit ICMS\-ST Conv Rest \(C185\-15\): Para saídas internas a consumidor final, valor do ressarcimento calculado com base nos campos Vlr Unit ICMS Operação Conv \(C185\-10\), Vlr Unit ICMS Op Conv \(C185\-11\), Vlr Unit ICMS Estoque Conv \(C185\-12\), Vlr Unit ICMS\-ST Estoque Conv \(C185\-13\)\.  Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico [Regra de Preenchimento C185 por Operação](#c185);

\- Vlr Unit FCP\-ST Conv Rest \(C185\-16\): Para saídas internas a consumidor final, valor do ressarcimento calculado com base no campo Vlr Unit ICMS\-ST Conv Rest \(C185\-15\) aplicando a Aliquota FECEP parametrizada para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\)\. Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico [Regra de Preenchimento C185 por Operação](#c185);

\- Vlr Unit ICMS\-ST Conv Compl \(C185\-17\): Para saídas internas a consumidor final, valor do complemento calculado com base nos campos Vlr Unit ICMS Operação Conv \(C185\-10\), Vlr Unit ICMS Op Conv \(C185\-11\), Vlr Unit ICMS Estoque Conv \(C185\-12\), Vlr Unit ICMS\-ST Estoque Conv \(C185\-13\)\.  Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico [Regra de Preenchimento C185 por Operação](#c185);

\- Vlr Unit FCP\-ST Conv Compl \(C185\-18\): Para saídas internas a consumidor final, valor do complemento calculado com base no campo Vlr Unit ICMS\-ST Conv Compl \(C185\-17\) aplicando a Aliquota FECEP parametrizada para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\)\. Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico [Regra de Preenchimento C185 por Operação](#c185);

• Campos Auxiliares origem Cadastro do Produto \(SAFX2013\):

\- Ind Produto \(SAFX2013\-01\) Cod Produto \(SAFX2013\-02\),

\- Medida Produto \(SAFX2013\-14\),

\- NCM Produto \(SAFX2013\-05\),

\- CEST Produto \(SAFX2013\-54\)

Para consultar o cadastro do produto \(SAFX2013\) acessar o módulo Básicos no menu: Data Warehouse > Manutenção > Códigos > Produto\.

• Campos Auxiliares origem Parametrização do Produto:

\- %Redução BC \(Parametrização Produto\)

\- Alíq\. Interna \(Parametrização Produto\)

\- Alíq\. FCP \(Parametrização Produto\)

Para consulta acesse o menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\.

• Campos Auxiliares origem Documento Fiscal \(SAFX08\):

\- Qtde Item \(SAFX08\-24\)

\- Qtde Conv Item \(SAFX08\-137\)

\- Medida Item \(SAFX08\-25\)

\- Fator Conv \(Cadastro Conversão Medida\): Fator de Conversão cadastrado no módulo Básicos no menu: Data Warehouse > Manutenção > Cadastros > Conversão de Unidades de Medida, opções Padrão ou Por Produto

\- Vlr Contábil Item \(SAFX08\-64\)

\- Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\): calculado considerando o %Redução BC parametrizado para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\)\.

Para produto sem %Redução BC: Vlr Unit BC ICMS Operação Conv = \[Valor Contábil do Item \(campo 64 da SAFX08\)\] dividido pela Quantidade Convertida;

Para produto com %Redução BC: Vlr Unit BC ICMS Operação Conv = \[\(Valor Contábil do Item – \(Valor Contábil do Item \* “%Redução BC” / 100\)\)\] dividido pela Quantidade Convertida\.

• Campos Auxiliares Recuperados da Média Ponderada:

\- Vlr Unit ICMS \(Recuperado da Média Ponderada\): Valor Médio Unitário ICMS obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit ICMS\-ST \(s/ FECEP\-ST\) \(Recuperado da Média Ponderada\): Valor Médio Unitário ICMS\-ST obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit BC ICMS\-ST \(Recuperado da Média Ponderada\): Valor Médio Unitário Base de Cálculo do ICMS\-ST obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit FECEP\-ST \(Recuperado da Média Ponderada\): Valor Médio Unitário FECEP\-ST obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada\.

<a id="c185"></a>__Regra de Preenchimento C185 por Operação__

Base Legal 

 IN 096/20

Cód

Operação \(menu Parâmetros 🡪 \(IN\-RE 087/20\) 🡪 Operações\)

Cod Motivo \(C185\-06\)

Vlr Unit ICMS

Operação Conv 

\(C185\-10\)

Vlr Unit ICMS Op Conv \(C185\-11\)

Vlr Unit ICMS Estoque Conv \(C185\-12\)

Vlr Unit ICMS\-ST Estoque Conv \(C185\-13\)

Vlr Unit FCP\-ST Estoque Conv \(C185\-14\)

Vlr Unit ICMS\-ST Conv Rest \(C185\-15\)

Vlr Unit FCP\-ST Conv Rest \(C185\-16\)

Vlr Unit ICMS\-ST Conv Compl \(C185\-17\)

Vlr Unit FCP\-ST Conv Compl \(C185\-18\)

19\.3\-A\.1\.12 

770

Saída Interna para Consumidor Final \(e Devoluções\)

RS100, RS300

Calculado c/ Valor Contábil do Item

= zero

Média

Pond\.

Média

Pond\.

Média

Pond\.

= \(C185\-12\) \+ \(C185\-13\)

\- \(C185\-10\)

= \(C185\-15\) x Alíq FCP

= \(C185\-10\) \- \(C185\-12\)  

\- \(C185\-13\)

= \(C185\-17\) 

x Alíq FCP

19\.3\-A\.1\.7 

772

Furto ou Roubo \- baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

RS211

= zero

= \(C185\-12\)

Média

Pond\.

Média

Pond\.

Média

Pond\.

= \(C185\-12\) \+ \(C185\-13\)

\- \(C185\-11\)

= \(C185\-15\) x Alíq FCP

= zero

= zero

19\.3\-A\.1\.7

773

Perda, extravio ou Deterioração – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

RS212

= zero

= \(C185\-12\)

Média

Pond\.

Média

Pond\.

Média

Pond\.

= \(C185\-12\) \+ \(C185\-13\)

\- \(C185\-11\)

= \(C185\-15\) x Alíq FCP

= zero

= zero

19\.3\-A\.1\.7

774

Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)

RS215

= zero

= \(C185\-12\)

Média

Pond\.

Média

Pond\.

Média

Pond\.

= \(C185\-12\) \+ \(C185\-13\)

\- \(C185\-11\)

= \(C185\-15\) x Alíq FCP

= zero

= zero

19\.3\-A\.1\.7

775

Furto ou Roubo \- baixa sem Ressarcimento 

RS011

= zero

= zero

= zero

= zero

= zero

= zero

= zero

= zero

= zero

19\.3\-A\.1\.7

776

Perda, extravio ou Deterioração – baixa sem Ressarcimento 

RS012

= zero

= zero

= zero

= zero

= zero

= zero

= zero

= zero

= zero

19\.3\-A\.1\.7

777

Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa sem Ressarcimento 

RS015

= zero

= zero

= zero

= zero

= zero

= zero

= zero

= zero

= zero

19\.3\-A\.1\.9 

778

Saída para Outra UF \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)

RS213

= zero

= zero

Média

Pond\.

Média

Pond\.

Média

Pond\.

= \(C185\-12\) \+ \(C185\-13\)

= \(C185\-15\) x Alíq FCP

= zero

= zero

19\.3\-A\.1\.10 

779

Saída para Outra UF \(RICMS, Livro III, art\.24\) \(e Devoluções\)

RS001

= zero

= zero

= zero

= zero

= zero

= zero

= zero

= zero

= zero

19\.3\-A\.1\.9 

780

Devolução para fornecedor de outra UF, quando a retenção inicial foi realizada pelo próprio remetente da devolução, nos moldes do RICMS, Livro III, art\. 53\-A \(RICMS, Livro III, art\. 25\)

RS213

= zero

= zero

Média

Pond\.

Média

Pond\.

Média

Pond\.

= \(C185\-12\) \+ \(C185\-13\)

= \(C185\-15\) x Alíq FCP

= zero

= zero

19\.3\-A\.1\.9 

781

Saída para Exportação \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)

RS214

= zero

= zero

Média

Pond\.

Média

Pond\.

Média

Pond\.

= \(C185\-12\) \+ \(C185\-13\)

= \(C185\-15\) x Alíq FCP

= zero

= zero

19\.3\-A\.1\.9 

782

Saída Interna com nova ST \(RICMS, Livro III, art\.23, III\) \(e Devoluções\)

RS217

= zero

= zero

Média

Pond\.

Média

Pond\.

Média

Pond\.

= \(C185\-12\) \+ \(C185\-13\)

= \(C185\-15\) x Alíq FCP

= zero

= zero

19\.3\-A\.1\.9 

783

Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.23, V\) \(e Devoluções\)

RS219

= zero

= zero

Média

Pond\.

Média

Pond\.

Média

Pond\.

= \(C185\-12\) \+ \(C185\-13\)

= \(C185\-15\) x Alíq FCP

= zero

= zero

19\.3\-A\.1\.10 

784

Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.24\-A\) \(e Devoluções\)

RS001

= zero

= zero

= zero

= zero

= zero

= zero

= zero

= zero

= zero

19\.3\-A\.1\.13 

785

Saída com ST não destinada a consumidor final deste Estado, ao abrigo de exclusão de responsabilidade \(RICMS, Livro III, art\. 11\) \(e Devoluções\)

RS000

= zero

= zero

= zero

= zero

= zero

= zero

= zero

= zero

= zero

__Relatório de Conferência do C380__

__Blá blá blá __

__Blá blá blá __

__Blá blá blá __

__Relatório de Conferência do C181__

• Campos de Identificação da Nota Fiscal de Devolução:

\- Do 1º ao 11º campo: identificação da nota Fiscal de devolução com o número do item de mercadoria \(Cod Empresa, Cod Estab, Dt Fiscal NF Devolução, E/S NF Devolução, Norm/Dev NF Devolução, Cod Docto NF Devolução, Ind Fis/Jur NF Devolução Cod Fis/Jur NF Devolução, Num Docfis NF Devolução, Serie NF Devolução, SubSerie NF Devolução, Num Item NF Devolução\);

• Campos do Layout do C181:

\- Num Docfis NF Saída \(C181\-08\), Serie NF Saída \(C181\-06\), Dt Fiscal NF Saída \(C181\-10\), Num Item NF Saída \(C181\-11\): campos de identificação da nota de Saída;

\- Cod Motivo \(C181\-02\): Para saídas internas a consumidor final objeto de devolução com ressarcimento \(“RS100”\), esse campo é preenchido com “RS600” – Estorno do Ressarcimento\-ST\.

Para saídas internas a consumidor final objeto de devolução com complemento \(“RS300”\), esse campo é preenchido com “RS600” – Estorno do Complemento\-ST\.

Para saber se houve ressarcimento ou complemento, é realizada a comparação entre os valores unitários da Entrada e da Saída, através dos campos:

- Valor Médio Unitário Base de Cálculo do ICMS\-ST: Valor unitário da entrada, obtido pelo Cálculo da Média Ponderada Móvel, para o dia e produto da saída objeto da devolução\. Ver campo “Valor Médio Unitário Base de Cálculo do ICMS\-ST” do Relatório de Conferência do Cálculo da Média Ponderada\. Para saídas de períodos anteriores à nova sistemática da IN087/20, o valor é calculado a partir da última nota de recebimento do produto anterior à data da saída\. Esse valor é demonstrado nesse relatório no campo “Vlr Unit BC ICMS\-ST \(p/ Cálculo da Média Ponderada\)”
- Vlr Unit BC ICMS Operação Conv: Valor unitário da saída, calculado considerando o %Redução BC parametrizado para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\):

Para produto sem %Redução BC: Vlr Unit BC ICMS Operação Conv = \[Valor Contábil do Item da Saída \(campo 64 da SAFX08\)\] dividido pela Quantidade Convertida da Saída;

Para produto com %Redução BC: Vlr Unit BC ICMS Operação Conv = \[\(Valor Contábil do Item da Saída – \(Valor Contábil do Item da Saída \* “%Redução BC” / 100\)\)\] dividido pela Quantidade Convertida da Saída;

O Vlr Unit BC ICMS Operação Conv é demonstrado nesse relatório no campo “Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\)”\.

Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico “[Regra de Preenchimento C181 por Operação](#C181)”;

\- Qtde Conv \(C181\-03\): Quantidade \(campo 24 da SAFX08\) do item documento Fiscal de devolução, quando a unidade de medida do item é igual a do Cadastro do Produto \(SAFX2013 – campo 14\)\.

Caso a medida do item do documento Fiscal de devolução seja diferente da medida no cadastro do produto, esse campo demonstra o resultado da multiplicação do campo Quantidade \(campo 24 da SAFX08\) pelo Fator de Conversão \(veja tópico [Cadastro de Conversão de Unidades de Medidas](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/Estadual/Ressarcimento_de_ICMS_ST_RS/oper_safufrcrs.htm#cadastro_unidade_medidas)\), ou apresenta a Quantidade já Convertida carregada no campo 137 da SAFX08\.

\- Medida \(C181\-04\): Unidade de Medida do Cadastro do Produto \(SAFX2013 – campo 14\);

\- Vlr Unit Conv \(C181\-12\): Valor unitário da mercadoria calculado com base na saída objeto da devolução, considerando: \[Valor Contábil do Item da Saída \(campo 64 da SAFX08\)\] dividido pela Quantidade Convertida da Saída;

\- Vlr Unit ICMS Op Conv \(C181\-17\): Para saídas internas a consumidor final objeto de devolução, esse campo não é preenchido; Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico “[Regra de Preenchimento C181 por Operação](#C181)”;

\- Vlr Unit ICMS Estoque Conv \(C181\-13\): Para saídas internas a consumidor final objeto de devolução, considera\-se o Valor Médio Unitário ICMS obtido do Cálculo da Média Ponderada Móvel, para o dia e produto da saída objeto da devolução\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada; para saídas de períodos anteriores à nova sistemática da IN087/20, o valor é calculado a partir da última nota de recebimento do produto anterior à data da saída;  

Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico “[Regra de Preenchimento C181 por Operação](#C181)”;

\- Vlr Unit ICMS\-ST Estoque Conv \(C181\-14\): Para saídas internas a consumidor final objeto de devolução, são considerados Valor Médio Unitário ICMS\-ST \+ Valor Médio Unitário FECEP\-ST obtidos do Cálculo da Média Ponderada Móvel, para o dia e produto da saída objeto da devolução\. Esses campos são demonstrados no Relatório de Conferência do Cálculo da Média Ponderada\. 

Para saídas de períodos anteriores à nova sistemática da IN087/20, o valor é calculado a partir da última nota de recebimento do produto anterior a data da saída, considerando: \[Valor do ICMS\-ST \(campo 52, ou 145 ou 133 ou 107 da SAFX08\) somado FECEP\-ST \(campo 140 da SAFX08\)\] dividido pela Quantidade Convertida\.

__ATENÇÃO:__ Quanto ao Valor do ICMS\-ST destacado na nota, o campo 52 \- Valor ICMS Substituição Tributária pode ser carregado via SAFX08 com o FECEP\-ST embutido ou não\. Por isso, quando o FECEP __não__ estiver embutido no valor do ICMS\-ST, marcar a opção “Realizar a soma dos valores FECP ao ICMS/ICMS\-ST” na equalização DATA MART e __não__ marcar a opção “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” na Geração do Movimento\.

Caso contrário, o FECEP\-ST será considerado dobrado\. Para maiores esclarecimentos veja o tópico [Sobre Procedimento para Equalização DATA MART versus FECEP embutido no ICMS, ICMS\-ST](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/Estadual/Ressarcimento_de_ICMS_ST_RS/oper_safufrcrs.htm#procedimento_datamart_FECEP)\.

Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico “[Regra de Preenchimento C181 por Operação](#C181)”;

\- Vlr Unit FCP\-ST Estoque Conv \(C181\-15\): Para saídas internas a consumidor final objeto de devolução, considera\-se o Valor Médio Unitário FECEP\-ST obtido do Cálculo da Média Ponderada Móvel, para o dia e produto da saída objeto da devolução\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada; para saídas de períodos anteriores à nova sistemática da IN087/20, o valor é calculado a partir da última nota de recebimento do produto anterior a data da saída;

Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico “[Regra de Preenchimento C181 por Operação](#C181)”;

\- Vlr Unit ICMS Operação Conv \(C181\-16\): Para saídas internas a consumidor final objeto de devolução, Valor unitário do ICMS calculado com base na saída objeto da devolução, considerando: \[Vlr Unit BC ICMS Operação Conv\] multiplicado pela Alíquota Interna dividido por 100;

Onde:

Vlr Unit BC ICMS Operação Conv é calculado considerando o %Redução BC parametrizado para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\):

Para produto sem %Redução BC: Vlr Unit BC ICMS Operação Conv = \[Valor Contábil do Item da Saída \(campo 64 da SAFX08\)\] dividido pela Quantidade Convertida da Saída;

Para produto com %Redução BC: Vlr Unit BC ICMS Operação Conv = \[\(Valor Contábil do Item da Saída – \(Valor Contábil do Item da Saída \* “%Redução BC” / 100\)\)\] dividido pela Quantidade Convertida da Saída;

O Vlr Unit BC ICMS Operação Conv é demonstrado nesse relatório no campo “Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\)”\.

Alíquota Interna: Alíquota parametrizada para o produto vigente em relação da data da emissão da nota de saída \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\)\.

Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico “[Regra de Preenchimento C181 por Operação](#C181)”;

\- Vlr Unit ICMS\-ST Conv Rest \(C181\-18\): Para saídas internas a consumidor final objeto de devolução, valor referente ao estorno de complemento calculado com base nos campos Vlr Unit ICMS Operação Conv \(C181\-16\), Vlr Unit ICMS Estoque Conv \(C181\-13\), Vlr Unit ICMS\-ST Estoque Conv \(C181\-14\)\.  Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico “[Regra de Preenchimento C181 por Operação](#C181)”;

\- Vlr Unit FCP\-ST Conv Rest \(C181\-19\): valor referente ao estorno de complemento calculado com base no campo Vlr Unit ICMS\-ST Conv Rest \(C181\-18\) aplicando a Alíquota FECEP parametrizada para o produto vigente em relação da data da emissão da nota de saída \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\)\. Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico “[Regra de Preenchimento C181 por Operação](#C181)”;

\- Vlr Unit ICMS\-ST Conv Compl \(C181\-20\): Para saídas internas a consumidor final objeto de devolução, valor referente ao estorno de ressarcimento calculado com base nos campos Vlr Unit ICMS Operação Conv \(C181\-16\), Vlr Unit ICMS Estoque Conv \(C181\-13\), Vlr Unit ICMS\-ST Estoque Conv \(C181\-14\)\.  Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico “[Regra de Preenchimento C181 por Operação](#C181)”;

\- Vlr Unit FCP\-ST Conv Compl \(C181\-21\): Para saídas internas a consumidor final objeto de devolução, valor referente ao estorno de ressarcimento calculado com base no campo Vlr Unit ICMS\-ST Conv Compl \(C181\-20\) aplicando a Alíquota FECEP parametrizada para o produto vigente em relação da data da emissão da nota de saída \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\)\.  Para as demais operações de saída \(exemplo Perda, Saída para Outra UF\) ver tópico “[Regra de Preenchimento C181 por Operação](#C181)”;

• Campos Auxiliares origem Cadastro do Produto \(SAFX2013\):

\- Ind Produto \(SAFX2013\-01\) Cod Produto \(SAFX2013\-02\)

\- Medida Produto \(SAFX2013\-14\)

\- NCM Produto \(SAFX2013\-05\)

\- CEST Produto \(SAFX2013\-54\)

Para consultar o cadastro do produto \(SAFX2013\) acessar o módulo Básicos no menu: Data Warehouse > Manutenção > Códigos > Produto\.

• Campos Auxiliares origem Parametrização do Produto:

\- %Redução BC \(Parametrização Produto\)

\- Alíq\. Interna \(Parametrização Produto\)

\- Alíq\. FCP \(Parametrização Produto\)

Para consulta acesse o menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\.

Observe que a parametrização do produto considerada é a vigente em relação a data da emissão da saída objeto da devolução\.

• Campos Auxiliares origem Documento Fiscal de Devolução \(SAFX08\):

\- Qtde Item NF Devolução \(SAFX08\-24\)

\- Qtde Conv Item NF Devolução \(SAFX08\-137\)

\- Medida Item NF Devolução \(SAFX08\-25\)

\- Fator Conv NF Devolução \(Cadastro Conversão Medida\): Fator de Conversão da Unidade de Origem sendo a Medida do Item NF Devolução e Unidade de Destino à Medida do Produto, cadastrado no módulo Básicos \[menu: Data Warehouse > Manutenção > Cadastros > Conversão de Unidades de Medida, opções Padrão ou Por Produto\];

\- Qtde Conv Calculada p/ NF Devolução: quantidade convertida calculada a partir da aplicação do Fator de Conversão à Qtde Item NF Devolução \(SAFX08\-24\)\. Ou a Qtde Conv Item NF Devolução \(SAFX08\-137\), caso a quantidade convertida já venha carregada no item da NF de devolução\.

\- Qtde Devolvida \(SAFX192\-24\): caso a nota de devolução referencie à nota de saída através da SAFX192, quantidade devolvida informada no campo 24 da SAFX192\.

\- Qtde Devolvida Conv Calculada \(SAFX192\-24 aplicado Fator Conv\): quantidade convertida calculada a partir da aplicação do Fator de Conversão à Qtde Devolvida \(SAFX192\-24\)\.

• Campos Auxiliares origem Documento Fiscal de Saída objeto da Devolução \(SAFX08\):

\- Qtde Item NF Saída \(SAFX08\-24\);

\- Qtde Conv Item NF Saída \(SAFX08\-137\);

\- Medida Item NF Saída \(SAFX08\-25\);

\- Fator Conv NF Saída \(Cadastro Conversão Medida\): Fator de Conversão da Unidade de Origem sendo a Medida do Item NF Saída e Unidade de Destino a Medida do Produto, cadastrado no módulo Básicos \[menu: Data Warehouse > Manutenção > Cadastros > Conversão de Unidades de Medida, opções Padrão ou Por Produto\];

\- Qtde Conv Calculada p/ NF Saída: quantidade convertida calculada a partir da aplicação do Fator de Conversão à Qtde Item NF Saída \(SAFX08\-24\)\. Ou a Qtde Conv Item NF Saída \(SAFX08\-137\), caso a quantidade convertida já venha carregada no item da NF de saída;

\- Vlr Contábil Item NF Saída \(SAFX08\-64\);

\- Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\): calculado considerando o %Redução BC parametrizado para o produto \(veja menu Parâmetros > Produto, opções por Código, por NCM ou por CEST\)\.

Para produto sem %Redução BC: Vlr Unit BC ICMS Operação Conv = \[Valor Contábil do Item \(campo 64 da SAFX08\)\] dividido pela Quantidade Convertida;

Para produto com %Redução BC: Vlr Unit BC ICMS Operação Conv = \[\(Valor Contábil do Item – \(Valor Contábil do Item \* “%Redução BC” / 100\)\)\] dividido pela Quantidade Convertida\.

• Campos Auxiliares Recuperados da Média Ponderada:

\- Vlr Unit ICMS \(Recuperado da Média Ponderada na ocasião da Emissão da Saída\): Valor Médio Unitário ICMS obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit ICMS\-ST \(s/ FECEP\-ST\) \(Recuperado da Média Ponderada na ocasião da Emissão da Saída\): Valor Médio Unitário ICMS\-ST obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit BC ICMS\-ST \(Recuperado da Média Ponderada na ocasião da Emissão da Saída\): Valor Médio Unitário Base de Cálculo do ICMS\-ST obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr Unit FECEP\-ST \(Recuperado da Média Ponderada na ocasião da Emissão da Saída\): Valor Médio Unitário FECEP\-ST obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada\.

• Campos Auxiliares origem Documento Fiscal – Último Recebimento \(SAFX08\):

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

• Campos Auxiliares para o Cálculo da Média Ponderada:

\- Vlr Unit ICMS \(p/ Cálculo da Média Ponderada\): igual ao campo Vlr Unit ICMS Estoque Conv \(C181\-13\);

\- Vlr Unit ICMS\-ST \(s/ FECEP\-ST\) \(p/ Cálculo da Média Ponderada\): Valor Médio Unitário ICMS\-ST obtido do Cálculo da Média Ponderada Móvel, para o dia e produto da saída objeto da devolução\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada\.

Para saídas de períodos anteriores à nova sistemática da IN087/20, o valor é calculado a partir da última nota de recebimento do produto anterior à data da saída, considerando: \[Valor do ICMS\-ST \(campo 52, ou 145 ou 133 ou 107 da SAFX08\) subtraído FECEP\-ST \(campo 140 da SAFX08\)\] dividido pela Quantidade Convertida\.  

__ATENÇÃO:__ Quanto ao Valor do ICMS\-ST destacado na nota, o campo 52 \- Valor ICMS Substituição Tributária pode ser carregado via SAFX08 com o FECEP\-ST embutido ou não\. Por isso, quando o FECEP __não__ estiver embutido no valor do ICMS\-ST, marcar a opção “Realizar a soma dos valores FECP ao ICMS/ICMS\-ST” na equalização DATA MART e __não__ marcar a opção “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” na Geração do Movimento\.

Caso contrário, o FECEP\-ST será considerado dobrado\. Para maiores esclarecimentos veja o tópico[ Sobre Procedimento para Equalização DATA MART versus FECEP embutido no ICMS, ICMS\-ST](file:///C:/Mastersaf/MsafDW/conteudo/Conteudo/Help_on_line/Estadual/Ressarcimento_de_ICMS_ST_RS/oper_safufrcrs.htm#procedimento_datamart_FECEP)\.

\- Vlr Unit BC ICMS\-ST \(p/ Cálculo da Média Ponderada\): Valor Médio Unitário Base de Cálculo do ICMS\-ST obtido do Cálculo da Média Ponderada Móvel para o dia e produto da saída\. Esse campo é demonstrado no Relatório de Conferência do Cálculo da Média Ponderada\.

Para saídas de períodos anteriores à nova sistemática da IN087/20, o valor é calculado a partir da última nota de recebimento do produto anterior à data da saída, considerando: \[Valor da BC ICMS\-ST \(campo 61, ou 144 ou 106 da SAFX08\)\] dividido pela Quantidade Convertida;

\- Vlr Unit FECEP\-ST \(p/ Cálculo da Média Ponderada\): igual ao campo Vlr Unit FCP\-ST Estoque Conv \(C181\-15\);

\- Vlr ICMS \(p/ Cálculo da Média Ponderada\): Valor calculado considerando: \[Qtde Conv \(C181\-03\) x Vlr Unit ICMS \(p/ Cálculo da Média Ponderada\)\]\. O total desse valor por dia e produto é apresentado no campo “Valor ICMS \(Devolução Saída\)” do Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr ICMS\-ST \(s/ FCP\-ST\) \(p/ Cálculo da Média Ponderada\): Valor calculado considerando: \[Qtde Conv \(C181\-03\) x Vlr Unit ICMS\-ST \(s/ FECEP\-ST\) \(p/ Cálculo da Média Ponderada\)\]\. O total desse valor por dia e produto é apresentado no campo “Valor ICMS\-ST \(Devolução Saída\)” do Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr BC ICMS\-ST \(p/ Cálculo da Média Ponderada\): Valor calculado considerando: \[Qtde Conv \(C181\-03\) x Vlr Unit BC ICMS\-ST \(p/ Cálculo da Média Ponderada\)\]\. O total desse valor por dia e produto é apresentado no campo “Valor Base de Cálculo do ICMS\-ST \(Devolução Saída\)” do Relatório de Conferência do Cálculo da Média Ponderada;

\- Vlr FECEP\-ST \(p/ Cálculo da Média Ponderada\): Valor calculado considerando: \[Qtde Conv \(C181\-03\) x Vlr Unit FECEP\-ST \(p/ Cálculo da Média Ponderada\)\]\. O total desse valor por dia e produto é apresentado no campo “Valor FECEP\-ST \(Devolução Saída\)” do Relatório de Conferência do Cálculo da Média Ponderada\.

<a id="C181"></a>__Regra de Preenchimento C181 por Operação__

Base Legal 

 IN 096/20

Cód

Operação \(menu Parâmetros 🡪 \(IN\-RE 087/20\) 🡪 Operações\)

Cod Motivo \(C181\-02\)

Vlr Unit ICMS

Operação Conv 

\(C181\-16\)

Vlr Unit ICMS Op Conv \(C181\-17\)

Vlr Unit ICMS Estoque Conv \(C181\-13\)

Vlr Unit ICMS\-ST Estoque Conv \(C181\-14\)

Vlr Unit FCP\-ST Estoque Conv \(C181\-15\)

Vlr Unit ICMS\-ST Conv Rest \(C181\-18\)

Vlr Unit FCP\-ST Conv Rest \(C181\-19\)

Vlr Unit ICMS\-ST Conv Compl \(C181\-20\)

Vlr Unit FCP\-ST Conv Compl \(C181\-21\)

19\.3\-A\.1\.12 

770

Saída Interna para Consumidor Final \(e Devoluções\)

RS600, RS800

Calculado c/ Valor Contábil do Item

= zero

Média

Pond\.

Média

Pond\.

Média

Pond\.

= \(C181\-16\)

 \- \(C181\-13\)  

\- \(C181\-14\)

= \(C181\-18\) x Alíq FCP

= \(C181\-13\)

 \+ \(C181\-14\)

\- \(C181\-16\)

= \(C181\-20\) 

x Alíq FCP

19\.3\-A\.1\.9 

778

Saída para Outra UF \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)

RS713

= zero

= zero

Média

Pond\.

Média

Pond\.

Média

Pond\.

= zero

= zero

= \(C181\-13\) 

\+ \(C181\-14\)

= \(C181\-20\) 

x Alíq FCP

19\.3\-A\.1\.10 

779

Saída para Outra UF \(RICMS, Livro III, art\.24\) \(e Devoluções\)

RS501

= zero

= zero

= zero

= zero

= zero

= zero

= zero

= zero

= zero

19\.3\-A\.1\.9 

780

Devolução para fornecedor de outra UF, quando a retenção inicial foi realizada pelo próprio remetente da devolução, nos moldes do RICMS, Livro III, art\. 53\-A \(RICMS, Livro III, art\. 25\)

RS713

= zero

= zero

Média

Pond\.

Média

Pond\.

Média

Pond\.

= zero

= zero

= \(C181\-13\) 

\+ \(C181\-14\)

= \(C181\-20\) 

x Alíq FCP

19\.3\-A\.1\.9 

781

Saída para Exportação \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)

RS714

= zero

= zero

Média

Pond\.

Média

Pond\.

Média

Pond\.

= zero

= zero

= \(C181\-13\) 

\+ \(C181\-14\)

= \(C181\-20\) 

x Alíq FCP

19\.3\-A\.1\.9 

782

Saída Interna com nova ST \(RICMS, Livro III, art\.23, III\) \(e Devoluções\)

RS717

= zero

= zero

Média

Pond\.

Média

Pond\.

Média

Pond\.

= zero

= zero

= \(C181\-13\) 

\+ \(C181\-14\)

= \(C181\-20\) 

x Alíq FCP

19\.3\-A\.1\.9 

783

Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.23, V\) \(e Devoluções\)

RS719

= zero

= zero

Média

Pond\.

Média

Pond\.

Média

Pond\.

= zero

= zero

= \(C181\-13\) 

\+ \(C181\-14\)

= \(C181\-20\) 

x Alíq FCP

19\.3\-A\.1\.10 

784

Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.24\-A\) \(e Devoluções\)

RS501

= zero

= zero

= zero

= zero

= zero

= zero

= zero

= zero

= zero

19\.3\-A\.1\.13 

785

Saída com ST não destinada a consumidor final deste Estado, ao abrigo de exclusão de responsabilidade \(RICMS, Livro III, art\. 11\) \(e Devoluções\)

RS500

= zero

= zero

= zero

= zero

= zero

= zero

= zero

= zero

= zero

__Relatório de Conferência do C186__

__Blá blá blá __

__Blá blá blá __

__Blá blá blá __

## <a id="_Toc23774813"></a><a id="_Toc65088967"></a>Criação / Alteração de Tabelas \(Fixas, Acessórias, Básicas\)

## <a id="_Toc354574233"></a><a id="_Toc354574408"></a><a id="_Toc354574452"></a><a id="_Toc354574537"></a><a id="_Toc354578083"></a><a id="_Toc354578310"></a><a id="_Toc354579001"></a><a id="_Toc354579142"></a><a id="_Toc23774814"></a><a id="_Toc65088968"></a>Criação / Alteração de Roteiro Operacional

## <a id="_Toc354574234"></a><a id="_Toc354574409"></a><a id="_Toc354574453"></a><a id="_Toc354574538"></a><a id="_Toc354578084"></a><a id="_Toc354578311"></a><a id="_Toc354579002"></a><a id="_Toc354579143"></a><a id="_Toc23774815"></a><a id="_Toc65088969"></a>Outras informações que necessitarão ser atualizadas \(help, manual operacional etc\)

## <a id="_Toc426992014"></a><a id="_Toc428981618"></a><a id="_Toc23774816"></a><a id="_Toc65088970"></a>Informações p/ Carta do Patch

Direto no Jira

# <a id="_Toc200962062"></a><a id="_Toc200996464"></a><a id="_Toc200996582"></a><a id="_Toc200998062"></a><a id="_Toc354574235"></a><a id="_Toc354574410"></a><a id="_Toc354574454"></a><a id="_Toc354574539"></a><a id="_Toc354578085"></a><a id="_Toc354578312"></a><a id="_Toc354579003"></a><a id="_Toc354579144"></a><a id="_Toc65088971"></a>TESTES

= = = = =


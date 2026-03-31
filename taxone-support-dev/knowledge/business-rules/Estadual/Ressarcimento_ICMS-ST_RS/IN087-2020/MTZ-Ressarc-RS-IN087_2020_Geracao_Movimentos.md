# MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos

- **Fonte:** MTZ-Ressarc-RS-IN087_2020_Geracao_Movimentos.docx
- **Modificado:** 2024-05-20
- **Tamanho:** 123 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 087/2020\) 

Geração dos Movimentos 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\), itens:

Geração 🡪 IN\-RE 087/20 🡪 Geração dos Movimentos

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS48753__

Liliane Videira Assaf

1ª Entrega \(Parte 1\):

__Escopo da 1ª Entrega__

- 770\-Saídas para Consumidor Final \(item 19\.3\-A\.1\.12, da IN 096/20\)
- 771\-Entradas sujeitas à ST \(item 19\.3\-A\.1\.11, da IN 096/20\)

Operações contempladas:

- Entradas \(e devoluções\)
- Saídas Internas para Consumidor Final \(e Devoluções\)

 

Criação da funcionalidade\.

Esta entrega não estão sendo contemplados:

\- Parametrização com Produtos Associados

\- Cupons Fiscais \(C480\)

\- Devolução de Saídas com Cupons Fiscais – C181

22/12/2020 

__MFS48753__

Liliane Videira Assaf

1ª Entrega \(Parte 2\):

Geração do Registro 1250/1255

12/01/2021

__MFS58042__

Liliane Videira Assaf

2ª Entrega:

__Escopo da 2ª Entrega__

- Item 19\.3\-A\.1\.9, da IN 096/20

Operações contempladas:

- 778Saída para Outra UF \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)
- 780Devolução para fornecedor de outra UF, quando a retenção inicial foi realizada pelo próprio remetente da devolução, nos moldes do RICMS, Livro III, art\. 53\-A \(RICMS, Livro III, art\. 25\)
- 781Saída para Exportação \(RICMS, Livro III, art\.23, I\) \(e Devoluções\)
- 782Saída interna com nova ST \(RICMS, Livro III, art\.23, III\) \(e Devoluções\)
- 783Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.23, V\) \(e Devoluções\)

08/02/2021

__MFS59698__

Liliane Videira Assaf

3ª Entrega

__Escopo da 3ª Entrega__

- Fato Gerador Não Realizado item \(item 19\.3\-A\.1\.7, da IN 096/20\)
- Situação de emissão de Nota Fiscal para estabelecimento que realizou retenção \(item 19\.3\-A\.1\.10, da IN 096/20\)
- Situação de operação de saída de mercadoria a destinatário do RS que não seja consumidor final \(item 19\.3\-A\.1\.13, da IN 096/20\)

Operações contempladas:

- 772Furto ou Roubo \- baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)
- 773Perda, extravio ou Deterioração – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)
- 774Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa com Ressarcimento \(RICMS, Livro III, art\. 22\)
- 775Furto ou Roubo \- baixa sem Ressarcimento
- 776Perda, extravio ou Deterioração – baixa sem Ressarcimento
- 777Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento – baixa sem Ressarcimento
- 779Saída para Outra UF \(RICMS, Livro III, art\.24\) \(e Devoluções\)
- 784Saída com Isenção de que trata o art\. 9º, CXX ou CLXIV, do Livro I \(RICMS, Livro III, art\.24\-A\) \(e Devoluções\)
- 785Saída com ST não destinada a consumidor final deste Estado, ao abrigo de exclusão de responsabilidade \(RICMS, Livro III, art\. 11\) \(e Devoluções\)

08/02/2021

__MFS65137__

Liliane Videira Assaf

1\) Inclusão do Cupom Fiscal \(Mod\. 02, 2D e 60\) para viabilizar a geração do registro C480 do Sped Fiscal\.

Os cupons gerados por esse processo devem ser gravados na tabela EST\_ST\_RS\_ECF e gerados em relatório de conferência\.

2\) Retirada dos parâmetros da tela de geração, pois foram para a Tela de Dados Iniciais:

\- Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)

\- Tratamento p/ Entrada objeto da Devolução de períodos anteriores à adoção da sistemática da IN\-RE 087/20:

Valores Unitários Médios recuperados:

\( \) do Inventário do Produto \(conforme IN\-RE 096/20 – item 19\.3\-A\.1\.4\.1\)

\( \) da própria Nota de Entrada referenciada pela Devolução

Dt anterior à adoção IN\-RE087/20: \[31/12/2020\]

13/05/2021

__MFS64191__

Liliane Videira Assaf

IN\-RE 037/21:

Alteração na validação dos códigos de motivos relacionados ao código da operação 780\. Os códigos de motivos relacionados a esta operação mudaram de RS213 e RS713 para RS413\. 

- 780 \- Devolução para fornecedor de outra UF, quando a retenção inicial foi realizada pelo próprio remetente da devolução, nos moldes do RICMS, Livro III, art\. 53\-A \(RICMS, Livro III, art\. 25\)

15/07/2021

__MFS72212__

Liliane Videira Assaf

Criação do Cálculo dos Valores Unitários Médios do Inventário, com a inclusão do parâmetro “Pesquisar as últimas entradas até”\.

09/09/2021 

__MFS72958__

Liliane Videira Assaf

Tratamento de produtos novos sem inventário\.

21/09/2021 

__MFS96666__

Liliane Assaf

Atualização legal IN RE 96/22 \(jan\-2023\):

Tópico 19\.3\-A\.1\.12 da IN RE045/98: criação dos códigos RS101, \.\.\., RS156 e RS301, \.\.\., RS356, RS601, \.\.\., RS656 e RS801, \.\.\., RS856 para as saídas internas a consumidor final\. 

07/12/2022

__MFS591083__

Liliane Assaf

Criação do parâmetro “Considerar as notas fiscais da empresa incorporada”\.

22/01/2024

Sumário

[1\.	Introdução	1](#_Toc85624136)

[2\.	Parâmetros da Tela	1](#_Toc85624137)

[3\.	Críticas	1](#_Toc85624138)

[4\.	Processamento	1](#_Toc85624139)

[1º Passo – Cálculo dos Valores Unitários Médios do Inventário	1](#_Toc85624140)

[2º Passo \- Geração dos Movimentos de Entradas \(C180\)	1](#_Toc85624141)

[3º Passo \- Geração dos Movimentos de Devolução de Entradas \(C186\)	1](#_Toc85624142)

[4º Passo \- Geração dos Movimentos de Devolução das Saídas \(C181\) e Cálculo da Média Ponderada Móvel dos Valores Unitários	1](#_Toc85624143)

[5º Passo \- Geração dos Movimentos de Saídas \(C185, C380, C480\)	1](#_Toc85624144)

[6º Passo – Tratamento para Produtos Novos sem Inventário	1](#_Toc85624145)

[7º Passo: Crítica de Produto Sem Inventário:	1](#_Toc85624146)

[8º Passo: Gerar Relatórios de Conferência	1](#_Toc85624147)

#  

# <a id="_Toc85624136"></a>Introdução

A geração do movimento consiste em recuperar informações dos documentos fiscais normais e devoluções \(SAFX07, SAFX08, SAFX192, SAFX117\), cupons fiscais \(SAFX993, SAFX994\), inventário \(SAFX52\) dos produtos sujeitos ao ICMS\-ST com base nas parametrizações por produtos \(Código, NCM, Cest\) e operações \(CFOP, CFOP/Natureza Operação\) disponíveis no módulo do Ressarcimento RS, menu Parâmetros >> IN\-RE 087/20 e gravar as tabelas que são base para geração dos registros C180, C181, C185, C186, 1250, 1255, H030 do Sped Fiscal\. 

__Sobre Cálculo da Média Pondera Móvel dos Valores Unitários__:

Nesse processo é feito o Cálculo da Média Pondera Móvel dos Valores Unitários do ICMS, ICMS\-ST, Base de Cálculo do ICMS\-ST e FECEP\-ST, com base na IN\-RE 087 tópico 19\.3\-A\.2\.2, para todos os dias do mês da geração e todos os produtos sujeitos a ST\. 

Esse cálculo que fornecerá o Valor Unitário da BC\-ICMS\-ST da entrada para confronto com o valor unitário da saída, cujo resultado da comparação definirá se haverá complemento ou ressarcimento nos movimentos de saídas \(C185\) e devolução de saídas \(C181\)\. 

O cálculo é feito com quatro valores conforme estabelece o tópico 19\.3\-A\.2\.2:

\(alínea “a”\) no saldo inicial do primeiro dia do período, que corresponde ao saldo final do dia anterior;

\(alínea “b”\): movimento de devolução de saídas do período;

\(alínea “c”\): movimento de entradas do período;

\(alínea “d”\): movimento de devolução de entradas do período;

__MFS72212: Criação do Cálculo dos Valores Unitários Médios do Inventário:__

Antes da __MFS72212__, para o __primeiro período__ da geração era necessário que os valores médios unitários fossem carregados na SAFX52 \(campos 21\-VLR\_ICMS\_MEDIO, 22\-VLR\_ICMSS\_MEDIO, 43\-VLR\_BASE\_ICMSS\_MEDIO e 44\-VLR\_FCP\_MEDIO\) no último dia do mês anterior ao período da geração, com IND\_MOT\_INV = 06\. A partir da __MFS72212__, a geração do movimento passou a calcular os valores médios unitários do inventário com base nas últimas notas de entradas do produto\.  Sendo assim, o preenchimento dos valores unitários na SAFX52 para o primeiro período de geração tornou\-se opcional\. Caso valores unitários venham carregados na SAFX52 estes serão utilizados para o cálculo da Média Ponderada, caso contrário a rotina irá calculá\-los\.  

A partir do __segundo período__ de geração, tais valores não precisam mais ser carregados na SAFX52, pois a geração irá considerar os valores unitários do Cálculo da Média Pondera Móvel gerados no período anterior\. Além disso a rotina atualizará os campos 21\-VLR\_ICMS\_MEDIO, 22\-VLR\_ICMSS\_MEDIO, 43\-VLR\_BASE\_ICMSS\_MEDIO e 44\-VLR\_FCP\_MEDIO da SAFX52 do último dia do mês anterior, com os valores unitários médios calculados\. Para isso o cliente deve carregar um registro na SAFX52 do último dia do mês anterior, com IND\_MOT\_INV = 06, sem os valores unitários médios\. 

__Sobre as regras de preenchimento dos campos dos registros C180 e C185__:

As regras foram baseadas no ressarcimento de MG, mas temos particularidades oriundas das definições estabelecidas pelo Rio Grande do Sul, nas IN\-RE 087/20 e IN\-RE 096/20\.

__Sobre as regras de preenchimento dos campos dos registros C181 e C186__:

O Ressarcimento MG ainda não adotou os registros de devolução C181 e C186\. As regras de preenchimento dos registros de devolução se baseiam nos registros das operações que originaram a devolução, ou seja, C181 \(devolução de saídas\) se baseia no C185 \(saída\), e C186 \(devolução de entrada\) se baseia no C180 \(entrada\)\.

__Artefatos gerados pela Geração do Movimento__:

O resultado desta geração são os movimentos que serão utilizados na geração do registro do Sped Fiscal\. Esses movimentos poderão ser conferidos através dos Relatórios que estarão disponíveis em arquivos formato excel:

- Relatório de Conferência do Movimento de Entradas – C180
- Relatório de Conferência do Movimento de Saídas – C185, C380
- Relatório de Conferência do Movimento de Devolução de Saídas – C181
- Relatório de Conferência do Movimento de Devolução de Entradas – C186
- Relatório de Conferência do Movimento de Saída por Cupom Fiscal – C480
- Relatório de Conferência do “Cálculo da Média Pondera Móvel dos Valores Unitários”
- Relatório de Conferência do Cálculo dos Valores Unitários Médios do Inventário

Inicialmente estamos trabalhando os as seguintes operações: Saídas Internas para Consumidor Final \(e Devoluções\) e Entradas \(e Devoluções\)\.

__Base Legal:__

\- IN\-RE 087/20

\- IN\-RE 096/20

# <a id="_Toc85624137"></a>Parâmetros da Tela 

Período: MM/AAAA

Pesquisar as últimas entradas até: \[DD/MM/AAAA\]

\[ \] Utilizar DATA MART para períodos anteriores

\[ \] Considerar as notas fiscais da empresa incorporada

\[ \] Gerar Relatórios de Conferência

Estabelecimentos

\[ \] xxxxxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[ \] xxxxxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[ \] xxxxxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Funcionamento dos campos:

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

<a id="_Hlk517437550"></a>Período 

Data

\(mês e ano\)

S

S

\(MM/AAAA\)

Neste campo será informado o período \(mês e ano\) para a geração dos dados\.

Deve ser um mês válido\.

__MFS72212__

Pesquisar as últimas entradas até

Data 

S

S

DD/MM/AAAA

Neste campo será informada a data utilizada na pesquisa das entradas para o Cálculo dos Valores Médios do Inventário\.

Utilizar DATA MART para períodos anteriores

Alfanumérico

S

S

Check box\.

Caso esse parâmetro seja marcado, a recuperação das notas fiscais de períodos anteriores, referenciadas pelas devoluções, será feita pelas tabelas DATA MART\. Caso contrário a busca será pelas tabelas normais \(X07/X08\)\.

__MFS591083__

Considerar as notas fiscais da empresa incorporada

Alfanumérico

N

S

Check\-box, com default habilitado e desmarcado\.

Este campo é um checkbox onde o usuário informa se vai considerar as notas fiscais de entrada da empresa incorporada, além das notas fiscais da empresa/estabelecimento da geração\. Aplicável ao Cálculo dos Valores médios do Inventário\.

Gerar Relatórios de Conferência

Alfanumérico

N

S

Check box\.

Esta opção, quando selecionada, disponibiliza os relatórios de Conferência dos registros em arquivos formato Excel\.

Estabelecimentos

Alfanumérico 

S

S

Neste campo é exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário\.

Serão disponibilizados para seleção apenas os estabelecimentos de RS \(UF do estabelecimento = RS\)\.

Selecionar

N

N

Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos\.

O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimento”:

\- Somente Estabelecimentos da empresa do login;

\- Somente Estabelecimentos da UF de RS;

Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimentos” já marcados\. 

   

Marcar todos

N

N

Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos”\.

# <a id="_Toc85624138"></a>Críticas 

Existem informações obrigatórias para a geração dos movimentos que são solicitadas através das parametrizações disponíveis no módulo, ou cadastros básicos\.

Assim, antes de iniciar cada uma das gerações \(das entradas, saídas \.\.\.\), vamos checar se elas foram realizadas\. Caso alguma delas não tenha sido efetuada, o processo será abortado\.

__\[MFS65137\]__

__Parâmetrização dos Dados Iniciais__

Caso não exista parametrização dos Dados Iniciais da IN087/20 \(tabela EST\_ST\_RS\_DADOS\_INI\_IN87\) para o estabelecimento foco da geração, então exibir a mensagem no Log da Geração:

*   “Faltou parametrização dos Dados Iniciais para o Estabelecimento\. Favor efetuar a parametrização localizada no menu Parâmetros 🡪 IN\-RE 087/20 🡪 Dados Iniciais”*

__\[MFS65137\]__

__Parâmetrização dos Dados Iniciais – campo Dt anterior à adoção IN\-RE087/20 __

    Caso o campo “Dt anterior à adoção IN\-RE087/20” recuperada da Parametrização dos Dados Iniciais da seja MAIOR OU IGUAL ao primeiro dia do Período informado na tela de geração, então exibir a mensagem no Log da Geração:

*   “Campo "Data anterior à adoção IN\-RE087/20" da Parametrização dos Dados Iniciais deve ser anterior ao Período informado\. Favor ajustar a parametrização localizada no menu Parâmetros 🡪 IN\-RE 087/20 🡪 Dados Iniciais”*

 

__Parametrização de Produtos \(por Código, por NCM e por CEST\):__

Verificar se existe pelo menos uma das parametrizações para Produto \(por Código, por NCM e por CEST\) para a UF = RS, vigente no período da geração\.

Se não for encontrada nenhuma das parametrizações, então exibir uma mensagem no Log da Geração:

*“Faltou realizar parametrização por Produto\. Favor realizar a parametrização em uma das opções disponíveis no menu Parâmetros 🡪 Produtos \(Por Código, Por NCM ou Por CEST\)”*

__Parametrização de Operação \(por CFOP, por Natureza de Operação\)__

Verificar se existe pelo menos uma das parametrizações \(por CFOP ou por Natureza de Operação\), alguma das operações listadas no quadro

- Saída Interna para Consumidor Final \(e Devoluções\) \(código parâmetro 770\)
- Entradas \(e Devoluções\)” \(código parâmetro 771\)
- Operações com códigos parâmetros 772 ao 785 \(vide descrições no quadro da próxima crítica\)

Se não for encontrada parametrização de CFOP nem Natureza de Operação, então exibir mensagem no Log da Geração:

*“Faltou realizar parametrização por CFOP e/ou Natureza da Operação\. Acesse o menu Parâmetros 🡪 \(IN\-RE 087/20\) 🡪 Operações”\.*

__Parametrização de Operação \(por CFOP, por Natureza de Operação\) – CFOP parametrizado para mais de uma operação __

Verificar se existe caso onde o CFOP está parametrizado tanto na Parametrização por CFOP quanto na Parametrização por CFOP/Natureza de Operação, para as operações listadas:

- Saída Interna para Consumidor Final \(e Devoluções\) \(código parâmetro 770\)
- Entradas \(e Devoluções\)” \(código parâmetro 771\)
- Operações com códigos parâmetros 772 ao 785 \(vide descrições no quadro da próxima crítica\)

Se for encontrada tal situação, então exibir mensagem no Log da Geração:

*“CFOP XXXX está parametrizado indevidamente para mais de uma operação\. Acesse o menu Parâmetros 🡪 \(IN\-RE 087/20\) 🡪 Operações, opções CFOP e Natureza da Operação e avalie qual das parametrizações está correta”\.*

__Cadastro dos Códigos de Motivos de Restituição/Complementação__

1\) Validação dos códigos de Motivos x Operações de Saídas parametrizadas por CFOP ou por Natureza de Operação\.

Para cada operação de saída parametrizada no *menu Parâmetros 🡪 \(IN\-RE 087/20\) 🡪 Operações \(por CFOP ou por Natureza de Operação\)*, existe uma relação de códigos de Motivos de Restituição/Complementação que devem estar cadastrados no módulo Básicos 🡪 Data Warehouse, menu Manutenção 🡪 Cadastros 🡪 Códigos de Motivo de Restituição/Complementação de ICMS \(SPED FISCAL\)\.

Veja a relação de códigos de motivo por Operação de Saída:

\[__MFS58042/ MFS59698\]__

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

__\[MFS64191\]__

RS413

__\[MFS64191\]__

19\.3\-A\.1\.11\.1

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

Caso algum código não esteja cadastrado, exibir a seguinte mensagem no log:

“*Falta cadastrar os códigos <RSXXX>, <RSYYYY> para geração dos movimentos de <Descrição da Operação>\.*

*Acesse o módulo Básicos > Data Warehouse, menu Manutenção >> Cadastros >> Códigos de Motivo de*

*Restituição/Complementação de ICMS \(SPED FISCAL\) e, com base na tabela 5\.7 do Sped Fiscal, realize seu cadastro\.”*

Onde:

	*<RSXXX>, <RSYYYY>*: substituia pelos códigos de motivos relacionados à operação que está sendo criticada\.

	*<Descrição da Operação>*: substitua pela descrição da operação que está sendo criticada\.

Exemplo: 

Foi parametrizada a Operação de Saída para Consumidor Final e os códigos de motivos “RS100”, “RS300” não foram cadastrados\. A mensagem exibida no Log da Geração será:

	“*Falta cadastrar os códigos “RS100”, “RS300”, “RS600”, “RS800” para geração dos movimentos de saída para consumidor *

*final \(e devoluções\)\. Acesse o módulo Básicos > Data Warehouse, menu Manutenção >> Cadastros >> Códigos de Motivo de *

*Restituição/Complementação de ICMS \(SPED FISCAL\) e, com base na tabela 5\.7 do Sped Fiscal, realize seu cadastro\.”*

__\[MFS96666\]: Inclusão dos códigos RS101, \.\.\., RS156 e RS301, \.\.\., RS356 a partir de Jan\-2023:__

Para geração com período a partir de Jan\-2023, executar a validação a seguir\.

2\) Validação dos Códigos de Motivos x Percentual de Redução de Base de Cálculo parametrizado para o Produto\.

Caso exista parametrização de CFOP ou Natureza de Operação para o Código de Operação __770__ \- Saída Interna para Consumidor Final \(e Devoluções\), então validar os Códigos de Motivos de acordo com as “Alíquotas Internas” e “%Redução BC” parametrizadas para Produto \(por Código, por NCM e por CEST\), conforme tabela abaixo\.

__Aliquota Interna \(%\)__

__Código Ressarcimento__

__Código Complemento__

__Código Ressarcimento__

__Código Complemento__

7

RS101

RS301

RS601

RS801

5,6

RS102

RS302

RS602

RS802

4

RS103

RS303

RS603

RS803

12

RS104

RS304

RS604

RS804

17,5

RS105

RS305

RS605

RS805

7,5

RS105

RS305

RS605

RS805

5,5

RS105

RS305

RS605

RS805

17

RS105

RS305

RS605

RS805

__Redução de BC \(%\)__

__Código Ressarcimento__

__Código Complemento__

__Código Ressarcimento__

__Código Complemento__

70,588

RS151

RS351

RS651

RS851

53,847

RS152

RS352

RS652

RS852

58,333

RS153

RS353

RS653

RS853

38,889

RS154

RS354

RS654

RS854

41,176

RS155

RS355

RS655

RS855

40

RS156

RS356

RS656

RS856

Recuperar as distintas Alíquota Interna \(%\) e Redução de BC \(%\) das parametrizações do Produto \(por Código, por NCM e por CEST\) de acordo com os critérios:

\- UF = RS;

\- Data Inicial de Vigente <= último dia do período da geração;

\- Data Final da Vigente nula ou, quando preenchida >= primeiro dia do período da geração\.

\- Alíquota Interna \(%\) = 7 ou 5,6 ou 4 ou 12 ou 17,5 ou 7,5 ou 5,5 ou 17;

  Ou 

  Redução de BC \(%\) = 70,588 ou 53,847 ou 58,333 ou 38,889 ou 41,176 ou 40;

Para cada Alíquota Interna \(%\) e Redução de BC \(%\) recuperado, verificar se os correspondentes códigos de Motivos de Restituição/Complementação estão cadastrados no módulo Básicos 🡪 Data Warehouse, menu Manutenção 🡪 Cadastros 🡪 Códigos de Motivo de Restituição/Complementação de ICMS \(SPED FISCAL\)\. 

Caso algum código não esteja cadastrado, exibir a seguinte mensagem no log:

“*Falta cadastrar os códigos <RSXXX>, <RSYYY>, <RSZZZ>, <RSWWW> para geração dos movimentos de Saída Interna para Consumidor Final \(e Devoluções\) com base de cálculo reduzida\.*

*Acesse o módulo Básicos > Data Warehouse, menu Manutenção >> Cadastros >> Códigos de Motivo de*

*Restituição/Complementação de ICMS \(SPED FISCAL\) e, com base na tabela 5\.7 do Sped Fiscal, realize seu cadastro\.”*

Onde:

	*<RSXXX>, <RSYYYY>, <RSZZZ>, <RSWWW>*: substitua pelos códigos de motivos relacionados ao percentual que está sendo criticado\.

Exemplo: 

Foi parametrizado CFOP para Operação de Saída para Consumidor Final, e produtos com Alíquota Interna de 7%\. Os códigos de motivos “RS601”, “RS801” não foram cadastrados\. A mensagem exibida no Log da Geração será:

	“*Falta cadastrar os códigos “RS101”, “RS301”, “RS601”, “RS801” para geração dos movimentos de saída para consumidor *

*final \(e devoluções\)\. Acesse o módulo Básicos > Data Warehouse, menu Manutenção >> Cadastros >> Códigos de Motivo de *

*Restituição/Complementação de ICMS \(SPED FISCAL\) e, com base na tabela 5\.7 do Sped Fiscal, realize seu cadastro\.”*

__Inventário do Último dia do mês anterior ao Período da Geração SAFX52__

Fazer uma consulta na tabela do Inventário \(X52\_INVENT\_PRODUTO\) com os seguintes critérios:

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data do Inventário \(campo 03 \- DATA\_INVENTARIO\) __*último dia do mês anterior*__ ao Mês/Ano informado na tela geração;

\- Motivo do Inventário \(campo 40 \- IND\_MOT\_INV\) = “06” \- controle das mercadorias sujeitas ao regime de substituição tributária;

\- Grupo Contagem \(campo 04 \- GRUPO\_CONTAGEM\) 🡪 1, 2, 3 e 5;

Caso não exista registro de inventário, exibir a seguinte mensagem no log:

*“Falta dados na tabela de inventário \(SAFX52\) para execução da geração do movimento\.  Favor incluir Inventário para o dia anterior ao período informado na tela, com Grupo Contagem igual a 1, 2, 3 ou 5 e Motivo Inventário igual a 06”\.*

Acontecendo qualquer erro, finalizar a geração com status = “\-1” – Erro\.

# <a id="_Toc85624139"></a>Processamento

__Visão resumida do Processamento__

O processamento requer uma ordem na geração dos movimentos já que algumas etapas dependem do resultado da execução anterior\. Por exemplo os movimentos de saída devem ser gerados por último pois dependem do Cálculo da Média Ponderada Móvel, que depende da geração dos demais movimentos\.

Sendo assim vamos executar o processamento seguindo os passos abaixo:

__MFS72212: __

1º Passo: Criação do Cálculo dos Valores Unitários Médios do Inventário

2º Passo: Gerar os Movimentos de Entradas 

3º Passo: Gerar os Movimentos de Devolução das Entradas

4º Passo: Para cada __dia__ do mês da geração, executar em ordem cronológica, a geração os Movimentos de Devolução das Saídas do dia e o Cálculo da Média Ponderada Móvel dos Valores Unitários do dia\.

5º Passo: Gerar os Movimentos de Saídas \(esse utiliza os valores unitários do Cálculo da Média Ponderada Móvel\)

__MFS72958:__

6º Passo: Tratamento de produtos novos sem inventário\.

7º Passo: Gerar Relatórios de Conferência

Segue detalhamento de cada passo do processamento

__MFS72212__

## <a id="_Toc85624140"></a>1º Passo – Cálculo dos Valores Unitários Médios do Inventário

Rotina executada para o seguinte cenário:

\- Para o primeiro período de geração do produto sujeito a ST\.

\- Produto sujeito a ST possui quantidade no inventário maior que zero, mas os valores médios unitários não estão carregados na SAFX52 \(campos 21\-VLR\_ICMS\_MEDIO, 22\-VLR\_ICMSS\_MEDIO, 43\-VLR\_BASE\_ICMSS\_MEDIO e 44\-VLR\_FCP\_MEDIO\) no último dia do mês anterior ao período da geração, com IND\_MOT\_INV = 06\.

Nesse cenário a rotina irá calcular os valores unitários médios do inventário a partir das últimas entradas até que a quantidade do inventário seja atingida e armazenará os valores unitários calculados na tabela de Média Ponderada \(EST\_ST\_RS\_MEDIA\_POND\) para o último dia do mês anterior ao período da geração\.

Definição está no documento matriz:

MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Cálculo Médio Unitario Inventário\.docx

## <a id="_Toc85624141"></a>2º Passo \- Geração dos Movimentos de Entradas \(C180\)

Nessa etapa é feita a recuperação das notas fiscais de entrada do período, dos produtos sujeitos a ICMS\-ST, execução das regras de negócio e gravação das tabelas específicas da geração do movimento, que servirão tanto para geração do registro C180 do Sped Fiscal, como para o “Cálculo da Média Pondera Móvel dos Valores Unitários” do período \.

As tabelas específicas da geração do movimento, que são gravadas nessa etapa, possuem uma correspondência com as tabelas que geram os registros do SPED FISCAL\. 

Definição

Tabelas Específicas da Geração do Movimento

Tabela Destino

Registros do SPED FISCAL

Notas Fiscais de Entrada

EST\_ST\_RS\_NF\_ENT

x296\_info\_compl\_st\_itens\_merc

C180

Para maiores detalhamentos ver documentos matrizes: 

\- MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Entradas\.docx

## <a id="_Toc85624142"></a>3º Passo \- Geração dos Movimentos de Devolução de Entradas \(C186\)

Nessa etapa é feita a recuperação das notas fiscais de devolução de entrada do período, dos produtos sujeitos a ICMS\-ST, execução das regras de negócio e gravação das tabelas específicas da geração do movimento, que servirão tanto para geração do registro C186 do Sped Fiscal, como para o “Cálculo da Média Pondera Móvel dos Valores Unitários” do período\.

As tabelas específicas da geração do movimento, que são gravadas nessa etapa, possuem uma correspondência com as tabelas que geram os registros do SPED FISCAL\. São elas:

Definição

Tabelas Específicas da Geração do Movimento

Tabela Destino

Registros do SPED FISCAL

Notas Fiscais de Devolução de Entrada

EST\_ST\_RS\_NF\_DEV\_ENT

X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV

C186

Para maiores detalhamentos ver documentos matrizes: 

\- MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Devolução de Entradas\.docx

## <a id="_Toc85624143"></a>4º Passo \- Geração dos Movimentos de Devolução das Saídas \(C181\) e Cálculo da Média Ponderada Móvel dos Valores Unitários

Para cada __DIA__ do mês da informado na tela de geração, executar:

- Geração dos Movimentos de Devolução das Saídas do dia;
- Cálculo da Média Ponderada Móvel dos Valores Unitários do dia\.

A execução deve ser realizada por dia, em __ordem cronológica__, pelos seguintes motivos:

\- No “Cálculo da Média Pondera Móvel dos Valores Unitários” os valores unitários resultantes do cálculo de um dia, servirão como saldo inicial para o cálculo do dia seguinte; Isso exige que o cálculo seja feito dia a dia\.

\- Os valores das Devoluções das Saídas do dia compõe os valores unitários calculados no “Cálculo da Média Pondera Móvel dos Valores Unitários”;

\- Na Geração dos Movimentos de Devolução de Saídas, a devolução utiliza os valores unitários médios calculados na ocasião da data de emissão da nota de saída referenciada\. Logo depende de um dia anteriormente calculado\. Ou seja, as notas de devolução de um dia só podem ser processadas se os dias anteriores já tiverem com o “Cálculo da Média Pondera Móvel dos Valores Unitários” realizado\.

Por exemplo:

Geração de Janeiro/2021

 Dia 01:   1º\) Gerar os Movimentos de Devolução de Saídas

                2º\) Realizar o Cálculo da Média Pondera Móvel dos Valores Unitários\.

                    \- Recuperar o total do dia anterior \(com a quantidade e os valores unitários de 31/12/2020\)

                    \-  Recuperar o total do Movimento de Devolução de Saídas do DIA 01

                    \-  Recuperar o total do Movimento de Entradas do DIA 01

                    \-  Recuperar o total do Movimento de Devolução de Entradas do DIA 01

                    \- Calcular os valores unitários de ICMS, ICMS\-ST, Base de Cálculo do ICMS\-ST e FECEP\-ST do DIA 01

  Dia 02:   1º\) Gerar os Movimentos de Devolução de Saídas

                 2º\) Realizar o Cálculo da Média Pondera Móvel dos Valores Unitários\.

                    \-  Recuperar o total do dia anterior \(do DIA 01\)

                    \-  Recuperar o total do Movimento de Devolução de Saídas do DIA 02

                    \-  Recuperar o total do Movimento de Entradas do DIA 02

                    \-  Recuperar o total do Movimento de Devolução de Entradas do DIA 02

                    \- Calcular os valores unitários de ICMS, ICMS\-ST, Base de Cálculo do ICMS\-ST e FECEP\-ST do DIA 02

\.\.\.

  Dia 31:   1º\) Gerar os Movimentos de Devolução de Saídas

                 2º\) Realizar o Cálculo da Média Pondera Móvel dos Valores Unitários

                   \- Recuperar o total do dia anterior \(do DIA 30\)

                   \-  Recuperar o total do Movimento de Devolução de Saídas do DIA 31

                   \-  Recuperar o total do Movimento de Entradas do DIA 31

                   \-  Recuperar o total do Movimento de Devolução de Entradas do DIA 31

                   \- Calcular os valores unitários de ICMS, ICMS\-ST, Base de Cálculo do ICMS\-ST e FECEP\-ST do DIA 31

__\- Geração dos Movimentos de Devolução de Saídas \(C181\)__

Nessa etapa é feita a recuperação das notas fiscais de devolução de saída do __DIA__, dos produtos sujeitos a ICMS\-ST, execução das regras de negócio e gravação das tabelas específicas da geração do movimento, que servirão tanto para geração dos registros C181 do Sped Fiscal, como para o “Cálculo da Média Pondera Móvel dos Valores Unitários” do DIA\.

As tabelas específicas da geração do movimento, que são gravadas nessa etapa, possuem uma correspondência com as tabelas que geram os registros do SPED FISCAL\. São elas:

Definição

Tabelas Específicas da Geração do Movimento

Tabela Destino

Registros do SPED FISCAL

Notas Fiscais de Devolução de Saída

EST\_ST\_RS\_NF\_DEV\_SAI

X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV

C181

Para maiores detalhamentos ver documentos matrizes: 

\- MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Devolução de Saidas\.docx

__\- Cálculo da Média Pondera Móvel dos Valores Unitários__

Realizar o “Cálculo da Média Pondera Móvel dos Valores Unitários” do ICMS, ICMS\-ST, Base de Cálculo do ICMS\-ST e FECEP\-ST, para o __DIA__, dos produtos sujeitos ao ICMS\-ST\. O cálculo é feito com quatro valores conforme estabelece o tópico 19\.3\-A\.2\.2:

\(alínea “a”\) no saldo inicial do primeiro dia do período, que corresponde ao saldo final do dia anterior;

\(alínea “b”\): movimento de devolução de saídas do período;

\(alínea “c”\): movimento de entradas do período;

\(alínea “d”\): movimento de devolução de entradas do período;

Os valores das alíneas “b”, “c” e “d” foram calculados na etapa anterior\.

O dia que não tiver movimento, os valores são os mesmos do dia anterior;

O resultado do cálculo é armazenado numa tabela para uso na Geração dos Movimentos de Saídas e em gerações de períodos posteriores:

Definição

Tabelas Específicas da Geração do Movimento

Cálculo da Média Pondera Móvel dos Valores Unitários

EST\_ST\_RS\_MEDIA\_POND

__Pré\-requisito__:

É necessário que todos os produtos sujeitos a ICMS\-ST possuam um registro de inventário \(SAFX52\) com IND\_MOT\_INV = 06 no dia imediatamente anterior ao período de geração\.

Para o primeiro período da geração, os Valores Unitários do ICMS, ICMS\-ST, Base de Cálculo do ICMS\-ST e FECEP\-ST devem estar carregados na SAFX52 para o dia imediatamente anterior ao mês da geração\. 

A geração irá calcular os valores unitários para todos os dias do mês da geração e, para isso, necessita que os valores unitários estejam carregados no inventário do último dia do mês anterior\. 

A partir do segundo período de geração, os Valores Unitários do ICMS, ICMS\-ST, Base de Cálculo do ICMS\-ST e FECEP\-ST do último dia do mês anterior já estarão calculados pela geração do mês anterior\. Essa rotina atualizárá a Tabela do Inventário \(X52\_INVENT\_PRODUTO\) com os valores unitários calculados, bastando apenas existir o registro do inventário para o produto com IND\_MOT\_INV = 06\. 

Para maiores detalhamentos ver documentos matrizes: 

\- MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Cálculo Média Ponderada\.docx

## <a id="_Toc85624144"></a>5º Passo \- Geração dos Movimentos de Saídas \(C185, C380, C480\)

Nessa etapa é feita a recuperação das notas fiscais de saídas e cupons fiscais do período, dos produtos sujeitos a ICMS\-ST, execução das regras de negócio e gravação das tabelas específicas da geração do movimento, que servirão de base para geração dos registros C185, c380 e C480 do Sped Fiscal\.

O “__Cálculo da Média Pondera Móvel dos Valores Unitários”__ realizado na etapa anterior fornecerá os valores médios unitários necessários para o cálculo do valor do ressarcimento ou complemento, apresentado nos registros C185, C380, C480\.

 

 As tabelas específicas da geração do movimento, que são gravadas nessa etapa, possuem uma correspondência com as tabelas que geram os registros do SPED FISCAL\. São elas:

Definição

Tabelas Específicas da Geração do Movimento

Tabela Destino

Registros do SPED FISCAL

Notas Fiscais de Saída

EST\_ST\_RS\_NF\_SAI

x296\_info\_compl\_st\_itens\_merc

C185, C380

Cupons Fiscais

EST\_ST\_RS\_ECF

X297\_INF\_COMP\_ST\_CUPOM\_ECF

C480

Para maiores detalhamentos ver documentos matrizes: 

\- MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Saídas\.docx

__MFS72958__

## <a id="_Toc85624145"></a>6º Passo – Tratamento para Produtos Novos sem Inventário

Nessa etapa é feito o tratamento para produtos novos\. Ou seja, produtos que iniciaram sua movimentação no período da geração, não existindo movimentação em período anterior e que o cliente não carrega o inventário do último dia do mês anterior pois este registro não se encontra no sistema ERP de origem\.

A rotina irá identificar esses produtos e gravar um registro com quantidade e valores zerados na tabela de Média Ponderada \(EST\_ST\_RS\_MEDIA\_POND\) com IND\_GRAVAÇÃO = B, para o produto e último dia do mês anterior ao período da geração\.

A rotina de Transferência dos Movimentos para EFD Fiscal irá ler esses registros da tabela de médias ponderadas \(EST\_ST\_RS\_MEDIA\_POND\), e gerar registros na Tabela de Inventário \(X52\) com quantidade e valores zerados\.

Definição está no documento matriz:

MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Tratamento Novo Produto sem Inventário\.docx

__MFS72958__

## <a id="_Toc85624146"></a>7º Passo: Crítica de Produto Sem Inventário:

Crítica para os produtos parametrizados que não possuam registro de inventário \(SAFX52\) para o último dia do mês anterior \(que não sejam os produtos novos tratados no passo 6º\)\.

Com a MFS\-72958 esta crítica foi transferida da rotina do Cálculo da Média Ponderada para cá, pois há necessidade de desconsiderar os produtos novos sem inventário que são tratados no passo 6º\.

__Recuperar os Produtos s/ inventário considerando os critérios__:

\- O produto deve constar na parametrização do menu “*Parâmetros 🡪 Produtos 🡪 Por Código*”, __ou__, seu NCM deve estar parametrizado no menu “*Parâmetros 🡪 Produtos 🡪 Por NCM*”, __ou__, seu CEST deve estar parametrizado no menu “*Parâmetros 🡪 Produtos 🡪 Por CEST*”\. 

\- Produto possua média ponderada \(EST\_ST\_RS\_MEDIA\_POND\) com primeiro dia do período com quantidade inicial zerada\.

\- Produto __não__ pertença aos “Novos Produtos sem Inventário” tratados no passo 6º, com a gravação de um registro na média ponderada \(EST\_ST\_RS\_MEDIA\_POND\) para o último dia do mês anterior com IND\_GRAVAÇÃO = B\. Desconsiderar esses produtos\.

\-Produto não possui registro de inventário \(X52\_INVENT\_PRODUTO\) com os critérios a seguir, ou possui registro de inventário com quantidade zerada:

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data do Inventário \(campo 03 \- DATA\_INVENTARIO\) último dia do mês anterior que está sendo processado;

\- Motivo do Inventário \(campo 40 \- IND\_MOT\_INV\) = “06” \- controle das mercadorias sujeitas ao regime de substituição tributária;

\- Grupo Contagem \(campo 04 \- GRUPO\_CONTAGEM\) 🡪 1, 2, 3 e 5;

__Crítica:__

Se o produto sujeito a ICMS\-ST __não__ possui registro na Tabela do Inventário \(X52\_INVENT\_PRODUTO\) para o último dia do mês anterior, 

__ou __

Se o produto sujeito a ICMS\-ST existir registro na Tabela de Inventário \(X52\_INVENT\_PRODUTO\) para o último dia do mês anterior com a quantidade zerada, então:

Exibir a seguinte mensagem no log:

*“Cálculo da Média Ponderada Móvel: O Saldo inicial do dia “XX” foi calculado zerado, pois o Saldo Final do dia anterior não foi encontrado na base, ou seus valores estão zerados\. Certifique\-se de que existe registro de inventário \(SAFX52\) para o produto em DD/MM/AAAA, com grupo de contagem 1, 2, 3 e 5, com motivo inventário 06 e Quantidade carregados\. Para o primeiro mês da geração carregue também os e Valores Médios Unitários de ICMS, ICMS\-ST, Base ICMS\-ST, FECEP\. Para maiores informações consulte o help do módulo\.”*

Onde: DD/MM/AAAA = último dia do mês anterior

Dados de Indentificação: Estabelecimento: xxx \-  Produto\(ind/cód\) x\-xxx

## <a id="_Toc85624147"></a>8º Passo: Gerar Relatórios de Conferência

Geração dos Relatórios de Conferência em arquivos excel, com base nas tabelas específicas da Geração do Movimento\.

__Relatório de Conferência__

__Tabelas Específicas da Geração do Movimento__

Movimento de Entradas \(C180\)

EST\_ST\_RS\_NF\_ENT

Movimento de Devolução de Entrada \(C186\)

EST\_ST\_RS\_NF\_DEV\_ENT

Movimento de Devolução de Saída \(C181\)

EST\_ST\_RS\_NF\_DEV\_SAI

Movimento de Saídas \(C185\)

EST\_ST\_RS\_NF\_SAI

Movimento de Saídas \(C380\)

EST\_ST\_RS\_NF\_SAI

Movimento de Cupons Fiscais \(C480\)

EST\_ST\_RS\_ECF

Cálculo da Média Pondera Móvel dos Valores Unitários

EST\_ST\_RS\_MEDIA\_POND

Cálculo dos Valores Unitários Médios do Inventário

Cálculo do Estoque Final 

Todas as tabelas acima

Para maiores detalhamentos ver documentos matrizes: 

\- MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Entradas\.docx

\- MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Devolução de Entradas\.docx

\- MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Devolução de Saidas\.docx

\- MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Saídas\.docx

\- MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Cálculo Média Ponderada\.docx

\- MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Cálculo Médio Unitario Inventário\.docx

\- MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Cálculo Estoque Final\.docx

= = = = = =

 


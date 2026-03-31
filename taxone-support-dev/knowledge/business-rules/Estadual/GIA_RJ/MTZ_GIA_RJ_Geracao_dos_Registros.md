# MTZ_GIA_RJ_Geracao_dos_Registros

- **Fonte:** MTZ_GIA_RJ_Geracao_dos_Registros.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 36 KB

---

# Geração dos Registros da GIA\-RJ 

__Localização: __

__Módulo:__ 🡪 Estadual 🡪 GIA\-RJ

__Menu:__ Obrigações 🡪 Geração 🡪 Geração dos Registros

##### DOCUMENTO DE REQUISITO

###### Data de Revisão

###### DR

###### Nome

__Descrição__

__Autor__

__OS2564__

\.

O objetivo deste documento de requisito é permitir que o campo “Valor de Isentas” do registro 0230 da GIA\-RJ recupere as informações do campo “Valor Abatimento não tributado” para a geração da GIA\-RJ\. 

Marcos Roberto de Oliveira

__OS2983__

GIA\-RJ – Gerar Registro 0230 com os 6 últimos dígitos da NF

Este documento de requisito tem por objetivo permitir que o módulo GIA\-RJ recupere a informação para o campo Número da Nota Fiscal do registro 0230 truncando o mesmo à esquerda\. 

Marcos Roberto de Oliveira

13/07/2010

__OS2967__

Lançamentos Complementares dos Registros 0140 a 0200

Criação do parâmetro que gera os registros por Lançamentos Complementar

Juliana Garcia

07/11/2011

__CH110797__

GIA\-RJ – Gerar Registro 0120 

O objetivo deste documento é corrigir a geração do registro tipo 0120, pois não está considerando os campos 117 – UF\_ORIG\_DEST e 122 – UF\_DESTINO, ambos da SAFX07 para a geração\.

Vanessa W\. Bravo

04/09/2012

__CH12228\_2012__

VALOR DO SALDO ANTERIOR ST 

Tratamento para geração do valor do saldo credor do período anterior ICMS ST que não esta sendo processado no Registro identificador da declaração \(0110\)

Edilson Marcelino

22/10/2014

__CH13935\_2014__

GIA\-RJ – Gerar Registro 0120 

Acrescentada a origem de informação para o Registro 0120\.

Julyana Perrucini

18/11/2014

__CH23901\_2014__

GIA\-RJ – Gerar Registro 0210

Acrescentada a origem de informação para o Registro 0210 para alteração do preenchimento do campo Valor ICMS\-ST Outros Produtos\.

Julyana Perrucini

17/12/2014

__OS4694__

GIA\-RJ – Alteração Registro 0120

Este documento tem como objetivo alterar o preenchimento dos campos “Valor Base ICMS\-ST” e “Valor ICMS\-ST” do Registro 0120 \- Entradas\.

Julyana Perrucini

08/07/2015

__CH3151\_2015__

GIA\-RJ – Alteração Registro 0120

Este documento tem como objetivo alterar o preenchimento dos campos “Valor Base ICMS\-ST” e “Valor ICMS\-ST” do Registro 0120 – Entradas, para que seja considerados os valores de ST apenas para os CFOP´s iniciados com 1\.

Lara Aline

09/07/2015

__CH11570\_2015__

Lançamentos Complementares dos Registros 0140 a 0200

Este documento tem como objetivo documentar a correta recuperação dos lançamentos complementares dos Registros 0140 à 0200\.

Lara Aline

23/02/2016

__CH3014\_2016__

GIA\-RJ – Inclusão Regra Geral para dados acessórios

Este documento tem como objetivo incluir a referência da geração dos dados acessórios para obtenção dos valores a serem gerados nos registros da GIA\.

Julyana Perrucini

27/12/2018

__MFS\-20953__

GIA\-RJ – Alteração Registro 0220

Essa MFS tem como objetivo alterar o preenchimento do campo Código de UF do Registro Tipo 0220 \- Movimentação de Saídas Interestaduais\.

Julyana Perrucini

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RG00__

__Regra Geral__

Alguns registros serão gerados a partir de Resumo das Operações das Obrigações Acessórias, que estarão especificadas no item “Origem” das regras de negócio\.

__\[ALTERADA – CH3014\_2016\]__

Para obter os valores do Resumo das Operações, é necessário que o usuário faça a execução da “Geração dos Dados Acessórios”, podendo ser pelo próprio módulo da GIA\-RJ, no item de menu Obrigações \(normal ou por IEU\); ou através do módulo de Obrigações Acessórias, no item de menu Movimento \(como Geração dos Dados\)\.

Para verificar a regra dos Parâmetros da Geração dos Dados Acessórios, verificar documento matriz MTZ \- Obrigacoes Acessorias – Geracao de Dados para as Obrigacoes Estaduais\.doc em \\MsafDW\\documentacao funcional\\Documento Matriz\\Estadual\\Obrigacoes Acessorias\.

__CH3014\_2016__

__RN00__

Após a apuração do ICMS, geração das notas fiscais remetidas da ZFM\-ALC, geração dos dados acessórios, valores de apuração por amparo/texto/ocorrência e dos registros o sistema deve recuperar para o campo “Parc\. Reduzir” da tela NF’s remetidas para ZFM\-ALC \(aba Complemento\) do módulo GIA RJ, a informação que estiver contida no campo 233 – VLR\_ABAT\_NTRIBUTADO da tabela SAFX07\.

__OS2564__

__RN01__

Gravar no campo “Valor de Isentas” do registro 0230 – Registro de Movimentação de Saídas para ZFM/ALC a informação que estiver contida no campo 233 – VLR\_ABAT\_NTRIBUTADO da tabela SAFX07\.

__OS2564__

__RN02__

O campo “Valor de Isentas” do registro 0230 – Registro de Movimentação de Saídas para ZFM/ALC não ira mais recuperar suas informações do Valor de Desconto como acontece atualmente,

__OS2564__

__RN03__

Recuperar para o campo Número da Nota Fiscal do registro __0230__ a informação do Número da Nota Fiscal truncando à esquerda, ou seja, recuperando o número da NF a partir do último dígito da direita até completar 6 \(seis\) posições\. Abaixo segue um exemplo de como recuperar a informação:

__Número da NF__

__Truncando à direita \(sistemática atual\)__

__Truncando à esquerda \(nova sistemática\)__

00257589

002575

257589

__OS2893__

__RN04__

Essa nova sistemática de geração do campo Número da Nota Fiscal do registro __0230 __deverá ser fixa no sistema\. Não existirá nenhum parâmetro para que o sistema se comporte dessa forma\.

__OS2893__

__RN05__

Parâmetro na tela de Geração dos Registros

Localização: Módulo 🡪 Estadual 🡪 GIA\-RJ

Menu: Obrigações 🡪 Geração 🡪 Geração dos Registros

Quando o parâmetro for habilitado atingirá os seguintes registros 0140 \(outros débitos\), 0150 \(estorno de crédito\), 0160 \(outros créditos\), 0170 \(estorno de débito\), 0180 \(deduções\), 0190 \(oper\. c/ prazo especial\), 0200 \(outros icms devido\. A partir da criação deste parâmetro no módulo da GIA\-RJ, a regra para demonstrar a montagem dos registros, passa a ser:

- Criar o parâmetro “Gerar registro por item de Lançamento Complementar do ICMS” e trazer “desmarcado”\.
- Se parâmetro Gerar registro por item de Lançamento Complementar do ICMS desmarcado:

Manter a funcionalidade da tabela EST\_GIA\_INFO, agrupar os lançamentos complementares da apuração do ICMS, pelo campo COD\_AMPARO\_LEGAL e COD\_SUB\_ITEM\_OCORR, totalizando o campo VLR\_OUTROS\. \(conforme funcionamento atual\);

- Se parâmetro Gerar registro por item de Lançamento Complementar do ICMS marcado:

Retirar os agrupamentos da rotina referente aos lançamentos complementares da apuração do ICMS, atualmente pelos campos COD\_AMPARO\_LEGAL e COD\_SUB\_ITEM\_OCORR\. A rotina deverá mostrar um registro para cada lançamento complementar de ICMS, mesmo que o código de amparo seja igual e a descrição diferente\. O campo VLR\_OUTROS na tabela EST\_GIA\_INFO não poderá ser totalizado\.

__OS2967__

__RN06__

__Geração dos Registros para geração Registro Tipo 0140 a 0200:__

Localização: Módulo 🡪 Estadual 🡪 GIA\-RJ

Menu: Obrigações 🡪 Geração 🡪 Geração dos Registros 

__\[ALTERADA CH11570\_2015\]__

Deverão ser recuperados apenas os lançamentos complementares \(outros débitos e créditos, estorno de débitos e créditos, deduções\.\.\.\) que possuam classe de lançamento e amparo cadastrados\.   
Localização: Módulo ICMS \(Menu Apuração/ Apuração do ICMS/ Lançamentos Complementares\) 

*Exemplo:* 

__Lançamento__

__Classe Lançamento   
ICMS Normal__

__Amparo   
ICMS Normal__

__Classe Lançamento   
ICMS\-ST__

__Amparo   
ICMS\-ST__

Outros Débitos

585

N02\.\.\.

632

S02\.\.\.

Estorno de Crédito

579

N03\.\.\.

633

S03\.\.\.

Outros Créditos

584

N07\.\.\.

636

S07\.\.\.

Estorno de Débitos

581

N08\.\.\.

637

S08\.\.\.

__\[ALTERADA OS2967\]__

A procedure SAF\_GERA\_GIA\_RJ sofrerá alteração dos agrupamentos/“desagrupamentos” e quando usar os registros na tabela EST\_RJ\_GIA\_R140\_2 para montar o arquivo texto, deverá obedecer ao critério do parâmetro “Gerar registro por item de Lançamento Complementar do ICMS” para os Registros 0140 a 0200\.

Parâmetro marcado: A rotina deverá gravar um registro para cada lançamento complementar de ICMS, mesmo que o código de amparo seja igual e a descrição diferente\.

Parâmetro desmarcado: Manter a mesma funcionalidade, agrupar os lançamentos complementares da apuração do ICMS, pelo campo COD\_AMPARO\_LEGAL e COD\_SUB\_ITEM\_OCORR, totalizando o campo VLR\_OUTROS da tabela EST\_GIA\_INFO \.

__OS2967__

__CH11570\_2015__

__RN07__

__Regra geral para geração Registro Tipo 0120:__

__Módulo:__ Estadual 🡪 GIA\-RJ

__Menu:__ Obrigações 🡪 Geração 🡪 Geração dos Registros

__Origem:__ Resumo das Operações por CFOP/UF \(módulo Estadual >> Obrigações Acessórias >> Relatórios >> Resumo das Operações\) tabela EST\_RES\_CFO\_UF\_01\.

No momento da geração dos registros, o sistema deve considerar os campos 117 – UF\_ORIGEM\_DEST E 122 – UF\_DESTINO, ambos da SAFX07, desde que o Parâmetro Item 67 \- Lançar Campo UF Origem/Destino do Documento Fiscal nos Livros Fiscais Movimentos/Resumo por UF, esteja devidamente parametrizado no módulo ICMS → Parâmetros por UF, quando:

\- Campo 11 \- DATA\_EMISSAO \(SAFX07\) for pertinente ao período de geração;

\- Campo 13 \- COD\_MODELO = ‘08’ \(SAFX07\)\.

__CH110797__

__CH13935\_2014__

__RN07\.a__

__Regra para geração Registro Tipo 0120 – Campo Valor Base ICMS\-ST:__

__Módulo:__ Estadual 🡪 GIA\-RJ

__Menu:__ Obrigações 🡪 Geração 🡪 Geração dos Registros

__Origem:__ Resumo das Operações por CFOP/UF \(módulo Estadual >> Obrigações Acessórias >> Relatórios >> Resumo das Operações\) tabela EST\_RES\_CFO\_UF\_01\.

__Tratamento:__

- Preencher com o valor total do CFOP da coluna “Valor Base ICMSS \(Apropriado\)” do Resumo\.
- Deve ser considerado apenas CFOPs iniciados com 1\. , 2 e 3\.

__OS4694__

__CH3151\_2015__

__RN07\.b__

__Regra para geração Registro Tipo 0120 – Campo Valor ICMS\-ST:__

__Módulo:__ Estadual 🡪 GIA\-RJ

__Menu:__ Obrigações 🡪 Geração 🡪 Geração dos Registros

__Origem:__ Resumo das Operações por CFOP/UF \(módulo Estadual >> Obrigações Acessórias >> Relatórios >> Resumo das Operações\) tabela EST\_RES\_CFO\_UF\_01\.

__Tratamento:__

- Preencher com o valor total do CFOP da coluna “Valor ICMSS \(Apropriado\)” do Resumo\.
- Deve ser considerado apenas CFOPs iniciados com 1\. , 2 e 3\.

__OS4694__

__CH3151\_2015__

__RN08__

__Regra para geração do campo  VALOR DO SALDO ANTERIOR ST do Registro 0110:__

Recuperar o valor da operação = '009' do Resumo SUBST\. TRIBUTÁRIA do Livro de Apuração ICMS \(108\) no período de geração, desde que todos os passos de geração da GIA\-RJ tenham sido executados corretamente\.

__CH12228\_2012__

__RN09__

__Regra para geração Registro Tipo 0220:__

__Módulo:__ Estadual 🡪 GIA\-RJ

__Menu:__ Obrigações 🡪 Geração 🡪 Geração dos Registros

__Origem: __Resumo das Operações UF /CFOP – Saídas \(módulo Estadual >> Obrigações Acessórias >> Relatórios >> Resumo das Operações\) tabela EST\_RES\_CFO\_UF\_01\.

__Destino:__ Manutenção – Saídas Interestaduais – Reg\. 0220\.

__\[ALTERADA – MFS\-20953\]__

__Tratamento:__

Quando o parâmetro “Identificação da UF/ Município nos Resumos por município e UF/ CFOP” do Resumo das Operações for selecionado por Campo Origem/ Destino/ Consumo da NF, ao se tratar de nota fiscal de Utilities \(SAFX42/SAFX43\) o campo Código de UF desse registro 0220 será gerado considerando o campo 75 \- UF do Ponto de Consumo/Terminal faturado da tabela definitiva da SAFX42 de acordo com o campo 76 \- Município do Ponto de Consumo gerado no Resumo das Operações UF /CFOP – Saídas, caso contrário, será considerada a UF da PFJ cadastrada na nota fiscal\.

__CH3014\_2016__

__MFS\-20953__

__RN12__

__Regra para geração Registro Tipo 0210:__

__Módulo:__ Estadual 🡪 GIA\-RJ

__Menu:__ Obrigações 🡪 Geração 🡪 Geração dos Registros

__Origem: __Resumo das Operações por UF /CFOP – Entradas \(módulo Estadual >> Obrigações Acessórias >> Relatórios >> Resumo das Operações\) tabela EST\_RES\_CFO\_UF\_01\.

__Destino:__ Manutenção – Entradas Interestaduais – Reg\. 0210\.

Campo __Valor ICMS\-ST Outros Produtos:__ Preencher com o total da soma do valor por estado da coluna Valor ICMSS do Resumo\.

__CH23901\_2014__

	

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


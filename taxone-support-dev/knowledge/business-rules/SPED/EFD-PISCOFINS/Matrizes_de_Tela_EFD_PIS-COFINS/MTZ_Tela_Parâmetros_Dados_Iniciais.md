# MTZ_Tela_Parâmetros_Dados_Iniciais

- **Fonte:** MTZ_Tela_Parâmetros_Dados_Iniciais.docx
- **Modificado:** 2026-02-10
- **Tamanho:** 92 KB

---

    

# EFD \- PIS/PASEP \- COFINS – Dados Iniciais 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3169\-GE

Criação do documento

Tela – Dados Iniciais

14/03/2012

OS3169\-GE25

Alteração do Documento

Adequação da tela para atendimento ao Lucro Presumido

16/03/2012

OS3169\-25CDW

Alteração do Documento

Adequação da tela para atendimento ao Lucro Presumido

03/05/2012

OS3169\-GE25C

Alteração do Documento

Adequação da tela para atendimento ao Lucro Presumido

03/07/2012

OS3710

Alteração do Documento

Inclusão de um novo parâmetro, para contemplar na EFD\-Contribuições as Notas Fiscais \(Saídas\) de Mercadorias Não Escrituradas\.

06/08/2012

OS4097

Alteração do Documento

Inclusão do parâmetro ‘Registro A100, C100, C190, C395, C500, D100 e D500 – Seleção das Operações Geradoras de Créditos’

12/07/2012

OS4165

Alteração do Documento

Inclusão do parâmetro ‘Registro 0145 \- Regime de Apuração da Contribuição Previdenciária sobre a Receita Bruta’

30/08/2013

CH19724/2013

Alteração do Documento

Ampliação das opções do parâmetro ‘Registro A100, C100, C190, C395, C500, D100 e D500 – Seleção das Operações Geradoras de Créditos’\.

16/10/2013

OS4316\-A

Alteração do Documento

Criação do campo Código da SCP

31/01/2014

CH28382

Alteração do Documento

Criação do parâmetro “Considerar para filtro da Data de Lançamento do EFD PIS/COFINS”\.

06/03/2014

OS4751

Novo parâmetro

Criação de parâmetros para Considerar o Indicador no Código do Participante na geração dos registros

07/05/2015

OS4834

Novo parâmetro

Criação do parâmetro 0500 – Plano de Contas Contábeis

13/07/2015

CH23086\_2014

Alteração do Documento

Alterar título do parâmetro “Registros M200 e M600 \- Ordem de Desconto/Deduções da Contribuição do PIS/PASEP \- COFINS” para considerar os Registros ma e M500\.

26/11/2015

MFS\-1661

Criação de Parâmetro

Criar parâmetro “Considerar Código do Item com \(60 posições\)”

29/01/2016

MFS\-5400

Alteração de Regra

Alteração da regra do parâmetro ‘Manter todos os cadastros centralizados no Estabelecimento Matriz’

16/08/2016

MFS10591

Novo parâmetro

Criação do parâmetro para o registro F500/F510/F525/F550/F560 

24/08/2017

MFS15817

Alteração do Documento

RN30a: Inclusão de parâmetro na tela de Dados Iniciais para indicar a utilização da parametrização “Cadastro de Conta Contábil \(M400/M800\)” na geração do arquivo magnético da EFD Contribuições, registros M400 e M800

12/03/2018

MFS\-29136

Alteração de Regra

Alteração no parâmetro para seleção do plano de contas referencial

30/07/2019

MFS\-39412

Alteração de Regra

RN32: Inclusão da Versão 6\.00 do Plano de Contas Referencial

14/07/2020

MFS\-57866

Criação de Parâmetro

Criação do parâmetro para os registros 1100 e 1500, que vai indicar se os créditos com mais de 5 anos podem ser usados ou não\.  

05/03/2021

MFS\-69209

Alteração de Regra

RN32: Inclusão da Versão 7\.00 do Plano de Contas Referencial

20/07/2021

MFS\-82576

Alteração de Regra

RN32: Inclusão da Versão 8\.00 do Plano de Contas Referencial

22/03/2022

MFS\-82775

Criação de Parâmetro

Criação do parâmetro para o registro C100, para considerar notas fiscais de saídas canceladas \(Modelo 55\)\.  

28/03/2022

MFS\-84559

Criação de Parâmetro

Criação do parâmetro para os registros C100/C170/C191/C195, para GERAR notas fiscais de devolução de compras, posterior a Nota de Aquisição\.  

16/05/2022

MFS\-516736

Alteração de Regra

Inclusão da Versão 9\.00 do Plano de Contas Referencial – \(RN32\)

22/02/2023

MFS\-536991

Criação de Parâmetro

Criação do parâmetro para o registro C170, para gerar o Valor de exclusão de ICMS no Campo 15 \- VL\_ICMS do registro C170 de acordo MP nº 1\.159  

06/06/2023

MFS\-602684

Alteração de Regra

Inclusão da Versão 10\.00 do Plano de Contas Referencial – \(RN32\)

11/01/2024

MFS\- 605470

Criação de Parâmetro

Criação do parâmetro para o registro C500, para considerar o Valor de ICMS Não Escriturado no Campo 11 – VL\_ICMS\.  

19/02/2024

MFS\-751558

Rosemeire Santos

Inclusão da Versão 11\.00 do Plano de Contas Referencial – \(RN32\)

22/01/2025

MFS\-1037769

Lyene Benvenutti

Inclusão de novo parâmetro para gerar um registro 0100 para cada estabelecimento centralizado\.

10/02/2026

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN01__

Criar uma tela para parametrização de alguns dados gerais que serão necessários para a geração do arquivo\. Deverá ser feita inicialmente esta parametrização por estabelecimento, obedecendo à regra de geração centralizada, deve\-se parametrizar o Estabelecimento centralizador\. 

Localização: Grupo → Sped → EFD – Escrituração Fiscal Digital \- PIS/PASEP\-COFINS → Parâmetros à Dados Iniciais

OS3169\-GE

__RN02__

Configuração adicional dos Parâmetros:

__\[ALTERADA – CH23086\_2014\]__

__Parâmetro__

__Conteúdo__

__Multi\-Seleção__

__Registro 0110__

Nome: __Incidência Tributária no Período__

Conteúdo: Criar lista de valores conforme abaixo

1 – Escrituração de operações com incidência exclusivamente no regime não\-cumulativo

2 – Escrituração de operações com incidência exclusivamente no regime cumulativo

3 – Escrituração de operações com incidência nos regimes não\-cumulativo e cumulativo

Não

__Registro 0110__

Nome: __Método de Apropriação de Créditos__

Conteúdo: Criar lista de valores conforme abaixo

1 – Método de Apropriação Direta

2 – Método de Rateio Proporcional \(Receita Bruta\)

Não

__Registro 0110__

Nome: __Tipo de Contribuição Apurada no Período__

Conteúdo: Criar lista de valores conforme abaixo

1 – Apuração da Contribuição Exclusivamente a Alíquota Básica 

2 – Apuração da Contribuição a Alíquotas Específicas \(Diferenciadas e/ou por Unidade de Medida de Produto\)

Não

__Registro C010__

Nome: __Indicador da apuração, na escrituração das operações por NF\-e e ECF__ Conteúdo: Criar lista de valores conforme abaixo

1 – Apuração com base nos registros de consolidação das operações por NF\-e \(C180 e C190\) e por ECF \(C490\)

2 –  Apuração com base no registro individualizado de NF\-e \(C100 e C170\) e de ECF \(C400\)

Não

__Registros  F120 e F130__

Nome: __Tipo de Apresentação__

Conteúdo: Criar lista de valores conforme abaixo

\- Geração dos bens de forma individualizada

\- Geração por grupos de bens de mesma natureza ou destinação

Não

__Registro 0200__

Nome: __Utilizar a Descrição Detalhada do Produto__

Tipo: CheckBox

Não

__Registro 0200__

Nome: __Substituir o código do Serviço pelo Código da Natureza do Serviço __

Tipo: CheckBox

Não

__Registros A100/C100,C180 e C190__

Nomes: __Data de Emissão__ e__ Data de Lançamento EFD PIS/COFINS__

Tipo: Radio Button\.

Não

__Registros C600,C601 e C605__

Nome: __Geração com base nas informações da SAFX190 e SAFX191 __

Tipo: CheckBox

Não

__Registros D600,D601 e D605__

Nome: __Geração com base nas informações da SAFX161 e SAFX162__

Tipo: CheckBox

Não

__Registro F100__

Nomes: __Utilizar a parametrização do Tipo do Documento X CST/Operação/Nat\. Base de Crédito __e__ Utilizar a parametrização da Conta Contábil/Centro de Custo X CST/Operação/Nat\. Base de Crédto __

Tipo: Radio Button\.

Não

__Registro 410 e 810__

Nomes: __Utilizar a parametrização do Identificador da Natureza da Receita __e__ Utilizar a parametrização da Natureza da Receita informada no Documento Fiscal/Operação__

Tipo: Radio Button\.

Não

__Registros 0450, A110,C110,C500,D100 e D500__

Nomes: __Justificar a Direita __e__ Justificar a Esquerda __

Tipo: Radio Button\.

Não 

__Registros M100, M500, M200, M600 __

Nome: __Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS__

Tipo: CheckBox

Não

__Registro C100 – NF’s de Saídas Canceladas \- Modelo 55__

Nome: __Considerar Notas Fiscais de Saídas Canceladas – Modelo 55__

Tipo: CheckBox

Default: Desmarcado

Não

__Registro C100/C170 e C190 e Filhos – NF’s de Devolução de Compras__

Nome: __Gerar NF’s de Devolução de Compras – Posterior a NF’s de Entradas__

Tipo: CheckBox

Default: Marcado

Não

__Registro C170 – Exclusão de ICMS – Base de Cálculo PIS/COFINS__

Nome: __Gerar Valor de Exclusão no campo 15 \- VL\_ICMS do registro C170 de acordo MP nº 1\.159__

Tipo: CheckBox

Default: Desmarcado

Não

__Registro C500 – Considerar Valor de ICMS Não Escriturado__

Nome: __Considerar valor de ICMS Não Escriturado no Campo 11 \- VL\_ICMS\.__

Tipo: CheckBox

Default: Desmarcado

Não

OS3169\-GE

CH23086\_2014

__RN03__

Incluir na tela de __‘Dados Iniciais’__, localizada no __Módulo:__ SPED >> EFD – Escrituração Fiscal Digital – PIS/PASEP – COFINS   __Menu:__ Parâmetros, o parâmetro__ ‘Manter todos os cadastros centralizados no Estabelecimento Matriz’__\.

Este parâmetro por default deve estar desmarcado\.

OS3543

__RN04__

Se esta opção for marcada exibir a seguinte mensagem ao usuário: ”Marcando esta opção, se existir na base produtos com o mesmo código, porém em grupos distintos, o mesmo só será gerado uma única vez e embaixo do estabelecimento Matriz\.”

OS3543

__RN05__

Quando o parâmetro estiver marcado, o comportamento do sistema não será alterado\.

OS3543

__RN06__

Se o parâmetro ‘Manter todos os cadastros centralizados no Estabelecimento Matriz’ estiver desmarcado, o sistema deve comparar os cadastros usados pelo estabelecimento matriz e pelas filiais e informar os cadastros embaixo de cada registro 0140, considerando as regras abaixo:

Verificar se o produto que foi movimentado está cadastrado na matriz \(usando o critério de comparação: Grupo \+ Indicador \+ Código\), em caso afirmativo, mostrar abaixo do estabelecimento centralizador \(Matriz\)\.

Se o produto que foi movimentado estiver cadastrado apenas pelos estabelecimentos centralizados \(ou seja, não está cadastrado no estabelecimento matriz\), este produto deve constar abaixo do estabelecimento em questão e não na matriz \(usando o critério de comparação: Grupo \+ Indicador \+ Código\), mas exibindo apenas Indicador \+ Código no registro 0200\. 

Se o produto que foi movimentado estiver cadastrado para ambos os estabelecimentos, centralizado e centralizador \(ou seja, está cadastrado para os estabelecimentos matriz e filial\), este produto deve constar abaixo dos estabelecimentos em questão \(usando o critério de comparação: Grupo \+ Indicador \+ Código\), mas exibindo apenas Indicador \+ Código no registro 0200\.

Caso exista informações referente aos registros 0150,0190,0205,0206,0208,0400,0450 também deverão ser gerados abaixo do estabelecimento centralizado\.

A geração dos registros 0500 e 0600 não devem sofrer alteração\. Devem ser gerados SEMPRE abaixo do estabelecimento Centralizador\.

__IMPORTANTE: Não iremos incluir a exibição do grupo na geração do registro 0200, pois os clientes informam que este campo não faz parte do seu cadastro\. Por isso, se o cliente possuir em mais de um estabelecimento, produtos com o mesmo código, porém em grupos distintos o parâmetro ‘Manter todos os cadastros centralizados no Estabelecimento Matriz’, deve estar desmarcado\.__

OS3543

MFS\-5400

__RN07__

Inclusão do parâmetro ‘Regime de Tributação’, sendo os valores válidos: 1\- Lucro Real e 2 \-Lucro Presumido

OS3169\-GE25

__RN08__

Inclusão do parâmetro ‘Critério de escrituração e Apuração adotada’, sendo os valores válidos: 

1 – Regime de Caixa – Escrituração consolidada \(Registro F500\)

2 – Regime de Competência \- Escrituração consolidada \(Registro F550\)

9 – Regime de Competência \- Escrituração detalhada, com base nos registros dos Blocos “A”, “C”, “D” e “F”

OS3169\-GE25

__RN09__

Caso a opção do parâmetro ‘Regime de Tributação’ seja 2 \- Lucro Presumido e o parâmetro ‘Incidência Tributária no Período’, seja igual a ‘2 – Escrituração de operações com incidência exclusivamente no regime cumulativo’, habilitar o parâmetro ‘Critério de escrituração e Apuração adotada’\. Caso contrário, o campo ‘Critério de escrituração e Apuração adotada’ deve permanecer desabilitado\.

OS3169\-GE25

__RN10__

O parâmetro ‘Regime de Tributação’ deve ter como default a opção ‘1\- Lucro Real’\.

OS3169\-GE25

__RN11__

Na gravação da parametrização da tela de Dados Iniciais, se o usuário marcou a opção de ‘2 \-Lucro Presumido’ no parâmetro ‘Regime de Tributação’  e uma das opções  ‘1 – Escrituração de operações com incidência exclusivamente no regime não\-cumulativo’ ou ‘3 – Escrituração de operações com incidência nos regimes não\-cumulativo e cumulativo’, no parâmetro ‘Incidência Tributária no 

Período’, não gravar o registro e exibir a seguinte mensagem ao usuário: “O Regime de Tributação escolhido está incompatível com a opção informada no parâmetro Incidência Tributária no Período\. Favor rever a parametrização”

OS3169\-GE25

__RN12__

Inclusão do parâmetro ‘Critério do Detalhamento do Registro F525, quando a origem da Receita for Documentos Fiscais’, 

OS3169\-25CDW

__RN13__

O parâmetro ‘Critério do detalhamento do Registro F525, quando a origem da receita for documentos fiscais‘: terá as seguintes opções válidas: 

Clientes

Documento Fiscal

Item Vendido

OS3169\-25CDW

__RN14__

A opção Documento Fiscal será a default, quando o regime escolhido for Lucro Presumido e Regime Caixa\.	

OS3169\-25CDW

__RN15__

Se a opção for Lucro Real, o parâmetro ‘‘Critério do detalhamento do Registro F525, quando a origem da receita for documentos fiscais ‘deverá ficar desabilitado e nenhum texto deverá ser exibido\.

Se a opção for Lucro Presumido e o Critério de escrituração e Apuração adotada’, for uma das opções: 

2 – Regime de Competência \- Escrituração consolidada \(Registro F550\)

9 – Regime de Competência \- Escrituração detalhada, com base nos registros dos Blocos “A”, “C”, “D” e “F”

o parâmetro ‘‘Critério do detalhamento do Registro F525, quando a origem da receita for documentos fiscais ‘deverá ficar desabilitado e nenhum texto deverá ser exibido\.

OS3169\-25CDW

__RN16__

Se a opção for Lucro Presumido é obrigatório o preenchimento do parâmetro ‘Critério de escrituração e Apuração adotada’, caso contrário exibir a seguinte msg ao usuário:  “Favor preencher o Critério de escrituração e Apuração adotada”

OS3169\-25CDW

__RN17__

Retirar do parâmetro”Incidência Tributária no período “ a opção em branco\.

Caso este parâmetro não for preenchido, exibir a seguinte msg ao usuário: “Favor preencher a Incidência Tributária no período”\.

OS3169\-25CDW

__RN18__

Se o parâmetro ‘Critério do detalhamento do Registro F525, quando a origem da receita for documentos fiscais’ for preenchido com a opção ‘Item Vendido’ deve ser exibido a seguinte msg de alerta ao usuário: “ATENÇÃO: Usando este critério, se existir na base algum documento que foi recebido parcelado, poderá haver diferenças entre o valor da receita informado nos registros F500 e F525\.”

OS3169\-25CDW

__RN19__

Renomear o parâmetro ‘Critério do Detalhamento do Registro F525, quando a origem da Receita for Documentos Fiscais’, para ‘Critério do Detalhamento do Registro F525’

OS3169\-GE25C

__RN20__

Incluir o parâmetro ‘Notas Fiscais de Mercadoria Não Escrituradas’ na tela de Dados Iniciais no módulo SPED / EFD – Escrituração Fiscal Digital das Contribuições / Menu: Parâmetros\. 

Com a opção : Considerar na EFD\-Contribuições, os documentos de saída com classificação ‘7\-Notas Fiscais de Mercadoria não escrituradas’, desde que possuam CST´s de PIS e COFINS\.

OS3710

__RN21__

O parâmetro ‘Notas Fiscais de Mercadoria Não Escrituradas’ deve ficar desmarcado por default\.

OS3710

__RN22__

Quando marcado o parâmetro ‘Notas Fiscais de Mercadoria Não Escrituradas’, todas as notas de saída que possuírem na safx07 o campo 12 – cod\_class\_doc\_fis com ‘07’ e que possuírem valores nos campos ‘249 – COD\_SIT\_PIS’, ‘250 \- COD\_SIT\_COFINS’ \(da safx07\) ou ‘175\- COD\_SITUACAO\_PIS’ e ‘178 \- COD\_SITUACAO\_COFINS’ \(da SAFX08\), devem ser consideradas na recuperação dos dados para a geração dos registros \(C100,C170,C180,C181,C185,C188,C190,C191,C195,C198,C199,C380,C381,C385,C395,C396,C500,D100,D101,D105,D111,D200,D201,D205,D300,D309,D500,D501,D505,F500,F509,F510,F519,F525,F550,F559,F560,F569\), além de gerar os cadastros pertinentes a essas notas \(registros 0150,0190,0200,0205,0206,0208,0400,0450,0500 e 0600\) da EFD\-Contribuições\.

OS3710

__RN23__

Se desmarcado \(parâmetro ‘Notas Fiscais de Mercadoria Não Escrituradas’\), nada deve ser alterado, ou seja, as notas de saída com Classificação ‘7 – Notas Fiscais de Mercadoria não Escrituradas’, \(campo 12 da safx07\), não devem ser consideradas no EFD\-Contribuições\.

OS3710

__RN24__

Incluir o parâmetro ‘Registro A100,C100,C190,C395,C500,D100 e D500 – Seleção das Operações Geradoras de Créditos’ na tela de Dados Iniciais no  Módulo: SPED à EFD – Escrituração Fiscal Digital – PIS/PASEP/COFINS, Menu: Parâmetros , logo abaixo do parâmetro ‘Registro A100,C100,C180 e C190 – Seleção das Operações Geradoras de Receita’

OS4097

__RN25__

O parâmetro ‘Registro A100, C100,C190,C395,C500,D100 e D500 – Seleção das Operações Geradoras de Créditos’ terá o texto:

__\[ALTERAÇÃO – CH28382\]__

Inclusão do campo “Considerar para Filtro da Data de Lançamento do EFD PIS/COFINS” 

Drop Down com as opções: “Capa NF” e “Item NF” \(Defaul “Capa NF”\)\.

Caso selecionado a opção “Item NF” a seguinte mensagem será apresentada:

“Marcar esta opção como item NF, poderá acarretar perdas de performance e aumento no tempo de geração”

ATENÇÂO: Parâmetro exclusivo para documentos de entrada \(Operações Geradoras de Créditos\)\.

/ CH28382

__RN26__

Além do parâmetro acima, iremos manter na recuperação dos documentos, os registros com data de um mês posterior a data da geração do arquivo \(com base na data da emissão dos documentos\), desde que a data de Lançamento EFD PIS/COFINS esteja preenchida e compreendida no período da geração do meio magnético, ou seja, o range do filtro dos documentos será ‘X meses anterior a data da apuração \(conforme novo parâmetro na tela de Dados Iniciais\) \+ 1 mês posterior \(fixo na rotina\)\.

Esta informação será detalhada nos registros impactados pelo parâmetro \(A100, C100, C190, C395,C500,D100 e D500\)\.

OS4097

__RN27__

Incluir o parâmetro ‘Registro 0145 \- Regime de Apuração da Contribuição Previdenciária sobre a Receita Bruta’ na tela de ‘Dados Iniciais’ no Módulo: SPED à EFD – Escrituração Fiscal Digital – PIS/PASEP/COFINS, Menu: Parâmetros, logo abaixo do parâmetro ‘Registro 0110 – Regime de Apuração da Contrib\. Social e de Aprop\. de Crédito’

OS4165

__RN28__

Por default, a opção ‘Gerar o Registro 0145 centralizado no Estabelecimento Matriz’ do parâmetro ‘Registro 0145 \- Regime de Apuração da Contribuição Previdenciária sobre a Receita Bruta’ estará marcada\.

OS4165

__RN29__

Se o parâmetro ‘Registro 0145 \- Regime de Apuração da Contribuição Previdenciária sobre a Receita Bruta’, estiver desmarcado, será gerado um registro 0145 para cada estabelecimento que possui dados de P100 no período da geração do arquivo da EFD\-Contribuições\.

Se o parâmetro ‘Registro 0145 \- Regime de Apuração da Contribuição Previdenciária sobre a Receita Bruta’, estiver marcado e existir algum registro P100 na base durante o período da geração do arquivo \(para o estabelecimento centralizador ou qualquer descentralizado\) será gerado um único registro 0145 \(embaixo do estabelecimento centralizador\) no arquivo da EFD\-Contribuições\.  

Atenção: Considerar o documento matriz do bloco zero da EFD\-Contribuições, para maiores detalhes da geração do registro 0145\. 

OS4165

__RN30__

Incluir o campo “Código da SCP” na tela de Dados Iniciais, logo abaixo do campo “Estabelecimento”\. Este campo terá o formato padrão do Mastersaf DW com pasta de seleção e campo de texto para digitação do código\. Deverá acessar as informações da tabela SAFX2057\.

Este campo deverá ser chave, mas não obrigatório\.

No processo de implementação da OS4316\-C os registros existentes nesta tela devem ser atualizados com conteúdo nulo, de modo que não haja exclusão dos cadastros\.

OS4316\-C

__RN30a__

__Registro M400 e M800 – Critério de Identificação da Conta Contábil __

__Considerar a parametrização do cadastro de Conta Contábil \[M400/800\]__

Por default esse parâmetro virá desmarcado \(N\), mas estará disponível para seleção \(S\)\.

Se o parâmetro for marcado, o sistema deverá recuperar as contas contábeis cadastradas em: \(SPED > EFD – Escrituração Fiscal Digital das Contribuições > Parâmetros > Cadastro de Conta Contábil \(M400/M800\) para geração do arquivo magnético do PIS/CONFINS\.

MFS15817

__R31__

__Campo “Considerar o Indicador no Código do Participante”__

__Tipo__: Checkbox / __Valor default__: Marcado

Considerar a seguinte regra para a geração do campo COD\_PART no SPED\-Contribuições\.

Se marcado,

Identificação do Participante da SAFX04 à Indicador de Pessoa Física/Jurídica \+  "\-" \+ Código Pessoa Física/Jurídica

Se desmarcado,

Identificação do Participante da SAFX04 à Código Pessoa Física/Jurídica

OS4751

__RN32__

 “Registro 0500 – Plano de Contas Contábeis”

__Campo: “Versão do Plano Referencial” __

__Tipo:__ Dropdown / __Valor__ __default:__ Desabilitado

Este campo só será habilitado se o campo “Entidade Responsável pelo Plano Referencial” estiver preenchido\.

__\[ALTERAÇÃO MFS\-751558\]__ Inclusão da versão 11\.00 do Plano de Contas Referencial\.

__\[ALTERAÇÃO MFS\-602684\]__ Inclusão da versão 10\.00 do Plano de Contas Referencial

\[__ALTERAÇÃO MFS\-516736\]__ Inclusão da versão 9\.00 do Plano de Contas Referencial 

\[__ALTERAÇÃO MFS\-82576\]__ Inclusão da versão 8\.00 do Plano de Contas Referencial 

\[__ALTERAÇÃO\-MFS\-69209\]__ Inclusão do Plano de Contas Referencial 7\.00

A lista é composta pelos valores “1\.00”, “3\.00”, “4\.00”, “5\.00”, “6\.00”, “7\.00”, “8\.00”, “9\.00” e “10\.00”

Apresentar o valor default “6\.00”\.

Apresentar o valor default “7\.00”\.

\[__ALTERAÇÃO MFS\-82576\]__ Ao selecionar uma opção no campo ‘Entidade Responsável pelo Plano Referencial’, apresentar sempre a versão mais atual no campo “Versão do Plano Referencial”, porém, se o usuário desejar, ele pode alterar a versão\.

OS4834

MFS\-29136

MFS\-39412

MFS\-69209

MFS\-82576

MFS\-516736

   MFS\-602684

   __MFS\-751558__

__RN33__

“Registro 0500 – Plano de Contas Contábeis”

__Campo “Entidade Responsável pelo Plano Referencial”__

Tipo: Dropdown / __Valor__ __default:__ Habilitado / Campo Obrigatório

Deverá ser listada as seguintes opções:

1 \- PJ em Geral

2 \- PJ em Geral \- Lucro Presumido

3 – Financeiras

4 – Seguradoras

5 \- Imunes e Isentas em Geral

6 \- Financeiras \- Imunes e Isentas

7 \- Seguradoras \- Imunes e Isentas

8 \- Entidades Fechadas de Previdência Complementar

9 \- Partidos Políticos

00 – SUSEP

10 – Secretaria da Receita Federal

20 – Banco Central do Brasil \(COSIF\)  

Obs: Caso não preenchido exibir a seguinte mensagem: “Entidade Responsável pelo Plano Referencial” deve ser preenchida\.

OS4834

__RN34__

__Registro 0200 – Identificação do Item__

Campo: Considerar Código do Item com \(60 posições\)

Tipo:  Checkbox

Defaut: Desmarcado

Quando selecionado deverá considerar o código do item informado no campo “Produto \(60 posições\)” – Módulo: Básicos >> MastersafDW / Menu: Manutenção >> Códigos >> Produto\.

MFS\-1661

__RN35__

__Registro F500/F510/F525/F550/F560 \- Consolidação das Operações da P\.J\. Submetida ao Regime de Tributação com Base no Lucro Presumido __

Campo: Geração com base nas informações da SAFX183 e SAFX187 

Tipo:  Checkbox

Defaut: Desmarcado

Este campo somente será habilitado quando o Regime de Tributação for igual a “Lucro Presumido”\.

MFS\-10591

__RN36__

__Registros 1100/1500/1300/1700 \- Controle de Créditos/Retenções Fiscais – PIS/Pasep \- COFINS__

Campo: Utilizar os créditos superiores a 60 meses

Tipo:  Checkbox

Defaut: Desmarcado

MFS\-57866

__RN37__

__Registro C100 – NF’s de Saídas Canceladas \- Modelo 55__

Incluir na tela de __‘Dados Iniciais’__, localizada no __Módulo:__ SPED >> EFD – Escrituração Fiscal Digital – PIS/PASEP – COFINS   __Menu:__ Parâmetros, o parâmetro__ ‘Considerar Notas Fiscais de Saídas Canceladas – Modelo 55’__\.

Tipo:  Checkbox

Defaut: Desmarcado

MFS\-82775

__RN38__

__Registro C100/C170 e C190 e Filhos – NF’s de Devolução de Compras__

Incluir na tela de __‘Dados Iniciais’__, localizada no __Módulo:__ SPED >> EFD – Escrituração Fiscal Digital – PIS/PASEP – COFINS   __Menu:__ Parâmetros,  o parâmetro__ ‘Gerar NF’s de Devolução de Compras – Posterior a NF’s de Entradas’__\.

Tipo:  Checkbox

Defaut: Marcado

MFS\-84559

__RN39__

__Registro C170 – Valor de Exclusão de ICMS \- Base de Cálculo PIS/COFINS__

Incluir na tela de __‘Dados Iniciais’__, localizada no __Módulo:__ SPED >> EFD – Escrituração Fiscal Digital – PIS/PASEP – COFINS   __Menu:__ Parâmetros, o parâmetro__ ‘Gerar Valor de Exclusão no campo 15 \- VL\_ICMS do registro C170 de acordo MP nº 1\.159’__\.

Tipo:  Checkbox

Defaut: Desmarcado

MFS\- 536991

__RN40__

__Registro C500 – Valor de ICMS Não Escriturado – VL\_ICMS__

Incluir na tela de __‘Dados Iniciais’__, localizada no __Módulo:__ SPED >> EFD – Escrituração Fiscal Digital – PIS/PASEP – COFINS   __Menu:__ Parâmetros, o parâmetro__ ‘Considerar valor de ICMS Não Escriturado no Campo 11 \- VL\_ICMS\.’__\.

Tipo:  Checkbox

Defaut: Desmarcado

MFS\- 605470

__RN41__

__Registro 0100 – Dados do Contabilista__

Criar uma nova subseção “Registro 0100 – Dados do Contabilista” na seção “Bloco 0”\.

Incluir um novo parâmetro na subseção 0100 “Considerar todos os estabelecimentos centralizados na geração do registro 0100\.” 

 

Tipo: Checkbox

Defaut: Desmarcado

MFS\-1037769


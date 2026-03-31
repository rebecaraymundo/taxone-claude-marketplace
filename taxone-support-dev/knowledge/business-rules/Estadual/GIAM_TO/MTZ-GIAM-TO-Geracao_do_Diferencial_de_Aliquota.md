# MTZ-GIAM-TO-Geracao_do_Diferencial_de_Aliquota

- **Fonte:** MTZ-GIAM-TO-Geracao_do_Diferencial_de_Aliquota.docx
- **Modificado:** 2021-01-13
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Módulo GIAM \- TO

Geração do Diferencial de Alíquota para o Segmento P

__Localização__: Menu Estadual, Módulo: GIAM – TO, menu Obrigação 🡪 Diferencial de Alíquota 🡪 Geração

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS6415

Alterações da GIAM\-TO p/a vrs\. 10\.0 \(Portaria n\. 748, de 17/08/2016\)

Alteração da geração do diferencial de alíquota para armazenar o valor da alíquota utilizada no cálculo\.

07/10/2016

\(criação do documento\)

MFS47324

Alteração na consolidação dos valores e gravação do campo Alíquota

Pontos para correção na geração:

\- Gravar o campo alíquota origem e não mais a diferença entre  alíquotas origem e destino\.

\- Totalizar os valores Contabil, Base e Imposto por UF e alíquota origem, gravando na tabela os resultado segregado por UF e alíquota

Alteração tem aval do Setor de Informação,que participou de call com o cliente BRK em 04/12/2020\.

04/12/2020

MFS48937

Andréa Rocha

Alteração da tabela usada para a recuperação dos dados do diferencial de alíquota\.  A tabela que será usada será a nova tabela do cálculo por UF e Alíquota, criada especificamente para a GIAM\-TO\.

13/01/2020

Sumário

[1\.	Regras Gerais	2](#_Toc463618929)

[2\.	Recuperação dos Dados	2](#_Toc463618930)

[3\.	Processamento	2](#_Toc463618931)

[4\.	Gravação dos Dados	2](#_Toc463618932)

# <a id="_Toc463618929"></a>Regras Gerais

__\[MFS48937\] Recuperação dos dados de uma nova tabela do cálculo do diferencial de alíquota por UF/Alíquota__

Anteriormente a GIAM\-TO usava a tabela ICT\_DIF\_ALIQ gravada na rotina de cálculo do diferencial de alíquota gerada na Apuração do ICMS, mas foi identificada uma situação em que era necessário gravar os dados por UF e Alíquota para a geração da GIAM\-TO, por isso está sendo criada uma nova tabela \(ICT\_DIF\_ALIQ\_DET\)\. A nova tabela também vai ser gravada na rotina de cálculo do diferencial de alíquota\.

Esta geração recupera os dados da tabela do diferencial de alíquotas \(ICT\_DIF\_ALIQ\_DET\), gerada na Apuração do ICMS, e grava as informações numa tabela auxiliar\. Estes dados serão posteriormente utilizados na geração do meio magnético da GIAM\- TO para o Segmento P\.

# <a id="_Toc463618930"></a>Recuperação dos Dados

# <a id="_Toc463618931"></a>Processamento 

# <a id="_Toc463618932"></a>Gravação dos Dados 

Alteração da __MFS6415__: Inclusão do valor da diferença entre as alíquotas origem x destino na tabela da GIAM\-TO 

Alteração da __MFS47324__: considerar a alíquota de origem no grupamento para consolidação dos valores e na gravação da tabela auxiliar \(EST\_TO\_DIF\_ALIQ\_UF\) da GIAM\-TO\.

Recuperar os registros da tabela do diferencial de alíquotas \(ICT\_DIF\_ALIQ\_DET\) gerada na Apuração do ICMS, com os seguintes critérios:

\- Empresa de login

\- Estabelecimento selecionado na tela de geração

\- Tipo de Livro informado na tela de geração

\- Período da Apuração = útimo dia do Mês/Ano informado na tela de geração

Recuperar os valores \(Valor Contábil, Base de Cálculo e Diferencial de Alíquota\) consolidados por UF e Alíquota de Origem \[__MFS47324\]__

Gravar os registros na tabela auxiliar \(EST\_TO\_DIF\_ALIQ\_UF\), conforme abaixo:

- Cod\_Empresa: preencher com o código da empresa de login;
- Cod\_Estab: preencher com o código do estabelecimento;
- Mes\_Ref: preencher com mês informado na tela de geração;
- Ano\_Ref: preencher com o ano informado na tela de geração;
- Cod\_Tipo\_Livro: preencher com o código do tipo do livro informado na tela de geração;
- Ident\_Estado: preencher com o Identificador da UF recuperado da tabela ICT\_DIF\_ALIQ;
- Ind\_Tp\_Dom\_Fiscal: preencher fixo com “A”;
- Vlr\_Contabil preencher com o Valor Contábil recuperado da tabela ICT\_DIF\_ALIQ;
- Vlr\_Base\_Calc: preencher com Valor da Base de Cáculo recuperado da tabela ICT\_DIF\_ALIQ;
- Vlr\_Dif\_Aliq: preencher com o Valor do Diferencial de Alíquota recuperado da tabela ICT\_DIF\_ALIQ;
- Aliq\_diferenca: preencher com a diferença entre a alíquota no estado de origem e a alíquota do estado de destino\. Esta informação conta na tabela do diferencial de alíquotas \(ICT\_DIF\_ALIQ\): coluna VLR\_DIF\_ALIQ __*ou*__ \( coluna VLR\_ALIQ\_ORIG – coluna VLR\_ALIQ\_DEST \), dependendo se o VLR\_DIF\_ALIQ estiver ou não preenchido\.
- Aliq\_diferença: __\[MFS47324\]__ preencher com a alíquota no estado de origem, campo  VLR\_ALIQ\_ORIG da tabela ICT\_DIF\_ALIQ;
- Ind\_Dig\_Calc: preencher com 2

= = = = = =


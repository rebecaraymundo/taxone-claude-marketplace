# MTZ-OTF-Portaria_63

- **Fonte:** MTZ-OTF-Portaria_63.docx
- **Modificado:** 2020-08-31
- **Tamanho:** 32 KB

---

# Portaria 63 – Geração do MANAD

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS 2475

Gerar MANAD para autônomo

*Para que os dados de autônomos sejam contemplados nos registros da MANAD, utilizando o cadastro de Pessoa Física e Jurídica\(SAFX04 \), e o Item  de Serviço\( SAFX09\)\. O objetivo é a geração do meio magnético MANAD corretamente com as informações dos autônomos\.*

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

Este campo será fixo com o seguinte conteúdo __“K001”__

OS2475

__RN02__

Caso o Flag na tela de Geração do Arquivo magnético estiver marcado, o sistema verifica se no período especificado se existe notas fiscais de autônomos \(__ RN03 __\):

      \- se sim o sistema deverá informar o conteúdo __“0“__ \( Bloco com dados informados \)

      \- caso contrário o sistema deverá informar o conteúdo __“1”__ \( Bloco sem dados informados \)

Caso o Flag na tela de Geração do Arquivo magnético não estiver marcado, não selecionar notas fiscais de autônomos\.

OS2475

__RN03__

O sistema verifica as Notas fiscais da SAFX07 de serviço com o Class\. Doc Fiscal = “2” ou “3, campo 12 da tabela SAFX07 relacionada com o cadastro da pessoa física/jurídica na SAFX04 se o campo de dados de autônomos está preenchido\.

Caso contrário não gerar meio magnético com informações de autônomo\.

OS2475

__RN04__

Este campo será fixo com o seguinte conteúdo __“K050”__

OS2475

__RN05__

O sistema deverá recuperar a informação do campo “__Cadastro Específico INSS\- CEI” __do box “Atendimento à Portaria 63” da tela, campo “CEI\_PORT63” da tabela Estabelecimento, caso o campo esteja vazio, o sistema deve recuperar a informação do campo “CNPJ” da tela,  campo “CGC”__  __da tabela “Estabelecimento”

OS2475

__RN06__

O sistema deverá recuperar a informação do campo __“Início Validade” __da tela; item 03, campo “DATA\_04” da tabela SAFX04, quando estiver preenchido os dados de autônomo no Cadastro de pessoa Física/Jurídica e a pessoa Física/Jurídica cuja a data dos documentos de serviços esteja dentro do período informado\.

OS2475

__RN07__

O sistema deverá recuperar a informação do campo __“Pessoa Física/Jurídica”__  da tela; item 02, campo “COD\_FIS\_JUR” da tabela SAFX04, quando estiver preenchido os dados de autônomo no Cadastro de pessoa Física/Jurídica e a pessoa Física/Jurídica cuja a data dos documentos de serviços esteja dentro do período informado\.\.

OS2475

__RN08__

O sistema deverá recuperar a informação do campo __“CPF/CNPJ”__ da tela; item 06, campo “CPF\_CGC”__ __da tabela SAFX04, quando estiver preenchido os dados de autônomo no Cadastro de pessoa Física/Jurídica e a pessoa Física/Jurídica cuja a data dos documentos de serviços esteja dentro do período informado\.

OS2475

__RN09__

O sistema deverá recuperar a informação do campo __“Nr\. PIS/PASEP/NIT” __ da tela; item 35, campo “PIS\_PASEP” da  tabela SAFX04, quando estiver preenchido os dados de autônomo no Cadastro de pessoa Física/Jurídica e a pessoa Física/Jurídica cuja a data dos documentos de serviços esteja dentro do período informado\.

OS2475

__RN10__

O sistema deverá recuperar a informação do campo __“Categoria” do box “ __da tela; item 36, campo “CATEGORIA\_TRAB” dos Dados do Autônomo” na tabela SAFX04, quando estiver preenchido os dados de autônomo no Cadastro de pessoa Física/Jurídica e a pessoa Física/Jurídica cuja a data dos documentos de serviços esteja dentro do período informado\.

OS2475

__RN11__

O sistema deverá recuperar a informação do campo __“Razão Social” __da tela; item 05, campo “RAZAO\_SOCIAL” da  tabela da SAFX04, quando estiver preenchido os dados de autônomo no Cadastro de pessoa Física/Jurídica e a pessoa Física/Jurídica cuja a data dos documentos de serviços esteja dentro do período informado\.

OS2475

__RN12__

O sistema deverá recuperar a informação do campo __“Data de Nascimento” __da tela; item e campo a serem criados na tabela SAFX04, quando estiver preenchido os dados de autônomo no Cadastro de pessoa Física/Jurídica e a pessoa Física/Jurídica cuja a data dos documentos de serviços esteja dentro do período informado\.

OS2475

__RN13__

Este campo será fixo com conteúdo __vazio__\.

OS2475

__RN14__

Este campo será fixo com conteúdo __vazio__\.

OS2475

__RN15__

Este campo será fixo com conteúdo __“8”__  \(Contribuintes Individuais\)

OS2475

__RN16__

Este campo será fixo com conteúdo __vazio__\.

OS2475

__RN17__

Este campo será fixo com conteúdo __vazio\.__

OS2475

__RN18__

Este campo será fixo com conteúdo __vazio\.__

OS2475

__RN19__

Este campo será fixo com o seguinte conteúdo __“K100”__

OS2475

__RN20__

O sistema deverá recuperar a informação do campo __“Início de validade”__ da tela; item 02, campo ‘DATA\_X2037” da tabela da SAFX2037 do setor encontrado na SAFX03\. O setor deverá estar na SAFX03, cuja notas devem estar relacionadas com a  SAFX07 dentro do período informado\.

OS2475

__RN21__

O sistema deverá recuperar a informação do campo __“Setor”__  da tela, campo a ser incluído na SAFX03; item 01, campo “COD\_SETOR” tabela SAFX2037\. O setor deverá estar na SAFX03, cuja notas devem estar relacionadas com a  SAFX07 dentro do período informado\.

OS2475

__RN22__

O sistema deverá recuperar a informação do campo __“Descrição”__ da SAFX2037 do setor encontrado na SAFX03\. O setor deverá estar na SAFX03, cuja notas devem estar relacionadas com a  SAFX07 dentro do período informado\.

OS2475

__RN23__

Este campo será fixo com conteúdo __vazio\.__

OS2475

__RN24__

Este campo será fixo com o seguinte conteúdo __“K150”\.__

OS2475

__RN25__

O sistema deverá recuperar a informação do campo __“Inicio de Validade”__ do campo verba da tela de Geração da Portaria 63; item 02, campo “DATA\_X2023” da tabela SAFX2023\. 

OS2475

__RN26__

O sistema deverá recuperar a informação \( Código \)  do campo __“Verba”__ referente a verba da tela de Geração da Portaria 63; item 01, campo “COD\_VERBA” da tabela SAFX2023\.

OS2475

__RN27__

O sistema deverá recuperar a informação do campo __“Descrição da Verba”__  da tela de Geração da Portaria 63; item 04, campo “DESCRIÇÃO” da tabela SAFX2023\.

OS2475

__RN28__

Este campo será fixo com o seguinte conteúdo __“K200”__

OS2475

__RN29__

O sistema deverá recuperar a informação do campo __“Inicio da validade”__  da tela; item 03, campo “DATA\_X04”  da tabela SAFX04, quando estiver preenchido os dados de autônomo no Cadastro de pessoa Física/Jurídica e a pessoa Física/Jurídica cuja a data dos documentos de serviços estejam dentro do período informado\.

OS2475

__RN30__

O sistema deverá recuperar a informação \( Código \) do campo __“Verba”__ da tela de Geração da Portaria 63; do item 01, campo “COD\_VERBA” da tabela SAFX2023\.

OS2475

__RN31__

O sistema deverá recuperar a informação \( Código \) do campo __“Setor”__ da tela da SAFX03; item 01, campo “COD\_SETOR”  da tabela SAFX2037\. O setor deverá estar na SAFX03, cuja notas estão relacionadas com a  SAFX07 dentro do período informado\.

OS2475

__RN32__

O sistema deverá recuperar a informação \( Código \) do campo __“Centro de Custos”__ da  tela SAFX03; item 01, campo “COD\_CUSTO”  da tabela SAFX 2003\. O centro de custos deverá estar na SAFX03, cuja notas devem estar relacionadas com a  SAFX07 dentro do período informado\.

OS2475

__RN33__

O sistema deverá recuperar a informação \( Código \) do campo __“Conta”__ da tela SAFX03\. A conta deverá estar na SAFX03, cuja notas devem estar relacionadas com a  SAFX07 dentro do período informado\.

OS2475

__RN34__

Este campo será fixo com o seguinte conteúdo __“K250”__

OS2475

__RN35__

Este campo será fixo com o seguinte conteúdo __“6”__

OS2475

__RN36__

O sistema deverá recuperar o campo __“Setor”__ da SAFX03; item 01, campo “COD\_SETOR”  da tabela SAFX2037\. O setor deve estar na SAFX03, cuja notas devem  estar relacionados com a SAFX07 dentro do período informado\.

OS2475

__RN37__

O sistema deverá recuperar a informação do campo __“Pessoa Física/Jurídica”__  da tela; item 02, campo “COD\_FIS\_JUR” da tabela SAFX04, quando estiver preenchido os dados de autônomo no Cadastro de pessoa Física/Jurídica e a pessoa Física/Jurídica cuja a data dos documentos de serviços estejam dentro do período informado\.\.

OS2475

__RN38__

O sistema deverá recuperar a informação do campo __“Data de emissão”__ da SAFX07, no formato “MM/AAAA\.;item 11, campo “DATA\_EMISSAO”, cuja data dos documentos de serviços estejam dentro do período informado\.

OS2475

__RN39__

O sistema deverá recuperar a informação __“Data de Pagamento”__ da SAFX07, no formato “DD/MM/AAAA\.; item 175, campo “DT\_PAGTO\_NF” da tabela SAFX07, cujo documentos de serviços estejam dentro do período informado\.

OS2475

__RN40__

O sistema deverá recuperar a informação \( Código \) do campo __“CBO“__ do box Dados do Autônomo” na tela SAFX04; item 34, campo “COD\_CBO” da tabela SAFX04, cuja pessoa Física/jurídica esteja relacionado com documentos de serviços que devem estar dentro do período informado\.

OS2475

__RN41__

O sistema deverá recuperar a informação\( Código \)  do campo __“Ocorrência”__ do box “ Dados do Autônomo” da tela  SAFX04; item 37, campo “OCORRENCIA\_TRAB” da tabela SAFX04, cuja pessoa Física/jurídica esteja relacionado com documentos de serviços que devem estar dentro do período informado\.

OS2475

__RN42__

O sistema deverá recuperar a informação\( Código \) do campo __”Função”__ da tela SAFX04 campo a ser incluído; item  01, campo “COD\_FUNCAO” da tabela SAFX2036, cuja pessoa Física/jurídica esteja relacionado com documento de serviço que devem estar dentro do período informado\.

OS2475

__RN43__

O sistema deverá recuperar a informação do campo __”Incide Imposto de Renda”__  campo a ser incluído na tela da SAFX04, cuja pessoa Física/jurídica esteja relacionado com documento de serviço estejam dentro do período informado\.

OS2475

__RN44__

O sistema deverá recuperar a informação do campo __“Incide  Salário Família__” campo a ser incluído na tela da SAFX04, cuja pessoa Física/jurídica esteja relacionado com documento de serviço estejam dentro do período informado\.

OS2475

__RN45__

O sistema deverá recuperar a informação do campo __“Valor Total da Nota”__ da SAFX07, cujo documentos de serviços estejam dentro do período informado\.

Caso o valor seja zero, informar  no campo igual a zeros\.

Item  23, campo VLR\_TOT\_NOTA da tabela  SAFX07\.

Obs: Essa informação será recuperada do campo de Valor Total da Nota, pois este é o mesmo valor informado no campo Receita Bruta \(safx53\) e é utilizado como Base de Cálculo para o IR\.

OS2475

__RN46__

O sistema deverá recuperar a informação do campo “__Base INSS”__ da tela SAFX07; item 85, campo “VLR\_BASE\_INSS”, cujos documentos de serviços estejam dentro do período informado\.

OS2475

__RN47__

Este campo será fixo com o seguinte conteúdo __“K300”__

OS2475

__RN48__

Este campo será fixo com o seguinte conteúdo __“6”__

OS2475

__RN49__

O sistema deverá recuperar a informação do campo __“Setor”__ da SAFX03; item 01, campo “COD\_SETOR”  da tabela SAFX2037\. O setor deve estar na SAFX03, cujo documentos estejam relacionados com a SAFX07 dentro do período informado\.

OS2475

__RN50__

O sistema deverá recuperar a informação do campo __“Pessoa Física/Jurídica”__  da tela; item 02, campo “COD\_FIS\_JUR” da tabela SAFX04, quando estiver preenchido os dados de autônomo no Cadastro de pessoa Física/Jurídica e a pessoa Física/Jurídica cuja data dos documentos de serviços estejam dentro do período informado\.\.

OS2475

__RN51__

O sistema deverá recuperar a informação do campo __“Data de emissão”__ da SAFX07, no formato “MM/AAAA; item 11, campo “DATA\_EMISSAO” da tabela SAFX07, cujo documentos estejam relacionados com a SAFX07 dentro do período informado\.

OS2475

__RN52__

O sistema deverá recuperar a informação \( Código \) do campo __“Verba”__  da tela de Geração da Portaria 63; do item 01, campo “COD\_VERBA” da tabela SAFX2023\.

OS2475

__RN53__

O sistema deverá totalizar os valores do campo “ Valor total” \( campo 15 da SAFX09\) de todos os itens do documento de Serviço, cujo documentos estejam dentro do período informado\.

OS2475

__RN54__

Este campo será fixo com o seguinte conteúdo __“P”__

OS2475

__RN55__

Este campo será fixo com o seguinte conteúdo __“9”__

OS2475

__RN56__

Este campo será fixo com o seguinte conteúdo __“9”__

OS2475

__RN57__

Este campo será fixo com o seguinte conteúdo __“K990”__

OS2475

__RN58__

O sistema deverá somar todas as linhas do bloco e exibir a Quantidade Total neste campo\.

OS2475

__RN59__

Inclusão de campo no Cadastro de Pessoa Física/Jurídica \( SAFX04 \):

*🡺 Data de Nascimento, campo tipo Data – dd/mm/aa, valores iniciais são zeros\.*

OS2475

__RN60__

Inclusão de campo no Cadastro de Pessoa Física/Jurídica \( SAFX04 \):

*🡺 Dependentes:*

- *Incide Imposto de Renda,campo do tipo Numérico com 2 posições \-  99, valores iniciais são zeros\.*
- *Incide Salário Família, campo to tipo numérico com 2 posições – 99, valores iniciais são zeros\.*

OS2475

__RN61__

Inclusão de campo no Cadastro de Pessoa Física/Jurídica \( SAFX04 \):

*🡺 Função, campo relacionada com a tabela SAFX2036, exibir a descrição da função com 20 caracteres\.*

*Valores iniciais em branco\.*

OS2475

__RN62__

Incluir um campo com o nome de “Setor” na SAFX03 \.

*🡺 Setor, campo relacionada com a  tabela SAFX2037, exibir a descrição do setor com 40 caracteres\.*

OS2475

__RN63__

Incluir na Tela de Geração do Meio Magnético o seguinte campo:

*🡺 Gerar para Autônomo, campo tipo check box, caso estiver marcado, habilitar  o campo verba para digitação de valores, caso contrário desabilitar o campo verba, não permitindo a digitação dos dados\.*

*🡺 Verba, campo relacionada com a tabela SAFX 2023, exibir o código, validade e descrição\.*

*\- Código, campo do tipo alfanumérico com 6 caracteres \( item 01 da tabela, o nome do campo é  cód\_verba\)\.*

*\- Validade, campo do tipo data, 8 posições \( item 02 da tabela, o nome do campo  é data\_x2023 \)\.*

*\- Descrição, campo do tipo alfanumérico \( item 04 da tabela, o nome do campo é descrição\. \) Exibir somente  20 caracteres\.*

OS2475


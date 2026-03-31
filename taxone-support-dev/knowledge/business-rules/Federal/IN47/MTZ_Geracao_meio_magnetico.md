# MTZ_Geracao_meio_magnetico

- **Fonte:** MTZ_Geracao_meio_magnetico.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 74 KB

---

THOMSON REUTERS

IN47

Geração do Meio Magnético

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-1864

Geração Meio Magnético

Geração Meio Magnético da IN47

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN\-00

Regra geral para geração do arquivo magnético

A forma para apresentação do arquivo da IN47 deve apresentar a seguinte sequencia

Registro 1 = cabeçalho do período atual

Registro 2 = linhas com movimentação do período atual

Registro1 = cabeçalho do mesmo período do ano anterior

Registro 2 linhas com movimentação do mesmo período do ano anterior

Ex:

100068051600012404201401546  
2HIGIENE PESSOAL   3304999002000090221444064000000045348446000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000  
2COSMETICOS          3305900001000024316514200000000230193412000000016081829000000000000000000000000000000000000000000000000000000000000000000000000000  
100068051600012404201301565  
2HIGIENE PESSOAL   3304999002000011670140302000000645372096000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000  
2COSMETICOS          3305900001000021454391510000000219538084000000015351162000000000000000000000000000000000000000000000000000000000000000000000000000  
2HIGIENE PESSOAL   3304999001000002602029060000000008642935000000001036237000000000000000000000000000000000000000000000000000000000000000000000000000

Desta forma a geração deverá buscar as regras abaixo para o período do bimestre informado na geração para compor o arquivo e logo depois de terminar de executar esta geração deverá repetir a mesma operação porem para o mesmo bimestre do ano anterior, alocando os registros na sequência do último registro da linha do período atual\.

O arquivo gerado será do tipo texto de largura fixa\. Os campos do Numérico serão alinhados com zeros à esquerda e os de tipo Alfa, serão alinhados à esquerda e com espaços a direita\.

Será gerado um arquivo para cada estabelecimento selecionado na tela de geração, sendo salvo com a nomenclatura: PROCESSO\_ESTAB\_BIMESTRE\_ANO, sendo que o processo é opcional, conforme parâmetro da tela de framework\.

Existira a aba de relatório demonstrando as informações de geração do relatório\.

MFS\-1864

__Registro 1__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN01\-00

Seleção

- __Origem das informações__: Tela de Geração do Meio Magnético e Cadastro de Estabelecimentos
- __Regra de seleção__: Serão consideradas informações do cadastro do estabelecimento selecionado no momento da geração do meio magnético\. Será gerado um registro “1” com as informações do Bimestre parametrizado na geração e outro com Data do mesmo Bimestre no ano anterior\.
- __Campos\-chave__: CNPJ, Bimestre e Ano 
- __Ordenação__: Ordenar pelo campo Ano, demonstrando informações do ano parametrizado e na sequência informações do ano imediatamente anterior\.
- __Agrupamento__: CNPJ, Bimestre e Ano

MFS\-1864

RN01\-01

Campo 1 Registro

O campo 1 Registro é fixo com a informação “1”

MFS\-1864

RN01\-02

Campo 2 CNPJ

O campo 2 CNPJ deverá ser buscado no campo CGC da tabela ESTABELECIMENTOS relacionado ao estabelecimento escolhido na tela de geração do Meio Magnético\.

MFS\-1864

RN01\-03

Campo 3 Bimestre

O campo 3 Bimestre deverá ser o parametrizado na tela de Geração do Meio Magnético

MFS\-1864

RN01\-04

Campo 4 Ano

O campo 4 ANO deverá ser buscado na tela de Geração do Meio Magnético\.

Quando se tratar do registro 1 referente ao ano anterior \(vide regra geral\)

MFS\-1864

RN01\-05

Campo 5 Quantidade de Funcionários

O campo 5 Quantidade de Funcionários deverá ser buscado na tela de Geração do Meio Magnético\.

Quando for o registro “1” com informações do período parametrizado, considerar o valor informado no campo “Quantidade de Funcionários \(Ano de Geração\)”\. Se for o registro do ano anterior, considerar o informado no campo “Quantidade de Funcionários \(Ano Anterior\)”\.

MFS\-1864

__Registro 2__

###### __CÓD__

###### __DESCRIÇÃO__

###### __OS/CH__

RN02\-00

Seleção

- __Origem das informações__: Itens de Mercadoria \(SAFX08\)
- __Regra de seleção__: Serão considerados registros da tabela de Itens de Mercadoria \(SAFX08\) do estabelecimento parametrizado na tela de geração, cuja Data Fiscal compreenda o Bimestre informado na tela de geração, cuja NF não seja cancelada \(informação da capa – SAFX07\) e que tenha o CFOP \(COD\_CFO\) informado na parametrização de “Definição de Movimentos”, do módulo IN47/2000, e que o Código NCM \(COD\_NBM\) ou Produto \(IND\_PRODUTO \+ COD\_PRODUTO\) informados nas telas vinculadas a parametrização de “Identificador da Categoria de Produtos” \(considerar primeiro NCM e depois Produto\)\.

Este registro será gerado na sequência do Registro “1”\. Após a conclusão da geração dos movimentos do bimestre parametrizado na tela de geração, será gerado um novo registro “1” com referência ao mesmo bimestre, porém, do ano anterior\. Neste caso, também devem ser gerados quantos registros do tipo “2” forem necessários para demonstrar as movimentações do ano anterior\. Neste contexto, a regra de seleção se mantém a mesma, com a exceção do ano de seleção que será o ano imediatamente anterior ao parametrizado na geração\.

- __Campos\-chave__: Campo 3 – Classificação Fiscal
- __Ordenação__: Campo 2 – NCM – Nome Comum de Mercadoria e Campo 3 – Classificação Fiscal
- __Agrupamento__: Campo 3 – Classificação Fiscal

O Registro “2” é composto pelas linhas do arquivo, e contém as atividades econômicas da empresa\.

As informações destes registros terão sua origem na SAFX08 e SAFX2013\.

MFS\-1864

RN02\-01

Campo 1 Registro

O campo 1 Registro é fixo com a informação “2”

MFS\-1864

RN02\-02

Campo 2 NCM \- Nome Comum de Mercadoria

Este campo será gerado com a descrição do conteúdo parametrizado no campo “Tipo de Produto” das telas de Parametrização por NCM ou Parametrização por Produto, que pode ser:

Higiene Pessoal

Cosméticos

Perfumaria

MFS\-1864

RN02\-03

Campo 3 Classificação Fiscal

Será gerado com o conteúdo do campo Código NBM \(COD\_NBM\) da SAFX08\.

MFS\-1864

RN02\-04

Campo 4 Valor Total de Mercadoria para Mercado Interno

Este campo irá somar os Valores do Produto \(VLR\_ITEM\) da SAFX08, considerando registros que tenham CFOP\(s\) parametrizados pelo usuário no seguinte caminho: Parâmetros >  Definição dos Movimentos, e que estes CFOP\(s\) estejam associados ao Parâmetro “1 – Saídas Mercado Interno”\.

Será gerado com 2 decimais, que serão as duas últimas posições do campo\.

MFS\-1864

RN02\-05

Campo 5 Valor de IPI para Mercado Interno

Este campo irá somar os Valores do IPI \(VLR\_IPI\) da SAFX08, considerando registros que tenham CFOP\(s\) parametrizados pelo usuário no seguinte caminho: Parâmetros >  Definição dos Movimentos, e que estes CFOP\(s\) estejam associados ao Parâmetro “1 – Saídas Mercado Interno”\.

Será gerado com 2 decimais, que serão as duas últimas posições do campo\.

MFS\-1864

RN02\-06

Campo 6 Quantidade Total para Mercado Externo

Este campo irá somar os valores do campo Quantidade \(QUANTIDADE\) da SAFX08, considerando registros que tenham CFOP\(s\) parametrizados pelo usuário no seguinte caminho: Parâmetros >  Definição dos Movimentos, e que estes CFOP\(s\) estejam associados ao Parâmetro “2 – Saídas Mercado Externo”\.

Este campo deve refletir a soma das quantidades em Toneladas\. Para isso, verificar, por item selecionado, se a Unidade de Medida Comercial \(COD\_MEDIDA\) é igual a Unidade de Medida \(Tonelada\) informada na tela de geração\. Se for igual, não há necessidade de conversão\. Se for diferente, a quantidade a ser considerada será a convertida conforme Fator de Conversão informado na tela de Parâmetros de Conversão de Unidades de Medida Padrão \(Módulo MasterSAF DW / Menu Manutenção > Cadastros > Conversão de Unidades de Medida > Padrão\)\. A quantidade a ser somada será aquela resultado do cálculo: Quantidade \* Fator de Conversão, considerando o registro que tenha a Unidade Origem igual a informada no Item selecionado e a Unidade Destino igual a parametrizada na tela de geração\.

Será gerado com 4 decimais, que serão as 4 últimas posições do campo\.

 

MFS\-1864

RN02\-07

Campo 7 Valor Total de Mercadoria para Mercado Externo

Este campo irá somar os Valores do Produto \(VLR\_ITEM\) da SAFX08, considerando registros que tenham CFOP\(s\) parametrizados pelo usuário no seguinte caminho: Parâmetros >  Definição dos Movimentos, e que estes CFOP\(s\) estejam associados ao Parâmetro “2 – Saídas Mercado Externo”\.

Será gerado com 2 decimais, que serão as duas últimas posições do campo\.

MFS\-1864

RN02\-08

Campo 8 Valor Total de IPI para Mercado Externo

Este campo irá somar os Valores do IPI \(VLR\_IPI\) da SAFX08, considerando registros que tenham CFOP\(s\) parametrizados pelo usuário no seguinte caminho: Parâmetros >  Definição dos Movimentos, e que estes CFOP\(s\) estejam associados ao Parâmetro “2 – Saídas Mercado Externo”\.

Será gerado com 2 decimais, que serão as duas últimas posições do campo\.

MFS\-1864

RN02\-09

Campo 9 Quantidade Total de Importações

Este campo irá somar os valores do campo Quantidade \(QUANTIDADE\) da SAFX08, considerando registros que tenham CFOP\(s\) parametrizados pelo usuário no seguinte caminho: Parâmetros >  Definição dos Movimentos, e que estes CFOP\(s\) estejam associados ao Parâmetro “3 – Importação”\.

Este campo deve refletir a soma das quantidades em Toneladas\. Para isso, verificar, por item selecionado, se a Unidade de Medida Comercial \(COD\_MEDIDA\) é igual a Unidade de Medida \(Tonelada\) informada na tela de geração\. Se for igual, não há necessidade de conversão\. Se for diferente, a quantidade a ser considerada será a convertida conforme Fator de Conversão informado na tela de Parâmetros de Conversão de Unidades de Medida Padrão \(Módulo MasterSAF DW / Menu Manutenção > Cadastros > Conversão de Unidades de Medida > Padrão\)\. A quantidade a ser somada será aquela resultado do cálculo: Quantidade \* Fator de Conversão, considerando o registro que tenha a Unidade Origem igual a informada no Item selecionado e a Unidade Destino igual a parametrizada na tela de geração\.

Será gerado com 4 decimais, que serão as 4 últimas posições do campo\.

MFS\-1864

RN02\-10

Campo 10 Valor de Mercadoria para Produtos Importados

Este campo irá somar os Valores do Produto \(VLR\_ITEM\) da SAFX08, considerando registros que tenham CFOP\(s\) parametrizados pelo usuário no seguinte caminho: Parâmetros >  Definição dos Movimentos, e que estes CFOP\(s\) estejam associados ao Parâmetro “3 – Importação”\.

Será gerado com 2 decimais, que serão as duas últimas posições do campo\.

MFS\-1864

RN02\-11

Campo 11 Valor Total de Mercadoria para Produtos Importados

Este campo irá somar o Valor Contábil do Item \(VLR\_CONTAB\_ITEM\) da SAFX08, considerando registros que tenham CFOP\(s\) parametrizados pelo usuário no seguinte caminho: Parâmetros >  Definição dos Movimentos, e que estes CFOP\(s\) estejam associados ao Parâmetro “3 – Importação”\.

Será gerado com 2 decimais, que serão as duas últimas posições do campo\.

MFS\-1864

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

